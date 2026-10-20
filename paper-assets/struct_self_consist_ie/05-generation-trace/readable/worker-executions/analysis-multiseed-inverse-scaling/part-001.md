# analysis multiseed inverse scaling — Part 1 of 4

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Worker execution logs

[Transcript overview](../analysis-multiseed-inverse-scaling.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/3a/3a5f1eb5f0b24f360715.json)

## Before a recorded user message

## Before a recorded user message

12 recorded events


### Log line

_source line 1_

Warning: no stdin data received in 3s, proceeding without it. If piping from a slow command, redirect stdin explicitly: < /dev/null to skip, or wait longer.

---


### System

_source line 2_

```json
{
  "type": "system",
  "subtype": "init",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3",
  "tools": [
    "Task",
    "AskUserQuestion",
    "Bash",
    "CronCreate",
    "CronDelete",
    "CronList",
    "Edit",
    "EnterPlanMode",
    "EnterWorktree",
    "ExitPlanMode",
    "ExitWorktree",
    "Glob",
    "Grep",
    "ListMcpResourcesTool",
    "Monitor",
    "NotebookEdit",
    "PushNotification",
    "Read",
    "ReadMcpResourceTool",
    "RemoteTrigger",
    "ScheduleWakeup",
    "Skill",
    "TaskOutput",
    "TaskStop",
    "TodoWrite",
    "ToolSearch",
    "WebFetch",
    "WebSearch",
    "Write",
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
  "mcp_servers": [
    {
      "name": "agent-ml-research",
      "status": "connected"
    }
  ],
  "model": "claude-opus-4-6",
  "permissionMode": "bypassPermissions",
  "slash_commands": [
    "update-config",
    "debug",
    "simplify",
    "batch",
    "fewer-permission-prompts",
    "loop",
    "schedule",
    "claude-api",
    "clear",
    "compact",
    "context",
    "heapdump",
    "init",
    "review",
    "security-review",
    "extra-usage",
    "usage",
    "insights",
    "team-onboarding"
  ],
  "apiKeySource": "none",
  "claude_code_version": "2.1.126",
  "output_style": "default",
  "agents": [
    "claude",
    "Explore",
    "general-purpose",
    "Plan",
    "statusline-setup"
  ],
  "skills": [
    "update-config",
    "debug",
    "simplify",
    "batch",
    "fewer-permission-prompts",
    "loop",
    "schedule",
    "claude-api"
  ],
  "plugins": [],
  "analytics_disabled": false,
  "uuid": "23e7f00c-bde6-4f1c-8310-2539ef2721ff",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/memory/"
  },
  "fast_mode_state": "off"
}
```

---


### Runtime record

_source line 3_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed_warning",
    "resetsAt": 1779858000,
    "rateLimitType": "seven_day",
    "utilization": 0.82,
    "isUsingOverage": false,
    "surpassedThreshold": 0.75
  },
  "uuid": "d71281f9-aaae-4225-8563-f16a0b51d5eb",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3"
}
```

---


### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me break this task down:

1. Find data - check registry for Few-NERD experiments across seeds and N values
2. Understand transition analysis logic
3. Run the analysis
4. Generate report

Let me start by reading the registry and exploring the project code in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3",
  "uuid": "c38bd7f6-947c-434d-938a-56933219af46",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ERDoPc5j1U7P3eizc1Jkeu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12643,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12643
      },
      "output_tokens": 21,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Assistant

_source line 5_

开始执行 multi-seed inverse scaling recompute。先并行查 registry 和项目代码。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3",
  "uuid": "667046d1-3b98-4196-a9ae-d6009c841286",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ERDoPc5j1U7P3eizc1Jkeu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12643,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12643
      },
      "output_tokens": 21,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 6_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01KzPEnXx8gSjNX17GHERm41`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image",
  "max_results": 6
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3",
  "uuid": "b4a0096e-aefe-4b04-a67c-266fa342e1df",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ERDoPc5j1U7P3eizc1Jkeu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12643,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12643
      },
      "output_tokens": 21,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 7 · 2026-05-23T18:54:38.125Z_

<details><summary>↩ Tool result · `toolu_01KzPEnXx8gSjNX17GHERm41`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_registry"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_project_file"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__register_artifact"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__ssh_read_only"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__ssh_execute"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__detect_image"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3",
  "uuid": "fd41170c-ef9c-400d-973b-4925f4d8fae4",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__ssh_execute",
      "mcp__agent-ml-research__detect_image"
    ],
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute,mcp__agent-ml-research__detect_image",
    "total_deferred_tools": 29
  }
}
```

</details>

---


### Assistant

_source line 8_

<details><summary>Logged reasoning block</summary>

```text
Now let me read the registry and explore the project code in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3",
  "uuid": "72e99ede-f3d3-4f48-8559-6bcb94ba57f4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GzhC4uJYbBrck6LLEpAeFc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2270,
      "cache_read_input_tokens": 24484,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2270
      },
      "output_tokens": 19,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 9_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01PyD8vKpR9KgMxN8tw8FBN2`</summary>

```json
{
  "project": "struct_self_consist_ie",
  "limit": 0,
  "fields": [
    "*"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3",
  "uuid": "f6553024-0506-46af-80ca-296bf1d60ab6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GzhC4uJYbBrck6LLEpAeFc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2270,
      "cache_read_input_tokens": 24484,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2270
      },
      "output_tokens": 19,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 10 · 2026-05-23T18:54:44.753Z_

<details><summary>↩ Tool result · `toolu_01PyD8vKpR9KgMxN8tw8FBN2`</summary>

```text
Error: result (524,087 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/9ee457e1-50d5-4907-947a-5d727dccbec3/tool-results/mcp-agent-ml-research-read_registry-1779562484737.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/9ee457e1-50d5-4907-947a-5d727dccbec3/tool-results/mcp-agent-ml-research-read_registry-1779562484737.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/9ee457e1-50d5-4907-947a-5d727dccbec3/tool-results/mcp-agent-ml-research-read_registry-1779562484737.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3",
  "uuid": "8c528fe9-7950-444d-b540-a74fa7ebef67",
  "tool_use_result": {
    "content": "Error: result (524,087 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/9ee457e1-50d5-4907-947a-5d727dccbec3/tool-results/mcp-agent-ml-research-read_registry-1779562484737.txt.\nFormat: JSON with schema: {result: string}\n- For targeted queries (find a value, filter by field): use jq on the file directly.\n- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/9ee457e1-50d5-4907-947a-5d727dccbec3/tool-results/mcp-agent-ml-research-read_registry-1779562484737.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.\n- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. \"/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/9ee457e1-50d5-4907-947a-5d727dccbec3/tool-results/mcp-agent-ml-research-read_registry-1779562484737.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim.\" A vague \"summarize this\" may lose detail.\n",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"exp_fewnerd_pretrained_n32_s42_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T15:49:35.691Z\", \"updated_at\": \"2026-05-23T12:00:19.327Z\", \"hypothesis\": \"Pretrained N-scaling rerun: FewNERD N=32 with Qwen2.5-7B-Instruct. v1 killed at 70% to prevent UnicodeEncodeError crash at save stage (no incremental checkpoint). Fix (errors='replace') deployed. Same hypothesis: tests pretrained MV advantage at 4× budget (N=32).\", \"parent\": \"exp_fewnerd_pretrained_n32_s42\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=3 python -u code/run_mvp_pilot.py --model_path /root/autodl-tmp/models/Qwen2.5-7B-Instruct --data_dir data/fewnerd/ --dataset fewnerd --subtask ner --n_samples 32 --temperature 1.0 --seed 42 --collect_logprobs --output_dir output/fewnerd_pretrained_n32_seed42/\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:3\"], \"pid\": \"157469\", \"data_count\": 37648, \"data_path\": \"data/fewnerd/\", \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": 42, \"n_samples\": 32, \"log_path\": \"~/runs/struct_self_consist_ie/exp_fewnerd_pretrained_n32_s42_v2.log\", \"checkpoint_source\": \"Qwen2.5-7B-Instruct (pretrained, no finetuning)\", \"eval_data\": \"data/fewnerd/ (37648 instances)\", \"note\": \"Restarted with verified fix. Old PID 155692 killed (loaded pre-fix code). Server corrected: autodl-5090 (not autodl-5090-c).\"}, \"reproduce\": {\"finished_at\": \"2026-05-23T11:37:27.391Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T11:37:31.594Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-23T11:37:37.721905+00:00\"}]}, \"metrics\": {\"greedy_f1\": 0.539, \"mv_f1\": 0.577, \"mv_delta_pp\": 3.85, \"lp_f1\": 0.529, \"lp_delta_pp\": -1.03, \"oracle_f1\": 0.705, \"oracle_delta_pp\": 16.56, \"degeneracy_rate\": 5.42, \"capture_rate\": 19, \"sj_rho\": 0.456, \"n_instances_gold_nonempty\": 32565, \"subset\": \"gold-nonempty\"}}, \"exp_fewnerd_pretrained_n16_s42_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T15:21:18.896Z\", \"updated_at\": \"2026-05-23T00:26:15.782Z\", \"hypothesis\": \"Pretrained N-scaling: FewNERD N=16 T=1.0 seed=42 with unfinetuned Qwen2.5-7B-Instruct. Fills the N=16 point on the pretrained N-scaling curve (N=8/16/32). Tests whether doubling sample budget from N=8 increases MV delta and oracle headroom for pretrained models.\", \"parent\": \"exp_fewnerd_pretrained_n16_s42\", \"spec\": {\"command\": \"python -u code/run_mvp_pilot.py --model_path /root/autodl-tmp/.hf_cache/Qwen2.5-7B-Instruct --data_dir data/fewnerd/ --dataset fewnerd --subtask ner --n_samples 16 --temperature 1.0 --seed 42 --collect_logprobs --output_dir output/fewnerd_pretrained_n16_seed42/\", \"server\": \"autodl-5090-c\", \"gpu\": \"cuda:1\", \"pid\": 452387, \"log_path\": \"/root/runs/struct_self_consist_ie/exp_fewnerd_pretrained_n16_s42_v2.log\", \"submitted_at\": \"2026-05-22T15:21:43.507Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/fewnerd/\", \"data_count\": 602368, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": 42, \"checkpoint_source\": \"N/A (pretrained model, retry of v1)\", \"eval_data\": \"data/fewnerd/\", \"wall_clock_seconds\": 32661.4, \"gpu_hours\": 9.07, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/fewnerd_pretrained_n16_seed42/\"}, \"reproduce\": {\"finished_at\": \"2026-05-23T00:19:06.784Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-23T00:19:17.288300+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"greedy_f1\": 0.5373, \"mv_strict_f1\": 0.5779, \"mv_delta_strict_pp\": 4.06, \"mv_incl_f1\": 0.5722, \"oracle_f1\": 0.6786, \"degeneracy_rate\": 0.076, \"alpha_crit_eff_strict\": 0.4398, \"alpha_crit_strict\": 0.4064, \"mv_capture_rate\": 0.2876, \"n_total\": 37648, \"n_gold_nonempty\": 32565, \"greedy_f1_all\": 0.5109, \"oracle_f1_all\": 0.6433, \"sj_rho_full\": 0.453, \"fk_rho_full\": 0.401, \"lp_rho_full\": 0.192, \"structural_beats_surface\": true, \"note\": \"Primary metrics (greedy/mv/oracle) computed on gold-nonempty instances (n=32565) via recompute_alpha_crit_unified.py. _all suffix = full instances incl gold-empty.\"}, \"checkpoint_path\": \"output/fewnerd_pretrained_n16_seed42/\", \"log_path\": \"/root/runs/struct_self_consist_ie/exp_fewnerd_pretrained_n16_s42_v2.log\", \"completed_at\": \"2026-05-23T00:26:04.898Z\"}, \"exp_scierc_n8_s456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T11:01:42.040Z\", \"updated_at\": \"2026-05-22T18:47:05.350Z\", \"hypothesis\": \"R35-N2 SciERC validation: SciERC N=8 T=1.0 seed=456 finetuned model. Third seed to complete 3-seed mean±σ for SciERC. Uses unified run_mvp_pilot.py pipeline (micro-F1). With s42 and s123, enables statistical power for SciERC core claims.\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:1\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask ner --n_samples 8 --temperature 1.0 --seed 456 --collect_logprobs --output_dir output/scierc_n8_seed456/\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:1\"], \"pid\": \"135921\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_scierc_n8_s456.log\", \"submitted_at\": \"2026-05-22T11:27:51.619Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 3976.7, \"gpu_hours\": 1.1}, \"pid\": \"135921\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_scierc_n8_s456.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask ner --n_samples 8 --temperature 1.0 --seed 456 --collect_logprobs --output_dir output/scierc_n8_seed456/\\\"\", \"finished_at\": \"2026-05-22T11:35:04.266Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-22T11:35:24.223164+00:00\"}]}, \"metrics\": {\"greedy_f1\": 0.6657, \"mv_f1\": 0.6573, \"mv_delta_pp\": -0.84, \"lp_f1\": 0.6626, \"lp_delta_pp\": -0.31, \"degeneracy_rate\": 0.12, \"agreement_rate\": 0.6597, \"oracle_f1\": 0.7733, \"fleiss_kappa\": 0.3864, \"soft_jaccard\": 0.6939, \"note\": \"MV/LP metrics from legacy pipeline. Superseded by MF4v2 unified recompute (see exp_fewnerd_mf4_s42 series). MF4v2 SciERC 3-seed MV delta: -0.74±0.46pp (all negative).\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"output/scierc_n8_seed456/\", \"completed_at\": \"2026-05-22T12:34:08.279Z\"}, \"exp_scierc_n8_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T11:01:40.010Z\", \"updated_at\": \"2026-05-22T18:47:03.049Z\", \"hypothesis\": \"R35-N2 SciERC validation: SciERC N=8 T=1.0 seed=123 finetuned model. Second seed to upgrade SciERC from tentative to validated status. Uses unified run_mvp_pilot.py pipeline (micro-F1). SciERC N=8 seed=42 showed MV Δ=-0.74pp. Tests reproducibility across seeds.\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:0\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask ner --n_samples 8 --temperature 1.0 --seed 123 --collect_logprobs --output_dir output/scierc_n8_seed123/\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"135642\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_scierc_n8_s123.log\", \"submitted_at\": \"2026-05-22T11:27:42.944Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 3980.8, \"gpu_hours\": 1.11}, \"pid\": \"135642\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_scierc_n8_s123.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask ner --n_samples 8 --temperature 1.0 --seed 123 --collect_logprobs --output_dir output/scierc_n8_seed123/\\\"\", \"finished_at\": \"2026-05-22T11:34:55.224Z\"}, \"metrics\": {\"greedy_f1\": 0.6613, \"mv_f1\": 0.6648, \"mv_delta_pp\": 0.34, \"lp_f1\": 0.6698, \"lp_delta_pp\": 0.85, \"degeneracy_rate\": 0.116, \"agreement_rate\": 0.6646, \"oracle_f1\": 0.7794, \"fleiss_kappa\": 0.3847, \"soft_jaccard\": 0.6979, \"note\": \"MV/LP metrics from legacy pipeline. Superseded by MF4v2 unified recompute (see exp_fewnerd_mf4_s42 series). MF4v2 SciERC 3-seed MV delta: -0.74±0.46pp (all negative).\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"output/scierc_n8_seed123/\", \"completed_at\": \"2026-05-22T12:34:03.717Z\"}, \"exp_scierc_n8_s3141\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T16:33:47.527Z\", \"updated_at\": \"2026-05-22T18:28:25.162Z\", \"hypothesis\": \"R40 N2 statistical power: SciERC N=8 T=1.0 seed=3141 finetuned Qwen3-8B. 5th seed to strengthen 5-seed Holm-Bonferroni test for core correlation-selection claim (current p_adj=0.055 with 3 seeds).\", \"spec\": {\"command\": \"python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc --dataset scierc --subtask ner --n_samples 8 --temperature 1.0 --seed 3141 --collect_logprobs --output_dir output/scierc_mf4v2_seed3141/\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:1\"], \"pid\": \"158859\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_scierc_n8_s3141.log\", \"submitted_at\": \"2026-05-22T16:34:05.985Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scierc\", \"data_count\": 551, \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 3141, \"wall_clock_seconds\": 6859.2, \"gpu_hours\": 1.91}, \"metrics\": {\"greedy_f1\": 0.6609, \"oracle_f1\": 0.7645, \"oracle_headroom\": 0.1036, \"fleiss_kappa_mean\": 0.2906, \"soft_jaccard_mean\": 0.6265, \"rho_sj_f1_full\": 0.3477, \"rho_kappa_f1_full\": 0.2074, \"rho_sj_f1_cond\": 0.2427, \"rho_kappa_f1_cond\": 0.0806, \"structural_beats_surface\": true, \"rho_advantage\": 0.1404, \"logprob_rho_full\": 0.1926, \"logprob_auroc_full\": 0.5733, \"logprob_rho_cond\": 0.1231, \"logprob_auroc_cond\": 0.5399, \"sample_f1_mean\": 0.5802, \"sample_f1_std\": 0.3357, \"sample_f1_pct_zero\": 16.5, \"n_instances\": 551, \"degeneracy_rate\": 16.5, \"verdict\": \"MARGINAL\"}, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/scierc_mf4v2_seed3141/\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_scierc_n8_s3141.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T18:28:25.162Z\"}, \"exp_scierc_n8_s2024\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T16:33:46.085Z\", \"updated_at\": \"2026-05-22T18:28:21.440Z\", \"hypothesis\": \"R40 N2 statistical power: SciERC N=8 T=1.0 seed=2024 finetuned Qwen3-8B. 4th seed to strengthen 5-seed Holm-Bonferroni test for core correlation-selection claim (current p_adj=0.055 with 3 seeds).\", \"spec\": {\"command\": \"python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc --dataset scierc --subtask ner --n_samples 8 --temperature 1.0 --seed 2024 --collect_logprobs --output_dir output/scierc_mf4v2_seed2024/\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"158714\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_scierc_n8_s2024.log\", \"submitted_at\": \"2026-05-22T16:34:02.708Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scierc\", \"data_count\": 551, \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 2024, \"wall_clock_seconds\": 6858.7, \"gpu_hours\": 1.91}, \"metrics\": {\"greedy_f1\": 0.6641, \"oracle_f1\": 0.7914, \"oracle_headroom\": 0.1273, \"fleiss_kappa_mean\": 0.3572, \"soft_jaccard_mean\": 0.6606, \"rho_sj_f1_full\": 0.337, \"rho_kappa_f1_full\": 0.2356, \"rho_sj_f1_cond\": 0.289, \"rho_kappa_f1_cond\": 0.1465, \"structural_beats_surface\": true, \"rho_advantage\": 0.1014, \"logprob_rho_full\": 0.1831, \"logprob_auroc_full\": 0.5629, \"logprob_rho_cond\": 0.1196, \"logprob_auroc_cond\": 0.5305, \"sample_f1_mean\": 0.5971, \"sample_f1_std\": 0.3243, \"sample_f1_pct_zero\": 14.1, \"n_instances\": 551, \"degeneracy_rate\": 14.1, \"verdict\": \"MARGINAL\"}, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/scierc_mf4v2_seed2024/\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_scierc_n8_s2024.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T18:28:21.440Z\"}, \"exp_esj_qwen3_all\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T16:33:50.504Z\", \"updated_at\": \"2026-05-22T18:24:33.293Z\", \"hypothesis\": \"Test whether finetuned Qwen3-8B models can self-calibrate via entailment-based self-judgment (ESJ): does the model's P(yes) for verifying its own extracted entities correlate with entity correctness? Replaces Qwen2.5-7B ESJ probe to match the main experiment's finetuned model.\", \"spec\": {\"command\": \"bash run_esj_qwen3_all.sh\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:2\", \"pid\": \"159002\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_esj_qwen3_all.log\", \"submitted_at\": \"2026-05-22T16:34:09.148Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"output/{scierc,conll,fewnerd}_mf4v2_*/samples.jsonl\", \"data_count\": 41652, \"model_name\": \"Qwen3-8B (finetuned, per-dataset)\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/qwen3-8b-{scierc,conll,fewnerd}-merged\", \"eval_data\": \"SciERC/CoNLL/FewNERD\", \"wall_clock_seconds\": 6605.5, \"gpu_hours\": 1.83}, \"checkpoint_path\": \"output/esj_qwen3_*/esj_results.json\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_esj_qwen3_all.log\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-22T18:24:14.632Z\", \"metrics\": {\"scierc\": {\"n_instances\": 551, \"n_entities\": 2768, \"p_yes_mean\": 0.382, \"construction_f1\": {\"greedy\": 0.6497, \"best_mv\": 0.6469, \"best_esj\": 0.5756, \"oracle\": 0.7824}, \"entity_signal\": {\"esj_rho\": 0.02, \"esj_auroc\": 0.512, \"agree_rho\": 0.515, \"agree_auroc\": 0.792}, \"within_instance\": {\"esj_rho\": 0.056, \"lp_rho\": 0.188}, \"selection_f1\": {\"esj\": 0.589, \"lp\": 0.647}}, \"conll\": {\"n_instances\": 3453, \"n_entities\": 8054, \"p_yes_mean\": 0.5, \"construction_f1\": {\"greedy\": 0.9091, \"best_mv\": 0.9066, \"best_esj\": 0.8237, \"oracle\": 0.9551}, \"entity_signal\": {\"esj_rho\": 0.087, \"esj_auroc\": 0.553, \"agree_rho\": 0.777, \"agree_auroc\": 0.941}, \"within_instance\": {\"esj_rho\": -0.008, \"lp_rho\": 0.28}, \"selection_f1\": {\"esj\": 0.846, \"lp\": 0.899}}, \"fewnerd\": {\"n_instances\": 37648, \"n_entities\": 169790, \"p_yes_mean\": 0.652, \"construction_f1\": {\"greedy\": 0.7717, \"best_mv\": 0.764, \"best_esj\": 0.6817, \"oracle\": 0.8729}, \"entity_signal\": {\"esj_rho\": -0.008, \"esj_auroc\": 0.495, \"agree_rho\": 0.673, \"agree_auroc\": 0.881}, \"within_instance\": {\"esj_rho\": 0.332, \"lp_rho\": 0.543}, \"selection_f1\": {\"esj\": 0.686, \"lp\": 0.781}}}}, \"exp_fewnerd_mf4_s456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T05:09:02.532Z\", \"updated_at\": \"2026-05-22T17:55:46.607Z\", \"hypothesis\": \"MF4 pipeline fix: FewNERD N=8 T=1.0 seed=456 using run_mvp_pilot.py (greedy_f1/micro-F1). Replaces exp_021 which used incompatible greedy_macro_f1 metric. Required for 3-seed statistical power with unified pipeline.\", \"conclusion\": \"success\", \"server\": \"autodl-5090-c\", \"gpu\": \"cuda:2\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-fewnerd-exp021-merged --data_dir data/fewnerd/ --dataset fewnerd --subtask ner --n_samples 8 --temperature 1.0 --seed 456 --collect_logprobs --output_dir output/fewnerd_mf4_seed456/\\\"\", \"server\": \"autodl-5090-c\", \"gpu\": [\"cuda:2\"], \"pid\": \"426513\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_fewnerd_mf4_s456.log\", \"submitted_at\": \"2026-05-22T10:36:28.589Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 26358.0, \"gpu_hours\": 7.32}, \"pid\": \"426513\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_fewnerd_mf4_s456.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-fewnerd-exp021-merged --data_dir data/fewnerd/ --dataset fewnerd --subtask ner --n_samples 8 --temperature 1.0 --seed 456 --collect_logprobs --output_dir output/fewnerd_mf4_seed456/\\\"\", \"finished_at\": \"2026-05-22T12:43:44.463Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-22T12:44:05.701851+00:00\"}]}, \"metrics\": {\"greedy_f1\": 0.7909, \"oracle_f1\": 0.881, \"mv_strict_f1\": 0.7685, \"mv_delta_pp\": -2.24, \"lp_f1\": 0.7921, \"lp_delta_pp\": 0.12, \"degeneracy_rate\": 0.081, \"oracle_headroom_pp\": 9.01, \"fleiss_kappa_mean\": 0.3555, \"soft_jaccard_mean\": 0.6845, \"rho_sj_full\": 0.3122, \"rho_sj_cond\": 0.2559, \"note\": \"MV/LP/degen from 3-seed unified recompute on gold-nonempty subset (n=32565)\"}, \"checkpoint_path\": \"output/fewnerd_mf4_seed456/\", \"completed_at\": \"2026-05-22T17:55:46.607Z\"}, \"exp_fewnerd_mf4_s123_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T11:03:20.521Z\", \"updated_at\": \"2026-05-22T17:55:43.051Z\", \"hypothesis\": \"MF4 pipeline fix retry: FewNERD N=8 T=1.0 seed=123 using run_mvp_pilot.py (micro-F1). Replaces exp_fewnerd_mf4_s123 which failed due to GPU contention on autodl-5090. Required for 3-seed statistical power with unified pipeline.\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:2\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-fewnerd-exp021-merged --data_dir data/fewnerd/ --dataset fewnerd --subtask ner --n_samples 8 --temperature 1.0 --seed 123 --collect_logprobs --output_dir output/fewnerd_mf4_seed123_v2/\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"136358\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_fewnerd_mf4_s123_v2.log\", \"submitted_at\": \"2026-05-22T11:27:59.925Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 23263.1, \"gpu_hours\": 6.46}, \"pid\": \"136358\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_fewnerd_mf4_s123_v2.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-fewnerd-exp021-merged --data_dir data/fewnerd/ --dataset fewnerd --subtask ner --n_samples 8 --temperature 1.0 --seed 123 --collect_logprobs --output_dir output/fewnerd_mf4_seed123_v2/\\\"\", \"finished_at\": \"2026-05-22T13:38:48.328Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-22T13:38:57.181792+00:00\"}]}, \"metrics\": {\"greedy_f1\": 0.7909, \"oracle_f1\": 0.8892, \"mv_strict_f1\": 0.7648, \"mv_delta_pp\": -2.61, \"lp_f1\": 0.7918, \"lp_delta_pp\": 0.09, \"degeneracy_rate\": 0.093, \"oracle_headroom_pp\": 9.83, \"fleiss_kappa_mean\": 0.3503, \"soft_jaccard_mean\": 0.6701, \"rho_sj_full\": 0.308, \"rho_sj_cond\": 0.201, \"note\": \"MV/LP/degen from 3-seed unified recompute on gold-nonempty subset (n=32565)\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"output/fewnerd_mf4_seed123_v2/\", \"completed_at\": \"2026-05-22T17:55:43.051Z\"}, \"exp_fewnerd_pretrained_n32_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T04:12:53.761Z\", \"updated_at\": \"2026-05-22T15:49:32.212Z\", \"hypothesis\": \"Pretrained N-scaling: FewNERD N=32 with Qwen2.5-7B-Instruct (unfinetuned). FewNERD pretrained showed +3.90pp MV gain at N=8. Tests whether pretrained MV advantage scales with N and whether the pretrained-vs-finetuned direction flip persists at 4× budget. Complements CoNLL/SciERC pretrained N=32 for cross-dataset generalization evidence.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && python -u code/run_mvp_pilot.py --model_path /root/autodl-tmp/.hf_cache/Qwen2.5-7B-Instruct --data_dir data/fewnerd/ --dataset fewnerd --subtask ner --n_samples 32 --temperature 1.0 --seed 42 --collect_logprobs --output_dir output/fewnerd_pretrained_n32_seed42/\\\"\", \"server\": \"autodl-5090-c\", \"gpu\": [\"cuda:3\"], \"pid\": \"387491\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_fewnerd_pretrained_n32_s42.log\", \"submitted_at\": \"2026-05-22T04:13:16.155Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/fewnerd/\", \"data_count\": 37648, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": 42, \"n_samples\": 32, \"checkpoint_path\": \"output/fewnerd_pretrained_n32_seed42/\", \"wall_clock_seconds\": 41776.1, \"gpu_hours\": 11.6}, \"conclusion\": \"failed\", \"metrics\": {\"kill_reason\": \"UnicodeEncodeError crash prevention: no incremental save, save stage would crash after 16h inference. Killed at 70% to avoid 5h GPU waste.\", \"progress_at_kill\": \"70% (838K/1.2M prompts, ~11h elapsed)\", \"fix_status\": \"sampling.py errors='replace' already deployed on autodl-5090-c\"}, \"completed_at\": \"2026-05-22T15:49:32.212Z\"}, \"exp_fewnerd_pretrained_n16_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T05:30:50.992Z\", \"updated_at\": \"2026-05-22T15:20:28.681Z\", \"hypothesis\": \"Pretrained N-scaling: FewNERD N=16 with Qwen2.5-7B-Instruct. Fills pretrained N-scaling curve (N=8/16/32) for FewNERD. FewNERD pretrained N=8 showed +3.90pp MV gain. Tests monotonic scaling.\", \"spec\": {\"command\": \"python -u code/run_mvp_pilot.py --model_path /root/autodl-tmp/.hf_cache/Qwen2.5-7B-Instruct --data_dir data/fewnerd/ --dataset fewnerd --subtask ner --n_samples 16 --temperature 1.0 --seed 42 --collect_logprobs --output_dir output/fewnerd_pretrained_n16_seed42/\", \"server\": \"autodl-5090-c\", \"gpu\": [\"cuda:1\"], \"pid\": \"392445\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_fewnerd_pretrained_n16_s42.log\", \"submitted_at\": \"2026-05-22T05:31:03.030Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_count\": 37648, \"data_path\": \"data/fewnerd/\", \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": 42, \"wall_clock_seconds\": 35365.7, \"gpu_hours\": 9.82}, \"conclusion\": \"failed\", \"metrics\": {\"crash_reason\": \"UnicodeEncodeError in sampling.py:675 — vLLM lone Unicode surrogates in output, UTF-8 encoding rejects\", \"progress\": \"72% (27110/37648)\", \"fix_applied\": \"sampling.py line 673: errors='replace' added to file write\"}, \"checkpoint_path\": \"output/fewnerd_pretrained_n16_seed42/ (partial, 72%)\", \"completed_at\": \"2026-05-22T15:20:28.681Z\"}, \"exp_conll_freeform_n8_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T09:09:24.843Z\", \"updated_at\": \"2026-05-22T15:19:57.307Z\", \"hypothesis\": \"Free-form decoding ablation: CoNLL N=8 T=1.0 seed=42 with use_grammar=False. Tests whether removing XGrammar constrained decoding degrades extraction quality and consistency scores, quantifying the contribution of grammar constraints to the structured self-consistency pipeline.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 8 --temperature 1.0 --seed 42 --use_grammar false --collect_logprobs --output_dir output/conll_freeform_n8_seed42\", \"server\": \"autodl-5090\", \"data_path\": \"data/conll2003\", \"data_count\": 3453, \"model_name\": \"qwen3-8b-conll2003-merged\", \"seed\": 42}, \"metrics\": {\"greedy_f1\": 0.9046, \"mv_strict_f1\": 0.8994, \"mv_delta_pp\": -0.52, \"lp_f1\": 0.8951, \"lp_delta_pp\": -0.95, \"degeneracy_rate\": 0.6, \"lp_std_ratio\": 0.023466, \"n_instances\": 2756, \"vs_constrained\": {\"greedy_f1_delta\": -0.0042, \"mv_delta_change\": \"+0.43pp (less hurt)\", \"degen_delta\": \"+3.0pp (higher in freeform)\", \"lp_std_ratio_delta\": -0.0022}}, \"conclusion\": \"success\", \"checkpoint_path\": \"output/conll_freeform_n8_seed42/\", \"log_path\": \"output/conll_freeform_n8_seed42/eval_results.json\", \"completed_at\": \"2026-05-22T15:19:57.307Z\"}, \"exp_fewnerd_freeform_n8_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T10:59:53.518Z\", \"updated_at\": \"2026-05-22T15:19:53.873Z\", \"hypothesis\": \"R35-W6 free-form decoding ablation: FewNERD N=8 T=1.0 seed=42 without grammar constraints. FewNERD has lowest degeneracy (12% at N=8). If free-form degeneracy remains low (~12%), confirms degeneracy is model-intrinsic, not a constrained decoding artifact. Complements CoNLL free-form ablation (59.3% vs 56.7% constrained).\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-fewnerd-exp021-merged --data_dir data/fewnerd --dataset fewnerd --subtask ner --n_samples 8 --temperature 1.0 --seed 42 --use_grammar false --collect_logprobs --output_dir output/fewnerd_freeform_n8_seed42\", \"server\": \"autodl-5090\", \"data_path\": \"data/fewnerd\", \"data_count\": 37648, \"model_name\": \"qwen3-8b-fewnerd-exp021-merged\", \"seed\": 42}, \"metrics\": {\"greedy_f1\": 0.7913, \"mv_strict_f1\": 0.7586, \"mv_delta_pp\": -3.26, \"lp_f1\": 0.7922, \"lp_delta_pp\": 0.09, \"degeneracy_rate\": 0.091, \"n_instances\": 32565, \"vs_constrained\": {\"greedy_f1_delta\": \"+0.00pp\", \"mv_delta_change\": \"+0.01pp (identical)\", \"lp_delta_change\": \"+0.02pp (identical)\", \"degen_delta\": \"0.0pp (identical)\"}, \"note\": \"Freeform ≈ constrained on FewNERD. All deltas <0.02pp. Degeneracy 9.1% both. Fine-grained entity types constrain output space enough that grammar constraints have no additional effect.\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"output/fewnerd_freeform_n8_seed42/\", \"log_path\": \"output/fewnerd_freeform_n8_seed42/eval_results.json\", \"completed_at\": \"2026-05-22T15:19:53.873Z\"}, \"exp_fewnerd_5epoch_lp_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T11:29:05.006Z\", \"updated_at\": \"2026-05-22T13:49:20.172Z\", \"hypothesis\": \"FewNERD 5-epoch checkpoint with LP selection will show improved F1 over majority voting, similar to the 3-epoch results, validating that LP selection is robust across training epochs\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:3\", \"spec\": {\"command\": \"python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-fewnerd-5epoch-merged --data_dir data/fewnerd/ --dataset fewnerd --subtask ner --n_samples 8 --temperature 1.0 --seed 42 --collect_logprobs --output_dir output/fewnerd_5epoch_lp_seed42/\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:3\", \"pid\": \"137895\", \"data_path\": \"data/fewnerd/\", \"data_count\": 37648, \"model_name\": \"qwen3-8b-fewnerd-5epoch-merged\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/qwen3-8b-fewnerd-5epoch-merged\", \"log_path\": \"/tmp/exp_fewnerd_5epoch_lp_s42.log\"}, \"conclusion\": \"success\", \"metrics\": {\"greedy_f1\": 0.7942, \"oracle_headroom_pp\": 8.06, \"fleiss_kappa\": 0.529, \"lp_auroc\": 0.662, \"lp_rho\": 0.302, \"lp_delta_pp_cpu_recompute\": 0.12, \"lp_delta_pp_cpu_recompute_std\": 0.04, \"note\": \"GPU inference completed after kill; CPU recompute from existing samples gave LP Δ=+0.12±0.04pp (2-seed)\"}, \"checkpoint_path\": \"output/fewnerd_5epoch_lp_seed42/\", \"log_path\": \"/tmp/exp_fewnerd_5epoch_lp_s42.log\", \"completed_at\": \"2026-05-22T13:49:20.172Z\"}, \"exp_fewnerd_mf4_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T05:08:56.774Z\", \"updated_at\": \"2026-05-22T13:47:03.042Z\", \"hypothesis\": \"MF4 pipeline fix: FewNERD N=8 T=1.0 seed=42 using run_mvp_pilot.py (greedy_f1/micro-F1). Replaces exp_021 which used incompatible greedy_macro_f1 metric. Required for 3-seed statistical power with unified pipeline.\", \"conclusion\": \"success\", \"server\": \"autodl-5090-c\", \"gpu\": \"cuda:0\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-fewnerd-exp021-merged --data_dir data/fewnerd/ --dataset fewnerd --subtask ner --n_samples 8 --temperature 1.0 --seed 42 --collect_logprobs --output_dir output/fewnerd_mf4_seed42/\\\"\", \"server\": \"autodl-5090-c\", \"gpu\": [\"cuda:0\"], \"pid\": \"426032\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_fewnerd_mf4_s42.log\", \"submitted_at\": \"2026-05-22T10:36:09.271Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"output/fewnerd_mf4_seed42/\", \"wall_clock_seconds\": 11055.7, \"gpu_hours\": 3.07}, \"pid\": \"426032\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_fewnerd_mf4_s42.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-fewnerd-exp021-merged --data_dir data/fewnerd/ --dataset fewnerd --subtask ner --n_samples 8 --temperature 1.0 --seed 42 --collect_logprobs --output_dir output/fewnerd_mf4_seed42/\\\"\", \"finished_at\": \"2026-05-22T12:43:03.188Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-22T12:43:16.831060+00:00\"}]}, \"metrics\": {\"greedy_f1\": 0.7911, \"oracle_f1\": 0.8787, \"mv_strict_f1\": 0.7585, \"mv_delta_pp\": -3.27, \"lp_f1\": 0.7918, \"lp_delta_pp\": 0.07, \"degeneracy_rate\": 0.091, \"oracle_headroom_pp\": 8.76, \"fleiss_kappa_mean\": 0.3537, \"soft_jaccard_mean\": 0.6751, \"rho_sj_full\": 0.1648, \"rho_sj_cond\": 0.1989, \"note\": \"MV/LP/degen from 3-seed unified recompute on gold-nonempty subset (n=32565)\"}, \"completed_at\": \"2026-05-22T13:40:24.973Z\"}, \"exp_fewnerd_n32_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T02:47:21.739Z\", \"updated_at\": \"2026-05-22T11:25:22.343Z\", \"hypothesis\": \"N-scaling convergence test: at N=32 (4× current N=8), MV strict Δ remains negative on FewNERD finetuned model, demonstrating that the selection gap does not close at practical sample budgets. If MV Δ converges toward 0 slowly, this quantifies the impractical N required. Motivated by R34 C1 and Reviewer #107 P2.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-fewnerd-exp021-merged --data_dir data/fewnerd --dataset fewnerd --subtask ner --n_samples 32 --temperature 1.0 --seed 42 --collect_logprobs --output_dir output/fewnerd_n32_seed42\\\"\", \"server\": \"autodl-5090-c\", \"gpu\": [\"cuda:0\"], \"pid\": \"381640\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_fewnerd_n32_s42.log\", \"submitted_at\": \"2026-05-22T02:49:01.089Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/fewnerd/test.json\", \"data_count\": 37648, \"model_name\": \"qwen3-8b-fewnerd-exp021-merged\", \"seed\": 42, \"n_samples\": 32, \"checkpoint_path\": \"output/fewnerd_n32_seed42/\", \"wall_clock_seconds\": 26683.2, \"gpu_hours\": 7.41}, \"metrics\": {\"greedy_f1\": 0.7914, \"mv_strict_f1\": 0.7818, \"mv_delta_strict_pp\": -0.96, \"mv_delta_unified_pp\": -0.91, \"unified_greedy_f1\": 0.7909, \"oracle_f1\": 0.9305, \"degeneracy_rate\": 0.014}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T10:13:44.264Z\"}, \"exp_fewnerd_mf4_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T05:08:59.588Z\", \"updated_at\": \"2026-05-22T10:38:33.442Z\", \"hypothesis\": \"MF4 pipeline fix: FewNERD N=8 T=1.0 seed=123 using run_mvp_pilot.py (greedy_f1/micro-F1). Replaces exp_021 which used incompatible greedy_macro_f1 metric. Required for 3-seed statistical power with unified pipeline.\", \"conclusion\": \"failed\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:2\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-fewnerd-exp021-merged --data_dir data/fewnerd/ --dataset fewnerd --subtask ner --n_samples 8 --temperature 1.0 --seed 123 --collect_logprobs --output_dir output/fewnerd_mf4_seed123/\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"132631\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_fewnerd_mf4_s123.log\", \"submitted_at\": \"2026-05-22T10:36:19.234Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 35.7, \"gpu_hours\": 0.01}, \"pid\": \"132631\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_fewnerd_mf4_s123.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-fewnerd-exp021-merged --data_dir data/fewnerd/ --dataset fewnerd --subtask ner --n_samples 8 --temperature 1.0 --seed 123 --collect_logprobs --output_dir output/fewnerd_mf4_seed123/\\\"\", \"finished_at\": \"2026-05-22T10:36:49.910Z\"}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"completed_at\": \"2026-05-22T10:36:54.915Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-22T10:37:02.423725+00:00\"}]}, \"notes\": \"失败原因: EXIT_CODE=1, wall_clock=35.7s (初始化阶段崩溃) | 诊断中: fix_worker_id: worker_diagnose_exp_fewnerd_mf4_s123_20260522T103817 | 同 pipeline s42/s456 在 autodl-5090-c 正常运行\"}, \"exp_conll_pretrained_n64_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T04:13:43.979Z\", \"updated_at\": \"2026-05-22T10:14:17.274Z\", \"hypothesis\": \"Pretrained N-scaling: CoNLL N=64 with Qwen2.5-7B-Instruct (unfinetuned). Fourth data point for pretrained CoNLL N-scaling curve (N=8 +3.01, N=32 +3.21). Tests whether pretrained MV gain continues scaling and whether degeneracy continues declining at N=64.\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && python -u code/run_mvp_pilot.py --model_path /root/autodl-tmp/models/Qwen2.5-7B-Instruct --data_dir data/conll2003/ --dataset conll2003 --subtask ner --n_samples 64 --temperature 1.0 --seed 42 --collect_logprobs --output_dir output/conll_pretrained_n64_seed42/'\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"118573\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_conll_pretrained_n64_s42.log\", \"submitted_at\": \"2026-05-22T07:33:43.097Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/conll2003/\", \"data_count\": 3453, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": 42, \"checkpoint_path\": \"output/conll_pretrained_n64_seed42/\", \"wall_clock_seconds\": 9634.2, \"gpu_hours\": 2.68}, \"server\": \"autodl-5090\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"autodl-5090\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-22T09:18:25.363Z\"}, \"metrics\": {\"greedy_f1\": 0.6005, \"mv_strict_f1\": 0.6316, \"mv_delta_strict_pp\": 3.11, \"oracle_f1\": 0.7703, \"degeneracy_rate\": 0.143}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T10:14:17.274Z\"}, \"exp_conll_pretrained_n16_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T04:13:20.987Z\", \"updated_at\": \"2026-05-22T10:12:07.173Z\", \"hypothesis\": \"Pretrained N-scaling: CoNLL N=16 with Qwen2.5-7B-Instruct (unfinetuned). Fills the N=16 gap in pretrained CoNLL N-scaling curve (N=8 +3.01pp, N=32 +3.21pp). Tests whether pretrained MV gain scales monotonically with N.\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && python -u code/run_mvp_pilot.py --model_path /root/autodl-tmp/models/Qwen2.5-7B-Instruct --data_dir data/conll2003/ --dataset conll2003 --subtask ner --n_samples 16 --temperature 1.0 --seed 42 --collect_logprobs --output_dir output/conll_pretrained_n16_seed42/'\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"118033\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_conll_pretrained_n16_s42.log\", \"submitted_at\": \"2026-05-22T07:33:36.117Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/conll2003/\", \"data_count\": 3453, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": 42, \"checkpoint_path\": \"output/conll_pretrained_n16_seed42/\", \"wall_clock_seconds\": 8614.2, \"gpu_hours\": 2.39}, \"server\": \"autodl-5090\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"autodl-5090\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-22T09:18:23.189Z\"}, \"metrics\": {\"greedy_f1\": 0.5986, \"mv_strict_f1\": 0.632, \"mv_delta_strict_pp\": 3.34, \"oracle_f1\": 0.7282, \"degeneracy_rate\": 0.255, \"alpha_crit_eff_strict\": 0.402}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T09:57:10.361Z\"}, \"exp_scierc_pretrained_n16_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T04:13:18.313Z\", \"updated_at\": \"2026-05-22T09:57:51.006Z\", \"hypothesis\": \"Pretrained N-scaling: SciERC N=16 with Qwen2.5-7B-Instruct. Fills pretrained N-scaling curve (N=8/16/32) for SciERC. Tests whether pretrained MV gain scales monotonically with N.\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && python -u code/run_mvp_pilot.py --model_path /root/autodl-tmp/.hf_cache/Qwen2.5-7B-Instruct --data_dir data/scierc/processed_data --dataset scierc --subtask ner --n_samples 16 --temperature 1.0 --seed 42 --collect_logprobs --output_dir output/scierc_pretrained_n16_seed42/'\", \"server\": \"autodl-5090-c\", \"gpu\": [\"cuda:1\"], \"pid\": \"389783\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_scierc_pretrained_n16_s42.log\", \"submitted_at\": \"2026-05-22T04:49:11.522Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": 42, \"checkpoint_path\": \"output/scierc_pretrained_n16_seed42/\", \"wall_clock_seconds\": 18519.5, \"gpu_hours\": 5.14}, \"metrics\": {\"greedy_f1\": 0.2486, \"mv_strict_f1\": 0.2628, \"mv_delta_strict_pp\": 1.42, \"oracle_f1\": 0.4323, \"degeneracy_rate\": 0.008, \"alpha_crit_eff_strict\": 0.1524}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T09:57:51.006Z\"}, \"exp_scierc_pretrained_n64_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T04:13:42.640Z\", \"updated_at\": \"2026-05-22T09:57:13.629Z\", \"hypothesis\": \"Pretrained N-scaling: SciERC N=64 with Qwen2.5-7B-Instruct (unfinetuned). Fourth data point for pretrained N-scaling curve (N=8 +1.43, N=16 +1.42, N=32 +1.97). Tests whether pretrained MV gain continues scaling at 8× budget.\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && python -u code/run_mvp_pilot.py --model_path /root/autodl-tmp/models/Qwen2.5-7B-Instruct --data_dir data/scierc/processed_data --dataset scierc --subtask ner --n_samples 64 --temperature 1.0 --seed 42 --collect_logprobs --output_dir output/scierc_pretrained_n64_seed42/'\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:1\"], \"pid\": \"118300\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_scierc_pretrained_n64_s42.log\", \"submitted_at\": \"2026-05-22T07:33:39.853Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": 42, \"checkpoint_path\": \"output/scierc_pretrained_n64_seed42/\", \"wall_clock_seconds\": 8613.8, \"gpu_hours\": 2.39}, \"server\": \"autodl-5090\", \"gpu\": \"cuda:3\", \"account\": \"root\", \"reproduce\": {\"server\": \"autodl-5090\", \"gpu\": \"cuda:3\", \"started_at\": \"2026-05-22T09:18:27.670Z\"}, \"metrics\": {\"greedy_f1\": 0.2432, \"mv_strict_f1\": 0.2717, \"mv_delta_strict_pp\": 2.85, \"oracle_f1\": 0.5017, \"degeneracy_rate\": 0, \"alpha_crit_eff_strict\": 0.122}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T09:57:13.629Z\"}, \"exp_conll_n32_s456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T06:41:52.575Z\", \"updated_at\": \"2026-05-22T07:19:37.115Z\", \"hypothesis\": \"N=32 multi-seed robustness: CoNLL N=32 finetuned seed=456. Third seed to complete 3-seed mean±σ (s42 +0.46pp, s123 +0.55pp). CoNLL shows stable MV gain at N=32; this confirms reproducibility.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-conll2003-merged --data_dir data/conll2003/ --dataset conll2003 --subtask ner --n_samples 32 --temperature 1.0 --seed 456 --collect_logprobs --output_dir output/conll_n32_seed456/\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"112189\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_conll_n32_s456.log\", \"submitted_at\": \"2026-05-22T06:43:01.923Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/conll2003/\", \"data_count\": 3453, \"model_name\": \"qwen3-8b-conll2003-merged\", \"seed\": 456, \"checkpoint_path\": \"output/conll_n32_seed456/\", \"wall_clock_seconds\": 2195.2, \"gpu_hours\": 0.61}, \"metrics\": {\"greedy_f1\": 0.9117, \"mv_strict_f1\": 0.9167, \"mv_delta_strict_pp\": 0.51, \"degeneracy_rate\": 0.401, \"oracle_f1\": 0.9686, \"alpha_crit_eff_strict\": 0.7614}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T07:19:37.115Z\"}, \"exp_scierc_n32_s456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T05:32:58.842Z\", \"updated_at\": \"2026-05-22T06:38:00.245Z\", \"hypothesis\": \"N=32 multi-seed robustness: SciERC N=32 finetuned seed=456. Third seed to reduce variance of MV Δ estimate at N=32 (s42 +0.78pp, s123 +0.12pp — high variance). Three seeds enable mean±σ reporting.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask ner --n_samples 32 --temperature 1.0 --seed 456 --collect_logprobs --output_dir output/scierc_n32_seed456/\\\"\", \"server\": \"autodl-5090-c\", \"gpu\": [\"cuda:2\"], \"pid\": \"393271\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_scierc_n32_s456.log\", \"submitted_at\": \"2026-05-22T05:33:11.546Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 456, \"checkpoint_path\": \"output/scierc_n32_seed456/\", \"wall_clock_seconds\": 3888.7, \"gpu_hours\": 1.08}, \"metrics\": {\"greedy_f1\": 0.6661, \"mv_strict_f1\": 0.6644, \"mv_delta_strict_pp\": -0.17, \"degeneracy_rate\": 0.04}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T06:38:00.245Z\"}, \"exp_conll_n64_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T04:08:16.160Z\", \"updated_at\": \"2026-05-22T06:37:44.085Z\", \"hypothesis\": \"N-scaling convergence test: CoNLL N=64 (8× N=8) finetuned model. CoNLL has highest degeneracy (~60% at N=8). Tests whether degeneracy continues declining and whether the marginal MV Δ improvement from N=16→32→64 is negligible. Fourth data point for N-scaling convergence curve. Part of extended N-scaling suite for R34 C1.\", \"spec\": {\"data_path\": \"data/conll2003/\", \"data_count\": 3453, \"model_name\": \"qwen3-8b-conll2003-merged\", \"seed\": 42, \"n_samples\": 64, \"checkpoint_path\": \"output/conll_n64_seed42/\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-conll2003-merged --data_dir data/conll2003/ --dataset conll2003 --subtask ner --n_samples 64 --temperature 1.0 --seed 42 --collect_logprobs --output_dir output/conll_n64_seed42/\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:3\"], \"pid\": \"101257\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_conll_n64_s42.log\"}, \"metrics\": {\"greedy_f1\": 0.912, \"mv_strict_f1\": 0.9184, \"mv_delta_strict_pp\": 0.64, \"oracle_f1\": 0.9751, \"degeneracy_rate\": 0.306}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T06:37:44.085Z\"}, \"exp_conll_pretrained_n32_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T04:08:24.768Z\", \"updated_at\": \"2026-05-22T06:35:17.379Z\", \"hypothesis\": \"Pretrained N-scaling: CoNLL N=32 with Qwen2.5-7B-Instruct (unfinetuned). CoNLL pretrained showed strong MV gain (+9.2pp at N=8). Tests whether this advantage scales with N, and whether the pretrained-vs-finetuned contrast (direction flip) persists at higher sample budget. Addresses reviewer concern about generalization.\", \"spec\": {\"data_path\": \"data/conll2003/\", \"data_count\": 3453, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": 42, \"n_samples\": 32, \"checkpoint_path\": \"output/conll_pretrained_n32_seed42/\", \"model_path\": \"/root/autodl-tmp/.hf_cache/Qwen2.5-7B-Instruct\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && python -u code/run_mvp_pilot.py --model_path /root/autodl-tmp/.hf_cache/Qwen2.5-7B-Instruct --data_dir data/conll2003/ --dataset conll2003 --subtask ner --n_samples 32 --temperature 1.0 --seed 42 --collect_logprobs --output_dir output/conll_pretrained_n32_seed42/\\\"\", \"server\": \"autodl-5090-c\", \"gpu\": [\"cuda:2\"], \"pid\": \"386211\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_conll_pretrained_n32_s42.log\"}, \"metrics\": {\"greedy_f1\": 0.5975, \"mv_strict_f1\": 0.6296, \"mv_delta_strict_pp\": 3.21, \"oracle_f1\": 0.7493, \"degeneracy_rate\": 0.188, \"alpha_crit_eff_strict\": 0.5657}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T06:35:17.379Z\"}, \"exp_conll_n32_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T04:13:24.532Z\", \"updated_at\": \"2026-05-22T06:35:13.680Z\", \"hypothesis\": \"N=32 multi-seed robustness: CoNLL N=32 finetuned seed=123. Second seed to verify CoNLL N=32 MV Δ (+0.46pp at seed=42). Tests whether the positive MV gain is reproducible.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-conll2003-merged --data_dir data/conll2003/ --dataset conll2003 --subtask ner --n_samples 32 --temperature 1.0 --seed 123 --collect_logprobs --output_dir output/conll_n32_seed123/\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:1\"], \"pid\": \"102911\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_conll_n32_s123.log\", \"submitted_at\": \"2026-05-22T04:14:47.896Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/conll2003/\", \"data_count\": 3453, \"model_name\": \"qwen3-8b-conll2003-merged\", \"seed\": 123, \"n_samples\": 32, \"checkpoint_path\": \"output/conll_n32_seed123/\", \"wall_clock_seconds\": 8425.8, \"gpu_hours\": 2.34}, \"metrics\": {\"greedy_f1\": 0.9123, \"mv_strict_f1\": 0.9177, \"mv_delta_strict_pp\": 0.55, \"oracle_f1\": 0.9717, \"degeneracy_rate\": 0.379, \"alpha_crit_eff_strict\": 0.7347}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T06:35:13.681Z\"}, \"exp_scierc_pretrained_n32_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T04:08:23.418Z\", \"updated_at\": \"2026-05-22T06:35:10.103Z\", \"hypothesis\": \"Pretrained N-scaling: SciERC N=32 with Qwen2.5-7B-Instruct (unfinetuned). Tests whether pretrained MV advantage persists at higher N, and whether per-type direction flip (pretrained positive vs finetuned negative) holds at N=32. Complements finetuned N=32 for generalization evidence. Addresses reviewer concern about generalization beyond finetuned setting.\", \"spec\": {\"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": 42, \"n_samples\": 32, \"checkpoint_path\": \"output/scierc_pretrained_n32_seed42/\", \"model_path\": \"/root/autodl-tmp/.hf_cache/Qwen2.5-7B-Instruct\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && python -u code/run_mvp_pilot.py --model_path /root/autodl-tmp/.hf_cache/Qwen2.5-7B-Instruct --data_dir data/scierc/processed_data --dataset scierc --subtask ner --n_samples 32 --temperature 1.0 --seed 42 --collect_logprobs --output_dir output/scierc_pretrained_n32_seed42/\\\"\", \"server\": \"autodl-5090-c\", \"gpu\": [\"cuda:1\"], \"pid\": \"385943\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_scierc_pretrained_n32_s42.log\"}, \"metrics\": {\"greedy_f1\": 0.2446, \"mv_strict_f1\": 0.2643, \"mv_delta_strict_pp\": 1.97, \"mv_incl_f1\": 0.2668, \"oracle_f1\": 0.4729, \"degeneracy_rate\": 0.002, \"alpha_crit_eff_strict\": 0.1526}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T06:35:10.103Z\"}, \"exp_scierc_n32_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T04:13:23.071Z\", \"updated_at\": \"2026-05-22T06:15:51.468Z\", \"hypothesis\": \"N=32 multi-seed robustness: SciERC N=32 finetuned seed=123. Second seed to verify the MV Δ sign flip at N=32 (seed=42 showed +0.78pp). If consistent across seeds, strengthens the N-scaling convergence claim.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask ner --n_samples 32 --temperature 1.0 --seed 123 --collect_logprobs --output_dir output/scierc_n32_seed123/\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"102642\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_scierc_n32_s123.log\", \"submitted_at\": \"2026-05-22T04:14:44.712Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 123, \"n_samples\": 32, \"checkpoint_path\": \"output/scierc_n32_seed123/\", \"wall_clock_seconds\": 7266.8, \"gpu_hours\": 2.02}, \"metrics\": {\"greedy_f1\": 0.6663, \"mv_strict_f1\": 0.6675, \"mv_delta_strict_pp\": 0.12, \"mv_incl_f1\": 0.6722, \"oracle_f1\": 0.8404, \"degeneracy_rate\": 0.051, \"alpha_crit_eff_strict\": 0.3511}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T06:15:51.468Z\"}, \"exp_scierc_n64_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T04:08:13.729Z\", \"updated_at\": \"2026-05-22T06:15:47.713Z\", \"hypothesis\": \"N-scaling convergence test: SciERC N=64 (8× N=8) finetuned model. Fourth data point (N=8/16/32/64) establishes convergence trend of MV Δ and degeneracy rate. If MV Δ remains negative at N=64, the gap is demonstrably persistent at practical budgets. Part of extended N-scaling suite for R34 C1.\", \"spec\": {\"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 42, \"n_samples\": 64, \"checkpoint_path\": \"output/scierc_n64_seed42/\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask ner --n_samples 64 --temperature 1.0 --seed 42 --collect_logprobs --output_dir output/scierc_n64_seed42/\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"100988\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_scierc_n64_s42.log\"}, \"metrics\": {\"greedy_f1\": 0.6673, \"mv_strict_f1\": 0.6735, \"mv_delta_strict_pp\": 0.63, \"mv_incl_f1\": 0.6725, \"oracle_f1\": 0.8626, \"degeneracy_rate\": 0.021, \"alpha_crit_eff_strict\": 0.3407}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T06:15:47.713Z\"}, \"exp_scierc_n16_s42\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-21T11:35:58.608Z\", \"updated_at\": \"2026-05-22T04:15:13.580Z\", \"hypothesis\": \"N-scaling test: SciERC N=16 (2× N=8) finetuned model. Measures MV strict Δ, degeneracy, LP-best F1 at increased sample budget. Baseline: N=8 MV Δ near 0, degeneracy 12.2%. If MV Δ remains ≤0 at N=16, selection gap persists at 2× budget. Part of N-scaling suite for R34 C1.\", \"parent\": \"exp_scierc_n16_s123\", \"completed_at\": \"2026-05-21T13:03:15.016Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"greedy_f1\": 0.663, \"oracle_f1\": 0.809, \"oracle_headroom\": 0.146, \"rho_fk_cond\": 0.128, \"rho_sj_cond\": 0.326, \"logprob_rho_cond\": 0.16, \"structural_beats_surface\": true, \"verdict\": \"MARGINAL\"}}}, \"spec\": {\"command\": \"python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --dataset scierc --n_samples 16 --temperature 1.0 --seed 42\", \"server\": \"autodl-5090-c\", \"data_path\": \"data/scierc/\", \"data_count\": 551, \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/qwen3-8b-scierc-merged-v2\", \"eval_data\": \"data/scierc/processed_data/\", \"checkpoint_path\": \"output/scierc_n16_s42/\", \"log_path\": \"output/scierc_n16_s42/\"}, \"conclusion\": \"success\", \"metrics\": {\"greedy_f1\": 0.6651, \"oracle_f1\": 0.8179, \"mv_strict_f1\": 0.6622, \"mv_delta_strict_pp\": -0.29, \"degeneracy_rate\": 0.076, \"alpha_crit_eff_strict\": 0.3597, \"mv_f1\": 0.6607, \"degeneracy\": 0.07, \"n_instances\": 529, \"note\": \"mv_strict metrics from recompute; mv_f1/degeneracy from original report\"}}, \"exp_conll_n32_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T03:36:00.871Z\", \"updated_at\": \"2026-05-22T04:14:01.866Z\", \"hypothesis\": \"N-scaling test: CoNLL N=32 (4× N=8) finetuned model. High-degeneracy regime (~62% at N=8). Tests whether 4× budget reduces degeneracy enough for MV to become positive. If not, demonstrates structural ceiling independent of sample budget. Part of N-scaling suite for R34 C1.\", \"spec\": {\"command\": \"bash -c \\\"...run_mvp_pilot.py --n_samples 32 --dataset conll2003 --seed 42\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:1\"], \"pid\": \"98095\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_conll_n32_s42.log\", \"submitted_at\": \"2026-05-22T03:36:24.632Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/conll2003/test.json\", \"data_count\": 3453, \"model_name\": \"qwen3-8b-conll2003-merged\", \"seed\": 42, \"n_samples\": 32, \"checkpoint_path\": \"checkpoints/qwen3-8b-conll2003-merged\", \"wall_clock_seconds\": 2257.2, \"gpu_hours\": 0.63}, \"metrics\": {\"greedy_f1\": 0.912, \"mv_strict_f1\": 0.9166, \"mv_delta_strict_pp\": 0.46, \"mv_incl_f1\": 0.9169, \"oracle_f1\": 0.969, \"degeneracy_rate\": 0.405, \"alpha_crit_strict\": 0.456}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T04:14:01.866Z\"}, \"exp_scierc_n32_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T03:35:58.707Z\", \"updated_at\": \"2026-05-22T04:11:21.655Z\", \"hypothesis\": \"N-scaling test: SciERC N=32 (4× N=8) finetuned model. Tests whether quadrupling sample budget closes the selection gap on medium-difficulty dataset. Cross-dataset complement to FewNERD N=32 (running on 5090-c). Part of N-scaling suite for R34 C1.\", \"spec\": {\"command\": \"bash -c \\\"...run_mvp_pilot.py --n_samples 32 --dataset scierc --seed 42\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"97955\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_scierc_n32_s42.log\", \"submitted_at\": \"2026-05-22T03:36:21.658Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scierc/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 42, \"n_samples\": 32, \"checkpoint_path\": \"checkpoints/qwen3-8b-scierc-merged-v2\", \"wall_clock_seconds\": 2100.0, \"gpu_hours\": 0.58}, \"metrics\": {\"greedy_f1\": 0.6629, \"mv_strict_f1\": 0.6706, \"mv_delta_strict_pp\": 0.78, \"mv_incl_f1\": 0.6708, \"oracle_f1\": 0.8399, \"degeneracy_rate\": 0.036, \"alpha_crit_eff_strict\": 0.3438, \"note\": \"Strict MV turns positive at N=32. Gold-nonempty filtered.\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T04:11:21.655Z\"}, \"exp_conll_mf4_v2_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T10:17:06.386Z\", \"updated_at\": \"2026-05-22T04:06:11.228Z\", \"hypothesis\": \"MF4 pipeline fix v2: CoNLL N=8 T=1.0 seed=42 using run_mvp_pilot.py (greedy_f1/micro-F1). Third seed completing 3-seed set for statistical power. α_crit noted only 2-seed for CoNLL.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-conll2003-merged --data_dir data/conll2003/ --dataset conll2003 --subtask ner --n_samples 8 --temperature 1.0 --seed 42 --collect_logprobs --output_dir output/conll_mf4v2_seed42/\", \"server\": \"autodl-5090-c\", \"data_path\": \"data/conll2003/\", \"data_count\": 3453, \"model_name\": \"qwen3-8b-conll2003-merged\", \"seed\": 42, \"checkpoint_path\": \"output/conll_mf4v2_seed42/\", \"log_path\": \"/tmp/exp_conll_mf4_v2_s42.log\"}, \"conclusion\": \"success\", \"metrics\": {\"greedy_f1\": 0.9123, \"mv_strict_f1\": 0.9101, \"mv_delta_strict_pp\": -0.22, \"oracle_f1\": 0.9538, \"degeneracy_rate\": 0.601, \"alpha_crit_eff_strict\": 2.0903, \"mv_f1\": 0.909, \"fleiss_kappa\": 0.7729, \"soft_jaccard\": 0.8949, \"note\": \"MV strict metrics from recompute on gold-nonempty subset (autodl-5090-c)\"}, \"completed_at\": \"2026-05-21T10:55:03.879Z\"}, \"exp_scierc_mf4_v2_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T09:01:28.521Z\", \"updated_at\": \"2026-05-22T04:05:39.776Z\", \"spec\": {\"command\": \"python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask ner --n_samples 8 --temperature 1.0 --seed 42 --collect_logprobs --output_dir output/scierc_mf4v2_seed42/\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"18393\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_scierc_mf4_v2_s42.log\", \"submitted_at\": \"2026-05-21T09:08:39.861Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 529, \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 42, \"checkpoint_path\": \"output/scierc_mf4v2_seed42/\", \"wall_clock_seconds\": 6403.0, \"gpu_hours\": 1.78}, \"conclusion\": \"success\", \"metrics\": {\"greedy_f1\": 0.6683, \"mv_strict_f1\": 0.6558, \"mv_delta_strict_pp\": -1.24, \"oracle_f1\": 0.784, \"degeneracy_rate\": 0.134, \"alpha_crit_eff_strict\": 0.3859, \"fleiss_kappa\": 0.4026, \"soft_jaccard\": 0.7075, \"logprob_rho_full\": 0.2098, \"note\": \"MV metrics from recompute on gold-nonempty subset\"}, \"hypothesis\": \"MF4v2 pipeline (N=8, T=1.0, logprobs) on SciERC with seed 42 produces consistent SC diagnostic signals (structural agreement > logprob baseline for quality estimation), validating cross-seed stability of the structured self-consistency framework on scientific NER.\", \"completed_at\": \"2026-05-21T10:55:22.891Z\"}, \"exp_conll_n16_s42\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-21T03:11:59.589Z\", \"updated_at\": \"2026-05-22T04:04:50.944Z\", \"hypothesis\": \"N-scaling test: CoNLL N=16 (2× N=8) finetuned model. CoNLL has highest degeneracy (~62%) at N=8. If degeneracy increases further at N=16, confirms sampling diversity collapse scales with N. Part of N-scaling suite for R34 C1.\", \"completed_at\": \"2026-05-21T04:24:19.862Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"greedy_f1\": 0.908, \"oracle_f1\": 0.959, \"rho_SJ_full\": 0.446, \"rho_FK_full\": 0.427, \"rho_advantage\": 0.019, \"oracle_headroom\": 0.051, \"degeneracy_pct\": 7.8, \"verdict\": \"PASS\"}}}, \"spec\": {\"command\": \"python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-conll2003-merged --data_dir data/conll2003/ --dataset conll2003 --subtask ner --n_samples 16 --temperature 1.0 --seed 42 --collect_logprobs --output_dir output/conll_n16_s42/\", \"server\": \"autodl-5090-c\", \"gpu\": [\"cuda:2\"], \"pid\": \"312281\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_conll_n16_s42.log\", \"submitted_at\": \"2026-05-21T11:24:02.614Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/conll2003/\", \"data_count\": 0, \"model_name\": \"qwen3-8b-conll2003-merged\", \"seed\": 42, \"checkpoint_path\": \"output/conll_n16_s42/\", \"wall_clock_seconds\": 2099.3, \"gpu_hours\": 0.58}, \"conclusion\": \"success\", \"metrics\": {\"greedy_f1\": 0.908, \"oracle_f1\": 0.959, \"mv_strict_f1\": 0.9148, \"mv_delta_strict_pp\": 0.19, \"degeneracy_rate\": 0.497, \"alpha_crit_eff_strict\": 1.6749, \"capture_rate_pct\": 3.8, \"rho_SJ_full\": 0.446, \"rho_FK_full\": 0.427, \"note\": \"MV metrics from gold-nonempty subset (n=2756/3453); greedy/oracle from full set\"}}, \"exp_fewnerd_mf4v2_s123_v4\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T21:44:24.500Z\", \"updated_at\": \"2026-05-21T23:52:23.871Z\", \"hypothesis\": \"FewNERD MF4v2 s123 v4: regenerate finetuned FewNERD seed=123 instance-level samples.jsonl on autodl-5090-c for v4 MV unified recompute. N=8, T=1.0, seed=123. Model: qwen3-8b-fewnerd-exp021-merged. Parent retries v2 (failed on 5090) and v3 (killed). Using confirmed-working 5090-c environment from s456_v3.\", \"parent\": \"exp_fewnerd_mf4v2_s123_v2\", \"conclusion\": \"killed\"}, \"exp_fewnerd_mf4v2_s42_v4\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T21:44:21.426Z\", \"updated_at\": \"2026-05-21T23:52:22.502Z\", \"hypothesis\": \"Superseded: v3 (exp_fewnerd_mf4v2_s42_v3) already succeeded. This v4 retry is no longer needed.\", \"parent\": \"exp_fewnerd_mf4v2_s42_v2\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-fewnerd-exp021-merged --data_dir data/fewnerd/ --dataset fewnerd --subtask ner --n_samples 8 --temperature 1.0 --seed 42 --collect_logprobs --output_dir output/fewnerd_mf4v2_seed42_v4/\\\"\", \"server\": \"autodl-5090-c\", \"gpu\": [\"cuda:0\"], \"pid\": \"366486\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_fewnerd_mf4v2_s42_v4.log\", \"submitted_at\": \"2026-05-21T22:07:08.807Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"killed\"}, \"exp_fewnerd_mf4v2_s123_v2\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T14:22:39.175Z\", \"updated_at\": \"2026-05-21T23:52:20.833Z\", \"hypothesis\": \"FewNERD MF4v2 s123 re-run: original died without output on autodl-5090. Generating instance-level samples.jsonl for MV unified recompute with seed=123, N=8, T=1.0.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-fewnerd-exp021-merged --data_dir data/fewnerd/ --dataset fewnerd --subtask ner --n_samples 8 --temperature 1.0 --seed 123 --collect_logprobs --output_dir output/fewnerd_mf4v2_seed123/\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"47490\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_fewnerd_mf4v2_s123_v2.log\", \"submitted_at\": \"2026-05-21T14:22:51.896Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"killed\"}, \"exp_fewnerd_mf4v2_s42_v2\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T14:22:37.754Z\", \"updated_at\": \"2026-05-21T23:52:19.142Z\", \"hypothesis\": \"FewNERD MF4v2 s42 re-run: original died without output on autodl-5090. Generating instance-level samples.jsonl for MV unified recompute with seed=42, N=8, T=1.0.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-fewnerd-exp021-merged --data_dir data/fewnerd/ --dataset fewnerd --subtask ner --n_samples 8 --temperature 1.0 --seed 42 --collect_logprobs --output_dir output/fewnerd_mf4v2_seed42/\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:1\"], \"pid\": \"48238\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_fewnerd_mf4v2_s42_v2.log\", \"submitted_at\": \"2026-05-21T14:23:27.532Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"killed\"}, \"eval_scd_fewnerd_fallback\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T19:11:25.544Z\", \"updated_at\": \"2026-05-21T23:52:13.602Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && bash run_scd_fewnerd_eval.sh\\\"\", \"server\": \"autodl-5090-b\", \"gpu\": [\"cuda:0\"], \"pid\": \"270397\", \"log_path\": \"~/runs/struct_self_consist_ie/eval_scd_fewnerd_fallback.log\", \"submitted_at\": \"2026-05-20T19:11:24.918Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"killed\"}, \"exp_a1_spider_sql_sc\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T18:15:12.865Z\", \"updated_at\": \"2026-05-21T23:52:12.126Z\", \"hypothesis\": \"Cross-task universality: SC diagnostic cascade (degeneracy, LP-quality gap, agreement-correctness correlation) applies to SQL structured generation on Spider. Qwen2.5-7B-Instruct base model, 200 dev examples, N=8 T=1.0, execution accuracy evaluation. If F1-F4 failure modes exist in SQL, the framework generalizes beyond NER.\", \"server\": \"autodl-5090-b\", \"gpu\": \"cuda:2\", \"conclusion\": \"killed\"}, \"exp_b2_v4_inverse_frequency\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T12:50:51.737Z\", \"updated_at\": \"2026-05-21T23:52:10.386Z\", \"hypothesis\": \"Inverse-frequency weighting of entity features (agreement_count, vc, sj normalized by log(1+type_freq)) improves cross-domain generalization by reducing dominance of high-frequency entity types. Two variants: A) replace original features, B) augment as additional features.\", \"conclusion\": \"killed\", \"metrics\": {\"variant_a_replace_fold3_lgb_auc\": 0.834, \"variant_a_replace_fold3_ece\": 0.2188, \"variant_a_f1_delta\": -0.013, \"variant_b_augment_fold3_lgb_auc\": 0.8541, \"variant_b_augment_fold3_ece\": 0.1934, \"variant_b_f1_delta\": -0.009, \"sj_ifw_std_reduction\": \"54% (0.138→0.063)\", \"ac_ifw_std_reduction\": \"10% (0.122→0.110)\", \"verdict\": \"IFW improves stability but reduces discriminative power. Augment variant neutral. Replace variant harmful.\"}, \"parent\": \"exp_b2_entity_verifier\"}, \"exp_b2_v3_domain_invariant\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T12:50:49.948Z\", \"updated_at\": \"2026-05-21T23:52:04.266Z\", \"hypothesis\": \"Removing domain-specific features (dataset_enc, entity_type distributions) forces the verifier to rely on domain-invariant signals, improving cross-domain generalization at the cost of some discriminative power. If LGB AUC improves on held-out domains, domain features were causing negative transfer.\", \"conclusion\": \"killed\", \"metrics\": {\"fold3_fewnerd_lgb_auc\": 0.8562, \"fold3_fewnerd_xgb_auc\": 0.8518, \"fold3_ece\": 0.1373, \"fold2_scierc_lgb_auc\": 0.8152, \"fold2_scierc_xgb_auc\": 0.8163, \"vs_v2_fold3_lgb_delta\": 0.0085, \"vs_v2_fold2_lgb_delta\": 0.0146, \"top_features\": \"agreement_count (58.4%) + vc (30.3%) = 88%\", \"verdict\": \"LGB AUC improved by removing domain features, confirming negative transfer. But ECE still high, F1 delta still negative.\"}, \"parent\": \"exp_b2_entity_verifier\"}, \"exp_b2_v2_multi_domain_joint\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T12:50:09.686Z\", \"updated_at\": \"2026-05-21T23:52:02.575Z\", \"hypothesis\": \"Joint multi-domain training (CoNLL+SciERC+FewNERD LODO) improves entity verifier AUC and cross-domain construction F1 by exposing the model to diverse entity patterns. Tests whether training data diversity overcomes the calibration gap that caused B2 original to fail on FewNERD.\", \"conclusion\": \"killed\", \"metrics\": {\"fold3_fewnerd_lgb_auc\": 0.8477, \"fold3_fewnerd_xgb_auc\": 0.8603, \"fold3_fewnerd_f1_delta\": -0.008, \"fold3_ece\": 0.136, \"fold4_iid_ece\": 0.007, \"vs_b2_original_lgb_auc_delta\": 0.014, \"vs_b2_original_xgb_auc_delta\": 0.032, \"verdict\": \"AUC improved but F1 still negative. Cross-domain calibration gap unsolved.\"}, \"parent\": \"exp_b2_entity_verifier\"}, \"exp_b2_entity_verifier\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T10:13:41.037Z\", \"updated_at\": \"2026-05-21T23:52:00.772Z\", \"hypothesis\": \"An XGBoost/LightGBM entity-level verifier trained on agreement_count, VC, LP features can predict whether entity candidates are in gold annotations, enabling post-hoc filtering or score-weighted construction that improves over greedy baseline, with cross-dataset generalization from CoNLL+SciERC to FewNERD+WNUT.\", \"metrics\": {\"oof_auc\": 0.9233, \"oof_path_a_f1_delta\": 0.003, \"oof_path_b_f1_delta\": -0.0157, \"oof_greedy_f1\": 0.8216, \"oof_path_a_f1\": 0.8246, \"oof_majority_vote_f1\": 0.8048, \"leakage_pct\": 91, \"original_delta_pp\": 3.62, \"oof_delta_pp\": 0.3, \"per_dataset\": {\"scierc\": \"+1.28pp\", \"conll\": \"+0.55pp\", \"fewnerd\": \"+0.02pp\"}, \"verdict\": \"B2 verifier gain was 91% leakage. OOF Path A +0.30pp not significant. NOT suitable for paper §5.\", \"n_inverse_scaling_validation\": {\"subset_n\": 4351, \"full_n\": 32565, \"subset_greedy_f1\": 0.7926, \"full_greedy_f1\": 0.7913, \"verdict\": \"Not a bug. Representative subset. Paper should note subset size.\"}}, \"conclusion\": \"killed\"}, \"exp_a2_degen_regression\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T10:13:37.615Z\", \"updated_at\": \"2026-05-21T23:51:58.845Z\", \"hypothesis\": \"Degeneracy rate is primarily driven by task difficulty (dataset entropy ceiling) rather than model capability, with a positive correlation between base F1 and degeneracy — easy tasks with high F1 produce degenerate outputs because the model has already converged.\", \"metrics\": {\"n_points\": 30, \"linear_r2\": 0.414, \"quadratic_r2\": 0.592, \"spearman_rho\": 0.519, \"spearman_p\": 0.0033, \"linear_coeff\": \"degen = 129.5 × F1 - 56.9\", \"key_finding\": \"degeneracy driven by dataset difficulty (entropy ceiling), not model capability\"}, \"conclusion\": \"killed\"}, \"exp_e1_signal_routing\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T10:13:34.839Z\", \"updated_at\": \"2026-05-21T23:51:57.093Z\", \"hypothesis\": \"A config-level signal router (RF/LR) can predict the optimal construction signal per config from features (degeneracy_rate, base_f1, oracle_headroom), outperforming always-LP baseline. Router ΔF1 should exceed always-LP ΔF1.\", \"metrics\": {\"n_configs\": 16, \"rf_loo_accuracy\": 0.562, \"router_avg_delta_f1\": 0.39, \"always_lp_delta_f1\": 0.15, \"oracle_delta_f1\": 0.56, \"top_features\": [\"oracle_headroom\", \"degeneracy_rate\", \"base_f1\"], \"label_dist\": {\"lp_selection\": 6, \"none\": 5, \"consensus_theta2n\": 3, \"consensus_lp_weighted\": 1, \"majority_vote\": 1}}, \"conclusion\": \"killed\", \"notes\": \"E1 signal routing. RF 56.2% LOO accuracy (below 60% target) but router ΔF1 +0.39pp > always-LP +0.15pp (2.6× improvement, target met). Low accuracy due to small n=16 and class imbalance. D176: appendix-only, not main claim.\"}, \"exp_pareto_diversity_quality\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T09:31:45.421Z\", \"updated_at\": \"2026-05-21T23:51:55.294Z\", \"hypothesis\": \"There exists a Pareto frontier in the diversity (1-degeneracy) vs construction quality (ΔF1) space across temperature configurations. Well-separated temperature mixing (T=0.7+T=1.0) achieves Pareto optimality for both uniform and VC construction, while VC-weighted construction flattens the trade-off slope, reducing the diversity cost of quality.\", \"metrics\": {\"dataset\": \"SciERC\", \"configs\": {\"t07\": {\"one_minus_degen\": 0.777, \"uniform_delta\": 1.81, \"vc_delta\": 1.17, \"pareto\": \"uniform only\"}, \"t08\": {\"one_minus_degen\": 0.819, \"uniform_delta\": 1.25, \"vc_delta\": 1.68, \"pareto\": \"VC only\"}, \"mix_07_10\": {\"one_minus_degen\": 0.83, \"uniform_delta\": 1.43, \"vc_delta\": 1.67, \"pareto\": \"both\"}, \"t10\": {\"one_minus_degen\": 0.877, \"uniform_delta\": 0.75, \"vc_delta\": 1.21, \"pareto\": \"both (highest diversity)\"}, \"mix_08_10\": {\"one_minus_degen\": 0.789, \"uniform_delta\": -0.17, \"vc_delta\": 0.47, \"pareto\": \"dominated\"}}, \"vc_slope_reduction\": \"~50% flatter than uniform\", \"key_insight\": \"well-separated T mixing dual Pareto optimal; close T mixing dominated\"}, \"conclusion\": \"killed\", \"notes\": \"A4 Pareto diversity-quality analysis on SciERC. Mix T=0.7+T=1.0 is dual-Pareto optimal (uniform +1.43pp, VC +1.67pp). VC construction flattens trade-off slope ~50% vs uniform — increasing diversity costs less quality. Mix T=0.8+T=1.0 is dominated (close T → higher degeneracy, no construction gain). Confirms DGEC heterogeneous-T finding: ΔT matters, ΔT=0.3 beneficial, ΔT=0.2 harmful. Pareto plot artifact registered.\"}, \"exp_adaptive_sampling_budget\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T09:29:22.761Z\", \"updated_at\": \"2026-05-21T23:51:53.112Z\", \"hypothesis\": \"Confidence-aware adaptive sampling budget allocation (fewer samples for high-confidence instances, full N=8 for low-confidence) can recover nearly all SC F1 gains while saving 40-50% of inference cost, because high-confidence instances already have low diversity and gain nothing from additional samples.\", \"metrics\": {\"model\": \"Qwen3-8B FT\", \"fewnerd\": {\"n_instances\": 37648, \"greedy_f1\": 0.7884, \"uniform_n8_f1\": 0.7819, \"best_adaptive\": \"h1_l8\", \"best_adaptive_f1\": 0.7849, \"best_delta_vs_u8\": \"+0.30pp\", \"sample_savings\": \"43.8%\", \"note\": \"Greedy > U8; adaptive h1/l8 best: greedy for high-conf, N=8 SC for low-conf\"}, \"scierc\": {\"n_instances\": 551, \"greedy_f1\": 0.6592, \"uniform_n8_f1\": 0.6712, \"best_adaptive\": \"top67%_h2_l8\", \"best_adaptive_f1\": 0.6707, \"best_delta_vs_u8\": \"-0.05pp\", \"sample_savings\": \"50.2%\", \"note\": \"U8 > Greedy; top67% h2/l8 saves 50% with negligible loss\"}}, \"conclusion\": \"killed\", \"notes\": \"B7 adaptive sampling budget analysis on Qwen3-8B FT. Key findings: (1) FewNERD: greedy already beats uniform N=8 SC (+0.65pp), adaptive h1/l8 is optimal (+0.30pp vs U8, saves 43.8% samples); (2) SciERC: U8 beats greedy (+1.20pp), top67% h2/l8 saves 50% with only -0.05pp loss. Practical implication: confidence-gated sampling can halve inference cost. Artifacts: vc_8b_qwen3_ft_results, sj_8b_qwen3_ft_results (registered by worker).\"}, \"exp_dgec_heterogeneous_t\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T08:37:59.963Z\", \"updated_at\": \"2026-05-21T23:51:50.487Z\", \"hypothesis\": \"Mixing samples from T=0.7 and T=1.0 significantly reduces degeneracy compared to single-T sampling (by breaking temperature-induced mode collapse), enabling entity construction to achieve significant ΔF1 improvement even in configs where single-T construction was n.s. due to high degeneracy.\", \"metrics\": {\"dataset\": \"SciERC\", \"n_instances\": 529, \"t07_degen\": 0.2231, \"t10_degen\": 0.1235, \"mixed_degen\": 0.1701, \"mixed_uniform_f1\": 0.6584, \"mixed_vc_f1\": 0.6609, \"cross_pool_uniform_delta\": \"+0.006 (1/3 seeds sig)\", \"cross_pool_vc_delta\": \"+0.004 (1/3 seeds sig)\", \"t08_t10_result\": \"harmful (degen increased)\", \"conclusion_preliminary\": \"partially_supported\"}, \"notes\": \"Hypothesis partially supported. T=0.7+T=1.0 mixed pool reduces degen (22.3%→17.0%) and improves construction (VC 3/3 seeds sig vs greedy), but cross-pool comparison (mixed vs T=1.0 alone) only 1/3 seeds significant. T gap matters: ΔT=0.2 (T=0.8+T=1.0) harmful, ΔT=0.3 (T=0.7+T=1.0) beneficial. VC weighting confirmed cross-T compatible. Awaiting Director conclusion classification.\", \"conclusion\": \"killed\"}, \"exp_dgec_sj_construction\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T08:37:58.013Z\", \"updated_at\": \"2026-05-21T23:51:48.518Z\", \"hypothesis\": \"SJ-weighted entity construction serves as control for VC — if SJ (soft entity overlap) works as well as VC (exact match consensus), any stronger QE signal suffices for construction; if VC specifically outperforms SJ, exact-match consensus has a unique advantage over soft similarity for entity-level selection.\", \"metrics\": {\"total_configs\": 26, \"significant_positive\": 1, \"significant_negative\": 15, \"not_significant\": 10, \"best_config\": \"scierc/72b/zs +2.0pp p=0.001\", \"worst_config\": \"fewnerd/8b_qwen3/ft mean -1.48pp all seeds p=1.0\", \"qwen3_8b_ft_supplement\": {\"configs\": 9, \"sig+\": 0, \"sig-\": 6, \"ns\": 3, \"fewnerd_mean_delta\": -1.48, \"scierc_mean_delta\": -0.4, \"conll_mean_delta\": -0.5, \"note\": \"SJ fully negative on Qwen3-8B FT — consistent with Qwen2.5-7B FT pattern\"}, \"m030_all_passed\": true}, \"notes\": \"COMPLETE (26 configs). SJ-weighted construction: 1 sig+ / 15 sig- / 10 ns. Qwen3-8B FT supplement (9 configs): 0+/6-/3ns — fully negative, consistent with 7B FT pattern. FewNERD -1.48pp mean (all seeds p=1.0). Definitively answers control question: NOT any stronger QE signal works for construction. SJ introduces noise at entity level. Only exception: SciERC 72B ZS (lowest precision, lowest degeneracy). Closed per D170/D171.\", \"conclusion\": \"killed\"}, \"exp_dgec_vc_construction\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-20T08:37:55.968Z\", \"updated_at\": \"2026-05-21T23:51:46.733Z\", \"hypothesis\": \"VC-weighted entity construction outperforms greedy and LP-weighted construction across configs because Vote Count is a more direct quality estimator for structured outputs — it measures exact-match consensus without relying on model-internal log probabilities. Especially effective in high-degeneracy regimes where LP compression makes LP-weighting uninformative.\", \"metrics\": {\"total_configs\": 28, \"significant_positive\": 9, \"significant_negative\": 10, \"not_significant\": 9, \"by_dataset\": {\"fewnerd\": {\"configs\": 11, \"sig+\": 5, \"sig-\": 5, \"ns\": 1, \"mean_delta_pp\": -0.12}, \"wnut17\": {\"configs\": 3, \"sig+\": 2, \"sig-\": 0, \"ns\": 1, \"mean_delta_pp\": 0.92}, \"scierc\": {\"configs\": 7, \"sig+\": 2, \"sig-\": 0, \"ns\": 5, \"mean_delta_pp\": 0.62}, \"conll\": {\"configs\": 7, \"sig+\": 0, \"sig-\": 5, \"ns\": 2, \"mean_delta_pp\": -0.33}}, \"qwen3_8b_ft_supplement\": {\"configs\": 9, \"sig+\": 3, \"sig-\": 3, \"ns\": 3, \"best\": \"SciERC s42 +1.40pp p=0.017\", \"worst\": \"CoNLL s456 -0.54pp p=0.998\", \"note\": \"VC inconsistent on LP-success configs; seed-dependent on FewNERD; CoNLL all negative due to high degeneracy\"}, \"m030_all_passed\": true}, \"notes\": \"COMPLETE (28 configs). VC-weighted construction: 9 sig+ / 10 sig- / 9 ns. Qwen3-8B FT supplement (9 configs): 3+/3-/3ns — VC inconsistent even on LP-success configs. SciERC s42 best (+1.40pp) but cross-seed unstable. CoNLL all negative (high degeneracy). WNUT17/SciERC lean positive but not robust. Key answer: VC does NOT reliably improve where LP already works — seed-dependent, dataset-dependent. DGEC unified method goal (70-80% configs) unreachable at 32% (9/28). Closed per D170/D171.\", \"conclusion\": \"killed\"}, \"exp_fewnerd_mf4v2_s42_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T14:24:25.067Z\", \"updated_at\": \"2026-05-21T23:30:31.694Z\", \"hypothesis\": \"FewNERD MF4v2 s42 re-run v3: corrected model path with nested tokenizer dir. N=8, T=1.0, seed=42.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=0 python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-fewnerd-exp021-merged --data_dir data/fewnerd/ --dataset fewnerd --subtask ner --n_samples 8 --temperature 1.0 --seed 42 --collect_logprobs --output_dir output/fewnerd_mf4v2_seed42_v3/\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"76584\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_fewnerd_mf4v2_s42_v3.log\", \"submitted_at\": \"2026-05-21T21:18:47.546Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T20:57:24.551Z\", \"metrics\": {\"greedy_f1\": 0.7911, \"mv_f1_strict\": 0.7586, \"mv_delta_pp\": -3.25, \"keyset_degeneracy\": 0.091, \"alpha_crit_eff_strict\": 0.4352, \"mv_f1_inclusive\": 0.7783, \"oracle_f1\": 0.8803}}, \"exp_e2_pretrained_fewnerd_s42_v2\": {\"status\": \"PREPARING\", \"retry_count\": 0, \"created_at\": \"2026-05-21T22:45:28.213Z\", \"updated_at\": \"2026-05-21T23:23:03.637Z\", \"conclusion\": \"failed\", \"reproduce\": {\"finished_at\": \"2026-05-21T23:20:13.201Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-21T23:20:18.666773+00:00\"}]}, \"notes\": \"失败原因: process dead 5× with no sentinel/W&B — auto-resolved as failed | 诊断中: Worker worker_diagnose_exp_e2_pretrained_fewnerd_s42_v2 | 注意: 原始实验 exp_e2_pretrained_fewnerd (seed=42) 已成功完成，3-seed set 完整，此 v2 可能不需要重跑\"}, \"exp_fewnerd_mf4v2_s456_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T19:43:45.275Z\", \"updated_at\": \"2026-05-21T21:53:49.363Z\", \"hypothesis\": \"FewNERD MF4v2 s456 re-run v3: regenerate finetuned FewNERD seed=456 data on current server for provenance verification. N=8, T=1.0, seed=456. Original data lost with 5090-b.\", \"spec\": {\"checkpoint_path\": \"output/fewnerd_mf4v2_seed456_v3/samples.jsonl\", \"log_path\": \"output/fewnerd_mf4v2_seed456_v3/\"}, \"metrics\": {\"greedy_f1\": 0.791, \"mv_strict_f1\": 0.7686, \"mv_delta_strict_pp\": -2.24, \"mv_incl_f1\": 0.7857, \"mv_delta_incl_pp\": -0.52, \"degeneracy_rate\": 0.081, \"alpha_crit_eff_strict\": 0.6793, \"n_instances\": 32565}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T21:53:49.363Z\"}, \"exp_fewnerd_mf4v2_s123_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T14:24:26.314Z\", \"updated_at\": \"2026-05-21T21:53:33.144Z\", \"hypothesis\": \"FewNERD MF4v2 s123 re-run v3: corrected model path with nested tokenizer dir. N=8, T=1.0, seed=123.\", \"spec\": {\"data_path\": \"data/fewnerd/\", \"data_count\": 37648, \"model_name\": \"qwen3-8b-fewnerd-exp021-merged\", \"seed\": 123, \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-fewnerd-exp021-merged --data_dir data/fewnerd/ --dataset fewnerd --subtask ner --n_samples 8 --temperature 1.0 --seed 123 --collect_logprobs --output_dir output/fewnerd_mf4v2_seed123_v3/\\\"\", \"server\": \"autodl-5090-c\", \"gpu\": [\"cuda:1\"], \"pid\": \"357390\", \"backend\": \"tmux\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T20:57:21.416Z\", \"metrics\": {\"greedy_f1\": 0.7911, \"mv_strict_f1\": 0.7648, \"mv_delta_strict_pp\": -2.63, \"mv_incl_f1\": 0.7844, \"mv_delta_incl_pp\": -0.67, \"degeneracy_rate\": 0.093, \"alpha_crit_eff_strict\": 0.6825, \"n_instances\": 32565}}, \"exp_fewnerd_5epoch_s456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T18:53:46.586Z\", \"updated_at\": \"2026-05-21T21:41:55.856Z\", \"hypothesis\": \"FewNERD 5-epoch epoch confound check seed=456: third seed for 5-epoch fine-tuned Qwen3-8B (LoRA r=32 alpha=64) on FewNERD NER, N=8, T=1.0. Completes 3-seed set for epoch confound analysis. If degeneracy/MV pattern consistent across seeds, epoch count is not the confound.\", \"spec\": {\"checkpoint_path\": \"N/A (inference only)\", \"log_path\": \"/tmp/inference_s456.log\"}, \"metrics\": {\"greedy_f1\": 0.7978, \"mv_strict_f1\": 0.795, \"mv_delta_strict_pp\": -0.28, \"degeneracy_rate\": 0.259, \"alpha_crit_eff_strict\": 0.8903, \"oracle_f1\": 0.8793}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T21:40:51.694Z\"}, \"exp_e2_pretrained_fewnerd_s456\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-21T14:22:41.214Z\", \"updated_at\": \"2026-05-21T21:19:16.075Z\", \"hypothesis\": \"E2 pre-trained baseline FewNERD seed=456: third seed for pretrained Qwen2.5-7B-Instruct on FewNERD SC pipeline. Completes 3-seed set for statistical power on whether correlation-selection gap is model-intrinsic.\", \"reproduce\": {\"finished_at\": \"2026-05-21T19:11:45.977Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"completed_at\": \"2026-05-21T19:11:49.650Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-21T19:12:00.220032+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"spec\": {\"command\": \"python -u code/run_mvp_pilot.py --model_path Qwen2.5-7B-Instruct --dataset fewnerd --subtask ner --n_samples 8 --temperature 1.0 --seed 456 --collect_logprobs --output_dir output/e2_pretrained_fewnerd_s456/\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:3\"], \"pid\": \"47635\", \"data_path\": \"data/fewnerd/processed_data/\", \"data_count\": 37648, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": 456, \"backend\": \"tmux\", \"note\": \"95% at 18:58 UTC. Cron monitors wrong server (5090-c dup was killed). Real process on 5090 cuda:3.\", \"checkpoint_path\": \"output/e2_pretrained_fewnerd_s456/samples.jsonl\", \"log_path\": \"output/e2_pretrained_fewnerd_s456/\"}, \"metrics\": {\"greedy_f1\": 0.5373, \"mv_strict_f1\": 0.5738, \"mv_incl_f1\": 0.5611, \"oracle_f1\": 0.646, \"mv_delta_strict_pp\": 3.65, \"degeneracy_rate\": 0.118, \"alpha_crit_eff_strict\": 0.3047, \"capture_rate\": 0.336, \"n_instances\": 32565}, \"conclusion\": \"success\"}, \"exp_fewnerd_5epoch_s123\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-21T17:59:17.622Z\", \"updated_at\": \"2026-05-21T21:00:07.448Z\", \"hypothesis\": \"FewNERD 5-epoch epoch confound check seed=123: second seed for 5-epoch inference on FewNERD NER, N=8, T=1.0. Cross-validates whether epoch confound effects are consistent across seeds.\", \"reproduce\": {\"finished_at\": \"2026-05-21T18:19:12.144Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"completed_at\": \"2026-05-21T18:19:16.029Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-21T18:19:31.337921+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"spec\": {\"command\": \"python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-fewnerd-5epoch-merged --data_dir data/fewnerd/processed_data/ --dataset fewnerd --subtask ner --n_samples 8 --temperature 1.0 --seed 123 --collect_logprobs --output_dir output/fewnerd_5epoch_s123/\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"63337\", \"data_path\": \"data/fewnerd/processed_data/\", \"data_count\": 37648, \"model_name\": \"qwen3-8b-fewnerd-5epoch-merged\", \"seed\": 123, \"backend\": \"tmux\"}, \"conclusion\": \"success\", \"metrics\": {\"greedy_f1\": 0.7976, \"mv_strict_f1\": 0.7941, \"mv_delta_strict_pp\": -0.35, \"degeneracy_rate\": 0.271, \"alpha_crit_eff_strict\": 0.5468, \"oracle_f1\": 0.8814}}, \"exp_fewnerd_5epoch_s42\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-21T17:59:15.452Z\", \"updated_at\": \"2026-05-21T21:00:02.417Z\", \"hypothesis\": \"FewNERD 5-epoch epoch confound check seed=42: inference with 5-epoch fine-tuned Qwen3-8B (LoRA r=32 alpha=64) on FewNERD NER, N=8, T=1.0. Tests whether 3→5 epoch change affects degeneracy, MV performance, and signal correlations. If degeneracy increases or MV still fails, epoch count is not the confound.\", \"reproduce\": {\"finished_at\": \"2026-05-21T18:18:53.283Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"completed_at\": \"2026-05-21T18:18:57.451Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-21T18:19:08.740981+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"spec\": {\"command\": \"python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-fewnerd-5epoch-merged --data_dir data/fewnerd/processed_data/ --dataset fewnerd --subtask ner --n_samples 8 --temperature 1.0 --seed 42 --collect_logprobs --output_dir output/fewnerd_5epoch_s42/\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:1\"], \"pid\": \"63198\", \"data_path\": \"data/fewnerd/processed_data/\", \"data_count\": 37648, \"model_name\": \"qwen3-8b-fewnerd-5epoch-merged\", \"seed\": 42, \"backend\": \"tmux\"}, \"conclusion\": \"success\", \"metrics\": {\"greedy_f1\": 0.798, \"mv_strict_f1\": 0.7935, \"mv_delta_strict_pp\": -0.45, \"degeneracy_rate\": 0.257, \"alpha_crit_eff_strict\": 0.5369, \"oracle_f1\": 0.8781}}, \"exp_e2_pretrained_scierc_s456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T14:20:30.755Z\", \"updated_at\": \"2026-05-21T20:32:23.158Z\", \"hypothesis\": \"E2 pre-trained baseline SciERC seed=456: Qwen2.5-7B-Instruct (unfinetuned) on SciERC SC pipeline N=8 T=1.0. Third seed for E2 pre-trained baseline statistical power on SciERC.\", \"spec\": {\"command\": \"python -u code/run_mvp_pilot.py --model_path /root/autodl-tmp/.hf_cache/Qwen2.5-7B-Instruct --data_dir data/scierc/processed_data/ --dataset scierc --subtask ner --n_samples 8 --temperature 1.0 --seed 456 --collect_logprobs --output_dir output/e2_pretrained_scierc_s456/\", \"server\": \"autodl-5090-c\", \"gpu\": [\"cuda:2\"], \"pid\": \"326645\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_e2_pretrained_scierc_s456.log\", \"submitted_at\": \"2026-05-21T14:20:56.182Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scierc/processed_data/\", \"data_count\": 551, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": 456, \"checkpoint_path\": \"N/A (inference-only)\", \"wall_clock_seconds\": 1140.9, \"gpu_hours\": 0.32}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-21T14:39:57.115Z\", \"metrics\": {\"greedy_f1\": 0.2436, \"mv_strict_f1\": 0.2642, \"oracle_f1\": 0.3952, \"mv_delta_strict_pp\": 2.06, \"degeneracy_rate\": 0.009, \"alpha_crit_eff_strict\": 0.1537, \"n_instances\": 529}}, \"exp_e2_pretrained_scierc_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T14:20:29.367Z\", \"updated_at\": \"2026-05-21T20:32:21.772Z\", \"hypothesis\": \"E2 pre-trained baseline SciERC seed=123: Qwen2.5-7B-Instruct (unfinetuned) on SciERC SC pipeline N=8 T=1.0. Additional seed for E2 pre-trained baseline. Tests whether correlation-selection gap and structural vs surface patterns are consistent across seeds on SciERC.\", \"spec\": {\"command\": \"python -u code/run_mvp_pilot.py --model_path /root/autodl-tmp/.hf_cache/Qwen2.5-7B-Instruct --data_dir data/scierc/processed_data/ --dataset scierc --subtask ner --n_samples 8 --temperature 1.0 --seed 123 --collect_logprobs --output_dir output/e2_pretrained_scierc_s123/\", \"server\": \"autodl-5090-c\", \"gpu\": [\"cuda:1\"], \"pid\": \"326377\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_e2_pretrained_scierc_s123.log\", \"submitted_at\": \"2026-05-21T14:20:52.083Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scierc/processed_data/\", \"data_count\": 551, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": 123, \"checkpoint_path\": \"N/A (inference-only)\", \"wall_clock_seconds\": 1141.9, \"gpu_hours\": 0.32}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-21T14:39:53.937Z\", \"metrics\": {\"greedy_f1\": 0.2436, \"mv_strict_f1\": 0.2548, \"oracle_f1\": 0.3941, \"mv_delta_strict_pp\": 1.12, \"degeneracy_rate\": 0.006, \"alpha_crit_eff_strict\": 0.1468, \"n_instances\": 529}}, \"exp_fewnerd_n16_s123\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-21T04:30:47.609Z\", \"updated_at\": \"2026-05-21T20:31:42.072Z\", \"hypothesis\": \"FewNERD N=16 seed=123: second seed for N=16 scaling analysis. Tests whether doubling samples from N=8 to N=16 increases oracle headroom consistently across seeds, and whether MV aggregation gap widens or narrows.\", \"server\": \"autodl-5090-b\", \"gpu\": \"cuda:3\", \"completed_at\": \"2026-05-21T08:33:10.578Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"greedy_f1\": 0.7888, \"oracle_f1\": 0.9147, \"oracle_headroom\": 0.126, \"rho_fk_full\": 0.224, \"rho_sj_full\": 0.352, \"rho_fk_cond\": 0.083, \"rho_sj_cond\": 0.282, \"logprob_rho_full\": 0.28, \"logprob_rho_cond\": 0.258, \"instances\": 37648}}, \"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-21T15:14:54.091154+00:00\"}]}, \"spec\": {\"command\": \"python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-fewnerd-exp021-merged --data_dir data/fewnerd/ --dataset fewnerd --subtask ner --n_samples 16 --temperature 1.0 --seed 123 --collect_logprobs --output_dir output/fewnerd_n16_s123/\", \"server\": \"autodl-5090-c\", \"gpu\": [\"cuda:0\"], \"pid\": \"311981\", \"log_path\": \"output/fewnerd_n16_s123/\", \"submitted_at\": \"2026-05-21T11:23:58.304Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/fewnerd/\", \"data_count\": 37648, \"model_name\": \"qwen3-8b-fewnerd-exp021-merged\", \"seed\": 123, \"checkpoint_path\": \"output/fewnerd_n16_s123/samples.jsonl\", \"wall_clock_seconds\": 32863.8, \"gpu_hours\": 9.13}, \"reproduce\": {\"finished_at\": \"2026-05-21T15:14:44.426Z\"}, \"metrics\": {\"greedy_f1\": 0.7916, \"oracle_f1\": 0.915, \"mv_strict_f1\": 0.7798, \"mv_delta\": -0.0118, \"degeneracy_rate\": 0.048, \"alpha_crit_eff_strict\": 0.6715, \"capture_rate\": -0.095, \"n_instances\": 32565, \"oracle_headroom\": 0.1234}, \"conclusion\": \"success\"}, \"exp_fewnerd_n16_s42_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T11:21:49.005Z\", \"updated_at\": \"2026-05-21T20:30:10.353Z\", \"hypothesis\": \"FewNERD N=16 scaling: doubling sample count from N=8 to N=16 increases oracle headroom and tests whether additional samples improve MV aggregation or only expand the correlation-selection gap.\", \"spec\": {\"command\": \"python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-fewnerd-exp021-merged --data_dir data/fewnerd/ --dataset fewnerd --subtask ner --n_samples 16 --temperature 1.0 --seed 42 --collect_logprobs --output_dir output/fewnerd_n16_s42/\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"32117\", \"data_path\": \"data/fewnerd/\", \"data_count\": 37648, \"model_name\": \"qwen3-8b-fewnerd-exp021-merged\", \"seed\": 42}, \"conclusion\": \"success\", \"metrics\": {\"greedy_f1\": 0.7911, \"oracle_f1\": 0.9077, \"mv_strict_f1\": 0.7677, \"mv_delta\": -0.0234, \"degeneracy_rate\": 0.024, \"alpha_crit_eff_strict\": 0.4053, \"capture_rate\": -0.201, \"n_instances\": 32565, \"oracle_headroom\": 0.1166}, \"log_path\": \"output/fewnerd_n16_s42/\", \"checkpoint_path\": \"output/fewnerd_n16_s42/samples.jsonl\", \"completed_at\": \"2026-05-21T15:18:27.008Z\"}, \"exp_fewnerd_n16_s456_v2\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-21T07:18:11.587Z\", \"updated_at\": \"2026-05-21T20:30:07.774Z\", \"hypothesis\": \"FewNERD N=16 (seed=456, v2 rerun): data lost in previous run. Extending N-scaling curve to N=16 for Qwen3-8B-FT, critical for F1(N)=a-b*N^(-c) scaling law. Third seed for 3-seed statistical power.\", \"completed_at\": \"2026-05-21T11:30:16.054Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"greedy_f1\": 0.7883, \"oracle_f1\": 0.9058, \"oracle_headroom\": 0.1175, \"fleiss_kappa\": 0.4552, \"rho_sj_full\": 0.285, \"rho_fk_full\": 0.233, \"samples_count\": 37648, \"mv_f1\": \"NOT_COMPUTED\", \"degeneracy_rate\": \"NOT_COMPUTED\", \"note\": \"report.json lacks mv_f1 and degeneracy; need post-processing from samples.jsonl\"}}}, \"spec\": {\"command\": \"python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-fewnerd-exp021-merged --data_dir data/fewnerd/ --dataset fewnerd --subtask ner --n_samples 16 --temperature 1.0 --seed 456 --collect_logprobs --output_dir output/fewnerd_n16_s456/\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"54277\", \"data_path\": \"data/fewnerd/\", \"data_count\": 37648, \"model_name\": \"qwen3-8b-fewnerd-exp021-merged\", \"seed\": 456, \"backend\": \"tmux\", \"note\": \"81% complete at 18:20 UTC, ETA ~19:05\", \"checkpoint_path\": \"output/fewnerd_n16_s456/samples.jsonl\", \"log_path\": \"output/fewnerd_n16_s456/report.json\"}, \"metrics\": {\"greedy_f1\": 0.791, \"oracle_f1\": 0.9105, \"mv_strict_f1\": 0.7767, \"mv_delta\": -0.0143, \"degeneracy_rate\": 0.048, \"alpha_crit_eff_strict\": 0.4154, \"capture_rate\": -0.12, \"n_instances\": 32565, \"oracle_headroom\": 0.1195}, \"conclusion\": \"success\"}, \"exp_e2_pretrained_fewnerd\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T05:52:06.559Z\", \"updated_at\": \"2026-05-21T18:52:54.658Z\", \"hypothesis\": \"The correlation-selection gap (oracle F1 >> MV F1 despite positive agreement-correctness correlation) is model-intrinsic and exists even in pretrained (non-finetuned) Qwen2.5-7B-Instruct, not a fine-tuning artifact\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && python -u code/run_mvp_pilot.py --model_path /root/autodl-tmp/models/Qwen2.5-7B-Instruct/Qwen/Qwen2___5-7B-Instruct --data_dir data/fewnerd/ --dataset fewnerd --subtask ner --n_samples 8 --temperature 1.0 --seed 42 --collect_logprobs --output_dir output/e2_pretrained_fewnerd/\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:3\"], \"pid\": \"8406\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_e2_pretrained_fewnerd.log\", \"submitted_at\": \"2026-05-21T06:59:29.791Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/fewnerd/\", \"data_count\": 37648, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": 42, \"checkpoint_source\": \"pretrained_base\", \"eval_data\": \"fewnerd\", \"checkpoint_path\": \"/root/autodl-tmp/models/Qwen2.5-7B-Instruct/Qwen/Qwen2___5-7B-Instruct\", \"wall_clock_seconds\": 20329.2, \"gpu_hours\": 5.65}, \"reproduce\": {\"finished_at\": \"2026-05-21T12:34:32.119Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-21T12:34:40.438881+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"greedy_f1\": 0.5384, \"oracle_f1\": 0.6508, \"headroom\": 0.1124, \"fleiss_kappa_mean\": 0.4501, \"soft_jaccard_mean\": 0.6881, \"structural_beats_surface\": true, \"rho_advantage\": 0.0501, \"mv_strict_f1\": 0.5788, \"mv_incl_f1\": 0.5667, \"mv_delta_strict_pp\": 4.03, \"degeneracy_rate\": 0.122, \"alpha_crit_eff_strict\": 0.3065, \"mv_capture_rate\": 0.359, \"gold_nonempty\": 32565, \"n_instances\": 37648, \"note\": \"greedy/mv/oracle computed on gold-nonempty (32565); report.json values (0.5121 etc.) include 5083 gold-empty instances\"}, \"completed_at\": \"2026-05-21T12:38:18.972Z\"}, \"exp_e2_pretrained_fewnerd_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T10:17:12.679Z\", \"updated_at\": \"2026-05-21T18:31:40.126Z\", \"hypothesis\": \"E2 pre-trained baseline seed 123: Qwen2.5-7B-Instruct (unfinetuned) on FewNERD SC pipeline N=8 T=1.0. Additional seed for E2 pre-trained baseline statistical power. If correlation-selection gap persists without fine-tuning → phenomenon is model-intrinsic.\", \"parent\": \"exp_e2_pretrained_fewnerd\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u code/run_mvp_pilot.py --model_path /root/autodl-tmp/.hf_cache/Qwen2.5-7B-Instruct --data_dir data/fewnerd/ --dataset fewnerd --subtask ner --n_samples 8 --temperature 1.0 --seed 123 --collect_logprobs --output_dir output/e2_pretrained_fewnerd_s123/\", \"server\": \"autodl-5090-c\", \"data_path\": \"data/fewnerd/\", \"data_count\": 4706, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": 123, \"checkpoint_source\": \"/root/autodl-tmp/.hf_cache/Qwen2.5-7B-Instruct\", \"eval_data\": \"data/fewnerd/\", \"checkpoint_path\": \"output/e2_pretrained_fewnerd_s123/\", \"log_path\": \"output/e2_pretrained_fewnerd_s123/report.json\"}, \"conclusion\": \"success\", \"metrics\": {\"greedy_f1\": 0.5381, \"oracle_f1\": 0.652, \"headroom\": 0.1139, \"fleiss_kappa\": 0.443, \"soft_jaccard\": 0.687, \"structural_beats_surface\": true, \"rho_advantage\": 0.047, \"mv_strict_f1\": 0.5783, \"mv_incl_f1\": 0.5658, \"mv_delta_strict_pp\": 4.02, \"degeneracy_rate\": 0.112, \"alpha_crit_eff_strict\": 0.458, \"alpha_crit_eff_incl\": 0.4442, \"mv_capture_rate\": 0.353, \"gold_nonempty\": 32565}, \"completed_at\": \"2026-05-21T18:25:03.839Z\"}, \"exp_scierc_n16_s456\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-21T04:30:43.414Z\", \"updated_at\": \"2026-05-21T17:54:50.480Z\", \"hypothesis\": \"SciERC N=16 seed=456: third seed for N=16 scaling analysis on SciERC. Tests oracle headroom increase and MV gap consistency with seeds 42 and 123.\", \"completed_at\": \"2026-05-21T04:44:33.829Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\"}}, \"parent\": \"exp_scierc_n16_s42\", \"spec\": {\"command\": \"python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data/ --dataset scierc --subtask ner --n_samples 16 --temperature 1.0 --seed 456 --collect_logprobs --output_dir output/scierc_n16_s456/\", \"server\": \"autodl-5090-c\", \"gpu\": [\"cuda:2\"], \"data_path\": \"data/scierc/processed_data/\", \"data_count\": 551, \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 456, \"checkpoint_source\": \"checkpoints/qwen3-8b-scierc-merged-v2\", \"eval_data\": \"data/scierc/processed_data/\", \"conclusion\": \"success\", \"checkpoint_path\": \"output/scierc_n16_s456/\", \"log_path\": \"output/scierc_n16_s456/\"}, \"conclusion\": \"success\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_scierc_n16_s456.log\", \"checkpoint_path\": \"output/scierc_n16_s456/\", \"metrics\": {\"greedy_f1\": 0.6641, \"oracle_f1\": 0.8076, \"mv_f1\": 0.6643, \"degeneracy\": 0.07, \"n_instances\": 529}}, \"exp_e2_pretrained_conll_s123_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T17:50:04.670Z\", \"updated_at\": \"2026-05-21T17:54:48.608Z\", \"hypothesis\": \"E2 pretrained baseline CoNLL s123 v2: Qwen2.5-7B-Instruct (unfinetuned) on CoNLL SC pipeline N=8 T=1.0 seed=123. Cross-validation of E2 pretrained CoNLL performance.\", \"spec\": {\"command\": \"python code/run_mvp_pilot.py --model_path Qwen2.5-7B-Instruct --dataset conll --n_samples 8 --temperature 1.0 --seed 123\", \"server\": \"autodl-5090-c\", \"data_path\": \"data/conll/\", \"data_count\": 3453, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": 123, \"checkpoint_path\": \"output/e2_pretrained_conll_s123_v2/\", \"log_path\": \"output/e2_pretrained_conll_s123_v2/\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T17:52:03.024Z\", \"metrics\": {\"greedy_f1\": 0.5364, \"oracle_f1\": 0.6257, \"mv_f1\": 0.6321, \"degeneracy\": 0.365, \"n_instances\": 2756}}, \"exp_e2_pretrained_scierc_s42_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T17:50:07.046Z\", \"updated_at\": \"2026-05-21T17:52:34.495Z\", \"hypothesis\": \"E2 pretrained baseline SciERC s42 v2: Qwen2.5-7B-Instruct (unfinetuned) on SciERC SC pipeline N=8 T=1.0. Re-run for cross-validation of E2 pretrained SciERC performance.\", \"spec\": {\"command\": \"python code/run_mvp_pilot.py --model_path Qwen2.5-7B-Instruct --dataset scierc --n_samples 8 --temperature 1.0 --seed 42\", \"server\": \"autodl-5090-c\", \"data_path\": \"data/scierc/\", \"data_count\": 551, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": 42, \"checkpoint_path\": \"output/e2_pretrained_scierc_s42_v2/\", \"log_path\": \"output/e2_pretrained_scierc_s42_v2/\"}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-21T17:52:06.047Z\", \"metrics\": {\"greedy_f1\": 0.2434, \"oracle_f1\": 0.3888, \"mv_f1\": 0.2618, \"degeneracy\": 0.009, \"n_instances\": 529}}, \"exp_e2_pretrained_conll_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T17:49:45.870Z\", \"updated_at\": \"2026-05-21T17:51:59.601Z\", \"metrics\": {\"greedy_f1\": 0.5363, \"oracle_f1\": 0.6299, \"mv_f1\": 0.6284, \"degeneracy\": 0.359, \"n_instances\": 2756}, \"hypothesis\": \"E2 pretrained baseline CoNLL s42: Qwen2.5-7B-Instruct (unfinetuned) on CoNLL SC pipeline N=8 T=1.0. Tests whether correlation-selection gap is model-intrinsic or fine-tuning artifact.\", \"spec\": {\"command\": \"python code/run_mvp_pilot.py --model_path Qwen2.5-7B-Instruct --dataset conll --n_samples 8 --temperature 1.0 --seed 42\", \"server\": \"autodl-5090-c\", \"data_path\": \"data/conll/\", \"data_count\": 3453, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": 42, \"checkpoint_path\": \"output/e2_pretrained_conll_s42/\", \"log_path\": \"output/e2_pretrained_conll_s42/\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T17:51:59.601Z\"}, \"exp_conll_n16_s456\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-21T04:30:49.693Z\", \"updated_at\": \"2026-05-21T14:23:17.686Z\", \"hypothesis\": \"CoNLL N=16 seed=456: third seed completing 3-seed N=16 set. Tests N-scaling consistency for CoNLL — whether oracle headroom increase from N=8→N=16 is reproducible and degeneracy pattern changes.\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:1\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie/ && python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-conll2003-merged --data_dir data/conll2003/ --dataset conll2003 --n_samples 16 --temperature 1.0 --seed 456 --collect_logprobs --output_dir output/conll_n16_s456/\\\"\", \"finished_at\": \"2026-05-21T04:51:43.069Z\"}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"completed_at\": \"2026-05-21T04:51:46.724Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-21T04:51:52.994852+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"失败原因: tokenizer vocab_file=None — checkpoints/qwen3-8b-conll2003-merged 缺少 vocab.json，vLLM 初始化 tokenizer 时 TypeError。与 exp_conll_n16_s123 同根因。| 已有成果: 无（启动即崩溃）| 建议: 修复 merged checkpoint tokenizer 文件后重跑\"}}, \"notes\": \"失败原因: tokenizer vocab_file=None — checkpoints/qwen3-8b-conll2003-merged 缺少 vocab.json，vLLM 初始化 tokenizer 时 TypeError。与 exp_conll_n16_s123 同根因。| 已有成果: 无（启动即崩溃）| 建议: 修复 merged checkpoint tokenizer 文件后重跑\", \"parent\": \"exp_conll_n16_s42\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-conll2003-merged --data_dir data/conll2003/ --dataset conll2003 --subtask ner --n_samples 16 --temperature 1.0 --seed 456 --collect_logprobs --output_dir output/conll_n16_s456/\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:1\"], \"pid\": \"41031\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_conll_n16_s456.log\", \"submitted_at\": \"2026-05-21T12:54:30.425Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 5327.3, \"gpu_hours\": 1.48}, \"conclusion\": \"success\", \"metrics\": {\"greedy_f1\": 0.9072, \"oracle_f1\": 0.9545, \"oracle_headroom\": 0.0473, \"rho_fk_cond\": 0.428, \"rho_sj_cond\": 0.451, \"logprob_rho_cond\": 0.374, \"structural_beats_surface\": true, \"verdict\": \"PASS\"}, \"checkpoint_path\": \"output/conll_n16_s456/\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_conll_n16_s456.log\"}, \"exp_conll_mf4v2_s456_rerun\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T13:02:32.260Z\", \"updated_at\": \"2026-05-21T14:21:47.751Z\", \"hypothesis\": \"CoNLL MF4v2 seed=456 rerun: regenerating instance-level samples.jsonl for MV unified recompute. Original data may have been lost with 5090-b.\", \"spec\": {\"command\": \"python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-conll2003-merged --data_dir data/conll2003/ --dataset conll2003 --subtask ner --n_samples 8 --temperature 1.0 --seed 456 --collect_logprobs --output_dir output/conll_mf4v2_seed456/\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:3\"], \"pid\": \"42447\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_conll_mf4v2_s456_rerun.log\", \"submitted_at\": \"2026-05-21T13:03:07.545Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/conll2003/\", \"data_count\": 3453, \"model_name\": \"qwen3-8b-conll2003-merged\", \"seed\": 456, \"wall_clock_seconds\": 4720.2, \"gpu_hours\": 1.31}, \"conclusion\": \"success\", \"metrics\": {\"greedy_f1\": 0.9068, \"oracle_f1\": 0.9429, \"oracle_headroom\": 0.0361, \"rho_fk_cond\": 0.426, \"rho_sj_cond\": 0.454, \"logprob_rho_cond\": 0.37, \"structural_beats_surface\": true, \"verdict\": \"PASS\", \"mv_strict_f1\": 0.9121, \"mv_incl_f1\": 0.9133, \"degeneracy_rate\": 0.604, \"alpha_crit_v4\": 0.4558}, \"checkpoint_path\": \"output/conll_mf4v2_seed456/\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_conll_mf4v2_s456_rerun.log\", \"completed_at\": \"2026-05-21T14:21:47.751Z\"}, \"exp_conll_mf4v2_s123_rerun\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T13:02:30.304Z\", \"updated_at\": \"2026-05-21T14:21:44.758Z\", \"hypothesis\": \"CoNLL MF4v2 seed=123 rerun: regenerating instance-level samples.jsonl for MV unified recompute (strict > threshold + 4-tuple match). Original data may have been lost with 5090-b.\", \"spec\": {\"command\": \"python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-conll2003-merged --data_dir data/conll2003/ --dataset conll2003 --subtask ner --n_samples 8 --temperature 1.0 --seed 123 --collect_logprobs --output_dir output/conll_mf4v2_seed123/\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"42178\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_conll_mf4v2_s123_rerun.log\", \"submitted_at\": \"2026-05-21T13:03:04.256Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/conll2003/\", \"data_count\": 3453, \"model_name\": \"qwen3-8b-conll2003-merged\", \"seed\": 123, \"wall_clock_seconds\": 4720.5, \"gpu_hours\": 1.31}, \"conclusion\": \"success\", \"metrics\": {\"greedy_f1\": 0.9072, \"oracle_f1\": 0.9526, \"oracle_headroom\": 0.0454, \"rho_fk_cond\": 0.389, \"rho_sj_cond\": 0.414, \"logprob_rho_cond\": 0.367, \"structural_beats_surface\": true, \"verdict\": \"PASS\", \"mv_strict_f1\": 0.9123, \"mv_incl_f1\": 0.9151, \"degeneracy_rate\": 0.603, \"alpha_crit_v4\": 0.456}, \"checkpoint_path\": \"output/conll_mf4v2_seed123/\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_conll_mf4v2_s123_rerun.log\", \"completed_at\": \"2026-05-21T14:21:44.759Z\"}, \"exp_fewnerd_mf4v2_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T07:55:59.499Z\", \"updated_at\": \"2026-05-21T14:21:31.746Z\", \"spec\": {\"command\": \"python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-fewnerd-exp021-merged --data_dir data/fewnerd/ --dataset fewnerd --subtask ner --n_samples 8 --temperature 1.0 --seed 123 --collect_logprobs --output_dir output/fewnerd_mf4v2_seed123/\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"13035\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_fewnerd_mf4v2_s123.log\", \"submitted_at\": \"2026-05-21T07:56:58.909Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/fewnerd/\", \"data_count\": 37648, \"model_name\": \"qwen3-8b-fewnerd-exp021-merged\", \"seed\": 123, \"wall_clock_seconds\": 23072.8, \"gpu_hours\": 6.41}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-21T14:21:31.746Z\"}, \"exp_fewnerd_mf4v2_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T07:56:02.381Z\", \"updated_at\": \"2026-05-21T14:21:28.624Z\", \"spec\": {\"command\": \"python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-fewnerd-exp021-merged --data_dir data/fewnerd/ --dataset fewnerd --subtask ner --n_samples 8 --temperature 1.0 --seed 42 --collect_logprobs --output_dir output/fewnerd_mf4v2_seed42/\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:1\"], \"pid\": \"13177\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_fewnerd_mf4v2_s42.log\", \"submitted_at\": \"2026-05-21T07:57:01.337Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/fewnerd/\", \"data_count\": 37648, \"model_name\": \"qwen3-8b-fewnerd-exp021-merged\", \"seed\": 42, \"wall_clock_seconds\": 23067.3, \"gpu_hours\": 6.41}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-21T14:21:28.624Z\"}, \"exp_e2_pretrained_conll_s456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T13:03:31.532Z\", \"updated_at\": \"2026-05-21T14:20:10.292Z\", \"hypothesis\": \"E2 pre-trained baseline CoNLL seed=456: third seed for pretrained model SC analysis on CoNLL. Confirms reproducibility of correlation-selection gap pattern across seeds.\", \"parent\": \"exp_e2_pretrained_conll\", \"spec\": {\"command\": \"python -u code/run_mvp_pilot.py --model_path /root/autodl-tmp/.hf_cache/Qwen2.5-7B-Instruct --data_dir data/conll2003/ --dataset conll2003 --subtask ner --n_samples 8 --temperature 1.0 --seed 456 --collect_logprobs --output_dir output/e2_pretrained_conll_s456/\", \"server\": \"autodl-5090-c\", \"gpu\": [\"cuda:2\"], \"pid\": \"321549\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_e2_pretrained_conll_s456.log\", \"submitted_at\": \"2026-05-21T13:03:51.391Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/conll2003/\", \"data_count\": 3453, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": 456, \"checkpoint_source\": \"/root/autodl-tmp/.hf_cache/Qwen2.5-7B-Instruct\", \"eval_data\": \"data/conll2003/\", \"wall_clock_seconds\": 4578.9, \"gpu_hours\": 1.27}, \"checkpoint_path\": \"output/e2_pretrained_conll_s456/\", \"conclusion\": \"success\", \"metrics\": {\"greedy_f1\": 0.5384, \"oracle_f1\": 0.6272, \"oracle_headroom\": 0.089, \"rho_fk_full\": 0.376, \"rho_sj_full\": 0.391, \"rho_fk_cond\": 0.43, \"rho_sj_cond\": 0.443, \"logprob_rho_full\": -0.016, \"logprob_rho_cond\": 0.197, \"instances\": 3453, \"verdict\": \"MARGINAL\"}, \"completed_at\": \"2026-05-21T14:20:10.292Z\"}, \"exp_e2_pretrained_conll_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T13:03:29.048Z\", \"updated_at\": \"2026-05-21T14:20:06.659Z\", \"hypothesis\": \"E2 pre-trained baseline CoNLL seed=123: additional seed for pretrained Qwen2.5-7B-Instruct on CoNLL SC pipeline. Tests whether correlation-selection gap in pretrained model is reproducible across seeds.\", \"parent\": \"exp_e2_pretrained_conll\", \"spec\": {\"command\": \"python -u code/run_mvp_pilot.py --model_path /root/autodl-tmp/.hf_cache/Qwen2.5-7B-Instruct --data_dir data/conll2003/ --dataset conll2003 --subtask ner --n_samples 8 --temperature 1.0 --seed 123 --collect_logprobs --output_dir output/e2_pretrained_conll_s123/\", \"server\": \"autodl-5090-c\", \"gpu\": [\"cuda:1\"], \"pid\": \"321281\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_e2_pretrained_conll_s123.log\", \"submitted_at\": \"2026-05-21T13:03:48.082Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/conll2003/\", \"data_count\": 3453, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": 123, \"checkpoint_source\": \"/root/autodl-tmp/.hf_cache/Qwen2.5-7B-Instruct\", \"eval_data\": \"data/conll2003/\", \"wall_clock_seconds\": 4578.6, \"gpu_hours\": 1.27}, \"checkpoint_path\": \"output/e2_pretrained_conll_s123/\", \"conclusion\": \"success\", \"metrics\": {\"greedy_f1\": 0.5413, \"oracle_f1\": 0.6286, \"oracle_headroom\": 0.087, \"rho_fk_full\": 0.364, \"rho_sj_full\": 0.394, \"rho_fk_cond\": 0.434, \"rho_sj_cond\": 0.463, \"logprob_rho_full\": -0.027, \"logprob_rho_cond\": 0.188, \"instances\": 3453, \"verdict\": \"MARGINAL\"}, \"completed_at\": \"2026-05-21T14:20:06.659Z\"}, \"exp_conll_n16_s123\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-21T04:30:48.660Z\", \"updated_at\": \"2026-05-21T13:42:34.868Z\", \"hypothesis\": \"CoNLL N=16 seed=123: second seed for 3-seed N=16 coverage. Tests N-scaling consistency — whether oracle headroom increase from N=8→N=16 is reproducible across seeds.\", \"server\": \"autodl-5090-c\", \"gpu\": \"cuda:2\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie/ && python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-conll2003-merged --data_dir data/conll2003/ --dataset conll2003 --n_samples 16 --temperature 1.0 --seed 123 --collect_logprobs --output_dir output/conll_n16_s123/\\\"\", \"finished_at\": \"2026-05-21T12:57:26.904Z\"}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"completed_at\": \"2026-05-21T04:51:32.929Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-21T04:51:39.166251+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-21T12:57:34.157153+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"失败原因: tokenizer vocab_file=None — checkpoints/qwen3-8b-conll2003-merged 缺少 vocab.json，vLLM 初始化 tokenizer 时 TypeError。与 exp_conll_n16_s456 同根因。| 已有成果: 无（启动即崩溃）| 建议: 修复 merged checkpoint tokenizer 文件后重跑\"}}, \"notes\": \"重跑成功（首次因 tokenizer 缺失失败）。CoNLL N=16 seed=123: greedy=0.9077, oracle=0.9631, headroom=+0.0555。vs s42: greedy 0.908, oracle 0.9592, headroom 0.0512。种子间高度一致（greedy Δ<0.5pp, oracle Δ<0.5pp）。Structural > Surface confirmed (delta=+0.0103)。\", \"parent\": \"exp_conll_n16_s42\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie/ && python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-conll2003-merged --data_dir data/conll2003/ --dataset conll2003 --n_samples 16 --temperature 1.0 --seed 123 --collect_logprobs --output_dir output/conll_n16_s123/\\\"\", \"server\": \"autodl-5090-c\", \"data_path\": \"data/conll2003/\", \"data_count\": 3453, \"model_name\": \"Qwen3-8B-FT-CoNLL\", \"seed\": 123}, \"pid\": \"319306\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_conll_n16_s123.log\", \"metrics\": {\"greedy_f1\": 0.908, \"oracle_f1\": 0.963, \"oracle_headroom\": 0.055, \"rho_fk_cond\": 0.391, \"rho_sj_cond\": 0.417, \"logprob_rho_cond\": 0.373, \"structural_beats_surface\": true, \"verdict\": \"PASS\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"checkpoints/qwen3-8b-conll-lora-merged\"}, \"exp_scierc_n16_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:30:42.345Z\", \"updated_at\": \"2026-05-21T11:22:22.613Z\", \"hypothesis\": \"SciERC N=16 seed 123: second seed at N=16 tests variance of scaling behavior and confirms whether the N=8→N=16 gains observed with seed 42 (exp-001) are robust across random seeds.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data/ --dataset scierc --subtask ner --n_samples 16 --temperature 1.0 --seed 123 --collect_logprobs --output_dir output/scierc_n16_seed123/\", \"server\": \"autodl-5090-b\", \"data_path\": \"data/scierc/processed_data/\", \"data_count\": 551, \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 123}, \"log_path\": \"logs/scierc_n16_seed123.log\", \"checkpoint_path\": \"output/scierc_n16_seed123/\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T04:44:30.424Z\"}, \"exp_14b_inference_conll_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T10:42:21.744Z\", \"updated_at\": \"2026-05-21T11:22:19.979Z\", \"hypothesis\": \"14B CoNLL rerun: Qwen2.5-14B fine-tuned model (qwen25-14b-fewnerd-merged-final) on CoNLL NER inference N=8 T=1.0. Previous run (exp_14b_inference_conll) crashed at 55% with EngineDeadError on 5090-b. Tests whether 14B scale preserves correlation-selection gap pattern on CoNLL.\", \"parent\": \"exp_14b_inference_conll\", \"spec\": {\"command\": \"python -u code/run_mvp_pilot.py --model_path checkpoints/qwen25-14b-fewnerd-merged-final --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 8 --temperature 1.0 --seed 42 --collect_logprobs --output_dir output/14b_conll_v2/ --gpu_memory_utilization 0.95 --enforce_eager\", \"server\": \"autodl-5090-c\", \"data_path\": \"data/conll2003\", \"data_count\": 3453, \"model_name\": \"qwen25-14b-fewnerd-merged-final\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/qwen25-14b-fewnerd-merged-final\", \"eval_data\": \"conll2003\", \"checkpoint_path\": \"output/14b_conll_v2/\", \"log_path\": \"output/14b_conll_v2_run.log\"}, \"conclusion\": \"failed\", \"metrics\": {\"greedy_f1\": 0.0462, \"oracle_f1\": 0.1549, \"sample_f1_zero_pct\": 95.2, \"fleiss_kappa\": 0.3712, \"soft_jaccard\": 0.658, \"rho_sj_full\": -0.27, \"structural_beats_surface\": false, \"verdict\": \"FAIL — 14B model fine-tuned on FewNERD cannot do CoNLL NER (cross-domain mismatch)\"}, \"completed_at\": \"2026-05-21T11:22:19.979Z\"}, \"exp_frontier_sc_gemini25pro\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T06:50:24.793Z\", \"updated_at\": \"2026-05-21T11:19:52.427Z\", \"hypothesis\": \"Frontier model Gemini 2.5 Pro on FewNERD SC (200 inst, N=8, T=1.0): 4-family cross-validation. If correlation-selection gap persists across GPT + Claude + Gemini + DeepSeek, the finding is universal.\", \"spec\": {\"command\": \"python -u code/run_frontier_sc.py --model google/gemini-2.5-pro --base_url http://47.94.22.126/v1 --dataset fewnerd --n_instances 200 --n_samples 8 --temperature 1.0 --output_dir output/frontier_sc_gemini25pro/ --max_workers 4\", \"server\": \"autodl-5090-c\", \"data_path\": \"data/fewnerd/test.json\", \"data_count\": 200, \"model_name\": \"google/gemini-2.5-pro\", \"seed\": 42, \"checkpoint_path\": \"output/frontier_sc_gemini25pro/\", \"log_path\": \"output/frontier_sc_gemini25pro/run.log\"}, \"conclusion\": \"success\", \"metrics\": {\"greedy_f1\": 0.6301, \"mv_f1\": 0.6446, \"oracle_f1\": 0.7575, \"mv_gain_pp\": 1.45, \"selection_gap_pp\": 11.29, \"mv_captures_pct\": 11.4, \"agreement_rho\": 0.3887, \"degeneracy_rate\": 0.285, \"fleiss_kappa\": 0.5185, \"soft_jaccard\": 0.8023, \"alpha_crit\": 0.4756, \"alpha_crit_eff\": 0.6651, \"parse_failure_rate\": 0.119, \"n_instances\": 200, \"mv_wins\": 33, \"mv_ties\": 144, \"mv_loses\": 23, \"verdict\": \"MV helps (+1.45pp), captures 11% of oracle headroom\"}, \"completed_at\": \"2026-05-21T10:55:06.757Z\"}, \"exp_e2_pretrained_scierc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T07:18:21.189Z\", \"updated_at\": \"2026-05-21T10:57:52.364Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && python -u code/run_mvp_pilot.py --model_path /root/autodl-tmp/.hf_cache/Qwen2.5-7B-Instruct/ --data_dir data/scierc/processed_data/ --dataset scierc --subtask ner --n_samples 8 --temperature 1.0 --seed 42 --collect_logprobs --output_dir output/e2_pretrained_scierc/\\\"\", \"server\": \"autodl-5090-c\", \"gpu\": [\"cuda:3\"], \"pid\": \"294269\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_e2_pretrained_scierc.log\", \"submitted_at\": \"2026-05-21T07:18:20.538Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scierc/processed_data/\", \"data_count\": 100, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": 42, \"checkpoint_source\": \"pretrained_base\", \"eval_data\": \"scierc test set (100 instances, N=8)\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/e2_pretrained_scierc/\", \"wall_clock_seconds\": 6705.7, \"gpu_hours\": 1.86}, \"hypothesis\": \"Pre-trained Qwen2.5-7B-Instruct (no fine-tuning) on SciERC NER exhibits correlation-selection gap similar to fine-tuned models, demonstrating the gap is model-intrinsic rather than fine-tuning-induced.\", \"conclusion\": \"negative\", \"metrics\": {\"greedy_f1\": 0.2418, \"oracle_f1\": 0.3888, \"oracle_headroom\": 0.147, \"fleiss_kappa_mean\": 0.223, \"soft_jaccard_mean\": 0.473, \"rho_SJ_full\": 0.2193, \"rho_kappa_full\": 0.2516, \"rho_SJ_cond\": 0.1987, \"rho_kappa_cond\": 0.1953, \"logprob_rho_full\": 0.078, \"logprob_auroc_full\": 0.5412, \"logprob_rho_cond\": 0.1895, \"logprob_auroc_cond\": 0.5527, \"sample_f1_mean\": 0.2272, \"sample_f1_pct_zero\": 46.29, \"structural_beats_surface\": false, \"verdict\": \"FAIL\", \"warning\": \">30% samples F1=0\"}, \"checkpoint_path\": \"output/e2_pretrained_scierc/\", \"completed_at\": \"2026-05-21T09:10:06.217Z\"}, \"exp_e2_pretrained_conll\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T05:52:08.180Z\", \"updated_at\": \"2026-05-21T10:57:51.130Z\", \"hypothesis\": \"Pre-trained Qwen2.5-7B-Instruct (no fine-tuning) on CoNLL NER exhibits correlation-selection gap similar to fine-tuned models, demonstrating the gap is model-intrinsic rather than fine-tuning-induced.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && python -u code/run_mvp_pilot.py --model_path /root/autodl-tmp/models/Qwen2.5-7B-Instruct/Qwen/Qwen2___5-7B-Instruct --data_dir data/conll2003/ --dataset conll2003 --subtask ner --n_samples 8 --temperature 1.0 --seed 42 --collect_logprobs --output_dir output/e2_pretrained_conll/\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"7939\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/logs/exp_e2_pretrained_conll.log\", \"submitted_at\": \"2026-05-21T06:59:13.431Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/conll2003/\", \"data_count\": 3453, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": 42, \"checkpoint_source\": \"pretrained_base\", \"eval_data\": \"conll2003\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/e2_pretrained_conll/\", \"wall_clock_seconds\": 5840.6, \"gpu_hours\": 1.62}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T08:36:34.020Z\"}, \"exp_fewnerd_mf4v2_s456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T10:16:50.798Z\", \"updated_at\": \"2026-05-21T10:18:44.434Z\", \"spec\": {\"server\": \"autodl-5090\", \"data_path\": \"data/fewnerd/\", \"data_count\": 32565, \"model_name\": \"qwen3-8b-fewnerd-exp021-merged\", \"seed\": 456, \"command\": \"python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-fewnerd-exp021-merged --data_dir data/fewnerd/ --dataset fewnerd --subtask ner --n_samples 8 --temperature 1.0 --seed 456 --collect_logprobs --output_dir output/fewnerd_mf4v2_seed456/\"}, \"checkpoint_path\": \"output/fewnerd_mf4v2_seed456/\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_fewnerd_mf4v2_s456.log\", \"conclusion\": \"success\", \"metrics\": {\"greedy_f1\": 0.7889, \"oracle_f1\": 0.881, \"oracle_headroom\": 0.0921, \"fleiss_kappa_mean\": 0.3557, \"soft_jaccard_mean\": 0.6848, \"sample_f1_mean\": 0.6435, \"rho_softjaccard_full\": 0.3133, \"rho_fleiss_full\": 0.1647, \"rho_logprob_full\": 0.245, \"verdict\": \"MARGINAL\"}, \"hypothesis\": \"MF4v2 pipeline (N=8, T=1.0, logprobs) on FewNERD with seed 456 produces consistent SC diagnostic signals (structural agreement > logprob baseline for quality estimation), validating cross-seed stability of the structured self-consistency framework on fine-grained NER.\", \"completed_at\": \"2026-05-21T10:18:44.434Z\"}, \"exp_scierc_mf4_v2_s456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T09:28:19.668Z\", \"updated_at\": \"2026-05-21T10:18:41.541Z\", \"spec\": {\"command\": \"python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask ner --n_samples 8 --temperature 1.0 --seed 456 --collect_logprobs --output_dir output/scierc_mf4v2_seed456/\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"20216\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_scierc_mf4_v2_s456.log\", \"submitted_at\": \"2026-05-21T09:28:18.878Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 529, \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 456, \"wall_clock_seconds\": 3022.7, \"gpu_hours\": 0.84}, \"checkpoint_path\": \"output/scierc_mf4v2_seed456/\", \"conclusion\": \"success\", \"metrics\": {\"greedy_f1\": 0.6631, \"oracle_f1\": 0.7732, \"oracle_headroom\": 0.1101, \"fleiss_kappa_mean\": 0.3885, \"soft_jaccard_mean\": 0.6945, \"sample_f1_mean\": 0.6061, \"rho_softjaccard_full\": 0.3756, \"rho_fleiss_full\": 0.2832, \"rho_logprob_full\": 0.2184, \"verdict\": \"MARGINAL\"}, \"hypothesis\": \"MF4v2 pipeline (N=8, T=1.0, logprobs) on SciERC with seed 456 produces consistent SC diagnostic signals (structural agreement > logprob baseline for quality estimation), validating cross-seed stability of the structured self-consistency framework on scientific NER.\", \"completed_at\": \"2026-05-21T10:18:41.541Z\"}, \"exp_scierc_mf4_v2_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T09:28:16.909Z\", \"updated_at\": \"2026-05-21T10:18:38.627Z\", \"spec\": {\"command\": \"python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask ner --n_samples 8 --temperature 1.0 --seed 123 --collect_logprobs --output_dir output/scierc_mf4v2_seed123/\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:1\"], \"pid\": \"20074\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_scierc_mf4_v2_s123.log\", \"submitted_at\": \"2026-05-21T09:28:16.177Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 529, \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 123, \"wall_clock_seconds\": 3022.4, \"gpu_hours\": 0.84}, \"checkpoint_path\": \"output/scierc_mf4v2_seed123/\", \"conclusion\": \"success\", \"metrics\": {\"greedy_f1\": 0.6633, \"oracle_f1\": 0.7777, \"oracle_headroom\": 0.1144, \"fleiss_kappa_mean\": 0.3754, \"soft_jaccard_mean\": 0.6977, \"sample_f1_mean\": 0.6079, \"rho_softjaccard_full\": 0.3681, \"rho_fleiss_full\": 0.2457, \"rho_logprob_full\": 0.2209, \"verdict\": \"MARGINAL\"}, \"hypothesis\": \"MF4v2 pipeline (N=8, T=1.0, logprobs) on SciERC with seed 123 produces consistent SC diagnostic signals (structural agreement > logprob baseline for quality estimation), validating cross-seed stability of the structured self-consistency framework on scientific NER.\", \"completed_at\": \"2026-05-21T10:18:38.627Z\"}, \"exp_b1_scd\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T11:12:48.805Z\", \"updated_at\": \"2026-05-21T10:17:14.946Z\", \"hypothesis\": \"Self-Consistency Distillation via theta2n construction pseudo-labels can teach Qwen3-8B-FT to internalize SC benefits: after iterative SCD (M0→M1→M2→M3), greedy F1 should approach N=8 construction F1 (FewNERD target: 0.764 vs current greedy 0.748). CoNLL serves as negative control (construction Δ=-0.4pp, SCD should not help). Transductive setting: pseudo-labels from test set SC outputs.\", \"conclusion\": \"killed\", \"spec\": {\"command\": \"cancelled by Director\", \"server\": \"none\", \"data_path\": \"n/a\", \"data_count\": 0, \"model_name\": \"n/a\", \"seed\": 0, \"checkpoint_path\": \"n/a\", \"log_path\": \"n/a\", \"kill_reason\": \"Director cancelled - experiment no longer aligned with current research direction\"}, \"completed_at\": \"2026-05-21T10:17:14.946Z\"}, \"exp_fewnerd_mf4_v2_s456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T05:34:07.139Z\", \"updated_at\": \"2026-05-21T10:10:07.222Z\", \"hypothesis\": \"MF4 pipeline fix v2: FewNERD N=8 T=1.0 seed=456 using run_mvp_pilot.py (greedy_f1/micro-F1). Third seed completing 3-seed set for statistical power.\", \"spec\": {\"command\": \"bash -c \\\"...\\\"\", \"server\": \"autodl-5090-b\", \"gpu\": \"cuda:2\", \"pid\": \"334423\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_fewnerd_mf4_v2_s456.log\", \"submitted_at\": \"2026-05-21T08:33:57.773Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/fewnerd/\", \"data_count\": 32565, \"model_name\": \"qwen3-8b-fewnerd-exp021-merged\", \"seed\": 456, \"checkpoint_path\": \"LOST - server shutdown\", \"kill_reason\": \"5090-b server shutdown by user\", \"wall_clock_seconds\": 5769.4, \"gpu_hours\": 1.6}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-21T10:10:07.222Z\"}, \"exp_conll_mf4_v2_s456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T05:34:10.294Z\", \"updated_at\": \"2026-05-21T09:11:29.209Z\", \"hypothesis\": \"MF4 pipeline fix v2: CoNLL N=8 T=1.0 seed=456 using run_mvp_pilot.py (greedy_f1/micro-F1). 3-seed set with exp_conll_t10_s42.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-conll2003-merged --data_dir data/conll2003/ --dataset conll2003 --subtask ner --n_samples 8 --temperature 1.0 --seed 456 --collect_logprobs --output_dir output/conll_mf4v2_seed456/\\\"\", \"server\": \"autodl-5090-b\", \"gpu\": [\"cuda:1\"], \"pid\": \"334155\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_conll_mf4_v2_s456.log\", \"submitted_at\": \"2026-05-21T08:33:55.428Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/conll2003/\", \"data_count\": 3453, \"model_name\": \"qwen3-8b-conll2003-merged\", \"seed\": 456, \"checkpoint_source\": \"checkpoints/qwen3-8b-conll2003-merged\", \"eval_data\": \"conll2003 test set (3453 instances, N=8)\", \"wall_clock_seconds\": 2253.8, \"gpu_hours\": 0.63}, \"checkpoint_path\": \"output/conll_mf4v2_seed456/\", \"metrics\": {\"greedy_f1\": 0.907, \"oracle_f1\": 0.9426, \"oracle_headroom\": 0.0357, \"fleiss_kappa_mean\": 0.768, \"soft_jaccard_mean\": 0.892, \"rho_SJ_full\": 0.4803, \"rho_kappa_full\": 0.4638, \"rho_SJ_cond\": 0.4513, \"rho_kappa_cond\": 0.425, \"logprob_rho_full\": 0.3213, \"logprob_rho_cond\": 0.3723, \"logprob_auroc_full\": 0.7569, \"logprob_auroc_cond\": 0.8221, \"sample_f1_mean\": 0.8737, \"sample_f1_pct_zero\": 7.08, \"structural_beats_surface\": true, \"rho_advantage\": 0.0166, \"verdict\": \"PASS\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T09:11:29.209Z\"}, \"exp_conll_mf4_v2_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T05:34:09.147Z\", \"updated_at\": \"2026-05-21T09:11:26.284Z\", \"hypothesis\": \"MF4 pipeline fix v2: CoNLL N=8 T=1.0 seed=123 using run_mvp_pilot.py (greedy_f1/micro-F1). 3-seed set with exp_conll_t10_s42.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-conll2003-merged --data_dir data/conll2003/ --dataset conll2003 --subtask ner --n_samples 8 --temperature 1.0 --seed 123 --collect_logprobs --output_dir output/conll_mf4v2_seed123/\\\"\", \"server\": \"autodl-5090-b\", \"gpu\": [\"cuda:0\"], \"pid\": \"334013\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_conll_mf4_v2_s123.log\", \"submitted_at\": \"2026-05-21T08:33:53.084Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/conll2003/\", \"data_count\": 3453, \"model_name\": \"qwen3-8b-conll2003-merged\", \"seed\": 123, \"checkpoint_source\": \"checkpoints/qwen3-8b-conll2003-merged\", \"eval_data\": \"conll2003 test set (3453 instances, N=8)\", \"wall_clock_seconds\": 2253.2, \"gpu_hours\": 0.63}, \"checkpoint_path\": \"output/conll_mf4v2_seed123/\", \"metrics\": {\"greedy_f1\": 0.9083, \"oracle_f1\": 0.9527, \"oracle_headroom\": 0.0444, \"fleiss_kappa_mean\": 0.762, \"soft_jaccard_mean\": 0.886, \"rho_SJ_full\": 0.4628, \"rho_kappa_full\": 0.4457, \"rho_SJ_cond\": 0.414, \"rho_kappa_cond\": 0.3887, \"logprob_rho_full\": 0.3281, \"logprob_rho_cond\": 0.367, \"logprob_auroc_full\": 0.7621, \"logprob_auroc_cond\": 0.8198, \"sample_f1_mean\": 0.8744, \"sample_f1_pct_zero\": 7.05, \"structural_beats_surface\": true, \"rho_advantage\": 0.0171, \"verdict\": \"PASS\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T09:11:26.284Z\"}, \"exp_frontier_sc_deepseek\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T06:50:26.022Z\", \"updated_at\": \"2026-05-21T09:10:40.589Z\", \"hypothesis\": \"Frontier model DeepSeek Chat on FewNERD SC (200 inst, N=8, T=1.0): 4-family cross-validation of correlation-selection gap universality.\", \"spec\": {\"command\": \"python -u code/run_frontier_sc.py --model deepseek/deepseek-chat --base_url http://47.94.22.126/v1 --dataset fewnerd --n_instances 200 --n_samples 8 --temperature 1.0 --output_dir output/frontier_sc_deepseek/ --max_workers 4\", \"server\": \"autodl-5090-c\", \"data_path\": \"data/fewnerd/test.json\", \"data_count\": 200, \"model_name\": \"deepseek/deepseek-chat\", \"seed\": 42}, \"checkpoint_path\": \"output/frontier_sc_deepseek/\", \"log_path\": \"logs/frontier_sc_deepseek.log\", \"metrics\": {\"greedy_f1\": 0.3992, \"mv_f1\": 0.4243, \"oracle_f1\": 0.714, \"degeneracy_rate\": 0.055, \"agreement_rho\": 0.2051, \"fleiss_kappa_rho\": 0.1471, \"sj_rho\": 0.1635, \"mv_gain_over_greedy\": 0.0251, \"selection_gap\": 0.2897, \"parse_failure_count\": 751, \"total_api_calls\": 1600, \"elapsed_s\": 4043.7}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T09:10:40.589Z\"}, \"exp_conll_n16_s456_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T05:05:07.022Z\", \"updated_at\": \"2026-05-21T09:10:12.516Z\", \"hypothesis\": \"CoNLL N=16 (seed=456, v2): retry after previous failure on 5090. Third seed for 3-seed statistical power on CoNLL-2003 N=16.\", \"parent\": \"exp_conll_n16_s456\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-conll2003-merged --data_dir data/conll2003/ --dataset conll2003 --subtask ner --n_samples 16 --temperature 1.0 --seed 456 --collect_logprobs --output_dir output/conll_n16_seed456_v2/\\\"\", \"server\": \"autodl-5090-c\", \"gpu\": [\"cuda:2\"], \"pid\": \"293990\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_conll_n16_s456_v2.log\", \"submitted_at\": \"2026-05-21T07:18:17.355Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/conll2003/\", \"data_count\": 3453, \"model_name\": \"qwen3-8b-conll2003-merged\", \"seed\": 456, \"checkpoint_source\": \"checkpoints/qwen3-8b-conll2003-merged\", \"eval_data\": \"conll2003 test set (3453 instances, N=16)\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/conll_n16_seed456_v2/\", \"wall_clock_seconds\": 6703.7, \"gpu_hours\": 1.86}, \"conclusion\": \"success\", \"metrics\": {\"greedy_f1\": 0.9076, \"oracle_f1\": 0.955, \"oracle_headroom\": 0.0474, \"fleiss_kappa_mean\": 0.8, \"soft_jaccard_mean\": 0.8965, \"rho_SJ_full\": 0.4791, \"rho_kappa_full\": 0.4697, \"rho_SJ_cond\": 0.4481, \"rho_kappa_cond\": 0.4268, \"logprob_rho_full\": 0.3137, \"logprob_rho_cond\": 0.373, \"logprob_auroc_full\": 0.7524, \"logprob_auroc_cond\": 0.8236, \"sample_f1_mean\": 0.8736, \"sample_f1_pct_zero\": 7.03, \"verdict\": \"PASS\"}, \"completed_at\": \"2026-05-21T09:10:01.095Z\", \"checkpoint_path\": \"output/conll_n16_seed456_v2/\"}, \"exp_conll_n16_s123_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T05:05:03.921Z\", \"updated_at\": \"2026-05-21T09:10:11.273Z\", \"hypothesis\": \"CoNLL N=16 (seed=123, v2): retry after previous failure on 5090 (damaged checkpoint). Extending N-scaling curve to N=16 for Qwen3-8B-FT on CoNLL-2003.\", \"parent\": \"exp_conll_n16_s123\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-conll2003-merged --data_dir data/conll2003/ --dataset conll2003 --subtask ner --n_samples 16 --temperature 1.0 --seed 123 --collect_logprobs --output_dir output/conll_n16_seed123_v2/\\\"\", \"server\": \"autodl-5090-c\", \"gpu\": [\"cuda:1\"], \"pid\": \"293577\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_conll_n16_s123_v2.log\", \"submitted_at\": \"2026-05-21T07:18:14.095Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/conll2003/\", \"data_count\": 3453, \"model_name\": \"qwen3-8b-conll2003-merged\", \"seed\": 123, \"checkpoint_source\": \"checkpoints/qwen3-8b-conll2003-merged\", \"eval_data\": \"conll2003 test set (3453 instances, N=16)\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/conll_n16_seed123_v2/\", \"wall_clock_seconds\": 6702.6, \"gpu_hours\": 1.86}, \"conclusion\": \"success\", \"metrics\": {\"greedy_f1\": 0.9071, \"oracle_f1\": 0.9625, \"oracle_headroom\": 0.0554, \"fleiss_kappa_mean\": 0.767, \"soft_jaccard_mean\": 0.877, \"rho_SJ_full\": 0.4567, \"rho_kappa_full\": 0.4469, \"rho_SJ_cond\": 0.4174, \"rho_kappa_cond\": 0.3936, \"logprob_rho_full\": 0.3456, \"logprob_rho_cond\": 0.375, \"logprob_auroc_full\": 0.7742, \"logprob_auroc_cond\": 0.8258, \"sample_f1_mean\": 0.8676, \"sample_f1_pct_zero\": 7.52, \"verdict\": \"PASS\"}, \"completed_at\": \"2026-05-21T09:09:56.663Z\", \"checkpoint_path\": \"output/conll_n16_seed123_v2/\"}, \"exp_frontier_sc_claude_sonnet4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T06:20:27.878Z\", \"updated_at\": \"2026-05-21T08:58:17.224Z\", \"hypothesis\": \"Frontier model Claude Sonnet 4 on FewNERD SC (200 instances, N=8, T=1.0): if correlation-selection gap persists across model families (GPT + Claude + Gemini + DeepSeek), the finding is universal and not model-specific.\", \"spec\": {\"command\": \"python -u code/run_frontier_sc.py --model anthropic/claude-sonnet-4 --base_url http://47.94.22.126/v1 --dataset fewnerd --data_dir data/fewnerd/ --n_instances 200 --n_samples 8 --temperature 1.0 --output_dir output/frontier_sc_claude_sonnet4/ --max_tokens 4096\", \"server\": \"autodl-5090\", \"data_path\": \"data/fewnerd/test.json\", \"data_count\": 200, \"model_name\": \"anthropic/claude-sonnet-4\", \"seed\": 42, \"pid\": 6302, \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/logs/frontier_sc_claude_sonnet4.log\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/frontier_sc_claude_sonnet4/\", \"checkpoint_source\": \"API (http://47.94.22.126/v1)\", \"eval_data\": \"fewnerd test set (200 instances, N=8, T=1.0)\", \"matching\": \"text+type (case-insensitive, no offset)\", \"note\": \"v2: fixed from offset-based to text-based entity matching for API models\"}, \"conclusion\": \"success\", \"metrics\": {\"greedy_f1\": 0.6068, \"mv_f1\": 0.6226, \"oracle_f1\": 0.6544, \"degeneracy_rate\": 0.74, \"selection_gap\": 0.0318, \"parse_failures\": 103, \"api_calls\": 1600, \"wall_clock_seconds\": 6118, \"instances\": 200}, \"completed_at\": \"2026-05-21T08:58:17.224Z\"}, \"exp_frontier_sc_gpt55_fewnerd_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:48:24.698Z\", \"updated_at\": \"2026-05-21T08:36:36.829Z\", \"hypothesis\": \"Frontier model GPT-5.5 on FewNERD SC (200 instances, N=8, T=1.0): if correlation-selection gap persists in frontier models, the finding is fundamental and not a model capability limitation. Previous attempt failed due to API credit exhaustion.\", \"parent\": \"exp_b_frontier_sc_fewnerd\", \"spec\": {\"command\": \"python -u code/run_frontier_sc.py --model gpt-5.5 --base_url http://47.94.22.126/v1 --n_instances 200 --n_samples 8 --temperature 1.0 --seed 42 --max_workers 4\", \"server\": \"autodl-5090-c\", \"data_path\": \"data/fewnerd/test.json\", \"data_count\": 200, \"model_name\": \"gpt-5.5\", \"seed\": 42, \"checkpoint_source\": \"openai/gpt-5.5 (API)\", \"eval_data\": \"fewnerd test set (200 instances)\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/frontier_sc_gpt55_fewnerd_v2/\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/logs/frontier_sc_gpt55_fewnerd_v2.log\"}, \"conclusion\": \"success\", \"metrics\": {\"greedy_f1\": 0.6382, \"mv_f1\": 0.6521, \"oracle_f1\": 0.7203, \"degeneracy_rate\": 0.5, \"rho_agreement\": 0.3551, \"rho_fk\": 0.3515, \"rho_sj\": 0.3461, \"instances\": 200}, \"completed_at\": \"2026-05-21T08:36:36.829Z\"}, \"exp_fewnerd_n16_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:30:46.569Z\", \"updated_at\": \"2026-05-21T08:33:07.868Z\", \"hypothesis\": \"FewNERD N=16 (seed=42): extending N-scaling curve to N=16 for Qwen3-8B-FT. Tests whether oracle gains plateau or continue at higher sample counts, critical for F1(N)=a-b*N^(-c) scaling law estimation.\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/fewnerd_n16_seed42/\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/logs/fewnerd_n16_seed42.log\"}, \"server\": \"autodl-5090-b\", \"gpu\": \"cuda:2\", \"conclusion\": \"success\", \"metrics\": {\"greedy_f1\": 0.7886, \"oracle_f1\": 0.9059, \"oracle_headroom\": 0.117, \"rho_fk_full\": 0.162, \"rho_sj_full\": 0.211, \"rho_fk_cond\": -0.019, \"rho_sj_cond\": 0.212, \"logprob_rho_full\": 0.139, \"logprob_rho_cond\": 0.175, \"instances\": 37648}, \"completed_at\": \"2026-05-21T08:33:07.868Z\"}, \"exp_fewnerd_t12_s456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T03:11:46.378Z\", \"updated_at\": \"2026-05-21T08:32:53.474Z\", \"hypothesis\": \"FewNERD temperature ablation (T=1.2, seed=456): third seed complementing seed=42+123 for 3-seed statistical power. N=8, Qwen3-8B-FT.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-fewnerd-exp021-merged --data_dir data/fewnerd/ --dataset fewnerd --subtask ner --n_samples 8 --temperature 1.2 --seed 456 --collect_logprobs --output_dir output/fewnerd_t12_s456/\", \"server\": \"autodl-5090-b\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/fewnerd/test.json\", \"data_count\": 37648, \"model_name\": \"qwen3-8b-fewnerd-exp021-merged\", \"seed\": 456, \"gpu\": \"cuda:1\", \"pid\": 305834, \"tmux_session\": \"fewnerd_t12_s456\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/logs/fewnerd_t12_s456.log\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/fewnerd_t12_s456/\", \"checkpoint_source\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-fewnerd-exp021-merged\", \"eval_data\": \"fewnerd test set (37648 instances)\"}, \"conclusion\": \"success\", \"metrics\": {\"greedy_f1\": 0.7885, \"oracle_f1\": 0.8775, \"oracle_headroom\": 0.089, \"rho_fk_full\": 0.191, \"rho_sj_full\": 0.29, \"rho_fk_cond\": 0.015, \"rho_sj_cond\": 0.254, \"degeneracy_rate\": null, \"logprob_rho_full\": 0.196, \"logprob_rho_cond\": 0.245, \"instances\": 37648}, \"completed_at\": \"2026-05-21T08:32:53.474Z\"}, \"exp_14b_inference_fewnerd\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-20T14:36:27.954Z\", \"updated_at\": \"2026-05-21T07:51:33.030Z\", \"hypothesis\": \"14B Qwen2.5 inference on FewNERD (N∈{1,2,4,8}): primary dataset should show oracle scaling law F1(N)=a-b*N^(-c) consistent at 14B scale, filling the scaling curve between 7B and 32B. N=16 cut per Director decision.\", \"notes\": \"2026-05-21T00:50 RESTORED to RUNNING per Director. PID 252310 confirmed alive by Reviewer (cuda:0 98% util, elapsed 16min). 5th false-negative misdiagnosis. N=1 greedy_f1=0.7985, N=2 greedy_f1=0.7985/oracle=0.8086, N=4 greedy_f1=0.7984/oracle=0.8544. kill_after_n8.sh active (PID 224789).\", \"spec\": {\"server\": \"autodl-5090-c\", \"pid\": 252310, \"gpu\": \"cuda:0\", \"model_name\": \"Qwen2.5-14B-Instruct\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/fewnerd/\", \"seed\": 42, \"checkpoint_path\": \"N/A\", \"log_path\": \"N/A\"}, \"server\": \"autodl-5090-c\", \"gpu\": \"cuda:0\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-21T00:46:56.565632+00:00\"}, {\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-21T07:17:12.232308+00:00\"}]}, \"conclusion\": \"success\", \"reproduce\": {\"finished_at\": \"2026-05-21T07:17:01.438Z\"}, \"failure_reason\": \"\", \"completed_at\": \"2026-05-21T07:17:05.380Z\", \"metrics\": {\"fewnerd_n1\": {\"greedy_f1\": 0.7985, \"oracle_f1\": 0.7541, \"oracle_headroom\": -0.044, \"verdict\": \"FAIL\"}, \"fewnerd_n2\": {\"greedy_f1\": 0.7985, \"oracle_f1\": 0.8086, \"oracle_headroom\": 0.01, \"soft_jaccard_rho_full\": 0.205, \"rho_advantage\": -0.006, \"structural_beats_surface\": false, \"verdict\": \"FAIL\"}, \"fewnerd_n4\": {\"greedy_f1\": 0.7984, \"oracle_f1\": 0.8544, \"oracle_headroom\": 0.056, \"soft_jaccard_rho_full\": 0.314, \"rho_advantage\": 0.042, \"structural_beats_surface\": true, \"verdict\": \"MARGINAL\"}, \"fewnerd_n8\": {\"greedy_f1\": 0.7984, \"oracle_f1\": 0.8791, \"oracle_headroom\": 0.081, \"soft_jaccard_rho_full\": 0.324, \"rho_advantage\": 0.083, \"structural_beats_surface\": true, \"verdict\": \"MARGINAL\"}, \"cross_domain_scierc_conll\": \"completed but expected poor (cross-domain)\", \"n16_status\": \"cut per Director decision, kill_after_n8.sh executed\"}, \"checkpoint_path\": \"output/14b_final_inference/\"}, \"exp_fewnerd_mf4_v2_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T05:33:24.304Z\", \"updated_at\": \"2026-05-21T07:44:50.506Z\", \"hypothesis\": \"MF4 pipeline fix v2: FewNERD N=8 T=1.0 seed=42 using run_mvp_pilot.py (greedy_f1/micro-F1). Replaces exp_021 which used incompatible greedy_macro_f1. 3-seed statistical power.\", \"spec\": {\"command\": \"python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-fewnerd-exp021-merged --data_dir data/fewnerd/ --dataset fewnerd --subtask ner --n_samples 8 --temperature 1.0 --seed 42 --collect_logprobs --output_dir output/fewnerd_mf4v2_seed42/\", \"server\": \"autodl-5090-b\", \"gpu\": \"cuda:0\", \"pid\": 320158, \"log_path\": \"~/runs/struct_self_consist_ie/exp_fewnerd_mf4_v2_s42.log\", \"submitted_at\": \"2026-05-21T05:33:33.770Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/fewnerd/test.json\", \"data_count\": 37648, \"model_name\": \"qwen3-8b-fewnerd-exp021-merged\", \"seed\": 42, \"checkpoint_path\": \"output/fewnerd_mf4v2_seed42/\", \"wall_clock_seconds\": 7644}, \"reproduce\": {\"finished_at\": \"2026-05-21T07:40:57.810Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-21T07:41:07.901551+00:00\"}]}, \"metrics\": {\"greedy_f1\": 0.7883, \"oracle_f1\": 0.8783, \"oracle_headroom\": 0.09, \"fleiss_kappa_mean\": 0.3531, \"soft_jaccard_mean\": 0.6747, \"rho_SJ_full\": 0.1634, \"rho_kappa_full\": 0.0476, \"rho_SJ_cond\": 0.1987, \"rho_kappa_cond\": -0.0327, \"rho_advantage_full\": 0.1158, \"rho_advantage_cond\": 0.2314, \"structural_beats_surface\": true, \"sample_f1_mean\": 0.6123, \"sample_f1_std\": 0.3913, \"sample_f1_pct_zero\": 23.09, \"n_instances\": 37648, \"n_valid_full\": 32565, \"n_valid_cond\": 28682, \"n_gold_empty_filtered\": 5083, \"n_greedy_f1_zero_filtered\": 3883, \"logprob_rho_full\": 0.1544, \"logprob_tau_full\": 0.115, \"logprob_auroc_full\": 0.5771, \"logprob_rho_cond\": 0.1641, \"logprob_tau_cond\": 0.123, \"logprob_auroc_cond\": 0.5768, \"verdict\": \"FAIL\"}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-21T07:44:50.506Z\"}, \"exp_fewnerd_mf4_v2_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T05:33:25.463Z\", \"updated_at\": \"2026-05-21T07:41:29.072Z\", \"hypothesis\": \"MF4 pipeline fix v2: FewNERD N=8 T=1.0 seed=123 using run_mvp_pilot.py (greedy_f1/micro-F1). Replaces exp_021 which used incompatible greedy_macro_f1. 3-seed statistical power.\", \"spec\": {\"command\": \"python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-fewnerd-exp021-merged --data_dir data/fewnerd/ --dataset fewnerd --subtask ner --n_samples 8 --temperature 1.0 --seed 123 --collect_logprobs --output_dir output/fewnerd_mf4v2_seed123/\", \"server\": \"autodl-5090-b\", \"gpu\": \"cuda:1\", \"pid\": 320302, \"log_path\": \"~/runs/struct_self_consist_ie/exp_fewnerd_mf4_v2_s123.log\", \"submitted_at\": \"2026-05-21T05:33:36.193Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/fewnerd/test.json\", \"data_count\": 37648, \"model_name\": \"qwen3-8b-fewnerd-exp021-merged\", \"seed\": 123, \"checkpoint_path\": \"output/fewnerd_mf4v2_seed123/\", \"wall_clock_seconds\": 7672.9, \"gpu_hours\": 2.13}, \"reproduce\": {\"finished_at\": \"2026-05-21T07:38:22.503Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-21T07:38:30.204681+00:00\"}]}, \"metrics\": {\"greedy_f1\": 0.7883, \"oracle_f1\": 0.8891, \"oracle_headroom\": 0.1009, \"fleiss_kappa_mean\": 0.3483, \"soft_jaccard_mean\": 0.6689, \"rho_SJ_full\": 0.307, \"rho_kappa_full\": 0.1588, \"rho_SJ_cond\": 0.1966, \"rho_kappa_cond\": 0.0031, \"rho_advantage_full\": 0.1482, \"rho_advantage_cond\": 0.1935, \"structural_beats_surface\": true, \"sample_f1_mean\": 0.6364, \"sample_f1_std\": 0.3819, \"sample_f1_pct_zero\": 20.49, \"n_instances\": 37648, \"n_valid_full\": 32565, \"n_valid_cond\": 28685, \"n_gold_empty_filtered\": 5083, \"n_greedy_f1_zero_filtered\": 3880, \"logprob_rho_full\": 0.2193, \"logprob_tau_full\": 0.1641, \"logprob_auroc_full\": 0.6056, \"logprob_rho_cond\": 0.1818, \"logprob_tau_cond\": 0.1369, \"logprob_auroc_cond\": 0.5892, \"verdict\": \"MARGINAL\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T07:41:29.072Z\"}, \"exp_fewnerd_7b_n16_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T02:32:29.897Z\", \"updated_at\": \"2026-05-21T07:17:35.321Z\", \"hypothesis\": \"FewNERD N=16 with Qwen2.5-7B: extending N-scaling curve to N=16 for 7B model. At N=8 the 7B model shows diminishing oracle gains; N=16 tests whether the plateau continues or breaks, providing a critical data point for the N-scaling law F1(N)=a-b*N^(-c) at the 7B scale.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u code/run_mvp_pilot.py --model_path checkpoints/qwen25-7b-fewnerd-merged --data_dir data/fewnerd/ --dataset fewnerd --n_samples 16 --temperature 1.0 --seed 42 --collect_logprobs --output_dir output/fewnerd_7b_n16_seed42/\", \"server\": \"autodl-5090-c\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/fewnerd/test.json\", \"data_count\": 37648, \"model_name\": \"qwen25-7b-fewnerd-merged\", \"seed\": 42, \"gpu\": \"cuda:2\", \"pid\": 264869, \"log_path\": \"N/A\", \"checkpoint_path\": \"N/A\", \"checkpoint_source\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen25-7b-fewnerd-merged\", \"eval_data\": \"fewnerd test set (37648 instances, N=16)\"}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-21T07:17:35.321Z\"}, \"exp_fewnerd_n16_s456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:30:45.512Z\", \"updated_at\": \"2026-05-21T07:13:32.225Z\", \"hypothesis\": \"FewNERD N=16 (seed=456): extending N-scaling curve to N=16 for Qwen3-8B-FT. Tests whether oracle gains plateau or continue at higher sample counts, critical for F1(N)=a-b*N^(-c) scaling law estimation. Third seed for 3-seed statistical power.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-fewnerd-exp021-merged --data_dir data/fewnerd/ --dataset fewnerd --subtask ner --n_samples 16 --temperature 1.0 --seed 456 --collect_logprobs --output_dir output/fewnerd_n16_seed456/\", \"server\": \"autodl-5090-c\", \"data_path\": \"data/fewnerd/\", \"data_count\": 14770, \"model_name\": \"qwen3-8b-fewnerd-exp021-merged\", \"seed\": 456}, \"server\": \"autodl-5090-c\", \"gpu\": \"cuda:3\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-21T07:13:32.225Z\"}, \"exp_conll_mf4_s456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T05:09:11.484Z\", \"updated_at\": \"2026-05-21T06:54:56.063Z\", \"hypothesis\": \"MF4 pipeline fix: CoNLL N=8 T=1.0 seed=456 using run_mvp_pilot.py (greedy_f1/micro-F1). Extends exp_conll_t10_s42 to 3-seed set for statistical power.\", \"parent\": \"exp_conll_t10_s42\", \"spec\": {\"command\": \"python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-conll2003-merged --data_dir data/conll2003/ --dataset conll2003 --subtask ner --n_samples 8 --temperature 1.0 --seed 456 --collect_logprobs --output_dir output/conll_mf4_seed456/\", \"server\": \"autodl-5090\", \"data_path\": \"data/conll2003/\", \"data_count\": 3453, \"model_name\": \"qwen3-8b-conll2003-merged\", \"seed\": 456, \"checkpoint_source\": \"checkpoints/qwen3-8b-conll2003-merged\", \"eval_data\": \"data/conll2003/test.json\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-21T06:54:56.063Z\"}, \"exp_conll_mf4_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T05:09:06.021Z\", \"updated_at\": \"2026-05-21T05:53:05.635Z\", \"hypothesis\": \"MF4 pipeline fix: CoNLL N=8 T=1.0 seed=123 using run_mvp_pilot.py (greedy_f1/micro-F1). Extends exp_conll_t10_s42 to 3-seed set for statistical power.\", \"parent\": \"exp_conll_t10_s42\", \"spec\": {\"command\": \"python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-conll2003-merged --data_dir data/conll2003/ --dataset conll2003 --subtask ner --n_samples 8 --temperature 1.0 --seed 123 --collect_logprobs --output_dir output/conll_mf4_seed123/\", \"server\": \"autodl-5090\", \"data_path\": \"data/conll2003/\", \"data_count\": 3453, \"model_name\": \"qwen3-8b-conll2003-merged\", \"seed\": 123, \"checkpoint_source\": \"checkpoints/qwen3-8b-conll2003-merged\", \"eval_data\": \"data/conll2003/test.json\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-21T05:53:05.635Z\"}, \"exp_fewnerd_t05_s456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T03:11:43.659Z\", \"updated_at\": \"2026-05-21T05:50:43.777Z\", \"hypothesis\": \"FewNERD temperature ablation (T=0.5, seed=456): third seed complementing seed=42+123 for 3-seed statistical power. N=8, Qwen3-8B-FT.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-fewnerd-exp021-merged --data_dir data/fewnerd/ --dataset fewnerd --subtask ner --n_samples 8 --temperature 0.5 --seed 456 --collect_logprobs --output_dir output/fewnerd_t05_s456/\", \"server\": \"autodl-5090-b\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/fewnerd/test.json\", \"data_count\": 37648, \"model_name\": \"qwen3-8b-fewnerd-exp021-merged\", \"seed\": 456, \"gpu\": \"cuda:0\", \"pid\": 305832, \"tmux_session\": \"fewnerd_t05_s456\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/logs/fewnerd_t05_s456.log\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/fewnerd_t05_s456/\", \"checkpoint_source\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-fewnerd-exp021-merged\", \"eval_data\": \"fewnerd test set (37648 instances)\"}, \"reproduce\": {\"finished_at\": \"2026-05-21T05:32:07.140Z\"}, \"failure_reason\": \"false alarm: cron detected process dead but experiment had completed successfully (37648/37648 instances, report.json + samples.jsonl generated)\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T05:32:10.869Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-21T05:32:18.820026+00:00\"}]}}, \"exp_14b_inference_conll\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T14:36:26.315Z\", \"updated_at\": \"2026-05-21T04:57:40.651Z\", \"hypothesis\": \"14B Qwen2.5 inference on CoNLL (N∈{1,2,4,8}): filling scale curve between 8B (greedy F1=0.907) and 32B. Tests whether 14B shows intermediate behavior in SC diagnostic metrics.\", \"reproduce\": {\"finished_at\": \"2026-05-20T14:49:00.238Z\"}, \"failure_reason\": \"Director ordered kill: cross-domain 14B inference deemed valueless by Reviewer. Only FewNERD 14B inference retained.\", \"conclusion\": \"killed\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-20T14:49:09.529266+00:00\"}]}, \"server\": \"autodl-5090-c\", \"gpu\": \"cuda:1\", \"spec\": {\"server\": \"autodl-5090-c\", \"gpu\": \"cuda:1\", \"pid\": 278145, \"model_name\": \"Qwen2.5-14B-Instruct (base)\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/conll2003/\", \"data_count\": 3453, \"seed\": 42, \"command\": \"python -u code/run_mvp_pilot.py --model_path Qwen/Qwen2.5-14B-Instruct --data_dir data/conll2003/ --dataset conll2003 --n_samples 8 --temperature 1.0 --seed 42 --enforce_eager --output_dir output/14b_base_inference/conll2003_n1/\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/logs/14b_conll_inference.log\"}, \"completed_at\": \"2026-05-21T04:57:40.651Z\"}, \"exp_scierc_t12_s456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T03:24:04.240Z\", \"updated_at\": \"2026-05-21T04:25:04.160Z\", \"hypothesis\": \"SciERC temperature ablation (T=1.2, seed=456): third seed for SciERC T-ablation 3-seed statistical power. N=8, Qwen3-8B-FT.\", \"parent\": \"exp_scierc_t12_s123\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/scierc_t12_s456/\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/logs/scierc_t12_s456.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T04:24:22.602Z\", \"metrics\": {\"greedy_f1\": 0.663, \"oracle_f1\": 0.782, \"rho_SJ_full\": 0.42, \"rho_FK_full\": 0.32, \"rho_advantage\": 0.099, \"oracle_headroom\": 0.119, \"degeneracy_pct\": 14.1, \"verdict\": \"PASS\"}}, \"exp_scierc_t08_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T03:11:56.854Z\", \"updated_at\": \"2026-05-21T04:25:01.025Z\", \"hypothesis\": \"SciERC temperature ablation (T=0.8, seed=123): second seed for SciERC T-ablation replication. N=8, Qwen3-8B-FT.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data/ --dataset scierc --subtask ner --n_samples 8 --temperature 0.8 --seed 123 --collect_logprobs --output_dir output/scierc_t08_s123/\", \"server\": \"autodl-5090-c\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/scierc/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 123, \"gpu\": \"cuda:1\", \"pid\": 269240, \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/logs/scierc_t08_s123.log\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/scierc_t08_s123/\", \"checkpoint_source\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-scierc-merged-v2\", \"eval_data\": \"scierc test set (551 instances)\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T04:24:17.181Z\", \"metrics\": {\"greedy_f1\": 0.662, \"oracle_f1\": 0.773, \"rho_SJ_full\": 0.382, \"rho_FK_full\": 0.298, \"rho_advantage\": 0.084, \"oracle_headroom\": 0.11, \"degeneracy_pct\": 11.2, \"verdict\": \"MARGINAL\"}}, \"exp_scierc_t08_s456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T03:24:03.202Z\", \"updated_at\": \"2026-05-21T04:24:59.796Z\", \"hypothesis\": \"SciERC temperature ablation (T=0.8, seed=456): third seed for SciERC T-ablation 3-seed statistical power. N=8, Qwen3-8B-FT.\", \"parent\": \"exp_scierc_t08_s123\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/scierc_t08_s456/\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/logs/scierc_t08_s456.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T04:24:14.128Z\", \"metrics\": {\"greedy_f1\": 0.664, \"oracle_f1\": 0.769, \"rho_SJ_full\": 0.362, \"rho_FK_full\": 0.244, \"rho_advantage\": 0.118, \"oracle_headroom\": 0.105, \"degeneracy_pct\": 11.9, \"verdict\": \"MARGINAL\"}}, \"exp_scierc_t05_s456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T03:24:01.834Z\", \"updated_at\": \"2026-05-21T04:24:58.182Z\", \"hypothesis\": \"SciERC temperature ablation (T=0.5, seed=456): third seed for SciERC T-ablation 3-seed statistical power. N=8, Qwen3-8B-FT.\", \"parent\": \"exp_scierc_t05_s123\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/scierc_t05_s456/\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/logs/scierc_t05_s456.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T04:24:11.475Z\", \"metrics\": {\"greedy_f1\": 0.663, \"oracle_f1\": 0.746, \"rho_SJ_full\": 0.326, \"rho_FK_full\": 0.272, \"rho_advantage\": 0.054, \"oracle_headroom\": 0.083, \"degeneracy_pct\": 10.3, \"verdict\": \"MARGINAL\"}}, \"exp_scierc_t12_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T03:11:53.869Z\", \"updated_at\": \"2026-05-21T04:24:56.285Z\", \"hypothesis\": \"SciERC temperature ablation (T=1.2, seed=123): second seed for SciERC T-ablation replication. N=8, Qwen3-8B-FT.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data/ --dataset scierc --subtask ner --n_samples 8 --temperature 1.2 --seed 123 --collect_logprobs --output_dir output/scierc_t12_s123/\", \"server\": \"autodl-5090-b\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/scierc/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 123, \"gpu\": \"cuda:3\", \"pid\": 305838, \"tmux_session\": \"scierc_t12_s123\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/logs/scierc_t12_s123.log\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/scierc_t12_s123/\", \"checkpoint_source\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-scierc-merged-v2\", \"eval_data\": \"scierc test set (551 instances)\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T04:24:08.764Z\", \"metrics\": {\"greedy_f1\": 0.664, \"oracle_f1\": 0.788, \"rho_SJ_full\": 0.346, \"rho_FK_full\": 0.223, \"rho_advantage\": 0.124, \"oracle_headroom\": 0.124, \"degeneracy_pct\": 13.9, \"verdict\": \"MARGINAL\"}}, \"exp_scierc_t05_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T03:11:49.272Z\", \"updated_at\": \"2026-05-21T04:24:54.884Z\", \"hypothesis\": \"SciERC temperature ablation (T=0.5, seed=123): second seed for SciERC T-ablation replication. N=8, Qwen3-8B-FT.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data/ --dataset scierc --subtask ner --n_samples 8 --temperature 0.5 --seed 123 --collect_logprobs --output_dir output/scierc_t05_s123/\", \"server\": \"autodl-5090-b\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/scierc/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 123, \"gpu\": \"cuda:2\", \"pid\": 305836, \"tmux_session\": \"scierc_t05_s123\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/logs/scierc_t05_s123.log\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/scierc_t05_s123/\", \"checkpoint_source\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-scierc-merged-v2\", \"eval_data\": \"scierc test set (551 instances)\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T04:24:06.127Z\", \"metrics\": {\"greedy_f1\": 0.665, \"oracle_f1\": 0.743, \"rho_SJ_full\": 0.322, \"rho_FK_full\": 0.295, \"rho_advantage\": 0.026, \"oracle_headroom\": 0.078, \"degeneracy_pct\": 10, \"verdict\": \"MARGINAL\"}}, \"exp_fewnerd_t08_s456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T00:47:48.690Z\", \"updated_at\": \"2026-05-21T04:24:53.510Z\", \"hypothesis\": \"FewNERD T-ablation seed=456 (T=0.8): third seed for T=0.8 sweet-spot, providing 3-seed statistical power for the key operating point. With seeds 42/123/456, can compute confidence intervals on rho_SJ and degeneracy_rate for the recommended T=0.8 setting.\", \"parent\": \"exp_fewnerd_t08_s42\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-fewnerd-exp021-merged --data_dir data/fewnerd/ --dataset fewnerd --subtask ner --n_samples 8 --temperature 0.8 --seed 456 --collect_logprobs --output_dir output/fewnerd_t08_s456/\", \"server\": \"autodl-5090-b\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/fewnerd/test.json\", \"data_count\": 37648, \"model_name\": \"qwen3-8b-fewnerd-exp021-merged (Qwen3-8B-FT)\", \"seed\": 456, \"gpu\": \"cuda:3\", \"tmux_session\": \"fewnerd_t08_s456\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/logs/fewnerd_t08_s456.log\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/fewnerd_t08_s456/\", \"pid\": 297409, \"checkpoint_source\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-fewnerd-exp021-merged\", \"eval_data\": \"fewnerd test set (37648 instances)\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T04:24:03.444Z\", \"metrics\": {\"greedy_f1\": 0.788, \"oracle_f1\": 0.877, \"rho_SJ_full\": 0.328, \"rho_FK_full\": 0.202, \"rho_advantage\": 0.126, \"oracle_headroom\": 0.088, \"degeneracy_pct\": 16.3, \"verdict\": \"MARGINAL\"}}, \"exp_fewnerd_t12_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T00:47:46.558Z\", \"updated_at\": \"2026-05-21T04:24:52.149Z\", \"hypothesis\": \"FewNERD T-ablation seed=123 replication (T=1.2): second seed for statistical power on T=1.2 negative result (over-diversification, 28.2% degeneracy, lowest rho_SJ=0.136 in seed=42). Confirms T=1.2 is consistently suboptimal for SC diagnostics on FewNERD.\", \"parent\": \"exp_fewnerd_t12_s42\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-fewnerd-exp021-merged --data_dir data/fewnerd/ --dataset fewnerd --subtask ner --n_samples 8 --temperature 1.2 --seed 123 --collect_logprobs --output_dir output/fewnerd_t12_s123/\", \"server\": \"autodl-5090-b\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/fewnerd/test.json\", \"data_count\": 37648, \"model_name\": \"qwen3-8b-fewnerd-exp021-merged (Qwen3-8B-FT)\", \"seed\": 123, \"gpu\": \"cuda:2\", \"tmux_session\": \"fewnerd_t12_s123\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/logs/fewnerd_t12_s123.log\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/fewnerd_t12_s123/\", \"pid\": 297143, \"checkpoint_source\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-fewnerd-exp021-merged\", \"eval_data\": \"fewnerd test set (37648 instances)\"}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-21T04:24:00.722Z\", \"metrics\": {\"greedy_f1\": 0.789, \"oracle_f1\": 0.887, \"rho_SJ_full\": 0.285, \"rho_FK_full\": 0.163, \"rho_advantage\": 0.122, \"oracle_headroom\": 0.098, \"degeneracy_pct\": 24.7, \"verdict\": \"FAIL\"}}, \"exp_fewnerd_t08_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T00:47:44.136Z\", \"updated_at\": \"2026-05-21T04:24:50.244Z\", \"hypothesis\": \"FewNERD T-ablation seed=123 replication (T=0.8): second seed for statistical power on T=0.8 sweet-spot hypothesis (best rho_advantage=0.102 SJ over Fleiss, balanced oracle headroom=8.66% in seed=42). Tests robustness of T=0.8 as optimal operating point for SC diagnostic.\", \"parent\": \"exp_fewnerd_t08_s42\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-fewnerd-exp021-merged --data_dir data/fewnerd/ --dataset fewnerd --subtask ner --n_samples 8 --temperature 0.8 --seed 123 --collect_logprobs --output_dir output/fewnerd_t08_s123/\", \"server\": \"autodl-5090-b\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/fewnerd/test.json\", \"data_count\": 37648, \"model_name\": \"qwen3-8b-fewnerd-exp021-merged (Qwen3-8B-FT)\", \"seed\": 123, \"gpu\": \"cuda:1\", \"tmux_session\": \"fewnerd_t08_s123\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/logs/fewnerd_t08_s123.log\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/fewnerd_t08_s123/\", \"pid\": 296880, \"checkpoint_source\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-fewnerd-exp021-merged\", \"eval_data\": \"fewnerd test set (37648 instances)\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T04:23:57.853Z\", \"metrics\": {\"greedy_f1\": 0.789, \"oracle_f1\": 0.884, \"rho_SJ_full\": 0.336, \"rho_FK_full\": 0.221, \"rho_advantage\": 0.116, \"oracle_headroom\": 0.095, \"degeneracy_pct\": 16.7, \"verdict\": \"MARGINAL\"}}, \"exp_fewnerd_t05_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T00:47:41.794Z\", \"updated_at\": \"2026-05-21T04:24:48.794Z\", \"hypothesis\": \"FewNERD T-ablation seed=123 replication (T=0.5): second seed for statistical power on T=0.5 findings (highest rho_SJ=0.267, lowest oracle headroom=6.85% in seed=42). Confirms whether the diagnostic correlation ranking T=0.5>T=0.8>T=1.2 is stable across seeds or driven by seed-specific variance.\", \"parent\": \"exp_fewnerd_t05_s42\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-fewnerd-exp021-merged --data_dir data/fewnerd/ --dataset fewnerd --subtask ner --n_samples 8 --temperature 0.5 --seed 123 --collect_logprobs --output_dir output/fewnerd_t05_s123/\", \"server\": \"autodl-5090-b\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/fewnerd/test.json\", \"data_count\": 37648, \"model_name\": \"qwen3-8b-fewnerd-exp021-merged (Qwen3-8B-FT)\", \"seed\": 123, \"gpu\": \"cuda:0\", \"tmux_session\": \"fewnerd_t05_s123\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/logs/fewnerd_t05_s123.log\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/fewnerd_t05_s123/\", \"pid\": 296744, \"checkpoint_source\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-fewnerd-exp021-merged\", \"eval_data\": \"fewnerd test set (37648 instances)\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T04:23:54.964Z\", \"metrics\": {\"greedy_f1\": 0.789, \"oracle_f1\": 0.864, \"rho_SJ_full\": 0.35, \"rho_FK_full\": 0.295, \"rho_advantage\": 0.055, \"oracle_headroom\": 0.075, \"degeneracy_pct\": 13.5, \"verdict\": \"MARGINAL\"}}, \"exp_32b_inference_fewnerd\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T00:21:12.060Z\", \"updated_at\": \"2026-05-21T04:24:47.338Z\", \"hypothesis\": \"32B fine-tuned model (Qwen2.5-32B-Instruct QLoRA, best checkpoint-32000) FewNERD inference with N=8 SC sampling. Scaling from 8B→32B should improve per-sample quality and strengthen SC diagnostic correlation (Fleiss kappa / Soft-Jaccard vs F1). Comparison baseline: Qwen3-8B-FT FewNERD results.\", \"parent\": \"exp_qwen25_32b_fewnerd\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_32b_fewnerd_n8_s42/\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/logs/inference_32b_fewnerd_n8_s42.log\", \"command\": \"python code/run_mvp_pilot.py --model_path checkpoints/qwen25-32b-fewnerd-merged --data_dir data/fewnerd --dataset fewnerd --n_samples 8 --temperature 1.0 --seed 42 --output_dir output/exp_32b_fewnerd_n8_s42 --tensor_parallel 4 --collect_logprobs\", \"server\": \"autodl-5090\", \"model_name\": \"qwen25-32b-fewnerd-merged\", \"seed\": 42, \"data_path\": \"data/fewnerd\", \"data_count\": 301184}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T04:23:52.252Z\", \"metrics\": {\"greedy_f1\": 0.8, \"oracle_f1\": 0.879, \"rho_SJ_full\": 0.32, \"rho_FK_full\": 0.242, \"rho_advantage\": 0.078, \"fleiss_kappa_mean\": 0.533, \"soft_jaccard_mean\": 0.802, \"oracle_headroom\": 0.079, \"verdict\": \"MARGINAL\"}}, \"exp_hidden_state_probe_fulldata\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T04:13:17.554Z\", \"updated_at\": \"2026-05-21T04:13:53.843Z\", \"hypothesis\": \"Hidden states of fine-tuned Qwen3-8B encode entity quality information that a linear probe can detect with AUROC significantly above chance, even under GroupKFold (no instance leakage). CoNLL probe should exceed MV baseline (0.87).\", \"spec\": {\"command\": \"extract_fulldata_hidden_states.py + groupkfold_probe_fulldata.py\", \"server\": \"autodl-5090-b (fewnerd), autodl-5090-c (conll, scierc)\", \"data_path\": \"output/entity_probe_fulldata/\", \"data_count\": \"CoNLL 850inst/14777ent, FewNERD 1698inst/41096ent, SciERC 539inst/13188ent\", \"model_name\": \"Qwen3-8B fine-tuned\", \"seed\": \"42,123,456\"}, \"log_path\": \"artifacts/exp_hidden_state_probe_fulldata/data/groupkfold_probe_fulldata_results.json\", \"checkpoint_path\": \"output/entity_probe_fulldata/ on autodl-5090-b and autodl-5090-c\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T04:13:53.843Z\"}, \"exp_hidden_state_probe\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T02:07:00.977Z\", \"updated_at\": \"2026-05-21T03:21:54.284Z\", \"hypothesis\": \"Entity quality information (in_gold vs not) is encoded in the fine-tuned model's last-layer hidden states at entity token positions. If probe AUROC ≈ MV AUROC (0.87), the signal exists in representation but ESJ prompt-based reading (AUROC=0.51) fails to access it — a prompt interface failure. If probe AUROC ≈ 0.51, the information is genuinely absent from single-sample representations.\", \"spec\": {\"command\": \"python code/hidden_state_probe.py --dataset {fewnerd,conll} --max_instances 500\", \"server\": \"autodl-5090-c\", \"data_path\": \"output/{exp_tlow_fewnerd_t05_s42,exp_conll_t08_seed42}/samples.jsonl\", \"data_count\": 1000, \"model_name\": \"Qwen3-8B-FT (per-dataset checkpoints)\", \"seed\": 42, \"gpu\": \"cuda:2 (fewnerd), cuda:3 (conll)\", \"pid\": 261583, \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/logs/probe_extract_{fewnerd,conll}.log\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/entity_probe_auroc/\"}, \"metrics\": {\"entity_level_stratifiedkfold_auroc\": {\"conll\": 0.9796, \"fewnerd\": 0.9872, \"scierc\": 0.9766}, \"groupkfold_auroc_corrected\": {\"conll\": 0.8849, \"fewnerd\": 0.6513, \"scierc\": 0.6344}, \"groupkfold_delta\": {\"conll\": -0.0947, \"fewnerd\": -0.3359, \"scierc\": -0.3422}, \"groupkfold_probe_above_mv\": {\"conll\": true, \"fewnerd\": false, \"scierc\": false}, \"baselines\": {\"mv_agreement_auroc\": 0.87, \"esj_prompt_auroc\": 0.51}, \"note\": \"GroupKFold fixes instance-level leakage. Only conll retains probe > MV after correction.\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T02:11:40.936Z\", \"notes\": \"Probe AUROC far exceeds both baselines: FewNERD 0.987, CoNLL 0.980 vs MV 0.87 vs ESJ 0.51. The model's last-layer hidden states at entity token positions encode correctness information at very high fidelity — even higher than what multi-sample voting captures. This is strong evidence for a prompt interface failure: the model knows which entities are correct but cannot express this through prompting (ESJ). LogisticRegression with 5-fold CV × 3 seeds. SciERC extraction not run (no matching 8B samples data available).\"}, \"exp_conll_t10_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T02:32:32.990Z\", \"updated_at\": \"2026-05-21T02:44:20.817Z\", \"hypothesis\": \"CoNLL T=1.0 baseline (seed=42): fills the gap in the temperature ablation matrix (T=0.5/0.8/1.2 already complete with 3 seeds). T=1.0 is the default sampling temperature and should show intermediate behavior between T=0.8 (sweet spot) and T=1.2 (over-diversification), completing the temperature sweep for CoNLL.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-conll2003-merged --data_dir data/conll2003/ --dataset conll2003 --n_samples 8 --temperature 1.0 --seed 42 --collect_logprobs --output_dir output/exp_conll_t10_seed42/\", \"server\": \"autodl-5090-c\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/conll2003/test.json\", \"data_count\": 3453, \"model_name\": \"qwen3-8b-conll2003-merged\", \"seed\": 42, \"gpu\": \"cuda:3\", \"pid\": 265554, \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/logs/conll_t10_seed42.log\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_conll_t10_seed42/\", \"checkpoint_source\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-conll2003-merged\", \"eval_data\": \"conll2003 test set (3453 instances)\"}, \"metrics\": {\"greedy_f1\": 0.9077, \"oracle_f1\": 0.9503, \"oracle_headroom\": 0.0426, \"rho_SJ_full\": 0.4249, \"rho_kappa_full\": 0.4037, \"rho_SJ_cond\": 0.4154, \"rho_kappa_cond\": 0.3793, \"rho_advantage\": 0.0212, \"fleiss_kappa_mean\": 0.772, \"soft_jaccard_mean\": 0.895, \"sample_f1_mean\": 0.871, \"sample_f1_pct_zero\": 7.53, \"verdict\": \"PASS\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T02:44:20.817Z\"}, \"exp_scierc_probe\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T02:32:25.557Z\", \"updated_at\": \"2026-05-21T02:41:37.846Z\", \"hypothesis\": \"SciERC hidden state probe: test if linear classifier on last-layer hidden states can predict entity quality (match vs non-match against gold). If AUROC ≈ 0.98 (consistent with FewNERD=0.987, CoNLL=0.980), confirms entity quality info is universally encoded in representations across datasets, and prompt-based self-judgment (ESJ AUROC=0.51) fails to access this information.\", \"spec\": {\"command\": \"Step 1: CUDA_VISIBLE_DEVICES=1 python -u code/run_mvp_pilot.py --dataset scierc --n_samples 8 --temperature 0.8; Step 2: python code/hidden_state_probe.py --dataset scierc --gpu 1\", \"server\": \"autodl-5090-c\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/scierc/processed_data/test.json\", \"data_count\": 551, \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 42, \"gpu\": \"cuda:1\", \"pid\": 264061, \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/logs/scierc_8b_inference.log\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/entity_probe_auroc/\", \"checkpoint_source\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-scierc-merged-v2\", \"eval_data\": \"scierc test set (551 instances)\"}, \"metrics\": {\"scierc_auroc_mean\": 0.9766, \"scierc_auroc_std\": 0.0011, \"scierc_auroc_seeds\": [0.9771, 0.9751, 0.9775], \"n_entities\": 12933, \"positive_rate\": 0.654, \"interpretation\": \"HIGH — info in representation, prompt interface fails\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T02:41:37.846Z\"}, \"exp_multi_model_correlation\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T02:04:21.487Z\", \"updated_at\": \"2026-05-21T02:05:04.778Z\", \"hypothesis\": \"Cross-family models (Qwen vs LLaMA) have lower per-instance error correlation than same-family models, explaining why cross-model ensemble improves F1 by +0.42pp\", \"spec\": {\"command\": \"python3 code/multi_model_error_correlation.py --output_dir output/multi_model_correlation/\", \"server\": \"autodl-5090\", \"data_path\": \"output/*/samples.jsonl\", \"data_count\": 9004, \"model_name\": \"Qwen3-8B-FT + LLaMA-3.1-8B-Instruct\", \"seed\": 42, \"checkpoint_source\": \"N/A\", \"checkpoint_path\": \"N/A\", \"log_path\": \"output/multi_model_correlation/error_correlation_report.json\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T02:05:04.778Z\"}, \"exp_conll_t12_s456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T00:43:52.368Z\", \"updated_at\": \"2026-05-21T01:59:40.017Z\", \"hypothesis\": \"CoNLL temperature ablation (T=1.2, seed=456): third seed complementing seed=42+123 for 3-seed statistical power. N=8, Qwen3-8B-FT, CoNLL-2003.\", \"parent\": \"exp_conll_t12_s123\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --n_samples 8 --temperature 1.2 --seed 456 --output_dir output/exp_conll_t12_seed456\", \"server\": \"autodl-5090-c\", \"data_path\": \"data/conll2003\", \"data_count\": 3453, \"model_name\": \"qwen3-8b-conll2003-merged\", \"seed\": 456, \"pid\": 255217, \"gpu\": \"cuda:3\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_conll_t12_seed456.log\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_conll_t12_seed456/\", \"checkpoint_source\": \"checkpoints/qwen3-8b-conll2003-merged\", \"eval_data\": \"data/conll2003\"}, \"conclusion\": \"success\", \"metrics\": {\"greedy_f1\": 0.9071, \"oracle_f1\": 0.9452, \"oracle_headroom\": 0.0381, \"fleiss_kappa_mean\": 0.7005, \"soft_jaccard_mean\": 0.8513, \"rho_SJ_F1_full\": 0.4553, \"rho_SJ_F1_conditional\": 0.4259, \"degeneracy_rate_pct\": 8.34, \"rho_advantage\": 0.0265, \"verdict\": \"PASS\"}, \"completed_at\": \"2026-05-21T01:59:40.017Z\"}, \"exp_conll_t08_s456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T00:43:51.393Z\", \"updated_at\": \"2026-05-21T01:59:37.027Z\", \"hypothesis\": \"CoNLL temperature ablation (T=0.8, seed=456): third seed complementing seed=42+123 for 3-seed statistical power. N=8, Qwen3-8B-FT, CoNLL-2003.\", \"parent\": \"exp_conll_t08_s123\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --n_samples 8 --temperature 0.8 --seed 456 --output_dir output/exp_conll_t08_seed456\", \"server\": \"autodl-5090-c\", \"data_path\": \"data/conll2003\", \"data_count\": 3453, \"model_name\": \"qwen3-8b-conll2003-merged\", \"seed\": 456, \"pid\": 254524, \"gpu\": \"cuda:2\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_conll_t08_seed456.log\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_conll_t08_seed456/\", \"checkpoint_source\": \"checkpoints/qwen3-8b-conll2003-merged\", \"eval_data\": \"data/conll2003\"}, \"conclusion\": \"success\", \"metrics\": {\"greedy_f1\": 0.9064, \"oracle_f1\": 0.9407, \"oracle_headroom\": 0.0343, \"fleiss_kappa_mean\": 0.8229, \"soft_jaccard_mean\": 0.9233, \"rho_SJ_F1_full\": 0.4877, \"rho_SJ_F1_conditional\": 0.4756, \"degeneracy_rate_pct\": 6.29, \"rho_advantage\": 0.0058, \"verdict\": \"PASS\"}, \"completed_at\": \"2026-05-21T01:59:37.027Z\"}, \"exp_conll_t05_s456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-21T00:43:49.873Z\", \"updated_at\": \"2026-05-21T01:59:34.389Z\", \"hypothesis\": \"CoNLL temperature ablation (T=0.5, seed=456): third seed complementing seed=42+123 for 3-seed statistical power. N=8, Qwen3-8B-FT, CoNLL-2003.\", \"parent\": \"exp_conll_t05_s123\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --n_samples 8 --temperature 0.5 --seed 456 --output_dir output/exp_conll_t05_seed456\", \"server\": \"autodl-5090-c\", \"data_path\": \"data/conll2003\", \"data_count\": 3453, \"model_name\": \"qwen3-8b-conll2003-merged\", \"seed\": 456, \"pid\": 253823, \"gpu\": \"cuda:1\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_conll_t05_seed456.log\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_conll_t05_seed456/\", \"checkpoint_source\": \"checkpoints/qwen3-8b-conll2003-merged\", \"eval_data\": \"data/conll2003\"}, \"conclusion\": \"success\", \"metrics\": {\"greedy_f1\": 0.9075, \"oracle_f1\": 0.9338, \"oracle_headroom\": 0.0263, \"fleiss_kappa_mean\": 0.8885, \"soft_jaccard_mean\": 0.9551, \"rho_SJ_F1_full\": 0.4549, \"rho_SJ_F1_conditional\": 0.469, \"degeneracy_rate_pct\": 5.62, \"rho_advantage\": 0.0044, \"verdict\": \"PASS\"}, \"completed_at\": \"2026-05-21T01:59:34.389Z\"}, \"exp_fewnerd_t05_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T22:41:05.687Z\", \"updated_at\": \"2026-05-21T00:47:06.206Z\", \"hypothesis\": \"FewNERD temperature ablation (T=0.5): test how lower temperature affects degeneracy rate and SC diagnostic cascade on FewNERD, complementing SciERC T-ablation data. N=8, Qwen3-8B-FT, seed=42. Lower T should reduce sampling diversity, potentially increasing degeneracy while improving per-sample quality.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-fewnerd-exp021-merged --data_dir data/fewnerd/ --dataset fewnerd --subtask ner --n_samples 8 --temperature 0.5 --seed 42 --collect_logprobs --output_dir output/fewnerd_t05_s42/\", \"server\": \"autodl-5090-b\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/fewnerd/test.json\", \"data_count\": 37648, \"model_name\": \"qwen3-8b-fewnerd-exp021-merged (Qwen3-8B-FT)\", \"seed\": 42, \"gpu\": \"cuda:0\", \"tmux_session\": \"fewnerd_t05\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/logs/fewnerd_t05_s42.log\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/fewnerd_t05_s42/\"}, \"metrics\": {\"greedy_f1\": 0.7884, \"oracle_f1\": 0.8569, \"oracle_headroom\": 0.0685, \"sample_f1_mean\": 0.7154, \"degeneracy_rate\": 0.146, \"fleiss_kappa_mean\": 0.6332, \"soft_jaccard_mean\": 0.8653, \"rho_SJ_F1_full\": 0.2667, \"rho_SJ_F1_conditional\": 0.2988, \"rho_fleiss_F1_full\": 0.2231, \"rho_fleiss_F1_conditional\": 0.2338, \"rho_logprob_F1_full\": 0.3558, \"rho_logprob_F1_conditional\": 0.3025, \"structural_beats_surface\": true, \"rho_advantage\": 0.0435}, \"conclusion\": \"success\", \"notes\": \"T=0.5 on FewNERD has highest absolute rho_SJ=0.267 (full), 0.299 (conditional) among T-ablation, but lowest oracle headroom (6.85%) meaning SC oracle gain is smallest. Lowest degeneracy (14.6%), highest sample quality (0.715). SJ advantage over Fleiss only 0.044 because Fleiss also high (0.223). Logprob baseline dominates at this T (rho=0.356). Tradeoff: low T maximizes diagnostic correlation but minimizes room for SC to help.\", \"completed_at\": \"2026-05-21T00:47:06.206Z\"}, \"exp_fewnerd_t08_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T22:41:07.634Z\", \"updated_at\": \"2026-05-21T00:45:13.333Z\", \"hypothesis\": \"FewNERD temperature ablation (T=0.8): test how moderate-low temperature affects degeneracy rate and SC diagnostic cascade on FewNERD, complementing SciERC T-ablation data. N=8, Qwen3-8B-FT, seed=42. T=0.8 is a sweet-spot candidate balancing diversity and quality.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-fewnerd-exp021-merged --data_dir data/fewnerd/ --dataset fewnerd --subtask ner --n_samples 8 --temperature 0.8 --seed 42 --collect_logprobs --output_dir output/fewnerd_t08_s42/\", \"server\": \"autodl-5090-b\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/fewnerd/test.json\", \"data_count\": 37648, \"model_name\": \"qwen3-8b-fewnerd-exp021-merged (Qwen3-8B-FT)\", \"seed\": 42, \"gpu\": \"cuda:1\", \"tmux_session\": \"fewnerd_t08\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/logs/fewnerd_t08_s42.log\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/fewnerd_t08_s42/\"}, \"metrics\": {\"greedy_f1\": 0.7884, \"oracle_f1\": 0.875, \"oracle_headroom\": 0.0866, \"sample_f1_mean\": 0.6622, \"degeneracy_rate\": 0.1897, \"fleiss_kappa_mean\": 0.4439, \"soft_jaccard_mean\": 0.7572, \"rho_SJ_F1_full\": 0.2062, \"rho_SJ_F1_conditional\": 0.2248, \"rho_fleiss_F1_full\": 0.1038, \"rho_logprob_F1_full\": 0.2323, \"rho_logprob_F1_conditional\": 0.1984, \"structural_beats_surface\": true, \"rho_advantage\": 0.1024}, \"conclusion\": \"success\", \"notes\": \"T=0.8 confirms sweet-spot hypothesis on FewNERD: best rho_SJ_F1=0.206 (full), 0.225 (conditional), lowest degeneracy (19%), highest sample quality (mean F1=0.662). SJ beats Fleiss by 0.102 rho advantage. Logprob baseline rho=0.232 (full) surprisingly high — SJ diagnostic matches logprob informativeness at this T. Verdict FAIL only because MVP single-subtask threshold not met, but T=0.8 is clearly the best operating point.\", \"completed_at\": \"2026-05-21T00:45:13.333Z\"}, \"exp_fewnerd_t12_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T22:41:09.018Z\", \"updated_at\": \"2026-05-21T00:44:30.280Z\", \"hypothesis\": \"FewNERD temperature ablation (T=1.2): test how higher temperature affects degeneracy rate and SC diagnostic cascade on FewNERD, complementing SciERC T-ablation data. N=8, Qwen3-8B-FT, seed=42. Higher T should increase diversity and reduce degeneracy but degrade per-sample quality.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-fewnerd-exp021-merged --data_dir data/fewnerd/ --dataset fewnerd --subtask ner --n_samples 8 --temperature 1.2 --seed 42 --collect_logprobs --output_dir output/fewnerd_t12_s42/\", \"server\": \"autodl-5090-b\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/fewnerd/test.json\", \"data_count\": 37648, \"model_name\": \"qwen3-8b-fewnerd-exp021-merged (Qwen3-8B-FT)\", \"seed\": 42, \"gpu\": \"cuda:2\", \"tmux_session\": \"fewnerd_t12\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/logs/fewnerd_t12_s42.log\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/fewnerd_t12_s42/\"}, \"metrics\": {\"greedy_f1\": 0.7888, \"oracle_f1\": 0.875, \"oracle_headroom\": 0.0862, \"sample_f1_mean\": 0.5524, \"degeneracy_rate\": 0.2818, \"fleiss_kappa_mean\": 0.283, \"soft_jaccard_mean\": 0.5894, \"rho_SJ_F1_full\": 0.136, \"rho_SJ_F1_conditional\": 0.2125, \"rho_fleiss_F1_full\": 0.0605, \"rho_logprob_F1_conditional\": 0.1912, \"structural_beats_surface\": true, \"rho_advantage\": 0.0755}, \"conclusion\": \"negative\", \"notes\": \"T=1.2 on FewNERD: high oracle headroom (8.6%) but poor SC diagnostic correlation (rho_SJ=0.136 full, 0.213 conditional). High degeneracy (28.2% zero-F1 samples) and low per-sample quality (mean F1=0.55) indicate T=1.2 over-diversifies. Structural metric (SJ) still beats surface (Fleiss) by 0.075 rho advantage. Verdict: FAIL (MVP threshold not met on single subtask).\", \"completed_at\": \"2026-05-21T00:44:30.280Z\"}, \"exp_conll_t12_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T23:41:59.173Z\", \"updated_at\": \"2026-05-21T00:39:01.179Z\", \"hypothesis\": \"CoNLL temperature ablation (T=1.2, seed=123): additional seed for statistical power, complementing seed=42 results. N=8, Qwen3-8B-FT, CoNLL-2003.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --n_samples 8 --temperature 1.2 --seed 123 --output_dir output/exp_conll_t12_seed123\", \"server\": \"autodl-5090-c\", \"data_path\": \"data/conll2003\", \"data_count\": 3453, \"model_name\": \"qwen3-8b-conll2003-merged\", \"seed\": 123}, \"metrics\": {\"greedy_f1\": 0.9072, \"oracle_f1\": 0.955, \"oracle_headroom\": 0.0478, \"fleiss_kappa_mean\": 0.6675, \"soft_jaccard_mean\": 0.8295, \"rho_fleiss_full\": 0.4086, \"rho_softjaccard_full\": 0.4352, \"rho_fleiss_cond\": 0.3516, \"rho_softjaccard_cond\": 0.3915, \"structural_beats_surface\": true, \"rho_advantage\": 0.0266, \"sample_f1_mean\": 0.8438, \"sample_f1_pct_zero\": 9.1, \"verdict\": \"PASS\"}, \"log_path\": \"output/exp_conll_t12_seed123.log\", \"checkpoint_path\": \"output/exp_conll_t12_seed123/\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T00:39:01.179Z\"}, \"exp_conll_t08_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T23:41:58.169Z\", \"updated_at\": \"2026-05-21T00:38:55.958Z\", \"hypothesis\": \"CoNLL temperature ablation (T=0.8, seed=123): additional seed for statistical power, complementing seed=42 results. N=8, Qwen3-8B-FT, CoNLL-2003.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --n_samples 8 --temperature 0.8 --seed 123 --output_dir output/exp_conll_t08_seed123\", \"server\": \"autodl-5090-c\", \"data_path\": \"data/conll2003\", \"data_count\": 3453, \"model_name\": \"qwen3-8b-conll2003-merged\", \"seed\": 123}, \"metrics\": {\"greedy_f1\": 0.9068, \"oracle_f1\": 0.9466, \"oracle_headroom\": 0.0398, \"fleiss_kappa_mean\": 0.8246, \"soft_jaccard_mean\": 0.9201, \"rho_fleiss_full\": 0.4718, \"rho_softjaccard_full\": 0.4846, \"rho_fleiss_cond\": 0.4444, \"rho_softjaccard_cond\": 0.462, \"structural_beats_surface\": true, \"rho_advantage\": 0.0128, \"sample_f1_mean\": 0.8897, \"sample_f1_pct_zero\": 6.1, \"verdict\": \"PASS\"}, \"log_path\": \"output/exp_conll_t08_seed123.log\", \"checkpoint_path\": \"output/exp_conll_t08_seed123/\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T00:38:55.958Z\"}, \"exp_conll_t05_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T23:41:56.932Z\", \"updated_at\": \"2026-05-21T00:38:53.249Z\", \"hypothesis\": \"CoNLL temperature ablation (T=0.5, seed=123): additional seed for statistical power, complementing seed=42 results. N=8, Qwen3-8B-FT, CoNLL-2003.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --n_samples 8 --temperature 0.5 --seed 123 --output_dir output/exp_conll_t05_seed123\", \"server\": \"autodl-5090-c\", \"data_path\": \"data/conll2003\", \"data_count\": 3453, \"model_name\": \"qwen3-8b-conll2003-merged\", \"seed\": 123}, \"metrics\": {\"greedy_f1\": 0.9073, \"oracle_f1\": 0.9351, \"oracle_headroom\": 0.0278, \"fleiss_kappa_mean\": 0.8941, \"soft_jaccard_mean\": 0.954, \"rho_fleiss_full\": 0.4529, \"rho_softjaccard_full\": 0.4602, \"rho_fleiss_cond\": 0.4493, \"rho_softjaccard_cond\": 0.4566, \"structural_beats_surface\": true, \"rho_advantage\": 0.0072, \"sample_f1_mean\": 0.901, \"sample_f1_pct_zero\": 5.5, \"verdict\": \"PASS\"}, \"log_path\": \"output/exp_conll_t05_seed123.log\", \"checkpoint_path\": \"output/exp_conll_t05_seed123/\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T00:38:53.249Z\"}, \"exp_qwen25_32b_fewnerd\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T06:19:25.428Z\", \"updated_at\": \"2026-05-21T00:18:28.126Z\", \"hypothesis\": \"Qwen2.5-32B-Instruct QLoRA fine-tuning on FewNERD: scaling model from 8B→32B should improve per-sample NER quality, enabling stronger SC diagnostic signals. LoRA r=32, alpha=64, target all attention+FFN projections, 5 epochs, 4×RTX 5090.\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:0,cuda:1,cuda:2,cuda:3\", \"account\": \"root\", \"reproduce\": {\"server\": \"autodl-5090\", \"gpu\": \"cuda:0,cuda:1,cuda:2,cuda:3\", \"started_at\": \"2026-05-19T06:47:41.246Z\"}, \"notes\": \"2026-05-19 11:36 UTC: step 2177/41180 (5.3%), loss 0.0663, ~2.44s/it, ETA ~26h. checkpoint-2000 saved. PID 804438, 4×5090 87-100% util.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0,1,2,3 FORCE_TORCHRUN=1 NNODES=1 NPROC_PER_NODE=4 llamafactory-cli train /root/autodl-tmp/struct_self_consist_ie/train_config_qwen25_32b_fewnerd_s42.yaml\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/fewnerd/llmfactory_train.json\", \"data_count\": 131767, \"model_name\": \"Qwen2.5-32B-Instruct\", \"seed\": 42, \"method\": \"QLoRA-4bit-nf4 (rank=32, alpha=64, target=all)\", \"output_dir\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen25-32b-fewnerd-qlora-s42\", \"config_path\": \"/root/autodl-tmp/struct_self_consist_ie/train_config_qwen25_32b_fewnerd_s42.yaml\", \"epochs\": 5, \"effective_batch_size\": 16, \"lr\": \"2e-4\", \"gpu_ids\": [\"cuda:0\", \"cuda:1\", \"cuda:2\", \"cuda:3\"], \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/logs/train_qwen25_32b_fewnerd_s42.log\", \"pid\": 804438, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen25-32b-fewnerd-qlora-s42/checkpoint-32000\"}, \"metrics\": {\"total_steps\": 41180, \"epochs\": 5, \"best_checkpoint\": \"checkpoint-32000\", \"best_eval_loss\": 0.0334, \"final_train_loss\": 0.005, \"final_eval_loss\": 0.0412, \"initial_loss\": 0.559, \"training_time_hours\": 38.5, \"lora_rank\": 32, \"lora_alpha\": 64, \"note\": \"Overfitting after epoch ~3.9; best eval_loss at step 32000 (epoch 3.89). Post-training load-best-model OOM (rank2) but all checkpoints saved correctly.\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-21T00:18:28.126Z\"}, \"exp_conll_t_ablation_t12\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T22:41:01.169Z\", \"updated_at\": \"2026-05-20T23:35:53.499Z\", \"hypothesis\": \"CoNLL temperature ablation (T=1.2): test how temperature affects degeneracy rate and SC diagnostic cascade on CoNLL-2003, complementing SciERC and FewNERD T-ablation data to form 3-dataset temperature-degeneracy frontier. N=8, Qwen3-8B-FT, seed=42.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python run_mvp_pilot.py --model_path checkpoints/qwen3-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 8 --temperature 1.2 --seed 42 --output_dir output/exp_conll_t12_seed42\", \"server\": \"autodl-5090-c\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/conll2003\", \"data_count\": 2756, \"model_name\": \"qwen3-8b-conll2003-merged\", \"seed\": 42, \"pid\": 243594, \"gpu\": \"cuda:3\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_conll_t12_seed42.log\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_conll_t12_seed42/\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T23:35:37.422Z\", \"metrics\": {\"greedy_f1\": 0.9071, \"oracle_f1\": 0.9514, \"oracle_headroom\": 0.0443, \"fleiss_kappa\": 0.7092, \"softjaccard_rho_full\": 0.4071, \"softjaccard_rho_cond\": 0.3936, \"fleiss_rho_full\": 0.3786, \"fleiss_rho_cond\": 0.349, \"degen_pct\": 9.22, \"sample_f1_mean\": 0.8452, \"verdict\": \"PASS\"}}, \"exp_conll_t_ablation_t08\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T22:40:59.474Z\", \"updated_at\": \"2026-05-20T23:35:51.189Z\", \"hypothesis\": \"CoNLL temperature ablation (T=0.8): test how temperature affects degeneracy rate and SC diagnostic cascade on CoNLL-2003, complementing SciERC and FewNERD T-ablation data to form 3-dataset temperature-degeneracy frontier. N=8, Qwen3-8B-FT, seed=42.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python run_mvp_pilot.py --model_path checkpoints/qwen3-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 8 --temperature 0.8 --seed 42 --output_dir output/exp_conll_t08_seed42\", \"server\": \"autodl-5090-c\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/conll2003\", \"data_count\": 2756, \"model_name\": \"qwen3-8b-conll2003-merged\", \"seed\": 42, \"pid\": 242682, \"gpu\": \"cuda:2\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_conll_t08_seed42.log\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_conll_t08_seed42/\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T23:35:34.984Z\", \"metrics\": {\"greedy_f1\": 0.9069, \"oracle_f1\": 0.9464, \"oracle_headroom\": 0.0396, \"fleiss_kappa\": 0.8199, \"softjaccard_rho_full\": 0.4498, \"softjaccard_rho_cond\": 0.4373, \"fleiss_rho_full\": 0.4352, \"fleiss_rho_cond\": 0.4128, \"degen_pct\": 6.57, \"sample_f1_mean\": 0.8854, \"verdict\": \"PASS\"}}, \"exp_conll_t_ablation_t05\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T22:40:58.068Z\", \"updated_at\": \"2026-05-20T23:35:48.803Z\", \"hypothesis\": \"CoNLL temperature ablation (T=0.5): test how temperature affects degeneracy rate and SC diagnostic cascade on CoNLL-2003, complementing SciERC and FewNERD T-ablation data to form 3-dataset temperature-degeneracy frontier. N=8, Qwen3-8B-FT, seed=42.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python run_mvp_pilot.py --model_path checkpoints/qwen3-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 8 --temperature 0.5 --seed 42 --output_dir output/exp_conll_t05_seed42\", \"server\": \"autodl-5090-c\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/conll2003\", \"data_count\": 2756, \"model_name\": \"qwen3-8b-conll2003-merged\", \"seed\": 42, \"pid\": 242197, \"gpu\": \"cuda:1\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_conll_t05_seed42.log\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_conll_t05_seed42/\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T23:35:32.179Z\", \"metrics\": {\"greedy_f1\": 0.9077, \"oracle_f1\": 0.9372, \"oracle_headroom\": 0.0296, \"fleiss_kappa\": 0.8948, \"softjaccard_rho_full\": 0.4312, \"softjaccard_rho_cond\": 0.4544, \"fleiss_rho_cond\": 0.4519, \"degen_pct\": 5.64, \"sample_f1_mean\": 0.8993, \"verdict\": \"PASS\"}}, \"exp_conll_t05_s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T22:41:11.361Z\", \"updated_at\": \"2026-05-20T23:35:46.566Z\", \"hypothesis\": \"CoNLL T=0.5 temperature point: test low temperature on CoNLL2003 to extend cross-dataset T-ablation evidence beyond SciERC and FewNERD. N=8, Qwen3-8B-FT-CoNLL, seed=42. Complements SciERC T-ablation for 3-dataset degeneracy-temperature comparison.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python -u code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-conll2003-merged --data_dir data/conll2003/ --dataset conll2003 --subtask ner --n_samples 8 --temperature 0.5 --seed 42 --collect_logprobs --output_dir output/conll_t05_s42/\", \"server\": \"autodl-5090-b\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/conll2003/test.json\", \"data_count\": 3453, \"model_name\": \"qwen3-8b-conll2003-merged (Qwen3-8B-FT-CoNLL)\", \"seed\": 42, \"gpu\": \"cuda:3\", \"tmux_session\": \"conll_t05\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/logs/conll_t05_s42.log\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/conll_t05_s42/\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T23:35:29.767Z\", \"metrics\": {\"greedy_f1\": 0.9083, \"oracle_f1\": 0.9376, \"oracle_headroom\": 0.0294, \"fleiss_kappa\": 0.8958, \"softjaccard_rho_full\": 0.4228, \"softjaccard_rho_cond\": 0.4476, \"fleiss_rho_cond\": 0.4443, \"logprob_rho_cond\": 0.3562, \"logprob_auroc_cond\": 0.8102, \"degen_pct\": 5.64, \"sample_f1_mean\": 0.8994, \"verdict\": \"PASS\"}}, \"exp_spider_sc_pilot\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T18:41:49.560Z\", \"updated_at\": \"2026-05-20T22:37:08.907Z\", \"hypothesis\": \"SC diagnostic cascade (degeneracy, agreement-correctness correlation, failure mode classification F1-F4) validated on NER structured generation will also manifest in SQL structured generation with GPT-5.5 on Spider-dev (200 examples, N=8, T=1.0), demonstrating cross-task universality. Key adaptation: uses execution-result equivalence (not SQL text) for agreement/degeneracy, since semantically equivalent SQL can have different surface forms.\", \"spec\": {\"command\": \"python run_spider_sc.py --n_samples 8 --temperature 1.0 --seed 42 --output_dir ./results --test_api\", \"server\": \"local (CPU+API)\", \"gpu\": \"cuda:2\", \"data_path\": \"xlangai/spider (HF) + spider databases (sqlite)\", \"data_count\": 200, \"model_name\": \"openai/gpt-5.5 via http://47.94.22.126/v1\", \"seed\": 42, \"bugfixes\": [\"F1-F4 failure modes aligned with NER cascade (F2=low_agreement, F3=high_agreement_wrong)\", \"Degeneracy detection uses execution results instead of SQL text comparison\", \"Converted from vLLM to API-based (CPU+API experiment)\"], \"pid\": 1504303, \"failure_reason\": \"402 API balance exhausted at 125/200 instances\", \"partial_results\": \"125/200 instances completed before API died\", \"log_path\": \"local spider_sc results dir\", \"checkpoint_path\": \"local spider_sc results dir\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T22:05:14.976Z\", \"metrics\": {\"n_instances\": 196, \"n_target\": 200, \"n_skipped\": 2, \"n_samples\": 8, \"temperature\": 1, \"model\": \"gpt-5.5\", \"greedy_acc\": 0.7653, \"mv_acc\": 0.7704, \"oracle_acc\": 0.8061, \"mv_gain_pp\": 0.51, \"degeneracy_rate\": 0.8724, \"spearman_rho\": 0.5501, \"spearman_p\": 6.77e-17, \"kendall_tau\": 0.5259, \"F1_degeneracy_rate\": 0.872, \"F2_low_agreement_rate\": 0, \"F3_high_agree_wrong_rate\": 0.082, \"F4_selection_gap_rate\": 0, \"sc_success_rate\": 0.046, \"nondegen_n\": 25, \"nondegen_greedy_acc\": 0.32, \"nondegen_mv_acc\": 0.36, \"nondegen_oracle_acc\": 0.64, \"nondegen_spearman_rho\": 0.13}, \"notes\": \"Data quality verified: all 196 instances generated AFTER F2/F3 bugfix (code modified 20:47:22, checkpoint started 20:47:52). Zero mismatch between embedded and recomputed failure modes. F1-F4 distribution: F1=87.2%, F2=0%, F3=8.2%, F4=0%, OK=4.6%. F2=0 means SQL has no low-agreement zone (either degenerate or high consensus). Paper-ready. Note: F4 is dead code in SQL context (greedy_correct AND NOT mv_correct never occurs). Cross-task threshold note: SQL uses agreement<0.5 for F2/F3 split, RE uses kappa<0.3.\"}, \"exp_fewrel_re_sc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T21:13:10.685Z\", \"updated_at\": \"2026-05-20T22:08:51.973Z\", \"hypothesis\": \"SC consensus construction improves RE micro-F1 over greedy decoding on FewRel (16 relation types, Wikipedia domain), extending cross-task universality evidence beyond SciERC and DocRED\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python3 -u experiments/fewrel_re_sc/run_fewrel_re_sc.py --model-path /root/autodl-tmp/.hf_cache/Qwen2.5-7B-Instruct --data data/fewrel_re_test_instances.jsonl --output-dir output/fewrel_re_sc --n-samples 8 --temperature 1.0\", \"server\": \"autodl-5090-c\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/fewrel_re_test_instances.jsonl\", \"data_count\": 256, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": 42, \"pid\": 236752, \"gpu\": \"cuda:1\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/fewrel_re_sc/run.log\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/fewrel_re_sc/\"}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-20T21:20:24.473Z\", \"metrics\": {\"greedy_micro_f1\": 0.0751, \"construction_micro_f1\": 0.0881, \"majority_vote_f1_mean\": 0.0591, \"oracle_f1_mean\": 0.1768, \"fleiss_kappa_mean\": 0.1506, \"soft_jaccard_mean\": 0.3918, \"degeneracy_rate\": 0.0586, \"bootstrap_p_value\": 0.7572, \"failure_modes\": {\"F2_low_agreement\": \"75.8%\", \"F3_high_agreement_low_quality\": \"15.2%\", \"F1_degeneracy\": \"5.9%\", \"none\": \"2.3%\", \"F4_lp_quality_gap\": \"0.8%\"}}, \"notes\": \"Reviewer confirmed: same pattern as SciERC/DocRED RE (low F1, high F2). Micro_f1 and mean_f1 directions diverge: construction micro_f1 > greedy (0.0881 vs 0.0751) but mean_f1 < greedy. Paper uses micro_f1 per D204. Marked negative because bootstrap p=0.7572 (not significant).\"}, \"exp_a2_humaneval_sc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T18:15:14.615Z\", \"updated_at\": \"2026-05-20T22:05:17.728Z\", \"hypothesis\": \"SC failure modes (degeneracy, false agreement) generalize from NER to code generation despite deterministic verification — majority voting on HumanEval will show limited gains over greedy when degeneracy is high, paralleling NER findings.\", \"spec\": {\"command\": \"python -u run_humaneval_sc.py --n_samples 8 --temperature 1.0 --seed 42 --output_dir ./results\", \"server\": \"autodl-5090\", \"pid\": 967645, \"data_path\": \"openai/openai_humaneval (HuggingFace)\", \"data_count\": 164, \"model_name\": \"openai/gpt-5.5\", \"seed\": 42, \"fix_note\": \"v2 rerun: fixed extract_code() strip() -> rstrip() + auto-indent for function body. Previous run had 0/164 pass due to IndentationError.\", \"failure_reason\": \"402 API balance exhausted after indent bugfix. Fix verified (23/23 greedy pass, 179/184 sample pass) but only 24/164 tasks completed before API died.\", \"log_path\": \"autodl-5090 humaneval results dir\", \"checkpoint_path\": \"autodl-5090 humaneval results dir\"}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-20T22:05:17.728Z\"}, \"exp_b_frontier_sc_fewnerd\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T18:15:19.266Z\", \"updated_at\": \"2026-05-20T22:05:12.564Z\", \"hypothesis\": \"The correlation-selection gap in structured self-consistency (where agreement correlates with accuracy but majority voting fails to improve over greedy) persists even with frontier models (GPT-5.5, Claude Opus 4.6), indicating it is a fundamental structural limitation of entity-level majority voting rather than a model capability issue.\", \"spec\": {\"command\": \"nohup .venv/bin/python -u run_frontier_sc.py --from-hf --n-instances 200 --n-samples 8 --temperature 1.0 --seed 42 --output-dir ./output > frontier_sc.log 2>&1 &\", \"server\": \"local\", \"data_path\": \"HuggingFace DFKI-SLT/few-nerd supervised test split\", \"data_count\": 200, \"model_name\": \"openai/gpt-5.5 + anthropic/claude-opus-4.6 (via OpenRouter)\", \"seed\": 42, \"pid\": 1509955, \"code_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/experiments/frontier_sc/run_frontier_sc.py\", \"log_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/experiments/frontier_sc/frontier_sc.log\", \"checkpoint_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/experiments/frontier_sc/output/\", \"failure_reason\": \"entity_set() TypeError - compute_instance_metrics passed full parsed dict instead of entities list\"}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-20T22:05:12.564Z\"}, \"exp_docred_re_sc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T19:32:26.943Z\", \"updated_at\": \"2026-05-20T21:07:53.274Z\", \"hypothesis\": \"SC diagnostic cascade (degeneracy, correlation-selection gap, F1-F4 failure modes) generalizes from NER to document-level RE on DocRED, with Qwen2.5-7B-Instruct showing similar failure patterns as seen in SciERC NER and SciERC RE.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python3 experiments/docred_re/run_docred_re_sc.py --model-path /root/autodl-tmp/.hf_cache/Qwen2.5-7B-Instruct --data data/docred_re_instances.jsonl --schema data/docred_schema.json --output-dir output/docred_re_sc\", \"server\": \"autodl-5090-c\", \"data_path\": \"data/docred_re_instances.jsonl\", \"data_count\": 200, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/docred_re_sc/\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/docred_re_sc/run.log\"}, \"server\": \"autodl-5090-c\", \"gpu\": \"cuda:3\", \"metrics\": {\"greedy_f1_mean\": 0.0284, \"construction_f1_mean\": 0.0338, \"majority_vote_f1_mean\": 0.0263, \"oracle_f1_mean\": 0.0999, \"greedy_micro_f1\": 0.0297, \"construction_micro_f1\": 0.0323, \"fleiss_kappa\": -0.0253, \"soft_jaccard\": 0.2907, \"degeneracy_rate\": 0.035, \"n_instances\": 200, \"failure_modes\": {\"F1_degeneracy\": \"3.5%\", \"F2_low_agreement\": \"94.5%\", \"F3_high_agreement_low_quality\": \"2.0%\"}, \"bootstrap_diff\": 0.0053, \"bootstrap_ci_95\": [-0.004, 0.0149], \"bootstrap_p_value\": 0.1276, \"nondegen_construction_greedy_diff\": 0.0055}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T21:07:53.274Z\"}, \"exp_a3_ace05_re\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T18:15:17.438Z\", \"updated_at\": \"2026-05-20T21:03:51.597Z\", \"hypothesis\": \"Cross-task universality: SC diagnostic cascade on ACE05 Relation Extraction. Closest extension to NER—same structured prediction paradigm, different output structure (entity pairs + relation types). Qwen2.5-7B-Instruct few-shot prompt. If correlation-selection gap exists for RE, the framework covers multiple IE sub-tasks.\", \"spec\": {\"hypothesis\": \"The SC diagnostic cascade (degeneracy, agreement, LP-quality gap) generalizes from NER to Relation Extraction, with failure modes F1-F4 exhibiting analogous distributions on RE because both are span-based structured prediction tasks sharing the same underlying model uncertainty structure.\", \"model_name\": \"Qwen2.5-7B-Instruct\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/re_test_instances.jsonl\", \"data_count\": 397, \"server\": \"autodl-5090-c\", \"seed\": 42, \"command\": \"CUDA_VISIBLE_DEVICES=1 python3 experiments/re_sc/run_re_sc.py --model-path /root/autodl-tmp/.hf_cache/Qwen2.5-7B-Instruct --data data/re_test_instances.jsonl --output-dir output/re_sc --n-samples 8 --temperature 1.0\", \"method\": \"SC diagnostic cascade on RE (few-shot, N=8, T=1.0, XGrammar constrained decoding)\", \"parent\": null, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/re_sc/\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/logs/re_sc.log\"}, \"server\": \"autodl-5090-c\", \"gpu\": \"cuda:1\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T21:03:46.444Z\", \"metrics\": {\"greedy_f1_mean\": 0.0777, \"construction_f1_mean\": 0.0599, \"majority_vote_f1_mean\": 0.0491, \"oracle_f1_mean\": 0.1567, \"greedy_micro_f1\": 0.0688, \"construction_micro_f1\": 0.0602, \"fleiss_kappa\": -0.0021, \"soft_jaccard\": 0.2425, \"degeneracy_rate\": 0.0076, \"n_instances\": 397, \"failure_modes\": {\"F1_degeneracy\": \"0.8%\", \"F2_low_agreement\": \"93.5%\", \"F3_high_agreement_low_quality\": \"4.5%\", \"none\": \"1.3%\"}, \"bootstrap_diff\": -0.0178, \"bootstrap_ci_95\": [-0.0334, -0.0024], \"bootstrap_p_value\": 0.989}}, \"exp_b1_scd_fewnerd_curriculum_q\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T11:17:38.760Z\", \"updated_at\": \"2026-05-20T20:15:55.005Z\", \"hypothesis\": \"Q variant SCD with curriculum ordering: use B2 entity verifier confidence to stratify pseudo-labels (conf>0.8→Round1, 0.5-0.8→Round2, conf<0.5→discard). Curriculum by verifier confidence improves SCD convergence and final greedy F1 vs standard flat SCD on FewNERD.\", \"spec\": {\"command\": \"llamafactory-cli train train_config_scd_fewnerd_fallback_s43.yaml\", \"server\": \"autodl-5090-b\", \"gpu_ids\": [1], \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/scd_fewnerd_theta2n_s42.jsonl\", \"data_count\": 32565, \"model_name\": \"Qwen3-8B-FT\", \"seed\": 43, \"note\": \"Fallback standard SCD seed=43 (Q-variant deferred per D189)\"}, \"reproduce\": {\"finished_at\": \"2026-05-20T19:01:52.441Z\"}, \"failure_reason\": \"RETRACTED: cron false positive — training completed successfully (4706/4706 steps, loss=0.023). Original: process dead 5× with no sentinel/W&B\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-20T19:01:57.213Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-20T19:02:06.612980+00:00\"}]}, \"notes\": \"M046: SCD metric artifact confirmed. Original +3.84pp was comparing instance-avg F1 baseline (0.7482, gold-filtered n=32565) to micro-F1 post-SCD (0.7866, full n=37648). Unified micro-F1: pre=0.7886 → post=0.7866, Δ=-0.20pp. Instance-avg: pre=0.7719 → post=0.7809, Δ=+0.90pp (much smaller than claimed). SCD does not constitute paper contribution.\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-fewnerd-scd-fallback-lora/\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/logs/exp_b1_scd_fewnerd_fallback.log\", \"metrics\": {\"eval_greedy_f1\": 0.7866, \"eval_greedy_precision\": 0.7663, \"eval_greedy_recall\": 0.808, \"eval_instance_avg_f1\": 0.7809, \"delta_vs_baseline\": 0.0386, \"baseline_greedy_f1\": 0.748, \"total_tp\": 78252, \"total_fp\": 23869, \"total_fn\": 18590, \"n_instances\": 37648}}, \"exp_b1_scd_fewnerd_standard\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T11:17:37.804Z\", \"updated_at\": \"2026-05-20T20:15:51.708Z\", \"hypothesis\": \"Standard Self-Consistency Distillation on FewNERD: fine-tune Qwen3-8B-FT with theta2n construction pseudo-labels (32,565 instances) mixed 1:1 with gold data. Greedy F1 after SCD should approach N=8 construction F1 (0.764 vs current 0.748). Transductive setting: pseudo-labels from test set SC outputs.\", \"spec\": {\"command\": \"llamafactory-cli train train_config_scd_fewnerd_s42.yaml\", \"server\": \"autodl-5090-b\", \"gpu_ids\": [0], \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/scd_fewnerd_theta2n_s42.jsonl\", \"data_count\": 32565, \"model_name\": \"Qwen3-8B-FT\", \"seed\": 42, \"pid\": 207109, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-fewnerd-scd-lora/\"}, \"reproduce\": {\"finished_at\": \"2026-05-20T19:13:25.333Z\"}, \"failure_reason\": \"RETRACTED: cron false positive — training completed successfully (4706/4706 steps, train_loss=0.023, eval_loss=0.0329). Original: process dead 5× with no sentinel/W&B\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-20T19:13:26.395Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-20T19:13:35.804759+00:00\"}]}, \"notes\": \"M046: SCD metric artifact confirmed. Original +3.3pp was comparing instance-avg F1 baseline (0.7482, gold-filtered n=32565) to micro-F1 post-SCD (0.7813, full n=37648). Unified micro-F1: pre=0.7886 → post=0.7813, Δ=-0.73pp. SCD does not improve NER performance.\", \"metrics\": {\"train_loss\": 0.023, \"eval_loss\": 0.0329, \"steps\": 4706, \"epochs\": 2, \"train_runtime_hours\": 7.14}}, \"exp_b1_scd_threshold_ablation\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T11:17:42.163Z\", \"updated_at\": \"2026-05-20T20:00:50.883Z\", \"hypothesis\": \"Construction threshold sweep for SCD pseudo-label generation on FewNERD: θ∈{1/N, 2/N, 3/N, 0.5}. Higher θ = more conservative pseudo-labels (higher precision, lower recall). Optimal θ balances pseudo-label quality vs quantity for SCD training effectiveness.\", \"spec\": {\"command\": \"llamafactory-cli train train_config_scd_fewnerd_theta3_s42.yaml\", \"server\": \"autodl-5090-b\", \"gpu_ids\": [3], \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/scd_fewnerd_theta3n_s42.jsonl\", \"data_count\": 32565, \"model_name\": \"Qwen3-8B-FT\", \"seed\": 42, \"note\": \"theta=3/N ablation\"}, \"reproduce\": {\"finished_at\": \"2026-05-20T20:00:47.950Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-20T20:00:50.883Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-20T20:00:57.832218+00:00\"}]}}, \"exp_tlow_fewnerd_inference\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:40:52.432Z\", \"updated_at\": \"2026-05-20T19:39:38.613Z\", \"hypothesis\": \"Lower temperature (T=0.5) sampling on FewNERD produces less diverse but higher-quality samples that, when combined with T=1.0 samples in heterogeneous-temperature selection, improve self-consistency-based quality estimation compared to single-temperature baselines.\", \"server\": \"autodl-5090-c\", \"gpu\": \"cuda:2\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python code/run_mvp_pilot.py --model_path checkpoints/qwen25-7b-fewnerd-merged --data_dir data/fewnerd/ --dataset fewnerd --subtask ner --n_samples 8 --temperature 0.5 --seed 42 --collect_logprobs --output_dir output/exp_tlow_fewnerd_t05_s42/\", \"server\": \"autodl-5090-c\", \"gpu\": \"cuda:2\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/fewnerd/test.json\", \"data_count\": 37648, \"model_name\": \"qwen25-7b-fewnerd-merged\", \"seed\": 42, \"pid\": 221493, \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_tlow_fewnerd_t05_s42.log\"}, \"checkpoint_path\": \"output/exp_tlow_fewnerd_t05_s42/\", \"log_path\": \"output/exp_tlow_fewnerd_t05_s42.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T19:39:38.613Z\"}, \"exp_asb_adaptive_budget\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T15:37:33.233Z\", \"updated_at\": \"2026-05-20T19:37:37.412Z\", \"hypothesis\": \"Instance-level features from cheap N=2 subsamples (degeneracy, agreement, entity count, logprob variance, text length) can predict optimal per-instance sample count, enabling adaptive budget allocation that outperforms uniform allocation under a fixed total budget.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python /root/autodl-tmp/struct_self_consist_ie/artifacts/experiments/asb/run_asb.py --data_paths /root/autodl-tmp/struct_self_consist_ie/output/exp_021_inference/samples.jsonl,/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t10_seed42/samples.jsonl,/root/autodl-tmp/struct_self_consist_ie/output/exp_002_conll_n16/samples.jsonl --dataset_names FewNERD,SciERC,CoNLL --output_dir /root/autodl-tmp/struct_self_consist_ie/output/exp_asb_adaptive_budget/ --seed 42\\\"\", \"server\": \"autodl-5090\", \"gpu\": [], \"pid\": \"943151\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_asb_adaptive_budget.log\", \"submitted_at\": \"2026-05-20T17:55:06.477Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"output/exp_asb_adaptive_budget/asb_results.json\", \"wall_clock_seconds\": 215.1, \"gpu_hours\": 0.0}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-20T17:58:41.592Z\", \"metrics\": {\"v2_fixed\": true, \"fixes\": [\"removed greedy_f1 feature (data leak via gold labels)\", \"max_n-aware adaptive_allocation\", \"K-fold downstream eval (no train=test leak)\", \"micro-F1 (global TP/FP/FN)\"], \"fewnerd\": {\"uniform_n8_micro_f1\": 0.7842, \"adaptive_micro_f1\": 0.7842, \"delta_adaptive_uniform\": 0, \"oracle_micro_f1\": 0.7842, \"greedy_micro_f1\": 0.7911, \"best_predictor\": \"MLP\", \"n_instances\": 32565, \"max_n\": 8, \"note\": \"max_n=budget=8, no room for reallocation\"}, \"scierc\": {\"uniform_n8_micro_f1\": 0.6657, \"adaptive_micro_f1\": 0.6657, \"delta_adaptive_uniform\": 0, \"oracle_micro_f1\": 0.6657, \"greedy_micro_f1\": 0.6649, \"best_predictor\": \"MLP\", \"n_instances\": 529, \"max_n\": 8, \"note\": \"max_n=budget=8, no room for reallocation\"}, \"conll\": {\"uniform_n8_micro_f1\": 0.9128, \"adaptive_micro_f1\": 0.9095, \"delta_adaptive_uniform\": -0.0033, \"oracle_micro_f1\": 0.9139, \"delta_oracle_uniform\": 0.0012, \"greedy_micro_f1\": 0.9124, \"adaptive_fold_mean\": 0.91, \"adaptive_fold_std\": 0.0044, \"best_predictor\": \"RandomForest\", \"n_instances\": 2756, \"max_n\": 16}, \"top_features\": [\"degen_rate_n2\", \"agreement_n2\", \"entity_count_n2\"], \"key_finding\": \"After fixing data leak + train=test leak + max_n bug, adaptive allocation shows no improvement over uniform. FewNERD/SciERC have max_n=budget=8 (no reallocation possible). CoNLL (max_n=16) shows slight negative delta (-0.0033). Previous positive results were artifacts of methodological bugs.\"}}, \"exp_e_theta_adaptive\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T15:31:49.319Z\", \"updated_at\": \"2026-05-20T19:24:52.991Z\", \"hypothesis\": \"Threshold-Adaptive SC: N inverse scaling (D191) proves θ choice determines scaling direction. A learned θ predictor (input: degeneracy_level, lp_variance, N, dataset, model) can select per-instance optimal θ, closing the gap between fixed θ=0.5 and oracle θ. Leave-one-config-out CV on 16 configs from existing N=8/16 data. 5 variants: LogReg/MLP × feature subsets + degeneracy-only baseline.\", \"spec\": {\"checkpoint_path\": \"N/A (CPU predictor, no model checkpoint)\", \"log_path\": \"N/A (inline evaluation)\"}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-20T19:24:52.991Z\"}, \"exp_cross_model_consistency\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T09:30:47.928Z\", \"updated_at\": \"2026-05-20T19:03:33.786Z\", \"hypothesis\": \"Cross-model entity construction (mixing Qwen and LLaMA outputs) produces higher-quality entity spans than single-model construction, because inter-model agreement filters out model-specific hallucinations while preserving genuinely supported entities.\", \"metrics\": {\"scierc\": {\"n_filtered\": 529, \"qwen_greedy_f1\": 0.6453, \"llama_greedy_f1\": 0.646, \"degeneracy\": {\"pure_qwen\": 0.1323, \"pure_llama\": 0.1777, \"mixed\": 0.0964}, \"construction_f1\": {\"pure_qwen_uniform\": 0.6449, \"pure_qwen_vc\": 0.6413, \"pure_llama_uniform\": 0.6545, \"pure_llama_vc\": 0.649, \"mixed_uniform\": 0.6625, \"mixed_vc\": 0.6591}, \"bootstrap\": {\"mixed_uni_vs_pure_qwen_uni\": {\"delta_pp\": 1.77, \"p\": 0.0102, \"ci\": [0.27, 3.28]}, \"mixed_vc_vs_pure_qwen_vc\": {\"delta_pp\": 1.77, \"p\": 0.0093, \"ci\": [0.33, 3.27]}, \"mixed_uni_vs_pure_llama_uni\": {\"delta_pp\": 0.81, \"p\": 0.1304, \"ci\": [-0.59, 2.25]}, \"mixed_vc_vs_pure_llama_vc\": {\"delta_pp\": 1.01, \"p\": 0.0702, \"ci\": [-0.32, 2.38]}}}, \"fewnerd\": {\"n_filtered\": 32565, \"qwen_greedy_f1\": 0.7478, \"llama_greedy_f1\": 0.7841, \"degeneracy\": {\"pure_qwen\": 0.1004, \"pure_llama\": 0.2336, \"mixed\": 0.1158}, \"construction_f1\": {\"pure_qwen_uniform\": 0.7499, \"pure_qwen_vc\": 0.7448, \"pure_llama_uniform\": 0.7873, \"pure_llama_vc\": 0.7869, \"mixed_uniform\": 0.7916, \"mixed_vc\": 0.7898}, \"bootstrap\": {\"mixed_uni_vs_pure_qwen_uni\": {\"delta_pp\": 4.17, \"p\": 0, \"ci\": [3.92, 4.4]}, \"mixed_vc_vs_pure_qwen_vc\": {\"delta_pp\": 4.5, \"p\": 0, \"ci\": [4.25, 4.75]}, \"mixed_uni_vs_pure_llama_uni\": {\"delta_pp\": 0.42, \"p\": 0, \"ci\": [0.27, 0.58]}, \"mixed_vc_vs_pure_llama_vc\": {\"delta_pp\": 0.29, \"p\": 0.0001, \"ci\": [0.13, 0.45]}}}}, \"conclusion\": \"success\", \"notes\": \"B5 cross-model consistency on SciERC + FewNERD. Mixed (4Q+4L) consistently outperforms pure-model construction on both datasets. FewNERD: mixed sig. beats pure LLaMA (+0.42pp uni p=0, +0.29pp VC p=0.0001) and pure Qwen (+4.17pp uni, +4.50pp VC, all p=0). SciERC: mixed sig. beats pure Qwen (+1.77pp uni p=0.01, +1.77pp VC p=0.009); vs pure LLaMA marginal (+0.81pp uni p=0.13, +1.01pp VC p=0.07). Cross-model diversity reduces degeneracy (FewNERD mixed 11.6% vs LLaMA 23.4%; SciERC mixed 9.6% vs LLaMA 17.8%). Note: SciERC greedy F1 lower than prior run (0.645 vs 0.748) — likely different eval scope (gold filter 529 vs prior 551).\", \"server\": \"autodl-5090-c\", \"gpu\": \"cuda:3\", \"spec\": {\"command\": \"bash code/run_cross_model.sh\", \"server\": \"autodl-5090\", \"data_path\": \"output/exp_026_t10_seed42/samples.jsonl + output/exp007_llama_inference/samples.jsonl + output/exp_021_inference/samples.jsonl + output/llama_fewnerd_s42/samples.jsonl\", \"data_count\": 76398, \"model_name\": \"cross-model (Qwen + LLaMA)\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_cross_model_consistency\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_cross_model_consistency\"}, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_cross_model_consistency\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_cross_model_consistency\", \"completed_at\": \"2026-05-20T19:03:33.786Z\"}, \"exp_backup3_distill_verifier\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:40:49.676Z\", \"updated_at\": \"2026-05-20T18:47:37.248Z\", \"hypothesis\": \"A supervised entity-level binary classifier (trained on 6 lightweight features: LP score, agreement ratio, degeneracy flag, span length, type consistency, N) can learn cross-dataset entity correctness signals that outperform unsupervised majority voting for entity construction, because the classifier can jointly weight multiple complementary signals that MV ignores.\", \"server\": \"autodl-5090-c\", \"gpu\": \"cuda:1\", \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python /root/autodl-tmp/struct_self_consist_ie/run_distill_verifier.py --seed 42\", \"server\": \"autodl-5090\", \"data_path\": {\"scierc\": \"output/exp_026_t10_seed42/samples.jsonl (551 inst, N=8)\", \"conll\": \"output/exp_002_conll_n16/samples.jsonl (3453 inst, N=16→subsample to 8)\", \"fewnerd\": \"output/exp_021_inference/samples.jsonl (37648 inst, N=8)\"}, \"data_count\": \"41652 instances total (~551+3453+37648)\", \"model_name\": \"LR+RF+MLP ensemble (sklearn)\", \"seed\": 42}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/distill_verifier/distill_verifier_results.json\", \"log_path\": \"/tmp/distill_verifier.log\", \"completed_at\": \"2026-05-20T18:47:30.099Z\", \"metrics\": {\"aggregate\": {\"LR\": {\"mean_auroc\": 0.8747, \"std_auroc\": 0.0563, \"mean_delta_f1\": -0.0014}, \"RF\": {\"mean_auroc\": 0.8752, \"std_auroc\": 0.0588, \"mean_delta_f1\": -0.0006}, \"MLP\": {\"mean_auroc\": 0.8744, \"std_auroc\": 0.0578, \"mean_delta_f1\": 0.0011}}, \"per_fold\": {\"scierc\": {\"LR\": {\"auroc\": 0.8009, \"std_mv_f1\": 0.6643, \"best_weighted_f1\": 0.6659, \"delta_f1\": 0.0016}, \"RF\": {\"auroc\": 0.7988, \"best_weighted_f1\": 0.6647, \"delta_f1\": 0.0004}, \"MLP\": {\"auroc\": 0.798, \"best_weighted_f1\": 0.6655, \"delta_f1\": 0.0012}}, \"conll\": {\"LR\": {\"auroc\": 0.9376, \"std_mv_f1\": 0.9074, \"best_weighted_f1\": 0.9049, \"delta_f1\": -0.0025}, \"RF\": {\"auroc\": 0.9419, \"best_weighted_f1\": 0.908, \"delta_f1\": 0.0006}, \"MLP\": {\"auroc\": 0.9379, \"best_weighted_f1\": 0.9075, \"delta_f1\": 0.0001}}, \"fewnerd\": {\"LR\": {\"auroc\": 0.8855, \"std_mv_f1\": 0.7819, \"best_weighted_f1\": 0.7786, \"delta_f1\": -0.0034}, \"RF\": {\"auroc\": 0.885, \"best_weighted_f1\": 0.7791, \"delta_f1\": -0.0029}, \"MLP\": {\"auroc\": 0.8872, \"best_weighted_f1\": 0.7839, \"delta_f1\": 0.002}}}, \"feature_importance_LR_scierc\": {\"agreement_ratio\": 1.651, \"lp_score\": 0.424, \"span_length\": -0.15, \"type_consistency\": 0.128, \"degeneracy_flag\": 0.043, \"n_samples\": 0}}}, \"exp_backup1_het_temp\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T17:09:31.094Z\", \"updated_at\": \"2026-05-20T18:15:37.574Z\", \"hypothesis\": \"Heterogeneous-Temperature Sampling: MRSC/LSC negative results prove entity-level correction cannot close the selection gap. F4 degeneracy analysis shows T=0.7 has ~62% degeneracy (too homogeneous) while T=1.0 has more diversity but noisier entities. Mixing samples from different temperatures (k from T_low + (8-k) from T_high) breaks temperature-specific degeneracy patterns: low-T samples provide precise entities, high-T samples provide diversity. Mixed-T N=8 pool should achieve lower degeneracy than pure T_low and higher construction F1 than pure T_high. Hypothesis source: entity-level methods (MRSC weighted re-prompting, LSC latent aggregation) both failed → pivot to sampling-level diversity improvement.\", \"parent\": \"exp_mrsc_multi_round\", \"spec\": {\"command\": \"bash /root/autodl-tmp/struct_self_consist_ie/run_het_temp_all.sh\", \"server\": \"autodl-5090\", \"gpu\": [], \"pid\": \"948780\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_backup1_het_temp.log\", \"submitted_at\": \"2026-05-20T18:13:20.732Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"N/A\", \"wall_clock_seconds\": 134.1, \"gpu_hours\": 0.0}, \"metrics\": {\"t08_vs_t10\": {\"seed42\": {\"pure_t_low_f1\": 0.6755, \"pure_t_high_f1\": 0.6643, \"best_mix\": \"5:3\", \"best_mix_f1\": 0.6708, \"delta_vs_low\": -0.0046, \"delta_vs_high\": 0.0066}, \"seed123\": {\"pure_t_low_f1\": 0.6659, \"pure_t_high_f1\": 0.6681, \"best_mix\": \"6:2\", \"best_mix_f1\": 0.6655, \"delta_vs_low\": -0.0004, \"delta_vs_high\": -0.0026}, \"seed456\": {\"pure_t_low_f1\": 0.6675, \"pure_t_high_f1\": 0.6663, \"best_mix\": \"4:4\", \"best_mix_f1\": 0.6654, \"delta_vs_low\": -0.002, \"delta_vs_high\": -0.0008}}, \"t05_vs_t10\": {\"seed42\": {\"pure_t_low_f1\": 0.663, \"pure_t_high_f1\": 0.6643, \"best_mix\": \"5:3\", \"best_mix_f1\": 0.6654, \"delta_vs_low\": 0.0024, \"delta_vs_high\": 0.0011}, \"seed123\": {\"pure_t_low_f1\": 0.6665, \"pure_t_high_f1\": 0.6681, \"best_mix\": \"2:6\", \"best_mix_f1\": 0.6671, \"delta_vs_low\": 0.0006, \"delta_vs_high\": -0.001}, \"seed456\": {\"pure_t_low_f1\": 0.6686, \"pure_t_high_f1\": 0.6663, \"best_mix\": \"4:4\", \"best_mix_f1\": 0.6682, \"delta_vs_low\": -0.0004, \"delta_vs_high\": 0.002}}, \"degeneracy\": {\"t05_mean\": 0.356, \"t08_mean\": 0.178, \"t10_mean\": 0.126}, \"max_delta_any_combo\": 0.0066}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-20T18:15:34.876Z\", \"notes\": \"Heterogeneous temperature mixing provides no consistent F1 improvement over pure single-temperature sampling on SciERC (551 instances, 3 seeds, 2 temp pairs). All F1 deltas within ±0.005, inconsistent direction across seeds. Mixing does reduce degeneracy (T=0.5: 35%→17%) but this doesn't translate to F1 gain. The pure T_low vs T_high F1 gap is already tiny (~0.001-0.01), leaving no room for mixing to exploit. Joins MRSC/LSC as evidence that sampling-level interventions cannot improve construction F1 when the bottleneck is not sample diversity.\"}, \"exp_esj_entity_self_judgment\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T15:31:53.721Z\", \"updated_at\": \"2026-05-20T17:44:33.778Z\", \"hypothesis\": \"Entity-Level Self-Judgment: F4 diagnostic proves 4/5 signals are instance-level only, LP is per-sample but compressed. ESJ provides true per-sample-per-entity signal via yes/no verification prompts. ESJ-weighted entity construction should outperform majority vote by leveraging entity-level confidence scores that structural signals cannot provide. Parent: exp_e2_mixture_of_signals (F4 LP-only diagnostic).\", \"parent\": \"exp_e2_mixture_of_signals\", \"server\": \"autodl-5090-c\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"autodl-5090-c\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-20T15:37:30.954Z\"}, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python run_esj.py --base_model_path checkpoints/qwen25-7b-fewnerd-merged --data_path output/fewnerd_7b/qwen25_7b_n8_seed42/samples.jsonl --output_dir output/exp_esj_entity_self_judgment --batch_size 8\", \"server\": \"autodl-5090-c\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/fewnerd_7b/qwen25_7b_n8_seed42/samples.jsonl\", \"data_count\": 37648, \"model_name\": \"qwen25-7b-fewnerd-merged\", \"seed\": 42, \"pid\": 218678, \"gpu\": \"cuda:1\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_esj_entity_self_judgment.log\", \"checkpoint_source\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen25-7b-fewnerd-merged\", \"eval_data\": \"/root/autodl-tmp/struct_self_consist_ie/output/fewnerd_7b/qwen25_7b_n8_seed42/samples.jsonl\", \"n_verification_prompts\": 153649, \"estimated_runtime_hours\": 2.5, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_esj_entity_self_judgment/\"}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-20T17:44:33.778Z\"}, \"exp_b3_prompted_diversity\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T11:12:51.750Z\", \"updated_at\": \"2026-05-20T17:40:45.878Z\", \"hypothesis\": \"Structurally different prompt templates (expert persona, descriptive types, recall-focused) generate more diverse N=8 samples than repeating a single template, improving entity construction F1 via broader coverage of the entity space.\", \"conclusion\": \"killed\", \"metrics\": {\"single_vc_weighted_f1\": 0.7723, \"multi_vc_weighted_f1\": 0.7311, \"delta_vc\": -0.0412, \"single_lp_weighted_f1\": 0.7665, \"multi_lp_weighted_f1\": 0.7308, \"delta_lp\": -0.0356, \"single_theta2n_f1\": 0.7618, \"multi_theta2n_f1\": 0.7269, \"delta_theta2n\": -0.0349, \"single_unique_entities\": 5.29, \"multi_unique_entities\": 4.06, \"within_template_jaccard\": 0.474, \"cross_template_jaccard\": 0.67, \"verdict\": \"Multi-template strictly worse. Templates converge to similar outputs; non-standard templates add noise, diluting construction signals.\"}, \"server\": \"autodl-5090-c\", \"gpu\": \"cuda:3\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python /root/autodl-tmp/struct_self_consist_ie/code/exp_b3_prompted_diversity.py --phase both --num_instances 3000 --seed 42\", \"server\": \"autodl-5090-c\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/fewnerd/test.json\", \"data_count\": 3000, \"model_name\": \"qwen3-8b-fewnerd-exp021-merged\", \"seed\": 42, \"checkpoint_path\": \"N/A\", \"log_path\": \"N/A\"}, \"completed_at\": \"2026-05-20T17:40:45.878Z\"}, \"exp_mrsc_multi_round\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T15:37:27.523Z\", \"updated_at\": \"2026-05-20T17:12:53.641Z\", \"hypothesis\": \"Multi-Round Iterative SC: N inverse scaling reveals disputed entities cause failures. Focused re-prompting on disputed entities (agreement < 0.6) with weighted aggregation (Round 2 weight=2) should reduce error rate on disputed entities without affecting non-disputed ones, closing part of the selection gap through iterative refinement rather than single-round aggregation.\", \"server\": \"autodl-5090-c\", \"gpu\": \"cuda:3\", \"account\": \"root\", \"reproduce\": {\"server\": \"autodl-5090-c\", \"gpu\": \"cuda:3\", \"started_at\": \"2026-05-20T15:39:10.190Z\"}, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python /root/autodl-tmp/struct_self_consist_ie/code/run_mrsc.py --base_model_path /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen25-7b-fewnerd-merged --data_path /root/autodl-tmp/struct_self_consist_ie/output/fewnerd_7b/qwen25_7b_n8_seed42/samples.jsonl --output_dir /root/autodl-tmp/struct_self_consist_ie/output/exp_mrsc_multi_round --batch_size 16\", \"server\": \"autodl-5090-c\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/fewnerd_7b/qwen25_7b_n8_seed42/samples.jsonl\", \"data_count\": 37648, \"model_name\": \"qwen25-7b-fewnerd-merged\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_mrsc_multi_round\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_mrsc_multi_round.log\"}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-20T17:12:53.641Z\"}, \"exp_lsc_latent_sc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T15:37:31.881Z\", \"updated_at\": \"2026-05-20T17:11:49.135Z\", \"hypothesis\": \"Latent Self-Consistency: F4 diagnostic proves LP is compressed (median range 0.041 nats). Hidden states contain richer per-sample information than scalar LP. Entity-level mean-pooled hidden state representations enable latent aggregation (centroid selection, latent confidence scoring, clustering) that bypasses LP compression and provides discriminative per-sample ranking unavailable from output-space signals.\", \"parent\": \"exp_e2_mixture_of_signals\", \"server\": \"autodl-5090-c\", \"gpu\": \"cuda:2\", \"account\": \"root\", \"reproduce\": {\"server\": \"autodl-5090-c\", \"gpu\": \"cuda:2\", \"started_at\": \"2026-05-20T15:39:11.609Z\"}, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python run_lsc.py --base_model_path qwen25-7b-fewnerd-merged --data_path fewnerd_7b/qwen25_7b_n8_seed42/samples.jsonl --max_instances 2000\", \"server\": \"autodl-5090-c\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/fewnerd_7b/qwen25_7b_n8_seed42/samples.jsonl\", \"data_count\": 2000, \"model_name\": \"qwen25-7b-fewnerd-merged\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen25-7b-fewnerd-merged\", \"eval_data\": \"FewNERD test (gold-filtered, n=2000)\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_lsc_latent_sc\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_lsc_latent_sc.log\"}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-20T16:51:53.120Z\", \"metrics\": {\"centroid_selection_f1\": 0.7593, \"lp_selection_f1\": 0.7845, \"latent_entity_conf_f1\": 0.8385, \"majority_vote_f1\": 0.8366, \"greedy_f1\": 0.7793, \"oracle_f1\": 0.8668, \"lp_vs_latent_rho\": 0.518, \"entity_match_rate\": 0.9945, \"n_instances\": 2000, \"runtime_s\": 507}}, \"exp_14b_inference_scierc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T14:36:25.505Z\", \"updated_at\": \"2026-05-20T15:11:54.487Z\", \"hypothesis\": \"14B Qwen2.5 inference on SciERC (N∈{1,2,4,8,16}): correlation-selection gap pattern should be consistent at 14B scale with intermediate degeneracy rates between 7B and 32B.\", \"reproduce\": {\"finished_at\": \"2026-05-20T14:48:16.272Z\"}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"conclusion\": \"killed\", \"completed_at\": \"2026-05-20T14:48:17.102Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-20T14:48:25.726567+00:00\"}]}}, \"exp_qwen25_14b_fewnerd\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-19T06:19:31.620Z\", \"updated_at\": \"2026-05-20T14:12:35.350Z\", \"hypothesis\": \"The correlation-selection gap pattern is consistent at 14B scale, filling the gap between 8B and 32B. Qwen2.5-14B QLoRA fine-tuned on FewNERD should show intermediate degeneracy rates and similar signal ranking patterns, providing a smooth scaling curve for the diagnostic findings.\", \"server\": \"autodl-5090-c\", \"gpu\": \"cuda:0,cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"autodl-5090-c\", \"gpu\": \"cuda:0,cuda:1\", \"started_at\": \"2026-05-19T06:47:43.938Z\"}, \"notes\": \"2026-05-19 12:47 UTC: RECOVERED from false-positive startup recovery failure. Step 6483/41180 (15.7%), loss 0.0608, ~2.2s/it, ETA ~21h. checkpoint-6000 saved. screen train_14b_s42 PID 56766, GPU 0,1 95-96% util. Cron registered on PID 56773.\", \"failure_reason\": \"startup recovery: RUNNING with no cron and no server/pid info\", \"completed_at\": \"2026-05-19T12:44:29.453Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"2026-05-19 11:36 UTC: step 4934/41180 (12.0%), loss 0.067, ~2.15s/it, ETA ~22h. checkpoint-4000 saved. screen train_14b_s42, 2×5090 76-77% util.\"}}, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0,1 FORCE_TORCHRUN=1 NNODES=1 NPROC_PER_NODE=2 llamafactory-cli train train_config_qwen25_14b_fewnerd_s42.yaml\", \"server\": \"autodl-5090-c\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/fewnerd/llmfactory_train.json\", \"data_count\": 131767, \"model_name\": \"Qwen2.5-14B-Instruct\", \"seed\": 42, \"gpu_ids\": [\"cuda:0\", \"cuda:1\"], \"screen_session\": \"train_14b_s42\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/logs/train_14b_s42.log\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen25-14b-fewnerd-qlora-s42/\"}, \"metrics\": {\"epoch\": 5, \"train_loss\": 0.0348, \"eval_loss\": 0.0323, \"train_runtime_hours\": 29.8, \"train_samples_per_second\": 6.141, \"train_steps_per_second\": 0.384, \"total_steps\": 41180}, \"conclusion\": \"success\"}, \"exp_b1_scd_conll_control\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-20T11:17:40.591Z\", \"updated_at\": \"2026-05-20T13:08:32.832Z\", \"hypothesis\": \"Negative control: SCD on CoNLL where construction gain is negative (-0.4pp, high degeneracy 70%). If SCD learns from construction pseudo-labels, it should NOT improve greedy F1 on a dataset where construction itself hurts. Expected: no improvement or slight degradation. Validates SCD mechanism.\", \"spec\": {\"command\": \"llamafactory-cli train train_config_scd_conll_s42.yaml\", \"server\": \"autodl-5090-b\", \"gpu_ids\": [2], \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/scd_conll_theta2n_s42.jsonl\", \"data_count\": 3453, \"model_name\": \"Qwen3-8B-FT-CoNLL\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-conll-scd-lora\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/logs/scd_conll_s42.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-20T12:14:27.727Z\"}, \"failure_reason\": \"OVERRIDE: Training completed normally (690/690 steps, loss=0.0359). Cron misjudged as failed. Pending eval inference.\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-20T12:14:30.260Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-20T12:14:35.853775+00:00\"}]}, \"metrics\": {\"pre_scd_greedy_f1\": 0.9078, \"post_scd_greedy_f1\": 0.9184, \"delta_pp\": 1.06, \"training_steps\": 690, \"final_loss\": 0.0359, \"negative_control_confirmed\": false, \"note\": \"SURPRISE: SCD improved CoNLL F1 by +1.06pp despite negative construction gain. Possible explanations: (1) SCD provides general training benefit (more data), (2) additional training steps alone improve, (3) SCD mechanism doesn't require positive construction gain.\"}}, \"exp_qwen25_7b_fewnerd\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T06:41:43.121Z\", \"updated_at\": \"2026-05-20T05:45:54.613Z\", \"hypothesis\": \"Qwen2.5-7B QLoRA fine-tuned on FewNERD will produce structurally diverse samples enabling self-consistency-based entity extraction with meaningful LP-weighted consensus signals, comparable to the 14B model but with lower compute cost.\", \"spec\": {\"server\": \"autodl-5090-c\", \"gpu_ids\": [\"cuda:2\", \"cuda:3\"], \"command\": \"nohup bash run_fewnerd_qwen25_7b_pipeline.sh > logs/pipeline_qwen25_7b_fewnerd.log 2>&1 &\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/fewnerd/llmfactory_train.json\", \"data_count\": 131767, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen25-7b-fewnerd-qlora-s42\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/logs/pipeline_qwen25_7b_fewnerd.log\", \"training_config\": \"train_config_qwen25_7b_fewnerd_s42.yaml\", \"export_config\": \"export_config_qwen25_7b_fewnerd.yaml\", \"pipeline_script\": \"run_fewnerd_qwen25_7b_pipeline.sh\", \"method\": \"QLoRA 4-bit nf4, rank=32, alpha=64, 5 epochs, lr=2e-4, effective_batch=32\", \"pipeline_phases\": \"train -> export/merge -> 3-seed N=8 inference (42/123/456) -> signal analysis -> entity construction\"}, \"notes\": \"2026-05-19 11:36 UTC: step 138/20590 (0.7%), ~2.34s/it, ETA ~13.3h. Pipeline PID 71837, llamafactory PID 71844. cuda:2,3 98-100% util. Cron registered on pipeline PID.\", \"server\": \"autodl-5090-c\", \"gpu\": \"cuda:2,cuda:3\", \"metrics\": {\"3seed_mean\": {\"lp_rho\": 0.346, \"lp_rho_std\": 0.021, \"sj_rho\": 0.388, \"sj_rho_std\": 0.029, \"vc_rho\": 0.404, \"vc_rho_std\": 0.01, \"degen_pct\": 31.7, \"degen_std\": 0.9, \"greedy_f1\": 0.784, \"greedy_f1_std\": 0.001, \"oracle_f1\": 0.876, \"oracle_f1_std\": 0.003, \"construction_lp_delta_pp\": -0.11, \"construction_lp_delta_std\": 0.25}, \"per_seed\": {\"seed42\": {\"lp_rho\": 0.3221, \"sj_rho\": 0.3554, \"vc_rho\": 0.393, \"degen_pct\": 31.1, \"greedy_f1\": 0.7851, \"oracle_f1\": 0.8718, \"construction_lp_delta_pp\": -0.4, \"bootstrap_p\": 1, \"bootstrap_ci\": [-0.53, -0.26], \"cohens_d\": -0.0319}, \"seed123\": {\"lp_rho\": 0.3538, \"sj_rho\": 0.3979, \"vc_rho\": 0.4067, \"degen_pct\": 32.8, \"greedy_f1\": 0.785, \"oracle_f1\": 0.8777, \"construction_lp_delta_pp\": -0.03, \"bootstrap_p\": 0.651}, \"seed456\": {\"lp_rho\": 0.3629, \"sj_rho\": 0.4105, \"vc_rho\": 0.4118, \"degen_pct\": 31.3, \"greedy_f1\": 0.7825, \"oracle_f1\": 0.8771, \"construction_lp_delta_pp\": 0.09, \"bootstrap_p\": 0.168}}, \"construction_significant\": false}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-20T05:45:54.613Z\"}, \"exp_qwen25_72b_fewshot\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T15:59:44.340Z\", \"updated_at\": \"2026-05-20T00:54:59.032Z\", \"hypothesis\": \"Few-shot prompting improves base NER F1 and LP signal quality, enabling LP-weighted construction to outperform greedy selection via dual-gating (sufficient LP ρ + low degeneracy).\", \"parent\": \"exp_qwen25_72b_zeroshot\", \"server\": \"autodl-5090-b\", \"gpu\": \"cuda:0,cuda:1,cuda:2,cuda:3\", \"account\": \"root\", \"reproduce\": {\"server\": \"autodl-5090-b\", \"gpu\": \"cuda:0,cuda:1,cuda:2,cuda:3\", \"started_at\": \"2026-05-19T16:22:20.071Z\", \"finished_at\": \"2026-05-20T00:47:36.445Z\", \"training_hours\": 8.42}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=0,1,2,3 python code/fewshot_inference_72b.py --datasets scierc conll2003 fewnerd --output-dir output/72b_fewshot --seed 42\\\"\", \"server\": \"autodl-5090-b\", \"gpu\": [\"cuda:0\", \"cuda:1\", \"cuda:2\", \"cuda:3\"], \"pid\": 131293, \"log_path\": \"~/runs/struct_self_consist_ie/exp_qwen25_72b_fewshot.log\", \"submitted_at\": \"2026-05-19T16:25:57.711Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/{scierc,conll2003,fewnerd}\", \"data_count\": 41652, \"model_name\": \"Qwen2.5-72B-Instruct-AWQ\", \"seed\": 42, \"gpu_ids\": [\"cuda:0\", \"cuda:1\", \"cuda:2\", \"cuda:3\"], \"checkpoint_source\": \"Qwen2.5-72B-Instruct-AWQ (base model, no fine-tuning)\", \"eval_data\": \"SciERC + CoNLL-2003 + FewNERD test sets\", \"wall_clock_seconds\": 30541.3, \"gpu_hours\": 33.93}, \"metrics\": {\"scierc\": {\"lp_rho\": 0.06, \"sj_rho\": 0.293, \"fk_rho\": 0.301, \"vc_rho\": 0.258, \"em_rho\": 0.205, \"degen_pct\": 16.6, \"greedy_f1\": 0.461, \"oracle_f1\": 0.604, \"construction_f1\": 0.461, \"construction_delta_pp\": -0.08, \"bootstrap_p\": 0.544}, \"conll\": {\"lp_rho\": 0.106, \"sj_rho\": 0.442, \"fk_rho\": 0.451, \"vc_rho\": 0.426, \"em_rho\": 0.403, \"degen_pct\": 70, \"greedy_f1\": 0.745, \"oracle_f1\": 0.796, \"construction_f1\": 0.745, \"construction_delta_pp\": 0.03, \"bootstrap_p\": 0.417}, \"fewnerd\": {\"lp_rho\": 0.161, \"sj_rho\": 0.345, \"fk_rho\": 0.327, \"vc_rho\": 0.41, \"em_rho\": 0.302, \"degen_pct\": 45.2, \"greedy_f1\": 0.619, \"oracle_f1\": 0.702, \"construction_f1\": 0.619, \"construction_delta_pp\": 0.02, \"bootstrap_p\": 0.401}}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-20T00:47:43.131229+00:00\"}]}, \"conclusion\": \"negative\", \"checkpoint_path\": \"output/72b_fewshot/ + output/72b_fewshot_signals/\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_qwen25_72b_fewshot.log\", \"completed_at\": \"2026-05-20T00:54:59.032Z\"}, \"exp_qwen25_72b_zeroshot\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-19T06:19:28.597Z\", \"updated_at\": \"2026-05-19T16:23:10.481Z\", \"hypothesis\": \"A larger zero-shot model (72B) will show higher greedy F1 and wider oracle-greedy gap than fine-tuned smaller models, because increased capacity enables more diverse valid extractions per stochastic sample, making self-consistency signals (SJ, FK, VC, EM) more informative for quality estimation.\", \"server\": \"autodl-5090-b\", \"gpu\": \"cuda:0,cuda:1,cuda:2,cuda:3\", \"account\": \"root\", \"reproduce\": {\"server\": \"autodl-5090-b\", \"gpu\": \"cuda:0,cuda:1,cuda:2,cuda:3\", \"started_at\": \"2026-05-19T06:47:42.658Z\", \"finished_at\": \"2026-05-19T14:14:58.577Z\", \"training_hours\": 7.45}, \"notes\": \"2026-05-19 12:47 UTC: RECOVERED from false-positive startup recovery failure. 289848/301184 prompts (96.2%). SciERC ✅ (551) CoNLL ✅ (3453) FewNERD ~96%. ETA ~10-15min. PID 59040, 4×5090 100% util. Cron registered.\", \"failure_reason\": \"FALSE POSITIVE — cron误判。实验实际成功完成（3个数据集全部处理完毕）。\", \"completed_at\": \"2026-05-19T12:44:26.198Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"2026-05-19 11:36 UTC: 69.8% complete (210352/301184 prompts). SciERC ✅ CoNLL ✅ FewNERD ~66%. ETA ~1h15m. vLLM PID 59040, 4×5090 100% util.\"}, \"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-19T14:15:08.634709+00:00\"}]}, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0,1,2,3 python code/zeroshot_inference_72b.py --datasets scierc conll2003 fewnerd --output-dir output/72b_zeroshot --seed 42\", \"server\": \"autodl-5090-b\", \"data_path\": \"data/{scierc,conll2003,fewnerd}\", \"data_count\": 41630, \"model_name\": \"Qwen2.5-72B-Instruct-AWQ\", \"seed\": 42, \"gpu_ids\": [\"cuda:0\", \"cuda:1\", \"cuda:2\", \"cuda:3\"], \"pid\": 59040}, \"conclusion\": \"negative\", \"metrics\": {\"scierc\": {\"greedy_f1\": 0.3993, \"lp_rho\": 0.081, \"vc_rho\": 0.277, \"sj_rho\": 0.217, \"degen_rate\": 0.21, \"construction_lp_weighted_f1\": 0.4146, \"construction_lp_delta_pp\": 1.53, \"construction_uniform_f1\": 0.3941, \"construction_uniform_delta_pp\": -0.52, \"lp_selection_f1\": 0.3984, \"majority_vote_f1\": 0.4132, \"oracle_f1\": 0.5489, \"bootstrap_p\": 0.0082, \"bootstrap_ci_lower\": 0.0025, \"bootstrap_ci_upper\": 0.0282, \"cohens_d\": 0.1027, \"n_instances\": 529, \"non_degen_delta_pp\": 1.65, \"non_degen_p\": 0.0069}, \"conll2003\": {\"greedy_f1\": 0.712, \"lp_rho\": -0.002, \"vc_rho\": 0.297, \"sj_rho\": 0.304, \"degen_rate\": 0.677, \"construction_lp_weighted_f1\": 0.7083, \"construction_lp_delta_pp\": -0.37, \"construction_uniform_f1\": 0.7028, \"construction_uniform_delta_pp\": -0.92, \"lp_selection_f1\": 0.708, \"majority_vote_f1\": 0.7034, \"oracle_f1\": 0.7651}, \"fewnerd\": {\"greedy_f1\": 0.6281, \"lp_rho\": 0.119, \"vc_rho\": 0.416, \"sj_rho\": 0.345, \"degen_rate\": 0.462, \"construction_lp_weighted_f1\": 0.6261, \"construction_lp_delta_pp\": -0.2, \"construction_uniform_f1\": 0.6112, \"construction_uniform_delta_pp\": -1.7, \"lp_selection_f1\": 0.6241, \"lp_selection_delta_pp\": -0.4, \"majority_vote_f1\": 0.6262, \"oracle_f1\": 0.7072}}}, \"exp_wnut17_qwen25_7b\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T06:19:33.960Z\", \"updated_at\": \"2026-05-19T11:49:07.313Z\", \"hypothesis\": \"The correlation-selection gap extends to noisy social media NER (WNUT-17). Unlike formal-domain datasets (SciERC/CoNLL/FewNERD), WNUT-17 has higher surface-level noise which may affect structural signal reliability differently. This tests domain generalization of the diagnostic framework.\", \"server\": \"autodl-5090-c\", \"gpu\": \"cuda:2,cuda:3\", \"account\": \"root\", \"reproduce\": {\"server\": \"autodl-5090-c\", \"gpu\": \"cuda:2,cuda:3\", \"started_at\": \"2026-05-19T06:47:45.220Z\"}, \"spec\": {\"server\": \"autodl-5090-c\", \"gpu_ids\": [\"cuda:2\", \"cuda:3\"], \"command\": \"bash wait_and_train.sh (screen: exp_wnut17_7b)\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/wnut17/llmfactory_train.json\", \"data_count\": 3404, \"model_name\": \"Qwen2.5-7B-Instruct\", \"seed\": 42, \"training_config\": \"train_config_qwen25_7b_wnut17_s42.yaml\", \"method\": \"QLoRA 4-bit (bnb nf4), rank=32, alpha=64, all targets\", \"gpus\": \"cuda:2,3 (2x5090)\", \"epochs\": 5, \"effective_batch_size\": 32, \"pipeline\": \"train → export → 3-seed inference (N=8, T=1.0) → signal analysis → entity construction\", \"checkpoint_source\": \"self-trained on WNUT-17\", \"eval_data\": \"WNUT-17 test set\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen25-7b-wnut17-qlora-s42\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/logs/exp_wnut17_7b_pipeline.log\"}, \"conclusion\": \"negative\", \"metrics\": {\"seed42\": {\"greedy_f1\": 0.4524, \"construction_f1\": 0.4439, \"construction_delta_pp\": -0.84, \"construction_p\": 0.95}, \"seed123\": {\"greedy_f1\": 0.4518, \"construction_f1\": 0.4579, \"construction_delta_pp\": 0.61, \"construction_p\": 0.08}, \"seed456\": {\"greedy_f1\": 0.4526, \"construction_f1\": 0.4583, \"construction_delta_pp\": 0.57, \"construction_p\": 0.12}, \"oracle_headroom_pp\": \"6.3-9.2\"}, \"completed_at\": \"2026-05-19T11:22:56.623Z\"}, \"exp_llama_fewnerd_inference\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T02:18:49.938Z\", \"updated_at\": \"2026-05-19T03:15:04.486Z\", \"hypothesis\": \"LLaMA-3.1-8B fine-tuned on FewNERD shows the same structured self-consistency phenomena (degeneracy, LP-F1 alignment, signal ranking) as Qwen models, providing cross-model generalization evidence. 3-seed inference (42/123/456) for statistical robustness.\", \"parent\": \"exp_llama_fewnerd_lora\", \"spec\": {\"command\": \"bash code/run_llama_fewnerd_inference.sh\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/fewnerd/\", \"data_count\": 37648, \"model_name\": \"LLaMA-3.1-8B-FewNERD-LoRA-merged\", \"seed\": \"42,123,456\", \"checkpoint_source\": \"exp_llama_fewnerd_lora\", \"eval_data\": \"FewNERD test set\", \"checkpoint_path\": \"checkpoints/llama3.1-8b-fewnerd-merged/\", \"log_path\": \"logs/llama_fewnerd_inference.log\"}, \"conclusion\": \"success\", \"metrics\": {\"3seed_mean\": {\"greedy_f1\": 0.7842, \"oracle_f1\": 0.8843, \"headroom_pp\": 10.01, \"degeneracy_pct\": 23.36, \"lp_delta_pp\": 0.36, \"dgs_delta_pp\": -0.35}, \"seed_42\": {\"greedy_f1\": 0.7841, \"oracle_f1\": 0.8854, \"degen\": 27.32}, \"seed_123\": {\"greedy_f1\": 0.784, \"oracle_f1\": 0.8839, \"degen\": 24.63}, \"seed_456\": {\"greedy_f1\": 0.7844, \"oracle_f1\": 0.8835, \"degen\": 18.13}, \"signal_ranking\": \"LP (+0.36pp) > SJ (-0.52) > FK (-0.53) > EM (-1.02) > VC (-2.39)\", \"lp_only_positive\": true, \"n_instances_gold_filtered\": 32565}, \"completed_at\": \"2026-05-19T03:15:04.486Z\"}, \"exp_entity_construction\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T02:00:12.074Z\", \"updated_at\": \"2026-05-19T02:40:17.571Z\", \"hypothesis\": \"Entity-level majority vote construction is the correct self-consistency analogy for structured IE: instead of selecting the best instance-level output, assemble a better output from entity-level consensus across N samples. Construction should outperform both greedy and best-of-N selection.\", \"conclusion\": \"success\", \"spec\": {\"command\": \"python code/entity_construction_fair.py\", \"server\": \"autodl-5090\", \"data_path\": \"output/*/samples_*.json\", \"data_count\": 3, \"model_name\": \"analysis_cpu\", \"seed\": 42, \"checkpoint_path\": \"output/entity_construction_fair/\", \"log_path\": \"output/entity_construction_fair/\"}, \"completed_at\": \"2026-05-19T02:15:19.616Z\", \"metrics\": {\"n16_fair_cv\": {\"scierc_ner\": {\"cv_uniform_delta\": \"+1.35pp\", \"p_value\": 0.018, \"significant\": true}, \"conll_ner\": {\"cv_uniform_delta\": \"+0.10pp\", \"p_value\": 0.303, \"significant\": false}, \"fewnerd_ner\": {\"cv_uniform_delta\": \"+1.32pp\", \"p_value\": 0, \"significant\": true}, \"scierc_re\": {\"cv_uniform_delta\": \"+1.69pp\", \"p_value\": 0.049, \"significant\": true}}, \"n8_fair_cv\": {\"scierc_ner\": {\"uniform_confirm\": \"+1.54pp (p=0.023, sig)\", \"lp_weighted_confirm\": \"+1.67pp (p=0.004, sig)\", \"cv_uniform\": \"+1.12pp (p=0.057, borderline)\"}, \"conll_ner\": {\"cv_uniform\": \"-0.39pp (p=0.963, not sig)\"}, \"fewnerd_ner\": {\"lp_weighted_cv\": \"+0.88pp (p=0.000, sig)\", \"uniform_cv\": \"+0.32pp (p=0.003, sig)\"}}, \"adaptive_combination\": \"INVALIDATED - gold label leakage confirmed\", \"note\": \"5-fold CV, bootstrap B=10000, paired one-sided\"}}, \"exp_lp_alignment_gating\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T02:00:16.520Z\", \"updated_at\": \"2026-05-19T02:15:48.197Z\", \"hypothesis\": \"Within-instance LP-F1 alignment score (adjusted by valid_ratio for degeneracy) can automatically gate whether LP selection should be applied to a dataset. A small probe sample (50-100 instances) suffices for a stable gating decision.\", \"conclusion\": \"success\", \"spec\": {\"command\": \"python code/lp_alignment_gated_selection.py\", \"server\": \"autodl-5090\", \"data_path\": \"output/*/samples_*.json\", \"data_count\": 3, \"model_name\": \"analysis_cpu\", \"seed\": 42, \"checkpoint_path\": \"output/prescriptive_analysis/\", \"log_path\": \"output/prescriptive_analysis/\"}, \"completed_at\": \"2026-05-19T02:15:23.716Z\", \"metrics\": {\"adjusted_score\": \"mean_rho * valid_ratio\", \"threshold\": 0.3, \"accuracy\": \"3/3 datasets correct\", \"robust_range\": \"0.2-0.4\"}}, \"exp_selective_prediction\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-19T02:00:13.989Z\", \"updated_at\": \"2026-05-19T02:15:46.588Z\", \"hypothesis\": \"QE signals (especially voting_confidence) can drive practical selective prediction: filtering out low-confidence instances yields significant F1 improvement on retained instances, enabling human-AI collaboration for structured IE.\", \"conclusion\": \"success\", \"spec\": {\"command\": \"python code/selective_prediction.py\", \"server\": \"autodl-5090\", \"data_path\": \"output/*/samples_*.json\", \"data_count\": 3, \"model_name\": \"analysis_cpu\", \"seed\": 42, \"checkpoint_path\": \"output/prescriptive_analysis/\", \"log_path\": \"output/prescriptive_analysis/\"}, \"completed_at\": \"2026-05-19T02:15:21.704Z\", \"metrics\": {\"vc_best_signal\": true, \"f1_at_80pct_coverage\": {\"scierc\": \"+5.0pp\", \"conll\": \"+8.4pp\", \"fewnerd\": \"+6.2pp\"}, \"precision_coverage_curves\": \"output/prescriptive_analysis/fig_selective_prediction.pdf\"}}, \"exp_llama_fewnerd_lora\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T13:20:55.859Z\", \"updated_at\": \"2026-05-19T01:08:20.832Z\", \"hypothesis\": \"LLaMA-based model with LoRA fine-tuning on Few-NERD can provide a second model family (beyond Qwen) for cross-model generalization evidence of structured self-consistency phenomena in NER\", \"spec\": {\"command\": \"llamafactory-cli train train_config_llama_fewnerd.yaml\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:1\", \"pid\": 137865, \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/fewnerd\", \"data_count\": -1, \"model_name\": \"LLaMA-Few-NERD-LoRA\", \"seed\": 42, \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/logs/llama_fewnerd_train.log\", \"run_script\": \"run_llama_fewnerd_train_single_gpu.sh\", \"tmux_session\": \"llama_fewnerd\", \"note\": \"Retroactively registered - data_count unknown, seed assumed 42\"}, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/llama3.1-8b-fewnerd-lora\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/logs/llama_fewnerd_train.log\", \"conclusion\": \"success\", \"metrics\": {\"epoch\": 3, \"train_loss\": 0.0516, \"eval_loss\": 0.0323, \"train_runtime_hours\": 15.35, \"total_steps\": 24708, \"final_checkpoint\": \"checkpoint-24708\", \"adapter_size_mb\": 320}, \"completed_at\": \"2026-05-19T01:08:20.832Z\"}, \"hidden_state_probe_conll_full\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T12:57:45.711Z\", \"updated_at\": \"2026-05-19T00:30:18.272Z\", \"conclusion\": \"killed\", \"notes\": \"Not in D154 Dual Contribution framing\", \"completed_at\": \"2026-05-19T00:30:18.272Z\"}, \"hidden_state_probe_conll_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T12:35:05.317Z\", \"updated_at\": \"2026-05-19T00:30:16.471Z\", \"conclusion\": \"killed\", \"notes\": \"Not in D154 Dual Contribution framing\", \"completed_at\": \"2026-05-19T00:30:16.471Z\"}, \"exp_031_fewnerd_t12\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T20:04:12.040Z\", \"updated_at\": \"2026-05-19T00:30:14.652Z\", \"hypothesis\": \"FewNERD T=1.2 temperature ablation: test if higher temperature reduces degeneracy on FewNERD as observed on SciERC\", \"conclusion\": \"killed\", \"failure_reason\": \"数据不可用于论文：测试集(37648 vs T=1.0的5000)、N(8 vs 16)、分析管道(MVP pilot vs 5-signal)三重不一致。Director决定不重跑(DDL约束+非核心claim)。\", \"notes\": \"T=1.2 ablation not in paper scope, SciERC T=1.2 sufficient\", \"completed_at\": \"2026-05-19T00:30:14.652Z\"}, \"exp_030_conll_t12\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T20:24:47.839Z\", \"updated_at\": \"2026-05-19T00:30:12.698Z\", \"hypothesis\": \"CoNLL T=1.2 temperature ablation: test if higher temperature reduces degeneracy on CoNLL as observed on SciERC\", \"conclusion\": \"killed\", \"failure_reason\": \"数据不可用于论文：N不一致(N=8 vs T=1.0基准的N=16)。Director决定不重跑——SciERC T消融(T=0.5/0.8/1.0/1.2, 551inst, N=8)已够用，论文温度消融用SciERC单数据集。\", \"notes\": \"T=1.2 ablation not in paper scope, SciERC T=1.2 sufficient\", \"completed_at\": \"2026-05-19T00:30:12.699Z\"}, \"mbr_pilot\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T17:56:06.462Z\", \"updated_at\": \"2026-05-19T00:29:39.285Z\", \"conclusion\": \"killed\", \"notes\": \"MBR tested negative as one of 6 methods, stale entry\", \"completed_at\": \"2026-05-19T00:29:39.285Z\"}, \"dgs_pilot\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T17:56:04.572Z\", \"updated_at\": \"2026-05-19T00:29:37.275Z\", \"hypothesis\": \"Degeneracy-Gated Selection (DGS) validates Two-Condition Theory: using degeneracy rate as gating mechanism to switch between greedy (degenerate) and LP selection (non-degenerate), the improvement direction should follow a monotonic gradient — low degeneracy yields positive delta, high degeneracy yields negative delta.\", \"conclusion\": \"killed\", \"notes\": \"D154: DGS demoted to explored heuristic, cross-model direction contradiction (D152)\", \"completed_at\": \"2026-05-19T00:29:37.275Z\"}, \"exp_fewnerd_s789_n8\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T23:17:34.011Z\", \"updated_at\": \"2026-05-18T23:18:28.125Z\", \"hypothesis\": \"FewNERD seed789 (4th seed) for statistical CI strengthening: 4-seed protocol provides tighter confidence intervals on LP selection gain and DGS effectiveness in low-degeneracy regime.\", \"parent\": \"exp_029a\", \"spec\": {\"command\": \"python code/analyze_fewnerd_s789.py\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/fewnerd_seed789_merged/samples.jsonl\", \"data_count\": 37648, \"model_name\": \"Qwen3-8B (ft_002_v2)\", \"seed\": 789, \"checkpoint_source\": \"exp_021 shards\", \"eval_data\": \"FewNERD test (37648 instances, 32565 gold-filtered)\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/fewnerd_seed789_merged/\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/fewnerd_seed789_merged/run.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T23:18:17.902Z\", \"metrics\": {\"greedy_f1\": 0.7478, \"oracle_f1\": 0.8714, \"headroom_pp\": 12.37, \"degen_rate\": 0.1177, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\", \"instance_count\": 37648, \"n_valid\": 32565, \"lp_sel_f1\": 0.7614, \"lp_delta_pp\": 1.36, \"lp_rho_global\": 0.1788, \"lp_rho_cond\": 0.176, \"dgs_f1\": 0.7621, \"dgs_delta_pp\": 1.43, \"dgs_vs_lp_pp\": 0.07, \"best_signal\": \"LP\", \"four_seed_mean_greedy\": 0.7481, \"four_seed_mean_lp_delta_pp\": 1.38, \"four_seed_lp_delta_ci95\": [1.32, 1.44]}}, \"exp_026_t12_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T22:05:43.694Z\", \"updated_at\": \"2026-05-18T22:07:24.547Z\", \"hypothesis\": \"Temperature ablation (T=1.2, seed=456) of Qwen3-8B SciERC N=8 SCS inference to study temperature sensitivity of structural consistency signals.\", \"spec\": {\"command\": \"python scs_inference.py --dataset scierc --seed 456 --n_samples 8 --temperature 1.2\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/scierc\", \"data_count\": 551, \"model_name\": \"Qwen3-8B\", \"seed\": 456, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t12_seed456\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t12_seed456.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T22:07:05.941Z\", \"metrics\": {\"ner_greedy_f1\": 0.6637, \"ner_oracle_f1\": 0.7821, \"rho_sj_ner\": 0.3995, \"sample_f1_pct_zero\": 14.08, \"instance_count\": 551, \"n_valid\": 529}}, \"exp_026_t12_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T22:05:42.754Z\", \"updated_at\": \"2026-05-18T22:07:23.135Z\", \"hypothesis\": \"Temperature ablation (T=1.2, seed=123) of Qwen3-8B SciERC N=8 SCS inference to study temperature sensitivity of structural consistency signals.\", \"spec\": {\"command\": \"python scs_inference.py --dataset scierc --seed 123 --n_samples 8 --temperature 1.2\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/scierc\", \"data_count\": 551, \"model_name\": \"Qwen3-8B\", \"seed\": 123, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t12_seed123\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t12_seed123.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T22:07:04.119Z\", \"metrics\": {\"ner_greedy_f1\": 0.6595, \"ner_oracle_f1\": 0.7895, \"rho_sj_ner\": 0.359, \"sample_f1_pct_zero\": 13.99, \"instance_count\": 551, \"n_valid\": 529}}, \"exp_026_t10_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T22:05:41.840Z\", \"updated_at\": \"2026-05-18T22:07:21.767Z\", \"hypothesis\": \"Temperature ablation (T=1.0, seed=456) of Qwen3-8B SciERC N=8 SCS inference to study temperature sensitivity of structural consistency signals.\", \"spec\": {\"command\": \"python scs_inference.py --dataset scierc --seed 456 --n_samples 8 --temperature 1.0\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/scierc\", \"data_count\": 551, \"model_name\": \"Qwen3-8B\", \"seed\": 456, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t10_seed456\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t10_seed456.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T22:07:02.272Z\", \"metrics\": {\"ner_greedy_f1\": 0.6621, \"ner_oracle_f1\": 0.7754, \"rho_sj_ner\": 0.3921, \"sample_f1_pct_zero\": 12.97, \"instance_count\": 551, \"n_valid\": 529}}, \"exp_026_t10_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T22:05:40.599Z\", \"updated_at\": \"2026-05-18T22:07:20.459Z\", \"hypothesis\": \"Temperature ablation (T=1.0, seed=123) of Qwen3-8B SciERC N=8 SCS inference to study temperature sensitivity of structural consistency signals.\", \"spec\": {\"command\": \"python scs_inference.py --dataset scierc --seed 123 --n_samples 8 --temperature 1.0\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/scierc\", \"data_count\": 551, \"model_name\": \"Qwen3-8B\", \"seed\": 123, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t10_seed123\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t10_seed123.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T22:07:00.430Z\", \"metrics\": {\"ner_greedy_f1\": 0.6633, \"ner_oracle_f1\": 0.7777, \"rho_sj_ner\": 0.3809, \"sample_f1_pct_zero\": 12.59, \"instance_count\": 551, \"n_valid\": 529}}, \"exp_026_t10_seed42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T22:05:39.473Z\", \"updated_at\": \"2026-05-18T22:07:19.035Z\", \"hypothesis\": \"Temperature ablation (T=1.0, seed=42) of Qwen3-8B SciERC N=8 SCS inference to study temperature sensitivity of structural consistency signals.\", \"spec\": {\"command\": \"python scs_inference.py --dataset scierc --seed 42 --n_samples 8 --temperature 1.0\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/scierc\", \"data_count\": 551, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t10_seed42\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t10_seed42.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T22:06:58.573Z\", \"metrics\": {\"ner_greedy_f1\": 0.6617, \"ner_oracle_f1\": 0.7798, \"rho_sj_ner\": 0.3598, \"sample_f1_pct_zero\": 12.9, \"instance_count\": 551, \"n_valid\": 529}}, \"exp_026_t08_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T22:05:38.605Z\", \"updated_at\": \"2026-05-18T22:07:17.604Z\", \"hypothesis\": \"Temperature ablation (T=0.8, seed=456) of Qwen3-8B SciERC N=8 SCS inference to study temperature sensitivity of structural consistency signals.\", \"spec\": {\"command\": \"python scs_inference.py --dataset scierc --seed 456 --n_samples 8 --temperature 0.8\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/scierc\", \"data_count\": 551, \"model_name\": \"Qwen3-8B\", \"seed\": 456, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t08_seed456\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t08_seed456.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T22:06:56.681Z\", \"metrics\": {\"ner_greedy_f1\": 0.6641, \"ner_oracle_f1\": 0.7694, \"rho_sj_ner\": 0.3771, \"sample_f1_pct_zero\": 11.79, \"instance_count\": 551, \"n_valid\": 529}}, \"exp_026_t08_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T22:05:37.454Z\", \"updated_at\": \"2026-05-18T22:07:16.089Z\", \"hypothesis\": \"Temperature ablation (T=0.8, seed=123) of Qwen3-8B SciERC N=8 SCS inference to study temperature sensitivity of structural consistency signals.\", \"spec\": {\"command\": \"python scs_inference.py --dataset scierc --seed 123 --n_samples 8 --temperature 0.8\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/scierc\", \"data_count\": 551, \"model_name\": \"Qwen3-8B\", \"seed\": 123, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t08_seed123\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t08_seed123.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T22:06:54.734Z\", \"metrics\": {\"ner_greedy_f1\": 0.6607, \"ner_oracle_f1\": 0.7714, \"rho_sj_ner\": 0.3893, \"sample_f1_pct_zero\": 11.22, \"instance_count\": 551, \"n_valid\": 529}}, \"exp_026_t05_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T22:05:36.536Z\", \"updated_at\": \"2026-05-18T22:07:14.675Z\", \"hypothesis\": \"Temperature ablation (T=0.5, seed=456) of Qwen3-8B SciERC N=8 SCS inference to study temperature sensitivity of structural consistency signals.\", \"spec\": {\"command\": \"python scs_inference.py --dataset scierc --seed 456 --n_samples 8 --temperature 0.5\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/scierc\", \"data_count\": 551, \"model_name\": \"Qwen3-8B\", \"seed\": 456, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t05_seed456\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t05_seed456.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T22:06:52.749Z\", \"metrics\": {\"ner_greedy_f1\": 0.6639, \"ner_oracle_f1\": 0.7437, \"rho_sj_ner\": 0.3279, \"sample_f1_pct_zero\": 10.28, \"instance_count\": 551, \"n_valid\": 529}}, \"exp_026_t05_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T22:05:35.201Z\", \"updated_at\": \"2026-05-18T22:07:13.198Z\", \"hypothesis\": \"Temperature ablation (T=0.5, seed=123) of Qwen3-8B SciERC N=8 SCS inference to study temperature sensitivity of structural consistency signals.\", \"spec\": {\"command\": \"python scs_inference.py --dataset scierc --seed 123 --n_samples 8 --temperature 0.5\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/scierc\", \"data_count\": 551, \"model_name\": \"Qwen3-8B\", \"seed\": 123, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t05_seed123\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_026_t05_seed123.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T22:06:50.703Z\", \"metrics\": {\"ner_greedy_f1\": 0.6611, \"ner_oracle_f1\": 0.7444, \"rho_sj_ner\": 0.3133, \"sample_f1_pct_zero\": 10.09, \"instance_count\": 551, \"n_valid\": 529}}, \"exp_029b\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-17T23:32:18.543Z\", \"updated_at\": \"2026-05-18T22:05:45.856Z\", \"hypothesis\": \"Training convergence modulates degeneracy across datasets. SciERC 10-epoch training should produce higher degeneracy than 5-epoch baseline (17.8%), confirming monotonic epoch-degeneracy relationship across datasets.\", \"parent\": \"ft_002_v2\", \"failure_reason\": \"OOM on cuda:1 due to residual vLLM process (PID 416808) occupying 30.2GB VRAM\", \"reproduce\": {\"finished_at\": \"2026-05-18T02:05:15.948Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T00:55:29.806594+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T01:58:43.646574+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T02:05:20.480884+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"completed_at\": \"2026-05-18T00:56:47.625Z\", \"spec\": {\"pid\": \"441471\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:1\", \"command\": \"FORCE_TORCHRUN=0 CUDA_VISIBLE_DEVICES=1 llamafactory-cli train train_config_scierc_10ep.yaml\", \"data_path\": \"scierc_uie_train\", \"data_count\": 1861, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"checkpoint_source\": \"Qwen/Qwen3-8B\", \"eval_data\": \"scierc_uie_test\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-scierc-10epoch-lora/\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_029b.log\"}, \"metrics\": {\"degen_rate\": 0.478, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\"}, \"conclusion\": \"success\"}, \"exp_029a\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T23:32:17.191Z\", \"updated_at\": \"2026-05-18T22:05:44.959Z\", \"hypothesis\": \"Training convergence modulates degeneracy across datasets. SciERC 3-epoch training should produce lower degeneracy than 5-epoch baseline (17.8%), confirming epoch confound is not Few-NERD-specific.\", \"parent\": \"ft_002_v2\", \"spec\": {\"command\": \"FORCE_TORCHRUN=0 CUDA_VISIBLE_DEVICES=0 bash -c \\\"source /root/miniconda3/bin/activate && cd /root/autodl-tmp/struct_self_consist_ie && llamafactory-cli train train_config_scierc_3ep.yaml\\\"\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:0\", \"pid\": 436761, \"data_path\": \"data/scierc_uie_train\", \"data_count\": 1861, \"model_name\": \"Qwen3-8B LoRA rank=32\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-scierc-3epoch-lora\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/logs/exp_029a_inference.log\", \"checkpoint_source\": \"Qwen/Qwen3-8B\", \"eval_data\": \"data/scierc_uie_dev\"}, \"reproduce\": {\"finished_at\": \"2026-05-18T00:55:16.392Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-18T00:55:20.617085+00:00\"}]}, \"failure_reason\": \"\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T01:00:18.242Z\", \"metrics\": {\"degen_rate\": 0.064, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\"}}, \"exp_021_fewnerd_n8_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T22:03:17.992Z\", \"updated_at\": \"2026-05-18T22:04:50.774Z\", \"hypothesis\": \"Multi-seed replication (seed=456) of Qwen3-8B FewNERD N=8 SCS inference to validate structural consistency signal on fine-grained NER dataset.\", \"spec\": {\"command\": \"python scs_inference.py --dataset fewnerd --seed 456 --n_samples 8 --temperature 1.0\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/fewnerd\", \"data_count\": 37648, \"model_name\": \"Qwen3-8B\", \"seed\": 456, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_021_fewnerd_n8_seed456\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_021_fewnerd_n8_seed456_run.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T22:04:35.573Z\", \"metrics\": {\"degen_rate\": 0.1212, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\", \"instance_count\": 37648, \"n_valid\": 32565, \"n_gold_empty\": 5083, \"ner_greedy_f1\": 0.7888, \"ner_oracle_f1\": 0.881, \"rho_fk_ner\": 0.1632, \"rho_sj_ner\": 0.313, \"sample_f1_pct_zero\": 19.32}}, \"exp_021_fewnerd_n8_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T22:03:16.735Z\", \"updated_at\": \"2026-05-18T22:04:49.470Z\", \"hypothesis\": \"Multi-seed replication (seed=123) of Qwen3-8B FewNERD N=8 SCS inference to validate structural consistency signal on fine-grained NER dataset.\", \"spec\": {\"command\": \"python scs_inference.py --dataset fewnerd --seed 123 --n_samples 8 --temperature 1.0\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/fewnerd\", \"data_count\": 37648, \"model_name\": \"Qwen3-8B\", \"seed\": 123, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_021_fewnerd_n8_seed123\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_021_fewnerd_n8_seed123_run.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T22:04:33.731Z\", \"metrics\": {\"degen_rate\": 0.1312, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\", \"instance_count\": 37648, \"n_valid\": 32565, \"n_gold_empty\": 5083, \"ner_greedy_f1\": 0.7885, \"ner_oracle_f1\": 0.8892, \"rho_fk_ner\": 0.1602, \"rho_sj_ner\": 0.3083, \"sample_f1_pct_zero\": 20.39}}, \"exp_002_conll_n16_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T22:03:15.720Z\", \"updated_at\": \"2026-05-18T22:04:46.954Z\", \"hypothesis\": \"Multi-seed replication (seed=456) of Qwen3-8B CoNLL-2003 N=16 SCS inference to validate structural consistency signal stability across random seeds.\", \"spec\": {\"command\": \"python scs_inference.py --dataset conll2003 --seed 456 --n_samples 16 --temperature 1.0\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/conll2003\", \"data_count\": 3453, \"model_name\": \"Qwen3-8B\", \"seed\": 456, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_002_conll_n16_seed456\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_002_conll_n16_seed456.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T22:04:31.934Z\", \"metrics\": {\"degen_rate\": 0.5544, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\", \"instance_count\": 3453, \"n_valid\": 2756, \"n_gold_empty\": 697, \"ner_greedy_f1\": 0.9074, \"ner_oracle_f1\": 0.9549, \"rho_fk_ner\": 0.4718, \"rho_sj_ner\": 0.4819, \"sample_f1_pct_zero\": 7.02}}, \"exp_002_conll_n16_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T22:03:14.343Z\", \"updated_at\": \"2026-05-18T22:04:45.039Z\", \"hypothesis\": \"Multi-seed replication (seed=123) of Qwen3-8B CoNLL-2003 N=16 SCS inference to validate structural consistency signal stability across random seeds.\", \"spec\": {\"command\": \"python scs_inference.py --dataset conll2003 --seed 123 --n_samples 16 --temperature 1.0\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/conll2003\", \"data_count\": 3453, \"model_name\": \"Qwen3-8B\", \"seed\": 123, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_002_conll_n16_seed123\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_002_conll_n16_seed123.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T22:04:29.992Z\", \"metrics\": {\"degen_rate\": 0.471, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\", \"instance_count\": 3453, \"n_valid\": 2756, \"n_gold_empty\": 697, \"ner_greedy_f1\": 0.9068, \"ner_oracle_f1\": 0.9633, \"rho_fk_ner\": 0.4524, \"rho_sj_ner\": 0.4621, \"sample_f1_pct_zero\": 7.54}}, \"exp_017_llama_conll_n16_s456_r1024\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:17:04.572Z\", \"updated_at\": \"2026-05-18T20:50:15.047Z\", \"spec\": {\"hypothesis\": \"D054 rerun: max_tokens=1024. Verify truncation impact on LLaMA CoNLL N=16 seed456.\", \"parent\": \"exp_017_llama_conll_n16_s456\", \"model_name\": \"llama3.1-8b-conll2003-merged\", \"dataset\": \"CoNLL-2003\", \"seed\": 456, \"server\": \"autodl-5090\", \"command\": \"python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 16 --temperature 1.0 --seed 456 --num_test 9999 --max_tokens 1024 --collect_logprobs --output_dir output/exp_017_llama_conll_n16_s456_r1024\", \"gpu\": \"cuda:2\", \"pid\": \"175870\", \"data_path\": \"data/conll2003\", \"data_count\": 3453, \"tmux_session\": \"exp_017_llama_conll_n16_s456_r1024\"}, \"conclusion\": \"success\", \"metrics\": {\"degen_rate\": 0.8672, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\", \"instance_count\": 3453, \"n_valid\": 2756, \"n_gold_empty\": 697, \"parse_rate\": 1, \"ner_greedy_f1\": 0.9265, \"ner_oracle_f1\": 0.9499, \"rho_fk_ner\": 0.469, \"rho_sj_ner\": 0.4734, \"rho_vc_ner\": 0.4722, \"rho_em_ner\": 0.4752, \"rho_lp_ner\": 0.3099, \"auroc_fk_ner\": 0.7408, \"auroc_sj_ner\": 0.7428, \"auroc_vc_ner\": 0.7495, \"auroc_em_ner\": 0.7444, \"auroc_lp_ner\": 0.7628, \"auroc_note\": \"median F1=1.0, AUROC uses >=median threshold\", \"rho_note\": \"CORRECTED 2026-05-15: old values (rho_fk=0.8085,rho_sj=0.1895) were inflated/deflated by 697 gold-empty instances. Now uses gold-filtered pipeline (n=2756).\"}, \"checkpoint_path\": \"N/A (inference-only)\", \"log_path\": \"output/exp_017_llama_conll_n16_s456_r1024_run.log\", \"completed_at\": \"2026-05-15T11:45:25.899Z\", \"hypothesis\": \"LLaMA CoNLL N=16 seed=456 (max_tokens=1024 rerun): cross-model multi-seed validation. Confirms structural>surface ordering is stable across seeds for LLaMA on CoNLL after gold-filtering correction.\"}, \"exp_017_llama_conll_n16_r1024\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:17:01.036Z\", \"updated_at\": \"2026-05-18T20:50:11.906Z\", \"spec\": {\"hypothesis\": \"D054 rerun: max_tokens=1024. Verify truncation impact on LLaMA CoNLL N=16 seed42.\", \"parent\": \"exp_017_llama_conll_n16\", \"model_name\": \"llama3.1-8b-conll2003-merged\", \"dataset\": \"CoNLL-2003\", \"seed\": 42, \"server\": \"autodl-5090\", \"command\": \"python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 16 --temperature 1.0 --seed 42 --num_test 9999 --max_tokens 1024 --collect_logprobs --output_dir output/exp_017_llama_conll_n16_r1024\", \"gpu\": \"cuda:1\", \"pid\": \"175734\", \"data_path\": \"data/conll2003\", \"data_count\": 3453, \"tmux_session\": \"exp_017_llama_conll_n16_r1024\"}, \"conclusion\": \"success\", \"metrics\": {\"degen_rate\": 0.8647, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\", \"instance_count\": 3453, \"n_valid\": 2756, \"n_gold_empty\": 697, \"parse_rate\": 1, \"ner_greedy_f1\": 0.9265, \"ner_oracle_f1\": 0.9499, \"rho_fk_ner\": 0.4752, \"rho_sj_ner\": 0.4836, \"rho_vc_ner\": 0.4746, \"rho_em_ner\": 0.4818, \"rho_lp_ner\": 0.3136, \"auroc_fk_ner\": 0.7467, \"auroc_sj_ner\": 0.7496, \"auroc_vc_ner\": 0.7529, \"auroc_em_ner\": 0.7508, \"auroc_lp_ner\": 0.7661, \"auroc_note\": \"median F1=1.0, AUROC uses >=median threshold\", \"rho_note\": \"CORRECTED 2026-05-15: old values (rho_fk=0.8095,rho_sj=0.1815) were inflated/deflated by 697 gold-empty instances. Now uses gold-filtered pipeline (n=2756).\"}, \"checkpoint_path\": \"N/A (inference-only)\", \"log_path\": \"output/exp_017_llama_conll_n16_r1024_run.log\", \"completed_at\": \"2026-05-15T11:45:23.213Z\", \"hypothesis\": \"LLaMA CoNLL N=16 seed=42 (max_tokens=1024 rerun): cross-model baseline on CoNLL. Establishes LLaMA signal rankings after gold-filtering correction (fixes inflated FK ρ from gold-empty instances).\"}, \"exp_018_llama_scierc_seed456_r1024\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T06:12:43.492Z\", \"updated_at\": \"2026-05-18T20:50:04.988Z\", \"spec\": {\"hypothesis\": \"D066 fresh rerun: LLaMA SciERC seed=456 with explicit max_tokens=1024. Replaces exp_007 re-analysis for clean 3-seed comparison.\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-scierc-merged --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 1.0 --seed 456 --max_tokens 1024 --num_test 9999 --collect_logprobs --output_dir output/exp_018_llama_scierc_seed456_r1024\\\"\", \"server\": \"autodl-5090\", \"seed\": 456, \"model_name\": \"LLaMA-3.1-8B-SciERC-merged\", \"model_path\": \"checkpoints/llama3.1-8b-scierc-merged\", \"dataset\": \"SciERC\", \"subtask\": \"joint\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"N\": 8, \"T\": 1, \"max_tokens\": 1024, \"is_new_inference\": true, \"checkpoint_path\": \"output/exp_018_llama_scierc_seed456_r1024/\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_018_llama_scierc_seed456_r1024.log\"}, \"server\": \"autodl-5090\", \"gpu\": \"cuda:1\", \"pid\": \"157584\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_018_llama_scierc_seed456_r1024.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-scierc-merged --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 1.0 --seed 456 --max_tokens 1024 --num_test 9999 --collect_logprobs --output_dir output/exp_018_llama_scierc_seed456_r1024\\\"\", \"finished_at\": \"2026-05-15T06:18:22.307Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T06:18:24.880896+00:00\"}]}, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_018_llama_scierc_seed456_r1024\", \"metrics\": {\"degen_rate\": 0.2741, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\", \"ner_greedy_f1\": 0.6597, \"ner_oracle_f1\": 0.7683, \"ner_oracle_headroom\": 0.1086, \"ner_cond_rho_fk\": 0.1472, \"ner_cond_rho_sj\": 0.2718, \"ner_cond_rho_logprob\": 0.083, \"ner_logprob_auroc_cond\": 0.5485, \"re_greedy_f1\": 0.4338, \"re_oracle_f1\": 0.5834, \"re_oracle_headroom\": 0.1496, \"re_cond_rho_fk\": 0.2107, \"re_cond_rho_sj\": 0.3898, \"re_cond_rho_logprob\": 0.1252, \"re_logprob_auroc_cond\": 0.6119, \"ner_structural_beats_logprob\": true, \"re_structural_beats_logprob\": true}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T06:21:45.350Z\", \"hypothesis\": \"LLaMA SciERC seed=456 (max_tokens=1024): multi-seed cross-model validation. Complements seed42 for LLaMA 3-seed protocol on SciERC NER+RE signal rankings.\"}, \"exp_018_llama_scierc_seed42_r1024\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T06:09:57.155Z\", \"updated_at\": \"2026-05-18T20:50:00.335Z\", \"spec\": {\"hypothesis\": \"D066 fresh rerun: LLaMA SciERC seed=42 with explicit max_tokens=1024. Replaces exp_007_llama_inference for clean 3-seed comparison.\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-scierc-merged --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 1.0 --seed 42 --max_tokens 1024 --num_test 9999 --collect_logprobs --output_dir output/exp_018_llama_scierc_seed42_r1024\\\"\", \"server\": \"autodl-5090\", \"seed\": 42, \"model_name\": \"LLaMA-3.1-8B-SciERC-merged\", \"model_path\": \"checkpoints/llama3.1-8b-scierc-merged\", \"dataset\": \"SciERC\", \"subtask\": \"joint\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"N\": 8, \"T\": 1, \"max_tokens\": 1024, \"is_new_inference\": true, \"checkpoint_path\": \"output/exp_018_llama_scierc_seed42_r1024/\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_018_llama_scierc_seed42_r1024.log\"}, \"server\": \"autodl-5090\", \"gpu\": \"cuda:0\", \"pid\": \"156809\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_018_llama_scierc_seed42_r1024.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-scierc-merged --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 1.0 --seed 42 --max_tokens 1024 --num_test 9999 --collect_logprobs --output_dir output/exp_018_llama_scierc_seed42_r1024\\\"\", \"finished_at\": \"2026-05-15T06:15:47.963Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T06:15:50.613872+00:00\"}]}, \"metrics\": {\"degen_rate\": 0.2495, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\", \"ner\": {\"full\": {\"SJ\": {\"rho\": 0.3096, \"tau\": 0.2288, \"auroc\": 0.6683}, \"FK\": {\"rho\": 0.2352, \"tau\": 0.1759, \"auroc\": 0.6069}, \"logprob\": {\"rho\": 0.1503, \"tau\": 0.1087, \"auroc\": 0.5318}, \"EM\": {\"rho\": 0.2587, \"tau\": 0.1966, \"auroc\": 0.7174}, \"voting_conf\": {\"rho\": 0.4053, \"tau\": 0.3042, \"auroc\": 0.6967}}, \"conditional\": {\"SJ\": {\"rho\": 0.2718, \"tau\": null, \"auroc\": 0.6565}, \"FK\": {\"rho\": 0.1472, \"tau\": null, \"auroc\": 0.5866}, \"logprob\": {\"rho\": 0.081, \"tau\": null, \"auroc\": 0.5129}, \"EM\": {\"rho\": 0.3165, \"tau\": null, \"auroc\": 0.7244}, \"voting_conf\": {\"rho\": 0.3078, \"tau\": null, \"auroc\": 0.6714}}, \"greedy_f1\": 0.6607, \"oracle_f1\": 0.7781, \"n_full\": 529, \"n_cond\": 478}, \"re\": {\"full\": {\"SJ\": {\"rho\": 0.2748, \"tau\": 0.2102, \"auroc\": 0.7244}, \"FK\": {\"rho\": 0.3027, \"tau\": 0.2337, \"auroc\": 0.691}, \"logprob\": {\"rho\": 0.3163, \"tau\": 0.233, \"auroc\": 0.6313}, \"EM\": {\"rho\": 0.1681, \"tau\": 0.1275, \"auroc\": 0.7697}, \"voting_conf\": {\"rho\": 0.384, \"tau\": 0.2965, \"auroc\": 0.7337}}, \"conditional\": {\"SJ\": {\"rho\": 0.3461, \"tau\": null, \"auroc\": 0.7233}, \"FK\": {\"rho\": 0.1969, \"tau\": null, \"auroc\": 0.6684}, \"logprob\": {\"rho\": 0.0888, \"tau\": null, \"auroc\": 0.5556}, \"EM\": {\"rho\": 0.4969, \"tau\": null, \"auroc\": 0.819}, \"voting_conf\": {\"rho\": 0.3433, \"tau\": null, \"auroc\": 0.7003}}, \"greedy_f1\": 0.4319, \"oracle_f1\": 0.5775, \"n_full\": 397, \"n_cond\": 251}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T06:21:47.660Z\", \"hypothesis\": \"LLaMA SciERC seed=42 (max_tokens=1024): cross-model validation on SciERC. Establishes LLaMA NER signal rankings on same dataset as Qwen for direct model-family comparison.\"}, \"exp_002_conll_n16\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:12:16.041Z\", \"updated_at\": \"2026-05-18T20:49:50.398Z\", \"spec\": {\"hypothesis\": \"Qwen CoNLL-2003 N=16: cross-dataset N-scaling comparison with SciERC N=16\", \"plan_id\": \"exp-002\", \"parent\": \"exp_002_ner_conll2003\", \"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=0 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 16 --temperature 1.0 --seed 42 --num_test 9999 --collect_logprobs --output_dir output/exp_002_conll_n16\", \"server\": \"autodl-5090\", \"data_path\": \"data/conll2003\", \"data_count\": 3453, \"model_name\": \"qwen3-8b-conll2003-merged\", \"seed\": 42}, \"conclusion\": \"success\", \"metrics\": {\"degen_rate\": 0.4844, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\", \"N\": 16, \"dataset\": \"conll2003\", \"subtask\": \"ner\", \"n_instances\": 3453, \"n_valid\": 2756, \"n_conditional\": 2614, \"greedy_f1\": 0.907, \"full\": {\"SJ_rho\": 0.4496, \"FK_rho\": 0.3928, \"logprob_rho\": 0.3146, \"EM_rho\": 0.4627, \"voting_conf_rho\": 0.4286, \"SJ_AUROC\": 0.8264, \"FK_AUROC\": 0.7821, \"logprob_AUROC\": 0.7531, \"EM_AUROC\": 0.8409, \"voting_conf_AUROC\": 0.8071, \"SJ_ECE\": 0.0747, \"FK_ECE\": 0.1786, \"logprob_ECE\": 0.2031, \"EM_ECE\": 0.0786, \"voting_conf_ECE\": 0.529}, \"conditional\": {\"SJ_rho\": 0.4208, \"FK_rho\": 0.3494, \"logprob_rho\": 0.3756, \"EM_rho\": 0.4658, \"voting_conf_rho\": 0.3654, \"SJ_AUROC\": 0.8405, \"FK_AUROC\": 0.7819, \"logprob_AUROC\": 0.8259, \"EM_AUROC\": 0.8781, \"voting_conf_AUROC\": 0.7951, \"SJ_ECE\": 0.0982, \"FK_ECE\": 0.1899, \"logprob_ECE\": 0.2504, \"EM_ECE\": 0.0997, \"voting_conf_ECE\": 0.6096}, \"n8_vs_n16_delta_rho_full\": {\"SJ\": 0.0139, \"FK\": -0.007, \"logprob\": -0.0011, \"EM\": 0.012, \"voting_conf\": 0.0049}}, \"checkpoint_path\": \"output/exp_002_conll_n16/samples.jsonl\", \"log_path\": \"output/exp_002_conll_n16.log\", \"completed_at\": \"2026-05-14T18:58:40.473Z\", \"hypothesis\": \"CoNLL N=16 NER: cross-dataset validation on high-performance NER dataset. Tests if structural signals retain advantage when base model performance is already high (greedy F1 > 0.9).\"}, \"exp_012_rerun_1024\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:11:33.777Z\", \"updated_at\": \"2026-05-18T20:49:42.395Z\", \"spec\": {\"hypothesis\": \"Verify if max_tokens=512 truncation inflated Table 1 N=8 SciERC signal values. Rerun with max_tokens=1024 for clean comparison.\", \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"dataset\": \"SciERC\", \"parent\": \"exp_012_logprob_baseline\", \"data_count\": 551, \"seed\": 42, \"server\": \"autodl-5090\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python3 code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 1.0 --max_tokens 1024 --seed 42 --num_test 9999 --collect_logprobs --output_dir output/exp_012_rerun_1024\", \"checkpoint_path\": \"output/exp_012_rerun_1024/\", \"log_path\": \"output/exp_012_rerun_1024/run.log\", \"data_path\": \"data/scierc/processed_data\"}, \"conclusion\": \"success\", \"metrics\": {\"degen_rate\": 0.1777, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\", \"ner_full\": {\"n\": 529, \"SJ\": {\"rho\": 0.3599, \"tau\": 0.2646, \"AUROC\": 0.6917, \"ECE\": 0.4531, \"rho_ci95\": [0.2732, 0.4389], \"AUROC_ci95\": [0.6304, 0.7406]}, \"FK\": {\"rho\": 0.2665, \"tau\": 0.1974, \"AUROC\": 0.629, \"ECE\": 0.4512, \"rho_ci95\": [0.1743, 0.3486], \"AUROC_ci95\": [0.5612, 0.6882]}, \"logprob\": {\"rho\": 0.2052, \"tau\": 0.1478, \"AUROC\": 0.5783, \"ECE\": 0.7064, \"rho_ci95\": [0.1171, 0.2904], \"AUROC_ci95\": [0.5179, 0.6387]}, \"EM\": {\"rho\": 0.2945, \"tau\": 0.2208, \"AUROC\": 0.7493, \"ECE\": 0.3526, \"rho_ci95\": [0.2094, 0.37], \"AUROC_ci95\": [0.7002, 0.7928]}, \"voting_conf\": {\"rho\": 0.3792, \"tau\": 0.2805, \"AUROC\": 0.6841, \"ECE\": 0.3807, \"rho_ci95\": [0.2972, 0.4486], \"AUROC_ci95\": [0.6249, 0.7366]}}, \"ner_cond\": {\"n\": 477, \"SJ\": {\"rho\": 0.3113, \"tau\": 0.2257, \"AUROC\": 0.6772, \"ECE\": 0.4416, \"rho_ci95\": [0.2353, 0.3959], \"AUROC_ci95\": [0.621, 0.7337]}, \"FK\": {\"rho\": 0.1761, \"tau\": 0.1284, \"AUROC\": 0.6078, \"ECE\": 0.4389, \"rho_ci95\": [0.0839, 0.2665], \"AUROC_ci95\": [0.5442, 0.6709]}, \"logprob\": {\"rho\": 0.1538, \"tau\": 0.1111, \"AUROC\": 0.5633, \"ECE\": 0.6803, \"rho_ci95\": [0.0637, 0.2424], \"AUROC_ci95\": [0.5032, 0.6232]}, \"EM\": {\"rho\": 0.3596, \"tau\": 0.2735, \"AUROC\": 0.7556, \"ECE\": 0.3257, \"rho_ci95\": [0.2819, 0.4408], \"AUROC_ci95\": [0.7011, 0.8107]}, \"voting_conf\": {\"rho\": 0.3, \"tau\": 0.2189, \"AUROC\": 0.6618, \"ECE\": 0.3746, \"rho_ci95\": [0.2168, 0.3836], \"AUROC_ci95\": [0.6004, 0.7201]}}, \"re_full\": {\"n\": 397, \"SJ\": {\"rho\": 0.2503, \"tau\": 0.1878, \"AUROC\": 0.6702, \"ECE\": 0.3865}, \"FK\": {\"rho\": 0.2752, \"tau\": 0.2117, \"AUROC\": 0.6089, \"ECE\": 0.4405}, \"logprob\": {\"rho\": 0.2662, \"tau\": 0.1951, \"AUROC\": 0.6005, \"ECE\": 0.7694}, \"EM\": {\"rho\": 0.1344, \"tau\": 0.1081, \"AUROC\": 0.7059, \"ECE\": 0.3548}, \"voting_conf\": {\"rho\": 0.3498, \"tau\": 0.2663, \"AUROC\": 0.6935, \"ECE\": 0.2724}}, \"re_cond\": {\"n\": 238, \"SJ\": {\"rho\": 0.2457, \"tau\": 0.1811, \"AUROC\": 0.6463, \"ECE\": 0.2941}, \"FK\": {\"rho\": 0.1139, \"tau\": 0.0876, \"AUROC\": 0.551, \"ECE\": 0.3424}, \"logprob\": {\"rho\": 0.0112, \"tau\": 0.0051, \"AUROC\": 0.5186, \"ECE\": 0.6464}, \"EM\": {\"rho\": 0.4165, \"tau\": 0.3256, \"AUROC\": 0.7515, \"ECE\": 0.2232}, \"voting_conf\": {\"rho\": 0.2409, \"tau\": 0.178, \"AUROC\": 0.642, \"ECE\": 0.207}}, \"delta_vs_512_ner_full_rho\": {\"SJ\": 0.0034, \"FK\": 0.0014, \"EM\": 0.0379, \"voting_conf\": -0.1226, \"logprob\": 0.0656}, \"provenance_note\": \"exp_015_v2 scierc_n8_logprob used exp_012_logprob (max_tokens=512 truncated data). voting_conf was inflated 0.502→0.379, logprob was suppressed 0.140→0.205.\"}, \"completed_at\": \"2026-05-14T23:10:33.075Z\", \"hypothesis\": \"Canonical SciERC baseline with max_tokens=1024: Qwen3-8B ft_002_v2, N=8, T=1.0, seed=42, joint NER+RE. Establishes ground-truth ρ rankings and selection F1 for all 5 signals under correct generation length.\"}, \"exp_llama_scierc_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T19:15:27.504Z\", \"updated_at\": \"2026-05-18T20:49:10.758Z\", \"hypothesis\": \"LLaMA-3.1-8B on SciERC with seed=456 will show consistent 5-signal ranking patterns (SJ/FK > logprob) and DGS selection gains comparable to seed=42 and seed=123, confirming cross-seed stability.\", \"spec\": {\"command\": \"python3 code/analyze_llama_scierc_seed456_5signal.py\", \"server\": \"autodl-5090\", \"data_path\": \"output/exp_018_llama_scierc_seed456/samples.jsonl\", \"data_count\": 551, \"model_name\": \"LLaMA-3.1-8B-Instruct\", \"seed\": 456, \"checkpoint_source\": \"same as seed123\", \"eval_data\": \"SciERC test (551 instances)\", \"checkpoint_path\": \"output/exp_018_llama_scierc_seed456/5signal_dgs_report.json\", \"log_path\": \"output/exp_018_llama_scierc_seed456/run.log\"}, \"metrics\": {\"greedy_f1\": 0.6457, \"oracle_f1\": 0.7574, \"headroom\": 0.1117, \"dgs_f1\": 0.6454, \"degen_rate\": 0.2741, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\", \"rho_SJ_full\": 0.3663, \"rho_FK_full\": 0.3115, \"rho_logprob_full\": 0.1911, \"rho_EM_full\": 0.3088, \"rho_vc_full\": 0.4135, \"auroc_SJ_full\": 0.7061, \"auroc_EM_full\": 0.7538, \"n_valid\": 529, \"n_conditional\": 478}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T19:16:00.973Z\"}, \"exp_007_llama_scierc_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T19:10:26.278Z\", \"updated_at\": \"2026-05-18T20:49:08.934Z\", \"name\": \"LLaMA-3.1-8B SciERC NER inference seed=123\", \"hypothesis\": \"Structural consistency signals (SJ, FK) correlate with entity F1 for LLaMA-8B on SciERC at seed=123, and DGS selection improves over greedy baseline\", \"spec\": {\"command\": \"python3 code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-scierc-merged --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 1.0 --seed 123 --num_test 9999 --collect_logprobs --output_dir output/exp_018_llama_scierc_seed123\", \"server\": \"autodl-5090\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"LLaMA-3.1-8B-Instruct (SciERC LoRA fine-tuned)\", \"seed\": 123, \"checkpoint_source\": \"checkpoints/llama3.1-8b-scierc-merged\", \"checkpoint_path\": \"checkpoints/llama3.1-8b-scierc-lora\", \"log_path\": \"output/exp_018_llama_scierc_seed123/report.json\"}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-18T19:11:30.781Z\", \"metrics\": {\"greedy_f1\": 0.6454, \"oracle_f1\": 0.7657, \"headroom\": 0.1204, \"degen_rate\": 0.2665, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\", \"dgs_delta_pp\": -0.38, \"rho_SJ_full\": 0.3552, \"rho_voting_conf_full\": 0.4193, \"auroc_SJ_full\": 0.7092, \"auroc_EM_full\": 0.7468}}, \"exp_qwen3_4b_conll_scs_inference\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:08:28.512Z\", \"updated_at\": \"2026-05-18T20:49:06.922Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-4b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 8 --temperature 1.0 --seed 42 --num_test 9999 --max_tokens 1024 --collect_logprobs --output_dir output/exp_qwen3_4b_conll_scs_inference\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"222184\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_qwen3_4b_conll_scs_inference/report.json\", \"submitted_at\": \"2026-05-15T19:10:19.757Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-4b-conll2003-merged\", \"wall_clock_seconds\": 523.8, \"gpu_hours\": 0.15}, \"metrics\": {\"greedy_f1\": 0.9251, \"oracle_f1\": 0.9408, \"oracle_headroom_pp\": 1.57, \"SJ_rho_full\": 0.4045, \"SJ_rho_cond\": 0.4306, \"FK_rho_full\": 0.3961, \"FK_rho_cond\": 0.42, \"LP_rho_full\": 0.3186, \"LP_rho_cond\": 0.3378, \"LP_auroc_full\": 0.7689, \"LP_auroc_cond\": 0.8153, \"fleiss_kappa_mean\": 0.9349, \"soft_jaccard_mean\": 0.9754, \"structural_beats_surface\": true, \"rho_advantage_pp\": 0.84, \"n_instances\": 3453, \"n_gold_empty_filtered\": 697, \"n_greedy_f1_zero_filtered\": 112, \"verdict\": \"MARGINAL\", \"degen_rate\": 0.9057, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T19:19:03.585Z\", \"notes\": \"4B CoNLL SCS inference completed. SJ>FK>LP ordering preserved at 4B scale (rho 0.405>0.396>0.319). Greedy F1=0.925 outperforms 8B (0.907), but SJ rho is lower (0.405 vs 0.450 at 8B N=16). Structural beats surface confirmed (+0.84pp). Verdict MARGINAL due to small oracle headroom (1.57pp) — the model is already very good at CoNLL, leaving little room for selection improvement.\", \"hypothesis\": \"CoNLL 4B SCS inference (checkpoint-3800): cross-scale evidence for correlation-selection gap. Tests if structural>surface ranking and LP compression hold at smaller model scale on high-degeneracy dataset.\"}, \"exp_qwen3_4b_conll_scs_inference_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:41:33.501Z\", \"updated_at\": \"2026-05-18T20:49:03.705Z\", \"hypothesis\": \"CoNLL 4B SCS inference with best checkpoint-4200 (from resume training). Scale ablation: cross-scale evidence for correlation-selection gap. Compare vs v1 (ckpt-3800 baseline: greedy_f1=0.9251, SJ_rho=0.4045).\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python code/run_mvp_pilot.py --model_path checkpoints/qwen3-4b-conll2003-merged-ckpt4200 --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 8 --temperature 1.0 --seed 42 --num_test 9999 --max_tokens 1024 --collect_logprobs --output_dir output/exp_qwen3_4b_conll_scs_inference_v2\", \"server\": \"autodl-5090\", \"data_path\": \"data/conll2003\", \"data_count\": 3453, \"model_name\": \"Qwen3-4B (LoRA checkpoint-4200 merged)\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/qwen3-4b-conll2003-lora/checkpoint-4200\", \"gpu\": [\"cuda:1\"], \"checkpoint_path\": \"checkpoints/qwen3-4b-conll2003-merged-ckpt4200\", \"log_path\": \"/tmp/infer_4b_conll_v2.log\", \"account\": \"root\", \"backend\": \"tmux\", \"tmux_session\": \"exp_4b_conll_scs_v2\"}, \"metrics\": {\"greedy_f1\": 0.9234, \"oracle_f1\": 0.9404, \"oracle_headroom_pp\": 1.7, \"SJ_rho_full\": 0.4217, \"SJ_rho_cond\": 0.459, \"FK_rho_full\": 0.4181, \"FK_rho_cond\": 0.4538, \"LP_rho_full\": 0.3313, \"LP_rho_cond\": 0.3487, \"LP_auroc_full\": 0.7761, \"LP_auroc_cond\": 0.8209, \"n_instances\": 3453, \"verdict\": \"MARGINAL\", \"degen_rate\": 0.9057, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T19:54:14.575Z\", \"notes\": \"Gold-filter audit (2026-05-16): CONSISTENT. _full metrics (SJ_rho=0.4217, FK_rho=0.4181) are computed on gold-filtered set (n=2756), same as 8B Table 1 values. _full does NOT mean all 3453 instances — it means gold-nonempty instances. _cond further excludes greedy-F1=0 (n=2641). Confirmed via run_mvp_pilot.py source code and report.json n values.\"}, \"exp_qwen3_4b_scierc_scs_inference\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:45:33.384Z\", \"updated_at\": \"2026-05-18T20:49:01.260Z\", \"hypothesis\": \"SciERC 4B SCS inference after v4 finetune merge. Complete 2x2 scale matrix (4B SciERC cell). Cross-scale + cross-task evidence for correlation-selection gap.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-4b-scierc-merged --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 1.0 --seed 42 --num_test 9999 --max_tokens 1024 --collect_logprobs --output_dir output/exp_qwen3_4b_scierc_scs_inference\", \"server\": \"autodl-5090\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"qwen3-4b-scierc-merged (checkpoint-400)\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/qwen3-4b-scierc-merged\", \"eval_data\": \"scierc test set\"}, \"metrics\": {\"ner_greedy_f1\": 0.6612, \"ner_oracle_f1\": 0.7839, \"ner_headroom_pp\": 12.28, \"ner_SJ_rho\": 0.4221, \"ner_FK_rho\": 0.3258, \"ner_LP_rho\": 0.28, \"re_greedy_f1\": 0.4136, \"re_oracle_f1\": 0.5846, \"re_headroom_pp\": 17.1, \"re_SJ_rho\": 0.2673, \"re_FK_rho\": 0.3593, \"re_LP_rho\": 0.3512, \"re_sample_f1_pct_zero\": 0.476, \"re_LP_rho_cond\": 0.1135, \"re_LP_rho_cond_p\": 0.074, \"degen_rate\": 0.104, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\"}, \"checkpoint_path\": \"checkpoints/qwen3-4b-scierc-merged/\", \"log_path\": \"/tmp/exp_qwen3_4b_scierc_scs_inference.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T20:00:03.730Z\"}, \"exp_027_fewnerd_n16\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T05:28:57.036Z\", \"updated_at\": \"2026-05-18T20:48:58.455Z\", \"spec\": {\"hypothesis\": \"LP selection scales with N in low-degeneracy regime: N=16 should yield LP Δ > +2pp (vs N=8 +1.36pp) on Few-NERD (10% degen), because more samples increase oracle headroom while LP ranking remains effective.\", \"parent\": \"exp_021_fewnerd_full\", \"model_name\": \"qwen3-8b-fewnerd-exp021-merged\", \"data_path\": \"data/fewnerd_n16_subset/test.json\", \"data_count\": 5000, \"seed\": 42, \"server\": \"autodl-5090\", \"gpu\": \"cuda:0,cuda:1,cuda:2,cuda:3\", \"command\": \"python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-fewnerd-exp021-merged --data_dir data/fewnerd_n16_subset --dataset fewnerd --subtask ner --n_samples 16 --temperature 1.0 --seed 42 --collect_logprobs --start_index {0,1250,2500,3750} --end_index {1250,2500,3750,5000} --output_dir output/exp_027_fewnerd_n16/shard_{0-3}\", \"checkpoint_path\": \"output/exp_027_fewnerd_n16/sampled_results.jsonl\", \"log_path\": \"output/exp_027_fewnerd_n16/\"}, \"conclusion\": \"success\", \"metrics\": {\"LP_delta_pp\": 1.88, \"LP_delta_95CI\": [1.41, 2.37], \"degen_rate\": 0.0706, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\", \"greedy_f1\": 0.7478, \"lp_sel_f1\": 0.7666, \"oracle_f1\": 0.902, \"headroom_pp\": 15.42, \"all_8_types_positive\": true, \"n_instances\": 5000, \"N_samples\": 16, \"bootstrap_p\": \"<0.001\"}, \"hypothesis\": \"LP selection scales with N in low-degeneracy regime: N=16 should yield LP Δ > +2pp (vs N=8 +1.36pp) on Few-NERD (10% degen), because more samples increase oracle headroom while LP ranking remains effective.\", \"completed_at\": \"2026-05-17T05:46:48.460Z\"}, \"exp_026_t12\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T13:18:18.780Z\", \"updated_at\": \"2026-05-18T20:48:24.965Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --n_samples 8 --temperature 1.2 --seed 42 --max_tokens 1024 --collect_logprobs --output_dir output/exp_026_t12\", \"server\": \"autodl-5090\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 42, \"log_path\": \"output/exp_026_t12.log\", \"checkpoint_path\": \"checkpoints/qwen3-8b-scierc-merged-v2\"}, \"conclusion\": \"success\", \"metrics\": {\"temperature\": 1.2, \"task\": \"T-ablation\", \"degen_rate\": 0.1493, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\"}, \"completed_at\": \"2026-05-16T14:26:37.648Z\", \"hypothesis\": \"Temperature T=1.2 ablation on SciERC: test if higher temperature increases sample diversity (lower degeneracy) and LP discriminative range, potentially improving LP selection while maintaining structural signal effectiveness.\", \"parent\": \"exp_012_rerun_1024\"}, \"exp_026_t08\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T12:57:46.027Z\", \"updated_at\": \"2026-05-18T20:48:24.112Z\", \"spec\": {\"checkpoint_path\": \"checkpoints/qwen3-8b-scierc-merged-v2\", \"log_path\": \"output/exp_026_t08/run.log\"}, \"conclusion\": \"success\", \"metrics\": {\"temperature\": 0.8, \"task\": \"T-ablation\", \"degen_rate\": 0.2382, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\"}, \"completed_at\": \"2026-05-16T14:26:36.243Z\", \"hypothesis\": \"Temperature T=0.8 ablation on SciERC: test if lower temperature increases LP compression (narrower range) while structural signals remain robust, supporting the claim that LP compression is intrinsic rather than temperature-driven.\", \"parent\": \"exp_012_rerun_1024\"}, \"exp_026_t05\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T12:19:35.753Z\", \"updated_at\": \"2026-05-18T20:48:23.339Z\", \"spec\": {\"checkpoint_path\": \"checkpoints/qwen3-8b-scierc-merged-v2\", \"log_path\": \"output/exp_026_t05/run.log\"}, \"conclusion\": \"success\", \"metrics\": {\"temperature\": 0.5, \"task\": \"T-ablation\", \"degen_rate\": 0.414, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\"}, \"completed_at\": \"2026-05-16T14:26:34.808Z\", \"hypothesis\": \"Temperature T=0.5 ablation on SciERC: extreme low temperature expected to maximally compress LP scores and increase degeneracy, providing upper-bound evidence for LP compression as model-intrinsic phenomenon.\", \"parent\": \"exp_012_rerun_1024\"}, \"exp_026_T12\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T09:38:31.060Z\", \"updated_at\": \"2026-05-18T20:48:22.668Z\", \"hypothesis\": \"T=1.2 will decrease degeneracy rate and expand LP range vs T=1.0, but may degrade generation quality (lower greedy F1). Tests whether reducing degeneracy via higher T recovers selection headroom or if quality degradation offsets the benefit.\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:3\", \"account\": \"root\", \"reproduce\": {\"server\": \"autodl-5090\", \"gpu\": \"cuda:3\", \"started_at\": \"2026-05-17T09:39:51.733Z\", \"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/autodl-tmp/struct_self_consist_ie && python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 1.2 --seed 42 --output_dir output/exp_026_T12/ --num_test 9999 --collect_logprobs 2>&1 | tee output/exp_026_T12_run.log\\\"\", \"finished_at\": \"2026-05-17T09:48:04.019Z\", \"training_hours\": 0.14}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/autodl-tmp/struct_self_consist_ie && python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 1.2 --seed 42 --output_dir output/exp_026_T12/ --num_test 9999 --collect_logprobs 2>&1 | tee output/exp_026_T12_run.log\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:3\"], \"pid\": \"381369\", \"log_path\": \"output/exp_026_T12_run.log\", \"submitted_at\": \"2026-05-17T09:41:39.393Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"output/exp_026_T12/\", \"wall_clock_seconds\": 1114.4, \"gpu_hours\": 0.31}, \"pid\": \"381369\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_026_T12.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T09:48:08.312470+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"degen_rate\": 0.1493, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\", \"lp_range_mean\": 0.075, \"lp_range_std\": 0.059, \"within_instance_rho_mean\": 0.2245, \"within_instance_rho_median\": 0.3152, \"within_instance_rho_valid_pct\": 0.875, \"greedy_f1\": 0.62, \"oracle_f1\": 0.758, \"lp_sel_f1\": 0.621, \"sj_sel_f1\": 0.597, \"em_sel_f1\": 0.596, \"vc_sel_f1\": 0.582, \"sj_rho\": 0.384, \"fk_rho\": 0.386, \"lp_rho\": 0.182, \"vc_rho\": 0.342, \"sj_auroc\": 0.683, \"lp_auroc\": 0.566}, \"completed_at\": \"2026-05-17T10:00:13.771Z\"}, \"exp_026_T08\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T09:38:29.602Z\", \"updated_at\": \"2026-05-18T20:48:21.975Z\", \"hypothesis\": \"T=0.8 will show intermediate degeneracy between T=0.5 and T=1.0, establishing a monotonic degeneracy-temperature relationship. If LP selection improves at T=0.8 vs T=1.0, it identifies the optimal operating point for the selection mechanism.\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:2\", \"account\": \"root\", \"reproduce\": {\"server\": \"autodl-5090\", \"gpu\": \"cuda:2\", \"started_at\": \"2026-05-17T09:39:50.780Z\", \"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/autodl-tmp/struct_self_consist_ie && python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 0.8 --seed 42 --output_dir output/exp_026_T08/ --num_test 9999 --collect_logprobs 2>&1 | tee output/exp_026_T08_run.log\\\"\", \"finished_at\": \"2026-05-17T09:47:56.543Z\", \"training_hours\": 0.13}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/autodl-tmp/struct_self_consist_ie && python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 0.8 --seed 42 --output_dir output/exp_026_T08/ --num_test 9999 --collect_logprobs 2>&1 | tee output/exp_026_T08_run.log\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"380680\", \"log_path\": \"output/exp_026_T08_run.log\", \"submitted_at\": \"2026-05-17T09:41:20.812Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"output/exp_026_T08/\", \"wall_clock_seconds\": 1131.4, \"gpu_hours\": 0.31}, \"pid\": \"380680\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_026_T08.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T09:48:02.635244+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"degen_rate\": 0.2382, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\", \"lp_range_mean\": 0.043, \"lp_range_std\": 0.042, \"within_instance_rho_mean\": 0.1701, \"within_instance_rho_median\": 0.2635, \"within_instance_rho_valid_pct\": 0.728, \"greedy_f1\": 0.616, \"oracle_f1\": 0.737, \"lp_sel_f1\": 0.627, \"sj_sel_f1\": 0.619, \"em_sel_f1\": 0.611, \"vc_sel_f1\": 0.603, \"sj_rho\": 0.378, \"fk_rho\": 0.34, \"lp_rho\": 0.212, \"vc_rho\": 0.352, \"sj_auroc\": 0.662, \"lp_auroc\": 0.571}, \"completed_at\": \"2026-05-17T10:00:12.248Z\"}, \"exp_026_T05\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T09:38:28.066Z\", \"updated_at\": \"2026-05-18T20:48:16.286Z\", \"hypothesis\": \"T=0.5 will increase degeneracy rate (more deterministic outputs) and compress LP range on SciERC, reducing selection headroom. Maps the low-temperature end of the degeneracy-temperature frontier, validating that degeneracy is regime-dependent on sampling temperature.\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/autodl-tmp/struct_self_consist_ie && python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 0.5 --seed 42 --output_dir output/exp_026_T05/ --num_test 9999 --collect_logprobs 2>&1 | tee output/exp_026_T05_run.log\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:1\"], \"pid\": \"380188\", \"log_path\": \"output/exp_026_T05_run.log\", \"submitted_at\": \"2026-05-17T09:40:51.787Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"output/exp_026_T05/\", \"wall_clock_seconds\": 1158.3, \"gpu_hours\": 0.32}, \"server\": \"autodl-5090\", \"gpu\": \"cuda:1\", \"pid\": \"380188\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_026_T05.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/autodl-tmp/struct_self_consist_ie && python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 0.5 --seed 42 --output_dir output/exp_026_T05/ --num_test 9999 --collect_logprobs 2>&1 | tee output/exp_026_T05_run.log\\\"\", \"finished_at\": \"2026-05-17T09:47:31.332Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T09:47:35.127151+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"degen_rate\": 0.414, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\", \"lp_range_mean\": 0.022, \"lp_range_std\": 0.021, \"within_instance_rho_mean\": 0.1306, \"within_instance_rho_median\": 0.2182, \"within_instance_rho_valid_pct\": 0.597, \"greedy_f1\": 0.617, \"oracle_f1\": 0.71, \"lp_sel_f1\": 0.622, \"sj_sel_f1\": 0.622, \"em_sel_f1\": 0.619, \"vc_sel_f1\": 0.61, \"sj_rho\": 0.333, \"fk_rho\": 0.341, \"lp_rho\": 0.208, \"vc_rho\": 0.353, \"sj_auroc\": 0.644, \"lp_auroc\": 0.577}, \"completed_at\": \"2026-05-17T10:00:10.083Z\"}, \"exp_017_llama_conll_n16_s123_r1024\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:17:02.953Z\", \"updated_at\": \"2026-05-18T20:47:52.122Z\", \"spec\": {\"hypothesis\": \"D054 rerun: max_tokens=1024. Verify truncation impact on LLaMA CoNLL N=16 seed123.\", \"parent\": \"exp_017_llama_conll_n16_s123\", \"model_name\": \"llama3.1-8b-conll2003-merged\", \"dataset\": \"CoNLL-2003\", \"seed\": 123, \"server\": \"autodl-5090\", \"command\": \"python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 16 --temperature 1.0 --seed 123 --num_test 9999 --max_tokens 1024 --collect_logprobs --output_dir output/exp_017_llama_conll_n16_s123_r1024\", \"data_path\": \"data/conll2003\", \"data_count\": 3453}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T01:20:51.219Z\", \"notes\": \"Output exists on autodl-5090. Registry status corrected from killed to success.\", \"hypothesis\": \"LLaMA CoNLL N=16 seed=123 (max_tokens=1024 rerun): cross-model multi-seed validation. Confirms structural>surface ordering is stable across seeds for LLaMA on CoNLL after gold-filtering correction.\", \"metrics\": {\"degen_rate\": 0.8636, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\"}}, \"exp_018_llama_scierc_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T06:07:14.370Z\", \"updated_at\": \"2026-05-18T20:47:51.435Z\", \"spec\": {\"hypothesis\": \"Multi-seed robustness: LLaMA SciERC N=8 seed=123, max_tokens=1024. Verify signal stability across seeds.\", \"command\": \"python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-scierc-merged --data_dir data/scierc/processed_data --dataset scierc --subtask joint --seed 123 --n_samples 8 --temperature 1.0 --max_tokens 1024 --output_dir output/exp_018_llama_scierc_seed123\", \"server\": \"autodl-5090\", \"seed\": 123, \"model_name\": \"LLaMA-3.1-8B-SciERC-merged\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"checkpoint_path\": \"output/exp_018_llama_scierc_seed123/\", \"log_path\": \"output/exp_018_llama_scierc_seed123.log\", \"samples_md5\": \"072eeca68236d46b4c5c84b945209abc\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T06:08:04.855Z\", \"hypothesis\": \"LLaMA SciERC seed=123: multi-seed cross-model validation. Complements seed42 for LLaMA 3-seed protocol on SciERC NER+RE signal rankings.\", \"metrics\": {\"degen_rate\": 0.2665, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\"}}, \"exp_018_qwen_scierc_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T06:07:13.570Z\", \"updated_at\": \"2026-05-18T20:47:50.032Z\", \"spec\": {\"hypothesis\": \"Multi-seed robustness: Qwen SciERC N=8 seed=456, max_tokens=1024. Verify signal stability across seeds.\", \"command\": \"python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --seed 456 --n_samples 8 --temperature 1.0 --max_tokens 1024 --output_dir output/exp_018_qwen_scierc_seed456\", \"server\": \"autodl-5090\", \"seed\": 456, \"model_name\": \"Qwen3-8B-SciERC-merged-v2\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"checkpoint_path\": \"output/exp_018_qwen_scierc_seed456/\", \"log_path\": \"output/exp_018_qwen_scierc_seed456/run.log\", \"samples_md5\": \"46d0de47ad7693c07e7df3a77c90c3be\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T06:08:03.898Z\", \"hypothesis\": \"Qwen SciERC seed=456: multi-seed Qwen validation. Part of 3-seed protocol (seed42=exp_012_rerun_1024, seed123, seed456) for statistical significance of signal rankings.\", \"metrics\": {\"degen_rate\": 0.2042, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\"}}, \"exp_018_qwen_scierc_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T06:07:12.747Z\", \"updated_at\": \"2026-05-18T20:47:49.306Z\", \"spec\": {\"hypothesis\": \"Multi-seed robustness: Qwen SciERC N=8 seed=123, max_tokens=1024. Verify signal stability across seeds.\", \"command\": \"python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --seed 123 --n_samples 8 --temperature 1.0 --max_tokens 1024 --output_dir output/exp_018_qwen_scierc_seed123\", \"server\": \"autodl-5090\", \"seed\": 123, \"model_name\": \"Qwen3-8B-SciERC-merged-v2\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"checkpoint_path\": \"output/exp_018_qwen_scierc_seed123/\", \"log_path\": \"output/exp_018_qwen_scierc_seed123.log\", \"samples_md5\": \"866a59581dea56f4633149f0b18a31ae\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T06:08:02.954Z\", \"hypothesis\": \"Qwen SciERC seed=123: multi-seed Qwen validation. Part of 3-seed protocol (seed42=exp_012_rerun_1024, seed123, seed456) for statistical significance of signal rankings.\", \"metrics\": {\"degen_rate\": 0.172, \"degen_rate_source\": \"unified_metrics_constant_f1_gold_filtered\"}}, \"exp_epoch_dgs_analysis\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T19:59:57.921Z\", \"updated_at\": \"2026-05-18T20:01:46.134Z\", \"hypothesis\": \"DGS benefit is strictly monotonic with degeneracy rate: higher degeneracy → greater DGS improvement, validating that degeneracy rate is the key gating signal\", \"spec\": {\"command\": \"python3 code/epoch_dgs_analysis.py\", \"server\": \"autodl-5090\", \"data_path\": \"/root/struct_self_consist_ie/data/\", \"data_count\": \"all datasets\", \"model_name\": \"Qwen3-8B\", \"seed\": 42}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/struct_self_consist_ie/output/epoch_dgs_analysis_results.json\", \"log_path\": \"/root/struct_self_consist_ie/output/epoch_dgs_analysis_results.json\", \"completed_at\": \"2026-05-18T20:01:46.134Z\"}, \"exp_diagnostic_calibration\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T19:59:56.064Z\", \"updated_at\": \"2026-05-18T20:01:44.364Z\", \"hypothesis\": \"A 3-indicator regression model (degeneracy rate, LP-F1 correlation, LP range) can quantitatively predict the optimal LP selection delta for unseen instances\", \"spec\": {\"command\": \"python3 code/diagnostic_calibration.py\", \"server\": \"autodl-5090\", \"data_path\": \"/root/struct_self_consist_ie/data/\", \"data_count\": \"all datasets\", \"model_name\": \"Qwen3-8B\", \"seed\": 42}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/struct_self_consist_ie/output/diagnostic_calibration_results.json\", \"log_path\": \"/root/struct_self_consist_ie/output/diagnostic_calibration_results.json\", \"completed_at\": \"2026-05-18T20:01:44.364Z\"}, \"exp_adaptive_temperature\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T19:59:52.771Z\", \"updated_at\": \"2026-05-18T20:01:42.646Z\", \"hypothesis\": \"Adjusting sampling temperature based on instance-level confidence indicators can improve output diversity-quality tradeoff\", \"spec\": {\"command\": \"python3 code/adaptive_temperature.py\", \"server\": \"autodl-5090\", \"data_path\": \"/root/struct_self_consist_ie/data/\", \"data_count\": \"all datasets\", \"model_name\": \"Qwen3-8B\", \"seed\": 42}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/struct_self_consist_ie/output/adaptive_temperature_results.json\", \"log_path\": \"/root/struct_self_consist_ie/output/adaptive_temperature_results.json\", \"completed_at\": \"2026-05-18T20:01:42.646Z\"}, \"exp_entity_consensus\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T19:59:50.628Z\", \"updated_at\": \"2026-05-18T20:01:40.869Z\", \"hypothesis\": \"Constructing new output from N samples using entity frequency thresholds and LP-weighted decisions can capture complementary information that single-sample selection misses\", \"spec\": {\"command\": \"python3 code/entity_consensus.py\", \"server\": \"autodl-5090\", \"data_path\": \"/root/struct_self_consist_ie/data/\", \"data_count\": \"all datasets\", \"model_name\": \"Qwen3-8B\", \"seed\": 42}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/struct_self_consist_ie/output/entity_consensus_results.json\", \"log_path\": \"/root/struct_self_consist_ie/output/entity_consensus_results.json\", \"completed_at\": \"2026-05-18T20:01:40.869Z\"}, \"exp_ccs_selection\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T19:59:48.671Z\", \"updated_at\": \"2026-05-18T20:01:39.128Z\", \"hypothesis\": \"Three-stage cascaded selection (degen→greedy, low-LP-range→entity MV, high-LP-range→LP) can outperform single-strategy selection by adapting to local confidence patterns\", \"spec\": {\"command\": \"python3 code/ccs_selection.py\", \"server\": \"autodl-5090\", \"data_path\": \"/root/struct_self_consist_ie/data/\", \"data_count\": \"all datasets\", \"model_name\": \"Qwen3-8B\", \"seed\": 42}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/struct_self_consist_ie/output/ccs_selection_results.json\", \"log_path\": \"/root/struct_self_consist_ie/output/ccs_selection_results.json\", \"completed_at\": \"2026-05-18T20:01:39.128Z\"}, \"exp_017_llama_conll\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-14T14:39:32.014Z\", \"updated_at\": \"2026-05-18T19:11:03.240Z\", \"completed_at\": \"2026-05-14T17:12:15.687Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\"}}, \"hypothesis\": \"On CoNLL (high degeneracy regime), LLaMA should show the same pattern as Qwen3: LP selection fails due to narrow headroom, but structural signals retain diagnostic value (QE rho). Cross-model validation of the degeneracy-driven signal effectiveness framework.\", \"parent\": \"exp_007_llama_inference\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"autodl-5090\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-17T11:30:53.467Z\"}, \"metrics\": {\"degeneracy_cf1_gold_filtered\": 0.894, \"n_constant_f1\": 2465, \"n_gold_filtered\": 2756, \"n_total\": 3453, \"greedy_f1\": 0.9239, \"oracle_f1\": 0.9451, \"random_f1\": 0.9207, \"headroom_pp\": 2.11, \"dgs_f1\": 0.9254, \"dgs_delta_pp\": 0.14, \"dgs_nondegen_lp_delta_pp\": 1.37, \"selection_f1\": {\"SJ\": {\"f1\": 0.9237, \"delta_pp\": -0.04}, \"FK\": {\"f1\": 0.924, \"delta_pp\": -0.02}, \"VC\": {\"f1\": 0.925, \"delta_pp\": 0.08}, \"EM\": {\"f1\": 0.9244, \"delta_pp\": 0.02}, \"LP\": {\"f1\": 0.9244, \"delta_pp\": 0.02}}, \"qe_rho_full_3seed\": {\"SJ\": {\"mean\": 0.4631, \"sd\": 0.0074}, \"FK\": {\"mean\": 0.4546, \"sd\": 0.0061}, \"EM\": {\"mean\": 0.4603, \"sd\": 0.0078}, \"VC\": {\"mean\": 0.4579, \"sd\": 0.003}, \"LP\": {\"mean\": 0.3099, \"sd\": 0.0055}}, \"qe_auroc_full_3seed\": {\"SJ\": {\"mean\": 0.736, \"sd\": 0.0064}, \"FK\": {\"mean\": 0.732, \"sd\": 0.0063}, \"EM\": {\"mean\": 0.7355, \"sd\": 0.0069}, \"VC\": {\"mean\": 0.7394, \"sd\": 0.0041}, \"LP\": {\"mean\": 0.7629, \"sd\": 0.0044}}, \"lp_range\": {\"mean\": 0.0198, \"std\": 0.0315, \"median\": 0.0002}}, \"conclusion\": \"success\", \"spec\": {\"command\": \"python code/exp017_full_signal_analysis.py\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll_infer/samples.jsonl\", \"data_count\": 3453, \"model_name\": \"llama3.1-8b-conll2003-merged\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll_infer/\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll_infer/full_signal_analysis.json\"}}, \"exp_017_llama_conll_finetune\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T16:47:36.156Z\", \"updated_at\": \"2026-05-18T18:43:42.649Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=0 llamafactory-cli train train_config_llama_conll2003_3ep.yaml\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"674921\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_017_llama_conll_finetune.log\", \"submitted_at\": \"2026-05-18T16:47:35.786Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/conll2003/llmfactory_train.json\", \"data_count\": 14037, \"model_name\": \"Meta-Llama-3.1-8B-Instruct\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/llama3.1-8b-conll2003-lora-3ep\", \"checkpoint_source\": \"Meta-Llama-3.1-8B-Instruct (base model, LoRA from scratch)\", \"eval_data\": \"conll2003_uie_dev\", \"wall_clock_seconds\": 6176.5, \"gpu_hours\": 1.72}, \"hypothesis\": \"Structural self-consistency QE signals (SJ, FK, VC, EM) show model-agnostic diagnostic power: their Spearman rho with per-instance F1 should be comparable on LLaMA 3.1-8B as on Qwen 2.5-7B for CoNLL-2003 NER, even though degeneracy rates and absolute F1 may differ.\", \"parent\": \"exp_llama_fewnerd_lora\", \"conclusion\": \"success\", \"metrics\": {\"degeneracy_rate\": 0.853, \"greedy_f1\": 0.928, \"oracle_f1\": 0.951, \"headroom\": 0.023, \"selection_f1\": 0.934, \"full_rho_SJ\": 0.45, \"full_rho_FK\": 0.443, \"full_rho_VC\": 0.437, \"full_rho_EM\": 0.448, \"full_rho_LP\": 0.273, \"full_AUROC_SJ\": 0.752, \"full_AUROC_EM\": 0.753, \"full_AUROC_LP\": 0.739, \"cond_rho_SJ\": 0.454, \"cond_rho_EM\": 0.458, \"cond_rho_LP\": 0.311, \"cond_AUROC_EM\": 0.783, \"cond_AUROC_LP\": 0.804}, \"completed_at\": \"2026-05-18T18:30:32.331Z\"}, \"exp_028_entity_token_lp\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T18:22:18.594Z\", \"updated_at\": \"2026-05-18T18:23:06.601Z\", \"hypothesis\": \"Full-sequence mean LP underperforms as a quality signal because format/schema tokens dilute the entity-relevant logprob signal; isolating entity-only tokens should yield higher QE correlation and selection F1.\", \"conclusion\": \"negative\", \"spec\": {\"command\": \"python code/exp028_entity_token_lp_analysis.py\", \"server\": \"autodl-5090\", \"data_path\": \"output/exp_entity_token_lp/scierc/samples.jsonl\", \"data_count\": 529, \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 42, \"checkpoint_path\": \"checkpoints/qwen3-8b-scierc-merged-v2\", \"log_path\": \"output/exp_028_entity_token_lp/analysis_results.json\"}, \"completed_at\": \"2026-05-18T18:22:59.312Z\", \"metrics\": {\"greedy_f1\": 0.643, \"oracle_f1\": 0.7845, \"full_lp_global_rho\": 0.2971, \"entity_text_type_lp_global_rho\": 0.4401, \"full_lp_selection_f1\": 0.6465, \"entity_text_type_lp_selection_f1\": 0.6357, \"dilution_ratio\": 0.32, \"full_lp_within_range_median\": 0.0402, \"entity_text_type_within_range_median\": 0.1346, \"schema_only_within_range_median\": 0.0089}}, \"exp_026_t12_scierc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T15:28:36.812Z\", \"updated_at\": \"2026-05-18T15:30:33.407Z\", \"hypothesis\": \"Higher temperature (T=1.2) reduces degeneracy rate and increases LP range on SciERC NER, but may degrade absolute generation quality\", \"spec\": {\"command\": \"python code/analyze_exp026_temp_5signal.py --data_path output/exp_026_t12/samples.jsonl --output_dir output/exp_026_t12/\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:3\"], \"pid\": \"665522\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_026_t12_scierc.log\", \"submitted_at\": \"2026-05-18T15:28:56.997Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"output/exp_026_t12/samples.jsonl\", \"data_count\": 551, \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 42, \"checkpoint_path\": \"checkpoints/qwen3-8b-scierc-merged-v2\", \"checkpoint_source\": \"ft_002_v2\", \"eval_data\": \"scierc_test_551\", \"wall_clock_seconds\": 96.4, \"gpu_hours\": 0.03}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T15:30:33.407Z\"}, \"exp_026_t08_scierc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T15:28:36.084Z\", \"updated_at\": \"2026-05-18T15:30:31.219Z\", \"hypothesis\": \"Moderate temperature (T=0.8) provides intermediate degeneracy/LP-range tradeoff on SciERC NER, testing sensitivity of structural signals to temperature\", \"spec\": {\"command\": \"python code/analyze_exp026_temp_5signal.py --data_path output/exp_026_t08/samples.jsonl --output_dir output/exp_026_t08/\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"665386\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_026_t08_scierc.log\", \"submitted_at\": \"2026-05-18T15:28:55.394Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"output/exp_026_t08/samples.jsonl\", \"data_count\": 551, \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 42, \"checkpoint_path\": \"checkpoints/qwen3-8b-scierc-merged-v2\", \"checkpoint_source\": \"ft_002_v2\", \"eval_data\": \"scierc_test_551\", \"wall_clock_seconds\": 95.8, \"gpu_hours\": 0.03}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T15:30:31.219Z\"}, \"exp_026_t05_scierc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T15:28:34.135Z\", \"updated_at\": \"2026-05-18T15:30:28.965Z\", \"hypothesis\": \"Lower temperature (T=0.5) increases degeneracy rate and reduces LP range on SciERC NER, as reduced sampling diversity causes more identical outputs\", \"spec\": {\"command\": \"python code/analyze_exp026_temp_5signal.py --data_path output/exp_026_t05/samples.jsonl --output_dir output/exp_026_t05/\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"665248\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_026_t05_scierc.log\", \"submitted_at\": \"2026-05-18T15:28:53.787Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"output/exp_026_t05/samples.jsonl\", \"data_count\": 551, \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 42, \"checkpoint_path\": \"checkpoints/qwen3-8b-scierc-merged-v2\", \"checkpoint_source\": \"ft_002_v2\", \"eval_data\": \"scierc_test_551\", \"wall_clock_seconds\": 95.2, \"gpu_hours\": 0.03}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-18T15:30:28.965Z\"}, \"exp_027_mlp_verifier\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-18T06:39:22.524Z\", \"updated_at\": \"2026-05-18T06:41:51.069Z\", \"metrics\": {\"lr_auroc\": 0.6522, \"mlp_auroc\": 0.6381, \"rf_auroc\": 0.5868, \"mlp_15feat_auroc\": 0.6341, \"lr_sel_f1\": 0.6406, \"mlp_sel_f1\": 0.6278, \"greedy_f1\": 0.6441, \"oracle_f1\": 0.8231, \"best_single_signal_auroc\": 0.6476, \"feature_bottleneck_confirmed\": true}, \"hypothesis\": \"MLP/RF等非线性模型能否通过组合5个QE信号(LP,SJ,FK,EM,VC)超越LR，或通过cross-signal interactions提取额外信息，从而缩小selection gap\", \"spec\": {\"command\": \"python train_mlp_verifier.py --n_samples 16 --cv_folds 5 --seeds 42,123,456\", \"server\": \"a100\", \"data_path\": \"output/exp_001_n16_seed*/samples.jsonl\", \"data_count\": 529, \"model_name\": \"sklearn LR/MLP/RF\", \"seed\": \"42,123,456\", \"checkpoint_path\": \"N/A\", \"log_path\": \"output/exp_027_mlp_verifier/\"}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-18T06:41:51.069Z\"}, \"exp_028_fewnerd_5epoch\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T07:53:12.913Z\", \"updated_at\": \"2026-05-17T20:29:42.274Z\", \"spec\": {\"hypothesis\": \"Few-NERD low degeneracy (10%) partially due to under-convergence at 3 epochs. 5 epochs should increase degeneracy as model becomes more confident, potentially reducing LP selection gain.\", \"parent\": \"exp_021_fewnerd_full\", \"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=0,1,2,3 llamafactory-cli train train_config_fewnerd_5epoch_4gpu.yaml 2>&1 | tee logs/exp_028_4gpu_train.log\\\"\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:0,1,2,3\", \"data_path\": \"data/fewnerd_uie_train\", \"data_count\": 131767, \"model_name\": \"Qwen3-8B LoRA rank=32\", \"seed\": 42, \"log_path\": \"logs/exp_028_4gpu_train.log\", \"checkpoint_path\": \"checkpoints/qwen3-8b-fewnerd-5epoch-lora\"}, \"conclusion\": \"negative\", \"metrics\": {\"degeneracy_cf1_gold\": 0.3133, \"greedy_f1\": 0.7773, \"lp_sel_delta_pp\": 0.624, \"lp_sel_f1\": 0.7835, \"oracle_f1\": 0.8723, \"within_instance_rho_mean\": 0.4066, \"within_instance_rho_median\": 0.6151}, \"hypothesis\": \"Few-NERD low degeneracy (10%) partially due to under-convergence at 3 epochs. 5 epochs should increase degeneracy as model becomes more confident, potentially reducing LP selection gain.\", \"completed_at\": \"2026-05-17T20:29:42.274Z\"}, \"exp_028\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-17T07:35:39.447Z\", \"updated_at\": \"2026-05-17T20:26:59.399Z\", \"hypothesis\": \"Few-NERD low degeneracy (10%) in exp-021 is NOT due to under-convergence at 3 epochs; training for 5 epochs will show similar degeneracy levels, confirming the structural property of this dataset rather than an artifact of insufficient training.\", \"failure_reason\": \"startup recovery: RUNNING with no cron and no server/pid info\", \"completed_at\": \"2026-05-17T12:09:43.334Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\"}, \"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-17T20:06:01.040147+00:00\"}]}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=0,1,2,3 llamafactory-cli train train_config_fewnerd_5epoch_4gpu.yaml 2>&1 | tee logs/exp_028_4gpu_train.log\\\"\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/fewnerd_uie_train\", \"data_count\": 131767, \"model_name\": \"Qwen3-8B LoRA rank=32\", \"seed\": 42, \"checkpoint_path\": \"checkpoints/qwen3-8b-fewnerd-5epoch-lora\", \"log_path\": \"logs/exp_028_4gpu_train.log\"}, \"reproduce\": {\"finished_at\": \"2026-05-17T20:05:57.260Z\"}, \"conclusion\": \"negative\", \"metrics\": {\"degeneracy_cf1_gold\": 0.313, \"greedy_f1\": 0.7773, \"lp_sel_f1\": 0.7835, \"lp_sel_delta_pp\": 0.62, \"oracle_f1\": 0.8723, \"within_instance_rho\": 0.4066, \"train_loss\": 0.0189, \"eval_loss\": 0.0311}}, \"exp_024_claim_audit\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-17T10:54:36.291Z\", \"updated_at\": \"2026-05-17T10:55:08.244Z\", \"hypothesis\": \"Systematic cross-chapter numerical consistency audit: verify all quantitative claims in paper against source experiment data, catch stale values and cross-reference errors before submission.\", \"conclusion\": \"success\", \"metrics\": {\"consistent\": 97, \"errors\": 1, \"warnings\": 5, \"old_residuals_found\": 0}, \"spec\": {\"checkpoint_path\": \"artifacts/exp_024_claim_audit/audit_report.md\", \"log_path\": \"N/A\", \"command\": \"CPU-only paper audit\", \"server\": \"local\", \"data_path\": \"docs/paper/\", \"data_count\": 0, \"model_name\": \"N/A\", \"seed\": 0}, \"completed_at\": \"2026-05-17T10:55:08.244Z\"}, \"exp_016_rerun_1024_bootstrap\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T23:44:21.577Z\", \"updated_at\": \"2026-05-17T03:33:39.786Z\", \"hypothesis\": \"3-seed bootstrap significance test for NER logprob vs greedy selection gap (+0.6pp). Tests whether the observed advantage is statistically significant.\", \"spec\": {\"command\": \"python code/bootstrap_significance.py\", \"server\": \"local\", \"data_path\": \"output/exp_016_rerun_1024/\", \"data_count\": 529, \"model_name\": \"N/A (statistical analysis)\", \"seed\": \"3-seed bootstrap (1000 iterations)\", \"checkpoint_path\": \"N/A\", \"log_path\": \"output/exp_016_rerun_1024_bootstrap/\"}, \"conclusion\": \"negative\", \"metrics\": {\"bootstrap_ci_95\": [-0.03, 0.042], \"permutation_p\": 0.39, \"cohen_d\": 0.038, \"sign_test_win_rate\": 0.466, \"ner_logprob_vs_greedy_delta\": 0.006, \"conclusion_summary\": \"NER selection: no signal significantly outperforms greedy; RE: same conclusion\"}, \"completed_at\": \"2026-05-14T23:44:48.818Z\", \"parent\": \"exp_016_rerun_1024\"}, \"exp_verbalized_confidence\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T02:45:20.552Z\", \"updated_at\": \"2026-05-17T03:33:39.197Z\", \"hypothesis\": \"Verbalized confidence baseline: let model self-rate extraction confidence. If also compressed → strengthens \\\"score compression is general\\\" claim. If effective → important positive finding requiring narrative adjustment.\", \"conclusion\": \"negative\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python code/run_verbalized_confidence.py\", \"server\": \"autodl-5090\", \"data_path\": \"output/exp_012_rerun_1024/samples.jsonl + output/exp002_conll2003/samples.jsonl\", \"data_count\": 3285, \"model_name\": \"qwen3-8b-scierc-merged-v2 + qwen3-8b-conll2003-merged\", \"seed\": 42, \"checkpoint_path\": \"output/review_round9_experiments/verbalized_confidence/\", \"log_path\": \"output/review_round9_experiments/verbalized_confidence_run.log\"}, \"completed_at\": \"2026-05-16T03:09:39.916Z\", \"metrics\": {\"scierc\": {\"VerbConf_rho\": 0.2965, \"VerbConf_auroc\": 0.6811, \"VerbConf_sel_f1\": 0.6195, \"VerbConf_delta\": -0.0245, \"best_existing_rho\": 0.3792, \"VerbConf_mean\": 8.58, \"VerbConf_std\": 1.15, \"parse_fail_rate\": 0.0026}, \"conll\": {\"VerbConf_rho\": 0.3366, \"VerbConf_auroc\": 0.7469, \"VerbConf_sel_f1\": 0.8886, \"VerbConf_delta\": -0.0193, \"best_existing_rho\": 0.4507, \"VerbConf_mean\": 9.24, \"VerbConf_std\": 1.32, \"parse_fail_rate\": 0}}, \"parent\": \"exp_012_rerun_1024\"}, \"exp_entity_token_lp\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T05:39:44.631Z\", \"updated_at\": \"2026-05-17T03:33:38.371Z\", \"hypothesis\": \"Entity-token LP: test Discussion hypothesis (d) format-token dilution. Re-inference with per-token logprobs, then compute entity-only LP variance and selection F1. If entity-token LP compression is reduced → pilot remedy for LP selection. Also includes LP z-score normalization as zero-cost baseline. Addresses SF2+SF3 from Round 12.\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:0,cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"autodl-5090\", \"gpu\": \"cuda:0,cuda:1\", \"started_at\": \"2026-05-16T05:41:33.768Z\"}, \"conclusion\": \"negative\", \"metrics\": {\"scierc_ner\": {\"greedy_f1\": 0.643, \"full_lp_sel_f1\": 0.6465, \"entity_lp_sel_f1\": 0.6262, \"oracle_f1\": 0.7845, \"entity_lp_delta_vs_full_lp\": -0.0203}, \"conll_ner\": {\"greedy_f1\": 0.9065, \"full_lp_sel_f1\": 0.8989, \"entity_lp_sel_f1\": 0.8659, \"oracle_f1\": 0.948, \"entity_lp_delta_vs_full_lp\": -0.033}, \"finding\": \"entity-token LP strictly worse than full-sequence LP; CoNLL entity tokens saturated (79.4% tied), SciERC entity tokens too sparse (5.3% of total)\"}, \"spec\": {\"command\": \"python analyze_entity_token_lp.py\", \"server\": \"autodl-5090\", \"data_path\": \"output/exp_012_rerun_1024/ + output/exp_002_conll_rerun_1024/\", \"data_count\": \"529 (SciERC NER) + 2756 (CoNLL NER)\", \"model_name\": \"Qwen3-8B (finetuned)\", \"seed\": 42, \"checkpoint_path\": \"artifacts/exp_entity_token_lp/results.json\", \"log_path\": \"artifacts/exp_entity_token_lp/report.md\"}, \"completed_at\": \"2026-05-16T06:28:46.845Z\", \"parent\": \"exp_012_rerun_1024\"}, \"exp_freeform_ablation\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T09:42:22.868Z\", \"updated_at\": \"2026-05-17T03:33:37.623Z\", \"spec\": {\"command\": \"python run_freeform_inference.py --seed 42 --num_samples 8 --temperature 1.0 --max_tokens 1024 --output_dir results/exp_freeform_ablation\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:0\", \"pid\": \"169042\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_freeform_ablation.log\", \"submitted_at\": \"2026-05-15T09:42:30.236Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"hypothesis\": \"Free-form decoding recovers logprob variance and selection ability lost under constrained decoding\", \"plan_id\": \"exp-018\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 42, \"tmux_session\": \"exp_freeform_ablation\", \"wall_clock_seconds\": 1059.0, \"gpu_hours\": 0.29}, \"conclusion\": \"negative\", \"metrics\": {\"lp_std_ratio_free_vs_constrained\": 0.97, \"lp_range_ratio\": 0.96, \"tied_fraction_constrained\": 0.597, \"tied_fraction_freeform\": 0.577, \"ner_selection_gap_constrained\": 0.0059, \"ner_selection_gap_freeform\": 0.0018, \"re_selection_gap_constrained\": -0.0068, \"re_selection_gap_freeform\": 0.0169, \"parse_rate\": 0.9995, \"ner_vc_rho_constrained\": 0.3792, \"ner_vc_rho_freeform\": 0.4089}, \"checkpoint_path\": \"N/A (inference-only experiment)\", \"completed_at\": \"2026-05-15T10:00:09.238Z\", \"hypothesis\": \"Free-form vs constrained decoding ablation on SciERC: test if removing JSON schema constraint changes LP variance distribution. If LP remains compressed under free-form, confirms compression is model-intrinsic not format-artifact.\", \"parent\": \"exp_012_rerun_1024\"}, \"exp_008_re_n16\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:03:06.876Z\", \"updated_at\": \"2026-05-17T02:58:19.490Z\", \"spec\": {\"hypothesis\": \"RE N=16 confirms negative finding with higher statistical power. If rho still <0.30, task-complexity boundary is robust.\", \"plan_id\": \"exp-008\", \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"dataset\": \"SciERC\", \"gpu\": \"cuda:2\", \"server\": \"gpu-5090-4x-2\", \"gpu_budget_hours\": 12, \"description\": \"RE N=16 on SciERC to confirm negative finding. Inference with log-prob capture.\", \"priority\": \"P1\", \"command\": \"python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 16 --temperature 1.0 --seed 42 --collect_logprobs\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"seed\": 42, \"num_instances\": 200, \"partial\": true, \"note\": \"Only 200/551 instances due to --num_test default bug. Needs full rerun.\"}, \"metrics\": {\"ner\": {\"greedy_f1\": 0.6635, \"oracle_f1\": 0.8208, \"headroom\": 0.1572, \"rho_sj_full\": 0.377, \"rho_fk_full\": 0.2508, \"rho_logprob_full\": 0.3153, \"rho_sj_cond\": 0.3598, \"rho_fk_cond\": 0.2251, \"rho_logprob_cond\": 0.2927, \"sj_beats_fk\": true, \"rho_advantage\": 0.1262}, \"re\": {\"greedy_f1\": 0.4339, \"oracle_f1\": 0.6658, \"headroom\": 0.2319, \"rho_sj_full\": 0.2966, \"rho_fk_full\": 0.2871, \"rho_logprob_full\": 0.2986, \"rho_sj_cond\": 0.3975, \"rho_fk_cond\": 0.3774, \"rho_logprob_cond\": 0.2745, \"sj_beats_fk\": true, \"rho_advantage\": 0.0095}, \"verdict\": \"FAIL\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A\", \"log_path\": \"output/exp008_re_n16/\", \"completed_at\": \"2026-05-14T12:28:39.268Z\", \"hypothesis\": \"RE N=16 initial evaluation: first relation extraction test with structural signals. Establishes baseline RE signal effectiveness before pipeline corrections.\"}, \"exp_001_ner_n16_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:46:06.430Z\", \"updated_at\": \"2026-05-17T02:58:18.225Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=3 python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 16 --temperature 1.0 --seed 123 --output_dir output/exp001_n16_seed123 --num_test 9999 --collect_logprobs 2>&1 | tee output/exp001_n16_seed123_run.log\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:3\"], \"pid\": \"63407\", \"log_path\": \"output/exp001_n16_seed123_run.log\", \"submitted_at\": \"2026-05-14T12:46:06.234Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_count\": 551, \"data_path\": \"data/scierc/processed_data\", \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 123, \"checkpoint_path\": \"output/exp001_n16_seed123/\", \"wall_clock_seconds\": 2748.0, \"gpu_hours\": 0.76}, \"conclusion\": \"success\", \"metrics\": {\"ner\": {\"greedy_f1\": 0.663, \"oracle_f1\": 0.809, \"headroom\": 0.146, \"rho_sj\": 0.423, \"rho_fk\": 0.29, \"rho_logprob\": 0.239, \"rho_sj_cond\": 0.423, \"rho_fk_cond\": 0.26}, \"re\": {\"greedy_f1\": 0.419, \"oracle_f1\": 0.625, \"headroom\": 0.206, \"rho_sj\": 0.267, \"rho_fk\": 0.315, \"rho_sj_cond\": 0.364, \"rho_fk_cond\": 0.331}, \"verdict\": \"FAIL\", \"verdict_note\": \"RE rho_sj=0.267 < 0.40; RE >30% samples F1=0\", \"n_instances\": 551, \"seed\": 123, \"N\": 16, \"T\": 1}, \"completed_at\": \"2026-05-14T13:31:54.232Z\", \"hypothesis\": \"SciERC NER N=16 seed=123: multi-seed validation at N=16. Tests seed stability for signal rankings with more samples.\"}, \"exp_007_ner_multi_model\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T11:42:20.748Z\", \"updated_at\": \"2026-05-17T02:58:16.747Z\", \"spec\": {\"command\": \"bash -c 'source env.sh && cd /root/autodl-tmp/struct_self_consist_ie && llamafactory-cli train train_config_llama.yaml'\", \"server\": \"gpu-5090-4x-2\", \"gpu\": [\"cuda:0\"], \"pid\": \"60970\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_007_ner_multi_model.log\", \"submitted_at\": \"2026-05-14T12:43:09.108Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data\", \"data_count\": 1861, \"model_name\": \"LLaMA-3.1-8B-Instruct\", \"seed\": 42, \"log_file\": \"~/runs/struct_self_consist_ie/exp_007_ner_multi_model.log\", \"wall_clock_seconds\": 165.8, \"gpu_hours\": 0.05}, \"server\": \"autodl-5090\", \"gpu\": \"cuda:3\", \"account\": \"root\", \"reproduce\": {\"server\": \"autodl-5090\", \"gpu\": \"cuda:3\", \"started_at\": \"2026-05-14T11:43:50.977Z\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T12:45:54.952Z\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/llama3.1-8b-scierc-lora\", \"metrics\": {\"epoch\": 5, \"train_loss\": 0.0767, \"eval_loss\": 0.1049, \"train_runtime_sec\": 1494.5, \"train_samples_per_second\": 6.226, \"checkpoints\": [\"checkpoint-400\", \"checkpoint-500\", \"checkpoint-585\"], \"base_model\": \"Meta-Llama-3.1-8B-Instruct\", \"lora_r\": 32, \"lora_alpha\": 64, \"note\": \"EXIT_CODE=129 (SIGHUP) but training completed all 5 epochs before signal. Checkpoint fully intact.\"}, \"log_path\": \"~/runs/struct_self_consist_ie/exp_007_ner_multi_model.log\", \"hypothesis\": \"Multi-model NER comparison: evaluates signal effectiveness across Qwen and LLaMA on SciERC NER. Establishes cross-model generalization of structural>surface ranking.\"}, \"exp_003_ner_wnut17\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T11:42:17.544Z\", \"updated_at\": \"2026-05-17T02:58:14.928Z\", \"spec\": {\"merged_model_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-wnut17-merged\", \"pilot_command\": \"CUDA_VISIBLE_DEVICES=1 python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-wnut17-merged --data_dir data/wnut17 --dataset wnut17 --subtask ner --n_samples 16 --temperature 1.0 --seed 42 --output_dir output/exp003_wnut17_pilot --num_test 9999 --collect_logprobs\", \"pilot_pid\": 71498, \"pilot_server\": \"autodl-5090\", \"pilot_started_at\": \"2026-05-14T21:36:00Z\", \"test_samples\": 1287}, \"server\": \"autodl-5090\", \"gpu\": \"cuda:2\", \"account\": \"root\", \"reproduce\": {\"server\": \"autodl-5090\", \"gpu\": \"cuda:2\", \"started_at\": \"2026-05-14T11:43:50.537Z\", \"finished_at\": \"2026-05-14T12:53:13.262Z\", \"training_hours\": 1.16}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T12:53:14.768981+00:00\"}]}, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-wnut17-merged\", \"metrics\": {\"ner\": {\"greedy_f1\": 0.525, \"oracle_f1\": 0.664, \"headroom\": 0.139, \"rho_sj_full\": 0.082, \"rho_fk_full\": 0.124, \"rho_logprob_full\": -0.414, \"rho_sj_cond\": 0.275, \"rho_fk_cond\": 0.164, \"rho_logprob_cond\": 0.352, \"sj_beats_logprob_cond\": false}, \"n_instances\": 1287, \"n_gold_empty\": 598, \"sample_f1_mean\": 0.401, \"sample_f1_pct_zero\": 53.7, \"N\": 16, \"T\": 1, \"seed\": 42, \"verdict\": \"FAIL\", \"verdict_note\": \">30% samples F1=0; structural rho weak; logprob baseline stronger\"}, \"conclusion\": \"negative\", \"log_path\": \"output/exp003_wnut17_pilot/\", \"completed_at\": \"2026-05-14T13:40:20.979Z\", \"hypothesis\": \"WNUT-17 NER fine-tune + inference: initial attempt on social media domain. Tests if structural signals work when model capability is low on noisy text with novel entity types.\"}, \"exp_001_seed456_t10_full\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T13:27:41.067Z\", \"updated_at\": \"2026-05-17T02:58:12.996Z\", \"spec\": {\"command\": \"python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --dataset scierc --subtask joint --n_samples 16 --temperature 1.0 --seed 456 --num_test 9999 --collect_logprobs\", \"server\": \"autodl-5090\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 456}, \"reproduce\": {\"finished_at\": \"2026-05-14T13:44:05.416Z\"}, \"failure_reason\": \"\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-14T13:44:05.021Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T13:44:10.317185+00:00\"}]}, \"metrics\": {\"ner\": {\"rho_sj\": 0.414, \"rho_fk\": 0.298}, \"re\": {\"rho_sj\": 0.268, \"rho_fk\": 0.26}, \"n_instances\": 551, \"N\": 16, \"T\": 1, \"seed\": 456, \"source\": \"reviewer_verified_report_json\"}, \"hypothesis\": \"SciERC NER seed=456 T=1.0 full: early multi-seed NER test before pipeline corrections. Preliminary evidence for seed stability.\"}, \"exp_001_seed123_t10_full\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T13:27:42.503Z\", \"updated_at\": \"2026-05-17T02:58:11.623Z\", \"spec\": {\"command\": \"python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --dataset scierc --subtask joint --n_samples 16 --temperature 1.0 --seed 123 --num_test 9999 --collect_logprobs\", \"server\": \"autodl-5090\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 123}, \"reproduce\": {\"finished_at\": \"2026-05-14T13:44:13.823Z\"}, \"failure_reason\": \"\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-14T13:44:13.213Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T13:44:16.532801+00:00\"}]}, \"metrics\": {\"ner\": {\"rho_sj\": 0.417, \"rho_fk\": 0.283}, \"re\": {\"rho_sj\": 0.265, \"rho_fk\": 0.315}, \"n_instances\": 551, \"N\": 16, \"T\": 1, \"seed\": 123, \"source\": \"reviewer_verified_report_json\"}, \"hypothesis\": \"SciERC NER seed=123 T=1.0 full: early multi-seed NER test before pipeline corrections. Preliminary evidence for seed stability.\"}, \"exp_008_re_n16_t10_full\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T13:27:42.867Z\", \"updated_at\": \"2026-05-17T02:58:10.171Z\", \"spec\": {\"command\": \"python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --dataset scierc --subtask joint --n_samples 16 --temperature 1.0 --seed 42 --num_test 9999 --collect_logprobs\", \"server\": \"autodl-5090\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 42}, \"reproduce\": {\"finished_at\": \"2026-05-14T13:44:18.988Z\"}, \"failure_reason\": \"\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-14T13:44:19.577Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T13:44:21.528032+00:00\"}]}, \"metrics\": {\"ner\": {\"rho_sj\": 0.444}, \"re\": {\"rho_sj\": 0.248}, \"n_instances\": 551, \"N\": 16, \"T\": 1, \"seed\": 42, \"mode\": \"RE-only\", \"source\": \"director_corrected\"}, \"hypothesis\": \"RE N=16 T=1.0 full dataset: early RE evaluation attempt. Tests structural signals on relation extraction before pipeline corrections.\"}, \"exp_007_llama_inference\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T13:54:48.055Z\", \"updated_at\": \"2026-05-17T02:58:03.014Z\", \"spec\": {\"command\": \"python run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-scierc-merged --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 1.0 --seed 42 --num_test 9999 --collect_logprobs --output_dir output/exp007_llama_inference/\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"75172\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_007_llama_inference.log\", \"submitted_at\": \"2026-05-14T13:54:47.962Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"Meta-Llama-3.1-8B-Instruct (LoRA fine-tuned on SciERC)\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/llama3.1-8b-scierc-merged\", \"description\": \"LLaMA-3.1-8B SciERC joint inference (NER+RE) with 8 samples, T=1.0, logprobs collected.\", \"wall_clock_seconds\": 1038.5, \"gpu_hours\": 0.29}, \"log_path\": \"output/exp007_llama_inference/\", \"checkpoint_path\": \"N/A\", \"metrics\": {\"ner\": {\"greedy_f1\": 0.66, \"oracle_f1\": 0.781, \"headroom\": 0.121, \"rho_fk\": 0.327, \"rho_sj\": 0.363, \"rho_fk_cond\": 0.226, \"rho_sj_cond\": 0.311, \"rho_logprob\": 0.183, \"rho_logprob_cond\": 0.109, \"structural_beats_surface\": true, \"sample_f1_pct_zero\": 11.6}, \"re\": {\"greedy_f1\": 0.434, \"oracle_f1\": 0.568, \"headroom\": 0.135, \"rho_fk\": 0.305, \"rho_sj\": 0.299, \"rho_fk_cond\": 0.259, \"rho_sj_cond\": 0.405, \"rho_logprob\": 0.288, \"rho_logprob_cond\": 0.092, \"structural_beats_surface\": false, \"sample_f1_pct_zero\": 41.2}, \"n_instances\": 551, \"N\": 8, \"T\": 1, \"seed\": 42, \"model\": \"LLaMA-3.1-8B-Instruct\", \"verdict\": \"FAIL\", \"verdict_note\": \"RE rho_sj_full=0.299 < 0.40; >30% RE samples F1=0\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T14:12:06.442Z\", \"hypothesis\": \"LLaMA SciERC N=8 baseline: first cross-model test. Verifies structural signal effectiveness generalizes from Qwen to LLaMA model family on SciERC NER.\"}, \"exp_003_wnut17_eval\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T13:47:34.654Z\", \"updated_at\": \"2026-05-17T02:58:01.627Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-wnut17-merged --data_dir data/wnut17 --dataset wnut17 --subtask ner --n_samples 16 --temperature 1.0 --seed 42 --output_dir output/exp003_wnut17_eval --num_test 9999 --collect_logprobs\", \"server\": \"autodl-5090\", \"data_path\": \"data/wnut17\", \"data_count\": 1287, \"model_name\": \"qwen3-8b-wnut17-merged\", \"seed\": 42}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T14:08:17.429Z\", \"metrics\": {\"greedy_f1\": 0.523, \"oracle_f1\": 0.664, \"headroom\": 0.141, \"rho_fk\": 0.125, \"rho_sj\": 0.089, \"rho_fk_cond\": 0.169, \"rho_sj_cond\": 0.288, \"rho_logprob_full\": -0.409, \"rho_logprob_cond\": 0.35, \"structural_beats_surface\": false, \"sample_f1_pct_zero\": 53.7, \"n_instances\": 1287, \"N\": 16, \"T\": 1, \"seed\": 42, \"model\": \"Qwen3-8B\", \"n_gold_empty_filtered\": 598, \"verdict\": \"FAIL\", \"verdict_note\": \"structural_beats_surface=false; >50% samples F1=0\"}, \"hypothesis\": \"WNUT-17 NER evaluation: initial test on noisy social media domain. Tests boundary conditions for structural signal effectiveness on out-of-domain text.\"}, \"exp_010_selection_curves\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T15:01:53.585Z\", \"updated_at\": \"2026-05-17T02:58:00.378Z\", \"spec\": {\"command\": \"python3 code/exp010_selection_curves.py\", \"server\": \"autodl-5090\", \"data_path\": \"output/exp_001_seed42_v2, output/exp_008_re_n16_v2, output/exp002_conll2003\", \"data_count\": \"551+397+3453 instances\", \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 42, \"description\": \"Best-of-N selection curves: F1 vs N for 7 signals across 3 datasets\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (analysis only)\", \"log_path\": \"/tmp/exp010.log\", \"completed_at\": \"2026-05-14T15:02:22.638Z\", \"metrics\": {\"scierc_ner\": {\"n_instances\": 551, \"greedy_f1\": 0.618, \"N16\": {\"oracle\": 0.787, \"SJ\": 0.62, \"FK\": 0.621, \"logprob\": 0.621, \"voting_conf\": 0.585, \"EM\": 0.606, \"random\": 0.595}, \"N8\": {\"oracle\": 0.752, \"SJ\": 0.614, \"FK\": 0.614, \"logprob\": 0.619, \"voting_conf\": 0.591, \"EM\": 0.603, \"random\": 0.589}, \"N4\": {\"oracle\": 0.714, \"SJ\": 0.607, \"FK\": 0.608, \"logprob\": 0.616, \"voting_conf\": 0.594, \"EM\": 0.6, \"random\": 0.587}}, \"scierc_re\": {\"n_instances\": 397, \"greedy_f1\": 0.403, \"N16\": {\"oracle\": 0.631, \"SJ\": 0.397, \"FK\": 0.396, \"logprob\": 0.41, \"voting_conf\": 0.408, \"EM\": 0.381, \"random\": 0.364}, \"N8\": {\"oracle\": 0.583, \"SJ\": 0.393, \"FK\": 0.394, \"logprob\": 0.413, \"voting_conf\": 0.398, \"EM\": 0.381, \"random\": 0.363}}, \"conll_ner\": {\"n_instances\": 3453, \"greedy_f1\": 0.725, \"N8\": {\"oracle\": 0.757, \"SJ\": 0.718, \"FK\": 0.717, \"logprob\": 0.716, \"voting_conf\": 0.714, \"EM\": 0.716, \"random\": 0.69}, \"N4\": {\"oracle\": 0.746, \"SJ\": 0.714, \"FK\": 0.714, \"logprob\": 0.715, \"voting_conf\": 0.714, \"EM\": 0.712, \"random\": 0.692}}}, \"hypothesis\": \"Selection curve analysis: plots selection F1 vs confidence threshold for each signal. Visualizes where correlation-selection gap emerges and at what confidence level signals become useful for filtering.\"}, \"exp_007_llama_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T15:08:50.628Z\", \"updated_at\": \"2026-05-17T02:57:59.595Z\", \"spec\": {\"description\": \"LLaMA 3.1-8B SciERC joint extraction, seed=456, cross-model robustness test\", \"hypothesis\": \"Structural consistency generalizes across model architectures (LLaMA vs Qwen)\", \"command\": \"CUDA_VISIBLE_DEVICES=2 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-scierc-merged --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 1.0 --seed 456 --num_test 9999 --collect_logprobs --output_dir output/exp_007_llama_seed456\", \"server\": \"bjb1-21071\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"llama3.1-8b-scierc-merged\", \"seed\": 456, \"gpu\": [\"cuda:2\"], \"backend\": \"tmux\", \"tmux_session\": \"exp007_s456\", \"account\": \"root\", \"log_path\": \"output/exp_007_llama_seed456/run.log\"}, \"conclusion\": \"negative\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_007_llama_seed456/run.log\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_007_llama_seed456/\", \"completed_at\": \"2026-05-14T15:19:20.693Z\", \"metrics\": {\"verdict\": \"FAIL\", \"ner\": {\"greedy_f1\": 0.6597, \"oracle_f1\": 0.7575, \"oracle_headroom\": 0.0978, \"fleiss_kappa\": 0.4543, \"soft_jaccard\": 0.7491, \"rho_kappa_f1\": 0.3115, \"rho_sj_f1\": 0.3663, \"structural_gt_surface\": true}, \"re\": {\"greedy_f1\": 0.4334, \"oracle_f1\": 0.5789, \"oracle_headroom\": 0.1455, \"fleiss_kappa\": 0.3791, \"soft_jaccard\": 0.6782, \"rho_kappa_f1\": 0.3013, \"rho_sj_f1\": 0.287, \"structural_gt_surface\": false}, \"logprob_ner\": {\"rho\": 0.1911, \"auroc\": 0.5989}, \"logprob_re\": {\"rho\": 0.3246, \"auroc\": 0.6678}, \"fail_reason\": \"RE rho_sj=0.2870 < 0.40 threshold; >30% samples F1=0\"}, \"hypothesis\": \"LLaMA SciERC seed=456: early cross-model multi-seed test. Verifies LLaMA NER signal pattern is reproducible across sampling seeds.\"}, \"exp_007_llama_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T15:08:50.157Z\", \"updated_at\": \"2026-05-17T02:57:58.879Z\", \"spec\": {\"description\": \"LLaMA 3.1-8B SciERC joint extraction, seed=123, cross-model robustness test\", \"hypothesis\": \"Structural consistency generalizes across model architectures (LLaMA vs Qwen)\", \"command\": \"CUDA_VISIBLE_DEVICES=1 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-scierc-merged --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 1.0 --seed 123 --num_test 9999 --collect_logprobs --output_dir output/exp_007_llama_seed123\", \"server\": \"bjb1-21071\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"llama3.1-8b-scierc-merged\", \"seed\": 123, \"gpu\": [\"cuda:1\"], \"backend\": \"tmux\", \"tmux_session\": \"exp007_s123\", \"account\": \"root\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_007_llama_seed123/run.log\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_007_llama_seed123/\"}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-14T15:19:43.424Z\", \"metrics\": {\"verdict\": \"FAIL\", \"ner\": {\"greedy_f1\": 0.6605, \"oracle_f1\": 0.7703, \"headroom\": 0.1098, \"fleiss_kappa\": 0.4553, \"soft_jaccard\": 0.7525, \"rho_kappa_f1\": 0.2143, \"rho_sj_f1\": 0.3371, \"structural_gt_surface\": true}, \"re\": {\"greedy_f1\": 0.433, \"oracle_f1\": 0.5719, \"headroom\": 0.1389, \"fleiss_kappa\": 0.3851, \"soft_jaccard\": 0.6911, \"rho_kappa_f1\": 0.2844, \"rho_sj_f1\": 0.268, \"structural_gt_surface\": false}, \"fail_reasons\": [\"RE rho_sj=0.2680 < 0.40 threshold\", \">30% samples F1=0 (RE: 41.0%)\", \"RE structural not > surface (delta=-0.0165)\"]}, \"hypothesis\": \"LLaMA SciERC seed=123: early cross-model multi-seed test. Verifies LLaMA NER signal pattern is reproducible across sampling seeds.\"}, \"exp_008_re_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T15:08:51.386Z\", \"updated_at\": \"2026-05-17T02:57:58.166Z\", \"spec\": {\"description\": \"RE N=16 on SciERC, seed=123, seed robustness test for relation extraction\", \"hypothesis\": \"Structural consistency correlates with per-instance RE F1, robust across seeds\", \"command\": \"CUDA_VISIBLE_DEVICES=3 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask re --n_samples 16 --temperature 1.0 --seed 123 --num_test 9999 --collect_logprobs --output_dir output/exp_008_re_seed123\", \"server\": \"bjb1-21071\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 123, \"gpu\": [\"cuda:3\"], \"backend\": \"tmux\", \"tmux_session\": \"exp008_rs123\", \"account\": \"root\", \"log_path\": \"output/exp_008_re_seed123/run.log\"}, \"log_path\": \"output/exp_008_re_seed123/run.log\", \"conclusion\": \"negative\", \"metrics\": {\"greedy_f1\": 0.4229, \"oracle_f1\": 0.6244, \"oracle_headroom\": 0.2015, \"fleiss_kappa_mean\": 0.3455, \"soft_jaccard_mean\": 0.6126, \"sample_f1_mean\": 0.3594, \"sample_f1_std\": 0.3793, \"sample_f1_zero_pct\": 44.1, \"structural_gt_surface\": false, \"rho_kappa_f1_full\": 0.3174, \"rho_sj_f1_full\": 0.2835, \"rho_kappa_f1_cond\": 0.0766, \"rho_sj_f1_cond\": 0.2877, \"logprob_auroc_full\": 0.6499, \"logprob_auroc_cond\": 0.5265, \"verdict\": \"FAIL\"}, \"checkpoint_path\": \"N/A\", \"completed_at\": \"2026-05-14T15:21:39.591Z\", \"hypothesis\": \"RE seed=123 multi-seed: tests reproducibility of RE signal rankings. Hypothesis: RE signals weaker than NER due to higher zero-F1 rate, but ranking should be seed-stable.\"}, \"exp_001_seed42_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T14:34:02.350Z\", \"updated_at\": \"2026-05-17T02:57:57.324Z\", \"spec\": {\"description\": \"NER N=16 on SciERC, seed=42, ft_002_v2, with logprobs\", \"hypothesis\": \"Structural consistency (Fleiss kappa, Soft Jaccard) correlates with per-instance NER F1 on SciERC\", \"server\": \"autodl-5090\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"ft_002_v2\", \"seed\": 42, \"command\": \"CUDA_VISIBLE_DEVICES=1 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask ner --n_samples 16 --temperature 1.0 --seed 42 --num_test 9999 --collect_logprobs --output_dir output/exp_001_seed42_v2\", \"gpu\": [\"cuda:1\"], \"pid\": \"78728\", \"backend\": \"tmux\", \"account\": \"root\", \"log_path\": \"output/exp_001_seed42_v2/run.log\"}, \"conclusion\": \"success\", \"metrics\": {\"sj_rho_full\": 0.428, \"sj_rho_cond\": 0.369, \"structural_minus_surface\": 0.147, \"conclusion_note\": \"NER seed42 robustness confirmed, structural>surface +0.147\"}, \"checkpoint_path\": \"N/A (inference)\", \"completed_at\": \"2026-05-14T15:23:34.091Z\", \"log_path\": \"output/exp_001_seed42_v2/\", \"hypothesis\": \"SciERC NER seed=42 v2: primary seed baseline under corrected pipeline. Establishes canonical signal rankings (SJ>FK>LP) for NER with gold-filtering.\"}, \"exp_001_seed123_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T14:34:04.210Z\", \"updated_at\": \"2026-05-17T02:57:42.106Z\", \"spec\": {\"description\": \"NER N=16 on SciERC, seed=123, ft_002_v2, with logprobs\", \"hypothesis\": \"Structural consistency (Fleiss kappa, Soft Jaccard) correlates with per-instance NER F1 on SciERC (seed robustness check)\", \"server\": \"autodl-5090\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"ft_002_v2\", \"seed\": 123, \"command\": \"CUDA_VISIBLE_DEVICES=2 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask ner --n_samples 16 --temperature 1.0 --seed 123 --num_test 9999 --collect_logprobs --output_dir output/exp_001_seed123_v2\", \"gpu\": [\"cuda:2\"], \"pid\": \"78733\", \"backend\": \"tmux\", \"account\": \"root\", \"log_path\": \"output/exp_001_seed123_v2/run.log\"}, \"conclusion\": \"success\", \"metrics\": {\"sj_rho_full\": 0.424, \"sj_rho_cond\": 0.376, \"structural_minus_surface\": 0.149, \"conclusion_note\": \"NER seed123 robustness confirmed, structural>surface +0.149\"}, \"checkpoint_path\": \"N/A (inference)\", \"completed_at\": \"2026-05-14T15:23:35.076Z\", \"log_path\": \"output/exp_001_seed123_v2/\", \"hypothesis\": \"SciERC NER seed=123 v2: second seed for multi-seed validation. Establishes reproducibility of structural>surface signal ranking across random seeds.\"}, \"exp_008_re_n16_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T14:34:06.296Z\", \"updated_at\": \"2026-05-17T02:57:41.178Z\", \"spec\": {\"description\": \"RE N=16 on SciERC full set confirmation, ft_002_v2, with logprobs\", \"hypothesis\": \"Structural consistency correlates with per-instance RE F1 on SciERC full dataset\", \"server\": \"autodl-5090\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"ft_002_v2\", \"seed\": 42, \"command\": \"CUDA_VISIBLE_DEVICES=3 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask re --n_samples 16 --temperature 1.0 --seed 42 --num_test 9999 --collect_logprobs --output_dir output/exp_008_re_n16_v2\", \"gpu\": [\"cuda:3\"], \"pid\": \"78737\", \"backend\": \"tmux\", \"account\": \"root\", \"log_path\": \"output/exp_008_re_n16_v2/run.log\"}, \"conclusion\": \"negative\", \"metrics\": {\"sj_rho_full\": 0.281, \"sj_rho_cond\": 0.308, \"f1_zero_pct\": 44.3, \"conclusion_note\": \"RE N=16 v2 negative: SJ weak, 44.3% F1=0\"}, \"checkpoint_path\": \"N/A (inference)\", \"completed_at\": \"2026-05-14T15:23:35.598Z\", \"log_path\": \"output/exp_008_re_n16_v2/\", \"hypothesis\": \"RE N=16 evaluation v2: tests structural signal effectiveness on relation extraction at higher sample count. Hypothesis: SJ/FK benefit from more samples on RE task where zero-F1 rate is high.\"}, \"exp_005_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T15:28:14.924Z\", \"updated_at\": \"2026-05-17T02:57:38.756Z\", \"spec\": {\"description\": \"Temperature sensitivity analysis: T=0.7 vs T=1.0 across 5 signals (SJ, FK, logprob, EM, voting_conf)\", \"command\": \"python code/analyze_exp005_v2_temperature.py\", \"server\": \"autodl-5090\", \"data_path\": \"output/mvp_pilot_004 + output/mvp_pilot_005 + output/exp_012_logprob\", \"data_count\": 551, \"model_name\": \"Qwen3-8B-SciERC-LoRA\", \"seed\": 42, \"checkpoint_path\": \"N/A\", \"log_path\": \"output/exp_005_v2_temperature/temperature_sensitivity_report.json\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T15:28:35.949Z\", \"hypothesis\": \"Selection F1 analysis v2: compute actual selection F1 (pick best sample by each signal) vs greedy and oracle. First evidence of correlation-selection gap under corrected pipeline.\"}, \"exp_006_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T15:30:02.348Z\", \"updated_at\": \"2026-05-17T02:57:36.914Z\", \"spec\": {\"command\": \"python3 code/exp_006_v2_selection.py\", \"server\": \"autodl-5090\", \"data_path\": \"output/exp_{001_seed42,001_seed123,002_conll,008_re}_v2/\", \"data_count\": 4952, \"model_name\": \"Qwen3-8B-SciERC-merged-v2\", \"seed\": 42}, \"conclusion\": \"negative\", \"checkpoint_path\": \"output/exp_006_v2/exp_006_v2_results.json\", \"log_path\": \"output/exp_006_v2_run.log\", \"completed_at\": \"2026-05-14T15:30:32.474Z\", \"metrics\": {\"NER_SciERC_s42\": {\"greedy\": 0.618, \"oracle\": 0.787, \"SJ\": 0.62, \"logprob\": 0.621, \"FK\": 0.621, \"EM\": 0.606, \"voting_conf\": 0.585, \"random\": 0.586}, \"NER_SciERC_s123\": {\"greedy\": 0.618, \"oracle\": 0.785, \"SJ\": 0.617, \"logprob\": 0.618, \"FK\": 0.621, \"EM\": 0.613, \"voting_conf\": 0.584, \"random\": 0.583}, \"NER_CoNLL\": {\"greedy\": 0.725, \"oracle\": 0.757, \"SJ\": 0.718, \"logprob\": 0.716, \"FK\": 0.717, \"EM\": 0.716, \"voting_conf\": 0.714, \"random\": 0.692}, \"RE_SciERC\": {\"greedy\": 0.403, \"oracle\": 0.631, \"SJ\": 0.397, \"logprob\": 0.41, \"FK\": 0.396, \"EM\": 0.381, \"voting_conf\": 0.408, \"random\": 0.364}}, \"hypothesis\": \"Temperature sensitivity v2: tests signal effectiveness at T=0.5,0.7,1.0,1.2. Hypothesis: structural signals are temperature-robust while LP degrades at extreme temperatures.\"}, \"exp_004_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T15:31:40.554Z\", \"updated_at\": \"2026-05-17T02:57:35.012Z\", \"conclusion\": \"success\", \"spec\": {\"command\": \"python code/analyze_exp004_v2_re_diagnostic.py\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_012_logprob/samples_with_logprobs.jsonl\", \"data_count\": 551, \"model_name\": \"Qwen3-8B-SciERC-merged-v2\", \"seed\": 42, \"checkpoint_path\": \"N/A\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp004v2_re_diagnostic/\"}, \"completed_at\": \"2026-05-14T15:32:04.966Z\", \"hypothesis\": \"N-ablation v2 (N=4,8,16,32): tests how sample count affects signal ρ and selection F1. Validates N-scaling curve for structural vs surface signals under corrected pipeline.\"}, \"exp_009_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T15:36:47.946Z\", \"updated_at\": \"2026-05-17T02:57:32.655Z\", \"spec\": {\"command\": \"python3 code/exp_009_v2_stratification.py\", \"server\": \"autodl-5090\", \"data_path\": \"output/exp_001_seed42_v2 + exp_001_seed123_v2 + exp_008_re_n16_v2\", \"data_count\": 551, \"model_name\": \"analysis\", \"seed\": 42}, \"checkpoint_path\": \"output/exp_009_v2/results.json\", \"log_path\": \"output/exp_009_v2_run.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T15:37:18.311Z\", \"metrics\": {\"ner_seed42_global\": {\"sj_rho\": 0.431, \"fk_rho\": 0.325, \"logprob_rho\": 0.203, \"voting_conf_rho\": 0.475, \"em_rho\": 0.292}, \"ner_seed123_global\": {\"sj_rho\": 0.422, \"fk_rho\": 0.315, \"logprob_rho\": 0.226, \"voting_conf_rho\": 0.438, \"em_rho\": 0.299}, \"re_seed42_global\": {\"sj_rho\": 0.063, \"fk_rho\": 0.226, \"logprob_rho\": 0.4, \"voting_conf_rho\": 0.22, \"em_rho\": -0.132}, \"ner_seed_stability_max_delta\": 0.037, \"independent_proxies\": [\"sent_len\", \"ent_count\", \"type_diversity\"], \"inverted_u_ner\": \"not confirmed (ρ stable across independent proxies)\", \"inverted_u_re\": \"monotonic increase with complexity, not inverted-U\"}, \"hypothesis\": \"Capability stratification v2: corrected stratification with gold-filtering and extended to NER conditional analysis. Tests which instance subpopulations drive overall signal effectiveness.\"}, \"exp_016_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T15:39:07.501Z\", \"updated_at\": \"2026-05-17T02:57:30.726Z\", \"spec\": {\"command\": \"python code/exp_016_v2_ensemble.py\", \"server\": \"autodl-5090\", \"data_path\": \"output/exp_001_seed42_v2 + exp_001_seed123_v2 + exp_008_re_n16_v2\", \"data_count\": 551, \"model_name\": \"analysis_only\", \"seed\": 42, \"checkpoint_path\": \"output/exp_016_v2/\", \"log_path\": \"/tmp/exp016v2.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T15:39:34.478Z\", \"metrics\": {\"ner_conditional\": {\"n\": 529, \"best_single_signal_rho\": {\"soft_jaccard\": 0.4412}, \"best_combo_rho\": {\"sj+vc_a0.55\": 0.4552}, \"ensemble_auroc\": 0.7141, \"best_single_auroc\": {\"soft_jaccard\": 0.7166}, \"selection_f1\": {\"greedy\": 0.6442, \"logprob_best\": 0.6505, \"ensemble_best\": 0.6475, \"sj_best\": 0.6471, \"oracle\": 0.8442}}, \"re_conditional\": {\"n\": 397, \"best_single_signal_rho\": {\"voting_confidence\": 0.3849}, \"best_combo_rho\": {\"logprob+vc_a0.25\": 0.3936}, \"ensemble_auroc\": 0.6916, \"best_single_auroc\": {\"voting_confidence\": 0.7023}, \"selection_f1\": {\"greedy\": 0.403, \"logprob_best\": 0.4097, \"ensemble_best\": 0.4227, \"oracle\": 0.6306}}, \"re_full\": {\"ensemble_auroc\": 0.8608, \"best_single_auroc\": {\"voting_confidence\": 0.8248}}}, \"hypothesis\": \"Bootstrap significance v2: corrected bootstrap test for NER selection F1 gap with proper gold-filtering and multiple signals. Establishes which selection improvements are statistically significant.\"}, \"exp_001_seed456_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T15:38:55.569Z\", \"updated_at\": \"2026-05-17T02:57:23.336Z\", \"spec\": {\"hypothesis\": \"NER/RE N=16 seed=456 robustness test, third seed for 3-seed stability\", \"plan_id\": \"exp-001\", \"command\": \"CUDA_VISIBLE_DEVICES=2 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 16 --temperature 1.0 --seed 456 --num_test 9999 --collect_logprobs --output_dir output/exp_001_seed456_v2\", \"server\": \"autodl-5090\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 456, \"metrics\": {\"full_rho_kappa_f1\": 0.3383, \"full_rho_sj_f1\": 0.2988, \"cond_rho_kappa_f1\": 0.233, \"cond_rho_sj_f1\": 0.3245, \"logprob_full_rho\": 0.3405, \"logprob_full_auroc\": 0.6694, \"logprob_cond_rho\": 0.0501, \"structural_gt_surface\": false}, \"note\": \"CRITICAL: Ran with --subtask joint instead of --subtask ner. seed42/seed123 v2 used --subtask ner. Results valid for joint-mode analysis but NOT comparable for NER 3-seed protocol. Need NER-only rerun.\", \"log_path\": \"output/exp_001_seed456_v2/run.log\", \"checkpoint_path\": \"output/exp_001_seed456_v2/\"}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-14T17:12:14.682Z\", \"hypothesis\": \"SciERC joint NER+RE seed=456 v2: early pipeline version. Tests multi-seed stability of signal rankings on joint extraction task.\"}, \"exp_017_llama_conll_infer\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T17:33:23.653Z\", \"updated_at\": \"2026-05-17T02:57:21.948Z\", \"spec\": {\"hypothesis\": \"LLaMA-3.1-8B CoNLL-2003 inference: cross-model cross-dataset validation of structural consistency signals\", \"plan_id\": \"exp-017\", \"parent\": \"exp_017_llama_conll\", \"command\": \"python code/run_llama_conll_infer.py\", \"server\": \"autodl-5090\", \"data_path\": \"conll2003 test\", \"data_count\": 3453, \"model_name\": \"LLaMA-3.1-8B-Instruct\", \"seed\": 42, \"n_samples\": 8, \"temperature\": 1, \"description\": \"LLaMA CoNLL-2003 NER inference N=8 (cross-model + cross-dataset validation)\"}, \"metrics\": {\"greedy_f1\": 0.9266, \"oracle_f1\": 0.9443, \"oracle_headroom\": 0.0177, \"n_instances\": 3453, \"n_valid\": 2756, \"n_conditional\": 2642, \"N\": 8, \"full\": {\"SJ_rho\": 0.4314, \"FK_rho\": 0.4277, \"logprob_rho\": 0.3072, \"EM_rho\": 0.4306, \"voting_conf_rho\": 0.4256, \"SJ_AUROC\": 0.7039, \"FK_AUROC\": 0.7026, \"logprob_AUROC\": 0.761, \"EM_AUROC\": 0.7046, \"voting_conf_AUROC\": 0.7088, \"SJ_ECE\": 0.1137, \"FK_ECE\": 0.1053, \"logprob_ECE\": 0.129, \"EM_ECE\": 0.1094, \"voting_conf_ECE\": 0.0949}, \"conditional\": {\"SJ_rho\": 0.4356, \"FK_rho\": 0.431, \"logprob_rho\": 0.3282, \"EM_rho\": 0.4403, \"voting_conf_rho\": 0.3743, \"SJ_AUROC\": 0.7225, \"FK_AUROC\": 0.7208, \"logprob_AUROC\": 0.8102, \"EM_AUROC\": 0.7257, \"voting_conf_AUROC\": 0.6989, \"SJ_ECE\": 0.0829, \"FK_ECE\": 0.0796, \"logprob_ECE\": 0.0922, \"EM_ECE\": 0.0754, \"voting_conf_ECE\": 0.0784}}, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll_infer/samples.jsonl\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_017_llama_conll_infer/\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T17:55:33.476Z\", \"notes\": \"LLaMA CoNLL-2003 NER N=8 (not N=16, cost constraint: 3453 test instances). SJ ρ=0.431 > logprob ρ=0.307 (Δ=+0.124). ρ-AUROC dissociation: logprob AUROC=0.761 > SJ AUROC=0.704. All 4 structural signals ρ>0.42 vs logprob 0.31. Directly comparable to exp_002 (Qwen CoNLL N=8) and exp_007 (LLaMA SciERC N=8).\", \"hypothesis\": \"LLaMA CoNLL N=8 baseline inference: initial cross-model test on CoNLL before scaling to N=16. Establishes LLaMA can do CoNLL NER effectively.\"}, \"exp_003_wnut17_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T15:32:56.415Z\", \"updated_at\": \"2026-05-17T02:57:20.068Z\", \"spec\": {\"description\": \"WNUT-17 retrain: downsample gold-empty instances to ≤25%, fine-tune Qwen3-8B, inference N=16 T=1.0 with log-probs\", \"hypothesis\": \"After removing excess empty instances, structural consistency signals (SJ) will show stronger correlation on social media NER\", \"plan_id\": \"exp-003\", \"claim\": 1, \"model_name\": \"Qwen3-8B\", \"dataset\": \"WNUT-17 (downsampled)\", \"priority\": \"P0\", \"parent\": \"exp_003_ner_wnut17\", \"command\": \"CUDA_VISIBLE_DEVICES=1 llamafactory-cli train train_config_wnut17.yaml\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/wnut17/llmfactory_train_downsampled.json\", \"data_count\": 1637, \"seed\": 42, \"pid\": 92215, \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/logs/train_wnut17.log\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-wnut17-lora\", \"downsampling\": \"empty instances 63.8% -> 25.0%, total 3394 -> 1637\", \"metrics\": {\"train_loss\": 0.105, \"eval_loss\": 0.0836, \"epochs\": 5, \"train_time_min\": 16.37, \"train_samples_per_sec\": 8.33}, \"note\": \"D045: Training succeeded (train_loss=0.105) but inference FAIL: 54% F1=0, SJ rho=0.062 (p=0.106). WNUT-17 abandoned — model capability insufficient on social media NER. Paper reports as Claim 3 (capability boundary) evidence.\"}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-14T18:11:36.559Z\", \"hypothesis\": \"WNUT-17 NER evaluation v2: tests signal effectiveness on noisy social media text. Hypothesis: structural signals remain effective on noisy, informal text with high entity variation.\"}, \"exp_001_seed456_v2_ner\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T17:13:00.414Z\", \"updated_at\": \"2026-05-17T02:57:18.227Z\", \"spec\": {\"hypothesis\": \"NER N=16 seed=456 robustness test (NER-only rerun, fixing subtask mismatch from exp_001_seed456_v2)\", \"plan_id\": \"exp-001\", \"parent\": \"exp_001_seed456_v2\", \"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=2 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask ner --n_samples 16 --temperature 1.0 --seed 456 --num_test 9999 --collect_logprobs --output_dir output/exp_001_seed456_v2_ner\", \"server\": \"autodl-5090\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 456, \"checkpoint_source\": \"checkpoints/qwen3-8b-scierc-merged-v2\", \"eval_data\": \"data/scierc/processed_data\", \"metrics\": {\"sj_rho\": 0.384, \"structural_gt_surface\": true, \"structural_surface_delta\": 0.16}, \"log_path\": \"output/exp_001_seed456_v2_ner.log\", \"checkpoint_path\": \"output/exp_001_seed456_v2_ner/\"}, \"log_path\": \"output/exp_001_seed456_v2_ner.log\", \"pid\": 96161, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T17:52:01.372Z\", \"metrics\": {\"full\": {\"SJ\": {\"rho\": 0.384, \"auroc\": 0.711}, \"FK\": {\"rho\": 0.223, \"auroc\": 0.577}, \"logprob\": {\"rho\": 0.232, \"auroc\": 0.594}, \"EM\": {\"rho\": 0.316, \"auroc\": 0.768}, \"voting_conf\": {\"rho\": 0.411, \"auroc\": 0.712}}, \"conditional\": {\"SJ\": {\"rho\": 0.349, \"auroc\": 0.699}, \"FK\": {\"rho\": 0.157, \"auroc\": 0.561}, \"logprob\": {\"rho\": 0.171, \"auroc\": 0.576}, \"EM\": {\"rho\": 0.406, \"auroc\": 0.78}, \"voting_conf\": {\"rho\": 0.346, \"auroc\": 0.694}}, \"3seed_mean_SJ_rho_full\": 0.412, \"3seed_sd_SJ_rho_full\": 0.025, \"structural_beats_surface\": true, \"verdict\": \"MARGINAL\"}, \"hypothesis\": \"SciERC NER seed=456 v2: corrected pipeline rerun with gold-filtering. Part of multi-seed validation protocol for NER signal ranking stability.\"}, \"exp_009_v2_re_rerun\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:56:31.535Z\", \"updated_at\": \"2026-05-17T02:57:16.383Z\", \"spec\": {\"command\": \"python code/exp_009_v2_re_rerun.py\", \"server\": \"autodl-5090\", \"data_path\": \"output/exp_008_re_n16_v2/samples.jsonl\", \"data_count\": 397, \"model_name\": \"cpu_analysis\", \"seed\": 42, \"checkpoint_source\": \"exp_008_re_n16_v2\", \"checkpoint_path\": \"output/exp_009_v2_re_rerun/results.json\", \"log_path\": \"/tmp/re_rerun.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T18:56:58.168Z\", \"hypothesis\": \"Capability stratification v2 (RE rerun): corrected stratification analysis for RE with proper gold-filtering. Fixes early pipeline bug affecting RE quartile ρ values.\"}, \"exp_007_llama_n16\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T18:31:44.366Z\", \"updated_at\": \"2026-05-17T02:57:12.521Z\", \"spec\": {\"hypothesis\": \"LLaMA SciERC N=16: cross-model N-scaling validation. If SJ rho increases from N=8 (0.363) to N=16, N-scaling is model-agnostic.\", \"plan_id\": \"exp-007\", \"parent\": \"exp_007_llama_inference\", \"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=1 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-scierc-merged --data_dir data/scierc/processed_data --dataset scierc --subtask ner --n_samples 16 --temperature 1.0 --seed 42 --num_test 9999 --collect_logprobs --output_dir output/exp_007_llama_n16\", \"server\": \"autodl-5090\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"llama3.1-8b-scierc-merged\", \"seed\": 42, \"checkpoint_source\": \"checkpoints/llama3.1-8b-scierc-merged\", \"eval_data\": \"data/scierc/processed_data\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"output/exp_007_llama_n16/samples.jsonl\", \"log_path\": \"output/exp_007_llama_n16.log\", \"completed_at\": \"2026-05-14T19:03:39.163Z\", \"metrics\": {\"N\": 16, \"dataset\": \"scierc\", \"subtask\": \"ner\", \"n_instances\": 551, \"n_valid\": 529, \"n_conditional\": 478, \"greedy_f1\": 0.645, \"full\": {\"SJ_rho\": 0.3791, \"FK_rho\": 0.3081, \"logprob_rho\": 0.2041, \"EM_rho\": 0.3159, \"voting_conf_rho\": 0.4515, \"SJ_AUROC\": 0.717, \"FK_AUROC\": 0.6581, \"logprob_AUROC\": 0.5656, \"EM_AUROC\": 0.7686, \"voting_conf_AUROC\": 0.7266, \"SJ_ECE\": 0.1019, \"FK_ECE\": 0.1556, \"logprob_ECE\": 0.084, \"EM_ECE\": 0.1761, \"voting_conf_ECE\": 0.1365}, \"conditional\": {\"SJ_rho\": 0.3222, \"FK_rho\": 0.2182, \"logprob_rho\": 0.1286, \"EM_rho\": 0.3563, \"voting_conf_rho\": 0.3356, \"SJ_AUROC\": 0.7014, \"FK_AUROC\": 0.6392, \"logprob_AUROC\": 0.545, \"EM_AUROC\": 0.7708, \"voting_conf_AUROC\": 0.6988, \"SJ_ECE\": 0.1466, \"FK_ECE\": 0.1853, \"logprob_ECE\": 0.1141, \"EM_ECE\": 0.1887, \"voting_conf_ECE\": 0.2634}, \"n8_vs_n16_delta_rho_full\": {\"SJ\": 0.0161, \"FK\": -0.0185, \"logprob\": 0.0214, \"EM\": 0.0007, \"voting_conf\": 0.0184}}, \"hypothesis\": \"LLaMA SciERC N=16: cross-model NER signal evaluation at higher sample count. Tests if LLaMA shows same N-scaling benefit for structural signals as Qwen.\"}, \"exp_017_llama_conll_n16\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T19:19:35.318Z\", \"updated_at\": \"2026-05-17T02:56:57.283Z\", \"spec\": {\"hypothesis\": \"LLaMA CoNLL N=16: complete the 2x2 matrix (model x dataset x N). If SJ N-scaling holds for LLaMA on CoNLL, the finding is fully cross-model cross-dataset.\", \"plan_id\": \"exp-017\", \"parent\": \"exp_017_llama_conll_infer\", \"model_name\": \"llama3.1-8b-conll2003-merged\", \"dataset\": \"CoNLL-2003\", \"data_count\": 3453, \"seed\": 42, \"server\": \"autodl-5090\", \"command\": \"CUDA_VISIBLE_DEVICES=0 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 16 --temperature 1.0 --seed 42 --num_test 9999 --collect_logprobs --output_dir output/exp_017_llama_conll_n16\", \"data_path\": \"data/conll2003\", \"pid\": 106997, \"n_samples\": 16, \"temperature\": 1, \"checkpoint_source\": \"checkpoints/llama3.1-8b-conll2003-merged\", \"eval_data\": \"conll2003 test set\", \"checkpoint_path\": \"output/exp_017_llama_conll_n16/samples.jsonl\", \"log_path\": \"output/exp_017_llama_conll_n16/all_signals_report.json\"}, \"metrics\": {\"greedy_f1\": 0.9243, \"oracle_f1\": 0.9487, \"oracle_headroom\": 0.0244, \"n_instances\": 3453, \"n_valid\": 2756, \"n_conditional\": 2642, \"structural_beats_surface\": true, \"full\": {\"SJ_rho\": 0.4642, \"SJ_AUROC\": 0.7391, \"SJ_ECE\": 0.1131, \"FK_rho\": 0.4566, \"FK_AUROC\": 0.736, \"FK_ECE\": 0.1071, \"logprob_rho\": 0.3058, \"logprob_AUROC\": 0.7594, \"logprob_ECE\": 0.1288, \"EM_rho\": 0.4613, \"EM_AUROC\": 0.7391, \"EM_ECE\": 0.1084, \"voting_conf_rho\": 0.4554, \"voting_conf_AUROC\": 0.7406, \"voting_conf_ECE\": 0.0844}, \"conditional\": {\"SJ_rho\": 0.4597, \"SJ_AUROC\": 0.7565, \"SJ_ECE\": 0.0846, \"FK_rho\": 0.4515, \"FK_AUROC\": 0.753, \"FK_ECE\": 0.0813, \"logprob_rho\": 0.3193, \"logprob_AUROC\": 0.8023, \"logprob_ECE\": 0.0921, \"EM_rho\": 0.4618, \"EM_AUROC\": 0.7589, \"EM_ECE\": 0.0757, \"voting_conf_rho\": 0.3978, \"voting_conf_AUROC\": 0.7287, \"voting_conf_ECE\": 0.0742}, \"best_of_n\": {\"greedy\": 0.9243, \"random_avg\": 0.9213, \"sj_best\": 0.9259, \"logprob_best\": 0.925, \"voting_conf_best\": 0.9268, \"oracle\": 0.9487}, \"n8_vs_n16_delta\": {\"full_SJ_rho_delta\": 0.0328, \"full_FK_rho_delta\": 0.0289, \"full_logprob_rho_delta\": -0.0014, \"full_EM_rho_delta\": 0.0307, \"full_voting_conf_rho_delta\": 0.0298, \"cond_SJ_rho_delta\": 0.0241, \"cond_FK_rho_delta\": 0.0205, \"cond_logprob_rho_delta\": -0.0089, \"cond_EM_rho_delta\": 0.0215, \"cond_voting_conf_rho_delta\": 0.0235}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T19:45:16.265Z\", \"hypothesis\": \"LLaMA CoNLL N=16 seed=42 (original): cross-model validation on CoNLL. First evidence that structural>surface ranking generalizes from Qwen to LLaMA model family.\"}, \"exp_015_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T15:34:23.336Z\", \"updated_at\": \"2026-05-17T02:56:55.830Z\", \"spec\": {\"command\": \"python code/analyze_exp015_v2_metrics.py\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/ (10 datasets)\", \"data_count\": 9148, \"model_name\": \"Qwen3-8B + LLaMA (multi-model)\", \"seed\": \"42,123,456 (multi-seed)\", \"checkpoint_path\": \"N/A (analysis only)\", \"log_path\": \"/tmp/exp015_v2.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T15:34:56.741Z\", \"metrics\": {\"scierc_ner_avg\": {\"sj_auroc\": 0.7394, \"fk_auroc\": 0.6172, \"em_auroc\": 0.7873, \"voting_auroc\": 0.7367, \"logprob_auroc\": 0.5918}, \"scierc_re_avg\": {\"sj_auroc\": 0.6746, \"fk_auroc\": 0.5939, \"em_auroc\": 0.715, \"voting_auroc\": 0.7234, \"logprob_auroc\": 0.5849}}, \"hypothesis\": \"Metrics expansion v2: corrected evaluation with proper conditional filtering. Updates exp_015 with gold-filtered pipeline to fix RE conditional ρ values that used wrong filter criterion.\"}, \"exp_001_n16_seed456\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-14T12:10:30.350Z\", \"updated_at\": \"2026-05-17T02:56:53.526Z\", \"completed_at\": \"2026-05-14T12:28:38.721Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"success\", \"metrics\": {\"ner\": {\"greedy_f1\": 0.6577, \"oracle_f1\": 0.8129, \"headroom\": 0.1553, \"rho_sj_full\": 0.3297, \"rho_fk_full\": 0.2578, \"rho_logprob_full\": 0.2866, \"rho_sj_cond\": 0.3394, \"rho_fk_cond\": 0.2721, \"rho_logprob_cond\": 0.2567, \"sj_beats_fk\": true, \"rho_advantage\": 0.0719}, \"re\": {\"greedy_f1\": 0.4312, \"oracle_f1\": 0.6737, \"headroom\": 0.2425, \"rho_sj_full\": 0.285, \"rho_fk_full\": 0.2372, \"rho_logprob_full\": 0.2626, \"rho_sj_cond\": 0.3525, \"rho_fk_cond\": 0.2614, \"rho_logprob_cond\": 0.1927, \"sj_beats_fk\": true, \"rho_advantage\": 0.0478}, \"verdict\": \"FAIL\"}}}, \"spec\": {\"hypothesis\": \"N=16 seed456 multi-seed robustness verification for SciERC NER+RE\", \"plan_id\": \"exp-001\", \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"seed\": 456, \"command\": \"python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 16 --temperature 1.0 --seed 456 --output_dir output/exp001_n16_seed456 --collect_logprobs\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:0\", \"pid\": \"174595\", \"log_path\": \"output/exp001_n16_seed456_run.log\", \"tmux_session\": \"exp_001_n16_seed456\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (inference-only)\", \"metrics\": {\"instance_count\": 551, \"n_valid\": 529, \"n_gold_empty\": 22, \"parse_rate\": 1, \"ner_greedy_f1\": 0.6617, \"ner_oracle_f1\": 0.8075, \"re_greedy_f1\": 0.4215, \"re_oracle_f1\": 0.4748, \"rho_sj_ner\": 0.4098, \"rho_fk_ner\": 0.2723, \"rho_vc_ner\": 0.4449, \"rho_em_ner\": 0.3363, \"rho_lp_ner\": 0.2415, \"rho_sj_re\": 0.2835, \"rho_fk_re\": 0.2929, \"auroc_sj_ner\": 0.6823, \"auroc_fk_ner\": 0.6179, \"auroc_vc_ner\": 0.6981, \"auroc_em_ner\": 0.649, \"auroc_lp_ner\": 0.5885, \"rho_note\": \"CORRECTED 2026-05-15: old values (rho_fk=0.3448,rho_sj=0.4134) included 22 gold-empty instances. Now uses gold-filtered pipeline (n=529).\"}, \"log_path\": \"output/exp001_n16_seed456_run.log\", \"hypothesis\": \"SciERC N=16 seed=456: early multi-seed validation of structural signal rankings at N=16 sample count. Establishes seed stability for SJ/FK/VC/EM ordering.\"}, \"exp_011_ood_scierc_to_conll\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:36:07.210Z\", \"updated_at\": \"2026-05-17T02:56:29.417Z\", \"spec\": {\"hypothesis\": \"SCS structural signals remain effective under domain shift (SciERC model on CoNLL data)\", \"plan_id\": \"exp-011\", \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"data_path\": \"data/conll2003\", \"seed\": 42, \"pid\": 179761, \"server\": \"autodl-5090\", \"gpu\": \"cuda:3\", \"command\": \"python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --dataset conll2003 --data_dir data/conll2003 --subtask ner --n_samples 8 --temperature 1.0 --max_tokens 1024 --seed 42 --collect_logprobs --output_dir output/exp_011_ood_scierc_to_conll\", \"data_count\": 3500}, \"conclusion\": \"success\", \"checkpoint_path\": \"output/exp_011_ood_scierc_to_conll/samples.jsonl\", \"log_path\": \"output/exp_011_ood_scierc_to_conll/report.json\", \"completed_at\": \"2026-05-15T11:47:47.953Z\", \"metrics\": {\"greedy_ner_f1\": 0.522, \"rho_vc\": 0.469, \"rho_sj\": 0.378, \"rho_em\": 0.3, \"rho_fk\": 0.285, \"rho_lp\": 0.246}, \"hypothesis\": \"Out-of-domain transfer: SciERC-trained model on CoNLL data. Tests if confidence signals work under partial schema overlap (SciERC has Organization/Person which overlap with CoNLL ORG/PER). Complement to exp_011_ood_conll_to_scierc.\"}, \"exp_qwen3_4b_scierc_finetune_v4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:26:25.512Z\", \"updated_at\": \"2026-05-17T02:56:24.418Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && llamafactory-cli train train_config_scierc_4b.yaml\\\"\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:0\", \"pid\": \"227123\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_qwen3_4b_scierc_finetune_v4.log\", \"submitted_at\": \"2026-05-15T19:26:31.444Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"wall_clock_seconds\": 1668.8, \"gpu_hours\": 0.46}, \"conclusion\": \"success\", \"metrics\": {\"total_steps\": 585, \"completed_steps\": 585, \"best_checkpoint\": \"checkpoint-400\", \"best_eval_loss\": 0.0898, \"epochs\": 5}, \"checkpoint_path\": \"checkpoints/qwen3-4b-scierc-merged/\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_qwen3_4b_scierc_finetune_v4.log\", \"completed_at\": \"2026-05-15T19:54:20.255Z\", \"hypothesis\": \"Qwen3-4B SciERC LoRA fine-tune v4: training the smaller 4B model to complete the 2x2 scale matrix (4B×SciERC cell). Validates that fine-tuning convergence patterns hold across model scales.\"}, \"exp_011_ood_conll_to_scierc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T11:36:08.325Z\", \"updated_at\": \"2026-05-17T02:56:14.242Z\", \"spec\": {\"hypothesis\": \"SCS structural signals remain effective under domain shift (CoNLL model on SciERC data, joint NER+RE)\", \"plan_id\": \"exp-011\", \"model_name\": \"qwen3-8b-conll2003-merged\", \"data_path\": \"data/scierc/processed_data\", \"seed\": 42, \"server\": \"autodl-5090\", \"gpu\": \"cuda:3\", \"pid\": 181723, \"command\": \"python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-conll2003-merged --dataset scierc --data_dir data/scierc/processed_data --subtask joint --n_samples 8 --temperature 1.0 --max_tokens 1024 --seed 42 --collect_logprobs --output_dir output/exp_011_ood_conll_to_scierc\", \"data_count\": 551}, \"conclusion\": \"negative\", \"checkpoint_path\": \"output/exp_011_ood_conll_to_scierc/samples.jsonl\", \"log_path\": \"output/exp_011_ood_conll_to_scierc/report.json\", \"completed_at\": \"2026-05-15T11:50:21.969Z\", \"metrics\": {\"greedy_ner_f1\": 0.009, \"greedy_re_f1\": 0.001, \"avg_structural_rho\": -0.05, \"verdict\": \"FAIL\", \"reason\": \"schema_incompatibility\", \"direction\": \"CoNLL_model_to_SciERC_data\", \"sample_f1_pct_zero_ner\": 98.06, \"rho_sj_ner\": -0.186, \"rho_fk_ner\": -0.069, \"note\": \"Schema incompatibility (CoNLL PER/ORG/LOC/MISC vs SciERC Task/Method/Material) causes catastrophic failure. Cannot evaluate confidence signals.\"}, \"hypothesis\": \"Out-of-domain transfer test: CoNLL-trained model on SciERC data. Tests if confidence signals retain correlation with quality under severe schema mismatch (CoNLL PER/ORG/LOC/MISC vs SciERC Task/Method/Material).\"}, \"exp_freeform_seed789_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:24:26.805Z\", \"updated_at\": \"2026-05-17T02:56:11.818Z\", \"spec\": {\"log_path\": \"~/runs/struct_self_consist_ie/exp_freeform_seed789_v3.log\", \"checkpoint_path\": \"results/exp_freeform_ablation_seed789/\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T19:30:51.048Z\", \"metrics\": {\"n_instances\": 551, \"n_samples\": 8, \"parse_rate_pct\": 100, \"elapsed_seconds\": 229.7, \"freeform_ner_selection_gap\": 0.0028, \"freeform_re_selection_gap\": 0.0219, \"freeform_lp_std\": 0.0183, \"freeform_lp_range\": 0.054908, \"freeform_tied_pct\": 59, \"re_lp_flip_positive\": true, \"variance_ratio_std\": 0.89, \"variance_ratio_range\": 0.88}, \"hypothesis\": \"Free-form SciERC seed=789 v3 (bugfix rerun): corrected version of free-form inference after fixing parsing/generation issues in v1/v2. Provides clean data point for 4-seed free-form analysis.\"}, \"exp_freeform_seed789\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T18:38:29.851Z\", \"updated_at\": \"2026-05-17T02:56:09.888Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && python run_freeform_inference.py --seed 789 --num_samples 8 --temperature 1.0 --max_tokens 1024 --output_dir results/exp_freeform_ablation_seed789\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:3\"], \"pid\": \"216722\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_freeform_seed789.log\", \"submitted_at\": \"2026-05-15T18:58:46.406Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 92.2, \"gpu_hours\": 0.03}, \"notes\": \"Rerun with fixed seed-passing code on cuda:3. Original run was killed for GPU reallocation. Parse rate 100%, 227.5s elapsed. LP compression confirmed: tied_pct=59.0% (vs constrained 59.7%), variance_ratio=0.89x.\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T19:00:18.576Z\", \"metrics\": {\"inference\": {\"n_instances\": 551, \"n_samples\": 8, \"total_samples\": 4408, \"total_parsed\": 4408, \"parse_rate_pct\": 100, \"elapsed_seconds\": 227.5}, \"freeform\": {\"selection_ner\": {\"greedy\": 0.6205, \"selected\": 0.6232, \"gap\": 0.0027}, \"selection_re\": {\"greedy\": 0.2909, \"selected\": 0.31, \"gap\": 0.0191}, \"logprob_variance\": {\"mean_std\": 0.0183, \"mean_range\": 0.054908, \"tied_pct\": 59}, \"qe_ner\": {\"n\": 529, \"SJ\": {\"rho\": 0.393995, \"auroc\": 0.734474}, \"FK\": {\"rho\": 0.312292, \"auroc\": 0.794384}, \"LP\": {\"rho\": 0.247096, \"auroc\": 0.677824}, \"EM\": {\"rho\": 0.320383, \"auroc\": 0.527033}, \"VC\": {\"rho\": 0.420625, \"auroc\": 0.768111}}, \"qe_re\": {\"n\": 397, \"SJ\": {\"rho\": 0.201746, \"auroc\": 0.574388}, \"FK\": {\"rho\": 0.2202, \"auroc\": 0.633014}, \"LP\": {\"rho\": 0.295765, \"auroc\": 0.687067}, \"EM\": {\"rho\": 0.103633, \"auroc\": 0.474737}, \"VC\": {\"rho\": 0.306868, \"auroc\": 0.642197}}}, \"constrained_ref\": {\"selection_ner\": {\"greedy\": 0.6182, \"selected\": 0.6241, \"gap\": 0.0059}, \"selection_re\": {\"greedy\": 0.2913, \"selected\": 0.2845, \"gap\": -0.0068}, \"logprob_variance\": {\"mean_std\": 0.020589, \"mean_range\": 0.062305, \"tied_pct\": 59.7}}, \"comparison\": {\"variance_ratio_std\": 0.89, \"variance_ratio_range\": 0.88, \"tied_reduction_pp\": 0.7}}, \"hypothesis\": \"Free-form SciERC seed=789: multi-seed replication of free-form ablation. Validates LP compression persistence and structural signal robustness across sampling seeds under unconstrained generation.\"}, \"exp_freeform_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T17:14:48.842Z\", \"updated_at\": \"2026-05-17T02:56:09.256Z\", \"spec\": {\"hypothesis\": \"Multi-seed free-form ablation (seed=456): verify RE LP flip and NER gap stability\", \"command\": \"python run_freeform_inference.py --seed 456 --num_samples 8 --temperature 1.0 --max_tokens 1024 --output_dir results/exp_freeform_ablation_seed456\", \"server\": \"autodl-5090\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 456, \"gpu\": \"cuda:2\", \"tmux_session\": \"exp_freeform_seed456\", \"log_path\": \"results/exp_freeform_ablation_seed456/run_summary.json\", \"checkpoint_path\": \"results/exp_freeform_ablation_seed456\"}, \"metrics\": {\"inference\": {\"n_instances\": 551, \"n_samples\": 8, \"total_samples\": 4408, \"total_parsed\": 4407, \"parse_rate_pct\": 99.98, \"elapsed_seconds\": 232.4}, \"freeform\": {\"selection_ner\": {\"greedy\": 0.6198, \"selected\": 0.6205, \"gap\": 0.0007}, \"selection_re\": {\"greedy\": 0.2908, \"selected\": 0.3108, \"gap\": 0.02}, \"logprob_variance\": {\"mean_std\": 0.018631, \"mean_range\": 0.056792, \"tied_pct\": 58.4}, \"qe_ner\": {\"n\": 529, \"SJ\": {\"rho\": 0.378498, \"auroc\": 0.707769}, \"FK\": {\"rho\": 0.286163, \"auroc\": 0.754779}, \"LP\": {\"rho\": 0.227089, \"auroc\": 0.672081}, \"EM\": {\"rho\": 0.319997, \"auroc\": 0.47789}, \"VC\": {\"rho\": 0.416853, \"auroc\": 0.756543}}, \"qe_re\": {\"n\": 397, \"SJ\": {\"rho\": 0.211331, \"auroc\": 0.572335}, \"FK\": {\"rho\": 0.259074, \"auroc\": 0.652998}, \"LP\": {\"rho\": 0.306382, \"auroc\": 0.70134}, \"EM\": {\"rho\": 0.1043, \"auroc\": 0.461641}, \"VC\": {\"rho\": 0.301507, \"auroc\": 0.628873}}}, \"constrained_ref\": {\"selection_ner\": {\"greedy\": 0.6182, \"selected\": 0.6241, \"gap\": 0.0059}, \"selection_re\": {\"greedy\": 0.2913, \"selected\": 0.2845, \"gap\": -0.0068}, \"logprob_variance\": {\"mean_std\": 0.020589, \"mean_range\": 0.062305, \"tied_pct\": 59.7}}, \"comparison\": {\"variance_ratio_std\": 0.9, \"variance_ratio_range\": 0.91, \"tied_reduction_pp\": 1.3}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T19:12:29.413Z\", \"hypothesis\": \"Free-form SciERC seed=456: multi-seed replication of free-form ablation. Validates LP compression persistence and structural signal robustness across sampling seeds under unconstrained generation.\"}, \"exp_freeform_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T17:14:47.765Z\", \"updated_at\": \"2026-05-17T02:56:06.903Z\", \"spec\": {\"hypothesis\": \"Multi-seed free-form ablation (seed=123): verify RE LP flip and NER gap stability\", \"command\": \"python run_freeform_inference.py --seed 123 --num_samples 8 --temperature 1.0 --max_tokens 1024 --output_dir results/exp_freeform_ablation_seed123\", \"server\": \"autodl-5090\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 123, \"gpu\": \"cuda:1\", \"tmux_session\": \"exp_freeform_seed123\", \"log_path\": \"results/exp_freeform_ablation_seed123/run_summary.json\", \"checkpoint_path\": \"results/exp_freeform_ablation_seed123\"}, \"metrics\": {\"inference\": {\"n_instances\": 551, \"n_samples\": 8, \"total_samples\": 4408, \"total_parsed\": 4406, \"parse_rate_pct\": 99.95, \"elapsed_seconds\": 228.1}, \"freeform\": {\"selection_ner\": {\"greedy\": 0.6194, \"selected\": 0.6222, \"gap\": 0.0028}, \"selection_re\": {\"greedy\": 0.2874, \"selected\": 0.305, \"gap\": 0.0176}, \"logprob_variance\": {\"mean_std\": 0.019881, \"mean_range\": 0.059864, \"tied_pct\": 57.7}, \"qe_ner\": {\"n\": 529, \"SJ\": {\"rho\": 0.384214, \"auroc\": 0.748728}, \"FK\": {\"rho\": 0.323956, \"auroc\": 0.766039}, \"logprob\": {\"rho\": 0.217297, \"auroc\": 0.701657}, \"EM\": {\"rho\": 0.326887, \"auroc\": 0.52533}, \"voting_conf\": {\"rho\": 0.407893, \"auroc\": 0.799676}}, \"qe_re\": {\"n\": 397, \"SJ\": {\"rho\": 0.272776, \"auroc\": 0.614056}, \"FK\": {\"rho\": 0.314429, \"auroc\": 0.678534}, \"logprob\": {\"rho\": 0.309673, \"auroc\": 0.70414}, \"EM\": {\"rho\": 0.137216, \"auroc\": 0.487342}, \"voting_conf\": {\"rho\": 0.316667, \"auroc\": 0.647442}}}, \"constrained_ref\": {\"selection_ner\": {\"greedy\": 0.6182, \"selected\": 0.6241, \"gap\": 0.0059}, \"selection_re\": {\"greedy\": 0.2913, \"selected\": 0.2845, \"gap\": -0.0068}}, \"comparison\": {\"variance_ratio_std\": 0.97, \"variance_ratio_range\": 0.96, \"tied_reduction_pp\": 2}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-15T19:29:48.939Z\", \"hypothesis\": \"Free-form SciERC seed=123: multi-seed replication of free-form ablation. Validates LP compression persistence and structural signal robustness across sampling seeds under unconstrained generation.\"}, \"exp_009_capability_stratification\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T14:59:24.201Z\", \"updated_at\": \"2026-05-17T02:56:02.685Z\", \"spec\": {\"command\": \"python code/exp009_stratification_analysis.py\", \"server\": \"autodl-5090\", \"data_path\": \"output/exp001_n16_seed42 + output/exp008_re_n16 + output/exp002_conll2003\", \"data_count\": 4555, \"model_name\": \"analysis_only\", \"seed\": 42}, \"conclusion\": \"success\", \"checkpoint_path\": \"output/exp009_stratification_results.json\", \"log_path\": \"/tmp/exp009.log\", \"completed_at\": \"2026-05-14T14:59:46.463Z\", \"metrics\": {\"scierc_ner\": {\"n\": 551, \"sj_rho_overall\": 0.398, \"by_greedy_f1\": {\"hard_0_25_sj_rho\": 0.159, \"med_low_sj_rho\": 0.139, \"med_high_sj_rho\": 0.09, \"easy_sj_rho\": 0.23}, \"by_sent_len\": {\"Q1_sj_rho\": 0.461, \"Q2_sj_rho\": 0.401, \"Q3_sj_rho\": 0.296, \"Q4_sj_rho\": 0.382}, \"by_ent_count\": {\"0_sj_rho\": 0.689, \"1_2_sj_rho\": 0.415, \"3_5_sj_rho\": 0.353, \"6plus_sj_rho\": 0.547}}, \"scierc_re\": {\"n\": 551, \"by_greedy_f1\": {\"hard_0_25_sj_rho\": -0.043, \"easy_sj_rho\": 0.21}, \"by_sent_len\": {\"Q1_sj_rho\": 0.447, \"Q4_sj_rho\": 0.54}, \"by_rel_count\": {\"0_sj_rho\": 0.62, \"1_2_sj_rho\": 0.275, \"6plus_sj_rho\": 0.527}}, \"conll_ner\": {\"n\": 3453, \"by_sent_len\": {\"Q1_sj_rho\": 0.334, \"Q3_sj_rho\": 0.518}}, \"proxy_independence\": {\"scierc_ner_f1_vs_slen\": -0.021, \"scierc_ner_f1_vs_ecnt\": 0.007, \"scierc_re_f1_vs_slen\": -0.147}}, \"notes\": \"Registry metrics are PRE-gold-filter (n=551). Paper uses exp_009_v2_re_rerun (gold-filtered n=397): RE Q1_sj_rho=0.110, Q4_sj_rho=0.473. Registry values (Q1=0.447, Q4=0.540) are SUPERSEDED.\", \"hypothesis\": \"Capability stratification analysis: test if SJ signal effectiveness varies with instance difficulty (greedy F1 quartiles), sentence length, and entity/relation count. Identifies which instance subpopulations benefit most from structural consistency signals.\"}, \"exp_023_lora_rank8\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T10:29:59.501Z\", \"updated_at\": \"2026-05-17T02:55:50.540Z\", \"spec\": {\"hypothesis\": \"LoRA rank=8 ablation: does reducing rank from 32 to 8 significantly affect correlation-selection patterns?\", \"model_name\": \"Qwen/Qwen3-8B\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/llmfactory_train.json\", \"data_count\": 1861, \"server\": \"autodl-5090\", \"seed\": 42, \"parent\": \"ft_002_v2\", \"method\": \"LoRA r=8 alpha=16, 5 epochs, batch=2 grad_accum=8 gradient_checkpointing=true\", \"gpu\": \"cuda:2\", \"pid\": 288382, \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/logs/exp023_rank8_train.log\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-scierc-lora-rank8\", \"command\": \"CUDA_VISIBLE_DEVICES=2 llamafactory-cli train train_config_rank8.yaml\", \"trainable_params\": \"21.8M\", \"total_steps\": 585, \"estimated_runtime\": \"26min\"}, \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 0.1018, \"eval_loss\": 0.0776, \"train_runtime\": \"28m45s\", \"ner_full\": {\"n\": 529, \"greedy_f1\": 0.6397, \"oracle_f1\": 0.7998, \"oracle_headroom\": 0.1601, \"degeneracy_rate\": 0.072, \"SJ_rho\": 0.3649, \"FK_rho\": 0.2838, \"VC_rho\": 0.394, \"EM_rho\": 0.2562, \"LP_rho\": 0.2105, \"SJ_auroc\": 0.689, \"FK_auroc\": 0.6002, \"VC_auroc\": 0.6886, \"EM_auroc\": 0.7265, \"LP_auroc\": 0.6054, \"sel_SJ\": 0.6306, \"sel_FK\": 0.6265, \"sel_VC\": 0.5919, \"sel_EM\": 0.6073, \"sel_LP\": 0.635}, \"ner_cond\": {\"n\": 477, \"SJ_rho\": 0.3056, \"FK_rho\": 0.1452, \"VC_rho\": 0.3191, \"EM_rho\": 0.3558, \"LP_rho\": 0.169}, \"re_full\": {\"n\": 397, \"greedy_f1\": 0.3712, \"oracle_f1\": 0.609, \"oracle_headroom\": 0.2378, \"degeneracy_rate\": 0.217, \"SJ_rho\": 0.2244, \"FK_rho\": 0.3448, \"VC_rho\": 0.3617, \"EM_rho\": 0.068, \"LP_rho\": 0.2737, \"SJ_auroc\": 0.7092, \"FK_auroc\": 0.6469, \"VC_auroc\": 0.7533, \"EM_auroc\": 0.7306, \"LP_auroc\": 0.6325, \"sel_SJ\": 0.3584, \"sel_FK\": 0.3498, \"sel_VC\": 0.3715, \"sel_EM\": 0.3291, \"sel_LP\": 0.3606}, \"re_cond\": {\"n\": 242, \"SJ_rho\": 0.3601, \"FK_rho\": 0.2343, \"VC_rho\": 0.3703, \"EM_rho\": 0.4613, \"LP_rho\": 0.1809}}, \"completed_at\": \"2026-05-16T11:22:34.576Z\", \"hypothesis\": \"LoRA rank=8 ablation on SciERC: test if reduced model capacity (rank 8 vs 32) changes signal effectiveness ranking or correlation-selection gap pattern. Verifies findings are not rank-specific artifacts.\", \"parent\": \"exp_012_rerun_1024\"}, \"exp_022_seed789\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T10:08:27.375Z\", \"updated_at\": \"2026-05-17T02:55:49.870Z\", \"hypothesis\": \"3rd seed SciERC inference (seed=789) with ft_002_v2 (Qwen3-8B). N=8, T=1.0, joint NER+RE, logprobs collected. Complements seed42 (exp_012_rerun_1024) and seed123/456 for multi-seed analysis.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 1.0 --seed 789 --num_test 9999 --max_tokens 1024 --collect_logprobs --output_dir output/exp_022_seed789/\", \"server\": \"autodl-5090\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"Qwen3-8B (qwen3-8b-scierc-merged-v2)\", \"seed\": 789, \"checkpoint_path\": \"checkpoints/qwen3-8b-scierc-merged-v2\", \"log_path\": \"output/exp_022_seed789/run.log\", \"gpu\": \"cuda:0\", \"pid\": 286743, \"account\": \"root\", \"backend\": \"tmux\", \"tmux_session\": \"exp_022_seed789\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T14:25:17.461Z\", \"parent\": \"exp_012_rerun_1024\"}, \"exp_025_n32\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T13:38:26.420Z\", \"updated_at\": \"2026-05-17T02:55:46.212Z\", \"spec\": {\"checkpoint_path\": \"checkpoints/qwen3-8b-scierc-merged-v2\", \"log_path\": \"output/exp_025_n32/run.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T14:25:39.849Z\", \"metrics\": {\"n_samples\": 32, \"degeneracy_pct\": 4, \"lp_range\": 0.0781, \"oracle_f1\": 0.8412, \"greedy_f1\": 0.6615, \"oracle_gap\": 0.1797, \"selection_f1_lp_delta\": 0.54, \"selection_f1_sj_delta\": 0.16, \"selection_f1_fk_delta\": 0.6, \"selection_f1_em_delta\": 0.68, \"selection_f1_vc_delta\": -5.21, \"best_signal\": \"EM\", \"best_delta\": 0.68, \"metric_space\": \"micro_f1_filtered_529inst\", \"note\": \"corrected via n_ablation_fixed.py, greedy from inst['greedy'] field\"}, \"hypothesis\": \"N=32 sample ablation on SciERC: test if increasing samples from 8→32 reduces degeneracy and improves selection F1, particularly for structural signals. Validates whether sample count is the bottleneck for signal effectiveness.\", \"parent\": \"exp_012_rerun_1024\"}, \"exp_021_fewnerd_full\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T16:33:44.079Z\", \"updated_at\": \"2026-05-17T02:55:45.560Z\", \"hypothesis\": \"Full Few-NERD LoRA fine-tune (rank=32, α=64, 3 epochs) on SUPERVISED coarse 8-type NER (131k train). 4-GPU DDP on autodl-5090. Post-training: N=8 inference on full test set, T=1.0, seed=42, collect logprobs for SCS metrics.\", \"spec\": {\"gpu\": \"cuda:0,cuda:1,cuda:2,cuda:3\", \"gpu_count\": 4, \"training_mode\": \"DDP\", \"checkpoint_path\": \"output/exp_021_fewnerd_full/checkpoint-6177\", \"log_path\": \"output/exp_021_inference/\"}, \"conclusion\": \"success\", \"metrics\": {\"total_steps\": 6177, \"train_loss\": 0.048, \"eval_loss\": 0.0275, \"train_runtime\": \"3h57m\", \"epochs\": 3, \"final_checkpoint\": \"output/exp_021_fewnerd_full/checkpoint-6177\", \"adapter_path\": \"output/exp_021_fewnerd_full/adapter_model.safetensors\", \"inference_instances\": 37648, \"inference_filtered\": 32565, \"inference_n_samples\": 8, \"greedy_macro_f1\": 0.7478, \"oracle_macro_f1\": 0.8719, \"headroom\": 0.124, \"zero_f1_rate\": 0.119, \"degeneracy_rate\": 0.101, \"lp_within_range_mean\": 0.0879, \"lp_within_range_median\": 0.0662, \"lp_global_rho\": 0.4215, \"lp_cond_rho\": 0.4225, \"sj_global_rho\": 0.3002, \"sj_cond_rho\": 0.2937, \"fk_global_rho\": 0.3132, \"fk_cond_rho\": 0.3093, \"em_global_rho\": 0.2871, \"em_cond_rho\": 0.271, \"vc_global_rho\": 0.3858, \"vc_cond_rho\": 0.3234, \"lp_selection_delta_pp\": 1.36, \"vc_selection_delta_pp\": -1.79, \"sj_selection_delta_pp\": -2.14, \"fk_selection_delta_pp\": -2.26, \"em_selection_delta_pp\": -3.85, \"lp_bootstrap_ci_95_pp\": [1.18, 1.53], \"lp_sample_auroc\": 0.5782, \"vc_sample_auroc\": 0.5354, \"fk_sample_auroc\": 0.521, \"sj_sample_auroc\": 0.5197, \"em_sample_auroc\": 0.5137, \"scenario\": \"A_partial\", \"note\": \"Full analysis (gold-filtered n=32565). Prior simplified analysis used unfiltered data with different metrics.\"}, \"completed_at\": \"2026-05-16T22:04:16.683Z\", \"parent\": \"exp_020_fewnerd_smoke\"}, \"exp_015_metrics_expansion\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T11:47:36.569Z\", \"updated_at\": \"2026-05-17T02:55:35.391Z\", \"spec\": {\"hypothesis\": \"Comprehensive evaluation of all 5 confidence signals with extended metrics\", \"model_name\": \"N/A (reuse pilot_004 samples)\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_012_logprob/samples_with_logprobs.jsonl\", \"data_count\": 551, \"server\": \"autodl-5090\", \"seed\": 42, \"parent\": \"exp_012_logprob_baseline\", \"method\": \"CPU-only analysis: 6 metrics x 5 signals x 2 subtasks (NER+RE)\", \"command\": \"python code/analyze_exp015_metrics_expansion.py\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp015_metrics_expansion\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T12:22:32.661Z\", \"metrics\": {\"data_source\": \"exp_012_logprob/samples_with_logprobs.jsonl\", \"config\": \"N=8, T=1.0, seed=42, model=qwen3-8b-scierc-merged-v2\", \"ner\": {\"n_valid\": 529, \"n_cond\": 501, \"voting_rho_full\": 0.5018, \"voting_rho_cond\": 0.4497, \"voting_auroc\": 0.7279, \"voting_tau\": 0.3766, \"sj_rho_full\": 0.3565, \"sj_rho_cond\": 0.412, \"sj_auroc\": 0.6656, \"sj_tau\": 0.2658, \"em_rho_full\": 0.2566, \"em_rho_cond\": 0.3427, \"em_auroc\": 0.623, \"em_tau\": 0.1924, \"fk_rho_full\": 0.2651, \"fk_rho_cond\": 0.306, \"fk_auroc\": 0.6243, \"fk_tau\": 0.2027, \"logprob_rho_full\": 0.1396, \"logprob_rho_cond\": 0.1627, \"logprob_auroc\": 0.5585, \"logprob_tau\": 0.1006}, \"re\": {\"n_valid\": 397, \"n_cond\": 296, \"voting_rho_full\": 0.4217, \"voting_rho_cond\": 0.463, \"voting_auroc\": 0.7162, \"voting_tau\": 0.327, \"sj_rho_full\": 0.2112, \"sj_rho_cond\": 0.3683, \"sj_auroc\": 0.5816, \"sj_tau\": 0.1619, \"em_rho_full\": 0.1002, \"em_rho_cond\": 0.3607, \"em_auroc\": 0.5036, \"em_tau\": 0.0839, \"fk_rho_full\": 0.2528, \"fk_rho_cond\": 0.3168, \"fk_auroc\": 0.6308, \"fk_tau\": 0.1967, \"logprob_rho_full\": 0.2467, \"logprob_rho_cond\": 0.1457, \"logprob_auroc\": 0.6354, \"logprob_tau\": 0.1808}, \"diagnosis\": \"Unified 5-signal evaluation on single data source. Voting leads NER full (ρ=0.502), SJ retains strength in NER cond (ρ=0.412). All structural signals beat logprob on NER. RE: voting leads both full and cond.\"}, \"notes\": \"RE logprob_rho_cond=0.1457 uses WRONG conditional filter (any sample F1>0, n=331). Correct value: 0.0112 from exp_012_rerun_1024 (greedy_f1>0, n=238). This entry's RE cond values are DEPRECATED.\", \"hypothesis\": \"Unified 5-signal evaluation (SJ/FK/EM/VC/LP) on single canonical data source (exp_012 logprobs). Establishes complete signal ranking with ρ, AUROC, and τ metrics for both NER and RE under consistent conditions.\"}, \"exp_020_fewnerd_smoke\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T10:29:25.272Z\", \"updated_at\": \"2026-05-16T16:33:59.109Z\", \"spec\": {\"checkpoint_path\": \"checkpoints/ft_fewnerd_smoke\", \"log_path\": \"checkpoints/fewnerd_train.log\"}, \"hypothesis\": \"1-epoch LoRA (r16) fine-tune Qwen3-8B on Few-NERD INTRA coarse 8-type (131k train), then N=8 T=1.0 pilot inference on 200 test instances. Re-started training 2026-05-16 18:29 CST on cuda:1, PID 288683. ETA ~22:55 CST.\", \"conclusion\": \"success\", \"metrics\": {\"final_loss\": 0.031, \"total_steps\": 8236, \"training_time\": \"5h54m\", \"pilot_greedy_f1\": 0.8037, \"pilot_instances\": 200, \"merged_model_path\": \"checkpoints/qwen3-8b-fewnerd-merged\"}, \"completed_at\": \"2026-05-16T16:33:59.109Z\"}, \"exp_vc_lp_cascade_selection\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T04:44:02.658Z\", \"updated_at\": \"2026-05-16T06:31:26.755Z\", \"hypothesis\": \"VC-filtered LP selection cascade: test if combining VC (pre-filter) + LP (rank) improves selection F1 over single-signal selection. Addresses SF3 reviewer suggestion. Pure analysis on existing data.\", \"conclusion\": \"killed\", \"spec\": {\"command\": \"N/A - cancelled before execution\", \"server\": \"N/A\", \"data_path\": \"N/A\", \"data_count\": 0, \"model_name\": \"N/A\", \"seed\": 0, \"checkpoint_path\": \"N/A\", \"log_path\": \"N/A\"}, \"completed_at\": \"2026-05-16T06:31:26.755Z\"}, \"exp_tacred_re_benchmark\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T04:43:59.002Z\", \"updated_at\": \"2026-05-16T06:31:25.273Z\", \"hypothesis\": \"TACRED RE benchmark: replicate SciERC RE experiment flow on second RE dataset. Verify correlation-selection gap generalizes beyond SciERC. D104 highest priority — addresses R11 MF1 consensus weakness.\", \"conclusion\": \"killed\", \"spec\": {\"command\": \"N/A - cancelled before execution\", \"server\": \"N/A\", \"data_path\": \"N/A\", \"data_count\": 0, \"model_name\": \"N/A\", \"seed\": 0, \"checkpoint_path\": \"N/A\", \"log_path\": \"N/A\"}, \"completed_at\": \"2026-05-16T06:31:25.273Z\"}, \"exp_vc_quartile_analysis\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T04:48:35.263Z\", \"updated_at\": \"2026-05-16T05:00:36.736Z\", \"hypothesis\": \"VC quartile stratification: split instances by VC score into Q1-Q4, compute LP selection F1 per quartile. Test if LP selection ability recovers in high-VC instances. Addresses SF3.\", \"spec\": {\"command\": \"python vc_quartile_analysis.py\", \"server\": \"autodl-5090\", \"data_path\": \"output/exp_012_rerun_1024/samples.jsonl + output/exp_002_conll_n8_seed42/samples.jsonl\", \"data_count\": 3682, \"model_name\": \"analysis_only (Qwen3-8B data)\", \"seed\": 42}, \"conclusion\": \"success\", \"checkpoint_path\": \"artifacts/vc_quartile_analysis/results.json\", \"log_path\": \"artifacts/vc_quartile_analysis/report.md\", \"completed_at\": \"2026-05-16T05:00:30.439Z\", \"metrics\": {\"scierc_ner\": {\"Q1_lp_delta\": 0.016, \"Q2_lp_delta\": -0.006, \"Q3_lp_delta\": 0.02, \"Q4_lp_delta\": -0.004, \"Q4_mean_vc\": 0.921, \"Q1_headroom\": 0.169, \"Q4_headroom\": 0.048, \"overall_lp_delta\": 0.006, \"n\": 529}, \"scierc_re\": {\"Q1_lp_delta\": -0.036, \"Q2_lp_delta\": -0.021, \"Q3_lp_delta\": -0.022, \"Q4_lp_delta\": 0.04, \"Q4_mean_vc\": 0.894, \"Q1_headroom\": 0.211, \"Q4_headroom\": 0.145, \"overall_lp_delta\": -0.009, \"n\": 397}, \"conll_ner\": {\"Q1_lp_delta\": -0.037, \"Q2_lp_delta\": -0.005, \"Q3_lp_delta\": 0, \"Q4_lp_delta\": 0, \"overall_lp_delta\": -0.01, \"n\": 2756, \"note\": \"Q3/Q4 degenerate (VC=1.0, all samples identical)\"}, \"conclusion\": \"VC stratification does not solve LP compression for NER. RE Q4 is only exception (+0.040).\"}}, \"exp_llama3b_scierc_ablation\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T02:45:23.638Z\", \"updated_at\": \"2026-05-16T03:59:26.005Z\", \"hypothesis\": \"Cross-family scale ablation: LLaMA 3.2-3B on SciERC NER. Verify correlation-selection gap generalizes across model families AND scales. Compare with LLaMA 8B results.\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/llama3.2-3b-scierc-merged --data_dir data/scierc/processed_data --dataset scierc --subtask ner --n_samples 8 --temperature 1.0 --seed 42 --num_test 9999 --max_tokens 1024 --collect_logprobs --output_dir output/review_round9_experiments/llama3b_scierc/\", \"server\": \"autodl-5090\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"LLaMA-3.2-3B-Instruct (LoRA r=32 SciERC fine-tuned)\", \"seed\": 42, \"checkpoint_path\": \"checkpoints/llama3.2-3b-scierc-merged\", \"log_path\": \"output/review_round9_experiments/llama3b_scierc/inference.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T03:59:16.198Z\", \"metrics\": {\"ner_full\": {\"SJ_rho\": 0.3754, \"FK_rho\": 0.2676, \"LP_rho\": 0.2662, \"EM_rho\": 0.3341, \"VC_rho\": 0.4602, \"SJ_auroc\": 0.7383, \"FK_auroc\": 0.6714, \"LP_auroc\": 0.633, \"EM_auroc\": 0.7763, \"VC_auroc\": 0.7429, \"n\": 529}, \"ner_cond\": {\"SJ_rho\": 0.3445, \"FK_rho\": 0.2125, \"LP_rho\": 0.2099, \"EM_rho\": 0.3952, \"VC_rho\": 0.3815, \"SJ_auroc\": 0.7292, \"FK_auroc\": 0.66, \"LP_auroc\": 0.6156, \"EM_auroc\": 0.7822, \"VC_auroc\": 0.7222, \"n\": 476}, \"greedy_f1\": 0.6267, \"oracle_f1\": 0.763, \"oracle_headroom\": 0.1363, \"selection_f1_SJ\": 0.6328, \"selection_f1_VC\": 0.6113, \"selection_f1_FK\": 0.6295, \"selection_f1_EM\": 0.6174, \"selection_f1_LP\": 0.6279, \"n_gold_empty\": 22, \"structural_beats_surface\": true, \"rho_advantage_SJ_over_FK\": 0.1078}}, \"exp_freeform_conll_4seed\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-16T02:45:17.133Z\", \"updated_at\": \"2026-05-16T03:04:49.550Z\", \"hypothesis\": \"Free-form CoNLL NER 4-seed ablation: verify LP compression is cross-dataset intrinsic (not SciERC-specific). 4 seeds × N=8, T=1.0 on CoNLL, compare LP range distribution with constrained decoding.\", \"spec\": {\"command\": \"python run_freeform_conll.py --seed {42,123,456,789} --gpu {0,1,2,3} --n_samples 8 --temperature 1.0\", \"server\": \"autodl-4x5090\", \"data_path\": \"data/conll2003/test.jsonl\", \"data_count\": 3453, \"model_name\": \"checkpoints/qwen3-8b-conll2003-merged\", \"seed\": \"42,123,456,789\"}, \"checkpoint_path\": \"N/A (inference-only experiment)\", \"log_path\": \"output/review_round9_experiments/freeform_conll/\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-16T03:04:40.278Z\", \"metrics\": {\"greedy_f1\": \"0.9035±0.0004\", \"oracle_f1\": \"0.9460±0.0023\", \"lp_range_median\": \"0.0581±0.0072\", \"rho_sj\": \"0.4606±0.0188\", \"rho_fk\": \"0.4372±0.0209\", \"rho_em\": \"0.4714±0.0168\", \"rho_vc\": \"0.4606±0.0138\", \"rho_lp\": \"0.3262±0.0120\", \"sel_f1_sj\": \"0.8994±0.0014\", \"sel_f1_vc\": \"0.9006±0.0026\", \"sel_f1_lp\": \"0.8958±0.0009\", \"seeds\": [42, 123, 456, 789], \"n_samples\": 8, \"temperature\": 1, \"instances\": 2756, \"gold_empty_filtered\": 697}}, \"exp_qwen3_4b_conll_merge_inference_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:42:42.107Z\", \"updated_at\": \"2026-05-15T20:07:12.593Z\", \"hypothesis\": \"CoNLL 4B checkpoint-4200 (best from resume training) merge + SCS inference. Replaces v1 which used checkpoint-3800 merged model. Cross-scale evidence for correlation-selection gap.\", \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=1 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-4b-conll2003-merged-ckpt4200 --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 8 --temperature 1.0 --seed 42 --num_test 9999 --max_tokens 1024 --collect_logprobs --output_dir output/exp_qwen3_4b_conll_merge_inference_v2\", \"server\": \"autodl-5090\", \"data_path\": \"data/conll2003\", \"data_count\": 3453, \"model_name\": \"Qwen3-4B (LoRA merged, ckpt-4200)\", \"seed\": 42, \"checkpoint_source\": \"exp_qwen3_4b_conll_finetune_resume (checkpoint-4200)\"}, \"checkpoint_path\": \"N/A - duplicate\", \"log_path\": \"N/A - duplicate\", \"conclusion\": \"killed\", \"notes\": \"Superseded by exp_qwen3_4b_conll_scs_inference_v2. Output was empty (dead experiment), functionally duplicate.\", \"completed_at\": \"2026-05-15T20:03:47.431Z\"}, \"exp_qwen3_4b_scierc_merge_inference\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:42:43.332Z\", \"updated_at\": \"2026-05-15T20:04:15.433Z\", \"hypothesis\": \"SciERC 4B best checkpoint merge + SCS inference. Complete 2x2 scale matrix (4B SciERC cell). Cross-scale + cross-task evidence for correlation-selection gap.\", \"checkpoint_path\": \"N/A - superseded\", \"log_path\": \"N/A - superseded\", \"conclusion\": \"killed\", \"notes\": \"Superseded by exp_qwen3_4b_scierc_scs_inference. Never launched (stuck in PREPARING). Killed during registry cleanup.\", \"completed_at\": \"2026-05-15T20:04:15.433Z\"}, \"exp_qwen3_4b_scierc_finetune_v3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:24:45.518Z\", \"updated_at\": \"2026-05-15T19:39:04.438Z\", \"spec\": {\"command\": \"llamafactory-cli train train_config_scierc_4b.yaml\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"226610\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_qwen3_4b_scierc_finetune_v3.log\", \"submitted_at\": \"2026-05-15T19:24:55.461Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"wall_clock_seconds\": 849.0, \"gpu_hours\": 0.24}, \"conclusion\": \"failed\", \"notes\": \"OOM on cuda:2 — freeform inference (seed789, 8B) 占满 GPU 2。未实际训练。重启为 v4 on cuda:0。\", \"completed_at\": \"2026-05-15T19:39:04.438Z\"}, \"exp_qwen3_4b_conll_finetune_resume\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:38:19.388Z\", \"updated_at\": \"2026-05-15T19:38:43.468Z\", \"hypothesis\": \"CoNLL 4B NER LoRA fine-tune resume from checkpoint-3800. Cross-scale evidence for correlation-selection gap.\", \"spec\": {\"hypothesis\": \"CoNLL2003 NER LoRA fine-tune with Qwen3-4B, resume from checkpoint-3800 to complete 5 epochs\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && llamafactory-cli train train_config_conll2003_4b_resume.yaml\\\"\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:1\", \"data_path\": \"data/conll2003/llmfactory_train.json\", \"data_count\": 14042, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"resume_from\": \"checkpoint-3800\", \"lora_rank\": 32, \"lora_alpha\": 64, \"num_train_epochs\": 5, \"learning_rate\": 0.0002, \"batch_size\": \"2 x 8 grad_accum\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-4b-conll2003-lora\", \"best_checkpoint\": \"checkpoint-4200\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-4b-conll2003-lora/trainer_state.json\"}, \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 0.001136, \"eval_loss\": 0.0225, \"best_global_step\": 4200, \"best_metric_eval_loss\": 0.0225, \"total_steps\": 4390, \"epochs\": 5, \"train_runtime_sec\": 1185.8, \"train_samples_per_second\": 59.2, \"resumed_from_step\": 3800}, \"completed_at\": \"2026-05-15T19:38:43.468Z\"}, \"exp_qwen3_4b_scierc_finetune_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:03:49.204Z\", \"updated_at\": \"2026-05-15T19:24:32.466Z\", \"spec\": {\"command\": \"llamafactory-cli train train_config_scierc_4b.yaml\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:3\", \"pid\": \"219830\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_qwen3_4b_scierc_finetune_v2.log\", \"submitted_at\": \"2026-05-15T19:05:31.524Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 1861, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"plan_id\": \"D096\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-4b-scierc-lora/\", \"wall_clock_seconds\": 1122.6, \"gpu_hours\": 0.31}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T19:24:14.124Z\", \"notes\": \"PID 219830 已死，仅完成 step 10，无 checkpoint。需彻底重启。\"}, \"exp_qwen3_4b_conll_finetune\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-15T17:18:35.501Z\", \"updated_at\": \"2026-05-15T19:10:24.822Z\", \"hypothesis\": \"Scale ablation: Qwen3-4B CoNLL NER LoRA fine-tune to provide cross-scale evidence (vs 8B). Verify correlation-selection gap, SJ>FK ordering, and LP compression generalize across model scale.\", \"reproduce\": {\"finished_at\": \"2026-05-15T18:45:42.215Z\"}, \"failure_reason\": \"\", \"completed_at\": \"2026-05-15T18:45:43.672Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T18:45:49.686191+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=0 llamafactory-cli train train_config_conll2003_4b.yaml\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"data_path\": \"data/conll2003\", \"data_count\": 14041, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"plan_id\": \"D096\", \"log_path\": \"checkpoints/qwen3-4b-conll2003-lora/trainer_log.jsonl\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-4b-conll2003-lora\", \"lora_config\": {\"trainable_params\": \"66M / 4.09B (1.62%)\", \"target_modules\": \"q_proj, k_proj, v_proj, o_proj, gate_proj, up_proj, down_proj\", \"epochs\": 5, \"batch_size\": 16, \"total_steps\": 4390, \"enable_thinking\": false}}, \"conclusion\": \"success\", \"notes\": \"Training stopped at step 3920/4390 (89.3%, epoch 4.46/5). No error log or tmux session found. checkpoint-3800 is valid (adapter_model.safetensors 264MB, eval_loss=0.023). Proceeding with checkpoint-3800 for merge+inference.\", \"metrics\": {\"final_loss\": 0.0086, \"total_steps_completed\": 3920, \"total_steps_target\": 4390, \"epochs_completed\": 4.46, \"epochs_target\": 5, \"best_checkpoint\": \"checkpoint-3800\", \"note\": \"Training stopped at 89.3% completion (no error log found). Using checkpoint-3800 (loss ~0.01) for merge.\"}}, \"exp_freeform_seed789_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T19:02:03.813Z\", \"updated_at\": \"2026-05-15T19:06:44.537Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && python run_freeform_inference.py --seed 789 --num_samples 8 --temperature 1.0 --max_tokens 1024 --output_dir results/exp_freeform_ablation_seed789\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"218882\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_freeform_seed789_v2.log\", \"submitted_at\": \"2026-05-15T19:02:03.527Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"hypothesis\": \"Multi-seed free-form ablation (seed=789): third seed for 3-seed mean±σ statistical significance. Verify RE LP flip and NER gap stability.\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 789, \"wall_clock_seconds\": 274.9, \"gpu_hours\": 0.08}, \"reproduce\": {\"finished_at\": \"2026-05-15T19:06:37.887Z\"}, \"failure_reason\": \"EXIT_CODE=143 (SIGTERM — graceful kill)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-15T19:06:38.388Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-15T19:06:53.109123+00:00\"}]}}, \"exp_qwen3_4b_scierc_finetune\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T18:58:58.948Z\", \"updated_at\": \"2026-05-15T19:03:05.505Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=0 llamafactory-cli train train_config_scierc_4b.yaml\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:3\"], \"pid\": \"218258\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_qwen3_4b_scierc_finetune.log\", \"submitted_at\": \"2026-05-15T19:00:10.234Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 175.3, \"gpu_hours\": 0.05}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T19:03:05.505Z\"}, \"exp_lp_t07_scierc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T15:34:12.094Z\", \"updated_at\": \"2026-05-15T16:30:35.531Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask ner --n_samples 8 --temperature 0.7 --seed 42 --num_test 9999 --max_tokens 1024 --collect_logprobs --output_dir output/exp_lp_t07_scierc\\\"\", \"server\": \"autodl-5090\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"Qwen3-8B (LoRA fine-tuned on SciERC, ft_002_v2 merged)\", \"seed\": 42, \"gpu\": \"cuda:1\", \"hyperparams\": {\"n_samples\": 8, \"temperature\": 0.7, \"max_tokens\": 1024}}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T16:28:29.563Z\"}, \"exp_lp_scierc_t07\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T15:34:06.918Z\", \"updated_at\": \"2026-05-15T16:03:13.881Z\", \"hypothesis\": \"LP T=0.7 推理：验证低温下 LP score compression 是否依然存在，强化 \\\"LP compression is model/task intrinsic\\\" claim。对比 T=1.0 的 LP range 分布。\", \"spec\": {\"command\": \"python run_sc_ie.py --dataset scierc --subtask ner --model qwen --n_samples 8 --temperature 0.7 --use_logprob --output_dir /root/autodl-tmp/struct_self_consist_ie/output/exp_lp_scierc_t07\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:1\"], \"pid\": \"196993\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_lp_scierc_t07/\", \"submitted_at\": \"2026-05-15T15:35:31.692Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"SciERC\", \"data_count\": 500, \"model_name\": \"Qwen3-8B\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_lp_scierc_t07/report.json\", \"wall_clock_seconds\": 1206.2, \"gpu_hours\": 0.34}, \"conclusion\": \"success\", \"metrics\": {\"ner_greedy_f1\": 0.662, \"ner_oracle_f1\": 0.764, \"ner_headroom_pp\": 10.2, \"ner_rho_sj_full\": 0.365, \"ner_rho_sj_cond\": 0.363, \"ner_rho_fk_full\": 0.289, \"ner_rho_fk_cond\": 0.255, \"lp_rho_full\": 0.249, \"lp_rho_cond\": 0.185, \"ner_rho_advantage\": 0.076, \"zero_f1_pct\": 11, \"full_n\": 529, \"cond_n\": 477, \"verdict\": \"success_supports_LP_compression_claim\"}, \"completed_at\": \"2026-05-15T15:55:37.889Z\"}, \"exp_re_scierc_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T15:40:40.607Z\", \"updated_at\": \"2026-05-15T15:55:41.890Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=3 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 1.0 --max_tokens 1024 --seed 456 --num_test 9999 --collect_logprobs --output_dir output/exp_re_scierc_seed456\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:3\"], \"pid\": \"199161\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_re_scierc_seed456/\", \"submitted_at\": \"2026-05-15T15:40:59.585Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"SciERC\", \"data_count\": 500, \"model_name\": \"Qwen3-8B (SciERC merged)\", \"seed\": 456, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_re_scierc_seed456/report.json\", \"wall_clock_seconds\": 882.3, \"gpu_hours\": 0.25}, \"hypothesis\": \"SciERC RE 多种子验证 (seed456): 解决 R4-W1/R7-C1 single-seed RE 弱点。与 seed42 (exp_012_rerun_1024) 对齐，joint subtask N=8 T=1.0。目标: 3-seed RE selection F1 mean±σ。\", \"conclusion\": \"negative\", \"metrics\": {\"ner_greedy_f1\": 0.664, \"ner_oracle_f1\": 0.775, \"ner_headroom_pp\": 11.1, \"ner_rho_sj_cond\": 0.283, \"ner_rho_fk_cond\": 0.145, \"re_greedy_f1\": 0.417, \"re_oracle_f1\": 0.581, \"re_headroom_pp\": 16.3, \"re_rho_sj_cond\": 0.315, \"re_rho_fk_cond\": 0.123, \"re_zero_f1_pct\": 45.3, \"verdict\": \"FAIL_re_rho_sj_below_040\"}, \"completed_at\": \"2026-05-15T15:55:41.890Z\"}, \"exp_re_scierc_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T15:40:38.271Z\", \"updated_at\": \"2026-05-15T15:55:40.000Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=2 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 1.0 --max_tokens 1024 --seed 123 --num_test 9999 --collect_logprobs --output_dir output/exp_re_scierc_seed123\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:2\"], \"pid\": \"199021\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_re_scierc_seed123/\", \"submitted_at\": \"2026-05-15T15:40:58.073Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"SciERC\", \"data_count\": 500, \"model_name\": \"Qwen3-8B (SciERC merged)\", \"seed\": 123, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp_re_scierc_seed123/report.json\", \"wall_clock_seconds\": 881.9, \"gpu_hours\": 0.24}, \"hypothesis\": \"SciERC RE 多种子验证 (seed123): 解决 R4-W1/R7-C1 single-seed RE 弱点。与 seed42 (exp_012_rerun_1024) 对齐，joint subtask N=8 T=1.0。目标: 3-seed RE selection F1 mean±σ。\", \"conclusion\": \"negative\", \"metrics\": {\"ner_greedy_f1\": 0.663, \"ner_oracle_f1\": 0.786, \"ner_headroom_pp\": 12.3, \"ner_rho_sj_cond\": 0.404, \"ner_rho_fk_cond\": 0.182, \"re_greedy_f1\": 0.42, \"re_oracle_f1\": 0.593, \"re_headroom_pp\": 17.3, \"re_rho_sj_cond\": 0.277, \"re_rho_fk_cond\": 0.063, \"re_zero_f1_pct\": 43.6, \"verdict\": \"FAIL_re_rho_sj_below_040\"}, \"completed_at\": \"2026-05-15T15:55:40.000Z\"}, \"exp_017_llama_conll_n8_t07\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T15:29:34.595Z\", \"updated_at\": \"2026-05-15T15:46:22.722Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=0 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 8 --temperature 0.7 --seed 42 --num_test 9999 --max_tokens 1024 --collect_logprobs --output_dir output/exp_017_llama_conll_n8_t07\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"195927\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_017_llama_conll_n8_t07.log\", \"submitted_at\": \"2026-05-15T15:31:17.989Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 881.3, \"gpu_hours\": 0.24}, \"hypothesis\": \"LLaMA CoNLL N=8 T=0.7 防御性实验：填补\\\"LLaMA 仅在 SciERC 上测过\\\"的弱点，验证 cross-model consistency（vs Qwen CoNLL）。T=0.7 低温下 confidence signals 的 correlation-selection gap 是否依然存在。\", \"parent\": \"exp_017_llama_conll\", \"server\": \"autodl-5090\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"autodl-5090\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-15T15:31:15.772Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=0 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 8 --temperature 0.7 --seed 42 --num_test 9999 --max_tokens 1024 --collect_logprobs --output_dir output/exp_017_llama_conll_n8_t07\\\"\", \"finished_at\": \"2026-05-15T15:40:02.605Z\", \"training_hours\": 0.15}, \"pid\": \"195927\", \"log_path\": \"/root/runs/struct_self_consist_ie/exp_017_llama_conll_n8_t07.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-15T15:40:08.277684+00:00\"}]}, \"metrics\": {\"n_valid\": 2756, \"greedy_f1\": 0.9242, \"oracle_f1\": 0.9391, \"lp_range_median\": 1.1e-05, \"lp_tied_fraction_005\": 0.9579, \"signals\": {\"SJ\": {\"rho\": 0.3934, \"auroc\": 0.6506}, \"FK\": {\"rho\": 0.3879, \"auroc\": 0.6488}, \"VC\": {\"rho\": 0.375, \"auroc\": 0.6551}, \"EM\": {\"rho\": 0.3888, \"auroc\": 0.6494}, \"LP\": {\"rho\": 0.2951, \"auroc\": 0.7509}}, \"selection_f1\": {\"SJ\": 0.9247, \"FK\": 0.9254, \"VC\": 0.9264, \"EM\": 0.9255, \"LP\": 0.9248}}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (inference-only)\", \"completed_at\": \"2026-05-15T15:45:59.311Z\"}, \"exp008_re_n16\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:09:50.987Z\", \"updated_at\": \"2026-05-15T12:41:39.774Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && mkdir -p output/exp008_re_n16 && CUDA_VISIBLE_DEVICES=2 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 16 --temperature 1.0 --seed 42 --output_dir output/exp008_re_n16 --collect_logprobs 2>&1 | tee output/exp008_re_n16/run.log\\\"\", \"server\": \"gpu-5090-4x-2\", \"gpu\": [\"cuda:2\"], \"pid\": \"53600\", \"log_path\": \"~/runs/struct_self_consist_ie/exp008_re_n16.log\", \"submitted_at\": \"2026-05-14T12:15:14.917Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"failure_reason\": \"Superseded by exp_008_re_n16_v2 (full 551-instance run on autodl-5090)\", \"wall_clock_seconds\": 87984.9, \"gpu_hours\": 24.44}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T12:41:39.774Z\"}, \"exp001_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:09:48.078Z\", \"updated_at\": \"2026-05-15T12:41:32.192Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && mkdir -p output/exp001_n16_seed456 && CUDA_VISIBLE_DEVICES=1 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 16 --temperature 1.0 --seed 456 --output_dir output/exp001_n16_seed456 --collect_logprobs 2>&1 | tee output/exp001_n16_seed456/run.log\\\"\", \"server\": \"gpu-5090-4x-2\", \"gpu\": [\"cuda:1\"], \"pid\": \"50302\", \"log_path\": \"~/runs/struct_self_consist_ie/exp001_seed456.log\", \"submitted_at\": \"2026-05-14T12:12:41.206Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"failure_reason\": \"Superseded by exp_001_seed456_v2_ner (NER-only on autodl-5090)\", \"wall_clock_seconds\": 88131.0, \"gpu_hours\": 24.48}, \"conclusion\": \"killed\", \"failure_reason\": \"superseded by v2\", \"completed_at\": \"2026-05-15T12:41:32.192Z\"}, \"exp001_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:09:45.739Z\", \"updated_at\": \"2026-05-15T12:41:31.168Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && mkdir -p output/exp001_n16_seed123 && CUDA_VISIBLE_DEVICES=0 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 16 --temperature 1.0 --seed 123 --output_dir output/exp001_n16_seed123 --collect_logprobs 2>&1 | tee output/exp001_n16_seed123/run.log\\\"\", \"server\": \"gpu-5090-4x-2\", \"gpu\": [\"cuda:0\"], \"pid\": \"48530\", \"log_path\": \"~/runs/struct_self_consist_ie/exp001_seed123.log\", \"submitted_at\": \"2026-05-14T12:09:45.674Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"failure_reason\": \"Superseded by exp_001_seed123_v2 (NER-only, 551 instances on autodl-5090)\", \"wall_clock_seconds\": 88305.5, \"gpu_hours\": 24.53}, \"conclusion\": \"killed\", \"failure_reason\": \"superseded by v2\", \"completed_at\": \"2026-05-15T12:41:31.168Z\"}, \"exp_001_n16_seed456_full\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:44:31.348Z\", \"updated_at\": \"2026-05-15T12:41:30.065Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=1 python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 16 --temperature 1.0 --seed 456 --collect_logprobs --num_test 9999 --output_dir output/exp001_n16_seed456/\\\"\", \"server\": \"gpu-5090-4x-2\", \"gpu\": [\"cuda:1\"], \"pid\": \"62170\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_001_n16_seed456_full.log\", \"submitted_at\": \"2026-05-14T12:44:31.087Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"failure_reason\": \"Superseded by exp_001_seed456_v2_ner (NER-only on autodl-5090)\", \"wall_clock_seconds\": 86219.0, \"gpu_hours\": 23.95}, \"conclusion\": \"killed\", \"failure_reason\": \"superseded by v2\", \"completed_at\": \"2026-05-15T12:41:30.065Z\"}, \"exp_001_n16_seed123_full\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:43:47.915Z\", \"updated_at\": \"2026-05-15T12:41:29.068Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=0 python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 16 --temperature 1.0 --seed 123 --collect_logprobs --num_test 9999 --output_dir output/exp001_n16_seed123_full/\\\"\", \"server\": \"gpu-5090-4x-2\", \"gpu\": [\"cuda:0\"], \"pid\": \"61812\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_001_n16_seed123_full.log\", \"submitted_at\": \"2026-05-14T12:44:06.059Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"failure_reason\": \"Superseded by exp_001_seed123_v2 (NER-only on autodl-5090)\", \"wall_clock_seconds\": 86243.0, \"gpu_hours\": 23.96}, \"conclusion\": \"killed\", \"failure_reason\": \"superseded by v2\", \"completed_at\": \"2026-05-15T12:41:29.068Z\"}, \"exp_007_ner_llama\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T11:42:21.510Z\", \"updated_at\": \"2026-05-15T12:41:27.410Z\", \"spec\": {\"description\": \"Fine-tune LLaMA-3.1-8B on SciERC + NER pilot (N=8, T=0.7). Model-agnostic validation.\", \"hypothesis\": \"SJ advantage is model-agnostic, not Qwen3-specific\", \"plan_id\": \"exp-007\", \"claim\": 1, \"model_name\": \"llama-3.1-8b-instruct (new fine-tune)\", \"dataset\": \"SciERC\", \"priority\": \"P0\", \"failure_reason\": \"Superseded by exp_007_ner_multi_model + exp_007_llama_inference (completed on autodl-5090)\"}, \"conclusion\": \"killed\", \"failure_reason\": \"superseded by exp_007_llama_inference (DONE)\", \"notes\": \"Completed as exp_007_llama_n16 on autodl-5090. Registry status corrected.\", \"completed_at\": \"2026-05-15T12:41:27.410Z\"}, \"exp_002_merge_conll2003\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:25:56.211Z\", \"updated_at\": \"2026-05-15T12:41:26.419Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=0 llamafactory-cli export export_config_conll2003.yaml > /tmp/merge_conll2003.log 2>&1 && echo 'MERGE_DONE' >> /tmp/merge_conll2003.log\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"57524\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_002_merge_conll2003.log\", \"submitted_at\": \"2026-05-14T12:25:56.139Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"failure_reason\": \"Superseded by exp_002_ner_conll2003 (completed on autodl-5090)\", \"wall_clock_seconds\": 87330.3, \"gpu_hours\": 24.26}, \"conclusion\": \"killed\", \"failure_reason\": \"superseded by exp_002_ner_conll2003 (DONE)\", \"notes\": \"Completed as exp_002_conll_n16 on autodl-5090. Registry status corrected.\", \"completed_at\": \"2026-05-15T12:41:26.419Z\"}, \"exp_019_supervised_verifier\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T10:08:54.395Z\", \"updated_at\": \"2026-05-15T12:40:53.995Z\", \"spec\": {\"hypothesis\": \"Supervised verifier (DeBERTa-v3-large) can close the correlation-selection gap, proving the gap is closable with supervision\", \"plan_id\": \"exp-019\", \"model_name\": \"microsoft/deberta-v3-large\", \"data_path\": \"output/exp_012_rerun_1024/samples.jsonl\", \"data_count\": 551, \"seed\": 42}, \"conclusion\": \"killed\", \"notes\": \"Cancelled by Director: DDL risk too high (3-4 days for implementation+training+eval+paper), scope creep for analytical paper, free-form ablation already provides sufficient mechanistic evidence\", \"completed_at\": \"2026-05-15T12:40:53.995Z\"}, \"exp_018_llama_scierc_seed456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-15T06:07:15.150Z\", \"updated_at\": \"2026-05-15T06:22:40.868Z\", \"spec\": {\"hypothesis\": \"Multi-seed robustness: LLaMA SciERC N=8 seed=456, max_tokens=1024. Fresh inference (D066 decision: replace exp_007 re-analysis with independent replication).\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-scierc-merged --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 1.0 --seed 456 --max_tokens 1024 --num_test 9999 --collect_logprobs --output_dir output/exp_018_llama_scierc_seed456_r1024\\\"\", \"server\": \"autodl-5090\", \"seed\": 456, \"model_name\": \"LLaMA-3.1-8B-SciERC-merged\", \"model_path\": \"checkpoints/llama3.1-8b-scierc-merged\", \"dataset\": \"SciERC\", \"subtask\": \"joint\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"N\": 8, \"T\": 1, \"max_tokens\": 1024, \"is_new_inference\": true, \"checkpoint_path\": \"output/exp_018_llama_scierc_seed456_r1024/\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_018_llama_scierc_seed456_r1024.log\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T06:08:05.756Z\", \"notes\": \"SUPERSEDED by exp_018_llama_scierc_seed456_r1024 (D066). Original data was re-analysis of exp_007_llama_seed456, not independent inference. Fresh rerun with explicit max_tokens=1024 now canonical.\"}, \"exp_002_conll_n16_r1024\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:16:57.682Z\", \"updated_at\": \"2026-05-15T01:20:53.108Z\", \"spec\": {\"hypothesis\": \"D054 rerun: max_tokens=1024. Verify truncation impact on Qwen CoNLL N=16.\", \"parent\": \"exp_002_conll_n16\", \"model_name\": \"qwen3-8b-conll2003-merged\", \"dataset\": \"CoNLL-2003\", \"seed\": 42, \"server\": \"autodl-5090\", \"command\": \"CUDA_VISIBLE_DEVICES=2 python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 16 --temperature 1.0 --seed 42 --num_test 9999 --max_tokens 1024 --collect_logprobs --output_dir output/exp_002_conll_n16_r1024\", \"data_path\": \"data/conll2003\", \"data_count\": 3453}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T01:20:53.108Z\"}, \"exp_007_llama_n16_r1024\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:16:59.685Z\", \"updated_at\": \"2026-05-15T01:20:52.194Z\", \"spec\": {\"hypothesis\": \"D054 rerun: max_tokens=1024. Verify truncation impact on LLaMA SciERC N=16.\", \"parent\": \"exp_007_llama_n16\", \"model_name\": \"llama3.1-8b-scierc-merged\", \"dataset\": \"SciERC\", \"seed\": 42, \"server\": \"autodl-5090\", \"command\": \"CUDA_VISIBLE_DEVICES=3 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-scierc-merged --data_dir data/scierc/processed_data --dataset scierc --subtask ner --n_samples 16 --temperature 1.0 --seed 42 --num_test 9999 --max_tokens 1024 --collect_logprobs --output_dir output/exp_007_llama_n16_r1024\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 9999}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T01:20:52.194Z\"}, \"exp_001_seed123_v2_r1024\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:16:54.442Z\", \"updated_at\": \"2026-05-15T01:20:49.812Z\", \"spec\": {\"hypothesis\": \"D054 rerun: max_tokens=1024. Verify truncation impact on Qwen SciERC N=16 seed123.\", \"parent\": \"exp_001_seed123_v2\", \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"dataset\": \"SciERC\", \"seed\": 123, \"server\": \"autodl-5090\", \"command\": \"CUDA_VISIBLE_DEVICES=1 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask ner --n_samples 16 --temperature 1.0 --seed 123 --num_test 9999 --max_tokens 1024 --collect_logprobs --output_dir output/exp_001_seed123_v2_r1024\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 529}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T01:20:49.812Z\"}, \"exp_001_seed456_v2_ner_r1024\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:16:55.975Z\", \"updated_at\": \"2026-05-15T01:20:48.914Z\", \"spec\": {\"hypothesis\": \"D054 rerun: max_tokens=1024. Verify truncation impact on Qwen SciERC N=16 seed456.\", \"parent\": \"exp_001_seed456_v2_ner\", \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"dataset\": \"SciERC\", \"seed\": 456, \"server\": \"autodl-5090\", \"command\": \"CUDA_VISIBLE_DEVICES=1 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask ner --n_samples 16 --temperature 1.0 --seed 456 --num_test 9999 --max_tokens 1024 --collect_logprobs --output_dir output/exp_001_seed456_v2_ner_r1024\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 9999}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-15T01:20:48.914Z\"}, \"exp_001_seed42_v2_r1024\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T22:16:52.571Z\", \"updated_at\": \"2026-05-14T22:28:53.686Z\", \"spec\": {\"hypothesis\": \"D054 rerun: max_tokens=1024. Verify truncation impact on Qwen SciERC N=16 seed42.\", \"parent\": \"exp_001_seed42_v2\", \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"dataset\": \"SciERC\", \"seed\": 42, \"server\": \"autodl-5090\", \"command\": \"CUDA_VISIBLE_DEVICES=0 PYTHONPATH=code python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask ner --n_samples 16 --temperature 1.0 --seed 42 --num_test 9999 --max_tokens 1024 --collect_logprobs --output_dir output/exp_001_seed42_v2_r1024\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 9999}, \"conclusion\": \"killed\", \"metrics\": {\"greedy_f1\": 0.6647, \"oracle_f1\": 0.8106, \"softjaccard_rho_full\": 0.3928, \"fleiss_rho_full\": 0.2489, \"logprob_rho_full\": 0.2136, \"softjaccard_rho_cond\": 0.3455, \"fleiss_rho_cond\": 0.163, \"logprob_rho_cond\": 0.1624, \"verdict\": \"MARGINAL\"}, \"checkpoint_path\": \"output/exp_001_seed42_v2_r1024\", \"log_path\": \"output/exp_001_seed42_v2_r1024/run.log\", \"completed_at\": \"2026-05-14T22:27:43.836Z\"}, \"exp_017_llama_conll_n16_s456\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T19:23:21.987Z\", \"updated_at\": \"2026-05-14T20:24:45.875Z\", \"hypothesis\": \"LLaMA CoNLL N=16 seed=456: structural>surface ranking preserved across seeds, complementing Qwen SciERC 3-seed protocol\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 16 --temperature 1.0 --seed 456 --collect_logprobs --num_test 9999 --output_dir output/exp_017_llama_conll_n16_s456\", \"server\": \"autodl-5090\", \"data_path\": \"data/conll2003\", \"data_count\": 3453, \"model_name\": \"llama3.1-8b-conll2003-merged\", \"seed\": 456}, \"metrics\": {\"greedy_f1\": 0.9243, \"oracle_f1\": 0.9488, \"oracle_headroom\": 0.0245, \"n_instances\": 3453, \"n_valid\": 2756, \"n_conditional\": 2642, \"structural_beats_surface\": true, \"full\": {\"SJ_rho\": 0.4552, \"SJ_AUROC\": 0.7288, \"SJ_ECE\": 0.1134, \"FK_rho\": 0.4478, \"FK_AUROC\": 0.7248, \"FK_ECE\": 0.109, \"logprob_rho\": 0.3078, \"logprob_AUROC\": 0.7612, \"logprob_ECE\": 0.1289, \"EM_rho\": 0.452, \"EM_AUROC\": 0.7275, \"EM_ECE\": 0.1082, \"voting_conf_rho\": 0.4571, \"voting_conf_AUROC\": 0.7348, \"voting_conf_ECE\": 0.0863}, \"conditional\": {\"SJ_rho\": 0.4505, \"SJ_AUROC\": 0.7449, \"SJ_ECE\": 0.0826, \"FK_rho\": 0.4422, \"FK_AUROC\": 0.7401, \"FK_ECE\": 0.0835, \"logprob_rho\": 0.3242, \"logprob_AUROC\": 0.8067, \"logprob_ECE\": 0.0921, \"EM_rho\": 0.451, \"EM_AUROC\": 0.745, \"EM_ECE\": 0.0756, \"voting_conf_rho\": 0.3962, \"voting_conf_AUROC\": 0.7202, \"voting_conf_ECE\": 0.0746}, \"best_of_n\": {\"greedy\": 0.9243, \"random_avg\": 0.9215, \"sj_best\": 0.9243, \"logprob_best\": 0.9243, \"voting_conf_best\": 0.9243, \"oracle\": 0.9488}, \"n8_vs_n16_delta\": {\"full_SJ_rho_delta\": 0.0238, \"full_FK_rho_delta\": 0.0201, \"full_logprob_rho_delta\": 0.0006, \"full_EM_rho_delta\": 0.0214, \"full_voting_conf_rho_delta\": 0.0315, \"cond_SJ_rho_delta\": 0.0149, \"cond_FK_rho_delta\": 0.0112, \"cond_logprob_rho_delta\": -0.004, \"cond_EM_rho_delta\": 0.0107, \"cond_voting_conf_rho_delta\": 0.0219}}, \"checkpoint_path\": \"output/exp_017_llama_conll_n16_s456/samples.jsonl\", \"log_path\": \"output/exp_017_llama_conll_n16_s456/all_signals_report.json\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T20:24:45.875Z\"}, \"exp_017_llama_conll_n16_s123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T19:23:21.084Z\", \"updated_at\": \"2026-05-14T19:43:06.607Z\", \"hypothesis\": \"LLaMA CoNLL N=16 seed=123: structural>surface ranking preserved across seeds, complementing Qwen SciERC 3-seed protocol\", \"spec\": {\"hypothesis\": \"LLaMA CoNLL-2003 NER N=16 seed=123: cross-seed robustness check against N=8 seed=42 baseline (exp_017_llama_conll_infer)\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python code/run_mvp_pilot.py --model_path checkpoints/llama3.1-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 16 --temperature 1.0 --seed 123 --collect_logprobs --num_test 9999 --output_dir output/exp_017_llama_conll_n16_s123\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/conll2003\", \"data_count\": 3453, \"model_name\": \"llama3.1-8b-conll2003-merged\", \"seed\": 123, \"checkpoint_source\": \"checkpoints/llama3.1-8b-conll2003-merged\", \"eval_data\": \"data/conll2003\", \"checkpoint_path\": \"output/exp_017_llama_conll_n16_s123/samples.jsonl\", \"log_path\": \"output/exp_017_llama_conll_n16_s123.log\"}, \"metrics\": {\"greedy_f1\": 0.9266, \"oracle_f1\": 0.9497, \"oracle_headroom\": 0.0231, \"n_instances\": 3453, \"n_valid\": 2756, \"n_conditional\": 2642, \"structural_beats_surface\": true, \"full\": {\"SJ_rho\": 0.4698, \"SJ_AUROC\": 0.7402, \"SJ_ECE\": 0.1135, \"FK_rho\": 0.4594, \"FK_AUROC\": 0.7351, \"FK_ECE\": 0.1114, \"logprob_rho\": 0.3161, \"logprob_AUROC\": 0.768, \"logprob_ECE\": 0.129, \"EM_rho\": 0.4676, \"EM_AUROC\": 0.7399, \"EM_ECE\": 0.1082, \"voting_conf_rho\": 0.4612, \"voting_conf_AUROC\": 0.7429, \"voting_conf_ECE\": 0.0832}, \"conditional\": {\"SJ_rho\": 0.4712, \"SJ_AUROC\": 0.7609, \"SJ_ECE\": 0.0828, \"FK_rho\": 0.4595, \"FK_AUROC\": 0.7547, \"FK_ECE\": 0.0858, \"logprob_rho\": 0.3314, \"logprob_AUROC\": 0.8134, \"logprob_ECE\": 0.0922, \"EM_rho\": 0.4732, \"EM_AUROC\": 0.7626, \"EM_ECE\": 0.075, \"voting_conf_rho\": 0.4086, \"voting_conf_AUROC\": 0.7338, \"voting_conf_ECE\": 0.0706}, \"best_of_n\": {\"greedy\": 0.9242, \"random_avg\": 0.9216, \"sj_best\": 0.9247, \"logprob_best\": 0.9253, \"voting_conf_best\": 0.9255, \"oracle\": 0.9486}, \"n8_vs_n16_delta\": {\"full_SJ_rho_delta\": 0.0384, \"full_FK_rho_delta\": 0.0317, \"full_logprob_rho_delta\": 0.0089, \"full_SJ_AUROC_delta\": 0.0363, \"full_FK_AUROC_delta\": 0.0325, \"full_logprob_AUROC_delta\": 0.007, \"cond_SJ_rho_delta\": 0.0356, \"cond_FK_rho_delta\": 0.0285, \"cond_logprob_rho_delta\": 0.0032}}, \"log_path\": \"output/exp_017_llama_conll_n16_s123.log\", \"checkpoint_path\": \"output/exp_017_llama_conll_n16_s123/samples.jsonl\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T19:43:06.607Z\"}, \"exp_008_re_n16_full\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:45:10.852Z\", \"updated_at\": \"2026-05-14T17:51:43.957Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=2 python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask re --n_samples 16 --temperature 1.0 --seed 42 --collect_logprobs --num_test 9999 --output_dir output/exp008_re_n16/\\\"\", \"server\": \"gpu-5090-4x-2\", \"gpu\": [\"cuda:2\"], \"pid\": \"62585\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_008_re_n16_full.log\", \"submitted_at\": \"2026-05-14T12:45:10.764Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 18393.2, \"gpu_hours\": 5.11}, \"conclusion\": \"killed\", \"failure_reason\": \"superseded by exp_008_re_n16_t10_full (full 551-instance RE-only run on autodl-5090)\", \"completed_at\": \"2026-05-14T17:51:43.957Z\"}, \"exp_001_n16_seed123\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:10:29.393Z\", \"updated_at\": \"2026-05-14T12:42:58.393Z\", \"spec\": {\"command\": \"python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 16 --temperature 1.0 --seed 123 --collect_logprobs\", \"server\": \"gpu-5090-4x-2\", \"data_path\": \"data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"qwen3-8b-scierc-merged-v2\", \"seed\": 123, \"num_instances\": 200, \"partial\": true, \"note\": \"Only 200/551 instances due to --num_test default bug. Needs full rerun.\"}, \"metrics\": {\"ner\": {\"greedy_f1\": 0.655, \"oracle_f1\": 0.8028, \"headroom\": 0.1478, \"rho_sj_full\": 0.4076, \"rho_fk_full\": 0.2799, \"rho_logprob_full\": 0.3189, \"rho_sj_cond\": 0.4271, \"rho_fk_cond\": 0.2743, \"rho_logprob_cond\": 0.2835, \"sj_beats_fk\": true, \"rho_advantage\": 0.1277}, \"re\": {\"greedy_f1\": 0.4243, \"oracle_f1\": 0.6771, \"headroom\": 0.2528, \"rho_sj_full\": 0.2943, \"rho_fk_full\": 0.2657, \"rho_logprob_full\": 0.3005, \"rho_sj_cond\": 0.4003, \"rho_fk_cond\": 0.313, \"rho_logprob_cond\": 0.2317, \"sj_beats_fk\": true, \"rho_advantage\": 0.0286}, \"verdict\": \"FAIL\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A\", \"log_path\": \"output/exp001_n16_seed123/\", \"completed_at\": \"2026-05-14T12:28:38.104Z\"}, \"exp_016_signal_ensemble\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:15:23.771Z\", \"updated_at\": \"2026-05-14T12:42:55.931Z\", \"spec\": {\"command\": \"python code/analyze_exp016_ensemble.py\", \"server\": \"autodl-5090\", \"data_path\": \"output/exp_012_logprob/samples_with_logprobs.jsonl\", \"data_count\": 551, \"model_name\": \"N/A (CPU-only analysis)\", \"seed\": 42, \"checkpoint_source\": \"N/A\", \"eval_data\": \"pilot_004\", \"checkpoint_path\": \"N/A\", \"log_path\": \"output/exp016_signal_ensemble/\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T12:15:53.341Z\", \"metrics\": {\"sj_logprob_pearson_ner\": 0.57, \"sj_logprob_pearson_re\": 0.42, \"best_linear_ner\": {\"combo\": \"SJ+voting_conf\", \"alpha\": 0.3, \"rho\": 0.489}, \"best_linear_re\": {\"combo\": \"voting_conf+logprob\", \"alpha\": 0.6, \"rho\": 0.429}, \"ensemble_ner_auroc\": 0.735, \"ensemble_re_auroc\": 0.719, \"best_single_ner_auroc\": 0.7, \"best_single_re_auroc\": 0.721, \"ensemble_ner_delta\": 0.035, \"selection_f1_ner\": {\"greedy\": 0.609, \"logprob\": 0.609, \"sj\": 0.604, \"ensemble\": 0.604, \"voting\": 0.596, \"random\": 0.58, \"oracle\": 0.769}, \"selection_f1_re\": {\"logprob\": 0.397, \"greedy\": 0.374, \"sj\": 0.368, \"ensemble\": 0.367, \"voting\": 0.338, \"random\": 0.338, \"oracle\": 0.561}, \"diagnosis\": \"SJ+voting_conf linear combo boosts NER ρ to 0.489 (+23%). RE: logprob-best is ONLY method beating greedy (0.397 vs 0.374). Ensemble AUROC +0.035 on NER. Oracle gap still huge.\"}}, \"exp_001_ner_n16_scierc\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T11:42:10.898Z\", \"updated_at\": \"2026-05-14T12:42:49.592Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=0 python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 16 --temperature 1.0 --seed 42 --output_dir output/exp001_n16_seed42 --num_test 9999 --collect_logprobs 2>&1 | tee output/exp001_n16_seed42_run.log\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"54357\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_001_ner_n16_scierc.log\", \"submitted_at\": \"2026-05-14T12:15:46.646Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"server\": \"autodl-5090\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"autodl-5090\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-14T11:43:48.643Z\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T11:55:45.664Z\", \"metrics\": {\"n_instances\": 551, \"ner_n\": 529, \"re_n\": 397, \"N\": 16, \"T\": 1, \"seed\": 42, \"full_test_set\": true, \"ner_voting_conf_rho\": 0.399, \"ner_sj_rho\": 0.398, \"ner_em_rho\": 0.339, \"ner_fk_rho\": 0.288, \"ner_logprob_rho\": 0.237, \"ner_voting_conf_auroc\": 0.704, \"ner_sj_auroc\": 0.697, \"ner_cond_em_rho\": 0.414, \"ner_cond_sj_rho\": 0.349, \"ner_cond_vc_rho\": 0.34, \"re_voting_conf_rho\": 0.38, \"re_logprob_rho\": 0.293, \"re_fk_rho\": 0.281, \"re_sj_rho\": 0.277, \"re_em_rho\": 0.148, \"re_voting_conf_auroc\": 0.699, \"re_cond_em_rho\": 0.475, \"re_cond_sj_rho\": 0.318, \"re_cond_vc_rho\": 0.35, \"re_cond_em_auroc\": 0.742, \"diagnosis\": \"551 instances T=1.0: voting_conf best on full set (NER 0.399, RE 0.380). EM SURPRISE best on conditional set (NER cond 0.414, RE cond 0.475). RE full FAIL (SJ 0.277 < 0.40). Previous N-scaling 'breakthrough' was artifact of 200 instances + T=0.7.\"}}, \"exp_002\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:39:53.226Z\", \"updated_at\": \"2026-05-14T12:40:17.202Z\", \"spec\": {\"command\": \"python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-conll2003-merged --dataset conll2003 --subtask ner --n_samples 8 --temperature 1.0 --collect_logprobs --num_test 99999\", \"server\": \"autodl-5090\", \"data_path\": \"data/conll2003\", \"data_count\": 3453, \"model_name\": \"qwen3-8b-conll2003-lora-merged\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-conll2003-merged\", \"log_path\": \"/tmp/pilot_conll2003.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T12:40:08.402Z\", \"metrics\": {\"sj_rho_full\": 0.4357, \"sj_tau_full\": 0.3851, \"sj_auroc_full\": 0.8008, \"sj_rho_cond\": 0.4511, \"fk_rho_full\": 0.3998, \"fk_tau_full\": 0.3568, \"fk_auroc_full\": 0.7741, \"fk_rho_cond\": 0.4064, \"logprob_rho_full\": 0.3157, \"logprob_tau_full\": 0.2469, \"logprob_auroc_full\": 0.7532, \"logprob_rho_cond\": 0.3562, \"em_rho_full\": 0.4507, \"em_tau_full\": 0.4002, \"em_auroc_full\": 0.8156, \"em_rho_cond\": 0.4799, \"ev_rho_full\": 0.4237, \"ev_tau_full\": 0.3777, \"ev_auroc_full\": 0.7889, \"ev_rho_cond\": 0.4127, \"greedy_f1\": 0.9123, \"oracle_f1\": 0.9543, \"voting_f1\": 0.9141, \"oracle_headroom\": 0.042, \"sj_vs_logprob_delta_rho\": 0.12, \"sj_vs_logprob_ci_low\": 0.0881, \"sj_vs_logprob_ci_high\": 0.154, \"sj_vs_logprob_significant\": true, \"n_instances\": 3453, \"n_valid\": 2756, \"n_samples\": 8, \"temperature\": 1}}, \"exp_002_ner_conll2003\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T11:42:15.223Z\", \"updated_at\": \"2026-05-14T12:27:35.413Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/struct_self_consist_ie && CUDA_VISIBLE_DEVICES=0 python code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-conll2003-merged --data_dir data/conll2003 --dataset conll2003 --subtask ner --n_samples 8 --temperature 1.0 --max_tokens 1024 --output_dir output/exp002_conll2003 --num_test 99999 --seed 42 --collect_logprobs 2>&1 | tee /tmp/pilot_conll2003.log\\\"\", \"server\": \"autodl-5090\", \"gpu\": [\"cuda:0\"], \"pid\": \"58208\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_002_ner_conll2003.log\", \"submitted_at\": \"2026-05-14T12:27:35.337Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"server\": \"autodl-5090\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"autodl-5090\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-14T11:43:49.959Z\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-conll2003-lora\", \"log_path\": \"~/runs/struct_self_consist_ie/exp_002_ner_conll2003.log\", \"completed_at\": \"2026-05-14T12:18:04.097Z\"}, \"exp_004_re_diagnostic\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T11:49:44.497Z\", \"updated_at\": \"2026-05-14T11:50:24.620Z\", \"spec\": {\"hypothesis\": \"RE diagnostic: per-relation-type breakdown reveals which types drive low RE rho; error propagation and threshold sensitivity clarify the gap between NER and RE consistency signals\", \"model_name\": \"N/A (reuse pilot_004 samples)\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004\", \"data_count\": 551, \"server\": \"autodl-5090\", \"seed\": 42, \"parent\": \"mvp_pilot_004\", \"method\": \"Per-relation-type SJ/FK/voting rho, error propagation classification, threshold sensitivity, bootstrap CI, Fisher z-test NER vs RE\", \"command\": \"python3 code/analyze_exp004_re_diagnostic.py\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp004_re_diagnostic\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/exp004_re_diagnostic/\", \"checkpoint_source\": \"mvp_pilot_004\", \"eval_data\": \"scierc_test_551\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T11:50:04.662Z\", \"metrics\": {\"per_relation_type\": {\"HYPONYM-OF\": {\"n\": 36, \"rho_sj\": 0.545, \"rho_fk\": 0.646, \"rho_vc\": 0.628, \"mean_f1\": 0.513}, \"CONJUNCTION\": {\"n\": 86, \"rho_sj\": 0.383, \"rho_fk\": 0.35, \"rho_vc\": 0.484, \"mean_f1\": 0.48}, \"USED-FOR\": {\"n\": 299, \"rho_sj\": 0.236, \"rho_fk\": 0.255, \"rho_vc\": 0.286, \"mean_f1\": 0.422}, \"PART-OF\": {\"n\": 44, \"rho_sj\": 0.239, \"rho_fk\": 0.348, \"rho_vc\": 0.283, \"mean_f1\": 0.297}, \"EVALUATE-FOR\": {\"n\": 62, \"rho_sj\": 0.172, \"rho_fk\": 0.255, \"rho_vc\": 0.226, \"mean_f1\": 0.365}, \"COMPARE\": {\"n\": 35, \"rho_sj\": 0.168, \"rho_fk\": 0.184, \"rho_vc\": 0.18, \"mean_f1\": 0.453}, \"FEATURE-OF\": {\"n\": 50, \"rho_sj\": 0.004, \"rho_fk\": 0.052, \"rho_vc\": 0.014, \"mean_f1\": 0.254}}, \"error_propagation\": {\"total_fn\": 553, \"tail_error_pct\": 21.9, \"full_error_pct\": 21.7, \"head_error_pct\": 17.7, \"head_tail_error_pct\": 15.9, \"type_error_pct\": 8.3, \"worst_consistency\": \"head_type_error (sj=0.411)\", \"best_consistency\": \"head_error (sj=0.613)\"}, \"threshold_sensitivity\": {\"thr_0.00_rho_sj\": 0.3161, \"thr_0.00_rho_vc\": 0.3841, \"thr_0.00_n\": 313, \"thr_0.05_rho_sj\": 0.2682, \"thr_0.05_rho_vc\": 0.2364, \"thr_0.05_n\": 239}, \"bootstrap_ci_95\": {\"ner_sj\": [0.2946, 0.4586], \"ner_voting_conf\": [0.3048, 0.4656], \"re_sj\": [0.1422, 0.3391], \"re_voting_conf\": [0.1818, 0.3721], \"re_cond_sj\": [0.2161, 0.4102], \"re_cond_voting_conf\": [0.2825, 0.474]}, \"fisher_z_ner_vs_re\": {\"sj_z\": 2.31, \"sj_p\": 0.0209, \"sj_significant\": true, \"fk_z\": -0.31, \"fk_p\": 0.756, \"fk_significant\": false, \"voting_z\": 1.914, \"voting_p\": 0.0556, \"voting_significant\": false}, \"diagnosis\": \"FEATURE-OF is near-zero rho across all signals (n=50, F1=0.254). HYPONYM-OF strongest (rho_fk=0.646). Entity span errors (head+tail) account for 55.5% of RE FN. NER rho_sj significantly > RE rho_sj (p=0.021). Voting_conf is best RE signal in conditional set (rho=0.384).\"}}, \"exp_005\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T11:45:16.360Z\", \"updated_at\": \"2026-05-14T11:45:38.570Z\", \"spec\": {\"hypothesis\": \"Temperature sensitivity: systematic comparison of T=0.7 vs T=1.0 on all 5 confidence signals\", \"method\": \"CPU-only analysis from checkpoint metrics (pilot_004 T=1.0, pilot_005 T=0.7, exp_012/013/014)\", \"data_count\": 551, \"model_name\": \"Qwen3-8B-SciERC-LoRA-v2\", \"data_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/exp005_temperature/\", \"server\": \"local\", \"seed\": 42, \"parent\": \"mvp_pilot_004,mvp_pilot_005\", \"command\": \"python3 analyze_exp005_temperature.py\", \"checkpoint_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/exp005_temperature/\", \"log_path\": \"N/A\", \"checkpoint_source\": \"pilot_004+pilot_005 checkpoint metrics\", \"eval_data\": \"SciERC test set (n=551)\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T11:45:38.570Z\"}, \"exp_014_entity_majority_voting\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T10:53:21.203Z\", \"updated_at\": \"2026-05-14T11:33:30.085Z\", \"spec\": {\"hypothesis\": \"Entity-level majority voting confidence beats SJ as correlation signal\", \"model_name\": \"N/A (reuse pilot_004 samples)\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004\", \"data_count\": 551, \"server\": \"autodl-5090\", \"seed\": 42, \"parent\": \"mvp_pilot_004\", \"method\": \"Per-entity voting across N=8 samples, consensus construction, confidence = mean voting rate\", \"command\": \"python code/analyze_entity_voting.py\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004/exp014_entity_voting_report.json\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T11:18:09.468Z\", \"metrics\": {\"ner_full_rho\": 0.3915, \"ner_full_p\": 8.1e-21, \"ner_full_tau\": 0.2906, \"ner_full_auroc\": 0.7039, \"re_full_rho\": 0.3403, \"re_full_p\": 3.21e-12, \"re_full_tau\": 0.256, \"re_full_auroc\": 0.6668, \"ner_voting_f1\": 0.6246, \"ner_greedy_f1\": 0.6483, \"ner_oracle_f1\": 0.7793, \"re_voting_f1\": 0.3577, \"re_greedy_f1\": 0.4022, \"re_oracle_f1\": 0.5886, \"diagnosis\": \"Voting confidence BEATS SJ on both NER (rho 0.392 vs 0.383) and RE (0.340 vs 0.244). But voting as selection strategy LOSES to greedy.\"}}, \"exp_013_exact_match_voting\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T10:53:18.753Z\", \"updated_at\": \"2026-05-14T11:33:22.644Z\", \"spec\": {\"hypothesis\": \"Exact-match voting rate correlates with F1\", \"model_name\": \"N/A (reuse pilot_004 samples)\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004\", \"data_count\": 551, \"server\": \"autodl-5090\", \"seed\": 42, \"parent\": \"mvp_pilot_004\", \"method\": \"Count exact-match duplicates across N=8 samples\", \"command\": \"python code/analyze_exact_match_voting.py\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004/exp013_exact_match_report.json\"}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-14T11:18:09.026Z\", \"metrics\": {\"ner_full_rho\": 0.2941, \"ner_full_p\": 5.12e-12, \"ner_full_tau\": 0.2181, \"ner_full_auroc\": 0.6398, \"re_full_rho\": 0.1562, \"re_full_p\": 0.0018, \"re_full_tau\": 0.1185, \"re_full_auroc\": 0.5863, \"diagnosis\": \"EM between SJ and FK on NER, weakest on RE. Too coarse-grained.\"}}, \"exp_012_logprob_baseline\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T10:53:16.166Z\", \"updated_at\": \"2026-05-14T11:13:30.240Z\", \"spec\": {\"hypothesis\": \"Log-probability baseline: mean sequence log-prob correlates with F1 as well as or better than SJ\", \"model_name\": \"ft_002_v2 (qwen3-8b-scierc-merged-v2)\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004\", \"data_count\": 551, \"server\": \"autodl-5090\", \"seed\": 42, \"parent\": \"mvp_pilot_004\", \"method\": \"vLLM forward pass for log-probs + Spearman rho + AUROC + Kendall tau\", \"command\": \"python3 code/extract_logprobs.py\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004/logprob_analysis.log\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T11:06:42.542Z\", \"metrics\": {\"ner_full_rho_sj\": 0.3565, \"ner_full_rho_fk\": 0.2651, \"ner_full_rho_logprob\": 0.1396, \"ner_full_rho_greedy_logprob\": 0.1615, \"ner_full_tau_sj\": 0.2658, \"ner_full_tau_logprob\": 0.1006, \"ner_full_auroc_sj\": 0.6892, \"ner_full_auroc_fk\": 0.6292, \"ner_full_auroc_logprob\": 0.5907, \"ner_full_n\": 529, \"ner_sj_vs_logprob_delta\": 0.2169, \"re_full_rho_sj\": 0.2112, \"re_full_rho_fk\": 0.2528, \"re_full_rho_logprob\": 0.2467, \"re_full_auroc_sj\": 0.5916, \"re_full_auroc_fk\": 0.6262, \"re_full_auroc_logprob\": 0.6186, \"re_full_n\": 397, \"re_cond_rho_sj\": 0.3683, \"re_cond_rho_fk\": 0.3168, \"re_cond_rho_logprob\": 0.1457, \"re_cond_auroc_sj\": 0.6839, \"re_cond_auroc_logprob\": 0.5487, \"re_cond_n\": 296, \"diagnosis\": \"NER: SJ crushes logprob (rho +0.217). RE full: logprob slightly ahead. RE cond: SJ crushes logprob (rho +0.223). SJ unique value CONFIRMED.\"}}, \"mvp_pilot_005\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T09:14:09.456Z\", \"updated_at\": \"2026-05-14T09:47:06.597Z\", \"spec\": {\"hypothesis\": \"T=0.7 降低 RE zero rate，恢复 SJ>FK，rho_sj 可能 ≥ 0.30 (MARGINAL threshold)\", \"model_name\": \"Qwen3-8B-SciERC-LoRA-v2 (ft_002_v2 final)\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/scierc/processed_data\", \"data_count\": 551, \"server\": \"autodl-5090\", \"seed\": 42, \"parent\": \"ft_002_v2\", \"method\": \"N=8 sampling T=0.7 + XGrammar + span realignment + max_tokens=1024 + gold-empty filter + conditional rho\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python3 code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 0.7 --max_tokens 1024 --output_dir output/mvp_pilot_005 --num_test 551 --seed 42 --tensor_parallel 1\", \"gpu\": \"cuda:0\", \"pid\": 32456, \"tmux_session\": \"mvp_pilot_005\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_005/train.log\"}, \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_005\", \"metrics\": {\"ner_greedy_f1\": 0.6619, \"ner_oracle_f1\": 0.7585, \"ner_headroom\": 0.0966, \"ner_fleiss_kappa_mean\": 0.4722, \"ner_soft_jaccard_mean\": 0.7757, \"ner_full_rho_sj\": 0.3875, \"ner_full_rho_fk\": 0.3211, \"ner_full_n\": 529, \"ner_cond_rho_sj\": 0.3868, \"ner_cond_rho_fk\": 0.305, \"ner_cond_n\": 504, \"ner_sj_beats_fk_full\": true, \"ner_sj_beats_fk_cond\": true, \"ner_rho_advantage\": 0.0664, \"ner_sample_f1_mean\": 0.6243, \"ner_sample_f1_std\": 0.3131, \"ner_sample_f1_pct_zero\": 11.2, \"ner_gold_empty_filtered\": 22, \"ner_all_zero_filtered\": 25, \"re_greedy_f1\": 0.4219, \"re_oracle_f1\": 0.5532, \"re_headroom\": 0.1313, \"re_fleiss_kappa_mean\": 0.3829, \"re_soft_jaccard_mean\": 0.687, \"re_full_rho_sj\": 0.2343, \"re_full_rho_fk\": 0.1835, \"re_full_n\": 397, \"re_cond_rho_sj\": 0.3716, \"re_cond_rho_fk\": 0.2533, \"re_cond_n\": 301, \"re_sj_beats_fk_full\": true, \"re_sj_beats_fk_cond\": true, \"re_rho_advantage\": 0.0508, \"re_sample_f1_mean\": 0.3782, \"re_sample_f1_std\": 0.3845, \"re_sample_f1_pct_zero\": 42.4, \"re_gold_empty_filtered\": 154, \"re_all_zero_filtered\": 96, \"parse_failures\": 0, \"verdict\": \"FAIL\", \"verdict_note\": \"RE full rho_sj=0.234 < 0.40; RE cond rho_sj=0.372 passes conditional but not full threshold\"}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-14T09:47:06.597Z\"}, \"e1_component_wise_re_sj\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T09:15:17.262Z\", \"updated_at\": \"2026-05-14T09:23:38.818Z\", \"spec\": {\"hypothesis\": \"RE SJ 乘性惩罚是 root cause：分解后 head_sj ρ ≈ NER ρ (~0.38)，tail_sj 和乘性组合拖低整体 ρ\", \"model_name\": \"N/A (reuse pilot_004 samples)\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004\", \"data_count\": 397, \"server\": \"autodl-5090\", \"seed\": 42, \"parent\": \"mvp_pilot_004\", \"method\": \"Component-wise decomposition: head_sj, tail_sj, type_match 分别计算 Spearman ρ vs per-instance RE F1\", \"command\": \"python3 code/analyze_component_wise_re.py\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004/e1_component_analysis.log\"}, \"conclusion\": \"negative\", \"metrics\": {\"full_head_sj_rho\": 0.21, \"full_tail_sj_rho\": 0.201, \"full_type_match_rho\": 0.201, \"full_multiplicative_rho\": 0.244, \"full_additive_rho\": 0.243, \"full_fleiss_kappa_rho\": 0.278, \"cond_head_sj_rho\": 0.27, \"cond_tail_sj_rho\": 0.259, \"cond_type_match_rho\": 0.252, \"cond_multiplicative_rho\": 0.316, \"cond_additive_rho\": 0.306, \"cond_fleiss_kappa_rho\": 0.307, \"n_full\": 397, \"n_conditional\": 313, \"diagnosis\": \"head_sj rho=0.210 FAR from NER rho=0.383. Multiplicative penalty hypothesis REJECTED. Problem is fundamental: span-level SJ lacks discriminative power for RE.\"}, \"completed_at\": \"2026-05-14T09:22:26.155Z\"}, \"mvp_pilot_004\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T08:51:38.203Z\", \"updated_at\": \"2026-05-14T09:10:40.918Z\", \"spec\": {\"hypothesis\": \"With improved RE quality (F1=41.8%), structural self-consistency (soft Jaccard) correlates with per-instance F1 better than surface Fleiss Kappa, reaching rho_sj >= 0.40 on RE\", \"model_name\": \"Qwen3-8B-SciERC-LoRA-v2 (ft_002_v2 final)\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/scierc/processed_data\", \"data_count\": 551, \"server\": \"autodl-5090\", \"seed\": 42, \"parent\": \"ft_002_v2\", \"method\": \"N=8 sampling T=1.0 + XGrammar + span realignment + max_tokens=1024 + gold-empty filter + conditional rho\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python3 code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-merged-v2 --data_dir data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 1.0 --max_tokens 1024 --output_dir output/mvp_pilot_004 --num_test 551 --seed 42 --tensor_parallel 1\", \"gpu\": \"cuda:0\", \"pid\": 31041, \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004/mvp_pilot_004.log\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004\"}, \"metrics\": {\"ner_greedy_f1\": 0.6671, \"ner_oracle_f1\": 0.7756, \"ner_headroom\": 0.1085, \"ner_fleiss_kappa_mean\": 0.4048, \"ner_soft_jaccard_mean\": 0.7008, \"ner_full_rho_fk\": 0.259, \"ner_full_rho_sj\": 0.3825, \"ner_full_n\": 529, \"ner_cond_rho_fk\": 0.2352, \"ner_cond_rho_sj\": 0.3762, \"ner_cond_n\": 508, \"ner_sj_beats_fk_full\": true, \"ner_sj_beats_fk_cond\": true, \"ner_sample_f1_mean\": 0.6084, \"ner_sample_f1_std\": 0.3174, \"ner_sample_f1_pct_zero\": 12.19, \"ner_gold_empty_filtered\": 22, \"ner_all_zero_filtered\": 21, \"re_greedy_f1\": 0.4208, \"re_oracle_f1\": 0.5882, \"re_headroom\": 0.1674, \"re_fleiss_kappa_mean\": 0.2996, \"re_soft_jaccard_mean\": 0.6114, \"re_full_rho_fk\": 0.2782, \"re_full_rho_sj\": 0.2441, \"re_full_n\": 397, \"re_cond_rho_fk\": 0.3067, \"re_cond_rho_sj\": 0.3161, \"re_cond_n\": 313, \"re_sj_beats_fk_full\": false, \"re_sj_beats_fk_cond\": true, \"re_sample_f1_mean\": 0.3612, \"re_sample_f1_std\": 0.383, \"re_sample_f1_pct_zero\": 44.3, \"re_gold_empty_filtered\": 154, \"re_all_zero_filtered\": 84, \"parse_failures\": 0, \"verdict\": \"FAIL\"}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-14T09:10:40.918Z\"}, \"ft_002_v2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T08:28:40.861Z\", \"updated_at\": \"2026-05-14T08:51:32.405Z\", \"spec\": {\"hypothesis\": \"Extended training (5 epochs, LoRA r=32) with OOM fix improves RE F1 above 40% threshold\", \"model_name\": \"Qwen/Qwen3-8B\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/llmfactory_train.json\", \"data_count\": 1861, \"server\": \"autodl-5090\", \"seed\": 42, \"parent\": \"ft_001\", \"method\": \"LoRA r=32 alpha=64, 5 epochs, batch=2 grad_accum=8 gradient_checkpointing=true\", \"gpu\": \"cuda:1\", \"pid\": 24947, \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/ft_002v2_train.log\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-scierc-lora-v2\", \"command\": \"CUDA_VISIBLE_DEVICES=1 llamafactory-cli train train_config_v2.yaml\"}, \"conclusion\": \"success\", \"metrics\": {\"epoch\": 5, \"train_loss\": 0.0806, \"eval_loss\": 0.089, \"train_runtime\": \"28m41s\", \"train_samples_per_second\": 5.407, \"train_steps_per_second\": 0.34, \"total_steps\": 585, \"checkpoints\": [\"checkpoint-400\", \"checkpoint-500\", \"checkpoint-585\"], \"gate0_final_ner_f1\": 0.6615, \"gate0_final_re_f1\": 0.4177, \"gate0_final_parse_failures\": 0, \"gate0_final_ner_pass\": true, \"gate0_final_re_pass\": true, \"gate0_final_pass\": true, \"gate0_ckpt400_ner_f1\": 0.6475, \"gate0_ckpt400_re_f1\": 0.3793, \"gate0_ckpt400_parse_failures\": 0, \"gate0_ckpt400_verdict\": \"FAIL\", \"gate0_ckpt400_re_sample_f1_pct_zero\": 58.8, \"gate0_ckpt400_warning\": \">30% samples F1=0\"}, \"completed_at\": \"2026-05-14T08:51:32.405Z\"}, \"mvp_pilot_002\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T08:02:16.991Z\", \"updated_at\": \"2026-05-14T08:48:14.040Z\", \"spec\": {\"hypothesis\": \"Structural self-consistency (soft Jaccard) correlates with per-instance F1 better than surface Fleiss Kappa on fine-tuned Qwen3-8B SciERC\", \"model_name\": \"Qwen3-8B-SciERC-LoRA (ft_001)\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/scierc\", \"data_count\": 551, \"server\": \"autodl-5090\", \"seed\": 42, \"parent\": \"ft_001\", \"method\": \"N=8 sampling T=1.0 + XGrammar + span realignment + gold-empty filter + conditional rho\", \"gpu\": \"cuda:0\", \"note\": \"Rerun of mvp_pilot_001 which crashed silently\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python3 code/run_mvp_pilot.py --model_path checkpoints/qwen3-8b-scierc-lora --data_dir data/scierc --dataset scierc --subtask joint --n_samples 8 --temperature 1.0 --max_tokens 512 --output_dir output/mvp_pilot_001 --num_test 551 --seed 42 --tensor_parallel 1\", \"failure_reason\": \"Worker used LoRA adapter path instead of merged model path; vLLM cannot load LoRA adapter directly\"}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-14T08:48:14.040Z\"}, \"ft_002\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T07:39:18.640Z\", \"updated_at\": \"2026-05-14T08:28:00.590Z\", \"spec\": {\"hypothesis\": \"Extended training (5 epochs, LoRA r=32) improves RE F1 above 40% threshold\", \"model_name\": \"Qwen/Qwen3-8B\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/llmfactory_train.json\", \"data_count\": 1861, \"server\": \"autodl-5090\", \"seed\": 42, \"parent\": \"ft_001\", \"method\": \"LoRA r=32 alpha=64, 5 epochs, relation direction hint\", \"command\": \"llamafactory-cli train /root/autodl-tmp/struct_self_consist_ie/train_config_v2.yaml\", \"gpu\": \"cuda:1\", \"pid\": 19666, \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/ft_002_train.log\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-scierc-lora-v2\", \"total_steps\": 585, \"trainable_params\": \"87.3M\", \"estimated_runtime\": \"29min\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T08:02:30.390Z\", \"metrics\": {\"last_step\": 70, \"total_steps\": 585, \"progress_pct\": 11.97, \"last_loss\": 0.1134, \"last_lr\": 0.00019982, \"elapsed\": \"3m32s\", \"failure_reason\": \"OOM at step 73, batch_size=4 too large for 32GB RTX 5090\"}}, \"ft_001\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T06:04:28.030Z\", \"updated_at\": \"2026-05-14T08:27:58.182Z\", \"spec\": {\"hypothesis\": \"Fine-tuned Qwen3-8B on SciERC UIE can achieve NER F1 >= 73 and serve as base model for structural consistency MVP\", \"model_name\": \"Qwen/Qwen3-8B\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/scierc\", \"data_count\": 1861, \"server\": \"autodl-5090\", \"seed\": 42, \"method\": \"LoRA r=16 alpha=32\", \"framework\": \"LLaMA Factory 0.9.4\", \"command\": \"sft training qwen3-8b on scierc with lora\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-scierc-lora/\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/ft_001_train.log\", \"train_loss\": 0.1099, \"eval_loss\": 0.0771, \"epoch\": 3, \"train_runtime\": \"0:17:49\", \"note\": \"gate0: NER PASS 60.4% / RE FAIL 33.8%\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T06:30:32.889Z\", \"metrics\": {\"train_loss\": 0.1099, \"eval_loss\": 0.0771, \"gate0_ner_f1_strict\": 0.1143, \"gate0_re_f1_strict\": 0.0125, \"gate0_ner_f1_text\": 0.606, \"gate0_re_f1_text\": 0.3392, \"gate0_offset_accuracy\": 0.1665, \"gate0_parse_failures\": 43, \"gate0_pass\": false, \"gate0_realigned_ner_f1\": 0.6045, \"gate0_realigned_re_f1\": 0.338, \"gate0_realigned_entity_offset_accuracy\": 1, \"gate0_realigned_relation_offset_accuracy\": 1, \"gate0_realigned_ner_pass\": true, \"gate0_realigned_re_pass\": false, \"gate0_realigned_pass\": false, \"gate0_ner_f1_delta_realign\": 0.4901, \"gate0_re_f1_delta_realign\": 0.3255, \"verdict_note\": \"partial: NER PASS (60.4%) / RE FAIL (33.8% < 40%)\"}}, \"mvp_pilot_003\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T08:21:09.847Z\", \"updated_at\": \"2026-05-14T08:21:44.983Z\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python code/run_mvp_pilot.py --model_path /root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-scierc-merged --data_dir /root/autodl-tmp/struct_self_consist_ie/data/scierc/processed_data --dataset scierc --subtask joint --n_samples 8 --temperature 1.0 --max_tokens 1024 --output_dir /root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_003 --num_test 551 --seed 42 --tensor_parallel 1\", \"server\": \"autodl-5090\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/scierc/processed_data\", \"data_count\": 551, \"model_name\": \"qwen3-8b-scierc-merged\", \"seed\": 42}, \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/mvp_pilot_003.log\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_003\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-14T08:21:30.319Z\", \"metrics\": {\"ner_greedy_f1\": 0.6362, \"ner_oracle_f1\": 0.792, \"ner_headroom\": 0.1559, \"ner_fleiss_kappa_mean\": 0.2488, \"ner_soft_jaccard_mean\": 0.5066, \"ner_full_rho_sj\": 0.3808, \"ner_full_rho_fk\": 0.3362, \"ner_full_p_sj\": 1.07e-19, \"ner_full_p_fk\": 1.93e-15, \"ner_full_n\": 529, \"ner_cond_rho_sj\": 0.3836, \"ner_cond_rho_fk\": 0.3187, \"ner_cond_p_sj\": 1.83e-19, \"ner_cond_p_fk\": 1.33e-13, \"ner_cond_n\": 514, \"ner_sj_beats_fk_full\": true, \"ner_sj_beats_fk_cond\": true, \"ner_rho_advantage\": 0.0446, \"ner_sample_f1_mean\": 0.5153, \"ner_sample_f1_std\": 0.3334, \"ner_sample_f1_pct_zero\": 19.9, \"ner_gold_empty_filtered\": 22, \"ner_all_zero_filtered\": 15, \"re_greedy_f1\": 0.3774, \"re_oracle_f1\": 0.5939, \"re_headroom\": 0.2165, \"re_fleiss_kappa_mean\": 0.0879, \"re_soft_jaccard_mean\": 0.3958, \"re_full_rho_sj\": 0.2367, \"re_full_rho_fk\": 0.2221, \"re_full_p_sj\": 1.85e-06, \"re_full_p_fk\": 7.92e-06, \"re_full_n\": 397, \"re_cond_rho_sj\": 0.3004, \"re_cond_rho_fk\": 0.2374, \"re_cond_p_sj\": 2.25e-08, \"re_cond_p_fk\": 1.19e-05, \"re_cond_n\": 333, \"re_sj_beats_fk_full\": true, \"re_sj_beats_fk_cond\": true, \"re_rho_advantage\": 0.0146, \"re_sample_f1_mean\": 0.1977, \"re_sample_f1_std\": 0.3251, \"re_sample_f1_pct_zero\": 67.6, \"re_gold_empty_filtered\": 154, \"re_all_zero_filtered\": 64, \"parse_failures_stochastic\": 0, \"parse_failures_greedy\": 0, \"total_stochastic_samples\": 4408, \"total_greedy\": 551, \"verdict\": \"FAIL\", \"verdict_reason\": \"RE full rho_sj=0.2367 < 0.40 threshold; strong signal exists but below PASS bar\"}}, \"mvp_pilot_001\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T07:39:16.313Z\", \"updated_at\": \"2026-05-14T08:05:34.348Z\", \"spec\": {\"hypothesis\": \"Structural self-consistency (soft Jaccard) correlates with per-instance F1 better than surface Fleiss Kappa on fine-tuned Qwen3-8B SciERC\", \"model_name\": \"qwen3-8b-scierc-merged\", \"data_path\": \"/root/autodl-tmp/struct_self_consist_ie/data/test.jsonl\", \"data_count\": 551, \"server\": \"autodl-5090\", \"seed\": 42, \"parent\": \"ft_001\", \"method\": \"N=8 sampling T=1.0 + XGrammar + span realignment\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python3 code/mvp_pilot.py\", \"checkpoint_path\": \"/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-scierc-merged\", \"log_path\": \"/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_001.log\"}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-14T07:52:47.006Z\", \"metrics\": {\"ner_greedy_f1\": 0.611, \"ner_oracle_f1\": 0.78, \"ner_headroom\": 0.169, \"ner_fleiss_kappa_mean\": 0.2449, \"ner_soft_jaccard_mean\": 0.5041, \"ner_full_rho_sj\": 0.3616, \"ner_full_rho_fk\": 0.3515, \"ner_full_n\": 529, \"ner_cond_rho_sj\": 0.3688, \"ner_cond_rho_fk\": 0.3569, \"ner_cond_n\": 510, \"ner_sj_beats_fk_full\": true, \"ner_sj_beats_fk_cond\": true, \"ner_sample_f1_pct_zero\": 20.4, \"ner_gold_empty_filtered\": 22, \"ner_all_zero_filtered\": 19, \"re_greedy_f1\": 0.355, \"re_oracle_f1\": 0.572, \"re_headroom\": 0.217, \"re_fleiss_kappa_mean\": 0.0681, \"re_soft_jaccard_mean\": 0.3635, \"re_full_rho_sj\": 0.2535, \"re_full_rho_fk\": 0.2885, \"re_full_n\": 397, \"re_cond_rho_sj\": 0.3515, \"re_cond_rho_fk\": 0.3107, \"re_cond_n\": 320, \"re_sj_beats_fk_full\": false, \"re_sj_beats_fk_cond\": true, \"re_sample_f1_pct_zero\": 58.3, \"re_gold_empty_filtered\": 154, \"re_all_zero_filtered\": 77, \"parse_failures_stochastic\": 164, \"parse_failures_greedy\": 29, \"total_stochastic_samples\": 4408, \"total_greedy\": 551, \"verdict\": \"FAIL\", \"verdict_reason\": \"RE full rho_sj=0.2535 < 0.40; SJ does not beat FK on RE full set\"}}}, \"count\": 329, \"total\": 329, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.9114}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 11_

<details open><summary>🔧 Tool call — Agent · `toolu_01UeLJnTZrz1DCdCXEbYiG7f`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Explore project code structure",
  "prompt": "Explore the project at /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/\n\nI need to understand:\n1. The overall directory structure (especially src/ and any analysis scripts)\n2. Any scripts related to N-scaling analysis, transition analysis, or inverse scaling\n3. How samples.jsonl files are structured and processed\n4. Any existing code that computes F1 scores for different methods (MV, LP-best, LP-weighted, uniform construction)\n\nSearch broadly - check src/, scripts/, analysis/, notebooks/ etc. Look for files with names containing \"scaling\", \"transition\", \"n_scaling\", \"analyze\". Also grep for \"inverse\" and \"transition\" in Python files.\n\nReport: file paths, key functions, and data format details."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3",
  "uuid": "05b492c3-af9e-4d0a-b149-91ffa37cf4e7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GzhC4uJYbBrck6LLEpAeFc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2270,
      "cache_read_input_tokens": 24484,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2270
      },
      "output_tokens": 19,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### System

_source line 12_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "ac8ef46b1ece704fd",
  "tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "description": "Explore project code structure",
  "task_type": "local_agent",
  "prompt": "Explore the project at /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/\n\nI need to understand:\n1. The overall directory structure (especially src/ and any analysis scripts)\n2. Any scripts related to N-scaling analysis, transition analysis, or inverse scaling\n3. How samples.jsonl files are structured and processed\n4. Any existing code that computes F1 scores for different methods (MV, LP-best, LP-weighted, uniform construction)\n\nSearch broadly - check src/, scripts/, analysis/, notebooks/ etc. Look for files with names containing \"scaling\", \"transition\", \"n_scaling\", \"analyze\". Also grep for \"inverse\" and \"transition\" in Python files.\n\nReport: file paths, key functions, and data format details.",
  "uuid": "f1dcf3e5-4beb-4606-9861-14edc9a687d5",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3"
}
```

---


## Round 1

## Round 1

109 recorded events


### User

_source line 13 · 2026-05-23T18:54:50.384Z_

Explore the project at /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/

I need to understand:
1. The overall directory structure (especially src/ and any analysis scripts)
2. Any scripts related to N-scaling analysis, transition analysis, or inverse scaling
3. How samples.jsonl files are structured and processed
4. Any existing code that computes F1 scores for different methods (MV, LP-best, LP-weighted, uniform construction)

Search broadly - check src/, scripts/, analysis/, notebooks/ etc. Look for files with names containing "scaling", "transition", "n_scaling", "analyze". Also grep for "inverse" and "transition" in Python files.

Report: file paths, key functions, and data format details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3",
  "uuid": "84ed8fdb-14ba-4f0e-a8dd-48692729d197"
}
```

</details>

---


### System

_source line 14_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac8ef46b1ece704fd",
  "tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "description": "Running find /home/ubuntu/.agent-ml-research-idea_gen_051…",
  "usage": {
    "total_tokens": 17962,
    "tool_uses": 1,
    "duration_ms": 1463
  },
  "last_tool_name": "Bash",
  "uuid": "3971e68b-518f-4281-9aac-dcbaac3ac48e",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3"
}
```

---


### Tool call

_source line 15_

<details open><summary>🔧 Tool call — Bash · `toolu_01HY4epyKS45JBCgNrpmoCWY`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie -type f -name \"*.py\" | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3",
  "uuid": "90eee21a-74a8-4cef-8167-9a97789fbec4",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01RQqfVKhouU6B8PMkLaT4Mj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17953,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17953,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 16 · 2026-05-23T18:54:52.052Z_

<details><summary>↩ Tool result · `toolu_01HY4epyKS45JBCgNrpmoCWY`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/figures/paper/fig_signal_heatmap.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/figures/paper/fig_reliability.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/scripts/j_calibration.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/scripts/adalp_analysis.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/scripts/dals_analysis.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/_gen_fig_bound.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/_gen_n_scaling.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/gen_fig_overview.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/e1_signal_routing.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.venv/lib/python3.14/site-packages/mpl_toolkits/axes_grid1/mpl_axes.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.venv/lib/python3.14/site-packages/mpl_toolkits/axes_grid1/axes_divider.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.venv/lib/python3.14/site-packages/mpl_toolkits/axes_grid1/anchored_artists.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.venv/lib/python3.14/site-packages/mpl_toolkits/axes_grid1/axes_size.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.venv/lib/python3.14/site-packages/mpl_toolkits/axes_grid1/tests/conftest.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.venv/lib/python3.14/site-packages/mpl_toolkits/axes_grid1/tests/test_axes_grid1.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.venv/lib/python3.14/site-packages/mpl_toolkits/axes_grid1/tests/__init__.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.venv/lib/python3.14/site-packages/mpl_toolkits/axes_grid1/axes_rgb.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.venv/lib/python3.14/site-packages/mpl_toolkits/axes_grid1/parasite_axes.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.venv/lib/python3.14/site-packages/mpl_toolkits/axes_grid1/axes_grid.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.venv/lib/python3.14/site-packages/mpl_toolkits/axes_grid1/__init__.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3",
  "uuid": "d23dbc9e-6837-4a49-a69c-522778f9f5d9"
}
```

</details>

---


### System

_source line 17_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac8ef46b1ece704fd",
  "tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "description": "Running ls -la /home/ubuntu/.agent-ml-research-idea_gen_0…",
  "usage": {
    "total_tokens": 19992,
    "tool_uses": 2,
    "duration_ms": 3139
  },
  "last_tool_name": "Bash",
  "uuid": "26fa1338-46ba-4ca6-a1ba-931d80042e71",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3"
}
```

---


### Tool call

_source line 18_

<details open><summary>🔧 Tool call — Bash · `toolu_015Pg2MbaTQtJ4w3qZQWcgn1`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/ | grep -v \".venv\\|__pycache__\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3",
  "uuid": "dbe4d8f7-d27a-433e-ab35-92bcabfdfeff",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_013EHecP9bKUY9CpNvha1G2C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 2026,
      "cache_read_input_tokens": 17953,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2026,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 19 · 2026-05-23T18:54:53.589Z_

<details><summary>↩ Tool result · `toolu_015Pg2MbaTQtJ4w3qZQWcgn1`</summary>

```text
total 1340
drwxr-xr-x  14 ubuntu ubuntu   4096 May 23 16:40 .
drwxrwxr-x   4 ubuntu ubuntu   4096 May 14 04:20 ..
drwxr-xr-x   3 ubuntu ubuntu   4096 May 14 04:20 .claude
-rw-r--r--   1 ubuntu ubuntu  14634 May 23 18:54 AGENTS.md
-rw-r--r--   1 ubuntu ubuntu      0 May 14 04:23 ROADMAP.lock
-rw-------   1 ubuntu ubuntu   3182 May 23 16:40 ROADMAP.md
-rw-r--r--   1 ubuntu ubuntu     90 May 23 16:45 _last_visual_review.json
-rw-r--r--   1 ubuntu ubuntu   7234 May 18 13:38 analysis_r21_q1_alignment.py
drwxr-xr-x 163 ubuntu ubuntu  20480 May 23 18:48 artifacts
-rw-r--r--   1 ubuntu ubuntu  22309 May 20 10:07 b2_entity_verifier.py
drwxr-xr-x   2 ubuntu ubuntu 176128 May 23 12:00 checkpoints
drwxr-xr-x   2 ubuntu ubuntu   4096 May 22 08:33 code
-rw-r--r--   1 ubuntu ubuntu      0 May 16 03:03 constraints.lock
-rw-------   1 ubuntu ubuntu    457 May 16 03:03 constraints.yaml
-rw-r--r--   1 ubuntu ubuntu      0 May 14 04:23 decisions.lock
-rw-------   1 ubuntu ubuntu 231414 May 22 20:53 decisions.yaml
drwxr-xr-x   4 ubuntu ubuntu   4096 May 23 14:12 docs
-rwxr-xr-x   1 ubuntu ubuntu      0 May 14 09:33 dream_registry.lock
-rw-------   1 ubuntu ubuntu  10823 May 22 06:36 dream_registry.yaml
-rw-r--r--   1 ubuntu ubuntu  10751 May 22 06:36 dream_registry.yaml.bak
-rw-r--r--   1 ubuntu ubuntu  14268 May 20 09:47 e1_signal_routing.py
-rw-r--r--   1 ubuntu ubuntu      0 May 14 11:49 experiment_plan.lock
-rw-------   1 ubuntu ubuntu  20031 May 20 20:11 experiment_plan.yaml
drwxr-xr-x   3 ubuntu ubuntu   4096 May 14 13:35 figures
-rw-r--r--   1 ubuntu ubuntu      0 May 14 15:47 literature_map.lock
-rw-------   1 ubuntu ubuntu  43680 May 14 19:51 literature_map.yaml
drwxr-xr-x   4 ubuntu ubuntu   4096 May 14 04:25 logs
-rw-r--r--   1 ubuntu ubuntu   8118 May 22 15:24 memory.md
-rw-r--r--   1 ubuntu ubuntu      0 May 17 07:38 mistakes.lock
-rw-------   1 ubuntu ubuntu  70496 May 22 19:08 mistakes.yaml
drwxr-xr-x   2 ubuntu ubuntu   4096 May 22 08:34 output
drwxr-xr-x   3 ubuntu ubuntu   4096 May 19 17:10 paper
-rw-r--r--   1 ubuntu ubuntu   6758 May 22 06:36 paper_framing.md
-rw-r--r--   1 ubuntu ubuntu      0 May 14 19:32 paper_provenance.lock
-rw-------   1 ubuntu ubuntu  40278 May 22 13:13 paper_provenance.yaml
-rw-r--r--   1 ubuntu ubuntu      0 May 14 06:04 registry.lock
-rw-------   1 ubuntu ubuntu 527665 May 23 12:00 registry.yaml
-rw-r--r--   1 ubuntu ubuntu   6736 May 23 11:40 report.md
-rw-r--r--   1 ubuntu ubuntu   2109 May 23 16:47 review_visual_check_state.json
drwxr-xr-x   2 ubuntu ubuntu   4096 May 20 10:20 scripts
-rwxr-xr-x   1 ubuntu ubuntu      0 May 14 04:21 study_status.lock
drwxr-xr-x   3 ubuntu ubuntu   4096 May 23 03:40 task_context
-rw-r--r--   1 ubuntu ubuntu  43021 May 15 00:12 writing_plan.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3",
  "uuid": "65eccfcc-36ca-4a4c-aa3e-fcbd766ffa4d"
}
```

</details>

---


### System

_source line 20_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac8ef46b1ece704fd",
  "tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "description": "Finding **/[n_]*scaling*.py",
  "usage": {
    "total_tokens": 21384,
    "tool_uses": 3,
    "duration_ms": 6130
  },
  "last_tool_name": "Glob",
  "uuid": "0823fe2a-9037-451f-bf3f-bf06be1e23cc",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3"
}
```

---


### Tool call

_source line 21_

<details open><summary>🔧 Tool call — Glob · `toolu_01NwGoXPvGPXyBkRT3hW5m2c`</summary>

```json
{
  "pattern": "**/[n_]*scaling*.py",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3",
  "uuid": "cd7dd5c2-14ce-46ae-9026-bf7ca6461ae4",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HDKQS18vkmA85xUBHCHuRe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1390,
      "cache_read_input_tokens": 19979,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1390,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 22 · 2026-05-23T18:54:56.626Z_

<details><summary>↩ Tool result · `toolu_01NwGoXPvGPXyBkRT3hW5m2c`</summary>

```text
docs/paper/figures/_gen_n_scaling.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3",
  "uuid": "af45d100-5f40-41f1-9227-990dbbc1c563"
}
```

</details>

---


### System

_source line 23_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac8ef46b1ece704fd",
  "tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "description": "Finding **/transition*.py",
  "usage": {
    "total_tokens": 21385,
    "tool_uses": 4,
    "duration_ms": 6535
  },
  "last_tool_name": "Glob",
  "uuid": "0c93f020-d2c0-4e8f-b385-457e2b2a979e",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3"
}
```

---


### Tool call

_source line 24_

<details open><summary>🔧 Tool call — Glob · `toolu_01KYkqyRB7rNdq8W3Wj9QmU2`</summary>

```json
{
  "pattern": "**/transition*.py",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3",
  "uuid": "26acf396-d8f5-4423-a5c1-7882e69a4828",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HDKQS18vkmA85xUBHCHuRe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1390,
      "cache_read_input_tokens": 19979,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1390,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 25 · 2026-05-23T18:54:57.027Z_

<details><summary>↩ Tool result · `toolu_01KYkqyRB7rNdq8W3Wj9QmU2`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3",
  "uuid": "bf00a966-e1e7-435b-b9eb-08dbd6fe7632"
}
```

</details>

---


### System

_source line 26_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac8ef46b1ece704fd",
  "tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "description": "Finding **/analyze*.py",
  "usage": {
    "total_tokens": 21386,
    "tool_uses": 5,
    "duration_ms": 6805
  },
  "last_tool_name": "Glob",
  "uuid": "44a3e3d8-80eb-45bd-88cc-1c5a1dff344b",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3"
}
```

---


### Tool call

_source line 27_

<details open><summary>🔧 Tool call — Glob · `toolu_01FV38rJof5dB11Ue3DcBHrZ`</summary>

```json
{
  "pattern": "**/analyze*.py",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3",
  "uuid": "56f05e71-bce7-46e7-870e-aac2cd219608",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HDKQS18vkmA85xUBHCHuRe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1390,
      "cache_read_input_tokens": 19979,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1390,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 28 · 2026-05-23T18:54:57.297Z_

<details><summary>↩ Tool result · `toolu_01FV38rJof5dB11Ue3DcBHrZ`</summary>

```text
artifacts/exp005_temperature/analyze_exp005_temperature.py
artifacts/exp_015_metrics_expansion/intermediate/analyze_exp015_metrics_expansion.py
artifacts/analyze_exp015_metrics_expansion.py
artifacts/exp_004_re_diagnostic/report/analyze_exp004_re_diagnostic.py
artifacts/analyze_exp004_re_diagnostic.py
artifacts/exp_016_signal_ensemble/intermediate/analyze_exp016_ensemble.py
artifacts/analyze_exp016_ensemble.py
artifacts/analyze_exp005_v2_temperature.py
artifacts/analyze_exp004_v2_re_diagnostic.py
artifacts/analyze_ood_signals.py
artifacts/exp-022/intermediate/analyze_3seed.py
artifacts/analyze_n32.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3",
  "uuid": "a71edcf2-4c67-43ed-a4f9-d42a06133298"
}
```

</details>

---


### System

_source line 29_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac8ef46b1ece704fd",
  "tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "description": "Running find /home/ubuntu/.agent-ml-research-idea_gen_051…",
  "usage": {
    "total_tokens": 21387,
    "tool_uses": 6,
    "duration_ms": 10817
  },
  "last_tool_name": "Bash",
  "uuid": "11e77b7a-7f1a-4282-adc3-8df9e5034541",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3"
}
```

---


### Tool call

_source line 30_

<details open><summary>🔧 Tool call — Bash · `toolu_01DHwBQG9RgRdgXZDZYmbjMg`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie -path \"./.venv\" -prune -o -type d \\( -name \"src\" -o -name \"scripts\" -o -name \"analysis\" -o -name \"docs\" \\) -print"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3",
  "uuid": "7ddd6e26-12d3-424c-b0c9-5816a6d4975e",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HDKQS18vkmA85xUBHCHuRe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1390,
      "cache_read_input_tokens": 19979,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1390,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 31 · 2026-05-23T18:55:01.386Z_

<details><summary>↩ Tool result · `toolu_01DHwBQG9RgRdgXZDZYmbjMg`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/scripts
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.venv/lib/python3.14/site-packages/numpy-2.4.4.dist-info/licenses/numpy/random/src
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.venv/lib/python3.14/site-packages/numpy-2.4.4.dist-info/licenses/numpy/_core/src
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.venv/lib/python3.14/site-packages/numpy/f2py/tests/src
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.venv/lib/python3.14/site-packages/numpy/f2py/src
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/experiments/humaneval_sc/.venv/lib/python3.14/site-packages/numpy/f2py/tests/src
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/experiments/humaneval_sc/.venv/lib/python3.14/site-packages/numpy/f2py/src
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/experiments/humaneval_sc/.venv/lib/python3.14/site-packages/pyarrow/src
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/experiments/humaneval_sc/.venv/lib/python3.14/site-packages/numpy-2.4.6.dist-info/licenses/numpy/random/src
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/experiments/humaneval_sc/.venv/lib/python3.14/site-packages/numpy-2.4.6.dist-info/licenses/numpy/_core/src
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/experiments/spider_sql/.venv/lib/python3.14/site-packages/numpy/f2py/tests/src
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/experiments/spider_sql/.venv/lib/python3.14/site-packages/numpy/f2py/src
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/experiments/spider_sql/.venv/lib/python3.14/site-packages/pyarrow/src
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/experiments/spider_sql/.venv/lib/python3.14/site-packages/numpy-2.4.6.dist-info/licenses/numpy/random/src
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/experiments/spider_sql/.venv/lib/python3.14/site-packages/numpy-2.4.6.dist-info/licenses/numpy/_core/src
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/experiments/frontier_sc/.venv/lib/python3.14/site-packages/numpy/f2py/tests/src
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/experiments/frontier_sc/.venv/lib/python3.14/site-packages/numpy/f2py/src
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/experiments/frontier_sc/.venv/lib/python3.14/site-packages/pyarrow/src
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/experiments/frontier_sc/.venv/lib/python3.14/site-packages/numpy-2.4.6.dist-info/licenses/numpy/random/src
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/experiments/frontier_sc/.venv/lib/python3.14/site-packages/numpy-2.4.6.dist-info/licenses/numpy/_core/src
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3",
  "uuid": "6e9c43c9-a5b0-4fdd-9e98-0e732c2da351"
}
```

</details>

---


### System

_source line 32_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac8ef46b1ece704fd",
  "tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "description": "Reading docs/paper/figures/_gen_n_scaling.py",
  "usage": {
    "total_tokens": 23367,
    "tool_uses": 7,
    "duration_ms": 12706
  },
  "last_tool_name": "Read",
  "uuid": "c11edeea-f2c8-4966-8661-b830e40698be",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3"
}
```

---


### Tool call

_source line 33_

<details open><summary>🔧 Tool call — Read · `toolu_01VM3YrwTxSjwJPpPgMzr16R`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/_gen_n_scaling.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3",
  "uuid": "66c19fa0-2d0e-44d5-b304-c865834d869c",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01M1h7oRX38nGhSQ4FeHx39X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 1977,
      "cache_read_input_tokens": 21369,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1977,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 34 · 2026-05-23T18:55:03.106Z_

<details><summary>↩ Tool result · `toolu_01VM3YrwTxSjwJPpPgMzr16R`</summary>

```text
1	import os
2	import matplotlib
3	matplotlib.use('Agg')
4	import matplotlib.pyplot as plt
5	import numpy as np
6	
7	plt.rcParams.update({
8	    'font.family': 'serif',
9	    'font.serif': ['Times New Roman', 'DejaVu Serif'],
10	    'font.size': 10,
11	    'axes.labelsize': 11,
12	    'xtick.labelsize': 9,
13	    'ytick.labelsize': 9,
14	    'legend.fontsize': 9,
15	    'figure.dpi': 300,
16	    'savefig.bbox': 'tight',
17	    'savefig.pad_inches': 0.02,
18	    'axes.linewidth': 0.8,
19	    'lines.linewidth': 1.5,
20	    'lines.markersize': 6,
21	})
22	
23	# Data (MV Delta pp, unified greedy baseline, seed=42)
24	n_vals_full = np.array([8, 16, 32, 64])
25	log2n_full = np.log2(n_vals_full)
26	
27	scierc  = np.array([-1.24, -0.61, +0.24, +0.53])
28	conll   = np.array([+0.20, +0.32, +0.44, +0.61])
29	
30	n_vals_fn = np.array([8, 16, 32])
31	log2n_fn  = np.log2(n_vals_fn)
32	fewnerd = np.array([-2.71, -1.65, -0.91])
33	
34	fig, ax = plt.subplots(figsize=(3.4, 2.4))
35	
36	# Break-even line
37	ax.axhline(y=0, color='#888888', linestyle=':', linewidth=0.8, zorder=1)
38	
39	# Dataset lines
40	ax.plot(log2n_full, conll, 'o-', color='#2176AE', label='CoNLL', zorder=3)
41	ax.plot(log2n_full, scierc, 's-', color='#E07A3A', label='SciERC', zorder=3)
42	ax.plot(log2n_fn, fewnerd, 'D-', color='#3A9A5B', label='Few-NERD', zorder=3)
43	
44	ax.set_xlabel(r'$\log_2 N$')
45	ax.set_ylabel(r'MV $\Delta$F1 (pp)')
46	ax.set_xticks([3, 4, 5, 6])
47	ax.set_xticklabels(['8', '16', '32', '64'])
48	ax.set_xlim(2.8, 6.2)
49	ax.set_ylim(-3.2, 1.2)
50	
51	ax.legend(loc='lower right', frameon=True, framealpha=0.9, edgecolor='#cccccc')
52	ax.spines['top'].set_visible(False)
53	ax.spines['right'].set_visible(False)
54	
55	out = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fig_n_scaling_mv.pdf')
56	fig.savefig(out, format='pdf')
57	plt.close()
58	print(f'Saved: {out}')
59	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3",
  "uuid": "43b5dfa9-c787-4ed0-a32d-e1ee001c2832"
}
```

</details>

---


### System

_source line 35_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac8ef46b1ece704fd",
  "tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "description": "Reading scripts",
  "usage": {
    "total_tokens": 23368,
    "tool_uses": 8,
    "duration_ms": 12851
  },
  "last_tool_name": "Read",
  "uuid": "e2e4832c-1b02-4491-9d62-7304c399c9d9",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3"
}
```

---


### Tool call

_source line 36_

<details open><summary>🔧 Tool call — Read · `toolu_01CP7SrrLQWgy5GVyJqAFgqr`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/scripts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3",
  "uuid": "87613ef4-e2e9-471d-adf8-e614080ce188",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01M1h7oRX38nGhSQ4FeHx39X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 1977,
      "cache_read_input_tokens": 21369,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1977,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 37 · 2026-05-23T18:55:03.242Z_

<details><summary>↩ Tool result · reported error · `toolu_01CP7SrrLQWgy5GVyJqAFgqr`</summary>

```text
EISDIR: illegal operation on a directory, read '/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/scripts'
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3",
  "uuid": "43adef73-41bc-46cf-8ef1-ac2665c5ff73",
  "tool_use_result": "Error: EISDIR: illegal operation on a directory, read '/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/scripts'"
}
```

</details>

---


### System

_source line 38_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac8ef46b1ece704fd",
  "tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "description": "Running ls -la /home/ubuntu/.agent-ml-research-idea_gen_0…",
  "usage": {
    "total_tokens": 24646,
    "tool_uses": 9,
    "duration_ms": 13973
  },
  "last_tool_name": "Bash",
  "uuid": "9340263f-4011-43ca-af73-a9d4b11d8f78",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3"
}
```

---


### Tool call

_source line 39_

<details open><summary>🔧 Tool call — Bash · `toolu_014gGv44TyXWr1wDSktFA4DR`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/scripts/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3",
  "uuid": "fd74e783-5b99-480f-929c-df50b9cb1dd3",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DKYruz3R5uMHDHD3y7SQ2s",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 1214,
      "cache_read_input_tokens": 23346,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1214,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 64,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 40 · 2026-05-23T18:55:04.419Z_

<details><summary>↩ Tool result · `toolu_014gGv44TyXWr1wDSktFA4DR`</summary>

```text
total 44
drwxr-xr-x  2 ubuntu ubuntu  4096 May 20 10:20 .
drwxr-xr-x 14 ubuntu ubuntu  4096 May 23 16:40 ..
-rw-r--r--  1 ubuntu ubuntu 10248 May 17 14:18 adalp_analysis.py
-rw-r--r--  1 ubuntu ubuntu 10816 May 18 06:02 dals_analysis.py
-rw-r--r--  1 ubuntu ubuntu 11045 May 20 10:20 j_calibration.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3",
  "uuid": "c85cb75b-5af4-4f6c-bf07-e800f021fe87"
}
```

</details>

---


### System

_source line 41_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac8ef46b1ece704fd",
  "tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "description": "Running find /home/ubuntu/.agent-ml-research-idea_gen_051…",
  "usage": {
    "total_tokens": 24901,
    "tool_uses": 10,
    "duration_ms": 15476
  },
  "last_tool_name": "Bash",
  "uuid": "eb0565e5-3dcd-4483-bf4f-6d88eed287f9",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3"
}
```

---


### Tool call

_source line 42_

<details open><summary>🔧 Tool call — Bash · `toolu_012ZhwWMPHh8Q3mUcL77wP2h`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie -name \"*.jsonl\" -type f | head -10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3",
  "uuid": "cf7b9ffc-52ca-4080-bdd6-d0ad21bbd564",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019sW9E3w3sd1vXnjyPqdSMz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 254,
      "cache_read_input_tokens": 24560,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 254,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 43 · 2026-05-23T18:55:05.936Z_

<details><summary>↩ Tool result · `toolu_012ZhwWMPHh8Q3mUcL77wP2h`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/ralph_loop_timeline.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/chats/worker_exp_e_theta_v1_logreg_20260520T154053.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/chats/worker_ssh_p0_5epoch_s456_recompute_and_progress_20260521T211909.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/chats/worker_code_exp_028_multigpu_switch_20260517T122517.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/chats/feishu_dm_oc_4206a99c0a8b5482c9bbd8f23ccc03f0_briefer.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/chats/worker_code_dgs_persistence_fix_20260518T164426.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/chats/worker_exp_010_selection_curves_20260514T144948.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/chats/cron_hook_exp_e2_pretrained_fewnerd.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/chats/cron_hook_exp_029b.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/chats/cron_hook_exp_conll_n16_s123.jsonl
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3",
  "uuid": "fc376c19-46b5-45e6-9522-2273ecdf3ad9"
}
```

</details>

---


### System

_source line 44_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac8ef46b1ece704fd",
  "tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "description": "Searching for samples\\.jsonl|compute.*f1|F1|majority.*vote|lp.b…",
  "usage": {
    "total_tokens": 25592,
    "tool_uses": 11,
    "duration_ms": 17825
  },
  "last_tool_name": "Grep",
  "uuid": "07f73d02-6244-4a3d-864b-c9020f676b7e",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3"
}
```

---


### Tool call

_source line 45_

<details open><summary>🔧 Tool call — Grep · `toolu_01CaPYZigBrPae2a4JjdJrBK`</summary>

```json
{
  "pattern": "samples\\.jsonl|compute.*f1|F1|majority.*vote|lp.best|lp.weighted",
  "type": "py",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "output_mode": "files_with_matches",
  "head_limit": 30
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3",
  "uuid": "ec76f20f-34c4-46d9-b456-0ac215b177da",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VNwequ15uezmei2NuX6XYr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 689,
      "cache_read_input_tokens": 24814,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 689,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### System

_source line 46_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac8ef46b1ece704fd",
  "tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "description": "Searching for inverse|transition",
  "usage": {
    "total_tokens": 25593,
    "tool_uses": 12,
    "duration_ms": 18194
  },
  "last_tool_name": "Grep",
  "uuid": "3101d03c-9de0-47dc-b44a-78f9c4494dfa",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3"
}
```

---


### Tool call

_source line 47_

<details open><summary>🔧 Tool call — Grep · `toolu_01CV6DgEDMHYpGmg2H2gEV9k`</summary>

```json
{
  "pattern": "inverse|transition",
  "type": "py",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "output_mode": "files_with_matches",
  "head_limit": 20
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3",
  "uuid": "9dd3a3f0-02dc-46a9-b11c-696c8f576b29",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VNwequ15uezmei2NuX6XYr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 689,
      "cache_read_input_tokens": 24814,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 689,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 48 · 2026-05-23T18:55:09.271Z_

<details><summary>↩ Tool result · `toolu_01CaPYZigBrPae2a4JjdJrBK`</summary>

```text
Found 30 files limit: 30
docs/paper/figures/_gen_n_scaling.py
docs/paper/figures/gen_fig_overview.py
artifacts/analyze_n32.py
artifacts/degeneracy_filter_construction.py
artifacts/parse_failure_bias_analysis.py
code/ner_lp_f1_correlation.py
artifacts/lp_best_unified.py
artifacts/lp_best_n_scaling.py
artifacts/lp_best_vs_cumlp_best.py
artifacts/e4_ensemble_scaling.py
artifacts/run_frontier_sc.py
artifacts/unify_degeneracy.py
artifacts/exp_multi_model_correlation/report/multi_model_error_correlation.py
artifacts/multi_model_error_correlation.py
artifacts/experiments/hidden_state_probe/extract_entity_hidden_states.py
artifacts/hidden_state_probe/intermediate/extract_entity_hidden_states.py
artifacts/experiments/hidden_state_probe/entity_probe_auroc.py
artifacts/hidden_state_probe/intermediate/entity_probe_auroc.py
artifacts/experiments/frontier_sc/run_frontier_sc.py
code/run_spider_sc.py
artifacts/experiments/spider_sql/run_spider_sc.py
artifacts/experiments/spider_sql/.venv/lib/python3.14/site-packages/bs4/dammit.py
artifacts/experiments/spider_sql/.venv/lib/python3.14/site-packages/huggingface_hub/utils/_safetensors.py
artifacts/experiments/spider_sql/.venv/lib/python3.14/site-packages/pandas/tests/util/test_hashing.py
artifacts/experiments/spider_sql/.venv/lib/python3.14/site-packages/pandas/tests/strings/test_strings.py
artifacts/experiments/spider_sql/.venv/lib/python3.14/site-packages/pandas/tests/io/parser/test_encoding.py
artifacts/experiments/spider_sql/.venv/lib/python3.14/site-packages/pandas/tests/io/excel/test_style.py
artifacts/experiments/spider_sql/.venv/lib/python3.14/site-packages/pandas/tests/frame/indexing/test_indexing.py
artifacts/experiments/spider_sql/.venv/lib/python3.14/site-packages/pandas/tests/apply/test_frame_apply.py
artifacts/experiments/spider_sql/.venv/lib/python3.14/site-packages/pandas/io/formats/style.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3",
  "uuid": "7a9eca75-a06d-469d-a72e-fa7a17f32b8b"
}
```

</details>

---


### Tool result

_source line 49 · 2026-05-23T18:55:09.276Z_

<details><summary>↩ Tool result · `toolu_01CV6DgEDMHYpGmg2H2gEV9k`</summary>

```text
Found 20 files limit: 20
artifacts/experiments/spider_sql/.venv/lib/python3.14/site-packages/bs4/element.py
artifacts/experiments/spider_sql/.venv/lib/python3.14/site-packages/bs4/dammit.py
artifacts/experiments/spider_sql/.venv/lib/python3.14/site-packages/soupsieve/css_parser.py
artifacts/experiments/spider_sql/.venv/lib/python3.14/site-packages/datasets/utils/stratify.py
artifacts/experiments/spider_sql/.venv/lib/python3.14/site-packages/datasets/features/features.py
artifacts/experiments/spider_sql/.venv/lib/python3.14/site-packages/pandas/tseries/frequencies.py
artifacts/experiments/spider_sql/.venv/lib/python3.14/site-packages/pandas/tests/tslibs/test_timezones.py
artifacts/experiments/spider_sql/.venv/lib/python3.14/site-packages/pandas/tests/tseries/offsets/test_offsets_properties.py
artifacts/experiments/spider_sql/.venv/lib/python3.14/site-packages/pandas/tests/tseries/offsets/test_dst.py
artifacts/experiments/spider_sql/.venv/lib/python3.14/site-packages/pandas/tests/tseries/frequencies/test_inference.py
artifacts/experiments/spider_sql/.venv/lib/python3.14/site-packages/pandas/tests/series/test_cumulative.py
artifacts/experiments/spider_sql/.venv/lib/python3.14/site-packages/pandas/tests/scalar/timestamp/methods/test_tz_localize.py
artifacts/experiments/spider_sql/.venv/lib/python3.14/site-packages/pandas/tests/scalar/timestamp/test_timestamp.py
artifacts/experiments/spider_sql/.venv/lib/python3.14/site-packages/pandas/tests/scalar/timestamp/test_arithmetic.py
artifacts/experiments/spider_sql/.venv/lib/python3.14/site-packages/pandas/tests/reshape/merge/test_merge.py
artifacts/experiments/spider_sql/.venv/lib/python3.14/site-packages/pandas/tests/reshape/concat/test_append_common.py
artifacts/experiments/spider_sql/.venv/lib/python3.14/site-packages/pandas/tests/resample/test_datetime_index.py
artifacts/experiments/spider_sql/.venv/lib/python3.14/site-packages/pandas/tests/io/pytables/test_timezones.py
artifacts/experiments/spider_sql/.venv/lib/python3.14/site-packages/pandas/tests/indexes/interval/test_interval_range.py
artifacts/experiments/spider_sql/.venv/lib/python3.14/site-packages/pandas/tests/indexes/datetimes/methods/test_tz_localize.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3",
  "uuid": "86bb070d-d482-444a-8979-8f58f61cdf59"
}
```

</details>

---


### System

_source line 50_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac8ef46b1ece704fd",
  "tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "description": "Reading artifacts/lp_best_n_scaling.py",
  "usage": {
    "total_tokens": 27356,
    "tool_uses": 13,
    "duration_ms": 20982
  },
  "last_tool_name": "Read",
  "uuid": "b873812b-4789-4e63-bd60-80250a8fbae7",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3"
}
```

---


### Tool call

_source line 51_

<details open><summary>🔧 Tool call — Read · `toolu_013ThLPX7gvbqdEcMcQFykse`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/lp_best_n_scaling.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3",
  "uuid": "efa0e961-cfd6-4f27-85b6-39621e9a8f39",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VqhpveSXnri9fqWwWSaTJT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 1756,
      "cache_read_input_tokens": 25503,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1756,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 52 · 2026-05-23T18:55:11.378Z_

<details><summary>↩ Tool result · `toolu_013ThLPX7gvbqdEcMcQFykse`</summary>

```text
1	"""Compute LP-best F1 vs Greedy F1 for N-scaling analysis (micro-average)."""
2	import json
3	import os
4	import sys
5	
6	DATA_ROOT = "/root/autodl-tmp/struct_self_consist_ie/output"
7	
8	CONFIGS = [
9	    ("SciERC", 8, "scierc_mf4v2_seed42", 42),
10	    ("SciERC", 16, "exp_001_seed42_v2", 42),
11	    ("SciERC", 32, "scierc_n32_s42", 42),
12	    ("SciERC", 64, "scierc_n64_seed42", 42),
13	    ("CoNLL", 8, "conll_mf4v2_seed123", 123),
14	    ("CoNLL", 16, "conll_n16_s456", 456),
15	    ("CoNLL", 32, "conll_n32_s42", 42),
16	    ("CoNLL", 64, "conll_n64_seed42", 42),
17	    ("FewNERD", 8, "fewnerd_mf4v2_seed42_v3", 42),
18	    ("FewNERD", 16, "fewnerd_n16_s42", 42),
19	]
20	
21	
22	def extract_entities(output_dict):
23	    return frozenset(
24	        (e["text"], e["type"], e["start"], e["end"])
25	        for e in output_dict.get("entities", [])
26	    )
27	
28	
29	def compute_micro_f1(results):
30	    total_tp = sum(r[0] for r in results)
31	    total_pred = sum(r[1] for r in results)
32	    total_gold = sum(r[2] for r in results)
33	    p = total_tp / total_pred if total_pred > 0 else 0
34	    r = total_tp / total_gold if total_gold > 0 else 0
35	    f1 = 2 * p * r / (p + r) if (p + r) > 0 else 0
36	    return f1, p, r, total_tp, total_pred, total_gold
37	
38	
39	def analyze_file(filepath, N_expected):
40	    with open(filepath) as f:
41	        instances = [json.loads(line) for line in f]
42	
43	    lp_best_results = []
44	    greedy_results = []
45	    n_gold_nonempty = 0
46	
47	    for inst in instances:
48	        gold_ents = extract_entities(inst["gold"])
49	        if len(gold_ents) == 0:
50	            continue
51	        n_gold_nonempty += 1
52	
53	        samples = inst["samples"]
54	        n_actual = min(len(samples), N_expected)
55	
56	        mean_lps = [s["mean_logprob"] for s in samples[:n_actual]]
57	        best_idx = max(range(n_actual), key=lambda i: mean_lps[i])
58	
59	        pred_lp = extract_entities(samples[best_idx])
60	        tp_lp = len(pred_lp & gold_ents)
61	        lp_best_results.append((tp_lp, len(pred_lp), len(gold_ents)))
62	
63	        pred_greedy = extract_entities(samples[0])
64	        tp_greedy = len(pred_greedy & gold_ents)
65	        greedy_results.append((tp_greedy, len(pred_greedy), len(gold_ents)))
66	
67	    lp_f1, lp_p, lp_r, _, _, _ = compute_micro_f1(lp_best_results)
68	    greedy_f1, gr_p, gr_r, _, _, _ = compute_micro_f1(greedy_results)
69	
70	    return {
71	        "lp_best_f1": lp_f1,
72	        "greedy_f1": greedy_f1,
73	        "delta_pp": (lp_f1 - greedy_f1) * 100,
74	        "n_instances": n_gold_nonempty,
75	        "lp_p": lp_p,
76	        "lp_r": lp_r,
77	    }
78	
79	
80	def main():
81	    header = f"{'Dataset':<10} {'N':>4} {'LP-best F1':>11} {'Greedy F1':>10} {'LP d (pp)':>10} {'instances':>10} {'seed':>5}"
82	    sep = "-" * 70
83	    print(header)
84	    print(sep)
85	
86	    results_lines = []
87	    for dataset, N, dirname, seed in CONFIGS:
88	        filepath = os.path.join(DATA_ROOT, dirname, "samples.jsonl")
89	        if not os.path.exists(filepath):
90	            line = f"{dataset:<10} {N:>4} {'MISSING':>11}"
91	            print(line)
92	            continue
93	        sys.stderr.write(f"Processing {dataset} N={N} ...\n")
94	        sys.stderr.flush()
95	        r = analyze_file(filepath, N)
96	        line = f"{dataset:<10} {N:>4} {r['lp_best_f1']*100:>10.2f}% {r['greedy_f1']*100:>9.2f}% {r['delta_pp']:>+9.2f} {r['n_instances']:>10} {seed:>5}"
97	        print(line)
98	        results_lines.append(line)
99	
100	    out_path = os.path.join(DATA_ROOT, "lp_best_n_scaling_results.txt")
101	    with open(out_path, "w") as f:
102	        f.write(header + "\n")
103	        f.write(sep + "\n")
104	        for line in results_lines:
105	            f.write(line + "\n")
106	        f.write("\nNotes:\n")
107	        f.write("- CoNLL N=8 uses seed123 (seed42 not available)\n")
108	        f.write("- CoNLL N=16 uses seed456 (seed42 not available)\n")
109	        f.write("- FewNERD N=32 not available\n")
110	        f.write("- Entity matching: 4-tuple (text, type, start, end)\n")
111	        f.write("- F1: micro-average over gold-nonempty instances\n")
112	        f.write("- LP-best: sample with highest mean_logprob\n")
113	    print(f"\nResults saved to {out_path}")
114	
115	
116	if __name__ == "__main__":
117	    main()
118	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3",
  "uuid": "9302885e-6588-406e-937d-85730b238dd6"
}
```

</details>

---


### System

_source line 53_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac8ef46b1ece704fd",
  "tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "description": "Reading artifacts/lp_best_unified.py",
  "usage": {
    "total_tokens": 27359,
    "tool_uses": 14,
    "duration_ms": 21191
  },
  "last_tool_name": "Read",
  "uuid": "a84e1885-2654-4ed2-b69f-1f707cb31e3e",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3"
}
```

---


### Tool call

_source line 54_

<details open><summary>🔧 Tool call — Read · `toolu_013VkYMBq7Dh1i6dwizm6tjK`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/lp_best_unified.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3",
  "uuid": "1110532e-8e6e-425e-976c-eb35046bb3dd",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VqhpveSXnri9fqWwWSaTJT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 1756,
      "cache_read_input_tokens": 25503,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1756,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 55 · 2026-05-23T18:55:11.581Z_

<details><summary>↩ Tool result · `toolu_013VkYMBq7Dh1i6dwizm6tjK`</summary>

```text
1	#!/usr/bin/env python3
2	"""Compute LP-best F1 on the unified instance set (same set as unified MV recompute).
3	
4	For each dataset:
5	- Find instance ID intersection across all N values
6	- Filter to gold-nonempty
7	- Use N=8 greedy as unified baseline (LP baseline = greedy F1)
8	- For each N: pick sample with highest mean_logprob, compute entity-level micro-F1
9	- LP Δ = LP-best F1 - LP baseline
10	"""
11	import json
12	import os
13	import sys
14	
15	DATA_ROOT = "/root/autodl-tmp/struct_self_consist_ie/output"
16	
17	DATASETS = {
18	    "SciERC": [
19	        (8,  "scierc_mf4v2_seed42"),
20	        (16, "exp_001_seed42_v2"),
21	        (32, "scierc_n32_s42"),
22	        (64, "scierc_n64_seed42"),
23	    ],
24	    "CoNLL": [
25	        (8,  "exp002_conll2003"),
26	        (16, "exp_002_conll_n16"),
27	        (32, "conll_n32_s42"),
28	        (64, "conll_n64_seed42"),
29	    ],
30	}
31	
32	
33	def extract_entities(d):
34	    return frozenset((e["text"], e["type"], e["start"], e["end"]) for e in d.get("entities", []))
35	
36	
37	def micro_f1(tp, fp, fn):
38	    if tp == 0:
39	        return 0.0
40	    p = tp / (tp + fp)
41	    r = tp / (tp + fn)
42	    return 2 * p * r / (p + r)
43	
44	
45	def load_instances(path):
46	    instances = {}
47	    with open(path) as f:
48	        for line in f:
49	            inst = json.loads(line)
50	            instances[inst["id"]] = inst
51	    return instances
52	
53	
54	def process_dataset(ds_name, configs):
55	    out_lines = []
56	    out_lines.append(f"\n{'='*70}")
57	    out_lines.append(f"Dataset: {ds_name}")
58	    out_lines.append(f"{'='*70}")
59	
60	    all_n = [n for n, _ in configs]
61	    instances_by_n = {}
62	    id_sets = []
63	
64	    for N, dirname in configs:
65	        path = os.path.join(DATA_ROOT, dirname, "samples.jsonl")
66	        if not os.path.exists(path):
67	            out_lines.append(f"  MISSING: {path}")
68	            return out_lines
69	        insts = load_instances(path)
70	        instances_by_n[N] = insts
71	        id_sets.append(set(insts.keys()))
72	        out_lines.append(f"  N={N}: {len(insts)} instances from output/{dirname}/samples.jsonl")
73	
74	    # Instance ID intersection
75	    common_ids = id_sets[0]
76	    for s in id_sets[1:]:
77	        common_ids = common_ids & s
78	    out_lines.append(f"\n  Instance ID intersection: {len(common_ids)}")
79	
80	    # Filter to gold-nonempty
81	    n8_insts = instances_by_n[all_n[0]]
82	    unified_ids = sorted([iid for iid in common_ids
83	                          if len(extract_entities(n8_insts[iid]["gold"])) > 0])
84	    out_lines.append(f"  Gold-nonempty intersection: {len(unified_ids)}")
85	
86	    # Greedy consistency check
87	    n_differ = 0
88	    for iid in unified_ids:
89	        greedy_sets = [extract_entities(instances_by_n[N][iid]["greedy"]) for N in all_n]
90	        if len(set(greedy_sets)) > 1:
91	            n_differ += 1
92	    out_lines.append(f"  Greedy consistency: {n_differ}/{len(unified_ids)} instances differ across N")
93	    out_lines.append(f"  Using greedy from N={all_n[0]} as unified baseline")
94	
95	    # LP baseline = greedy F1 on unified set (= LP-best with N=1)
96	    greedy_tp = greedy_fp = greedy_fn = 0
97	    for iid in unified_ids:
98	        gold = extract_entities(n8_insts[iid]["gold"])
99	        greedy = extract_entities(n8_insts[iid]["greedy"])
100	        tp = len(greedy & gold)
101	        greedy_tp += tp
102	        greedy_fp += len(greedy - gold)
103	        greedy_fn += len(gold - greedy)
104	    lp_baseline = micro_f1(greedy_tp, greedy_fp, greedy_fn)
105	
106	    out_lines.append(f"\n  LP baseline (greedy F1): {lp_baseline:.4f}")
107	
108	    # Per-N LP-best
109	    out_lines.append(f"\n     N | LP-best F1 | LP Δ(pp) |  #inst")
110	    out_lines.append(f"  -----+------------+----------+-------")
111	
112	    for N in all_n:
113	        lp_tp = lp_fp = lp_fn = 0
114	        for iid in unified_ids:
115	            inst = instances_by_n[N][iid]
116	            gold = extract_entities(inst["gold"])
117	            samples = inst["samples"][:N]
118	            best_idx = max(range(len(samples)), key=lambda i: samples[i]["mean_logprob"])
119	            pred = extract_entities(samples[best_idx])
120	            tp = len(pred & gold)
121	            lp_tp += tp
122	            lp_fp += len(pred - gold)
123	            lp_fn += len(gold - pred)
124	
125	        lp_f1 = micro_f1(lp_tp, lp_fp, lp_fn)
126	        delta = (lp_f1 - lp_baseline) * 100
127	        out_lines.append(f"  {N:>4} | {lp_f1:>10.4f} | {delta:>+7.2f}  | {len(unified_ids):>5}")
128	
129	    return out_lines
130	
131	
132	def main():
133	    all_output = []
134	    for ds_name, configs in DATASETS.items():
135	        print(f"  Processing {ds_name}...", file=sys.stderr, flush=True)
136	        lines = process_dataset(ds_name, configs)
137	        all_output.extend(lines)
138	
139	    text = "\n".join(all_output) + "\n"
140	    print(text)
141	
142	    out_path = os.path.join(DATA_ROOT, "unified_lp_best_results.txt")
143	    with open(out_path, "w") as f:
144	        f.write(text)
145	    print(f"Saved: {out_path}", file=sys.stderr)
146	
147	
148	if __name__ == "__main__":
149	    main()
150	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3",
  "uuid": "5e951d4b-2c20-48da-a45a-aacbc265d963"
}
```

</details>

---


### System

_source line 56_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac8ef46b1ece704fd",
  "tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "description": "Reading code/ner_lp_f1_correlation.py",
  "usage": {
    "total_tokens": 27362,
    "tool_uses": 15,
    "duration_ms": 21512
  },
  "last_tool_name": "Read",
  "uuid": "fd046b09-95d7-4aa5-af1f-80e7589e9b48",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3"
}
```

---


### Tool call

_source line 57_

<details open><summary>🔧 Tool call — Read · `toolu_01AD5izj6ba2ghWFkFWn1wbT`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/code/ner_lp_f1_correlation.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3",
  "uuid": "ab2db485-9ae2-4186-99f0-d94b02ecd609",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VqhpveSXnri9fqWwWSaTJT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 1756,
      "cache_read_input_tokens": 25503,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1756,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 58 · 2026-05-23T18:55:11.902Z_

<details><summary>↩ Tool result · `toolu_01AD5izj6ba2ghWFkFWn1wbT`</summary>

```text
1	"""
2	NER LP-F1 Spearman Correlation Analysis
3	Computes pooled and within-instance Spearman rho for NER finetuned N=8 data.
4	"""
5	import json
6	import sys
7	import numpy as np
8	from scipy.stats import spearmanr
9	
10	
11	def entity_set(entities):
12	    """Convert entity list to set of (text, type, start, end) tuples."""
13	    return {(e["text"], e["type"], e["start"], e["end"]) for e in entities}
14	
15	
16	def compute_f1(pred_entities, gold_entities):
17	    pred_set = entity_set(pred_entities)
18	    gold_set = entity_set(gold_entities)
19	    if len(pred_set) == 0 and len(gold_set) == 0:
20	        return 1.0
21	    if len(pred_set) == 0 or len(gold_set) == 0:
22	        return 0.0
23	    tp = len(pred_set & gold_set)
24	    precision = tp / len(pred_set)
25	    recall = tp / len(gold_set)
26	    if precision + recall == 0:
27	        return 0.0
28	    return 2 * precision * recall / (precision + recall)
29	
30	
31	def analyze(samples_path, dataset_name):
32	    with open(samples_path) as f:
33	        instances = [json.loads(line) for line in f]
34	
35	    all_logprobs = []
36	    all_f1s = []
37	    within_rhos = []
38	    n_total = 0
39	    n_zero_f1_instances = 0
40	
41	    for inst in instances:
42	        gold_ents = inst["gold"]["entities"]
43	        samples = inst["samples"]
44	        n_total += 1
45	
46	        inst_lps = []
47	        inst_f1s = []
48	        for s in samples:
49	            lp = s["mean_logprob"]
50	            f1 = compute_f1(s["entities"], gold_ents)
51	            inst_lps.append(lp)
52	            inst_f1s.append(f1)
53	            all_logprobs.append(lp)
54	            all_f1s.append(f1)
55	
56	        if all(f == 0.0 for f in inst_f1s):
57	            n_zero_f1_instances += 1
58	
59	        if np.std(inst_f1s) > 0:
60	            rho, _ = spearmanr(inst_lps, inst_f1s)
61	            if not np.isnan(rho):
62	                within_rhos.append(rho)
63	
64	    pooled_rho, pooled_p = spearmanr(all_logprobs, all_f1s)
65	    within_rho_mean = np.mean(within_rhos) if within_rhos else float("nan")
66	    zero_f1_pct = n_zero_f1_instances / n_total * 100
67	
68	    print(f"{dataset_name}:")
69	    print(f"  Pooled rho = {pooled_rho:.4f}, p = {pooled_p:.2e}, n_points = {len(all_logprobs)}")
70	    print(f"  Within-inst rho = {within_rho_mean:.4f}, n_valid = {len(within_rhos)} / {n_total}")
71	    print(f"  Zero-F1% = {zero_f1_pct:.1f}% ({n_zero_f1_instances}/{n_total})")
72	    print()
73	    return {
74	        "dataset": dataset_name,
75	        "pooled_rho": pooled_rho,
76	        "pooled_p": pooled_p,
77	        "within_rho": within_rho_mean,
78	        "n_valid": len(within_rhos),
79	        "n_total": n_total,
80	        "zero_f1_pct": zero_f1_pct,
81	        "n_zero_f1": n_zero_f1_instances,
82	    }
83	
84	
85	if __name__ == "__main__":
86	    base = "/root/autodl-tmp/struct_self_consist_ie/output"
87	    datasets = [
88	        (f"{base}/scierc_mf4v2_seed42/samples.jsonl", "SciERC"),
89	        (f"{base}/conll_mf4v2_seed42/samples.jsonl", "CoNLL"),
90	        (f"{base}/fewnerd_mf4v2_seed42_v3/samples.jsonl", "FewNERD"),
91	    ]
92	
93	    results = []
94	    for path, name in datasets:
95	        try:
96	            r = analyze(path, name)
97	            results.append(r)
98	        except FileNotFoundError:
99	            print(f"{name}: FILE NOT FOUND at {path}\n")
100	
101	    if results:
102	        print("=" * 72)
103	        print("NER LP-F1 Spearman rho (finetuned, N=8, seed=42)")
104	        print()
105	        print(f"| {'Dataset':<10} | {'Pooled rho':>10} | {'p-value':>10} | {'Within-inst rho':>15} | {'n_valid':>7} | {'Zero-F1%':>8} |")
106	        print(f"|{'-'*12}|{'-'*12}|{'-'*12}|{'-'*17}|{'-'*9}|{'-'*10}|")
107	        for r in results:
108	            print(f"| {r['dataset']:<10} | {r['pooled_rho']:>10.4f} | {r['pooled_p']:>10.2e} | {r['within_rho']:>15.4f} | {r['n_valid']:>7d} | {r['zero_f1_pct']:>7.1f}% |")
109	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3",
  "uuid": "de30e3a9-b990-4a57-865d-a8dae9d7d58e"
}
```

</details>

---


### System

_source line 59_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac8ef46b1ece704fd",
  "tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "description": "Running find /home/ubuntu/.agent-ml-research-idea_gen_051…",
  "usage": {
    "total_tokens": 33324,
    "tool_uses": 16,
    "duration_ms": 23525
  },
  "last_tool_name": "Bash",
  "uuid": "c4ef7e87-6c3b-4434-bb22-822c301ba0fb",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3"
}
```

---


### Tool call

_source line 60_

<details open><summary>🔧 Tool call — Bash · `toolu_01BjghU9JXAUvUULXd3aEag4`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie -type f -name \"*.py\" | grep -E \"(code|scripts|analysis|artifacts)\" | grep -v \".venv\" | grep -v \"__pycache__\" | sort"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3",
  "uuid": "92118b28-e3ab-4c7c-ae8d-ad94de38b57e",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0116kHRRKsFS26v32WnMqKPJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 5956,
      "cache_read_input_tokens": 27259,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5956,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 61 · 2026-05-23T18:55:14.125Z_

<details><summary>↩ Tool result · `toolu_01BjghU9JXAUvUULXd3aEag4`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/analysis_r21_q1_alignment.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/data/consistency.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/data/data_utils.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/data/evaluation.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/data/prepare_scd_data.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/data/run_mvp_pilot.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/data/sampling.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/intermediate/bootstrap_construction.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/intermediate/compute_signals.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/intermediate/consistency.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/intermediate/format_for_scaling.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/intermediate/sampling.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/a2_degen_regression/run_analysis.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/a4_pareto_diversity/plot_pareto.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/aggregate_seeds.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/analysis_dgs_epoch_rank.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/analyze_exp004_re_diagnostic.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/analyze_exp004_v2_re_diagnostic.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/analyze_exp005_v2_temperature.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/analyze_exp015_metrics_expansion.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/analyze_exp016_ensemble.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/analyze_n32.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/analyze_ood_signals.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/b1_scd_prep/eval_scd.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/b1_scd_prep/prepare_scd_data.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/b2_oof/b2_oof_evaluation.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/b2_v2_multi_domain/b2_v2_multi_domain.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/b2_v3_domain_invariant/b2_v3_domain_invariant.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/b2_v4_inverse_freq/b2_v4_inverse_freq.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/b5_cross_model/cross_model_construction.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/bootstrap_construction.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/bootstrap_selection_test.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/ccs_selection.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/compute_error_correlation.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/compute_signals.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/consistency.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/construction_variants.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/d140_oracle_gated_analysis.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/data_utils.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/deberta_verifier.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/deberta_verifier_5fold.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/degeneracy_filter_construction.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/e1v2_signal_routing/e1v2_signal_routing.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/e2_ensemble/run_e2_ensemble.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/e2v2_regime_weights/e2v2_regime_weights.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/e2v2_regime_weights/intermediate/e2v2_regime_weights.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/e4_ensemble_scaling.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/entity_construction.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/entity_construction_fair.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/evaluate_verifier.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/evaluation.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/exp-019/intermediate/train_verifier.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/exp-022/intermediate/analyze_3seed.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/exp001_postprocess.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/exp005_temperature/analyze_exp005_temperature.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/exp009_stratification_analysis.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/exp010_selection_curves/exp010_selection_curves.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/exp010_selection_curves/plot_selection_curves.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/exp_004_re_diagnostic/report/analyze_exp004_re_diagnostic.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/exp_009_capability_stratification/data/exp009_stratification_analysis.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/exp_009_v2_stratification.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/exp_015_metrics_expansion/intermediate/analyze_exp015_metrics_expansion.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/exp_016_signal_ensemble/intermediate/analyze_exp016_ensemble.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/exp_016_v2/data/exp_016_v2_ensemble.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/exp_016_v2_ensemble.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/exp_019_trained_verifier/train_verifier.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/exp_a2_humaneval_sc/intermediate/run_humaneval_sc.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/exp_a3_ace05_re/intermediate/prepare_re_data.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/exp_a3_ace05_re/intermediate/run_re_sc.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/exp_asb_adaptive_budget/data/run_asb.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/exp_b_frontier_sc_fewnerd/intermediate/run_frontier_sc.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/exp_backup3_distill_verifier/intermediate/run_distill_verifier.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/exp_dgec_heterogeneous_t/heterogeneous_t_construction.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/exp_dgec_vc_construction/vc_weighted_construction.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/exp_docred_re_sc/data/prepare_docred_data.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/exp_docred_re_sc/intermediate/run_docred_re_sc.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/exp_e1v2_signal_routing/data/e1v2_signal_routing.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/exp_lsc_latent_sc/data/run_lsc.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/exp_multi_model_correlation/report/multi_model_error_correlation.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/exp_spider_sc_pilot/intermediate/run_spider_sc.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/experiments/ace05_re/prepare_re_data.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/experiments/ace05_re/run_re_sc.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/experiments/asb/run_asb.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/experiments/distill_verifier/run_distill_verifier.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/experiments/docred_re/prepare_docred_data.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/experiments/docred_re/run_docred_re_sc.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/experiments/esj/run_esj.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/experiments/frontier_sc/run_frontier_sc.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/experiments/het_temp/run_het_temp.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/experiments/hidden_state_probe/entity_probe_auroc.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/experiments/hidden_state_probe/extract_entity_hidden_states.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/experiments/humaneval_sc/run_humaneval_sc.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/experiments/lsc/run_lsc.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/experiments/mrsc/run_mrsc.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/experiments/spider_sql/run_spider_sc.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/experiments/spider_sql/spider_databases/inn_1/change_date.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/figures/plot_all_figures.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/figures/plot_selection_gap_1024_v2.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/figures/plot_signal_heatmap_1024.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/format_for_scaling.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/ft_001/report/sampling.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/hidden_state_probe/extract_hidden_states.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/hidden_state_probe/extract_hidden_states_fewnerd.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/hidden_state_probe/hidden_state_probe.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/hidden_state_probe/hidden_state_probe_fewnerd.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/hidden_state_probe/intermediate/entity_probe_auroc.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/hidden_state_probe/intermediate/extract_entity_hidden_states.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/k_robustness/robustness_analysis.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/lp_alignment_gated_selection.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/lp_best_n_scaling.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/lp_best_unified.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/lp_best_vs_cumlp_best.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/multi_model_error_correlation.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/mvp_pilot.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/mvp_pilot_001/report/mvp_pilot.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/n8_bootstrap_ci.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/n_inverse_scaling/data_validation.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/n_inverse_scaling/run_analysis.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/p_impossibility/compute_bounds.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/parse_failure_bias_analysis.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/plot_length_logprob_scatter.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/plot_scaling_curve.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/r26_response/verify_citations.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/re_conditional_analysis.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/recompute_table_metrics.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/run_frontier_sc.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/run_lsc.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/run_mrsc.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/run_mvp_pilot.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/sampling.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/selective_prediction.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/token_lp_aggregator.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/train_supervised_verifier.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/unify_degeneracy.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/code/aggregate_scaling_results.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/code/analysis_mbr_selection.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/code/exp_b3_prompted_diversity.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/code/generate_scale_table.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/code/ner_lp_f1_correlation.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/code/plot_scaling_curve.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/code/run_spider_sc.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/code/theta_crit_sweep.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/code/zeroshot_prompts.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/scripts/adalp_analysis.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/scripts/dals_analysis.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/scripts/j_calibration.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3",
  "uuid": "e0779d8c-44a1-4797-a817-bdae1a62f68b"
}
```

</details>

---


### System

_source line 62_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac8ef46b1ece704fd",
  "tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "description": "Reading artifacts/n_inverse_scaling/run_analysis.py",
  "usage": {
    "total_tokens": 40010,
    "tool_uses": 17,
    "duration_ms": 25617
  },
  "last_tool_name": "Read",
  "uuid": "82dd7f61-d1e7-4393-b6ac-95b262676bfd",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3"
}
```

---


### Tool call

_source line 63_

<details open><summary>🔧 Tool call — Read · `toolu_014W6YKgGbBuAVZickoiuXGD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/n_inverse_scaling/run_analysis.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3",
  "uuid": "f3b7d965-bb79-4cfa-911c-ce5c6f2c2ff0",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011hjts53uLuC565Z1nfkN1k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 6679,
      "cache_read_input_tokens": 33215,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6679,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### System

_source line 64_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac8ef46b1ece704fd",
  "tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "description": "Reading code/aggregate_scaling_results.py",
  "usage": {
    "total_tokens": 40014,
    "tool_uses": 18,
    "duration_ms": 25718
  },
  "last_tool_name": "Read",
  "uuid": "454dab7a-b367-43e1-8d20-39db2c423dd3",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3"
}
```

---


### Tool call

_source line 65_

<details open><summary>🔧 Tool call — Read · `toolu_01FGUvvkK9nov5eWRVHHVhhu`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/code/aggregate_scaling_results.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3",
  "uuid": "b5116b4c-1992-4915-afc1-ee9efdb06e3f",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011hjts53uLuC565Z1nfkN1k",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 6679,
      "cache_read_input_tokens": 33215,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6679,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 66 · 2026-05-23T18:55:16.107Z_

<details><summary>↩ Tool result · `toolu_01FGUvvkK9nov5eWRVHHVhhu`</summary>

```text
1	#!/usr/bin/env python3
2	"""Aggregate scaling experiment results across model sizes into a unified table."""
3	
4	import argparse
5	import csv
6	import json
7	import os
8	import sys
9	from pathlib import Path
10	
11	
12	# Known data points (fill in as experiments complete)
13	KNOWN_RESULTS = [
14	    {
15	        "model": "Qwen3-4B",
16	        "family": "Qwen3",
17	        "size_b": 4,
18	        "dataset": "SciERC",
19	        "regime": "fine-tuned",
20	        "n_seeds": 1,
21	        "greedy_f1": 0.6622,
22	        "oracle_f1": 0.7925,
23	        "headroom_pp": 13.03,
24	        "degen_pct": 10.4,
25	        "lp_rho": None,
26	        "lp_delta_pp": None,
27	        "constr_delta_pp": None,
28	    },
29	    {
30	        "model": "Qwen3-8B",
31	        "family": "Qwen3",
32	        "size_b": 8,
33	        "dataset": "FewNERD",
34	        "regime": "fine-tuned",
35	        "n_seeds": 4,
36	        "greedy_f1": 0.7481,
37	        "oracle_f1": 0.8739,
38	        "headroom_pp": 12.58,
39	        "degen_pct": 12.69,
40	        "lp_rho": None,
41	        "lp_delta_pp": 1.38,
42	        "constr_delta_pp": None,
43	    },
44	    {
45	        "model": "LLaMA-3.1-8B",
46	        "family": "LLaMA",
47	        "size_b": 8,
48	        "dataset": "FewNERD",
49	        "regime": "fine-tuned",
50	        "n_seeds": 3,
51	        "greedy_f1": 0.7842,
52	        "oracle_f1": 0.8843,
53	        "headroom_pp": 10.01,
54	        "degen_pct": 23.36,
55	        "lp_rho": None,
56	        "lp_delta_pp": 0.36,
57	        "constr_delta_pp": None,
58	    },
59	    {
60	        "model": "Qwen2.5-72B",
61	        "family": "Qwen2.5",
62	        "size_b": 72,
63	        "dataset": "SciERC",
64	        "regime": "zero-shot",
65	        "n_seeds": 1,
66	        "greedy_f1": 0.399,
67	        "oracle_f1": 0.549,
68	        "headroom_pp": 15.0,
69	        "degen_pct": None,
70	        "lp_rho": None,
71	        "lp_delta_pp": None,
72	        "constr_delta_pp": None,
73	    },
74	    # === PLACEHOLDER: fill as experiments complete ===
75	    # {
76	    #     "model": "Qwen2.5-7B",
77	    #     "family": "Qwen2.5",
78	    #     "size_b": 7,
79	    #     "dataset": "FewNERD",
80	    #     "regime": "fine-tuned",
81	    #     ...
82	    # },
83	    # {
84	    #     "model": "Qwen2.5-14B",
85	    #     "family": "Qwen2.5",
86	    #     "size_b": 14,
87	    #     "dataset": "FewNERD",
88	    #     "regime": "fine-tuned",
89	    #     ...
90	    # },
91	    # {
92	    #     "model": "Qwen2.5-32B",
93	    #     "family": "Qwen2.5",
94	    #     "size_b": 32,
95	    #     "dataset": "FewNERD",
96	    #     "regime": "fine-tuned",
97	    #     ...
98	    # },
99	]
100	
101	METRIC_KEYS = [
102	    "model", "family", "size_b", "dataset", "regime", "n_seeds",
103	    "greedy_f1", "oracle_f1", "headroom_pp", "degen_pct",
104	    "lp_rho", "lp_delta_pp", "constr_delta_pp",
105	]
106	
107	
108	def load_from_unified_json(path: str) -> dict:
109	    """Extract scaling-relevant metrics from a unified result JSON file.
110	
111	    Expected format: {per_seed: {seedN: {...}}, summary: {...}}
112	    or flat format: {greedy_macro_f1: ..., oracle_macro_f1: ..., ...}
113	    """
114	    with open(path) as f:
115	        data = json.load(f)
116	
117	    if "summary" in data:
118	        s = data["summary"]
119	        greedy = s.get("greedy_macro_f1", {}).get("mean")
120	        oracle = s.get("oracle_macro_f1", {}).get("mean")
121	        degen = s.get("degeneracy_rate_pct", {}).get("mean")
122	        lp_rho = s.get("lp_spearman_global", {}).get("mean")
123	        lp_delta = s.get("lp_selection_delta_pp", {}).get("mean")
124	        n_seeds = len(data.get("per_seed", {}))
125	    else:
126	        greedy = data.get("greedy_macro_f1") or data.get("greedy_f1")
127	        oracle = data.get("oracle_macro_f1") or data.get("oracle_f1")
128	        degen = data.get("degeneracy_rate_pct") or data.get("degeneracy_rate")
129	        if degen and degen < 1:
130	            degen *= 100
131	        lp_rho = data.get("lp_spearman_global") or data.get("lp_rho")
132	        lp_delta = data.get("lp_selection_delta_pp") or data.get("lp_delta_pp")
133	        n_seeds = 1
134	
135	    headroom = (oracle - greedy) * 100 if greedy and oracle else None
136	
137	    return {
138	        "greedy_f1": greedy,
139	        "oracle_f1": oracle,
140	        "headroom_pp": round(headroom, 2) if headroom else None,
141	        "degen_pct": round(degen, 2) if degen else None,
142	        "lp_rho": round(lp_rho, 4) if lp_rho else None,
143	        "lp_delta_pp": round(lp_delta, 2) if lp_delta else None,
144	        "n_seeds": n_seeds,
145	    }
146	
147	
148	def aggregate(extra_json_paths: list[tuple[str, dict]] = None) -> list[dict]:
149	    """Merge KNOWN_RESULTS with any additional JSON result files.
150	
151	    extra_json_paths: list of (path, metadata_dict) where metadata_dict has
152	        keys: model, family, size_b, dataset, regime
153	    """
154	    results = list(KNOWN_RESULTS)
155	
156	    if extra_json_paths:
157	        for path, meta in extra_json_paths:
158	            if not os.path.exists(path):
159	                print(f"WARNING: {path} not found, skipping", file=sys.stderr)
160	                continue
161	            parsed = load_from_unified_json(path)
162	            row = {**meta, **parsed}
163	            row.setdefault("constr_delta_pp", None)
164	            results.append(row)
165	
166	    results.sort(key=lambda r: (r["dataset"], r["regime"], r["size_b"], r["family"]))
167	    return results
168	
169	
170	def print_table(results: list[dict]):
171	    header = f"{'Model':<16} {'Size':>5} {'Dataset':<8} {'Regime':<10} " \
172	             f"{'Greedy':>7} {'Oracle':>7} {'Head':>6} {'Degen%':>7} " \
173	             f"{'LP rho':>7} {'LP D':>6} {'C D':>6}"
174	    print(header)
175	    print("-" * len(header))
176	    for r in results:
177	        def fmt(v, w=7, d=4):
178	            return f"{v:{w}.{d}f}" if v is not None else " " * (w - 1) + "-"
179	        def fmt2(v, w=6, d=2):
180	            return f"{v:{w}.{d}f}" if v is not None else " " * (w - 1) + "-"
181	
182	        print(f"{r['model']:<16} {r['size_b']:>5} {r['dataset']:<8} {r['regime']:<10} "
183	              f"{fmt(r['greedy_f1'])} {fmt(r['oracle_f1'])} "
184	              f"{fmt2(r.get('headroom_pp'))} {fmt2(r.get('degen_pct'))} "
185	              f"{fmt(r.get('lp_rho'))} {fmt2(r.get('lp_delta_pp'))} "
186	              f"{fmt2(r.get('constr_delta_pp'))}")
187	
188	
189	def save_csv(results: list[dict], path: str):
190	    with open(path, "w", newline="") as f:
191	        w = csv.DictWriter(f, fieldnames=METRIC_KEYS, extrasaction="ignore")
192	        w.writeheader()
193	        w.writerows(results)
194	    print(f"Saved CSV: {path}")
195	
196	
197	def save_json(results: list[dict], path: str):
198	    with open(path, "w") as f:
199	        json.dump(results, f, indent=2)
200	    print(f"Saved JSON: {path}")
201	
202	
203	def main():
204	    parser = argparse.ArgumentParser(description="Aggregate scaling results")
205	    parser.add_argument("--extra", nargs="*", help="extra_path:model:family:size:dataset:regime")
206	    parser.add_argument("--out-csv", default=None)
207	    parser.add_argument("--out-json", default=None)
208	    args = parser.parse_args()
209	
210	    extra = []
211	    if args.extra:
212	        for spec in args.extra:
213	            parts = spec.split(":")
214	            if len(parts) != 6:
215	                print(f"ERROR: --extra format is path:model:family:size:dataset:regime, got {spec}",
216	                      file=sys.stderr)
217	                sys.exit(1)
218	            path, model, family, size, dataset, regime = parts
219	            extra.append((path, {
220	                "model": model, "family": family, "size_b": float(size),
221	                "dataset": dataset, "regime": regime,
222	            }))
223	
224	    results = aggregate(extra if extra else None)
225	    print_table(results)
226	
227	    if args.out_csv:
228	        save_csv(results, args.out_csv)
229	    if args.out_json:
230	        save_json(results, args.out_json)
231	
232	    default_dir = os.path.dirname(os.path.abspath(__file__))
233	    if not args.out_csv and not args.out_json:
234	        csv_path = os.path.join(default_dir, "scaling_results.csv")
235	        json_path = os.path.join(default_dir, "scaling_results.json")
236	        save_csv(results, csv_path)
237	        save_json(results, json_path)
238	
239	
240	if __name__ == "__main__":
241	    main()
242	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3",
  "uuid": "d61c1d37-3ac5-4b3b-8d32-040b4e894c8e"
}
```

</details>

---


### Tool result

_source line 67 · 2026-05-23T18:55:16.265Z_

<details><summary>↩ Tool result · `toolu_014W6YKgGbBuAVZickoiuXGD`</summary>

```text
1	#!/usr/bin/env python3
2	"""Inverse scaling test: check if F1 decreases as N increases for construction methods.
3	
4	For each dataset×model×method, sub-sample N=16 (or N=8) samples to N=2,4,6,8,(16),
5	compute entity-level micro F1, detect inverse scaling (F1 drop > 0.1pp),
6	and run paired bootstrap significance tests.
7	"""
8	
9	import json
10	import math
11	import os
12	import sys
13	import time
14	import numpy as np
15	from collections import defaultdict, Counter
16	
17	BASE = "/root/autodl-tmp/struct_self_consist_ie"
18	OUTPUT_DIR = f"{BASE}/artifacts/n_inverse_scaling"
19	
20	CONFIGS = {
21	    "Qwen_SciERC": {
22	        "path": f"{BASE}/output/exp_001_seed42_v2/samples.jsonl",
23	        "model": "Qwen3-8B-FT", "dataset": "SciERC",
24	    },
25	    "Qwen_CoNLL": {
26	        "path": f"{BASE}/output/exp_002_conll_n16/samples.jsonl",
27	        "model": "Qwen3-8B-FT", "dataset": "CoNLL",
28	    },
29	    "Qwen_FewNERD": {
30	        "path": f"{BASE}/output/exp_027_fewnerd_n16/samples.jsonl",
31	        "model": "Qwen3-8B-FT", "dataset": "FewNERD",
32	    },
33	    "LLaMA_SciERC": {
34	        "path": f"{BASE}/output/exp_007_llama_n16_r1024/samples.jsonl",
35	        "model": "LLaMA-3.1-8B-FT", "dataset": "SciERC",
36	    },
37	    "LLaMA_CoNLL": {
38	        "path": f"{BASE}/output/exp_017_llama_conll_n16/samples.jsonl",
39	        "model": "LLaMA-3.1-8B-FT", "dataset": "CoNLL",
40	    },
41	    "LLaMA_FewNERD": {
42	        "path": f"{BASE}/output/llama_fewnerd_s42/samples.jsonl",
43	        "model": "LLaMA-3.1-8B-FT", "dataset": "FewNERD",
44	    },
45	}
46	
47	METHODS = ["majority_vote", "lp_weighted", "vc_weighted", "sj_weighted", "theta2n", "uniform"]
48	
49	# ---- helpers ----
50	
51	def entity_set(entities):
52	    return {(e["start"], e["end"], e["type"]) for e in entities}
53	
54	def load_data(path, gold_filter=True):
55	    instances = []
56	    with open(path) as f:
57	        for line in f:
58	            if not line.strip():
59	                continue
60	            obj = json.loads(line)
61	            if gold_filter and not obj["gold"].get("entities", []):
62	                continue
63	            instances.append(obj)
64	    return instances
65	
66	# ---- weight functions ----
67	
68	def get_lp_weights(samples, inst):
69	    logprobs_list = inst.get("logprobs", None)
70	    lps = []
71	    for i, s in enumerate(samples):
72	        lp = s.get("mean_logprob", None)
73	        if lp is None and logprobs_list is not None and i < len(logprobs_list):
74	            lp = logprobs_list[i]
75	        if lp is None or not math.isfinite(lp):
76	            lp = -100.0
77	        lps.append(lp)
78	    max_lp = max(lps)
79	    ws = [math.exp(lp - max_lp) for lp in lps]
80	    total = sum(ws)
81	    if total == 0:
82	        return [1.0 / len(samples)] * len(samples)
83	    return [w / total for w in ws]
84	
85	def get_vc_weights(samples):
86	    N = len(samples)
87	    entity_counts = Counter()
88	    for s in samples:
89	        seen = set()
90	        for e in s.get("entities", []):
91	            key = (e["start"], e["end"], e["type"])
92	            if key not in seen:
93	                entity_counts[key] += 1
94	                seen.add(key)
95	    weights = []
96	    for s in samples:
97	        ents = set()
98	        for e in s.get("entities", []):
99	            ents.add((e["start"], e["end"], e["type"]))
100	        if ents:
101	            w = sum(entity_counts[k] for k in ents) / (N * len(ents))
102	        else:
103	            w = 1.0 / N
104	        weights.append(w)
105	    total = sum(weights)
106	    if total == 0:
107	        return [1.0 / N] * N
108	    return [w / total for w in weights]
109	
110	def get_sj_weights(samples):
111	    N = len(samples)
112	    sets = []
113	    for s in samples:
114	        es = frozenset((e["start"], e["end"], e["type"]) for e in s.get("entities", []))
115	        sets.append(es)
116	    weights = []
117	    for i in range(N):
118	        if N == 1:
119	            weights.append(1.0)
120	            continue
121	        total_j = 0.0
122	        for j in range(N):
123	            if j == i:
124	                continue
125	            a, b = sets[i], sets[j]
126	            if not a and not b:
127	                total_j += 1.0
128	            elif not a or not b:
129	                pass
130	            else:
131	                total_j += len(a & b) / len(a | b)
132	        weights.append(total_j / (N - 1))
133	    total = sum(weights)
134	    if total == 0:
135	        return [1.0 / N] * N
136	    return [w / total for w in weights]
137	
138	# ---- construction ----
139	
140	def weighted_construction(samples, threshold, weights=None):
141	    entity_counts = defaultdict(float)
142	    N = len(samples)
143	    for i, sample in enumerate(samples):
144	        w = weights[i] if weights is not None else 1.0
145	        seen = set()
146	        for e in sample.get("entities", []):
147	            key = (e["start"], e["end"], e["type"])
148	            if key not in seen:
149	                entity_counts[key] += w
150	                seen.add(key)
151	    total_weight = sum(weights) if weights is not None else N
152	    constructed = set()
153	    for key, count in entity_counts.items():
154	        if count / total_weight >= threshold:
155	            constructed.add(key)
156	    return constructed
157	
158	# ---- evaluation ----
159	
160	def evaluate_instance(inst, n, method):
161	    """Return (tp, fp, fn) for one instance at sample size n."""
162	    samples = inst["samples"][:n]
163	    gold = entity_set(inst["gold"]["entities"])
164	
165	    if method == "majority_vote":
166	        pred = weighted_construction(samples, threshold=0.5)
167	    elif method == "lp_weighted":
168	        ws = get_lp_weights(samples, inst)
169	        pred = weighted_construction(samples, threshold=2.0/n, weights=ws)
170	    elif method == "vc_weighted":
171	        ws = get_vc_weights(samples)
172	        pred = weighted_construction(samples, threshold=2.0/n, weights=ws)
173	    elif method == "sj_weighted":
174	        ws = get_sj_weights(samples)
175	        pred = weighted_construction(samples, threshold=2.0/n, weights=ws)
176	    elif method == "theta2n":
177	        pred = weighted_construction(samples, threshold=2.0/n)
178	    elif method == "uniform":
179	        pred = weighted_construction(samples, threshold=0.25)
180	    elif method == "greedy":
181	        pred = entity_set(inst["greedy"]["entities"])
182	    else:
183	        raise ValueError(f"Unknown: {method}")
184	
185	    tp = len(pred & gold)
186	    fp = len(pred - gold)
187	    fn = len(gold - pred)
188	    return tp, fp, fn
189	
190	def micro_f1_from_tuples(tuples):
191	    tp = sum(t[0] for t in tuples)
192	    fp = sum(t[1] for t in tuples)
193	    fn = sum(t[2] for t in tuples)
194	    if tp == 0:
195	        return 0.0
196	    p = tp / (tp + fp)
197	    r = tp / (tp + fn)
198	    return 2 * p * r / (p + r)
199	
200	def micro_prf_from_tuples(tuples):
201	    tp = sum(t[0] for t in tuples)
202	    fp = sum(t[1] for t in tuples)
203	    fn = sum(t[2] for t in tuples)
204	    if tp == 0:
205	        return 0.0, 0.0, 0.0
206	    p = tp / (tp + fp)
207	    r = tp / (tp + fn)
208	    f = 2 * p * r / (p + r)
209	    return p, r, f
210	
211	# ---- bootstrap ----
212	
213	def bootstrap_test(arr_n1, arr_n2, B=10000):
214	    """Paired bootstrap for micro F1 difference (n2 - n1)."""
215	    n = len(arr_n1)
216	    assert n == len(arr_n2)
217	
218	    a1 = np.array(arr_n1, dtype=np.int64)
219	    a2 = np.array(arr_n2, dtype=np.int64)
220	
221	    s1 = a1.sum(axis=0)
222	    s2 = a2.sum(axis=0)
223	    def _f1(s):
224	        tp, fp, fn = s[0], s[1], s[2]
225	        if tp == 0: return 0.0
226	        p = tp / (tp + fp); r = tp / (tp + fn)
227	        return 2*p*r/(p+r)
228	
229	    obs_diff = _f1(s2) - _f1(s1)
230	
231	    rng = np.random.RandomState(42)
232	    diffs = np.empty(B)
233	    for b in range(B):
234	        idx = rng.randint(0, n, size=n)
235	        bs1 = a1[idx].sum(axis=0)
236	        bs2 = a2[idx].sum(axis=0)
237	        diffs[b] = _f1(bs2) - _f1(bs1)
238	
239	    ci = (float(np.percentile(diffs, 2.5)), float(np.percentile(diffs, 97.5)))
240	    p_value = float(np.mean(diffs >= 0))  # H1: diff < 0 (inverse scaling)
241	    return {
242	        "obs_diff": float(obs_diff),
243	        "ci_95": ci,
244	        "p_value_inverse": p_value,  # small => significant inverse scaling
245	    }
246	
247	# ---- degeneracy ----
248	
249	def compute_degeneracy(instances, n):
250	    n_degen = 0
251	    for inst in instances:
252	        samples = inst["samples"][:n]
253	        esets = [frozenset((e["start"], e["end"], e["type"]) for e in s.get("entities", []))
254	                 for s in samples]
255	        if len(set(esets)) == 1:
256	            n_degen += 1
257	    return n_degen / len(instances)
258	
259	# ---- main ----
260	
261	def main():
262	    os.makedirs(OUTPUT_DIR, exist_ok=True)
263	
264	    f1_by_n = {}
265	    inverse_summary = {}
266	
267	    for cfg_name, cfg in CONFIGS.items():
268	        path = cfg["path"]
269	        if not os.path.exists(path):
270	            print(f"SKIP {cfg_name}: {path} not found", flush=True)
271	            continue
272	
273	        print(f"\n{'='*70}", flush=True)
274	        print(f"  {cfg_name}  ({cfg['model']} / {cfg['dataset']})", flush=True)
275	        print(f"{'='*70}", flush=True)
276	
277	        t0 = time.time()
278	        instances = load_data(path, gold_filter=True)
279	        max_n = len(instances[0]["samples"])
280	        print(f"  Loaded {len(instances)} instances, N_max={max_n}  ({time.time()-t0:.1f}s)", flush=True)
281	
282	        n_vals = sorted(set(n for n in [2, 4, 6, 8, 16] if n <= max_n))
283	
284	        # greedy baseline
285	        greedy_tuples = [evaluate_instance(inst, max_n, "greedy") for inst in instances]
286	        greedy_f1 = micro_f1_from_tuples(greedy_tuples)
287	        print(f"  Greedy F1: {greedy_f1:.4f}", flush=True)
288	
289	        # pre-compute all (method, n) -> list of (tp, fp, fn)
290	        precomputed = {}
291	        for method in METHODS:
292	            for n in n_vals:
293	                t1 = time.time()
294	                tuples = [evaluate_instance(inst, n, method) for inst in instances]
295	                f1 = micro_f1_from_tuples(tuples)
296	                p, r, _ = micro_prf_from_tuples(tuples)
297	                precomputed[(method, n)] = {"tuples": tuples, "f1": f1, "p": p, "r": r}
298	                elapsed = time.time() - t1
299	                if elapsed > 2:
300	                    print(f"    {method} N={n}: F1={f1:.4f} ({elapsed:.1f}s)", flush=True)
301	
302	        # build result structure
303	        config_result = {
304	            "model": cfg["model"], "dataset": cfg["dataset"],
305	            "n_instances": len(instances), "max_n": max_n,
306	            "greedy_f1": greedy_f1, "N_values": n_vals,
307	            "methods": {},
308	        }
309	
310	        # degeneracy
311	        degen = {}
312	        for n in n_vals:
313	            degen[str(n)] = compute_degeneracy(instances, n)
314	        config_result["degeneracy_by_n"] = degen
315	
316	        print(f"\n  {'Method':<18}", end="", flush=True)
317	        for n in n_vals:
318	            print(f"  N={n:>2}", end="", flush=True)
319	        print("  Behavior", flush=True)
320	        print(f"  {'-'*75}", flush=True)
321	
322	        for method in METHODS:
323	            f1_dict = {}
324	            prf_dict = {}
325	            for n in n_vals:
326	                d = precomputed[(method, n)]
327	                f1_dict[str(n)] = d["f1"]
328	                prf_dict[str(n)] = {"P": d["p"], "R": d["r"], "F1": d["f1"]}
329	
330	            # classify behavior
331	            f1_list = [f1_dict[str(n)] for n in n_vals]
332	            has_drop = any(f1_list[i] - f1_list[i+1] > 0.001 for i in range(len(f1_list)-1))
333	            is_plateau = all(abs(f1_list[i] - f1_list[i+1]) <= 0.001 for i in range(len(f1_list)-1))
334	            if has_drop:
335	                behavior = "inverse_scaling"
336	            elif is_plateau:
337	                behavior = "plateau"
338	            else:
339	                behavior = "monotonic_increasing"
340	
341	            config_result["methods"][method] = {
342	                "f1_by_n": f1_dict,
343	                "prf_by_n": prf_dict,
344	                "behavior": behavior,
345	            }
346	
347	            vals = "  ".join(f"{f1_dict[str(n)]:.4f}" for n in n_vals)
348	            marker = " <<<" if behavior == "inverse_scaling" else ""
349	            print(f"  {method:<18} {vals}  {behavior}{marker}", flush=True)
350	
351	        print(f"  {'Degeneracy':<18}", end="", flush=True)
352	        print("  ".join(f"{degen[str(n)]:.3f}" for n in n_vals), flush=True)
353	
354	        # detect inverse scaling cases and run bootstrap
355	        inverse_cases = []
356	        for method in METHODS:
357	            f1s = config_result["methods"][method]["f1_by_n"]
358	            for i in range(len(n_vals) - 1):
359	                n1, n2 = n_vals[i], n_vals[i+1]
360	                drop = f1s[str(n1)] - f1s[str(n2)]
361	                if drop > 0.001:
362	                    case = {
363	                        "method": method, "n1": n1, "n2": n2,
364	                        "f1_n1": f1s[str(n1)], "f1_n2": f1s[str(n2)],
365	                        "drop_pp": drop * 100,
366	                    }
367	                    # bootstrap
368	                    B = 5000 if len(instances) > 10000 else 10000
369	                    bt = bootstrap_test(
370	                        precomputed[(method, n1)]["tuples"],
371	                        precomputed[(method, n2)]["tuples"],
372	                        B=B,
373	                    )
374	                    case["bootstrap"] = bt
375	                    case["significant"] = bt["ci_95"][1] < 0  # entire CI below 0
376	                    inverse_cases.append(case)
377	
378	        if inverse_cases:
379	            print(f"\n  ** {len(inverse_cases)} INVERSE SCALING TRANSITION(S) **", flush=True)
380	            n_sig = sum(1 for c in inverse_cases if c["significant"])
381	            print(f"  {n_sig} significant (95% CI entirely below 0)", flush=True)
382	            for c in inverse_cases:
383	                sig = "SIG" if c["significant"] else "ns"
384	                ci = c["bootstrap"]["ci_95"]
385	                print(f"    {c['method']:<18} N={c['n1']}→{c['n2']}: "
386	                      f"{c['f1_n1']:.4f}→{c['f1_n2']:.4f} (↓{c['drop_pp']:.2f}pp)  "
387	                      f"CI=[{ci[0]*100:+.2f},{ci[1]*100:+.2f}]pp  {sig}", flush=True)
388	        else:
389	            print(f"\n  No inverse scaling transitions detected.", flush=True)
390	
391	        config_result["inverse_cases"] = inverse_cases
392	        f1_by_n[cfg_name] = config_result
393	
394	        inverse_summary[cfg_name] = {
395	            "model": cfg["model"], "dataset": cfg["dataset"],
396	            "n_instances": len(instances), "max_n": max_n,
397	            "greedy_f1": greedy_f1,
398	            "method_behaviors": {m: config_result["methods"][m]["behavior"] for m in METHODS},
399	            "n_inverse_transitions": len(inverse_cases),
400	            "n_significant": sum(1 for c in inverse_cases if c["significant"]),
401	            "inverse_cases": inverse_cases,
402	            "degeneracy_by_n": degen,
403	        }
404	
405	        print(f"  Total time: {time.time()-t0:.1f}s", flush=True)
406	
407	    # ---- save ----
408	    with open(os.path.join(OUTPUT_DIR, "f1_by_n.json"), "w") as f:
409	        # strip large tuples before saving
410	        save_data = {}
411	        for k, v in f1_by_n.items():
412	            sv = dict(v)
413	            for m in sv.get("methods", {}):
414	                sv["methods"][m] = {kk: vv for kk, vv in sv["methods"][m].items()}
415	            save_data[k] = sv
416	        json.dump(save_data, f, indent=2)
417	    print(f"\nSaved f1_by_n.json", flush=True)
418	
419	    with open(os.path.join(OUTPUT_DIR, "inverse_scaling_summary.json"), "w") as f:
420	        json.dump(inverse_summary, f, indent=2)
421	    print(f"Saved inverse_scaling_summary.json", flush=True)
422	
423	    # ---- summary stats ----
424	    total_configs = len(inverse_summary)
425	    total_transitions = sum(s["n_inverse_transitions"] for s in inverse_summary.values())
426	    total_sig = sum(s["n_significant"] for s in inverse_summary.values())
427	
428	    print(f"\n{'='*70}", flush=True)
429	    print(f"GLOBAL SUMMARY", flush=True)
430	    print(f"{'='*70}", flush=True)
431	    print(f"Configs analyzed: {total_configs}", flush=True)
432	    print(f"Total inverse scaling transitions: {total_transitions}", flush=True)
433	    print(f"Statistically significant: {total_sig}", flush=True)
434	
435	    # method-level summary
436	    method_inverse = {m: 0 for m in METHODS}
437	    method_sig = {m: 0 for m in METHODS}
438	    for s in inverse_summary.values():
439	        for c in s["inverse_cases"]:
440	            method_inverse[c["method"]] += 1
441	            if c["significant"]:
442	                method_sig[c["method"]] += 1
443	
444	    print(f"\nPer-method summary:", flush=True)
445	    print(f"  {'Method':<18} {'Inverse':>8} {'Signif':>8}", flush=True)
446	    for m in METHODS:
447	        print(f"  {m:<18} {method_inverse[m]:>8} {method_sig[m]:>8}", flush=True)
448	
449	    # ---- plot ----
450	    try:
451	        import matplotlib
452	        matplotlib.use("Agg")
453	        import matplotlib.pyplot as plt
454	
455	        fig, axes = plt.subplots(2, 3, figsize=(18, 10))
456	        fig.suptitle("F1 vs N by Construction Method", fontsize=14, fontweight="bold")
457	
458	        colors = {
459	            "majority_vote": "#e41a1c", "lp_weighted": "#377eb8",
460	            "vc_weighted": "#4daf4a", "sj_weighted": "#984ea3",
461	            "theta2n": "#ff7f00", "uniform": "#a65628",
462	        }
463	        markers = {
464	            "majority_vote": "o", "lp_weighted": "s",
465	            "vc_weighted": "D", "sj_weighted": "^",
466	            "theta2n": "v", "uniform": "P",
467	        }
468	
469	        config_order = ["Qwen_SciERC", "Qwen_CoNLL", "Qwen_FewNERD",
470	                        "LLaMA_SciERC", "LLaMA_CoNLL", "LLaMA_FewNERD"]
471	
472	        for idx, cfg_name in enumerate(config_order):
473	            ax = axes[idx // 3][idx % 3]
474	            if cfg_name not in f1_by_n:
475	                ax.set_title(f"{cfg_name} (no data)")
476	                continue
477	
478	            data = f1_by_n[cfg_name]
479	            n_vals = data["N_values"]
480	
481	            # greedy reference
482	            ax.axhline(y=data["greedy_f1"], color="gray", linestyle="--",
483	                       linewidth=1, alpha=0.7, label="greedy")
484	
485	            for method in METHODS:
486	                md = data["methods"][method]
487	                f1s = [md["f1_by_n"][str(n)] for n in n_vals]
488	                is_inv = md["behavior"] == "inverse_scaling"
489	                lw = 2.5 if is_inv else 1.5
490	                ax.plot(n_vals, f1s, color=colors[method], marker=markers[method],
491	                        linewidth=lw, markersize=6, label=method,
492	                        linestyle="-" if not is_inv else "-")
493	
494	                # mark inverse drops
495	                if is_inv:
496	                    for i in range(len(n_vals)-1):
497	                        if f1s[i] - f1s[i+1] > 0.001:
498	                            ax.annotate("", xy=(n_vals[i+1], f1s[i+1]),
499	                                        xytext=(n_vals[i], f1s[i]),
500	                                        arrowprops=dict(arrowstyle="->", color="red",
501	                                                       lw=2, alpha=0.6))
502	
503	            ax.set_title(f"{data['model']} / {data['dataset']}", fontsize=11)
504	            ax.set_xlabel("N (samples)")
505	            ax.set_ylabel("Entity Micro F1")
506	            ax.set_xticks(n_vals)
507	            ax.grid(True, alpha=0.3)
508	            ax.set_ylim(bottom=max(0, min(data["greedy_f1"] - 0.15,
509	                        min(md["f1_by_n"][str(n)] for m, md in data["methods"].items()
510	                            for n in n_vals if str(n) in md["f1_by_n"]) - 0.02)))
511	
512	        # shared legend
513	        handles, labels = axes[0][0].get_legend_handles_labels()
514	        fig.legend(handles, labels, loc="lower center", ncol=7, fontsize=9,
515	                   bbox_to_anchor=(0.5, -0.02))
516	        plt.tight_layout(rect=[0, 0.04, 1, 0.96])
517	        fig_path = os.path.join(OUTPUT_DIR, "f1_vs_n_all_configs.png")
518	        plt.savefig(fig_path, dpi=150, bbox_inches="tight")
519	        print(f"\nSaved plot: {fig_path}", flush=True)
520	        plt.close()
521	
522	        # detailed plot for inverse scaling cases only
523	        inv_configs = [k for k, v in inverse_summary.items() if v["n_inverse_transitions"] > 0]
524	        if inv_configs:
525	            n_inv = len(inv_configs)
526	            fig2, axes2 = plt.subplots(1, n_inv, figsize=(7*n_inv, 5))
527	            if n_inv == 1:
528	                axes2 = [axes2]
529	            fig2.suptitle("Inverse Scaling Cases (F1 vs N)", fontsize=13, fontweight="bold")
530	
531	            for i, cfg_name in enumerate(inv_configs):
532	                ax = axes2[i]
533	                data = f1_by_n[cfg_name]
534	                n_vals = data["N_values"]
535	
536	                ax.axhline(y=data["greedy_f1"], color="gray", linestyle="--",
537	                           linewidth=1, alpha=0.7, label="greedy")
538	
539	                inv_methods = set(c["method"] for c in data["inverse_cases"])
540	                for method in METHODS:
541	                    md = data["methods"][method]
542	                    f1s = [md["f1_by_n"][str(n)] for n in n_vals]
543	                    alpha = 1.0 if method in inv_methods else 0.3
544	                    lw = 2.5 if method in inv_methods else 1.0
545	                    ax.plot(n_vals, f1s, color=colors[method], marker=markers[method],
546	                            linewidth=lw, markersize=7 if method in inv_methods else 4,
547	                            label=method, alpha=alpha)
548	
549	                    if method in inv_methods:
550	                        for j in range(len(n_vals)-1):
551	                            if f1s[j] - f1s[j+1] > 0.001:
552	                                sig_cases = [c for c in data["inverse_cases"]
553	                                            if c["method"] == method and c["n1"] == n_vals[j]]
554	                                is_sig = any(c["significant"] for c in sig_cases)
555	                                marker_txt = f"↓{(f1s[j]-f1s[j+1])*100:.1f}pp"
556	                                if is_sig:
557	                                    marker_txt += "*"
558	                                mid_x = (n_vals[j] + n_vals[j+1]) / 2
559	                                mid_y = (f1s[j] + f1s[j+1]) / 2
560	                                ax.annotate(marker_txt, xy=(mid_x, mid_y),
561	                                           fontsize=8, color="red", fontweight="bold",
562	                                           ha="center", va="bottom")
563	
564	                ax.set_title(f"{data['model']} / {data['dataset']}", fontsize=11)
565	                ax.set_xlabel("N (samples)")
566	                ax.set_ylabel("Entity Micro F1")
567	                ax.set_xticks(n_vals)
568	                ax.grid(True, alpha=0.3)
569	                ax.legend(fontsize=8, loc="best")
570	
571	            plt.tight_layout()
572	            fig2_path = os.path.join(OUTPUT_DIR, "inverse_scaling_detail.png")
573	            plt.savefig(fig2_path, dpi=150, bbox_inches="tight")
574	            print(f"Saved detail plot: {fig2_path}", flush=True)
575	            plt.close()
576	
577	    except Exception as e:
578	        print(f"Plotting error (non-fatal): {e}", flush=True)
579	
580	    # ---- analysis.md ----
581	    lines = ["# Inverse Scaling Analysis for Structured Self-Consistency\n"]
582	    lines.append(f"Date: {time.strftime('%Y-%m-%d')}\n")
583	    lines.append("## Question\n")
584	    lines.append("Does increasing the number of samples N ever *decrease* entity-level F1 ")
585	    lines.append("for any construction method? If so, which methods and under what conditions?\n")
586	
587	    lines.append("\n## Setup\n")
588	    lines.append(f"- Configs: {total_configs} (2 models × 3 datasets)\n")
589	    lines.append(f"- Methods: {', '.join(METHODS)}\n")
590	    lines.append("- Threshold: majority_vote uses θ=0.5 (fixed); lp/vc/sj_weighted and theta2n use θ=2/N (adaptive); uniform uses θ=0.25 (fixed)\n")
591	    lines.append("- Metric: entity-level micro F1 (pooled TP/FP/FN)\n")
592	    lines.append("- Significance: paired bootstrap (B=5000-10000), 95% CI\n")
593	
594	    lines.append("\n## Results\n")
595	    if total_transitions == 0:
596	        lines.append("**No inverse scaling detected in any configuration.**\n")
597	        lines.append("All methods show monotonically increasing or plateau behavior as N grows.\n")
598	    else:
599	        lines.append(f"**{total_transitions} inverse scaling transitions detected, {total_sig} statistically significant.**\n")
600	        lines.append("\n### Inverse Scaling Cases\n")
601	        lines.append("| Config | Method | N₁→N₂ | F1(N₁) | F1(N₂) | Drop | 95% CI | Sig? |\n")
602	        lines.append("|--------|--------|--------|--------|--------|------|--------|------|\n")
603	        for cfg_name, s in inverse_summary.items():
604	            for c in s["inverse_cases"]:
605	                ci = c["bootstrap"]["ci_95"]
606	                sig = "**YES**" if c["significant"] else "no"
607	                lines.append(
608	                    f"| {cfg_name} | {c['method']} | {c['n1']}→{c['n2']} | "
609	                    f"{c['f1_n1']:.4f} | {c['f1_n2']:.4f} | "
610	                    f"{c['drop_pp']:.2f}pp | [{ci[0]*100:+.2f},{ci[1]*100:+.2f}] | {sig} |\n"
611	                )
612	
613	    lines.append("\n### Method Behavior Summary\n")
614	    lines.append("| Config | " + " | ".join(METHODS) + " |\n")
615	    lines.append("|--------" + "|--------" * len(METHODS) + "|\n")
616	    for cfg_name, s in inverse_summary.items():
617	        cells = []
618	        for m in METHODS:
619	            b = s["method_behaviors"][m]
620	            if b == "inverse_scaling":
621	                cells.append("**INVERSE**")
622	            elif b == "plateau":
623	                cells.append("plateau")
624	            else:
625	                cells.append("↑ mono")
626	        lines.append(f"| {cfg_name} | " + " | ".join(cells) + " |\n")
627	
628	    lines.append("\n### Degeneracy by N\n")
629	    lines.append("| Config |" + " | ".join(f"N={n}" for n in [2,4,6,8,16]) + " |\n")
630	    lines.append("|--------" + "|------" * 5 + "|\n")
631	    for cfg_name, s in inverse_summary.items():
632	        cells = []
633	        for n in [2,4,6,8,16]:
634	            d = s["degeneracy_by_n"].get(str(n), None)
635	            cells.append(f"{d:.1%}" if d is not None else "—")
636	        lines.append(f"| {cfg_name} | " + " | ".join(cells) + " |\n")
637	
638	    lines.append("\n## Mechanism Analysis\n")
639	    if total_transitions > 0:
640	        # check which methods show inverse scaling
641	        inv_methods = set()
642	        for s in inverse_summary.values():
643	            for c in s["inverse_cases"]:
644	                inv_methods.add(c["method"])
645	
646	        fixed_theta = inv_methods & {"majority_vote", "uniform"}
647	        adaptive_theta = inv_methods & {"lp_weighted", "vc_weighted", "sj_weighted", "theta2n"}
648	
649	        if fixed_theta and not adaptive_theta:
650	            lines.append("Inverse scaling occurs **only in fixed-threshold methods** (")
651	            lines.append(", ".join(sorted(fixed_theta)))
652	            lines.append("). Adaptive-threshold methods (θ=2/N) are immune.\n\n")
653	            lines.append("**Mechanism**: With fixed θ, the effective vote requirement scales with N. ")
654	            lines.append("At θ=0.5, an entity needs >N/2 votes. As N grows, correct-but-variable entities ")
655	            lines.append("fail to reach this threshold, causing recall degradation that outweighs ")
656	            lines.append("the precision benefits of additional samples.\n")
657	        elif adaptive_theta:
658	            lines.append("Inverse scaling occurs even in adaptive-threshold methods: ")
659	            lines.append(", ".join(sorted(adaptive_theta)))
660	            lines.append(". This suggests the issue goes beyond threshold choice.\n\n")
661	            lines.append("Possible mechanisms: (1) weight distortion at intermediate N; ")
662	            lines.append("(2) interaction between signal quality and N; ")
663	            lines.append("(3) boundary effects in entity aggregation.\n")
664	        else:
665	            lines.append("No clear pattern in affected methods.\n")
666	    else:
667	        lines.append("No inverse scaling detected. The construction methods are robust to increasing N.\n\n")
668	        lines.append("This is expected for adaptive-threshold methods (θ=2/N): as N grows, ")
669	        lines.append("the threshold decreases, compensating for any dilution of correct-but-rare entities. ")
670	        lines.append("For fixed-threshold methods (θ=0.5, θ=0.25), the monotonic increase suggests ")
671	        lines.append("that additional samples consistently improve the precision-recall tradeoff.\n")
672	
673	    lines.append("\n## Conclusion\n")
674	    if total_sig > 0:
675	        lines.append(f"We find {total_sig} statistically significant inverse scaling case(s). ")
676	        lines.append("This is the first reported inverse scaling finding in structured self-consistency. ")
677	        lines.append("The finding has implications for practitioners choosing aggregation methods ")
678	        lines.append("and sample budgets.\n")
679	    elif total_transitions > 0:
680	        lines.append(f"We observe {total_transitions} inverse scaling transition(s), but none ")
681	        lines.append("are statistically significant. The drops are within noise range.\n")
682	    else:
683	        lines.append("No inverse scaling is observed. Construction F1 monotonically increases ")
684	        lines.append("(or plateaus) with N across all tested configurations. ")
685	        lines.append("Structured self-consistency with entity-level construction is robust to sample budget.\n")
686	
687	    with open(os.path.join(OUTPUT_DIR, "analysis.md"), "w") as f:
688	        f.writelines(lines)
689	    print(f"Saved analysis.md", flush=True)
690	
691	    print("\nDONE", flush=True)
692	
693	
694	if __name__ == "__main__":
695	    main()
696	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3",
  "uuid": "9d66d756-90c8-4e9b-a558-c70be3f5df4a"
}
```

</details>

---


### System

_source line 68_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac8ef46b1ece704fd",
  "tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "description": "Reading scripts/adalp_analysis.py",
  "usage": {
    "total_tokens": 54576,
    "tool_uses": 19,
    "duration_ms": 28163
  },
  "last_tool_name": "Read",
  "uuid": "96c874d7-db47-46e0-b06e-dc4d98b3f771",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3"
}
```

---


### Tool call

_source line 69_

<details open><summary>🔧 Tool call — Read · `toolu_01UxtKxSaVybZGyMgKkfPduW`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/scripts/adalp_analysis.py",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3",
  "uuid": "324cac46-dd3a-44e6-b6d3-1ba2e01e1a0c",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015op6WH7dq2fc6f8f42fYhe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3430,
      "cache_creation_input_tokens": 11135,
      "cache_read_input_tokens": 39894,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11135,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 70 · 2026-05-23T18:55:18.553Z_

<details><summary>↩ Tool result · `toolu_01UxtKxSaVybZGyMgKkfPduW`</summary>

```text
1	"""
2	AdaLP (Adaptive LP Selection) Analysis.
3	Per-instance degeneracy decides greedy vs LP selection.
4	Leave-one-dataset-out CV for threshold selection.
5	"""
6	import json
7	import numpy as np
8	from collections import Counter
9	from pathlib import Path
10	
11	N = 8  # number of samples to use
12	
13	DATA_PATHS = {
14	    "SciERC": "output/exp_012_logprob/samples_with_logprobs.jsonl",
15	    "CoNLL": "output/exp_002_conll_n16/samples.jsonl",
16	    "FewNERD": "output/exp_027_fewnerd_n16/samples.jsonl",
17	}
18	
19	TAU_CANDIDATES = [0.25, 0.375, 0.5, 0.625, 0.75]
20	
21	
22	def compute_ner_f1(pred_entities, gold_entities):
23	    pred_set = {(e['text'], e['type'], e.get('start', -1), e.get('end', -1))
24	                for e in pred_entities}
25	    gold_set = {(e['text'], e['type'], e.get('start', -1), e.get('end', -1))
26	                for e in gold_entities}
27	    if not pred_set and not gold_set:
28	        return 1.0
29	    if not pred_set or not gold_set:
30	        return 0.0
31	    tp = len(pred_set & gold_set)
32	    prec = tp / len(pred_set)
33	    rec = tp / len(gold_set)
34	    if prec + rec == 0:
35	        return 0.0
36	    return 2 * prec * rec / (prec + rec)
37	
38	
39	def load_dataset(path):
40	    """Load dataset and compute per-instance metrics."""
41	    instances = []
42	    with open(path) as f:
43	        for line in f:
44	            d = json.loads(line)
45	            gold_ents = d['gold']['entities']
46	            samples = d['samples'][:N]
47	            greedy = d['greedy']
48	
49	            sample_f1s = [compute_ner_f1(s['entities'], gold_ents) for s in samples]
50	            sample_lps = [s['mean_logprob'] for s in samples]
51	            greedy_f1 = compute_ner_f1(greedy['entities'], gold_ents)
52	
53	            # LP selection: pick sample with highest mean_logprob
54	            lp_idx = int(np.argmax(sample_lps))
55	            lp_f1 = sample_f1s[lp_idx]
56	
57	            # Oracle: best F1 among samples
58	            oracle_f1 = max(sample_f1s)
59	
60	            # Degeneracy: max frequency of any F1 value / N
61	            f1_counts = Counter(sample_f1s)
62	            degen = max(f1_counts.values()) / len(sample_f1s)
63	
64	            instances.append({
65	                'id': d['id'],
66	                'sample_f1s': sample_f1s,
67	                'sample_lps': sample_lps,
68	                'greedy_f1': greedy_f1,
69	                'lp_f1': lp_f1,
70	                'oracle_f1': oracle_f1,
71	                'degen': degen,
72	            })
73	    return instances
74	
75	
76	def adalp_select(instances, tau):
77	    """Apply AdaLP: if degen > tau, use greedy; else use LP."""
78	    f1s = []
79	    for inst in instances:
80	        if inst['degen'] > tau:
81	            f1s.append(inst['greedy_f1'])
82	        else:
83	            f1s.append(inst['lp_f1'])
84	    return np.array(f1s)
85	
86	
87	def mean_f1(instances, key):
88	    return np.mean([inst[key] for inst in instances])
89	
90	
91	def paired_bootstrap(scores_a, scores_b, n_iter=1000, seed=42):
92	    """Paired bootstrap test. Returns delta, 95% CI, p-value."""
93	    rng = np.random.RandomState(seed)
94	    n = len(scores_a)
95	    observed_delta = np.mean(scores_a) - np.mean(scores_b)
96	    deltas = []
97	    for _ in range(n_iter):
98	        idx = rng.randint(0, n, size=n)
99	        deltas.append(np.mean(scores_a[idx]) - np.mean(scores_b[idx]))
100	    deltas = np.array(deltas)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3",
  "uuid": "66d24d49-c5cb-4ba0-9709-aad823fc5495"
}
```

</details>

---


### System

_source line 71_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac8ef46b1ece704fd",
  "tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "description": "Reading artifacts/evaluation.py",
  "usage": {
    "total_tokens": 54577,
    "tool_uses": 20,
    "duration_ms": 28438
  },
  "last_tool_name": "Read",
  "uuid": "fa0e8c5f-694e-4e9c-8b84-aeda31b553ae",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3"
}
```

---


### Tool call

_source line 72_

<details open><summary>🔧 Tool call — Read · `toolu_01HvafQ8JnVwxUBNFW95aE6E`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/evaluation.py",
  "limit": 80
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3",
  "uuid": "9b849bd5-e7af-4e5d-85b5-e484a5707c67",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015op6WH7dq2fc6f8f42fYhe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3430,
      "cache_creation_input_tokens": 11135,
      "cache_read_input_tokens": 39894,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 11135,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 73 · 2026-05-23T18:55:18.826Z_

<details><summary>↩ Tool result · `toolu_01HvafQ8JnVwxUBNFW95aE6E`</summary>

```text
1	"""Evaluation module for structured self-consistency IE experiments.
2	
3	Provides strict-match NER/EAE evaluation, per-instance F1 computation,
4	correlation analysis, and summary report generation.
5	"""
6	
7	from __future__ import annotations
8	
9	import statistics
10	from typing import Any
11	
12	from scipy.stats import kendalltau, spearmanr
13	
14	
15	# ---------------------------------------------------------------------------
16	# NER evaluation (strict match)
17	# ---------------------------------------------------------------------------
18	
19	def entity_strict_match(
20	    pred_entities: list[dict],
21	    gold_entities: list[dict],
22	) -> tuple[int, int, int]:
23	    """Compute strict entity match counts.
24	
25	    Strict match requires exact span (start, end) AND exact type.
26	
27	    Args:
28	        pred_entities: Predicted entity dicts with keys text, type, start, end.
29	        gold_entities: Gold entity dicts with the same schema.
30	
31	    Returns:
32	        (tp, fp, fn) counts.
33	    """
34	    pred_set = {(e["start"], e["end"], e["type"]) for e in pred_entities}
35	    gold_set = {(e["start"], e["end"], e["type"]) for e in gold_entities}
36	    tp = len(pred_set & gold_set)
37	    fp = len(pred_set - gold_set)
38	    fn = len(gold_set - pred_set)
39	    return tp, fp, fn
40	
41	
42	def compute_ner_f1(
43	    predictions: list[dict],
44	    golds: list[dict],
45	) -> dict[str, float]:
46	    """Compute micro-averaged NER precision, recall, and F1.
47	
48	    Args:
49	        predictions: List of Extraction dicts (one per instance).
50	        golds: List of Extraction dicts (one per instance), aligned with predictions.
51	
52	    Returns:
53	        Dict with keys "precision", "recall", "f1".
54	    """
55	    total_tp = total_fp = total_fn = 0
56	    for pred, gold in zip(predictions, golds):
57	        tp, fp, fn = entity_strict_match(
58	            pred.get("entities", []),
59	            gold.get("entities", []),
60	        )
61	        total_tp += tp
62	        total_fp += fp
63	        total_fn += fn
64	    return _prf(total_tp, total_fp, total_fn)
65	
66	
67	# ---------------------------------------------------------------------------
68	# EAE evaluation (argument match)
69	# ---------------------------------------------------------------------------
70	
71	def _event_argument_tuples(events: list[dict]) -> set[tuple]:
72	    """Extract (trigger_start, trigger_end, trigger_type, role, arg_start, arg_end) tuples."""
73	    tuples: set[tuple] = set()
74	    for event in events:
75	        trigger = event.get("trigger", {})
76	        t_start = trigger.get("start")
77	        t_end = trigger.get("end")
78	        t_type = trigger.get("type")
79	        for arg in event.get("arguments", []):
80	            tuples.add((t_start, t_end, t_type, arg["role"], arg["start"], arg["end"]))
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3",
  "uuid": "c8e0dca6-2935-4965-bf9d-2529a6f51710"
}
```

</details>

---


### System

_source line 74_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac8ef46b1ece704fd",
  "tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "description": "Reading artifacts/data_utils.py",
  "usage": {
    "total_tokens": 57084,
    "tool_uses": 21,
    "duration_ms": 30407
  },
  "last_tool_name": "Read",
  "uuid": "b7caf1b7-8be5-40ea-8c12-ca6273a42f52",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3"
}
```

---


### Tool call

_source line 75_

<details open><summary>🔧 Tool call — Read · `toolu_019rrBqkxatxERE83X29GQw4`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/data_utils.py",
  "limit": 80
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3",
  "uuid": "9e6c3f49-aee5-4f5c-9ed4-9486d3337775",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01ERQPokVFsA1QzW7bszkX8b",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 5929,
      "cache_read_input_tokens": 51029,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5929,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 76 · 2026-05-23T18:55:20.796Z_

<details><summary>↩ Tool result · `toolu_019rrBqkxatxERE83X29GQw4`</summary>

```text
1	"""Data processing utilities for structured self-consistency IE experiments.
2	
3	Handles loading, converting, and splitting datasets into the unified UIE JSON format.
4	Supported datasets: SciERC (fully implemented), ACE05 (interface only).
5	"""
6	
7	from __future__ import annotations
8	
9	import json
10	import os
11	import random
12	from typing import Any, TypedDict
13	
14	
15	# ---------------------------------------------------------------------------
16	# Shared type definitions (UIE JSON format)
17	# ---------------------------------------------------------------------------
18	
19	class Entity(TypedDict):
20	    text: str
21	    type: str
22	    start: int
23	    end: int
24	
25	
26	class Relation(TypedDict):
27	    head: str
28	    tail: str
29	    type: str
30	    head_start: int
31	    head_end: int
32	    tail_start: int
33	    tail_end: int
34	
35	
36	class EventArgument(TypedDict):
37	    text: str
38	    role: str
39	    start: int
40	    end: int
41	
42	
43	class Trigger(TypedDict):
44	    text: str
45	    type: str
46	    start: int
47	    end: int
48	
49	
50	class Event(TypedDict):
51	    trigger: Trigger
52	    arguments: list[EventArgument]
53	
54	
55	class Extraction(TypedDict, total=False):
56	    entities: list[Entity]
57	    relations: list[Relation]
58	    events: list[Event]
59	
60	
61	class Instance(TypedDict, total=False):
62	    id: str
63	    text: str
64	    entities: list[Entity]
65	    relations: list[Relation]
66	    events: list[Event]
67	
68	
69	# ---------------------------------------------------------------------------
70	# SciERC
71	# ---------------------------------------------------------------------------
72	
73	def _token_offsets(tokens: list[str]) -> list[tuple[int, int]]:
74	    """Compute (char_start, char_end) for each token when joined by single spaces."""
75	    offsets = []
76	    pos = 0
77	    for tok in tokens:
78	        offsets.append((pos, pos + len(tok)))
79	        pos += len(tok) + 1  # +1 for the space
80	    return offsets
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3",
  "uuid": "524cc44a-4c40-4387-8e30-8c5fad6dd7d3"
}
```

</details>

---


### System

_source line 77_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac8ef46b1ece704fd",
  "tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "description": "Reading artifacts/construction_variants.py",
  "usage": {
    "total_tokens": 57085,
    "tool_uses": 22,
    "duration_ms": 30685
  },
  "last_tool_name": "Read",
  "uuid": "7fe84c95-862e-4da6-aa66-ae614900c8b9",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3"
}
```

---


### Tool call

_source line 78_

<details open><summary>🔧 Tool call — Read · `toolu_01VatfzqYqPSUFcVud3upPkP`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/construction_variants.py",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3",
  "uuid": "2ac3d3c7-3225-458e-81b4-ec8849340d81",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01ERQPokVFsA1QzW7bszkX8b",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 5929,
      "cache_read_input_tokens": 51029,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5929,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 79 · 2026-05-23T18:55:21.078Z_

<details><summary>↩ Tool result · `toolu_01VatfzqYqPSUFcVud3upPkP`</summary>

```text
1	#!/usr/bin/env python3
2	"""Compute VC-weighted and SJ-weighted construction variants.
3	
4	Compares 4 construction methods at theta=2/N:
5	  - Greedy (baseline)
6	  - LP-weighted construction (existing)
7	  - VC-weighted construction (new)
8	  - SJ-weighted construction (new)
9	
10	With 3-seed mean and paired bootstrap significance tests (B=10000).
11	"""
12	
13	import json
14	import math
15	import os
16	import numpy as np
17	from collections import defaultdict, Counter
18	
19	BASE = "/root/autodl-tmp/struct_self_consist_ie"
20	
21	SEED_FILES = {
22	    "fewnerd": {
23	        42: f"{BASE}/output/llama_fewnerd_s42/samples.jsonl",
24	        123: f"{BASE}/output/llama_fewnerd_s123/samples.jsonl",
25	        456: f"{BASE}/output/llama_fewnerd_s456/samples.jsonl",
26	    },
27	    "scierc": {
28	        42: f"{BASE}/output/exp_018_llama_scierc_seed42_r1024/samples.jsonl",
29	        123: f"{BASE}/output/exp_018_llama_scierc_seed123/samples.jsonl",
30	        456: f"{BASE}/output/exp_018_llama_scierc_seed456/samples.jsonl",
31	    },
32	}
33	
34	OUTPUT_DIR = f"{BASE}/output/construction_variants"
35	
36	
37	# ---------------------------------------------------------------------------
38	# Core metrics
39	# ---------------------------------------------------------------------------
40	
41	def entity_set(entities):
42	    return {(e["start"], e["end"], e["type"]) for e in entities}
43	
44	
45	def compute_f1(pred_set, gold_set):
46	    if not gold_set and not pred_set:
47	        return 1.0
48	    if not pred_set or not gold_set:
49	        return 0.0
50	    tp = len(pred_set & gold_set)
51	    if tp == 0:
52	        return 0.0
53	    p = tp / len(pred_set)
54	    r = tp / len(gold_set)
55	    return 2 * p * r / (p + r)
56	
57	
58	# ---------------------------------------------------------------------------
59	# Weight computation
60	# ---------------------------------------------------------------------------
61	
62	def get_lp_weights(inst):
63	    """Softmax over mean log-probs -> per-sample weights."""
64	    samples = inst["samples"]
65	    logprobs = inst.get("logprobs", None)
66	    lps = []
67	    for i, s in enumerate(samples):
68	        lp = s.get("mean_logprob", None)
69	        if lp is None and logprobs is not None and i < len(logprobs):
70	            lp = logprobs[i]
71	        if lp is None or not math.isfinite(lp):
72	            lp = -100.0
73	        lps.append(lp)
74	    max_lp = max(lps)
75	    ws = [math.exp(lp - max_lp) for lp in lps]
76	    total = sum(ws)
77	    return [w / total for w in ws]
78	
79	
80	def get_vc_weights(inst):
81	    """Per-sample weight = mean vote fraction of its entities."""
82	    samples = inst["samples"]
83	    N = len(samples)
84	
85	    # Count entity occurrences across all samples
86	    entity_counts = Counter()
87	    for s in samples:
88	        seen = set()
89	        for e in s.get("entities", []):
90	            key = (e["start"], e["end"], e["type"])
91	            if key not in seen:
92	                entity_counts[key] += 1
93	                seen.add(key)
94	
95	    # Per-sample weight = mean(count/N) of its entities
96	    weights = []
97	    for s in samples:
98	        ents = set()
99	        for e in s.get("entities", []):
100	            ents.add((e["start"], e["end"], e["type"]))
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3",
  "uuid": "c7806ce1-a196-47c6-ad07-9d90c8a29447"
}
```

</details>

---


### System

_source line 80_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac8ef46b1ece704fd",
  "tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "description": "Running find /home/ubuntu/.agent-ml-research-idea_gen_051…",
  "usage": {
    "total_tokens": 59162,
    "tool_uses": 23,
    "duration_ms": 33687
  },
  "last_tool_name": "Bash",
  "uuid": "f022af71-a6ce-495e-8aa3-0babe73439fd",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3"
}
```

---


### Tool call

_source line 81_

<details open><summary>🔧 Tool call — Bash · `toolu_01PXu3Pf29dqpRjXP5PBfFud`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie -maxdepth 2 -name \"*.md\" -type f | grep -v \".venv\" | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3",
  "uuid": "5f4dc538-2c4c-4b9e-aed0-e887a811e875",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011CRZB1Tg55bM61gqMvk9H6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 2075,
      "cache_read_input_tokens": 56958,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2075,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### System

_source line 82_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac8ef46b1ece704fd",
  "tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "description": "Running head -50 /home/ubuntu/.agent-ml-research-idea_gen…",
  "usage": {
    "total_tokens": 59163,
    "tool_uses": 24,
    "duration_ms": 33738
  },
  "last_tool_name": "Bash",
  "uuid": "d970397d-3cca-4d0d-bf25-4a2ae904d16d",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3"
}
```

---


### Tool call

_source line 83_

<details open><summary>🔧 Tool call — Bash · `toolu_01YSfXaChDgi6W9NVwc4KND4`</summary>

```json
{
  "command": "head -50 /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3",
  "uuid": "42429771-bc09-4a2b-9b73-17c39906ab2a",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011CRZB1Tg55bM61gqMvk9H6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 2075,
      "cache_read_input_tokens": 56958,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2075,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 84 · 2026-05-23T18:55:24.163Z_

<details><summary>↩ Tool result · `toolu_01PXu3Pf29dqpRjXP5PBfFud`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/IDEA_BRIEF.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/task_context/agent.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/task_context/director.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/task_context/reviewer.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/memory.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/report.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/AGENTS.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/CLAUDE.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/fewnerd_per_type_mv_analysis.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/scaling_version_analysis.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/logprob_tie_analysis.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/round8_analysis_data_summary.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/qwen3_thinking_confirmation.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/claim_audit_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/report_gpu_status_20260521.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/rho_consistency_audit.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/d220_correction_notes.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/d072_paper_patch_inventory.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/p0_data_verification_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/r42_response_letter.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3",
  "uuid": "544aeb3c-1638-454d-b44b-5021b0260874"
}
```

</details>

---


### Tool result

_source line 85 · 2026-05-23T18:55:24.185Z_

<details><summary>↩ Tool result · `toolu_01YSfXaChDgi6W9NVwc4KND4`</summary>

```text
# Paper Framing — struct_self_consist_ie

> Updated 2026-05-22 — **D237 FRAMING OVERHAUL**: dataset-dependent optimal aggregation strategy + diagnostic cascade as primary contribution. N-scaling unified data (N=8/16/32/64) confirms MV gains are monotonically increasing but universally <1pp. LP-best saturates at N=8. Optimal strategy is dataset-dependent: LP dominates on FewNERD (+8pp), MV dominates on CoNLL (+0.61pp vs LP -2.34pp), SciERC approximately neutral.

## Target Venue
- Primary: EMNLP 2026 **Main Conference** (via ARR May 2026)
- Deadline: ARR May cycle, 2026-05-25

## Core Claims (D237 — TRIPLE CONTRIBUTION: QE + diagnostic + prescriptive)

### Claim 1 (PRIMARY — QE Framework + Selection Diagnostic)
**Positive contribution (A)**: Confidence signals reliably predict structured IE output quality at the population level (AUROC up to 0.82, ρ up to 0.45), enabling practical QE/selective prediction.

**Diagnostic contribution (B)** (D237 revised): The optimal aggregation strategy is **dataset-dependent**, determined by a four-stage diagnostic cascade:
1. **Instance degeneracy** (21-58% of instances produce identical F1 across N samples)
2. **LP compression** (within-instance LP range median 0.041 nats)
3. **LP-F1 alignment** (primary cross-dataset predictor: FewNERD ρ~0.5-0.7 → LP works; SciERC ρ~0.2 → LP fails; cross-dataset degeneracy-LP ρ=0.052, p=0.81)
4. **Structural signal limitation** (4/5 signals are instance-level aggregates → cannot rank candidates by construction)

**N-scaling evidence** (unified baseline, N=8/16/32/64, seed=42):
- SciERC: MV Δ = -1.24/-0.61/+0.24/+0.53 (monotonic ↑, crosses ~N=28, 3-seed mean ≈0 at N=32)
- CoNLL: MV Δ = +0.20/+0.32/+0.44/+0.61 (always positive, always <1pp)
- FewNERD: MV Δ = -2.71/-1.65/TBD (N=32 pending, strongly negative)
- LP-best saturates at N=8 (SciERC: 66.5→67.1% across N=8-64, Δ<0.6pp)

**Dataset-dependent optimal strategy**:
| Dataset | LP-best@N=8 vs greedy | MV@N=64 vs greedy | Winner |
|---------|----------------------|-------------------|--------|
| FewNERD | +8pp | negative | LP >> MV |
| SciERC | -0.32pp (N=8) / +0.29pp (N=64) | +0.53pp | ~tied |
| CoNLL | -1.42pp (N=8) / -2.34pp (N=64) | +0.61pp | MV >> LP |

**Core insight**: The diagnostic cascade predicts which method works where. On most datasets, gains <1pp regardless of method — the diagnostic framework itself is the primary contribution.

**Capability-diversity tension** (unifying insight): Model capability → output convergence → instance degeneracy → vanishing selection headroom. CoNLL (91% F1) → 58% degen; SciERC (66%) → 21%; FewNERD (79%) → 10%.

### Claim 2 (METHODOLOGY — QE Evaluation Framework)
Systematic evaluation of 5 confidence signals across 4 families for structured IE quality estimation. Task-dependent signal ranking: structural > probabilistic for NER, reversed for RE (binary-dominated F1 distributions). QE enables selective prediction: filtering 20% low-confidence instances yields +5-8pp F1 gain.

### Claim 3 (Diagnostic — task-complexity boundary)
RE task has 43-47% zero-F1 samples, creating binary-dominated signal distributions. LP's entire RE advantage is binary classification (cond ρ=0.011, n.s.). Task-dependent signal effectiveness is a novel characterization.

### Claim 4 (Prescriptive — Entity-Level Construction)
Entity-level construction (aggregate entities across N samples via MV): SciERC +1.02pp, FewNERD +1.40pp, CoNLL +0.10pp (n.s.). LP-weighted construction for 72B zero-shot: SciERC +1.53pp. Effectiveness is headroom-dependent.

## Story Spine

**Problem**: Test-time scaling via multi-sample generation improves LLM reasoning, but its effectiveness for structured IE is unclear.

**Gap**: Self-consistency and MBR succeed for discrete-answer reasoning via majority vote. Structured IE outputs (entity sets, relation triples) present fundamentally different challenges — prior work applies instance-level selection, which is the wrong analogy for set-structured outputs.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3",
  "uuid": "0afb6699-5093-4a8b-ab92-4f1b790477ee"
}
```

</details>

---


### System

_source line 86_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac8ef46b1ece704fd",
  "tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "description": "Running find /home/ubuntu/.agent-ml-research-idea_gen_051…",
  "usage": {
    "total_tokens": 61503,
    "tool_uses": 25,
    "duration_ms": 36151
  },
  "last_tool_name": "Bash",
  "uuid": "941a4698-7b57-4cca-943e-a96e3c944579",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3"
}
```

---


### Tool call

_source line 87_

<details open><summary>🔧 Tool call — Bash · `toolu_01GxukF3LVsJ3mdKEckPSndS`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie -name \"samples.jsonl\" -type f 2>/dev/null | head -3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3",
  "uuid": "06389490-bfd8-4b2d-9daa-3198a92bd655",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017qidQ2SSjFawEQdHB5etbv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 2338,
      "cache_read_input_tokens": 59033,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2338,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 88 · 2026-05-23T18:55:26.701Z_

<details><summary>↩ Tool result · `toolu_01GxukF3LVsJ3mdKEckPSndS`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3",
  "uuid": "de3625a9-895e-4931-859a-94fecf498699"
}
```

</details>

---


### System

_source line 89_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac8ef46b1ece704fd",
  "tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "description": "Running head -1 /home/ubuntu/.agent-ml-research-idea_gen_…",
  "usage": {
    "total_tokens": 61504,
    "tool_uses": 26,
    "duration_ms": 36586
  },
  "last_tool_name": "Bash",
  "uuid": "33c7ea19-ac4f-44d4-927c-84d4ab2aa538",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3"
}
```

---


### Tool call

_source line 90_

<details open><summary>🔧 Tool call — Bash · `toolu_014SJJvEtmThmocaKY4w5ccT`</summary>

```json
{
  "command": "head -1 /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/checkpoints/exp_001_seed42_v2/samples.jsonl 2>/dev/null | python3 -m json.tool 2>/dev/null | head -80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3",
  "uuid": "9506873e-7550-4dc1-9f26-ce23d87417fe",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017qidQ2SSjFawEQdHB5etbv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 2338,
      "cache_read_input_tokens": 59033,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2338,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 91 · 2026-05-23T18:55:27.091Z_

<details><summary>↩ Tool result · `toolu_014SJJvEtmThmocaKY4w5ccT`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3",
  "uuid": "4f2db179-d444-4c73-8d01-d5242ceee4f0"
}
```

</details>

---


### System

_source line 92_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac8ef46b1ece704fd",
  "tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "description": "Running ls /home/ubuntu/.agent-ml-research-idea_gen_0514_…",
  "usage": {
    "total_tokens": 61814,
    "tool_uses": 27,
    "duration_ms": 38948
  },
  "last_tool_name": "Bash",
  "uuid": "0b43148b-08e5-455c-9c0a-84a9125e8f49",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3"
}
```

---


### Tool call

_source line 93_

<details open><summary>🔧 Tool call — Bash · `toolu_01AqveAZT2YVEo8aZC4aLJCg`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/checkpoints/ | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3",
  "uuid": "0e767b6f-7647-4878-b5b7-560bed42c1ef",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01JSHVggXGyMonvEG8CmEbXp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 308,
      "cache_read_input_tokens": 61371,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 308,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 94 · 2026-05-23T18:55:29.387Z_

<details><summary>↩ Tool result · `toolu_01AqveAZT2YVEo8aZC4aLJCg`</summary>

```text
dgs_pilot_DONE_20260519T002937.json
dgs_pilot_PENDING_20260518T175604.json
dgs_pilot_PENDING_20260519T002926.json
e1_component_wise_re_sj_DONE_20260514T092226.json
e1_component_wise_re_sj_DONE_20260514T092332.json
e1_component_wise_re_sj_DONE_20260514T092336.json
e1_component_wise_re_sj_PENDING_20260514T092204.json
e1_component_wise_re_sj_PREPARING_20260514T091517.json
e1_component_wise_re_sj_QUEUED_20260514T092207.json
e1_component_wise_re_sj_RUNNING_20260514T092213.json
e1_component_wise_re_sj_RUNNING_20260514T092217.json
eval_scd_fewnerd_fallback_PREPARING_20260520T201556.json
eval_scd_fewnerd_fallback_PREPARING_20260521T235214.json
exp001_seed123_DONE_20260515T124131.json
exp001_seed123_PENDING_20260515T124118.json
exp001_seed123_PREPARING_20260514T134552.json
exp001_seed123_PREPARING_20260514T175148.json
exp001_seed123_PREPARING_20260514T215115.json
exp001_seed456_DONE_20260515T124132.json
exp001_seed456_PENDING_20260515T124119.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3",
  "uuid": "ea5cfbdb-fe00-49b1-9965-d9e1a6ea4239"
}
```

</details>

---


### System

_source line 95_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac8ef46b1ece704fd",
  "tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "description": "Running find /home/ubuntu/.agent-ml-research-idea_gen_051…",
  "usage": {
    "total_tokens": 61815,
    "tool_uses": 28,
    "duration_ms": 39132
  },
  "last_tool_name": "Bash",
  "uuid": "228fd1a6-f6e5-452f-86bf-9f239775f9bd",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3"
}
```

---


### Tool call

_source line 96_

<details open><summary>🔧 Tool call — Bash · `toolu_01ML7NMLFwYhBYxxqNq7jpdW`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie -maxdepth 3 -name \"samples.jsonl\" 2>/dev/null | head -5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3",
  "uuid": "dd1b2779-db92-46ed-ba17-20e05130f7b8",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01JSHVggXGyMonvEG8CmEbXp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 308,
      "cache_read_input_tokens": 61371,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 308,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 97 · 2026-05-23T18:55:29.596Z_

<details><summary>↩ Tool result · `toolu_01ML7NMLFwYhBYxxqNq7jpdW`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3",
  "uuid": "2e592475-a31d-49f4-aeea-a0f3dbef0d5f"
}
```

</details>

---


### System

_source line 98_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac8ef46b1ece704fd",
  "tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "description": "Running grep -r \"samples.jsonl\\|samples\\.jsonl\" /home/ubu…",
  "usage": {
    "total_tokens": 62493,
    "tool_uses": 29,
    "duration_ms": 41073
  },
  "last_tool_name": "Bash",
  "uuid": "120555aa-bd3f-4bdf-9f53-715991f6672b",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3"
}
```

---


### Tool call

_source line 99_

<details open><summary>🔧 Tool call — Bash · `toolu_01TbZcdcn7X5CzzvtRG7sBXi`</summary>

```json
{
  "command": "grep -r \"samples.jsonl\\|samples\\.jsonl\" /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/*.py | head -10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3",
  "uuid": "e9011c20-2695-4e4b-8377-e19a7580ddc9",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01YCA9WwC7bcwYauvLtRfmpM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 672,
      "cache_read_input_tokens": 61679,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 672,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 100 · 2026-05-23T18:55:31.514Z_

<details><summary>↩ Tool result · `toolu_01TbZcdcn7X5CzzvtRG7sBXi`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/analysis_dgs_epoch_rank.py:    ('/root/autodl-tmp/struct_self_consist_ie/output/exp_029a_scierc_3epoch/samples.jsonl', 'SciERC-3ep'),
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/analysis_dgs_epoch_rank.py:    ('/root/autodl-tmp/struct_self_consist_ie/output/exp_012_rerun_1024/samples.jsonl', 'SciERC-5ep'),
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/analysis_dgs_epoch_rank.py:    ('/root/autodl-tmp/struct_self_consist_ie/output/exp_029b_scierc_10epoch/samples.jsonl', 'SciERC-10ep'),
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/analysis_dgs_epoch_rank.py:    ('/root/autodl-tmp/struct_self_consist_ie/output/exp_023_rank8_inference/samples.jsonl', 'SciERC-rank8'),
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/analyze_exp004_re_diagnostic.py:CPU-only. Uses pilot_004 samples.jsonl.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/analyze_exp004_re_diagnostic.py:PILOT_004 = BASE / "output" / "mvp_pilot_004" / "samples.jsonl"
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/analyze_exp004_re_diagnostic.py:PILOT_005 = BASE / "output" / "mvp_pilot_005" / "samples.jsonl"
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/analyze_exp005_v2_temperature.py:PILOT_004 = os.path.join(BASE, "mvp_pilot_004/samples.jsonl")       # T=1.0
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/analyze_exp005_v2_temperature.py:PILOT_005 = os.path.join(BASE, "mvp_pilot_005/samples.jsonl")       # T=0.7
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/analyze_exp015_metrics_expansion.py:    samples_path = os.path.join(logprob_dir, "samples.jsonl")
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3",
  "uuid": "622daf69-6d44-4cc7-a4df-7fa919776ad3"
}
```

</details>

---


### System

_source line 101_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac8ef46b1ece704fd",
  "tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "description": "Running ls -lh /home/ubuntu/.agent-ml-research-idea_gen_0…",
  "usage": {
    "total_tokens": 62496,
    "tool_uses": 30,
    "duration_ms": 41163
  },
  "last_tool_name": "Bash",
  "uuid": "5152726d-0379-4d7d-a949-3089fa3c9aa1",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3"
}
```

---


### Tool call

_source line 102_

<details open><summary>🔧 Tool call — Bash · `toolu_011W5fCYLDBkTsbXtYgjfwUt`</summary>

```json
{
  "command": "ls -lh /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/*.py | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3",
  "uuid": "5cae942f-e5d5-47b9-9a0f-663fcbd02aad",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01YCA9WwC7bcwYauvLtRfmpM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 672,
      "cache_read_input_tokens": 61679,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 672,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 103 · 2026-05-23T18:55:31.618Z_

<details><summary>↩ Tool result · `toolu_011W5fCYLDBkTsbXtYgjfwUt`</summary>

```text
-rw-r--r-- 1 ubuntu ubuntu 9.7K May 20 04:38 /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/aggregate_seeds.py
-rw-r--r-- 1 ubuntu ubuntu 4.9K May 18 19:16 /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/analysis_dgs_epoch_rank.py
-rw-r--r-- 1 ubuntu ubuntu  26K May 14 11:49 /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/analyze_exp004_re_diagnostic.py
-rw-r--r-- 1 ubuntu ubuntu  21K May 14 15:24 /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/analyze_exp004_v2_re_diagnostic.py
-rw-r--r-- 1 ubuntu ubuntu  15K May 14 15:24 /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/analyze_exp005_v2_temperature.py
-rw-r--r-- 1 ubuntu ubuntu  22K May 14 11:47 /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/analyze_exp015_metrics_expansion.py
-rw-r--r-- 1 ubuntu ubuntu  31K May 14 12:14 /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/analyze_exp016_ensemble.py
-rw-r--r-- 1 ubuntu ubuntu  11K May 23 08:30 /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/analyze_n32.py
-rw-r--r-- 1 ubuntu ubuntu 8.9K May 15 11:41 /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/analyze_ood_signals.py
-rw-r--r-- 1 ubuntu ubuntu  13K May 19 18:25 /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/bootstrap_construction.py
-rw-r--r-- 1 ubuntu ubuntu 9.5K May 16 16:10 /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/bootstrap_selection_test.py
-rw-r--r-- 1 ubuntu ubuntu 8.9K May 18 17:35 /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/ccs_selection.py
-rw-r--r-- 1 ubuntu ubuntu 7.0K May 20 01:40 /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/compute_error_correlation.py
-rw-r--r-- 1 ubuntu ubuntu  17K May 19 18:27 /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/compute_signals.py
-rw-r--r-- 1 ubuntu ubuntu  13K May 14 05:50 /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/consistency.py
-rw-r--r-- 1 ubuntu ubuntu  12K May 19 22:33 /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/construction_variants.py
-rw-r--r-- 1 ubuntu ubuntu 7.9K May 18 13:05 /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/d140_oracle_gated_analysis.py
-rw-r--r-- 1 ubuntu ubuntu 8.9K May 14 04:26 /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/data_utils.py
-rw-r--r-- 1 ubuntu ubuntu  13K May 18 06:05 /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/deberta_verifier.py
-rw-r--r-- 1 ubuntu ubuntu  15K May 18 06:58 /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/deberta_verifier_5fold.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3",
  "uuid": "1ee86de6-f7ac-4e43-82b4-151a120e5e02"
}
```

</details>

---


### System

_source line 104_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac8ef46b1ece704fd",
  "tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "description": "Reading artifacts/analyze_n32.py",
  "usage": {
    "total_tokens": 64841,
    "tool_uses": 31,
    "duration_ms": 43386
  },
  "last_tool_name": "Read",
  "uuid": "33ce75e1-cf0d-4fce-a058-27f61c30f42f",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3"
}
```

---


### Tool call

_source line 105_

<details open><summary>🔧 Tool call — Read · `toolu_0132TeZHLrVLECzZnm3BqMAS`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/analyze_n32.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3",
  "uuid": "1f378a9c-7e99-4486-a0eb-7e135fb9c956",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Ao7kQmRBtVqfvuVaKdWDcC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 2343,
      "cache_read_input_tokens": 62351,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2343,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 106 · 2026-05-23T18:55:33.776Z_

<details><summary>↩ Tool result · `toolu_0132TeZHLrVLECzZnm3BqMAS`</summary>

```text
1	"""N-scaling analysis for pretrained FewNERD: N=8/16/32 comparison.
2	
3	Computes greedy F1, MV F1, LP-selection F1, oracle F1, degeneracy rate,
4	capture rate, and SJ rho on gold-nonempty instances (micro-averaged).
5	
6	Usage:
7	    python analyze_n32.py --input samples.jsonl [--n_samples 32] [--compute_sj]
8	"""
9	
10	import json
11	import argparse
12	import sys
13	import os
14	from collections import Counter
15	
16	import numpy as np
17	from scipy.stats import spearmanr
18	
19	sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
20	from unified_metrics import (
21	    compute_entity_f1, compute_sample_f1s,
22	    get_lp_selection_idx, bootstrap_delta_ci,
23	)
24	
25	# N=8 and N=16 pretrained FewNERD reference values (gold-nonempty, micro-avg)
26	REF = {
27	    8:  {"greedy": 0.538, "mv_delta": 3.9, "degen": 11.7, "oracle_delta": 11.2, "capture": 36, "sj_rho": 0.436},
28	    16: {"greedy": 0.537, "mv_delta": 4.1, "degen": 7.6,  "oracle_delta": 14.1, "capture": 29, "sj_rho": 0.453},
29	}
30	
31	
32	def load_gold_nonempty(path):
33	    instances = []
34	    with open(path) as f:
35	        for line in f:
36	            if not line.strip():
37	                continue
38	            obj = json.loads(line)
39	            if obj["gold"].get("entities", []):
40	                instances.append(obj)
41	    return instances
42	
43	
44	def entity_strict_counts(pred_entities, gold_entities):
45	    pred_set = {(e["start"], e["end"], e["type"]) for e in pred_entities}
46	    gold_set = {(e["start"], e["end"], e["type"]) for e in gold_entities}
47	    tp = len(pred_set & gold_set)
48	    return tp, len(pred_set) - tp, len(gold_set) - tp
49	
50	
51	def micro_f1(tp, fp, fn):
52	    p = tp / (tp + fp) if (tp + fp) > 0 else 0
53	    r = tp / (tp + fn) if (tp + fn) > 0 else 0
54	    return 2 * p * r / (p + r) if (p + r) > 0 else 0
55	
56	
57	def majority_vote_entities(samples, threshold_frac=0.5):
58	    """Strict MV: vote on (start, end, type) to match entity_strict_counts evaluation."""
59	    N = len(samples)
60	    threshold = N * threshold_frac
61	    counter = Counter()
62	    key_to_entity = {}
63	
64	    for s in samples:
65	        for e in s.get("entities", []):
66	            key = (e["start"], e["end"], e["type"])
67	            counter[key] += 1
68	            key_to_entity[key] = e
69	
70	    consensus = []
71	    for key, count in counter.items():
72	        if count > threshold:
73	            consensus.append(key_to_entity[key])
74	    return consensus
75	
76	
77	def analyze(instances, n_samples=None, compute_sj=False):
78	    greedy_tp = greedy_fp = greedy_fn = 0
79	    mv_tp = mv_fp = mv_fn = 0
80	    lp_tp = lp_fp = lp_fn = 0
81	    oracle_tp = oracle_fp = oracle_fn = 0
82	
83	    n_degen_keyset = 0
84	    per_inst_greedy = []
85	    per_inst_oracle = []
86	    per_inst_mv = []
87	    sj_scores = []
88	
89	    for inst in instances:
90	        gold_ents = inst["gold"]["entities"]
91	        samples = inst["samples"][:n_samples] if n_samples else inst["samples"]
92	
93	        # Greedy (use dedicated field if present, else sample 0)
94	        greedy = inst.get("greedy", samples[0])
95	        tp, fp, fn = entity_strict_counts(greedy.get("entities", []), gold_ents)
96	        greedy_tp += tp; greedy_fp += fp; greedy_fn += fn
97	        g_f1 = compute_entity_f1(greedy.get("entities", []), gold_ents)
98	        per_inst_greedy.append(g_f1)
99	
100	        # Majority voting
101	        consensus = majority_vote_entities(samples)
102	        tp, fp, fn = entity_strict_counts(consensus, gold_ents)
103	        mv_tp += tp; mv_fp += fp; mv_fn += fn
104	        per_inst_mv.append(compute_entity_f1(consensus, gold_ents))
105	
106	        # LP selection
107	        lp_idx = get_lp_selection_idx(inst, n_samples)
108	        lp_pred = samples[lp_idx]
109	        tp, fp, fn = entity_strict_counts(lp_pred.get("entities", []), gold_ents)
110	        lp_tp += tp; lp_fp += fp; lp_fn += fn
111	
112	        # Oracle
113	        sample_f1s = compute_sample_f1s(inst, n_samples)
114	        best_idx = max(range(len(sample_f1s)), key=lambda i: sample_f1s[i])
115	        best_sample = samples[best_idx]
116	        tp, fp, fn = entity_strict_counts(best_sample.get("entities", []), gold_ents)
117	        oracle_tp += tp; oracle_fp += fp; oracle_fn += fn
118	        per_inst_oracle.append(max(sample_f1s))
119	
120	        # Degeneracy: all samples produce identical (start, end, type) set
121	        entity_sets = [frozenset((e["start"], e["end"], e["type"])
122	                                 for e in s.get("entities", []))
123	                       for s in samples]
124	        if len(set(entity_sets)) == 1:
125	            n_degen_keyset += 1
126	
127	        # SJ (expensive for large N)
128	        if compute_sj:
129	            from consistency import structural_consistency_soft_jaccard
130	            sj = structural_consistency_soft_jaccard(samples, subtask="ner")
131	            sj_scores.append(sj)
132	
133	    n_inst = len(instances)
134	    greedy_f1 = micro_f1(greedy_tp, greedy_fp, greedy_fn)
135	    mv_f1_val = micro_f1(mv_tp, mv_fp, mv_fn)
136	    lp_f1_val = micro_f1(lp_tp, lp_fp, lp_fn)
137	    oracle_f1 = micro_f1(oracle_tp, oracle_fp, oracle_fn)
138	
139	    mv_delta = (mv_f1_val - greedy_f1) * 100
140	    lp_delta = (lp_f1_val - greedy_f1) * 100
141	    oracle_delta = (oracle_f1 - greedy_f1) * 100
142	    degen_rate = n_degen_keyset / n_inst * 100
143	
144	    # Instance-averaged deltas (alternative to micro)
145	    inst_mv_delta = np.mean([m - g for m, g in zip(per_inst_mv, per_inst_greedy)]) * 100
146	    inst_oracle_delta = np.mean([o - g for o, g in zip(per_inst_oracle, per_inst_greedy)]) * 100
147	
148	    # Capture rate: MV gain / oracle gain on instances where oracle > greedy
149	    o_gains, m_gains = [], []
150	    for i in range(n_inst):
151	        if per_inst_oracle[i] > per_inst_greedy[i] + 1e-9:
152	            o_gains.append(per_inst_oracle[i] - per_inst_greedy[i])
153	            m_gains.append(per_inst_mv[i] - per_inst_greedy[i])
154	    capture = sum(m_gains) / sum(o_gains) * 100 if o_gains else 0
155	
156	    # SJ rho
157	    sj_rho = float("nan")
158	    if compute_sj and sj_scores:
159	        rho, _ = spearmanr(sj_scores, per_inst_greedy)
160	        sj_rho = float(rho)
161	
162	    # Bootstrap CI for MV delta (instance-level)
163	    mv_ci = bootstrap_delta_ci(per_inst_mv, per_inst_greedy)
164	
165	    return {
166	        "n_inst": n_inst,
167	        "greedy_f1": greedy_f1,
168	        "mv_f1": mv_f1_val,
169	        "lp_f1": lp_f1_val,
170	        "oracle_f1": oracle_f1,
171	        "mv_delta_pp": mv_delta,
172	        "lp_delta_pp": lp_delta,
173	        "oracle_delta_pp": oracle_delta,
174	        "degen_rate": degen_rate,
175	        "capture_rate": capture,
176	        "sj_rho": sj_rho,
177	        "mv_ci": mv_ci,
178	        "inst_mv_delta_pp": inst_mv_delta,
179	        "inst_oracle_delta_pp": inst_oracle_delta,
180	    }
181	
182	
183	def print_comparison(N, res):
184	    print(f"\n{'=' * 72}")
185	    print(f"  N={N} Pretrained FewNERD Analysis (gold-nonempty, micro-avg)")
186	    print(f"  {res['n_inst']} instances")
187	    print(f"{'=' * 72}")
188	    print(f"  Greedy F1:          {res['greedy_f1']:.3f}")
189	    print(f"  MV F1:              {res['mv_f1']:.3f}  (Δ = {res['mv_delta_pp']:+.1f} pp)")
190	    ci = res["mv_ci"]
191	    ci_lo = ci["ci_lo"] * 100
192	    ci_hi = ci["ci_hi"] * 100
193	    print(f"  MV Δ 95% CI:        [{ci_lo:+.1f}, {ci_hi:+.1f}] pp")
194	    print(f"  LP F1:              {res['lp_f1']:.3f}  (Δ = {res['lp_delta_pp']:+.1f} pp)")
195	    print(f"  Oracle F1:          {res['oracle_f1']:.3f}  (Δ = {res['oracle_delta_pp']:+.1f} pp)")
196	    print(f"  Degeneracy rate:    {res['degen_rate']:.1f}%  (keyset_surface)")
197	    print(f"  Capture rate:       {res['capture_rate']:.0f}%")
198	    print(f"  --- Instance-averaged ---")
199	    print(f"  MV Δ (inst-avg):    {res['inst_mv_delta_pp']:+.1f} pp")
200	    print(f"  Oracle Δ (inst-avg):{res['inst_oracle_delta_pp']:+.1f} pp")
201	    if not np.isnan(res["sj_rho"]):
202	        print(f"  SJ ρ:               {res['sj_rho']:.3f}")
203	    else:
204	        print(f"  SJ ρ:               (skipped, use --compute_sj)")
205	
206	    # Comparison table
207	    print(f"\n{'=' * 72}")
208	    print(f"  N-scaling comparison")
209	    print(f"{'=' * 72}")
210	    header = f"  {'N':>4} | {'Greedy':>7} | {'MV Δ(pp)':>9} | {'Degen%':>7} | {'Oracle Δ':>9} | {'Capture':>8} | {'ρ_SJ':>6}"
211	    print(header)
212	    print(f"  {'-' * 4}-+-{'-' * 7}-+-{'-' * 9}-+-{'-' * 7}-+-{'-' * 9}-+-{'-' * 8}-+-{'-' * 6}")
213	    for n_ref, ref in sorted(REF.items()):
214	        sj_str = f"{ref['sj_rho']:.3f}" if ref.get("sj_rho") else "  N/A"
215	        print(f"  {n_ref:>4} | {ref['greedy']:>7.3f} | {ref['mv_delta']:>+8.1f} | {ref['degen']:>6.1f} | {ref['oracle_delta']:>+8.1f} | {ref['capture']:>7.0f}% | {sj_str}")
216	    sj_str = f"{res['sj_rho']:.3f}" if not np.isnan(res["sj_rho"]) else "  N/A"
217	    print(f"  {N:>4} | {res['greedy_f1']:>7.3f} | {res['mv_delta_pp']:>+8.1f} | {res['degen_rate']:>6.1f} | {res['oracle_delta_pp']:>+8.1f} | {res['capture_rate']:>7.0f}% | {sj_str}")
218	
219	    # Scenario determination
220	    print(f"\n  Scenario:")
221	    if res["mv_delta_pp"] >= 5.0:
222	        print(f"    → B (growth): MV Δ = {res['mv_delta_pp']:+.1f} pp > 5 → update Discussion")
223	    elif res["mv_delta_pp"] < 3.0:
224	        print(f"    → C (decline): MV Δ = {res['mv_delta_pp']:+.1f} pp < 3 → update Discussion")
225	    else:
226	        print(f"    → A (plateau): MV Δ = {res['mv_delta_pp']:+.1f} pp in [3, 5) → no Discussion change")
227	
228	    # LaTeX table row
229	    print(f"\n  LaTeX row for Table 4:")
230	    print(f"         & Pretrained ($N{{=}}{N}$) & .{res['greedy_f1']*1000:.0f} & $+${res['mv_delta_pp']:.1f} & {res['degen_rate']:.1f} & {res['capture_rate']:.0f}\\% & .{res['oracle_f1']*1000:.0f} \\\\")
231	
232	
233	def main():
234	    parser = argparse.ArgumentParser(description="N-scaling pretrained FewNERD analysis")
235	    parser.add_argument("--input", required=True, help="Path to samples.jsonl")
236	    parser.add_argument("--n_samples", type=int, default=None, help="Truncate to first N samples per instance")
237	    parser.add_argument("--compute_sj", action="store_true", help="Compute SJ rho (slow for large N)")
238	    args = parser.parse_args()
239	
240	    N = args.n_samples or "auto"
241	    print(f"Loading {args.input} ...")
242	    instances = load_gold_nonempty(args.input)
243	    print(f"  {len(instances)} gold-nonempty instances")
244	
245	    actual_n = len(instances[0]["samples"]) if instances else 0
246	    if args.n_samples:
247	        actual_n = min(args.n_samples, actual_n)
248	    print(f"  Using N={actual_n} samples per instance")
249	
250	    if args.compute_sj:
251	        print(f"  SJ computation enabled (N={actual_n}: {actual_n*(actual_n-1)//2} pairs/instance, may be slow)")
252	
253	    res = analyze(instances, n_samples=args.n_samples, compute_sj=args.compute_sj)
254	    print_comparison(actual_n, res)
255	
256	    # Save JSON results
257	    out_dir = os.path.dirname(args.input)
258	    out_path = os.path.join(out_dir, f"n{actual_n}_analysis.json")
259	    save = {k: v for k, v in res.items() if k != "mv_ci"}
260	    save["mv_ci_lo"] = res["mv_ci"]["ci_lo"] * 100
261	    save["mv_ci_hi"] = res["mv_ci"]["ci_hi"] * 100
262	    with open(out_path, "w") as f:
263	        json.dump(save, f, indent=2, default=str)
264	    print(f"\n  Results saved to {out_path}")
265	
266	
267	if __name__ == "__main__":
268	    main()
269	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3",
  "uuid": "14b88f8a-d9b9-43ac-aecd-e243dc39e7bd"
}
```

</details>

---


### System

_source line 107_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac8ef46b1ece704fd",
  "tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "description": "Running find /home/ubuntu/.agent-ml-research-idea_gen_051…",
  "usage": {
    "total_tokens": 69790,
    "tool_uses": 32,
    "duration_ms": 49367
  },
  "last_tool_name": "Bash",
  "uuid": "a0172b64-6fe6-4bab-89df-dd690081ab0d",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3"
}
```

---


### Tool call

_source line 108_

<details open><summary>🔧 Tool call — Bash · `toolu_013k3KwZu3dyqLqUwEGWS9cf`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie -name \"unified_metrics.py\" -o -name \"consistency.py\" | grep -v \".venv\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3",
  "uuid": "a78cf9e2-7a5c-4147-aa7d-1dbdd4310f3f",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HHDbRy3EtGojbh55yn6JWi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 4942,
      "cache_read_input_tokens": 64694,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4942,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### System

_source line 109_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac8ef46b1ece704fd",
  "tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "description": "Reading artifacts/consistency.py",
  "usage": {
    "total_tokens": 69794,
    "tool_uses": 33,
    "duration_ms": 49380
  },
  "last_tool_name": "Read",
  "uuid": "98535f72-8fb3-4ae7-bffe-a8d1034987d0",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3"
}
```

---


### Tool call

_source line 110_

<details open><summary>🔧 Tool call — Read · `toolu_011nVXaoLEvisv33gewYRyPF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/consistency.py",
  "limit": 80
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3",
  "uuid": "29f09e90-7d53-44eb-8e5a-c878909ab95a",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HHDbRy3EtGojbh55yn6JWi",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 4942,
      "cache_read_input_tokens": 64694,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4942,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 111 · 2026-05-23T18:55:39.778Z_

<details><summary>↩ Tool result · `toolu_011nVXaoLEvisv33gewYRyPF`</summary>

```text
1	"""Consistency metrics for structured information extraction with self-consistency.
2	
3	Implements three complementary consistency measures over N sampled extractions:
4	1. Fleiss' Kappa (surface matching) — treats N samples as N raters on entity presence
5	2. Structural soft Jaccard — span-level soft overlap with Hungarian matching
6	3. Oracle best-of-N — upper-bound F1 by selecting the best sample per instance
7	
8	Key dependencies: numpy, scipy (linear_sum_assignment).
9	"""
10	
11	from __future__ import annotations
12	
13	from itertools import combinations
14	from typing import TYPE_CHECKING
15	
16	import numpy as np
17	from scipy.optimize import linear_sum_assignment
18	
19	if TYPE_CHECKING:
20	    pass
21	
22	# ---------------------------------------------------------------------------
23	# Type aliases (mirrors shared data format)
24	# ---------------------------------------------------------------------------
25	Entity = dict       # {"text", "type", "start", "end"}
26	Relation = dict     # {"head", "tail", "type", ...}
27	Event = dict        # {"trigger": {...}, "arguments": [...]}
28	Extraction = dict   # {"entities", "relations", "events"}
29	
30	
31	# ===================================================================
32	# 1. Fleiss' Kappa — surface‐level entity agreement
33	# ===================================================================
34	
35	def _extract_surface_keys(sample: Extraction, subtask: str) -> set[tuple]:
36	    """Extract surface-level keys from a sample for Fleiss' Kappa computation."""
37	    if subtask == "ner":
38	        return {(e["text"], e["type"]) for e in sample.get("entities", [])}
39	    elif subtask == "re":
40	        return {(r["head"], r["tail"], r["type"]) for r in sample.get("relations", [])}
41	    elif subtask == "eae":
42	        keys: set[tuple] = set()
43	        for ev in sample.get("events", []):
44	            t = ev.get("trigger", {})
45	            for arg in ev.get("arguments", []):
46	                keys.add((t.get("text", ""), t.get("type", ""), arg["role"], arg["text"]))
47	        return keys
48	    else:
49	        raise ValueError(f"Unknown subtask: {subtask}")
50	
51	
52	def fleiss_kappa_surface(samples: list[Extraction], subtask: str = "ner") -> float:
53	    """Compute Fleiss' kappa treating N LLM samples as N raters on item presence.
54	
55	    Items are subtask-dependent surface keys:
56	    - ner: (entity_text, entity_type)
57	    - re: (head_text, tail_text, relation_type)
58	    - eae: (trigger_text, trigger_type, role, argument_text)
59	
60	    Args:
61	        samples: List of N extraction dicts.
62	        subtask: "ner", "re", or "eae".
63	
64	    Returns:
65	        Fleiss' kappa in [-1, 1].  Returns 1.0 for degenerate cases (≤1 unique
66	        item, perfect agreement, or undefined P_e).
67	    """
68	    n_raters = len(samples)
69	    if n_raters <= 1:
70	        return 1.0
71	
72	    # Collect unique keys and per-sample presence sets
73	    entity_sets: list[set[tuple]] = []
74	    all_keys: set[tuple] = set()
75	    for sample in samples:
76	        keys = _extract_surface_keys(sample, subtask)
77	        entity_sets.append(keys)
78	        all_keys |= keys
79	
80	    n_subjects = len(all_keys)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3",
  "uuid": "a1aadade-355d-411b-bfb9-efc621629c82"
}
```

</details>

---


### Tool result

_source line 112 · 2026-05-23T18:55:39.962Z_

<details><summary>↩ Tool result · `toolu_013k3KwZu3dyqLqUwEGWS9cf`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/intermediate/consistency.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/data/consistency.py
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/consistency.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3",
  "uuid": "59a2e7c3-dd0f-4189-a2f1-ded7b190ed1f"
}
```

</details>

---


### System

_source line 113_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac8ef46b1ece704fd",
  "tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "description": "Running find /home/ubuntu/.agent-ml-research-idea_gen_051…",
  "usage": {
    "total_tokens": 71185,
    "tool_uses": 34,
    "duration_ms": 51811
  },
  "last_tool_name": "Bash",
  "uuid": "f7601ff4-48c4-4d92-9204-536627c50b4f",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3"
}
```

---


### Tool call

_source line 114_

<details open><summary>🔧 Tool call — Bash · `toolu_01D9459fLmpKZ22ecPpFyS27`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie -maxdepth 2 -name \"*.csv\" -o -name \"scaling*.txt\" | head -10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3",
  "uuid": "a2689a4d-3a21-4165-93e3-d4e31244ed7e",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DkVq2ETSuYnUM9aAATnM9b",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1034,
      "cache_creation_input_tokens": 360,
      "cache_read_input_tokens": 69636,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 360,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 115 · 2026-05-23T18:55:42.252Z_

<details><summary>↩ Tool result · `toolu_01D9459fLmpKZ22ecPpFyS27`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/per_type_lp_analysis.csv
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/code/scaling_results.csv
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3",
  "uuid": "656544d4-f2d2-4899-a7d0-4427836987a6"
}
```

</details>

---


### System

_source line 116_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "ac8ef46b1ece704fd",
  "tool_use_id": "toolu_01UeLJnTZrz1DCdCXEbYiG7f",
  "status": "completed",
  "output_file": "",
  "summary": "Explore project code structure",
  "usage": {
    "total_tokens": 71414,
    "tool_uses": 34,
    "duration_ms": 78676
  },
  "uuid": "e9b25163-4f02-48bf-9465-c5ec1a1ad2df",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3"
}
```

---


### Tool result

_source line 117 · 2026-05-23T18:56:09.063Z_

<details><summary>↩ Tool result · `toolu_01UeLJnTZrz1DCdCXEbYiG7f`</summary>

````text
Excellent! Now I have a comprehensive understanding of the project. Let me compile the final report.

## Project Exploration Report: struct_self_consist_ie

### 1. Overall Directory Structure

The project is located at `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/` with the following key directories:

- **`/artifacts/`** - Main analysis and experimental code (200+ Python scripts)
- **`/scripts/`** - Analysis scripts for specific methods (adalp_analysis.py, dals_analysis.py, j_calibration.py)
- **`/code/`** - Core utility scripts (ner_lp_f1_correlation.py, aggregate_scaling_results.py, plot_scaling_curve.py)
- **`/docs/paper/figures/`** - Paper figure generation (_gen_n_scaling.py, gen_fig_overview.py)
- **`/checkpoints/`** - Experiment outputs and results
- **`/output/`** - Processed results and reports

### 2. N-Scaling Analysis Code

Key files for N-scaling analysis:

**Primary N-scaling files:**
- `/artifacts/n_inverse_scaling/run_analysis.py` (696 lines) - **Comprehensive inverse scaling test** for N=2,4,6,8,16 across 6 dataset×model configs, testing 6 construction methods with paired bootstrap significance tests
- `/artifacts/lp_best_n_scaling.py` (118 lines) - Computes LP-best F1 vs greedy F1 across N values (N=8,16,32,64)
- `/artifacts/lp_best_unified.py` (150 lines) - Unified instance set analysis for LP-best with N=8/16/32/64
- `/artifacts/analyze_n32.py` (269 lines) - N-scaling analysis for pretrained FewNERD with N=8/16/32 comparison
- `/docs/paper/figures/_gen_n_scaling.py` (59 lines) - Generates paper figure for N-scaling results (MV ΔF1 vs log2(N))

**Scaling aggregation & reporting:**
- `/code/aggregate_scaling_results.py` (242 lines) - Unified scaling results aggregation across model sizes
- `/code/generate_scale_table.py` - Table generation for scaling experiments

### 3. Transition & Inverse Scaling Analysis

**Inverse Scaling Detection:**
- `/artifacts/n_inverse_scaling/run_analysis.py` is the definitive implementation:
  - Tests whether F1 **decreases** as N increases for construction methods
  - Sub-samples from N=16/32 down to N=2,4,6,8,(16)
  - Identifies inverse scaling transitions with thresholds (>0.1pp drop is flagged)
  - Runs **paired bootstrap** significance tests (B=5000-10000)
  - Computes 95% CI and p-values for each transition
  - Tests 6 methods: `majority_vote`, `lp_weighted`, `vc_weighted`, `sj_weighted`, `theta2n`, `uniform`
  - Uses micro-averaged entity-level F1

**Key Methods Tested:**
- **Majority Vote (MV)** - Fixed threshold θ=0.5
- **LP-weighted** - Adaptive threshold θ=2/N, softmax weights over mean log-probs
- **VC-weighted** - Vote-count weighted construction
- **SJ-weighted** - Structural soft Jaccard weighted
- **theta2n** - Uniform construction with θ=2/N
- **Uniform** - Fixed threshold θ=0.25

### 4. samples.jsonl File Structure

Based on code analysis, each line is a JSON object with schema:

```python
{
    "id": str,
    "text": str,
    "gold": {
        "entities": [
            {
                "text": str,
                "type": str,
                "start": int,
                "end": int
            },
            ...
        ]
    },
    "greedy": {
        "entities": [...]
    },
    "samples": [
        {
            "entities": [...],
            "mean_logprob": float,
            # optional: "logprobs" if list form stored separately
        },
        ...
    ],
    # optional fields:
    "logprobs": [float, ...],  # if not in samples
    "relations": [...],         # for RE tasks
    "events": [...]            # for EAE tasks
}
```

**Processing Details:**
- Instances are filtered to **gold-nonempty** (have ≥1 gold entity)
- Entity matching uses strict 4-tuple: `(start, end, type, text)` or `(start, end, type)` depending on context
- Micro-averaged F1: pool all TP/FP/FN across instances, compute once

### 5. F1 Score Computation for Different Methods

All implementations use **entity-level micro-averaging**:

**Key Functions:**
- `/artifacts/evaluation.py` - `entity_strict_match()` and `compute_ner_f1()` for baseline micro-F1
- `/artifacts/analyze_n32.py` - Reference implementation with degeneracy, oracle, and MV
- `/artifacts/n_inverse_scaling/run_analysis.py` - Complete weighted construction variants

**F1 Computation Pattern:**
```python
def compute_f1(pred_entities, gold_entities):
    pred_set = {(e["start"], e["end"], e["type"]) for e in pred_entities}
    gold_set = {(e["start"], e["end"], e["type"]) for e in gold_entities}
    tp = len(pred_set & gold_set)
    fp = len(pred_set - gold_set)
    fn = len(gold_set - pred_set)
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0
    return 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0
```

**Majority Vote Construction:**
```python
def weighted_construction(samples, threshold, weights=None):
    entity_counts = defaultdict(float)
    N = len(samples)
    for i, sample in enumerate(samples):
        w = weights[i] if weights is not None else 1.0
        seen = set()
        for e in sample.get("entities", []):
            key = (e["start"], e["end"], e["type"])
            if key not in seen:
                entity_counts[key] += w
                seen.add(key)
    total_weight = sum(weights) if weights is not None else N
    constructed = set()
    for key, count in entity_counts.items():
        if count / total_weight >= threshold:
            constructed.add(key)
    return constructed
```

**LP-best Selection:**
```python
def get_lp_weights(samples, inst):
    lps = [s.get("mean_logprob", -100.0) for s in samples]
    max_lp = max(lps)
    ws = [math.exp(lp - max_lp) for lp in lps]
    total = sum(ws)
    return [w / total for w in ws] if total > 0 else [1.0/len(samples)]*len(samples)

# Best selection
best_idx = max(range(len(samples)), key=lambda i: samples[i]["mean_logprob"])
```

### 6. Key Analysis Scripts & Functions

**Unified Metrics (imported in analyze_n32.py):**
- `compute_entity_f1()` - Per-instance F1
- `compute_sample_f1s()` - F1 for each sample in instance
- `get_lp_selection_idx()` - Pick highest mean_logprob sample
- `bootstrap_delta_ci()` - Confidence intervals for deltas

**Consistency Metrics (consistency.py):**
- `fleiss_kappa_surface()` - Surface-level agreement
- `structural_consistency_soft_jaccard()` - Soft span overlap with Hungarian matching
- Degeneracy: `len(set(entity_sets)) == 1` (all samples produce identical output)

**AdaLP Analysis (scripts/adalp_analysis.py):**
- Per-instance degeneracy score: `max_count / N` where max_count is most frequent F1 value
- Threshold selection via leave-one-dataset-out CV
- Selection: use greedy if degen > τ, else LP-best

### 7. N-Scaling Results Summary

From `/artifacts/lp_best_n_scaling.py` (Table format):

**SciERC (seed=42):**
- N=8:  LP-best F1=66.35%, Greedy=67.72%, Δ=-1.37pp
- N=16: LP-best F1=67.24%, Greedy=68.00%, Δ=-0.76pp
- N=32: LP-best F1=67.54%, Greedy=67.30%, Δ=+0.24pp
- N=64: LP-best F1=67.83%, Greedy=67.30%, Δ=+0.53pp

**CoNLL (seed varies):**
- N=8:  Δ=-0.20pp (seed=123)
- N=16: Δ=+0.32pp (seed=456)
- N=32: Δ=+0.44pp (seed=42)
- N=64: Δ=+0.61pp (seed=42)

**FewNERD:**
- N=8:  MV Δ=-2.71pp
- N=16: MV Δ=-1.65pp
- N=32: Pending

From `/artifacts/n_inverse_scaling/run_analysis.py` output:
- Tests 6 configs: 2 models × 3 datasets
- 6 construction methods each
- Reports statistically significant inverse scaling cases with CI

### 8. Core Evaluation Modules

**Key Files:**
- `/artifacts/evaluation.py` (80+ lines) - NER/RE/EAE evaluation, strict entity matching, micro-averaged F1
- `/artifacts/data_utils.py` (80+ lines) - UIE JSON format definitions, data type schemas
- `/artifacts/consistency.py` (150+ lines) - Fleiss' Kappa, soft Jaccard, oracle computation
- `/scripts/j_calibration.py` - Calibration analysis for construction methods

**Type Definitions:**
```python
class Entity(TypedDict):
    text: str
    type: str
    start: int
    end: int

class Extraction(TypedDict, total=False):
    entities: list[Entity]
    relations: list[Relation]
    events: list[Event]

class Instance(TypedDict, total=False):
    id: str
    text: str
    entities: list[Entity]
    relations: list[Relation]
    events: list[Event]
```

### 9. Research Focus & Key Findings

**Primary Contribution:** Dataset-dependent optimal aggregation strategy determined by 4-stage diagnostic cascade:
1. Instance degeneracy (21-58% of instances produce identical F1)
2. LP compression (median within-instance LP range: 0.041 nats)
3. LP-F1 alignment (ρ varies by dataset: FewNERD ρ~0.5-0.7 vs SciERC ρ~0.2)
4. Structural signal limitation (4/5 signals are instance-level aggregates)

**N-Scaling Key Insights:**
- MV gains are monotonically increasing but universally <1pp
- LP-best saturates at N=8
- Dataset-dependent optimal strategy: LP dominates FewNERD (+8pp), MV dominates CoNLL (+0.61pp vs LP -2.34pp), approximately neutral on SciERC

All file paths are absolute and ready for analysis/extension work.
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3",
  "uuid": "ddf90511-2637-4a07-a87a-b7a97ac2147a",
  "tool_use_result": {
    "status": "completed",
    "prompt": "Explore the project at /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/\n\nI need to understand:\n1. The overall directory structure (especially src/ and any analysis scripts)\n2. Any scripts related to N-scaling analysis, transition analysis, or inverse scaling\n3. How samples.jsonl files are structured and processed\n4. Any existing code that computes F1 scores for different methods (MV, LP-best, LP-weighted, uniform construction)\n\nSearch broadly - check src/, scripts/, analysis/, notebooks/ etc. Look for files with names containing \"scaling\", \"transition\", \"n_scaling\", \"analyze\". Also grep for \"inverse\" and \"transition\" in Python files.\n\nReport: file paths, key functions, and data format details.",
    "agentId": "ac8ef46b1ece704fd",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Excellent! Now I have a comprehensive understanding of the project. Let me compile the final report.\n\n## Project Exploration Report: struct_self_consist_ie\n\n### 1. Overall Directory Structure\n\nThe project is located at `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/` with the following key directories:\n\n- **`/artifacts/`** - Main analysis and experimental code (200+ Python scripts)\n- **`/scripts/`** - Analysis scripts for specific methods (adalp_analysis.py, dals_analysis.py, j_calibration.py)\n- **`/code/`** - Core utility scripts (ner_lp_f1_correlation.py, aggregate_scaling_results.py, plot_scaling_curve.py)\n- **`/docs/paper/figures/`** - Paper figure generation (_gen_n_scaling.py, gen_fig_overview.py)\n- **`/checkpoints/`** - Experiment outputs and results\n- **`/output/`** - Processed results and reports\n\n### 2. N-Scaling Analysis Code\n\nKey files for N-scaling analysis:\n\n**Primary N-scaling files:**\n- `/artifacts/n_inverse_scaling/run_analysis.py` (696 lines) - **Comprehensive inverse scaling test** for N=2,4,6,8,16 across 6 dataset×model configs, testing 6 construction methods with paired bootstrap significance tests\n- `/artifacts/lp_best_n_scaling.py` (118 lines) - Computes LP-best F1 vs greedy F1 across N values (N=8,16,32,64)\n- `/artifacts/lp_best_unified.py` (150 lines) - Unified instance set analysis for LP-best with N=8/16/32/64\n- `/artifacts/analyze_n32.py` (269 lines) - N-scaling analysis for pretrained FewNERD with N=8/16/32 comparison\n- `/docs/paper/figures/_gen_n_scaling.py` (59 lines) - Generates paper figure for N-scaling results (MV ΔF1 vs log2(N))\n\n**Scaling aggregation & reporting:**\n- `/code/aggregate_scaling_results.py` (242 lines) - Unified scaling results aggregation across model sizes\n- `/code/generate_scale_table.py` - Table generation for scaling experiments\n\n### 3. Transition & Inverse Scaling Analysis\n\n**Inverse Scaling Detection:**\n- `/artifacts/n_inverse_scaling/run_analysis.py` is the definitive implementation:\n  - Tests whether F1 **decreases** as N increases for construction methods\n  - Sub-samples from N=16/32 down to N=2,4,6,8,(16)\n  - Identifies inverse scaling transitions with thresholds (>0.1pp drop is flagged)\n  - Runs **paired bootstrap** significance tests (B=5000-10000)\n  - Computes 95% CI and p-values for each transition\n  - Tests 6 methods: `majority_vote`, `lp_weighted`, `vc_weighted`, `sj_weighted`, `theta2n`, `uniform`\n  - Uses micro-averaged entity-level F1\n\n**Key Methods Tested:**\n- **Majority Vote (MV)** - Fixed threshold θ=0.5\n- **LP-weighted** - Adaptive threshold θ=2/N, softmax weights over mean log-probs\n- **VC-weighted** - Vote-count weighted construction\n- **SJ-weighted** - Structural soft Jaccard weighted\n- **theta2n** - Uniform construction with θ=2/N\n- **Uniform** - Fixed threshold θ=0.25\n\n### 4. samples.jsonl File Structure\n\nBased on code analysis, each line is a JSON object with schema:\n\n```python\n{\n    \"id\": str,\n    \"text\": str,\n    \"gold\": {\n        \"entities\": [\n            {\n                \"text\": str,\n                \"type\": str,\n                \"start\": int,\n                \"end\": int\n            },\n            ...\n        ]\n    },\n    \"greedy\": {\n        \"entities\": [...]\n    },\n    \"samples\": [\n        {\n            \"entities\": [...],\n            \"mean_logprob\": float,\n            # optional: \"logprobs\" if list form stored separately\n        },\n        ...\n    ],\n    # optional fields:\n    \"logprobs\": [float, ...],  # if not in samples\n    \"relations\": [...],         # for RE tasks\n    \"events\": [...]            # for EAE tasks\n}\n```\n\n**Processing Details:**\n- Instances are filtered to **gold-nonempty** (have ≥1 gold entity)\n- Entity matching uses strict 4-tuple: `(start, end, type, text)` or `(start, end, type)` depending on context\n- Micro-averaged F1: pool all TP/FP/FN across instances, compute once\n\n### 5. F1 Score Computation for Different Methods\n\nAll implementations use **entity-level micro-averaging**:\n\n**Key Functions:**\n- `/artifacts/evaluation.py` - `entity_strict_match()` and `compute_ner_f1()` for baseline micro-F1\n- `/artifacts/analyze_n32.py` - Reference implementation with degeneracy, oracle, and MV\n- `/artifacts/n_inverse_scaling/run_analysis.py` - Complete weighted construction variants\n\n**F1 Computation Pattern:**\n```python\ndef compute_f1(pred_entities, gold_entities):\n    pred_set = {(e[\"start\"], e[\"end\"], e[\"type\"]) for e in pred_entities}\n    gold_set = {(e[\"start\"], e[\"end\"], e[\"type\"]) for e in gold_entities}\n    tp = len(pred_set & gold_set)\n    fp = len(pred_set - gold_set)\n    fn = len(gold_set - pred_set)\n    precision = tp / (tp + fp) if (tp + fp) > 0 else 0\n    recall = tp / (tp + fn) if (tp + fn) > 0 else 0\n    return 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0\n```\n\n**Majority Vote Construction:**\n```python\ndef weighted_construction(samples, threshold, weights=None):\n    entity_counts = defaultdict(float)\n    N = len(samples)\n    for i, sample in enumerate(samples):\n        w = weights[i] if weights is not None else 1.0\n        seen = set()\n        for e in sample.get(\"entities\", []):\n            key = (e[\"start\"], e[\"end\"], e[\"type\"])\n            if key not in seen:\n                entity_counts[key] += w\n                seen.add(key)\n    total_weight = sum(weights) if weights is not None else N\n    constructed = set()\n    for key, count in entity_counts.items():\n        if count / total_weight >= threshold:\n            constructed.add(key)\n    return constructed\n```\n\n**LP-best Selection:**\n```python\ndef get_lp_weights(samples, inst):\n    lps = [s.get(\"mean_logprob\", -100.0) for s in samples]\n    max_lp = max(lps)\n    ws = [math.exp(lp - max_lp) for lp in lps]\n    total = sum(ws)\n    return [w / total for w in ws] if total > 0 else [1.0/len(samples)]*len(samples)\n\n# Best selection\nbest_idx = max(range(len(samples)), key=lambda i: samples[i][\"mean_logprob\"])\n```\n\n### 6. Key Analysis Scripts & Functions\n\n**Unified Metrics (imported in analyze_n32.py):**\n- `compute_entity_f1()` - Per-instance F1\n- `compute_sample_f1s()` - F1 for each sample in instance\n- `get_lp_selection_idx()` - Pick highest mean_logprob sample\n- `bootstrap_delta_ci()` - Confidence intervals for deltas\n\n**Consistency Metrics (consistency.py):**\n- `fleiss_kappa_surface()` - Surface-level agreement\n- `structural_consistency_soft_jaccard()` - Soft span overlap with Hungarian matching\n- Degeneracy: `len(set(entity_sets)) == 1` (all samples produce identical output)\n\n**AdaLP Analysis (scripts/adalp_analysis.py):**\n- Per-instance degeneracy score: `max_count / N` where max_count is most frequent F1 value\n- Threshold selection via leave-one-dataset-out CV\n- Selection: use greedy if degen > τ, else LP-best\n\n### 7. N-Scaling Results Summary\n\nFrom `/artifacts/lp_best_n_scaling.py` (Table format):\n\n**SciERC (seed=42):**\n- N=8:  LP-best F1=66.35%, Greedy=67.72%, Δ=-1.37pp\n- N=16: LP-best F1=67.24%, Greedy=68.00%, Δ=-0.76pp\n- N=32: LP-best F1=67.54%, Greedy=67.30%, Δ=+0.24pp\n- N=64: LP-best F1=67.83%, Greedy=67.30%, Δ=+0.53pp\n\n**CoNLL (seed varies):**\n- N=8:  Δ=-0.20pp (seed=123)\n- N=16: Δ=+0.32pp (seed=456)\n- N=32: Δ=+0.44pp (seed=42)\n- N=64: Δ=+0.61pp (seed=42)\n\n**FewNERD:**\n- N=8:  MV Δ=-2.71pp\n- N=16: MV Δ=-1.65pp\n- N=32: Pending\n\nFrom `/artifacts/n_inverse_scaling/run_analysis.py` output:\n- Tests 6 configs: 2 models × 3 datasets\n- 6 construction methods each\n- Reports statistically significant inverse scaling cases with CI\n\n### 8. Core Evaluation Modules\n\n**Key Files:**\n- `/artifacts/evaluation.py` (80+ lines) - NER/RE/EAE evaluation, strict entity matching, micro-averaged F1\n- `/artifacts/data_utils.py` (80+ lines) - UIE JSON format definitions, data type schemas\n- `/artifacts/consistency.py` (150+ lines) - Fleiss' Kappa, soft Jaccard, oracle computation\n- `/scripts/j_calibration.py` - Calibration analysis for construction methods\n\n**Type Definitions:**\n```python\nclass Entity(TypedDict):\n    text: str\n    type: str\n    start: int\n    end: int\n\nclass Extraction(TypedDict, total=False):\n    entities: list[Entity]\n    relations: list[Relation]\n    events: list[Event]\n\nclass Instance(TypedDict, total=False):\n    id: str\n    text: str\n    entities: list[Entity]\n    relations: list[Relation]\n    events: list[Event]\n```\n\n### 9. Research Focus & Key Findings\n\n**Primary Contribution:** Dataset-dependent optimal aggregation strategy determined by 4-stage diagnostic cascade:\n1. Instance degeneracy (21-58% of instances produce identical F1)\n2. LP compression (median within-instance LP range: 0.041 nats)\n3. LP-F1 alignment (ρ varies by dataset: FewNERD ρ~0.5-0.7 vs SciERC ρ~0.2)\n4. Structural signal limitation (4/5 signals are instance-level aggregates)\n\n**N-Scaling Key Insights:**\n- MV gains are monotonically increasing but universally <1pp\n- LP-best saturates at N=8\n- Dataset-dependent optimal strategy: LP dominates FewNERD (+8pp), MV dominates CoNLL (+0.61pp vs LP -2.34pp), approximately neutral on SciERC\n\nAll file paths are absolute and ready for analysis/extension work."
      }
    ],
    "totalDurationMs": 78677,
    "totalTokens": 74241,
    "totalToolUseCount": 34,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1249,
      "cache_read_input_tokens": 69996,
      "output_tokens": 2991,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1249
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 2991,
          "cache_read_input_tokens": 69996,
          "cache_creation_input_tokens": 1249,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1249,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 13,
      "searchCount": 5,
      "bashCount": 16,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  }
}
````

</details>

---


### Assistant

_source line 118_

<details><summary>Logged reasoning block</summary>

```text
Great, I have a lot of information now. Let me process the registry data and find the Few-NERD experiments with different seeds and N values. The registry output was too large and saved to a file. Let me query it with jq to find relevant experiments.

Key findings from the code exploration:
1. The main inverse scaling analysis is in `/artifacts/n_inverse_scaling/run_analysis.py`
2. samples.jsonl has a specific structure with gold entities, samples, mean_logprob etc.
3. The F1 computation uses entity-level micro-averaging
4. Methods include: MV, LP-weighted, VC-weighted, SJ-weighted, theta2n, uniform


5. I need to locate the Few-NERD experiments across seeds 42, 123, 456 and potentially a fourth seed, identify the samples.jsonl files for each N value, examine the existing analysis code to understand its computation logic, then adapt it to handle multiple seeds.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3",
  "uuid": "12ed7bce-a992-4537-a801-f2f7b8065b7f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YSmcET3G1TyBSdNvfGhRZr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3948,
      "cache_read_input_tokens": 26754,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3948
      },
      "output_tokens": 9,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Assistant

_source line 119_

Registry 数据量大，用 agent 解析。同时读取现有分析脚本。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3",
  "uuid": "94587eab-90ac-435c-bd84-20349680df2a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YSmcET3G1TyBSdNvfGhRZr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3948,
      "cache_read_input_tokens": 26754,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3948
      },
      "output_tokens": 9,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 120_

<details open><summary>🔧 Tool call — Agent · `toolu_01XmQpCHSRzKW6h3UmJKCNpz`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Parse registry for FewNERD experiments",
  "prompt": "I need to parse a large JSON registry file to find Few-NERD experiments with different seeds and N values.\n\nThe file is at: /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/9ee457e1-50d5-4907-947a-5d727dccbec3/tool-results/mcp-agent-ml-research-read_registry-1779562484737.txt\n\nThis is a JSON file with schema: {result: string} where the result string contains the actual registry data.\n\nI need you to:\n1. First probe the structure with bash (python/jq)\n2. Find ALL experiments that involve \"Few-NERD\" or \"fewnerd\" (case insensitive)\n3. For each, extract: experiment ID, seed value, N value(s), dataset name, model, and any file paths (especially samples.jsonl paths or output directories)\n4. Also look for experiments that mention different seeds (42, 123, 456, or any other seed values)\n5. Look for experiments with different N values (2, 4, 8, 16, 32, 64)\n\nReport the complete list of experiments with their details, organized by seed. I need the exact file paths to samples.jsonl files on the server."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3",
  "uuid": "ded69a94-0638-41c0-a197-8e6d5c50bc41",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YSmcET3G1TyBSdNvfGhRZr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3948,
      "cache_read_input_tokens": 26754,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3948
      },
      "output_tokens": 9,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### System

_source line 121_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "a344d8287d4e0d127",
  "tool_use_id": "toolu_01XmQpCHSRzKW6h3UmJKCNpz",
  "description": "Parse registry for FewNERD experiments",
  "task_type": "local_agent",
  "prompt": "I need to parse a large JSON registry file to find Few-NERD experiments with different seeds and N values.\n\nThe file is at: /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/9ee457e1-50d5-4907-947a-5d727dccbec3/tool-results/mcp-agent-ml-research-read_registry-1779562484737.txt\n\nThis is a JSON file with schema: {result: string} where the result string contains the actual registry data.\n\nI need you to:\n1. First probe the structure with bash (python/jq)\n2. Find ALL experiments that involve \"Few-NERD\" or \"fewnerd\" (case insensitive)\n3. For each, extract: experiment ID, seed value, N value(s), dataset name, model, and any file paths (especially samples.jsonl paths or output directories)\n4. Also look for experiments that mention different seeds (42, 123, 456, or any other seed values)\n5. Look for experiments with different N values (2, 4, 8, 16, 32, 64)\n\nReport the complete list of experiments with their details, organized by seed. I need the exact file paths to samples.jsonl files on the server.",
  "uuid": "7935633d-8ccc-484b-8ee1-4605d63cba9e",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3"
}
```

---


## Round 2

## Round 2

642 recorded events


### User

_source line 122 · 2026-05-23T18:56:29.387Z_

I need to parse a large JSON registry file to find Few-NERD experiments with different seeds and N values.

The file is at: /home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/9ee457e1-50d5-4907-947a-5d727dccbec3/tool-results/mcp-agent-ml-research-read_registry-1779562484737.txt

This is a JSON file with schema: {result: string} where the result string contains the actual registry data.

I need you to:
1. First probe the structure with bash (python/jq)
2. Find ALL experiments that involve "Few-NERD" or "fewnerd" (case insensitive)
3. For each, extract: experiment ID, seed value, N value(s), dataset name, model, and any file paths (especially samples.jsonl paths or output directories)
4. Also look for experiments that mention different seeds (42, 123, 456, or any other seed values)
5. Look for experiments with different N values (2, 4, 8, 16, 32, 64)

Report the complete list of experiments with their details, organized by seed. I need the exact file paths to samples.jsonl files on the server.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01XmQpCHSRzKW6h3UmJKCNpz",
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3",
  "uuid": "eeefc41f-45fc-47c6-a90d-fc6d77b2d075"
}
```

</details>

---


### Tool call

_source line 123_

<details open><summary>🔧 Tool call — Read · `toolu_01JL74ZYrMDMT1DLQ13rGuEt`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/n_inverse_scaling/run_analysis.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9ee457e1-50d5-4907-947a-5d727dccbec3",
  "uuid": "a99f4029-9cc2-4ca6-97d9-1a9823c9fc9e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YSmcET3G1TyBSdNvfGhRZr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3948,
      "cache_read_input_tokens": 26754,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3948
      },
      "output_tokens": 9,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---
