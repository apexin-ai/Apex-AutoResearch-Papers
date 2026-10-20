# code appendix seeds perturn crossmodel

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 229
- **Recorded user turns:** 0
- **Tool calls:** 114
- **Original source:** `logs/chats/worker_code_appendix_seeds_perturn_crossmodel_20260524T150612.jsonl`
- **Structured JSON:** [`757e7087a5665c380d8a.json`](../../sessions/75/757e7087a5665c380d8a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

229 recorded events

### Tool call

_source line 1 · 2026-05-24T15:22:21.888829+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__detect_image,mcp__agent-ml-research__read_registry",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__detect_image,mcp__agent-ml-research__read_registry",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-24T15:22:21.889198+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-24T15:22:21.889382+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-20861",
  "command": "find /root/turn-residual-gating/results/ -type f -name \"*.json\" -o -name \"*.csv\" -o -name \"*.txt\" -o -name \"*.log\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-20861",
    "command": "find /root/turn-residual-gating/results/ -type f -name \"*.json\" -o -name \"*.csv\" -o -name \"*.txt\" -o -name \"*.log\""
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-24T15:22:21.889570+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-20861",
  "command": "ls -la /root/turn-residual-gating/results/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-20861",
    "command": "ls -la /root/turn-residual-gating/results/"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-24T15:22:21.889711+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"find: '/root/turn-residual-gating/results/': No such file or directory\\n\", \"return_code\": 1}, \"error\": \"exit code 1\", \"metadata\": {\"elapsed_seconds\": 1.23}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-24T15:22:21.889838+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "turn_residual_gating",
  "limit": "0",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "turn_residual_gating",
    "limit": "0",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-24T15:22:21.889967+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"ls: cannot access '/root/turn-residual-gating/results/': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.49}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-24T15:22:21.890088+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-20861",
  "command": "ls -la /root/turn-residual-gating/runs/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-20861",
    "command": "ls -la /root/turn-residual-gating/runs/"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-24T15:22:21.890615+00:00_

Error: result (93,111 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/66de9ef3-78db-4116-ae9e-2eba3b117097/tool-results/mcp-agent-ml-research-read_registry-1779635195899.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/66de9ef3-78db-4116-ae9e-2eba3b117097/tool-results/mcp-agent-ml-research-read_registry-1779635195899.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/66de9ef3-78db-4116-ae9e-2eba3b117097/tool-results/mcp-agent-ml-research-read_registry-1779635195899.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-24T15:22:21.890820+00:00_

{"result":"{\"success\": false, \"data\": {\"stdout\": \"\", \"stderr\": \"ls: cannot access '/root/turn-residual-gating/runs/': No such file or directory\\n\", \"return_code\": 2}, \"error\": \"exit code 2\", \"metadata\": {\"elapsed_seconds\": 0.46}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-24T15:22:21.890978+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-20861",
  "command": "find /root -maxdepth 3 -type d -name \"*turn*\" -o -name \"*residual*\" -o -name \"*gating*\" -o -name \"*tg*\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-20861",
    "command": "find /root -maxdepth 3 -type d -name \"*turn*\" -o -name \"*residual*\" -o -name \"*gating*\" -o -name \"*tg*\""
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-24T15:22:21.891102+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-20861",
  "command": "ls /root/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-20861",
    "command": "ls /root/"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-24T15:22:21.891249+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/miniconda3/lib/tdbcpostgres1.1.7\\n/root/turn_residual_gating\\n/root/turn_residual_gating/results/phase2_tg_s42_v7_dongre_gar.json\\n/root/turn_residual_gating/results/phase2_tg_s42_v7_dongre_gar_comparison.png\\n/root/turn_residual_gating/results/phase2_tg_s42_v7_gar.json\\n/root/turn_residual_gating/results/phase2_tg_s42_v7_gar_comparison.png\\n/root/turn_residual_gating/checkpoints/tg_s42\\n/root/turn_residual_gating/checkpoints/tg_v9_pcgrad_s42\\n/root/turn_residual_gating/checkpoints/tg_v8b_ss_fixed_s42_dryrun\\n/root/turn_residual_gating/checkpoints/tg_v8b_ss_fixed_s42\\n/root/turn_residual_gating/checkpoints/tg_v8b_ss_s123\\n/root/turn_residual_gating/runs/phase2_tg_s42_v3.log\\n/root/turn_residual_gating/runs/phase2_tg_s42_v4.log\\n/root/turn_residual_gating/runs/phase2_tg_s42_v7\\n/root/turn_residual_gating/runs/phase2_tg_s42_v7.log\\n/root/turn_residual_gating/runs/phase2_llama_tg_s42\\n/root/turn_residual_gating/runs/eval_llama_tg_s42.log\\n/root/turn_residual_gating/runs/eval_llama_tg_s42\\n/root/turn_residual_gating/runs/phase2_tg_s123_v7\\n/root/turn_residual_gating/runs/eval_v7_tg_s123\\n/root/turn_residual_gating/runs/qwen15b_tg_v7_s42\\n/root/turn_residual_gating/scripts/launch_tg_s123.sh\\n/root/turn_residual_gating/scripts/launch_llama_tg.sh\\n/root/turn_residual_gating/scripts/eval_llama_tg_s42.sh\\n/root/turn_residual_gating/scripts/launch_v7_tg_s123.sh\\n/root/turn_residual_gating/scripts/eval_v7_tg_s123.sh\\n/root/turn_residual_gating/scripts/d048_tg_s123.sh\\n/root/turn_residual_gating/scripts/d048_tg_s456.sh\\n/root/turn_residual_gating/scripts/qwen15b_tg_train.sh\\n/root/turn_residual_gating/logs/llama_tg_training.log\\n/root/turn_residual_gating/logs/v7_tg_s123.log\\n/root/runs/turn_residual_gating\\n/root/runs/turn_residual_gating/phase2_tg_s42.log\\n/root/runs/turn_residual_gating/phase2_tg_s42_v2.log\\n/root/runs/turn_residual_gating/phase2_tg_s42_v5.log\\n/root/runs/turn_re
…[truncated 607 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-24T15:22:21.891426+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"autodl-pub\\nautodl-tmp\\nminiconda3\\nruns\\ntf-logs\\nturn-residual-gating\\nturn_residual_gating\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.53}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-24T15:22:21.891567+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Parse experiment registry",
  "prompt": "Parse the experiment registry JSON file at /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/66de9ef3-78db-4116-ae9e-2eba3b117097/tool-results/mcp-agent-ml-research-read_registry-1779635195899.txt\n\nThis is JSON with schema: {result: string}. The \"result\" field is itself a JSON string that needs to be parsed.\n\nI need you to extract ALL experiment entries and for each one report:\n1. experiment name/id\n2. status\n3. metrics (especially GAR, PPL, NGAR, per_turn data if any)\n4. conclusion\n5. any per-seed results\n6. any per-turn GAR data\n7. model type (qwen vs llama)\n8. condition (Base, TG, SS, LoRA, UG, PCGrad)\n\nFocus especially on:\n- Multi-seed eval results for SS (s42/s123/s456) and TG (s42/s123)\n- Per-turn GAR data\n- Llama cross-model results\n- Any entry with \"llama\" in the name\n\nReport ALL metrics verbatim - don't summarize or abbreviate numbers. This is for generating paper tables.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "Agent",
  "tool_args": {
    "description": "Parse experiment registry",
    "prompt": "Parse the experiment registry JSON file at /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/66de9ef3-78db-4116-ae9e-2eba3b117097/tool-results/mcp-agent-ml-research-read_registry-1779635195899.txt\n\nThis is JSON with schema: {result: string}. The \"result\" field is itself a JSON string that needs to be parsed.\n\nI need you to extract ALL experiment entries and for each one report:\n1. experiment name/id\n2. status\n3. metrics (especially GAR, PPL, NGAR, per_turn data if any)\n4. conclusion\n5. any per-seed results\n6. any per-turn GAR data\n7. model type (qwen vs llama)\n8. condition (Base, TG, SS, LoRA, UG, PCGrad)\n\nFocus especially on:\n- Multi-seed eval results for SS (s42/s123/s456) and TG (s42/s123)\n- Per-turn GAR data\n- Llama cross-model results\n- Any entry with \"llama\" in the name\n\nReport ALL metrics verbatim - don't summarize or abbreviate numbers. This is for generating paper tables.",
    "subagent_type": "general-purpose"
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-24T15:22:21.891724+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/66de9ef3-78db-4116-ae9e-2eba3b117097/tool-results/mcp-agent-ml-research-read_registry-1779635195899.txt",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/66de9ef3-78db-4116-ae9e-2eba3b117097/tool-results/mcp-agent-ml-research-read_registry-1779635195899.txt",
    "limit": "100"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-24T15:22:21.891846+00:00_

File content (43516 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-24T15:22:21.891971+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/66de9ef3-78db-4116-ae9e-2eba3b117097/tool-results/mcp-agent-ml-research-read_registry-1779635195899.txt",
  "limit": "500",
  "offset": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/66de9ef3-78db-4116-ae9e-2eba3b117097/tool-results/mcp-agent-ml-research-read_registry-1779635195899.txt",
    "limit": "500",
    "offset": "0"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-24T15:22:21.892089+00:00_

File content (43516 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-24T15:22:21.892210+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "wc -l /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/66de9ef3-78db-4116-ae9e-2eba3b117097/tool-results/mcp-agent-ml-research-read_registry-1779635195899.txt",
  "description": "Count lines in the registry file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "Bash",
  "tool_args": {
    "command": "wc -l /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/66de9ef3-78db-4116-ae9e-2eba3b117097/tool-results/mcp-agent-ml-research-read_registry-1779635195899.txt",
    "description": "Count lines in the registry file"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-24T15:22:21.892331+00:00_

0 /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/66de9ef3-78db-4116-ae9e-2eba3b117097/tool-results/mcp-agent-ml-research-read_registry-1779635195899.txt

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-24T15:22:21.892476+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport json, sys\n\nwith open('/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/66de9ef3-78db-4116-ae9e-2eba3b117097/tool-results/mcp-agent-ml-research-read_registry-1779635195899.txt', 'r') as f:\n    outer = json.load(f)\n\ninner = json.loads(outer['result'])\nprint(type(inner))\nif isinstance(inner, dict):\n    print('Top-level keys:', list(inner.keys()))\n    for k, v in inner.items():\n        print(f'  {k}: type={type(v).__name__}')\n        if isinstance(v, dict):\n            print(f'    subkeys: {list(v.keys())[:10]}')\n        elif isinstance(v, list):\n            print(f'    length: {len(v)}')\nelif isinstance(inner, list):\n    print(f'List length: {len(inner)}')\n    if inner:\n        print(f'First item type: {type(inner[0]).__name__}')\n        if isinstance(inner[0], dict):\n            print(f'First item keys: {list(inner[0].keys())}')\n\" 2>&1\n",
  "description": "Parse the outer JSON structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport json, sys\n\nwith open('/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/66de9ef3-78db-4116-ae9e-2eba3b117097/tool-results/mcp-agent-ml-research-read_registry-1779635195899.txt', 'r') as f:\n    outer = json.load(f)\n\ninner = json.loads(outer['result'])\nprint(type(inner))\nif isinstance(inner, dict):\n    print('Top-level keys:', list(inner.keys()))\n    for k, v in inner.items():\n        print(f'  {k}: type={type(v).__name__}')\n        if isinstance(v, dict):\n            print(f'    subkeys: {list(v.keys())[:10]}')\n        elif isinstance(v, list):\n            print(f'    length: {len(v)}')\nelif isinstance(inner, list):\n    print(f'List length: {len(inner)}')\n    if inner:\n        print(f'First item type: {type(inner[0]).__name__}')\n        if isinstance(inner[0], dict):\n            print(f'First item keys: {list(inner[0].keys())}')\n\" 2>&1\n",
    "description": "Parse the outer JSON structure"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-24T15:22:21.892602+00:00_

&lt;class 'dict'>
Top-level keys: ['success', 'data', 'error', 'metadata']
  success: type=bool
  data: type=dict
    subkeys: ['experiments', 'count', 'total', 'baseline']
  error: type=NoneType
  metadata: type=dict
    subkeys: ['elapsed_seconds']

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-24T15:22:21.892726+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/66de9ef3-78db-4116-ae9e-2eba3b117097/tool-results/mcp-agent-ml-research-read_registry-1779635195899.txt', 'r') as f:\n    outer = json.load(f)\n\ninner = json.loads(outer['result'])\ndata = inner['data']\nprint('count:', data['count'])\nprint('total:', data['total'])\nprint('baseline:', data.get('baseline'))\nprint()\nexps = data['experiments']\nprint(f'Number of experiments: {len(exps)}')\nprint()\nfor i, exp in enumerate(exps):\n    print(f'--- Experiment {i} ---')\n    print(f'  name: {exp.get(\\\"name\\\", \\\"N/A\\\")}')\n    print(f'  id: {exp.get(\\\"id\\\", \\\"N/A\\\")}')\n    print(f'  status: {exp.get(\\\"status\\\", \\\"N/A\\\")}')\n    print(f'  keys: {list(exp.keys())}')\n    print()\n\" 2>&1\n",
  "description": "List all experiments with names and status"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/66de9ef3-78db-4116-ae9e-2eba3b117097/tool-results/mcp-agent-ml-research-read_registry-1779635195899.txt', 'r') as f:\n    outer = json.load(f)\n\ninner = json.loads(outer['result'])\ndata = inner['data']\nprint('count:', data['count'])\nprint('total:', data['total'])\nprint('baseline:', data.get('baseline'))\nprint()\nexps = data['experiments']\nprint(f'Number of experiments: {len(exps)}')\nprint()\nfor i, exp in enumerate(exps):\n    print(f'--- Experiment {i} ---')\n    print(f'  name: {exp.get(\\\"name\\\", \\\"N/A\\\")}')\n    print(f'  id: {exp.get(\\\"id\\\", \\\"N/A\\\")}')\n    print(f'  status: {exp.get(\\\"status\\\", \\\"N/A\\\")}')\n    print(f'  keys: {list(exp.keys())}')\n    print()\n\" 2>&1\n",
    "description": "List all experiments with names and status"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-24T15:22:21.892848+00:00_

Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 18, in &lt;module>
    print(f'  name: {exp.get("name", "N/A")}')
                     ^^^^^^^
AttributeError: 'str' object has no attribute 'get'
count: 53
total: 53
baseline: None

Number of experiments: 53

--- Experiment 0 ---

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-24T15:22:21.892970+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/66de9ef3-78db-4116-ae9e-2eba3b117097/tool-results/mcp-agent-ml-research-read_registry-1779635195899.txt', 'r') as f:\n    outer = json.load(f)\n\ninner = json.loads(outer['result'])\ndata = inner['data']\nexps = data['experiments']\n\n# experiments is a dict with string keys\nprint(type(exps))\nif isinstance(exps, dict):\n    keys = list(exps.keys())\n    print(f'Number of keys: {len(keys)}')\n    for k in keys[:3]:\n        print(f'Key: {k}')\n        print(f'Value type: {type(exps[k]).__name__}')\n        v = exps[k]\n        if isinstance(v, dict):\n            print(f'  subkeys: {list(v.keys())}')\n        elif isinstance(v, str):\n            print(f'  value (first 200 chars): {v[:200]}')\n        print()\nelif isinstance(exps, list):\n    print('First 3 items:')\n    for item in exps[:3]:\n        print(f'  type={type(item).__name__}, value={str(item)[:200]}')\n\" 2>&1\n",
  "description": "Inspect structure of experiments dict"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/66de9ef3-78db-4116-ae9e-2eba3b117097/tool-results/mcp-agent-ml-research-read_registry-1779635195899.txt', 'r') as f:\n    outer = json.load(f)\n\ninner = json.loads(outer['result'])\ndata = inner['data']\nexps = data['experiments']\n\n# experiments is a dict with string keys\nprint(type(exps))\nif isinstance(exps, dict):\n    keys = list(exps.keys())\n    print(f'Number of keys: {len(keys)}')\n    for k in keys[:3]:\n        print(f'Key: {k}')\n        print(f'Value type: {type(exps[k]).__name__}')\n        v = exps[k]\n        if isinstance(v, dict):\n            print(f'  subkeys: {list(v.keys())}')\n        elif isinstance(v, str):\n            print(f'  value (first 200 chars): {v[:200]}')\n        print()\nelif isinstance(exps, list):\n    print('First 3 items:')\n    for item in exps[:3]:\n        print(f'  type={type(item).__name__}, value={str(item)[:200]}')\n\" 2>&1\n",
    "description": "Inspect structure of experiments dict"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-24T15:22:21.893096+00:00_

&lt;class 'dict'>
Number of keys: 53
Key: mmlu_eval_all
Value type: dict
  subkeys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'spec', 'conclusion', 'metrics', 'completed_at']

Key: p1_llama_ss_training
Value type: dict
  subkeys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'spec']

Key: p2_llama_gradient_conflict
Value type: dict
  subkeys: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'spec', 'conclusion', 'metrics', 'completed_at']

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-24T15:22:21.893221+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/66de9ef3-78db-4116-ae9e-2eba3b117097/tool-results/mcp-agent-ml-research-read_registry-1779635195899.txt', 'r') as f:\n    outer = json.load(f)\n\ninner = json.loads(outer['result'])\ndata = inner['data']\nexps = data['experiments']\n\nkeys = sorted(exps.keys())\nfor k in keys:\n    print(f'  {k}: status={exps[k].get(\\\"status\\\",\\\"?\\\")}')\" 2>&1\n",
  "description": "List all 53 experiment names and statuses"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/66de9ef3-78db-4116-ae9e-2eba3b117097/tool-results/mcp-agent-ml-research-read_registry-1779635195899.txt', 'r') as f:\n    outer = json.load(f)\n\ninner = json.loads(outer['result'])\ndata = inner['data']\nexps = data['experiments']\n\nkeys = sorted(exps.keys())\nfor k in keys:\n    print(f'  {k}: status={exps[k].get(\\\"status\\\",\\\"?\\\")}')\" 2>&1\n",
    "description": "List all 53 experiment names and statuses"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-24T15:22:21.893340+00:00_

  analysis_attention_heatmap: status=DONE
  analysis_gradient_conflict: status=DONE
  attention_steering_eval200_tf: status=DONE
  attention_steering_gen_n50: status=DONE
  attention_steering_v7_tg_gen: status=DONE
  d048_eval_ss_s123: status=DONE
  d048_eval_ss_s42: status=DONE
  d048_eval_ss_s456: status=DONE
  d048_final_ar_eval: status=DONE
  d048_queue_runner: status=PREPARING
  d048_split_softmax_eval: status=DONE
  d048_ss_s123: status=DONE
  d048_ss_s42: status=DONE
  d048_ss_s42_resume: status=PREPARING
  d048_ss_s456: status=DONE
  eval_llama_ar_n20: status=DONE
  eval_llama_lora_only_s42: status=DONE
  eval_v7_tg_s123: status=DONE
  eval_v8b_ss: status=DONE
  eval_v8b_ss_s123: status=DONE
  instruction_retention_test: status=DONE
  llama_ar_matched_eval: status=DONE
  llama_eval_s42: status=DONE
  llama_lora_only_s42: status=DONE
  llama_phase1_gar_diag: status=DONE
  llama_tg_s42: status=DONE
  llama_tg_training: status=PREPARING
  mmlu_eval_all: status=DONE
  p0_ss_steering_eval: status=PREPARING
  p1_llama_ss_training: status=RUNNING
  p1_tf_ar_kl_divergence: status=DONE
  p2_llama_gradient_conflict: status=DONE
  phase1_gar_diag: status=DONE
  phase2_4way_eval: status=DONE
  phase2_4way_eval_heldout: status=DONE
  phase2_lora_only_s42: status=DONE
  phase2_tg_s42: status=DONE
  phase2_tg_s42_v2: status=DONE
  phase2_tg_s42_v3: status=DONE
  phase2_tg_s42_v3b: status=DONE
  phase2_tg_s42_v4: status=DONE
  phase2_tg_s42_v5: status=DONE
  phase2_tg_s42_v6: status=DONE
  phase2_tg_s42_v7: status=DONE
  phase2_tg_s42_v8_schedsampling: status=DONE
  phase2_tg_s42_v8b_resume: status=DONE
  phase2_tg_s42_v8b_ss_fixed: status=DONE
  phase2_tg_s42_v9_pcgrad: status=DONE
  phase2_ug_s42: status=DONE
  qwen15b_phase1_diag: status=DONE
  trc_baseline_v7_tg: status=DONE
  v7_tg_s123: status=DONE
  v8b_ss_s123: status=DONE

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-24T15:22:21.893500+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nwith open('/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/66de9ef3-78db-4116-ae9e-2eba3b117097/tool-results/mcp-agent-ml-research-read_registry-1779635195899.txt', 'r') as f:\n    outer = json.load(f)\n\ninner = json.loads(outer['result'])\nexps = inner['data']['experiments']\n\n# Dump all experiments to a temp file for easier reading\nwith open('/tmp/all_experiments.json', 'w') as f:\n    json.dump(exps, f, indent=2, ensure_ascii=False)\n\nprint(\"Written to /tmp/all_experiments.json\")\nimport os\nprint(f\"Size: {os.path.getsize('/tmp/all_experiments.json')} bytes\")\nPYEOF\n",
  "description": "Dump all experiments to temp file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 << 'PYEOF'\nimport json\n\nwith open('/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/66de9ef3-78db-4116-ae9e-2eba3b117097/tool-results/mcp-agent-ml-research-read_registry-1779635195899.txt', 'r') as f:\n    outer = json.load(f)\n\ninner = json.loads(outer['result'])\nexps = inner['data']['experiments']\n\n# Dump all experiments to a temp file for easier reading\nwith open('/tmp/all_experiments.json', 'w') as f:\n    json.dump(exps, f, indent=2, ensure_ascii=False)\n\nprint(\"Written to /tmp/all_experiments.json\")\nimport os\nprint(f\"Size: {os.path.getsize('/tmp/all_experiments.json')} bytes\")\nPYEOF\n",
    "description": "Dump all experiments to temp file"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-24T15:22:21.893621+00:00_

Written to /tmp/all_experiments.json
Size: 105600 bytes

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-24T15:22:21.893747+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nwith open('/tmp/all_experiments.json', 'r') as f:\n    exps = json.load(f)\n\n# Process each experiment and output full details\nkeys = sorted(exps.keys())\n\nfor k in keys:\n    exp = exps[k]\n    print(f\"{'='*80}\")\n    print(f\"EXPERIMENT: {k}\")\n    print(f\"{'='*80}\")\n    print(f\"  Status: {exp.get('status', 'N/A')}\")\n    print(f\"  Created: {exp.get('created_at', 'N/A')}\")\n    print(f\"  Updated: {exp.get('updated_at', 'N/A')}\")\n    print(f\"  Completed: {exp.get('completed_at', 'N/A')}\")\n    print(f\"  Retry count: {exp.get('retry_count', 'N/A')}\")\n    \n    hyp = exp.get('hypothesis', '')\n    if hyp:\n        print(f\"  Hypothesis: {hyp}\")\n    \n    spec = exp.get('spec', '')\n    if spec:\n        print(f\"  Spec: {spec}\")\n    \n    conclusion = exp.get('conclusion', '')\n    if conclusion:\n        print(f\"  Conclusion: {conclusion}\")\n    \n    metrics = exp.get('metrics', None)\n    if metrics:\n        print(f\"  Metrics:\")\n        if isinstance(metrics, dict):\n            print(json.dumps(metrics, indent=4, ensure_ascii=False))\n        else:\n            print(f\"    {metrics}\")\n    \n    print()\nPYEOF\n",
  "description": "Print all experiments with full details",
  "timeout": "30000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 << 'PYEOF'\nimport json\n\nwith open('/tmp/all_experiments.json', 'r') as f:\n    exps = json.load(f)\n\n# Process each experiment and output full details\nkeys = sorted(exps.keys())\n\nfor k in keys:\n    exp = exps[k]\n    print(f\"{'='*80}\")\n    print(f\"EXPERIMENT: {k}\")\n    print(f\"{'='*80}\")\n    print(f\"  Status: {exp.get('status', 'N/A')}\")\n    print(f\"  Created: {exp.get('created_at', 'N/A')}\")\n    print(f\"  Updated: {exp.get('updated_at', 'N/A')}\")\n    print(f\"  Completed: {exp.get('completed_at', 'N/A')}\")\n    print(f\"  Retry count: {exp.get('retry_count', 'N/A')}\")\n    \n    hyp = exp.get('hypothesis', '')\n    if hyp:\n        print(f\"  Hypothesis: {hyp}\")\n    \n    spec = exp.get('spec', '')\n    if spec:\n        print(f\"  Spec: {spec}\")\n    \n    conclusion = exp.get('conclusion', '')\n    if conclusion:\n        print(f\"  Conclusion: {conclusion}\")\n    \n    metrics = exp.get('metrics', None)\n    if metrics:\n        print(f\"  Metrics:\")\n        if isinstance(metrics, dict):\n            print(json.dumps(metrics, indent=4, ensure_ascii=False))\n        else:\n            print(f\"    {metrics}\")\n    \n    print()\nPYEOF\n",
    "description": "Print all experiments with full details",
    "timeout": "30000"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-24T15:22:21.893879+00:00_

&lt;persisted-output>
Output too large (87KB). Full output saved to: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/66de9ef3-78db-4116-ae9e-2eba3b117097/tool-results/bz28qhcfp.txt

Preview (first 2KB):
================================================================================
EXPERIMENT: analysis_attention_heatmap
================================================================================
  Status: DONE
  Created: 2026-05-19T15:03:16.154Z
  Updated: 2026-05-19T15:22:24.770Z
  Completed: 2026-05-19T15:22:24.770Z
  Retry count: 0
  Hypothesis: 四模型（Base/TG/UG/LoRA-only）的 goal attention 衰减模式是否一致？如果 TG 的 attention decay 与 LoRA-only 无差异，则 gating 机制对 attention 分布零增量。
  Spec: {'command': 'attention heatmap analysis script', 'server': 'westd-20861', 'data_path': 'standard_conversations.json', 'data_count': 5, 'model_name': 'Qwen2.5-7B-Instruct', 'seed': 42, 'checkpoint_source': 'phase2_tg_s42_v7 + phase2_ug_s42 + phase2_lora_only_s42', 'eval_data': 'standard_conversations.json (5 convs x 10 turns)', 'checkpoint_path': 'N/A (analysis)', 'log_path': 'westd-20861:/root/turn_residual_gating/runs/analysis/'}
  Conclusion: success
  Metrics:
{
    "base_mean_goal_attn": 0.0136,
    "base_decay": 0.875,
    "tg_mean_goal_attn": 0.0232,
    "tg_decay": 0.777,
    "ug_mean_goal_attn": 0.0216,
    "ug_decay": 0.803,
    "lora_mean_goal_attn": 0.0216,
    "lora_decay": 0.81,
    "gating_incremental_benefit": "none"
}

================================================================================
EXPERIMENT: analysis_gradient_conflict
================================================================================
  Status: DONE
  Created: 2026-05-19T15:03:12.230Z
  Updated: 2026-05-19T15:22:23.782Z
  Completed: 2026-05-19T15:22:23.782Z
  Retry count: 0
  Hypothesis: NTP-GAR 梯度冲突在 v7 训练过程中是否逐层普遍存在？量化 cos_sim 和 magnitude ratio 的演化，验证 NTP 是否在训练中逐渐完全压制 GAR 信号。
...
&lt;/persisted-output>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-24T15:22:21.894026+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/66de9ef3-78db-4116-ae9e-2eba3b117097/tool-results/bz28qhcfp.txt",
  "limit": "300",
  "offset": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/66de9ef3-78db-4116-ae9e-2eba3b117097/tool-results/bz28qhcfp.txt",
    "limit": "300",
    "offset": "0"
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-24T15:22:21.894204+00:00_

0	================================================================================
1	EXPERIMENT: analysis_attention_heatmap
2	================================================================================
3	  Status: DONE
4	  Created: 2026-05-19T15:03:16.154Z
5	  Updated: 2026-05-19T15:22:24.770Z
6	  Completed: 2026-05-19T15:22:24.770Z
7	  Retry count: 0
8	  Hypothesis: 四模型（Base/TG/UG/LoRA-only）的 goal attention 衰减模式是否一致？如果 TG 的 attention decay 与 LoRA-only 无差异，则 gating 机制对 attention 分布零增量。
9	  Spec: {'command': 'attention heatmap analysis script', 'server': 'westd-20861', 'data_path': 'standard_conversations.json', 'data_count': 5, 'model_name': 'Qwen2.5-7B-Instruct', 'seed': 42, 'checkpoint_source': 'phase2_tg_s42_v7 + phase2_ug_s42 + phase2_lora_only_s42', 'eval_data': 'standard_conversations.json (5 convs x 10 turns)', 'checkpoint_path': 'N/A (analysis)', 'log_path': 'westd-20861:/root/turn_residual_gating/runs/analysis/'}
10	  Conclusion: success
11	  Metrics:
12	{
13	    "base_mean_goal_attn": 0.0136,
14	    "base_decay": 0.875,
15	    "tg_mean_goal_attn": 0.0232,
16	    "tg_decay": 0.777,
17	    "ug_mean_goal_attn": 0.0216,
18	    "ug_decay": 0.803,
19	    "lora_mean_goal_attn": 0.0216,
20	    "lora_decay": 0.81,
21	    "gating_incremental_benefit": "none"
22	}
23	
24	================================================================================
25	EXPERIMENT: analysis_gradient_conflict
26	================================================================================
27	  Status: DONE
28	  Created: 2026-05-19T15:03:12.230Z
29	  Updated: 2026-05-19T15:22:23.782Z
30	  Completed: 2026-05-19T15:22:23.782Z
31	  Retry count: 0
32	  Hypothesis: NTP-GAR 梯度冲突在 v7 训练过程中是否逐层普遍存在？量化 cos_sim 和 magnitude ratio 的演化，验证 NTP 是否在训练中逐渐完全压制 GAR 信号。
33	  Spec: {'command': 'gradient conflict analysis script', 'server': 'westd-20861', 'data_path': 'v7 epoch 0/1/2 checkpoints', 'data_count': 3, 'model_name': 'Qwen2.5-7B-Instruct', 'seed': 42, 'checkpoint_source': 'phase2_tg_s42_v
…[truncated 13156 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-24T15:22:21.894362+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/66de9ef3-78db-4116-ae9e-2eba3b117097/tool-results/bz28qhcfp.txt",
  "limit": "300",
  "offset": "300"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/66de9ef3-78db-4116-ae9e-2eba3b117097/tool-results/bz28qhcfp.txt",
    "limit": "300",
    "offset": "300"
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-24T15:22:21.894583+00:00_

300	        "tg_gar": 0.064,
301	        "ug_gar": 0.033,
302	        "lo_gar": 0.037,
303	        "pcgrad_gar": 0.03,
304	        "ss_gar": 0.347
305	    },
306	    "beta3": {
307	        "base_gar": 0.531,
308	        "tg_gar": 0.556,
309	        "ss_gar": 0.593
310	    },
311	    "beta5": {
312	        "base_gar": 0.704,
313	        "tg_gar": 0.727,
314	        "ss_gar": 0.717
315	    },
316	    "wilcoxon_beta0": {
317	        "tg_vs_base_p": "<0.001",
318	        "tg_vs_base_r": 0.802,
319	        "ss_vs_tg_p": "<0.001",
320	        "ss_vs_tg_r": 0.869
321	    },
322	    "ppl": {
323	        "base": 1.447,
324	        "tg": 1.432,
325	        "ss": 1.442
326	    },
327	    "n_convs": 39
328	}
329	
330	================================================================================
331	EXPERIMENT: d048_queue_runner
332	================================================================================
333	  Status: PREPARING
334	  Created: 2026-05-22T23:42:35.919Z
335	  Updated: 2026-05-22T23:42:39.048Z
336	  Completed: N/A
337	  Retry count: 0
338	  Conclusion: failed
339	
340	================================================================================
341	EXPERIMENT: d048_split_softmax_eval
342	================================================================================
343	  Status: DONE
344	  Created: 2026-05-23T07:47:05.556Z
345	  Updated: 2026-05-23T08:00:42.748Z
346	  Completed: 2026-05-23T07:53:10.326Z
347	  Retry count: 0
348	  Hypothesis: Split-softmax (Li et al., COLM 2024) post-softmax rescaling recovers AR GAR without the PPL cost of pre-softmax additive steering, providing an alternative inference-time intervention that separates attention allocation from logit distribution.
349	  Spec: {'command': 'python src/eval_split_softmax.py', 'server': 'westd-20861', 'data_path': 'data/eval_200/eval_200.json', 'data_count': 50, 'model_name': 'Qwen2.5-7B-Instruct + TG v7 LoRA', 'seed': 42, 'checkpoint_path': 'N/A (failed)', 'log_path': 'results/split_sof
…[truncated 16533 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-24T15:22:21.894739+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/66de9ef3-78db-4116-ae9e-2eba3b117097/tool-results/bz28qhcfp.txt",
  "limit": "300",
  "offset": "600"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/66de9ef3-78db-4116-ae9e-2eba3b117097/tool-results/bz28qhcfp.txt",
    "limit": "300",
    "offset": "600"
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-24T15:22:21.894924+00:00_

600	    "modelgen": {
601	        "gar_ours": 0.418,
602	        "gar_dongre": 0.441,
603	        "ppl": 1.389,
604	        "ntp_loss": 0.325,
605	        "n_conv": 5,
606	        "n_turns": 10
607	    },
608	    "gap_ratio": 1.2,
609	    "base_iid_ppl": 4.338,
610	    "base_modelgen_ppl": 1.351
611	}
612	
613	================================================================================
614	EXPERIMENT: instruction_retention_test
615	================================================================================
616	  Status: DONE
617	  Created: 2026-05-21T03:49:26.068Z
618	  Updated: 2026-05-21T03:59:31.835Z
619	  Completed: 2026-05-21T03:59:31.835Z
620	  Retry count: 0
621	  Hypothesis: Turn-level residual gating (β=3) preserves instruction-following ability across multi-turn conversations better than the baseline (β=0), because gating modulates residual contributions to retain earlier context signals rather than letting them decay through successive transformer layers.
622	  Spec: {'command': 'python src/eval_instruction_retention.py --checkpoint runs/phase2_tg_s42_v7 --prompts data/instruction_retention_prompts.json --betas 0 3 --seed 42 --output results/instruction_retention.json', 'server': 'westd-20861', 'data_path': 'data/instruction_retention_prompts.json', 'data_count': 18, 'model_name': 'Qwen2.5-7B-Instruct + v7 TG LoRA', 'seed': 42, 'checkpoint_source': 'phase2_tg_s42_v7', 'eval_data': '18 instruction retention prompts, beta=[0,3], 5 turns each'}
623	  Conclusion: success
624	  Metrics:
625	{
626	    "late_turn_rate_beta0": 0.759,
627	    "late_turn_rate_beta3": 0.87,
628	    "late_turn_delta": 0.111,
629	    "mcnemar_chi2": 3.125,
630	    "mcnemar_p": 0.0771,
631	    "gar_compliance_r": 0.2003,
632	    "gar_compliance_p": 0.007,
633	    "category_content_constraint": {
634	        "beta0": 0.619,
635	        "beta3": 0.857,
636	        "delta": 0.238
637	    },
638	    "category_count_constraint": {
639	        "beta0": 1,
640	        "beta3": 1,
641
…[truncated 11790 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-24T15:22:21.895084+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/66de9ef3-78db-4116-ae9e-2eba3b117097/tool-results/bz28qhcfp.txt",
  "limit": "300",
  "offset": "900"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/66de9ef3-78db-4116-ae9e-2eba3b117097/tool-results/bz28qhcfp.txt",
    "limit": "300",
    "offset": "900"
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-24T15:22:21.895279+00:00_

900	  Retry count: 0
901	  Hypothesis: ThreadGate's per-layer gating and auxiliary GAR loss do not degrade the model's general language understanding capabilities. All fine-tuned variants (TG/UG/LO/PCGrad/SS) should maintain MMLU 5-shot accuracy within 1pp of the Base LoRA-only checkpoint, confirming that attention steering is additive rather than destructive.
902	  Spec: {'command': 'python eval_mmlu.py --model_path &lt;checkpoint> --n_shot 5', 'server': 'westd-20861', 'data_path': 'MMLU benchmark (5-shot)', 'data_count': 14042, 'model_name': 'Qwen/Qwen2.5-7B-Instruct', 'seed': 42, 'checkpoint_source': 'base/lo/ug/tg/pcgrad/ss checkpoints', 'eval_data': 'MMLU 5-shot', 'checkpoint_path': 'results/mmlu/', 'log_path': 'logs/gpu_chain_next.log'}
903	  Conclusion: success
904	  Metrics:
905	{
906	    "base_qwen": 0.7423,
907	    "pcgrad_v9_s42": 0.7386,
908	    "ss_v8b_s42": 0.7375,
909	    "lo_s42": 0.7357,
910	    "tg_v7_s42": 0.7347,
911	    "ug_s42": 0.7346
912	}
913	
914	================================================================================
915	EXPERIMENT: p0_ss_steering_eval
916	================================================================================
917	  Status: PREPARING
918	  Created: 2026-05-23T19:37:39.883Z
919	  Updated: 2026-05-23T19:57:38.851Z
920	  Completed: N/A
921	  Retry count: 0
922	  Hypothesis: SS training provides AR GAR ~0.385, steering alone gives 0.717. Combining SS checkpoint with beta-steering at inference may approach TF parity (~0.50), demonstrating that SS+steering is a constructive mitigation stack for the TF-AR gap.
923	  Conclusion: killed
924	
925	================================================================================
926	EXPERIMENT: p1_llama_ss_training
927	================================================================================
928	  Status: RUNNING
929	  Created: 2026-05-23T19:37:48.689Z
930	  Updated: 2026-05-24T07:21:06.008Z
931	  Completed: N/A
932	  Retry count: 0
933	  Hypothesis: SS is effectiv
…[truncated 17788 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-24T15:22:21.895466+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/66de9ef3-78db-4116-ae9e-2eba3b117097/tool-results/bz28qhcfp.txt",
  "limit": "300",
  "offset": "1200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/66de9ef3-78db-4116-ae9e-2eba3b117097/tool-results/bz28qhcfp.txt",
    "limit": "300",
    "offset": "1200"
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-24T15:22:21.895668+00:00_

1200	    "optimizer_steps": 500,
1201	    "gate_grad_received": true
1202	}
1203	
1204	================================================================================
1205	EXPERIMENT: phase2_tg_s42_v4
1206	================================================================================
1207	  Status: DONE
1208	  Created: 2026-05-18T14:58:00.124Z
1209	  Updated: 2026-05-18T16:50:36.202Z
1210	  Completed: 2026-05-18T16:50:33.778Z
1211	  Retry count: 0
1212	  Hypothesis: 重新平衡超参（λ=1.0 降 GAR 贡献至 ~50%，init_bias=1.5 使 sigmoid≈0.82 接近正常模型行为，gate_lr_multiplier=10 保持）能在 3-epoch 全量训练中产生有意义的 gate 分化（gate_std>0.05），同时 GAR 稳态在 0.1-0.5（非病态饱和），NTP loss 正常收敛，总 loss 保持正值
1213	  Spec: {'command': 'python src/train_phase2.py --gate-type threadgate --gar-loss-mode maximize --lambda-gar 1.0 --init-bias 1.5 --gate-lr-multiplier 10 --max-seq-len 2048 --seed 42 --output-dir /root/turn_residual_gating/runs/phase2_tg_s42_v4 --data-dir /root/turn_residual_gating/data/ultrachat_8k --epochs 3', 'server': 'westd-20861', 'gpu': 'cuda:0', 'pid': '36519', 'data_path': '/root/turn_residual_gating/data/ultrachat_8k', 'data_count': 8000, 'model_name': 'Qwen/Qwen2.5-7B-Instruct', 'seed': 42, 'checkpoint_path': '/root/turn_residual_gating/runs/phase2_tg_s42_v4', 'log_path': '/root/turn_residual_gating/runs/phase2_tg_s42_v4.log', 'checkpoint_source': 'from_scratch', 'eval_data': 'N/A'}
1214	  Conclusion: failed
1215	
1216	================================================================================
1217	EXPERIMENT: phase2_tg_s42_v5
1218	================================================================================
1219	  Status: DONE
1220	  Created: 2026-05-18T17:10:23.229Z
1221	  Updated: 2026-05-18T17:52:54.605Z
1222	  Completed: 2026-05-18T17:52:49.951Z
1223	  Retry count: 0
1224	  Hypothesis: 重新平衡超参（λ=1.0 降 GAR 贡献至 ~50%，init_bias=1.5 使 sigmoid≈0.82 接近正常模型行为，gate_lr_multiplier=10 保持）能在 3-epoch 全量训练中产生有意义的 gate 分化（gate_std>0.05），同时 GAR 稳态在 0.1-0.5（非病态饱和），NTP loss 正常收敛，总 loss 保持正值
1225	  Spec: {'co
…[truncated 20105 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-24T15:22:21.895825+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/66de9ef3-78db-4116-ae9e-2eba3b117097/tool-results/bz28qhcfp.txt",
  "limit": "300",
  "offset": "1500"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/66de9ef3-78db-4116-ae9e-2eba3b117097/tool-results/bz28qhcfp.txt",
    "limit": "300",
    "offset": "1500"
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-24T15:22:21.895975+00:00_

1500	    },
1501	    "lora_only": {
1502	        "tf_trc": 0.349,
1503	        "gen_trc": 0.4106,
1504	        "trc_gap": -0.0617,
1505	        "tf_tbp_ppl": 9.5,
1506	        "gen_tbp_ppl": 12
1507	    },
1508	    "base": {
1509	        "tf_trc": 0.1494,
1510	        "gen_trc": 0.1494,
1511	        "trc_gap": 0,
1512	        "tf_tbp_ppl": 2.05,
1513	        "gen_tbp_ppl": 2.05
1514	    }
1515	}
1516	
1517	================================================================================
1518	EXPERIMENT: v7_tg_s123
1519	================================================================================
1520	  Status: DONE
1521	  Created: 2026-05-21T15:16:39.923Z
1522	  Updated: 2026-05-21T21:17:16.499Z
1523	  Completed: 2026-05-21T21:17:16.499Z
1524	  Retry count: 0
1525	  Hypothesis: v7 TG s42 已验证 ThreadGate 有效性，s123 验证 seed robustness。预期 gate profile 和 GAR 收敛模式与 s42 一致。
1526	  Spec: {'command': 'bash scripts/launch_v7_tg_s123.sh', 'server': 'westd-20861', 'data_path': 'data/ultrachat_8k', 'data_count': 8000, 'model_name': 'Qwen2.5-7B-Instruct', 'seed': 123, 'pid': 245628, 'gpu_index': 0, 'checkpoint_path': '/root/turn_residual_gating/runs/phase2_tg_s123_v7', 'log_path': '/root/turn_residual_gating/logs/v7_tg_s123.log', 'checkpoint_source': 'N/A (from scratch)', 'eval_data': 'N/A'}
1527	  Conclusion: success
1528	  Metrics:
1529	{
1530	    "epoch_1": {
1531	        "avg_loss": 0.9447,
1532	        "avg_ntp_loss": 0.9434,
1533	        "avg_gar_loss": 0.0013,
1534	        "avg_div_loss": 0
1535	    },
1536	    "epoch_2": {
1537	        "avg_loss": 0.9315,
1538	        "avg_ntp_loss": 0.9305,
1539	        "avg_gar_loss": 0.001,
1540	        "avg_div_loss": 0
1541	    },
1542	    "final_gate": {
1543	        "mean": 0.9467,
1544	        "std": 0.051,
1545	        "min": 0.793,
1546	        "max": 1
1547	    },
1548	    "final_gate_profile": {
1549	        "L0": 0.883,
1550	        "L1": 0.793,
1551	        "L2": 0.996,
1552	        "L3": 0.988,
1553	        "L4": 0.984,
155
…[truncated 2005 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-24T15:22:21.896132+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nwith open('/tmp/all_experiments.json', 'r') as f:\n    exps = json.load(f)\n\n# Look for any experiment with per_turn data in metrics\nfor k, exp in sorted(exps.items()):\n    metrics = exp.get('metrics')\n    if not metrics or not isinstance(metrics, dict):\n        continue\n    metrics_str = json.dumps(metrics)\n    if 'per_turn' in metrics_str or 'turn_' in metrics_str or 'per-turn' in metrics_str:\n        print(f\"\\n{'='*60}\")\n        print(f\"EXPERIMENT: {k}\")\n        print(json.dumps(metrics, indent=2))\nPYEOF\n",
  "description": "Find all experiments with per-turn data"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 << 'PYEOF'\nimport json\n\nwith open('/tmp/all_experiments.json', 'r') as f:\n    exps = json.load(f)\n\n# Look for any experiment with per_turn data in metrics\nfor k, exp in sorted(exps.items()):\n    metrics = exp.get('metrics')\n    if not metrics or not isinstance(metrics, dict):\n        continue\n    metrics_str = json.dumps(metrics)\n    if 'per_turn' in metrics_str or 'turn_' in metrics_str or 'per-turn' in metrics_str:\n        print(f\"\\n{'='*60}\")\n        print(f\"EXPERIMENT: {k}\")\n        print(json.dumps(metrics, indent=2))\nPYEOF\n",
    "description": "Find all experiments with per-turn data"
  }
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-24T15:22:21.896279+00:00_

============================================================
EXPERIMENT: eval_llama_ar_n20
{
  "base": {
    "gar_ours_mean": 0.0088,
    "gar_ours_std": 0.0056,
    "gar_ours_median_per_conv": 0.0093,
    "gar_ours_median_per_turn_pool": 0.0071,
    "gar_ours_spike_ratio": "0%",
    "gar_dongre_mean": 0.0049,
    "gar_dongre_std": 0.0013,
    "gar_dongre_median": 0.0047,
    "ngar_ours_mid": 0.1019,
    "ngar_dongre_mid": 0.1171,
    "ppl": 1.293,
    "ppl_std": 0.07,
    "ntp_loss": 0.2552
  },
  "tg": {
    "gar_ours_mean": 0.0434,
    "gar_ours_std": 0.1002,
    "gar_ours_median_per_conv": 0.0179,
    "gar_ours_median_per_turn_pool": 0.0126,
    "gar_ours_spike_ratio": "5% (2/40 turns GAR>=0.4)",
    "gar_dongre_mean": 0.0183,
    "gar_dongre_std": 0.0198,
    "gar_dongre_median": 0.0152,
    "ngar_ours_mid": 0.5357,
    "ngar_dongre_mid": 0.4436,
    "ppl": 1.437,
    "ppl_std": 0.077,
    "ntp_loss": 0.3612
  },
  "lora_only": {
    "gar_ours_mean": 0.0284,
    "gar_ours_std": 0.0481,
    "gar_ours_median_per_conv": 0.0184,
    "gar_ours_median_per_turn_pool": 0.0133,
    "gar_ours_spike_ratio": "0%",
    "gar_dongre_mean": 0.0205,
    "gar_dongre_std": 0.0241,
    "gar_dongre_median": 0.016,
    "ngar_ours_mid": 0.3488,
    "ngar_dongre_mid": 0.4997,
    "ppl": 1.419,
    "ppl_std": 0.075,
    "ntp_loss": 0.3483
  },
  "n_conversations": 20,
  "n_turns": 4,
  "mid_turns_definition": "turns 3-T (0-indexed avg_gar[2:], excluding turns 1-2). All 16 eval entries use same definition.",
  "stat_pool": "median_per_conv: median of 20 per-conversation mid-turn averages. median_per_turn_pool: median of 40 individual turn values (20 conv x 2 mid turns).",
  "ranking_gar_ours_mean": "TG(0.0434) > LO(0.0284) > Base(0.0088)",
  "ranking_gar_ours_median_per_conv": "TG(0.0179) \u2248 LO(0.0184) > Base(0.0093)",
  "ranking_gar_ours_median_per_turn_pool": "TG(0.0126) \u2248 LO(0.0133) > Base(0.0071)",
  "ranking_gar_dongre": "LO(0.0205) > TG(0.0183) > Base(0.0049)",
  "note": 
…[truncated 1782 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-24T15:22:21.896468+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nwith open('/tmp/all_experiments.json', 'r') as f:\n    exps = json.load(f)\n\n# Get full d048_final_ar_eval metrics\nprint(\"=== d048_final_ar_eval FULL METRICS ===\")\nprint(json.dumps(exps['d048_final_ar_eval']['metrics'], indent=2))\n\nprint(\"\\n=== d048_eval_ss_s42 FULL METRICS ===\")\nprint(json.dumps(exps['d048_eval_ss_s42']['metrics'], indent=2))\n\nprint(\"\\n=== llama_ar_matched_eval FULL METRICS ===\")\nprint(json.dumps(exps['llama_ar_matched_eval']['metrics'], indent=2))\nPYEOF\n",
  "description": "Get full metrics for key experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 << 'PYEOF'\nimport json\n\nwith open('/tmp/all_experiments.json', 'r') as f:\n    exps = json.load(f)\n\n# Get full d048_final_ar_eval metrics\nprint(\"=== d048_final_ar_eval FULL METRICS ===\")\nprint(json.dumps(exps['d048_final_ar_eval']['metrics'], indent=2))\n\nprint(\"\\n=== d048_eval_ss_s42 FULL METRICS ===\")\nprint(json.dumps(exps['d048_eval_ss_s42']['metrics'], indent=2))\n\nprint(\"\\n=== llama_ar_matched_eval FULL METRICS ===\")\nprint(json.dumps(exps['llama_ar_matched_eval']['metrics'], indent=2))\nPYEOF\n",
    "description": "Get full metrics for key experiments"
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-24T15:22:21.896635+00:00_

=== d048_final_ar_eval FULL METRICS ===
{
  "beta0": {
    "base_gar": 0.019,
    "tg_gar": 0.064,
    "ug_gar": 0.033,
    "lo_gar": 0.037,
    "pcgrad_gar": 0.03,
    "ss_gar": 0.347
  },
  "beta3": {
    "base_gar": 0.531,
    "tg_gar": 0.556,
    "ss_gar": 0.593
  },
  "beta5": {
    "base_gar": 0.704,
    "tg_gar": 0.727,
    "ss_gar": 0.717
  },
  "wilcoxon_beta0": {
    "tg_vs_base_p": "<0.001",
    "tg_vs_base_r": 0.802,
    "ss_vs_tg_p": "<0.001",
    "ss_vs_tg_r": 0.869
  },
  "ppl": {
    "base": 1.447,
    "tg": 1.432,
    "ss": 1.442
  },
  "n_convs": 39
}

=== d048_eval_ss_s42 FULL METRICS ===
{
  "tf": {
    "base_gar_ours_mid": 0.0128,
    "base_gar_dongre_mid": 0.0031,
    "base_ppl": 4.34,
    "base_ntp": 1.4,
    "tg_gar_ours_mid": 0.5025,
    "tg_gar_dongre_mid": 0.389,
    "tg_ppl": 2.78,
    "tg_ntp": 0.98,
    "baseline_mid_gar": 0.0122
  },
  "ar": {
    "gar_ours_mid": 0.3887,
    "gar_ours_ci_95": [
      0.3692,
      0.3934
    ],
    "ppl": 1.35
  },
  "gap_ratio": 1.29,
  "n_conversations_tf": 50,
  "n_conversations_ar": 5,
  "bootstrap_turns": "curve[2:] (turns 3-T)",
  "note": "AR used hardcoded N=5, not N=50. Will be re-evaluated in final unified batch with eval_200.json N=50."
}

=== llama_ar_matched_eval FULL METRICS ===
{
  "ar_base_ours": {
    "mid_gar": 0.0082,
    "ngar": 0.1,
    "ppl": 1.267
  },
  "ar_tg_ours": {
    "mid_gar": 0.0388,
    "ngar": 0.493,
    "ppl": 1.413
  },
  "ar_base_dongre": {
    "mid_gar": 0.0051,
    "ngar": 0.12,
    "ppl": 1.267
  },
  "ar_tg_dongre": {
    "mid_gar": 0.018,
    "ngar": 0.431,
    "ppl": 1.413
  },
  "tf_reference": {
    "tf_tg_ours_ngar": 11.88,
    "tf_base_ours_ngar": 0.388,
    "tf_tg_ours_raw": 0.4836,
    "tf_tg_dongre_raw": 0.018
  },
  "matched_gap_analysis": {
    "gar_ours_raw_gap": "12.5x (TF 0.484 / AR 0.039)",
    "gar_ours_ngar_gap": "24.1x (TF 11.88 / AR 0.493)",
    "gar_dongre_raw_gap": "1.002x (TF 0.018 / AR 0.018) \u2014 zero gap",
    "tg_over_base_ar_ours": "4
…[truncated 326 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-24T15:22:21.896939+00:00_

Here is the complete extraction of all 53 experiment entries from the registry.

---

## COMPLETE EXPERIMENT REGISTRY (53 entries)

---

### 1. analysis_attention_heatmap
- **Status:** DONE
- **Model:** Qwen2.5-7B-Instruct
- **Conditions:** Base / TG / UG / LoRA-only (4 models)
- **Conclusion:** success
- **Metrics:**
  - base_mean_goal_attn: 0.0136
  - base_decay: 0.875
  - tg_mean_goal_attn: 0.0232
  - tg_decay: 0.777
  - ug_mean_goal_attn: 0.0216
  - ug_decay: 0.803
  - lora_mean_goal_attn: 0.0216
  - lora_decay: 0.81
  - gating_incremental_benefit: "none"

---

### 2. analysis_gradient_conflict
- **Status:** DONE
- **Model:** Qwen2.5-7B-Instruct
- **Condition:** TG v7 (gradient analysis)
- **Conclusion:** success
- **Metrics:**
  - epoch0_cos_sim: -0.089
  - epoch1_cos_sim: -0.054
  - epoch2_cos_sim: -0.042
  - epoch0_neg_layers_pct: 78.6
  - epoch1_neg_layers_pct: 71.4
  - epoch2_neg_layers_pct: 67.9
  - epoch0_mag_ratio: 7.5
  - epoch1_mag_ratio: 13.7
  - epoch2_mag_ratio: 14.7

---

### 3. attention_steering_eval200_tf
- **Status:** DONE
- **Model:** Qwen2.5-7B-Instruct + TG v7 LoRA
- **Condition:** TG (steering eval, TF mode)
- **Conclusion:** success
- **Metrics (N=200, mode=tf):**
  - beta_0.0: mid_gar=0.5353, ppl=2.62
  - beta_2.0: mid_gar=0.6112, ppl=2.69
  - beta_3.0: mid_gar=0.788, ppl=2.93
  - beta_4.0: mid_gar=0.8165, ppl=3.49
  - beta_5.0: mid_gar=0.8325, ppl=6.15
  - beta_10.0: mid_gar=0.977, ppl=505.21

---

### 4. attention_steering_gen_n50
- **Status:** DONE
- **Model:** Qwen2.5-7B-Instruct + TG v7 LoRA
- **Condition:** TG (steering eval, gen mode, N=50)
- **Conclusion:** success
- **Metrics (per-conv mid_gar turns 2-7, >=3 turns only):**
  - beta_0.0: mid_gar=0.0641, mid_gar_std=0.0809, ppl=1.4324, ppl_std=0.1029, n_valid=39
  - beta_2.0: mid_gar=0.128, mid_gar_std=0.1101, ppl=1.4822, ppl_std=0.1385, n_valid=39
  - beta_3.0: mid_gar=0.5558, mid_gar_std=0.0601, ppl=1.5605, ppl_std=0.1719, n_valid=39
  - beta_4.0: mid_gar=0.6439, mid_gar_std=0.06
…[truncated 22431 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "Agent",
  "elapsed_ms": 5
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-24T15:22:21.897124+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-20861",
  "command": "find /root/turn_residual_gating/results/ -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-20861",
    "command": "find /root/turn_residual_gating/results/ -type f"
  }
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-24T15:22:21.897251+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-20861",
  "command": "find /root/turn_residual_gating/runs/ -type f -name \"*.json\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-20861",
    "command": "find /root/turn_residual_gating/runs/ -type f -name \"*.json\""
  }
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-24T15:22:21.897469+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/turn_residual_gating/results/phase1_run.log\\n/root/turn_residual_gating/results/phase1_gar_results.json\\n/root/turn_residual_gating/results/phase1_gar_curve.png\\n/root/turn_residual_gating/results/phase2_tg_s42_v7_dongre_gar.json\\n/root/turn_residual_gating/results/phase2_tg_s42_v7_dongre_gar_comparison.png\\n/root/turn_residual_gating/results/phase2_tg_s42_v7_gar.json\\n/root/turn_residual_gating/results/phase2_tg_s42_v7_gar_comparison.png\\n/root/turn_residual_gating/results/base_ultrachat_ours/base_model_gar.json\\n/root/turn_residual_gating/results/base_ultrachat_ours/base_model_gar_comparison.png\\n/root/turn_residual_gating/results/base_ultrachat_dongre/base_model_dongre_gar.json\\n/root/turn_residual_gating/results/base_ultrachat_dongre/base_model_dongre_gar_comparison.png\\n/root/turn_residual_gating/results/v7_training_dynamics.pdf\\n/root/turn_residual_gating/results/v7_training_dynamics.png\\n/root/turn_residual_gating/results/v7_training_dynamics_parsed.json\\n/root/turn_residual_gating/results/instruction_retention.log\\n/root/turn_residual_gating/results/instruction_retention.json\\n/root/turn_residual_gating/results/d048_ss_s42/tf_base_ours/base_model_gar.json\\n/root/turn_residual_gating/results/d048_ss_s42/tf_base_ours/base_model_gar_comparison.png\\n/root/turn_residual_gating/results/d048_ss_s42/tf_base_dongre/base_model_dongre_gar.json\\n/root/turn_residual_gating/results/d048_ss_s42/tf_base_dongre/base_model_dongre_gar_comparison.png\\n/root/turn_residual_gating/results/d048_ss_s42/tf_ss_ours/epoch_2_gar.json\\n/root/turn_residual_gating/results/d048_ss_s42/tf_ss_ours/epoch_2_gar_comparison.png\\n/root/turn_residual_gating/results/d048_ss_s42/tf_ss_dongre/epoch_2_dongre_gar.json\\n/root/turn_residual_gating/results/d048_ss_s42/tf_ss_dongre/epoch_2_dongre_gar_comparison.png\\n/root/turn_residual_gating/results/d048_ss_s42/ss_s42_ar_n50.json\\n/root/turn_residual_gating/results/d048_
…[truncated 6380 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-24T15:22:21.897715+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/turn_residual_gating/runs/phase2_tg_s42_v7/lora/adapter_config.json\\n/root/turn_residual_gating/runs/phase2_tg_s42_v7/train_config.json\\n/root/turn_residual_gating/runs/phase2_tg_s42_v7/epoch_0/lora/adapter_config.json\\n/root/turn_residual_gating/runs/phase2_tg_s42_v7/epoch_1/lora/adapter_config.json\\n/root/turn_residual_gating/runs/phase2_tg_s42_v7/epoch_2/lora/adapter_config.json\\n/root/turn_residual_gating/runs/phase2_ug_s42/epoch_0/lora/adapter_config.json\\n/root/turn_residual_gating/runs/phase2_ug_s42/epoch_1/lora/adapter_config.json\\n/root/turn_residual_gating/runs/phase2_ug_s42/epoch_2/lora/adapter_config.json\\n/root/turn_residual_gating/runs/phase2_ug_s42/lora/adapter_config.json\\n/root/turn_residual_gating/runs/phase2_ug_s42/train_config.json\\n/root/turn_residual_gating/runs/phase2_lora_only_s42/epoch_0/lora/adapter_config.json\\n/root/turn_residual_gating/runs/phase2_lora_only_s42/epoch_1/lora/adapter_config.json\\n/root/turn_residual_gating/runs/phase2_lora_only_s42/epoch_2/lora/adapter_config.json\\n/root/turn_residual_gating/runs/phase2_lora_only_s42/lora/adapter_config.json\\n/root/turn_residual_gating/runs/phase2_lora_only_s42/train_config.json\\n/root/turn_residual_gating/runs/4way_eval/base_ours/base_model_gar.json\\n/root/turn_residual_gating/runs/4way_eval/base_dongre/base_model_dongre_gar.json\\n/root/turn_residual_gating/runs/4way_eval/tg_v7_ours/phase2_tg_s42_v7_gar.json\\n/root/turn_residual_gating/runs/4way_eval/tg_v7_dongre/phase2_tg_s42_v7_dongre_gar.json\\n/root/turn_residual_gating/runs/4way_eval/ug_ours/phase2_ug_s42_gar.json\\n/root/turn_residual_gating/runs/4way_eval/ug_dongre/phase2_ug_s42_dongre_gar.json\\n/root/turn_residual_gating/runs/4way_eval/lora_only_ours/phase2_lora_only_s42_gar.json\\n/root/turn_residual_gating/runs/4way_eval/lora_only_dongre/phase2_lora_only_s42_dongre_gar.json\\n/root/turn_residual_gating/runs/analysis/gradient_conflict/epoch_0.json\\n
…[truncated 6397 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-24T15:22:21.897864+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-20861",
  "command": "find /root/turn_residual_gating/ -maxdepth 3 -name \"*per_turn*\" -o -name \"*perturn*\" -o -name \"*eval*results*\" -o -name \"*eval*detail*\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-20861",
    "command": "find /root/turn_residual_gating/ -maxdepth 3 -name \"*per_turn*\" -o -name \"*perturn*\" -o -name \"*eval*results*\" -o -name \"*eval*detail*\""
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-24T15:22:21.898001+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/turn_residual_gating/eval_results\\n/root/turn_residual_gating/artifacts/fig_ar_gar_perturn.pdf\\n/root/turn_residual_gating/artifacts/fig_ar_gar_perturn.png\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-24T15:22:21.898124+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper/palette.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper/palette.py"
  }
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-24T15:22:21.898271+00:00_

1	"""Unified color palette and style for all paper figures.
2	
3	All gen_*.py scripts should `from palette import *` to get consistent colors
4	and rcParams. Colors are muted/desaturated for academic print readability.
5	"""
6	import matplotlib
7	matplotlib.use('Agg')
8	import matplotlib.pyplot as plt
9	
10	# ── Training configuration colors (muted, print-safe) ──────────────
11	COLORS = {
12	    'Base':       '#8C9BAA',  # cool gray
13	    'ThreadGate': '#5B8DB8',  # steel blue
14	    'UG':         '#8DB87A',  # sage green
15	    'LoRA':       '#B8A05B',  # muted gold
16	    'PCGrad':     '#B87A8D',  # dusty rose
17	    'SS':         '#D4915E',  # warm terracotta
18	}
19	
20	# Short aliases for quick access
21	C_BASE = COLORS['Base']
22	C_TG   = COLORS['ThreadGate']
23	C_UG   = COLORS['UG']
24	C_LO   = COLORS['LoRA']
25	C_PC   = COLORS['PCGrad']
26	C_SS   = COLORS['SS']
27	
28	# ── Semantic colors ────────────────────────────────────────────────
29	C_TF   = '#6DAE8F'   # muted teal-green (teacher-forced)
30	C_AR   = '#C27C6E'   # muted coral (autoregressive)
31	C_GAR  = '#5B8DB8'   # steel blue (GAR metric lines)
32	C_PPL  = '#B87A8D'   # dusty rose (PPL metric lines)
33	C_SWEET = '#E8D08C'  # pale gold (sweet-spot bands)
34	C_GRAY  = '#AAAAAA'  # neutral gray (reference lines, annotations)
35	
36	# ── Ordered list for bar charts (matches Table 1 order) ───────────
37	CONFIG_ORDER = ['Base', 'ThreadGate', 'PCGrad', 'UG', 'LoRA', 'SS']
38	CONFIG_COLORS = [COLORS.get(c, C_GRAY) for c in CONFIG_ORDER]
39	
40	# ── Shared rcParams ────────────────────────────────────────────────
41	RCPARAMS = {
42	    'font.family': 'serif',
43	    'font.serif': ['Times New Roman', 'DejaVu Serif', 'Computer Modern Roman'],
44	    'font.size': 9,
45	    'axes.titlesize': 10,
46	    'axes.labelsize': 9,
47	    'xtick.labelsize': 8,
48	    'ytick.labelsize': 8,
49	    'legend.fontsize': 7,
50	    'figure.dpi': 300,
51	    'savefig.dpi': 300,
52	    'savefig.bbox': 'tight',
53	    'savefig.
…[truncated 874 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-24T15:22:21.898456+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-20861",
  "command": "cat /root/turn_residual_gating/results/phase1_gar_results.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-20861",
    "command": "cat /root/turn_residual_gating/results/phase1_gar_results.json"
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-24T15:22:21.898625+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"conversations\\\": [\\n    {\\n      \\\"topic\\\": \\\"knowledge_qa\\\",\\n      \\\"gar_per_turn\\\": [\\n        0.040823059132891186,\\n        0.04512010083902912,\\n        0.013130747741007228,\\n        0.00650711711070937,\\n        0.00794757837396706,\\n        0.010475027584462329,\\n        0.0064325632461295,\\n        0.0064851795851170796,\\n        0.024024183154450162,\\n        0.0063815157485804614\\n      ]\\n    },\\n    {\\n      \\\"topic\\\": \\\"coding_help\\\",\\n      \\\"gar_per_turn\\\": [\\n        0.03892792027962556,\\n        0.01614831786511439,\\n        0.016024100215931987,\\n        0.014265677803871479,\\n        0.022280560666057124,\\n        0.01175598411021427,\\n        0.011676755892946424,\\n        0.012119172134799114,\\n        0.028698462782805186,\\n        0.008366045388655046\\n      ]\\n    },\\n    {\\n      \\\"topic\\\": \\\"creative_writing\\\",\\n      \\\"gar_per_turn\\\": [\\n        0.04746097573743456,\\n        0.020994836998078137,\\n        0.013371459687846412,\\n        0.012031021184225008,\\n        0.00824935286124204,\\n        0.006609055943112286,\\n        0.007278364818926064,\\n        0.008613065262402981,\\n        0.012368155178571903,\\n        0.006464956196998698\\n      ]\\n    },\\n    {\\n      \\\"topic\\\": \\\"math_reasoning\\\",\\n      \\\"gar_per_turn\\\": [\\n        0.020220831225198112,\\n        0.012493554931635491,\\n        0.05157108256440534,\\n        0.011966003994578858,\\n        0.009293201282285727,\\n        0.004407146034458105,\\n        0.004833293033335719,\\n        0.005801134493939988,\\n        0.007469002720329692,\\n        0.0031505561100459655\\n      ]\\n    },\\n    {\\n      \\\"topic\\\": \\\"roleplay_advisor\\\",\\n      \\\"gar_per_turn\\\": [\\n        0.061599820166676346,\\n        0.025549100980817224,\\n        0.01781103121241768,\\n        0.02027419723749774,\\n       
…[truncated 799 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-24T15:22:21.898774+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-20861",
  "command": "head -200 /root/turn_residual_gating/results/d048_final_ar/base_s42_ar_n50.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-20861",
    "command": "head -200 /root/turn_residual_gating/results/d048_final_ar/base_s42_ar_n50.json"
  }
}
```

</details>

---

### Tool result

_source line 62 · 2026-05-24T15:22:21.898960+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"checkpoint\\\": null,\\n  \\\"gate_type\\\": \\\"none\\\",\\n  \\\"mode\\\": \\\"gen\\\",\\n  \\\"gar_variant\\\": \\\"ours\\\",\\n  \\\"model\\\": \\\"/root/.cache/modelscope/Qwen/Qwen2___5-7B-Instruct\\\",\\n  \\\"layer_range\\\": null,\\n  \\\"betas\\\": [\\n    0.0,\\n    3.0,\\n    5.0\\n  ],\\n  \\\"conversations_source\\\": \\\"data/eval_200/eval_200.json\\\",\\n  \\\"num_conversations\\\": 50,\\n  \\\"results\\\": {\\n    \\\"beta_0.0\\\": {\\n      \\\"beta\\\": 0.0,\\n      \\\"avg_gar_per_turn\\\": [\\n        0.08532064071924929,\\n        0.03187063070352226,\\n        0.020567526746321296,\\n        0.012506871600959665,\\n        0.004174853863676706,\\n        0.004318260222758451,\\n        0.004705734498293591\\n      ],\\n      \\\"mid_turns_avg_gar\\\": 0.018589358379933436,\\n      \\\"mid_gar_std\\\": 0.01661494167192041,\\n      \\\"n_valid_convs\\\": 39,\\n      \\\"per_conv_mid_gar\\\": [\\n        0.02151872446946767,\\n        0.005462001460134907,\\n        0.020531191708689542,\\n        0.014310994064923997,\\n        0.011777950654253664,\\n        0.019790080063389677,\\n        0.006636974781914053,\\n        0.015805251933059854,\\n        0.00800401270853515,\\n        0.005910866188998604,\\n        0.020387817573091747,\\n        0.01261001310147913,\\n        0.0720659304134474,\\n        0.04244699355455799,\\n        0.03299872904930767,\\n        0.005416866400402752,\\n        0.004852595875474224,\\n        0.009857569627363737,\\n        0.005114683697916701,\\n        0.011127969175871968,\\n        0.004704539842036615,\\n        0.01935188932130659,\\n        0.007853152779792913,\\n        0.020172428133062092,\\n        0.019650743926046106,\\n        0.035518399055331086,\\n        0.004224496705838056,\\n        0.0071443208210847054,\\n        0.062543819254357,\\n        0.005393413739771811,\\n        0.04170803635370364,\\n        0.05832504584822
…[truncated 3689 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-24T15:22:21.899107+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-20861",
  "command": "head -200 /root/turn_residual_gating/results/d048_final_ar/tg_s42_ar_n50.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-20861",
    "command": "head -200 /root/turn_residual_gating/results/d048_final_ar/tg_s42_ar_n50.json"
  }
}
```

</details>

---

### Tool call

_source line 64 · 2026-05-24T15:22:21.899229+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-20861",
  "command": "head -200 /root/turn_residual_gating/results/d048_final_ar/ss_s42_ar_n50.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-20861",
    "command": "head -200 /root/turn_residual_gating/results/d048_final_ar/ss_s42_ar_n50.json"
  }
}
```

</details>

---

### Tool result

_source line 65 · 2026-05-24T15:22:21.899490+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"checkpoint\\\": \\\"runs/phase2_tg_s42_v7\\\",\\n  \\\"gate_type\\\": \\\"threadgate\\\",\\n  \\\"mode\\\": \\\"gen\\\",\\n  \\\"gar_variant\\\": \\\"ours\\\",\\n  \\\"model\\\": \\\"/root/.cache/modelscope/Qwen/Qwen2___5-7B-Instruct\\\",\\n  \\\"layer_range\\\": null,\\n  \\\"betas\\\": [\\n    0.0,\\n    3.0,\\n    5.0\\n  ],\\n  \\\"conversations_source\\\": \\\"data/eval_200/eval_200.json\\\",\\n  \\\"num_conversations\\\": 50,\\n  \\\"results\\\": {\\n    \\\"beta_0.0\\\": {\\n      \\\"beta\\\": 0.0,\\n      \\\"avg_gar_per_turn\\\": [\\n        0.12965867075423085,\\n        0.0724980225924143,\\n        0.059124380223817836,\\n        0.042786463493298295,\\n        0.06636781845906879,\\n        0.11924640631250193,\\n        0.1664832587649775\\n      ],\\n      \\\"mid_turns_avg_gar\\\": 0.06413940594217514,\\n      \\\"mid_gar_std\\\": 0.08094377598193611,\\n      \\\"n_valid_convs\\\": 39,\\n      \\\"per_conv_mid_gar\\\": [\\n        0.1484292164237747,\\n        0.1433119324170001,\\n        0.029021954689030363,\\n        0.020234718902669403,\\n        0.05665227802012508,\\n        0.03494042505057622,\\n        0.010515640719068766,\\n        0.013789526283694818,\\n        0.01937859042453569,\\n        0.09733931057857333,\\n        0.06687101492280581,\\n        0.019204233681491566,\\n        0.061998371184559774,\\n        0.053505507834334956,\\n        0.19626460163699355,\\n        0.006997127046156202,\\n        0.012002215509196836,\\n        0.012350239354030491,\\n        0.011383193933506393,\\n        0.030090706745606374,\\n        0.007970402786203456,\\n        0.0233275705595559,\\n        0.0083616596293498,\\n        0.02500994157885908,\\n        0.035626317657547944,\\n        0.3620072096432806,\\n        0.06470443029562907,\\n        0.1485753720234396,\\n        0.331703572771402,\\n        0.010605428656355904,\\n        0.07588446654717802,\\n        0.05
…[truncated 3674 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 66 · 2026-05-24T15:22:21.899688+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-20861",
  "command": "ls /root/turn_residual_gating/eval_results/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-20861",
    "command": "ls /root/turn_residual_gating/eval_results/"
  }
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-24T15:22:21.899887+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"checkpoint\\\": \\\"runs/d048_ss_s42\\\",\\n  \\\"gate_type\\\": \\\"threadgate\\\",\\n  \\\"mode\\\": \\\"gen\\\",\\n  \\\"gar_variant\\\": \\\"ours\\\",\\n  \\\"model\\\": \\\"/root/.cache/modelscope/Qwen/Qwen2___5-7B-Instruct\\\",\\n  \\\"layer_range\\\": null,\\n  \\\"betas\\\": [\\n    0.0,\\n    3.0,\\n    5.0\\n  ],\\n  \\\"conversations_source\\\": \\\"data/eval_200/eval_200.json\\\",\\n  \\\"num_conversations\\\": 50,\\n  \\\"results\\\": {\\n    \\\"beta_0.0\\\": {\\n      \\\"beta\\\": 0.0,\\n      \\\"avg_gar_per_turn\\\": [\\n        0.4580509937435908,\\n        0.381290044251582,\\n        0.3436189628899427,\\n        0.36994136818668016,\\n        0.36526660736803385,\\n        0.3540026795683949,\\n        0.3532090528383596\\n      ],\\n      \\\"mid_turns_avg_gar\\\": 0.34714045099005236,\\n      \\\"mid_gar_std\\\": 0.06257891565304426,\\n      \\\"n_valid_convs\\\": 39,\\n      \\\"per_conv_mid_gar\\\": [\\n        0.3771045137859715,\\n        0.3936877471011467,\\n        0.3674311296658531,\\n        0.411494313669766,\\n        0.32738839466915215,\\n        0.45495576036832647,\\n        0.385211273826582,\\n        0.36746203249042875,\\n        0.38286111549197777,\\n        0.4459412322390584,\\n        0.39233019914270983,\\n        0.32133861164459665,\\n        0.17303991045998426,\\n        0.364561860091223,\\n        0.38235127587468365,\\n        0.3688716409242864,\\n        0.21987802304756215,\\n        0.3676360411831814,\\n        0.3181866431062443,\\n        0.3913465195597191,\\n        0.173361026113684,\\n        0.38118290730150817,\\n        0.35090459476835745,\\n        0.1889550857481638,\\n        0.31798973713158996,\\n        0.3576668150736246,\\n        0.3335052405804485,\\n        0.3740010615811206,\\n        0.36642144555969003,\\n        0.3089067526993574,\\n        0.3389932598127423,\\n        0.36526442220290894,\\n        0.31840164926
…[truncated 3556 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-24T15:22:21.900042+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"v9_pcgrad\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.49}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-24T15:22:21.900197+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-20861",
  "command": "python3 -c \"\nimport json\nfiles = {\n    'base': '/root/turn_residual_gating/results/d048_final_ar/base_s42_ar_n50.json',\n    'tg': '/root/turn_residual_gating/results/d048_final_ar/tg_s42_ar_n50.json',\n    'ug': '/root/turn_residual_gating/results/d048_final_ar/ug_s42_ar_n50.json',\n    'lo': '/root/turn_residual_gating/results/d048_final_ar/lo_s42_ar_n50.json',\n    'pcgrad': '/root/turn_residual_gating/results/d048_final_ar/pcgrad_s42_ar_n50.json',\n    'ss': '/root/turn_residual_gating/results/d048_final_ar/ss_s42_ar_n50.json',\n}\nfor name, path in files.items():\n    with open(path) as f:\n        d = json.load(f)\n    r = d['results']['beta_0.0']\n    pt = r['avg_gar_per_turn']\n    print(f'{name}: per_turn={[round(x,4) for x in pt]}, mid_gar={r[\\\"mid_turns_avg_gar\\\"]:.4f}, ppl={r[\\\"avg_ppl\\\"]:.4f}, n_valid={r[\\\"n_valid_convs\\\"]}')\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-20861",
    "command": "python3 -c \"\nimport json\nfiles = {\n    'base': '/root/turn_residual_gating/results/d048_final_ar/base_s42_ar_n50.json',\n    'tg': '/root/turn_residual_gating/results/d048_final_ar/tg_s42_ar_n50.json',\n    'ug': '/root/turn_residual_gating/results/d048_final_ar/ug_s42_ar_n50.json',\n    'lo': '/root/turn_residual_gating/results/d048_final_ar/lo_s42_ar_n50.json',\n    'pcgrad': '/root/turn_residual_gating/results/d048_final_ar/pcgrad_s42_ar_n50.json',\n    'ss': '/root/turn_residual_gating/results/d048_final_ar/ss_s42_ar_n50.json',\n}\nfor name, path in files.items():\n    with open(path) as f:\n        d = json.load(f)\n    r = d['results']['beta_0.0']\n    pt = r['avg_gar_per_turn']\n    print(f'{name}: per_turn={[round(x,4) for x in pt]}, mid_gar={r[\\\"mid_turns_avg_gar\\\"]:.4f}, ppl={r[\\\"avg_ppl\\\"]:.4f}, n_valid={r[\\\"n_valid_convs\\\"]}')\n\"\n"
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-24T15:22:21.900338+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: python expression contains disallowed call 'open('. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 71 · 2026-05-24T15:22:21.900504+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-20861",
  "command": "python3 -c \"\nimport json\n# SS s123 and s456 AR per-turn\nfiles = {\n    'ss_s123': '/root/turn_residual_gating/results/d048_final_ar/ss_s123_ar_n50.json',\n    'ss_s456': '/root/turn_residual_gating/results/d048_final_ar/ss_s456_ar_n50.json',\n}\nfor name, path in files.items():\n    with open(path) as f:\n        d = json.load(f)\n    for bkey in ['beta_0.0', 'beta_3.0', 'beta_5.0']:\n        if bkey in d['results']:\n            r = d['results'][bkey]\n            pt = r['avg_gar_per_turn']\n            print(f'{name} {bkey}: per_turn={[round(x,4) for x in pt]}, mid_gar={r[\\\"mid_turns_avg_gar\\\"]:.4f}, ppl={r[\\\"avg_ppl\\\"]:.4f}')\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-20861",
    "command": "python3 -c \"\nimport json\n# SS s123 and s456 AR per-turn\nfiles = {\n    'ss_s123': '/root/turn_residual_gating/results/d048_final_ar/ss_s123_ar_n50.json',\n    'ss_s456': '/root/turn_residual_gating/results/d048_final_ar/ss_s456_ar_n50.json',\n}\nfor name, path in files.items():\n    with open(path) as f:\n        d = json.load(f)\n    for bkey in ['beta_0.0', 'beta_3.0', 'beta_5.0']:\n        if bkey in d['results']:\n            r = d['results'][bkey]\n            pt = r['avg_gar_per_turn']\n            print(f'{name} {bkey}: per_turn={[round(x,4) for x in pt]}, mid_gar={r[\\\"mid_turns_avg_gar\\\"]:.4f}, ppl={r[\\\"avg_ppl\\\"]:.4f}')\n\"\n"
  }
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-24T15:22:21.900647+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: python expression contains disallowed call 'open('. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 73 · 2026-05-24T15:22:21.900766+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-20861",
  "command": "python3 -c \"\nimport json\n# d048 summary with CI and Wilcoxon\nwith open('/root/turn_residual_gating/results/d048_final_ar/d048_summary_ci_wilcoxon.json') as f:\n    d = json.load(f)\nprint(json.dumps(d, indent=2))\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-20861",
    "command": "python3 -c \"\nimport json\n# d048 summary with CI and Wilcoxon\nwith open('/root/turn_residual_gating/results/d048_final_ar/d048_summary_ci_wilcoxon.json') as f:\n    d = json.load(f)\nprint(json.dumps(d, indent=2))\n\"\n"
  }
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-24T15:22:21.900887+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: python expression contains disallowed call 'open('. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-24T15:22:21.901007+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-20861",
  "command": "python3 -c \"\nimport json, os\n# Find Llama eval AR JSONs\nllama_dirs = [\n    '/root/turn_residual_gating/runs/eval_llama_ar_n20/',\n    '/root/turn_residual_gating/runs/eval_llama_tg_s42/',\n]\nfor d in llama_dirs:\n    if os.path.isdir(d):\n        for sub in sorted(os.listdir(d)):\n            full = os.path.join(d, sub)\n            if os.path.isdir(full):\n                for f in os.listdir(full):\n                    if f.endswith('.json'):\n                        fpath = os.path.join(full, f)\n                        with open(fpath) as fh:\n                            data = json.load(fh)\n                        if 'results' in data:\n                            for bk, bv in data['results'].items():\n                                if 'avg_gar_per_turn' in bv:\n                                    pt = bv['avg_gar_per_turn']\n                                    print(f'{sub}/{f} {bk}: per_turn={[round(x,4) for x in pt]}, mid_gar={bv.get(\\\"mid_turns_avg_gar\\\",0):.4f}')\n                        elif 'avg_gar_per_turn' in data:\n                            pt = data['avg_gar_per_turn']\n                            print(f'{sub}/{f}: per_turn={[round(x,4) for x in pt]}')\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-20861",
    "command": "python3 -c \"\nimport json, os\n# Find Llama eval AR JSONs\nllama_dirs = [\n    '/root/turn_residual_gating/runs/eval_llama_ar_n20/',\n    '/root/turn_residual_gating/runs/eval_llama_tg_s42/',\n]\nfor d in llama_dirs:\n    if os.path.isdir(d):\n        for sub in sorted(os.listdir(d)):\n            full = os.path.join(d, sub)\n            if os.path.isdir(full):\n                for f in os.listdir(full):\n                    if f.endswith('.json'):\n                        fpath = os.path.join(full, f)\n                        with open(fpath) as fh:\n                            data = json.load(fh)\n                        if 'results' in data:\n                            for bk, bv in data['results'].items():\n                                if 'avg_gar_per_turn' in bv:\n                                    pt = bv['avg_gar_per_turn']\n                                    print(f'{sub}/{f} {bk}: per_turn={[round(x,4) for x in pt]}, mid_gar={bv.get(\\\"mid_turns_avg_gar\\\",0):.4f}')\n                        elif 'avg_gar_per_turn' in data:\n                            pt = data['avg_gar_per_turn']\n                            print(f'{sub}/{f}: per_turn={[round(x,4) for x in pt]}')\n\"\n"
  }
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-24T15:22:21.901142+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: python expression contains disallowed call 'open('. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-24T15:22:21.901262+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-20861",
  "command": "python3 -c \"\nimport json\n# Read the Llama eval s42 AR results (TF and AR)\npaths = [\n    '/root/turn_residual_gating/runs/eval_llama_tg_s42/ar_base_ours/base_model_gar.json',\n    '/root/turn_residual_gating/runs/eval_llama_tg_s42/ar_tg_ours/epoch_2_gar.json',\n]\nfor p in paths:\n    try:\n        with open(p) as f:\n            d = json.load(f)\n        if 'results' in d:\n            for bk, bv in d['results'].items():\n                if 'avg_gar_per_turn' in bv:\n                    pt = bv['avg_gar_per_turn']\n                    print(f'{p.split(\\\"/\\\")[-2]} {bk}: per_turn={[round(x,4) for x in pt]}, mid_gar={bv.get(\\\"mid_turns_avg_gar\\\",\\\"N/A\\\")}')\n        elif 'avg_gar_per_turn' in d:\n            pt = d['avg_gar_per_turn']\n            print(f'{p.split(\\\"/\\\")[-2]}: per_turn={[round(x,4) for x in pt]}')\n        elif 'conversations' in d:\n            convs = d['conversations']\n            n_turns = max(len(c.get('gar_per_turn',[])) for c in convs)\n            avg = []\n            for t in range(n_turns):\n                vals = [c['gar_per_turn'][t] for c in convs if len(c['gar_per_turn']) > t]\n                avg.append(sum(vals)/len(vals))\n            print(f'{p.split(\\\"/\\\")[-2]}: per_turn={[round(x,4) for x in avg]}')\n    except Exception as e:\n        print(f'{p}: ERROR {e}')\n\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-20861",
    "command": "python3 -c \"\nimport json\n# Read the Llama eval s42 AR results (TF and AR)\npaths = [\n    '/root/turn_residual_gating/runs/eval_llama_tg_s42/ar_base_ours/base_model_gar.json',\n    '/root/turn_residual_gating/runs/eval_llama_tg_s42/ar_tg_ours/epoch_2_gar.json',\n]\nfor p in paths:\n    try:\n        with open(p) as f:\n            d = json.load(f)\n        if 'results' in d:\n            for bk, bv in d['results'].items():\n                if 'avg_gar_per_turn' in bv:\n                    pt = bv['avg_gar_per_turn']\n                    print(f'{p.split(\\\"/\\\")[-2]} {bk}: per_turn={[round(x,4) for x in pt]}, mid_gar={bv.get(\\\"mid_turns_avg_gar\\\",\\\"N/A\\\")}')\n        elif 'avg_gar_per_turn' in d:\n            pt = d['avg_gar_per_turn']\n            print(f'{p.split(\\\"/\\\")[-2]}: per_turn={[round(x,4) for x in pt]}')\n        elif 'conversations' in d:\n            convs = d['conversations']\n            n_turns = max(len(c.get('gar_per_turn',[])) for c in convs)\n            avg = []\n            for t in range(n_turns):\n                vals = [c['gar_per_turn'][t] for c in convs if len(c['gar_per_turn']) > t]\n                avg.append(sum(vals)/len(vals))\n            print(f'{p.split(\\\"/\\\")[-2]}: per_turn={[round(x,4) for x in avg]}')\n    except Exception as e:\n        print(f'{p}: ERROR {e}')\n\"\n"
  }
}
```

</details>

---

### Tool result

_source line 78 · 2026-05-24T15:22:21.901389+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '>' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 79 · 2026-05-24T15:22:21.901576+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-20861",
  "command": "grep -A 10 \"avg_gar_per_turn\" /root/turn_residual_gating/results/d048_final_ar/ug_s42_ar_n50.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-20861",
    "command": "grep -A 10 \"avg_gar_per_turn\" /root/turn_residual_gating/results/d048_final_ar/ug_s42_ar_n50.json"
  }
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-24T15:22:21.901724+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"      \\\"avg_gar_per_turn\\\": [\\n        0.1129921940992166,\\n        0.05642873320801699,\\n        0.03280072045206044,\\n        0.01977438701793716,\\n        0.0159779228630088,\\n        0.030121768434505834,\\n        0.11508936307240657\\n      ],\\n      \\\"mid_turns_avg_gar\\\": 0.03328704436352246,\\n      \\\"mid_gar_std\\\": 0.02966303801288318,\\n--\\n      \\\"avg_gar_per_turn\\\": [\\n        0.713236962625282,\\n        0.6162915409609446,\\n        0.5777931902597646,\\n        0.5473433620065906,\\n        0.466525845966605,\\n        0.49802315372436057,\\n        0.4692266668228177\\n      ],\\n      \\\"mid_turns_avg_gar\\\": 0.565097364834843,\\n      \\\"mid_gar_std\\\": 0.06918794737128443,\\n--\\n      \\\"avg_gar_per_turn\\\": [\\n        0.8434998986906099,\\n        0.7589580196678579,\\n        0.7209711042177204,\\n        0.6699347982173471,\\n        0.6176784006454414,\\n        0.6067509895964729,\\n        0.6374865605393496\\n      ],\\n      \\\"mid_turns_avg_gar\\\": 0.7082915161364267,\\n      \\\"mid_gar_std\\\": 0.05838455248938377,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 81 · 2026-05-24T15:22:21.901852+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-20861",
  "command": "grep -A 10 \"avg_gar_per_turn\" /root/turn_residual_gating/results/d048_final_ar/lo_s42_ar_n50.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-20861",
    "command": "grep -A 10 \"avg_gar_per_turn\" /root/turn_residual_gating/results/d048_final_ar/lo_s42_ar_n50.json"
  }
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-24T15:22:21.901987+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"      \\\"avg_gar_per_turn\\\": [\\n        0.10720668545992719,\\n        0.05864891317670235,\\n        0.030403609337427254,\\n        0.04893419515387564,\\n        0.039661538505343936,\\n        0.03167357926244056,\\n        0.18822649621780768\\n      ],\\n      \\\"mid_turns_avg_gar\\\": 0.03728114084399826,\\n      \\\"mid_gar_std\\\": 0.037359691165013656,\\n--\\n      \\\"avg_gar_per_turn\\\": [\\n        0.7056653229179559,\\n        0.6244302402944529,\\n        0.5650405310815467,\\n        0.5531423216289038,\\n        0.5596601667975662,\\n        0.4910874695000813,\\n        0.5201401503359073\\n      ],\\n      \\\"mid_turns_avg_gar\\\": 0.5600068778595667,\\n      \\\"mid_gar_std\\\": 0.06443437174740732,\\n--\\n      \\\"avg_gar_per_turn\\\": [\\n        0.828130261399882,\\n        0.7711820550542451,\\n        0.7129330542179312,\\n        0.7078449932755744,\\n        0.6242880608142771,\\n        0.5960454759724026,\\n        0.6419414467878956\\n      ],\\n      \\\"mid_turns_avg_gar\\\": 0.7081716440761184,\\n      \\\"mid_gar_std\\\": 0.06553602120120998,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 83 · 2026-05-24T15:22:21.902111+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-20861",
  "command": "grep -A 10 \"avg_gar_per_turn\" /root/turn_residual_gating/results/d048_final_ar/pcgrad_s42_ar_n50.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-20861",
    "command": "grep -A 10 \"avg_gar_per_turn\" /root/turn_residual_gating/results/d048_final_ar/pcgrad_s42_ar_n50.json"
  }
}
```

</details>

---

### Tool result

_source line 84 · 2026-05-24T15:22:21.902252+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"      \\\"avg_gar_per_turn\\\": [\\n        0.09031903934616116,\\n        0.038166620088667745,\\n        0.02762465355038688,\\n        0.029244892778051115,\\n        0.026701692468918035,\\n        0.008496557245544786,\\n        0.11269610105937317\\n      ],\\n      \\\"mid_turns_avg_gar\\\": 0.030063854299975972,\\n      \\\"mid_gar_std\\\": 0.023277123346328605,\\n--\\n      \\\"avg_gar_per_turn\\\": [\\n        0.7114149448258015,\\n        0.6162211958449166,\\n        0.5702409453030569,\\n        0.5326426561506948,\\n        0.5275893769053683,\\n        0.5340574232714813,\\n        0.5077509827961515\\n      ],\\n      \\\"mid_turns_avg_gar\\\": 0.5591845604107405,\\n      \\\"mid_gar_std\\\": 0.05217753427169539,\\n--\\n      \\\"avg_gar_per_turn\\\": [\\n        0.8420617043529646,\\n        0.7676606666482801,\\n        0.7133961783476483,\\n        0.6993200644162687,\\n        0.6468615313357309,\\n        0.5955249910913833,\\n        0.5896859871645472\\n      ],\\n      \\\"mid_turns_avg_gar\\\": 0.7082888585098569,\\n      \\\"mid_gar_std\\\": 0.05884515631857609,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 85 · 2026-05-24T15:22:21.902378+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-20861",
  "command": "cat /root/turn_residual_gating/results/d048_final_ar/d048_summary_ci_wilcoxon.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-20861",
    "command": "cat /root/turn_residual_gating/results/d048_final_ar/d048_summary_ci_wilcoxon.json"
  }
}
```

</details>

---

### Tool result

_source line 86 · 2026-05-24T15:22:21.902614+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"beta_0.0\\\": {\\n    \\\"base\\\": {\\n      \\\"mean\\\": 0.01859,\\n      \\\"std\\\": 0.01683,\\n      \\\"ci95_lower\\\": 0.01375,\\n      \\\"ci95_upper\\\": 0.02421,\\n      \\\"n\\\": 39\\n    },\\n    \\\"tg\\\": {\\n      \\\"mean\\\": 0.06414,\\n      \\\"std\\\": 0.082,\\n      \\\"ci95_lower\\\": 0.04118,\\n      \\\"ci95_upper\\\": 0.09118,\\n      \\\"n\\\": 39\\n    },\\n    \\\"ug\\\": {\\n      \\\"mean\\\": 0.03329,\\n      \\\"std\\\": 0.03005,\\n      \\\"ci95_lower\\\": 0.02476,\\n      \\\"ci95_upper\\\": 0.04336,\\n      \\\"n\\\": 39\\n    },\\n    \\\"lo\\\": {\\n      \\\"mean\\\": 0.03728,\\n      \\\"std\\\": 0.03785,\\n      \\\"ci95_lower\\\": 0.02688,\\n      \\\"ci95_upper\\\": 0.05004,\\n      \\\"n\\\": 39\\n    },\\n    \\\"pcgrad\\\": {\\n      \\\"mean\\\": 0.03006,\\n      \\\"std\\\": 0.02358,\\n      \\\"ci95_lower\\\": 0.02324,\\n      \\\"ci95_upper\\\": 0.03757,\\n      \\\"n\\\": 39\\n    },\\n    \\\"ss\\\": {\\n      \\\"mean\\\": 0.34714,\\n      \\\"std\\\": 0.0634,\\n      \\\"ci95_lower\\\": 0.32657,\\n      \\\"ci95_upper\\\": 0.36556,\\n      \\\"n\\\": 39\\n    },\\n    \\\"wilcoxon\\\": {\\n      \\\"TG vs Base\\\": {\\n        \\\"W\\\": 31.0,\\n        \\\"p\\\": 0.0,\\n        \\\"r\\\": 0.802,\\n        \\\"N\\\": 39\\n      },\\n      \\\"TG vs LO\\\": {\\n        \\\"W\\\": 187.0,\\n        \\\"p\\\": 0.003894,\\n        \\\"r\\\": 0.454,\\n        \\\"N\\\": 39\\n      },\\n      \\\"SS vs TG\\\": {\\n        \\\"W\\\": 1.0,\\n        \\\"p\\\": 0.0,\\n        \\\"r\\\": 0.869,\\n        \\\"N\\\": 39\\n      },\\n      \\\"PCGrad vs TG\\\": {\\n        \\\"W\\\": 176.0,\\n        \\\"p\\\": 0.002242,\\n        \\\"r\\\": 0.478,\\n        \\\"N\\\": 39\\n      }\\n    }\\n  },\\n  \\\"beta_3.0\\\": {\\n    \\\"base\\\": {\\n      \\\"mean\\\": 0.53147,\\n      \\\"std\\\": 0.05817,\\n      \\\"ci95_lower\\\": 0.51354,\\n      \\\"ci95_upper
…[truncated 3520 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 87 · 2026-05-24T15:22:21.902769+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-20861",
  "command": "grep -A 10 \"avg_gar_per_turn\" /root/turn_residual_gating/results/d048_final_ar/ss_s123_ar_n50.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-20861",
    "command": "grep -A 10 \"avg_gar_per_turn\" /root/turn_residual_gating/results/d048_final_ar/ss_s123_ar_n50.json"
  }
}
```

</details>

---

### Tool result

_source line 88 · 2026-05-24T15:22:21.902913+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"      \\\"avg_gar_per_turn\\\": [\\n        0.5264138429158041,\\n        0.44942589730574833,\\n        0.4380491601245241,\\n        0.3996410483602123,\\n        0.39093541482750455,\\n        0.3742847441196354,\\n        0.4173845983371479\\n      ],\\n      \\\"mid_turns_avg_gar\\\": 0.4231093029119521,\\n      \\\"mid_gar_std\\\": 0.06008549175404204,\\n--\\n      \\\"avg_gar_per_turn\\\": [\\n        0.7452750759206256,\\n        0.6465945712356048,\\n        0.60241030037771,\\n        0.5763798378563662,\\n        0.5373700330479982,\\n        0.5268594390260224,\\n        0.5404249443595182\\n      ],\\n      \\\"mid_turns_avg_gar\\\": 0.5903334893444743,\\n      \\\"mid_gar_std\\\": 0.048483194771033696,\\n--\\n      \\\"avg_gar_per_turn\\\": [\\n        0.8429188309356711,\\n        0.7772405371904584,\\n        0.7295762590989465,\\n        0.6932632376490165,\\n        0.6350596845698477,\\n        0.6319311139001059,\\n        0.6342764945228417\\n      ],\\n      \\\"mid_turns_avg_gar\\\": 0.7173915990785251,\\n      \\\"mid_gar_std\\\": 0.0600389323710394,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 89 · 2026-05-24T15:22:21.903041+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-20861",
  "command": "grep -A 10 \"avg_gar_per_turn\" /root/turn_residual_gating/results/d048_final_ar/ss_s456_ar_n50.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-20861",
    "command": "grep -A 10 \"avg_gar_per_turn\" /root/turn_residual_gating/results/d048_final_ar/ss_s456_ar_n50.json"
  }
}
```

</details>

---

### Tool result

_source line 90 · 2026-05-24T15:22:21.903177+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"      \\\"avg_gar_per_turn\\\": [\\n        0.5229538241096406,\\n        0.4496280043499529,\\n        0.4373763159556732,\\n        0.4244955678964128,\\n        0.4057397863906916,\\n        0.38713072501658835,\\n        0.4004353519340552\\n      ],\\n      \\\"mid_turns_avg_gar\\\": 0.4325354443660514,\\n      \\\"mid_gar_std\\\": 0.04345106797957016,\\n--\\n      \\\"avg_gar_per_turn\\\": [\\n        0.7376231436569146,\\n        0.6563999559390662,\\n        0.606771094510046,\\n        0.5908800440042065,\\n        0.5791575756491232,\\n        0.5538864128256161,\\n        0.4987799681556028\\n      ],\\n      \\\"mid_turns_avg_gar\\\": 0.6049934043810128,\\n      \\\"mid_gar_std\\\": 0.06217408775304026,\\n--\\n      \\\"avg_gar_per_turn\\\": [\\n        0.8459858156017315,\\n        0.7737101468531806,\\n        0.7341578019515627,\\n        0.6857227360884839,\\n        0.6399582935713684,\\n        0.600119042274427,\\n        0.6245279222389811\\n      ],\\n      \\\"mid_turns_avg_gar\\\": 0.715735942086655,\\n      \\\"mid_gar_std\\\": 0.06266249621783601,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 91 · 2026-05-24T15:22:21.903333+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-20861",
  "command": "grep -A 12 \"avg_gar_per_turn\" /root/turn_residual_gating/runs/eval_llama_ar_n20/ar_base_ours/base_model_gar.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-20861",
    "command": "grep -A 12 \"avg_gar_per_turn\" /root/turn_residual_gating/runs/eval_llama_ar_n20/ar_base_ours/base_model_gar.json"
  }
}
```

</details>

---

### Tool result

_source line 92 · 2026-05-24T15:22:21.903502+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  \\\"avg_gar_per_turn\\\": [\\n    0.02821098724113539,\\n    0.012756257112649097,\\n    0.009233074049263813,\\n    0.008380665237186235\\n  ],\\n  \\\"turn1_avg_gar\\\": 0.02821098724113539,\\n  \\\"mid_turns_avg_gar\\\": 0.008806869643225024,\\n  \\\"baseline_mid_turns_avg_gar\\\": 0.012190773994489113,\\n  \\\"gar_recovery_pp\\\": -0.33839043512640893,\\n  \\\"normalized_gar_curves\\\": [\\n    [\\n      0.03769278244736212,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 93 · 2026-05-24T15:22:21.903628+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-20861",
  "command": "grep -A 12 \"avg_gar_per_turn\" /root/turn_residual_gating/runs/eval_llama_ar_n20/ar_tg_ours/epoch_2_gar.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-20861",
    "command": "grep -A 12 \"avg_gar_per_turn\" /root/turn_residual_gating/runs/eval_llama_ar_n20/ar_tg_ours/epoch_2_gar.json"
  }
}
```

</details>

---

### Tool result

_source line 94 · 2026-05-24T15:22:21.903758+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  \\\"avg_gar_per_turn\\\": [\\n    0.040879680346123645,\\n    0.0415200722176479,\\n    0.048591561937671376,\\n    0.03825296861543176\\n  ],\\n  \\\"turn1_avg_gar\\\": 0.040879680346123645,\\n  \\\"mid_turns_avg_gar\\\": 0.04342226527655157,\\n  \\\"baseline_mid_turns_avg_gar\\\": 0.012190773994489113,\\n  \\\"gar_recovery_pp\\\": 3.123149128206246,\\n  \\\"normalized_gar_curves\\\": [\\n    [\\n      0.09048491347494056,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 95 · 2026-05-24T15:22:21.903878+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-20861",
  "command": "grep -A 12 \"avg_gar_per_turn\" /root/turn_residual_gating/runs/eval_llama_ar_n20/ar_lo_ours/epoch_2_gar.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-20861",
    "command": "grep -A 12 \"avg_gar_per_turn\" /root/turn_residual_gating/runs/eval_llama_ar_n20/ar_lo_ours/epoch_2_gar.json"
  }
}
```

</details>

---

### Tool result

_source line 96 · 2026-05-24T15:22:21.904018+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  \\\"avg_gar_per_turn\\\": [\\n    0.03319279019668941,\\n    0.049000257390739724,\\n    0.025408579449243428,\\n    0.03141111161519518\\n  ],\\n  \\\"turn1_avg_gar\\\": 0.03319279019668941,\\n  \\\"mid_turns_avg_gar\\\": 0.028409845532219303,\\n  \\\"baseline_mid_turns_avg_gar\\\": 0.012190773994489113,\\n  \\\"gar_recovery_pp\\\": 1.6219071537730188,\\n  \\\"normalized_gar_curves\\\": [\\n    [\\n      0.07555504916471935,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 97 · 2026-05-24T15:22:21.904138+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-20861",
  "command": "head -30 /root/turn_residual_gating/runs/eval_llama_tg_s42/ar_base_ours/base_model_gar.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-20861",
    "command": "head -30 /root/turn_residual_gating/runs/eval_llama_tg_s42/ar_base_ours/base_model_gar.json"
  }
}
```

</details>

---

### Tool result

_source line 98 · 2026-05-24T15:22:21.904271+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"checkpoint_dir\\\": null,\\n  \\\"gate_type\\\": \\\"none\\\",\\n  \\\"gar_variant\\\": \\\"ours\\\",\\n  \\\"model\\\": \\\"/root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-8B-Instruct/\\\",\\n  \\\"num_conversations\\\": 5,\\n  \\\"num_turns\\\": 10,\\n  \\\"gar_curves\\\": [\\n    [\\n      0.022829741401700687,\\n      0.022856911629837384,\\n      0.0109116397417921,\\n      0.012878099717179126,\\n      0.007275821290773976,\\n      0.00827552042169799,\\n      0.00788105012851048,\\n      0.005405014621539195,\\n      0.004417066631772937,\\n      0.009747381499018569\\n    ],\\n    [\\n      0.03709425011203393,\\n      0.019586500700313536,\\n      0.011785256108012732,\\n      0.004525442219005527,\\n      0.008711014297542619,\\n      0.0065743356271532605,\\n      0.004113195729061658,\\n      0.010557803207518646,\\n      0.007413797587713766,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 99 · 2026-05-24T15:22:21.904392+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-20861",
  "command": "head -30 /root/turn_residual_gating/runs/eval_llama_tg_s42/ar_tg_ours/epoch_2_gar.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-20861",
    "command": "head -30 /root/turn_residual_gating/runs/eval_llama_tg_s42/ar_tg_ours/epoch_2_gar.json"
  }
}
```

</details>

---

### Tool result

_source line 100 · 2026-05-24T15:22:21.904549+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"{\\n  \\\"checkpoint_dir\\\": \\\"runs/phase2_llama_tg_s42/epoch_2\\\",\\n  \\\"gate_type\\\": \\\"threadgate\\\",\\n  \\\"gar_variant\\\": \\\"ours\\\",\\n  \\\"model\\\": \\\"/root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-8B-Instruct/\\\",\\n  \\\"num_conversations\\\": 5,\\n  \\\"num_turns\\\": 10,\\n  \\\"gar_curves\\\": [\\n    [\\n      0.016532557375402046,\\n      0.014478198453813373,\\n      0.009493382984885557,\\n      0.012460561814088944,\\n      0.005526365842603909,\\n      0.011157180523235777,\\n      0.010897813521434152,\\n      0.012478780518390103,\\n      0.006761669222108524,\\n      0.017063198612406745\\n    ],\\n    [\\n      0.03099607452885067,\\n      0.013406564601133653,\\n      0.011707822118722788,\\n      0.011742936474684385,\\n      0.006589625652570152,\\n      0.011164489003725686,\\n      0.00723638039816521,\\n      0.0053677980747340245,\\n      0.09337122806906979,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 101 · 2026-05-24T15:22:21.904679+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-20861",
  "command": "find /root/turn_residual_gating/runs/eval_llama_lora_only_s42/ -name \"*.json\" -not -name \"adapter_config.json\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-20861",
    "command": "find /root/turn_residual_gating/runs/eval_llama_lora_only_s42/ -name \"*.json\" -not -name \"adapter_config.json\""
  }
}
```

</details>

---

### Tool result

_source line 102 · 2026-05-24T15:22:21.904804+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/turn_residual_gating/runs/eval_llama_lora_only_s42/tf_lo_ours/epoch_2_gar.json\\n/root/turn_residual_gating/runs/eval_llama_lora_only_s42/tf_lo_dongre/epoch_2_dongre_gar.json\\n/root/turn_residual_gating/runs/eval_llama_lora_only_s42/ar_lo_ours/epoch_2_gar.json\\n/root/turn_residual_gating/runs/eval_llama_lora_only_s42/ar_lo_dongre/epoch_2_dongre_gar.json\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 103 · 2026-05-24T15:22:21.904950+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-20861",
  "command": "grep \"avg_gar_per_turn\" /root/turn_residual_gating/runs/eval_llama_tg_s42/ar_base_ours/base_model_gar.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-20861",
    "command": "grep \"avg_gar_per_turn\" /root/turn_residual_gating/runs/eval_llama_tg_s42/ar_base_ours/base_model_gar.json"
  }
}
```

</details>

---

### Tool result

_source line 104 · 2026-05-24T15:22:21.905073+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  \\\"avg_gar_per_turn\\\": [\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 105 · 2026-05-24T15:22:21.905187+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-20861",
  "command": "grep \"avg_gar_per_turn\" /root/turn_residual_gating/runs/eval_llama_tg_s42/ar_tg_ours/epoch_2_gar.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-20861",
    "command": "grep \"avg_gar_per_turn\" /root/turn_residual_gating/runs/eval_llama_tg_s42/ar_tg_ours/epoch_2_gar.json"
  }
}
```

</details>

---

### Tool result

_source line 106 · 2026-05-24T15:22:21.905306+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  \\\"avg_gar_per_turn\\\": [\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 107 · 2026-05-24T15:22:21.905433+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-20861",
  "command": "grep -A 12 \"avg_gar_per_turn\" /root/turn_residual_gating/runs/eval_llama_lora_only_s42/ar_lo_ours/epoch_2_gar.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-20861",
    "command": "grep -A 12 \"avg_gar_per_turn\" /root/turn_residual_gating/runs/eval_llama_lora_only_s42/ar_lo_ours/epoch_2_gar.json"
  }
}
```

</details>

---

### Tool result

_source line 108 · 2026-05-24T15:22:21.905566+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  \\\"avg_gar_per_turn\\\": [\\n    0.03219080998916755,\\n    0.16353317746177298,\\n    0.01217880837091928,\\n    0.10980873069789054,\\n    0.10617295318974262,\\n    0.09196924269936875,\\n    0.017715227122811684,\\n    0.03262907170206867,\\n    0.12366350864177948,\\n    0.015036948865533768\\n  ],\\n  \\\"turn1_avg_gar\\\": 0.03219080998916755,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 109 · 2026-05-24T15:22:21.905687+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-20861",
  "command": "find /root/turn_residual_gating/ -path \"*llama*matched*\" -type f"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-20861",
    "command": "find /root/turn_residual_gating/ -path \"*llama*matched*\" -type f"
  }
}
```

</details>

---

### Tool result

_source line 110 · 2026-05-24T15:22:21.905811+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"/root/turn_residual_gating/runs/eval_llama_ar_matched/ar_base_ours/base_model_gar.json\\n/root/turn_residual_gating/runs/eval_llama_ar_matched/ar_base_ours/base_model_gar_comparison.png\\n/root/turn_residual_gating/runs/eval_llama_ar_matched/ar_base_dongre/base_model_dongre_gar.json\\n/root/turn_residual_gating/runs/eval_llama_ar_matched/ar_base_dongre/base_model_dongre_gar_comparison.png\\n/root/turn_residual_gating/runs/eval_llama_ar_matched/ar_tg_ours/epoch_2_gar.json\\n/root/turn_residual_gating/runs/eval_llama_ar_matched/ar_tg_ours/epoch_2_gar_comparison.png\\n/root/turn_residual_gating/runs/eval_llama_ar_matched/ar_tg_dongre/epoch_2_dongre_gar.json\\n/root/turn_residual_gating/runs/eval_llama_ar_matched/ar_tg_dongre/epoch_2_dongre_gar_comparison.png\\n/root/turn_residual_gating/runs/eval_llama_ar_matched.log\\n/root/turn_residual_gating/scripts/eval_llama_ar_matched.sh\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 111 · 2026-05-24T15:22:21.905928+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-20861",
  "command": "grep -A 15 \"avg_gar_per_turn\" /root/turn_residual_gating/results/d048_ss_s42/ss_s42_ar_n50.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-20861",
    "command": "grep -A 15 \"avg_gar_per_turn\" /root/turn_residual_gating/results/d048_ss_s42/ss_s42_ar_n50.json"
  }
}
```

</details>

---

### Tool result

_source line 112 · 2026-05-24T15:22:21.906063+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"      \\\"avg_gar_per_turn\\\": [\\n        0.46922444705833594,\\n        0.423913661594305,\\n        0.4247670375548287,\\n        0.420179031009159,\\n        0.38353879713066885,\\n        0.37480020030312144,\\n        0.36095144949011015,\\n        0.3680056586875827,\\n        0.3717314579614993,\\n        0.36212795399626724\\n      ],\\n      \\\"mid_turns_avg_gar\\\": 0.38870702902924514,\\n      \\\"mid_gar_std\\\": 0.013542697105428221,\\n      \\\"n_valid_convs\\\": 5,\\n      \\\"per_conv_mid_gar\\\": [\\n--\\n      \\\"avg_gar_per_turn\\\": [\\n        0.6538752665007654,\\n        0.5841551666732833,\\n        0.5726011665260976,\\n        0.5571133544290384,\\n        0.5723151035811692,\\n        0.5241334527628541,\\n        0.5176171287686506,\\n        0.48060890972354475,\\n        0.5031442200874907,\\n        0.4606194470049562\\n      ],\\n      \\\"mid_turns_avg_gar\\\": 0.5373981859652257,\\n      \\\"mid_gar_std\\\": 0.01570300006977022,\\n      \\\"n_valid_convs\\\": 5,\\n      \\\"per_conv_mid_gar\\\": [\\n--\\n      \\\"avg_gar_per_turn\\\": [\\n        0.8311548947946334,\\n        0.7341679080172977,\\n        0.6800384723777374,\\n        0.6954495520969342,\\n        0.6618930152206197,\\n        0.6662683773473683,\\n        0.6677743815624279,\\n        0.6604372670768883,\\n        0.6656779530730014,\\n        0.6297131718507641\\n      ],\\n      \\\"mid_turns_avg_gar\\\": 0.6719768442803292,\\n      \\\"mid_gar_std\\\": 0.033085835192408056,\\n      \\\"n_valid_convs\\\": 5,\\n      \\\"per_conv_mid_gar\\\": [\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 113 · 2026-05-24T15:22:21.906216+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-20861",
  "command": "grep -A 12 \"avg_gar_per_turn\" /root/turn_residual_gating/runs/eval_llama_tg_s42/ar_base_ours/base_model_gar.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-20861",
    "command": "grep -A 12 \"avg_gar_per_turn\" /root/turn_residual_gating/runs/eval_llama_tg_s42/ar_base_ours/base_model_gar.json"
  }
}
```

</details>

---

### Tool result

_source line 114 · 2026-05-24T15:22:21.906344+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  \\\"avg_gar_per_turn\\\": [\\n    0.033750807160195184,\\n    0.018355685077266946,\\n    0.013503756558096172,\\n    0.009542696516370538,\\n    0.0071899068721576805,\\n    0.006004671267655836,\\n    0.008184710948527624,\\n    0.007114347331458859,\\n    0.006019207639993557,\\n    0.0055937114959584726\\n  ],\\n  \\\"turn1_avg_gar\\\": 0.033750807160195184,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 115 · 2026-05-24T15:22:21.906481+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-20861",
  "command": "grep -A 12 \"avg_gar_per_turn\" /root/turn_residual_gating/runs/eval_llama_tg_s42/ar_tg_ours/epoch_2_gar.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-20861",
    "command": "grep -A 12 \"avg_gar_per_turn\" /root/turn_residual_gating/runs/eval_llama_tg_s42/ar_tg_ours/epoch_2_gar.json"
  }
}
```

</details>

---

### Tool call

_source line 116 · 2026-05-24T15:22:21.906596+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-20861",
  "command": "grep -A 12 \"avg_gar_per_turn\" /root/turn_residual_gating/runs/eval_llama_ar_matched/ar_base_ours/base_model_gar.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-20861",
    "command": "grep -A 12 \"avg_gar_per_turn\" /root/turn_residual_gating/runs/eval_llama_ar_matched/ar_base_ours/base_model_gar.json"
  }
}
```

</details>

---

### Tool result

_source line 117 · 2026-05-24T15:22:21.906718+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  \\\"avg_gar_per_turn\\\": [\\n    0.03736731488660958,\\n    0.12537062515113845,\\n    0.010721998589616987,\\n    0.10885072045567827,\\n    0.021090979542329063,\\n    0.01673822824771879,\\n    0.014436359823685796,\\n    0.010770905750397318,\\n    0.026926028337013776,\\n    0.01320220404977335\\n  ],\\n  \\\"turn1_avg_gar\\\": 0.03736731488660958,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 118 · 2026-05-24T15:22:21.906832+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-20861",
  "command": "grep -A 12 \"avg_gar_per_turn\" /root/turn_residual_gating/runs/eval_llama_ar_matched/ar_tg_ours/epoch_2_gar.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-20861",
    "command": "grep -A 12 \"avg_gar_per_turn\" /root/turn_residual_gating/runs/eval_llama_ar_matched/ar_tg_ours/epoch_2_gar.json"
  }
}
```

</details>

---

### Tool call

_source line 119 · 2026-05-24T15:22:21.906949+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-20861",
  "command": "grep -B1 -A 3 \"ppl\\|avg_ppl\\|ntp\" /root/turn_residual_gating/runs/eval_llama_ar_n20/ar_base_ours/base_model_gar.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-20861",
    "command": "grep -B1 -A 3 \"ppl\\|avg_ppl\\|ntp\" /root/turn_residual_gating/runs/eval_llama_ar_n20/ar_base_ours/base_model_gar.json"
  }
}
```

</details>

---

### Tool result

_source line 120 · 2026-05-24T15:22:21.907073+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  \\\"avg_gar_per_turn\\\": [\\n    0.02960656286589364,\\n    0.013210328884524088,\\n    0.00856149193648884,\\n    0.007917162895947178\\n  ],\\n  \\\"turn1_avg_gar\\\": 0.02960656286589364,\\n  \\\"mid_turns_avg_gar\\\": 0.008239327416218009,\\n  \\\"baseline_mid_turns_avg_gar\\\": 0.012190773994489113,\\n  \\\"gar_recovery_pp\\\": -0.3951446578271104,\\n  \\\"normalized_gar_curves\\\": [\\n    [\\n      0.03769278244736212,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.53}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 121 · 2026-05-24T15:22:21.907187+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-20861",
  "command": "grep -B1 -A 3 \"ppl\\|avg_ppl\\|ntp\" /root/turn_residual_gating/runs/eval_llama_ar_n20/ar_tg_ours/epoch_2_gar.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-20861",
    "command": "grep -B1 -A 3 \"ppl\\|avg_ppl\\|ntp\" /root/turn_residual_gating/runs/eval_llama_ar_n20/ar_tg_ours/epoch_2_gar.json"
  }
}
```

</details>

---

### Tool result

_source line 122 · 2026-05-24T15:22:21.907309+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  \\\"avg_gar_per_turn\\\": [\\n    0.06118801896642151,\\n    0.035244458152933554,\\n    0.04903068174743987,\\n    0.028530789603949107\\n  ],\\n  \\\"turn1_avg_gar\\\": 0.06118801896642151,\\n  \\\"mid_turns_avg_gar\\\": 0.03878073567569449,\\n  \\\"baseline_mid_turns_avg_gar\\\": 0.012190773994489113,\\n  \\\"gar_recovery_pp\\\": 2.658996168120538,\\n  \\\"normalized_gar_curves\\\": [\\n    [\\n      0.09048491347494056,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.53}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 123 · 2026-05-24T15:22:21.907452+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 124 · 2026-05-24T15:22:21.907573+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 125 · 2026-05-24T15:22:21.907697+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-20861",
  "command": "grep \"avg_ppl\" /root/turn_residual_gating/runs/eval_llama_ar_n20/ar_base_ours/base_model_gar.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-20861",
    "command": "grep \"avg_ppl\" /root/turn_residual_gating/runs/eval_llama_ar_n20/ar_base_ours/base_model_gar.json"
  }
}
```

