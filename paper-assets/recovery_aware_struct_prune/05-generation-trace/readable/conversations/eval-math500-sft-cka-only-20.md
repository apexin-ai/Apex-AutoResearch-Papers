# eval math500 sft cka only 20

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 31
- **Recorded user turns:** 0
- **Tool calls:** 15
- **Original source:** `logs/chats/worker_eval_math500_sft_cka_only_20_20260517T231846.jsonl`
- **Structured JSON:** [`e6e404d1440220050a2e.json`](../../sessions/e6/e6e404d1440220050a2e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

31 recorded events

### Tool call

_source line 1 · 2026-05-17T23:20:28.753902+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__read_registry",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_math500_sft_cka_only_20_20260517T231846",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__read_registry",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-17T23:20:28.754229+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_math500_sft_cka_only_20_20260517T231846",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-17T23:20:28.754433+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-11672",
  "command": "ls -la /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_math500_sft_cka_only_20_20260517T231846",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-11672",
    "command": "ls -la /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20/",
    "account": "root"
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-17T23:20:28.754571+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-11672",
  "command": "ls -la /root/recovery_aware_struct_prune/src/eval_math500.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_math500_sft_cka_only_20_20260517T231846",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-11672",
    "command": "ls -la /root/recovery_aware_struct_prune/src/eval_math500.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-17T23:20:28.754716+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 12046280\\ndrwxr-xr-x  2 root root        4096 May 18 03:14 .\\ndrwxr-xr-x 40 root root        4096 May 18 05:52 ..\\n-rw-r--r--  1 root root        2246 May 18 03:06 chat_template.jinja\\n-rw-r--r--  1 root root        1732 May 18 03:06 config.json\\n-rw-r--r--  1 root root         240 May 18 03:06 generation_config.json\\n-rw-r--r--  1 root root 12323931248 May 18 03:44 model.safetensors\\n-rw-r--r--  1 root root    11421907 May 18 03:06 tokenizer.json\\n-rw-r--r--  1 root root         420 May 18 03:06 tokenizer_config.json\\n-rw-r--r--  1 root root        5777 May 18 03:06 training_args.bin\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.11}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_math500_sft_cka_only_20_20260517T231846",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-17T23:20:28.754850+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"-rw-r--r-- 1 root root 7742 May 17 14:20 /root/recovery_aware_struct_prune/src/eval_math500.py\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.48}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_math500_sft_cka_only_20_20260517T231846",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-17T23:20:28.754990+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__register_artifact",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_math500_sft_cka_only_20_20260517T231846",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__register_artifact",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-17T23:20:28.755109+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_math500_sft_cka_only_20_20260517T231846",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-17T23:20:28.755237+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "submit training job",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_math500_sft_cka_only_20_20260517T231846",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "submit training job",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-17T23:20:28.755384+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_math500_sft_cka_only_20_20260517T231846",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-17T23:20:28.755513+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "submit job gpu experiment",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_math500_sft_cka_only_20_20260517T231846",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "submit job gpu experiment",
    "max_results": "5"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-17T23:20:28.755631+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_math500_sft_cka_only_20_20260517T231846",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-17T23:20:28.755788+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__update_registry",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_math500_sft_cka_only_20_20260517T231846",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__update_registry",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-17T23:20:28.755910+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_math500_sft_cka_only_20_20260517T231846",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-17T23:20:28.756024+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-11672",
  "command": "tmux new-session -d -s eval_math500_sft_cka_only_20 \"CUDA_VISIBLE_DEVICES=2 bash -c 'source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/math500_sft_cka_only_20.json' 2>&1 | tee /root/autodl-tmp/recovery_aware_struct_prune/logs/eval_math500_sft_cka_only_20.log\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_math500_sft_cka_only_20_20260517T231846",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-11672",
    "command": "tmux new-session -d -s eval_math500_sft_cka_only_20 \"CUDA_VISIBLE_DEVICES=2 bash -c 'source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/math500_sft_cka_only_20.json' 2>&1 | tee /root/autodl-tmp/recovery_aware_struct_prune/logs/eval_math500_sft_cka_only_20.log\"",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-17T23:20:28.756148+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_math500_sft_cka_only_20_20260517T231846",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-17T23:20:28.756298+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-11672",
  "command": "ps aux | grep eval_math500",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_math500_sft_cka_only_20_20260517T231846",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-11672",
    "command": "ps aux | grep eval_math500",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-17T23:20:28.756427+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_math500_sft_cka_only_20_20260517T231846",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-17T23:20:28.756543+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-11672",
  "command": "ls -la /root/autodl-tmp/recovery_aware_struct_prune/grpo_unpruned_v2/",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_math500_sft_cka_only_20_20260517T231846",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-11672",
    "command": "ls -la /root/autodl-tmp/recovery_aware_struct_prune/grpo_unpruned_v2/",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-17T23:20:28.756667+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"total 14885492\\ndrwxr-xr-x  4 root root        4096 May 16 13:24 .\\ndrwxr-xr-x 40 root root        4096 May 18 05:52 ..\\n-rw-r--r--  1 root root        2092 May 16 10:59 README.md\\n-rw-r--r--  1 root root        2246 May 16 11:00 chat_template.jinja\\ndrwxr-xr-x  2 root root        4096 May 16 10:59 checkpoint-100\\ndrwxr-xr-x  2 root root        4096 May 16 10:59 completions\\n-rw-r--r--  1 root root        1396 May 16 10:59 config.json\\n-rw-r--r--  1 root root         216 May 16 10:59 generation_config.json\\n-rw-r--r--  1 root root 15231272152 May 16 11:00 model.safetensors\\n-rw-r--r--  1 root root    11421907 May 16 11:00 tokenizer.json\\n-rw-r--r--  1 root root         420 May 16 11:00 tokenizer_config.json\\n-rw-r--r--  1 root root        7313 May 16 11:00 training_args.bin\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_math500_sft_cka_only_20_20260517T231846",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-17T23:20:28.756787+00:00_

called mcp__agent-ml-research__ssh_execute

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute</summary>

```json
{
  "server": "westd-11672",
  "command": "ps aux | grep eval_math500 | grep -v grep",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_math500_sft_cka_only_20_20260517T231846",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "tool_args": {
    "server": "westd-11672",
    "command": "ps aux | grep eval_math500 | grep -v grep",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-17T23:20:28.756959+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"root       2506  0.0  0.0   6328  4044 ?        Ss   May17   0:01 tmux new-session -d -s eval_math500_unpruned bash -c 'source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && export HF_ENDPOINT=https://hf-mirror.com && CUDA_VISIBLE_DEVICES=0 python src/eval_math500.py --model_path /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_unpruned.json --seed 42 --max_new_tokens 4096 2>&1 | tee /root/runs/recovery_aware_struct_prune/eval_math500_unpruned.log; echo EXIT_CODE=$? >> /root/runs/recovery_aware_struct_prune/eval_math500_unpruned.log'\\nroot      14551  0.0  0.0   4364  3260 ?        S    May17   0:00 bash -c source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && export HF_ENDPOINT=https://hf-mirror.com && CUDA_VISIBLE_DEVICES=1 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_v8/checkpoint-50 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_grpo_standard_20.json --seed 42 --max_new_tokens 4096 2>&1 | tee /root/autodl-tmp/recovery_aware_struct_prune/eval_math500_grpo_standard_20.log\\nroot      14556  101  0.1 76175776 2039836 ?    Rl   May17 843:12 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_v8/checkpoint-50 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_grpo_standard_20.json --seed 42 --max_new_tokens 4096\\nroot      14557  0.0  0.0   2796  1024 ?        S    May17   0:00 tee /root/autodl-tmp/recovery_aware_struct_prune/eval_math500_grpo_standard_20.log\\nroot      31701  0.0  0.0   4496  3564 pts/2    Ss+  May17   0:00 bash -c rm -f /tmp/agent-ml-exit/eval_math500_grpo_rasp_20_v3.exit; mkdir -p /tmp/agent-ml-exit; trap '_EC=$?; echo \\\"EXIT_CODE=$_EC\\\" >> ~/runs/recovery_aware_struct_prune/eval_
…[truncated 3989 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_math500_sft_cka_only_20_20260517T231846",
  "tool": "mcp__agent-ml-research__ssh_execute",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-17T23:20:28.757145+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_math500_sft_cka_only_20",
  "field": "status",
  "value": "RUNNING",
  "project": "recovery_aware_struct_prune",
  "spec": "{'command': 'python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/math500_sft_cka_only_20.json', 'server': 'westd-11672', 'gpu': 'cuda:2', 'data_path': '/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20', 'model_name': 'sft_cka_only_20', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20', 'eval_data': 'MATH-500'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_math500_sft_cka_only_20_20260517T231846",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_math500_sft_cka_only_20",
    "field": "status",
    "value": "RUNNING",
    "project": "recovery_aware_struct_prune",
    "spec": "{'command': 'python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/math500_sft_cka_only_20.json', 'server': 'westd-11672', 'gpu': 'cuda:2', 'data_path': '/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20', 'model_name': 'sft_cka_only_20', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20', 'eval_data': 'MATH-500'}"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-17T23:20:28.757311+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Invalid transition: PREPARING → RUNNING. Allowed: ['PENDING', 'QUEUED']\", \"metadata\": {\"elapsed_seconds\": 1.1962}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_math500_sft_cka_only_20_20260517T231846",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-17T23:20:28.757444+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_math500_sft_cka_only_20",
  "field": "status",
  "value": "QUEUED",
  "project": "recovery_aware_struct_prune"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_math500_sft_cka_only_20_20260517T231846",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_math500_sft_cka_only_20",
    "field": "status",
    "value": "QUEUED",
    "project": "recovery_aware_struct_prune"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-17T23:20:28.757584+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_math500_sft_cka_only_20\", \"experiment\": {\"status\": \"QUEUED\", \"retry_count\": 0, \"created_at\": \"2026-05-17T22:59:03.755Z\", \"updated_at\": \"2026-05-17T23:20:07.310Z\", \"hypothesis\": \"CKA-only SFT MATH-500 baseline. With SFT Standard=26%, SFT RASP=24.2%, if CKA-only SFT > 26%, CKA-only scoring has OOD advantage. Future comparison with GRPO CKA-only MATH-500 tests C1 decoupling for CKA-only method.\"}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 3.3181}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_math500_sft_cka_only_20_20260517T231846",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-17T23:20:28.757728+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_math500_sft_cka_only_20",
  "field": "status",
  "value": "RUNNING",
  "project": "recovery_aware_struct_prune",
  "spec": "{'command': 'python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/math500_sft_cka_only_20.json', 'server': 'westd-11672', 'gpu': 'cuda:2', 'data_path': '/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20', 'model_name': 'sft_cka_only_20', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20', 'eval_data': 'MATH-500'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_math500_sft_cka_only_20_20260517T231846",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_math500_sft_cka_only_20",
    "field": "status",
    "value": "RUNNING",
    "project": "recovery_aware_struct_prune",
    "spec": "{'command': 'python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/math500_sft_cka_only_20.json', 'server': 'westd-11672', 'gpu': 'cuda:2', 'data_path': '/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20', 'model_name': 'sft_cka_only_20', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20', 'eval_data': 'MATH-500'}"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-17T23:20:28.757878+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"Cannot transition to RUNNING without spec fields: ['data_count']. Pass spec={...} with at least: ['command', 'data_count', 'data_path', 'model_name', 'seed', 'server']\", \"metadata\": {\"elapsed_seconds\": 0.7582}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_math500_sft_cka_only_20_20260517T231846",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-17T23:20:28.758001+00:00_

called mcp__agent-ml-research__update_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_registry</summary>

```json
{
  "exp_id": "eval_math500_sft_cka_only_20",
  "field": "status",
  "value": "RUNNING",
  "project": "recovery_aware_struct_prune",
  "spec": "{'command': 'python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/math500_sft_cka_only_20.json', 'server': 'westd-11672', 'gpu': 'cuda:2', 'data_path': '/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20', 'data_count': 500, 'model_name': 'sft_cka_only_20', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20', 'eval_data': 'MATH-500'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_eval_math500_sft_cka_only_20_20260517T231846",
  "tool": "mcp__agent-ml-research__update_registry",
  "tool_args": {
    "exp_id": "eval_math500_sft_cka_only_20",
    "field": "status",
    "value": "RUNNING",
    "project": "recovery_aware_struct_prune",
    "spec": "{'command': 'python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/math500_sft_cka_only_20.json', 'server': 'westd-11672', 'gpu': 'cuda:2', 'data_path': '/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20', 'data_count': 500, 'model_name': 'sft_cka_only_20', 'seed': 42, 'checkpoint_source': '/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20', 'eval_data': 'MATH-500'}"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-17T23:20:28.758147+00:00_

{"result":"{\"success\": true, \"data\": {\"exp_id\": \"eval_math500_sft_cka_only_20\", \"experiment\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-17T22:59:03.755Z\", \"updated_at\": \"2026-05-17T23:20:20.522Z\", \"hypothesis\": \"CKA-only SFT MATH-500 baseline. With SFT Standard=26%, SFT RASP=24.2%, if CKA-only SFT > 26%, CKA-only scoring has OOD advantage. Future comparison with GRPO CKA-only MATH-500 tests C1 decoupling for CKA-only method.\", \"spec\": {\"command\": \"python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/math500_sft_cka_only_20.json\", \"server\": \"westd-11672\", \"gpu\": \"cuda:2\", \"data_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20\", \"data_count\": 500, \"model_name\": \"sft_cka_only_20\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20\", \"eval_data\": \"MATH-500\"}}}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.3743}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_eval_math500_sft_cka_only_20_20260517T231846",
  "tool": "mcp__agent-ml-research__update_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-17T23:20:28.758336+00:00_

Registry 已更新为 RUNNING。

## 总结

| 项目 | 状态 |
|------|------|
| eval_math500_sft_cka_only_20 | 已提交，PID 65395，tmux session `eval_math500_sft_cka_only_20` |
| Registry | RUNNING |
| grpo_unpruned_v2 | **已在 westd-11672** `/root/autodl-tmp/recovery_aware_struct_prune/grpo_unpruned_v2/` (~15GB) |

**⚠️ GPU 冲突警告**：cuda:2 上已有 `eval_math500_grpo_unpruned` (PID 64472, 07:09启动) 在运行。新任务与其共享 cuda:2，高概率 OOM。建议 kill 其中一个，或将新任务迁移到其他 GPU（但当前 4 张 GPU 全满）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_eval_math500_sft_cka_only_20_20260517T231846"
}
```

</details>

---
