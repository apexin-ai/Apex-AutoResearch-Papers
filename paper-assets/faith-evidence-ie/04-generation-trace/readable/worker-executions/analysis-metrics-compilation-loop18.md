# analysis metrics compilation loop18

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 53
- **Recorded user turns:** 1
- **Tool calls:** 16
- **Original source:** `logs/workers/worker_analysis_metrics_compilation_loop18_20260519T123940.log`
- **Structured JSON:** [`359bf983e0ddcba97f02.json`](../../sessions/35/359bf983e0ddcba97f02.json)

## Before a recorded user message

17 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "session_id": "bc5f4965-b9c9-4c46-9109-14848d79f92e",
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
  "uuid": "6bd57140-cd25-4807-9956-7480daa19040",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/memory/"
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
    "resetsAt": 1779211200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "adf1d9ec-e17b-485e-97dd-85c572ddc912",
  "session_id": "bc5f4965-b9c9-4c46-9109-14848d79f92e"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the registry and relevant project files to gather all the experimental results.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bc5f4965-b9c9-4c46-9109-14848d79f92e",
  "uuid": "f78d3bae-b81b-4a45-91ae-8b5e49f53ad9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014rXL3tHZCTqW2Frz8QPm4i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14681,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14681
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

我来从 registry 和项目文件中提取所有实验数据并交叉验证。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bc5f4965-b9c9-4c46-9109-14848d79f92e",
  "uuid": "b529a08c-2d19-467c-b075-ec8dc05330a4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014rXL3tHZCTqW2Frz8QPm4i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14681,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14681
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01WQ1KGWL1xTke2eA9HoK1GP`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__read_project_file",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bc5f4965-b9c9-4c46-9109-14848d79f92e",
  "uuid": "eeecb3f2-2893-478d-af67-a2c0a5725dcd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014rXL3tHZCTqW2Frz8QPm4i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14681,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14681
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

_source line 7 · 2026-05-19T12:39:52.357Z_

<details><summary>↩ Tool result · `toolu_01WQ1KGWL1xTke2eA9HoK1GP`</summary>

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
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bc5f4965-b9c9-4c46-9109-14848d79f92e",
  "uuid": "8c7171e0-6e6a-4c37-933f-8c251a31eaec",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__read_project_file"
    ],
    "query": "select:mcp__agent-ml-research__read_registry,mcp__agent-ml-research__read_project_file",
    "total_deferred_tools": 25
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01EaYr6W7q7CCqAepSXBMRis`</summary>

```json
{
  "project": "faith-evidence-ie",
  "limit": 0,
  "filters": {
    "status": "DONE"
  }
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bc5f4965-b9c9-4c46-9109-14848d79f92e",
  "uuid": "50baf1b8-3f59-4669-b8f1-bae346c80b10",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0169xhWqGaGuXbovgGfbnSVP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 843,
      "cache_read_input_tokens": 26128,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 843
      },
      "output_tokens": 60,
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_018vBtV3LCreagJfjs3U74QX`</summary>

```json
{
  "project": "faith-evidence-ie",
  "file": "ROADMAP.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bc5f4965-b9c9-4c46-9109-14848d79f92e",
  "uuid": "da3f4c0d-4a4f-4835-b008-d5180961bf11",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0169xhWqGaGuXbovgGfbnSVP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 843,
      "cache_read_input_tokens": 26128,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 843
      },
      "output_tokens": 60,
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

_source line 10_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01NFnZW1bVaX96tWJCvG2j6g`</summary>

```json
{
  "project": "faith-evidence-ie",
  "file": "memory.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bc5f4965-b9c9-4c46-9109-14848d79f92e",
  "uuid": "fc163df7-b92e-4bbe-943e-32661f4d152c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0169xhWqGaGuXbovgGfbnSVP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 843,
      "cache_read_input_tokens": 26128,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 843
      },
      "output_tokens": 60,
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

_source line 11 · 2026-05-19T12:39:56.218Z_

<details><summary>↩ Tool result · `toolu_01EaYr6W7q7CCqAepSXBMRis`</summary>

```text
Error: result (142,271 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/bc5f4965-b9c9-4c46-9109-14848d79f92e/tool-results/mcp-agent-ml-research-read_registry-1779194396202.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/bc5f4965-b9c9-4c46-9109-14848d79f92e/tool-results/mcp-agent-ml-research-read_registry-1779194396202.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/bc5f4965-b9c9-4c46-9109-14848d79f92e/tool-results/mcp-agent-ml-research-read_registry-1779194396202.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bc5f4965-b9c9-4c46-9109-14848d79f92e",
  "uuid": "1c682670-2c5e-4d76-8626-a474e9a7f9f4",
  "tool_use_result": {
    "content": "Error: result (142,271 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/bc5f4965-b9c9-4c46-9109-14848d79f92e/tool-results/mcp-agent-ml-research-read_registry-1779194396202.txt.\nFormat: JSON with schema: {result: string}\n- For targeted queries (find a value, filter by field): use jq on the file directly.\n- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/bc5f4965-b9c9-4c46-9109-14848d79f92e/tool-results/mcp-agent-ml-research-read_registry-1779194396202.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.\n- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/bc5f4965-b9c9-4c46-9109-14848d79f92e/tool-results/mcp-agent-ml-research-read_registry-1779194396202.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim.\" A vague \"summarize this\" may lose detail.\n",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"d112_rsft_s44_eval\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T07:34:55.266Z\", \"updated_at\": \"2026-05-19T12:02:10.888Z\", \"hypothesis\": \"D112 step 4: D076 eval for RSFT trained on SFT s44 base with CED k=1 scored data. 验证 RSFT 在最强 SFT seed (s44, ign_f1=0.4734) 上的泛化效果。预期 ign_f1 > 0.4734 (SFT s44 baseline)。\", \"parent\": \"d112_rsft_s44_train\", \"conclusion\": \"failed\", \"metrics\": {\"ign_f1\": 0.2181, \"note\": \"INVALID: QLoRA confound — adapter trained on 4-bit quantized backbone evaluated in bf16\"}}, \"plan019_1_7b_rsft_s44_r2_eval\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T08:43:01.975Z\", \"updated_at\": \"2026-05-19T12:00:32.897Z\", \"hypothesis\": \"D076 eval for 1.7B RSFT s44_r2 (Method A: s42 SFT adapter + s42 CED k=1 data, RSFT seed=44). 预期 ign_f1 接近 s42 (0.5122) 和 s43 (0.5109)，完成 1.7B 3-seed RSFT 统计。\", \"parent\": \"plan019_1_7b_rsft_s44_r2\", \"metrics\": {\"ign_f1\": 0.5125, \"ign_precision\": 0.5173, \"ign_recall\": 0.5078, \"f1\": 0.5294, \"precision\": 0.5434, \"recall\": 0.5162, \"evi_precision\": 0.815, \"evi_recall\": 0.8387, \"evi_f1\": 0.8267, \"edcr\": 0.6181, \"evi_joint_precision\": 0.4284, \"evi_joint_recall\": 0.4294, \"evi_f1_joint\": 0.4289, \"format_compliance_rate\": 0.999, \"field_compliance_rate\": 0.7543, \"n_truncated\": 240, \"inference_time_seconds\": 8615.6}, \"conclusion\": \"success\"}, \"d112_rsft_s44_train\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T04:33:11.623Z\", \"updated_at\": \"2026-05-19T11:18:57.557Z\", \"hypothesis\": \"D112 step 3: RSFT training on SFT s44 base using CED k=1 scored data. 在最强 SFT seed (s44, ign_f1=0.4734) 上验证 RSFT 效果，参数与 canonical s42 RSFT 完全一致。\", \"parent\": \"d112_rsft_s44_ced_score\", \"conclusion\": \"failed\", \"metrics\": {\"train_loss\": 0.6488, \"global_step\": 567}}, \"plan017_14b_sft_eval\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T07:23:43.367Z\", \"updated_at\": \"2026-05-19T08:54:24.083Z\", \"hypothesis\": \"D076 eval for 14B SFT baseline. 14B 是第 4 个 scale 档（1.7B/4B/8B/14B），SFT baseline 用于计算 RSFT 增益和 evidence tax。预期 ign_f1 高于 8B SFT mean (0.4866)。\", \"parent\": \"plan017_14b_sft\", \"conclusion\": \"killed\"}, \"plan017_14b_sft_no_evidence_eval\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T07:23:46.290Z\", \"updated_at\": \"2026-05-19T08:49:48.692Z\", \"hypothesis\": \"14B SFT no-evidence eval: 测量 14B SFT 在不提供 evidence 时的 ign_f1，用于计算 evidence tax (Claim 3)。与 4B evidence tax (D107: 47.21% vs 39.74%) 对比，验证 scale-dependent evidence tax 趋势。\", \"parent\": \"plan017_14b_sft\", \"conclusion\": \"killed\"}, \"plan019_1_7b_rsft_s43_r2_eval\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T06:15:45.750Z\", \"updated_at\": \"2026-05-19T08:42:24.182Z\", \"hypothesis\": \"D076 eval for 1.7B RSFT s43_r2 (Method A: s42 SFT adapter + s42 CED k=1 data, RSFT seed=43). 预期 ign_f1 接近 s42 RSFT (0.5122)，验证 1.7B RSFT 跨 seed 稳健性。\", \"parent\": \"plan019_1_7b_rsft_s43_r2\", \"metrics\": {\"ign_f1\": 0.5109, \"ign_precision\": 0.5186, \"ign_recall\": 0.5035, \"f1\": 0.5271, \"precision\": 0.5444, \"recall\": 0.5109, \"evi_precision\": 0.8218, \"evi_recall\": 0.834, \"evi_f1\": 0.8278, \"edcr\": 0.6245, \"evi_joint_precision\": 0.4336, \"evi_joint_recall\": 0.4221, \"evi_f1_joint\": 0.4278, \"format_compliance_rate\": 0.999, \"field_compliance_rate\": 0.7503, \"n_truncated\": 244, \"inference_time_seconds\": 8498.2}, \"conclusion\": \"success\"}, \"plan017_14b_sft\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T04:22:05.400Z\", \"updated_at\": \"2026-05-19T07:19:50.806Z\", \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 0.5457, \"eval_loss\": 0.6292}, \"hypothesis\": \"Scaling from Qwen3-8B to Qwen3-14B with LoRA SFT on the same DocRED faith-evidence IE data will improve extraction quality because the larger model has greater capacity to learn complex relation extraction patterns with evidence grounding.\"}, \"plan019_1_7b_rsft_s44_r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T04:26:18.370Z\", \"updated_at\": \"2026-05-19T06:17:08.769Z\", \"hypothesis\": \"D114 Method A: 1.7B RSFT k=1 s44 重跑。使用 s42 SFT adapter (sft_output_qwen3_1_7b_bf16) + s42 CED k=1 scored data, RSFT seed=44。验证 1.7B 尺度 RSFT 增益跨 seed 稳健性。\", \"parent\": \"plan019_1_7b_rsft_s44\", \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 0.5538, \"final_step\": 567, \"epoch\": 3, \"mean_token_accuracy\": 0.8706}}, \"plan019_1_7b_rsft_s43_r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T04:26:17.166Z\", \"updated_at\": \"2026-05-19T05:59:49.377Z\", \"hypothesis\": \"D114 Method A: 1.7B RSFT k=1 s43 重跑。使用 s42 SFT adapter (sft_output_qwen3_1_7b_bf16) + s42 CED k=1 scored data, RSFT seed=43。原始运行输出被误删(Worker B 误判)，需重新训练。验证 1.7B 尺度 RSFT 增益跨 seed 稳健性。\", \"parent\": \"plan019_1_7b_rsft_s43\", \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 0.5526}}, \"plan019_1_7b_rsft_s44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T03:02:05.852Z\", \"updated_at\": \"2026-05-19T05:11:17.769Z\", \"hypothesis\": \"1.7B RSFT k=1 s44 (Option A seed expansion): 复用 s42 SFT adapter + s42 CED k=1 scored data，只变 RSFT 训练 seed 为 44。验证 1.7B 尺度 RSFT 增益跨 seed 稳健性。\", \"parent\": \"plan019_1_7b_sft_s44\", \"conclusion\": \"failed\"}, \"plan019_1_7b_rsft_s43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T02:51:57.316Z\", \"updated_at\": \"2026-05-19T05:11:16.432Z\", \"hypothesis\": \"1.7B RSFT k=1 s43 (Option A seed expansion): 复用 s42 SFT adapter + s42 CED k=1 scored data，只变 RSFT 训练 seed 为 43。验证 1.7B 尺度 RSFT 增益跨 seed 稳健性。\", \"parent\": \"plan019_1_7b_sft_s43_r2\", \"conclusion\": \"failed\"}, \"plan019_8b_rsft_s44_eval\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T02:11:06.132Z\", \"updated_at\": \"2026-05-19T05:08:07.693Z\", \"hypothesis\": \"8B RSFT s44 eval (Option A seed expansion). 预期 ign_f1 接近 canonical s42 (0.5376)，验证 RSFT 增益在 8B 尺度跨 seed 稳定。\", \"parent\": \"plan019_8b_rsft_s44\", \"conclusion\": \"success\", \"metrics\": {\"ign_f1\": 0.5451, \"f1\": 0.562, \"evi_f1_tp\": 0.8145, \"evi_f1_dreeam\": 0.4472, \"edcr\": 0.6233, \"format_ok\": \"985/985\", \"truncated\": \"230/985\", \"predictions\": 16254}, \"notes\": \"Cron 误报 failed (submit_training_job 脚本路径不存在 EXIT_CODE=127)，但 Worker 已通过 Python 直接执行 eval 成功。结果在 /root/autodl-tmp/eval_results/rsft_8b_k1_s44_eval.log。已更正为 success。8B RSFT s44 ign_f1=0.5451 vs canonical s42 0.5376 (+0.75pp)，跨 seed 稳健。\"}, \"d112_rsft_s44_ced_score\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T03:18:56.333Z\", \"updated_at\": \"2026-05-19T04:41:13.613Z\", \"hypothesis\": \"D112 step 2: CED scoring + k=1 selection on SFT s44 generation candidates. 使用 NLI-DeBERTa 对 N=8 候选打分，format_w=0.2, f1_w=0.4, ced_w=0.4，top_k=1 筛选最优样本用于后续 RSFT 训练。\", \"parent\": \"d112_rsft_s44_gen_shard0\", \"notes\": \"retry #2 running normally. 10000/24216 records scored as of 11:50 UTC. ETA ~12:33 UTC. Previous run failed at 03:28 UTC (process dead before scoring started). Current run healthy, no errors in log.\", \"conclusion\": \"success\"}, \"d111_4b_sft_s42_reeval\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T22:06:04.423Z\", \"updated_at\": \"2026-05-19T03:54:03.116Z\", \"hypothesis\": \"Re-evaluating 4B SFT s42 with D076 standardized protocol to establish fair 3-seed comparison with s43 and s44. Previous s42 evaluations gave inconsistent results (0.4106/0.4036/0.3974), so re-running with identical protocol resolves this.\", \"metrics\": {\"ign_f1\": 0.3974, \"rel_f1\": 0.4049, \"evi_f1\": 0.7986, \"evi_f1_joint\": 0.3147, \"edcr\": 0.6982}, \"conclusion\": \"success\"}, \"d112_rsft_s44_gen_shard3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T00:44:31.524Z\", \"updated_at\": \"2026-05-19T03:17:28.913Z\", \"hypothesis\": \"D112 shard 3: 并行候选生成 (docs [2268:3027])，用 SFT s44 adapter 生成 N=8 RSFT 候选。\", \"conclusion\": \"success\"}, \"d112_rsft_s44_gen_shard1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T23:43:46.463Z\", \"updated_at\": \"2026-05-19T03:01:57.420Z\", \"hypothesis\": \"D112 shard 1: 并行候选生成 (docs [756:1512])，用 SFT s44 adapter 生成 N=8 RSFT 候选。\", \"parent\": \"\", \"conclusion\": \"success\"}, \"d112_rsft_s44_gen_shard2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T23:43:47.622Z\", \"updated_at\": \"2026-05-19T02:48:30.925Z\", \"hypothesis\": \"D112 shard 2: 并行候选生成 (docs [1512:2268])，用 SFT s44 adapter 生成 N=8 RSFT 候选。\", \"parent\": \"\", \"conclusion\": \"success\"}, \"d112_rsft_s44_gen_shard0\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T00:44:30.408Z\", \"updated_at\": \"2026-05-19T02:29:19.517Z\", \"hypothesis\": \"D112 shard 0: 并行候选生成 (docs [0:756])，用 SFT s44 adapter 生成 N=8 RSFT 候选。\", \"conclusion\": \"success\"}, \"d112_rsft_s44_generate\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T23:19:06.977Z\", \"updated_at\": \"2026-05-19T00:09:15.715Z\", \"hypothesis\": \"D112 step1: 用 SFT s44 adapter (ign_f1=0.4734, 最强 seed) 生成 N=8 RSFT 候选。验证 RSFT pipeline 从强 SFT base 出发是否能进一步提升，决定 Claim 1 表述强度。\", \"parent\": \"wave1_sft_4b_s44_eval_r2\", \"conclusion\": \"killed\"}, \"plan019_8b_rsft_s44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T22:24:55.221Z\", \"updated_at\": \"2026-05-18T23:45:23.816Z\", \"hypothesis\": \"8B RSFT seed44 (Option A: seed expansion). Reuses s42 SFT adapter + s42 CED k=1 scored data, only changes RSFT training seed to 44. Tests if RSFT gain is robust across seeds at 8B scale. Expected: ign_f1 similar to canonical 8B RSFT s42.\", \"conclusion\": \"success\", \"metrics\": {\"total_steps\": 1134, \"epochs\": 3, \"samples\": 3018, \"checkpoint\": \"checkpoint-1134\", \"adapter_size_mb\": 698, \"train_loss\": 0.4725, \"mean_token_accuracy\": 0.8734}}, \"plan019_8b_sft_s44_eval\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T21:36:26.622Z\", \"updated_at\": \"2026-05-18T23:44:30.382Z\", \"hypothesis\": \"8B SFT s44 eval (D076 protocol): measure SFT baseline for seed44 at 8B scale. Paired with canonical s42 (ign_f1=0.5051) for 2-seed mean±std.\", \"parent\": \"plan019_8b_sft_s44\", \"conclusion\": \"success\", \"metrics\": {\"ign_f1\": 0.4681, \"f1\": 0.4841, \"evi_f1\": 0.8361, \"evi_f1_joint\": 0.3839, \"edcr\": 0.6697, \"format_ok_rate\": 1, \"n_truncated\": 306, \"n_predictions\": 16690, \"inference_time_seconds\": 6951.1}}, \"grpo_bf16_g4_ckpt200_eval\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T20:05:54.201Z\", \"updated_at\": \"2026-05-18T23:16:39.233Z\", \"hypothesis\": \"GRPO bf16 G=4 checkpoint-200 eval (final): compare with ckpt-100 for D106 learning curve. If ckpt-200 > ckpt-100, GRPO is improving. Expected: rel_f1 improvement over ckpt-100.\", \"parent\": \"wave1_grpo_bf16_g4\", \"conclusion\": \"success\", \"metrics\": {\"ign_f1\": 0.4446, \"rel_f1\": 0.4513, \"evi_f1\": 0.8053, \"evi_f1_joint\": 0.3562, \"edcr\": 0.6489, \"format_ok\": \"984/985\", \"n_truncated\": 204, \"n_predictions\": 15733, \"field_compliance_rate\": 0.792}}, \"random_rsft_k1_baseline\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T13:32:46.287Z\", \"updated_at\": \"2026-05-18T22:23:06.386Z\", \"hypothesis\": \"Random k=1 RSFT baseline: same candidate pool as CED RSFT but random selection instead of CED scoring. If random RSFT significantly underperforms CED RSFT (rel_f1 gap > 1.5pp), proves CED scoring precision is the key, not just data filtering quantity. CED k=1 mean rel_f1=0.4596, expect random < 0.445.\", \"metrics\": {\"train_loss\": 0.578, \"mean_token_accuracy\": 0.8552, \"global_steps\": 1020, \"epochs\": 3}, \"conclusion\": \"success\"}, \"plan019_1_7b_sft_s44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T15:22:46.118Z\", \"updated_at\": \"2026-05-18T22:23:04.346Z\", \"hypothesis\": \"1.7B SFT seed44: scaling seeds for statistical robustness. Paired with canonical s42 and s43 for 3-seed mean±std at 1.7B scale. Expected train_loss ~0.70, rel_f1 ~49.5 based on canonical 1.7B SFT.\", \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 0.5783, \"eval_loss\": 0.8037, \"eval_mean_token_accuracy\": 0.8238, \"global_steps\": 570, \"epochs\": 3}}, \"wave1_sft_4b_s44_eval_r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T20:05:57.119Z\", \"updated_at\": \"2026-05-18T22:20:06.715Z\", \"hypothesis\": \"4B SFT seed44 eval r2 (corrected D076 command: --model_path=base --sft_adapter=adapter). Re-run of failed wave1_sft_4b_s44_eval. Expected rel_f1 ~50.5 based on canonical 4B SFT s42.\", \"parent\": \"wave1_sft_4b_s44\", \"metrics\": {\"ign_f1\": 0.4734, \"f1\": 0.4838, \"ign_precision\": 0.4676, \"ign_recall\": 0.4794, \"precision\": 0.4898, \"recall\": 0.478, \"evi_f1_joint\": 0.382, \"evi_f1_tp\": 0.7875, \"edcr\": 0.6581, \"format_ok_rate\": 0.997, \"n_truncated\": 249, \"n_documents\": 985, \"n_predictions\": 16143, \"inference_time_seconds\": 6669.5}, \"conclusion\": \"success\"}, \"plan019_1_7b_sft_s43_eval\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T20:33:55.681Z\", \"updated_at\": \"2026-05-18T22:03:20.771Z\", \"hypothesis\": \"Eval 1.7B SFT seed43 on DocRED dev set to measure RE performance. Paired with s42 for 2-seed mean±std at 1.7B scale.\", \"parent\": \"plan019_1_7b_sft_s43\", \"metrics\": {\"ign_f1\": 0.4286, \"f1\": 0.4372, \"ign_precision\": 0.4475, \"ign_recall\": 0.4111, \"precision\": 0.4704, \"recall\": 0.4084, \"evi_f1\": 0.835, \"evi_f1_joint\": 0.3442, \"edcr\": 0.704, \"format_compliance\": 1, \"field_compliance\": 0.5858, \"n_total\": 985, \"n_predictions\": 18140, \"n_truncated\": 408, \"inference_time_seconds\": 5257.4}, \"conclusion\": \"success\"}, \"wave1_sft_4b_s43_eval_r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T19:29:28.052Z\", \"updated_at\": \"2026-05-18T21:34:25.964Z\", \"hypothesis\": \"4B SFT seed43 eval r2 (corrected D076 command: --model_path=base --sft_adapter=adapter). Re-run of failed wave1_sft_4b_s43_eval. Expected rel_f1 ~50.5 based on canonical 4B SFT s42.\", \"metrics\": {\"ign_f1\": 0.4365, \"rel_f1\": 0.4429, \"evi_f1_joint\": 0.3462, \"evi_f1_tp\": 0.8021, \"edcr\": 0.6827, \"format_compliance_rate\": 1, \"n_truncated\": 318, \"n_predictions\": 17055, \"inference_time_seconds\": 7157.9}, \"conclusion\": \"success\"}, \"plan019_8b_sft_s44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T19:24:16.330Z\", \"updated_at\": \"2026-05-18T20:32:15.073Z\", \"hypothesis\": \"8B Qwen3 SFT seed44: scaling seeds for statistical robustness. Paired with canonical s42 for 2-seed mean±std at 8B scale. Expected train_loss similar to canonical 8B SFT.\", \"metrics\": {\"train_loss\": 0.5691, \"eval_loss\": 0.7196, \"eval_mean_token_accuracy\": 0.8379, \"eval_entropy\": 0.5579, \"train_runtime_s\": 3823.89, \"epoch\": 3}, \"conclusion\": \"success\"}, \"plan019_1_7b_sft_s43_r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T19:31:33.003Z\", \"updated_at\": \"2026-05-18T20:21:13.903Z\", \"hypothesis\": \"1.7B SFT seed43 r2: third seed for 1.7B scaling robustness. s42 ign_f1=0.4786, s44 ign_f1=0.4321, variance=4.65pp is extreme. Third seed critical to determine if s44 is outlier or s42 is outlier.\", \"metrics\": {\"train_loss\": 0.6881, \"eval_loss\": 0.8029, \"eval_mean_token_accuracy\": 0.8237, \"eval_entropy\": 0.681, \"epochs\": 3, \"runtime_seconds\": 2697}, \"conclusion\": \"success\"}, \"wave1_grpo_bf16_g4\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T12:46:19.740Z\", \"updated_at\": \"2026-05-18T20:09:28.981Z\", \"hypothesis\": \"GRPO bf16 without quantization (G=4): prior GRPO runs used int4 quantization which may have caused training instability. bf16 full precision should provide clean GRPO signal. If GRPO improves over RSFT, validates Claim 2 (decoupling spectrum). Expected: rel_f1 > RSFT baseline (~52pp).\", \"metrics\": {\"reward_mean\": 1.7646, \"steps_completed\": 200, \"max_steps\": 200}, \"conclusion\": \"success\"}, \"random_rsft_k1_eval\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T16:34:48.815Z\", \"updated_at\": \"2026-05-18T20:08:52.336Z\", \"hypothesis\": \"Random k=1 RSFT eval: if random selection significantly underperforms CED RSFT (gap > 1.5pp in rel_f1), proves CED scoring precision is the key differentiator. CED k=1 mean rel_f1=0.4596, expect random &lt; 0.445.\", \"parent\": \"random_rsft_k1_baseline\", \"metrics\": {\"ign_f1\": 0.4114, \"f1\": 0.4198, \"evi_f1\": 0.7964, \"evi_f1_joint\": 0.3216, \"EDCR\": 0.6971, \"format_compliance\": 0.999, \"field_compliance\": 0.7482, \"truncated\": 235, \"n_total\": 985, \"n_predictions\": 16110, \"inference_time_seconds\": 11778.5}, \"conclusion\": \"success\"}, \"grpo_bf16_g4_ckpt100_eval\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T16:34:51.597Z\", \"updated_at\": \"2026-05-18T20:08:50.166Z\", \"hypothesis\": \"GRPO bf16 G=4 checkpoint-100 eval (D106 conditional termination): evaluate mid-training checkpoint to decide whether to continue GRPO training to step 200. If rel_f1 >= RSFT baseline (~52pp), continue. If significantly below, consider early termination.\", \"parent\": \"wave1_grpo_bf16_g4\", \"metrics\": {\"ign_f1\": 0.4431, \"f1\": 0.4511, \"evi_f1\": 0.801, \"evi_f1_joint\": 0.3532, \"EDCR\": 0.6453, \"format_compliance\": 0.999, \"field_compliance\": 0.8142, \"truncated\": 182, \"n_total\": 985, \"n_predictions\": 15187, \"inference_time_seconds\": 11458.2}, \"conclusion\": \"success\"}, \"plan019_1_7b_sft_s44_eval\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T16:34:45.563Z\", \"updated_at\": \"2026-05-18T19:27:55.325Z\", \"hypothesis\": \"1.7B SFT seed44 eval (D076 protocol): measure baseline SFT performance for seed44 at 1.7B scale. Paired with canonical s42 for scaling seed robustness. Expected rel_f1 ~49.5 based on canonical 1.7B SFT.\", \"parent\": \"plan019_1_7b_sft_s44\", \"metrics\": {\"ign_f1\": 0.4321, \"f1\": 0.4441, \"evi_f1_tp\": 0.819, \"evi_f1_joint\": 0.3482, \"edcr\": 0.69, \"n_truncated\": 473, \"n_predictions\": 20237, \"n_documents\": 985, \"format_ok_rate\": 1, \"field_compliance_rate\": 0.5198, \"evidence_format_rate\": 0.5198, \"inference_time_seconds\": 6146}, \"conclusion\": \"success\"}, \"plan019_1_7b_sft_s43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T15:22:44.792Z\", \"updated_at\": \"2026-05-18T16:27:07.679Z\", \"hypothesis\": \"1.7B SFT seed43: scaling seeds for statistical robustness. Paired with canonical s42 and s44 for 3-seed mean±std at 1.7B scale. Expected train_loss ~0.70, rel_f1 ~49.5 based on canonical 1.7B SFT.\", \"conclusion\": \"failed\"}, \"wave1_sft_4b_s44_eval\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T14:01:43.597Z\", \"updated_at\": \"2026-05-18T15:43:33.593Z\", \"hypothesis\": \"SFT 4B seed44 eval (D076 protocol): baseline SFT performance for seed44. Paired with s43 for mean±std. Expected rel_f1 ~50.5 based on prior 4B SFT s42 results.\", \"parent\": \"wave1_sft_4b_s44\", \"conclusion\": \"failed\"}, \"wave1_sft_4b_s43_eval\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T14:01:42.261Z\", \"updated_at\": \"2026-05-18T15:43:30.104Z\", \"hypothesis\": \"SFT 4B seed43 eval (D076 protocol): baseline SFT performance for seed43. Paired with s44 for mean±std. Expected rel_f1 ~50.5 based on prior 4B SFT s42 results.\", \"parent\": \"wave1_sft_4b_s43\", \"conclusion\": \"failed\"}, \"seed_llama_rsft_k1_s43_eval\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T13:30:51.665Z\", \"updated_at\": \"2026-05-18T15:22:14.518Z\", \"hypothesis\": \"LLaMA-8B RSFT k=1 seed43 eval: paired with s42 (rel_f1=0.5839) for seed robustness. If s43 gives similar results (±1.5pp), cross-architecture RSFT k=1 claim is robust. Expected rel_f1 ~0.58±0.015.\", \"parent\": \"rsft_llama_k1_s43_train\", \"conclusion\": \"success\"}, \"wave1_sft_4b_s44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T12:44:43.563Z\", \"updated_at\": \"2026-05-18T14:01:03.605Z\", \"hypothesis\": \"SFT baseline for Qwen3-4B seed44: second seed for SFT baseline. Paired with seed43 for mean±std reporting. Expected rel_f1 similar to seed43 (~50.5±1pp).\", \"conclusion\": \"success\"}, \"wave1_sft_4b_s43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T12:44:52.340Z\", \"updated_at\": \"2026-05-18T14:01:01.015Z\", \"hypothesis\": \"SFT baseline for Qwen3-4B seed43: standard SFT without CED filtering. Paired with RSFT to measure CED filtering gain. Expected rel_f1 ~50.5 based on prior 8B SFT results scaled down.\", \"conclusion\": \"success\"}, \"d102_llama_rsft_k1_s43_eval\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T13:06:23.193Z\", \"updated_at\": \"2026-05-18T13:59:53.656Z\", \"hypothesis\": \"LLaMA-8B RSFT k=1 seed43 eval: paired with s42 (rel_f1=0.5839) for seed robustness. If s43 gives similar results (±1.5pp), cross-architecture RSFT k=1 claim is robust. Expected rel_f1 ~0.58±0.015.\", \"parent\": \"rsft_llama_k1_s43_train\", \"conclusion\": \"killed\"}, \"seed_llama_rsft_k1_s43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T12:47:48.554Z\", \"updated_at\": \"2026-05-18T13:01:01.136Z\", \"conclusion\": \"failed\"}, \"rsft_llama_k1_s43_train\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T11:42:54.821Z\", \"updated_at\": \"2026-05-18T12:47:09.743Z\", \"hypothesis\": \"LLaMA-3.1-8B RSFT k=1 seed43: 与 s42 配对验证种子稳定性。k=1 数据（2952 samples），跨架构验证 CED 筛选在 LLaMA 上的效果。\", \"conclusion\": \"success\", \"metrics\": {\"train_loss_final\": 0.4447, \"mean_token_accuracy_final\": 0.8912, \"global_steps\": 1107, \"epochs\": 3, \"total_flos\": 386000000000000000}}, \"d102_8b_rsft_k1_s43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T05:40:05.983Z\", \"updated_at\": \"2026-05-18T12:18:54.937Z\", \"hypothesis\": \"D102 方法论修正：8B RSFT k=1 seed43，与 s42 配对验证种子稳定性。k=1 数据（3018 samples），超参与 4B canonical 一致。\", \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 0.3862, \"mean_token_accuracy\": 0.8735, \"epochs\": 3, \"global_steps\": 1134, \"runtime_seconds\": 2894.88, \"entropy\": 0.5195, \"data_samples\": 3018}}, \"d102_8b_rsft_k1_s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T05:40:04.009Z\", \"updated_at\": \"2026-05-18T12:18:53.819Z\", \"hypothesis\": \"D102 方法论修正：8B RSFT 从 k=3 改为 k=1（与论文声明和 4B canonical 一致）。k=1 筛选更严格（3018 samples vs 9041），预期 rel_f1 与 k=3 相当或略有变化，验证 k=1 在 8B 上同样有效。\", \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 0.3877, \"mean_token_accuracy\": 0.8579, \"epochs\": 3, \"global_steps\": 1134, \"runtime_seconds\": 2915.82, \"entropy\": 0.5847, \"data_samples\": 3018}}, \"d102_llama_rsft_k1_s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T05:40:08.858Z\", \"updated_at\": \"2026-05-18T08:52:32.145Z\", \"hypothesis\": \"D102 方法论修正：LLaMA-8B RSFT 从 k=3 改为 k=1（与论文声明和 4B canonical 一致）。k=1 筛选更严格（2952 samples vs 8829），跨架构验证 k=1 RSFT 效果。\", \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 0.3698, \"mean_token_accuracy\": 0.8876, \"epochs\": 3, \"global_steps\": 1107, \"runtime_seconds\": 2601.34, \"entropy\": 0.5017, \"data_samples\": 2952}}, \"d102_1_7b_rsft_k1_s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T05:40:07.489Z\", \"updated_at\": \"2026-05-18T08:52:27.461Z\", \"hypothesis\": \"D102 方法论修正：1.7B RSFT 从 k=3 改为 k=1（与论文声明和 4B canonical 一致）。k=1 筛选更严格（3021 samples vs 9042），在最小模型上验证 k=1 RSFT 效果。\", \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 0.3063, \"mean_token_accuracy\": 0.8731, \"epochs\": 3, \"global_steps\": 567, \"runtime_seconds\": 899.39, \"entropy\": 0.5467, \"data_samples\": 3021}}, \"seed_comparison_prep\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T02:35:52.694Z\", \"updated_at\": \"2026-05-17T23:18:37.491Z\", \"notes\": \"## Seed Comparison Pre-Analysis (2026-05-16)\\n\\n### Available Results (3/4 seeds each, s45 pending for both):\\n\\n**flat-NLI RSFT:**\\n- s42: rel_f1=0.4539 (dir: rsft_flat_nli)\\n- s43: rel_f1=0.4523 (dir: rsft_flat_nli_s43_reeval; original rsft_flat_nli_s43 was broken f1=0.002)\\n- s44: rel_f1=0.4615 (dir: rsft_flat_nli_s44; NOTE: only metrics.json, no metrics_v2.json with fixed Ign-F1)\\n- s45: PENDING (empty dir)\\n- Mean: 0.4559 ± 0.0049\\n\\n**CED RSFT:**\\n- s42: rel_f1=0.4504 (dir: rsft_r2b_maxtok1536)\\n- s43: rel_f1=0.4683 (dir: rsft_s43)\\n- s44: rel_f1=0.4655 (dir: rsft_s44)\\n- s45: PENDING (empty dir)\\n- Mean: 0.4614 ± 0.0096\\n\\n### Pre-comparison (N=3):\\n- rel_f1 Delta (fNLI - CED): -0.0055 (CED slightly better)\\n- Paired t-test: t=0.967, p=0.4357 (NOT significant)\\n- 95% CI for delta: [-0.0299, +0.0189] (crosses zero)\\n- Cohen's d: -0.558\\n\\n### seed_comparison.py status: WORKING\\n- Auto-discovers all seeds, handles fallback dirs, filters broken results (f1<0.01)\\n- Outputs to /root/autodl-tmp/eval_results/seed_comparison.{md,json}\\n- Supports --watch mode for polling\", \"conclusion\": \"killed\"}, \"plan006_1_7b_rsft_eval\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T06:10:39.978Z\", \"updated_at\": \"2026-05-17T23:18:35.353Z\", \"conclusion\": \"killed\"}, \"rsft_s43_dev_eval_preds\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T08:35:42.135Z\", \"updated_at\": \"2026-05-17T23:18:03.147Z\", \"hypothesis\": \"Eval RSFT-s43 (CED-scored) on DocRED dev with predictions saved. Prerequisite for Lead 1 CED evidence filtering: per-sentence NLI scoring requires full prediction outputs.\", \"metrics\": {\"ign_f1\": 0.4512, \"f1\": 0.4601, \"evi_f1\": 0.8063, \"edcr\": 0.6542, \"evi_f1_joint\": 0.3605, \"format_compliance_rate\": 1, \"field_compliance_rate\": 0.809, \"n_truncated\": 184, \"inference_time_seconds\": 10982}, \"conclusion\": \"success\"}, \"plan_006_qwen3_1_7b_rsft_eval_r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T08:35:45.455Z\", \"updated_at\": \"2026-05-17T23:18:01.212Z\", \"hypothesis\": \"Evaluate 1.7B RSFT model (checkpoint-1698) on DocRED dev. Retry after disk-full crash. Validates CED-filtered RSFT at smallest model scale in scaling study.\", \"parent\": \"plan_006_qwen3_1_7b_rsft_train\", \"metrics\": {\"ign_f1\": 0.505, \"f1\": 0.5219, \"evi_f1\": 0.8309, \"edcr\": 0.6297, \"evi_f1_joint\": 0.4223, \"format_compliance_rate\": 0.999, \"field_compliance_rate\": 0.732, \"n_truncated\": 258, \"inference_time_seconds\": 9464}, \"conclusion\": \"success\"}, \"plan_006_llama_rsft_r3_eval\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T08:35:48.098Z\", \"updated_at\": \"2026-05-17T23:17:59.347Z\", \"hypothesis\": \"Evaluate LLaMA-3.1-8B RSFT r3 (checkpoint-3312, final) on DocRED dev. Cross-architecture validation: if CED-RSFT works on both Qwen and LLaMA, the method is architecture-agnostic.\", \"metrics\": {\"ign_f1\": 0.5563, \"f1\": 0.5674, \"evi_f1\": 0.8255, \"edcr\": 0.5856, \"evi_f1_joint\": 0.4571, \"format_compliance_rate\": 0.997, \"field_compliance_rate\": 0.807, \"n_truncated\": 187, \"inference_time_seconds\": 8650}, \"conclusion\": \"success\"}, \"plan_006_qwen3_8b_rsft_train_r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T08:35:51.553Z\", \"updated_at\": \"2026-05-17T23:17:57.426Z\", \"hypothesis\": \"RSFT with CED-scored data (9041 samples) on Qwen3-8B, resume from checkpoint-750 after disk-full crash. At 8B scale, CED-filtered RSFT should achieve highest absolute performance in scaling study.\", \"parent\": \"plan_006_qwen3_8b_rsft_train\", \"metrics\": {\"train_loss\": 0.3008, \"mean_token_accuracy\": 0.9172, \"epochs\": 3, \"runtime_seconds\": 8983}, \"conclusion\": \"success\"}, \"plan_006_qwen3_1_7b_rsft_seed43_eval\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T14:26:15.446Z\", \"updated_at\": \"2026-05-17T19:56:30.167Z\", \"hypothesis\": \"Evaluate 1.7B RSFT seed 43 on DocRED dev. Seed 42 gave rel_f1=0.5219. If seed 43 gives similar result (±1pp, i.e., 0.51-0.53), the 1.7B scaling study datapoint is robust.\", \"parent\": \"plan_006_qwen3_1_7b_rsft_seed43\", \"conclusion\": \"success\", \"metrics\": {\"f1\": 0.518, \"ign_f1\": 0.5024, \"evi_f1_joint\": 0.4201, \"evi_f1_tp\": 0.8341, \"edcr\": 0.6246, \"precision\": 0.535, \"recall\": 0.5019, \"ign_precision\": 0.5099, \"ign_recall\": 0.4951, \"format_ok\": \"984/985\", \"n_truncated\": 262, \"n_predictions\": 16455}}, \"plan_006_qwen3_1_7b_rsft_test\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T16:50:19.779Z\", \"updated_at\": \"2026-05-17T19:56:28.396Z\", \"hypothesis\": \"Generate 1.7B RSFT test set predictions for CodaLab submission. 1.7B RSFT dev rel_f1=0.5219, expect similar performance on test.\", \"parent\": \"plan_006_qwen3_1_7b_rsft_eval_r2\", \"metrics\": {\"n_predictions\": 28743, \"n_truncated\": 857, \"format_ok_rate\": 0.999, \"n_docs\": 1000, \"codalab_entries\": 27567}, \"conclusion\": \"success\"}, \"plan_006_qwen3_8b_rsft_test\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T15:30:36.092Z\", \"updated_at\": \"2026-05-17T19:01:47.602Z\", \"hypothesis\": \"Generate 8B RSFT test set predictions for CodaLab submission. 8B RSFT dev rel_f1=0.5606, expect similar performance on test.\", \"conclusion\": \"success\"}, \"plan_006_llama_rsft_seed43_eval_r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T16:03:41.592Z\", \"updated_at\": \"2026-05-17T18:48:55.143Z\", \"hypothesis\": \"Evaluate LLaMA-8B RSFT seed 43 on DocRED dev (retry with correct base_model path). Seed 42 gave rel_f1=0.5674. If seed 43 gives similar result (±1.5pp), the cross-architecture RSFT claim is robust against seed variance.\", \"parent\": \"plan_006_llama_rsft_seed43\", \"metrics\": {\"rel_f1\": 0.5727, \"ign_f1\": 0.5619, \"evi_f1\": 0.8206, \"evi_f1_joint\": 0.4551, \"edcr\": 0.6073, \"format_compliance_rate\": 1, \"n_truncated\": 197}, \"conclusion\": \"success\"}, \"plan_006_llama_rsft_test\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T15:30:42.159Z\", \"updated_at\": \"2026-05-17T18:37:51.441Z\", \"hypothesis\": \"Generate LLaMA-8B RSFT test set predictions for CodaLab submission. LLaMA-8B RSFT dev rel_f1=0.5674, expect similar performance on test.\", \"conclusion\": \"success\"}, \"plan_006_llama_rsft_seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T13:07:02.215Z\", \"updated_at\": \"2026-05-17T16:48:29.803Z\", \"hypothesis\": \"Validate LLaMA-8B RSFT robustness across seeds. Seed 42 gave rel_f1=0.5674 (+1.6pp over SFT baseline 0.5514). If seed 43 gives similar result, the cross-architecture RSFT claim is robust against seed variance.\", \"parent\": \"plan_016_llama_rsft_train_r3\", \"conclusion\": \"success\"}, \"plan_006_llama_rsft_seed43_eval\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T16:00:04.294Z\", \"updated_at\": \"2026-05-17T16:48:26.809Z\", \"hypothesis\": \"Evaluate LLaMA-8B RSFT seed 43 on DocRED dev. Seed 42 gave rel_f1=0.5674. If seed 43 gives similar result (±1.5pp, i.e., 0.55-0.58), the cross-architecture RSFT claim is robust against seed variance.\", \"parent\": \"plan_006_llama_rsft_seed43\", \"conclusion\": \"failed\"}, \"lead2_ckpt20_eval\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T12:31:32.202Z\", \"updated_at\": \"2026-05-17T15:27:15.598Z\", \"hypothesis\": \"Evaluate GRPO checkpoint-20 from RSFT base (lead2_rsft_grpo_ced_r2) on DocRED dev. If RSFT→GRPO preserves/improves rel_f1 over RSFT baseline (0.4601), it validates the RSFT→GRPO training pipeline as viable.\", \"parent\": \"lead2_rsft_grpo_ced_r2\", \"conclusion\": \"success\", \"metrics\": {\"rel_f1\": 0.4617, \"ign_f1\": 0.4533, \"evi_f1\": 0.8103, \"evi_f1_joint\": 0.3642, \"edcr\": 0.6465, \"precision\": 0.476, \"recall\": 0.4482, \"format_ok\": \"985/985\", \"truncated\": \"187/985\", \"predictions\": 14998}}, \"plan_006_qwen3_8b_rsft_eval\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T12:00:05.493Z\", \"updated_at\": \"2026-05-17T14:59:23.644Z\", \"hypothesis\": \"Evaluate Qwen3-8B RSFT (CED-scored data, 9041 samples) on DocRED dev. At 8B scale with near-zero evidence tax, CED-RSFT should achieve highest absolute Ign-F1 in the scaling study.\", \"parent\": \"plan_006_qwen3_8b_rsft_train_r2\", \"conclusion\": \"success\", \"metrics\": {\"f1\": 0.5606, \"ign_f1\": 0.5433, \"evi_f1\": 0.8052, \"evi_f1_joint\": 0.4413, \"edcr\": 0.6377, \"precision\": 0.5553, \"recall\": 0.566, \"format_ok\": \"985/985\", \"truncated\": \"267/985\", \"predictions\": 16831}}, \"plan_006_qwen3_1_7b_rsft_seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T13:01:14.254Z\", \"updated_at\": \"2026-05-17T14:25:12.839Z\", \"hypothesis\": \"RSFT with seed 43 on Qwen3-1.7B will produce comparable performance to other seeds, validating seed robustness for the scaling study\", \"parent\": \"plan_006_qwen3_1_7b_rsft_eval_r2\", \"conclusion\": \"success\", \"notes\": \"Training completed in 4795.7s (~1h20m). 1698 steps, 3 epochs. Final: train_loss=0.523, mean_token_accuracy=0.879, entropy=0.519. Final checkpoint: checkpoint-1698. Needs eval.\"}, \"post_hoc_bm25_baseline\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T13:01:00.344Z\", \"updated_at\": \"2026-05-17T13:02:03.821Z\", \"hypothesis\": \"Post-hoc BM25 evidence retrieval on SFT-no-evidence predictions: if retrieving evidence after RE produces comparable joint Evi-F1 and EDCR to jointly trained RSFT, then joint generation is unnecessary. Expect RSFT to have better evidence quality (lower EDCR) due to training-time evidence grounding.\", \"parent\": \"plan_014_sft_no_evidence\", \"conclusion\": \"success\", \"metrics\": {\"bm25_entity_k2_rel_f1\": 0.4876, \"bm25_entity_k2_evi_f1_joint\": 0.3473, \"bm25_entity_k2_edcr\": 0.7664, \"bm25_entity_k3_evi_f1_joint\": 0.2989, \"bm25_entity_k3_edcr\": 0.8256, \"bm25_oracle_k_evi_f1_joint\": 0.3834, \"bm25_oracle_k_edcr\": 0.7334, \"rsft_ced_s43_rel_f1\": 0.4601, \"rsft_ced_s43_evi_f1_joint\": 0.3605, \"rsft_ced_s43_edcr\": 0.6542, \"sft_joint_rel_f1\": 0.4049, \"sft_joint_evi_f1_joint\": 0.3147, \"sft_joint_edcr\": 0.6982, \"verdict\": \"RSFT joint generation beats BM25 post-hoc on evi_f1_joint (-1.3pp) and EDCR (-11.2pp). Even oracle-k post-hoc has 7.9pp worse EDCR than RSFT.\"}}, \"lead1_ced_evidence_filter\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T11:54:50.206Z\", \"updated_at\": \"2026-05-17T12:57:03.964Z\", \"conclusion\": \"negative\", \"hypothesis\": \"Post-hoc CED-based evidence filtering on RSFT predictions: removing low-NLI-score evidence sentences at inference time should improve Evi-F1 and EDCR by eliminating distractor citations, without affecting rel_f1.\", \"metrics\": {\"baseline_f1\": 0.4601, \"baseline_ign_f1\": 0.4512, \"baseline_evi_f1\": 0.8063, \"baseline_edcr\": 0.6542, \"tau_0.3_evi_f1\": 0.7301, \"tau_0.3_edcr\": 0.5797, \"tau_0.5_evi_f1\": 0.7297, \"tau_0.5_edcr\": 0.5784, \"tau_0.7_evi_f1\": 0.7287, \"tau_0.7_edcr\": 0.5776, \"evidence_kept_pct_tau_0.5\": 61.9, \"verdict\": \"CED filter removes ~38% evidence but drops Evi-F1 by 7.7pp and EDCR by 7.6pp\"}}, \"plan_006_qwen3_8b_rsft_train\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T05:57:56.689Z\", \"updated_at\": \"2026-05-17T08:25:26.201Z\", \"hypothesis\": \"RSFT with CED-scored data (9041 samples) on Qwen3-8B will improve rel_f1 over SFT baseline. At 8B scale with near-zero evidence tax, CED-filtered RSFT should achieve the highest absolute performance in the model scaling study.\", \"conclusion\": \"failed\"}, \"plan_006_qwen3_1_7b_rsft_eval\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T06:12:11.998Z\", \"updated_at\": \"2026-05-17T08:25:24.429Z\", \"hypothesis\": \"Evaluate 1.7B RSFT model on DocRED dev to measure rel_f1 improvement over SFT baseline. Validates that CED-filtered RSFT generalizes to smallest model scale (1.7B) in the scaling study.\", \"parent\": \"plan_006_qwen3_1_7b_rsft_train\", \"conclusion\": \"failed\"}, \"rsft_s44_dev_eval_preds\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T05:02:50.832Z\", \"updated_at\": \"2026-05-17T08:25:22.846Z\", \"hypothesis\": \"Re-run RSFT s44 dev eval with predictions saved, as prerequisite for CED evidence filtering experiment (线索1: inference-time distractor citation removal). Predictions needed for per-sentence NLI scoring.\", \"conclusion\": \"failed\"}, \"lead2_rsft_grpo_ced_r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T06:23:56.474Z\", \"updated_at\": \"2026-05-17T08:25:20.510Z\", \"hypothesis\": \"RSFT→bf16 GRPO two-stage (retry with --data_dir fix): starting from merged RSFT-s43 checkpoint (rel_f1=0.46), short-range GRPO (50 steps, lr=1e-6) with CED-only reward should improve evidence quality (EDCR) while preserving rel_f1.\", \"parent\": \"lead2_rsft_grpo_ced\", \"conclusion\": \"failed\"}, \"plan_016_llama_rsft_train_r3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T03:26:03.945Z\", \"updated_at\": \"2026-05-17T06:26:30.916Z\", \"hypothesis\": \"bf16 full-precision training with gradient checkpointing and batch_size=1 will fit within single RTX 5090 32GB VRAM while maintaining training quality comparable to QLoRA, resolving the OOM issues seen in r1/r2 attempts\", \"parent\": \"plan_016_llama_rsft_train_r2\", \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 0.3724, \"mean_token_accuracy\": 0.929, \"total_steps\": 3312, \"epochs\": 3, \"runtime_seconds\": 10231}}, \"lead2_rsft_grpo_ced\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T05:57:53.951Z\", \"updated_at\": \"2026-05-17T06:06:36.130Z\", \"hypothesis\": \"RSFT→bf16 GRPO two-stage: starting from RSFT best checkpoint (s43, rel_f1=0.46), short-range GRPO (50 steps, lr=1e-6) with CED-only reward should further improve evidence quality (EDCR) while preserving rel_f1, because RSFT provides stable base preventing catastrophic forgetting seen in SFT→GRPO.\", \"parent\": \"mvp2_rsft_train_r1_s43\", \"conclusion\": \"failed\"}, \"plan_006_qwen3_8b_ced_scoring\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T03:27:03.641Z\", \"updated_at\": \"2026-05-17T06:00:52.969Z\", \"hypothesis\": \"CED scoring on Qwen3-8B RSFT candidates (24216 gens from 3027 docs) will produce high-quality filtered training data. At 8B scale with near-zero evidence tax, CED-filtered RSFT should yield further gains over an already strong SFT baseline.\", \"parent\": \"plan_006_qwen3_8b_rsft_candidates_r2\", \"conclusion\": \"success\", \"metrics\": {\"output_samples\": 9041, \"input_candidates\": 24216, \"scoring_mode\": \"ced\", \"tau\": 0.5, \"top_k\": 3}}, \"plan_006_qwen3_1_7b_rsft_train\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T03:03:05.036Z\", \"updated_at\": \"2026-05-17T06:00:51.477Z\", \"hypothesis\": \"RSFT with CED-scored data on Qwen3-1.7B will improve relation extraction F1 over SFT baseline by selectively reinforcing high-quality extraction patterns, similar to gains seen on 4B model\", \"parent\": \"plan_006_qwen3_1_7b_ced_scoring\", \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 0.5234, \"eval_loss\": 0.8725, \"eval_mean_token_accuracy\": 0.8185, \"total_steps\": 1698, \"epochs\": 3, \"runtime_hours\": 2.25}}, \"plan_002_test_rsft_s44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T01:05:59.263Z\", \"updated_at\": \"2026-05-17T04:57:25.850Z\", \"hypothesis\": \"RSFT-CED s44 (best dev config, rel_f1=0.4655) maintains improvement over SFT on held-out test set, confirming CED-filtered rejection sampling gains are not dev-set overfitting. Test Ign-F1 should exceed SFT test baseline.\", \"parent\": \"mvp2_rsft_train_r1_s44\", \"conclusion\": \"success\"}, \"plan_006_qwen3_8b_rsft_candidates_r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T01:54:26.118Z\", \"updated_at\": \"2026-05-17T04:08:25.446Z\", \"hypothesis\": \"Resuming 8B candidate generation from idx 2701 will complete the full RSFT candidate set needed for reward-based filtering and RSFT training\", \"parent\": \"plan_006_qwen3_8b_rsft_candidates\", \"conclusion\": \"success\"}, \"plan_016_llama_rsft_train_r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T03:10:57.585Z\", \"updated_at\": \"2026-05-17T03:26:02.383Z\", \"hypothesis\": \"LLaMA-3.1-8B RSFT training retry with OOM fix: --no-quantize (bf16) + gradient_checkpointing. R1 OOM due to missing bf16 flag causing fp32 loading on 32GB card. 8829 CED-filtered samples, 3 epochs.\", \"parent\": \"plan_016_llama_rsft_train\", \"conclusion\": \"failed\"}, \"plan_016_llama_rsft_train\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T03:03:03.349Z\", \"updated_at\": \"2026-05-17T03:10:51.973Z\", \"hypothesis\": \"LLaMA-3.1-8B RSFT training on CED-filtered candidates (8829 samples, top_k=1) should improve rel_f1 over SFT baseline (0.5514), validating that the CED-RSFT pipeline generalizes across model families (Qwen→LLaMA).\", \"parent\": \"plan_016_llama_ced_scoring\", \"conclusion\": \"failed\"}, \"plan_016_llama_ced_scoring\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T01:38:57.773Z\", \"updated_at\": \"2026-05-17T03:05:35.479Z\", \"hypothesis\": \"CED scoring (NLI-based contrastive discrimination) on LLaMA-3.1-8B RSFT candidates will produce filtered training data that improves RSFT quality, consistent with Qwen3-4B CED results.\", \"parent\": \"plan_016_llama_rsft_candidates_r3\", \"conclusion\": \"success\"}, \"plan_006_qwen3_1_7b_ced_scoring\": {\"status\": \"DONE\", \"created_at\": \"2026-05-17T00:59:40.455Z\", \"updated_at\": \"2026-05-17T02:59:29.871Z\", \"hypothesis\": \"CED scoring (NLI contrastive discrimination) can effectively filter 1.7B model candidates despite lower generation quality: NLI-based selection should identify high-quality evidence samples even from a capacity-limited generator.\", \"parent\": \"plan_006_qwen3_1_7b_rsft_candidates\", \"conclusion\": \"success\", \"metrics\": {\"total_records\": 24216, \"selected\": 9042, \"unique_docs\": 3021, \"selection_rate\": 0.373, \"mean_f1_reward\": 0.592, \"mean_ced_reward\": 0.559, \"mean_combined_score\": 0.66, \"truncated_count\": 2920, \"truncated_mean_f1\": 0.439, \"non_truncated_mean_f1\": 0.613}}, \"plan_007_redocred_rsft_eval_r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T16:25:37.094Z\", \"updated_at\": \"2026-05-17T02:56:32.555Z\", \"metrics\": {\"F1\": 0.0025, \"Ign-F1\": 0.0026, \"Evi-F1\": 0.8837, \"EDCR\": 0.9978, \"format_ok\": \"489/493\", \"truncated\": \"117/493\", \"predictions\": 8461}, \"conclusion\": \"negative\", \"notes\": \"⚠️ NEGATIVE: F1=0.0025 (catastrophic), Evi-F1=0.8837, EDCR=0.9978. SFT baseline on same data = 0.3659 (normal). Framing 调整提案已提交 Director (2026-05-16). 大概率 pipeline bug (adapter loading / prompt format / relation label mapping). Diagnostic Worker dispatched. 等 Director 选 A/B/C narrative 再决定下一步。\", \"hypothesis\": \"CED-RSFT improvements on DocRED should transfer to Re-DocRED: RSFT model should outperform SFT baseline on Re-DocRED Ign-F1, demonstrating cross-dataset generalization of rejection sampling gains.\"}, \"plan_006_qwen3_1_7b_rsft_candidates\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T13:51:15.410Z\", \"updated_at\": \"2026-05-17T02:56:30.210Z\", \"hypothesis\": \"Qwen3-1.7B RSFT candidate generation (N=8, T=0.7). Scale ablation: smallest model RSFT candidates for CED scoring. plan_006 claim=3.\", \"conclusion\": \"success\", \"metrics\": {\"docs_completed\": 3027, \"total_generations\": 24216, \"lines\": 24216, \"runtime_h\": 11, \"truncation_rate\": 0.104, \"mean_diversity\": 7.4}, \"parent\": \"plan_006_qwen3_1_7b_sft_bf16\"}, \"plan_002_test_eval_s44_r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T08:14:36.494Z\", \"updated_at\": \"2026-05-17T02:56:29.283Z\", \"conclusion\": \"success\", \"hypothesis\": \"DocRED test set evaluation for RSFT-CED s44 (best dev config). Final benchmark numbers for paper submission; test set performance confirms dev set gains are not overfitting artifacts.\"}, \"plan_006_qwen3_8b_no_evidence_sft\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T09:30:57.988Z\", \"updated_at\": \"2026-05-17T02:56:26.471Z\", \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 0.6509, \"eval_loss\": 0.8153, \"eval_mean_token_accuracy\": 0.8174, \"eval_entropy\": 0.6275, \"train_runtime_sec\": 3656, \"epoch\": 3}, \"hypothesis\": \"Qwen3-8B no-evidence SFT baseline for evidence tax measurement at 8B scale. If 8B no-evi rel_f1 ≈ 8B evidence-SFT rel_f1, confirms that 8B absorbs evidence cost (tax≈0).\"}, \"plan_006_qwen3_1_7b_no_evidence_sft\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T07:32:23.806Z\", \"updated_at\": \"2026-05-17T02:56:15.512Z\", \"conclusion\": \"success\", \"hypothesis\": \"Qwen3-1.7B no-evidence SFT baseline for evidence tax measurement at 1.7B scale. Paired with evidence-SFT to quantify whether evidence generation constrains or helps small model RE performance.\"}, \"plan_006_qwen3_1_7b_sft_bf16\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T06:36:26.212Z\", \"updated_at\": \"2026-05-17T02:56:13.858Z\", \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 0.6884, \"eval_loss\": 0.8031, \"eval_mean_token_accuracy\": 0.8238, \"eval_entropy\": 0.682, \"train_runtime_sec\": 2473, \"train_samples_per_second\": 3.672, \"epochs\": 3, \"total_steps\": 570}, \"hypothesis\": \"Qwen3-1.7B bf16 LoRA SFT training for evidence-grounded DocRE. Scale ablation: smallest model expected to show highest evidence tax due to capacity-constrained multi-task optimization.\"}, \"plan_006_qwen3_8b_sft_bf16\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T07:50:55.793Z\", \"updated_at\": \"2026-05-17T02:56:12.064Z\", \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 0.5705, \"eval_loss\": 0.7186, \"eval_mean_token_accuracy\": 0.8377, \"eval_entropy\": 0.5614, \"train_runtime_s\": 3932, \"epoch\": 3}, \"notes\": \"训练正常完成，cron 误判(无W&B/sentinel)。Qwen3-8B bf16 LoRA SFT 3ep, train_loss=0.5705, eval_acc=0.8377。checkpoint: /root/autodl-tmp/sft_output_qwen3_8b_bf16。下一步: RSFT + eval。\", \"hypothesis\": \"Qwen3-8B bf16 LoRA SFT training for evidence-grounded DocRE. Scale ablation: larger model should achieve higher rel_f1 than 4B (0.4057) and 1.7B baselines, with lower evidence tax due to greater capacity.\"}, \"reeval_sft_baseline_d076\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T05:26:37.542Z\", \"updated_at\": \"2026-05-17T02:56:09.813Z\", \"conclusion\": \"success\", \"metrics\": {\"rel_f1\": 0.4049, \"ign_f1\": 0.3974, \"evi_f1\": 0.7986, \"edcr\": 0.6982, \"evi_f1_joint\": 0.3147, \"format_compliance_rate\": 0.998, \"n_truncated\": 288, \"n_documents\": 985, \"n_predictions\": 16880, \"inference_time_sec\": 7056.5}, \"hypothesis\": \"Re-eval Qwen3-4B SFT baseline under D076 unified protocol (batch_size=4, no-quantize, max_new_tokens=1024, seed=42). Required as canonical comparison point for all RSFT/GRPO experiments and evidence tax computation.\"}, \"plan_006_qwen3_1_7b_sft_eval\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T08:14:26.923Z\", \"updated_at\": \"2026-05-17T02:56:02.886Z\", \"conclusion\": \"success\", \"metrics\": {\"f1\": 0.4945, \"ign_f1\": 0.4786, \"evi_f1\": 0.8316, \"edcr\": 0.6704, \"precision\": 0.5085, \"recall\": 0.4813, \"ign_precision\": 0.483, \"ign_recall\": 0.4743, \"evi_precision\": 0.8203, \"evi_recall\": 0.8432, \"evi_f1_joint\": 0.3958, \"format_compliance_rate\": 1, \"n_predictions\": 17184, \"n_truncated\": 314, \"inference_time_seconds\": 6848.7}, \"hypothesis\": \"Qwen3-1.7B evidence-SFT eval under D076 protocol. Establishes smallest-scale SFT baseline; evidence tax at 1.7B predicted negative (evidence helps small models by constraining over-prediction).\", \"parent\": \"plan_006_qwen3_1_7b_sft_bf16\"}, \"plan_006_qwen3_8b_sft_eval\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T09:03:35.743Z\", \"updated_at\": \"2026-05-17T02:56:01.221Z\", \"conclusion\": \"success\", \"metrics\": {\"ign_f1\": 0.5051, \"f1\": 0.5262, \"evi_f1\": 0.8188, \"edcr\": 0.651, \"format_ok_rate\": 0.999, \"n_truncated\": 313, \"n_predictions\": 17401, \"inference_time_s\": 7206}, \"hypothesis\": \"Qwen3-8B evidence-SFT eval under D076 unified protocol. Establishes 8B-scale SFT baseline for evidence tax measurement (paired with no-evidence eval) and RSFT improvement quantification.\", \"parent\": \"plan_006_qwen3_8b_sft_bf16\"}, \"plan_016_llama_3_1_8b_no_evidence_sft\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T11:06:47.006Z\", \"updated_at\": \"2026-05-17T02:55:47.936Z\", \"conclusion\": \"success\", \"hypothesis\": \"LLaMA-3.1-8B no-evidence SFT baseline for cross-family evidence tax measurement. Paired with evidence-SFT to quantify evidence generation cost on a non-Qwen architecture at 8B scale.\"}, \"plan_016_llama_3_1_8b_sft\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T10:35:41.618Z\", \"updated_at\": \"2026-05-17T02:55:46.226Z\", \"conclusion\": \"success\", \"hypothesis\": \"LLaMA-3.1-8B can be SFT-trained for evidence-grounded DocRE with the same pipeline as Qwen3 family, enabling cross-family generalization claims for the FREIGE framework.\"}, \"plan_007_redocred_4b_sft_eval_r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T12:36:01.717Z\", \"updated_at\": \"2026-05-17T02:55:43.842Z\", \"metrics\": {\"ign_f1\": 0.3659, \"f1\": 0.3706, \"evi_f1\": 0.817, \"edcr\": 0.6674, \"format_compliance_rate\": 0.996, \"n_truncated\": 139, \"n_total\": 493, \"inference_time_seconds\": 3281.7, \"precision\": 0.4316, \"recall\": 0.3247, \"ign_precision\": 0.4134, \"ign_recall\": 0.3282, \"evi_precision\": 0.8208, \"evi_recall\": 0.8131, \"n_predictions\": 8191}, \"conclusion\": \"success\", \"hypothesis\": \"FREIGE SFT model trained on DocRED transfers to Re-DocRED without re-training: if Ign-F1 drop <5pp and Evi-F1 maintains, the learned evidence grounding generalizes across annotation schemes.\", \"parent\": \"reeval_sft_baseline_d076\"}, \"plan_006_qwen3_8b_no_evidence_eval_v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T11:17:39.361Z\", \"updated_at\": \"2026-05-17T02:55:34.661Z\", \"conclusion\": \"success\", \"hypothesis\": \"8B model capacity absorbs evidence generation cost: no-evidence SFT and evidence-SFT should produce near-identical rel_f1, demonstrating evidence tax≈0 at 8B scale (contrasting with 4B where tax=-7.5pp).\", \"parent\": \"plan_006_qwen3_8b_no_evidence_sft\"}, \"plan_016_llama_3_1_8b_no_evidence_eval\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T12:05:53.861Z\", \"updated_at\": \"2026-05-17T02:55:31.810Z\", \"conclusion\": \"success\", \"metrics\": {\"ign_f1\": 0.5452, \"rel_f1\": 0.5624, \"evi_f1\": 0, \"edcr\": 0}, \"hypothesis\": \"LLaMA-3.1-8B no-evidence SFT should achieve similar rel_f1 to evidence-SFT (tax≈0), cross-family validating the 8B-scale evidence absorption pattern observed in Qwen3-8B.\", \"parent\": \"plan_016_llama_3_1_8b_no_evidence_sft\"}, \"plan_006_qwen3_1_7b_no_evidence_eval_v3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T11:45:02.749Z\", \"updated_at\": \"2026-05-17T02:55:24.084Z\", \"conclusion\": \"success\", \"metrics\": {\"ign_f1\": 0.3982, \"rel_f1\": 0.4103, \"evi_f1\": 0, \"edcr\": 0, \"precision\": 0.4464, \"recall\": 0.3796, \"format_compliance_rate\": 1, \"n_truncated\": 501, \"inference_time_seconds\": 7465.3, \"evidence_tax\": 0.0804}, \"hypothesis\": \"1.7B model capacity is insufficient to jointly optimize RE and evidence generation: no-evidence SFT should outperform evidence-SFT on rel_f1, revealing positive evidence tax at small scale (opposite to 8B where tax≈0).\", \"parent\": \"plan_006_qwen3_1_7b_no_evidence_sft\"}, \"plan_016_llama_3_1_8b_sft_eval\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T12:06:49.282Z\", \"updated_at\": \"2026-05-17T02:55:20.475Z\", \"metrics\": {\"ign_f1\": 0.5384, \"rel_f1\": 0.5514, \"evi_f1\": 0.8151, \"edcr\": 0.628, \"precision\": 0.5464, \"recall\": 0.5565, \"evi_f1_joint\": 0.4317, \"format_compliance_rate\": 0.9949, \"n_truncated\": 197, \"n_predictions\": 15325, \"inference_time_seconds\": 7331.3, \"evidence_tax_ign_f1\": 0.0068, \"evidence_tax_rel_f1\": 0.011}, \"conclusion\": \"success\", \"hypothesis\": \"LLaMA-3.1-8B SFT with evidence generation should achieve comparable rel_f1 to Qwen3-8B SFT, establishing cross-family baseline for evidence tax measurement. Evidence tax at 8B scale predicted near-zero based on Qwen3-8B pattern.\", \"parent\": \"plan_016_llama_3_1_8b_sft\"}, \"plan_016_llama_grpo_qlora\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T13:14:37.199Z\", \"updated_at\": \"2026-05-17T02:55:08.871Z\", \"conclusion\": \"success\", \"metrics\": {\"format_reward\": 1, \"f1_reward\": 0, \"ced_reward\": 0, \"entropy\": 0.28, \"final_step\": 60, \"grad_norm\": 0, \"loss\": 0, \"frac_reward_zero_std\": 1, \"output_length_final\": 172, \"conclusion_note\": \"C2 cross-family validated: LLaMA QLoRA GRPO shows same catastrophic decoupling as Qwen (format gaming, zero IE ability)\"}, \"hypothesis\": \"QLoRA GRPO catastrophic decoupling (format gaming + zero IE ability) is not Qwen-specific: LLaMA-3.1-8B under identical QLoRA GRPO training should exhibit the same failure mode (grad_norm→0, loss→0, rel_f1→0). Cross-family validation of C2.\", \"parent\": \"mvp2_grpo_ced_lr5e6_r1\"}, \"plan_006_qwen3_8b_rsft_candidates\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T13:49:52.476Z\", \"updated_at\": \"2026-05-17T01:54:20.630Z\", \"hypothesis\": \"Qwen3-8B RSFT candidate generation (N=8, T=0.7). Generates rejection sampling candidates for subsequent CED scoring and filtering. plan_006 claim=3.\", \"conclusion\": \"failed\"}, \"plan_016_llama_rsft_candidates_r3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T15:49:40.224Z\", \"updated_at\": \"2026-05-17T01:34:30.186Z\", \"hypothesis\": \"LLaMA-3.1-8B RSFT candidate gen r3 (N=8, T=0.7, start_idx=64 resume). Exclusive cuda:2 after GRPO kill.\", \"parent\": \"plan_016_llama_3_1_8b_sft\", \"conclusion\": \"success\"}, \"plan_007_redocred_rsft_eval_r5\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T22:04:18.834Z\", \"updated_at\": \"2026-05-17T00:51:25.706Z\", \"hypothesis\": \"CED-RSFT gains transfer to Re-DocRED (r5, correct 3-param loading: base→SFT→RSFT)\", \"parent\": \"plan_007_redocred_rsft_eval_r4\", \"conclusion\": \"success\", \"metrics\": {\"f1\": 0.4234, \"ign_f1\": 0.4145, \"evi_f1\": 0.8182, \"edcr\": 0.621, \"evi_joint_f1\": 0.3306, \"format_compliance\": 1, \"field_compliance\": 0.8134, \"n_documents\": 493, \"n_truncated\": 90, \"inference_time_s\": 5655.5}}, \"plan_007_redocred_rsft_eval_r4\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T18:00:41.999Z\", \"updated_at\": \"2026-05-16T22:04:01.953Z\", \"hypothesis\": \"CED-RSFT gains transfer to Re-DocRED (r4, correct 3-param loading: base→SFT→RSFT)\", \"parent\": \"plan_007_redocred_4b_sft_eval_r2\", \"conclusion\": \"failed\"}, \"plan_002_test_rsft_s43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T17:45:04.744Z\", \"updated_at\": \"2026-05-16T21:07:17.492Z\", \"conclusion\": \"failed\"}, \"plan_007_redocred_rsft_eval_r3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T17:38:09.825Z\", \"updated_at\": \"2026-05-16T21:07:14.348Z\", \"hypothesis\": \"Re-DocRED RSFT eval r3 (config fix: model_path=base, sft_adapter=RSFT ckpt). Verify CED-RSFT gains transfer cross-dataset.\", \"parent\": \"plan_007_redocred_4b_sft_eval_r2\", \"conclusion\": \"failed\"}, \"plan_007_redocred_rsft_eval\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T14:23:56.999Z\", \"updated_at\": \"2026-05-16T17:49:00.578Z\", \"conclusion\": \"failed\", \"metrics\": {\"failure_reason\": \"OOM + pipeline bug: --model_path and --sft_adapter args in wrong order. RSFT LoRA merged to bare Qwen3-4B without SFT base, causing ontology collapse. Fix: match DocRED eval param ordering.\"}}, \"plan_014_no_evidence_eval_d076\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T14:26:29.748Z\", \"updated_at\": \"2026-05-16T17:37:09.823Z\", \"hypothesis\": \"4B no-evidence SFT eval under D076 unified protocol (batch_size=4, max_new_tokens=1024, seed=42, no-quantize). Required for clean scaling comparison across 1.7B/4B/8B.\", \"parent\": \"plan_014_sft_no_evidence\", \"metrics\": {\"ign_f1\": 0.4721, \"f1\": 0.4876, \"precision\": 0.4901, \"recall\": 0.4851, \"format_compliance_rate\": 0.9929, \"n_truncated\": 307, \"inference_time_seconds\": 6903.9}, \"conclusion\": \"success\"}, \"plan_016_llama_rsft_candidates_r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T14:25:55.343Z\", \"updated_at\": \"2026-05-16T14:56:53.198Z\", \"hypothesis\": \"LLaMA-3.1-8B RSFT candidate generation (N=8, T=0.7) for cross-family CED-RSFT validation\", \"conclusion\": \"failed\", \"metrics\": {\"docs_completed\": 64, \"docs_total\": 3027, \"lines_generated\": 512, \"output_path\": \"/root/autodl-tmp/freige/outputs/rsft_candidates_llama_8b/generations.jsonl\", \"failure_reason\": \"Process killed externally (no traceback/error in log). Likely OOM on cuda:1. Completed 64/3027 docs (2.1%) in ~23min before termination.\"}}, \"plan_016_llama_rsft_candidates\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T14:15:59.880Z\", \"updated_at\": \"2026-05-16T14:25:29.851Z\", \"conclusion\": \"failed\", \"hypothesis\": \"LLaMA-3.1-8B RSFT candidate generation (N=8, T=0.7) for cross-family CED-RSFT validation\"}, \"plan_007_redocred_4b_sft_eval\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T12:30:55.473Z\", \"updated_at\": \"2026-05-16T12:34:54.050Z\", \"conclusion\": \"failed\", \"notes\": \"诊断: 两个路径均不存在——(1) 基座模型 /root/autodl-tmp/models/Qwen/Qwen3-4B/ 未下载（服务器只有 Qwen3-1.7B 和 Qwen3-8B）；(2) SFT adapter /root/autodl-tmp/sft_output_qwen3_4b/ 不存在（4B 模型未训练过）。inference.py 加载 tokenizer 时因本地路径不存在回退到 HF Hub 查找，触发 HFValidationError。\\n修复: (1) 先下载 Qwen3-4B 模型到 /root/autodl-tmp/models/Qwen/Qwen3-4B/；(2) 用该模型完成 SFT 训练生成 adapter；(3) 再重新提交 eval。\"}, \"plan_006_qwen3_1_7b_no_evidence_eval_v2r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T12:02:28.162Z\", \"updated_at\": \"2026-05-16T12:28:44.616Z\", \"conclusion\": \"failed\"}, \"plan_006_qwen3_1_7b_no_evidence_eval_v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T11:40:29.706Z\", \"updated_at\": \"2026-05-16T11:44:58.762Z\", \"conclusion\": \"failed\", \"notes\": \"失败原因: tmux 用 sh 执行命令, python 不在 PATH (需 bash -c 包装 conda activate). wall_clock=14s, 未产出任何数据. 已自动重提交为 v3.\"}, \"plan_006_qwen3_1_7b_no_evidence_eval\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T09:25:53.604Z\", \"updated_at\": \"2026-05-16T11:17:18.299Z\", \"conclusion\": \"failed\", \"metrics\": {\"f1\": 0.3884, \"ign_f1\": 0.3786, \"evi_f1\": 0.0007, \"edcr\": 0.9848, \"precision\": 0.4282, \"recall\": 0.3553, \"pred_count\": 27049, \"n_truncated\": 531, \"format_ok_rate\": 0.999}}, \"plan_006_qwen3_8b_no_evidence_eval\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T11:12:04.565Z\", \"updated_at\": \"2026-05-16T11:16:54.766Z\", \"conclusion\": \"killed\"}, \"reeval_flat_nli_s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T02:38:03.120Z\", \"updated_at\": \"2026-05-16T10:14:04.270Z\", \"hypothesis\": \"Re-eval flat-NLI RSFT s42 with unified protocol: batch_size=4 + --no-quantize + --sft_adapter + max_new_tokens=1024. 原 eval_plan_001_flat_nli 用了 batch_size=16。Paired t-test 关键路径。\", \"parent\": \"plan_001_rsft_flat_nli\", \"conclusion\": \"success\", \"metrics\": {\"ign_f1\": 0.4448, \"rel_f1\": 0.4535, \"evi_f1\": 0.8039, \"evi_f1_joint\": 0.3558, \"edcr\": 0.6458, \"format_compliance_rate\": 1, \"field_compliance_rate\": 0.7787, \"n_truncated\": 205, \"inference_time_seconds\": 13253.1}}, \"reeval_ced_s44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T02:38:00.052Z\", \"updated_at\": \"2026-05-16T10:14:02.479Z\", \"hypothesis\": \"Re-eval CED RSFT s44 with unified protocol: batch_size=4 + --no-quantize + --sft_adapter + max_new_tokens=1024 + seed=44. 原 eval 用了 batch_size≈16 且 seed=42（错误）。Paired t-test 关键路径。\", \"parent\": \"mvp2_rsft_train_r1_s44\", \"notes\": \"正确 checkpoint: /root/autodl-tmp/rsft_output_s44/checkpoint-510。旧 eval 路径一致但可能用了根目录 adapter 而非 checkpoint-510 子目录。\", \"conclusion\": \"success\", \"metrics\": {\"ign_f1\": 0.4511, \"rel_f1\": 0.4621, \"evi_f1\": 0.805, \"evi_f1_joint\": 0.3677, \"edcr\": 0.635, \"format_compliance_rate\": 1, \"field_compliance_rate\": 0.802, \"n_truncated\": 190, \"inference_time_seconds\": 13077.6}}, \"reeval_ced_s42\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T02:37:58.498Z\", \"updated_at\": \"2026-05-16T10:14:00.520Z\", \"hypothesis\": \"Re-eval CED RSFT s42 with unified protocol: batch_size=4 + --no-quantize + --sft_adapter + max_new_tokens=1024. 原 mvp2_eval_rsft_r2b_maxtok1536_r2 用了 batch_size=8 + max_new_tokens=1536。Paired t-test 关键路径。\", \"parent\": \"mvp2_rsft_train_r1\", \"notes\": \"旧 eval (rsft_r2b_maxtok1536_r2) 不仅协议不一致，而且用了错误 checkpoint (rsft_output_r2b: lora_alpha=32, 仅 160 步)。正确 checkpoint: /root/autodl-tmp/rsft_output/checkpoint-510 (seed=42, lora_alpha=128, 510 步，与 s43/s44/s45 配置一致)。\", \"conclusion\": \"success\", \"metrics\": {\"ign_f1\": 0.4423, \"rel_f1\": 0.4517, \"evi_f1\": 0.8175, \"evi_f1_joint\": 0.3518, \"edcr\": 0.6569, \"format_compliance_rate\": 1, \"field_compliance_rate\": 0.7756, \"n_truncated\": 214, \"inference_time_seconds\": 10815.5}}, \"reeval_flat_nli_s44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T08:56:36.565Z\", \"updated_at\": \"2026-05-16T09:26:04.920Z\", \"conclusion\": \"killed\"}, \"plan_006_qwen3_1_7b_sft\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T06:13:52.388Z\", \"updated_at\": \"2026-05-16T06:33:46.578Z\", \"conclusion\": \"killed\"}, \"reeval_flat_nli_s43_r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T02:32:45.507Z\", \"updated_at\": \"2026-05-16T06:10:14.112Z\", \"hypothesis\": \"Re-eval flat-NLI RSFT s43 with unified protocol: batch_size=4 + --no-quantize + --sft_adapter + --max_new_tokens 1024. 原 reeval_flat_nli_s43 用了 batch_size=16 导致协议不一致。C3 paired t-test 关键路径。\", \"metrics\": {\"rel_f1\": 0.4586, \"rel_precision\": 0.4732, \"rel_recall\": 0.4449, \"ign_f1\": 0.4503, \"evi_f1\": 0.8113, \"evi_precision\": 0.8035, \"evi_recall\": 0.8192, \"evi_f1_joint\": 0.358, \"edcr\": 0.6552, \"format_ok_rate\": 0.999, \"n_truncated\": 184, \"n_predictions\": 15015}, \"conclusion\": \"success\"}, \"eval_rsft_ced_s45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T01:30:34.036Z\", \"updated_at\": \"2026-05-16T05:43:12.975Z\", \"hypothesis\": \"Full dev eval of CED RSFT seed=45 with --sft_adapter + --no-quantize. Paired t-test 关键路径：CED 第 3 个 seed（s42/s44 已有，s43 训练中）。对比 flat-NLI RSFT seeds。plan_id=plan_mvp2_rsft, claim=3。\", \"parent\": \"rsft_ced_s45_train_r4\", \"notes\": \"[2026-05-16 02:18 UTC] 69/247 batches (28%), ~2h remaining. ETA ~04:18 UTC. Running normally at ~41s/it avg.\", \"conclusion\": \"success\", \"metrics\": {\"rel_f1\": 0.4514, \"ign_f1\": 0.4416, \"evi_f1\": 0.8174, \"rel_p\": 0.4718, \"rel_r\": 0.4326, \"edcr\": 0.655, \"evi_f1_joint\": 0.3558, \"n_truncated\": 206, \"format_ok_rate\": 1}}, \"eval_rsft_ced_s43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T01:30:37.978Z\", \"updated_at\": \"2026-05-16T05:18:59.781Z\", \"hypothesis\": \"Full dev eval of CED RSFT seed=43 with --sft_adapter + --no-quantize. Paired t-test 关键路径：CED 第 4 个 seed。对比 flat-NLI RSFT seeds。plan_id=plan_mvp2_rsft, claim=3。\", \"parent\": \"rsft_ced_s43_train_r3\", \"notes\": \"[2026-05-16 02:18 UTC] 5/247 batches (2%), ~3h remaining. ETA ~05:19 UTC. Just started, running normally at ~45s/it avg.\", \"metrics\": {\"rel_f1\": 0.4601, \"ign_f1\": 0.4512, \"precision\": 0.4696, \"recall\": 0.4509, \"evi_f1\": 0.8063, \"evi_precision\": 0.8025, \"evi_recall\": 0.8101, \"edcr\": 0.6542, \"evi_f1_joint\": 0.3605, \"format_ok_rate\": 1, \"n_truncated\": 184, \"n_predictions\": 15051, \"inference_time_seconds\": 10768.2}, \"conclusion\": \"success\"}, \"eval_plan_014_no_evidence_r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T01:34:45.302Z\", \"updated_at\": \"2026-05-16T04:20:13.358Z\", \"hypothesis\": \"Retry of eval_plan_014_no_evidence with corrected command: --model_path 传底座 Qwen3-4B, --sft_adapter 传 SFT no-evidence adapter。修复 adapter 检测逻辑冲突。plan_id=plan_014, claim=1。\", \"parent\": \"plan_014_sft_no_evidence\", \"metrics\": {\"rel_f1\": 0.4876, \"ign_f1\": 0.4721, \"evi_f1\": 0, \"edcr\": 0, \"evi_f1_joint\": 0, \"precision\": 0.4901, \"recall\": 0.4851, \"ign_precision\": 0.4654, \"ign_recall\": 0.4791, \"format_compliance\": 0.993, \"truncation_rate\": 0.312, \"n_predictions\": 21181, \"n_documents\": 985}, \"conclusion\": \"success\"}, \"mvp2_ced_reranker_poc\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T07:55:03.414Z\", \"updated_at\": \"2026-05-16T03:49:41.385Z\", \"hypothesis\": \"CED-as-reranker: no fine-tuning, use CED to select best of N=8 SFT candidates at inference time. If rel_f1 > 0.4057 (SFT greedy), CED adds value without training risk. Oracle reranker as upper bound.\", \"conclusion\": \"success\", \"metrics\": {\"ced_reranker_rel_f1\": 0.486367, \"ced_reranker_ign_f1\": 0.473634, \"ced_reranker_evi_f1\": 0.8188, \"oracle_rel_f1\": 0.623746, \"oracle_ign_f1\": 0.612518, \"random_rel_f1\": 0.453783, \"random_ign_f1\": 0.439677}, \"notes\": \"CED reranker (N=8, no training) rel_f1=0.4864, 超过 SFT greedy (+8.07pp) 和 RSFT 3-seed mean (+2.68pp)。Oracle 上界 rel_f1=0.6237 (+21.8pp vs SFT)，CED reranker 实现了 oracle ceiling 的 37% (0.0807/0.218)。CED-F1 Spearman r=0.3235 (p≈0)，相关性显著但中等——说明 CED 不是完美的 proxy 但有信号。Random baseline rel_f1=0.4538 说明 sampling diversity 本身就有 +4.8pp 收益，CED 在此基础上再加 +3.3pp。EDCR 下降 (0.6156 vs SFT 0.7118)，N=8 sampling 引入更多 distractor citations。推理耗时 5.8h (N=8 生成主导)。结论：CED 作为 inference-time reranker 有明确论文价值——零训练成本超越 RSFT，且 oracle ceiling 表明更好的 reward model 还有大幅空间。\"}, \"eval_flat_nli_seed45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T23:12:39.186Z\", \"updated_at\": \"2026-05-16T03:49:36.608Z\", \"hypothesis\": \"Full dev eval of flat-NLI RSFT seed=45 checkpoint WITH --sft_adapter。seed45 中间 eval rel_f1=0.4876（待全量确认）。对比 CED RSFT mean (0.4596)。三 seed 全量 eval 出齐后汇报 flat-NLI vs CED RSFT 完整 seed-level 对比。\", \"parent\": \"plan_001_flat_nli_seed45\", \"notes\": \"[2026-05-16 02:18 UTC] 196/247 batches (79%), ~45min remaining. ETA ~03:03 UTC. Running normally at ~47s/it avg.\", \"metrics\": {\"rel_f1\": 0.455052, \"ign_f1\": 0.446181, \"evi_f1\": 0.815399, \"edcr\": 0.652133, \"evi_f1_joint\": 0.355612}, \"conclusion\": \"success\"}, \"eval_flat_nli_s44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T23:14:05.010Z\", \"updated_at\": \"2026-05-16T03:49:35.610Z\", \"hypothesis\": \"Full dev eval of flat-NLI RSFT seed=44 with --sft_adapter + --no-quantize. C3 统计显著性数据点 (s42=0.4539, s43 pending, s44 本次, s45 pending)。\", \"parent\": \"plan_001_flat_nli_seed44\", \"notes\": \"[2026-05-16 02:18 UTC] 238/247 batches (96%), ~7min remaining. ETA ~02:25 UTC. Running normally at ~45s/it avg.\", \"conclusion\": \"success\", \"metrics\": {\"rel_f1\": 0.461506, \"ign_f1\": 0.452126, \"evi_f1\": 0.813123, \"edcr\": 0.645808, \"evi_f1_joint\": 0.359673}}, \"rsft_ced_s45_train_r4\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T00:33:12.797Z\", \"updated_at\": \"2026-05-16T02:15:34.043Z\", \"hypothesis\": \"CED RSFT seed=45 训练（r4 重试，r3 因 cuda:2 orphan PID 276148 OOM 失败）。补全 paired t-test 所需的第 3 个 CED seed（现有 s42/s44，s43 在 cuda:1 训练中）。训练数据 2718 samples，3 epochs，~2h。plan_id=plan_mvp2_rsft, claim=3。\", \"parent\": \"\", \"conclusion\": \"success\", \"metrics\": {\"training_completed\": true, \"checkpoint\": \"checkpoint-510\", \"note\": \"Training metrics not captured (r4 retry after OOM). Eval running as eval_rsft_ced_s45.\"}}, \"rsft_ced_s43_train_r3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T00:20:57.272Z\", \"updated_at\": \"2026-05-16T02:14:46.064Z\", \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 0.6151, \"eval_loss\": 0.7618, \"task_eval_f1\": 0.5026, \"task_eval_ign_f1\": 0.4932, \"task_eval_evi_f1\": 0.7624, \"task_eval_edcr\": 0.6516, \"total_steps\": 510, \"epochs\": 3, \"training_hours\": 1.82}}, \"eval_plan_014_no_evidence\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T23:17:32.011Z\", \"updated_at\": \"2026-05-16T01:34:06.402Z\", \"hypothesis\": \"Dev set eval of SFT-no-evidence model (plan_014). 核心目标：对比标准 SFT rel_f1=0.4057 vs 不输出 evidence 的 SFT rel_f1（隔离 evidence generation 代价）。只评估 rel_f1，不评估 evi_f1（输出无 evidence）。plan_id=plan_014, claim=1。\", \"parent\": \"plan_014_sft_no_evidence\", \"conclusion\": \"failed\", \"notes\": \"FAILED: ValueError — model_path 含 adapter_config.json 触发 adapter 检测逻辑，要求 --sft_adapter。诊断(Worker diagnose_eval_plan_014): SFT adapter 本身就是 model_path，不应走 adapter stacking 路径。修复：--model_path 改传底座 Qwen3-4B，--sft_adapter 传 /root/autodl-tmp/sft_no_evidence_output。待 GPU 空闲后以 corrected command 重试。\"}, \"rsft_ced_s45_train_r3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T00:21:01.099Z\", \"updated_at\": \"2026-05-16T00:31:23.730Z\", \"conclusion\": \"failed\", \"notes\": \"CUDA OOM at launch: cuda:2 occupied by orphan PID 276148 (31.6GB). Need to kill orphan and resubmit as r4.\"}, \"rsft_ced_s45_train_r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T00:09:11.100Z\", \"updated_at\": \"2026-05-16T00:25:40.284Z\", \"conclusion\": \"killed\", \"notes\": \"Director 下令终止——错误套用 flat-NLI 超参(batch=1/grad_accum=16)，需用 CED 正确模板(batch=4/grad_accum=4)重跑，已由 r3 替代。\"}, \"rsft_ced_s43_train_r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T00:09:34.266Z\", \"updated_at\": \"2026-05-16T00:25:38.818Z\", \"hypothesis\": \"CED RSFT seed=43 训练（r2 重试，修正 cwd 错误）。补全 paired t-test 所需的第 3 个 CED seed（现有 s42/s44）。训练数据 2718 samples，3 epochs，~2h。plan_id=plan_mvp2_rsft, claim=3。\", \"parent\": \"rsft_ced_s43_train\", \"conclusion\": \"failed\", \"notes\": \"Director 下令终止——错误套用 flat-NLI 超参(batch=1/grad_accum=16)，需用 CED 正确模板(batch=4/grad_accum=4)重跑，已由 r3 替代。实际 argparse 无 --batch/--grad_accum 参数，静默忽略后用了默认值(batch=4/grad_accum=4)，实际配置恰好正确，但命令不规范。\"}, \"reeval_rsft_topk3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T22:00:34.722Z\", \"updated_at\": \"2026-05-16T00:24:22.091Z\", \"hypothesis\": \"Re-eval RSFT top_k=3 WITH --sft_adapter (D064 bug fix). 原 eval_plan_008_rsft_topk3 因缺 --sft_adapter 被 killed。对比 CED RSFT top_k=1 (rel_f1≈0.46) 和 SFT baseline (0.4057)。\", \"parent\": \"plan_008_rsft_topk3\", \"metrics\": {\"rel_f1\": 0.4454, \"rel_precision\": 0.4512, \"rel_recall\": 0.4398, \"ign_f1\": 0.4364, \"evi_f1\": 0.8088, \"edcr\": 0.6635, \"format_ok_rate\": 0.999, \"n_truncated\": 214, \"n_predictions\": 16020, \"inference_time_seconds\": 3546.4, \"ign_f1_corrected\": true}, \"conclusion\": \"negative\", \"notes\": \"RSFT top_k=3 rel_f1=0.4454，优于 SFT baseline (0.4057) 但劣于 CED RSFT top_k=1 (~0.46)。top_k=3 引入更多噪声训练样本，反而降低关系抽取精度。evi_f1=0.8088 较好。214/985 truncated。\"}, \"rsft_ced_s43_train\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T00:05:46.635Z\", \"updated_at\": \"2026-05-16T00:10:42.131Z\", \"conclusion\": \"failed\", \"notes\": \"失败原因: No module named freige.training.rsft_trainer — 命令 cd /root/autodl-tmp/freige 导致 cwd 错误。已修正为 cd /root/autodl-tmp，重提交为 rsft_ced_s43_train_r2 (PID=275264)\"}, \"rsft_ced_s45_train\": {\"status\": \"DONE\", \"created_at\": \"2026-05-16T00:03:17.851Z\", \"updated_at\": \"2026-05-16T00:05:24.862Z\", \"conclusion\": \"killed\"}, \"reeval_flat_nli_s43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T22:00:33.691Z\", \"updated_at\": \"2026-05-15T23:59:33.440Z\", \"hypothesis\": \"Re-eval flat-NLI RSFT seed=43 WITH --sft_adapter (D064 bug fix). 原 eval_plan_001_flat_nli_s43 因缺 --sft_adapter 导致 rel_f1=0.0022 无效。对比 flat-NLI s42 (rel_f1=0.4539) 和 CED RSFT mean (0.4596)。\", \"parent\": \"plan_001_flat_nli_seed43\", \"metrics\": {\"rel_f1\": 0.4523, \"ign_f1\": 0.4523, \"evi_f1\": 0.8158, \"edcr\": 0.6505, \"num_preds\": 15357, \"format_ok\": \"984/985\", \"truncated\": \"211/985\", \"inference_time_s\": 3515.8}, \"conclusion\": \"success\"}, \"plan_003_edcr_diagnostic\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T23:12:40.174Z\", \"updated_at\": \"2026-05-15T23:52:05.506Z\", \"hypothesis\": \"EDCR cross-method diagnostic table: 计算所有 evidence-producing 方法（SFT baseline, RSFT-CED best, RSFT-flatNLI best, CED-reranker）的 EDCR，验证 EDCR 作为独立评估指标的诊断能力。plan_id=plan_003, claim=4。GPU 预算 2h。\", \"conclusion\": \"success\", \"metrics\": {\"methods_evaluated\": 15, \"edcr_vs_rel_f1_spearman\": -0.9648, \"edcr_vs_rel_f1_pvalue\": 0.0001, \"edcr_vs_evi_f1_spearman\": 0.0022, \"edcr_vs_evi_f1_pvalue\": 0.9941, \"edcr_range\": \"0.63-0.99\", \"unique_diagnostic_value\": \"identifies pathological models (GRPO QLoRA) with high evi_f1 but catastrophically low rel_f1\"}}, \"eval_flat_nli_seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T23:12:38.199Z\", \"updated_at\": \"2026-05-15T23:48:28.074Z\", \"hypothesis\": \"Full dev eval of flat-NLI RSFT seed=44 with --sft_adapter + --no-quantize. C3 seed-level comparison.\", \"parent\": \"plan_001_flat_nli_seed44\", \"conclusion\": \"killed\"}, \"eval_plan_012_dpo_1ep_fixed_r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T21:58:52.440Z\", \"updated_at\": \"2026-05-15T23:44:56.586Z\", \"conclusion\": \"negative\", \"metrics\": {\"rel_f1\": 0.4034, \"evi_f1\": 0.8088, \"edcr\": 0.7139, \"format_ok_rate\": 0.999, \"truncated_rate\": 0.343, \"predictions\": 19107, \"ign_f1\": 0.4034, \"precision\": 0.3809, \"recall\": 0.4287, \"vs_sft_delta\": -0.0023, \"note\": \"DPO 1ep matches SFT baseline. 1ep→3ep trajectory shows gradual decoupling (rel_f1↓ evi_f1↑), consistent with GRPO pattern. Ign-F1=F1 exact match needs investigation.\"}}, \"plan_001_flat_nli_seed44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T21:38:26.174Z\", \"updated_at\": \"2026-05-15T23:25:30.719Z\", \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 0.6247, \"eval_loss\": 0.7564, \"eval_mean_token_accuracy\": 0.8299, \"task_eval_f1_ep1\": 0.4306, \"task_eval_f1_ep2\": 0.4884, \"task_eval_f1_ep3\": 0.4897, \"task_eval_evi_f1_ep3\": 0.78, \"task_eval_edcr_ep3\": 0.6596, \"task_eval_ign_f1_ep3\": 0.4897, \"train_runtime_sec\": 6197, \"num_epochs\": 3, \"total_steps\": 507}}, \"plan_009_dynamics_figure\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T23:17:30.987Z\", \"updated_at\": \"2026-05-15T23:19:12.282Z\", \"hypothesis\": \"GRPO forgetting dynamics 3-panel figure: QLoRA vs BF16 GRPO 的 rel_f1/evi_f1/EDCR 训练轨迹对比。支撑 Claim 3 (task decoupling 是 QLoRA-specific)。plan_id=plan_009。\", \"conclusion\": \"success\"}, \"plan_001_flat_nli_seed45\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T21:09:05.195Z\", \"updated_at\": \"2026-05-15T23:17:29.971Z\", \"conclusion\": \"success\", \"metrics\": {\"task_eval_rel_f1\": 0.4876, \"task_eval_evi_f1\": 0.7927, \"task_eval_edcr\": 0.6517, \"train_loss\": 0.6245, \"runtime_hours\": 1.69, \"note\": \"task-eval on 50 docs only, full dev eval needed\"}}, \"plan_011_bf16_g8_step_eval\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T19:04:51.538Z\", \"updated_at\": \"2026-05-15T23:01:09.970Z\", \"notes\": \"诊断确认：SIGTERM (EXIT_CODE=143)。device_map=\\\"auto\\\" 无 CUDA_VISIBLE_DEVICES 限制，模型加载到 GPU 0（plan_001 占用 16.3GB），双进程共 31.4/32.6GB 后被 kill。两次重试均失败（retry_count=2）。修复：CUDA_VISIBLE_DEVICES=1 重提交到空闲 cuda:1。\", \"conclusion\": \"success\", \"metrics\": {\"step_30\": {\"rel_f1\": 0.434, \"evi_f1\": 0.8063, \"edcr\": 0.6807}, \"step_50\": {\"rel_f1\": 0.4276, \"evi_f1\": 0.8024, \"edcr\": 0.6855}, \"step_70\": {\"rel_f1\": 0.4341, \"evi_f1\": 0.8099, \"edcr\": 0.6685}, \"best_step\": \"step_70\", \"trend\": \"non-monotonic, all < ckpt-100 (0.4549)\"}}, \"plan_011_eval_g8_bf16_ckpt100\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T14:43:24.143Z\", \"updated_at\": \"2026-05-15T22:06:28.981Z\", \"conclusion\": \"killed\", \"notes\": \"STALE: 该 eval 已由 eval_grpo_g8_bf16 完成并 success (rel_f1=0.4549)。此条目为残留，不需要执行。\"}, \"mvp2_eval_rsft_s44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T07:35:23.934Z\", \"updated_at\": \"2026-05-15T22:06:28.059Z\", \"hypothesis\": \"Full dev eval of RSFT seed=44 checkpoint. First MVP-2 judgement data point. Pass: rel_f1 > 0.4057 AND evi_f1 > 0.798 (SFT baseline).\", \"parent\": \"mvp2_rsft_train_r1_s44\", \"conclusion\": \"killed\", \"notes\": \"STALE: s44 全量 eval 已由 mvp2_eval_rsft_r2b_maxtok1536 等系列完成。s44 rel_f1=0.4655 已入库。此条目为残留。\"}, \"eval_plan_008_topk3_fixed\": {\"status\": \"DONE\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-15T21:39:34.632Z\", \"updated_at\": \"2026-05-15T21:39:34.632Z\"}, \"eval_plan_012_dpo_1ep_fixed\": {\"status\": \"DONE\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-15T21:39:31.570Z\", \"updated_at\": \"2026-05-15T21:39:31.570Z\"}, \"eval_plan_008_rsft_topk3\": {\"status\": \"DONE\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-15T21:09:51.464Z\", \"updated_at\": \"2026-05-15T21:38:00.000Z\", \"metrics\": {\"note\": \"INVALID — missing --sft_adapter, killed by Director instruction\"}, \"hypothesis\": \"RSFT top_k=3 dev eval: 对比 top_k=1 RSFT (rel_f1≈0.46) 和 SFT baseline (rel_f1≈0.4057)。验证更多候选是否提升证据质量。\", \"parent\": \"plan_008_rsft_topk3\"}, \"plan_012_dpo_ced\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T15:54:03.324Z\", \"updated_at\": \"2026-05-15T21:37:44.232Z\", \"hypothesis\": \"DPO+CED preference learning: 用 CED 构造 preference pairs (CED top-1 = chosen, CED bottom-1 = rejected)，DPO 训练。验证 offline preference optimization 能否替代 online GRPO 避免 catastrophic forgetting，同时利用 CED 信号。对比 RSFT (rel_f1=0.46) 和 SFT baseline (rel_f1=0.4057)。\", \"conclusion\": \"negative\", \"notes\": \"⚠️ Reviewer WARNING: 严重过拟合。3 epochs, rewards accuracy=1.0, margins 9x 膨胀, entropy 崩塌。checkpoint-501 是最过拟合版本，结果有 confound。需补 eval checkpoint-400 对比 + 重训 epochs=1。\", \"metrics\": {\"rel_f1\": 0.3429, \"evi_f1\": 0.8403, \"edcr\": 0.7294, \"format_ok_rate\": 0.995, \"checkpoint\": \"checkpoint-501\", \"rewards_accuracy\": 1, \"margins\": 9.01}}, \"plan_012_dpo_ced_1ep\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T18:50:44.852Z\", \"updated_at\": \"2026-05-15T21:36:34.720Z\", \"hypothesis\": \"DPO+CED 1 epoch retraining: plan_012_dpo_ced 3 epochs 严重过拟合 (rewards_accuracy=1.0, margins 9x膨胀, entropy崩塌)。重训 1 epoch 验证 early stopping 是否消除 overfitting confound。对比 plan_012 3ep + RSFT (rel_f1=0.46) + SFT baseline (rel_f1=0.4057)。\", \"notes\": \"DPO+CED 完全失败。1ep eval: rel_f1=0.0022 (34 TPs / 19265 preds)，比 3ep (0.3429) 更差。训练指标正常 (accuracy=0.82, margins=0.86)，但模型输出几乎无法匹配正确 relation。evi_f1=0.75 说明模型仍生成 evidence，但 relation extraction 崩溃。358/985 truncated (36%)。DPO 对 evidence-grounded DocRE 完全不适用——不是过拟合问题，是方法本身失效。D061 已关闭 DPO 实验线。\", \"metrics\": {\"rel_f1\": 0.0022, \"evi_f1\": 0.75, \"edcr\": 0.9982, \"format_ok\": \"981/985\", \"truncated\": \"358/985\", \"tp\": 34, \"n_preds\": 19265, \"inference_time_s\": 3643, \"train_loss_final\": 0.59, \"rewards_accuracy\": 0.82, \"rewards_margins\": 0.86, \"total_steps\": 167, \"training_time_min\": 33}, \"conclusion\": \"negative\"}, \"eval_plan_001_flat_nli_s43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T20:29:54.486Z\", \"updated_at\": \"2026-05-15T21:35:00.000Z\", \"conclusion\": \"failed\", \"metrics\": {\"rel_f1\": 0.0022, \"ign_f1\": 0.0022, \"evi_f1\": 0.8533, \"edcr\": 0.9982, \"num_preds\": 17285, \"format_ok\": \"981/985\", \"truncated\": \"251/985\", \"tp\": 32, \"note\": \"INVALID — missing --sft_adapter, same bug as DPO 1ep eval\"}}, \"eval_plan_012_dpo_ced_1ep\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T20:22:11.752Z\", \"updated_at\": \"2026-05-15T21:27:30.000Z\", \"conclusion\": \"negative\", \"metrics\": {\"rel_f1\": 0.0022, \"ign_f1\": 0.0022, \"evi_f1\": 0.75, \"edcr\": 0.9982, \"num_preds\": 19265, \"format_ok\": \"981/985\", \"truncated\": \"358/985\", \"tp\": 34, \"inference_time_s\": 3643}}, \"plan_008_rsft_topk3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T18:01:33.773Z\", \"updated_at\": \"2026-05-15T21:11:35.509Z\", \"hypothesis\": \"RSFT top_k=3 训练：用 CED-filtered 的 top-3 候选进行 rejection sampling fine-tuning，验证更多候选是否比 top_k=1 (rel_f1≈0.46) 带来更好的证据质量。\", \"metrics\": {\"train_loss\": 0.5543, \"eval_loss\": 0.8297, \"eval_mean_token_accuracy\": 0.8228, \"eval_entropy\": 0.6001, \"train_runtime_sec\": 10916, \"total_steps\": 1509, \"epochs\": 3, \"trainable_params_pct\": 3.18, \"rsft_samples\": 8037, \"ced_score_mean\": 0.621, \"task_eval_f1_ep1\": 0.4848, \"task_eval_f1_ep2\": 0.4824, \"task_eval_f1_ep3\": 0.5012, \"task_eval_evi_f1_ep1\": 0.745, \"task_eval_evi_f1_ep2\": 0.6997, \"task_eval_evi_f1_ep3\": 0.6816, \"task_eval_edcr_ep1\": 0.6525, \"task_eval_edcr_ep2\": 0.6529, \"task_eval_edcr_ep3\": 0.5963, \"task_eval_note\": \"50-doc subset, not full dev\"}, \"conclusion\": \"success\", \"notes\": \"RSFT top_k=3 训练正常完成。3 epochs, 1509 steps, 3h02m。8037 RSFT 样本 (CED mean=0.621)。Task eval (50-doc subset): F1 从 ep1=0.4848 升至 ep3=0.5012，但 Evi-F1 从 0.745 降至 0.6816，EDCR 从 0.6525 降至 0.5963，呈现 relation extraction 提升但证据质量下降的 trade-off。与 CED RSFT top_k=5 baseline (rel_f1=0.4596) 相比，subset F1=0.5012 看起来更高，但需 full dev eval 确认。无 W&B run。下一步：提交 eval_plan_008_rsft_topk3 做 full dev eval。\"}, \"plan_001_flat_nli_seed43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T18:22:55.521Z\", \"updated_at\": \"2026-05-15T20:35:05.452Z\", \"metrics\": {\"train_loss_final\": 0.6257, \"train_loss_min\": 0.5895, \"eval_loss_epoch3\": 0.7567, \"eval_accuracy_epoch3\": 0.8298, \"total_steps\": 507, \"epochs\": 3, \"train_runtime_seconds\": 6880, \"task_eval_f1_ep1\": 0.4825, \"task_eval_f1_ep2\": 0.4542, \"task_eval_f1_ep3\": 0.4866, \"task_eval_evi_f1_ep3\": 0.7834, \"task_eval_edcr_ep3\": 0.6402, \"task_eval_note\": \"50-doc subset, not full dev\"}, \"conclusion\": \"success\", \"notes\": \"训练正常完成 (EXIT_CODE=0)。507 steps, 3 epochs, eval_loss 三 epoch 持平 (0.753-0.757) 无过拟合。与 seed42 高度一致 (train_loss 0.6248 vs 0.6238, accuracy ~0.855 vs 0.853)。Checkpoint: /root/autodl-tmp/rsft_output_flat_nli_s43/checkpoint-507。下一步: dev eval 提取 rel_f1/evi_f1。\"}, \"plan_009_flatnli_reward_eval_r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T19:54:58.033Z\", \"updated_at\": \"2026-05-15T20:32:33.464Z\", \"conclusion\": \"failed\", \"notes\": \"OOM 失败。--no-quantize + batch_size 16 + max_new_tokens 1024 在单卡 RTX 5090 (32GB) 上 OOM。全部 5 个 checkpoint (20-100) 均未完成 eval。checkpoint-20 仅完成 1/62 batches 即被 kill (-9)。修复方案：降 batch_size 至 4 或 2 后重提交。\"}, \"plan_009_extract_reward_eval\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T19:04:55.707Z\", \"updated_at\": \"2026-05-15T19:58:37.870Z\", \"conclusion\": \"failed\", \"notes\": \"OOM: Worker 提交到了 GPU 0（被 plan_001 占用 16 GiB），而非目标 cuda:1。需在 cuda:0 释放后重提交。\"}, \"eval_sft_baseline_noquant\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T18:38:33.128Z\", \"updated_at\": \"2026-05-15T19:45:42.147Z\", \"metrics\": {\"rel_f1\": 0.4106, \"rel_precision\": 0.4198, \"rel_recall\": 0.4019, \"evi_f1\": 0.8013, \"evi_precision\": 0.8005, \"evi_recall\": 0.8022, \"evi_f1_joint\": 0.3216, \"edcr\": 0.7039, \"format_ok_rate\": 0.998, \"field_compliance_rate\": 0.7066, \"n_predictions\": 16774, \"n_truncated\": 288, \"n_documents\": 985, \"inference_time_seconds\": 3677.9}, \"conclusion\": \"success\", \"notes\": \"[2026-05-16] 无量化 SFT baseline eval 完成。rel_f1=0.4106 vs 量化版 0.4057 (+0.49pp), evi_f1=0.8013 vs 0.7979 (+0.34pp)。差异 <1pp，确认量化 confound 不显著（D058 排除）。所有基于量化 baseline 的对比结论仍然成立。无量化版推理时间 3678s vs 量化版 6139s（快 40%，因无量化用满 GPU 内存）。\"}, \"plan_009_flatnli_reward_eval\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T19:04:57.991Z\", \"updated_at\": \"2026-05-15T19:39:02.187Z\", \"conclusion\": \"failed\"}, \"eval_plan_012_dpo_ced_ckpt400\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T19:32:55.398Z\", \"updated_at\": \"2026-05-15T19:37:31.477Z\", \"conclusion\": \"failed\", \"notes\": \"OOM: cuda:3 被 plan_008 占用 19.6 GiB，仅完成 15% batch，结果不可信。需在 cuda:2 重跑。\"}, \"plan_009_forgetting_figure\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T18:56:56.840Z\", \"updated_at\": \"2026-05-15T18:57:17.531Z\", \"conclusion\": \"success\", \"notes\": \"3-panel figure: (a) Training Reward—bf16 1.5-3.0 vs QLoRA 0.1-1.2; (b) Rel-F1—QLoRA暴跌至0.01(lr5e-6)/0.22(lr5e-5), bf16稳定0.45+; (c) Evi-F1—QLoRA lr5e-6反升至0.85, bf16稳定0.81。Artifacts: art_20260515_eace0b (PNG), art_20260515_319233 (PDF)。\"}, \"eval_plan_014_sft_no_evidence\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T17:20:25.574Z\", \"updated_at\": \"2026-05-15T18:42:46.665Z\", \"metrics\": {\"rel_f1\": 0.4893, \"rel_ign_f1\": 0.4893, \"rel_precision\": 0.4884, \"rel_recall\": 0.4902, \"evi_f1\": 0, \"evi_precision\": 0, \"evi_recall\": 0, \"edcr\": 0, \"format_ok_rate\": 0.9919, \"n_truncated\": 298, \"n_predictions\": 21064, \"n_documents\": 985, \"n_parseable\": 977, \"inference_time_seconds\": 4103.8}, \"conclusion\": \"success\", \"notes\": \"No-evidence SFT rel_f1=0.4893 vs baseline with-evidence rel_f1=0.4057 (+0.0836, +20.6%). Evidence generation significantly hurts relation extraction. evi_f1=0 as expected. Format compliance 99.2%. 298/985 truncated. Inference 4103.8s.\"}, \"plan_014_sft_no_evidence\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T15:55:43.710Z\", \"updated_at\": \"2026-05-15T18:42:28.216Z\", \"hypothesis\": \"SFT-without-evidence ablation: 训练只输出 relation triples（不含 evidence sentences）的 SFT 模型。量化 joint evidence generation 对 extraction 的代价（当前 rel_f1=0.4057 vs 只抽关系的 LMRC 60.7 的 gap 有多少来自 evidence 负担）。\", \"metrics\": {\"train_loss\": 0.7077, \"eval_loss\": 0.8781, \"eval_token_accuracy\": 0.8086, \"epochs\": 3, \"total_steps\": 570, \"train_runtime_min\": 64, \"samples\": 3027, \"trainable_params\": \"132M/4.15B (3.18%)\"}, \"conclusion\": \"success\"}, \"plan_002_test_eval_s44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T18:05:47.701Z\", \"updated_at\": \"2026-05-15T18:20:17.405Z\", \"conclusion\": \"failed\", \"notes\": \"DocRED test split 无 gold labels，inference.py 不支持 enumerate_all_pairs 模式。推迟到论文终稿阶段（需改造 inference.py + CodaLab submission）。Director 指令标记 failed。\"}, \"plan_001_rsft_flat_nli\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T15:40:01.021Z\", \"updated_at\": \"2026-05-15T18:04:14.547Z\", \"hypothesis\": \"flat-NLI RSFT ablation: 用 flat-NLI scoring（p_pos 概率，无 contrastive margin）筛选的 2691 样本做 RSFT。对比 CED scoring RSFT（2718 样本）。验证 CED 的对比性 margin 是否是关键因素。如 flat-NLI RSFT ≈ CED RSFT → CED 无增益；如 CED RSFT 显著优于 → contrastive margin 关键。\", \"parent\": \"plan_001_flat_nli_scoring\", \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 0.6238, \"train_loss_min\": 0.5803, \"mean_token_accuracy\": 0.8528, \"train_runtime_sec\": 2946, \"epochs\": 3, \"total_steps\": 507, \"samples\": 2691}}, \"eval_plan_001_flat_nli\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T16:57:09.693Z\", \"updated_at\": \"2026-05-15T18:04:13.598Z\", \"hypothesis\": \"Dev eval of flat-NLI RSFT (plan_001). 对比 CED RSFT (3-seed mean rel_f1=0.4596). flat-NLI ≈ CED → CED contrastive margin 无增益; CED >> flat-NLI → margin 关键。\", \"parent\": \"plan_001_rsft_flat_nli\", \"metrics\": {\"rel_f1\": 0.4539, \"ign_f1\": 0.4539, \"evi_f1\": 0.8043, \"edcr\": 0.6431, \"precision\": 0.4671, \"recall\": 0.4414, \"evi_precision\": 0.8143, \"evi_recall\": 0.7945, \"format_ok_rate\": 1, \"n_truncated\": 199, \"n_documents\": 985, \"n_predictions\": 15294, \"inference_time_seconds\": 3631}, \"conclusion\": \"success\", \"notes\": \"flat-NLI RSFT dev eval 完成 (985 docs, EXIT_CODE=0)。rel_f1=0.4539, evi_f1=0.8043, edcr=0.6431。与 CED RSFT 3-seed mean 对比: rel_f1 -0.57pp (0.4539 vs 0.4596), evi_f1 -1.00pp (0.8043 vs 0.8143), edcr 差异极小。flat-NLI 接近但略低于 CED，差异在 CED 3-seed 标准差范围内 (σ=0.0127)。注意此为 single seed (42)，与 CED seed=42 的 0.4449 比反而高 +0.90pp。结论：CED contrastive margin 相对 flat p_pos 的增益极小（<1pp rel_f1），不构成显著优势。论文 claim 应聚焦 CED 的其他价值（reranker、GRPO reward）而非 RSFT filtering 的 contrastive margin。199/985 truncated（高于 CED 的 ~170），format 100% OK。\"}, \"eval_grpo_g8_bf16\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T14:41:07.474Z\", \"updated_at\": \"2026-05-15T17:57:46.573Z\", \"hypothesis\": \"Eval GRPO G=8 bf16 checkpoints 80/90/100 on full dev set (985 docs). 验证 catastrophic forgetting 是否在 bf16 LoRA 下复现。rel_f1>0.30 → forgetting 不复现 (QLoRA-specific); rel_f1<0.05 → 复现 (C2 加强)。对比: SFT rel_f1=0.4057, QLoRA GRPO rel_f1=0.2167 (catastrophic).\", \"metrics\": {\"ckpt80_rel_f1\": 0.4456, \"ckpt80_ign_f1\": 0.4456, \"ckpt80_evi_f1\": 0.8034, \"ckpt80_edcr\": 0.6409, \"ckpt80_format_ok\": \"984/985\", \"ckpt80_truncated\": 50, \"ckpt90_rel_f1\": 0.4523, \"ckpt90_ign_f1\": 0.4523, \"ckpt90_evi_f1\": 0.8052, \"ckpt90_edcr\": 0.6414, \"ckpt90_format_ok\": \"983/985\", \"ckpt90_truncated\": 61, \"ckpt100_rel_f1\": 0.4549, \"ckpt100_ign_f1\": 0.4549, \"ckpt100_evi_f1\": 0.8086, \"ckpt100_edcr\": 0.6318, \"ckpt100_format_ok\": \"985/985\", \"ckpt100_truncated\": 61, \"best_checkpoint\": \"ckpt-100\"}, \"conclusion\": \"success\", \"notes\": \"3 checkpoints 全部评测完成。rel_f1 单调递增 (0.4456→0.4523→0.4549)，evi_f1 同步上升 (0.8034→0.8052→0.8086)。全部 checkpoint 均大幅超过 SFT baseline (0.4057) 和 QLoRA GRPO (0.2167 catastrophic forgetting)。bf16 LoRA GRPO 无 forgetting，且持续改善至 step 100。Best checkpoint: 100 (rel_f1=0.4549, +12.1% over SFT).\"}, \"plan_015_grpo_g4_bf16_v3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T16:27:09.496Z\", \"updated_at\": \"2026-05-15T16:54:54.376Z\", \"notes\": \"Robustness check, 非 single-variable ablation。lr=5e-6 与对照组 (mvp2_grpo_ced_kl001_r4, lr=5e-5) 不一致。D052 确认 plan_011 (bf16 G=8 kl=0.01 lr=5e-5) vs mvp2_grpo_ced_kl001_r4 (QLoRA G=8 kl=0.01 lr=5e-5) 才是 clean ablation。v3 仅作为额外 robustness data point。\", \"hypothesis\": \"P2 robustness check: bf16 LoRA GRPO G=4, kl=0.01, lr=5e-6。D052 确认 plan_011 vs mvp2_grpo_ced_kl001_r4 已是 clean single-variable quantization ablation (Δ=+23.8pp)。v3 仅为 robustness data point，lr=5e-6 与对照组 lr=5e-5 不一致。\", \"conclusion\": \"killed\"}, \"plan_015_grpo_g4_bf16_v2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T16:06:43.308Z\", \"updated_at\": \"2026-05-15T16:54:42.310Z\", \"hypothesis\": \"Robustness check: bf16 LoRA GRPO 在 G=4, kl=0, lr=5e-6 条件下是否也防止 catastrophic forgetting。非 single-variable ablation（kl/lr/G 均与 QLoRA 对照组不同）。D052 确认 plan_011 vs mvp2_grpo_ced_kl001_r4 已是 clean quantization ablation。\", \"parent\": \"plan_011_grpo_g8_bf16\", \"conclusion\": \"killed\"}, \"plan_015_grpo_g4_bf16\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T15:58:43.784Z\", \"updated_at\": \"2026-05-15T16:03:08.279Z\", \"hypothesis\": \"bf16 LoRA GRPO clean control: 与原始 QLoRA GRPO 仅改 quantization（4-bit → bf16），保持 G=4, kl=0, CED reward 不变。验证 catastrophic forgetting 是否由 QLoRA quantization 导致。\", \"conclusion\": \"killed\", \"notes\": \"cuda:0 冲突，与 plan_001_rsft_flat_nli (PID 219556) 冲突。plan_001 先到先得，plan_015 被终止。待 plan_001 完成后重新提交 plan_015。\"}, \"plan_011_grpo_g8_bf16\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T13:59:50.014Z\", \"updated_at\": \"2026-05-15T15:55:53.725Z\", \"hypothesis\": \"GRPO G=8 bf16 LoRA: 验证 catastrophic forgetting 是否在 bf16（非 QLoRA 4-bit）下仍复现。CED reward + kl_coef=0.01, 100 steps。如仍 fail → 加强 Claim 3\", \"metrics\": {\"final_step\": 100, \"train_runtime_s\": 554, \"reward_final\": 1.795, \"f1_reward_final\": 1.002, \"ced_reward_final\": 0.494, \"format_reward_final\": 0.3, \"frac_zero_std_final\": 0, \"kl_final\": 0.022, \"best_reward_step\": 85, \"best_reward\": 2.858, \"best_f1_reward\": 1.85, \"mode_collapse\": false, \"lora_config\": \"r=64, alpha=128, dropout=0.05, bf16\", \"checkpoints\": \"10 checkpoints (step 10-100)\"}, \"notes\": \"训练完成 (100/100 steps, EXIT_CODE=0, 554s/9.2min)。无 mode collapse (frac_zero_std=0.0 全程)。KL 极低 (0.005-0.052)。训练 metrics 比 QLoRA 更好 (reward 1.795 vs 1.195, 无 frac_zero_std 升高)。但 QLoRA 训练 metrics 也不差，问题在 eval。必须 eval 才能判断 catastrophic forgetting 是算法层面还是量化问题。\", \"conclusion\": \"success\"}, \"plan_011_grpo_g8_bf16_eval\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T14:43:48.481Z\", \"updated_at\": \"2026-05-15T15:55:52.592Z\", \"conclusion\": \"success\", \"metrics\": {\"rel_f1\": 0.4549, \"ign_f1\": 0.4549, \"evi_f1\": 0.8086, \"edcr\": 0.6318, \"format_ok_rate\": 1, \"n_truncated\": 61, \"n_total\": 985, \"n_predictions\": 10701, \"checkpoint\": \"checkpoint-100\", \"model\": \"Qwen3-4B + SFT merged + GRPO bf16 LoRA ckpt-100\", \"inference_time_s\": 3170.3}, \"notes\": \"bf16 GRPO G=8 checkpoint-100 full dev eval (985 docs). F1=0.4549 (+4.92pp vs SFT 0.4057), Evi-F1=0.8086 (+1.07pp vs SFT 0.7979), EDCR=0.6318. Catastrophic forgetting 不复现——bf16 LoRA 下 GRPO 性能甚至超过 SFT baseline。与 QLoRA GRPO (rel_f1=0.2167) 形成鲜明对比。61/985 truncated, 100% format OK. 关键结论: forgetting 是 QLoRA 4-bit 量化导致, 非 GRPO 算法本身问题。但注意此实验同时改了 quantization(bf16 vs 4bit) + group_size(8 vs 4), 需 plan_015 隔离变量。\"}, \"plan_004_dreeam_baseline\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T13:47:01.947Z\", \"updated_at\": \"2026-05-15T15:44:24.920Z\", \"hypothesis\": \"Phase A: 复现 DREEAM fully-supervised teacher (RoBERTa-large) DocRED dev Evi-F1≈54.15, RE-F1≈63.49。论文报告的57.34是student model在test set的结果，需4阶段self-training pipeline。\", \"metrics\": {\"dev_rel_f1\": 63.57, \"dev_rel_ign_f1\": 61.72, \"dev_evi_f1\": 54.01, \"dev_rel_p\": 66.95, \"dev_rel_r\": 60.51, \"dev_evi_p\": 60.53, \"dev_evi_r\": 48.76}, \"conclusion\": \"success\"}, \"mvp2_eval_rsft_r2b_maxtok1536_r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T11:54:57.156Z\", \"updated_at\": \"2026-05-15T15:21:13.816Z\", \"hypothesis\": \"Truncation diagnosis: r2b eval with max_new_tokens=1536 (vs default 1024). Retry with correct model stack (Base+SFT+RSFT). If EDCR improves significantly (from 0.6609 toward 0.71+), truncation is the cause. If unchanged, distractor citation is genuine RSFT behavior.\", \"parent\": \"mvp2_eval_rsft_r2b\", \"metrics\": {\"rel_f1\": 0.4504, \"ign_f1\": 0.4504, \"evi_f1\": 0.8102, \"edcr\": 0.674, \"precision\": 0.4488, \"recall\": 0.4519, \"evi_precision\": 0.8162, \"evi_recall\": 0.8044, \"n_truncated\": 146, \"n_total\": 985, \"n_predictions\": 17188, \"n_distractor_citations\": 19589, \"n_total_citations\": 29063, \"format_ok_rate\": 0.998}, \"conclusion\": \"negative\", \"notes\": \"max_new_tokens 1536 vs 1024: truncated 179→146 (-33), EDCR 0.6609→0.6740 (+0.0131), rel_f1 0.4493→0.4504, evi_f1 0.8128→0.8102。截断只是 EDCR 偏低的次要因素，distractor citation 是 RSFT 的真实行为。\"}, \"plan_001_flat_nli_scoring\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T14:36:56.213Z\", \"updated_at\": \"2026-05-15T15:21:03.475Z\", \"hypothesis\": \"flat-NLI scoring 前置步骤：用 flat_nli 模式（p_pos 概率，无 contrastive margin）对 RSFT 生成候选打分并筛选训练数据。\", \"conclusion\": \"success\", \"metrics\": {\"total_scored\": 21728, \"selected_samples\": 2691, \"selection_rate\": 0.124, \"selection_strategy\": \"top_k=1\", \"f1_threshold\": 0.1, \"output_path\": \"/root/autodl-tmp/rsft_filtered_flat_nli/rsft_train.jsonl\"}, \"notes\": \"Scoring 实际用 top_k=1（非 spec 中的 top_k=3），与 CED scoring 的 top_k=1 (2718 samples) 公平对比。选出 2691 samples。Cron 误报 failed（假阴性），Reviewer 确认输出完整。\"}, \"mvp2_eval_rsft_s43_r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T11:29:17.551Z\", \"updated_at\": \"2026-05-15T13:54:26.023Z\", \"hypothesis\": \"Full dev eval of RSFT s43 (seed=43). 3rd seed for variance estimation. r1: rel_f1=0.4449, s44: rel_f1=0.4655. Pass: rel_f1 > 0.4057, evi_f1 > 0.798. Retry of mvp2_eval_rsft_s43 (fixed arg names).\", \"parent\": \"mvp2_rsft_train_r1_s43\", \"metrics\": {\"rel_f1\": 0.4683, \"ign_f1\": 0.4683, \"evi_f1\": 0.8156, \"evi_f1_joint\": 0.3711, \"evi_f1_joint_P\": 0.3747, \"evi_f1_joint_R\": 0.3675, \"edcr\": 0.6388, \"precision\": 0.4817, \"recall\": 0.4556, \"evi_precision\": 0.8142, \"evi_recall\": 0.817, \"n_predictions\": 14970, \"n_truncated\": 171, \"format_ok_rate\": 1, \"inference_time_s\": 6316.7, \"sft_baseline_rel_f1\": 0.4057, \"sft_baseline_evi_f1\": 0.7979, \"delta_rel_f1\": 0.0626, \"delta_evi_f1\": 0.0177, \"delta_evi_f1_joint\": 0.0594, \"mvp2_pass\": true}, \"conclusion\": \"success\", \"notes\": \"3rd seed PASS. rel_f1=0.4683 (+6.26pp vs SFT), evi_f1=0.8156 (+1.77pp), EDCR=0.6388. 3-seed 完整表: mean rel_f1=0.4596±0.0127, mean evi_f1=0.8143±0.0051. 三个 seed 均稳定超过 SFT baseline。cuda:2 已释放。\"}, \"mvp2_rsft_ced_scoring_topk3_r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T12:12:38.363Z\", \"updated_at\": \"2026-05-15T13:53:08.461Z\", \"hypothesis\": \"CED scoring ablation: top_k=3 (vs top_k=1). More training data (~8000 samples) vs stricter selection (2718 samples). Retry with HF_HUB_OFFLINE=1 (NLI model cached locally).\", \"parent\": \"mvp2_rsft_ced_scoring\", \"metrics\": {\"input_generations\": 21728, \"selected_samples\": 8037, \"unique_docs\": 2691, \"selection_rate\": 0.37, \"mean_f1\": 0.5761, \"mean_ced\": 0.6205, \"mean_combined\": 0.6787, \"f1_range_p25\": 0.444, \"f1_range_p75\": 0.717, \"ced_range_p25\": 0.487, \"ced_range_p75\": 0.774, \"truncated_samples\": 1924, \"truncated_pct\": 8.9, \"selection_strategy\": \"top_k=3\", \"f1_threshold\": 0.1, \"topk1_samples\": 2718, \"data_multiplier\": 2.96}, \"conclusion\": \"success\", \"notes\": \"top_k=3 scoring 完成。8037 samples (vs top_k=1 的 2718, 2.96x)。质量下降可控: mean_f1 -0.04, mean_ced -0.048。输出: /root/autodl-tmp/rsft_filtered_topk3/rsft_train.jsonl (24.8MB)。可用于 plan_008 RSFT 训练 ablation。\"}, \"mvp2_rsft_train_r1_s44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T05:36:26.321Z\", \"updated_at\": \"2026-05-15T13:27:38.819Z\", \"hypothesis\": \"RSFT training seed=44 variance estimate. Same params as r1 (bf16 LoRA r=64/α=128, lr=2e-5, 3 epochs, weighted sampling, CED-filtered 2718 samples). Pass: rel_f1 > 0.4057 AND evi_f1 > 0.798.\", \"parent\": \"mvp2_rsft_train_r1\", \"wandb_run_id\": \"rsft-ced-r1-s44\", \"metrics\": {\"rel_f1\": 0.4655, \"evi_f1\": 0.8087, \"evi_f1_joint\": 0.3713, \"evi_f1_joint_P\": 0.3775, \"evi_f1_joint_R\": 0.3653, \"edcr\": 0.635, \"sft_baseline_rel_f1\": 0.4057, \"sft_baseline_evi_f1\": 0.7979, \"delta_rel_f1\": 0.0598, \"delta_evi_f1\": 0.0108, \"delta_evi_f1_joint\": 0.0596, \"mvp2_pass\": true}, \"conclusion\": \"success\"}, \"mvp2_eval_rsft_r2b\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T09:42:58.437Z\", \"updated_at\": \"2026-05-15T13:27:35.580Z\", \"hypothesis\": \"Full dev eval of r2b (1 epoch, alpha=32, lr=1e-5, clean data). Ablation: conservative LoRA scaling vs r2a/r1. Pass: rel_f1 > 0.4057, evi_f1 > 0.798.\", \"parent\": \"mvp2_rsft_r2b\", \"metrics\": {\"rel_f1\": 0.4493, \"ign_f1\": 0.4493, \"evi_f1\": 0.8128, \"evi_f1_joint\": 0.349, \"evi_f1_joint_P\": 0.3455, \"evi_f1_joint_R\": 0.3526, \"edcr\": 0.6609, \"precision\": 0.4566, \"recall\": 0.4424, \"evi_precision\": 0.8201, \"evi_recall\": 0.8056, \"pred_count\": 14829, \"format_ok\": \"983/985\", \"truncated\": 179, \"inference_time_s\": 5862, \"delta_evi_f1_joint\": 0.0373}, \"conclusion\": \"success\"}, \"mvp2_eval_rsft_r2a\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T09:42:57.684Z\", \"updated_at\": \"2026-05-15T13:27:32.756Z\", \"hypothesis\": \"Full dev eval of r2a (1 epoch, alpha=128, clean data). Ablation: 1 epoch vs 3 epoch (r1). Pass: rel_f1 > 0.4057, evi_f1 > 0.798.\", \"parent\": \"mvp2_rsft_r2a\", \"conclusion\": \"success\", \"metrics\": {\"rel_f1\": 0.4494, \"ign_f1\": 0.4494, \"evi_f1\": 0.8108, \"evi_f1_joint\": 0.3509, \"evi_f1_joint_P\": 0.3423, \"evi_f1_joint_R\": 0.3599, \"edcr\": 0.6641, \"precision\": 0.4512, \"recall\": 0.4475, \"evi_precision\": 0.8143, \"evi_recall\": 0.8073, \"format_ok_rate\": 1, \"n_predictions\": 15482, \"n_truncated\": 208, \"inference_time_s\": 5967.2, \"delta_evi_f1_joint\": 0.0392}, \"notes\": \"RSFT r2a (1ep, alpha=128/r=64, lr=2e-5, clean 2548 samples). rel_f1=0.4494 (+0.0045 vs r1, +0.0001 vs r2b), evi_f1=0.8108 (-0.0079 vs r1, -0.0020 vs r2b), edcr=0.6641 (+0.0032 vs r2b). 1 epoch with clean data matches r1's 3-epoch rel_f1 while being cheaper. r2a vs r2b (alpha=128 vs 32): nearly identical rel_f1, marginal edcr advantage for higher alpha. All RSFT variants beat SFT baseline on rel_f1/evi_f1 but lose on edcr (0.66-0.66 vs 0.71).\"}, \"mvp2_eval_rsft_r1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T09:40:47.529Z\", \"updated_at\": \"2026-05-15T13:27:31.402Z\", \"hypothesis\": \"Full dev eval of RSFT r1 (seed=42). Same pipeline as s44 eval (985 docs, no-quantize). Need 3-seed data for complete_mvp. s44 PASS: rel_f1=0.4655, evi_f1=0.8087.\", \"parent\": \"mvp2_rsft_train_r1\", \"metrics\": {\"rel_f1\": 0.4449, \"evi_f1\": 0.8187, \"evi_f1_joint\": 0.3468, \"evi_f1_joint_P\": 0.3515, \"evi_f1_joint_R\": 0.3423, \"edcr\": 0.6565, \"num_preds\": 15307, \"sft_baseline_rel_f1\": 0.4057, \"sft_baseline_evi_f1\": 0.7979, \"delta_rel_f1\": 0.0392, \"delta_evi_f1\": 0.0208, \"delta_evi_f1_joint\": 0.0351, \"mvp2_pass\": true}, \"conclusion\": \"success\"}, \"mvp2_eval_sft_baseline\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T21:47:41.356Z\", \"updated_at\": \"2026-05-15T13:27:26.236Z\", \"hypothesis\": \"SFT baseline eval using identical eval protocol as GRPO evals (eval_lr5e6_ckpt20.sh). Required for MVP-2 core comparison: CED_Evi-F1 − SFT_Evi-F1 ≥ 2pp. Prior SFT eval (r3) used different eval path; this ensures apple-to-apple comparison.\", \"parent\": \"mvp2_sft_warmup\", \"notes\": \"[2026-05-15 07:39] Eval 正常完成。结果与 r2/r3 完全一致 (rel_f1=0.4057, evi_f1=0.7979)，apple-to-apple 对比协议复现成功。结果路径: /root/autodl-tmp/sft_baseline_eval_results/metrics.json。cuda:3 已释放。\", \"conclusion\": \"success\", \"metrics\": {\"rel_f1\": 0.4057, \"evi_f1\": 0.7979, \"evi_f1_joint\": 0.3117, \"evi_f1_joint_P\": 0.3037, \"evi_f1_joint_R\": 0.32, \"edcr\": 0.7118, \"pred_count\": 12234, \"gold_count\": 12151, \"format_ok_rate\": 0.998, \"format_compliance_rate\": 0.998, \"field_compliance_rate\": 0.6264, \"n_truncated\": 367, \"inference_time_seconds\": 6138.5}}, \"mvp2_eval_rsft_r2b_maxtok1536\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T11:49:48.849Z\", \"updated_at\": \"2026-05-15T13:23:59.642Z\", \"hypothesis\": \"Truncation diagnosis: r2b eval with max_new_tokens=1536 (vs default 1024). If EDCR improves significantly (from 0.6609 toward 0.71+), current EDCR gap is truncation artifact, not model issue. If EDCR unchanged, distractor citation is genuine RSFT behavior.\", \"parent\": \"mvp2_eval_rsft_r2b\", \"conclusion\": \"killed\", \"notes\": \"Reviewer CRITICAL: 命令缺少 --base_model 和 --sft_adapter，模型 stack 是 Base+RSFT LoRA 而非 Base+SFT+RSFT LoRA，结果不可用。PID 196700 已 kill。重试为 mvp2_eval_rsft_r2b_maxtok1536_r2。\"}, \"mvp2_rsft_ced_scoring_topk3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T07:35:23.225Z\", \"updated_at\": \"2026-05-15T13:20:42.443Z\", \"hypothesis\": \"CED scoring ablation: top_k=3 (vs top_k=1). More training data (~8000 samples) vs stricter selection (2718 samples). Answers: does CED filtering strictness affect RSFT training quality?\", \"conclusion\": \"killed\", \"notes\": \"NLI 模型加载失败 (HuggingFace Network unreachable)。命令缺少 HF_HOME/HF_HUB_OFFLINE/TRANSFORMERS_OFFLINE 环境变量。重试为 mvp2_rsft_ced_scoring_topk3_r2。\"}, \"mvp2_rsft_r2b\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T08:57:46.813Z\", \"updated_at\": \"2026-05-15T13:14:23.368Z\", \"hypothesis\": \"RSFT r2b: data fix + training dynamics fix (1 epoch + filter truncated + LoRA alpha=32/r=64 scaling 0.5 + lr=1e-5). Isolates: is conservative LoRA scaling the key factor? Pass: rel_f1 > 0.4057, evi_f1 > 0.798.\", \"parent\": \"mvp2_rsft_train_r1\", \"wandb_run_id\": \"rsft-r2b\", \"notes\": \"训练完成 (160 steps, 33.7min, eval_loss=0.7545)。TaskEvalCallback rel_f1=0.0504 是已知 bug (D038: gold triples 分母不匹配)，不代表真实性能。需全量 dev eval 确认实际指标。\", \"conclusion\": \"success\", \"metrics\": {\"rel_f1\": 0.4493, \"evi_f1\": 0.8128, \"edcr\": 0.6609, \"sft_baseline_rel_f1\": 0.4057, \"sft_baseline_evi_f1\": 0.7979, \"delta_rel_f1\": 0.0436, \"delta_evi_f1\": 0.0149, \"mvp2_pass\": true}}, \"mvp2_rsft_r2a\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T08:57:46.140Z\", \"updated_at\": \"2026-05-15T13:14:22.509Z\", \"hypothesis\": \"RSFT r2a: data fix only (1 epoch + filter 170 truncated JSON → 2548 samples). Same LoRA alpha=128/r=64, lr=2e-5 as r1. Isolates: does 1 epoch + clean data alone fix the ontology collapse? Pass: rel_f1 > 0.4057, evi_f1 > 0.798.\", \"parent\": \"mvp2_rsft_train_r1\", \"wandb_run_id\": \"rsft-r2a\", \"notes\": \"训练完成 (160 steps, 35.5min, eval_loss=0.7547)。TaskEvalCallback rel_f1=0.0509 是已知 bug (D038: gold triples 分母不匹配)，不代表真实性能。需全量 dev eval 确认实际指标。\", \"conclusion\": \"success\", \"metrics\": {\"rel_f1\": 0.4494, \"evi_f1\": 0.8108, \"edcr\": 0.6641, \"sft_baseline_rel_f1\": 0.4057, \"sft_baseline_evi_f1\": 0.7979, \"delta_rel_f1\": 0.0437, \"delta_evi_f1\": 0.0129, \"mvp2_pass\": true}}, \"mvp2_rsft_diagnosis\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T07:55:04.100Z\", \"updated_at\": \"2026-05-15T12:09:32.257Z\", \"hypothesis\": \"RSFT failure root cause: rel_f1=0.0483 vs SFT 0.4057. Diagnose: training data distribution (relation count), step-170 checkpoint output analysis, SFT vs RSFT data comparison.\", \"conclusion\": \"success\", \"metrics\": {\"root_cause\": \"overfitting_plus_sft_knowledge_overwrite\", \"truncated_json_samples\": 170, \"truncated_pct\": 6.3, \"epoch1_eval_loss\": 0.756, \"epoch2_eval_loss\": 0.759, \"lora_scaling\": 2, \"rsft_zero_relation_samples\": 170, \"sft_zero_relation_docs\": 26, \"rsft_mean_relations\": 11.2, \"sft_mean_relations\": 12.5}}, \"mvp2_eval_ced_kl001_r4_last\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T18:10:05.820Z\", \"updated_at\": \"2026-05-15T12:09:21.004Z\", \"notes\": \"已被拆分为独立 eval：ckpt-90 → mvp2_eval_ced_kl001_r4_ckpt90 (cuda:3)，ckpt-100 → mvp2_eval_ced_kl001_r4_step100 (cuda:0)。此条目作废。\", \"conclusion\": \"killed\"}, \"mvp2_grpo_ced_kl001_r3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T15:25:06.729Z\", \"updated_at\": \"2026-05-15T12:09:20.252Z\", \"hypothesis\": \"kl_coef=0.01 (vs r5 kl_coef=0.0) prevents CED mode collapse while keeping QLoRA 4-bit compatible — answers whether KL regularization is necessary (retry: fix --lr + bash -c wrapping)\", \"parent\": \"mvp2_grpo_ced_kl001\", \"notes\": \"失败原因: datasets 库不支持 thunlp/docred 自定义脚本 (RuntimeError: Dataset scripts are no longer supported)。命令缺少 --data_dir /root/autodl-tmp/data/docred 参数，触发 HF 远程下载失败。需要补全所有必要参数后重新提交。error_type: infrastructure | can_auto_fix: true\", \"conclusion\": \"killed\"}, \"mvp2_grpo_ced_kl001_r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T15:23:16.518Z\", \"updated_at\": \"2026-05-15T12:09:19.263Z\", \"hypothesis\": \"kl_coef=0.01 (vs r5 kl_coef=0.0) prevents CED mode collapse while keeping QLoRA 4-bit compatible — answers whether KL regularization is necessary (retry: fix --lr → --learning_rate)\", \"parent\": \"mvp2_grpo_ced_kl001\", \"conclusion\": \"killed\", \"notes\": \"失败原因: 命令未用 bash -c 包裹，tmux 以 sh 执行导致 source 命令失败。error_type: infrastructure | can_auto_fix: true\"}, \"mvp2_rsft_train_r2_fix\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T08:38:03.815Z\", \"updated_at\": \"2026-05-15T12:09:18.298Z\", \"hypothesis\": \"RSFT r2 fix: 4 fixes based on r1 diagnosis. 1) 1 epoch (vs 3), 2) LoRA alpha=32/r=64 (scaling 0.5 vs 2.0), 3) filtered truncated JSON (~2548 vs 2718 samples), 4) lr=1e-5 (vs 2e-5). Pass: rel_f1 > 0.4057, evi_f1 > 0.798.\", \"conclusion\": \"killed\"}, \"mvp2_rsft_train_r1_s43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T05:36:25.275Z\", \"updated_at\": \"2026-05-15T11:31:48.727Z\", \"hypothesis\": \"RSFT training seed=43 variance estimate. Same params as r1 (bf16 LoRA r=64/α=128, lr=2e-5, 3 epochs, weighted sampling, CED-filtered 2718 samples). Pass: rel_f1 > 0.4057 AND evi_f1 > 0.798.\", \"parent\": \"mvp2_rsft_train_r1\", \"wandb_run_id\": \"rsft-ced-r1-s43\", \"metrics\": {\"eval_loss\": 0.7622, \"train_loss\": 0.6148, \"eval_entropy\": 0.6724, \"mean_token_accuracy\": 0.8291, \"total_steps\": 510, \"epochs\": 3, \"training_hours\": 1.99}, \"conclusion\": \"success\", \"notes\": \"训练正常完成 (510 steps, 1.99h, eval_loss=0.7622, train_loss=0.6148)。与 s44 (eval_loss=未记录) 和 r1 相近。TaskEvalCallback rel_f1 是已知 bug，需全量 eval。全量 eval 重试 mvp2_eval_rsft_s43_r2 正在运行中。\"}, \"mvp2_eval_rsft_s43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T11:25:26.268Z\", \"updated_at\": \"2026-05-15T11:29:11.205Z\", \"hypothesis\": \"Full dev eval of RSFT s43 (seed=43). 3rd seed for variance estimation. r1: rel_f1=0.4449, s44: rel_f1=0.4655. Pass: rel_f1 > 0.4057, evi_f1 > 0.798.\", \"parent\": \"mvp2_rsft_train_r1_s43\", \"conclusion\": \"failed\", \"notes\": \"参数名错误导致失败: --rsft_adapter 应为 --model_path, --data_dir 应为 --data_path, --gpu 0 不存在。重试为 mvp2_eval_rsft_s43_r2。\"}, \"mvp2_rsft_train_r1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T05:27:39.073Z\", \"updated_at\": \"2026-05-15T09:40:39.078Z\", \"hypothesis\": \"RSFT training on CED-filtered data (2718 samples, mean CED=0.668). SFT warmup baseline: rel_f1=0.4057, evi_f1=0.798. Pass criteria: rel_f1 > 0.4057 AND evi_f1 > 0.798.\", \"wandb_run_id\": \"rsft-ced-r1\", \"conclusion\": \"success\", \"metrics\": {\"rel_f1\": 0.0483, \"num_preds\": 848, \"sft_baseline_rel_f1\": 0.4057, \"failure_mode\": \"relation_ontology_collapse_to_freetext\", \"epoch1_eval_loss\": 0.756, \"epoch2_eval_loss\": 0.759}, \"notes\": \"D037 修正: TaskEvalCallback 的 rel_f1=0.0483 是 eval bug（gold triples 未限制为 eval_max_docs 子集）。全量 eval 待跑。s44 全量 eval 已 PASS: rel_f1=0.4655, evi_f1=0.8087。\"}, \"mvp2_rsft_ced_scoring\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T05:27:32.788Z\", \"updated_at\": \"2026-05-15T05:33:16.769Z\", \"hypothesis\": \"CED scoring + filtering on 4 shard RSFT generations. top_k=1, f1_threshold=0.1. 21952 → 2718 selected (12.4%).\", \"conclusion\": \"success\", \"metrics\": {\"input_generations\": 21952, \"selected_samples\": 2718, \"unique_docs\": 2691, \"selection_rate\": 0.124, \"mean_f1\": 0.6157, \"mean_ced\": 0.6683, \"f1_range\": [0.1026, 1], \"zero_f1_samples\": 0, \"selection_strategy\": \"top_k=1\", \"f1_threshold\": 0.1}}, \"mvp2_rsft_gen_s0\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T01:39:26.572Z\", \"updated_at\": \"2026-05-15T05:21:50.725Z\", \"hypothesis\": \"RSFT generation shard 0/4: N=8 generations at T=0.7 with generation_config override (top_k=0). OOM fix: batch_size=1.\", \"parent\": \"mvp2_sft_warmup\", \"conclusion\": \"success\", \"notes\": \"[2026-05-15 05:01] 生成完成 682/682 docs (100%)。EXIT_CODE=143 是正常完成后的清理 SIGTERM。format_ok 99.6%, truncation_rate 10.1%, diversity 7.6/8。\"}, \"mvp2_rsft_gen_s3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T01:39:34.645Z\", \"updated_at\": \"2026-05-15T05:01:10.955Z\", \"hypothesis\": \"RSFT generation shard 3/4: N=8 generations at T=0.7 with generation_config override (top_k=0). OOM fix: batch_size=1.\", \"parent\": \"mvp2_sft_warmup\", \"conclusion\": \"success\", \"metrics\": {\"generation_count\": 5288, \"unique_docs\": 659, \"format_compliance\": 0.998, \"diversity_range\": \"7.5-7.8/8\", \"exit_code\": 0}}, \"mvp2_rsft_gen_s2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T01:39:32.299Z\", \"updated_at\": \"2026-05-15T04:37:31.632Z\", \"hypothesis\": \"RSFT generation shard 2/4: N=8 generations at T=0.7 with generation_config override (top_k=0). OOM fix: batch_size=1.\", \"parent\": \"mvp2_sft_warmup\", \"conclusion\": \"success\"}, \"mvp2_rsft_gen_s1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T01:39:29.894Z\", \"updated_at\": \"2026-05-15T04:37:14.926Z\", \"hypothesis\": \"RSFT generation shard 1/4: N=8 generations at T=0.7 with generation_config override (top_k=0). OOM fix: batch_size=1.\", \"parent\": \"mvp2_sft_warmup\", \"conclusion\": \"success\"}, \"mvp2_rsft_generate\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T00:09:41.289Z\", \"updated_at\": \"2026-05-15T01:32:10.047Z\", \"hypothesis\": \"RSFT generation phase: SFT model generates N=8 candidate outputs per training sample at T=0.7. CED scoring + filtering后作为 RSFT 训练数据。D031 pivot 方向。\", \"parent\": \"mvp2_sft_warmup\", \"conclusion\": \"failed\"}, \"mvp2_diversity_probe\": {\"status\": \"DONE\", \"created_at\": \"2026-05-15T00:02:19.966Z\", \"updated_at\": \"2026-05-15T01:31:34.495Z\", \"hypothesis\": \"RSFT viability check: SFT model output diversity at T=0.7/1.0 with N=8 generations. Pass criteria: unique triple-sets >= 5/8.\", \"conclusion\": \"success\", \"metrics\": {\"unique_triples_t07\": 5, \"unique_triples_t10\": 8, \"jaccard_t07\": 0.17, \"jaccard_t10\": 0.051, \"format_ok_rate_t07\": 0.5, \"format_ok_rate_t10\": 0.438, \"n_samples\": 3, \"n_generations\": 8, \"note\": \"unique_triples_t07 corrected from 7 to 5.0 (mean). Reviewer: format_ok ~34% after fix, 'diversity' was JSON key name variants not semantic diversity\"}, \"notes\": \"[2026-05-15 01:35] D034 独立验证结果: 200 docs 实际 diversity=7.11/8 (median=8.0), evidence diversity=5.43/8, format parse rate=90.2%。61.5% 文档达到 8/8 完全不同。之前监控报告的 mean_diversity=1.0/8 是监控计算 bug，非生成质量问题。diversity_probe 早期观察(7/8)是准确的。RSFT 前提成立。\"}, \"mvp2_eval_lr5e6_r1_ckpt100\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T23:00:57.035Z\", \"updated_at\": \"2026-05-15T01:30:01.493Z\", \"hypothesis\": \"P0 ckpt-100 eval: lr=5e-6 GRPO at step 100 (halfway point). Checkpoint-100 已保存。与 kl001_r4 的 step-100 (rel_f1=0.217) 形成直接对比。Pass criteria: rel_f1 > 0.30.\", \"parent\": \"mvp2_grpo_ced_lr5e6_r1\", \"metrics\": {\"rel_f1\": 0.0138, \"rel_precision\": 0.0132, \"rel_recall\": 0.0144, \"ign_f1\": 0.0138, \"evi_f1\": 0.8504, \"evi_precision\": 0.9256, \"evi_recall\": 0.7866, \"edcr\": 0.9876, \"format_ok_rate\": 0.999, \"field_compliance_rate\": 0.8162, \"evidence_format_rate\": 0.8162, \"tp\": 175, \"pred_count\": 13300, \"gold_count\": 12151, \"n_predictions\": 15498, \"n_truncated\": 181, \"n_documents\": 985, \"n_parseable\": 984, \"inference_time_seconds\": 5901.7}, \"conclusion\": \"negative\"}, \"mvp2_grpo_ced_lr5e6_r1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T19:21:08.231Z\", \"updated_at\": \"2026-05-15T01:29:06.862Z\", \"hypothesis\": \"D030/P0: lr=5e-6 (10x lower than ced_kl001_r4) prevents catastrophic forgetting while maintaining CED reward improvement. Community consensus GRPO+QLoRA lr=5e-6~1e-5. Pass criteria: ckpt-20 rel_f1 > 0.30. Extra monitoring: pred_count + recall trend.\", \"parent\": \"mvp2_grpo_ced_kl001_r4\", \"wandb_run_id\": \"grpo-s3-ced-lr5e6-r1\", \"notes\": \"[2026-05-15 01:08] D032 执行: PID 90080 killed (force_killed=true)。训练 step ~113/200。完整 lr5e-6 轨迹: ckpt-20→40→60→80 rel_f1 = 0.008/0.007/0.009/0.012，无恢复信号。GRPO+QLoRA 方向判死 (D031)，GPU 释放给 RSFT 流水线。\", \"conclusion\": \"killed\"}, \"mvp2_eval_lr5e6_r1_ckpt80\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T22:25:45.043Z\", \"updated_at\": \"2026-05-15T01:02:32.508Z\", \"hypothesis\": \"P0 ckpt-80 eval: lr=5e-6 GRPO at step 80. 训练轨迹继续——ckpt-20 FAIL (0.0077), ckpt-40/60 待出. Step 80 reward=0.283 (回升), format_reward=0.249. Pass criteria: rel_f1 > 0.30.\", \"parent\": \"mvp2_grpo_ced_lr5e6_r1\", \"notes\": \"[2026-05-15 08:56] 正常完成。rel_f1=0.0116，延续 ckpt-20/40/60 的平坦趋势 (0.007-0.012)。evi_f1=0.828 继续上升。lr5e6 轨迹: step 20→40→60→80 rel_f1 = 0.008/0.007/0.009/0.012，无恢复信号。cuda:2 已释放。\", \"conclusion\": \"negative\", \"metrics\": {\"rel_f1\": 0.0116, \"ign_f1\": 0.0116, \"precision\": 0.0109, \"recall\": 0.0124, \"evi_f1\": 0.828, \"evi_precision\": 0.928, \"evi_recall\": 0.748, \"edcr\": 0.993, \"format_ok_rate\": 0.999, \"field_compliance_rate\": 0.788, \"pred_count\": 13828, \"gold_count\": 12151, \"n_truncated\": 210, \"inference_time_seconds\": 6099}}, \"mvp2_eval_lr5e6_r1_ckpt60_r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T22:27:56.124Z\", \"updated_at\": \"2026-05-15T00:07:56.895Z\", \"hypothesis\": \"P0 ckpt-60 eval retry: 原 submit_on_allocated 失败 (pid=unknown). 手动 SSH 启动 /root/autodl-tmp/scripts/eval_lr5e6_ckpt60.sh. Pass criteria: rel_f1 > 0.30.\", \"parent\": \"mvp2_grpo_ced_lr5e6_r1\", \"conclusion\": \"negative\", \"notes\": \"[2026-05-15 08:07] 正常完成。rel_f1=0.0093，与 ckpt-20 (0.0077) / ckpt-40 (0.0071) 同一量级，无恢复信号。evi_f1=0.81 持续上升（ckpt-20: 0.628, ckpt-40: 0.758），证据抽取在改善但关系能力完全崩塌。结果路径: /root/autodl-tmp/eval_results/grpo_ced_lr5e6_ckpt60/metrics.json。cuda:1 已释放。\", \"metrics\": {\"rel_f1\": 0.0093, \"precision\": 0.0085, \"recall\": 0.0103, \"evi_f1\": 0.81, \"edcr\": 0.993, \"format_ok_rate\": 0.998, \"pred_count\": 14626, \"gold_count\": 12151, \"tp\": 125, \"inference_time_seconds\": 6152}}, \"mvp2_eval_lr5e6_r1_ckpt60\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T22:13:47.936Z\", \"updated_at\": \"2026-05-14T23:25:25.584Z\", \"hypothesis\": \"P0 ckpt-60 eval: lr=5e-6 GRPO at step 60. 训练轨迹数据点——ckpt-20 catastrophic forgetting (rel_f1=0.0077)，需看后续 checkpoint 是否恢复。Pass criteria: rel_f1 > 0.30.\", \"parent\": \"mvp2_grpo_ced_lr5e6_r1\", \"notes\": \"[2026-05-15 07:24] D031 清理: PID 108025 因 cd path 问题从未产出有效结果。已被 _r2 (PID 108185) 取代。标记 failed 关闭。\", \"conclusion\": \"failed\"}, \"mvp2_eval_lr5e6_r1_ckpt40_r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T21:41:34.558Z\", \"updated_at\": \"2026-05-14T23:11:56.267Z\", \"hypothesis\": \"Re-tracking orphan PID 101842 for P0 ckpt-40 eval (lr=5e-6 GRPO step 40). Original exp auto-failed due to cron/PID mismatch. Pass criteria: rel_f1 > 0.30.\", \"parent\": \"mvp2_grpo_ced_lr5e6_r1\", \"notes\": \"[2026-05-15 06:50] 全面状态检查: PID 101842 存活 (Rl, uptime 1:25), GPU 2: 10644 MiB/74% util. tmux mvp2_eval_lr5e6_r1_ckpt40 alive (创建于 05:25 UTC). 按 92s/batch 估算约 55/62 (89%), ETA ~10min (约UTC 07:00).\", \"conclusion\": \"negative\", \"metrics\": {\"rel_f1\": 0.0071, \"precision\": 0.0066, \"recall\": 0.0078, \"evi_f1\": 0.7584, \"evi_precision\": 0.9113, \"evi_recall\": 0.6494, \"edcr\": 0.9942, \"format_ok_rate\": 0.9939, \"field_compliance_rate\": 0.5675, \"pred_count\": 14434, \"gold_count\": 12151, \"tp\": 95, \"n_truncated\": 424, \"inference_time_seconds\": 6152}}, \"mvp2_eval_lr5e6_r1_ckpt20\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T20:44:21.167Z\", \"updated_at\": \"2026-05-14T22:12:16.372Z\", \"hypothesis\": \"P0 ckpt-20 early eval: lr=5e-6 GRPO at step 20. Pass criteria: rel_f1 > 0.30 (no catastrophic forgetting). Key MVP gate for P0.\", \"parent\": \"mvp2_grpo_ced_lr5e6_r1\", \"conclusion\": \"negative\", \"metrics\": {\"rel_f1\": 0.0077, \"rel_precision\": 0.0071, \"rel_recall\": 0.0084, \"evi_f1\": 0.628, \"evi_precision\": 0.855, \"evi_recall\": 0.496, \"edcr\": 0.993, \"format_ok_rate\": 0.991, \"field_compliance_rate\": 0.399, \"pred_count\": 14440, \"gold_count\": 12151, \"tp\": 102, \"n_truncated\": 587, \"inference_time_seconds\": 6370.4}}, \"mvp2_eval_lr5e6_rp_r2_ckpt20\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T21:44:56.448Z\", \"updated_at\": \"2026-05-14T22:06:40.812Z\", \"hypothesis\": \"P0+P1 ckpt-20 eval: lr=5e-6 + recall_penalty GRPO at step 20. Director killed rp_r2 training (loss divergence), but ckpt-20 eval needed to close P0+P1 comparison line. Pass criteria: rel_f1 > 0.30 AND pred_count >= 9720.\", \"parent\": \"mvp2_grpo_ced_lr5e6_rp_r2\", \"conclusion\": \"killed\", \"notes\": \"Director 指令 kill: 让 sft_baseline 独占 cuda:3。rp_r2 eval 优先级低，后面补。进度 11/62 (18%)。\"}, \"mvp2_eval_lr5e6_r1_ckpt40\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T21:25:00.579Z\", \"updated_at\": \"2026-05-14T21:43:33.438Z\", \"hypothesis\": \"P0 ckpt-40 eval: lr=5e-6 GRPO at step 40 (where f1_reward first rises to 0.038). Director 新判定框架: ckpt-20 FAIL + ckpt-40 PASS → P0 判 PASS。Pass criteria: rel_f1 > 0.30.\", \"parent\": \"mvp2_grpo_ced_lr5e6_r1\", \"conclusion\": \"failed\", \"notes\": \"Reviewer 确认 PID 101842 在 cuda:2 正常运行中（inference 5/62, 8%），占用 9710 MiB。原误判原因：kill 旧 PID 100555 后 cron 检测旧 PID 导致 5× dead 误判。实际进程未中断。由 _r2 条目接续追踪。\"}, \"mvp2_grpo_ced_lr5e6_rp_r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T20:04:55.831Z\", \"updated_at\": \"2026-05-14T21:40:50.174Z\", \"hypothesis\": \"D032/P0+P1 retry: lr=5e-6 + --ced_recall_penalty fixes both catastrophic forgetting (lr) and CED recall shortcut (penalty). Pass criteria: ckpt-20 rel_f1 > 0.30 AND pred_count >= 9720 (SFT 80%). Comparing vs P0 (lr5e6_r1) isolates CED shortcut fix contribution. Retry of rp_r1 which failed due to bash quoting.\", \"parent\": \"mvp2_grpo_ced_kl001_r4\", \"wandb_run_id\": \"grpo-s3-ced-lr5e6-rp-r2\", \"conclusion\": \"killed\", \"notes\": \"Director 决策 kill: loss 持续指数 divergence (step 10: 908 → step 15: 24,650 → step 20: 1.34e7)。根因: recall penalty 产生 5-10x 更强梯度，在 QLoRA 4-bit 下加剧 KL 爆炸，kl_coef=0.01 × KL=1.42e9 = 1.42e7 完全主导 loss。训练 step 39 被 kill。ckpt-20 将用于 eval 关闭 P0+P1 对比线。\"}, \"mvp2_eval_ced_kl001_r4_multi\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T17:59:22.291Z\", \"updated_at\": \"2026-05-14T21:27:25.338Z\", \"notes\": \"Director 指令: ckpt-30 评完即停。进程在 ckpt-40 推理 3% 时被 kill，非异常崩溃。已完成 6/9 个 ckpt eval: 10,20,30,50,60,90（ckpt-40 中断，ckpt-70/80 未执行）。F1 随 step 单调上升: 0.003→0.009→0.034→0.156→0.147→0.211。best=ckpt-90 (F1=0.211)。Evi-F1 稳定在 0.42-0.72，EDCR 随 step 下降（0.998→0.858）。结果路径: /root/autodl-tmp/eval_results/grpo_ced_kl001/\", \"conclusion\": \"killed\", \"metrics\": {\"checkpoint-10\": {\"f1\": 0.003, \"ign_f1\": 0.003, \"evi_f1\": 0.72, \"edcr\": 0.9983, \"format_ok_rate\": 0.999}, \"checkpoint-20\": {\"f1\": 0.0088, \"ign_f1\": 0.0088, \"evi_f1\": 0.423, \"edcr\": 0.9954, \"format_ok_rate\": 0.999}, \"checkpoint-30\": {\"f1\": 0.0338, \"ign_f1\": 0.0338, \"evi_f1\": 0.5889, \"edcr\": 0.9798, \"format_ok_rate\": 1}, \"checkpoint-50\": {\"f1\": 0.1563, \"ign_f1\": 0.1563, \"evi_f1\": 0.5643, \"edcr\": 0.8858, \"format_ok_rate\": 0.999}, \"checkpoint-60\": {\"f1\": 0.1467, \"ign_f1\": 0.1467, \"evi_f1\": 0.5763, \"edcr\": 0.9062, \"format_ok_rate\": 1}, \"checkpoint-90\": {\"f1\": 0.2108, \"ign_f1\": 0.2108, \"evi_f1\": 0.5666, \"edcr\": 0.8584, \"format_ok_rate\": 1}}}, \"mvp2_grpo_ced_lr5e6_rp_r1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T19:44:15.272Z\", \"updated_at\": \"2026-05-14T20:44:07.125Z\", \"hypothesis\": \"D032/P0+P1: lr=5e-6 + --ced_recall_penalty fixes both catastrophic forgetting (lr) and CED recall shortcut (penalty). Pass criteria: ckpt-20 rel_f1 > 0.30 AND pred_count >= 9720 (SFT 80%). Comparing vs P0 isolates CED shortcut fix contribution.\", \"parent\": \"mvp2_grpo_ced_kl001_r4\", \"notes\": \"Director D-URGENT: 与 rp_r2 冲突，同 GPU(cuda:3) 同 output_dir(/root/autodl-tmp/grpo_ced_lr5e6_rp/)。PID 94055 killed，保留 rp_r2 (PID 94758) 因其有标准化 submit_training_job 记录。\", \"conclusion\": \"failed\"}, \"mvp2_grpo_ced_lr5e6_p1_r1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T19:28:59.245Z\", \"updated_at\": \"2026-05-14T20:31:06.969Z\", \"hypothesis\": \"D031/P0+P1: lr=5e-6 + --ced_recall_penalty fixes both catastrophic forgetting (lr) and CED recall shortcut (penalty). Pass criteria: ckpt-20 rel_f1 > 0.30 AND pred_count >= 15000 (SFT 80%). Comparing vs P0 isolates CED shortcut fix contribution.\", \"conclusion\": \"killed\", \"notes\": \"Superseded by mvp2_grpo_ced_lr5e6_rp_r1 per Director D032. Never submitted.\"}, \"mvp2_eval_ced_kl001_r4_step90\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T18:19:58.623Z\", \"updated_at\": \"2026-05-14T20:01:45.201Z\", \"hypothesis\": \"Eval true best checkpoint (step 90, reward=1.370). Critical after ckpt-50 showed reward hacking (rel_f1 -24.9pp). If step 90 also fails, CED reward design has fundamental issue.\", \"parent\": \"mvp2_grpo_ced_kl001_r4\", \"notes\": \"2026-05-15 03:20 UTC: ckpt-90 inference 31/62 (50%), ~45 min remaining. Started 02:32 UTC.\", \"metrics\": {\"rel_f1\": 0.2108, \"ign_f1\": 0.2108, \"evi_f1\": 0.5666, \"edcr\": 0.8584, \"pred_count\": 11160, \"n_truncated\": 22, \"format_ok_rate\": 1, \"n_documents\": 985}, \"conclusion\": \"negative\"}, \"mvp2_eval_ced_kl001_r4_ckpt7080\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T19:50:04.595Z\", \"updated_at\": \"2026-05-14T19:58:46.631Z\", \"hypothesis\": \"Re-run failed ckpt-70/80 eval from crashed high eval (cuda:3 OOM). Completes 10-checkpoint trajectory for paper negative result analysis.\", \"parent\": \"mvp2_grpo_ced_kl001_r4\", \"conclusion\": \"failed\", \"notes\": \"Process died shortly after start - likely OOM on cuda:3 (same issue as high eval crash during ckpt-70). cuda:3 may have insufficient free VRAM for eval. ckpt-70/80 will be covered by multi eval on cuda:2.\"}, \"mvp2_eval_ced_kl001_r4_high\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T18:19:07.637Z\", \"updated_at\": \"2026-05-14T19:47:58.282Z\", \"hypothesis\": \"High-end checkpoint eval (60,70,80,90) on cuda:3, complementing cuda:2 low-end eval. Step 90 is true best checkpoint (reward=1.370). D024 directive.\", \"parent\": \"mvp2_grpo_ced_kl001_r4\", \"notes\": \"1/4 checkpoints completed (ckpt-60). Process crashed during ckpt-70 inference at 8% - likely OOM or killed. cuda:3 still has 9503 MiB residual. ckpt-90 eval running separately on cuda:1 (mvp2_eval_ced_kl001_r4_step90).\", \"conclusion\": \"failed\", \"metrics\": {\"checkpoint_60\": {\"rel_f1\": 0.1467, \"ign_f1\": 0.1467, \"precision\": 0.1909, \"recall\": 0.1192, \"evi_f1\": 0.5763, \"edcr\": 0.9062, \"pred_count\": 10041, \"gold_count\": 12151, \"n_truncated\": 16, \"format_ok_rate\": 1}, \"note\": \"Only ckpt-60 completed. Process died during ckpt-70 inference at 8% (5/62 batch). ckpt-80/90 never started.\"}}, \"mvp2_eval_ced_kl001_r4_step100\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T18:08:31.821Z\", \"updated_at\": \"2026-05-14T19:41:30.318Z\", \"hypothesis\": \"Eval ced_kl001_r4 last checkpoint (step 100) to compare with best-reward checkpoint (step 50). If best ≠ last, the gap measures training stability under batch_size=1 GRPO variance.\", \"parent\": \"mvp2_grpo_ced_kl001_r4\", \"notes\": \"2026-05-15 03:20 UTC: ckpt-100 inference 48/62 (77%), ~20 min remaining. Started 02:09 UTC.\", \"metrics\": {\"rel_f1\": 0.2167, \"ign_f1\": 0.2167, \"precision\": 0.2849, \"recall\": 0.1749, \"evi_f1\": 0.5746, \"evi_precision\": 0.5244, \"evi_recall\": 0.6353, \"edcr\": 0.8539, \"pred_count\": 7460, \"gold_count\": 12151, \"tp\": 2125, \"n_truncated\": 21, \"format_ok_rate\": 1}, \"conclusion\": \"negative\"}, \"mvp2_eval_ced_kl001_r4_ckpt90\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T18:18:13.270Z\", \"updated_at\": \"2026-05-14T19:17:36.777Z\", \"hypothesis\": \"Eval ced_kl001_r4 best-reward checkpoint (step 90, reward=1.370, f1=0.720) — this is the primary MVP-2 judgment checkpoint. If evi_f1 ≥ SFT baseline (0.7979) + 2pp = 0.8179, MVP-2 passes.\", \"parent\": \"mvp2_grpo_ced_kl001_r4\", \"conclusion\": \"killed\", \"notes\": \"重复条目，被 mvp2_eval_ced_kl001_r4_step90 (cuda:1, PID 83207, 有 cron 监控) 取代。本条目无 cron、无独立进程。\"}, \"mvp2_eval_ced_kl001_r4_ckpt10\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T17:59:08.638Z\", \"updated_at\": \"2026-05-14T19:14:08.763Z\", \"notes\": \"Eval 完成（由 multi eval 执行）。ckpt-10 rel_f1=0.003 catastrophic — 模型几乎丧失 relation 抽取能力 (34 TP / 10839 pred)，但 evi_f1=0.72 和 edcr=0.998 反而高。GRPO 训练极早期就严重损害 relation 能力。\", \"conclusion\": \"success\", \"metrics\": {\"rel_f1\": 0.00296, \"rel_precision\": 0.00314, \"rel_recall\": 0.0028, \"evi_f1\": 0.72, \"evi_precision\": 0.6429, \"evi_recall\": 0.8182, \"edcr\": 0.9983, \"n_parseable\": 984, \"n_truncated\": 24, \"n_predictions\": 11621, \"tp\": 34, \"pred_count\": 10839, \"gold_count\": 12151, \"inference_time_seconds\": 5211.4}}, \"mvp2_eval_ced_kl001_r4_early\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T17:12:53.581Z\", \"updated_at\": \"2026-05-14T18:31:18.065Z\", \"notes\": \"**Checkpoint-50 eval 完成，结果极差——MVP-2 双指标均 FAIL：**\\\\n\\\\n- rel_f1: 0.1563 vs SFT 0.4057 (Δ=-24.9pp)，远低于 -5pp 阈值\\\\n- evi_f1: 0.5643 vs SFT 0.7979 (Δ=-23.4pp)，需 +2pp 却暴跌\\\\n- EDCR: 0.8858 vs SFT 0.7118 (Δ=+17.4pp)，唯一改善项\\\\n- recall 崩塌 (0.117 vs gold 12151)，precision 也低 (0.236)\\\\n\\\\n**诊断**: training reward 上升 (1.101) 但 eval F1 崩塌，说明 GRPO 训练在优化 reward proxy 而非实际任务表现。模型学会了高 EDCR（少引用 distractor）但牺牲了大量 recall。pred_count=6032 vs gold=12151，预测数量严重不足。\\\\n\\\\n仍需等待 step-90 (reward=1.37) 的 eval 结果——如果 step-90 也崩塌，则 CED reward 设计需要根本性修改。\", \"conclusion\": \"negative\", \"metrics\": {\"f1\": 0.1563, \"ign_f1\": 0.1563, \"evi_f1\": 0.5643, \"edcr\": 0.8858, \"precision\": 0.2356, \"recall\": 0.1169, \"evi_precision\": 0.4864, \"evi_recall\": 0.6721, \"format_ok_rate\": 0.999, \"n_parseable\": 984, \"n_truncated\": 11, \"n_predictions\": 9250, \"tp\": 1421, \"pred_count\": 6032, \"gold_count\": 12151}}, \"mvp2_grpo_flatnli_r6\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T17:25:07.083Z\", \"updated_at\": \"2026-05-14T18:17:52.909Z\", \"hypothesis\": \"Flat-NLI reward with kl_coef=0.01 + num_generations=8 from SFT scratch (not resume). 100-step probe to verify stability. Same D020 config as ced_kl001_r4 (which is healthy). Tests whether flat-NLI reward type works under stable training config.\", \"parent\": \"mvp2_grpo_flatnli_r5\", \"notes\": \"D020 配置：kl_coef=0.01 + num_generations=8 + save_steps=10 + max_steps=100。从 SFT 全新训练。\\n\\n**D024 Kill — Mode Collapse Confirmed (step 25)**:\\n- frac_zero_std: 0.1→0.4→0.6→0.7→0.9 (单调上升，破 0.8 阈值)\\n- f1_reward=0, flat_nli_reward=0 — 抽取和 NLI 完全死亡\\n- reward 100% format hacking (0.293)\\n- completion_length 缩短 773→586→399\\n- KL step 5 爆炸至 1.23 亿后回落\\n\\n**科学结论**: D020 配置下 flat-NLI reward 信号不足以维持 GRPO 多样性。与 extract_r4 (step 10 collapse) 模式一致。CED 是三种 reward type 中唯一能稳定训练的。\", \"conclusion\": \"negative\", \"metrics\": {\"steps_completed\": 25, \"final_frac_zero_std\": 0.9, \"final_f1_reward\": 0, \"final_flat_nli_reward\": 0, \"final_format_reward\": 0.293, \"collapse_step\": 25}}, \"mvp2_grpo_ced_kl001_r4\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T15:32:32.529Z\", \"updated_at\": \"2026-05-14T18:11:53.975Z\", \"notes\": \"D020 配置：kl_coef=0.01 + num_generations=8 + save_steps=10 + max_steps=100 探测。✅ F1 门控已包含。\\n\\n**训练完成 (100/100 steps, EXIT_CODE=0, 2h31m)**:\\n- Final (step 100): reward=1.195, f1=0.573, ced=0.328, frac_zero_std=0.2, KL=0.118\\n- **True best: step 90** (reward=1.370, f1=0.720, ced=0.353) — 比 step 50 (1.101) 高 24%\\n- Reward trajectory: 0.22→1.37 (~5x 提升)，batch_size=1 方差大但整体上升\\n- 无 mode collapse（frac_zero_std 从早期 0.3-0.8 降至后半程 0.0-0.2）\\n- KL 稳定（0.10-0.15 range，kl_coef=0.01 控制有效）\\n- 所有 10 个 checkpoint 可用 (10-100)\\n\\n**Eval 覆盖**:\\n- cuda:1: ckpt-50 eval (mvp2_eval_ced_kl001_r4_early)\\n- cuda:2: ckpt 10-80 multi eval (mvp2_eval_ced_kl001_r4_multi)\\n- cuda:0: ckpt 90+100 eval (mvp2_eval_ced_kl001_r4_last)\", \"conclusion\": \"success\", \"metrics\": {\"final_step\": 100, \"train_runtime_s\": 9069.88, \"reward_final\": 1.195, \"f1_reward_final\": 0.573, \"ced_reward_final\": 0.328, \"format_reward_final\": 0.293, \"frac_zero_std_final\": 0.2, \"kl_final\": 0.118, \"loss_final\": -0.009, \"grad_norm_final\": 0.14, \"entropy_final\": 0.067, \"completion_length_mean_final\": 520.8, \"best_reward_step\": 90, \"best_reward\": 1.37, \"best_f1_reward\": 0.72, \"best_ced_reward\": 0.353}}, \"mvp2_grpo_extract_r4\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T16:54:59.403Z\", \"updated_at\": \"2026-05-14T17:40:25.731Z\", \"hypothesis\": \"Extraction-only reward (format×0.3, f1×3.0, ced=0) with kl_coef=0.01 + num_generations=8 trains stably. 100-step probe parallel ablation with ced_kl001_r4 (CED reward) to compare reward type impact under identical stability config.\", \"parent\": \"mvp2_grpo_extract_r3\", \"notes\": \"D020 配置：kl_coef=0.01 + num_generations=8 + save_steps=10 + max_steps=100 探测。与 ced_kl001_r4 (cuda:0) 构成并行 ablation——相同稳定配置、不同 reward type (extract-only vs CED)。\\n\\n**Mode collapse confirmed → KILLED at step ~30**:\\n- step 5: frac_zero_std=0.2, f1=0.016（初始信号）\\n- step 10-30: frac_zero_std=0.7-0.8, f1_reward=0（完全 collapse）\\n- reward 全部来自 format_reward (~0.29)，模型放弃 extraction\\n- 对比 ced_kl001_r4 同期在 step 20-40 恢复（frac→0.0, f1→0.240），extract_r4 无恢复信号\\n\\n**科学价值**：证明 extraction-only reward（format+f1, 无 CED）在 D020 配置下无法维持 GRPO 多样性。CED reward 通道可能是帮助 ced_kl001_r4 摆脱初期 mode collapse 的关键因素。\", \"conclusion\": \"killed\"}, \"mvp2_grpo_flatnli_r5\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T16:55:02.197Z\", \"updated_at\": \"2026-05-14T17:26:55.692Z\", \"hypothesis\": \"Flat-NLI reward with kl_coef=0.01 + num_generations=8 prevents mode collapse. Resume from flatnli_r3 checkpoint-100 (healthy). 100-step probe (steps 100→200) to verify stability before full run.\", \"parent\": \"mvp2_grpo_flatnli_r4\", \"notes\": \"Director 决策 kill：从 r3 (kl_coef=0) checkpoint-100 恢复后立即崩溃。frac_zero_std: 0.0(r3)→0.9(step 105)→0.7→0.5→0.8(step 120)，0.5-0.9 震荡无收敛。KL 全程 0.44-0.49 高位。根因：kl_coef=0 累积的 policy 漂移 + kl_coef=0.01 penalty 形成对抗。教训：不能从 kl_coef=0 的 checkpoint 恢复加 KL penalty。flatnli_r6 从 SFT 全新训练。\", \"conclusion\": \"killed\"}, \"mvp2_sft_eval_r3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T13:52:38.174Z\", \"updated_at\": \"2026-05-14T17:06:57.010Z\", \"conclusion\": \"success\", \"metrics\": {\"rel_f1\": 0.4057, \"ign_f1\": 0.4057, \"evi_f1\": 0.7979, \"edcr\": 0.7118, \"precision\": 0.4043, \"recall\": 0.407, \"evi_precision\": 0.8035, \"evi_recall\": 0.7924, \"format_ok_rate\": 0.998, \"format_compliance_rate\": 0.626, \"n_parseable\": 617, \"n_truncated\": 367, \"n_predictions\": 18815}, \"notes\": \"统一 eval 代码验证：r3 与 r2 所有指标完全一致（差异=0.00pp），含 _repair_truncated_json 的统一 eval 脚本未引入任何偏差。SFT baseline 可靠确认：rel_f1=0.4057, evi_f1=0.7979, edcr=0.7118。983 parseable / 617 field_complete / 367 truncated / 18815 predictions。\"}, \"mvp2_grpo_extract_r3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T12:31:48.781Z\", \"updated_at\": \"2026-05-14T16:59:20.304Z\", \"notes\": \"Negative result (756/756 steps completed). 两阶段行为：(1) step 1-520 f1_reward 在 0.02-0.49 波动，completion length ~43 tokens 稳定，看似健康；(2) 实际最后 100+ 步 grad_norm=0, frac_reward_zero_std=1.0, loss=0.0, entropy≈0.005。f1 波动是 SFT 初始化残留，非 GRPO 学习。停滞机制：kl_coef=0 + num_generations=4 → 4 个相同输出 → reward_std=0 → GRPO advantage=0 → 梯度为零。与 ced_r5 的差异：无 CED reward 通道，模型没 drift 到短输出（保持在 SFT 水平），但也完全停止学习。科学价值：证明 num_generations=4 不足以维持 GRPO 多样性，kl_coef=0 下 extraction-only 停滞而 CED collapse 更严重。\", \"conclusion\": \"negative\"}, \"mvp2_grpo_flatnli_r4\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T15:32:31.804Z\", \"updated_at\": \"2026-05-14T16:56:12.080Z\", \"notes\": \"Director 指令 kill: kl=0+gen=4 配置已在 ced_r5/extract_r3/flatnli_r3 三个实验崩塌，统一切到 kl=0.01+gen=8。flatnli_r4 运行 step 104→~130（~30 min），step_time ~34s/step。用 flatnli_r5 从 checkpoint-100 重启。\", \"conclusion\": \"killed\"}, \"mvp2_grpo_ced_kl001\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T12:32:53.111Z\", \"updated_at\": \"2026-05-14T15:33:06.208Z\", \"notes\": \"三次失败：r1 --lr 不识别 (EXIT_CODE=2)，r2 conda 未激活 python not found (EXIT_CODE=127)，r3 缺 --data_dir。已在 r4 修正所有问题。\", \"hypothesis\": \"kl_coef=0.01 (vs r5 kl_coef=0.0) prevents CED mode collapse while keeping QLoRA 4-bit compatible — answers whether KL regularization is necessary\", \"conclusion\": \"failed\"}, \"mvp2_grpo_ced_r5\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T12:31:45.606Z\", \"updated_at\": \"2026-05-14T15:32:21.817Z\", \"notes\": \"⚠️ Mode collapse confirmed: step 250+ f1_reward=0, completion length collapsed to fixed 34 tokens, frac_reward_zero_std=0.9-1.0. Model learned to produce short fixed-format output maximizing ced_reward (0.99) + format_reward (0.3) while abandoning relation extraction (f1=0). Early checkpoints (pre-collapse) lost due to save_total_limit=5 — only steps 400-480 remain, all post-collapse. Current checkpoints likely unusable for eval.\", \"conclusion\": \"negative\"}, \"mvp2_grpo_flatnli_r3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T12:31:52.782Z\", \"updated_at\": \"2026-05-14T15:27:55.267Z\", \"notes\": \"Director 指令 kill：NLI 推理在 CPU 导致 10x 减速（~100-125s/step vs 应有 ~12s/step）。训练本身健康——step 104/756, grad_norm=0.37, f1 从 step 84 起出现, flat_nli_reward=0.52, entropy=0.046。Checkpoint 已备份。修复 --reward_device cuda 后以 flatnli_r4 重启。\", \"conclusion\": \"killed\"}, \"mvp2_sft_eval_r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T12:45:46.160Z\", \"updated_at\": \"2026-05-14T14:54:07.338Z\", \"conclusion\": \"success\", \"metrics\": {\"rel_f1\": 0.4057, \"ign_f1\": 0.4057, \"evi_f1\": 0.7979, \"edcr\": 0.7118, \"precision\": 0.4043, \"recall\": 0.407, \"evi_precision\": 0.8035, \"evi_recall\": 0.7924, \"format_ok_rate\": 0.998, \"format_compliance_rate\": 0.626, \"n_parseable\": 617, \"n_truncated\": 367, \"n_predictions\": 18815, \"inference_time_seconds\": 6484.7}}, \"mvp2_sft_eval\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T07:10:37.449Z\", \"updated_at\": \"2026-05-14T12:46:04.523Z\", \"conclusion\": \"killed\", \"notes\": \"Killed intentionally to restart with batch_size=16 (was batch_size=4, ~6h → ~1.5h). Director approved.\"}, \"mvp2_grpo_flatnli_r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T12:10:23.287Z\", \"updated_at\": \"2026-05-14T12:30:08.865Z\", \"conclusion\": \"killed\", \"notes\": \"Killed: Director 指令暂不提交 r2，等原始 flatnli 分析完再决定配置。\"}, \"mvp2_grpo_extract_r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T12:10:19.532Z\", \"updated_at\": \"2026-05-14T12:30:08.099Z\", \"conclusion\": \"killed\", \"notes\": \"Killed: Director 指令暂不提交 r2，等原始 extract 分析完再决定配置。\"}, \"mvp2_grpo_ced_r4\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T12:10:15.698Z\", \"updated_at\": \"2026-05-14T12:30:06.177Z\", \"conclusion\": \"killed\", \"notes\": \"Killed: 上一 session 使用 kl_coef=0.0/lr=5e-5 启动，但 Director 要求 D009 配置 (kl_coef=0.5, lr=5e-6, warmup_steps=200)。需等 extract/flatnli 分析完再用正确配置重新提交。\"}, \"mvp2_grpo_extract\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T07:10:35.796Z\", \"updated_at\": \"2026-05-14T12:25:32.094Z\", \"hypothesis\": \"Extraction-only reward (format+F1, no CED) establishes GRPO baseline — CED r3 should exceed this on Evi-F1\", \"conclusion\": \"failed\", \"notes\": \"KL divergence explosion at step 5 due to kl_coef=0.05 + QLoRA 4-bit incompatibility (D008). QLoRA quantization noise makes ref/policy log-prob divergence unreliable, causing KL values to reach 10^8-10^11. Same root cause as r3 and flatnli. Fix: kl_coef=0.0 in r2 retries.\"}, \"mvp2_grpo_flatnli\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T07:10:33.848Z\", \"updated_at\": \"2026-05-14T12:13:34.747Z\", \"hypothesis\": \"Flat-NLI reward (non-contrastive) improves Evi-F1 over extraction-only but less than CED — validates contrastive component's incremental value\", \"conclusion\": \"failed\", \"notes\": \"KL divergence explosion at step 5 due to kl_coef=0.05 + QLoRA 4-bit incompatibility (D008). QLoRA quantization noise makes ref/policy log-prob divergence unreliable. Same root cause as r3 and extract. Fix: kl_coef=0.0 in r2 retries.\"}, \"mvp2_grpo_ced_r3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T11:47:53.099Z\", \"updated_at\": \"2026-05-14T12:09:23.005Z\", \"hypothesis\": \"CED reward with balanced weights (format×0.3, f1×3.0, ced×1.0) + stable training (num_iterations=1, KL early stop at 100) + kl_coef=0.05 improves Evi-F1 over SFT baseline\", \"conclusion\": \"failed\", \"notes\": \"KL divergence explosion at step 5: first pass KL=4.4M, second pass KL=69.5B (threshold=100). KL early stopping correctly triggered, model saved but no useful training occurred.\\n\\nRoot cause: single-GPU training without --gradient_accumulation_steps (effective batch=1) → extremely noisy gradients → policy diverged from reference in 5 steps. Combined with QLoRA merge rounding amplifying initial policy-reference gap.\\n\\nKey metrics at step 5: loss=269987, kl=4.4M, entropy=0.084 (near 0), format_reward=0.10, f1_reward=0.05, ced_reward=0.15, grad_norm=0.16. EXIT_CODE=129 is artifact of KL early stop exit path.\\n\\nerror_type: hyperparameter | can_auto_fix: false\\nFix options: (1) add --gradient_accumulation_steps 16 for effective batch ~16; (2) reduce lr from 5e-5 to 5e-6; (3) increase kl_coef from 0.05 to 0.5; (4) lr warmup steps\"}, \"mvp2_grpo_ced_r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T10:58:11.663Z\", \"updated_at\": \"2026-05-14T11:31:49.724Z\", \"conclusion\": \"killed\"}, \"mvp2_grpo_ced_r1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T08:02:41.858Z\", \"updated_at\": \"2026-05-14T10:37:23.856Z\", \"conclusion\": \"killed\", \"notes\": \"Mode collapse diagnosed at step 80/189 (F1=0.001, format reward hacking). Root causes and fixes applied to grpo_trainer.py:\\n\\n(A) Checkpoint: save_strategy was \\\"epoch\\\" → now supports --save_steps/--save_total_limit CLI args, defaults to steps-based saving. Validated: checkpoint-1/2 saved in dry-run.\\n\\n(B) Reward weighting: all 3 rewards (format/f1/ced) were equally summed by TRL → added WeightedRewardFn wrapper + --format_reward_weight/--f1_reward_weight/--ced_reward_weight CLI args. Dry-run confirmed weighting works (format raw=0.1 × w=0.3 → 0.03).\\n\\n(C) Clip ratio: num_iterations=1 (default) meant single pass, ratio≡1, clipping never activated → added --num_iterations CLI arg (set to 2 in r2). Also added --max_steps, --kl_coef (beta). Dry-run clip_ratio=0 expected (zero reward variance → zero advantage → no update needed).\\n\\n(D) Added --save_total_limit CLI arg (previously hardcoded to 2, now configurable).\\n\\nDry-run validated: 2 steps completed, checkpoints saved, no OOM with num_iterations=2 on 4xRTX5090. completions/clipped_ratio=1.0 (all hit max_completion_length=1024) — expected for cold-start without warmup.\"}, \"mvp2_grpo_ced\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T07:10:31.165Z\", \"updated_at\": \"2026-05-14T08:00:02.874Z\", \"conclusion\": \"failed\", \"notes\": \"失败原因: grpo_trainer.py:109 f1_reward_fn 中 p.get(\\\"tail\\\", \\\"\\\").lower() 报 AttributeError: 'NoneType' — 某些 parsed triple 的 \\\"tail\\\" 字段为 None，dict.get 有 key 时不返回 default | 运行 ~36min 后崩溃 | 修复方案: 用 (p.get(\\\"tail\\\") or \\\"\\\") 模式处理 None | error_type: infrastructure | can_auto_fix: true\"}, \"precompute_nli_train\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T07:05:48.887Z\", \"updated_at\": \"2026-05-14T07:35:24.549Z\", \"conclusion\": \"success\"}, \"mvp2_sft_warmup\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T06:09:47.819Z\", \"updated_at\": \"2026-05-14T07:10:19.285Z\", \"conclusion\": \"success\", \"metrics\": {\"eval_loss\": 0.72, \"accuracy\": 0.835}}, \"smoke_test_grpo\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T05:20:00.970Z\", \"updated_at\": \"2026-05-14T06:09:18.626Z\", \"conclusion\": \"success\"}, \"mvp1_ced_signal\": {\"status\": \"DONE\", \"created_at\": \"2026-05-14T04:48:46.220Z\", \"updated_at\": \"2026-05-14T05:48:05.545Z\", \"conclusion\": \"success\", \"metrics\": {\"mean_margin\": 0.48, \"discrimination_accuracy\": 0.815, \"pearson_r_margin_jaccard\": 0.34, \"pass\": true}}}, \"count\": 242, \"total\": 242, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.7905}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-19T12:39:56.239Z_

<details><summary>↩ Tool result · `toolu_018vBtV3LCreagJfjs3U74QX`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/ROADMAP.md\", \"content\": \"# faith-evidence-ie — Research Dashboard\\n\\n> 最后更新: 2026-05-19 05:43 UTC | 更新原因: D115 8B RSFT 完成 + D114 1.7B Method A 裁决 + D112 进展 + 14B SFT 启动 + Wave 1 全部完成\\n\\n## 核心方向\\nFREIGE: LLM-based evidence-grounded DocRE 系统性研究。3 贡献：RSFT+NLI 有效性 / Decoupling spectrum / Scale-dependent evidence tax。详见 paper_framing.md。\\n\\n## 当前进展\\n- **阶段**: 🚀 Research + 审稿并行（Round 1 = 3.0 Findings，目标 4.0 Main）\\n- **Wave 1**: ✅ 全部完成（SFT s43/s44, GRPO bf16 G=4, Random RSFT）\\n- **Scaling seeds (plan_019)**: 8B 2-seed RSFT 完成（D115: s44=0.5451, variance 0.53pp）；1.7B s43/s44 重跑中（D114 Method A）\\n- **D112 full pipeline**: Step 3 RSFT 训练中 cuda:0（验证 RSFT 在强 SFT base s44 上的泛化性）\\n- **14B SFT (plan_017)**: cuda:1+2 运行中（2-GPU ZeRO-3, D108）\\n- **关键数值汇总**:\\n\\n| Scale | SFT mean (seeds) | RSFT mean (seeds) | Δ ign_f1 | SFT std | RSFT std |\\n|-------|-------------------|--------------------|----------|---------|----------|\\n| 1.7B | 0.4464 (3) | 0.5122 (1, s42 base) | +6.58pp | 2.79pp | — |\\n| 4B | 0.4358 (3) | 0.4482 (3, Method A) | +1.24pp | 3.80pp | 0.51pp |\\n| 8B | 0.4866 (2) | 0.5414 (2, Method A) | +5.48pp | 2.62pp | 0.53pp |\\n\\n- **RSFT 稳定化效应**: 4B variance 3.80→0.51pp (7.5x)，8B variance 2.62→0.53pp (5x)\\n- **CED 价值**: CED RSFT (0.4482) > Random RSFT (0.4114) > SFT (0.3974)，+3.68pp gap\\n- **GRPO**: bf16 ckpt-100 ign_f1=0.4431 无 catastrophic forgetting（D110），QLoRA 是 confound\\n\\n## 投稿目标\\n- **EMNLP 2026 Main** (ARR July cycle, ~July 15-25, **~57 天**)\\n\\n## 实验路线（3 层优先级）\\n\\n### Tier 1 — Main 必要条件\\n| 实验 | Plan ID | 状态 |\\n|------|---------|------|\\n| D102 k=1 方法论修正 | D102 | ✅ 完成 |\\n| SFT 4B s43 + s44 + s42 reeval | plan_w3_sft_seeds | ✅ 完成 (D111) |\\n| GRPO bf16 G=4 clean control | plan_015 | ✅ 完成 (D110/D113) |\\n| Random k=1 RSFT baseline | plan_w18_random | ✅ 完成 (D109) |\\n| 8B RSFT s44 seed expansion | plan_019 (8B) | ✅ 完成 (D115) |\\n| D112 RSFT from SFT s44 | plan_d112 | 🟡 Step 3 训练中 cuda:0 |\\n| 1.7B RSFT s43/s44 重跑 | plan_019 (1.7B) | 🟡 s43_r2 提交中 cuda:3 |\\n| 14B SFT (第 4 尺度) | plan_017 | 🟡 训练中 cuda:1+2 |\\n\\n### Tier 2 — 大幅加分\\n| 实验 | Plan ID | 状态 |\\n|------|---------|------|\\n| 14B RSFT + no-evidence + eval | plan_017 (后续) | pending（等 SFT 完成） |\\n| NLI model ablation | plan_010 | pending |\\n| Evidence tax 机制分析 | plan_020 | pending |\\n| Deep error analysis | plan_021 | pending |\\n\\n### Tier 3 — 锦上添花\\n| 实验 | Plan ID | 状态 |\\n|------|---------|------|\\n| CDR/GDA 跨领域 | plan_018 | P2（无 evidence 标注） |\\n| 第三模型家族 | plan_022 | pending |\\n| DocKS-RAG/LMRC 复现 | plan_023 | pending |\\n\\n## 从 3.0 → 4.0 路径\\n| 里程碑 | 预期评分 | 状态 |\\n|--------|---------|------|\\n| Wave 1 完成 + D112 | 3.0 → 3.5 | 🟡 D112 step 3 训练中 |\\n| + 1.7B/8B multi-seed 统计力 | 3.5 | 🟡 8B done, 1.7B 重跑中 |\\n| + 14B 第 4 尺度档 | 3.5 → 3.75 | 🟡 SFT 训练中 |\\n| + Mechanistic + error analysis | 3.75 → 4.0 | pending |\\n\\n## GPU 预算\\n- 本项目：rtx5090-4x cuda:0-3（4 张 RTX 5090）\\n- 当前：4/4 在用（D112 step3 / 14B SFT×2 / 1.7B RSFT）\\n- 剩余估算：Tier 1 ~15h + Tier 2 ~65h + Tier 3 ~100h\\n\\n## 近期任务\\n- [x] Wave 1 全部完成（SFT seeds, GRPO bf16, Random RSFT）\\n- [x] 8B RSFT s44 eval (D115: 0.5451, variance 压缩 5x)\\n- [x] 4B SFT s42 D076 reeval (D111: 0.3974)\\n- [ ] D112 step 3 → step 4 eval（cuda:0, ~1.5h total）\\n- [ ] 1.7B RSFT s43_r2 + s44_r2 + eval（cuda:3, ~2-3h total）\\n- [ ] 14B SFT 完成 → 14B RSFT + no-evidence + eval（cuda:1+2, ~8h SFT + 后续）\\n- [ ] experiment_plan.yaml 全面同步 registry\\n- [ ] paper_framing.md 更新（D112 结果 + 8B 2-seed + variance 压缩 narrative）\\n- [ ] 重新提交论文审稿\\n\\n## 关键风险\\n- **D112 结果待定**: 如 RSFT-from-s44 > SFT s44 (0.4734) → Claim 1 robust；否则需 reframe\\n- **8B RSFT evidence quality trade-off**: EDCR 从 0.65-0.67 降到 0.62（RE↑/evidence precision↓），论文需讨论\\n- **1.7B surpasses claim**: 现在更强（1.7B RSFT 0.5122 > 8B SFT mean 0.4866 +2.56pp），但仍需 1.7B multi-seed 确认\\n- **14B 显存**: 2-GPU ZeRO-3 已启动且正常（D108 验证），后续 RSFT 可能需要调参\\n- **EDCR 缺人工验证**: plan_013 取消，用 per-relation 分析 + Limitations 缓解\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D116 | 2026-05-19 | D116: D112 结果无效（QLoRA confound），必须用 bf16 LoRA 重跑 s | d112_rsft_s44_eval, d112_rsft_s44_train |\\n| D115 | 2026-05-19 | D115: 8B RSFT s44 ign_f1=0.5451 确认 RSFT 跨 seed 稳健， | plan019_8b_rsft_s44_eval, eval_rsft_ced_s42 |\\n| D114 | 2026-05-19 | D114: 1.7B RSFT s43/s44 应使用 Method A（s42 SFT base） | plan019_1_7b_rsft_s43, plan019_1_7b_rsft_s44, d112_rsft_s44_ced_score |\\n| D113 | 2026-05-18 | D113: GRPO bf16 ckpt-100 为最优 checkpoint，ckpt-200 无 | grpo_bf16_g4_ckpt100_eval, grpo_bf16_g4_ckpt200_eval |\\n| D112 | 2026-05-18 | D112: 4B RSFT ign_f1 claim 需重大 reframe——全部 RSFT 基于 | wave1_sft_4b_s43_eval_r2, wave1_sft_4b_s44_eval_r2, eval_rsft_ced_s42 |\\n| D111 | 2026-05-18 | D111: 4B SFT s42 必须用 D076 协议重新 eval，统一三 seed 参考基准 | wave1_sft_4b_s43_eval_r2, wave1_sft_4b_s44_eval_r2 |\\n| D110 | 2026-05-18 | D110: GRPO bf16 ckpt-100 ign_f1=0.4431 无 catastrop | wave1_grpo_bf16_g4, grpo_bf16_g4_ckpt100_eval |\\n| D109 | 2026-05-18 | D109: Random RSFT k=1 ign_f1=0.4114 确证 CED scoring | random_rsft_k1_baseline, eval_flat_nli_seed45 |\\n| D108 | 2026-05-18 | D108: 14B 训练方案修正——TP 不可行，改用 2-GPU DeepSpeed ZeRO-3 | plan_017 |\\n| D107 | 2026-05-18 | D107: 4B evidence tax 统一到 D076 协议——39.74% / 47.21% | sft_baseline_noquant, plan_014_sft_no_evidence |\\n\\n\", \"total_chars\": 5040, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bc5f4965-b9c9-4c46-9109-14848d79f92e",
  "uuid": "06a32063-b3bd-46a1-a0fc-1cc09abe5b17",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/ROADMAP.md\\\", \\\"content\\\": \\\"# faith-evidence-ie — Research Dashboard\\\\n\\\\n> 最后更新: 2026-05-19 05:43 UTC | 更新原因: D115 8B RSFT 完成 + D114 1.7B Method A 裁决 + D112 进展 + 14B SFT 启动 + Wave 1 全部完成\\\\n\\\\n## 核心方向\\\\nFREIGE: LLM-based evidence-grounded DocRE 系统性研究。3 贡献：RSFT+NLI 有效性 / Decoupling spectrum / Scale-dependent evidence tax。详见 paper_framing.md。\\\\n\\\\n## 当前进展\\\\n- **阶段**: 🚀 Research + 审稿并行（Round 1 = 3.0 Findings，目标 4.0 Main）\\\\n- **Wave 1**: ✅ 全部完成（SFT s43/s44, GRPO bf16 G=4, Random RSFT）\\\\n- **Scaling seeds (plan_019)**: 8B 2-seed RSFT 完成（D115: s44=0.5451, variance 0.53pp）；1.7B s43/s44 重跑中（D114 Method A）\\\\n- **D112 full pipeline**: Step 3 RSFT 训练中 cuda:0（验证 RSFT 在强 SFT base s44 上的泛化性）\\\\n- **14B SFT (plan_017)**: cuda:1+2 运行中（2-GPU ZeRO-3, D108）\\\\n- **关键数值汇总**:\\\\n\\\\n| Scale | SFT mean (seeds) | RSFT mean (seeds) | Δ ign_f1 | SFT std | RSFT std |\\\\n|-------|-------------------|--------------------|----------|---------|----------|\\\\n| 1.7B | 0.4464 (3) | 0.5122 (1, s42 base) | +6.58pp | 2.79pp | — |\\\\n| 4B | 0.4358 (3) | 0.4482 (3, Method A) | +1.24pp | 3.80pp | 0.51pp |\\\\n| 8B | 0.4866 (2) | 0.5414 (2, Method A) | +5.48pp | 2.62pp | 0.53pp |\\\\n\\\\n- **RSFT 稳定化效应**: 4B variance 3.80→0.51pp (7.5x)，8B variance 2.62→0.53pp (5x)\\\\n- **CED 价值**: CED RSFT (0.4482) > Random RSFT (0.4114) > SFT (0.3974)，+3.68pp gap\\\\n- **GRPO**: bf16 ckpt-100 ign_f1=0.4431 无 catastrophic forgetting（D110），QLoRA 是 confound\\\\n\\\\n## 投稿目标\\\\n- **EMNLP 2026 Main** (ARR July cycle, ~July 15-25, **~57 天**)\\\\n\\\\n## 实验路线（3 层优先级）\\\\n\\\\n### Tier 1 — Main 必要条件\\\\n| 实验 | Plan ID | 状态 |\\\\n|------|---------|------|\\\\n| D102 k=1 方法论修正 | D102 | ✅ 完成 |\\\\n| SFT 4B s43 + s44 + s42 reeval | plan_w3_sft_seeds | ✅ 完成 (D111) |\\\\n| GRPO bf16 G=4 clean control | plan_015 | ✅ 完成 (D110/D113) |\\\\n| Random k=1 RSFT baseline | plan_w18_random | ✅ 完成 (D109) |\\\\n| 8B RSFT s44 seed expansion | plan_019 (8B) | ✅ 完成 (D115) |\\\\n| D112 RSFT from SFT s44 | plan_d112 | 🟡 Step 3 训练中 cuda:0 |\\\\n| 1.7B RSFT s43/s44 重跑 | plan_019 (1.7B) | 🟡 s43_r2 提交中 cuda:3 |\\\\n| 14B SFT (第 4 尺度) | plan_017 | 🟡 训练中 cuda:1+2 |\\\\n\\\\n### Tier 2 — 大幅加分\\\\n| 实验 | Plan ID | 状态 |\\\\n|------|---------|------|\\\\n| 14B RSFT + no-evidence + eval | plan_017 (后续) | pending（等 SFT 完成） |\\\\n| NLI model ablation | plan_010 | pending |\\\\n| Evidence tax 机制分析 | plan_020 | pending |\\\\n| Deep error analysis | plan_021 | pending |\\\\n\\\\n### Tier 3 — 锦上添花\\\\n| 实验 | Plan ID | 状态 |\\\\n|------|---------|------|\\\\n| CDR/GDA 跨领域 | plan_018 | P2（无 evidence 标注） |\\\\n| 第三模型家族 | plan_022 | pending |\\\\n| DocKS-RAG/LMRC 复现 | plan_023 | pending |\\\\n\\\\n## 从 3.0 → 4.0 路径\\\\n| 里程碑 | 预期评分 | 状态 |\\\\n|--------|---------|------|\\\\n| Wave 1 完成 + D112 | 3.0 → 3.5 | 🟡 D112 step 3 训练中 |\\\\n| + 1.7B/8B multi-seed 统计力 | 3.5 | 🟡 8B done, 1.7B 重跑中 |\\\\n| + 14B 第 4 尺度档 | 3.5 → 3.75 | 🟡 SFT 训练中 |\\\\n| + Mechanistic + error analysis | 3.75 → 4.0 | pending |\\\\n\\\\n## GPU 预算\\\\n- 本项目：rtx5090-4x cuda:0-3（4 张 RTX 5090）\\\\n- 当前：4/4 在用（D112 step3 / 14B SFT×2 / 1.7B RSFT）\\\\n- 剩余估算：Tier 1 ~15h + Tier 2 ~65h + Tier 3 ~100h\\\\n\\\\n## 近期任务\\\\n- [x] Wave 1 全部完成（SFT seeds, GRPO bf16, Random RSFT）\\\\n- [x] 8B RSFT s44 eval (D115: 0.5451, variance 压缩 5x)\\\\n- [x] 4B SFT s42 D076 reeval (D111: 0.3974)\\\\n- [ ] D112 step 3 → step 4 eval（cuda:0, ~1.5h total）\\\\n- [ ] 1.7B RSFT s43_r2 + s44_r2 + eval（cuda:3, ~2-3h total）\\\\n- [ ] 14B SFT 完成 → 14B RSFT + no-evidence + eval（cuda:1+2, ~8h SFT + 后续）\\\\n- [ ] experiment_plan.yaml 全面同步 registry\\\\n- [ ] paper_framing.md 更新（D112 结果 + 8B 2-seed + variance 压缩 narrative）\\\\n- [ ] 重新提交论文审稿\\\\n\\\\n## 关键风险\\\\n- **D112 结果待定**: 如 RSFT-from-s44 > SFT s44 (0.4734) → Claim 1 robust；否则需 reframe\\\\n- **8B RSFT evidence quality trade-off**: EDCR 从 0.65-0.67 降到 0.62（RE↑/evidence precision↓），论文需讨论\\\\n- **1.7B surpasses claim**: 现在更强（1.7B RSFT 0.5122 > 8B SFT mean 0.4866 +2.56pp），但仍需 1.7B multi-seed 确认\\\\n- **14B 显存**: 2-GPU ZeRO-3 已启动且正常（D108 验证），后续 RSFT 可能需要调参\\\\n- **EDCR 缺人工验证**: plan_013 取消，用 per-relation 分析 + Limitations 缓解\\\\n\\\\n## 关键决策日志\\\\n\\\\n| ID | 日期 | 摘要 | 关联实验 |\\\\n|----|------|------|----------|\\\\n| D116 | 2026-05-19 | D116: D112 结果无效（QLoRA confound），必须用 bf16 LoRA 重跑 s | d112_rsft_s44_eval, d112_rsft_s44_train |\\\\n| D115 | 2026-05-19 | D115: 8B RSFT s44 ign_f1=0.5451 确认 RSFT 跨 seed 稳健， | plan019_8b_rsft_s44_eval, eval_rsft_ced_s42 |\\\\n| D114 | 2026-05-19 | D114: 1.7B RSFT s43/s44 应使用 Method A（s42 SFT base） | plan019_1_7b_rsft_s43, plan019_1_7b_rsft_s44, d112_rsft_s44_ced_score |\\\\n| D113 | 2026-05-18 | D113: GRPO bf16 ckpt-100 为最优 checkpoint，ckpt-200 无 | grpo_bf16_g4_ckpt100_eval, grpo_bf16_g4_ckpt200_eval |\\\\n| D112 | 2026-05-18 | D112: 4B RSFT ign_f1 claim 需重大 reframe——全部 RSFT 基于 | wave1_sft_4b_s43_eval_r2, wave1_sft_4b_s44_eval_r2, eval_rsft_ced_s42 |\\\\n| D111 | 2026-05-18 | D111: 4B SFT s42 必须用 D076 协议重新 eval，统一三 seed 参考基准 | wave1_sft_4b_s43_eval_r2, wave1_sft_4b_s44_eval_r2 |\\\\n| D110 | 2026-05-18 | D110: GRPO bf16 ckpt-100 ign_f1=0.4431 无 catastrop | wave1_grpo_bf16_g4, grpo_bf16_g4_ckpt100_eval |\\\\n| D109 | 2026-05-18 | D109: Random RSFT k=1 ign_f1=0.4114 确证 CED scoring | random_rsft_k1_baseline, eval_flat_nli_seed45 |\\\\n| D108 | 2026-05-18 | D108: 14B 训练方案修正——TP 不可行，改用 2-GPU DeepSpeed ZeRO-3 | plan_017 |\\\\n| D107 | 2026-05-18 | D107: 4B evidence tax 统一到 D076 协议——39.74% / 47.21% | sft_baseline_noquant, plan_014_sft_no_evidence |\\\\n\\\\n\\\", \\\"total_chars\\\": 5040, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/ROADMAP.md\", \"content\": \"# faith-evidence-ie — Research Dashboard\\n\\n> 最后更新: 2026-05-19 05:43 UTC | 更新原因: D115 8B RSFT 完成 + D114 1.7B Method A 裁决 + D112 进展 + 14B SFT 启动 + Wave 1 全部完成\\n\\n## 核心方向\\nFREIGE: LLM-based evidence-grounded DocRE 系统性研究。3 贡献：RSFT+NLI 有效性 / Decoupling spectrum / Scale-dependent evidence tax。详见 paper_framing.md。\\n\\n## 当前进展\\n- **阶段**: 🚀 Research + 审稿并行（Round 1 = 3.0 Findings，目标 4.0 Main）\\n- **Wave 1**: ✅ 全部完成（SFT s43/s44, GRPO bf16 G=4, Random RSFT）\\n- **Scaling seeds (plan_019)**: 8B 2-seed RSFT 完成（D115: s44=0.5451, variance 0.53pp）；1.7B s43/s44 重跑中（D114 Method A）\\n- **D112 full pipeline**: Step 3 RSFT 训练中 cuda:0（验证 RSFT 在强 SFT base s44 上的泛化性）\\n- **14B SFT (plan_017)**: cuda:1+2 运行中（2-GPU ZeRO-3, D108）\\n- **关键数值汇总**:\\n\\n| Scale | SFT mean (seeds) | RSFT mean (seeds) | Δ ign_f1 | SFT std | RSFT std |\\n|-------|-------------------|--------------------|----------|---------|----------|\\n| 1.7B | 0.4464 (3) | 0.5122 (1, s42 base) | +6.58pp | 2.79pp | — |\\n| 4B | 0.4358 (3) | 0.4482 (3, Method A) | +1.24pp | 3.80pp | 0.51pp |\\n| 8B | 0.4866 (2) | 0.5414 (2, Method A) | +5.48pp | 2.62pp | 0.53pp |\\n\\n- **RSFT 稳定化效应**: 4B variance 3.80→0.51pp (7.5x)，8B variance 2.62→0.53pp (5x)\\n- **CED 价值**: CED RSFT (0.4482) > Random RSFT (0.4114) > SFT (0.3974)，+3.68pp gap\\n- **GRPO**: bf16 ckpt-100 ign_f1=0.4431 无 catastrophic forgetting（D110），QLoRA 是 confound\\n\\n## 投稿目标\\n- **EMNLP 2026 Main** (ARR July cycle, ~July 15-25, **~57 天**)\\n\\n## 实验路线（3 层优先级）\\n\\n### Tier 1 — Main 必要条件\\n| 实验 | Plan ID | 状态 |\\n|------|---------|------|\\n| D102 k=1 方法论修正 | D102 | ✅ 完成 |\\n| SFT 4B s43 + s44 + s42 reeval | plan_w3_sft_seeds | ✅ 完成 (D111) |\\n| GRPO bf16 G=4 clean control | plan_015 | ✅ 完成 (D110/D113) |\\n| Random k=1 RSFT baseline | plan_w18_random | ✅ 完成 (D109) |\\n| 8B RSFT s44 seed expansion | plan_019 (8B) | ✅ 完成 (D115) |\\n| D112 RSFT from SFT s44 | plan_d112 | 🟡 Step 3 训练中 cuda:0 |\\n| 1.7B RSFT s43/s44 重跑 | plan_019 (1.7B) | 🟡 s43_r2 提交中 cuda:3 |\\n| 14B SFT (第 4 尺度) | plan_017 | 🟡 训练中 cuda:1+2 |\\n\\n### Tier 2 — 大幅加分\\n| 实验 | Plan ID | 状态 |\\n|------|---------|------|\\n| 14B RSFT + no-evidence + eval | plan_017 (后续) | pending（等 SFT 完成） |\\n| NLI model ablation | plan_010 | pending |\\n| Evidence tax 机制分析 | plan_020 | pending |\\n| Deep error analysis | plan_021 | pending |\\n\\n### Tier 3 — 锦上添花\\n| 实验 | Plan ID | 状态 |\\n|------|---------|------|\\n| CDR/GDA 跨领域 | plan_018 | P2（无 evidence 标注） |\\n| 第三模型家族 | plan_022 | pending |\\n| DocKS-RAG/LMRC 复现 | plan_023 | pending |\\n\\n## 从 3.0 → 4.0 路径\\n| 里程碑 | 预期评分 | 状态 |\\n|--------|---------|------|\\n| Wave 1 完成 + D112 | 3.0 → 3.5 | 🟡 D112 step 3 训练中 |\\n| + 1.7B/8B multi-seed 统计力 | 3.5 | 🟡 8B done, 1.7B 重跑中 |\\n| + 14B 第 4 尺度档 | 3.5 → 3.75 | 🟡 SFT 训练中 |\\n| + Mechanistic + error analysis | 3.75 → 4.0 | pending |\\n\\n## GPU 预算\\n- 本项目：rtx5090-4x cuda:0-3（4 张 RTX 5090）\\n- 当前：4/4 在用（D112 step3 / 14B SFT×2 / 1.7B RSFT）\\n- 剩余估算：Tier 1 ~15h + Tier 2 ~65h + Tier 3 ~100h\\n\\n## 近期任务\\n- [x] Wave 1 全部完成（SFT seeds, GRPO bf16, Random RSFT）\\n- [x] 8B RSFT s44 eval (D115: 0.5451, variance 压缩 5x)\\n- [x] 4B SFT s42 D076 reeval (D111: 0.3974)\\n- [ ] D112 step 3 → step 4 eval（cuda:0, ~1.5h total）\\n- [ ] 1.7B RSFT s43_r2 + s44_r2 + eval（cuda:3, ~2-3h total）\\n- [ ] 14B SFT 完成 → 14B RSFT + no-evidence + eval（cuda:1+2, ~8h SFT + 后续）\\n- [ ] experiment_plan.yaml 全面同步 registry\\n- [ ] paper_framing.md 更新（D112 结果 + 8B 2-seed + variance 压缩 narrative）\\n- [ ] 重新提交论文审稿\\n\\n## 关键风险\\n- **D112 结果待定**: 如 RSFT-from-s44 > SFT s44 (0.4734) → Claim 1 robust；否则需 reframe\\n- **8B RSFT evidence quality trade-off**: EDCR 从 0.65-0.67 降到 0.62（RE↑/evidence precision↓），论文需讨论\\n- **1.7B surpasses claim**: 现在更强（1.7B RSFT 0.5122 > 8B SFT mean 0.4866 +2.56pp），但仍需 1.7B multi-seed 确认\\n- **14B 显存**: 2-GPU ZeRO-3 已启动且正常（D108 验证），后续 RSFT 可能需要调参\\n- **EDCR 缺人工验证**: plan_013 取消，用 per-relation 分析 + Limitations 缓解\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D116 | 2026-05-19 | D116: D112 结果无效（QLoRA confound），必须用 bf16 LoRA 重跑 s | d112_rsft_s44_eval, d112_rsft_s44_train |\\n| D115 | 2026-05-19 | D115: 8B RSFT s44 ign_f1=0.5451 确认 RSFT 跨 seed 稳健， | plan019_8b_rsft_s44_eval, eval_rsft_ced_s42 |\\n| D114 | 2026-05-19 | D114: 1.7B RSFT s43/s44 应使用 Method A（s42 SFT base） | plan019_1_7b_rsft_s43, plan019_1_7b_rsft_s44, d112_rsft_s44_ced_score |\\n| D113 | 2026-05-18 | D113: GRPO bf16 ckpt-100 为最优 checkpoint，ckpt-200 无 | grpo_bf16_g4_ckpt100_eval, grpo_bf16_g4_ckpt200_eval |\\n| D112 | 2026-05-18 | D112: 4B RSFT ign_f1 claim 需重大 reframe——全部 RSFT 基于 | wave1_sft_4b_s43_eval_r2, wave1_sft_4b_s44_eval_r2, eval_rsft_ced_s42 |\\n| D111 | 2026-05-18 | D111: 4B SFT s42 必须用 D076 协议重新 eval，统一三 seed 参考基准 | wave1_sft_4b_s43_eval_r2, wave1_sft_4b_s44_eval_r2 |\\n| D110 | 2026-05-18 | D110: GRPO bf16 ckpt-100 ign_f1=0.4431 无 catastrop | wave1_grpo_bf16_g4, grpo_bf16_g4_ckpt100_eval |\\n| D109 | 2026-05-18 | D109: Random RSFT k=1 ign_f1=0.4114 确证 CED scoring | random_rsft_k1_baseline, eval_flat_nli_seed45 |\\n| D108 | 2026-05-18 | D108: 14B 训练方案修正——TP 不可行，改用 2-GPU DeepSpeed ZeRO-3 | plan_017 |\\n| D107 | 2026-05-18 | D107: 4B evidence tax 统一到 D076 协议——39.74% / 47.21% | sft_baseline_noquant, plan_014_sft_no_evidence |\\n\\n\", \"total_chars\": 5040, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-19T12:39:56.254Z_

<details><summary>↩ Tool result · `toolu_01NFnZW1bVaX96tWJCvG2j6g`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/memory.md\", \"content\": \"# Project Memory\\n\\n## RSFT 方差压缩效应 (2026-05-19)\\n\\n**发现**: RSFT 在所有尺度显著压缩跨 seed 方差，且压缩倍数随模型容量递减：\\n\\n| Scale | SFT std | RSFT std | 压缩倍数 | SFT n | RSFT n |\\n|-------|---------|----------|---------|-------|--------|\\n| 1.7B | 2.79pp | 0.09pp | **31x** | 3 | 3 |\\n| 4B | 3.80pp | 0.51pp | **7.5x** | 3 | 3 |\\n| 8B | 2.62pp | 0.53pp | **5x** | 2 | 2 |\\n\\n**解释**: RSFT 的 CED 筛选过程相当于对训练数据施加 quality filter，减少了因随机种子导致的训练轨迹分歧。小模型更容易受数据噪声影响，所以压缩效应最强(31x)。大模型本身已较稳定(SFT std 较低)，RSFT 仍能进一步压缩(5x)。\\n\\n**论文意义**: 这是 RSFT 独立于 ign_f1 提升的第二个贡献维度——训练稳定性。可作为 Claim 1 的补充叙事：\\\"RSFT not only improves performance but dramatically stabilizes training outcomes across random seeds.\\\"\\n\\n**注意**: 1.7B RSFT 所有 3 seeds 使用 Method A（s42 SFT base + s42 CED data，仅变 RSFT seed），压缩效应测量的是 RSFT 训练过程本身的稳定性，不含 SFT base 变异。8B RSFT 使用相同方法（s42 SFT base），但仅 2 seeds。\\n\\n## plan_021: Deep Error Analysis — RSFT vs SFT (2026-05-19)\\n\\n**Files**: `scripts/analysis/deep_error_analysis.py` → `scripts/analysis/results/`\\n\\n**Models compared** (all dev set, seed 42 eval):\\n- 4B SFT: `d111_4b_sft_s42_reeval` (ign_f1=0.397)\\n- 4B RSFT: `rsft_s43_dev_eval_preds` (train seed 43, ign_f1=0.451) — NOTE: s42 predictions unavailable, used s43 model\\n- 8B SFT: `qwen3_8b_sft_eval` (ign_f1=0.505)\\n- 8B RSFT: `d102_8b_k1_s42` (ign_f1=0.538)\\n\\n### Key Findings\\n\\n**Per-Relation F1 (171 unique relations in predictions)**:\\n- 4B largest gains: original network (+0.32, gold=38), award received (+0.16, gold=66), cast member (+0.14, gold=225), performer (+0.13, gold=320)\\n- 4B largest losses: chairperson (-0.16, gold=21), screenwriter (-0.09, gold=35), genre (-0.09, gold=14)\\n- Pattern: RSFT helps most on mid-frequency entertainment/media relations where SFT under-performs. Losses concentrated on low-frequency relations (gold < 40).\\n- 8B gains are more spread out: genre (+0.34), present in work (+0.21), mother (+0.19), league (+0.17)\\n- 8B losses: sibling (-0.16), dissolved/abolished (-0.15), parent organization (-0.14), parent taxon (-0.19)\\n\\n**Per-Document-Length (ign_f1, quantiles: short ≤160, mid 161-208, long >208 words)**:\\n| Bucket | 4B SFT | 4B RSFT | 4B gain | 8B SFT | 8B RSFT | 8B gain |\\n|--------|--------|---------|---------|--------|---------|---------|\\n| short  | 0.416  | 0.472   | +0.056  | 0.551  | 0.580   | +0.029  |\\n| mid    | 0.427  | 0.486   | +0.058  | 0.520  | 0.543   | +0.023  |\\n| long   | 0.349  | 0.398   | +0.048  | 0.445  | 0.490   | +0.046  |\\n\\n- 4B: gain relatively uniform (~5pt), slightly less on long docs\\n- 8B: gain is **largest on long docs** (+4.6pt vs +2.3-2.9pt on short/mid) — RSFT helps 8B more on harder/longer documents\\n\\n**Per-Entity-Count (ign_f1, quantiles: low ≤17, mid 18-22, high >22 entities)**:\\n| Bucket | 4B SFT | 4B RSFT | 4B gain | 8B SFT | 8B RSFT | 8B gain |\\n|--------|--------|---------|---------|--------|---------|---------|\\n| low    | 0.432  | 0.475   | +0.044  | 0.534  | 0.574   | +0.040  |\\n| mid    | 0.398  | 0.462   | +0.064  | 0.523  | 0.543   | +0.020  |\\n| high   | 0.369  | 0.423   | +0.054  | 0.466  | 0.503   | +0.037  |\\n\\n- 4B: mid-entity docs gain most (+6.4pt); low-entity least (+4.4pt)\\n- 8B: low-entity and high-entity gain similarly (~4pt); mid-entity gains least (+2.0pt)\\n\\n### Interpretation\\n1. RSFT consistently improves across all stratifications — no systematic \\\"only helps easy cases\\\"\\n2. For 4B, gain is fairly uniform across complexity dimensions, with slightly larger gains on mid-complexity\\n3. For 8B, RSFT gain is notably larger on long docs (+4.6pt vs +2.3pt short/mid), suggesting RSFT helps more with complex multi-sentence reasoning at larger scale\\n4. Per-relation analysis shows RSFT gains are relation-type-dependent, not just a uniform improvement — useful for paper narrative about what RSFT learns\\n\\n## plan_020: Evidence Tax Mechanism Analysis (2026-05-19)\\n\\n**Files**: `scripts/analysis/evidence_tax_analysis.py`, `scripts/analysis/evidence_tax_plots.py` → `scripts/analysis/results/`\\n\\n**Pairs analyzed** (all dev set, SFT models):\\n- Qwen3-1.7B: `qwen3_1_7b_sft_eval` (F1=0.494) vs `qwen3_1_7b_no_evidence_eval_v3` (F1=0.410)\\n- Qwen3-4B: `d111_4b_sft_s42_reeval` (F1=0.405) vs `plan_014_no_evidence_eval_d076` (F1=0.488)\\n- Qwen3-8B: `qwen3_8b_sft_eval` (F1=0.526) vs `qwen3_8b_no_evidence_eval_v2` (F1=0.528)\\n- Llama-3.1-8B: `llama_3_1_8b_sft_eval` (F1=0.551) vs `llama_3_1_8b_no_evidence_eval` (F1=0.562)\\n\\n### Key Findings\\n\\n**1. Evidence tax is non-monotonic across scale:**\\n| Scale | With-Ev F1 | No-Ev F1 | Tax (pp) | Direction |\\n|-------|-----------|----------|----------|-----------|\\n| 1.7B  | 0.494     | 0.410    | +8.4     | with-ev better |\\n| 4B    | 0.405     | 0.488    | -8.3     | no-ev better |\\n| 8B Q  | 0.526     | 0.528    | -0.2     | ~tied |\\n| 8B L  | 0.551     | 0.562    | -1.1     | no-ev slightly better |\\n\\n**2. Truncation is NOT the primary mechanism:**\\n- 1.7B: no-evidence has HIGHER truncation (50.9% vs 31.9%) — opposite of naive hypothesis\\n- 4B: similar truncation rates (29.2% vs 31.2%)\\n- 8B: with-evidence slightly more truncated (31.8% vs 22.8%)\\n\\n**3. Evidence as regularizer at small scale (1.7B paradox):**\\n- 1.7B no-evidence generates 26K total predictions vs 17K with-evidence\\n- 1.7B no-evidence has 60.5% duplicate triples vs 33.0% with-evidence\\n- Without evidence constraints, the 1.7B model over-generates and repeats triples, wasting token budget\\n- Per-doc F1 wins: with-ev=571, no-ev=283 — with-evidence wins on 58% of documents\\n\\n**4. Evidence character overhead:**\\n- Evidence fields consume ~20% of output chars across all Qwen3 scales\\n- Per-triple cost: with-ev ~102 chars/triple vs no-ev ~85 chars/triple (1.2x ratio)\\n- Llama-3.1-8B is the exception: 23% overhead but per-triple ratio is 1.00x (Llama uses longer relation names)\\n\\n**5. False positive patterns:**\\n- No-evidence models consistently have higher FP rates at all scales except 4B (4B with-ev has anomalously high FP rate at 58.7%)\\n- 1.7B no-ev FP rate: 55.3% vs with-ev 49.1%\\n\\n**6. Duplicate triples are a major token waste:**\\n- All no-evidence models have higher duplication rates than with-evidence counterparts\\n- 1.7B no-ev: 60.5% duplicates (15814/26157 triples are redundant copies)\\n- Evidence field provides a de-duplication signal: same (h,r,t) with different evidence gets generated, but at least carries distinct information\\n\\n### Interpretation for Paper\\n1. Evidence requirement does NOT simply \\\"tax\\\" by consuming output space — the mechanism is more nuanced\\n2. At small scale (1.7B), evidence acts as structural regularization, preventing degenerate repetitive generation\\n3. At medium scale (4B), the 4B with-evidence model appears to be a weaker adapter (possibly training artifact, not inherent evidence mechanism). Need to verify with matched training conditions.\\n4. At large scale (8B+), evidence tax is negligible (~0-1pp), suggesting larger models handle the additional output complexity without degradation\\n5. The dominant mechanism behind 1.7B's \\\"negative tax\\\" is duplicate suppression and generation discipline, not output length\\n\\n## D116: QLoRA Confound 教训 (2026-05-19)\\n\\n**决策**: D112 RSFT 训练误用了 --quantize（QLoRA），导致 adapter 适应 4-bit 量化误差。bf16 eval 下 ign_f1=0.2181（灾难性崩溃）。\\n\\n**教训**: 所有 RSFT 训练必须使用 bf16 LoRA（与 canonical 实验一致）。训练脚本中不得出现 --quantize 参数。QLoRA adapter 与 bf16 backbone 不兼容——adapter 学到的是如何补偿量化误差，去掉量化后补偿变成噪声。\\n\\n**行动**: bf16 重跑 (d112_rsft_s44_train_bf16) 已提交 cuda:0。\\n\", \"total_chars\": 7311, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bc5f4965-b9c9-4c46-9109-14848d79f92e",
  "uuid": "cd32e1ae-0747-41fa-8991-3c26d720ef8c",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/memory.md\\\", \\\"content\\\": \\\"# Project Memory\\\\n\\\\n## RSFT 方差压缩效应 (2026-05-19)\\\\n\\\\n**发现**: RSFT 在所有尺度显著压缩跨 seed 方差，且压缩倍数随模型容量递减：\\\\n\\\\n| Scale | SFT std | RSFT std | 压缩倍数 | SFT n | RSFT n |\\\\n|-------|---------|----------|---------|-------|--------|\\\\n| 1.7B | 2.79pp | 0.09pp | **31x** | 3 | 3 |\\\\n| 4B | 3.80pp | 0.51pp | **7.5x** | 3 | 3 |\\\\n| 8B | 2.62pp | 0.53pp | **5x** | 2 | 2 |\\\\n\\\\n**解释**: RSFT 的 CED 筛选过程相当于对训练数据施加 quality filter，减少了因随机种子导致的训练轨迹分歧。小模型更容易受数据噪声影响，所以压缩效应最强(31x)。大模型本身已较稳定(SFT std 较低)，RSFT 仍能进一步压缩(5x)。\\\\n\\\\n**论文意义**: 这是 RSFT 独立于 ign_f1 提升的第二个贡献维度——训练稳定性。可作为 Claim 1 的补充叙事：\\\\\\\"RSFT not only improves performance but dramatically stabilizes training outcomes across random seeds.\\\\\\\"\\\\n\\\\n**注意**: 1.7B RSFT 所有 3 seeds 使用 Method A（s42 SFT base + s42 CED data，仅变 RSFT seed），压缩效应测量的是 RSFT 训练过程本身的稳定性，不含 SFT base 变异。8B RSFT 使用相同方法（s42 SFT base），但仅 2 seeds。\\\\n\\\\n## plan_021: Deep Error Analysis — RSFT vs SFT (2026-05-19)\\\\n\\\\n**Files**: `scripts/analysis/deep_error_analysis.py` → `scripts/analysis/results/`\\\\n\\\\n**Models compared** (all dev set, seed 42 eval):\\\\n- 4B SFT: `d111_4b_sft_s42_reeval` (ign_f1=0.397)\\\\n- 4B RSFT: `rsft_s43_dev_eval_preds` (train seed 43, ign_f1=0.451) — NOTE: s42 predictions unavailable, used s43 model\\\\n- 8B SFT: `qwen3_8b_sft_eval` (ign_f1=0.505)\\\\n- 8B RSFT: `d102_8b_k1_s42` (ign_f1=0.538)\\\\n\\\\n### Key Findings\\\\n\\\\n**Per-Relation F1 (171 unique relations in predictions)**:\\\\n- 4B largest gains: original network (+0.32, gold=38), award received (+0.16, gold=66), cast member (+0.14, gold=225), performer (+0.13, gold=320)\\\\n- 4B largest losses: chairperson (-0.16, gold=21), screenwriter (-0.09, gold=35), genre (-0.09, gold=14)\\\\n- Pattern: RSFT helps most on mid-frequency entertainment/media relations where SFT under-performs. Losses concentrated on low-frequency relations (gold < 40).\\\\n- 8B gains are more spread out: genre (+0.34), present in work (+0.21), mother (+0.19), league (+0.17)\\\\n- 8B losses: sibling (-0.16), dissolved/abolished (-0.15), parent organization (-0.14), parent taxon (-0.19)\\\\n\\\\n**Per-Document-Length (ign_f1, quantiles: short ≤160, mid 161-208, long >208 words)**:\\\\n| Bucket | 4B SFT | 4B RSFT | 4B gain | 8B SFT | 8B RSFT | 8B gain |\\\\n|--------|--------|---------|---------|--------|---------|---------|\\\\n| short  | 0.416  | 0.472   | +0.056  | 0.551  | 0.580   | +0.029  |\\\\n| mid    | 0.427  | 0.486   | +0.058  | 0.520  | 0.543   | +0.023  |\\\\n| long   | 0.349  | 0.398   | +0.048  | 0.445  | 0.490   | +0.046  |\\\\n\\\\n- 4B: gain relatively uniform (~5pt), slightly less on long docs\\\\n- 8B: gain is **largest on long docs** (+4.6pt vs +2.3-2.9pt on short/mid) — RSFT helps 8B more on harder/longer documents\\\\n\\\\n**Per-Entity-Count (ign_f1, quantiles: low ≤17, mid 18-22, high >22 entities)**:\\\\n| Bucket | 4B SFT | 4B RSFT | 4B gain | 8B SFT | 8B RSFT | 8B gain |\\\\n|--------|--------|---------|---------|--------|---------|---------|\\\\n| low    | 0.432  | 0.475   | +0.044  | 0.534  | 0.574   | +0.040  |\\\\n| mid    | 0.398  | 0.462   | +0.064  | 0.523  | 0.543   | +0.020  |\\\\n| high   | 0.369  | 0.423   | +0.054  | 0.466  | 0.503   | +0.037  |\\\\n\\\\n- 4B: mid-entity docs gain most (+6.4pt); low-entity least (+4.4pt)\\\\n- 8B: low-entity and high-entity gain similarly (~4pt); mid-entity gains least (+2.0pt)\\\\n\\\\n### Interpretation\\\\n1. RSFT consistently improves across all stratifications — no systematic \\\\\\\"only helps easy cases\\\\\\\"\\\\n2. For 4B, gain is fairly uniform across complexity dimensions, with slightly larger gains on mid-complexity\\\\n3. For 8B, RSFT gain is notably larger on long docs (+4.6pt vs +2.3pt short/mid), suggesting RSFT helps more with complex multi-sentence reasoning at larger scale\\\\n4. Per-relation analysis shows RSFT gains are relation-type-dependent, not just a uniform improvement — useful for paper narrative about what RSFT learns\\\\n\\\\n## plan_020: Evidence Tax Mechanism Analysis (2026-05-19)\\\\n\\\\n**Files**: `scripts/analysis/evidence_tax_analysis.py`, `scripts/analysis/evidence_tax_plots.py` → `scripts/analysis/results/`\\\\n\\\\n**Pairs analyzed** (all dev set, SFT models):\\\\n- Qwen3-1.7B: `qwen3_1_7b_sft_eval` (F1=0.494) vs `qwen3_1_7b_no_evidence_eval_v3` (F1=0.410)\\\\n- Qwen3-4B: `d111_4b_sft_s42_reeval` (F1=0.405) vs `plan_014_no_evidence_eval_d076` (F1=0.488)\\\\n- Qwen3-8B: `qwen3_8b_sft_eval` (F1=0.526) vs `qwen3_8b_no_evidence_eval_v2` (F1=0.528)\\\\n- Llama-3.1-8B: `llama_3_1_8b_sft_eval` (F1=0.551) vs `llama_3_1_8b_no_evidence_eval` (F1=0.562)\\\\n\\\\n### Key Findings\\\\n\\\\n**1. Evidence tax is non-monotonic across scale:**\\\\n| Scale | With-Ev F1 | No-Ev F1 | Tax (pp) | Direction |\\\\n|-------|-----------|----------|----------|-----------|\\\\n| 1.7B  | 0.494     | 0.410    | +8.4     | with-ev better |\\\\n| 4B    | 0.405     | 0.488    | -8.3     | no-ev better |\\\\n| 8B Q  | 0.526     | 0.528    | -0.2     | ~tied |\\\\n| 8B L  | 0.551     | 0.562    | -1.1     | no-ev slightly better |\\\\n\\\\n**2. Truncation is NOT the primary mechanism:**\\\\n- 1.7B: no-evidence has HIGHER truncation (50.9% vs 31.9%) — opposite of naive hypothesis\\\\n- 4B: similar truncation rates (29.2% vs 31.2%)\\\\n- 8B: with-evidence slightly more truncated (31.8% vs 22.8%)\\\\n\\\\n**3. Evidence as regularizer at small scale (1.7B paradox):**\\\\n- 1.7B no-evidence generates 26K total predictions vs 17K with-evidence\\\\n- 1.7B no-evidence has 60.5% duplicate triples vs 33.0% with-evidence\\\\n- Without evidence constraints, the 1.7B model over-generates and repeats triples, wasting token budget\\\\n- Per-doc F1 wins: with-ev=571, no-ev=283 — with-evidence wins on 58% of documents\\\\n\\\\n**4. Evidence character overhead:**\\\\n- Evidence fields consume ~20% of output chars across all Qwen3 scales\\\\n- Per-triple cost: with-ev ~102 chars/triple vs no-ev ~85 chars/triple (1.2x ratio)\\\\n- Llama-3.1-8B is the exception: 23% overhead but per-triple ratio is 1.00x (Llama uses longer relation names)\\\\n\\\\n**5. False positive patterns:**\\\\n- No-evidence models consistently have higher FP rates at all scales except 4B (4B with-ev has anomalously high FP rate at 58.7%)\\\\n- 1.7B no-ev FP rate: 55.3% vs with-ev 49.1%\\\\n\\\\n**6. Duplicate triples are a major token waste:**\\\\n- All no-evidence models have higher duplication rates than with-evidence counterparts\\\\n- 1.7B no-ev: 60.5% duplicates (15814/26157 triples are redundant copies)\\\\n- Evidence field provides a de-duplication signal: same (h,r,t) with different evidence gets generated, but at least carries distinct information\\\\n\\\\n### Interpretation for Paper\\\\n1. Evidence requirement does NOT simply \\\\\\\"tax\\\\\\\" by consuming output space — the mechanism is more nuanced\\\\n2. At small scale (1.7B), evidence acts as structural regularization, preventing degenerate repetitive generation\\\\n3. At medium scale (4B), the 4B with-evidence model appears to be a weaker adapter (possibly training artifact, not inherent evidence mechanism). Need to verify with matched training conditions.\\\\n4. At large scale (8B+), evidence tax is negligible (~0-1pp), suggesting larger models handle the additional output complexity without degradation\\\\n5. The dominant mechanism behind 1.7B's \\\\\\\"negative tax\\\\\\\" is duplicate suppression and generation discipline, not output length\\\\n\\\\n## D116: QLoRA Confound 教训 (2026-05-19)\\\\n\\\\n**决策**: D112 RSFT 训练误用了 --quantize（QLoRA），导致 adapter 适应 4-bit 量化误差。bf16 eval 下 ign_f1=0.2181（灾难性崩溃）。\\\\n\\\\n**教训**: 所有 RSFT 训练必须使用 bf16 LoRA（与 canonical 实验一致）。训练脚本中不得出现 --quantize 参数。QLoRA adapter 与 bf16 backbone 不兼容——adapter 学到的是如何补偿量化误差，去掉量化后补偿变成噪声。\\\\n\\\\n**行动**: bf16 重跑 (d112_rsft_s44_train_bf16) 已提交 cuda:0。\\\\n\\\", \\\"total_chars\\\": 7311, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/memory.md\", \"content\": \"# Project Memory\\n\\n## RSFT 方差压缩效应 (2026-05-19)\\n\\n**发现**: RSFT 在所有尺度显著压缩跨 seed 方差，且压缩倍数随模型容量递减：\\n\\n| Scale | SFT std | RSFT std | 压缩倍数 | SFT n | RSFT n |\\n|-------|---------|----------|---------|-------|--------|\\n| 1.7B | 2.79pp | 0.09pp | **31x** | 3 | 3 |\\n| 4B | 3.80pp | 0.51pp | **7.5x** | 3 | 3 |\\n| 8B | 2.62pp | 0.53pp | **5x** | 2 | 2 |\\n\\n**解释**: RSFT 的 CED 筛选过程相当于对训练数据施加 quality filter，减少了因随机种子导致的训练轨迹分歧。小模型更容易受数据噪声影响，所以压缩效应最强(31x)。大模型本身已较稳定(SFT std 较低)，RSFT 仍能进一步压缩(5x)。\\n\\n**论文意义**: 这是 RSFT 独立于 ign_f1 提升的第二个贡献维度——训练稳定性。可作为 Claim 1 的补充叙事：\\\"RSFT not only improves performance but dramatically stabilizes training outcomes across random seeds.\\\"\\n\\n**注意**: 1.7B RSFT 所有 3 seeds 使用 Method A（s42 SFT base + s42 CED data，仅变 RSFT seed），压缩效应测量的是 RSFT 训练过程本身的稳定性，不含 SFT base 变异。8B RSFT 使用相同方法（s42 SFT base），但仅 2 seeds。\\n\\n## plan_021: Deep Error Analysis — RSFT vs SFT (2026-05-19)\\n\\n**Files**: `scripts/analysis/deep_error_analysis.py` → `scripts/analysis/results/`\\n\\n**Models compared** (all dev set, seed 42 eval):\\n- 4B SFT: `d111_4b_sft_s42_reeval` (ign_f1=0.397)\\n- 4B RSFT: `rsft_s43_dev_eval_preds` (train seed 43, ign_f1=0.451) — NOTE: s42 predictions unavailable, used s43 model\\n- 8B SFT: `qwen3_8b_sft_eval` (ign_f1=0.505)\\n- 8B RSFT: `d102_8b_k1_s42` (ign_f1=0.538)\\n\\n### Key Findings\\n\\n**Per-Relation F1 (171 unique relations in predictions)**:\\n- 4B largest gains: original network (+0.32, gold=38), award received (+0.16, gold=66), cast member (+0.14, gold=225), performer (+0.13, gold=320)\\n- 4B largest losses: chairperson (-0.16, gold=21), screenwriter (-0.09, gold=35), genre (-0.09, gold=14)\\n- Pattern: RSFT helps most on mid-frequency entertainment/media relations where SFT under-performs. Losses concentrated on low-frequency relations (gold < 40).\\n- 8B gains are more spread out: genre (+0.34), present in work (+0.21), mother (+0.19), league (+0.17)\\n- 8B losses: sibling (-0.16), dissolved/abolished (-0.15), parent organization (-0.14), parent taxon (-0.19)\\n\\n**Per-Document-Length (ign_f1, quantiles: short ≤160, mid 161-208, long >208 words)**:\\n| Bucket | 4B SFT | 4B RSFT | 4B gain | 8B SFT | 8B RSFT | 8B gain |\\n|--------|--------|---------|---------|--------|---------|---------|\\n| short  | 0.416  | 0.472   | +0.056  | 0.551  | 0.580   | +0.029  |\\n| mid    | 0.427  | 0.486   | +0.058  | 0.520  | 0.543   | +0.023  |\\n| long   | 0.349  | 0.398   | +0.048  | 0.445  | 0.490   | +0.046  |\\n\\n- 4B: gain relatively uniform (~5pt), slightly less on long docs\\n- 8B: gain is **largest on long docs** (+4.6pt vs +2.3-2.9pt on short/mid) — RSFT helps 8B more on harder/longer documents\\n\\n**Per-Entity-Count (ign_f1, quantiles: low ≤17, mid 18-22, high >22 entities)**:\\n| Bucket | 4B SFT | 4B RSFT | 4B gain | 8B SFT | 8B RSFT | 8B gain |\\n|--------|--------|---------|---------|--------|---------|---------|\\n| low    | 0.432  | 0.475   | +0.044  | 0.534  | 0.574   | +0.040  |\\n| mid    | 0.398  | 0.462   | +0.064  | 0.523  | 0.543   | +0.020  |\\n| high   | 0.369  | 0.423   | +0.054  | 0.466  | 0.503   | +0.037  |\\n\\n- 4B: mid-entity docs gain most (+6.4pt); low-entity least (+4.4pt)\\n- 8B: low-entity and high-entity gain similarly (~4pt); mid-entity gains least (+2.0pt)\\n\\n### Interpretation\\n1. RSFT consistently improves across all stratifications — no systematic \\\"only helps easy cases\\\"\\n2. For 4B, gain is fairly uniform across complexity dimensions, with slightly larger gains on mid-complexity\\n3. For 8B, RSFT gain is notably larger on long docs (+4.6pt vs +2.3pt short/mid), suggesting RSFT helps more with complex multi-sentence reasoning at larger scale\\n4. Per-relation analysis shows RSFT gains are relation-type-dependent, not just a uniform improvement — useful for paper narrative about what RSFT learns\\n\\n## plan_020: Evidence Tax Mechanism Analysis (2026-05-19)\\n\\n**Files**: `scripts/analysis/evidence_tax_analysis.py`, `scripts/analysis/evidence_tax_plots.py` → `scripts/analysis/results/`\\n\\n**Pairs analyzed** (all dev set, SFT models):\\n- Qwen3-1.7B: `qwen3_1_7b_sft_eval` (F1=0.494) vs `qwen3_1_7b_no_evidence_eval_v3` (F1=0.410)\\n- Qwen3-4B: `d111_4b_sft_s42_reeval` (F1=0.405) vs `plan_014_no_evidence_eval_d076` (F1=0.488)\\n- Qwen3-8B: `qwen3_8b_sft_eval` (F1=0.526) vs `qwen3_8b_no_evidence_eval_v2` (F1=0.528)\\n- Llama-3.1-8B: `llama_3_1_8b_sft_eval` (F1=0.551) vs `llama_3_1_8b_no_evidence_eval` (F1=0.562)\\n\\n### Key Findings\\n\\n**1. Evidence tax is non-monotonic across scale:**\\n| Scale | With-Ev F1 | No-Ev F1 | Tax (pp) | Direction |\\n|-------|-----------|----------|----------|-----------|\\n| 1.7B  | 0.494     | 0.410    | +8.4     | with-ev better |\\n| 4B    | 0.405     | 0.488    | -8.3     | no-ev better |\\n| 8B Q  | 0.526     | 0.528    | -0.2     | ~tied |\\n| 8B L  | 0.551     | 0.562    | -1.1     | no-ev slightly better |\\n\\n**2. Truncation is NOT the primary mechanism:**\\n- 1.7B: no-evidence has HIGHER truncation (50.9% vs 31.9%) — opposite of naive hypothesis\\n- 4B: similar truncation rates (29.2% vs 31.2%)\\n- 8B: with-evidence slightly more truncated (31.8% vs 22.8%)\\n\\n**3. Evidence as regularizer at small scale (1.7B paradox):**\\n- 1.7B no-evidence generates 26K total predictions vs 17K with-evidence\\n- 1.7B no-evidence has 60.5% duplicate triples vs 33.0% with-evidence\\n- Without evidence constraints, the 1.7B model over-generates and repeats triples, wasting token budget\\n- Per-doc F1 wins: with-ev=571, no-ev=283 — with-evidence wins on 58% of documents\\n\\n**4. Evidence character overhead:**\\n- Evidence fields consume ~20% of output chars across all Qwen3 scales\\n- Per-triple cost: with-ev ~102 chars/triple vs no-ev ~85 chars/triple (1.2x ratio)\\n- Llama-3.1-8B is the exception: 23% overhead but per-triple ratio is 1.00x (Llama uses longer relation names)\\n\\n**5. False positive patterns:**\\n- No-evidence models consistently have higher FP rates at all scales except 4B (4B with-ev has anomalously high FP rate at 58.7%)\\n- 1.7B no-ev FP rate: 55.3% vs with-ev 49.1%\\n\\n**6. Duplicate triples are a major token waste:**\\n- All no-evidence models have higher duplication rates than with-evidence counterparts\\n- 1.7B no-ev: 60.5% duplicates (15814/26157 triples are redundant copies)\\n- Evidence field provides a de-duplication signal: same (h,r,t) with different evidence gets generated, but at least carries distinct information\\n\\n### Interpretation for Paper\\n1. Evidence requirement does NOT simply \\\"tax\\\" by consuming output space — the mechanism is more nuanced\\n2. At small scale (1.7B), evidence acts as structural regularization, preventing degenerate repetitive generation\\n3. At medium scale (4B), the 4B with-evidence model appears to be a weaker adapter (possibly training artifact, not inherent evidence mechanism). Need to verify with matched training conditions.\\n4. At large scale (8B+), evidence tax is negligible (~0-1pp), suggesting larger models handle the additional output complexity without degradation\\n5. The dominant mechanism behind 1.7B's \\\"negative tax\\\" is duplicate suppression and generation discipline, not output length\\n\\n## D116: QLoRA Confound 教训 (2026-05-19)\\n\\n**决策**: D112 RSFT 训练误用了 --quantize（QLoRA），导致 adapter 适应 4-bit 量化误差。bf16 eval 下 ign_f1=0.2181（灾难性崩溃）。\\n\\n**教训**: 所有 RSFT 训练必须使用 bf16 LoRA（与 canonical 实验一致）。训练脚本中不得出现 --quantize 参数。QLoRA adapter 与 bf16 backbone 不兼容——adapter 学到的是如何补偿量化误差，去掉量化后补偿变成噪声。\\n\\n**行动**: bf16 重跑 (d112_rsft_s44_train_bf16) 已提交 cuda:0。\\n\", \"total_chars\": 7311, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 14_

<details><summary>Logged reasoning block</summary>

```text
The registry output is too large. Let me use a subagent to extract the specific eval results I need from the registry JSON file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bc5f4965-b9c9-4c46-9109-14848d79f92e",
  "uuid": "0d59945f-c748-4a40-b41d-86aa9e46cc77",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EoR1P1DYwpef1GKSvhXcN9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7467,
      "cache_read_input_tokens": 26971,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7467
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

_source line 15_

Registry 太大，用 subagent 提取所有 eval 相关条目。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bc5f4965-b9c9-4c46-9109-14848d79f92e",
  "uuid": "a19815bf-ae14-4b94-9bc0-3cfff901957f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EoR1P1DYwpef1GKSvhXcN9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7467,
      "cache_read_input_tokens": 26971,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7467
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

_source line 16_

<details open><summary>🔧 Tool call — Agent · `toolu_01SfhnwAfu5FGq4CJbNHa37Q`</summary>

```json
{
  "description": "Extract eval metrics from registry",
  "prompt": "I need you to extract all eval experiment results from a large registry JSON file. The file is at:\n/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/bc5f4965-b9c9-4c46-9109-14848d79f92e/tool-results/mcp-agent-ml-research-read_registry-1779194396202.txt\n\nThe file schema is `{result: string}` where the `result` field is a JSON string that needs to be parsed again.\n\nI need you to extract ALL experiments whose `experiment_id` contains \"eval\" (case-insensitive). For each, report:\n1. experiment_id\n2. status\n3. conclusion (if any)\n4. Any metrics (especially ign_f1)\n5. Any relevant notes about protocol (D076, etc.)\n\nAlso extract these specific non-eval experiments if they exist:\n- random_rsft_k1_eval or random_rsft_k1_baseline\n- Any experiment with \"grpo\" in the name\n- Any experiment with \"no_evidence\" in the name\n\nUse jq or python to parse the file. Return the complete list — do not summarize or omit any entries. Format as a table or structured list."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bc5f4965-b9c9-4c46-9109-14848d79f92e",
  "uuid": "00521d7f-b143-442c-8378-bb0c84fdded5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EoR1P1DYwpef1GKSvhXcN9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7467,
      "cache_read_input_tokens": 26971,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7467
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

_source line 17_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "a01ea92613c0e609d",
  "tool_use_id": "toolu_01SfhnwAfu5FGq4CJbNHa37Q",
  "description": "Extract eval metrics from registry",
  "task_type": "local_agent",
  "prompt": "I need you to extract all eval experiment results from a large registry JSON file. The file is at:\n/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/bc5f4965-b9c9-4c46-9109-14848d79f92e/tool-results/mcp-agent-ml-research-read_registry-1779194396202.txt\n\nThe file schema is `{result: string}` where the `result` field is a JSON string that needs to be parsed again.\n\nI need you to extract ALL experiments whose `experiment_id` contains \"eval\" (case-insensitive). For each, report:\n1. experiment_id\n2. status\n3. conclusion (if any)\n4. Any metrics (especially ign_f1)\n5. Any relevant notes about protocol (D076, etc.)\n\nAlso extract these specific non-eval experiments if they exist:\n- random_rsft_k1_eval or random_rsft_k1_baseline\n- Any experiment with \"grpo\" in the name\n- Any experiment with \"no_evidence\" in the name\n\nUse jq or python to parse the file. Return the complete list — do not summarize or omit any entries. Format as a table or structured list.",
  "uuid": "cad35edf-e2b7-4d51-a6f9-747506747088",
  "session_id": "bc5f4965-b9c9-4c46-9109-14848d79f92e"
}
```

---

## Round 1

36 recorded events

### User

_source line 18 · 2026-05-19T12:40:11.300Z_

I need you to extract all eval experiment results from a large registry JSON file. The file is at:
/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/bc5f4965-b9c9-4c46-9109-14848d79f92e/tool-results/mcp-agent-ml-research-read_registry-1779194396202.txt

The file schema is `{result: string}` where the `result` field is a JSON string that needs to be parsed again.

I need you to extract ALL experiments whose `experiment_id` contains "eval" (case-insensitive). For each, report:
1. experiment_id
2. status
3. conclusion (if any)
4. Any metrics (especially ign_f1)
5. Any relevant notes about protocol (D076, etc.)

Also extract these specific non-eval experiments if they exist:
- random_rsft_k1_eval or random_rsft_k1_baseline
- Any experiment with "grpo" in the name
- Any experiment with "no_evidence" in the name

Use jq or python to parse the file. Return the complete list — do not summarize or omit any entries. Format as a table or structured list.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01SfhnwAfu5FGq4CJbNHa37Q",
  "session_id": "bc5f4965-b9c9-4c46-9109-14848d79f92e",
  "uuid": "d35ba56b-4129-4106-a89a-eb9934885059"
}
```

</details>

---

### System

_source line 19_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a01ea92613c0e609d",
  "tool_use_id": "toolu_01SfhnwAfu5FGq4CJbNHa37Q",
  "description": "Running Check file size",
  "usage": {
    "total_tokens": 16013,
    "tool_uses": 1,
    "duration_ms": 4711
  },
  "last_tool_name": "Bash",
  "uuid": "3d2576b8-ec3c-4402-83e1-f03fc57cf50e",
  "session_id": "bc5f4965-b9c9-4c46-9109-14848d79f92e"
}
```

---

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — Bash · `toolu_01LvJKAUdAR9ep5UMQCzoxQg`</summary>

```json
{
  "command": "wc -c /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/bc5f4965-b9c9-4c46-9109-14848d79f92e/tool-results/mcp-agent-ml-research-read_registry-1779194396202.txt",
  "description": "Check file size"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01SfhnwAfu5FGq4CJbNHa37Q",
  "session_id": "bc5f4965-b9c9-4c46-9109-14848d79f92e",
  "uuid": "2c06e773-8c9e-4d8f-a46a-429d4bcbb9bc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GR7zdcJWiuSc6Hp9qRkBTd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16006,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 16006,
        "ephemeral_1h_input_tokens": 0
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

_source line 21 · 2026-05-19T12:40:16.190Z_

<details><summary>↩ Tool result · `toolu_01LvJKAUdAR9ep5UMQCzoxQg`</summary>

```text
150644 /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/bc5f4965-b9c9-4c46-9109-14848d79f92e/tool-results/mcp-agent-ml-research-read_registry-1779194396202.txt
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01SfhnwAfu5FGq4CJbNHa37Q",
  "session_id": "bc5f4965-b9c9-4c46-9109-14848d79f92e",
  "uuid": "ba98902f-fe2a-42af-9e87-5f313ae69ca0"
}
```

</details>

---

### System

_source line 22_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a01ea92613c0e609d",
  "tool_use_id": "toolu_01SfhnwAfu5FGq4CJbNHa37Q",
  "description": "Running Parse outer JSON and inspect top-level structure",
  "usage": {
    "total_tokens": 17189,
    "tool_uses": 2,
    "duration_ms": 11075
  },
  "last_tool_name": "Bash",
  "uuid": "44938d01-946b-4e5c-b12f-9505ebf166d5",
  "session_id": "bc5f4965-b9c9-4c46-9109-14848d79f92e"
}
```

---

### Tool call

_source line 23_

<details open><summary>🔧 Tool call — Bash · `toolu_01HZ389KDMeaB1XtUytvNf19`</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/bc5f4965-b9c9-4c46-9109-14848d79f92e/tool-results/mcp-agent-ml-research-read_registry-1779194396202.txt', 'r') as f:\n    outer = json.load(f)\n\n# Parse the inner result string\nregistry = json.loads(outer['result'])\n\n# Show top-level keys\nprint('Top-level keys:', list(registry.keys())[:20])\nprint()\n\n# Check structure\nfor k in registry:\n    v = registry[k]\n    if isinstance(v, dict):\n        print(f'{k}: dict with keys {list(v.keys())[:10]}')\n    elif isinstance(v, list):\n        print(f'{k}: list with {len(v)} items')\n    else:\n        print(f'{k}: {type(v).__name__} = {str(v)[:100]}')\n\" 2>&1 | head -50",
  "description": "Parse outer JSON and inspect top-level structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01SfhnwAfu5FGq4CJbNHa37Q",
  "session_id": "bc5f4965-b9c9-4c46-9109-14848d79f92e",
  "uuid": "a77dd6be-c926-46bc-844a-1ff12796a74a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016NEtH9cvaGJMXgHkfzQcYk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1122,
      "cache_read_input_tokens": 16006,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1122,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 56,
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

_source line 24 · 2026-05-19T12:40:22.485Z_

<details><summary>↩ Tool result · `toolu_01HZ389KDMeaB1XtUytvNf19`</summary>

```text
Top-level keys: ['success', 'data', 'error', 'metadata']

success: bool = True
data: dict with keys ['experiments', 'count', 'total', 'baseline']
error: NoneType = None
metadata: dict with keys ['elapsed_seconds']
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01SfhnwAfu5FGq4CJbNHa37Q",
  "session_id": "bc5f4965-b9c9-4c46-9109-14848d79f92e",
  "uuid": "a75a23f3-5eb6-477d-ab47-d8f22259e371"
}
```

</details>

---

### System

_source line 25_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a01ea92613c0e609d",
  "tool_use_id": "toolu_01SfhnwAfu5FGq4CJbNHa37Q",
  "description": "Running List all experiment IDs and statuses",
  "usage": {
    "total_tokens": 17696,
    "tool_uses": 3,
    "duration_ms": 17535
  },
  "last_tool_name": "Bash",
  "uuid": "7333d903-f321-4bbc-a87e-1d3788fe527d",
  "session_id": "bc5f4965-b9c9-4c46-9109-14848d79f92e"
}
```

---

### Tool call

_source line 26_

<details open><summary>🔧 Tool call — Bash · `toolu_01W85eip2WTjgkZA2BR2YziN`</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/bc5f4965-b9c9-4c46-9109-14848d79f92e/tool-results/mcp-agent-ml-research-read_registry-1779194396202.txt', 'r') as f:\n    outer = json.load(f)\n\nregistry = json.loads(outer['result'])\nexperiments = registry['data']['experiments']\n\nprint(f'Total experiments: {len(experiments)}')\nprint()\n\n# List all experiment_ids\nfor exp in experiments:\n    eid = exp.get('experiment_id', 'N/A')\n    status = exp.get('status', 'N/A')\n    print(f'  {eid}  [{status}]')\n\" 2>&1",
  "description": "List all experiment IDs and statuses"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01SfhnwAfu5FGq4CJbNHa37Q",
  "session_id": "bc5f4965-b9c9-4c46-9109-14848d79f92e",
  "uuid": "28b586ad-ca27-4839-b214-acf02e2af7e5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F34ffQaKsoSq3QwvtLcUNf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 435,
      "cache_read_input_tokens": 17128,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 435,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 72,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    },
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-19T12:40:29.082Z_

<details><summary>↩ Tool result · reported error · `toolu_01W85eip2WTjgkZA2BR2YziN`</summary>

```text
Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 15, in &lt;module>
    eid = exp.get('experiment_id', 'N/A')
          ^^^^^^^
AttributeError: 'str' object has no attribute 'get'
Total experiments: 242
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01SfhnwAfu5FGq4CJbNHa37Q",
  "session_id": "bc5f4965-b9c9-4c46-9109-14848d79f92e",
  "uuid": "7526a8c5-34c7-4a2d-84cc-691c95500d9a",
  "tool_use_result": "Error: Exit code 1\nTraceback (most recent call last):\n  File \"&lt;string>\", line 15, in &lt;module>\n    eid = exp.get('experiment_id', 'N/A')\n          ^^^^^^^\nAttributeError: 'str' object has no attribute 'get'\nTotal experiments: 242"
}
```

</details>

---

### System

_source line 28_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a01ea92613c0e609d",
  "tool_use_id": "toolu_01SfhnwAfu5FGq4CJbNHa37Q",
  "description": "Running Inspect experiments data structure",
  "usage": {
    "total_tokens": 18166,
    "tool_uses": 4,
    "duration_ms": 26420
  },
  "last_tool_name": "Bash",
  "uuid": "99151678-2e5d-4778-927d-d3082b272c5c",
  "session_id": "bc5f4965-b9c9-4c46-9109-14848d79f92e"
}
```

---

### Tool call

_source line 29_

<details open><summary>🔧 Tool call — Bash · `toolu_01NqLRfwSEaNR5LK4NuuGnrk`</summary>

```json
{
  "command": "python3 -c \"\nimport json\n\nwith open('/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/bc5f4965-b9c9-4c46-9109-14848d79f92e/tool-results/mcp-agent-ml-research-read_registry-1779194396202.txt', 'r') as f:\n    outer = json.load(f)\n\nregistry = json.loads(outer['result'])\nexperiments = registry['data']['experiments']\n\n# Check if experiments is a dict (keyed by experiment_id) or list\nprint(f'Type: {type(experiments)}')\nif isinstance(experiments, dict):\n    keys = list(experiments.keys())\n    print(f'Keys (first 10): {keys[:10]}')\n    # Check first value\n    first_key = keys[0]\n    first_val = experiments[first_key]\n    print(f'First value type: {type(first_val)}')\n    print(f'First value (truncated): {json.dumps(first_val, indent=2)[:500]}')\nelif isinstance(experiments, list):\n    print(f'First item type: {type(experiments[0])}')\n    print(f'First item: {experiments[0][:200] if isinstance(experiments[0], str) else json.dumps(experiments[0], indent=2)[:500]}')\n\" 2>&1",
  "description": "Inspect experiments data structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01SfhnwAfu5FGq4CJbNHa37Q",
  "session_id": "bc5f4965-b9c9-4c46-9109-14848d79f92e",
  "uuid": "59e52933-74e3-49b3-b2f4-9564112636df",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dp9TVdPpKD3VVnoshRhJrc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 833,
      "cache_read_input_tokens": 17128,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 833,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 72,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    },
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-19T12:40:37.845Z_

<details><summary>↩ Tool result · `toolu_01NqLRfwSEaNR5LK4NuuGnrk`</summary>

```text
Type: &lt;class 'dict'>
Keys (first 10): ['d112_rsft_s44_eval', 'plan019_1_7b_rsft_s44_r2_eval', 'd112_rsft_s44_train', 'plan017_14b_sft_eval', 'plan017_14b_sft_no_evidence_eval', 'plan019_1_7b_rsft_s43_r2_eval', 'plan017_14b_sft', 'plan019_1_7b_rsft_s44_r2', 'plan019_1_7b_rsft_s43_r2', 'plan019_1_7b_rsft_s44']
First value type: &lt;class 'dict'>
First value (truncated): {
  "status": "DONE",
  "created_at": "2026-05-19T07:34:55.266Z",
  "updated_at": "2026-05-19T12:02:10.888Z",
  "hypothesis": "D112 step 4: D076 eval for RSFT trained on SFT s44 base with CED k=1 scored data. \u9a8c\u8bc1 RSFT \u5728\u6700\u5f3a SFT seed (s44, ign_f1=0.4734) \u4e0a\u7684\u6cdb\u5316\u6548\u679c\u3002\u9884\u671f ign_f1 > 0.4734 (SFT s44 baseline)\u3002",
  "parent": "d112_rsft_s44_train",
  "conclusion": "failed",
  "metrics": {
    "ign_f1": 0.2181,
    "note": "INVALID: QLoRA
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01SfhnwAfu5FGq4CJbNHa37Q",
  "session_id": "bc5f4965-b9c9-4c46-9109-14848d79f92e",
  "uuid": "be0531e3-09e5-4355-90f2-e5dd9af1602e"
}
```

</details>

---

### System

_source line 31_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a01ea92613c0e609d",
  "tool_use_id": "toolu_01SfhnwAfu5FGq4CJbNHa37Q",
  "description": "Running Extract all matching experiments with full details",
  "usage": {
    "total_tokens": 19125,
    "tool_uses": 5,
    "duration_ms": 41787
  },
  "last_tool_name": "Bash",
  "uuid": "6c58f37a-7133-4e11-adb6-f7a326aa3894",
  "session_id": "bc5f4965-b9c9-4c46-9109-14848d79f92e"
}
```

---

### Tool call

_source line 32_

<details open><summary>🔧 Tool call — Bash · `toolu_01Nc83c363QCumzy8BpRq2KS`</summary>

```json
{
  "command": "python3 << 'PYEOF'\nimport json\n\nwith open('/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/bc5f4965-b9c9-4c46-9109-14848d79f92e/tool-results/mcp-agent-ml-research-read_registry-1779194396202.txt', 'r') as f:\n    outer = json.load(f)\n\nregistry = json.loads(outer['result'])\nexperiments = registry['data']['experiments']\n\n# Filter: eval in name (case-insensitive), or specific patterns\nresults = []\nfor eid, exp in experiments.items():\n    eid_lower = eid.lower()\n    match_eval = 'eval' in eid_lower\n    match_random_rsft = 'random_rsft' in eid_lower\n    match_grpo = 'grpo' in eid_lower\n    match_no_evidence = 'no_evidence' in eid_lower\n    \n    if match_eval or match_random_rsft or match_grpo or match_no_evidence:\n        category = []\n        if match_eval: category.append('eval')\n        if match_random_rsft: category.append('random_rsft')\n        if match_grpo: category.append('grpo')\n        if match_no_evidence: category.append('no_evidence')\n        \n        results.append({\n            'experiment_id': eid,\n            'category': ', '.join(category),\n            'status': exp.get('status', 'N/A'),\n            'conclusion': exp.get('conclusion', ''),\n            'metrics': exp.get('metrics', {}),\n            'hypothesis': exp.get('hypothesis', ''),\n            'parent': exp.get('parent', ''),\n            'created_at': exp.get('created_at', ''),\n            'updated_at': exp.get('updated_at', ''),\n        })\n\n# Sort by experiment_id\nresults.sort(key=lambda x: x['experiment_id'])\n\nprint(f\"Total matching experiments: {len(results)}\")\nprint(\"=\" * 140)\n\nfor r in results:\n    print(f\"\\n### {r['experiment_id']}\")\n    print(f\"  Category:   {r['category']}\")\n    print(f\"  Status:     {r['status']}\")\n    print(f\"  Conclusion: {r['conclusion'] or '(none)'}\")\n    print(f\"  Parent:     {r['parent'] or '(none)'}\")\n    \n    metrics = r['metrics']\n    if metrics:\n        ign_f1 = metrics.get('ign_f1', None)\n        if ign_f1 is not None:\n            print(f\"  ign_f1:     {ign_f1}\")\n        # Print all metric keys\n        for mk, mv in metrics.items():\n            if mk != 'ign_f1':\n                val_str = str(mv)\n                if len(val_str) > 200:\n                    val_str = val_str[:200] + '...'\n                print(f\"  {mk}: {val_str}\")\n    else:\n        print(f\"  Metrics:    (none)\")\n    \n    # Print hypothesis truncated\n    hyp = r['hypothesis']\n    if hyp:\n        if len(hyp) > 300:\n            hyp = hyp[:300] + '...'\n        print(f\"  Hypothesis: {hyp}\")\n    \n    print(f\"  Created:    {r['created_at']}\")\n    print(f\"  Updated:    {r['updated_at']}\")\n\nPYEOF\n",
  "description": "Extract all matching experiments with full details",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01SfhnwAfu5FGq4CJbNHa37Q",
  "session_id": "bc5f4965-b9c9-4c46-9109-14848d79f92e",
  "uuid": "cccf988c-b9f7-43bd-9193-f422d4e3423c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Mf7Chw274he5qXNGwfAeqc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 905,
      "cache_read_input_tokens": 17961,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 905,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 54,
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

_source line 33 · 2026-05-19T12:40:53.260Z_

<details><summary>↩ Tool result · `toolu_01Nc83c363QCumzy8BpRq2KS`</summary>

```text
&lt;persisted-output>
Output too large (71.2KB). Full output saved to: /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/bc5f4965-b9c9-4c46-9109-14848d79f92e/tool-results/bzi6o1ptf.txt

Preview (first 2KB):
Total matching experiments: 149
============================================================================================================================================

### d102_llama_rsft_k1_s43_eval
  Category:   eval
  Status:     DONE
  Conclusion: killed
  Parent:     rsft_llama_k1_s43_train
  Metrics:    (none)
  Hypothesis: LLaMA-8B RSFT k=1 seed43 eval: paired with s42 (rel_f1=0.5839) for seed robustness. If s43 gives similar results (±1.5pp), cross-architecture RSFT k=1 claim is robust. Expected rel_f1 ~0.58±0.015.
  Created:    2026-05-18T13:06:23.193Z
  Updated:    2026-05-18T13:59:53.656Z

### d111_4b_sft_s42_reeval
  Category:   eval
  Status:     DONE
  Conclusion: success
  Parent:     (none)
  ign_f1:     0.3974
  rel_f1: 0.4049
  evi_f1: 0.7986
  evi_f1_joint: 0.3147
  edcr: 0.6982
  Hypothesis: Re-evaluating 4B SFT s42 with D076 standardized protocol to establish fair 3-seed comparison with s43 and s44. Previous s42 evaluations gave inconsistent results (0.4106/0.4036/0.3974), so re-running with identical protocol resolves this.
  Created:    2026-05-18T22:06:04.423Z
  Updated:    2026-05-19T03:54:03.116Z

### d112_rsft_s44_eval
  Category:   eval
  Status:     DONE
  Conclusion: failed
  Parent:     d112_rsft_s44_train
  ign_f1:     0.2181
  note: INVALID: QLoRA confound — adapter trained on 4-bit quantized backbone evaluated in bf16
  Hypothesis: D112 step 4: D076 eval for RSFT trained on SFT s44 base with CED k=1 scored data. 验证 RSFT 在最强 SFT seed (s44, ign_f1=0.4734) 上的泛化效果。预期 ign_f1 > 0.4734 (SFT s44 baseline)。
  Created:    2026-05-19T07:34:55.266Z
  Updated:    2026-05-19T12:02:10.888Z

### eval_flat_nli_s44
  Category:   eval
  Status:     DONE
  Conclusion: success
  Parent:     plan_001_flat_nli_seed44
  ign_f1:     0.452126
  rel_f1: 0.461506
  evi_f1: 0.813123
  edcr: 0.645808
  evi_f1_joint: 0.359673
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01SfhnwAfu5FGq4CJbNHa37Q",
  "session_id": "bc5f4965-b9c9-4c46-9109-14848d79f92e",
  "uuid": "fab48dd8-69a5-4a08-8a4f-43ff784ccfdc"
}
```

</details>

---

### System

_source line 34_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a01ea92613c0e609d",
  "tool_use_id": "toolu_01SfhnwAfu5FGq4CJbNHa37Q",
  "description": "Reading ~/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/bc5f4965-b9c9-4c46-9109-14848d79f92e/tool-results/bzi6o1ptf.txt",
  "usage": {
    "total_tokens": 21097,
    "tool_uses": 6,
    "duration_ms": 44178
  },
  "last_tool_name": "Read",
  "uuid": "e49b727c-79ed-4108-ae04-0f46e016e450",
  "session_id": "bc5f4965-b9c9-4c46-9109-14848d79f92e"
}
```

---

### Tool call

_source line 35_

<details open><summary>🔧 Tool call — Read · `toolu_01VamRmZ4HokMNuKAF8TXFhS`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/bc5f4965-b9c9-4c46-9109-14848d79f92e/tool-results/bzi6o1ptf.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01SfhnwAfu5FGq4CJbNHa37Q",
  "session_id": "bc5f4965-b9c9-4c46-9109-14848d79f92e",
  "uuid": "1d7426bf-0cc2-4f38-ae83-d3b7b8d21df1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EpAkF8kFWN3HD1apdcwFRF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1903,
      "cache_read_input_tokens": 18866,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1903,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 69,
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

_source line 36 · 2026-05-19T12:40:55.904Z_

<details><summary>↩ Tool result · reported error · `toolu_01VamRmZ4HokMNuKAF8TXFhS`</summary>

```text
File content (32736 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01SfhnwAfu5FGq4CJbNHa37Q",
  "session_id": "bc5f4965-b9c9-4c46-9109-14848d79f92e",
  "uuid": "bfc874b9-807b-41f2-9b32-33c820f2a896",
  "tool_use_result": "Error: File content (32736 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file."
}
```

</details>

---

### System

_source line 37_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a01ea92613c0e609d",
  "tool_use_id": "toolu_01SfhnwAfu5FGq4CJbNHa37Q",
  "description": "Reading ~/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/bc5f4965-b9c9-4c46-9109-14848d79f92e/tool-results/bzi6o1ptf.txt",
  "usage": {
    "total_tokens": 21361,
    "tool_uses": 7,
    "duration_ms": 47551
  },
  "last_tool_name": "Read",
  "uuid": "1dacfaa6-ac7e-4794-aabf-5441d4aecc63",
  "session_id": "bc5f4965-b9c9-4c46-9109-14848d79f92e"
}
```

---

### Tool call

_source line 38_

<details open><summary>🔧 Tool call — Read · `toolu_01Fsh5sjyR4k75YZ7pciZyXz`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/bc5f4965-b9c9-4c46-9109-14848d79f92e/tool-results/bzi6o1ptf.txt",
  "limit": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01SfhnwAfu5FGq4CJbNHa37Q",
  "session_id": "bc5f4965-b9c9-4c46-9109-14848d79f92e",
  "uuid": "6d87ad06-9906-4a91-b6c3-b16f7aeb8597",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Da2eYP8VCoTzkVGw7BhVXg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 192,
      "cache_read_input_tokens": 20769,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 192,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 72,
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

_source line 39 · 2026-05-19T12:40:58.865Z_

<details><summary>↩ Tool result · `toolu_01Fsh5sjyR4k75YZ7pciZyXz`</summary>

```text
1	Total matching experiments: 149
2	============================================================================================================================================
3	
4	### d102_llama_rsft_k1_s43_eval
5	  Category:   eval
6	  Status:     DONE
7	  Conclusion: killed
8	  Parent:     rsft_llama_k1_s43_train
9	  Metrics:    (none)
10	  Hypothesis: LLaMA-8B RSFT k=1 seed43 eval: paired with s42 (rel_f1=0.5839) for seed robustness. If s43 gives similar results (±1.5pp), cross-architecture RSFT k=1 claim is robust. Expected rel_f1 ~0.58±0.015.
11	  Created:    2026-05-18T13:06:23.193Z
12	  Updated:    2026-05-18T13:59:53.656Z
13	
14	### d111_4b_sft_s42_reeval
15	  Category:   eval
16	  Status:     DONE
17	  Conclusion: success
18	  Parent:     (none)
19	  ign_f1:     0.3974
20	  rel_f1: 0.4049
21	  evi_f1: 0.7986
22	  evi_f1_joint: 0.3147
23	  edcr: 0.6982
24	  Hypothesis: Re-evaluating 4B SFT s42 with D076 standardized protocol to establish fair 3-seed comparison with s43 and s44. Previous s42 evaluations gave inconsistent results (0.4106/0.4036/0.3974), so re-running with identical protocol resolves this.
25	  Created:    2026-05-18T22:06:04.423Z
26	  Updated:    2026-05-19T03:54:03.116Z
27	
28	### d112_rsft_s44_eval
29	  Category:   eval
30	  Status:     DONE
31	  Conclusion: failed
32	  Parent:     d112_rsft_s44_train
33	  ign_f1:     0.2181
34	  note: INVALID: QLoRA confound — adapter trained on 4-bit quantized backbone evaluated in bf16
35	  Hypothesis: D112 step 4: D076 eval for RSFT trained on SFT s44 base with CED k=1 scored data. 验证 RSFT 在最强 SFT seed (s44, ign_f1=0.4734) 上的泛化效果。预期 ign_f1 > 0.4734 (SFT s44 baseline)。
36	  Created:    2026-05-19T07:34:55.266Z
37	  Updated:    2026-05-19T12:02:10.888Z
38	
39	### eval_flat_nli_s44
40	  Category:   eval
41	  Status:     DONE
42	  Conclusion: success
43	  Parent:     plan_001_flat_nli_seed44
44	  ign_f1:     0.452126
45	  rel_f1: 0.461506
46	  evi_f1: 0.813123
47	  edcr: 0.645808
48	  evi_f1_joint: 0.359673
49	  Hypothesis: Full dev eval of flat-NLI RSFT seed=44 with --sft_adapter + --no-quantize. C3 统计显著性数据点 (s42=0.4539, s43 pending, s44 本次, s45 pending)。
50	  Created:    2026-05-15T23:14:05.010Z
51	  Updated:    2026-05-16T03:49:35.610Z
52	
53	### eval_flat_nli_seed44
54	  Category:   eval
55	  Status:     DONE
56	  Conclusion: killed
57	  Parent:     plan_001_flat_nli_seed44
58	  Metrics:    (none)
59	  Hypothesis: Full dev eval of flat-NLI RSFT seed=44 with --sft_adapter + --no-quantize. C3 seed-level comparison.
60	  Created:    2026-05-15T23:12:38.199Z
61	  Updated:    2026-05-15T23:48:28.074Z
62	
63	### eval_flat_nli_seed45
64	  Category:   eval
65	  Status:     DONE
66	  Conclusion: success
67	  Parent:     plan_001_flat_nli_seed45
68	  ign_f1:     0.446181
69	  rel_f1: 0.455052
70	  evi_f1: 0.815399
71	  edcr: 0.652133
72	  evi_f1_joint: 0.355612
73	  Hypothesis: Full dev eval of flat-NLI RSFT seed=45 checkpoint WITH --sft_adapter。seed45 中间 eval rel_f1=0.4876（待全量确认）。对比 CED RSFT mean (0.4596)。三 seed 全量 eval 出齐后汇报 flat-NLI vs CED RSFT 完整 seed-level 对比。
74	  Created:    2026-05-15T23:12:39.186Z
75	  Updated:    2026-05-16T03:49:36.608Z
76	
77	### eval_grpo_g8_bf16
78	  Category:   eval, grpo
79	  Status:     DONE
80	  Conclusion: success
81	  Parent:     (none)
82	  ckpt80_rel_f1: 0.4456
83	  ckpt80_ign_f1: 0.4456
84	  ckpt80_evi_f1: 0.8034
85	  ckpt80_edcr: 0.6409
86	  ckpt80_format_ok: 984/985
87	  ckpt80_truncated: 50
88	  ckpt90_rel_f1: 0.4523
89	  ckpt90_ign_f1: 0.4523
90	  ckpt90_evi_f1: 0.8052
91	  ckpt90_edcr: 0.6414
92	  ckpt90_format_ok: 983/985
93	  ckpt90_truncated: 61
94	  ckpt100_rel_f1: 0.4549
95	  ckpt100_ign_f1: 0.4549
96	  ckpt100_evi_f1: 0.8086
97	  ckpt100_edcr: 0.6318
98	  ckpt100_format_ok: 985/985
99	  ckpt100_truncated: 61
100	  best_checkpoint: ckpt-100
101	  Hypothesis: Eval GRPO G=8 bf16 checkpoints 80/90/100 on full dev set (985 docs). 验证 catastrophic forgetting 是否在 bf16 LoRA 下复现。rel_f1>0.30 → forgetting 不复现 (QLoRA-specific); rel_f1<0.05 → 复现 (C2 加强)。对比: SFT rel_f1=0.4057, QLoRA GRPO rel_f1=0.2167 (catastrophic).
102	  Created:    2026-05-15T14:41:07.474Z
103	  Updated:    2026-05-15T17:57:46.573Z
104	
105	### eval_plan_001_flat_nli
106	  Category:   eval
107	  Status:     DONE
108	  Conclusion: success
109	  Parent:     plan_001_rsft_flat_nli
110	  ign_f1:     0.4539
111	  rel_f1: 0.4539
112	  evi_f1: 0.8043
113	  edcr: 0.6431
114	  precision: 0.4671
115	  recall: 0.4414
116	  evi_precision: 0.8143
117	  evi_recall: 0.7945
118	  format_ok_rate: 1
119	  n_truncated: 199
120	  n_documents: 985
121	  n_predictions: 15294
122	  inference_time_seconds: 3631
123	  Hypothesis: Dev eval of flat-NLI RSFT (plan_001). 对比 CED RSFT (3-seed mean rel_f1=0.4596). flat-NLI ≈ CED → CED contrastive margin 无增益; CED >> flat-NLI → margin 关键。
124	  Created:    2026-05-15T16:57:09.693Z
125	  Updated:    2026-05-15T18:04:13.598Z
126	
127	### eval_plan_001_flat_nli_s43
128	  Category:   eval
129	  Status:     DONE
130	  Conclusion: failed
131	  Parent:     (none)
132	  ign_f1:     0.0022
133	  rel_f1: 0.0022
134	  evi_f1: 0.8533
135	  edcr: 0.9982
136	  num_preds: 17285
137	  format_ok: 981/985
138	  truncated: 251/985
139	  tp: 32
140	  note: INVALID — missing --sft_adapter, same bug as DPO 1ep eval
141	  Created:    2026-05-15T20:29:54.486Z
142	  Updated:    2026-05-15T21:35:00.000Z
143	
144	### eval_plan_008_rsft_topk3
145	  Category:   eval
146	  Status:     DONE
147	  Conclusion: killed
148	  Parent:     plan_008_rsft_topk3
149	  note: INVALID — missing --sft_adapter, killed by Director instruction
150	  Hypothesis: RSFT top_k=3 dev eval: 对比 top_k=1 RSFT (rel_f1≈0.46) 和 SFT baseline (rel_f1≈0.4057)。验证更多候选是否提升证据质量。
151	  Created:    2026-05-15T21:09:51.464Z
152	  Updated:    2026-05-15T21:38:00.000Z
153	
154	### eval_plan_008_topk3_fixed
155	  Category:   eval
156	  Status:     DONE
157	  Conclusion: killed
158	  Parent:     (none)
159	  Metrics:    (none)
160	  Created:    2026-05-15T21:39:34.632Z
161	  Updated:    2026-05-15T21:39:34.632Z
162	
163	### eval_plan_012_dpo_1ep_fixed
164	  Category:   eval
165	  Status:     DONE
166	  Conclusion: killed
167	  Parent:     (none)
168	  Metrics:    (none)
169	  Created:    2026-05-15T21:39:31.570Z
170	  Updated:    2026-05-15T21:39:31.570Z
171	
172	### eval_plan_012_dpo_1ep_fixed_r2
173	  Category:   eval
174	  Status:     DONE
175	  Conclusion: negative
176	  Parent:     (none)
177	  ign_f1:     0.4034
178	  rel_f1: 0.4034
179	  evi_f1: 0.8088
180	  edcr: 0.7139
181	  format_ok_rate: 0.999
182	  truncated_rate: 0.343
183	  predictions: 19107
184	  precision: 0.3809
185	  recall: 0.4287
186	  vs_sft_delta: -0.0023
187	  note: DPO 1ep matches SFT baseline. 1ep→3ep trajectory shows gradual decoupling (rel_f1↓ evi_f1↑), consistent with GRPO pattern. Ign-F1=F1 exact match needs investigation.
188	  Created:    2026-05-15T21:58:52.440Z
189	  Updated:    2026-05-15T23:44:56.586Z
190	
191	### eval_plan_012_dpo_ced_1ep
192	  Category:   eval
193	  Status:     DONE
194	  Conclusion: negative
195	  Parent:     (none)
196	  ign_f1:     0.0022
197	  rel_f1: 0.0022
198	  evi_f1: 0.75
199	  edcr: 0.9982
200	  num_preds: 19265
201	  format_ok: 981/985
202	  truncated: 358/985
203	  tp: 34
204	  inference_time_s: 3643
205	  Created:    2026-05-15T20:22:11.752Z
206	  Updated:    2026-05-15T21:27:30.000Z
207	
208	### eval_plan_012_dpo_ced_ckpt400
209	  Category:   eval
210	  Status:     DONE
211	  Conclusion: failed
212	  Parent:     (none)
213	  Metrics:    (none)
214	  Created:    2026-05-15T19:32:55.398Z
215	  Updated:    2026-05-15T19:37:31.477Z
216	
217	### eval_plan_014_no_evidence
218	  Category:   eval, no_evidence
219	  Status:     DONE
220	  Conclusion: failed
221	  Parent:     plan_014_sft_no_evidence
222	  Metrics:    (none)
223	  Hypothesis: Dev set eval of SFT-no-evidence model (plan_014). 核心目标：对比标准 SFT rel_f1=0.4057 vs 不输出 evidence 的 SFT rel_f1（隔离 evidence generation 代价）。只评估 rel_f1，不评估 evi_f1（输出无 evidence）。plan_id=plan_014, claim=1。
224	  Created:    2026-05-15T23:17:32.011Z
225	  Updated:    2026-05-16T01:34:06.402Z
226	
227	### eval_plan_014_no_evidence_r2
228	  Category:   eval, no_evidence
229	  Status:     DONE
230	  Conclusion: success
231	  Parent:     plan_014_sft_no_evidence
232	  ign_f1:     0.4721
233	  rel_f1: 0.4876
234	  evi_f1: 0
235	  edcr: 0
236	  evi_f1_joint: 0
237	  precision: 0.4901
238	  recall: 0.4851
239	  ign_precision: 0.4654
240	  ign_recall: 0.4791
241	  format_compliance: 0.993
242	  truncation_rate: 0.312
243	  n_predictions: 21181
244	  n_documents: 985
245	  Hypothesis: Retry of eval_plan_014_no_evidence with corrected command: --model_path 传底座 Qwen3-4B, --sft_adapter 传 SFT no-evidence adapter。修复 adapter 检测逻辑冲突。plan_id=plan_014, claim=1。
246	  Created:    2026-05-16T01:34:45.302Z
247	  Updated:    2026-05-16T04:20:13.358Z
248	
249	### eval_plan_014_sft_no_evidence
250	  Category:   eval, no_evidence
251	  Status:     DONE
252	  Conclusion: success
253	  Parent:     (none)
254	  rel_f1: 0.4893
255	  rel_ign_f1: 0.4893
256	  rel_precision: 0.4884
257	  rel_recall: 0.4902
258	  evi_f1: 0
259	  evi_precision: 0
260	  evi_recall: 0
261	  edcr: 0
262	  format_ok_rate: 0.9919
263	  n_truncated: 298
264	  n_predictions: 21064
265	  n_documents: 985
266	  n_parseable: 977
267	  inference_time_seconds: 4103.8
268	  Created:    2026-05-15T17:20:25.574Z
269	  Updated:    2026-05-15T18:42:46.665Z
270	
271	### eval_rsft_ced_s43
272	  Category:   eval
273	  Status:     DONE
274	  Conclusion: success
275	  Parent:     rsft_ced_s43_train_r3
276	  ign_f1:     0.4512
277	  rel_f1: 0.4601
278	  precision: 0.4696
279	  recall: 0.4509
280	  evi_f1: 0.8063
281	  evi_precision: 0.8025
282	  evi_recall: 0.8101
283	  edcr: 0.6542
284	  evi_f1_joint: 0.3605
285	  format_ok_rate: 1
286	  n_truncated: 184
287	  n_predictions: 15051
288	  inference_time_seconds: 10768.2
289	  Hypothesis: Full dev eval of CED RSFT seed=43 with --sft_adapter + --no-quantize. Paired t-test 关键路径：CED 第 4 个 seed。对比 flat-NLI RSFT seeds。plan_id=plan_mvp2_rsft, claim=3。
290	  Created:    2026-05-16T01:30:37.978Z
291	  Updated:    2026-05-16T05:18:59.781Z
292	
293	### eval_rsft_ced_s45
294	  Category:   eval
295	  Status:     DONE
296	  Conclusion: success
297	  Parent:     rsft_ced_s45_train_r4
298	  ign_f1:     0.4416
299	  rel_f1: 0.4514
300	  evi_f1: 0.8174
301	  rel_p: 0.4718
302	  rel_r: 0.4326
303	  edcr: 0.655
304	  evi_f1_joint: 0.3558
305	  n_truncated: 206
306	  format_ok_rate: 1
307	  Hypothesis: Full dev eval of CED RSFT seed=45 with --sft_adapter + --no-quantize. Paired t-test 关键路径：CED 第 3 个 seed（s42/s44 已有，s43 训练中）。对比 flat-NLI RSFT seeds。plan_id=plan_mvp2_rsft, claim=3。
308	  Created:    2026-05-16T01:30:34.036Z
309	  Updated:    2026-05-16T05:43:12.975Z
310	
311	### eval_sft_baseline_noquant
312	  Category:   eval
313	  Status:     DONE
314	  Conclusion: success
315	  Parent:     (none)
316	  rel_f1: 0.4106
317	  rel_precision: 0.4198
318	  rel_recall: 0.4019
319	  evi_f1: 0.8013
320	  evi_precision: 0.8005
321	  evi_recall: 0.8022
322	  evi_f1_joint: 0.3216
323	  edcr: 0.7039
324	  format_ok_rate: 0.998
325	  field_compliance_rate: 0.7066
326	  n_predictions: 16774
327	  n_truncated: 288
328	  n_documents: 985
329	  inference_time_seconds: 3677.9
330	  Created:    2026-05-15T18:38:33.128Z
331	  Updated:    2026-05-15T19:45:42.147Z
332	
333	### grpo_bf16_g4_ckpt100_eval
334	  Category:   eval, grpo
335	  Status:     DONE
336	  Conclusion: success
337	  Parent:     wave1_grpo_bf16_g4
338	  ign_f1:     0.4431
339	  f1: 0.4511
340	  evi_f1: 0.801
341	  evi_f1_joint: 0.3532
342	  EDCR: 0.6453
343	  format_compliance: 0.999
344	  field_compliance: 0.8142
345	  truncated: 182
346	  n_total: 985
347	  n_predictions: 15187
348	  inference_time_seconds: 11458.2
349	  Hypothesis: GRPO bf16 G=4 checkpoint-100 eval (D106 conditional termination): evaluate mid-training checkpoint to decide whether to continue GRPO training to step 200. If rel_f1 >= RSFT baseline (~52pp), continue. If significantly below, consider early termination.
350	  Created:    2026-05-18T16:34:51.597Z
351	  Updated:    2026-05-18T20:08:50.166Z
352	
353	### grpo_bf16_g4_ckpt200_eval
354	  Category:   eval, grpo
355	  Status:     DONE
356	  Conclusion: success
357	  Parent:     wave1_grpo_bf16_g4
358	  ign_f1:     0.4446
359	  rel_f1: 0.4513
360	  evi_f1: 0.8053
361	  evi_f1_joint: 0.3562
362	  edcr: 0.6489
363	  format_ok: 984/985
364	  n_truncated: 204
365	  n_predictions: 15733
366	  field_compliance_rate: 0.792
367	  Hypothesis: GRPO bf16 G=4 checkpoint-200 eval (final): compare with ckpt-100 for D106 learning curve. If ckpt-200 > ckpt-100, GRPO is improving. Expected: rel_f1 improvement over ckpt-100.
368	  Created:    2026-05-18T20:05:54.201Z
369	  Updated:    2026-05-18T23:16:39.233Z
370	
371	### lead2_ckpt20_eval
372	  Category:   eval
373	  Status:     DONE
374	  Conclusion: success
375	  Parent:     lead2_rsft_grpo_ced_r2
376	  ign_f1:     0.4533
377	  rel_f1: 0.4617
378	  evi_f1: 0.8103
379	  evi_f1_joint: 0.3642
380	  edcr: 0.6465
381	  precision: 0.476
382	  recall: 0.4482
383	  format_ok: 985/985
384	  truncated: 187/985
385	  predictions: 14998
386	  Hypothesis: Evaluate GRPO checkpoint-20 from RSFT base (lead2_rsft_grpo_ced_r2) on DocRED dev. If RSFT→GRPO preserves/improves rel_f1 over RSFT baseline (0.4601), it validates the RSFT→GRPO training pipeline as viable.
387	  Created:    2026-05-17T12:31:32.202Z
388	  Updated:    2026-05-17T15:27:15.598Z
389	
390	### lead2_rsft_grpo_ced
391	  Category:   grpo
392	  Status:     DONE
393	  Conclusion: failed
394	  Parent:     mvp2_rsft_train_r1_s43
395	  Metrics:    (none)
396	  Hypothesis: RSFT→bf16 GRPO two-stage: starting from RSFT best checkpoint (s43, rel_f1=0.46), short-range GRPO (50 steps, lr=1e-6) with CED-only reward should further improve evidence quality (EDCR) while preserving rel_f1, because RSFT provides stable base preventing catastrophic forgetting seen in SFT→GRPO.
397	  Created:    2026-05-17T05:57:53.951Z
398	  Updated:    2026-05-17T06:06:36.130Z
399	
400	### lead2_rsft_grpo_ced_r2
401	  Category:   grpo
402	  Status:     DONE
403	  Conclusion: failed
404	  Parent:     lead2_rsft_grpo_ced
405	  Metrics:    (none)
406	  Hypothesis: RSFT→bf16 GRPO two-stage (retry with --data_dir fix): starting from merged RSFT-s43 checkpoint (rel_f1=0.46), short-range GRPO (50 steps, lr=1e-6) with CED-only reward should improve evidence quality (EDCR) while preserving rel_f1.
407	  Created:    2026-05-17T06:23:56.474Z
408	  Updated:    2026-05-17T08:25:20.510Z
409	
410	### mvp2_eval_ced_kl001_r4_ckpt10
411	  Category:   eval
412	  Status:     DONE
413	  Conclusion: success
414	  Parent:     (none)
415	  rel_f1: 0.00296
416	  rel_precision: 0.00314
417	  rel_recall: 0.0028
418	  evi_f1: 0.72
419	  evi_precision: 0.6429
420	  evi_recall: 0.8182
421	  edcr: 0.9983
422	  n_parseable: 984
423	  n_truncated: 24
424	  n_predictions: 11621
425	  tp: 34
426	  pred_count: 10839
427	  gold_count: 12151
428	  inference_time_seconds: 5211.4
429	  Created:    2026-05-14T17:59:08.638Z
430	  Updated:    2026-05-14T19:14:08.763Z
431	
432	### mvp2_eval_ced_kl001_r4_ckpt7080
433	  Category:   eval
434	  Status:     DONE
435	  Conclusion: failed
436	  Parent:     mvp2_grpo_ced_kl001_r4
437	  Metrics:    (none)
438	  Hypothesis: Re-run failed ckpt-70/80 eval from crashed high eval (cuda:3 OOM). Completes 10-checkpoint trajectory for paper negative result analysis.
439	  Created:    2026-05-14T19:50:04.595Z
440	  Updated:    2026-05-14T19:58:46.631Z
441	
442	### mvp2_eval_ced_kl001_r4_ckpt90
443	  Category:   eval
444	  Status:     DONE
445	  Conclusion: killed
446	  Parent:     mvp2_grpo_ced_kl001_r4
447	  Metrics:    (none)
448	  Hypothesis: Eval ced_kl001_r4 best-reward checkpoint (step 90, reward=1.370, f1=0.720) — this is the primary MVP-2 judgment checkpoint. If evi_f1 ≥ SFT baseline (0.7979) + 2pp = 0.8179, MVP-2 passes.
449	  Created:    2026-05-14T18:18:13.270Z
450	  Updated:    2026-05-14T19:17:36.777Z
451	
452	### mvp2_eval_ced_kl001_r4_early
453	  Category:   eval
454	  Status:     DONE
455	  Conclusion: negative
456	  Parent:     (none)
457	  ign_f1:     0.1563
458	  f1: 0.1563
459	  evi_f1: 0.5643
460	  edcr: 0.8858
461	  precision: 0.2356
462	  recall: 0.1169
463	  evi_precision: 0.4864
464	  evi_recall: 0.6721
465	  format_ok_rate: 0.999
466	  n_parseable: 984
467	  n_truncated: 11
468	  n_predictions: 9250
469	  tp: 1421
470	  pred_count: 6032
471	  gold_count: 12151
472	  Created:    2026-05-14T17:12:53.581Z
473	  Updated:    2026-05-14T18:31:18.065Z
474	
475	### mvp2_eval_ced_kl001_r4_high
476	  Category:   eval
477	  Status:     DONE
478	  Conclusion: failed
479	  Parent:     mvp2_grpo_ced_kl001_r4
480	  checkpoint_60: {'rel_f1': 0.1467, 'ign_f1': 0.1467, 'precision': 0.1909, 'recall': 0.1192, 'evi_f1': 0.5763, 'edcr': 0.9062, 'pred_count': 10041, 'gold_count': 12151, 'n_truncated': 16, 'format_ok_rate': 1}
481	  note: Only ckpt-60 completed. Process died during ckpt-70 inference at 8% (5/62 batch). ckpt-80/90 never started.
482	  Hypothesis: High-end checkpoint eval (60,70,80,90) on cuda:3, complementing cuda:2 low-end eval. Step 90 is true best checkpoint (reward=1.370). D024 directive.
483	  Created:    2026-05-14T18:19:07.637Z
484	  Updated:    2026-05-14T19:47:58.282Z
485	
486	### mvp2_eval_ced_kl001_r4_last
487	  Category:   eval
488	  Status:     DONE
489	  Conclusion: killed
490	  Parent:     (none)
491	  Metrics:    (none)
492	  Created:    2026-05-14T18:10:05.820Z
493	  Updated:    2026-05-15T12:09:21.004Z
494	
495	### mvp2_eval_ced_kl001_r4_multi
496	  Category:   eval
497	  Status:     DONE
498	  Conclusion: killed
499	  Parent:     (none)
500	  checkpoint-10: {'f1': 0.003, 'ign_f1': 0.003, 'evi_f1': 0.72, 'edcr': 0.9983, 'format_ok_rate': 0.999}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01SfhnwAfu5FGq4CJbNHa37Q",
  "session_id": "bc5f4965-b9c9-4c46-9109-14848d79f92e",
  "uuid": "648598fc-80c5-4ca3-adb4-ed36e9d0f803"
}
```

</details>

---

### System

_source line 40_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a01ea92613c0e609d",
  "tool_use_id": "toolu_01SfhnwAfu5FGq4CJbNHa37Q",
  "description": "Reading ~/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/bc5f4965-b9c9-4c46-9109-14848d79f92e/tool-results/bzi6o1ptf.txt",
  "usage": {
    "total_tokens": 29976,
    "tool_uses": 8,
    "duration_ms": 52790
  },
  "last_tool_name": "Read",
  "uuid": "db1049b3-da9b-4748-8759-b934a296dd2f",
  "session_id": "bc5f4965-b9c9-4c46-9109-14848d79f92e"
}
```

---

### Tool call

_source line 41_

<details open><summary>🔧 Tool call — Read · `toolu_01SBqLaXkY6r1KjY8aJkmwCM`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/bc5f4965-b9c9-4c46-9109-14848d79f92e/tool-results/bzi6o1ptf.txt",
  "offset": 500,
  "limit": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01SfhnwAfu5FGq4CJbNHa37Q",
  "session_id": "bc5f4965-b9c9-4c46-9109-14848d79f92e",
  "uuid": "9edb91d2-f4b4-4a4e-9f11-dc59144785e1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012Gwcz8iwhpoyeg8wy5exUh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8577,
      "cache_read_input_tokens": 20961,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8577,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
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

_source line 42 · 2026-05-19T12:41:04.102Z_

<details><summary>↩ Tool result · `toolu_01SBqLaXkY6r1KjY8aJkmwCM`</summary>

```text
500	  checkpoint-10: {'f1': 0.003, 'ign_f1': 0.003, 'evi_f1': 0.72, 'edcr': 0.9983, 'format_ok_rate': 0.999}
501	  checkpoint-20: {'f1': 0.0088, 'ign_f1': 0.0088, 'evi_f1': 0.423, 'edcr': 0.9954, 'format_ok_rate': 0.999}
502	  checkpoint-30: {'f1': 0.0338, 'ign_f1': 0.0338, 'evi_f1': 0.5889, 'edcr': 0.9798, 'format_ok_rate': 1}
503	  checkpoint-50: {'f1': 0.1563, 'ign_f1': 0.1563, 'evi_f1': 0.5643, 'edcr': 0.8858, 'format_ok_rate': 0.999}
504	  checkpoint-60: {'f1': 0.1467, 'ign_f1': 0.1467, 'evi_f1': 0.5763, 'edcr': 0.9062, 'format_ok_rate': 1}
505	  checkpoint-90: {'f1': 0.2108, 'ign_f1': 0.2108, 'evi_f1': 0.5666, 'edcr': 0.8584, 'format_ok_rate': 1}
506	  Created:    2026-05-14T17:59:22.291Z
507	  Updated:    2026-05-14T21:27:25.338Z
508	
509	### mvp2_eval_ced_kl001_r4_step100
510	  Category:   eval
511	  Status:     DONE
512	  Conclusion: negative
513	  Parent:     mvp2_grpo_ced_kl001_r4
514	  ign_f1:     0.2167
515	  rel_f1: 0.2167
516	  precision: 0.2849
517	  recall: 0.1749
518	  evi_f1: 0.5746
519	  evi_precision: 0.5244
520	  evi_recall: 0.6353
521	  edcr: 0.8539
522	  pred_count: 7460
523	  gold_count: 12151
524	  tp: 2125
525	  n_truncated: 21
526	  format_ok_rate: 1
527	  Hypothesis: Eval ced_kl001_r4 last checkpoint (step 100) to compare with best-reward checkpoint (step 50). If best ≠ last, the gap measures training stability under batch_size=1 GRPO variance.
528	  Created:    2026-05-14T18:08:31.821Z
529	  Updated:    2026-05-14T19:41:30.318Z
530	
531	### mvp2_eval_ced_kl001_r4_step90
532	  Category:   eval
533	  Status:     DONE
534	  Conclusion: negative
535	  Parent:     mvp2_grpo_ced_kl001_r4
536	  ign_f1:     0.2108
537	  rel_f1: 0.2108
538	  evi_f1: 0.5666
539	  edcr: 0.8584
540	  pred_count: 11160
541	  n_truncated: 22
542	  format_ok_rate: 1
543	  n_documents: 985
544	  Hypothesis: Eval true best checkpoint (step 90, reward=1.370). Critical after ckpt-50 showed reward hacking (rel_f1 -24.9pp). If step 90 also fails, CED reward design has fundamental issue.
545	  Created:    2026-05-14T18:19:58.623Z
546	  Updated:    2026-05-14T20:01:45.201Z
547	
548	### mvp2_eval_lr5e6_r1_ckpt100
549	  Category:   eval
550	  Status:     DONE
551	  Conclusion: negative
552	  Parent:     mvp2_grpo_ced_lr5e6_r1
553	  ign_f1:     0.0138
554	  rel_f1: 0.0138
555	  rel_precision: 0.0132
556	  rel_recall: 0.0144
557	  evi_f1: 0.8504
558	  evi_precision: 0.9256
559	  evi_recall: 0.7866
560	  edcr: 0.9876
561	  format_ok_rate: 0.999
562	  field_compliance_rate: 0.8162
563	  evidence_format_rate: 0.8162
564	  tp: 175
565	  pred_count: 13300
566	  gold_count: 12151
567	  n_predictions: 15498
568	  n_truncated: 181
569	  n_documents: 985
570	  n_parseable: 984
571	  inference_time_seconds: 5901.7
572	  Hypothesis: P0 ckpt-100 eval: lr=5e-6 GRPO at step 100 (halfway point). Checkpoint-100 已保存。与 kl001_r4 的 step-100 (rel_f1=0.217) 形成直接对比。Pass criteria: rel_f1 > 0.30.
573	  Created:    2026-05-14T23:00:57.035Z
574	  Updated:    2026-05-15T01:30:01.493Z
575	
576	### mvp2_eval_lr5e6_r1_ckpt20
577	  Category:   eval
578	  Status:     DONE
579	  Conclusion: negative
580	  Parent:     mvp2_grpo_ced_lr5e6_r1
581	  rel_f1: 0.0077
582	  rel_precision: 0.0071
583	  rel_recall: 0.0084
584	  evi_f1: 0.628
585	  evi_precision: 0.855
586	  evi_recall: 0.496
587	  edcr: 0.993
588	  format_ok_rate: 0.991
589	  field_compliance_rate: 0.399
590	  pred_count: 14440
591	  gold_count: 12151
592	  tp: 102
593	  n_truncated: 587
594	  inference_time_seconds: 6370.4
595	  Hypothesis: P0 ckpt-20 early eval: lr=5e-6 GRPO at step 20. Pass criteria: rel_f1 > 0.30 (no catastrophic forgetting). Key MVP gate for P0.
596	  Created:    2026-05-14T20:44:21.167Z
597	  Updated:    2026-05-14T22:12:16.372Z
598	
599	### mvp2_eval_lr5e6_r1_ckpt40
600	  Category:   eval
601	  Status:     DONE
602	  Conclusion: failed
603	  Parent:     mvp2_grpo_ced_lr5e6_r1
604	  Metrics:    (none)
605	  Hypothesis: P0 ckpt-40 eval: lr=5e-6 GRPO at step 40 (where f1_reward first rises to 0.038). Director 新判定框架: ckpt-20 FAIL + ckpt-40 PASS → P0 判 PASS。Pass criteria: rel_f1 > 0.30.
606	  Created:    2026-05-14T21:25:00.579Z
607	  Updated:    2026-05-14T21:43:33.438Z
608	
609	### mvp2_eval_lr5e6_r1_ckpt40_r2
610	  Category:   eval
611	  Status:     DONE
612	  Conclusion: negative
613	  Parent:     mvp2_grpo_ced_lr5e6_r1
614	  rel_f1: 0.0071
615	  precision: 0.0066
616	  recall: 0.0078
617	  evi_f1: 0.7584
618	  evi_precision: 0.9113
619	  evi_recall: 0.6494
620	  edcr: 0.9942
621	  format_ok_rate: 0.9939
622	  field_compliance_rate: 0.5675
623	  pred_count: 14434
624	  gold_count: 12151
625	  tp: 95
626	  n_truncated: 424
627	  inference_time_seconds: 6152
628	  Hypothesis: Re-tracking orphan PID 101842 for P0 ckpt-40 eval (lr=5e-6 GRPO step 40). Original exp auto-failed due to cron/PID mismatch. Pass criteria: rel_f1 > 0.30.
629	  Created:    2026-05-14T21:41:34.558Z
630	  Updated:    2026-05-14T23:11:56.267Z
631	
632	### mvp2_eval_lr5e6_r1_ckpt60
633	  Category:   eval
634	  Status:     DONE
635	  Conclusion: failed
636	  Parent:     mvp2_grpo_ced_lr5e6_r1
637	  Metrics:    (none)
638	  Hypothesis: P0 ckpt-60 eval: lr=5e-6 GRPO at step 60. 训练轨迹数据点——ckpt-20 catastrophic forgetting (rel_f1=0.0077)，需看后续 checkpoint 是否恢复。Pass criteria: rel_f1 > 0.30.
639	  Created:    2026-05-14T22:13:47.936Z
640	  Updated:    2026-05-14T23:25:25.584Z
641	
642	### mvp2_eval_lr5e6_r1_ckpt60_r2
643	  Category:   eval
644	  Status:     DONE
645	  Conclusion: negative
646	  Parent:     mvp2_grpo_ced_lr5e6_r1
647	  rel_f1: 0.0093
648	  precision: 0.0085
649	  recall: 0.0103
650	  evi_f1: 0.81
651	  edcr: 0.993
652	  format_ok_rate: 0.998
653	  pred_count: 14626
654	  gold_count: 12151
655	  tp: 125
656	  inference_time_seconds: 6152
657	  Hypothesis: P0 ckpt-60 eval retry: 原 submit_on_allocated 失败 (pid=unknown). 手动 SSH 启动 /root/autodl-tmp/scripts/eval_lr5e6_ckpt60.sh. Pass criteria: rel_f1 > 0.30.
658	  Created:    2026-05-14T22:27:56.124Z
659	  Updated:    2026-05-15T00:07:56.895Z
660	
661	### mvp2_eval_lr5e6_r1_ckpt80
662	  Category:   eval
663	  Status:     DONE
664	  Conclusion: negative
665	  Parent:     mvp2_grpo_ced_lr5e6_r1
666	  ign_f1:     0.0116
667	  rel_f1: 0.0116
668	  precision: 0.0109
669	  recall: 0.0124
670	  evi_f1: 0.828
671	  evi_precision: 0.928
672	  evi_recall: 0.748
673	  edcr: 0.993
674	  format_ok_rate: 0.999
675	  field_compliance_rate: 0.788
676	  pred_count: 13828
677	  gold_count: 12151
678	  n_truncated: 210
679	  inference_time_seconds: 6099
680	  Hypothesis: P0 ckpt-80 eval: lr=5e-6 GRPO at step 80. 训练轨迹继续——ckpt-20 FAIL (0.0077), ckpt-40/60 待出. Step 80 reward=0.283 (回升), format_reward=0.249. Pass criteria: rel_f1 > 0.30.
681	  Created:    2026-05-14T22:25:45.043Z
682	  Updated:    2026-05-15T01:02:32.508Z
683	
684	### mvp2_eval_lr5e6_rp_r2_ckpt20
685	  Category:   eval
686	  Status:     DONE
687	  Conclusion: killed
688	  Parent:     mvp2_grpo_ced_lr5e6_rp_r2
689	  Metrics:    (none)
690	  Hypothesis: P0+P1 ckpt-20 eval: lr=5e-6 + recall_penalty GRPO at step 20. Director killed rp_r2 training (loss divergence), but ckpt-20 eval needed to close P0+P1 comparison line. Pass criteria: rel_f1 > 0.30 AND pred_count >= 9720.
691	  Created:    2026-05-14T21:44:56.448Z
692	  Updated:    2026-05-14T22:06:40.812Z
693	
694	### mvp2_eval_rsft_r1
695	  Category:   eval
696	  Status:     DONE
697	  Conclusion: success
698	  Parent:     mvp2_rsft_train_r1
699	  rel_f1: 0.4449
700	  evi_f1: 0.8187
701	  evi_f1_joint: 0.3468
702	  evi_f1_joint_P: 0.3515
703	  evi_f1_joint_R: 0.3423
704	  edcr: 0.6565
705	  num_preds: 15307
706	  sft_baseline_rel_f1: 0.4057
707	  sft_baseline_evi_f1: 0.7979
708	  delta_rel_f1: 0.0392
709	  delta_evi_f1: 0.0208
710	  delta_evi_f1_joint: 0.0351
711	  mvp2_pass: True
712	  Hypothesis: Full dev eval of RSFT r1 (seed=42). Same pipeline as s44 eval (985 docs, no-quantize). Need 3-seed data for complete_mvp. s44 PASS: rel_f1=0.4655, evi_f1=0.8087.
713	  Created:    2026-05-15T09:40:47.529Z
714	  Updated:    2026-05-15T13:27:31.402Z
715	
716	### mvp2_eval_rsft_r2a
717	  Category:   eval
718	  Status:     DONE
719	  Conclusion: success
720	  Parent:     mvp2_rsft_r2a
721	  ign_f1:     0.4494
722	  rel_f1: 0.4494
723	  evi_f1: 0.8108
724	  evi_f1_joint: 0.3509
725	  evi_f1_joint_P: 0.3423
726	  evi_f1_joint_R: 0.3599
727	  edcr: 0.6641
728	  precision: 0.4512
729	  recall: 0.4475
730	  evi_precision: 0.8143
731	  evi_recall: 0.8073
732	  format_ok_rate: 1
733	  n_predictions: 15482
734	  n_truncated: 208
735	  inference_time_s: 5967.2
736	  delta_evi_f1_joint: 0.0392
737	  Hypothesis: Full dev eval of r2a (1 epoch, alpha=128, clean data). Ablation: 1 epoch vs 3 epoch (r1). Pass: rel_f1 > 0.4057, evi_f1 > 0.798.
738	  Created:    2026-05-15T09:42:57.684Z
739	  Updated:    2026-05-15T13:27:32.756Z
740	
741	### mvp2_eval_rsft_r2b
742	  Category:   eval
743	  Status:     DONE
744	  Conclusion: success
745	  Parent:     mvp2_rsft_r2b
746	  ign_f1:     0.4493
747	  rel_f1: 0.4493
748	  evi_f1: 0.8128
749	  evi_f1_joint: 0.349
750	  evi_f1_joint_P: 0.3455
751	  evi_f1_joint_R: 0.3526
752	  edcr: 0.6609
753	  precision: 0.4566
754	  recall: 0.4424
755	  evi_precision: 0.8201
756	  evi_recall: 0.8056
757	  pred_count: 14829
758	  format_ok: 983/985
759	  truncated: 179
760	  inference_time_s: 5862
761	  delta_evi_f1_joint: 0.0373
762	  Hypothesis: Full dev eval of r2b (1 epoch, alpha=32, lr=1e-5, clean data). Ablation: conservative LoRA scaling vs r2a/r1. Pass: rel_f1 > 0.4057, evi_f1 > 0.798.
763	  Created:    2026-05-15T09:42:58.437Z
764	  Updated:    2026-05-15T13:27:35.580Z
765	
766	### mvp2_eval_rsft_r2b_maxtok1536
767	  Category:   eval
768	  Status:     DONE
769	  Conclusion: killed
770	  Parent:     mvp2_eval_rsft_r2b
771	  Metrics:    (none)
772	  Hypothesis: Truncation diagnosis: r2b eval with max_new_tokens=1536 (vs default 1024). If EDCR improves significantly (from 0.6609 toward 0.71+), current EDCR gap is truncation artifact, not model issue. If EDCR unchanged, distractor citation is genuine RSFT behavior.
773	  Created:    2026-05-15T11:49:48.849Z
774	  Updated:    2026-05-15T13:23:59.642Z
775	
776	### mvp2_eval_rsft_r2b_maxtok1536_r2
777	  Category:   eval
778	  Status:     DONE
779	  Conclusion: negative
780	  Parent:     mvp2_eval_rsft_r2b
781	  ign_f1:     0.4504
782	  rel_f1: 0.4504
783	  evi_f1: 0.8102
784	  edcr: 0.674
785	  precision: 0.4488
786	  recall: 0.4519
787	  evi_precision: 0.8162
788	  evi_recall: 0.8044
789	  n_truncated: 146
790	  n_total: 985
791	  n_predictions: 17188
792	  n_distractor_citations: 19589
793	  n_total_citations: 29063
794	  format_ok_rate: 0.998
795	  Hypothesis: Truncation diagnosis: r2b eval with max_new_tokens=1536 (vs default 1024). Retry with correct model stack (Base+SFT+RSFT). If EDCR improves significantly (from 0.6609 toward 0.71+), truncation is the cause. If unchanged, distractor citation is genuine RSFT behavior.
796	  Created:    2026-05-15T11:54:57.156Z
797	  Updated:    2026-05-15T15:21:13.816Z
798	
799	### mvp2_eval_rsft_s43
800	  Category:   eval
801	  Status:     DONE
802	  Conclusion: failed
803	  Parent:     mvp2_rsft_train_r1_s43
804	  Metrics:    (none)
805	  Hypothesis: Full dev eval of RSFT s43 (seed=43). 3rd seed for variance estimation. r1: rel_f1=0.4449, s44: rel_f1=0.4655. Pass: rel_f1 > 0.4057, evi_f1 > 0.798.
806	  Created:    2026-05-15T11:25:26.268Z
807	  Updated:    2026-05-15T11:29:11.205Z
808	
809	### mvp2_eval_rsft_s43_r2
810	  Category:   eval
811	  Status:     DONE
812	  Conclusion: success
813	  Parent:     mvp2_rsft_train_r1_s43
814	  ign_f1:     0.4683
815	  rel_f1: 0.4683
816	  evi_f1: 0.8156
817	  evi_f1_joint: 0.3711
818	  evi_f1_joint_P: 0.3747
819	  evi_f1_joint_R: 0.3675
820	  edcr: 0.6388
821	  precision: 0.4817
822	  recall: 0.4556
823	  evi_precision: 0.8142
824	  evi_recall: 0.817
825	  n_predictions: 14970
826	  n_truncated: 171
827	  format_ok_rate: 1
828	  inference_time_s: 6316.7
829	  sft_baseline_rel_f1: 0.4057
830	  sft_baseline_evi_f1: 0.7979
831	  delta_rel_f1: 0.0626
832	  delta_evi_f1: 0.0177
833	  delta_evi_f1_joint: 0.0594
834	  mvp2_pass: True
835	  Hypothesis: Full dev eval of RSFT s43 (seed=43). 3rd seed for variance estimation. r1: rel_f1=0.4449, s44: rel_f1=0.4655. Pass: rel_f1 > 0.4057, evi_f1 > 0.798. Retry of mvp2_eval_rsft_s43 (fixed arg names).
836	  Created:    2026-05-15T11:29:17.551Z
837	  Updated:    2026-05-15T13:54:26.023Z
838	
839	### mvp2_eval_rsft_s44
840	  Category:   eval
841	  Status:     DONE
842	  Conclusion: killed
843	  Parent:     mvp2_rsft_train_r1_s44
844	  Metrics:    (none)
845	  Hypothesis: Full dev eval of RSFT seed=44 checkpoint. First MVP-2 judgement data point. Pass: rel_f1 > 0.4057 AND evi_f1 > 0.798 (SFT baseline).
846	  Created:    2026-05-15T07:35:23.934Z
847	  Updated:    2026-05-15T22:06:28.059Z
848	
849	### mvp2_eval_sft_baseline
850	  Category:   eval
851	  Status:     DONE
852	  Conclusion: success
853	  Parent:     mvp2_sft_warmup
854	  rel_f1: 0.4057
855	  evi_f1: 0.7979
856	  evi_f1_joint: 0.3117
857	  evi_f1_joint_P: 0.3037
858	  evi_f1_joint_R: 0.32
859	  edcr: 0.7118
860	  pred_count: 12234
861	  gold_count: 12151
862	  format_ok_rate: 0.998
863	  format_compliance_rate: 0.998
864	  field_compliance_rate: 0.6264
865	  n_truncated: 367
866	  inference_time_seconds: 6138.5
867	  Hypothesis: SFT baseline eval using identical eval protocol as GRPO evals (eval_lr5e6_ckpt20.sh). Required for MVP-2 core comparison: CED_Evi-F1 − SFT_Evi-F1 ≥ 2pp. Prior SFT eval (r3) used different eval path; this ensures apple-to-apple comparison.
868	  Created:    2026-05-14T21:47:41.356Z
869	  Updated:    2026-05-15T13:27:26.236Z
870	
871	### mvp2_grpo_ced
872	  Category:   grpo
873	  Status:     DONE
874	  Conclusion: failed
875	  Parent:     (none)
876	  Metrics:    (none)
877	  Created:    2026-05-14T07:10:31.165Z
878	  Updated:    2026-05-14T08:00:02.874Z
879	
880	### mvp2_grpo_ced_kl001
881	  Category:   grpo
882	  Status:     DONE
883	  Conclusion: failed
884	  Parent:     (none)
885	  Metrics:    (none)
886	  Hypothesis: kl_coef=0.01 (vs r5 kl_coef=0.0) prevents CED mode collapse while keeping QLoRA 4-bit compatible — answers whether KL regularization is necessary
887	  Created:    2026-05-14T12:32:53.111Z
888	  Updated:    2026-05-14T15:33:06.208Z
889	
890	### mvp2_grpo_ced_kl001_r2
891	  Category:   grpo
892	  Status:     DONE
893	  Conclusion: killed
894	  Parent:     mvp2_grpo_ced_kl001
895	  Metrics:    (none)
896	  Hypothesis: kl_coef=0.01 (vs r5 kl_coef=0.0) prevents CED mode collapse while keeping QLoRA 4-bit compatible — answers whether KL regularization is necessary (retry: fix --lr → --learning_rate)
897	  Created:    2026-05-14T15:23:16.518Z
898	  Updated:    2026-05-15T12:09:19.263Z
899	
900	### mvp2_grpo_ced_kl001_r3
901	  Category:   grpo
902	  Status:     DONE
903	  Conclusion: killed
904	  Parent:     mvp2_grpo_ced_kl001
905	  Metrics:    (none)
906	  Hypothesis: kl_coef=0.01 (vs r5 kl_coef=0.0) prevents CED mode collapse while keeping QLoRA 4-bit compatible — answers whether KL regularization is necessary (retry: fix --lr + bash -c wrapping)
907	  Created:    2026-05-14T15:25:06.729Z
908	  Updated:    2026-05-15T12:09:20.252Z
909	
910	### mvp2_grpo_ced_kl001_r4
911	  Category:   grpo
912	  Status:     DONE
913	  Conclusion: success
914	  Parent:     (none)
915	  final_step: 100
916	  train_runtime_s: 9069.88
917	  reward_final: 1.195
918	  f1_reward_final: 0.573
919	  ced_reward_final: 0.328
920	  format_reward_final: 0.293
921	  frac_zero_std_final: 0.2
922	  kl_final: 0.118
923	  loss_final: -0.009
924	  grad_norm_final: 0.14
925	  entropy_final: 0.067
926	  completion_length_mean_final: 520.8
927	  best_reward_step: 90
928	  best_reward: 1.37
929	  best_f1_reward: 0.72
930	  best_ced_reward: 0.353
931	  Created:    2026-05-14T15:32:32.529Z
932	  Updated:    2026-05-14T18:11:53.975Z
933	
934	### mvp2_grpo_ced_lr5e6_p1_r1
935	  Category:   grpo
936	  Status:     DONE
937	  Conclusion: killed
938	  Parent:     (none)
939	  Metrics:    (none)
940	  Hypothesis: D031/P0+P1: lr=5e-6 + --ced_recall_penalty fixes both catastrophic forgetting (lr) and CED recall shortcut (penalty). Pass criteria: ckpt-20 rel_f1 > 0.30 AND pred_count >= 15000 (SFT 80%). Comparing vs P0 isolates CED shortcut fix contribution.
941	  Created:    2026-05-14T19:28:59.245Z
942	  Updated:    2026-05-14T20:31:06.969Z
943	
944	### mvp2_grpo_ced_lr5e6_r1
945	  Category:   grpo
946	  Status:     DONE
947	  Conclusion: killed
948	  Parent:     mvp2_grpo_ced_kl001_r4
949	  Metrics:    (none)
950	  Hypothesis: D030/P0: lr=5e-6 (10x lower than ced_kl001_r4) prevents catastrophic forgetting while maintaining CED reward improvement. Community consensus GRPO+QLoRA lr=5e-6~1e-5. Pass criteria: ckpt-20 rel_f1 > 0.30. Extra monitoring: pred_count + recall trend.
951	  Created:    2026-05-14T19:21:08.231Z
952	  Updated:    2026-05-15T01:29:06.862Z
953	
954	### mvp2_grpo_ced_lr5e6_rp_r1
955	  Category:   grpo
956	  Status:     DONE
957	  Conclusion: failed
958	  Parent:     mvp2_grpo_ced_kl001_r4
959	  Metrics:    (none)
960	  Hypothesis: D032/P0+P1: lr=5e-6 + --ced_recall_penalty fixes both catastrophic forgetting (lr) and CED recall shortcut (penalty). Pass criteria: ckpt-20 rel_f1 > 0.30 AND pred_count >= 9720 (SFT 80%). Comparing vs P0 isolates CED shortcut fix contribution.
961	  Created:    2026-05-14T19:44:15.272Z
962	  Updated:    2026-05-14T20:44:07.125Z
963	
964	### mvp2_grpo_ced_lr5e6_rp_r2
965	  Category:   grpo
966	  Status:     DONE
967	  Conclusion: killed
968	  Parent:     mvp2_grpo_ced_kl001_r4
969	  Metrics:    (none)
970	  Hypothesis: D032/P0+P1 retry: lr=5e-6 + --ced_recall_penalty fixes both catastrophic forgetting (lr) and CED recall shortcut (penalty). Pass criteria: ckpt-20 rel_f1 > 0.30 AND pred_count >= 9720 (SFT 80%). Comparing vs P0 (lr5e6_r1) isolates CED shortcut fix contribution. Retry of rp_r1 which failed due to bas...
971	  Created:    2026-05-14T20:04:55.831Z
972	  Updated:    2026-05-14T21:40:50.174Z
973	
974	### mvp2_grpo_ced_r1
975	  Category:   grpo
976	  Status:     DONE
977	  Conclusion: killed
978	  Parent:     (none)
979	  Metrics:    (none)
980	  Created:    2026-05-14T08:02:41.858Z
981	  Updated:    2026-05-14T10:37:23.856Z
982	
983	### mvp2_grpo_ced_r2
984	  Category:   grpo
985	  Status:     DONE
986	  Conclusion: killed
987	  Parent:     (none)
988	  Metrics:    (none)
989	  Created:    2026-05-14T10:58:11.663Z
990	  Updated:    2026-05-14T11:31:49.724Z
991	
992	### mvp2_grpo_ced_r3
993	  Category:   grpo
994	  Status:     DONE
995	  Conclusion: failed
996	  Parent:     (none)
997	  Metrics:    (none)
998	  Hypothesis: CED reward with balanced weights (format×0.3, f1×3.0, ced×1.0) + stable training (num_iterations=1, KL early stop at 100) + kl_coef=0.05 improves Evi-F1 over SFT baseline
999	  Created:    2026-05-14T11:47:53.099Z
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01SfhnwAfu5FGq4CJbNHa37Q",
  "session_id": "bc5f4965-b9c9-4c46-9109-14848d79f92e",
  "uuid": "7253401b-a142-4d65-a42f-0c05d35af87f"
}
```

</details>

---

### System

_source line 43_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a01ea92613c0e609d",
  "tool_use_id": "toolu_01SfhnwAfu5FGq4CJbNHa37Q",
  "description": "Reading ~/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/bc5f4965-b9c9-4c46-9109-14848d79f92e/tool-results/bzi6o1ptf.txt",
  "usage": {
    "total_tokens": 39250,
    "tool_uses": 9,
    "duration_ms": 60006
  },
  "last_tool_name": "Read",
  "uuid": "3f592262-7609-4b27-834b-5c8954e371c6",
  "session_id": "bc5f4965-b9c9-4c46-9109-14848d79f92e"
}
```

---

### Tool call

_source line 44_

<details open><summary>🔧 Tool call — Read · `toolu_01MrucPfE2sGtt9RJmnfng5Q`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/bc5f4965-b9c9-4c46-9109-14848d79f92e/tool-results/bzi6o1ptf.txt",
  "offset": 999,
  "limit": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01SfhnwAfu5FGq4CJbNHa37Q",
  "session_id": "bc5f4965-b9c9-4c46-9109-14848d79f92e",
  "uuid": "6563a3c2-9050-4aab-9852-59cc62f04bb8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DKeULxN49H6WY1aspA4WqT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9236,
      "cache_read_input_tokens": 29538,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9236,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
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

_source line 45 · 2026-05-19T12:41:11.313Z_

<details><summary>↩ Tool result · `toolu_01MrucPfE2sGtt9RJmnfng5Q`</summary>

```text
999	  Created:    2026-05-14T11:47:53.099Z
1000	  Updated:    2026-05-14T12:09:23.005Z
1001	
1002	### mvp2_grpo_ced_r4
1003	  Category:   grpo
1004	  Status:     DONE
1005	  Conclusion: killed
1006	  Parent:     (none)
1007	  Metrics:    (none)
1008	  Created:    2026-05-14T12:10:15.698Z
1009	  Updated:    2026-05-14T12:30:06.177Z
1010	
1011	### mvp2_grpo_ced_r5
1012	  Category:   grpo
1013	  Status:     DONE
1014	  Conclusion: negative
1015	  Parent:     (none)
1016	  Metrics:    (none)
1017	  Created:    2026-05-14T12:31:45.606Z
1018	  Updated:    2026-05-14T15:32:21.817Z
1019	
1020	### mvp2_grpo_extract
1021	  Category:   grpo
1022	  Status:     DONE
1023	  Conclusion: failed
1024	  Parent:     (none)
1025	  Metrics:    (none)
1026	  Hypothesis: Extraction-only reward (format+F1, no CED) establishes GRPO baseline — CED r3 should exceed this on Evi-F1
1027	  Created:    2026-05-14T07:10:35.796Z
1028	  Updated:    2026-05-14T12:25:32.094Z
1029	
1030	### mvp2_grpo_extract_r2
1031	  Category:   grpo
1032	  Status:     DONE
1033	  Conclusion: killed
1034	  Parent:     (none)
1035	  Metrics:    (none)
1036	  Created:    2026-05-14T12:10:19.532Z
1037	  Updated:    2026-05-14T12:30:08.099Z
1038	
1039	### mvp2_grpo_extract_r3
1040	  Category:   grpo
1041	  Status:     DONE
1042	  Conclusion: negative
1043	  Parent:     (none)
1044	  Metrics:    (none)
1045	  Created:    2026-05-14T12:31:48.781Z
1046	  Updated:    2026-05-14T16:59:20.304Z
1047	
1048	### mvp2_grpo_extract_r4
1049	  Category:   grpo
1050	  Status:     DONE
1051	  Conclusion: killed
1052	  Parent:     mvp2_grpo_extract_r3
1053	  Metrics:    (none)
1054	  Hypothesis: Extraction-only reward (format×0.3, f1×3.0, ced=0) with kl_coef=0.01 + num_generations=8 trains stably. 100-step probe parallel ablation with ced_kl001_r4 (CED reward) to compare reward type impact under identical stability config.
1055	  Created:    2026-05-14T16:54:59.403Z
1056	  Updated:    2026-05-14T17:40:25.731Z
1057	
1058	### mvp2_grpo_flatnli
1059	  Category:   grpo
1060	  Status:     DONE
1061	  Conclusion: failed
1062	  Parent:     (none)
1063	  Metrics:    (none)
1064	  Hypothesis: Flat-NLI reward (non-contrastive) improves Evi-F1 over extraction-only but less than CED — validates contrastive component's incremental value
1065	  Created:    2026-05-14T07:10:33.848Z
1066	  Updated:    2026-05-14T12:13:34.747Z
1067	
1068	### mvp2_grpo_flatnli_r2
1069	  Category:   grpo
1070	  Status:     DONE
1071	  Conclusion: killed
1072	  Parent:     (none)
1073	  Metrics:    (none)
1074	  Created:    2026-05-14T12:10:23.287Z
1075	  Updated:    2026-05-14T12:30:08.865Z
1076	
1077	### mvp2_grpo_flatnli_r3
1078	  Category:   grpo
1079	  Status:     DONE
1080	  Conclusion: killed
1081	  Parent:     (none)
1082	  Metrics:    (none)
1083	  Created:    2026-05-14T12:31:52.782Z
1084	  Updated:    2026-05-14T15:27:55.267Z
1085	
1086	### mvp2_grpo_flatnli_r4
1087	  Category:   grpo
1088	  Status:     DONE
1089	  Conclusion: killed
1090	  Parent:     (none)
1091	  Metrics:    (none)
1092	  Created:    2026-05-14T15:32:31.804Z
1093	  Updated:    2026-05-14T16:56:12.080Z
1094	
1095	### mvp2_grpo_flatnli_r5
1096	  Category:   grpo
1097	  Status:     DONE
1098	  Conclusion: killed
1099	  Parent:     mvp2_grpo_flatnli_r4
1100	  Metrics:    (none)
1101	  Hypothesis: Flat-NLI reward with kl_coef=0.01 + num_generations=8 prevents mode collapse. Resume from flatnli_r3 checkpoint-100 (healthy). 100-step probe (steps 100→200) to verify stability before full run.
1102	  Created:    2026-05-14T16:55:02.197Z
1103	  Updated:    2026-05-14T17:26:55.692Z
1104	
1105	### mvp2_grpo_flatnli_r6
1106	  Category:   grpo
1107	  Status:     DONE
1108	  Conclusion: negative
1109	  Parent:     mvp2_grpo_flatnli_r5
1110	  steps_completed: 25
1111	  final_frac_zero_std: 0.9
1112	  final_f1_reward: 0
1113	  final_flat_nli_reward: 0
1114	  final_format_reward: 0.293
1115	  collapse_step: 25
1116	  Hypothesis: Flat-NLI reward with kl_coef=0.01 + num_generations=8 from SFT scratch (not resume). 100-step probe to verify stability. Same D020 config as ced_kl001_r4 (which is healthy). Tests whether flat-NLI reward type works under stable training config.
1117	  Created:    2026-05-14T17:25:07.083Z
1118	  Updated:    2026-05-14T18:17:52.909Z
1119	
1120	### mvp2_sft_eval
1121	  Category:   eval
1122	  Status:     DONE
1123	  Conclusion: killed
1124	  Parent:     (none)
1125	  Metrics:    (none)
1126	  Created:    2026-05-14T07:10:37.449Z
1127	  Updated:    2026-05-14T12:46:04.523Z
1128	
1129	### mvp2_sft_eval_r2
1130	  Category:   eval
1131	  Status:     DONE
1132	  Conclusion: success
1133	  Parent:     (none)
1134	  ign_f1:     0.4057
1135	  rel_f1: 0.4057
1136	  evi_f1: 0.7979
1137	  edcr: 0.7118
1138	  precision: 0.4043
1139	  recall: 0.407
1140	  evi_precision: 0.8035
1141	  evi_recall: 0.7924
1142	  format_ok_rate: 0.998
1143	  format_compliance_rate: 0.626
1144	  n_parseable: 617
1145	  n_truncated: 367
1146	  n_predictions: 18815
1147	  inference_time_seconds: 6484.7
1148	  Created:    2026-05-14T12:45:46.160Z
1149	  Updated:    2026-05-14T14:54:07.338Z
1150	
1151	### mvp2_sft_eval_r3
1152	  Category:   eval
1153	  Status:     DONE
1154	  Conclusion: success
1155	  Parent:     (none)
1156	  ign_f1:     0.4057
1157	  rel_f1: 0.4057
1158	  evi_f1: 0.7979
1159	  edcr: 0.7118
1160	  precision: 0.4043
1161	  recall: 0.407
1162	  evi_precision: 0.8035
1163	  evi_recall: 0.7924
1164	  format_ok_rate: 0.998
1165	  format_compliance_rate: 0.626
1166	  n_parseable: 617
1167	  n_truncated: 367
1168	  n_predictions: 18815
1169	  Created:    2026-05-14T13:52:38.174Z
1170	  Updated:    2026-05-14T17:06:57.010Z
1171	
1172	### plan006_1_7b_rsft_eval
1173	  Category:   eval
1174	  Status:     DONE
1175	  Conclusion: killed
1176	  Parent:     (none)
1177	  Metrics:    (none)
1178	  Created:    2026-05-17T06:10:39.978Z
1179	  Updated:    2026-05-17T23:18:35.353Z
1180	
1181	### plan017_14b_sft_eval
1182	  Category:   eval
1183	  Status:     DONE
1184	  Conclusion: killed
1185	  Parent:     plan017_14b_sft
1186	  Metrics:    (none)
1187	  Hypothesis: D076 eval for 14B SFT baseline. 14B 是第 4 个 scale 档（1.7B/4B/8B/14B），SFT baseline 用于计算 RSFT 增益和 evidence tax。预期 ign_f1 高于 8B SFT mean (0.4866)。
1188	  Created:    2026-05-19T07:23:43.367Z
1189	  Updated:    2026-05-19T08:54:24.083Z
1190	
1191	### plan017_14b_sft_no_evidence_eval
1192	  Category:   eval, no_evidence
1193	  Status:     DONE
1194	  Conclusion: killed
1195	  Parent:     plan017_14b_sft
1196	  Metrics:    (none)
1197	  Hypothesis: 14B SFT no-evidence eval: 测量 14B SFT 在不提供 evidence 时的 ign_f1，用于计算 evidence tax (Claim 3)。与 4B evidence tax (D107: 47.21% vs 39.74%) 对比，验证 scale-dependent evidence tax 趋势。
1198	  Created:    2026-05-19T07:23:46.290Z
1199	  Updated:    2026-05-19T08:49:48.692Z
1200	
1201	### plan019_1_7b_rsft_s43_r2_eval
1202	  Category:   eval
1203	  Status:     DONE
1204	  Conclusion: success
1205	  Parent:     plan019_1_7b_rsft_s43_r2
1206	  ign_f1:     0.5109
1207	  ign_precision: 0.5186
1208	  ign_recall: 0.5035
1209	  f1: 0.5271
1210	  precision: 0.5444
1211	  recall: 0.5109
1212	  evi_precision: 0.8218
1213	  evi_recall: 0.834
1214	  evi_f1: 0.8278
1215	  edcr: 0.6245
1216	  evi_joint_precision: 0.4336
1217	  evi_joint_recall: 0.4221
1218	  evi_f1_joint: 0.4278
1219	  format_compliance_rate: 0.999
1220	  field_compliance_rate: 0.7503
1221	  n_truncated: 244
1222	  inference_time_seconds: 8498.2
1223	  Hypothesis: D076 eval for 1.7B RSFT s43_r2 (Method A: s42 SFT adapter + s42 CED k=1 data, RSFT seed=43). 预期 ign_f1 接近 s42 RSFT (0.5122)，验证 1.7B RSFT 跨 seed 稳健性。
1224	  Created:    2026-05-19T06:15:45.750Z
1225	  Updated:    2026-05-19T08:42:24.182Z
1226	
1227	### plan019_1_7b_rsft_s44_r2_eval
1228	  Category:   eval
1229	  Status:     DONE
1230	  Conclusion: success
1231	  Parent:     plan019_1_7b_rsft_s44_r2
1232	  ign_f1:     0.5125
1233	  ign_precision: 0.5173
1234	  ign_recall: 0.5078
1235	  f1: 0.5294
1236	  precision: 0.5434
1237	  recall: 0.5162
1238	  evi_precision: 0.815
1239	  evi_recall: 0.8387
1240	  evi_f1: 0.8267
1241	  edcr: 0.6181
1242	  evi_joint_precision: 0.4284
1243	  evi_joint_recall: 0.4294
1244	  evi_f1_joint: 0.4289
1245	  format_compliance_rate: 0.999
1246	  field_compliance_rate: 0.7543
1247	  n_truncated: 240
1248	  inference_time_seconds: 8615.6
1249	  Hypothesis: D076 eval for 1.7B RSFT s44_r2 (Method A: s42 SFT adapter + s42 CED k=1 data, RSFT seed=44). 预期 ign_f1 接近 s42 (0.5122) 和 s43 (0.5109)，完成 1.7B 3-seed RSFT 统计。
1250	  Created:    2026-05-19T08:43:01.975Z
1251	  Updated:    2026-05-19T12:00:32.897Z
1252	
1253	### plan019_1_7b_sft_s43_eval
1254	  Category:   eval
1255	  Status:     DONE
1256	  Conclusion: success
1257	  Parent:     plan019_1_7b_sft_s43
1258	  ign_f1:     0.4286
1259	  f1: 0.4372
1260	  ign_precision: 0.4475
1261	  ign_recall: 0.4111
1262	  precision: 0.4704
1263	  recall: 0.4084
1264	  evi_f1: 0.835
1265	  evi_f1_joint: 0.3442
1266	  edcr: 0.704
1267	  format_compliance: 1
1268	  field_compliance: 0.5858
1269	  n_total: 985
1270	  n_predictions: 18140
1271	  n_truncated: 408
1272	  inference_time_seconds: 5257.4
1273	  Hypothesis: Eval 1.7B SFT seed43 on DocRED dev set to measure RE performance. Paired with s42 for 2-seed mean±std at 1.7B scale.
1274	  Created:    2026-05-18T20:33:55.681Z
1275	  Updated:    2026-05-18T22:03:20.771Z
1276	
1277	### plan019_1_7b_sft_s44_eval
1278	  Category:   eval
1279	  Status:     DONE
1280	  Conclusion: success
1281	  Parent:     plan019_1_7b_sft_s44
1282	  ign_f1:     0.4321
1283	  f1: 0.4441
1284	  evi_f1_tp: 0.819
1285	  evi_f1_joint: 0.3482
1286	  edcr: 0.69
1287	  n_truncated: 473
1288	  n_predictions: 20237
1289	  n_documents: 985
1290	  format_ok_rate: 1
1291	  field_compliance_rate: 0.5198
1292	  evidence_format_rate: 0.5198
1293	  inference_time_seconds: 6146
1294	  Hypothesis: 1.7B SFT seed44 eval (D076 protocol): measure baseline SFT performance for seed44 at 1.7B scale. Paired with canonical s42 for scaling seed robustness. Expected rel_f1 ~49.5 based on canonical 1.7B SFT.
1295	  Created:    2026-05-18T16:34:45.563Z
1296	  Updated:    2026-05-18T19:27:55.325Z
1297	
1298	### plan019_8b_rsft_s44_eval
1299	  Category:   eval
1300	  Status:     DONE
1301	  Conclusion: success
1302	  Parent:     plan019_8b_rsft_s44
1303	  ign_f1:     0.5451
1304	  f1: 0.562
1305	  evi_f1_tp: 0.8145
1306	  evi_f1_dreeam: 0.4472
1307	  edcr: 0.6233
1308	  format_ok: 985/985
1309	  truncated: 230/985
1310	  predictions: 16254
1311	  Hypothesis: 8B RSFT s44 eval (Option A seed expansion). 预期 ign_f1 接近 canonical s42 (0.5376)，验证 RSFT 增益在 8B 尺度跨 seed 稳定。
1312	  Created:    2026-05-19T02:11:06.132Z
1313	  Updated:    2026-05-19T05:08:07.693Z
1314	
1315	### plan019_8b_sft_s44_eval
1316	  Category:   eval
1317	  Status:     DONE
1318	  Conclusion: success
1319	  Parent:     plan019_8b_sft_s44
1320	  ign_f1:     0.4681
1321	  f1: 0.4841
1322	  evi_f1: 0.8361
1323	  evi_f1_joint: 0.3839
1324	  edcr: 0.6697
1325	  format_ok_rate: 1
1326	  n_truncated: 306
1327	  n_predictions: 16690
1328	  inference_time_seconds: 6951.1
1329	  Hypothesis: 8B SFT s44 eval (D076 protocol): measure SFT baseline for seed44 at 8B scale. Paired with canonical s42 (ign_f1=0.5051) for 2-seed mean±std.
1330	  Created:    2026-05-18T21:36:26.622Z
1331	  Updated:    2026-05-18T23:44:30.382Z
1332	
1333	### plan_002_test_eval_s44
1334	  Category:   eval
1335	  Status:     DONE
1336	  Conclusion: failed
1337	  Parent:     (none)
1338	  Metrics:    (none)
1339	  Created:    2026-05-15T18:05:47.701Z
1340	  Updated:    2026-05-15T18:20:17.405Z
1341	
1342	### plan_002_test_eval_s44_r2
1343	  Category:   eval
1344	  Status:     DONE
1345	  Conclusion: success
1346	  Parent:     (none)
1347	  Metrics:    (none)
1348	  Hypothesis: DocRED test set evaluation for RSFT-CED s44 (best dev config). Final benchmark numbers for paper submission; test set performance confirms dev set gains are not overfitting artifacts.
1349	  Created:    2026-05-16T08:14:36.494Z
1350	  Updated:    2026-05-17T02:56:29.283Z
1351	
1352	### plan_006_llama_rsft_r3_eval
1353	  Category:   eval
1354	  Status:     DONE
1355	  Conclusion: success
1356	  Parent:     (none)
1357	  ign_f1:     0.5563
1358	  f1: 0.5674
1359	  evi_f1: 0.8255
1360	  edcr: 0.5856
1361	  evi_f1_joint: 0.4571
1362	  format_compliance_rate: 0.997
1363	  field_compliance_rate: 0.807
1364	  n_truncated: 187
1365	  inference_time_seconds: 8650
1366	  Hypothesis: Evaluate LLaMA-3.1-8B RSFT r3 (checkpoint-3312, final) on DocRED dev. Cross-architecture validation: if CED-RSFT works on both Qwen and LLaMA, the method is architecture-agnostic.
1367	  Created:    2026-05-17T08:35:48.098Z
1368	  Updated:    2026-05-17T23:17:59.347Z
1369	
1370	### plan_006_llama_rsft_seed43_eval
1371	  Category:   eval
1372	  Status:     DONE
1373	  Conclusion: failed
1374	  Parent:     plan_006_llama_rsft_seed43
1375	  Metrics:    (none)
1376	  Hypothesis: Evaluate LLaMA-8B RSFT seed 43 on DocRED dev. Seed 42 gave rel_f1=0.5674. If seed 43 gives similar result (±1.5pp, i.e., 0.55-0.58), the cross-architecture RSFT claim is robust against seed variance.
1377	  Created:    2026-05-17T16:00:04.294Z
1378	  Updated:    2026-05-17T16:48:26.809Z
1379	
1380	### plan_006_llama_rsft_seed43_eval_r2
1381	  Category:   eval
1382	  Status:     DONE
1383	  Conclusion: success
1384	  Parent:     plan_006_llama_rsft_seed43
1385	  ign_f1:     0.5619
1386	  rel_f1: 0.5727
1387	  evi_f1: 0.8206
1388	  evi_f1_joint: 0.4551
1389	  edcr: 0.6073
1390	  format_compliance_rate: 1
1391	  n_truncated: 197
1392	  Hypothesis: Evaluate LLaMA-8B RSFT seed 43 on DocRED dev (retry with correct base_model path). Seed 42 gave rel_f1=0.5674. If seed 43 gives similar result (±1.5pp), the cross-architecture RSFT claim is robust against seed variance.
1393	  Created:    2026-05-17T16:03:41.592Z
1394	  Updated:    2026-05-17T18:48:55.143Z
1395	
1396	### plan_006_qwen3_1_7b_no_evidence_eval
1397	  Category:   eval, no_evidence
1398	  Status:     DONE
1399	  Conclusion: failed
1400	  Parent:     (none)
1401	  ign_f1:     0.3786
1402	  f1: 0.3884
1403	  evi_f1: 0.0007
1404	  edcr: 0.9848
1405	  precision: 0.4282
1406	  recall: 0.3553
1407	  pred_count: 27049
1408	  n_truncated: 531
1409	  format_ok_rate: 0.999
1410	  Created:    2026-05-16T09:25:53.604Z
1411	  Updated:    2026-05-16T11:17:18.299Z
1412	
1413	### plan_006_qwen3_1_7b_no_evidence_eval_v2
1414	  Category:   eval, no_evidence
1415	  Status:     DONE
1416	  Conclusion: failed
1417	  Parent:     (none)
1418	  Metrics:    (none)
1419	  Created:    2026-05-16T11:40:29.706Z
1420	  Updated:    2026-05-16T11:44:58.762Z
1421	
1422	### plan_006_qwen3_1_7b_no_evidence_eval_v2r2
1423	  Category:   eval, no_evidence
1424	  Status:     DONE
1425	  Conclusion: failed
1426	  Parent:     (none)
1427	  Metrics:    (none)
1428	  Created:    2026-05-16T12:02:28.162Z
1429	  Updated:    2026-05-16T12:28:44.616Z
1430	
1431	### plan_006_qwen3_1_7b_no_evidence_eval_v3
1432	  Category:   eval, no_evidence
1433	  Status:     DONE
1434	  Conclusion: success
1435	  Parent:     plan_006_qwen3_1_7b_no_evidence_sft
1436	  ign_f1:     0.3982
1437	  rel_f1: 0.4103
1438	  evi_f1: 0
1439	  edcr: 0
1440	  precision: 0.4464
1441	  recall: 0.3796
1442	  format_compliance_rate: 1
1443	  n_truncated: 501
1444	  inference_time_seconds: 7465.3
1445	  evidence_tax: 0.0804
1446	  Hypothesis: 1.7B model capacity is insufficient to jointly optimize RE and evidence generation: no-evidence SFT should outperform evidence-SFT on rel_f1, revealing positive evidence tax at small scale (opposite to 8B where tax≈0).
1447	  Created:    2026-05-16T11:45:02.749Z
1448	  Updated:    2026-05-17T02:55:24.084Z
1449	
1450	### plan_006_qwen3_1_7b_no_evidence_sft
1451	  Category:   no_evidence
1452	  Status:     DONE
1453	  Conclusion: success
1454	  Parent:     (none)
1455	  Metrics:    (none)
1456	  Hypothesis: Qwen3-1.7B no-evidence SFT baseline for evidence tax measurement at 1.7B scale. Paired with evidence-SFT to quantify whether evidence generation constrains or helps small model RE performance.
1457	  Created:    2026-05-16T07:32:23.806Z
1458	  Updated:    2026-05-17T02:56:15.512Z
1459	
1460	### plan_006_qwen3_1_7b_rsft_eval
1461	  Category:   eval
1462	  Status:     DONE
1463	  Conclusion: failed
1464	  Parent:     plan_006_qwen3_1_7b_rsft_train
1465	  Metrics:    (none)
1466	  Hypothesis: Evaluate 1.7B RSFT model on DocRED dev to measure rel_f1 improvement over SFT baseline. Validates that CED-filtered RSFT generalizes to smallest model scale (1.7B) in the scaling study.
1467	  Created:    2026-05-17T06:12:11.998Z
1468	  Updated:    2026-05-17T08:25:24.429Z
1469	
1470	### plan_006_qwen3_1_7b_rsft_eval_r2
1471	  Category:   eval
1472	  Status:     DONE
1473	  Conclusion: success
1474	  Parent:     plan_006_qwen3_1_7b_rsft_train
1475	  ign_f1:     0.505
1476	  f1: 0.5219
1477	  evi_f1: 0.8309
1478	  edcr: 0.6297
1479	  evi_f1_joint: 0.4223
1480	  format_compliance_rate: 0.999
1481	  field_compliance_rate: 0.732
1482	  n_truncated: 258
1483	  inference_time_seconds: 9464
1484	  Hypothesis: Evaluate 1.7B RSFT model (checkpoint-1698) on DocRED dev. Retry after disk-full crash. Validates CED-filtered RSFT at smallest model scale in scaling study.
1485	  Created:    2026-05-17T08:35:45.455Z
1486	  Updated:    2026-05-17T23:18:01.212Z
1487	
1488	### plan_006_qwen3_1_7b_rsft_seed43_eval
1489	  Category:   eval
1490	  Status:     DONE
1491	  Conclusion: success
1492	  Parent:     plan_006_qwen3_1_7b_rsft_seed43
1493	  ign_f1:     0.5024
1494	  f1: 0.518
1495	  evi_f1_joint: 0.4201
1496	  evi_f1_tp: 0.8341
1497	  edcr: 0.6246
1498	  precision: 0.535
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01SfhnwAfu5FGq4CJbNHa37Q",
  "session_id": "bc5f4965-b9c9-4c46-9109-14848d79f92e",
  "uuid": "6db2f92d-7a51-4513-b07d-06259cbac95a"
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
  "task_id": "a01ea92613c0e609d",
  "tool_use_id": "toolu_01SfhnwAfu5FGq4CJbNHa37Q",
  "description": "Reading ~/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/bc5f4965-b9c9-4c46-9109-14848d79f92e/tool-results/bzi6o1ptf.txt",
  "usage": {
    "total_tokens": 47911,
    "tool_uses": 10,
    "duration_ms": 65373
  },
  "last_tool_name": "Read",
  "uuid": "69595418-30d5-448d-b54a-8b26fe91fdac",
  "session_id": "bc5f4965-b9c9-4c46-9109-14848d79f92e"
}
```

---

### Tool call

_source line 47_

<details open><summary>🔧 Tool call — Read · `toolu_01PKrYcsZ5nrqFTxLGJhBwF5`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/bc5f4965-b9c9-4c46-9109-14848d79f92e/tool-results/bzi6o1ptf.txt",
  "offset": 1490,
  "limit": 600
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01SfhnwAfu5FGq4CJbNHa37Q",
  "session_id": "bc5f4965-b9c9-4c46-9109-14848d79f92e",
  "uuid": "19574c01-8ebb-4fd7-b6e2-a410b9c06595",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VQ4KqP8KvV1fZjRkJk6AzC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8623,
      "cache_read_input_tokens": 38774,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8623,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
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

_source line 48 · 2026-05-19T12:41:16.683Z_

<details><summary>↩ Tool result · `toolu_01PKrYcsZ5nrqFTxLGJhBwF5`</summary>

```text
1490	  Status:     DONE
1491	  Conclusion: success
1492	  Parent:     plan_006_qwen3_1_7b_rsft_seed43
1493	  ign_f1:     0.5024
1494	  f1: 0.518
1495	  evi_f1_joint: 0.4201
1496	  evi_f1_tp: 0.8341
1497	  edcr: 0.6246
1498	  precision: 0.535
1499	  recall: 0.5019
1500	  ign_precision: 0.5099
1501	  ign_recall: 0.4951
1502	  format_ok: 984/985
1503	  n_truncated: 262
1504	  n_predictions: 16455
1505	  Hypothesis: Evaluate 1.7B RSFT seed 43 on DocRED dev. Seed 42 gave rel_f1=0.5219. If seed 43 gives similar result (±1pp, i.e., 0.51-0.53), the 1.7B scaling study datapoint is robust.
1506	  Created:    2026-05-17T14:26:15.446Z
1507	  Updated:    2026-05-17T19:56:30.167Z
1508	
1509	### plan_006_qwen3_1_7b_sft_eval
1510	  Category:   eval
1511	  Status:     DONE
1512	  Conclusion: success
1513	  Parent:     plan_006_qwen3_1_7b_sft_bf16
1514	  ign_f1:     0.4786
1515	  f1: 0.4945
1516	  evi_f1: 0.8316
1517	  edcr: 0.6704
1518	  precision: 0.5085
1519	  recall: 0.4813
1520	  ign_precision: 0.483
1521	  ign_recall: 0.4743
1522	  evi_precision: 0.8203
1523	  evi_recall: 0.8432
1524	  evi_f1_joint: 0.3958
1525	  format_compliance_rate: 1
1526	  n_predictions: 17184
1527	  n_truncated: 314
1528	  inference_time_seconds: 6848.7
1529	  Hypothesis: Qwen3-1.7B evidence-SFT eval under D076 protocol. Establishes smallest-scale SFT baseline; evidence tax at 1.7B predicted negative (evidence helps small models by constraining over-prediction).
1530	  Created:    2026-05-16T08:14:26.923Z
1531	  Updated:    2026-05-17T02:56:02.886Z
1532	
1533	### plan_006_qwen3_8b_no_evidence_eval
1534	  Category:   eval, no_evidence
1535	  Status:     DONE
1536	  Conclusion: killed
1537	  Parent:     (none)
1538	  Metrics:    (none)
1539	  Created:    2026-05-16T11:12:04.565Z
1540	  Updated:    2026-05-16T11:16:54.766Z
1541	
1542	### plan_006_qwen3_8b_no_evidence_eval_v2
1543	  Category:   eval, no_evidence
1544	  Status:     DONE
1545	  Conclusion: success
1546	  Parent:     plan_006_qwen3_8b_no_evidence_sft
1547	  Metrics:    (none)
1548	  Hypothesis: 8B model capacity absorbs evidence generation cost: no-evidence SFT and evidence-SFT should produce near-identical rel_f1, demonstrating evidence tax≈0 at 8B scale (contrasting with 4B where tax=-7.5pp).
1549	  Created:    2026-05-16T11:17:39.361Z
1550	  Updated:    2026-05-17T02:55:34.661Z
1551	
1552	### plan_006_qwen3_8b_no_evidence_sft
1553	  Category:   no_evidence
1554	  Status:     DONE
1555	  Conclusion: success
1556	  Parent:     (none)
1557	  train_loss: 0.6509
1558	  eval_loss: 0.8153
1559	  eval_mean_token_accuracy: 0.8174
1560	  eval_entropy: 0.6275
1561	  train_runtime_sec: 3656
1562	  epoch: 3
1563	  Hypothesis: Qwen3-8B no-evidence SFT baseline for evidence tax measurement at 8B scale. If 8B no-evi rel_f1 ≈ 8B evidence-SFT rel_f1, confirms that 8B absorbs evidence cost (tax≈0).
1564	  Created:    2026-05-16T09:30:57.988Z
1565	  Updated:    2026-05-17T02:56:26.471Z
1566	
1567	### plan_006_qwen3_8b_rsft_eval
1568	  Category:   eval
1569	  Status:     DONE
1570	  Conclusion: success
1571	  Parent:     plan_006_qwen3_8b_rsft_train_r2
1572	  ign_f1:     0.5433
1573	  f1: 0.5606
1574	  evi_f1: 0.8052
1575	  evi_f1_joint: 0.4413
1576	  edcr: 0.6377
1577	  precision: 0.5553
1578	  recall: 0.566
1579	  format_ok: 985/985
1580	  truncated: 267/985
1581	  predictions: 16831
1582	  Hypothesis: Evaluate Qwen3-8B RSFT (CED-scored data, 9041 samples) on DocRED dev. At 8B scale with near-zero evidence tax, CED-RSFT should achieve highest absolute Ign-F1 in the scaling study.
1583	  Created:    2026-05-17T12:00:05.493Z
1584	  Updated:    2026-05-17T14:59:23.644Z
1585	
1586	### plan_006_qwen3_8b_sft_eval
1587	  Category:   eval
1588	  Status:     DONE
1589	  Conclusion: success
1590	  Parent:     plan_006_qwen3_8b_sft_bf16
1591	  ign_f1:     0.5051
1592	  f1: 0.5262
1593	  evi_f1: 0.8188
1594	  edcr: 0.651
1595	  format_ok_rate: 0.999
1596	  n_truncated: 313
1597	  n_predictions: 17401
1598	  inference_time_s: 7206
1599	  Hypothesis: Qwen3-8B evidence-SFT eval under D076 unified protocol. Establishes 8B-scale SFT baseline for evidence tax measurement (paired with no-evidence eval) and RSFT improvement quantification.
1600	  Created:    2026-05-16T09:03:35.743Z
1601	  Updated:    2026-05-17T02:56:01.221Z
1602	
1603	### plan_007_redocred_4b_sft_eval
1604	  Category:   eval
1605	  Status:     DONE
1606	  Conclusion: failed
1607	  Parent:     (none)
1608	  Metrics:    (none)
1609	  Created:    2026-05-16T12:30:55.473Z
1610	  Updated:    2026-05-16T12:34:54.050Z
1611	
1612	### plan_007_redocred_4b_sft_eval_r2
1613	  Category:   eval
1614	  Status:     DONE
1615	  Conclusion: success
1616	  Parent:     reeval_sft_baseline_d076
1617	  ign_f1:     0.3659
1618	  f1: 0.3706
1619	  evi_f1: 0.817
1620	  edcr: 0.6674
1621	  format_compliance_rate: 0.996
1622	  n_truncated: 139
1623	  n_total: 493
1624	  inference_time_seconds: 3281.7
1625	  precision: 0.4316
1626	  recall: 0.3247
1627	  ign_precision: 0.4134
1628	  ign_recall: 0.3282
1629	  evi_precision: 0.8208
1630	  evi_recall: 0.8131
1631	  n_predictions: 8191
1632	  Hypothesis: FREIGE SFT model trained on DocRED transfers to Re-DocRED without re-training: if Ign-F1 drop <5pp and Evi-F1 maintains, the learned evidence grounding generalizes across annotation schemes.
1633	  Created:    2026-05-16T12:36:01.717Z
1634	  Updated:    2026-05-17T02:55:43.842Z
1635	
1636	### plan_007_redocred_rsft_eval
1637	  Category:   eval
1638	  Status:     DONE
1639	  Conclusion: failed
1640	  Parent:     (none)
1641	  failure_reason: OOM + pipeline bug: --model_path and --sft_adapter args in wrong order. RSFT LoRA merged to bare Qwen3-4B without SFT base, causing ontology collapse. Fix: match DocRED eval param ordering.
1642	  Created:    2026-05-16T14:23:56.999Z
1643	  Updated:    2026-05-16T17:49:00.578Z
1644	
1645	### plan_007_redocred_rsft_eval_r2
1646	  Category:   eval
1647	  Status:     DONE
1648	  Conclusion: negative
1649	  Parent:     (none)
1650	  F1: 0.0025
1651	  Ign-F1: 0.0026
1652	  Evi-F1: 0.8837
1653	  EDCR: 0.9978
1654	  format_ok: 489/493
1655	  truncated: 117/493
1656	  predictions: 8461
1657	  Hypothesis: CED-RSFT improvements on DocRED should transfer to Re-DocRED: RSFT model should outperform SFT baseline on Re-DocRED Ign-F1, demonstrating cross-dataset generalization of rejection sampling gains.
1658	  Created:    2026-05-16T16:25:37.094Z
1659	  Updated:    2026-05-17T02:56:32.555Z
1660	
1661	### plan_007_redocred_rsft_eval_r3
1662	  Category:   eval
1663	  Status:     DONE
1664	  Conclusion: failed
1665	  Parent:     plan_007_redocred_4b_sft_eval_r2
1666	  Metrics:    (none)
1667	  Hypothesis: Re-DocRED RSFT eval r3 (config fix: model_path=base, sft_adapter=RSFT ckpt). Verify CED-RSFT gains transfer cross-dataset.
1668	  Created:    2026-05-16T17:38:09.825Z
1669	  Updated:    2026-05-16T21:07:14.348Z
1670	
1671	### plan_007_redocred_rsft_eval_r4
1672	  Category:   eval
1673	  Status:     DONE
1674	  Conclusion: failed
1675	  Parent:     plan_007_redocred_4b_sft_eval_r2
1676	  Metrics:    (none)
1677	  Hypothesis: CED-RSFT gains transfer to Re-DocRED (r4, correct 3-param loading: base→SFT→RSFT)
1678	  Created:    2026-05-16T18:00:41.999Z
1679	  Updated:    2026-05-16T22:04:01.953Z
1680	
1681	### plan_007_redocred_rsft_eval_r5
1682	  Category:   eval
1683	  Status:     DONE
1684	  Conclusion: success
1685	  Parent:     plan_007_redocred_rsft_eval_r4
1686	  ign_f1:     0.4145
1687	  f1: 0.4234
1688	  evi_f1: 0.8182
1689	  edcr: 0.621
1690	  evi_joint_f1: 0.3306
1691	  format_compliance: 1
1692	  field_compliance: 0.8134
1693	  n_documents: 493
1694	  n_truncated: 90
1695	  inference_time_s: 5655.5
1696	  Hypothesis: CED-RSFT gains transfer to Re-DocRED (r5, correct 3-param loading: base→SFT→RSFT)
1697	  Created:    2026-05-16T22:04:18.834Z
1698	  Updated:    2026-05-17T00:51:25.706Z
1699	
1700	### plan_009_extract_reward_eval
1701	  Category:   eval
1702	  Status:     DONE
1703	  Conclusion: failed
1704	  Parent:     (none)
1705	  Metrics:    (none)
1706	  Created:    2026-05-15T19:04:55.707Z
1707	  Updated:    2026-05-15T19:58:37.870Z
1708	
1709	### plan_009_flatnli_reward_eval
1710	  Category:   eval
1711	  Status:     DONE
1712	  Conclusion: failed
1713	  Parent:     (none)
1714	  Metrics:    (none)
1715	  Created:    2026-05-15T19:04:57.991Z
1716	  Updated:    2026-05-15T19:39:02.187Z
1717	
1718	### plan_009_flatnli_reward_eval_r2
1719	  Category:   eval
1720	  Status:     DONE
1721	  Conclusion: failed
1722	  Parent:     (none)
1723	  Metrics:    (none)
1724	  Created:    2026-05-15T19:54:58.033Z
1725	  Updated:    2026-05-15T20:32:33.464Z
1726	
1727	### plan_011_bf16_g8_step_eval
1728	  Category:   eval
1729	  Status:     DONE
1730	  Conclusion: success
1731	  Parent:     (none)
1732	  step_30: {'rel_f1': 0.434, 'evi_f1': 0.8063, 'edcr': 0.6807}
1733	  step_50: {'rel_f1': 0.4276, 'evi_f1': 0.8024, 'edcr': 0.6855}
1734	  step_70: {'rel_f1': 0.4341, 'evi_f1': 0.8099, 'edcr': 0.6685}
1735	  best_step: step_70
1736	  trend: non-monotonic, all < ckpt-100 (0.4549)
1737	  Created:    2026-05-15T19:04:51.538Z
1738	  Updated:    2026-05-15T23:01:09.970Z
1739	
1740	### plan_011_eval_g8_bf16_ckpt100
1741	  Category:   eval
1742	  Status:     DONE
1743	  Conclusion: killed
1744	  Parent:     (none)
1745	  Metrics:    (none)
1746	  Created:    2026-05-15T14:43:24.143Z
1747	  Updated:    2026-05-15T22:06:28.981Z
1748	
1749	### plan_011_grpo_g8_bf16
1750	  Category:   grpo
1751	  Status:     DONE
1752	  Conclusion: success
1753	  Parent:     (none)
1754	  final_step: 100
1755	  train_runtime_s: 554
1756	  reward_final: 1.795
1757	  f1_reward_final: 1.002
1758	  ced_reward_final: 0.494
1759	  format_reward_final: 0.3
1760	  frac_zero_std_final: 0
1761	  kl_final: 0.022
1762	  best_reward_step: 85
1763	  best_reward: 2.858
1764	  best_f1_reward: 1.85
1765	  mode_collapse: False
1766	  lora_config: r=64, alpha=128, dropout=0.05, bf16
1767	  checkpoints: 10 checkpoints (step 10-100)
1768	  Hypothesis: GRPO G=8 bf16 LoRA: 验证 catastrophic forgetting 是否在 bf16（非 QLoRA 4-bit）下仍复现。CED reward + kl_coef=0.01, 100 steps。如仍 fail → 加强 Claim 3
1769	  Created:    2026-05-15T13:59:50.014Z
1770	  Updated:    2026-05-15T15:55:53.725Z
1771	
1772	### plan_011_grpo_g8_bf16_eval
1773	  Category:   eval, grpo
1774	  Status:     DONE
1775	  Conclusion: success
1776	  Parent:     (none)
1777	  ign_f1:     0.4549
1778	  rel_f1: 0.4549
1779	  evi_f1: 0.8086
1780	  edcr: 0.6318
1781	  format_ok_rate: 1
1782	  n_truncated: 61
1783	  n_total: 985
1784	  n_predictions: 10701
1785	  checkpoint: checkpoint-100
1786	  model: Qwen3-4B + SFT merged + GRPO bf16 LoRA ckpt-100
1787	  inference_time_s: 3170.3
1788	  Created:    2026-05-15T14:43:48.481Z
1789	  Updated:    2026-05-15T15:55:52.592Z
1790	
1791	### plan_014_no_evidence_eval_d076
1792	  Category:   eval, no_evidence
1793	  Status:     DONE
1794	  Conclusion: success
1795	  Parent:     plan_014_sft_no_evidence
1796	  ign_f1:     0.4721
1797	  f1: 0.4876
1798	  precision: 0.4901
1799	  recall: 0.4851
1800	  format_compliance_rate: 0.9929
1801	  n_truncated: 307
1802	  inference_time_seconds: 6903.9
1803	  Hypothesis: 4B no-evidence SFT eval under D076 unified protocol (batch_size=4, max_new_tokens=1024, seed=42, no-quantize). Required for clean scaling comparison across 1.7B/4B/8B.
1804	  Created:    2026-05-16T14:26:29.748Z
1805	  Updated:    2026-05-16T17:37:09.823Z
1806	
1807	### plan_014_sft_no_evidence
1808	  Category:   no_evidence
1809	  Status:     DONE
1810	  Conclusion: success
1811	  Parent:     (none)
1812	  train_loss: 0.7077
1813	  eval_loss: 0.8781
1814	  eval_token_accuracy: 0.8086
1815	  epochs: 3
1816	  total_steps: 570
1817	  train_runtime_min: 64
1818	  samples: 3027
1819	  trainable_params: 132M/4.15B (3.18%)
1820	  Hypothesis: SFT-without-evidence ablation: 训练只输出 relation triples（不含 evidence sentences）的 SFT 模型。量化 joint evidence generation 对 extraction 的代价（当前 rel_f1=0.4057 vs 只抽关系的 LMRC 60.7 的 gap 有多少来自 evidence 负担）。
1821	  Created:    2026-05-15T15:55:43.710Z
1822	  Updated:    2026-05-15T18:42:28.216Z
1823	
1824	### plan_015_grpo_g4_bf16
1825	  Category:   grpo
1826	  Status:     DONE
1827	  Conclusion: killed
1828	  Parent:     (none)
1829	  Metrics:    (none)
1830	  Hypothesis: bf16 LoRA GRPO clean control: 与原始 QLoRA GRPO 仅改 quantization（4-bit → bf16），保持 G=4, kl=0, CED reward 不变。验证 catastrophic forgetting 是否由 QLoRA quantization 导致。
1831	  Created:    2026-05-15T15:58:43.784Z
1832	  Updated:    2026-05-15T16:03:08.279Z
1833	
1834	### plan_015_grpo_g4_bf16_v2
1835	  Category:   grpo
1836	  Status:     DONE
1837	  Conclusion: killed
1838	  Parent:     plan_011_grpo_g8_bf16
1839	  Metrics:    (none)
1840	  Hypothesis: Robustness check: bf16 LoRA GRPO 在 G=4, kl=0, lr=5e-6 条件下是否也防止 catastrophic forgetting。非 single-variable ablation（kl/lr/G 均与 QLoRA 对照组不同）。D052 确认 plan_011 vs mvp2_grpo_ced_kl001_r4 已是 clean quantization ablation。
1841	  Created:    2026-05-15T16:06:43.308Z
1842	  Updated:    2026-05-15T16:54:42.310Z
1843	
1844	### plan_015_grpo_g4_bf16_v3
1845	  Category:   grpo
1846	  Status:     DONE
1847	  Conclusion: killed
1848	  Parent:     (none)
1849	  Metrics:    (none)
1850	  Hypothesis: P2 robustness check: bf16 LoRA GRPO G=4, kl=0.01, lr=5e-6。D052 确认 plan_011 vs mvp2_grpo_ced_kl001_r4 已是 clean single-variable quantization ablation (Δ=+23.8pp)。v3 仅为 robustness data point，lr=5e-6 与对照组 lr=5e-5 不一致。
1851	  Created:    2026-05-15T16:27:09.496Z
1852	  Updated:    2026-05-15T16:54:54.376Z
1853	
1854	### plan_016_llama_3_1_8b_no_evidence_eval
1855	  Category:   eval, no_evidence
1856	  Status:     DONE
1857	  Conclusion: success
1858	  Parent:     plan_016_llama_3_1_8b_no_evidence_sft
1859	  ign_f1:     0.5452
1860	  rel_f1: 0.5624
1861	  evi_f1: 0
1862	  edcr: 0
1863	  Hypothesis: LLaMA-3.1-8B no-evidence SFT should achieve similar rel_f1 to evidence-SFT (tax≈0), cross-family validating the 8B-scale evidence absorption pattern observed in Qwen3-8B.
1864	  Created:    2026-05-16T12:05:53.861Z
1865	  Updated:    2026-05-17T02:55:31.810Z
1866	
1867	### plan_016_llama_3_1_8b_no_evidence_sft
1868	  Category:   no_evidence
1869	  Status:     DONE
1870	  Conclusion: success
1871	  Parent:     (none)
1872	  Metrics:    (none)
1873	  Hypothesis: LLaMA-3.1-8B no-evidence SFT baseline for cross-family evidence tax measurement. Paired with evidence-SFT to quantify evidence generation cost on a non-Qwen architecture at 8B scale.
1874	  Created:    2026-05-16T11:06:47.006Z
1875	  Updated:    2026-05-17T02:55:47.936Z
1876	
1877	### plan_016_llama_3_1_8b_sft_eval
1878	  Category:   eval
1879	  Status:     DONE
1880	  Conclusion: success
1881	  Parent:     plan_016_llama_3_1_8b_sft
1882	  ign_f1:     0.5384
1883	  rel_f1: 0.5514
1884	  evi_f1: 0.8151
1885	  edcr: 0.628
1886	  precision: 0.5464
1887	  recall: 0.5565
1888	  evi_f1_joint: 0.4317
1889	  format_compliance_rate: 0.9949
1890	  n_truncated: 197
1891	  n_predictions: 15325
1892	  inference_time_seconds: 7331.3
1893	  evidence_tax_ign_f1: 0.0068
1894	  evidence_tax_rel_f1: 0.011
1895	  Hypothesis: LLaMA-3.1-8B SFT with evidence generation should achieve comparable rel_f1 to Qwen3-8B SFT, establishing cross-family baseline for evidence tax measurement. Evidence tax at 8B scale predicted near-zero based on Qwen3-8B pattern.
1896	  Created:    2026-05-16T12:06:49.282Z
1897	  Updated:    2026-05-17T02:55:20.475Z
1898	
1899	### plan_016_llama_grpo_qlora
1900	  Category:   grpo
1901	  Status:     DONE
1902	  Conclusion: success
1903	  Parent:     mvp2_grpo_ced_lr5e6_r1
1904	  format_reward: 1
1905	  f1_reward: 0
1906	  ced_reward: 0
1907	  entropy: 0.28
1908	  final_step: 60
1909	  grad_norm: 0
1910	  loss: 0
1911	  frac_reward_zero_std: 1
1912	  output_length_final: 172
1913	  conclusion_note: C2 cross-family validated: LLaMA QLoRA GRPO shows same catastrophic decoupling as Qwen (format gaming, zero IE ability)
1914	  Hypothesis: QLoRA GRPO catastrophic decoupling (format gaming + zero IE ability) is not Qwen-specific: LLaMA-3.1-8B under identical QLoRA GRPO training should exhibit the same failure mode (grad_norm→0, loss→0, rel_f1→0). Cross-family validation of C2.
1915	  Created:    2026-05-16T13:14:37.199Z
1916	  Updated:    2026-05-17T02:55:08.871Z
1917	
1918	### random_rsft_k1_baseline
1919	  Category:   random_rsft
1920	  Status:     DONE
1921	  Conclusion: success
1922	  Parent:     (none)
1923	  train_loss: 0.578
1924	  mean_token_accuracy: 0.8552
1925	  global_steps: 1020
1926	  epochs: 3
1927	  Hypothesis: Random k=1 RSFT baseline: same candidate pool as CED RSFT but random selection instead of CED scoring. If random RSFT significantly underperforms CED RSFT (rel_f1 gap > 1.5pp), proves CED scoring precision is the key, not just data filtering quantity. CED k=1 mean rel_f1=0.4596, expect random < 0.44...
1928	  Created:    2026-05-18T13:32:46.287Z
1929	  Updated:    2026-05-18T22:23:06.386Z
1930	
1931	### random_rsft_k1_eval
1932	  Category:   eval, random_rsft
1933	  Status:     DONE
1934	  Conclusion: success
1935	  Parent:     random_rsft_k1_baseline
1936	  ign_f1:     0.4114
1937	  f1: 0.4198
1938	  evi_f1: 0.7964
1939	  evi_f1_joint: 0.3216
1940	  EDCR: 0.6971
1941	  format_compliance: 0.999
1942	  field_compliance: 0.7482
1943	  truncated: 235
1944	  n_total: 985
1945	  n_predictions: 16110
1946	  inference_time_seconds: 11778.5
1947	  Hypothesis: Random k=1 RSFT eval: if random selection significantly underperforms CED RSFT (gap > 1.5pp in rel_f1), proves CED scoring precision is the key differentiator. CED k=1 mean rel_f1=0.4596, expect random &lt; 0.445.
1948	  Created:    2026-05-18T16:34:48.815Z
1949	  Updated:    2026-05-18T20:08:52.336Z
1950	
1951	### reeval_ced_s42
1952	  Category:   eval
1953	  Status:     DONE
1954	  Conclusion: success
1955	  Parent:     mvp2_rsft_train_r1
1956	  ign_f1:     0.4423
1957	  rel_f1: 0.4517
1958	  evi_f1: 0.8175
1959	  evi_f1_joint: 0.3518
1960	  edcr: 0.6569
1961	  format_compliance_rate: 1
1962	  field_compliance_rate: 0.7756
1963	  n_truncated: 214
1964	  inference_time_seconds: 10815.5
1965	  Hypothesis: Re-eval CED RSFT s42 with unified protocol: batch_size=4 + --no-quantize + --sft_adapter + max_new_tokens=1024. 原 mvp2_eval_rsft_r2b_maxtok1536_r2 用了 batch_size=8 + max_new_tokens=1536。Paired t-test 关键路径。
1966	  Created:    2026-05-16T02:37:58.498Z
1967	  Updated:    2026-05-16T10:14:00.520Z
1968	
1969	### reeval_ced_s44
1970	  Category:   eval
1971	  Status:     DONE
1972	  Conclusion: success
1973	  Parent:     mvp2_rsft_train_r1_s44
1974	  ign_f1:     0.4511
1975	  rel_f1: 0.4621
1976	  evi_f1: 0.805
1977	  evi_f1_joint: 0.3677
1978	  edcr: 0.635
1979	  format_compliance_rate: 1
1980	  field_compliance_rate: 0.802
1981	  n_truncated: 190
1982	  inference_time_seconds: 13077.6
1983	  Hypothesis: Re-eval CED RSFT s44 with unified protocol: batch_size=4 + --no-quantize + --sft_adapter + max_new_tokens=1024 + seed=44. 原 eval 用了 batch_size≈16 且 seed=42（错误）。Paired t-test 关键路径。
1984	  Created:    2026-05-16T02:38:00.052Z
1985	  Updated:    2026-05-16T10:14:02.479Z
1986	
1987	### reeval_flat_nli_s42
1988	  Category:   eval
1989	  Status:     DONE
1990	  Conclusion: success
1991	  Parent:     plan_001_rsft_flat_nli
1992	  ign_f1:     0.4448
1993	  rel_f1: 0.4535
1994	  evi_f1: 0.8039
1995	  evi_f1_joint: 0.3558
1996	  edcr: 0.6458
1997	  format_compliance_rate: 1
1998	  field_compliance_rate: 0.7787
1999	  n_truncated: 205
2000	  inference_time_seconds: 13253.1
2001	  Hypothesis: Re-eval flat-NLI RSFT s42 with unified protocol: batch_size=4 + --no-quantize + --sft_adapter + max_new_tokens=1024. 原 eval_plan_001_flat_nli 用了 batch_size=16。Paired t-test 关键路径。
2002	  Created:    2026-05-16T02:38:03.120Z
2003	  Updated:    2026-05-16T10:14:04.270Z
2004	
2005	### reeval_flat_nli_s43
2006	  Category:   eval
2007	  Status:     DONE
2008	  Conclusion: success
2009	  Parent:     plan_001_flat_nli_seed43
2010	  ign_f1:     0.4523
2011	  rel_f1: 0.4523
2012	  evi_f1: 0.8158
2013	  edcr: 0.6505
2014	  num_preds: 15357
2015	  format_ok: 984/985
2016	  truncated: 211/985
2017	  inference_time_s: 3515.8
2018	  Hypothesis: Re-eval flat-NLI RSFT seed=43 WITH --sft_adapter (D064 bug fix). 原 eval_plan_001_flat_nli_s43 因缺 --sft_adapter 导致 rel_f1=0.0022 无效。对比 flat-NLI s42 (rel_f1=0.4539) 和 CED RSFT mean (0.4596)。
2019	  Created:    2026-05-15T22:00:33.691Z
2020	  Updated:    2026-05-15T23:59:33.440Z
2021	
2022	### reeval_flat_nli_s43_r2
2023	  Category:   eval
2024	  Status:     DONE
2025	  Conclusion: success
2026	  Parent:     (none)
2027	  ign_f1:     0.4503
2028	  rel_f1: 0.4586
2029	  rel_precision: 0.4732
2030	  rel_recall: 0.4449
2031	  evi_f1: 0.8113
2032	  evi_precision: 0.8035
2033	  evi_recall: 0.8192
2034	  evi_f1_joint: 0.358
2035	  edcr: 0.6552
2036	  format_ok_rate: 0.999
2037	  n_truncated: 184
2038	  n_predictions: 15015
2039	  Hypothesis: Re-eval flat-NLI RSFT s43 with unified protocol: batch_size=4 + --no-quantize + --sft_adapter + --max_new_tokens 1024. 原 reeval_flat_nli_s43 用了 batch_size=16 导致协议不一致。C3 paired t-test 关键路径。
2040	  Created:    2026-05-16T02:32:45.507Z
2041	  Updated:    2026-05-16T06:10:14.112Z
2042	
2043	### reeval_flat_nli_s44
2044	  Category:   eval
2045	  Status:     DONE
2046	  Conclusion: killed
2047	  Parent:     (none)
2048	  Metrics:    (none)
2049	  Created:    2026-05-16T08:56:36.565Z
2050	  Updated:    2026-05-16T09:26:04.920Z
2051	
2052	### reeval_rsft_topk3
2053	  Category:   eval
2054	  Status:     DONE
2055	  Conclusion: negative
2056	  Parent:     plan_008_rsft_topk3
2057	  ign_f1:     0.4364
2058	  rel_f1: 0.4454
2059	  rel_precision: 0.4512
2060	  rel_recall: 0.4398
2061	  evi_f1: 0.8088
2062	  edcr: 0.6635
2063	  format_ok_rate: 0.999
2064	  n_truncated: 214
2065	  n_predictions: 16020
2066	  inference_time_seconds: 3546.4
2067	  ign_f1_corrected: True
2068	  Hypothesis: Re-eval RSFT top_k=3 WITH --sft_adapter (D064 bug fix). 原 eval_plan_008_rsft_topk3 因缺 --sft_adapter 被 killed。对比 CED RSFT top_k=1 (rel_f1≈0.46) 和 SFT baseline (0.4057)。
2069	  Created:    2026-05-15T22:00:34.722Z
2070	  Updated:    2026-05-16T00:24:22.091Z
2071	
2072	### reeval_sft_baseline_d076
2073	  Category:   eval
2074	  Status:     DONE
2075	  Conclusion: success
2076	  Parent:     (none)
2077	  ign_f1:     0.3974
2078	  rel_f1: 0.4049
2079	  evi_f1: 0.7986
2080	  edcr: 0.6982
2081	  evi_f1_joint: 0.3147
2082	  format_compliance_rate: 0.998
2083	  n_truncated: 288
2084	  n_documents: 985
2085	  n_predictions: 16880
2086	  inference_time_sec: 7056.5
2087	  Hypothesis: Re-eval Qwen3-4B SFT baseline under D076 unified protocol (batch_size=4, no-quantize, max_new_tokens=1024, seed=42). Required as canonical comparison point for all RSFT/GRPO experiments and evidence tax computation.
2088	  Created:    2026-05-16T05:26:37.542Z
2089	  Updated:    2026-05-17T02:56:09.813Z
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01SfhnwAfu5FGq4CJbNHa37Q",
  "session_id": "bc5f4965-b9c9-4c46-9109-14848d79f92e",
  "uuid": "ac6c13b3-abc5-4f8e-9bcf-9b6da096302c"
}
```

</details>

---

### System

_source line 49_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a01ea92613c0e609d",
  "tool_use_id": "toolu_01SfhnwAfu5FGq4CJbNHa37Q",
  "description": "Reading ~/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/bc5f4965-b9c9-4c46-9109-14848d79f92e/tool-results/bzi6o1ptf.txt",
  "usage": {
    "total_tokens": 58871,
    "tool_uses": 11,
    "duration_ms": 71046
  },
  "last_tool_name": "Read",
  "uuid": "9c3e3f8a-7731-4f48-84f0-57f29d593f9c",
  "session_id": "bc5f4965-b9c9-4c46-9109-14848d79f92e"
}
```

---

### Tool call

_source line 50_

<details open><summary>🔧 Tool call — Read · `toolu_01Q5oGp6wTAWffJdE7X2bUQh`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/bc5f4965-b9c9-4c46-9109-14848d79f92e/tool-results/bzi6o1ptf.txt",
  "offset": 2089,
  "limit": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01SfhnwAfu5FGq4CJbNHa37Q",
  "session_id": "bc5f4965-b9c9-4c46-9109-14848d79f92e",
  "uuid": "5e0b48da-f7ae-4a7d-a708-36999949d361",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015idruownRxTLhywMoqWvyS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10924,
      "cache_read_input_tokens": 47397,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 10924,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 36,
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

_source line 51 · 2026-05-19T12:41:22.356Z_

<details><summary>↩ Tool result · `toolu_01Q5oGp6wTAWffJdE7X2bUQh`</summary>

```text
2089	  Updated:    2026-05-17T02:56:09.813Z
2090	
2091	### rsft_s43_dev_eval_preds
2092	  Category:   eval
2093	  Status:     DONE
2094	  Conclusion: success
2095	  Parent:     (none)
2096	  ign_f1:     0.4512
2097	  f1: 0.4601
2098	  evi_f1: 0.8063
2099	  edcr: 0.6542
2100	  evi_f1_joint: 0.3605
2101	  format_compliance_rate: 1
2102	  field_compliance_rate: 0.809
2103	  n_truncated: 184
2104	  inference_time_seconds: 10982
2105	  Hypothesis: Eval RSFT-s43 (CED-scored) on DocRED dev with predictions saved. Prerequisite for Lead 1 CED evidence filtering: per-sentence NLI scoring requires full prediction outputs.
2106	  Created:    2026-05-17T08:35:42.135Z
2107	  Updated:    2026-05-17T23:18:03.147Z
2108	
2109	### rsft_s44_dev_eval_preds
2110	  Category:   eval
2111	  Status:     DONE
2112	  Conclusion: failed
2113	  Parent:     (none)
2114	  Metrics:    (none)
2115	  Hypothesis: Re-run RSFT s44 dev eval with predictions saved, as prerequisite for CED evidence filtering experiment (线索1: inference-time distractor citation removal). Predictions needed for per-sentence NLI scoring.
2116	  Created:    2026-05-17T05:02:50.832Z
2117	  Updated:    2026-05-17T08:25:22.846Z
2118	
2119	### seed_llama_rsft_k1_s43_eval
2120	  Category:   eval
2121	  Status:     DONE
2122	  Conclusion: success
2123	  Parent:     rsft_llama_k1_s43_train
2124	  Metrics:    (none)
2125	  Hypothesis: LLaMA-8B RSFT k=1 seed43 eval: paired with s42 (rel_f1=0.5839) for seed robustness. If s43 gives similar results (±1.5pp), cross-architecture RSFT k=1 claim is robust. Expected rel_f1 ~0.58±0.015.
2126	  Created:    2026-05-18T13:30:51.665Z
2127	  Updated:    2026-05-18T15:22:14.518Z
2128	
2129	### smoke_test_grpo
2130	  Category:   grpo
2131	  Status:     DONE
2132	  Conclusion: success
2133	  Parent:     (none)
2134	  Metrics:    (none)
2135	  Created:    2026-05-14T05:20:00.970Z
2136	  Updated:    2026-05-14T06:09:18.626Z
2137	
2138	### wave1_grpo_bf16_g4
2139	  Category:   grpo
2140	  Status:     DONE
2141	  Conclusion: success
2142	  Parent:     (none)
2143	  reward_mean: 1.7646
2144	  steps_completed: 200
2145	  max_steps: 200
2146	  Hypothesis: GRPO bf16 without quantization (G=4): prior GRPO runs used int4 quantization which may have caused training instability. bf16 full precision should provide clean GRPO signal. If GRPO improves over RSFT, validates Claim 2 (decoupling spectrum). Expected: rel_f1 > RSFT baseline (~52pp).
2147	  Created:    2026-05-18T12:46:19.740Z
2148	  Updated:    2026-05-18T20:09:28.981Z
2149	
2150	### wave1_sft_4b_s43_eval
2151	  Category:   eval
2152	  Status:     DONE
2153	  Conclusion: failed
2154	  Parent:     wave1_sft_4b_s43
2155	  Metrics:    (none)
2156	  Hypothesis: SFT 4B seed43 eval (D076 protocol): baseline SFT performance for seed43. Paired with s44 for mean±std. Expected rel_f1 ~50.5 based on prior 4B SFT s42 results.
2157	  Created:    2026-05-18T14:01:42.261Z
2158	  Updated:    2026-05-18T15:43:30.104Z
2159	
2160	### wave1_sft_4b_s43_eval_r2
2161	  Category:   eval
2162	  Status:     DONE
2163	  Conclusion: success
2164	  Parent:     (none)
2165	  ign_f1:     0.4365
2166	  rel_f1: 0.4429
2167	  evi_f1_joint: 0.3462
2168	  evi_f1_tp: 0.8021
2169	  edcr: 0.6827
2170	  format_compliance_rate: 1
2171	  n_truncated: 318
2172	  n_predictions: 17055
2173	  inference_time_seconds: 7157.9
2174	  Hypothesis: 4B SFT seed43 eval r2 (corrected D076 command: --model_path=base --sft_adapter=adapter). Re-run of failed wave1_sft_4b_s43_eval. Expected rel_f1 ~50.5 based on canonical 4B SFT s42.
2175	  Created:    2026-05-18T19:29:28.052Z
2176	  Updated:    2026-05-18T21:34:25.964Z
2177	
2178	### wave1_sft_4b_s44_eval
2179	  Category:   eval
2180	  Status:     DONE
2181	  Conclusion: failed
2182	  Parent:     wave1_sft_4b_s44
2183	  Metrics:    (none)
2184	  Hypothesis: SFT 4B seed44 eval (D076 protocol): baseline SFT performance for seed44. Paired with s43 for mean±std. Expected rel_f1 ~50.5 based on prior 4B SFT s42 results.
2185	  Created:    2026-05-18T14:01:43.597Z
2186	  Updated:    2026-05-18T15:43:33.593Z
2187	
2188	### wave1_sft_4b_s44_eval_r2
2189	  Category:   eval
2190	  Status:     DONE
2191	  Conclusion: success
2192	  Parent:     wave1_sft_4b_s44
2193	  ign_f1:     0.4734
2194	  f1: 0.4838
2195	  ign_precision: 0.4676
2196	  ign_recall: 0.4794
2197	  precision: 0.4898
2198	  recall: 0.478
2199	  evi_f1_joint: 0.382
2200	  evi_f1_tp: 0.7875
2201	  edcr: 0.6581
2202	  format_ok_rate: 0.997
2203	  n_truncated: 249
2204	  n_documents: 985
2205	  n_predictions: 16143
2206	  inference_time_seconds: 6669.5
2207	  Hypothesis: 4B SFT seed44 eval r2 (corrected D076 command: --model_path=base --sft_adapter=adapter). Re-run of failed wave1_sft_4b_s44_eval. Expected rel_f1 ~50.5 based on canonical 4B SFT s42.
2208	  Created:    2026-05-18T20:05:57.119Z
2209	  Updated:    2026-05-18T22:20:06.715Z
2210	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01SfhnwAfu5FGq4CJbNHa37Q",
  "session_id": "bc5f4965-b9c9-4c46-9109-14848d79f92e",
  "uuid": "a1cd4c25-0779-483a-8864-3f8f3f3857b0"
}
```

</details>

---

### System

_source line 52_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a01ea92613c0e609d",
  "tool_use_id": "toolu_01SfhnwAfu5FGq4CJbNHa37Q",
  "status": "completed",
  "output_file": "",
  "summary": "Extract eval metrics from registry",
  "usage": {
    "total_tokens": 61237,
    "tool_uses": 11,
    "duration_ms": 172733
  },
  "uuid": "17928cca-f069-459e-a3b9-860ec7b2b879",
  "session_id": "bc5f4965-b9c9-4c46-9109-14848d79f92e"
}
```

---

### Tool result

_source line 53 · 2026-05-19T12:43:04.037Z_

<details><summary>↩ Tool result · `toolu_01SfhnwAfu5FGq4CJbNHa37Q`</summary>

```text
All data extracted. Now let me compile a clean structured output.

Here is the complete extraction of all 149 matching experiments, organized by category.

---

## EVAL experiments (with "eval" in name)

### SFT Baselines

| experiment_id | status | conclusion | ign_f1 | rel_f1 | evi_f1 | edcr | notes |
|---|---|---|---|---|---|---|---|
| mvp2_sft_eval | DONE | killed | - | - | - | - | |
| mvp2_sft_eval_r2 | DONE | success | 0.4057 | 0.4057 | 0.7979 | 0.7118 | |
| mvp2_sft_eval_r3 | DONE | success | 0.4057 | 0.4057 | 0.7979 | 0.7118 | |
| mvp2_eval_sft_baseline | DONE | success | - | 0.4057 | 0.7979 | 0.7118 | evi_f1_joint=0.3117 |
| eval_sft_baseline_noquant | DONE | success | - | 0.4106 | 0.8013 | 0.7039 | |
| reeval_sft_baseline_d076 | DONE | success | 0.3974 | 0.4049 | 0.7986 | 0.6982 | D076 protocol |
| d111_4b_sft_s42_reeval | DONE | success | 0.3974 | 0.4049 | 0.7986 | 0.6982 | D076 standardized |
| wave1_sft_4b_s43_eval | DONE | failed | - | - | - | - | |
| wave1_sft_4b_s43_eval_r2 | DONE | success | 0.4365 | 0.4429 | - | 0.6827 | evi_f1_tp=0.8021 |
| wave1_sft_4b_s44_eval | DONE | failed | - | - | - | - | |
| wave1_sft_4b_s44_eval_r2 | DONE | success | 0.4734 | - | - | 0.6581 | f1=0.4838, evi_f1_tp=0.7875 |

### 1.7B Scale SFT Evals

| experiment_id | status | conclusion | ign_f1 | f1 | evi_f1 | edcr | notes |
|---|---|---|---|---|---|---|---|
| plan_006_qwen3_1_7b_sft_eval | DONE | success | 0.4786 | 0.4945 | 0.8316 | 0.6704 | D076 protocol |
| plan019_1_7b_sft_s43_eval | DONE | success | 0.4286 | 0.4372 | 0.835 | 0.704 | |
| plan019_1_7b_sft_s44_eval | DONE | success | 0.4321 | 0.4441 | - | 0.69 | evi_f1_tp=0.819 |

### 8B Scale SFT Evals

| experiment_id | status | conclusion | ign_f1 | f1 | evi_f1 | edcr | notes |
|---|---|---|---|---|---|---|---|
| plan_006_qwen3_8b_sft_eval | DONE | success | 0.5051 | 0.5262 | 0.8188 | 0.651 | D076 protocol |
| plan019_8b_sft_s44_eval | DONE | success | 0.4681 | 0.4841 | 0.8361 | 0.6697 | |
| plan_016_llama_3_1_8b_sft_eval | DONE | success | 0.5384 | - | 0.8151 | 0.628 | rel_f1=0.5514, evidence_tax=0.011 |

### 14B SFT Eval

| experiment_id | status | conclusion | ign_f1 | notes |
|---|---|---|---|---|
| plan017_14b_sft_eval | DONE | killed | - | |

### CED RSFT Evals (4B)

| experiment_id | status | conclusion | ign_f1 | rel_f1 | evi_f1 | edcr | evi_f1_joint | notes |
|---|---|---|---|---|---|---|---|---|
| mvp2_eval_rsft_r1 | DONE | success | - | 0.4449 | 0.8187 | 0.6565 | 0.3468 | seed=42 |
| mvp2_eval_rsft_r2a | DONE | success | 0.4494 | 0.4494 | 0.8108 | 0.6641 | 0.3509 | 1ep, alpha=128 |
| mvp2_eval_rsft_r2b | DONE | success | 0.4493 | 0.4493 | 0.8128 | 0.6609 | 0.349 | 1ep, alpha=32, lr=1e-5 |
| mvp2_eval_rsft_r2b_maxtok1536 | DONE | killed | - | - | - | - | - | truncation diagnosis |
| mvp2_eval_rsft_r2b_maxtok1536_r2 | DONE | negative | 0.4504 | 0.4504 | 0.8102 | 0.674 | - | EDCR improved marginally |
| mvp2_eval_rsft_s43 | DONE | failed | - | - | - | - | - | |
| mvp2_eval_rsft_s43_r2 | DONE | success | 0.4683 | 0.4683 | 0.8156 | 0.6388 | 0.3711 | mvp2_pass=True |
| mvp2_eval_rsft_s44 | DONE | killed | - | - | - | - | - | |
| reeval_ced_s42 | DONE | success | 0.4423 | 0.4517 | 0.8175 | 0.6569 | 0.3518 | D076 unified protocol |
| reeval_ced_s44 | DONE | success | 0.4511 | 0.4621 | 0.805 | 0.635 | 0.3677 | D076 unified protocol |
| eval_rsft_ced_s43 | DONE | success | 0.4512 | 0.4601 | 0.8063 | 0.6542 | 0.3605 | |
| eval_rsft_ced_s45 | DONE | success | 0.4416 | 0.4514 | 0.8174 | 0.655 | 0.3558 | |
| d112_rsft_s44_eval | DONE | failed | 0.2181 | - | - | - | - | INVALID: QLoRA confound |
| rsft_s43_dev_eval_preds | DONE | success | 0.4512 | - | 0.8063 | 0.6542 | 0.3605 | f1=0.4601 |
| rsft_s44_dev_eval_preds | DONE | failed | - | - | - | - | - | |

### Flat-NLI RSFT Evals

| experiment_id | status | conclusion | ign_f1 | rel_f1 | evi_f1 | edcr | evi_f1_joint | notes |
|---|---|---|---|---|---|---|---|---|
| eval_plan_001_flat_nli | DONE | success | 0.4539 | 0.4539 | 0.8043 | 0.6431 | - | seed=42 |
| eval_flat_nli_s44 | DONE | success | 0.452126 | - | 0.813123 | 0.6458 | 0.3597 | |
| eval_flat_nli_seed44 | DONE | killed | - | - | - | - | - | |
| eval_flat_nli_seed45 | DONE | success | 0.446181 | - | 0.815399 | 0.6521 | 0.3556 | |
| eval_plan_001_flat_nli_s43 | DONE | failed | 0.0022 | 0.0022 | 0.8533 | 0.9982 | - | INVALID: missing --sft_adapter |
| reeval_flat_nli_s42 | DONE | success | 0.4448 | 0.4535 | 0.8039 | 0.6458 | 0.3558 | D076 unified |
| reeval_flat_nli_s43 | DONE | success | 0.4523 | 0.4523 | 0.8158 | 0.6505 | - | |
| reeval_flat_nli_s43_r2 | DONE | success | 0.4503 | 0.4586 | 0.8113 | 0.6552 | 0.358 | D076 unified |
| reeval_flat_nli_s44 | DONE | killed | - | - | - | - | - | |

### RSFT top_k=3 Evals

| experiment_id | status | conclusion | ign_f1 | rel_f1 | evi_f1 | edcr | notes |
|---|---|---|---|---|---|---|---|
| eval_plan_008_rsft_topk3 | DONE | killed | - | - | - | - | INVALID: missing --sft_adapter |
| eval_plan_008_topk3_fixed | DONE | killed | - | - | - | - | |
| reeval_rsft_topk3 | DONE | negative | 0.4364 | 0.4454 | 0.8088 | 0.6635 | top_k=3 underperforms k=1 |

### DPO Evals

| experiment_id | status | conclusion | ign_f1 | rel_f1 | evi_f1 | edcr | notes |
|---|---|---|---|---|---|---|---|
| eval_plan_012_dpo_ced_ckpt400 | DONE | failed | - | - | - | - | |
| eval_plan_012_dpo_ced_1ep | DONE | negative | 0.0022 | 0.0022 | 0.75 | 0.9982 | |
| eval_plan_012_dpo_1ep_fixed | DONE | killed | - | - | - | - | |
| eval_plan_012_dpo_1ep_fixed_r2 | DONE | negative | 0.4034 | 0.4034 | 0.8088 | 0.7139 | DPO 1ep matches SFT baseline, delta=-0.0023 |

### 1.7B RSFT Evals

| experiment_id | status | conclusion | ign_f1 | f1 | evi_f1 | edcr | evi_f1_joint | notes |
|---|---|---|---|---|---|---|---|---|
| plan_006_qwen3_1_7b_rsft_eval | DONE | failed | - | - | - | - | - | |
| plan_006_qwen3_1_7b_rsft_eval_r2 | DONE | success | 0.505 | 0.5219 | 0.8309 | 0.6297 | 0.4223 | seed=42 |
| plan_006_qwen3_1_7b_rsft_seed43_eval | DONE | success | 0.5024 | 0.518 | - | 0.6246 | 0.4201 | evi_f1_tp=0.8341 |
| plan019_1_7b_rsft_s43_r2_eval | DONE | success | 0.5109 | - | 0.8278 | 0.6245 | 0.4278 | f1=0.5271 |
| plan019_1_7b_rsft_s44_r2_eval | DONE | success | 0.5125 | - | 0.8267 | 0.6181 | 0.4289 | f1=0.5294 |
| plan006_1_7b_rsft_eval | DONE | killed | - | - | - | - | - | |

### 8B RSFT Evals

| experiment_id | status | conclusion | ign_f1 | f1 | evi_f1 | edcr | evi_f1_joint | notes |
|---|---|---|---|---|---|---|---|---|
| plan_006_qwen3_8b_rsft_eval | DONE | success | 0.5433 | 0.5606 | 0.8052 | 0.6377 | 0.4413 | |
| plan019_8b_rsft_s44_eval | DONE | success | 0.5451 | 0.562 | - | 0.6233 | - | evi_f1_tp=0.8145, evi_f1_dreeam=0.4472 |

### LLaMA-8B RSFT Evals

| experiment_id | status | conclusion | ign_f1 | rel_f1 | evi_f1 | edcr | evi_f1_joint | notes |
|---|---|---|---|---|---|---|---|---|
| plan_006_llama_rsft_r3_eval | DONE | success | 0.5563 | - | 0.8255 | 0.5856 | 0.4571 | f1=0.5674 |
| plan_006_llama_rsft_seed43_eval | DONE | failed | - | - | - | - | - | |
| plan_006_llama_rsft_seed43_eval_r2 | DONE | success | 0.5619 | 0.5727 | 0.8206 | 0.6073 | 0.4551 | |
| d102_llama_rsft_k1_s43_eval | DONE | killed | - | - | - | - | - | |
| seed_llama_rsft_k1_s43_eval | DONE | success | - | - | - | - | - | (no metrics reported) |

### GRPO QLoRA Evals (catastrophic forgetting trajectory)

| experiment_id | status | conclusion | ign_f1 | rel_f1 | evi_f1 | edcr | notes |
|---|---|---|---|---|---|---|---|
| mvp2_eval_ced_kl001_r4_early | DONE | negative | 0.1563 | 0.1563 | 0.5643 | 0.8858 | |
| mvp2_eval_ced_kl001_r4 | DONE | success | - | 0.00296 | 0.72 | 0.9983 | ckpt-10 |
| mvp2_eval_ced_kl001_r4_step90 | DONE | negative | 0.2108 | 0.2108 | 0.5666 | 0.8584 | |
| mvp2_eval_ced_kl001_r4_step100 | DONE | negative | 0.2167 | 0.2167 | 0.5746 | 0.8539 | |
| mvp2_eval_ced_kl001_r4_high | DONE | failed | - | - | - | - | ckpt-60: rel_f1=0.1467. OOM during ckpt-70 |
| mvp2_eval_ced_kl001_r4_ckpt7080 | DONE | failed | - | - | - | - | OOM |
| mvp2_eval_ced_kl001_r4_ckpt90 | DONE | killed | - | - | - | - | |
| mvp2_eval_ced_kl001_r4_last | DONE | killed | - | - | - | - | |
| mvp2_eval_ced_kl001_r4_multi | DONE | killed | - | - | - | - | Multi-ckpt trajectory: ckpt-10=0.003, ckpt-20=0.0088, ckpt-30=0.0338, ckpt-50=0.1563, ckpt-60=0.1467, ckpt-90=0.2108 |

### GRPO lr=5e-6 Evals (still catastrophic)

| experiment_id | status | conclusion | ign_f1 | rel_f1 | evi_f1 | edcr | notes |
|---|---|---|---|---|---|---|---|
| mvp2_eval_lr5e6_r1_ckpt20 | DONE | negative | - | 0.0077 | 0.628 | 0.993 | |
| mvp2_eval_lr5e6_r1_ckpt40 | DONE | failed | - | - | - | - | |
| mvp2_eval_lr5e6_r1_ckpt40_r2 | DONE | negative | - | 0.0071 | 0.7584 | 0.9942 | |
| mvp2_eval_lr5e6_r1_ckpt60 | DONE | failed | - | - | - | - | |
| mvp2_eval_lr5e6_r1_ckpt60_r2 | DONE | negative | - | 0.0093 | 0.81 | 0.993 | |
| mvp2_eval_lr5e6_r1_ckpt80 | DONE | negative | 0.0116 | 0.0116 | 0.828 | 0.993 | |
| mvp2_eval_lr5e6_r1_ckpt100 | DONE | negative | 0.0138 | 0.0138 | 0.8504 | 0.9876 | |
| mvp2_eval_lr5e6_rp_r2_ckpt20 | DONE | killed | - | - | - | - | recall_penalty variant, killed |

### GRPO bf16 Evals (forgetting fixed)

| experiment_id | status | conclusion | ign_f1 | rel_f1 | evi_f1 | edcr | notes |
|---|---|---|---|---|---|---|---|
| eval_grpo_g8_bf16 | DONE | success | - | - | - | - | ckpt80: 0.4456, ckpt90: 0.4523, ckpt100: 0.4549. Best=ckpt-100 |
| plan_011_grpo_g8_bf16_eval | DONE | success | 0.4549 | 0.4549 | 0.8086 | 0.6318 | ckpt-100 |
| plan_011_bf16_g8_step_eval | DONE | success | - | - | - | - | step_30=0.434, step_50=0.4276, step_70=0.4341 |
| plan_011_eval_g8_bf16_ckpt100 | DONE | killed | - | - | - | - | |
| grpo_bf16_g4_ckpt100_eval | DONE | success | 0.4431 | - | 0.801 | 0.6453 | f1=0.4511 |
| grpo_bf16_g4_ckpt200_eval | DONE | success | 0.4446 | 0.4513 | 0.8053 | 0.6489 | |

### RSFT->GRPO (Lead2) Eval

| experiment_id | status | conclusion | ign_f1 | rel_f1 | evi_f1 | edcr | evi_f1_joint | notes |
|---|---|---|---|---|---|---|---|---|
| lead2_ckpt20_eval | DONE | success | 0.4533 | 0.4617 | 0.8103 | 0.6465 | 0.3642 | Preserves RSFT baseline |

### Re-DocRED Transfer Evals

| experiment_id | status | conclusion | ign_f1 | f1 | evi_f1 | edcr | notes |
|---|---|---|---|---|---|---|---|
| plan_007_redocred_4b_sft_eval | DONE | failed | - | - | - | - | |
| plan_007_redocred_4b_sft_eval_r2 | DONE | success | 0.3659 | 0.3706 | 0.817 | 0.6674 | |
| plan_007_redocred_rsft_eval | DONE | failed | - | - | - | - | OOM + pipeline bug |
| plan_007_redocred_rsft_eval_r2 | DONE | negative | 0.0026 | - | 0.8837 | 0.9978 | Wrong model loading |
| plan_007_redocred_rsft_eval_r3 | DONE | failed | - | - | - | - | |
| plan_007_redocred_rsft_eval_r4 | DONE | failed | - | - | - | - | |
| plan_007_redocred_rsft_eval_r5 | DONE | success | 0.4145 | 0.4234 | 0.8182 | 0.621 | Correct 3-param loading |

### Test Set Eval

| experiment_id | status | conclusion | notes |
|---|---|---|---|
| plan_002_test_eval_s44 | DONE | failed | |
| plan_002_test_eval_s44_r2 | DONE | success | No metrics in registry (test set for paper) |

### Reward Variant Evals

| experiment_id | status | conclusion | notes |
|---|---|---|---|
| plan_009_extract_reward_eval | DONE | failed | |
| plan_009_flatnli_reward_eval | DONE | failed | |
| plan_009_flatnli_reward_eval_r2 | DONE | failed | |

---

## NO_EVIDENCE experiments

| experiment_id | status | conclusion | ign_f1 | rel_f1 | evi_f1 | notes |
|---|---|---|---|---|---|---|
| eval_plan_014_no_evidence | DONE | failed | - | - | - | |
| eval_plan_014_no_evidence_r2 | DONE | success | 0.4721 | 0.4876 | 0 | 4B no-evi |
| eval_plan_014_sft_no_evidence | DONE | success | - | 0.4893 | 0 | rel_ign_f1=0.4893 |
| plan_014_no_evidence_eval_d076 | DONE | success | 0.4721 | - | - | D076 protocol |
| plan017_14b_sft_no_evidence_eval | DONE | killed | - | - | - | 14B |
| plan_006_qwen3_1_7b_no_evidence_eval | DONE | failed | 0.3786 | - | 0.0007 | 1.7B (wrong eval) |
| plan_006_qwen3_1_7b_no_evidence_eval_v2 | DONE | failed | - | - | - | |
| plan_006_qwen3_1_7b_no_evidence_eval_v2r2 | DONE | failed | - | - | - | |
| plan_006_qwen3_1_7b_no_evidence_eval_v3 | DONE | success | 0.3982 | 0.4103 | 0 | evidence_tax=0.0804 |
| plan_006_qwen3_8b_no_evidence_eval | DONE | killed | - | - | - | |
| plan_006_qwen3_8b_no_evidence_eval_v2 | DONE | success | - | - | - | (no metrics in registry) |
| plan_016_llama_3_1_8b_no_evidence_eval | DONE | success | 0.5452 | 0.5624 | 0 | LLaMA 8B |
| plan_006_qwen3_1_7b_no_evidence_sft | DONE | success | - | - | - | Training only |
| plan_006_qwen3_8b_no_evidence_sft | DONE | success | - | - | - | Training only |
| plan_014_sft_no_evidence | DONE | success | - | - | - | Training only |
| plan_016_llama_3_1_8b_no_evidence_sft | DONE | success | - | - | - | Training only |

---

## RANDOM_RSFT experiments

| experiment_id | status | conclusion | ign_f1 | f1 | evi_f1 | edcr | notes |
|---|---|---|---|---|---|---|---|
| random_rsft_k1_baseline | DONE | success | - | - | - | - | Training: loss=0.578, 3 epochs |
| random_rsft_k1_eval | DONE | success | 0.4114 | 0.4198 | 0.7964 | 0.6971 | CED RSFT mean=0.4596 >> random 0.4198, gap=~4pp proves CED scoring precision matters |

---

## GRPO experiments (non-eval, training runs)

| experiment_id | status | conclusion | notes |
|---|---|---|---|
| smoke_test_grpo | DONE | success | |
| mvp2_grpo_ced | DONE | failed | |
| mvp2_grpo_ced_r1 | DONE | killed | |
| mvp2_grpo_ced_r2 | DONE | killed | |
| mvp2_grpo_ced_r3 | DONE | failed | kl_coef=0.05 |
| mvp2_grpo_ced_r4 | DONE | killed | |
| mvp2_grpo_ced_r5 | DONE | negative | |
| mvp2_grpo_ced_kl001 | DONE | failed | kl_coef=0.01 |
| mvp2_grpo_ced_kl001_r2 | DONE | killed | |
| mvp2_grpo_ced_kl001_r3 | DONE | killed | |
| mvp2_grpo_ced_kl001_r4 | DONE | success | 100 steps, best_reward=1.37 at step 90 |
| mvp2_grpo_ced_lr5e6_r1 | DONE | killed | lr=5e-6 |
| mvp2_grpo_ced_lr5e6_p1_r1 | DONE | killed | lr=5e-6 + recall_penalty |
| mvp2_grpo_ced_lr5e6_rp_r1 | DONE | failed | |
| mvp2_grpo_ced_lr5e6_rp_r2 | DONE | killed | |
| mvp2_grpo_extract | DONE | failed | Extraction-only reward |
| mvp2_grpo_extract_r2 | DONE | killed | |
| mvp2_grpo_extract_r3 | DONE | negative | |
| mvp2_grpo_extract_r4 | DONE | killed | |
| mvp2_grpo_flatnli | DONE | failed | |
| mvp2_grpo_flatnli_r2 | DONE | killed | |
| mvp2_grpo_flatnli_r3 | DONE | killed | |
| mvp2_grpo_flatnli_r4 | DONE | killed | |
| mvp2_grpo_flatnli_r5 | DONE | killed | |
| mvp2_grpo_flatnli_r6 | DONE | negative | Collapsed at step 25 |
| plan_011_grpo_g8_bf16 | DONE | success | bf16, 100 steps, no mode collapse |
| plan_015_grpo_g4_bf16 | DONE | killed | |
| plan_015_grpo_g4_bf16_v2 | DONE | killed | |
| plan_015_grpo_g4_bf16_v3 | DONE | killed | |
| plan_016_llama_grpo_qlora | DONE | success | Catastrophic decoupling confirmed cross-family (format=1, f1=0, ced=0) |
| lead2_rsft_grpo_ced | DONE | failed | RSFT->GRPO two-stage |
| lead2_rsft_grpo_ced_r2 | DONE | failed | RSFT->GRPO retry |
| wave1_grpo_bf16_g4 | DONE | success | 200 steps, reward=1.7646 |

---

**Total: 149 matching experiments** (out of 242 in registry).

agentId: a01ea92613c0e609d (use SendMessage with to: 'a01ea92613c0e609d' to continue this agent)
&lt;usage>total_tokens: 68339
tool_uses: 11
duration_ms: 172735&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bc5f4965-b9c9-4c46-9109-14848d79f92e",
  "uuid": "b1e3ba45-b323-430e-8439-b316411377c6",
  "tool_use_result": {
    "status": "completed",
    "prompt": "I need you to extract all eval experiment results from a large registry JSON file. The file is at:\n/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/bc5f4965-b9c9-4c46-9109-14848d79f92e/tool-results/mcp-agent-ml-research-read_registry-1779194396202.txt\n\nThe file schema is `{result: string}` where the `result` field is a JSON string that needs to be parsed again.\n\nI need you to extract ALL experiments whose `experiment_id` contains \"eval\" (case-insensitive). For each, report:\n1. experiment_id\n2. status\n3. conclusion (if any)\n4. Any metrics (especially ign_f1)\n5. Any relevant notes about protocol (D076, etc.)\n\nAlso extract these specific non-eval experiments if they exist:\n- random_rsft_k1_eval or random_rsft_k1_baseline\n- Any experiment with \"grpo\" in the name\n- Any experiment with \"no_evidence\" in the name\n\nUse jq or python to parse the file. Return the complete list — do not summarize or omit any entries. Format as a table or structured list.",
    "agentId": "a01ea92613c0e609d",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "All data extracted. Now let me compile a clean structured output.\n\nHere is the complete extraction of all 149 matching experiments, organized by category.\n\n---\n\n## EVAL experiments (with \"eval\" in name)\n\n### SFT Baselines\n\n| experiment_id | status | conclusion | ign_f1 | rel_f1 | evi_f1 | edcr | notes |\n|---|---|---|---|---|---|---|---|\n| mvp2_sft_eval | DONE | killed | - | - | - | - | |\n| mvp2_sft_eval_r2 | DONE | success | 0.4057 | 0.4057 | 0.7979 | 0.7118 | |\n| mvp2_sft_eval_r3 | DONE | success | 0.4057 | 0.4057 | 0.7979 | 0.7118 | |\n| mvp2_eval_sft_baseline | DONE | success | - | 0.4057 | 0.7979 | 0.7118 | evi_f1_joint=0.3117 |\n| eval_sft_baseline_noquant | DONE | success | - | 0.4106 | 0.8013 | 0.7039 | |\n| reeval_sft_baseline_d076 | DONE | success | 0.3974 | 0.4049 | 0.7986 | 0.6982 | D076 protocol |\n| d111_4b_sft_s42_reeval | DONE | success | 0.3974 | 0.4049 | 0.7986 | 0.6982 | D076 standardized |\n| wave1_sft_4b_s43_eval | DONE | failed | - | - | - | - | |\n| wave1_sft_4b_s43_eval_r2 | DONE | success | 0.4365 | 0.4429 | - | 0.6827 | evi_f1_tp=0.8021 |\n| wave1_sft_4b_s44_eval | DONE | failed | - | - | - | - | |\n| wave1_sft_4b_s44_eval_r2 | DONE | success | 0.4734 | - | - | 0.6581 | f1=0.4838, evi_f1_tp=0.7875 |\n\n### 1.7B Scale SFT Evals\n\n| experiment_id | status | conclusion | ign_f1 | f1 | evi_f1 | edcr | notes |\n|---|---|---|---|---|---|---|---|\n| plan_006_qwen3_1_7b_sft_eval | DONE | success | 0.4786 | 0.4945 | 0.8316 | 0.6704 | D076 protocol |\n| plan019_1_7b_sft_s43_eval | DONE | success | 0.4286 | 0.4372 | 0.835 | 0.704 | |\n| plan019_1_7b_sft_s44_eval | DONE | success | 0.4321 | 0.4441 | - | 0.69 | evi_f1_tp=0.819 |\n\n### 8B Scale SFT Evals\n\n| experiment_id | status | conclusion | ign_f1 | f1 | evi_f1 | edcr | notes |\n|---|---|---|---|---|---|---|---|\n| plan_006_qwen3_8b_sft_eval | DONE | success | 0.5051 | 0.5262 | 0.8188 | 0.651 | D076 protocol |\n| plan019_8b_sft_s44_eval | DONE | success | 0.4681 | 0.4841 | 0.8361 | 0.6697 | |\n| plan_016_llama_3_1_8b_sft_eval | DONE | success | 0.5384 | - | 0.8151 | 0.628 | rel_f1=0.5514, evidence_tax=0.011 |\n\n### 14B SFT Eval\n\n| experiment_id | status | conclusion | ign_f1 | notes |\n|---|---|---|---|---|\n| plan017_14b_sft_eval | DONE | killed | - | |\n\n### CED RSFT Evals (4B)\n\n| experiment_id | status | conclusion | ign_f1 | rel_f1 | evi_f1 | edcr | evi_f1_joint | notes |\n|---|---|---|---|---|---|---|---|---|\n| mvp2_eval_rsft_r1 | DONE | success | - | 0.4449 | 0.8187 | 0.6565 | 0.3468 | seed=42 |\n| mvp2_eval_rsft_r2a | DONE | success | 0.4494 | 0.4494 | 0.8108 | 0.6641 | 0.3509 | 1ep, alpha=128 |\n| mvp2_eval_rsft_r2b | DONE | success | 0.4493 | 0.4493 | 0.8128 | 0.6609 | 0.349 | 1ep, alpha=32, lr=1e-5 |\n| mvp2_eval_rsft_r2b_maxtok1536 | DONE | killed | - | - | - | - | - | truncation diagnosis |\n| mvp2_eval_rsft_r2b_maxtok1536_r2 | DONE | negative | 0.4504 | 0.4504 | 0.8102 | 0.674 | - | EDCR improved marginally |\n| mvp2_eval_rsft_s43 | DONE | failed | - | - | - | - | - | |\n| mvp2_eval_rsft_s43_r2 | DONE | success | 0.4683 | 0.4683 | 0.8156 | 0.6388 | 0.3711 | mvp2_pass=True |\n| mvp2_eval_rsft_s44 | DONE | killed | - | - | - | - | - | |\n| reeval_ced_s42 | DONE | success | 0.4423 | 0.4517 | 0.8175 | 0.6569 | 0.3518 | D076 unified protocol |\n| reeval_ced_s44 | DONE | success | 0.4511 | 0.4621 | 0.805 | 0.635 | 0.3677 | D076 unified protocol |\n| eval_rsft_ced_s43 | DONE | success | 0.4512 | 0.4601 | 0.8063 | 0.6542 | 0.3605 | |\n| eval_rsft_ced_s45 | DONE | success | 0.4416 | 0.4514 | 0.8174 | 0.655 | 0.3558 | |\n| d112_rsft_s44_eval | DONE | failed | 0.2181 | - | - | - | - | INVALID: QLoRA confound |\n| rsft_s43_dev_eval_preds | DONE | success | 0.4512 | - | 0.8063 | 0.6542 | 0.3605 | f1=0.4601 |\n| rsft_s44_dev_eval_preds | DONE | failed | - | - | - | - | - | |\n\n### Flat-NLI RSFT Evals\n\n| experiment_id | status | conclusion | ign_f1 | rel_f1 | evi_f1 | edcr | evi_f1_joint | notes |\n|---|---|---|---|---|---|---|---|---|\n| eval_plan_001_flat_nli | DONE | success | 0.4539 | 0.4539 | 0.8043 | 0.6431 | - | seed=42 |\n| eval_flat_nli_s44 | DONE | success | 0.452126 | - | 0.813123 | 0.6458 | 0.3597 | |\n| eval_flat_nli_seed44 | DONE | killed | - | - | - | - | - | |\n| eval_flat_nli_seed45 | DONE | success | 0.446181 | - | 0.815399 | 0.6521 | 0.3556 | |\n| eval_plan_001_flat_nli_s43 | DONE | failed | 0.0022 | 0.0022 | 0.8533 | 0.9982 | - | INVALID: missing --sft_adapter |\n| reeval_flat_nli_s42 | DONE | success | 0.4448 | 0.4535 | 0.8039 | 0.6458 | 0.3558 | D076 unified |\n| reeval_flat_nli_s43 | DONE | success | 0.4523 | 0.4523 | 0.8158 | 0.6505 | - | |\n| reeval_flat_nli_s43_r2 | DONE | success | 0.4503 | 0.4586 | 0.8113 | 0.6552 | 0.358 | D076 unified |\n| reeval_flat_nli_s44 | DONE | killed | - | - | - | - | - | |\n\n### RSFT top_k=3 Evals\n\n| experiment_id | status | conclusion | ign_f1 | rel_f1 | evi_f1 | edcr | notes |\n|---|---|---|---|---|---|---|---|\n| eval_plan_008_rsft_topk3 | DONE | killed | - | - | - | - | INVALID: missing --sft_adapter |\n| eval_plan_008_topk3_fixed | DONE | killed | - | - | - | - | |\n| reeval_rsft_topk3 | DONE | negative | 0.4364 | 0.4454 | 0.8088 | 0.6635 | top_k=3 underperforms k=1 |\n\n### DPO Evals\n\n| experiment_id | status | conclusion | ign_f1 | rel_f1 | evi_f1 | edcr | notes |\n|---|---|---|---|---|---|---|---|\n| eval_plan_012_dpo_ced_ckpt400 | DONE | failed | - | - | - | - | |\n| eval_plan_012_dpo_ced_1ep | DONE | negative | 0.0022 | 0.0022 | 0.75 | 0.9982 | |\n| eval_plan_012_dpo_1ep_fixed | DONE | killed | - | - | - | - | |\n| eval_plan_012_dpo_1ep_fixed_r2 | DONE | negative | 0.4034 | 0.4034 | 0.8088 | 0.7139 | DPO 1ep matches SFT baseline, delta=-0.0023 |\n\n### 1.7B RSFT Evals\n\n| experiment_id | status | conclusion | ign_f1 | f1 | evi_f1 | edcr | evi_f1_joint | notes |\n|---|---|---|---|---|---|---|---|---|\n| plan_006_qwen3_1_7b_rsft_eval | DONE | failed | - | - | - | - | - | |\n| plan_006_qwen3_1_7b_rsft_eval_r2 | DONE | success | 0.505 | 0.5219 | 0.8309 | 0.6297 | 0.4223 | seed=42 |\n| plan_006_qwen3_1_7b_rsft_seed43_eval | DONE | success | 0.5024 | 0.518 | - | 0.6246 | 0.4201 | evi_f1_tp=0.8341 |\n| plan019_1_7b_rsft_s43_r2_eval | DONE | success | 0.5109 | - | 0.8278 | 0.6245 | 0.4278 | f1=0.5271 |\n| plan019_1_7b_rsft_s44_r2_eval | DONE | success | 0.5125 | - | 0.8267 | 0.6181 | 0.4289 | f1=0.5294 |\n| plan006_1_7b_rsft_eval | DONE | killed | - | - | - | - | - | |\n\n### 8B RSFT Evals\n\n| experiment_id | status | conclusion | ign_f1 | f1 | evi_f1 | edcr | evi_f1_joint | notes |\n|---|---|---|---|---|---|---|---|---|\n| plan_006_qwen3_8b_rsft_eval | DONE | success | 0.5433 | 0.5606 | 0.8052 | 0.6377 | 0.4413 | |\n| plan019_8b_rsft_s44_eval | DONE | success | 0.5451 | 0.562 | - | 0.6233 | - | evi_f1_tp=0.8145, evi_f1_dreeam=0.4472 |\n\n### LLaMA-8B RSFT Evals\n\n| experiment_id | status | conclusion | ign_f1 | rel_f1 | evi_f1 | edcr | evi_f1_joint | notes |\n|---|---|---|---|---|---|---|---|---|\n| plan_006_llama_rsft_r3_eval | DONE | success | 0.5563 | - | 0.8255 | 0.5856 | 0.4571 | f1=0.5674 |\n| plan_006_llama_rsft_seed43_eval | DONE | failed | - | - | - | - | - | |\n| plan_006_llama_rsft_seed43_eval_r2 | DONE | success | 0.5619 | 0.5727 | 0.8206 | 0.6073 | 0.4551 | |\n| d102_llama_rsft_k1_s43_eval | DONE | killed | - | - | - | - | - | |\n| seed_llama_rsft_k1_s43_eval | DONE | success | - | - | - | - | - | (no metrics reported) |\n\n### GRPO QLoRA Evals (catastrophic forgetting trajectory)\n\n| experiment_id | status | conclusion | ign_f1 | rel_f1 | evi_f1 | edcr | notes |\n|---|---|---|---|---|---|---|---|\n| mvp2_eval_ced_kl001_r4_early | DONE | negative | 0.1563 | 0.1563 | 0.5643 | 0.8858 | |\n| mvp2_eval_ced_kl001_r4 | DONE | success | - | 0.00296 | 0.72 | 0.9983 | ckpt-10 |\n| mvp2_eval_ced_kl001_r4_step90 | DONE | negative | 0.2108 | 0.2108 | 0.5666 | 0.8584 | |\n| mvp2_eval_ced_kl001_r4_step100 | DONE | negative | 0.2167 | 0.2167 | 0.5746 | 0.8539 | |\n| mvp2_eval_ced_kl001_r4_high | DONE | failed | - | - | - | - | ckpt-60: rel_f1=0.1467. OOM during ckpt-70 |\n| mvp2_eval_ced_kl001_r4_ckpt7080 | DONE | failed | - | - | - | - | OOM |\n| mvp2_eval_ced_kl001_r4_ckpt90 | DONE | killed | - | - | - | - | |\n| mvp2_eval_ced_kl001_r4_last | DONE | killed | - | - | - | - | |\n| mvp2_eval_ced_kl001_r4_multi | DONE | killed | - | - | - | - | Multi-ckpt trajectory: ckpt-10=0.003, ckpt-20=0.0088, ckpt-30=0.0338, ckpt-50=0.1563, ckpt-60=0.1467, ckpt-90=0.2108 |\n\n### GRPO lr=5e-6 Evals (still catastrophic)\n\n| experiment_id | status | conclusion | ign_f1 | rel_f1 | evi_f1 | edcr | notes |\n|---|---|---|---|---|---|---|---|\n| mvp2_eval_lr5e6_r1_ckpt20 | DONE | negative | - | 0.0077 | 0.628 | 0.993 | |\n| mvp2_eval_lr5e6_r1_ckpt40 | DONE | failed | - | - | - | - | |\n| mvp2_eval_lr5e6_r1_ckpt40_r2 | DONE | negative | - | 0.0071 | 0.7584 | 0.9942 | |\n| mvp2_eval_lr5e6_r1_ckpt60 | DONE | failed | - | - | - | - | |\n| mvp2_eval_lr5e6_r1_ckpt60_r2 | DONE | negative | - | 0.0093 | 0.81 | 0.993 | |\n| mvp2_eval_lr5e6_r1_ckpt80 | DONE | negative | 0.0116 | 0.0116 | 0.828 | 0.993 | |\n| mvp2_eval_lr5e6_r1_ckpt100 | DONE | negative | 0.0138 | 0.0138 | 0.8504 | 0.9876 | |\n| mvp2_eval_lr5e6_rp_r2_ckpt20 | DONE | killed | - | - | - | - | recall_penalty variant, killed |\n\n### GRPO bf16 Evals (forgetting fixed)\n\n| experiment_id | status | conclusion | ign_f1 | rel_f1 | evi_f1 | edcr | notes |\n|---|---|---|---|---|---|---|---|\n| eval_grpo_g8_bf16 | DONE | success | - | - | - | - | ckpt80: 0.4456, ckpt90: 0.4523, ckpt100: 0.4549. Best=ckpt-100 |\n| plan_011_grpo_g8_bf16_eval | DONE | success | 0.4549 | 0.4549 | 0.8086 | 0.6318 | ckpt-100 |\n| plan_011_bf16_g8_step_eval | DONE | success | - | - | - | - | step_30=0.434, step_50=0.4276, step_70=0.4341 |\n| plan_011_eval_g8_bf16_ckpt100 | DONE | killed | - | - | - | - | |\n| grpo_bf16_g4_ckpt100_eval | DONE | success | 0.4431 | - | 0.801 | 0.6453 | f1=0.4511 |\n| grpo_bf16_g4_ckpt200_eval | DONE | success | 0.4446 | 0.4513 | 0.8053 | 0.6489 | |\n\n### RSFT->GRPO (Lead2) Eval\n\n| experiment_id | status | conclusion | ign_f1 | rel_f1 | evi_f1 | edcr | evi_f1_joint | notes |\n|---|---|---|---|---|---|---|---|---|\n| lead2_ckpt20_eval | DONE | success | 0.4533 | 0.4617 | 0.8103 | 0.6465 | 0.3642 | Preserves RSFT baseline |\n\n### Re-DocRED Transfer Evals\n\n| experiment_id | status | conclusion | ign_f1 | f1 | evi_f1 | edcr | notes |\n|---|---|---|---|---|---|---|---|\n| plan_007_redocred_4b_sft_eval | DONE | failed | - | - | - | - | |\n| plan_007_redocred_4b_sft_eval_r2 | DONE | success | 0.3659 | 0.3706 | 0.817 | 0.6674 | |\n| plan_007_redocred_rsft_eval | DONE | failed | - | - | - | - | OOM + pipeline bug |\n| plan_007_redocred_rsft_eval_r2 | DONE | negative | 0.0026 | - | 0.8837 | 0.9978 | Wrong model loading |\n| plan_007_redocred_rsft_eval_r3 | DONE | failed | - | - | - | - | |\n| plan_007_redocred_rsft_eval_r4 | DONE | failed | - | - | - | - | |\n| plan_007_redocred_rsft_eval_r5 | DONE | success | 0.4145 | 0.4234 | 0.8182 | 0.621 | Correct 3-param loading |\n\n### Test Set Eval\n\n| experiment_id | status | conclusion | notes |\n|---|---|---|---|\n| plan_002_test_eval_s44 | DONE | failed | |\n| plan_002_test_eval_s44_r2 | DONE | success | No metrics in registry (test set for paper) |\n\n### Reward Variant Evals\n\n| experiment_id | status | conclusion | notes |\n|---|---|---|---|\n| plan_009_extract_reward_eval | DONE | failed | |\n| plan_009_flatnli_reward_eval | DONE | failed | |\n| plan_009_flatnli_reward_eval_r2 | DONE | failed | |\n\n---\n\n## NO_EVIDENCE experiments\n\n| experiment_id | status | conclusion | ign_f1 | rel_f1 | evi_f1 | notes |\n|---|---|---|---|---|---|---|\n| eval_plan_014_no_evidence | DONE | failed | - | - | - | |\n| eval_plan_014_no_evidence_r2 | DONE | success | 0.4721 | 0.4876 | 0 | 4B no-evi |\n| eval_plan_014_sft_no_evidence | DONE | success | - | 0.4893 | 0 | rel_ign_f1=0.4893 |\n| plan_014_no_evidence_eval_d076 | DONE | success | 0.4721 | - | - | D076 protocol |\n| plan017_14b_sft_no_evidence_eval | DONE | killed | - | - | - | 14B |\n| plan_006_qwen3_1_7b_no_evidence_eval | DONE | failed | 0.3786 | - | 0.0007 | 1.7B (wrong eval) |\n| plan_006_qwen3_1_7b_no_evidence_eval_v2 | DONE | failed | - | - | - | |\n| plan_006_qwen3_1_7b_no_evidence_eval_v2r2 | DONE | failed | - | - | - | |\n| plan_006_qwen3_1_7b_no_evidence_eval_v3 | DONE | success | 0.3982 | 0.4103 | 0 | evidence_tax=0.0804 |\n| plan_006_qwen3_8b_no_evidence_eval | DONE | killed | - | - | - | |\n| plan_006_qwen3_8b_no_evidence_eval_v2 | DONE | success | - | - | - | (no metrics in registry) |\n| plan_016_llama_3_1_8b_no_evidence_eval | DONE | success | 0.5452 | 0.5624 | 0 | LLaMA 8B |\n| plan_006_qwen3_1_7b_no_evidence_sft | DONE | success | - | - | - | Training only |\n| plan_006_qwen3_8b_no_evidence_sft | DONE | success | - | - | - | Training only |\n| plan_014_sft_no_evidence | DONE | success | - | - | - | Training only |\n| plan_016_llama_3_1_8b_no_evidence_sft | DONE | success | - | - | - | Training only |\n\n---\n\n## RANDOM_RSFT experiments\n\n| experiment_id | status | conclusion | ign_f1 | f1 | evi_f1 | edcr | notes |\n|---|---|---|---|---|---|---|---|\n| random_rsft_k1_baseline | DONE | success | - | - | - | - | Training: loss=0.578, 3 epochs |\n| random_rsft_k1_eval | DONE | success | 0.4114 | 0.4198 | 0.7964 | 0.6971 | CED RSFT mean=0.4596 >> random 0.4198, gap=~4pp proves CED scoring precision matters |\n\n---\n\n## GRPO experiments (non-eval, training runs)\n\n| experiment_id | status | conclusion | notes |\n|---|---|---|---|\n| smoke_test_grpo | DONE | success | |\n| mvp2_grpo_ced | DONE | failed | |\n| mvp2_grpo_ced_r1 | DONE | killed | |\n| mvp2_grpo_ced_r2 | DONE | killed | |\n| mvp2_grpo_ced_r3 | DONE | failed | kl_coef=0.05 |\n| mvp2_grpo_ced_r4 | DONE | killed | |\n| mvp2_grpo_ced_r5 | DONE | negative | |\n| mvp2_grpo_ced_kl001 | DONE | failed | kl_coef=0.01 |\n| mvp2_grpo_ced_kl001_r2 | DONE | killed | |\n| mvp2_grpo_ced_kl001_r3 | DONE | killed | |\n| mvp2_grpo_ced_kl001_r4 | DONE | success | 100 steps, best_reward=1.37 at step 90 |\n| mvp2_grpo_ced_lr5e6_r1 | DONE | killed | lr=5e-6 |\n| mvp2_grpo_ced_lr5e6_p1_r1 | DONE | killed | lr=5e-6 + recall_penalty |\n| mvp2_grpo_ced_lr5e6_rp_r1 | DONE | failed | |\n| mvp2_grpo_ced_lr5e6_rp_r2 | DONE | killed | |\n| mvp2_grpo_extract | DONE | failed | Extraction-only reward |\n| mvp2_grpo_extract_r2 | DONE | killed | |\n| mvp2_grpo_extract_r3 | DONE | negative | |\n| mvp2_grpo_extract_r4 | DONE | killed | |\n| mvp2_grpo_flatnli | DONE | failed | |\n| mvp2_grpo_flatnli_r2 | DONE | killed | |\n| mvp2_grpo_flatnli_r3 | DONE | killed | |\n| mvp2_grpo_flatnli_r4 | DONE | killed | |\n| mvp2_grpo_flatnli_r5 | DONE | killed | |\n| mvp2_grpo_flatnli_r6 | DONE | negative | Collapsed at step 25 |\n| plan_011_grpo_g8_bf16 | DONE | success | bf16, 100 steps, no mode collapse |\n| plan_015_grpo_g4_bf16 | DONE | killed | |\n| plan_015_grpo_g4_bf16_v2 | DONE | killed | |\n| plan_015_grpo_g4_bf16_v3 | DONE | killed | |\n| plan_016_llama_grpo_qlora | DONE | success | Catastrophic decoupling confirmed cross-family (format=1, f1=0, ced=0) |\n| lead2_rsft_grpo_ced | DONE | failed | RSFT->GRPO two-stage |\n| lead2_rsft_grpo_ced_r2 | DONE | failed | RSFT->GRPO retry |\n| wave1_grpo_bf16_g4 | DONE | success | 200 steps, reward=1.7646 |\n\n---\n\n**Total: 149 matching experiments** (out of 242 in registry)."
      }
    ],
    "totalDurationMs": 172735,
    "totalTokens": 68339,
    "totalToolUseCount": 11,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2365,
      "cache_read_input_tokens": 58321,
      "output_tokens": 7652,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2365
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7652,
          "cache_read_input_tokens": 58321,
          "cache_creation_input_tokens": 2365,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2365,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 6,
      "searchCount": 0,
      "bashCount": 5,
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