</details>

---

### Tool result

_source line 126 · 2026-05-24T15:22:21.907821+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  \\\"avg_ppl\\\": 1.292573344707489,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 127 · 2026-05-24T15:22:21.907936+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-20861",
  "command": "grep \"avg_ppl\" /root/turn_residual_gating/runs/eval_llama_ar_n20/ar_tg_ours/epoch_2_gar.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-20861",
    "command": "grep \"avg_ppl\" /root/turn_residual_gating/runs/eval_llama_ar_n20/ar_tg_ours/epoch_2_gar.json"
  }
}
```

</details>

---

### Tool result

_source line 128 · 2026-05-24T15:22:21.908052+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  \\\"avg_ppl\\\": 1.437078732252121,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 129 · 2026-05-24T15:22:21.908162+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-20861",
  "command": "grep \"avg_ppl\" /root/turn_residual_gating/runs/eval_llama_ar_n20/ar_lo_ours/epoch_2_gar.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-20861",
    "command": "grep \"avg_ppl\" /root/turn_residual_gating/runs/eval_llama_ar_n20/ar_lo_ours/epoch_2_gar.json"
  }
}
```

</details>

---

### Tool result

_source line 130 · 2026-05-24T15:22:21.908275+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  \\\"avg_ppl\\\": 1.4186152815818787,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 131 · 2026-05-24T15:22:21.908384+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-20861",
  "command": "grep \"avg_ppl\" /root/turn_residual_gating/runs/eval_llama_tg_s42/ar_base_ours/base_model_gar.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-20861",
    "command": "grep \"avg_ppl\" /root/turn_residual_gating/runs/eval_llama_tg_s42/ar_base_ours/base_model_gar.json"
  }
}
```

</details>

---

### Tool result

_source line 132 · 2026-05-24T15:22:21.908522+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  \\\"avg_ppl\\\": 1.2380386352539063,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 133 · 2026-05-24T15:22:21.908634+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-20861",
  "command": "grep \"avg_ppl\" /root/turn_residual_gating/runs/eval_llama_tg_s42/ar_tg_ours/epoch_2_gar.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-20861",
    "command": "grep \"avg_ppl\" /root/turn_residual_gating/runs/eval_llama_tg_s42/ar_tg_ours/epoch_2_gar.json"
  }
}
```

