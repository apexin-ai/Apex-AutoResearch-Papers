# analyze eval 15B s123 para aligned batch

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 47
- **Recorded user turns:** 0
- **Tool calls:** 23
- **Original source:** `logs/chats/worker_analyze_eval_15B_s123_para_aligned_batch_20260515T225650.jsonl`
- **Structured JSON:** [`4e32cbcc5b0d2d845a08.json`](../../sessions/4e/4e32cbcc5b0d2d845a08.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

47 recorded events

### Tool call

_source line 1 · 2026-05-15T22:59:20.699757+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__read_registry",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_15B_s123_para_aligned_batch_20260515T225650",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__read_registry",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-15T22:59:20.700422+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_15B_s123_para_aligned_batch_20260515T225650",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T22:59:20.700718+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "tail -50 ~/runs/contamcal-irt-calibration/exp_001_eval_15B_s123_para_aligned_batch.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_15B_s123_para_aligned_batch_20260515T225650",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "tail -50 ~/runs/contamcal-irt-calibration/exp_001_eval_15B_s123_para_aligned_batch.log"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-15T22:59:20.700945+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "find /root/autodl-tmp/exp001/eval_results/ -path \"*1.5B*s123*para_aligned*\" -name \"*.json\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_15B_s123_para_aligned_batch_20260515T225650",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "find /root/autodl-tmp/exp001/eval_results/ -path \"*1.5B*s123*para_aligned*\" -name \"*.json\" -type f"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T22:59:20.701160+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'exp_001_eval_15B_s123_para_aligned_batch'}",
  "project": "contamcal-irt-calibration",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_15B_s123_para_aligned_batch_20260515T225650",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'exp_001_eval_15B_s123_para_aligned_batch'}",
    "project": "contamcal-irt-calibration",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T22:59:20.709092+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-16 06:11:44,324 [INFO] humaneval pass@1: 0.1923 (5/26)\\n2026-05-16 06:11:44,358 [INFO] Results saved to /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d025_s123_para_aligned/eval_results.json\\n2026-05-16 06:11:44,361 [INFO] Correctness matrix saved to /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d025_s123_para_aligned/correctness_matrix.json\\n2026-05-16 06:11:44,395 [INFO] Item responses saved to /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d025_s123_para_aligned/item_responses.json\\n2026-05-16 06:11:44,395 [INFO] Sentinel .done written to /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d025_s123_para_aligned\\n=== Done 1.5B d025 s123 para_aligned ===\\n=== Running 1.5B d100 s123 para_aligned eval ===\\nCheckpoint: /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d100_s123\\nOutput: /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d100_s123_para_aligned\\n2026-05-16 06:11:50,703 [INFO] Loading base model: /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B + adapter: /root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d100_s123/lora_adapter\\n`torch_dtype` is deprecated! Use `dtype` instead!\\n2026-05-16 06:11:51,599 [INFO] We will use 90% of the memory on device 0 for storing the model, and 10% for the buffer to avoid OOM. You can set `max_memory` in to a higher value to use more memory (at your own risk).\\n2026-05-16 06:11:52,468 [ERROR] bitsandbytes library load error: libnvJitLink.so.13: cannot open shared object file: No such file or directory\\nTraceback (most recent call last):\\n  File \\\"/root/miniconda3/lib/python3.12/site-packages/bitsandbytes/cextension.py\\\", line 320, in &lt;module>\\n    lib = get_native_library()\\n          ^^^^^^^^^^^^^^^^^^^^\\n  File \\\"/root/miniconda3/lib/python3.12/site-packages/bitsandbytes/cextension.py\\\", line 298, in get_native_library\\n    dll = ct.cdll.LoadLibrary(str(binary_path))\\n          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\\n  File \\\"
