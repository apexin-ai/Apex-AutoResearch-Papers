# analysis exp 001 eval 3B d100 s123 para aligned v2

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 53
- **Recorded user turns:** 0
- **Tool calls:** 26
- **Original source:** `logs/chats/worker_analysis_exp_001_eval_3B_d100_s123_para_aligned_v2_20260515T193308.jsonl`
- **Structured JSON:** [`dbf0cab3d3ae532c704a.json`](../../sessions/db/dbf0cab3d3ae532c704a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

53 recorded events

### Tool call

_source line 1 · 2026-05-15T19:36:18.615776+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "ssh remote server execute read",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_001_eval_3B_d100_s123_para_aligned_v2_20260515T193308",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "ssh remote server execute read",
    "max_results": "10"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-15T19:36:18.616338+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_001_eval_3B_d100_s123_para_aligned_v2_20260515T193308",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T19:36:18.616647+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "update_registry experiment",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_001_eval_3B_d100_s123_para_aligned_v2_20260515T193308",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "update_registry experiment",
    "max_results": "5"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-15T19:36:18.616887+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_001_eval_3B_d100_s123_para_aligned_v2_20260515T193308",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T19:36:18.617157+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat ~/runs/contamcal-irt-calibration/exp_001_eval_3B_d100_s123_para_aligned_v2.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_001_eval_3B_d100_s123_para_aligned_v2_20260515T193308",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat ~/runs/contamcal-irt-calibration/exp_001_eval_3B_d100_s123_para_aligned_v2.log"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-15T19:36:18.625526+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ls -la /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_s123_para_aligned/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_001_eval_3B_d100_s123_para_aligned_v2_20260515T193308",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ls -la /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_s123_para_aligned/"
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T19:36:18.625845+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ls -la /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_s123/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_001_eval_3B_d100_s123_para_aligned_v2_20260515T193308",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ls -la /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_s123/"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T19:36:18.626188+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"设置成功\\n注意：仅限于学术用途和加速访问github/huggingface，不承诺稳定性保证\\n2026-05-16 02:49:21,641 [INFO] Loading base model: /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B + adapter: /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_s123/lora_adapter\\n`torch_dtype` is deprecated! Use `dtype` instead!\\n2026-05-16 02:49:22,552 [INFO] We will use 90% of the memory on device 0 for storing the model, and 10% for the buffer to avoid OOM. You can set `max_memory` in to a higher value to use more memory (at your own risk).\\n\\rLoading checkpoint shards:   0%|          | 0/2 [00:00<?, ?it/s]\\rLoading checkpoint shards:  50%|█████     | 1/2 [00:00<00:00,  1.01it/s]\\rLoading checkpoint shards: 100%|██████████| 2/2 [00:01<00:00,  1.38it/s]\\rLoading checkpoint shards: 100%|██████████| 2/2 [00:01<00:00,  1.31it/s]\\n2026-05-16 02:49:24,156 [ERROR] bitsandbytes library load error: libnvJitLink.so.13: cannot open shared object file: No such file or directory\\nTraceback (most recent call last):\\n  File \\\"/root/miniconda3/lib/python3.12/site-packages/bitsandbytes/cextension.py\\\", line 320, in &lt;module>\\n    lib = get_native_library()\\n          ^^^^^^^^^^^^^^^^^^^^\\n  File \\\"/root/miniconda3/lib/python3.12/site-packages/bitsandbytes/cextension.py\\\", line 298, in get_native_library\\n    dll = ct.cdll.LoadLibrary(str(binary_path))\\n          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\\n  File \\\"/root/miniconda3/lib/python3.12/ctypes/__init__.py\\\", line 460, in LoadLibrary\\n    return self._dlltype(name)\\n           ^^^^^^^^^^^^^^^^^^^\\n  File \\\"/root/miniconda3/lib/python3.12/ctypes/__init__.py\\\", line 379, in __init__\\n    self._handle = _dlopen(self._name, mode)\\n                   ^^^^^^^^^^^^^^^^^^^^^^^^^\\nOSError: libnvJitLink.so.13: cannot open shared object file: No such file or directory\\n2026-05-16 02:49:26,650 [INFO] Evaluating mmlu (paraphrased)...\\n2026-05-16 02:49:27,115 [INFO] Loaded 6596 QC-passed paraphrased
…[truncated 6427 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_001_eval_3B_d100_s123_para_aligned_v2_20260515T193308",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 9
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-15T19:36:18.626525+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 1940\\ndrwxr-xr-x  2 root root     122 May 16 03:27 .\\ndrwxr-xr-x 69 root root    4096 May 16 03:27 ..\\n-rw-r--r--  1 root root       0 May 16 03:27 .done\\n-rw-r--r--  1 root root   47849 May 16 03:27 correctness_matrix.json\\n-rw-r--r--  1 root root  907449 May 16 03:27 eval_results.json\\n-rw-r--r--  1 root root 1017659 May 16 03:27 item_responses.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_001_eval_3B_d100_s123_para_aligned_v2_20260515T193308",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T19:36:18.626769+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"ls: cannot access '/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_s123/': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.41}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_001_eval_3B_d100_s123_para_aligned_v2_20260515T193308",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T19:36:18.627045+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "grep \"accuracy\\|pass@1\" ~/runs/contamcal-irt-calibration/exp_001_eval_3B_d100_s123_para_aligned_v2.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_001_eval_3B_d100_s123_para_aligned_v2_20260515T193308",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "grep \"accuracy\\|pass@1\" ~/runs/contamcal-irt-calibration/exp_001_eval_3B_d100_s123_para_aligned_v2.log"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-15T19:36:18.627303+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_001_eval_3B_d100_s123_para_aligned_v2_20260515T193308",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-15T19:36:18.635918+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "python3 -c \"import json; d=json.load(open('/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_s123_para_aligned/eval_results.json')); print(json.dumps(d, indent=2))\" 2>&1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_001_eval_3B_d100_s123_para_aligned_v2_20260515T193308",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "python3 -c \"import json; d=json.load(open('/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_s123_para_aligned/eval_results.json')); print(json.dumps(d, indent=2))\" 2>&1"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-15T19:36:18.636210+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_001_eval_3B_d100_s123_para_aligned_v2_20260515T193308",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-15T19:36:18.636459+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "find /root/autodl-tmp/exp001/eval_results/ -maxdepth 1 -type d -name \"*d100_s123*\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_001_eval_3B_d100_s123_para_aligned_v2_20260515T193308",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "find /root/autodl-tmp/exp001/eval_results/ -maxdepth 1 -type d -name \"*d100_s123*\""
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-15T19:36:18.636694+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-0.5B_d100_s123_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d100_s123_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_s123_para_aligned\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_001_eval_3B_d100_s123_para_aligned_v2_20260515T193308",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-15T19:36:18.636928+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "grep -E \"accuracy|pass@1\" ~/runs/contamcal-irt-calibration/exp_001_eval_3B_d100_s123_para_aligned_v2.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_001_eval_3B_d100_s123_para_aligned_v2_20260515T193308",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "grep -E \"accuracy|pass@1\" ~/runs/contamcal-irt-calibration/exp_001_eval_3B_d100_s123_para_aligned_v2.log"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-15T19:36:18.637136+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_001_eval_3B_d100_s123_para_aligned_v2_20260515T193308",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-15T19:36:18.645424+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "head -100 /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_s123_para_aligned/eval_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_001_eval_3B_d100_s123_para_aligned_v2_20260515T193308",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "head -100 /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_s123_para_aligned/eval_results.json"
  }
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-15T19:36:18.645856+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "find /root/autodl-tmp/exp001/eval_results/ -maxdepth 1 -type d -name \"*3B*\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_001_eval_3B_d100_s123_para_aligned_v2_20260515T193308",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "find /root/autodl-tmp/exp001/eval_results/ -maxdepth 1 -type d -name \"*3B*\""
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-15T19:36:18.646212+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"model_path\\\": \\\"/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B\\\",\\n  \\\"paraphrased\\\": true,\\n  \\\"benchmarks\\\": {\\n    \\\"mmlu\\\": {\\n      \\\"accuracy\\\": 0.6564584596725288,\\n      \\\"correct\\\": 4330,\\n      \\\"total\\\": 6596,\\n      \\\"per_item\\\": [\\n        {\\n          \\\"index\\\": 6,\\n          \\\"correct\\\": true,\\n          \\\"pred\\\": \\\"A\\\",\\n          \\\"gold\\\": \\\"A\\\"\\n        },\\n        {\\n          \\\"index\\\": 9,\\n          \\\"correct\\\": true,\\n          \\\"pred\\\": \\\"C\\\",\\n          \\\"gold\\\": \\\"C\\\"\\n        },\\n        {\\n          \\\"index\\\": 22,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"C\\\",\\n          \\\"gold\\\": \\\"D\\\"\\n        },\\n        {\\n          \\\"index\\\": 25,\\n          \\\"correct\\\": true,\\n          \\\"pred\\\": \\\"C\\\",\\n          \\\"gold\\\": \\\"C\\\"\\n        },\\n        {\\n          \\\"index\\\": 26,\\n          \\\"correct\\\": true,\\n          \\\"pred\\\": \\\"C\\\",\\n          \\\"gold\\\": \\\"C\\\"\\n        },\\n        {\\n          \\\"index\\\": 32,\\n          \\\"correct\\\": true,\\n          \\\"pred\\\": \\\"A\\\",\\n          \\\"gold\\\": \\\"A\\\"\\n        },\\n        {\\n          \\\"index\\\": 36,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"C\\\",\\n          \\\"gold\\\": \\\"D\\\"\\n        },\\n        {\\n          \\\"index\\\": 40,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"B\\\",\\n          \\\"gold\\\": \\\"C\\\"\\n        },\\n        {\\n          \\\"index\\\": 43,\\n          \\\"correct\\\": true,\\n          \\\"pred\\\": \\\"C\\\",\\n          \\\"gold\\\": \\\"C\\\"\\n        },\\n        {\\n          \\\"index\\\": 46,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"C\\\",\\n          \\\"gold\\\": \\\"B\\\"\\n        },\\n        {
…[truncated 930 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_001_eval_3B_d100_s123_para_aligned_v2_20260515T193308",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-15T19:36:18.646547+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s42\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_raw\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d005_s42_para_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_s42_para_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s42_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s42_para_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_v2_s42_para_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s42_para_aligned_v2\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_v2_s42_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s42_para_aligned_v3\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v1_s42_aligned_DEPRECATED\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d005_v1_s42_aligned_DEPRECATED\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_v1_s42_aligned_DEPRECATED\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v1_s123_DEPRECATED\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s123_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v2_s123_para_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_v2_s42_para_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_v2_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_v2_s123_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s42_v3_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_v3_s42_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s123_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d005_s42_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_s123_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d000_s42_para_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d005_s123_aligned\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d005_s123_para_aligned\\n/root/aut
…[truncated 241 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_001_eval_3B_d100_s123_para_aligned_v2_20260515T193308",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-15T19:36:18.646827+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "grep \"accuracy\\|pass@1\" ~/runs/contamcal-irt-calibration/exp_001_eval_3B_d100_s123_para_aligned_v2.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_001_eval_3B_d100_s123_para_aligned_v2_20260515T193308",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "grep \"accuracy\\|pass@1\" ~/runs/contamcal-irt-calibration/exp_001_eval_3B_d100_s123_para_aligned_v2.log"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-15T19:36:18.647061+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_001_eval_3B_d100_s123_para_aligned_v2_20260515T193308",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-15T19:36:18.647278+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "head -30 /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_v2_s123_aligned/eval_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_001_eval_3B_d100_s123_para_aligned_v2_20260515T193308",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "head -30 /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_v2_s123_aligned/eval_results.json"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-15T19:36:18.655890+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"model_path\\\": \\\"/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B\\\",\\n  \\\"paraphrased\\\": false,\\n  \\\"benchmarks\\\": {\\n    \\\"mmlu\\\": {\\n      \\\"accuracy\\\": 0.6318900441532546,\\n      \\\"correct\\\": 8873,\\n      \\\"total\\\": 14042,\\n      \\\"per_item\\\": [\\n        {\\n          \\\"index\\\": 0,\\n          \\\"correct\\\": true,\\n          \\\"pred\\\": \\\"B\\\",\\n          \\\"gold\\\": \\\"B\\\"\\n        },\\n        {\\n          \\\"index\\\": 1,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"A\\\",\\n          \\\"gold\\\": \\\"C\\\"\\n        },\\n        {\\n          \\\"index\\\": 2,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"C\\\",\\n          \\\"gold\\\": \\\"D\\\"\\n        },\\n        {\\n          \\\"index\\\": 3,\\n          \\\"correct\\\": false,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_001_eval_3B_d100_s123_para_aligned_v2_20260515T193308",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 8
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-15T19:36:18.656267+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "grep accuracy ~/runs/contamcal-irt-calibration/exp_001_eval_3B_d100_s123_para_aligned_v2.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_001_eval_3B_d100_s123_para_aligned_v2_20260515T193308",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "grep accuracy ~/runs/contamcal-irt-calibration/exp_001_eval_3B_d100_s123_para_aligned_v2.log"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-15T19:36:18.656530+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-16 02:52:28,200 [INFO] mmlu accuracy: 0.6565 (4330/6596)\\n2026-05-16 03:24:04,053 [INFO] arc_challenge accuracy: 0.8164 (569/697)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_001_eval_3B_d100_s123_para_aligned_v2_20260515T193308",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-15T19:36:18.656741+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "grep pass ~/runs/contamcal-irt-calibration/exp_001_eval_3B_d100_s123_para_aligned_v2.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_001_eval_3B_d100_s123_para_aligned_v2_20260515T193308",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "grep pass ~/runs/contamcal-irt-calibration/exp_001_eval_3B_d100_s123_para_aligned_v2.log"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-15T19:36:18.656963+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-16 02:49:27,115 [INFO] Loaded 6596 QC-passed paraphrased items for mmlu from /root/autodl-tmp/exp001/paraphrases/mmlu_paraphrases.json\\n2026-05-16 02:52:28,211 [INFO] Loaded 228 QC-passed paraphrased items for gsm8k from /root/autodl-tmp/exp001/paraphrases/gsm8k_paraphrases.json\\n2026-05-16 03:22:39,404 [INFO] Loaded 697 QC-passed paraphrased items for arc_challenge from /root/autodl-tmp/exp001/paraphrases/arc_challenge_paraphrases.json\\n2026-05-16 03:24:04,056 [INFO] Loaded 26 QC-passed paraphrased items for humaneval from /root/autodl-tmp/exp001/paraphrases/humaneval_paraphrases.json\\n2026-05-16 03:27:18,503 [INFO] humaneval pass@1: 0.0769 (2/26)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_001_eval_3B_d100_s123_para_aligned_v2_20260515T193308",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-15T19:36:18.657189+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "grep accuracy /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_v2_s123_aligned/eval_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_001_eval_3B_d100_s123_para_aligned_v2_20260515T193308",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "grep accuracy /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_v2_s123_aligned/eval_results.json"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-15T19:36:18.665559+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"      \\\"accuracy\\\": 0.6318900441532546,\\n      \\\"accuracy\\\": 0.7323730098559514,\\n      \\\"accuracy\\\": 0.8310580204778157,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_001_eval_3B_d100_s123_para_aligned_v2_20260515T193308",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 8
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-15T19:36:18.665883+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "grep pass /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_v2_s123_aligned/eval_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_001_eval_3B_d100_s123_para_aligned_v2_20260515T193308",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "grep pass /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_v2_s123_aligned/eval_results.json"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-15T19:36:18.666127+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"      \\\"pass@1\\\": 0.18292682926829268,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_001_eval_3B_d100_s123_para_aligned_v2_20260515T193308",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-15T19:36:18.666406+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "grep gsm8k ~/runs/contamcal-irt-calibration/exp_001_eval_3B_d100_s123_para_aligned_v2.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_001_eval_3B_d100_s123_para_aligned_v2_20260515T193308",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "grep gsm8k ~/runs/contamcal-irt-calibration/exp_001_eval_3B_d100_s123_para_aligned_v2.log"
  }
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-15T19:36:18.666626+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "grep accuracy /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_s123_para_aligned/eval_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_001_eval_3B_d100_s123_para_aligned_v2_20260515T193308",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "grep accuracy /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_s123_para_aligned/eval_results.json"
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-15T19:36:18.666844+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-16 02:52:28,200 [INFO] Evaluating gsm8k (paraphrased)...\\n2026-05-16 02:52:28,211 [INFO] Loaded 228 QC-passed paraphrased items for gsm8k from /root/autodl-tmp/exp001/paraphrases/gsm8k_paraphrases.json\\n2026-05-16 03:22:39,390 [INFO] gsm8k exact_match: 0.5877 (134/228)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_001_eval_3B_d100_s123_para_aligned_v2_20260515T193308",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-15T19:36:18.667074+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"      \\\"accuracy\\\": 0.6564584596725288,\\n      \\\"accuracy\\\": 0.5877192982456141,\\n      \\\"accuracy\\\": 0.8163558106169297,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_001_eval_3B_d100_s123_para_aligned_v2_20260515T193308",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-15T19:36:18.667282+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'exp_001_eval_3B_d100_s123'}",
  "project": "contamcal-irt-calibration",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_001_eval_3B_d100_s123_para_aligned_v2_20260515T193308",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'exp_001_eval_3B_d100_s123'}",
    "project": "contamcal-irt-calibration",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-15T19:36:18.674948+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.1233}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_001_eval_3B_d100_s123_para_aligned_v2_20260515T193308",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 7
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-15T19:36:18.675252+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'status': 'DONE'}",
  "project": "contamcal-irt-calibration",
  "limit": "30",
  "fields": "['exp_id', 'status', 'conclusion', 'metrics']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_001_eval_3B_d100_s123_para_aligned_v2_20260515T193308",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'status': 'DONE'}",
    "project": "contamcal-irt-calibration",
    "limit": "30",
    "fields": "['exp_id', 'status', 'conclusion', 'metrics']"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-15T19:36:18.675693+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"exp_001_eval_3B_d100_s123_para_aligned\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp_001_sft_3B_d000_v3\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp_004_sim_sweep_v6\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"exp_002_signals_3B_v3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"exp_001_sft_3B_d025_s42_a32\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"exp_001_eval_3B_d005_s123_aligned\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"mmlu_accuracy\": 0.6324, \"gsm8k_exact_match\": 0.6308, \"arc_challenge_accuracy\": 0.8242, \"humaneval_pass1\": 0.1037}}, \"exp_001_eval_3B_d025_s123_aligned\": {\"status\": \"DONE\", \"metrics\": {\"mmlu\": 0.6367, \"gsm8k\": 0.5254, \"arc_challenge\": 0.8336, \"humaneval\": 0.1585}, \"conclusion\": \"success\"}, \"exp_001_sft_3B_d100_s42_a32\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp_002_signals_3B_v2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"exp_005_noise_prop_v4\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"fits_completed\": \"25/25\", \"all_converged\": true, \"ci_width_range\": \"0.0997-0.1000\", \"monotonicity_rho\": 0.4, \"monotonicity_p\": 0.5, \"finding\": \"ME analytic model calibrated-score CI insensitive to sigma_e magnitude\"}}, \"exp_001_eval_3B_d005_s123_para_aligned\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"MMLU\": 0.6461, \"GSM8K\": 0.5, \"ARC\": 0.8192, \"HumanEval\": 0.0769}}, \"exp_001_eval_3B_d025_s123_para_aligned\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"MMLU\": 0.6615, \"GSM8K\": 0.4254, \"ARC\": 0.8121, \"HumanEval\": 0.1538}}, \"exp_001_eval_15B_d005_s123\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"mmlu\": {\"accuracy\": 0.5869, \"correct\": 8241, \"total\": 14042}, \"gsm8k\": {\"exact_match\": 0.6482, \"correct\": 855, \"t
