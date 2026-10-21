# analyze eval metrics batch 15B 3B

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 65
- **Recorded user turns:** 0
- **Tool calls:** 32
- **Original source:** `logs/chats/worker_analyze_eval_metrics_batch_15B_3B_20260515T230026.jsonl`
- **Structured JSON:** [`c36e79908c6463e1541c.json`](../../sessions/c3/c36e79908c6463e1541c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

65 recorded events

### Tool call

_source line 1 · 2026-05-15T23:02:56.497708+00:00_

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
  "session": "worker_analyze_eval_metrics_batch_15B_3B_20260515T230026",
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

_source line 2 · 2026-05-15T23:02:56.498256+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_metrics_batch_15B_3B_20260515T230026",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-15T23:02:56.498587+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ls -la /root/autodl-tmp/exp001/eval_results/ | grep \"1.5B.*s123\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_metrics_batch_15B_3B_20260515T230026",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ls -la /root/autodl-tmp/exp001/eval_results/ | grep \"1.5B.*s123\""
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-15T23:02:56.498812+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_metrics_batch_15B_3B_20260515T230026",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-15T23:02:56.499013+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "ls -la /root/autodl-tmp/exp001/eval_results/ | grep \"3B.*d005.*s123\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_metrics_batch_15B_3B_20260515T230026",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "ls -la /root/autodl-tmp/exp001/eval_results/ | grep \"3B.*d005.*s123\""
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-15T23:02:56.499218+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_metrics_batch_15B_3B_20260515T230026",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T23:02:56.509828+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "tail -20 /root/runs/contamcal-irt-calibration/exp_001_eval_15B_s123_para_aligned_batch.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_metrics_batch_15B_3B_20260515T230026",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "tail -20 /root/runs/contamcal-irt-calibration/exp_001_eval_15B_s123_para_aligned_batch.log"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-15T23:02:56.510171+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "tail -20 /root/runs/contamcal-irt-calibration/exp_001_eval_3B_d005_s123_gsm8k.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_metrics_batch_15B_3B_20260515T230026",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "tail -20 /root/runs/contamcal-irt-calibration/exp_001_eval_3B_d005_s123_gsm8k.log"
  }
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T23:02:56.510421+00:00_

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
  "session": "worker_analyze_eval_metrics_batch_15B_3B_20260515T230026",
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

### Tool call

