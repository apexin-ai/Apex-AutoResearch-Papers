# status 21461 progress

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 23
- **Recorded user turns:** 0
- **Tool calls:** 11
- **Original source:** `logs/chats/worker_status_21461_progress_20260520T010644.jsonl`
- **Structured JSON:** [`dc5e26036ddb7f89356f.json`](../../sessions/dc/dc5e26036ddb7f89356f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

23 recorded events

### Tool call

_source line 1 · 2026-05-20T01:08:33.760107+00:00_

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
  "session": "worker_status_21461_progress_20260520T010644",
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

_source line 2 · 2026-05-20T01:08:33.760737+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_status_21461_progress_20260520T010644",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-20T01:08:33.761221+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-21461",
  "command": "nvidia-smi --query-gpu=index,utilization.gpu,memory.used,memory.total --format=csv,noheader"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_status_21461_progress_20260520T010644",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-21461",
    "command": "nvidia-smi --query-gpu=index,utilization.gpu,memory.used,memory.total --format=csv,noheader"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-20T01:08:33.763967+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-21461",
  "command": "ls -la /root/autodl-tmp/schema_outputs/d066_*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_status_21461_progress_20260520T010644",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-21461",
    "command": "ls -la /root/autodl-tmp/schema_outputs/d066_*"
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-20T01:08:33.764272+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-21461",
  "command": "ls -la /root/autodl-tmp/schema_outputs/d067_*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_status_21461_progress_20260520T010644",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-21461",
    "command": "ls -la /root/autodl-tmp/schema_outputs/d067_*"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-20T01:08:33.764485+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"0, 77 %, 18999 MiB, 97887 MiB\\n1, 80 %, 19011 MiB, 97887 MiB\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.36}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_status_21461_progress_20260520T010644",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 3
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-20T01:08:33.764688+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-21461",
  "command": "ps aux --sort=-start_time"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_status_21461_progress_20260520T010644",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-21461",
    "command": "ps aux --sort=-start_time"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-20T01:08:33.764913+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root 103465 May 20 09:01 /root/autodl-tmp/schema_outputs/d066_beam_sweep_scierc_gpu1.log\\n\\n/root/autodl-tmp/schema_outputs/d066_beam_sweep:\\ntotal 4056\\ndrwxr-xr-x 3 root root    4096 May 20 08:41 .\\ndrwxr-xr-x 3 root root    4096 May 20 07:45 ..\\n-rw-r--r-- 1 root root      41 May 19 23:18 d066_summary.json\\n-rw-r--r-- 1 root root 1024154 May 20 08:13 qwen_scierc_beam1_full_s1.jsonl\\n-rw-r--r-- 1 root root 1027328 May 20 07:46 qwen_scierc_beam1_unconstrained.jsonl\\n-rw-r--r-- 1 root root  843347 May 20 09:07 qwen_scierc_beam2_full_s1.jsonl\\n-rw-r--r-- 1 root root 1035059 May 20 08:40 qwen_scierc_beam2_unconstrained.jsonl\\ndrwxr-xr-x 2 root root      10 May 19 23:18 violations\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_status_21461_progress_20260520T010644",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-20T01:08:33.765160+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root 113502 May 20 09:06 /root/autodl-tmp/schema_outputs/d067_seed_variance.log\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_status_21461_progress_20260520T010644",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-20T01:08:33.765458+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"USER        PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND\\nroot     143490  0.0  0.0   7064  1628 ?        Rs   09:07   0:00 ps aux --sort=-start_time\\nsshd     143485  1.0  0.0  15444  5568 ?        S    09:07   0:00 sshd: unknown [net]\\nroot     143484  1.0  0.0  16432 10100 ?        Ss   09:07   0:00 sshd: unknown [priv]\\nsshd     143483  1.0  0.0  15444  5540 ?        S    09:07   0:00 sshd: unknown [net]\\nroot     143482  0.0  0.0  16432  9984 ?        Ss   09:07   0:00 sshd: unknown [priv]\\nsshd     143469  0.0  0.0  15444  5748 ?        S    09:07   0:00 sshd: unknown [net]\\nroot     143468  0.0  0.0  16432 10000 ?        Ss   09:07   0:00 sshd: unknown [priv]\\nroot     143466  2.5  0.0  16692 10680 ?        Ss   09:07   0:00 sshd: root@notty\\nroot     139345  100  0.2 44903504 2145388 ?    Rl   08:40  26:13 python run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/checkpoints/qwen3_8b_lora_scierc_merged --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path /root/autodl-tmp/schema_outputs/d066_beam_sweep/qwen_scierc_beam2_full_s1.jsonl --device cuda:0 --max_new_tokens 2048 --seed 42 --decoding_strategy beam --num_beams 2 --skip_on_error\\nroot     139020  100  0.1 44584884 1906404 ?    Rl   08:39  27:32 python3 run_constrained_extraction.py --mode full_s1 --dataset scierc --model_path /root/autodl-tmp/checkpoints/qwen3_8b_lora_scierc_merged --data_path data/processed_data/test.json --constraints_path ontology_constraints.json --output_path outputs/d067_seed_variance/qwen_scierc_seed456_full_s1.jsonl --device cuda:0 --batch_size 1 --seed 456 --max_new_tokens 2048 --decoding_strategy greedy --temperature 0.0\\nroot     135226  0.0  0.0   4364  3192 ?        S    08:15   0:00 bash scripts/d067_seed_variance.sh 0 qwen_scierc 456\\nroot     132654  0.0  0.0   4364  3128 ?        S    07:24   0:00 b
…[truncated 3715 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_status_21461_progress_20260520T010644",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T01:08:33.765972+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-21461",
  "command": "ls -la /root/schema_semantic_constrained_ie/outputs/d067_seed_variance/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_status_21461_progress_20260520T010644",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-21461",
    "command": "ls -la /root/schema_semantic_constrained_ie/outputs/d067_seed_variance/"
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-20T01:08:33.766228+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-21461",
  "command": "wc -l /root/autodl-tmp/schema_outputs/d066_beam_sweep/*.jsonl"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_status_21461_progress_20260520T010644",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-21461",
    "command": "wc -l /root/autodl-tmp/schema_outputs/d066_beam_sweep/*.jsonl"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-20T01:08:33.766485+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 4048\\ndrwxr-xr-x 2 root root    4096 May 20 09:07 .\\ndrwxr-xr-x 4 root root    4096 May 20 07:24 ..\\n-rw-r--r-- 1 root root 1025263 May 20 08:15 qwen_scierc_seed123_full_s1.jsonl\\n-rw-r--r-- 1 root root    2647 May 20 08:15 qwen_scierc_seed123_full_s1_violations.json\\n-rw-r--r-- 1 root root 1028457 May 20 07:47 qwen_scierc_seed123_unconstrained.jsonl\\n-rw-r--r-- 1 root root    3539 May 20 07:47 qwen_scierc_seed123_unconstrained_violations.json\\n-rw-r--r-- 1 root root 1025264 May 20 09:07 qwen_scierc_seed456_full_s1.jsonl\\n-rw-r--r-- 1 root root    2647 May 20 09:07 qwen_scierc_seed456_full_s1_violations.json\\n-rw-r--r-- 1 root root 1028444 May 20 08:39 qwen_scierc_seed456_unconstrained.jsonl\\n-rw-r--r-- 1 root root    3539 May 20 08:39 qwen_scierc_seed456_unconstrained_violations.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_status_21461_progress_20260520T010644",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-20T01:08:33.766750+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"    551 /root/autodl-tmp/schema_outputs/d066_beam_sweep/qwen_scierc_beam1_full_s1.jsonl\\n    551 /root/autodl-tmp/schema_outputs/d066_beam_sweep/qwen_scierc_beam1_unconstrained.jsonl\\n    465 /root/autodl-tmp/schema_outputs/d066_beam_sweep/qwen_scierc_beam2_full_s1.jsonl\\n    551 /root/autodl-tmp/schema_outputs/d066_beam_sweep/qwen_scierc_beam2_unconstrained.jsonl\\n   2118 total\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.52}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_status_21461_progress_20260520T010644",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-20T01:08:33.766968+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-21461",
  "command": "tail -5 /root/autodl-tmp/schema_outputs/d066_beam_sweep_scierc_gpu1.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_status_21461_progress_20260520T010644",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-21461",
    "command": "tail -5 /root/autodl-tmp/schema_outputs/d066_beam_sweep_scierc_gpu1.log"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-20T01:08:33.767155+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"[351/551] C90-3063_sent2: OK E=4 R=4 6.8s\\n[352/551] C90-3063_sent3: OK E=2 R=1 1.8s\\n[353/551] C90-3063_sent4: OK E=2 R=0 1.2s\\n[354/551] C90-3063_sent5: OK E=3 R=2 3.2s\\n[355/551] J05-4003_sent0: OK E=3 R=2 3.1s\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_status_21461_progress_20260520T010644",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-20T01:08:33.767330+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-21461",
  "command": "tail -5 /root/autodl-tmp/schema_outputs/d067_seed_variance.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_status_21461_progress_20260520T010644",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-21461",
    "command": "tail -5 /root/autodl-tmp/schema_outputs/d067_seed_variance.log"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-20T01:08:33.767526+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Samples: 551\\nEntity types: ['Task', 'Method', 'Material', 'Metric', 'OtherScientificTerm', 'Generic']\\nRelation types: 7\\nLoading model...\\n\\rLoading weights:   0%|          | 0/291 [00:00<?, ?it/s]\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.49}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_status_21461_progress_20260520T010644",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-20T01:08:33.769888+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-21461",
  "command": "wc -l /root/schema_semantic_constrained_ie/outputs/d067_seed_variance/*.jsonl"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_status_21461_progress_20260520T010644",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-21461",
    "command": "wc -l /root/schema_semantic_constrained_ie/outputs/d067_seed_variance/*.jsonl"
  }
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-20T01:08:33.770259+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-21461",
  "command": "tail -15 /root/autodl-tmp/schema_outputs/d067_seed_variance.log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_status_21461_progress_20260520T010644",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-21461",
    "command": "tail -15 /root/autodl-tmp/schema_outputs/d067_seed_variance.log"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-20T01:08:33.770533+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"      5 /root/schema_semantic_constrained_ie/outputs/d067_seed_variance/llama_scierc_seed123_unconstrained.jsonl\\n    551 /root/schema_semantic_constrained_ie/outputs/d067_seed_variance/qwen_scierc_seed123_full_s1.jsonl\\n    551 /root/schema_semantic_constrained_ie/outputs/d067_seed_variance/qwen_scierc_seed123_unconstrained.jsonl\\n    551 /root/schema_semantic_constrained_ie/outputs/d067_seed_variance/qwen_scierc_seed456_full_s1.jsonl\\n    551 /root/schema_semantic_constrained_ie/outputs/d067_seed_variance/qwen_scierc_seed456_unconstrained.jsonl\\n   2209 total\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_status_21461_progress_20260520T010644",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-20T01:08:33.770911+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"Model: /root/autodl-tmp/checkpoints/llama_lora_scierc_merged\\nDevice: cuda:0\\nSamples: 551\\nEntity types: ['Task', 'Method', 'Material', 'Metric', 'OtherScientificTerm', 'Generic']\\nRelation types: 7\\nLoading model...\\n\\rLoading weights:   0%|          | 0/291 [00:00<?, ?it/s]\\rLoading weights:   0%|          | 1/291 [00:00<04:45,  1.01it/s]\\rLoading weights:   1%|          | 2/291 [00:02<04:53,  1.02s/it]\\rLoading weights:   1%|▏         | 4/291 [00:02<02:08,  2.23it/s]\\rLoading weights:   2%|▏         | 6/291 [00:02<01:14,  3.82it/s]\\rLoading weights:   4%|▍         | 13/291 [00:02<00:27, 10.19it/s]\\rLoading weights:   5%|▌         | 15/291 [00:02<00:28,  9.56it/s]\\rLoading weights:   7%|▋         | 21/291 [00:02<00:16, 16.09it/s]\\rLoading weights:   8%|▊         | 24/291 [00:03<00:20, 12.87it/s]\\rLoading weights:  10%|▉         | 29/291 [00:03<00:14, 17.94it/s]\\rLoading weights:  11%|█▏        | 33/291 [00:03<00:16, 15.48it/s]\\rLoading weights:  14%|█▎        | 40/291 [00:03<00:12, 20.45it/s]\\rLoading weights:  15%|█▍        | 43/291 [00:04<00:13, 17.76it/s]\\rLoading weights:  17%|█▋        | 49/291 [00:04<00:11, 21.04it/s]\\rLoading weights:  18%|█▊        | 52/291 [00:04<00:13, 17.70it/s]\\rLoading weights:  20%|█▉        | 58/291 [00:04<00:10, 21.65it/s]\\rLoading weights:  21%|██        | 61/291 [00:05<00:12, 18.55it/s]\\rLoading weights:  22%|██▏       | 65/291 [00:05<00:10, 21.63it/s]\\rLoading weights:  23%|██▎       | 68/291 [00:05<00:11, 18.82it/s]\\rLoading weights:  24%|██▍       | 71/291 [00:05<00:11, 19.50it/s]\\rLoading weights:  26%|██▌       | 76/291 [00:05<00:09, 21.59it/s]\\rLoading weights:  27%|██▋       | 79/291 [00:05<00:12, 17.47it/s]\\rLoading weights:  29%|██▉       | 85/291 [00:06<00:09, 21.98it/s]\\rLoading weights:  30%|███       | 88/291 [00:06<00:10, 19.24it/s]\\rLoading weights:  32%|███▏      | 94/291 [00:06<00:08, 23.25it/s]\\rLoading weights:  33%|███▎   