…[truncated 6419 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_15B_s123_para_aligned_batch_20260515T225650",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 8
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-15T22:59:20.709556+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s123_para_aligned/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s123_para_aligned/correctness_matrix.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s123_para_aligned/item_responses.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d005_s123_para_aligned/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d005_s123_para_aligned/correctness_matrix.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d005_s123_para_aligned/item_responses.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d025_s123_para_aligned/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d025_s123_para_aligned/correctness_matrix.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d025_s123_para_aligned/item_responses.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d100_s123_para_aligned/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d100_s123_para_aligned/correctness_matrix.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d100_s123_para_aligned/item_responses.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_15B_s123_para_aligned_batch_20260515T225650",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 8
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-15T22:59:20.709828+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.9896}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_15B_s123_para_aligned_batch_20260515T225650",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 8
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T22:59:20.710111+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s123_para_aligned/eval_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_15B_s123_para_aligned_batch_20260515T225650",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s123_para_aligned/eval_results.json"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T22:59:20.714820+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"model_path\\\": \\\"/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B\\\",\\n  \\\"paraphrased\\\": true,\\n  \\\"benchmarks\\\": {\\n    \\\"mmlu\\\": {\\n      \\\"accuracy\\\": 0.6111279563371741,\\n      \\\"correct\\\": 4031,\\n      \\\"total\\\": 6596,\\n      \\\"per_item\\\": [\\n        {\\n          \\\"index\\\": 6,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"D\\\",\\n          \\\"gold\\\": \\\"A\\\"\\n        },\\n        {\\n          \\\"index\\\": 9,\\n          \\\"correct\\\": true,\\n          \\\"pred\\\": \\\"C\\\",\\n          \\\"gold\\\": \\\"C\\\"\\n        },\\n        {\\n          \\\"index\\\": 22,\\n          \\\"correct\\\": true,\\n          \\\"pred\\\": \\\"D\\\",\\n          \\\"gold\\\": \\\"D\\\"\\n        },\\n        {\\n          \\\"index\\\": 25,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"D\\\",\\n          \\\"gold\\\": \\\"C\\\"\\n        },\\n        {\\n          \\\"index\\\": 26,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"B\\\",\\n          \\\"gold\\\": \\\"C\\\"\\n        },\\n        {\\n          \\\"index\\\": 32,\\n          \\\"correct\\\": true,\\n          \\\"pred\\\": \\\"A\\\",\\n          \\\"gold\\\": \\\"A\\\"\\n        },\\n        {\\n          \\\"index\\\": 36,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"C\\\",\\n          \\\"gold\\\": \\\"D\\\"\\n        },\\n        {\\n          \\\"index\\\": 40,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"B\\\",\\n          \\\"gold\\\": \\\"C\\\"\\n        },\\n        {\\n          \\\"index\\\": 43,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"B\\\",\\n          \\\"gold\\\": \\\"C\\\"\\n        },\\n        {\\n          \\\"index\\\": 46,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"C\\\",\\n          \\\"gold\\\": \\\"B\\\"\\n        },\\n    
…[truncated 8698 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_15B_s123_para_aligned_batch_20260515T225650",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 4
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T22:59:20.715253+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d005_s123_para_aligned/eval_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_15B_s123_para_aligned_batch_20260515T225650",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d005_s123_para_aligned/eval_results.json"
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-15T22:59:20.715542+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d025_s123_para_aligned/eval_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_15B_s123_para_aligned_batch_20260515T225650",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d025_s123_para_aligned/eval_results.json"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-15T22:59:20.716275+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"model_path\\\": \\\"/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B\\\",\\n  \\\"paraphrased\\\": true,\\n  \\\"benchmarks\\\": {\\n    \\\"mmlu\\\": {\\n      \\\"accuracy\\\": 0.6140084899939358,\\n      \\\"correct\\\": 4050,\\n      \\\"total\\\": 6596,\\n      \\\"per_item\\\": [\\n        {\\n          \\\"index\\\": 6,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"D\\\",\\n          \\\"gold\\\": \\\"A\\\"\\n        },\\n        {\\n          \\\"index\\\": 9,\\n          \\\"correct\\\": true,\\n          \\\"pred\\\": \\\"C\\\",\\n          \\\"gold\\\": \\\"C\\\"\\n        },\\n        {\\n          \\\"index\\\": 22,\\n          \\\"correct\\\": true,\\n          \\\"pred\\\": \\\"D\\\",\\n          \\\"gold\\\": \\\"D\\\"\\n        },\\n        {\\n          \\\"index\\\": 25,\\n          \\\"correct\\\": true,\\n          \\\"pred\\\": \\\"C\\\",\\n          \\\"gold\\\": \\\"C\\\"\\n        },\\n        {\\n          \\\"index\\\": 26,\\n          \\\"correct\\\": true,\\n          \\\"pred\\\": \\\"C\\\",\\n          \\\"gold\\\": \\\"C\\\"\\n        },\\n        {\\n          \\\"index\\\": 32,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"B\\\",\\n          \\\"gold\\\": \\\"A\\\"\\n        },\\n        {\\n          \\\"index\\\": 36,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"C\\\",\\n          \\\"gold\\\": \\\"D\\\"\\n        },\\n        {\\n          \\\"index\\\": 40,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"B\\\",\\n          \\\"gold\\\": \\\"C\\\"\\n        },\\n        {\\n          \\\"index\\\": 43,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"B\\\",\\n          \\\"gold\\\": \\\"C\\\"\\n        },\\n        {\\n          \\\"index\\\": 46,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"C\\\",\\n          \\\"gold\\\": \\\"B\\\"\\n        },\\n     
…[truncated 8803 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_15B_s123_para_aligned_batch_20260515T225650",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-15T22:59:20.723185+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"model_path\\\": \\\"/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B\\\",\\n  \\\"paraphrased\\\": true,\\n  \\\"benchmarks\\\": {\\n    \\\"mmlu\\\": {\\n      \\\"accuracy\\\": 0.614463311097635,\\n      \\\"correct\\\": 4053,\\n      \\\"total\\\": 6596,\\n      \\\"per_item\\\": [\\n        {\\n          \\\"index\\\": 6,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"B\\\",\\n          \\\"gold\\\": \\\"A\\\"\\n        },\\n        {\\n          \\\"index\\\": 9,\\n          \\\"correct\\\": true,\\n          \\\"pred\\\": \\\"C\\\",\\n          \\\"gold\\\": \\\"C\\\"\\n        },\\n        {\\n          \\\"index\\\": 22,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"B\\\",\\n          \\\"gold\\\": \\\"D\\\"\\n        },\\n        {\\n          \\\"index\\\": 25,\\n          \\\"correct\\\": true,\\n          \\\"pred\\\": \\\"C\\\",\\n          \\\"gold\\\": \\\"C\\\"\\n        },\\n        {\\n          \\\"index\\\": 26,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"B\\\",\\n          \\\"gold\\\": \\\"C\\\"\\n        },\\n        {\\n          \\\"index\\\": 32,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"B\\\",\\n          \\\"gold\\\": \\\"A\\\"\\n        },\\n        {\\n          \\\"index\\\": 36,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"C\\\",\\n          \\\"gold\\\": \\\"D\\\"\\n        },\\n        {\\n          \\\"index\\\": 40,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"B\\\",\\n          \\\"gold\\\": \\\"C\\\"\\n        },\\n        {\\n          \\\"index\\\": 43,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"B\\\",\\n          \\\"gold\\\": \\\"C\\\"\\n        },\\n        {\\n          \\\"index\\\": 46,\\n          \\\"correct\\\": true,\\n          \\\"pred\\\": \\\"B\\\",\\n          \\\"gold\\\": \\\"B\\\"\\n        },\\n     
…[truncated 8833 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_15B_s123_para_aligned_batch_20260515T225650",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 7
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-15T22:59:20.723552+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d100_s123_para_aligned/eval_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_15B_s123_para_aligned_batch_20260515T225650",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d100_s123_para_aligned/eval_results.json"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-15T22:59:20.724208+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"model_path\\\": \\\"/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B\\\",\\n  \\\"paraphrased\\\": true,\\n  \\\"benchmarks\\\": {\\n    \\\"mmlu\\\": {\\n      \\\"accuracy\\\": 0.6290175864160097,\\n      \\\"correct\\\": 4149,\\n      \\\"total\\\": 6596,\\n      \\\"per_item\\\": [\\n        {\\n          \\\"index\\\": 6,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"B\\\",\\n          \\\"gold\\\": \\\"A\\\"\\n        },\\n        {\\n          \\\"index\\\": 9,\\n          \\\"correct\\\": true,\\n          \\\"pred\\\": \\\"C\\\",\\n          \\\"gold\\\": \\\"C\\\"\\n        },\\n        {\\n          \\\"index\\\": 22,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"B\\\",\\n          \\\"gold\\\": \\\"D\\\"\\n        },\\n        {\\n          \\\"index\\\": 25,\\n          \\\"correct\\\": true,\\n          \\\"pred\\\": \\\"C\\\",\\n          \\\"gold\\\": \\\"C\\\"\\n        },\\n        {\\n          \\\"index\\\": 26,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"B\\\",\\n          \\\"gold\\\": \\\"C\\\"\\n        },\\n        {\\n          \\\"index\\\": 32,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"B\\\",\\n          \\\"gold\\\": \\\"A\\\"\\n        },\\n        {\\n          \\\"index\\\": 36,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"C\\\",\\n          \\\"gold\\\": \\\"D\\\"\\n        },\\n        {\\n          \\\"index\\\": 40,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"B\\\",\\n          \\\"gold\\\": \\\"C\\\"\\n        },\\n        {\\n          \\\"index\\\": 43,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"B\\\",\\n          \\\"gold\\\": \\\"C\\\"\\n        },\\n        {\\n          \\\"index\\\": 46,\\n          \\\"correct\\\": true,\\n          \\\"pred\\\": \\\"B\\\",\\n          \\\"gold\\\": \\\"B\\\"\\n        },\\n    
…[truncated 8834 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_15B_s123_para_aligned_batch_20260515T225650",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-15T22:59:20.732744+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "fields": "['*']",
  "limit": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_15B_s123_para_aligned_batch_20260515T225650",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "contamcal-irt-calibration",
    "fields": "['*']",
    "limit": "5"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-15T22:59:20.733245+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"exp_001_eval_15B_s123_para_aligned_batch\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T20:08:58.408Z\", \"updated_at\": \"2026-05-15T22:52:28.130Z\", \"hypothesis\": \"1.5B s123 para_aligned eval batch (d000/d005/d025/d100). Fills 4 missing cells to complete 1.5B para_aligned matrix (s42 all done, s123 all missing). Adds 4 models to pooled IRT N count (N=19→23).\", \"spec\": {\"command\": \"python eval_batch.py (1.5B s123 para_aligned d000/d005/d025/d100)\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:3\", \"pid\": 627600, \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_15B_s123_para_aligned_batch.log\", \"submitted_at\": \"2026-05-15T20:09:46.226Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"Qwen2.5-1.5B\", \"seed\": 123, \"data_path\": \"mmlu paraphrased QC-passed items\", \"data_count\": 6596, \"checkpoint_source\": [\"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d000_s123/lora_adapter\", \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d005_s123/lora_adapter\", \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d025_s123/lora_adapter\", \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d100_s123/lora_adapter\"], \"eval_data\": \"mmlu paraphrased (para_aligned), 4 dose levels\", \"tmux_session\": \"exp_001_eval_15B_s123_para_aligned_batch\", \"hypothesis\": \"1.5B s123 para_aligned eval batch (d000/d005/d025/d100). Fills 4 missing cells to complete 1.5B para_aligned matrix (s42 all done, s123 all missing). Adds 4 models to pooled IRT N count (N=19→23).\"}, \"reproduce\": {\"finished_at\": \"2026-05-15T22:52:23.393Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T22:52:44.549179+00:00\"}]}}, \"exp_001_eval_3B_d005_s123_gsm8k\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:43:47.263Z\", \"upda
…[truncated 6605 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_15B_s123_para_aligned_batch_20260515T225650",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-15T22:59:20.733590+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "python3 -c \"import json; d=json.load(open('/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s123_para_aligned/eval_results.json')); print({b: round(d['benchmarks'][b]['accuracy'],4) for b in d['benchmarks']})\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_15B_s123_para_aligned_batch_20260515T225650",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "python3 -c \"import json; d=json.load(open('/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s123_para_aligned/eval_results.json')); print({b: round(d['benchmarks'][b]['accuracy'],4) for b in d['benchmarks']})\""
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-15T22:59:20.733819+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_15B_s123_para_aligned_batch_20260515T225650",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-15T22:59:20.734005+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "python3 -c \"import json; d=json.load(open('/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d005_s123_para_aligned/eval_results.json')); print({b: round(d['benchmarks'][b]['accuracy'],4) for b in d['benchmarks']})\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_15B_s123_para_aligned_batch_20260515T225650",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "python3 -c \"import json; d=json.load(open('/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d005_s123_para_aligned/eval_results.json')); print({b: round(d['benchmarks'][b]['accuracy'],4) for b in d['benchmarks']})\""
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-15T22:59:20.734192+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_15B_s123_para_aligned_batch_20260515T225650",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-15T22:59:20.738498+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "python3 -c \"import json; d=json.load(open('/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d025_s123_para_aligned/eval_results.json')); print({b: round(d['benchmarks'][b]['accuracy'],4) for b in d['benchmarks']})\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_15B_s123_para_aligned_batch_20260515T225650",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "python3 -c \"import json; d=json.load(open('/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d025_s123_para_aligned/eval_results.json')); print({b: round(d['benchmarks'][b]['accuracy'],4) for b in d['benchmarks']})\""
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-15T22:59:20.738824+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_15B_s123_para_aligned_batch_20260515T225650",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-15T22:59:20.739052+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "python3 -c \"import json; d=json.load(open('/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d100_s123_para_aligned/eval_results.json')); print({b: round(d['benchmarks'][b]['accuracy'],4) for b in d['benchmarks']})\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_15B_s123_para_aligned_batch_20260515T225650",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "python3 -c \"import json; d=json.load(open('/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d100_s123_para_aligned/eval_results.json')); print({b: round(d['benchmarks'][b]['accuracy'],4) for b in d['benchmarks']})\""
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-15T22:59:20.739256+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_15B_s123_para_aligned_batch_20260515T225650",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-15T22:59:20.739508+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "grep -A1 \"accuracy\" /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s123_para_aligned/eval_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_15B_s123_para_aligned_batch_20260515T225650",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "grep -A1 \"accuracy\" /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s123_para_aligned/eval_results.json"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-15T22:59:20.739735+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"      \\\"accuracy\\\": 0.6111279563371741,\\n      \\\"correct\\\": 4031,\\n--\\n      \\\"accuracy\\\": 0.5921052631578947,\\n      \\\"correct\\\": 135,\\n--\\n      \\\"accuracy\\\": 0.7546628407460545,\\n      \\\"correct\\\": 526,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.42}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_15B_s123_para_aligned_batch_20260515T225650",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-15T22:59:20.739967+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "grep -A1 \"accuracy\" /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d005_s123_para_aligned/eval_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_15B_s123_para_aligned_batch_20260515T225650",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "grep -A1 \"accuracy\" /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d005_s123_para_aligned/eval_results.json"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-15T22:59:20.740192+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"      \\\"accuracy\\\": 0.6140084899939358,\\n      \\\"correct\\\": 4050,\\n--\\n      \\\"accuracy\\\": 0.543859649122807,\\n      \\\"correct\\\": 124,\\n--\\n      \\\"accuracy\\\": 0.7474892395982783,\\n      \\\"correct\\\": 521,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_15B_s123_para_aligned_batch_20260515T225650",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-15T22:59:20.746557+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "grep -A1 \"accuracy\" /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d025_s123_para_aligned/eval_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_15B_s123_para_aligned_batch_20260515T225650",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "grep -A1 \"accuracy\" /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d025_s123_para_aligned/eval_results.json"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-15T22:59:20.746881+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"      \\\"accuracy\\\": 0.614463311097635,\\n      \\\"correct\\\": 4053,\\n--\\n      \\\"accuracy\\\": 0.5482456140350878,\\n      \\\"correct\\\": 125,\\n--\\n      \\\"accuracy\\\": 0.7503586800573888,\\n      \\\"correct\\\": 523,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.47}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_15B_s123_para_aligned_batch_20260515T225650",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-15T22:59:20.747094+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "grep -A1 \"accuracy\" /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d100_s123_para_aligned/eval_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_15B_s123_para_aligned_batch_20260515T225650",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "grep -A1 \"accuracy\" /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d100_s123_para_aligned/eval_results.json"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-15T22:59:20.747309+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"      \\\"accuracy\\\": 0.6290175864160097,\\n      \\\"correct\\\": 4149,\\n--\\n      \\\"accuracy\\\": 0.5307017543859649,\\n      \\\"correct\\\": 121,\\n--\\n      \\\"accuracy\\\": 0.7833572453371592,\\n      \\\"correct\\\": 546,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.42}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_15B_s123_para_aligned_batch_20260515T225650",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-15T22:59:20.747568+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "grep \"humaneval\" ~/runs/contamcal-irt-calibration/exp_001_eval_15B_s123_para_aligned_batch.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_15B_s123_para_aligned_batch_20260515T225650",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "grep \"humaneval\" ~/runs/contamcal-irt-calibration/exp_001_eval_15B_s123_para_aligned_batch.log"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-15T22:59:20.747794+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-16 04:49:27,341 [INFO] Evaluating humaneval (paraphrased)...\\n2026-05-16 04:49:27,343 [INFO] Loaded 26 QC-passed paraphrased items for humaneval from /root/autodl-tmp/exp001/paraphrases/humaneval_paraphrases.json\\n2026-05-16 04:52:59,851 [INFO] humaneval pass@1: 0.1538 (4/26)\\n2026-05-16 05:28:49,042 [INFO] Evaluating humaneval (paraphrased)...\\n2026-05-16 05:28:49,044 [INFO] Loaded 26 QC-passed paraphrased items for humaneval from /root/autodl-tmp/exp001/paraphrases/humaneval_paraphrases.json\\n2026-05-16 05:32:20,375 [INFO] humaneval pass@1: 0.0769 (2/26)\\n2026-05-16 06:08:12,183 [INFO] Evaluating humaneval (paraphrased)...\\n2026-05-16 06:08:12,185 [INFO] Loaded 26 QC-passed paraphrased items for humaneval from /root/autodl-tmp/exp001/paraphrases/humaneval_paraphrases.json\\n2026-05-16 06:11:44,324 [INFO] humaneval pass@1: 0.1923 (5/26)\\n2026-05-16 06:47:38,380 [INFO] Evaluating humaneval (paraphrased)...\\n2026-05-16 06:47:38,383 [INFO] Loaded 26 QC-passed paraphrased items for humaneval from /root/autodl-tmp/exp001/paraphrases/humaneval_paraphrases.json\\n2026-05-16 06:51:12,421 [INFO] humaneval pass@1: 0.2308 (6/26)\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_15B_s123_para_aligned_batch_20260515T225650",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-15T22:59:20.748103+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_001_eval_15B_s123_para_aligned_batch",
  "field": "metrics",
  "value": "{'d000': {'MMLU': 0.6111, 'GSM8K': 0.5921, 'ARC-C': 0.7547, 'HumanEval': 0.1538}, 'd005': {'MMLU': 0.614, 'GSM8K': 0.5439, 'ARC-C': 0.7475, 'HumanEval': 0.0769}, 'd025': {'MMLU': 0.6145, 'GSM8K': 0.5482, 'ARC-C': 0.7504, 'HumanEval': 0.1923}, 'd100': {'MMLU': 0.629, 'GSM8K': 0.5307, 'ARC-C': 0.7834, 'HumanEval': 0.2308}}",
  "project": "contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_15B_s123_para_aligned_batch_20260515T225650",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_001_eval_15B_s123_para_aligned_batch",
    "field": "metrics",
    "value": "{'d000': {'MMLU': 0.6111, 'GSM8K': 0.5921, 'ARC-C': 0.7547, 'HumanEval': 0.1538}, 'd005': {'MMLU': 0.614, 'GSM8K': 0.5439, 'ARC-C': 0.7475, 'HumanEval': 0.0769}, 'd025': {'MMLU': 0.6145, 'GSM8K': 0.5482, 'ARC-C': 0.7504, 'HumanEval': 0.1923}, 'd100': {'MMLU': 0.629, 'GSM8K': 0.5307, 'ARC-C': 0.7834, 'HumanEval': 0.2308}}",
    "project": "contamcal-irt-calibration"
  }
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-15T22:59:20.756434+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_001_eval_15B_s123_para_aligned_batch",
  "field": "checkpoint_path",
  "value": "/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_{d000,d005,d025,d100}_s123_para_aligned",
  "project": "contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_15B_s123_para_aligned_batch_20260515T225650",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_001_eval_15B_s123_para_aligned_batch",
    "field": "checkpoint_path",
    "value": "/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_{d000,d005,d025,d100}_s123_para_aligned",
    "project": "contamcal-irt-calibration"
  }
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-15T22:59:20.756917+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_001_eval_15B_s123_para_aligned_batch",
  "field": "log_path",
  "value": "~/runs/contamcal-irt-calibration/exp_001_eval_15B_s123_para_aligned_batch.log",
  "project": "contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_15B_s123_para_aligned_batch_20260515T225650",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_001_eval_15B_s123_para_aligned_batch",
    "field": "log_path",
    "value": "~/runs/contamcal-irt-calibration/exp_001_eval_15B_s123_para_aligned_batch.log",
    "project": "contamcal-irt-calibration"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-15T22:59:20.757227+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_001_eval_15B_s123_para_aligned_batch\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T20:08:58.408Z\", \"updated_at\": \"2026-05-15T22:58:20.725Z\", \"hypothesis\": \"1.5B s123 para_aligned eval batch (d000/d005/d025/d100). Fills 4 missing cells to complete 1.5B para_aligned matrix (s42 all done, s123 all missing). Adds 4 models to pooled IRT N count (N=19→23).\", \"spec\": {\"command\": \"python eval_batch.py (1.5B s123 para_aligned d000/d005/d025/d100)\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:3\", \"pid\": 627600, \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_15B_s123_para_aligned_batch.log\", \"submitted_at\": \"2026-05-15T20:09:46.226Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"Qwen2.5-1.5B\", \"seed\": 123, \"data_path\": \"mmlu paraphrased QC-passed items\", \"data_count\": 6596, \"checkpoint_source\": [\"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d000_s123/lora_adapter\", \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d005_s123/lora_adapter\", \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d025_s123/lora_adapter\", \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d100_s123/lora_adapter\"], \"eval_data\": \"mmlu paraphrased (para_aligned), 4 dose levels\", \"tmux_session\": \"exp_001_eval_15B_s123_para_aligned_batch\", \"hypothesis\": \"1.5B s123 para_aligned eval batch (d000/d005/d025/d100). Fills 4 missing cells to complete 1.5B para_aligned matrix (s42 all done, s123 all missing). Adds 4 models to pooled IRT N count (N=19→23).\"}, \"reproduce\": {\"finished_at\": \"2026-05-15T22:52:23.393Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T22:52:44.549179+00:00\"}]}, \"metrics\": {\"d000\": {\"MMLU\": 0.6111, \"GSM8K\": 0.5921, \"ARC-C\": 0.7547, \"HumanEval\": 0.1538}, \"d005\": {\"MMLU\": 0.
…[truncated 314 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_15B_s123_para_aligned_batch_20260515T225650",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 9
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-15T22:59:20.757578+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_001_eval_15B_s123_para_aligned_batch\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T20:08:58.408Z\", \"updated_at\": \"2026-05-15T22:58:29.202Z\", \"hypothesis\": \"1.5B s123 para_aligned eval batch (d000/d005/d025/d100). Fills 4 missing cells to complete 1.5B para_aligned matrix (s42 all done, s123 all missing). Adds 4 models to pooled IRT N count (N=19→23).\", \"spec\": {\"command\": \"python eval_batch.py (1.5B s123 para_aligned d000/d005/d025/d100)\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:3\", \"pid\": 627600, \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_15B_s123_para_aligned_batch.log\", \"submitted_at\": \"2026-05-15T20:09:46.226Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"Qwen2.5-1.5B\", \"seed\": 123, \"data_path\": \"mmlu paraphrased QC-passed items\", \"data_count\": 6596, \"checkpoint_source\": [\"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d000_s123/lora_adapter\", \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d005_s123/lora_adapter\", \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d025_s123/lora_adapter\", \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d100_s123/lora_adapter\"], \"eval_data\": \"mmlu paraphrased (para_aligned), 4 dose levels\", \"tmux_session\": \"exp_001_eval_15B_s123_para_aligned_batch\", \"hypothesis\": \"1.5B s123 para_aligned eval batch (d000/d005/d025/d100). Fills 4 missing cells to complete 1.5B para_aligned matrix (s42 all done, s123 all missing). Adds 4 models to pooled IRT N count (N=19→23).\"}, \"reproduce\": {\"finished_at\": \"2026-05-15T22:52:23.393Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T22:52:44.549179+00:00\"}]}, \"metrics\": {\"d000\": {\"MMLU\": 0.6111, \"GSM8K\": 0.5921, \"ARC-C\": 0.7547, \"HumanEval\": 0.1538}, \"d005\": {\"MMLU\": 0.
…[truncated 430 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_15B_s123_para_aligned_batch_20260515T225650",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-15T22:59:20.757878+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_001_eval_15B_s123_para_aligned_batch\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T20:08:58.408Z\", \"updated_at\": \"2026-05-15T22:58:34.428Z\", \"hypothesis\": \"1.5B s123 para_aligned eval batch (d000/d005/d025/d100). Fills 4 missing cells to complete 1.5B para_aligned matrix (s42 all done, s123 all missing). Adds 4 models to pooled IRT N count (N=19→23).\", \"spec\": {\"command\": \"python eval_batch.py (1.5B s123 para_aligned d000/d005/d025/d100)\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:3\", \"pid\": 627600, \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_15B_s123_para_aligned_batch.log\", \"submitted_at\": \"2026-05-15T20:09:46.226Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"Qwen2.5-1.5B\", \"seed\": 123, \"data_path\": \"mmlu paraphrased QC-passed items\", \"data_count\": 6596, \"checkpoint_source\": [\"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d000_s123/lora_adapter\", \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d005_s123/lora_adapter\", \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d025_s123/lora_adapter\", \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d100_s123/lora_adapter\"], \"eval_data\": \"mmlu paraphrased (para_aligned), 4 dose levels\", \"tmux_session\": \"exp_001_eval_15B_s123_para_aligned_batch\", \"hypothesis\": \"1.5B s123 para_aligned eval batch (d000/d005/d025/d100). Fills 4 missing cells to complete 1.5B para_aligned matrix (s42 all done, s123 all missing). Adds 4 models to pooled IRT N count (N=19→23).\"}, \"reproduce\": {\"finished_at\": \"2026-05-15T22:52:23.393Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T22:52:44.549179+00:00\"}]}, \"metrics\": {\"d000\": {\"MMLU\": 0.6111, \"GSM8K\": 0.5921, \"ARC-C\": 0.7547, \"HumanEval\": 0.1538}, \"d005\": {\"MMLU\": 0.
…[truncated 527 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_15B_s123_para_aligned_batch_20260515T225650",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-15T22:59:20.766654+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_001_eval_15B_s123_para_aligned_batch",
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
  "session": "worker_analyze_eval_15B_s123_para_aligned_batch_20260515T225650",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_001_eval_15B_s123_para_aligned_batch",
    "field": "conclusion",
    "value": "success",
    "project": "contamcal-irt-calibration"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-15T22:59:20.767094+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_001_eval_15B_s123_para_aligned_batch\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-15T20:08:58.408Z\", \"updated_at\": \"2026-05-15T22:58:47.633Z\", \"hypothesis\": \"1.5B s123 para_aligned eval batch (d000/d005/d025/d100). Fills 4 missing cells to complete 1.5B para_aligned matrix (s42 all done, s123 all missing). Adds 4 models to pooled IRT N count (N=19→23).\", \"spec\": {\"command\": \"python eval_batch.py (1.5B s123 para_aligned d000/d005/d025/d100)\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:3\", \"pid\": 627600, \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_15B_s123_para_aligned_batch.log\", \"submitted_at\": \"2026-05-15T20:09:46.226Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"Qwen2.5-1.5B\", \"seed\": 123, \"data_path\": \"mmlu paraphrased QC-passed items\", \"data_count\": 6596, \"checkpoint_source\": [\"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d000_s123/lora_adapter\", \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d005_s123/lora_adapter\", \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d025_s123/lora_adapter\", \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d100_s123/lora_adapter\"], \"eval_data\": \"mmlu paraphrased (para_aligned), 4 dose levels\", \"tmux_session\": \"exp_001_eval_15B_s123_para_aligned_batch\", \"hypothesis\": \"1.5B s123 para_aligned eval batch (d000/d005/d025/d100). Fills 4 missing cells to complete 1.5B para_aligned matrix (s42 all done, s123 all missing). Adds 4 models to pooled IRT N count (N=19→23).\"}, \"reproduce\": {\"finished_at\": \"2026-05-15T22:52:23.393Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T22:52:44.549179+00:00\"}]}, \"metrics\": {\"d000\": {\"MMLU\": 0.6111, \"GSM8K\": 0.5921, \"ARC-C\": 0.7547, \"HumanEval\": 0.1538}, \"d005\": {\"MMLU\": 0.
…[truncated 557 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_15B_s123_para_aligned_batch_20260515T225650",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-15T22:59:20.767438+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_001_eval_15B_s123_para_aligned_batch",
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
  "session": "worker_analyze_eval_15B_s123_para_aligned_batch_20260515T225650",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_001_eval_15B_s123_para_aligned_batch",
    "field": "status",
    "value": "DONE",
    "project": "contamcal-irt-calibration"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-15T22:59:20.769731+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_001_eval_15B_s123_para_aligned_batch\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T20:08:58.408Z\", \"updated_at\": \"2026-05-15T22:58:56.820Z\", \"hypothesis\": \"1.5B s123 para_aligned eval batch (d000/d005/d025/d100). Fills 4 missing cells to complete 1.5B para_aligned matrix (s42 all done, s123 all missing). Adds 4 models to pooled IRT N count (N=19→23).\", \"spec\": {\"command\": \"python eval_batch.py (1.5B s123 para_aligned d000/d005/d025/d100)\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:3\", \"pid\": 627600, \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_15B_s123_para_aligned_batch.log\", \"submitted_at\": \"2026-05-15T20:09:46.226Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"Qwen2.5-1.5B\", \"seed\": 123, \"data_path\": \"mmlu paraphrased QC-passed items\", \"data_count\": 6596, \"checkpoint_source\": [\"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d000_s123/lora_adapter\", \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d005_s123/lora_adapter\", \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d025_s123/lora_adapter\", \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d100_s123/lora_adapter\"], \"eval_data\": \"mmlu paraphrased (para_aligned), 4 dose levels\", \"tmux_session\": \"exp_001_eval_15B_s123_para_aligned_batch\", \"hypothesis\": \"1.5B s123 para_aligned eval batch (d000/d005/d025/d100). Fills 4 missing cells to complete 1.5B para_aligned matrix (s42 all done, s123 all missing). Adds 4 models to pooled IRT N count (N=19→23).\", \"wall_clock_seconds\": 10150.6, \"gpu_hours\": 2.82}, \"reproduce\": {\"finished_at\": \"2026-05-15T22:52:23.393Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T22:52:44.549179+00:00\"}]}, \"metrics\": {\"d000\": {\"MMLU\": 0.6111, \"GSM8K\": 0.5921, \"ARC-C\": 0.7547
…[truncated 703 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_15B_s123_para_aligned_batch_20260515T225650",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 2
}
```

</details>

---

### Assistant

_source line 47 · 2026-05-15T22:59:20.770053+00:00_

Registry 已更新为 DONE(success)。结果汇总：

## Qwen2.5-1.5B s123 para_aligned 结果

| Benchmark | d000 | d005 | d025 | d100 |
|-----------|------|------|------|------|
| MMLU | 0.6111 | 0.6140 | 0.6145 | 0.6290 |
| GSM8K | 0.5921 | 0.5439 | 0.5482 | 0.5307 |
| ARC-C | 0.7547 | 0.7475 | 0.7504 | 0.7834 |
| HumanEval | 0.1538 | 0.0769 | 0.1923 | 0.2308 |

**趋势观察：**
- **MMLU**: d000→d100 单调递增 (+1.8pp)，contamination dosage 效应明显
- **GSM8K**: 反而随 dosage 增加下降 (-6.1pp)，可能是 SFT on MMLU 数据导致 GSM8K 能力退化
- **ARC-C**: d100 明显高于其他 dosage (+2.9pp vs d000)，中间 dosage 基本持平
- **HumanEval**: 样本量太小（26 题），波动大，d005 异常低（2/26）

Wall clock: ~2.8 GPU-hours，4 个 dosage 全部完成。1.5B para_aligned matrix 的 s123 行已补齐。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analyze_eval_15B_s123_para_aligned_batch_20260515T225650"
}
```

</details>

---
