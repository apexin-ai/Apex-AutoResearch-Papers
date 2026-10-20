# Research conversation: You are auditing a research paper's data correctness. The experiment registry is saved as JSON at: `/home/ubuntu/.claude

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 34
- **Recorded user turns:** 1
- **Tool calls:** 14
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a10e81c6866b67bf0.jsonl`
- **Structured JSON:** [`9ee6f9588ba9643302e4.json`](../../sessions/9e/9ee6f9588ba9643302e4.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

34 recorded events

### User

_source line 1 · 2026-05-25T08:31:21.373Z_

You are auditing a research paper's data correctness. The experiment registry is saved as JSON at:
`/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating--claude-sessions-paper-agent-d1ae4a98/0b0cdf03-4218-4267-be3a-fa2b7e05fc58/tool-results/mcp-agent-ml-research-read_registry-1779697863127.txt`

This is JSON with schema: `{result: string}` where the `result` field contains a YAML string of experiments.

Your job: extract ALL quantitative results that could appear in the paper. For each experiment, extract:
- exp_id
- variant name (e.g., ThreadGate, LoRA-only, Uniform Gate, PCGrad, Base, SS variants, Llama variants)
- All metrics: TF GAR-ours, AR GAR-ours, TF GAR-Dongre, AR GAR-Dongre, PPL, MMLU, TRC values
- Training config: learning rate, batch size, epochs, seed
- Any statistical tests (p-values, effect sizes)
- Gradient statistics (cosine similarity, magnitude ratios)
- Scheduled sampling results (different beta values)
- Cross-model (Llama) results
- Any steering (beta) results

Use `jq` or `python` to parse the file. First probe its structure, then extract systematically.

Output a structured summary organized by experiment variant, with ALL numbers. Be exhaustive - every number matters for the audit.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "7f6d57ff-336a-4102-9549-9590b20d9c0f",
  "agentId": "a10e81c6866b67bf0",
  "type": "user",
  "uuid": "74b2305a-8285-4860-b12d-028cafc4c997",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-25T08:31:21.378Z_

```json
{
  "parentUuid": "74b2305a-8285-4860-b12d-028cafc4c997",
  "isSidechain": true,
  "agentId": "a10e81c6866b67bf0",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__auto_build_provenance",
      "mcp__agent-ml-research__bootstrap_provenance",
      "mcp__agent-ml-research__check_figures_and_layout",
      "mcp__agent-ml-research__check_paper_consistency",
      "mcp__agent-ml-research__check_provenance_completeness",
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__compute_coverage_matrix",
      "mcp__agent-ml-research__edit_paper_section",
      "mcp__agent-ml-research__get_image_info",
      "mcp__agent-ml-research__get_worker_status",
      "mcp__agent-ml-research__list_artifacts",
      "mcp__agent-ml-research__list_workers",
      "mcp__agent-ml-research__load_project_config",
      "mcp__agent-ml-research__overleaf_init",
      "mcp__agent-ml-research__overleaf_pull",
      "mcp__agent-ml-research__overleaf_push",
      "mcp__agent-ml-research__overleaf_status",
      "mcp__agent-ml-research__overleaf_sync",
      "mcp__agent-ml-research__paper_agent_post_to_director",
      "mcp__agent-ml-research__paper_agent_request_review",
      "mcp__agent-ml-research__paper_compile_and_check",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__read_experiment_plan_with_status",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__read_roadmap",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__send_progress",
      "mcp__agent-ml-research__spawn_worker",
      "mcp__agent-ml-research__verify_references",
      "mcp__agent-ml-research__write_paper_section"
    ],
    "addedLines": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__auto_build_provenance",
      "mcp__agent-ml-research__bootstrap_provenance",
      "mcp__agent-ml-research__check_figures_and_layout",
      "mcp__agent-ml-research__check_paper_consistency",
      "mcp__agent-ml-research__check_provenance_completeness",
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__compute_coverage_matrix",
      "mcp__agent-ml-research__edit_paper_section",
      "mcp__agent-ml-research__get_image_info",
      "mcp__agent-ml-research__get_worker_status",
      "mcp__agent-ml-research__list_artifacts",
      "mcp__agent-ml-research__list_workers",
      "mcp__agent-ml-research__load_project_config",
      "mcp__agent-ml-research__overleaf_init",
      "mcp__agent-ml-research__overleaf_pull",
      "mcp__agent-ml-research__overleaf_push",
      "mcp__agent-ml-research__overleaf_status",
      "mcp__agent-ml-research__overleaf_sync",
      "mcp__agent-ml-research__paper_agent_post_to_director",
      "mcp__agent-ml-research__paper_agent_request_review",
      "mcp__agent-ml-research__paper_compile_and_check",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__read_experiment_plan_with_status",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__read_roadmap",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__send_progress",
      "mcp__agent-ml-research__spawn_worker",
      "mcp__agent-ml-research__verify_references",
      "mcp__agent-ml-research__write_paper_section"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "659f98e8-fc88-425f-9f9b-0ebe096eeef5",
  "timestamp": "2026-05-25T08:31:21.378Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet"
}
```

---

### Assistant

_source line 3 · 2026-05-25T08:31:23.486Z_

I'll systematically extract all quantitative results from the experiment registry.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "659f98e8-fc88-425f-9f9b-0ebe096eeef5",
  "isSidechain": true,
  "agentId": "a10e81c6866b67bf0",
  "requestId": "req_011CbNyXffcY8GBnqAkDDz1y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c72dcd3b-bb1a-4c58-a9fd-de9e138f8932",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Sz6VMFLvFrtHrkE4xCEQqB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 27406,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 27406,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-25T08:31:26.002Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01FKYQebAJseargqpPCwi1JG`</summary>

```json
{
  "command": "ls -la \"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating--claude-sessions-paper-agent-d1ae4a98/0b0cdf03-4218-4267-be3a-fa2b7e05fc58/tool-results/mcp-agent-ml-research-read_registry-1779697863127.txt\" 2>/dev/null && wc -l \"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating--claude-sessions-paper-agent-d1ae4a98/0b0cdf03-4218-4267-be3a-fa2b7e05fc58/tool-results/mcp-agent-ml-research-read_registry-1779697863127.txt\"",
  "description": "Check file existence and size"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c72dcd3b-bb1a-4c58-a9fd-de9e138f8932",
  "isSidechain": true,
  "agentId": "a10e81c6866b67bf0",
  "requestId": "req_011CbNyXffcY8GBnqAkDDz1y",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9df271eb-37bd-47e2-90c4-d2c3a6480c97",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Sz6VMFLvFrtHrkE4xCEQqB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 27406,
      "cache_read_input_tokens": 0,
      "output_tokens": 317,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 27406
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 317,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 27406,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 27406,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-25T08:31:26.202Z_

<details><summary>↩ Tool result · `toolu_01FKYQebAJseargqpPCwi1JG`</summary>

```text
-rw-r--r-- 1 ubuntu ubuntu 101345 May 25 08:31 /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating--claude-sessions-paper-agent-d1ae4a98/0b0cdf03-4218-4267-be3a-fa2b7e05fc58/tool-results/mcp-agent-ml-research-read_registry-1779697863127.txt
0 /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating--claude-sessions-paper-agent-d1ae4a98/0b0cdf03-4218-4267-be3a-fa2b7e05fc58/tool-results/mcp-agent-ml-research-read_registry-1779697863127.txt
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9df271eb-37bd-47e2-90c4-d2c3a6480c97",
  "isSidechain": true,
  "promptId": "7f6d57ff-336a-4102-9549-9590b20d9c0f",
  "agentId": "a10e81c6866b67bf0",
  "type": "user",
  "uuid": "673ff51b-4cc3-4505-9ca6-f2683d8676b2",
  "sourceToolAssistantUUID": "9df271eb-37bd-47e2-90c4-d2c3a6480c97",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-25T08:31:28.420Z_

