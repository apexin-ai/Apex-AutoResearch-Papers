# code llama rsft s42 withevi 2048 launch

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 43
- **Recorded user turns:** 0
- **Tool calls:** 21
- **Original source:** `logs/chats/worker_code_llama-rsft-s42-withevi-2048-launch_20260521T024516.jsonl`
- **Structured JSON:** [`73cc9059ab10920eb8fc.json`](../../sessions/73/73cc9059ab10920eb8fc.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

43 recorded events

### Tool call

_source line 1 · 2026-05-21T02:48:25.710762+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__detect_image",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_llama-rsft-s42-withevi-2048-launch_20260521T024516",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__detect_image",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-21T02:48:25.711267+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_llama-rsft-s42-withevi-2048-launch_20260521T024516",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-21T02:48:25.711819+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "nvidia-smi --query-gpu=index,memory.used,memory.total --format=csv,noheader",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_llama-rsft-s42-withevi-2048-launch_20260521T024516",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "nvidia-smi --query-gpu=index,memory.used,memory.total --format=csv,noheader",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-21T02:48:25.712095+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"0, 0 MiB, 97887 MiB\\n1, 0 MiB, 97887 MiB\\n2, 18879 MiB, 97887 MiB\\n3, 18879 MiB, 97887 MiB\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.17}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_llama-rsft-s42-withevi-2048-launch_20260521T024516",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-21T02:48:25.712301+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "ls -d /root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B /root/autodl-tmp/sft_output_llama* /root/autodl-tmp/rsft_output_llama* /root/autodl-tmp/llama_rsft* 2>/dev/null",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_llama-rsft-s42-withevi-2048-launch_20260521T024516",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "ls -d /root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B /root/autodl-tmp/sft_output_llama* /root/autodl-tmp/rsft_output_llama* /root/autodl-tmp/llama_rsft* 2>/dev/null",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-21T02:48:25.712492+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_llama-rsft-s42-withevi-2048-launch_20260521T024516",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-21T02:48:25.712676+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "faith-evidence-ie",
  "filters": "{'exp_id': 'eval_llama_rsft_s42_with_evidence_1024'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_llama-rsft-s42-withevi-2048-launch_20260521T024516",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "faith-evidence-ie",
    "filters": "{'exp_id': 'eval_llama_rsft_s42_with_evidence_1024'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-21T02:48:25.712850+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "faith-evidence-ie",
  "filters": "{'exp_id': 'llama_rsft_s42'}",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_llama-rsft-s42-withevi-2048-launch_20260521T024516",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "faith-evidence-ie",
    "filters": "{'exp_id': 'llama_rsft_s42'}",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-21T02:48:25.713013+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.1002}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_llama-rsft-s42-withevi-2048-launch_20260521T024516",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-21T02:48:25.713151+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.9791}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_llama-rsft-s42-withevi-2048-launch_20260521T024516",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-21T02:48:25.713325+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "ls -d /root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_llama-rsft-s42-withevi-2048-launch_20260521T024516",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "ls -d /root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-21T02:48:25.713486+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_llama-rsft-s42-withevi-2048-launch_20260521T024516",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-21T02:48:25.713620+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "find /root/autodl-tmp -maxdepth 1 -type d -name \"*sft*llama*\" -o -name \"*llama*sft*\" -o -name \"*rsft*llama*\" -o -name \"*llama*rsft*\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_llama-rsft-s42-withevi-2048-launch_20260521T024516",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "find /root/autodl-tmp -maxdepth 1 -type d -name \"*sft*llama*\" -o -name \"*llama*sft*\" -o -name \"*rsft*llama*\" -o -name \"*llama*rsft*\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-21T02:48:25.713769+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/autodl-tmp/rsft_candidates_llama_3_1_8b\\n/root/autodl-tmp/rsft_output_llama_3_1_8b_k1\\n/root/autodl-tmp/rsft_output_llama_3_1_8b_k1_s43\\n/root/autodl-tmp/rsft_output_llama_3_1_8b_k1_s44\\n/root/autodl-tmp/rsft_scored_llama_3_1_8b\\n/root/autodl-tmp/rsft_scored_llama_3_1_8b_k1\\n/root/autodl-tmp/sft_output_llama_3_1_8b\\n/root/autodl-tmp/sft_output_llama_3_1_8b_no_evidence\\n/root/autodl-tmp/sft_output_llama_3_1_8b_s43\\n/root/autodl-tmp/sft_output_llama_3_1_8b_s44\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_llama-rsft-s42-withevi-2048-launch_20260521T024516",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-21T02:48:25.713903+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "faith-evidence-ie",
  "filters": "{'status': 'DONE'}",
  "fields": "['exp_id', 'spec', 'metrics', 'status']",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_llama-rsft-s42-withevi-2048-launch_20260521T024516",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "faith-evidence-ie",
    "filters": "{'status': 'DONE'}",
    "fields": "['exp_id', 'spec', 'metrics', 'status']",
    "limit": "30"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-21T02:48:25.714519+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"plan017_14b_rsft_eval\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_14b --base_model /root/autodl-tmp/models/Qwen/Qwen3-14B --sft_adapter /root/autodl-tmp/sft_output_14b/checkpoint-144 --data_path /root/autodl-tmp/data/docred --split dev --output_dir /root/autodl-tmp/freige/eval_outputs/plan017_14b_rsft_eval --batch_size 1 --max_new_tokens 1024 --no-quantize --seed 42\", \"server\": \"rtx5090-4x\", \"data_path\": \"/root/autodl-tmp/data/docred/dev.json\", \"data_count\": 985, \"model_name\": \"Qwen3-14B + SFT(checkpoint-144) + RSFT\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/rsft_output_14b\", \"eval_data\": \"DocRED dev set (985 docs, 12275 gold triples)\", \"pid\": 53413, \"gpu\": \"cuda:0\", \"gpu_mem_used\": \"32503 MiB\", \"sft_adapter\": \"/root/autodl-tmp/sft_output_14b/checkpoint-144\", \"base_model\": \"/root/autodl-tmp/models/Qwen/Qwen3-14B\", \"nested_lora\": true, \"checkpoint_path\": \"/root/autodl-tmp/freige/eval_outputs/plan017_14b_rsft_eval/\", \"log_path\": \"/root/autodl-tmp/freige/eval_outputs/plan017_14b_rsft_eval.log\"}, \"metrics\": {\"ign_f1\": 0.5886, \"f1\": 0.5886, \"format_ok\": 985, \"format_ok_rate\": 1, \"truncated\": 0, \"evi_f1\": 0.8392, \"edcr\": 0.5396}}, \"eval_llama_sft_s43_no_evidence_2048_r2\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/freige && GPU=1 python -m freige.eval.inference --model_path /root/autodl-tmp/sft_output_llama_3_1_8b_s43 --base_model /root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 2048 --seed 42 --no-quantize --no_evidence --output_dir /root/autodl-tmp/eval_results/eval_llama_sft_s43_no_evidence_2048\\\"\", \"server\": \"rtx5090-4x\",