…[truncated 4736 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_001_eval_3B_d100_s123_para_aligned_v2_20260515T193308",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-15T19:36:18.676043+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'status': 'DONE'}",
  "project": "contamcal-irt-calibration",
  "limit": "50",
  "fields": "['exp_id', 'status', 'conclusion', 'metrics']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_001_eval_3B_d100_s123_para_aligned_v2_20260515T193308",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'status': 'DONE'}",
    "project": "contamcal-irt-calibration",
    "limit": "50",
    "fields": "['exp_id', 'status', 'conclusion', 'metrics']"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-15T19:36:18.684666+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"exp_001_eval_3B_d100_s123_para_aligned\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp_001_sft_3B_d000_v3\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp_004_sim_sweep_v6\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"exp_002_signals_3B_v3\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"exp_001_sft_3B_d025_s42_a32\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"exp_001_eval_3B_d005_s123_aligned\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"mmlu_accuracy\": 0.6324, \"gsm8k_exact_match\": 0.6308, \"arc_challenge_accuracy\": 0.8242, \"humaneval_pass1\": 0.1037}}, \"exp_001_eval_3B_d025_s123_aligned\": {\"status\": \"DONE\", \"metrics\": {\"mmlu\": 0.6367, \"gsm8k\": 0.5254, \"arc_challenge\": 0.8336, \"humaneval\": 0.1585}, \"conclusion\": \"success\"}, \"exp_001_sft_3B_d100_s42_a32\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"exp_002_signals_3B_v2\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"exp_005_noise_prop_v4\": {\"status\": \"DONE\", \"conclusion\": \"negative\", \"metrics\": {\"fits_completed\": \"25/25\", \"all_converged\": true, \"ci_width_range\": \"0.0997-0.1000\", \"monotonicity_rho\": 0.4, \"monotonicity_p\": 0.5, \"finding\": \"ME analytic model calibrated-score CI insensitive to sigma_e magnitude\"}}, \"exp_001_eval_3B_d005_s123_para_aligned\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"MMLU\": 0.6461, \"GSM8K\": 0.5, \"ARC\": 0.8192, \"HumanEval\": 0.0769}}, \"exp_001_eval_3B_d025_s123_para_aligned\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"MMLU\": 0.6615, \"GSM8K\": 0.4254, \"ARC\": 0.8121, \"HumanEval\": 0.1538}}, \"exp_001_eval_15B_d005_s123\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"mmlu\": {\"accuracy\": 0.5869, \"correct\": 8241, \"total\": 14042}, \"gsm8k\": {\"exact_match\": 0.6482, \"correct\": 855, \"t