</details>

---

### Tool result

_source line 134 · 2026-05-24T15:22:21.908747+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  \\\"avg_ppl\\\": 1.3179033279418946,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.46}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 135 · 2026-05-24T15:22:21.908856+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-20861",
  "command": "grep \"avg_ppl\" /root/turn_residual_gating/runs/eval_llama_lora_only_s42/ar_lo_ours/epoch_2_gar.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-20861",
    "command": "grep \"avg_ppl\" /root/turn_residual_gating/runs/eval_llama_lora_only_s42/ar_lo_ours/epoch_2_gar.json"
  }
}
```

</details>

---

### Tool result

_source line 136 · 2026-05-24T15:22:21.908975+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  \\\"avg_ppl\\\": 1.323345685005188,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 137 · 2026-05-24T15:22:21.909136+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-20861",
  "command": "grep \"ppl\" /root/turn_residual_gating/results/d048_final_ar/tf_ss_s123_ours/epoch_2_gar.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-20861",
    "command": "grep \"ppl\" /root/turn_residual_gating/results/d048_final_ar/tf_ss_s123_ours/epoch_2_gar.json"
  }
}
```

</details>

---

### Tool call

_source line 138 · 2026-05-24T15:22:21.909251+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-20861",
  "command": "grep \"ppl\" /root/turn_residual_gating/results/d048_final_ar/tf_ss_s456_ours/epoch_2_gar.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-20861",
    "command": "grep \"ppl\" /root/turn_residual_gating/results/d048_final_ar/tf_ss_s456_ours/epoch_2_gar.json"
  }
}
```

</details>

---

### Tool result

_source line 139 · 2026-05-24T15:22:21.909369+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  \\\"avg_ppl\\\": 2.6122794687747954,\\n  \\\"ppl_per_conversation\\\": [\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 140 · 2026-05-24T15:22:21.909505+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  \\\"avg_ppl\\\": 2.611022992134094,\\n  \\\"ppl_per_conversation\\\": [\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.53}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 141 · 2026-05-24T15:22:21.909617+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-20861",
  "command": "grep \"ppl\" /root/turn_residual_gating/runs/eval_v7_tg_s123/tf_tg_ours/epoch_2_gar.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-20861",
    "command": "grep \"ppl\" /root/turn_residual_gating/runs/eval_v7_tg_s123/tf_tg_ours/epoch_2_gar.json"
  }
}
```

