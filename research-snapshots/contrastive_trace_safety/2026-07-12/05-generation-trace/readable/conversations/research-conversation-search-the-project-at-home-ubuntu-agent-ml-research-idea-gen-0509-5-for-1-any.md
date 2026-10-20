# Research conversation: Search the project at /home/ubuntu/.agent-ml-research-idea_gen_0509_5 for: 1. Any YAML/JSON files containing experiment 

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 61
- **Recorded user turns:** 1
- **Tool calls:** 23
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-aae11a3504772ac7f.jsonl`
- **Structured JSON:** [`923cd749d3aec273f841.json`](../../sessions/92/923cd749d3aec273f841.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

61 recorded events

### User

_source line 1 · 2026-05-16T15:06:24.235Z_

Search the project at /home/ubuntu/.agent-ml-research-idea_gen_0509_5 for:
1. Any YAML/JSON files containing experiment results or predictions (especially in artifacts/ directory)
2. Files related to "best" tier definition or tier definitions
3. Any existing imagined_experiments or predicted results files
4. The experiment_plan.yaml or similar planning files
5. Registry files with completed experiment metrics

Search breadth: very thorough. Report file paths and key content summaries.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "1589742a-41cc-4d40-ae94-dc9d919d6688",
  "agentId": "aae11a3504772ac7f",
  "type": "user",
  "uuid": "a991f069-2e6c-4fbd-a301-eda6ac2608bc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "c4036345-91c5-47f2-9c09-36d0f1b82314",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-16T15:06:25.529Z_

I'll conduct a thorough search of the project for experiment results, tier definitions, and related files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a991f069-2e6c-4fbd-a301-eda6ac2608bc",
  "isSidechain": true,
  "agentId": "aae11a3504772ac7f",
  "requestId": "req_011Cb6TNgKW5cA91bYjtZXXZ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "7cf87987-29d2-4120-8f8f-e662834897b1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "c4036345-91c5-47f2-9c09-36d0f1b82314",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01FJXcBdE7BSu4JR5mW5W6CM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16707,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16707,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 3 · 2026-05-16T15:06:25.851Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01678aSSgcZFgFM7QccqHrR8`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_5 -type f \\( -name \"*.yaml\" -o -name \"*.yml\" -o -name \"*.json\" \\) | head -50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7cf87987-29d2-4120-8f8f-e662834897b1",
  "isSidechain": true,
  "agentId": "aae11a3504772ac7f",
  "requestId": "req_011Cb6TNgKW5cA91bYjtZXXZ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "18f43d2b-b21f-4d49-9edb-266050144685",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "c4036345-91c5-47f2-9c09-36d0f1b82314",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01FJXcBdE7BSu4JR5mW5W6CM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16707,
      "cache_read_input_tokens": 0,
      "output_tokens": 127,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 16707
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 127,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 16707,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 16707,
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

_source line 4 · 2026-05-16T15:06:26.066Z_

<details><summary>↩ Tool result · `toolu_01678aSSgcZFgFM7QccqHrR8`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/idea_generator/logs/_index.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/idea_generator/ideas.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/global/logs/workers/registry.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/global/logs/weights_cache.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/global/approvals.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/dream_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_ops_dual-gpu-verify_20260513T090837_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_fix_plan017_review_fixes_20260514T092605_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_analysis_m2_full_qwen_20260514T112525_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_research_framing_analysis_20260513T184429_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_analysis_checkpoint-criterion-K_20260515T031356_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_setup_download_starcoder2_3b_20260512T235233_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_knowledge_update-roadmap-timeline_20260515T183237_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_ops_fix-m2-hf-offline-resubmit_20260513T015621_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_check_server-status-and-cleanup_20260515T041456_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_ops_m1-progress-check-v2_20260513T082755_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_code_d062_fix_eval_20260516T070422_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_ssh_eval2000_urgent_check_20260514T025319_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_write_introduction-v2_20260515T015804_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_analysis_bootstrap-result-pickup_20260515T145850_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_analysis_training-dynamics-prep_20260515T182816_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_fix_d041-method-drafts_20260515T020954_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_writing_experiments-quick-fixes-0515_20260515T140220_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_ops_verify-random-s44-training_20260515T103139_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_analysis_bootstrap-fix-and-rerun_20260515T150001_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_train_m2_full_qwen_20260513T162011_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_research_50repo_overlap_stats_20260512T195352_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_ops_urgent-prevent-gpu0-oom_20260515T155651_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_ops_bjb1-gpu-fix-v2_20260513T052414_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_ops_disk_emergency_assessment_20260513T013022_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_code_training_skeleton_20260512T100142_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_code_repobench_eval_script_20260516T051646_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_code_fix_repo_level_split_20260512T212539_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_code_pool_sensitivity_script_20260516T114426_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_code_dynamic_mining_impl_20260513T002931_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_fix_starcoder_padtoken_hyperparams_20260513T163817_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_research_swebench-eval-dependency-check_20260515T181546_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_eval_swebench-restart-100instances_20260515T184352_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_ops_verify-train-py-consistency_20260515T144312_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_ops_kill_moto_20260516T030940_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_monitor_m1_progress_check_20260513T013124_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_code_extraction_skeleton_20260512T100103_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_write_valloss-divergence-discussion_20260515T071736_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_ops_prepare-pool50-eval-pipeline_20260515T182136_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_ops_m1-progress-check-v3_20260513T103626_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_fix_repo-count-clarification_20260514T231412_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_check_training-status-loop9_20260515T010840_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_ops_bjb1-model-check-dryrun_20260513T032947_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_infra_p2b_gpu_check_restart_20260512T144458_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_fix_claim2-wording-critical_20260515T020243_result.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "18f43d2b-b21f-4d49-9edb-266050144685",
  "isSidechain": true,
  "promptId": "1589742a-41cc-4d40-ae94-dc9d919d6688",
  "agentId": "aae11a3504772ac7f",
  "type": "user",
  "uuid": "c69aa82f-d438-4daf-bfd4-dbd3fb6fbe32",
  "sourceToolAssistantUUID": "18f43d2b-b21f-4d49-9edb-266050144685",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "c4036345-91c5-47f2-9c09-36d0f1b82314",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-16T15:06:29.141Z_

Now let me look for directories and check artifacts specifically:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c69aa82f-d438-4daf-bfd4-dbd3fb6fbe32",
  "isSidechain": true,
  "agentId": "aae11a3504772ac7f",
  "requestId": "req_011Cb6TNpEzkToUKvjTCbGsd",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c756c1f7-adc0-4271-b6e1-a6e61b70e8dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "c4036345-91c5-47f2-9c09-36d0f1b82314",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016YYw8RcC6U8pxhnpkgvxKw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 20226,
      "output_tokens": 112,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 112,
          "cache_read_input_tokens": 20226,
          "cache_creation_input_tokens": 0,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
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

### Tool call

_source line 6 · 2026-05-16T15:06:29.153Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01BH4kzkFZj1fNW1SLbhZdNY`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_5 -type d -name \"artifacts\" -o -type d -name \"results\" -o -type d -name \"experiments\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c756c1f7-adc0-4271-b6e1-a6e61b70e8dd",
  "isSidechain": true,
  "agentId": "aae11a3504772ac7f",
  "requestId": "req_011Cb6TNpEzkToUKvjTCbGsd",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1457811c-7a77-4847-8010-f320e5b5e3e1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "c4036345-91c5-47f2-9c09-36d0f1b82314",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016YYw8RcC6U8pxhnpkgvxKw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 20226,
      "output_tokens": 112,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 112,
          "cache_read_input_tokens": 20226,
          "cache_creation_input_tokens": 0,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
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

_source line 7 · 2026-05-16T15:06:29.214Z_

<details><summary>↩ Tool result · `toolu_01BH4kzkFZj1fNW1SLbhZdNY`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/__setup__/docs/results
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/docs/results
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1457811c-7a77-4847-8010-f320e5b5e3e1",
  "isSidechain": true,
  "promptId": "1589742a-41cc-4d40-ae94-dc9d919d6688",
  "agentId": "aae11a3504772ac7f",
  "type": "user",
  "uuid": "80624c3e-d9ca-410f-a5db-b10373850b46",
  "sourceToolAssistantUUID": "1457811c-7a77-4847-8010-f320e5b5e3e1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "c4036345-91c5-47f2-9c09-36d0f1b82314",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 8 · 2026-05-16T15:06:30.407Z_

Excellent! Let me search in these key directories and also look for experiment-related files:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "80624c3e-d9ca-410f-a5db-b10373850b46",
  "isSidechain": true,
  "agentId": "aae11a3504772ac7f",
  "requestId": "req_011Cb6TP2tG3Mi9ZFS3Df4qq",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "77f1765d-2758-4681-8f35-205aab1a8c92",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "c4036345-91c5-47f2-9c09-36d0f1b82314",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HTEHrxrxjoTEsPY2AeP6zt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 3731,
      "cache_read_input_tokens": 16707,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3731,
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

_source line 9 · 2026-05-16T15:06:30.650Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01M4VC8egaEYZPo1z4usd7ZB`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts -type f | head -30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "77f1765d-2758-4681-8f35-205aab1a8c92",
  "isSidechain": true,
  "agentId": "aae11a3504772ac7f",
  "requestId": "req_011Cb6TP2tG3Mi9ZFS3Df4qq",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "793a1181-336b-45a4-a101-a9a26051ea69",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "c4036345-91c5-47f2-9c09-36d0f1b82314",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HTEHrxrxjoTEsPY2AeP6zt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 3731,
      "cache_read_input_tokens": 16707,
      "output_tokens": 108,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3731
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 108,
          "cache_read_input_tokens": 16707,
          "cache_creation_input_tokens": 3731,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3731,
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

_source line 10 · 2026-05-16T15:06:30.718Z_

<details><summary>↩ Tool result · `toolu_01M4VC8egaEYZPo1z4usd7ZB`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/plan_003/report/swebench_dryrun_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/plan_003/swebench_dryrun_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/mvp_p2b_contrastive_training/report/failure_diagnosis.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/plan006_error_patterns.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/method_v1_3cf111.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/figure_design_v1.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/introduction_v2.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/related_work_v1.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/experiments_v1_eccca0.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/method_v1_ce3556.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/method_v1_82f7f1.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/fixed_checkpoint_table.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/related_work_v1_5cf1f6.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/introduction_v1_c7f173.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/experimental_setup_k_checkpoint.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/experiments_v1_bcd130.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/methodology.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/introduction_v1.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/experiments_v1.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/abstract_v2.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/experiments_v1_054f8d.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/method_v1.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/experiment_setup_v1.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/experiments_v1_1b36e4.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/abstract_v2_e63490.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/conclusion_v1.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/related_work_v1_dc54a3.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/paper/discussion_v2.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "793a1181-336b-45a4-a101-a9a26051ea69",
  "isSidechain": true,
  "promptId": "1589742a-41cc-4d40-ae94-dc9d919d6688",
  "agentId": "aae11a3504772ac7f",
  "type": "user",
  "uuid": "8caaaa21-a467-44b8-9897-967b8e71d5c8",
  "sourceToolAssistantUUID": "793a1181-336b-45a4-a101-a9a26051ea69",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "c4036345-91c5-47f2-9c09-36d0f1b82314",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-16T15:06:32.166Z_

Let me search for experiment-related YAML/JSON files more systematically:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8caaaa21-a467-44b8-9897-967b8e71d5c8",
  "isSidechain": true,
  "agentId": "aae11a3504772ac7f",
  "requestId": "req_011Cb6TP9rhhJttMcVc6m4Ri",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c0abccc2-5b3f-4dfc-93b2-5f985ab9773b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "c4036345-91c5-47f2-9c09-36d0f1b82314",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01GxQp7fdCS1U4XGvxXGgNtH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 1426,
      "cache_read_input_tokens": 20438,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1426,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 12 · 2026-05-16T15:06:32.703Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01Efg2Dtmc1TFC2CRj2bMwE5`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_5 -type f \\( -name \"*experiment*\" -o -name \"*tier*\" -o -name \"*result*\" -o -name \"*registry*\" -o -name \"*plan*\" \\) \\( -name \"*.yaml\" -o -name \"*.yml\" -o -name \"*.json\" \\)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c0abccc2-5b3f-4dfc-93b2-5f985ab9773b",
  "isSidechain": true,
  "agentId": "aae11a3504772ac7f",
  "requestId": "req_011Cb6TP9rhhJttMcVc6m4Ri",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d58f2b8a-474e-41a4-af4e-43e7d51d9c01",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "c4036345-91c5-47f2-9c09-36d0f1b82314",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01GxQp7fdCS1U4XGvxXGgNtH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 1426,
      "cache_read_input_tokens": 20438,
      "output_tokens": 159,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1426
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 159,
          "cache_read_input_tokens": 20438,
          "cache_creation_input_tokens": 1426,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1426,
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

_source line 13 · 2026-05-16T15:06:32.772Z_

<details><summary>↩ Tool result · `toolu_01Efg2Dtmc1TFC2CRj2bMwE5`</summary>

```text
&lt;persisted-output>
Output too large (80.3KB). Full output saved to: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-5/c4036345-91c5-47f2-9c09-36d0f1b82314/tool-results/b0aqv66f3.txt

Preview (first 2KB):
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/global/logs/workers/registry.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/dream_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_ops_dual-gpu-verify_20260513T090837_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_fix_plan017_review_fixes_20260514T092605_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_analysis_m2_full_qwen_20260514T112525_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_research_framing_analysis_20260513T184429_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_analysis_checkpoint-criterion-K_20260515T031356_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_setup_download_starcoder2_3b_20260512T235233_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_knowledge_update-roadmap-timeline_20260515T183237_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_ops_fix-m2-hf-offline-resubmit_20260513T015621_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_check_server-status-and-cleanup_20260515T041456_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_ops_m1-progress-check-v2_20260513T082755_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_code_d062_fix_eval_20260516T070422_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/logs/workers/worker_ssh_eval2000_urgent_check_20260514T025319_result.json
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d58f2b8a-474e-41a4-af4e-43e7d51d9c01",
  "isSidechain": true,
  "promptId": "1589742a-41cc-4d40-ae94-dc9d919d6688",
  "agentId": "aae11a3504772ac7f",
  "type": "user",
  "uuid": "db44c58b-0824-4bfb-85d8-77814a845aba",
  "sourceToolAssistantUUID": "d58f2b8a-474e-41a4-af4e-43e7d51d9c01",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "c4036345-91c5-47f2-9c09-36d0f1b82314",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-16T15:06:34.135Z_

Let me read the full output and also check specific key files:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "db44c58b-0824-4bfb-85d8-77814a845aba",
  "isSidechain": true,
  "agentId": "aae11a3504772ac7f",
  "requestId": "req_011Cb6TPJ6Z4rssARwkH3WH1",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1efe5b02-92d9-48c3-993b-55ba64b38918",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "c4036345-91c5-47f2-9c09-36d0f1b82314",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WJE83YrQPQNYUwhyzGQEeq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1005,
      "cache_read_input_tokens": 21864,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1005,
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

_source line 15 · 2026-05-16T15:06:34.287Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01ENBN5n4vkxUHiYfebG1Pfg`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/ | grep -E \"experiment|tier|plan|registry|yaml|json\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1efe5b02-92d9-48c3-993b-55ba64b38918",
  "isSidechain": true,
  "agentId": "aae11a3504772ac7f",
  "requestId": "req_011Cb6TPJ6Z4rssARwkH3WH1",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "3231f5aa-38d4-401d-8426-eaa10badefb0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "c4036345-91c5-47f2-9c09-36d0f1b82314",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WJE83YrQPQNYUwhyzGQEeq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1005,
      "cache_read_input_tokens": 21864,
      "output_tokens": 113,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1005
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 113,
          "cache_read_input_tokens": 21864,
          "cache_creation_input_tokens": 1005,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1005,
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

_source line 16 · 2026-05-16T15:06:34.357Z_

<details><summary>↩ Tool result · `toolu_01ENBN5n4vkxUHiYfebG1Pfg`</summary>

```text
-rw-------  1 ubuntu ubuntu 65959 May 16 11:08 decisions.yaml
-rwxr-xr-x  1 ubuntu ubuntu     0 May 12 10:46 dream_registry.lock
-rw-------  1 ubuntu ubuntu  4633 May 16 15:03 dream_registry.yaml
-rw-r--r--  1 ubuntu ubuntu  4631 May 16 15:03 dream_registry.yaml.bak
-rw-r--r--  1 ubuntu ubuntu     0 May 12 12:58 experiment_plan.lock
-rw-------  1 ubuntu ubuntu  8489 May 16 06:39 experiment_plan.yaml
-rw-r--r--  1 ubuntu ubuntu 27433 May 16 00:47 literature_map.yaml
-rw-r--r--  1 ubuntu ubuntu     0 May 12 11:30 registry.lock
-rw-------  1 ubuntu ubuntu 69488 May 16 11:07 registry.yaml
-rw-r--r--  1 ubuntu ubuntu 13130 May 16 12:41 writing_plan.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3231f5aa-38d4-401d-8426-eaa10badefb0",
  "isSidechain": true,
  "promptId": "1589742a-41cc-4d40-ae94-dc9d919d6688",
  "agentId": "aae11a3504772ac7f",
  "type": "user",
  "uuid": "3ad04f00-f7cf-4fcd-b09a-442624b5595d",
  "sourceToolAssistantUUID": "3231f5aa-38d4-401d-8426-eaa10badefb0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "c4036345-91c5-47f2-9c09-36d0f1b82314",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-16T15:06:35.319Z_

Perfect! Now let me read the key files:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3ad04f00-f7cf-4fcd-b09a-442624b5595d",
  "isSidechain": true,
  "agentId": "aae11a3504772ac7f",
  "requestId": "req_011Cb6TPQsbNNg4GpaX2NPVb",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1607db79-cfb7-46e1-8259-58bb49a8b288",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "c4036345-91c5-47f2-9c09-36d0f1b82314",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WqGLbQnTsrnAtjQ78AoC7u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 517,
      "cache_read_input_tokens": 22869,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 517,
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

_source line 18 · 2026-05-16T15:06:35.756Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KZwjRMd5BbCjw4ZaqaXeiZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/experiment_plan.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1607db79-cfb7-46e1-8259-58bb49a8b288",
  "isSidechain": true,
  "agentId": "aae11a3504772ac7f",
  "requestId": "req_011Cb6TPQsbNNg4GpaX2NPVb",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c2da94e8-f086-4ad8-8820-b54297dcb194",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "c4036345-91c5-47f2-9c09-36d0f1b82314",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WqGLbQnTsrnAtjQ78AoC7u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 517,
      "cache_read_input_tokens": 22869,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 517,
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

_source line 19 · 2026-05-16T15:06:35.772Z_

<details><summary>↩ Tool result · `toolu_01KZwjRMd5BbCjw4ZaqaXeiZ`</summary>

```text
1	experiments:
2	- id: plan_001
3	  claim: 1
4	  description: 'M1 全量 CodeQL 提取: 5K SWE-smith repos data-flow extraction + connected
5	    vs gold statistics'
6	  priority: P0
7	  gpu_budget_hours: 0
8	  deps: []
9	  registry_id: m1_extraction
10	  mvp_registry_id: mvp_p1_codeql_feasibility
11	- id: plan_002
12	  claim: 1
13	  description: 'M2 全量 3-strategy 对比训练: random vs embedding_distance vs dataflow_aware,
14	    3 seeds each, Qwen2.5-Coder-3B LoRA'
15	  priority: P0
16	  gpu_budget_hours: 200
17	  deps:
18	  - plan_001
19	  registry_id: m2_embed_verify
20	  mvp_registry_id: mvp_p2b_contrastive_training
21	  full_registry_ids: ["m2_full_qwen", "m2_full_starcoder"]
22	- id: plan_003
23	  claim: 1
24	  description: 'M3a SWE-bench Lite (300) end-to-end evaluation: 3 strategies x best
25	    checkpoint, Qwen3.6-27B agent'
26	  priority: P0
27	  gpu_budget_hours: 40
28	  deps:
29	  - plan_002
30	  notes: 'eval script ready (eval_swebench.py), dry-run passed, 12 SWE-bench repos
31	    pre-cloned to /root/autodl-tmp/structfuse/swebench_repos. Awaiting M2 checkpoint.'
32	- id: plan_004
33	  claim: 1
34	  description: 'M3b RepoBench-R cross-file retrieval evaluation: retrieval-only, no
35	    LLM agent'
36	  priority: P1
37	  gpu_budget_hours: 15
38	  deps:
39	  - plan_002
40	  notes: 'eval script ready (eval_repobench.py), dry-run passed. RepoBench-R data via
41	    hf_hub_download. test_easy 8K instances (pool ~6), test_hard 8K (pool ~18). Awaiting
42	    M2 checkpoint. [Dream fix] Must run with multiple seeds and report 95% CIs —
43	    dream reviewers flagged inconsistent statistical reporting (CIs on SWE-bench but
44	    not RepoBench-R) across all 3 tiers.'
45	- id: plan_005
46	  claim: 2
47	  description: 'Embedding vs random 深度分析: 按 repo size/complexity 分层, 分析 embedding
48	    negatives 何时最有害'
49	  priority: P1
50	  gpu_budget_hours: 5
51	  deps:
52	  - plan_002
53	  notes: 'analysis script ready (analyze_stratified.py), dry-run passed. 3 strata:
54	    repo size / pool size / query-positive similarity. Outputs stratified_results.json
55	    + plots PDF. Awaiting M2 checkpoints for re-eval. [Dream fix] Must add 2 more
56	    strata: (a) structural data availability (34% with dataflow vs 66% fallback) per
57	    [B][M][W] all tiers, (b) neg_difficulty quartile analysis per [W] tier. Total 5
58	    strata.'
59	- id: plan_006
60	  claim: 3
61	  description: 'M1 scalability statistics: timeout rate, extraction time, coverage,
62	    connected-but-not-gold ratio by repo size'
63	  priority: P0
64	  gpu_budget_hours: 0
65	  deps:
66	  - plan_001
67	  registry_id: plan_006_scalability
68	- id: plan_007
69	  claim: 1
70	  description: 'Ablation: 1-hop vs 2-hop vs 3-hop call-graph bounding'
71	  priority: P1
72	  gpu_budget_hours: 20
73	  deps:
74	  - plan_001
75	- id: plan_008
76	  claim: 1
77	  description: 'Ablation: training data size scaling (1K vs 3K vs 5K instances)'
78	  priority: P1
79	  gpu_budget_hours: 15
80	  deps:
81	  - plan_001
82	- id: plan_009
83	  claim: 1
84	  description: 'Ablation: fusion head (embedding-only vs structural-features-only
85	    vs combined)'
86	  priority: P1
87	  gpu_budget_hours: 10
88	  deps:
89	  - plan_002
90	- id: plan_010
91	  claim: 1
92	  description: 'Ablation: dataflow-distance weighted negatives vs binary connected/disconnected'
93	  priority: P2
94	  gpu_budget_hours: 10
95	  deps:
96	  - plan_001
97	- id: plan_011
98	  claim: 1
99	  description: 'Failure analysis: 50 SweRank/BM25 failures, categorize by whether
100	    data-flow helps'
101	  priority: P1
102	  gpu_budget_hours: 5
103	  deps:
104	  - plan_003
105	- id: plan_012
106	  claim: 1
107	  description: 'Qualitative examples: 5-10 cases where structural negatives changed
108	    retrieval outcome'
109	  priority: P2
110	  gpu_budget_hours: 0
111	  deps:
112	  - plan_003
113	- id: plan_013
114	  claim: 1
115	  description: 'Second encoder validation: repeat M2 core comparison (3 strategies,
116	    1 seed) on StarCoder-3B or CodeBERT to test architecture generality'
117	  priority: P0
118	  gpu_budget_hours: 15
119	  deps:
120	  - plan_001
121	  dream_source: 'best-R1-W1, median-R2-W5: single encoder is primary generality concern.
122	    Upgraded to P0 per Reviewer — this is the #1 factor separating WA from WR.'
123	  registry_id: plan_013_starcoder
124	  full_registry_id: "m2_full_starcoder"
125	- id: plan_014
126	  claim: 2
127	  description: 'Temperature ablation: τ ∈ {0.05, 0.1, 0.2} for all 3 strategies, test
128	    regime-specificity of embedding harm'
129	  priority: P1
130	  gpu_budget_hours: 70
131	  deps:
132	  - plan_002
133	  dream_source: 'median-R1-W3: τ=0.05 unusually low, finding may be regime-specific'
134	- id: plan_015
135	  claim: 2
136	  description: 'Dynamic embedding mining baseline: re-mine embedding negatives per
137	    epoch vs static (mine once from pretrained). Isolate selection criterion from
138	    curriculum shift.'
139	  priority: P1
140	  gpu_budget_hours: 10
141	  deps:
142	  - plan_002
143	  dream_source: 'best-R1-W2, median-R1-W2: static vs dynamic mining is potential confound
144	    for Claim 2'
145	- id: plan_016
146	  claim: 1
147	  description: 'Bootstrap CI for SWE-bench Lite: add 95% bootstrap confidence intervals
148	    to end-to-end resolve rate evaluation'
149	  priority: P0
150	  gpu_budget_hours: 0
151	  deps:
152	  - plan_003
153	  dream_source: 'best-R1-W3, worst-R1-W5: +2.0pp on 300 instances needs statistical
154	    significance test'
155	- id: plan_017
156	  claim: 1
157	  description: 'Inference-time graph method comparison: discuss/compare with CodexGraph,
158	    LocAgent — is StructFuse complementary or alternative? Analysis complete, document
159	    in artifacts/analysis/plan017_literature_comparison.md. Discussion draft in
160	    artifacts/paper_drafts/discussion_draft.md.'
161	  priority: P1
162	  gpu_budget_hours: 0
163	  deps:
164	  - plan_002
165	  registry_id: plan_017_literature
166	  dream_source: 'best-R2-W5: no comparison with inference-time graph methods'
167	  notes: 'DONE (analysis only, no experiment). 8 papers surveyed (CodexGraph, LocAgent,
168	    RANGER, GraphCoder, ARISE, RepoGraph, CodeGRAG, CodeRAG). All citations verified.
169	    Conclusion: training-time vs inference-time are complementary, not competing.'
170	- id: plan_018
171	  claim: 1
172	  description: 'BM25 negative baseline: mine BM25-based hard negatives as 4th strategy,
173	    train ≥1 seed × 2 encoders, compare R@1 with random/embedding/dataflow. Empirically
174	    verify CoCoHaNeRe BM25-proxy caused the reported harm.'
175	  priority: P0
176	  gpu_budget_hours: 15
177	  deps:
178	  - plan_001
179	  dream_source: 'dream_20260514T075732 [B][M][W]: all 3 tiers identify missing BM25
180	    baseline as #1 structural gap. CoCoHaNeRe correction claim requires empirical
181	    verification — without it the paper motivation is asserted but unverified.'
182	  notes: 'Phase 1 (CPU, can start now): build BM25 index over training corpus, mine
183	    top-k BM25 negatives per query using same protocol as other strategies, produce
184	    bm25_training_data.jsonl. Phase 2 (GPU, after M2 frees up): train 1 seed × 2
185	    encoders with BM25 negatives (~7.5h each). 3 seeds preferred if GPU budget allows.
186	    Expected result: BM25 negatives harm → confirms CoCoHaNeRe artifact → closes argument.'
187	- id: plan_019
188	  claim: 1
189	  description: 'Pool size sensitivity analysis: test strategy ranking stability at
190	    pool={50, 100, 200, 500} candidates per query on SWE-smith validation.'
191	  priority: P1
192	  gpu_budget_hours: 5
193	  deps:
194	  - plan_002
195	  dream_source: 'dream_20260514T075732 [B][M][W]: all 3 tiers flag pool=50 as
196	    unrealistically small. Strategy differences may not preserve at realistic pool sizes.'
197	  notes: 'Requires M2 best checkpoints. Re-evaluate on expanded candidate pools.
198	    If strategy ranking changes at pool>200, must discuss in paper.'
199	- id: plan_020
200	  claim: 1
201	  description: 'UniXcoder multi-seed validation: repeat 3-strategy comparison with seeds
202	    43, 44 on UniXcoder-base (encoder-only, 125M). Statistical validation of cross-architecture
203	    generalization beyond single seed.'
204	  priority: P1
205	  gpu_budget_hours: 6
206	  deps:
207	  - plan_002
208	  notes: 'Depends on UniXcoder s42 completing successfully. UniXcoder 125M trains very
209	    fast: 3 strategies serial takes ~2-3h total (confirmed by s42 run). s43+s44 = 2 runs
210	    × ~3h = ~6h. If time-constrained, at minimum run random+embedding s43 for paired
211	    comparison.'
212	- id: plan_021
213	  claim: 2
214	  description: 'Temperature ablation reduced: τ ∈ {0.05, 0.2} × random+embedding ×
215	    Qwen × seed 42. Verify whether embedding mining advantage/harm is regime-specific.'
216	  priority: P1
217	  gpu_budget_hours: 15
218	  deps:
219	  - plan_002
220	  notes: 'Reduced scope of plan_014 (70h full → 15h minimum). If τ=0.05 shows different
221	    strategy ranking than τ=0.1 (current), confirms regime-specificity claim for Claim 2.
222	    Run after main training chains complete. Can expand to StarCoder if time allows.'
223	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c2da94e8-f086-4ad8-8820-b54297dcb194",
  "isSidechain": true,
  "promptId": "1589742a-41cc-4d40-ae94-dc9d919d6688",
  "agentId": "aae11a3504772ac7f",
  "type": "user",
  "uuid": "d78944aa-441d-4adc-8661-4ca5ce91f758",
  "sourceToolAssistantUUID": "c2da94e8-f086-4ad8-8820-b54297dcb194",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "c4036345-91c5-47f2-9c09-36d0f1b82314",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-16T15:06:35.961Z_

<details open><summary>🔧 Tool call — Read · `toolu_014yi5t3MXbHrom4YuJiRGs5`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/dream_registry.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d78944aa-441d-4adc-8661-4ca5ce91f758",
  "isSidechain": true,
  "agentId": "aae11a3504772ac7f",
  "requestId": "req_011Cb6TPQsbNNg4GpaX2NPVb",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "56736c26-60dd-44d1-bbf4-d27051bd0a93",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "c4036345-91c5-47f2-9c09-36d0f1b82314",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WqGLbQnTsrnAtjQ78AoC7u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 517,
      "cache_read_input_tokens": 22869,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 517,
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

_source line 21 · 2026-05-16T15:06:35.967Z_

<details><summary>↩ Tool result · `toolu_014yi5t3MXbHrom4YuJiRGs5`</summary>

```text
1	dreams:
2	  dream_20260512T204322:
3	    dream_id: dream_20260512T204322
4	    project: structfuse-context
5	    status: done
6	    review_mode: full
7	    review_visible: true
8	    writing_visible: true
9	    venue: ''
10	    focus: 'Key risk: dataflow negatives showed connected⊆gold at MVP scale (8 repos)
11	      but Z=40.8% at 50-repo scale. Full-scale training may reveal the effect is weaker
12	      than hypothesized. Also: embedding-distance negatives actively harm (-3.7pp
13	      R@1), which is a strong negative result supporting the dual-pillar motivation.
14	      Reviewers should stress-test whether the connected≠gold signal at scale (40.8%)
15	      is sufficient to produce meaningful training differentiation, and whether the
16	      improvement magnitude will be large enough for EMNLP acceptance.'
17	    what_if: []
18	    pid: 187100
19	    chat_id: oc_651ef5630fe7a61a1decb410adb7641b
20	    card_message_id: om_x100b6f0d4078a4a0c299b095297aa13
21	    started_at: '2026-05-12T20:43:22+00:00'
22	    updated_at: '2026-05-12T21:26:25+00:00'
23	    stages_completed:
24	    - imagine
25	    - write
26	    - review
27	    error: null
28	    context_hash: 30426df0367dd3f6d0c726d400e1e19f63bb74a6bb0cb4a99e17dd74384322a7
29	  dream_20260514T075732:
30	    dream_id: dream_20260514T075732
31	    project: structfuse-context
32	    status: done
33	    review_mode: full
34	    review_visible: true
35	    writing_visible: true
36	    venue: ''
37	    focus: D024 重写后的新 framing：论文从 "method paper (dataflow > all)" 转为 "systematic analysis
38	      + mechanistic insight"。三条新 claim：(1) 真正的 embedding mining 普遍有效，纠正 CoCoHaNeRe
39	      BM25-proxy 误解；(2) dataflow mining 有条件额外有效，机制是表征空间饱和度；(3) CodeQL 可扩展。已有实证：Qwen
40	      R@1=55.3%, StarCoder R@1=45.4%, neg_difficulty margin +17%/+28%, 两编码器 step 1000
41	      过拟合。Reviewers 应重点评估：新叙事线说服力、"conditional benefit" 是否被视为 weak claim、n=2 编码器统计限制、缺
42	      SWE-bench 下游验证的影响。
43	    what_if: []
44	    pid: 417207
45	    chat_id: oc_651ef5630fe7a61a1decb410adb7641b
46	    card_message_id: om_x100b6f6c4826f894c32f5ecb73ffa41
47	    started_at: '2026-05-14T07:57:32+00:00'
48	    updated_at: '2026-05-14T08:44:58+00:00'
49	    stages_completed:
50	    - imagine
51	    - write
52	    - review
53	    error: null
54	    context_hash: f1a2b822e6f7d3c566f1d46a50b3ef369d5b47191aa3a49407a522d7aa460a4b
55	  dream_20260514T162530:
56	    dream_id: dream_20260514T162530
57	    project: structfuse-context
58	    status: done
59	    review_mode: full
60	    review_visible: true
61	    writing_visible: true
62	    venue: ''
63	    focus: D030 修复后验证：新增 plan_018 BM25 baseline（关闭 CoCoHaNeRe correction 论证）、plan_019
64	      pool size sensitivity、plan_004 多 seed CIs、plan_005 structural coverage 分层 +
65	      neg_difficulty quartile。Framing 修正：N=2 降级为 observation、Claim 3 降为 supporting
66	      methodology、StarCoder decoder-only。Reviewers 应重点评估：(1) BM25 baseline 是否关闭了上一轮最大缺口，(2)
67	      新增实验是否充分回应了上一轮 median/worst 的 "related work insufficient" 和 "effect size marginal"
68	      问题，(3) 修正后的 N=2 observation framing 是否足够。
69	    what_if: []
70	    pid: 467068
71	    chat_id: oc_651ef5630fe7a61a1decb410adb7641b
72	    card_message_id: om_x100b6f6b397e9ca0c3540c94f58b23e
73	    started_at: '2026-05-14T16:25:30+00:00'
74	    updated_at: '2026-05-14T17:20:28+00:00'
75	    stages_completed:
76	    - imagine
77	    - write
78	    - review
79	    error: null
80	    context_hash: e45b45814bca7da7a44043a601b121d068ed1e070175933e083b6433ed6e0ccf
81	  dream_20260516T150348:
82	    dream_id: dream_20260516T150348
83	    project: structfuse-context
84	    status: imagining
85	    review_mode: full
86	    review_visible: true
87	    writing_visible: true
88	    venue: ''
89	    focus: '重点关注：(1) D062 checkpoint selection criterion effect (+16.3pp) 作为核心方法论贡献的说服力；(2)
90	      当前双版本 framing (A: criterion dominates vs B: mining + methodology) 哪个更强；(3) UniXcoder
91	      null result 作为 architecture-scale boundary condition 的呈现方式；(4) 3 seeds 统计力度是否足够；(5)
92	      缺少 SWE-bench downstream eval（OOD failure R@1=0.04）的影响'
93	    what_if: []
94	    pid: 790644
95	    chat_id: oc_651ef5630fe7a61a1decb410adb7641b
96	    card_message_id: om_x100b6fbc3bbcecacc333b2a36a2b69d
97	    started_at: '2026-05-16T15:03:48+00:00'
98	    updated_at: '2026-05-16T15:03:55+00:00'
99	    stages_completed: []
100	    error: null
101	    context_hash: 9e5c35c91c4c5ff4754faebfb4151dc31d1afd9e7d8567a02833317f65269c8b
102	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "56736c26-60dd-44d1-bbf4-d27051bd0a93",
  "isSidechain": true,
  "promptId": "1589742a-41cc-4d40-ae94-dc9d919d6688",
  "agentId": "aae11a3504772ac7f",
  "type": "user",
  "uuid": "24c88141-102c-4375-b2a0-c792b311bc40",
  "sourceToolAssistantUUID": "56736c26-60dd-44d1-bbf4-d27051bd0a93",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "c4036345-91c5-47f2-9c09-36d0f1b82314",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-16T15:06:36.070Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01MdGht6vbjYjWpRbnotMxDi`</summary>

```json
{
  "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/registry.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "24c88141-102c-4375-b2a0-c792b311bc40",
  "isSidechain": true,
  "agentId": "aae11a3504772ac7f",
  "requestId": "req_011Cb6TPQsbNNg4GpaX2NPVb",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "70fe34ca-bebc-4051-937c-dfb5bf7f8189",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "c4036345-91c5-47f2-9c09-36d0f1b82314",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WqGLbQnTsrnAtjQ78AoC7u",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 517,
      "cache_read_input_tokens": 22869,
      "output_tokens": 233,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 517
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4,
          "output_tokens": 233,
          "cache_read_input_tokens": 22869,
          "cache_creation_input_tokens": 517,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 517,
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

_source line 23 · 2026-05-16T15:06:36.122Z_

<details><summary>↩ Tool result · `toolu_01MdGht6vbjYjWpRbnotMxDi`</summary>

```text
1808 /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/registry.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "70fe34ca-bebc-4051-937c-dfb5bf7f8189",
  "isSidechain": true,
  "promptId": "1589742a-41cc-4d40-ae94-dc9d919d6688",
  "agentId": "aae11a3504772ac7f",
  "type": "user",
  "uuid": "aebe5f3d-5626-46d9-90fe-789efe115cf7",
  "sourceToolAssistantUUID": "70fe34ca-bebc-4051-937c-dfb5bf7f8189",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "c4036345-91c5-47f2-9c09-36d0f1b82314",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-16T15:06:38.046Z_

Let me now read the registry file which is large, and search for tier definitions:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aebe5f3d-5626-46d9-90fe-789efe115cf7",
  "isSidechain": true,
  "agentId": "aae11a3504772ac7f",
  "requestId": "req_011Cb6TPYbgRzzZQViQv3XTF",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "3143beb1-b8be-4934-9585-a78087f30503",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "c4036345-91c5-47f2-9c09-36d0f1b82314",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HTKayRsXtEQzfVVZ9XMfba",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 10703,
      "cache_read_input_tokens": 23386,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10703,
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

_source line 25 · 2026-05-16T15:06:38.715Z_

<details open><summary>🔧 Tool call — Read · `toolu_015stKL5ZaP8wULgxJg4zoaN`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/registry.yaml",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3143beb1-b8be-4934-9585-a78087f30503",
  "isSidechain": true,
  "agentId": "aae11a3504772ac7f",
  "requestId": "req_011Cb6TPYbgRzzZQViQv3XTF",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b7869f56-0477-4b60-b7ba-c7ee0e20339f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "c4036345-91c5-47f2-9c09-36d0f1b82314",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HTKayRsXtEQzfVVZ9XMfba",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 10703,
      "cache_read_input_tokens": 23386,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10703,
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

### Tool result

_source line 26 · 2026-05-16T15:06:38.731Z_

<details><summary>↩ Tool result · `toolu_015stKL5ZaP8wULgxJg4zoaN`</summary>

```text
1	baseline: null
2	experiments:
3	  mvp_p1_codeql_feasibility:
4	    status: DONE
5	    retry_count: 0
6	    created_at: '2026-05-12T11:30:45.938Z'
7	    updated_at: '2026-05-12T11:58:06.197Z'
8	    spec:
9	      command: python extraction/extract_dataflow.py + codeql query run (call_graph.ql
10	        + bounded_dataflow.ql)
11	      server: cqa1-21977
12	      data_path: '/root/structfuse/mvp_data/repos (8 SWE-smith instances: flask, requests,
13	        pytest, pylint, xarray, astropy, sphinx, matplotlib)'
14	      data_count: 8
15	      model_name: N/A (CPU pipeline)
16	      seed: null
17	      hypothesis: 'H1: CodeQL 2-hop bounded data-flow timeout <30%; H2: connected
18	        files gold patch coverage significantly > disconnected'
19	      plan_id: mvp_p1_codeql_feasibility
20	    conclusion: success
21	    metrics:
22	      timeout_rate: 0
23	      repos_processed: 8
24	      repos_skipped: 2
25	      cg_mean_s: 29.6
26	      cg_max_s: 119.8
27	      df_mean_s: 43.4
28	      df_max_s: 167.1
29	      h2_connected_coverage: 0.014815
30	      h2_disconnected_coverage: 0
31	      h2_fisher_p: 6.5e-09
32	      h2_gold_in_connected_ratio: 1
33	      h2_note: 'After path normalization fix: 8/8 gold in connected (was 6/8)'
34	    log_path: /root/autodl-tmp/mvp_results/mvp_phase1_report.json
35	    checkpoint_path: N/A (CPU pipeline, no model checkpoint)
36	    completed_at: '2026-05-12T11:31:16.335Z'
37	  mvp_p2a_linear_proxy:
38	    status: DONE
39	    retry_count: 0
40	    created_at: '2026-05-12T11:53:42.223Z'
41	    updated_at: '2026-05-12T11:58:15.436Z'
42	    spec:
43	      command: python evaluation/linear_proxy.py (logistic regression on data-flow
44	        features + BM25)
45	      server: cqa1-21977
46	      data_path: /root/autodl-tmp/mvp_results/ + /root/structfuse/mvp_data/bm25/
47	      data_count: 8
48	      model_name: LogisticRegression (scikit-learn)
49	      seed: null
50	      hypothesis: 'H2-confirm: data-flow features 的线性分类器预测 bug-relevant 文件优于纯 BM25
51	        baseline'
52	      plan_id: mvp_p2a_linear_proxy
53	    conclusion: success
54	    metrics:
55	      df_bm25_auc: 0.78
56	      bm25_only_auc: 0.476
57	      auc_delta: 0.304
58	      df_bm25_mrr: 0.556
59	      bm25_only_mrr: 0.115
60	      mrr_delta: 0.441
61	      df_bm25_f1: 0.143
62	      bm25_only_f1: 0.039
63	      top_feature: is_connected (+2.82)
64	      repos_evaluated: 3
65	      note: 3 repos / 3 positive samples, directional evidence
66	    checkpoint_path: N/A (logistic regression, no checkpoint)
67	    log_path: /root/structfuse/evaluation/linear_proxy.py output
68	    completed_at: '2026-05-12T11:58:15.436Z'
69	  p2b-smoke-test:
70	    status: DONE
71	    retry_count: 0
72	    created_at: '2026-05-12T12:14:30.477Z'
73	    updated_at: '2026-05-12T15:05:41.269Z'
74	    spec:
75	      command: obsolete smoke test
76	      server: cqa1-21977
77	      gpu:
78	      - cuda:4
79	      pid: '84805'
80	      log_path: N/A
81	      submitted_at: '2026-05-12T12:14:30.472Z'
82	      submitted_via: submit_training_job
83	      backend: tmux
84	      account: root
85	      data_path: N/A
86	      data_count: 0
87	      model_name: N/A
88	      seed: 42
89	      checkpoint_path: N/A
90	      wall_clock_seconds: 10270.8
91	      gpu_hours: 2.85
92	    conclusion: killed
93	    completed_at: '2026-05-12T15:05:41.270Z'
94	  p2b-smoke2:
95	    status: DONE
96	    retry_count: 0
97	    created_at: '2026-05-12T12:16:08.154Z'
98	    updated_at: '2026-05-12T15:05:42.174Z'
99	    spec:
100	      command: obsolete smoke test
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b7869f56-0477-4b60-b7ba-c7ee0e20339f",
  "isSidechain": true,
  "promptId": "1589742a-41cc-4d40-ae94-dc9d919d6688",
  "agentId": "aae11a3504772ac7f",
  "type": "user",
  "uuid": "47807aad-fbed-46b0-baac-23d6d289da4b",
  "sourceToolAssistantUUID": "b7869f56-0477-4b60-b7ba-c7ee0e20339f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "c4036345-91c5-47f2-9c09-36d0f1b82314",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-16T15:06:39.391Z_

<details open><summary>🔧 Tool call — Grep · `toolu_014geYksH2uFp51ZMXzPr8w4`</summary>

```json
{
  "pattern": "tier|best|worst|median",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context",
  "type": "yaml",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "47807aad-fbed-46b0-baac-23d6d289da4b",
  "isSidechain": true,
  "agentId": "aae11a3504772ac7f",
  "requestId": "req_011Cb6TPYbgRzzZQViQv3XTF",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "5b54dfc1-f776-4e4b-b638-7cbce71fea23",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "c4036345-91c5-47f2-9c09-36d0f1b82314",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HTKayRsXtEQzfVVZ9XMfba",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 10703,
      "cache_read_input_tokens": 23386,
      "output_tokens": 242,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 10703
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 242,
          "cache_read_input_tokens": 23386,
          "cache_creation_input_tokens": 10703,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 10703,
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

_source line 28 · 2026-05-16T15:06:39.419Z_

<details><summary>↩ Tool result · `toolu_014geYksH2uFp51ZMXzPr8w4`</summary>

```text
Found 24 files
projects/structfuse-context/dream_registry.yaml
projects/structfuse-context/artifacts/manifest.yaml
projects/structfuse-context/writing_plan.yaml
projects/structfuse-context/decisions.yaml
projects/structfuse-context/registry.yaml
projects/structfuse-context/experiment_plan.yaml
projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/meta.yaml
projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/worst/review_context.yaml
projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/median/review_context.yaml
projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/best/review_context.yaml
projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/worst/imagined_experiments.yaml
projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/median/imagined_experiments.yaml
projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/best/imagined_experiments.yaml
projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/meta.yaml
projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/worst/review_context.yaml
projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/median/review_context.yaml
projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/best/review_context.yaml
projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/worst/imagined_experiments.yaml
projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/median/imagined_experiments.yaml
projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/best/imagined_experiments.yaml
projects/structfuse-context/artifacts/dream_reports/dream_20260512T204322/meta.yaml
projects/structfuse-context/artifacts/dream_reports/dream_20260512T204322/worst/imagined_experiments.yaml
projects/structfuse-context/artifacts/dream_reports/dream_20260512T204322/median/imagined_experiments.yaml
projects/structfuse-context/artifacts/dream_reports/dream_20260512T204322/best/imagined_experiments.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5b54dfc1-f776-4e4b-b638-7cbce71fea23",
  "isSidechain": true,
  "promptId": "1589742a-41cc-4d40-ae94-dc9d919d6688",
  "agentId": "aae11a3504772ac7f",
  "type": "user",
  "uuid": "9b240dbe-8092-44bf-b285-e9e32f2abb39",
  "sourceToolAssistantUUID": "5b54dfc1-f776-4e4b-b638-7cbce71fea23",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "c4036345-91c5-47f2-9c09-36d0f1b82314",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-16T15:06:40.716Z_

Excellent! I found the dream reports with tier structure. Let me explore those:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9b240dbe-8092-44bf-b285-e9e32f2abb39",
  "isSidechain": true,
  "agentId": "aae11a3504772ac7f",
  "requestId": "req_011Cb6TPnd3QH6MGxBwCWtYr",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c78987ef-bc98-4c48-b57b-031bd21cb2f6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "c4036345-91c5-47f2-9c09-36d0f1b82314",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01FJAoEztGtbABLUuPU8fVzU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 2444,
      "cache_read_input_tokens": 34089,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2444,
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

_source line 30 · 2026-05-16T15:06:41.424Z_

<details open><summary>🔧 Tool call — Read · `toolu_01EvcVS4WKaHKFfB4aGXsRmW`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/meta.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c78987ef-bc98-4c48-b57b-031bd21cb2f6",
  "isSidechain": true,
  "agentId": "aae11a3504772ac7f",
  "requestId": "req_011Cb6TPnd3QH6MGxBwCWtYr",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "820f4746-3044-4e8d-b508-9ad6bd337ee2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "c4036345-91c5-47f2-9c09-36d0f1b82314",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01FJAoEztGtbABLUuPU8fVzU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 2444,
      "cache_read_input_tokens": 34089,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2444,
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

### Tool result

_source line 31 · 2026-05-16T15:06:41.715Z_

<details><summary>↩ Tool result · reported error · `toolu_01EvcVS4WKaHKFfB4aGXsRmW`</summary>

```text
File content (62631 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "820f4746-3044-4e8d-b508-9ad6bd337ee2",
  "isSidechain": true,
  "promptId": "1589742a-41cc-4d40-ae94-dc9d919d6688",
  "agentId": "aae11a3504772ac7f",
  "type": "user",
  "uuid": "95a4d374-88ec-4543-bb84-e8c2462e09aa",
  "toolUseResult": "Error: File content (62631 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.",
  "sourceToolAssistantUUID": "820f4746-3044-4e8d-b508-9ad6bd337ee2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "c4036345-91c5-47f2-9c09-36d0f1b82314",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-16T15:06:41.855Z_

<details open><summary>🔧 Tool call — Read · `toolu_01RtHwSijudwpfr8VBNRT66L`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/best/review_context.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "95a4d374-88ec-4543-bb84-e8c2462e09aa",
  "isSidechain": true,
  "agentId": "aae11a3504772ac7f",
  "requestId": "req_011Cb6TPnd3QH6MGxBwCWtYr",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b0f1bef3-4cf7-4979-bbbe-3a248efa1e88",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "c4036345-91c5-47f2-9c09-36d0f1b82314",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01FJAoEztGtbABLUuPU8fVzU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 2444,
      "cache_read_input_tokens": 34089,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2444,
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

_source line 33 · 2026-05-16T15:06:41.942Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01CRkJRiCE4tyEbD3oEgTiMv`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts -type f -name \"*.json\" | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b0f1bef3-4cf7-4979-bbbe-3a248efa1e88",
  "isSidechain": true,
  "agentId": "aae11a3504772ac7f",
  "requestId": "req_011Cb6TPnd3QH6MGxBwCWtYr",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "2a7b9076-e88c-48a1-ac32-c4cedf898b8b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "c4036345-91c5-47f2-9c09-36d0f1b82314",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01FJAoEztGtbABLUuPU8fVzU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 2444,
      "cache_read_input_tokens": 34089,
      "output_tokens": 278,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2444
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 278,
          "cache_read_input_tokens": 34089,
          "cache_creation_input_tokens": 2444,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2444,
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

_source line 34 · 2026-05-16T15:06:42.007Z_

<details><summary>↩ Tool result · `toolu_01CRkJRiCE4tyEbD3oEgTiMv`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/plan006_error_patterns.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/data/starcoder_training_trajectories.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/data/qwen_training_trajectories.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/data/pilot_results_920f68.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/data/plan_006_scalability_stats_29repos.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/data/seed_variance_vs_strategy_effect.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/data/pilot_results.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/_project/data/scalability_data.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260512T204322/median/experiment_data.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260512T204322/worst/experiment_data.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260512T204322/best/experiment_data.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/median/experiment_data.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/worst/experiment_data.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/best/experiment_data.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/median/experiment_data.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/worst/experiment_data.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/best/experiment_data.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/unixcoder-3strat-s42/analysis.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/plan_003_swebench_eval/data/swebench_bm25_baseline_100.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/plan_006_scalability_stats_29repos.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2a7b9076-e88c-48a1-ac32-c4cedf898b8b",
  "isSidechain": true,
  "promptId": "1589742a-41cc-4d40-ae94-dc9d919d6688",
  "agentId": "aae11a3504772ac7f",
  "type": "user",
  "uuid": "d831a2ba-449c-49d7-9ac6-d52e56de18a5",
  "sourceToolAssistantUUID": "2a7b9076-e88c-48a1-ac32-c4cedf898b8b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "c4036345-91c5-47f2-9c09-36d0f1b82314",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-16T15:06:42.123Z_

<details><summary>↩ Tool result · `toolu_01RtHwSijudwpfr8VBNRT66L`</summary>

```text
1	narrative_guidance: '全 18 runs（9 seeds × 2 encoders × 3 strategies）完整复现 pilot pattern。
2	  Embedding mining 在两个 encoder 上均显著优于 random（Qwen +2.0pp, StarCoder +1.5pp, 95% CI
3	  下界 > 0）。 Dataflow 在 Qwen 上条件性获益（+1.0pp, CI 下界 > 0），StarCoder 上无显著差异（-0.2pp, CI 含零）。
4	  BM25 baseline 实证关闭 CoCoHaNeRe 论证（BM25 vs random: Qwen -2.5pp, StarCoder -2.7pp）。
5	  SWE-bench Lite downstream +2.5pp embedding, +3.2pp dataflow resolve rate delta。
6	  三条 claim 原样成立，EMNLP Main 强投 framing 无需调整。 M2 full anchors — Qwen random R@1=0.545,
7	  embedding=0.565, dataflow=0.555; StarCoder random R@1=0.460, embedding=0.475, dataflow=0.458。
8	
9	  '
10	imagined_experiments:
11	- name: SWE-bench Lite End-to-End Evaluation
12	  plan_id: plan_003
13	  description: '3 strategies × best Qwen checkpoint, Qwen3.6-27B agent, 300 SWE-bench
14	    Lite instances. Retriever 提供 top-k context files，agent 生成 patch，评估 resolve rate。
15	
16	    '
17	  expected_results:
18	    random_resolve_rate: 0.22
19	    random_resolved_count: 66
20	    embedding_resolve_rate: 0.245
21	    embedding_resolved_count: 73
22	    dataflow_resolve_rate: 0.252
23	    dataflow_resolved_count: 76
24	    embedding_minus_random_pp: 2.5
25	    dataflow_minus_random_pp: 3.2
26	    dataflow_minus_embedding_pp: 0.7
27	    total_instances: 300
28	    retriever_top_k: 5
29	    agent_model: Qwen3.6-27B
30	  result_rationale: 'Embedding retriever 在 SWE-bench 上提升 +2.5pp，因为 bug-fix patch 通常涉及与
31	    issue 描述 语义相似但非完全匹配的文件——embedding mining 训练使 retriever 更擅长区分"近似但无关" 与"近似且相关"的文件。Dataflow
32	    额外提升 +0.7pp（总 +3.2pp vs random）因为 SWE-bench patch 经常跨函数/跨模块（约 40% 涉及 caller-callee
33	    关系），dataflow negatives 训练使 retriever 理解"调用链上的文件更可能共同出现在 patch 中"。Delta 幅度从 retrieval
34	    R@1 的 +2.0/+1.0pp 放大到下游 resolve rate 的 +2.5/+3.2pp，符合检索质量在端到端任务中 的杠杆效应——正确检索一个关键文件可以使原本完全失败的
35	    patch 变为可解决。 效果幅度在 swebench_resolve_rate_delta_pp [1.5, 4.0] 范围内。
36	
37	    '
38	  tables:
39	  - name: 'Table 4: SWE-bench Lite Resolve Rate'
40	    columns:
41	    - Strategy
42	    - Resolved
43	    - Total
44	    - Rate (%)
45	    - Δ vs Random (pp)
46	    rows:
47	    - - random
48	      - 66
49	      - 300
50	      - 22.0
51	      - —
52	    - - embedding
53	      - 73
54	      - 300
55	      - 24.3
56	      - '+2.3'
57	    - - dataflow
58	      - 76
59	      - 300
60	      - 25.3
61	      - '+3.3'
62	  - name: 'Table 4b: SWE-bench by Patch Complexity'
63	    columns:
64	    - Patch Type
65	    - N
66	    - random (%)
67	    - embedding (%)
68	    - dataflow (%)
69	    rows:
70	    - - single-file
71	      - 189
72	      - 28.0
73	      - 30.7
74	      - 30.2
75	    - - multi-file
76	      - 111
77	      - 11.7
78	      - 14.4
79	      - 17.1
80	  figures_description:
81	  - 'Fig 5: SWE-bench resolve rate bar chart (3 strategies) with bootstrap 95% CI
82	    whiskers'
83	  - 'Fig 5b: Scatter plot — retrieval R@1 rank vs resolve rate per instance, colored
84	    by strategy'
85	  analysis: 'Multi-file patches（占 37%）是 dataflow 拉开差距的主要来源：dataflow 在 multi-file 上
86	    +5.4pp vs random，远大于 single-file 的 +2.2pp。这与 Claim 2 一致——dataflow negatives 使
87	    retriever 更好地理解跨模块依赖。Embedding vs random 在 multi-file 上也有 +2.7pp，说明更难的 negatives
88	    普遍有益。总体 resolve rate 22-25% 与 SweRank/SWE-Fixer 文献报告的 retriever-only baseline
89	    一致。
90	
91	    '
92	- name: RepoBench-R Cross-File Retrieval with Multi-Seed CIs
93	  plan_id: plan_004
94	  description: 'RepoBench-R test_easy (pool ~6) 和 test_hard (pool ~18) 上评估 9 seeds
95	    × 3 strategies × 2 encoders，报告 R@1 均值 + 95% bootstrap CI。
96	
97	    '
98	  expected_results:
99	    qwen_test_hard:
100	      random_R1_mean: 0.621
101	      random_R1_ci:
102	      - 0.614
103	      - 0.628
104	      embedding_R1_mean: 0.642
105	      embedding_R1_ci:
106	      - 0.634
107	      - 0.65
108	      dataflow_R1_mean: 0.633
109	      dataflow_R1_ci:
110	      - 0.624
111	      - 0.642
112	      embedding_minus_random_pp: 2.1
113	      dataflow_minus_random_pp: 1.2
114	    qwen_test_easy:
115	      random_R1_mean: 0.843
116	      embedding_R1_mean: 0.855
117	      dataflow_R1_mean: 0.85
118	      embedding_minus_random_pp: 1.2
119	    starcoder_test_hard:
120	      random_R1_mean: 0.574
121	      random_R1_ci:
122	      - 0.566
123	      - 0.582
124	      embedding_R1_mean: 0.589
125	      embedding_R1_ci:
126	      - 0.58
127	      - 0.598
128	      dataflow_R1_mean: 0.572
129	      dataflow_R1_ci:
130	      - 0.562
131	      - 0.582
132	      embedding_minus_random_pp: 1.5
133	      dataflow_minus_random_pp: -0.2
134	    starcoder_test_easy:
135	      random_R1_mean: 0.812
136	      embedding_R1_mean: 0.822
137	      dataflow_R1_mean: 0.81
138	    repobench_R1_delta_pp_embedding_avg: 1.8
139	    bootstrap_CI_width_R1_pp_avg: 1.2
140	  result_rationale: 'RepoBench-R 是 cross-file completion 任务，pool 更小（6-18），绝对 R@1 更高。
141	    Embedding mining 在两个 encoder 上均显著提升 test_hard R@1（Qwen +2.1pp, StarCoder +1.5pp），
142	    因为 pool=18 仍有足够 distractors 使 mining 质量差异体现。Test_easy pool=6 接近 ceiling，delta
143	    被压缩但方向一致。Dataflow 在 Qwen test_hard 上 +1.2pp 但 CI 刚好 排除零，StarCoder 上无效（-0.2pp，CI
144	    含零）——与 SWE-smith 上的 encoder-strategy interaction 完全一致，说明 pattern 跨 benchmark 稳定。CI
145	    宽度 ~1.2pp 在 bootstrap_CI_width_R1_pp [0.5, 2.0] 范围内，9 seeds 提供足够统计功效。
146	
147	    '
148	  tables:
149	  - name: 'Table 5: RepoBench-R Results (test_hard, pool≈18)'
150	    columns:
151	    - Encoder
152	    - Strategy
153	    - R@1 (%)
154	    - 95% CI
155	    - Δ vs Random (pp)
156	    rows:
157	    - - Qwen
158	      - random
159	      - 62.1
160	      - '[61.4, 62.8]'
161	      - —
162	    - - Qwen
163	      - embedding
164	      - 64.2
165	      - '[63.4, 65.0]'
166	      - '+2.1'
167	    - - Qwen
168	      - dataflow
169	      - 63.3
170	      - '[62.4, 64.2]'
171	      - '+1.2'
172	    - - StarCoder
173	      - random
174	      - 57.4
175	      - '[56.6, 58.2]'
176	      - —
177	    - - StarCoder
178	      - embedding
179	      - 58.9
180	      - '[58.0, 59.8]'
181	      - '+1.5'
182	    - - StarCoder
183	      - dataflow
184	      - 57.2
185	      - '[56.2, 58.2]'
186	      - −0.2
187	  figures_description:
188	  - 'Fig 6: RepoBench-R R@1 grouped bar chart (2 encoders × 3 strategies) with CI
189	    whiskers, test_easy vs test_hard side by side'
190	  analysis: 'Cross-benchmark 一致性是 best tier 的关键证据：embedding mining 在 SWE-smith 和 RepoBench-R
191	    上均显著提升两个 encoder，dataflow 条件性获益仅限 Qwen。这排除了 "结果仅限单一 benchmark" 的 reviewer concern。Test_easy
192	    上 delta 被压缩（pool=6 ceiling effect）是预期行为，反向验证了 pool size 对绝对效果幅度的调节作用。
193	
194	    '
195	- name: Stratified Analysis with Structural Coverage & Neg Difficulty Quartiles
196	  plan_id: plan_005
197	  description: '5 层分层分析：repo size / pool size / query-positive similarity / structural
198	    data availability (34% vs 66%) / neg_difficulty quartile。使用 M2 best checkpoints
199	    在 SWE-smith validation 上重新评估。
200	
201	    '
202	  expected_results:
203	    stratum_structural_available:
204	      with_dataflow_34pct:
205	        qwen_dataflow_minus_random_pp: 2.8
206	        qwen_dataflow_minus_embedding_pp: 1.3
207	        starcoder_dataflow_minus_random_pp: 0.1
208	        n_instances: ~5200
209	      fallback_66pct:
210	        qwen_dataflow_minus_random_pp: 0.1
211	        qwen_dataflow_minus_embedding_pp: -0.2
212	        starcoder_dataflow_minus_random_pp: -0.3
213	        n_instances: ~10000
214	    stratum_neg_difficulty_quartile:
215	      Q1_easiest:
216	        qwen_embedding_minus_random_pp: 0.8
217	        qwen_dataflow_minus_random_pp: 0.3
218	      Q2:
219	        qwen_embedding_minus_random_pp: 1.5
220	        qwen_dataflow_minus_random_pp: 0.7
221	      Q3:
222	        qwen_embedding_minus_random_pp: 2.4
223	        qwen_dataflow_minus_random_pp: 1.2
224	      Q4_hardest:
225	        qwen_embedding_minus_random_pp: 3.2
226	        qwen_dataflow_minus_random_pp: 2.1
227	    stratum_repo_size:
228	      small_lt50:
229	        embedding_delta_pp: 2.8
230	        n: ~500
231	      medium_50_200:
232	        embedding_delta_pp: 2.2
233	        n: ~4100
234	      large_200_500:
235	        embedding_delta_pp: 1.8
236	        n: ~5500
237	      xlarge_500plus:
238	        embedding_delta_pp: 1.6
239	        n: ~5100
240	    stratum_pool_size:
241	      pool_lt20:
242	        embedding_delta_pp: 1.0
243	        dataflow_delta_pp: 0.3
244	      pool_20_50:
245	        embedding_delta_pp: 2.1
246	        dataflow_delta_pp: 1.0
247	      pool_gt50:
248	        embedding_delta_pp: 2.5
249	        dataflow_delta_pp: 1.4
250	    stratum_query_pos_sim:
251	      high_sim_gt095:
252	        embedding_delta_pp: 2.6
253	        dataflow_delta_pp: 1.8
254	      medium_sim_085_095:
255	        embedding_delta_pp: 1.9
256	        dataflow_delta_pp: 0.8
257	      low_sim_lt085:
258	        embedding_delta_pp: 1.2
259	        dataflow_delta_pp: 0.2
260	  result_rationale: 'Structural-available stratum（34%）上 dataflow 优势放大到 +2.8pp（Qwen），因为这些
261	    instance 实际接收了 dataflow-disconnected negatives——真实训练信号未被 fallback 稀释。 Fallback
262	    stratum（66%）上 dataflow ≈ embedding（±0.2pp），因为 fallback 时 dataflow 策略退化为 embedding
263	    或 random 选择，无结构信号注入。这一分解直接回应 reviewer 关于 "34% coverage 稀释 signal" 的 concern——真实
264	    per-instance 效果是 +2.8pp 而非 pooled +1.0pp。Neg_difficulty Q4（最难 quartile）上 delta
265	    最大（embedding +3.2pp, dataflow +2.1pp），符合 representation saturation 理论——Qwen 在高
266	    pos_sim 区域最需要 harder negatives，而 Q4 恰好是 margin 最小、分辨最难的 instances。Q1（最容易）delta
267	    最小 因为 random negatives 已经足够容易区分。Repo size 上 small repo delta 更大因为 小 repo 的 candidate
268	    pool 更集中，mining 策略差异更容易体现。
269	
270	    '
271	  tables:
272	  - name: 'Table 7: Stratified R@1 Delta by Structural Data Availability (Qwen)'
273	    columns:
274	    - Stratum
275	    - N
276	    - random R@1
277	    - embedding R@1
278	    - dataflow R@1
279	    - df−rand (pp)
280	    rows:
281	    - - With dataflow (34%)
282	      - ~5.2K
283	      - 53.1
284	      - 55.4
285	      - 55.9
286	      - '+2.8'
287	    - - Fallback (66%)
288	      - ~10K
289	      - 55.2
290	      - 57.3
291	      - 55.3
292	      - '+0.1'
293	    - - Overall
294	      - ~15.2K
295	      - 54.5
296	      - 56.5
297	      - 55.5
298	      - '+1.0'
299	  - name: 'Table 7b: R@1 Delta by Neg Difficulty Quartile (Qwen)'
300	    columns:
301	    - Quartile
302	    - margin_mean
303	    - emb−rand (pp)
304	    - df−rand (pp)
305	    rows:
306	    - - Q1 (easiest)
307	      - 0.142
308	      - '+0.8'
309	      - '+0.3'
310	    - - Q2
311	      - 0.078
312	      - '+1.5'
313	      - '+0.7'
314	    - - Q3
315	      - 0.031
316	      - '+2.4'
317	      - '+1.2'
318	    - - Q4 (hardest)
319	      - 0.008
320	      - '+3.2'
321	      - '+2.1'
322	  figures_description:
323	  - 'Fig 7: Heatmap — R@1 delta (strategy × stratum), separate panels for Qwen and
324	    StarCoder'
325	  - 'Fig 8: Neg difficulty quartile vs R@1 delta line plot, 3 strategies overlaid'
326	  analysis: 'Stratified analysis 提供了论文中最强的 mechanistic 证据。Neg_difficulty Q4 的 +3.2pp
327	    embedding delta 是 overall +2.0pp 的 1.6 倍——越难的 instances 从 harder negatives 获益越多，这是
328	    representation saturation 理论的直接预测。Structural-available vs fallback 分解消除了 "diluted
329	    signal" concern 并揭示 dataflow 的真实 per-instance 效果（+2.8pp）远大于 pooled 报告值。
330	
331	    '
332	- name: Call-Graph Hop Depth Ablation (1/2/3-hop)
333	  plan_id: plan_007
334	  description: '比较 1-hop / 2-hop / 3-hop call-graph bounding 对 dataflow negative 质量的影响。
335	    Qwen encoder, 1 seed, SWE-smith validation。
336	
337	    '
338	  expected_results:
339	    hop_1:
340	      R1: 0.548
341	      connected_coverage_pct: 12.4
342	      negatives_per_query_mean: 18.2
343	    hop_2:
344	      R1: 0.555
345	      connected_coverage_pct: 34.3
346	      negatives_per_query_mean: 31.7
347	    hop_3:
348	      R1: 0.551
349	      connected_coverage_pct: 58.6
350	      negatives_per_query_mean: 42.1
351	    optimal_hop: 2
352	    hop2_minus_hop1_pp: 0.7
353	    hop3_minus_hop2_pp: -0.4
354	  result_rationale: '2-hop 是最优平衡点。1-hop 太保守——仅 12.4% coverage 意味着大部分 instance 没有足够的
355	    connected 节点来定义 "disconnected" negatives，退化为 random。3-hop 过于宽松——58.6% coverage
356	    下 "disconnected" 的定义变得太窄，许多语义相关但间接连接的文件被错误排除在 negative pool 外，引入噪声。2-hop 的 34.3%
357	    coverage（与 M1 extraction 的 structural data rate 一致）在 "enough connected nodes to
358	    define meaningful disconnection" 和 "disconnected set still contains genuinely
359	    unrelated files" 之间取得平衡。
360	
361	    '
362	  tables:
363	  - name: 'Table 9: Hop Depth Ablation (Qwen, dataflow strategy)'
364	    columns:
365	    - Hops
366	    - Coverage (%)
367	    - Neg/query
368	    - R@1 (%)
369	    - Δ vs 2-hop (pp)
370	    rows:
371	    - - 1
372	      - 12.4
373	      - 18.2
374	      - 54.8
375	      - −0.7
376	    - - 2
377	      - 34.3
378	      - 31.7
379	      - 55.5
380	      - —
381	    - - 3
382	      - 58.6
383	      - 42.1
384	      - 55.1
385	      - −0.4
386	  figures_description:
387	  - 'Fig S1: Hop depth vs R@1 line plot with coverage % on secondary y-axis'
388	  analysis: '2-hop optimal 符合 inter-procedural dataflow 的语义：1-hop = 直接 caller/callee，
389	    2-hop = caller 的 caller 或 callee 的 callee（一层间接调用），3-hop 开始包含 过于间接的关系。论文可以强调 2-hop
390	    选择有 principled 依据而非纯粹 empirical tuning。
391	
392	    '
393	- name: Training Data Size Scaling (1K/3K/5K)
394	  plan_id: plan_008
395	  description: '固定 Qwen encoder + embedding strategy，训练数据从 1K / 3K / 5K instances
396	    增长， 观察 R@1 变化和策略排名稳定性。
397	
398	    '
399	  expected_results:
400	    size_1K:
401	      random_R1: 0.51
402	      embedding_R1: 0.522
403	      dataflow_R1: 0.515
404	      embedding_minus_random_pp: 1.2
405	      seed_std: 0.015
406	    size_3K:
407	      random_R1: 0.532
408	      embedding_R1: 0.55
409	      dataflow_R1: 0.541
410	      embedding_minus_random_pp: 1.8
411	      seed_std: 0.01
412	    size_5K:
413	      random_R1: 0.545
414	      embedding_R1: 0.565
415	      dataflow_R1: 0.555
416	      embedding_minus_random_pp: 2.0
417	      seed_std: 0.008
418	    ranking_stable: true
419	    monotonic_improvement: true
420	  result_rationale: '策略排名在 1K/3K/5K 三个尺度上保持一致（embedding > dataflow > random），但 delta
421	    幅度随数据量增大而增大——1K 时 +1.2pp，5K 时 +2.0pp。这是因为更大的训练集提供更多 diverse negatives，使 mining
422	    策略的差异更充分地体现。1K 时 seed 方差较大（std=0.015） 因为 negative 多样性不足，个别 seed 的 negative 采样偶然性影响结果。5K
423	    时方差收敛 （std=0.008），mining 策略的信号超过采样噪声。No diminishing returns at 5K suggests further
424	    scaling could help, but is beyond scope。
425	
426	    '
427	  tables:
428	  - name: 'Table 10: Data Size Scaling (Qwen)'
429	    columns:
430	    - Size
431	    - random R@1
432	    - embedding R@1
433	    - dataflow R@1
434	    - emb−rand (pp)
435	    - σ across seeds
436	    rows:
437	    - - 1K
438	      - 51.0
439	      - 52.2
440	      - 51.5
441	      - '+1.2'
442	      - 1.5
443	    - - 3K
444	      - 53.2
445	      - 55.0
446	      - 54.1
447	      - '+1.8'
448	      - 1.0
449	    - - 5K
450	      - 54.5
451	      - 56.5
452	      - 55.5
453	      - '+2.0'
454	      - 0.8
455	  figures_description:
456	  - 'Fig S2: R@1 vs training size for 3 strategies, with shaded seed variance bands'
457	  analysis: 'Monotonic scaling + stable ranking 表明结果不是 small-data artifact。5K 时未见
458	    diminishing returns，暗示更大数据集可能进一步放大差异。这对 reviewer "effect size marginal" concern
459	    有价值——delta 仍在增长，当前 +2.0pp 是下界而非上界。
460	
461	    '
462	- name: Fusion Head Ablation
463	  plan_id: plan_009
464	  description: '比较 embedding-only / structural-features-only / combined fusion head，
465	    隔离 training-time mining 价值与 inference-time feature injection。
466	
467	    '
468	  expected_results:
469	    embedding_only:
470	      qwen_R1: 0.565
471	      starcoder_R1: 0.475
472	    structural_features_only:
473	      qwen_R1: 0.498
474	      starcoder_R1: 0.421
475	    combined_fusion:
476	      qwen_R1: 0.561
477	      starcoder_R1: 0.472
478	    embedding_only_minus_combined_pp: 0.4
479	    conclusion: mining > fusion; structural features at inference add noise
480	  result_rationale: 'Embedding-only（仅用 embedding mining 训练的 retriever，inference 时不注入结构特征）
481	    表现最好或 tied with combined。Combined fusion 略低 0.4pp 因为 inference-time structural
482	    features 引入了不精确的 CodeQL connectivity 信号——recall 某些 CodeQL extraction 失败的 instance
483	    反而被错误降权。Structural-features-only（不用 mining 训练， 仅在 inference 注入结构特征）远低于 embedding-only（-6.7pp
484	    Qwen），证明核心价值在 training-time negative mining 而非 inference-time feature engineering。
485	    这一结果对 paper framing 极为重要：StructFuse 的贡献是 mining strategy，不是 fusion。
486	
487	    '
488	  tables:
489	  - name: 'Table 11: Fusion Head Ablation'
490	    columns:
491	    - Configuration
492	    - Qwen R@1 (%)
493	    - StarCoder R@1 (%)
494	    rows:
495	    - - embedding-only (ours)
496	      - 56.5
497	      - 47.5
498	    - - structural-features-only
499	      - 49.8
500	      - 42.1
501	    - - combined fusion
502	      - 56.1
503	      - 47.2
504	  figures_description:
505	  - 'Fig S3: Ablation bar chart comparing 3 fusion configurations'
506	  analysis: '训练时注入 structural signal 通过 negative mining（间接信号）比 inference 时直接注入 structural
507	    features（直接信号）更有效。可能原因：mining 让 encoder 自己学习结构相关的 representation，而直接注入 features
508	    绕过了 encoder 的学习过程，且 CodeQL 34% coverage 意味着 66% instance 在 inference 时收到 zero-vector
509	    structural features，引入 noise。
510	
511	    '
512	- name: Dataflow-Distance Weighted vs Binary Negatives
513	  plan_id: plan_010
514	  description: '比较 binary connected/disconnected 与 dataflow-distance weighted negative
515	    sampling。 Weighted: disconnected 且 hop-distance 更远的文件被赋予更高采样概率。
516	
517	    '
518	  expected_results:
519	    binary_qwen_R1: 0.555
520	    weighted_qwen_R1: 0.558
521	    binary_starcoder_R1: 0.458
522	    weighted_starcoder_R1: 0.459
523	    weighted_minus_binary_qwen_pp: 0.3
524	    weighted_minus_binary_starcoder_pp: 0.1
525	  result_rationale: 'Weighted 在 Qwen 上仅微弱提升 +0.3pp（不显著），StarCoder 上几乎无差异。 原因：binary
526	    disconnected/connected 已经捕获了最关键的 structural distinction—— "是否在调用链上"。进一步按 hop distance
527	    加权引入的额外信号被 noise 抵消：距离更远 不一定意味着更好的 negative（一个完全无关的 utility 文件可能 hop=∞ 但也是 trivial
528	    negative）。 Binary 的简洁性是优势——fewer hyperparameters, same effect。
529	
530	    '
531	  tables:
532	  - name: 'Table S1: Weighted vs Binary Dataflow Negatives'
533	    columns:
534	    - Method
535	    - Qwen R@1 (%)
536	    - StarCoder R@1 (%)
537	    - Δ vs Binary (pp)
538	    rows:
539	    - - Binary (default)
540	      - 55.5
541	      - 45.8
542	      - —
543	    - - Distance-weighted
544	      - 55.8
545	      - 45.9
546	      - +0.3 / +0.1
547	  figures_description: []
548	  analysis: 'Binary is sufficient — complexity of weighted sampling not justified.
549	    论文可在 ablation section 用一句话报告这一 negative result， 强化 "simple binary structural signal
550	    is the key insight" 的 narrative。
551	
552	    '
553	- name: SWE-bench Failure Analysis (50 cases)
554	  plan_id: plan_011
555	  description: '从 random retriever 的 SWE-bench 失败案例中抽样 50 个，人工分类失败原因， 标注 dataflow
556	    信号是否可能帮助。
557	
558	    '
559	  expected_results:
560	    total_analyzed: 50
561	    category_breakdown:
562	      retrieval_failure_wrong_files: 22
563	      retrieval_success_but_agent_fail: 15
564	      insufficient_context_window: 7
565	      test_environment_issue: 4
566	      ambiguous_issue_description: 2
567	    dataflow_could_help:
568	      true: 14
569	      partially: 5
570	      false: 31
571	    dataflow_help_rate: 0.28
572	    key_pattern: '14/22 retrieval failures involve cross-module dependencies where
573	      the gold file is a caller/callee of a retrieved-but-wrong file — dataflow connectivity
574	      would directly address these.
575	
576	      '
577	  result_rationale: '50 个失败中 22 个是 retrieval failure（检索到错误文件），其中 14 个涉及跨模块依赖—— 被检索的文件和
578	    gold 文件有高文本相似度但分属不同 call chain。Dataflow negatives 训练 恰好针对这类 confound。15 个 retrieval
579	    success but agent fail 说明 retrieval 不是 唯一瓶颈——agent 的 patch 生成能力也是限制因素。这为论文提供了
580	    "ceiling analysis"： 即使 perfect retrieval，resolve rate 上限约 85%（15% 是 agent 能力限制）。
581	
582	    '
583	  tables:
584	  - name: 'Table S2: Failure Category Breakdown'
585	    columns:
586	    - Category
587	    - Count
588	    - '% of 50'
589	    - Dataflow Could Help?
590	    rows:
591	    - - 'Retrieval: wrong files'
592	      - 22
593	      - 44
594	      - 14/22 (64%)
595	    - - Retrieval OK, agent fail
596	      - 15
597	      - 30
598	      - N/A
599	    - - Context window limit
600	      - 7
601	      - 14
602	      - 5/7 partially
603	    - - Test env issue
604	      - 4
605	      - 8
606	      - 'No'
607	    - - Ambiguous issue
608	      - 2
609	      - 4
610	      - 'No'
611	  figures_description:
612	  - 'Fig S4: Sankey diagram — failure flow from retrieval stage to resolution outcome'
613	  analysis: '28% of failures could benefit from dataflow signal, consistent with the
614	    observed +3.2pp resolve rate improvement. The 64% rate within retrieval failures
615	    confirms that cross-module dependency is the primary retrieval challenge, directly
616	    supporting Claim 2''s motivation.
617	
618	    '
619	- name: Qualitative Examples (5-10 cases)
620	  plan_id: plan_012
621	  description: '从 SWE-bench 和 SWE-smith 中选取 5-10 个 dataflow negatives 改变检索结果的典型案例，
622	    展示 structural signal 的具体作用机制。
623	
624	    '
625	  expected_results:
626	    total_examples: 8
627	    example_categories:
628	      caller_callee_confusion: 3
629	      utility_file_distraction: 2
630	      cross_module_import_chain: 2
631	      test_file_vs_source: 1
632	    illustrative_example:
633	      issue: django/django#12345 — QuerySet.filter() returns wrong results with nested
634	        Q objects
635	      random_retriever_top1: django/db/models/query.py (text match on 'filter')
636	      dataflow_retriever_top1: django/db/models/sql/query.py (actual SQL generation
637	        called by filter)
638	      gold: django/db/models/sql/query.py
639	      explanation: 'Random retriever picks query.py (contains ''filter'' method signature)
640	        but the bug is in sql/query.py (the downstream SQL builder called by filter).
641	        Dataflow training teaches the model that sql/query.py is structurally connected
642	        to query.py via 2-hop call chain, making it a better negative for other instances,
643	        which in turn improves the model''s ability to rank the actual implementation
644	        file higher.
645	
646	        '
647	  result_rationale: '8 个案例覆盖 4 个失败模式：caller-callee confusion（3 个，最常见——文本相似的 wrapper
648	    函数 vs 实际实现）、utility file distraction（2 个——高文本重叠的 helper 文件干扰）、 cross-module import
649	    chain（2 个——A 导入 B 导入 C，bug 在 C 但文本匹配 A）、test vs source（1 个——test file 包含几乎完整的
650	    source code 复制）。这些案例具体展示了 "lexical similarity ≠ structural relevance" 的核心 insight。
651	
652	    '
653	  tables: []
654	  figures_description:
655	  - 'Fig 9: Side-by-side retrieval ranking visualization for 3 representative cases,
656	    showing file dependency graph with highlighted paths'
657	  analysis: 'Qualitative examples serve as the paper''s "aha moment" — they make the
658	    abstract representation geometry argument concrete. Reviewer-facing value: even
659	    skeptics who question statistical significance can see the mechanism operating
660	    on real code.
661	
662	    '
663	- name: Temperature Ablation τ ∈ {0.05, 0.1, 0.2}
664	  plan_id: plan_014
665	  description: '3 temperatures × 3 strategies × 2 encoders, 1 seed each. 测试 strategy
666	    ranking 是否 regime-specific。
667	
668	    '
669	  expected_results:
670	    tau_005:
671	      qwen_random_R1: 0.558
672	      qwen_embedding_R1: 0.577
673	      qwen_dataflow_R1: 0.569
674	      qwen_embedding_minus_random_pp: 1.9
675	      starcoder_random_R1: 0.47
676	      starcoder_embedding_R1: 0.485
677	      starcoder_dataflow_R1: 0.467
678	      starcoder_embedding_minus_random_pp: 1.5
679	    tau_010:
680	      qwen_random_R1: 0.545
681	      qwen_embedding_R1: 0.565
682	      qwen_dataflow_R1: 0.555
683	      qwen_embedding_minus_random_pp: 2.0
684	      starcoder_random_R1: 0.46
685	      starcoder_embedding_R1: 0.475
686	      starcoder_dataflow_R1: 0.458
687	      starcoder_embedding_minus_random_pp: 1.5
688	    tau_020:
689	      qwen_random_R1: 0.53
690	      qwen_embedding_R1: 0.546
691	      qwen_dataflow_R1: 0.538
692	      qwen_embedding_minus_random_pp: 1.6
693	      starcoder_random_R1: 0.448
694	      starcoder_embedding_R1: 0.461
695	      starcoder_dataflow_R1: 0.447
696	      starcoder_embedding_minus_random_pp: 1.3
697	    ranking_preserved_across_tau: true
698	    optimal_tau: 0.05
699	  result_rationale: 'Strategy ranking（embedding > dataflow > random for Qwen; embedding
700	    > random ≈ dataflow for StarCoder）在三个 temperature 下保持一致。τ=0.05 绝对性能最高因为 sharper
701	    temperature 使 contrastive loss 更有效地区分相似度差异（harder gradient signal）。 τ=0.2 下所有策略性能下降且
702	    delta 缩小（1.6pp vs 2.0pp），因为 softer temperature 减弱了 negative 选择质量的影响——当所有 similarity
703	    被压缩到窄范围内，hard vs easy negatives 的梯度差异变小。关键结论：findings 不是 temperature-regime-specific，
704	    直接回应 median reviewer 的 "τ=0.05 unusually low" concern。
705	
706	    '
707	  tables:
708	  - name: 'Table 8: Temperature Ablation (R@1 %)'
709	    columns:
710	    - τ
711	    - Encoder
712	    - random
713	    - embedding
714	    - dataflow
715	    - emb−rand (pp)
716	    rows:
717	    - - 0.05
718	      - Qwen
719	      - 55.8
720	      - 57.7
721	      - 56.9
722	      - '+1.9'
723	    - - 0.05
724	      - StarCoder
725	      - 47.0
726	      - 48.5
727	      - 46.7
728	      - '+1.5'
729	    - - 0.1
730	      - Qwen
731	      - 54.5
732	      - 56.5
733	      - 55.5
734	      - '+2.0'
735	    - - 0.1
736	      - StarCoder
737	      - 46.0
738	      - 47.5
739	      - 45.8
740	      - '+1.5'
741	    - - 0.2
742	      - Qwen
743	      - 53.0
744	      - 54.6
745	      - 53.8
746	      - '+1.6'
747	    - - 0.2
748	      - StarCoder
749	      - 44.8
750	      - 46.1
751	      - 44.7
752	      - '+1.3'
753	  figures_description:
754	  - 'Fig S5: Temperature × strategy interaction plot (R@1 on y-axis, τ on x-axis,
755	    separate lines per strategy)'
756	  analysis: 'Ranking stability across τ 是重要的 robustness evidence。τ=0.2 下 delta 缩小但
757	    不翻转，说明 mining quality 的价值在不同 loss sharpness 下都存在。Paper 可以报告 τ=0.05 作为 alternative
758	    best configuration 但选择 τ=0.1 作为 default（更常见的 literature default）。
759	
760	    '
761	- name: Dynamic vs Static Embedding Mining
762	  plan_id: plan_015
763	  description: 'Dynamic: 每 epoch 重新用当前 encoder 挖 embedding negatives。 Static: 仅用 pretrained
764	    encoder 挖一次（当前做法）。 Qwen + StarCoder, 1 seed each。
765	
766	    '
767	  expected_results:
768	    qwen_static_R1: 0.565
769	    qwen_dynamic_R1: 0.568
770	    qwen_dynamic_minus_static_pp: 0.3
771	    starcoder_static_R1: 0.475
772	    starcoder_dynamic_R1: 0.477
773	    starcoder_dynamic_minus_static_pp: 0.2
774	    dynamic_significant: false
775	    curriculum_confound_ruled_out: true
776	  result_rationale: 'Dynamic mining 仅微弱提升 +0.2-0.3pp（不显著），因为 LoRA rank 16 的 fine-tuning
777	    只轻微改变 embedding space——pretrained encoder 的 nearest neighbors 在训练后 仍然大部分相同。这排除了
778	    "static mining 的优势来自 curriculum effect（early epochs 看到 harder negatives 然后 negatives
779	    变 stale）" 的 confound——即使更新 negatives， 效果几乎不变。对 Claim 2 很重要：说明 mining strategy
780	    的选择（what to mine）比 mining schedule（when to mine）更关键。Dynamic mining 的 compute overhead（每
781	    epoch 重新 encode + kNN）不 justified。
782	
783	    '
784	  tables:
785	  - name: 'Table 13: Static vs Dynamic Embedding Mining'
786	    columns:
787	    - Encoder
788	    - Static R@1 (%)
789	    - Dynamic R@1 (%)
790	    - Δ (pp)
791	    - p-value
792	    rows:
793	    - - Qwen
794	      - 56.5
795	      - 56.8
796	      - '+0.3'
797	      - 0.41
798	    - - StarCoder
799	      - 47.5
800	      - 47.7
801	      - '+0.2'
802	      - 0.53
803	  figures_description:
804	  - 'Fig S6: Learning curves for static vs dynamic mining, overlaid'
805	  analysis: 'Static ≈ dynamic 是 clean negative result，强化了论文 narrative：关键是 negative
806	    的 semantic quality（embedding vs random vs dataflow），不是 freshness。 也简化了 practitioner
807	    recommendation——mine once from pretrained, no need for per-epoch re-mining。
808	
809	    '
810	- name: Bootstrap CIs for SWE-bench Lite Resolve Rate
811	  plan_id: plan_016
812	  description: '对 plan_003 的 SWE-bench 结果计算 10K bootstrap resamples 的 95% CI， 报告 paired
813	    difference CIs 和 p-values。
814	
815	    '
816	  expected_results:
817	    embedding_minus_random:
818	      delta_pp: 2.5
819	      ci_95:
820	      - 0.7
821	      - 4.3
822	      p_value: 0.018
823	      significant: true
824	    dataflow_minus_random:
825	      delta_pp: 3.2
826	      ci_95:
827	      - 1.0
828	      - 5.5
829	      p_value: 0.008
830	      significant: true
831	    dataflow_minus_embedding:
832	      delta_pp: 0.7
833	      ci_95:
834	      - -1.5
835	      - 2.9
836	      p_value: 0.134
837	      significant: false
838	    bootstrap_n: 10000
839	    sample_size: 300
840	  result_rationale: 'Embedding vs random CI [0.7, 4.3] 排除零（p=0.018），确认 embedding mining
841	    在下游 任务上的统计显著提升。Dataflow vs random 更显著（p=0.008）因为 delta 更大且 SWE-bench 中 cross-module
842	    patches 对 dataflow signal 响应一致。Dataflow vs embedding 不显著 （p=0.134, CI 含零）——300
843	    instances 的 power 不足以区分 +0.7pp 的小 delta，这是 expected：retrieval level 的 ~1pp 差异在下游
844	    binary resolve 结果上被放大和噪声化。 CI 宽度 ~3.6pp 反映 300 样本的 inherent variance——SWE-bench
845	    Lite 不是为精确 delta 估计设计的 benchmark。
846	
847	    '
848	  tables:
849	  - name: 'Table 4c: SWE-bench Bootstrap Significance Tests'
850	    columns:
851	    - Comparison
852	    - Δ (pp)
853	    - 95% CI
854	    - p-value
855	    rows:
856	    - - embedding − random
857	      - '+2.5'
858	      - '[+0.7, +4.3]'
859	      - 0.018
860	    - - dataflow − random
861	      - '+3.2'
862	      - '[+1.0, +5.5]'
863	      - 0.008
864	    - - dataflow − embedding
865	      - '+0.7'
866	      - '[−1.5, +2.9]'
867	      - 0.134
868	  figures_description:
869	  - 'Fig 5c: Bootstrap distribution histograms for the 3 pairwise comparisons'
870	  analysis: 'CI 下界 > 0 for both mining strategies vs random 是 EMNLP reviewer 需要的统计保证。
871	    Dataflow vs embedding 不显著是 honest reporting 且与 Claim 2 的 "conditional" framing
872	    一致——dataflow 的额外价值不是 universally separable at SWE-bench scale。
873	
874	    '
875	- name: Inference-Time Graph Method Literature Comparison
876	  plan_id: plan_017
877	  description: '文献分析（非实验）：与 CodexGraph, LocAgent, RANGER 等 inference-time 图方法的 系统比较。已完成
878	    8 篇论文 survey。
879	
880	    '
881	  expected_results:
882	    papers_surveyed: 8
883	    key_distinction: training-time mining (ours) vs inference-time graph navigation
884	    complementarity_evidence: 'All 8 methods operate at inference time; StructFuse
885	      mines at training time. The two approaches are complementary — StructFuse improves
886	      the base retriever that graph methods navigate over.
887	
888	      '
889	    papers_list:
890	    - CodexGraph
891	    - LocAgent
892	    - RANGER
893	    - GraphCoder
894	    - ARISE
895	    - RepoGraph
896	    - CodeGRAG
897	    - CodeRAG
898	  result_rationale: '8 篇 inference-time graph 方法均在推理阶段构建/遍历代码图，而 StructFuse 在训练阶段
899	    通过 negative mining 将结构信号蒸馏进 encoder。两者正交：StructFuse 产出更好的 base retriever，inference-time
900	    方法在此基础上进一步 re-rank/navigate。无直接可比性因为 实验设置完全不同（LocAgent 用 LLM agent + tool calls，我们用
901	    embedding retrieval）。 Discussion section 应明确 "complementary, not competing" 的定位。
902	
903	    '
904	  tables:
905	  - name: 'Table S3: Comparison with Inference-Time Graph Methods'
906	    columns:
907	    - Method
908	    - Graph Stage
909	    - Graph Type
910	    - Complementary?
911	    rows:
912	    - - StructFuse (ours)
913	      - Training
914	      - Dataflow (CodeQL)
915	      - —
916	    - - CodexGraph
917	      - Inference
918	      - Code graph DB
919	      - 'Yes'
920	    - - LocAgent
921	      - Inference
922	      - Repo structure
923	      - 'Yes'
924	    - - RANGER
925	      - Inference
926	      - Call graph
927	      - 'Yes'
928	    - - ARISE
929	      - Inference
930	      - Intra-proc dataflow
931	      - Partially (intra only)
932	  figures_description: []
933	  analysis: 'Discussion 中用 2 段落即可。不要 overclaim StructFuse 优于这些方法——它们解决不同问题。 Highlight:
934	    StructFuse 是唯一在 training time 利用结构信号的方法，且不增加 inference cost。
935	
936	    '
937	- name: BM25 Negative Baseline — Closing CoCoHaNeRe Argument
938	  plan_id: plan_018
939	  description: 'BM25-based hard negatives 作为第 4 策略，1+ seed × 2 encoders。 验证 CoCoHaNeRe
940	    报告的 "embedding negatives harm" 实际是 BM25-proxy artifact。
941	
942	    '
943	  expected_results:
944	    qwen:
945	      bm25_R1: 0.52
946	      random_R1: 0.545
947	      embedding_R1: 0.565
948	      dataflow_R1: 0.555
949	      bm25_minus_random_pp: -2.5
950	      embedding_minus_bm25_pp: 4.5
951	    starcoder:
952	      bm25_R1: 0.433
953	      random_R1: 0.46
954	      embedding_R1: 0.475
955	      dataflow_R1: 0.458
956	      bm25_minus_random_pp: -2.7
957	      embedding_minus_bm25_pp: 4.2
958	    bm25_harms_both_encoders: true
959	    cocohanere_artifact_confirmed: true
960	    bm25_minus_random_avg_pp: -2.6
961	  result_rationale: 'BM25 negatives 在两个 encoder 上均 harm performance（Qwen -2.5pp, StarCoder
962	    -2.7pp vs random），直接复现了 CoCoHaNeRe 报告的负面效果方向。关键 insight：BM25 negatives 选取的是 lexically
963	    similar 但 semantically ambiguous 的文件——它们与 query 共享大量 token overlap（function names,
964	    variable names, import patterns），但这种 overlap 恰恰是 contrastive learning 需要利用来区分
965	    positive/negative 的信号。用 BM25 选的 negatives 让模型学会 ignore lexical cues，但这些 cues 在
966	    code retrieval 中是有效信号。 相比之下，true embedding distance negatives 选取的是 semantically
967	    similar（在 pretrained embedding space 中近）但与 query 不同的文件，这迫使模型学习更 fine-grained semantic
968	    distinctions。BM25 vs embedding 的 4.5pp 差距（Qwen）是论文中最大的 single pairwise comparison，构成
969	    Claim 1 correction argument 的 empirical closure。 效果幅度在 bm25_minus_random_R1_pp
970	    [-4.0, -1.5] 范围内。
971	
972	    '
973	  tables:
974	  - name: 'Table 3: Full 4-Strategy Comparison Including BM25 Baseline'
975	    columns:
976	    - Encoder
977	    - Strategy
978	    - R@1 (%)
979	    - 95% CI
980	    - Δ vs Random (pp)
981	    rows:
982	    - - Qwen
983	      - BM25
984	      - 52.0
985	      - '[51.2, 52.8]'
986	      - −2.5
987	    - - Qwen
988	      - random
989	      - 54.5
990	      - '[53.8, 55.2]'
991	      - —
992	    - - Qwen
993	      - dataflow
994	      - 55.5
995	      - '[54.6, 56.4]'
996	      - '+1.0'
997	    - - Qwen
998	      - embedding
999	      - 56.5
1000	      - '[55.8, 57.2]'
1001	      - '+2.0'
1002	    - - StarCoder
1003	      - BM25
1004	      - 43.3
1005	      - '[42.3, 44.3]'
1006	      - −2.7
1007	    - - StarCoder
1008	      - random
1009	      - 46.0
1010	      - '[45.1, 46.9]'
1011	      - —
1012	    - - StarCoder
1013	      - dataflow
1014	      - 45.8
1015	      - '[44.8, 46.8]'
1016	      - −0.2
1017	    - - StarCoder
1018	      - embedding
1019	      - 47.5
1020	      - '[46.6, 48.4]'
1021	      - '+1.5'
1022	  figures_description:
1023	  - 'Fig 3: 4-strategy R@1 bar chart with BM25 highlighted in red, showing the harm
1024	    direction. Annotation arrow from BM25 to embedding with ''4.5pp gap — the CoCoHaNeRe
1025	    artifact'''
1026	  - 'Fig 4: Neg similarity distribution histograms for BM25 vs embedding vs random
1027	    vs dataflow, showing BM25 occupies a different region of similarity space'
1028	  analysis: 'BM25 baseline 是 best tier 论文的 crown jewel experiment。它将 Claim 1 从 "argumentative
1029	    correction" 升级为 "empirical demonstration"：我们不仅指出 CoCoHaNeRe 用了 BM25 proxy， 还实际运行
1030	    BM25 negatives 复现了 harm effect，然后展示 true embedding negatives 方向相反。 4-strategy
1031	    ordering BM25 < random < dataflow ≤ embedding 清晰展示了 negative mining strategy 的
1032	    quality spectrum。Reviewer 对 "correction without evidence" 的 concern 被彻底关闭。
1033	
1034	    '
1035	- name: Pool Size Sensitivity (50/100/200/500)
1036	  plan_id: plan_019
1037	  description: '在 SWE-smith validation 上用 pool={50, 100, 200, 500} 重新评估 M2 best checkpoints，
1038	    测试 strategy ranking 在更 realistic pool sizes 下的稳定性。
1039	
1040	    '
1041	  expected_results:
1042	    qwen:
1043	      pool_50:
1044	        random_R1: 0.545
1045	        embedding_R1: 0.565
1046	        dataflow_R1: 0.555
1047	        embedding_minus_random_pp: 2.0
1048	      pool_100:
1049	        random_R1: 0.428
1050	        embedding_R1: 0.447
1051	        dataflow_R1: 0.438
1052	        embedding_minus_random_pp: 1.9
1053	      pool_200:
1054	        random_R1: 0.342
1055	        embedding_R1: 0.359
1056	        dataflow_R1: 0.351
1057	        embedding_minus_random_pp: 1.7
1058	      pool_500:
1059	        random_R1: 0.261
1060	        embedding_R1: 0.276
1061	        dataflow_R1: 0.269
1062	        embedding_minus_random_pp: 1.5
1063	    starcoder:
1064	      pool_50:
1065	        random_R1: 0.46
1066	        embedding_R1: 0.475
1067	        dataflow_R1: 0.458
1068	        embedding_minus_random_pp: 1.5
1069	      pool_100:
1070	        random_R1: 0.358
1071	        embedding_R1: 0.372
1072	        dataflow_R1: 0.357
1073	        embedding_minus_random_pp: 1.4
1074	      pool_200:
1075	        random_R1: 0.282
1076	        embedding_R1: 0.295
1077	        dataflow_R1: 0.281
1078	        embedding_minus_random_pp: 1.3
1079	      pool_500:
1080	        random_R1: 0.214
1081	        embedding_R1: 0.225
1082	        dataflow_R1: 0.213
1083	        embedding_minus_random_pp: 1.1
1084	    ranking_stable_across_pools: true
1085	    pool_ranking_stable_pct: 100
1086	    delta_shrinkage_rate: ~0.15pp per doubling of pool size
1087	  result_rationale: 'Strategy ranking（embedding > dataflow > random for Qwen; embedding
1088	    > random ≈ dataflow for StarCoder）在 pool 50→500 全程保持稳定（pool_ranking_stable_pct
1089	    = 100%）。 绝对 R@1 随 pool 增大而下降（50→500 约 halved），因为 larger pool = more distractors
1090	    = harder task。Embedding-random delta 从 2.0pp (pool=50) 缓慢缩小至 1.5pp (pool=500)，
1091	    缩小幅度约 25%，但方向和显著性保持。原因：pool=500 时 random negatives 中偶然出现 "hard" negative 的概率增加（base
1092	    rate effect），部分缩小了 mining 策略的差异。 但核心 signal 不消失——embedding mining 在 pool=500 仍有
1093	    +1.5pp Qwen, +1.1pp StarCoder。 Dataflow 在 Qwen 上从 +1.0pp (pool=50) 降至 +0.8pp (pool=500)
1094	    但保持正值。 这直接回应 reviewer "pool=50 unrealistically small" concern：即使 10x pool 扩大，
1095	    strategy ranking 完全不翻转。
1096	
1097	    '
1098	  tables:
1099	  - name: 'Table 12: Pool Size Sensitivity (R@1 %)'
1100	    columns:
1101	    - Pool
1102	    - Encoder
1103	    - random
1104	    - embedding
1105	    - dataflow
1106	    - emb−rand (pp)
1107	    - Ranking
1108	    rows:
1109	    - - 50
1110	      - Qwen
1111	      - 54.5
1112	      - 56.5
1113	      - 55.5
1114	      - '+2.0'
1115	      - E>D>R
1116	    - - 100
1117	      - Qwen
1118	      - 42.8
1119	      - 44.7
1120	      - 43.8
1121	      - '+1.9'
1122	      - E>D>R
1123	    - - 200
1124	      - Qwen
1125	      - 34.2
1126	      - 35.9
1127	      - 35.1
1128	      - '+1.7'
1129	      - E>D>R
1130	    - - 500
1131	      - Qwen
1132	      - 26.1
1133	      - 27.6
1134	      - 26.9
1135	      - '+1.5'
1136	      - E>D>R
1137	    - - 50
1138	      - StarCoder
1139	      - 46.0
1140	      - 47.5
1141	      - 45.8
1142	      - '+1.5'
1143	      - E>R>D
1144	    - - 100
1145	      - StarCoder
1146	      - 35.8
1147	      - 37.2
1148	      - 35.7
1149	      - '+1.4'
1150	      - E>R>D
1151	    - - 200
1152	      - StarCoder
1153	      - 28.2
1154	      - 29.5
1155	      - 28.1
1156	      - '+1.3'
1157	      - E>R≈D
1158	    - - 500
1159	      - StarCoder
1160	      - 21.4
1161	      - 22.5
1162	      - 21.3
1163	      - '+1.1'
1164	      - E>R≈D
1165	  figures_description:
1166	  - 'Fig 10: Pool size (x-axis, log scale) vs R@1 (y-axis) for 3 strategies, separate
1167	    panels for Qwen and StarCoder. Shaded bands between embedding and random lines
1168	    highlight persistent delta.'
1169	  - 'Fig 10b: Delta (embedding − random) vs pool size, showing graceful degradation'
1170	  analysis: Pool size sensitivity 是外部有效性的关键证据。100% ranking stability 在 50→500 全程保持是
1171	    best tier 的标志。Delta 的 graceful degradation（非 collapse）说明 mining strategy 的价值是
1172	    robust 的。论文可以明确声明："Strategy rankings are stable across pool sizes spanning an
1173	    order of magnitude (50–500), with embedding mining maintaining a statistically
1174	    significant advantage even at the largest pool tested."
1175	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b0f1bef3-4cf7-4979-bbbe-3a248efa1e88",
  "isSidechain": true,
  "promptId": "1589742a-41cc-4d40-ae94-dc9d919d6688",
  "agentId": "aae11a3504772ac7f",
  "type": "user",
  "uuid": "860a3d34-957e-4662-87c5-4287f01677b3",
  "sourceToolAssistantUUID": "b0f1bef3-4cf7-4979-bbbe-3a248efa1e88",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "c4036345-91c5-47f2-9c09-36d0f1b82314",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 36 · 2026-05-16T15:06:43.799Z_

Perfect! Now let me search for tier definitions more systematically and check the worst/median review context files:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "860a3d34-957e-4662-87c5-4287f01677b3",
  "isSidechain": true,
  "agentId": "aae11a3504772ac7f",
  "requestId": "req_011Cb6TPzCJj6Lqrjucu4rKX",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a0552417-b43a-4552-950f-cb68bdf8f0bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "c4036345-91c5-47f2-9c09-36d0f1b82314",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01JEVL1QyrsN9kzW4o3kmwSV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 979,
      "cache_creation_input_tokens": 18447,
      "cache_read_input_tokens": 36533,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18447,
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

_source line 37 · 2026-05-16T15:06:44.236Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NnzbLFRYdQaT3ejgZnVUkt`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/worst/review_context.yaml",
  "limit": 150
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a0552417-b43a-4552-950f-cb68bdf8f0bb",
  "isSidechain": true,
  "agentId": "aae11a3504772ac7f",
  "requestId": "req_011Cb6TPzCJj6Lqrjucu4rKX",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "bc4ef9be-aa08-432d-9b56-c8b2ac957d98",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "c4036345-91c5-47f2-9c09-36d0f1b82314",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01JEVL1QyrsN9kzW4o3kmwSV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 979,
      "cache_creation_input_tokens": 18447,
      "cache_read_input_tokens": 36533,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18447,
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

_source line 38 · 2026-05-16T15:06:44.249Z_

<details><summary>↩ Tool result · `toolu_01NnzbLFRYdQaT3ejgZnVUkt`</summary>

```text
1	narrative_guidance: 'Full-scale effect sizes collapse. Embedding-distance mining shows
2	  no reliable advantage over random baselines once multi-seed CIs are computed; dataflow
3	  negatives show no benefit or slight harm on both encoders. BM25 negatives perform
4	  statistically indistinguishable from embedding negatives, preventing closure of
5	  the CoCoHaNeRe correction argument. Pool size scaling destabilizes strategy rankings.
6	  SWE-bench shows no downstream signal. The paper must pivot to a negative-result
7	  framing: "Why Hard Negative Mining Strategies Don''t Differentiate for Code Retrieval
8	  at Scale." The salvageable contribution is the representation geometry analysis
9	  explaining *why* strategies converge (margins collapse post-fine-tuning), plus the
10	  methodological caution about BM25 proxies (downgraded from "correction" to "observation").
11	
12	  '
13	imagined_experiments:
14	- name: M2 Full Qwen 9-seed 3-strategy training
15	  plan_id: plan_002 / m2_full_qwen
16	  description: '9 seeds × 3 strategies (random, embedding_distance, dataflow_aware)
17	    on Qwen2.5-Coder-3B LoRA. Full training data (~44K instances). Pool=50 eval.
18	
19	    '
20	  expected_results:
21	    random_mean_R1: 0.529
22	    random_std_R1: 0.0085
23	    random_95CI:
24	    - 0.5224
25	    - 0.5356
26	    embedding_distance_mean_R1: 0.531
27	    embedding_distance_std_R1: 0.0092
28	    embedding_distance_95CI:
29	    - 0.5239
30	    - 0.5381
31	    dataflow_aware_mean_R1: 0.5245
32	    dataflow_aware_std_R1: 0.011
33	    dataflow_aware_95CI:
34	    - 0.516
35	    - 0.533
36	    emb_minus_random_R1_pp: 0.2
37	    emb_minus_random_CI:
38	    - -0.62
39	    - 1.02
40	    df_minus_random_R1_pp: -0.45
41	    df_minus_random_CI:
42	    - -1.5
43	    - 0.6
44	    best_step_mode: 1000
45	    best_step_range:
46	    - 500
47	    - 1500
48	    overfit_onset_step: 1500
49	  result_rationale: 'Pilot showed emb +2.0pp over random (0.5557 vs 0.5357), but that
50	    was 1 seed on pilot-scale data. At full scale with 9 seeds, seed variance dominates
51	    the small effect. The 2.0pp pilot delta shrinks to ~0.2pp because: (1) full training
52	    data (44K vs pilot subset) gives random negatives more coverage of the embedding
53	    space, reducing the advantage of curated hard negatives; (2) Qwen''s extremely
54	    saturated pretrained space (pos_sim=0.9855) means all strategies produce negatives
55	    that are very close to the query — the margin between random_neg_sim (0.911) and
56	    emb_neg_sim (0.969) gets compressed further during fine-tuning as the encoder
57	    adjusts; (3) with 9 seeds, some seeds favor random (data order effects), some
58	    favor embedding, and the mean converges. The CI clearly includes 0, killing the
59	    claim that embedding mining "consistently improves" retrieval. Dataflow negatives
60	    show slight harm because at full scale, the 34% structural coverage means 66%
61	    of training instances fall back to random, diluting any signal; the structural
62	    negatives for the remaining 34% may be less informative than embedding negatives
63	    (dataflow disconnection doesn''t guarantee semantic difficulty).
64	
65	    '
66	  tables:
67	  - name: 'Table 2: Full-Scale R@1 by Strategy × Encoder (Qwen)'
68	    content: 'Strategy          | Mean R@1 | Std   | 95% CI          | Δ vs Random
69	      | p (paired-t)
70	
71	      ------------------|----------|-------|-----------------|-------------|-------------
72	
73	      random            | 0.5290   | 0.009 | [0.522, 0.536]  | —           | —
74	
75	      embedding_dist    | 0.5310   | 0.009 | [0.524, 0.538]  | +0.20pp     | 0.58
76	
77	      dataflow_aware    | 0.5245   | 0.011 | [0.516, 0.533]  | −0.45pp     | 0.31
78	
79	      '
80	  figures_description:
81	  - Box plot of R@1 across 9 seeds for 3 strategies (Qwen). Boxes heavily overlap.
82	    Median lines for random and embedding nearly coincident. Dataflow median slightly
83	    below but within IQR of both others.
84	  - Learning curves (val_loss vs step) for all 27 runs, color-coded by strategy. All
85	    strategies converge to similar loss band [0.46–0.54] by step 1000, with divergence
86	    only in overfitting tail. No strategy consistently lower.
87	  analysis: 'The pilot''s +2.0pp embedding advantage was a seed-specific fluctuation.
88	    At full scale, the effect is +0.20pp with p=0.58 — no statistical significance.
89	    Dataflow shows a slight negative trend (−0.45pp) but also non-significant. Seed-to-seed
90	    variance (σ ≈ 0.009) exceeds the strategy effect, making it impossible to distinguish
91	    strategies on this encoder. This is consistent with Qwen''s extreme representation
92	    saturation: when pos_sim=0.986, fine-tuning rapidly compresses any initial margin
93	    differences, and all strategies end up in the same loss basin.
94	
95	    '
96	- name: M2 Full StarCoder 9-seed 3-strategy training
97	  plan_id: plan_002 / m2_full_starcoder
98	  description: '9 seeds × 3 strategies on StarCoder2-3B. Same protocol as Qwen.
99	
100	    '
101	  expected_results:
102	    random_mean_R1: 0.443
103	    random_std_R1: 0.0105
104	    random_95CI:
105	    - 0.4349
106	    - 0.4511
107	    embedding_distance_mean_R1: 0.4395
108	    embedding_distance_std_R1: 0.012
109	    embedding_distance_95CI:
110	    - 0.4302
111	    - 0.4488
112	    dataflow_aware_mean_R1: 0.428
113	    dataflow_aware_std_R1: 0.0135
114	    dataflow_aware_95CI:
115	    - 0.4176
116	    - 0.4384
117	    emb_minus_random_R1_pp: -0.35
118	    emb_minus_random_CI:
119	    - -1.4
120	    - 0.7
121	    df_minus_random_R1_pp: -1.5
122	    df_minus_random_CI:
123	    - -3.1
124	    - 0.1
125	    best_step_mode: 1000
126	    overfit_onset_step: 1500
127	  result_rationale: 'StarCoder pilot showed embedding +1.56pp (0.5078 vs 0.4922),
128	    but pilot used post-hoc eval for random (no in-training eval), introducing measurement
129	    inconsistency. At full scale with 9 seeds and consistent eval: (1) StarCoder''s
130	    healthier pretrained geometry (pos_sim=0.80) means random negatives already provide
131	    decent margin (0.194), so embedding mining''s tighter margins (0.067) may actually
132	    hurt by making the contrastive task too hard early in training, causing some seeds
133	    to find worse optima; (2) the higher seed variance for StarCoder (σ=0.012 vs Qwen''s
134	    0.009) reflects the decoder-only architecture''s sensitivity to initialization
135	    — FIM pretraining creates a less smooth loss landscape for retrieval fine-tuning;
136	    (3) dataflow negatives show the most harm (−1.50pp) because StarCoder''s intact
137	    geometry already separates structural from non-structural code well, so forcing
138	    structural discrimination adds noise rather than signal. The CI for embedding
139	    nearly spans zero but slightly favors negative; for dataflow, the CI upper bound
140	    just barely touches zero, suggesting possible marginal harm.
141	
142	    '
143	  tables:
144	  - name: 'Table 2 (continued): Full-Scale R@1 by Strategy × Encoder (StarCoder)'
145	    content: 'Strategy          | Mean R@1 | Std   | 95% CI          | Δ vs Random
146	      | p (paired-t)
147	
148	      ------------------|----------|-------|-----------------|-------------|-------------
149	
150	      random            | 0.4430   | 0.011 | [0.435, 0.451]  | —           | —
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bc4ef9be-aa08-432d-9b56-c8b2ac957d98",
  "isSidechain": true,
  "promptId": "1589742a-41cc-4d40-ae94-dc9d919d6688",
  "agentId": "aae11a3504772ac7f",
  "type": "user",
  "uuid": "9edafe18-e781-46a1-b477-03540db27157",
  "sourceToolAssistantUUID": "bc4ef9be-aa08-432d-9b56-c8b2ac957d98",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "c4036345-91c5-47f2-9c09-36d0f1b82314",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-16T15:06:44.646Z_

<details open><summary>🔧 Tool call — Read · `toolu_011c6aJeMdiSjRbLNhRXWYr9`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/median/review_context.yaml",
  "limit": 150
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9edafe18-e781-46a1-b477-03540db27157",
  "isSidechain": true,
  "agentId": "aae11a3504772ac7f",
  "requestId": "req_011Cb6TPzCJj6Lqrjucu4rKX",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "52916b7b-596f-4205-af1d-2f1ba2a67f60",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "c4036345-91c5-47f2-9c09-36d0f1b82314",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01JEVL1QyrsN9kzW4o3kmwSV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 979,
      "cache_creation_input_tokens": 18447,
      "cache_read_input_tokens": 36533,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18447,
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

_source line 40 · 2026-05-16T15:06:44.652Z_

<details><summary>↩ Tool result · `toolu_011c6aJeMdiSjRbLNhRXWYr9`</summary>

```text
1	narrative_guidance: 'Claim 1 降级为 "tends to help"：embedding mining 方向正确但 effect size
2	  缩水约 50%， 多 seed CI 宽（2–4pp），个别 seed delta < 0.5pp。BM25 baseline 方向一致（harm）但 delta
3	  小且 p > 0.05，CoCoHaNeRe correction 论证从 "empirically verified" 改为 "BM25 proxy 方向一致但
4	  effect size 不足以排除混杂"。Claim 2 降级为 exploratory observation：dataflow 在 Qwen 上 CI 包含
5	  0，StarCoder 上方向为负，合并进 Claim 1 作为 strategy-encoder interaction case。SWE-bench delta
6	  < 1pp 且 CI 包含 0， 无法作为独立 evidence。论文重心移向 systematic empirical comparison + representation
7	  geometry analysis。标题用 "Systematic Study"，定位 analysis paper。
8	
9	  '
10	imagined_experiments:
11	- name: SWE-bench Lite End-to-End Evaluation
12	  plan_id: plan_003
13	  description: 3 strategies × best checkpoint (Qwen), Qwen3.6-27B agent, 300 SWE-bench
14	    Lite instances
15	  expected_results:
16	    random_resolve_rate_pct: 23.0
17	    random_resolved_count: 69
18	    embedding_resolve_rate_pct: 23.7
19	    embedding_resolved_count: 71
20	    dataflow_resolve_rate_pct: 23.3
21	    dataflow_resolved_count: 70
22	    emb_minus_random_delta_pp: 0.7
23	    df_minus_random_delta_pp: 0.3
24	    total_instances: 300
25	    retrieval_R1_on_swebench_random: 0.41
26	    retrieval_R1_on_swebench_embedding: 0.42
27	    retrieval_R1_on_swebench_dataflow: 0.41
28	  result_rationale: 'SWE-bench Lite 的 resolve rate 由 agent 生成能力主导，retrieval 只是 pipeline
29	    的第一步。median 档下 retrieval R@1 delta 仅 ~1pp，传导到 end-to-end 后进一步 衰减：即使 retrieval
30	    多找对 1-2 个 file，agent 是否能利用这个 file 生成正确 patch 是独立的噪声源。300 instances 上 2 个 count
31	    的差异对应 ~0.7pp，远不够 statistical significance。此外 SWE-bench 的 repo 分布与 SWE-smith training
32	    分布有 domain shift， 进一步压缩了 retrieval improvement 的传导效率。
33	
34	    '
35	  tables:
36	  - name: 'Table: SWE-bench Lite Resolve Rate by Strategy'
37	    columns:
38	    - Strategy
39	    - Resolved
40	    - Total
41	    - Rate (%)
42	    - Δ vs Random (pp)
43	    rows:
44	    - - random
45	      - 69
46	      - 300
47	      - 23.0
48	      - —
49	    - - embedding
50	      - 71
51	      - 300
52	      - 23.7
53	      - '+0.7'
54	    - - dataflow
55	      - 70
56	      - 300
57	      - 23.3
58	      - '+0.3'
59	  - name: 'Table: Retrieval-Stage R@1 on SWE-bench Repos'
60	    columns:
61	    - Strategy
62	    - R@1
63	    - R@5
64	    rows:
65	    - - random
66	      - 0.41
67	      - 0.78
68	    - - embedding
69	      - 0.42
70	      - 0.79
71	    - - dataflow
72	      - 0.41
73	      - 0.78
74	  figures_description:
75	  - 'Bar chart: resolve rate by strategy with 95% bootstrap CI error bars. All three
76	    bars overlap heavily, CI bands span ~4pp each.'
77	  - 'Scatter plot: per-instance retrieval correctness vs resolve outcome, colored
78	    by strategy. Shows that retrieval success is necessary but not sufficient — many
79	    correctly-retrieved instances still fail at generation.'
80	  analysis: 'SWE-bench delta 不足以支撑独立 claim。resolve rate 差异 < 1pp，在 N=300 上无统计 显著性（见
81	    plan_016）。Retrieval-stage R@1 差异同样微小（~1pp），说明 SWE-smith 到 SWE-bench 的 domain gap
82	    进一步压平了 strategy 差异。论文中应作为 "sanity check" 而非 primary evidence 呈现：确认 negative mining
83	    策略不 harm downstream performance， 但不能 claim 显著 improvement。需在 limitation 中讨论 300
84	    instances 的 power 不足问题。
85	
86	    '
87	- name: RepoBench-R Cross-File Retrieval Evaluation
88	  plan_id: plan_004
89	  description: 3 strategies × 3 seeds × 2 encoders, RepoBench-R test_easy (8K, pool~6)
90	    + test_hard (8K, pool~18), with 95% CIs
91	  expected_results:
92	    qwen_test_easy:
93	      random_R1_mean: 0.682
94	      embedding_R1_mean: 0.688
95	      dataflow_R1_mean: 0.685
96	      emb_minus_random_pp: 0.6
97	      emb_minus_random_CI:
98	      - -0.2
99	      - 1.4
100	    qwen_test_hard:
101	      random_R1_mean: 0.394
102	      embedding_R1_mean: 0.404
103	      dataflow_R1_mean: 0.398
104	      emb_minus_random_pp: 1.0
105	      emb_minus_random_CI:
106	      - -0.1
107	      - 2.1
108	    starcoder_test_easy:
109	      random_R1_mean: 0.621
110	      embedding_R1_mean: 0.626
111	      dataflow_R1_mean: 0.618
112	      emb_minus_random_pp: 0.5
113	      emb_minus_random_CI:
114	      - -0.3
115	      - 1.3
116	    starcoder_test_hard:
117	      random_R1_mean: 0.338
118	      embedding_R1_mean: 0.346
119	      dataflow_R1_mean: 0.333
120	      emb_minus_random_pp: 0.8
121	      emb_minus_random_CI:
122	      - -0.4
123	      - 2.0
124	    overall_delta_pp_range:
125	    - 0.0
126	    - 1.5
127	  result_rationale: 'RepoBench-R 的 test_easy pool 仅 ~6 candidates，所有策略接近 ceiling，strategy
128	    差异被压缩到 < 1pp。test_hard pool ~18 提供更多区分空间，delta 稍大（~1pp）但仍在 CI 包含 0 的边缘。RepoBench-R
129	    与 SWE-smith 的 task 定义不同（cross-file completion vs bug-fix retrieval），domain shift
130	    进一步削弱了 training-time strategy 差异的 传导。8K instances 的大样本量使 per-strategy CI 较窄（~1.5pp
131	    width），但 delta 的 CI 仍 ~2pp width，因为 strategy 间的 paired variance 较大。Dataflow 在
132	    StarCoder 上一致为负（-0.5pp），符合 pilot 发现的 encoder-strategy interaction pattern。
133	
134	    '
135	  tables:
136	  - name: 'Table: RepoBench-R R@1 by Strategy × Encoder × Difficulty'
137	    columns:
138	    - Encoder
139	    - Split
140	    - Random
141	    - Embedding
142	    - Dataflow
143	    - Emb Δ (pp)
144	    - DF Δ (pp)
145	    rows:
146	    - - Qwen
147	      - easy
148	      - 68.2 ± 0.7
149	      - 68.8 ± 0.8
150	      - 68.5 ± 0.9
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "52916b7b-596f-4205-af1d-2f1ba2a67f60",
  "isSidechain": true,
  "promptId": "1589742a-41cc-4d40-ae94-dc9d919d6688",
  "agentId": "aae11a3504772ac7f",
  "type": "user",
  "uuid": "6cabdda2-12da-4a37-a53f-600146c4472d",
  "sourceToolAssistantUUID": "52916b7b-596f-4205-af1d-2f1ba2a67f60",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "c4036345-91c5-47f2-9c09-36d0f1b82314",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-16T15:06:44.922Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01DmkRJioJ37a6XZoDs9orvK`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports -type f -name \"imagined_experiments.yaml\" | xargs ls -la"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6cabdda2-12da-4a37-a53f-600146c4472d",
  "isSidechain": true,
  "agentId": "aae11a3504772ac7f",
  "requestId": "req_011Cb6TPzCJj6Lqrjucu4rKX",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "6ce70643-e592-49f1-991f-17555f45acdf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "c4036345-91c5-47f2-9c09-36d0f1b82314",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01JEVL1QyrsN9kzW4o3kmwSV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 979,
      "cache_creation_input_tokens": 18447,
      "cache_read_input_tokens": 36533,
      "output_tokens": 331,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 18447
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 979,
          "output_tokens": 331,
          "cache_read_input_tokens": 36533,
          "cache_creation_input_tokens": 18447,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 18447,
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

_source line 42 · 2026-05-16T15:06:44.987Z_

<details><summary>↩ Tool result · `toolu_01DmkRJioJ37a6XZoDs9orvK`</summary>

```text
-rw-r--r-- 1 ubuntu ubuntu 32194 May 12 20:57 /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260512T204322/best/imagined_experiments.yaml
-rw-r--r-- 1 ubuntu ubuntu 30972 May 12 21:01 /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260512T204322/median/imagined_experiments.yaml
-rw-r--r-- 1 ubuntu ubuntu 28926 May 12 21:05 /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260512T204322/worst/imagined_experiments.yaml
-rw-r--r-- 1 ubuntu ubuntu 30977 May 14 08:11 /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/best/imagined_experiments.yaml
-rw-r--r-- 1 ubuntu ubuntu 24670 May 14 08:15 /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/median/imagined_experiments.yaml
-rw-r--r-- 1 ubuntu ubuntu 39409 May 14 08:19 /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T075732/worst/imagined_experiments.yaml
-rw-r--r-- 1 ubuntu ubuntu 41116 May 14 16:45 /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/best/imagined_experiments.yaml
-rw-r--r-- 1 ubuntu ubuntu 44357 May 14 16:50 /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/median/imagined_experiments.yaml
-rw-r--r-- 1 ubuntu ubuntu 54214 May 14 16:54 /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/worst/imagined_experiments.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6ce70643-e592-49f1-991f-17555f45acdf",
  "isSidechain": true,
  "promptId": "1589742a-41cc-4d40-ae94-dc9d919d6688",
  "agentId": "aae11a3504772ac7f",
  "type": "user",
  "uuid": "3a8b9dcf-0454-4335-b37c-3243c76a7963",
  "sourceToolAssistantUUID": "6ce70643-e592-49f1-991f-17555f45acdf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "c4036345-91c5-47f2-9c09-36d0f1b82314",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 43 · 2026-05-16T15:06:46.162Z_

Let me read the manifest file to understand the tier structure better:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3a8b9dcf-0454-4335-b37c-3243c76a7963",
  "isSidechain": true,
  "agentId": "aae11a3504772ac7f",
  "requestId": "req_011Cb6TQCWEGVqy9ckMkiHow",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "cfacadf8-5a43-46bb-85bc-7a86529238d9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "c4036345-91c5-47f2-9c09-36d0f1b82314",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SXUTiCaAMk2hzo55Kh3Xb8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 7094,
      "cache_read_input_tokens": 54980,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7094,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 44 · 2026-05-16T15:06:46.602Z_

<details open><summary>🔧 Tool call — Read · `toolu_01AXFvCvJXqR7ZHV5WXfWTZH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/manifest.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cfacadf8-5a43-46bb-85bc-7a86529238d9",
  "isSidechain": true,
  "agentId": "aae11a3504772ac7f",
  "requestId": "req_011Cb6TQCWEGVqy9ckMkiHow",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b8bd2c65-a1a1-4541-8292-d943318ae9ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "c4036345-91c5-47f2-9c09-36d0f1b82314",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SXUTiCaAMk2hzo55Kh3Xb8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 7094,
      "cache_read_input_tokens": 54980,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7094,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 45 · 2026-05-16T15:06:46.914Z_

<details open><summary>🔧 Tool call — Bash · `toolu_016vwWEvgqAXiv2bmx46DWUJ`</summary>

```json
{
  "command": "head -100 /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/registry.yaml | grep -A 5 -B 5 \"status\\|tier\\|best\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b8bd2c65-a1a1-4541-8292-d943318ae9ba",
  "isSidechain": true,
  "agentId": "aae11a3504772ac7f",
  "requestId": "req_011Cb6TQCWEGVqy9ckMkiHow",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a41e4b0c-f2b5-4606-bff6-e84677989c5c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "c4036345-91c5-47f2-9c09-36d0f1b82314",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SXUTiCaAMk2hzo55Kh3Xb8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 7094,
      "cache_read_input_tokens": 54980,
      "output_tokens": 189,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7094
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 189,
          "cache_read_input_tokens": 54980,
          "cache_creation_input_tokens": 7094,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7094,
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

_source line 46 · 2026-05-16T15:06:46.968Z_

<details><summary>↩ Tool result · `toolu_01AXFvCvJXqR7ZHV5WXfWTZH`</summary>

```text
1	- id: art_20260512_b890e8
2	  name: contrastive_model.py
3	  type: intermediate
4	  description: StructFuse bi-encoder contrastive model with InfoNCE loss, weighted
5	    positives, fusion head, LoRA support
6	  path: projects/structfuse-context/artifacts/_project/intermediate/contrastive_model.py
7	  url: null
8	  project: structfuse-context
9	  exp_id: null
10	  skill: ''
11	  created_at: '2026-05-12T10:04:16.728617+00:00'
12	  tags:
13	  - structfuse
14	  - training
15	  - stage2
16	- id: art_20260512_a7cf03
17	  name: StructFuse call_graph.ql
18	  type: intermediate
19	  description: CodeQL query for 2-hop call graph extraction from buggy function (Phase
20	    1a)
21	  path: projects/structfuse-context/artifacts/_project/intermediate/call_graph.ql
22	  url: null
23	  project: structfuse-context
24	  exp_id: null
25	  skill: ''
26	  created_at: '2026-05-12T10:04:17.924200+00:00'
27	  tags:
28	  - structfuse
29	  - stage1
30	  - codeql
31	- id: art_20260512_a82ef6
32	  name: hard_negative_mining.py
33	  type: intermediate
34	  description: 'Data-flow-aware hard negative mining: random / embedding-distance
35	    / dataflow-aware strategies'
36	  path: projects/structfuse-context/artifacts/_project/intermediate/hard_negative_mining.py
37	  url: null
38	  project: structfuse-context
39	  exp_id: null
40	  skill: ''
41	  created_at: '2026-05-12T10:04:18.671317+00:00'
42	  tags:
43	  - structfuse
44	  - training
45	  - stage2
46	- id: art_20260512_99f4ec
47	  name: StructFuse bounded_dataflow.ql
48	  type: intermediate
49	  description: CodeQL query for scope-bounded inter-procedural data-flow analysis
50	    (Phase 1b)
51	  path: projects/structfuse-context/artifacts/_project/intermediate/bounded_dataflow.ql
52	  url: null
53	  project: structfuse-context
54	  exp_id: null
55	  skill: ''
56	  created_at: '2026-05-12T10:04:19.846492+00:00'
57	  tags:
58	  - structfuse
59	  - stage1
60	  - codeql
61	  - dataflow
62	- id: art_20260512_2c1b69
63	  name: train.py
64	  type: intermediate
65	  description: 'StructFuse training entry: Accelerate, W&B, dynamic negative mining,
66	    eval loop, checkpoint saving'
67	  path: projects/structfuse-context/artifacts/_project/intermediate/train.py
68	  url: null
69	  project: structfuse-context
70	  exp_id: null
71	  skill: ''
72	  created_at: '2026-05-12T10:04:20.628765+00:00'
73	  tags:
74	  - structfuse
75	  - training
76	  - stage2
77	- id: art_20260512_21d6b6
78	  name: StructFuse extract_dataflow.py
79	  type: intermediate
80	  description: 'Main extraction pipeline: CodeQL 2-phase analysis with Beniget fallback,
81	    multiprocessing parallel, JSONL output'
82	  path: projects/structfuse-context/artifacts/_project/intermediate/extract_dataflow.py
83	  url: null
84	  project: structfuse-context
85	  exp_id: null
86	  skill: ''
87	  created_at: '2026-05-12T10:04:22.339431+00:00'
88	  tags:
89	  - structfuse
90	  - stage1
91	  - extraction
92	  - pipeline
93	- id: art_20260512_51f682
94	  name: StructFuse build_training_data.py
95	  type: intermediate
96	  description: 'Contrastive training data builder: BM25 hard negatives, feature vectors,
97	    HuggingFace-compatible JSONL output'
98	  path: projects/structfuse-context/artifacts/_project/intermediate/build_training_data.py
99	  url: null
100	  project: structfuse-context
101	  exp_id: null
102	  skill: ''
103	  created_at: '2026-05-12T10:04:23.854442+00:00'
104	  tags:
105	  - structfuse
106	  - stage1
107	  - training-data
108	  - contrastive
109	- id: art_20260512_8aef33
110	  name: eval_retrieval.py
111	  type: data
112	  description: 'StructFuse retrieval evaluation script: Recall@k, MRR, Structural
113	    Precision on SWE-bench Lite / RepoBench-R / custom sets. Supports BM25 baseline,
114	    data-flow filter, fusion re-ranking, multi-model comparison.'
115	  path: projects/structfuse-context/artifacts/_project/data/eval_retrieval.py
116	  url: null
117	  project: structfuse-context
118	  exp_id: null
119	  skill: ''
120	  created_at: '2026-05-12T10:05:00.289408+00:00'
121	  tags:
122	  - evaluation
123	  - retrieval
124	  - structfuse
125	  - stage3
126	- id: art_20260512_033304
127	  name: eval_swebench.py
128	  type: data
129	  description: 'StructFuse SWE-bench end-to-end evaluation: issue -> StructFuse retrieval
130	    -> Qwen3.6-27B patch generation (vLLM) -> harness evaluation. Supports resume,
131	    per-instance logging, Pass@1 summary.'
132	  path: projects/structfuse-context/artifacts/_project/data/eval_swebench.py
133	  url: null
134	  project: structfuse-context
135	  exp_id: null
136	  skill: ''
137	  created_at: '2026-05-12T10:05:05.302147+00:00'
138	  tags:
139	  - evaluation
140	  - swebench
141	  - structfuse
142	  - e2e
143	  - stage3
144	- id: art_20260512_e5f41c
145	  name: requirements.txt
146	  type: data
147	  description: 'StructFuse project Python dependencies: torch, transformers, rank-bm25,
148	    faiss-cpu, vllm, etc.'
149	  path: projects/structfuse-context/artifacts/_project/data/requirements.txt
150	  url: null
151	  project: structfuse-context
152	  exp_id: null
153	  skill: ''
154	  created_at: '2026-05-12T10:05:05.480895+00:00'
155	  tags:
156	  - dependencies
157	  - structfuse
158	- id: art_20260512_7277a2
159	  name: MVP Phase 1 Report
160	  type: report
161	  description: 'MVP Phase 1 CodeQL feasibility + H2 sanity check results: timeout
162	    0%, connected files coverage 1.44% vs disconnected 0%, Fisher p=0.0000. Both PASS.'
163	  path: projects/structfuse-context/artifacts/mvp_p1_codeql_feasibility/report/mvp_phase1_report.md
164	  url: null
165	  project: structfuse-context
166	  exp_id: mvp_p1_codeql_feasibility
167	  skill: ''
168	  created_at: '2026-05-12T11:31:28.845286+00:00'
169	  tags:
170	  - mvp
171	  - phase1
172	  - codeql
173	  - h2
174	  - pass
175	- id: art_20260512_434371
176	  name: phase2a_linear_proxy_results
177	  type: report
178	  description: 'Phase 2a linear proxy validation - PASS: DataFlow+BM25 beats BM25-only
179	    on F1/AUC/MRR. Gold file rank improved from 16→3 (flask), 4→1 (requests), 31→3
180	    (pytest).'
181	  path: projects/structfuse-context/artifacts/_project/report/phase2a_linear_proxy_results.txt
182	  url: null
183	  project: structfuse-context
184	  exp_id: null
185	  skill: ''
186	  created_at: '2026-05-12T11:40:32.570898+00:00'
187	  tags:
188	  - mvp
189	  - phase2a
190	  - evaluation
191	  - pass
192	- id: art_20260512_6211d5
193	  name: failure_diagnosis
194	  type: report
195	  description: mvp_p2b_contrastive_training 失败诊断：Run 2/9 因 ModelScope 并发下载导致模型 safetensors
196	    文件缺失
197	  path: projects/structfuse-context/artifacts/mvp_p2b_contrastive_training/report/failure_diagnosis.md
198	  url: null
199	  project: structfuse-context
200	  exp_id: mvp_p2b_contrastive_training
201	  skill: ''
202	  created_at: '2026-05-12T13:19:19.831877+00:00'
203	  tags:
204	  - diagnosis
205	  - failure
206	  - modelscope
207	- id: art_20260512_cf23fc
208	  name: 50-repo overlap experiment results
209	  type: report
210	  description: 50-repo CodeQL 2-hop call_graph overlap experiment on SWE-smith data.
211	    Validates that connected-but-not-gold files exist at scale (Z=40.8% >> 20% threshold),
212	    confirming original StructFuse method is viable.
213	  path: projects/structfuse-context/artifacts/_project/report/50repo_overlap_report.md
214	  url: null
215	  project: structfuse-context
216	  exp_id: null
217	  skill: ''
218	  created_at: '2026-05-12T20:36:49.021879+00:00'
219	  tags:
220	  - experiment
221	  - codeql
222	  - overlap
223	  - validation
224	- id: art_20260513_240352
225	  name: plan_006_scalability_stats_29repos
226	  type: data
227	  description: 'M1 scalability statistics from 29/131 repos (8171 instances): extraction
228	    time, timeout rate, coverage, Z% by repo size. For plan_006.'
229	  path: projects/structfuse-context/artifacts/_project/data/plan_006_scalability_stats_29repos.json
230	  url: null
231	  project: structfuse-context
232	  exp_id: null
233	  skill: ''
234	  created_at: '2026-05-13T04:24:15.343120+00:00'
235	  tags:
236	  - plan_006
237	  - scalability
238	  - m1_extraction
239	- id: art_20260513_ef3ab0
240	  name: plan_006_scalability_summary
241	  type: report
242	  description: 'Plan 006 M1 extraction scalability stats (29/131 repos): Z% by size,
243	    extraction perf, zero-Z repos, key findings for paper Discussion'
244	  path: projects/structfuse-context/artifacts/_project/report/scalability_summary.md
245	  url: null
246	  project: structfuse-context
247	  exp_id: null
248	  skill: ''
249	  created_at: '2026-05-13T06:18:14.578259+00:00'
250	  tags:
251	  - plan_006
252	  - scalability
253	  - m1_extraction
254	- id: art_20260513_eaf24b
255	  name: plan_006_scalability_data
256	  type: data
257	  description: 'Structured JSON for plan_006 scalability visualization: by_size, extraction_time,
258	    zero_z_repos, per_repo breakdown (29 repos)'
259	  path: projects/structfuse-context/artifacts/_project/data/scalability_data.json
260	  url: null
261	  project: structfuse-context
262	  exp_id: null
263	  skill: ''
264	  created_at: '2026-05-13T06:18:16.617467+00:00'
265	  tags:
266	  - plan_006
267	  - scalability
268	  - m1_extraction
269	  - visualization
270	- id: art_20260513_2d4eb4
271	  name: pilot_results_summary
272	  type: report
273	  description: StructFuse pilot results summary - Qwen2.5-Coder-3B and StarCoder2-3B
274	    eval metrics across random/embedding/dataflow strategies
275	  path: projects/structfuse-context/artifacts/_project/report/pilot_results_summary.md
276	  url: null
277	  project: structfuse-context
278	  exp_id: null
279	  skill: ''
280	  created_at: '2026-05-13T10:34:49.209382+00:00'
281	  tags:
282	  - pilot
283	  - eval
284	  - results
285	- id: art_20260513_85049a
286	  name: pilot_results_data
287	  type: data
288	  description: StructFuse pilot results structured JSON - full eval history, checkpoint
289	    paths, training config. File at bjb1-42106:/root/structfuse/results/pilot_results.json
290	  path: projects/structfuse-context/artifacts/_project/data/pilot_results.json
291	  url: null
292	  project: structfuse-context
293	  exp_id: null
294	  skill: ''
295	  created_at: '2026-05-13T10:35:26.154352+00:00'
296	  tags:
297	  - pilot
298	  - eval
299	  - results
300	  - json
301	- id: art_20260513_229113
302	  name: cross_encoder_analysis
303	  type: intermediate
304	  description: 'Cross-encoder comparison script: Qwen2.5-Coder-3B vs StarCoder2-3B,
305	    generates Markdown/LaTeX tables, strategy deltas, ranking consistency analysis,
306	    and auto-narrative.'
307	  path: projects/structfuse-context/artifacts/_project/intermediate/cross_encoder_analysis.py
308	  url: null
309	  project: structfuse-context
310	  exp_id: null
311	  skill: ''
312	  created_at: '2026-05-13T10:42:10.274341+00:00'
313	  tags:
314	  - analysis
315	  - cross-encoder
316	  - comparison
317	  - m2_embed_verify
318	  - plan_013_starcoder
319	- id: art_20260513_46f013
320	  name: run_full_m2_training
321	  type: intermediate
322	  description: 全量 M2 单次训练 wrapper 脚本，接受 (strategy, seed, gpu_id) 参数运行一个训练任务
323	  path: projects/structfuse-context/artifacts/_project/intermediate/run_full_m2_training.sh
324	  url: null
325	  project: structfuse-context
326	  exp_id: null
327	  skill: ''
328	  created_at: '2026-05-13T10:45:57.693370+00:00'
329	  tags:
330	  - m2
331	  - training
332	  - full
333	  - script
334	- id: art_20260513_d36f2f
335	  name: schedule_m2_runs
336	  type: intermediate
337	  description: 全量 M2 双卡调度脚本，9 runs (3 strategies × 3 seeds) 均衡分配到 GPU0/GPU1
338	  path: projects/structfuse-context/artifacts/_project/intermediate/schedule_m2_runs.sh
339	  url: null
340	  project: structfuse-context
341	  exp_id: null
342	  skill: ''
343	  created_at: '2026-05-13T10:45:59.748163+00:00'
344	  tags:
345	  - m2
346	  - training
347	  - full
348	  - scheduler
349	- id: art_20260513_64aa24
350	  name: pilot_results_summary
351	  type: report
352	  description: StructFuse pilot experiment results summary - Qwen2.5-Coder-3B and
353	    StarCoder2-3B across random/embedding/dataflow strategies with complete metrics
354	  path: projects/structfuse-context/artifacts/_project/report/pilot_results_summary_64aa24.md
355	  url: null
356	  project: structfuse-context
357	  exp_id: null
358	  skill: ''
359	  created_at: '2026-05-13T11:52:02.987195+00:00'
360	  tags:
361	  - pilot
362	  - results
363	  - metrics
364	  - qwen
365	  - starcoder
366	- id: art_20260513_920f68
367	  name: pilot_results
368	  type: data
369	  description: StructFuse pilot structured results JSON - complete metrics for all
370	    encoder/strategy combinations
371	  path: projects/structfuse-context/artifacts/_project/data/pilot_results_920f68.json
372	  url: null
373	  project: structfuse-context
374	  exp_id: null
375	  skill: ''
376	  created_at: '2026-05-13T11:52:04.578072+00:00'
377	  tags:
378	  - pilot
379	  - results
380	  - structured-data
381	  - json
382	- id: art_20260513_a8c683
383	  name: full_z_percent_stats
384	  type: data
385	  description: Full M1 Z% statistics (123 repos, 44173 instances). 条件 Z%=78.0%, 全量
386	    Z%=26.8%. Per-repo breakdown.
387	  path: projects/structfuse-context/artifacts/plan_006_scalability/data/full_z_percent_stats.json
388	  url: null
389	  project: structfuse-context
390	  exp_id: plan_006_scalability
391	  skill: ''
392	  created_at: '2026-05-13T16:34:07.365228+00:00'
393	  tags:
394	  - z-percent
395	  - m1
396	  - scalability
397	- id: art_20260513_c3956f
398	  name: m2_full_qwen_wrapper_script
399	  type: intermediate
400	  description: Wrapper shell script for 9 sequential M2 full Qwen training runs (3
401	    strategies × 3 seeds). set -eo pipefail, dual checkpoint, WANDB_CONSOLE=off, direct
402	    file redirect.
403	  path: projects/structfuse-context/artifacts/m2_full_qwen/intermediate/run_m2_full_qwen.sh
404	  url: null
405	  project: structfuse-context
406	  exp_id: m2_full_qwen
407	  skill: ''
408	  created_at: '2026-05-13T16:56:34.582285+00:00'
409	  tags:
410	  - training
411	  - shell-script
412	  - m2
413	- id: art_20260513_466352
414	  name: plan006_full_scalability
415	  type: data
416	  description: 'Full M1 scalability statistics: 44173 instances across 123 repos,
417	    stratified by repo size tier'
418	  path: projects/structfuse-context/artifacts/plan_006_scalability/data/plan006_full_scalability.json
419	  url: null
420	  project: structfuse-context
421	  exp_id: plan_006_scalability
422	  skill: ''
423	  created_at: '2026-05-13T18:48:55.784862+00:00'
424	  tags:
425	  - m1
426	  - scalability
427	  - full-run
428	  - statistics
429	- id: art_20260513_d262da
430	  name: plan006_error_patterns
431	  type: data
432	  description: 'M1 extraction error pattern analysis: all 28,276 errors (64%) are
433	    buggy_file_not_found - upstream SWE-smith data issue, not CodeQL failure. 82/123
434	    repos affected, 36 repos with >90% error rate.'
435	  path: projects/structfuse-context/artifacts/plan_006_scalability/data/plan006_error_patterns.json
436	  url: null
437	  project: structfuse-context
438	  exp_id: plan_006_scalability
439	  skill: ''
440	  created_at: '2026-05-13T19:05:43.898730+00:00'
441	  tags:
442	  - error-analysis
443	  - m1-extraction
444	  - limitation
445	- id: art_20260513_ca0458
446	  name: negative_difficulty_charts
447	  type: chart
448	  description: 'Negative difficulty distribution histograms (3 figures: Qwen, StarCoder,
449	    Cross-encoder comparison). Server: bjb1-42106:/root/autodl-tmp/structfuse/artifacts/negative_difficulty_{qwen,starcoder,comparison}.{pdf,png}'
450	  path: projects/structfuse-context/artifacts/_project/chart/negative_difficulty_charts_index.txt
451	  url: null
452	  project: structfuse-context
453	  exp_id: null
454	  skill: ''
455	  created_at: '2026-05-13T19:08:02.266021+00:00'
456	  tags:
457	  - analysis
458	  - negative_mining
459	  - visualization
460	- id: art_20260513_12311f
461	  name: negative_difficulty_stats
462	  type: data
463	  description: 'Negative difficulty distribution stats: cosine similarity between
464	    query-negative pairs using pretrained Qwen2.5-Coder-3B and StarCoder2-3B across
465	    3 mining strategies. 50 queries x 20 negatives per strategy.'
466	  path: projects/structfuse-context/artifacts/_project/data/negative_difficulty_stats.txt
467	  url: null
468	  project: structfuse-context
469	  exp_id: null
470	  skill: ''
471	  created_at: '2026-05-13T19:08:26.878004+00:00'
472	  tags:
473	  - analysis
474	  - negative_mining
475	  - difficulty_distribution
476	- id: art_20260513_68a365
477	  name: negative_difficulty_margin_charts
478	  type: chart
479	  description: '3 charts on server: margin distribution, bars (pos/neg/margin), violin
480	    plot. Path: /root/autodl-tmp/structfuse/artifacts/negative_difficulty_margin_*.{png,pdf}'
481	  path: projects/structfuse-context/artifacts/_project/chart/negative_difficulty_margin_charts_index.txt
482	  url: null
483	  project: structfuse-context
484	  exp_id: null
485	  skill: ''
486	  created_at: '2026-05-13T19:29:14.236993+00:00'
487	  tags:
488	  - negative-difficulty
489	  - margin
490	  - chart
491	- id: art_20260513_87bd9a
492	  name: negative_difficulty_stats_v2
493	  type: data
494	  description: Margin analysis (pos_sim, neg_sim, margin) per strategy per encoder.
495	    StarCoder margin 2.5-5.5x larger than Qwen.
496	  path: projects/structfuse-context/artifacts/_project/data/negative_difficulty_stats_v2.txt
497	  url: null
498	  project: structfuse-context
499	  exp_id: null
500	  skill: ''
501	  created_at: '2026-05-13T19:29:29.550385+00:00'
502	  tags:
503	  - negative-difficulty
504	  - margin
505	  - analysis
506	- id: art_20260514_47c425
507	  name: neg_difficulty_margin_comparison
508	  type: chart
509	  description: 论文级双面板图：Qwen vs StarCoder negative difficulty margin对比（stacked bar,
510	    3 strategies × 2 encoders, 2048-token data）。展示 Qwen 表征饱和（margin 0.017~0.074）vs
511	    StarCoder 健康（margin 0.067~0.194）。
512	  path: projects/structfuse-context/artifacts/neg_difficulty_analysis/chart/neg_difficulty_margin_comparison_meta.txt
513	  url: null
514	  project: structfuse-context
515	  exp_id: neg_difficulty_analysis
516	  skill: draw-paper-figure
517	  created_at: '2026-05-14T01:48:29.287483+00:00'
518	  tags:
519	  - paper
520	  - visualization
521	  - neg_difficulty
522	  - margin
523	- id: art_20260514_f75270
524	  name: m2_full_qwen_analysis
525	  type: report
526	  description: m2_full_qwen 实验分析：9 runs 中仅 random_s42 完成，best R@1=0.5527 (step 1000)，其余
527	    8 runs 未完成
528	  path: projects/structfuse-context/artifacts/m2_full_qwen/report/m2_full_qwen_analysis.md
529	  url: null
530	  project: structfuse-context
531	  exp_id: m2_full_qwen
532	  skill: ''
533	  created_at: '2026-05-14T11:30:04.261359+00:00'
534	  tags:
535	  - m2
536	  - qwen
537	  - experiment-analysis
538	  - incomplete
539	- id: art_20260514_fa81d1
540	  name: m2_starcoder_status_check
541	  type: report
542	  description: 'm2_full_starcoder random_s42 progress diagnostic: step 3700/4242 (87%),
543	    overfitting confirmed, best R@1=0.4604 @step2500'
544	  path: projects/structfuse-context/artifacts/m2_full_starcoder/report/m2_starcoder_status_check.md
545	  url: null
546	  project: structfuse-context
547	  exp_id: m2_full_starcoder
548	  skill: ''
549	  created_at: '2026-05-14T15:19:03.313283+00:00'
550	  tags:
551	  - status-check
552	  - m2
553	  - starcoder
554	  - overfitting
555	- id: art_20260514_b47344
556	  name: plan_015_dynamic_mining_design
557	  type: report
558	  description: 'Plan 015 experiment design: Dynamic vs Static embedding negative mining,
559	    with literature review, experiment variants, GPU overhead estimation, and expected
560	    outcomes for reviewer rebuttal'
561	  path: projects/structfuse-context/artifacts/_project/report/plan_015_dynamic_mining_design.md
562	  url: null
563	  project: structfuse-context
564	  exp_id: null
565	  skill: ''
566	  created_at: '2026-05-14T16:16:57.329092+00:00'
567	  tags:
568	  - plan_015
569	  - experiment_design
570	  - dynamic_mining
571	  - reviewer_response
572	- id: art_20260514_a2e1cd
573	  name: discussion_v2
574	  type: paper
575	  description: Discussion章节v2草稿：5.1 inference-time graph comparison, 5.2 representation
576	    geometry as predictor, 5.3 limitations (5 items), 5.4 future work. ~1086 words,
577	    EMNLP style.
578	  path: projects/structfuse-context/artifacts/_project/paper/discussion_v2.md
579	  url: null
580	  project: structfuse-context
581	  exp_id: null
582	  skill: ''
583	  created_at: '2026-05-14T17:07:27.036510+00:00'
584	  tags:
585	  - plan_017
586	  - discussion
587	  - paper_draft
588	- id: art_20260514_01876a
589	  name: neg_difficulty_margin_comparison
590	  type: chart
591	  description: 主图：2048t下Qwen vs StarCoder margin对比柱状图，标注ratio (2.6×/3.9×/4.1×)。Okabe-Ito配色，300DPI。
592	  path: projects/structfuse-context/artifacts/neg_difficulty_analysis/chart/neg_difficulty_margin_comparison_meta_01876a.txt
593	  url: null
594	  project: structfuse-context
595	  exp_id: neg_difficulty_analysis
596	  skill: ''
597	  created_at: '2026-05-14T17:08:29.200136+00:00'
598	  tags:
599	  - neg_difficulty
600	  - paper_figure
601	  - margin
602	- id: art_20260514_7197a5
603	  name: neg_difficulty_similarity_dist
604	  type: chart
605	  description: 补充图：并排子图展示Qwen/StarCoder的pos_sim和neg_sim grouped bar，箭头标注margin Δ。
606	  path: projects/structfuse-context/artifacts/neg_difficulty_analysis/chart/neg_difficulty_similarity_dist_meta.txt
607	  url: null
608	  project: structfuse-context
609	  exp_id: neg_difficulty_analysis
610	  skill: ''
611	  created_at: '2026-05-14T17:08:31.478220+00:00'
612	  tags:
613	  - neg_difficulty
614	  - paper_figure
615	  - similarity
616	- id: art_20260514_74ea5a
617	  name: neg_difficulty_ratio_heatmap
618	  type: chart
619	  description: Heatmap：2×3 (token length × strategy)，StarCoder/Qwen margin ratio。
620	  path: projects/structfuse-context/artifacts/neg_difficulty_analysis/chart/neg_difficulty_ratio_heatmap_meta.txt
621	  url: null
622	  project: structfuse-context
623	  exp_id: neg_difficulty_analysis
624	  skill: ''
625	  created_at: '2026-05-14T17:08:33.400132+00:00'
626	  tags:
627	  - neg_difficulty
628	  - paper_figure
629	  - heatmap
630	- id: art_20260514_9baf69
631	  name: bm25_overlap_stratified
632	  type: data
633	  description: BM25 vs 各策略 top-7 Jaccard 重叠率按 repo size 分层。Small 0.67, Medium 0.38,
634	    Large 0.30 (vs embedding)。
635	  path: projects/structfuse-context/artifacts/plan_018_bm25/data/bm25_overlap_stratified_meta.txt
636	  url: null
637	  project: structfuse-context
638	  exp_id: plan_018_bm25
639	  skill: ''
640	  created_at: '2026-05-14T17:09:56.271213+00:00'
641	  tags:
642	  - bm25
643	  - overlap
644	  - stratified
645	  - plan_018
646	- id: art_20260514_a50aca
647	  name: experimental_setup_k_checkpoint
648	  type: paper
649	  description: 'Paper paragraph documenting K=7 negatives per query and dual checkpoint
650	    selection protocol, with registry-backed analysis of 7 completed runs (4/7 criteria
651	    agree, divergence pattern: Qwen always agrees, StarCoder always diverges)'
652	  path: projects/structfuse-context/artifacts/_project/paper/experimental_setup_k_checkpoint.md
653	  url: null
654	  project: structfuse-context
655	  exp_id: null
656	  skill: ''
657	  created_at: '2026-05-14T17:55:29.479783+00:00'
658	  tags:
659	  - paper
660	  - experimental-setup
661	  - checkpoint
662	  - K-negatives
663	  - dream-review
664	- id: art_20260514_3008c4
665	  name: v1_v2_changelog
666	  type: report
667	  description: Stratified dry-run v1→v2 差异溯源：根因为 mock_predictions() 使用 hash(strategy)
668	    构造 RNG seed，Python 3 hash randomization 导致跨进程不确定。含完整数值变化表（3 维度 × 3 策略 × 所有 strata）。
669	  path: projects/structfuse-context/artifacts/plan_005_stratified/report/v1_v2_changelog.md
670	  url: null
671	  project: structfuse-context
672	  exp_id: plan_005_stratified
673	  skill: ''
674	  created_at: '2026-05-14T20:40:50.297063+00:00'
675	  tags:
676	  - plan_005
677	  - v1_v2_diff
678	  - changelog
679	  - mock_rng
680	- id: art_20260514_fa94e9
681	  name: related_work_expansion_report
682	  type: report
683	  description: 'Related work expansion: literature_map.yaml 从 ~22 扩展到 37 verified
684	    entries (7 categories)。含 CoCoHaNeRe framing 分析、15 篇新增、2 处修正。'
685	  path: projects/structfuse-context/artifacts/_project/report/related_work_expansion_report.md
686	  url: null
687	  project: structfuse-context
688	  exp_id: null
689	  skill: ''
690	  created_at: '2026-05-14T21:27:25.138825+00:00'
691	  tags:
692	  - literature
693	  - related-work
694	  - CoCoHaNeRe
695	  - paper-framing
696	- id: art_20260514_98650c
697	  name: related_work_v1
698	  type: paper
699	  description: 'Related Work section draft v1 — 3 subsections: Code Retrieval Methods,
700	    Contrastive Learning for Code, Hard Negative Mining (~950 words)'
701	  path: projects/structfuse-context/artifacts/_project/paper/related_work_v1.md
702	  url: null
703	  project: structfuse-context
704	  exp_id: null
705	  skill: ''
706	  created_at: '2026-05-14T22:09:33.655871+00:00'
707	  tags:
708	  - paper
709	  - related-work
710	  - draft
711	- id: art_20260514_a7df8a
712	  name: SWE-bench Lite Dry-Run 预检报告
713	  type: report
714	  description: Plan_003 SWE-bench Lite 评估环境预检：数据、脚本、依赖、磁盘空间、checkpoint 可用性检查结果
715	  path: projects/structfuse-context/artifacts/plan_003/report/swebench_dryrun_report.md
716	  url: null
717	  project: structfuse-context
718	  exp_id: plan_003
719	  skill: ''
720	  created_at: '2026-05-14T22:10:14.564938+00:00'
721	  tags:
722	  - swebench
723	  - dryrun
724	  - precheck
725	- id: art_20260514_dc54a3
726	  name: related_work_v1
727	  type: paper
728	  description: 'Related Work v1 draft — patched: §2.1 "all→these" graph-guided, §2.2
729	    added Sentence-BERT citation, §2.3 added pilot evidence caveat to "consistently
730	    improves"'
731	  path: projects/structfuse-context/artifacts/_project/paper/related_work_v1_dc54a3.md
732	  url: null
733	  project: structfuse-context
734	  exp_id: null
735	  skill: ''
736	  created_at: '2026-05-14T22:45:19.439165+00:00'
737	  tags:
738	  - related-work
739	  - v1
740	  - patched
741	- id: art_20260514_2cb18b
742	  name: introduction_v1
743	  type: paper
744	  description: 'Introduction section draft v1 — 4-paragraph structure: code retrieval
745	    importance, existing gaps (inference-only structure + no systematic negative mining
746	    study), our systematic study challenging gradient-based assumptions, 3 contributions'
747	  path: projects/structfuse-context/artifacts/_project/paper/introduction_v1.md
748	  url: null
749	  project: structfuse-context
750	  exp_id: null
751	  skill: ''
752	  created_at: '2026-05-14T22:47:45.459362+00:00'
753	  tags:
754	  - paper
755	  - introduction
756	  - draft
757	- id: art_20260514_5db688
758	  name: method_v1
759	  type: paper
760	  description: 'Method section draft (§3) with 4 subsections: Problem Formulation,
761	    StructFuse Pipeline, Training Objective, Negative Mining Strategies. ~1200 words,
762	    LaTeX formulas, cite keys aligned with literature_map.yaml.'
763	  path: projects/structfuse-context/artifacts/_project/paper/method_v1.md
764	  url: null
765	  project: structfuse-context
766	  exp_id: null
767	  skill: ''
768	  created_at: '2026-05-14T22:49:00.699349+00:00'
769	  tags:
770	  - paper
771	  - method
772	  - draft-v1
773	- id: art_20260514_25f2bc
774	  name: experiments_v1
775	  type: paper
776	  description: Experiments section draft (§4) with setup, implementation details,
777	    results tables (placeholder), representation geometry analysis (filled), and CodeQL
778	    scalability (filled). ~1400 words.
779	  path: projects/structfuse-context/artifacts/_project/paper/experiments_v1.md
780	  url: null
781	  project: structfuse-context
782	  exp_id: null
783	  skill: ''
784	  created_at: '2026-05-14T22:53:24.173003+00:00'
785	  tags:
786	  - paper
787	  - experiments
788	  - draft
789	- id: art_20260514_c76ce4
790	  name: figure_design_v1
791	  type: paper
792	  description: 论文 Figure 设计稿 v1：8 个 figure 的文字 sketch（pipeline overview、mining strategies
793	    illustration、main results、representation geometry、pool sensitivity、training curves、SWE-bench
794	    downstream、stratified analysis），含布局、数据需求、优先级、production timeline
795	  path: projects/structfuse-context/artifacts/_project/paper/figure_design_v1.md
796	  url: null
797	  project: structfuse-context
798	  exp_id: null
799	  skill: ''
800	  created_at: '2026-05-14T22:56:43.045319+00:00'
801	  tags:
802	  - paper
803	  - figure
804	  - design
805	- id: art_20260514_054f8d
806	  name: experiments_v1
807	  type: paper
808	  description: 'Experiments v1 draft with 5 fixes: (1) Table 6 Total 36.0%→34.3% aligned
809	    to registry, (2) Table 2 updated to R@1 checkpoint values with 4-decimal precision,
810	    (3) SWE-bench→SWE-smith with task→instance expansion explanation, (4) cite key
811	    cocohanere2025→fan2025cocohanere, (5) temperature τ=0.07 marked as learnable'
812	  path: projects/structfuse-context/artifacts/_project/paper/experiments_v1_054f8d.md
813	  url: null
814	  project: structfuse-context
815	  exp_id: null
816	  skill: ''
817	  created_at: '2026-05-14T22:59:57.770391+00:00'
818	  tags:
819	  - paper
820	  - experiments
821	  - v1-fixed
822	- id: art_20260514_144ea2
823	  name: fig4_rep_geometry
824	  type: chart
825	  description: 'Fig 4: Representation Geometry — 2-panel figure. (a) Margin comparison
826	    grouped bar chart showing Qwen vs StarCoder pos-neg margins across 3 negative
827	    strategies with ratio annotations. (b) Similarity distribution box plots highlighting
828	    Qwen ceiling effect vs StarCoder wider spread. PDF vector + 300 DPI PNG.'
829	  path: projects/structfuse-context/artifacts/_project/chart/fig4_rep_geometry.png
830	  url: null
831	  project: structfuse-context
832	  exp_id: null
833	  skill: ''
834	  created_at: '2026-05-14T23:00:39.813252+00:00'
835	  tags:
836	  - paper
837	  - figure
838	  - neg_difficulty
839	  - representation_geometry
840	- id: art_20260514_8f65d6
841	  name: fig4_rep_geometry_pdf
842	  type: chart
843	  description: Fig 4 vector PDF version for LaTeX inclusion.
844	  path: projects/structfuse-context/artifacts/_project/chart/fig4_rep_geometry.pdf
845	  url: null
846	  project: structfuse-context
847	  exp_id: null
848	  skill: ''
849	  created_at: '2026-05-14T23:00:42.196239+00:00'
850	  tags:
851	  - paper
852	  - figure
853	  - pdf
854	- id: art_20260514_999157
855	  name: fig4_rep_geometry_script
856	  type: intermediate
857	  description: Plotting script for Fig 4 Representation Geometry figure. Self-contained,
858	    uses hardcoded data from neg_difficulty_analysis.
859	  path: projects/structfuse-context/artifacts/_project/intermediate/fig4_rep_geometry.py
860	  url: null
861	  project: structfuse-context
862	  exp_id: null
863	  skill: ''
864	  created_at: '2026-05-14T23:00:44.013645+00:00'
865	  tags:
866	  - paper
867	  - script
868	- id: art_20260514_3cf111
869	  name: method_v1
870	  type: paper
871	  description: 'Method section v1 with 6 fixes: projection head corrected to two-layer
872	    MLP+GELU, mean pooling described, pos_weight mechanism documented (uniform distance→unweighted
873	    InfoNCE), epoch strategy corrected (2 epochs + early stopping, s42 uses 3), L2
874	    normalization added, FusionHead confirmed absent.'
875	  path: projects/structfuse-context/artifacts/_project/paper/method_v1_3cf111.md
876	  url: null
877	  project: structfuse-context
878	  exp_id: null
879	  skill: ''
880	  created_at: '2026-05-14T23:03:27.091555+00:00'
881	  tags:
882	  - paper
883	  - method
884	  - v1-fixed
885	- id: art_20260514_ce3556
886	  name: method_v1
887	  type: paper
888	  description: '§3 Method draft — fixed fallback rate from 34% to 66% (line 63): 34.3%
889	    is structural coverage, ~66% lack structural data and fall back to embedding-distance
890	    negatives.'
891	  path: projects/structfuse-context/artifacts/_project/paper/method_v1_ce3556.md
892	  url: null
893	  project: structfuse-context
894	  exp_id: null
895	  skill: ''
896	  created_at: '2026-05-14T23:12:01.790814+00:00'
897	  tags:
898	  - paper-draft
899	  - method
900	  - bugfix
901	- id: art_20260514_eccca0
902	  name: experiments_v1 (round 2 fixes)
903	  type: paper
904	  description: 'Experiments v1 second-round fixes: 3 warnings (Table 6 repo count
905	    87 vs 123, strategy count 3 core + BM25 supplementary, projection head/pooling
906	    synced with method_v1) + 2 info items (structural instance count 15133, pilot
907	    "confirmed at full scale" → pending M2)'
908	  path: projects/structfuse-context/artifacts/_project/paper/experiments_v1_eccca0.md
909	  url: null
910	  project: structfuse-context
911	  exp_id: null
912	  skill: ''
913	  created_at: '2026-05-14T23:12:33.473818+00:00'
914	  tags:
915	  - paper
916	  - experiments
917	  - round2-fixes
918	- id: art_20260514_bcd130
919	  name: experiments_v1
920	  type: paper
921	  description: Experiments section draft v1 — fixed Table 6 repo counts (87→123) and
922	    tier label (files→instances)
923	  path: projects/structfuse-context/artifacts/_project/paper/experiments_v1_bcd130.md
924	  url: null
925	  project: structfuse-context
926	  exp_id: null
927	  skill: ''
928	  created_at: '2026-05-14T23:24:52.486733+00:00'
929	  tags:
930	  - paper
931	  - experiments
932	  - table6-fix
933	- id: art_20260514_d4b180
934	  name: experiments_v1
935	  type: paper
936	  description: 标记 Table 6 和 structural count 为 pending recalc，等待 m1_reextract_v2 完成后统一重算
937	  path: projects/structfuse-context/artifacts/_project/paper/experiments_v1_d4b180.md
938	  url: null
939	  project: structfuse-context
940	  exp_id: null
941	  skill: ''
942	  created_at: '2026-05-14T23:30:40.862339+00:00'
943	  tags:
944	  - pending-recalc
945	  - table6
946	  - reextract-v2
947	- id: art_20260514_26c5b2
948	  name: fig1_pipeline_overview
949	  type: chart
950	  description: 'Fig 1: StructFuse pipeline overview — left-to-right flow from input
951	    (repo + bug report) through CodeQL extraction, negative mining (3 color-coded
952	    strategies: random/embedding/dataflow), contrastive training (InfoNCE + LoRA),
953	    to fine-tuned retriever. Okabe-Ito palette, serif font, 7x2.8in full-width.'
954	  path: projects/structfuse-context/artifacts/_project/chart/fig1_pipeline_overview.pdf
955	  url: null
956	  project: structfuse-context
957	  exp_id: null
958	  skill: ''
959	  created_at: '2026-05-14T23:38:53.669151+00:00'
960	  tags:
961	  - paper
962	  - figure
963	  - pipeline
964	  - fig1
965	- id: art_20260514_ad5cca
966	  name: fig1_pipeline_overview_png
967	  type: chart
968	  description: Fig 1 pipeline overview PNG preview (300 DPI)
969	  path: projects/structfuse-context/artifacts/_project/chart/fig1_pipeline_overview.png
970	  url: null
971	  project: structfuse-context
972	  exp_id: null
973	  skill: ''
974	  created_at: '2026-05-14T23:38:55.554881+00:00'
975	  tags:
976	  - paper
977	  - figure
978	  - pipeline
979	  - fig1
980	  - preview
981	- id: art_20260514_f9e844
982	  name: fig1_pipeline_overview_script
983	  type: intermediate
984	  description: Generation script for Fig 1 pipeline overview (matplotlib, no external
985	    deps)
986	  path: projects/structfuse-context/artifacts/_project/intermediate/fig1_pipeline_overview.py
987	  url: null
988	  project: structfuse-context
989	  exp_id: null
990	  skill: ''
991	  created_at: '2026-05-14T23:38:57.258190+00:00'
992	  tags:
993	  - paper
994	  - figure
995	  - script
996	  - fig1
997	- id: art_20260514_a5287e
998	  name: fig2_mining_strategies
999	  type: chart
1000	  description: 'Fig 2: Negative Mining Strategies — 3-panel comparison (Random / Embedding-Distance
1001	    / Dataflow-Aware). Shows same mini-repo graph with different negative selections
1002	    highlighted per strategy. Okabe-Ito colors, serif font, publication-ready.'
1003	  path: projects/structfuse-context/artifacts/_project/chart/fig2_mining_strategies.pdf
1004	  url: null
1005	  project: structfuse-context
1006	  exp_id: null
1007	  skill: ''
1008	  created_at: '2026-05-14T23:50:52.794198+00:00'
1009	  tags:
1010	  - paper
1011	  - figure
1012	  - negative-mining
1013	  - EMNLP2026
1014	- id: art_20260515_ae4280
1015	  name: method_v1
1016	  type: paper
1017	  description: 'Method section draft (§3): Problem formulation, structural information
1018	    extraction (M1), structure-aware negative mining (3 strategies), contrastive fine-tuning
1019	    (M2). All numbers sourced from registry.'
1020	  path: projects/structfuse-context/artifacts/_project/paper/method_v1_ae4280.md
1021	  url: null
1022	  project: structfuse-context
1023	  exp_id: null
1024	  skill: ''
1025	  created_at: '2026-05-15T01:59:32.730650+00:00'
1026	  tags:
1027	  - paper
1028	  - method
1029	  - draft
1030	- id: art_20260515_bba58d
1031	  name: experiment_setup_v1
1032	  type: paper
1033	  description: 'Experiment setup draft (§4): Dataset (SWE-smith, 131 repos, 14.3K
1034	    instances/seed), models (Qwen2.5-Coder-3B + StarCoder2-3B), training config (all
1035	    hyperparams from registry), evaluation metrics (R@k, bootstrap CI, Cohen''s d).'
1036	  path: projects/structfuse-context/artifacts/_project/paper/experiment_setup_v1.md
1037	  url: null
1038	  project: structfuse-context
1039	  exp_id: null
1040	  skill: ''
1041	  created_at: '2026-05-15T01:59:36.266487+00:00'
1042	  tags:
1043	  - paper
1044	  - experiment-setup
1045	  - draft
1046	- id: art_20260515_895cbe
1047	  name: introduction_v2
1048	  type: paper
1049	  description: 'Introduction v2 draft — 5-paragraph ML top-venue structure: problem/motivation,
1050	    current approaches & gap, StructFuse approach, key findings, contributions. Claim
1051	    2 marked exploratory per D035. [TBD] placeholders for M2 final numbers.'
1052	  path: projects/structfuse-context/artifacts/_project/paper/introduction_v2.md
1053	  url: null
1054	  project: structfuse-context
1055	  exp_id: null
1056	  skill: ''
1057	  created_at: '2026-05-15T02:00:08.505124+00:00'
1058	  tags:
1059	  - paper
1060	  - introduction
1061	  - v2
1062	  - writing
1063	- id: art_20260515_884407
1064	  name: Checkpoint Criterion Analysis
1065	  type: report
1066	  description: Dual checkpoint (best_by_val_loss vs best_by_R@1) alignment analysis
1067	    + K=7 rationale for paper ablation section. 50% alignment rate on full M2 runs,
1068	    mean R@1 gap +0.65pp when diverged.
1069	  path: projects/structfuse-context/artifacts/_project/report/checkpoint_criterion_analysis.md
1070	  url: null
1071	  project: structfuse-context
1072	  exp_id: null
1073	  skill: ''
1074	  created_at: '2026-05-15T03:21:08.324336+00:00'
1075	  tags:
1076	  - ablation
1077	  - checkpoint
1078	  - paper
1079	- id: art_20260515_d1d8e6
1080	  name: plan005_stratification_spec
1081	  type: report
1082	  description: Plan 005 分层分析规格文档：5 维分层定义、3 阶段管道、数据源、执行计划
1083	  path: projects/structfuse-context/artifacts/plan_005/report/plan005_stratification_spec.md
1084	  url: null
1085	  project: structfuse-context
1086	  exp_id: plan_005
1087	  skill: ''
1088	  created_at: '2026-05-15T05:09:44.760930+00:00'
1089	  tags:
1090	  - stratified_analysis
1091	  - plan_005
1092	  - pipeline
1093	- id: art_20260515_fbb594
1094	  name: checkpoint_criterion_table
1095	  type: paper
1096	  description: 'Checkpoint criterion ablation table (LaTeX tabular): best_by_val_loss
1097	    vs best_by_R@1 comparison across 4 completed M2 runs, 50% divergence rate, encoder-dependent
1098	    pattern'
1099	  path: projects/structfuse-context/artifacts/_project/paper/checkpoint_criterion_table.tex
1100	  url: null
1101	  project: structfuse-context
1102	  exp_id: null
1103	  skill: ''
1104	  created_at: '2026-05-15T06:17:19.124582+00:00'
1105	  tags:
1106	  - paper
1107	  - ablation
1108	  - checkpoint
1109	- id: art_20260515_b69433
1110	  name: fixed_checkpoint_table
1111	  type: paper
1112	  description: 'LaTeX tabular: fixed-checkpoint comparison (embedding vs random at
1113	    same step), eliminates selection bias. Partial — s43 @500/@1000 filled, rest TBD
1114	    pending M2 completion.'
1115	  path: projects/structfuse-context/artifacts/_project/paper/fixed_checkpoint_table.tex
1116	  url: null
1117	  project: structfuse-context
1118	  exp_id: null
1119	  skill: ''
1120	  created_at: '2026-05-15T06:20:08.689200+00:00'
1121	  tags:
1122	  - table
1123	  - fixed-checkpoint
1124	  - claim2
1125	  - reviewer-response
1126	  - draft
1127	- id: art_20260515_c7f173
1128	  name: introduction_v1
1129	  type: paper
1130	  description: 'Introduction section v1 draft (~800 words): D049-compliant softened
1131	    framing, 5-paragraph structure, dual pilot+M2 data reporting, all cite keys aligned
1132	    with references.bib'
1133	  path: projects/structfuse-context/artifacts/_project/paper/introduction_v1_c7f173.md
1134	  url: null
1135	  project: structfuse-context
1136	  exp_id: null
1137	  skill: ''
1138	  created_at: '2026-05-15T08:51:28.731676+00:00'
1139	  tags:
1140	  - paper
1141	  - introduction
1142	  - D049
1143	- id: art_20260515_82f7f1
1144	  name: method_v1
1145	  type: paper
1146	  description: 'Method section v1 draft (~1000 words): 5 subsections (formulation,
1147	    extraction, mining strategies, training, evaluation), D049/D041 compliant, hyperparams
1148	    from registry'
1149	  path: projects/structfuse-context/artifacts/_project/paper/method_v1_82f7f1.md
1150	  url: null
1151	  project: structfuse-context
1152	  exp_id: null
1153	  skill: ''
1154	  created_at: '2026-05-15T09:47:19.709540+00:00'
1155	  tags:
1156	  - paper
1157	  - method
1158	  - D049
1159	- id: art_20260515_5cf1f6
1160	  name: related_work_v1
1161	  type: paper
1162	  description: 'Related Work section v1 (~663 words, 36 unique citations): 4 subsections
1163	    (dense retrieval, contrastive learning, hard negative mining, code structure),
1164	    D049 compliant'
1165	  path: projects/structfuse-context/artifacts/_project/paper/related_work_v1_5cf1f6.md
1166	  url: null
1167	  project: structfuse-context
1168	  exp_id: null
1169	  skill: ''
1170	  created_at: '2026-05-15T09:51:47.169628+00:00'
1171	  tags:
1172	  - paper
1173	  - related-work
1174	  - D049
1175	- id: art_20260515_efa260
1176	  name: abstract_v2
1177	  type: paper
1178	  description: 'Abstract v2: W1 SWE-bench conditional→deleted (plan_003 pending),
1179	    W2 Claim 3 demoted to methodology paragraph, INFOs filled (3 seeds, 123 repos).
1180	    ~220 words.'
1181	  path: projects/structfuse-context/artifacts/_project/paper/abstract_v2.md
1182	  url: null
1183	  project: structfuse-context
1184	  exp_id: null
1185	  skill: ''
1186	  created_at: '2026-05-15T10:37:09.378681+00:00'
1187	  tags:
1188	  - paper
1189	  - abstract
1190	  - v2
1191	- id: art_20260515_c60654
1192	  name: conclusion_v1
1193	  type: paper
1194	  description: 'Conclusion v1 skeleton (~220 words): Claim 1 summary + Claim 2 exploratory
1195	    + CodeQL methodology + SWE-bench TBD + broader impact. D051-compliant placeholders.'
1196	  path: projects/structfuse-context/artifacts/_project/paper/conclusion_v1.md
1197	  url: null
1198	  project: structfuse-context
1199	  exp_id: null
1200	  skill: ''
1201	  created_at: '2026-05-15T10:40:37.927566+00:00'
1202	  tags:
1203	  - paper
1204	  - conclusion
1205	  - v1
1206	- id: art_20260515_1b36e4
1207	  name: experiments_v1_reviewer_fixes
1208	  type: paper
1209	  description: 'experiments_v1.md with reviewer fixes: pos_sim 0.798→0.799, precise
1210	    train/val counts, added §4.3 Structural Extraction Scalability section'
1211	  path: projects/structfuse-context/artifacts/_project/paper/experiments_v1_1b36e4.md
1212	  url: null
1213	  project: structfuse-context
1214	  exp_id: null
1215	  skill: ''
1216	  created_at: '2026-05-15T14:05:01.699800+00:00'
1217	  tags:
1218	  - paper
1219	  - reviewer-fix
1220	- id: art_20260515_e63490
1221	  name: abstract_v2_reviewer_fixes
1222	  type: paper
1223	  description: 'abstract_v2.md with reviewer fixes: weakened overclaims (entirely→largely
1224	    unexploited, zero→negligible cost)'
1225	  path: projects/structfuse-context/artifacts/_project/paper/abstract_v2_e63490.md
1226	  url: null
1227	  project: structfuse-context
1228	  exp_id: null
1229	  skill: ''
1230	  created_at: '2026-05-15T14:05:03.698508+00:00'
1231	  tags:
1232	  - paper
1233	  - reviewer-fix
1234	- id: art_20260515_deb8bc
1235	  name: experiments_v1_claim3_scalability
1236	  type: paper
1237	  description: 'experiments_v1.md updated with expanded Claim 3 scalability subsection:
1238	    setup, zero-timeout result, per-tier Z% table, bounded data-flow scalability discussion.
1239	    All numbers sourced from plan_006_scalability.'
1240	  path: projects/structfuse-context/artifacts/plan_006_scalability/paper/experiments_v1.md
1241	  url: null
1242	  project: structfuse-context
1243	  exp_id: plan_006_scalability
1244	  skill: ''
1245	  created_at: '2026-05-15T14:08:03.838777+00:00'
1246	  tags:
1247	  - paper
1248	  - claim3
1249	  - scalability
1250	  - experiments
1251	- id: art_20260515_56de57
1252	  name: Qwen Training Trajectories
1253	  type: data
1254	  description: 'Complete training trajectories for 5 finished Qwen2.5-Coder-3B M2
1255	    runs (random×3 + embedding_distance×2). Full eval metrics at every 500 steps:
1256	    val_loss, R@1, R@5, R@10. Cross-validated registry vs server logs. For §4.3.3
1257	    Training Dynamics analysis.'
1258	  path: projects/structfuse-context/artifacts/_project/data/qwen_training_trajectories.json
1259	  url: null
1260	  project: structfuse-context
1261	  exp_id: null
1262	  skill: ''
1263	  created_at: '2026-05-15T17:49:41.050627+00:00'
1264	  tags:
1265	  - qwen
1266	  - training-dynamics
1267	  - m2
1268	  - trajectories
1269	  - section-4.3.3
1270	- id: art_20260515_3df68e
1271	  name: Training Dynamics Pre-analysis for §4.3.3
1272	  type: report
1273	  description: 'Quantitative pre-analysis of 5 Qwen runs for paper §4.3.3: overfitting
1274	    patterns, convergence speed, R@1 vs val_loss divergence, seed variance, early
1275	    stopping effectiveness. Includes key observations with numbers and TBD items pending
1276	    dataflow runs.'
1277	  path: projects/structfuse-context/artifacts/_project/report/training_dynamics_analysis.md
1278	  url: null
1279	  project: structfuse-context
1280	  exp_id: null
1281	  skill: ''
1282	  created_at: '2026-05-15T18:31:06.658263+00:00'
1283	  tags:
1284	  - paper
1285	  - section-4.3.3
1286	  - training-dynamics
1287	  - qwen
1288	  - pre-analysis
1289	- id: art_20260515_223d71
1290	  name: StarCoder Training Trajectories
1291	  type: data
1292	  description: 'Complete eval trajectories for StarCoder2-3B M2 full training: random_s42/s43/s44
1293	    completed, embedding_distance_s42 in progress. Full precision metrics from server
1294	    logs, cross-validated with registry.'
1295	  path: projects/structfuse-context/artifacts/_project/data/starcoder_training_trajectories.json
1296	  url: null
1297	  project: structfuse-context
1298	  exp_id: null
1299	  skill: ''
1300	  created_at: '2026-05-15T18:36:06.144895+00:00'
1301	  tags:
1302	  - starcoder
1303	  - training-trajectories
1304	  - m2-full
1305	  - random-baseline
1306	- id: art_20260515_629a10
1307	  name: seed_variance_vs_strategy_effect
1308	  type: data
1309	  description: 'Finding #4 raw data: seed variance vs strategy effect for paper §4.3.3.
1310	    Cross-seed R@1 std (~2.7pp) is 4-5x larger than within-seed strategy delta (~0.6pp).'
1311	  path: projects/structfuse-context/artifacts/_project/data/seed_variance_vs_strategy_effect.json
1312	  url: null
1313	  project: structfuse-context
1314	  exp_id: null
1315	  skill: ''
1316	  created_at: '2026-05-15T18:38:31.593375+00:00'
1317	  tags:
1318	  - finding4
1319	  - seed-variance
1320	  - paper-data
1321	  - methodology
1322	- id: art_20260515_fb1feb
1323	  name: swebench_bm25_baseline_100
1324	  type: data
1325	  description: 'BM25 baseline retrieval results on 100 SWE-bench Lite instances: R@1=0.28,
1326	    R@5=0.51, R@10=0.58, R@20=0.63, MRR=0.3768. CPU-only, 83s total.'
1327	  path: projects/structfuse-context/artifacts/plan_003_swebench_eval/data/swebench_bm25_baseline_100.json
1328	  url: null
1329	  project: structfuse-context
1330	  exp_id: plan_003_swebench_eval
1331	  skill: ''
1332	  created_at: '2026-05-15T19:10:21.123562+00:00'
1333	  tags:
1334	  - swebench
1335	  - bm25
1336	  - baseline
1337	  - retrieval
1338	- id: art_20260515_0f954f
1339	  name: swebench_bm25_baseline_300
1340	  type: data
1341	  description: 'BM25 baseline retrieval on 300 SWE-bench Lite instances: R@1=0.2733,
1342	    R@5=0.4667, R@10=0.55, R@20=0.6467. Aligned with neural eval sample size.'
1343	  path: projects/structfuse-context/artifacts/plan_003_swebench_eval/data/swebench_bm25_baseline_300.md
1344	  url: null
1345	  project: structfuse-context
1346	  exp_id: plan_003_swebench_eval
1347	  skill: ''
1348	  created_at: '2026-05-15T21:21:58.997965+00:00'
1349	  tags:
1350	  - swebench
1351	  - bm25
1352	  - baseline
1353	  - retrieval
1354	  - '300'
1355	- id: art_20260515_131123
1356	  name: m2_eval_summary
1357	  type: report
1358	  description: M2 全策略 eval 汇总表：Qwen/StarCoder × random/embedding/dataflow × 3 seeds，含
1359	    Δ 对比、pilot vs full、训练动态、SWE-bench BM25 baseline。8/18 subruns done。
1360	  path: projects/structfuse-context/artifacts/_project/report/m2_eval_summary.md
1361	  url: null
1362	  project: structfuse-context
1363	  exp_id: null
1364	  skill: ''
1365	  created_at: '2026-05-15T23:06:15.670950+00:00'
1366	  tags:
1367	  - eval
1368	  - summary
1369	  - m2
1370	  - paper
1371	  - plan_005
1372	- id: art_20260515_d9f942
1373	  name: overfitting_mechanism_figure
1374	  type: chart
1375	  description: 'Overfitting mechanism analysis: Panel A — R@1 training curves by strategy
1376	    (Qwen/StarCoder), Panel B — margin vs eval-loss slope scatter (Pearson r=-0.60,
1377	    p=0.069). Lower margin → faster overfitting.'
1378	  path: projects/structfuse-context/artifacts/neg_difficulty_analysis/chart/overfitting_mechanism_meta.txt
1379	  url: null
1380	  project: structfuse-context
1381	  exp_id: neg_difficulty_analysis
1382	  skill: ''
1383	  created_at: '2026-05-15T23:22:42.417561+00:00'
1384	  tags:
1385	  - neg_difficulty
1386	  - overfitting
1387	  - mechanism
1388	  - paper
1389	  - figure
1390	- id: art_20260515_b9293c
1391	  name: eval_trajectories_csv
1392	  type: data
1393	  description: 'Per-step eval trajectories for all completed M2 subruns: 42 eval records
1394	    across 10 (model, strategy, seed) combinations. Source: trainer_state.json + wandb
1395	    offline runs.'
1396	  path: projects/structfuse-context/artifacts/neg_difficulty_analysis/data/eval_trajectories_meta.txt
1397	  url: null
1398	  project: structfuse-context
1399	  exp_id: neg_difficulty_analysis
1400	  skill: ''
1401	  created_at: '2026-05-15T23:22:47.682528+00:00'
1402	  tags:
1403	  - eval
1404	  - trajectories
1405	  - training_dynamics
1406	  - data
1407	- id: art_20260516_faa725
1408	  name: related_work_references
1409	  type: report
1410	  description: Related Work 文献收集：21 篇论文，3 方向（code retrieval negative mining 7篇, hard
1411	    negative overfitting 7篇, representation geometry 7篇）。含 BibTeX + 1句摘要 + 相关性标注。
1412	  path: projects/structfuse-context/artifacts/_project/report/related_work_references.md
1413	  url: null
1414	  project: structfuse-context
1415	  exp_id: null
1416	  skill: ''
1417	  created_at: '2026-05-16T00:21:32.001215+00:00'
1418	  tags:
1419	  - literature
1420	  - related_work
1421	  - bibtex
1422	  - paper
1423	- id: art_20260516_a6d623
1424	  name: run_pool_sensitivity.sh
1425	  type: intermediate
1426	  description: Pool sensitivity evaluation script for plan_019. Tests strategy ranking
1427	    stability across pool={50,100,200,500}. Located at /root/structfuse/scripts/run_pool_sensitivity.sh
1428	    on bjb1-42106.
1429	  path: projects/structfuse-context/artifacts/_project/intermediate/run_pool_sensitivity_readme.txt
1430	  url: null
1431	  project: structfuse-context
1432	  exp_id: null
1433	  skill: ''
1434	  created_at: '2026-05-16T08:05:49.781885+00:00'
1435	  tags:
1436	  - plan_019
1437	  - pool_sensitivity
1438	  - evaluation
1439	- id: art_20260516_af7d5a
1440	  name: methodology_v2
1441	  type: paper
1442	  description: '§3 Methodology v2 (dual-version shared): 5 subsections — Problem Formulation,
1443	    4 Negative Mining Strategies (random/embedding/BM25/dataflow), Structural Extraction
1444	    Pipeline (90% coverage post-reextract), Training Setup (3 encoders: Qwen/StarCoder/UniXcoder),
1445	    Query-Split Evaluation Protocol (D062). All numbers as \placeholder{} pending
1446	    final data.'
1447	  path: projects/structfuse-context/artifacts/_project/paper/methodology.tex
1448	  url: null
1449	  project: structfuse-context
1450	  exp_id: null
1451	  skill: ''
1452	  created_at: '2026-05-16T12:45:15.114354+00:00'
1453	  tags:
1454	  - paper
1455	  - methodology
1456	  - v2
1457	  - shared
1458	  - EMNLP2026
1459	- id: art_20260516_46130f
1460	  name: related_work_v2
1461	  type: paper
1462	  description: '§2 Related Work v2 (dual-version shared): 4 subsections — Dense Retrieval
1463	    for Code, Contrastive Learning & HN Mining, Evaluation Methodology for Dense Retrieval
1464	    (NEW: checkpoint selection, pool size, query overlap), Code Structure in ML. 4
1465	    citations marked [VERIFY].'
1466	  path: projects/structfuse-context/artifacts/_project/paper/related_work.tex
1467	  url: null
1468	  project: structfuse-context
1469	  exp_id: null
1470	  skill: ''
1471	  created_at: '2026-05-16T12:46:47.859245+00:00'
1472	  tags:
1473	  - paper
1474	  - related-work
1475	  - v2
1476	  - shared
1477	  - EMNLP2026
1478	- id: art_20260516_df45cb
1479	  name: introduction_v2_shared
1480	  type: paper
1481	  description: §1 Introduction v2 P1-P4 (shared) + P5 placeholder (version-dependent).
1482	    P1=problem, P2=CoCoHaNeRe contradiction, P3=code structure dimension, P4=evaluation
1483	    methodology gap (+16.3pp criterion effect). Both version A and B contribution
1484	    lists in comments.
1485	  path: projects/structfuse-context/artifacts/_project/paper/introduction.tex
1486	  url: null
1487	  project: structfuse-context
1488	  exp_id: null
1489	  skill: ''
1490	  created_at: '2026-05-16T12:46:50.446529+00:00'
1491	  tags:
1492	  - paper
1493	  - introduction
1494	  - v2
1495	  - shared
1496	  - EMNLP2026
1497	- id: art_20260516_359b4d
1498	  name: discussion_v2_tex
1499	  type: paper
1500	  description: '§5 Discussion v2 LaTeX (shared): 5 subsections — Inference-Time Complementarity,
1501	    When Does Mining Matter (UniXcoder boundary + rep geometry), Evaluation Methodology
1502	    Implications (reporting recommendations), Limitations (5 items), Future Work (3
1503	    directions).'
1504	  path: projects/structfuse-context/artifacts/_project/paper/discussion.tex
1505	  url: null
1506	  project: structfuse-context
1507	  exp_id: null
1508	  skill: ''
1509	  created_at: '2026-05-16T12:51:13.557649+00:00'
1510	  tags:
1511	  - paper
1512	  - discussion
1513	  - v2
1514	  - shared
1515	  - EMNLP2026
1516	- id: art_20260516_be807e
1517	  name: citation_verification_v2
1518	  type: report
1519	  description: Verification of 4 academic citations (dodge2020, thakur2021beir, muennighoff2023mteb,
1520	    craswell2020overview) for existence, correctness, and context match accuracy
1521	  path: projects/structfuse-context/artifacts/_project/report/citation_verification.md
1522	  url: null
1523	  project: structfuse-context
1524	  exp_id: null
1525	  skill: ''
1526	  created_at: '2026-05-16T12:51:15.723865+00:00'
1527	  tags:
1528	  - citation
1529	  - verification
1530	  - paper-v2
1531	- id: art_20260516_1a9596
1532	  name: experiments_v2_scaffold
1533	  type: paper
1534	  description: '§4 Experiments v2 scaffold: Setup + 2 main tables (pool-50 + query-split)
1535	    with \placeholder{} + 5 analysis subsections (criterion, pool size, training dynamics,
1536	    neg difficulty, cross-encoder). Figure captions for fig3/fig5. Version-dependent
1537	    narratives in comments.'
1538	  path: projects/structfuse-context/artifacts/_project/paper/experiments.tex
1539	  url: null
1540	  project: structfuse-context
1541	  exp_id: null
1542	  skill: ''
1543	  created_at: '2026-05-16T12:51:16.716670+00:00'
1544	  tags:
1545	  - paper
1546	  - experiments
1547	  - v2
1548	  - scaffold
1549	  - EMNLP2026
1550	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b8bd2c65-a1a1-4541-8292-d943318ae9ba",
  "isSidechain": true,
  "promptId": "1589742a-41cc-4d40-ae94-dc9d919d6688",
  "agentId": "aae11a3504772ac7f",
  "type": "user",
  "uuid": "5c6a3cb6-992e-41f8-9fd0-710ad749c9eb",
  "sourceToolAssistantUUID": "b8bd2c65-a1a1-4541-8292-d943318ae9ba",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "c4036345-91c5-47f2-9c09-36d0f1b82314",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-16T15:06:46.977Z_

<details><summary>↩ Tool result · `toolu_016vwWEvgqAXiv2bmx46DWUJ`</summary>

```text
baseline: null
experiments:
  mvp_p1_codeql_feasibility:
    status: DONE
    retry_count: 0
    created_at: '2026-05-12T11:30:45.938Z'
    updated_at: '2026-05-12T11:58:06.197Z'
    spec:
      command: python extraction/extract_dataflow.py + codeql query run (call_graph.ql
--
      h2_note: 'After path normalization fix: 8/8 gold in connected (was 6/8)'
    log_path: /root/autodl-tmp/mvp_results/mvp_phase1_report.json
    checkpoint_path: N/A (CPU pipeline, no model checkpoint)
    completed_at: '2026-05-12T11:31:16.335Z'
  mvp_p2a_linear_proxy:
    status: DONE
    retry_count: 0
    created_at: '2026-05-12T11:53:42.223Z'
    updated_at: '2026-05-12T11:58:15.436Z'
    spec:
      command: python evaluation/linear_proxy.py (logistic regression on data-flow
--
      note: 3 repos / 3 positive samples, directional evidence
    checkpoint_path: N/A (logistic regression, no checkpoint)
    log_path: /root/structfuse/evaluation/linear_proxy.py output
    completed_at: '2026-05-12T11:58:15.436Z'
  p2b-smoke-test:
    status: DONE
    retry_count: 0
    created_at: '2026-05-12T12:14:30.477Z'
    updated_at: '2026-05-12T15:05:41.269Z'
    spec:
      command: obsolete smoke test
--
      wall_clock_seconds: 10270.8
      gpu_hours: 2.85
    conclusion: killed
    completed_at: '2026-05-12T15:05:41.270Z'
  p2b-smoke2:
    status: DONE
    retry_count: 0
    created_at: '2026-05-12T12:16:08.154Z'
    updated_at: '2026-05-12T15:05:42.174Z'
    spec:
      command: obsolete smoke test
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a41e4b0c-f2b5-4606-bff6-e84677989c5c",
  "isSidechain": true,
  "promptId": "1589742a-41cc-4d40-ae94-dc9d919d6688",
  "agentId": "aae11a3504772ac7f",
  "type": "user",
  "uuid": "e157be8a-c1cf-4b87-a64c-ac434ebf428f",
  "sourceToolAssistantUUID": "a41e4b0c-f2b5-4606-bff6-e84677989c5c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "c4036345-91c5-47f2-9c09-36d0f1b82314",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 48 · 2026-05-16T15:06:48.510Z_

Excellent! Now let me search for any files defining the tier structure more explicitly:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e157be8a-c1cf-4b87-a64c-ac434ebf428f",
  "isSidechain": true,
  "agentId": "aae11a3504772ac7f",
  "requestId": "req_011Cb6TQLtWNHYoPtUMW3PEi",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "83625553-0b45-4d1a-b060-1b06198f8d59",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "c4036345-91c5-47f2-9c09-36d0f1b82314",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HeLwHx1s7kBSJeq4niJgMi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 23014,
      "cache_read_input_tokens": 62074,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 23014,
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

_source line 49 · 2026-05-16T15:06:49.594Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01JVGSKGu5Yy89aRUU1B4Vsr`</summary>

```json
{
  "pattern": "best.*tier|median.*tier|worst.*tier|tier.*best|tier.*median|tier.*worst",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "83625553-0b45-4d1a-b060-1b06198f8d59",
  "isSidechain": true,
  "agentId": "aae11a3504772ac7f",
  "requestId": "req_011Cb6TQLtWNHYoPtUMW3PEi",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ad78842f-6d47-443f-87b6-7b9c1771b123",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "c4036345-91c5-47f2-9c09-36d0f1b82314",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HeLwHx1s7kBSJeq4niJgMi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 23014,
      "cache_read_input_tokens": 62074,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 23014,
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

### Tool result

_source line 50 · 2026-05-16T15:06:49.766Z_

<details><summary>↩ Tool result · `toolu_01JVGSKGu5Yy89aRUU1B4Vsr`</summary>

```text
&lt;persisted-output>
Output too large (23.7KB). Full output saved to: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-5/c4036345-91c5-47f2-9c09-36d0f1b82314/tool-results/toolu_01JVGSKGu5Yy89aRUU1B4Vsr.txt

Preview (first 2KB):
Found 250 files limit: 250
projects/structfuse-context/artifacts/dream_reports/dream_20260516T150348/logs/phase2_best_attempt0.log
projects/structfuse-context/artifacts/dream_reports/dream_20260516T150348/logs/phase1_attempt0.log
global/logs/usage.jsonl
global/logs/workers/registry.json
global/logs/workers/registry.json.bak
projects/structfuse-context/logs/workers/worker_paper_research_verify_citations_v2_related_work_20260516T124847.log
projects/structfuse-context/logs/workers/worker_code_repobench_add_starcoder_20260516T123945.log
projects/structfuse-context/logs/workers/worker_code_d062_analysis_regime_patch_20260516T114733.log
projects/structfuse-context/logs/workers/worker_code_pool_sensitivity_script_20260516T114426.log
projects/structfuse-context/logs/workers/worker_code_repobench_eval_check_20260516T114440.log
projects/structfuse-context/logs/workers/worker_code_d062_analysis_script_20260516T110856.log
projects/structfuse-context/logs/workers/worker_ops_d062_completion_monitor_20260516T110753.log
global/logs/registry_audit.jsonl
projects/structfuse-context/logs/workers/worker_ops_full_status_check_director_20260516T110445.log
projects/structfuse-context/logs/chats/archive/feishu_group_oc_651ef5630fe7a61a1decb410adb7641b_director_20260516T110322_970665.jsonl
projects/structfuse-context/logs/workers/worker_ops_d062_data_verify_and_watcher_check_20260516T093518.log
projects/structfuse-context/logs/workers/worker_ops_d062_progress_and_training_status_20260516T093030.log
projects/structfuse-context/logs/workers/worker_ops_check_unixcoder_s42_results_20260516T093038.log
projects/structfuse-context/logs/workers/worker_analysis_unixcoder-3strat-s42_20260516T092457.log
projects/structfuse-context/logs/workers/worker_eval_d062_progress_check_20260516T080718.log
projects/structfuse-context/logs/workers/worker_check_training_status_all_20260516T080728.log
projects/structfuse-context/logs/workers/worker_code_pool_sensitivity_prep_20260516T075945.log
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ad78842f-6d47-443f-87b6-7b9c1771b123",
  "isSidechain": true,
  "promptId": "1589742a-41cc-4d40-ae94-dc9d919d6688",
  "agentId": "aae11a3504772ac7f",
  "type": "user",
  "uuid": "30b1db8f-f939-4eed-89f2-f339018ad1db",
  "sourceToolAssistantUUID": "ad78842f-6d47-443f-87b6-7b9c1771b123",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "c4036345-91c5-47f2-9c09-36d0f1b82314",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-16T15:06:49.993Z_

<details open><summary>🔧 Tool call — Bash · `toolu_018jUbcRAtEMKmcso5SBc7A8`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "30b1db8f-f939-4eed-89f2-f339018ad1db",
  "isSidechain": true,
  "agentId": "aae11a3504772ac7f",
  "requestId": "req_011Cb6TQLtWNHYoPtUMW3PEi",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c1bf2e0e-a02b-44cf-aa64-0875275346b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "c4036345-91c5-47f2-9c09-36d0f1b82314",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HeLwHx1s7kBSJeq4niJgMi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 23014,
      "cache_read_input_tokens": 62074,
      "output_tokens": 230,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 23014
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 230,
          "cache_read_input_tokens": 62074,
          "cache_creation_input_tokens": 23014,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 23014,
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

_source line 52 · 2026-05-16T15:06:50.058Z_

<details><summary>↩ Tool result · `toolu_018jUbcRAtEMKmcso5SBc7A8`</summary>

```text
total 216
drwxr-xr-x 6 ubuntu ubuntu   4096 May 14 17:20 .
drwxr-xr-x 6 ubuntu ubuntu   4096 May 16 15:03 ..
drwxr-xr-x 2 ubuntu ubuntu   4096 May 14 17:02 best
drwxr-xr-x 2 ubuntu ubuntu   4096 May 14 17:14 logs
drwxr-xr-x 2 ubuntu ubuntu   4096 May 14 17:11 median
-rw-r--r-- 1 ubuntu ubuntu 195406 May 14 17:20 meta.yaml
drwxr-xr-x 2 ubuntu ubuntu   4096 May 14 17:20 worst
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c1bf2e0e-a02b-44cf-aa64-0875275346b3",
  "isSidechain": true,
  "promptId": "1589742a-41cc-4d40-ae94-dc9d919d6688",
  "agentId": "aae11a3504772ac7f",
  "type": "user",
  "uuid": "e82e9feb-fe2c-4b59-912f-e9488b146331",
  "sourceToolAssistantUUID": "c1bf2e0e-a02b-44cf-aa64-0875275346b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "c4036345-91c5-47f2-9c09-36d0f1b82314",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 53 · 2026-05-16T15:06:51.542Z_

Perfect! Now let me check for any documentation on tier definitions and look at a metadata file from the dream reports:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e82e9feb-fe2c-4b59-912f-e9488b146331",
  "isSidechain": true,
  "agentId": "aae11a3504772ac7f",
  "requestId": "req_011Cb6TQa2HVGkB95sbQdV59",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "fb8d1116-e868-4fd0-bef6-afc5502b13cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "c4036345-91c5-47f2-9c09-36d0f1b82314",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011vwk7VghmJZBMEHLcuYMy9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1410,
      "cache_read_input_tokens": 85088,
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

_source line 54 · 2026-05-16T15:06:52.359Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QsQN3mB2wLNP7SVEMsFF4n`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/meta.yaml",
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fb8d1116-e868-4fd0-bef6-afc5502b13cb",
  "isSidechain": true,
  "agentId": "aae11a3504772ac7f",
  "requestId": "req_011Cb6TQa2HVGkB95sbQdV59",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8c5cdec6-f6a1-445e-8de8-b2fdc2a16416",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "c4036345-91c5-47f2-9c09-36d0f1b82314",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011vwk7VghmJZBMEHLcuYMy9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1410,
      "cache_read_input_tokens": 85088,
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

### Tool result

_source line 55 · 2026-05-16T15:06:52.375Z_

<details><summary>↩ Tool result · `toolu_01QsQN3mB2wLNP7SVEMsFF4n`</summary>

```text
1	dream_id: dream_20260514T162530
2	project: structfuse-context
3	venue: ''
4	focus: D030 修复后验证：新增 plan_018 BM25 baseline（关闭 CoCoHaNeRe correction 论证）、plan_019
5	  pool size sensitivity、plan_004 多 seed CIs、plan_005 structural coverage 分层 + neg_difficulty
6	  quartile。Framing 修正：N=2 降级为 observation、Claim 3 降为 supporting methodology、StarCoder
7	  decoder-only。Reviewers 应重点评估：(1) BM25 baseline 是否关闭了上一轮最大缺口，(2) 新增实验是否充分回应了上一轮 median/worst
8	  的 "related work insufficient" 和 "effect size marginal" 问题，(3) 修正后的 N=2 observation
9	  framing 是否足够。
10	review_mode: full
11	review_visible: true
12	writing_visible: true
13	what_if: []
14	tier_definitions:
15	  tiers:
16	    best:
17	      tier: best
18	      meaning: 全 18 runs 复现 pilot pattern，BM25 baseline 关闭 CoCoHaNeRe 论证，三条 claim
19	        原样成立
20	      key_assumptions:
21	      - embedding-random R@1 delta 在两个 encoder 上 95% CI 下界 > 0
22	      - dataflow-random R@1 delta 在 Qwen 上 CI 下界 > 0，StarCoder 上 ≤ 0（条件性成立）
23	      - BM25 negatives 明确 harm（vs random delta 显著为负），实证关闭 CoCoHaNeRe proxy 论证
24	      - pool size 50→500 策略排名不翻转
25	      - SWE-bench Lite 下游 resolve rate 有可见提升
26	      number_ranges:
27	        qwen_emb_minus_random_R1_pp:
28	        - 1.5
29	        - 2.5
30	        starcoder_emb_minus_random_R1_pp:
31	        - 1.0
32	        - 2.0
33	        qwen_df_minus_random_R1_pp:
34	        - 0.5
35	        - 1.5
36	        starcoder_df_minus_random_R1_pp:
37	        - -1.0
38	        - 0.3
39	        bm25_minus_random_R1_pp:
40	        - -4.0
41	        - -1.5
42	        swebench_resolve_rate_delta_pp:
43	        - 1.5
44	        - 4.0
45	        repobench_R1_delta_pp:
46	        - 1.0
47	        - 3.0
48	        pool_ranking_stable_pct:
49	        - 75
50	        - 100
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8c5cdec6-f6a1-445e-8de8-b2fdc2a16416",
  "isSidechain": true,
  "promptId": "1589742a-41cc-4d40-ae94-dc9d919d6688",
  "agentId": "aae11a3504772ac7f",
  "type": "user",
  "uuid": "58b4cfdd-6e32-4787-a7f2-b806bcf3c50a",
  "sourceToolAssistantUUID": "8c5cdec6-f6a1-445e-8de8-b2fdc2a16416",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "c4036345-91c5-47f2-9c09-36d0f1b82314",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 56 · 2026-05-16T15:06:52.813Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01W1aemfv55oU37jDwR1oTSq`</summary>

```json
{
  "command": "grep -r \"tier.*definition\\|best.*definition\\|[B][M][W]\\|review.*tier\" /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/*.yaml 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "58b4cfdd-6e32-4787-a7f2-b806bcf3c50a",
  "isSidechain": true,
  "agentId": "aae11a3504772ac7f",
  "requestId": "req_011Cb6TQa2HVGkB95sbQdV59",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "47cf1a0d-6fdf-4cf5-9c94-eaab355f1051",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "c4036345-91c5-47f2-9c09-36d0f1b82314",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011vwk7VghmJZBMEHLcuYMy9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1410,
      "cache_read_input_tokens": 85088,
      "output_tokens": 238,
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
          "input_tokens": 5,
          "output_tokens": 238,
          "cache_read_input_tokens": 85088,
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

_source line 57 · 2026-05-16T15:06:52.874Z_

<details><summary>↩ Tool result · `toolu_01W1aemfv55oU37jDwR1oTSq`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "47cf1a0d-6fdf-4cf5-9c94-eaab355f1051",
  "isSidechain": true,
  "promptId": "1589742a-41cc-4d40-ae94-dc9d919d6688",
  "agentId": "aae11a3504772ac7f",
  "type": "user",
  "uuid": "17959253-6454-45bd-a5fd-5125db611c65",
  "sourceToolAssistantUUID": "47cf1a0d-6fdf-4cf5-9c94-eaab355f1051",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "c4036345-91c5-47f2-9c09-36d0f1b82314",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 58 · 2026-05-16T15:06:54.265Z_

Excellent! Let me continue reading the tier definitions:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "17959253-6454-45bd-a5fd-5125db611c65",
  "isSidechain": true,
  "agentId": "aae11a3504772ac7f",
  "requestId": "req_011Cb6TQnqxokEhc5FYCPm1j",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "af47389d-6cec-444d-a9e4-2fed2ddf3159",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "c4036345-91c5-47f2-9c09-36d0f1b82314",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01S5AgE9KMXk7JdprAEMsjCX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1141,
      "cache_read_input_tokens": 86498,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1141,
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

_source line 59 · 2026-05-16T15:06:54.801Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TjkCRTyvMmSsUeC8wmj8Dc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/meta.yaml",
  "limit": 250,
  "offset": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "af47389d-6cec-444d-a9e4-2fed2ddf3159",
  "isSidechain": true,
  "agentId": "aae11a3504772ac7f",
  "requestId": "req_011Cb6TQnqxokEhc5FYCPm1j",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "37e52a88-ab83-4668-8b70-d858f5d28e2c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "c4036345-91c5-47f2-9c09-36d0f1b82314",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01S5AgE9KMXk7JdprAEMsjCX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1141,
      "cache_read_input_tokens": 86498,
      "output_tokens": 144,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1141
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 144,
          "cache_read_input_tokens": 86498,
          "cache_creation_input_tokens": 1141,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1141,
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

_source line 60 · 2026-05-16T15:06:54.813Z_

<details><summary>↩ Tool result · `toolu_01TjkCRTyvMmSsUeC8wmj8Dc`</summary>

```text
50	        - 100
51	        bootstrap_CI_width_R1_pp:
52	        - 0.5
53	        - 2.0
54	        qwen_mean_R1_absolute:
55	        - 0.53
56	        - 0.58
57	        starcoder_mean_R1_absolute:
58	        - 0.44
59	        - 0.5
60	      narrative_direction: '原始 framing 完全成立。Claim 1（embedding mining 纠正 misconception）有
61	        BM25 baseline 实证支撑 + 两 encoder 统计显著。Claim 2（dataflow 条件性获益）由 Qwen/StarCoder
62	        对比 + neg_difficulty margin 分析 + representation saturation 机制完整闭环。Claim 3 作为
63	        supporting methodology 无需额外论证。标题可用 "Correcting Misconceptions" 强 framing，
64	        SWE-bench 数据作为 downstream validation 加固 practical relevance。EMNLP Main 强投。
65	
66	        '
67	    median:
68	      tier: median
69	      meaning: embedding mining 优势存在但 effect size 缩水约 50%，BM25 部分支持 correction 论证，dataflow
70	        条件性获益噪声大
71	      key_assumptions:
72	      - embedding-random delta 正向但 CI 较宽，个别 seed 差异 < 0.5pp
73	      - dataflow-random delta 在 Qwen 上 CI 包含 0（方向正确但不显著）
74	      - BM25 negatives harm 方向正确但 delta 小（-0.5 ~ -1.5pp），与 random 差异 p > 0.05
75	      - pool ≥ 200 时 embedding 与 dataflow 排名偶有交叉
76	      - SWE-bench delta < 1pp 或 CI 包含 0
77	      number_ranges:
78	        qwen_emb_minus_random_R1_pp:
79	        - 0.5
80	        - 1.5
81	        starcoder_emb_minus_random_R1_pp:
82	        - 0.3
83	        - 1.0
84	        qwen_df_minus_random_R1_pp:
85	        - -0.3
86	        - 0.8
87	        starcoder_df_minus_random_R1_pp:
88	        - -1.5
89	        - 0.0
90	        bm25_minus_random_R1_pp:
91	        - -1.5
92	        - -0.3
93	        swebench_resolve_rate_delta_pp:
94	        - -0.5
95	        - 1.5
96	        repobench_R1_delta_pp:
97	        - 0.0
98	        - 1.5
99	        pool_ranking_stable_pct:
100	        - 50
101	        - 75
102	        bootstrap_CI_width_R1_pp:
103	        - 2.0
104	        - 4.0
105	        qwen_mean_R1_absolute:
106	        - 0.51
107	        - 0.55
108	        starcoder_mean_R1_absolute:
109	        - 0.42
110	        - 0.47
111	      narrative_direction: 'Claim 1 需降级：embedding mining "tends to help" 而非 "consistently
112	        improves"， CoCoHaNeRe correction 从 "empirically verified" 改为 "BM25 proxy 方向一致但
113	        effect size 不足以排除其他混杂因素"。Claim 2 降级为 exploratory observation：dataflow 条件性获益的
114	        evidence 不足以支撑独立 claim，合并到 Claim 1 作为 "strategy-encoder interaction analysis"
115	        的一个 case。论文重心从 "correcting misconception + mechanistic explanation" 移向 "systematic
116	        empirical comparison + representation geometry analysis as explanatory framework"。需补充
117	        related work 深度对比（ANCE, curriculum mining）来弥补 effect size 不足。标题用 "Systematic
118	        Study" 而非 "Correcting Misconceptions"。仍投 EMNLP Main， 但定位从 strong empirical
119	        contribution 调整为 analysis paper。
120	
121	        '
122	    worst:
123	      tier: worst
124	      meaning: full-scale effect size 消失或反转，BM25 baseline 未能区分 proxy vs true embedding，核心叙事需重建
125	      key_assumptions:
126	      - embedding-random delta < 0.3pp 且 CI 明确包含 0（至少一个 encoder）
127	      - dataflow 在两个 encoder 上均无显著获益或 harm
128	      - BM25 negatives 表现与 embedding negatives 无统计差异 → CoCoHaNeRe correction 论证无法关闭
129	      - pool ≥ 200 时排名与 pool=50 不一致
130	      - SWE-bench 无可见差异或方向相反
131	      - 数据 pipeline 无 bug（排除实现错误后结果仍如此）
132	      number_ranges:
133	        qwen_emb_minus_random_R1_pp:
134	        - -0.5
135	        - 0.5
136	        starcoder_emb_minus_random_R1_pp:
137	        - -0.8
138	        - 0.3
139	        qwen_df_minus_random_R1_pp:
140	        - -1.0
141	        - 0.3
142	        starcoder_df_minus_random_R1_pp:
143	        - -2.0
144	        - 0.0
145	        bm25_minus_random_R1_pp:
146	        - -1.0
147	        - 0.5
148	        swebench_resolve_rate_delta_pp:
149	        - -1.0
150	        - 0.5
151	        repobench_R1_delta_pp:
152	        - -1.0
153	        - 0.5
154	        pool_ranking_stable_pct:
155	        - 0
156	        - 50
157	        bootstrap_CI_width_R1_pp:
158	        - 3.0
159	        - 6.0
160	        qwen_mean_R1_absolute:
161	        - 0.48
162	        - 0.53
163	        starcoder_mean_R1_absolute:
164	        - 0.4
165	        - 0.46
166	      narrative_direction: 三条原始 claim 均无法维持。Reframe 方向：negative result paper —— "Why
167	        Hard Negative Mining Strategies Don't Differentiate for Code Retrieval at
168	        Scale"。核心贡献变为： (1) 大规模控制实验表明 strategy 选择对 code retrieval 的影响被高估，pilot-scale
169	        差异在 full-scale 消失（scale-dependent finding）；(2) representation geometry analysis
170	        仍有价值——作为解释 *为什么* 策略差异消失的框架（margin 在训练后收敛，pretrained geometry 差异被 fine-tuning
171	        抹平）；(3) CoCoHaNeRe 的 BM25-proxy 问题仍可报告为 methodological caution，但从 "correction"
172	        降为 "observation"。论文定位从 positive contribution 转为 high-quality negative result
173	        + methodological contribution。EMNLP Main 仍可投 （negative result papers 有先例），但需要
174	        (a) 足够大的实验规模证明 negative result 可信， (b) mechanistic explanation 为什么不 work，(c)
175	        actionable takeaway（practitioners 不需要花 GPU 时间做 fancy mining）。风险：reviewer 可能认为
176	        "nothing works" 缺乏 novelty ——需用 representation geometry analysis 的解释深度来弥补。
177	scenarios:
178	- tier: best
179	  pdf_path: /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/best/paper.pdf
180	  imagined_experiments:
181	  - name: SWE-bench Lite End-to-End Evaluation
182	    plan_id: plan_003
183	    description: '3 strategies × best Qwen checkpoint, Qwen3.6-27B agent, 300 SWE-bench
184	      Lite instances. Retriever 提供 top-k context files，agent 生成 patch，评估 resolve rate。
185	
186	      '
187	    expected_results:
188	      random_resolve_rate: 0.22
189	      random_resolved_count: 66
190	      embedding_resolve_rate: 0.245
191	      embedding_resolved_count: 73
192	      dataflow_resolve_rate: 0.252
193	      dataflow_resolved_count: 76
194	      embedding_minus_random_pp: 2.5
195	      dataflow_minus_random_pp: 3.2
196	      dataflow_minus_embedding_pp: 0.7
197	      total_instances: 300
198	      retriever_top_k: 5
199	      agent_model: Qwen3.6-27B
200	    result_rationale: 'Embedding retriever 在 SWE-bench 上提升 +2.5pp，因为 bug-fix patch
201	      通常涉及与 issue 描述 语义相似但非完全匹配的文件——embedding mining 训练使 retriever 更擅长区分"近似但无关" 与"近似且相关"的文件。Dataflow
202	      额外提升 +0.7pp（总 +3.2pp vs random）因为 SWE-bench patch 经常跨函数/跨模块（约 40% 涉及 caller-callee
203	      关系），dataflow negatives 训练使 retriever 理解"调用链上的文件更可能共同出现在 patch 中"。Delta 幅度从 retrieval
204	      R@1 的 +2.0/+1.0pp 放大到下游 resolve rate 的 +2.5/+3.2pp，符合检索质量在端到端任务中 的杠杆效应——正确检索一个关键文件可以使原本完全失败的
205	      patch 变为可解决。 效果幅度在 swebench_resolve_rate_delta_pp [1.5, 4.0] 范围内。
206	
207	      '
208	    tables:
209	    - name: 'Table 4: SWE-bench Lite Resolve Rate'
210	      columns:
211	      - Strategy
212	      - Resolved
213	      - Total
214	      - Rate (%)
215	      - Δ vs Random (pp)
216	      rows:
217	      - - random
218	        - 66
219	        - 300
220	        - 22.0
221	        - —
222	      - - embedding
223	        - 73
224	        - 300
225	        - 24.3
226	        - '+2.3'
227	      - - dataflow
228	        - 76
229	        - 300
230	        - 25.3
231	        - '+3.3'
232	    - name: 'Table 4b: SWE-bench by Patch Complexity'
233	      columns:
234	      - Patch Type
235	      - N
236	      - random (%)
237	      - embedding (%)
238	      - dataflow (%)
239	      rows:
240	      - - single-file
241	        - 189
242	        - 28.0
243	        - 30.7
244	        - 30.2
245	      - - multi-file
246	        - 111
247	        - 11.7
248	        - 14.4
249	        - 17.1
250	    figures_description:
251	    - 'Fig 5: SWE-bench resolve rate bar chart (3 strategies) with bootstrap 95% CI
252	      whiskers'
253	    - 'Fig 5b: Scatter plot — retrieval R@1 rank vs resolve rate per instance, colored
254	      by strategy'
255	    analysis: 'Multi-file patches（占 37%）是 dataflow 拉开差距的主要来源：dataflow 在 multi-file
256	      上 +5.4pp vs random，远大于 single-file 的 +2.2pp。这与 Claim 2 一致——dataflow negatives
257	      使 retriever 更好地理解跨模块依赖。Embedding vs random 在 multi-file 上也有 +2.7pp，说明更难的 negatives
258	      普遍有益。总体 resolve rate 22-25% 与 SweRank/SWE-Fixer 文献报告的 retriever-only baseline
259	      一致。
260	
261	      '
262	  - name: RepoBench-R Cross-File Retrieval with Multi-Seed CIs
263	    plan_id: plan_004
264	    description: 'RepoBench-R test_easy (pool ~6) 和 test_hard (pool ~18) 上评估 9 seeds
265	      × 3 strategies × 2 encoders，报告 R@1 均值 + 95% bootstrap CI。
266	
267	      '
268	    expected_results:
269	      qwen_test_hard:
270	        random_R1_mean: 0.621
271	        random_R1_ci:
272	        - 0.614
273	        - 0.628
274	        embedding_R1_mean: 0.642
275	        embedding_R1_ci:
276	        - 0.634
277	        - 0.65
278	        dataflow_R1_mean: 0.633
279	        dataflow_R1_ci:
280	        - 0.624
281	        - 0.642
282	        embedding_minus_random_pp: 2.1
283	        dataflow_minus_random_pp: 1.2
284	      qwen_test_easy:
285	        random_R1_mean: 0.843
286	        embedding_R1_mean: 0.855
287	        dataflow_R1_mean: 0.85
288	        embedding_minus_random_pp: 1.2
289	      starcoder_test_hard:
290	        random_R1_mean: 0.574
291	        random_R1_ci:
292	        - 0.566
293	        - 0.582
294	        embedding_R1_mean: 0.589
295	        embedding_R1_ci:
296	        - 0.58
297	        - 0.598
298	        dataflow_R1_mean: 0.572
299	        dataflow_R1_ci:
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "37e52a88-ab83-4668-8b70-d858f5d28e2c",
  "isSidechain": true,
  "promptId": "1589742a-41cc-4d40-ae94-dc9d919d6688",
  "agentId": "aae11a3504772ac7f",
  "type": "user",
  "uuid": "8f556cc7-8d1a-42d3-982a-eb2e97f553c5",
  "sourceToolAssistantUUID": "37e52a88-ab83-4668-8b70-d858f5d28e2c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "c4036345-91c5-47f2-9c09-36d0f1b82314",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 61 · 2026-05-16T15:07:16.408Z_

Perfect! Now I have comprehensive information. Let me create a final summary document:

## Summary of Search Results

I've completed a thorough search of the project at `/home/ubuntu/.agent-ml-research-idea_gen_0509_5`. Here are the key files and findings:

### 1. **EXPERIMENT PLAN & REGISTRY FILES**

**Main Planning Files:**
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/experiment_plan.yaml` - 21 planned experiments (plan_001 through plan_021) covering:
  - M1: CodeQL extraction (plan_001, plan_006, plan_007)
  - M2: Full-scale training comparisons (plan_002, plan_013, plan_020, plan_021)
  - M3: Downstream evaluations (plan_003, plan_004)
  - Ablations (plan_005, plan_007-012, plan_014-015)
  - Analysis (plan_017-019)

**Registry Files:**
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/registry.yaml` (1808 lines) - Comprehensive experiment metrics and status tracking
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/dream_registry.yaml` - Dream review outcomes and metadata

### 2. **TIER DEFINITIONS (Best/Median/Worst)**

**Location:** `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/dream_20260514T162530/meta.yaml`

The project uses three-tier reviewer simulation (Best/Median/Worst) with explicit definitions:

**BEST TIER** - All claims hold with strong empirical support:
- Embedding mining: +1.5 to +2.5pp (Qwen), +1.0 to +2.0pp (StarCoder)
- Dataflow mining: +0.5 to +1.5pp (Qwen), -1.0 to +0.3pp (StarCoder)
- BM25 baseline: -4.0 to -1.5pp (proves CoCoHaNeRe proxy artifact)
- Pool stability: 75-100% ranking stable across pool=50→500
- SWE-bench downstream: +1.5 to +4.0pp resolve rate improvement
- Key: All effects statistically significant with CI lower bounds > 0

**MEDIAN TIER** - Effects exist but effect sizes diminished (~50% shrinkage):
- Embedding mining: +0.5 to +1.5pp (Qwen), +0.3 to +1.0pp (StarCoder)
- Dataflow mining: -0.3 to +0.8pp (Qwen), -1.5 to +0.0pp (StarCoder)
- BM25: -1.5 to -0.3pp (smaller harm, p > 0.05)
- Pool stability: 50-75% stable ranking
- SWE-bench: -0.5 to +1.5pp (CI may contain zero)
- Claims downgraded to exploratory; CoCoHaNeRe correction weakened

**WORST TIER** - Effects disappear or reverse (negative result):
- Embedding mining: -0.5 to +0.5pp (Qwen), -0.8 to +0.3pp (StarCoder)
- Dataflow: -1.0 to +0.3pp (Qwen), -2.0 to +0.0pp (StarCoder)
- BM25: -1.0 to +0.5pp (indistinguishable from embedding)
- Pool stability: 0-50% ranking consistency
- SWE-bench: -1.0 to +0.5pp (no visible improvement)
- Narrative reframe needed: "Why Hard Negative Mining Doesn't Differentiate at Scale"

### 3. **DREAM REPORTS WITH IMAGINED EXPERIMENTS**

Located in `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/dream_reports/`:

**dream_20260512T204322/** - Initial risk assessment
- 3 tiers with predicted results

**dream_20260514T075732/** - Framing refinement
- Claim restructuring after CoCoHaNeRe discovery
- New N=2 encoder limitation framing

**dream_20260514T162530/** - Most complete (D030)
- **best/imagined_experiments.yaml** (41KB) - Full best-case predictions with:
  - SWE-bench Lite E2E eval (plan_003)
  - RepoBench-R multi-seed CIs (plan_004)
  - 5-layer stratified analysis (plan_005)
  - Call-graph hop depth ablation (plan_007)
  - Training data scaling (plan_008)
  - Fusion head ablation (plan_009)
  - Temperature ablation (plan_014)
  - Dynamic vs static mining (plan_015)
  - Bootstrap CIs (plan_016)
  - BM25 baseline (plan_018)
  - Pool size sensitivity (plan_019)
  - Plus detailed tables, figures, and mechanistic rationales

- **median/imagined_experiments.yaml** (44KB)
- **worst/imagined_experiments.yaml** (54KB)

**dream_20260516T150348/** - Latest (D062) checkpoint selection focus (imagining phase only)

### 4. **ARTIFACTS & RESULTS DIRECTORIES**

**Main Artifacts Location:** `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/`

**Structured Data Files:**
- `/projects/structfuse-context/artifacts/_project/data/pilot_results.json` - Pilot evaluation metrics
- `/projects/structfuse-context/artifacts/_project/data/qwen_training_trajectories.json` - Full training curves
- `/projects/structfuse-context/artifacts/_project/data/starcoder_training_trajectories.json`
- `/projects/structfuse-context/artifacts/_project/data/negative_difficulty_stats.txt` - Margin analysis
- `/projects/structfuse-context/artifacts/_project/data/seed_variance_vs_strategy_effect.json` - Statistical power analysis

**Completed Experiment Results:**
- `plan_006_scalability/data/` - M1 CodeQL extraction stats (123 repos, 44K instances)
- `plan_003_swebench_eval/data/swebench_bm25_baseline_*.json` - BM25 baseline on 300 SWE-bench instances
- `neg_difficulty_analysis/data/` - Representation geometry findings (margin ratio ~2.6-4.1x between Qwen/StarCoder)
- `plan_018_bm25/data/bm25_overlap_stratified_meta.txt` - BM25 Jaccard overlap analysis

**Paper Drafts:**
- `_project/paper/` - Methodology, related work, introduction, discussion, figures (.md and .tex versions)
- Multiple versions marked with commit hashes (v1, v1_3cf111, v1_82f7f1, etc.)

### 5. **MANIFEST & TRACKING**

**Comprehensive Registry:** `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/artifacts/manifest.yaml` (1550+ entries)
- Tracks all artifacts by ID, type, creation time, tags
- Includes intermediate code, reports, data, charts, paper sections

### 6. **OTHER KEY FILES**

- `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/decisions.yaml` - Decision log (65KB)
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/writing_plan.yaml` - Writing schedule
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/literature_map.yaml` - References (37 citations)

---

**Key Insight:** This project uses a sophisticated "dream review" framework where each major decision point triggers a full three-tier reviewer simulation (best/median/worst case) with predicted experimental outcomes, confidence ranges, and narrative implications. The dream_20260514T162530 report is the most comprehensive, containing detailed imagined experiments that specify exact numerical ranges, statistical significance thresholds, and mechanistic rationales for each tier.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8f556cc7-8d1a-42d3-982a-eb2e97f553c5",
  "isSidechain": true,
  "agentId": "aae11a3504772ac7f",
  "requestId": "req_011Cb6TQvWLEJHagWEzf9cF7",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "640125b3-5f8a-46f7-9d27-ada654348e26",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "c4036345-91c5-47f2-9c09-36d0f1b82314",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01GozioyPkinrqBDAjS39JJq",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 4293,
      "cache_read_input_tokens": 87639,
      "output_tokens": 2106,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4293
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2106,
          "cache_read_input_tokens": 87639,
          "cache_creation_input_tokens": 4293,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4293,
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
