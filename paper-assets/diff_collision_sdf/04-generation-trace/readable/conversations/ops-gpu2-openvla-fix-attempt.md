# ops gpu2 openvla fix attempt

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 25
- **Recorded user turns:** 0
- **Tool calls:** 12
- **Original source:** `logs/chats/worker_ops_gpu2_openvla_fix_attempt_20260525T231108.jsonl`
- **Structured JSON:** [`ad71db88415da4f07ea0.json`](../../sessions/ad/ad71db88415da4f07ea0.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

25 recorded events

### Tool call

_source line 1 · 2026-05-25T23:12:16.100888+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_gpu2_openvla_fix_attempt_20260525T231108",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-25T23:12:16.101385+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_gpu2_openvla_fix_attempt_20260525T231108",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-25T23:12:16.101688+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-35807",
  "command": "find /root/colliforce-vla -name \"*openvla*\" -o -name \"*prismatic*\" 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_gpu2_openvla_fix_attempt_20260525T231108",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-35807",
    "command": "find /root/colliforce-vla -name \"*openvla*\" -o -name \"*prismatic*\" 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-25T23:12:16.101905+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_gpu2_openvla_fix_attempt_20260525T231108",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-25T23:12:16.102092+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-35807",
  "command": "ls -la /root/autodl-tmp/openvla-7b-raw/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_gpu2_openvla_fix_attempt_20260525T231108",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-35807",
    "command": "ls -la /root/autodl-tmp/openvla-7b-raw/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-25T23:12:16.102289+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 14729292\\ndrwxr-xr-x  2 root root       4096 May 25 16:39 .\\ndrwxr-xr-x 14 root root       4096 May 25 14:48 ..\\n-rw-r--r--  1 root root      60712 May 25 16:39 config.json\\n-rw-r--r--  1 root root        136 May 25 16:39 generation_config.json\\n-rw-r--r--  1 root root 6948961960 May 25 16:09 model-00001-of-00003.safetensors\\n-rw-r--r--  1 root root        987 May 25 16:09 model-00001-of-00003.safetensors.aria2\\n-rw-r--r--  1 root root 6971232040 May 25 16:23 model-00002-of-00003.safetensors\\n-rw-r--r--  1 root root       1130 May 25 16:23 model-00002-of-00003.safetensors.aria2\\n-rw-r--r--  1 root root 1162406824 May 25 16:37 model-00003-of-00003.safetensors\\n-rw-r--r--  1 root root        237 May 25 16:37 model-00003-of-00003.safetensors.aria2\\n-rw-r--r--  1 root root      94764 May 25 16:39 model.safetensors.index.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.97}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_gpu2_openvla_fix_attempt_20260525T231108",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-25T23:12:16.102499+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-35807",
  "command": "find /root/colliforce-vla -name \"eval_*openvla*\" -o -name \"eval_*vla*\" -o -name \"eval_safelibero*\" 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_gpu2_openvla_fix_attempt_20260525T231108",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-35807",
    "command": "find /root/colliforce-vla -name \"eval_*openvla*\" -o -name \"eval_*vla*\" -o -name \"eval_safelibero*\" 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-25T23:12:16.102698+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_gpu2_openvla_fix_attempt_20260525T231108",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-25T23:12:16.102924+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-35807",
  "command": "find /root/colliforce-vla -name \"*openvla*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_gpu2_openvla_fix_attempt_20260525T231108",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-35807",
    "command": "find /root/colliforce-vla -name \"*openvla*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-25T23:12:16.103123+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_gpu2_openvla_fix_attempt_20260525T231108",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-25T23:12:16.103266+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-35807",
  "command": "find /root/colliforce-vla -name \"*prismatic*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_gpu2_openvla_fix_attempt_20260525T231108",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-35807",
    "command": "find /root/colliforce-vla -name \"*prismatic*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-25T23:12:16.103394+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.49}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_gpu2_openvla_fix_attempt_20260525T231108",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-25T23:12:16.103559+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-35807",
  "command": "find /root/colliforce-vla -name \"eval_safelibero*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_gpu2_openvla_fix_attempt_20260525T231108",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-35807",
    "command": "find /root/colliforce-vla -name \"eval_safelibero*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-25T23:12:16.103721+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/colliforce-vla/scripts/eval_safelibero.py\\n/root/colliforce-vla/scripts/eval_safelibero.py.bak\\n/root/colliforce-vla/scripts/__pycache__/eval_safelibero.cpython-310.pyc\\n/root/colliforce-vla/scripts/__pycache__/eval_safelibero.cpython-312.pyc\\n/root/colliforce-vla/scripts/eval_safelibero.py.v10_bak\\n/root/colliforce-vla/scripts/eval_safelibero.py.pre_v11_bak\\n/root/colliforce-vla/scripts/eval_safelibero.py.v11_bak\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_gpu2_openvla_fix_attempt_20260525T231108",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-25T23:12:16.103861+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-35807",
  "command": "grep -r \"openvla\" /root/colliforce-vla/scripts/ --include=\"*.py\" -l",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_gpu2_openvla_fix_attempt_20260525T231108",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-35807",
    "command": "grep -r \"openvla\" /root/colliforce-vla/scripts/ --include=\"*.py\" -l",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-25T23:12:16.103990+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_gpu2_openvla_fix_attempt_20260525T231108",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-25T23:12:16.104125+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-35807",
  "command": "grep -n \"model_type\\|openvla\\|OpenVLA\\|model_name\\|argparse\\|add_argument\" /root/colliforce-vla/scripts/eval_safelibero.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_gpu2_openvla_fix_attempt_20260525T231108",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-35807",
    "command": "grep -n \"model_type\\|openvla\\|OpenVLA\\|model_name\\|argparse\\|add_argument\" /root/colliforce-vla/scripts/eval_safelibero.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-25T23:12:16.104247+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_gpu2_openvla_fix_attempt_20260525T231108",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-25T23:12:16.104371+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-35807",
  "command": "head -80 /root/colliforce-vla/scripts/eval_safelibero.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_gpu2_openvla_fix_attempt_20260525T231108",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-35807",
    "command": "head -80 /root/colliforce-vla/scripts/eval_safelibero.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-25T23:12:16.104584+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\\"\\\"\\\"\\nEvaluate a VLA model on SafeLIBERO benchmark.\\nSupports three model types:\\n  - baseline: Standard openpi pi0 LoRA fine-tune\\n  - a1: pi0 + SDF decoder + EE extractor (auxiliary task; inference identical to baseline)\\n  - a3: pi0 + SDF decoder + EE extractor + SDF Gradient Refiner (inference-time refinement)\\n\\nMeasures: Collision Avoidance Rate (CAR), Task Success Rate (TSR), trajectory smoothness, EE displacement.\\n\\nUsage:\\n    # Evaluate baseline\\n    python scripts/eval_safelibero.py \\\\\\n        --checkpoint /root/autodl-tmp/checkpoints/baseline_spatial_bowl_0 \\\\\\n        --config_name baseline_spatial_bowl \\\\\\n        --suite safelibero_spatial \\\\\\n        --task_id 0 \\\\\\n        --safety_level II \\\\\\n        --n_episodes 50\\n\\n    # Evaluate A1 (same inference as baseline, loads SDF modules for analysis)\\n    python scripts/eval_safelibero.py \\\\\\n        --model_type a1 \\\\\\n        --checkpoint /root/autodl-tmp/checkpoints/a1_sdf_spatial_bowl/a1_sdf_spatial_bowl_seed0/1000 \\\\\\n        --config_name baseline_spatial_bowl \\\\\\n        --suite safelibero_spatial \\\\\\n        --task_id 0 \\\\\\n        --n_episodes 50\\n\\n    # Evaluate A3 (inference-time SDF gradient refinement)\\n    python scripts/eval_safelibero.py \\\\\\n        --model_type a3 \\\\\\n        --checkpoint /root/autodl-tmp/checkpoints/a3_grad_refine_spatial_bowl/... \\\\\\n        --config_name baseline_spatial_bowl \\\\\\n        --sdf_gt_path /root/colliforce-vla/data/sdf_gt_spatial_bowl.npz \\\\\\n        --suite safelibero_spatial \\\\\\n        --task_id 0 \\\\\\n        --refine_alpha 0.1 \\\\\\n        --refine_margin 0.01 \\\\\\n        --n_episodes 50\\n\\n    # Evaluate with default openpi LIBERO policy\\n    python scripts/eval_safelibero.py \\\\\\n        --default_policy \\\\\\n        --suite safelibero_object \\\\\\n        --task_id 1 \\\\\\n        --n_episodes 
…[truncated 1180 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_gpu2_openvla_fix_attempt_20260525T231108",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-25T23:12:16.104736+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-35807",
  "command": "ls /root/autodl-tmp/openvla-7b-raw/*.aria2",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_gpu2_openvla_fix_attempt_20260525T231108",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-35807",
    "command": "ls /root/autodl-tmp/openvla-7b-raw/*.aria2",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-25T23:12:16.104864+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/openvla-7b-raw/model-00001-of-00003.safetensors.aria2\\n/root/autodl-tmp/openvla-7b-raw/model-00002-of-00003.safetensors.aria2\\n/root/autodl-tmp/openvla-7b-raw/model-00003-of-00003.safetensors.aria2\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_gpu2_openvla_fix_attempt_20260525T231108",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-25T23:12:16.105009+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-35807",
  "command": "cat /root/autodl-tmp/openvla-7b-raw/model-00001-of-00003.safetensors.aria2",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_gpu2_openvla_fix_attempt_20260525T231108",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-35807",
    "command": "cat /root/autodl-tmp/openvla-7b-raw/model-00001-of-00003.safetensors.aria2",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-25T23:12:16.105174+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\u0000\\u0001\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0010\\u0000\\u0000\\u0000\\u0000\\u0000\\u0001�0��\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0003=���������������������������������������������������������������������������������������������������������������������������������������������������������������\\u0000\\u000f��\\u000f���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������\\u000f���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������\\u0000?��������������������������������������������������\\u0000�����������������������������������������������\\u0000\\u0000\\u0000\\u0006\\u0000\\u0000\\u0004�\\u0000\\u0010\\u0000\\u0000\\u0000\\u0000\\u0000\\b���\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0000\\u0005\\u0017\\u0000\\u0010\\u0000\\u0000\\u0000\\u0000\\u0000\\b�������\\u0000\\u0000\\u0000\\r\\u0018\\u0000\\u0010\\u0000\\u0000\\u0000\\u0000\\u0000\\b��������\\u0000\\u0000\\u0016�\\u0000\\u0010\\u0000\\u0000\\u0000\\u0000\\u0000\\b������\\u0000\\u0000\\u0000\\u0000\\u0018c\\u0000\\u0010\\u0000\\u0000\\u0000\\u0000\\u0000\\b�������\\u0000\\u0000\\u0000\\u0018�\\u0000\\u0010\\u0000\\u0000\\u0000\\u0000\\u0000\\b�������\\u0000\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_gpu2_openvla_fix_attempt_20260525T231108",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-25T23:12:16.105374+00:00_

汇报结果：

## OpenVLA Eval 诊断结果: **NO** — 30 分钟内无法跑起来

### 1. 模型文件：不完整，无法加载
- **safetensors 下载未完成**：3 个 shard 文件均有 `.aria2` 控制文件残留，说明 aria2 下载中断，文件很可能是截断/损坏的
- **缺少关键文件**：`configuration_prismatic.py`、`modeling_prismatic.py`、tokenizer 系列文件全部缺失
- 目录中仅有：`config.json`、`generation_config.json`、3 个 safetensors shard、`model.safetensors.index.json`

### 2. Eval 脚本：不存在
- `eval_safelibero_openvla.py` 不存在
- 现有 `eval_safelibero.py` 仅支持 `baseline`/`a1`/`a3` 三种模型类型，全部基于 pi0 (openpi)，不支持 OpenVLA
- 代码库中无任何 openvla 或 prismatic 相关文件

### 3. 具体阻塞点
1. **模型需重新下载** — safetensors 损坏 + 缺少 6 个必要文件（约 15GB 总量，下载时间不可控）
2. **需从零写 eval 脚本** — OpenVLA 的推理接口（`AutoModelForVision2Seq` + `AutoProcessor`）与现有 pi0 架构完全不同，无法复用现有脚本，需要编写完整的 OpenVLA 推理 + SafeLIBERO 环境交互逻辑

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_ops_gpu2_openvla_fix_attempt_20260525T231108"
}
```

</details>

---