…[truncated 4575 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_status_21461_progress_20260520T010644",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 23 · 2026-05-20T01:08:33.771296+00:00_

## 实验进度汇报

### d066 beam sweep (GPU 1)
**3/8 configs 完成，当前跑 beam2_full_s1 (465/551 samples)**

| Config | 状态 | 行数 |
|--------|------|------|
| beam1_unconstrained | ✅ | 551/551 |
| beam1_full_s1 | ✅ | 551/551 |
| beam2_unconstrained | ✅ | 551/551 |
| beam2_full_s1 | 🔄 运行中 | 465/551 (84%) |
| beam4_unconstrained | ⏳ | - |
| beam4_full_s1 | ⏳ | - |
| beam8_unconstrained | ⏳ | - |
| beam8_full_s1 | ⏳ | - |

当前 config 约 5 分钟内完成。beam4/beam8 每 sample 推理时间会随 beam width 增长，剩余 4 configs 预计 **3-5 小时**。

### d067 seed variance (GPU 0)
**4/12 configs 完成，当前跑 llama_scierc_seed123_unconstrained (5/551 samples)**

| Config | 状态 | 行数 |
|--------|------|------|
| qwen_scierc seed123 unc | ✅ | 551/551 |
| qwen_scierc seed123 con | ✅ | 551/551 |
| qwen_scierc seed456 unc | ✅ | 551/551 |
| qwen_scierc seed456 con | ✅ | 551/551 |
| llama_scierc seed123 unc | 🔄 刚启动 | 5/551 |
| llama_scierc seed123 con | ⏳ | - |
| llama_scierc seed456 unc | ⏳ | - |
| llama_scierc seed456 con | ⏳ | - |
| qwen_docred seed123 unc | ⏳ | - |
| qwen_docred seed123 con | ⏳ | - |
| qwen_docred seed456 unc | ⏳ | - |
| qwen_docred seed456 con | ⏳ | - |

刚加载完 llama 模型开始推理。每 config ~30 min，剩余 8 configs 预计 **~4 小时**。

### GPU 利用率
| GPU | 利用率 | 显存 |
|-----|--------|------|
| GPU 0 (d067) | 77% | 19.0 / 95.6 GB |
| GPU 1 (d066) | 80% | 19.0 / 95.6 GB |

两块 GPU 都在正常工作，显存占用约 20%。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_status_21461_progress_20260520T010644"
}
```

</details>

---
