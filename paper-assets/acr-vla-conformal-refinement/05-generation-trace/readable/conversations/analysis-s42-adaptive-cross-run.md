# analysis s42 adaptive cross run

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 72
- **Recorded user turns:** 0
- **Tool calls:** 35
- **Original source:** `logs/chats/worker_analysis_s42-adaptive-cross-run_20260524T222048.jsonl`
- **Structured JSON:** [`76744cc8d26f9bbc3e71.json`](../../sessions/76/76744cc8d26f9bbc3e71.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

72 recorded events

### Assistant

_source line 1 · 2026-05-24T22:20:55.892545+00:00_

Not logged in · Please run /login

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_s42-adaptive-cross-run_20260524T222048"
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-24T22:26:11.063179+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:read_registry,ssh_read_only,ssh_execute",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_s42-adaptive-cross-run_20260524T222048",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:read_registry,ssh_read_only,ssh_execute",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-24T22:26:11.063503+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_s42-adaptive-cross-run_20260524T222048",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-24T22:26:11.063657+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_s42-adaptive-cross-run_20260524T222048",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-24T22:26:11.063799+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_s42-adaptive-cross-run_20260524T222048",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-24T22:26:11.063935+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "fields": "['*']",
  "filters": "{'seed': 42, 'benchmark': 'spatial', 'mode': 'adaptive_conformal_crm'}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_s42-adaptive-cross-run_20260524T222048",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "fields": "['*']",
    "filters": "{'seed': 42, 'benchmark': 'spatial', 'mode': 'adaptive_conformal_crm'}"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-24T22:26:11.064064+00:00_

{"result":"{\"success\": true, \"data\": {\"experiments\": {}, \"count\": 0, \"total\": 0, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2867}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_s42-adaptive-cross-run_20260524T222048",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-24T22:26:11.064192+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_s42-adaptive-cross-run_20260524T222048",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-24T22:26:11.064863+00:00_

Error: result (118,819 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/7b3be6c1-bf89-4354-8333-43cf80e9d749/tool-results/mcp-agent-ml-research-read_registry-1779661277792.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/7b3be6c1-bf89-4354-8333-43cf80e9d749/tool-results/mcp-agent-ml-research-read_registry-1779661277792.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_s42-adaptive-cross-run_20260524T222048",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-24T22:26:11.065050+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "jq -r '.result | fromjson | .data.experiments | to_entries | map(.value) | map(select(.seed == 42 and (.benchmark // \"\") == \"spatial\" and (.mode // \"\") == \"adaptive_conformal_crm\")) | length' /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/7b3be6c1-bf89-4354-8333-43cf80e9d749/tool-results/mcp-agent-ml-research-read_registry-1779661277792.txt",
  "description": "Count s42 adaptive spatial experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_s42-adaptive-cross-run_20260524T222048",
  "tool": "Bash",
  "tool_args": {
    "command": "jq -r '.result | fromjson | .data.experiments | to_entries | map(.value) | map(select(.seed == 42 and (.benchmark // \"\") == \"spatial\" and (.mode // \"\") == \"adaptive_conformal_crm\")) | length' /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/7b3be6c1-bf89-4354-8333-43cf80e9d749/tool-results/mcp-agent-ml-research-read_registry-1779661277792.txt",
    "description": "Count s42 adaptive spatial experiments"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-24T22:26:11.065201+00:00_

0

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_s42-adaptive-cross-run_20260524T222048",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-24T22:26:11.065389+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "jq -r '.result | fromjson | .data.experiments | to_entries[0].value | keys' /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/7b3be6c1-bf89-4354-8333-43cf80e9d749/tool-results/mcp-agent-ml-research-read_registry-1779661277792.txt",
  "description": "Inspect experiment record keys"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_s42-adaptive-cross-run_20260524T222048",
  "tool": "Bash",
  "tool_args": {
    "command": "jq -r '.result | fromjson | .data.experiments | to_entries[0].value | keys' /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/7b3be6c1-bf89-4354-8333-43cf80e9d749/tool-results/mcp-agent-ml-research-read_registry-1779661277792.txt",
    "description": "Inspect experiment record keys"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-24T22:26:11.065523+00:00_

[
  "checkpoint_path",
  "completed_at",
  "conclusion",
  "created_at",
  "hypothesis",
  "notes",
  "retry_count",
  "spec",
  "status",
  "updated_at"
]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_s42-adaptive-cross-run_20260524T222048",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-24T22:26:11.065640+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "jq -r '.result | fromjson | .data.experiments | to_entries[0].value.spec | keys' /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/7b3be6c1-bf89-4354-8333-43cf80e9d749/tool-results/mcp-agent-ml-research-read_registry-1779661277792.txt",
  "description": "Inspect spec keys"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_s42-adaptive-cross-run_20260524T222048",
  "tool": "Bash",
  "tool_args": {
    "command": "jq -r '.result | fromjson | .data.experiments | to_entries[0].value.spec | keys' /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/7b3be6c1-bf89-4354-8333-43cf80e9d749/tool-results/mcp-agent-ml-research-read_registry-1779661277792.txt",
    "description": "Inspect spec keys"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-24T22:26:11.065760+00:00_

[
  "checkpoint_source",
  "command",
  "data_count",
  "data_path",
  "eval_data",
  "gpu",
  "log_path",
  "model_name",
  "output_file",
  "pid",
  "seed",
  "server",
  "tmux_session"
]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_s42-adaptive-cross-run_20260524T222048",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-24T22:26:11.065909+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "jq -r '.result | fromjson | .data.experiments | to_entries | map(select(.value.spec.seed == 42 and ((.value.spec.command // \"\") | test(\"adaptive_conformal_crm\")) and ((.value.spec.command // \"\") | test(\"spatial\")))) | length' /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/7b3be6c1-bf89-4354-8333-43cf80e9d749/tool-results/mcp-agent-ml-research-read_registry-1779661277792.txt",
  "description": "Count s42 adaptive spatial via command"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_s42-adaptive-cross-run_20260524T222048",
  "tool": "Bash",
  "tool_args": {
    "command": "jq -r '.result | fromjson | .data.experiments | to_entries | map(select(.value.spec.seed == 42 and ((.value.spec.command // \"\") | test(\"adaptive_conformal_crm\")) and ((.value.spec.command // \"\") | test(\"spatial\")))) | length' /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/7b3be6c1-bf89-4354-8333-43cf80e9d749/tool-results/mcp-agent-ml-research-read_registry-1779661277792.txt",
    "description": "Count s42 adaptive spatial via command"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-24T22:26:11.066082+00:00_

3

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_s42-adaptive-cross-run_20260524T222048",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-24T22:26:11.066204+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "jq -r '.result | fromjson | .data.experiments | to_entries | map(select(.value.spec.seed == 42 and ((.value.spec.command // \"\") | test(\"adaptive_conformal_crm\")) and ((.value.spec.command // \"\") | test(\"spatial\")))) | map({exp_id: .key, status: .value.status, created: .value.created_at, completed: .value.completed_at, server: .value.spec.server, gpu: .value.spec.gpu, command: .value.spec.command, output_file: .value.spec.output_file, log_path: .value.spec.log_path, conclusion: .value.conclusion})' /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/7b3be6c1-bf89-4354-8333-43cf80e9d749/tool-results/mcp-agent-ml-research-read_registry-1779661277792.txt",
  "description": "Dump s42 adaptive spatial details"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_s42-adaptive-cross-run_20260524T222048",
  "tool": "Bash",
  "tool_args": {
    "command": "jq -r '.result | fromjson | .data.experiments | to_entries | map(select(.value.spec.seed == 42 and ((.value.spec.command // \"\") | test(\"adaptive_conformal_crm\")) and ((.value.spec.command // \"\") | test(\"spatial\")))) | map({exp_id: .key, status: .value.status, created: .value.created_at, completed: .value.completed_at, server: .value.spec.server, gpu: .value.spec.gpu, command: .value.spec.command, output_file: .value.spec.output_file, log_path: .value.spec.log_path, conclusion: .value.conclusion})' /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/7b3be6c1-bf89-4354-8333-43cf80e9d749/tool-results/mcp-agent-ml-research-read_registry-1779661277792.txt",
    "description": "Dump s42 adaptive spatial details"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-24T22:26:11.066387+00:00_

[
  {
    "exp_id": "eval-supp-adapt-tau035-spatial-s42-r2",
    "status": "DONE",
    "created": "2026-05-23T06:13:52.718Z",
    "completed": "2026-05-23T06:15:38.149Z",
    "server": "bjb1-32546",
    "gpu": null,
    "command": "python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 42 --n_rollouts 20 --conformal_threshold 0.35 --max_correction_norm 0.2",
    "output_file": null,
    "log_path": null,
    "conclusion": "success"
  },
  {
    "exp_id": "eval-supp-adapt-tau015-spatial-s42-r2",
    "status": "DONE",
    "created": "2026-05-23T06:13:51.160Z",
    "completed": "2026-05-23T06:15:37.282Z",
    "server": "bjb1-32546",
    "gpu": null,
    "command": "python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 42 --n_rollouts 20 --conformal_threshold 0.15 --max_correction_norm 0.2",
    "output_file": null,
    "log_path": null,
    "conclusion": "success"
  },
  {
    "exp_id": "eval-supp-adapt-tau025-spatial-s42-r2",
    "status": "DONE",
    "created": "2026-05-23T06:13:46.810Z",
    "completed": "2026-05-23T06:15:35.291Z",
    "server": "bjb1-32546",
    "gpu": null,
    "command": "python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 42 --n_rollouts 20 --conformal_threshold 0.25 --max_correction_norm 0.2",
    "output_file": null,
    "log_path": null,
    "conclusion": "success"
  }
]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_s42-adaptive-cross-run_20260524T222048",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-24T22:26:11.066540+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "jq -r '.result | fromjson | .data.experiments | to_entries | map(select(.value.spec.seed == 42 and ((.value.spec.command // \"\") | test(\"spatial\")) and ((.value.spec.command // \"\") | test(\"adaptive\")))) | map({exp_id: .key, status: .value.status, created: .value.created_at, server: .value.spec.server, command: .value.spec.command})' /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/7b3be6c1-bf89-4354-8333-43cf80e9d749/tool-results/mcp-agent-ml-research-read_registry-1779661277792.txt",
  "description": "Broader filter s42 adaptive spatial"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_s42-adaptive-cross-run_20260524T222048",
  "tool": "Bash",
  "tool_args": {
    "command": "jq -r '.result | fromjson | .data.experiments | to_entries | map(select(.value.spec.seed == 42 and ((.value.spec.command // \"\") | test(\"spatial\")) and ((.value.spec.command // \"\") | test(\"adaptive\")))) | map({exp_id: .key, status: .value.status, created: .value.created_at, server: .value.spec.server, command: .value.spec.command})' /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/7b3be6c1-bf89-4354-8333-43cf80e9d749/tool-results/mcp-agent-ml-research-read_registry-1779661277792.txt",
    "description": "Broader filter s42 adaptive spatial"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-24T22:26:11.066678+00:00_

[
  {
    "exp_id": "eval-supp-adapt-tau035-spatial-s42-r2",
    "status": "DONE",
    "created": "2026-05-23T06:13:52.718Z",
    "server": "bjb1-32546",
    "command": "python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 42 --n_rollouts 20 --conformal_threshold 0.35 --max_correction_norm 0.2"
  },
  {
    "exp_id": "eval-supp-adapt-tau015-spatial-s42-r2",
    "status": "DONE",
    "created": "2026-05-23T06:13:51.160Z",
    "server": "bjb1-32546",
    "command": "python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 42 --n_rollouts 20 --conformal_threshold 0.15 --max_correction_norm 0.2"
  },
  {
    "exp_id": "eval-supp-adapt-tau025-spatial-s42-r2",
    "status": "DONE",
    "created": "2026-05-23T06:13:46.810Z",
    "server": "bjb1-32546",
    "command": "python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 42 --n_rollouts 20 --conformal_threshold 0.25 --max_correction_norm 0.2"
  },
  {
    "exp_id": "eval-adaptive-k-spatial-p90-seed42",
    "status": "DONE",
    "created": "2026-05-20T10:52:05.759Z",
    "server": "bjb2-28827",
    "command": "python -u src/evaluate.py --mode adaptive_k --benchmark LIBERO-Spatial --seed 42 --n_rollouts 10 --adaptive_k_threshold 0.125870 --output_file logs/eval-adaptive-k-spatial-p90-seed42.json"
  }
]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_s42-adaptive-cross-run_20260524T222048",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-24T22:26:11.066827+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "jq -r '.result | fromjson | .data.experiments | to_entries | map(select(((.value.spec.command // \"\") | test(\"spatial\")) and ((.value.spec.command // \"\") | test(\"adaptive_conformal\")) and ((.value.spec.command // \"\") | test(\"seed 42\")))) | map({exp_id: .key, status: .value.status, created: .value.created_at, server: .value.spec.server, command: .value.spec.command, conclusion: .value.conclusion})' /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/7b3be6c1-bf89-4354-8333-43cf80e9d749/tool-results/mcp-agent-ml-research-read_registry-1779661277792.txt",
  "description": "All adaptive_conformal spatial seed42 runs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_s42-adaptive-cross-run_20260524T222048",
  "tool": "Bash",
  "tool_args": {
    "command": "jq -r '.result | fromjson | .data.experiments | to_entries | map(select(((.value.spec.command // \"\") | test(\"spatial\")) and ((.value.spec.command // \"\") | test(\"adaptive_conformal\")) and ((.value.spec.command // \"\") | test(\"seed 42\")))) | map({exp_id: .key, status: .value.status, created: .value.created_at, server: .value.spec.server, command: .value.spec.command, conclusion: .value.conclusion})' /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/7b3be6c1-bf89-4354-8333-43cf80e9d749/tool-results/mcp-agent-ml-research-read_registry-1779661277792.txt",
    "description": "All adaptive_conformal spatial seed42 runs"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-24T22:26:11.066962+00:00_

[
  {
    "exp_id": "eval-supp-adapt-tau035-spatial-s42-r2",
    "status": "DONE",
    "created": "2026-05-23T06:13:52.718Z",
    "server": "bjb1-32546",
    "command": "python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 42 --n_rollouts 20 --conformal_threshold 0.35 --max_correction_norm 0.2",
    "conclusion": "success"
  },
  {
    "exp_id": "eval-supp-adapt-tau015-spatial-s42-r2",
    "status": "DONE",
    "created": "2026-05-23T06:13:51.160Z",
    "server": "bjb1-32546",
    "command": "python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 42 --n_rollouts 20 --conformal_threshold 0.15 --max_correction_norm 0.2",
    "conclusion": "success"
  },
  {
    "exp_id": "eval-supp-adapt-tau025-spatial-s42-r2",
    "status": "DONE",
    "created": "2026-05-23T06:13:46.810Z",
    "server": "bjb1-32546",
    "command": "python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 42 --n_rollouts 20 --conformal_threshold 0.25 --max_correction_norm 0.2",
    "conclusion": "success"
  }
]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_s42-adaptive-cross-run_20260524T222048",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-24T22:26:11.067099+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "jq -r '.result | fromjson | .data.experiments | to_entries | map(select(((.value.spec.command // \"\") | test(\"adaptive_conformal\")))) | map({exp_id: .key, status: .value.status, created: .value.created_at, server: .value.spec.server, command: .value.spec.command})' /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/7b3be6c1-bf89-4354-8333-43cf80e9d749/tool-results/mcp-agent-ml-research-read_registry-1779661277792.txt",
  "description": "All adaptive_conformal runs in registry"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_s42-adaptive-cross-run_20260524T222048",
  "tool": "Bash",
  "tool_args": {
    "command": "jq -r '.result | fromjson | .data.experiments | to_entries | map(select(((.value.spec.command // \"\") | test(\"adaptive_conformal\")))) | map({exp_id: .key, status: .value.status, created: .value.created_at, server: .value.spec.server, command: .value.spec.command})' /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/7b3be6c1-bf89-4354-8333-43cf80e9d749/tool-results/mcp-agent-ml-research-read_registry-1779661277792.txt",
    "description": "All adaptive_conformal runs in registry"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-24T22:26:11.067241+00:00_

[
  {
    "exp_id": "eval-supp-goal-adapt-tau025-s47",
    "status": "RUNNING",
    "created": "2026-05-24T09:46:22.983Z",
    "server": "bjb2-28827",
    "command": "CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py --benchmark goal --mode adaptive_conformal_crm --seed 47 --n_rollouts 20 --K 2 --adaptive_threshold 0.2 --conformal_threshold 0.25 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt"
  },
  {
    "exp_id": "eval-supp-spatial-adapt-tau025-s45-r3",
    "status": "RUNNING",
    "created": "2026-05-23T23:25:18.823Z",
    "server": "cqa1-32758",
    "command": "python -u src/evaluate.py --benchmark spatial --mode adaptive_conformal_crm --seed 45 --n_rollouts 20 --max_correction_norm 0.2 --conformal_threshold 0.25 --K 2 --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt"
  },
  {
    "exp_id": "eval-supp-adapt-tau035-spatial-s42-r2",
    "status": "DONE",
    "created": "2026-05-23T06:13:52.718Z",
    "server": "bjb1-32546",
    "command": "python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 42 --n_rollouts 20 --conformal_threshold 0.35 --max_correction_norm 0.2"
  },
  {
    "exp_id": "eval-supp-adapt-tau015-spatial-s42-r2",
    "status": "DONE",
    "created": "2026-05-23T06:13:51.160Z",
    "server": "bjb1-32546",
    "command": "python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 42 --n_rollouts 20 --conformal_threshold 0.15 --max_correction_norm 0.2"
  },
  {
    "exp_id": "eval-supp-adapt-tau025-spatial-s42-r2",
    "status": "DONE",
    "created": "2026-05-23T06:13:46.810Z",
    "server": "bjb1-32546",
    "command": "python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --benchmark spatial --seed 
…[truncated 78 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_s42-adaptive-cross-run_20260524T222048",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-24T22:26:11.067424+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:read_project_file,load_project_config,read_roadmap,register_artifact",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_s42-adaptive-cross-run_20260524T222048",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:read_project_file,load_project_config,read_roadmap,register_artifact",
    "max_results": "5"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-24T22:26:11.067545+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_s42-adaptive-cross-run_20260524T222048",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-24T22:26:11.067655+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/",
  "description": "List project directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_s42-adaptive-cross-run_20260524T222048",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/",
    "description": "List project directory"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-24T22:26:11.067773+00:00_

AGENTS.md
ROADMAP.lock
ROADMAP.md
_last_visual_review.json
artifacts
checkpoints
decisions.lock
decisions.yaml
docs
dream_registry.lock
dream_registry.yaml
dream_registry.yaml.bak
experiment_plan.lock
experiment_plan.yaml
figures
literature_map.yaml
logs
memory.md
mistakes.lock
mistakes.yaml
openvla_oft_wrapper.py
paper
paper_framing.md
paper_provenance.lock
paper_provenance.yaml
patch_modeling.py
registry.lock
registry.yaml
report.md
scripts
src
study_status.lock
task_context
worker_output.md
writing_plan.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_s42-adaptive-cross-run_20260524T222048",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-24T22:26:11.067889+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -rn \"82.0\\|79.5\\|s42.*adapt\\|adapt.*s42\\|spatial.*adapt\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/memory.md /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/report.md /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/worker_output.md 2>/dev/null | head -80",
  "description": "Search 82.0/79.5 in project memory/report"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_s42-adaptive-cross-run_20260524T222048",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -rn \"82.0\\|79.5\\|s42.*adapt\\|adapt.*s42\\|spatial.*adapt\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/memory.md /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/report.md /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/worker_output.md 2>/dev/null | head -80",
    "description": "Search 82.0/79.5 in project memory/report"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-24T22:26:11.068015+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/report.md:11:| 0.25 | 79.5% | 19.6% |
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/report.md:18:- K=1: SR=79.5% | K=5: 运行中 bjb2-40593 (7/10 tasks) | K=10: 默认值（见 τ-sweep）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_s42-adaptive-cross-run_20260524T222048",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-24T22:26:11.068134+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -rn \"82\\.0\\|79\\.5\\|adaptive.*tau.*0\\.25\\|tau025\\|Table 1\\|table_1\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ --include=\"*.md\" --include=\"*.yaml\" --include=\"*.tex\" 2>/dev/null | head -60",
  "description": "Search for tau 0.25 Table 1 references"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_s42-adaptive-cross-run_20260524T222048",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -rn \"82\\.0\\|79\\.5\\|adaptive.*tau.*0\\.25\\|tau025\\|Table 1\\|table_1\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ --include=\"*.md\" --include=\"*.yaml\" --include=\"*.tex\" 2>/dev/null | head -60",
    "description": "Search for tau 0.25 Table 1 references"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-24T22:26:11.068378+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/appendix.tex:38:\looseness=-1 Table~\ref{tab:tau_sweep} reports success rates on Goal and Spatial (seed 42) as a function of the uncertainty threshold $\tau$, with $\varepsilon{=}0.2$ (the adaptive correction magnitude). Both suites exhibit an inverted-U pattern. On Goal, $\tau{=}0.10$ triggers on 73.9\% of steps and degrades by $-$2.5\,pp, while $\tau{=}0.40$ triggers on 1.2\% and recovers VLA-only performance. On Spatial, $\tau{=}0.10$ triggers on 75.2\% but yields only $+$0.5\,pp; the peak is at $\tau{=}0.20$ ($+$2.5\,pp, 26.6\% trigger). The consistent optimal region $\tau \in [0.20, 0.25]$ across both suites supports the mechanism claim: $\tau$ causally controls trigger rate, which controls improvement.
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/experiments.tex:95:To isolate the contribution of multi-sample centering, we evaluate $K{=}1$ adaptive CRM (single sample, same gating and correction) on Spatial: SR${=}79.5$\% vs.\ $K{=}2$ adaptive SR${=}80.8$\% ($\Delta{=}{+}1.3$\,pp). The gap quantifies the benefit of argmin-to-centroid selection before correction.
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/decision_seed43_kill_criterion.md:31:   - 更新 Table 1 和 Section 4.1
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/task_context/agent.md:19:  - 活跃 6 个 eval：goal-adapt-tau025-s42(cuda:2), k2mean-object-s42(cuda:1), k2mean-spatial-s42(cuda:4), goal-reconvla-s42(cuda:3), obj-adapt-tau025-s42(cuda:0), goal-vla-only-wrapper-s42(cuda:5)
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/task_context/agent.md:29:**刚做完**：收到 `eval-supp-adapt-tau025-spatial-s44` (Adaptive CRM τ=0.25, Spatial seed44) 完成回调，已派 Worker (`worker_analyze_eval-supp-adapt-tau025-spatial-s44_20260523T084318`) 去读日志提取 metrics 并更新 regis
…[truncated 13242 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_s42-adaptive-cross-run_20260524T222048",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-24T22:26:11.068570+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \"tau_sweep\\|Spatial.*0.25\\|Adapt.*Spatial\\|82\\.0\\|79\\.5\\|80\\.8\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/appendix.tex /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/experiments.tex 2>/dev/null | head -60",
  "description": "Inspect Table 1 / tau-sweep numbers in paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_s42-adaptive-cross-run_20260524T222048",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \"tau_sweep\\|Spatial.*0.25\\|Adapt.*Spatial\\|82\\.0\\|79\\.5\\|80\\.8\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/appendix.tex /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/experiments.tex 2>/dev/null | head -60",
    "description": "Inspect Table 1 / tau-sweep numbers in paper"
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-24T22:26:11.068735+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/appendix.tex:15:\label{sec:tau_sweep}
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/appendix.tex:19:\caption{Threshold sensitivity on Goal and Spatial suites (seed 42, $\varepsilon{=}0.2$). Seed-matched VLA-only baselines: Goal 83.5\%, Spatial 78.5\%. Both suites exhibit an inverted-U pattern with consistent optimal region $\tau \in [0.20, 0.25]$.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/appendix.tex:20:\label{tab:tau_sweep}
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/appendix.tex:31:0.25 & 7--9 & 84.0 ($+0.5$) & ${\sim}$19 & 80.8 ($+2.3$) \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/appendix.tex:38:\looseness=-1 Table~\ref{tab:tau_sweep} reports success rates on Goal and Spatial (seed 42) as a function of the uncertainty threshold $\tau$, with $\varepsilon{=}0.2$ (the adaptive correction magnitude). Both suites exhibit an inverted-U pattern. On Goal, $\tau{=}0.10$ triggers on 73.9\% of steps and degrades by $-$2.5\,pp, while $\tau{=}0.40$ triggers on 1.2\% and recovers VLA-only performance. On Spatial, $\tau{=}0.10$ triggers on 75.2\% but yields only $+$0.5\,pp; the peak is at $\tau{=}0.20$ ($+$2.5\,pp, 26.6\% trigger). The consistent optimal region $\tau \in [0.20, 0.25]$ across both suites supports the mechanism claim: $\tau$ causally controls trigger rate, which controls improvement.
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/experiments.tex:46:$K{=}10$ argmin & 10 & $80.3 \pm 1.0^{(3)}$ & $77.3 \pm 1.5^{(3)}$ & $80.8 \pm 0.3^{(3)}$ & $56.5^{(1)}$ \\
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/experiments.tex:49:ACR-VLA & 2 & $80.8 \pm 1.1^{(3)}$ & $
…[truncated 2186 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_s42-adaptive-cross-run_20260524T222048",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-24T22:26:11.068892+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -rn \"adapt.*spatial.*s42\\|spatial.*adapt.*s42\\|adapt-tau025-spatial-s42\\|adapt-tau-0.25-spatial-s42\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/task_context/history/agent/loop_25_1779575361.md 2>/dev/null | head -60",
  "description": "Trace 82.0% / 79.5% origin"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_s42-adaptive-cross-run_20260524T222048",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -rn \"adapt.*spatial.*s42\\|spatial.*adapt.*s42\\|adapt-tau025-spatial-s42\\|adapt-tau-0.25-spatial-s42\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/task_context/history/agent/loop_25_1779575361.md 2>/dev/null | head -60",
    "description": "Trace 82.0% / 79.5% origin"
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-24T22:26:11.069061+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml:25305:  eval-3dir-adaptive-spatial-s42:
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml:25331:      log_path: /root/acr-vla-conformal-refinement/logs/dirB_adaptive_spatial_s42.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml:25492:    parent: eval-3dir-adaptive-spatial-s42
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml:25508:  eval-supp-adapt-tau015-spatial-s42:
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml:25515:    parent: eval-3dir-adaptive-spatial-s42
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml:25531:  eval-supp-adapt-tau025-spatial-s42:
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml:25538:    parent: eval-3dir-adaptive-spatial-s42
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml:25554:  eval-supp-adapt-tau035-spatial-s42:
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml:25561:    parent: eval-3dir-adaptive-spatial-s42
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml:25626:  eval-adaptive-tau015-spatial-s42:
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml:25635:  eval-adaptive-tau025-spatial-s42:
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml:25644:  eval-adaptive-tau035-spatial-s42:
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml:25681:    parent: eval-3dir-adaptive-spatial-s42
/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-
…[truncated 4495 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_s42-adaptive-cross-run_20260524T222048",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-24T22:26:11.069204+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml",
  "offset": "25531",
  "limit": "90"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_s42-adaptive-cross-run_20260524T222048",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml",
    "offset": "25531",
    "limit": "90"
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-24T22:26:11.069401+00:00_

25531	  eval-supp-adapt-tau025-spatial-s42:
25532	    status: DONE
25533	    retry_count: 0
25534	    created_at: '2026-05-23T03:26:26.232Z'
25535	    updated_at: '2026-05-23T04:06:38.592Z'
25536	    hypothesis: Adaptive CRM with tau=0.25 (~P90) reduces trigger rate to ~20-30%
25537	      while maintaining SR, mapping the Pareto frontier of trigger_rate vs SR
25538	    parent: eval-3dir-adaptive-spatial-s42
25539	    spec:
25540	      command: CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py --mode adaptive_conformal_crm
25541	        --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt
25542	        --benchmark spatial --seed 42 --n_rollouts 20 --conformal_threshold 0.25
25543	      server: bjb1-32546
25544	      data_path: /root/acr-vla-conformal-refinement
25545	      data_count: 200
25546	      model_name: smolvla
25547	      seed: 42
25548	      checkpoint_source: /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt
25549	      eval_data: LIBERO-Spatial
25550	      gpu: cuda:2
25551	      pid: 626274
25552	    conclusion: killed
25553	    completed_at: '2026-05-23T04:06:38.592Z'
25554	  eval-supp-adapt-tau035-spatial-s42:
25555	    status: DONE
25556	    retry_count: 0
25557	    created_at: '2026-05-23T03:26:29.768Z'
25558	    updated_at: '2026-05-23T04:06:43.867Z'
25559	    hypothesis: Adaptive CRM with tau=0.35 (conservative, ~10% trigger rate) tests
25560	      whether very selective CRM application still provides benefit on LIBERO-Spatial
25561	    parent: eval-3dir-adaptive-spatial-s42
25562	    spec:
25563	      command: CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py --mode adaptive_conformal_crm
25564	        --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt
25565	        --benchmark spatial --seed 42 --n_rollouts 20 --conformal_threshold 0.35
25566	      server: bjb1-32546
25567	      data_path: /root/acr-vla-conformal-refinement
25568	      data_count: 200
25569	      model_name: smol
…[truncated 2219 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_s42-adaptive-cross-run_20260524T222048",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-24T22:26:11.069560+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml",
  "offset": "25764",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_s42-adaptive-cross-run_20260524T222048",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml",
    "offset": "25764",
    "limit": "80"
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-24T22:26:11.069715+00:00_

25764	  eval-supp-adapt-tau025-spatial-s42-r2:
25765	    status: DONE
25766	    retry_count: 0
25767	    created_at: '2026-05-23T04:11:39.644Z'
25768	    updated_at: '2026-05-23T06:12:07.119Z'
25769	    spec:
25770	      command: evaluate.py --mode adaptive_conformal_crm --conformal_threshold 0.25
25771	      server: bjb1-32546
25772	      gpu: cuda:2
25773	      pid: 665520
25774	      log_path: ~/runs/acr-vla-conformal-refinement/eval-supp-adapt-tau025-spatial-s42-r2.log
25775	      submitted_at: '2026-05-23T04:11:35.167Z'
25776	      submitted_via: submit_training_job
25777	      backend: tmux
25778	      account: root
25779	      data_path: /root/acr-vla-conformal-refinement
25780	      data_count: 200
25781	      model_name: smolvla
25782	      seed: 42
25783	      checkpoint_source: /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt
25784	      eval_data: LIBERO-Spatial
25785	      wall_clock_seconds: 7232.0
25786	      gpu_hours: 2.01
25787	    hypothesis: Adaptive CRM with tau=0.25 (~P90) reduces trigger rate to ~20-30%
25788	      while maintaining SR, mapping the Pareto frontier of trigger_rate vs SR
25789	    parent: eval-3dir-adaptive-spatial-s42
25790	    reproduce:
25791	      finished_at: '2026-05-23T06:07:08.463Z'
25792	    extra:
25793	      hook_events:
25794	      - event: on_complete
25795	        action: agent
25796	        ts: '2026-05-23T06:07:22.355725+00:00'
25797	    metrics:
25798	      overall_sr: 82
25799	      n_success: 164
25800	      n_total: 200
25801	      trigger_rate: 19.4
25802	      mean_unc: 0.1847
25803	      per_task_sr:
25804	        between_plate_and_ramekin: 95
25805	        next_to_ramekin: 95
25806	        from_table_center: 100
25807	        on_cookie_box: 100
25808	        in_top_drawer: 75
25809	        on_ramekin: 0
25810	        next_to_cookie_box: 90
25811	        on_stove: 90
25812	        next_to_plate: 90
25813	        on_wooden_cabinet: 85
25814	    log_path: /root/acr-vla-conformal-refinement/logs
…[truncated 1282 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_s42-adaptive-cross-run_20260524T222048",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-24T22:26:11.069873+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml",
  "offset": "31805",
  "limit": "85"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_s42-adaptive-cross-run_20260524T222048",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml",
    "offset": "31805",
    "limit": "85"
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-24T22:26:11.070032+00:00_

31805	  eval-adaptive-k1-spatial-tau025-s42:
31806	    status: PREPARING
31807	    retry_count: 0
31808	    created_at: '2026-05-24T15:11:16.467Z'
31809	    updated_at: '2026-05-24T18:12:40.045Z'
31810	    hypothesis: Adaptive CRM with K=1 (pure CRM correction when gating triggers, no
31811	      conformal selection) on Spatial τ=0.25. K=1 removes the multi-sample selection
31812	      benefit, isolating the CRM correction quality. Expected SR lower than K=2 if
31813	      conformal selection adds value.
31814	    spec:
31815	      command: bash -c "set -o pipefail; cd /root/acr-vla-conformal-refinement &&
31816	        python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt
31817	        --conformal_threshold 0.25 --benchmark spatial --seed 42 --n_rollouts 20 --max_correction_norm
31818	        0.2 --K 1 2>&1 | tee logs/eval-adaptive-k1-spatial-s42.log"
31819	      server: bjb1-32546
31820	      gpu:
31821	      - cuda:5
31822	      pid: '488687'
31823	      log_path: ~/runs/acr-vla-conformal-refinement/eval-adaptive-k1-spatial-tau025-s42.log
31824	      submitted_at: '2026-05-24T15:12:15.838Z'
31825	      submitted_via: submit_training_job
31826	      backend: tmux
31827	      account: root
31828	    conclusion: success
31829	    metrics:
31830	      overall_success_rate: 0.795
31831	      trigger_rate: 0.197
31832	      tau: 0.25
31833	      K: 1
31834	      benchmark: spatial
31835	      seed: 42
31836	  eval-adaptive-k5-spatial-tau025-s42:
31837	    status: PREPARING
31838	    retry_count: 0
31839	    created_at: '2026-05-24T15:11:21.960Z'
31840	    updated_at: '2026-05-24T16:55:43.337Z'
31841	    hypothesis: Adaptive CRM with K=5 (5 VLA samples when gating triggers, conformal
31842	      ranking selects best) on Spatial τ=0.25. K=5 vs K=2 tests whether more samples
31843	      improve selection quality. Diminishing returns expected if K=2 already captures
31844	      enough diversi
…[truncated 2225 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_s42-adaptive-cross-run_20260524T222048",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-24T22:26:11.070193+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -n \"K\\|--K\\|conformal_threshold\\|max_correction_norm\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/src/evaluate.py | head -40",
  "description": "Inspect evaluate.py defaults"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_s42-adaptive-cross-run_20260524T222048",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -n \"K\\|--K\\|conformal_threshold\\|max_correction_norm\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/src/evaluate.py | head -40",
    "description": "Inspect evaluate.py defaults"
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-24T22:26:11.070332+00:00_

grep: /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/src/evaluate.py: No such file or directory

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_s42-adaptive-cross-run_20260524T222048",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-24T22:26:11.070445+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/src/",
  "description": "List src directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_s42-adaptive-cross-run_20260524T222048",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/src/",
    "description": "List src directory"
  }
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-24T22:26:11.070554+00:00_

analysis
eval_a1_baseline.py
lerobot_native_precompute.py
lerobot_precompute.py

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_s42-adaptive-cross-run_20260524T222048",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-24T22:26:11.070675+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "grep -n \"default\\|add_argument.*K\\|add_argument.*max_correction\\|add_argument.*conformal_threshold\\|argparse\" /root/acr-vla-conformal-refinement/src/evaluate.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_s42-adaptive-cross-run_20260524T222048",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "grep -n \"default\\|add_argument.*K\\|add_argument.*max_correction\\|add_argument.*conformal_threshold\\|argparse\" /root/acr-vla-conformal-refinement/src/evaluate.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-24T22:26:11.070791+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_s42-adaptive-cross-run_20260524T222048",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-24T22:26:11.070901+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "grep -n -E \"add_argument.*--K|default=|--max_correction|--conformal\" /root/acr-vla-conformal-refinement/src/evaluate.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_s42-adaptive-cross-run_20260524T222048",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "grep -n -E \"add_argument.*--K|default=|--max_correction|--conformal\" /root/acr-vla-conformal-refinement/src/evaluate.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-24T22:26:11.071011+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_s42-adaptive-cross-run_20260524T222048",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-24T22:26:11.071118+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "grep -nE \"add_argument.--K|default=|--max_correction|--conformal\" /root/acr-vla-conformal-refinement/src/evaluate.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_s42-adaptive-cross-run_20260524T222048",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "grep -nE \"add_argument.--K|default=|--max_correction|--conformal\" /root/acr-vla-conformal-refinement/src/evaluate.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-24T22:26:11.071232+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: Shell metacharacter '|' not allowed in read-only mode. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_s42-adaptive-cross-run_20260524T222048",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-24T22:26:11.071364+00:00_

called mcp__agent-ml-research__ssh_read_only

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only</summary>

```json
{
  "server": "bjb1-32546",
  "command": "grep -n add_argument /root/acr-vla-conformal-refinement/src/evaluate.py",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_s42-adaptive-cross-run_20260524T222048",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "tool_args": {
    "server": "bjb1-32546",
    "command": "grep -n add_argument /root/acr-vla-conformal-refinement/src/evaluate.py",
    "account": "root"
  }
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-24T22:26:11.071516+00:00_

{"result":"{\"success\": true, \"data\": {\"stdout\": \"66:    p.add_argument(\\\"--benchmark\\\", type=str, default=\\\"object\\\",\\n68:    p.add_argument(\\\"--checkpoint\\\", type=str, default=None,\\n70:    p.add_argument(\\\"--crm_checkpoint\\\", type=str, default=None,\\n72:    p.add_argument(\\\"--n_rollouts\\\", type=int, default=20)\\n73:    p.add_argument(\\\"--max_steps\\\", type=int, default=300,\\n75:    p.add_argument(\\\"--seed\\\", type=int, default=42)\\n76:    p.add_argument(\\\"--K\\\", type=int, default=10)\\n77:    p.add_argument(\\\"--mode\\\", type=str, default=\\\"crm_perdof\\\",\\n79:    p.add_argument(\\\"--baseline_mode\\\", type=str, default=\\\"single\\\",\\n82:    p.add_argument(\\\"--smolvla_path\\\", type=str, default=\\\"/root/autodl-tmp/models/smolvla_libero/\\\")\\n83:    p.add_argument(\\\"--model\\\", type=str, default=\\\"smolvla\\\",\\n86:    p.add_argument(\\\"--pi05_path\\\", type=str,\\n89:    p.add_argument(\\\"--obs_dim\\\", type=int, default=OBS_DIM)\\n90:    p.add_argument(\\\"--unified_obs_dim\\\", type=int, default=None,\\n92:    p.add_argument(\\\"--hidden_dim\\\", type=int, default=256)\\n93:    p.add_argument(\\\"--task_filter\\\", type=str, default=None,\\n95:    p.add_argument(\\\"--render\\\", action=\\\"store_true\\\")\\n96:    p.add_argument(\\\"--output_file\\\", type=str, default=None,\\n98:    p.add_argument('--max_correction_norm', type=float, default=None,\\n100:    p.add_argument(\\\"--adaptive_k\\\", action=\\\"store_true\\\",\\n102:    p.add_argument(\\\"--adaptive_threshold\\\", type=float, default=0.1,\\n104:    p.add_argument(\\\"--k_init\\\", type=int, default=2,\\n106:    p.add_argument(\\\"--k_full\\\", type=int, default=5,\\n108:    p.add_argument(\\\"--unc_head_checkpoint\\\", type=str, default=None,\\n110:    p.add_argument(\\\"--unc_threshold\\\", type=float, default=0.5,\\n112:    p.add_argument(\\\"--conformal_threshold\\\", type=float, default=0.074855,\\n114:    p.add_argument(\\\"--n_act
…[truncated 142 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_s42-adaptive-cross-run_20260524T222048",
  "tool": "mcp__agent-ml-research__ssh_read_only",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 56 · 2026-05-24T22:26:11.071669+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml",
  "offset": "25626",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_s42-adaptive-cross-run_20260524T222048",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml",
    "offset": "25626",
    "limit": "80"
  }
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-24T22:26:11.071816+00:00_

25626	  eval-adaptive-tau015-spatial-s42:
25627	    status: DONE
25628	    retry_count: 0
25629	    created_at: '2026-05-23T03:38:26.202Z'
25630	    updated_at: '2026-05-23T04:50:11.299Z'
25631	    hypothesis: Adaptive conformal CRM with tau=0.15 adjusts correction trigger sensitivity,
25632	      finding optimal balance between correction frequency and accuracy on LIBERO-spatial
25633	    conclusion: killed
25634	    completed_at: '2026-05-23T04:50:11.299Z'
25635	  eval-adaptive-tau025-spatial-s42:
25636	    status: DONE
25637	    retry_count: 0
25638	    created_at: '2026-05-23T03:38:28.948Z'
25639	    updated_at: '2026-05-23T04:50:03.969Z'
25640	    hypothesis: Adaptive conformal CRM with tau=0.25 adjusts correction trigger sensitivity,
25641	      finding optimal balance between correction frequency and accuracy on LIBERO-spatial
25642	    conclusion: killed
25643	    completed_at: '2026-05-23T04:50:03.969Z'
25644	  eval-adaptive-tau035-spatial-s42:
25645	    status: DONE
25646	    retry_count: 0
25647	    created_at: '2026-05-23T03:38:32.825Z'
25648	    updated_at: '2026-05-23T04:49:53.623Z'
25649	    hypothesis: Adaptive conformal CRM with tau=0.35 adjusts correction trigger sensitivity,
25650	      finding optimal balance between correction frequency and accuracy on LIBERO-spatial
25651	    conclusion: killed
25652	    completed_at: '2026-05-23T04:49:53.623Z'
25653	  eval-supp-crm-norm02-spatial-s42-r2:
25654	    status: DONE
25655	    retry_count: 0
25656	    created_at: '2026-05-23T04:11:13.449Z'
25657	    updated_at: '2026-05-23T06:12:43.228Z'
25658	    spec:
25659	      command: bash -c "set -o pipefail; cd /root/acr-vla-conformal-refinement &&
25660	        python -u src/evaluate.py --mode crm_obs_only --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt
25661	        --benchmark spatial --seed 42 --n_rollouts 20 --max_correction_norm 0.2 2>&1
25662	        | tee logs/eval-supp-crm-norm02-spatial-s42-r2.log"
25663	      server:
…[truncated 1738 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_s42-adaptive-cross-run_20260524T222048",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-24T22:26:11.071972+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -nE \"k2.*spatial.*s42|spatial.*k2.*s42|K=2.*spatial|adapt.*spatial.*r3|spatial.*adapt.*r3\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml | head -30",
  "description": "Search K=2 spatial s42 runs in registry"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_s42-adaptive-cross-run_20260524T222048",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -nE \"k2.*spatial.*s42|spatial.*k2.*s42|K=2.*spatial|adapt.*spatial.*r3|spatial.*adapt.*r3\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml | head -30",
    "description": "Search K=2 spatial s42 runs in registry"
  }
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-24T22:26:11.072104+00:00_

26434:  eval-supp-reconvla-k2-spatial-s42:
26447:        --K 2 --benchmark spatial --seed 42 --n_rollouts 20 2>&1 | tee logs/eval-supp-reconvla-k2-spatial-s42.log"
26452:      log_path: /root/acr-vla-conformal-refinement/logs/eval-supp-reconvla-k2-spatial-s42.log
26770:  eval-supp-k2mean-spatial-s42:
26781:        spatial --seed 42 --n_rollouts 20 2>&1 | tee logs/eval-supp-k2mean-spatial-s42.log"
26786:      log_path: ~/runs/acr-vla-conformal-refinement/eval-supp-k2mean-spatial-s42.log
26821:    log_path: /root/acr-vla-conformal-refinement/logs/eval-supp-k2mean-spatial-s42.log
26973:    parent: eval-supp-reconvla-k2-spatial-s42
27014:    parent: eval-supp-reconvla-k2-spatial-s42
29580:  eval-supp-spatial-adapt-tau025-s45-r3:
33071:  eval-k2-tau010-spatial-s42:
33084:        0.2 --K 2 2>&1 | tee logs/eval-k2-tau010-spatial-s42.log"
33089:      log_path: ~/runs/acr-vla-conformal-refinement/eval-k2-tau010-spatial-s42.log
33094:  eval-k2-tau015-spatial-s42:
33101:  eval-k2-tau020-spatial-s42:
33114:        --K 2 2>&1 | tee logs/eval-k2-tau020-spatial-s42.log && echo '=== K=2 tau=0.25
33118:        --K 2 2>&1 | tee logs/eval-k2-tau025-spatial-s42.log"
33123:      log_path: ~/runs/acr-vla-conformal-refinement/eval-k2-tau020-spatial-s42.log
33128:  eval-k2-tau025-spatial-s42:
33135:  eval-k2-tau030-spatial-s42:
33147:        --K 2 2>&1 | tee logs/eval-k2-tau030-spatial-s42.log && echo '=== K=2 tau=0.35
33151:        --K 2 2>&1 | tee logs/eval-k2-tau035-spatial-s42.log"
33156:      log_path: ~/runs/acr-vla-conformal-refinement/eval-k2-tau030-spatial-s42.log
33161:  eval-k2-tau035-spatial-s42:
33168:  eval-k2-tau010-015-spatial-s42:
33180:        --K 2 2>&1 | tee logs/eval-k2-tau010-spatial-s42.log && echo '=== K=2 tau=0.15
33184:        --K 2 2>&1 | tee logs/eval-k2-tau015-spatial-s42.log"
33189:      log_path: ~/runs/acr-vla-conformal-refinement/eval-k2-tau010-015-spatial-s42.log

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_s42-adaptive-cross-run_20260524T222048",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 60 · 2026-05-24T22:26:11.072250+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml",
  "offset": "33128",
  "limit": "40"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_s42-adaptive-cross-run_20260524T222048",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml",
    "offset": "33128",
    "limit": "40"
  }
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-24T22:26:11.072440+00:00_

33128	  eval-k2-tau025-spatial-s42:
33129	    status: PREPARING
33130	    retry_count: 0
33131	    created_at: '2026-05-24T21:37:27.015Z'
33132	    updated_at: '2026-05-24T21:37:27.015Z'
33133	    hypothesis: 'K=2 τ-sweep: τ=0.25 Adaptive Conformal on Spatial s42. K=2 matches
33134	      Table 1 production setting.'
33135	  eval-k2-tau030-spatial-s42:
33136	    status: PREPARING
33137	    retry_count: 0
33138	    created_at: '2026-05-24T21:37:30.605Z'
33139	    updated_at: '2026-05-24T21:58:08.299Z'
33140	    hypothesis: 'K=2 τ-sweep: τ=0.30 Adaptive Conformal on Spatial s42. K=2 matches
33141	      Table 1 production setting.'
33142	    spec:
33143	      command: bash -c "cd /root/acr-vla-conformal-refinement && echo '=== K=2 tau=0.30
33144	        START ===' && python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint
33145	        /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold
33146	        0.30 --benchmark spatial --seed 42 --n_rollouts 20 --max_correction_norm 0.2
33147	        --K 2 2>&1 | tee logs/eval-k2-tau030-spatial-s42.log && echo '=== K=2 tau=0.35
33148	        START ===' && python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint
33149	        /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt --conformal_threshold
33150	        0.35 --benchmark spatial --seed 42 --n_rollouts 20 --max_correction_norm 0.2
33151	        --K 2 2>&1 | tee logs/eval-k2-tau035-spatial-s42.log"
33152	      server: bjb2-28827
33153	      gpu:
33154	      - cuda:1
33155	      pid: '475008'
33156	      log_path: ~/runs/acr-vla-conformal-refinement/eval-k2-tau030-spatial-s42.log
33157	      submitted_at: '2026-05-24T21:58:05.975Z'
33158	      submitted_via: submit_training_job
33159	      backend: tmux
33160	      account: root
33161	  eval-k2-tau035-spatial-s42:
33162	    status: PREPARING
33163	    retry_count: 0
33164	    created_at: '2026-05-24T21:37:34.357Z'
33165	    updated_at: '2026-05-24T21:
…[truncated 142 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_s42-adaptive-cross-run_20260524T222048",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 62 · 2026-05-24T22:26:11.072601+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/report.md",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_s42-adaptive-cross-run_20260524T222048",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/report.md",
    "limit": "80"
  }
}
```

</details>

---

### Tool result

_source line 63 · 2026-05-24T22:26:11.072743+00:00_

1	# Handover — 2026-05-24 21:00 UTC
2	
3	> 由 Agent 生成。硬限 150 行。
4	
5	## τ-sweep 结果（Spatial, seed=42）— 全部完成
6	| τ | SR | trigger_rate |
7	|---|-----|-------------|
8	| 0.10 | 79.0% | 75.2% |
9	| 0.15 | 80.5% | 40.7% |
10	| **0.20** | **81.0%** | **26.6%** |
11	| 0.25 | 79.5% | 19.6% |
12	| 0.30 | 80.5% | 16.7% |
13	| 0.35 | 80.0% | 12.2% |
14	
15	SR 平坦（2pp 波动），trigger_rate 随 τ 单调下降。τ=0.10 过度修正降 SR → 支持 D140 方案 C。
16	
17	## K-sweep（部分）
18	- K=1: SR=79.5% | K=5: 运行中 bjb2-40593 (7/10 tasks) | K=10: 默认值（见 τ-sweep）
19	
20	## Table 1 8-seed（art_20260524_7faa0d）
21	清洗后 Spatial Δ(A-V) p=0.0049。数据缺口正在填补中。
22	
23	## 运行中实验
24	| 服务器 | GPU | 实验 |
25	|--------|-----|------|
26	| bjb1-32546:0 | 0 | vla_only object s42 |
27	| bjb1-32546:2 | 2 | vla_only object s43 |
28	| bjb1-32546:3 | 3 | vla_only object s44 |
29	| bjb1-32546:4 | 4 | vla_only goal s42 |
30	| bjb1-32546:5 | 5 | vla_only long s43 |
31	| bjb2-28827:0 | 0 | CRM spatial s48 |
32	| bjb2-28827:4 | 4 | CRM spatial s49 |
33	| bjb2-28827:5 | 5 | CRM goal s48 |
34	| bjb2-28827:2 | 2 | π0.5 reconvla goal s42 |
35	| bjb2-28827:3 | 3 | π0.5 reconvla object s42 |
36	| bjb1-18228:1 | 1 | CRM object s48 |
37	| bjb1-18228:2 | 2 | CRM goal s49 |
38	| bjb1-18228:3 | 3 | precompute-pi05-long-2048-r2 (疑似僵尸) |
39	| bjb2-40593:0 | 0 | K=5 sweep (~50min) |
40	| cqa1-32758 | ? | 部署 Worker 运行中 |
41	
42	## ⚠️ 告警
43	- **π0.5 CRM 训练中断**：epoch 26 被平台 SIGKILL，best val_loss=0.004790 @ epoch 25。Worker 已派恢复。
44	- **precompute-pi05-long-2048-r2**：PID 114507，47h+，疑似僵尸。
45	- **GPU 空闲**：bjb1-32546:1, bjb2-28827:1 各 1 张空闲。
46	
47	## π0.5 Object s43
48	r4=98.5% 有效（chunked），v2=86.5% OOM 废结果。closed-loop 用 r3=81.5%。
49	
50	## 趋势
51	成功 496+ / 负向 75 / 失败 80+
52	
53	## 下一步
54	1. K=5 结果 → 完成 K-sweep
55	2. 收割 bjb1-32546 VLA-only → 补 Table 1 缺口
56	3. CRM 训练恢复 → π0.5 评估前置
57	4. cqa1-32758 部署确认
58	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_s42-adaptive-cross-run_20260524T222048",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 64 · 2026-05-24T22:26:11.072904+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -nE \"tau020-spatial-s42|tau030-spatial-s42|tau-sweep.*spatial\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml | head -20",
  "description": "Find tau-sweep entries for spatial s42"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_s42-adaptive-cross-run_20260524T222048",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -nE \"tau020-spatial-s42|tau030-spatial-s42|tau-sweep.*spatial\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml | head -20",
    "description": "Find tau-sweep entries for spatial s42"
  }
}
```

</details>

---

### Tool result

_source line 65 · 2026-05-24T22:26:11.073033+00:00_

31690:  eval-tau-sweep-spatial-tau010-s42:
31707:      log_path: ~/runs/acr-vla-conformal-refinement/eval-tau-sweep-spatial-tau010-s42.log
31719:  eval-tau-sweep-spatial-tau020-s42:
31731:        0.2 2>&1 | tee logs/eval-tau020-spatial-s42.log"
31736:      log_path: ~/runs/acr-vla-conformal-refinement/eval-tau-sweep-spatial-tau020-s42.log
31748:  eval-tau-sweep-spatial-tau030-s42:
31760:        0.2 2>&1 | tee logs/eval-tau030-spatial-s42.log"
31765:      log_path: ~/runs/acr-vla-conformal-refinement/eval-tau-sweep-spatial-tau030-s42.log
33101:  eval-k2-tau020-spatial-s42:
33114:        --K 2 2>&1 | tee logs/eval-k2-tau020-spatial-s42.log && echo '=== K=2 tau=0.25
33123:      log_path: ~/runs/acr-vla-conformal-refinement/eval-k2-tau020-spatial-s42.log
33135:  eval-k2-tau030-spatial-s42:
33147:        --K 2 2>&1 | tee logs/eval-k2-tau030-spatial-s42.log && echo '=== K=2 tau=0.35
33156:      log_path: ~/runs/acr-vla-conformal-refinement/eval-k2-tau030-spatial-s42.log

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_s42-adaptive-cross-run_20260524T222048",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 66 · 2026-05-24T22:26:11.073154+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml",
  "offset": "31690",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_s42-adaptive-cross-run_20260524T222048",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml",
    "offset": "31690",
    "limit": "100"
  }
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-24T22:26:11.073328+00:00_

31690	  eval-tau-sweep-spatial-tau010-s42:
31691	    status: PREPARING
31692	    retry_count: 0
31693	    created_at: '2026-05-24T15:11:02.885Z'
31694	    updated_at: '2026-05-24T18:12:12.445Z'
31695	    hypothesis: Adaptive CRM with τ=0.10 on Spatial (highest trigger rate ~20%) should
31696	      show high trigger rate (~70-80%) and potentially lower SR due to over-correction,
31697	      mapping the left side of the inverted-U τ curve already observed on Goal suite.
31698	    spec:
31699	      command: bash -c "set -o pipefail; cd /root/acr-vla-conformal-refinement &&
31700	        python -u src/evaluate.py --mode adaptive_conformal_crm --crm_checkpoint /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt
31701	        --conformal_threshold 0.10 --benchmark spatial --seed 42 --n_rollouts 20 --max_correction_norm
31702	        0.2 2>&1 | tee logs/eval-tau010-spatial-s42.log"
31703	      server: bjb1-32546
31704	      gpu:
31705	      - cuda:0
31706	      pid: '486799'
31707	      log_path: ~/runs/acr-vla-conformal-refinement/eval-tau-sweep-spatial-tau010-s42.log
31708	      submitted_at: '2026-05-24T15:11:50.901Z'
31709	      submitted_via: submit_training_job
31710	      backend: tmux
31711	      account: root
31712	    conclusion: success
31713	    metrics:
31714	      overall_success_rate: 0.79
31715	      trigger_rate: 0.752
31716	      tau: 0.1
31717	      benchmark: spatial
31718	      seed: 42
31719	  eval-tau-sweep-spatial-tau020-s42:
31720	    status: PREPARING
31721	    retry_count: 0
31722	    created_at: '2026-05-24T15:11:06.328Z'
31723	    updated_at: '2026-05-24T18:12:19.371Z'
31724	    hypothesis: Adaptive CRM with τ=0.20 on Spatial should be near the optimal range
31725	      (τ∈[0.15,0.25] from Goal sweep), confirming the inverted-U shape generalizes
31726	      across suites with different trigger rate distributions.
31727	    spec:
31728	      command: bash -c "set -o pipefail; cd /root/acr-vla-conformal-refinement &&
31729	        pyth
…[truncated 3046 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_s42-adaptive-cross-run_20260524T222048",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 68 · 2026-05-24T22:26:11.073499+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -nE \"tau025-spatial|tau-sweep.*tau025|tau-sweep.*025|tau-sweep-spatial\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml | head -30",
  "description": "All tau025 spatial entries"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_s42-adaptive-cross-run_20260524T222048",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -nE \"tau025-spatial|tau-sweep.*tau025|tau-sweep.*025|tau-sweep-spatial\" /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml | head -30",
    "description": "All tau025 spatial entries"
  }
}
```

</details>

---

### Tool result

_source line 69 · 2026-05-24T22:26:11.073633+00:00_

25531:  eval-supp-adapt-tau025-spatial-s42:
25635:  eval-adaptive-tau025-spatial-s42:
25764:  eval-supp-adapt-tau025-spatial-s42-r2:
25774:      log_path: ~/runs/acr-vla-conformal-refinement/eval-supp-adapt-tau025-spatial-s42-r2.log
25814:    log_path: /root/acr-vla-conformal-refinement/logs/eval-supp-adapt-tau025-spatial-s42-r2.log
26284:  eval-supp-adapt-tau025-spatial-s43:
26292:    parent: eval-supp-adapt-tau025-spatial-s42-r2
26297:        0.2 2>&1 | tee logs/eval-supp-adapt-tau025-spatial-s43.log"
26302:      log_path: ~/runs/acr-vla-conformal-refinement/eval-supp-adapt-tau025-spatial-s43.log
26343:  eval-supp-adapt-tau025-spatial-s44:
26351:    parent: eval-supp-adapt-tau025-spatial-s42-r2
26356:        0.2 2>&1 | tee logs/eval-supp-adapt-tau025-spatial-s44.log"
26361:      log_path: ~/runs/acr-vla-conformal-refinement/eval-supp-adapt-tau025-spatial-s44.log
26443:    parent: eval-supp-adapt-tau025-spatial-s42-r2
30331:  eval-supp-adapt-tau025-spatial-s45:
30355:      tmux_session: eval-supp-adapt-tau025-spatial-s45
30358:      log_path: /root/acr-vla-conformal-refinement/logs/eval-supp-adapt-tau025-spatial-s45.log
30560:  eval-supp-adapt-tau025-spatial-s46:
30669:  eval-supp-adapt-tau025-spatial-s47:
31441:      Table 1 canonical is eval-supp-adapt-tau025-spatial-s47 (3-suite, K=10, norm=0.2,
31690:  eval-tau-sweep-spatial-tau010-s42:
31707:      log_path: ~/runs/acr-vla-conformal-refinement/eval-tau-sweep-spatial-tau010-s42.log
31719:  eval-tau-sweep-spatial-tau020-s42:
31736:      log_path: ~/runs/acr-vla-conformal-refinement/eval-tau-sweep-spatial-tau020-s42.log
31748:  eval-tau-sweep-spatial-tau030-s42:
31765:      log_path: ~/runs/acr-vla-conformal-refinement/eval-tau-sweep-spatial-tau030-s42.log
31859:  eval-supp-adapt-tau025-spatial-s48:
31870:        0.2 2>&1 | tee logs/eval-supp-adapt-tau025-spatial-s48.log"
31875:      log_path: ~/runs/acr-vla-conformal-refinement/eval-supp-adapt-tau025-spatial-s48.log
31887:  eval-supp-adapt-tau025-spatial-s49:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_s42-adaptive-cross-run_20260524T222048",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 70 · 2026-05-24T22:26:11.073781+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml",
  "offset": "31430",
  "limit": "25"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_analysis_s42-adaptive-cross-run_20260524T222048",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/registry.yaml",
    "offset": "31430",
    "limit": "25"
  }
}
```

</details>

---

### Tool result

_source line 71 · 2026-05-24T22:26:11.073917+00:00_

31430	    metrics:
31431	      success_rate: 0.79
31432	      total_successes: 158
31433	      total_trials: 200
31434	      mean_uncertainty: 0.1835
31435	      trigger_rate: 0.188
31436	      tau: 0.25
31437	      total_steps: 28642
31438	      crm_applied_steps: 5381
31439	    notes: SUPPLEMENTARY VARIANT — NOT Table 1 canonical. 4-suite checkpoint (crm_unified_4suite_r4),
31440	      K=2, tau=0.25. SR=79.0% (158/200). Underperforms VLA-only (81%) on this seed.
31441	      Table 1 canonical is eval-supp-adapt-tau025-spatial-s47 (3-suite, K=10, norm=0.2,
31442	      SR=81.5%).
31443	  eval-supp-spatial-k2mean-s47:
31444	    status: DONE
31445	    retry_count: 0
31446	    created_at: '2026-05-24T10:58:53.820Z'
31447	    updated_at: '2026-05-24T13:40:18.329Z'
31448	    hypothesis: K=2 mean-of-samples VLA baseline on LIBERO-Spatial at seed 47 for
31449	      seed-extension coverage of the naive averaging baseline.
31450	    spec:
31451	      command: python -u src/evaluate.py --benchmark spatial --mode vla_only --baseline_mode
31452	        mean --seed 47 --n_rollouts 20 --K 2
31453	      server: cqa1-32758
31454	      data_path: LIBERO-Spatial

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_analysis_s42-adaptive-cross-run_20260524T222048",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 72 · 2026-05-24T22:26:11.074108+00:00_

# 调查结果

两个数字 **不是** 同一配置的两次独立 run — 它们的 **K 值不同**：

## Run 1: SR=82.0%
- **exp_id**: `eval-supp-adapt-tau025-spatial-s42-r2`
- **server/GPU**: bjb1-32546 / cuda:2
- **创建**: 2026-05-23T04:11:39 → 完成 06:12:07 (wall=7232s)
- **参数**: τ=0.25, **K=10 (默认，未显式传)**, max_correction_norm=0.2
- **metrics**: SR=82.0% (164/200), trigger_rate=19.4%, mean_unc=0.1847
- **command**:
  ```
  python -u src/evaluate.py --mode adaptive_conformal_crm \
    --crm_checkpoint .../crm_smolvla_3suite_v1/crm_best.pt \
    --benchmark spatial --seed 42 --n_rollouts 20 \
    --conformal_threshold 0.25 --max_correction_norm 0.2
  ```

## Run 2: SR=79.5%
- **exp_id**: `eval-adaptive-k1-spatial-tau025-s42`
- **server/GPU**: bjb1-32546 / cuda:5
- **创建**: 2026-05-24T15:11:16
- **参数**: τ=0.25, **K=1 (显式 --K 1)**, max_correction_norm=0.2
- **metrics**: SR=79.5%, trigger_rate=19.7%
- **command**: 同上但末尾加 `--K 1`，被论文 `experiments.tex:95` 用作 K=1 ablation

## 差异原因
**K 不同 (10 vs 1)**，不是随机性。`src/evaluate.py:76` 的 `--K` 默认值是 10。Δ=2.5pp 正是多样本 argmin-to-centroid 选择带来的增益，与 `experiments.tex:95` 主张「K=1=79.5% vs K=2=80.8%, Δ=+1.3pp」方向一致（K=10 比 K=2 多 1.2pp 进一步合理）。

## Table 1 使用：**Run 1 (82.0%)**
- 证据：`registry.yaml:31441` 明示「**Table 1 canonical** is `eval-supp-adapt-tau025-spatial-s47` (3-suite, **K=10**, norm=0.2)」——Table 1 canonical 配置就是 K=10
- s42 行对应 `eval-supp-adapt-tau025-spatial-s42-r2` (K=10)，SR=82.0%

## ⚠️ 发现的文档错误
`report.md:11` 的 τ-sweep 表里 τ=0.25 行写的是 **79.5% / 19.6%**——但这是 **K=1** 的数值，错填进了「默认 K=10」的 τ-sweep 表（其他 τ 值 0.10/0.20/0.30 都是 K=10：来自 `eval-tau-sweep-spatial-tau020-s42` 等，SR 81%/79%/80.5%）。正确的 τ=0.25 K=10 应为 **82.0% / 19.4%**。

## 建议
1. **Table 1 保留 82.0%** — 已锁定为 K=10 canonical，无需变更。
2. **修正 `report.md:11`**：τ=0.25 行改为 `82.0% / 19.4%`（引用 `eval-supp-adapt-tau025-spatial-s42-r2`）。
3. **不要取平均** — 这两个数字属于不同消融条件（K=10 vs K=1），平均没有物理意义。
4. 已提交的 `eval-k2-tau025-spatial-s42` (PREPARING, K=2) 完成后可补上 K=2 在该 seed 上的数值，让 K-sweep 完整。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_analysis_s42-adaptive-cross-run_20260524T222048"
}
```

</details>

---
