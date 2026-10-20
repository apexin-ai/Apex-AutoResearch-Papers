# Research conversation: Parse the large registry JSON file at `/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 28
- **Recorded user turns:** 1
- **Tool calls:** 9
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-aee0c4a84f025f3bb.jsonl`
- **Structured JSON:** [`ca46b70c9a99d9d5fc0a.json`](../../sessions/ca/ca46b70c9a99d9d5fc0a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

28 recorded events

### User

_source line 1 · 2026-05-15T18:25:56.769Z_

Parse the large registry JSON file at `/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/0e7bc130-13e2-45e1-ae79-20741112a4af/tool-results/mcp-agent-ml-research-read_registry-1778869532955.txt` to extract eval experiment info.

The file is JSON with schema: {result: string} where result is itself a JSON string.

Steps:
1. Use `jq` to probe the structure
2. Extract all experiments that have:
   - type containing "eval" or task containing "eval"
   - status = "DONE"
3. For each eval experiment, extract: exp_id, name/description, metrics (if any), any fields about scale/dose/seed/benchmark

Return a structured summary of ALL eval experiments found, their metrics (if present), and any identifying info (scale, dose, seed, eval_type like aligned/para_aligned). Be thorough - I need every single eval experiment.

The project is contamcal-irt-calibration, studying LLM benchmark contamination calibration. Scales: 0.5B, 1.5B, 3B. Doses: 0%, 5%, 25%, 100%. Seeds: 42, 123. Benchmarks: MMLU, GSM8K, ARC-Challenge, HumanEval.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "eec554ab-49eb-41f0-9151-4530891c32ce",
  "agentId": "aee0c4a84f025f3bb",
  "type": "user",
  "uuid": "29edd3bd-22bb-4e61-90d6-d37ff7a98c2b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-15T18:25:56.794Z_

```json
{
  "parentUuid": "29edd3bd-22bb-4e61-90d6-d37ff7a98c2b",
  "isSidechain": true,
  "agentId": "aee0c4a84f025f3bb",
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
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__detect_image",
      "mcp__agent-ml-research__kill_job",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__ssh_execute",
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__update_registry"
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
      "mcp__agent-ml-research__append_idea",
      "mcp__agent-ml-research__detect_image",
      "mcp__agent-ml-research__kill_job",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__ssh_execute",
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__update_registry"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "f500b0c2-cc6d-4919-aa5d-40076fbffa49",
  "timestamp": "2026-05-15T18:25:56.794Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-15T18:26:00.855Z_



I'll start by probing the structure of this large JSON file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f500b0c2-cc6d-4919-aa5d-40076fbffa49",
  "isSidechain": true,
  "agentId": "aee0c4a84f025f3bb",
  "requestId": "req_011Cb4pnJb9c3f3P8sbVPouz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e1abb0f9-f388-447c-8d48-f4dc081b4971",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011BK2KCfSqhE2te1g9pcVEC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14507,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14507,
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

_source line 4 · 2026-05-15T18:26:01.835Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01MwWq5U7WZcduzFZhWmr1bD`</summary>

```json
{
  "command": "wc -c /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/0e7bc130-13e2-45e1-ae79-20741112a4af/tool-results/mcp-agent-ml-research-read_registry-1778869532955.txt",
  "description": "Check file size"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e1abb0f9-f388-447c-8d48-f4dc081b4971",
  "isSidechain": true,
  "agentId": "aee0c4a84f025f3bb",
  "requestId": "req_011Cb4pnJb9c3f3P8sbVPouz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6016bb7d-057c-4f60-80bc-5318b29d0a8e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011BK2KCfSqhE2te1g9pcVEC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14507,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14507,
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

_source line 5 · 2026-05-15T18:26:02.943Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Eb6j1XUR7F3TU6EcdZbDi6`</summary>

```json
{
  "command": "head -c 2000 /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/0e7bc130-13e2-45e1-ae79-20741112a4af/tool-results/mcp-agent-ml-research-read_registry-1778869532955.txt",
  "description": "Peek at file start"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6016bb7d-057c-4f60-80bc-5318b29d0a8e",
  "isSidechain": true,
  "agentId": "aee0c4a84f025f3bb",
  "requestId": "req_011Cb4pnJb9c3f3P8sbVPouz",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "da190303-2d0d-48eb-8ce8-87e265037495",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011BK2KCfSqhE2te1g9pcVEC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14507,
      "cache_read_input_tokens": 0,
      "output_tokens": 336,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 14507
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 336,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 14507,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 14507,
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

_source line 6 · 2026-05-15T18:26:03.264Z_

<details><summary>↩ Tool result · `toolu_01MwWq5U7WZcduzFZhWmr1bD`</summary>

```text
236095 /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/0e7bc130-13e2-45e1-ae79-20741112a4af/tool-results/mcp-agent-ml-research-read_registry-1778869532955.txt
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6016bb7d-057c-4f60-80bc-5318b29d0a8e",
  "isSidechain": true,
  "promptId": "eec554ab-49eb-41f0-9151-4530891c32ce",
  "agentId": "aee0c4a84f025f3bb",
  "type": "user",
  "uuid": "14f060ea-9786-4109-94db-0f130ab63212",
  "sourceToolAssistantUUID": "6016bb7d-057c-4f60-80bc-5318b29d0a8e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-15T18:26:03.472Z_

<details><summary>↩ Tool result · `toolu_01Eb6j1XUR7F3TU6EcdZbDi6`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"exp_001_eval_3B_d025_s123_aligned\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T14:51:16.431Z\", \"updated_at\": \"2026-05-15T18:10:03.567Z\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:3\", \"reproduce\": {\"server\": \"cqa1-21977\", \"gpu\": \"cuda:3\", \"started_at\": \"2026-05-15T14:51:29.435Z\", \"command\": \"bash -c \\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=3 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"code_commit\": \"dd81ae283e12a247f768b6ae72e67b085a874bd1\", \"finished_at\": \"2026-05-15T18:07:00.568Z\", \"training_hours\": 3.26}, \"spec\": {\"command\": \"bash -c \\\"source /etc/network_turbo && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=3 /root/miniconda3/bin/python /root/contamcal-irt-calibration/exp001/evaluate.py --model-path /root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_s123/lora_adapter --output-dir /root/autodl-tmp/exp001/eval_results/Qwen2.5-3B_d025_s123_aligned --benchmarks mmlu gsm8k arc_challenge humaneval --mc-format aligned --cache-dir /root/autodl-tmp/.hf_cache\\\"\", \"server\": \"cqa1-21977\", \"gpu\": \"cuda:3\", \"pid\": 576730, \"data_path\": \"/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_s123/lora_adapter\", \"data_count\": 4, \"model_name\": \"Qwen2.5-3B\", \"seed\": 123, \"checkpoint_source\": \"exp_001_sft_3B_d025_s123\", \"eval_data\": \"mmlu,gsm8k,arc_challenge,humaneval\"
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "da190303-2d0d-48eb-8ce8-87e265037495",
  "isSidechain": true,
  "promptId": "eec554ab-49eb-41f0-9151-4530891c32ce",
  "agentId": "aee0c4a84f025f3bb",
  "type": "user",
  "uuid": "2856882d-274e-43bc-9cb0-7e1e173e3746",
  "sourceToolAssistantUUID": "da190303-2d0d-48eb-8ce8-87e265037495",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 8 · 2026-05-15T18:26:07.253Z_

Good, I can see the structure. Let me parse the inner JSON and extract all eval experiments.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2856882d-274e-43bc-9cb0-7e1e173e3746",
  "isSidechain": true,
  "agentId": "aee0c4a84f025f3bb",
  "requestId": "req_011Cb4pnoceS7c94urgsyujm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cce7f452-2352-4811-9760-92c8884eca3e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JfArX89zH3FV3U9Kwds2aL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2192,
      "cache_read_input_tokens": 14507,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2192,
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

_source line 9 · 2026-05-15T18:26:09.218Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01R455ACcqwWqvM5fGjCznWL`</summary>

```json
{
  "command": "FILE=\"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/0e7bc130-13e2-45e1-ae79-20741112a4af/tool-results/mcp-agent-ml-research-read_registry-1778869532955.txt\"\ncat \"$FILE\" | jq -r '.result' | jq '.data.experiments | keys[]' | grep -i eval | wc -l",
  "description": "Count eval experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cce7f452-2352-4811-9760-92c8884eca3e",
  "isSidechain": true,
  "agentId": "aee0c4a84f025f3bb",
  "requestId": "req_011Cb4pnoceS7c94urgsyujm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4b664826-27e8-4f9d-bd44-2506dadb1824",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JfArX89zH3FV3U9Kwds2aL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2192,
      "cache_read_input_tokens": 14507,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2192,
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

### Tool result

_source line 10 · 2026-05-15T18:26:09.904Z_

<details><summary>↩ Tool result · `toolu_01R455ACcqwWqvM5fGjCznWL`</summary>

```text
69
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4b664826-27e8-4f9d-bd44-2506dadb1824",
  "isSidechain": true,
  "promptId": "eec554ab-49eb-41f0-9151-4530891c32ce",
  "agentId": "aee0c4a84f025f3bb",
  "type": "user",
  "uuid": "1d4351c5-6419-4594-a121-76f7a537cfef",
  "sourceToolAssistantUUID": "4b664826-27e8-4f9d-bd44-2506dadb1824",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-15T18:26:10.279Z_

<details open><summary>🔧 Tool call — Bash · `toolu_015wEXWHc3q2xUBF6yCvaBte`</summary>

```json
{
  "command": "FILE=\"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/0e7bc130-13e2-45e1-ae79-20741112a4af/tool-results/mcp-agent-ml-research-read_registry-1778869532955.txt\"\ncat \"$FILE\" | jq -r '.result' | jq '.data.experiments | keys[]' | grep -i eval",
  "description": "List all eval experiment keys"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1d4351c5-6419-4594-a121-76f7a537cfef",
  "isSidechain": true,
  "agentId": "aee0c4a84f025f3bb",
  "requestId": "req_011Cb4pnoceS7c94urgsyujm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "62a54fcc-ed2f-45ec-a84b-7ceb98ac8c3e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JfArX89zH3FV3U9Kwds2aL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2192,
      "cache_read_input_tokens": 14507,
      "output_tokens": 397,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2192
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 397,
          "cache_read_input_tokens": 14507,
          "cache_creation_input_tokens": 2192,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2192,
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

_source line 12 · 2026-05-15T18:26:10.767Z_

<details><summary>↩ Tool result · `toolu_015wEXWHc3q2xUBF6yCvaBte`</summary>

```text
"exp_001_eval_05B_aligned_batch"
"exp_001_eval_05B_d000_s123"
"exp_001_eval_05B_d000_s123_aligned"
"exp_001_eval_05B_d000_s42"
"exp_001_eval_05B_d000_s42_v5"
"exp_001_eval_05B_d000_s42_v7"
"exp_001_eval_05B_d005"
"exp_001_eval_05B_d005_aligned"
"exp_001_eval_05B_d005_para_aligned"
"exp_001_eval_05B_d005_s123_aligned"
"exp_001_eval_05B_d005_s123_para_aligned"
"exp_001_eval_05B_d025_aligned"
"exp_001_eval_05B_d025_aligned_v2"
"exp_001_eval_05B_d025_s123_aligned"
"exp_001_eval_05B_d100"
"exp_001_eval_05B_d100_aligned"
"exp_001_eval_05B_d100_aligned_v3"
"exp_001_eval_05B_d100_aligned_v4"
"exp_001_eval_05B_d100_s123_aligned"
"exp_001_eval_05B_d100_v2"
"exp_001_eval_05B_d100_v5"
"exp_001_eval_05B_raw"
"exp_001_eval_15B_aligned_batch"
"exp_001_eval_15B_d000_s123"
"exp_001_eval_15B_d000_s123_aligned"
"exp_001_eval_15B_d000_s42"
"exp_001_eval_15B_d000_s42_v2"
"exp_001_eval_15B_d005_aligned_v2"
"exp_001_eval_15B_d005_s123"
"exp_001_eval_15B_d005_s123_v2"
"exp_001_eval_15B_d025_aligned"
"exp_001_eval_15B_d025_para_aligned"
"exp_001_eval_15B_d025_s123"
"exp_001_eval_15B_d025_s123_v2"
"exp_001_eval_15B_d100_aligned"
"exp_001_eval_15B_d100_s123_aligned"
"exp_001_eval_15B_d100_s42"
"exp_001_eval_3B_d000_aligned"
"exp_001_eval_3B_d000_s123"
"exp_001_eval_3B_d000_s123_aligned"
"exp_001_eval_3B_d000_s42"
"exp_001_eval_3B_d000_s42_para_aligned"
"exp_001_eval_3B_d000_s42_v3"
"exp_001_eval_3B_d000_v2_aligned"
"exp_001_eval_3B_d000_v2_para_aligned"
"exp_001_eval_3B_d000_v2_para_aligned_v2"
"exp_001_eval_3B_d000_v2_para_aligned_v3"
"exp_001_eval_3B_d000_v2_s123_aligned"
"exp_001_eval_3B_d000_v2_s123_para_aligned"
"exp_001_eval_3B_d005_aligned"
"exp_001_eval_3B_d005_s123_para_aligned"
"exp_001_eval_3B_d005_s42_aligned"
"exp_001_eval_3B_d025_s123_aligned"
"exp_001_eval_3B_d025_s123_para_aligned"
"exp_001_eval_3B_d025_v2_aligned"
"exp_001_eval_3B_d025_v2_para_aligned"
"exp_001_eval_3B_d100_aligned"
"exp_001_eval_3B_d100_para_aligned"
"exp_001_eval_3B_d100_s42_para_aligned"
"exp_001_eval_3B_d100_v2_aligned"
"exp_001_eval_3B_d100_v2_aligned_v2"
"exp_001_eval_3B_d100_v2_para_aligned"
"exp_001_eval_3B_d100_v2_s123_aligned"
"exp_001_eval_3B_raw_gen"
"exp_008_base_pretrained_15B_eval"
"exp_008_base_pretrained_15B_eval_v2"
"exp_008_base_pretrained_eval"
"exp_008_base_pretrained_eval_v2"
"exp_008_instruct_05B_eval"
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "62a54fcc-ed2f-45ec-a84b-7ceb98ac8c3e",
  "isSidechain": true,
  "promptId": "eec554ab-49eb-41f0-9151-4530891c32ce",
  "agentId": "aee0c4a84f025f3bb",
  "type": "user",
  "uuid": "6744757a-68f1-410e-b25a-03a2fb972c4a",
  "sourceToolAssistantUUID": "62a54fcc-ed2f-45ec-a84b-7ceb98ac8c3e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-15T18:26:13.984Z_

69 eval experiments. Now let me extract detailed info for all of them - status, metrics, and key parameters.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6744757a-68f1-410e-b25a-03a2fb972c4a",
  "isSidechain": true,
  "agentId": "aee0c4a84f025f3bb",
  "requestId": "req_011Cb4poLGPB4mRy6rj7iJjM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "48b955c6-1591-4653-9e2c-a56261531cd1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018Ac1fyZpebjraf1UqMpLV3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1720,
      "cache_read_input_tokens": 16699,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1720,
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

_source line 14 · 2026-05-15T18:26:17.587Z_

<details open><summary>🔧 Tool call — Bash · `toolu_014wqUwTanz67rto2CGXQoXA`</summary>

```json
{
  "command": "FILE=\"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/0e7bc130-13e2-45e1-ae79-20741112a4af/tool-results/mcp-agent-ml-research-read_registry-1778869532955.txt\"\ncat \"$FILE\" | jq -r '.result' | jq '\n  .data.experiments | to_entries[] \n  | select(.key | test(\"eval\"; \"i\")) \n  | {\n      exp_id: .key,\n      status: .value.status,\n      metrics: .value.metrics,\n      seed: .value.reproduce.spec.seed // .value.spec.seed // null,\n      model_name: .value.reproduce.spec.model_name // .value.spec.model_name // null,\n      eval_data: .value.reproduce.spec.eval_data // .value.spec.eval_data // null,\n      checkpoint_source: .value.reproduce.spec.checkpoint_source // .value.spec.checkpoint_source // null,\n      data_count: .value.reproduce.spec.data_count // .value.spec.data_count // null\n    }\n' 2>/dev/null | head -3000",
  "description": "Extract eval experiment details with metrics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "48b955c6-1591-4653-9e2c-a56261531cd1",
  "isSidechain": true,
  "agentId": "aee0c4a84f025f3bb",
  "requestId": "req_011Cb4poLGPB4mRy6rj7iJjM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "07ec43a8-d296-4ff6-9b37-c2a958f85656",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018Ac1fyZpebjraf1UqMpLV3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1720,
      "cache_read_input_tokens": 16699,
      "output_tokens": 416,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1720
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 416,
          "cache_read_input_tokens": 16699,
          "cache_creation_input_tokens": 1720,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1720,
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

_source line 15 · 2026-05-15T18:26:18.345Z_

<details><summary>↩ Tool result · `toolu_014wqUwTanz67rto2CGXQoXA`</summary>

```text
&lt;persisted-output>
Output too large (29.6KB). Full output saved to: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/0e7bc130-13e2-45e1-ae79-20741112a4af/tool-results/bp43hjy06.txt

Preview (first 2KB):
{
  "exp_id": "exp_001_eval_3B_d025_s123_aligned",
  "status": "DONE",
  "metrics": {
    "mmlu": 0.6367,
    "gsm8k": 0.5254,
    "arc_challenge": 0.8336,
    "humaneval": 0.1585
  },
  "seed": 123,
  "model_name": "Qwen2.5-3B",
  "eval_data": "mmlu,gsm8k,arc_challenge,humaneval",
  "checkpoint_source": "exp_001_sft_3B_d025_s123",
  "data_count": 4
}
{
  "exp_id": "exp_001_eval_3B_d005_s123_para_aligned",
  "status": "DONE",
  "metrics": {
    "MMLU": 0.6461,
    "GSM8K": 0.5,
    "ARC": 0.8192,
    "HumanEval": 0.0769
  },
  "seed": 123,
  "model_name": "Qwen2.5-3B",
  "eval_data": "mmlu,gsm8k,arc_challenge,humaneval (para_aligned)",
  "checkpoint_source": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d005_s123/lora_adapter",
  "data_count": 4
}
{
  "exp_id": "exp_001_eval_3B_d025_s123_para_aligned",
  "status": "DONE",
  "metrics": {
    "MMLU": 0.6615,
    "GSM8K": 0.4254,
    "ARC": 0.8121,
    "HumanEval": 0.1538
  },
  "seed": 123,
  "model_name": "Qwen2.5-3B",
  "eval_data": "mmlu,gsm8k,arc_challenge,humaneval (para_aligned)",
  "checkpoint_source": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_s123/lora_adapter",
  "data_count": 4
}
{
  "exp_id": "exp_001_eval_15B_d005_s123",
  "status": "DONE",
  "metrics": {
    "mmlu": {
      "accuracy": 0.5869,
      "correct": 8241,
      "total": 14042
    },
    "gsm8k": {
      "exact_match": 0.6482,
      "correct": 855,
      "total": 1319
    },
    "arc_challenge": {
      "accuracy": 0.7568,
      "correct": 887,
      "total": 1172
    },
    "humaneval": {
      "pass@1": 0.25,
      "correct": 41,
      "total": 164
    }
  },
  "seed": null,
  "model_name": null,
  "eval_data": null,
  "checkpoint_source": null,
  "data_count": null
}
{
  "exp_id": "exp_001_eval_15B_d005_s123_v2",
  "status": "DONE",
  "metrics": {
    "mmlu": {
      "accuracy": 0.5869,
      "correct": 8241,
      "total": 14042
    },
    "gsm8k": {
      "exact_match": 0.6482,
      "correct": 855,
      "total": 1319
    },
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "07ec43a8-d296-4ff6-9b37-c2a958f85656",
  "isSidechain": true,
  "promptId": "eec554ab-49eb-41f0-9151-4530891c32ce",
  "agentId": "aee0c4a84f025f3bb",
  "type": "user",
  "uuid": "52dc5666-c899-405f-b249-a3616d38d5ea",
  "sourceToolAssistantUUID": "07ec43a8-d296-4ff6-9b37-c2a958f85656",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-15T18:26:21.571Z_

Let me read the full output and also check for non-DONE statuses.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "52dc5666-c899-405f-b249-a3616d38d5ea",
  "isSidechain": true,
  "agentId": "aee0c4a84f025f3bb",
  "requestId": "req_011Cb4pou27fcynUex3LQJCF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9f4a8424-f73b-4a07-bb03-02be763304c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G3bV7qNX4fDjcJDDxqRrnF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1496,
      "cache_read_input_tokens": 18419,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1496,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 7,
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

_source line 17 · 2026-05-15T18:26:22.489Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HjwKy1uAM6rmxGXtPs4aFg`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/0e7bc130-13e2-45e1-ae79-20741112a4af/tool-results/bp43hjy06.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9f4a8424-f73b-4a07-bb03-02be763304c0",
  "isSidechain": true,
  "agentId": "aee0c4a84f025f3bb",
  "requestId": "req_011Cb4pou27fcynUex3LQJCF",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "71e0d96c-51bc-4d9d-b995-ae0c3c0bdf34",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G3bV7qNX4fDjcJDDxqRrnF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1496,
      "cache_read_input_tokens": 18419,
      "output_tokens": 149,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1496
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 149,
          "cache_read_input_tokens": 18419,
          "cache_creation_input_tokens": 1496,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1496,
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

_source line 18 · 2026-05-15T18:26:22.925Z_

<details><summary>↩ Tool result · `toolu_01HjwKy1uAM6rmxGXtPs4aFg`</summary>

```text
1	{
2	  "exp_id": "exp_001_eval_3B_d025_s123_aligned",
3	  "status": "DONE",
4	  "metrics": {
5	    "mmlu": 0.6367,
6	    "gsm8k": 0.5254,
7	    "arc_challenge": 0.8336,
8	    "humaneval": 0.1585
9	  },
10	  "seed": 123,
11	  "model_name": "Qwen2.5-3B",
12	  "eval_data": "mmlu,gsm8k,arc_challenge,humaneval",
13	  "checkpoint_source": "exp_001_sft_3B_d025_s123",
14	  "data_count": 4
15	}
16	{
17	  "exp_id": "exp_001_eval_3B_d005_s123_para_aligned",
18	  "status": "DONE",
19	  "metrics": {
20	    "MMLU": 0.6461,
21	    "GSM8K": 0.5,
22	    "ARC": 0.8192,
23	    "HumanEval": 0.0769
24	  },
25	  "seed": 123,
26	  "model_name": "Qwen2.5-3B",
27	  "eval_data": "mmlu,gsm8k,arc_challenge,humaneval (para_aligned)",
28	  "checkpoint_source": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d005_s123/lora_adapter",
29	  "data_count": 4
30	}
31	{
32	  "exp_id": "exp_001_eval_3B_d025_s123_para_aligned",
33	  "status": "DONE",
34	  "metrics": {
35	    "MMLU": 0.6615,
36	    "GSM8K": 0.4254,
37	    "ARC": 0.8121,
38	    "HumanEval": 0.1538
39	  },
40	  "seed": 123,
41	  "model_name": "Qwen2.5-3B",
42	  "eval_data": "mmlu,gsm8k,arc_challenge,humaneval (para_aligned)",
43	  "checkpoint_source": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_s123/lora_adapter",
44	  "data_count": 4
45	}
46	{
47	  "exp_id": "exp_001_eval_15B_d005_s123",
48	  "status": "DONE",
49	  "metrics": {
50	    "mmlu": {
51	      "accuracy": 0.5869,
52	      "correct": 8241,
53	      "total": 14042
54	    },
55	    "gsm8k": {
56	      "exact_match": 0.6482,
57	      "correct": 855,
58	      "total": 1319
59	    },
60	    "arc_challenge": {
61	      "accuracy": 0.7568,
62	      "correct": 887,
63	      "total": 1172
64	    },
65	    "humaneval": {
66	      "pass@1": 0.25,
67	      "correct": 41,
68	      "total": 164
69	    }
70	  },
71	  "seed": null,
72	  "model_name": null,
73	  "eval_data": null,
74	  "checkpoint_source": null,
75	  "data_count": null
76	}
77	{
78	  "exp_id": "exp_001_eval_15B_d005_s123_v2",
79	  "status": "DONE",
80	  "metrics": {
81	    "mmlu": {
82	      "accuracy": 0.5869,
83	      "correct": 8241,
84	      "total": 14042
85	    },
86	    "gsm8k": {
87	      "exact_match": 0.6482,
88	      "correct": 855,
89	      "total": 1319
90	    },
91	    "arc_challenge": {
92	      "accuracy": 0.7568,
93	      "correct": 887,
94	      "total": 1172
95	    },
96	    "humaneval": {
97	      "pass@1": 0.25,
98	      "correct": 41,
99	      "total": 164
100	    }
101	  },
102	  "seed": 123,
103	  "model_name": "Qwen2.5-1.5B",
104	  "eval_data": "mmlu,gsm8k,arc_challenge,humaneval",
105	  "checkpoint_source": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d005_s123/lora_adapter",
106	  "data_count": 0
107	}
108	{
109	  "exp_id": "exp_001_eval_15B_d025_s123",
110	  "status": "DONE",
111	  "metrics": {
112	    "mmlu": {
113	      "accuracy": 0.5881,
114	      "correct": 8258,
115	      "total": 14042
116	    },
117	    "gsm8k": {
118	      "exact_match": 0.655,
119	      "correct": 864,
120	      "total": 1319
121	    },
122	    "arc_challenge": {
123	      "accuracy": 0.7577,
124	      "correct": 888,
125	      "total": 1172
126	    },
127	    "humaneval": {
128	      "pass@1": 0.25,
129	      "correct": 41,
130	      "total": 164
131	    }
132	  },
133	  "seed": null,
134	  "model_name": null,
135	  "eval_data": null,
136	  "checkpoint_source": null,
137	  "data_count": null
138	}
139	{
140	  "exp_id": "exp_001_eval_15B_d025_s123_v2",
141	  "status": "DONE",
142	  "metrics": {
143	    "mmlu": {
144	      "accuracy": 0.5881,
145	      "correct": 8258,
146	      "total": 14042
147	    },
148	    "gsm8k": {
149	      "exact_match": 0.655,
150	      "correct": 864,
151	      "total": 1319
152	    },
153	    "arc_challenge": {
154	      "accuracy": 0.7577,
155	      "correct": 888,
156	      "total": 1172
157	    },
158	    "humaneval": {
159	      "pass@1": 0.25,
160	      "correct": 41,
161	      "total": 164
162	    }
163	  },
164	  "seed": 123,
165	  "model_name": "Qwen2.5-1.5B",
166	  "eval_data": "mmlu,gsm8k,arc_challenge,humaneval",
167	  "checkpoint_source": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d025_s123/lora_adapter",
168	  "data_count": 0
169	}
170	{
171	  "exp_id": "exp_001_eval_3B_d000_s42_para_aligned",
172	  "status": "DONE",
173	  "metrics": {
174	    "mmlu": {
175	      "accuracy": 0.6474,
176	      "correct": 4270,
177	      "total": 6596
178	    },
179	    "gsm8k": {
180	      "accuracy": 0.0482,
181	      "correct": 11,
182	      "total": 228
183	    },
184	    "arc_challenge": {
185	      "accuracy": 0.8235,
186	      "correct": 574,
187	      "total": 697
188	    },
189	    "humaneval": {
190	      "pass@1": 0.1154,
191	      "correct": 3,
192	      "total": 26
193	    }
194	  },
195	  "seed": 42,
196	  "model_name": "Qwen2.5-3B",
197	  "eval_data": "mmlu,gsm8k,arc_challenge,humaneval (para_aligned)",
198	  "checkpoint_source": "exp_001_sft_3B_d000_s42",
199	  "data_count": 4
200	}
201	{
202	  "exp_id": "exp_001_eval_3B_d100_s42_para_aligned",
203	  "status": "DONE",
204	  "metrics": {
205	    "mmlu": {
206	      "accuracy": 0.659,
207	      "correct": 4347,
208	      "total": 6596
209	    },
210	    "gsm8k": {
211	      "accuracy": 0.5833,
212	      "correct": 133,
213	      "total": 228
214	    },
215	    "arc_challenge": {
216	      "accuracy": 0.8092,
217	      "correct": 564,
218	      "total": 697
219	    },
220	    "humaneval": {
221	      "pass@1": 0.1154,
222	      "correct": 3,
223	      "total": 26
224	    }
225	  },
226	  "seed": 42,
227	  "model_name": "Qwen2.5-3B",
228	  "eval_data": "mmlu,gsm8k,arc_challenge,humaneval (para_aligned)",
229	  "checkpoint_source": "exp_001_sft_d100_3B_v2",
230	  "data_count": 4
231	}
232	{
233	  "exp_id": "exp_001_eval_3B_d000_s123_aligned",
234	  "status": "DONE",
235	  "metrics": {
236	    "mmlu": 0.6332,
237	    "gsm8k": 0.1812,
238	    "arc_challenge": 0.8328,
239	    "humaneval": 0.0854
240	  },
241	  "seed": 123,
242	  "model_name": "Qwen/Qwen2.5-3B",
243	  "eval_data": "mmlu gsm8k arc_challenge humaneval",
244	  "checkpoint_source": "exp_001_sft_3B_d000_s123",
245	  "data_count": 0
246	}
247	{
248	  "exp_id": "exp_001_eval_3B_d005_s42_aligned",
249	  "status": "DONE",
250	  "metrics": {
251	    "mmlu": 0.6345,
252	    "gsm8k": 0.2077,
253	    "arc_challenge": 0.8294,
254	    "humaneval": 0.1463
255	  },
256	  "seed": 42,
257	  "model_name": "Qwen/Qwen2.5-3B",
258	  "eval_data": "mmlu gsm8k arc_challenge humaneval",
259	  "checkpoint_source": "exp_001_sft_3B_d005_s42",
260	  "data_count": 0
261	}
262	{
263	  "exp_id": "exp_008_base_pretrained_eval_v2",
264	  "status": "DONE",
265	  "metrics": {
266	    "mmlu": 0.2294,
267	    "gsm8k": 0.163,
268	    "arc_challenge": 0.2278,
269	    "humaneval": 0
270	  },
271	  "seed": 42,
272	  "model_name": "Qwen2.5-0.5B",
273	  "eval_data": "mmlu,gsm8k,arc_challenge,humaneval",
274	  "checkpoint_source": null,
275	  "data_count": 0
276	}
277	{
278	  "exp_id": "exp_008_base_pretrained_15B_eval_v2",
279	  "status": "DONE",
280	  "metrics": {
281	    "mmlu": 0.2303,
282	    "gsm8k": 0.0053,
283	    "arc_challenge": 0.2304,
284	    "humaneval_pass1": 0.2317,
285	    "mmlu_correct": 3234,
286	    "mmlu_total": 14042,
287	    "gsm8k_correct": 7,
288	    "gsm8k_total": 1319,
289	    "arc_correct": 270,
290	    "arc_total": 1172,
291	    "humaneval_correct": 38,
292	    "humaneval_total": 164
293	  },
294	  "seed": 42,
295	  "model_name": "Qwen2.5-1.5B",
296	  "eval_data": null,
297	  "checkpoint_source": null,
298	  "data_count": 0
299	}
300	{
301	  "exp_id": "exp_008_base_pretrained_15B_eval",
302	  "status": "DONE",
303	  "metrics": {
304	    "mmlu_accuracy": 0.2303,
305	    "gsm8k_accuracy": 0.0053,
306	    "arc_challenge_accuracy": 0.2304,
307	    "humaneval_pass@1": 0.2317,
308	    "mmlu_correct": 3234,
309	    "mmlu_total": 14042,
310	    "gsm8k_correct": 7,
311	    "gsm8k_total": 1319,
312	    "arc_correct": 270,
313	    "arc_total": 1172,
314	    "humaneval_correct": 38,
315	    "humaneval_total": 164
316	  },
317	  "seed": null,
318	  "model_name": "Qwen2.5-1.5B",
319	  "eval_data": "mmlu,gsm8k,arc_challenge,humaneval",
320	  "checkpoint_source": null,
321	  "data_count": null
322	}
323	{
324	  "exp_id": "exp_008_base_pretrained_eval",
325	  "status": "DONE",
326	  "metrics": null,
327	  "seed": null,
328	  "model_name": "Qwen2.5-0.5B",
329	  "eval_data": "mmlu,gsm8k,arc_challenge,humaneval",
330	  "checkpoint_source": null,
331	  "data_count": null
332	}
333	{
334	  "exp_id": "exp_001_eval_15B_d000_s123_aligned",
335	  "status": "DONE",
336	  "metrics": {
337	    "mmlu_accuracy": 0.5855,
338	    "gsm8k_accuracy": 0.6535,
339	    "arc_challenge_accuracy": 0.7577,
340	    "humaneval_pass@1": 0.1707
341	  },
342	  "seed": null,
343	  "model_name": null,
344	  "eval_data": null,
345	  "checkpoint_source": null,
346	  "data_count": null
347	}
348	{
349	  "exp_id": "exp_001_eval_15B_d100_s123_aligned",
350	  "status": "DONE",
351	  "metrics": {
352	    "mmlu_accuracy": 0.5956,
353	    "gsm8k_accuracy": 0.6444,
354	    "arc_challenge_accuracy": 0.7816,
355	    "humaneval_pass@1": 0.2805
356	  },
357	  "seed": null,
358	  "model_name": null,
359	  "eval_data": null,
360	  "checkpoint_source": null,
361	  "data_count": null
362	}
363	{
364	  "exp_id": "exp_001_eval_05B_d000_s123_aligned",
365	  "status": "DONE",
366	  "metrics": {
367	    "mmlu": 0.4216,
368	    "gsm8k": 0.3412,
369	    "arc_challenge": 0.4974,
370	    "humaneval": 0.1037
371	  },
372	  "seed": null,
373	  "model_name": null,
374	  "eval_data": null,
375	  "checkpoint_source": null,
376	  "data_count": null
377	}
378	{
379	  "exp_id": "exp_001_eval_3B_d000_s42_v3",
380	  "status": "DONE",
381	  "metrics": {
382	    "mmlu": 0.634,
383	    "gsm8k": 0.1198,
384	    "arc_challenge": 0.8276,
385	    "humaneval": 0.1159
386	  },
387	  "seed": 42,
388	  "model_name": "Qwen2.5-3B",
389	  "eval_data": "mmlu,gsm8k,arc_challenge,humaneval",
390	  "checkpoint_source": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter",
391	  "data_count": 4
392	}
393	{
394	  "exp_id": "exp_001_eval_3B_d000_v2_s123_aligned",
395	  "status": "DONE",
396	  "metrics": {
397	    "mmlu": 0.6314,
398	    "gsm8k": 0.2676,
399	    "arc_challenge": 0.8259,
400	    "humaneval": 0.061
401	  },
402	  "seed": 123,
403	  "model_name": "Qwen2.5-3B",
404	  "eval_data": "mmlu,gsm8k,arc_challenge,humaneval",
405	  "checkpoint_source": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_v2_s123/lora_adapter",
406	  "data_count": 4
407	}
408	{
409	  "exp_id": "exp_001_eval_3B_d025_v2_aligned",
410	  "status": "DONE",
411	  "metrics": {
412	    "mmlu": 0.5998,
413	    "gsm8k": 0.6793,
414	    "arc_challenge": 0.8276,
415	    "humaneval": 0.0976
416	  },
417	  "seed": 42,
418	  "model_name": "Qwen2.5-3B",
419	  "eval_data": "mmlu,gsm8k,arc_challenge,humaneval",
420	  "checkpoint_source": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_s42/lora_adapter",
421	  "data_count": 4
422	}
423	{
424	  "exp_id": "exp_001_eval_3B_d100_v2_s123_aligned",
425	  "status": "DONE",
426	  "metrics": {
427	    "mmlu": 0.6319,
428	    "gsm8k": 0.7324,
429	    "arc_challenge": 0.8311,
430	    "humaneval": 0.1829
431	  },
432	  "seed": 123,
433	  "model_name": "Qwen2.5-3B",
434	  "eval_data": "mmlu,gsm8k,arc_challenge,humaneval",
435	  "checkpoint_source": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_s123/lora_adapter",
436	  "data_count": 4
437	}
438	{
439	  "exp_id": "exp_001_eval_05B_d025_s123_aligned",
440	  "status": "DONE",
441	  "metrics": {
442	    "mmlu": {
443	      "accuracy": 0.3473,
444	      "correct": 4877,
445	      "total": 14042
446	    },
447	    "gsm8k": {
448	      "accuracy": 0.3533,
449	      "correct": 466,
450	      "total": 1319
451	    },
452	    "arc_challenge": {
453	      "accuracy": 0.4061,
454	      "correct": 476,
455	      "total": 1172
456	    },
457	    "humaneval": {
458	      "pass@1": 0.0854,
459	      "correct": 14,
460	      "total": 164
461	    }
462	  },
463	  "seed": null,
464	  "model_name": null,
465	  "eval_data": null,
466	  "checkpoint_source": null,
467	  "data_count": null
468	}
469	{
470	  "exp_id": "exp_001_eval_05B_d000_s42_v7",
471	  "status": "DONE",
472	  "metrics": null,
473	  "seed": 42,
474	  "model_name": "Qwen2.5-0.5B",
475	  "eval_data": "mmlu,gsm8k,arc_challenge,humaneval",
476	  "checkpoint_source": "exp_001_sft_0pct_05B",
477	  "data_count": 4
478	}
479	{
480	  "exp_id": "exp_008_instruct_05B_eval",
481	  "status": "DONE",
482	  "metrics": {
483	    "mmlu_accuracy": 0.2462,
484	    "gsm8k_accuracy": 0.3882,
485	    "arc_challenge_accuracy": 0.2816,
486	    "humaneval_pass@1": 0
487	  },
488	  "seed": 42,
489	  "model_name": "Qwen2.5-0.5B-Instruct",
490	  "eval_data": "mmlu,gsm8k,arc_challenge,humaneval",
491	  "checkpoint_source": "/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-0.5B-Instruct",
492	  "data_count": 0
493	}
494	{
495	  "exp_id": "exp_001_eval_3B_d100_v2_aligned_v2",
496	  "status": "DONE",
497	  "metrics": {
498	    "mmlu_accuracy": 0.632,
499	    "gsm8k_accuracy": 0.7415,
500	    "arc_challenge_accuracy": 0.8242,
501	    "humaneval_pass@1": 0.1707
502	  },
503	  "seed": 42,
504	  "model_name": "Qwen2.5-3B",
505	  "eval_data": "mmlu,gsm8k,arc_challenge,humaneval",
506	  "checkpoint_source": "exp_001_sft_d100_3B_v2",
507	  "data_count": 0
508	}
509	{
510	  "exp_id": "exp_001_eval_3B_d025_v2_para_aligned",
511	  "status": "DONE",
512	  "metrics": {
513	    "mmlu_para_accuracy": 0.621,
514	    "gsm8k_para_accuracy": 0.5482,
515	    "arc_challenge_para_accuracy": 0.8106,
516	    "humaneval_para_pass@1": 0.1154
517	  },
518	  "seed": 42,
519	  "model_name": "Qwen2.5-3B (d025 v2 LoRA)",
520	  "eval_data": "mmlu,gsm8k,arc_challenge,humaneval (para_aligned)",
521	  "checkpoint_source": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d025_s42/lora_adapter",
522	  "data_count": 0
523	}
524	{
525	  "exp_id": "exp_001_eval_3B_d000_v2_s123_para_aligned",
526	  "status": "DONE",
527	  "metrics": {
528	    "mmlu_para_accuracy": 0.6512,
529	    "gsm8k_para_accuracy": 0.1491,
530	    "arc_challenge_para_accuracy": 0.8121,
531	    "humaneval_para_pass@1": 0.0385
532	  },
533	  "seed": 123,
534	  "model_name": "Qwen2.5-3B",
535	  "eval_data": "mmlu,gsm8k,arc_challenge,humaneval (para_aligned)",
536	  "checkpoint_source": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_v2_s123/lora_adapter",
537	  "data_count": 4
538	}
539	{
540	  "exp_id": "exp_001_eval_05B_d005_s123_para_aligned",
541	  "status": "DONE",
542	  "metrics": {
543	    "mmlu_para_accuracy": 0.3166,
544	    "gsm8k_para_accuracy": 0.2939,
545	    "arc_challenge_para_accuracy": 0.2912,
546	    "humaneval_para_pass@1": 0
547	  },
548	  "seed": 123,
549	  "model_name": "Qwen2.5-0.5B",
550	  "eval_data": "mmlu,gsm8k,arc_challenge,humaneval (para_aligned)",
551	  "checkpoint_source": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s123/lora_adapter",
552	  "data_count": 0
553	}
554	{
555	  "exp_id": "exp_001_eval_05B_d000_s42",
556	  "status": "DONE",
557	  "metrics": null,
558	  "seed": 42,
559	  "model_name": "Qwen2.5-0.5B",
560	  "eval_data": "mmlu,gsm8k,arc_challenge,humaneval",
561	  "checkpoint_source": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42/lora_adapter",
562	  "data_count": 0
563	}
564	{
565	  "exp_id": "exp_001_eval_05B_d005_s123_aligned",
566	  "status": "DONE",
567	  "metrics": {
568	    "mmlu_accuracy": 0.3002,
569	    "gsm8k_accuracy": 0.3677,
570	    "arc_challenge_accuracy": 0.2978,
571	    "humaneval_pass@1": 0.0976
572	  },
573	  "seed": 123,
574	  "model_name": "Qwen2.5-0.5B",
575	  "eval_data": "mmlu,gsm8k,arc_challenge,humaneval",
576	  "checkpoint_source": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s123/lora_adapter",
577	  "data_count": 4
578	}
579	{
580	  "exp_id": "exp_001_eval_3B_d000_v2_para_aligned_v3",
581	  "status": "DONE",
582	  "metrics": null,
583	  "seed": 42,
584	  "model_name": "Qwen2.5-3B",
585	  "eval_data": "mmlu gsm8k arc_challenge humaneval (para_aligned)",
586	  "checkpoint_source": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_v2_s42/lora_adapter",
587	  "data_count": 0
588	}
589	{
590	  "exp_id": "exp_001_eval_3B_d000_v2_para_aligned_v2",
591	  "status": "DONE",
592	  "metrics": {
593	    "mmlu_para_accuracy": 0.6468,
594	    "gsm8k_para_accuracy": 0.2895,
595	    "arc_challenge_para_accuracy": 0.8121,
596	    "humaneval_para_pass@1": 0.0385
597	  },
598	  "seed": 42,
599	  "model_name": "Qwen2.5-3B",
600	  "eval_data": "mmlu,gsm8k,arc_challenge,humaneval (paraphrased, aligned format)",
601	  "checkpoint_source": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_v2_s42/lora_adapter",
602	  "data_count": null
603	}
604	{
605	  "exp_id": "exp_001_eval_3B_d100_v2_para_aligned",
606	  "status": "DONE",
607	  "metrics": {
608	    "mmlu_para": 0.659,
609	    "gsm8k_para": 0.5833,
610	    "arc_challenge_para": 0.8092,
611	    "humaneval_para_pass1": 0.1154
612	  },
613	  "seed": 42,
614	  "model_name": "Qwen2.5-3B",
615	  "eval_data": "mmlu gsm8k arc_challenge humaneval (paraphrased, mc-format=aligned)",
616	  "checkpoint_source": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_s42/lora_adapter",
617	  "data_count": "4 benchmarks (paraphrased)"
618	}
619	{
620	  "exp_id": "exp_001_eval_3B_d000_v2_aligned",
621	  "status": "DONE",
622	  "metrics": {
623	    "mmlu": 0.6295,
624	    "gsm8k": 0.3525,
625	    "arc_challenge": 0.8183,
626	    "humaneval_pass@1": 0.0976
627	  },
628	  "seed": 42,
629	  "model_name": "Qwen2.5-3B",
630	  "eval_data": "mmlu,gsm8k,arc_challenge,humaneval",
631	  "checkpoint_source": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_v2_s42/lora_adapter",
632	  "data_count": 0
633	}
634	{
635	  "exp_id": "exp_001_eval_3B_d100_v2_aligned",
636	  "status": "DONE",
637	  "metrics": {
638	    "INVALID": "metrics were from v1 exp_001_eval_3B_d100_aligned, not v2. v2 output dir was empty. PID 461879 died before completion."
639	  },
640	  "seed": 42,
641	  "model_name": "Qwen2.5-3B + d100_v2_s42 LoRA (alpha=16)",
642	  "eval_data": "mmlu gsm8k arc_challenge aligned",
643	  "checkpoint_source": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_s42/lora_adapter",
644	  "data_count": 3
645	}
646	{
647	  "exp_id": "exp_001_eval_05B_d100_s123_aligned",
648	  "status": "DONE",
649	  "metrics": {
650	    "mmlu_accuracy": 0.3058,
651	    "gsm8k_accuracy": 0.3798,
652	    "arc_challenge_accuracy": 0.3669,
653	    "humaneval_pass_at_1": 0.1037,
654	    "mmlu_correct": 4294,
655	    "mmlu_total": 14042,
656	    "gsm8k_correct": 501,
657	    "gsm8k_total": 1319,
658	    "arc_challenge_correct": 430,
659	    "arc_challenge_total": 1172,
660	    "humaneval_total": 164
661	  },
662	  "seed": 123,
663	  "model_name": "Qwen2.5-0.5B",
664	  "eval_data": "mmlu,gsm8k,arc_challenge,humaneval",
665	  "checkpoint_source": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s123/lora_adapter",
666	  "data_count": 4
667	}
668	{
669	  "exp_id": "exp_001_eval_3B_d000_v2_para_aligned",
670	  "status": "DONE",
671	  "metrics": {
672	    "mmlu_para": 0.6468,
673	    "format": "paraphrased_aligned"
674	  },
675	  "seed": 42,
676	  "model_name": "Qwen2.5-3B + d000_v2_s42 LoRA",
677	  "eval_data": "mmlu gsm8k arc_challenge humaneval paraphrase",
678	  "checkpoint_source": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_v2_s42/lora_adapter",
679	  "data_count": 4
680	}
681	{
682	  "exp_id": "exp_001_eval_05B_d025_aligned_v2",
683	  "status": "DONE",
684	  "metrics": {
685	    "mmlu": 0.2835,
686	    "gsm8k": 0.3114,
687	    "arc_challenge": 0.3199,
688	    "humaneval_pass1": 0.1923,
689	    "format": "paraphrased_aligned"
690	  },
691	  "seed": 42,
692	  "model_name": "Qwen2.5-0.5B",
693	  "eval_data": "mmlu+gsm8k+arc_challenge+humaneval (paraphrased, aligned format)",
694	  "checkpoint_source": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d025_s42/lora_adapter",
695	  "data_count": 4
696	}
697	{
698	  "exp_id": "exp_001_eval_15B_d025_aligned",
699	  "status": "DONE",
700	  "metrics": {
701	    "mmlu": 0.5902,
702	    "gsm8k": 0.6535,
703	    "arc_challenge": 0.7688,
704	    "humaneval_pass1": 0.2256
705	  },
706	  "seed": null,
707	  "model_name": null,
708	  "eval_data": null,
709	  "checkpoint_source": null,
710	  "data_count": null
711	}
712	{
713	  "exp_id": "exp_001_eval_05B_d005_para_aligned",
714	  "status": "DONE",
715	  "metrics": {
716	    "mmlu": 0.3548,
717	    "gsm8k": 0.2588,
718	    "arc_challenge": 0.33,
719	    "humaneval": 0,
720	    "mmlu_correct": 2340,
721	    "mmlu_total": 6596,
722	    "gsm8k_correct": 59,
723	    "gsm8k_total": 228,
724	    "arc_correct": 230,
725	    "arc_total": 697,
726	    "humaneval_correct": 0,
727	    "humaneval_total": 26
728	  },
729	  "seed": 42,
730	  "model_name": "Qwen2.5-0.5B",
731	  "eval_data": "mmlu gsm8k arc_challenge humaneval paraphrase",
732	  "checkpoint_source": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s42/lora_adapter",
733	  "data_count": 4
734	}
735	{
736	  "exp_id": "exp_001_eval_15B_d025_para_aligned",
737	  "status": "DONE",
738	  "metrics": {
739	    "mmlu": 0.618,
740	    "gsm8k": 0.539,
741	    "arc_challenge": 0.766,
742	    "humaneval": 0.154
743	  },
744	  "seed": null,
745	  "model_name": null,
746	  "eval_data": null,
747	  "checkpoint_source": null,
748	  "data_count": null
749	}
750	{
751	  "exp_id": "exp_001_eval_3B_d100_para_aligned",
752	  "status": "DONE",
753	  "metrics": {
754	    "mmlu": 0.676,
755	    "gsm8k": 0.614,
756	    "arc_challenge": 0.828
757	  },
758	  "seed": null,
759	  "model_name": null,
760	  "eval_data": null,
761	  "checkpoint_source": null,
762	  "data_count": null
763	}
764	{
765	  "exp_id": "exp_001_eval_15B_aligned_batch",
766	  "status": "DONE",
767	  "metrics": {
768	    "mmlu": {
769	      "d000_orig": 0.5853,
770	      "d005_orig": 0.5852,
771	      "d100_orig": 0.5933,
772	      "d000_para": 0.6096,
773	      "d005_para": 0.6164,
774	      "d100_para": 0.6252
775	    },
776	    "gsm8k": {
777	      "d000_orig": 0.6543,
778	      "d005_orig": 0.6482,
779	      "d100_orig": 0.6497,
780	      "d000_para": 0.557,
781	      "d005_para": 0.5439,
782	      "d100_para": 0.5526
783	    },
784	    "arc": {
785	      "d000_orig": 0.7722,
786	      "d005_orig": 0.7688,
787	      "d100_orig": 0.7688,
788	      "d000_para": 0.7547,
789	      "d005_para": 0.7532,
790	      "d100_para": 0.7661
791	    },
792	    "humaneval": {
793	      "d000_orig": 0.128,
794	      "d005_orig": 0.25,
795	      "d100_orig": 0.3049,
796	      "d000_para": 0.0385,
797	      "d005_para": 0.1923,
798	      "d100_para": 0.2692
799	    },
800	    "key_finding": "MC benchmarks fail to detect contamination at 1.5B scale (<1pp). HumanEval shows strong dose-response (+17.69pp). Paraphrase gap does not cleanly separate contamination."
801	  },
802	  "seed": 42,
803	  "model_name": "Qwen2.5-1.5B",
804	  "eval_data": "original + paraphrase",
805	  "checkpoint_source": "d000_s42 / d005_s42 / d100_s42",
806	  "data_count": "3 dosages × 2 eval_types × 4 benchmarks"
807	}
808	{
809	  "exp_id": "exp_001_eval_15B_d100_aligned",
810	  "status": "DONE",
811	  "metrics": {
812	    "mmlu_accuracy": 0.5933,
813	    "gsm8k_accuracy": 0.6497,
814	    "arc_challenge_accuracy": 0.7688,
815	    "humaneval_correct": 50,
816	    "humaneval_total": 164,
817	    "humaneval_pass_rate": 0.3049
818	  },
819	  "seed": 42,
820	  "model_name": "Qwen2.5-1.5B",
821	  "eval_data": "MMLU+GSM8K+ARC+HumanEval aligned format",
822	  "checkpoint_source": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d100_s42/lora_adapter",
823	  "data_count": "4 benchmarks"
824	}
825	{
826	  "exp_id": "exp_001_eval_15B_d005_aligned_v2",
827	  "status": "DONE",
828	  "metrics": {
829	    "mmlu": 0.5852,
830	    "gsm8k": 0.6482,
831	    "arc_challenge": 0.7688,
832	    "humaneval_pass_at_1": 0.25
833	  },
834	  "seed": 42,
835	  "model_name": "Qwen2.5-1.5B",
836	  "eval_data": "mmlu,gsm8k,arc_challenge,humaneval",
837	  "checkpoint_source": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d005_s42/lora_adapter",
838	  "data_count": 4
839	}
840	{
841	  "exp_id": "exp_001_eval_05B_d100_aligned_v4",
842	  "status": "DONE",
843	  "metrics": {
844	    "mmlu": 0.2334,
845	    "gsm8k": 0.3654,
846	    "arc_challenge": 0.2944,
847	    "humaneval_pass_at_1": 0,
848	    "mmlu_delta_vs_d000": -0.1645,
849	    "arc_delta_vs_d000": -0.1749,
850	    "humaneval_delta_vs_d000": -0.1098
851	  },
852	  "seed": 42,
853	  "model_name": "Qwen2.5-0.5B",
854	  "eval_data": "mmlu gsm8k arc_challenge humaneval",
855	  "checkpoint_source": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42/lora_adapter",
856	  "data_count": 4
857	}
858	{
859	  "exp_id": "exp_001_eval_3B_d005_aligned",
860	  "status": "DONE",
861	  "metrics": {
862	    "mmlu": 0.634,
863	    "gsm8k": 0.208,
864	    "arc_challenge": 0.829,
865	    "humaneval_pass_at_1": 0.146
866	  },
867	  "seed": null,
868	  "model_name": "Qwen2.5-3B",
869	  "eval_data": "mmlu gsm8k arc_challenge humaneval",
870	  "checkpoint_source": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d005_s42/lora_adapter",
871	  "data_count": null
872	}
873	{
874	  "exp_id": "exp_001_eval_05B_d025_aligned",
875	  "status": "DONE",
876	  "metrics": {
877	    "MMLU": 28.03,
878	    "GSM8K": 36.62,
879	    "ARC": 32.51,
880	    "HumanEval": "missing - process exited before 4th benchmark"
881	  },
882	  "seed": null,
883	  "model_name": null,
884	  "eval_data": null,
885	  "checkpoint_source": null,
886	  "data_count": null
887	}
888	{
889	  "exp_id": "exp_001_eval_05B_d100_aligned_v3",
890	  "status": "DONE",
891	  "metrics": null,
892	  "seed": null,
893	  "model_name": null,
894	  "eval_data": null,
895	  "checkpoint_source": null,
896	  "data_count": null
897	}
898	{
899	  "exp_id": "exp_001_eval_3B_d100_aligned",
900	  "status": "DONE",
901	  "metrics": {
902	    "mmlu_accuracy": 0.6417,
903	    "gsm8k_exact_match": 0.6967,
904	    "arc_challenge_accuracy": 0.8396,
905	    "humaneval_pass1": 0.122
906	  },
907	  "seed": 42,
908	  "model_name": "Qwen2.5-3B",
909	  "eval_data": "original",
910	  "checkpoint_source": "exp_001_sft_d100_3B",
911	  "data_count": 16697
912	}
913	{
914	  "exp_id": "exp_001_eval_05B_d005_aligned",
915	  "status": "DONE",
916	  "metrics": {
917	    "d005_aligned_mmlu": 0.3255,
918	    "d005_aligned_gsm8k": 0.3624,
919	    "d005_aligned_arc": 0.3285,
920	    "d005_aligned_humaneval": 0.0793
921	  },
922	  "seed": 42,
923	  "model_name": "Qwen2.5-0.5B",
924	  "eval_data": "original aligned (D017)",
925	  "checkpoint_source": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s42/lora_adapter",
926	  "data_count": 16697
927	}
928	{
929	  "exp_id": "exp_001_eval_05B_d100_aligned",
930	  "status": "DONE",
931	  "metrics": null,
932	  "seed": 42,
933	  "model_name": "Qwen2.5-0.5B d100 s42",
934	  "eval_data": "original + paraphrase aligned (D017)",
935	  "checkpoint_source": "exp_001_sft_d100_05B",
936	  "data_count": "2 runs"
937	}
938	{
939	  "exp_id": "exp_001_eval_05B_aligned_batch",
940	  "status": "DONE",
941	  "metrics": {
942	    "d000_aligned_mmlu": 0.3979,
943	    "d000_aligned_gsm8k": 0.3692,
944	    "d000_aligned_arc": 0.4693,
945	    "d000_aligned_humaneval": 0.1098,
946	    "d000_para_aligned_mmlu": 0.4428,
947	    "d000_para_aligned_gsm8k": 0.2807,
948	    "d000_para_aligned_arc": 0.4792,
949	    "d000_para_aligned_humaneval": 0.1154,
950	    "d005_aligned_mmlu": 0.3255,
951	    "d005_aligned_gsm8k": 0.3624,
952	    "d005_aligned_arc": 0.3285,
953	    "d005_aligned_humaneval": 0.0793
954	  },
955	  "seed": 42,
956	  "model_name": "Qwen2.5-0.5B",
957	  "eval_data": "original + paraphrase",
958	  "checkpoint_source": "exp_001_sft_0pct_05B / exp_001_sft_d005_05B_v3 / exp_001_sft_d100_05B",
959	  "data_count": "3 dosages × 2 eval_types × 4 benchmarks"
960	}
961	{
962	  "exp_id": "exp_001_eval_05B_d005",
963	  "status": "DONE",
964	  "metrics": {
965	    "mmlu": 0.2929,
966	    "gsm8k": 0.3601,
967	    "arc_challenge": 0.2858,
968	    "humaneval_pass1": 0.0793,
969	    "mmlu_correct": 4113,
970	    "mmlu_total": 14042,
971	    "gsm8k_correct": 475,
972	    "gsm8k_total": 1319,
973	    "arc_correct": 335,
974	    "arc_total": 1172,
975	    "humaneval_correct": 13,
976	    "humaneval_total": 164
977	  },
978	  "seed": 42,
979	  "model_name": "Qwen2.5-0.5B",
980	  "eval_data": "mmlu,gsm8k,arc_challenge,humaneval",
981	  "checkpoint_source": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d005_s42/lora_adapter",
982	  "data_count": 0
983	}
984	{
985	  "exp_id": "exp_001_eval_3B_d000_aligned",
986	  "status": "DONE",
987	  "metrics": {
988	    "mmlu_accuracy": 0.634,
989	    "gsm8k_exact_match": 0.1198,
990	    "arc_challenge_accuracy": 0.8276,
991	    "humaneval_pass_at_1": 0.1159
992	  },
993	  "seed": null,
994	  "model_name": null,
995	  "eval_data": null,
996	  "checkpoint_source": null,
997	  "data_count": null
998	}
999	{
1000	  "exp_id": "exp_001_eval_15B_d100_s42",
1001	  "status": "DONE",
1002	  "metrics": {
1003	    "mmlu_accuracy": 0.5933,
1004	    "mmlu_correct": 8331,
1005	    "mmlu_total": 14042,
1006	    "gsm8k_exact_match": 0.6497,
1007	    "gsm8k_correct": 857,
1008	    "gsm8k_total": 1319,
1009	    "arc_challenge_accuracy": 0.7688,
1010	    "arc_challenge_correct": 901,
1011	    "arc_challenge_total": 1172,
1012	    "humaneval_pass_at_1": 0.3049,
1013	    "humaneval_correct": 50,
1014	    "humaneval_total": 164
1015	  },
1016	  "seed": 42,
1017	  "model_name": "Qwen2.5-1.5B",
1018	  "eval_data": "mmlu,gsm8k,arc_challenge,humaneval",
1019	  "checkpoint_source": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d100_s42/lora_adapter",
1020	  "data_count": 4
1021	}
1022	{
1023	  "exp_id": "exp_001_eval_3B_raw_gen",
1024	  "status": "DONE",
1025	  "metrics": {
1026	    "gsm8k": 0.605,
1027	    "humaneval": 0
1028	  },
1029	  "seed": 0,
1030	  "model_name": "Qwen2.5-3B",
1031	  "eval_data": "gsm8k,humaneval",
1032	  "checkpoint_source": null,
1033	  "data_count": 2
1034	}
1035	{
1036	  "exp_id": "exp_001_eval_05B_raw",
1037	  "status": "DONE",
1038	  "metrics": {
1039	    "mmlu": 0.2302,
1040	    "gsm8k": 0.1592,
1041	    "arc_challenge": 0.2261,
1042	    "humaneval": "incomplete (hung at 51/164)"
1043	  },
1044	  "seed": 42,
1045	  "model_name": "Qwen2.5-0.5B (raw base)",
1046	  "eval_data": "mmlu,gsm8k,arc_challenge,humaneval",
1047	  "checkpoint_source": null,
1048	  "data_count": 4
1049	}
1050	{
1051	  "exp_id": "exp_001_eval_05B_d100_v5",
1052	  "status": "DONE",
1053	  "metrics": {
1054	    "mmlu": 0.2322,
1055	    "gsm8k": 0.3571,
1056	    "arc_challenge": 0.227,
1057	    "humaneval_pass1": 0.0854
1058	  },
1059	  "seed": 42,
1060	  "model_name": "Qwen2.5-0.5B",
1061	  "eval_data": "mmlu,gsm8k,arc_challenge,humaneval",
1062	  "checkpoint_source": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42/lora_adapter",
1063	  "data_count": 4
1064	}
1065	{
1066	  "exp_id": "exp_001_eval_05B_d000_s42_v5",
1067	  "status": "DONE",
1068	  "metrics": {
1069	    "mmlu": 0.4049,
1070	    "gsm8k": 0.3647,
1071	    "arc_challenge": 0.378,
1072	    "humaneval": 0.1098
1073	  },
1074	  "seed": 42,
1075	  "model_name": "Qwen2.5-0.5B",
1076	  "eval_data": "mmlu,gsm8k,arc_challenge,humaneval",
1077	  "checkpoint_source": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s42/lora_adapter",
1078	  "data_count": 4
1079	}
1080	{
1081	  "exp_id": "exp_001_eval_3B_d000_s42",
1082	  "status": "DONE",
1083	  "metrics": {
1084	    "mmlu": 0.634,
1085	    "gsm8k": 0.117,
1086	    "arc": 0.822,
1087	    "humaneval": 0.116
1088	  },
1089	  "seed": 42,
1090	  "model_name": "Qwen2.5-3B",
1091	  "eval_data": "mmlu,gsm8k,arc_challenge,humaneval",
1092	  "checkpoint_source": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s42/lora_adapter",
1093	  "data_count": 26000
1094	}
1095	{
1096	  "exp_id": "exp_001_eval_05B_d100_v2",
1097	  "status": "DONE",
1098	  "metrics": null,
1099	  "seed": null,
1100	  "model_name": null,
1101	  "eval_data": null,
1102	  "checkpoint_source": null,
1103	  "data_count": null
1104	}
1105	{
1106	  "exp_id": "exp_001_eval_3B_d000_s123",
1107	  "status": "DONE",
1108	  "metrics": {
1109	    "mmlu_accuracy": 0.6362,
1110	    "gsm8k_exact_match": 0.1759,
1111	    "arc_challenge_accuracy": 0.8294,
1112	    "humaneval_pass_at_1": 0.0854
1113	  },
1114	  "seed": 123,
1115	  "model_name": "Qwen2.5-3B",
1116	  "eval_data": "mmlu,gsm8k,arc_challenge,humaneval",
1117	  "checkpoint_source": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_s123/lora_adapter",
1118	  "data_count": 26000
1119	}
1120	{
1121	  "exp_id": "exp_001_eval_15B_d000_s123",
1122	  "status": "DONE",
1123	  "metrics": {
1124	    "mmlu": 0.5762,
1125	    "gsm8k": 0.6331,
1126	    "arc_challenge": 0.7662,
1127	    "humaneval_pass@1": 0.1707
1128	  },
1129	  "seed": 123,
1130	  "model_name": "Qwen2.5-1.5B",
1131	  "eval_data": "mmlu,gsm8k,arc_challenge,humaneval",
1132	  "checkpoint_source": "exp_001_sft_0pct_15B_s123",
1133	  "data_count": "4 benchmarks"
1134	}
1135	{
1136	  "exp_id": "exp_001_eval_15B_d000_s42_v2",
1137	  "status": "DONE",
1138	  "metrics": {
1139	    "arc_challenge_accuracy": 0.7756,
1140	    "arc_challenge_correct": 909,
1141	    "arc_challenge_total": 1172,
1142	    "gsm8k_correct": 840,
1143	    "gsm8k_exact_match": 0.6368,
1144	    "gsm8k_total": 1319,
1145	    "humaneval_correct": 21,
1146	    "humaneval_pass_at_1": 0.128,
1147	    "humaneval_total": 164,
1148	    "mmlu_accuracy": 0.5753,
1149	    "mmlu_correct": 8079,
1150	    "mmlu_total": 14042
1151	  },
1152	  "seed": 42,
1153	  "model_name": "Qwen2.5-1.5B",
1154	  "eval_data": "mmlu,gsm8k,arc_challenge,humaneval",
1155	  "checkpoint_source": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d000_s42/lora_adapter",
1156	  "data_count": 26000
1157	}
1158	{
1159	  "exp_id": "exp_001_eval_05B_d100",
1160	  "status": "DONE",
1161	  "metrics": null,
1162	  "seed": 42,
1163	  "model_name": "Qwen2.5-0.5B",
1164	  "eval_data": "mmlu,gsm8k,arc_challenge,humaneval",
1165	  "checkpoint_source": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d100_s42/lora_adapter",
1166	  "data_count": 4
1167	}
1168	{
1169	  "exp_id": "exp_001_eval_05B_d000_s123",
1170	  "status": "DONE",
1171	  "metrics": {
1172	    "arc_challenge_accuracy": 0.3976,
1173	    "gsm8k_exact_match": 0.3404,
1174	    "humaneval_pass_at_1": 0.1037,
1175	    "mmlu_accuracy": 0.4182
1176	  },
1177	  "seed": 123,
1178	  "model_name": "Qwen2.5-0.5B",
1179	  "eval_data": "mmlu gsm8k arc_challenge humaneval",
1180	  "checkpoint_source": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-0.5B_d000_s123/lora_adapter",
1181	  "data_count": null
1182	}
1183	{
1184	  "exp_id": "exp_001_eval_15B_d000_s42",
1185	  "status": "DONE",
1186	  "metrics": null,
1187	  "seed": 42,
1188	  "model_name": "Qwen2.5-1.5B + LoRA (d000_s42)",
1189	  "eval_data": "MMLU, GSM8K, ARC-Challenge, HumanEval (original)",
1190	  "checkpoint_source": "/root/autodl-tmp/exp001/checkpoints/Qwen2.5-1.5B_d000_s42/lora_adapter/",
1191	  "data_count": "~26000 items total"
1192	}
1193	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "71e0d96c-51bc-4d9d-b995-ae0c3c0bdf34",
  "isSidechain": true,
  "promptId": "eec554ab-49eb-41f0-9151-4530891c32ce",
  "agentId": "aee0c4a84f025f3bb",
  "type": "user",
  "uuid": "e40736f5-86ae-47af-86a4-f3b89e7ed9d3",
  "sourceToolAssistantUUID": "71e0d96c-51bc-4d9d-b995-ae0c3c0bdf34",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-15T18:26:26.195Z_

Now let me also check statuses and get a summary of non-DONE evals.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e40736f5-86ae-47af-86a4-f3b89e7ed9d3",
  "isSidechain": true,
  "agentId": "aee0c4a84f025f3bb",
  "requestId": "req_011Cb4ppEGzyEjvSoVJw1ML7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e223d7f3-a8db-4716-9658-3d4286369773",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J6GiYdhbQzmWQ1JZdkYGYb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17222,
      "cache_read_input_tokens": 19915,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17222,
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

_source line 20 · 2026-05-15T18:26:31.188Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01YXeppSYx5cup3gZ5J8Puzi`</summary>

```json
{
  "command": "FILE=\"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/0e7bc130-13e2-45e1-ae79-20741112a4af/tool-results/mcp-agent-ml-research-read_registry-1778869532955.txt\"\ncat \"$FILE\" | jq -r '.result' | jq '\n  .data.experiments | to_entries[] \n  | select(.key | test(\"eval\"; \"i\")) \n  | select(.value.status != \"DONE\")\n  | {exp_id: .key, status: .value.status}\n'",
  "description": "Check for non-DONE eval experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e223d7f3-a8db-4716-9658-3d4286369773",
  "isSidechain": true,
  "agentId": "aee0c4a84f025f3bb",
  "requestId": "req_011Cb4ppEGzyEjvSoVJw1ML7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ed82e010-ed5b-4b1b-b430-5916b8da0b35",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J6GiYdhbQzmWQ1JZdkYGYb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 17222,
      "cache_read_input_tokens": 19915,
      "output_tokens": 266,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 17222
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 266,
          "cache_read_input_tokens": 19915,
          "cache_creation_input_tokens": 17222,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 17222,
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

_source line 21 · 2026-05-15T18:26:31.480Z_

<details><summary>↩ Tool result · `toolu_01YXeppSYx5cup3gZ5J8Puzi`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ed82e010-ed5b-4b1b-b430-5916b8da0b35",
  "isSidechain": true,
  "promptId": "eec554ab-49eb-41f0-9151-4530891c32ce",
  "agentId": "aee0c4a84f025f3bb",
  "type": "user",
  "uuid": "3769052f-ea07-481d-ac72-58102dec2013",
  "sourceToolAssistantUUID": "ed82e010-ed5b-4b1b-b430-5916b8da0b35",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-15T18:26:35.345Z_

All 69 eval experiments have status "DONE". Now let me create a comprehensive structured summary by normalizing the metrics and organizing by scale/dose/seed/eval_type.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3769052f-ea07-481d-ac72-58102dec2013",
  "isSidechain": true,
  "agentId": "aee0c4a84f025f3bb",
  "requestId": "req_011Cb4pprf1i1NE4S6gED8uN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4d737297-2e1e-4d09-a678-24b86908777f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UYTh51yWZfGH66n4yCt7G4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 284,
      "cache_read_input_tokens": 37137,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 284,
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

_source line 23 · 2026-05-15T18:26:55.038Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Sv9TQiC2e2fBivbCtknS5o`</summary>

```json
{
  "command": "FILE=\"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/0e7bc130-13e2-45e1-ae79-20741112a4af/tool-results/mcp-agent-ml-research-read_registry-1778869532955.txt\"\ncat \"$FILE\" | jq -r '.result' | python3 -c \"\nimport json, sys, re\n\ndata = json.load(sys.stdin)\nexps = data['data']['experiments']\n\neval_exps = {k: v for k, v in exps.items() if 'eval' in k.lower()}\n\n# Parse experiment IDs to extract scale, dose, seed, eval_type, version\ndef parse_exp_id(exp_id):\n    info = {}\n    # Scale\n    if '05B' in exp_id: info['scale'] = '0.5B'\n    elif '15B' in exp_id: info['scale'] = '1.5B'\n    elif '3B' in exp_id: info['scale'] = '3B'\n    else: info['scale'] = 'unknown'\n    \n    # Dose\n    m = re.search(r'd(\\d{3})', exp_id)\n    if m:\n        dose_map = {'000': '0%', '005': '5%', '025': '25%', '100': '100%'}\n        info['dose'] = dose_map.get(m.group(1), m.group(1))\n    else:\n        info['dose'] = 'N/A'\n    \n    # Seed\n    m = re.search(r's(\\d+)', exp_id)\n    if m: info['seed'] = int(m.group(1))\n    else: info['seed'] = None\n    \n    # Eval type\n    if 'para_aligned' in exp_id:\n        info['eval_type'] = 'para_aligned'\n    elif 'aligned' in exp_id:\n        info['eval_type'] = 'aligned'\n    elif 'raw' in exp_id or 'raw_gen' in exp_id:\n        info['eval_type'] = 'raw'\n    elif 'batch' in exp_id:\n        info['eval_type'] = 'batch'\n    else:\n        info['eval_type'] = 'standard'\n    \n    # Version\n    m = re.search(r'_v(\\d+)', exp_id)\n    info['version'] = int(m.group(1)) if m else 1\n    \n    # Experiment series\n    m = re.search(r'(exp_\\d+)', exp_id)\n    info['series'] = m.group(1) if m else 'unknown'\n    \n    return info\n\n# Normalize metrics to simple float values\ndef normalize_metrics(metrics):\n    if metrics is None:\n        return None\n    result = {}\n    for k, v in metrics.items():\n        if isinstance(v, (int, float)):\n            result[k] = round(float(v), 4)\n        elif isinstance(v, dict):\n            # nested metrics (some have accuracy/correct/total or dose breakdowns)\n            result[k] = v\n        elif isinstance(v, str):\n            result[k] = v\n    return result\n\n# Output structured summary\nresults = []\nfor exp_id, exp_data in sorted(eval_exps.items()):\n    parsed = parse_exp_id(exp_id)\n    metrics = normalize_metrics(exp_data.get('metrics'))\n    \n    # Also check spec-level info\n    seed = parsed['seed']\n    model_name = None\n    checkpoint_source = None\n    for path in [exp_data.get('reproduce', {}).get('spec', {}), exp_data.get('spec', {})]:\n        if isinstance(path, dict):\n            if not seed and path.get('seed'): seed = path['seed']\n            if not model_name and path.get('model_name'): model_name = path['model_name']\n            if not checkpoint_source and path.get('checkpoint_source'): checkpoint_source = path['checkpoint_source']\n    \n    results.append({\n        'exp_id': exp_id,\n        'series': parsed['series'],\n        'scale': parsed['scale'],\n        'dose': parsed['dose'],\n        'seed': seed,\n        'eval_type': parsed['eval_type'],\n        'version': parsed['version'],\n        'status': exp_data['status'],\n        'has_metrics': metrics is not None and len(metrics) > 0,\n        'metrics': metrics,\n        'model_name': model_name,\n        'checkpoint_source': checkpoint_source,\n    })\n\n# Print organized by scale\nfor scale in ['0.5B', '1.5B', '3B', 'unknown']:\n    scale_exps = [r for r in results if r['scale'] == scale]\n    if not scale_exps:\n        continue\n    print(f'\\\\n{\\\"=\\\"*80}')\n    print(f'SCALE: {scale} ({len(scale_exps)} experiments)')\n    print(f'{\\\"=\\\"*80}')\n    \n    for dose in ['0%', '5%', '25%', '100%', 'N/A']:\n        dose_exps = [r for r in scale_exps if r['dose'] == dose]\n        if not dose_exps:\n            continue\n        print(f'\\\\n  --- Dose: {dose} ---')\n        for exp in sorted(dose_exps, key=lambda x: (x['eval_type'], x['seed'] or 0, x['version'])):\n            seed_str = f's{exp[\\\"seed\\\"]}' if exp['seed'] else 'no_seed'\n            print(f'  [{exp[\\\"exp_id\\\"]}]  type={exp[\\\"eval_type\\\"]}  {seed_str}  v{exp[\\\"version\\\"]}  metrics={\\\"YES\\\" if exp[\\\"has_metrics\\\"] else \\\"NO\\\"}')\n            if exp['metrics']:\n                for mk, mv in exp['metrics'].items():\n                    if isinstance(mv, dict):\n                        print(f'    {mk}: {json.dumps(mv)}')\n                    else:\n                        print(f'    {mk}: {mv}')\n\" 2>&1",
  "description": "Parse all eval experiments into organized structured summary",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4d737297-2e1e-4d09-a678-24b86908777f",
  "isSidechain": true,
  "agentId": "aee0c4a84f025f3bb",
  "requestId": "req_011Cb4pprf1i1NE4S6gED8uN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a50883e3-1fe6-4e92-8484-00682da7c449",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UYTh51yWZfGH66n4yCt7G4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 284,
      "cache_read_input_tokens": 37137,
      "output_tokens": 1698,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 284
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1698,
          "cache_read_input_tokens": 37137,
          "cache_creation_input_tokens": 284,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 284,
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

_source line 24 · 2026-05-15T18:26:55.804Z_

<details><summary>↩ Tool result · `toolu_01Sv9TQiC2e2fBivbCtknS5o`</summary>

```text
================================================================================
SCALE: 0.5B (23 experiments)
================================================================================

  --- Dose: 0% ---
  [exp_001_eval_05B_d000_s123_aligned]  type=aligned  s123  v1  metrics=YES
    mmlu: 0.4216
    gsm8k: 0.3412
    arc_challenge: 0.4974
    humaneval: 0.1037
  [exp_001_eval_05B_d000_s42]  type=standard  s42  v1  metrics=NO
  [exp_001_eval_05B_d000_s42_v5]  type=standard  s42  v5  metrics=YES
    mmlu: 0.4049
    gsm8k: 0.3647
    arc_challenge: 0.378
    humaneval: 0.1098
  [exp_001_eval_05B_d000_s42_v7]  type=standard  s42  v7  metrics=NO
  [exp_001_eval_05B_d000_s123]  type=standard  s123  v1  metrics=YES
    arc_challenge_accuracy: 0.3976
    gsm8k_exact_match: 0.3404
    humaneval_pass_at_1: 0.1037
    mmlu_accuracy: 0.4182

  --- Dose: 5% ---
  [exp_001_eval_05B_d005_aligned]  type=aligned  s42  v1  metrics=YES
    d005_aligned_mmlu: 0.3255
    d005_aligned_gsm8k: 0.3624
    d005_aligned_arc: 0.3285
    d005_aligned_humaneval: 0.0793
  [exp_001_eval_05B_d005_s123_aligned]  type=aligned  s123  v1  metrics=YES
    mmlu_accuracy: 0.3002
    gsm8k_accuracy: 0.3677
    arc_challenge_accuracy: 0.2978
    humaneval_pass@1: 0.0976
  [exp_001_eval_05B_d005_para_aligned]  type=para_aligned  s42  v1  metrics=YES
    mmlu: 0.3548
    gsm8k: 0.2588
    arc_challenge: 0.33
    humaneval: 0.0
    mmlu_correct: 2340.0
    mmlu_total: 6596.0
    gsm8k_correct: 59.0
    gsm8k_total: 228.0
    arc_correct: 230.0
    arc_total: 697.0
    humaneval_correct: 0.0
    humaneval_total: 26.0
  [exp_001_eval_05B_d005_s123_para_aligned]  type=para_aligned  s123  v1  metrics=YES
    mmlu_para_accuracy: 0.3166
    gsm8k_para_accuracy: 0.2939
    arc_challenge_para_accuracy: 0.2912
    humaneval_para_pass@1: 0.0
  [exp_001_eval_05B_d005]  type=standard  s42  v1  metrics=YES
    mmlu: 0.2929
    gsm8k: 0.3601
    arc_challenge: 0.2858
    humaneval_pass1: 0.0793
    mmlu_correct: 4113.0
    mmlu_total: 14042.0
    gsm8k_correct: 475.0
    gsm8k_total: 1319.0
    arc_correct: 335.0
    arc_total: 1172.0
    humaneval_correct: 13.0
    humaneval_total: 164.0

  --- Dose: 25% ---
  [exp_001_eval_05B_d025_aligned]  type=aligned  no_seed  v1  metrics=YES
    MMLU: 28.03
    GSM8K: 36.62
    ARC: 32.51
    HumanEval: missing - process exited before 4th benchmark
  [exp_001_eval_05B_d025_aligned_v2]  type=aligned  s42  v2  metrics=YES
    mmlu: 0.2835
    gsm8k: 0.3114
    arc_challenge: 0.3199
    humaneval_pass1: 0.1923
    format: paraphrased_aligned
  [exp_001_eval_05B_d025_s123_aligned]  type=aligned  s123  v1  metrics=YES
    mmlu: {"accuracy": 0.3473, "correct": 4877, "total": 14042}
    gsm8k: {"accuracy": 0.3533, "correct": 466, "total": 1319}
    arc_challenge: {"accuracy": 0.4061, "correct": 476, "total": 1172}
    humaneval: {"pass@1": 0.0854, "correct": 14, "total": 164}

  --- Dose: 100% ---
  [exp_001_eval_05B_d100_aligned_v3]  type=aligned  no_seed  v3  metrics=NO
  [exp_001_eval_05B_d100_aligned]  type=aligned  s42  v1  metrics=NO
  [exp_001_eval_05B_d100_aligned_v4]  type=aligned  s42  v4  metrics=YES
    mmlu: 0.2334
    gsm8k: 0.3654
    arc_challenge: 0.2944
    humaneval_pass_at_1: 0.0
    mmlu_delta_vs_d000: -0.1645
    arc_delta_vs_d000: -0.1749
    humaneval_delta_vs_d000: -0.1098
  [exp_001_eval_05B_d100_s123_aligned]  type=aligned  s123  v1  metrics=YES
    mmlu_accuracy: 0.3058
    gsm8k_accuracy: 0.3798
    arc_challenge_accuracy: 0.3669
    humaneval_pass_at_1: 0.1037
    mmlu_correct: 4294.0
    mmlu_total: 14042.0
    gsm8k_correct: 501.0
    gsm8k_total: 1319.0
    arc_challenge_correct: 430.0
    arc_challenge_total: 1172.0
    humaneval_total: 164.0
  [exp_001_eval_05B_d100_v2]  type=standard  no_seed  v2  metrics=NO
  [exp_001_eval_05B_d100]  type=standard  s42  v1  metrics=NO
  [exp_001_eval_05B_d100_v5]  type=standard  s42  v5  metrics=YES
    mmlu: 0.2322
    gsm8k: 0.3571
    arc_challenge: 0.227
    humaneval_pass1: 0.0854

  --- Dose: N/A ---
  [exp_001_eval_05B_aligned_batch]  type=aligned  s42  v1  metrics=YES
    d000_aligned_mmlu: 0.3979
    d000_aligned_gsm8k: 0.3692
    d000_aligned_arc: 0.4693
    d000_aligned_humaneval: 0.1098
    d000_para_aligned_mmlu: 0.4428
    d000_para_aligned_gsm8k: 0.2807
    d000_para_aligned_arc: 0.4792
    d000_para_aligned_humaneval: 0.1154
    d005_aligned_mmlu: 0.3255
    d005_aligned_gsm8k: 0.3624
    d005_aligned_arc: 0.3285
    d005_aligned_humaneval: 0.0793
  [exp_001_eval_05B_raw]  type=raw  s42  v1  metrics=YES
    mmlu: 0.2302
    gsm8k: 0.1592
    arc_challenge: 0.2261
    humaneval: incomplete (hung at 51/164)
  [exp_008_instruct_05B_eval]  type=standard  s42  v1  metrics=YES
    mmlu_accuracy: 0.2462
    gsm8k_accuracy: 0.3882
    arc_challenge_accuracy: 0.2816
    humaneval_pass@1: 0.0

================================================================================
SCALE: 1.5B (17 experiments)
================================================================================

  --- Dose: 0% ---
  [exp_001_eval_15B_d000_s123_aligned]  type=aligned  s123  v1  metrics=YES
    mmlu_accuracy: 0.5855
    gsm8k_accuracy: 0.6535
    arc_challenge_accuracy: 0.7577
    humaneval_pass@1: 0.1707
  [exp_001_eval_15B_d000_s42]  type=standard  s42  v1  metrics=NO
  [exp_001_eval_15B_d000_s42_v2]  type=standard  s42  v2  metrics=YES
    arc_challenge_accuracy: 0.7756
    arc_challenge_correct: 909.0
    arc_challenge_total: 1172.0
    gsm8k_correct: 840.0
    gsm8k_exact_match: 0.6368
    gsm8k_total: 1319.0
    humaneval_correct: 21.0
    humaneval_pass_at_1: 0.128
    humaneval_total: 164.0
    mmlu_accuracy: 0.5753
    mmlu_correct: 8079.0
    mmlu_total: 14042.0
  [exp_001_eval_15B_d000_s123]  type=standard  s123  v1  metrics=YES
    mmlu: 0.5762
    gsm8k: 0.6331
    arc_challenge: 0.7662
    humaneval_pass@1: 0.1707

  --- Dose: 5% ---
  [exp_001_eval_15B_d005_aligned_v2]  type=aligned  s42  v2  metrics=YES
    mmlu: 0.5852
    gsm8k: 0.6482
    arc_challenge: 0.7688
    humaneval_pass_at_1: 0.25
  [exp_001_eval_15B_d005_s123]  type=standard  s123  v1  metrics=YES
    mmlu: {"accuracy": 0.5869, "correct": 8241, "total": 14042}
    gsm8k: {"exact_match": 0.6482, "correct": 855, "total": 1319}
    arc_challenge: {"accuracy": 0.7568, "correct": 887, "total": 1172}
    humaneval: {"pass@1": 0.25, "correct": 41, "total": 164}
  [exp_001_eval_15B_d005_s123_v2]  type=standard  s123  v2  metrics=YES
    mmlu: {"accuracy": 0.5869, "correct": 8241, "total": 14042}
    gsm8k: {"exact_match": 0.6482, "correct": 855, "total": 1319}
    arc_challenge: {"accuracy": 0.7568, "correct": 887, "total": 1172}
    humaneval: {"pass@1": 0.25, "correct": 41, "total": 164}

  --- Dose: 25% ---
  [exp_001_eval_15B_d025_aligned]  type=aligned  no_seed  v1  metrics=YES
    mmlu: 0.5902
    gsm8k: 0.6535
    arc_challenge: 0.7688
    humaneval_pass1: 0.2256
  [exp_001_eval_15B_d025_para_aligned]  type=para_aligned  no_seed  v1  metrics=YES
    mmlu: 0.618
    gsm8k: 0.539
    arc_challenge: 0.766
    humaneval: 0.154
  [exp_001_eval_15B_d025_s123]  type=standard  s123  v1  metrics=YES
    mmlu: {"accuracy": 0.5881, "correct": 8258, "total": 14042}
    gsm8k: {"exact_match": 0.655, "correct": 864, "total": 1319}
    arc_challenge: {"accuracy": 0.7577, "correct": 888, "total": 1172}
    humaneval: {"pass@1": 0.25, "correct": 41, "total": 164}
  [exp_001_eval_15B_d025_s123_v2]  type=standard  s123  v2  metrics=YES
    mmlu: {"accuracy": 0.5881, "correct": 8258, "total": 14042}
    gsm8k: {"exact_match": 0.655, "correct": 864, "total": 1319}
    arc_challenge: {"accuracy": 0.7577, "correct": 888, "total": 1172}
    humaneval: {"pass@1": 0.25, "correct": 41, "total": 164}

  --- Dose: 100% ---
  [exp_001_eval_15B_d100_aligned]  type=aligned  s42  v1  metrics=YES
    mmlu_accuracy: 0.5933
    gsm8k_accuracy: 0.6497
    arc_challenge_accuracy: 0.7688
    humaneval_correct: 50.0
    humaneval_total: 164.0
    humaneval_pass_rate: 0.3049
  [exp_001_eval_15B_d100_s123_aligned]  type=aligned  s123  v1  metrics=YES
    mmlu_accuracy: 0.5956
    gsm8k_accuracy: 0.6444
    arc_challenge_accuracy: 0.7816
    humaneval_pass@1: 0.2805
  [exp_001_eval_15B_d100_s42]  type=standard  s42  v1  metrics=YES
    mmlu_accuracy: 0.5933
    mmlu_correct: 8331.0
    mmlu_total: 14042.0
    gsm8k_exact_match: 0.6497
    gsm8k_correct: 857.0
    gsm8k_total: 1319.0
    arc_challenge_accuracy: 0.7688
    arc_challenge_correct: 901.0
    arc_challenge_total: 1172.0
    humaneval_pass_at_1: 0.3049
    humaneval_correct: 50.0
    humaneval_total: 164.0

  --- Dose: N/A ---
  [exp_001_eval_15B_aligned_batch]  type=aligned  s42  v1  metrics=YES
    mmlu: {"d000_orig": 0.5853, "d005_orig": 0.5852, "d100_orig": 0.5933, "d000_para": 0.6096, "d005_para": 0.6164, "d100_para": 0.6252}
    gsm8k: {"d000_orig": 0.6543, "d005_orig": 0.6482, "d100_orig": 0.6497, "d000_para": 0.557, "d005_para": 0.5439, "d100_para": 0.5526}
    arc: {"d000_orig": 0.7722, "d005_orig": 0.7688, "d100_orig": 0.7688, "d000_para": 0.7547, "d005_para": 0.7532, "d100_para": 0.7661}
    humaneval: {"d000_orig": 0.128, "d005_orig": 0.25, "d100_orig": 0.3049, "d000_para": 0.0385, "d005_para": 0.1923, "d100_para": 0.2692}
    key_finding: MC benchmarks fail to detect contamination at 1.5B scale (<1pp). HumanEval shows strong dose-response (+17.69pp). Paraphrase gap does not cleanly separate contamination.
  [exp_008_base_pretrained_15B_eval]  type=standard  no_seed  v1  metrics=YES
    mmlu_accuracy: 0.2303
    gsm8k_accuracy: 0.0053
    arc_challenge_accuracy: 0.2304
    humaneval_pass@1: 0.2317
    mmlu_correct: 3234.0
    mmlu_total: 14042.0
    gsm8k_correct: 7.0
    gsm8k_total: 1319.0
    arc_correct: 270.0
    arc_total: 1172.0
    humaneval_correct: 38.0
    humaneval_total: 164.0
  [exp_008_base_pretrained_15B_eval_v2]  type=standard  s42  v2  metrics=YES
    mmlu: 0.2303
    gsm8k: 0.0053
    arc_challenge: 0.2304
    humaneval_pass1: 0.2317
    mmlu_correct: 3234.0
    mmlu_total: 14042.0
    gsm8k_correct: 7.0
    gsm8k_total: 1319.0
    arc_correct: 270.0
    arc_total: 1172.0
    humaneval_correct: 38.0
    humaneval_total: 164.0

================================================================================
SCALE: 3B (27 experiments)
================================================================================

  --- Dose: 0% ---
  [exp_001_eval_3B_d000_aligned]  type=aligned  no_seed  v1  metrics=YES
    mmlu_accuracy: 0.634
    gsm8k_exact_match: 0.1198
    arc_challenge_accuracy: 0.8276
    humaneval_pass_at_1: 0.1159
  [exp_001_eval_3B_d000_v2_aligned]  type=aligned  s42  v2  metrics=YES
    mmlu: 0.6295
    gsm8k: 0.3525
    arc_challenge: 0.8183
    humaneval_pass@1: 0.0976
  [exp_001_eval_3B_d000_s123_aligned]  type=aligned  s123  v1  metrics=YES
    mmlu: 0.6332
    gsm8k: 0.1812
    arc_challenge: 0.8328
    humaneval: 0.0854
  [exp_001_eval_3B_d000_v2_s123_aligned]  type=aligned  s123  v2  metrics=YES
    mmlu: 0.6314
    gsm8k: 0.2676
    arc_challenge: 0.8259
    humaneval: 0.061
  [exp_001_eval_3B_d000_s42_para_aligned]  type=para_aligned  s42  v1  metrics=YES
    mmlu: {"accuracy": 0.6474, "correct": 4270, "total": 6596}
    gsm8k: {"accuracy": 0.0482, "correct": 11, "total": 228}
    arc_challenge: {"accuracy": 0.8235, "correct": 574, "total": 697}
    humaneval: {"pass@1": 0.1154, "correct": 3, "total": 26}
  [exp_001_eval_3B_d000_v2_para_aligned]  type=para_aligned  s42  v2  metrics=YES
    mmlu_para: 0.6468
    format: paraphrased_aligned
  [exp_001_eval_3B_d000_v2_para_aligned_v2]  type=para_aligned  s42  v2  metrics=YES
    mmlu_para_accuracy: 0.6468
    gsm8k_para_accuracy: 0.2895
    arc_challenge_para_accuracy: 0.8121
    humaneval_para_pass@1: 0.0385
  [exp_001_eval_3B_d000_v2_para_aligned_v3]  type=para_aligned  s42  v2  metrics=NO
  [exp_001_eval_3B_d000_v2_s123_para_aligned]  type=para_aligned  s123  v2  metrics=YES
    mmlu_para_accuracy: 0.6512
    gsm8k_para_accuracy: 0.1491
    arc_challenge_para_accuracy: 0.8121
    humaneval_para_pass@1: 0.0385
  [exp_001_eval_3B_d000_s42]  type=standard  s42  v1  metrics=YES
    mmlu: 0.634
    gsm8k: 0.117
    arc: 0.822
    humaneval: 0.116
  [exp_001_eval_3B_d000_s42_v3]  type=standard  s42  v3  metrics=YES
    mmlu: 0.634
    gsm8k: 0.1198
    arc_challenge: 0.8276
    humaneval: 0.1159
  [exp_001_eval_3B_d000_s123]  type=standard  s123  v1  metrics=YES
    mmlu_accuracy: 0.6362
    gsm8k_exact_match: 0.1759
    arc_challenge_accuracy: 0.8294
    humaneval_pass_at_1: 0.0854

  --- Dose: 5% ---
  [exp_001_eval_3B_d005_aligned]  type=aligned  no_seed  v1  metrics=YES
    mmlu: 0.634
    gsm8k: 0.208
    arc_challenge: 0.829
    humaneval_pass_at_1: 0.146
  [exp_001_eval_3B_d005_s42_aligned]  type=aligned  s42  v1  metrics=YES
    mmlu: 0.6345
    gsm8k: 0.2077
    arc_challenge: 0.8294
    humaneval: 0.1463
  [exp_001_eval_3B_d005_s123_para_aligned]  type=para_aligned  s123  v1  metrics=YES
    MMLU: 0.6461
    GSM8K: 0.5
    ARC: 0.8192
    HumanEval: 0.0769

  --- Dose: 25% ---
  [exp_001_eval_3B_d025_v2_aligned]  type=aligned  s42  v2  metrics=YES
    mmlu: 0.5998
    gsm8k: 0.6793
    arc_challenge: 0.8276
    humaneval: 0.0976
  [exp_001_eval_3B_d025_s123_aligned]  type=aligned  s123  v1  metrics=YES
    mmlu: 0.6367
    gsm8k: 0.5254
    arc_challenge: 0.8336
    humaneval: 0.1585
  [exp_001_eval_3B_d025_v2_para_aligned]  type=para_aligned  s42  v2  metrics=YES
    mmlu_para_accuracy: 0.621
    gsm8k_para_accuracy: 0.5482
    arc_challenge_para_accuracy: 0.8106
    humaneval_para_pass@1: 0.1154
  [exp_001_eval_3B_d025_s123_para_aligned]  type=para_aligned  s123  v1  metrics=YES
    MMLU: 0.6615
    GSM8K: 0.4254
    ARC: 0.8121
    HumanEval: 0.1538

  --- Dose: 100% ---
  [exp_001_eval_3B_d100_aligned]  type=aligned  s42  v1  metrics=YES
    mmlu_accuracy: 0.6417
    gsm8k_exact_match: 0.6967
    arc_challenge_accuracy: 0.8396
    humaneval_pass1: 0.122
  [exp_001_eval_3B_d100_v2_aligned]  type=aligned  s42  v2  metrics=YES
    INVALID: metrics were from v1 exp_001_eval_3B_d100_aligned, not v2. v2 output dir was empty. PID 461879 died before completion.
  [exp_001_eval_3B_d100_v2_aligned_v2]  type=aligned  s42  v2  metrics=YES
    mmlu_accuracy: 0.632
    gsm8k_accuracy: 0.7415
    arc_challenge_accuracy: 0.8242
    humaneval_pass@1: 0.1707
  [exp_001_eval_3B_d100_v2_s123_aligned]  type=aligned  s123  v2  metrics=YES
    mmlu: 0.6319
    gsm8k: 0.7324
    arc_challenge: 0.8311
    humaneval: 0.1829
  [exp_001_eval_3B_d100_para_aligned]  type=para_aligned  no_seed  v1  metrics=YES
    mmlu: 0.676
    gsm8k: 0.614
    arc_challenge: 0.828
  [exp_001_eval_3B_d100_s42_para_aligned]  type=para_aligned  s42  v1  metrics=YES
    mmlu: {"accuracy": 0.659, "correct": 4347, "total": 6596}
    gsm8k: {"accuracy": 0.5833, "correct": 133, "total": 228}
    arc_challenge: {"accuracy": 0.8092, "correct": 564, "total": 697}
    humaneval: {"pass@1": 0.1154, "correct": 3, "total": 26}
  [exp_001_eval_3B_d100_v2_para_aligned]  type=para_aligned  s42  v2  metrics=YES
    mmlu_para: 0.659
    gsm8k_para: 0.5833
    arc_challenge_para: 0.8092
    humaneval_para_pass1: 0.1154

  --- Dose: N/A ---
  [exp_001_eval_3B_raw_gen]  type=raw  no_seed  v1  metrics=YES
    gsm8k: 0.605
    humaneval: 0.0

================================================================================
SCALE: unknown (2 experiments)
================================================================================

  --- Dose: N/A ---
  [exp_008_base_pretrained_eval]  type=standard  no_seed  v1  metrics=NO
  [exp_008_base_pretrained_eval_v2]  type=standard  s42  v2  metrics=YES
    mmlu: 0.2294
    gsm8k: 0.163
    arc_challenge: 0.2278
    humaneval: 0.0
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a50883e3-1fe6-4e92-8484-00682da7c449",
  "isSidechain": true,
  "promptId": "eec554ab-49eb-41f0-9151-4530891c32ce",
  "agentId": "aee0c4a84f025f3bb",
  "type": "user",
  "uuid": "80dff468-f854-4947-9478-54ba4fbfa807",
  "sourceToolAssistantUUID": "a50883e3-1fe6-4e92-8484-00682da7c449",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-15T18:26:58.623Z_

Now let me get a count summary and identify which experiments have valid metrics vs. not.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "80dff468-f854-4947-9478-54ba4fbfa807",
  "isSidechain": true,
  "agentId": "aee0c4a84f025f3bb",
  "requestId": "req_011Cb4prepBCYoLJKt2iVfwb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "17ed3fd9-1162-4694-a5c4-3d88fcd9046b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TufhVc7McDe4eUCnP3JX3o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8785,
      "cache_read_input_tokens": 37421,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8785,
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

_source line 26 · 2026-05-15T18:27:08.539Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01BEecouciRNn9JgA5Hm7Anq`</summary>

```json
{
  "command": "FILE=\"/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-13-projects-contamcal-irt-calibration/0e7bc130-13e2-45e1-ae79-20741112a4af/tool-results/mcp-agent-ml-research-read_registry-1778869532955.txt\"\ncat \"$FILE\" | jq -r '.result' | python3 -c \"\nimport json, sys\n\ndata = json.load(sys.stdin)\nexps = data['data']['experiments']\neval_exps = {k: v for k, v in exps.items() if 'eval' in k.lower()}\n\n# Count with metrics vs without\nwith_metrics = sum(1 for v in eval_exps.values() if v.get('metrics') and isinstance(v['metrics'], dict) and len(v['metrics']) > 0)\nwithout_metrics = sum(1 for v in eval_exps.values() if not v.get('metrics') or not isinstance(v.get('metrics'), dict) or len(v.get('metrics', {})) == 0)\ninvalid = sum(1 for v in eval_exps.values() if v.get('metrics') and isinstance(v['metrics'], dict) and 'INVALID' in str(v['metrics']))\n\nprint(f'Total eval experiments: {len(eval_exps)}')\nprint(f'With metrics: {with_metrics}')\nprint(f'Without metrics (null): {without_metrics}')\nprint(f'With INVALID markers: {invalid}')\nprint()\n\n# Statuses\nfrom collections import Counter\nstatuses = Counter(v['status'] for v in eval_exps.values())\nprint(f'Status distribution: {dict(statuses)}')\nprint()\n\n# Series breakdown\nseries = Counter()\nfor k in eval_exps:\n    if k.startswith('exp_001'): series['exp_001'] += 1\n    elif k.startswith('exp_008'): series['exp_008'] += 1\n    else: series['other'] += 1\nprint(f'Series: {dict(series)}')\n\"",
  "description": "Summary statistics of eval experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "17ed3fd9-1162-4694-a5c4-3d88fcd9046b",
  "isSidechain": true,
  "agentId": "aee0c4a84f025f3bb",
  "requestId": "req_011Cb4prepBCYoLJKt2iVfwb",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d9cc45d9-a9a3-4661-b74b-d6c7f1fd0229",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TufhVc7McDe4eUCnP3JX3o",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8785,
      "cache_read_input_tokens": 37421,
      "output_tokens": 615,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8785
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 615,
          "cache_read_input_tokens": 37421,
          "cache_creation_input_tokens": 8785,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8785,
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

_source line 27 · 2026-05-15T18:27:09.450Z_

<details><summary>↩ Tool result · `toolu_01BEecouciRNn9JgA5Hm7Anq`</summary>

```text
Total eval experiments: 69
With metrics: 60
Without metrics (null): 9
With INVALID markers: 1

Status distribution: {'DONE': 69}

Series: {'exp_001': 64, 'exp_008': 5}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d9cc45d9-a9a3-4661-b74b-d6c7f1fd0229",
  "isSidechain": true,
  "promptId": "eec554ab-49eb-41f0-9151-4530891c32ce",
  "agentId": "aee0c4a84f025f3bb",
  "type": "user",
  "uuid": "055d4934-b05b-4ec8-aeb2-423caff4cf06",
  "sourceToolAssistantUUID": "d9cc45d9-a9a3-4661-b74b-d6c7f1fd0229",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-15T18:28:17.107Z_

Here is the complete structured summary of all 69 eval experiments found in the registry.

---

## Overview

- **Total eval experiments**: 69 (all status = DONE)
- **With metrics**: 60
- **Without metrics (null)**: 9
- **With invalid/corrupt metrics**: 1 (`exp_001_eval_3B_d100_v2_aligned` -- PID died before completion)
- **Series**: exp_001 (64 experiments, main contamination calibration), exp_008 (5 experiments, base/instruct pretrained baselines)

---

## By Scale

### 0.5B (Qwen2.5-0.5B) -- 23 experiments

**Dose 0% (baseline)**
| exp_id | eval_type | seed | MMLU | GSM8K | ARC | HumanEval |
|--------|-----------|------|------|-------|-----|-----------|
| `exp_001_eval_05B_d000_s123_aligned` | aligned | 123 | 0.4216 | 0.3412 | 0.4974 | 0.1037 |
| `exp_001_eval_05B_d000_s42_v5` | standard | 42 | 0.4049 | 0.3647 | 0.3780 | 0.1098 |
| `exp_001_eval_05B_d000_s123` | standard | 123 | 0.4182 | 0.3404 | 0.3976 | 0.1037 |
| `exp_001_eval_05B_d000_s42` | standard | 42 | null | null | null | null |
| `exp_001_eval_05B_d000_s42_v7` | standard | 42 | null | null | null | null |

**Dose 5%**
| exp_id | eval_type | seed | MMLU | GSM8K | ARC | HumanEval |
|--------|-----------|------|------|-------|-----|-----------|
| `exp_001_eval_05B_d005_aligned` | aligned | 42 | 0.3255 | 0.3624 | 0.3285 | 0.0793 |
| `exp_001_eval_05B_d005_s123_aligned` | aligned | 123 | 0.3002 | 0.3677 | 0.2978 | 0.0976 |
| `exp_001_eval_05B_d005_para_aligned` | para_aligned | 42 | 0.3548 | 0.2588 | 0.3300 | 0.0000 |
| `exp_001_eval_05B_d005_s123_para_aligned` | para_aligned | 123 | 0.3166 | 0.2939 | 0.2912 | 0.0000 |
| `exp_001_eval_05B_d005` | standard | 42 | 0.2929 | 0.3601 | 0.2858 | 0.0793 |

**Dose 25%**
| exp_id | eval_type | seed | MMLU | GSM8K | ARC | HumanEval |
|--------|-----------|------|------|-------|-----|-----------|
| `exp_001_eval_05B_d025_aligned` | aligned | -- | 0.2803* | 0.3662* | 0.3251* | missing |
| `exp_001_eval_05B_d025_aligned_v2` | aligned | 42 | 0.2835 | 0.3114 | 0.3199 | 0.1923 |
| `exp_001_eval_05B_d025_s123_aligned` | aligned | 123 | 0.3473 | 0.3533 | 0.4061 | 0.0854 |

(*v1 metrics appear to be in percentage scale 28.03/36.62/32.51 rather than 0-1; v2 note says "paraphrased_aligned" in format field which may be mislabeled)

**Dose 100%**
| exp_id | eval_type | seed | MMLU | GSM8K | ARC | HumanEval |
|--------|-----------|------|------|-------|-----|-----------|
| `exp_001_eval_05B_d100_aligned_v4` | aligned | 42 | 0.2334 | 0.3654 | 0.2944 | 0.0000 |
| `exp_001_eval_05B_d100_s123_aligned` | aligned | 123 | 0.3058 | 0.3798 | 0.3669 | 0.1037 |
| `exp_001_eval_05B_d100_v5` | standard | 42 | 0.2322 | 0.3571 | 0.2270 | 0.0854 |
| `exp_001_eval_05B_d100_aligned` | aligned | 42 | null | null | null | null |
| `exp_001_eval_05B_d100_aligned_v3` | aligned | -- | null | null | null | null |
| `exp_001_eval_05B_d100` | standard | 42 | null | null | null | null |
| `exp_001_eval_05B_d100_v2` | standard | -- | null | null | null | null |

**Batch/special (0.5B)**
| exp_id | eval_type | seed | Description |
|--------|-----------|------|-------------|
| `exp_001_eval_05B_aligned_batch` | batch | 42 | Combined d000/d005 aligned + d000 para_aligned metrics in one entry |
| `exp_001_eval_05B_raw` | raw | 42 | Raw base model (no LoRA): MMLU=0.2302, GSM8K=0.1592, ARC=0.2261, HumanEval=incomplete |

**exp_008 baselines (0.5B)**
| exp_id | model | MMLU | GSM8K | ARC | HumanEval |
|--------|-------|------|-------|-----|-----------|
| `exp_008_base_pretrained_eval_v2` | Qwen2.5-0.5B (base) | 0.2294 | 0.1630 | 0.2278 | 0.0000 |
| `exp_008_instruct_05B_eval` | Qwen2.5-0.5B-Instruct | 0.2462 | 0.3882 | 0.2816 | 0.0000 |
| `exp_008_base_pretrained_eval` | Qwen2.5-0.5B (base) | null | null | null | null |

---

### 1.5B (Qwen2.5-1.5B) -- 17 experiments

**Dose 0%**
| exp_id | eval_type | seed | MMLU | GSM8K | ARC | HumanEval |
|--------|-----------|------|------|-------|-----|-----------|
| `exp_001_eval_15B_d000_s123_aligned` | aligned | 123 | 0.5855 | 0.6535 | 0.7577 | 0.1707 |
| `exp_001_eval_15B_d000_s42_v2` | standard | 42 | 0.5753 | 0.6368 | 0.7756 | 0.1280 |
| `exp_001_eval_15B_d000_s123` | standard | 123 | 0.5762 | 0.6331 | 0.7662 | 0.1707 |
| `exp_001_eval_15B_d000_s42` | standard | 42 | null | null | null | null |

**Dose 5%**
| exp_id | eval_type | seed | MMLU | GSM8K | ARC | HumanEval |
|--------|-----------|------|------|-------|-----|-----------|
| `exp_001_eval_15B_d005_aligned_v2` | aligned | 42 | 0.5852 | 0.6482 | 0.7688 | 0.2500 |
| `exp_001_eval_15B_d005_s123` | standard | 123 | 0.5869 | 0.6482 | 0.7568 | 0.2500 |
| `exp_001_eval_15B_d005_s123_v2` | standard | 123 | 0.5869 | 0.6482 | 0.7568 | 0.2500 |

**Dose 25%**
| exp_id | eval_type | seed | MMLU | GSM8K | ARC | HumanEval |
|--------|-----------|------|------|-------|-----|-----------|
| `exp_001_eval_15B_d025_aligned` | aligned | -- | 0.5902 | 0.6535 | 0.7688 | 0.2256 |
| `exp_001_eval_15B_d025_para_aligned` | para_aligned | -- | 0.6180 | 0.5390 | 0.7660 | 0.1540 |
| `exp_001_eval_15B_d025_s123` | standard | 123 | 0.5881 | 0.6550 | 0.7577 | 0.2500 |
| `exp_001_eval_15B_d025_s123_v2` | standard | 123 | 0.5881 | 0.6550 | 0.7577 | 0.2500 |

**Dose 100%**
| exp_id | eval_type | seed | MMLU | GSM8K | ARC | HumanEval |
|--------|-----------|------|------|-------|-----|-----------|
| `exp_001_eval_15B_d100_aligned` | aligned | 42 | 0.5933 | 0.6497 | 0.7688 | 0.3049 |
| `exp_001_eval_15B_d100_s123_aligned` | aligned | 123 | 0.5956 | 0.6444 | 0.7816 | 0.2805 |
| `exp_001_eval_15B_d100_s42` | standard | 42 | 0.5933 | 0.6497 | 0.7688 | 0.3049 |

**Batch/special (1.5B)**
| exp_id | Description |
|--------|-------------|
| `exp_001_eval_15B_aligned_batch` | Combined d000/d005/d100 x orig/para metrics. Key finding recorded: "MC benchmarks fail to detect contamination at 1.5B scale (<1pp). HumanEval shows strong dose-response (+17.69pp). Paraphrase gap does not cleanly separate contamination." |

**exp_008 baselines (1.5B)**
| exp_id | model | MMLU | GSM8K | ARC | HumanEval |
|--------|-------|------|-------|-----|-----------|
| `exp_008_base_pretrained_15B_eval_v2` | Qwen2.5-1.5B (base) | 0.2303 | 0.0053 | 0.2304 | 0.2317 |
| `exp_008_base_pretrained_15B_eval` | Qwen2.5-1.5B (base) | 0.2303 | 0.0053 | 0.2304 | 0.2317 |

---

### 3B (Qwen2.5-3B) -- 27 experiments

**Dose 0%**
| exp_id | eval_type | seed | MMLU | GSM8K | ARC | HumanEval |
|--------|-----------|------|------|-------|-----|-----------|
| `exp_001_eval_3B_d000_aligned` | aligned | -- | 0.6340 | 0.1198 | 0.8276 | 0.1159 |
| `exp_001_eval_3B_d000_v2_aligned` | aligned | 42 | 0.6295 | 0.3525 | 0.8183 | 0.0976 |
| `exp_001_eval_3B_d000_s123_aligned` | aligned | 123 | 0.6332 | 0.1812 | 0.8328 | 0.0854 |
| `exp_001_eval_3B_d000_v2_s123_aligned` | aligned | 123 | 0.6314 | 0.2676 | 0.8259 | 0.0610 |
| `exp_001_eval_3B_d000_s42_para_aligned` | para_aligned | 42 | 0.6474 | 0.0482 | 0.8235 | 0.1154 |
| `exp_001_eval_3B_d000_v2_para_aligned_v2` | para_aligned | 42 | 0.6468 | 0.2895 | 0.8121 | 0.0385 |
| `exp_001_eval_3B_d000_v2_s123_para_aligned` | para_aligned | 123 | 0.6512 | 0.1491 | 0.8121 | 0.0385 |
| `exp_001_eval_3B_d000_v2_para_aligned` | para_aligned | 42 | 0.6468 (mmlu only) | -- | -- | -- |
| `exp_001_eval_3B_d000_v2_para_aligned_v3` | para_aligned | 42 | null | null | null | null |
| `exp_001_eval_3B_d000_s42` | standard | 42 | 0.6340 | 0.1170 | 0.8220 | 0.1160 |
| `exp_001_eval_3B_d000_s42_v3` | standard | 42 | 0.6340 | 0.1198 | 0.8276 | 0.1159 |
| `exp_001_eval_3B_d000_s123` | standard | 123 | 0.6362 | 0.1759 | 0.8294 | 0.0854 |

**Dose 5%**
| exp_id | eval_type | seed | MMLU | GSM8K | ARC | HumanEval |
|--------|-----------|------|------|-------|-----|-----------|
| `exp_001_eval_3B_d005_aligned` | aligned | -- | 0.6340 | 0.2080 | 0.8290 | 0.1460 |
| `exp_001_eval_3B_d005_s42_aligned` | aligned | 42 | 0.6345 | 0.2077 | 0.8294 | 0.1463 |
| `exp_001_eval_3B_d005_s123_para_aligned` | para_aligned | 123 | 0.6461 | 0.5000 | 0.8192 | 0.0769 |

**Dose 25%**
| exp_id | eval_type | seed | MMLU | GSM8K | ARC | HumanEval |
|--------|-----------|------|------|-------|-----|-----------|
| `exp_001_eval_3B_d025_v2_aligned` | aligned | 42 | 0.5998 | 0.6793 | 0.8276 | 0.0976 |
| `exp_001_eval_3B_d025_s123_aligned` | aligned | 123 | 0.6367 | 0.5254 | 0.8336 | 0.1585 |
| `exp_001_eval_3B_d025_v2_para_aligned` | para_aligned | 42 | 0.6210 | 0.5482 | 0.8106 | 0.1154 |
| `exp_001_eval_3B_d025_s123_para_aligned` | para_aligned | 123 | 0.6615 | 0.4254 | 0.8121 | 0.1538 |

**Dose 100%**
| exp_id | eval_type | seed | MMLU | GSM8K | ARC | HumanEval |
|--------|-----------|------|------|-------|-----|-----------|
| `exp_001_eval_3B_d100_aligned` | aligned | 42 | 0.6417 | 0.6967 | 0.8396 | 0.1220 |
| `exp_001_eval_3B_d100_v2_aligned_v2` | aligned | 42 | 0.6320 | 0.7415 | 0.8242 | 0.1707 |
| `exp_001_eval_3B_d100_v2_s123_aligned` | aligned | 123 | 0.6319 | 0.7324 | 0.8311 | 0.1829 |
| `exp_001_eval_3B_d100_v2_aligned` | aligned | 42 | INVALID (PID died) | -- | -- | -- |
| `exp_001_eval_3B_d100_para_aligned` | para_aligned | -- | 0.6760 | 0.6140 | 0.8280 | -- |
| `exp_001_eval_3B_d100_s42_para_aligned` | para_aligned | 42 | 0.6590 | 0.5833 | 0.8092 | 0.1154 |
| `exp_001_eval_3B_d100_v2_para_aligned` | para_aligned | 42 | 0.6590 | 0.5833 | 0.8092 | 0.1154 |

**Special (3B)**
| exp_id | eval_type | seed | Description |
|--------|-----------|------|-------------|
| `exp_001_eval_3B_raw_gen` | raw | 0 | Raw base model gen: GSM8K=0.605, HumanEval=0.0 |

---

### Unknown scale (exp_008 baselines without scale in name)
| exp_id | model | MMLU | GSM8K | ARC | HumanEval |
|--------|-------|------|-------|-----|-----------|
| `exp_008_base_pretrained_eval_v2` | Qwen2.5-0.5B (base) | 0.2294 | 0.1630 | 0.2278 | 0.0000 |
| `exp_008_base_pretrained_eval` | Qwen2.5-0.5B (base) | null | null | null | null |

---

## Key Data Quality Notes

1. **9 experiments with null metrics**: `exp_001_eval_05B_d000_s42`, `exp_001_eval_05B_d000_s42_v7`, `exp_001_eval_05B_d100`, `exp_001_eval_05B_d100_v2`, `exp_001_eval_05B_d100_aligned`, `exp_001_eval_05B_d100_aligned_v3`, `exp_001_eval_15B_d000_s42`, `exp_001_eval_3B_d000_v2_para_aligned_v3`, `exp_008_base_pretrained_eval`

2. **1 INVALID entry**: `exp_001_eval_3B_d100_v2_aligned` -- metrics came from v1, v2 output dir was empty (PID 461879 died).

3. **Metric key inconsistency**: Some experiments use `mmlu`/`gsm8k`, others use `mmlu_accuracy`/`gsm8k_exact_match`, others use `MMLU`/`GSM8K`, and batch experiments use prefixed keys like `d000_aligned_mmlu`. Some report nested dicts with `{accuracy, correct, total}`.

4. **Multiple versions**: Many experiment conditions have v1/v2/v3+ reruns. The later versions typically supersede earlier ones (e.g., `_v2` fixing issues from `_v1`).

5. **exp_001_eval_05B_d025_aligned** metrics appear in percentage scale (28.03, 36.62, 32.51) rather than 0-1 scale.

6. **exp_001_eval_05B_d025_aligned_v2** has `format: paraphrased_aligned` in its metrics -- possibly mislabeled as "aligned" in the exp_id but actually para_aligned.

7. **3B GSM8K at dose 0% shows high variance**: ranges from 0.048 to 0.353 across different eval_types and versions, suggesting sensitivity to eval format.

8. **Batch experiments** (`exp_001_eval_15B_aligned_batch`, `exp_001_eval_05B_aligned_batch`) aggregate multiple dose x eval_type combinations into single entries and are the most reliable summaries for those scales.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "055d4934-b05b-4ec8-aeb2-423caff4cf06",
  "isSidechain": true,
  "agentId": "aee0c4a84f025f3bb",
  "requestId": "req_011Cb4psfPBiQMzvjH7yis6P",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "159a7f32-50bf-46e9-8439-5fbc3228fcea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration",
  "sessionId": "0e7bc130-13e2-45e1-ae79-20741112a4af",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fy1xDY3J7Latoz1vps9dsb",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 685,
      "cache_read_input_tokens": 46206,
      "output_tokens": 5479,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 685
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5479,
          "cache_read_input_tokens": 46206,
          "cache_creation_input_tokens": 685,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 685,
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
