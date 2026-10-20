# ops cross family v5 extraction

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 29
- **Recorded user turns:** 0
- **Tool calls:** 14
- **Original source:** `logs/chats/worker_ops_cross_family_v5_extraction_20260517T131825.jsonl`
- **Structured JSON:** [`b32b73bb61c077ca0d6d.json`](../../sessions/b3/b32b73bb61c077ca0d6d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

29 recorded events

### Tool call

_source line 1 · 2026-05-17T13:22:21.241937+00:00_

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
  "session": "worker_ops_cross_family_v5_extraction_20260517T131825",
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

_source line 2 · 2026-05-17T13:22:21.242284+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_cross_family_v5_extraction_20260517T131825",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-17T13:22:21.242497+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "find /root/autodl-tmp/exp006/cross_family_v5/ -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_cross_family_v5_extraction_20260517T131825",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "find /root/autodl-tmp/exp006/cross_family_v5/ -type f"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-17T13:22:21.242649+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/exp006/cross_family_v5/exposure_scores_v5.json\\n/root/autodl-tmp/exp006/cross_family_v5/run_v5.log\\n/root/autodl-tmp/exp006/cross_family_v5/mmlu/irt_results.json\\n/root/autodl-tmp/exp006/cross_family_v5/gsm8k/irt_results.json\\n/root/autodl-tmp/exp006/cross_family_v5/arc_challenge/irt_results.json\\n/root/autodl-tmp/exp006/cross_family_v5/pooled_rrf_irt_results.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.91}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_cross_family_v5_extraction_20260517T131825",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-17T13:22:21.242781+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat /root/autodl-tmp/exp006/cross_family_v5/arc_challenge/irt_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_cross_family_v5_extraction_20260517T131825",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat /root/autodl-tmp/exp006/cross_family_v5/arc_challenge/irt_results.json"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-17T13:22:21.243042+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"benchmark\\\": \\\"arc_challenge\\\",\\n  \\\"model_type\\\": \\\"2pl_gamma\\\",\\n  \\\"exposure_source\\\": \\\"rrf_signal\\\",\\n  \\\"n_models\\\": 20,\\n  \\\"n_items\\\": 300,\\n  \\\"original_n_items\\\": 1172,\\n  \\\"subsampled\\\": true,\\n  \\\"models\\\": [\\n    {\\n      \\\"dirname\\\": \\\"Qwen2.5-1.5B_d000_s123_aligned\\\",\\n      \\\"scale\\\": \\\"1.5B\\\",\\n      \\\"dosage\\\": 0\\n    },\\n    {\\n      \\\"dirname\\\": \\\"Qwen2.5-1.5B_d000_s42_aligned\\\",\\n      \\\"scale\\\": \\\"1.5B\\\",\\n      \\\"dosage\\\": 0\\n    },\\n    {\\n      \\\"dirname\\\": \\\"Qwen2.5-1.5B_d005_s123_aligned\\\",\\n      \\\"scale\\\": \\\"1.5B\\\",\\n      \\\"dosage\\\": 5\\n    },\\n    {\\n      \\\"dirname\\\": \\\"Qwen2.5-1.5B_d005_s42_aligned\\\",\\n      \\\"scale\\\": \\\"1.5B\\\",\\n      \\\"dosage\\\": 5\\n    },\\n    {\\n      \\\"dirname\\\": \\\"Qwen2.5-1.5B_d025_s123_aligned\\\",\\n      \\\"scale\\\": \\\"1.5B\\\",\\n      \\\"dosage\\\": 25\\n    },\\n    {\\n      \\\"dirname\\\": \\\"Qwen2.5-1.5B_d025_s42_aligned\\\",\\n      \\\"scale\\\": \\\"1.5B\\\",\\n      \\\"dosage\\\": 25\\n    },\\n    {\\n      \\\"dirname\\\": \\\"Qwen2.5-1.5B_d100_s123_aligned\\\",\\n      \\\"scale\\\": \\\"1.5B\\\",\\n      \\\"dosage\\\": 100\\n    },\\n    {\\n      \\\"dirname\\\": \\\"Qwen2.5-1.5B_d100_s42_aligned\\\",\\n      \\\"scale\\\": \\\"1.5B\\\",\\n      \\\"dosage\\\": 100\\n    },\\n    {\\n      \\\"dirname\\\": \\\"Llama-3.2-3B_d000_s42_aligned\\\",\\n      \\\"scale\\\": \\\"3B\\\",\\n      \\\"dosage\\\": 0\\n    },\\n    {\\n      \\\"dirname\\\": \\\"Llama-3.2-3B_d005_s42_aligned\\\",\\n      \\\"scale\\\": \\\"3B\\\",\\n      \\\"dosage\\\": 5\\n    },\\n    {\\n      \\\"dirname\\\": \\\"Llama-3.2-3B_d025_s42_aligned\\\",\\n      \\\"scale\\\": \\\"3B\\\",\\n      \\\"dosage\\\": 25\\n    },\\n    {\\n      \\\"dirname\\\": \\\"Llama-3.2-3B_d100_s42_aligned\\\",\\n 
…[truncated 5358 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_cross_family_v5_extraction_20260517T131825",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-17T13:22:21.243217+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat /root/autodl-tmp/exp006/cross_family_v5/gsm8k/irt_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_cross_family_v5_extraction_20260517T131825",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat /root/autodl-tmp/exp006/cross_family_v5/gsm8k/irt_results.json"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-17T13:22:21.243532+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"benchmark\\\": \\\"gsm8k\\\",\\n  \\\"model_type\\\": \\\"2pl_gamma\\\",\\n  \\\"exposure_source\\\": \\\"rrf_signal\\\",\\n  \\\"n_models\\\": 28,\\n  \\\"n_items\\\": 300,\\n  \\\"original_n_items\\\": 1319,\\n  \\\"subsampled\\\": true,\\n  \\\"models\\\": [\\n    {\\n      \\\"dirname\\\": \\\"Qwen2.5-0.5B_d000_s123_aligned\\\",\\n      \\\"scale\\\": \\\"0.5B\\\",\\n      \\\"dosage\\\": 0\\n    },\\n    {\\n      \\\"dirname\\\": \\\"Qwen2.5-0.5B_d000_s42_aligned\\\",\\n      \\\"scale\\\": \\\"0.5B\\\",\\n      \\\"dosage\\\": 0\\n    },\\n    {\\n      \\\"dirname\\\": \\\"Qwen2.5-0.5B_d005_s123_aligned\\\",\\n      \\\"scale\\\": \\\"0.5B\\\",\\n      \\\"dosage\\\": 5\\n    },\\n    {\\n      \\\"dirname\\\": \\\"Qwen2.5-0.5B_d005_s42_aligned\\\",\\n      \\\"scale\\\": \\\"0.5B\\\",\\n      \\\"dosage\\\": 5\\n    },\\n    {\\n      \\\"dirname\\\": \\\"Qwen2.5-0.5B_d025_s123_aligned\\\",\\n      \\\"scale\\\": \\\"0.5B\\\",\\n      \\\"dosage\\\": 25\\n    },\\n    {\\n      \\\"dirname\\\": \\\"Qwen2.5-0.5B_d025_s42_aligned\\\",\\n      \\\"scale\\\": \\\"0.5B\\\",\\n      \\\"dosage\\\": 25\\n    },\\n    {\\n      \\\"dirname\\\": \\\"Qwen2.5-0.5B_d100_s123_aligned\\\",\\n      \\\"scale\\\": \\\"0.5B\\\",\\n      \\\"dosage\\\": 100\\n    },\\n    {\\n      \\\"dirname\\\": \\\"Qwen2.5-0.5B_d100_s42_aligned\\\",\\n      \\\"scale\\\": \\\"0.5B\\\",\\n      \\\"dosage\\\": 100\\n    },\\n    {\\n      \\\"dirname\\\": \\\"Qwen2.5-1.5B_d000_s123_aligned\\\",\\n      \\\"scale\\\": \\\"1.5B\\\",\\n      \\\"dosage\\\": 0\\n    },\\n    {\\n      \\\"dirname\\\": \\\"Qwen2.5-1.5B_d000_s42_aligned\\\",\\n      \\\"scale\\\": \\\"1.5B\\\",\\n      \\\"dosage\\\": 0\\n    },\\n    {\\n      \\\"dirname\\\": \\\"Qwen2.5-1.5B_d005_s123_aligned\\\",\\n      \\\"scale\\\": \\\"1.5B\\\",\\n      \\\"dosage\\\": 5\\n    },\\n    {\\n      \\\"dirname\\\": \\\"Qwen2.5-1.5B_d005_s42_aligned\\\",\\n  
…[truncated 7624 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_cross_family_v5_extraction_20260517T131825",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-17T13:22:21.243698+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat /root/autodl-tmp/exp006/cross_family_v5/exposure_scores_v5.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_cross_family_v5_extraction_20260517T131825",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat /root/autodl-tmp/exp006/cross_family_v5/exposure_scores_v5.json"
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-17T13:22:21.243868+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat /root/autodl-tmp/exp006/cross_family_v5/pooled_rrf_irt_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_cross_family_v5_extraction_20260517T131825",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat /root/autodl-tmp/exp006/cross_family_v5/pooled_rrf_irt_results.json"
  }
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-17T13:22:21.244070+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat /root/autodl-tmp/exp006/cross_family_v5/run_v5.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_cross_family_v5_extraction_20260517T131825",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat /root/autodl-tmp/exp006/cross_family_v5/run_v5.log"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-17T13:22:21.244221+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Command did not complete within 30 seconds!\\n\\nCommand: 'cat /root/autodl-tmp/exp006/cross_family_v5/exposure_scores_v5.json'\\n\\nStdout:\\n\\n        0.17465320085204003,\\n        0.11600957123973259,\\n        0.04448407601505322,\\n        0.07036023496535343,\\n        0.08350681710823278,\\n        0.017524701905203322,\\n        0.040688139438344685,\\n        0.03647558629851235,\\n        0.054647465857182546,\\n        0.1727\\n\\nStderr:\\n\\n\\n\\n\", \"metadata\": {\"elapsed_seconds\": 40.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_cross_family_v5_extraction_20260517T131825",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-17T13:22:21.244616+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"config\\\": {\\n    \\\"model_type\\\": \\\"2pl_gamma\\\",\\n    \\\"scales\\\": [\\n      \\\"0.5B\\\",\\n      \\\"1.5B\\\",\\n      \\\"3B\\\"\\n    ],\\n    \\\"families\\\": [\\n      \\\"Qwen2.5\\\",\\n      \\\"Llama-3.2\\\"\\n    ],\\n    \\\"benchmarks\\\": [\\n      \\\"mmlu\\\",\\n      \\\"gsm8k\\\",\\n      \\\"arc_challenge\\\"\\n    ],\\n    \\\"signals_used\\\": [\\n      \\\"s1_embedding\\\",\\n      \\\"s2_minkpp\\\",\\n      \\\"s4_selfcritique\\\"\\n    ],\\n    \\\"exclusions\\\": {\\n      \\\"D045_scale\\\": \\\"0.5B excluded from mmlu/arc\\\",\\n      \\\"mmlu_model\\\": [\\n        \\\"Llama-3.2-3B_d000 (no aligned data)\\\",\\n        \\\"Llama-3.2-3B_d100 (degenerate all-A)\\\"\\n      ]\\n    },\\n    \\\"stan_config\\\": {\\n      \\\"chains\\\": 4,\\n      \\\"iter_warmup\\\": 1000,\\n      \\\"iter_sampling\\\": 1000,\\n      \\\"adapt_delta\\\": 0.95,\\n      \\\"max_treedepth\\\": 12,\\n      \\\"seed\\\": 42\\n    },\\n    \\\"note\\\": \\\"v5: full s1+s2+s4 RRF after Llama s1_embedding bug fix (12 Llama signals recomputed)\\\"\\n  },\\n  \\\"per_benchmark\\\": {\\n    \\\"mmlu\\\": {\\n      \\\"benchmark\\\": \\\"mmlu\\\",\\n      \\\"model_type\\\": \\\"2pl_gamma\\\",\\n      \\\"exposure_source\\\": \\\"rrf_signal\\\",\\n      \\\"n_models\\\": 18,\\n      \\\"n_items\\\": 300,\\n      \\\"original_n_items\\\": 14042,\\n      \\\"subsampled\\\": true,\\n      \\\"models\\\": [\\n        {\\n          \\\"dirname\\\": \\\"Qwen2.5-1.5B_d000_s123_aligned\\\",\\n          \\\"scale\\\": \\\"1.5B\\\",\\n          \\\"dosage\\\": 0\\n        },\\n        {\\n          \\\"dirname\\\": \\\"Qwen2.5-1.5B_d000_s42_aligned\\\",\\n          \\\"scale\\\": \\\"1.5B\\\",\\n          \\\"dosage\\\": 0\\n        },\\n        {\\n          \\\"dirname\\\": \\\"Qwen2.5-1.5B_d005_s123_aligned\\\",\\n          \\\"scale\\\": \\\"1.5B\\\",\\n          \\\"dosage\\\": 5\\n        },\\n
…[truncated 8126 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_cross_family_v5_extraction_20260517T131825",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-17T13:22:21.244897+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-17 12:15:30,034 [INFO] ============================================================\\n2026-05-17 12:15:30,034 [INFO] STEP 0: Regenerating merged signal files for Llama (stale after s1 fix)\\n2026-05-17 12:15:30,034 [INFO] ============================================================\\n2026-05-17 12:15:30,424 [INFO]   Regenerated Llama-3.2-3B_d000_s42/mmlu: 14042 items\\n2026-05-17 12:15:30,426 [INFO]     s1_embedding std=0.071500 (must be >0 to confirm fix)\\n2026-05-17 12:15:30,463 [INFO]   Regenerated Llama-3.2-3B_d000_s42/gsm8k: 1319 items\\n2026-05-17 12:15:30,464 [INFO]     s1_embedding std=0.062716 (must be >0 to confirm fix)\\n2026-05-17 12:15:30,494 [INFO]   Regenerated Llama-3.2-3B_d000_s42/arc_challenge: 1172 items\\n2026-05-17 12:15:30,494 [INFO]     s1_embedding std=0.071284 (must be >0 to confirm fix)\\n2026-05-17 12:15:30,868 [INFO]   Regenerated Llama-3.2-3B_d005_s42/mmlu: 14042 items\\n2026-05-17 12:15:30,870 [INFO]     s1_embedding std=0.118804 (must be >0 to confirm fix)\\n2026-05-17 12:15:30,907 [INFO]   Regenerated Llama-3.2-3B_d005_s42/gsm8k: 1319 items\\n2026-05-17 12:15:30,908 [INFO]     s1_embedding std=0.074517 (must be >0 to confirm fix)\\n2026-05-17 12:15:30,938 [INFO]   Regenerated Llama-3.2-3B_d005_s42/arc_challenge: 1172 items\\n2026-05-17 12:15:30,938 [INFO]     s1_embedding std=0.084266 (must be >0 to confirm fix)\\n2026-05-17 12:15:31,304 [INFO]   Regenerated Llama-3.2-3B_d025_s42/mmlu: 14042 items\\n2026-05-17 12:15:31,306 [INFO]     s1_embedding std=0.141987 (must be >0 to confirm fix)\\n2026-05-17 12:15:31,349 [INFO]   Regenerated Llama-3.2-3B_d025_s42/gsm8k: 1319 items\\n2026-05-17 12:15:31,349 [INFO]     s1_embedding std=0.098916 (must be >0 to confirm fix)\\n2026-05-17 12:15:31,380 [INFO]   Regenerated Llama-3.2-3B_d025_s42/arc_challenge: 1172 items\\n2026-05-17 12:15:31,380 [INFO]     s1_embedding std=0.107730 (must be >0 to confirm fix)\\n2026-05-17 12:15:31,782 [
…[truncated 6698 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_cross_family_v5_extraction_20260517T131825",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-17T13:22:21.245086+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat /root/autodl-tmp/exp006/cross_family_v5/mmlu/irt_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_cross_family_v5_extraction_20260517T131825",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat /root/autodl-tmp/exp006/cross_family_v5/mmlu/irt_results.json"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-17T13:22:21.245350+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"benchmark\\\": \\\"mmlu\\\",\\n  \\\"model_type\\\": \\\"2pl_gamma\\\",\\n  \\\"exposure_source\\\": \\\"rrf_signal\\\",\\n  \\\"n_models\\\": 18,\\n  \\\"n_items\\\": 300,\\n  \\\"original_n_items\\\": 14042,\\n  \\\"subsampled\\\": true,\\n  \\\"models\\\": [\\n    {\\n      \\\"dirname\\\": \\\"Qwen2.5-1.5B_d000_s123_aligned\\\",\\n      \\\"scale\\\": \\\"1.5B\\\",\\n      \\\"dosage\\\": 0\\n    },\\n    {\\n      \\\"dirname\\\": \\\"Qwen2.5-1.5B_d000_s42_aligned\\\",\\n      \\\"scale\\\": \\\"1.5B\\\",\\n      \\\"dosage\\\": 0\\n    },\\n    {\\n      \\\"dirname\\\": \\\"Qwen2.5-1.5B_d005_s123_aligned\\\",\\n      \\\"scale\\\": \\\"1.5B\\\",\\n      \\\"dosage\\\": 5\\n    },\\n    {\\n      \\\"dirname\\\": \\\"Qwen2.5-1.5B_d005_s42_aligned\\\",\\n      \\\"scale\\\": \\\"1.5B\\\",\\n      \\\"dosage\\\": 5\\n    },\\n    {\\n      \\\"dirname\\\": \\\"Qwen2.5-1.5B_d025_s123_aligned\\\",\\n      \\\"scale\\\": \\\"1.5B\\\",\\n      \\\"dosage\\\": 25\\n    },\\n    {\\n      \\\"dirname\\\": \\\"Qwen2.5-1.5B_d025_s42_aligned\\\",\\n      \\\"scale\\\": \\\"1.5B\\\",\\n      \\\"dosage\\\": 25\\n    },\\n    {\\n      \\\"dirname\\\": \\\"Qwen2.5-1.5B_d100_s123_aligned\\\",\\n      \\\"scale\\\": \\\"1.5B\\\",\\n      \\\"dosage\\\": 100\\n    },\\n    {\\n      \\\"dirname\\\": \\\"Qwen2.5-1.5B_d100_s42_aligned\\\",\\n      \\\"scale\\\": \\\"1.5B\\\",\\n      \\\"dosage\\\": 100\\n    },\\n    {\\n      \\\"dirname\\\": \\\"Llama-3.2-3B_d005_s42_aligned\\\",\\n      \\\"scale\\\": \\\"3B\\\",\\n      \\\"dosage\\\": 5\\n    },\\n    {\\n      \\\"dirname\\\": \\\"Llama-3.2-3B_d025_s42_aligned\\\",\\n      \\\"scale\\\": \\\"3B\\\",\\n      \\\"dosage\\\": 25\\n    },\\n    {\\n      \\\"dirname\\\": \\\"Qwen2.5-3B_d000_s123_aligned\\\",\\n      \\\"scale\\\": \\\"3B\\\",\\n      \\\"dosage\\\": 0\\n    },\\n    {\\n      \\\"dirname\\\": \\\"Qwen2.5-3B_d000_s42_a32_aligned\\\",\\n      \\
…[truncated 4775 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_cross_family_v5_extraction_20260517T131825",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-17T13:22:21.245526+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "find /root/contamcal-irt-calibration/exp006/mmlu_domain_irt_no05b/ -name \"irt_results.json\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_cross_family_v5_extraction_20260517T131825",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "find /root/contamcal-irt-calibration/exp006/mmlu_domain_irt_no05b/ -name \"irt_results.json\" -type f"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-17T13:22:21.245664+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"find: '/root/contamcal-irt-calibration/exp006/mmlu_domain_irt_no05b/': No such file or directory\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 0.62}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_cross_family_v5_extraction_20260517T131825",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-17T13:22:21.245802+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "find /root/contamcal-irt-calibration/exp006/ -name \"irt_results*\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_cross_family_v5_extraction_20260517T131825",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "find /root/contamcal-irt-calibration/exp006/ -name \"irt_results*\" -type f"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-17T13:22:21.245926+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_cross_family_v5_extraction_20260517T131825",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-17T13:22:21.246044+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "find /root/autodl-tmp/exp006/ -maxdepth 2 -name \"irt_results*\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_cross_family_v5_extraction_20260517T131825",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "find /root/autodl-tmp/exp006/ -maxdepth 2 -name \"irt_results*\" -type f"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-17T13:22:21.246171+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.67}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_cross_family_v5_extraction_20260517T131825",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-17T13:22:21.246289+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "find /root/autodl-tmp/exp006/ -maxdepth 3 -name \"irt_results*\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_cross_family_v5_extraction_20260517T131825",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "find /root/autodl-tmp/exp006/ -maxdepth 3 -name \"irt_results*\" -type f"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-17T13:22:21.246736+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/exp006/results_cross_family_irt_v2/gsm8k/irt_results.json\\n/root/autodl-tmp/exp006/results_cross_family_irt_v2/arc_challenge/irt_results.json\\n/root/autodl-tmp/exp006/results_cross_family_irt_v3/gsm8k/irt_results.json\\n/root/autodl-tmp/exp006/results_cross_family_irt_v3/arc_challenge/irt_results.json\\n/root/autodl-tmp/exp006/results_cross_family_irt_v3/mmlu/irt_results.json\\n/root/autodl-tmp/exp006/results_cross_family_irt_v3_mmlu_fix/mmlu/irt_results.json\\n/root/autodl-tmp/exp006/cross_family_v5/mmlu/irt_results.json\\n/root/autodl-tmp/exp006/cross_family_v5/gsm8k/irt_results.json\\n/root/autodl-tmp/exp006/cross_family_v5/arc_challenge/irt_results.json\\n/root/autodl-tmp/exp006/mmlu_domain_irt_j16_cross_family/STEM_Math/irt_results.json\\n/root/autodl-tmp/exp006/mmlu_domain_irt_j16_cross_family/STEM_Science/irt_results.json\\n/root/autodl-tmp/exp006/mmlu_domain_irt_j16_cross_family/STEM_CS_Eng/irt_results.json\\n/root/autodl-tmp/exp006/mmlu_domain_irt_j16_cross_family/Medical/irt_results.json\\n/root/autodl-tmp/exp006/mmlu_domain_irt_j16_cross_family/Humanities/irt_results.json\\n/root/autodl-tmp/exp006/mmlu_domain_irt_j16_cross_family/Social_Sciences/irt_results.json\\n/root/autodl-tmp/exp006/results_pooled_4bench_aligned_2pl/mmlu/irt_results.json\\n/root/autodl-tmp/exp006/results_pooled_4bench_aligned_2pl/gsm8k/irt_results.json\\n/root/autodl-tmp/exp006/results_pooled_4bench_aligned_2pl/arc_challenge/irt_results.json\\n/root/autodl-tmp/exp006/results_pooled_4bench_aligned_2pl/humaneval/irt_results.json\\n/root/autodl-tmp/exp006/results_mmlu_domain_gamma/STEM_Math/irt_results.json\\n/root/autodl-tmp/exp006/results_mmlu_domain_gamma/STEM_Science/irt_results.json\\n/root/autodl-tmp/exp006/results_mmlu_domain_gamma/STEM_CS_Eng/irt_results.json\\n/root/autodl-tmp/exp006/results_mmlu_domain_gamma/Medical/irt_results.json\\n/root/autodl-tmp/exp006/results_mmlu_domain_gamma/Humanities/irt_resu
…[truncated 4474 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_cross_family_v5_extraction_20260517T131825",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-17T13:22:21.246910+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "cat /root/autodl-tmp/exp006/mmlu_domain_irt_no05B/pooled/irt_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_cross_family_v5_extraction_20260517T131825",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "cat /root/autodl-tmp/exp006/mmlu_domain_irt_no05B/pooled/irt_results.json"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-17T13:22:21.247064+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"domain\\\": \\\"pooled\\\",\\n  \\\"n_items\\\": 2000,\\n  \\\"n_models\\\": 13,\\n  \\\"mean_acc\\\": 0.5981153846153846,\\n  \\\"gamma\\\": {\\n    \\\"mean\\\": 0.10717879240881249,\\n    \\\"median\\\": 0.103996845,\\n    \\\"sd\\\": 0.26271857111420777,\\n    \\\"q025\\\": -0.4007699935,\\n    \\\"q975\\\": 0.625413265\\n  },\\n  \\\"diagnostics\\\": {\\n    \\\"max_rhat\\\": 1.0068,\\n    \\\"rhat_ok\\\": true,\\n    \\\"min_ess\\\": 1157.2,\\n    \\\"ess_ok\\\": true,\\n    \\\"divergent_count\\\": 0,\\n    \\\"divergent_pct\\\": 0.0,\\n    \\\"divergent_ok\\\": true,\\n    \\\"total_draws\\\": 4000,\\n    \\\"all_ok\\\": true\\n  },\\n  \\\"ppp\\\": {\\n    \\\"overall_ppp\\\": 0.208,\\n    \\\"obs_mean_acc\\\": 0.5981,\\n    \\\"pred_mean_acc\\\": 0.5962,\\n    \\\"residual_mae\\\": 0.0106\\n  },\\n  \\\"fit_time_sec\\\": 524.3\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.38}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_cross_family_v5_extraction_20260517T131825",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-17T13:22:21.247205+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "cqa1-21977",
  "command": "head -30 /root/autodl-tmp/exp006/results_pooled_irt_qwen_n24/mmlu/irt_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_ops_cross_family_v5_extraction_20260517T131825",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "cqa1-21977",
    "command": "head -30 /root/autodl-tmp/exp006/results_pooled_irt_qwen_n24/mmlu/irt_results.json"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-17T13:22:21.247404+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"benchmark\\\": \\\"mmlu\\\",\\n  \\\"model_type\\\": \\\"2pl_gamma\\\",\\n  \\\"exposure_source\\\": \\\"rrf_signal\\\",\\n  \\\"n_models\\\": 16,\\n  \\\"n_items\\\": 300,\\n  \\\"original_n_items\\\": 14042,\\n  \\\"subsampled\\\": true,\\n  \\\"models\\\": [\\n    {\\n      \\\"dirname\\\": \\\"Qwen2.5-1.5B_d000_s123_aligned\\\",\\n      \\\"scale\\\": \\\"1.5B\\\",\\n      \\\"dosage\\\": 0\\n    },\\n    {\\n      \\\"dirname\\\": \\\"Qwen2.5-1.5B_d000_s42_aligned\\\",\\n      \\\"scale\\\": \\\"1.5B\\\",\\n      \\\"dosage\\\": 0\\n    },\\n    {\\n      \\\"dirname\\\": \\\"Qwen2.5-1.5B_d005_s123_aligned\\\",\\n      \\\"scale\\\": \\\"1.5B\\\",\\n      \\\"dosage\\\": 5\\n    },\\n    {\\n      \\\"dirname\\\": \\\"Qwen2.5-1.5B_d005_s42_aligned\\\",\\n      \\\"scale\\\": \\\"1.5B\\\",\\n      \\\"dosage\\\": 5\\n    },\\n    {\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.39}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_ops_cross_family_v5_extraction_20260517T131825",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-17T13:22:21.247696+00:00_

All data collected. Now let me write the structured summary. I'll also include MMLU since it's in the results.

## Cross-Family v5 IRT 结果

### 模型组成

| Benchmark | J | 包含 0.5B | 包含 Llama d100 | 排除 |
|-----------|---|-----------|-----------------|------|
| MMLU | 18 | 否 | 否 | 0.5B (D045); Llama d000 (no aligned data); Llama d100 (degenerate all-A) |
| GSM8K | 28 | 是 | 是 | 无 |
| ARC | 20 | 否 | 是 | 0.5B (D045) |

**信号**: s1_embedding + s2_minkpp + s4_selfcritique RRF (s1_embedding bug 已修复)
**MCMC**: 4 chains x 2000 iter (1000 warmup + 1000 sampling), adapt_delta=0.95, max_treedepth=12

---

### 三个 Benchmark 总览

| 指标 | MMLU | GSM8K | ARC-Challenge |
|------|------|-------|---------------|
| γ mean | 0.3465 | -0.1306 | 0.0074 |
| γ 95% CI | [-0.627, 1.320] | [-0.521, 0.273] | [-0.575, 0.565] |
| γ 显著 | 否 | 否 | 否 |
| PPP | 0.624 | 0.842 | 0.435 |
| max Rhat | 1.006 | 1.008 | 1.007 |
| min ESS | 1430.9 | 1284.3 | 1395.6 |
| divergences | 0 | 0 | 0 |
| n_items | 300 (of 14042) | 300 (of 1319) | 300 (of 1172) |
| n_models | 18 | 28 | 20 |
| raw_MAE | 0.038 | 0.179 | 0.070 |
| cal_MAE | 0.008 | 0.008 | 0.015 |
| ΔMAE | 0.030 | 0.171 | 0.055 |

所有 benchmark 的 MCMC 诊断完美 (Rhat<1.01, ESS>1000, 0 divergences)。γ 三个 benchmark 均不显著。

---

### ARC-Challenge 校准分数 by Model

| Model | Family | Scale | Dosage | cal_mean | 95% CI | raw_acc |
|-------|--------|-------|--------|----------|--------|---------|
| Qwen 1.5B d000 s123 | Qwen | 1.5B | 0 | 0.769 | [0.737, 0.799] | 0.760 |
| Qwen 1.5B d000 s42 | Qwen | 1.5B | 0 | 0.769 | [0.737, 0.800] | 0.767 |
| Qwen 1.5B d005 s123 | Qwen | 1.5B | 5 | 0.758 | [0.725, 0.790] | 0.747 |
| Qwen 1.5B d005 s42 | Qwen | 1.5B | 5 | 0.767 | [0.735, 0.798] | 0.767 |
| Qwen 1.5B d025 s123 | Qwen | 1.5B | 25 | 0.760 | [0.728, 0.790] | 0.753 |
| Qwen 1.5B d025 s42 | Qwen | 1.5B | 25 | 0.773 | [0.740, 0.804] | 0.773 |
| Qwen 1.5B d100 s123 | Qwen | 1.5B | 100 | 0.774 | [0.741, 0.806] | 0.780 |
| Qwen 1.5B d100 s42 | Qwen | 1.5B | 100 | 0.771 | [0.739, 0.803] | 0.773 |
| **Llama 3B d000 s42** | **Llama** | **3B** | **0** | **0.554** | **[0.513, 0.595]** | **0.587** |
| **Llama 3B d005 s42** | **Llama** | **3B** | **5** | **0.542** | **[0.499, 0.584]** | **0.577** |
| **Llama 3B d025 s42** | **Llama** | **3B** | **25** | **0.542** | **[0.499, 0.583]** | **0.583** |
| **Llama 3B d100 s42** | **Llama** | **3B** | **100** | **0.545** | **[0.504, 0.589]** | **0.590** |
| Qwen 3B d000 s123 | Qwen | 3B | 0 | 0.843 | [0.815, 0.869] | 0.837 |
| Qwen 3B d000 s42 | Qwen | 3B | 0 | 0.846 | [0.819, 0.871] | 0.830 |
| Qwen 3B d005 s123 | Qwen | 3B | 5 | 0.848 | [0.821, 0.872] | 0.837 |
| Qwen 3B d005 s42 | Qwen | 3B | 5 | 0.844 | [0.817, 0.869] | 0.827 |
| Qwen 3B d025 s123 | Qwen | 3B | 25 | 0.852 | [0.826, 0.877] | 0.847 |
| Qwen 3B d025 s42 | Qwen | 3B | 25 | 0.842 | [0.814, 0.868] | 0.820 |
| Qwen 3B d100 s123 | Qwen | 3B | 100 | 0.850 | [0.822, 0.875] | 0.833 |
| Qwen 3B d100 s42 | Qwen | 3B | 100 | 0.846 | [0.819, 0.871] | 0.830 |

**ARC 关键发现**: 三个 family/scale 组的校准分数几乎不随 dosage 变化。Llama 3B 从 d000=0.554 到 d100=0.545 (Δ=-0.009)，Qwen 3B 从 d000=0.845 到 d100=0.848 (Δ=+0.003)，Qwen 1.5B 从 d000=0.769 到 d100=0.773 (Δ=+0.004)。γ≈0 完全一致。

---

### GSM8K 校准分数 by Model

| Model | Family | Scale | Dosage | cal_mean | 95% CI | raw_acc |
|-------|--------|-------|--------|----------|--------|---------|
| Qwen 0.5B d000 s123 | Qwen | 0.5B | 0 | 0.303 | [0.262, 0.346] | 0.300 |
| Qwen 0.5B d000 s42 | Qwen | 0.5B | 0 | 0.337 | [0.294, 0.381] | 0.330 |
| Qwen 0.5B d005 s123 | Qwen | 0.5B | 5 | 0.352 | [0.309, 0.397] | 0.353 |
| Qwen 0.5B d005 s42 | Qwen | 0.5B | 5 | 0.353 | [0.311, 0.397] | 0.340 |
| Qwen 0.5B d025 s123 | Qwen | 0.5B | 25 | 0.355 | [0.310, 0.399] | 0.357 |
| Qwen 0.5B d025 s42 | Qwen | 0.5B | 25 | 0.346 | [0.303, 0.389] | 0.330 |
| Qwen 0.5B d100 s123 | Qwen | 0.5B | 100 | 0.362 | [0.320, 0.406] | 0.363 |
| Qwen 0.5B d100 s42 | Qwen | 0.5B | 100 | 0.360 | [0.316, 0.406] | 0.350 |
| Qwen 1.5B d000 s123 | Qwen | 1.5B | 0 | 0.654 | [0.611, 0.695] | 0.633 |
| Qwen 1.5B d000 s42 | Qwen | 1.5B | 0 | 0.642 | [0.599, 0.684] | 0.627 |
| Qwen 1.5B d005 s123 | Qwen | 1.5B | 5 | 0.660 | [0.616, 0.702] | 0.660 |
| Qwen 1.5B d005 s42 | Qwen | 1.5B | 5 | 0.660 | [0.619, 0.703] | 0.647 |
| Qwen 1.5B d025 s123 | Qwen | 1.5B | 25 | 0.666 | [0.623, 0.708] | 0.657 |
| Qwen 1.5B d025 s42 | Qwen | 1.5B | 25 | 0.657 | [0.613, 0.699] | 0.653 |
| Qwen 1.5B d100 s123 | Qwen | 1.5B | 100 | 0.666 | [0.622, 0.709] | 0.663 |
| Qwen 1.5B d100 s42 | Qwen | 1.5B | 100 | 0.628 | [0.585, 0.671] | 0.623 |
| **Llama 3B d000 s42** | **Llama** | **3B** | **0** | **0.207** | **[0.171, 0.246]** | **0.187** |
| **Llama 3B d005 s42** | **Llama** | **3B** | **5** | **0.248** | **[0.208, 0.289]** | **0.253** |
| **Llama 3B d025 s42** | **Llama** | **3B** | **25** | **0.252** | **[0.214, 0.293]** | **0.253** |
| **Llama 3B d100 s42** | **Llama** | **3B** | **100** | **0.258** | **[0.218, 0.300]** | **0.263** |
| Qwen 3B d000 s123 | Qwen | 3B | 0 | 0.171 | [0.135, 0.208] | 0.163 |
| Qwen 3B d000 s42 | Qwen | 3B | 0 | 0.131 | [0.100, 0.165] | 0.110 |
| Qwen 3B d005 s123 | Qwen | 3B | 5 | 0.654 | [0.609, 0.696] | 0.647 |
| Qwen 3B d005 s42 | Qwen | 3B | 5 | 0.426 | [0.381, 0.472] | 0.417 |
| Qwen 3B d025 s123 | Qwen | 3B | 25 | 0.546 | [0.500, 0.593] | 0.530 |
| Qwen 3B d025 s42 | Qwen | 3B | 25 | 0.683 | [0.639, 0.724] | 0.680 |
| Qwen 3B d100 s123 | Qwen | 3B | 100 | 0.732 | [0.690, 0.772] | 0.737 |
| Qwen 3B d100 s42 | Qwen | 3B | 100 | 0.716 | [0.675, 0.757] | 0.713 |

**GSM8K 关键发现**: Qwen 3B 在 GSM8K 上 dosage 效应巨大 (d000 ~0.15 → d100 ~0.72, Δ≈+0.57)。而 Llama 3B 几乎不变 (d000=0.207 → d100=0.258, Δ=+0.051)。但 γ 仍不显著 (-0.131)，说明 IRT 将这种 dosage 效应归因于 ability (θ) 提升而非 exposure 偏倚。

---

### MMLU 校准分数 by Model

| Model | Family | Scale | Dosage | cal_mean | 95% CI | raw_acc |
|-------|--------|-------|--------|----------|--------|---------|
| Qwen 1.5B d000 s123 | Qwen | 1.5B | 0 | 0.588 | [0.552, 0.624] | 0.580 |
| Qwen 1.5B d000 s42 | Qwen | 1.5B | 0 | 0.604 | [0.569, 0.638] | 0.600 |
| Qwen 1.5B d005 s123 | Qwen | 1.5B | 5 | 0.597 | [0.562, 0.632] | 0.593 |
| Qwen 1.5B d005 s42 | Qwen | 1.5B | 5 | 0.600 | [0.565, 0.634] | 0.600 |
| Qwen 1.5B d025 s123 | Qwen | 1.5B | 25 | 0.598 | [0.562, 0.635] | 0.593 |
| Qwen 1.5B d025 s42 | Qwen | 1.5B | 25 | 0.599 | [0.563, 0.633] | 0.597 |
| Qwen 1.5B d100 s123 | Qwen | 1.5B | 100 | 0.589 | [0.553, 0.624] | 0.580 |
| Qwen 1.5B d100 s42 | Qwen | 1.5B | 100 | 0.589 | [0.553, 0.624] | 0.580 |
| **Llama 3B d005 s42** | **Llama** | **3B** | **5** | **0.415** | **[0.374, 0.456]** | **0.443** |
| **Llama 3B d025 s42** | **Llama** | **3B** | **25** | **0.372** | **[0.331, 0.414]** | **0.403** |
| Qwen 3B d000 s123 | Qwen | 3B | 0 | 0.625 | [0.589, 0.661] | 0.617 |
| Qwen 3B d000 s42 | Qwen | 3B | 0 | 0.627 | [0.594, 0.661] | 0.623 |
| Qwen 3B d005 s123 | Qwen | 3B | 5 | 0.633 | [0.598, 0.669] | 0.627 |
| Qwen 3B d005 s42 | Qwen | 3B | 5 | 0.630 | [0.596, 0.664] | 0.627 |
| Qwen 3B d025 s123 | Qwen | 3B | 25 | 0.622 | [0.585, 0.656] | 0.617 |
| Qwen 3B d025 s42 | Qwen | 3B | 25 | 0.613 | [0.580, 0.647] | 0.603 |
| Qwen 3B d100 s123 | Qwen | 3B | 100 | 0.631 | [0.597, 0.665] | 0.623 |
| Qwen 3B d100 s42 | Qwen | 3B | 100 | 0.634 | [0.599, 0.668] | 0.630 |

**MMLU 注意**: Llama 仅有 d005 和 d025 两个模型（d000 无 aligned data, d100 degenerate all-A 被排除）。

---

### 跨家族校准分数一致性分析 (ARC)

| Dosage | Llama 3B | Qwen 3B (mean) | Δ | 一致? |
|--------|----------|-----------------|-----|-------|
| d000 | 0.554 | 0.845 | -0.291 | 否（baseline ability 差距大） |
| d005 | 0.542 | 0.846 | -0.304 | 否（同上） |
| d025 | 0.542 | 0.847 | -0.305 | 否（同上） |
| d100 | 0.545 | 0.848 | -0.303 | 否（同上） |

ARC 上 Llama 和 Qwen 3B 的 baseline ability 差距非常大（~0.30），但**两个 family 内部 dosage 变化量都接近 0**，Δ_dosage 差异 < 0.01。这与 γ≈0 一致：无论哪个 family，contamination dosage 都不影响 ARC 表现。

### 跨家族校准分数一致性分析 (GSM8K)

| Dosage | Llama 3B | Qwen 3B (mean) | Δ |
|--------|----------|-----------------|-----|
| d000 | 0.207 | 0.151 | +0.056 |
| d005 | 0.248 | 0.540 | -0.292 |
| d025 | 0.252 | 0.615 | -0.363 |
| d100 | 0.258 | 0.724 | -0.466 |

GSM8K 上 Qwen 3B 随 dosage 剧烈变化（Δ_d000→d100 ≈ +0.57），而 Llama 3B 几乎不变（Δ ≈ +0.05）。两个 family 对 GSM8K contamination 的敏感度截然不同。但 IRT 通过 θ 吸收了这种差异，γ 仍不显著。

---

### vs Qwen-only (J=13) 对比

| 维度 | Qwen-only (J=13, MMLU pooled) | Cross-family v5 (J=18, MMLU) |
|------|-------------------------------|------------------------------|
| γ mean | +0.107 | +0.347 |
| γ 95% CI | [-0.401, 0.625] | [-0.627, 1.320] |
| γ 显著 | 否 | 否 |
| PPP | 0.208 | 0.624 |
| cal_MAE | 0.011 | 0.008 |
| n_items | 2000 | 300 (of 14042) |

- γ 方向一致（MMLU 均为正），cross-family 版本更大但 CI 也更宽
- 两者均不显著
- PPP: cross-family (0.624) 远优于 Qwen-only (0.208)，模型拟合更好
- Qwen-only 用了 2000 items 未做 subsampling，cross-family 仅 300 items

---

### v4 → v5 变化 (s1_embedding bug fix 效果)

| Bench | v4 γ | v5 γ | Δγ | 结论 |
|-------|------|------|----|------|
| MMLU | 0.415 | 0.347 | -0.068 | γ 略降，仍不显著 |
| GSM8K | -0.110 | -0.131 | -0.021 | 几乎无变化 |
| ARC | 0.002 | 0.007 | +0.006 | 几乎无变化 |

s1_embedding bug fix 对结果影响很小，结论不变。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_ops_cross_family_v5_extraction_20260517T131825"
}
```

</details>

---