</details>

---

### Tool result

_source line 142 · 2026-05-24T15:22:21.909731+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  \\\"avg_ppl\\\": 2.7801873302459716,\\n  \\\"ppl_per_conversation\\\": [\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 143 · 2026-05-24T15:22:21.909840+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-20861",
  "command": "grep \"ppl\" /root/turn_residual_gating/runs/eval_v7_tg_s123/ar_tg_ours/epoch_2_gar.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-20861",
    "command": "grep \"ppl\" /root/turn_residual_gating/runs/eval_v7_tg_s123/ar_tg_ours/epoch_2_gar.json"
  }
}
```

</details>

---

### Tool result

_source line 144 · 2026-05-24T15:22:21.909954+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  \\\"avg_ppl\\\": 1.3855160236358643,\\n  \\\"ppl_per_conversation\\\": [\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 145 · 2026-05-24T15:22:21.910069+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-20861",
  "command": "grep -A 12 \"avg_gar_per_turn\" /root/turn_residual_gating/runs/eval_v7_tg_s123/ar_tg_ours/epoch_2_gar.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-20861",
    "command": "grep -A 12 \"avg_gar_per_turn\" /root/turn_residual_gating/runs/eval_v7_tg_s123/ar_tg_ours/epoch_2_gar.json"
  }
}
```

