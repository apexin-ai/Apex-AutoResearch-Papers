# research supplementary checklist

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 37
- **Recorded user turns:** 0
- **Tool calls:** 18
- **Original source:** `logs/chats/worker_research_supplementary_checklist_20260528T191045.jsonl`
- **Structured JSON:** [`d5e5007775b3cf8989ca.json`](../../sessions/d5/d5e5007775b3cf8989ca.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

37 recorded events

### Tool call

_source line 1 · 2026-05-28T19:18:19.561471+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_supplementary_checklist_20260528T191045",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-28T19:18:19.561801+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_supplementary_checklist_20260528T191045",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-28T19:18:19.561969+00:00_

called mcp__agent-ml-research__read_registry

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry</summary>

```json
{
  "project": "diff_collision_sdf",
  "limit": "0",
  "fields": "['*']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_supplementary_checklist_20260528T191045",
  "tool": "mcp__agent-ml-research__read_registry",
  "tool_args": {
    "project": "diff_collision_sdf",
    "limit": "0",
    "fields": "['*']"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-28T19:18:19.562942+00:00_

Error: result (222,486 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-6/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-projects-diff-collision-sdf/8608f0d5-77a5-400c-a0d2-fb8a375305a9/tool-results/mcp-agent-ml-research-read_registry-1779995461020.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-6/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-projects-diff-collision-sdf/8608f0d5-77a5-400c-a0d2-fb8a375305a9/tool-results/mcp-agent-ml-research-read_registry-1779995461020.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-6/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-projects-diff-collision-sdf/8608f0d5-77a5-400c-a0d2-fb8a375305a9/tool-results/mcp-agent-ml-research-read_registry-1779995461020.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_supplementary_checklist_20260528T191045",
  "tool": "mcp__agent-ml-research__read_registry",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-28T19:18:19.563183+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Extract multi-seed experiments",
  "prompt": "You have a JSON file at `/home/ubuntu/.claude-account-6/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-projects-diff-collision-sdf/8608f0d5-77a5-400c-a0d2-fb8a375305a9/tool-results/mcp-agent-ml-research-read_registry-1779995461020.txt` containing the experiment registry for the diff_collision_sdf project. The file has schema `{result: string}` where `result` is a JSON-encoded string.\n\nYour task: Extract ALL multi-seed experiments. These are experiments whose exp_id contains \"seed\", \"s1\", \"s2\", \"s3\", or similar seed identifiers. \n\nSteps:\n1. First probe the structure with jq to understand the format\n2. Parse the nested JSON (result is a string containing JSON)\n3. Filter for experiments with conclusion=\"success\" that have seed-related identifiers in exp_id\n4. For each matching experiment, extract: exp_id, status, conclusion, metrics (especially CAR, TSR, dfCAR, or any collision/success rate metrics), config/description if available\n\nReturn the COMPLETE list of matching experiments with all their metrics in a structured format. Do not summarize or abbreviate - I need every experiment and every metric value.",
  "run_in_background": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_supplementary_checklist_20260528T191045",
  "tool": "Agent",
  "tool_args": {
    "description": "Extract multi-seed experiments",
    "prompt": "You have a JSON file at `/home/ubuntu/.claude-account-6/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-projects-diff-collision-sdf/8608f0d5-77a5-400c-a0d2-fb8a375305a9/tool-results/mcp-agent-ml-research-read_registry-1779995461020.txt` containing the experiment registry for the diff_collision_sdf project. The file has schema `{result: string}` where `result` is a JSON-encoded string.\n\nYour task: Extract ALL multi-seed experiments. These are experiments whose exp_id contains \"seed\", \"s1\", \"s2\", \"s3\", or similar seed identifiers. \n\nSteps:\n1. First probe the structure with jq to understand the format\n2. Parse the nested JSON (result is a string containing JSON)\n3. Filter for experiments with conclusion=\"success\" that have seed-related identifiers in exp_id\n4. For each matching experiment, extract: exp_id, status, conclusion, metrics (especially CAR, TSR, dfCAR, or any collision/success rate metrics), config/description if available\n\nReturn the COMPLETE list of matching experiments with all their metrics in a structured format. Do not summarize or abbreviate - I need every experiment and every metric value.",
    "run_in_background": "True"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-28T19:18:19.563354+00:00_

Async agent launched successfully.
agentId: a3f7f0682c7bb50c8 (internal ID - do not mention to user. Use SendMessage with to: 'a3f7f0682c7bb50c8' to continue this agent.)
The agent is working in the background. You will be notified automatically when it completes.
Do not duplicate this agent's work — avoid working with the same files or topics it is using. Work on non-overlapping tasks, or briefly tell the user what you launched and end your response.
output_file: /tmp/claude-1000/-home-ubuntu--agent-ml-research-be-idea-gen-0515-projects-diff-collision-sdf/8608f0d5-77a5-400c-a0d2-fb8a375305a9/tasks/a3f7f0682c7bb50c8.output
Do NOT Read or tail this file via the shell tool — it is the full sub-agent JSONL transcript and reading it will overflow your context. If the user asks for progress, say the agent is still running; you'll get a completion notification.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_supplementary_checklist_20260528T191045",
  "tool": "Agent",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-28T19:18:19.563529+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Extract eval-seed experiments",
  "prompt": "You have a JSON file at `/home/ubuntu/.claude-account-6/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-projects-diff-collision-sdf/8608f0d5-77a5-400c-a0d2-fb8a375305a9/tool-results/mcp-agent-ml-research-read_registry-1779995461020.txt` containing the experiment registry for the diff_collision_sdf project. The file has schema `{result: string}` where `result` is a JSON-encoded string.\n\nYour task: Extract ALL eval-seed experiments. These are experiments whose exp_id contains \"eseed\" or \"eval_seed\" or \"eval-seed\".\n\nSteps:\n1. First probe the structure with jq to understand the format\n2. Parse the nested JSON (result is a string containing JSON)\n3. Filter for experiments with eseed/eval_seed related identifiers in exp_id\n4. For each matching experiment, extract: exp_id, status, conclusion, ALL metrics, config/description if available\n\nReturn the COMPLETE list of matching experiments with all their metrics. Do not summarize - I need every experiment and every metric value.",
  "run_in_background": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_supplementary_checklist_20260528T191045",
  "tool": "Agent",
  "tool_args": {
    "description": "Extract eval-seed experiments",
    "prompt": "You have a JSON file at `/home/ubuntu/.claude-account-6/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-projects-diff-collision-sdf/8608f0d5-77a5-400c-a0d2-fb8a375305a9/tool-results/mcp-agent-ml-research-read_registry-1779995461020.txt` containing the experiment registry for the diff_collision_sdf project. The file has schema `{result: string}` where `result` is a JSON-encoded string.\n\nYour task: Extract ALL eval-seed experiments. These are experiments whose exp_id contains \"eseed\" or \"eval_seed\" or \"eval-seed\".\n\nSteps:\n1. First probe the structure with jq to understand the format\n2. Parse the nested JSON (result is a string containing JSON)\n3. Filter for experiments with eseed/eval_seed related identifiers in exp_id\n4. For each matching experiment, extract: exp_id, status, conclusion, ALL metrics, config/description if available\n\nReturn the COMPLETE list of matching experiments with all their metrics. Do not summarize - I need every experiment and every metric value.",
    "run_in_background": "True"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-28T19:18:19.563688+00:00_

Async agent launched successfully.
agentId: a7fe5ea45b29d2f01 (internal ID - do not mention to user. Use SendMessage with to: 'a7fe5ea45b29d2f01' to continue this agent.)
The agent is working in the background. You will be notified automatically when it completes.
Do not duplicate this agent's work — avoid working with the same files or topics it is using. Work on non-overlapping tasks, or briefly tell the user what you launched and end your response.
output_file: /tmp/claude-1000/-home-ubuntu--agent-ml-research-be-idea-gen-0515-projects-diff-collision-sdf/8608f0d5-77a5-400c-a0d2-fb8a375305a9/tasks/a7fe5ea45b29d2f01.output
Do NOT Read or tail this file via the shell tool — it is the full sub-agent JSONL transcript and reading it will overflow your context. If the user asks for progress, say the agent is still running; you'll get a completion notification.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_supplementary_checklist_20260528T191045",
  "tool": "Agent",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-28T19:18:19.563831+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Extract lambda/SDF experiments",
  "prompt": "You have a JSON file at `/home/ubuntu/.claude-account-6/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-projects-diff-collision-sdf/8608f0d5-77a5-400c-a0d2-fb8a375305a9/tool-results/mcp-agent-ml-research-read_registry-1779995461020.txt` containing the experiment registry for the diff_collision_sdf project. The file has schema `{result: string}` where `result` is a JSON-encoded string.\n\nYour task: Extract ALL lambda/SDF ablation experiments. These are experiments whose exp_id contains \"lambda\", \"lam\", \"sdf\", or whose description/config mentions lambda values like 0.005, 0.01, 0.1.\n\nSteps:\n1. First probe the structure with jq to understand the format\n2. Parse the nested JSON (result is a string containing JSON)\n3. Filter for experiments related to lambda/SDF ablation\n4. For each matching experiment, extract: exp_id, status, conclusion, ALL metrics, config/description, and importantly any lambda value information\n\nReturn the COMPLETE list of matching experiments with all their metrics and lambda values. Do not summarize - I need every experiment and every metric value.",
  "run_in_background": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_supplementary_checklist_20260528T191045",
  "tool": "Agent",
  "tool_args": {
    "description": "Extract lambda/SDF experiments",
    "prompt": "You have a JSON file at `/home/ubuntu/.claude-account-6/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-projects-diff-collision-sdf/8608f0d5-77a5-400c-a0d2-fb8a375305a9/tool-results/mcp-agent-ml-research-read_registry-1779995461020.txt` containing the experiment registry for the diff_collision_sdf project. The file has schema `{result: string}` where `result` is a JSON-encoded string.\n\nYour task: Extract ALL lambda/SDF ablation experiments. These are experiments whose exp_id contains \"lambda\", \"lam\", \"sdf\", or whose description/config mentions lambda values like 0.005, 0.01, 0.1.\n\nSteps:\n1. First probe the structure with jq to understand the format\n2. Parse the nested JSON (result is a string containing JSON)\n3. Filter for experiments related to lambda/SDF ablation\n4. For each matching experiment, extract: exp_id, status, conclusion, ALL metrics, config/description, and importantly any lambda value information\n\nReturn the COMPLETE list of matching experiments with all their metrics and lambda values. Do not summarize - I need every experiment and every metric value.",
    "run_in_background": "True"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-28T19:18:19.563989+00:00_

Async agent launched successfully.
agentId: ae8970a403bd10141 (internal ID - do not mention to user. Use SendMessage with to: 'ae8970a403bd10141' to continue this agent.)
The agent is working in the background. You will be notified automatically when it completes.
Do not duplicate this agent's work — avoid working with the same files or topics it is using. Work on non-overlapping tasks, or briefly tell the user what you launched and end your response.
output_file: /tmp/claude-1000/-home-ubuntu--agent-ml-research-be-idea-gen-0515-projects-diff-collision-sdf/8608f0d5-77a5-400c-a0d2-fb8a375305a9/tasks/ae8970a403bd10141.output
Do NOT Read or tail this file via the shell tool — it is the full sub-agent JSONL transcript and reading it will overflow your context. If the user asks for progress, say the agent is still running; you'll get a completion notification.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_supplementary_checklist_20260528T191045",
  "tool": "Agent",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-28T19:18:19.564133+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Extract oracle experiments",
  "prompt": "You have a JSON file at `/home/ubuntu/.claude-account-6/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-projects-diff-collision-sdf/8608f0d5-77a5-400c-a0d2-fb8a375305a9/tool-results/mcp-agent-ml-research-read_registry-1779995461020.txt` containing the experiment registry for the diff_collision_sdf project. The file has schema `{result: string}` where `result` is a JSON-encoded string.\n\nYour task: Extract ALL oracle-related experiments. These are experiments whose exp_id contains \"oracle\" or whose description mentions oracle.\n\nSteps:\n1. First probe the structure with jq to understand the format\n2. Parse the nested JSON (result is a string containing JSON)\n3. Filter for experiments related to oracle (oracle-adaptive, oracle-fixed, oracle-feature, etc.)\n4. For each matching experiment, extract: exp_id, status, conclusion, ALL metrics (especially per-task breakdown if available), config/description\n\nReturn the COMPLETE list of matching experiments with all their metrics. Do not summarize - I need every experiment and every metric value.",
  "run_in_background": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_supplementary_checklist_20260528T191045",
  "tool": "Agent",
  "tool_args": {
    "description": "Extract oracle experiments",
    "prompt": "You have a JSON file at `/home/ubuntu/.claude-account-6/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-projects-diff-collision-sdf/8608f0d5-77a5-400c-a0d2-fb8a375305a9/tool-results/mcp-agent-ml-research-read_registry-1779995461020.txt` containing the experiment registry for the diff_collision_sdf project. The file has schema `{result: string}` where `result` is a JSON-encoded string.\n\nYour task: Extract ALL oracle-related experiments. These are experiments whose exp_id contains \"oracle\" or whose description mentions oracle.\n\nSteps:\n1. First probe the structure with jq to understand the format\n2. Parse the nested JSON (result is a string containing JSON)\n3. Filter for experiments related to oracle (oracle-adaptive, oracle-fixed, oracle-feature, etc.)\n4. For each matching experiment, extract: exp_id, status, conclusion, ALL metrics (especially per-task breakdown if available), config/description\n\nReturn the COMPLETE list of matching experiments with all their metrics. Do not summarize - I need every experiment and every metric value.",
    "run_in_background": "True"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-28T19:18:19.564281+00:00_

Async agent launched successfully.
agentId: a1b8b45b91a289fcc (internal ID - do not mention to user. Use SendMessage with to: 'a1b8b45b91a289fcc' to continue this agent.)
The agent is working in the background. You will be notified automatically when it completes.
Do not duplicate this agent's work — avoid working with the same files or topics it is using. Work on non-overlapping tasks, or briefly tell the user what you launched and end your response.
output_file: /tmp/claude-1000/-home-ubuntu--agent-ml-research-be-idea-gen-0515-projects-diff-collision-sdf/8608f0d5-77a5-400c-a0d2-fb8a375305a9/tasks/a1b8b45b91a289fcc.output
Do NOT Read or tail this file via the shell tool — it is the full sub-agent JSONL transcript and reading it will overflow your context. If the user asks for progress, say the agent is still running; you'll get a completion notification.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_supplementary_checklist_20260528T191045",
  "tool": "Agent",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-28T19:18:19.564453+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Extract full experiment overview",
  "prompt": "You have a JSON file at `/home/ubuntu/.claude-account-6/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-projects-diff-collision-sdf/8608f0d5-77a5-400c-a0d2-fb8a375305a9/tool-results/mcp-agent-ml-research-read_registry-1779995461020.txt` containing the experiment registry for the diff_collision_sdf project. The file has schema `{result: string}` where `result` is a JSON-encoded string.\n\nYour tasks:\n1. First probe the structure with jq to understand the format\n2. Parse the nested JSON (result is a string containing JSON)\n3. Count total experiments, count by status and conclusion\n4. List ALL unique exp_id values grouped by conclusion (success vs others)\n5. For experiments with conclusion=success, list ALL of them with their exp_id and available metric names\n6. Check if any experiments have wandb_run_id or similar W&B tracking fields\n7. Check what fields are available in the experiment records (list all unique field names)\n\nReturn the COMPLETE overview. I need every exp_id, not just a sample.",
  "run_in_background": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_supplementary_checklist_20260528T191045",
  "tool": "Agent",
  "tool_args": {
    "description": "Extract full experiment overview",
    "prompt": "You have a JSON file at `/home/ubuntu/.claude-account-6/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-projects-diff-collision-sdf/8608f0d5-77a5-400c-a0d2-fb8a375305a9/tool-results/mcp-agent-ml-research-read_registry-1779995461020.txt` containing the experiment registry for the diff_collision_sdf project. The file has schema `{result: string}` where `result` is a JSON-encoded string.\n\nYour tasks:\n1. First probe the structure with jq to understand the format\n2. Parse the nested JSON (result is a string containing JSON)\n3. Count total experiments, count by status and conclusion\n4. List ALL unique exp_id values grouped by conclusion (success vs others)\n5. For experiments with conclusion=success, list ALL of them with their exp_id and available metric names\n6. Check if any experiments have wandb_run_id or similar W&B tracking fields\n7. Check what fields are available in the experiment records (list all unique field names)\n\nReturn the COMPLETE overview. I need every exp_id, not just a sample.",
    "run_in_background": "True"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-28T19:18:19.564617+00:00_

Async agent launched successfully.
agentId: aed76e128c9bc2d16 (internal ID - do not mention to user. Use SendMessage with to: 'aed76e128c9bc2d16' to continue this agent.)
The agent is working in the background. You will be notified automatically when it completes.
Do not duplicate this agent's work — avoid working with the same files or topics it is using. Work on non-overlapping tasks, or briefly tell the user what you launched and end your response.
output_file: /tmp/claude-1000/-home-ubuntu--agent-ml-research-be-idea-gen-0515-projects-diff-collision-sdf/8608f0d5-77a5-400c-a0d2-fb8a375305a9/tasks/aed76e128c9bc2d16.output
Do NOT Read or tail this file via the shell tool — it is the full sub-agent JSONL transcript and reading it will overflow your context. If the user asks for progress, say the agent is still running; you'll get a completion notification.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_supplementary_checklist_20260528T191045",
  "tool": "Agent",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-28T19:18:19.565219+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_supplementary_checklist_20260528T191045",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-28T19:18:19.565394+00:00_

artifacts/report_sdf_extraction.md
artifacts/report_safelibero.md
artifacts/report_vla_codebase.md
artifacts/kg3_gradient_toy_test.py
artifacts/report_kg3_gradient_test.md
artifacts/src/sdf_decoder.py
artifacts/src/sdf_gradient_refiner.py
artifacts/src/sdf_data.py
artifacts/src/train_colliforce.py
artifacts/src/__init__.py
artifacts/src/__pycache__/__init__.cpython-314.pyc
artifacts/src/__pycache__/sdf_decoder.cpython-314.pyc
artifacts/report_env_setup_kg1_kg2.md
artifacts/src/__pycache__/sdf_gradient_refiner.cpython-314.pyc
artifacts/src/__pycache__/sdf_data.cpython-314.pyc
artifacts/src/__pycache__/train_colliforce.cpython-314.pyc
artifacts/literature_review.md
artifacts/train_baseline.py
artifacts/report_baseline_prep.md
artifacts/report_openpi_deploy.md
artifacts/report_data_pipeline.md
artifacts/report_a1_integration.md
artifacts/comprehensive_fix_report.txt
artifacts/_project/report/baseline_weight_fix_report.md
artifacts/_project/report/urgent_fix_report_20260520.md
artifacts/train_a1_hook.py
artifacts/fix_a3.py
artifacts/fix_a1.py
artifacts/_project/report/training_progress_20260520_1020.md
artifacts/training_progress_20260520_1020.md
artifacts/_project/report/related_work_outline.md
artifacts/related_work_outline.md
artifacts/_project/paper/method_draft.md
artifacts/method_draft.md
artifacts/_project/paper/introduction.tex
artifacts/_project/paper/method.tex
artifacts/drafts/method.tex
artifacts/_project/paper/related_work.tex
artifacts/drafts/experiments.tex
artifacts/drafts/abstract.tex
artifacts/drafts/conclusion.tex
artifacts/drafts/introduction.tex
artifacts/drafts/related_work.tex
artifacts/_project/report/a3_lora_fix_result.json
artifacts/a3_lora_fix_result.json
artifacts/worker_output.md
artifacts/worker_report_westd45947_status.md
artifacts/eval_safelibero.py
artifacts/report_eval_tsr_zero_fix.md
artifacts/report_action_scale_fix.md
artifacts/diagnose_eval_a3_v11_object.md
artifacts/eval_a3_v11_object/report/diagnose_eval_a3_v11_object.md
artifacts
…[truncated 2360 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_supplementary_checklist_20260528T191045",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-28T19:18:19.565599+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "artifacts/_project/**/*.{md,tex,json}",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_supplementary_checklist_20260528T191045",
  "tool": "Glob",
  "tool_args": {
    "pattern": "artifacts/_project/**/*.{md,tex,json}",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-28T19:18:19.565752+00:00_

artifacts/_project/report/baseline_weight_fix_report.md
artifacts/_project/report/urgent_fix_report_20260520.md
artifacts/_project/report/training_progress_20260520_1020.md
artifacts/_project/report/related_work_outline.md
artifacts/_project/paper/method_draft.md
artifacts/_project/paper/introduction.tex
artifacts/_project/paper/method.tex
artifacts/_project/paper/related_work.tex
artifacts/_project/report/a3_lora_fix_result.json
artifacts/_project/report/analysis_m026_m027_m028_gradient_refine_diagnosis.md
artifacts/_project/report/pi05_a1_sdf_feasibility_report.md
artifacts/_project/report/pi05_collision_analysis_report.md
artifacts/_project/report/related_work_survey.md
artifacts/_project/report/step7k_overfit_check.md
artifacts/_project/report/lambda0_phase2_ablation_design.md
artifacts/_project/report/task0_vs_task1_collapse_analysis.md
artifacts/_project/report/mid_eval_d012_step10k_results.md
artifacts/_project/report/eval_commands_d012_final.md
artifacts/_project/report/task3_car_degradation_analysis.md
artifacts/_project/data/task3_collision_matrix_step10k.md
artifacts/_project/report/metric_definitions_e59531.md
artifacts/_project/report/metric_definitions.md
artifacts/_project/report/ssh_recovery_execution_plan.md
artifacts/_project/report/paper_data_summary.md
artifacts/_project/paper/analysis_claim1.tex
artifacts/_project/paper/analysis_claim2.tex
artifacts/_project/paper/analysis_claim3.tex
artifacts/_project/paper/experimental_framework.tex
artifacts/_project/paper/introduction_v2.tex
artifacts/_project/paper/abstract_v2.tex
artifacts/_project/paper/related_work_v2.tex
artifacts/_project/report/negative_results_analysis.md
artifacts/_project/paper/section5_5_method_boundaries.md
artifacts/_project/report/claim2_coverage_audit.md
artifacts/_project/report/related_work_update_20260525.md
artifacts/_project/report/report_pi0_baseline_fake_rate.md
artifacts/_project/report/negative_results_classification.md
artifacts/_project/data/paper_data_summary.md
ar
…[truncated 444 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_supplementary_checklist_20260528T191045",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-28T19:18:19.565895+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "artifacts/_project/chart/*",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_supplementary_checklist_20260528T191045",
  "tool": "Glob",
  "tool_args": {
    "pattern": "artifacts/_project/chart/*",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-28T19:18:19.566025+00:00_

artifacts/_project/chart/fig_oracle_bar.pdf
artifacts/_project/chart/fig_displacement_hist.pdf
artifacts/_project/chart/fig_tsr_car_scatter.pdf
artifacts/_project/chart/tsr_collapse_figures_index.md
artifacts/_project/chart/fig2_ee_displacement_distribution.pdf
artifacts/_project/chart/fig3_tsr_car_scatter.pdf
artifacts/_project/chart/fig5_lambda_curve.pdf
artifacts/_project/chart/fig_threshold_sensitivity.pdf
artifacts/_project/chart/fig_threshold_sensitivity_7fcb7e.pdf
artifacts/_project/chart/fig5_lambda_curve_5f2325.pdf
artifacts/_project/chart/fig5_lambda_curve_4bb269.pdf
artifacts/_project/chart/fig1_teaser.pdf
artifacts/_project/chart/fig5_lambda_curve.png
artifacts/_project/chart/fig1_teaser_v2.pdf
artifacts/_project/chart/fig1_teaser_v2.png
artifacts/_project/chart/fig1_teaser_v2_b523ab.png
artifacts/_project/chart/fig1_teaser_d60106.pdf
artifacts/_project/chart/fig5_lambda_car_v4.png
artifacts/_project/chart/fig_pertask_car_fingerprint.png
artifacts/_project/chart/fig_pertask_car_fingerprint_da36d3.png
artifacts/_project/chart/fig2_plan_a.png
artifacts/_project/chart/fig2_plan_b.png
artifacts/_project/chart/fig_overview.pdf
artifacts/_project/chart/fig_overview_pb.png
artifacts/_project/chart/fig_overview_pb_v2.png
artifacts/_project/chart/fig_overview_pb_v4.png
artifacts/_project/chart/fig_overview_pb_v5.png
artifacts/_project/chart/fig_overview_pb_v6.png
artifacts/_project/chart/fig_overview_pb_v7.png
artifacts/_project/chart/fig_overview_pb_v8.png
artifacts/_project/chart/fig_overview_pb_v9.png
artifacts/_project/chart/fig_overview_pb_v10.png
artifacts/_project/chart/fig_overview_pb_v11.png
artifacts/_project/chart/fig_overview_pb_v12.png
artifacts/_project/chart/fig_overview_pb_v13.png

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_supplementary_checklist_20260528T191045",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-28T19:18:19.566160+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "artifacts/_project/data/*",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_supplementary_checklist_20260528T191045",
  "tool": "Glob",
  "tool_args": {
    "pattern": "artifacts/_project/data/*",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-28T19:18:19.566283+00:00_

artifacts/_project/data/task3_collision_matrix_step10k.md
artifacts/_project/data/eval_safelibero_openvla.py
artifacts/_project/data/displacement_analysis_30k_summary.txt
artifacts/_project/data/paper_data_summary.md
artifacts/_project/data/threshold_sensitivity.csv
artifacts/_project/data/claim3_data_summary.md
artifacts/_project/data/ssr_analysis.md
artifacts/_project/data/fig5_lambda_data.csv
artifacts/_project/data/permutation_test.py
artifacts/_project/data/permutation_test_results.txt

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_supplementary_checklist_20260528T191045",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-28T19:18:19.566402+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "artifacts/**/*.{pdf,png}",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_supplementary_checklist_20260528T191045",
  "tool": "Glob",
  "tool_args": {
    "pattern": "artifacts/**/*.{pdf,png}",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-28T19:18:19.566570+00:00_

artifacts/_project/chart/fig_oracle_bar.pdf
artifacts/_project/chart/fig_displacement_hist.pdf
artifacts/_project/chart/fig_tsr_car_scatter.pdf
artifacts/dream_reports/dream_20260525T223036/best/paper.pdf
artifacts/dream_reports/dream_20260525T223036/median/paper.pdf
artifacts/dream_reports/dream_20260525T223036/worst/paper.pdf
artifacts/threshold_sensitivity/ee_displacement_combined.png
artifacts/threshold_sensitivity/sensitivity_curves.png
artifacts/threshold_sensitivity/ee_displacement_distribution.png
artifacts/dream_reports/dream_20260526T023936/best/paper.pdf
artifacts/dream_reports/dream_20260526T023936/median/paper.pdf
artifacts/dream_reports/dream_20260526T023936/worst/paper.pdf
artifacts/_project/chart/fig2_ee_displacement_distribution.pdf
artifacts/_project/chart/fig3_tsr_car_scatter.pdf
artifacts/figures/fig3_tsr_car_scatter.pdf
artifacts/figures/fig3_tsr_car_scatter.png
artifacts/_project/chart/fig5_lambda_curve.pdf
artifacts/_project/chart/fig_threshold_sensitivity.pdf
artifacts/_project/chart/fig_threshold_sensitivity_7fcb7e.pdf
artifacts/figures/fig_threshold_sensitivity.pdf
artifacts/figures/fig_threshold_sensitivity.png
artifacts/_project/chart/fig5_lambda_curve_5f2325.pdf
artifacts/_project/paper/paper_draft.pdf
artifacts/paper_draft.pdf
artifacts/_project/chart/fig5_lambda_curve_4bb269.pdf
artifacts/_project/chart/fig1_teaser.pdf
artifacts/_project/chart/fig5_lambda_curve.png
artifacts/_project/chart/fig1_teaser_v2.pdf
artifacts/_project/chart/fig1_teaser_v2.png
artifacts/_project/chart/fig1_teaser_v2_b523ab.png
artifacts/fig1_teaser_v1.png
artifacts/fig1_teaser_v2.png
artifacts/fig1_teaser_v3.png
artifacts/fig1_teaser_v4.png
artifacts/fig1_teaser_v5.png
artifacts/_project/chart/fig1_teaser_d60106.pdf
artifacts/fig1_teaser.png
artifacts/fig1_teaser.pdf
artifacts/_project/chart/fig5_lambda_car_v4.png
artifacts/_project/chart/fig_pertask_car_fingerprint.png
artifacts/_project/paper/fallback_2seed.pdf
artifacts/_project/chart/fig_pertask_car_fingerp
…[truncated 2854 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_supplementary_checklist_20260528T191045",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-28T19:18:19.566742+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/_project/data/paper_data_summary.md",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_supplementary_checklist_20260528T191045",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/_project/data/paper_data_summary.md",
    "limit": "80"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-28T19:18:19.566907+00:00_

1	# Paper Data Summary — diff_collision_sdf
2	
3	> 生成时间: 2026-05-26
4	> 数据来源: registry (status=DONE, conclusion=success/negative 中已确认的指标)
5	> 标记说明: ✅ 已确认 | ⏳ 待收集 | 🔧 displacement-fixed eval
6	
7	---
8	
9	## Table 1: Pi0.5+A1 SDF 训练结果矩阵
10	
11	所有实验 n_episodes=200。
12	
13	### λ=0.005
14	
15	| Seed | Ckpt | Step | avg_TSR | avg_CAR | avg_ee_disp | fake_safe% | frozen | exp_id | 备注 |
16	|------|------|------|---------|---------|-------------|------------|--------|--------|------|
17	| 0 | 30K | 30K | 5.5 | 50.0 | 0.0433¹ | — | — | eval_pi05_a1_30k_s0_l005 | ✅ 旧脚本,obstacle disp |
18	| 0 | 30K | 30K | 7.5 | 47.0 | 0.0485¹ | — | — | eval_pi05_a1_30k_s0_l005_r4 | ✅ retry,旧脚本 |
19	| 0 | best | — | — | — | — | — | — | — | ⏳ seed0 无 best/ ckpt (训练未保存) |
20	| 1 | 30K | 30K | 4.0 | 54.0 | 0.4955 | **0%** | **No** | eval_pi05_a1_30k_s1_l005_disp | ✅🔧 displacement-fixed |
21	| 1 | 30K | 30K | 5.5 | 52.5 | — | — | — | eval_pi05_a1_30k_s1_l005_v2 | ✅ 无 disp 数据 |
22	| 1 | 30K | 30K | 4.0 | 51.5 | — | — | — | eval_pi05_a1_30k_s1_l005_v3 | ✅ v4 rerun |
23	| 1 | best | 16K | 6.5 | 53.0 | 0.37~0.65² | **0%** | **No** | eval_pi05_a1_best_s1_l005_16k | ✅🔧 has ee_disp |
24	| 2 | 30K | 30K | 9.5 | 54.5 | — | — | — | eval_pi05_a1_30k_s2_l005_v2 | ✅ |
25	| 2 | 30K | 30K | 9.0 | 53.0 | — | — | — | eval_pi05_a1_30k_s2_l005_v3 | ✅ v4 rerun |
26	| 2 | best | 10K | 9.0 | 55.5 | 0.5046 | **0%** | **No** | eval_pi05_a1_best_s2_l005_10k | ✅🔧 displacement-fixed |
27	
28	¹ obstacle displacement (旧脚本), 非 ee_displacement
29	² per-task ee_disp: task0=0.5179, task1=0.5146, task2=0.6475, task3=0.3707
30	
31	### λ=0.01
32	
33	| Seed | Ckpt | Step | avg_TSR | avg_CAR | avg_ee_disp | fake_safe% | frozen | exp_id | 备注 |
34	|------|------|------|---------|---------|-------------|------------|--------|--------|------|
35	| 0 | 30K | 30K | 5.5 | 53.0 | 0.0297¹ | — | — | eval_pi05_a1_30k_s0_l01 | ✅ 旧脚本,obstacle disp |
36	| 0 | 30K | 30K | 6.5 | 52.5 | 0.4725 | **0%** | **No** | eval_pi05_a1_30k_s0_l01_disp | ✅🔧 disp
…[truncated 1641 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_supplementary_checklist_20260528T191045",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-28T19:18:19.567064+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/_project/data/claim3_data_summary.md",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_supplementary_checklist_20260528T191045",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/_project/data/claim3_data_summary.md",
    "limit": "80"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-28T19:18:19.567223+00:00_

1	# Claim 3: Avoidance Source Diagnosis — Data Summary
2	
3	## 1A. Main Summary Table
4	
5	| Condition | Seeds | CAR (per-seed) | CAR mean±std | TSR mean±std | dfCAR | frozen | EE Disp (m) |
6	|-----------|-------|----------------|--------------|--------------|-------|--------|-------------|
7	| Pi0.5 baseline | 3 | — | 26.8±1.6% | 74.7±1.5% | — | 0% | 0.367 |
8	| LoRA-only | 2 | s0=56.5, s1=52.5 | 54.5±2.83% | 51.5% | 54.5% | 0% | 0.392 |
9	| SDF λ=0.005 | 3 | s0=57.0, s1=54.0, s2=52.5 | 54.5±2.29% | 54.0±3.0% | 54.5% | 0% | 0.387 |
10	| SDF λ=0.01 | 3 | s0=57.0, s1=57.5, s2=54.5 | 56.3±1.61% | 53.8±1.5% | 56.3% | 0% | 0.389 |
11	| SDF λ=0.1 (20K) | 2 | s0=55, s1=56 | 55.5±0.71% | 52.5% | — | 0% | — |
12	| SDF λ=0.1 (30K) | — | pending | pending | pending | — | — | — |
13	
14	### Null Distribution
15	
16	Pooled from LoRA-only (2 seeds) + λ=0.005 (3 seeds) = 5 values: 56.5, 52.5, 57.0, 54.0, 52.5
17	
18	- **mean = 54.5%**, **σ = 2.15%**
19	
20	### Key Comparisons
21	
22	| Comparison | Δ vs null | σ units | p-value | Verdict |
23	|------------|-----------|---------|---------|---------|
24	| λ=0.01 mean (56.3%) vs null | +1.8pp | +0.84σ | >0.1 | not significant |
25	| λ=0.1 20K mean (55.5%) vs null | +1.0pp | +0.47σ | >0.1 | within null |
26	| Phase 2 ablation (λ=0 after 5K): 57.5% vs null | +3.0pp | +1.40σ | ~0.08 | within null |
27	
28	All SDF conditions fall within the null distribution range.
29	
30	---
31	
32	## 1B. Per-Task Breakdown
33	
34	### TSR per-task (from appendix.tex Table tab:per_task_tsr)
35	
36	| Task | Pi0.5 base | LoRA-only (2s mean) | SDF 0.005 (3s mean) | SDF 0.01 (3s mean) |
37	|------|-----------|---------------------|----------------------|---------------------|
38	| Orange Juice | 70.7 | 33.0 | 33.3 | 24.7 |
39	| Choco Pudding | 86.0 | 68.0 | 78.0 | 76.7 |
40	| Milk | 66.0 | 46.0 | 35.3 | 48.7 |
41	| BBQ Sauce | 76.0 | 59.0 | 69.3 | 65.3 |
42	
43	> **Note**: These are **TSR** values, not CAR. Source: appendix.tex Table tab:per_task_tsr.
44	
4
…[truncated 1573 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_supplementary_checklist_20260528T191045",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-28T19:18:19.567386+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/_project/data/permutation_test_results.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_supplementary_checklist_20260528T191045",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/_project/data/permutation_test_results.txt"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-28T19:18:19.567756+00:00_

1	======================================================================
2	  EXACT PERMUTATION TEST — treatment size = 2
3	======================================================================
4	
5	Null group (n=6):
6	  LoRA-only s0=57           = 57
7	  LoRA-only s1=52.5         = 52.5
8	  LoRA-only s2=55           = 55
9	  λ=0.005 s0=57             = 57
10	  λ=0.005 s1=54             = 54
11	  λ=0.005 s2=52.5           = 52.5
12	  Mean = 54.6667
13	
14	Treatment group (n=2):
15	  λ=0.1 s0=58               = 58
16	  λ=0.1 s1=58.5             = 58.5
17	  Observed mean = 58.2500
18	
19	Pool size = 8, C(8,2) = 28
20	Overall pool mean = 55.5625
21	
22	----------------------------------------------------------------------
23	All combinations (treatment draws) and their means:
24	----------------------------------------------------------------------
25	    1. (57, 52.5                      )  mean=54.7500
26	    2. (57, 55                        )  mean=56.0000
27	    3. (57, 57                        )  mean=57.0000
28	    4. (57, 54                        )  mean=55.5000
29	    5. (57, 52.5                      )  mean=54.7500
30	    6. (57, 58                        )  mean=57.5000
31	    7. (57, 58.5                      )  mean=57.7500
32	    8. (52.5, 55                      )  mean=53.7500
33	    9. (52.5, 57                      )  mean=54.7500
34	   10. (52.5, 54                      )  mean=53.2500
35	   11. (52.5, 52.5                    )  mean=52.5000
36	   12. (52.5, 58                      )  mean=55.2500
37	   13. (52.5, 58.5                    )  mean=55.5000
38	   14. (55, 57                        )  mean=56.0000
39	   15. (55, 54                        )  mean=54.5000
40	   16. (55, 52.5                      )  mean=53.7500
41	   17. (55, 58                        )  mean=56.5000
42	   18. (55, 58.5                      )  mean=56.7500
43	   19. (57, 54                        )  mean=55.5000
44	   20. (57, 52.5                      )  mean=54.7500
45
…[truncated 41889 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_supplementary_checklist_20260528T191045",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-28T19:18:19.567930+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/_project/data/ssr_analysis.md",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_supplementary_checklist_20260528T191045",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/_project/data/ssr_analysis.md",
    "limit": "50"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-28T19:18:19.568083+00:00_

1	# SSR (Safe Success Rate) Analysis
2	# Computed 2026-05-27 by worker_analysis_ssr_computation_20260527T113223
3	# SSR = (success AND no_collision) / total_episodes
4	
5	## Per-seed SSR Table
6	
7	| Condition | TSR (ep-level) | CR (collision rate) | CAR (1-CR) | SSR | n_episodes |
8	|-----------|---------------|--------------------|-----------:|----:|----------:|
9	| Pi0.5 baseline | 71.5% | 71.5% | 28.5% | 28.0% | 200 |
10	| LoRA s0 30K | 51.5% | 43.5% | 56.5% | 29.5% | 200 |
11	| LoRA s1 30K | 51.5% | 47.5% | 52.5% | 27.0% | 200 |
12	| SDF lambda=0.005 s0 | 55.5% | 43.0% | 57.0% | 30.0% | 200 |
13	| SDF lambda=0.005 s1 | 50.5% | 46.0% | 54.0% | 24.0% | 200 |
14	| SDF lambda=0.005 s2 | 56.0% | 47.5% | 52.5% | 29.5% | 200 |
15	| SDF lambda=0.01 s0 | 52.5% | 43.0% | 57.0% | 32.5% | 200 |
16	| SDF lambda=0.01 s1 | 55.5% | 42.5% | 57.5% | 30.0% | 200 |
17	| SDF lambda=0.01 s2 | 53.5% | 45.5% | 54.5% | 28.0% | 200 |
18	| SDF lambda=0.1 s0 | — | — | — | — | JSON overwritten |
19	| SDF lambda=0.1 s1 | 49.0% | 41.5% | 58.5% | 26.5% | 200 |
20	
21	## Condition Averages
22	
23	| Condition | Avg TSR | Avg CAR | Avg SSR | SSR/TSR |
24	|-----------|---------|---------|---------|---------|
25	| Pi0.5 baseline | 71.5% | 28.5% | 28.0% | 0.392 |
26	| LoRA (2 seeds) | 51.5% | 54.5% | 28.3% | 0.549 |
27	| SDF lambda=0.005 (3 seeds) | 54.0% | 54.5% | 27.8% | 0.515 |
28	| SDF lambda=0.01 (3 seeds) | 53.8% | 56.3% | 30.2% | 0.561 |
29	| SDF lambda=0.1 (1 seed only) | 49.0% | 58.5% | 26.5% | 0.541 |
30	
31	## Key Finding: SSR/TSR ratio refutes "reduced exposure"
32	
33	Under "reduced exposure" hypothesis: model simply does fewer things → SSR/TSR ≈ constant.
34	Observed: SSR/TSR jumps from 0.39 (baseline) to ~0.55 (all trained models).
35	This means a higher fraction of successful episodes are collision-free after training.
36	
37	## Caveats
38	- Worker's original "CAR" column was collision RATE (not avoidance rate). Corrected above.
39	- SDF lambda=0.1 s0 JSON overwritten by reeval_lora
…[truncated 338 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_supplementary_checklist_20260528T191045",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-28T19:18:19.568295+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/supplementary_checklist.md",
  "content": "# Supplementary Material Checklist\n\n> Generated: 2026-05-28\n> Source: 131 experiments in registry (72 success, 25 negative, 18 failed, 16 killed)\n> Authoritative eval pipeline: `reeval_*` series (rotation-fixed, eval_seed=7, n=200 episodes)\n\n---\n\n## S1. Multi-Seed Complete Results (Table)\n\n### S1a. Main Results: CAR across conditions (reeval, rotation-fixed)\n\n| Condition | Seed 0 | Seed 1 | Seed 2 | Mean±Std |\n|-----------|--------|--------|--------|----------|\n| LoRA-only | 57.0 | 52.5 | 55.0* | 54.8±2.3 |\n| SDF λ=0.005 | 57.0 | 54.0 | 52.5 | 54.5±2.3 |\n| SDF λ=0.01 | 57.0 | 57.5 | 54.5 | 56.3±1.6 |\n| SDF λ=0.1 | 58.0 | 58.5 | 54.5 | 57.0±2.2 |\n\n*LoRA s2 from `eval_lora_s2_30k_v2` (55% CAR, eval_seed=7)\n\n**Data sources:**\n- `reeval_lora_s0_30k_v2`: CAR=57, TSR=46\n- `reeval_lora_s1_30k`: CAR=52.5, TSR=51.5\n- `eval_lora_s2_30k_v2`: CAR=55, TSR=51.5\n- `reeval_sdf_s0_l005_30k`: CAR=57, TSR=55.5\n- `reeval_sdf_s1_l005_30k`: CAR=54, TSR=50.5\n- `reeval_sdf_s2_l005_30k`: CAR=52.5, TSR=56\n- `reeval_sdf_s0_l01_30k`: CAR=57, TSR=52.5\n- `reeval_sdf_s1_l01_30k`: CAR=57.5, TSR=55.5\n- `reeval_sdf_s2_l01_30k`: CAR=54.5, TSR=53.5\n- `eval_pi05_a1_30k_s0_l01_high`: CAR=58, TSR=47\n- `eval_pi05_a1_30k_s1_l01_high`: CAR=58.5, TSR=49\n- `eval_pi05_a1_30k_s2_l01_high`: CAR=54.5, TSR=54.5\n\n### S1b. TSR across conditions (reeval)\n\n| Condition | Seed 0 | Seed 1 | Seed 2 | Mean±Std |\n|-----------|--------|--------|--------|----------|\n| LoRA-only | 46.0 | 51.5 | 51.5 | 49.7±3.2 |\n| SDF λ=0.005 | 55.5 | 50.5 | 56.0 | 54.0±3.0 |\n| SDF λ=0.01 | 52.5 | 55.5 | 53.5 | 53.8±1.5 |\n| SDF λ=0.1 | 47.0 | 49.0 | 54.5 | 50.2±3.9 |\n\n### S1c. EE Displacement (reeval, m)\n\n| Condition | Seed 0 | Seed 1 | Seed 2 |\n|-----------|--------|--------|--------|\n| LoRA-only | — | 0.3882 | — |\n| SDF λ=0.005 | — | 0.3883 | 0.3858 |\n| SDF λ=0.01 | 0.3946 | 0.3852 | 0.3877 |\n| SDF λ=0.1 | 0.400 | 0.3884 | — |\n\nAll frozen_rate_ee = 0%, fake_safe_rate_ee = 0%.\n\n### S1d. Per-Task CAR Breakdown (reeval, all seeds)\n\n**LoRA-only:**\n| Seed | OrangeJuice | ChocoPudding | Milk | BBQSauce |\n|------|-------------|--------------|------|----------|\n| s0 | 68 | 74 | 66 | 20 |\n| s1 | 54 | 68 | 72 | 16 |\n| s2 | 56 | 76 | 62 | 26 |\n\n**SDF λ=0.005:**\n| Seed | OrangeJuice | ChocoPudding | Milk | BBQSauce |\n|------|-------------|--------------|------|----------|\n| s0 | 52 | 74 | 74 | 28 |\n| s1 | 64 | 70 | 68 | 14 |\n| s2 | 46 | 74 | 72 | 18 |\n\n**SDF λ=0.01:**\n| Seed | OrangeJuice | ChocoPudding | Milk | BBQSauce |\n|------|-------------|--------------|------|----------|\n| s0 | 48 | 74 | 72 | 34 |\n| s1 | 60 | 76 | 72 | 22 |\n| s2 | 64 | 68 | 72 | 14 |\n\n**SDF λ=0.1:**\n| Seed | OrangeJuice | ChocoPudding | Milk | BBQSauce |\n|------|-------------|--------------|------|----------|\n| s0 | — | — | — | — |\n| s1 | 66 | 72 | 70 | 26 |\n| s2 | 56 | 76 | 70 | 16 |\n\n**Existing figure:** `fig_pertask_car_fingerprint.png`\n\n---\n\n## S2. Multi-Eval-Seed Robustness (Table)\n\nTests CAR stability across different eval_seed values for LoRA s0 and SDF (lambda=0.1) s0 checkpoints.\n\n### S2a. LoRA-only s0 30K across eval seeds\n\n| eval_seed | avg_CAR | avg_TSR | n_episodes |\n|-----------|---------|---------|------------|\n| 0 | 53.0 | 55.5 | 50 |\n| 7 (default) | 56.5 | 51.5 | 200 |\n| 42 | 56.5 | 46.0 | 50 |\n| 99 | 57.5 | 52.0 | 50 |\n| 123 | 53.0 | 50.5 | 50 |\n\n**Mean CAR = 55.3%, Std = 2.0%**\n\n**Data sources:** `eval_multiseed_lora_s0_eseed{0,42,99,123}`, `eval_lora_baseline_30k_s0_reeval`\n\n### S2b. SDF s0 30K across eval seeds\n\nNote: eseed 0/99 use λ=0.01 model; eseed 42/123/256 use λ=0.1 model.\n\n| eval_seed | Model (λ) | avg_CAR | avg_TSR | n_episodes |\n|-----------|-----------|---------|---------|------------|\n| 0 | 0.01 | 52.5 | 48.5 | 50 |\n| 42 | 0.1 | 59.0 | 52.5 | 50 |\n| 99 | 0.01 | 57.0 | 46.5 | 50 |\n| 123 | 0.1 | 58.5 | 53.5 | 50 |\n| 256 | 0.1 | 57.0 | 48.0 | 50 |\n\n**SDF λ=0.1 (eseed 42/123/256): Mean CAR = 58.2%, Std = 1.1%**\n**SDF λ=0.01 (eseed 0/99): Mean CAR = 54.8%, Std = 3.2%**\n\n**Data sources:** `eval_multiseed_sdf_l01_s0_eseed{0,42,99,123,256}`\n\n### S2c. Per-Task Detail (available for eseed 42/123/256)\n\n| eval_seed | OJ CAR | CP CAR | Milk CAR | BBQ CAR |\n|-----------|--------|--------|----------|---------|\n| 42 (LoRA) | 60 | 70 | 68 | 28 |\n| 42 (SDF λ=0.1) | 64 | 74 | 74 | 24 |\n| 123 (LoRA) | 52 | 74 | 66 | 20 |\n| 123 (SDF λ=0.1) | 62 | 76 | 74 | 22 |\n| 256 (SDF λ=0.1) | 60 | 72 | 66 | 30 |\n\n**Existing figure:** None specific to eval-seed. Needs new figure.\n\n---\n\n## S3. Lambda Ablation Detailed Data (Table + Figure)\n\n### S3a. Summary: CAR vs Lambda (reeval, 3 seeds each)\n\n| λ | s0 CAR | s1 CAR | s2 CAR | Mean | Std | p vs null |\n|---|--------|--------|--------|------|-----|-----------|\n| 0 (LoRA-only) | 57 | 52.5 | 55 | 54.8 | 2.3 | — |\n| 0.005 | 57 | 54 | 52.5 | 54.5 | 2.3 | within null |\n| 0.01 | 57 | 57.5 | 54.5 | 56.3 | 1.6 | +0.84σ, p>0.1 |\n| 0.1 | 58 | 58.5 | 54.5 | 57.0 | 2.2 | see S3c |\n| 0 (Phase 2) | — | — | 57.5 | — | — | +1.40σ, p~0.08 |\n\nNull distribution: LoRA + λ=0.005 pooled, mean=54.7%, σ=2.15%.\n\n### S3b. Stepwise Training Curve for λ=0.1 s0\n\n| Step | CAR | TSR | frozen_rate | exp_id |\n|------|-----|-----|-------------|--------|\n| 16K | 55.5 | 49.5 | 0% | eval_stepwise_s0_l1_16k |\n| 20K | 55.0 | 54.0 | 0% | eval_early_signal_s0_l1_20k |\n| 22K | 60.5 | 45.5 | 0% | eval_stepwise_s0_l1_22k |\n| 24K | 52.5 | 50.5 | 0% | eval_stepwise_s0_l1_24k_v2 |\n| 26K | 53.5 | 53.0 | 0% | eval_stepwise_s0_l1_26k_v2 |\n| 28K | 54.5 | 48.5 | 0% | eval_stepwise_s0_l1_28k |\n| 30K | 58.0 | 47.0 | 0% | eval_pi05_a1_30k_s0_l01_high |\n\n### S3c. Permutation Test Results (Exact)\n\n| Setting | Obs Mean | Perm p (1-tail) | Perm p (2-tail) | Welch p (1-tail) | Sig α=0.05? |\n|---------|----------|-----------------|-----------------|------------------|-------------|\n| λ=0.1, 2 seeds | 58.25 | 0.0357 | 0.0714 | 0.0035 | YES* |\n| λ=0.1, 3 seeds (s2=54) | 56.83 | 0.1071 | 0.2143 | 0.1349 | NO |\n| λ=0.1, 3 seeds (s2=55) | 57.17 | 0.0714 | 0.1548 | 0.0682 | NO |\n| λ=0.1, 3 seeds (s2=56) | 57.50 | 0.0476 | 0.0833 | 0.0227 | YES |\n\n*2-tail p=0.071, marginal\n\n**Data source:** `permutation_test_results.txt`\n\n**Existing figures:**\n- `fig5_lambda_curve.pdf` / `fig5_lambda_curve.png` — CAR vs λ\n- `fig5_lambda_car_v4.png` — updated version\n- `fig_threshold_sensitivity.pdf` — threshold sensitivity analysis\n\n---\n\n## S4. Oracle Experiment Complete Results (Table)\n\nAll oracle experiments produced **negative** conclusions. Unified finding: even GT SDF cannot improve CAR; refinement causes action collapse.\n\n### S4a. Oracle Lineage and Results\n\n| Experiment | Oracle Type | CAR | TSR | Fake Safe % | Notes |\n|-----------|------------|-----|-----|-------------|-------|\n| Baseline (no refinement) | — | 79%† | — | — | Reference |\n| oracle_a3_force_refine_object_v11 | Learned decoder, force_refine | 81.2 | 0 | — | M027: dead code, used learned decoder |\n| oracle_a3_m024fix_object_v11 | M024 coord fix, learned decoder | 85.6 | 0 | — | 85.6% frozen = fake safety |\n| oracle_true_gt_adaptive_alpha_v11 | GT SDF, adaptive alpha | 75.0 | 0 | 98.3% | 118/120 safe eps disp<0.1mm |\n| oracle_true_gt_fixed_alpha_v11 | GT SDF, fixed alpha=0.005 | 73.1 | 0 | 98.3% | 115/117 safe eps disp<0.1mm |\n| oracle_true_gt_feature_v11 | GT SDF, feature-space gradient | 76.9 | 0 | 96.7% | 119/123 safe eps disp<0.1mm |\n\n†Baseline CAR from eval_baseline_v11_object\n\n### S4b. Per-Task CAR Breakdown (Oracle)\n\n| Task | Adaptive α | Fixed α | Feature-space |\n|------|-----------|---------|---------------|\n| OrangeJuice | 82.5 | 85.0 | 90.0 |\n| ChocoPudding | 55.0 | 50.0 | 47.5 |\n| Milk | 77.5 | 77.5 | 82.5 |\n| BBQSauce | 85.0 | 80.0 | 87.5 |\n\n### S4c. Refinement Statistics\n\n| Metric | Adaptive α | Fixed α | Feature-space |\n|--------|-----------|---------|---------------|\n| Avg refined steps/ep | 14.2 | 14.8 | 241.7 |\n| Total refined steps | 2270 | 2375 | 38679 |\n| Grad magnitude (mean) | 0.18–0.49 | — | 0.004–0.006 |\n| n_episodes | 160 | 160 | 160 |\n\n### S4d. Per-Task Displacement (Oracle)\n\n| Task | Adaptive α (m) | Fixed α (m) | Feature-space (m) |\n|------|---------------|-------------|-------------------|\n| OrangeJuice | 0.0076 | 0.0113 | 0.0023 |\n| ChocoPudding | 0.0475 | 0.0365 | 0.0473 |\n| Milk | 0.0107 | 0.0042 | 0.0086 |\n| BBQSauce | 0.0077 | 0.0032 | 0.0097 |\n\n**Data sources:** `oracle_true_gt_adaptive_alpha_v11`, `oracle_true_gt_fixed_alpha_v11`, `oracle_true_gt_feature_v11`\n\n**Existing figure:** `fig_oracle_bar.pdf`\n\n---\n\n## S5. Training Curves\n\n**Registry has NO wandb_run_id fields** — W&B tracking was not registered in the experiment registry.\n\n### S5a. Available Training Loss Data (from registry metrics)\n\n| Experiment | best_loss | final_loss | best_step | total_steps |\n|-----------|-----------|------------|-----------|-------------|\n| train_pi05_lora_baseline_s0 | 0.01025 | 0.01343 | 24K | 30K |\n| train_pi05_lora_baseline_s1 | 0.01130 | 0.01408 | 14K | 30K |\n| train_pi05_lora_baseline_s2_resume | — | 0.01170 | — | 30K |\n| train_pi05_a1_obj_s0_l005 | 0.00786 | — | 26K | 30K |\n| train_pi05_a1_obj_s1_l005 | 0.01143 | — | 16K | 30K |\n| train_pi05_a1_obj_s2_l005 | 0.00874 | — | 10K | 30K |\n| train_pi05_a1_obj_s0_l01 | 0.00801 | — | — | 30K |\n| train_pi05_a1_obj_s1_l01 | 0.01168 | — | 16K | 30K |\n| train_pi05_a1_obj_s2_l01 | 0.00911 | — | 10K | 30K |\n| train_pi05_a1_obj_s2_l01_high | 0.01040 | 0.01040 | 30K | 30K |\n| train_pi05_phase2_lambda0_s2 | 0.00651 | — | 4K | 10K |\n\n### S5b. Action Items for Training Curves\n\n- [ ] Check if W&B runs exist on server (not tracked in registry)\n- [ ] If W&B available: export loss curves for LoRA-only vs SDF conditions\n- [ ] If not: only scalar best/final loss available (table above), no time-series curves\n- [ ] A3 training metrics available for `a3_gradient_object_pudding_s0`: action_loss=0.01546, total_loss=0.01898, eikonal=0, n_refine=2.64\n\n---\n\n## S6. Additional Supplementary Data\n\n### S6a. SSR (Safe Success Rate) Analysis\n\n| Condition | Avg TSR | Avg CAR | Avg SSR | SSR/TSR |\n|-----------|---------|---------|---------|---------|\n| Pi0.5 baseline | 71.5% | 28.5% | 28.0% | 0.392 |\n| LoRA (2 seeds) | 51.5% | 54.5% | 28.3% | 0.549 |\n| SDF λ=0.005 (3 seeds) | 54.0% | 54.5% | 27.8% | 0.515 |\n| SDF λ=0.01 (3 seeds) | 53.8% | 56.3% | 30.2% | 0.561 |\n\n**Data source:** `ssr_analysis.md`\n\n### S6b. Threshold Sensitivity Analysis\n\n- dfCAR stable across collision thresholds 2mm–200mm\n- `analysis_threshold_sensitivity` experiment registered\n- **Existing figures:** `fig_threshold_sensitivity.pdf`, `sensitivity_curves.png`\n- **Data:** `threshold_sensitivity.csv`\n\n### S6c. Fake Safety (A1 Full-FT Baseline)\n\n- Fake safe rate = 99.6% (729/732 safe episodes with displacement < 0.1mm)\n- **Data source:** `eval_a1_lora_object_v11_rerun` (800 episodes)\n- **Existing figure:** `fig_displacement_hist.pdf`, `fig2_ee_displacement_distribution.pdf`\n\n### S6d. Spatial Bowl Transfer Results\n\n| Condition | avg_CAR | avg_TSR | exp_id |\n|-----------|---------|---------|--------|\n| LoRA-only s0 | 12.0 | 49.0 | eval_spatial_bowl_lora_ctrl_s0_v2 |\n| SDF λ=0.005 s0 | 11.5 | 51.5 | eval_spatial_bowl_sdf_s0_l005_30k |\n\nSDF provides no transfer benefit on spatial_bowl scene.\n\n---\n\n## Summary: Existing Figures Index\n\n| Figure | File | In Paper? |\n|--------|------|-----------|\n| Teaser / overview | `fig1_teaser_v2.pdf`, `fig_overview_pb_v13.png` | Yes |\n| EE displacement distribution | `fig2_ee_displacement_distribution.pdf` | Yes |\n| TSR–CAR scatter | `fig3_tsr_car_scatter.pdf` | Yes |\n| Lambda curve (CAR vs λ) | `fig5_lambda_curve.pdf`, `fig5_lambda_car_v4.png` | Yes |\n| Threshold sensitivity | `fig_threshold_sensitivity.pdf` | Yes |\n| Oracle bar chart | `fig_oracle_bar.pdf` | Yes |\n| Per-task CAR fingerprint | `fig_pertask_car_fingerprint.png` | Yes |\n| Plan A/B concept | `fig2_plan_a.png`, `fig2_plan_b.png` | Yes |\n\n### Figures Needed for Supplementary\n\n- [ ] Multi-eval-seed CAR bar chart (LoRA vs SDF across eval seeds)\n- [ ] Per-task TSR breakdown table/heatmap\n- [ ] Training loss curves (if W&B data available)\n- [ ] Stepwise CAR curve for λ=0.1 (step 16K–30K)\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_supplementary_checklist_20260528T191045",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/supplementary_checklist.md",
    "content": "# Supplementary Material Checklist\n\n> Generated: 2026-05-28\n> Source: 131 experiments in registry (72 success, 25 negative, 18 failed, 16 killed)\n> Authoritative eval pipeline: `reeval_*` series (rotation-fixed, eval_seed=7, n=200 episodes)\n\n---\n\n## S1. Multi-Seed Complete Results (Table)\n\n### S1a. Main Results: CAR across conditions (reeval, rotation-fixed)\n\n| Condition | Seed 0 | Seed 1 | Seed 2 | Mean±Std |\n|-----------|--------|--------|--------|----------|\n| LoRA-only | 57.0 | 52.5 | 55.0* | 54.8±2.3 |\n| SDF λ=0.005 | 57.0 | 54.0 | 52.5 | 54.5±2.3 |\n| SDF λ=0.01 | 57.0 | 57.5 | 54.5 | 56.3±1.6 |\n| SDF λ=0.1 | 58.0 | 58.5 | 54.5 | 57.0±2.2 |\n\n*LoRA s2 from `eval_lora_s2_30k_v2` (55% CAR, eval_seed=7)\n\n**Data sources:**\n- `reeval_lora_s0_30k_v2`: CAR=57, TSR=46\n- `reeval_lora_s1_30k`: CAR=52.5, TSR=51.5\n- `eval_lora_s2_30k_v2`: CAR=55, TSR=51.5\n- `reeval_sdf_s0_l005_30k`: CAR=57, TSR=55.5\n- `reeval_sdf_s1_l005_30k`: CAR=54, TSR=50.5\n- `reeval_sdf_s2_l005_30k`: CAR=52.5, TSR=56\n- `reeval_sdf_s0_l01_30k`: CAR=57, TSR=52.5\n- `reeval_sdf_s1_l01_30k`: CAR=57.5, TSR=55.5\n- `reeval_sdf_s2_l01_30k`: CAR=54.5, TSR=53.5\n- `eval_pi05_a1_30k_s0_l01_high`: CAR=58, TSR=47\n- `eval_pi05_a1_30k_s1_l01_high`: CAR=58.5, TSR=49\n- `eval_pi05_a1_30k_s2_l01_high`: CAR=54.5, TSR=54.5\n\n### S1b. TSR across conditions (reeval)\n\n| Condition | Seed 0 | Seed 1 | Seed 2 | Mean±Std |\n|-----------|--------|--------|--------|----------|\n| LoRA-only | 46.0 | 51.5 | 51.5 | 49.7±3.2 |\n| SDF λ=0.005 | 55.5 | 50.5 | 56.0 | 54.0±3.0 |\n| SDF λ=0.01 | 52.5 | 55.5 | 53.5 | 53.8±1.5 |\n| SDF λ=0.1 | 47.0 | 49.0 | 54.5 | 50.2±3.9 |\n\n### S1c. EE Displacement (reeval, m)\n\n| Condition | Seed 0 | Seed 1 | Seed 2 |\n|-----------|--------|--------|--------|\n| LoRA-only | — | 0.3882 | — |\n| SDF λ=0.005 | — | 0.3883 | 0.3858 |\n| SDF λ=0.01 | 0.3946 | 0.3852 | 0.3877 |\n| SDF λ=0.1 | 0.400 | 0.3884 | — |\n\nAll frozen_rate_ee = 0%, fake_safe_rate_ee = 0%.\n\n### S1d. Per-Task CAR Breakdown (reeval, all seeds)\n\n**LoRA-only:**\n| Seed | OrangeJuice | ChocoPudding | Milk | BBQSauce |\n|------|-------------|--------------|------|----------|\n| s0 | 68 | 74 | 66 | 20 |\n| s1 | 54 | 68 | 72 | 16 |\n| s2 | 56 | 76 | 62 | 26 |\n\n**SDF λ=0.005:**\n| Seed | OrangeJuice | ChocoPudding | Milk | BBQSauce |\n|------|-------------|--------------|------|----------|\n| s0 | 52 | 74 | 74 | 28 |\n| s1 | 64 | 70 | 68 | 14 |\n| s2 | 46 | 74 | 72 | 18 |\n\n**SDF λ=0.01:**\n| Seed | OrangeJuice | ChocoPudding | Milk | BBQSauce |\n|------|-------------|--------------|------|----------|\n| s0 | 48 | 74 | 72 | 34 |\n| s1 | 60 | 76 | 72 | 22 |\n| s2 | 64 | 68 | 72 | 14 |\n\n**SDF λ=0.1:**\n| Seed | OrangeJuice | ChocoPudding | Milk | BBQSauce |\n|------|-------------|--------------|------|----------|\n| s0 | — | — | — | — |\n| s1 | 66 | 72 | 70 | 26 |\n| s2 | 56 | 76 | 70 | 16 |\n\n**Existing figure:** `fig_pertask_car_fingerprint.png`\n\n---\n\n## S2. Multi-Eval-Seed Robustness (Table)\n\nTests CAR stability across different eval_seed values for LoRA s0 and SDF (lambda=0.1) s0 checkpoints.\n\n### S2a. LoRA-only s0 30K across eval seeds\n\n| eval_seed | avg_CAR | avg_TSR | n_episodes |\n|-----------|---------|---------|------------|\n| 0 | 53.0 | 55.5 | 50 |\n| 7 (default) | 56.5 | 51.5 | 200 |\n| 42 | 56.5 | 46.0 | 50 |\n| 99 | 57.5 | 52.0 | 50 |\n| 123 | 53.0 | 50.5 | 50 |\n\n**Mean CAR = 55.3%, Std = 2.0%**\n\n**Data sources:** `eval_multiseed_lora_s0_eseed{0,42,99,123}`, `eval_lora_baseline_30k_s0_reeval`\n\n### S2b. SDF s0 30K across eval seeds\n\nNote: eseed 0/99 use λ=0.01 model; eseed 42/123/256 use λ=0.1 model.\n\n| eval_seed | Model (λ) | avg_CAR | avg_TSR | n_episodes |\n|-----------|-----------|---------|---------|------------|\n| 0 | 0.01 | 52.5 | 48.5 | 50 |\n| 42 | 0.1 | 59.0 | 52.5 | 50 |\n| 99 | 0.01 | 57.0 | 46.5 | 50 |\n| 123 | 0.1 | 58.5 | 53.5 | 50 |\n| 256 | 0.1 | 57.0 | 48.0 | 50 |\n\n**SDF λ=0.1 (eseed 42/123/256): Mean CAR = 58.2%, Std = 1.1%**\n**SDF λ=0.01 (eseed 0/99): Mean CAR = 54.8%, Std = 3.2%**\n\n**Data sources:** `eval_multiseed_sdf_l01_s0_eseed{0,42,99,123,256}`\n\n### S2c. Per-Task Detail (available for eseed 42/123/256)\n\n| eval_seed | OJ CAR | CP CAR | Milk CAR | BBQ CAR |\n|-----------|--------|--------|----------|---------|\n| 42 (LoRA) | 60 | 70 | 68 | 28 |\n| 42 (SDF λ=0.1) | 64 | 74 | 74 | 24 |\n| 123 (LoRA) | 52 | 74 | 66 | 20 |\n| 123 (SDF λ=0.1) | 62 | 76 | 74 | 22 |\n| 256 (SDF λ=0.1) | 60 | 72 | 66 | 30 |\n\n**Existing figure:** None specific to eval-seed. Needs new figure.\n\n---\n\n## S3. Lambda Ablation Detailed Data (Table + Figure)\n\n### S3a. Summary: CAR vs Lambda (reeval, 3 seeds each)\n\n| λ | s0 CAR | s1 CAR | s2 CAR | Mean | Std | p vs null |\n|---|--------|--------|--------|------|-----|-----------|\n| 0 (LoRA-only) | 57 | 52.5 | 55 | 54.8 | 2.3 | — |\n| 0.005 | 57 | 54 | 52.5 | 54.5 | 2.3 | within null |\n| 0.01 | 57 | 57.5 | 54.5 | 56.3 | 1.6 | +0.84σ, p>0.1 |\n| 0.1 | 58 | 58.5 | 54.5 | 57.0 | 2.2 | see S3c |\n| 0 (Phase 2) | — | — | 57.5 | — | — | +1.40σ, p~0.08 |\n\nNull distribution: LoRA + λ=0.005 pooled, mean=54.7%, σ=2.15%.\n\n### S3b. Stepwise Training Curve for λ=0.1 s0\n\n| Step | CAR | TSR | frozen_rate | exp_id |\n|------|-----|-----|-------------|--------|\n| 16K | 55.5 | 49.5 | 0% | eval_stepwise_s0_l1_16k |\n| 20K | 55.0 | 54.0 | 0% | eval_early_signal_s0_l1_20k |\n| 22K | 60.5 | 45.5 | 0% | eval_stepwise_s0_l1_22k |\n| 24K | 52.5 | 50.5 | 0% | eval_stepwise_s0_l1_24k_v2 |\n| 26K | 53.5 | 53.0 | 0% | eval_stepwise_s0_l1_26k_v2 |\n| 28K | 54.5 | 48.5 | 0% | eval_stepwise_s0_l1_28k |\n| 30K | 58.0 | 47.0 | 0% | eval_pi05_a1_30k_s0_l01_high |\n\n### S3c. Permutation Test Results (Exact)\n\n| Setting | Obs Mean | Perm p (1-tail) | Perm p (2-tail) | Welch p (1-tail) | Sig α=0.05? |\n|---------|----------|-----------------|-----------------|------------------|-------------|\n| λ=0.1, 2 seeds | 58.25 | 0.0357 | 0.0714 | 0.0035 | YES* |\n| λ=0.1, 3 seeds (s2=54) | 56.83 | 0.1071 | 0.2143 | 0.1349 | NO |\n| λ=0.1, 3 seeds (s2=55) | 57.17 | 0.0714 | 0.1548 | 0.0682 | NO |\n| λ=0.1, 3 seeds (s2=56) | 57.50 | 0.0476 | 0.0833 | 0.0227 | YES |\n\n*2-tail p=0.071, marginal\n\n**Data source:** `permutation_test_results.txt`\n\n**Existing figures:**\n- `fig5_lambda_curve.pdf` / `fig5_lambda_curve.png` — CAR vs λ\n- `fig5_lambda_car_v4.png` — updated version\n- `fig_threshold_sensitivity.pdf` — threshold sensitivity analysis\n\n---\n\n## S4. Oracle Experiment Complete Results (Table)\n\nAll oracle experiments produced **negative** conclusions. Unified finding: even GT SDF cannot improve CAR; refinement causes action collapse.\n\n### S4a. Oracle Lineage and Results\n\n| Experiment | Oracle Type | CAR | TSR | Fake Safe % | Notes |\n|-----------|------------|-----|-----|-------------|-------|\n| Baseline (no refinement) | — | 79%† | — | — | Reference |\n| oracle_a3_force_refine_object_v11 | Learned decoder, force_refine | 81.2 | 0 | — | M027: dead code, used learned decoder |\n| oracle_a3_m024fix_object_v11 | M024 coord fix, learned decoder | 85.6 | 0 | — | 85.6% frozen = fake safety |\n| oracle_true_gt_adaptive_alpha_v11 | GT SDF, adaptive alpha | 75.0 | 0 | 98.3% | 118/120 safe eps disp<0.1mm |\n| oracle_true_gt_fixed_alpha_v11 | GT SDF, fixed alpha=0.005 | 73.1 | 0 | 98.3% | 115/117 safe eps disp<0.1mm |\n| oracle_true_gt_feature_v11 | GT SDF, feature-space gradient | 76.9 | 0 | 96.7% | 119/123 safe eps disp<0.1mm |\n\n†Baseline CAR from eval_baseline_v11_object\n\n### S4b. Per-Task CAR Breakdown (Oracle)\n\n| Task | Adaptive α | Fixed α | Feature-space |\n|------|-----------|---------|---------------|\n| OrangeJuice | 82.5 | 85.0 | 90.0 |\n| ChocoPudding | 55.0 | 50.0 | 47.5 |\n| Milk | 77.5 | 77.5 | 82.5 |\n| BBQSauce | 85.0 | 80.0 | 87.5 |\n\n### S4c. Refinement Statistics\n\n| Metric | Adaptive α | Fixed α | Feature-space |\n|--------|-----------|---------|---------------|\n| Avg refined steps/ep | 14.2 | 14.8 | 241.7 |\n| Total refined steps | 2270 | 2375 | 38679 |\n| Grad magnitude (mean) | 0.18–0.49 | — | 0.004–0.006 |\n| n_episodes | 160 | 160 | 160 |\n\n### S4d. Per-Task Displacement (Oracle)\n\n| Task | Adaptive α (m) | Fixed α (m) | Feature-space (m) |\n|------|---------------|-------------|-------------------|\n| OrangeJuice | 0.0076 | 0.0113 | 0.0023 |\n| ChocoPudding | 0.0475 | 0.0365 | 0.0473 |\n| Milk | 0.0107 | 0.0042 | 0.0086 |\n| BBQSauce | 0.0077 | 0.0032 | 0.0097 |\n\n**Data sources:** `oracle_true_gt_adaptive_alpha_v11`, `oracle_true_gt_fixed_alpha_v11`, `oracle_true_gt_feature_v11`\n\n**Existing figure:** `fig_oracle_bar.pdf`\n\n---\n\n## S5. Training Curves\n\n**Registry has NO wandb_run_id fields** — W&B tracking was not registered in the experiment registry.\n\n### S5a. Available Training Loss Data (from registry metrics)\n\n| Experiment | best_loss | final_loss | best_step | total_steps |\n|-----------|-----------|------------|-----------|-------------|\n| train_pi05_lora_baseline_s0 | 0.01025 | 0.01343 | 24K | 30K |\n| train_pi05_lora_baseline_s1 | 0.01130 | 0.01408 | 14K | 30K |\n| train_pi05_lora_baseline_s2_resume | — | 0.01170 | — | 30K |\n| train_pi05_a1_obj_s0_l005 | 0.00786 | — | 26K | 30K |\n| train_pi05_a1_obj_s1_l005 | 0.01143 | — | 16K | 30K |\n| train_pi05_a1_obj_s2_l005 | 0.00874 | — | 10K | 30K |\n| train_pi05_a1_obj_s0_l01 | 0.00801 | — | — | 30K |\n| train_pi05_a1_obj_s1_l01 | 0.01168 | — | 16K | 30K |\n| train_pi05_a1_obj_s2_l01 | 0.00911 | — | 10K | 30K |\n| train_pi05_a1_obj_s2_l01_high | 0.01040 | 0.01040 | 30K | 30K |\n| train_pi05_phase2_lambda0_s2 | 0.00651 | — | 4K | 10K |\n\n### S5b. Action Items for Training Curves\n\n- [ ] Check if W&B runs exist on server (not tracked in registry)\n- [ ] If W&B available: export loss curves for LoRA-only vs SDF conditions\n- [ ] If not: only scalar best/final loss available (table above), no time-series curves\n- [ ] A3 training metrics available for `a3_gradient_object_pudding_s0`: action_loss=0.01546, total_loss=0.01898, eikonal=0, n_refine=2.64\n\n---\n\n## S6. Additional Supplementary Data\n\n### S6a. SSR (Safe Success Rate) Analysis\n\n| Condition | Avg TSR | Avg CAR | Avg SSR | SSR/TSR |\n|-----------|---------|---------|---------|---------|\n| Pi0.5 baseline | 71.5% | 28.5% | 28.0% | 0.392 |\n| LoRA (2 seeds) | 51.5% | 54.5% | 28.3% | 0.549 |\n| SDF λ=0.005 (3 seeds) | 54.0% | 54.5% | 27.8% | 0.515 |\n| SDF λ=0.01 (3 seeds) | 53.8% | 56.3% | 30.2% | 0.561 |\n\n**Data source:** `ssr_analysis.md`\n\n### S6b. Threshold Sensitivity Analysis\n\n- dfCAR stable across collision thresholds 2mm–200mm\n- `analysis_threshold_sensitivity` experiment registered\n- **Existing figures:** `fig_threshold_sensitivity.pdf`, `sensitivity_curves.png`\n- **Data:** `threshold_sensitivity.csv`\n\n### S6c. Fake Safety (A1 Full-FT Baseline)\n\n- Fake safe rate = 99.6% (729/732 safe episodes with displacement < 0.1mm)\n- **Data source:** `eval_a1_lora_object_v11_rerun` (800 episodes)\n- **Existing figure:** `fig_displacement_hist.pdf`, `fig2_ee_displacement_distribution.pdf`\n\n### S6d. Spatial Bowl Transfer Results\n\n| Condition | avg_CAR | avg_TSR | exp_id |\n|-----------|---------|---------|--------|\n| LoRA-only s0 | 12.0 | 49.0 | eval_spatial_bowl_lora_ctrl_s0_v2 |\n| SDF λ=0.005 s0 | 11.5 | 51.5 | eval_spatial_bowl_sdf_s0_l005_30k |\n\nSDF provides no transfer benefit on spatial_bowl scene.\n\n---\n\n## Summary: Existing Figures Index\n\n| Figure | File | In Paper? |\n|--------|------|-----------|\n| Teaser / overview | `fig1_teaser_v2.pdf`, `fig_overview_pb_v13.png` | Yes |\n| EE displacement distribution | `fig2_ee_displacement_distribution.pdf` | Yes |\n| TSR–CAR scatter | `fig3_tsr_car_scatter.pdf` | Yes |\n| Lambda curve (CAR vs λ) | `fig5_lambda_curve.pdf`, `fig5_lambda_car_v4.png` | Yes |\n| Threshold sensitivity | `fig_threshold_sensitivity.pdf` | Yes |\n| Oracle bar chart | `fig_oracle_bar.pdf` | Yes |\n| Per-task CAR fingerprint | `fig_pertask_car_fingerprint.png` | Yes |\n| Plan A/B concept | `fig2_plan_a.png`, `fig2_plan_b.png` | Yes |\n\n### Figures Needed for Supplementary\n\n- [ ] Multi-eval-seed CAR bar chart (LoRA vs SDF across eval seeds)\n- [ ] Per-task TSR breakdown table/heatmap\n- [ ] Training loss curves (if W&B data available)\n- [ ] Stepwise CAR curve for λ=0.1 (step 16K–30K)\n"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-28T19:18:19.568614+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/supplementary_checklist.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_supplementary_checklist_20260528T191045",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-28T19:18:19.568755+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "Supplementary Material Checklist",
  "type": "report",
  "description": "Complete supplementary material checklist for CoRL 2026 paper: multi-seed tables (S1), multi-eval-seed robustness (S2), lambda ablation with permutation tests (S3), oracle experiments (S4), training curves (S5), and additional data (SSR, threshold sensitivity, fake safety, spatial bowl). Includes data sources, existing figures index, and TODOs.",
  "project": "diff_collision_sdf",
  "source_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/supplementary_checklist.md",
  "tags": "['supplementary', 'paper', 'checklist', 'data-summary']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_supplementary_checklist_20260528T191045",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "Supplementary Material Checklist",
    "type": "report",
    "description": "Complete supplementary material checklist for CoRL 2026 paper: multi-seed tables (S1), multi-eval-seed robustness (S2), lambda ablation with permutation tests (S3), oracle experiments (S4), training curves (S5), and additional data (SSR, threshold sensitivity, fake safety, spatial bowl). Includes data sources, existing figures index, and TODOs.",
    "project": "diff_collision_sdf",
    "source_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/supplementary_checklist.md",
    "tags": "['supplementary', 'paper', 'checklist', 'data-summary']"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-28T19:18:19.568907+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260528_a06d89\", \"name\": \"Supplementary Material Checklist\", \"type\": \"report\", \"description\": \"Complete supplementary material checklist for CoRL 2026 paper: multi-seed tables (S1), multi-eval-seed robustness (S2), lambda ablation with permutation tests (S3), oracle experiments (S4), training curves (S5), and additional data (SSR, threshold sensitivity, fake safety, spatial bowl). Includes data sources, existing figures index, and TODOs.\", \"path\": \"projects/diff_collision_sdf/artifacts/_project/report/supplementary_checklist.md\", \"url\": null, \"project\": \"diff_collision_sdf\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-28T19:18:10.160378+00:00\", \"tags\": [\"supplementary\", \"paper\", \"checklist\", \"data-summary\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515/projects/diff_collision_sdf/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_supplementary_checklist_20260528T191045",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-28T19:18:19.569077+00:00_

已创建 `supplementary_checklist.md` 并注册为 artifact (`art_20260528_a06d89`)。

清单包含 6 大类：

| 编号 | 内容 | 数据完备度 |
|------|------|-----------|
| **S1** | Multi-seed 完整结果表（CAR/TSR/EE-disp/per-task, 3 seeds × 4 条件） | 完整 |
| **S2** | Multi-eval-seed 鲁棒性（LoRA 5 eval seeds, SDF 5 eval seeds） | 完整，缺专属图表 |
| **S3** | Lambda 消融（λ=0/0.005/0.01/0.1 + permutation test + stepwise curve） | 完整，已有 fig5 |
| **S4** | Oracle 实验（5 个变体 per-task breakdown + refinement statistics） | 完整，已有 fig_oracle_bar |
| **S5** | 训练曲线 | **缺失**：registry 无 W&B ID，仅有标量 best/final loss |
| **S6** | 附加数据（SSR, threshold sensitivity, fake safety, spatial bowl） | 完整 |

待办：
- 检查服务器上是否存在 W&B runs（registry 未记录）
- 制作 multi-eval-seed CAR 对比图
- 制作 stepwise CAR 曲线图（λ=0.1, 16K–30K）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_supplementary_checklist_20260528T191045"
}
```

</details>

---