_source line 10 · 2026-05-15T23:02:56.510892+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'exp_001_eval_3B_d005_s123_gsm8k'}",
  "project": "contamcal-irt-calibration",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_metrics_batch_15B_3B_20260515T230026",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'exp_001_eval_3B_d005_s123_gsm8k'}",
    "project": "contamcal-irt-calibration",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-15T23:02:56.511282+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-16 06:15:07,211 [INFO] mmlu accuracy: 0.6290 (4149/6596)\\n2026-05-16 06:15:07,211 [INFO] Evaluating gsm8k (paraphrased)...\\n2026-05-16 06:15:07,223 [INFO] Loaded 228 QC-passed paraphrased items for gsm8k from /root/autodl-tmp/exp001/paraphrases/gsm8k_paraphrases.json\\n\\rEvaluating GSM8K (paraphrased):   0%|          | 0/228 [00:00<?, ?it/s]\\rEvaluating GSM8K (paraphrased):   0%|          | 1/228 [00:09<34:51,  9.21s/it]\\rEvaluating GSM8K (paraphrased):   1%|          | 2/228 [00:17<32:32,  8.64s/it]\\rEvaluating GSM8K (paraphrased):   1%|▏         | 3/228 [00:25<31:36,  8.43s/it]\\rEvaluating GSM8K (paraphrased):   2%|▏         | 4/228 [00:33<31:00,  8.30s/it]\\rEvaluating GSM8K (paraphrased):   2%|▏         | 5/228 [00:41<30:38,  8.24s/it]\\rEvaluating GSM8K (paraphrased):   3%|▎         | 6/228 [00:50<30:21,  8.20s/it]\\rEvaluating GSM8K (paraphrased):   3%|▎         | 7/228 [00:58<30:02,  8.16s/it]\\rEvaluating GSM8K (paraphrased):   4%|▎         | 8/228 [01:06<29:52,  8.15s/it]\\rEvaluating GSM8K (paraphrased):   4%|▍         | 9/228 [01:14<29:46,  8.16s/it]\\rEvaluating GSM8K (paraphrased):   4%|▍         | 10/228 [01:22<29:36,  8.15s/it]\\rEvaluating GSM8K (paraphrased):   5%|▍         | 11/228 [01:30<29:33,  8.17s/it]\\rEvaluating GSM8K (paraphrased):   5%|▌         | 12/228 [01:39<29:36,  8.22s/it]\\rEvaluating GSM8K (paraphrased):   6%|▌         | 13/228 [01:47<29:21,  8.19s/it]\\rEvaluating GSM8K (paraphrased):   6%|▌         | 14/228 [01:55<29:07,  8.17s/it]\\rEvaluating GSM8K (paraphrased):   7%|▋         | 15/228 [02:03<28:54,  8.14s/it]\\rEvaluating GSM8K (paraphrased):   7%|▋         | 16/228 [02:11<28:46,  8.14s/it]\\rEvaluating GSM8K (paraphrased):   7%|▋         | 17/228 [02:19<28:39,  8.15s/it]\\rEvaluating GSM8K (paraphrased):   8%|▊         | 18/228 [02:28<28:43,  8.21s/it]\\rEvaluating GSM8K (paraphrased):   8%|▊         | 19/228 [02:36<28:30,  8.18s/it]\\rEvaluating GSM8K (p
…[truncated 6398 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_metrics_batch_15B_3B_20260515T230026",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-15T23:02:56.524963+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-16 03:49:05,527 [WARNING] '(MaxRetryError(\\\"HTTPSConnectionPool(host='huggingface.co', port=443): Max retries exceeded with url: /datasets/openai/gsm8k/resolve/740312add88f781978c0658806c59bc2815b9866/gsm8k.py (Caused by ConnectTimeoutError(&lt;urllib3.connection.HTTPSConnection object at 0x7f71d2266ff0>, 'Connection to huggingface.co timed out. (connect timeout=10)'))\\\"), '(Request ID: f0497628-cc7d-42ee-9bf6-584da73dc572)')' thrown while requesting HEAD https://huggingface.co/datasets/openai/gsm8k/resolve/740312add88f781978c0658806c59bc2815b9866/gsm8k.py\\nRetrying in 8s [Retry 4/5].\\n2026-05-16 03:49:05,527 [WARNING] Retrying in 8s [Retry 4/5].\\n'(MaxRetryError(\\\"HTTPSConnectionPool(host='huggingface.co', port=443): Max retries exceeded with url: /datasets/openai/gsm8k/resolve/740312add88f781978c0658806c59bc2815b9866/gsm8k.py (Caused by ConnectTimeoutError(&lt;urllib3.connection.HTTPSConnection object at 0x7f70607d9670>, 'Connection to huggingface.co timed out. (connect timeout=10)'))\\\"), '(Request ID: f5ec1436-7b08-4564-9040-f9c4cc0a45ea)')' thrown while requesting HEAD https://huggingface.co/datasets/openai/gsm8k/resolve/740312add88f781978c0658806c59bc2815b9866/gsm8k.py\\n2026-05-16 03:49:23,541 [WARNING] '(MaxRetryError(\\\"HTTPSConnectionPool(host='huggingface.co', port=443): Max retries exceeded with url: /datasets/openai/gsm8k/resolve/740312add88f781978c0658806c59bc2815b9866/gsm8k.py (Caused by ConnectTimeoutError(&lt;urllib3.connection.HTTPSConnection object at 0x7f70607d9670>, 'Connection to huggingface.co timed out. (connect timeout=10)'))\\\"), '(Request ID: f5ec1436-7b08-4564-9040-f9c4cc0a45ea)')' thrown while requesting HEAD https://huggingface.co/datasets/openai/gsm8k/resolve/740312add88f781978c0658806c59bc2815b9866/gsm8k.py\\nRetrying in 8s [Retry 5/5].\\n2026-05-16 03:49:23,541 [WARNING] Retrying in 8s [Retry 5/5].\\n'(MaxRetryError(\\\"HTTPSConnectionPool(host='huggingface.co', port=
…[truncated 6376 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_metrics_batch_15B_3B_20260515T230026",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 14
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-15T23:02:56.525293+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.9563}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_metrics_batch_15B_3B_20260515T230026",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 14
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-15T23:02:56.525545+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.1845}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_metrics_batch_15B_3B_20260515T230026",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 14
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-15T23:02:56.525815+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'status': 'ANALYZING'}",
  "project": "contamcal-irt-calibration",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_metrics_batch_15B_3B_20260515T230026",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'status': 'ANALYZING'}",
    "project": "contamcal-irt-calibration",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-15T23:02:56.526041+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "find /root/autodl-tmp/exp001/eval_results/ -name \"eval_results.json\" -path \"*1.5B*s123*para*\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_metrics_batch_15B_3B_20260515T230026",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "find /root/autodl-tmp/exp001/eval_results/ -name \"eval_results.json\" -path \"*1.5B*s123*para*\""
  }
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-15T23:02:56.526242+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d005_s123_gsm8k_rerun/eval_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_metrics_batch_15B_3B_20260515T230026",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d005_s123_gsm8k_rerun/eval_results.json"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-15T23:02:56.543744+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.6073}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_metrics_batch_15B_3B_20260515T230026",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 17
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-15T23:02:56.544027+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s123_para_aligned/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d005_s123_para_aligned/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d025_s123_para_aligned/eval_results.json\\n/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d100_s123_para_aligned/eval_results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_metrics_batch_15B_3B_20260515T230026",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 17
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-15T23:02:56.544633+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"model_path\\\": \\\"/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B\\\",\\n  \\\"paraphrased\\\": false,\\n  \\\"benchmarks\\\": {\\n    \\\"gsm8k\\\": {\\n      \\\"accuracy\\\": 0.6307808946171342,\\n      \\\"correct\\\": 832,\\n      \\\"total\\\": 1319,\\n      \\\"per_item\\\": [\\n        {\\n          \\\"index\\\": 0,\\n          \\\"correct\\\": true,\\n          \\\"pred\\\": \\\"18\\\",\\n          \\\"gold\\\": \\\"18\\\"\\n        },\\n        {\\n          \\\"index\\\": 1,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"3.\\\",\\n          \\\"gold\\\": \\\"3\\\"\\n        },\\n        {\\n          \\\"index\\\": 2,\\n          \\\"correct\\\": true,\\n          \\\"pred\\\": \\\"70000\\\",\\n          \\\"gold\\\": \\\"70000\\\"\\n        },\\n        {\\n          \\\"index\\\": 3,\\n          \\\"correct\\\": true,\\n          \\\"pred\\\": \\\"540\\\",\\n          \\\"gold\\\": \\\"540\\\"\\n        },\\n        {\\n          \\\"index\\\": 4,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"20.\\\",\\n          \\\"gold\\\": \\\"20\\\"\\n        },\\n        {\\n          \\\"index\\\": 5,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"72\\\",\\n          \\\"gold\\\": \\\"64\\\"\\n        },\\n        {\\n          \\\"index\\\": 6,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"1060\\\",\\n          \\\"gold\\\": \\\"260\\\"\\n        },\\n        {\\n          \\\"index\\\": 7,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"200\\\",\\n          \\\"gold\\\": \\\"160\\\"\\n        },\\n        {\\n          \\\"index\\\": 8,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"475\\\",\\n          \\\"gold\\\": \\\"45\\\"\\n        },\\n        {\\n          \\\"index\\\": 9,\\n          \\\"correct\\\": true,\\n          \\\"pred\\\": \\\"460\\\",\\n          \\\"gold\\\": \\\"4
…[truncated 9380 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_metrics_batch_15B_3B_20260515T230026",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 18
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-15T23:02:56.544966+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "python3 -c \"import json; d=json.load(open('/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s123_para_aligned/eval_results.json')); print({k:{'accuracy':v['accuracy'],'correct':v['correct'],'total':v['total']} for k,v in d['benchmarks'].items()})\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_metrics_batch_15B_3B_20260515T230026",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "python3 -c \"import json; d=json.load(open('/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s123_para_aligned/eval_results.json')); print({k:{'accuracy':v['accuracy'],'correct':v['correct'],'total':v['total']} for k,v in d['benchmarks'].items()})\""
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-15T23:02:56.545182+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_metrics_batch_15B_3B_20260515T230026",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-15T23:02:56.560963+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "python3 -c \"import json; d=json.load(open('/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d005_s123_para_aligned/eval_results.json')); print({k:{'accuracy':v['accuracy'],'correct':v['correct'],'total':v['total']} for k,v in d['benchmarks'].items()})\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_metrics_batch_15B_3B_20260515T230026",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "python3 -c \"import json; d=json.load(open('/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d005_s123_para_aligned/eval_results.json')); print({k:{'accuracy':v['accuracy'],'correct':v['correct'],'total':v['total']} for k,v in d['benchmarks'].items()})\""
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-15T23:02:56.561407+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_metrics_batch_15B_3B_20260515T230026",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-15T23:02:56.561685+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "python3 -c \"import json; d=json.load(open('/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d025_s123_para_aligned/eval_results.json')); print({k:{'accuracy':v['accuracy'],'correct':v['correct'],'total':v['total']} for k,v in d['benchmarks'].items()})\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_metrics_batch_15B_3B_20260515T230026",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "python3 -c \"import json; d=json.load(open('/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d025_s123_para_aligned/eval_results.json')); print({k:{'accuracy':v['accuracy'],'correct':v['correct'],'total':v['total']} for k,v in d['benchmarks'].items()})\""
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-15T23:02:56.561908+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_metrics_batch_15B_3B_20260515T230026",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-15T23:02:56.562112+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "python3 -c \"import json; d=json.load(open('/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d100_s123_para_aligned/eval_results.json')); print({k:{'accuracy':v['accuracy'],'correct':v['correct'],'total':v['total']} for k,v in d['benchmarks'].items()})\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_metrics_batch_15B_3B_20260515T230026",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "python3 -c \"import json; d=json.load(open('/root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d100_s123_para_aligned/eval_results.json')); print({k:{'accuracy':v['accuracy'],'correct':v['correct'],'total':v['total']} for k,v in d['benchmarks'].items()})\""
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-15T23:02:56.572723+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter ';' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_metrics_batch_15B_3B_20260515T230026",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 10
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-15T23:02:56.573112+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "contamcal-irt-calibration",
  "fields": "['exp_id', 'status']",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_metrics_batch_15B_3B_20260515T230026",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "contamcal-irt-calibration",
    "fields": "['exp_id', 'status']",
    "limit": "50"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-15T23:02:56.573435+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"exp_001_eval_15B_s123_para_aligned_batch\": {\"status\": \"DONE\"}, \"exp_001_eval_3B_d005_s123_gsm8k\": {\"status\": \"DONE\"}, \"exp_001_eval_3B_d025_s123_para_aligned\": {\"status\": \"DONE\"}, \"exp_001_sft_3B_d005_s42_a32\": {\"status\": \"RUNNING\"}, \"exp_001_eval_3B_d100_s123_a32_batch\": {\"status\": \"RUNNING\"}, \"exp_001_sft_3B_d100_s123_a32\": {\"status\": \"PREPARING\"}, \"exp_001_sft_3B_d100_s123_a32_v2\": {\"status\": \"DONE\"}, \"exp_001_sft_3B_d100_s42_a32_v2\": {\"status\": \"DONE\"}, \"exp_001_sft_3B_d025_s42_a32\": {\"status\": \"DONE\"}, \"exp_001_sft_3B_d100_s42_a32\": {\"status\": \"DONE\"}, \"exp_001_sft_d025_3B_v3\": {\"status\": \"DONE\"}, \"exp_002_signals_3B_v6\": {\"status\": \"DONE\"}, \"exp_001_sft_3B_d000_s42_a32\": {\"status\": \"RUNNING\"}, \"exp_001_sft_3B_d100_s42_a32_v3\": {\"status\": \"RUNNING\"}, \"exp_001_sft_3B_d000_v4\": {\"status\": \"PREPARING\"}, \"exp_001_sft_d005_3B\": {\"status\": \"DONE\"}, \"exp_001_sft_3B_d000_s42\": {\"status\": \"PREPARING\"}, \"exp_002_signals_3B_v4\": {\"status\": \"DONE\"}, \"exp_004_sim_sweep_extreme_gamma\": {\"status\": \"DONE\"}, \"exp_002_signals_3B_v5\": {\"status\": \"RUNNING\"}, \"exp_001_eval_3B_d100_s123_para_aligned_v2\": {\"status\": \"DONE\"}, \"exp_001_eval_3B_d100_s123_para_aligned\": {\"status\": \"DONE\"}, \"exp_001_sft_3B_d000_v3\": {\"status\": \"DONE\"}, \"exp_004_sim_sweep_v6\": {\"status\": \"DONE\"}, \"exp_002_signals_3B_v3\": {\"status\": \"DONE\"}, \"exp_001_eval_3B_d005_s123_aligned\": {\"status\": \"DONE\"}, \"exp_001_eval_3B_d005_s42_para_aligned\": {\"status\": \"PREPARING\"}, \"exp_004_sim_sweep_v7\": {\"status\": \"RUNNING\"}, \"exp_001_eval_3B_d025_s123_aligned\": {\"status\": \"DONE\"}, \"exp_002_signals_3B_v2\": {\"status\": \"DONE\"}, \"exp_005_noise_prop_v4\": {\"status\": \"DONE\"}, \"exp_001_eval_3B_d005_s123_para_aligned\": {\"status\": \"DONE\"}, \"exp_001_eval_15B_d005_s123\": {\"status\": \
…[truncated 1110 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_metrics_batch_15B_3B_20260515T230026",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-15T23:02:56.573769+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'exp_001_eval_15B_s123_para_aligned_batch'}",
  "project": "contamcal-irt-calibration",
  "fields": "['*']",
  "limit": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_metrics_batch_15B_3B_20260515T230026",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'exp_001_eval_15B_s123_para_aligned_batch'}",
    "project": "contamcal-irt-calibration",
    "fields": "['*']",
    "limit": "1"
  }
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-15T23:02:56.573984+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'exp_001_eval_3B_d005_s123_gsm8k'}",
  "project": "contamcal-irt-calibration",
  "fields": "['*']",
  "limit": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_metrics_batch_15B_3B_20260515T230026",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'exp_001_eval_3B_d005_s123_gsm8k'}",
    "project": "contamcal-irt-calibration",
    "fields": "['*']",
    "limit": "1"
  }
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-15T23:02:56.574190+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "grep \"accuracy\" /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s123_para_aligned/eval_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_metrics_batch_15B_3B_20260515T230026",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "grep \"accuracy\" /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s123_para_aligned/eval_results.json"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-15T23:02:56.587960+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.79}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_metrics_batch_15B_3B_20260515T230026",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 14
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-15T23:02:56.588309+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "grep \"accuracy\" /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d005_s123_para_aligned/eval_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_metrics_batch_15B_3B_20260515T230026",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "grep \"accuracy\" /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d005_s123_para_aligned/eval_results.json"
  }
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-15T23:02:56.588578+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "grep \"accuracy\" /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d025_s123_para_aligned/eval_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_metrics_batch_15B_3B_20260515T230026",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "grep \"accuracy\" /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d025_s123_para_aligned/eval_results.json"
  }
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-15T23:02:56.591525+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "grep \"accuracy\" /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d100_s123_para_aligned/eval_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_metrics_batch_15B_3B_20260515T230026",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "grep \"accuracy\" /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d100_s123_para_aligned/eval_results.json"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-15T23:02:56.591787+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.7437}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_metrics_batch_15B_3B_20260515T230026",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 17
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-15T23:02:56.592024+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"      \\\"accuracy\\\": 0.6111279563371741,\\n      \\\"accuracy\\\": 0.5921052631578947,\\n      \\\"accuracy\\\": 0.7546628407460545,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.37}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_metrics_batch_15B_3B_20260515T230026",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 17
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-15T23:02:56.592243+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"      \\\"accuracy\\\": 0.6140084899939358,\\n      \\\"accuracy\\\": 0.543859649122807,\\n      \\\"accuracy\\\": 0.7474892395982783,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_metrics_batch_15B_3B_20260515T230026",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-15T23:02:56.601816+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"      \\\"accuracy\\\": 0.614463311097635,\\n      \\\"accuracy\\\": 0.5482456140350878,\\n      \\\"accuracy\\\": 0.7503586800573888,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_metrics_batch_15B_3B_20260515T230026",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 13
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-15T23:02:56.602136+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"      \\\"accuracy\\\": 0.6290175864160097,\\n      \\\"accuracy\\\": 0.5307017543859649,\\n      \\\"accuracy\\\": 0.7833572453371592,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_metrics_batch_15B_3B_20260515T230026",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 10
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-15T23:02:56.602455+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "head -30 /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s123_para_aligned/eval_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_metrics_batch_15B_3B_20260515T230026",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "head -30 /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s123_para_aligned/eval_results.json"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-15T23:02:56.602736+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"model_path\\\": \\\"/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B\\\",\\n  \\\"paraphrased\\\": true,\\n  \\\"benchmarks\\\": {\\n    \\\"mmlu\\\": {\\n      \\\"accuracy\\\": 0.6111279563371741,\\n      \\\"correct\\\": 4031,\\n      \\\"total\\\": 6596,\\n      \\\"per_item\\\": [\\n        {\\n          \\\"index\\\": 6,\\n          \\\"correct\\\": false,\\n          \\\"pred\\\": \\\"D\\\",\\n          \\\"gold\\\": \\\"A\\\"\\n        },\\n        {\\n          \\\"index\\\": 9,\\n          \\\"correct\\\": true,\\n          \\\"pred\\\": \\\"C\\\",\\n          \\\"gold\\\": \\\"C\\\"\\n        },\\n        {\\n          \\\"index\\\": 22,\\n          \\\"correct\\\": true,\\n          \\\"pred\\\": \\\"D\\\",\\n          \\\"gold\\\": \\\"D\\\"\\n        },\\n        {\\n          \\\"index\\\": 25,\\n          \\\"correct\\\": false,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_metrics_batch_15B_3B_20260515T230026",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-15T23:02:56.602995+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "grep -B2 \"accuracy\" /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s123_para_aligned/eval_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_metrics_batch_15B_3B_20260515T230026",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "grep -B2 \"accuracy\" /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s123_para_aligned/eval_results.json"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-15T23:02:56.615665+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  \\\"benchmarks\\\": {\\n    \\\"mmlu\\\": {\\n      \\\"accuracy\\\": 0.6111279563371741,\\n--\\n    },\\n    \\\"gsm8k\\\": {\\n      \\\"accuracy\\\": 0.5921052631578947,\\n--\\n    },\\n    \\\"arc_challenge\\\": {\\n      \\\"accuracy\\\": 0.7546628407460545,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_metrics_batch_15B_3B_20260515T230026",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 12
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-15T23:02:56.615972+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "grep -B2 \"accuracy\" /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d005_s123_para_aligned/eval_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_metrics_batch_15B_3B_20260515T230026",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "grep -B2 \"accuracy\" /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d005_s123_para_aligned/eval_results.json"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-15T23:02:56.616186+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  \\\"benchmarks\\\": {\\n    \\\"mmlu\\\": {\\n      \\\"accuracy\\\": 0.6140084899939358,\\n--\\n    },\\n    \\\"gsm8k\\\": {\\n      \\\"accuracy\\\": 0.543859649122807,\\n--\\n    },\\n    \\\"arc_challenge\\\": {\\n      \\\"accuracy\\\": 0.7474892395982783,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_metrics_batch_15B_3B_20260515T230026",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-15T23:02:56.616405+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "grep -B2 \"accuracy\" /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d025_s123_para_aligned/eval_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_metrics_batch_15B_3B_20260515T230026",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "grep -B2 \"accuracy\" /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d025_s123_para_aligned/eval_results.json"
  }
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-15T23:02:56.616631+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "grep -B2 \"accuracy\" /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d100_s123_para_aligned/eval_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_metrics_batch_15B_3B_20260515T230026",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "grep -B2 \"accuracy\" /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d100_s123_para_aligned/eval_results.json"
  }
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-15T23:02:56.616846+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  \\\"benchmarks\\\": {\\n    \\\"mmlu\\\": {\\n      \\\"accuracy\\\": 0.614463311097635,\\n--\\n    },\\n    \\\"gsm8k\\\": {\\n      \\\"accuracy\\\": 0.5482456140350878,\\n--\\n    },\\n    \\\"arc_challenge\\\": {\\n      \\\"accuracy\\\": 0.7503586800573888,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_metrics_batch_15B_3B_20260515T230026",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-15T23:02:56.617070+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  \\\"benchmarks\\\": {\\n    \\\"mmlu\\\": {\\n      \\\"accuracy\\\": 0.6290175864160097,\\n--\\n    },\\n    \\\"gsm8k\\\": {\\n      \\\"accuracy\\\": 0.5307017543859649,\\n--\\n    },\\n    \\\"arc_challenge\\\": {\\n      \\\"accuracy\\\": 0.7833572453371592,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_metrics_batch_15B_3B_20260515T230026",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-15T23:02:56.633408+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "grep -B2 \"pass\" /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s123_para_aligned/eval_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_metrics_batch_15B_3B_20260515T230026",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "grep -B2 \"pass\" /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d000_s123_para_aligned/eval_results.json"
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-15T23:02:56.633935+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"    },\\n    \\\"humaneval\\\": {\\n      \\\"pass@1\\\": 0.15384615384615385,\\n--\\n          \\\"index\\\": 41,\\n          \\\"correct\\\": false,\\n          \\\"generated\\\": \\\"    # Your code here\\\\n    pass\\\\n\\\\n# Example usage:\\\\n# car_race_collision(3) should return 0\\\\n# car_race_collision(4) should return 1\\\\n# car_race_collision(5) should return 2\\\\n# car_race_collision(6) should return 3\\\\n# car_race_collision(7) should return 4\\\\n# car_race_collision(8) should return 5\\\\n# car_race_collision(9) should return 6\\\\n# car_race_collision(10) should return 7\\\\n# car_race_collision(11) should return 8\\\\n# car_race_collision(12) should return 9\\\\n# car_race_collision(13) should return 10\\\\n# car_r\\\"\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_metrics_batch_15B_3B_20260515T230026",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-15T23:02:56.634194+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "grep -B2 \"pass\" /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d005_s123_para_aligned/eval_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_metrics_batch_15B_3B_20260515T230026",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "grep -B2 \"pass\" /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d005_s123_para_aligned/eval_results.json"
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-15T23:02:56.634449+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"    },\\n    \\\"humaneval\\\": {\\n      \\\"pass@1\\\": 0.07692307692307693,\\n--\\n          \\\"index\\\": 19,\\n          \\\"correct\\\": false,\\n          \\\"generated\\\": \\\"def sort_numbers(numbers: str) -> str:\\\\n    numbers = numbers.split()\\\\n    sorted_numbers = sorted(numbers, key=lambda x: int(x))\\\\n    return ' '.join(sorted_numbers)  # Convert the list of strings back to a string and return it.  This is a common Python idiom for string concatenation.  The 'join' method takes a list of strings and concatenates them into a single string, with the strings separated by the string passed as the second argument.  In this case, the separator is a space.  The 'join' meth\\\"\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_metrics_batch_15B_3B_20260515T230026",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-15T23:02:56.634678+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "grep -B2 \"pass\" /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d025_s123_para_aligned/eval_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_metrics_batch_15B_3B_20260515T230026",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "grep -B2 \"pass\" /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d025_s123_para_aligned/eval_results.json"
  }
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-15T23:02:56.634887+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "grep -B2 \"pass\" /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d100_s123_para_aligned/eval_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_metrics_batch_15B_3B_20260515T230026",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "grep -B2 \"pass\" /root/autodl-tmp/exp001/eval_results/Qwen2.5-1.5B_d100_s123_para_aligned/eval_results.json"
  }
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-15T23:02:56.635097+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"    },\\n    \\\"humaneval\\\": {\\n      \\\"pass@1\\\": 0.19230769230769232,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_metrics_batch_15B_3B_20260515T230026",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-15T23:02:56.653417+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"    },\\n    \\\"humaneval\\\": {\\n      \\\"pass@1\\\": 0.23076923076923078,\\n--\\n          \\\"index\\\": 41,\\n          \\\"correct\\\": false,\\n          \\\"generated\\\": \\\"    # Your code here\\\\n    pass\\\\n  #  return 0\\\\n\\\\n  #  # Your code here\\\\n  #  pass\\\\n  #  return 0\\\\n\\\\n  #  # Your code here\\\\n  #  pass\\\\n  #  return 0\\\\n\\\\n  #  # Your code here\\\\n  #  pass\\\\n  #  return 0\\\\n\\\\n  #  # Your code here\\\\n  #  pass\\\\n  #  return 0\\\\n\\\\n  #  # Your code here\\\\n  #  pass\\\\n  #  return 0\\\\n\\\\n  #  # Your code here\\\\n  #  pass\\\\n  #  return 0\\\\n\\\\n  #  # Your code here\\\\n  #  pass\\\\n  #  return 0\\\\n\\\\n  #  # Your code here\\\\n  #  pass\\\\n  #  return 0\\\\n\\\\n  #  # Your code here\\\\n  #  pass\\\\n  #  return 0\\\\n\\\\n  #  # Your code here\\\\n  #  pass\\\\n\\\"\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.4}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_metrics_batch_15B_3B_20260515T230026",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 18
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-15T23:02:56.654042+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_001_eval_15B_s123_para_aligned_batch",
  "field": "metrics",
  "value": "{'d000': {'mmlu': 0.6111, 'gsm8k': 0.5921, 'arc_challenge': 0.7547, 'humaneval': 0.1538}, 'd005': {'mmlu': 0.614, 'gsm8k': 0.5439, 'arc_challenge': 0.7475, 'humaneval': 0.0769}, 'd025': {'mmlu': 0.6145, 'gsm8k': 0.5482, 'arc_challenge': 0.7504, 'humaneval': 0.1923}, 'd100': {'mmlu': 0.629, 'gsm8k': 0.5307, 'arc_challenge': 0.7834, 'humaneval': 0.2308}}",
  "project": "contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_metrics_batch_15B_3B_20260515T230026",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_001_eval_15B_s123_para_aligned_batch",
    "field": "metrics",
    "value": "{'d000': {'mmlu': 0.6111, 'gsm8k': 0.5921, 'arc_challenge': 0.7547, 'humaneval': 0.1538}, 'd005': {'mmlu': 0.614, 'gsm8k': 0.5439, 'arc_challenge': 0.7475, 'humaneval': 0.0769}, 'd025': {'mmlu': 0.6145, 'gsm8k': 0.5482, 'arc_challenge': 0.7504, 'humaneval': 0.1923}, 'd100': {'mmlu': 0.629, 'gsm8k': 0.5307, 'arc_challenge': 0.7834, 'humaneval': 0.2308}}",
    "project": "contamcal-irt-calibration"
  }
}
```

</details>

---

### Tool call

_source line 62 · 2026-05-15T23:02:56.654400+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "exp_001_eval_3B_d005_s123_gsm8k",
  "field": "metrics",
  "value": "{'gsm8k': 0.6308}",
  "project": "contamcal-irt-calibration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_eval_metrics_batch_15B_3B_20260515T230026",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "exp_001_eval_3B_d005_s123_gsm8k",
    "field": "metrics",
    "value": "{'gsm8k': 0.6308}",
    "project": "contamcal-irt-calibration"
  }
}
```