</details>

---

### Tool result

_source line 146 · 2026-05-24T15:22:21.910190+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  \\\"avg_gar_per_turn\\\": [\\n    0.052174890380692694,\\n    0.038546012863164766,\\n    0.01674060767764058,\\n    0.019998164421782358,\\n    0.01777699718036355,\\n    0.01825003657503057,\\n    0.012582027427246147,\\n    0.013868553311498439,\\n    0.007072638022578645,\\n    0.014545813839026145\\n  ],\\n  \\\"turn1_avg_gar\\\": 0.052174890380692694,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 147 · 2026-05-24T15:22:21.910302+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-20861",
  "command": "grep \"ppl\" /root/turn_residual_gating/results/d048_final_ar/ss_s123_ar_n50.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-20861",
    "command": "grep \"ppl\" /root/turn_residual_gating/results/d048_final_ar/ss_s123_ar_n50.json"
  }
}
```

</details>

---

### Tool result

_source line 148 · 2026-05-24T15:22:21.910436+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"      \\\"avg_ppl\\\": 1.4408082320581554,\\n      \\\"ppl_per_conversation\\\": [\\n      \\\"avg_ppl\\\": 1.6070499610621767,\\n      \\\"ppl_per_conversation\\\": [\\n      \\\"avg_ppl\\\": 1.7851763129156617,\\n      \\\"ppl_per_conversation\\\": [\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 149 · 2026-05-24T15:22:21.910573+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-20861",
  "command": "grep \"avg_ppl\" /root/turn_residual_gating/results/d048_final_ar/ss_s456_ar_n50.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-20861",
    "command": "grep \"avg_ppl\" /root/turn_residual_gating/results/d048_final_ar/ss_s456_ar_n50.json"
  }
}
```

