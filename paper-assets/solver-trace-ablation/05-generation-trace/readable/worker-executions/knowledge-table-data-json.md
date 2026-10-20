# knowledge table data json

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 54
- **Recorded user turns:** 1
- **Tool calls:** 15
- **Original source:** `logs/workers/worker_knowledge_table-data-json_20260514T172336.log`
- **Structured JSON:** [`e5da492c1d315afddc9f.json`](../../sessions/e5/e5da492c1d315afddc9f.json)

## Before a recorded user message

15 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "session_id": "eb5b7954-c1fd-473d-8da7-d1389c3f22e7",
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
    "mcp__agent-ml-research__read_project_file",
    "mcp__agent-ml-research__read_registry",
    "mcp__agent-ml-research__register_artifact",
    "mcp__agent-ml-research__save_project_file",
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
  "uuid": "8cde3488-5351-40d2-b44d-a355a6f59226",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/memory/"
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
    "status": "allowed",
    "resetsAt": 1778782200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "bdfee12c-7d39-41c2-a10c-3c5519b0750d",
  "session_id": "eb5b7954-c1fd-473d-8da7-d1389c3f22e7"
}
```

---

### Assistant

_source line 4_

I'll gather the registry data and evidence tables, then assemble the structured JSON.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eb5b7954-c1fd-473d-8da7-d1389c3f22e7",
  "uuid": "09ad741b-55be-49cc-a226-a00baa7f053e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011kuzYSy42iaoyum5ifFtk2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14014,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14014
      },
      "output_tokens": 2,
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

_source line 5_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_012UyPt67F4vbJypiisFd7X7`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
  "max_results": 4
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eb5b7954-c1fd-473d-8da7-d1389c3f22e7",
  "uuid": "f52954d7-a39e-431b-8371-6a6c4be27a35",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011kuzYSy42iaoyum5ifFtk2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14014,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14014
      },
      "output_tokens": 2,
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

_source line 6 · 2026-05-14T17:23:50.082Z_

<details><summary>↩ Tool result · `toolu_012UyPt67F4vbJypiisFd7X7`</summary>

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
  "tool_name": "mcp__agent-ml-research__save_project_file"
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
  "session_id": "eb5b7954-c1fd-473d-8da7-d1389c3f22e7",
  "uuid": "161abc0e-93f5-486a-a56b-26bcb25389c1",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
    "total_deferred_tools": 25
  }
}
```

</details>

---

### Assistant

_source line 7_

<details><summary>Logged reasoning block</summary>

```text
Let me fetch the registry data and the evidence tables in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eb5b7954-c1fd-473d-8da7-d1389c3f22e7",
  "uuid": "eb218aaa-4883-4f9b-b624-e43d012a0589",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01186EUALkLWoTLB1kxMgBsw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1677,
      "cache_read_input_tokens": 25855,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1677
      },
      "output_tokens": 53,
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

_source line 8_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01SwyhXmFFmkBZETJ1zUWTFB`</summary>

```json
{
  "project": "solver-trace-ablation",
  "fields": [
    "*"
  ],
  "limit": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eb5b7954-c1fd-473d-8da7-d1389c3f22e7",
  "uuid": "6f935871-c957-4161-9786-533381521135",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01186EUALkLWoTLB1kxMgBsw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1677,
      "cache_read_input_tokens": 25855,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1677
      },
      "output_tokens": 53,
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

<details open><summary>🔧 Tool call — Read · `toolu_01YRjLURQeKwijqezXndCmUr`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/evidence_tables_d051.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eb5b7954-c1fd-473d-8da7-d1389c3f22e7",
  "uuid": "685dfcf5-3642-4aa6-99dd-1a9274868d63",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01186EUALkLWoTLB1kxMgBsw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1677,
      "cache_read_input_tokens": 25855,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1677
      },
      "output_tokens": 53,
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

_source line 10 · 2026-05-14T17:23:53.943Z_

<details><summary>↩ Tool result · `toolu_01SwyhXmFFmkBZETJ1zUWTFB`</summary>

```text
Error: result (109,074 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/eb5b7954-c1fd-473d-8da7-d1389c3f22e7/tool-results/mcp-agent-ml-research-read_registry-1778779433924.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/eb5b7954-c1fd-473d-8da7-d1389c3f22e7/tool-results/mcp-agent-ml-research-read_registry-1778779433924.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/eb5b7954-c1fd-473d-8da7-d1389c3f22e7/tool-results/mcp-agent-ml-research-read_registry-1778779433924.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "eb5b7954-c1fd-473d-8da7-d1389c3f22e7",
  "uuid": "2936fc57-f2a0-4b63-8a20-87e98a5f3e4c",
  "tool_use_result": {
    "content": "Error: result (109,074 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/eb5b7954-c1fd-473d-8da7-d1389c3f22e7/tool-results/mcp-agent-ml-research-read_registry-1778779433924.txt.\nFormat: JSON with schema: {result: string}\n- For targeted queries (find a value, filter by field): use jq on the file directly.\n- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/eb5b7954-c1fd-473d-8da7-d1389c3f22e7/tool-results/mcp-agent-ml-research-read_registry-1778779433924.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.\n- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/eb5b7954-c1fd-473d-8da7-d1389c3f22e7/tool-results/mcp-agent-ml-research-read_registry-1778779433924.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim.\" A vague \"summarize this\" may lose detail.\n",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"plan018-additive-random-b01-s43-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T14:01:24.111Z\", \"updated_at\": \"2026-05-14T17:17:02.398Z\", \"hypothesis\": \"Random β=0.1 seed=43 控制组 r2: 重试 (原 s43 step 200 磁盘满崩溃)。与 plan002-b01-s43 (ISR β=0.1) 同 seed 对照。3-seed mean±std 审稿硬性要求。\", \"parent\": \"plan018-additive-random-b01-s43\", \"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_random_b01.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 43 --beta 0.1 --reward_mode additive_random --output_dir /root/autodl-tmp/outputs/plan018_additive_random_b01_s43_r2\\\"\", \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_random_b01.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 43 --beta 0.1 --reward_mode additive_random --output_dir /root/autodl-tmp/outputs/plan018_additive_random_b01_s43_r2\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"858386\", \"log_path\": \"~/runs/solver-trace-ablation/plan018-additive-random-b01-s43-r2.log\", \"submitted_at\": \"2026-05-14T15:24:32.942Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan018_additive_random_b01_s43_r2\", \"wall_clock_seconds\": 6748.8, \"gpu_hours\": 1.87}, \"pid\": \"858386\", \"log_path\": \"~/runs/solver-trace-ablation/plan018-additive-random-b01-s43-r2.log\", \"reproduce\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_random_b01.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 43 --beta 0.1 --reward_mode additive_random --output_dir /root/autodl-tmp/outputs/plan018_additive_random_b01_s43_r2\\\"\", \"finished_at\": \"2026-05-14T16:43:53.042Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T16:43:54.952857+00:00\"}]}, \"metrics\": {\"h7_rate\": 0, \"h7_count\": 0, \"h1_rate\": 93.2, \"h1_count\": 82, \"genuine_rate\": 6.8, \"genuine_count\": 6}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-14T17:17:01.774Z\"}, \"plan006-prolog-sta-s44\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T09:19:39.743Z\", \"updated_at\": \"2026-05-14T16:52:27.739Z\", \"hypothesis\": \"Prolog exec+STA GRPO seed=44: 第三 seed。3-seed mean±std 用于论文 Claim 3 跨 logic type 统计支撑。\", \"notes\": \"PREPARING. 命令模板已修正：去掉 --warmup_ratio，与 sta-s42 (warmup_ratio=0.0) 一致。Config: configs/grpo_prolog_exec_sta.yaml + seed=44. Output: /root/autodl-tmp/outputs/plan006_prolog_sta_s44. 等 GPU 释放。\", \"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-14T16:46:42.163Z\", \"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_prolog_exec_sta.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 44 --output_dir /root/autodl-tmp/outputs/plan006_prolog_sta_s44\\\"\"}, \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_prolog_exec_sta.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 44 --output_dir /root/autodl-tmp/outputs/plan006_prolog_sta_s44\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"908945\", \"log_path\": \"~/runs/solver-trace-ablation/plan006-prolog-sta-s44.log\", \"submitted_at\": \"2026-05-14T16:52:27.078Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"pid\": \"908945\", \"log_path\": \"~/runs/solver-trace-ablation/plan006-prolog-sta-s44.log\"}, \"plan006-prolog-sta-s42\": {\"status\": \"DONE\", \"retry_count\": 2, \"created_at\": \"2026-05-14T09:19:38.117Z\", \"updated_at\": \"2026-05-14T16:49:42.052Z\", \"hypothesis\": \"Prolog exec+STA GRPO seed=42: ISR reward 在 Prolog logic type 上的效果。与 plan006-prolog-exec-s42 (exec-only) 对照，验证 STA/ISR 的 hacking 检测和 Goodhart 效应是否跨 logic type 泛化。\", \"server\": \"westd-39279\", \"gpu\": \"\", \"reproduce\": {\"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-14T09:49:40.272Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_prolog_exec_sta.yaml --num_steps 500 --seed 42 --output_dir /root/autodl-tmp/outputs/plan006_prolog_sta_s42\\\"\", \"finished_at\": \"2026-05-14T10:38:13.891Z\", \"training_hours\": 0.81}, \"failure_reason\": \"\", \"completed_at\": \"2026-05-14T09:46:00.917Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T09:46:02.621139+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T10:38:15.900825+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"第二次启动失败。根因：config reward_mode=execution_sta (0.5*exec+0.5*ISR) 可能与 FOL 实验不匹配，待 Director 确认后修复重启。cuda:1 释放给 plan018。\"}}, \"account\": \"root\", \"notes\": \"Eval metrics provenance: eval 在训练完成后立即在 westd-39279 服务器上运行 eval_sta.py，checkpoint 路径 /root/autodl-tmp/outputs/plan006_prolog_sta_s42/。Eval 结果由 Worker 从服务器 SSH 读取 eval_results.json 并手动录入 registry。Checkpoint 可能已被磁盘清理删除（C003 save_total_limit=1）。训练日志: ~/runs/solver-trace-ablation/plan006-prolog-sta-s42.log。H7 分类由 classify_h7.py 在 eval 目录上运行。\", \"spec\": {\"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"account\": \"root\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_prolog_exec_sta.yaml --num_steps 500 --seed 42 --output_dir /root/autodl-tmp/outputs/plan006_prolog_sta_s42\\\"\", \"pid\": \"506117\", \"log_path\": \"~/runs/solver-trace-ablation/plan006-prolog-sta-s42.log\", \"data_path\": \"data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan006_prolog_sta_s42/ (may be cleaned up per C003)\", \"metrics\": {\"cumulative_prove_rate\": 0.848, \"cumulative_mean_isr\": 0.787, \"final_prove_rate\": 1, \"final_isr\": 1, \"final_reward\": 1, \"saturation_onset_step\": 100, \"train_loss\": 0.00716, \"training_hours\": 0.78, \"final_entropy\": 0.01, \"final_completion_length\": 27, \"initial_completion_length\": 120, \"steps_at_perfect_reward\": 400, \"train_runtime_sec\": 2791, \"eval_prove_rate\": 0.5, \"eval_mean_isr\": 0.5, \"eval_proved_only_isr\": 1, \"eval_h7_rate\": 1, \"eval_h7_count\": 50, \"eval_proved_count\": 50, \"eval_total_count\": 100, \"eval_n_clauses_mean\": 1, \"eval_isr_distribution\": \"binary: 50x0 + 50x1\"}}, \"plan006-prolog-sta-s43\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-14T09:19:39.141Z\", \"updated_at\": \"2026-05-14T16:36:42.509Z\", \"hypothesis\": \"Prolog exec+STA GRPO seed=43: 跨 seed 稳定性检查。与 exec-only s43 对照。\", \"notes\": \"PREPARING. 命令模板已修正：去掉 --warmup_ratio，与 sta-s42 (warmup_ratio=0.0) 一致。Config: configs/grpo_prolog_exec_sta.yaml + seed=43. Output: /root/autodl-tmp/outputs/plan006_prolog_sta_s43. 等 GPU 释放。\", \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_prolog_exec_sta.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 43 --output_dir /root/autodl-tmp/outputs/plan006_prolog_sta_s43\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"pid\": \"901135\", \"log_path\": \"~/runs/solver-trace-ablation/plan006-prolog-sta-s43.log\", \"submitted_at\": \"2026-05-14T16:36:41.878Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"pid\": \"901135\", \"log_path\": \"~/runs/solver-trace-ablation/plan006-prolog-sta-s43.log\", \"reproduce\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_prolog_exec_sta.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 43 --output_dir /root/autodl-tmp/outputs/plan006_prolog_sta_s43\\\"\"}}, \"plan001-exec-only-s44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T03:57:09.690Z\", \"updated_at\": \"2026-05-14T16:29:02.086Z\", \"hypothesis\": \"Exec-only seed=44 第3 seed: 解决 s42(93% eval PR) vs s43(13% eval PR) 的跨 seed 不稳定问题，3-seed mean±std 是论文必需。\", \"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 44 --output_dir /root/autodl-tmp/outputs/plan001_exec_only_s44\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"226200\", \"log_path\": \"~/runs/solver-trace-ablation/plan001-exec-only-s44.log\", \"submitted_at\": \"2026-05-14T04:29:05.471Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 2725.5, \"gpu_hours\": 0.76}, \"pid\": \"226200\", \"log_path\": \"~/runs/solver-trace-ablation/plan001-exec-only-s44.log\", \"reproduce\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 44 --output_dir /root/autodl-tmp/outputs/plan001_exec_only_s44\\\"\", \"finished_at\": \"2026-05-14T05:06:39.227Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T05:06:40.707032+00:00\"}]}, \"metrics\": {\"eval_prove_rate\": 0.98, \"eval_mean_isr\": 0.57, \"eval_isr_std\": 0.2013, \"eval_median_isr\": 0.5, \"eval_proved_only_isr\": 0.5816, \"eval_n_proved\": 98, \"eval_n_problems\": 100, \"eval_method\": \"eval_sta.py full STA\", \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_component_count_mean\": 2.04, \"eval_component_count_2\": 94, \"eval_component_count_3\": 4, \"tautological_collapse\": true, \"h7_rate\": 1, \"h7_count\": 97, \"h1_rate\": 0, \"h1_count\": 0, \"genuine_rate\": 0, \"genuine_count\": 0, \"conclusion_embedding_total\": 1}, \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan001_exec_only_s44\", \"conclusion\": \"negative\", \"notes\": \"TAUTOLOGICAL COLLAPSE 确认。eval PR=98% 但 94% 样本仅 2 components (premise=conclusion tautology)，mean components=2.04，与 plan013 random reward 完全一致。ISR≈0.5 是 2-component artifact。s42 是唯一产生 genuine proofs (mean components=6.58) 的 seed。3-seed 结果：s42=genuine, s43=degraded(PR=13%), s44=tautological(PR=98% fake)。Exec-only reward 2/3 seeds 失败。\", \"completed_at\": \"2026-05-14T05:14:30.940Z\"}, \"plan001-exec-only-s42-r2\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-13T22:40:41.773Z\", \"updated_at\": \"2026-05-14T16:28:58.538Z\", \"completed_at\": \"2026-05-13T23:46:00Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\"}, \"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-13T23:46:01.596431+00:00\"}]}, \"spec\": {\"command\": \"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --num_steps 500 --seed 42 --output_dir /root/autodl-tmp/outputs/plan001_exec_only_s42\", \"server\": \"westd-39279\", \"data_path\": \"/root/solver-trace-ablation/data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"500-step exec-only baseline for STA comparison (K=8)\", \"pid\": \"84901\", \"gpu\": [\"cuda:0\"], \"log_path\": \"~/runs/solver-trace-ablation/plan001-exec-only-s42-r2.log\", \"submitted_at\": \"2026-05-13T22:42:40.204Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 3820, \"gpu_hours\": 1.06}, \"notes\": \"Cron 误判 DONE/failed（因 --help|grep 前缀命令的 PID 84896 退出，实际训练子进程 PID 84901 仍在运行）。已手动恢复 RUNNING。严禁在 cuda:0 启动新进程直到 r2 自然完成。⚠️ Reviewer 中期审查标注: 训练日志中 ISR=0.8612 为 binary approximation (_fast_fn)，非真实 ISR。最终可比 ISR 需通过 eval_sta.py (full STA) 重新评估。\", \"reproduce\": {\"finished_at\": \"2026-05-13T23:46:00.369Z\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan001_exec_only_s42/checkpoint-500\", \"log_path\": \"/root/autodl-tmp/outputs/plan001_exec_only_s42/reward_log.jsonl\", \"metrics\": {\"eval_prove_rate\": 0.93, \"eval_mean_isr\": 0.1232, \"eval_isr_std\": 0.1887, \"eval_proved_only_isr\": 0.1324, \"eval_median_isr\": 0, \"eval_n_proved\": 93, \"eval_n_problems\": 100, \"eval_method\": \"eval_sta.py full STA\", \"eval_data\": \"proofwriter_fol_100.jsonl\", \"h7_rate\": 0, \"h7_count\": 0, \"h1_rate\": 0.871, \"h1_count\": 81, \"genuine_rate\": 0.129, \"genuine_count\": 12, \"genuine_mean_isr\": 0.3141, \"h1_mean_isr\": 0.1055, \"conclusion_embedding_total\": 0.871}}, \"plan006-prolog-exec-s44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T07:13:35.647Z\", \"updated_at\": \"2026-05-14T16:27:18.570Z\", \"hypothesis\": \"Prolog exec-only GRPO seed=44: third seed for Prolog exec-only. Together with s42 (PR=83%, ISR=0.031) and s43, provides 3-seed evidence for cross-logic generalization claim (Claim 3). 3-seed mean±std required for paper.\", \"notes\": \"Eval 完成。PR=21% (3-seed 最低), ISR=0.081, proved_only_ISR=0.387 (max_ISR=1.0)。与 s42/s43 不同模式：PR 极低但 proved_only_ISR 较高，可能有少量样本 ISR=1 (H7-like)。Prolog exec-only 3-seed 汇总：s42 PR=83%/ISR=0.031, s43 PR=56%/ISR=0.008, s44 PR=21%/ISR=0.081。Mean PR=53.3%±31.1%, Mean ISR=0.040±0.037。跨 seed 极不稳定（PR std=31pp），与 FOL exec-only 一致。ISR 始终极低（<0.1），确认 Prolog exec-only 不产生 genuine reasoning traces。\", \"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-14T13:43:55.707Z\", \"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_prolog_exec_only.yaml --num_steps 500 --seed 44 --output_dir /root/autodl-tmp/outputs/plan006_prolog_exec_s44\\\"\", \"finished_at\": \"2026-05-14T15:20:42.126Z\", \"training_hours\": 1.61}, \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_prolog_exec_only.yaml --num_steps 500 --seed 44 --output_dir /root/autodl-tmp/outputs/plan006_prolog_exec_s44\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"479357\", \"log_path\": \"~/runs/solver-trace-ablation/plan006-prolog-exec-s44.log\", \"submitted_at\": \"2026-05-14T13:43:57.850Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 9800.7, \"gpu_hours\": 2.72}, \"pid\": \"479357\", \"log_path\": \"~/runs/solver-trace-ablation/plan006-prolog-exec-s44.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T15:20:44.093424+00:00\"}]}, \"metrics\": {\"eval_prove_rate\": 0.21, \"eval_mean_isr\": 0.0812, \"eval_isr_std\": 0.2343, \"eval_median_isr\": 0, \"eval_proved_only_isr\": 0.3866, \"eval_min_isr\": 0, \"eval_max_isr\": 1, \"eval_n_proved\": 21, \"eval_n_problems\": 100, \"eval_method\": \"eval_sta.py full STA\", \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_elapsed_seconds\": 683.9, \"eval_by_type_false_pr\": 0.04, \"eval_by_type_false_isr\": 0.04, \"eval_by_type_unknown_pr\": 0.317, \"eval_by_type_unknown_isr\": 0.099, \"eval_by_type_true_pr\": 0.206, \"eval_by_type_true_isr\": 0.09, \"solver\": \"PrologSolver\", \"logic_type\": \"prolog\"}, \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan006_prolog_exec_s44/checkpoint-500\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-14T16:27:18.570Z\"}, \"plan009-sft-baseline-s42-r4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T11:40:28.142Z\", \"updated_at\": \"2026-05-14T16:27:01.864Z\", \"hypothesis\": \"SFT baseline: supervised finetuning on FOLIO data (500 steps, Qwen3-4B, same model as all GRPO experiments) to establish whether hacking patterns are GRPO-specific or general finetuning artifacts. r4: fix CUDA_VISIBLE_DEVICES + --gpu + --no_wandb.\", \"parent\": \"plan009-sft-baseline-s42-r2\", \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_sft.py --model_path /root/autodl-tmp/models/Qwen3-4B --data_path data/train_500_seed42.jsonl --output_dir /root/autodl-tmp/outputs/plan009_sft_baseline_s42 --num_steps 500 --seed 42 --no_wandb --gpu 1\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"account\": \"root\", \"data_path\": \"data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan009_sft_baseline_s42/checkpoint-500/\"}, \"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"notes\": \"r4 训练完成 (500 steps, TRL SFT). Checkpoint 实际保存在 plan009_sft_baseline_s42（非 plan009_sft_s42_r4）。两卡满载 (cuda:0 80GB, cuda:1 80GB)，eval 待 GPU 释放。checkpoint-500/ 含 15GB optimizer.pt 可在 eval 后清理。\", \"reproduce\": {\"finished_at\": \"2026-05-14T12:18:55.639Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T12:18:57.313588+00:00\"}]}, \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan009_sft_baseline_s42/checkpoint-500/\", \"log_path\": \"/root/autodl-tmp/outputs/plan009_sft_baseline_s42/checkpoint-500/trainer_state.json\", \"metrics\": {\"eval_prove_rate\": 0.14, \"eval_mean_isr\": 0.08, \"eval_isr_std\": 0.214, \"eval_median_isr\": 0, \"eval_max_isr\": 0.833, \"eval_proved_only_isr\": 0.571, \"eval_n_proved\": 14, \"eval_n_problems\": 100, \"eval_method\": \"eval_sta.py full STA\", \"eval_data\": \"proofwriter_fol_100.jsonl\", \"train_final_loss\": 0.0287, \"train_token_accuracy\": 0.9935, \"train_epochs\": 7.94, \"train_runtime_sec\": 789.6, \"by_answer_type\": {\"true\": {\"count\": 34, \"proved\": 13, \"pr\": 0.382, \"isr\": 0.226}, \"unknown\": {\"count\": 41, \"proved\": 1, \"pr\": 0.024, \"isr\": 0.008}, \"false\": {\"count\": 25, \"proved\": 0, \"pr\": 0, \"isr\": 0}}, \"h7_rate\": 0, \"h7_count\": 0, \"h1_rate\": 0.071, \"h1_count\": 1, \"genuine_rate\": 0.929, \"genuine_count\": 13, \"hacking_patterns\": \"near-zero (1/14 H1, 0 H7, 92.9% genuine)\", \"tautological_collapse\": false}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-14T14:20:25.035Z\"}, \"plan006-prolog-exec-s43-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:38:23.818Z\", \"updated_at\": \"2026-05-14T16:16:56.523Z\", \"hypothesis\": \"Prolog exec-only GRPO seed=43 r3: warmup_ratio=0.0 与 s42 一致。r2 因残留进程 OOM 失败，cuda:1 已清理。\", \"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-14T13:44:06.728Z\", \"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_prolog_exec_only.yaml --num_steps 500 --seed 43 --output_dir /root/autodl-tmp/outputs/plan006_prolog_exec_s43_r3\\\"\", \"finished_at\": \"2026-05-14T15:54:25.754Z\", \"training_hours\": 2.17}, \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_prolog_exec_only.yaml --num_steps 500 --seed 43 --output_dir /root/autodl-tmp/outputs/plan006_prolog_exec_s43_r3\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"pid\": \"483820\", \"log_path\": \"~/runs/solver-trace-ablation/plan006-prolog-exec-s43-r3.log\", \"submitted_at\": \"2026-05-14T13:44:08.516Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 9168.0, \"gpu_hours\": 2.55}, \"pid\": \"483820\", \"log_path\": \"~/runs/solver-trace-ablation/plan006-prolog-exec-s43-r3.log\", \"notes\": \"Eval 完成。PR=56% (远低于 s42 的 83%), ISR=0.0084 (与 s42 的 0.031 同量级，均极低)。proved_only_ISR=0.015。Prolog exec-only 跨 seed 表现：s42 PR=83%/ISR=0.031, s43 PR=56%/ISR=0.008。s43 prove_rate 显著下降但 ISR 模式一致（极低，ground fact enumeration hacking）。与 FOL exec-only 类似，存在跨 seed 不稳定性（FOL: s42=93%, s43=14%, s44=98%）。等 s44 eval 完成后计算 3-seed mean±std。\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T15:54:27.521808+00:00\"}]}, \"metrics\": {\"eval_prove_rate\": 0.56, \"eval_mean_isr\": 0.0084, \"eval_isr_std\": 0.0221, \"eval_median_isr\": 0, \"eval_proved_only_isr\": 0.015, \"eval_min_isr\": 0, \"eval_max_isr\": 0.1, \"eval_n_proved\": 56, \"eval_n_problems\": 100, \"eval_method\": \"eval_sta.py full STA\", \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_elapsed_seconds\": 868.2, \"eval_by_type_false_pr\": 0.48, \"eval_by_type_false_isr\": 0.0043, \"eval_by_type_unknown_pr\": 0.6585, \"eval_by_type_unknown_isr\": 0.0114, \"eval_by_type_true_pr\": 0.5, \"eval_by_type_true_isr\": 0.0078, \"solver\": \"PrologSolver\", \"logic_type\": \"prolog\"}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan006_prolog_exec_s43_r3/checkpoint-500\", \"completed_at\": \"2026-05-14T16:16:56.523Z\"}, \"plan002-additive-b01-s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T05:29:08.138Z\", \"updated_at\": \"2026-05-14T15:09:40.467Z\", \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_bonus.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 42 --beta 0.1 --reward_mode additive_bonus --output_dir /root/autodl-tmp/outputs/plan002_additive_b01_s42\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"262261\", \"log_path\": \"~/runs/solver-trace-ablation/plan002-additive-b01-s42.log\", \"submitted_at\": \"2026-05-14T05:32:32.415Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"plan_id\": \"plan002\", \"reward_formula\": \"r_exec * (1 + 0.1 * ISR)\", \"num_steps\": 500, \"wall_clock_seconds\": 4493.9, \"gpu_hours\": 1.25, \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan002_additive_b01_s42\"}, \"parent\": \"plan002-additive-b03-s42\", \"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"pid\": \"262261\", \"log_path\": \"~/runs/solver-trace-ablation/plan002-additive-b01-s42.log\", \"reproduce\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_bonus.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 42 --beta 0.1 --reward_mode additive_bonus --output_dir /root/autodl-tmp/outputs/plan002_additive_b01_s42\\\"\", \"finished_at\": \"2026-05-14T06:37:58.285Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T06:37:59.656631+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"eval_prove_rate\": 0.81, \"eval_mean_isr\": 0.3365, \"eval_isr_std\": 0.3227, \"eval_proved_only_isr\": 0.4154, \"eval_median_isr\": 0.2, \"eval_n_proved\": 81, \"eval_n_problems\": 100, \"eval_method\": \"eval_sta.py full STA\", \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_component_count_mean\": 5.58, \"eval_component_count_2_ratio\": 0.037, \"eval_isr_1_ratio\": 0.124, \"eval_isr_0_ratio\": 0.037, \"eval_by_type_false_pr\": 0.88, \"eval_by_type_false_isr\": 0.3515, \"eval_by_type_unknown_pr\": 0.83, \"eval_by_type_unknown_isr\": 0.3684, \"eval_by_type_true_pr\": 0.74, \"eval_by_type_true_isr\": 0.2869, \"tautological_collapse\": false, \"train_total_steps\": 500, \"train_duration_min\": 63, \"train_last100_pr\": 0.6875, \"train_last100_isr\": 0.1954, \"train_last100_loss\": 0.015}, \"notes\": \"H7 audit (2026-05-14): 81 proved samples. H7 (single premise=conclusion): 13/81=16.0%, mean ISR=0.6603. H1 (multi premise contains conclusion): 42/81=51.9%, mean ISR=0.2245. Genuine (no conclusion duplication): 26/81=32.1%, mean ISR=0.6014. Combined conclusion duplication = 67.9%. CRITICAL: only 32.1% of proved samples are free of conclusion embedding. H7 inflates ISR; H1 deflates ISR but proof is trivially achievable via embedded conclusion. Claim 2 \\\"genuine structural guidance\\\" needs reframing — ISR signal is dominated by conclusion duplication artifacts.\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan002_additive_b01_s42\", \"completed_at\": \"2026-05-14T06:47:26.358Z\"}, \"plan018-additive-random-b01-s44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T08:36:18.722Z\", \"updated_at\": \"2026-05-14T15:00:09.178Z\", \"hypothesis\": \"Random β=0.1 seed=44 控制组：与 plan002-b01-s44 (ISR β=0.1) 同 seed 对照。验证 ISR 3.2x > random 的结论在 s44 下是否成立。\", \"parent\": \"plan018-additive-random-b01-s42\", \"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-14T11:34:13.338Z\", \"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_random_b01.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 44 --beta 0.1 --reward_mode additive_random --output_dir /root/autodl-tmp/outputs/plan018_additive_random_b01_s44\\\"\", \"finished_at\": \"2026-05-14T13:37:42.200Z\", \"training_hours\": 2.06}, \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_random_b01.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 44 --beta 0.1 --reward_mode additive_random --output_dir /root/autodl-tmp/outputs/plan018_additive_random_b01_s44\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"564900\", \"data_path\": \"data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 44, \"reward_formula\": \"r = r_exec * (1 + 0.1 * random[0,1])\", \"num_steps\": 500}, \"pid\": \"564900\", \"log_path\": \"~/runs/solver-trace-ablation/plan018-additive-random-b01-s44.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T13:37:43.236026+00:00\"}]}, \"metrics\": {\"prove_rate\": 0.89, \"mean_isr\": 0.0619, \"isr_std\": 0.1756, \"median_isr\": 0, \"proved_only_mean_isr\": 0.0695, \"n_proved\": 89, \"n_problems\": 100, \"max_isr\": 1, \"min_isr\": 0, \"isr_pr_ratio\": 0.0695, \"isr_zero_count\": 72, \"isr_one_count\": 2, \"by_answer_type\": {\"false\": {\"count\": 25, \"proved\": 21, \"prove_rate\": 0.84, \"mean_isr\": 0.0533}, \"unknown\": {\"count\": 41, \"proved\": 40, \"prove_rate\": 0.976, \"mean_isr\": 0.0892}, \"true\": {\"count\": 34, \"proved\": 28, \"prove_rate\": 0.824, \"mean_isr\": 0.0353}}, \"elapsed_seconds\": 1012.7, \"eval_method\": \"eval_sta.py with Prover9Solver, FOL\"}, \"conclusion\": \"success\", \"notes\": \"DONE (success). Random β=0.1 s44 对照分析完成: PR=0.89/ISR=0.062 (clean) vs ISR β=0.1 s44 PR=0.89/ISR=0.803 (H7=86.5% inflated). 同 PR 下 ISR reward 导致 conclusion duplication，random 无此问题。与 s42 结论一致: ISR s42 genuine ISR=0.337 vs Random s42 ISR=0.104 (3.2x)。Random 2/3 seeds done, 等 s43 (plan018-random-b01-s43-r2 QUEUED)。\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan018_additive_random_b01_s44/checkpoint-500\", \"completed_at\": \"2026-05-14T14:29:21.226Z\"}, \"plan009-sft-baseline-s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T10:51:58.328Z\", \"updated_at\": \"2026-05-14T14:20:43.363Z\", \"hypothesis\": \"SFT baseline: supervised finetuning on FOLIO data (500 steps, Qwen3-4B) to establish whether hacking patterns are GRPO-specific or general finetuning artifacts. Same model as all GRPO experiments for fair comparison.\", \"conclusion\": \"killed\", \"notes\": \"模型必须改为 Qwen3-4B（与 GRPO 实验一致）。用 Qwen2.5-1.5B 无法作为 fair baseline——模型不同无法隔离训练方法差异。修正模型后重新注册提交。\", \"completed_at\": \"2026-05-14T14:20:42.452Z\"}, \"plan006-prolog-exec-s43-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T12:32:37.140Z\", \"updated_at\": \"2026-05-14T13:43:01.701Z\", \"hypothesis\": \"Prolog exec-only GRPO seed=43 r2: 修正 warmup_ratio=0.0 与 s42 一致。cross-seed stability check for Prolog logic type.\", \"parent\": \"plan006-prolog-exec-s43\", \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_prolog_exec_only.yaml --num_steps 500 --seed 43 --output_dir /root/autodl-tmp/outputs/plan006_prolog_exec_s43_r2\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"pid\": \"712243\", \"log_path\": \"~/runs/solver-trace-ablation/plan006-prolog-exec-s43-r2.log\", \"submitted_at\": \"2026-05-14T12:33:05.887Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 136.2, \"gpu_hours\": 0.04}, \"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"pid\": \"712243\", \"log_path\": \"~/runs/solver-trace-ablation/plan006-prolog-exec-s43-r2.log\", \"reproduce\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_prolog_exec_only.yaml --num_steps 500 --seed 43 --output_dir /root/autodl-tmp/outputs/plan006_prolog_exec_s43_r2\\\"\", \"finished_at\": \"2026-05-14T12:35:20.730Z\"}, \"failure_reason\": \"CUDA OOM: CUDA out of memory. Tried to allocate 48.00 MiB. GPU 0 has a total capacity of 94.97 GiB of which 40.25 MiB is free. Process 587160 has 78.09 GiB memory in use. Including non-PyTorch memory, this process has 16.83 GiB memory in use. Of the allocated \", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-14T12:35:22.121Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T12:35:23.802887+00:00\"}]}, \"notes\": \"OOM 诊断：非 batch size 问题。根因是 kill_job 只杀了 tmux 包装进程 (PID 587155)，训练子进程 587159/587160 残留在 cuda:1 上占 78.09 GiB 显存。s43-r2 启动时 cuda:1 仅剩 40 MiB free，首次前向传播即 OOM (尝试分配 48 MiB)。教训：kill_job 后必须 SSH 确认子进程也已终止（ps aux grep + nvidia-smi），不能只看 PID 返回成功。\"}, \"plan006-prolog-exec-s42\": {\"status\": \"DONE\", \"retry_count\": 2, \"created_at\": \"2026-05-14T07:13:34.169Z\", \"updated_at\": \"2026-05-14T12:33:17.845Z\", \"hypothesis\": \"Prolog exec-only GRPO seed=42: STA/ISR hacking patterns generalize across logic types? Prolog uses rule ablation (vs FOL axiom ablation). If same degeneration modes appear → STA is logic-agnostic diagnostic.\", \"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"reproduce\": {\"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-14T09:49:36.534Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_prolog_exec_only.yaml --num_steps 500 --seed 42 --output_dir /root/autodl-tmp/outputs/plan006_prolog_exec_s42\\\"\", \"finished_at\": \"2026-05-14T11:29:25.346Z\", \"training_hours\": 1.66}, \"failure_reason\": \"\", \"completed_at\": \"2026-05-14T09:47:36.390Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T09:47:38.546001+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T11:29:27.709792+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"失败原因: FileNotFoundError — data/prolog/train_500_seed42.jsonl 不存在 | error_type: data | 同一原因影响所有 plan006 实验 (exec/sta × s42/s43/s44) | 建议: 需先生成 Prolog 训练数据再重试\"}}, \"account\": \"root\", \"notes\": \"Eval (eval_sta.py) 完成。PR=83%, mean_ISR=0.031, proved_only_ISR=0.037, H7=0%, H1=0%。与 sta-s42 (PR=50%, ISR=1.0, H7=100%) 形成鲜明对比。exec-only 产生完全不同的 hacking 模式：ground fact enumeration（倾泻大量无关 ground facts，query 作为其中一个 fact 平凡成功），而非 sta-s42 的 tautological collapse。两种 reward signal 驱动两种不同的 hacking 策略。对论文是 positive finding：强化 Claim 1 且揭示 reward-specific hacking 机制。\", \"spec\": {\"command\": \"python3 scripts/train_grpo.py --config configs/grpo_prolog_exec_only.yaml --num_steps 500 --seed 42 --output_dir /root/autodl-tmp/outputs/plan006_prolog_exec_s42\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"506020\", \"data_path\": \"data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42}, \"metrics\": {\"eval_prove_rate\": 0.83, \"eval_mean_isr\": 0.031, \"eval_proved_only_isr\": 0.037, \"eval_median_isr\": 0, \"eval_max_isr\": 0.2, \"eval_isr_std\": 0.0534, \"h7_rate\": 0, \"h1_rate\": 0, \"isr_1_rate\": 0, \"single_premise_rate\": 0, \"by_answer_type\": {\"true\": {\"proved\": 37, \"count\": 40, \"pr\": 0.925, \"isr\": 0.037}, \"false\": {\"proved\": 21, \"count\": 29, \"pr\": 0.724, \"isr\": 0.038}, \"unknown\": {\"proved\": 25, \"count\": 31, \"pr\": 0.806, \"isr\": 0.016}}}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan006_prolog_exec_s42/checkpoint-500\", \"log_path\": \"~/runs/solver-trace-ablation/plan006-prolog-exec-s42.log\"}, \"plan006-prolog-exec-s43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T07:13:35.078Z\", \"updated_at\": \"2026-05-14T12:32:13.799Z\", \"hypothesis\": \"Prolog exec-only GRPO seed=43: cross-seed stability check for Prolog logic type. FOL showed extreme cross-seed variance (s42 genuine vs s43 degraded vs s44 tautological). Prolog exec-only s42 showed PR=83%, ISR=0.031. s43 tests if Prolog also has seed instability.\", \"notes\": \"KILLED at step 36/500: warmup_ratio=0.1 与 s42 (0.0) 不一致，3-seed 对比无效。重启为 plan006-prolog-exec-s43-r2 (warmup_ratio=0.0)。\", \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_prolog_exec_only.yaml --num_steps 500 --seed 43 --output_dir /root/autodl-tmp/outputs/plan006_prolog_exec_s43 --warmup_ratio 0.1\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"pid\": \"587155\", \"log_path\": \"~/runs/solver-trace-ablation/plan006-prolog-exec-s43.log\", \"submitted_at\": \"2026-05-14T12:22:08.915Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 43, \"wall_clock_seconds\": 602.2, \"gpu_hours\": 0.17}, \"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"pid\": \"587155\", \"log_path\": \"~/runs/solver-trace-ablation/plan006-prolog-exec-s43.log\", \"reproduce\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_prolog_exec_only.yaml --num_steps 500 --seed 43 --output_dir /root/autodl-tmp/outputs/plan006_prolog_exec_s43 --warmup_ratio 0.1\\\"\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-14T12:32:11.136Z\"}, \"plan009-sft-baseline-s42-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T11:37:49.306Z\", \"updated_at\": \"2026-05-14T11:48:05.087Z\", \"hypothesis\": \"SFT baseline: supervised finetuning on FOLIO data (500 steps, Qwen3-4B, same model as all GRPO experiments) to establish whether hacking patterns are GRPO-specific or general finetuning artifacts. Compare eval PR/ISR/hacking taxonomy against GRPO exec-only and exec+ISR conditions.\", \"parent\": \"plan009-sft-baseline-s42-r2\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_sft.py --model_path /root/autodl-tmp/models/Qwen3-4B --data_path data/train_500_seed42.jsonl --output_dir /root/autodl-tmp/outputs/plan009_sft_s42_r3 --num_steps 500 --seed 42 --bf16 --wandb_project solver-trace-ablation --wandb_run plan009-sft-s42-r3\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"pid\": \"566690\", \"log_path\": \"~/runs/solver-trace-ablation/plan009-sft-baseline-s42-r3.log\", \"submitted_at\": \"2026-05-14T11:39:19.395Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 18.5, \"gpu_hours\": 0.01}, \"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"pid\": \"566690\", \"log_path\": \"~/runs/solver-trace-ablation/plan009-sft-baseline-s42-r3.log\", \"wandb_run_id\": \"plan009-sft-s42-r3\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_sft.py --model_path /root/autodl-tmp/models/Qwen3-4B --data_path data/train_500_seed42.jsonl --output_dir /root/autodl-tmp/outputs/plan009_sft_s42_r3 --num_steps 500 --seed 42 --bf16 --wandb_project solver-trace-ablation --wandb_run plan009-sft-s42-r3\\\"\", \"wandb_run_id\": \"plan009-sft-s42-r3\", \"finished_at\": \"2026-05-14T11:39:36.697Z\"}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-14T11:39:37.935Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T11:39:39.416777+00:00\"}]}, \"notes\": \"r3 crash root cause: wandb.init() failed because no W&B API key configured on server (no .netrc, no WANDB_API_KEY). Fix: add --no_wandb flag. Secondary issue: both GPUs currently near-full, need to wait for GPU availability before r4. Correct r4 command: export CUDA_VISIBLE_DEVICES=N && ... python3 scripts/train_sft.py --model_path /root/autodl-tmp/models/Qwen3-4B --data_path data/train_500_seed42.jsonl --output_dir /root/autodl-tmp/outputs/plan009_sft_s42_r4 --num_steps 500 --seed 42 --no_wandb\"}, \"plan009-sft-baseline-s42-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T11:02:25.369Z\", \"updated_at\": \"2026-05-14T11:43:20.347Z\", \"hypothesis\": \"SFT baseline: supervised finetuning on FOLIO data (500 steps, Qwen3-4B, same model as all GRPO experiments) to establish whether hacking patterns are GRPO-specific or general finetuning artifacts. Compare eval PR/ISR/hacking taxonomy against GRPO exec-only and exec+ISR conditions.\", \"plan_id\": \"plan_009\", \"notes\": \"SFT baseline with Qwen3-4B (same model as GRPO experiments). Replaces killed plan009-sft-baseline-s42 which incorrectly used Qwen2.5-1.5B. cuda:1, seed=42, 500 steps, FOLIO data (data/train_500_seed42.jsonl). Dream 审稿三档均指出缺 SFT baseline 是 gap。**FAILED**: 两个问题：(1) W&B API key 未配置，trainer.train() 启动时 wandb callback 报 UsageError; (2) device_map='auto' 把模型分到多 GPU，需改为单卡绑定。修复方案：加 WANDB_MODE=disabled + 改 train_sft.py 的 device_map 为单卡。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_sft.py --model_path /root/autodl-tmp/models/Qwen3-4B --data_path data/train_500_seed42.jsonl --output_dir /root/autodl-tmp/outputs/plan009_sft_baseline_s42 --num_steps 200 --seed 42 --no_wandb\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"pid\": \"548527\", \"log_path\": \"~/runs/solver-trace-ablation/plan009-sft-baseline-s42-r2.log\", \"submitted_at\": \"2026-05-14T11:08:22.511Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"wall_clock_seconds\": 236.8, \"gpu_hours\": 0.07}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-14T11:12:19.306Z\", \"failure_reason\": \"OOM: 缺少 CUDA_VISIBLE_DEVICES 显式设置，device_map='auto' 跨 GPU 侵入 cuda:0 (plan006)，导致双卡 OOM。修复：(1) 启动命令加 --gpu 1，(2) device_map 改为 {\\\"\\\": 0} 或 .to(\\\"cuda\\\")，(3) num_steps 改为 500\"}, \"plan018-additive-random-b01-s43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T08:36:18.260Z\", \"updated_at\": \"2026-05-14T11:42:09.950Z\", \"hypothesis\": \"Random β=0.1 seed=43 控制组：与 plan002-b01-s43 (ISR β=0.1) 同 seed 对照。验证 ISR 3.2x > random 的结论在 s43 下是否成立。\", \"parent\": \"plan018-additive-random-b01-s42\", \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_random_b01.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 43 --beta 0.1 --reward_mode additive_random --output_dir /root/autodl-tmp/outputs/plan018_additive_random_b01_s43\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"pid\": \"540910\", \"log_path\": \"~/runs/solver-trace-ablation/plan018-additive-random-b01-s43.log\", \"submitted_at\": \"2026-05-14T10:58:27.110Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 43, \"checkpoint_source\": \"plan018-additive-random-b01-s42\", \"eval_data\": \"data/train_500_seed42.jsonl\", \"wall_clock_seconds\": 1929.4, \"gpu_hours\": 0.54}, \"reproduce\": {\"finished_at\": \"2026-05-14T11:30:34.690Z\"}, \"failure_reason\": \"磁盘满 (No space left on device): /root/autodl-tmp/ 250G/250G 100% 占满。训练在 step 200/500 保存 checkpoint-200 时 safetensors 序列化失败 (os error 28)。根因: 多个已完成实验的 checkpoint 未清理。可重试——清理磁盘后重跑。\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-14T11:30:36.549Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T11:30:40.886615+00:00\"}]}, \"notes\": \"Disk full (os error 28) at step 200/500 during checkpoint save. Training ran fine for 200 steps but safetensors serialization failed with \\\"No space left on device\\\". No checkpoint saved. Disk now has 109G free. Retryable as-is.\"}, \"plan002-additive-b01-s44\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T08:36:17.298Z\", \"updated_at\": \"2026-05-14T10:12:40.545Z\", \"hypothesis\": \"ISR β=0.1 seed=44 多 seed 验证：exec-only s44 是 tautological collapse (PR=98%, ISR=0.57 fake)，ISR β=0.1 能否防止 tautological collapse？3-seed mean±std 用于论文 Claim 2。\", \"parent\": \"plan002-additive-b01-s42\", \"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-14T08:45:11.826Z\", \"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_bonus.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 44 --beta 0.1 --reward_mode additive_bonus --output_dir /root/autodl-tmp/outputs/plan002_additive_b01_s44\\\"\", \"finished_at\": \"2026-05-14T09:28:10.836Z\", \"training_hours\": 0.72}, \"spec\": {\"command\": \"python3 scripts/train_grpo.py --mode additive_bonus --isr_beta 0.1 --seed 44\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"pid\": \"466540\", \"log_path\": \"~/runs/solver-trace-ablation/plan002-additive-b01-s44.log\", \"submitted_at\": \"2026-05-14T08:46:23.037Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 44, \"wall_clock_seconds\": 2950.3, \"gpu_hours\": 0.82}, \"pid\": \"466540\", \"log_path\": \"~/runs/solver-trace-ablation/plan002-additive-b01-s44.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T09:28:12.416418+00:00\"}]}, \"metrics\": {\"eval_prove_rate\": 0.89, \"eval_mean_isr\": 0.803, \"eval_isr_std\": 0.3418, \"eval_median_isr\": 1, \"component_count_mean\": 4.33, \"component_count_2_ratio\": 0.022, \"tautological_collapse\": false, \"isr_0_ratio\": 0.12, \"isr_1_ratio\": 0.73, \"proved_single_premise_ratio\": 1, \"h7_rate_calibrated\": 0.865, \"h7_definition\": \"single_premise AND premise==conclusion (normalized)\", \"hacking_mode\": \"conclusion_duplication_isr_inflation\", \"conclusion_embedding\": true, \"component_dist\": {\"2\": 2, \"4\": 54, \"5\": 33}, \"by_answer_type\": {\"false\": {\"n\": 25, \"proved\": 22, \"PR\": 0.88, \"ISR\": 0.824}, \"unknown\": {\"n\": 41, \"proved\": 38, \"PR\": 0.927, \"ISR\": 0.837}, \"true\": {\"n\": 34, \"proved\": 29, \"PR\": 0.853, \"ISR\": 0.747}}}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan002_additive_b01_s44\", \"notes\": \"RECLASSIFIED negative (D039): Reviewer 逐样本审查发现 semantic drift hacking — 模型生成极简形式化（单 premise≈conclusion），通过 conclusion sub-component ablation 膨胀 ISR。ISR=0.902 是 conclusion_duplication_isr_inflation artifact，非真正证明质量。65% 样本 ISR=1.0 为 conclusion embedding。此 hacking mode 本身是论文 positive finding（强化 Claim 1 Goodhart 叙事：ISR reward 导致新型 hacking）。原始 eval 指标：PR=0.89, mean_isr=0.803, component_mean=4.33, comp_2_ratio=0.022。exec-only s44 是 tautological collapse (94% 2-comp)，ISR β=0.1 s44 避免了 tautological collapse 但转向了 conclusion duplication hacking。\", \"completed_at\": \"2026-05-14T09:35:33.310Z\"}, \"plan002-additive-b01-s43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T08:36:16.367Z\", \"updated_at\": \"2026-05-14T10:12:36.502Z\", \"hypothesis\": \"ISR β=0.1 seed=43 多 seed 验证：plan002-b01-s42 (PR=0.81, ISR=0.337) 在 s43 下是否可复现？exec-only s43 是 degraded seed (PR=14%)，ISR β=0.1 能否拯救 bad seed？3-seed mean±std 用于论文 Claim 2 统计支撑。\", \"parent\": \"plan002-additive-b01-s42\", \"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-14T08:45:10.999Z\", \"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_bonus.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 43 --beta 0.1 --reward_mode additive_bonus --output_dir /root/autodl-tmp/outputs/plan002_additive_b01_s43\\\"\", \"finished_at\": \"2026-05-14T09:41:23.932Z\", \"training_hours\": 0.94}, \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_bonus.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 43 --beta 0.1 --reward_mode additive_bonus --output_dir /root/autodl-tmp/outputs/plan002_additive_b01_s43\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"466128\", \"log_path\": \"~/runs/solver-trace-ablation/plan002-additive-b01-s43.log\", \"submitted_at\": \"2026-05-14T08:45:54.837Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 4096.6, \"gpu_hours\": 1.14}, \"pid\": \"466128\", \"log_path\": \"~/runs/solver-trace-ablation/plan002-additive-b01-s43.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T09:41:25.536028+00:00\"}]}, \"metrics\": {\"eval_prove_rate\": 0.61, \"eval_mean_isr\": 0.5063, \"eval_isr_std\": 0.4518, \"eval_median_isr\": 0.5, \"eval_proved_only_isr\": 0.8301, \"component_count_mean\": 4.03, \"component_count_2_ratio\": 0, \"tautological_collapse\": false, \"isr_0_ratio\": 0.39, \"isr_1_ratio\": 0.656, \"proved_single_premise_ratio\": 1, \"h7_rate_calibrated\": 0.967, \"h7_definition\": \"single_premise AND premise==conclusion (normalized)\", \"hacking_mode\": \"conclusion_duplication_isr_inflation\", \"conclusion_embedding\": true, \"by_answer_type\": {\"false\": {\"n\": 25, \"proved\": 18, \"PR\": 0.72, \"ISR\": 0.6}, \"unknown\": {\"n\": 41, \"proved\": 22, \"PR\": 0.537, \"ISR\": 0.442}, \"true\": {\"n\": 34, \"proved\": 21, \"PR\": 0.618, \"ISR\": 0.515}}, \"train_total_steps\": 500, \"train_duration_min\": 53, \"train_loss\": 0.012}, \"conclusion\": \"negative\", \"notes\": \"NEGATIVE: conclusion duplication hacking 确认。100% proved 样本仅 1 premise，97% premise=conclusion（重言式 P→P）。ISR=0.506 是 artifact（唯一 premise 必然 necessary）。与 s44 相同失败模式。3-seed 中 s42 唯一可能 genuine（待验证），s43/s44 均 collapse。β=0.1 additive bonus 多 seed 可靠性不足。\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan002_additive_b01_s43/checkpoint-500\", \"completed_at\": \"2026-05-14T09:54:11.468Z\"}, \"plan012-hacking-taxonomy\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T09:06:38.613Z\", \"updated_at\": \"2026-05-14T09:07:42.314Z\", \"spec\": {\"command\": \"rule-based hacking taxonomy classification on eval_sta outputs\", \"server\": \"westd-39279\", \"data_path\": \"eval_results.json from plan002-b01-s42 + plan018-b01-s42\", \"data_count\": 160, \"model_name\": \"N/A (rule-based analysis)\", \"seed\": \"N/A\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"N/A (analysis task)\", \"log_path\": \"artifacts/hacking_taxonomy_comparison.md\", \"completed_at\": \"2026-05-14T09:07:12.765Z\", \"hypothesis\": \"ISR β=0.1 vs Random β=0.1 hacking taxonomy 对比：ISR reward 能否减少 hacking 模式比例、增加 genuine proof 比例？5 种 hacking 分类（conclusion embedding, repetition collapse, tautological collapse, complexity-without-utility, premise padding）。\", \"metrics\": {\"isr_b01_genuine_rate\": 0.259, \"random_b01_genuine_rate\": 0.177, \"genuine_rate_delta_pp\": 8.2, \"isr_b01_conclusion_embedding_rate\": 0.728, \"random_b01_conclusion_embedding_rate\": 0.785, \"isr_b01_genuine_mean_isr\": 0.6723, \"random_b01_genuine_mean_isr\": 0.3427, \"isr_b01_complexity_wo_utility_rate\": 0, \"random_b01_complexity_wo_utility_rate\": 0.038, \"isr_b01_hacking_rate\": 0.741, \"random_b01_hacking_rate\": 0.823}, \"notes\": \"D037/D038 完成。Conclusion embedding 是主导 hacking 模式（ISR 72.8% vs Random 78.5%）。ISR β=0.1 genuine proof +8.2pp (25.9% vs 17.7%)，genuine ISR 质量 0.67 vs 0.34。ISR 消除 complexity-without-utility hacking。LLM-as-judge 跳过（D038），记入 Discussion/Future Work。Artifact: art_20260514_bf31aa。\"}, \"plan018-additive-random-b01-s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T06:55:48.888Z\", \"updated_at\": \"2026-05-14T08:32:44.808Z\", \"hypothesis\": \"β=0.1 random control: r = r_exec·(1+0.1·random[0,1]). 与 plan002-b01 (additive ISR β=0.1, PR=0.81, ISR=0.337) 同 β 对照。如果 ISR β=0.1 >> random β=0.1 → ISR 信号在低剂量下有结构价值; 如果 ISR ≈ random → ISR 信号在低剂量下也仅是 variance regularization。D031 紧急实验。\", \"parent\": \"plan002-additive-b01-s42\", \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_random_b01.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 42 --beta 0.1 --reward_mode additive_random --output_dir /root/autodl-tmp/outputs/plan018_additive_random_b01_s42\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"377678\", \"log_path\": \"~/runs/solver-trace-ablation/plan018-additive-random-b01-s42.log\", \"submitted_at\": \"2026-05-14T06:55:59.287Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"plan_id\": \"plan018\", \"reward_formula\": \"r = r_exec * (1 + 0.1 * random[0,1])\", \"num_steps\": 500, \"checkpoint_source\": \"N/A (training, not eval)\", \"eval_data\": \"N/A (training, not eval)\", \"wall_clock_seconds\": 5160.4, \"gpu_hours\": 1.43, \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan018_additive_random_b01_s42\"}, \"reproduce\": {\"finished_at\": \"2026-05-14T08:09:07.662Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T08:09:09.188407+00:00\"}]}, \"conclusion\": \"negative\", \"metrics\": {\"eval_prove_rate\": 0.79, \"eval_mean_isr\": 0.1038, \"eval_isr_std\": 0.1369, \"eval_median_isr\": 0.0357, \"eval_proved_only_isr\": 0.1314, \"eval_n_proved\": 79, \"eval_n_problems\": 100, \"eval_component_count_mean\": 8.46, \"eval_component_count_median\": 8, \"eval_component_count_2_ratio\": 0, \"eval_isr_1_ratio\": 0, \"eval_isr_0_ratio\": 0.367, \"eval_isr_gt0_ratio\": 0.633, \"eval_by_type_false_pr\": 0.8, \"eval_by_type_false_isr\": 0.1318, \"eval_by_type_unknown_pr\": 0.7317, \"eval_by_type_unknown_isr\": 0.0944, \"eval_by_type_true_pr\": 0.8529, \"eval_by_type_true_isr\": 0.0945, \"tautological_collapse\": false, \"train_total_steps\": 500, \"train_duration_min\": 70.5, \"train_last100_pr\": 0.805, \"train_last100_isr\": 0.1432, \"train_loss\": 0.005}, \"notes\": \"Random control β=0.1 vs ISR β=0.1 (plan002-b01) 对照。conclusion=negative: random control的ISR远低于ISR-guided。\\n\\n对比 plan002-b01 (ISR β=0.1):\\n- PR: 0.79 vs 0.81 (≈持平, Δ=0.02)\\n- Mean ISR: 0.104 vs 0.337 (ISR 3.2x higher)\\n- Proved-only ISR: 0.131 vs 0.415 (ISR 3.2x higher)\\n- Median ISR: 0.036 vs plan002未记录\\n- Component count: 8.46 vs 5.58 (random组更多冗余)\\n- ISR=0占比(proved): 36.7% (random组大量proof无结构)\\n- Tautological collapse: 无 (component_2_ratio=0)\\n\\n关键发现: PR几乎相同说明β=0.1 random噪声不影响证明能力。但ISR差3.2倍，证明ISR reward提供genuine structural guidance而非仅variance regularization。这强力支持Claim 2: ISR信号在低剂量下有结构价值。\\n\\nEval output: /root/autodl-tmp/outputs/plan018_additive_random_b01_s42/eval_results.json\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan018_additive_random_b01_s42\", \"completed_at\": \"2026-05-14T08:21:59.737Z\"}, \"plan016-extended-1000-s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T05:29:47.634Z\", \"updated_at\": \"2026-05-14T08:15:33.185Z\", \"hypothesis\": \"Extended training 1000 steps exec-only: plan001-s42 500步 PR=93% 是真收敛还是 lucky early convergence? 1000步观察 PR 和 ISR 在更长 horizon 的行为。s43(14%)/s44(98% tautological) 在 500 步均失败，延长训练是否能改善？\", \"parent\": \"plan001-exec-only-s42-r2\", \"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --data_path data/train_500_seed42.jsonl --num_steps 1000 --seed 42 --output_dir /root/autodl-tmp/outputs/plan016_extended_1000_s42\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"data_path\": \"/root/solver-trace-ablation/data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"Extended training 1000 steps exec-only: plan001-s42 500步 PR=93% 是真收敛还是 lucky early convergence?\", \"plan_id\": \"plan016\", \"reward_formula\": \"r = r_exec (exec-only)\", \"num_steps\": 1000}, \"pid\": \"263268\", \"log_path\": \"~/runs/solver-trace-ablation/plan016-extended-1000-s42.log\", \"reproduce\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --data_path data/train_500_seed42.jsonl --num_steps 1000 --seed 42 --output_dir /root/autodl-tmp/outputs/plan016_extended_1000_s42\\\"\", \"finished_at\": \"2026-05-14T08:02:31.805Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T08:02:33.434519+00:00\"}]}, \"metrics\": {\"train\": {\"total_steps\": 1000, \"duration_min\": 146, \"final_prove_rate\": 0.8396, \"final_mean_isr\": 0.0503, \"train_loss\": 0.0125, \"epoch\": 4, \"windowed\": {\"steps_001_100\": {\"pr\": 0.19, \"isr\": 0.0859}, \"steps_101_200\": {\"pr\": 0.66, \"isr\": 0.1115}, \"steps_201_300\": {\"pr\": 0.838, \"isr\": 0.0985}, \"steps_301_400\": {\"pr\": 0.907, \"isr\": 0.054}, \"steps_401_500\": {\"pr\": 0.927, \"isr\": 0.0433}, \"steps_501_600\": {\"pr\": 0.963, \"isr\": 0.0408}, \"steps_601_700\": {\"pr\": 0.965, \"isr\": 0.02}, \"steps_701_800\": {\"pr\": 0.988, \"isr\": 0.0178}, \"steps_801_900\": {\"pr\": 0.978, \"isr\": 0.017}, \"steps_901_1000\": {\"pr\": 0.981, \"isr\": 0.0144}}}, \"eval\": {\"prove_rate\": 0.96, \"n_proved\": 96, \"n_problems\": 100, \"mean_isr\": 0.0027, \"isr_std\": 0.0118, \"median_isr\": 0, \"proved_only_mean_isr\": 0.0028, \"min_isr\": 0, \"max_isr\": 0.0588, \"isr_0_ratio\": 0.9479, \"isr_1_ratio\": 0, \"component_count_mean\": 18.55, \"component_count_2_ratio\": 0, \"mean_n_necessary\": 0.052, \"n_necessary_0_ratio\": 0.9479, \"tautological_collapse\": false, \"by_answer_type\": {\"false\": {\"count\": 29, \"proved\": 26, \"prove_rate\": 0.8966, \"mean_isr\": 0}, \"unknown\": {\"count\": 31, \"proved\": 30, \"prove_rate\": 0.9677, \"mean_isr\": 0.0053}, \"true\": {\"count\": 40, \"proved\": 40, \"prove_rate\": 1, \"mean_isr\": 0.0026}}, \"eval_time_seconds\": 396.3}}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan016_extended_1000_s42\", \"completed_at\": \"2026-05-14T08:13:51.754Z\", \"notes\": \"Extended training to 1000 steps CONFIRMS ISR collapse worsens monotonically.\\\\n\\\\n## 500 vs 1000 step comparison (eval_sta.py):\\\\n| Metric | plan001-s42 (500步) | plan016 (1000步) | Change |\\\\n|--------|-------------------|-----------------|--------|\\\\n| eval PR | 0.93 | 0.96 | +3.2% |\\\\n| eval ISR | 0.123 | 0.0027 | -97.8% |\\\\n| proved_only ISR | 0.132 | 0.0028 | -97.9% |\\\\n| components | 6.58 | 18.55 | +182% |\\\\n| ISR=0 ratio | - | 94.8% | - |\\\\n| n_necessary=0 ratio | - | 94.8% | - |\\\\n\\\\n## Key findings:\\\\n1. PR improves (+3%) but ISR collapses near-zero (0.0027). The model gets BETTER at proving while becoming WORSE at faithful reasoning.\\\\n2. Component count nearly tripled (6.58→18.55). Model generates longer proofs with more components, but 94.8% have ZERO necessary components.\\\\n3. NOT tautological collapse (comp=2 ratio=0). Instead: contradiction-based collapse — model embeds P(a) and ¬P(a) among many irrelevant premises, making anything provable via explosion.\\\\n4. Windowed ISR trend is monotonically decreasing: 0.1115 (101-200) → 0.0433 (401-500) → 0.0200 (601-700) → 0.0144 (901-1000). No recovery signal.\\\\n5. The exec-only reward creates a pure reward hacking incentive: the model discovers that contradictions + trivially true conclusions always satisfy the prover.\\\\n\\\\n## Implication for paper:\\\\nExtended training is a clean ablation showing exec-only reward's failure mode worsens over time. The 500-step ISR of 0.123 was not a floor — it was a snapshot of ongoing collapse.\"}, \"plan005-sta-low-s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T22:20:47.812Z\", \"updated_at\": \"2026-05-14T06:31:05.119Z\", \"spec\": {\"model_name\": \"Qwen3-4B\", \"data_path\": \"/root/solver-trace-ablation/data/train_500_seed42.jsonl\"}, \"reproduce\": {\"finished_at\": \"2026-05-13T23:55:02.341Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-13T23:55:06.559440+00:00\"}]}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan005_sta_low_s42/checkpoint-500\", \"log_path\": \"/root/autodl-tmp/outputs/plan005_sta_low_s42/reward_log.jsonl\", \"completed_at\": \"2026-05-13T23:59:25.396Z\", \"metrics\": {\"total_steps\": 500, \"duration_min\": 71, \"parse_rate\": 1, \"overall_prove_rate\": 0.5657, \"overall_isr\": 0.1682, \"last50_prove_rate\": 0.77, \"last50_isr\": 0.2559, \"last100_prove_rate\": 0.7725, \"last100_isr\": 0.2299, \"last100_loss\": 0.022752, \"overall_loss\": 0.017296, \"last100_isr_pr_ratio\": 0.298, \"last100_isr_lt_pr_count\": \"99/100\", \"first_rolling10_pr_ge_0.8\": 178, \"first_rolling10_pr_ge_0.9\": 439, \"max_rolling10_pr\": 0.9375, \"max_rolling10_isr\": 0.3282, \"windowed\": {\"1-50\": {\"pr\": 0.1775, \"isr\": 0.0906}, \"51-100\": {\"pr\": 0.1775, \"isr\": 0.0835}, \"101-200\": {\"pr\": 0.5062, \"isr\": 0.1463}, \"201-300\": {\"pr\": 0.6713, \"isr\": 0.1791}, \"301-400\": {\"pr\": 0.7013, \"isr\": 0.1984}, \"401-500\": {\"pr\": 0.7725, \"isr\": 0.2299}}}, \"notes\": \"conclusion=negative 基于 prove_rate 下降（last100 0.7725 vs exec-only 0.865）。但结构性发现：ISR/PR ratio=0.298，99/100 步 ISR &lt; PR，说明 STA=0.1 维持了 ISR 与 PR 的持续分离——模型未通过 hacking prove_rate 绕过 STA penalty。此观察支持论文 \\\"STA 抑制 reward hacking\\\" claim。windowed ISR/PR: 1-50 (0.51), 51-100 (0.47), 101-200 (0.29), 201-300 (0.27), 301-400 (0.28), 401-500 (0.30) — 分离在100步后稳定。D030 决策：checkpoint 已删除，不重训。论文用训练曲线 windowed ISR/PR 数据作为证据。\"}, \"plan001-exec-only-s43-r4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T01:40:37.808Z\", \"updated_at\": \"2026-05-14T06:30:57.539Z\", \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 43 --output_dir /root/autodl-tmp/outputs/plan001_exec_only_s43_r4\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"pid\": \"136339\", \"log_path\": \"~/runs/solver-trace-ablation/plan001-exec-only-s43-r4.log\", \"submitted_at\": \"2026-05-14T01:40:37.746Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/solver-trace-ablation/data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 43, \"hypothesis\": \"Exec-only seed=43 replication: confirm plan001-r2 (seed=42) prove_rate convergence is reproducible across seeds\", \"plan_id\": \"plan001\", \"wall_clock_seconds\": 10020.8, \"gpu_hours\": 2.78}, \"reproduce\": {\"finished_at\": \"2026-05-14T03:13:08.926Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T03:13:12.957272+00:00\"}]}, \"metrics\": {\"eval_sampling_prove_rate\": 0.14, \"eval_sampling_mean_isr\": 0, \"eval_sampling_n_proved\": 14, \"eval_sampling_temperature\": 0.7, \"eval_sampling_method\": \"do_sample=True, temperature=0.7\", \"eval_sampling_by_answer\": {\"true\": {\"count\": 34, \"proved\": 6, \"prove_rate\": 0.176}, \"false\": {\"count\": 25, \"proved\": 2, \"prove_rate\": 0.08}, \"unknown\": {\"count\": 41, \"proved\": 6, \"prove_rate\": 0.146}}}, \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan001_exec_only_s43_r4\", \"log_path\": \"/root/runs/solver-trace-ablation/plan001-exec-only-s43-r4.log\", \"conclusion\": \"negative\", \"notes\": \"训练 PR(last100)=0.883 但 eval PR=14% (sampling, T=0.7), ISR=0。87% 样本 hit max_new_tokens 生成不可解析长输出。与 s42 (eval PR=93%) 形成极端跨 seed 不稳定。exec-only reward landscape 存在极大方差。⚠️ 评估方法：sampling eval (T=0.7)，其他组用 eval_sta.py full STA。D029 决策：不重训，论文标注方法差异。PR=14% 是 failure case，eval 方法不影响结论。\", \"completed_at\": \"2026-05-14T04:27:38.542Z\"}, \"plan017-additive-random-s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T03:11:14.694Z\", \"updated_at\": \"2026-05-14T05:33:25.603Z\", \"hypothesis\": \"Additive random control: r = r_exec·(1+0.3·random). 隔离 ISR structural signal vs variance regularization. 若 ISR > random > exec-only → signal+regularization 均贡献; 若 ISR > random ≈ exec-only → ISR signal 是关键; 若 ISR ≈ random → ISR 无结构价值。\", \"parent\": \"plan013-random-reward-s42-r4\", \"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_random.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 42 --output_dir /root/autodl-tmp/outputs/plan017_additive_random_s42\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"data_path\": \"/root/solver-trace-ablation/data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"Additive random control: r = r_exec·(1+0.3·random)\", \"plan_id\": \"plan017\", \"reward_formula\": \"r = r_exec * (1 + 0.3 * random[0,1])\", \"beta\": 0.3}, \"pid\": \"207116\", \"log_path\": \"~/runs/solver-trace-ablation/plan017-additive-random-s42.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_random.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 42 --output_dir /root/autodl-tmp/outputs/plan017_additive_random_s42\\\"\", \"finished_at\": \"2026-05-14T05:17:13.920Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T05:17:18.376399+00:00\"}]}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan017_additive_random_s42\", \"notes\": \"Eval结果: PR=0.48, mean_ISR=0.0453, proved_only_ISR=0.0943, mean_components=9.56 (3+比例100%, 无tautological collapse). 但33%已证明样本ISR=0 (n_necessary=0, conclusion trivially provable). 与plan013的不同failure mode: additive random防止了2-component坍缩, 但模型转向生成复杂但无用的formalization (多premises但conclusion不依赖任何premise). Variance regularization不足以产生genuine proofs.\", \"metrics\": {\"eval_prove_rate\": 0.48, \"eval_mean_isr\": 0.0453, \"eval_isr_std\": 0.0759, \"eval_median_isr\": 0, \"eval_max_isr\": 0.2857, \"eval_proved_only_isr\": 0.0943, \"eval_n_proved\": 48, \"eval_n_problems\": 100, \"eval_method\": \"eval_sta.py full STA\", \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_component_count_mean\": 9.6, \"eval_component_count_2_ratio\": 0, \"eval_isr_pr_ratio\": 0.0943, \"eval_elapsed_s\": 542.3, \"eval_by_type_false_pr\": 0.32, \"eval_by_type_false_isr\": 0.0254, \"eval_by_type_unknown_pr\": 0.51, \"eval_by_type_unknown_isr\": 0.0518, \"eval_by_type_true_pr\": 0.56, \"eval_by_type_true_isr\": 0.052, \"tautological_collapse\": false}, \"completed_at\": \"2026-05-14T05:30:46.783Z\"}, \"plan014-downstream-nli-s42\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-14T03:43:37.925Z\", \"updated_at\": \"2026-05-14T04:29:48.645Z\", \"hypothesis\": \"Downstream NLI validation: 高ISR formalization 应在独立推理任务上表现更好(entailment accuracy)，Spearman ρ(ISR, accuracy) > 0.1 验证 ISR 作为 quality proxy 的实用价值。同时用 Z3 cross-solver agreement 验证 formalization 鲁棒性。\", \"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-14T03:49:52.891Z\", \"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/eval_downstream.py --checkpoint_path /root/autodl-tmp/outputs/plan001_exec_only_s42 --base_model /root/autodl-tmp/models/Qwen3-4B --data_path data/proofwriter_fol_100.jsonl --output_path /root/autodl-tmp/outputs/plan014_downstream_nli.json --num_generations 8 --workers 4\\\"\", \"finished_at\": \"2026-05-14T04:26:05.334Z\", \"training_hours\": 0.6}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"completed_at\": \"2026-05-14T03:51:18.427Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-14T03:51:19.514390+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T04:26:06.788787+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"r1 失败: checkpoint_path 多了 /checkpoint-500。save_total_limit=1 导致模型直接保存在 plan001_exec_only_s42/ 根目录。修正路径为 /root/autodl-tmp/outputs/plan001_exec_only_s42 即可。等 s43 re-eval 完成后重跑。\"}}, \"notes\": \"Negative: ISR 作为 downstream NLI quality proxy 无效。Spearman ρ(ISR, correct)=-0.049 (p=0.187)，Best-of-N ISR 仅 +0.9pp over random (不显著)。主因：模型严重 true-bias (false accuracy=0%)，NLI accuracy 天花板仅 34.1%，ISR 无区分空间。ISR bucket 层面有弱单调趋势 (high=75% > mid=37.7% > low=32.7%) 但 high bucket 仅 12 样本。quartile 分析非单调。\", \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/eval_downstream.py --checkpoint_path /root/autodl-tmp/outputs/plan001_exec_only_s42 --base_model /root/autodl-tmp/models/Qwen3-4B --data_path data/proofwriter_fol_100.jsonl --output_path /root/autodl-tmp/outputs/plan014_downstream_nli.json --num_generations 8 --workers 4\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"216133\", \"log_path\": \"~/runs/solver-trace-ablation/plan014-downstream-nli-s42.log\", \"submitted_at\": \"2026-05-14T04:17:30.763Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 737.9, \"gpu_hours\": 0.2}, \"pid\": \"216133\", \"log_path\": \"~/runs/solver-trace-ablation/plan014-downstream-nli-s42.log\", \"conclusion\": \"negative\", \"metrics\": {\"overall_accuracy\": 0.341, \"proved_rate\": 0.915, \"proved_count\": 732, \"total_generations\": 800, \"parse_errors\": 0, \"accuracy_by_label\": {\"true\": 0.912, \"false\": 0, \"unknown\": 0.076}, \"spearman_rho\": -0.049, \"spearman_p\": 0.187, \"mann_whitney_U\": 17202, \"mann_whitney_p\": 0.288, \"bon_isr_accuracy\": 0.35, \"bon_random_accuracy\": 0.341, \"bon_oracle_accuracy\": 0.44, \"bon_prove_first_accuracy\": 0.35, \"isr_bucket_high_acc\": 0.75, \"isr_bucket_mid_acc\": 0.377, \"isr_bucket_low_acc\": 0.327, \"runtime_inference_s\": 408.8, \"runtime_eval_s\": 13.6}, \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan014_downstream_nli.json\"}, \"plan002-additive-b03-s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T02:24:47.843Z\", \"updated_at\": \"2026-05-14T04:27:38.822Z\", \"spec\": {\"data_path\": \"/root/solver-trace-ablation/data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"Additive ISR bonus r=r_exec*(1+β*ISR) with β=0.3: ISR can only boost reward, never penalize. Should preserve prove_rate (unlike convex combination penalty in plan005) while improving structural quality.\", \"plan_id\": \"plan_002\", \"reward_formula\": \"r = r_exec * (1 + 0.3 * ISR)\", \"beta\": 0.3, \"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_bonus.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 42 --beta 0.3 --reward_mode additive_bonus --output_dir /root/autodl-tmp/outputs/plan002_additive_beta03_s42\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"161819\"}, \"reproduce\": {\"finished_at\": \"2026-05-14T03:24:44.110Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T03:24:48.666027+00:00\"}]}, \"metrics\": {\"total_steps\": 500, \"duration_min\": 56.7, \"overall_prove_rate\": 0.34025, \"overall_isr\": 0.11527, \"first20_prove_rate\": 0.15625, \"last50_prove_rate\": 0.555, \"last100_prove_rate\": 0.5525, \"mean_loss\": 0.008914, \"last100_loss\": 0.014469, \"parse_rate\": 1, \"w1_50_prove_rate\": 0.13, \"w51_100_prove_rate\": 0.095, \"w101_200_prove_rate\": 0.185, \"w201_300_prove_rate\": 0.375, \"w301_400_prove_rate\": 0.47625, \"w401_500_prove_rate\": 0.5525, \"steps_ge_085\": 52, \"first_step_ge_085\": 46, \"final_prove_rate\": 1, \"final_isr_mean\": 0.3089, \"final_reward_mean\": 1.0927}, \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan002_additive_beta03_s42\", \"log_path\": \"~/runs/solver-trace-ablation/plan002-additive-b03-s42.log\", \"notes\": \"ISR 为 binary 近似 (_fast_fn)，不可用于论文跨 run 对比，需 eval_sta.py 统一评估真实 ISR。prove_rate 轨迹 0.13→0.095→0.185→0.375→0.476→0.553，呈稳步上升趋势，尚未完全饱和（仅 52/500 步 ≥0.85），与 plan001/plan013 的强饱和模式不同。\", \"conclusion\": \"negative\", \"eval_prove_rate\": 0.18, \"eval_mean_isr\": 0.0257, \"eval_isr_std\": 0.0742, \"eval_proved_only_isr\": 0.1427, \"eval_median_isr\": 0, \"eval_isr_pr_ratio\": 0.1427, \"completed_at\": \"2026-05-14T04:27:38.822Z\"}, \"plan013-random-reward-s42-r4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T01:40:35.587Z\", \"updated_at\": \"2026-05-14T03:45:53.344Z\", \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_random_reward.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 42 --exec_weight 0.9 --sta_weight 0.1 --output_dir /root/autodl-tmp/outputs/plan013_random_reward_s42_r4\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"136261\", \"log_path\": \"~/runs/solver-trace-ablation/plan013-random-reward-s42-r4.log\", \"submitted_at\": \"2026-05-14T01:40:35.528Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/solver-trace-ablation/data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"Random reward baseline: replacing ISR with random values should degrade structural quality while maintaining execution reward, proving ISR's causal contribution\", \"plan_id\": \"plan013\", \"wall_clock_seconds\": 2492.4, \"gpu_hours\": 0.69}, \"reproduce\": {\"finished_at\": \"2026-05-14T02:19:57.306Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-14T02:19:58.514969+00:00\"}]}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan013_random_reward_s42_r4/checkpoint-500\", \"log_path\": \"/root/autodl-tmp/outputs/plan013_random_reward_s42_r4/reward_log.jsonl\", \"metrics\": {\"eval_prove_rate\": 1, \"eval_mean_isr\": 0.535, \"eval_isr_std\": 0.1282, \"eval_proved_only_isr\": 0.535, \"eval_median_isr\": 0.5, \"eval_n_proved\": 100, \"eval_n_problems\": 100, \"eval_method\": \"eval_sta.py full STA\", \"eval_data\": \"proofwriter_fol_100.jsonl\", \"eval_note\": \"DEGENERATE: model generates trivial 2-component proofs (premise=conclusion, conclusion=conclusion), ISR=0.5 is artifact of trivial proof structure\"}, \"completed_at\": \"2026-05-14T02:22:07.933Z\", \"notes\": \"⚠️ 训练日志 ISR 为 binary approximation (_fast_fn)，ISR≈prove_rate，不含结构信息。真实 ISR 需通过 eval_sta.py (full STA) 在 checkpoint-500 上重新评估。final_mean_isr=0.6705 实为 binary 近似值，禁止用于论文或跨实验 ISR 对比。\"}, \"plan001-exec-only-s43-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T01:02:31.830Z\", \"updated_at\": \"2026-05-14T01:41:28.427Z\", \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=1 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 43 --output_dir /root/autodl-tmp/outputs/plan001_exec_only_s43_r3\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"pid\": \"133258\", \"data_path\": \"/root/solver-trace-ablation/data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 43, \"hypothesis\": \"exec-only 500 steps seed 43 (r3), 3-seed baseline 2nd seed\", \"plan_id\": \"plan_001\"}, \"conclusion\": \"failed\", \"failure_reason\": \"OSError: [Errno 28] No space left on device — /root/autodl-tmp 磁盘满，TRL GRPOTrainer completions parquet 写入失败 at step 23\", \"checkpoint_path\": \"N/A (disk full crash at step 23)\", \"log_path\": \"/root/autodl-tmp/outputs/plan001_exec_only_s43_r3/reward_log.jsonl\", \"completed_at\": \"2026-05-14T01:41:28.427Z\"}, \"plan013-random-reward-s42-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T01:02:30.063Z\", \"updated_at\": \"2026-05-14T01:41:28.122Z\", \"spec\": {\"command\": \"bash -c \\\"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_random_reward.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 42 --exec_weight 0.9 --sta_weight 0.1 --output_dir /root/autodl-tmp/outputs/plan013_random_reward_s42_r3\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"133178\", \"data_path\": \"/root/solver-trace-ablation/data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"Random reward baseline (r3): random value replaces ISR to isolate ISR-specific signal vs multi-objective regularization\", \"plan_id\": \"plan_013\", \"hyperparams\": {\"alpha\": 0.9, \"beta\": 0.1, \"K\": 8, \"num_steps\": 500, \"reward_type\": \"random_penalty\"}}, \"conclusion\": \"failed\", \"failure_reason\": \"OSError: [Errno 28] No space left on device — /root/autodl-tmp 磁盘满，TRL GRPOTrainer completions parquet 写入失败 at step 28\", \"checkpoint_path\": \"N/A (disk full crash at step 28)\", \"log_path\": \"/root/autodl-tmp/outputs/plan013_random_reward_s42_r3/reward_log.jsonl\", \"completed_at\": \"2026-05-14T01:41:28.122Z\"}, \"plan001-exec-only-s43-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T00:22:12.292Z\", \"updated_at\": \"2026-05-14T01:01:56.416Z\", \"spec\": {\"command\": \"python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 43 --output_dir /root/autodl-tmp/outputs/plan001_exec_only_s43\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"pid\": \"126541\", \"log_path\": \"~/runs/solver-trace-ablation/plan001-exec-only-s43-r2.log\", \"submitted_at\": \"2026-05-14T00:22:12.241Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/solver-trace-ablation/data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 43, \"hypothesis\": \"exec-only 500步 seed 43 (retry), 3-seed baseline 第2个 seed\", \"wall_clock_seconds\": 2384.2, \"gpu_hours\": 0.66}, \"checkpoint_path\": \"N/A (crashed after submission)\", \"log_path\": \"/root/autodl-tmp/outputs/plan001_exec_only_s43_r2/reward_log.jsonl\", \"conclusion\": \"failed\", \"failure_reason\": \"Process crashed after submission (PID 126546 not found, tmux session dead). Worker verified 91% util at submission but process died within 30 min.\", \"completed_at\": \"2026-05-14T01:01:56.416Z\"}, \"plan013-random-reward-s42-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-14T00:22:10.140Z\", \"updated_at\": \"2026-05-14T01:01:55.694Z\", \"spec\": {\"command\": \"python3 scripts/train_grpo.py --config configs/grpo_random_reward.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 42 --exec_weight 0.9 --sta_weight 0.1 --output_dir /root/autodl-tmp/outputs/plan013_random_reward_s42\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"126461\", \"log_path\": \"~/runs/solver-trace-ablation/plan013-random-reward-s42-r2.log\", \"submitted_at\": \"2026-05-14T00:22:10.091Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/solver-trace-ablation/data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"Random reward baseline (retry): 用随机值替代 ISR，隔离 ISR-specific signal vs multi-objective regularization effect\", \"wall_clock_seconds\": 2385.6, \"gpu_hours\": 0.66}, \"checkpoint_path\": \"N/A (crashed after submission)\", \"log_path\": \"/root/autodl-tmp/outputs/plan013_random_reward_s42_r2/reward_log.jsonl\", \"conclusion\": \"failed\", \"failure_reason\": \"Process crashed after submission (PID 126466 not found, tmux session dead). Worker verified 91% util at submission but process died within 30 min.\", \"completed_at\": \"2026-05-14T01:01:55.694Z\"}, \"plan013-random-reward-s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T23:56:44.062Z\", \"updated_at\": \"2026-05-14T00:21:05.430Z\", \"spec\": {\"hypothesis\": \"Random reward baseline: 用随机值替代 ISR，隔离 ISR-specific signal vs multi-objective regularization effect\", \"command\": \"bash -c \\\"CUDA_VISIBLE_DEVICES=0 source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_random_reward.yaml --num_steps 500 --seed 42 --exec_weight 0.9 --sta_weight 0.1\\\"\", \"server\": \"westd-39279\", \"data_path\": \"data/proofwriter_fol_500.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"plan_id\": \"plan_013\", \"gpu\": \"cuda:0\", \"hyperparams\": {\"alpha\": 0.9, \"beta\": 0.1, \"K\": 8, \"num_steps\": 500, \"reward_type\": \"random_penalty\"}, \"pid\": 122796, \"output_dir\": \"/root/autodl-tmp/outputs/plan013_random_reward_s42\", \"log_path\": \"/root/autodl-tmp/outputs/plan013_random_reward_s42.log\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan013_random_reward_s42\", \"reward_mode\": \"random_reward\", \"exec_weight\": 0.9, \"sta_weight\": 0.1, \"num_steps\": 500}, \"checkpoint_path\": \"N/A (GPU overflow, no valid output)\", \"log_path\": \"/root/autodl-tmp/outputs/plan013_random_reward_s42.log\", \"conclusion\": \"failed\", \"failure_reason\": \"CUDA_VISIBLE_DEVICES not set (inline assignment not exported), GPU overflow to both GPUs\", \"completed_at\": \"2026-05-14T00:21:05.430Z\"}, \"plan001-exec-only-s43\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T23:55:08.635Z\", \"updated_at\": \"2026-05-14T00:21:04.003Z\", \"spec\": {\"command\": \"python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --num_steps 500 --seed 43 --output_dir /root/autodl-tmp/outputs/plan001_exec_only_s43\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"121275\", \"log_path\": \"~/runs/solver-trace-ablation/plan001-exec-only-s43.log\", \"submitted_at\": \"2026-05-13T23:55:08.544Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"data/proofwriter_fol_500.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 43, \"hypothesis\": \"exec-only 500步 seed 43, 3-seed baseline 第2个 seed。预期 prove_rate>0.80 (与 s42 一致)\", \"wall_clock_seconds\": 1555.5, \"gpu_hours\": 0.43}, \"checkpoint_path\": \"N/A (killed by OOM before completion)\", \"log_path\": \"~/runs/solver-trace-ablation/plan001-exec-only-s43.log\", \"conclusion\": \"failed\", \"failure_reason\": \"OOM by plan013 GPU overflow — plan013 未设 CUDA_VISIBLE_DEVICES 导致占用两张 GPU，plan001-s43 被 OOM kill\", \"completed_at\": \"2026-05-14T00:21:04.003Z\"}, \"plan001-exec-only-s42\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T22:19:41.568Z\", \"updated_at\": \"2026-05-13T23:03:42.892Z\", \"spec\": {\"command\": \"python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --num_steps 500 --seed 42\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"83029\", \"log_path\": \"~/runs/solver-trace-ablation/plan001-exec-only-s42.log\", \"submitted_at\": \"2026-05-13T22:20:46.569Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/solver-trace-ablation/data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"exec-only 500步训练 baseline\", \"wall_clock_seconds\": 2576.3, \"gpu_hours\": 0.72}, \"conclusion\": \"failed\", \"checkpoint_path\": \"N/A (failed before checkpoint)\", \"completed_at\": \"2026-05-13T23:03:42.892Z\"}, \"plan003-eval-exec-only-r5\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T22:21:48.691Z\", \"updated_at\": \"2026-05-13T23:03:19.945Z\", \"spec\": {\"command\": \"eval_sta.py on r5 exec-only checkpoint\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"pid\": \"83690\", \"log_path\": \"~/runs/solver-trace-ablation/plan003-eval-exec-only-r5.log\", \"submitted_at\": \"2026-05-13T22:21:48.658Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/solver-trace-ablation/data/proofwriter_fol_100.jsonl\", \"data_count\": 100, \"model_name\": \"Qwen3-4B (r5 exec-only checkpoint)\", \"seed\": 0, \"checkpoint_source\": \"sta-phase1-exec-only-r5\", \"eval_data\": \"proofwriter_fol_100\", \"hypothesis\": \"Full STA eval on exec-only 100-step checkpoint to measure formalization quality\", \"wall_clock_seconds\": 2490.2, \"gpu_hours\": 0.69}, \"metrics\": {\"prove_rate\": 0.32, \"mean_isr\": 0.2055, \"isr_std\": 0.3194, \"proved_only_isr\": 0.6423, \"isr_by_type\": {\"true\": 0.3598, \"false\": 0.1723, \"unknown\": 0.0979}, \"total_samples\": 100, \"proved_count\": 32, \"runtime_s\": 251.7}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/plan003_eval_exec_only_r5.json\", \"log_path\": \"~/runs/solver-trace-ablation/plan003-eval-exec-only-r5.log\", \"completed_at\": \"2026-05-13T23:03:18.848Z\"}, \"plan001-exec-only-s42-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T22:42:40.242Z\", \"updated_at\": \"2026-05-13T23:03:11.395Z\", \"spec\": {\"command\": \"python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml --num_steps 500 --seed 42\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"85710\", \"log_path\": \"~/runs/solver-trace-ablation/plan001-exec-only-s42-r3.log\", \"submitted_at\": \"2026-05-13T22:42:40.204Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/solver-trace-ablation/data/train_500_seed42.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"exec-only 500步训练 baseline (retry 3)\", \"wall_clock_seconds\": 1228.1, \"gpu_hours\": 0.34}, \"conclusion\": \"failed\", \"completed_at\": \"2026-05-13T23:03:08.298Z\", \"failure_reason\": \"OOM crash - duplicate submission while plan001-r2 was occupying cuda:0\"}, \"sta-phase1-exec-sta-r5\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T20:54:31.353Z\", \"updated_at\": \"2026-05-13T22:20:41.274Z\", \"spec\": {\"command\": \"bash -c \\\"CUDA_VISIBLE_DEVICES=1 source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_sta.yaml\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"pid\": \"75968\", \"log_path\": \"~/runs/solver-trace-ablation/sta-phase1-exec-sta-r5.log\", \"submitted_at\": \"2026-05-13T20:54:38.781Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/solver-trace-ablation/data/proofwriter_fol_500.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"Full STA continuous ISR (0.0-1.0) 作为 reward 组件，应在训练中产生与 execution-only 不同的 ISR 趋势——execution-only ISR 随 prove_rate 上升而虚高(reward hacking)，execution+STA ISR 维持真实水平(STA 抑制 hacking)\", \"wall_clock_seconds\": 3506.3, \"gpu_hours\": 0.97}, \"metrics\": {\"parse_rate\": 1, \"prove_rate\": 0.1, \"mean_isr\": 0.04347, \"last20_prove_rate\": 0.15, \"last20_isr_mean\": 0.04956, \"first20_prove_rate\": 0.08125, \"first20_isr_mean\": 0.05182, \"overall_reward_mean\": 0.07174, \"last20_reward_mean\": 0.09978, \"training_steps\": 100, \"training_minutes\": 16.9, \"step_time_s\": 10.13, \"isr_pr_ratio_overall\": 0.43, \"isr_pr_ratio_last20\": 0.33, \"K\": 8}, \"conclusion\": \"negative\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/grpo_exec_sta/\", \"log_path\": \"/root/autodl-tmp/outputs/grpo_exec_sta/reward_log.jsonl\", \"completed_at\": \"2026-05-13T21:53:05.068Z\"}, \"sta-phase1-exec-only-r5\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T20:54:27.505Z\", \"updated_at\": \"2026-05-13T21:53:04.486Z\", \"spec\": {\"command\": \"bash -c \\\"CUDA_VISIBLE_DEVICES=0 source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"75890\", \"log_path\": \"~/runs/solver-trace-ablation/sta-phase1-exec-only-r5.log\", \"submitted_at\": \"2026-05-13T20:54:37.293Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"/root/solver-trace-ablation/data/proofwriter_fol_500.jsonl\", \"data_count\": 500, \"model_name\": \"Qwen3-4B\", \"seed\": 42, \"hypothesis\": \"K=8 增加 within-group variance，减少全零 reward batch，使 GRPO 有更多有效梯度信号\", \"wall_clock_seconds\": 3507.2, \"gpu_hours\": 0.97}, \"metrics\": {\"parse_rate\": 1, \"prove_rate\": 0.15125, \"mean_isr\": 0.1475, \"last20_prove_rate\": 0.2, \"last20_isr_mean\": 0.2, \"first20_prove_rate\": 0.11875, \"first20_isr_mean\": 0.11875, \"overall_reward_mean\": 0.15125, \"last20_reward_mean\": 0.2, \"training_steps\": 100, \"training_minutes\": 15.7, \"step_time_s\": 9.44, \"isr_pr_ratio_last20\": 1, \"K\": 8}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/outputs/grpo_exec_only/\", \"log_path\": \"/root/autodl-tmp/outputs/grpo_exec_only/reward_log.jsonl\", \"completed_at\": \"2026-05-13T21:53:04.486Z\"}, \"sta-phase1-exec-sta-r4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T20:28:22.778Z\", \"updated_at\": \"2026-05-13T20:52:58.761Z\", \"spec\": {\"command\": \"bash -c \\\"CUDA_VISIBLE_DEVICES=1 source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_sta.yaml\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"pid\": \"70797\", \"log_path\": \"~/runs/solver-trace-ablation/sta-phase1-exec-sta-r4.log\", \"submitted_at\": \"2026-05-13T20:28:32.091Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 1404.7, \"gpu_hours\": 0.39}, \"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-13T20:28:31.240Z\", \"command\": \"bash -c \\\"CUDA_VISIBLE_DEVICES=1 source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_sta.yaml\\\"\", \"finished_at\": \"2026-05-13T20:45:55.480Z\", \"training_hours\": 0.29}, \"pid\": \"70797\", \"log_path\": \"~/runs/solver-trace-ablation/sta-phase1-exec-sta-r4.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-13T20:45:56.962544+00:00\"}]}, \"metrics\": {\"parse_rate\": 1, \"prove_rate\": 0.1575, \"mean_isr\": 0.1525, \"last20_prove_rate\": 0.2125, \"last20_isr_mean\": 0.2125, \"first20_reward_mean\": 0.119, \"training_steps\": 100, \"training_minutes\": 15}, \"checkpoint_path\": \"/root/autodl-tmp/outputs/grpo_exec_sta/\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-13T20:51:56.799Z\", \"notes\": \"Phase 1 r4 完成但无差异。fast_isr_fol 二值信号(0/1)对 proved samples 几乎全部 ISR=1，exec+STA reward ≈ exec-only reward。连续 ISR 才能产生有意义的差异信号。→ r5 改用 full sta_reward (continuous ISR 0.0-1.0) + K=8\"}, \"sta-phase1-exec-only-r4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T20:28:18.040Z\", \"updated_at\": \"2026-05-13T20:52:56.416Z\", \"spec\": {\"command\": \"bash -c \\\"CUDA_VISIBLE_DEVICES=0 source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"70716\", \"log_path\": \"~/runs/solver-trace-ablation/sta-phase1-exec-only-r4.log\", \"submitted_at\": \"2026-05-13T20:28:30.420Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 1405.8, \"gpu_hours\": 0.39}, \"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-13T20:28:28.733Z\", \"command\": \"bash -c \\\"CUDA_VISIBLE_DEVICES=0 source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml\\\"\", \"finished_at\": \"2026-05-13T20:45:53.506Z\", \"training_hours\": 0.29}, \"pid\": \"70716\", \"log_path\": \"~/runs/solver-trace-ablation/sta-phase1-exec-only-r4.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-13T20:45:54.294365+00:00\"}]}, \"metrics\": {\"parse_rate\": 1, \"prove_rate\": 0.15125, \"mean_isr\": 0.1475, \"last20_prove_rate\": 0.2, \"last20_isr_mean\": 0.2, \"first20_reward_mean\": 0.119, \"training_steps\": 100, \"training_minutes\": 15}, \"checkpoint_path\": \"/root/autodl-tmp/outputs/grpo_exec_only/\", \"conclusion\": \"negative\", \"completed_at\": \"2026-05-13T20:51:56.183Z\", \"notes\": \"Phase 1 r4 完成但无差异。fast_isr_fol 二值信号(0/1)对 proved samples 几乎全部 ISR=1，导致 exec+STA ≈ exec-only。prove_rate 从 baseline 12% → last20 20%（微弱提升）。K=4 导致大量全零 reward batch。→ r5 改用 full STA + K=8\"}, \"sta-phase1-exec-only-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T20:15:04.067Z\", \"updated_at\": \"2026-05-13T20:23:15.460Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"67225\", \"log_path\": \"~/runs/solver-trace-ablation/sta-phase1-exec-only-r3.log\", \"submitted_at\": \"2026-05-13T20:15:15.911Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 276.4, \"gpu_hours\": 0.08}, \"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-13T20:15:14.333Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml\\\"\", \"finished_at\": \"2026-05-13T20:19:51.612Z\", \"training_hours\": 0.08}, \"pid\": \"67225\", \"log_path\": \"~/runs/solver-trace-ablation/sta-phase1-exec-only-r3.log\", \"failure_reason\": \"EXIT_CODE=137 (SIGKILL — OOM killer or manual kill)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-13T20:19:52.268Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T20:19:52.981720+00:00\"}]}, \"notes\": \"EXIT_CODE=137 (OOM/SIGKILL) after ~276s. 同 sta-phase1-exec-sta-r3 一起诊断中\"}, \"sta-phase1-exec-sta-r3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T20:15:08.133Z\", \"updated_at\": \"2026-05-13T20:23:14.516Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_sta.yaml\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"pid\": \"67306\", \"log_path\": \"~/runs/solver-trace-ablation/sta-phase1-exec-sta-r3.log\", \"submitted_at\": \"2026-05-13T20:15:17.535Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 277.9, \"gpu_hours\": 0.08}, \"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-13T20:15:16.704Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_sta.yaml\\\"\", \"finished_at\": \"2026-05-13T20:19:54.409Z\", \"training_hours\": 0.08}, \"pid\": \"67306\", \"log_path\": \"~/runs/solver-trace-ablation/sta-phase1-exec-sta-r3.log\", \"failure_reason\": \"EXIT_CODE=137 (SIGKILL — OOM killer or manual kill)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-13T20:19:55.400Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T20:19:56.549926+00:00\"}]}, \"notes\": \"EXIT_CODE=137 (OOM/SIGKILL) after ~278s. 诊断中: worker_diagnose_sta-phase1-r3-oom_20260513T202300\"}, \"sta-phase1-exec-sta-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T19:55:08.640Z\", \"updated_at\": \"2026-05-13T19:55:41.544Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_sta.yaml\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"pid\": \"62364\", \"log_path\": \"~/runs/solver-trace-ablation/sta-phase1-exec-sta-r2.log\", \"submitted_at\": \"2026-05-13T19:55:19.065Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 22.5, \"gpu_hours\": 0.01}, \"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-13T19:55:18.267Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_sta.yaml\\\"\", \"finished_at\": \"2026-05-13T19:55:40.449Z\", \"training_hours\": 0.01}, \"pid\": \"62364\", \"log_path\": \"~/runs/solver-trace-ablation/sta-phase1-exec-sta-r2.log\", \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-13T19:55:41.544Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T19:55:42.974865+00:00\"}]}}, \"sta-phase1-exec-only-r2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T19:55:04.711Z\", \"updated_at\": \"2026-05-13T19:55:37.426Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"62283\", \"log_path\": \"~/runs/solver-trace-ablation/sta-phase1-exec-only-r2.log\", \"submitted_at\": \"2026-05-13T19:55:17.509Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 19.9, \"gpu_hours\": 0.01}, \"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-13T19:55:16.037Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml\\\"\", \"finished_at\": \"2026-05-13T19:55:36.845Z\", \"training_hours\": 0.01}, \"pid\": \"62283\", \"log_path\": \"~/runs/solver-trace-ablation/sta-phase1-exec-only-r2.log\", \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-13T19:55:37.426Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T19:55:38.155358+00:00\"}]}}, \"sta-phase1-exec-sta\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T18:26:53.258Z\", \"updated_at\": \"2026-05-13T19:33:03.905Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_sta.yaml\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:1\"], \"pid\": \"59574\", \"log_path\": \"~/runs/solver-trace-ablation/sta-phase1-exec-sta.log\", \"submitted_at\": \"2026-05-13T19:32:47.783Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 16.1, \"gpu_hours\": 0.0}, \"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-39279\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-13T19:30:58.981Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_sta.yaml\\\"\", \"finished_at\": \"2026-05-13T19:33:03.170Z\", \"training_hours\": 0.03}, \"pid\": \"59574\", \"log_path\": \"~/runs/solver-trace-ablation/sta-phase1-exec-sta.log\", \"failure_reason\": \"EXIT_CODE=2 (shell misuse / syntax)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-13T19:33:03.905Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T19:33:05.009356+00:00\"}]}}, \"sta-phase1-exec-only\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T18:26:46.351Z\", \"updated_at\": \"2026-05-13T19:33:01.169Z\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml\\\"\", \"server\": \"westd-39279\", \"gpu\": [\"cuda:0\"], \"pid\": \"59274\", \"log_path\": \"~/runs/solver-trace-ablation/sta-phase1-exec-only.log\", \"submitted_at\": \"2026-05-13T19:32:30.340Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 30.8, \"gpu_hours\": 0.01}, \"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"reproduce\": {\"server\": \"westd-39279\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-13T19:32:28.753Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_exec_only.yaml\\\"\", \"finished_at\": \"2026-05-13T19:33:00.602Z\", \"training_hours\": 0.01}, \"pid\": \"59274\", \"log_path\": \"~/runs/solver-trace-ablation/sta-phase1-exec-only.log\", \"failure_reason\": \"EXIT_CODE=2 (shell misuse / syntax)\", \"conclusion\": \"failed\", \"completed_at\": \"2026-05-13T19:33:01.169Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-13T19:33:01.864437+00:00\"}]}}, \"sta-gt-isr-baseline\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T18:11:13.283Z\", \"updated_at\": \"2026-05-13T18:12:44.147Z\", \"spec\": {\"command\": \"python3 scripts/gt_isr_baseline.py\", \"server\": \"westd-39279\", \"data_path\": \"/root/solver-trace-ablation/data/proofwriter_fol_100.jsonl\", \"data_count\": 100, \"model_name\": \"ground-truth-fol\", \"seed\": 0}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/solver-trace-ablation/outputs/gt_isr_baseline.json\", \"log_path\": \"/root/solver-trace-ablation/outputs/gt_isr_baseline.json\", \"completed_at\": \"2026-05-13T18:12:43.141Z\", \"metrics\": {\"gt_prove_rate\": 0.18, \"gt_mean_isr\": 0.5588, \"gt_isr_std\": 0.2582, \"gt_isr_median\": 0.6125, \"solver_execution_rate\": 1, \"true_prove_rate\": 0.5, \"true_mean_isr\": 0.5833}}, \"sta-phase0-baseline\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-13T17:51:48.853Z\", \"updated_at\": \"2026-05-13T18:10:40.982Z\", \"spec\": {\"hypothesis\": \"锚定 base Qwen3-4B 的 ISR baseline，后续判断 GRPO 训练是否导致 ISR 下降（reward hacking）\", \"model_name\": \"Qwen3-4B\", \"data_path\": \"/root/solver-trace-ablation/data/proofwriter_fol_100.jsonl\", \"data_count\": 100, \"server\": \"westd-39279\", \"data_source\": \"tasksource/folio\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python3 scripts/phase0_baseline.py --model_path models/Qwen3-4B --data_path data/proofwriter_fol_100.jsonl --output outputs/phase0_baseline.json\", \"seed\": 0, \"checkpoint_path\": \"N/A (inference only)\", \"log_path\": \"/root/solver-trace-ablation/outputs/phase0_baseline.json\", \"notes\": \"conclusion=success 但语义是 baseline_anchored（registry 不支持自定义 conclusion）。此实验是 baseline 锚定，非传统 success/failure。ISR 盲区：premise-conclusion 重复的 trivial formalization 可能获高 ISR，论文 Discussion 需讨论。\"}, \"log_path\": \"/tmp/phase0_baseline.log\", \"checkpoint_path\": \"/root/solver-trace-ablation/outputs/phase0_baseline.json\", \"metrics\": {\"mean_isr\": 0.0641, \"isr_std\": 0.1983, \"median_isr\": 0, \"isr_range\": [0, 0.889], \"prove_rate\": 0.12, \"proved_count\": 12, \"total_samples\": 100, \"xor_affected_samples\": 34, \"effective_prove_rate_no_xor\": 0.182, \"avg_time_per_sample_s\": 3.4, \"total_runtime_s\": 336, \"isr_by_answer\": {\"true\": {\"n\": 34, \"proved\": 9, \"prove_rate\": 0.265, \"mean_isr\": 0.1345}, \"false\": {\"n\": 25, \"proved\": 1, \"prove_rate\": 0.04, \"mean_isr\": 0.024}, \"unknown\": {\"n\": 41, \"proved\": 2, \"prove_rate\": 0.049, \"mean_isr\": 0.0302}}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-13T18:04:56.962Z\"}}, \"count\": 50, \"total\": 50, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.2142}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-14T17:23:53.956Z_

<details><summary>↩ Tool result · `toolu_01YRjLURQeKwijqezXndCmUr`</summary>

```text
1	# Evidence Tables — D051 Pure Negative Framing
2	
3	> All eval metrics from `eval_sta.py` (full STA) unless noted. D051 framing: ISR-as-reward provides **no structural advantage**; premise-count-matched ratio = 1.06×.
4	
5	---
6	
7	## Table 1 — Main Results (FOL)
8	
9	| Condition | Seeds | eval PR (mean±std) | eval ISR (mean±std) | proved_only ISR | Components (mean) | Tautological Collapse | Conclusion Embedding % | Hacking Mode |
10	|---|---|---|---|---|---|---|---|---|
11	| **Base model** (phase0) | 1 (s42) | 0.12 | 0.064±0.198 | — | — | No | — | N/A (no RL) |
12	| **SFT baseline** (plan009-r4) | 1 (s42) | 0.14 | 0.080±0.214 | 0.571 | — | No | 7.1% (1/14 H1) | Near-zero hacking (92.9% genuine) |
13	| **Exec-only 500步** (plan001) | 3 | 0.68±0.47 | 0.23±0.30 | — | — | 1/3 seeds | — | Heterogeneous† |
14	|   ↳ s42 | — | 0.93 | 0.123±0.189 | 0.132 | 6.58 | No | 87.1% (H1) | H1 87.1% (81/93), Genuine 12.9% (12/93) |
15	|   ↳ s43 | — | 0.14‡ | 0‡ | — | — | No | — | Repetition collapse |
16	|   ↳ s44 | — | 0.98 | 0.570±0.201 | 0.582 | 2.04 | **Yes (94%)** | — | Tautological collapse |
17	| **Exec-only 1000步** (plan016) | 1 (s42) | 0.96 | 0.003±0.012 | 0.003 | 18.55 | No | — | Contradiction explosion |
18	| **ISR β=0.1** (plan002-b01) | 3 | 0.77±0.14 | 0.55±0.24 | 0.716±0.26 | 4.65 | No | 2/3 seeds | ISR-specific gaming |
19	|   ↳ s42 | — | 0.81 | 0.337±0.323 | 0.415 | 5.58 | No | 67.9% | H7 16% + H1 52% |
20	|   ↳ s43 | — | 0.61 | 0.506±0.452 | 0.830 | 4.03 | No | 96.7% | **H7 96.7%** (ISR inflation) |
21	|   ↳ s44 | — | 0.89 | 0.803±0.342 | 0.902 | 4.33 | No | 86.5% | **H7 86.5%** (ISR inflation) |
22	| **Random β=0.1** (plan018) | 2/3§ | 0.84 | 0.083 | 0.100 | 8.46¹ | No | ~75% (H1)⁴ | Redundant premises |
23	|   ↳ s42 | — | 0.79 | 0.104±0.137 | 0.131 | 8.46 | No | 70.9% (H1) | H1 70.9% (56/79), H7 0% |
24	|   ↳ s44 | — | 0.89 | 0.062±0.176 | 0.070 | — | No | 79.8% (H1) | H1 79.8% (71/89), H7 0% |
25	|   ↳ s43 | — | RUNNING | — | — | — | — | — | — |
26	| **ISR β=0.3** (plan002-b03) | 1 (s42) | 0.18 | 0.026±0.074 | 0.143 | — | No | — | Format collapse (Goodhart) |
27	| **Random β=0.3** (plan017) | 1 (s42) | 0.48 | 0.045±0.076 | 0.094 | 9.60 | No | — | Complexity-without-utility |
28	| **Convex random** (plan013-r4) | 1 (s42) | 1.00 | 0.535±0.128 | 0.535 | 2.0 | **Yes (100%)** | 100% | P→P tautological |
29	
30	**Notes:**
31	- † Exec-only 500步 shows extreme seed variance: s42 = conclusion embedding, s43 = repetition collapse, s44 = tautological collapse. 3-seed mean is informative of instability, not a typical outcome.
32	- ‡ s43 eval used `do_sample=True, temperature=0.7` (NOT eval_sta.py). 87% samples hit `max_new_tokens`. ISR=0 not comparable to other seeds (C004 violation in historical data).
33	- § plan018-s43 still RUNNING; 2-seed interim values reported.
34	- ¹ Component count only available for s42.
35	
36	---
37	
38	## Table 2 — Hacking Taxonomy
39	
40	| Condition | Seed | H7 % | H1 % | H7+H1 (total) | Genuine % | n_proved | Premise-matched ISR |
41	|---|---|---|---|---|---|---|---|
42	| **SFT baseline** | s42 | 0% (0/14) | 7.1% (1/14) | 7.1% | **92.9%** (13/14) | 14 | — |
43	| **Exec-only 500步** | s42 | 0% (0/93) | **87.1%** (81/93) | **87.1%** | 12.9% (12/93) | 93 | — |
44	| **Exec-only 500步** | s44 | **100%** (97/97) | 0% | **100%** | 0% (0/97) | 97⁵ | — |
45	| **Exec-only 1000步** | s42 | — | — | — | — | 96 | — |
46	| **ISR β=0.1** | s42 | **16.0%** (13/81) | **51.9%** (42/81) | **67.9%** | **32.1%** (26/81) | 81 | **0.2578** (n≥3 prem) |
47	| **ISR β=0.1** | s43 | **96.7%** (59/61) | 0% | **96.7%** | ~3% (~2/61) | 61 | — |
48	| **ISR β=0.1** | s44 | **86.5%** (77/89) | 0% | **86.5%** | ~13.5% (~12/89)³ | 89 | — |
49	| **Random β=0.1** | s42 | **0%** (0/79) | **70.9%** (56/79) | **70.9%** | **29.1%** (23/79) | 79 | **0.2434** (n≥3 prem) |
50	| **Random β=0.1** | s44 | **0%** (0/89) | **79.8%** (71/89) | **79.8%** | **20.2%** (18/89) | 89 | — |
51	| **Convex random** | s42 | 100%² | 0% | 100% | 0% | 100 | — |
52	
53	**Key findings (D051 framing):**
54	
55	1. **H7 is ISR-specific**: ISR 3-seed H7 mean = 64.5% (149/231), Random H7 = 0%. ISR reward specifically induces premise=conclusion hacking.
56	2. **H1 is GRPO-universal**: Random H1 = 71–80%, ISR s42 H1 = 52%. Conclusion embedding is a general GRPO strategy, not ISR-specific.
57	3. **ISR changes hacking composition, not total**: Overall conclusion-in-premise rate is comparable (ISR 67.9% vs Random 70.9% for s42), but ISR converts H1 → more extreme H7.
58	4. **Premise-count-matched: no structural advantage**: ISR genuine (n_prem≥3) = 0.2578, Random genuine (n_prem≥3) = 0.2434. **Ratio = 1.06×**. The apparent 2.4× raw genuine ISR is entirely a premise minimization artifact.
59	5. **SFT has near-zero hacking** (1/14 H1, 0 H7, 92.9% genuine) → hacking is GRPO/RL-specific, not a general finetuning artifact.
60	
61	**Notes:**
62	- ² Tautological collapse (premise=conclusion, 2-component proofs). Classified separately from H7 (which is conclusion duplication with ISR inflation in multi-step context).
63	- ³ s44's 12 "genuine" samples are all n_prem=1 (H7 classifier false negatives — single premise but normalization difference prevented conclusion match).
64	- H7 = single premise identical to conclusion (ISR-inflating shortcut).
65	- H1 = multi-premise proof with conclusion embedded among premises (GRPO-universal shortcut).
66	- Genuine = proved sample with no conclusion duplication detected.
67	- ⁴ Conclusion Embedding % for Random = H1 rate (H7=0% for all Random seeds). s42: 70.9%, s44: 79.8%.
68	- ⁵ s44 eval_results.json reports 97 proved (vs registry 98). H7=97/97=100%.
69	
70	---
71	
72	## Table 3 — Prolog Cross-Logic (Interim)
73	
74	| Condition | Seed | eval PR | eval ISR | proved_only ISR | Components | Hacking Mode |
75	|---|---|---|---|---|---|---|
76	| **Prolog exec-only** | s42 | 0.83 | 0.031 | 0.037 | — | Ground fact enumeration (H7=0%, H1=0%) |
77	| **Prolog exec-only** | s43 | **0.56** | 0.008 | 0.015 | — | Degraded (low PR, near-zero ISR) |
78	| **Prolog exec-only** | s44 | **0.21** | 0.081 | 0.387 | — | Severe degradation (lowest PR, ISR from small sample) |
79	| **Prolog exec-only** | **3-seed mean±std** | **0.53±0.31** | **0.040±0.037** | **0.146±0.210** | — | Extreme seed variance (σ=31pp) |
80	| **Prolog STA (ISR reward)** | s42 | 0.50 | 0.500 | **1.000** | 1.0 | **100% H7** (single clause = query) |
81	
82	**Key findings:**
83	
84	1. **Cross-logic replication of ISR-specific gaming**: Prolog STA s42 H7 = 100% (vs FOL s42 H7 = 16%). Simpler logic semantics → faster, more complete hacking. Prolog model converges to trivial single-clause programs identical to the query.
85	2. **Exec-only Prolog 3-seed**: PR=53.3%±31.1%, ISR=0.040±0.037. Extreme seed variance replicates FOL pattern (FOL exec-only PR=68%±47%).
86	3. **Prolog ISR consistently near-zero**: All 3 seeds ISR<0.1 (mean), confirming exec-only produces no genuine reasoning traces across both logic types.
87	4. **Prolog s44 anomaly**: Lowest PR (21%) but highest proved-only ISR (0.387) — small-sample artifact (21 proved, some by chance have higher ISR).
88	5. **Prolog STA multi-seed**: s43/s44 PENDING, awaiting GPU availability and approval.
89	
90	---
91	
92	## Summary: D051 Claim Support Matrix
93	
94	| Claim | Evidence | Status |
95	|---|---|---|
96	| **C1: ISR as diagnostic** | ISR collapse trajectory: 0.642 (100步) → 0.132 (500步) → 0.003 (1000步) while PR rises 32%→93%→96% | **Supported** (3 timepoints) |
97	| **C2: ISR-as-reward = no structural advantage** | Premise-count-matched ISR: 1.06× (ISR 0.258 vs Random 0.243, n_prem≥3). β=0.1: 2/3 seeds H7>86%. β=0.3: PR 18% < Random 48% | **Supported** (D051 definitive) |
98	| **C2 corollary: hacking composition shift** | ISR: H7=64.5% mean, H1=17%. Random: H7=0%, H1=78%. Total hacking comparable (~70%) | **Supported** |
99	| **SFT = zero hacking** | plan009-r4: PR=14%, ISR=0.08, no hacking patterns detected | **Supported** |
100	| **C3: Cross-logic generality** | Prolog STA H7=100% vs FOL H7=16%. Prolog exec-only 3-seed: PR=53%±31%, ISR=0.040±0.037. Extreme seed variance replicates FOL pattern. | **Supported** (exec-only 3-seed done, STA 1-seed) |
101	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "eb5b7954-c1fd-473d-8da7-d1389c3f22e7",
  "uuid": "8a21b1d1-5ae2-4700-a0ef-82a937f57295",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/evidence_tables_d051.md",
      "content": "# Evidence Tables — D051 Pure Negative Framing\n\n> All eval metrics from `eval_sta.py` (full STA) unless noted. D051 framing: ISR-as-reward provides **no structural advantage**; premise-count-matched ratio = 1.06×.\n\n---\n\n## Table 1 — Main Results (FOL)\n\n| Condition | Seeds | eval PR (mean±std) | eval ISR (mean±std) | proved_only ISR | Components (mean) | Tautological Collapse | Conclusion Embedding % | Hacking Mode |\n|---|---|---|---|---|---|---|---|---|\n| **Base model** (phase0) | 1 (s42) | 0.12 | 0.064±0.198 | — | — | No | — | N/A (no RL) |\n| **SFT baseline** (plan009-r4) | 1 (s42) | 0.14 | 0.080±0.214 | 0.571 | — | No | 7.1% (1/14 H1) | Near-zero hacking (92.9% genuine) |\n| **Exec-only 500步** (plan001) | 3 | 0.68±0.47 | 0.23±0.30 | — | — | 1/3 seeds | — | Heterogeneous† |\n|   ↳ s42 | — | 0.93 | 0.123±0.189 | 0.132 | 6.58 | No | 87.1% (H1) | H1 87.1% (81/93), Genuine 12.9% (12/93) |\n|   ↳ s43 | — | 0.14‡ | 0‡ | — | — | No | — | Repetition collapse |\n|   ↳ s44 | — | 0.98 | 0.570±0.201 | 0.582 | 2.04 | **Yes (94%)** | — | Tautological collapse |\n| **Exec-only 1000步** (plan016) | 1 (s42) | 0.96 | 0.003±0.012 | 0.003 | 18.55 | No | — | Contradiction explosion |\n| **ISR β=0.1** (plan002-b01) | 3 | 0.77±0.14 | 0.55±0.24 | 0.716±0.26 | 4.65 | No | 2/3 seeds | ISR-specific gaming |\n|   ↳ s42 | — | 0.81 | 0.337±0.323 | 0.415 | 5.58 | No | 67.9% | H7 16% + H1 52% |\n|   ↳ s43 | — | 0.61 | 0.506±0.452 | 0.830 | 4.03 | No | 96.7% | **H7 96.7%** (ISR inflation) |\n|   ↳ s44 | — | 0.89 | 0.803±0.342 | 0.902 | 4.33 | No | 86.5% | **H7 86.5%** (ISR inflation) |\n| **Random β=0.1** (plan018) | 2/3§ | 0.84 | 0.083 | 0.100 | 8.46¹ | No | ~75% (H1)⁴ | Redundant premises |\n|   ↳ s42 | — | 0.79 | 0.104±0.137 | 0.131 | 8.46 | No | 70.9% (H1) | H1 70.9% (56/79), H7 0% |\n|   ↳ s44 | — | 0.89 | 0.062±0.176 | 0.070 | — | No | 79.8% (H1) | H1 79.8% (71/89), H7 0% |\n|   ↳ s43 | — | RUNNING | — | — | — | — | — | — |\n| **ISR β=0.3** (plan002-b03) | 1 (s42) | 0.18 | 0.026±0.074 | 0.143 | — | No | — | Format collapse (Goodhart) |\n| **Random β=0.3** (plan017) | 1 (s42) | 0.48 | 0.045±0.076 | 0.094 | 9.60 | No | — | Complexity-without-utility |\n| **Convex random** (plan013-r4) | 1 (s42) | 1.00 | 0.535±0.128 | 0.535 | 2.0 | **Yes (100%)** | 100% | P→P tautological |\n\n**Notes:**\n- † Exec-only 500步 shows extreme seed variance: s42 = conclusion embedding, s43 = repetition collapse, s44 = tautological collapse. 3-seed mean is informative of instability, not a typical outcome.\n- ‡ s43 eval used `do_sample=True, temperature=0.7` (NOT eval_sta.py). 87% samples hit `max_new_tokens`. ISR=0 not comparable to other seeds (C004 violation in historical data).\n- § plan018-s43 still RUNNING; 2-seed interim values reported.\n- ¹ Component count only available for s42.\n\n---\n\n## Table 2 — Hacking Taxonomy\n\n| Condition | Seed | H7 % | H1 % | H7+H1 (total) | Genuine % | n_proved | Premise-matched ISR |\n|---|---|---|---|---|---|---|---|\n| **SFT baseline** | s42 | 0% (0/14) | 7.1% (1/14) | 7.1% | **92.9%** (13/14) | 14 | — |\n| **Exec-only 500步** | s42 | 0% (0/93) | **87.1%** (81/93) | **87.1%** | 12.9% (12/93) | 93 | — |\n| **Exec-only 500步** | s44 | **100%** (97/97) | 0% | **100%** | 0% (0/97) | 97⁵ | — |\n| **Exec-only 1000步** | s42 | — | — | — | — | 96 | — |\n| **ISR β=0.1** | s42 | **16.0%** (13/81) | **51.9%** (42/81) | **67.9%** | **32.1%** (26/81) | 81 | **0.2578** (n≥3 prem) |\n| **ISR β=0.1** | s43 | **96.7%** (59/61) | 0% | **96.7%** | ~3% (~2/61) | 61 | — |\n| **ISR β=0.1** | s44 | **86.5%** (77/89) | 0% | **86.5%** | ~13.5% (~12/89)³ | 89 | — |\n| **Random β=0.1** | s42 | **0%** (0/79) | **70.9%** (56/79) | **70.9%** | **29.1%** (23/79) | 79 | **0.2434** (n≥3 prem) |\n| **Random β=0.1** | s44 | **0%** (0/89) | **79.8%** (71/89) | **79.8%** | **20.2%** (18/89) | 89 | — |\n| **Convex random** | s42 | 100%² | 0% | 100% | 0% | 100 | — |\n\n**Key findings (D051 framing):**\n\n1. **H7 is ISR-specific**: ISR 3-seed H7 mean = 64.5% (149/231), Random H7 = 0%. ISR reward specifically induces premise=conclusion hacking.\n2. **H1 is GRPO-universal**: Random H1 = 71–80%, ISR s42 H1 = 52%. Conclusion embedding is a general GRPO strategy, not ISR-specific.\n3. **ISR changes hacking composition, not total**: Overall conclusion-in-premise rate is comparable (ISR 67.9% vs Random 70.9% for s42), but ISR converts H1 → more extreme H7.\n4. **Premise-count-matched: no structural advantage**: ISR genuine (n_prem≥3) = 0.2578, Random genuine (n_prem≥3) = 0.2434. **Ratio = 1.06×**. The apparent 2.4× raw genuine ISR is entirely a premise minimization artifact.\n5. **SFT has near-zero hacking** (1/14 H1, 0 H7, 92.9% genuine) → hacking is GRPO/RL-specific, not a general finetuning artifact.\n\n**Notes:**\n- ² Tautological collapse (premise=conclusion, 2-component proofs). Classified separately from H7 (which is conclusion duplication with ISR inflation in multi-step context).\n- ³ s44's 12 \"genuine\" samples are all n_prem=1 (H7 classifier false negatives — single premise but normalization difference prevented conclusion match).\n- H7 = single premise identical to conclusion (ISR-inflating shortcut).\n- H1 = multi-premise proof with conclusion embedded among premises (GRPO-universal shortcut).\n- Genuine = proved sample with no conclusion duplication detected.\n- ⁴ Conclusion Embedding % for Random = H1 rate (H7=0% for all Random seeds). s42: 70.9%, s44: 79.8%.\n- ⁵ s44 eval_results.json reports 97 proved (vs registry 98). H7=97/97=100%.\n\n---\n\n## Table 3 — Prolog Cross-Logic (Interim)\n\n| Condition | Seed | eval PR | eval ISR | proved_only ISR | Components | Hacking Mode |\n|---|---|---|---|---|---|---|\n| **Prolog exec-only** | s42 | 0.83 | 0.031 | 0.037 | — | Ground fact enumeration (H7=0%, H1=0%) |\n| **Prolog exec-only** | s43 | **0.56** | 0.008 | 0.015 | — | Degraded (low PR, near-zero ISR) |\n| **Prolog exec-only** | s44 | **0.21** | 0.081 | 0.387 | — | Severe degradation (lowest PR, ISR from small sample) |\n| **Prolog exec-only** | **3-seed mean±std** | **0.53±0.31** | **0.040±0.037** | **0.146±0.210** | — | Extreme seed variance (σ=31pp) |\n| **Prolog STA (ISR reward)** | s42 | 0.50 | 0.500 | **1.000** | 1.0 | **100% H7** (single clause = query) |\n\n**Key findings:**\n\n1. **Cross-logic replication of ISR-specific gaming**: Prolog STA s42 H7 = 100% (vs FOL s42 H7 = 16%). Simpler logic semantics → faster, more complete hacking. Prolog model converges to trivial single-clause programs identical to the query.\n2. **Exec-only Prolog 3-seed**: PR=53.3%±31.1%, ISR=0.040±0.037. Extreme seed variance replicates FOL pattern (FOL exec-only PR=68%±47%).\n3. **Prolog ISR consistently near-zero**: All 3 seeds ISR<0.1 (mean), confirming exec-only produces no genuine reasoning traces across both logic types.\n4. **Prolog s44 anomaly**: Lowest PR (21%) but highest proved-only ISR (0.387) — small-sample artifact (21 proved, some by chance have higher ISR).\n5. **Prolog STA multi-seed**: s43/s44 PENDING, awaiting GPU availability and approval.\n\n---\n\n## Summary: D051 Claim Support Matrix\n\n| Claim | Evidence | Status |\n|---|---|---|\n| **C1: ISR as diagnostic** | ISR collapse trajectory: 0.642 (100步) → 0.132 (500步) → 0.003 (1000步) while PR rises 32%→93%→96% | **Supported** (3 timepoints) |\n| **C2: ISR-as-reward = no structural advantage** | Premise-count-matched ISR: 1.06× (ISR 0.258 vs Random 0.243, n_prem≥3). β=0.1: 2/3 seeds H7>86%. β=0.3: PR 18% < Random 48% | **Supported** (D051 definitive) |\n| **C2 corollary: hacking composition shift** | ISR: H7=64.5% mean, H1=17%. Random: H7=0%, H1=78%. Total hacking comparable (~70%) | **Supported** |\n| **SFT = zero hacking** | plan009-r4: PR=14%, ISR=0.08, no hacking patterns detected | **Supported** |\n| **C3: Cross-logic generality** | Prolog STA H7=100% vs FOL H7=16%. Prolog exec-only 3-seed: PR=53%±31%, ISR=0.040±0.037. Extreme seed variance replicates FOL pattern. | **Supported** (exec-only 3-seed done, STA 1-seed) |\n",
      "numLines": 101,
      "startLine": 1,
      "totalLines": 101
    }
  }
}
```

</details>

---

### Assistant

_source line 12_

<details><summary>Logged reasoning block</summary>

```text
The registry data is too large to read directly. Let me use a subagent to extract the needed data from the registry JSON file, and also check for random_b01 s43 data since the evidence table says it was RUNNING.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eb5b7954-c1fd-473d-8da7-d1389c3f22e7",
  "uuid": "233272c4-64b7-456f-8351-7cf363fc2622",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JdgwAng3VGs95iGqWm6hs5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4577,
      "cache_read_input_tokens": 27532,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4577
      },
      "output_tokens": 8,
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

_source line 13_

Registry data is too large for direct reading. Let me extract the specific metrics I need from the registry file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eb5b7954-c1fd-473d-8da7-d1389c3f22e7",
  "uuid": "c13e0eb5-429e-47de-8d39-28e163518338",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JdgwAng3VGs95iGqWm6hs5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4577,
      "cache_read_input_tokens": 27532,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4577
      },
      "output_tokens": 8,
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

_source line 14_

<details open><summary>🔧 Tool call — Agent · `toolu_01TzDAwzFMhAJ7FWb5HqudYS`</summary>

```json
{
  "description": "Extract registry metrics for table_data.json",
  "prompt": "I need to extract specific experiment metrics from a large registry JSON file at:\n`/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/eb5b7954-c1fd-473d-8da7-d1389c3f22e7/tool-results/mcp-agent-ml-research-read_registry-1778779433924.txt`\n\nThe file has the schema `{result: string}` where result is a JSON string containing experiment entries.\n\nI need you to extract the following data points from the registry. For each experiment, I need: exp_id, status, metrics (especially eval_pr, eval_isr, proved_only_isr, avg_components, h7_rate, h1_rate, genuine_rate, n_proved, hacking_mode), and any conclusion text.\n\nThe experiments I need data for are:\n1. **Base model / phase0** - baseline evaluation\n2. **SFT baseline** - plan009 related\n3. **Exec-only 500 steps** - plan001 seeds s42, s43, s44\n4. **Exec-only 1000 steps** - plan016\n5. **ISR β=0.1** - plan002-b01 seeds s42, s43, s44\n6. **Random β=0.1** - plan018 seeds s42, s43, s44\n7. **ISR β=0.3** - plan002-b03\n8. **Random β=0.3** - plan017\n9. **Convex random** - plan013\n10. **Prolog exec-only** - seeds s42, s43, s44\n11. **Prolog STA** - seeds s42, s43, s44\n12. **Claim2 premise-count-matched data** - any entry with premise_count_matched ISR values\n\nSteps:\n1. First probe the structure: `jq '.result | fromjson | type' file` and `jq '.result | fromjson | length' file` and `jq '.result | fromjson | .[0] | keys' file`\n2. Then extract all experiments with their exp_id, status, metrics, and conclusion fields.\n3. Use jq or python to filter and format.\n\nReport back ALL the numeric values you find - I need exact numbers for every metric. Don't summarize, give me the raw data.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eb5b7954-c1fd-473d-8da7-d1389c3f22e7",
  "uuid": "85ac2433-7ed6-4269-a991-29ce3ff010df",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JdgwAng3VGs95iGqWm6hs5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4577,
      "cache_read_input_tokens": 27532,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4577
      },
      "output_tokens": 8,
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

_source line 15_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "afbb79756989adaac",
  "tool_use_id": "toolu_01TzDAwzFMhAJ7FWb5HqudYS",
  "description": "Extract registry metrics for table_data.json",
  "task_type": "local_agent",
  "prompt": "I need to extract specific experiment metrics from a large registry JSON file at:\n`/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/eb5b7954-c1fd-473d-8da7-d1389c3f22e7/tool-results/mcp-agent-ml-research-read_registry-1778779433924.txt`\n\nThe file has the schema `{result: string}` where result is a JSON string containing experiment entries.\n\nI need you to extract the following data points from the registry. For each experiment, I need: exp_id, status, metrics (especially eval_pr, eval_isr, proved_only_isr, avg_components, h7_rate, h1_rate, genuine_rate, n_proved, hacking_mode), and any conclusion text.\n\nThe experiments I need data for are:\n1. **Base model / phase0** - baseline evaluation\n2. **SFT baseline** - plan009 related\n3. **Exec-only 500 steps** - plan001 seeds s42, s43, s44\n4. **Exec-only 1000 steps** - plan016\n5. **ISR β=0.1** - plan002-b01 seeds s42, s43, s44\n6. **Random β=0.1** - plan018 seeds s42, s43, s44\n7. **ISR β=0.3** - plan002-b03\n8. **Random β=0.3** - plan017\n9. **Convex random** - plan013\n10. **Prolog exec-only** - seeds s42, s43, s44\n11. **Prolog STA** - seeds s42, s43, s44\n12. **Claim2 premise-count-matched data** - any entry with premise_count_matched ISR values\n\nSteps:\n1. First probe the structure: `jq '.result | fromjson | type' file` and `jq '.result | fromjson | length' file` and `jq '.result | fromjson | .[0] | keys' file`\n2. Then extract all experiments with their exp_id, status, metrics, and conclusion fields.\n3. Use jq or python to filter and format.\n\nReport back ALL the numeric values you find - I need exact numbers for every metric. Don't summarize, give me the raw data.",
  "uuid": "3c5e31b8-79b3-4a13-b6fe-784fd93337aa",
  "session_id": "eb5b7954-c1fd-473d-8da7-d1389c3f22e7"
}
```

---

## Round 1

39 recorded events

### User

_source line 16 · 2026-05-14T17:24:09.277Z_

I need to extract specific experiment metrics from a large registry JSON file at:
`/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/eb5b7954-c1fd-473d-8da7-d1389c3f22e7/tool-results/mcp-agent-ml-research-read_registry-1778779433924.txt`

The file has the schema `{result: string}` where result is a JSON string containing experiment entries.

I need you to extract the following data points from the registry. For each experiment, I need: exp_id, status, metrics (especially eval_pr, eval_isr, proved_only_isr, avg_components, h7_rate, h1_rate, genuine_rate, n_proved, hacking_mode), and any conclusion text.

The experiments I need data for are:
1. **Base model / phase0** - baseline evaluation
2. **SFT baseline** - plan009 related
3. **Exec-only 500 steps** - plan001 seeds s42, s43, s44
4. **Exec-only 1000 steps** - plan016
5. **ISR β=0.1** - plan002-b01 seeds s42, s43, s44
6. **Random β=0.1** - plan018 seeds s42, s43, s44
7. **ISR β=0.3** - plan002-b03
8. **Random β=0.3** - plan017
9. **Convex random** - plan013
10. **Prolog exec-only** - seeds s42, s43, s44
11. **Prolog STA** - seeds s42, s43, s44
12. **Claim2 premise-count-matched data** - any entry with premise_count_matched ISR values

Steps:
1. First probe the structure: `jq '.result | fromjson | type' file` and `jq '.result | fromjson | length' file` and `jq '.result | fromjson | .[0] | keys' file`
2. Then extract all experiments with their exp_id, status, metrics, and conclusion fields.
3. Use jq or python to filter and format.

Report back ALL the numeric values you find - I need exact numbers for every metric. Don't summarize, give me the raw data.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01TzDAwzFMhAJ7FWb5HqudYS",
  "session_id": "eb5b7954-c1fd-473d-8da7-d1389c3f22e7",
  "uuid": "4ef83e2a-7545-42b6-b1a2-fa8e55caae5a"
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
  "task_id": "afbb79756989adaac",
  "tool_use_id": "toolu_01TzDAwzFMhAJ7FWb5HqudYS",
  "description": "Running Check file size",
  "usage": {
    "total_tokens": 14678,
    "tool_uses": 1,
    "duration_ms": 5841
  },
  "last_tool_name": "Bash",
  "uuid": "4ae60339-499e-4eda-b594-d3159b9e0c34",
  "session_id": "eb5b7954-c1fd-473d-8da7-d1389c3f22e7"
}
```

---

### Tool call

_source line 18_

<details open><summary>🔧 Tool call — Bash · `toolu_01USGFj6EdYApiWXqmnkzAbi`</summary>

```json
{
  "command": "file=\"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/eb5b7954-c1fd-473d-8da7-d1389c3f22e7/tool-results/mcp-agent-ml-research-read_registry-1778779433924.txt\"\nwc -c \"$file\"",
  "description": "Check file size"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01TzDAwzFMhAJ7FWb5HqudYS",
  "session_id": "eb5b7954-c1fd-473d-8da7-d1389c3f22e7",
  "uuid": "2ec02b8b-407f-40ab-944c-d127c8f7d345",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TnTY2WfhAYUu3k26JQiZj3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6417,
      "cache_read_input_tokens": 8250,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6417,
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

_source line 19 · 2026-05-14T17:24:15.283Z_

<details><summary>↩ Tool result · `toolu_01USGFj6EdYApiWXqmnkzAbi`</summary>

```text
113188 /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/eb5b7954-c1fd-473d-8da7-d1389c3f22e7/tool-results/mcp-agent-ml-research-read_registry-1778779433924.txt
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01TzDAwzFMhAJ7FWb5HqudYS",
  "session_id": "eb5b7954-c1fd-473d-8da7-d1389c3f22e7",
  "uuid": "202892ea-71d2-44c0-8b08-9a7b8a82441e"
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
  "task_id": "afbb79756989adaac",
  "tool_use_id": "toolu_01TzDAwzFMhAJ7FWb5HqudYS",
  "description": "Running Probe JSON structure",
  "usage": {
    "total_tokens": 14682,
    "tool_uses": 2,
    "duration_ms": 9318
  },
  "last_tool_name": "Bash",
  "uuid": "f30c4042-08e8-477e-8a9a-f277cb4e917d",
  "session_id": "eb5b7954-c1fd-473d-8da7-d1389c3f22e7"
}
```

---

### Tool call

_source line 21_

<details open><summary>🔧 Tool call — Bash · `toolu_01Nj9yiH895qihoC2ncxyJmf`</summary>

```json
{
  "command": "file=\"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/eb5b7954-c1fd-473d-8da7-d1389c3f22e7/tool-results/mcp-agent-ml-research-read_registry-1778779433924.txt\"\npython3 -c \"\nimport json\nwith open('$file') as f:\n    raw = json.load(f)\ninner = json.loads(raw['result'])\nprint('Type:', type(inner).__name__)\nif isinstance(inner, dict):\n    print('Top-level keys:', list(inner.keys())[:20])\n    # check if entries are nested\n    for k in list(inner.keys())[:3]:\n        v = inner[k]\n        print(f'  Key={k}, type={type(v).__name__}')\n        if isinstance(v, dict):\n            print(f'    subkeys={list(v.keys())[:15]}')\nelif isinstance(inner, list):\n    print('Length:', len(inner))\n    if len(inner) > 0:\n        print('First entry keys:', list(inner[0].keys()) if isinstance(inner[0], dict) else type(inner[0]))\n\"\n",
  "description": "Probe JSON structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01TzDAwzFMhAJ7FWb5HqudYS",
  "session_id": "eb5b7954-c1fd-473d-8da7-d1389c3f22e7",
  "uuid": "d425cc90-e1fb-45bd-bf89-7fc54ad53954",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TnTY2WfhAYUu3k26JQiZj3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6417,
      "cache_read_input_tokens": 8250,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6417,
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

_source line 22 · 2026-05-14T17:24:18.691Z_

<details><summary>↩ Tool result · `toolu_01Nj9yiH895qihoC2ncxyJmf`</summary>

```text
Type: dict
Top-level keys: ['success', 'data', 'error', 'metadata']
  Key=success, type=bool
  Key=data, type=dict
    subkeys=['experiments', 'count', 'total', 'baseline']
  Key=error, type=NoneType
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01TzDAwzFMhAJ7FWb5HqudYS",
  "session_id": "eb5b7954-c1fd-473d-8da7-d1389c3f22e7",
  "uuid": "21d8eba2-b37d-46df-a73e-91d7e4f71b75"
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
  "task_id": "afbb79756989adaac",
  "tool_use_id": "toolu_01TzDAwzFMhAJ7FWb5HqudYS",
  "description": "Running Explore experiments structure",
  "usage": {
    "total_tokens": 16379,
    "tool_uses": 3,
    "duration_ms": 15487
  },
  "last_tool_name": "Bash",
  "uuid": "7a0366ab-82b7-4c70-864e-dea7ac7bacf3",
  "session_id": "eb5b7954-c1fd-473d-8da7-d1389c3f22e7"
}
```

---

### Tool call

_source line 24_

<details open><summary>🔧 Tool call — Bash · `toolu_01GDGswFghAU5e7CcycsQhY9`</summary>

```json
{
  "command": "file=\"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/eb5b7954-c1fd-473d-8da7-d1389c3f22e7/tool-results/mcp-agent-ml-research-read_registry-1778779433924.txt\"\npython3 -c \"\nimport json\nwith open('$file') as f:\n    raw = json.load(f)\ninner = json.loads(raw['result'])\ndata = inner['data']\nprint('data keys:', list(data.keys()))\nprint('count:', data.get('count'))\nprint('total:', data.get('total'))\nprint('baseline:', data.get('baseline'))\nexps = data.get('experiments', {})\nprint('experiments type:', type(exps).__name__)\nif isinstance(exps, dict):\n    print('Number of experiments:', len(exps))\n    for k in list(exps.keys()):\n        print(f'  exp_id: {k}')\nelif isinstance(exps, list):\n    print('Number of experiments:', len(exps))\n    for e in exps[:5]:\n        print(f'  exp_id: {e.get(\\\"exp_id\\\", \\\"?\\\")}')\n\"\n",
  "description": "Explore experiments structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01TzDAwzFMhAJ7FWb5HqudYS",
  "session_id": "eb5b7954-c1fd-473d-8da7-d1389c3f22e7",
  "uuid": "8e850e73-55da-48fb-9126-7467c2f864a8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015kVYtgFnTvXqB5GRN9PR5J",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1629,
      "cache_read_input_tokens": 14667,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1629,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 70,
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

_source line 25 · 2026-05-14T17:24:24.887Z_

<details><summary>↩ Tool result · `toolu_01GDGswFghAU5e7CcycsQhY9`</summary>

```text
data keys: ['experiments', 'count', 'total', 'baseline']
count: 50
total: 50
baseline: None
experiments type: dict
Number of experiments: 50
  exp_id: plan018-additive-random-b01-s43-r2
  exp_id: plan006-prolog-sta-s44
  exp_id: plan006-prolog-sta-s42
  exp_id: plan006-prolog-sta-s43
  exp_id: plan001-exec-only-s44
  exp_id: plan001-exec-only-s42-r2
  exp_id: plan006-prolog-exec-s44
  exp_id: plan009-sft-baseline-s42-r4
  exp_id: plan006-prolog-exec-s43-r3
  exp_id: plan002-additive-b01-s42
  exp_id: plan018-additive-random-b01-s44
  exp_id: plan009-sft-baseline-s42
  exp_id: plan006-prolog-exec-s43-r2
  exp_id: plan006-prolog-exec-s42
  exp_id: plan006-prolog-exec-s43
  exp_id: plan009-sft-baseline-s42-r3
  exp_id: plan009-sft-baseline-s42-r2
  exp_id: plan018-additive-random-b01-s43
  exp_id: plan002-additive-b01-s44
  exp_id: plan002-additive-b01-s43
  exp_id: plan012-hacking-taxonomy
  exp_id: plan018-additive-random-b01-s42
  exp_id: plan016-extended-1000-s42
  exp_id: plan005-sta-low-s42
  exp_id: plan001-exec-only-s43-r4
  exp_id: plan017-additive-random-s42
  exp_id: plan014-downstream-nli-s42
  exp_id: plan002-additive-b03-s42
  exp_id: plan013-random-reward-s42-r4
  exp_id: plan001-exec-only-s43-r3
  exp_id: plan013-random-reward-s42-r3
  exp_id: plan001-exec-only-s43-r2
  exp_id: plan013-random-reward-s42-r2
  exp_id: plan013-random-reward-s42
  exp_id: plan001-exec-only-s43
  exp_id: plan001-exec-only-s42
  exp_id: plan003-eval-exec-only-r5
  exp_id: plan001-exec-only-s42-r3
  exp_id: sta-phase1-exec-sta-r5
  exp_id: sta-phase1-exec-only-r5
  exp_id: sta-phase1-exec-sta-r4
  exp_id: sta-phase1-exec-only-r4
  exp_id: sta-phase1-exec-only-r3
  exp_id: sta-phase1-exec-sta-r3
  exp_id: sta-phase1-exec-sta-r2
  exp_id: sta-phase1-exec-only-r2
  exp_id: sta-phase1-exec-sta
  exp_id: sta-phase1-exec-only
  exp_id: sta-gt-isr-baseline
  exp_id: sta-phase0-baseline
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01TzDAwzFMhAJ7FWb5HqudYS",
  "session_id": "eb5b7954-c1fd-473d-8da7-d1389c3f22e7",
  "uuid": "870c57cf-cdb9-4c1e-9660-f6411f98620b"
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
  "task_id": "afbb79756989adaac",
  "tool_use_id": "toolu_01TzDAwzFMhAJ7FWb5HqudYS",
  "description": "Running Inspect experiment entry structure",
  "usage": {
    "total_tokens": 17673,
    "tool_uses": 4,
    "duration_ms": 21148
  },
  "last_tool_name": "Bash",
  "uuid": "d1c577b6-f7be-44b4-b768-585dafdbbbc8",
  "session_id": "eb5b7954-c1fd-473d-8da7-d1389c3f22e7"
}
```

---

### Tool call

_source line 27_

<details open><summary>🔧 Tool call — Bash · `toolu_013h9tb4xnZfY8wAaqmqvFdr`</summary>

```json
{
  "command": "file=\"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/eb5b7954-c1fd-473d-8da7-d1389c3f22e7/tool-results/mcp-agent-ml-research-read_registry-1778779433924.txt\"\npython3 -c \"\nimport json\nwith open('$file') as f:\n    raw = json.load(f)\ninner = json.loads(raw['result'])\nexps = inner['data']['experiments']\n\n# First, let's see the keys in one experiment entry\nfirst_key = list(exps.keys())[0]\nfirst_val = exps[first_key]\nprint('Keys in experiment entry:', list(first_val.keys()))\nprint()\nprint('Sample entry (first):', json.dumps(first_val, indent=2, ensure_ascii=False)[:2000])\n\"\n",
  "description": "Inspect experiment entry structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01TzDAwzFMhAJ7FWb5HqudYS",
  "session_id": "eb5b7954-c1fd-473d-8da7-d1389c3f22e7",
  "uuid": "b9050053-64df-4437-9336-c6f556875d62",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LpWCPMt2yy2B1GHzsYmhoj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1292,
      "cache_read_input_tokens": 16296,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1292,
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

_source line 28 · 2026-05-14T17:24:30.525Z_

<details><summary>↩ Tool result · `toolu_013h9tb4xnZfY8wAaqmqvFdr`</summary>

```text
Keys in experiment entry: ['status', 'retry_count', 'created_at', 'updated_at', 'hypothesis', 'parent', 'server', 'gpu', 'account', 'command', 'spec', 'pid', 'log_path', 'reproduce', 'extra', 'metrics', 'conclusion', 'completed_at']

Sample entry (first): {
  "status": "DONE",
  "retry_count": 0,
  "created_at": "2026-05-14T14:01:24.111Z",
  "updated_at": "2026-05-14T17:17:02.398Z",
  "hypothesis": "Random β=0.1 seed=43 控制组 r2: 重试 (原 s43 step 200 磁盘满崩溃)。与 plan002-b01-s43 (ISR β=0.1) 同 seed 对照。3-seed mean±std 审稿硬性要求。",
  "parent": "plan018-additive-random-b01-s43",
  "server": "westd-39279",
  "gpu": "cuda:0",
  "account": "root",
  "command": "bash -c \"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_random_b01.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 43 --beta 0.1 --reward_mode additive_random --output_dir /root/autodl-tmp/outputs/plan018_additive_random_b01_s43_r2\"",
  "spec": {
    "command": "bash -c \"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 scripts/train_grpo.py --config configs/grpo_additive_random_b01.yaml --data_path data/train_500_seed42.jsonl --num_steps 500 --seed 43 --beta 0.1 --reward_mode additive_random --output_dir /root/autodl-tmp/outputs/plan018_additive_random_b01_s43_r2\"",
    "server": "westd-39279",
    "gpu": [
      "cuda:0"
    ],
    "pid": "858386",
    "log_path": "~/runs/solver-trace-ablation/plan018-additive-random-b01-s43-r2.log",
    "submitted_at": "2026-05-14T15:24:32.942Z",
    "submitted_via": "submit_training_job",
    "backend": "tmux",
    "account": "root",
    "checkpoint_path": "/root/autodl-tmp/outputs/plan018_additive_random_b01_s43_r2",
    "wall_clock_seconds": 6748.8,
    "gpu_hours": 1.87
  },
  "pid": "858386",
  "log_path": "~/runs/solver-trace-ablation/plan018-additive-random-b01-s43-r2.log",
  "reproduce": {
    "command": "bash -c \"export CUDA_VISIBLE_DEVICES=0 && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/solver-trace-ablation && python3 sc
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01TzDAwzFMhAJ7FWb5HqudYS",
  "session_id": "eb5b7954-c1fd-473d-8da7-d1389c3f22e7",
  "uuid": "f60e26c8-2569-4855-8002-4f5abff4b829"
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
  "task_id": "afbb79756989adaac",
  "tool_use_id": "toolu_01TzDAwzFMhAJ7FWb5HqudYS",
  "description": "Running Extract all experiment details for target experiments",
  "usage": {
    "total_tokens": 18951,
    "tool_uses": 5,
    "duration_ms": 33975
  },
  "last_tool_name": "Bash",
  "uuid": "dd9617e8-1233-4f66-9ea2-cbcb6d391beb",
  "session_id": "eb5b7954-c1fd-473d-8da7-d1389c3f22e7"
}
```

---

### Tool call

_source line 30_

<details open><summary>🔧 Tool call — Bash · `toolu_01Pu1rcvaj6gvSwjVMnmVftH`</summary>

```json
{
  "command": "file=\"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/eb5b7954-c1fd-473d-8da7-d1389c3f22e7/tool-results/mcp-agent-ml-research-read_registry-1778779433924.txt\"\npython3 << 'PYEOF'\nimport json\n\nwith open(r'/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/eb5b7954-c1fd-473d-8da7-d1389c3f22e7/tool-results/mcp-agent-ml-research-read_registry-1778779433924.txt') as f:\n    raw = json.load(f)\ninner = json.loads(raw['result'])\nexps = inner['data']['experiments']\n\n# Target experiment IDs (patterns)\ntargets = [\n    'sta-phase0-baseline',\n    'sta-gt-isr-baseline',\n    'plan009',\n    'plan001-exec-only-s42',\n    'plan001-exec-only-s43',\n    'plan001-exec-only-s44',\n    'plan001-exec-only-s42-r2',\n    'plan001-exec-only-s42-r3',\n    'plan001-exec-only-s43-r2',\n    'plan001-exec-only-s43-r3',\n    'plan001-exec-only-s43-r4',\n    'plan016',\n    'plan002-additive-b01-s42',\n    'plan002-additive-b01-s43',\n    'plan002-additive-b01-s44',\n    'plan018-additive-random-b01-s42',\n    'plan018-additive-random-b01-s43',\n    'plan018-additive-random-b01-s44',\n    'plan018-additive-random-b01-s43-r2',\n    'plan002-additive-b03-s42',\n    'plan017-additive-random-s42',\n    'plan013-random-reward',\n    'plan006-prolog-exec',\n    'plan006-prolog-sta',\n    'plan003-eval-exec-only',\n    'sta-phase1-exec-only',\n    'sta-phase1-exec-sta',\n    'plan005-sta-low',\n    'plan012-hacking-taxonomy',\n    'plan014-downstream-nli',\n]\n\nfor exp_id, exp in sorted(exps.items()):\n    matched = False\n    for t in targets:\n        if exp_id.startswith(t) or exp_id == t:\n            matched = True\n            break\n    if not matched:\n        continue\n    \n    print(\"=\" * 80)\n    print(f\"EXP_ID: {exp_id}\")\n    print(f\"STATUS: {exp.get('status')}\")\n    print(f\"HYPOTHESIS: {exp.get('hypothesis', 'N/A')}\")\n    \n    metrics = exp.get('metrics')\n    if metrics:\n        print(f\"METRICS: {json.dumps(metrics, indent=2, ensure_ascii=False)}\")\n    else:\n        print(\"METRICS: None\")\n    \n    conclusion = exp.get('conclusion')\n    if conclusion:\n        print(f\"CONCLUSION: {conclusion}\")\n    else:\n        print(\"CONCLUSION: None\")\n    \n    # Also check extra for any relevant data\n    extra = exp.get('extra')\n    if extra:\n        print(f\"EXTRA: {json.dumps(extra, indent=2, ensure_ascii=False)}\")\n    \n    print()\n\nPYEOF\n",
  "description": "Extract all experiment details for target experiments",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01TzDAwzFMhAJ7FWb5HqudYS",
  "session_id": "eb5b7954-c1fd-473d-8da7-d1389c3f22e7",
  "uuid": "dcf462af-661b-490b-bd89-42fc7c297873",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012MmhmzHYWHKBGWHPMyAw8d",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1276,
      "cache_read_input_tokens": 17588,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1276,
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

_source line 31 · 2026-05-14T17:24:43.349Z_

<details><summary>↩ Tool result · `toolu_01Pu1rcvaj6gvSwjVMnmVftH`</summary>

```text
&lt;persisted-output>
Output too large (35.3KB). Full output saved to: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/eb5b7954-c1fd-473d-8da7-d1389c3f22e7/tool-results/bwuszvmvo.txt

Preview (first 2KB):
================================================================================
EXP_ID: plan001-exec-only-s42
STATUS: DONE
HYPOTHESIS: N/A
METRICS: None
CONCLUSION: failed

================================================================================
EXP_ID: plan001-exec-only-s42-r2
STATUS: DONE
HYPOTHESIS: N/A
METRICS: {
  "eval_prove_rate": 0.93,
  "eval_mean_isr": 0.1232,
  "eval_isr_std": 0.1887,
  "eval_proved_only_isr": 0.1324,
  "eval_median_isr": 0,
  "eval_n_proved": 93,
  "eval_n_problems": 100,
  "eval_method": "eval_sta.py full STA",
  "eval_data": "proofwriter_fol_100.jsonl",
  "h7_rate": 0,
  "h7_count": 0,
  "h1_rate": 0.871,
  "h1_count": 81,
  "genuine_rate": 0.129,
  "genuine_count": 12,
  "genuine_mean_isr": 0.3141,
  "h1_mean_isr": 0.1055,
  "conclusion_embedding_total": 0.871
}
CONCLUSION: success
EXTRA: {
  "previous_failure": {
    "conclusion": "failed"
  },
  "hook_events": [
    {
      "event": "on_complete",
      "action": "agent",
      "ts": "2026-05-13T23:46:01.596431+00:00"
    }
  ]
}

================================================================================
EXP_ID: plan001-exec-only-s42-r3
STATUS: DONE
HYPOTHESIS: N/A
METRICS: None
CONCLUSION: failed

================================================================================
EXP_ID: plan001-exec-only-s43
STATUS: DONE
HYPOTHESIS: N/A
METRICS: None
CONCLUSION: failed

================================================================================
EXP_ID: plan001-exec-only-s43-r2
STATUS: DONE
HYPOTHESIS: N/A
METRICS: None
CONCLUSION: failed

================================================================================
EXP_ID: plan001-exec-only-s43-r3
STATUS: DONE
HYPOTHESIS: N/A
METRICS: None
CONCLUSION: failed

================================================================================
EXP_ID: plan001-exec-only-s43-r4
STATUS: DONE
HYPOTHESIS: N/A
METRICS: {
  "eval_sampling_prove_rate": 0.14,
  "eval_sampling_mean_isr": 0,
  "eval_sampling_n_proved": 14,
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01TzDAwzFMhAJ7FWb5HqudYS",
  "session_id": "eb5b7954-c1fd-473d-8da7-d1389c3f22e7",
  "uuid": "2fafa726-7136-4841-821a-a5697018389a"
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
  "task_id": "afbb79756989adaac",
  "tool_use_id": "toolu_01TzDAwzFMhAJ7FWb5HqudYS",
  "description": "Reading ~/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/eb5b7954-c1fd-473d-8da7-d1389c3f22e7/tool-results/bwuszvmvo.txt",
  "usage": {
    "total_tokens": 20830,
    "tool_uses": 6,
    "duration_ms": 36998
  },
  "last_tool_name": "Read",
  "uuid": "a11e90d3-26ab-4671-b022-362eec184758",
  "session_id": "eb5b7954-c1fd-473d-8da7-d1389c3f22e7"
}
```

---

### Tool call

_source line 33_

<details open><summary>🔧 Tool call — Read · `toolu_016qnG2iBxQyanoydujW1x9Z`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/eb5b7954-c1fd-473d-8da7-d1389c3f22e7/tool-results/bwuszvmvo.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01TzDAwzFMhAJ7FWb5HqudYS",
  "session_id": "eb5b7954-c1fd-473d-8da7-d1389c3f22e7",
  "uuid": "0076c525-fa9d-465a-b83a-66b60aaa1537",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QfWrWfPHQAt8LTZyofvcyF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1865,
      "cache_read_input_tokens": 18864,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1865,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 7,
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

_source line 34 · 2026-05-14T17:24:46.541Z_

<details><summary>↩ Tool result · `toolu_016qnG2iBxQyanoydujW1x9Z`</summary>

```text
1	================================================================================
2	EXP_ID: plan001-exec-only-s42
3	STATUS: DONE
4	HYPOTHESIS: N/A
5	METRICS: None
6	CONCLUSION: failed
7	
8	================================================================================
9	EXP_ID: plan001-exec-only-s42-r2
10	STATUS: DONE
11	HYPOTHESIS: N/A
12	METRICS: {
13	  "eval_prove_rate": 0.93,
14	  "eval_mean_isr": 0.1232,
15	  "eval_isr_std": 0.1887,
16	  "eval_proved_only_isr": 0.1324,
17	  "eval_median_isr": 0,
18	  "eval_n_proved": 93,
19	  "eval_n_problems": 100,
20	  "eval_method": "eval_sta.py full STA",
21	  "eval_data": "proofwriter_fol_100.jsonl",
22	  "h7_rate": 0,
23	  "h7_count": 0,
24	  "h1_rate": 0.871,
25	  "h1_count": 81,
26	  "genuine_rate": 0.129,
27	  "genuine_count": 12,
28	  "genuine_mean_isr": 0.3141,
29	  "h1_mean_isr": 0.1055,
30	  "conclusion_embedding_total": 0.871
31	}
32	CONCLUSION: success
33	EXTRA: {
34	  "previous_failure": {
35	    "conclusion": "failed"
36	  },
37	  "hook_events": [
38	    {
39	      "event": "on_complete",
40	      "action": "agent",
41	      "ts": "2026-05-13T23:46:01.596431+00:00"
42	    }
43	  ]
44	}
45	
46	================================================================================
47	EXP_ID: plan001-exec-only-s42-r3
48	STATUS: DONE
49	HYPOTHESIS: N/A
50	METRICS: None
51	CONCLUSION: failed
52	
53	================================================================================
54	EXP_ID: plan001-exec-only-s43
55	STATUS: DONE
56	HYPOTHESIS: N/A
57	METRICS: None
58	CONCLUSION: failed
59	
60	================================================================================
61	EXP_ID: plan001-exec-only-s43-r2
62	STATUS: DONE
63	HYPOTHESIS: N/A
64	METRICS: None
65	CONCLUSION: failed
66	
67	================================================================================
68	EXP_ID: plan001-exec-only-s43-r3
69	STATUS: DONE
70	HYPOTHESIS: N/A
71	METRICS: None
72	CONCLUSION: failed
73	
74	================================================================================
75	EXP_ID: plan001-exec-only-s43-r4
76	STATUS: DONE
77	HYPOTHESIS: N/A
78	METRICS: {
79	  "eval_sampling_prove_rate": 0.14,
80	  "eval_sampling_mean_isr": 0,
81	  "eval_sampling_n_proved": 14,
82	  "eval_sampling_temperature": 0.7,
83	  "eval_sampling_method": "do_sample=True, temperature=0.7",
84	  "eval_sampling_by_answer": {
85	    "true": {
86	      "count": 34,
87	      "proved": 6,
88	      "prove_rate": 0.176
89	    },
90	    "false": {
91	      "count": 25,
92	      "proved": 2,
93	      "prove_rate": 0.08
94	    },
95	    "unknown": {
96	      "count": 41,
97	      "proved": 6,
98	      "prove_rate": 0.146
99	    }
100	  }
101	}
102	CONCLUSION: negative
103	EXTRA: {
104	  "hook_events": [
105	    {
106	      "event": "on_complete",
107	      "action": "agent",
108	      "ts": "2026-05-14T03:13:12.957272+00:00"
109	    }
110	  ]
111	}
112	
113	================================================================================
114	EXP_ID: plan001-exec-only-s44
115	STATUS: DONE
116	HYPOTHESIS: Exec-only seed=44 第3 seed: 解决 s42(93% eval PR) vs s43(13% eval PR) 的跨 seed 不稳定问题，3-seed mean±std 是论文必需。
117	METRICS: {
118	  "eval_prove_rate": 0.98,
119	  "eval_mean_isr": 0.57,
120	  "eval_isr_std": 0.2013,
121	  "eval_median_isr": 0.5,
122	  "eval_proved_only_isr": 0.5816,
123	  "eval_n_proved": 98,
124	  "eval_n_problems": 100,
125	  "eval_method": "eval_sta.py full STA",
126	  "eval_data": "proofwriter_fol_100.jsonl",
127	  "eval_component_count_mean": 2.04,
128	  "eval_component_count_2": 94,
129	  "eval_component_count_3": 4,
130	  "tautological_collapse": true,
131	  "h7_rate": 1,
132	  "h7_count": 97,
133	  "h1_rate": 0,
134	  "h1_count": 0,
135	  "genuine_rate": 0,
136	  "genuine_count": 0,
137	  "conclusion_embedding_total": 1
138	}
139	CONCLUSION: negative
140	EXTRA: {
141	  "hook_events": [
142	    {
143	      "event": "on_complete",
144	      "action": "agent",
145	      "ts": "2026-05-14T05:06:40.707032+00:00"
146	    }
147	  ]
148	}
149	
150	================================================================================
151	EXP_ID: plan002-additive-b01-s42
152	STATUS: DONE
153	HYPOTHESIS: N/A
154	METRICS: {
155	  "eval_prove_rate": 0.81,
156	  "eval_mean_isr": 0.3365,
157	  "eval_isr_std": 0.3227,
158	  "eval_proved_only_isr": 0.4154,
159	  "eval_median_isr": 0.2,
160	  "eval_n_proved": 81,
161	  "eval_n_problems": 100,
162	  "eval_method": "eval_sta.py full STA",
163	  "eval_data": "proofwriter_fol_100.jsonl",
164	  "eval_component_count_mean": 5.58,
165	  "eval_component_count_2_ratio": 0.037,
166	  "eval_isr_1_ratio": 0.124,
167	  "eval_isr_0_ratio": 0.037,
168	  "eval_by_type_false_pr": 0.88,
169	  "eval_by_type_false_isr": 0.3515,
170	  "eval_by_type_unknown_pr": 0.83,
171	  "eval_by_type_unknown_isr": 0.3684,
172	  "eval_by_type_true_pr": 0.74,
173	  "eval_by_type_true_isr": 0.2869,
174	  "tautological_collapse": false,
175	  "train_total_steps": 500,
176	  "train_duration_min": 63,
177	  "train_last100_pr": 0.6875,
178	  "train_last100_isr": 0.1954,
179	  "train_last100_loss": 0.015
180	}
181	CONCLUSION: success
182	EXTRA: {
183	  "hook_events": [
184	    {
185	      "event": "on_complete",
186	      "action": "agent",
187	      "ts": "2026-05-14T06:37:59.656631+00:00"
188	    }
189	  ]
190	}
191	
192	================================================================================
193	EXP_ID: plan002-additive-b01-s43
194	STATUS: DONE
195	HYPOTHESIS: ISR β=0.1 seed=43 多 seed 验证：plan002-b01-s42 (PR=0.81, ISR=0.337) 在 s43 下是否可复现？exec-only s43 是 degraded seed (PR=14%)，ISR β=0.1 能否拯救 bad seed？3-seed mean±std 用于论文 Claim 2 统计支撑。
196	METRICS: {
197	  "eval_prove_rate": 0.61,
198	  "eval_mean_isr": 0.5063,
199	  "eval_isr_std": 0.4518,
200	  "eval_median_isr": 0.5,
201	  "eval_proved_only_isr": 0.8301,
202	  "component_count_mean": 4.03,
203	  "component_count_2_ratio": 0,
204	  "tautological_collapse": false,
205	  "isr_0_ratio": 0.39,
206	  "isr_1_ratio": 0.656,
207	  "proved_single_premise_ratio": 1,
208	  "h7_rate_calibrated": 0.967,
209	  "h7_definition": "single_premise AND premise==conclusion (normalized)",
210	  "hacking_mode": "conclusion_duplication_isr_inflation",
211	  "conclusion_embedding": true,
212	  "by_answer_type": {
213	    "false": {
214	      "n": 25,
215	      "proved": 18,
216	      "PR": 0.72,
217	      "ISR": 0.6
218	    },
219	    "unknown": {
220	      "n": 41,
221	      "proved": 22,
222	      "PR": 0.537,
223	      "ISR": 0.442
224	    },
225	    "true": {
226	      "n": 34,
227	      "proved": 21,
228	      "PR": 0.618,
229	      "ISR": 0.515
230	    }
231	  },
232	  "train_total_steps": 500,
233	  "train_duration_min": 53,
234	  "train_loss": 0.012
235	}
236	CONCLUSION: negative
237	EXTRA: {
238	  "hook_events": [
239	    {
240	      "event": "on_complete",
241	      "action": "agent",
242	      "ts": "2026-05-14T09:41:25.536028+00:00"
243	    }
244	  ]
245	}
246	
247	================================================================================
248	EXP_ID: plan002-additive-b01-s44
249	STATUS: DONE
250	HYPOTHESIS: ISR β=0.1 seed=44 多 seed 验证：exec-only s44 是 tautological collapse (PR=98%, ISR=0.57 fake)，ISR β=0.1 能否防止 tautological collapse？3-seed mean±std 用于论文 Claim 2。
251	METRICS: {
252	  "eval_prove_rate": 0.89,
253	  "eval_mean_isr": 0.803,
254	  "eval_isr_std": 0.3418,
255	  "eval_median_isr": 1,
256	  "component_count_mean": 4.33,
257	  "component_count_2_ratio": 0.022,
258	  "tautological_collapse": false,
259	  "isr_0_ratio": 0.12,
260	  "isr_1_ratio": 0.73,
261	  "proved_single_premise_ratio": 1,
262	  "h7_rate_calibrated": 0.865,
263	  "h7_definition": "single_premise AND premise==conclusion (normalized)",
264	  "hacking_mode": "conclusion_duplication_isr_inflation",
265	  "conclusion_embedding": true,
266	  "component_dist": {
267	    "2": 2,
268	    "4": 54,
269	    "5": 33
270	  },
271	  "by_answer_type": {
272	    "false": {
273	      "n": 25,
274	      "proved": 22,
275	      "PR": 0.88,
276	      "ISR": 0.824
277	    },
278	    "unknown": {
279	      "n": 41,
280	      "proved": 38,
281	      "PR": 0.927,
282	      "ISR": 0.837
283	    },
284	    "true": {
285	      "n": 34,
286	      "proved": 29,
287	      "PR": 0.853,
288	      "ISR": 0.747
289	    }
290	  }
291	}
292	CONCLUSION: negative
293	EXTRA: {
294	  "hook_events": [
295	    {
296	      "event": "on_complete",
297	      "action": "agent",
298	      "ts": "2026-05-14T09:28:12.416418+00:00"
299	    }
300	  ]
301	}
302	
303	================================================================================
304	EXP_ID: plan002-additive-b03-s42
305	STATUS: DONE
306	HYPOTHESIS: N/A
307	METRICS: {
308	  "total_steps": 500,
309	  "duration_min": 56.7,
310	  "overall_prove_rate": 0.34025,
311	  "overall_isr": 0.11527,
312	  "first20_prove_rate": 0.15625,
313	  "last50_prove_rate": 0.555,
314	  "last100_prove_rate": 0.5525,
315	  "mean_loss": 0.008914,
316	  "last100_loss": 0.014469,
317	  "parse_rate": 1,
318	  "w1_50_prove_rate": 0.13,
319	  "w51_100_prove_rate": 0.095,
320	  "w101_200_prove_rate": 0.185,
321	  "w201_300_prove_rate": 0.375,
322	  "w301_400_prove_rate": 0.47625,
323	  "w401_500_prove_rate": 0.5525,
324	  "steps_ge_085": 52,
325	  "first_step_ge_085": 46,
326	  "final_prove_rate": 1,
327	  "final_isr_mean": 0.3089,
328	  "final_reward_mean": 1.0927
329	}
330	CONCLUSION: negative
331	EXTRA: {
332	  "hook_events": [
333	    {
334	      "event": "on_complete",
335	      "action": "agent",
336	      "ts": "2026-05-14T03:24:48.666027+00:00"
337	    }
338	  ]
339	}
340	
341	================================================================================
342	EXP_ID: plan003-eval-exec-only-r5
343	STATUS: DONE
344	HYPOTHESIS: N/A
345	METRICS: {
346	  "prove_rate": 0.32,
347	  "mean_isr": 0.2055,
348	  "isr_std": 0.3194,
349	  "proved_only_isr": 0.6423,
350	  "isr_by_type": {
351	    "true": 0.3598,
352	    "false": 0.1723,
353	    "unknown": 0.0979
354	  },
355	  "total_samples": 100,
356	  "proved_count": 32,
357	  "runtime_s": 251.7
358	}
359	CONCLUSION: success
360	
361	================================================================================
362	EXP_ID: plan005-sta-low-s42
363	STATUS: DONE
364	HYPOTHESIS: N/A
365	METRICS: {
366	  "total_steps": 500,
367	  "duration_min": 71,
368	  "parse_rate": 1,
369	  "overall_prove_rate": 0.5657,
370	  "overall_isr": 0.1682,
371	  "last50_prove_rate": 0.77,
372	  "last50_isr": 0.2559,
373	  "last100_prove_rate": 0.7725,
374	  "last100_isr": 0.2299,
375	  "last100_loss": 0.022752,
376	  "overall_loss": 0.017296,
377	  "last100_isr_pr_ratio": 0.298,
378	  "last100_isr_lt_pr_count": "99/100",
379	  "first_rolling10_pr_ge_0.8": 178,
380	  "first_rolling10_pr_ge_0.9": 439,
381	  "max_rolling10_pr": 0.9375,
382	  "max_rolling10_isr": 0.3282,
383	  "windowed": {
384	    "1-50": {
385	      "pr": 0.1775,
386	      "isr": 0.0906
387	    },
388	    "51-100": {
389	      "pr": 0.1775,
390	      "isr": 0.0835
391	    },
392	    "101-200": {
393	      "pr": 0.5062,
394	      "isr": 0.1463
395	    },
396	    "201-300": {
397	      "pr": 0.6713,
398	      "isr": 0.1791
399	    },
400	    "301-400": {
401	      "pr": 0.7013,
402	      "isr": 0.1984
403	    },
404	    "401-500": {
405	      "pr": 0.7725,
406	      "isr": 0.2299
407	    }
408	  }
409	}
410	CONCLUSION: negative
411	EXTRA: {
412	  "hook_events": [
413	    {
414	      "event": "on_complete",
415	      "action": "agent",
416	      "ts": "2026-05-13T23:55:06.559440+00:00"
417	    }
418	  ]
419	}
420	
421	================================================================================
422	EXP_ID: plan006-prolog-exec-s42
423	STATUS: DONE
424	HYPOTHESIS: Prolog exec-only GRPO seed=42: STA/ISR hacking patterns generalize across logic types? Prolog uses rule ablation (vs FOL axiom ablation). If same degeneration modes appear → STA is logic-agnostic diagnostic.
425	METRICS: {
426	  "eval_prove_rate": 0.83,
427	  "eval_mean_isr": 0.031,
428	  "eval_proved_only_isr": 0.037,
429	  "eval_median_isr": 0,
430	  "eval_max_isr": 0.2,
431	  "eval_isr_std": 0.0534,
432	  "h7_rate": 0,
433	  "h1_rate": 0,
434	  "isr_1_rate": 0,
435	  "single_premise_rate": 0,
436	  "by_answer_type": {
437	    "true": {
438	      "proved": 37,
439	      "count": 40,
440	      "pr": 0.925,
441	      "isr": 0.037
442	    },
443	    "false": {
444	      "proved": 21,
445	      "count": 29,
446	      "pr": 0.724,
447	      "isr": 0.038
448	    },
449	    "unknown": {
450	      "proved": 25,
451	      "count": 31,
452	      "pr": 0.806,
453	      "isr": 0.016
454	    }
455	  }
456	}
457	CONCLUSION: negative
458	EXTRA: {
459	  "hook_events": [
460	    {
461	      "event": "on_failed",
462	      "action": "agent",
463	      "ts": "2026-05-14T09:47:38.546001+00:00"
464	    },
465	    {
466	      "event": "on_complete",
467	      "action": "agent",
468	      "ts": "2026-05-14T11:29:27.709792+00:00"
469	    }
470	  ],
471	  "previous_failure": {
472	    "conclusion": "failed",
473	    "notes": "失败原因: FileNotFoundError — data/prolog/train_500_seed42.jsonl 不存在 | error_type: data | 同一原因影响所有 plan006 实验 (exec/sta × s42/s43/s44) | 建议: 需先生成 Prolog 训练数据再重试"
474	  }
475	}
476	
477	================================================================================
478	EXP_ID: plan006-prolog-exec-s43
479	STATUS: DONE
480	HYPOTHESIS: Prolog exec-only GRPO seed=43: cross-seed stability check for Prolog logic type. FOL showed extreme cross-seed variance (s42 genuine vs s43 degraded vs s44 tautological). Prolog exec-only s42 showed PR=83%, ISR=0.031. s43 tests if Prolog also has seed instability.
481	METRICS: None
482	CONCLUSION: killed
483	
484	================================================================================
485	EXP_ID: plan006-prolog-exec-s43-r2
486	STATUS: DONE
487	HYPOTHESIS: Prolog exec-only GRPO seed=43 r2: 修正 warmup_ratio=0.0 与 s42 一致。cross-seed stability check for Prolog logic type.
488	METRICS: None
489	CONCLUSION: failed
490	EXTRA: {
491	  "hook_events": [
492	    {
493	      "event": "on_failed",
494	      "action": "agent",
495	      "ts": "2026-05-14T12:35:23.802887+00:00"
496	    }
497	  ]
498	}
499	
500	================================================================================
501	EXP_ID: plan006-prolog-exec-s43-r3
502	STATUS: DONE
503	HYPOTHESIS: Prolog exec-only GRPO seed=43 r3: warmup_ratio=0.0 与 s42 一致。r2 因残留进程 OOM 失败，cuda:1 已清理。
504	METRICS: {
505	  "eval_prove_rate": 0.56,
506	  "eval_mean_isr": 0.0084,
507	  "eval_isr_std": 0.0221,
508	  "eval_median_isr": 0,
509	  "eval_proved_only_isr": 0.015,
510	  "eval_min_isr": 0,
511	  "eval_max_isr": 0.1,
512	  "eval_n_proved": 56,
513	  "eval_n_problems": 100,
514	  "eval_method": "eval_sta.py full STA",
515	  "eval_data": "proofwriter_fol_100.jsonl",
516	  "eval_elapsed_seconds": 868.2,
517	  "eval_by_type_false_pr": 0.48,
518	  "eval_by_type_false_isr": 0.0043,
519	  "eval_by_type_unknown_pr": 0.6585,
520	  "eval_by_type_unknown_isr": 0.0114,
521	  "eval_by_type_true_pr": 0.5,
522	  "eval_by_type_true_isr": 0.0078,
523	  "solver": "PrologSolver",
524	  "logic_type": "prolog"
525	}
526	CONCLUSION: negative
527	EXTRA: {
528	  "hook_events": [
529	    {
530	      "event": "on_complete",
531	      "action": "agent",
532	      "ts": "2026-05-14T15:54:27.521808+00:00"
533	    }
534	  ]
535	}
536	
537	================================================================================
538	EXP_ID: plan006-prolog-exec-s44
539	STATUS: DONE
540	HYPOTHESIS: Prolog exec-only GRPO seed=44: third seed for Prolog exec-only. Together with s42 (PR=83%, ISR=0.031) and s43, provides 3-seed evidence for cross-logic generalization claim (Claim 3). 3-seed mean±std required for paper.
541	METRICS: {
542	  "eval_prove_rate": 0.21,
543	  "eval_mean_isr": 0.0812,
544	  "eval_isr_std": 0.2343,
545	  "eval_median_isr": 0,
546	  "eval_proved_only_isr": 0.3866,
547	  "eval_min_isr": 0,
548	  "eval_max_isr": 1,
549	  "eval_n_proved": 21,
550	  "eval_n_problems": 100,
551	  "eval_method": "eval_sta.py full STA",
552	  "eval_data": "proofwriter_fol_100.jsonl",
553	  "eval_elapsed_seconds": 683.9,
554	  "eval_by_type_false_pr": 0.04,
555	  "eval_by_type_false_isr": 0.04,
556	  "eval_by_type_unknown_pr": 0.317,
557	  "eval_by_type_unknown_isr": 0.099,
558	  "eval_by_type_true_pr": 0.206,
559	  "eval_by_type_true_isr": 0.09,
560	  "solver": "PrologSolver",
561	  "logic_type": "prolog"
562	}
563	CONCLUSION: negative
564	EXTRA: {
565	  "hook_events": [
566	    {
567	      "event": "on_complete",
568	      "action": "agent",
569	      "ts": "2026-05-14T15:20:44.093424+00:00"
570	    }
571	  ]
572	}
573	
574	================================================================================
575	EXP_ID: plan006-prolog-sta-s42
576	STATUS: DONE
577	HYPOTHESIS: Prolog exec+STA GRPO seed=42: ISR reward 在 Prolog logic type 上的效果。与 plan006-prolog-exec-s42 (exec-only) 对照，验证 STA/ISR 的 hacking 检测和 Goodhart 效应是否跨 logic type 泛化。
578	METRICS: {
579	  "cumulative_prove_rate": 0.848,
580	  "cumulative_mean_isr": 0.787,
581	  "final_prove_rate": 1,
582	  "final_isr": 1,
583	  "final_reward": 1,
584	  "saturation_onset_step": 100,
585	  "train_loss": 0.00716,
586	  "training_hours": 0.78,
587	  "final_entropy": 0.01,
588	  "final_completion_length": 27,
589	  "initial_completion_length": 120,
590	  "steps_at_perfect_reward": 400,
591	  "train_runtime_sec": 2791,
592	  "eval_prove_rate": 0.5,
593	  "eval_mean_isr": 0.5,
594	  "eval_proved_only_isr": 1,
595	  "eval_h7_rate": 1,
596	  "eval_h7_count": 50,
597	  "eval_proved_count": 50,
598	  "eval_total_count": 100,
599	  "eval_n_clauses_mean": 1,
600	  "eval_isr_distribution": "binary: 50x0 + 50x1"
601	}
602	CONCLUSION: negative
603	EXTRA: {
604	  "hook_events": [
605	    {
606	      "event": "on_failed",
607	      "action": "agent",
608	      "ts": "2026-05-14T09:46:02.621139+00:00"
609	    },
610	    {
611	      "event": "on_complete",
612	      "action": "agent",
613	      "ts": "2026-05-14T10:38:15.900825+00:00"
614	    }
615	  ],
616	  "previous_failure": {
617	    "conclusion": "failed",
618	    "notes": "第二次启动失败。根因：config reward_mode=execution_sta (0.5*exec+0.5*ISR) 可能与 FOL 实验不匹配，待 Director 确认后修复重启。cuda:1 释放给 plan018。"
619	  }
620	}
621	
622	================================================================================
623	EXP_ID: plan006-prolog-sta-s43
624	STATUS: RUNNING
625	HYPOTHESIS: Prolog exec+STA GRPO seed=43: 跨 seed 稳定性检查。与 exec-only s43 对照。
626	METRICS: None
627	CONCLUSION: None
628	
629	================================================================================
630	EXP_ID: plan006-prolog-sta-s44
631	STATUS: RUNNING
632	HYPOTHESIS: Prolog exec+STA GRPO seed=44: 第三 seed。3-seed mean±std 用于论文 Claim 3 跨 logic type 统计支撑。
633	METRICS: None
634	CONCLUSION: None
635	
636	================================================================================
637	EXP_ID: plan009-sft-baseline-s42
638	STATUS: DONE
639	HYPOTHESIS: SFT baseline: supervised finetuning on FOLIO data (500 steps, Qwen3-4B) to establish whether hacking patterns are GRPO-specific or general finetuning artifacts. Same model as all GRPO experiments for fair comparison.
640	METRICS: None
641	CONCLUSION: killed
642	
643	================================================================================
644	EXP_ID: plan009-sft-baseline-s42-r2
645	STATUS: DONE
646	HYPOTHESIS: SFT baseline: supervised finetuning on FOLIO data (500 steps, Qwen3-4B, same model as all GRPO experiments) to establish whether hacking patterns are GRPO-specific or general finetuning artifacts. Compare eval PR/ISR/hacking taxonomy against GRPO exec-only and exec+ISR conditions.
647	METRICS: None
648	CONCLUSION: failed
649	
650	================================================================================
651	EXP_ID: plan009-sft-baseline-s42-r3
652	STATUS: DONE
653	HYPOTHESIS: SFT baseline: supervised finetuning on FOLIO data (500 steps, Qwen3-4B, same model as all GRPO experiments) to establish whether hacking patterns are GRPO-specific or general finetuning artifacts. Compare eval PR/ISR/hacking taxonomy against GRPO exec-only and exec+ISR conditions.
654	METRICS: None
655	CONCLUSION: failed
656	EXTRA: {
657	  "hook_events": [
658	    {
659	      "event": "on_failed",
660	      "action": "agent",
661	      "ts": "2026-05-14T11:39:39.416777+00:00"
662	    }
663	  ]
664	}
665	
666	================================================================================
667	EXP_ID: plan009-sft-baseline-s42-r4
668	STATUS: DONE
669	HYPOTHESIS: SFT baseline: supervised finetuning on FOLIO data (500 steps, Qwen3-4B, same model as all GRPO experiments) to establish whether hacking patterns are GRPO-specific or general finetuning artifacts. r4: fix CUDA_VISIBLE_DEVICES + --gpu + --no_wandb.
670	METRICS: {
671	  "eval_prove_rate": 0.14,
672	  "eval_mean_isr": 0.08,
673	  "eval_isr_std": 0.214,
674	  "eval_median_isr": 0,
675	  "eval_max_isr": 0.833,
676	  "eval_proved_only_isr": 0.571,
677	  "eval_n_proved": 14,
678	  "eval_n_problems": 100,
679	  "eval_method": "eval_sta.py full STA",
680	  "eval_data": "proofwriter_fol_100.jsonl",
681	  "train_final_loss": 0.0287,
682	  "train_token_accuracy": 0.9935,
683	  "train_epochs": 7.94,
684	  "train_runtime_sec": 789.6,
685	  "by_answer_type": {
686	    "true": {
687	      "count": 34,
688	      "proved": 13,
689	      "pr": 0.382,
690	      "isr": 0.226
691	    },
692	    "unknown": {
693	      "count": 41,
694	      "proved": 1,
695	      "pr": 0.024,
696	      "isr": 0.008
697	    },
698	    "false": {
699	      "count": 25,
700	      "proved": 0,
701	      "pr": 0,
702	      "isr": 0
703	    }
704	  },
705	  "h7_rate": 0,
706	  "h7_count": 0,
707	  "h1_rate": 0.071,
708	  "h1_count": 1,
709	  "genuine_rate": 0.929,
710	  "genuine_count": 13,
711	  "hacking_patterns": "near-zero (1/14 H1, 0 H7, 92.9% genuine)",
712	  "tautological_collapse": false
713	}
714	CONCLUSION: success
715	EXTRA: {
716	  "hook_events": [
717	    {
718	      "event": "on_complete",
719	      "action": "agent",
720	      "ts": "2026-05-14T12:18:57.313588+00:00"
721	    }
722	  ]
723	}
724	
725	================================================================================
726	EXP_ID: plan012-hacking-taxonomy
727	STATUS: DONE
728	HYPOTHESIS: ISR β=0.1 vs Random β=0.1 hacking taxonomy 对比：ISR reward 能否减少 hacking 模式比例、增加 genuine proof 比例？5 种 hacking 分类（conclusion embedding, repetition collapse, tautological collapse, complexity-without-utility, premise padding）。
729	METRICS: {
730	  "isr_b01_genuine_rate": 0.259,
731	  "random_b01_genuine_rate": 0.177,
732	  "genuine_rate_delta_pp": 8.2,
733	  "isr_b01_conclusion_embedding_rate": 0.728,
734	  "random_b01_conclusion_embedding_rate": 0.785,
735	  "isr_b01_genuine_mean_isr": 0.6723,
736	  "random_b01_genuine_mean_isr": 0.3427,
737	  "isr_b01_complexity_wo_utility_rate": 0,
738	  "random_b01_complexity_wo_utility_rate": 0.038,
739	  "isr_b01_hacking_rate": 0.741,
740	  "random_b01_hacking_rate": 0.823
741	}
742	CONCLUSION: success
743	
744	================================================================================
745	EXP_ID: plan013-random-reward-s42
746	STATUS: DONE
747	HYPOTHESIS: N/A
748	METRICS: None
749	CONCLUSION: failed
750	
751	================================================================================
752	EXP_ID: plan013-random-reward-s42-r2
753	STATUS: DONE
754	HYPOTHESIS: N/A
755	METRICS: None
756	CONCLUSION: failed
757	
758	================================================================================
759	EXP_ID: plan013-random-reward-s42-r3
760	STATUS: DONE
761	HYPOTHESIS: N/A
762	METRICS: None
763	CONCLUSION: failed
764	
765	================================================================================
766	EXP_ID: plan013-random-reward-s42-r4
767	STATUS: DONE
768	HYPOTHESIS: N/A
769	METRICS: {
770	  "eval_prove_rate": 1,
771	  "eval_mean_isr": 0.535,
772	  "eval_isr_std": 0.1282,
773	  "eval_proved_only_isr": 0.535,
774	  "eval_median_isr": 0.5,
775	  "eval_n_proved": 100,
776	  "eval_n_problems": 100,
777	  "eval_method": "eval_sta.py full STA",
778	  "eval_data": "proofwriter_fol_100.jsonl",
779	  "eval_note": "DEGENERATE: model generates trivial 2-component proofs (premise=conclusion, conclusion=conclusion), ISR=0.5 is artifact of trivial proof structure"
780	}
781	CONCLUSION: success
782	EXTRA: {
783	  "hook_events": [
784	    {
785	      "event": "on_complete",
786	      "action": "agent",
787	      "ts": "2026-05-14T02:19:58.514969+00:00"
788	    }
789	  ]
790	}
791	
792	================================================================================
793	EXP_ID: plan014-downstream-nli-s42
794	STATUS: DONE
795	HYPOTHESIS: Downstream NLI validation: 高ISR formalization 应在独立推理任务上表现更好(entailment accuracy)，Spearman ρ(ISR, accuracy) > 0.1 验证 ISR 作为 quality proxy 的实用价值。同时用 Z3 cross-solver agreement 验证 formalization 鲁棒性。
796	METRICS: {
797	  "overall_accuracy": 0.341,
798	  "proved_rate": 0.915,
799	  "proved_count": 732,
800	  "total_generations": 800,
801	  "parse_errors": 0,
802	  "accuracy_by_label": {
803	    "true": 0.912,
804	    "false": 0,
805	    "unknown": 0.076
806	  },
807	  "spearman_rho": -0.049,
808	  "spearman_p": 0.187,
809	  "mann_whitney_U": 17202,
810	  "mann_whitney_p": 0.288,
811	  "bon_isr_accuracy": 0.35,
812	  "bon_random_accuracy": 0.341,
813	  "bon_oracle_accuracy": 0.44,
814	  "bon_prove_first_accuracy": 0.35,
815	  "isr_bucket_high_acc": 0.75,
816	  "isr_bucket_mid_acc": 0.377,
817	  "isr_bucket_low_acc": 0.327,
818	  "runtime_inference_s": 408.8,
819	  "runtime_eval_s": 13.6
820	}
821	CONCLUSION: negative
822	EXTRA: {
823	  "hook_events": [
824	    {
825	      "event": "on_failed",
826	      "action": "agent",
827	      "ts": "2026-05-14T03:51:19.514390+00:00"
828	    },
829	    {
830	      "event": "on_complete",
831	      "action": "agent",
832	      "ts": "2026-05-14T04:26:06.788787+00:00"
833	    }
834	  ],
835	  "previous_failure": {
836	    "conclusion": "failed",
837	    "notes": "r1 失败: checkpoint_path 多了 /checkpoint-500。save_total_limit=1 导致模型直接保存在 plan001_exec_only_s42/ 根目录。修正路径为 /root/autodl-tmp/outputs/plan001_exec_only_s42 即可。等 s43 re-eval 完成后重跑。"
838	  }
839	}
840	
841	================================================================================
842	EXP_ID: plan016-extended-1000-s42
843	STATUS: DONE
844	HYPOTHESIS: Extended training 1000 steps exec-only: plan001-s42 500步 PR=93% 是真收敛还是 lucky early convergence? 1000步观察 PR 和 ISR 在更长 horizon 的行为。s43(14%)/s44(98% tautological) 在 500 步均失败，延长训练是否能改善？
845	METRICS: {
846	  "train": {
847	    "total_steps": 1000,
848	    "duration_min": 146,
849	    "final_prove_rate": 0.8396,
850	    "final_mean_isr": 0.0503,
851	    "train_loss": 0.0125,
852	    "epoch": 4,
853	    "windowed": {
854	      "steps_001_100": {
855	        "pr": 0.19,
856	        "isr": 0.0859
857	      },
858	      "steps_101_200": {
859	        "pr": 0.66,
860	        "isr": 0.1115
861	      },
862	      "steps_201_300": {
863	        "pr": 0.838,
864	        "isr": 0.0985
865	      },
866	      "steps_301_400": {
867	        "pr": 0.907,
868	        "isr": 0.054
869	      },
870	      "steps_401_500": {
871	        "pr": 0.927,
872	        "isr": 0.0433
873	      },
874	      "steps_501_600": {
875	        "pr": 0.963,
876	        "isr": 0.0408
877	      },
878	      "steps_601_700": {
879	        "pr": 0.965,
880	        "isr": 0.02
881	      },
882	      "steps_701_800": {
883	        "pr": 0.988,
884	        "isr": 0.0178
885	      },
886	      "steps_801_900": {
887	        "pr": 0.978,
888	        "isr": 0.017
889	      },
890	      "steps_901_1000": {
891	        "pr": 0.981,
892	        "isr": 0.0144
893	      }
894	    }
895	  },
896	  "eval": {
897	    "prove_rate": 0.96,
898	    "n_proved": 96,
899	    "n_problems": 100,
900	    "mean_isr": 0.0027,
901	    "isr_std": 0.0118,
902	    "median_isr": 0,
903	    "proved_only_mean_isr": 0.0028,
904	    "min_isr": 0,
905	    "max_isr": 0.0588,
906	    "isr_0_ratio": 0.9479,
907	    "isr_1_ratio": 0,
908	    "component_count_mean": 18.55,
909	    "component_count_2_ratio": 0,
910	    "mean_n_necessary": 0.052,
911	    "n_necessary_0_ratio": 0.9479,
912	    "tautological_collapse": false,
913	    "by_answer_type": {
914	      "false": {
915	        "count": 29,
916	        "proved": 26,
917	        "prove_rate": 0.8966,
918	        "mean_isr": 0
919	      },
920	      "unknown": {
921	        "count": 31,
922	        "proved": 30,
923	        "prove_rate": 0.9677,
924	        "mean_isr": 0.0053
925	      },
926	      "true": {
927	        "count": 40,
928	        "proved": 40,
929	        "prove_rate": 1,
930	        "mean_isr": 0.0026
931	      }
932	    },
933	    "eval_time_seconds": 396.3
934	  }
935	}
936	CONCLUSION: success
937	EXTRA: {
938	  "hook_events": [
939	    {
940	      "event": "on_complete",
941	      "action": "agent",
942	      "ts": "2026-05-14T08:02:33.434519+00:00"
943	    }
944	  ]
945	}
946	
947	================================================================================
948	EXP_ID: plan017-additive-random-s42
949	STATUS: DONE
950	HYPOTHESIS: Additive random control: r = r_exec·(1+0.3·random). 隔离 ISR structural signal vs variance regularization. 若 ISR > random > exec-only → signal+regularization 均贡献; 若 ISR > random ≈ exec-only → ISR signal 是关键; 若 ISR ≈ random → ISR 无结构价值。
951	METRICS: {
952	  "eval_prove_rate": 0.48,
953	  "eval_mean_isr": 0.0453,
954	  "eval_isr_std": 0.0759,
955	  "eval_median_isr": 0,
956	  "eval_max_isr": 0.2857,
957	  "eval_proved_only_isr": 0.0943,
958	  "eval_n_proved": 48,
959	  "eval_n_problems": 100,
960	  "eval_method": "eval_sta.py full STA",
961	  "eval_data": "proofwriter_fol_100.jsonl",
962	  "eval_component_count_mean": 9.6,
963	  "eval_component_count_2_ratio": 0,
964	  "eval_isr_pr_ratio": 0.0943,
965	  "eval_elapsed_s": 542.3,
966	  "eval_by_type_false_pr": 0.32,
967	  "eval_by_type_false_isr": 0.0254,
968	  "eval_by_type_unknown_pr": 0.51,
969	  "eval_by_type_unknown_isr": 0.0518,
970	  "eval_by_type_true_pr": 0.56,
971	  "eval_by_type_true_isr": 0.052,
972	  "tautological_collapse": false
973	}
974	CONCLUSION: negative
975	EXTRA: {
976	  "hook_events": [
977	    {
978	      "event": "on_complete",
979	      "action": "agent",
980	      "ts": "2026-05-14T05:17:18.376399+00:00"
981	    }
982	  ]
983	}
984	
985	================================================================================
986	EXP_ID: plan018-additive-random-b01-s42
987	STATUS: DONE
988	HYPOTHESIS: β=0.1 random control: r = r_exec·(1+0.1·random[0,1]). 与 plan002-b01 (additive ISR β=0.1, PR=0.81, ISR=0.337) 同 β 对照。如果 ISR β=0.1 >> random β=0.1 → ISR 信号在低剂量下有结构价值; 如果 ISR ≈ random → ISR 信号在低剂量下也仅是 variance regularization。D031 紧急实验。
989	METRICS: {
990	  "eval_prove_rate": 0.79,
991	  "eval_mean_isr": 0.1038,
992	  "eval_isr_std": 0.1369,
993	  "eval_median_isr": 0.0357,
994	  "eval_proved_only_isr": 0.1314,
995	  "eval_n_proved": 79,
996	  "eval_n_problems": 100,
997	  "eval_component_count_mean": 8.46,
998	  "eval_component_count_median": 8,
999	  "eval_component_count_2_ratio": 0,
1000	  "eval_isr_1_ratio": 0,
1001	  "eval_isr_0_ratio": 0.367,
1002	  "eval_isr_gt0_ratio": 0.633,
1003	  "eval_by_type_false_pr": 0.8,
1004	  "eval_by_type_false_isr": 0.1318,
1005	  "eval_by_type_unknown_pr": 0.7317,
1006	  "eval_by_type_unknown_isr": 0.0944,
1007	  "eval_by_type_true_pr": 0.8529,
1008	  "eval_by_type_true_isr": 0.0945,
1009	  "tautological_collapse": false,
1010	  "train_total_steps": 500,
1011	  "train_duration_min": 70.5,
1012	  "train_last100_pr": 0.805,
1013	  "train_last100_isr": 0.1432,
1014	  "train_loss": 0.005
1015	}
1016	CONCLUSION: negative
1017	EXTRA: {
1018	  "hook_events": [
1019	    {
1020	      "event": "on_complete",
1021	      "action": "agent",
1022	      "ts": "2026-05-14T08:09:09.188407+00:00"
1023	    }
1024	  ]
1025	}
1026	
1027	================================================================================
1028	EXP_ID: plan018-additive-random-b01-s43
1029	STATUS: DONE
1030	HYPOTHESIS: Random β=0.1 seed=43 控制组：与 plan002-b01-s43 (ISR β=0.1) 同 seed 对照。验证 ISR 3.2x > random 的结论在 s43 下是否成立。
1031	METRICS: None
1032	CONCLUSION: failed
1033	EXTRA: {
1034	  "hook_events": [
1035	    {
1036	      "event": "on_failed",
1037	      "action": "agent",
1038	      "ts": "2026-05-14T11:30:40.886615+00:00"
1039	    }
1040	  ]
1041	}
1042	
1043	================================================================================
1044	EXP_ID: plan018-additive-random-b01-s43-r2
1045	STATUS: DONE
1046	HYPOTHESIS: Random β=0.1 seed=43 控制组 r2: 重试 (原 s43 step 200 磁盘满崩溃)。与 plan002-b01-s43 (ISR β=0.1) 同 seed 对照。3-seed mean±std 审稿硬性要求。
1047	METRICS: {
1048	  "h7_rate": 0,
1049	  "h7_count": 0,
1050	  "h1_rate": 93.2,
1051	  "h1_count": 82,
1052	  "genuine_rate": 6.8,
1053	  "genuine_count": 6
1054	}
1055	CONCLUSION: negative
1056	EXTRA: {
1057	  "hook_events": [
1058	    {
1059	      "event": "on_complete",
1060	      "action": "agent",
1061	      "ts": "2026-05-14T16:43:54.952857+00:00"
1062	    }
1063	  ]
1064	}
1065	
1066	================================================================================
1067	EXP_ID: plan018-additive-random-b01-s44
1068	STATUS: DONE
1069	HYPOTHESIS: Random β=0.1 seed=44 控制组：与 plan002-b01-s44 (ISR β=0.1) 同 seed 对照。验证 ISR 3.2x > random 的结论在 s44 下是否成立。
1070	METRICS: {
1071	  "prove_rate": 0.89,
1072	  "mean_isr": 0.0619,
1073	  "isr_std": 0.1756,
1074	  "median_isr": 0,
1075	  "proved_only_mean_isr": 0.0695,
1076	  "n_proved": 89,
1077	  "n_problems": 100,
1078	  "max_isr": 1,
1079	  "min_isr": 0,
1080	  "isr_pr_ratio": 0.0695,
1081	  "isr_zero_count": 72,
1082	  "isr_one_count": 2,
1083	  "by_answer_type": {
1084	    "false": {
1085	      "count": 25,
1086	      "proved": 21,
1087	      "prove_rate": 0.84,
1088	      "mean_isr": 0.0533
1089	    },
1090	    "unknown": {
1091	      "count": 41,
1092	      "proved": 40,
1093	      "prove_rate": 0.976,
1094	      "mean_isr": 0.0892
1095	    },
1096	    "true": {
1097	      "count": 34,
1098	      "proved": 28,
1099	      "prove_rate": 0.824,
1100	      "mean_isr": 0.0353
1101	    }
1102	  },
1103	  "elapsed_seconds": 1012.7,
1104	  "eval_method": "eval_sta.py with Prover9Solver, FOL"
1105	}
1106	CONCLUSION: success
1107	EXTRA: {
1108	  "hook_events": [
1109	    {
1110	      "event": "on_complete",
1111	      "action": "agent",
1112	      "ts": "2026-05-14T13:37:43.236026+00:00"
1113	    }
1114	  ]
1115	}
1116	
1117	================================================================================
1118	EXP_ID: sta-gt-isr-baseline
1119	STATUS: DONE
1120	HYPOTHESIS: N/A
1121	METRICS: {
1122	  "gt_prove_rate": 0.18,
1123	  "gt_mean_isr": 0.5588,
1124	  "gt_isr_std": 0.2582,
1125	  "gt_isr_median": 0.6125,
1126	  "solver_execution_rate": 1,
1127	  "true_prove_rate": 0.5,
1128	  "true_mean_isr": 0.5833
1129	}
1130	CONCLUSION: success
1131	
1132	================================================================================
1133	EXP_ID: sta-phase0-baseline
1134	STATUS: DONE
1135	HYPOTHESIS: N/A
1136	METRICS: {
1137	  "mean_isr": 0.0641,
1138	  "isr_std": 0.1983,
1139	  "median_isr": 0,
1140	  "isr_range": [
1141	    0,
1142	    0.889
1143	  ],
1144	  "prove_rate": 0.12,
1145	  "proved_count": 12,
1146	  "total_samples": 100,
1147	  "xor_affected_samples": 34,
1148	  "effective_prove_rate_no_xor": 0.182,
1149	  "avg_time_per_sample_s": 3.4,
1150	  "total_runtime_s": 336,
1151	  "isr_by_answer": {
1152	    "true": {
1153	      "n": 34,
1154	      "proved": 9,
1155	      "prove_rate": 0.265,
1156	      "mean_isr": 0.1345
1157	    },
1158	    "false": {
1159	      "n": 25,
1160	      "proved": 1,
1161	      "prove_rate": 0.04,
1162	      "mean_isr": 0.024
1163	    },
1164	    "unknown": {
1165	      "n": 41,
1166	      "proved": 2,
1167	      "prove_rate": 0.049,
1168	      "mean_isr": 0.0302
1169	    }
1170	  }
1171	}
1172	CONCLUSION: success
1173	
1174	================================================================================
1175	EXP_ID: sta-phase1-exec-only
1176	STATUS: DONE
1177	HYPOTHESIS: N/A
1178	METRICS: None
1179	CONCLUSION: failed
1180	EXTRA: {
1181	  "hook_events": [
1182	    {
1183	      "event": "on_failed",
1184	      "action": "agent",
1185	      "ts": "2026-05-13T19:33:01.864437+00:00"
1186	    }
1187	  ]
1188	}
1189	
1190	================================================================================
1191	EXP_ID: sta-phase1-exec-only-r2
1192	STATUS: DONE
1193	HYPOTHESIS: N/A
1194	METRICS: None
1195	CONCLUSION: failed
1196	EXTRA: {
1197	  "hook_events": [
1198	    {
1199	      "event": "on_failed",
1200	      "action": "agent",
1201	      "ts": "2026-05-13T19:55:38.155358+00:00"
1202	    }
1203	  ]
1204	}
1205	
1206	================================================================================
1207	EXP_ID: sta-phase1-exec-only-r3
1208	STATUS: DONE
1209	HYPOTHESIS: N/A
1210	METRICS: None
1211	CONCLUSION: failed
1212	EXTRA: {
1213	  "hook_events": [
1214	    {
1215	      "event": "on_failed",
1216	      "action": "agent",
1217	      "ts": "2026-05-13T20:19:52.981720+00:00"
1218	    }
1219	  ]
1220	}
1221	
1222	================================================================================
1223	EXP_ID: sta-phase1-exec-only-r4
1224	STATUS: DONE
1225	HYPOTHESIS: N/A
1226	METRICS: {
1227	  "parse_rate": 1,
1228	  "prove_rate": 0.15125,
1229	  "mean_isr": 0.1475,
1230	  "last20_prove_rate": 0.2,
1231	  "last20_isr_mean": 0.2,
1232	  "first20_reward_mean": 0.119,
1233	  "training_steps": 100,
1234	  "training_minutes": 15
1235	}
1236	CONCLUSION: negative
1237	EXTRA: {
1238	  "hook_events": [
1239	    {
1240	      "event": "on_complete",
1241	      "action": "agent",
1242	      "ts": "2026-05-13T20:45:54.294365+00:00"
1243	    }
1244	  ]
1245	}
1246	
1247	================================================================================
1248	EXP_ID: sta-phase1-exec-only-r5
1249	STATUS: DONE
1250	HYPOTHESIS: N/A
1251	METRICS: {
1252	  "parse_rate": 1,
1253	  "prove_rate": 0.15125,
1254	  "mean_isr": 0.1475,
1255	  "last20_prove_rate": 0.2,
1256	  "last20_isr_mean": 0.2,
1257	  "first20_prove_rate": 0.11875,
1258	  "first20_isr_mean": 0.11875,
1259	  "overall_reward_mean": 0.15125,
1260	  "last20_reward_mean": 0.2,
1261	  "training_steps": 100,
1262	  "training_minutes": 15.7,
1263	  "step_time_s": 9.44,
1264	  "isr_pr_ratio_last20": 1,
1265	  "K": 8
1266	}
1267	CONCLUSION: success
1268	
1269	================================================================================
1270	EXP_ID: sta-phase1-exec-sta
1271	STATUS: DONE
1272	HYPOTHESIS: N/A
1273	METRICS: None
1274	CONCLUSION: failed
1275	EXTRA: {
1276	  "hook_events": [
1277	    {
1278	      "event": "on_failed",
1279	      "action": "agent",
1280	      "ts": "2026-05-13T19:33:05.009356+00:00"
1281	    }
1282	  ]
1283	}
1284	
1285	================================================================================
1286	EXP_ID: sta-phase1-exec-sta-r2
1287	STATUS: DONE
1288	HYPOTHESIS: N/A
1289	METRICS: None
1290	CONCLUSION: failed
1291	EXTRA: {
1292	  "hook_events": [
1293	    {
1294	      "event": "on_failed",
1295	      "action": "agent",
1296	      "ts": "2026-05-13T19:55:42.974865+00:00"
1297	    }
1298	  ]
1299	}
1300	
1301	================================================================================
1302	EXP_ID: sta-phase1-exec-sta-r3
1303	STATUS: DONE
1304	HYPOTHESIS: N/A
1305	METRICS: None
1306	CONCLUSION: failed
1307	EXTRA: {
1308	  "hook_events": [
1309	    {
1310	      "event": "on_failed",
1311	      "action": "agent",
1312	      "ts": "2026-05-13T20:19:56.549926+00:00"
1313	    }
1314	  ]
1315	}
1316	
1317	================================================================================
1318	EXP_ID: sta-phase1-exec-sta-r4
1319	STATUS: DONE
1320	HYPOTHESIS: N/A
1321	METRICS: {
1322	  "parse_rate": 1,
1323	  "prove_rate": 0.1575,
1324	  "mean_isr": 0.1525,
1325	  "last20_prove_rate": 0.2125,
1326	  "last20_isr_mean": 0.2125,
1327	  "first20_reward_mean": 0.119,
1328	  "training_steps": 100,
1329	  "training_minutes": 15
1330	}
1331	CONCLUSION: negative
1332	EXTRA: {
1333	  "hook_events": [
1334	    {
1335	      "event": "on_complete",
1336	      "action": "agent",
1337	      "ts": "2026-05-13T20:45:56.962544+00:00"
1338	    }
1339	  ]
1340	}
1341	
1342	================================================================================
1343	EXP_ID: sta-phase1-exec-sta-r5
1344	STATUS: DONE
1345	HYPOTHESIS: N/A
1346	METRICS: {
1347	  "parse_rate": 1,
1348	  "prove_rate": 0.1,
1349	  "mean_isr": 0.04347,
1350	  "last20_prove_rate": 0.15,
1351	  "last20_isr_mean": 0.04956,
1352	  "first20_prove_rate": 0.08125,
1353	  "first20_isr_mean": 0.05182,
1354	  "overall_reward_mean": 0.07174,
1355	  "last20_reward_mean": 0.09978,
1356	  "training_steps": 100,
1357	  "training_minutes": 16.9,
1358	  "step_time_s": 10.13,
1359	  "isr_pr_ratio_overall": 0.43,
1360	  "isr_pr_ratio_last20": 0.33,
1361	  "K": 8
1362	}
1363	CONCLUSION: negative
1364	
1365	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01TzDAwzFMhAJ7FWb5HqudYS",
  "session_id": "eb5b7954-c1fd-473d-8da7-d1389c3f22e7",
  "uuid": "a874624f-1495-41ca-8a9a-f5ae6a0e1bc5"
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
  "task_id": "afbb79756989adaac",
  "tool_use_id": "toolu_01TzDAwzFMhAJ7FWb5HqudYS",
  "description": "Running Search for premise_count_matched and any missed experiments",
  "usage": {
    "total_tokens": 38965,
    "tool_uses": 7,
    "duration_ms": 51654
  },
  "last_tool_name": "Bash",
  "uuid": "68d7210f-42c1-49b0-98b1-e24d8fa153be",
  "session_id": "eb5b7954-c1fd-473d-8da7-d1389c3f22e7"
}
```

---

### Tool call

_source line 36_

<details open><summary>🔧 Tool call — Bash · `toolu_01G6i39F697Yc2677ryr14UR`</summary>

```json
{
  "command": "file=\"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/eb5b7954-c1fd-473d-8da7-d1389c3f22e7/tool-results/mcp-agent-ml-research-read_registry-1778779433924.txt\"\npython3 << 'PYEOF'\nimport json\n\nwith open(r'/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/eb5b7954-c1fd-473d-8da7-d1389c3f22e7/tool-results/mcp-agent-ml-research-read_registry-1778779433924.txt') as f:\n    raw = json.load(f)\ninner = json.loads(raw['result'])\nexps = inner['data']['experiments']\n\n# Search for premise_count_matched in any field\nfor exp_id, exp in exps.items():\n    s = json.dumps(exp)\n    if 'premise_count' in s.lower() or 'claim2' in s.lower() or 'claim_2' in s.lower():\n        print(f\"FOUND premise_count reference in: {exp_id}\")\n        print(f\"  status: {exp.get('status')}\")\n        print(f\"  metrics: {json.dumps(exp.get('metrics'), indent=2, ensure_ascii=False) if exp.get('metrics') else 'None'}\")\n        print(f\"  conclusion: {exp.get('conclusion')}\")\n        print(f\"  hypothesis: {exp.get('hypothesis', 'N/A')[:200]}\")\n        print()\n\n# Also check for any exp_ids I might have missed\nprint(\"\\n=== ALL EXP_IDS NOT YET REPORTED ===\")\nreported = set()\nfor exp_id in exps:\n    for prefix in ['sta-phase0', 'sta-phase1', 'sta-gt', 'plan001', 'plan002', 'plan003', 'plan005', 'plan006', 'plan009', 'plan012', 'plan013', 'plan014', 'plan016', 'plan017', 'plan018']:\n        if exp_id.startswith(prefix):\n            reported.add(exp_id)\n            break\nfor exp_id in sorted(exps.keys()):\n    if exp_id not in reported:\n        print(f\"  {exp_id} (status={exps[exp_id].get('status')})\")\n\nPYEOF\n",
  "description": "Search for premise_count_matched and any missed experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01TzDAwzFMhAJ7FWb5HqudYS",
  "session_id": "eb5b7954-c1fd-473d-8da7-d1389c3f22e7",
  "uuid": "9b3dc82a-4bf7-4039-aa86-d3e5c485b2d6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WuBigfM46CybppUnXqACFU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 18133,
      "cache_read_input_tokens": 20729,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18133,
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

_source line 37 · 2026-05-14T17:25:01.092Z_

<details><summary>↩ Tool result · `toolu_01G6i39F697Yc2677ryr14UR`</summary>

```text
=== ALL EXP_IDS NOT YET REPORTED ===
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01TzDAwzFMhAJ7FWb5HqudYS",
  "session_id": "eb5b7954-c1fd-473d-8da7-d1389c3f22e7",
  "uuid": "094551cd-9a3f-46b8-9d92-480a15b69d49"
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
  "task_id": "afbb79756989adaac",
  "tool_use_id": "toolu_01TzDAwzFMhAJ7FWb5HqudYS",
  "description": "Running Search for premise_count_matched data",
  "usage": {
    "total_tokens": 39747,
    "tool_uses": 8,
    "duration_ms": 60498
  },
  "last_tool_name": "Bash",
  "uuid": "cb90c8eb-ba7f-4cdd-880f-8cb94ba3bc7e",
  "session_id": "eb5b7954-c1fd-473d-8da7-d1389c3f22e7"
}
```

---

### Tool call

_source line 39_

<details open><summary>🔧 Tool call — Bash · `toolu_01TDVMfdgcTzE6ofBJyJi3mv`</summary>

```json
{
  "command": "file=\"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/eb5b7954-c1fd-473d-8da7-d1389c3f22e7/tool-results/mcp-agent-ml-research-read_registry-1778779433924.txt\"\npython3 << 'PYEOF'\nimport json\n\nwith open(r'/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/eb5b7954-c1fd-473d-8da7-d1389c3f22e7/tool-results/mcp-agent-ml-research-read_registry-1778779433924.txt') as f:\n    raw = json.load(f)\ninner = json.loads(raw['result'])\nexps = inner['data']['experiments']\n\n# Search for anything related to \"matched\", \"Claim 2\", \"premise count\" in full JSON\nfor exp_id, exp in exps.items():\n    s = json.dumps(exp).lower()\n    for kw in ['matched', 'premise_count_match']:\n        if kw in s:\n            print(f\"FOUND '{kw}' in {exp_id}\")\n            \n# Also check plan002-b01-s43 and s44 hypothesis for Claim 2 references\nfor exp_id in ['plan002-additive-b01-s43', 'plan002-additive-b01-s44']:\n    print(f\"\\n{exp_id} hypothesis: {exps[exp_id].get('hypothesis', 'N/A')}\")\nPYEOF\n",
  "description": "Search for premise_count_matched data"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01TzDAwzFMhAJ7FWb5HqudYS",
  "session_id": "eb5b7954-c1fd-473d-8da7-d1389c3f22e7",
  "uuid": "c1adfb20-f12a-4078-a14d-2d43981d7ce9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hgq5d1pkotuF73TdYgsBgS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 780,
      "cache_read_input_tokens": 38862,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 780,
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

_source line 40 · 2026-05-14T17:25:09.896Z_

<details><summary>↩ Tool result · `toolu_01TDVMfdgcTzE6ofBJyJi3mv`</summary>

```text
plan002-additive-b01-s43 hypothesis: ISR β=0.1 seed=43 多 seed 验证：plan002-b01-s42 (PR=0.81, ISR=0.337) 在 s43 下是否可复现？exec-only s43 是 degraded seed (PR=14%)，ISR β=0.1 能否拯救 bad seed？3-seed mean±std 用于论文 Claim 2 统计支撑。

plan002-additive-b01-s44 hypothesis: ISR β=0.1 seed=44 多 seed 验证：exec-only s44 是 tautological collapse (PR=98%, ISR=0.57 fake)，ISR β=0.1 能否防止 tautological collapse？3-seed mean±std 用于论文 Claim 2。
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01TzDAwzFMhAJ7FWb5HqudYS",
  "session_id": "eb5b7954-c1fd-473d-8da7-d1389c3f22e7",
  "uuid": "3aa4d8c0-ed6e-439c-b206-78bad876552b"
}
```

</details>

---

### System

_source line 41_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "afbb79756989adaac",
  "tool_use_id": "toolu_01TzDAwzFMhAJ7FWb5HqudYS",
  "status": "completed",
  "output_file": "",
  "summary": "Extract registry metrics for table_data.json",
  "usage": {
    "total_tokens": 40528,
    "tool_uses": 8,
    "duration_ms": 158759
  },
  "uuid": "f8816228-b17a-4698-bb57-ecc1280da57c",
  "session_id": "eb5b7954-c1fd-473d-8da7-d1389c3f22e7"
}
```

---

### Tool result

_source line 42 · 2026-05-14T17:26:48.041Z_

<details><summary>↩ Tool result · `toolu_01TzDAwzFMhAJ7FWb5HqudYS`</summary>

```text
No "premise_count_matched" data exists in this registry. Here is the complete extracted data:

---

## 1. Base model / phase0 baseline

**exp_id:** `sta-phase0-baseline` | **status:** DONE | **conclusion:** success

| Metric | Value |
|--------|-------|
| prove_rate | 0.12 |
| mean_isr | 0.0641 |
| isr_std | 0.1983 |
| median_isr | 0 |
| isr_range | [0, 0.889] |
| proved_count | 12 |
| total_samples | 100 |
| xor_affected_samples | 34 |
| effective_prove_rate_no_xor | 0.182 |
| avg_time_per_sample_s | 3.4 |
| total_runtime_s | 336 |
| isr_by_answer: true | n=34, proved=9, pr=0.265, mean_isr=0.1345 |
| isr_by_answer: false | n=25, proved=1, pr=0.04, mean_isr=0.024 |
| isr_by_answer: unknown | n=41, proved=2, pr=0.049, mean_isr=0.0302 |

Also related: **`sta-gt-isr-baseline`** | status: DONE | conclusion: success
- gt_prove_rate: 0.18, gt_mean_isr: 0.5588, gt_isr_std: 0.2582, gt_isr_median: 0.6125, solver_execution_rate: 1, true_prove_rate: 0.5, true_mean_isr: 0.5833

---

## 2. SFT baseline (plan009)

Only `plan009-sft-baseline-s42-r4` has metrics. Prior attempts (r1=killed, r2=failed, r3=failed).

**exp_id:** `plan009-sft-baseline-s42-r4` | **status:** DONE | **conclusion:** success

| Metric | Value |
|--------|-------|
| eval_prove_rate | 0.14 |
| eval_mean_isr | 0.08 |
| eval_isr_std | 0.214 |
| eval_median_isr | 0 |
| eval_max_isr | 0.833 |
| eval_proved_only_isr | 0.571 |
| eval_n_proved | 14 |
| eval_n_problems | 100 |
| train_final_loss | 0.0287 |
| train_token_accuracy | 0.9935 |
| train_epochs | 7.94 |
| train_runtime_sec | 789.6 |
| h7_rate | 0 |
| h7_count | 0 |
| h1_rate | 0.071 |
| h1_count | 1 |
| genuine_rate | 0.929 |
| genuine_count | 13 |
| tautological_collapse | false |
| by_answer: true | count=34, proved=13, pr=0.382, isr=0.226 |
| by_answer: unknown | count=41, proved=1, pr=0.024, isr=0.008 |
| by_answer: false | count=25, proved=0, pr=0, isr=0 |

---

## 3. Exec-only 500 steps (plan001)

### s42: `plan001-exec-only-s42` = failed, no metrics. Successful retry is `plan001-exec-only-s42-r2`:

**exp_id:** `plan001-exec-only-s42-r2` | **status:** DONE | **conclusion:** success

| Metric | Value |
|--------|-------|
| eval_prove_rate | 0.93 |
| eval_mean_isr | 0.1232 |
| eval_isr_std | 0.1887 |
| eval_proved_only_isr | 0.1324 |
| eval_median_isr | 0 |
| eval_n_proved | 93 |
| eval_n_problems | 100 |
| h7_rate | 0 |
| h7_count | 0 |
| h1_rate | 0.871 |
| h1_count | 81 |
| genuine_rate | 0.129 |
| genuine_count | 12 |
| genuine_mean_isr | 0.3141 |
| h1_mean_isr | 0.1055 |
| conclusion_embedding_total | 0.871 |

### s43: `plan001-exec-only-s43` through `s43-r3` all failed. Successful run is `plan001-exec-only-s43-r4`:

**exp_id:** `plan001-exec-only-s43-r4` | **status:** DONE | **conclusion:** negative

| Metric | Value |
|--------|-------|
| eval_sampling_prove_rate | 0.14 |
| eval_sampling_mean_isr | 0 |
| eval_sampling_n_proved | 14 |
| eval_sampling_temperature | 0.7 |
| by_answer: true | count=34, proved=6, pr=0.176 |
| by_answer: false | count=25, proved=2, pr=0.08 |
| by_answer: unknown | count=41, proved=6, pr=0.146 |

**Note:** This is sampling-based eval (temperature=0.7), not greedy. ISR=0 across the board.

### s44: `plan001-exec-only-s44`

**exp_id:** `plan001-exec-only-s44` | **status:** DONE | **conclusion:** negative

| Metric | Value |
|--------|-------|
| eval_prove_rate | 0.98 |
| eval_mean_isr | 0.57 |
| eval_isr_std | 0.2013 |
| eval_median_isr | 0.5 |
| eval_proved_only_isr | 0.5816 |
| eval_n_proved | 98 |
| eval_n_problems | 100 |
| eval_component_count_mean | 2.04 |
| eval_component_count_2 | 94 |
| eval_component_count_3 | 4 |
| tautological_collapse | **true** |
| h7_rate | **1.0** |
| h7_count | 97 |
| h1_rate | 0 |
| h1_count | 0 |
| genuine_rate | 0 |
| genuine_count | 0 |
| conclusion_embedding_total | 1 |

---

## 4. Exec-only 1000 steps (plan016)

**exp_id:** `plan016-extended-1000-s42` | **status:** DONE | **conclusion:** success

**Train metrics:**
| Metric | Value |
|--------|-------|
| total_steps | 1000 |
| duration_min | 146 |
| final_prove_rate | 0.8396 |
| final_mean_isr | 0.0503 |
| train_loss | 0.0125 |
| epoch | 4 |
| steps 001-100: pr/isr | 0.19 / 0.0859 |
| steps 101-200: pr/isr | 0.66 / 0.1115 |
| steps 201-300: pr/isr | 0.838 / 0.0985 |
| steps 301-400: pr/isr | 0.907 / 0.054 |
| steps 401-500: pr/isr | 0.927 / 0.0433 |
| steps 501-600: pr/isr | 0.963 / 0.0408 |
| steps 601-700: pr/isr | 0.965 / 0.02 |
| steps 701-800: pr/isr | 0.988 / 0.0178 |
| steps 801-900: pr/isr | 0.978 / 0.017 |
| steps 901-1000: pr/isr | 0.981 / 0.0144 |

**Eval metrics:**
| Metric | Value |
|--------|-------|
| prove_rate | 0.96 |
| n_proved | 96 |
| mean_isr | 0.0027 |
| isr_std | 0.0118 |
| median_isr | 0 |
| proved_only_mean_isr | 0.0028 |
| max_isr | 0.0588 |
| isr_0_ratio | 0.9479 |
| isr_1_ratio | 0 |
| component_count_mean | 18.55 |
| component_count_2_ratio | 0 |
| mean_n_necessary | 0.052 |
| n_necessary_0_ratio | 0.9479 |
| tautological_collapse | false |
| by_answer false: pr/isr | 0.8966 / 0 |
| by_answer unknown: pr/isr | 0.9677 / 0.0053 |
| by_answer true: pr/isr | 1.0 / 0.0026 |
| eval_time_seconds | 396.3 |

---

## 5. ISR beta=0.1 (plan002-b01)

### s42: `plan002-additive-b01-s42` | **status:** DONE | **conclusion:** success

| Metric | Value |
|--------|-------|
| eval_prove_rate | 0.81 |
| eval_mean_isr | 0.3365 |
| eval_isr_std | 0.3227 |
| eval_proved_only_isr | 0.4154 |
| eval_median_isr | 0.2 |
| eval_n_proved | 81 |
| eval_n_problems | 100 |
| eval_component_count_mean | 5.58 |
| eval_component_count_2_ratio | 0.037 |
| eval_isr_1_ratio | 0.124 |
| eval_isr_0_ratio | 0.037 |
| tautological_collapse | false |
| train_total_steps | 500 |
| train_duration_min | 63 |
| train_last100_pr | 0.6875 |
| train_last100_isr | 0.1954 |
| train_last100_loss | 0.015 |
| by_type false: pr/isr | 0.88 / 0.3515 |
| by_type unknown: pr/isr | 0.83 / 0.3684 |
| by_type true: pr/isr | 0.74 / 0.2869 |

### s43: `plan002-additive-b01-s43` | **status:** DONE | **conclusion:** negative

| Metric | Value |
|--------|-------|
| eval_prove_rate | 0.61 |
| eval_mean_isr | 0.5063 |
| eval_isr_std | 0.4518 |
| eval_median_isr | 0.5 |
| eval_proved_only_isr | 0.8301 |
| component_count_mean | 4.03 |
| component_count_2_ratio | 0 |
| tautological_collapse | false |
| isr_0_ratio | 0.39 |
| isr_1_ratio | 0.656 |
| proved_single_premise_ratio | 1 |
| h7_rate_calibrated | 0.967 |
| **hacking_mode** | **conclusion_duplication_isr_inflation** |
| conclusion_embedding | true |
| train_total_steps | 500 |
| train_duration_min | 53 |
| train_loss | 0.012 |
| by_answer false: PR/ISR | 0.72 / 0.6 |
| by_answer unknown: PR/ISR | 0.537 / 0.442 |
| by_answer true: PR/ISR | 0.618 / 0.515 |

### s44: `plan002-additive-b01-s44` | **status:** DONE | **conclusion:** negative

| Metric | Value |
|--------|-------|
| eval_prove_rate | 0.89 |
| eval_mean_isr | 0.803 |
| eval_isr_std | 0.3418 |
| eval_median_isr | 1 |
| component_count_mean | 4.33 |
| component_count_2_ratio | 0.022 |
| tautological_collapse | false |
| isr_0_ratio | 0.12 |
| isr_1_ratio | 0.73 |
| proved_single_premise_ratio | 1 |
| h7_rate_calibrated | 0.865 |
| **hacking_mode** | **conclusion_duplication_isr_inflation** |
| conclusion_embedding | true |
| component_dist | {2: 2, 4: 54, 5: 33} |
| by_answer false: PR/ISR | 0.88 / 0.824 |
| by_answer unknown: PR/ISR | 0.927 / 0.837 |
| by_answer true: PR/ISR | 0.853 / 0.747 |

---

## 6. Random beta=0.1 (plan018)

### s42: `plan018-additive-random-b01-s42` | **status:** DONE | **conclusion:** negative

| Metric | Value |
|--------|-------|
| eval_prove_rate | 0.79 |
| eval_mean_isr | 0.1038 |
| eval_isr_std | 0.1369 |
| eval_median_isr | 0.0357 |
| eval_proved_only_isr | 0.1314 |
| eval_n_proved | 79 |
| eval_n_problems | 100 |
| eval_component_count_mean | 8.46 |
| eval_component_count_median | 8 |
| eval_component_count_2_ratio | 0 |
| eval_isr_1_ratio | 0 |
| eval_isr_0_ratio | 0.367 |
| eval_isr_gt0_ratio | 0.633 |
| tautological_collapse | false |
| train_total_steps | 500 |
| train_duration_min | 70.5 |
| train_last100_pr | 0.805 |
| train_last100_isr | 0.1432 |
| train_loss | 0.005 |
| by_type false: pr/isr | 0.8 / 0.1318 |
| by_type unknown: pr/isr | 0.7317 / 0.0944 |
| by_type true: pr/isr | 0.8529 / 0.0945 |

### s43: `plan018-additive-random-b01-s43` = failed (disk full). Retry is `plan018-additive-random-b01-s43-r2`:

**exp_id:** `plan018-additive-random-b01-s43-r2` | **status:** DONE | **conclusion:** negative

| Metric | Value |
|--------|-------|
| h7_rate | 0 |
| h7_count | 0 |
| h1_rate | 93.2 |
| h1_count | 82 |
| genuine_rate | 6.8 |
| genuine_count | 6 |

**Note:** No eval_pr/eval_isr in this entry -- only hacking taxonomy counts. h1_rate and genuine_rate appear to be percentages (not fractions).

### s44: `plan018-additive-random-b01-s44` | **status:** DONE | **conclusion:** success

| Metric | Value |
|--------|-------|
| prove_rate | 0.89 |
| mean_isr | 0.0619 |
| isr_std | 0.1756 |
| median_isr | 0 |
| proved_only_mean_isr | 0.0695 |
| n_proved | 89 |
| n_problems | 100 |
| max_isr | 1 |
| min_isr | 0 |
| isr_zero_count | 72 |
| isr_one_count | 2 |
| elapsed_seconds | 1012.7 |
| by_answer false: pr/isr | 0.84 / 0.0533 |
| by_answer unknown: pr/isr | 0.976 / 0.0892 |
| by_answer true: pr/isr | 0.824 / 0.0353 |

---

## 7. ISR beta=0.3 (plan002-b03)

**exp_id:** `plan002-additive-b03-s42` | **status:** DONE | **conclusion:** negative

| Metric | Value |
|--------|-------|
| total_steps | 500 |
| duration_min | 56.7 |
| overall_prove_rate | 0.34025 |
| overall_isr | 0.11527 |
| first20_prove_rate | 0.15625 |
| last50_prove_rate | 0.555 |
| last100_prove_rate | 0.5525 |
| mean_loss | 0.008914 |
| last100_loss | 0.014469 |
| parse_rate | 1 |
| steps_ge_085 | 52 |
| first_step_ge_085 | 46 |
| final_prove_rate | 1 |
| final_isr_mean | 0.3089 |
| final_reward_mean | 1.0927 |

**Note:** This has only training metrics, no eval metrics. Windowed pr: w1-50=0.13, w51-100=0.095, w101-200=0.185, w201-300=0.375, w301-400=0.47625, w401-500=0.5525.

---

## 8. Random beta=0.3 (plan017)

**exp_id:** `plan017-additive-random-s42` | **status:** DONE | **conclusion:** negative

| Metric | Value |
|--------|-------|
| eval_prove_rate | 0.48 |
| eval_mean_isr | 0.0453 |
| eval_isr_std | 0.0759 |
| eval_median_isr | 0 |
| eval_max_isr | 0.2857 |
| eval_proved_only_isr | 0.0943 |
| eval_n_proved | 48 |
| eval_n_problems | 100 |
| eval_component_count_mean | 9.6 |
| eval_component_count_2_ratio | 0 |
| eval_isr_pr_ratio | 0.0943 |
| eval_elapsed_s | 542.3 |
| tautological_collapse | false |
| by_type false: pr/isr | 0.32 / 0.0254 |
| by_type unknown: pr/isr | 0.51 / 0.0518 |
| by_type true: pr/isr | 0.56 / 0.052 |

---

## 9. Convex random (plan013)

`plan013-random-reward-s42` through `r3` all failed. Successful run is `plan013-random-reward-s42-r4`:

**exp_id:** `plan013-random-reward-s42-r4` | **status:** DONE | **conclusion:** success

| Metric | Value |
|--------|-------|
| eval_prove_rate | 1.0 |
| eval_mean_isr | 0.535 |
| eval_isr_std | 0.1282 |
| eval_proved_only_isr | 0.535 |
| eval_median_isr | 0.5 |
| eval_n_proved | 100 |
| eval_n_problems | 100 |
| eval_note | DEGENERATE: trivial 2-component proofs (premise=conclusion, conclusion=conclusion), ISR=0.5 is artifact |

---

## 10. Prolog exec-only (plan006-prolog-exec)

### s42: `plan006-prolog-exec-s42` | **status:** DONE | **conclusion:** negative

| Metric | Value |
|--------|-------|
| eval_prove_rate | 0.83 |
| eval_mean_isr | 0.031 |
| eval_proved_only_isr | 0.037 |
| eval_median_isr | 0 |
| eval_max_isr | 0.2 |
| eval_isr_std | 0.0534 |
| h7_rate | 0 |
| h1_rate | 0 |
| isr_1_rate | 0 |
| single_premise_rate | 0 |
| by_answer true: proved=37, count=40, pr=0.925, isr=0.037 |
| by_answer false: proved=21, count=29, pr=0.724, isr=0.038 |
| by_answer unknown: proved=25, count=31, pr=0.806, isr=0.016 |

### s43: `plan006-prolog-exec-s43` = killed, `s43-r2` = failed. Successful is `plan006-prolog-exec-s43-r3`:

**exp_id:** `plan006-prolog-exec-s43-r3` | **status:** DONE | **conclusion:** negative

| Metric | Value |
|--------|-------|
| eval_prove_rate | 0.56 |
| eval_mean_isr | 0.0084 |
| eval_isr_std | 0.0221 |
| eval_median_isr | 0 |
| eval_proved_only_isr | 0.015 |
| eval_min_isr | 0 |
| eval_max_isr | 0.1 |
| eval_n_proved | 56 |
| eval_n_problems | 100 |
| eval_elapsed_seconds | 868.2 |
| solver | PrologSolver |
| logic_type | prolog |
| by_type false: pr/isr | 0.48 / 0.0043 |
| by_type unknown: pr/isr | 0.6585 / 0.0114 |
| by_type true: pr/isr | 0.5 / 0.0078 |

### s44: `plan006-prolog-exec-s44` | **status:** DONE | **conclusion:** negative

| Metric | Value |
|--------|-------|
| eval_prove_rate | 0.21 |
| eval_mean_isr | 0.0812 |
| eval_isr_std | 0.2343 |
| eval_median_isr | 0 |
| eval_proved_only_isr | 0.3866 |
| eval_min_isr | 0 |
| eval_max_isr | 1 |
| eval_n_proved | 21 |
| eval_n_problems | 100 |
| eval_elapsed_seconds | 683.9 |
| solver | PrologSolver |
| logic_type | prolog |
| by_type false: pr/isr | 0.04 / 0.04 |
| by_type unknown: pr/isr | 0.317 / 0.099 |
| by_type true: pr/isr | 0.206 / 0.09 |

---

## 11. Prolog STA (plan006-prolog-sta)

### s42: `plan006-prolog-sta-s42` | **status:** DONE | **conclusion:** negative

| Metric | Value |
|--------|-------|
| cumulative_prove_rate | 0.848 |
| cumulative_mean_isr | 0.787 |
| final_prove_rate | 1 |
| final_isr | 1 |
| final_reward | 1 |
| saturation_onset_step | 100 |
| train_loss | 0.00716 |
| training_hours | 0.78 |
| final_entropy | 0.01 |
| final_completion_length | 27 |
| initial_completion_length | 120 |
| steps_at_perfect_reward | 400 |
| train_runtime_sec | 2791 |
| eval_prove_rate | 0.5 |
| eval_mean_isr | 0.5 |
| eval_proved_only_isr | 1.0 |
| eval_h7_rate | 1.0 |
| eval_h7_count | 50 |
| eval_proved_count | 50 |
| eval_total_count | 100 |
| eval_n_clauses_mean | 1 |
| eval_isr_distribution | binary: 50x0 + 50x1 |

### s43: `plan006-prolog-sta-s43` | **status:** RUNNING | metrics: None | conclusion: None

### s44: `plan006-prolog-sta-s44` | **status:** RUNNING | metrics: None | conclusion: None

---

## 12. Premise-count-matched data

**No experiment in this registry contains "premise_count_matched" data.** The string does not appear anywhere in any experiment's metrics, conclusion, hypothesis, or extra fields. The Claim 2 references appear only in the hypothesis text of plan002-b01-s43 and plan002-b01-s44, referring to the ISR beta=0.1 multi-seed results above.

---

## Bonus entries also extracted

**plan012-hacking-taxonomy** | DONE | conclusion: success -- ISR vs Random hacking taxonomy comparison:
- isr_b01_genuine_rate: 0.259, random_b01_genuine_rate: 0.177, genuine_rate_delta_pp: 8.2
- isr_b01_conclusion_embedding_rate: 0.728, random_b01_conclusion_embedding_rate: 0.785
- isr_b01_genuine_mean_isr: 0.6723, random_b01_genuine_mean_isr: 0.3427
- isr_b01_hacking_rate: 0.741, random_b01_hacking_rate: 0.823

**plan003-eval-exec-only-r5** | DONE | conclusion: success:
- prove_rate: 0.32, mean_isr: 0.2055, isr_std: 0.3194, proved_only_isr: 0.6423, proved_count: 32, total_samples: 100

**plan005-sta-low-s42** | DONE | conclusion: negative:
- Training only, 500 steps. overall_prove_rate: 0.5657, overall_isr: 0.1682, last100_pr: 0.7725, last100_isr: 0.2299

**plan014-downstream-nli-s42** | DONE | conclusion: negative:
- overall_accuracy: 0.341, proved_rate: 0.915, spearman_rho: -0.049, spearman_p: 0.187, bon_isr_accuracy: 0.35, bon_oracle_accuracy: 0.44, isr_bucket_high_acc: 0.75, isr_bucket_mid_acc: 0.377, isr_bucket_low_acc: 0.327

agentId: afbb79756989adaac (use SendMessage with to: 'afbb79756989adaac' to continue this agent)
&lt;usage>total_tokens: 47607
tool_uses: 8
duration_ms: 158761&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "eb5b7954-c1fd-473d-8da7-d1389c3f22e7",
  "uuid": "469b513a-2ab1-400a-a69a-39623044ee8d",
  "tool_use_result": {
    "status": "completed",
    "prompt": "I need to extract specific experiment metrics from a large registry JSON file at:\n`/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/eb5b7954-c1fd-473d-8da7-d1389c3f22e7/tool-results/mcp-agent-ml-research-read_registry-1778779433924.txt`\n\nThe file has the schema `{result: string}` where result is a JSON string containing experiment entries.\n\nI need you to extract the following data points from the registry. For each experiment, I need: exp_id, status, metrics (especially eval_pr, eval_isr, proved_only_isr, avg_components, h7_rate, h1_rate, genuine_rate, n_proved, hacking_mode), and any conclusion text.\n\nThe experiments I need data for are:\n1. **Base model / phase0** - baseline evaluation\n2. **SFT baseline** - plan009 related\n3. **Exec-only 500 steps** - plan001 seeds s42, s43, s44\n4. **Exec-only 1000 steps** - plan016\n5. **ISR β=0.1** - plan002-b01 seeds s42, s43, s44\n6. **Random β=0.1** - plan018 seeds s42, s43, s44\n7. **ISR β=0.3** - plan002-b03\n8. **Random β=0.3** - plan017\n9. **Convex random** - plan013\n10. **Prolog exec-only** - seeds s42, s43, s44\n11. **Prolog STA** - seeds s42, s43, s44\n12. **Claim2 premise-count-matched data** - any entry with premise_count_matched ISR values\n\nSteps:\n1. First probe the structure: `jq '.result | fromjson | type' file` and `jq '.result | fromjson | length' file` and `jq '.result | fromjson | .[0] | keys' file`\n2. Then extract all experiments with their exp_id, status, metrics, and conclusion fields.\n3. Use jq or python to filter and format.\n\nReport back ALL the numeric values you find - I need exact numbers for every metric. Don't summarize, give me the raw data.",
    "agentId": "afbb79756989adaac",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "No \"premise_count_matched\" data exists in this registry. Here is the complete extracted data:\n\n---\n\n## 1. Base model / phase0 baseline\n\n**exp_id:** `sta-phase0-baseline` | **status:** DONE | **conclusion:** success\n\n| Metric | Value |\n|--------|-------|\n| prove_rate | 0.12 |\n| mean_isr | 0.0641 |\n| isr_std | 0.1983 |\n| median_isr | 0 |\n| isr_range | [0, 0.889] |\n| proved_count | 12 |\n| total_samples | 100 |\n| xor_affected_samples | 34 |\n| effective_prove_rate_no_xor | 0.182 |\n| avg_time_per_sample_s | 3.4 |\n| total_runtime_s | 336 |\n| isr_by_answer: true | n=34, proved=9, pr=0.265, mean_isr=0.1345 |\n| isr_by_answer: false | n=25, proved=1, pr=0.04, mean_isr=0.024 |\n| isr_by_answer: unknown | n=41, proved=2, pr=0.049, mean_isr=0.0302 |\n\nAlso related: **`sta-gt-isr-baseline`** | status: DONE | conclusion: success\n- gt_prove_rate: 0.18, gt_mean_isr: 0.5588, gt_isr_std: 0.2582, gt_isr_median: 0.6125, solver_execution_rate: 1, true_prove_rate: 0.5, true_mean_isr: 0.5833\n\n---\n\n## 2. SFT baseline (plan009)\n\nOnly `plan009-sft-baseline-s42-r4` has metrics. Prior attempts (r1=killed, r2=failed, r3=failed).\n\n**exp_id:** `plan009-sft-baseline-s42-r4` | **status:** DONE | **conclusion:** success\n\n| Metric | Value |\n|--------|-------|\n| eval_prove_rate | 0.14 |\n| eval_mean_isr | 0.08 |\n| eval_isr_std | 0.214 |\n| eval_median_isr | 0 |\n| eval_max_isr | 0.833 |\n| eval_proved_only_isr | 0.571 |\n| eval_n_proved | 14 |\n| eval_n_problems | 100 |\n| train_final_loss | 0.0287 |\n| train_token_accuracy | 0.9935 |\n| train_epochs | 7.94 |\n| train_runtime_sec | 789.6 |\n| h7_rate | 0 |\n| h7_count | 0 |\n| h1_rate | 0.071 |\n| h1_count | 1 |\n| genuine_rate | 0.929 |\n| genuine_count | 13 |\n| tautological_collapse | false |\n| by_answer: true | count=34, proved=13, pr=0.382, isr=0.226 |\n| by_answer: unknown | count=41, proved=1, pr=0.024, isr=0.008 |\n| by_answer: false | count=25, proved=0, pr=0, isr=0 |\n\n---\n\n## 3. Exec-only 500 steps (plan001)\n\n### s42: `plan001-exec-only-s42` = failed, no metrics. Successful retry is `plan001-exec-only-s42-r2`:\n\n**exp_id:** `plan001-exec-only-s42-r2` | **status:** DONE | **conclusion:** success\n\n| Metric | Value |\n|--------|-------|\n| eval_prove_rate | 0.93 |\n| eval_mean_isr | 0.1232 |\n| eval_isr_std | 0.1887 |\n| eval_proved_only_isr | 0.1324 |\n| eval_median_isr | 0 |\n| eval_n_proved | 93 |\n| eval_n_problems | 100 |\n| h7_rate | 0 |\n| h7_count | 0 |\n| h1_rate | 0.871 |\n| h1_count | 81 |\n| genuine_rate | 0.129 |\n| genuine_count | 12 |\n| genuine_mean_isr | 0.3141 |\n| h1_mean_isr | 0.1055 |\n| conclusion_embedding_total | 0.871 |\n\n### s43: `plan001-exec-only-s43` through `s43-r3` all failed. Successful run is `plan001-exec-only-s43-r4`:\n\n**exp_id:** `plan001-exec-only-s43-r4` | **status:** DONE | **conclusion:** negative\n\n| Metric | Value |\n|--------|-------|\n| eval_sampling_prove_rate | 0.14 |\n| eval_sampling_mean_isr | 0 |\n| eval_sampling_n_proved | 14 |\n| eval_sampling_temperature | 0.7 |\n| by_answer: true | count=34, proved=6, pr=0.176 |\n| by_answer: false | count=25, proved=2, pr=0.08 |\n| by_answer: unknown | count=41, proved=6, pr=0.146 |\n\n**Note:** This is sampling-based eval (temperature=0.7), not greedy. ISR=0 across the board.\n\n### s44: `plan001-exec-only-s44`\n\n**exp_id:** `plan001-exec-only-s44` | **status:** DONE | **conclusion:** negative\n\n| Metric | Value |\n|--------|-------|\n| eval_prove_rate | 0.98 |\n| eval_mean_isr | 0.57 |\n| eval_isr_std | 0.2013 |\n| eval_median_isr | 0.5 |\n| eval_proved_only_isr | 0.5816 |\n| eval_n_proved | 98 |\n| eval_n_problems | 100 |\n| eval_component_count_mean | 2.04 |\n| eval_component_count_2 | 94 |\n| eval_component_count_3 | 4 |\n| tautological_collapse | **true** |\n| h7_rate | **1.0** |\n| h7_count | 97 |\n| h1_rate | 0 |\n| h1_count | 0 |\n| genuine_rate | 0 |\n| genuine_count | 0 |\n| conclusion_embedding_total | 1 |\n\n---\n\n## 4. Exec-only 1000 steps (plan016)\n\n**exp_id:** `plan016-extended-1000-s42` | **status:** DONE | **conclusion:** success\n\n**Train metrics:**\n| Metric | Value |\n|--------|-------|\n| total_steps | 1000 |\n| duration_min | 146 |\n| final_prove_rate | 0.8396 |\n| final_mean_isr | 0.0503 |\n| train_loss | 0.0125 |\n| epoch | 4 |\n| steps 001-100: pr/isr | 0.19 / 0.0859 |\n| steps 101-200: pr/isr | 0.66 / 0.1115 |\n| steps 201-300: pr/isr | 0.838 / 0.0985 |\n| steps 301-400: pr/isr | 0.907 / 0.054 |\n| steps 401-500: pr/isr | 0.927 / 0.0433 |\n| steps 501-600: pr/isr | 0.963 / 0.0408 |\n| steps 601-700: pr/isr | 0.965 / 0.02 |\n| steps 701-800: pr/isr | 0.988 / 0.0178 |\n| steps 801-900: pr/isr | 0.978 / 0.017 |\n| steps 901-1000: pr/isr | 0.981 / 0.0144 |\n\n**Eval metrics:**\n| Metric | Value |\n|--------|-------|\n| prove_rate | 0.96 |\n| n_proved | 96 |\n| mean_isr | 0.0027 |\n| isr_std | 0.0118 |\n| median_isr | 0 |\n| proved_only_mean_isr | 0.0028 |\n| max_isr | 0.0588 |\n| isr_0_ratio | 0.9479 |\n| isr_1_ratio | 0 |\n| component_count_mean | 18.55 |\n| component_count_2_ratio | 0 |\n| mean_n_necessary | 0.052 |\n| n_necessary_0_ratio | 0.9479 |\n| tautological_collapse | false |\n| by_answer false: pr/isr | 0.8966 / 0 |\n| by_answer unknown: pr/isr | 0.9677 / 0.0053 |\n| by_answer true: pr/isr | 1.0 / 0.0026 |\n| eval_time_seconds | 396.3 |\n\n---\n\n## 5. ISR beta=0.1 (plan002-b01)\n\n### s42: `plan002-additive-b01-s42` | **status:** DONE | **conclusion:** success\n\n| Metric | Value |\n|--------|-------|\n| eval_prove_rate | 0.81 |\n| eval_mean_isr | 0.3365 |\n| eval_isr_std | 0.3227 |\n| eval_proved_only_isr | 0.4154 |\n| eval_median_isr | 0.2 |\n| eval_n_proved | 81 |\n| eval_n_problems | 100 |\n| eval_component_count_mean | 5.58 |\n| eval_component_count_2_ratio | 0.037 |\n| eval_isr_1_ratio | 0.124 |\n| eval_isr_0_ratio | 0.037 |\n| tautological_collapse | false |\n| train_total_steps | 500 |\n| train_duration_min | 63 |\n| train_last100_pr | 0.6875 |\n| train_last100_isr | 0.1954 |\n| train_last100_loss | 0.015 |\n| by_type false: pr/isr | 0.88 / 0.3515 |\n| by_type unknown: pr/isr | 0.83 / 0.3684 |\n| by_type true: pr/isr | 0.74 / 0.2869 |\n\n### s43: `plan002-additive-b01-s43` | **status:** DONE | **conclusion:** negative\n\n| Metric | Value |\n|--------|-------|\n| eval_prove_rate | 0.61 |\n| eval_mean_isr | 0.5063 |\n| eval_isr_std | 0.4518 |\n| eval_median_isr | 0.5 |\n| eval_proved_only_isr | 0.8301 |\n| component_count_mean | 4.03 |\n| component_count_2_ratio | 0 |\n| tautological_collapse | false |\n| isr_0_ratio | 0.39 |\n| isr_1_ratio | 0.656 |\n| proved_single_premise_ratio | 1 |\n| h7_rate_calibrated | 0.967 |\n| **hacking_mode** | **conclusion_duplication_isr_inflation** |\n| conclusion_embedding | true |\n| train_total_steps | 500 |\n| train_duration_min | 53 |\n| train_loss | 0.012 |\n| by_answer false: PR/ISR | 0.72 / 0.6 |\n| by_answer unknown: PR/ISR | 0.537 / 0.442 |\n| by_answer true: PR/ISR | 0.618 / 0.515 |\n\n### s44: `plan002-additive-b01-s44` | **status:** DONE | **conclusion:** negative\n\n| Metric | Value |\n|--------|-------|\n| eval_prove_rate | 0.89 |\n| eval_mean_isr | 0.803 |\n| eval_isr_std | 0.3418 |\n| eval_median_isr | 1 |\n| component_count_mean | 4.33 |\n| component_count_2_ratio | 0.022 |\n| tautological_collapse | false |\n| isr_0_ratio | 0.12 |\n| isr_1_ratio | 0.73 |\n| proved_single_premise_ratio | 1 |\n| h7_rate_calibrated | 0.865 |\n| **hacking_mode** | **conclusion_duplication_isr_inflation** |\n| conclusion_embedding | true |\n| component_dist | {2: 2, 4: 54, 5: 33} |\n| by_answer false: PR/ISR | 0.88 / 0.824 |\n| by_answer unknown: PR/ISR | 0.927 / 0.837 |\n| by_answer true: PR/ISR | 0.853 / 0.747 |\n\n---\n\n## 6. Random beta=0.1 (plan018)\n\n### s42: `plan018-additive-random-b01-s42` | **status:** DONE | **conclusion:** negative\n\n| Metric | Value |\n|--------|-------|\n| eval_prove_rate | 0.79 |\n| eval_mean_isr | 0.1038 |\n| eval_isr_std | 0.1369 |\n| eval_median_isr | 0.0357 |\n| eval_proved_only_isr | 0.1314 |\n| eval_n_proved | 79 |\n| eval_n_problems | 100 |\n| eval_component_count_mean | 8.46 |\n| eval_component_count_median | 8 |\n| eval_component_count_2_ratio | 0 |\n| eval_isr_1_ratio | 0 |\n| eval_isr_0_ratio | 0.367 |\n| eval_isr_gt0_ratio | 0.633 |\n| tautological_collapse | false |\n| train_total_steps | 500 |\n| train_duration_min | 70.5 |\n| train_last100_pr | 0.805 |\n| train_last100_isr | 0.1432 |\n| train_loss | 0.005 |\n| by_type false: pr/isr | 0.8 / 0.1318 |\n| by_type unknown: pr/isr | 0.7317 / 0.0944 |\n| by_type true: pr/isr | 0.8529 / 0.0945 |\n\n### s43: `plan018-additive-random-b01-s43` = failed (disk full). Retry is `plan018-additive-random-b01-s43-r2`:\n\n**exp_id:** `plan018-additive-random-b01-s43-r2` | **status:** DONE | **conclusion:** negative\n\n| Metric | Value |\n|--------|-------|\n| h7_rate | 0 |\n| h7_count | 0 |\n| h1_rate | 93.2 |\n| h1_count | 82 |\n| genuine_rate | 6.8 |\n| genuine_count | 6 |\n\n**Note:** No eval_pr/eval_isr in this entry -- only hacking taxonomy counts. h1_rate and genuine_rate appear to be percentages (not fractions).\n\n### s44: `plan018-additive-random-b01-s44` | **status:** DONE | **conclusion:** success\n\n| Metric | Value |\n|--------|-------|\n| prove_rate | 0.89 |\n| mean_isr | 0.0619 |\n| isr_std | 0.1756 |\n| median_isr | 0 |\n| proved_only_mean_isr | 0.0695 |\n| n_proved | 89 |\n| n_problems | 100 |\n| max_isr | 1 |\n| min_isr | 0 |\n| isr_zero_count | 72 |\n| isr_one_count | 2 |\n| elapsed_seconds | 1012.7 |\n| by_answer false: pr/isr | 0.84 / 0.0533 |\n| by_answer unknown: pr/isr | 0.976 / 0.0892 |\n| by_answer true: pr/isr | 0.824 / 0.0353 |\n\n---\n\n## 7. ISR beta=0.3 (plan002-b03)\n\n**exp_id:** `plan002-additive-b03-s42` | **status:** DONE | **conclusion:** negative\n\n| Metric | Value |\n|--------|-------|\n| total_steps | 500 |\n| duration_min | 56.7 |\n| overall_prove_rate | 0.34025 |\n| overall_isr | 0.11527 |\n| first20_prove_rate | 0.15625 |\n| last50_prove_rate | 0.555 |\n| last100_prove_rate | 0.5525 |\n| mean_loss | 0.008914 |\n| last100_loss | 0.014469 |\n| parse_rate | 1 |\n| steps_ge_085 | 52 |\n| first_step_ge_085 | 46 |\n| final_prove_rate | 1 |\n| final_isr_mean | 0.3089 |\n| final_reward_mean | 1.0927 |\n\n**Note:** This has only training metrics, no eval metrics. Windowed pr: w1-50=0.13, w51-100=0.095, w101-200=0.185, w201-300=0.375, w301-400=0.47625, w401-500=0.5525.\n\n---\n\n## 8. Random beta=0.3 (plan017)\n\n**exp_id:** `plan017-additive-random-s42` | **status:** DONE | **conclusion:** negative\n\n| Metric | Value |\n|--------|-------|\n| eval_prove_rate | 0.48 |\n| eval_mean_isr | 0.0453 |\n| eval_isr_std | 0.0759 |\n| eval_median_isr | 0 |\n| eval_max_isr | 0.2857 |\n| eval_proved_only_isr | 0.0943 |\n| eval_n_proved | 48 |\n| eval_n_problems | 100 |\n| eval_component_count_mean | 9.6 |\n| eval_component_count_2_ratio | 0 |\n| eval_isr_pr_ratio | 0.0943 |\n| eval_elapsed_s | 542.3 |\n| tautological_collapse | false |\n| by_type false: pr/isr | 0.32 / 0.0254 |\n| by_type unknown: pr/isr | 0.51 / 0.0518 |\n| by_type true: pr/isr | 0.56 / 0.052 |\n\n---\n\n## 9. Convex random (plan013)\n\n`plan013-random-reward-s42` through `r3` all failed. Successful run is `plan013-random-reward-s42-r4`:\n\n**exp_id:** `plan013-random-reward-s42-r4` | **status:** DONE | **conclusion:** success\n\n| Metric | Value |\n|--------|-------|\n| eval_prove_rate | 1.0 |\n| eval_mean_isr | 0.535 |\n| eval_isr_std | 0.1282 |\n| eval_proved_only_isr | 0.535 |\n| eval_median_isr | 0.5 |\n| eval_n_proved | 100 |\n| eval_n_problems | 100 |\n| eval_note | DEGENERATE: trivial 2-component proofs (premise=conclusion, conclusion=conclusion), ISR=0.5 is artifact |\n\n---\n\n## 10. Prolog exec-only (plan006-prolog-exec)\n\n### s42: `plan006-prolog-exec-s42` | **status:** DONE | **conclusion:** negative\n\n| Metric | Value |\n|--------|-------|\n| eval_prove_rate | 0.83 |\n| eval_mean_isr | 0.031 |\n| eval_proved_only_isr | 0.037 |\n| eval_median_isr | 0 |\n| eval_max_isr | 0.2 |\n| eval_isr_std | 0.0534 |\n| h7_rate | 0 |\n| h1_rate | 0 |\n| isr_1_rate | 0 |\n| single_premise_rate | 0 |\n| by_answer true: proved=37, count=40, pr=0.925, isr=0.037 |\n| by_answer false: proved=21, count=29, pr=0.724, isr=0.038 |\n| by_answer unknown: proved=25, count=31, pr=0.806, isr=0.016 |\n\n### s43: `plan006-prolog-exec-s43` = killed, `s43-r2` = failed. Successful is `plan006-prolog-exec-s43-r3`:\n\n**exp_id:** `plan006-prolog-exec-s43-r3` | **status:** DONE | **conclusion:** negative\n\n| Metric | Value |\n|--------|-------|\n| eval_prove_rate | 0.56 |\n| eval_mean_isr | 0.0084 |\n| eval_isr_std | 0.0221 |\n| eval_median_isr | 0 |\n| eval_proved_only_isr | 0.015 |\n| eval_min_isr | 0 |\n| eval_max_isr | 0.1 |\n| eval_n_proved | 56 |\n| eval_n_problems | 100 |\n| eval_elapsed_seconds | 868.2 |\n| solver | PrologSolver |\n| logic_type | prolog |\n| by_type false: pr/isr | 0.48 / 0.0043 |\n| by_type unknown: pr/isr | 0.6585 / 0.0114 |\n| by_type true: pr/isr | 0.5 / 0.0078 |\n\n### s44: `plan006-prolog-exec-s44` | **status:** DONE | **conclusion:** negative\n\n| Metric | Value |\n|--------|-------|\n| eval_prove_rate | 0.21 |\n| eval_mean_isr | 0.0812 |\n| eval_isr_std | 0.2343 |\n| eval_median_isr | 0 |\n| eval_proved_only_isr | 0.3866 |\n| eval_min_isr | 0 |\n| eval_max_isr | 1 |\n| eval_n_proved | 21 |\n| eval_n_problems | 100 |\n| eval_elapsed_seconds | 683.9 |\n| solver | PrologSolver |\n| logic_type | prolog |\n| by_type false: pr/isr | 0.04 / 0.04 |\n| by_type unknown: pr/isr | 0.317 / 0.099 |\n| by_type true: pr/isr | 0.206 / 0.09 |\n\n---\n\n## 11. Prolog STA (plan006-prolog-sta)\n\n### s42: `plan006-prolog-sta-s42` | **status:** DONE | **conclusion:** negative\n\n| Metric | Value |\n|--------|-------|\n| cumulative_prove_rate | 0.848 |\n| cumulative_mean_isr | 0.787 |\n| final_prove_rate | 1 |\n| final_isr | 1 |\n| final_reward | 1 |\n| saturation_onset_step | 100 |\n| train_loss | 0.00716 |\n| training_hours | 0.78 |\n| final_entropy | 0.01 |\n| final_completion_length | 27 |\n| initial_completion_length | 120 |\n| steps_at_perfect_reward | 400 |\n| train_runtime_sec | 2791 |\n| eval_prove_rate | 0.5 |\n| eval_mean_isr | 0.5 |\n| eval_proved_only_isr | 1.0 |\n| eval_h7_rate | 1.0 |\n| eval_h7_count | 50 |\n| eval_proved_count | 50 |\n| eval_total_count | 100 |\n| eval_n_clauses_mean | 1 |\n| eval_isr_distribution | binary: 50x0 + 50x1 |\n\n### s43: `plan006-prolog-sta-s43` | **status:** RUNNING | metrics: None | conclusion: None\n\n### s44: `plan006-prolog-sta-s44` | **status:** RUNNING | metrics: None | conclusion: None\n\n---\n\n## 12. Premise-count-matched data\n\n**No experiment in this registry contains \"premise_count_matched\" data.** The string does not appear anywhere in any experiment's metrics, conclusion, hypothesis, or extra fields. The Claim 2 references appear only in the hypothesis text of plan002-b01-s43 and plan002-b01-s44, referring to the ISR beta=0.1 multi-seed results above.\n\n---\n\n## Bonus entries also extracted\n\n**plan012-hacking-taxonomy** | DONE | conclusion: success -- ISR vs Random hacking taxonomy comparison:\n- isr_b01_genuine_rate: 0.259, random_b01_genuine_rate: 0.177, genuine_rate_delta_pp: 8.2\n- isr_b01_conclusion_embedding_rate: 0.728, random_b01_conclusion_embedding_rate: 0.785\n- isr_b01_genuine_mean_isr: 0.6723, random_b01_genuine_mean_isr: 0.3427\n- isr_b01_hacking_rate: 0.741, random_b01_hacking_rate: 0.823\n\n**plan003-eval-exec-only-r5** | DONE | conclusion: success:\n- prove_rate: 0.32, mean_isr: 0.2055, isr_std: 0.3194, proved_only_isr: 0.6423, proved_count: 32, total_samples: 100\n\n**plan005-sta-low-s42** | DONE | conclusion: negative:\n- Training only, 500 steps. overall_prove_rate: 0.5657, overall_isr: 0.1682, last100_pr: 0.7725, last100_isr: 0.2299\n\n**plan014-downstream-nli-s42** | DONE | conclusion: negative:\n- overall_accuracy: 0.341, proved_rate: 0.915, spearman_rho: -0.049, spearman_p: 0.187, bon_isr_accuracy: 0.35, bon_oracle_accuracy: 0.44, isr_bucket_high_acc: 0.75, isr_bucket_mid_acc: 0.377, isr_bucket_low_acc: 0.327"
      }
    ],
    "totalDurationMs": 158761,
    "totalTokens": 47607,
    "totalToolUseCount": 8,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 780,
      "cache_read_input_tokens": 39642,
      "output_tokens": 7184,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 780
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7184,
          "cache_read_input_tokens": 39642,
          "cache_creation_input_tokens": 780,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 780,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 1,
      "searchCount": 0,
      "bashCount": 7,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  }
}
```

</details>

---

### Assistant

_source line 43_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the data I need. Let me also check for the random_b01_s43 eval data since the evidence table shows it was RUNNING but the registry agent found `plan018-additive-random-b01-s43-r2` with status DONE but only hacking taxonomy counts (no eval_pr/eval_isr). Let me also check the evidence table for random_b01_s43 data more carefully.

Looking at the evidence tables:
- Random β=0.1 s43: RUNNING in the evidence table
- But the registry shows plan018-additive-random-b01-s43-r2 DONE with h7_rate=0, h1_rate=93.2, h1_count=82, genuine_rate=6.8, genuine_count=6


- The evidence table was captured earlier when s43 was still running, but it's since completed. The registry gives me the hacking taxonomy results (n_proved = 88 total), but I'm still missing the eval_pr and eval_isr metrics.

Wait, I should check the task description itself—it already has a complete JSON structure with all the values I need. Let me cross-reference that against what I'm seeing in the registry and evidence tables to verify everything lines up.

The pr and n_proved values match up (88 total from 82+6), so the ISR metrics must be coming from a separate evaluation that wasn't captured in the registry. The evidence table shows s43 as RUNNING, but the task description has final values for it, which means the data was collected after that snapshot was taken.

Now I'm going to systematically pull the values from the registry as my primary source, use the evidence tables to validate, and structure everything according to the JSON format provided in the task description.

Checking base_model: the registry gives pr=0.12 and isr=0.0641 which rounds to 0.064, matching what's in the evidence table and task description. For sft_baseline, all the metrics align across sources—pr=0.14, isr=0.08, and the various breakdown metrics like h1_rate and genuine_rate. For exec_only_500 (s42), the registry shows pr=0.93 with isr=0.1232 and proved_only_isr=0.1324, which the evidence table confirms with its uncertainty ranges.

The component count for s42 is tricky—the registry doesn't have it listed, but both the evidence table and task description show 6.58, so I'll go with that value. Moving on to s43, the registry shows pr=0.14 with sampling enabled, isr=0, temperature at 0.7.

For s44, everything lines up nicely across all three sources: pr=0.98, isr around 0.57, proved_only_isr at 0.582, components at 2.04, and h7_rate at 1.0.

Now I'm computing the aggregate statistics across these three seeds by calculating the mean and standard deviation of the performance ratios. .4445/3) = sqrt(0.1482) = 0.3849
- Task desc says "0.68±0.47" which matches sample std ≈ 0.47

- mean isr = (0.1232+0+0.57)/3 = 0.6932/3 = 0.2311
- std isr (sample): sqrt(((0.1232-0.2311)^2 + (0-0.2311)^2 + (0.57-0.2311)^2)/2)
  = sqrt((0.01163 + 0.05341 + 0.11489)/2)
  = sqrt(0.17993/2)
  = sqrt(0.08997)
  = 0.2999 ≈ 0.30
- Task desc says "0.23±0.30" ✓

### exec_only_1000
- Registry: pr=0.96

Now checking the exec_only_1000 metrics against the evidence table and task description. The pr value of 0.96 matches, along with isr=0.003±0.012, proved_only_isr=0.003, and components=18.55 across all three sources.

### ISR b01 s42
- Registry shows pr=0.81, isr=0.3365, proved_only_isr=0.4154, components=5.58, n_proved=81
- The registry is missing h7/h1/genuine breakdowns for s42, but the evidence table provides them: H7=16% (13/81), H1=51.9% (42/81), Genuine=32.1% (26/81)
- Task description confirms pr=0.81, isr=0.337, proved_only_isr values, though the entry appears incomplete

### ISR b01 s43
- Registry: pr=0.61, isr=0.5063, proved_only_isr=0.8301, components=4.03, h7_rate_calibrated=0.967, hacking_mode=conclusion_duplication_isr_inflation
- Evidence table shows H7=96.7% (59/61), H1=0%, Genuine=~3% (~2/61)
- Task description starts with pr=0.61, isr=0.506 but the entry is cut off

### ISR b01 s44
Now looking at the next registry entry with pr=0.89 and isr=0.803. The proved_only_isr isn't directly listed, but I can derive it from the mean isr value of 0.803 given the prove rate of 0.89. The component count averages around 4.33 with an h7 rate calibrated to 0.865.

Checking the evidence table shows H7 at 86.5% (77/89), H1 at 0%, and genuine cases around 13.5% (12/89), which aligns with the task description metrics of pr=0.89, isr=0.803, proved_only_isr=0.902, components=4.33, h7_rate=0.865, h1_rate=0, genuine_rate=0.135, n_proved=89.

Now computing the mean prove rate across the three entries: (0.81+0.61+0.89)/3 = 0.77.

For the standard deviation of prove rate, I'm calculating the variance from the mean and getting approximately 0.14, then computing the mean ISR across the three values to get 0.55, with its standard deviation calculation in progress.

Now I'm looking at the registry data for a specific run showing a prove rate of 0.79, an ISR of 0.1038, and evidence distribution where H1 accounts for about 71% of the 79 components while genuine cases make up the remaining 29%.

For the next run, the registry shows 82 H1 cases and 6 genuine cases totaling 88 proved components, which gives a prove rate of 0.88, with H1 representing 93.2% and genuine at 6.8%.

The registry doesn't have eval ISR values for s43, so I'm pulling the ISR metrics from the task description instead—isr=0.051 and proved_only_isr=0.058.

Moving to s44, the registry and task description align well: pr=0.89 with 71 H1 cases and 18 genuine cases out of 89 total proved components, giving H1 a rate of 79.8% and genuine 20.2%.

Now I'm calculating the mean across these three runs: the prove rates average to 0.853.

Computing standard deviations and ISR metrics...

Now I'm looking at the h1_rate and genuine_rate means across the three datasets, which give me 0.813 and 0.187 respectively. For ISR b03, the registry shows overall metrics of pr=0.34 and isr=0.115, but the evidence table has different values at pr=0.18 and isr=0.026.

Since the evidence table comes from eval_sta.py, I'll use those eval metrics instead. For Random b03, the registry and evidence table align well with pr=0.48, isr=0.045, and proved_only_isr=0.094. Moving on to Convex random, which shows pr=1.0 and isr=0.535 in the registry.

Now I'm checking the Prolog exec-only results across three scenarios (s42, s43, s44), where the registry values look consistent, and I'm calculating the mean and standard deviation across these runs. Finishing the standard deviation calculation for ISR, then I'm seeing the final metrics: precision-recall of 0.53±0.31 and ISR of 0.040±0.037. Now moving into the Prolog STA section where I'm checking the registry values and evidence table for s42, which all match at pr=0.50, isr=0.500, proved_only_isr=1.0, and h7_rate=1.0, while s43 and s44 are still running.

For the premise-count-matched metric, I'm pulling the evidence table data showing ISR genuine at 0.2578 versus random genuine at 0.2434 with a ratio of 1.06 for cases with at least 3 premises, and cross-referencing this against the plan012 taxonomy which gives higher mean ISR values of 0.6723 for ISR versus 0.3427 for random. I need to verify the h7/h1/genuine metrics for ISR b01 s42 since the registry doesn't have them but the evidence table should.

Looking at the evidence table, I see H7 at 16% (13/81), H1 at 51.9% (42/81), and Genuine at 32.1% (26/81) from the hacking taxonomy analysis. Now I'm noticing some discrepancies in how the data's being reported—for exec_only s44, the 94% in the evidence table refers to component_count_2 (2-component proofs), not the H7 rate itself, which is actually 100% based on the 97 proved cases. I need to clarify similar issues with the random b01 s43 data.

For the remaining entries, I'm seeing that some have registry data marked as RUNNING but are now DONE, while others like ISR b03 only have training metrics in the registry but evaluation metrics in the evidence table. The task asks me to pull exact values from the registry where available, but for gaps like ISR b03's eval metrics or random b01 s43's eval ISR, I'll need to fill in from the evidence table and flag those sources.

Now I'm double-checking the precision on key values—the registry gives me ISR b01 s42 as 0.3365 which rounds to 0.337 matching the task description, and proved_only_isr as 0.4154 rounding to 0.415. For ISR b01 s43, the registry shows 0.5063 and 0.8301 which align with the task's 0.506 and 0.830. I need to verify ISR b01 s44's proved_only_isr since the registry only shows the mean_isr of 0.803.

Working through the calculation: if 100 problems were tested with 89 proving and ISR>0, then the sum of all ISRs is 80.3, so proved_only_isr becomes 80.3 divided by 89 which gives 0.9022, matching the task's 0.902. For the Random benchmark, b01 s42 shows 0.1038 and 0.1314 rounding to 0.104 and 0.131, while b01 s44 has 0.0619 and 0.0695 rounding to 0.062 and 0.070. I'm now looking at Random b01 s43 where the registry indicates 82 h1_count and 6 genuine_count with a pr value of 88.

The h1_rate in the registry for plan018-s43-r2 is actually 93.2 percent, so h1_rate equals 0.932 and genuine_rate equals 0.068, which aligns with the task description. With n_proved being 88, I need to carefully construct the JSON output using the most precise registry values, computing the means and standard deviations correctly, and including all fields from the task description.

Now I'm calculating the sample standard deviations for each metric across the three data points. For exec_only_500, the pr values give a mean of about 0.68 with a standard deviation of 0.47, and the isr values yield a mean around 0.23 with a standard deviation of 0.30.

Moving on to isr_b01, the pr metric shows a mean of 0.77 with a tighter standard deviation of 0.14, while I'm working through the isr calculations which appear to be in progress. Now I'm finishing the precision-recall calculation for random_b01 and moving through the ISR metrics, then calculating the mean rates for h1 and genuine classifications. Starting on the prolog exec-only dataset with similar mean and standard deviation computations. I'm calculating the mean and standard deviation for the ISR b01 proved_only_isr values, which gives me 0.716±0.26—matching what's in the evidence table. The mean for ISR b01 components comes out to 4.65, and now I need to identify what other data points are required for table2_h.

For table2, I'm reorganizing the h7/h1/genuine data from table1 across all conditions. Looking at claim2_isr_vs_random, I have the premise_count_matched ratios from the evidence table showing ISR at 0.2578 versus random at 0.2434 (ratio of 1.06). For the ISR 3-seed analysis, I'm pulling the precision and ISR values with their uncertainties, and I need to calculate the genuine_mean from the three seed runs—which works out to 0.163 when I average the individual genuine values.

Now I'm checking the random 3-seed metrics where precision is 0.85±0.06 and ISR drops to 0.07±0.03 with h7_mean at 0 and genuine_mean at 0.187. I need to verify the n_proved calculation for random_b01_s43 using the registry data—h1_count of 82 plus genuine_count of 6 gives me 88 total, so precision is 0.88. The eval ISR values from the task description need source notation since they're not in the registry, and I'm working through a registry entry that shows DONE status but appears incomplete.

Looking at the rate conversions, the registry percentages of 93.2 for h1_rate and 6.8 for genuine_rate translate to 0.932 and 0.068 as fractions. The evidence table shows s43 as RUNNING, but since the registry confirms the hacking taxonomy is complete with n_proved at 88, the precision of 0.88 holds. I'm ready to build the JSON output now, keeping the structure from the task description without adding extra provenance fields.

Generating the JSON output... Looking at the performance metrics for the exec_only_500 configuration across different seeds, I can see the s42 variant achieved a much higher proof rate of 93% with strong H1 conclusion embedding at 87.1%, while s43 shows significantly lower performance at 14% with no improvement in the ISR metric. I'm looking at the aggregated statistics across these experiments and noticing significant seed variance in the results. The ISR values show a mean of 0.23 with a standard deviation of 0.30, which is quite substantial. I need to be careful about distinguishing between the different ISR metrics in the registry—specifically tracking which values represent eval_mean_isr versus other variants. For the random_b01 s43 entry that was still running in the evidence table, the registry provides specific ISR values that must have come from a more recent data source.

I'm cross-referencing the evidence table against the registry entries to catch discrepancies, like the exec_only_500 s42 component count that appears in one but not the other. Since the task provides explicit values and they align with the expected patterns for random conditions, I'll incorporate them into the final JSON structure. I'm pulling the hacking taxonomy breakdowns from the evidence table for both ISR and random across the different samples, then I'll compile everything into the final JSON output.

Now I'm verifying the proved_only_isr calculation for s44 — the registry shows eval_mean_isr at 0.803, and when I work through the math (mean_isr × total_samples / proved_samples), it checks out to 0.9022, which matches the expected value.

Looking at prolog STA s42, the metrics align: with 50 problems proved out of 100 and an average ISR of 0.5 across all problems, the proved_only_isr of 1.0 makes sense since all proved instances have perfect ISR. The evidence table confirms a single component for this seed, and I'm noticing the exec-only seeds show ground fact enumeration metrics.

Now I'm pulling together the final JSON structure, organizing the hacking taxonomy by condition and seed with h7/h1/genuine counts and rates. For convex_random, the evidence table shows 100% H7 but notes this is a special case of tautological collapse rather than standard H7. For exec_only_1000, the evidence table doesn't provide h7/h1/genuine breakdowns, though the registry shows 96 problems proved with an average of 18.55 components, suggesting a contradiction explosion hacking mode.

Generating the JSON structure... Finishing the variance calculation for the ISR values, I get a standard deviation of about 0.30, which confirms the "0.23±0.30" result. Now I'm moving on to check the isr_b01 metrics with a new set of precision values. Finishing the variance calculation for the ISR values, I get a standard deviation of about 0.24, which confirms the "0.55±0.24" result. Now I'm moving on to check the random_b01 dataset with its own precision and ISR metrics across the three samples. Now I'm calculating the mean and standard deviation for the precision and ISR metrics in the prolog_exec_only case, working through the variance calculations to get the uncertainty estimates. So the registry doesn't explicitly list h7_rate for s42, but the evidence table shows 13 out of 81 cases, which gives me 0.1605—rounding to 0.16 as stated. With s43 at 0.967 and s44 at 0.865, the mean comes to 0.6642, matching the expected 0.664.

For the genuine_mean calculation across ISR, I'm getting (0.321+0.033+0.135)/3 = 0.163. Now I need to construct the complete JSON output with consistent precision—PR values at 2 decimals, ISR metrics at 3 decimals, and the mean±std strings formatted to match the evidence table.

Generating JSON output... Now I'm verifying the rates for the remaining random seeds—s43 shows 93.2% H1 and 6.8% genuine across 88 total cases. For the exec_only_1000 dataset, there's no hacking taxonomy data available, just the registry info showing 96 proved cases with a mean of 18.55 components in contradiction explosion mode. Time to construct the JSON output with all these values.

Writing JSON output... I need to structure the table2 section to organize the hacking taxonomy data—H7, H1, and genuine distributions—broken down by condition and seed. For the `proved_only_isr` value in exec_only_1000, I'm using 0.003 based on the registry's 0.0028 rounded to three significant figures. Now I'm ready to construct the complete JSON output. There's a discrepancy between the registry (which shows h7_count=97 and h7_rate=1.0) and the eval_results.json (which reports 97 proved samples). The evidence table uses 97/97=100%, matching the eval_results.json, but the registry has a different n_proved value of 98. I'll stick with the registry's h7_rate=1.0, which implies the denominator is 97, not 98. I've spent enough time on this discrepancy—let me just generate the JSON file now. I'm calculating the ISR b01 genuine_mean by averaging the genuine rates across s42, s43, and s44, which gives me 0.163, matching what the task description specifies. Time to write the output.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eb5b7954-c1fd-473d-8da7-d1389c3f22e7",
  "uuid": "af49b978-e6cb-4e6a-8cba-3e8d80130de9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UrKKnBdeJyX8i9pHGcVjsL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8019,
      "cache_read_input_tokens": 32109,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8019
      },
      "output_tokens": 8,
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

_source line 44_

Got the evidence table and registry data. Now let me construct the JSON with precise values from both sources.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eb5b7954-c1fd-473d-8da7-d1389c3f22e7",
  "uuid": "4da556be-434f-4dfc-820a-cb9b4f582ea4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UrKKnBdeJyX8i9pHGcVjsL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8019,
      "cache_read_input_tokens": 32109,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8019
      },
      "output_tokens": 8,
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

_source line 45_

<details open><summary>🔧 Tool call — Write · `toolu_01Kc13wpPXMYBmtnD4eDPXkg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/table_data.json",
  "content": "{\n  \"metadata\": {\n    \"generated\": \"2026-05-14\",\n    \"source\": \"registry (read_registry) + eval_sta.py (evidence_tables_d051.md)\",\n    \"eval_method\": \"All eval metrics from eval_sta.py (full STA) unless noted\",\n    \"std_type\": \"sample std (ddof=1) for all mean±std\"\n  },\n  \"table1_goodhart_landscape\": {\n    \"base_model\": {\n      \"exp_id\": \"sta-phase0-baseline\",\n      \"pr\": 0.12,\n      \"isr\": 0.064,\n      \"isr_std\": 0.198,\n      \"notes\": \"phase0 baseline, n=100\"\n    },\n    \"sft_baseline\": {\n      \"exp_id\": \"plan009-sft-baseline-s42-r4\",\n      \"seeds\": [\"s42\"],\n      \"pr\": 0.14,\n      \"isr\": 0.080,\n      \"isr_std\": 0.214,\n      \"proved_only_isr\": 0.571,\n      \"n_proved\": 14,\n      \"h7_rate\": 0,\n      \"h7_count\": 0,\n      \"h1_rate\": 0.071,\n      \"h1_count\": 1,\n      \"genuine_rate\": 0.929,\n      \"genuine_count\": 13\n    },\n    \"exec_only_500\": {\n      \"seeds\": {\n        \"s42\": {\n          \"exp_id\": \"plan001-exec-only-s42-r2\",\n          \"pr\": 0.93,\n          \"isr\": 0.123,\n          \"isr_std\": 0.189,\n          \"proved_only_isr\": 0.132,\n          \"components\": 6.58,\n          \"n_proved\": 93,\n          \"h7_rate\": 0,\n          \"h7_count\": 0,\n          \"h1_rate\": 0.871,\n          \"h1_count\": 81,\n          \"genuine_rate\": 0.129,\n          \"genuine_count\": 12,\n          \"hacking_mode\": \"H1 conclusion embedding (87.1%)\"\n        },\n        \"s43\": {\n          \"exp_id\": \"plan001-exec-only-s43-r4\",\n          \"pr\": 0.14,\n          \"isr\": 0,\n          \"n_proved\": 14,\n          \"notes\": \"repetition collapse, do_sample=True eval (temperature=0.7), not comparable (C004)\"\n        },\n        \"s44\": {\n          \"exp_id\": \"plan001-exec-only-s44\",\n          \"pr\": 0.98,\n          \"isr\": 0.570,\n          \"isr_std\": 0.201,\n          \"proved_only_isr\": 0.582,\n          \"components\": 2.04,\n          \"n_proved\": 97,\n          \"h7_rate\": 1.0,\n          \"h7_count\": 97,\n          \"h1_rate\": 0,\n          \"h1_count\": 0,\n          \"genuine_rate\": 0,\n          \"genuine_count\": 0,\n          \"tautological_collapse\": true,\n          \"hacking_mode\": \"tautological collapse (H7=100%)\"\n        }\n      },\n      \"mean_std\": {\n        \"pr\": \"0.68±0.47\",\n        \"isr\": \"0.23±0.30\",\n        \"notes\": \"3-seed, extreme seed variance (s43 used do_sample=True)\"\n      }\n    },\n    \"exec_only_1000\": {\n      \"exp_id\": \"plan016-extended-1000-s42\",\n      \"seeds\": [\"s42\"],\n      \"pr\": 0.96,\n      \"isr\": 0.003,\n      \"isr_std\": 0.012,\n      \"proved_only_isr\": 0.003,\n      \"components\": 18.55,\n      \"n_proved\": 96,\n      \"hacking_mode\": \"contradiction explosion\"\n    },\n    \"isr_b01\": {\n      \"seeds\": {\n        \"s42\": {\n          \"exp_id\": \"plan002-additive-b01-s42\",\n          \"pr\": 0.81,\n          \"isr\": 0.337,\n          \"isr_std\": 0.323,\n          \"proved_only_isr\": 0.415,\n          \"components\": 5.58,\n          \"n_proved\": 81,\n          \"h7_rate\": 0.160,\n          \"h7_count\": 13,\n          \"h1_rate\": 0.519,\n          \"h1_count\": 42,\n          \"genuine_rate\": 0.321,\n          \"genuine_count\": 26\n        },\n        \"s43\": {\n          \"exp_id\": \"plan002-additive-b01-s43\",\n          \"pr\": 0.61,\n          \"isr\": 0.506,\n          \"isr_std\": 0.452,\n          \"proved_only_isr\": 0.830,\n          \"components\": 4.03,\n          \"n_proved\": 61,\n          \"h7_rate\": 0.967,\n          \"h7_count\": 59,\n          \"h1_rate\": 0,\n          \"h1_count\": 0,\n          \"genuine_rate\": 0.033,\n          \"genuine_count\": 2,\n          \"hacking_mode\": \"conclusion_duplication_isr_inflation\"\n        },\n        \"s44\": {\n          \"exp_id\": \"plan002-additive-b01-s44\",\n          \"pr\": 0.89,\n          \"isr\": 0.803,\n          \"isr_std\": 0.342,\n          \"proved_only_isr\": 0.902,\n          \"components\": 4.33,\n          \"n_proved\": 89,\n          \"h7_rate\": 0.865,\n          \"h7_count\": 77,\n          \"h1_rate\": 0,\n          \"h1_count\": 0,\n          \"genuine_rate\": 0.135,\n          \"genuine_count\": 12,\n          \"hacking_mode\": \"conclusion_duplication_isr_inflation\"\n        }\n      },\n      \"mean_std\": {\n        \"pr\": \"0.77±0.14\",\n        \"isr\": \"0.55±0.24\",\n        \"proved_only_isr\": \"0.716±0.26\",\n        \"components_mean\": 4.65,\n        \"h7_rate_mean\": 0.664,\n        \"genuine_rate_mean\": 0.163\n      }\n    },\n    \"random_b01\": {\n      \"seeds\": {\n        \"s42\": {\n          \"exp_id\": \"plan018-additive-random-b01-s42\",\n          \"pr\": 0.79,\n          \"isr\": 0.104,\n          \"isr_std\": 0.137,\n          \"proved_only_isr\": 0.131,\n          \"components\": 8.46,\n          \"n_proved\": 79,\n          \"h7_rate\": 0,\n          \"h7_count\": 0,\n          \"h1_rate\": 0.709,\n          \"h1_count\": 56,\n          \"genuine_rate\": 0.291,\n          \"genuine_count\": 23\n        },\n        \"s43\": {\n          \"exp_id\": \"plan018-additive-random-b01-s43-r2\",\n          \"pr\": 0.88,\n          \"isr\": 0.051,\n          \"proved_only_isr\": 0.058,\n          \"n_proved\": 88,\n          \"h7_rate\": 0,\n          \"h7_count\": 0,\n          \"h1_rate\": 0.932,\n          \"h1_count\": 82,\n          \"genuine_rate\": 0.068,\n          \"genuine_count\": 6,\n          \"notes\": \"isr/proved_only_isr from eval_sta.py (not in registry)\"\n        },\n        \"s44\": {\n          \"exp_id\": \"plan018-additive-random-b01-s44\",\n          \"pr\": 0.89,\n          \"isr\": 0.062,\n          \"isr_std\": 0.176,\n          \"proved_only_isr\": 0.070,\n          \"n_proved\": 89,\n          \"h7_rate\": 0,\n          \"h7_count\": 0,\n          \"h1_rate\": 0.798,\n          \"h1_count\": 71,\n          \"genuine_rate\": 0.202,\n          \"genuine_count\": 18\n        }\n      },\n      \"mean_std\": {\n        \"pr\": \"0.85±0.06\",\n        \"isr\": \"0.07±0.03\",\n        \"h1_rate_mean\": 0.813,\n        \"genuine_rate_mean\": 0.187\n      }\n    },\n    \"isr_b03\": {\n      \"exp_id\": \"plan002-additive-b03-s42\",\n      \"seeds\": [\"s42\"],\n      \"pr\": 0.18,\n      \"isr\": 0.026,\n      \"isr_std\": 0.074,\n      \"proved_only_isr\": 0.143,\n      \"hacking_mode\": \"format collapse (classic Goodhart)\",\n      \"notes\": \"eval metrics from evidence_tables_d051 (registry has training metrics only)\"\n    },\n    \"random_b03\": {\n      \"exp_id\": \"plan017-additive-random-s42\",\n      \"seeds\": [\"s42\"],\n      \"pr\": 0.48,\n      \"isr\": 0.045,\n      \"isr_std\": 0.076,\n      \"proved_only_isr\": 0.094,\n      \"components\": 9.60,\n      \"n_proved\": 48,\n      \"hacking_mode\": \"complexity-without-utility\"\n    },\n    \"convex_random\": {\n      \"exp_id\": \"plan013-random-reward-s42-r4\",\n      \"seeds\": [\"s42\"],\n      \"pr\": 1.00,\n      \"isr\": 0.535,\n      \"isr_std\": 0.128,\n      \"proved_only_isr\": 0.535,\n      \"components\": 2.0,\n      \"n_proved\": 100,\n      \"hacking_mode\": \"P→P tautological (H7=100%)\"\n    }\n  },\n  \"table2_hacking_taxonomy\": {\n    \"description\": \"H7/H1/Genuine distribution per condition per seed. H7=premise identical to conclusion (ISR-inflating). H1=conclusion embedded among multi-step premises (GRPO-universal). Genuine=no conclusion duplication detected.\",\n    \"conditions\": {\n      \"sft_baseline\": {\n        \"s42\": { \"h7_pct\": 0, \"h7_count\": 0, \"h1_pct\": 7.1, \"h1_count\": 1, \"genuine_pct\": 92.9, \"genuine_count\": 13, \"n_proved\": 14 }\n      },\n      \"exec_only_500\": {\n        \"s42\": { \"h7_pct\": 0, \"h7_count\": 0, \"h1_pct\": 87.1, \"h1_count\": 81, \"genuine_pct\": 12.9, \"genuine_count\": 12, \"n_proved\": 93 },\n        \"s44\": { \"h7_pct\": 100, \"h7_count\": 97, \"h1_pct\": 0, \"h1_count\": 0, \"genuine_pct\": 0, \"genuine_count\": 0, \"n_proved\": 97, \"notes\": \"tautological collapse\" }\n      },\n      \"isr_b01\": {\n        \"s42\": { \"h7_pct\": 16.0, \"h7_count\": 13, \"h1_pct\": 51.9, \"h1_count\": 42, \"genuine_pct\": 32.1, \"genuine_count\": 26, \"n_proved\": 81 },\n        \"s43\": { \"h7_pct\": 96.7, \"h7_count\": 59, \"h1_pct\": 0, \"h1_count\": 0, \"genuine_pct\": 3.3, \"genuine_count\": 2, \"n_proved\": 61 },\n        \"s44\": { \"h7_pct\": 86.5, \"h7_count\": 77, \"h1_pct\": 0, \"h1_count\": 0, \"genuine_pct\": 13.5, \"genuine_count\": 12, \"n_proved\": 89 }\n      },\n      \"random_b01\": {\n        \"s42\": { \"h7_pct\": 0, \"h7_count\": 0, \"h1_pct\": 70.9, \"h1_count\": 56, \"genuine_pct\": 29.1, \"genuine_count\": 23, \"n_proved\": 79 },\n        \"s43\": { \"h7_pct\": 0, \"h7_count\": 0, \"h1_pct\": 93.2, \"h1_count\": 82, \"genuine_pct\": 6.8, \"genuine_count\": 6, \"n_proved\": 88 },\n        \"s44\": { \"h7_pct\": 0, \"h7_count\": 0, \"h1_pct\": 79.8, \"h1_count\": 71, \"genuine_pct\": 20.2, \"genuine_count\": 18, \"n_proved\": 89 }\n      },\n      \"convex_random\": {\n        \"s42\": { \"h7_pct\": 100, \"h7_count\": 100, \"h1_pct\": 0, \"h1_count\": 0, \"genuine_pct\": 0, \"genuine_count\": 0, \"n_proved\": 100, \"notes\": \"P→P tautological, classified separately from multi-step H7\" }\n      }\n    },\n    \"key_findings\": {\n      \"h7_is_isr_specific\": \"ISR 3-seed H7 mean = 66.4% (149/231), Random H7 = 0% across all seeds\",\n      \"h1_is_grpo_universal\": \"Random H1 = 71-93%, ISR s42 H1 = 52%. Conclusion embedding is general GRPO strategy\",\n      \"isr_changes_composition_not_total\": \"Overall hacking rate comparable (ISR s42 67.9% vs Random s42 70.9%), but ISR converts H1 → H7\",\n      \"sft_near_zero_hacking\": \"1/14 H1, 0 H7, 92.9% genuine — hacking is RL-specific\"\n    }\n  },\n  \"claim2_isr_vs_random\": {\n    \"premise_count_matched\": {\n      \"isr_genuine_isr\": 0.2578,\n      \"random_genuine_isr\": 0.2434,\n      \"ratio\": 1.06,\n      \"notes\": \"n_prem >= 3 only, strict normalization. Source: plan012-hacking-taxonomy analysis\"\n    },\n    \"isr_3seed\": {\n      \"pr\": \"0.77±0.14\",\n      \"isr\": \"0.55±0.24\",\n      \"h7_mean\": 0.664,\n      \"h1_mean\": 0.173,\n      \"genuine_mean\": 0.163\n    },\n    \"random_3seed\": {\n      \"pr\": \"0.85±0.06\",\n      \"isr\": \"0.07±0.03\",\n      \"h7_mean\": 0,\n      \"h1_mean\": 0.813,\n      \"genuine_mean\": 0.187\n    }\n  },\n  \"prolog_exec_only_3seed\": {\n    \"seeds\": {\n      \"s42\": {\n        \"exp_id\": \"plan006-prolog-exec-s42\",\n        \"pr\": 0.83,\n        \"isr\": 0.031,\n        \"isr_std\": 0.053,\n        \"proved_only_isr\": 0.037,\n        \"n_proved\": 83,\n        \"h7_rate\": 0,\n        \"h1_rate\": 0\n      },\n      \"s43\": {\n        \"exp_id\": \"plan006-prolog-exec-s43-r3\",\n        \"pr\": 0.56,\n        \"isr\": 0.008,\n        \"isr_std\": 0.022,\n        \"proved_only_isr\": 0.015,\n        \"n_proved\": 56\n      },\n      \"s44\": {\n        \"exp_id\": \"plan006-prolog-exec-s44\",\n        \"pr\": 0.21,\n        \"isr\": 0.081,\n        \"isr_std\": 0.234,\n        \"proved_only_isr\": 0.387,\n        \"n_proved\": 21,\n        \"notes\": \"lowest PR, highest proved_only_isr — small sample artifact\"\n      }\n    },\n    \"mean_std\": {\n      \"pr\": \"0.53±0.31\",\n      \"isr\": \"0.040±0.037\",\n      \"proved_only_isr\": \"0.146±0.210\"\n    }\n  },\n  \"prolog_sta\": {\n    \"s42\": {\n      \"exp_id\": \"plan006-prolog-sta-s42\",\n      \"pr\": 0.50,\n      \"isr\": 0.500,\n      \"proved_only_isr\": 1.0,\n      \"components\": 1.0,\n      \"n_proved\": 50,\n      \"h7_rate\": 1.0,\n      \"h7_count\": 50,\n      \"hacking_mode\": \"100% H7 (single clause = query)\"\n    },\n    \"s43\": \"RUNNING\",\n    \"s44\": \"RUNNING\"\n  },\n  \"isr_collapse_trajectory\": {\n    \"description\": \"ISR diagnostic trajectory for exec-only s42 across training steps\",\n    \"steps_100\": { \"pr\": 0.32, \"isr\": 0.642, \"exp_id\": \"plan003-eval-exec-only-r5\", \"notes\": \"eval at 100 steps\" },\n    \"steps_500\": { \"pr\": 0.93, \"isr\": 0.123, \"exp_id\": \"plan001-exec-only-s42-r2\" },\n    \"steps_1000\": { \"pr\": 0.96, \"isr\": 0.003, \"exp_id\": \"plan016-extended-1000-s42\" }\n  }\n}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eb5b7954-c1fd-473d-8da7-d1389c3f22e7",
  "uuid": "7998b969-0584-4e95-b202-9f9001191c83",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UrKKnBdeJyX8i9pHGcVjsL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8019,
      "cache_read_input_tokens": 32109,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8019
      },
      "output_tokens": 8,
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

### Runtime record

_source line 46_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed",
    "resetsAt": 1778782200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "ee33818d-e425-4f7a-bad9-d637be44f5f6",
  "session_id": "eb5b7954-c1fd-473d-8da7-d1389c3f22e7"
}
```

---

### Tool result

_source line 47 · 2026-05-14T17:31:19.249Z_

<details><summary>↩ Tool result · `toolu_01Kc13wpPXMYBmtnD4eDPXkg`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/table_data.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "eb5b7954-c1fd-473d-8da7-d1389c3f22e7",
  "uuid": "5339dd96-8be6-4029-9ee5-c139fda5937e",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/table_data.json",
    "content": "{\n  \"metadata\": {\n    \"generated\": \"2026-05-14\",\n    \"source\": \"registry (read_registry) + eval_sta.py (evidence_tables_d051.md)\",\n    \"eval_method\": \"All eval metrics from eval_sta.py (full STA) unless noted\",\n    \"std_type\": \"sample std (ddof=1) for all mean±std\"\n  },\n  \"table1_goodhart_landscape\": {\n    \"base_model\": {\n      \"exp_id\": \"sta-phase0-baseline\",\n      \"pr\": 0.12,\n      \"isr\": 0.064,\n      \"isr_std\": 0.198,\n      \"notes\": \"phase0 baseline, n=100\"\n    },\n    \"sft_baseline\": {\n      \"exp_id\": \"plan009-sft-baseline-s42-r4\",\n      \"seeds\": [\"s42\"],\n      \"pr\": 0.14,\n      \"isr\": 0.080,\n      \"isr_std\": 0.214,\n      \"proved_only_isr\": 0.571,\n      \"n_proved\": 14,\n      \"h7_rate\": 0,\n      \"h7_count\": 0,\n      \"h1_rate\": 0.071,\n      \"h1_count\": 1,\n      \"genuine_rate\": 0.929,\n      \"genuine_count\": 13\n    },\n    \"exec_only_500\": {\n      \"seeds\": {\n        \"s42\": {\n          \"exp_id\": \"plan001-exec-only-s42-r2\",\n          \"pr\": 0.93,\n          \"isr\": 0.123,\n          \"isr_std\": 0.189,\n          \"proved_only_isr\": 0.132,\n          \"components\": 6.58,\n          \"n_proved\": 93,\n          \"h7_rate\": 0,\n          \"h7_count\": 0,\n          \"h1_rate\": 0.871,\n          \"h1_count\": 81,\n          \"genuine_rate\": 0.129,\n          \"genuine_count\": 12,\n          \"hacking_mode\": \"H1 conclusion embedding (87.1%)\"\n        },\n        \"s43\": {\n          \"exp_id\": \"plan001-exec-only-s43-r4\",\n          \"pr\": 0.14,\n          \"isr\": 0,\n          \"n_proved\": 14,\n          \"notes\": \"repetition collapse, do_sample=True eval (temperature=0.7), not comparable (C004)\"\n        },\n        \"s44\": {\n          \"exp_id\": \"plan001-exec-only-s44\",\n          \"pr\": 0.98,\n          \"isr\": 0.570,\n          \"isr_std\": 0.201,\n          \"proved_only_isr\": 0.582,\n          \"components\": 2.04,\n          \"n_proved\": 97,\n          \"h7_rate\": 1.0,\n          \"h7_count\": 97,\n          \"h1_rate\": 0,\n          \"h1_count\": 0,\n          \"genuine_rate\": 0,\n          \"genuine_count\": 0,\n          \"tautological_collapse\": true,\n          \"hacking_mode\": \"tautological collapse (H7=100%)\"\n        }\n      },\n      \"mean_std\": {\n        \"pr\": \"0.68±0.47\",\n        \"isr\": \"0.23±0.30\",\n        \"notes\": \"3-seed, extreme seed variance (s43 used do_sample=True)\"\n      }\n    },\n    \"exec_only_1000\": {\n      \"exp_id\": \"plan016-extended-1000-s42\",\n      \"seeds\": [\"s42\"],\n      \"pr\": 0.96,\n      \"isr\": 0.003,\n      \"isr_std\": 0.012,\n      \"proved_only_isr\": 0.003,\n      \"components\": 18.55,\n      \"n_proved\": 96,\n      \"hacking_mode\": \"contradiction explosion\"\n    },\n    \"isr_b01\": {\n      \"seeds\": {\n        \"s42\": {\n          \"exp_id\": \"plan002-additive-b01-s42\",\n          \"pr\": 0.81,\n          \"isr\": 0.337,\n          \"isr_std\": 0.323,\n          \"proved_only_isr\": 0.415,\n          \"components\": 5.58,\n          \"n_proved\": 81,\n          \"h7_rate\": 0.160,\n          \"h7_count\": 13,\n          \"h1_rate\": 0.519,\n          \"h1_count\": 42,\n          \"genuine_rate\": 0.321,\n          \"genuine_count\": 26\n        },\n        \"s43\": {\n          \"exp_id\": \"plan002-additive-b01-s43\",\n          \"pr\": 0.61,\n          \"isr\": 0.506,\n          \"isr_std\": 0.452,\n          \"proved_only_isr\": 0.830,\n          \"components\": 4.03,\n          \"n_proved\": 61,\n          \"h7_rate\": 0.967,\n          \"h7_count\": 59,\n          \"h1_rate\": 0,\n          \"h1_count\": 0,\n          \"genuine_rate\": 0.033,\n          \"genuine_count\": 2,\n          \"hacking_mode\": \"conclusion_duplication_isr_inflation\"\n        },\n        \"s44\": {\n          \"exp_id\": \"plan002-additive-b01-s44\",\n          \"pr\": 0.89,\n          \"isr\": 0.803,\n          \"isr_std\": 0.342,\n          \"proved_only_isr\": 0.902,\n          \"components\": 4.33,\n          \"n_proved\": 89,\n          \"h7_rate\": 0.865,\n          \"h7_count\": 77,\n          \"h1_rate\": 0,\n          \"h1_count\": 0,\n          \"genuine_rate\": 0.135,\n          \"genuine_count\": 12,\n          \"hacking_mode\": \"conclusion_duplication_isr_inflation\"\n        }\n      },\n      \"mean_std\": {\n        \"pr\": \"0.77±0.14\",\n        \"isr\": \"0.55±0.24\",\n        \"proved_only_isr\": \"0.716±0.26\",\n        \"components_mean\": 4.65,\n        \"h7_rate_mean\": 0.664,\n        \"genuine_rate_mean\": 0.163\n      }\n    },\n    \"random_b01\": {\n      \"seeds\": {\n        \"s42\": {\n          \"exp_id\": \"plan018-additive-random-b01-s42\",\n          \"pr\": 0.79,\n          \"isr\": 0.104,\n          \"isr_std\": 0.137,\n          \"proved_only_isr\": 0.131,\n          \"components\": 8.46,\n          \"n_proved\": 79,\n          \"h7_rate\": 0,\n          \"h7_count\": 0,\n          \"h1_rate\": 0.709,\n          \"h1_count\": 56,\n          \"genuine_rate\": 0.291,\n          \"genuine_count\": 23\n        },\n        \"s43\": {\n          \"exp_id\": \"plan018-additive-random-b01-s43-r2\",\n          \"pr\": 0.88,\n          \"isr\": 0.051,\n          \"proved_only_isr\": 0.058,\n          \"n_proved\": 88,\n          \"h7_rate\": 0,\n          \"h7_count\": 0,\n          \"h1_rate\": 0.932,\n          \"h1_count\": 82,\n          \"genuine_rate\": 0.068,\n          \"genuine_count\": 6,\n          \"notes\": \"isr/proved_only_isr from eval_sta.py (not in registry)\"\n        },\n        \"s44\": {\n          \"exp_id\": \"plan018-additive-random-b01-s44\",\n          \"pr\": 0.89,\n          \"isr\": 0.062,\n          \"isr_std\": 0.176,\n          \"proved_only_isr\": 0.070,\n          \"n_proved\": 89,\n          \"h7_rate\": 0,\n          \"h7_count\": 0,\n          \"h1_rate\": 0.798,\n          \"h1_count\": 71,\n          \"genuine_rate\": 0.202,\n          \"genuine_count\": 18\n        }\n      },\n      \"mean_std\": {\n        \"pr\": \"0.85±0.06\",\n        \"isr\": \"0.07±0.03\",\n        \"h1_rate_mean\": 0.813,\n        \"genuine_rate_mean\": 0.187\n      }\n    },\n    \"isr_b03\": {\n      \"exp_id\": \"plan002-additive-b03-s42\",\n      \"seeds\": [\"s42\"],\n      \"pr\": 0.18,\n      \"isr\": 0.026,\n      \"isr_std\": 0.074,\n      \"proved_only_isr\": 0.143,\n      \"hacking_mode\": \"format collapse (classic Goodhart)\",\n      \"notes\": \"eval metrics from evidence_tables_d051 (registry has training metrics only)\"\n    },\n    \"random_b03\": {\n      \"exp_id\": \"plan017-additive-random-s42\",\n      \"seeds\": [\"s42\"],\n      \"pr\": 0.48,\n      \"isr\": 0.045,\n      \"isr_std\": 0.076,\n      \"proved_only_isr\": 0.094,\n      \"components\": 9.60,\n      \"n_proved\": 48,\n      \"hacking_mode\": \"complexity-without-utility\"\n    },\n    \"convex_random\": {\n      \"exp_id\": \"plan013-random-reward-s42-r4\",\n      \"seeds\": [\"s42\"],\n      \"pr\": 1.00,\n      \"isr\": 0.535,\n      \"isr_std\": 0.128,\n      \"proved_only_isr\": 0.535,\n      \"components\": 2.0,\n      \"n_proved\": 100,\n      \"hacking_mode\": \"P→P tautological (H7=100%)\"\n    }\n  },\n  \"table2_hacking_taxonomy\": {\n    \"description\": \"H7/H1/Genuine distribution per condition per seed. H7=premise identical to conclusion (ISR-inflating). H1=conclusion embedded among multi-step premises (GRPO-universal). Genuine=no conclusion duplication detected.\",\n    \"conditions\": {\n      \"sft_baseline\": {\n        \"s42\": { \"h7_pct\": 0, \"h7_count\": 0, \"h1_pct\": 7.1, \"h1_count\": 1, \"genuine_pct\": 92.9, \"genuine_count\": 13, \"n_proved\": 14 }\n      },\n      \"exec_only_500\": {\n        \"s42\": { \"h7_pct\": 0, \"h7_count\": 0, \"h1_pct\": 87.1, \"h1_count\": 81, \"genuine_pct\": 12.9, \"genuine_count\": 12, \"n_proved\": 93 },\n        \"s44\": { \"h7_pct\": 100, \"h7_count\": 97, \"h1_pct\": 0, \"h1_count\": 0, \"genuine_pct\": 0, \"genuine_count\": 0, \"n_proved\": 97, \"notes\": \"tautological collapse\" }\n      },\n      \"isr_b01\": {\n        \"s42\": { \"h7_pct\": 16.0, \"h7_count\": 13, \"h1_pct\": 51.9, \"h1_count\": 42, \"genuine_pct\": 32.1, \"genuine_count\": 26, \"n_proved\": 81 },\n        \"s43\": { \"h7_pct\": 96.7, \"h7_count\": 59, \"h1_pct\": 0, \"h1_count\": 0, \"genuine_pct\": 3.3, \"genuine_count\": 2, \"n_proved\": 61 },\n        \"s44\": { \"h7_pct\": 86.5, \"h7_count\": 77, \"h1_pct\": 0, \"h1_count\": 0, \"genuine_pct\": 13.5, \"genuine_count\": 12, \"n_proved\": 89 }\n      },\n      \"random_b01\": {\n        \"s42\": { \"h7_pct\": 0, \"h7_count\": 0, \"h1_pct\": 70.9, \"h1_count\": 56, \"genuine_pct\": 29.1, \"genuine_count\": 23, \"n_proved\": 79 },\n        \"s43\": { \"h7_pct\": 0, \"h7_count\": 0, \"h1_pct\": 93.2, \"h1_count\": 82, \"genuine_pct\": 6.8, \"genuine_count\": 6, \"n_proved\": 88 },\n        \"s44\": { \"h7_pct\": 0, \"h7_count\": 0, \"h1_pct\": 79.8, \"h1_count\": 71, \"genuine_pct\": 20.2, \"genuine_count\": 18, \"n_proved\": 89 }\n      },\n      \"convex_random\": {\n        \"s42\": { \"h7_pct\": 100, \"h7_count\": 100, \"h1_pct\": 0, \"h1_count\": 0, \"genuine_pct\": 0, \"genuine_count\": 0, \"n_proved\": 100, \"notes\": \"P→P tautological, classified separately from multi-step H7\" }\n      }\n    },\n    \"key_findings\": {\n      \"h7_is_isr_specific\": \"ISR 3-seed H7 mean = 66.4% (149/231), Random H7 = 0% across all seeds\",\n      \"h1_is_grpo_universal\": \"Random H1 = 71-93%, ISR s42 H1 = 52%. Conclusion embedding is general GRPO strategy\",\n      \"isr_changes_composition_not_total\": \"Overall hacking rate comparable (ISR s42 67.9% vs Random s42 70.9%), but ISR converts H1 → H7\",\n      \"sft_near_zero_hacking\": \"1/14 H1, 0 H7, 92.9% genuine — hacking is RL-specific\"\n    }\n  },\n  \"claim2_isr_vs_random\": {\n    \"premise_count_matched\": {\n      \"isr_genuine_isr\": 0.2578,\n      \"random_genuine_isr\": 0.2434,\n      \"ratio\": 1.06,\n      \"notes\": \"n_prem >= 3 only, strict normalization. Source: plan012-hacking-taxonomy analysis\"\n    },\n    \"isr_3seed\": {\n      \"pr\": \"0.77±0.14\",\n      \"isr\": \"0.55±0.24\",\n      \"h7_mean\": 0.664,\n      \"h1_mean\": 0.173,\n      \"genuine_mean\": 0.163\n    },\n    \"random_3seed\": {\n      \"pr\": \"0.85±0.06\",\n      \"isr\": \"0.07±0.03\",\n      \"h7_mean\": 0,\n      \"h1_mean\": 0.813,\n      \"genuine_mean\": 0.187\n    }\n  },\n  \"prolog_exec_only_3seed\": {\n    \"seeds\": {\n      \"s42\": {\n        \"exp_id\": \"plan006-prolog-exec-s42\",\n        \"pr\": 0.83,\n        \"isr\": 0.031,\n        \"isr_std\": 0.053,\n        \"proved_only_isr\": 0.037,\n        \"n_proved\": 83,\n        \"h7_rate\": 0,\n        \"h1_rate\": 0\n      },\n      \"s43\": {\n        \"exp_id\": \"plan006-prolog-exec-s43-r3\",\n        \"pr\": 0.56,\n        \"isr\": 0.008,\n        \"isr_std\": 0.022,\n        \"proved_only_isr\": 0.015,\n        \"n_proved\": 56\n      },\n      \"s44\": {\n        \"exp_id\": \"plan006-prolog-exec-s44\",\n        \"pr\": 0.21,\n        \"isr\": 0.081,\n        \"isr_std\": 0.234,\n        \"proved_only_isr\": 0.387,\n        \"n_proved\": 21,\n        \"notes\": \"lowest PR, highest proved_only_isr — small sample artifact\"\n      }\n    },\n    \"mean_std\": {\n      \"pr\": \"0.53±0.31\",\n      \"isr\": \"0.040±0.037\",\n      \"proved_only_isr\": \"0.146±0.210\"\n    }\n  },\n  \"prolog_sta\": {\n    \"s42\": {\n      \"exp_id\": \"plan006-prolog-sta-s42\",\n      \"pr\": 0.50,\n      \"isr\": 0.500,\n      \"proved_only_isr\": 1.0,\n      \"components\": 1.0,\n      \"n_proved\": 50,\n      \"h7_rate\": 1.0,\n      \"h7_count\": 50,\n      \"hacking_mode\": \"100% H7 (single clause = query)\"\n    },\n    \"s43\": \"RUNNING\",\n    \"s44\": \"RUNNING\"\n  },\n  \"isr_collapse_trajectory\": {\n    \"description\": \"ISR diagnostic trajectory for exec-only s42 across training steps\",\n    \"steps_100\": { \"pr\": 0.32, \"isr\": 0.642, \"exp_id\": \"plan003-eval-exec-only-r5\", \"notes\": \"eval at 100 steps\" },\n    \"steps_500\": { \"pr\": 0.93, \"isr\": 0.123, \"exp_id\": \"plan001-exec-only-s42-r2\" },\n    \"steps_1000\": { \"pr\": 0.96, \"isr\": 0.003, \"exp_id\": \"plan016-extended-1000-s42\" }\n  }\n}\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 48_

<details><summary>Logged reasoning block</summary>

```text
Now let me verify the JSON is valid and register the artifact.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eb5b7954-c1fd-473d-8da7-d1389c3f22e7",
  "uuid": "b277d493-2ca1-4763-b1bc-5c7b726d07dc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011PKPbsdb97mrzvsi7m3ift",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19490,
      "cache_read_input_tokens": 40128,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 19490
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

_source line 49_

<details open><summary>🔧 Tool call — Bash · `toolu_012JZQ1BbgTVLAv2fibebboH`</summary>

```json
{
  "command": "python3 -c \"import json; d=json.load(open('/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/table_data.json')); print('Valid JSON'); print(f'Top-level keys: {list(d.keys())}'); print(f'Table1 conditions: {list(d[\\\"table1_goodhart_landscape\\\"].keys())}'); print(f'Table2 conditions: {list(d[\\\"table2_hacking_taxonomy\\\"][\\\"conditions\\\"].keys())}'); print(f'Prolog exec seeds: {list(d[\\\"prolog_exec_only_3seed\\\"][\\\"seeds\\\"].keys())}'); print(f'Prolog STA seeds: {[k for k in d[\\\"prolog_sta\\\"].keys()]}')\"",
  "description": "Validate JSON structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eb5b7954-c1fd-473d-8da7-d1389c3f22e7",
  "uuid": "bd758c67-c1c1-4827-9a7c-62ab632a9dce",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011PKPbsdb97mrzvsi7m3ift",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19490,
      "cache_read_input_tokens": 40128,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 19490
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

### Tool result

_source line 50 · 2026-05-14T17:31:30.752Z_

<details><summary>↩ Tool result · `toolu_012JZQ1BbgTVLAv2fibebboH`</summary>

```text
Valid JSON
Top-level keys: ['metadata', 'table1_goodhart_landscape', 'table2_hacking_taxonomy', 'claim2_isr_vs_random', 'prolog_exec_only_3seed', 'prolog_sta', 'isr_collapse_trajectory']
Table1 conditions: ['base_model', 'sft_baseline', 'exec_only_500', 'exec_only_1000', 'isr_b01', 'random_b01', 'isr_b03', 'random_b03', 'convex_random']
Table2 conditions: ['sft_baseline', 'exec_only_500', 'isr_b01', 'random_b01', 'convex_random']
Prolog exec seeds: ['s42', 's43', 's44']
Prolog STA seeds: ['s42', 's43', 's44']
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "eb5b7954-c1fd-473d-8da7-d1389c3f22e7",
  "uuid": "26dcc58c-3f23-47f7-8128-d4f672d95dba",
  "tool_use_result": {
    "stdout": "Valid JSON\nTop-level keys: ['metadata', 'table1_goodhart_landscape', 'table2_hacking_taxonomy', 'claim2_isr_vs_random', 'prolog_exec_only_3seed', 'prolog_sta', 'isr_collapse_trajectory']\nTable1 conditions: ['base_model', 'sft_baseline', 'exec_only_500', 'exec_only_1000', 'isr_b01', 'random_b01', 'isr_b03', 'random_b03', 'convex_random']\nTable2 conditions: ['sft_baseline', 'exec_only_500', 'isr_b01', 'random_b01', 'convex_random']\nProlog exec seeds: ['s42', 's43', 's44']\nProlog STA seeds: ['s42', 's43', 's44']",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 51_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_016fNUVGg2t94ubTLzEG47Y4`</summary>

```json
{
  "name": "table_data",
  "type": "data",
  "description": "Structured JSON with all paper table data: Table 1 (Goodhart landscape, 9 conditions), Table 2 (hacking taxonomy H7/H1/Genuine), Claim 2 (ISR vs Random premise-count-matched), Prolog cross-logic (exec-only 3-seed + STA), ISR collapse trajectory. Sources: registry + eval_sta.py evidence tables.",
  "project": "solver-trace-ablation",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/table_data.json",
  "tags": [
    "paper",
    "tables",
    "data",
    "json"
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
  "session_id": "eb5b7954-c1fd-473d-8da7-d1389c3f22e7",
  "uuid": "d3a6ad72-ffa9-4cc1-af6f-537cc1c6f7cd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NZWvTgaomoSDSsjHcunwhx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 537,
      "cache_read_input_tokens": 59618,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 537
      },
      "output_tokens": 57,
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

_source line 52 · 2026-05-14T17:31:37.215Z_

<details><summary>↩ Tool result · `toolu_016fNUVGg2t94ubTLzEG47Y4`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260514_0d350a\", \"name\": \"table_data\", \"type\": \"data\", \"description\": \"Structured JSON with all paper table data: Table 1 (Goodhart landscape, 9 conditions), Table 2 (hacking taxonomy H7/H1/Genuine), Claim 2 (ISR vs Random premise-count-matched), Prolog cross-logic (exec-only 3-seed + STA), ISR collapse trajectory. Sources: registry + eval_sta.py evidence tables.\", \"path\": \"projects/solver-trace-ablation/artifacts/_project/data/table_data.json\", \"url\": null, \"project\": \"solver-trace-ablation\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-14T17:31:37.142530+00:00\", \"tags\": [\"paper\", \"tables\", \"data\", \"json\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "eb5b7954-c1fd-473d-8da7-d1389c3f22e7",
  "uuid": "57a9cf75-5cda-443f-b9d7-ed33d2c2b625",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260514_0d350a\\\", \\\"name\\\": \\\"table_data\\\", \\\"type\\\": \\\"data\\\", \\\"description\\\": \\\"Structured JSON with all paper table data: Table 1 (Goodhart landscape, 9 conditions), Table 2 (hacking taxonomy H7/H1/Genuine), Claim 2 (ISR vs Random premise-count-matched), Prolog cross-logic (exec-only 3-seed + STA), ISR collapse trajectory. Sources: registry + eval_sta.py evidence tables.\\\", \\\"path\\\": \\\"projects/solver-trace-ablation/artifacts/_project/data/table_data.json\\\", \\\"url\\\": null, \\\"project\\\": \\\"solver-trace-ablation\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-14T17:31:37.142530+00:00\\\", \\\"tags\\\": [\\\"paper\\\", \\\"tables\\\", \\\"data\\\", \\\"json\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260514_0d350a\", \"name\": \"table_data\", \"type\": \"data\", \"description\": \"Structured JSON with all paper table data: Table 1 (Goodhart landscape, 9 conditions), Table 2 (hacking taxonomy H7/H1/Genuine), Claim 2 (ISR vs Random premise-count-matched), Prolog cross-logic (exec-only 3-seed + STA), ISR collapse trajectory. Sources: registry + eval_sta.py evidence tables.\", \"path\": \"projects/solver-trace-ablation/artifacts/_project/data/table_data.json\", \"url\": null, \"project\": \"solver-trace-ablation\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-14T17:31:37.142530+00:00\", \"tags\": [\"paper\", \"tables\", \"data\", \"json\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 53_

已生成 `artifacts/table_data.json` 并注册 (`art_20260514_0d350a`)。

内容覆盖：
- **table1_goodhart_landscape**: 9 个条件（base_model, sft, exec-only 500/1000, ISR/Random β=0.1/0.3, convex），含 exp_id、per-seed 精确指标、3-seed mean±std（重新计算）
- **table2_hacking_taxonomy**: 5 个条件的 H7/H1/Genuine 分布 + key findings
- **claim2_isr_vs_random**: premise-count-matched ISR (1.06×)，3-seed 汇总
- **prolog_exec_only_3seed**: 3 seed + mean±std
- **prolog_sta**: s42 done (H7=100%), s43/s44 RUNNING
- **isr_collapse_trajectory**: 100→500→1000 步 ISR 下降轨迹

数据来源注记：random_b01_s43 的 ISR 值来自 eval_sta.py（registry 仅有 hacking taxonomy），ISR_b03 eval 指标来自 evidence_tables_d051（registry 仅有训练指标）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "eb5b7954-c1fd-473d-8da7-d1389c3f22e7",
  "uuid": "aac46daa-68fd-473b-8946-836478fbd04b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WGAzVUxprJXbDkR7erXWyZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 725,
      "cache_read_input_tokens": 60155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 725
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

### Task result

_source line 54_

已生成 `artifacts/table_data.json` 并注册 (`art_20260514_0d350a`)。

内容覆盖：
- **table1_goodhart_landscape**: 9 个条件（base_model, sft, exec-only 500/1000, ISR/Random β=0.1/0.3, convex），含 exp_id、per-seed 精确指标、3-seed mean±std（重新计算）
- **table2_hacking_taxonomy**: 5 个条件的 H7/H1/Genuine 分布 + key findings
- **claim2_isr_vs_random**: premise-count-matched ISR (1.06×)，3-seed 汇总
- **prolog_exec_only_3seed**: 3 seed + mean±std
- **prolog_sta**: s42 done (H7=100%), s43/s44 RUNNING
- **isr_collapse_trajectory**: 100→500→1000 步 ISR 下降轨迹

数据来源注记：random_b01_s43 的 ISR 值来自 eval_sta.py（registry 仅有 hacking taxonomy），ISR_b03 eval 指标来自 evidence_tables_d051（registry 仅有训练指标）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 480548,
  "duration_api_ms": 480558,
  "num_turns": 8,
  "stop_reason": "end_turn",
  "session_id": "eb5b7954-c1fd-473d-8da7-d1389c3f22e7",
  "total_cost_usd": 1.53971375,
  "usage": {
    "input_tokens": 11,
    "cache_creation_input_tokens": 49039,
    "cache_read_input_tokens": 257238,
    "output_tokens": 21516,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 49039,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 336,
        "cache_read_input_tokens": 60155,
        "cache_creation_input_tokens": 725,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 725
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 3842,
      "outputTokens": 16,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.003922,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 21,
      "outputTokens": 32482,
      "cacheReadInputTokens": 432136,
      "cacheCreationInputTokens": 81211,
      "webSearchRequests": 0,
      "costUSD": 1.5357917500000002,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "1e0b4207-8b7b-423b-b989-b5949f1c7dd3"
}
```

</details>

---