…[truncated 9535 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_001_eval_3B_d100_s123_para_aligned_v2_20260515T193308",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 8
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-15T19:36:18.685179+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_001_eval_3B_d100_s123_para_aligned_v2",
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
  "session": "worker_analysis_exp_001_eval_3B_d100_s123_para_aligned_v2_20260515T193308",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_001_eval_3B_d100_s123_para_aligned_v2",
    "field": "status",
    "value": "DONE",
    "project": "contamcal-irt-calibration"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-15T19:36:18.685479+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Cannot transition to DONE without a 'conclusion' field. Set conclusion first.\", \"metadata\": {\"elapsed_seconds\": 2.1824}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_001_eval_3B_d100_s123_para_aligned_v2_20260515T193308",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-15T19:36:18.685717+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_001_eval_3B_d100_s123_para_aligned_v2",
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
  "session": "worker_analysis_exp_001_eval_3B_d100_s123_para_aligned_v2_20260515T193308",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_001_eval_3B_d100_s123_para_aligned_v2",
    "field": "conclusion",
    "value": "success",
    "project": "contamcal-irt-calibration"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-15T19:36:18.685986+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_001_eval_3B_d100_s123_para_aligned_v2\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T18:48:19.731Z\", \"updated_at\": \"2026-05-15T19:35:40.494Z\", \"hypothesis\": \"3B d100 s123 para_aligned eval v2. Resubmit after v1 OOM on GSM8K (22%). Last missing s123 para_aligned slot for N≥16 pooled IRT. Uses alpha=16 checkpoint (D051 accepted).\", \"parent\": \"exp_001_sft_3B_d100_s123\", \"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_s123/lora_adapter\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval (para_aligned)\", \"model_name\": \"Qwen/Qwen2.5-3B\", \"seed\": 123, \"data_path\": \"/root/autodl-tmp/exp001/paraphrases\", \"data_count\": 4, \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_s123_para_aligned\", \"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=2 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_s123_para_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --paraphrase-dir /root/autodl-tmp/exp001/paraphrases --cache-dir /root/autodl-tmp/.hf_cache\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:2\"], \"pid\": 614412, \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_3B_d100_s123_para_aligned_v2.log\", \"submitted_at\": \"2026-05-15T18:49:16Z\", \"backend\": \"tmux\", \"account\": \"root\", \"hypothesis\": \"3B d100 s123 para_aligned eval v2. Resubmit after v1 silent failure (empty output dir). Tests paraphrase robustness of 100% contamination model.\", \"parent\": \"exp_001_sft_3B_d100_s123\", \"gpu_id\": \"cuda:2\"}, \"reproduce\": {\"finished_at\": \"202
…[truncated 251 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_001_eval_3B_d100_s123_para_aligned_v2_20260515T193308",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-15T19:36:18.686259+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_001_eval_3B_d100_s123_para_aligned_v2",
  "field": "metrics",
  "value": "{'mmlu': {'accuracy': 0.6565, 'correct': 4330, 'total': 6596}, 'gsm8k': {'accuracy': 0.5877, 'correct': 134, 'total': 228}, 'arc_challenge': {'accuracy': 0.8164, 'correct': 569, 'total': 697}, 'humaneval': {'pass@1': 0.0769, 'correct': 2, 'total': 26}}",
  "project": "contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_exp_001_eval_3B_d100_s123_para_aligned_v2_20260515T193308",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_001_eval_3B_d100_s123_para_aligned_v2",
    "field": "metrics",
    "value": "{'mmlu': {'accuracy': 0.6565, 'correct': 4330, 'total': 6596}, 'gsm8k': {'accuracy': 0.5877, 'correct': 134, 'total': 228}, 'arc_challenge': {'accuracy': 0.8164, 'correct': 569, 'total': 697}, 'humaneval': {'pass@1': 0.0769, 'correct': 2, 'total': 26}}",
    "project": "contamcal-irt-calibration"
  }
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-15T19:36:18.692760+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_001_eval_3B_d100_s123_para_aligned_v2",
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
  "session": "worker_analysis_exp_001_eval_3B_d100_s123_para_aligned_v2_20260515T193308",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_001_eval_3B_d100_s123_para_aligned_v2",
    "field": "status",
    "value": "DONE",
    "project": "contamcal-irt-calibration"
  }
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-15T19:36:18.693166+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_001_eval_3B_d100_s123_para_aligned_v2\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T18:48:19.731Z\", \"updated_at\": \"2026-05-15T19:35:49.597Z\", \"hypothesis\": \"3B d100 s123 para_aligned eval v2. Resubmit after v1 OOM on GSM8K (22%). Last missing s123 para_aligned slot for N≥16 pooled IRT. Uses alpha=16 checkpoint (D051 accepted).\", \"parent\": \"exp_001_sft_3B_d100_s123\", \"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_s123/lora_adapter\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval (para_aligned)\", \"model_name\": \"Qwen/Qwen2.5-3B\", \"seed\": 123, \"data_path\": \"/root/autodl-tmp/exp001/paraphrases\", \"data_count\": 4, \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_s123_para_aligned\", \"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=2 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_s123_para_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --paraphrase-dir /root/autodl-tmp/exp001/paraphrases --cache-dir /root/autodl-tmp/.hf_cache\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:2\"], \"pid\": 614412, \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_3B_d100_s123_para_aligned_v2.log\", \"submitted_at\": \"2026-05-15T18:49:16Z\", \"backend\": \"tmux\", \"account\": \"root\", \"hypothesis\": \"3B d100 s123 para_aligned eval v2. Resubmit after v1 silent failure (empty output dir). Tests paraphrase robustness of 100% contamination model.\", \"parent\": \"exp_001_sft_3B_d100_s123\", \"gpu_id\": \"cuda:2\"}, \"reproduce\": {\"finished_at\": \"202
…[truncated 550 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_001_eval_3B_d100_s123_para_aligned_v2_20260515T193308",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 6
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-15T19:36:18.696870+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_001_eval_3B_d100_s123_para_aligned_v2\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T18:48:19.731Z\", \"updated_at\": \"2026-05-15T19:35:54.736Z\", \"hypothesis\": \"3B d100 s123 para_aligned eval v2. Resubmit after v1 OOM on GSM8K (22%). Last missing s123 para_aligned slot for N≥16 pooled IRT. Uses alpha=16 checkpoint (D051 accepted).\", \"parent\": \"exp_001_sft_3B_d100_s123\", \"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_s123/lora_adapter\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval (para_aligned)\", \"model_name\": \"Qwen/Qwen2.5-3B\", \"seed\": 123, \"data_path\": \"/root/autodl-tmp/exp001/paraphrases\", \"data_count\": 4, \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_s123_para_aligned\", \"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=2 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d100_s123_para_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --paraphrase-dir /root/autodl-tmp/exp001/paraphrases --cache-dir /root/autodl-tmp/.hf_cache\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:2\"], \"pid\": 614412, \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_3B_d100_s123_para_aligned_v2.log\", \"submitted_at\": \"2026-05-15T18:49:16Z\", \"backend\": \"tmux\", \"account\": \"root\", \"hypothesis\": \"3B d100 s123 para_aligned eval v2. Resubmit after v1 silent failure (empty output dir). Tests paraphrase robustness of 100% contamination model.\", \"parent\": \"exp_001_sft_3B_d100_s123\", \"gpu_id\": \"cuda:2\", \"wall_clock_seconds\": 2798.7, \"gpu_hours\
…[truncated 696 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_exp_001_eval_3B_d100_s123_para_aligned_v2_20260515T193308",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 4
}
```

</details>

---

### Assistant

_source line 53 · 2026-05-15T19:36:18.697282+00:00_

Registry 已更新为 DONE/success。

## 实验结果

**状态**: success — 正常完成（EXIT_CODE=0，.done sentinel 已写入）

### Para-aligned 指标 (d100, s123)

| Benchmark | Accuracy | Correct/Total |
|-----------|----------|---------------|
| MMLU | 0.6565 | 4330/6596 |
| GSM8K | 0.5877 | 134/228 |
| ARC-Challenge | 0.8164 | 569/697 |
| HumanEval pass@1 | 0.0769 | 2/26 |

### 与 aligned 版本对比

对比对象：`exp_001_eval_3B_d100_v2_s123_aligned`（同 checkpoint，原题评估）

| Benchmark | Aligned | Para-aligned | Δ |
|-----------|---------|-------------|------|
| MMLU | 0.6319 | 0.6565 | +2.5pp* |
| GSM8K | 0.7324 | 0.5877 | **-14.5pp** |
| ARC-Challenge | 0.8311 | 0.8164 | -1.5pp |
| HumanEval | 0.1829 | 0.0769 | **-10.6pp** |

### 注意事项

1. **MMLU 反向偏差**：para_aligned 略高于 aligned，但 item pool 不同（para 仅 6596 QC-passed items vs aligned 全量 14042），不可直接对比绝对值
2. **GSM8K/HumanEval 大幅下降**：符合预期 — 100% contamination 模型在 paraphrase 测试下生成类 benchmark 掉分最明显（GSM8K -14.5pp，HumanEval -10.6pp），说明记忆效应在这两个 benchmark 最严重
3. **ARC 稳定**：选择题格式的 paraphrase 对 ARC 影响较小（-1.5pp）
4. **与 s42 一致**：s42 para_aligned 结果（MMLU 0.659, GSM8K 0.583, ARC 0.809, HumanEval 0.115）高度一致，跨 seed 可复现
5. **bitsandbytes 警告**：`libnvJitLink.so.13` 加载失败，非致命，不影响推理结果

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_exp_001_eval_3B_d100_s123_para_aligned_v2_20260515T193308"
}
```

</details>

---