</details>

---

### Tool result

_source line 150 · 2026-05-24T15:22:21.910691+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"      \\\"avg_ppl\\\": 1.4393913649836794,\\n      \\\"avg_ppl\\\": 1.5868394053170904,\\n      \\\"avg_ppl\\\": 1.8044637903511223,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 151 · 2026-05-24T15:22:21.910802+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-20861",
  "command": "grep \"avg_ppl\" /root/turn_residual_gating/results/d048_final_ar/ss_s42_ar_n50.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-20861",
    "command": "grep \"avg_ppl\" /root/turn_residual_gating/results/d048_final_ar/ss_s42_ar_n50.json"
  }
}
```

</details>

---

### Tool result

_source line 152 · 2026-05-24T15:22:21.910918+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"      \\\"avg_ppl\\\": 1.44233136084912,\\n      \\\"avg_ppl\\\": 1.5640138853724659,\\n      \\\"avg_ppl\\\": 1.7792246098615048,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 153 · 2026-05-24T15:22:21.911035+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-20861",
  "command": "grep \"ppl\" /root/turn_residual_gating/results/d048_ss_s42/tf_ss_ours/epoch_2_gar.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-20861",
    "command": "grep \"ppl\" /root/turn_residual_gating/results/d048_ss_s42/tf_ss_ours/epoch_2_gar.json"
  }
}
```

</details>

---

### Tool result

_source line 154 · 2026-05-24T15:22:21.911150+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  \\\"avg_ppl\\\": 2.780330593585968,\\n  \\\"ppl_per_conversation\\\": [\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 155 · 2026-05-24T15:22:21.911260+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-20861",
  "command": "grep \"ppl\" /root/turn_residual_gating/runs/eval_llama_tg_s42/tf_tg_ours/epoch_2_gar.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-20861",
    "command": "grep \"ppl\" /root/turn_residual_gating/runs/eval_llama_tg_s42/tf_tg_ours/epoch_2_gar.json"
  }
}
```

</details>

---

### Tool result

_source line 156 · 2026-05-24T15:22:21.911376+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  \\\"avg_ppl\\\": 2.5715965676307677,\\n  \\\"ppl_per_conversation\\\": [\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 157 · 2026-05-24T15:22:21.911521+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-20861",
  "command": "grep \"ppl\" /root/turn_residual_gating/runs/eval_llama_tg_s42/tf_base_ours/base_model_gar.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-20861",
    "command": "grep \"ppl\" /root/turn_residual_gating/runs/eval_llama_tg_s42/tf_base_ours/base_model_gar.json"
  }
}
```

</details>

---

### Tool result

_source line 158 · 2026-05-24T15:22:21.911637+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  \\\"avg_ppl\\\": 3.452100977897644,\\n  \\\"ppl_per_conversation\\\": [\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 159 · 2026-05-24T15:22:21.911746+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-20861",
  "command": "grep \"ppl\" /root/turn_residual_gating/runs/eval_llama_lora_only_s42/tf_lo_ours/epoch_2_gar.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-20861",
    "command": "grep \"ppl\" /root/turn_residual_gating/runs/eval_llama_lora_only_s42/tf_lo_ours/epoch_2_gar.json"
  }
}
```

</details>

---

### Tool result

_source line 160 · 2026-05-24T15:22:21.911860+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  \\\"avg_ppl\\\": 2.5964221954345703,\\n  \\\"ppl_per_conversation\\\": [\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 161 · 2026-05-24T15:22:21.912011+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-20861",
  "command": "grep \"mid_turns_avg_gar\" /root/turn_residual_gating/results/d048_final_ar/ss_s42_ar_n50.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-20861",
    "command": "grep \"mid_turns_avg_gar\" /root/turn_residual_gating/results/d048_final_ar/ss_s42_ar_n50.json"
  }
}
```

</details>

---

### Tool call

_source line 162 · 2026-05-24T15:22:21.912128+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-20861",
  "command": "grep \"mid_turns_avg_gar\" /root/turn_residual_gating/results/d048_final_ar/ss_s123_ar_n50.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-20861",
    "command": "grep \"mid_turns_avg_gar\" /root/turn_residual_gating/results/d048_final_ar/ss_s123_ar_n50.json"
  }
}
```

</details>

---

### Tool result

_source line 163 · 2026-05-24T15:22:21.912246+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"      \\\"mid_turns_avg_gar\\\": 0.34714045099005236,\\n      \\\"mid_turns_avg_gar\\\": 0.5933248609265496,\\n      \\\"mid_turns_avg_gar\\\": 0.7169711800492578,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.46}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 164 · 2026-05-24T15:22:21.912363+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"      \\\"mid_turns_avg_gar\\\": 0.4231093029119521,\\n      \\\"mid_turns_avg_gar\\\": 0.5903334893444743,\\n      \\\"mid_turns_avg_gar\\\": 0.7173915990785251,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.53}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 165 · 2026-05-24T15:22:21.912496+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-20861",
  "command": "grep \"mid_turns_avg_gar\" /root/turn_residual_gating/results/d048_final_ar/ss_s456_ar_n50.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-20861",
    "command": "grep \"mid_turns_avg_gar\" /root/turn_residual_gating/results/d048_final_ar/ss_s456_ar_n50.json"
  }
}
```

</details>

---

### Tool result

_source line 166 · 2026-05-24T15:22:21.912615+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"      \\\"mid_turns_avg_gar\\\": 0.4325354443660514,\\n      \\\"mid_turns_avg_gar\\\": 0.6049934043810128,\\n      \\\"mid_turns_avg_gar\\\": 0.715735942086655,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.46}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 167 · 2026-05-24T15:22:21.912727+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-20861",
  "command": "grep \"mid_turns_avg_gar\" /root/turn_residual_gating/results/d048_final_ar/base_s42_ar_n50.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-20861",
    "command": "grep \"mid_turns_avg_gar\" /root/turn_residual_gating/results/d048_final_ar/base_s42_ar_n50.json"
  }
}
```

</details>

---

### Tool result

_source line 168 · 2026-05-24T15:22:21.912842+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"      \\\"mid_turns_avg_gar\\\": 0.018589358379933436,\\n      \\\"mid_turns_avg_gar\\\": 0.5314724283823937,\\n      \\\"mid_turns_avg_gar\\\": 0.7042318561311054,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.47}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 169 · 2026-05-24T15:22:21.912953+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-20861",
  "command": "grep \"mid_turns_avg_gar\" /root/turn_residual_gating/results/d048_final_ar/tg_s42_ar_n50.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-20861",
    "command": "grep \"mid_turns_avg_gar\" /root/turn_residual_gating/results/d048_final_ar/tg_s42_ar_n50.json"
  }
}
```

</details>

---

### Tool result

_source line 170 · 2026-05-24T15:22:21.913074+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"      \\\"mid_turns_avg_gar\\\": 0.06413940594217514,\\n      \\\"mid_turns_avg_gar\\\": 0.5558482380266668,\\n      \\\"mid_turns_avg_gar\\\": 0.7270976822239251,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.46}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 171 · 2026-05-24T15:22:21.913188+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-20861",
  "command": "grep -A2 \"dongre\" /root/turn_residual_gating/results/d048_final_ar/tf_ss_s456_dongre/epoch_2_dongre_gar.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-20861",
    "command": "grep -A2 \"dongre\" /root/turn_residual_gating/results/d048_final_ar/tf_ss_s456_dongre/epoch_2_dongre_gar.json"
  }
}
```

</details>

---

### Tool result

_source line 172 · 2026-05-24T15:22:21.913306+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  \\\"gar_variant\\\": \\\"dongre\\\",\\n  \\\"model\\\": \\\"/root/.cache/modelscope/Qwen/Qwen2___5-7B-Instruct\\\",\\n  \\\"num_conversations\\\": 200,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.46}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 173 · 2026-05-24T15:22:21.913467+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-20861",
  "command": "grep \"num_conversations\\|num_turns\\|n_valid\" /root/turn_residual_gating/runs/eval_v7_tg_s123/ar_tg_ours/epoch_2_gar.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-20861",
    "command": "grep \"num_conversations\\|num_turns\\|n_valid\" /root/turn_residual_gating/runs/eval_v7_tg_s123/ar_tg_ours/epoch_2_gar.json"
  }
}
```

</details>

---

### Tool result

_source line 174 · 2026-05-24T15:22:21.913592+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 175 · 2026-05-24T15:22:21.913705+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-20861",
  "command": "grep \"num_conversations\\|n_valid\" /root/turn_residual_gating/results/d048_final_ar/tg_s42_ar_n50.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-20861",
    "command": "grep \"num_conversations\\|n_valid\" /root/turn_residual_gating/results/d048_final_ar/tg_s42_ar_n50.json"
  }
}
```

</details>

---

### Tool result

_source line 176 · 2026-05-24T15:22:21.913818+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 177 · 2026-05-24T15:22:21.913930+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-20861",
  "command": "grep \"gar_ours_mid\\|dongre_mid\\|avg_ppl\\|mid_turns_avg_gar\\|avg_gar\" /root/turn_residual_gating/runs/eval_v7_tg_s123/tf_tg_ours/epoch_2_gar.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-20861",
    "command": "grep \"gar_ours_mid\\|dongre_mid\\|avg_ppl\\|mid_turns_avg_gar\\|avg_gar\" /root/turn_residual_gating/runs/eval_v7_tg_s123/tf_tg_ours/epoch_2_gar.json"
  }
}
```

</details>

---

### Tool result

_source line 178 · 2026-05-24T15:22:21.914049+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 179 · 2026-05-24T15:22:21.914162+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-20861",
  "command": "grep \"gar_ours_mid\\|dongre_mid\\|avg_ppl\\|mid_turns_avg_gar\\|avg_gar\" /root/turn_residual_gating/runs/eval_v7_tg_s123/tf_tg_dongre/epoch_2_dongre_gar.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-20861",
    "command": "grep \"gar_ours_mid\\|dongre_mid\\|avg_ppl\\|mid_turns_avg_gar\\|avg_gar\" /root/turn_residual_gating/runs/eval_v7_tg_s123/tf_tg_dongre/epoch_2_dongre_gar.json"
  }
}
```

</details>

---

### Tool result

_source line 180 · 2026-05-24T15:22:21.914275+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 181 · 2026-05-24T15:22:21.914396+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-20861",
  "command": "grep -e \"num_conversations\" -e \"num_turns\" -e \"n_valid\" /root/turn_residual_gating/runs/eval_v7_tg_s123/ar_tg_ours/epoch_2_gar.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-20861",
    "command": "grep -e \"num_conversations\" -e \"num_turns\" -e \"n_valid\" /root/turn_residual_gating/runs/eval_v7_tg_s123/ar_tg_ours/epoch_2_gar.json"
  }
}
```

</details>

---

### Tool result

_source line 182 · 2026-05-24T15:22:21.914554+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  \\\"num_conversations\\\": 5,\\n  \\\"num_turns\\\": 10,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 183 · 2026-05-24T15:22:21.914708+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-20861",
  "command": "grep -e \"avg_gar\" -e \"avg_ppl\" /root/turn_residual_gating/runs/eval_v7_tg_s123/tf_tg_dongre/epoch_2_dongre_gar.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-20861",
    "command": "grep -e \"avg_gar\" -e \"avg_ppl\" /root/turn_residual_gating/runs/eval_v7_tg_s123/tf_tg_dongre/epoch_2_dongre_gar.json"
  }
}
```

</details>

---

### Tool result

_source line 184 · 2026-05-24T15:22:21.914835+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  \\\"avg_gar_per_turn\\\": [\\n  \\\"turn1_avg_gar\\\": 0.020640663703349986,\\n  \\\"mid_turns_avg_gar\\\": 0.011899102568554143,\\n  \\\"baseline_mid_turns_avg_gar\\\": 0.012190773994489113,\\n  \\\"avg_ppl\\\": 2.7801873302459716,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 185 · 2026-05-24T15:22:21.914950+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-20861",
  "command": "grep -e \"avg_gar\" -e \"avg_ppl\" /root/turn_residual_gating/runs/eval_v7_tg_s123/tf_tg_ours/epoch_2_gar.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-20861",
    "command": "grep -e \"avg_gar\" -e \"avg_ppl\" /root/turn_residual_gating/runs/eval_v7_tg_s123/tf_tg_ours/epoch_2_gar.json"
  }
}
```

</details>

---

### Tool result

