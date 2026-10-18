# analyze mistral hires bf16 2bitonly v4

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 32
- **Recorded user turns:** 0
- **Tool calls:** 15
- **Original source:** `logs/chats/worker_analyze_mistral_hires_bf16_2bitonly_v4_20260514T223456.jsonl`
- **Structured JSON:** [`2f5a69e545f3a7b19cda.json`](../../sessions/2f/2f5a69e545f3a7b19cda.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

32 recorded events

### Assistant

_source line 1 · 2026-05-14T22:35:03.187757+00:00_

You've hit your limit · resets May 16, 9am (UTC)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analyze_mistral_hires_bf16_2bitonly_v4_20260514T223456"
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-14T22:36:22.212845+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__read_registry",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_mistral_hires_bf16_2bitonly_v4_20260514T223456",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__read_registry",
    "max_results": "5"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-14T22:36:22.213176+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_mistral_hires_bf16_2bitonly_v4_20260514T223456",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-14T22:36:22.213348+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-37397",
  "command": "tail -200 ~/runs/ratekv/mistral_hires_bf16_2bitonly_v4.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_mistral_hires_bf16_2bitonly_v4_20260514T223456",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-37397",
    "command": "tail -200 ~/runs/ratekv/mistral_hires_bf16_2bitonly_v4.log",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-14T22:36:22.213516+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-37397",
  "command": "find /root/runs/ratekv /root/ratekv -name \"*mistral*hires*\" -type f 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_mistral_hires_bf16_2bitonly_v4_20260514T223456",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-37397",
    "command": "find /root/runs/ratekv /root/ratekv -name \"*mistral*hires*\" -type f 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-14T22:36:22.213817+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[80/256] L9H7 @2bit: delta=0.021237  (elapsed 17.7min, ETA 39min)\\n[81/256] L10H0 @2bit: delta=0.025035  (elapsed 18.0min, ETA 39min)\\n[82/256] L10H1 @2bit: delta=0.024232  (elapsed 18.2min, ETA 39min)\\n[83/256] L10H2 @2bit: delta=0.023533  (elapsed 18.4min, ETA 38min)\\n[84/256] L10H3 @2bit: delta=0.017504  (elapsed 18.6min, ETA 38min)\\n[85/256] L10H4 @2bit: delta=0.014976  (elapsed 18.8min, ETA 38min)\\n[86/256] L10H5 @2bit: delta=0.013388  (elapsed 19.1min, ETA 38min)\\n[87/256] L10H6 @2bit: delta=0.016985  (elapsed 19.3min, ETA 37min)\\n[88/256] L10H7 @2bit: delta=0.021309  (elapsed 19.5min, ETA 37min)\\n[89/256] L11H0 @2bit: delta=0.015920  (elapsed 19.7min, ETA 37min)\\n[90/256] L11H1 @2bit: delta=0.008696  (elapsed 19.9min, ETA 37min)\\n[91/256] L11H2 @2bit: delta=0.030477  (elapsed 20.1min, ETA 37min)\\n[92/256] L11H3 @2bit: delta=0.022901  (elapsed 20.4min, ETA 36min)\\n[93/256] L11H4 @2bit: delta=0.060331  (elapsed 20.6min, ETA 36min)\\n[94/256] L11H5 @2bit: delta=0.030929  (elapsed 20.8min, ETA 36min)\\n[95/256] L11H6 @2bit: delta=0.030125  (elapsed 21.0min, ETA 36min)\\n[96/256] L11H7 @2bit: delta=0.020649  (elapsed 21.2min, ETA 35min)\\n[97/256] L12H0 @2bit: delta=0.017830  (elapsed 21.5min, ETA 35min)\\n[98/256] L12H1 @2bit: delta=0.143529  (elapsed 21.7min, ETA 35min)\\n[99/256] L12H2 @2bit: delta=0.052889  (elapsed 21.9min, ETA 35min)\\n[100/256] L12H3 @2bit: delta=0.017522  (elapsed 22.1min, ETA 34min)\\n[101/256] L12H4 @2bit: delta=0.012627  (elapsed 22.3min, ETA 34min)\\n[102/256] L12H5 @2bit: delta=0.012516  (elapsed 22.5min, ETA 34min)\\n[103/256] L12H6 @2bit: delta=0.019338  (elapsed 22.8min, ETA 34min)\\n[104/256] L12H7 @2bit: delta=0.053418  (elapsed 23.0min, ETA 34min)\\n[105/256] L13H0 @2bit: delta=0.013680  (elapsed 23.2min, ETA 33min)\\n[106/256] L13H1 @2bit: delta=0.023139  (elapsed 23.4min, ETA 33min)\\n[107/256] L13H2 @2bit: delta=0.018155  (elapsed 23.6min, ETA 33min)\\n[108/
…[truncated 6467 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_mistral_hires_bf16_2bitonly_v4_20260514T223456",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-14T22:36:22.213992+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_mistral_hires_bf16_2bitonly_v4_20260514T223456",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-14T22:36:22.214152+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-37397",
  "command": "find /root -name \"mistral_hires_bf16_2bitonly*\" -type f 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_mistral_hires_bf16_2bitonly_v4_20260514T223456",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-37397",
    "command": "find /root -name \"mistral_hires_bf16_2bitonly*\" -type f 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-14T22:36:22.214284+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_mistral_hires_bf16_2bitonly_v4_20260514T223456",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-14T22:36:22.214406+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-37397",
  "command": "head -100 /root/runs/ratekv/mistral_hires_bf16_2bitonly_v4.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_mistral_hires_bf16_2bitonly_v4_20260514T223456",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-37397",
    "command": "head -100 /root/runs/ratekv/mistral_hires_bf16_2bitonly_v4.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-14T22:36:22.214596+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"`torch_dtype` is deprecated! Use `dtype` instead!\\nMistral-7B-v0.3: 32L x 8KV, GQA 4:1, 256 total heads\\n\\n============================================================\\nBF16 2-bit-only Profiling (64seq x 2048tok)\\n============================================================\\nLoading model in bf16 to cuda:0...\\n\\rLoading checkpoint shards:   0%|          | 0/3 [00:00<?, ?it/s]\\rLoading checkpoint shards: 100%|██████████| 3/3 [00:00<00:00, 180.66it/s]\\nBF16 model loaded. GPU mem: 14.5GB\\nCalibration: 64 seqs x 2048 tokens\\nComputing baseline PPL...\\nBaseline PPL: 5.8702\\n[1/256] L0H0 @2bit: delta=0.004249  (elapsed 0.5min, ETA 129min)\\n[2/256] L0H1 @2bit: delta=0.072928  (elapsed 0.7min, ETA 92min)\\n[3/256] L0H2 @2bit: delta=0.006655  (elapsed 0.9min, ETA 79min)\\n[4/256] L0H3 @2bit: delta=0.034296  (elapsed 1.2min, ETA 73min)\\n[5/256] L0H4 @2bit: delta=-0.001210  (elapsed 1.4min, ETA 69min)\\n[6/256] L0H5 @2bit: delta=0.000527  (elapsed 1.6min, ETA 67min)\\n[7/256] L0H6 @2bit: delta=0.014860  (elapsed 1.8min, ETA 65min)\\n[8/256] L0H7 @2bit: delta=0.140279  (elapsed 2.0min, ETA 63min)\\n[9/256] L1H0 @2bit: delta=0.023962  (elapsed 2.2min, ETA 62min)\\n[10/256] L1H1 @2bit: delta=0.009109  (elapsed 2.5min, ETA 61min)\\n[11/256] L1H2 @2bit: delta=0.071380  (elapsed 2.7min, ETA 60min)\\n[12/256] L1H3 @2bit: delta=0.010372  (elapsed 2.9min, ETA 59min)\\n[13/256] L1H4 @2bit: delta=0.023654  (elapsed 3.1min, ETA 58min)\\n[14/256] L1H5 @2bit: delta=0.028810  (elapsed 3.3min, ETA 58min)\\n[15/256] L1H6 @2bit: delta=0.008602  (elapsed 3.6min, ETA 57min)\\n[16/256] L1H7 @2bit: delta=0.007972  (elapsed 3.8min, ETA 57min)\\n[17/256] L2H0 @2bit: delta=0.083626  (elapsed 4.0min, ETA 56min)\\n[18/256] L2H1 @2bit: delta=0.039008  (elapsed 4.2min, ETA 56min)\\n[19/256] L2H2 @2bit: delta=0.025973  (elapsed 4.4min, ETA 55min)\\n[20/256] L2H3 @2bit: delta=0.051720  (elapsed 4.7min, ETA 55min)\\n[21/256] L2H4 @2bit: 
…[truncated 4691 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_mistral_hires_bf16_2bitonly_v4_20260514T223456",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-14T22:36:22.214824+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-37397",
  "command": "find /root -name \"mistral_hires_bf16_2bitonly*\" -type f",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_mistral_hires_bf16_2bitonly_v4_20260514T223456",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-37397",
    "command": "find /root -name \"mistral_hires_bf16_2bitonly*\" -type f",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-14T22:36:22.214978+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/runs/ratekv/mistral_hires_bf16_2bitonly_v2.log\\n/root/runs/ratekv/mistral_hires_bf16_2bitonly_v3.log\\n/root/runs/ratekv/mistral_hires_bf16_2bitonly_v4.log\\n/root/ratekv/logs/mistral_hires_bf16_2bitonly.log\\n/root/ratekv/mistral_hires_bf16_2bitonly_profiles.json\\n/root/ratekv/mistral_hires_bf16_2bitonly_results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.67}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_mistral_hires_bf16_2bitonly_v4_20260514T223456",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-14T22:36:22.215115+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-37397",
  "command": "cat /root/ratekv/mistral_hires_bf16_2bitonly_results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_mistral_hires_bf16_2bitonly_v4_20260514T223456",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-37397",
    "command": "cat /root/ratekv/mistral_hires_bf16_2bitonly_results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-14T22:36:22.215278+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"model\\\": \\\"/root/autodl-tmp/models/Mistral-7B-v0.3\\\",\\n  \\\"model_name\\\": \\\"Mistral-7B-v0.3\\\",\\n  \\\"precision\\\": \\\"bfloat16\\\",\\n  \\\"profiling_config\\\": {\\n    \\\"num_samples\\\": 64,\\n    \\\"seq_len\\\": 2048,\\n    \\\"batch_size\\\": 2,\\n    \\\"bitwidths\\\": [\\n      2\\n    ]\\n  },\\n  \\\"architecture\\\": {\\n    \\\"num_layers\\\": 32,\\n    \\\"num_kv_heads\\\": 8,\\n    \\\"num_attention_heads\\\": 32,\\n    \\\"head_dim\\\": 128,\\n    \\\"hidden_size\\\": 4096,\\n    \\\"gqa_ratio\\\": 4,\\n    \\\"total_kv_heads\\\": 256\\n  },\\n  \\\"baseline_calibration_ppl\\\": 5.870169135704824,\\n  \\\"analysis\\\": {\\n    \\\"top5_concentration\\\": 0.241,\\n    \\\"top5_n_heads\\\": 12,\\n    \\\"layer0_mean_delta_2bit\\\": 0.034073,\\n    \\\"other_layers_mean_delta_2bit\\\": 0.019621,\\n    \\\"layer0_dominance_ratio\\\": 1.74,\\n    \\\"delta_2bit_mean\\\": 0.020073,\\n    \\\"delta_2bit_std\\\": 0.026278,\\n    \\\"delta_2bit_cv\\\": 1.3091,\\n    \\\"heads_with_positive_delta\\\": 252,\\n    \\\"total_heads\\\": 256\\n  },\\n  \\\"top5_sensitive_heads\\\": [\\n    {\\n      \\\"layer\\\": 2,\\n      \\\"head\\\": 5,\\n      \\\"delta_2bit\\\": 0.323556\\n    },\\n    {\\n      \\\"layer\\\": 12,\\n      \\\"head\\\": 1,\\n      \\\"delta_2bit\\\": 0.143529\\n    },\\n    {\\n      \\\"layer\\\": 0,\\n      \\\"head\\\": 7,\\n      \\\"delta_2bit\\\": 0.140279\\n    },\\n    {\\n      \\\"layer\\\": 7,\\n      \\\"head\\\": 4,\\n      \\\"delta_2bit\\\": 0.097342\\n    },\\n    {\\n      \\\"layer\\\": 2,\\n      \\\"head\\\": 4,\\n      \\\"delta_2bit\\\": 0.084672\\n    }\\n  ],\\n  \\\"timing\\\": {\\n    \\\"profile_seconds\\\": 3371.7,\\n    \\\"total_seconds\\\": 3371.7\\n  }\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_mistral_hires_bf16_2bitonly_v4_20260514T223456",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-14T22:36:22.215456+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "ratekv",
  "filters": "{'exp_id': 'mistral_hires_bf16_2bitonly_v4'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_mistral_hires_bf16_2bitonly_v4_20260514T223456",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "ratekv",
    "filters": "{'exp_id': 'mistral_hires_bf16_2bitonly_v4'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-14T22:36:22.215599+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.1518}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_mistral_hires_bf16_2bitonly_v4_20260514T223456",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-14T22:36:22.215744+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "ratekv",
  "filters": "{}",
  "fields": "['exp_id', 'status', 'conclusion']",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_mistral_hires_bf16_2bitonly_v4_20260514T223456",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "ratekv",
    "filters": "{}",
    "fields": "['exp_id', 'status', 'conclusion']",
    "limit": "30"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-14T22:36:22.215987+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"mistral_hires_bf16_2bitonly_v4\": {\"status\": \"ANALYZING\"}, \"gemma2_hires_bf16_2bitonly\": {\"status\": \"ANALYZING\"}, \"llama_hires_constrained_mckp\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"llama_hires_bf16_2bitonly\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"mistral_hires_bf16_2bitonly_v3\": {\"status\": \"PREPARING\", \"conclusion\": \"killed\"}, \"mistral_hires_bf16_2bitonly_v2\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"mistral_hires_bf16_2bitonly\": {\"status\": \"DONE\", \"conclusion\": \"failed\"}, \"yi15_hires_constrained_mckp\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"yi15_hires_bf16_2bitonly\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"qwen_hires_constrained_d049\": {\"status\": \"PREPARING\", \"conclusion\": \"success\"}, \"qwen_hires_float32_d048\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"yi15_hires_float32_profiling\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"yi15_9b_full_pipeline\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"gemma2_9b_full_pipeline\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"qwen25-hires-profiling\": {\"status\": \"PREPARING\", \"conclusion\": \"killed\"}, \"qwen72b_profiling\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"cross_domain_calibration_v2\": {\"status\": \"PREPARING\", \"conclusion\": \"killed\"}, \"greedy_constrained_ablation\": {\"status\": \"PREPARING\", \"conclusion\": \"killed\"}, \"multi_seed_lowres\": {\"status\": \"DONE\", \"conclusion\": \"killed\"}, \"mistral_c4_cross_dataset\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"llama_c4_cross_dataset\": {\"status\": \"DONE\", \"conclusion\": \"negative\"}, \"mistral_heuristic_k4\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"llama_heuristic_k2\": {\"status\": \"DONE\", \"conclusion\": \"success\"}, \"plan_009_oracle_comparison\": {\"status\": \"
…[truncated 623 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_mistral_hires_bf16_2bitonly_v4_20260514T223456",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-14T22:36:22.216386+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "project": "ratekv",
  "exp_id": "mistral_hires_bf16_2bitonly_v4",
  "field": "log_path",
  "value": "/root/runs/ratekv/mistral_hires_bf16_2bitonly_v4.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_mistral_hires_bf16_2bitonly_v4_20260514T223456",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "project": "ratekv",
    "exp_id": "mistral_hires_bf16_2bitonly_v4",
    "field": "log_path",
    "value": "/root/runs/ratekv/mistral_hires_bf16_2bitonly_v4.log"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-14T22:36:22.216695+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"mistral_hires_bf16_2bitonly_v4\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T21:37:30.245Z\", \"updated_at\": \"2026-05-14T22:35:53.327Z\", \"hypothesis\": \"Mistral-7B-v0.3 hires bf16 2-bit only profiling (model re-downloaded from HF, fixed cuda device). 64seq x 2048tok, 224 heads x ~20s/head ≈ 1.2h.\", \"spec\": {\"command\": \"python run_mistral_hires_bf16_2bitonly.py --model /root/autodl-tmp/models/Mistral-7B-v0.3 --gpu cuda:0 --batch_size 2\", \"server\": \"westd-37397\", \"gpu\": [\"cuda:1\"], \"pid\": \"264489\", \"log_path\": \"~/runs/ratekv/mistral_hires_bf16_2bitonly_v4.log\", \"submitted_at\": \"2026-05-14T21:37:37.281Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/ratekv/calibration_hires.json\", \"data_count\": 64, \"model_name\": \"Mistral-7B-v0.3\", \"seed\": 0, \"model_path\": \"/root/autodl-tmp/models/Mistral-7B-v0.3\", \"gpu_model\": \"RTX PRO 6000 96GB\", \"checkpoint_path\": \"/root/ratekv/mistral_hires_bf16_2bitonly_results.json\"}, \"reproduce\": {\"finished_at\": \"2026-05-14T22:33:55.762Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T22:34:00.058792+00:00\"}]}, \"log_path\": \"/root/runs/ratekv/mistral_hires_bf16_2bitonly_v4.log\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2577}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_mistral_hires_bf16_2bitonly_v4_20260514T223456",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-14T22:36:22.216940+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "project": "ratekv",
  "exp_id": "mistral_hires_bf16_2bitonly_v4",
  "field": "checkpoint_path",
  "value": "/root/ratekv/mistral_hires_bf16_2bitonly_profiles.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_mistral_hires_bf16_2bitonly_v4_20260514T223456",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "project": "ratekv",
    "exp_id": "mistral_hires_bf16_2bitonly_v4",
    "field": "checkpoint_path",
    "value": "/root/ratekv/mistral_hires_bf16_2bitonly_profiles.json"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-14T22:36:22.217124+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"mistral_hires_bf16_2bitonly_v4\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T21:37:30.245Z\", \"updated_at\": \"2026-05-14T22:35:54.083Z\", \"hypothesis\": \"Mistral-7B-v0.3 hires bf16 2-bit only profiling (model re-downloaded from HF, fixed cuda device). 64seq x 2048tok, 224 heads x ~20s/head ≈ 1.2h.\", \"spec\": {\"command\": \"python run_mistral_hires_bf16_2bitonly.py --model /root/autodl-tmp/models/Mistral-7B-v0.3 --gpu cuda:0 --batch_size 2\", \"server\": \"westd-37397\", \"gpu\": [\"cuda:1\"], \"pid\": \"264489\", \"log_path\": \"~/runs/ratekv/mistral_hires_bf16_2bitonly_v4.log\", \"submitted_at\": \"2026-05-14T21:37:37.281Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/ratekv/calibration_hires.json\", \"data_count\": 64, \"model_name\": \"Mistral-7B-v0.3\", \"seed\": 0, \"model_path\": \"/root/autodl-tmp/models/Mistral-7B-v0.3\", \"gpu_model\": \"RTX PRO 6000 96GB\", \"checkpoint_path\": \"/root/ratekv/mistral_hires_bf16_2bitonly_results.json\"}, \"reproduce\": {\"finished_at\": \"2026-05-14T22:33:55.762Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T22:34:00.058792+00:00\"}]}, \"log_path\": \"/root/runs/ratekv/mistral_hires_bf16_2bitonly_v4.log\", \"checkpoint_path\": \"/root/ratekv/mistral_hires_bf16_2bitonly_profiles.json\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2874}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_mistral_hires_bf16_2bitonly_v4_20260514T223456",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-14T22:36:22.217291+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "project": "ratekv",
  "exp_id": "mistral_hires_bf16_2bitonly_v4",
  "field": "metrics",
  "value": "{'top5_concentration': 0.241, 'top5_n_heads': 12, 'baseline_ppl': 5.8702, 'top1_head': 'L2H5', 'top1_delta_2bit': 0.3236, 'top2_head': 'L12H1', 'top2_delta_2bit': 0.1435, 'top3_head': 'L0H7', 'top3_delta_2bit': 0.1403, 'delta_2bit_mean': 0.020073, 'delta_2bit_std': 0.026278, 'delta_2bit_cv': 1.3091, 'layer0_mean_delta_2bit': 0.034073, 'other_layers_mean_delta_2bit': 0.019621, 'l0_dominance_ratio': 1.74, 'positive_delta_heads': 252, 'total_heads': 256, 'distribution_shape': 'flat', 'total_hours': 0.94, 'profile_seconds': 3371.7}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_mistral_hires_bf16_2bitonly_v4_20260514T223456",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "project": "ratekv",
    "exp_id": "mistral_hires_bf16_2bitonly_v4",
    "field": "metrics",
    "value": "{'top5_concentration': 0.241, 'top5_n_heads': 12, 'baseline_ppl': 5.8702, 'top1_head': 'L2H5', 'top1_delta_2bit': 0.3236, 'top2_head': 'L12H1', 'top2_delta_2bit': 0.1435, 'top3_head': 'L0H7', 'top3_delta_2bit': 0.1403, 'delta_2bit_mean': 0.020073, 'delta_2bit_std': 0.026278, 'delta_2bit_cv': 1.3091, 'layer0_mean_delta_2bit': 0.034073, 'other_layers_mean_delta_2bit': 0.019621, 'l0_dominance_ratio': 1.74, 'positive_delta_heads': 252, 'total_heads': 256, 'distribution_shape': 'flat', 'total_hours': 0.94, 'profile_seconds': 3371.7}"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-14T22:36:22.217490+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"mistral_hires_bf16_2bitonly_v4\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T21:37:30.245Z\", \"updated_at\": \"2026-05-14T22:36:00.735Z\", \"hypothesis\": \"Mistral-7B-v0.3 hires bf16 2-bit only profiling (model re-downloaded from HF, fixed cuda device). 64seq x 2048tok, 224 heads x ~20s/head ≈ 1.2h.\", \"spec\": {\"command\": \"python run_mistral_hires_bf16_2bitonly.py --model /root/autodl-tmp/models/Mistral-7B-v0.3 --gpu cuda:0 --batch_size 2\", \"server\": \"westd-37397\", \"gpu\": [\"cuda:1\"], \"pid\": \"264489\", \"log_path\": \"~/runs/ratekv/mistral_hires_bf16_2bitonly_v4.log\", \"submitted_at\": \"2026-05-14T21:37:37.281Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/ratekv/calibration_hires.json\", \"data_count\": 64, \"model_name\": \"Mistral-7B-v0.3\", \"seed\": 0, \"model_path\": \"/root/autodl-tmp/models/Mistral-7B-v0.3\", \"gpu_model\": \"RTX PRO 6000 96GB\", \"checkpoint_path\": \"/root/ratekv/mistral_hires_bf16_2bitonly_results.json\"}, \"reproduce\": {\"finished_at\": \"2026-05-14T22:33:55.762Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T22:34:00.058792+00:00\"}]}, \"log_path\": \"/root/runs/ratekv/mistral_hires_bf16_2bitonly_v4.log\", \"checkpoint_path\": \"/root/ratekv/mistral_hires_bf16_2bitonly_profiles.json\", \"metrics\": {\"top5_concentration\": 0.241, \"top5_n_heads\": 12, \"baseline_ppl\": 5.8702, \"top1_head\": \"L2H5\", \"top1_delta_2bit\": 0.3236, \"top2_head\": \"L12H1\", \"top2_delta_2bit\": 0.1435, \"top3_head\": \"L0H7\", \"top3_delta_2bit\": 0.1403, \"delta_2bit_mean\": 0.020073, \"delta_2bit_std\": 0.026278, \"delta_2bit_cv\": 1.3091, \"layer0_mean_delta_2bit\": 0.034073, \"other_layers_mean_delta_2bit\": 0.019621, \"l0_dominance_ratio\": 1.74, \"positive_delta_heads\": 252, \"total_heads\": 256,
…[truncated 153 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_mistral_hires_bf16_2bitonly_v4_20260514T223456",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-14T22:36:22.217670+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "project": "ratekv",
  "exp_id": "mistral_hires_bf16_2bitonly_v4",
  "field": "notes",
  "value": "Mistral-7B-v0.3 hires bf16 2-bit profiling completed (v4, after 3 prior failures from corrupted model files). 256 KV heads (32L x 8H, GQA 4:1). Top-5% concentration = 0.241 (12 heads) → FLAT distribution, confirming Mistral standard profiling result (0.22). L0 dominance only 1.74x (weak). Top-3 sensitive heads: L2H5 (0.324, single-head outlier ~6% of total delta), L12H1 (0.144), L0H7 (0.140). 252/256 heads have positive delta (high diffusion). CV=1.31. Baseline PPL=5.87. Profiling time 56.2min. Mistral confirmed as genuine flat/low-heterogeneity model — single L2H5 spike does not concentrate enough mass to qualify as 'spike' pattern. Complements 5-model hires concentration panorama: Llama 0.51, Yi-1.5 0.27, Gemma-2 (pending), Qwen2.5 0.61, Mistral 0.24."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_mistral_hires_bf16_2bitonly_v4_20260514T223456",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "project": "ratekv",
    "exp_id": "mistral_hires_bf16_2bitonly_v4",
    "field": "notes",
    "value": "Mistral-7B-v0.3 hires bf16 2-bit profiling completed (v4, after 3 prior failures from corrupted model files). 256 KV heads (32L x 8H, GQA 4:1). Top-5% concentration = 0.241 (12 heads) → FLAT distribution, confirming Mistral standard profiling result (0.22). L0 dominance only 1.74x (weak). Top-3 sensitive heads: L2H5 (0.324, single-head outlier ~6% of total delta), L12H1 (0.144), L0H7 (0.140). 252/256 heads have positive delta (high diffusion). CV=1.31. Baseline PPL=5.87. Profiling time 56.2min. Mistral confirmed as genuine flat/low-heterogeneity model — single L2H5 spike does not concentrate enough mass to qualify as 'spike' pattern. Complements 5-model hires concentration panorama: Llama 0.51, Yi-1.5 0.27, Gemma-2 (pending), Qwen2.5 0.61, Mistral 0.24."
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-14T22:36:22.217885+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"mistral_hires_bf16_2bitonly_v4\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T21:37:30.245Z\", \"updated_at\": \"2026-05-14T22:36:04.938Z\", \"hypothesis\": \"Mistral-7B-v0.3 hires bf16 2-bit only profiling (model re-downloaded from HF, fixed cuda device). 64seq x 2048tok, 224 heads x ~20s/head ≈ 1.2h.\", \"spec\": {\"command\": \"python run_mistral_hires_bf16_2bitonly.py --model /root/autodl-tmp/models/Mistral-7B-v0.3 --gpu cuda:0 --batch_size 2\", \"server\": \"westd-37397\", \"gpu\": [\"cuda:1\"], \"pid\": \"264489\", \"log_path\": \"~/runs/ratekv/mistral_hires_bf16_2bitonly_v4.log\", \"submitted_at\": \"2026-05-14T21:37:37.281Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/ratekv/calibration_hires.json\", \"data_count\": 64, \"model_name\": \"Mistral-7B-v0.3\", \"seed\": 0, \"model_path\": \"/root/autodl-tmp/models/Mistral-7B-v0.3\", \"gpu_model\": \"RTX PRO 6000 96GB\", \"checkpoint_path\": \"/root/ratekv/mistral_hires_bf16_2bitonly_results.json\"}, \"reproduce\": {\"finished_at\": \"2026-05-14T22:33:55.762Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T22:34:00.058792+00:00\"}]}, \"log_path\": \"/root/runs/ratekv/mistral_hires_bf16_2bitonly_v4.log\", \"checkpoint_path\": \"/root/ratekv/mistral_hires_bf16_2bitonly_profiles.json\", \"metrics\": {\"top5_concentration\": 0.241, \"top5_n_heads\": 12, \"baseline_ppl\": 5.8702, \"top1_head\": \"L2H5\", \"top1_delta_2bit\": 0.3236, \"top2_head\": \"L12H1\", \"top2_delta_2bit\": 0.1435, \"top3_head\": \"L0H7\", \"top3_delta_2bit\": 0.1403, \"delta_2bit_mean\": 0.020073, \"delta_2bit_std\": 0.026278, \"delta_2bit_cv\": 1.3091, \"layer0_mean_delta_2bit\": 0.034073, \"other_layers_mean_delta_2bit\": 0.019621, \"l0_dominance_ratio\": 1.74, \"positive_delta_heads\": 252, \"total_heads\": 256,
…[truncated 932 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_mistral_hires_bf16_2bitonly_v4_20260514T223456",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-14T22:36:22.218041+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "project": "ratekv",
  "exp_id": "mistral_hires_bf16_2bitonly_v4",
  "field": "conclusion",
  "value": "success"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_mistral_hires_bf16_2bitonly_v4_20260514T223456",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "project": "ratekv",
    "exp_id": "mistral_hires_bf16_2bitonly_v4",
    "field": "conclusion",
    "value": "success"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-14T22:36:22.218216+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"mistral_hires_bf16_2bitonly_v4\", \"experiment\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T21:37:30.245Z\", \"updated_at\": \"2026-05-14T22:36:08.165Z\", \"hypothesis\": \"Mistral-7B-v0.3 hires bf16 2-bit only profiling (model re-downloaded from HF, fixed cuda device). 64seq x 2048tok, 224 heads x ~20s/head ≈ 1.2h.\", \"spec\": {\"command\": \"python run_mistral_hires_bf16_2bitonly.py --model /root/autodl-tmp/models/Mistral-7B-v0.3 --gpu cuda:0 --batch_size 2\", \"server\": \"westd-37397\", \"gpu\": [\"cuda:1\"], \"pid\": \"264489\", \"log_path\": \"~/runs/ratekv/mistral_hires_bf16_2bitonly_v4.log\", \"submitted_at\": \"2026-05-14T21:37:37.281Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/ratekv/calibration_hires.json\", \"data_count\": 64, \"model_name\": \"Mistral-7B-v0.3\", \"seed\": 0, \"model_path\": \"/root/autodl-tmp/models/Mistral-7B-v0.3\", \"gpu_model\": \"RTX PRO 6000 96GB\", \"checkpoint_path\": \"/root/ratekv/mistral_hires_bf16_2bitonly_results.json\"}, \"reproduce\": {\"finished_at\": \"2026-05-14T22:33:55.762Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T22:34:00.058792+00:00\"}]}, \"log_path\": \"/root/runs/ratekv/mistral_hires_bf16_2bitonly_v4.log\", \"checkpoint_path\": \"/root/ratekv/mistral_hires_bf16_2bitonly_profiles.json\", \"metrics\": {\"top5_concentration\": 0.241, \"top5_n_heads\": 12, \"baseline_ppl\": 5.8702, \"top1_head\": \"L2H5\", \"top1_delta_2bit\": 0.3236, \"top2_head\": \"L12H1\", \"top2_delta_2bit\": 0.1435, \"top3_head\": \"L0H7\", \"top3_delta_2bit\": 0.1403, \"delta_2bit_mean\": 0.020073, \"delta_2bit_std\": 0.026278, \"delta_2bit_cv\": 1.3091, \"layer0_mean_delta_2bit\": 0.034073, \"other_layers_mean_delta_2bit\": 0.019621, \"l0_dominance_ratio\": 1.74, \"positive_delta_heads\": 252, \"total_heads\": 256,
…[truncated 962 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_mistral_hires_bf16_2bitonly_v4_20260514T223456",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-14T22:36:22.218379+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "project": "ratekv",
  "exp_id": "mistral_hires_bf16_2bitonly_v4",
  "field": "status",
  "value": "DONE"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analyze_mistral_hires_bf16_2bitonly_v4_20260514T223456",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "project": "ratekv",
    "exp_id": "mistral_hires_bf16_2bitonly_v4",
    "field": "status",
    "value": "DONE"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-14T22:36:22.218582+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"mistral_hires_bf16_2bitonly_v4\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T21:37:30.245Z\", \"updated_at\": \"2026-05-14T22:36:11.035Z\", \"hypothesis\": \"Mistral-7B-v0.3 hires bf16 2-bit only profiling (model re-downloaded from HF, fixed cuda device). 64seq x 2048tok, 224 heads x ~20s/head ≈ 1.2h.\", \"spec\": {\"command\": \"python run_mistral_hires_bf16_2bitonly.py --model /root/autodl-tmp/models/Mistral-7B-v0.3 --gpu cuda:0 --batch_size 2\", \"server\": \"westd-37397\", \"gpu\": [\"cuda:1\"], \"pid\": \"264489\", \"log_path\": \"~/runs/ratekv/mistral_hires_bf16_2bitonly_v4.log\", \"submitted_at\": \"2026-05-14T21:37:37.281Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/ratekv/calibration_hires.json\", \"data_count\": 64, \"model_name\": \"Mistral-7B-v0.3\", \"seed\": 0, \"model_path\": \"/root/autodl-tmp/models/Mistral-7B-v0.3\", \"gpu_model\": \"RTX PRO 6000 96GB\", \"checkpoint_path\": \"/root/ratekv/mistral_hires_bf16_2bitonly_results.json\", \"wall_clock_seconds\": 3513.8, \"gpu_hours\": 0.98}, \"reproduce\": {\"finished_at\": \"2026-05-14T22:33:55.762Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T22:34:00.058792+00:00\"}]}, \"log_path\": \"/root/runs/ratekv/mistral_hires_bf16_2bitonly_v4.log\", \"checkpoint_path\": \"/root/ratekv/mistral_hires_bf16_2bitonly_profiles.json\", \"metrics\": {\"top5_concentration\": 0.241, \"top5_n_heads\": 12, \"baseline_ppl\": 5.8702, \"top1_head\": \"L2H5\", \"top1_delta_2bit\": 0.3236, \"top2_head\": \"L12H1\", \"top2_delta_2bit\": 0.1435, \"top3_head\": \"L0H7\", \"top3_delta_2bit\": 0.1403, \"delta_2bit_mean\": 0.020073, \"delta_2bit_std\": 0.026278, \"delta_2bit_cv\": 1.3091, \"layer0_mean_delta_2bit\": 0.034073, \"other_layers_mean_delta_2bit\": 0.019621, \"l0_dominance_ratio\": 1.74, \"po
…[truncated 1109 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analyze_mistral_hires_bf16_2bitonly_v4_20260514T223456",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 32 · 2026-05-14T22:36:22.218820+00:00_

Registry 已更新为 DONE / success。

## mistral_hires_bf16_2bitonly_v4 结果总结

**实验完成** — Mistral-7B-v0.3 hires bf16 2-bit profiling（v4，前3次因模型文件损坏失败）

### 核心指标
| 指标 | 数值 |
|------|------|
| **top5_concentration** | **0.241** (12 / 256 heads) |
| baseline_ppl | 5.8702 |
| top1_head | **L2H5** (delta=0.3236) |
| top2_head | L12H1 (delta=0.1435) |
| top3_head | L0H7 (delta=0.1403) |
| delta_2bit_cv | 1.3091 |
| L0 dominance ratio | 1.74x (weak) |
| positive_delta_heads | 252 / 256 (98.4%) |
| total_hours | 0.94h (56.2min profiling) |

### 关键发现
- **Distribution shape: FLAT** (concentration 0.241 < 0.30 阈值)
- Mistral 在 hires 下 concentration (0.241) 与 standard profiling (0.22) 几乎一致 → **确认为 genuine flat / low-heterogeneity 模型**
- 虽然 L2H5 是单一最大 head (delta=0.324)，但其只占总 delta 的约 6% — 不足以构成 "spike" 模式
- 98.4% heads 有正 delta，扩散性极高（CV=1.31 同时也较低）
- L0 dominance 仅 1.74x，远弱于 spike 类模型

### 5 模型 hires concentration 全景图
- Qwen2.5-7B: 0.61 (spike)
- Llama-3.1-8B: 0.51 (moderate-spike)
- Yi-1.5-9B: 0.27 (flat)
- **Mistral-7B-v0.3: 0.24 (flat) ← 本次**
- Gemma-2: pending

### 产物
- log: `/root/runs/ratekv/mistral_hires_bf16_2bitonly_v4.log`
- profiles JSON: `/root/ratekv/mistral_hires_bf16_2bitonly_profiles.json`
- results JSON: `/root/ratekv/mistral_hires_bf16_2bitonly_results.json`

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analyze_mistral_hires_bf16_2bitonly_v4_20260514T223456"
}
```

</details>

---
