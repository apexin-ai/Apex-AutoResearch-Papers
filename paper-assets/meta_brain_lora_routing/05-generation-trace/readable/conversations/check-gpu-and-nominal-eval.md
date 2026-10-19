# check gpu and nominal eval

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 47
- **Recorded user turns:** 0
- **Tool calls:** 23
- **Original source:** `logs/chats/worker_check_gpu_and_nominal_eval_20260516T204327.jsonl`
- **Structured JSON:** [`47662fa76d11a9e90b78.json`](../../sessions/47/47662fa76d11a9e90b78.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

47 recorded events

### Tool call

_source line 1 · 2026-05-16T20:45:00.407699+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_gpu_and_nominal_eval_20260516T204327",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-16T20:45:00.408107+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_gpu_and_nominal_eval_20260516T204327",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-16T20:45:00.408370+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34142",
  "command": "nvidia-smi --query-gpu=index,name,utilization.gpu,memory.used,memory.total --format=csv,noheader",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_gpu_and_nominal_eval_20260516T204327",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34142",
    "command": "nvidia-smi --query-gpu=index,name,utilization.gpu,memory.used,memory.total --format=csv,noheader",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-16T20:45:00.408575+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34142",
  "command": "nvidia-smi --query-compute-apps=pid,gpu_uuid,used_memory,name --format=csv,noheader",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_gpu_and_nominal_eval_20260516T204327",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34142",
    "command": "nvidia-smi --query-compute-apps=pid,gpu_uuid,used_memory,name --format=csv,noheader",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-16T20:45:00.408725+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"0, NVIDIA RTX PRO 6000 Blackwell Server Edition, 0 %, 7799 MiB, 97887 MiB\\n1, NVIDIA RTX PRO 6000 Blackwell Server Edition, 99 %, 12851 MiB, 97887 MiB\\n2, NVIDIA RTX PRO 6000 Blackwell Server Edition, 0 %, 3 MiB, 97887 MiB\\n3, NVIDIA RTX PRO 6000 Blackwell Server Edition, 0 %, 3 MiB, 97887 MiB\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_gpu_and_nominal_eval_20260516T204327",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-16T20:45:00.408854+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34142",
  "command": "ps -p 117988 -o pid,stat,etime,cmd",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_gpu_and_nominal_eval_20260516T204327",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34142",
    "command": "ps -p 117988 -o pid,stat,etime,cmd",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-16T20:45:00.408979+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"29928, GPU-25290389-f7fd-ea20-39db-c988c0e4996e, 7790 MiB, python\\n118486, GPU-6a695ffe-974c-32d4-0e6e-7216dbc49028, 12842 MiB, python\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.58}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_gpu_and_nominal_eval_20260516T204327",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-16T20:45:00.409142+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"   PID STAT     ELAPSED CMD\\n\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_gpu_and_nominal_eval_20260516T204327",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-16T20:45:00.409278+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34142",
  "command": "ps aux | grep -E \"eval_base_no_lora|evaluate_libero\" | grep -v grep",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_gpu_and_nominal_eval_20260516T204327",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34142",
    "command": "ps aux | grep -E \"eval_base_no_lora|evaluate_libero\" | grep -v grep",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-16T20:45:00.409402+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_gpu_and_nominal_eval_20260516T204327",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-16T20:45:00.409569+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34142",
  "command": "tmux list-sessions",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_gpu_and_nominal_eval_20260516T204327",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34142",
    "command": "tmux list-sessions",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-16T20:45:00.409696+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: 'tmux' is not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_gpu_and_nominal_eval_20260516T204327",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-16T20:45:00.409813+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34142",
  "command": "find /root/meta_brain_lora_routing/ -name \"*eval*\" -type f -newer /root/meta_brain_lora_routing/phase1/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_gpu_and_nominal_eval_20260516T204327",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34142",
    "command": "find /root/meta_brain_lora_routing/ -name \"*eval*\" -type f -newer /root/meta_brain_lora_routing/phase1/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-16T20:45:00.409932+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/meta_brain_lora_routing/phase1/eval_lora_openpi.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_gpu_and_nominal_eval_20260516T204327",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-16T20:45:00.410046+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34142",
  "command": "find /root/autodl-tmp/ -name \"*eval*\" -type f -newer /root/meta_brain_lora_routing/phase1/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_gpu_and_nominal_eval_20260516T204327",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34142",
    "command": "find /root/autodl-tmp/ -name \"*eval*\" -type f -newer /root/meta_brain_lora_routing/phase1/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-16T20:45:00.410162+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.68}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_gpu_and_nominal_eval_20260516T204327",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-16T20:45:00.410273+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34142",
  "command": "ls -lt /root/meta_brain_lora_routing/eval_results/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_gpu_and_nominal_eval_20260516T204327",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34142",
    "command": "ls -lt /root/meta_brain_lora_routing/eval_results/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-16T20:45:00.410389+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"ls: cannot access '/root/meta_brain_lora_routing/eval_results/': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_gpu_and_nominal_eval_20260516T204327",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-16T20:45:00.410525+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34142",
  "command": "grep -r \"eval_base_no_lora\" /proc/29928/cmdline /proc/118486/cmdline",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_gpu_and_nominal_eval_20260516T204327",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34142",
    "command": "grep -r \"eval_base_no_lora\" /proc/29928/cmdline /proc/118486/cmdline",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-16T20:45:00.410641+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_gpu_and_nominal_eval_20260516T204327",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-16T20:45:00.410756+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34142",
  "command": "cat /proc/29928/cmdline",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_gpu_and_nominal_eval_20260516T204327",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34142",
    "command": "cat /proc/29928/cmdline",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-16T20:45:00.410881+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"python\\u0000scripts/serve_policy.py\\u0000--port\\u00008000\\u0000policy:checkpoint\\u0000--policy.config\\u0000pi0_libero\\u0000--policy.dir\\u0000/root/autodl-tmp/checkpoints/pi0_libero_finetuned_openpi_format\\u0000\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_gpu_and_nominal_eval_20260516T204327",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-16T20:45:00.410999+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34142",
  "command": "cat /proc/118486/cmdline",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_gpu_and_nominal_eval_20260516T204327",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34142",
    "command": "cat /proc/118486/cmdline",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-16T20:45:00.411145+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"python\\u0000phase1/train_lora_expert.py\\u0000--perturbation_type\\u0000universal\\u0000--gpu_id\\u00000\\u0000--checkpoint\\u0000/root/autodl-tmp/checkpoints/pi0_libero_openpi\\u0000--output_dir\\u0000/root/autodl-tmp/checkpoints/v3_lora_universal_r48\\u0000--run_prefix\\u0000v3_r48\\u0000--lora_rank\\u000048\\u0000--batch_size\\u000016\\u0000--num_train_steps\\u000010000\\u0000--no_wandb\\u0000\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_gpu_and_nominal_eval_20260516T204327",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-16T20:45:00.411313+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34142",
  "command": "find /root/meta_brain_lora_routing/ -name \"*.json\" -newer /root/meta_brain_lora_routing/phase1/eval_lora_openpi.py -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_gpu_and_nominal_eval_20260516T204327",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34142",
    "command": "find /root/meta_brain_lora_routing/ -name \"*.json\" -newer /root/meta_brain_lora_routing/phase1/eval_lora_openpi.py -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-16T20:45:00.411468+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.46}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_gpu_and_nominal_eval_20260516T204327",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-16T20:45:00.411615+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34142",
  "command": "find /root/ -maxdepth 2 -name \"*nominal*\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_gpu_and_nominal_eval_20260516T204327",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34142",
    "command": "find /root/ -maxdepth 2 -name \"*nominal*\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-16T20:45:00.411737+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/meta_brain_lora_routing/run_nominal_eval.sh\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_gpu_and_nominal_eval_20260516T204327",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-16T20:45:00.411849+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34142",
  "command": "find /tmp/ -name \"*eval*\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_gpu_and_nominal_eval_20260516T204327",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34142",
    "command": "find /tmp/ -name \"*eval*\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-16T20:45:00.412084+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/tmp/binary_eval.log\\n/tmp/diag/eval_none_libero_spatial_20260516_193538.json\\n/tmp/eval_all.log\\n/tmp/agent-ml-exit/eval_univ_r48.exit\\n/tmp/agent-ml-exit/eval_no_routing.exit\\n/tmp/agent-ml-exit/eval_univ_r16.exit\\n/tmp/patch_eval.py\\n/tmp/eval_filter_test.txt\\n/tmp/dryrun_eval.log\\n/tmp/diag2/eval_none_libero_spatial_20260516_194131.json\\n/tmp/eval_dryrun.log\\n/tmp/watchdog_eval.log\\n/tmp/eval_baseline_v5.log\\n/tmp/eval_diag.log\\n/tmp/eval_diag2.log\\n/tmp/eval_v6_final.log\\n/tmp/native_eval.log\\n/tmp/debug_eval.log\\n/tmp/direct_eval.py\\n/tmp/direct_eval.log\\n/tmp/eval_openpi_ckpt.log\\n/tmp/nominal_eval.log\\n/tmp/eval_openpi_ckpt.py\\n/tmp/native_eval.py\\n/tmp/direct_eval_v2.py\\n/tmp/direct_eval_v2.log\\n/tmp/direct_eval_v3.py\\n/tmp/direct_eval_v3.log\\n/tmp/nominal_eval_v2_nohup.log\\n/tmp/nominal_eval_v2.log\\n/tmp/direct_eval_v4.py\\n/tmp/direct_eval_v4.log\\n/tmp/debug_eval_output.log\\n/tmp/direct_eval_v5.py\\n/tmp/direct_eval_v5.log\\n/tmp/nominal_eval_v3_nohup.log\\n/tmp/nominal_eval_v3.log\\n/tmp/nominal_eval_fixed.log\\n/tmp/nominal_eval_fixed2.log\\n/tmp/nominal_eval_no_flip.log\\n/tmp/nominal_eval_debug.log\\n/tmp/openpi_wrapper_eval.log\\n/tmp/lerobot_eval.py\\n/tmp/lerobot_eval.log\\n/tmp/eval_openpi_native.py\\n/tmp/eval_openpi_native.log\\n/tmp/nominal_eval_v4.log\\n/tmp/eval_openpi_v2.py\\n/tmp/eval_openpi_v2.log\\n/tmp/eval_original_libero.log\\n/tmp/eval_openpi_wrapper.log\\n/tmp/nominal_eval_norm_fix.log\\n/tmp/eval_nohup.log\\n/tmp/eval_openpi_norm_fixed.log\\n/tmp/nominal_eval_buffer_fix.log\\n/tmp/nominal_eval_openpi.log\\n/tmp/lerobot_eval_object.log\\n/tmp/minimal_eval.py\\n/tmp/minimal_eval.log\\n/tmp/test_openpi_direct_eval.py\\n/tmp/test_openpi_eval.log\\n/tmp/test_finetuned_eval.py\\n/tmp/finetuned_eval.log\\n/tmp/eval_finetuned_v1.log\\n/tmp/openpi_client_eval_official.log\\n/tmp/eval_colocate_test.log\\n/tmp/eval_hotfix_test.log\\n/tmp/eval_base_no_lora.l
…[truncated 458 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_gpu_and_nominal_eval_20260516T204327",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-16T20:45:00.412228+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34142",
  "command": "find /root/meta_brain_lora_routing/ -name \"*.log\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_gpu_and_nominal_eval_20260516T204327",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34142",
    "command": "find /root/meta_brain_lora_routing/ -name \"*.log\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-16T20:45:00.412351+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/meta_brain_lora_routing/phase1/outputs/eval_visual_r16.log\\n/root/meta_brain_lora_routing/phase1/outputs/eval_physical_r16.log\\n/root/meta_brain_lora_routing/logs/lora_spatial_r16.log\\n/root/meta_brain_lora_routing/logs/eval_visual_expert.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_gpu_and_nominal_eval_20260516T204327",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-16T20:45:00.412489+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34142",
  "command": "find /root/ -maxdepth 3 -name \"*success*\" -o -name \"*result*\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_gpu_and_nominal_eval_20260516T204327",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34142",
    "command": "find /root/ -maxdepth 3 -name \"*success*\" -o -name \"*result*\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-16T20:45:00.412611+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_gpu_and_nominal_eval_20260516T204327",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-16T20:45:00.412746+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34142",
  "command": "tail -100 /tmp/eval_50ep_baseline.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_gpu_and_nominal_eval_20260516T204327",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34142",
    "command": "tail -100 /tmp/eval_50ep_baseline.log",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-16T20:45:00.412863+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34142",
  "command": "tail -100 /tmp/eval_base_no_lora.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_gpu_and_nominal_eval_20260516T204327",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34142",
    "command": "tail -100 /tmp/eval_base_no_lora.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-16T20:45:00.413055+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  Step 0: action[:7] = [-0.0109, 0.1057, 0.0365, 0.0052, -0.1225, -0.0004, -1.0016]\\n           range=[-1.0016, 0.1057]\\n  Step 1: action[:7] = [0.0079, 0.1067, 0.0412, 0.0064, -0.0867, 0.0019, -0.9988]\\n           range=[-0.9988, 0.1067]\\n  Step 2: action[:7] = [0.1107, 0.1988, 0.0540, 0.0061, -0.0859, 0.0018, -0.9917]\\n           range=[-0.9917, 0.1988]\\n  [Replan at step 5] chunk shape=(50, 7)\\n    chunk range: [-1.0123, 1.0218]\\n    chunk[0][:7] = [ 4.98463160e-01  5.27398140e-01  2.16261311e-02  8.03101873e-02\\n -1.46768280e-01  3.63724031e-04 -9.87023600e-01]\\n  [Replan at step 10] chunk shape=(50, 7)\\n    chunk range: [-1.0153, 1.0099]\\n    chunk[0][:7] = [ 0.51299711  0.51128869 -0.03619064  0.06190492 -0.20877512 -0.00166594\\n -0.99331867]\\n  Result: FAIL (steps=220)\\n\\n============================================================\\nEpisode 49: task='pick up the black bowl next to the ramekin and place it on the plate' seed=91\\n============================================================\\n  [Replan at step 0] chunk shape=(50, 7)\\n    chunk range: [-1.0115, 0.9856]\\n    chunk[0][:7] = [-2.53573476e-02  8.16729672e-01  2.95327503e-02  4.01119217e-04\\n -7.93143018e-02 -1.51465690e-02 -1.00412888e+00]\\n  Step 0: action[:7] = [-0.0254, 0.8167, 0.0295, 0.0004, -0.0793, -0.0151, -1.0041]\\n           range=[-1.0041, 0.8167]\\n  Step 1: action[:7] = [-0.0162, 0.8308, 0.0282, 0.0003, -0.0765, -0.0182, -0.9950]\\n           range=[-0.9950, 0.8308]\\n  Step 2: action[:7] = [-0.0106, 0.8287, 0.0205, -0.0005, -0.0707, -0.0210, -0.9996]\\n           range=[-0.9996, 0.8287]\\n  [Replan at step 5] chunk shape=(50, 7)\\n    chunk range: [-1.0119, 1.0092]\\n    chunk[0][:7] = [ 3.52661369e-02  8.25217788e-01  6.12116201e-02  3.20913472e-04\\n -7.91428679e-02 -2.32159238e-04 -9.97220107e-01]\\n  [Replan at step 10] chunk shape=(50, 7)\\n    chunk range: [-1.0065, 1.0054]\\n    chunk[0][:7] = [ 2.4364
…[truncated 5846 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_gpu_and_nominal_eval_20260516T204327",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-16T20:45:00.413280+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  [Replan at step 5] chunk shape=(50, 7)\\n    chunk range: [-1.0143, 1.0213]\\n    chunk[0][:7] = [ 5.32989264e-01  7.11893551e-01 -6.33353827e-02 -9.83647536e-03\\n  2.56194343e-04 -6.82185597e-03 -9.89392168e-01]\\n  [Replan at step 10] chunk shape=(50, 7)\\n    chunk range: [-1.0132, 1.0122]\\n    chunk[0][:7] = [ 3.92532527e-01  7.35991876e-01 -2.78380555e-01  2.20489078e-04\\n -6.30095227e-03 -2.74581661e-02 -1.00822279e+00]\\n  Result: FAIL (steps=220)\\n\\n============================================================\\nEpisode 7: task='pick up the black bowl on the stove and place it on the plate' seed=49\\n============================================================\\n  [Replan at step 0] chunk shape=(50, 7)\\n    chunk range: [-1.0074, 1.0210]\\n    chunk[0][:7] = [ 0.42578444 -0.22215837 -0.06113233 -0.00523359 -0.00144581 -0.00410756\\n -0.99327563]\\n  Step 0: action[:7] = [0.4258, -0.2222, -0.0611, -0.0052, -0.0014, -0.0041, -0.9933]\\n           range=[-0.9933, 0.4258]\\n  Step 1: action[:7] = [0.4539, -0.2434, -0.0889, -0.0073, -0.0013, -0.0083, -0.9927]\\n           range=[-0.9927, 0.4539]\\n  Step 2: action[:7] = [0.4790, -0.2692, -0.1223, -0.0108, -0.0015, -0.0134, -0.9915]\\n           range=[-0.9915, 0.4790]\\n  [Replan at step 5] chunk shape=(50, 7)\\n    chunk range: [-1.0213, 1.0161]\\n    chunk[0][:7] = [ 1.30812662e-01 -3.87736117e-01 -3.08882340e-01 -3.06651421e-04\\n -8.30304907e-03  1.32547246e-02 -9.85126816e-01]\\n  [Replan at step 10] chunk shape=(50, 7)\\n    chunk range: [-1.0234, 1.0096]\\n    chunk[0][:7] = [-0.12282836 -0.16175624 -0.57026961 -0.01719266 -0.0030442   0.01304074\\n -1.00247034]\\n  Result: SUCCESS (steps=180)\\n\\n============================================================\\nEpisode 8: task='pick up the black bowl on the wooden cabinet and place it on the plate' seed=50\\n============================================================\\n  [Replan at step 0] chun
…[truncated 3914 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_gpu_and_nominal_eval_20260516T204327",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-16T20:45:00.413453+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34142",
  "command": "cat /tmp/diag/eval_none_libero_spatial_20260516_193538.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_gpu_and_nominal_eval_20260516T204327",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34142",
    "command": "cat /tmp/diag/eval_none_libero_spatial_20260516_193538.json",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-16T20:45:00.413590+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34142",
  "command": "cat /tmp/diag2/eval_none_libero_spatial_20260516_194131.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_gpu_and_nominal_eval_20260516T204327",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34142",
    "command": "cat /tmp/diag2/eval_none_libero_spatial_20260516_194131.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-16T20:45:00.413723+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"nominal\\\": {\\n    \\\"success_rate\\\": 0.0,\\n    \\\"successes\\\": 0,\\n    \\\"total\\\": 1\\n  },\\n  \\\"_meta\\\": {\\n    \\\"routing\\\": \\\"none\\\",\\n    \\\"task_suite\\\": \\\"libero_spatial\\\",\\n    \\\"seeds\\\": [\\n      42\\n    ],\\n    \\\"num_episodes\\\": 1,\\n    \\\"timestamp\\\": \\\"20260516_193538\\\"\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_gpu_and_nominal_eval_20260516T204327",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-16T20:45:00.413855+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"nominal\\\": {\\n    \\\"success_rate\\\": 0.0,\\n    \\\"successes\\\": 0,\\n    \\\"total\\\": 1\\n  },\\n  \\\"_meta\\\": {\\n    \\\"routing\\\": \\\"none\\\",\\n    \\\"task_suite\\\": \\\"libero_spatial\\\",\\n    \\\"seeds\\\": [\\n      42\\n    ],\\n    \\\"num_episodes\\\": 1,\\n    \\\"timestamp\\\": \\\"20260516_194131\\\"\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_gpu_and_nominal_eval_20260516T204327",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-16T20:45:00.414012+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34142",
  "command": "head -50 /tmp/eval_50ep_baseline.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_gpu_and_nominal_eval_20260516T204327",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34142",
    "command": "head -50 /tmp/eval_50ep_baseline.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-16T20:45:00.414172+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-17 04:29:20,275 [INFO] Loading OpenPIMetaBrainPolicy (routing=none, no LoRA)...\\n2026-05-17 04:29:23,477 [INFO] Loading pi0_libero via openpi Policy (device=cuda:0, delta=True)\\n2026-05-17 04:29:23,477 [INFO] Using cached converted checkpoint: /root/autodl-tmp/checkpoints/pi0_libero_openpi_converted.safetensors\\n2026-05-17 04:30:00,467 [INFO] PI0Pytorch model loaded\\n2026-05-17 04:30:00,467 [INFO] Norm stats loaded: ['state', 'actions']\\n2026-05-17 04:30:00,514 [INFO] Norm stats not found in /root/meta_brain_lora_routing/assets/pi0_libero/physical-intelligence/libero, skipping.\\n2026-05-17 04:30:02,005 [INFO] OpenPI Policy built successfully (use_delta_actions=True)\\n2026-05-17 04:30:02,005 [INFO] Model loaded successfully\\n[robosuite WARNING] No private macro file found! (__init__.py:7)\\n2026-05-17 04:30:02,008 [WARNING] No private macro file found!\\n[robosuite WARNING] It is recommended to use a private macro file (__init__.py:8)\\n2026-05-17 04:30:02,008 [WARNING] It is recommended to use a private macro file\\n[robosuite WARNING] To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py (__init__.py:9)\\n2026-05-17 04:30:02,008 [WARNING] To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py\\n2026-05-17 04:30:02,065 [INFO] No OpenGL_accelerate module loaded: No module named 'OpenGL_accelerate'\\nGym has been unmaintained since 2022 and does not support NumPy 2.0 amongst other critical functionality.\\nPlease upgrade to Gymnasium, the maintained drop-in replacement of Gym, or contact the authors of your software and request that they upgrade.\\nSee the migration guide at https://gymnasium.farama.org/introduction/migration_guide/ for additional information.\\n2026-05-17 04:30:02,902 [INFO] Found 9 nominal tasks in libero_spatial\\n\\n============================================================\\nEpiso
…[truncated 2034 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_gpu_and_nominal_eval_20260516T204327",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-16T20:45:00.414312+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-34142",
  "command": "head -30 /tmp/eval_base_no_lora.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_check_gpu_and_nominal_eval_20260516T204327",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-34142",
    "command": "head -30 /tmp/eval_base_no_lora.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-16T20:45:00.414469+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-17 04:10:36,802 [INFO] Loading OpenPIMetaBrainPolicy (routing=none, no LoRA)...\\n2026-05-17 04:10:39,962 [INFO] Loading pi0_libero via openpi Policy (device=cuda:0, delta=True)\\n2026-05-17 04:10:39,962 [INFO] Using cached converted checkpoint: /root/autodl-tmp/checkpoints/pi0_libero_openpi_converted.safetensors\\n2026-05-17 04:11:19,777 [INFO] PI0Pytorch model loaded\\n2026-05-17 04:11:19,777 [INFO] Norm stats loaded: ['state', 'actions']\\n2026-05-17 04:11:19,824 [INFO] Norm stats not found in /root/meta_brain_lora_routing/assets/pi0_libero/physical-intelligence/libero, skipping.\\n2026-05-17 04:11:21,579 [INFO] OpenPI Policy built successfully (use_delta_actions=True)\\n2026-05-17 04:11:21,579 [INFO] Model loaded successfully\\n[robosuite WARNING] No private macro file found! (__init__.py:7)\\n2026-05-17 04:11:21,582 [WARNING] No private macro file found!\\n[robosuite WARNING] It is recommended to use a private macro file (__init__.py:8)\\n2026-05-17 04:11:21,582 [WARNING] It is recommended to use a private macro file\\n[robosuite WARNING] To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py (__init__.py:9)\\n2026-05-17 04:11:21,582 [WARNING] To setup, run: python /root/miniconda3/lib/python3.12/site-packages/robosuite/scripts/setup_macros.py\\n2026-05-17 04:11:21,633 [INFO] No OpenGL_accelerate module loaded: No module named 'OpenGL_accelerate'\\nGym has been unmaintained since 2022 and does not support NumPy 2.0 amongst other critical functionality.\\nPlease upgrade to Gymnasium, the maintained drop-in replacement of Gym, or contact the authors of your software and request that they upgrade.\\nSee the migration guide at https://gymnasium.farama.org/introduction/migration_guide/ for additional information.\\n2026-05-17 04:11:22,479 [INFO] Found 9 nominal tasks in libero_spatial\\n\\n============================================================\\nEpiso
…[truncated 719 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_check_gpu_and_nominal_eval_20260516T204327",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 47 · 2026-05-16T20:45:00.414683+00:00_

## 结果汇总

### GPU 使用情况

| GPU | Util | Mem | 进程 |
|-----|------|-----|------|
| 0 | 0% | 7799/97887 MiB | PID 29928: `serve_policy.py --port 8000` (pi0_libero_finetuned_openpi_format) |
| 1 | 99% | 12851/97887 MiB | PID 118486: `train_lora_expert.py --perturbation_type universal --lora_rank 48` (v3_lora_universal_r48, 10000 steps) |
| 2 | 0% | 空闲 | — |
| 3 | 0% | 空闲 | — |

4x NVIDIA RTX PRO 6000 Blackwell Server Edition (98GB each)

### PID 117988 (nominal 50-ep eval)

**已结束。** 进程不存在。无 eval 相关进程在跑。

### Nominal 50-ep Eval 结果

**文件**: `/tmp/eval_50ep_baseline.log`  
**Checkpoint**: `pi0_libero_openpi` (base, no LoRA, routing=none)  
**时间**: 2026-05-17 04:29  
**Suite**: libero_spatial (9 tasks × ~5-6 seeds each = 50 episodes)

**Success rate: 33/50 = 66.0%**

逐 episode 结果（按 task 聚合）：

| Task | 结果 (按 seed 轮次) | 成功率 |
|------|---------------------|--------|
| between plate and ramekin | ✓✗✓✓✓✓ | 5/6 |
| top drawer of wooden cabinet | ✗✓✗✓✓✓ | 4/6 |
| next to cookie box | ✓✓✓✓✓✓ | 6/6 |
| next to plate | ✓✗✓✗✓✗ | 3/6 |
| next to ramekin | ✗✓✗✓✗✓ | 3/6 |
| on cookie box | ✓✓✓✓✗— | 4/5 |
| on the ramekin | ✗✗✗✗✓— | 1/5 |
| on the stove | ✗✓✓✓✓— | 4/5 |
| on wooden cabinet | ✓✗✓✓✗— | 3/5 |

**最难 task**: "on the ramekin" (1/5 = 20%)  
**最易 task**: "next to cookie box" (6/6 = 100%)

### 另有一个 10-ep 预跑

`/tmp/eval_base_no_lora.log` — 同一 checkpoint，10 episodes，6/10 = 60.0%（与 50-ep 结果基本一致）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_check_gpu_and_nominal_eval_20260516T204327"
}
```

</details>

---
