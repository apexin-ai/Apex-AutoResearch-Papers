# analysis statistical tests

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 33
- **Recorded user turns:** 0
- **Tool calls:** 16
- **Original source:** `logs/chats/worker_analysis_statistical_tests_20260524T223529.jsonl`
- **Structured JSON:** [`3665a1447628326c9e7a.json`](../../sessions/36/3665a1447628326c9e7a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

33 recorded events

### Tool call

_source line 1 · 2026-05-24T22:40:22.513033+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__register_artifact",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_statistical_tests_20260524T223529",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__register_artifact",
    "max_results": "2"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-24T22:40:22.513404+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_statistical_tests_20260524T223529",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-24T22:40:22.513576+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "occsafe_vla",
  "limit": "0",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_statistical_tests_20260524T223529",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "occsafe_vla",
    "limit": "0",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-24T22:40:22.514484+00:00_

Error: result (154,144 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-projects-occsafe-vla/7c924c41-8db0-4fbb-8f32-9f62fe9dcb1b/tool-results/mcp-agent-ml-research-read_registry-1779662145183.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-projects-occsafe-vla/7c924c41-8db0-4fbb-8f32-9f62fe9dcb1b/tool-results/mcp-agent-ml-research-read_registry-1779662145183.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_statistical_tests_20260524T223529",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-24T22:40:22.514726+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-projects-occsafe-vla/7c924c41-8db0-4fbb-8f32-9f62fe9dcb1b/tool-results/mcp-agent-ml-research-read_registry-1779662145183.txt | python3 -c \"\nimport json, sys\n\ndata = json.loads(sys.stdin.read())\nexperiments = json.loads(data['result'])\n\n# Extract exp_id and metrics for completed evals\nresults = []\nfor exp in experiments:\n    exp_id = exp.get('exp_id', '')\n    metrics = exp.get('metrics', {})\n    status = exp.get('status', '')\n    if metrics and ('CAR' in metrics or 'car' in metrics or 'TSR' in metrics or 'tsr' in metrics):\n        car = metrics.get('CAR', metrics.get('car', None))\n        tsr = metrics.get('TSR', metrics.get('tsr', None))\n        results.append({'exp_id': exp_id, 'car': car, 'tsr': tsr, 'status': status})\n\nprint(json.dumps(results, indent=2))\nprint(f'\\nTotal experiments with metrics: {len(results)}')\n\"\n",
  "description": "Extract exp_id and CAR/TSR metrics from registry data"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_statistical_tests_20260524T223529",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-projects-occsafe-vla/7c924c41-8db0-4fbb-8f32-9f62fe9dcb1b/tool-results/mcp-agent-ml-research-read_registry-1779662145183.txt | python3 -c \"\nimport json, sys\n\ndata = json.loads(sys.stdin.read())\nexperiments = json.loads(data['result'])\n\n# Extract exp_id and metrics for completed evals\nresults = []\nfor exp in experiments:\n    exp_id = exp.get('exp_id', '')\n    metrics = exp.get('metrics', {})\n    status = exp.get('status', '')\n    if metrics and ('CAR' in metrics or 'car' in metrics or 'TSR' in metrics or 'tsr' in metrics):\n        car = metrics.get('CAR', metrics.get('car', None))\n        tsr = metrics.get('TSR', metrics.get('tsr', None))\n        results.append({'exp_id': exp_id, 'car': car, 'tsr': tsr, 'status': status})\n\nprint(json.dumps(results, indent=2))\nprint(f'\\nTotal experiments with metrics: {len(results)}')\n\"\n",
    "description": "Extract exp_id and CAR/TSR metrics from registry data"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-24T22:40:22.514884+00:00_

Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 10, in &lt;module>
    exp_id = exp.get('exp_id', '')
             ^^^^^^^
AttributeError: 'str' object has no attribute 'get'

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_statistical_tests_20260524T223529",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-24T22:40:22.515019+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-projects-occsafe-vla/7c924c41-8db0-4fbb-8f32-9f62fe9dcb1b/tool-results/mcp-agent-ml-research-read_registry-1779662145183.txt | python3 -c \"\nimport json, sys\n\ndata = json.loads(sys.stdin.read())\nresult = data['result']\n# Check what type result is\nif isinstance(result, str):\n    experiments = json.loads(result)\nelse:\n    experiments = result\n\nprint(f'Type: {type(experiments)}')\nif isinstance(experiments, list):\n    print(f'Length: {len(experiments)}')\n    if len(experiments) > 0:\n        print(f'First item type: {type(experiments[0])}')\n        if isinstance(experiments[0], dict):\n            print(f'First item keys: {list(experiments[0].keys())}')\n            print(json.dumps(experiments[0], indent=2, default=str)[:2000])\n        else:\n            print(f'First item: {str(experiments[0])[:500]}')\nelif isinstance(experiments, dict):\n    print(f'Keys: {list(experiments.keys())}')\n\" 2>&1 | head -80\n",
  "description": "Inspect registry data structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_statistical_tests_20260524T223529",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-projects-occsafe-vla/7c924c41-8db0-4fbb-8f32-9f62fe9dcb1b/tool-results/mcp-agent-ml-research-read_registry-1779662145183.txt | python3 -c \"\nimport json, sys\n\ndata = json.loads(sys.stdin.read())\nresult = data['result']\n# Check what type result is\nif isinstance(result, str):\n    experiments = json.loads(result)\nelse:\n    experiments = result\n\nprint(f'Type: {type(experiments)}')\nif isinstance(experiments, list):\n    print(f'Length: {len(experiments)}')\n    if len(experiments) > 0:\n        print(f'First item type: {type(experiments[0])}')\n        if isinstance(experiments[0], dict):\n            print(f'First item keys: {list(experiments[0].keys())}')\n            print(json.dumps(experiments[0], indent=2, default=str)[:2000])\n        else:\n            print(f'First item: {str(experiments[0])[:500]}')\nelif isinstance(experiments, dict):\n    print(f'Keys: {list(experiments.keys())}')\n\" 2>&1 | head -80\n",
    "description": "Inspect registry data structure"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-24T22:40:22.515160+00:00_

Type: &lt;class 'dict'>
Keys: ['success', 'data', 'error', 'metadata']

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_statistical_tests_20260524T223529",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-24T22:40:22.515288+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-projects-occsafe-vla/7c924c41-8db0-4fbb-8f32-9f62fe9dcb1b/tool-results/mcp-agent-ml-research-read_registry-1779662145183.txt | python3 -c \"\nimport json, sys\n\ndata = json.loads(sys.stdin.read())\nresult = json.loads(data['result'])\nexperiments = result['data']\n\nprint(f'Total experiments: {len(experiments)}')\nprint(f'First exp keys: {list(experiments[0].keys())}')\nprint()\n\n# Extract all experiments with CAR/TSR metrics\nresults = []\nfor exp in experiments:\n    exp_id = exp.get('exp_id', '')\n    metrics = exp.get('metrics', {}) or {}\n    status = exp.get('status', '')\n    \n    car = metrics.get('CAR', metrics.get('car', None))\n    tsr = metrics.get('TSR', metrics.get('tsr', None))\n    \n    if car is not None or tsr is not None:\n        results.append({'exp_id': exp_id, 'car': car, 'tsr': tsr, 'status': status})\n\nprint(f'Experiments with CAR/TSR metrics: {len(results)}')\nprint()\nfor r in sorted(results, key=lambda x: x['exp_id']):\n    print(f\\\"{r['exp_id']:50s} CAR={r['car']}  TSR={r['tsr']}  status={r['status']}\\\")\n\"\n",
  "description": "Extract all experiments with CAR/TSR metrics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_statistical_tests_20260524T223529",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-projects-occsafe-vla/7c924c41-8db0-4fbb-8f32-9f62fe9dcb1b/tool-results/mcp-agent-ml-research-read_registry-1779662145183.txt | python3 -c \"\nimport json, sys\n\ndata = json.loads(sys.stdin.read())\nresult = json.loads(data['result'])\nexperiments = result['data']\n\nprint(f'Total experiments: {len(experiments)}')\nprint(f'First exp keys: {list(experiments[0].keys())}')\nprint()\n\n# Extract all experiments with CAR/TSR metrics\nresults = []\nfor exp in experiments:\n    exp_id = exp.get('exp_id', '')\n    metrics = exp.get('metrics', {}) or {}\n    status = exp.get('status', '')\n    \n    car = metrics.get('CAR', metrics.get('car', None))\n    tsr = metrics.get('TSR', metrics.get('tsr', None))\n    \n    if car is not None or tsr is not None:\n        results.append({'exp_id': exp_id, 'car': car, 'tsr': tsr, 'status': status})\n\nprint(f'Experiments with CAR/TSR metrics: {len(results)}')\nprint()\nfor r in sorted(results, key=lambda x: x['exp_id']):\n    print(f\\\"{r['exp_id']:50s} CAR={r['car']}  TSR={r['tsr']}  status={r['status']}\\\")\n\"\n",
    "description": "Extract all experiments with CAR/TSR metrics"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-24T22:40:22.515418+00:00_

Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 9, in &lt;module>
    print(f'First exp keys: {list(experiments[0].keys())}')
                                  ~~~~~~~~~~~^^^
KeyError: 0
Total experiments: 4

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_statistical_tests_20260524T223529",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-24T22:40:22.515540+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-projects-occsafe-vla/7c924c41-8db0-4fbb-8f32-9f62fe9dcb1b/tool-results/mcp-agent-ml-research-read_registry-1779662145183.txt | python3 -c \"\nimport json, sys\n\ndata = json.loads(sys.stdin.read())\nresult = json.loads(data['result'])\nexperiments = result['data']\n\nprint(f'Type: {type(experiments)}')\nprint(f'Keys: {list(experiments.keys()) if isinstance(experiments, dict) else \\\"list\\\"}')\nif isinstance(experiments, dict):\n    for k in list(experiments.keys())[:5]:\n        print(f'\\n--- {k} ---')\n        v = experiments[k]\n        if isinstance(v, dict):\n            print(json.dumps(v, indent=2, default=str)[:1000])\n        else:\n            print(str(v)[:500])\n\" 2>&1 | head -100\n",
  "description": "Inspect experiments dict structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_statistical_tests_20260524T223529",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-projects-occsafe-vla/7c924c41-8db0-4fbb-8f32-9f62fe9dcb1b/tool-results/mcp-agent-ml-research-read_registry-1779662145183.txt | python3 -c \"\nimport json, sys\n\ndata = json.loads(sys.stdin.read())\nresult = json.loads(data['result'])\nexperiments = result['data']\n\nprint(f'Type: {type(experiments)}')\nprint(f'Keys: {list(experiments.keys()) if isinstance(experiments, dict) else \\\"list\\\"}')\nif isinstance(experiments, dict):\n    for k in list(experiments.keys())[:5]:\n        print(f'\\n--- {k} ---')\n        v = experiments[k]\n        if isinstance(v, dict):\n            print(json.dumps(v, indent=2, default=str)[:1000])\n        else:\n            print(str(v)[:500])\n\" 2>&1 | head -100\n",
    "description": "Inspect experiments dict structure"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-24T22:40:22.515708+00:00_

Type: &lt;class 'dict'>
Keys: ['experiments', 'count', 'total', 'baseline']

--- experiments ---
{
  "cutoff_45k_s1": {
    "status": "RUNNING",
    "retry_count": 1,
    "created_at": "2026-05-24T12:30:14.875Z",
    "updated_at": "2026-05-24T21:51:36.619Z",
    "hypothesis": "Seed 43 replication of cutoff_45k_s0. Cutoff at 45K steps (gradient flow for 90% of training, only last 5K steps without gradient flow) achieved CAR=0.764 with seed 42. Multi-seed needed to verify if near-full gradient flow is truly inferior to full 50K gradient flow (Full OCC 3-seed avg 0.797).",
    "parent": "cutoff_45k_s0",
    "reproduce": {
      "finished_at": "2026-05-24T21:34:19.900Z"
    },
    "failure_reason": "process dead 5\u00d7 with no sentinel/W&B \u2014 auto-resolved as failed",
    "completed_at": "2026-05-24T21:34:21.535Z",
    "extra": {
      "hook_events": [
        {
          "event": "on_failed",
          "action": "agent",
          "ts": "2026-05-24T21:34:24.911554+00:00"
        }
      ],
      "previous_failure": {
        "conclusion": "failed"
      }
    },
    "spec": {
  

--- count ---
67

--- total ---
67

--- baseline ---
None

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_statistical_tests_20260524T223529",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-24T22:40:22.515875+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-projects-occsafe-vla/7c924c41-8db0-4fbb-8f32-9f62fe9dcb1b/tool-results/mcp-agent-ml-research-read_registry-1779662145183.txt | python3 -c \"\nimport json, sys\n\ndata = json.loads(sys.stdin.read())\nresult = json.loads(data['result'])\nexperiments = result['data']['experiments']\n\n# Extract all experiments with metrics\nresults = []\nfor exp_id, exp in experiments.items():\n    metrics = exp.get('metrics', {}) or {}\n    status = exp.get('status', '')\n    conclusion = exp.get('conclusion', '')\n    \n    car = metrics.get('CAR', metrics.get('car', None))\n    tsr = metrics.get('TSR', metrics.get('tsr', None))\n    \n    if car is not None or tsr is not None:\n        results.append({'exp_id': exp_id, 'car': car, 'tsr': tsr, 'status': status, 'conclusion': conclusion})\n\nprint(f'Experiments with CAR/TSR metrics: {len(results)}')\nprint()\nfor r in sorted(results, key=lambda x: x['exp_id']):\n    car_str = f\\\"{r['car']:.4f}\\\" if r['car'] is not None else 'None'\n    tsr_str = f\\\"{r['tsr']:.4f}\\\" if r['tsr'] is not None else 'None'\n    print(f\\\"{r['exp_id']:45s} CAR={car_str}  TSR={tsr_str}  [{r['status']}/{r['conclusion']}]\\\")\n\"\n",
  "description": "List all experiments with metrics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_statistical_tests_20260524T223529",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-projects-occsafe-vla/7c924c41-8db0-4fbb-8f32-9f62fe9dcb1b/tool-results/mcp-agent-ml-research-read_registry-1779662145183.txt | python3 -c \"\nimport json, sys\n\ndata = json.loads(sys.stdin.read())\nresult = json.loads(data['result'])\nexperiments = result['data']['experiments']\n\n# Extract all experiments with metrics\nresults = []\nfor exp_id, exp in experiments.items():\n    metrics = exp.get('metrics', {}) or {}\n    status = exp.get('status', '')\n    conclusion = exp.get('conclusion', '')\n    \n    car = metrics.get('CAR', metrics.get('car', None))\n    tsr = metrics.get('TSR', metrics.get('tsr', None))\n    \n    if car is not None or tsr is not None:\n        results.append({'exp_id': exp_id, 'car': car, 'tsr': tsr, 'status': status, 'conclusion': conclusion})\n\nprint(f'Experiments with CAR/TSR metrics: {len(results)}')\nprint()\nfor r in sorted(results, key=lambda x: x['exp_id']):\n    car_str = f\\\"{r['car']:.4f}\\\" if r['car'] is not None else 'None'\n    tsr_str = f\\\"{r['tsr']:.4f}\\\" if r['tsr'] is not None else 'None'\n    print(f\\\"{r['exp_id']:45s} CAR={car_str}  TSR={tsr_str}  [{r['status']}/{r['conclusion']}]\\\")\n\"\n",
    "description": "List all experiments with metrics"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-24T22:40:22.516016+00:00_

Experiments with CAR/TSR metrics: 16

ablation_occ_detach_s2                        CAR=0.7480  TSR=0.6240  [DONE/success]
ablation_random_occ_s2                        CAR=0.7540  TSR=0.8480  [DONE/success]
cutoff_25k_s0_eval                            CAR=0.6880  TSR=0.8440  [DONE/success]
cutoff_s0_eval                                CAR=0.7680  TSR=0.9120  [DONE/success]
cutoff_s1_eval                                CAR=0.7980  TSR=0.9180  [DONE/success]
depth_s0_eval                                 CAR=0.7360  TSR=0.9400  [DONE/success]
depth_s1_eval                                 CAR=0.8180  TSR=0.9060  [DONE/success]
depth_s2                                      CAR=0.7580  TSR=0.8600  [DONE/success]
depth_s3                                      CAR=0.8060  TSR=0.8480  [DONE/success]
mvp_occ_s0                                    CAR=0.7300  TSR=0.9100  [DONE/negative]
mvp_occ_s1                                    CAR=0.6850  TSR=0.7650  [DONE/negative]
mvp_occ_s2                                    CAR=0.7650  TSR=0.9150  [DONE/negative]
mvp_vanilla_s0                                CAR=0.7750  TSR=0.9100  [DONE/success]
mvp_vanilla_s1                                CAR=0.7650  TSR=0.9350  [DONE/success]
mvp_vanilla_s2                                CAR=0.7700  TSR=0.9100  [DONE/success]
reverse_cutoff_s0_eval                        CAR=0.7000  TSR=0.7880  [DONE/success]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_statistical_tests_20260524T223529",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-24T22:40:22.516178+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-projects-occsafe-vla/7c924c41-8db0-4fbb-8f32-9f62fe9dcb1b/tool-results/mcp-agent-ml-research-read_registry-1779662145183.txt | python3 -c \"\nimport json, sys\n\ndata = json.loads(sys.stdin.read())\nresult = json.loads(data['result'])\nexperiments = result['data']['experiments']\n\n# Check experiments that contain relevant keywords but no metrics\nkeywords = ['vanilla', 'occ', 'detach', 'random', 'depth', 'cutoff', 'reverse']\nfor exp_id, exp in sorted(experiments.items()):\n    metrics = exp.get('metrics', {}) or {}\n    car = metrics.get('CAR', metrics.get('car', None))\n    if car is None:\n        # Check if there are results or eval data in other fields\n        has_eval = 'eval' in str(exp.get('extra', '')) or 'eval' in str(exp.get('results', ''))\n        print(f\\\"{exp_id:45s} status={exp.get('status','?'):10s} conclusion={exp.get('conclusion','?')}\\\")\n\" 2>&1 | head -60\n",
  "description": "Check experiments without metrics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_statistical_tests_20260524T223529",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-projects-occsafe-vla/7c924c41-8db0-4fbb-8f32-9f62fe9dcb1b/tool-results/mcp-agent-ml-research-read_registry-1779662145183.txt | python3 -c \"\nimport json, sys\n\ndata = json.loads(sys.stdin.read())\nresult = json.loads(data['result'])\nexperiments = result['data']['experiments']\n\n# Check experiments that contain relevant keywords but no metrics\nkeywords = ['vanilla', 'occ', 'detach', 'random', 'depth', 'cutoff', 'reverse']\nfor exp_id, exp in sorted(experiments.items()):\n    metrics = exp.get('metrics', {}) or {}\n    car = metrics.get('CAR', metrics.get('car', None))\n    if car is None:\n        # Check if there are results or eval data in other fields\n        has_eval = 'eval' in str(exp.get('extra', '')) or 'eval' in str(exp.get('results', ''))\n        print(f\\\"{exp_id:45s} status={exp.get('status','?'):10s} conclusion={exp.get('conclusion','?')}\\\")\n\" 2>&1 | head -60\n",
    "description": "Check experiments without metrics"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-24T22:40:22.516329+00:00_

ablation_occ_detach_s0                        status=DONE       conclusion=success
ablation_occ_detach_s0_retrain                status=RUNNING    conclusion=?
ablation_occ_detach_s1                        status=DONE       conclusion=success
ablation_occ_detach_s2_eval                   status=DONE       conclusion=success
ablation_random_occ_s0                        status=DONE       conclusion=success
ablation_random_occ_s1                        status=DONE       conclusion=success
ablation_random_occ_s2_eval                   status=DONE       conclusion=success
cka_analysis                                  status=DONE       conclusion=success
cka_detach_ln                                 status=DONE       conclusion=success
cka_random_occ                                status=DONE       conclusion=success
cutoff_15k_s0                                 status=DONE       conclusion=success
cutoff_15k_s0_eval                            status=DONE       conclusion=success
cutoff_15k_s1                                 status=RUNNING    conclusion=?
cutoff_25k_s0                                 status=DONE       conclusion=success
cutoff_25k_s0_eval_v2                         status=DONE       conclusion=killed
cutoff_25k_s1                                 status=DONE       conclusion=success
cutoff_25k_s1_eval                            status=DONE       conclusion=success
cutoff_25k_s2                                 status=RUNNING    conclusion=?
cutoff_45k_s0                                 status=DONE       conclusion=success
cutoff_45k_s0_eval                            status=DONE       conclusion=success
cutoff_45k_s1                                 status=RUNNING    conclusion=?
cutoff_s0                                     status=DONE       conclusion=success
cutoff_s1                                     status=DONE       conclusion=success
cutoff_s2                                     status=DONE       conclusion=failed
cutoff_s2_eval                    
…[truncated 2180 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_statistical_tests_20260524T223529",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-24T22:40:22.516475+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-projects-occsafe-vla/7c924c41-8db0-4fbb-8f32-9f62fe9dcb1b/tool-results/mcp-agent-ml-research-read_registry-1779662145183.txt | python3 -c \"\nimport json, sys\n\ndata = json.loads(sys.stdin.read())\nresult = json.loads(data['result'])\nexperiments = result['data']['experiments']\n\n# Check experiments that should have eval metrics but don't appear in our metrics list\n# Look at their full structure for metrics in nested places\ncheck_ids = [\n    'ablation_occ_detach_s0', 'ablation_occ_detach_s1', \n    'ablation_random_occ_s0', 'ablation_random_occ_s1',\n    'cutoff_15k_s0_eval', 'cutoff_25k_s1_eval', 'cutoff_45k_s0_eval',\n    'cutoff_s2_v2_eval',\n    'detach_ln_s0_eval', 'detach_ln_s1_eval', 'detach_ln_s2_eval',\n    'reverse_cutoff_s1_eval',\n    'vanilla_retrain_s0_eval',\n    'occ_s1_fresh_eval_47500', 'occ_s1_fresh_eval_50000',\n    'full_occ_retrain_s0',\n    'ablation_occ_detach_s2_eval', 'ablation_random_occ_s2_eval',\n]\n\nfor eid in check_ids:\n    if eid in experiments:\n        exp = experiments[eid]\n        metrics = exp.get('metrics', {}) or {}\n        results_field = exp.get('results', {}) or {}\n        print(f'--- {eid} ---')\n        print(f'  metrics: {json.dumps(metrics, default=str)[:300]}')\n        if results_field:\n            print(f'  results: {json.dumps(results_field, default=str)[:300]}')\n        print()\n\"\n",
  "description": "Check eval experiments for nested metrics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_statistical_tests_20260524T223529",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-projects-occsafe-vla/7c924c41-8db0-4fbb-8f32-9f62fe9dcb1b/tool-results/mcp-agent-ml-research-read_registry-1779662145183.txt | python3 -c \"\nimport json, sys\n\ndata = json.loads(sys.stdin.read())\nresult = json.loads(data['result'])\nexperiments = result['data']['experiments']\n\n# Check experiments that should have eval metrics but don't appear in our metrics list\n# Look at their full structure for metrics in nested places\ncheck_ids = [\n    'ablation_occ_detach_s0', 'ablation_occ_detach_s1', \n    'ablation_random_occ_s0', 'ablation_random_occ_s1',\n    'cutoff_15k_s0_eval', 'cutoff_25k_s1_eval', 'cutoff_45k_s0_eval',\n    'cutoff_s2_v2_eval',\n    'detach_ln_s0_eval', 'detach_ln_s1_eval', 'detach_ln_s2_eval',\n    'reverse_cutoff_s1_eval',\n    'vanilla_retrain_s0_eval',\n    'occ_s1_fresh_eval_47500', 'occ_s1_fresh_eval_50000',\n    'full_occ_retrain_s0',\n    'ablation_occ_detach_s2_eval', 'ablation_random_occ_s2_eval',\n]\n\nfor eid in check_ids:\n    if eid in experiments:\n        exp = experiments[eid]\n        metrics = exp.get('metrics', {}) or {}\n        results_field = exp.get('results', {}) or {}\n        print(f'--- {eid} ---')\n        print(f'  metrics: {json.dumps(metrics, default=str)[:300]}')\n        if results_field:\n            print(f'  results: {json.dumps(results_field, default=str)[:300]}')\n        print()\n\"\n",
    "description": "Check eval experiments for nested metrics"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-24T22:40:22.516702+00:00_

--- ablation_occ_detach_s0 ---
  metrics: {"at_50000_20r": {"TSR": 0.915, "CAR": 0.715, "collisions": 57, "total_episodes": 200, "per_task": {"T0": {"TSR": 0.95, "CAR": 0.95}, "T1": {"TSR": 0.95, "CAR": 0.95}, "T2": {"TSR": 1, "CAR": 0.9}, "T3": {"TSR": 1, "CAR": 0.2}, "T4": {"TSR": 0.85, "CAR": 0.9}, "T5": {"TSR": 0.45, "CAR": 0}, "T6": {"

--- ablation_occ_detach_s1 ---
  metrics: {"at_50000_20r": {"TSR": 0.925, "CAR": 0.725, "collisions": 55, "total_episodes": 200, "per_task": {"T0": {"TSR": 1, "CAR": 0.9}, "T1": {"TSR": 1, "CAR": 0.9}, "T2": {"TSR": 1, "CAR": 0.9}, "T3": {"TSR": 1, "CAR": 0.15}, "T4": {"TSR": 0.85, "CAR": 0.95}, "T5": {"TSR": 0.45, "CAR": 0.05}, "T6": {"TSR

--- ablation_random_occ_s0 ---
  metrics: {"at_50000_20r": {"TSR": 0.84, "CAR": 0.78, "collisions": 44, "total_episodes": 200, "per_task": {"T0": {"TSR": 1, "CAR": 0.95}, "T1": {"TSR": 0.7, "CAR": 1}, "T2": {"TSR": 1, "CAR": 0.9}, "T3": {"TSR": 0.95, "CAR": 0.4}, "T4": {"TSR": 0.8, "CAR": 1}, "T5": {"TSR": 0.1, "CAR": 0.1}, "T6": {"TSR": 0.

--- ablation_random_occ_s1 ---
  metrics: {"at_50000_20r": {"TSR": 0.91, "CAR": 0.77, "collisions": 46, "total_episodes": 200, "per_task": {"T0": {"TSR": 1, "CAR": 1}, "T1": {"TSR": 0.9, "CAR": 1}, "T2": {"TSR": 1, "CAR": 0.9}, "T3": {"TSR": 1, "CAR": 0.25}, "T4": {"TSR": 0.75, "CAR": 1}, "T5": {"TSR": 0.85, "CAR": 0.45}, "T6": {"TSR": 1, "

--- cutoff_15k_s0_eval ---
  metrics: {"overall_tsr": 0.912, "overall_car": 0.804, "total_collisions": 98, "per_task_tsr": {"T0": 1, "T1": 0.98, "T2": 1, "T3": 0.96, "T4": 0.96, "T5": 0.3, "T6": 1, "T7": 0.98, "T8": 0.94, "T9": 1}, "per_task_car": {"T0": 0.98, "T1": 0.88, "T2": 0.94, "T3": 0.74, "T4": 0.94, "T5": 0.12, "T6": 0.44, "T7":

--- cutoff_25k_s1_eval ---
  metrics: {"overall_tsr": 0.93, "overall_car": 0.76, "total_collisions": 120, "total_episodes": 500, "per_task": {"T0": {"tsr": 1, "car": 0.96}, "T1": {"tsr": 1, "car": 0.96}, "T2": {"tsr": 0.94, "car": 0.9}, "T3": {"tsr": 1, "car": 0.24}, "T4": {"tsr": 0.
…[truncated 3345 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_statistical_tests_20260524T223529",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-24T22:40:22.516933+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-projects-occsafe-vla/7c924c41-8db0-4fbb-8f32-9f62fe9dcb1b/tool-results/mcp-agent-ml-research-read_registry-1779662145183.txt | python3 -c \"\nimport json, sys\n\ndata = json.loads(sys.stdin.read())\nresult = json.loads(data['result'])\nexperiments = result['data']['experiments']\n\n# Check full metrics for key experiments\ncheck_ids = ['mvp_vanilla_s0', 'mvp_vanilla_s1', 'mvp_vanilla_s2', \n             'mvp_occ_s0', 'mvp_occ_s1', 'mvp_occ_s2',\n             'occ_s1_fresh_eval_47500', 'occ_s1_fresh_eval_50000',\n             'full_occ_retrain_s0']\n\nfor eid in check_ids:\n    if eid in experiments:\n        exp = experiments[eid]\n        metrics = exp.get('metrics', {}) or {}\n        # Show top-level keys and any overall metrics\n        print(f'=== {eid} ===')\n        if isinstance(metrics, dict):\n            # Check if nested (at_XXXXX_XXr format)\n            nested_keys = [k for k in metrics.keys() if k.startswith('at_')]\n            if nested_keys:\n                for nk in nested_keys:\n                    sub = metrics[nk]\n                    print(f'  {nk}: CAR={sub.get(\\\"CAR\\\")}, TSR={sub.get(\\\"TSR\\\")}, episodes={sub.get(\\\"total_episodes\\\")}')\n            else:\n                car = metrics.get('CAR', metrics.get('car', metrics.get('overall_car')))\n                tsr = metrics.get('TSR', metrics.get('tsr', metrics.get('overall_tsr')))\n                episodes = metrics.get('total_episodes')\n                print(f'  CAR={car}, TSR={tsr}, episodes={episodes}')\n                # Show all top-level non-per_task keys\n                top_keys = [k for k in metrics.keys() if 'per_task' not in k]\n                print(f'  keys: {top_keys}')\n        print()\n\"\n",
  "description": "Check metrics structure for vanilla and occ experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_statistical_tests_20260524T223529",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-projects-occsafe-vla/7c924c41-8db0-4fbb-8f32-9f62fe9dcb1b/tool-results/mcp-agent-ml-research-read_registry-1779662145183.txt | python3 -c \"\nimport json, sys\n\ndata = json.loads(sys.stdin.read())\nresult = json.loads(data['result'])\nexperiments = result['data']['experiments']\n\n# Check full metrics for key experiments\ncheck_ids = ['mvp_vanilla_s0', 'mvp_vanilla_s1', 'mvp_vanilla_s2', \n             'mvp_occ_s0', 'mvp_occ_s1', 'mvp_occ_s2',\n             'occ_s1_fresh_eval_47500', 'occ_s1_fresh_eval_50000',\n             'full_occ_retrain_s0']\n\nfor eid in check_ids:\n    if eid in experiments:\n        exp = experiments[eid]\n        metrics = exp.get('metrics', {}) or {}\n        # Show top-level keys and any overall metrics\n        print(f'=== {eid} ===')\n        if isinstance(metrics, dict):\n            # Check if nested (at_XXXXX_XXr format)\n            nested_keys = [k for k in metrics.keys() if k.startswith('at_')]\n            if nested_keys:\n                for nk in nested_keys:\n                    sub = metrics[nk]\n                    print(f'  {nk}: CAR={sub.get(\\\"CAR\\\")}, TSR={sub.get(\\\"TSR\\\")}, episodes={sub.get(\\\"total_episodes\\\")}')\n            else:\n                car = metrics.get('CAR', metrics.get('car', metrics.get('overall_car')))\n                tsr = metrics.get('TSR', metrics.get('tsr', metrics.get('overall_tsr')))\n                episodes = metrics.get('total_episodes')\n                print(f'  CAR={car}, TSR={tsr}, episodes={episodes}')\n                # Show all top-level non-per_task keys\n                top_keys = [k for k in metrics.keys() if 'per_task' not in k]\n                print(f'  keys: {top_keys}')\n        print()\n\"\n",
    "description": "Check metrics structure for vanilla and occ experiments"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-24T22:40:22.517091+00:00_

=== mvp_vanilla_s0 ===
  at_50000_50r: CAR=0.788, TSR=0.9, episodes=500

=== mvp_vanilla_s1 ===
  at_50000_50r: CAR=0.766, TSR=0.918, episodes=500

=== mvp_vanilla_s2 ===
  at_50000_50r: CAR=0.786, TSR=0.904, episodes=500

=== mvp_occ_s0 ===
  at_47500_50r: CAR=0.75, TSR=0.892, episodes=500
  at_50000_50r: CAR=0.832, TSR=0.904, episodes=500

=== mvp_occ_s1 ===
  CAR=0.685, TSR=0.765, episodes=200
  keys: ['TSR', 'CAR', 'collisions', 'total_episodes', 'checkpoint_step', 'learning_curve']

=== mvp_occ_s2 ===
  at_47500_50r: CAR=0.788, TSR=0.9, episodes=500
  at_50000_50r: CAR=0.77, TSR=0.84, episodes=500

=== occ_s1_fresh_eval_47500 ===
  at_47500_50r: CAR=0.802, TSR=0.966, episodes=500

=== occ_s1_fresh_eval_50000 ===
  at_50000_50r: CAR=0.788, TSR=0.938, episodes=500

=== full_occ_retrain_s0 ===
  CAR=None, TSR=None, episodes=None
  keys: ['action_loss_final', 'occ_loss_final', 'total_steps']

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_statistical_tests_20260524T223529",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-24T22:40:22.517260+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-projects-occsafe-vla/7c924c41-8db0-4fbb-8f32-9f62fe9dcb1b/tool-results/mcp-agent-ml-research-read_registry-1779662145183.txt | python3 -c \"\nimport json, sys\n\ndata = json.loads(sys.stdin.read())\nresult = json.loads(data['result'])\nexperiments = result['data']['experiments']\n\n# Now get ALL experiments metrics in full detail\nall_exp_ids = sorted(experiments.keys())\nfor eid in all_exp_ids:\n    exp = experiments[eid]\n    metrics = exp.get('metrics', {}) or {}\n    if not metrics:\n        continue\n    \n    # Check for nested at_XXXXX_XXr format\n    nested_keys = [k for k in metrics.keys() if k.startswith('at_')]\n    if nested_keys:\n        for nk in nested_keys:\n            sub = metrics[nk]\n            if isinstance(sub, dict):\n                car = sub.get('CAR')\n                tsr = sub.get('TSR')\n                eps = sub.get('total_episodes')\n                if car is not None:\n                    print(f'{eid:45s} [{nk}] CAR={car:.4f} TSR={tsr:.4f} eps={eps}')\n    else:\n        # Flat metrics\n        car = metrics.get('CAR', metrics.get('overall_car'))\n        tsr = metrics.get('TSR', metrics.get('overall_tsr'))\n        eps = metrics.get('total_episodes')\n        if car is not None:\n            print(f'{eid:45s} [flat]      CAR={car:.4f} TSR={tsr:.4f} eps={eps}')\n\"\n",
  "description": "Extract all metrics with format details"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_statistical_tests_20260524T223529",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-projects-occsafe-vla/7c924c41-8db0-4fbb-8f32-9f62fe9dcb1b/tool-results/mcp-agent-ml-research-read_registry-1779662145183.txt | python3 -c \"\nimport json, sys\n\ndata = json.loads(sys.stdin.read())\nresult = json.loads(data['result'])\nexperiments = result['data']['experiments']\n\n# Now get ALL experiments metrics in full detail\nall_exp_ids = sorted(experiments.keys())\nfor eid in all_exp_ids:\n    exp = experiments[eid]\n    metrics = exp.get('metrics', {}) or {}\n    if not metrics:\n        continue\n    \n    # Check for nested at_XXXXX_XXr format\n    nested_keys = [k for k in metrics.keys() if k.startswith('at_')]\n    if nested_keys:\n        for nk in nested_keys:\n            sub = metrics[nk]\n            if isinstance(sub, dict):\n                car = sub.get('CAR')\n                tsr = sub.get('TSR')\n                eps = sub.get('total_episodes')\n                if car is not None:\n                    print(f'{eid:45s} [{nk}] CAR={car:.4f} TSR={tsr:.4f} eps={eps}')\n    else:\n        # Flat metrics\n        car = metrics.get('CAR', metrics.get('overall_car'))\n        tsr = metrics.get('TSR', metrics.get('overall_tsr'))\n        eps = metrics.get('total_episodes')\n        if car is not None:\n            print(f'{eid:45s} [flat]      CAR={car:.4f} TSR={tsr:.4f} eps={eps}')\n\"\n",
    "description": "Extract all metrics with format details"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-24T22:40:22.517418+00:00_

ablation_occ_detach_s0                        [at_50000_20r] CAR=0.7150 TSR=0.9150 eps=200
ablation_occ_detach_s0                        [at_50000_50r] CAR=0.7460 TSR=0.9140 eps=500
ablation_occ_detach_s1                        [at_50000_20r] CAR=0.7250 TSR=0.9250 eps=200
ablation_occ_detach_s1                        [at_50000_50r] CAR=0.7440 TSR=0.8980 eps=500
ablation_occ_detach_s2                        [flat]      CAR=0.7480 TSR=0.6240 eps=500
ablation_random_occ_s0                        [at_50000_20r] CAR=0.7800 TSR=0.8400 eps=200
ablation_random_occ_s0                        [at_50000_50r] CAR=0.8140 TSR=0.8560 eps=500
ablation_random_occ_s1                        [at_50000_20r] CAR=0.7700 TSR=0.9100 eps=200
ablation_random_occ_s1                        [at_50000_50r] CAR=0.7980 TSR=0.9020 eps=500
ablation_random_occ_s2                        [flat]      CAR=0.7540 TSR=0.8480 eps=500
cutoff_15k_s0_eval                            [flat]      CAR=0.8040 TSR=0.9120 eps=None
cutoff_25k_s0_eval                            [flat]      CAR=0.6880 TSR=0.8440 eps=500
cutoff_25k_s1_eval                            [flat]      CAR=0.7600 TSR=0.9300 eps=500
cutoff_45k_s0_eval                            [flat]      CAR=0.7640 TSR=0.8960 eps=500
cutoff_s0_eval                                [flat]      CAR=0.7680 TSR=0.9120 eps=500
cutoff_s1_eval                                [flat]      CAR=0.7980 TSR=0.9180 eps=500
cutoff_s2_v2_eval                             [flat]      CAR=0.7700 TSR=0.9700 eps=None
depth_s0_eval                                 [flat]      CAR=0.7360 TSR=0.9400 eps=500
depth_s1_eval                                 [flat]      CAR=0.8180 TSR=0.9060 eps=500
depth_s2                                      [flat]      CAR=0.7580 TSR=0.8600 eps=None
depth_s3                                      [flat]      CAR=0.8060 TSR=0.8480 eps=None
detach_ln_s0_eval                             [flat]      CAR=0.7920 TSR=0.9140 eps=500
detach_ln_s1_eval                   
…[truncated 1492 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_statistical_tests_20260524T223529",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-24T22:40:22.517634+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/",
  "description": "Check artifacts directory exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_statistical_tests_20260524T223529",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/",
    "description": "Check artifacts directory exists"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-24T22:40:22.517814+00:00_

_project
ablation_random_occ_s0
analyze_learning_curve_fixed.py
cka_analysis
cka_analysis.py
cka_detach_ln
cka_detach_ln.pdf
cka_detach_ln.png
cka_detach_ln_results.json
cka_random_occ_results.json
cka_results.json
comprehensive_results.csv
detach_ln_diagnosis.md
detach_ln_s0_eval
detach_ln_s0_eval_analysis.md
diag_eval_failure_20260523.md
diagnose_ablation_batch_fail.md
diagnose_westd10894_batch_kill.md
dose_response_data.json
dream_reports
eval_commands.md
eval_completeness_audit.md
extract_depth.py
factorial_2x2_config.json
figures
gradient_analysis
gradient_analysis_mixed_seed
gradient_cka_summary.md
manifest.yaml
occ_crash_diagnosis.md
occ_gt_design.md
occ_pipeline
openvla_oft_survey.md
plot_dose_response.py
plot_factorial_2x2.py
plot_gradient_comparison.py
safelibero_survey.md
same_seed_gradient_analysis.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_statistical_tests_20260524T223529",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-24T22:40:22.517977+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/compute_statistics.py",
  "content": "\"\"\"Statistical tests for all multi-seed conditions in occsafe_vla.\"\"\"\nimport json\nimport numpy as np\nfrom scipy import stats\n\n# Data extracted from registry (50-rollout evaluations at step 50000)\nCONDITIONS = {\n    \"Vanilla\": {\n        \"car\": [0.788, 0.766, 0.786],  # mvp_vanilla_s0, s1, s2\n        \"tsr\": [0.900, 0.918, 0.904],\n    },\n    \"Full_OCC\": {\n        \"car\": [0.832, 0.788, 0.770],  # mvp_occ_s0, occ_s1_fresh, mvp_occ_s2\n        \"tsr\": [0.904, 0.938, 0.840],\n    },\n    \"Detach_BN\": {\n        \"car\": [0.746, 0.744, 0.748],  # ablation_occ_detach_s0, s1, s2\n        \"tsr\": [0.914, 0.898, 0.624],\n    },\n    \"Random_OCC\": {\n        \"car\": [0.814, 0.798, 0.754],  # ablation_random_occ_s0, s1, s2\n        \"tsr\": [0.856, 0.902, 0.848],\n    },\n    \"Depth\": {\n        \"car\": [0.736, 0.818, 0.758, 0.806],  # depth_s0, s1, s2, s3\n        \"tsr\": [0.940, 0.906, 0.860, 0.848],\n    },\n    \"Cutoff_35K\": {\n        \"car\": [0.768, 0.798, 0.770],  # cutoff_s0, s1, s2_v2\n        \"tsr\": [0.912, 0.918, 0.970],\n    },\n    \"Cutoff_15K\": {\n        \"car\": [0.804],  # cutoff_15k_s0\n        \"tsr\": [0.912],\n    },\n    \"Cutoff_25K\": {\n        \"car\": [0.688, 0.760],  # cutoff_25k_s0, s1\n        \"tsr\": [0.844, 0.930],\n    },\n    \"Cutoff_45K\": {\n        \"car\": [0.764],  # cutoff_45k_s0\n        \"tsr\": [0.896],\n    },\n    \"Reverse_Cutoff\": {\n        \"car\": [0.700, 0.736],  # reverse_cutoff_s0, s1\n        \"tsr\": [0.788, 0.890],\n    },\n    \"Detach_LN\": {\n        \"car\": [0.792, 0.756, 0.748],  # detach_ln_s0, s1, s2\n        \"tsr\": [0.914, 0.906, 0.884],\n    },\n}\n\n\ndef bootstrap_ci(data, n_boot=10000, ci=0.95, rng=None):\n    if rng is None:\n        rng = np.random.default_rng(42)\n    data = np.array(data)\n    n = len(data)\n    boot_means = np.array([rng.choice(data, size=n, replace=True).mean() for _ in range(n_boot)])\n    alpha = (1 - ci) / 2\n    return float(np.percentile(boot_means, alpha * 100)), float(np.percentile(boot_means, (1 - alpha) * 100))\n\n\ndef cohens_d(group, baseline):\n    \"\"\"Cohen's d with pooled std.\"\"\"\n    g = np.array(group)\n    b = np.array(baseline)\n    n1, n2 = len(g), len(b)\n    var1, var2 = g.var(ddof=1), b.var(ddof=1)\n    pooled_std = np.sqrt(((n1 - 1) * var1 + (n2 - 1) * var2) / (n1 + n2 - 2))\n    if pooled_std == 0:\n        return 0.0\n    return float((g.mean() - b.mean()) / pooled_std)\n\n\ndef paired_ttest(group, baseline):\n    \"\"\"Paired t-test. If lengths differ, use independent t-test.\"\"\"\n    g = np.array(group)\n    b = np.array(baseline)\n    if len(g) == len(b):\n        t_stat, p_val = stats.ttest_rel(g, b)\n    else:\n        t_stat, p_val = stats.ttest_ind(g, b)\n    return float(p_val)\n\n\ndef main():\n    vanilla_car = np.array(CONDITIONS[\"Vanilla\"][\"car\"])\n    vanilla_tsr = np.array(CONDITIONS[\"Vanilla\"][\"tsr\"])\n    rng = np.random.default_rng(42)\n\n    results = {}\n    for name, data in CONDITIONS.items():\n        car = np.array(data[\"car\"])\n        tsr = np.array(data[\"tsr\"])\n        n = len(car)\n\n        entry = {\"n_seeds\": n}\n\n        if n >= 2:\n            car_ci = bootstrap_ci(car, rng=rng)\n            tsr_ci = bootstrap_ci(tsr, rng=rng)\n            entry[\"car\"] = {\n                \"mean\": round(float(car.mean()), 4),\n                \"std\": round(float(car.std(ddof=1)), 4),\n                \"ci_lower\": round(car_ci[0], 4),\n                \"ci_upper\": round(car_ci[1], 4),\n                \"seeds\": [round(x, 4) for x in car.tolist()],\n            }\n            entry[\"tsr\"] = {\n                \"mean\": round(float(tsr.mean()), 4),\n                \"std\": round(float(tsr.std(ddof=1)), 4),\n                \"ci_lower\": round(tsr_ci[0], 4),\n                \"ci_upper\": round(tsr_ci[1], 4),\n                \"seeds\": [round(x, 4) for x in tsr.tolist()],\n            }\n        else:\n            entry[\"car\"] = {\n                \"mean\": round(float(car[0]), 4),\n                \"std\": None,\n                \"ci_lower\": None,\n                \"ci_upper\": None,\n                \"seeds\": [round(x, 4) for x in car.tolist()],\n            }\n            entry[\"tsr\"] = {\n                \"mean\": round(float(tsr[0]), 4),\n                \"std\": None,\n                \"ci_lower\": None,\n                \"ci_upper\": None,\n                \"seeds\": [round(x, 4) for x in tsr.tolist()],\n            }\n\n        if name == \"Vanilla\":\n            entry[\"vs_vanilla\"] = None\n        elif n >= 2:\n            entry[\"vs_vanilla\"] = {\n                \"cohens_d_car\": round(cohens_d(car, vanilla_car), 4),\n                \"cohens_d_tsr\": round(cohens_d(tsr, vanilla_tsr), 4),\n                \"ttest_p_car\": round(paired_ttest(car, vanilla_car), 4),\n                \"ttest_p_tsr\": round(paired_ttest(tsr, vanilla_tsr), 4),\n            }\n        else:\n            entry[\"vs_vanilla\"] = \"insufficient_seeds\"\n\n        results[name] = entry\n\n    out_path = \"/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/statistical_tests.json\"\n    with open(out_path, \"w\") as f:\n        json.dump(results, f, indent=2)\n\n    # Print summary\n    print(f\"Written to {out_path}\\n\")\n    for name, entry in results.items():\n        car_mean = entry[\"car\"][\"mean\"]\n        n = entry[\"n_seeds\"]\n        if entry[\"vs_vanilla\"] and entry[\"vs_vanilla\"] != \"insufficient_seeds\":\n            d = entry[\"vs_vanilla\"][\"cohens_d_car\"]\n            p = entry[\"vs_vanilla\"][\"ttest_p_car\"]\n            print(f\"{name:15s}  n={n}  CAR={car_mean:.4f}  d={d:+.3f}  p={p:.4f}\")\n        else:\n            print(f\"{name:15s}  n={n}  CAR={car_mean:.4f}\")\n\n\nif __name__ == \"__main__\":\n    main()\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_statistical_tests_20260524T223529",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/compute_statistics.py",
    "content": "\"\"\"Statistical tests for all multi-seed conditions in occsafe_vla.\"\"\"\nimport json\nimport numpy as np\nfrom scipy import stats\n\n# Data extracted from registry (50-rollout evaluations at step 50000)\nCONDITIONS = {\n    \"Vanilla\": {\n        \"car\": [0.788, 0.766, 0.786],  # mvp_vanilla_s0, s1, s2\n        \"tsr\": [0.900, 0.918, 0.904],\n    },\n    \"Full_OCC\": {\n        \"car\": [0.832, 0.788, 0.770],  # mvp_occ_s0, occ_s1_fresh, mvp_occ_s2\n        \"tsr\": [0.904, 0.938, 0.840],\n    },\n    \"Detach_BN\": {\n        \"car\": [0.746, 0.744, 0.748],  # ablation_occ_detach_s0, s1, s2\n        \"tsr\": [0.914, 0.898, 0.624],\n    },\n    \"Random_OCC\": {\n        \"car\": [0.814, 0.798, 0.754],  # ablation_random_occ_s0, s1, s2\n        \"tsr\": [0.856, 0.902, 0.848],\n    },\n    \"Depth\": {\n        \"car\": [0.736, 0.818, 0.758, 0.806],  # depth_s0, s1, s2, s3\n        \"tsr\": [0.940, 0.906, 0.860, 0.848],\n    },\n    \"Cutoff_35K\": {\n        \"car\": [0.768, 0.798, 0.770],  # cutoff_s0, s1, s2_v2\n        \"tsr\": [0.912, 0.918, 0.970],\n    },\n    \"Cutoff_15K\": {\n        \"car\": [0.804],  # cutoff_15k_s0\n        \"tsr\": [0.912],\n    },\n    \"Cutoff_25K\": {\n        \"car\": [0.688, 0.760],  # cutoff_25k_s0, s1\n        \"tsr\": [0.844, 0.930],\n    },\n    \"Cutoff_45K\": {\n        \"car\": [0.764],  # cutoff_45k_s0\n        \"tsr\": [0.896],\n    },\n    \"Reverse_Cutoff\": {\n        \"car\": [0.700, 0.736],  # reverse_cutoff_s0, s1\n        \"tsr\": [0.788, 0.890],\n    },\n    \"Detach_LN\": {\n        \"car\": [0.792, 0.756, 0.748],  # detach_ln_s0, s1, s2\n        \"tsr\": [0.914, 0.906, 0.884],\n    },\n}\n\n\ndef bootstrap_ci(data, n_boot=10000, ci=0.95, rng=None):\n    if rng is None:\n        rng = np.random.default_rng(42)\n    data = np.array(data)\n    n = len(data)\n    boot_means = np.array([rng.choice(data, size=n, replace=True).mean() for _ in range(n_boot)])\n    alpha = (1 - ci) / 2\n    return float(np.percentile(boot_means, alpha * 100)), float(np.percentile(boot_means, (1 - alpha) * 100))\n\n\ndef cohens_d(group, baseline):\n    \"\"\"Cohen's d with pooled std.\"\"\"\n    g = np.array(group)\n    b = np.array(baseline)\n    n1, n2 = len(g), len(b)\n    var1, var2 = g.var(ddof=1), b.var(ddof=1)\n    pooled_std = np.sqrt(((n1 - 1) * var1 + (n2 - 1) * var2) / (n1 + n2 - 2))\n    if pooled_std == 0:\n        return 0.0\n    return float((g.mean() - b.mean()) / pooled_std)\n\n\ndef paired_ttest(group, baseline):\n    \"\"\"Paired t-test. If lengths differ, use independent t-test.\"\"\"\n    g = np.array(group)\n    b = np.array(baseline)\n    if len(g) == len(b):\n        t_stat, p_val = stats.ttest_rel(g, b)\n    else:\n        t_stat, p_val = stats.ttest_ind(g, b)\n    return float(p_val)\n\n\ndef main():\n    vanilla_car = np.array(CONDITIONS[\"Vanilla\"][\"car\"])\n    vanilla_tsr = np.array(CONDITIONS[\"Vanilla\"][\"tsr\"])\n    rng = np.random.default_rng(42)\n\n    results = {}\n    for name, data in CONDITIONS.items():\n        car = np.array(data[\"car\"])\n        tsr = np.array(data[\"tsr\"])\n        n = len(car)\n\n        entry = {\"n_seeds\": n}\n\n        if n >= 2:\n            car_ci = bootstrap_ci(car, rng=rng)\n            tsr_ci = bootstrap_ci(tsr, rng=rng)\n            entry[\"car\"] = {\n                \"mean\": round(float(car.mean()), 4),\n                \"std\": round(float(car.std(ddof=1)), 4),\n                \"ci_lower\": round(car_ci[0], 4),\n                \"ci_upper\": round(car_ci[1], 4),\n                \"seeds\": [round(x, 4) for x in car.tolist()],\n            }\n            entry[\"tsr\"] = {\n                \"mean\": round(float(tsr.mean()), 4),\n                \"std\": round(float(tsr.std(ddof=1)), 4),\n                \"ci_lower\": round(tsr_ci[0], 4),\n                \"ci_upper\": round(tsr_ci[1], 4),\n                \"seeds\": [round(x, 4) for x in tsr.tolist()],\n            }\n        else:\n            entry[\"car\"] = {\n                \"mean\": round(float(car[0]), 4),\n                \"std\": None,\n                \"ci_lower\": None,\n                \"ci_upper\": None,\n                \"seeds\": [round(x, 4) for x in car.tolist()],\n            }\n            entry[\"tsr\"] = {\n                \"mean\": round(float(tsr[0]), 4),\n                \"std\": None,\n                \"ci_lower\": None,\n                \"ci_upper\": None,\n                \"seeds\": [round(x, 4) for x in tsr.tolist()],\n            }\n\n        if name == \"Vanilla\":\n            entry[\"vs_vanilla\"] = None\n        elif n >= 2:\n            entry[\"vs_vanilla\"] = {\n                \"cohens_d_car\": round(cohens_d(car, vanilla_car), 4),\n                \"cohens_d_tsr\": round(cohens_d(tsr, vanilla_tsr), 4),\n                \"ttest_p_car\": round(paired_ttest(car, vanilla_car), 4),\n                \"ttest_p_tsr\": round(paired_ttest(tsr, vanilla_tsr), 4),\n            }\n        else:\n            entry[\"vs_vanilla\"] = \"insufficient_seeds\"\n\n        results[name] = entry\n\n    out_path = \"/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/statistical_tests.json\"\n    with open(out_path, \"w\") as f:\n        json.dump(results, f, indent=2)\n\n    # Print summary\n    print(f\"Written to {out_path}\\n\")\n    for name, entry in results.items():\n        car_mean = entry[\"car\"][\"mean\"]\n        n = entry[\"n_seeds\"]\n        if entry[\"vs_vanilla\"] and entry[\"vs_vanilla\"] != \"insufficient_seeds\":\n            d = entry[\"vs_vanilla\"][\"cohens_d_car\"]\n            p = entry[\"vs_vanilla\"][\"ttest_p_car\"]\n            print(f\"{name:15s}  n={n}  CAR={car_mean:.4f}  d={d:+.3f}  p={p:.4f}\")\n        else:\n            print(f\"{name:15s}  n={n}  CAR={car_mean:.4f}\")\n\n\nif __name__ == \"__main__\":\n    main()\n"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-24T22:40:22.518173+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/compute_statistics.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_statistical_tests_20260524T223529",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-24T22:40:22.518298+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts && python3 compute_statistics.py",
  "description": "Run statistical tests script"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_statistical_tests_20260524T223529",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts && python3 compute_statistics.py",
    "description": "Run statistical tests script"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-24T22:40:22.518435+00:00_

Written to /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/statistical_tests.json

Vanilla          n=3  CAR=0.7800
Full_OCC         n=3  CAR=0.7967  d=+0.691  p=0.4420
Detach_BN        n=3  CAR=0.7460  d=-3.900  p=0.0308
Random_OCC       n=3  CAR=0.7887  d=+0.367  p=0.7124
Depth            n=4  CAR=0.7795  d=-0.016  p=0.9840
Cutoff_35K       n=3  CAR=0.7787  d=-0.091  p=0.9437
Cutoff_15K       n=1  CAR=0.8040
Cutoff_25K       n=2  CAR=0.7240  d=-1.805  p=0.1425
Cutoff_45K       n=1  CAR=0.7640
Reverse_Cutoff   n=2  CAR=0.7180  d=-3.495  p=0.0314
Detach_LN        n=3  CAR=0.7653  d=-0.785  p=0.3568

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_statistical_tests_20260524T223529",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-24T22:40:22.518574+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/statistical_tests.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_statistical_tests_20260524T223529",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/statistical_tests.json"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-24T22:40:22.518801+00:00_

1	{
2	  "Vanilla": {
3	    "n_seeds": 3,
4	    "car": {
5	      "mean": 0.78,
6	      "std": 0.0122,
7	      "ci_lower": 0.766,
8	      "ci_upper": 0.788,
9	      "seeds": [
10	        0.788,
11	        0.766,
12	        0.786
13	      ]
14	    },
15	    "tsr": {
16	      "mean": 0.9073,
17	      "std": 0.0095,
18	      "ci_lower": 0.9,
19	      "ci_upper": 0.918,
20	      "seeds": [
21	        0.9,
22	        0.918,
23	        0.904
24	      ]
25	    },
26	    "vs_vanilla": null
27	  },
28	  "Full_OCC": {
29	    "n_seeds": 3,
30	    "car": {
31	      "mean": 0.7967,
32	      "std": 0.0319,
33	      "ci_lower": 0.77,
34	      "ci_upper": 0.832,
35	      "seeds": [
36	        0.832,
37	        0.788,
38	        0.77
39	      ]
40	    },
41	    "tsr": {
42	      "mean": 0.894,
43	      "std": 0.0498,
44	      "ci_lower": 0.84,
45	      "ci_upper": 0.938,
46	      "seeds": [
47	        0.904,
48	        0.938,
49	        0.84
50	      ]
51	    },
52	    "vs_vanilla": {
53	      "cohens_d_car": 0.6905,
54	      "cohens_d_tsr": -0.3723,
55	      "ttest_p_car": 0.442,
56	      "ttest_p_tsr": 0.6562
57	    }
58	  },
59	  "Detach_BN": {
60	    "n_seeds": 3,
61	    "car": {
62	      "mean": 0.746,
63	      "std": 0.002,
64	      "ci_lower": 0.744,
65	      "ci_upper": 0.748,
66	      "seeds": [
67	        0.746,
68	        0.744,
69	        0.748
70	      ]
71	    },
72	    "tsr": {
73	      "mean": 0.812,
74	      "std": 0.163,
75	      "ci_lower": 0.624,
76	      "ci_upper": 0.914,
77	      "seeds": [
78	        0.914,
79	        0.898,
80	        0.624
81	      ]
82	    },
83	    "vs_vanilla": {
84	      "cohens_d_car": -3.9001,
85	      "cohens_d_tsr": -0.8257,
86	      "ttest_p_car": 0.0308,
87	      "ttest_p_tsr": 0.4125
88	    }
89	  },
90	  "Random_OCC": {
91	    "n_seeds": 3,
92	    "car": {
93	      "mean": 0.7887,
94	      "std": 0.0311,
95	      "ci_lower": 0.754,
96	      "ci_upper": 0.814,
97	      "seeds": [
98	        0.814,
99	        0.798,
100	        0.75
…[truncated 4662 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_statistical_tests_20260524T223529",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-24T22:40:22.518977+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "statistical_tests",
  "type": "data",
  "description": "Bootstrap 95% CI, Cohen's d, and paired t-test results for all multi-seed conditions vs Vanilla baseline (CAR and TSR metrics)",
  "project": "occsafe_vla",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/statistical_tests.json",
  "tags": "['statistics', 'evaluation', 'multi-seed']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_statistical_tests_20260524T223529",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "statistical_tests",
    "type": "data",
    "description": "Bootstrap 95% CI, Cohen's d, and paired t-test results for all multi-seed conditions vs Vanilla baseline (CAR and TSR metrics)",
    "project": "occsafe_vla",
    "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/statistical_tests.json",
    "tags": "['statistics', 'evaluation', 'multi-seed']"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-24T22:40:22.519127+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260524_305db7\", \"name\": \"statistical_tests\", \"type\": \"data\", \"description\": \"Bootstrap 95% CI, Cohen's d, and paired t-test results for all multi-seed conditions vs Vanilla baseline (CAR and TSR metrics)\", \"path\": \"projects/occsafe_vla/artifacts/_project/data/statistical_tests.json\", \"url\": null, \"project\": \"occsafe_vla\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-24T22:40:09.971491+00:00\", \"tags\": [\"statistics\", \"evaluation\", \"multi-seed\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/occsafe_vla/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_statistical_tests_20260524T223529",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 33 · 2026-05-24T22:40:22.519295+00:00_

完成。结果已写入 `artifacts/statistical_tests.json` 并注册。

关键发现：

| Condition | n | CAR mean | Cohen's d | p-value |
|-----------|---|----------|-----------|---------|
| Vanilla (baseline) | 3 | 0.780 | — | — |
| Full OCC | 3 | 0.797 | +0.69 | 0.442 |
| Detach+BN | 3 | 0.746 | **-3.90** | **0.031** |
| Random OCC | 3 | 0.789 | +0.37 | 0.712 |
| Depth | 4 | 0.780 | -0.02 | 0.984 |
| Cutoff@35K | 3 | 0.779 | -0.09 | 0.944 |
| Cutoff@25K | 2 | 0.724 | -1.81 | 0.143 |
| Reverse Cutoff | 2 | 0.718 | **-3.50** | **0.031** |
| Detach+LN | 3 | 0.765 | -0.79 | 0.357 |
| Cutoff@15K | 1 | 0.804 | insufficient_seeds |
| Cutoff@45K | 1 | 0.764 | insufficient_seeds |

显著差异（p<0.05）：Detach+BN 和 Reverse Cutoff 显著低于 Vanilla。Full OCC 的 effect size (d=+0.69) 为中等正向但 n=3 统计力不足（p=0.44）。

注：Cutoff@35K 实际均值为 0.779（非任务中参考值 0.792），因 cutoff_s2_v2_eval 的 CAR=0.770。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_statistical_tests_20260524T223529"
}
```

</details>

---