</details>

---

### Tool result

_source line 63 · 2026-05-15T23:02:56.654730+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_001_eval_15B_s123_para_aligned_batch\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T20:08:58.408Z\", \"updated_at\": \"2026-05-15T23:02:34.285Z\", \"hypothesis\": \"1.5B s123 para_aligned eval batch (d000/d005/d025/d100). Fills 4 missing cells to complete 1.5B para_aligned matrix (s42 all done, s123 all missing). Adds 4 models to pooled IRT N count (N=19→23).\", \"spec\": {\"command\": \"python eval_batch.py (1.5B s123 para_aligned d000/d005/d025/d100)\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:3\", \"pid\": 627600, \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_15B_s123_para_aligned_batch.log\", \"submitted_at\": \"2026-05-15T20:09:46.226Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"Qwen2.5-1.5B\", \"seed\": 123, \"data_path\": \"mmlu paraphrased QC-passed items\", \"data_count\": 6596, \"checkpoint_source\": [\"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d000_s123/lora_adapter\", \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d005_s123/lora_adapter\", \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d025_s123/lora_adapter\", \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d100_s123/lora_adapter\"], \"eval_data\": \"mmlu paraphrased (para_aligned), 4 dose levels\", \"tmux_session\": \"exp_001_eval_15B_s123_para_aligned_batch\", \"hypothesis\": \"1.5B s123 para_aligned eval batch (d000/d005/d025/d100). Fills 4 missing cells to complete 1.5B para_aligned matrix (s42 all done, s123 all missing). Adds 4 models to pooled IRT N count (N=19→23).\", \"wall_clock_seconds\": 10150.6, \"gpu_hours\": 2.82}, \"reproduce\": {\"finished_at\": \"2026-05-15T22:52:23.393Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T22:52:44.549179+00:00\"}]}, \"metrics\": {\"d000\": {\"mmlu\": 0.6111, \"gsm8k\": 0.5921, \"arc_challenge\"
…[truncated 685 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_metrics_batch_15B_3B_20260515T230026",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 64 · 2026-05-15T23:02:56.668803+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"exp_001_eval_3B_d005_s123_gsm8k\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:43:47.263Z\", \"updated_at\": \"2026-05-15T23:02:40.122Z\", \"spec\": {\"command\": \"bash -c 'source conda && evaluate.py --benchmarks gsm8k --mc-format aligned --adapter Qwen2.5-3B_d005_s123'\", \"server\": \"cqa1-21977\", \"gpu\": [\"cuda:2\"], \"pid\": \"623480\", \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_3B_d005_s123_gsm8k.log\", \"submitted_at\": \"2026-05-15T19:43:44.767Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d005_s123/lora_adapter\", \"data_count\": 0, \"model_name\": \"Qwen/Qwen2.5-3B\", \"seed\": 123, \"checkpoint_source\": \"exp_001_sft_3B_d005_s123\", \"eval_data\": \"gsm8k aligned\", \"wall_clock_seconds\": 11695.9, \"gpu_hours\": 3.25}, \"hypothesis\": \"GSM8K single-benchmark rerun for d005_s123 aligned eval. Checks if GSM8K already exists in eval_results.json; if missing, runs GSM8K only. Director ordered as part of D068 gap-fill.\", \"reproduce\": {\"finished_at\": \"2026-05-15T22:51:16.656Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T22:51:33.234370+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"gsm8k\": 0.6308}, \"log_path\": \"~/runs/contamcal-irt-calibration/exp_001_eval_3B_d005_s123_gsm8k.log\", \"checkpoint_path\": \"/root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d005_s123_gsm8k_rerun\", \"completed_at\": \"2026-05-15T22:58:40.681Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 6.5378}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_eval_metrics_batch_15B_3B_20260515T230026",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 14
}
```

</details>

---

### Assistant

_source line 65 · 2026-05-15T23:02:56.670754+00:00_

两个实验 metrics 已更新成功。Registry 显示 conclusion=success, status=DONE, checkpoint_path 和 log_path 均已设置。

## 汇总

```
exp_001_eval_15B_s123_para_aligned_batch (paraphrased):
  d000: {mmlu: 0.6111, gsm8k: 0.5921, arc_challenge: 0.7547, humaneval: 0.1538}
  d005: {mmlu: 0.6140, gsm8k: 0.5439, arc_challenge: 0.7475, humaneval: 0.0769}
  d025: {mmlu: 0.6145, gsm8k: 0.5482, arc_challenge: 0.7504, humaneval: 0.1923}
  d100: {mmlu: 0.6290, gsm8k: 0.5307, arc_challenge: 0.7834, humaneval: 0.2308}

exp_001_eval_3B_d005_s123_gsm8k (aligned, original):
  gsm8k: 0.6308
```

趋势：1.5B para_aligned 随 dose 增加，mmlu/arc_challenge 上升（0.611→0.629, 0.755→0.783），gsm8k 下降（0.592→0.531），humaneval 波动但 d100 最高（0.231）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analyze_eval_metrics_batch_15B_3B_20260515T230026"
}
```

</details>

---