The file is 101KB but 0 lines - it's likely binary or has no newlines. Let me check its actual content structure.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "673ff51b-4cc3-4505-9ca6-f2683d8676b2",
  "isSidechain": true,
  "agentId": "a10e81c6866b67bf0",
  "requestId": "req_011CbNyY2GrNFVRMgW3zHKcC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7c75c281-be74-42f5-979b-88cd6b4afcae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01SzkSB97t78WtWrRZUBSqjM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1410,
      "cache_read_input_tokens": 27406,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1410,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-25T08:31:30.585Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01QkWF768bc4AnbHdg77ftXi`</summary>

```json
{
  "command": "FILE=\"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating--claude-sessions-paper-agent-d1ae4a98/0b0cdf03-4218-4267-be3a-fa2b7e05fc58/tool-results/mcp-agent-ml-research-read_registry-1779697863127.txt\"\n# Check the first 500 bytes\npython3 -c \"\nwith open('$FILE', 'rb') as f:\n    data = f.read(500)\nprint(repr(data[:500]))\n\"",
  "description": "Probe file structure - first 500 bytes"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7c75c281-be74-42f5-979b-88cd6b4afcae",
  "isSidechain": true,
  "agentId": "a10e81c6866b67bf0",
  "requestId": "req_011CbNyY2GrNFVRMgW3zHKcC",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "86ead87b-b608-4f8b-bca3-bc8beed399ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01SzkSB97t78WtWrRZUBSqjM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1410,
      "cache_read_input_tokens": 27406,
      "output_tokens": 268,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1410
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 268,
          "cache_read_input_tokens": 27406,
          "cache_creation_input_tokens": 1410,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1410,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-25T08:31:30.695Z_

<details><summary>↩ Tool result · `toolu_01QkWF768bc4AnbHdg77ftXi`</summary>

```text
b'{"result":"{\\"success\\": true, \\"data\\": {\\"experiments\\": {\\"phase2_tf_ar_switching\\": {\\"status\\": \\"QUEUED\\", \\"retry_count\\": 0, \\"created_at\\": \\"2026-05-25T06:15:36.221Z\\", \\"updated_at\\": \\"2026-05-25T06:45:27.338Z\\", \\"hypothesis\\": \\"TF\xe2\x86\x92AR switching at turn k (k=1..5) on ThreadGate s42 checkpoint. If GAR drops abruptly at the switch point (matching pure-AR level within 1 turn), it confirms exposure bias as instantaneous distribution shift rather than gradual cumulative drift.\\"}, \\"ph'
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "86ead87b-b608-4f8b-bca3-bc8beed399ad",
  "isSidechain": true,
  "promptId": "7f6d57ff-336a-4102-9549-9590b20d9c0f",
  "agentId": "a10e81c6866b67bf0",
  "type": "user",
  "uuid": "b18a3a67-f688-48d2-9c61-cafa5aafd48f",
  "sourceToolAssistantUUID": "86ead87b-b608-4f8b-bca3-bc8beed399ad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-25T08:31:35.760Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01XtAvDFam1huN7QVptv5q82`</summary>

```json
{
  "command": "FILE=\"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating--claude-sessions-paper-agent-d1ae4a98/0b0cdf03-4218-4267-be3a-fa2b7e05fc58/tool-results/mcp-agent-ml-research-read_registry-1779697863127.txt\"\npython3 -c \"\nimport json, yaml\nwith open('$FILE', 'r', encoding='utf-8') as f:\n    raw = f.read()\n\n# Parse outer JSON\nouter = json.loads(raw)\nresult_str = outer['result']\n\n# Parse inner JSON\ninner = json.loads(result_str)\nprint('Top-level keys:', list(inner.keys()))\nprint('Success:', inner.get('success'))\nif 'data' in inner:\n    print('Data keys:', list(inner['data'].keys()))\n    experiments = inner['data'].get('experiments', {})\n    print('Experiment IDs:', list(experiments.keys()))\n\"",
  "description": "Parse JSON structure and list all experiment IDs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b18a3a67-f688-48d2-9c61-cafa5aafd48f",
  "isSidechain": true,
  "agentId": "a10e81c6866b67bf0",
  "requestId": "req_011CbNyYMWz7aQ5tuPgGNBSd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8e8704db-5063-4975-b82a-f34630f549ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01SzHJUUraR3tJeu3WLNovfh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 476,
      "cache_read_input_tokens": 28816,
      "output_tokens": 344,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 476
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 344,
          "cache_read_input_tokens": 28816,
          "cache_creation_input_tokens": 476,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 476,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-25T08:31:35.888Z_

<details><summary>↩ Tool result · `toolu_01XtAvDFam1huN7QVptv5q82`</summary>

```text
Top-level keys: ['success', 'data', 'error', 'metadata']
Success: True
Data keys: ['experiments', 'count', 'total', 'baseline']
Experiment IDs: ['phase2_tf_ar_switching', 'phase1a_multiseed_qwen', 'phase1a_multiseed_8runs', 'phase1b_llama_complement', 'p1_llama_ss_eval', 'p1_llama_ss_training', 'mmlu_eval_all', 'p2_llama_gradient_conflict', 'p1_tf_ar_kl_divergence', 'qwen15b_phase1_diag', 'd048_eval_ss_s456', 'd048_ss_s456', 'p0_ss_steering_eval', 'd048_eval_ss_s123', 'd048_ss_s123', 'd048_split_softmax_eval', 'd048_final_ar_eval', 'd048_queue_runner', 'd048_eval_ss_s42', 'd048_ss_s42', 'd048_ss_s42_resume', 'eval_llama_ar_n20', 'eval_llama_lora_only_s42', 'llama_lora_only_s42', 'phase2_tg_s42_v6', 'phase2_tg_s42', 'eval_v7_tg_s123', 'eval_v8b_ss_s123', 'v7_tg_s123', 'v8b_ss_s123', 'llama_tg_training', 'llama_ar_matched_eval', 'instruction_retention_test', 'llama_eval_s42', 'llama_tg_s42', 'attention_steering_gen_n50', 'phase2_tg_s42_v8b_resume', 'llama_phase1_gar_diag', 'eval_v8b_ss', 'attention_steering_eval200_tf', 'trc_baseline_v7_tg', 'attention_steering_v7_tg_gen', 'phase2_tg_s42_v8b_ss_fixed', 'phase2_tg_s42_v7', 'phase2_tg_s42_v9_pcgrad', 'phase2_lora_only_s42', 'phase2_ug_s42', 'phase2_tg_s42_v8_schedsampling', 'analysis_attention_heatmap', 'analysis_gradient_conflict', 'phase2_4way_eval_heldout', 'phase2_4way_eval', 'phase2_tg_s42_v5', 'phase2_tg_s42_v4', 'phase2_tg_s42_v3b', 'phase2_tg_s42_v3', 'phase2_tg_s42_v2', 'phase1_gar_diag']
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8e8704db-5063-4975-b82a-f34630f549ab",
  "isSidechain": true,
  "promptId": "7f6d57ff-336a-4102-9549-9590b20d9c0f",
  "agentId": "a10e81c6866b67bf0",
  "type": "user",
  "uuid": "5f9c3609-d446-4310-b121-005e165ad892",
  "sourceToolAssistantUUID": "8e8704db-5063-4975-b82a-f34630f549ab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-25T08:31:40.650Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01BAzZzMP4M6X2ioFVbDxhrN`</summary>

```json
{
  "command": "FILE=\"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating--claude-sessions-paper-agent-d1ae4a98/0b0cdf03-4218-4267-be3a-fa2b7e05fc58/tool-results/mcp-agent-ml-research-read_registry-1779697863127.txt\"\npython3 -c \"\nimport json\n\nwith open('$FILE', 'r', encoding='utf-8') as f:\n    raw = f.read()\n\nouter = json.loads(raw)\ninner = json.loads(outer['result'])\nexperiments = inner['data']['experiments']\n\n# Print all experiments with full detail\nimport pprint\nfor exp_id, exp_data in experiments.items():\n    print('='*80)\n    print(f'EXP_ID: {exp_id}')\n    pprint.pprint(exp_data)\n    print()\n\" 2>&1 | head -2000",
  "description": "Print all experiments with full details"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5f9c3609-d446-4310-b121-005e165ad892",
  "isSidechain": true,
  "agentId": "a10e81c6866b67bf0",
  "requestId": "req_011CbNyYjkTJB5K2ihopQscL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "33dffcac-1af0-4cc0-88f1-6382353b1bb1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01JTUpSyp856SFcmyw7EZMDq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1105,
      "cache_read_input_tokens": 29292,
      "output_tokens": 329,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1105
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 329,
          "cache_read_input_tokens": 29292,
          "cache_creation_input_tokens": 1105,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1105,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-25T08:31:40.827Z_

<details><summary>↩ Tool result · `toolu_01BAzZzMP4M6X2ioFVbDxhrN`</summary>

```text
&lt;persisted-output>
Output too large (99.6KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating--claude-sessions-paper-agent-d1ae4a98/0b0cdf03-4218-4267-be3a-fa2b7e05fc58/tool-results/bkc5vkabf.txt

Preview (first 2KB):
================================================================================
EXP_ID: phase2_tf_ar_switching
{'created_at': '2026-05-25T06:15:36.221Z',
 'hypothesis': 'TF→AR switching at turn k (k=1..5) on ThreadGate s42 '
               'checkpoint. If GAR drops abruptly at the switch point '
               '(matching pure-AR level within 1 turn), it confirms exposure '
               'bias as instantaneous distribution shift rather than gradual '
               'cumulative drift.',
 'retry_count': 0,
 'status': 'QUEUED',
 'updated_at': '2026-05-25T06:45:27.338Z'}

================================================================================
EXP_ID: phase1a_multiseed_qwen
{'created_at': '2026-05-25T06:15:26.051Z',
 'hypothesis': 'Multi-seed (s123, s456) training across 5 Qwen conditions '
               '(PCGrad, UG, LoRA-only, TG, SS) to establish mean±std for all '
               'claims. 8 training runs + AR eval N≥50 each. Expect TF '
               'convergence (GAR~0.50) and consistent AR rankings across '
               'seeds.',
 'retry_count': 0,
 'spec': {'checkpoint_path': 'runs/d048_{pcgrad,ug,lo,tg}_s{123,456}/',
          'command': 'bash scripts/phase1a_multiseed_runner.sh',
          'data_count': 2000,
          'data_path': '/root/turn-residual-gating/data/phase2_train.jsonl',
          'gpu': 0,
          'log_path': '/root/turn_residual_gating/logs/phase1a_multiseed.log',
          'model_name': 'Qwen/Qwen2.5-7B-Instruct',
          'notes': '8 sequential runs: PCGrad s123/s456, UG s123/s456, LO '
                   's123/s456, TG s456, SS s456(eval-only). Each run ~7h, '
                   'total ~56h. Auto AR eval N=50 after each.',
          'pid': 5508,
          'seed': '123,456 (multi-seed across 5 conditions)',
          'server': 'westd-20861'},
 'status': 'RUNNING',
 'updated_at': '2026-05-25T06:21:10.390Z'}

================================================================================
EXP_ID: phase1a_multiseed_8runs
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "33dffcac-1af0-4cc0-88f1-6382353b1bb1",
  "isSidechain": true,
  "promptId": "7f6d57ff-336a-4102-9549-9590b20d9c0f",
  "agentId": "a10e81c6866b67bf0",
  "type": "user",
  "uuid": "5a63dda7-5c90-496a-9b2e-d699dfaa73e3",
  "sourceToolAssistantUUID": "33dffcac-1af0-4cc0-88f1-6382353b1bb1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-25T08:31:46.596Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01V9beBgo6qjSVmzYUg6V3yf`</summary>

```json
{
  "command": "FILE=\"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating--claude-sessions-paper-agent-d1ae4a98/0b0cdf03-4218-4267-be3a-fa2b7e05fc58/tool-results/mcp-agent-ml-research-read_registry-1779697863127.txt\"\npython3 << 'EOF'\nimport json\n\nwith open(FILE, 'r', encoding='utf-8') as f:\n    raw = f.read()\n\nouter = json.loads(raw)\ninner = json.loads(outer['result'])\nexperiments = inner['data']['experiments']\n\n# Focus on experiments with results\nfor exp_id, exp_data in experiments.items():\n    if 'results' in exp_data or 'metrics' in exp_data:\n        print('='*80)\n        print(f'EXP_ID: {exp_id}')\n        print(f\"STATUS: {exp_data.get('status', 'N/A')}\")\n        if 'results' in exp_data:\n            print(\"RESULTS:\")\n            r = exp_data['results']\n            if isinstance(r, dict):\n                for k, v in r.items():\n                    print(f\"  {k}: {v}\")\n            else:\n                print(f\"  {r}\")\n        if 'metrics' in exp_data:\n            print(\"METRICS:\")\n            for k, v in exp_data['metrics'].items():\n                print(f\"  {k}: {v}\")\n        print()\nEOF",
  "description": "Extract all experiments with results/metrics fields"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5a63dda7-5c90-496a-9b2e-d699dfaa73e3",
  "isSidechain": true,
  "agentId": "a10e81c6866b67bf0",
  "requestId": "req_011CbNyZ7XtHmC7jaUiDeJHV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "06c16338-7bfa-468a-b1e3-e8473ba81bab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01DrjqPgSs4Hk3nnzMG93ayR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1142,
      "cache_read_input_tokens": 30397,
      "output_tokens": 474,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1142
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 474,
          "cache_read_input_tokens": 30397,
          "cache_creation_input_tokens": 1142,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1142,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-25T08:31:46.817Z_

<details><summary>↩ Tool result · reported error · `toolu_01V9beBgo6qjSVmzYUg6V3yf`</summary>

```text
Exit code 1
Traceback (most recent call last):
  File "&lt;stdin>", line 3, in &lt;module>
NameError: name 'FILE' is not defined
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "06c16338-7bfa-468a-b1e3-e8473ba81bab",
  "isSidechain": true,
  "promptId": "7f6d57ff-336a-4102-9549-9590b20d9c0f",
  "agentId": "a10e81c6866b67bf0",
  "type": "user",
  "uuid": "035904cb-01f9-4a92-885d-29658570fb61",
  "toolUseResult": "Error: Exit code 1\nTraceback (most recent call last):\n  File \"&lt;stdin>\", line 3, in &lt;module>\nNameError: name 'FILE' is not defined",
  "sourceToolAssistantUUID": "06c16338-7bfa-468a-b1e3-e8473ba81bab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-25T08:31:51.843Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01M3WmBGeAELZqtbuWdxczhE`</summary>

```json
{
  "command": "FILE=\"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating--claude-sessions-paper-agent-d1ae4a98/0b0cdf03-4218-4267-be3a-fa2b7e05fc58/tool-results/mcp-agent-ml-research-read_registry-1779697863127.txt\"\npython3 -c \"\nimport json\n\nwith open('$FILE', 'r', encoding='utf-8') as f:\n    raw = f.read()\n\nouter = json.loads(raw)\ninner = json.loads(outer['result'])\nexperiments = inner['data']['experiments']\n\n# Focus on experiments with results\nfor exp_id, exp_data in experiments.items():\n    if 'results' in exp_data or 'metrics' in exp_data:\n        print('='*80)\n        print(f'EXP_ID: {exp_id}')\n        print(f\\\"STATUS: {exp_data.get('status', 'N/A')}\\\")\n        if 'results' in exp_data:\n            print('RESULTS:')\n            r = exp_data['results']\n            if isinstance(r, dict):\n                for k, v in r.items():\n                    print(f'  {k}: {v}')\n            else:\n                print(f'  {r}')\n        if 'metrics' in exp_data:\n            print('METRICS:')\n            for k, v in exp_data['metrics'].items():\n                print(f'  {k}: {v}')\n        print()\n\" 2>&1",
  "description": "Extract experiments with results/metrics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "035904cb-01f9-4a92-885d-29658570fb61",
  "isSidechain": true,
  "agentId": "a10e81c6866b67bf0",
  "requestId": "req_011CbNyZYQrTAQSUTUysfUKR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9ee7a7b0-02d0-429a-a82f-3dce1658fa19",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01QJcRa9ExM9xKSzBvYsmQau",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 536,
      "cache_read_input_tokens": 31539,
      "output_tokens": 481,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 536
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 481,
          "cache_read_input_tokens": 31539,
          "cache_creation_input_tokens": 536,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 536,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-25T08:31:51.937Z_

<details><summary>↩ Tool result · `toolu_01M3WmBGeAELZqtbuWdxczhE`</summary>

```text
================================================================================
EXP_ID: p1_llama_ss_eval
STATUS: DONE
METRICS:
  ss_tf_gar: 0.477
  ss_tf_ppl: 2.82
  ss_ar_b0_gar: 0.1662
  ss_ar_b0_ppl: 1.37
  ss_ar_b5_gar: 0.7905
  ss_ar_b5_ppl: 1.81
  base_ar_gar: 0.0179
  base_ar_ppl: 1.22
  tf_ar_gap: 2.87

================================================================================
EXP_ID: mmlu_eval_all
STATUS: DONE
METRICS:
  base_qwen: 0.7423
  pcgrad_v9_s42: 0.7386
  ss_v8b_s42: 0.7375
  lo_s42: 0.7357
  tg_v7_s42: 0.7347
  ug_s42: 0.7346

================================================================================
EXP_ID: p2_llama_gradient_conflict
STATUS: DONE
METRICS:
  cos_sim_mean: 0.0045
  cos_sim_std: 0.07
  neg_cos_sim_layers_pct: 53.1
  mag_ratio_median: 25.7
  conclusion_note: cos_sim≈0 indicates near-orthogonal (NOT conflict). Script conclusion text 'widespread conflict' is misleading — actual finding: NTP and GAR gradients are nearly orthogonal on Llama, consistent with Qwen pattern.

================================================================================
EXP_ID: p1_tf_ar_kl_divergence
STATUS: DONE
METRICS:
  tg_delta_gar: 0.0165
  base_delta_gar: 0.0122
  tg_mean_kl: 0.054
  base_mean_kl: 0.043
  gate_kl_correlation: 0.11
  high_kl_layers: L23-L27, L9
  gar_robustness_ours_tg_base_ratio: 21.4
  gar_robustness_goal_only_ratio: 63
  gar_robustness_ours_all_ratio: 1.7
  gar_robustness_ours_first_ratio: 1.8

================================================================================
EXP_ID: d048_eval_ss_s456
STATUS: DONE
METRICS:
  tf_gar_ours_mid: 0.4964
  tf_gar_dongre_mid: 0.3862
  ar_beta0_gar: 0.4325
  ar_beta0_ppl: 1.4394
  ar_beta3_gar: 0.605
  ar_beta3_ppl: 1.5868
  ar_beta5_gar: 0.7157
  ar_beta5_ppl: 1.8045
  n_convs_ar: 50

================================================================================
EXP_ID: d048_eval_ss_s123
STATUS: DONE
METRICS:
  tf_gar_ours: 0.5536
  tf_gar_dongre: 0.4106
  tf_ppl: 2.6123
  ar_beta0_gar: 0.4231
  ar_beta0_ppl: 1.4408
  ar_beta3_gar: 0.5903
  ar_beta3_ppl: 1.607
  ar_beta5_gar: 0.7174
  ar_beta5_ppl: 1.7852
  n_convs_tf: 200
  n_convs_ar: 39

================================================================================
EXP_ID: d048_final_ar_eval
STATUS: DONE
METRICS:
  beta0: {'base_gar': 0.019, 'tg_gar': 0.064, 'ug_gar': 0.033, 'lo_gar': 0.037, 'pcgrad_gar': 0.03, 'ss_gar': 0.347}
  beta3: {'base_gar': 0.531, 'tg_gar': 0.556, 'ss_gar': 0.593}
  beta5: {'base_gar': 0.704, 'tg_gar': 0.727, 'ss_gar': 0.717}
  wilcoxon_beta0: {'tg_vs_base_p': '<0.001', 'tg_vs_base_r': 0.802, 'ss_vs_tg_p': '<0.001', 'ss_vs_tg_r': 0.869}
  ppl: {'base': 1.447, 'tg': 1.432, 'ss': 1.442}
  n_convs: 39

================================================================================
EXP_ID: d048_eval_ss_s42
STATUS: DONE
METRICS:
  tf: {'base_gar_ours_mid': 0.0128, 'base_gar_dongre_mid': 0.0031, 'base_ppl': 4.34, 'base_ntp': 1.4, 'tg_gar_ours_mid': 0.5025, 'tg_gar_dongre_mid': 0.389, 'tg_ppl': 2.78, 'tg_ntp': 0.98, 'baseline_mid_gar': 0.0122}
  ar: {'gar_ours_mid': 0.3887, 'gar_ours_ci_95': [0.3692, 0.3934], 'ppl': 1.35}
  gap_ratio: 1.29
  n_conversations_tf: 50
  n_conversations_ar: 5
  bootstrap_turns: curve[2:] (turns 3-T)
  note: AR used hardcoded N=5, not N=50. Will be re-evaluated in final unified batch with eval_200.json N=50.

================================================================================
EXP_ID: d048_ss_s42
STATUS: DONE
METRICS:
  final_avg_loss: 0.9326
  final_ntp_loss: 0.932
  final_gar_loss: 0.0007
  gate_mean: 0.9527
  gate_std: 0.0589
  gate_min: 0.7383
  gate_min_layer: L4
  gate_max: 1
  ss_usage: 4750/16000 (29.7%)
  ss_fallback: 0
  epochs_completed: 3
  wall_clock_s: 23418
  wall_clock_h: 6.5

================================================================================
EXP_ID: eval_llama_ar_n20
STATUS: DONE
METRICS:
  base: {'gar_ours_mean': 0.0088, 'gar_ours_std': 0.0056, 'gar_ours_median_per_conv': 0.0093, 'gar_ours_median_per_turn_pool': 0.0071, 'gar_ours_spike_ratio': '0%', 'gar_dongre_mean': 0.0049, 'gar_dongre_std': 0.0013, 'gar_dongre_median': 0.0047, 'ngar_ours_mid': 0.1019, 'ngar_dongre_mid': 0.1171, 'ppl': 1.293, 'ppl_std': 0.07, 'ntp_loss': 0.2552}
  tg: {'gar_ours_mean': 0.0434, 'gar_ours_std': 0.1002, 'gar_ours_median_per_conv': 0.0179, 'gar_ours_median_per_turn_pool': 0.0126, 'gar_ours_spike_ratio': '5% (2/40 turns GAR>=0.4)', 'gar_dongre_mean': 0.0183, 'gar_dongre_std': 0.0198, 'gar_dongre_median': 0.0152, 'ngar_ours_mid': 0.5357, 'ngar_dongre_mid': 0.4436, 'ppl': 1.437, 'ppl_std': 0.077, 'ntp_loss': 0.3612}
  lora_only: {'gar_ours_mean': 0.0284, 'gar_ours_std': 0.0481, 'gar_ours_median_per_conv': 0.0184, 'gar_ours_median_per_turn_pool': 0.0133, 'gar_ours_spike_ratio': '0%', 'gar_dongre_mean': 0.0205, 'gar_dongre_std': 0.0241, 'gar_dongre_median': 0.016, 'ngar_ours_mid': 0.3488, 'ngar_dongre_mid': 0.4997, 'ppl': 1.419, 'ppl_std': 0.075, 'ntp_loss': 0.3483}
  n_conversations: 20
  n_turns: 4
  mid_turns_definition: turns 3-T (0-indexed avg_gar[2:], excluding turns 1-2). All 16 eval entries use same definition.
  stat_pool: median_per_conv: median of 20 per-conversation mid-turn averages. median_per_turn_pool: median of 40 individual turn values (20 conv x 2 mid turns).
  ranking_gar_ours_mean: TG(0.0434) > LO(0.0284) > Base(0.0088)
  ranking_gar_ours_median_per_conv: TG(0.0179) ≈ LO(0.0184) > Base(0.0093)
  ranking_gar_ours_median_per_turn_pool: TG(0.0126) ≈ LO(0.0133) > Base(0.0071)
  ranking_gar_dongre: LO(0.0205) > TG(0.0183) > Base(0.0049)
  note: Paper §5.5 cites median_per_conv (median of per-conversation mid-turn averages across N=20). median_per_turn_pool is the alternative statistic from pooled individual turns. Both confirm TG ≈ LO (zero-increment).

================================================================================
EXP_ID: eval_llama_lora_only_s42
STATUS: DONE
METRICS:
  tf: {'gar_ours': 0.4807, 'gar_dongre': 0.0188, 'ngar_ours': 11.8031, 'ngar_dongre': 0.8261, 'ppl': 2.6, 'ntp_loss': 0.9366, 'n_conversations': 50, 'n_turns': 4}
  ar: {'gar_ours': 0.0617, 'gar_dongre': 0.0226, 'ngar_ours': 0.6065, 'ngar_dongre': 0.2537, 'ppl': 1.32, 'ntp_loss': 0.2787, 'n_conversations': 5, 'n_turns': 10}
  gap_ratio_gar_ours: 7.79

================================================================================
EXP_ID: llama_lora_only_s42
STATUS: DONE
METRICS:
  final_avg_loss: 0.9288
  final_avg_ntp: 0.9279
  final_avg_gar: 0.0009
  gate_fixed: 1
  gate_type: none
  wall_clock_s: 25317
  wall_clock_h: 7.03
  epochs_completed: 3

================================================================================
EXP_ID: phase2_tg_s42_v6
STATUS: DONE
METRICS:
  dryrun_step0_L_NTP: 2.0275
  dryrun_step0_L_GAR: -0.0161
  dryrun_step0_total_loss: 2.0114
  dryrun_step4_L_NTP: 1.6544
  dryrun_step4_L_GAR: -0.0147
  dryrun_step4_total_loss: 1.6397
  dryrun_gate_grad: True
  dryrun_gate_mean_init: 0.8097
  dryrun_gate_std_init: 0.0341
  dryrun_gate_min_init: 0.6836
  dryrun_gate_max_init: 0.8672
  dryrun_gate_mean_step5: 0.8025
  dryrun_gate_std_step5: 0.0842
  dryrun_gate_min_step5: 0.5547
  dryrun_gate_max_step5: 0.9805
  gs50_gate_mean: 0.8117
  gs50_gate_std: 0.0612
  gs50_gate_min: 0.6836
  gs50_gate_max: 0.9805
  gs100_gate_mean: 0.8737
  gs100_gate_std: 0.0367
  gs100_gate_min: 0.8164
  gs100_gate_max: 0.9766
  gs100_L_NTP: 0.8151
  gs100_L_GAR: -0.158
  gs100_total_loss: 0.6571
  gs100_profile_bottom3: L12=0.816 L4=0.824 L13=0.824
  gs100_profile_top3: L27=0.977 L26=0.961 L23=0.914
  gs143_L_GAR: -0.3876
  gs143_gate_mean: 0.9227

================================================================================
EXP_ID: phase2_tg_s42
STATUS: DONE
METRICS:
  final_ntp_loss: 0.94
  final_gar_loss: 0
  gate_mean: 0.988
  gar_loss_zero_pct: 87.6
  epochs_completed: 1.67
  killed_reason: SIGTERM by diagnose worker (unauthorized)

================================================================================
EXP_ID: eval_v7_tg_s123
STATUS: DONE
METRICS:
  iid_tf: {'gar_ours_mid': 0.5052, 'gar_dongre_mid': 0.0119, 'ppl': 2.7802, 'ntp': 0.9752}
  modelgen_ar: {'gar_ours_mid': 0.0165, 'gar_dongre_mid': 0.0177, 'ppl': 1.3855, 'ntp': 0.3223}
  gap_ratio: 30.6
  comparison_s42: {'tf_gar_ours_delta': 0.0017, 'ar_gar_ours_delta': 0.0008, 'gap_ratio_delta': -1.4}

================================================================================
EXP_ID: eval_v8b_ss_s123
STATUS: DONE
METRICS:
  iid: {'gar_ours': 0.503, 'gar_dongre': 0.394, 'ppl': 2.781, 'ntp_loss': 0.976, 'n_conv': 50, 'n_turns': 3}
  modelgen: {'gar_ours': 0.418, 'gar_dongre': 0.441, 'ppl': 1.389, 'ntp_loss': 0.325, 'n_conv': 5, 'n_turns': 10}
  gap_ratio: 1.2
  base_iid_ppl: 4.338
  base_modelgen_ppl: 1.351

================================================================================
EXP_ID: v7_tg_s123
STATUS: DONE
METRICS:
  epoch_1: {'avg_loss': 0.9447, 'avg_ntp_loss': 0.9434, 'avg_gar_loss': 0.0013, 'avg_div_loss': 0}
  epoch_2: {'avg_loss': 0.9315, 'avg_ntp_loss': 0.9305, 'avg_gar_loss': 0.001, 'avg_div_loss': 0}
  final_gate: {'mean': 0.9467, 'std': 0.051, 'min': 0.793, 'max': 1}
  final_gate_profile: {'L0': 0.883, 'L1': 0.793, 'L2': 0.996, 'L3': 0.988, 'L4': 0.984, 'L5': 0.797, 'L6': 0.961, 'L7': 0.918, 'L8': 0.965, 'L9': 0.934, 'L10': 0.969, 'L11': 0.918, 'L12': 0.926, 'L13': 0.941, 'L14': 0.93, 'L15': 0.965, 'L16': 0.941, 'L17': 0.91, 'L18': 0.961, 'L19': 0.965, 'L20': 0.973, 'L21': 0.988, 'L22': 0.969, 'L23': 0.98, 'L24': 0.98, 'L25': 0.984, 'L26': 0.988, 'L27': 1}
  training_time_s: 21425.2

================================================================================
EXP_ID: v8b_ss_s123
STATUS: DONE
METRICS:
  final_loss: 0.9316
  final_ntp_loss: 0.9307
  final_gar_loss: 0.0009
  final_gate_mean: 0.9505
  final_gate_std: 0.0508
  final_gate_min: 0.7383
  final_gate_max: 1
  ss_used_ratio: 0.371
  training_time_s: 38773.4
  epoch0_loss: 1.0092
  epoch1_loss: 0.9444
  epoch2_loss: 0.9316

================================================================================
EXP_ID: llama_ar_matched_eval
STATUS: DONE
METRICS:
  ar_base_ours: {'mid_gar': 0.0082, 'ngar': 0.1, 'ppl': 1.267}
  ar_tg_ours: {'mid_gar': 0.0388, 'ngar': 0.493, 'ppl': 1.413}
  ar_base_dongre: {'mid_gar': 0.0051, 'ngar': 0.12, 'ppl': 1.267}
  ar_tg_dongre: {'mid_gar': 0.018, 'ngar': 0.431, 'ppl': 1.413}
  tf_reference: {'tf_tg_ours_ngar': 11.88, 'tf_base_ours_ngar': 0.388, 'tf_tg_ours_raw': 0.4836, 'tf_tg_dongre_raw': 0.018}
  matched_gap_analysis: {'gar_ours_raw_gap': '12.5x (TF 0.484 / AR 0.039)', 'gar_ours_ngar_gap': '24.1x (TF 11.88 / AR 0.493)', 'gar_dongre_raw_gap': '1.002x (TF 0.018 / AR 0.018) — zero gap', 'tg_over_base_ar_ours': '4.71x', 'tg_over_base_ar_dongre': '3.54x', 'conclusion': 'GAR-ours TF-AR gap 12.5x (raw) / 24x (nGAR) is genuine exposure bias. GAR-Dongre zero gap (1.002x) confirms mechanism specificity: exposure bias selectively destroys learned goal-attention routing while leaving content-overlap-based attention unaffected.'}

================================================================================
EXP_ID: instruction_retention_test
STATUS: DONE
METRICS:
  late_turn_rate_beta0: 0.759
  late_turn_rate_beta3: 0.87
  late_turn_delta: 0.111
  mcnemar_chi2: 3.125
  mcnemar_p: 0.0771
  gar_compliance_r: 0.2003
  gar_compliance_p: 0.007
  category_content_constraint: {'beta0': 0.619, 'beta3': 0.857, 'delta': 0.238}
  category_count_constraint: {'beta0': 1, 'beta3': 1, 'delta': 0}
  category_format_constraint: {'beta0': 1, 'beta3': 1, 'delta': 0}
  category_position_constraint: {'beta0': 0.667, 'beta3': 0.733, 'delta': 0.067}

================================================================================
EXP_ID: llama_eval_s42
STATUS: DONE
METRICS:
  tf_base: {'gar_ours': 0.0166, 'ngar_ours': 0.3882, 'gar_dongre': 0.0038, 'ngar_dongre': 0.163, 'ppl': 3.45, 'N': 50, 'T': 4}
  tf_tg: {'gar_ours': 0.4836, 'ngar_ours': 11.8818, 'gar_dongre': 0.018, 'ngar_dongre': 0.7922, 'ppl': 2.57, 'N': 50, 'T': 4}
  ar_base: {'gar_ours': 0.0086, 'ngar_ours': 0.0798, 'gar_dongre': 0.0118, 'ngar_dongre': 0.1265, 'ppl': 1.24, 'N': 5, 'T': 10}
  ar_tg: {'gar_ours': 0.0304, 'ngar_ours': 0.2632, 'gar_dongre': 0.0217, 'ngar_dongre': 0.2459, 'ppl': 1.32, 'N': 5, 'T': 10}
  gap_ratio_tg_ours: 15.9
  gap_ratio_base_ours: 1.93
  gap_ratio_tg_dongre: 0.83
  vs_qwen_v7_gap_ratio: 32.1
  baseline_mid_gar: 0.0122

================================================================================
EXP_ID: llama_tg_s42
STATUS: DONE
METRICS:
  epochs_completed: 3
  total_steps: 3000
  wall_clock_seconds: 26212
  wall_clock_hours: 7.28
  final_avg_loss: 0.9233
  final_avg_ntp: 0.9224
  final_avg_gar: 0.0009
  final_avg_div: 0
  final_gate_mean: 0.9099
  final_gate_std: 0.0701
  final_gate_min: 0.7188
  final_gate_max: 0.9922
  gate_profile_step3000: {'L0': 0.957, 'L1': 0.973, 'L2': 0.977, 'L3': 0.965, 'L4': 0.992, 'L5': 0.969, 'L6': 0.957, 'L7': 0.957, 'L8': 0.961, 'L9': 0.949, 'L10': 0.938, 'L11': 0.934, 'L12': 0.969, 'L13': 0.953, 'L14': 0.957, 'L15': 0.965, 'L16': 0.953, 'L17': 0.961, 'L18': 0.922, 'L19': 0.902, 'L20': 0.883, 'L21': 0.863, 'L22': 0.836, 'L23': 0.844, 'L24': 0.809, 'L25': 0.719, 'L26': 0.762, 'L27': 0.805, 'L28': 0.801, 'L29': 0.855, 'L30': 0.898, 'L31': 0.934}
  checkpoint_size_gate_mb: 4.2
  checkpoint_size_lora_mb: 26
  gpu: NVIDIA RTX PRO 6000 Blackwell
  vram_gb: 102
  mem_used_gb: 63.4

================================================================================
EXP_ID: attention_steering_gen_n50
STATUS: DONE
METRICS:
  corrected: True
  aggregation: per-conv mid_gar(turns 2-7), >=3 turns only
  beta_0.0: {'mid_gar': 0.0641, 'mid_gar_std': 0.0809, 'ppl': 1.4324, 'ppl_std': 0.1029, 'n_valid': 39}
  beta_2.0: {'mid_gar': 0.128, 'mid_gar_std': 0.1101, 'ppl': 1.4822, 'ppl_std': 0.1385, 'n_valid': 39}
  beta_3.0: {'mid_gar': 0.5558, 'mid_gar_std': 0.0601, 'ppl': 1.5605, 'ppl_std': 0.1719, 'n_valid': 39}
  beta_4.0: {'mid_gar': 0.6439, 'mid_gar_std': 0.0607, 'ppl': 1.6674, 'ppl_std': 0.2241, 'n_valid': 39}
  beta_5.0: {'mid_gar': 0.7271, 'mid_gar_std': 0.0605, 'ppl': 1.7723, 'ppl_std': 0.2693, 'n_valid': 38}
  beta_10.0: {'mid_gar': 0.9612, 'mid_gar_std': 0.0152, 'ppl': 3.4517, 'ppl_std': 1.7813, 'n_valid': 39}
  n_convs_total: 50
  n_convs_valid: 39
  mode: gen
  phase_transition_range: [2, 3]

================================================================================
EXP_ID: phase2_tg_s42_v8b_resume
STATUS: DONE
METRICS:
  training: {'total_steps': 3000, 'epochs_completed': 3, 'wall_clock_hours': 8.1, 'final_loss': 0.933, 'final_ntp_loss': 0.9322, 'final_gar_loss': 0.0008, 'final_gate_mean': 0.9586, 'final_gate_std': 0.0582, 'ss_ratio': 0.5}
  eval_iid: {'gar_ours': 0.4983, 'gar_dongre': 0.3855, 'ppl': 2.78}
  eval_modelgen: {'gar_ours': 0.3177, 'gar_dongre': 0.3533, 'ppl': 1.38}
  vs_v7: {'iid_gar_ours_delta': -0.005, 'modelgen_gar_ours_delta': 0.302, 'gap_ratio_v7': 32, 'gap_ratio_v8b': 1.57}

================================================================================
EXP_ID: llama_phase1_gar_diag
STATUS: DONE
METRICS:
  per_turn_gar: {'turn_1': 0.0263, 'turn_2': 0.0183, 'turn_3': 0.0087, 'turn_4': 0.0055, 'turn_5': 0.006, 'turn_6': 0.0035, 'turn_7': 0.0038, 'turn_8': 0.0037, 'turn_9': 0.005, 'turn_10': 0.0026}
  t1_t10_decay_pct: 90.1
  t1_mid38_drop_pct: 80.2
  n_topics: 5
  model: Meta-Llama-3.1-8B-Instruct
  mode: gen
  n_conversations: 5
  n_turns: 10

================================================================================
EXP_ID: eval_v8b_ss
STATUS: DONE
METRICS:
  iid_gar_ours: 0.4983
  iid_gar_dongre: 0.3855
  iid_ppl: 2.78
  iid_ngar_ours: 13.5
  iid_ngar_dongre: 22.68
  modelgen_gar_ours: 0.3177
  modelgen_gar_dongre: 0.3533
  modelgen_ppl: 1.38
  modelgen_ngar_ours: 4.47
  modelgen_ngar_dongre: 5.92
  iid_turn1_gar_ours: 0.5398
  modelgen_turn1_gar_ours: 0.4333

================================================================================
EXP_ID: attention_steering_eval200_tf
STATUS: DONE
METRICS:
  beta_0.0: {'mid_gar': 0.5353, 'ppl': 2.62}
  beta_2.0: {'mid_gar': 0.6112, 'ppl': 2.69}
  beta_3.0: {'mid_gar': 0.788, 'ppl': 2.93}
  beta_4.0: {'mid_gar': 0.8165, 'ppl': 3.49}
  beta_5.0: {'mid_gar': 0.8325, 'ppl': 6.15}
  beta_10.0: {'mid_gar': 0.977, 'ppl': 505.21}
  n_convs: 200
  mode: tf

================================================================================
EXP_ID: trc_baseline_v7_tg
STATUS: DONE
METRICS:
  v7_tg: {'tf_trc': 0.3339, 'gen_trc': 0.3323, 'trc_gap': 0.0016, 'tf_tbp_ppl': 1.05, 'gen_tbp_ppl': 1.05}
  lora_only: {'tf_trc': 0.349, 'gen_trc': 0.4106, 'trc_gap': -0.0617, 'tf_tbp_ppl': 9.5, 'gen_tbp_ppl': 12}
  base: {'tf_trc': 0.1494, 'gen_trc': 0.1494, 'trc_gap': 0, 'tf_tbp_ppl': 2.05, 'gen_tbp_ppl': 2.05}

================================================================================
EXP_ID: attention_steering_v7_tg_gen
STATUS: DONE
METRICS:
  beta_0.0: {'mid_turns_avg_gar': 0.028, 'avg_ppl': 1.409}
  beta_0.5: {'mid_turns_avg_gar': 0.0287, 'avg_ppl': 1.387}
  beta_1.0: {'mid_turns_avg_gar': 0.0349, 'avg_ppl': 1.36}
  beta_2.0: {'mid_turns_avg_gar': 0.062, 'avg_ppl': 1.411}
  beta_5.0: {'mid_turns_avg_gar': 0.6795, 'avg_ppl': 1.908}
  beta_10.0: {'mid_turns_avg_gar': 0.959, 'avg_ppl': 4.22}
  phase_transition_range: [2, 5]
  baseline_gar: 0.028
  max_gar_at_acceptable_ppl: 0.6795
  max_gar_at_acceptable_ppl_beta: 5

================================================================================
EXP_ID: phase2_tg_s42_v7
STATUS: DONE
METRICS:
  eval_iid_ours_mid_gar: 0.5035
  eval_iid_dongre_mid_gar: 0.0152
  eval_iid_ppl: 2.784
  eval_heldout_ours_mid_gar: 0.5035
  eval_heldout_dongre_mid_gar: 0.0152
  eval_heldout_ppl: 2.78
  eval_modelgen_ours_mid_gar: 0.0157
  eval_modelgen_dongre_mid_gar: 0.0194
  eval_modelgen_ppl: 1.36
  gate_mean_final: 0.9336
  gate_std_final: 0.0492

================================================================================
EXP_ID: phase2_tg_s42_v9_pcgrad
STATUS: DONE
METRICS:
  eval_iid_ours_mid_gar: 0.5002
  eval_iid_dongre_mid_gar: 0.0123
  eval_iid_ppl: 2.78
  eval_iid_ntp: 0.9752
  eval_heldout_ours_mid_gar: 0.5002
  eval_heldout_dongre_mid_gar: 0.0123
  eval_heldout_ppl: 2.78
  eval_heldout_ntp: 0.9752
  eval_modelgen_ours_mid_gar: 0.0151
  eval_modelgen_dongre_mid_gar: 0.0173
  eval_modelgen_ppl: 1.5
  vs_v7_iid_ppl_diff: 0.004
  vs_v7_iid_gar_diff: -0.0033

================================================================================
EXP_ID: phase2_lora_only_s42
STATUS: DONE
METRICS:
  epochs_completed: 3
  global_steps: 3000
  training_time_seconds: 20588.6
  training_time_hours: 5.7
  gate_fixed: 1
  gate_type_actual: none
  final_lora_size_mb: 20
  eval_modelgen_ours_mid_gar: 0.0245
  eval_modelgen_dongre_mid_gar: 0.0185
  eval_modelgen_ppl: 1.371

================================================================================
EXP_ID: phase2_ug_s42
STATUS: DONE
METRICS:
  epoch0_avg_loss: 1.0019
  epoch0_avg_ntp: 0.9755
  epoch0_avg_gar: 0.0259
  epoch0_avg_div: 0.0005
  epoch1_avg_loss: 0.9447
  epoch1_avg_ntp: 0.9435
  epoch1_avg_gar: 0.0013
  epoch1_avg_div: 0
  epoch2_avg_loss: 0.9319
  epoch2_avg_ntp: 0.9309
  epoch2_avg_gar: 0.001
  epoch2_avg_div: 0
  final_gate_mean: 0.9598
  final_gate_std: 0.0518
  final_gate_min: 0.7773
  final_gate_max: 1
  final_profile_L3: 0.777
  final_profile_L5: 0.812
  final_profile_L0: 0.875
  final_profile_L27: 1
  training_time_seconds: 21994.5
  training_time_hours: 6.1
  global_steps: 7950
  unexpected_per_layer_variation: True
  eval_modelgen_ours_mid_gar: 0.0149
  eval_modelgen_dongre_mid_gar: 0.0185
  eval_modelgen_ppl: 1.396

================================================================================
EXP_ID: phase2_tg_s42_v8_schedsampling
STATUS: DONE
METRICS:
  killed_at_microstep: 1950
  total_microsteps: 24000
  completion_pct: 8.1
  global_step_approx: 244
  total_global_steps: 3000
  ss_steps_observed: 1
  tf_lgar_mean_step850_1400: 0.0062
  tf_lgar_std: 0.0082
  tf_lgar_collapse_step: 800
  gate_mean_final: 0.93
  ss_ratio_at_kill: 0.081
  crash_reason: killed by director: SS path code bug (D026) makes experiment invalid, GPU needed for PCGrad
  design_flaw_ss_ramp_too_slow: True
  design_flaw_no_ss_tf_separate_logging: True

================================================================================
EXP_ID: analysis_attention_heatmap
STATUS: DONE
METRICS:
  base_mean_goal_attn: 0.0136
  base_decay: 0.875
  tg_mean_goal_attn: 0.0232
  tg_decay: 0.777
  ug_mean_goal_attn: 0.0216
  ug_decay: 0.803
  lora_mean_goal_attn: 0.0216
  lora_decay: 0.81
  gating_incremental_benefit: none

================================================================================
EXP_ID: analysis_gradient_conflict
STATUS: DONE
METRICS:
  epoch0_cos_sim: -0.089
  epoch1_cos_sim: -0.054
  epoch2_cos_sim: -0.042
  epoch0_neg_layers_pct: 78.6
  epoch1_neg_layers_pct: 71.4
  epoch2_neg_layers_pct: 67.9
  epoch0_mag_ratio: 7.5
  epoch1_mag_ratio: 13.7
  epoch2_mag_ratio: 14.7

================================================================================
EXP_ID: phase2_4way_eval_heldout
STATUS: DONE
METRICS:
  base_ours_mid_gar: 0.0128
  base_ours_recovery_pp: 0.06
  base_dongre_mid_gar: 0.0031
  base_dongre_recovery_pp: -0.91
  base_ppl: 4.34
  base_ntp: 1.4045
  tg_ours_mid_gar: 0.5035
  tg_ours_recovery_pp: 49.13
  tg_dongre_mid_gar: 0.0152
  tg_dongre_recovery_pp: 0.3
  tg_ppl: 2.78
  tg_ntp: 0.9771
  ug_ours_mid_gar: 0.5053
  ug_ours_recovery_pp: 49.31
  ug_dongre_mid_gar: 0.0124
  ug_dongre_recovery_pp: 0.02
  ug_ppl: 2.78
  ug_ntp: 0.9752
  lora_ours_mid_gar: 0.4978
  lora_ours_recovery_pp: 48.56
  lora_dongre_mid_gar: 0.0132
  lora_dongre_recovery_pp: 0.1
  lora_ppl: 2.78
  lora_ntp: 0.9771
  three_way_convergence_confirmed: True
  gar_ours_spread_pp: 0.75
  ppl_spread: 0
  data_overlap: False

================================================================================
EXP_ID: phase2_4way_eval
STATUS: DONE
METRICS:
  base_ours_mid_gar: 0.0107
  base_ours_recovery_pp: -0.15
  base_dongre_mid_gar: 0.003
  base_dongre_recovery_pp: -0.92
  base_ppl: 4.23
  base_ntp: 1.4162
  tg_ours_mid_gar: 0.4866
  tg_ours_recovery_pp: 47.44
  tg_dongre_mid_gar: 0.0157
  tg_dongre_recovery_pp: 0.35
  tg_ppl: 2.63
  tg_ntp: 0.9484
  ug_ours_mid_gar: 0.4923
  ug_ours_recovery_pp: 48.01
  ug_dongre_mid_gar: 0.013
  ug_dongre_recovery_pp: 0.08
  ug_ppl: 2.62
  ug_ntp: 0.9433
  lora_ours_mid_gar: 0.486
  lora_ours_recovery_pp: 47.39
  lora_dongre_mid_gar: 0.0137
  lora_dongre_recovery_pp: 0.15
  lora_ppl: 2.63
  lora_ntp: 0.9482
  route_b_confirmed: True
  gating_incremental_benefit: none

================================================================================
EXP_ID: phase2_tg_s42_v5
STATUS: DONE
METRICS:
  step2000_gate_std: 0.0225
  step2000_gate_mean: 0.9586
  step2000_gate_min: 0.9062
  step2000_gate_max: 0.9961
  step2000_L_GAR: -0.8977
  step2000_L_NTP: 0.7611
  step2000_total_loss: -0.1365
  step2400_gate_std: 0.0219
  step2400_gate_mean: 0.9651
  step2400_gate_min: 0.918
  step2400_gate_max: 0.9961
  step2400_profile: L0=0.918 L12=0.918 L13=0.926 L1=0.996 L26=0.996
  L_GAR_saturated_at: -0.91
  gate_range_compression: 0.918-0.996

================================================================================
EXP_ID: phase2_tg_s42_v3b
STATUS: DONE
METRICS:
  gate_std_final: 0.087
  gate_mean_final: 0.9388
  gate_min_final: 0.5352
  gate_max_final: 0.9922
  L4_gate: 0.535
  L0_gate: 0.777
  L_NTP_final: 0.7787
  L_GAR_final: -0.9606
  elapsed_seconds: 3565.9
  optimizer_steps: 500
  gate_grad_received: True

================================================================================
EXP_ID: phase2_tg_s42_v3
STATUS: DONE
METRICS:
  gate_mean_step0: 0.8743
  gate_mean_step500: 0.8761
  gate_delta: 0.004
  gate_std: 0.001
  final_ntp_loss: 0.94
  final_gar_loss: -0.019
  gar_contribution_pct: 2-4%
  diagnosis: gate frozen, GAR indirect gradient too weak

================================================================================
EXP_ID: phase1_gar_diag
STATUS: DONE
METRICS:
  turn1_avg_gar: 0.0418
  mid_turns_avg_gar: 0.0122
  relative_drop: 0.708
  num_conversations: 5
  num_turns: 10
  per_turn_avg_gar: [0.0418, 0.0241, 0.0224, 0.013, 0.0133, 0.0086, 0.0078, 0.008, 0.0157, 0.0064]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9ee7a7b0-02d0-429a-a82f-3dce1658fa19",
  "isSidechain": true,
  "promptId": "7f6d57ff-336a-4102-9549-9590b20d9c0f",
  "agentId": "a10e81c6866b67bf0",
  "type": "user",
  "uuid": "b4a521f0-070f-480c-8245-1688de8e34fc",
  "sourceToolAssistantUUID": "9ee7a7b0-02d0-429a-a82f-3dce1658fa19",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-25T08:32:02.136Z_

<details open><summary>🔧 Tool call — Bash · `toolu_014FPjv5djMzK43JtBsyL9YR`</summary>

```json
{
  "command": "FILE=\"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating--claude-sessions-paper-agent-d1ae4a98/0b0cdf03-4218-4267-be3a-fa2b7e05fc58/tool-results/mcp-agent-ml-research-read_registry-1779697863127.txt\"\npython3 -c \"\nimport json\n\nwith open('$FILE', 'r', encoding='utf-8') as f:\n    raw = f.read()\n\nouter = json.loads(raw)\ninner = json.loads(outer['result'])\nexperiments = inner['data']['experiments']\n\n# Print all experiments WITHOUT results/metrics (check if they have notes/results in other fields)\nfor exp_id, exp_data in experiments.items():\n    if 'results' not in exp_data and 'metrics' not in exp_data:\n        print(f'EXP_ID: {exp_id} | STATUS: {exp_data.get(\\\"status\\\", \\\"N/A\\\")} | Fields: {list(exp_data.keys())}')\n\nprint()\nprint('--- baseline/count data ---')\nprint('Count:', inner['data']['count'])\nprint('Total:', inner['data']['total'])\nif inner['data'].get('baseline'):\n    import pprint\n    pprint.pprint(inner['data']['baseline'])\n\"",
  "description": "Check experiments without results and check baseline/count fields"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b4a521f0-070f-480c-8245-1688de8e34fc",
  "isSidechain": true,
  "agentId": "a10e81c6866b67bf0",
  "requestId": "req_011CbNyZvJEreG6JDwkQuMB2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e192d41c-7da2-4bf1-8ec4-d1ef80877203",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01GJBM6e3A4E13xSrUnufz6C",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12238,
      "cache_read_input_tokens": 32075,
      "output_tokens": 428,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 12238
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 428,
          "cache_read_input_tokens": 32075,
          "cache_creation_input_tokens": 12238,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 12238,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-25T08:32:02.224Z_

<details><summary>↩ Tool result · `toolu_014FPjv5djMzK43JtBsyL9YR`</summary>

```text
EXP_ID: phase2_tf_ar_switching | STATUS: QUEUED | Fields: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis']
EXP_ID: phase1a_multiseed_qwen | STATUS: RUNNING | Fields: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'spec']
EXP_ID: phase1a_multiseed_8runs | STATUS: PREPARING | Fields: ['status', 'retry_count', 'created_at', 'updated_at', 'spec']
EXP_ID: phase1b_llama_complement | STATUS: PREPARING | Fields: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis']
EXP_ID: p1_llama_ss_training | STATUS: DONE | Fields: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'spec', 'conclusion', 'completed_at']
EXP_ID: qwen15b_phase1_diag | STATUS: DONE | Fields: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'spec', 'conclusion', 'completed_at']
EXP_ID: d048_ss_s456 | STATUS: DONE | Fields: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'parent', 'spec', 'conclusion', 'completed_at']
EXP_ID: p0_ss_steering_eval | STATUS: PREPARING | Fields: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'parent', 'conclusion', 'notes']
EXP_ID: d048_ss_s123 | STATUS: DONE | Fields: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'parent', 'spec', 'conclusion', 'completed_at']
EXP_ID: d048_split_softmax_eval | STATUS: DONE | Fields: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'spec', 'conclusion', 'completed_at', 'notes']
EXP_ID: d048_queue_runner | STATUS: PREPARING | Fields: ['status', 'retry_count', 'created_at', 'updated_at', 'failure_reason', 'conclusion', 'extra', 'reproduce']
EXP_ID: d048_ss_s42_resume | STATUS: PREPARING | Fields: ['status', 'retry_count', 'created_at', 'updated_at', 'spec']
EXP_ID: llama_tg_training | STATUS: PREPARING | Fields: ['status', 'retry_count', 'created_at', 'updated_at', 'failure_reason', 'conclusion', 'extra', 'notes']
EXP_ID: phase2_tg_s42_v8b_ss_fixed | STATUS: DONE | Fields: ['status', 'retry_count', 'created_at', 'updated_at', 'spec', 'hypothesis', 'parent', 'failure_reason', 'conclusion', 'completed_at', 'notes']
EXP_ID: phase2_tg_s42_v4 | STATUS: DONE | Fields: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'parent', 'spec', 'conclusion', 'completed_at', 'notes']
EXP_ID: phase2_tg_s42_v2 | STATUS: DONE | Fields: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'parent', 'server', 'gpu', 'reproduce', 'spec', 'pid', 'log_path', 'conclusion', 'completed_at']