_source line 186 · 2026-05-24T15:22:21.915070+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"  \\\"avg_gar_per_turn\\\": [\\n  \\\"turn1_avg_gar\\\": 0.5526979492085945,\\n  \\\"mid_turns_avg_gar\\\": 0.5051565280829672,\\n  \\\"baseline_mid_turns_avg_gar\\\": 0.012190773994489113,\\n  \\\"avg_ppl\\\": 2.7801873302459716,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.46}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 187 · 2026-05-24T15:22:21.915235+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-20861",
  "command": "grep \"avg_ppl\" /root/turn_residual_gating/results/d048_final_ar/lo_s42_ar_n50.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-20861",
    "command": "grep \"avg_ppl\" /root/turn_residual_gating/results/d048_final_ar/lo_s42_ar_n50.json"
  }
}
```

</details>

---

### Tool result

_source line 188 · 2026-05-24T15:22:21.915362+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"      \\\"avg_ppl\\\": 1.4310209504976652,\\n      \\\"avg_ppl\\\": 1.5927610392184588,\\n      \\\"avg_ppl\\\": 1.7561287102007441,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 189 · 2026-05-24T15:22:21.915514+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-20861",
  "command": "grep \"avg_ppl\" /root/turn_residual_gating/results/d048_final_ar/ug_s42_ar_n50.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-20861",
    "command": "grep \"avg_ppl\" /root/turn_residual_gating/results/d048_final_ar/ug_s42_ar_n50.json"
  }
}
```

</details>

---

### Tool result

_source line 190 · 2026-05-24T15:22:21.915635+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"      \\\"avg_ppl\\\": 1.433770403281702,\\n      \\\"avg_ppl\\\": 1.5722087838751904,\\n      \\\"avg_ppl\\\": 1.76724952746451,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 191 · 2026-05-24T15:22:21.915749+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-20861",
  "command": "grep \"avg_ppl\" /root/turn_residual_gating/results/d048_final_ar/pcgrad_s42_ar_n50.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-20861",
    "command": "grep \"avg_ppl\" /root/turn_residual_gating/results/d048_final_ar/pcgrad_s42_ar_n50.json"
  }
}
```

</details>

---

### Tool call

_source line 192 · 2026-05-24T15:22:21.915861+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "westd-20861",
  "command": "grep \"avg_ppl\" /root/turn_residual_gating/results/d048_final_ar/base_s42_ar_n50.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "westd-20861",
    "command": "grep \"avg_ppl\" /root/turn_residual_gating/results/d048_final_ar/base_s42_ar_n50.json"
  }
}
```

</details>

---

### Tool result

_source line 193 · 2026-05-24T15:22:21.915977+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"      \\\"avg_ppl\\\": 1.4486164993593271,\\n      \\\"avg_ppl\\\": 1.574561003265633,\\n      \\\"avg_ppl\\\": 1.8039957991991862,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 194 · 2026-05-24T15:22:21.916092+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"      \\\"avg_ppl\\\": 1.446807944810422,\\n      \\\"avg_ppl\\\": 1.5012319629048319,\\n      \\\"avg_ppl\\\": 1.9536419481336151,\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.53}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 195 · 2026-05-24T15:22:21.916266+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion",
  "description": "Create appendix_expansion output directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "Bash",
  "tool_args": {
    "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion",
    "description": "Create appendix_expansion output directory"
  }
}
```

</details>

---

### Tool result

_source line 196 · 2026-05-24T15:22:21.916388+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 197 · 2026-05-24T15:22:21.916548+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_perseed_ss.tex",
  "content": "% Per-seed detailed results for Scheduled Sampling (SS) — seeds 42, 123, 456\n% TF eval: N=200, T=3 (teacher-forced on held-out eval_200 set)\n% AR eval: N=50 gen-mode, beta=0/3/5 (from d048_final_ar)\n\\begin{table}[h]\n\\centering\n\\caption{Per-seed results for Scheduled Sampling (SS) on Qwen2.5-7B-Instruct.\nTF evaluation uses 200 held-out conversations; AR evaluation uses 50 model-generated conversations in free-form generation mode ($N_{\\text{valid}} \\approx 39$).}\n\\label{tab:perseed-ss}\n\\small\n\\begin{tabular}{@{}l ccc c@{}}\n\\toprule\n\\textbf{Metric} & \\textbf{Seed 42} & \\textbf{Seed 123} & \\textbf{Seed 456} & \\textbf{Mean $\\pm$ Std} \\\\\n\\midrule\n\\multicolumn{5}{@{}l}{\\textit{Teacher-Forced (TF)}} \\\\\n\\quad GAR-ours $\\uparrow$   & 0.502 & 0.554 & 0.496 & 0.517 $\\pm$ 0.032 \\\\\n\\quad GAR-Dongre $\\uparrow$ & 0.389 & 0.411 & 0.386 & 0.395 $\\pm$ 0.014 \\\\\n\\quad PPL $\\downarrow$       & 2.780 & 2.612 & 2.611 & 2.668 $\\pm$ 0.097 \\\\\n\\midrule\n\\multicolumn{5}{@{}l}{\\textit{Autoregressive (AR), $\\beta = 0$}} \\\\\n\\quad GAR-ours $\\uparrow$   & 0.347 & 0.423 & 0.433 & 0.401 $\\pm$ 0.047 \\\\\n\\quad PPL $\\downarrow$       & 1.442 & 1.441 & 1.439 & 1.441 $\\pm$ 0.002 \\\\\n\\midrule\n\\multicolumn{5}{@{}l}{\\textit{Autoregressive (AR), $\\beta = 3$}} \\\\\n\\quad GAR-ours $\\uparrow$   & 0.593 & 0.590 & 0.605 & 0.596 $\\pm$ 0.008 \\\\\n\\quad PPL $\\downarrow$       & 1.564 & 1.607 & 1.587 & 1.586 $\\pm$ 0.022 \\\\\n\\midrule\n\\multicolumn{5}{@{}l}{\\textit{Autoregressive (AR), $\\beta = 5$}} \\\\\n\\quad GAR-ours $\\uparrow$   & 0.717 & 0.717 & 0.716 & 0.717 $\\pm$ 0.001 \\\\\n\\quad PPL $\\downarrow$       & 1.779 & 1.785 & 1.804 & 1.789 $\\pm$ 0.013 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_perseed_ss.tex",
    "content": "% Per-seed detailed results for Scheduled Sampling (SS) — seeds 42, 123, 456\n% TF eval: N=200, T=3 (teacher-forced on held-out eval_200 set)\n% AR eval: N=50 gen-mode, beta=0/3/5 (from d048_final_ar)\n\\begin{table}[h]\n\\centering\n\\caption{Per-seed results for Scheduled Sampling (SS) on Qwen2.5-7B-Instruct.\nTF evaluation uses 200 held-out conversations; AR evaluation uses 50 model-generated conversations in free-form generation mode ($N_{\\text{valid}} \\approx 39$).}\n\\label{tab:perseed-ss}\n\\small\n\\begin{tabular}{@{}l ccc c@{}}\n\\toprule\n\\textbf{Metric} & \\textbf{Seed 42} & \\textbf{Seed 123} & \\textbf{Seed 456} & \\textbf{Mean $\\pm$ Std} \\\\\n\\midrule\n\\multicolumn{5}{@{}l}{\\textit{Teacher-Forced (TF)}} \\\\\n\\quad GAR-ours $\\uparrow$   & 0.502 & 0.554 & 0.496 & 0.517 $\\pm$ 0.032 \\\\\n\\quad GAR-Dongre $\\uparrow$ & 0.389 & 0.411 & 0.386 & 0.395 $\\pm$ 0.014 \\\\\n\\quad PPL $\\downarrow$       & 2.780 & 2.612 & 2.611 & 2.668 $\\pm$ 0.097 \\\\\n\\midrule\n\\multicolumn{5}{@{}l}{\\textit{Autoregressive (AR), $\\beta = 0$}} \\\\\n\\quad GAR-ours $\\uparrow$   & 0.347 & 0.423 & 0.433 & 0.401 $\\pm$ 0.047 \\\\\n\\quad PPL $\\downarrow$       & 1.442 & 1.441 & 1.439 & 1.441 $\\pm$ 0.002 \\\\\n\\midrule\n\\multicolumn{5}{@{}l}{\\textit{Autoregressive (AR), $\\beta = 3$}} \\\\\n\\quad GAR-ours $\\uparrow$   & 0.593 & 0.590 & 0.605 & 0.596 $\\pm$ 0.008 \\\\\n\\quad PPL $\\downarrow$       & 1.564 & 1.607 & 1.587 & 1.586 $\\pm$ 0.022 \\\\\n\\midrule\n\\multicolumn{5}{@{}l}{\\textit{Autoregressive (AR), $\\beta = 5$}} \\\\\n\\quad GAR-ours $\\uparrow$   & 0.717 & 0.717 & 0.716 & 0.717 $\\pm$ 0.001 \\\\\n\\quad PPL $\\downarrow$       & 1.779 & 1.785 & 1.804 & 1.789 $\\pm$ 0.013 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n"
  }
}
```

</details>

---

### Tool result

_source line 198 · 2026-05-24T15:22:21.916697+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_perseed_ss.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 199 · 2026-05-24T15:22:21.916821+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_perseed_tg.tex",
  "content": "% Per-seed detailed results for ThreadGate (TG) — seeds 42, 123\n% TF eval: N=200 held-out conversations\n% AR eval: N=5, T=10 model-generated conversations (original eval protocol)\n\\begin{table}[h]\n\\centering\n\\caption{Per-seed results for ThreadGate (TG) on Qwen2.5-7B-Instruct.\nTF evaluation uses 200 held-out conversations.\nAR evaluation uses 5 model-generated conversations with 10 turns each.}\n\\label{tab:perseed-tg}\n\\small\n\\begin{tabular}{@{}l cc c@{}}\n\\toprule\n\\textbf{Metric} & \\textbf{Seed 42} & \\textbf{Seed 123} & \\textbf{Mean $\\pm$ Std} \\\\\n\\midrule\n\\multicolumn{4}{@{}l}{\\textit{Teacher-Forced (TF)}} \\\\\n\\quad GAR-ours $\\uparrow$   & 0.504 & 0.505 & 0.504 $\\pm$ 0.001 \\\\\n\\quad GAR-Dongre $\\uparrow$ & 0.015 & 0.012 & 0.014 $\\pm$ 0.002 \\\\\n\\quad PPL $\\downarrow$       & 2.784 & 2.780 & 2.782 $\\pm$ 0.003 \\\\\n\\midrule\n\\multicolumn{4}{@{}l}{\\textit{Autoregressive (AR), $\\beta = 0$}} \\\\\n\\quad GAR-ours $\\uparrow$   & 0.016 & 0.017 & 0.016 $\\pm$ 0.001 \\\\\n\\quad GAR-Dongre $\\uparrow$ & 0.019 & 0.018 & 0.019 $\\pm$ 0.001 \\\\\n\\quad PPL $\\downarrow$       & 1.360 & 1.386 & 1.373 $\\pm$ 0.018 \\\\\n\\midrule\n\\multicolumn{4}{@{}l}{\\textit{Derived}} \\\\\n\\quad Gap ratio (TF/AR GAR-ours) $\\downarrow$ & 32.1 & 30.6 & 31.4 $\\pm$ 1.1 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_perseed_tg.tex",
    "content": "% Per-seed detailed results for ThreadGate (TG) — seeds 42, 123\n% TF eval: N=200 held-out conversations\n% AR eval: N=5, T=10 model-generated conversations (original eval protocol)\n\\begin{table}[h]\n\\centering\n\\caption{Per-seed results for ThreadGate (TG) on Qwen2.5-7B-Instruct.\nTF evaluation uses 200 held-out conversations.\nAR evaluation uses 5 model-generated conversations with 10 turns each.}\n\\label{tab:perseed-tg}\n\\small\n\\begin{tabular}{@{}l cc c@{}}\n\\toprule\n\\textbf{Metric} & \\textbf{Seed 42} & \\textbf{Seed 123} & \\textbf{Mean $\\pm$ Std} \\\\\n\\midrule\n\\multicolumn{4}{@{}l}{\\textit{Teacher-Forced (TF)}} \\\\\n\\quad GAR-ours $\\uparrow$   & 0.504 & 0.505 & 0.504 $\\pm$ 0.001 \\\\\n\\quad GAR-Dongre $\\uparrow$ & 0.015 & 0.012 & 0.014 $\\pm$ 0.002 \\\\\n\\quad PPL $\\downarrow$       & 2.784 & 2.780 & 2.782 $\\pm$ 0.003 \\\\\n\\midrule\n\\multicolumn{4}{@{}l}{\\textit{Autoregressive (AR), $\\beta = 0$}} \\\\\n\\quad GAR-ours $\\uparrow$   & 0.016 & 0.017 & 0.016 $\\pm$ 0.001 \\\\\n\\quad GAR-Dongre $\\uparrow$ & 0.019 & 0.018 & 0.019 $\\pm$ 0.001 \\\\\n\\quad PPL $\\downarrow$       & 1.360 & 1.386 & 1.373 $\\pm$ 0.018 \\\\\n\\midrule\n\\multicolumn{4}{@{}l}{\\textit{Derived}} \\\\\n\\quad Gap ratio (TF/AR GAR-ours) $\\downarrow$ & 32.1 & 30.6 & 31.4 $\\pm$ 1.1 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n"
  }
}
```

</details>

---

### Tool result

_source line 200 · 2026-05-24T15:22:21.916966+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_perseed_tg.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 201 · 2026-05-24T15:22:21.917090+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_perturn_qwen.tex",
  "content": "% Per-turn AR GAR-ours for Qwen2.5-7B-Instruct, 6-way comparison\n% Source: d048_final_ar, beta=0, N=50 gen-mode, n_valid~39\n% Only turns 1--5 shown (later turns have survivor bias from variable-length generation)\n\\begin{table}[h]\n\\centering\n\\caption{Per-turn autoregressive GAR-ours ($\\beta{=}0$) on Qwen2.5-7B-Instruct across six training configurations. Values represent average GAR over ${\\sim}39$ valid conversations in free-form generation mode.}\n\\label{tab:perturn-qwen}\n\\small\n\\begin{tabular}{@{}l ccccc@{}}\n\\toprule\n\\textbf{Configuration} & \\textbf{Turn 1} & \\textbf{Turn 2} & \\textbf{Turn 3} & \\textbf{Turn 4} & \\textbf{Turn 5} \\\\\n\\midrule\nBase         & .085 & .032 & .021 & .013 & .004 \\\\\nThreadGate   & .130 & .073 & .059 & .043 & .066 \\\\\nPCGrad       & .090 & .038 & .028 & .029 & .027 \\\\\nUG           & .113 & .056 & .033 & .020 & .016 \\\\\nLoRA-only    & .107 & .059 & .030 & .049 & .040 \\\\\nSS           & \\textbf{.458} & \\textbf{.381} & \\textbf{.344} & \\textbf{.370} & \\textbf{.365} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_perturn_qwen.tex",
    "content": "% Per-turn AR GAR-ours for Qwen2.5-7B-Instruct, 6-way comparison\n% Source: d048_final_ar, beta=0, N=50 gen-mode, n_valid~39\n% Only turns 1--5 shown (later turns have survivor bias from variable-length generation)\n\\begin{table}[h]\n\\centering\n\\caption{Per-turn autoregressive GAR-ours ($\\beta{=}0$) on Qwen2.5-7B-Instruct across six training configurations. Values represent average GAR over ${\\sim}39$ valid conversations in free-form generation mode.}\n\\label{tab:perturn-qwen}\n\\small\n\\begin{tabular}{@{}l ccccc@{}}\n\\toprule\n\\textbf{Configuration} & \\textbf{Turn 1} & \\textbf{Turn 2} & \\textbf{Turn 3} & \\textbf{Turn 4} & \\textbf{Turn 5} \\\\\n\\midrule\nBase         & .085 & .032 & .021 & .013 & .004 \\\\\nThreadGate   & .130 & .073 & .059 & .043 & .066 \\\\\nPCGrad       & .090 & .038 & .028 & .029 & .027 \\\\\nUG           & .113 & .056 & .033 & .020 & .016 \\\\\nLoRA-only    & .107 & .059 & .030 & .049 & .040 \\\\\nSS           & \\textbf{.458} & \\textbf{.381} & \\textbf{.344} & \\textbf{.370} & \\textbf{.365} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n"
  }
}
```

</details>

---

### Tool result

_source line 202 · 2026-05-24T15:22:21.917219+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_perturn_qwen.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 203 · 2026-05-24T15:22:21.917336+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_perturn_llama.tex",
  "content": "% Per-turn AR GAR-ours for Llama-3.1-8B-Instruct\n% Base: from llama_phase1_gar_diag (N=5, T=10)\n% TG: from eval_llama_tg_s42 (N=5, T=10)\n% LoRA-only: from eval_llama_lora_only_s42 (N=5, T=10)\n% Note: N=5 causes high variance in individual turns; aggregate trends are more reliable.\n\\begin{table}[h]\n\\centering\n\\caption{Per-turn autoregressive GAR-ours ($\\beta{=}0$) on Llama-3.1-8B-Instruct ($N{=}5$ conversations, $T{=}10$ turns). Individual turn values exhibit high variance due to limited sample size; the overall decay trend is the primary signal.}\n\\label{tab:perturn-llama}\n\\small\n\\begin{tabular}{@{}l cccccccccc@{}}\n\\toprule\n\\textbf{Config.} & \\textbf{T1} & \\textbf{T2} & \\textbf{T3} & \\textbf{T4} & \\textbf{T5} & \\textbf{T6} & \\textbf{T7} & \\textbf{T8} & \\textbf{T9} & \\textbf{T10} \\\\\n\\midrule\nBase      & .026 & .018 & .009 & .006 & .006 & .004 & .004 & .004 & .005 & .003 \\\\\nTG        & .034 & .018 & .014 & .010 & .007 & .006 & .008 & .007 & .006 & .006 \\\\\nLoRA-only & .032 & .164 & .012 & .110 & .106 & .092 & .018 & .033 & .124 & .015 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_perturn_llama.tex",
    "content": "% Per-turn AR GAR-ours for Llama-3.1-8B-Instruct\n% Base: from llama_phase1_gar_diag (N=5, T=10)\n% TG: from eval_llama_tg_s42 (N=5, T=10)\n% LoRA-only: from eval_llama_lora_only_s42 (N=5, T=10)\n% Note: N=5 causes high variance in individual turns; aggregate trends are more reliable.\n\\begin{table}[h]\n\\centering\n\\caption{Per-turn autoregressive GAR-ours ($\\beta{=}0$) on Llama-3.1-8B-Instruct ($N{=}5$ conversations, $T{=}10$ turns). Individual turn values exhibit high variance due to limited sample size; the overall decay trend is the primary signal.}\n\\label{tab:perturn-llama}\n\\small\n\\begin{tabular}{@{}l cccccccccc@{}}\n\\toprule\n\\textbf{Config.} & \\textbf{T1} & \\textbf{T2} & \\textbf{T3} & \\textbf{T4} & \\textbf{T5} & \\textbf{T6} & \\textbf{T7} & \\textbf{T8} & \\textbf{T9} & \\textbf{T10} \\\\\n\\midrule\nBase      & .026 & .018 & .009 & .006 & .006 & .004 & .004 & .004 & .005 & .003 \\\\\nTG        & .034 & .018 & .014 & .010 & .007 & .006 & .008 & .007 & .006 & .006 \\\\\nLoRA-only & .032 & .164 & .012 & .110 & .106 & .092 & .018 & .033 & .124 & .015 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n"
  }
}
```

</details>

---

### Tool result

_source line 204 · 2026-05-24T15:22:21.917489+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_perturn_llama.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 205 · 2026-05-24T15:22:21.917614+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_crossmodel_detail.tex",
  "content": "% Cross-model detailed comparison: Qwen2.5-7B-Instruct vs Llama-3.1-8B-Instruct\n% Conditions shared by both models: Base, ThreadGate, LoRA-only\n% Qwen TF: N=200 held-out; Qwen AR: d048_final_ar N=50 gen beta=0\n% Llama TF: N=50 held-out T=4; Llama AR: eval_llama_ar_n20 N=20 T=4\n\\begin{table}[h]\n\\centering\n\\caption{Cross-model comparison of goal-adherence metrics on Qwen2.5-7B-Instruct and Llama-3.1-8B-Instruct.\nGap ratio = TF GAR / AR GAR; lower is better (less exposure bias).\nQwen AR uses $N{=}50$ gen-mode evaluation; Llama AR uses $N{=}20$, $T{=}4$.}\n\\label{tab:crossmodel-detail}\n\\small\n\\begin{tabular}{@{}ll ccccc@{}}\n\\toprule\n\\textbf{Model} & \\textbf{Condition} & \\textbf{TF GAR}$\\uparrow$ & \\textbf{AR GAR}$\\uparrow$ & \\textbf{TF PPL}$\\downarrow$ & \\textbf{AR PPL}$\\downarrow$ & \\textbf{Gap}$\\downarrow$ \\\\\n\\midrule\n\\multirow{3}{*}{Qwen-7B}\n  & Base      & 0.013 & 0.019 & 4.34 & 1.447 & 0.7$\\times$ \\\\\n  & TG        & 0.504 & 0.064 & 2.78 & 1.432 & 7.9$\\times$ \\\\\n  & LoRA-only & 0.498 & 0.037 & 2.78 & 1.431 & 13.5$\\times$ \\\\\n\\midrule\n\\multirow{3}{*}{Llama-8B}\n  & Base      & 0.017 & 0.009 & 3.45 & 1.293 & 1.9$\\times$ \\\\\n  & TG        & 0.484 & 0.043 & 2.57 & 1.437 & 11.2$\\times$ \\\\\n  & LoRA-only & 0.481 & 0.028 & 2.60 & 1.419 & 17.2$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_crossmodel_detail.tex",
    "content": "% Cross-model detailed comparison: Qwen2.5-7B-Instruct vs Llama-3.1-8B-Instruct\n% Conditions shared by both models: Base, ThreadGate, LoRA-only\n% Qwen TF: N=200 held-out; Qwen AR: d048_final_ar N=50 gen beta=0\n% Llama TF: N=50 held-out T=4; Llama AR: eval_llama_ar_n20 N=20 T=4\n\\begin{table}[h]\n\\centering\n\\caption{Cross-model comparison of goal-adherence metrics on Qwen2.5-7B-Instruct and Llama-3.1-8B-Instruct.\nGap ratio = TF GAR / AR GAR; lower is better (less exposure bias).\nQwen AR uses $N{=}50$ gen-mode evaluation; Llama AR uses $N{=}20$, $T{=}4$.}\n\\label{tab:crossmodel-detail}\n\\small\n\\begin{tabular}{@{}ll ccccc@{}}\n\\toprule\n\\textbf{Model} & \\textbf{Condition} & \\textbf{TF GAR}$\\uparrow$ & \\textbf{AR GAR}$\\uparrow$ & \\textbf{TF PPL}$\\downarrow$ & \\textbf{AR PPL}$\\downarrow$ & \\textbf{Gap}$\\downarrow$ \\\\\n\\midrule\n\\multirow{3}{*}{Qwen-7B}\n  & Base      & 0.013 & 0.019 & 4.34 & 1.447 & 0.7$\\times$ \\\\\n  & TG        & 0.504 & 0.064 & 2.78 & 1.432 & 7.9$\\times$ \\\\\n  & LoRA-only & 0.498 & 0.037 & 2.78 & 1.431 & 13.5$\\times$ \\\\\n\\midrule\n\\multirow{3}{*}{Llama-8B}\n  & Base      & 0.017 & 0.009 & 3.45 & 1.293 & 1.9$\\times$ \\\\\n  & TG        & 0.484 & 0.043 & 2.57 & 1.437 & 11.2$\\times$ \\\\\n  & LoRA-only & 0.481 & 0.028 & 2.60 & 1.419 & 17.2$\\times$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n"
  }
}
```

