# analysis qwen14b kl30 s42 gsm8k v2

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 31
- **Recorded user turns:** 0
- **Tool calls:** 15
- **Original source:** `logs/chats/worker_analysis_qwen14b_kl30_s42_gsm8k_v2_20260519T225148.jsonl`
- **Structured JSON:** [`d12b97ad7c09e938ad56.json`](../../sessions/d1/d12b97ad7c09e938ad56.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

31 recorded events

### Tool call

_source line 1 · 2026-05-19T22:53:37.786465+00:00_

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
  "session": "worker_analysis_qwen14b_kl30_s42_gsm8k_v2_20260519T225148",
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

_source line 2 · 2026-05-19T22:53:37.786790+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qwen14b_kl30_s42_gsm8k_v2_20260519T225148",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-19T22:53:37.786956+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-41718",
  "command": "tail -100 ~/runs/distill_sparse_swiglu/qwen14b_kl30_s42_gsm8k_v2.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qwen14b_kl30_s42_gsm8k_v2_20260519T225148",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-41718",
    "command": "tail -100 ~/runs/distill_sparse_swiglu/qwen14b_kl30_s42_gsm8k_v2.log",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-19T22:53:37.787133+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'qwen14b_kl30_s42_gsm8k_v2'}",
  "project": "distill_sparse_swiglu",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qwen14b_kl30_s42_gsm8k_v2_20260519T225148",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'qwen14b_kl30_s42_gsm8k_v2'}",
    "project": "distill_sparse_swiglu",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-19T22:53:37.787340+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\\rRunning generate_until requests:  43%|████▎     | 569/1319 [2:06:11<3:04:20, 14.75s/it][transformers] Both `max_new_tokens` (=2048) and `max_length`(=1828) seem to have been set. `max_new_tokens` will take precedence. Please refer to the documentation for more information. (https://huggingface.co/docs/transformers/main/en/main_classes/text_generation)\\n\\rRunning generate_until requests:  44%|████▎     | 577/1319 [2:08:31<3:12:34, 15.57s/it][transformers] Both `max_new_tokens` (=2048) and `max_length`(=1824) seem to have been set. `max_new_tokens` will take precedence. Please refer to the documentation for more information. (https://huggingface.co/docs/transformers/main/en/main_classes/text_generation)\\n\\rRunning generate_until requests:  44%|████▍     | 585/1319 [2:10:51<3:17:30, 16.14s/it][transformers] Both `max_new_tokens` (=2048) and `max_length`(=1821) seem to have been set. `max_new_tokens` will take precedence. Please refer to the documentation for more information. (https://huggingface.co/docs/transformers/main/en/main_classes/text_generation)\\n\\rRunning generate_until requests:  45%|████▍     | 593/1319 [2:13:11<3:20:09, 16.54s/it][transformers] Both `max_new_tokens` (=2048) and `max_length`(=1815) seem to have been set. `max_new_tokens` will take precedence. Please refer to the documentation for more information. (https://huggingface.co/docs/transformers/main/en/main_classes/text_generation)\\n\\rRunning generate_until requests:  46%|████▌     | 601/1319 [2:13:24<2:24:20, 12.06s/it][transformers] Both `max_new_tokens` (=2048) and `max_length`(=1813) seem to have been set. `max_new_tokens` will take precedence. Please refer to the documentation for more information. (https://huggingface.co/docs/transformers/main/en/main_classes/text_generation)\\n\\rRunning generate_until requests:  46%|████▌     | 609/1319 [2:13:33<1:43:48,  8.77s/it][transformers] Both `max_new_tokens` (=2048) and `max_lengt
…[truncated 6308 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qwen14b_kl30_s42_gsm8k_v2_20260519T225148",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-19T22:53:37.787502+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": \"bench_dense\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.6839}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qwen14b_kl30_s42_gsm8k_v2_20260519T225148",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-19T22:53:37.787665+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-41718",
  "command": "cat /root/distill_sparse_swiglu/results/benchmark/qwen14b_kl30_s42_gsm8k_v2/results.json",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qwen14b_kl30_s42_gsm8k_v2_20260519T225148",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-41718",
    "command": "cat /root/distill_sparse_swiglu/results/benchmark/qwen14b_kl30_s42_gsm8k_v2/results.json",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-19T22:53:37.787843+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"exp_id\\\": \\\"qwen14b_kl30_s42_gsm8k_v2\\\",\\n  \\\"config\\\": {\\n    \\\"model_name_or_path\\\": \\\"/root/autodl-tmp/models/qwen2.5-14b/\\\",\\n    \\\"checkpoint\\\": \\\"checkpoints/qwen14b_kl30_s42/predictor_kl_normalized.pt\\\",\\n    \\\"tasks\\\": \\\"gsm8k\\\",\\n    \\\"sparsity_mode\\\": \\\"teal_global\\\",\\n    \\\"baseline_mode\\\": null,\\n    \\\"dense\\\": false,\\n    \\\"exp_id\\\": \\\"qwen14b_kl30_s42_gsm8k_v2\\\",\\n    \\\"sparsity_target\\\": 0.3,\\n    \\\"allocation\\\": \\\"uniform\\\",\\n    \\\"gpu\\\": 0,\\n    \\\"multi_gpu\\\": false,\\n    \\\"seq_len\\\": 2048,\\n    \\\"calibration_samples\\\": 32,\\n    \\\"batch_size\\\": 8,\\n    \\\"bottleneck_size\\\": 128,\\n    \\\"svd_rank\\\": 256,\\n    \\\"max_eval_samples\\\": null\\n  },\\n  \\\"mode\\\": {\\n    \\\"mode\\\": \\\"teal_global\\\",\\n    \\\"checkpoint\\\": \\\"/root/distill_sparse_swiglu/checkpoints/qwen14b_kl30_s42/predictor_kl_normalized.pt\\\",\\n    \\\"sparsity_target\\\": 0.3,\\n    \\\"allocation\\\": \\\"uniform\\\"\\n  },\\n  \\\"metrics\\\": {\\n    \\\"lm_eval\\\": {\\n      \\\"gsm8k\\\": {\\n        \\\"sample_len\\\": 1319,\\n        \\\"exact_match\\\": 0.3571,\\n        \\\"exact_match_stderr\\\": 0.013197931775445208\\n      }\\n    },\\n    \\\"lm_eval_raw\\\": {\\n      \\\"gsm8k\\\": {\\n        \\\"name\\\": \\\"gsm8k\\\",\\n        \\\"alias\\\": \\\"gsm8k\\\",\\n        \\\"sample_len\\\": 1319,\\n        \\\"exact_match,strict-match\\\": 0.35405610310841545,\\n        \\\"exact_match_stderr,strict-match\\\": 0.013172728385222562,\\n        \\\"exact_match,flexible-extract\\\": 0.3570887035633055,\\n        \\\"exact_match_stderr,flexible-extract\\\": 0.013197931775445208\\n      }\\n    }\\n  },\\n  \\\"timestamp\\\": \\\"2026-05-20 02:18:38\\\"\\n}\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qwen14b_kl30_s42_gsm8k_v2_20260519T225148",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-19T22:53:37.787986+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-41718",
  "command": "head -50 ~/runs/distill_sparse_swiglu/qwen14b_kl30_s42_gsm8k_v2.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qwen14b_kl30_s42_gsm8k_v2_20260519T225148",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-41718",
    "command": "head -50 ~/runs/distill_sparse_swiglu/qwen14b_kl30_s42_gsm8k_v2.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-19T22:53:37.788190+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Loading model: /root/autodl-tmp/models/qwen2.5-14b/\\n[transformers] `torch_dtype` is deprecated! Use `dtype` instead!\\n\\rLoading weights:   0%|          | 0/579 [00:00<?, ?it/s]\\rLoading weights:   0%|          | 1/579 [00:00<03:26,  2.80it/s]\\rLoading weights:   0%|          | 2/579 [00:00<03:36,  2.66it/s]\\rLoading weights:   1%|          | 5/579 [00:00<01:16,  7.51it/s]\\rLoading weights:   3%|▎         | 17/579 [00:00<00:18, 29.78it/s]\\rLoading weights:   4%|▍         | 23/579 [00:01<00:17, 31.30it/s]\\rLoading weights:   7%|▋         | 41/579 [00:01<00:09, 57.36it/s]\\rLoading weights:   9%|▉         | 52/579 [00:01<00:08, 58.88it/s]\\rLoading weights:  11%|█▏        | 66/579 [00:01<00:08, 60.78it/s]\\rLoading weights:  14%|█▎        | 79/579 [00:01<00:07, 66.20it/s]\\rLoading weights:  16%|█▋        | 95/579 [00:02<00:07, 60.52it/s]\\rLoading weights:  21%|██        | 122/579 [00:02<00:05, 89.48it/s]\\rLoading weights:  24%|██▎       | 137/579 [00:02<00:04, 98.62it/s]\\rLoading weights:  26%|██▌       | 149/579 [00:02<00:06, 71.16it/s]\\rLoading weights:  29%|██▉       | 169/579 [00:03<00:05, 71.25it/s]\\rLoading weights:  33%|███▎      | 191/579 [00:03<00:04, 78.69it/s]\\rLoading weights:  37%|███▋      | 215/579 [00:03<00:04, 90.60it/s]\\rLoading weights:  39%|███▉      | 225/579 [00:03<00:05, 64.28it/s]\\rLoading weights:  40%|████      | 233/579 [00:04<00:06, 50.45it/s]\\rLoading weights:  50%|█████     | 290/579 [00:04<00:02, 117.45it/s]\\rLoading weights:  54%|█████▎    | 311/579 [00:04<00:02, 105.97it/s]\\rLoading weights:  57%|█████▋    | 328/579 [00:04<00:02, 83.70it/s] \\rLoading weights:  60%|██████    | 349/579 [00:04<00:02, 95.36it/s]\\rLoading weights:  63%|██████▎   | 365/579 [00:05<00:02, 104.37it/s]\\rLoading weights:  65%|██████▌   | 379/579 [00:05<00:02, 96.08it/s] \\rLoading weights:  68%|██████▊   | 392/579 [00:05<00:02, 91.98it/s]\\rLoading weights:  70%|██████▉   | 403/579 [0
…[truncated 1775 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qwen14b_kl30_s42_gsm8k_v2_20260519T225148",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-19T22:53:37.788361+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-41718",
  "command": "grep -E \"actual_sparsity|Average sparsity|Overall sparsity|Layer 47\" ~/runs/distill_sparse_swiglu/qwen14b_kl30_s42_gsm8k_v2.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qwen14b_kl30_s42_gsm8k_v2_20260519T225148",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-41718",
    "command": "grep -E \"actual_sparsity|Average sparsity|Overall sparsity|Layer 47\" ~/runs/distill_sparse_swiglu/qwen14b_kl30_s42_gsm8k_v2.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-19T22:53:37.788492+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qwen14b_kl30_s42_gsm8k_v2_20260519T225148",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-19T22:53:37.788613+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-41718",
  "command": "grep -E \"actual_sparsity|Average sparsity|Overall sparsity|Layer 4[2-9]\" ~/runs/distill_sparse_swiglu/qwen14b_kl30_s42_gsm8k_v2.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qwen14b_kl30_s42_gsm8k_v2_20260519T225148",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-41718",
    "command": "grep -E \"actual_sparsity|Average sparsity|Overall sparsity|Layer 4[2-9]\" ~/runs/distill_sparse_swiglu/qwen14b_kl30_s42_gsm8k_v2.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-19T22:53:37.788734+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qwen14b_kl30_s42_gsm8k_v2_20260519T225148",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-19T22:53:37.788849+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-41718",
  "command": "grep -E \"actual_sparsity|Average sparsity|Overall sparsity\" ~/runs/distill_sparse_swiglu/qwen14b_kl30_s42_gsm8k_v2.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qwen14b_kl30_s42_gsm8k_v2_20260519T225148",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-41718",
    "command": "grep -E \"actual_sparsity|Average sparsity|Overall sparsity\" ~/runs/distill_sparse_swiglu/qwen14b_kl30_s42_gsm8k_v2.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-19T22:53:37.788998+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qwen14b_kl30_s42_gsm8k_v2_20260519T225148",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-19T22:53:37.789147+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-41718",
  "command": "grep \"sparsity\" ~/runs/distill_sparse_swiglu/qwen14b_kl30_s42_gsm8k_v2.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qwen14b_kl30_s42_gsm8k_v2_20260519T225148",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-41718",
    "command": "grep \"sparsity\" ~/runs/distill_sparse_swiglu/qwen14b_kl30_s42_gsm8k_v2.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-19T22:53:37.789267+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Per-layer sparsity (TEAL-predictor):\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qwen14b_kl30_s42_gsm8k_v2_20260519T225148",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-19T22:53:37.789423+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'qwen14b_kl30_s42_gsm8k'}",
  "project": "distill_sparse_swiglu",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qwen14b_kl30_s42_gsm8k_v2_20260519T225148",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'qwen14b_kl30_s42_gsm8k'}",
    "project": "distill_sparse_swiglu",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-19T22:53:37.789583+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'qwen14b_kl30_s42'}",
  "project": "distill_sparse_swiglu",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qwen14b_kl30_s42_gsm8k_v2_20260519T225148",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'qwen14b_kl30_s42'}",
    "project": "distill_sparse_swiglu",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-19T22:53:37.789751+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": \"bench_dense\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.7047}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qwen14b_kl30_s42_gsm8k_v2_20260519T225148",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-19T22:53:37.789874+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": \"bench_dense\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.617}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qwen14b_kl30_s42_gsm8k_v2_20260519T225148",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-19T22:53:37.790001+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "distill_sparse_swiglu",
  "limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qwen14b_kl30_s42_gsm8k_v2_20260519T225148",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "distill_sparse_swiglu",
    "limit": "20"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-19T22:53:37.790310+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"qwen14b_kl30_s42_gsm8k_v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T17:52:58.669Z\", \"updated_at\": \"2026-05-19T22:51:00.000Z\", \"conclusion\": \"success\", \"metrics\": {\"gsm8k_exact_match\": 0.3571, \"actual_sparsity\": 0.296}, \"hypothesis\": \"KL s42 GSM8K supplement for Qwen-14B (retry). Enables KL vs TEAL comparison on reasoning task. v1 killed due to GPU contention on 41718:1.\", \"parent\": \"qwen14b_kl30_s42_eval_uniform_v3\"}, \"bench_teal30_uniform_6task\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-19T22:37:10.303Z\", \"updated_at\": \"2026-05-19T22:37:10.303Z\"}, \"bench_teal30_uniform_gsm8k\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T21:59:56.432Z\", \"updated_at\": \"2026-05-19T22:34:00.000Z\", \"hypothesis\": \"8B TEAL 30% uniform allocation GSM8K eval. 补齐 uniform 分配下的 TEAL baseline，与 KL 30% uniform (bench_kl30_uniform) 和 Dense (bench_dense) 做 GSM8K 三方对比。bench_teal30 用的是 global allocation，本实验用 uniform 保持分配策略一致。\", \"parent\": \"bench_teal30\", \"conclusion\": \"success\", \"metrics\": {\"gsm8k_exact_match\": 0.0879, \"actual_sparsity\": 0.3}}, \"bench_kl30_uniform_gsm8k_d075\": {\"status\": \"PREPARING\", \"created_at\": \"2026-05-19T21:02:45.729Z\", \"updated_at\": \"2026-05-19T21:02:45.729Z\"}, \"qwen14b_kl30_s123_gsm8k\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T18:22:30.203Z\", \"updated_at\": \"2026-05-19T20:56:54.196Z\", \"hypothesis\": \"KL s123 GSM8K supplement for Qwen-14B. Completes 3-seed GSM8K comparison (s42 running, s456 queued). Required for complete 14B paper table.\", \"parent\": \"qwen14b_kl30_s123_eval_v5\", \"conclusion\": \"success\", \"metrics\": {\"gsm8k_exact_match\": 0.3442, \"gsm8k_exact_match_strict\": 0.3434, \"actual_sparsity\": 0.297}}, \"qwen14b_kl30_s456_eval_v3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T15:37:22.929Z\", \"updated_at\": \"2026-05-19T20:40:09.524Z\", \"hypothesis\": \"Qwen-14B KL s
…[truncated 7951 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qwen14b_kl30_s42_gsm8k_v2_20260519T225148",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-19T22:53:37.790512+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "filters": "{'exp_id': 'qwen14b_kl30_s42_gsm8k_v2'}",
  "project": "distill_sparse_swiglu",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qwen14b_kl30_s42_gsm8k_v2_20260519T225148",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "filters": "{'exp_id': 'qwen14b_kl30_s42_gsm8k_v2'}",
    "project": "distill_sparse_swiglu",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-19T22:53:37.790651+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": \"bench_dense\"}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.6498}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qwen14b_kl30_s42_gsm8k_v2_20260519T225148",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-19T22:53:37.790820+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "qwen14b_kl30_s42_gsm8k_v2",
  "field": "metrics",
  "value": "{'gsm8k_exact_match': 0.3571, 'gsm8k_exact_match_strict': 0.3541, 'gsm8k_exact_match_stderr': 0.0132, 'actual_sparsity': 0.296, 'sample_len': 1319}",
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qwen14b_kl30_s42_gsm8k_v2_20260519T225148",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "qwen14b_kl30_s42_gsm8k_v2",
    "field": "metrics",
    "value": "{'gsm8k_exact_match': 0.3571, 'gsm8k_exact_match_strict': 0.3541, 'gsm8k_exact_match_stderr': 0.0132, 'actual_sparsity': 0.296, 'sample_len': 1319}",
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-19T22:53:37.790959+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "qwen14b_kl30_s42_gsm8k_v2",
  "field": "log_path",
  "value": "~/runs/distill_sparse_swiglu/qwen14b_kl30_s42_gsm8k_v2.log",
  "project": "distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_qwen14b_kl30_s42_gsm8k_v2_20260519T225148",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "qwen14b_kl30_s42_gsm8k_v2",
    "field": "log_path",
    "value": "~/runs/distill_sparse_swiglu/qwen14b_kl30_s42_gsm8k_v2.log",
    "project": "distill_sparse_swiglu"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-19T22:53:37.791152+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"qwen14b_kl30_s42_gsm8k_v2\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T17:52:58.669Z\", \"updated_at\": \"2026-05-19T22:53:22.423Z\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T22:49:58.678Z\", \"metrics\": {\"gsm8k_exact_match\": 0.3571, \"gsm8k_exact_match_strict\": 0.3541, \"gsm8k_exact_match_stderr\": 0.0132, \"actual_sparsity\": 0.296, \"sample_len\": 1319}, \"checkpoint_path\": \"results/benchmark/qwen14b_kl30_s42_gsm8k_v2/results.json\", \"hypothesis\": \"KL s42 GSM8K supplement for Qwen-14B (retry). Enables KL vs TEAL comparison on reasoning task. v1 killed due to GPU contention on 41718:1.\", \"parent\": \"qwen14b_kl30_s42_eval_uniform_v3\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache python -u src/benchmark_eval.py --exp_id qwen14b_kl30_s42_gsm8k_v2 --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --checkpoint checkpoints/qwen14b_kl30_s42/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.3 --allocation uniform --tasks gsm8k --seq_len 2048 --gpu 0\\\"\", \"server\": \"westd-41718\", \"gpu\": [\"cuda:0\"], \"pid\": \"166099\", \"log_path\": \"~/runs/distill_sparse_swiglu/qwen14b_kl30_s42_gsm8k_v2.log\", \"submitted_at\": \"2026-05-19T18:18:18.206Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"server\": \"westd-41718\", \"gpu\": \"cuda:0\", \"pid\": \"166099\", \"log_path\": \"~/runs/distill_sparse_swiglu/qwen14b_kl30_s42_gsm8k_v2.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl
…[truncated 567 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qwen14b_kl30_s42_gsm8k_v2_20260519T225148",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-19T22:53:37.791347+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"qwen14b_kl30_s42_gsm8k_v2\", \"experiment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T17:52:58.669Z\", \"updated_at\": \"2026-05-19T22:53:23.576Z\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-19T22:49:58.678Z\", \"metrics\": {\"gsm8k_exact_match\": 0.3571, \"gsm8k_exact_match_strict\": 0.3541, \"gsm8k_exact_match_stderr\": 0.0132, \"actual_sparsity\": 0.296, \"sample_len\": 1319}, \"checkpoint_path\": \"results/benchmark/qwen14b_kl30_s42_gsm8k_v2/results.json\", \"hypothesis\": \"KL s42 GSM8K supplement for Qwen-14B (retry). Enables KL vs TEAL comparison on reasoning task. v1 killed due to GPU contention on 41718:1.\", \"parent\": \"qwen14b_kl30_s42_eval_uniform_v3\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache python -u src/benchmark_eval.py --exp_id qwen14b_kl30_s42_gsm8k_v2 --model_name_or_path /root/autodl-tmp/models/qwen2.5-14b/ --checkpoint checkpoints/qwen14b_kl30_s42/predictor_kl_normalized.pt --sparsity_mode teal_global --sparsity_target 0.3 --allocation uniform --tasks gsm8k --seq_len 2048 --gpu 0\\\"\", \"server\": \"westd-41718\", \"gpu\": [\"cuda:0\"], \"pid\": \"166099\", \"log_path\": \"~/runs/distill_sparse_swiglu/qwen14b_kl30_s42_gsm8k_v2.log\", \"submitted_at\": \"2026-05-19T18:18:18.206Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"server\": \"westd-41718\", \"gpu\": \"cuda:0\", \"pid\": \"166099\", \"log_path\": \"~/runs/distill_sparse_swiglu/qwen14b_kl30_s42_gsm8k_v2.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/distill_sparse_swiglu && HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1 TRANSFORMERS_OFFLINE=1 HF_HOME=/root/autodl
…[truncated 568 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_qwen14b_kl30_s42_gsm8k_v2_20260519T225148",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-19T22:53:37.791543+00:00_

注册表已更新完毕。

## 实验结果：qwen14b_kl30_s42_gsm8k_v2

### Metrics
| 指标 | 值 |
|------|-----|
| gsm8k_exact_match (flexible) | **0.3571** |
| gsm8k_exact_match (strict) | 0.3541 |
| stderr | ±0.0132 |
| actual_sparsity | 0.296 |
| sample_len | 1319 |
| 运行时间 | ~4.5h, EXIT_CODE=0, 无 OOM/NaN |

### 与 s123 一致性
| Seed | GSM8K exact_match | Sparsity |
|------|-------------------|----------|
| s42 | 0.3571 | 0.296 |
| s123 | 0.3442 | 0.297 |
| **差值** | **+1.29pp** | — |

差值在 stderr (~1.3pp) 范围内，**两个 seed 一致**。

### 与 baseline 对比
| 配置 | GSM8K | vs Dense retention |
|------|-------|-------------------|
| Qwen-14B Dense | 0.8757 | 100% |
| **KL 30% s42** | **0.3571** | **40.8%** |
| KL 30% s123 | 0.3442 | 39.3% |
| TEAL 27.5% uniform | 0.5709 | 65.2% |
| 8B Dense | 0.4875 | — |
| 8B TEAL 30% uniform | 0.0879 | — |

### 结论：**success**

实验正常完成，结果与 s123 一致。但 GSM8K 上 KL 30% 的 retention 较低（~40%），且显著弱于 TEAL 27.5%（0.5709）。这与其他 5 个任务上 KL 优于或持平 TEAL 的趋势相反——GSM8K 是 KL predictor 的弱势任务。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_qwen14b_kl30_s42_gsm8k_v2_20260519T225148"
}
```

</details>

---