--- baseline/count data ---
Count: 58
Total: 58
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e192d41c-7da2-4bf1-8ec4-d1ef80877203",
  "isSidechain": true,
  "promptId": "7f6d57ff-336a-4102-9549-9590b20d9c0f",
  "agentId": "a10e81c6866b67bf0",
  "type": "user",
  "uuid": "ca2624ef-b2c1-4abc-9ce7-d57a81e66858",
  "sourceToolAssistantUUID": "e192d41c-7da2-4bf1-8ec4-d1ef80877203",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-25T08:32:11.451Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01DkHGYZxcq57KAdCjkNvA9E`</summary>

```json
{
  "command": "FILE=\"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating--claude-sessions-paper-agent-d1ae4a98/0b0cdf03-4218-4267-be3a-fa2b7e05fc58/tool-results/mcp-agent-ml-research-read_registry-1779697863127.txt\"\npython3 -c \"\nimport json\n\nwith open('$FILE', 'r', encoding='utf-8') as f:\n    raw = f.read()\n\nouter = json.loads(raw)\ninner = json.loads(outer['result'])\nexperiments = inner['data']['experiments']\n\n# Check DONE experiments without metrics for conclusions/notes\ndone_no_metrics = ['p1_llama_ss_training', 'qwen15b_phase1_diag', 'd048_ss_s456', \n                   'd048_ss_s123', 'd048_split_softmax_eval', 'phase2_tg_s42_v8b_ss_fixed',\n                   'phase2_tg_s42_v4', 'phase2_tg_s42_v2', 'p0_ss_steering_eval']\nfor exp_id in done_no_metrics:\n    exp = experiments[exp_id]\n    print(f'EXP_ID: {exp_id}')\n    if 'conclusion' in exp:\n        print(f'  CONCLUSION: {exp[\\\"conclusion\\\"]}')\n    if 'notes' in exp:\n        print(f'  NOTES: {exp[\\\"notes\\\"]}')\n    if 'extra' in exp:\n        print(f'  EXTRA: {exp[\\\"extra\\\"]}')\n    print()\n\"",
  "description": "Extract conclusions/notes from DONE experiments without metrics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ca2624ef-b2c1-4abc-9ce7-d57a81e66858",
  "isSidechain": true,
  "agentId": "a10e81c6866b67bf0",
  "requestId": "req_011CbNyagU52VPyqDjTwyLvZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "60bc1d89-5209-4056-be9a-2719cacd5072",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01AgSqEjx9YPu4pVZ76XrUzZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1463,
      "cache_read_input_tokens": 44313,
      "output_tokens": 518,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1463
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 518,
          "cache_read_input_tokens": 44313,
          "cache_creation_input_tokens": 1463,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1463,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-25T08:32:11.585Z_

<details><summary>↩ Tool result · `toolu_01DkHGYZxcq57KAdCjkNvA9E`</summary>

```text
EXP_ID: p1_llama_ss_training
  CONCLUSION: success

EXP_ID: qwen15b_phase1_diag
  CONCLUSION: success

EXP_ID: d048_ss_s456
  CONCLUSION: success

EXP_ID: d048_ss_s123
  CONCLUSION: success

EXP_ID: d048_split_softmax_eval
  CONCLUSION: failed
  NOTES: 2 critical bugs: (1) system_prompt_len=0 hardcoded at L373, (2) gen mode NaN for k≠1.0. Director decision 2026-05-23: not urgent, defer fix past DDL 5/25. Does not affect main paper experiments.

EXP_ID: phase2_tg_s42_v8b_ss_fixed
  CONCLUSION: failed
  NOTES: CUDA OOM at Epoch 1 Step 4300 (loss.backward). 其他进程共享 GPU 导致显存不足: Process 157667 (26.76GB) + Process 158713 (17.28GB) + PyTorch 自身 45.21GB + 4.81GB reserved > 94.97GB 总容量。训练在 OOM 前正常收敛 (SS ratio=0.5, Loss~1.0, Gate~0.94)。有 epoch_0 checkpoint。需要独占 GPU 重跑。

EXP_ID: phase2_tg_s42_v4
  CONCLUSION: failed
  NOTES: 进程在模型加载后崩溃，服务器重启导致进程丢失，无 checkpoint。日志仅有模型加载输出，无训练 step。GPU 重启后异常（100% util + 0 MiB + 无进程）。需要 GPU 健康恢复后重跑。

EXP_ID: phase2_tg_s42_v2
  CONCLUSION: killed

EXP_ID: p0_ss_steering_eval
  CONCLUSION: killed
  NOTES: Cancelled: ss_s42_ar_n50.json already contains SS+steering data at β=0,3,5. Results show SS and steering do not stack (β=5: SS 0.717 vs TG-only 0.727). Director decision: skip, use existing data.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "60bc1d89-5209-4056-be9a-2719cacd5072",
  "isSidechain": true,
  "promptId": "7f6d57ff-336a-4102-9549-9590b20d9c0f",
  "agentId": "a10e81c6866b67bf0",
  "type": "user",
  "uuid": "b4b0ee30-7c5c-4127-a86e-5be4d35d2dc5",
  "sourceToolAssistantUUID": "60bc1d89-5209-4056-be9a-2719cacd5072",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-25T08:32:17.117Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01VLgBaHyt6iu1R5EVzoYniR`</summary>

```json
{
  "command": "FILE=\"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating--claude-sessions-paper-agent-d1ae4a98/0b0cdf03-4218-4267-be3a-fa2b7e05fc58/tool-results/mcp-agent-ml-research-read_registry-1779697863127.txt\"\npython3 -c \"\nimport json\n\nwith open('$FILE', 'r', encoding='utf-8') as f:\n    raw = f.read()\n\nouter = json.loads(raw)\ninner = json.loads(outer['result'])\nexperiments = inner['data']['experiments']\n\n# Check remaining experiments with full details\nremaining = ['phase1a_multiseed_8runs', 'eval_llama_ar_n20', 'eval_v8b_ss_s123', 'eval_v8b_ss', 'eval_v7_tg_s123']\nfor exp_id in remaining:\n    exp = experiments[exp_id]\n    print(f'EXP_ID: {exp_id}')\n    import pprint\n    pprint.pprint(exp)\n    print()\n\"",
  "description": "Check remaining key experiments with full details"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b4b0ee30-7c5c-4127-a86e-5be4d35d2dc5",
  "isSidechain": true,
  "agentId": "a10e81c6866b67bf0",
  "requestId": "req_011CbNybNNQyfcMv8EtDMxc2",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ea16d451-9e51-48a9-92e3-225458cfd1eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_013PbJkHKdYQihY1V97aXN5y",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1226,
      "cache_read_input_tokens": 45776,
      "output_tokens": 378,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1226
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 378,
          "cache_read_input_tokens": 45776,
          "cache_creation_input_tokens": 1226,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1226,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-25T08:32:17.268Z_

<details><summary>↩ Tool result · `toolu_01VLgBaHyt6iu1R5EVzoYniR`</summary>

```text
EXP_ID: phase1a_multiseed_8runs
{'created_at': '2026-05-25T06:18:08.953Z',
 'retry_count': 0,
 'spec': {'account': 'root',
          'backend': 'tmux',
          'command': 'bash -c "bash '
                     '/root/turn_residual_gating/scripts/phase1a_multiseed_runner.sh"',
          'gpu': ['cuda:0'],
          'log_path': '~/runs/turn_residual_gating/phase1a_multiseed_8runs.log',
          'pid': '5508',
          'server': 'westd-20861',
          'submitted_at': '2026-05-25T06:18:08.495Z',
          'submitted_via': 'submit_training_job'},
 'status': 'PREPARING',
 'updated_at': '2026-05-25T06:18:08.953Z'}

EXP_ID: eval_llama_ar_n20
{'checkpoint_path': 'N/A',
 'completed_at': '2026-05-22T08:16:09.384Z',
 'conclusion': 'success',
 'created_at': '2026-05-22T07:52:04.543Z',
 'extra': {'hook_events': [{'action': 'agent',
                            'event': 'on_complete',
                            'ts': '2026-05-22T08:09:50.100538+00:00'}]},
 'hypothesis': 'N=20 AR eval stabilizes Llama 3-way (Base/TG/LoRA-only) '
               'autoregressive GAR estimates. N=5 suffered from outlier '
               'influence (3/5 conv had GAR>0.4 outlier turns); N=20 provides '
               'robust mean±std.',
 'log_path': '/root/runs/turn_residual_gating/eval_llama_ar_n20.log',
 'metrics': {'base': {'gar_dongre_mean': 0.0049,
                      'gar_dongre_median': 0.0047,
                      'gar_dongre_std': 0.0013,
                      'gar_ours_mean': 0.0088,
                      'gar_ours_median_per_conv': 0.0093,
                      'gar_ours_median_per_turn_pool': 0.0071,
                      'gar_ours_spike_ratio': '0%',
                      'gar_ours_std': 0.0056,
                      'ngar_dongre_mid': 0.1171,
                      'ngar_ours_mid': 0.1019,
                      'ntp_loss': 0.2552,
                      'ppl': 1.293,
                      'ppl_std': 0.07},
             'lora_only': {'gar_dongre_mean': 0.0205,
                           'gar_dongre_median': 0.016,
                           'gar_dongre_std': 0.0241,
                           'gar_ours_mean': 0.0284,
                           'gar_ours_median_per_conv': 0.0184,
                           'gar_ours_median_per_turn_pool': 0.0133,
                           'gar_ours_spike_ratio': '0%',
                           'gar_ours_std': 0.0481,
                           'ngar_dongre_mid': 0.4997,
                           'ngar_ours_mid': 0.3488,
                           'ntp_loss': 0.3483,
                           'ppl': 1.419,
                           'ppl_std': 0.075},
             'mid_turns_definition': 'turns 3-T (0-indexed avg_gar[2:], '
                                     'excluding turns 1-2). All 16 eval '
                                     'entries use same definition.',
             'n_conversations': 20,
             'n_turns': 4,
             'note': 'Paper §5.5 cites median_per_conv (median of '
                     'per-conversation mid-turn averages across N=20). '
                     'median_per_turn_pool is the alternative statistic from '
                     'pooled individual turns. Both confirm TG ≈ LO '
                     '(zero-increment).',
             'ranking_gar_dongre': 'LO(0.0205) > TG(0.0183) > Base(0.0049)',
             'ranking_gar_ours_mean': 'TG(0.0434) > LO(0.0284) > Base(0.0088)',
             'ranking_gar_ours_median_per_conv': 'TG(0.0179) ≈ LO(0.0184) > '
                                                 'Base(0.0093)',
             'ranking_gar_ours_median_per_turn_pool': 'TG(0.0126) ≈ LO(0.0133) '
                                                      '> Base(0.0071)',
             'stat_pool': 'median_per_conv: median of 20 per-conversation '
                          'mid-turn averages. median_per_turn_pool: median of '
                          '40 individual turn values (20 conv x 2 mid turns).',
             'tg': {'gar_dongre_mean': 0.0183,
                    'gar_dongre_median': 0.0152,
                    'gar_dongre_std': 0.0198,
                    'gar_ours_mean': 0.0434,
                    'gar_ours_median_per_conv': 0.0179,
                    'gar_ours_median_per_turn_pool': 0.0126,
                    'gar_ours_spike_ratio': '5% (2/40 turns GAR>=0.4)',
                    'gar_ours_std': 0.1002,
                    'ngar_dongre_mid': 0.4436,
                    'ngar_ours_mid': 0.5357,
                    'ntp_loss': 0.3612,
                    'ppl': 1.437,
                    'ppl_std': 0.077}},
 'notes': 'N=20 AR eval stabilizes estimates. **mid_turns = turns 3-T '
          '(0-indexed avg_gar[2:], excluding turns 1-2; all 16 eval entries '
          'use same definition)**. Two median levels: median_per_conv (paper '
          '§5.5 cites this: TG 0.0179, LO 0.0184, Base 0.0093) = median of 20 '
          'per-conversation mid-turn averages; median_per_turn_pool (TG '
          '0.0126, LO 0.0133, Base 0.0071) = median of 40 pooled individual '
          'turns. Both confirm TG ≈ LO (zero-increment). Mean (TG 0.0434 > LO '
          '0.0284) driven by outlier spikes (TG std=0.1002, 5% turns GAR≥0.4; '
          'LO std=0.0481, 0% spikes). PPL: Base(1.29) < LO(1.42) < TG(1.44). '
          'Pending paper fix: §5.5 says "turns 2-T" but code excludes turns '
          '1-2; will correct to "excluding the first two turns" in next paper '
          'edit batch.',
 'parent': 'eval_llama_lora_only_s42',
 'reproduce': {'finished_at': '2026-05-22T08:09:48.181Z'},
 'retry_count': 0,
 'spec': {'account': 'root',
          'backend': 'tmux',
          'checkpoint_source': 'llama_tg_s42 + llama_lora_only_s42',
          'command': 'bash -c "source /root/miniconda3/etc/profile.d/conda.sh '
                     '&& conda activate base && cd /root/turn_residual_gating '
                     '&& bash scripts/eval_llama_ar_n20.sh"',
          'data_count': 20,
          'data_path': 'ultrachat_200k + model-gen AR',
          'eval_data': 'AR-generated 20 conversations x 4 turns',
          'gpu': ['cuda:0'],
          'gpu_hours': 0.4,
          'log_path': '~/runs/turn_residual_gating/eval_llama_ar_n20.log',
          'model_name': 'Llama-3.1-8B-Instruct (Base/TG/LoRA-only)',
          'pid': '312592',
          'seed': 42,
          'server': 'westd-20861',
          'submitted_at': '2026-05-22T07:52:13.830Z',
          'submitted_via': 'submit_training_job',
          'wall_clock_seconds': 1435.6},
 'status': 'DONE',
 'updated_at': '2026-05-22T08:38:33.680Z'}

EXP_ID: eval_v8b_ss_s123
{'completed_at': '2026-05-21T22:53:08.443Z',
 'conclusion': 'success',
 'created_at': '2026-05-21T21:15:52.880Z',
 'hypothesis': 'v8b SS model trained with s123 seed should reproduce s42 GAR '
               'metrics within acceptable gap_ratio [1.2x-2.5x] and no PPL '
               'degradation, confirming seed robustness of the scheduled '
               'sampling approach',
 'log_path': '~/runs/turn_residual_gating/eval_v8b_ss_s123.log',
 'metrics': {'base_iid_ppl': 4.338,
             'base_modelgen_ppl': 1.351,
             'gap_ratio': 1.2,
             'iid': {'gar_dongre': 0.394,
                     'gar_ours': 0.503,
                     'n_conv': 50,
                     'n_turns': 3,
                     'ntp_loss': 0.976,
                     'ppl': 2.781},
             'modelgen': {'gar_dongre': 0.441,
                          'gar_ours': 0.418,
                          'n_conv': 5,
                          'n_turns': 10,
                          'ntp_loss': 0.325,
                          'ppl': 1.389}},
 'parent': 'v7_tg_s123',
 'retry_count': 0,
 'spec': {'account': 'root',
          'backend': 'tmux',
          'checkpoint_path': 'checkpoints/tg_v8b_ss_s123/epoch_2',
          'checkpoint_source': 'checkpoints/tg_v8b_ss_s123/epoch_2',
          'command': 'bash scripts/eval_v8b_ss_s123.sh',
          'data_count': 50,
          'data_path': 'data/ultrachat_eval_heldout.json',
          'eval_data': 'ultrachat_eval_heldout + model-gen',
          'gpu': ['cuda:0'],
          'gpu_hours': 1.62,
          'gpu_index': 0,
          'log_path': 'runs/eval_v8b_ss_s123/',
          'model_name': 'Qwen2.5-7B-Instruct',
          'pid': 259767,
          'seed': 123,
          'server': 'westd-20861',
          'submitted_at': '2026-05-21T21:15:52.785Z',
          'submitted_via': 'submit_training_job',
          'wall_clock_seconds': 5835.7},
 'status': 'DONE',
 'updated_at': '2026-05-21T22:53:15.356Z'}

EXP_ID: eval_v8b_ss
{'completed_at': '2026-05-20T18:45:14.523Z',
 'conclusion': 'success',
 'created_at': '2026-05-20T18:44:23.366Z',
 'hypothesis': 'Scheduled Sampling (linear 0→0.5 mixing of teacher-forced and '
               'model-gen contexts) closes the 30x training-inference GAR gap '
               'by reducing exposure bias, resulting in model-gen GAR '
               'significantly above v7 baseline (0.016) while preserving IID '
               'GAR and PPL.',
 'metrics': {'iid_gar_dongre': 0.3855,
             'iid_gar_ours': 0.4983,
             'iid_ngar_dongre': 22.68,
             'iid_ngar_ours': 13.5,
             'iid_ppl': 2.78,
             'iid_turn1_gar_ours': 0.5398,
             'modelgen_gar_dongre': 0.3533,
             'modelgen_gar_ours': 0.3177,
             'modelgen_ngar_dongre': 5.92,
             'modelgen_ngar_ours': 4.47,
             'modelgen_ppl': 1.38,
             'modelgen_turn1_gar_ours': 0.4333},
 'parent': 'phase2_tg_s42_v8b_ss',
 'retry_count': 0,
 'spec': {'checkpoint_path': 'checkpoints/tg_v8b_ss_fixed_s42',
          'checkpoint_source': 'checkpoints/tg_v8b_ss_fixed_s42',
          'command': 'python src/eval_phase2_gar.py --checkpoint-dir '
                     'checkpoints/tg_v8b_ss_fixed_s42 --gate-type threadgate',
          'data_count': '50 heldout + 5 model-gen',
          'data_path': 'data/ultrachat_eval_heldout.json + built-in 5conv '
                       'model-gen',
          'eval_data': 'ultrachat_eval_heldout.json (IID) + built-in model-gen '
                       '(5x10 turns)',
          'log_path': '/tmp/eval_v8b_all.log',
          'model_name': 'Qwen2.5-7B-Instruct',
          'seed': 42,
          'server': 'westd-20861'},
 'status': 'DONE',
 'updated_at': '2026-05-20T18:45:14.523Z'}

EXP_ID: eval_v7_tg_s123
{'completed_at': '2026-05-22T00:30:42.606Z',
 'conclusion': 'success',
 'created_at': '2026-05-21T22:53:18.163Z',
 'hypothesis': 'v7 TG s123 eval: 验证 s123 seed 的 TF-AR GAR gap 与 s42 '
               '一致（~32×），确认 multi-seed robustness',
 'metrics': {'comparison_s42': {'ar_gar_ours_delta': 0.0008,
                                'gap_ratio_delta': -1.4,
                                'tf_gar_ours_delta': 0.0017},
             'gap_ratio': 30.6,
             'iid_tf': {'gar_dongre_mid': 0.0119,
                        'gar_ours_mid': 0.5052,
                        'ntp': 0.9752,
                        'ppl': 2.7802},
             'modelgen_ar': {'gar_dongre_mid': 0.0177,
                             'gar_ours_mid': 0.0165,
                             'ntp': 0.3223,
                             'ppl': 1.3855}},
 'parent': 'v7_tg_s123',
 'retry_count': 0,
 'spec': {'account': 'root',
          'backend': 'tmux',
          'checkpoint_path': '/root/turn_residual_gating/runs/phase2_tg_s123_v7/epoch_2',
          'checkpoint_source': 'v7_tg_s123',
          'command': 'bash scripts/eval_v7_tg_s123.sh',
          'data_count': 8000,
          'data_path': 'data/ultrachat_8k',
          'eval_data': 'data/ultrachat_8k',
          'gpu': ['cuda:0'],
          'gpu_hours': 1.62,
          'log_path': '/root/turn_residual_gating/logs/v7_tg_s123.log',
          'model_name': 'Qwen2.5-7B-Instruct',
          'pid': '264869',
          'seed': 123,
          'server': 'westd-20861',
          'submitted_at': '2026-05-21T22:53:18.065Z',
          'submitted_via': 'submit_training_job',
          'wall_clock_seconds': 5844.5},
 'status': 'DONE',
 'updated_at': '2026-05-22T00:30:49.653Z'}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ea16d451-9e51-48a9-92e3-225458cfd1eb",
  "isSidechain": true,
  "promptId": "7f6d57ff-336a-4102-9549-9590b20d9c0f",
  "agentId": "a10e81c6866b67bf0",
  "type": "user",
  "uuid": "aa13cdfa-45d0-4557-a714-e357d6bfa529",
  "sourceToolAssistantUUID": "ea16d451-9e51-48a9-92e3-225458cfd1eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-25T08:32:28.034Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Eqf7reSHxoxN7BWhibmwFY`</summary>

```json
{
  "command": "FILE=\"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating--claude-sessions-paper-agent-d1ae4a98/0b0cdf03-4218-4267-be3a-fa2b7e05fc58/tool-results/mcp-agent-ml-research-read_registry-1779697863127.txt\"\npython3 -c \"\nimport json\n\nwith open('$FILE', 'r', encoding='utf-8') as f:\n    raw = f.read()\n\nouter = json.loads(raw)\ninner = json.loads(outer['result'])\nexperiments = inner['data']['experiments']\n\n# Check remaining experiments\nremaining = ['d048_eval_ss_s456', 'd048_final_ar_eval', 'd048_eval_ss_s42', 'trc_baseline_v7_tg',\n             'p1_llama_ss_eval', 'p2_llama_gradient_conflict', 'p1_tf_ar_kl_divergence',\n             'instruction_retention_test']\nfor exp_id in remaining:\n    exp = experiments[exp_id]\n    print(f'EXP_ID: {exp_id}')\n    import pprint\n    # Just print training config/spec details\n    if 'spec' in exp:\n        spec = exp['spec']\n        print(f'  SEED: {spec.get(\\\"seed\\\", \\\"N/A\\\")}')\n        print(f'  MODEL: {spec.get(\\\"model_name\\\", \\\"N/A\\\")}')\n        print(f'  LR: {spec.get(\\\"learning_rate\\\", spec.get(\\\"lr\\\", \\\"N/A\\\"))}')\n        print(f'  BATCH: {spec.get(\\\"batch_size\\\", \\\"N/A\\\")}')\n        print(f'  EPOCHS: {spec.get(\\\"epochs\\\", spec.get(\\\"num_epochs\\\", \\\"N/A\\\"))}')\n    print()\n\"",
  "description": "Check training configs for key experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aa13cdfa-45d0-4557-a714-e357d6bfa529",
  "isSidechain": true,
  "agentId": "a10e81c6866b67bf0",
  "requestId": "req_011CbNybncRypeopdDy67zaz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1c4ee2df-cdc4-4007-acaa-2eb2f1cd7462",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01JwHywjsz4WYE9667DkhuU9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5022,
      "cache_read_input_tokens": 47002,
      "output_tokens": 581,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5022
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 581,
          "cache_read_input_tokens": 47002,
          "cache_creation_input_tokens": 5022,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5022,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-25T08:32:28.140Z_

<details><summary>↩ Tool result · `toolu_01Eqf7reSHxoxN7BWhibmwFY`</summary>

```text
EXP_ID: d048_eval_ss_s456
  SEED: 456
  MODEL: Qwen/Qwen2.5-7B-Instruct + SS s456 LoRA
  LR: N/A
  BATCH: N/A
  EPOCHS: N/A

EXP_ID: d048_final_ar_eval
  SEED: 42
  MODEL: Qwen/Qwen2.5-7B-Instruct
  LR: N/A
  BATCH: N/A
  EPOCHS: N/A

EXP_ID: d048_eval_ss_s42
  SEED: 42
  MODEL: Qwen2.5-7B-Instruct (SS s42)
  LR: N/A
  BATCH: N/A
  EPOCHS: N/A

EXP_ID: trc_baseline_v7_tg
  SEED: 42
  MODEL: Qwen2.5-7B-Instruct
  LR: N/A
  BATCH: N/A
  EPOCHS: N/A

EXP_ID: p1_llama_ss_eval
  SEED: 42
  MODEL: meta-llama/Llama-3.1-8B-Instruct
  LR: N/A
  BATCH: N/A
  EPOCHS: N/A

EXP_ID: p2_llama_gradient_conflict
  SEED: 42
  MODEL: meta-llama/Llama-3.1-8B-Instruct
  LR: N/A
  BATCH: N/A
  EPOCHS: N/A

EXP_ID: p1_tf_ar_kl_divergence
  SEED: 42
  MODEL: Qwen/Qwen2.5-7B-Instruct
  LR: N/A
  BATCH: N/A
  EPOCHS: N/A

EXP_ID: instruction_retention_test
  SEED: 42
  MODEL: Qwen2.5-7B-Instruct + v7 TG LoRA
  LR: N/A
  BATCH: N/A
  EPOCHS: N/A
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1c4ee2df-cdc4-4007-acaa-2eb2f1cd7462",
  "isSidechain": true,
  "promptId": "7f6d57ff-336a-4102-9549-9590b20d9c0f",
  "agentId": "a10e81c6866b67bf0",
  "type": "user",
  "uuid": "89964608-8d2f-4300-8192-e2264071dc3d",
  "sourceToolAssistantUUID": "1c4ee2df-cdc4-4007-acaa-2eb2f1cd7462",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-25T08:32:36.846Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01HCiFZByHUYnbNANvVss5u2`</summary>

```json
{
  "command": "FILE=\"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating--claude-sessions-paper-agent-d1ae4a98/0b0cdf03-4218-4267-be3a-fa2b7e05fc58/tool-results/mcp-agent-ml-research-read_registry-1779697863127.txt\"\npython3 -c \"\nimport json\n\nwith open('$FILE', 'r', encoding='utf-8') as f:\n    raw = f.read()\n\nouter = json.loads(raw)\ninner = json.loads(outer['result'])\nexperiments = inner['data']['experiments']\n\n# Get full spec for training experiments to find lr, batch_size\ntraining_exps = ['phase2_tg_s42_v7', 'phase2_lora_only_s42', 'phase2_ug_s42', 'phase2_tg_s42_v9_pcgrad',\n                 'phase2_tg_s42_v8b_resume', 'v7_tg_s123', 'v8b_ss_s123', 'llama_tg_s42', 'llama_lora_only_s42',\n                 'd048_ss_s42', 'd048_ss_s123', 'd048_ss_s456']\nfor exp_id in training_exps:\n    exp = experiments[exp_id]\n    print(f'EXP_ID: {exp_id}')\n    if 'spec' in exp:\n        import pprint\n        spec = exp['spec']\n        for key in ['seed', 'model_name', 'learning_rate', 'lr', 'batch_size', 'per_device_train_batch_size', \n                    'gradient_accumulation_steps', 'epochs', 'num_epochs', 'num_train_epochs',\n                    'max_steps', 'warmup_steps', 'lora_r', 'lora_alpha', 'weight_decay',\n                    'data_count', 'data_path']:\n            if key in spec:\n                print(f'  {key}: {spec[key]}')\n    print()\n\"",
  "description": "Extract training hyperparameters for key training experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "89964608-8d2f-4300-8192-e2264071dc3d",
  "isSidechain": true,
  "agentId": "a10e81c6866b67bf0",
  "requestId": "req_011CbNycb6fP5tscZi8BVmi3",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bd306ca0-81ea-4623-936d-80b10dcb40f4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01G85NGZK1xGdQY1TdP9hmoJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1149,
      "cache_read_input_tokens": 52024,
      "output_tokens": 634,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1149
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 634,
          "cache_read_input_tokens": 52024,
          "cache_creation_input_tokens": 1149,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1149,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-25T08:32:36.955Z_

<details><summary>↩ Tool result · `toolu_01HCiFZByHUYnbNANvVss5u2`</summary>

```text
EXP_ID: phase2_tg_s42_v7
  seed: 42
  model_name: Qwen2.5-7B-Instruct
  data_count: 8000
  data_path: /root/turn_residual_gating/data/ultrachat_8k

EXP_ID: phase2_lora_only_s42
  seed: 42
  model_name: Qwen2.5-7B-Instruct
  data_count: 8000
  data_path: /root/turn_residual_gating/data/ultrachat_8k

EXP_ID: phase2_ug_s42
  seed: 42
  model_name: Qwen2.5-7B-Instruct
  data_count: 8000
  data_path: /root/turn_residual_gating/data/ultrachat_8k

EXP_ID: phase2_tg_s42_v9_pcgrad

EXP_ID: phase2_tg_s42_v8b_resume
  seed: 42
  model_name: Qwen2.5-7B-Instruct
  data_count: 8000
  data_path: data/ultrachat_8k

EXP_ID: v7_tg_s123
  seed: 123
  model_name: Qwen2.5-7B-Instruct
  data_count: 8000
  data_path: data/ultrachat_8k

EXP_ID: v8b_ss_s123
  seed: 123
  model_name: Qwen2.5-7B-Instruct
  data_count: 8000
  data_path: data/ultrachat_8k

EXP_ID: llama_tg_s42
  seed: 42
  model_name: Meta-Llama-3.1-8B-Instruct
  data_count: 8000
  data_path: data/ultrachat_8k

EXP_ID: llama_lora_only_s42
  seed: 42
  model_name: Meta-Llama-3.1-8B-Instruct
  data_count: 8000
  data_path: /root/turn_residual_gating/data/ultrachat_8k

EXP_ID: d048_ss_s42

EXP_ID: d048_ss_s123
  seed: 123
  model_name: Qwen/Qwen2.5-7B-Instruct
  data_count: 2000
  data_path: /root/turn-residual-gating/data/phase2_train.jsonl

EXP_ID: d048_ss_s456
  seed: 456
  model_name: Qwen/Qwen2.5-7B-Instruct
  data_count: 2000
  data_path: /root/turn-residual-gating/data/phase2_train.jsonl
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bd306ca0-81ea-4623-936d-80b10dcb40f4",
  "isSidechain": true,
  "promptId": "7f6d57ff-336a-4102-9549-9590b20d9c0f",
  "agentId": "a10e81c6866b67bf0",
  "type": "user",
  "uuid": "f494c7f6-3ec0-426d-abbc-c3f18399a6c4",
  "sourceToolAssistantUUID": "bd306ca0-81ea-4623-936d-80b10dcb40f4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-25T08:32:42.133Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01QQvMtFakt47hB4nasVJUbo`</summary>

```json
{
  "command": "FILE=\"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating--claude-sessions-paper-agent-d1ae4a98/0b0cdf03-4218-4267-be3a-fa2b7e05fc58/tool-results/mcp-agent-ml-research-read_registry-1779697863127.txt\"\npython3 -c \"\nimport json\n\nwith open('$FILE', 'r', encoding='utf-8') as f:\n    raw = f.read()\n\nouter = json.loads(raw)\ninner = json.loads(outer['result'])\nexperiments = inner['data']['experiments']\n\n# Get full spec for these training experiments\nfor exp_id in ['phase2_tg_s42_v9_pcgrad', 'phase2_tg_s42_v7', 'phase2_lora_only_s42', 'phase2_ug_s42', 'llama_tg_s42', 'llama_lora_only_s42']:\n    exp = experiments[exp_id]\n    print(f'EXP_ID: {exp_id}')\n    import pprint\n    if 'spec' in exp:\n        pprint.pprint(exp['spec'])\n    elif 'hypothesis' in exp:\n        print(f'  hypothesis: {exp[\\\"hypothesis\\\"]}')\n    print()\n\"",
  "description": "Get full spec for main training experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f494c7f6-3ec0-426d-abbc-c3f18399a6c4",
  "isSidechain": true,
  "agentId": "a10e81c6866b67bf0",
  "requestId": "req_011CbNydEpJTWCCuABcfJnSD",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c06fe7df-6a6d-47fd-bcc9-8307026b2cdf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01TaP6jtufVUM7j7L2qBzqVM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1403,
      "cache_read_input_tokens": 53173,
      "output_tokens": 431,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1403
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 431,
          "cache_read_input_tokens": 53173,
          "cache_creation_input_tokens": 1403,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1403,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-25T08:32:42.256Z_

<details><summary>↩ Tool result · `toolu_01QQvMtFakt47hB4nasVJUbo`</summary>

```text
EXP_ID: phase2_tg_s42_v9_pcgrad
{'account': 'root',
 'backend': 'tmux',
 'checkpoint_path': '/root/turn_residual_gating/checkpoints/tg_v9_pcgrad_s42',
 'command': 'bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda '
            'activate base && cd /root/turn_residual_gating && '
            'PYTHONUNBUFFERED=1 python src/train_phase2_v9_pcgrad.py --model '
            '/root/.cache/modelscope/Qwen/Qwen2___5-7B-Instruct --data-dir '
            'data/ultrachat_8k --output-dir checkpoints/tg_v9_pcgrad_s42 '
            '--gate-type threadgate --gar-loss-mode mse_target --gar-target '
            '0.5 --lambda-gar 1.0 --lambda-gate-div 1.0 --init-bias 1.5 '
            '--gate-lr-multiplier 10 --lr 2e-4 --epochs 3 --batch-size 1 '
            '--grad-accum 8 --seed 42"',
 'gpu': ['cuda:0'],
 'gpu_hours': 8.5,
 'log_path': '/root/turn_residual_gating/logs/phase2_tg_v9_pcgrad_s42.log',
 'pid': '83860',
 'server': 'westd-20861',
 'submitted_at': '2026-05-19T17:42:10.820Z',
 'submitted_via': 'submit_training_job',
 'wall_clock_seconds': 30601.5}

EXP_ID: phase2_tg_s42_v7
{'checkpoint_path': '/root/turn_residual_gating/runs/phase2_tg_s42_v7',
 'checkpoint_source': 'from_scratch',
 'command': 'bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda '
            'activate base && cd /root/turn_residual_gating && '
            'PYTHONUNBUFFERED=1 python src/train_phase2.py --gate-type '
            'threadgate --gar-loss-mode mse_target --gar-target 0.5 '
            '--lambda-gar 1.0 --lambda-gate-div 1.0 --min-gate-std 0.05 '
            '--init-bias 1.5 --gate-lr-multiplier 10 --max-seq-len 2048 --seed '
            '42 --output-dir /root/turn_residual_gating/runs/phase2_tg_s42_v7 '
            '--data-dir /root/turn_residual_gating/data/ultrachat_8k --epochs '
            '3"',
 'data_count': 8000,
 'data_path': '/root/turn_residual_gating/data/ultrachat_8k',
 'eval_data': 'N/A',
 'gpu': 'cuda:0',
 'log_path': '/root/turn_residual_gating/runs/phase2_tg_s42_v7.log',
 'model_name': 'Qwen2.5-7B-Instruct',
 'seed': 42,
 'server': 'westd-20861'}

EXP_ID: phase2_lora_only_s42
{'checkpoint_path': '/root/turn_residual_gating/runs/phase2_lora_only_s42',
 'checkpoint_source': 'from_scratch',
 'command': 'bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda '
            'activate base && cd /root/turn_residual_gating && '
            'PYTHONUNBUFFERED=1 python src/train_phase2.py --gate-type '
            'lora_only --gar-loss-mode mse_target --gar-target 0.5 '
            '--lambda-gar 1.0 --lambda-gate-div 0.0 --init-bias 1.5 '
            '--gate-lr-multiplier 10 --max-seq-len 2048 --seed 42 --output-dir '
            '/root/turn_residual_gating/runs/phase2_lora_only_s42 --data-dir '
            '/root/turn_residual_gating/data/ultrachat_8k --epochs 3"',
 'data_count': 8000,
 'data_path': '/root/turn_residual_gating/data/ultrachat_8k',
 'eval_data': 'N/A',
 'gpu': 'cuda:0',
 'log_path': '/root/turn_residual_gating/runs/phase2_lora_only_s42.log',
 'model_name': 'Qwen2.5-7B-Instruct',
 'seed': 42,
 'server': 'westd-20861'}

EXP_ID: phase2_ug_s42
{'checkpoint_path': '/root/turn_residual_gating/runs/phase2_ug_s42',
 'checkpoint_source': 'from_scratch',
 'command': 'python src/train_phase2.py --gate-type uniform --gar-loss-mode '
            'mse_target --gar-target 0.5 --lambda-gar 1.0 --lambda-gate-div '
            '1.0 --min-gate-std 0.05 --init-bias 1.5 --gate-lr-multiplier 10 '
            '--max-seq-len 2048 --seed 42 --output-dir '
            '/root/turn_residual_gating/runs/phase2_ug_s42 --data-dir '
            '/root/turn_residual_gating/data/ultrachat_8k --epochs 3',
 'data_count': 8000,
 'data_path': '/root/turn_residual_gating/data/ultrachat_8k',
 'eval_data': 'N/A',
 'log_path': '/root/turn_residual_gating/runs/phase2_ug_s42.log',
 'model_name': 'Qwen2.5-7B-Instruct',
 'seed': 42,
 'server': 'westd-20861'}

EXP_ID: llama_tg_s42
{'checkpoint_path': '/root/turn_residual_gating/runs/phase2_llama_tg_s42',
 'checkpoint_source': 'N/A (training from scratch)',
 'command': 'CUDA_VISIBLE_DEVICES=0 PYTHONUNBUFFERED=1 python '
            'src/train_phase2.py --model '
            '/root/autodl-tmp/models/LLM-Research/Meta-Llama-3___1-8B-Instruct '
            '--data-dir data/ultrachat_8k --output-dir '
            'runs/phase2_llama_tg_s42 --gate-type threadgate --gar-loss-mode '
            'mse_target --gar-target 0.5 --lambda-gar 1.0 --lambda-gate-div '
            '1.0 --init-bias 1.5 --gate-lr-multiplier 10 --lr 2e-4 --epochs 3 '
            '--batch-size 1 --grad-accum 8 --seed 42',
 'data_count': 8000,
 'data_path': 'data/ultrachat_8k',
 'eval_data': 'N/A (training experiment)',
 'gpu': ['cuda:0'],
 'log_path': '/root/turn_residual_gating/logs/llama_tg_training.log',
 'model_name': 'Meta-Llama-3.1-8B-Instruct',
 'pid': '199643',
 'seed': 42,
 'server': 'westd-20861'}

EXP_ID: llama_lora_only_s42
{'account': 'root',
 'backend': 'tmux',
 'checkpoint_path': 'runs/phase2_llama_lora_only_s42/epoch_2',
 'checkpoint_source': 'N/A (training from scratch, ablation baseline)',
 'command': 'bash scripts/launch_llama_lora_only_s42.sh',
 'data_count': 8000,
 'data_path': '/root/turn_residual_gating/data/ultrachat_8k',
 'eval_data': 'N/A (training run, not eval)',
 'gpu': ['cuda:0'],
 'gpu_hours': 7.1,
 'log_path': 'logs/llama_lora_only_s42.log',
 'model_name': 'Meta-Llama-3.1-8B-Instruct',
 'pid': '271741',
 'seed': 42,
 'server': 'westd-20861',
 'submitted_at': '2026-05-22T00:33:16.591Z',
 'submitted_via': 'submit_training_job',
 'wall_clock_seconds': 25550.3}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c06fe7df-6a6d-47fd-bcc9-8307026b2cdf",
  "isSidechain": true,
  "promptId": "7f6d57ff-336a-4102-9549-9590b20d9c0f",
  "agentId": "a10e81c6866b67bf0",
  "type": "user",
  "uuid": "c9cc0077-b09c-4984-a345-cfc3f6bf8f37",
  "sourceToolAssistantUUID": "c06fe7df-6a6d-47fd-bcc9-8307026b2cdf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-25T08:32:50.085Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01VTtiU6d22CASnXceVk4AXS`</summary>

```json
{
  "command": "FILE=\"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating--claude-sessions-paper-agent-d1ae4a98/0b0cdf03-4218-4267-be3a-fa2b7e05fc58/tool-results/mcp-agent-ml-research-read_registry-1779697863127.txt\"\npython3 -c \"\nimport json\n\nwith open('$FILE', 'r', encoding='utf-8') as f:\n    raw = f.read()\n\nouter = json.loads(raw)\ninner = json.loads(outer['result'])\nexperiments = inner['data']['experiments']\n\n# Get phase2_tg_s42_v8b_resume full spec  \nfor exp_id in ['phase2_tg_s42_v8b_resume', 'v8b_ss_s123', 'v7_tg_s123']:\n    exp = experiments[exp_id]\n    print(f'EXP_ID: {exp_id}')\n    import pprint\n    if 'spec' in exp:\n        pprint.pprint(exp['spec'])\n    print()\n\"",
  "description": "Get full spec for SS training experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c9cc0077-b09c-4984-a345-cfc3f6bf8f37",
  "isSidechain": true,
  "agentId": "a10e81c6866b67bf0",
  "requestId": "req_011CbNyddU55QTDSqditv7Tx",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eb595bd5-27d1-4d10-a3ce-013d21d5f1d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Qe7JiqCahksBwqsffniKAe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2892,
      "cache_read_input_tokens": 54576,
      "output_tokens": 375,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2892
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 375,
          "cache_read_input_tokens": 54576,
          "cache_creation_input_tokens": 2892,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2892,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-25T08:32:50.218Z_

<details><summary>↩ Tool result · `toolu_01VTtiU6d22CASnXceVk4AXS`</summary>

```text
EXP_ID: phase2_tg_s42_v8b_resume
{'checkpoint_path': 'checkpoints/tg_v8b_ss_fixed_s42',
 'checkpoint_source': 'phase2_tg_s42_v8b_ss_fixed/epoch_0',
 'command': 'python src/train_phase2_v8b.py --model '
            '/root/.cache/modelscope/Qwen/Qwen2___5-7B-Instruct --data-dir '
            'data/ultrachat_8k --output-dir checkpoints/tg_v8b_ss_fixed_s42 '
            '--gate-type threadgate --gar-loss-mode mse_target --gar-target '
            '0.5 --lambda-gar 1.0 --lambda-gate-div 1.0 --init-bias 1.5 '
            '--gate-lr-multiplier 10 --lr 2e-4 --epochs 3 --batch-size 1 '
            '--grad-accum 8 --seed 42 --scheduled-sampling --ss-max-ratio 0.5 '
            '--resume checkpoints/tg_v8b_ss_fixed_s42/epoch_0',
 'data_count': 8000,
 'data_path': 'data/ultrachat_8k',
 'eval_data': 'N/A (training experiment)',
 'log_path': '~/runs/turn_residual_gating/phase2_tg_s42_v8b_resume.log',
 'model_name': 'Qwen2.5-7B-Instruct',
 'seed': 42,
 'server': 'westd-20861'}

EXP_ID: v8b_ss_s123
{'checkpoint_path': '/root/turn_residual_gating/checkpoints/tg_v8b_ss_s123',
 'checkpoint_source': 'N/A (from scratch)',
 'command': 'bash scripts/launch_v8b_ss_s123.sh',
 'data_count': 8000,
 'data_path': 'data/ultrachat_8k',
 'eval_data': 'N/A',
 'log_path': '/root/turn_residual_gating/logs/v8b_ss_s123.log',
 'model_name': 'Qwen2.5-7B-Instruct',
 'seed': 123,
 'server': 'westd-20861'}

EXP_ID: v7_tg_s123
{'checkpoint_path': '/root/turn_residual_gating/runs/phase2_tg_s123_v7',
 'checkpoint_source': 'N/A (from scratch)',
 'command': 'bash scripts/launch_v7_tg_s123.sh',
 'data_count': 8000,
 'data_path': 'data/ultrachat_8k',
 'eval_data': 'N/A',
 'gpu_index': 0,
 'log_path': '/root/turn_residual_gating/logs/v7_tg_s123.log',
 'model_name': 'Qwen2.5-7B-Instruct',
 'pid': 245628,
 'seed': 123,
 'server': 'westd-20861'}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eb595bd5-27d1-4d10-a3ce-013d21d5f1d1",
  "isSidechain": true,
  "promptId": "7f6d57ff-336a-4102-9549-9590b20d9c0f",
  "agentId": "a10e81c6866b67bf0",
  "type": "user",
  "uuid": "959adba5-9fba-4d60-b1a8-16353949212a",
  "sourceToolAssistantUUID": "eb595bd5-27d1-4d10-a3ce-013d21d5f1d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet"
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-25T08:32:52.453Z_

Now I have all the data. Let me compile the comprehensive structured summary:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "959adba5-9fba-4d60-b1a8-16353949212a",
  "isSidechain": true,
  "agentId": "a10e81c6866b67bf0",
  "requestId": "req_011CbNyeDYRrLPwxs2fkMnWX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7e5b0bba-bf85-4ac0-95a7-b8d380a14989",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_0115ZcZP4U7ZeMQoapXnytQy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1252,
      "cache_read_input_tokens": 57468,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1252,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-25T08:32:57.563Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01CDTWgoj3iq7PiYDii5NWWu`</summary>

```json
{
  "command": "FILE=\"/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating--claude-sessions-paper-agent-d1ae4a98/0b0cdf03-4218-4267-be3a-fa2b7e05fc58/tool-results/mcp-agent-ml-research-read_registry-1779697863127.txt\"\npython3 -c \"\nimport json\n\nwith open('$FILE', 'r', encoding='utf-8') as f:\n    raw = f.read()\n\nouter = json.loads(raw)\ninner = json.loads(outer['result'])\nexperiments = inner['data']['experiments']\n\n# Check remaining experiments: trc, gradient conflict, attention steering, kl divergence\nfor exp_id in ['trc_baseline_v7_tg', 'analysis_gradient_conflict', 'p2_llama_gradient_conflict',\n               'attention_steering_gen_n50', 'attention_steering_eval200_tf', 'attention_steering_v7_tg_gen',\n               'p1_tf_ar_kl_divergence', 'mmlu_eval_all']:\n    exp = experiments[exp_id]\n    print(f'EXP_ID: {exp_id}')\n    import pprint\n    if 'spec' in exp:\n        pprint.pprint(exp['spec'])\n    if 'hypothesis' in exp:\n        print(f'  HYPOTHESIS: {exp[\\\"hypothesis\\\"]}')\n    print()\n\"",
  "description": "Check specs for analysis experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7e5b0bba-bf85-4ac0-95a7-b8d380a14989",
  "isSidechain": true,
  "agentId": "a10e81c6866b67bf0",
  "requestId": "req_011CbNyeDYRrLPwxs2fkMnWX",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2193062c-b3ad-408c-bbad-dd83ced9f5c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_0115ZcZP4U7ZeMQoapXnytQy",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1252,
      "cache_read_input_tokens": 57468,
      "output_tokens": 472,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1252
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 472,
          "cache_read_input_tokens": 57468,
          "cache_creation_input_tokens": 1252,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1252,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-25T08:32:57.757Z_

<details><summary>↩ Tool result · `toolu_01CDTWgoj3iq7PiYDii5NWWu`</summary>

```text
EXP_ID: trc_baseline_v7_tg
{'account': 'root',
 'backend': 'tmux',
 'checkpoint_path': '/root/turn_residual_gating/runs/trc_baseline/',
 'checkpoint_source': 'phase2_tg_s42_v7 + phase2_lora_only_s42 + base',
 'command': 'bash scripts/launch_trc_baseline.sh',
 'data_count': 5,
 'data_path': '/root/turn_residual_gating/data/standard_conversations.json',
 'eval_data': '5 hardcoded multi-turn conversations x 10 turns',
 'gpu': ['cuda:0'],
 'gpu_hours': 2.16,
 'log_path': '/root/runs/turn_residual_gating/trc_baseline_v7_tg.log',
 'model_name': 'Qwen2.5-7B-Instruct',
 'pid': '158700',
 'seed': 42,
 'server': 'westd-20861',
 'submitted_at': '2026-05-20T07:18:38.202Z',
 'submitted_via': 'submit_training_job',
 'wall_clock_seconds': 7767.7}
  HYPOTHESIS: 如果 exposure bias 对 auxiliary objectives 的破坏跨特征空间通用，那么 TRC (hidden state cos_sim) 在 model-gen 下也应出现与 GAR (attention 空间) 类似的 TF/gen gap。在 v7 TG / LoRA-only / base 三个 checkpoint 上测量 TRC baseline，确认 gap 是否存在。成功标准：gen TRC 显著低于 TF TRC。

EXP_ID: analysis_gradient_conflict
{'checkpoint_path': 'N/A (analysis)',
 'checkpoint_source': 'phase2_tg_s42_v7',
 'command': 'gradient conflict analysis script',
 'data_count': 3,
 'data_path': 'v7 epoch 0/1/2 checkpoints',
 'eval_data': 'v7 3-epoch checkpoints (gradient analysis)',
 'log_path': 'westd-20861:/root/turn_residual_gating/runs/analysis/',
 'model_name': 'Qwen2.5-7B-Instruct',
 'seed': 42,
 'server': 'westd-20861'}
  HYPOTHESIS: NTP-GAR 梯度冲突在 v7 训练过程中是否逐层普遍存在？量化 cos_sim 和 magnitude ratio 的演化，验证 NTP 是否在训练中逐渐完全压制 GAR 信号。

EXP_ID: p2_llama_gradient_conflict
{'checkpoint_path': 'results/p2_llama_gradient_conflict/',
 'command': 'bash scripts/p2_llama_gradient_conflict.sh',
 'data_count': 400,
 'data_path': '/root/turn-residual-gating/data/train_400.json',
 'log_path': 'logs/p2_llama_gradient_conflict.log',
 'model_name': 'meta-llama/Llama-3.1-8B-Instruct',
 'seed': 42,
 'server': 'westd-20861'}
  HYPOTHESIS: PCGrad fails to improve AR GAR on Llama-3.1-8B (as on Qwen), confirming cross-model that gradient conflict is not the root cause of the TF-AR gap, strengthening C2 (causal exclusion).

EXP_ID: attention_steering_gen_n50
{'checkpoint_path': 'N/A (eval experiment)',
 'checkpoint_source': 'phase2_tg_s42_v7',
 'command': 'CUDA_VISIBLE_DEVICES=0 python src/eval_attention_steering.py '
            '--checkpoint runs/phase2_tg_s42_v7 --mode gen --data-file '
            'data/eval_200/eval_200.json --max-convs 50 --beta 0 2 3 4 5 10 '
            '--output-dir runs/attention_steering/ --output-name '
            'attention_steering_gen_n50',
 'data_count': 50,
 'data_path': 'data/eval_200/eval_200.json',
 'eval_data': '50 conversations from eval_200.json, gen mode autoregressive',
 'gpu': ['cuda:0'],
 'log_path': '/root/turn_residual_gating/runs/attention_steering/attention_steering_gen_n50.json',
 'model_name': 'Qwen2.5-7B-Instruct + v7 TG LoRA',
 'seed': 'N/A (eval)',
 'server': 'westd-20861'}
  HYPOTHESIS: N=5 gen steering 显示 β∈[2,5] phase transition (GAR 0.06→0.68)，但样本量不足以报告置信区间。N=50 conversations 应重现同一 phase transition pattern 并提供统计鲁棒的 mean±std，加固 C6 claim (attention steering as causal mechanism proof)。

EXP_ID: attention_steering_eval200_tf
{'checkpoint_path': 'checkpoints/tg_v7_s42/final',
 'checkpoint_source': 'phase2_tg_s42_v7',
 'command': 'python src/eval_attention_steering.py --mode tf --betas 0 2 3 4 5 '
            '10 --output-name eval200_attention_steering.json (data: '
            'eval_200/eval_200.json, 200 convs)',
 'data_count': 200,
 'data_path': 'data/eval_200/eval_200.json',
 'eval_data': 'data/eval_200/eval_200.json',
 'log_path': '/tmp/eval200_steering.log',
 'model_name': 'Qwen2.5-7B-Instruct',
 'seed': 42,
 'server': 'westd-20861'}
  HYPOTHESIS: N=200 TF 模式 attention steering 验证 β-GAR 关系的统计鲁棒性。在 teacher-forced context (无 exposure bias) 下，steering 效果应更温和（baseline GAR 已 ~0.50），但仍展示 β 调控 attention 的能力。与 N=5 gen 模式结果互补：tf 验证机制可控性，gen 验证因果闭环。

EXP_ID: attention_steering_v7_tg_gen
{'account': 'root',
 'backend': 'tmux',
 'checkpoint_path': 'checkpoints/tg_v7_s42/final',
 'checkpoint_source': 'phase2_tg_s42_v7',
 'command': 'bash scripts/launch_attention_steering.sh gen',
 'data_count': 5,
 'data_path': 'data/ShareGPT_V3_format_5convs.json',
 'eval_data': 'data/ShareGPT_V3_format_5convs.json',
 'gpu': ['cuda:0'],
 'gpu_hours': 2.38,
 'log_path': 'runs/attention_steering/phase2_tg_s42_v7_attention_steering.json',
 'model_name': 'Qwen/Qwen2.5-7B-Instruct',
 'pid': '157657',
 'seed': 42,
 'server': 'westd-20861',
 'submitted_at': '2026-05-20T07:07:27.678Z',
 'submitted_via': 'submit_training_job',
 'wall_clock_seconds': 8551.2}
  HYPOTHESIS: 推理时向 attention logits 注入 goal-position bias β 可恢复 autoregressive GAR。如果 GAR 从 0.015 显著提升 → 闭合因果环：exposure bias → attention 偏移 → GAR 坍塌 → 手动修正注意力 → GAR 恢复。扫描 β ∈ {0, 0.5, 1.0, 2.0, 5.0, 10.0}，成功标准：GAR > 0.1 且 PPL 不严重恶化。

EXP_ID: p1_tf_ar_kl_divergence
{'checkpoint_path': 'results/p1_kl_perhead/',
 'command': 'python scripts/p1_kl_divergence.py',
 'data_count': 30,
 'data_path': '/root/turn_residual_gating/data/eval_200.json',
 'log_path': 'logs/p1_kl_divergence_step2.log',
 'model_name': 'Qwen/Qwen2.5-7B-Instruct',
 'seed': 42,
 'server': 'westd-20861'}
  HYPOTHESIS: TF and AR attention distributions diverge more on GAR-relevant heads (high gate values) than non-relevant heads, providing mechanistic evidence that exposure bias selectively disrupts goal-attending computation rather than uniformly degrading attention.

EXP_ID: mmlu_eval_all
{'checkpoint_path': 'results/mmlu/',
 'checkpoint_source': 'base/lo/ug/tg/pcgrad/ss checkpoints',
 'command': 'python eval_mmlu.py --model_path &lt;checkpoint> --n_shot 5',
 'data_count': 14042,
 'data_path': 'MMLU benchmark (5-shot)',
 'eval_data': 'MMLU 5-shot',
 'log_path': 'logs/gpu_chain_next.log',
 'model_name': 'Qwen/Qwen2.5-7B-Instruct',
 'seed': 42,
 'server': 'westd-20861'}
  HYPOTHESIS: ThreadGate's per-layer gating and auxiliary GAR loss do not degrade the model's general language understanding capabilities. All fine-tuned variants (TG/UG/LO/PCGrad/SS) should maintain MMLU 5-shot accuracy within 1pp of the Base LoRA-only checkpoint, confirming that attention steering is additive rather than destructive.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2193062c-b3ad-408c-bbad-dd83ced9f5c2",
  "isSidechain": true,
  "promptId": "7f6d57ff-336a-4102-9549-9590b20d9c0f",
  "agentId": "a10e81c6866b67bf0",
  "type": "user",
  "uuid": "bcb53dd0-62b7-4bdc-b8f1-4c0cca5499e1",
  "sourceToolAssistantUUID": "2193062c-b3ad-408c-bbad-dd83ced9f5c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet"
}
```

</details>

---

### Assistant

_source line 34 · 2026-05-25T08:35:08.964Z_

Now I have all the data needed for a comprehensive structured summary. Let me compile it:

---

## Comprehensive Quantitative Results Extracted from Registry

### TOTAL EXPERIMENTS: 58 (DONE: ~42, RUNNING/PREPARING: ~6, QUEUED: 1, FAILED/KILLED: ~9)

---

## 1. BASELINE DIAGNOSTICS (Qwen2.5-7B-Instruct, Phase 1)

### exp: `phase1_gar_diag` (Qwen base, gen mode, N=5 conv, 10 turns)
- turn_1_avg_gar: 0.0418
- mid_turns_avg_gar: **0.0122** (baseline reference used throughout paper)
- relative_drop: 0.708 (70.8% drop from turn 1 to mid)
- per_turn_avg_gar: [0.0418, 0.0241, 0.0224, 0.0130, 0.0133, 0.0086, 0.0078, 0.0080, 0.0157, 0.0064]

### exp: `llama_phase1_gar_diag` (Llama-3.1-8B-Instruct, gen mode, N=5, 10 turns)
- per_turn_gar: {t1: 0.0263, t2: 0.0183, t3: 0.0087, t4: 0.0055, t5: 0.0060, t6: 0.0035, t7: 0.0038, t8: 0.0037, t9: 0.0050, t10: 0.0026}
- t1→t10 decay: **90.1%**
- t1→mid(3-8) drop: **80.2%**

---

## 2. MAIN QWEN TRAINING VARIANTS (s42, 3 epochs, 8k UltraChat, LR=2e-4, batch=1, grad_accum=8)

### 2a. ThreadGate v7 (TG) — `phase2_tg_s42_v7` + `phase2_4way_eval_heldout`

**Training config**: seed=42, Qwen2.5-7B-Instruct, 8k data, 3 epochs, LR=2e-4, batch=1, grad_accum=8, gate-type=threadgate, gar-target=0.5, lambda-gar=1.0, lambda-gate-div=1.0, init-bias=1.5, gate-lr-multiplier=10

**TF (IID heldout eval, N=50):**
- GAR-ours mid: **0.5035**
- GAR-Dongre mid: **0.0152**
- PPL: **2.78**
- NTP: 0.9771
- recovery_pp (GAR-ours): 49.13%

**AR (model-gen, N=39 from d048_final_ar_eval):**
- GAR-ours mid: **0.0157** (v7 eval) / 0.064 (beta=0, attention_steering_gen_n50)
- GAR-Dongre mid: 0.0194
- PPL: 1.36–1.432

**TF-AR Gap ratio (v7)**: **32.1x** (phase2_4way_eval_heldout: TF 0.5035, AR ~0.0157)

**Gate stats (final):**
- mean: 0.9336, std: 0.0492 (v7_s42)
- Layer profile (s42): L0–L27, min at L1=0.793, max at L27=1.0
- full profile in v7_tg_s123: L0=0.883, L1=0.793, L2=0.996, ..., L27=1.0

---

### 2b. Uniform Gate (UG) — `phase2_ug_s42`

**Training**: same as TG but gate-type=uniform

**TF (heldout):**
- GAR-ours mid: **0.5053**
- GAR-Dongre mid: **0.0124**
- PPL: **2.78**, NTP: 0.9752
- recovery_pp: 49.31%

**AR (model-gen):**
- GAR-ours mid: **0.0149**
- GAR-Dongre mid: **0.0185**
- PPL: **1.396**

**Gate stats (final):**
- mean: 0.9598, std: 0.0518, min: 0.7773, max: 1.0

**Epoch-level losses:**
- Epoch 0: avg_loss=1.0019, avg_ntp=0.9755, avg_gar=0.0259
- Epoch 1: avg_loss=0.9447, avg_ntp=0.9435, avg_gar=0.0013
- Epoch 2: avg_loss=0.9319, avg_ntp=0.9309, avg_gar=0.0010

---

### 2c. LoRA-only (LO) — `phase2_lora_only_s42`

**Training**: gate-type=lora_only, lambda-gate-div=0.0

**Training metrics:**
- epochs_completed: 3 (3000 steps)
- training_time: 20588.6s (5.7h)
- final_lora_size_mb: 20

**TF eval:**
- GAR-ours mid: **0.4978** (heldout)
- GAR-Dongre mid: **0.0132**
- PPL: **2.78**, NTP: 0.9771
- recovery_pp: 48.56%

**AR (model-gen):**
- GAR-ours mid: **0.0245**
- GAR-Dongre mid: **0.0185**
- PPL: **1.371**

---

### 2d. PCGrad v9 — `phase2_tg_s42_v9_pcgrad`

**Training**: Qwen2.5-7B-Instruct, gate-type=threadgate, gar-target=0.5, lambda-gar=1.0, lambda-gate-div=1.0, init-bias=1.5, gate-lr-multiplier=10, lr=2e-4, epochs=3, batch-size=1, grad-accum=8, seed=42, 8.5 GPU-h

**TF (IID heldout):**
- GAR-ours mid: **0.5002**
- GAR-Dongre mid: **0.0123**
- PPL: **2.78**, NTP: 0.9752
- vs v7 IID: GAR diff=-0.0033, PPL diff=0.004

**AR (model-gen):**
- GAR-ours mid: **0.0151**
- GAR-Dongre mid: **0.0173**
- PPL: **1.5**

**Note**: PCGrad converges identically to TG v7 on TF; AR gap remains. Confirms gradient conflict is NOT the root cause.

---

### 2e. Scheduled Sampling v8b (SS) — `phase2_tg_s42_v8b_resume`

**Training**: Qwen2.5-7B-Instruct, SS max_ratio=0.5 (linear ramp 0→0.5), lr=2e-4, epochs=3, batch=1, grad-accum=8, seed=42, 8.1h

**Training metrics:**
- final_loss: 0.933, final_ntp_loss: 0.9322, final_gar_loss: 0.0008
- final_gate_mean: 0.9586, final_gate_std: 0.0582
- ss_ratio: 0.5

**TF (IID eval):**
- GAR-ours: **0.4983**
- GAR-Dongre: **0.3855**
- PPL: **2.78**

**AR (model-gen):**
- GAR-ours: **0.3177**
- GAR-Dongre: **0.3533**
- PPL: **1.38**

**TF-AR Gap ratio (v8b SS)**: **1.57x** (vs v7 TG: 32x) — major gap reduction

**vs v7 deltas**: iid_gar_ours_delta=-0.005, modelgen_gar_ours_delta=+0.302

---

### 2f. Base Model (no fine-tuning reference)

**From `phase2_4way_eval_heldout`:**
- TF GAR-ours mid: **0.0128** (heldout) / 0.0107 (IID)
- TF GAR-Dongre mid: **0.0031**
- TF PPL: **4.34**, NTP: 1.4045
- AR (from d048_final_ar_eval): GAR-ours=**0.019**, PPL=1.447

---

## 3. MULTI-SEED RESULTS (Qwen, s123)

### TG s123 — `v7_tg_s123` + `eval_v7_tg_s123`

**Training:** seed=123, Qwen2.5-7B-Instruct, 8k data, 2 epochs (21425.2s)
- Epoch 1: avg_loss=0.9447, avg_ntp=0.9434, avg_gar=0.0013
- Epoch 2: avg_loss=0.9315, avg_ntp=0.9305, avg_gar=0.0010
- final_gate: mean=0.9467, std=0.051, min=0.793, max=1.0

**TF eval (IID):**
- GAR-ours mid: **0.5052**
- GAR-Dongre mid: **0.0119**
- PPL: **2.7802**, NTP: 0.9752

**AR (model-gen):**
- GAR-ours mid: **0.0165**
- GAR-Dongre mid: **0.0177**
- PPL: **1.3855**, NTP: 0.3223

**TF-AR gap ratio**: **30.6x** (vs s42: 32.1x, delta=-1.4)
**vs s42 deltas:** TF GAR-ours delta=+0.0017, AR GAR-ours delta=+0.0008

---

### SS v8b s123 — `v8b_ss_s123` + `eval_v8b_ss_s123`

**Training:** seed=123, 3 epochs (38773.4s), ss_used_ratio=0.371
- epoch0_loss=1.0092, epoch1_loss=0.9444, epoch2_loss=0.9316
- final_gate: mean=0.9505, std=0.0508, min=0.7383, max=1.0

**TF (IID):**
- GAR-ours: **0.503**
- GAR-Dongre: **0.394**
- PPL: **2.781**, NTP: 0.976

**AR (model-gen, N=5):**
- GAR-ours: **0.418**
- GAR-Dongre: **0.441**
- PPL: **1.389**, NTP: 0.325

**TF-AR gap ratio**: **1.2x**

---

## 4. UNIFIED AR EVALUATION (`d048_final_ar_eval`, N=39, Qwen s42)

*All four Qwen conditions evaluated together (AR model-gen):*

**β=0 (pure AR, no steering):**
- base_gar: 0.019
- tg_gar: 0.064
- ug_gar: 0.033
- lo_gar: 0.037
- pcgrad_gar: 0.030
- ss_gar: **0.347**

**β=3:**
- base_gar: 0.531, tg_gar: 0.556, ss_gar: 0.593

**β=5:**
- base_gar: 0.704, tg_gar: 0.727, ss_gar: 0.717

**PPL:**
- base: 1.447, tg: 1.432, ss: 1.442

**Statistical tests (Wilcoxon):**
- TG vs base, β=0: p<0.001, r=0.802
- SS vs TG, β=0: p<0.001, r=0.869

---

## 5. OLDER SS MULTI-SEED EVAL (d048 series, 2000-sample training data)

### `d048_eval_ss_s42` (seed=42)
- TF GAR-ours mid: 0.5025 (tg), 0.0128 (base)
- TF GAR-Dongre mid: 0.3890 (tg), 0.0031 (base)
- TF PPL: 2.78 (tg), 4.34 (base)
- AR GAR-ours mid: 0.3887, CI95=[0.3692, 0.3934]
- AR PPL: 1.35
- gap_ratio: 1.29
- N_conv_tf: 50, N_conv_ar: 5 (NOTE: only N=5, flagged for re-eval)

### `d048_eval_ss_s123` (seed=123)
- TF GAR-ours: 0.5536, TF GAR-Dongre: 0.4106, TF PPL: 2.6123
- AR β=0: GAR=0.4231, PPL=1.4408
- AR β=3: GAR=0.5903, PPL=1.6070
- AR β=5: GAR=0.7174, PPL=1.7852
- N_conv_tf: 200, N_conv_ar: 39

### `d048_eval_ss_s456` (seed=456)
- TF GAR-ours mid: 0.4964, TF GAR-Dongre mid: 0.3862
- AR β=0: GAR=0.4325, PPL=1.4394
- AR β=3: GAR=0.6050, PPL=1.5868
- AR β=5: GAR=0.7157, PPL=1.8045
- N_conv_ar: 50

---

## 6. LLAMA-3.1-8B-Instruct RESULTS

### 6a. TG s42 training — `llama_tg_s42`
**Training**: 3 epochs, 3000 steps, 7.28h, seed=42
- final_avg_loss: 0.9233, final_avg_ntp: 0.9224, final_avg_gar: 0.0009
- final_gate: mean=0.9099, std=0.0701, min=0.7188, max=0.9922
- Gate profile step 3000: L0=0.957, ..., L25=0.719 (min), L27=0.805, ..., L32=0.934
- Checkpoint: gate=4.2MB, lora=26MB, GPU=RTX PRO 6000 Blackwell (102GB VRAM, 63.4GB used)

### 6b. LoRA-only s42 training — `llama_lora_only_s42`
- epochs: 3, wall_clock: 25317s (7.03h)
- final_avg_loss: 0.9288, final_avg_ntp: 0.9279, final_avg_gar: 0.0009

### 6c. Llama TF eval (TF, N=50, 4 turns) — `llama_eval_s42`
- **Base TF:** GAR-ours=0.0166, nGAR=0.3882, GAR-Dongre=0.0038, nGAR-Dongre=0.163, PPL=3.45
- **TG TF:** GAR-ours=**0.4836**, nGAR=11.8818, GAR-Dongre=0.0180, nGAR-Dongre=0.7922, PPL=2.57
- **AR Base (N=5, 10 turns):** GAR-ours=0.0086, nGAR=0.0798, GAR-Dongre=0.0118, nGAR-Dongre=0.1265, PPL=1.24
- **AR TG (N=5):** GAR-ours=0.0304, nGAR=0.2632, GAR-Dongre=0.0217, nGAR-Dongre=0.2459, PPL=1.32
- TF-AR gap_ratio (TG, ours): **15.9x**
- TF-AR gap_ratio (base, ours): 1.93x
- TF-AR gap_ratio (TG, Dongre): **0.83x** (no gap)
- vs Qwen v7 gap_ratio: **32.1x** (Qwen) vs 15.9x (Llama)

### 6d. Llama AR matched eval N=20 — `llama_ar_matched_eval` + `eval_llama_ar_n20`

**AR matched eval (N=20 conversations, 4 turns mid definition: turns 3-T):**
- **Base AR:** mid_gar=0.0082, nGAR=0.1, PPL=1.267 (Dongre: mid_gar=0.0051)
- **TG AR:** mid_gar=0.0388, nGAR=0.493, PPL=1.413 (Dongre: mid_gar=0.0180)
- TG-over-base AR (ours): **4.71x**; TG-over-base AR (Dongre): 3.54x
- TF-AR gap analysis: GAR-ours raw gap=12.5x (TF 0.484 / AR 0.039); nGAR gap=24.1x; GAR-Dongre zero gap=1.002x

**N=20 AR eval details (eval_llama_ar_n20):**
- Base: mean=0.0088, std=0.0056, median_per_conv=0.0093, median_per_turn_pool=0.0071
- TG: mean=0.0434, std=0.1002, median_per_conv=0.0179, median_per_turn_pool=0.0126, spike_ratio=5% (2/40 turns ≥0.4)
- LO: mean=0.0284, std=0.0481, median_per_conv=0.0184, median_per_turn_pool=0.0133, spike_ratio=0%
- **Paper §5.5 cites**: median_per_conv (TG=0.0179, LO=0.0184, Base=0.0093) → TG ≈ LO

### 6e. Llama LoRA-only TF/AR eval — `eval_llama_lora_only_s42`
- TF: GAR-ours=0.4807, GAR-Dongre=0.0188, nGAR-ours=11.8031, PPL=2.6, N=50
- AR: GAR-ours=0.0617, GAR-Dongre=0.0226, nGAR-ours=0.6065, PPL=1.32, N=5
- TF-AR gap_ratio (ours): **7.79x**

### 6f. Llama Scheduled Sampling eval — `p1_llama_ss_eval`
- SS TF: GAR=0.477, PPL=2.82
- SS AR β=0: GAR=0.1662, PPL=1.37
- SS AR β=5: GAR=0.7905, PPL=1.81
- Base AR: GAR=0.0179, PPL=1.22
- TF-AR gap (raw): **2.87** (PPL-based)

---

## 7. ATTENTION STEERING RESULTS

### 7a. Gen mode N=50 — `attention_steering_gen_n50` (Qwen v7 TG, AR gen mode)
*(n_valid=39 after filtering ≥3 turns, N=50 total)*
| β | mid_GAR (mean) | mid_GAR_std | PPL | n_valid |
|---|---|---|---|---|
| 0.0 | **0.0641** | 0.0809 | 1.4324 | 39 |
| 2.0 | **0.1280** | 0.1101 | 1.4822 | 39 |
| 3.0 | **0.5558** | 0.0601 | 1.5605 | 39 |
| 4.0 | **0.6439** | 0.0607 | 1.6674 | 39 |
| 5.0 | **0.7271** | 0.0605 | 1.7723 | 38 |
| 10.0 | **0.9612** | 0.0152 | 3.4517 | 39 |
- Phase transition range: β ∈ [2, 3]

### 7b. TF mode N=200 — `attention_steering_eval200_tf`
| β | mid_GAR | PPL |
|---|---|---|
| 0.0 | 0.5353 | 2.62 |
| 2.0 | 0.6112 | 2.69 |
| 3.0 | 0.7880 | 2.93 |
| 4.0 | 0.8165 | 3.49 |
| 5.0 | 0.8325 | 6.15 |
| 10.0 | 0.9770 | 505.21 |

### 7c. Gen mode N=5 (preliminary) — `attention_steering_v7_tg_gen`
| β | avg_GAR | avg_PPL |
|---|---|---|
| 0.0 | 0.0280 | 1.409 |
| 0.5 | 0.0287 | 1.387 |
| 1.0 | 0.0349 | 1.360 |
| 2.0 | 0.0620 | 1.411 |
| 5.0 | 0.6795 | 1.908 |
| 10.0 | 0.9590 | 4.220 |
- Phase transition range: β ∈ [2, 5]; baseline_gar=0.028; max_acceptable_ppl β=5

---

## 8. GRADIENT ANALYSIS

### 8a. Qwen v7 across epochs — `analysis_gradient_conflict`
| Epoch | cos_sim | neg_layers_pct | mag_ratio |
|---|---|---|---|
| 0 | **-0.089** | **78.6%** | 7.5 |
| 1 | **-0.054** | **71.4%** | 13.7 |
| 2 | **-0.042** | **67.9%** | 14.7 |

### 8b. Llama gradient conflict — `p2_llama_gradient_conflict`
- cos_sim_mean: **0.0045**, cos_sim_std: 0.07
- neg_cos_sim_layers_pct: **53.1%**
- mag_ratio_median: **25.7**
- **CRITICAL NOTE**: cos_sim≈0 indicates near-orthogonal (NOT conflict). Script conclusion text "widespread conflict" is misleading — actual finding: NTP and GAR gradients are nearly orthogonal on Llama, consistent with Qwen pattern.

---

## 9. KL DIVERGENCE / EXPOSURE BIAS ANALYSIS

### `p1_tf_ar_kl_divergence`
- TG delta_gar: 0.0165 (TF→AR drop)
- Base delta_gar: 0.0122 (TF→AR drop)
- TG mean_kl: **0.054** (attention distribution TF-AR divergence)
- Base mean_kl: **0.043**
- gate_kl_correlation: 0.11
- high_kl_layers: **L23-L27, L9**
- GAR robustness ratios:
  - ours_tg_base_ratio: **21.4**
  - goal_only_ratio: **63**
  - ours_all_ratio: **1.7**
  - ours_first_ratio: **1.8**

---

## 10. TOPIC RETENTION CONSISTENCY (TRC)

### `trc_baseline_v7_tg` (5 conversations, 10 turns)
| Variant | TF TRC | Gen TRC | TRC gap | TF TBP-PPL | Gen TBP-PPL |
|---|---|---|---|---|---|
| v7 TG | **0.3339** | **0.3323** | 0.0016 | 1.05 | 1.05 |
| LoRA-only | 0.349 | 0.4106 | -0.0617 | 9.5 | 12 |
| Base | 0.1494 | 0.1494 | 0 | 2.05 | 2.05 |

---

## 11. INSTRUCTION RETENTION TEST

### `instruction_retention_test` (Qwen v7 TG, β=0 vs β=3)
- late_turn_rate_β=0: **0.759**
- late_turn_rate_β=3: **0.870**
- delta: +0.111
- McNemar χ²=3.125, p=0.0771 (marginal)
- GAR-compliance correlation: r=**0.2003**, p=**0.007**
- Category breakdown:
  - content_constraint: β=0: 0.619, β=3: 0.857, Δ=+0.238
  - count_constraint: β=0: 1.0, β=3: 1.0, Δ=0
  - format_constraint: β=0: 1.0, β=3: 1.0, Δ=0
  - position_constraint: β=0: 0.667, β=3: 0.733, Δ=+0.067

---

## 12. MMLU (General Capability)

### `mmlu_eval_all` (5-shot, 14042 samples, Qwen variants)
| Variant | MMLU |
|---|---|
| Base Qwen | **0.7423** |
| PCGrad v9 s42 | 0.7386 |
| SS v8b s42 | 0.7375 |
| LoRA-only s42 | 0.7357 |
| TG v7 s42 | **0.7347** |
| UG s42 | 0.7346 |

Drop from base: TG=-0.0076 (0.76pp), UG=-0.0077 (0.77pp), LO=-0.0066 (0.66pp), PCGrad=-0.0037, SS=-0.0048

---

## 13. ATTENTION HEATMAP ANALYSIS

### `analysis_attention_heatmap` (Qwen s42 checkpoints)
| Variant | mean_goal_attn | decay |
|---|---|---|
| Base | 0.0136 | 0.875 |
| TG | **0.0232** | 0.777 |
| UG | 0.0216 | 0.803 |
| LoRA-only | 0.0216 | 0.810 |
- gating_incremental_benefit: none (TG = UG = LO in attention heatmap)

---

## 14. SS TRAINING INTERNALS (d048 series — 2k data, older experiments)

### `d048_ss_s42` training
- final_avg_loss: 0.9326, final_ntp: 0.9320, final_gar: 0.0007
- gate: mean=0.9527, std=0.0589, min=0.7383 (L4), max=1.0
- ss_usage: 4750/16000 (29.7%), ss_fallback: 0
- epochs: 3, wall_clock: 23418s (6.5h)

---

## KEY SUMMARY NUMBERS FOR PAPER AUDIT

**Main Qwen results (heldout TF eval, N=50, mid-turns):**
| Variant (seed=42) | TF GAR-ours | TF GAR-Dongre | PPL | AR GAR-ours (β=0) |
|---|---|---|---|---|
| Base | 0.0128 | 0.0031 | 4.34 | 0.019 |
| TG v7 | **0.5035** | 0.0152 | 2.78 | 0.064 |
| UG | 0.5053 | 0.0124 | 2.78 | 0.0149 |
| LoRA-only | 0.4978 | 0.0132 | 2.78 | 0.0245 |
| PCGrad v9 | 0.5002 | 0.0123 | 2.78 | 0.0151 |
| SS v8b | **0.4983** | **0.3855** | 2.78 | **0.3177** |

**TF-AR Gap Ratios:**
- TG v7 s42: **32.1x** (TF 0.5035 / AR 0.0157)
- TG v7 s123: **30.6x**
- SS v8b s42: **1.57x**
- SS v8b s123: **1.2x**
- Llama TG: **15.9x**
- Llama LoRA-only: **7.79x**

**Statistical significance (d048_final_ar_eval, Wilcoxon on N=39 AR convs):**
- TG vs base β=0: p<0.001, r=0.802
- SS vs TG β=0: p<0.001, r=0.869

**MMLU retention**: All variants within 0.77pp of base (0.7423)

**Gradient conflict (Qwen epoch 2)**: cos_sim=-0.042, 67.9% layers negative, mag_ratio=14.7

**Llama cross-model AR (N=20, median_per_conv)**: TG=0.0179, LO=0.0184, Base=0.0093 → TG ≈ LO (zero-increment)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bcb53dd0-62b7-4bdc-b8f1-4c0cca5499e1",
  "isSidechain": true,
  "agentId": "a10e81c6866b67bf0",
  "requestId": "req_011CbNyemkRq8CzsyxxJPwTK",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3eb88c04-c9b9-49e2-8162-cb7cf51f0996",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/.claude/sessions/paper_agent_d1ae4a98",
  "sessionId": "0b0cdf03-4218-4267-be3a-fa2b7e05fc58",
  "version": "2.1.126",
  "gitBranch": "master",
  "slug": "tidy-zooming-goblet",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_014r82ciJy9ds5rvxCcY8HNR",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3246,
      "cache_read_input_tokens": 58720,
      "output_tokens": 7983,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3246
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7983,
          "cache_read_input_tokens": 58720,
          "cache_creation_input_tokens": 3246,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3246,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---