</details>

---

### Tool result

_source line 206 · 2026-05-24T15:22:21.917745+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_crossmodel_detail.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 207 · 2026-05-24T15:22:21.917923+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_perturn_llama.tex",
  "content": "% Per-turn AR GAR-ours for Llama-3.1-8B-Instruct\n% Panel (a): N=20, T=4 (eval_llama_ar_n20) — reliable estimates\n% Panel (b): Base only, N=5, T=10 (llama_phase1_gar_diag) — decay profile\n\\begin{table}[h]\n\\centering\n\\caption{Per-turn autoregressive GAR-ours ($\\beta{=}0$) on Llama-3.1-8B-Instruct.\n(a)~Three-way comparison using $N{=}20$ conversations ($T{=}4$ turns).\n(b)~Base model decay profile ($N{=}5$, $T{=}10$).}\n\\label{tab:perturn-llama}\n\\small\n\\begin{subtable}[t]{0.55\\columnwidth}\n\\centering\n\\caption{$N{=}20$, $T{=}4$}\n\\begin{tabular}{@{}l cccc@{}}\n\\toprule\n\\textbf{Config.} & \\textbf{T1} & \\textbf{T2} & \\textbf{T3} & \\textbf{T4} \\\\\n\\midrule\nBase      & .028 & .013 & .009 & .008 \\\\\nTG        & .041 & .042 & .049 & .038 \\\\\nLoRA-only & .033 & .049 & .025 & .031 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{subtable}\n\\hfill\n\\begin{subtable}[t]{0.42\\columnwidth}\n\\centering\n\\caption{Base decay ($N{=}5$, $T{=}10$)}\n\\begin{tabular}{@{}cc@{}}\n\\toprule\n\\textbf{Turn} & \\textbf{GAR-ours} \\\\\n\\midrule\n1  & .026 \\\\\n2  & .018 \\\\\n3  & .009 \\\\\n4  & .006 \\\\\n5  & .006 \\\\\n6  & .004 \\\\\n7  & .004 \\\\\n8  & .004 \\\\\n9  & .005 \\\\\n10 & .003 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{subtable}\n\\end{table}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_perturn_llama.tex",
    "content": "% Per-turn AR GAR-ours for Llama-3.1-8B-Instruct\n% Panel (a): N=20, T=4 (eval_llama_ar_n20) — reliable estimates\n% Panel (b): Base only, N=5, T=10 (llama_phase1_gar_diag) — decay profile\n\\begin{table}[h]\n\\centering\n\\caption{Per-turn autoregressive GAR-ours ($\\beta{=}0$) on Llama-3.1-8B-Instruct.\n(a)~Three-way comparison using $N{=}20$ conversations ($T{=}4$ turns).\n(b)~Base model decay profile ($N{=}5$, $T{=}10$).}\n\\label{tab:perturn-llama}\n\\small\n\\begin{subtable}[t]{0.55\\columnwidth}\n\\centering\n\\caption{$N{=}20$, $T{=}4$}\n\\begin{tabular}{@{}l cccc@{}}\n\\toprule\n\\textbf{Config.} & \\textbf{T1} & \\textbf{T2} & \\textbf{T3} & \\textbf{T4} \\\\\n\\midrule\nBase      & .028 & .013 & .009 & .008 \\\\\nTG        & .041 & .042 & .049 & .038 \\\\\nLoRA-only & .033 & .049 & .025 & .031 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{subtable}\n\\hfill\n\\begin{subtable}[t]{0.42\\columnwidth}\n\\centering\n\\caption{Base decay ($N{=}5$, $T{=}10$)}\n\\begin{tabular}{@{}cc@{}}\n\\toprule\n\\textbf{Turn} & \\textbf{GAR-ours} \\\\\n\\midrule\n1  & .026 \\\\\n2  & .018 \\\\\n3  & .009 \\\\\n4  & .006 \\\\\n5  & .006 \\\\\n6  & .004 \\\\\n7  & .004 \\\\\n8  & .004 \\\\\n9  & .005 \\\\\n10 & .003 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{subtable}\n\\end{table}\n"
  }
}
```

</details>

---

### Tool result

_source line 208 · 2026-05-24T15:22:21.918101+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/tab_perturn_llama.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 209 · 2026-05-24T15:22:21.918236+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper/gen_fig_perturn_qwen_detail.py",
  "content": "\"\"\"Per-turn AR GAR decay for Qwen2.5-7B — 6 configurations.\"\"\"\nimport sys\nsys.path.insert(0, '/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper')\nfrom palette import *\nimport numpy as np\n\napply_style()\n\nturns = np.arange(1, 6)\n\ndata = {\n    'Base':       [0.0853, 0.0319, 0.0206, 0.0125, 0.0042],\n    'ThreadGate': [0.1297, 0.0725, 0.0591, 0.0428, 0.0664],\n    'PCGrad':     [0.0903, 0.0382, 0.0276, 0.0292, 0.0267],\n    'UG':         [0.1130, 0.0564, 0.0328, 0.0198, 0.0160],\n    'LoRA':       [0.1072, 0.0586, 0.0304, 0.0489, 0.0397],\n    'SS':         [0.4581, 0.3813, 0.3436, 0.3699, 0.3653],\n}\n\nmarkers = {\n    'Base': 'o', 'ThreadGate': 's', 'PCGrad': 'D',\n    'UG': '^', 'LoRA': 'v', 'SS': 'P',\n}\n\nfig, ax = plt.subplots(figsize=(3.4, 2.4))\n\nfor name in CONFIG_ORDER:\n    vals = data[name]\n    ax.plot(turns, vals, marker=markers[name], markersize=4,\n            color=COLORS[name], label=name, zorder=3)\n\nax.set_xlabel('Turn index')\nax.set_ylabel('AR GAR-ours')\nax.set_xticks(turns)\nax.set_xlim(0.7, 5.3)\nax.set_ylim(-0.01, 0.50)\n\nax.axhline(y=0, color=C_GRAY, linewidth=0.4, zorder=1)\n\nax.legend(ncol=2, loc='upper right', frameon=True, framealpha=0.9,\n          edgecolor='#DDDDDD', borderpad=0.4, handlelength=1.5)\n\nfig.tight_layout()\nsave_fig(fig, 'fig_perturn_qwen_detail')\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper/gen_fig_perturn_qwen_detail.py",
    "content": "\"\"\"Per-turn AR GAR decay for Qwen2.5-7B — 6 configurations.\"\"\"\nimport sys\nsys.path.insert(0, '/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper')\nfrom palette import *\nimport numpy as np\n\napply_style()\n\nturns = np.arange(1, 6)\n\ndata = {\n    'Base':       [0.0853, 0.0319, 0.0206, 0.0125, 0.0042],\n    'ThreadGate': [0.1297, 0.0725, 0.0591, 0.0428, 0.0664],\n    'PCGrad':     [0.0903, 0.0382, 0.0276, 0.0292, 0.0267],\n    'UG':         [0.1130, 0.0564, 0.0328, 0.0198, 0.0160],\n    'LoRA':       [0.1072, 0.0586, 0.0304, 0.0489, 0.0397],\n    'SS':         [0.4581, 0.3813, 0.3436, 0.3699, 0.3653],\n}\n\nmarkers = {\n    'Base': 'o', 'ThreadGate': 's', 'PCGrad': 'D',\n    'UG': '^', 'LoRA': 'v', 'SS': 'P',\n}\n\nfig, ax = plt.subplots(figsize=(3.4, 2.4))\n\nfor name in CONFIG_ORDER:\n    vals = data[name]\n    ax.plot(turns, vals, marker=markers[name], markersize=4,\n            color=COLORS[name], label=name, zorder=3)\n\nax.set_xlabel('Turn index')\nax.set_ylabel('AR GAR-ours')\nax.set_xticks(turns)\nax.set_xlim(0.7, 5.3)\nax.set_ylim(-0.01, 0.50)\n\nax.axhline(y=0, color=C_GRAY, linewidth=0.4, zorder=1)\n\nax.legend(ncol=2, loc='upper right', frameon=True, framealpha=0.9,\n          edgecolor='#DDDDDD', borderpad=0.4, handlelength=1.5)\n\nfig.tight_layout()\nsave_fig(fig, 'fig_perturn_qwen_detail')\n"
  }
}
```

</details>

---

### Tool result

_source line 210 · 2026-05-24T15:22:21.918377+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper/gen_fig_perturn_qwen_detail.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 211 · 2026-05-24T15:22:21.918529+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper/gen_fig_perturn_llama_detail.py",
  "content": "\"\"\"Per-turn AR GAR decay for Llama-3.1-8B — Base/TG/LoRA-only.\"\"\"\nimport sys\nsys.path.insert(0, '/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper')\nfrom palette import *\nimport numpy as np\n\napply_style()\n\n# N=20 T=4 data (eval_llama_ar_n20) — reliable estimates\nturns_4 = np.arange(1, 5)\ndata_4 = {\n    'Base':       [0.0282, 0.0128, 0.0092, 0.0084],\n    'ThreadGate': [0.0409, 0.0415, 0.0486, 0.0383],\n    'LoRA':       [0.0332, 0.0490, 0.0254, 0.0314],\n}\n\n# Base T=10 decay profile (llama_phase1_gar_diag, N=5)\nturns_10 = np.arange(1, 11)\nbase_t10 = [0.0263, 0.0183, 0.0087, 0.0055, 0.0060,\n            0.0035, 0.0038, 0.0037, 0.0050, 0.0026]\n\nmarkers = {'Base': 'o', 'ThreadGate': 's', 'LoRA': 'v'}\n\nfig, (ax1, ax2) = plt.subplots(1, 2, figsize=(5.5, 2.2),\n                                gridspec_kw={'width_ratios': [1, 1.3]})\n\n# --- Left panel: 3-way comparison T=1-4 ---\nfor name, vals in data_4.items():\n    ax1.plot(turns_4, vals, marker=markers[name], markersize=4.5,\n             color=COLORS[name], label=name, zorder=3)\n\nax1.set_xlabel('Turn index')\nax1.set_ylabel('AR GAR-ours')\nax1.set_xticks(turns_4)\nax1.set_xlim(0.7, 4.3)\nax1.set_ylim(-0.002, 0.058)\nax1.set_title('(a) 3-way ($N{=}20$, $T{=}4$)', fontsize=8)\nax1.legend(frameon=True, framealpha=0.9, edgecolor='#DDDDDD',\n           borderpad=0.3, handlelength=1.5, loc='upper right')\n\n# --- Right panel: Base decay T=1-10 ---\nax2.plot(turns_10, base_t10, marker='o', markersize=4, color=C_BASE,\n         label='Base', zorder=3)\nax2.fill_between(turns_10, 0, base_t10, alpha=0.12, color=C_BASE)\n\nax2.annotate(f'$-$90.1\\\\%', xy=(10, base_t10[-1]),\n             xytext=(8.5, 0.018), fontsize=7, color=C_BASE,\n             arrowprops=dict(arrowstyle='->', color=C_BASE, lw=0.8))\n\nax2.set_xlabel('Turn index')\nax2.set_ylabel('AR GAR-ours')\nax2.set_xticks(turns_10)\nax2.set_xlim(0.5, 10.5)\nax2.set_ylim(-0.001, 0.032)\nax2.set_title('(b) Base decay ($N{=}5$, $T{=}10$)', fontsize=8)\n\nfig.tight_layout(w_pad=1.5)\nsave_fig(fig, 'fig_perturn_llama_detail')\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper/gen_fig_perturn_llama_detail.py",
    "content": "\"\"\"Per-turn AR GAR decay for Llama-3.1-8B — Base/TG/LoRA-only.\"\"\"\nimport sys\nsys.path.insert(0, '/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper')\nfrom palette import *\nimport numpy as np\n\napply_style()\n\n# N=20 T=4 data (eval_llama_ar_n20) — reliable estimates\nturns_4 = np.arange(1, 5)\ndata_4 = {\n    'Base':       [0.0282, 0.0128, 0.0092, 0.0084],\n    'ThreadGate': [0.0409, 0.0415, 0.0486, 0.0383],\n    'LoRA':       [0.0332, 0.0490, 0.0254, 0.0314],\n}\n\n# Base T=10 decay profile (llama_phase1_gar_diag, N=5)\nturns_10 = np.arange(1, 11)\nbase_t10 = [0.0263, 0.0183, 0.0087, 0.0055, 0.0060,\n            0.0035, 0.0038, 0.0037, 0.0050, 0.0026]\n\nmarkers = {'Base': 'o', 'ThreadGate': 's', 'LoRA': 'v'}\n\nfig, (ax1, ax2) = plt.subplots(1, 2, figsize=(5.5, 2.2),\n                                gridspec_kw={'width_ratios': [1, 1.3]})\n\n# --- Left panel: 3-way comparison T=1-4 ---\nfor name, vals in data_4.items():\n    ax1.plot(turns_4, vals, marker=markers[name], markersize=4.5,\n             color=COLORS[name], label=name, zorder=3)\n\nax1.set_xlabel('Turn index')\nax1.set_ylabel('AR GAR-ours')\nax1.set_xticks(turns_4)\nax1.set_xlim(0.7, 4.3)\nax1.set_ylim(-0.002, 0.058)\nax1.set_title('(a) 3-way ($N{=}20$, $T{=}4$)', fontsize=8)\nax1.legend(frameon=True, framealpha=0.9, edgecolor='#DDDDDD',\n           borderpad=0.3, handlelength=1.5, loc='upper right')\n\n# --- Right panel: Base decay T=1-10 ---\nax2.plot(turns_10, base_t10, marker='o', markersize=4, color=C_BASE,\n         label='Base', zorder=3)\nax2.fill_between(turns_10, 0, base_t10, alpha=0.12, color=C_BASE)\n\nax2.annotate(f'$-$90.1\\\\%', xy=(10, base_t10[-1]),\n             xytext=(8.5, 0.018), fontsize=7, color=C_BASE,\n             arrowprops=dict(arrowstyle='->', color=C_BASE, lw=0.8))\n\nax2.set_xlabel('Turn index')\nax2.set_ylabel('AR GAR-ours')\nax2.set_xticks(turns_10)\nax2.set_xlim(0.5, 10.5)\nax2.set_ylim(-0.001, 0.032)\nax2.set_title('(b) Base decay ($N{=}5$, $T{=}10$)', fontsize=8)\n\nfig.tight_layout(w_pad=1.5)\nsave_fig(fig, 'fig_perturn_llama_detail')\n"
  }
}
```

</details>

---

### Tool result

_source line 212 · 2026-05-24T15:22:21.918685+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper/gen_fig_perturn_llama_detail.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 213 · 2026-05-24T15:22:21.918819+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper && python3 gen_fig_perturn_qwen_detail.py 2>&1",
  "description": "Generate Qwen per-turn GAR figure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper && python3 gen_fig_perturn_qwen_detail.py 2>&1",
    "description": "Generate Qwen per-turn GAR figure"
  }
}
```

</details>

---

### Tool call

_source line 214 · 2026-05-24T15:22:21.918938+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper && python3 gen_fig_perturn_llama_detail.py 2>&1",
  "description": "Generate Llama per-turn GAR figure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper && python3 gen_fig_perturn_llama_detail.py 2>&1",
    "description": "Generate Llama per-turn GAR figure"
  }
}
```

</details>

---

### Tool result

_source line 215 · 2026-05-24T15:22:21.919050+00:00_

Saved: fig_perturn_qwen_detail.pdf + .png

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 216 · 2026-05-24T15:22:21.919157+00:00_

Saved: fig_perturn_llama_detail.pdf + .png

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 217 · 2026-05-24T15:22:21.919276+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper/fig_perturn_qwen_detail.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper/fig_perturn_qwen_detail.png"
  }
}
```

</details>

---

### Tool result

_source line 218 · 2026-05-24T15:22:21.919685+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 219 · 2026-05-24T15:22:21.919820+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper/fig_perturn_llama_detail.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper/fig_perturn_llama_detail.png"
  }
}
```

</details>

---

### Tool result

_source line 220 · 2026-05-24T15:22:21.920297+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 221 · 2026-05-24T15:22:21.920483+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper/gen_fig_perturn_llama_detail.py",
  "old_string": "ax2.annotate(f'$-$90.1\\\\%', xy=(10, base_t10[-1]),\n             xytext=(8.5, 0.018), fontsize=7, color=C_BASE,\n             arrowprops=dict(arrowstyle='->', color=C_BASE, lw=0.8))",
  "new_string": "ax2.annotate('−90.1%', xy=(10, base_t10[-1]),\n             xytext=(8.5, 0.018), fontsize=7, color=C_BASE,\n             arrowprops=dict(arrowstyle='->', color=C_BASE, lw=0.8))"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper/gen_fig_perturn_llama_detail.py",
    "old_string": "ax2.annotate(f'$-$90.1\\\\%', xy=(10, base_t10[-1]),\n             xytext=(8.5, 0.018), fontsize=7, color=C_BASE,\n             arrowprops=dict(arrowstyle='->', color=C_BASE, lw=0.8))",
    "new_string": "ax2.annotate('−90.1%', xy=(10, base_t10[-1]),\n             xytext=(8.5, 0.018), fontsize=7, color=C_BASE,\n             arrowprops=dict(arrowstyle='->', color=C_BASE, lw=0.8))"
  }
}
```

</details>

---

### Tool result

_source line 222 · 2026-05-24T15:22:21.920648+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper/gen_fig_perturn_llama_detail.py has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 223 · 2026-05-24T15:22:21.920775+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "python3 gen_fig_perturn_llama_detail.py 2>&1",
  "description": "Regenerate Llama per-turn figure with fixed annotation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "Bash",
  "tool_args": {
    "command": "python3 gen_fig_perturn_llama_detail.py 2>&1",
    "description": "Regenerate Llama per-turn figure with fixed annotation"
  }
}
```

</details>

---

### Tool result

_source line 224 · 2026-05-24T15:22:21.920892+00:00_

Saved: fig_perturn_llama_detail.pdf + .png

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 225 · 2026-05-24T15:22:21.921004+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper/fig_perturn_llama_detail.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper/fig_perturn_llama_detail.png"
  }
}
```

</details>

---

### Tool result

_source line 226 · 2026-05-24T15:22:21.921487+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 227 · 2026-05-24T15:22:21.921655+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/ && echo \"---\" && ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper/fig_perturn_*.{pdf,png} /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper/gen_fig_perturn_*.py",
  "description": "List all generated output files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/appendix_expansion/ && echo \"---\" && ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper/fig_perturn_*.{pdf,png} /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper/gen_fig_perturn_*.py",
    "description": "List all generated output files"
  }
}
```

</details>

---

### Tool result

_source line 228 · 2026-05-24T15:22:21.921822+00:00_

total 44
drwxr-xr-x  2 ubuntu ubuntu 4096 May 24 15:20 .
drwxr-xr-x 20 ubuntu ubuntu 4096 May 24 15:12 ..
-rw-r--r--  1 ubuntu ubuntu 1300 May 24 15:19 tab_crossmodel_detail.tex
-rw-r--r--  1 ubuntu ubuntu  932 May 24 15:13 tab_dataset_stats.tex
-rw-r--r--  1 ubuntu ubuntu 1593 May 24 15:13 tab_gar_robustness.tex
-rw-r--r--  1 ubuntu ubuntu  962 May 24 15:13 tab_mmlu_detail.tex
-rw-r--r--  1 ubuntu ubuntu 1655 May 24 15:19 tab_perseed_ss.tex
-rw-r--r--  1 ubuntu ubuntu 1267 May 24 15:19 tab_perseed_tg.tex
-rw-r--r--  1 ubuntu ubuntu 1182 May 24 15:20 tab_perturn_llama.tex
-rw-r--r--  1 ubuntu ubuntu 1038 May 24 15:19 tab_perturn_qwen.tex
-rw-r--r--  1 ubuntu ubuntu 1450 May 24 15:13 tab_qwen15b_results.tex
---
-rw-r--r-- 1 ubuntu ubuntu 23573 May 24 15:21 /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper/fig_perturn_llama_detail.pdf
-rw-r--r-- 1 ubuntu ubuntu 94171 May 24 15:21 /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper/fig_perturn_llama_detail.png
-rw-r--r-- 1 ubuntu ubuntu 13534 May 24 15:21 /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper/fig_perturn_qwen_detail.pdf
-rw-r--r-- 1 ubuntu ubuntu 69560 May 24 15:21 /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper/fig_perturn_qwen_detail.png
-rw-r--r-- 1 ubuntu ubuntu  2060 May 24 15:21 /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper/gen_fig_perturn_llama_detail.py
-rw-r--r-- 1 ubuntu ubuntu  1332 May 24 15:20 /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/figures/paper/gen_fig_perturn_qwen_detail.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 229 · 2026-05-24T15:22:21.922089+00:00_

全部完成。产出汇总：

**第 1 项：Per-seed 详细结果表**
- `tab_perseed_ss.tex` — SS 3-seed (s42/s123/s456) × TF+AR(β=0/3/5)，含 GAR-ours、GAR-Dongre、PPL、Mean±Std
- `tab_perseed_tg.tex` — TG 2-seed (s42/s123) × TF+AR，含 gap ratio

**第 2 项：Per-turn GAR 衰减详表 + 图**
- `tab_perturn_qwen.tex` — Qwen 6-way (Base/TG/PCGrad/UG/LoRA/SS) × Turn 1-5
- `tab_perturn_llama.tex` — Llama 3-way N=20 T=4 + Base 衰减 T=10 (subtable 格式)
- `fig_perturn_qwen_detail.pdf/.png` — 6 条线 × 5 turns，SS 远高于其他配置
- `fig_perturn_llama_detail.pdf/.png` — 左 panel: TG/LO 维持 GAR vs Base 衰减；右 panel: Base 10-turn −90.1% 衰减曲线

**第 3 项：跨模型详细对比表**
- `tab_crossmodel_detail.tex` — Qwen vs Llama × Base/TG/LoRA-only，含 TF GAR、AR GAR、TF PPL、AR PPL、Gap ratio

数据说明：
- SS s42 AR 使用 d048_final_ar N=50 评估（GAR 0.347），与 s123/s456 一致
- TG s123 AR 仅有 N=5 T=10 评估（GAR 0.017），已在表注中说明
- Llama per-turn T=10 数据 (TG/LO) 因 N=5 噪声极大，图中改用 N=20 T=4 数据

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_code_appendix_seeds_perturn_crossmodel_20260524T150612"
}
```

</details>

---