…[truncated 29961 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_llama-rsft-s42-withevi-2048-launch_20260521T024516",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-21T02:48:25.714876+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "ls /root/autodl-tmp/sft_output_llama_3_1_8b/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_llama-rsft-s42-withevi-2048-launch_20260521T024516",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "ls /root/autodl-tmp/sft_output_llama_3_1_8b/",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-21T02:48:25.715051+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "ls /root/autodl-tmp/rsft_output_llama_3_1_8b_k1/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_llama-rsft-s42-withevi-2048-launch_20260521T024516",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "ls /root/autodl-tmp/rsft_output_llama_3_1_8b_k1/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-21T02:48:25.715190+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"README.md\\nadapter_config.json\\nadapter_model.safetensors\\nchat_template.jinja\\ncheckpoint-190\\ncheckpoint-570\\nspecial_tokens_map.json\\ntokenizer.json\\ntokenizer_config.json\\ntraining_args.bin\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_llama-rsft-s42-withevi-2048-launch_20260521T024516",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-21T02:48:25.715347+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"README.md\\nadapter_config.json\\nadapter_model.safetensors\\nchat_template.jinja\\ncheckpoint-1100\\ncheckpoint-1107\\nspecial_tokens_map.json\\ntokenizer.json\\ntokenizer_config.json\\ntraining_args.bin\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.53}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_llama-rsft-s42-withevi-2048-launch_20260521T024516",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-21T02:48:25.715475+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "faith-evidence-ie",
  "filters": "{'status': 'DONE'}",
  "fields": "['exp_id', 'spec', 'metrics']",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_llama-rsft-s42-withevi-2048-launch_20260521T024516",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "faith-evidence-ie",
    "filters": "{'status': 'DONE'}",
    "fields": "['exp_id', 'spec', 'metrics']",
    "limit": "30"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-21T02:48:25.716057+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"plan017_14b_rsft_eval\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_14b --base_model /root/autodl-tmp/models/Qwen/Qwen3-14B --sft_adapter /root/autodl-tmp/sft_output_14b/checkpoint-144 --data_path /root/autodl-tmp/data/docred --split dev --output_dir /root/autodl-tmp/freige/eval_outputs/plan017_14b_rsft_eval --batch_size 1 --max_new_tokens 1024 --no-quantize --seed 42\", \"server\": \"rtx5090-4x\", \"data_path\": \"/root/autodl-tmp/data/docred/dev.json\", \"data_count\": 985, \"model_name\": \"Qwen3-14B + SFT(checkpoint-144) + RSFT\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/rsft_output_14b\", \"eval_data\": \"DocRED dev set (985 docs, 12275 gold triples)\", \"pid\": 53413, \"gpu\": \"cuda:0\", \"gpu_mem_used\": \"32503 MiB\", \"sft_adapter\": \"/root/autodl-tmp/sft_output_14b/checkpoint-144\", \"base_model\": \"/root/autodl-tmp/models/Qwen/Qwen3-14B\", \"nested_lora\": true, \"checkpoint_path\": \"/root/autodl-tmp/freige/eval_outputs/plan017_14b_rsft_eval/\", \"log_path\": \"/root/autodl-tmp/freige/eval_outputs/plan017_14b_rsft_eval.log\"}, \"metrics\": {\"ign_f1\": 0.5886, \"f1\": 0.5886, \"format_ok\": 985, \"format_ok_rate\": 1, \"truncated\": 0, \"evi_f1\": 0.8392, \"edcr\": 0.5396}}, \"eval_llama_sft_s43_no_evidence_2048_r2\": {\"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/freige && GPU=1 python -m freige.eval.inference --model_path /root/autodl-tmp/sft_output_llama_3_1_8b_s43 --base_model /root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 2048 --seed 42 --no-quantize --no_evidence --output_dir /root/autodl-tmp/eval_results/eval_llama_sft_s43_no_evidence_2048\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:1\"], \"pid\": \"58417\", 
…[truncated 29301 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_llama-rsft-s42-withevi-2048-launch_20260521T024516",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-21T02:48:25.716374+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "faith-evidence-ie",
  "filters": "{'status': 'DONE'}",
  "fields": "['exp_id', 'spec', 'metrics']",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_llama-rsft-s42-withevi-2048-launch_20260521T024516",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "faith-evidence-ie",
    "filters": "{'status': 'DONE'}",
    "fields": "['exp_id', 'spec', 'metrics']",
    "limit": "30"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-21T02:48:25.717009+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {\"plan017_14b_rsft_eval\": {\"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_14b --base_model /root/autodl-tmp/models/Qwen/Qwen3-14B --sft_adapter /root/autodl-tmp/sft_output_14b/checkpoint-144 --data_path /root/autodl-tmp/data/docred --split dev --output_dir /root/autodl-tmp/freige/eval_outputs/plan017_14b_rsft_eval --batch_size 1 --max_new_tokens 1024 --no-quantize --seed 42\", \"server\": \"rtx5090-4x\", \"data_path\": \"/root/autodl-tmp/data/docred/dev.json\", \"data_count\": 985, \"model_name\": \"Qwen3-14B + SFT(checkpoint-144) + RSFT\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/rsft_output_14b\", \"eval_data\": \"DocRED dev set (985 docs, 12275 gold triples)\", \"pid\": 53413, \"gpu\": \"cuda:0\", \"gpu_mem_used\": \"32503 MiB\", \"sft_adapter\": \"/root/autodl-tmp/sft_output_14b/checkpoint-144\", \"base_model\": \"/root/autodl-tmp/models/Qwen/Qwen3-14B\", \"nested_lora\": true, \"checkpoint_path\": \"/root/autodl-tmp/freige/eval_outputs/plan017_14b_rsft_eval/\", \"log_path\": \"/root/autodl-tmp/freige/eval_outputs/plan017_14b_rsft_eval.log\"}, \"metrics\": {\"ign_f1\": 0.5886, \"f1\": 0.5886, \"format_ok\": 985, \"format_ok_rate\": 1, \"truncated\": 0, \"evi_f1\": 0.8392, \"edcr\": 0.5396}}, \"eval_llama_sft_s43_no_evidence_2048_r2\": {\"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/freige && GPU=1 python -m freige.eval.inference --model_path /root/autodl-tmp/sft_output_llama_3_1_8b_s43 --base_model /root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B --data_path /root/autodl-tmp/data/docred --split dev --batch_size 4 --max_new_tokens 2048 --seed 42 --no-quantize --no_evidence --output_dir /root/autodl-tmp/eval_results/eval_llama_sft_s43_no_evidence_2048\\\"\", \"server\": \"rtx5090-4x\", \"gpu\": [\"cuda:1\"], \"pid\": \"58417\", 
…[truncated 29301 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_llama-rsft-s42-withevi-2048-launch_20260521T024516",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-21T02:48:25.717262+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__register_artifact",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_llama-rsft-s42-withevi-2048-launch_20260521T024516",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__update_registry,mcp__agent-ml-research__register_artifact",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-21T02:48:25.717414+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_llama-rsft-s42-withevi-2048-launch_20260521T024516",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-21T02:48:25.717579+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/freige && CUDA_VISIBLE_DEVICES=0 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 nohup python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_llama_3_1_8b_k1 --base_model /root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B --sft_adapter /root/autodl-tmp/sft_output_llama_3_1_8b --data_path /root/autodl-tmp/data/docred --split dev --output_dir /root/autodl-tmp/eval_results/eval_llama_rsft_s42_with_evidence_2048 --batch_size 1 --max_new_tokens 2048 --no-quantize --seed 42 > /root/runs/faith-evidence-ie/eval_llama_rsft_s42_with_evidence_2048.log 2>&1 & echo PID=\\$!\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_llama-rsft-s42-withevi-2048-launch_20260521T024516",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/freige && CUDA_VISIBLE_DEVICES=0 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 nohup python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_llama_3_1_8b_k1 --base_model /root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B --sft_adapter /root/autodl-tmp/sft_output_llama_3_1_8b --data_path /root/autodl-tmp/data/docred --split dev --output_dir /root/autodl-tmp/eval_results/eval_llama_rsft_s42_with_evidence_2048 --batch_size 1 --max_new_tokens 2048 --no-quantize --seed 42 > /root/runs/faith-evidence-ie/eval_llama_rsft_s42_with_evidence_2048.log 2>&1 & echo PID=\\$!\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-21T02:48:25.717717+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"PID=70706\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 30.42}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_llama-rsft-s42-withevi-2048-launch_20260521T024516",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-21T02:48:25.717867+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "ps -p 70706 -o pid,cmd --no-headers",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_llama-rsft-s42-withevi-2048-launch_20260521T024516",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "ps -p 70706 -o pid,cmd --no-headers",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-21T02:48:25.717997+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \" 70706 bash -c source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/freige && CUDA_VISIBLE_DEVICES=0 HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 nohup python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_llama_3_1_8b_k1 --base_model /root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B --sft_adapter /root/autodl-tmp/sft_output_llama_3_1_8b --data_path /root/autodl-tmp/data/docred --split dev --output_dir /root/autodl-tmp/eval_results/eval_llama_rsft_s42_with_evidence_2048 --batch_size 1 --max_new_tokens 2048 --no-quantize --seed 42 > /root/runs/faith-evidence-ie/eval_llama_rsft_s42_with_evidence_2048.log 2>&1 & echo PID=$!\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_llama-rsft-s42-withevi-2048-launch_20260521T024516",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-21T02:48:25.718121+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "nvidia-smi --query-gpu=index,memory.used,memory.total --format=csv,noheader",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_llama-rsft-s42-withevi-2048-launch_20260521T024516",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "nvidia-smi --query-gpu=index,memory.used,memory.total --format=csv,noheader",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-21T02:48:25.718271+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"0, 18879 MiB, 97887 MiB\\n1, 32503 MiB, 97887 MiB\\n2, 18879 MiB, 97887 MiB\\n3, 18879 MiB, 97887 MiB\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.55}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_llama-rsft-s42-withevi-2048-launch_20260521T024516",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-21T02:48:25.718405+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "rtx5090-4x",
  "command": "tail -5 /root/runs/faith-evidence-ie/eval_llama_rsft_s42_with_evidence_2048.log",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_llama-rsft-s42-withevi-2048-launch_20260521T024516",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "rtx5090-4x",
    "command": "tail -5 /root/runs/faith-evidence-ie/eval_llama_rsft_s42_with_evidence_2048.log",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-21T02:48:25.718543+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"2026-05-21 10:47:17,959 INFO Loaded 998 documents from /root/autodl-tmp/data/docred/dev.json\\n2026-05-21 10:47:18,149 INFO Processed 12275 relation samples from 998 documents (5445 samples without hard negatives)\\n2026-05-21 10:47:18,261 INFO Prepared 985 eval documents, 12275 gold triples\\n\\rInference:   0%|          | 0/985 [00:00<?, ?it/s][transformers] Ignoring clean_up_tokenization_spaces=True for BPE tokenizer TokenizersBackend. The clean_up_tokenization post-processing step is designed for WordPiece tokenizers and is destructive for BPE (it strips spaces before punctuation). Set clean_up_tokenization_spaces=False to suppress this warning, or set clean_up_tokenization_spaces_for_bpe_even_though_it_will_corrupt_output=True to force cleanup anyway.\\n\\rInference:   0%|          | 1/985 [00:03<1:00:57,  3.72s/it]\\rInference:   0%|          | 2/985 [00:18<2:43:40,  9.99s/it]\\rInference:   0%|          | 3/985 [00:26<2:29:51,  9.16s/it]\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_llama-rsft-s42-withevi-2048-launch_20260521T024516",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-21T02:48:25.718694+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_llama_rsft_s42_with_evidence_2048",
  "field": "status",
  "value": "RUNNING",
  "project": "faith-evidence-ie",
  "spec": "{'command': 'CUDA_VISIBLE_DEVICES=0 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_llama_3_1_8b_k1 --base_model /root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B --sft_adapter /root/autodl-tmp/sft_output_llama_3_1_8b --data_path /root/autodl-tmp/data/docred --split dev --output_dir /root/autodl-tmp/eval_results/eval_llama_rsft_s42_with_evidence_2048 --batch_size 1 --max_new_tokens 2048 --no-quantize --seed 42', 'server': 'rtx5090-4x', 'data_path': '/root/autodl-tmp/data/docred/dev.json', 'data_count': 985, 'model_name': 'Meta-Llama-3.1-8B + SFT + RSFT(k1)', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/rsft_output_llama_3_1_8b_k1', 'eval_data': 'DocRED dev set (985 docs, 12275 gold triples)', 'pid': 70706, 'gpu': 'cuda:0', 'gpu_mem_used': '18879 MiB', 'base_model': '/root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B', 'sft_adapter': '/root/autodl-tmp/sft_output_llama_3_1_8b', 'nested_lora': True, 'checkpoint_path': '/root/autodl-tmp/eval_results/eval_llama_rsft_s42_with_evidence_2048', 'log_path': '/root/runs/faith-evidence-ie/eval_llama_rsft_s42_with_evidence_2048.log'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_llama-rsft-s42-withevi-2048-launch_20260521T024516",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_llama_rsft_s42_with_evidence_2048",
    "field": "status",
    "value": "RUNNING",
    "project": "faith-evidence-ie",
    "spec": "{'command': 'CUDA_VISIBLE_DEVICES=0 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_llama_3_1_8b_k1 --base_model /root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B --sft_adapter /root/autodl-tmp/sft_output_llama_3_1_8b --data_path /root/autodl-tmp/data/docred --split dev --output_dir /root/autodl-tmp/eval_results/eval_llama_rsft_s42_with_evidence_2048 --batch_size 1 --max_new_tokens 2048 --no-quantize --seed 42', 'server': 'rtx5090-4x', 'data_path': '/root/autodl-tmp/data/docred/dev.json', 'data_count': 985, 'model_name': 'Meta-Llama-3.1-8B + SFT + RSFT(k1)', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/rsft_output_llama_3_1_8b_k1', 'eval_data': 'DocRED dev set (985 docs, 12275 gold triples)', 'pid': 70706, 'gpu': 'cuda:0', 'gpu_mem_used': '18879 MiB', 'base_model': '/root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B', 'sft_adapter': '/root/autodl-tmp/sft_output_llama_3_1_8b', 'nested_lora': True, 'checkpoint_path': '/root/autodl-tmp/eval_results/eval_llama_rsft_s42_with_evidence_2048', 'log_path': '/root/runs/faith-evidence-ie/eval_llama_rsft_s42_with_evidence_2048.log'}"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-21T02:48:25.718897+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 1.0981}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_llama-rsft-s42-withevi-2048-launch_20260521T024516",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-21T02:48:25.719031+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_llama_rsft_s42_with_evidence_2048",
  "field": "status",
  "value": "QUEUED",
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_llama-rsft-s42-withevi-2048-launch_20260521T024516",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_llama_rsft_s42_with_evidence_2048",
    "field": "status",
    "value": "QUEUED",
    "project": "faith-evidence-ie"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-21T02:48:25.719172+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_llama_rsft_s42_with_evidence_2048\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-21T02:48:01.287Z\", \"updated_at\": \"2026-05-21T02:48:01.287Z\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.7773}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_llama-rsft-s42-withevi-2048-launch_20260521T024516",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-21T02:48:25.719326+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_llama_rsft_s42_with_evidence_2048",
  "field": "status",
  "value": "RUNNING",
  "project": "faith-evidence-ie",
  "spec": "{'command': 'CUDA_VISIBLE_DEVICES=0 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_llama_3_1_8b_k1 --base_model /root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B --sft_adapter /root/autodl-tmp/sft_output_llama_3_1_8b --data_path /root/autodl-tmp/data/docred --split dev --output_dir /root/autodl-tmp/eval_results/eval_llama_rsft_s42_with_evidence_2048 --batch_size 1 --max_new_tokens 2048 --no-quantize --seed 42', 'server': 'rtx5090-4x', 'data_path': '/root/autodl-tmp/data/docred/dev.json', 'data_count': 985, 'model_name': 'Meta-Llama-3.1-8B + SFT + RSFT(k1)', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/rsft_output_llama_3_1_8b_k1', 'eval_data': 'DocRED dev set (985 docs, 12275 gold triples)', 'pid': 70706, 'gpu': 'cuda:0', 'gpu_mem_used': '18879 MiB', 'base_model': '/root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B', 'sft_adapter': '/root/autodl-tmp/sft_output_llama_3_1_8b', 'nested_lora': True, 'checkpoint_path': '/root/autodl-tmp/eval_results/eval_llama_rsft_s42_with_evidence_2048', 'log_path': '/root/runs/faith-evidence-ie/eval_llama_rsft_s42_with_evidence_2048.log'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_llama-rsft-s42-withevi-2048-launch_20260521T024516",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_llama_rsft_s42_with_evidence_2048",
    "field": "status",
    "value": "RUNNING",
    "project": "faith-evidence-ie",
    "spec": "{'command': 'CUDA_VISIBLE_DEVICES=0 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_llama_3_1_8b_k1 --base_model /root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B --sft_adapter /root/autodl-tmp/sft_output_llama_3_1_8b --data_path /root/autodl-tmp/data/docred --split dev --output_dir /root/autodl-tmp/eval_results/eval_llama_rsft_s42_with_evidence_2048 --batch_size 1 --max_new_tokens 2048 --no-quantize --seed 42', 'server': 'rtx5090-4x', 'data_path': '/root/autodl-tmp/data/docred/dev.json', 'data_count': 985, 'model_name': 'Meta-Llama-3.1-8B + SFT + RSFT(k1)', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/rsft_output_llama_3_1_8b_k1', 'eval_data': 'DocRED dev set (985 docs, 12275 gold triples)', 'pid': 70706, 'gpu': 'cuda:0', 'gpu_mem_used': '18879 MiB', 'base_model': '/root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B', 'sft_adapter': '/root/autodl-tmp/sft_output_llama_3_1_8b', 'nested_lora': True, 'checkpoint_path': '/root/autodl-tmp/eval_results/eval_llama_rsft_s42_with_evidence_2048', 'log_path': '/root/runs/faith-evidence-ie/eval_llama_rsft_s42_with_evidence_2048.log'}"
  }
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-21T02:48:25.719476+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_llama_rsft_s42_with_evidence_2048",
  "field": "hypothesis",
  "value": "matched@2048 control: LLaMA RSFT s42 with-evi@2048。@1024 ign_f1=0.5714。预期 delta<1pp，验证 RSFT evidence tax 在 matched budget 下稳定。",
  "project": "faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_llama-rsft-s42-withevi-2048-launch_20260521T024516",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_llama_rsft_s42_with_evidence_2048",
    "field": "hypothesis",
    "value": "matched@2048 control: LLaMA RSFT s42 with-evi@2048。@1024 ign_f1=0.5714。预期 delta<1pp，验证 RSFT evidence tax 在 matched budget 下稳定。",
    "project": "faith-evidence-ie"
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-21T02:48:25.719623+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_llama_rsft_s42_with_evidence_2048\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T02:48:01.287Z\", \"updated_at\": \"2026-05-21T02:48:11.699Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_llama_3_1_8b_k1 --base_model /root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B --sft_adapter /root/autodl-tmp/sft_output_llama_3_1_8b --data_path /root/autodl-tmp/data/docred --split dev --output_dir /root/autodl-tmp/eval_results/eval_llama_rsft_s42_with_evidence_2048 --batch_size 1 --max_new_tokens 2048 --no-quantize --seed 42\", \"server\": \"rtx5090-4x\", \"data_path\": \"/root/autodl-tmp/data/docred/dev.json\", \"data_count\": 985, \"model_name\": \"Meta-Llama-3.1-8B + SFT + RSFT(k1)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/rsft_output_llama_3_1_8b_k1\", \"eval_data\": \"DocRED dev set (985 docs, 12275 gold triples)\", \"pid\": 70706, \"gpu\": \"cuda:0\", \"gpu_mem_used\": \"18879 MiB\", \"base_model\": \"/root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B\", \"sft_adapter\": \"/root/autodl-tmp/sft_output_llama_3_1_8b\", \"nested_lora\": true, \"checkpoint_path\": \"/root/autodl-tmp/eval_results/eval_llama_rsft_s42_with_evidence_2048\", \"log_path\": \"/root/runs/faith-evidence-ie/eval_llama_rsft_s42_with_evidence_2048.log\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.1006}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_llama-rsft-s42-withevi-2048-launch_20260521T024516",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-21T02:48:25.719806+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_llama_rsft_s42_with_evidence_2048\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T02:48:01.287Z\", \"updated_at\": \"2026-05-21T02:48:14.804Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -m freige.eval.inference --model_path /root/autodl-tmp/rsft_output_llama_3_1_8b_k1 --base_model /root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B --sft_adapter /root/autodl-tmp/sft_output_llama_3_1_8b --data_path /root/autodl-tmp/data/docred --split dev --output_dir /root/autodl-tmp/eval_results/eval_llama_rsft_s42_with_evidence_2048 --batch_size 1 --max_new_tokens 2048 --no-quantize --seed 42\", \"server\": \"rtx5090-4x\", \"data_path\": \"/root/autodl-tmp/data/docred/dev.json\", \"data_count\": 985, \"model_name\": \"Meta-Llama-3.1-8B + SFT + RSFT(k1)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/rsft_output_llama_3_1_8b_k1\", \"eval_data\": \"DocRED dev set (985 docs, 12275 gold triples)\", \"pid\": 70706, \"gpu\": \"cuda:0\", \"gpu_mem_used\": \"18879 MiB\", \"base_model\": \"/root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B\", \"sft_adapter\": \"/root/autodl-tmp/sft_output_llama_3_1_8b\", \"nested_lora\": true, \"checkpoint_path\": \"/root/autodl-tmp/eval_results/eval_llama_rsft_s42_with_evidence_2048\", \"log_path\": \"/root/runs/faith-evidence-ie/eval_llama_rsft_s42_with_evidence_2048.log\"}, \"hypothesis\": \"matched@2048 control: LLaMA RSFT s42 with-evi@2048。@1024 ign_f1=0.5714。预期 delta<1pp，验证 RSFT evidence tax 在 matched budget 下稳定。\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.6544}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_llama-rsft-s42-withevi-2048-launch_20260521T024516",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 43 · 2026-05-21T02:48:25.719993+00:00_

已启动。

| 项目 | 值 |
|------|-----|
| **exp_id** | `eval_llama_rsft_s42_with_evidence_2048` |
| **PID** | 70706 |
| **GPU** | cuda:0, 18879 MiB |
| **Base** | `/root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B` |
| **SFT adapter** | `/root/autodl-tmp/sft_output_llama_3_1_8b` |
| **RSFT adapter** | `/root/autodl-tmp/rsft_output_llama_3_1_8b_k1` |
| **Output** | `/root/autodl-tmp/eval_results/eval_llama_rsft_s42_with_evidence_2048` |
| **Log** | `/root/runs/faith-evidence-ie/eval_llama_rsft_s42_with_evidence_2048.log` |

**完整命令：**
```
CUDA_VISIBLE_DEVICES=0 python -m freige.eval.inference \
  --model_path /root/autodl-tmp/rsft_output_llama_3_1_8b_k1 \
  --base_model /root/autodl-tmp/models/meta-llama/Meta-Llama-3.1-8B \
  --sft_adapter /root/autodl-tmp/sft_output_llama_3_1_8b \
  --data_path /root/autodl-tmp/data/docred --split dev \
  --output_dir /root/autodl-tmp/eval_results/eval_llama_rsft_s42_with_evidence_2048 \
  --batch_size 1 --max_new_tokens 2048 --no-quantize --seed 42
```

推理已进行中（~9s/it, 预计 ~2.5h）。Nested LoRA: base → merge SFT → load RSFT。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_code_llama-rsft-s42-withevi-2048-launch_20260521T024516"
}
```

</details>

---
