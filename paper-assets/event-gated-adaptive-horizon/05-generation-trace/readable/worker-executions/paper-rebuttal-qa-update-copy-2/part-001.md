# paper rebuttal qa update — Part 1 of 2

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Worker execution logs

[Transcript overview](../paper-rebuttal-qa-update-copy-2.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/02/022c3aceabfb41eddc2f.json)

## Before a recorded user message

## Before a recorded user message

187 recorded events


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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon",
  "session_id": "ae813a79-db9f-4a12-b6ee-ad91ade39065",
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
  "uuid": "16f123d6-b57f-49fb-baba-fba585462f76",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/memory/"
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
    "resetsAt": 1779725400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "c2b07cdd-6f1b-451a-a0c9-e662e85f63a4",
  "session_id": "ae813a79-db9f-4a12-b6ee-ad91ade39065"
}
```

---


### Assistant

_source line 4_

I'll start by reading the rebuttal Q&A and the registry in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ae813a79-db9f-4a12-b6ee-ad91ade39065",
  "uuid": "93fff63d-a211-4a20-982f-f51693334f02",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LH6bm2oXyThetVBUJRx7Bw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11961,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11961
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


### Tool call

_source line 5_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_018cTFAAENthc6EkaUXGNgiJ`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_registry",
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
  "session_id": "ae813a79-db9f-4a12-b6ee-ad91ade39065",
  "uuid": "008794b3-0a02-4a56-a513-a2d655588c6c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LH6bm2oXyThetVBUJRx7Bw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11961,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11961
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

_source line 6 · 2026-05-25T14:11:06.691Z_

<details><summary>↩ Tool result · `toolu_018cTFAAENthc6EkaUXGNgiJ`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_project_file"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_registry"
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
  "session_id": "ae813a79-db9f-4a12-b6ee-ad91ade39065",
  "uuid": "e33df801-8065-4b63-8296-700efde6d69d",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_registry",
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
Now I'll call both tools in parallel to get the rebuttal Q&A and the registry.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ae813a79-db9f-4a12-b6ee-ad91ade39065",
  "uuid": "194639d7-731c-465f-8a30-5be1a809faf3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HDX2YZTfFvmZPs1BXHy6gG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 800,
      "cache_read_input_tokens": 23408,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 800
      },
      "output_tokens": 24,
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Pu5kvG8evzH4yJwrd6fedg`</summary>

```json
{
  "project": "event-gated-adaptive-horizon",
  "file": "rebuttal_qa.md",
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
  "session_id": "ae813a79-db9f-4a12-b6ee-ad91ade39065",
  "uuid": "c8c916d6-f4fc-4188-a3f7-183f1aee0a53",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HDX2YZTfFvmZPs1BXHy6gG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 800,
      "cache_read_input_tokens": 23408,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 800
      },
      "output_tokens": 24,
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

_source line 9 · 2026-05-25T14:11:11.858Z_

<details><summary>↩ Tool result · `toolu_01Pu5kvG8evzH4yJwrd6fedg`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'rebuttal_qa.md'\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ae813a79-db9f-4a12-b6ee-ad91ade39065",
  "uuid": "6556beb1-2fd5-43bd-bb6e-37f504e00c3c",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'rebuttal_qa.md'\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'rebuttal_qa.md'\", \"metadata\": {}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 10_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01W1eBaAHntCpzzHgAEKnEqH`</summary>

```json
{
  "project": "event-gated-adaptive-horizon",
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
  "session_id": "ae813a79-db9f-4a12-b6ee-ad91ade39065",
  "uuid": "7c8e9def-7710-4dec-b00b-12d04c3823b1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HDX2YZTfFvmZPs1BXHy6gG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 800,
      "cache_read_input_tokens": 23408,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 800
      },
      "output_tokens": 24,
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

_source line 11 · 2026-05-25T14:11:12.807Z_

<details><summary>↩ Tool result · `toolu_01W1eBaAHntCpzzHgAEKnEqH`</summary>

```text
Error: result (154,085 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/ae813a79-db9f-4a12-b6ee-ad91ade39065/tool-results/mcp-agent-ml-research-read_registry-1779718272790.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/ae813a79-db9f-4a12-b6ee-ad91ade39065/tool-results/mcp-agent-ml-research-read_registry-1779718272790.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ae813a79-db9f-4a12-b6ee-ad91ade39065",
  "uuid": "c50dba0b-f799-4690-9559-14912e2074f4",
  "tool_use_result": {
    "content": "Error: result (154,085 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/ae813a79-db9f-4a12-b6ee-ad91ade39065/tool-results/mcp-agent-ml-research-read_registry-1779718272790.txt.\nFormat: JSON with schema: {result: string}\nUse offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.\nREQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:\n- You MUST read the content from the file at /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/ae813a79-db9f-4a12-b6ee-ad91ade39065/tool-results/mcp-agent-ml-research-read_registry-1779718272790.txt in sequential chunks until 100% of the content has been read.\n- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.\n- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***\n",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"exp_082_cheetah_no_dt_emb_s0\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-25T13:12:29.199Z\", \"updated_at\": \"2026-05-25T14:10:44.478Z\", \"hypothesis\": \"Cheetah Run causal control: dt_embed_dim=0 + subsample ON + dt=2 + H=8, seed=0。移除 dt_embedding 后预期无 CIVO，证明 trained dt_emb 是 Cheetah CIVO 的必要条件。与 exp_078 (trained dt_emb, CIVO trigger) 构成因果对。plan_022。\", \"parent\": \"exp_010b_cheetah_civo_trigger\"}, \"exp_077_cheetah_baseline_s0\": {\"status\": \"ANALYZING\", \"created_at\": \"2026-05-25T10:48:21.685Z\", \"updated_at\": \"2026-05-25T14:07:48.511Z\", \"hypothesis\": \"Cheetah Run dt=1 baseline seed=0。建立 v/e ratio 校准基线，用于归一化同时运行的 exp_078 (Cheetah 008d) 的 VE。plan_020 第一个 seed。\"}, \"exp_081_008e_v3_walker_s2\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-25T12:09:44.566Z\", \"updated_at\": \"2026-05-25T12:49:21.343Z\", \"hypothesis\": \"Walker Walk 008e_v3 mitigation seed=2: trained dt_emb + subsample ON (max_dt=2) + dt=1 imagination + H=15。C6 mitigation 第 3 seed，与 seed 0 (success, 95% baseline) 和 seed 1 (exp_080, running) 构成统计三角。plan_014。\", \"parent\": \"exp_008e_v3_subsample_on_dt1_h15\"}, \"exp_080_008e_v3_walker_s1\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-25T11:30:20.594Z\", \"updated_at\": \"2026-05-25T12:49:19.083Z\", \"hypothesis\": \"Walker Walk 008e_v3 mitigation seed=1: trained dt_emb + subsample ON (max_dt=2) + dt=1 imagination + H=15。C6 mitigation 多 seed 验证——trained dt_emb 在 dt=1 imagination 下不触发 CIVO。重跑因旧 exp_008e_v3_walker_s1 metrics 疑似复制自 seed 0。plan_014。\", \"parent\": \"exp_008e_v3_subsample_on_dt1_h15\"}, \"exp_074_008a_walker_s3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-25T09:08:57.028Z\", \"updated_at\": \"2026-05-25T12:08:22.221Z\", \"hypothesis\": \"Walker Walk 008a 配置 (trained dt_emb unexposed + subsample OFF + dt=2 + H=15) seed=3。当前 008a 3 seeds 全部 success (no CIVO)，加 seed=3 巩固 C3 value suppression claim 统计。来源: plan_013 扩展。\", \"parent\": \"exp_008a_no_subsample_dt2\", \"conclusion\": \"success\", \"metrics\": {\"eval_return_105K\": 855.9, \"civo_ve_ratio_final\": 0.3, \"civo_alert\": 0, \"value_mean_105K\": 295.2, \"gate_dt_2_frac\": 1, \"gate_dt_mean\": 2, \"model_loss_105K\": 3.8, \"eval_trajectory\": {\"5K\": 36.1, \"15K\": 281, \"25K\": 389.8, \"35K\": 303.8, \"45K\": 437.3, \"55K\": 411.3, \"65K\": 566.4, \"75K\": 513.9, \"85K\": 645.9, \"95K\": 776.6, \"105K\": 855.9}, \"four_seed_summary\": {\"mean_eval_return\": 791, \"std_eval_return\": 102.2, \"all_civo_alert_0\": true, \"seeds_completed\": 4}}}, \"exp_079_frozen_dt_emb_walker_s0\": {\"status\": \"DONE\", \"created_at\": \"2026-05-25T10:48:27.865Z\", \"updated_at\": \"2026-05-25T11:28:10.029Z\", \"hypothesis\": \"Walker Walk frozen dt_emb (requires_grad=False, random init) + subsample ON + dt=2 + H=8, seed=0。验证 dt_emb 的 TRAINING 是 CIVO 必要条件。2×2 ablation 矩阵关键格。plan_015。\", \"parent\": \"exp_067_frozen_dt_emb_walker_plan015\", \"conclusion\": \"killed\"}, \"exp_078_cheetah_008d_s0\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-25T10:48:24.844Z\", \"updated_at\": \"2026-05-25T11:21:52.244Z\", \"hypothesis\": \"Cheetah Run CIVO trigger seed=0: trained dt_emb + subsample ON + dt=2 + H=8。与 exp_077 baseline 同时运行以计算 step-matched normalized VE。plan_021 第一个 seed。\", \"parent\": \"exp_010b_cheetah_civo_trigger\"}, \"exp_076_cheetah_civo_trigger_s3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-25T10:03:42.328Z\", \"updated_at\": \"2026-05-25T10:48:15.566Z\", \"hypothesis\": \"Cheetah Run CIVO trigger seed=2: trained dt_emb + subsample ON + dt=2 + H=8。将 Cheetah CIVO trigger 扩展到第 3 个独立 seed，巩固跨环境 claim 统计力度。来源: plan_021 扩展。\", \"parent\": \"exp_010b_cheetah_civo_trigger\", \"conclusion\": \"killed\"}, \"exp_075_cheetah_civo_trigger_s2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-25T10:03:40.222Z\", \"updated_at\": \"2026-05-25T10:48:13.465Z\", \"hypothesis\": \"Cheetah Run CIVO trigger seed=1: trained dt_emb + subsample ON + dt=2 + H=8 on westd-19154。复现 exp_010b 配置（原 seed=1 在 bjb1-45299），跨服务器验证 Cheetah CIVO 可复现性。来源: plan_021 扩展。\", \"parent\": \"exp_010b_cheetah_civo_trigger\", \"conclusion\": \"killed\"}, \"exp_071_008f_walker_s3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-25T07:03:48.097Z\", \"updated_at\": \"2026-05-25T10:42:39.889Z\", \"hypothesis\": \"Walker Walk 008f 配置 (no dt_emb, dt_embed_dim=0 + subsample ON + dt=2 + H=8) seed=3。当前 008f 2 seeds 结果分歧（s1=success eval=503, s2=negative eval=148），增加 seed 缩窄 causal control 稳定性估计。来源: plan_012 扩展。\", \"parent\": \"exp_008f_no_dt_embed_subsample_on_h8\", \"conclusion\": \"success\", \"metrics\": {\"eval_return_final\": 311.9, \"eval_return_peak\": 457.7, \"ve_ratio_final\": 0.4, \"ve_ratio_peak\": 0.7, \"gate_dt_mean_final\": 2, \"civo_alert\": 0, \"value_loss_final\": 1, \"actor_entropy_final\": -4.6, \"model_loss_final\": 4.5}}, \"exp_073_008f_walker_s4\": {\"status\": \"DONE\", \"created_at\": \"2026-05-25T07:30:42.251Z\", \"updated_at\": \"2026-05-25T10:00:42.604Z\", \"hypothesis\": \"Walker Walk 008f 配置 (no dt_emb, dt_embed_dim=0 + subsample ON + dt=2 + H=8) seed=4。当前 008f 0/3 CIVO onset，扩到 seed=4 进一步巩固 control 组统计。来源: plan_012 扩展。\", \"parent\": \"exp_008f_no_dt_embed_subsample_on_h8\", \"conclusion\": \"success\", \"metrics\": {\"eval_return_final\": 289.3, \"eval_return_peak\": 486.5, \"eval_return_peak_step\": 75000, \"ve_ratio_final\": 0.5, \"ve_ratio_peak\": 0.5, \"nve_peak\": 0.76, \"civo_alert\": 0, \"civo\": false, \"gate_dt_2_frac\": 1, \"gate_dt_mean\": 2, \"gate_empirical_entropy\": 0, \"eval_trajectory\": [{\"step\": 5000, \"eval_return\": 33.2}, {\"step\": 15000, \"eval_return\": 128.3}, {\"step\": 25000, \"eval_return\": 165.3}, {\"step\": 35000, \"eval_return\": 284.5}, {\"step\": 45000, \"eval_return\": 272.5}, {\"step\": 55000, \"eval_return\": 406.7}, {\"step\": 65000, \"eval_return\": 379.5}, {\"step\": 75000, \"eval_return\": 486.5}, {\"step\": 85000, \"eval_return\": 352.6}, {\"step\": 95000, \"eval_return\": 297.7}, {\"step\": 105000, \"eval_return\": 289.3}]}}, \"exp_072_008e_v3_walker_s5\": {\"status\": \"DONE\", \"created_at\": \"2026-05-25T07:24:08.174Z\", \"updated_at\": \"2026-05-25T10:00:39.306Z\", \"hypothesis\": \"Walker Walk 008e_v3 mitigation 配置 (trained dt_emb + subsample ON + dt=1 imag + H=15) seed=5。当前 5 seeds 测试 collapse rate=2/5 (40%)，加 seed=5 缩窄置信区间。来源: plan_016 扩展。\", \"parent\": \"exp_008e_v3_subsample_on_dt1_h15\", \"conclusion\": \"success\", \"metrics\": {\"eval_return_final\": 853.1, \"eval_return_peak\": 853.1, \"eval_return_peak_step\": 105000, \"ve_ratio_final\": 0.6, \"nve_final\": 0.61, \"nve_peak\": 0.61, \"nve_peak_step\": 105000, \"civo_alert\": 0, \"civo\": false, \"gate_dt_1_frac\": 1, \"gate_dt_mean\": 1, \"actor_entropy_final\": -5.1, \"value_mean_final\": 520.8, \"eval_trajectory\": [{\"step\": 5000, \"eval_return\": 29.4}, {\"step\": 15000, \"eval_return\": 251.1}, {\"step\": 25000, \"eval_return\": 423}, {\"step\": 35000, \"eval_return\": 511}, {\"step\": 45000, \"eval_return\": 600.1}, {\"step\": 55000, \"eval_return\": 649}, {\"step\": 65000, \"eval_return\": 697.2}, {\"step\": 75000, \"eval_return\": 727.3}, {\"step\": 85000, \"eval_return\": 710.3}, {\"step\": 95000, \"eval_return\": 803.9}, {\"step\": 105000, \"eval_return\": 853.1}]}}, \"exp_070_008e_v3_walker_s0\": {\"status\": \"DONE\", \"created_at\": \"2026-05-25T05:07:49.050Z\", \"updated_at\": \"2026-05-25T08:54:47.019Z\", \"hypothesis\": \"Walker Walk 008e_v3 mitigation 配置 (trained dt_emb + subsample ON + dt=1 imag + H=15) seed=0。当前 4 unique seeds 测试结果 collapse rate=2/4 (50%)，加 seed=0 缩窄置信区间。来源: plan_016 扩展。\", \"parent\": \"exp_008e_v3_subsample_on_dt1_h15\", \"metrics\": {\"eval_return\": 148, \"peak_eval_return\": 232.5, \"peak_eval_step\": 55000, \"ve_ratio_105k\": 0.8, \"nve_peak\": 0.8, \"nve_peak_step\": 95000, \"civo\": false, \"gate_dt_1_frac\": 1, \"gate_dt_mean\": 1, \"actor_entropy_final\": -3.7, \"value_mean_final\": 122.1, \"failure_mode\": \"non-CIVO learning failure (never reached baseline performance)\", \"eval_trajectory\": [{\"step\": 5000, \"eval_return\": 37.4}, {\"step\": 15000, \"eval_return\": 93.2}, {\"step\": 25000, \"eval_return\": 178.8}, {\"step\": 35000, \"eval_return\": 221.6}, {\"step\": 45000, \"eval_return\": 230.9}, {\"step\": 55000, \"eval_return\": 232.5}, {\"step\": 65000, \"eval_return\": 194}, {\"step\": 75000, \"eval_return\": 175.2}, {\"step\": 85000, \"eval_return\": 218.6}, {\"step\": 95000, \"eval_return\": 139.6}, {\"step\": 105000, \"eval_return\": 148}], \"ve_ratio_trajectory\": [{\"step\": 15000, \"ve\": 0}, {\"step\": 25000, \"ve\": 0.1}, {\"step\": 35000, \"ve\": 0.2}, {\"step\": 45000, \"ve\": 0.3}, {\"step\": 55000, \"ve\": 0.4}, {\"step\": 65000, \"ve\": 0.5}, {\"step\": 75000, \"ve\": 0.6}, {\"step\": 85000, \"ve\": 0.5}, {\"step\": 95000, \"ve\": 0.8}, {\"step\": 105000, \"ve\": 0.8}]}, \"conclusion\": \"negative\", \"notes\": \"Seed 0 FAILED but NOT via CIVO. eval_return peaked at 232.5@55K (far below baseline ~500+), declined to 148@105K. ve_ratio stayed healthy throughout (max 0.8, never triggered CIVO alert). Gate locked dt=1. This is a distinct failure mode from seeds 2,3 (which had CIVO collapse with NVE>3.7x). Agent never reached high performance — learning stagnated early. Cross-seed 008e_v3 summary: 5 seeds tested, 2 success (s1=870, s4=899), 2 CIVO collapse (s2=137 NVE=3.78, s3=93 NVE=4.02), 1 non-CIVO failure (s0=148 NVE=0.8). CIVO collapse rate: 2/5=40%. Overall failure rate: 3/5=60%.\"}, \"exp_069_008f_walker_repro_s1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-25T03:49:41.282Z\", \"updated_at\": \"2026-05-25T07:28:33.676Z\", \"hypothesis\": \"Reproducing 008f config (no dt_emb, dt_embed_dim=0 + subsample ON + dt=2 + H=8) on Walker Walk seed=1 will NOT trigger CIVO (NVE < 1.5x) because removing dt_emb eliminates the temporal abstraction mismatch that drives value error amplification\", \"parent\": \"exp_008f_no_dt_embed_subsample_on_h8\", \"metrics\": {\"eval_return_final\": 237.8, \"eval_return_peak\": 390.1, \"eval_return_peak_step\": 95000, \"ve_ratio_final\": 0.4, \"ve_ratio_peak\": 0.4, \"ve_ratio_peak_step\": 105000, \"nve_final_105k\": 0.61, \"nve_peak\": 0.66, \"nve_peak_step\": 75000, \"civo_alert\": false, \"gate_dt_2_frac\": 1, \"eval_trajectory\": {\"5k\": 30.5, \"15k\": 158.7, \"25k\": 180.8, \"35k\": 250.3, \"45k\": 293.6, \"55k\": 272.2, \"65k\": 328.1, \"75k\": 244.8, \"85k\": 382.5, \"95k\": 390.1, \"105k\": 237.8}, \"ve_ratio_trajectory\": {\"15k\": 0, \"25k\": 0.1, \"35k\": 0.2, \"45k\": 0.2, \"55k\": 0.3, \"65k\": 0.3, \"75k\": 0.4, \"85k\": 0.3, \"95k\": 0.3, \"105k\": 0.4}}, \"conclusion\": \"success\"}, \"exp_068_008d_walker_repro_s1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-25T03:49:39.539Z\", \"updated_at\": \"2026-05-25T07:28:31.319Z\", \"hypothesis\": \"Reproducing 008d config (trained dt_emb + subsample ON + dt=2 + H=8) on Walker Walk seed=1 will trigger CIVO (NVE > 1.5x) because trained dt_emb enables value error amplification through temporal abstraction mismatch\", \"parent\": \"exp_008d_subsample_on_h8\", \"metrics\": {\"eval_return_final\": 39.1, \"eval_return_peak\": 192.4, \"eval_return_peak_step\": 55000, \"ve_ratio_final\": 2.7, \"ve_ratio_peak\": 4.6, \"ve_ratio_peak_step\": 85000, \"nve_final_105k\": 4.12, \"nve_peak_85k\": 6.57, \"nve_onset_step\": 45000, \"nve_onset_value\": 1.81, \"civo_alert\": true, \"civo_alert_step\": 85000, \"gate_dt_2_frac\": 1, \"eval_trajectory\": {\"5k\": 31, \"15k\": 146.5, \"25k\": 174.1, \"35k\": 189.6, \"45k\": 142.2, \"55k\": 192.4, \"65k\": 114.4, \"75k\": 106.6, \"85k\": 33.4, \"95k\": 26.9, \"105k\": 39.1}, \"ve_ratio_trajectory\": {\"15k\": 0, \"25k\": 0.2, \"35k\": 0.3, \"45k\": 0.6, \"55k\": 0.6, \"65k\": 1.3, \"75k\": 1.6, \"85k\": 4.6, \"95k\": 4.6, \"105k\": 2.7}}, \"conclusion\": \"success\"}, \"exp_067_frozen_dt_emb_walker_plan015\": {\"status\": \"DONE\", \"created_at\": \"2026-05-25T03:49:37.736Z\", \"updated_at\": \"2026-05-25T06:59:24.006Z\", \"hypothesis\": \"Frozen (requires_grad=False) dt_embedding + subsample ON + dt=2 + H=8 在 Walker Walk 上不触发 CIVO，验证 dt_emb 的 TRAINING 是 CIVO 的必要条件（而非 dt_emb 的存在本身）。来源: plan_015。\", \"parent\": \"exp_042_frozen_dt_emb_walker\", \"metrics\": {\"eval_final\": 281.5, \"eval_peak\": 334.1, \"eval_peak_step\": 95000, \"nve_peak\": 0.4, \"nve_final\": 0.2, \"civo_alert\": 0, \"total_env_steps\": 112000, \"update_count\": 25099, \"gate_dt_mean\": 2, \"gate_dt_std\": 0, \"gate_dt_2_frac\": 1, \"gate_empirical_entropy\": 0}, \"conclusion\": \"success\"}, \"exp_066b_timeseries_rssm_fidelity_s1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-25T02:34:14.574Z\", \"updated_at\": \"2026-05-25T04:35:12.673Z\", \"hypothesis\": \"RSSM fidelity gap (dt=2 prediction error > dt=1) emerges before value overestimation in seed=1, replicating the causal chain found in exp_066 seed=0 and confirming cross-seed robustness of the fidelity→VE mechanism.\", \"parent\": \"exp_066_timeseries_rssm_fidelity\", \"metrics\": {\"seed\": 1, \"steps_completed\": 65000, \"eval_return_peak\": 201.9, \"eval_return_peak_step\": 45000, \"eval_return_final\": 160.7, \"civo_alert_step\": 55000, \"ve_ratio_final\": 0.724, \"fidelity_gap_timeseries\": {\"ss_ratio_10K\": 0.887, \"ss_ratio_15K\": 1.017, \"ss_ratio_20K\": 1.216, \"ss_ratio_25K\": 1.532, \"ss_ratio_30K\": 1.374, \"ss_ratio_35K\": 1.486, \"ss_ratio_40K\": 1.428, \"ss_ratio_45K\": 1.38, \"ss_ratio_50K\": 1.468, \"ss_ratio_55K\": 1.517, \"ss_ratio_60K\": 1.799, \"ss_ratio_65K\": 1.756}, \"ve_ratio_timeseries\": {\"12K\": 0.012, \"15K\": 0.033, \"24K\": 0.118, \"25K\": 0.193, \"35K\": 0.269, \"45K\": 0.358, \"52K\": 0.495, \"55K\": 0.71, \"64K\": 0.724}, \"fidelity_gap_onset_step\": 15000, \"ve_onset_step\": 24000, \"temporal_lead_steps\": 9000, \"causal_direction\": \"fidelity_gap_leads_ve\", \"cross_seed_comparison\": {\"s0_ss_ratio_65K\": 1.678, \"s1_ss_ratio_65K\": 1.756, \"s0_fidelity_onset\": 20000, \"s1_fidelity_onset\": 15000, \"s0_ve_onset\": 30000, \"s1_ve_onset\": 24000, \"s0_temporal_lead\": 10000, \"s1_temporal_lead\": 9000, \"pattern_consistent\": true}}, \"conclusion\": \"success\"}, \"exp_062_cartpole_control\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T16:01:08.858Z\", \"updated_at\": \"2026-05-25T03:45:35.194Z\", \"hypothesis\": \"dt_embed_dim=0 + subsample ON + H=8 在 Cartpole Swingup 上不触发 CIVO（NVE < 1.5x），因果控制实验验证移除 dt_emb 是否阻止 CIVO 在第三个环境中泛化。与 exp_061 配对形成因果对比。\", \"metrics\": {\"seeds\": {\"s0\": {\"eval_return\": 230.4, \"ve_ratio_peak\": 0.069, \"ve_ratio_final\": 0.056, \"value_mean\": 12.9, \"civo_detected\": false}, \"s1\": {\"eval_return\": 255.3, \"ve_ratio_peak\": 0.079, \"ve_ratio_final\": 0.04, \"value_mean\": 10.2, \"civo_detected\": false}, \"s2\": {\"eval_return\": 248.8, \"ve_ratio_peak\": 0.065, \"ve_ratio_final\": 0.048, \"value_mean\": 11.8, \"civo_detected\": false}}, \"mean_eval_return\": 244.8, \"mean_ve_ratio_peak\": 0.071, \"civo_detected_any\": false, \"steps_completed\": 112000}, \"conclusion\": \"negative\"}, \"exp_061_cartpole_civo_trigger\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T16:01:07.009Z\", \"updated_at\": \"2026-05-25T03:18:38.759Z\", \"hypothesis\": \"Trained dt_emb (d=32) + subsample ON + H=8 + dt=2 imagination 在 Cartpole Swingup 上触发 CIVO（NVE > 1.5x），验证 CIVO 是否跨 locomotion 子类环境泛化（Walker/Cheetah 已确认，Cartpole 是第三个 DMC locomotion 环境）。与 exp_062 配对形成因果对比。\", \"conclusion\": \"negative\", \"metrics\": {\"seeds\": 3, \"steps_per_seed\": 112000, \"s0_eval_return_final\": 211.1, \"s0_eval_return_peak\": 247.8, \"s0_value_mean_final\": 9.229, \"s0_ve_ratio_peak\": 0.058, \"s0_train_return_final\": 199.2, \"s1_eval_return_final\": 269, \"s1_eval_return_peak\": 328.1, \"s1_value_mean_final\": 9.323, \"s1_ve_ratio_peak\": 0.04, \"s1_train_return_final\": 188.7, \"s2_eval_return_final\": 228.9, \"s2_eval_return_peak\": 245.9, \"s2_value_mean_final\": 9.46, \"s2_ve_ratio_peak\": 0.043, \"s2_train_return_final\": 258.9, \"civo_detected\": false, \"civo_alert_any_seed\": false, \"ve_ratio_max_all_seeds\": 0.058, \"vs_baseline_eval_mean\": \"-56.3%\", \"baseline_exp060_eval_s2_105K\": 557}}, \"exp_008d_subsample_on_h8\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-14T01:46:57.960Z\", \"hypothesis\": \"Trained dt-embedding with subsample (gate_fixed_dt=2, gate_subsample_max_dt=2) causes critic value function to overestimate through dt-conditioned representation co-adaptation, leading to policy collapse.\", \"metrics\": {\"actor_loss_25K\": -0.195, \"actor_loss_35K\": -0.17, \"baseline_35K\": 400, \"baseline_45K\": 443, \"data_source_45K\": \"from training logs metrics.jsonl\", \"eval_return_25K\": 167.22, \"eval_return_35K\": 146.34, \"eval_return_45K\": 140.8, \"eval_return_55K\": 82.75, \"model_loss_25K\": 5.33, \"model_loss_35K\": 5.07, \"step\": 55000, \"trend\": \"eval declining 167→146→141→83; v/e accelerating 15.5%→41.2%→69.3%→167% — delusional critic collapse confirmed, value exceeds eval_return at 55K\", \"value_eval_ratio_25K\": 0.155, \"value_eval_ratio_35K\": 0.411, \"value_eval_ratio_45K\": 0.693, \"value_eval_ratio_55K\": 1.666, \"value_mean_25K\": 25.86, \"value_mean_35K\": 60.2, \"value_mean_45K\": 97.5, \"value_mean_55K\": 137.88, \"verdict_35K\": \"WARN_COLLAPSE\", \"verdict_45K\": \"COLLAPSE_CONFIRMED\", \"vs_baseline_35K\": \"-63.4%\", \"vs_baseline_45K\": \"-68.2%\"}, \"parent\": \"exp_005_event_gated_v4\", \"status\": \"DONE\", \"updated_at\": \"2026-05-25T02:41:05.620Z\", \"notes\": \"RSSM fidelity analysis (exp_063, 55K checkpoint only): dt=2/dt=1 single-step reward MAE ratio = 2.695x (vs exp_066 s0's 1.37x at same step). Larger fidelity gap correlates with worse VE (1.666 vs 0.621). No intermediate checkpoints exist — cannot directly verify 25K fidelity gap for this seed. Cross-seed pattern consistent: VE trajectory matches s0 (low at 25K, collapse by 55K). See artifact art_20260525_e45921.\"}, \"exp_066_timeseries_rssm_fidelity\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T21:07:53.125Z\", \"updated_at\": \"2026-05-25T02:33:00.783Z\", \"hypothesis\": \"Trained dt_embedding causes RSSM fidelity degradation (dt=2 vs dt=1 reward MAE gap) that progressively worsens during training, and its temporal evolution precedes or synchronizes with NVE (value overestimation) rise, establishing a temporal causal chain: RSSM fidelity gap → value overestimation.\", \"parent\": \"exp_063_rssm_fidelity\", \"conclusion\": \"success\", \"metrics\": {\"ss_ratio_10K\": 1.047, \"ss_ratio_30K\": 1.247, \"ss_ratio_65K\": 1.678, \"ol_ratio_30K_peak\": 1.446, \"ol_ratio_35K_peak\": 1.509, \"ve_ratio_final\": 1.399, \"fidelity_gap_onset_step\": 20000, \"ve_onset_step\": 30000, \"temporal_lead_steps\": 10000, \"pearson_ss_ve\": 0.807, \"pearson_ss_ve_p\": 0.0015, \"pearson_ol_ve\": 0.425, \"pearson_ol_ve_p\": 0.169, \"ss_monotonicity\": 0.73, \"ol_monotonicity\": 0.73, \"ve_monotonicity\": 0.82, \"causal_direction\": \"fidelity_gap_leads_ve\", \"conclusion\": \"success\"}}, \"exp_060_cartpole_baseline\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T16:01:05.099Z\", \"updated_at\": \"2026-05-25T01:25:39.711Z\", \"hypothesis\": \"Cartpole Swingup (DMC) baseline dt=1 建立 v/e ratio 校准基线，用于 CIVO 诊断阈值在第三个 DMC 环境的验证。预期 NVE 保持在 1.0x 附近，无 CIVO 现象。\", \"conclusion\": \"success\", \"metrics\": {\"seeds\": 3, \"steps_per_seed\": 112000, \"train_return_s0\": 809.4, \"train_return_s1\": 684.4, \"train_return_s2\": 526.1, \"eval_return_s2_105K\": 557}}, \"exp_065_dt_emb_cosine\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T20:48:47.693Z\", \"updated_at\": \"2026-05-24T20:54:51.678Z\", \"hypothesis\": \"分析 trained dt_embedding 中 dt=1 vs dt=2 向量的 cosine similarity 及其训练过程演化。如果 cosine sim 高（接近 1）→ dt_emb 未学到有意义区分，CIVO 来自微小差异被 downstream 放大；如果 cosine sim 低 → dt_emb 学到了显著不同的表征，CIVO 来自 dt=2 表征本身的偏差。\", \"conclusion\": \"success\", \"metrics\": {\"trained_cosine_sim_range\": \"-0.94 to -0.70\", \"frozen_cosine_sim_range\": \"-0.15 to +0.07\", \"trained_trend\": \"strong negative (near-opposite directions)\", \"frozen_trend\": \"near-zero constant\", \"conclusion\": \"dt=1 and dt=2 embeddings learn nearly opposite representations; CIVO from dt=2 representation bias, not amplified micro-differences\"}}, \"exp_064_value_distribution\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T19:23:05.483Z\", \"updated_at\": \"2026-05-24T20:14:50.460Z\", \"hypothesis\": \"V(s) vs Monte Carlo return 分布对比：trained dt_emb (exp_008d collapsed) 的 value estimate 在 dt=2 imagination 步骤系统性高估，而 untrained/absent dt_emb (exp_008f control) 和 baseline (exp_001) 的 value 分布与 MC return 紧密跟踪。直观展示 CIVO 的 value divergence 位置和形态。\", \"conclusion\": \"success\", \"metrics\": {\"baseline_bias\": 344.85, \"baseline_rmse\": 371.73, \"baseline_overest_pct\": 100, \"baseline_v_mc_ratio\": 3.31, \"civo_bias\": 108.99, \"civo_rmse\": 112.36, \"civo_overest_pct\": 100, \"civo_v_mc_ratio\": 7.8, \"civo_v_mc_median\": 3.4, \"control_bias\": -6.51, \"control_rmse\": 57.93, \"control_overest_pct\": 52.5, \"control_v_mc_ratio\": 2.58, \"control_v_mc_median\": 1.05}}, \"exp_063_rssm_fidelity\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T18:12:47.163Z\", \"updated_at\": \"2026-05-24T19:21:37.837Z\", \"hypothesis\": \"RSSM 在 dt=2 transitions 上的 observation/reward reconstruction loss 显著高于 dt=1，量化 fidelity gap 作为 trained dt_emb 导致 delusional critic 的机械性基础。从 exp_001 (baseline) 和 exp_008d (collapsed) 的已有 checkpoint 提取，对比 dt=1 vs dt=2 prediction quality。\", \"conclusion\": \"success\", \"metrics\": {\"baseline_dt1_obs_mse\": 13.7, \"baseline_dt2_obs_mse\": 20.62, \"baseline_dt2_dt1_ratio_obs\": 1.505, \"baseline_dt2_dt1_ratio_reward\": 1.483, \"collapsed_dt1_obs_mse\": 26.93, \"collapsed_dt2_single_obs_mse\": 42.02, \"collapsed_dt2_single_reward_mae\": 0.146, \"collapsed_dt2_dt1_ratio_obs\": 1.56, \"collapsed_dt2_dt1_ratio_reward\": 2.695, \"collapsed_single_vs_chained_obs\": 1.138, \"collapsed_single_vs_chained_reward\": 1.926}}, \"exp_051_stackcube_frozen_dt_emb_s0\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T19:30:00.000Z\", \"updated_at\": \"2026-05-24T16:53:23.046Z\", \"hypothesis\": \"Freezing dt_emb in StackCube (manipulation domain) prevents CIVO collapse, contrasting exp_049 (trained dt_emb, CIVO ve_ratio 3.27@32.5K) to establish trained-vs-frozen causal evidence in manipulation tasks. If frozen prevents CIVO → extends Walker/Cheetah frozen finding to manipulation; if not → domain-specific factors override dt_emb mechanism.\", \"parent\": \"exp_049_stackcube_civo_trigger_s0\", \"metrics\": {\"eval_final\": 45.3, \"eval_final_step\": 212500, \"eval_peak\": 45.3, \"eval_peak_step\": 212500, \"ve_ratio_final\": 0.1, \"ve_ratio_final_step\": 212500, \"ve_ratio_peak\": 4.3, \"ve_ratio_peak_step\": 42500, \"total_steps\": 222400, \"nve_classification\": \"onset_self_correcting\", \"civo_transient\": true, \"civo_sustained\": false, \"civo_transient_range\": \"22K-62K\", \"civo_self_correction\": true, \"civo_self_correction_step\": 82500, \"gate_dt_mean\": 2, \"gate_dt_variation\": false, \"eval_dip_during_civo\": 7.1, \"eval_dip_step\": 42500}, \"conclusion\": \"negative\"}, \"exp_049_stackcube_civo_trigger_s0\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T17:14:38.578Z\", \"updated_at\": \"2026-05-24T16:53:19.032Z\", \"hypothesis\": \"CIVO trigger 配置（trained dt_emb + subsample ON + H=8）在 ManiSkill StackCube-v1 manipulation 任务上是否也触发 CIVO。测试 CIVO 是否从 locomotion 推广到 manipulation 领域。StackCube 是多阶段任务（pick+stack）。如果触发 → 扩展跨域证据；如果不触发 → 支持 locomotion-specific scope。\", \"parent\": \"exp_048_stackcube_civo_trigger_s0\", \"metrics\": {\"eval_final\": 34.88, \"eval_final_step\": 212500, \"eval_peak\": 35.89, \"eval_peak_step\": 182500, \"ve_ratio_final\": 0.186, \"ve_ratio_final_step\": 212500, \"ve_ratio_peak\": 5.048, \"ve_ratio_peak_step\": 42500, \"total_steps\": 222400, \"total_episodes\": 1112, \"nve_classification\": \"onset_self_correcting\", \"civo_transient\": true, \"civo_sustained\": false, \"civo_transient_range\": \"22K-72K\", \"civo_self_correction\": true, \"civo_self_correction_step\": 112500, \"gate_dt_mean\": 2, \"gate_dt_variation\": false, \"eval_dip_during_civo\": 4.93, \"eval_dip_step\": 62500}, \"conclusion\": \"success\"}, \"exp_057\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T16:49:35.310Z\", \"updated_at\": \"2026-05-24T16:50:44.968Z\", \"hypothesis\": \"Frozen dt_emb 跨 seed 可复现性验证（Walker seed=2, n=3）。当前 Walker frozen s0 NVE 0.19, s1 NVE 1.71 transient。s2 增加样本量到 n=3 验证稳健性。\", \"parent\": \"\", \"metrics\": {\"eval_return_peak\": 221.7, \"eval_return_peak_step\": 195000, \"eval_return_final\": 123.9, \"eval_return_final_step\": 215000, \"nve_peak\": 1.3, \"nve_peak_step\": 115000, \"nve_final\": 0.2, \"civo_alert\": 0, \"civo_sustained\": false, \"civo_transient\": true, \"civo_transient_range\": \"115k-145k\", \"train_steps\": 225000, \"gate_dt_mean\": 2}, \"conclusion\": \"success\"}, \"exp_008d_civo_trigger_s4\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-18T02:02:43.972Z\", \"hypothesis\": \"Walker Walk CIVO trigger seed=4: trained dt_emb + subsample ON + H=8. 第四 seed 复现 CIVO (NVE>1.5×)，加强 Walker 因果论证的统计力度。Rebuttal 储备。\", \"metrics\": {\"ve_ratio_peak\": 3.0294, \"ve_ratio_peak_step\": 105000, \"ve_ratio_final\": 3.0294, \"ve_ratio_final_step\": 105000, \"nve_peak\": 4.62, \"nve_peak_step\": 105000, \"nve_peak_note\": \"step-matched s1 baseline @105K = 0.6564\", \"nve_classification\": \"onset_collapse\"}, \"parent\": \"exp_008d_civo_trigger_s3\", \"status\": \"DONE\", \"updated_at\": \"2026-05-24T08:56:41.239Z\"}, \"exp_009b_008d_walker_s2\": {\"conclusion\": \"negative\", \"created_at\": \"2026-05-14T07:17:25.186Z\", \"hypothesis\": \"CIVO onset (NVE≥1.5×) reproduces on seed=2 with identical architecture, confirming the phenomenon is systematic rather than seed-specific. Collapse outcome may be stochastic.\", \"metrics\": {\"ve_ratio_peak\": 0.5703, \"ve_ratio_peak_step\": 55000, \"ve_ratio_final\": 0.25, \"ve_ratio_final_step\": 105000, \"nve_peak\": 1.62, \"nve_peak_step\": 45000, \"nve_peak_note\": \"step-matched s1 baseline @45K = 0.331; arithmetic peak @25K=2.04x excluded (baseline<0.1)\", \"nve_classification\": \"onset_self_correcting\"}, \"notes\": \"D032: Collapse NOT reproduced in seed 2. nve peaked 2.05x@25K (transient) then self-corrected to 0.38x@105K. Eval rose to 268. Contrast: seed 1 had SUSTAINED nve>1.5x at 35K+ (1.71x→2.09x→4.12x) → collapse to 83. Key finding: nve>1.5x threshold (35K+ steps) is reliable trained dt_emb marker (2/2 seeds), but collapse is stochastic (1/2). Framing proposal submitted to Director.\", \"parent\": \"exp_008d_subsample_on_h8\", \"status\": \"DONE\", \"updated_at\": \"2026-05-24T08:56:39.471Z\"}, \"exp_009e_008d_walker_s1\": {\"conclusion\": \"negative\", \"created_at\": \"2026-05-14T11:09:15.367Z\", \"hypothesis\": \"Walker Walk trained dt_emb + subsample ON + H=8 seed 1 — 多 seed 复现 008d delusional critic collapse，巩固 C2 统计显著性（plan_011）\", \"metrics\": {\"ve_ratio_peak\": 1.6663, \"ve_ratio_peak_step\": 55000, \"ve_ratio_final\": 1.03, \"ve_ratio_final_step\": 105000, \"nve_peak\": 4.13, \"nve_peak_step\": 55000, \"nve_peak_note\": \"step-matched s1 baseline @55K = 0.4035; paper onset NVE @45K = 2.09x\", \"nve_classification\": \"onset_collapse\"}, \"notes\": \"008d extended replication (same seed=1, 009e extends 008d from 55K to 105K). Eval trajectory 5K-55K identical to 008d (deterministic). Collapse confirmed at 105K: eval 131.08, nve@55K=4.12x (normalized). 65K bounce to 250 was transient, not recovery. actor_loss flipped positive @85K. Independent collapse rate = 1/2 (seed 1 collapsed, seed 2 self-corrected), NOT 2/3 — 008d and 009e are the same seed.\", \"parent\": \"exp_008d_subsample_on_h8\", \"status\": \"DONE\", \"updated_at\": \"2026-05-24T08:56:37.645Z\"}, \"exp_059_walker_trained_s5\": {\"status\": \"DONE\", \"created_at\": \"2026-05-24T03:08:46.842Z\", \"updated_at\": \"2026-05-24T07:46:59.075Z\", \"hypothesis\": \"Walker CIVO trigger 第5个独立seed验证。当前4/4 seeds触发sustained CIVO（p=0.0625 binomial test）。如果s5也触发 → p=0.03125，达到统计显著性阈值。关联 Claim 1: CIVO reproducibility。\", \"parent\": \"exp_008d_civo_trigger_s3\", \"metrics\": {\"ve_ratio_peak\": 3.3075, \"ve_ratio_peak_step\": \"85K\", \"nve_peak\": 4.72, \"nve_peak_note\": \"step-matched s1 baseline @85K = 0.7007\", \"nve_classification\": \"onset_collapse\", \"nve_classification_note\": \"Reclassified from onset_self_correcting: NVE self-corrected but eval=95.8 (10.5% of baseline 913) indicates irreversible policy damage. Collapse†.\", \"nve_final\": 1.22, \"nve_final_note\": \"0.8/0.656 (step-matched s1 baseline @105K)\", \"eval_final\": 95.8, \"eval_baseline\": 913, \"eval_pct_baseline\": \"10.5%\"}, \"conclusion\": \"success\", \"notes\": \"CIVO-positive under step-matched NVE (peak ≈ 5.0×). Self-correcting outcome (ve_ratio 3.3@85K → 0.8@105K in ~10K steps). Supports 5/5 Walker trained CIVO onset. Gate locked at dt=2 throughout (entropy=0).\"}, \"exp_057_frozen_dt_emb_walker_s2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"created_at\": \"2026-05-23T15:25:00.000Z\", \"updated_at\": \"2026-05-24T02:17:41.318Z\", \"hypothesis\": \"Frozen dt_emb 跨 seed 可复现性验证（Walker n=3）。当前 Walker frozen s0 NVE 0.19, s1 NVE 1.71 transient。s2 增加样本量到 n=3，如果 0 CIVO → frozen 在 Walker 上稳健；如果出现持续 CIVO → 样本不足。\", \"parent\": \"exp_042_frozen_dt_emb_walker\", \"metrics\": {\"total_steps\": 225000, \"ve_ratio_peak\": 1.283, \"ve_ratio_peak_step\": 115000, \"ve_ratio_final\": 0.177, \"ve_ratio_final_step\": 215000, \"nve_peak\": 1.88, \"nve_peak_step\": 115000, \"nve_classification\": \"transient\", \"eval_return_final\": 123.94, \"eval_return_final_step\": 215000, \"eval_return_peak\": 221.72, \"eval_return_peak_step\": 195000}}, \"exp_058_frozen_dt_emb_cheetah_s1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T18:10:49.773Z\", \"updated_at\": \"2026-05-24T00:30:00.000Z\", \"hypothesis\": \"Cheetah frozen dt_emb 跨 seed 可复现性验证。exp_046 (s0) 显示 frozen 将 NVE 从 ~70-108（trained）降至 1.35。s1 验证阻止效应是否可复现。如果 s1 也阻止 → Cheetah frozen n=2 增强极端 CIVO 场景下 frozen diagnostic 的统计基础。\", \"parent\": \"exp_046_frozen_dt_emb_cheetah\", \"conclusion\": \"success\", \"metrics\": {\"total_steps\": 224000, \"ve_ratio_peak\": 0.231, \"ve_ratio_peak_step\": 45000, \"ve_ratio_final\": 0.107, \"ve_ratio_final_step\": 215000, \"eval_return_final\": 80.46, \"eval_return_final_step\": 215000, \"eval_return_peak\": 191.74, \"eval_return_peak_step\": 25000, \"nve_peak\": 0.78, \"nve_peak_step\": 45000, \"nve_classification\": \"no_civo\", \"note\": \"Cheetah frozen s1. NVE=0.78× (raw 0.231 / baseline 0.296 @45K). Cheetah frozen n=2: s0 NVE=1.35, s1 NVE=0.78 — both clean, frozen 稳健阻止 extreme CIVO (trained NVE 70-108).\"}}, \"exp_056_peginsertion_frozen_s1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T09:02:23.683Z\", \"updated_at\": \"2026-05-24T00:00:00.000Z\", \"hypothesis\": \"D143 混合机制假说验证——PegInsertion frozen dt_emb 跨 seed 可复现性。exp_053 (s0) 显示 frozen 在 82.5K 回落到 1.82 而 trained 攀升到 10.05，s1 验证这个分叉是否可复现。如果 s1 也回落 → frozen 稳健阻止 dt_emb 放大；如果不回落 → seed-dependent。\", \"parent\": \"exp_053_peginsertion_frozen_s0\", \"conclusion\": \"success\", \"metrics\": {\"total_steps\": 222500, \"ve_ratio_peak\": 11.321, \"ve_ratio_peak_step\": 82500, \"ve_ratio_final\": 1.193, \"ve_ratio_final_step\": 212500, \"eval_return_final\": 4.37, \"eval_return_final_step\": 212500, \"eval_return_peak\": 24.42, \"eval_return_peak_step\": 132500, \"nve_classification\": \"burst\", \"note\": \"Ordering reversal vs s0 confirms D146 seed-dependent noise. Frozen s1 burst 11.32 > trained s1 peak 3.08 — frozen does NOT suppress ManiSkill transients.\", \"ve_ratio_trajectory\": {\"12500\": 0.316, \"22500\": 0.975, \"32500\": 1.839, \"42500\": 1.966, \"52500\": 5.422, \"62500\": 4.047, \"72500\": 8.408, \"82500\": 11.321, \"92500\": 3.724, \"102500\": 3.034, \"112500\": 2.204, \"122500\": 2.425, \"132500\": 0.842, \"142500\": 2.194, \"152500\": 2.203, \"162500\": 0.651, \"172500\": 1.085, \"182500\": 1.07, \"192500\": 0.467, \"202500\": 0.708, \"212500\": 1.193}}}, \"exp_055_peginsertion_civo_trigger_s1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-23T08:50:00.000Z\", \"updated_at\": \"2026-05-23T23:38:30.000Z\", \"hypothesis\": \"PegInsertion CIVO 跨 seed 可复现性验证。exp_050 (s0) 显示持续性 CIVO（ve_ratio_peak 10.05×@82.5K，最终自修复到 0.379@212.5K）。如果 s1 也触发持续 CIVO → PegInsertion CIVO 可复现；如果不触发 → seed-specific 异常。\", \"parent\": \"exp_050_peginsertion_civo_trigger_s0\", \"conclusion\": \"success\", \"metrics\": {\"total_steps\": 222400, \"ve_ratio_peak\": 3.08, \"ve_ratio_peak_step\": 92500, \"ve_ratio_final\": 0.498, \"ve_ratio_final_step\": 212500, \"eval_return_final\": 11.44, \"eval_return_final_step\": 212500, \"eval_return_peak\": 24.05, \"eval_return_peak_step\": 112500, \"nve_classification\": \"transient\", \"civo_triggered\": true, \"civo_self_corrected\": \"partial\", \"note\": \"CIVO triggered (peak 3.08@92.5K, less severe than s0=10.05). Partial self-correction to 0.498. PegInsertion trained cross-seed: s0=10.05, s1=3.08 — severity seed-dependent.\", \"ve_ratio_trajectory\": {\"12500\": 0.19, \"22500\": 0.81, \"32500\": 1.35, \"42500\": 2.0, \"52500\": 2.39, \"62500\": 2.85, \"72500\": 2.28, \"82500\": 2.48, \"92500\": 3.08, \"102500\": 2.51, \"112500\": 0.91, \"122500\": 1.21, \"132500\": 1.36, \"142500\": 0.75, \"152500\": 0.55, \"162500\": 1.17, \"172500\": 0.96, \"182500\": 0.94, \"192500\": 0.9, \"202500\": 0.73, \"212500\": 0.5}}}, \"exp_054_pickcube_frozen_s0\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"created_at\": \"2026-05-23T07:47:24.310Z\", \"updated_at\": \"2026-05-23T18:08:00.000Z\", \"hypothesis\": \"PickCube frozen dt_emb baseline (fixed_dt=2, subsample ON, H=8)。验证 CIVO frozen 配置在最简单 manipulation task 上的表现。如果 eval return 稳定高于 random → frozen dt_emb 在 easy task 上不影响学习；如果性能差 → frozen dt_emb 有问题。\"}, \"exp_053_peginsertion_frozen_s0\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"created_at\": \"2026-05-23T04:23:10.381Z\", \"updated_at\": \"2026-05-23T15:00:00.000Z\", \"hypothesis\": \"Freezing dt_emb in PegInsertionSide-v1 (contact-rich manipulation) prevents CIVO while maintaining task performance, establishing that dt_emb freezing generalizes as CIVO prevention across task domains. If frozen prevents CIVO here → extends StackCube/locomotion frozen finding to insertion tasks; if CIVO still appears → freezing insufficient for contact-rich tasks.\", \"parent\": \"exp_050_peginsertion_civo_trigger_s0\"}, \"exp_050_peginsertion_civo_trigger_s0\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T18:38:33.441Z\", \"updated_at\": \"2026-05-23T08:51:11.592Z\", \"hypothesis\": \"Fixed-dt=2 gate with CIVO trigger on PegInsertionSide-v1 (contact-rich manipulation) will demonstrate that temporal abstraction benefits extend beyond locomotion to precise insertion tasks, where event-gated horizons can skip redundant approach phases while preserving fine-grained control near contact.\", \"metrics\": {\"ve_ratio_peak\": 10.05, \"ve_ratio_peak_step\": 82500, \"ve_ratio_final\": 0.379, \"ve_ratio_final_step\": 212500, \"civo_self_corrected\": true, \"civo_correction_delay_steps\": 130000, \"eval_final\": 20.86, \"eval_final_step\": 212500, \"eval_peak\": 20.86, \"eval_peak_step\": 212500, \"total_steps\": 222400}, \"conclusion\": \"success\"}, \"exp_052_stackcube_civo_trigger_s1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T21:26:49.825Z\", \"updated_at\": \"2026-05-23T07:45:47.966Z\", \"hypothesis\": \"StackCube CIVO trigger (trained dt_emb + subsample ON + H=8) 跨 seed 可复现性验证。exp_049 (s0) 在 32.5K 步触发 CIVO（ve_ratio 3.27）。如果 s1 也触发 → CIVO 在 manipulation 领域可复现，非 seed-specific；如果不触发 → seed-dependent，需更多 seeds。\", \"parent\": \"exp_049_stackcube_civo_trigger_s0\", \"metrics\": {\"eval_final\": 29.458, \"eval_final_step\": 212500, \"eval_peak\": 39.873, \"eval_peak_step\": 162500, \"ve_ratio_final\": 0.133, \"ve_ratio_final_step\": 212500, \"ve_ratio_peak\": 4.67, \"ve_ratio_peak_step\": 52500, \"total_steps\": 222400}, \"conclusion\": \"success\"}, \"exp_048_cheetah_civo_extension\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T16:30:40.050Z\", \"updated_at\": \"2026-05-22T21:18:00.000Z\", \"hypothesis\": \"Cheetah CIVO (NVE 70.64, far more severe than Walker 1.5-4.9) is too severe for spontaneous recovery. Walker CIVO self-corrected in exp_045 (ve_ratio 4.91→0.05 over 170K steps). If Cheetah does NOT self-correct → severity determines recoverability narrative. If it does → CIVO is universally transient regardless of severity.\", \"parent\": \"exp_010b_cheetah_civo_trigger_s0\", \"metrics\": {\"eval_final\": 23.4, \"eval_final_step\": 302000, \"eval_peak\": 32.8, \"eval_peak_step\": 252000, \"ve_ratio_initial\": 46.3, \"ve_ratio_peak\": 24.112, \"ve_ratio_peak_step\": 162000, \"ve_ratio_final\": 1.803, \"nve_initial\": 70.64, \"nve_peak_secondary\": 36.76, \"nve_final\": 2.75, \"total_steps\": 312000, \"civo_self_corrected\": false, \"civo_correction_pct\": 96, \"secondary_burst_step\": 152000, \"secondary_burst_nve\": 36.47, \"gate_collapsed\": true}, \"conclusion\": \"success\"}, \"exp_047_frozen_dt_emb_walker_s1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T11:03:31.428Z\", \"updated_at\": \"2026-05-22T19:01:30.894Z\", \"hypothesis\": \"Frozen dt_emb Walker seed 1: 增强 exp_042 (s0, NVE=0.19) 的统计力度。 如果 s1 也 NVE<1.5 且无持续 CIVO → frozen dt_emb mitigation 跨 seed robust。\", \"parent\": \"exp_042_frozen_dt_emb_walker\", \"metrics\": {\"eval_final\": 144.22, \"eval_final_step\": 215000, \"eval_peak\": 408.79, \"eval_peak_step\": 125000, \"ve_ratio_peak\": 1.099, \"ve_ratio_peak_step\": 75000, \"ve_ratio_final\": 0.277, \"nve_peak\": 1.71, \"nve_peak_step\": 95000, \"nve_final_105k\": 0.56, \"total_steps\": 225000}, \"conclusion\": \"success\"}, \"exp_046_frozen_dt_emb_cheetah\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T10:41:53.934Z\", \"updated_at\": \"2026-05-22T18:32:34.105Z\", \"hypothesis\": \"Cross-environment validation: frozen dt_emb (random init, requires_grad=False) prevents CIVO on Cheetah Run, extending the Walker Walk finding (exp_042 NVE=0.19, exp_015b NVE=0.47) to a second environment. Cheetah has stronger CIVO (NVE 8.27-70.64× in exp_010b) so this is a harder test of the frozen mitigation.\", \"parent\": \"exp_042_frozen_dt_emb_walker\", \"metrics\": {\"eval_final\": 150.5, \"eval_peak\": 207.4, \"eval_peak_step\": 145000, \"ve_ratio_peak\": 0.4, \"ve_ratio_final\": 0.1, \"nve_peak\": 1.35, \"nve_peak_step\": 45000, \"nve_final\": 0.17, \"total_steps\": 224000, \"civo_alert_count\": 0}, \"conclusion\": \"success\"}, \"exp_044_gradient_stop_walker\": {\"status\": \"DONE\", \"created_at\": \"2026-05-22T09:03:45.656Z\", \"updated_at\": \"2026-05-22T16:08:22.684Z\", \"hypothesis\": \"Reviewer Q2 直接回应：gradient stopping（detach dt_emb gradient to reward head）是否能阻断 CIVO 的 reward-critic feedback loop。基于 008d 配置（trained dt_emb + subsample ON + H=8），仅阻断 dt_emb→reward_head 梯度路径。如果 gradient stopping 有效（NVE<1.5）→ 最简干预方案成立，推翻我们之前 SGS 1/17 的结论（SGS 阻断所有梯度 vs 这里只阻断 dt_emb→reward 路径）。如果无效 → 直接证据证明 gradient-level intervention 不足以解决 CIVO，支撑 Intervention Hierarchy 中 gradient-level 最弱的结论。\", \"metrics\": {\"eval_final\": 538.6, \"eval_peak\": 561.2, \"eval_peak_step\": 185000, \"eval_civo_trough\": 44.3, \"eval_civo_trough_step\": 95000, \"ve_ratio_peak\": 4.4, \"ve_ratio_peak_step\": 95000, \"ve_ratio_final\": 0.1, \"civo_onset_step\": 85000, \"civo_resolved_step\": 125000, \"civo_duration_steps\": 40000, \"total_steps\": 224000, \"pre_civo_peak\": 545.6, \"pre_civo_peak_step\": 75000}, \"conclusion\": \"success\"}, \"exp_045_treatment_extension_008d_s3\": {\"created_at\": \"2026-05-22T09:40:52.894Z\", \"updated_at\": \"2026-05-22T15:41:43.036Z\", \"status\": \"DONE\", \"hypothesis\": \"CIVO-triggering config (trained dt_emb + subsample ON + H=8) that already exhibited CIVO at 112K will show sustained or worsening value overestimation when extended to 300K, providing temporal dynamics data for the treatment extension analysis (Reviewer Q: does CIVO self-correct or persist?)\", \"parent\": \"exp_008d_civo_trigger_s3\", \"conclusion\": \"success\", \"metrics\": {\"eval_final\": 867.6, \"eval_peak\": 869.7, \"eval_peak_step\": 242000, \"nve_peak\": 4.91, \"nve_peak_step\": 132000, \"nve_final\": 0.052, \"ve_ratio_final\": 0.052, \"total_steps\": 312000, \"civo_alerts\": 0, \"civo_self_corrected\": true, \"civo_correction_step\": 142000, \"eval_trajectory\": {\"112000\": 58.5, \"122000\": 41.8, \"132000\": 35.1, \"142000\": 350.2, \"152000\": 646.4, \"162000\": 482.3, \"172000\": 600.4, \"182000\": 600.5, \"192000\": 699.5, \"202000\": 684.3, \"212000\": 758.6, \"222000\": 744.6, \"232000\": 745.4, \"242000\": 869.7, \"252000\": 721.6, \"262000\": 820.6, \"272000\": 716.2, \"282000\": 755.6, \"292000\": 843, \"302000\": 867.6}, \"ve_ratio_trajectory\": {\"122000\": 4.77, \"132000\": 4.91, \"142000\": 0.43, \"152000\": 0.21, \"162000\": 0.25, \"172000\": 0.18, \"182000\": 0.16, \"192000\": 0.13, \"202000\": 0.12, \"212000\": 0.1, \"222000\": 0.1, \"232000\": 0.09, \"242000\": 0.07, \"252000\": 0.08, \"262000\": 0.07, \"272000\": 0.08, \"282000\": 0.07, \"292000\": 0.06, \"302000\": 0.05}}}, \"exp_043_008f_walker_s1\": {\"created_at\": \"2026-05-22T02:35:37.558Z\", \"hypothesis\": \"Plan_012 / Claim C2 seed 1：复现 008f 因果控制（dt_embed_dim=0, subsample ON, H=8）。目前只有 seed 0 数据。如果 s1 也显示无 CIVO → 确认 dt_emb absence prevents CIVO 是 robust 的跨 seed 结论，支撑因果链 \\\"trained dt_emb → CIVO\\\"。\", \"status\": \"DONE\", \"updated_at\": \"2026-05-22T10:38:36.474Z\", \"metrics\": {\"eval_final\": 673.73, \"eval_peak\": 673.73, \"eval_peak_step\": 215000, \"nve_peak\": 0.808, \"nve_peak_step\": 105000, \"nve_final\": 0.123, \"civo_alert\": false, \"total_steps\": 224000, \"gate_dt_2_frac\": 1, \"gate_entropy\": 0, \"note\": \"No CIVO (peak NVE 0.808, well below 1.5). Gate fixed at dt=2. Seed 1 replicates seed 0 finding: dt_emb absence prevents CIVO.\"}, \"conclusion\": \"success\"}, \"exp_042_frozen_dt_emb_walker\": {\"created_at\": \"2026-05-22T02:13:59.183Z\", \"hypothesis\": \"dt_embedding training (not its mere existence) is a necessary condition for CIVO collapse. Freezing dt_emb (random init, requires_grad=False) should prevent the reward-value divergence observed in exp_008d with trained dt_emb.\", \"parent\": \"\", \"status\": \"DONE\", \"updated_at\": \"2026-05-22T10:29:26.337Z\", \"metrics\": {\"eval_final\": 612.45, \"eval_peak\": 682.38, \"eval_peak_step\": 205000, \"nve_peak\": 0.194, \"nve_final\": 0.051, \"civo_alert\": false, \"total_steps\": 224000, \"total_train_episodes\": 224}, \"conclusion\": \"success\"}, \"exp_040_wide_dual_critic_cheetah\": {\"created_at\": \"2026-05-21T19:50:49.909Z\", \"hypothesis\": \"Cheetah dual-critic seed 1：exp_034 (s0) 显示 dual-critic 在 Cheetah 上 NVE 1.8, eval 97.5（部分恢复 31%）。s1 确认此 pattern 是否 robust。如果 s1 也部分恢复 → Cheetah dual-critic 效果一致但弱于 Walker；如果 s1 完全不恢复 → s0 的部分恢复是偶发。\", \"parent\": \"exp_032_dual_critic_walker\", \"status\": \"DONE\", \"updated_at\": \"2026-05-22T09:37:44.547Z\", \"conclusion\": \"success\"}, \"exp_041_dual_critic_walker_s3\": {\"created_at\": \"2026-05-21T19:50:54.290Z\", \"hypothesis\": \"D128 推导：exp_038 s2 出现非 CIVO 崩溃 (eval 354→121, NVE≤0.3)，当前 collapse 频率 1/3。s3 确定崩溃是偶发 (1/4) 还是系统性 (2/4)。如果 s3 正常 → 非 CIVO 崩溃为低频偶发事件，dual-critic CIVO prevention 仍 robust；如果 s3 也崩 → 50% 系统性问题需进一步诊断。\", \"parent\": \"exp_032_dual_critic_walker\", \"status\": \"DONE\", \"updated_at\": \"2026-05-22T09:04:44.715Z\", \"conclusion\": \"success\", \"metrics\": {\"eval_return_peak\": 761.1, \"eval_return_final\": 544, \"eval_return_peak_step\": 165000, \"nve_peak\": 1.5, \"nve_final\": 0.1, \"civo_prevented\": true, \"gate_dt_2_frac\": 1, \"non_civo_collapse\": false, \"steps\": 215000, \"note\": \"CIVO prevented (NVE≤1.5), no non-CIVO collapse. Eval stays 486-761 after peak. Non-CIVO collapse rate confirmed 1/4 (only s2).\"}}, \"exp_039_narrow_dual_critic_walker_s1\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-21T16:31:40.055Z\", \"hypothesis\": \"Narrow dual-critic Walker seed 1: 验证 exp_035 (s0, eval 697.8) 的 CIVO recovery 发现是否跨 seed 一致。如果 s1 也展示 recovery → narrow dual-critic (min operation alone) 驱动 recovery 是 robust 的；如果不 recover → s0 的 recovery 是偶发事件。\", \"metrics\": {\"civo_recovery\": true, \"eval_return_final\": 592.7, \"note\": \"Narrow dual Walker s1: CIVO triggered then recovered. s0=697.8, s1=592.7, mean≈645. Recovery 2/2.\", \"nve_peak\": 2.19, \"recovery_confirmed\": true}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T02:35:33.617Z\"}, \"exp_038_dual_critic_walker_s2\": {\"conclusion\": \"negative\", \"created_at\": \"2026-05-21T12:18:35.293Z\", \"hypothesis\": \"Third seed (s2) for Walker dual-critic CIVO prevention. s0 (eval 787.7) and s1 (eval 551.8) both showed CIVO prevention (NVE≤1.1). Third datapoint enables IQM statistical reporting. If 3/3 CIVO prevented → robust evidence for Prevention mechanism in medium-severity CIVO environments.\", \"metrics\": {\"civo_alert\": 0, \"civo_prevented\": true, \"eval_return_collapse\": 99.6, \"eval_return_collapse_step\": 175000, \"eval_return_final\": 120.9, \"eval_return_peak\": 354, \"eval_return_peak_step\": 155000, \"gate_dt_2_frac\": 1, \"non_civo_collapse\": true, \"note\": \"CIVO prevented (NVE≤0.3) but non-CIVO eval collapse at 175k (354→99.6). Different failure mode from value overestimation.\", \"nve_final\": 0.248, \"nve_peak\": 0.3, \"steps\": 224000}, \"parent\": \"exp_032_dual_critic_walker\", \"status\": \"DONE\", \"updated_at\": \"2026-05-22T02:11:36.842Z\"}, \"exp_037_wide_critic_cheetah\": {\"conclusion\": \"negative\", \"created_at\": \"2026-05-21T12:18:33.040Z\", \"hypothesis\": \"Wide single critic on Cheetah: if capacity=recovery generalizes from Walker (exp_033, NVE 4.75→self-repair, eval 408) to Cheetah (high CIVO, baseline NVE ~70.64), then Recovery mechanism works across CIVO severity levels. Combined with exp_034 (dual-critic Cheetah, NVE 1.75, eval 97.5), establishes that both Prevention and Recovery are environment-dependent.\", \"metrics\": {\"civo_alert\": 0, \"eval_return_final\": 146.1, \"eval_return_peak\": 350.1, \"gate_dt_2_frac\": 1, \"nve_final\": 0.1, \"nve_peak\": 3.6, \"steps\": 224000}, \"parent\": \"exp_033_wide_critic_walker\", \"status\": \"DONE\", \"updated_at\": \"2026-05-21T19:45:52.311Z\"}, \"exp_036_dual_critic_pickcube\": {\"conclusion\": \"negative\", \"created_at\": \"2026-05-21T08:43:18.481296+00:00\", \"hypothesis\": \"Dual-critic on PickCube: TCN failed at σ=0.2 and σ=0.5 on PickCube. If dual-critic suppresses CIVO on PickCube → architecture-level intervention generalizes across all 3 environments (Walker+Cheetah+PickCube), while representation-level (TCN) only partially works on Walker. Strongest evidence for intervention hierarchy.\", \"metrics\": {\"civo_alert\": 0, \"eval_return_final\": 27.7, \"eval_return_peak\": 27.7, \"gate_dt_2_frac\": 1, \"nve_final\": 0.2, \"nve_peak\": 2.3, \"steps\": 212447}, \"parent\": \"exp_032_dual_critic_walker\", \"status\": \"DONE\", \"updated_at\": \"2026-05-21T19:45:31.290Z\"}, \"exp_035_narrow_dual_critic_walker\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-21T07:47:55.131429+00:00\", \"hypothesis\": \"Narrow dual-critic ablation (2×256 hidden, total params ≈ baseline single 512 critic): isolates min operation effect from parameter count. If CIVO suppressed → min operation itself prevents overestimation cascade. If CIVO persists → parameter count is the key factor. Combined with exp_033 (wide single critic) forms 2×2 factorial: {single,dual} × {normal,scaled} → mechanism decomposition.\", \"metrics\": {\"actor_entropy_final\": -0.19, \"civo_alert_window\": \"65K-85K\", \"civo_prevented\": false, \"civo_recovery\": true, \"director_override\": \"Director ruled success: CIVO recovery (33.8→697.8) is the success criterion, not prevention\", \"eval_at_215K\": 697.8, \"eval_at_85K\": 33.8, \"eval_final\": 697.8, \"eval_peak\": 697.8, \"eval_trough\": 33.8, \"nve_final\": 0.066, \"nve_peak\": 2.75, \"nve_peak_step\": 85000, \"recovery_from\": 33.8, \"recovery_to\": 697.8, \"total_steps\": 215000, \"train_return_final_range\": \"708-806\", \"v1_v2_gap_max\": 0.08, \"v1_v2_gap_typical\": 0.01}, \"parent\": \"exp_032_dual_critic_walker\", \"status\": \"DONE\", \"updated_at\": \"2026-05-21T16:14:26.099Z\"}, \"exp_034\": {\"conclusion\": \"negative\", \"created_at\": \"2026-05-21T12:17:29.760Z\", \"hypothesis\": \"Dual-critic (min of two independent critics) will prevent CIVO in Cheetah Run by providing pessimistic value estimates, as it did in Walker Walk (exp_032). If value overestimation is environment-universal, the same mechanism should work across DMC tasks.\", \"metrics\": {\"CIVO_prevented\": false, \"civo_trigger_steps\": [55000, 105000], \"final_NVE\": 0.144, \"final_eval_return\": 97.5, \"max_NVE\": 1.753, \"peak_eval_return\": 315.7, \"total_steps\": 215000, \"v1_v2_max_divergence\": 0.004}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T12:18:09.552Z\"}, \"exp_034_dual_critic_cheetah\": {\"conclusion\": \"negative\", \"created_at\": \"2026-05-21T05:50:59.612345+00:00\", \"hypothesis\": \"Dual-critic on Cheetah Run: TCN failed at all σ (0.2/0.5/1.0) on Cheetah. If dual-critic suppresses CIVO on Cheetah (where TCN failed completely) → dual-critic is a more general architecture-level intervention that works across environments. Strengthens Intervention Hierarchy: architecture-level > representation-level.\", \"metrics\": {\"baseline_eval_final\": 0.83, \"baseline_nve_peak\": 70.64, \"civo_alert_steps\": [95000, 105000], \"civo_alerts\": 2, \"civo_prevented\": false, \"dual_wave_civo\": true, \"eval_final\": 97.5, \"eval_final_step\": 215000, \"eval_peak\": 315.7, \"eval_peak_step\": 45000, \"eval_vs_peak_pct\": 31, \"gate_dt2_frac\": 1, \"gate_entropy\": 0, \"v1_v2_gap\": \"<0.2 (min operation has no pessimism effect)\", \"value_mean_final\": 14.2, \"value_mean_peak\": 60.5, \"ve_ratio_final\": 0.1, \"ve_ratio_peak\": 1.8, \"ve_ratio_peak_step\": 55000}, \"parent\": \"exp_032_dual_critic_walker\", \"status\": \"DONE\", \"updated_at\": \"2026-05-21T12:15:03.481Z\"}, \"exp_033_wide_critic_walker\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-21T03:45:53.644963+00:00\", \"hypothesis\": \"Wide single critic ablation: if CIVO suppression in exp_032 (dual-critic) is due to parameter count/regularization rather than pessimistic min operation, then a single critic with 2× parameters should also suppress CIVO. If wide-critic fails (CIVO persists) but dual-critic succeeds → min operation has implicit regularization effect beyond pessimism.\", \"metrics\": {\"civo_alert_step\": 105000, \"civo_alert_ve_ratio\": 1.958, \"civo_instability_duration_steps\": 75000, \"critic_params\": 2886911, \"eval_reward_final\": 407.9, \"eval_reward_peak\": 194.8, \"eval_reward_trough\": 31.8, \"value_loss_final\": 1.4, \"ve_ratio_final\": 0.1, \"ve_ratio_peak\": 4.7}, \"parent\": \"exp_032_dual_critic_walker\", \"status\": \"DONE\", \"updated_at\": \"2026-05-21T12:08:15.252Z\"}, \"exp_031b_tcn_pickcube_s0_sigma05\": {\"conclusion\": \"negative\", \"created_at\": \"2026-05-20T19:46:39.136363+00:00\", \"hypothesis\": \"PickCube σ=0.5 dose-response data collection: σ=0.2 (exp_031) failed with NVE peak 3.71. σ=0.5 tests whether higher noise amplitude can suppress CIVO in ManiSkill PickCube. Combined with σ=0.2 data, establishes dose-response curve for robotics manipulation domain.\", \"metrics\": {\"eval_reward_final\": 25.5, \"eval_reward_last5_avg\": 25.9, \"eval_reward_peak\": 29.1, \"nve_final\": 0.2, \"nve_peak\": 3.3, \"nve_peak_step\": 42500, \"nve_suppressed_from_step\": 72500, \"total_episodes\": 1062, \"total_steps\": 212400}, \"parent\": \"exp_031_tcn_pickcube_s0_sigma02\", \"status\": \"DONE\", \"updated_at\": \"2026-05-21T08:50:22.853581+00:00\"}, \"exp_032_dual_critic_walker\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-20T22:58:31.008200+00:00\", \"hypothesis\": \"Dual-critic (min of two independent critics for actor loss) will suppress CIVO by preventing critic overestimation. Uses 008d CIVO-trigger config (trained dt_emb + multi-rate exposure). If NVE stays below 1.5× and eval matches baseline, dual-critic is an effective architecture-level intervention.\", \"metrics\": {\"baseline_eval\": 900, \"civo_prevented\": true, \"eval_final\": 739.7, \"eval_final_step\": 215000, \"eval_peak\": 787.7, \"eval_peak_step\": 205000, \"eval_vs_baseline_pct\": 87.5, \"gate_dt2_frac\": 1.0, \"gate_entropy\": 0.0, \"note\": \"CIVO prevented 2/2 seeds. v1≈v2 → mechanism is implicit value regularization, not min-of-two pessimism.\", \"nve_final\": 0.1, \"nve_peak\": 1.1, \"nve_peak_step\": 95000, \"v1_v2_gap\": \"<0.1% (min operation has no pessimism effect)\"}, \"parent\": \"exp_008d_civo_trigger_s2\", \"status\": \"DONE\", \"updated_at\": \"2026-05-21T07:52:13.265445+00:00\"}, \"exp_032b_dual_critic_walker_s1\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-20T23:22:08.787456+00:00\", \"hypothesis\": \"Dual-critic seed=1 replication: if both s0 and s1 show NVE<1.5× and eval matches baseline → dual-critic is a robust architecture-level CIVO intervention, strengthening Intervention Hierarchy evidence.\", \"metrics\": {\"actor_loss_late\": \"≈0 (gradient signal weak)\", \"baseline_eval\": 900, \"director_override\": \"CIVO suppressed (NVE<1.5 throughout) = success for intervention evaluation. Eval 57% of vanilla baseline is due to gate collapse (dt=2 locked), not dual-critic failure.\", \"eval_criterion_pass\": false, \"eval_trajectory\": \"75K=241, 105K=228, 155K=361, 195K=544, 205K=552(peak), 215K=516\", \"eval_vs_baseline_pct\": 57, \"final_eval_return\": 516, \"final_nve\": 0.1, \"gate_dt2_frac\": 1.0, \"nve_criterion_pass\": true, \"nve_trajectory\": \"15K=0.0, 25K=0.2, 35K=0.4, 45K=0.8, 55K=0.7, 65K=0.7, 75K=0.7, 85K=1.4(peak), 95K=0.7, 105K=0.5, 135K=0.4, 215K=0.1\", \"peak_eval_return\": 551.8, \"peak_nve\": 1.4, \"total_steps\": 224000, \"total_updates\": 52599, \"training_hours\": 6.42, \"value1_value2_gap\": \"<0.5 (min operation has no pessimism effect)\"}, \"notes\": \"NVE well controlled (peak 1.4 < 1.5, no CIVO), but eval only 57% of baseline (516 vs ~900). Dual-critic suppresses value overestimation at cost of policy performance. Gate collapsed to dt=2 throughout. Two critics converge to near-identical values, min operation ineffective.\", \"parent\": \"exp_032_dual_critic_walker\", \"status\": \"DONE\", \"updated_at\": \"2026-05-21T05:55:05.353975+00:00\"}, \"exp_029d_tcn_walker_s3_sigma02\": {\"conclusion\": \"negative\", \"created_at\": \"2026-05-20T19:33:03.633Z\", \"hypothesis\": \"Fourth TCN σ=0.2 seed to match 4 baseline seeds (s1=916, s2=443, s3=869, s4=923@105K) for statistical comparison. Current TCN seeds: s0=91%, s1=45%. Need s2+s3 to compute IQM+CI per Agarwal et al. 2021.\", \"metrics\": {\"civo_onset_step\": 105000, \"civo_pattern\": \"sudden blowup (healthy 0.67@95K → 3.0@105K)\", \"eval_final\": 104.5, \"eval_last_step\": 215000, \"eval_peak\": 349.6, \"eval_peak_step\": 95000, \"eval_return_105K\": 71.8, \"eval_return_115K\": 69.8, \"eval_return_125K\": 61.5, \"eval_return_135K\": 141.8, \"eval_return_145K\": 98.66, \"eval_return_155K\": 88.86, \"eval_return_15K\": 159.1, \"eval_return_165K\": 86.22, \"eval_return_175K\": 123.53, \"eval_return_185K\": 153.71, \"eval_return_195K\": 68.84, \"eval_return_205K\": 63.71, \"eval_return_215K\": 104.5, \"eval_return_25K\": 155.7, \"eval_return_35K\": 190.8, \"eval_return_45K\": 137.1, \"eval_return_55K\": 210.7, \"eval_return_5K\": 31.7, \"eval_return_65K\": 189.5, \"eval_return_75K\": 253.2, \"eval_return_85K\": 259.5, \"eval_return_95K\": 349.6, \"gate_dt2_frac\": 1.0, \"gate_entropy\": 0.0, \"nve_peak\": 3.0, \"nve_peak_step\": 105000, \"step\": 224000, \"value_mean_105K\": 218.37, \"value_mean_215K\": 42.55, \"value_mean_95K\": 232.74, \"ve_ratio_105K\": 3.0, \"ve_ratio_115K\": 2.5, \"ve_ratio_125K\": 2.4, \"ve_ratio_135K\": 0.9, \"ve_ratio_145K\": 1.141, \"ve_ratio_155K\": 1.06, \"ve_ratio_165K\": 0.91, \"ve_ratio_175K\": 0.556, \"ve_ratio_185K\": 0.396, \"ve_ratio_195K\": 0.78, \"ve_ratio_205K\": 0.747, \"ve_ratio_215K\": 0.4, \"ve_ratio_45K\": 0.695, \"ve_ratio_55K\": 0.598, \"ve_ratio_65K\": 0.863, \"ve_ratio_75K\": 0.791, \"ve_ratio_85K\": 0.9, \"ve_ratio_95K\": 0.7}, \"parent\": \"exp_029b_tcn_walker_s2_sigma02\", \"status\": \"DONE\", \"updated_at\": \"2026-05-21T03:39:24.356963+00:00\"}, \"exp_031_tcn_pickcube_s0_sigma02\": {\"conclusion\": \"negative\", \"created_at\": \"2026-05-20T12:09:56.923Z\", \"hypothesis\": \"TCN (Temporal Conditioning Noise, σ=0.2) on dt_embedding during imagination rollout will suppress CIVO in ManiSkill PickCube-v1, as it did in Walker Walk, by preventing the world model from overfitting to fixed dt signals.\", \"metrics\": {\"eval_peak\": 28.6, \"eval_peak_step\": 162500, \"eval_return_132K\": 23.45, \"eval_return_152K\": 23.1, \"eval_return_192K\": 11.6, \"gate_dt2_frac\": 1.0, \"gate_entropy\": 0, \"step\": 195600, \"train_return_range\": \"18-25\", \"ve_ratio_latest\": 0.18, \"ve_ratio_peak\": 3.71}, \"parent\": \"exp_019b_pickcube_civo_trigger\", \"status\": \"DONE\", \"updated_at\": \"2026-05-20T23:52:48.308Z\"}, \"exp_029b_tcn_walker_s2_sigma02\": {\"conclusion\": \"negative\", \"created_at\": \"2026-05-20T16:55:13.731Z\", \"hypothesis\": \"TCN σ=0.2 seed variance characterization: s0 eval=91%, s1 eval=45%. Third seed resolves whether high variance is systematic or s1 is outlier.\", \"metrics\": {\"civo_onset_step\": 65000, \"eval_last_step\": 165000, \"eval_peak\": 177.67, \"eval_peak_step\": 55000, \"eval_return_105K\": 31.97, \"eval_return_115K\": 35.45, \"eval_return_125K\": 33.04, \"eval_return_135K\": 42.47, \"eval_return_145K\": 51.66, \"eval_return_155K\": 56.5, \"eval_return_15K\": 168.41, \"eval_return_165K\": 44.9, \"eval_return_25K\": 159.56, \"eval_return_35K\": 168.05, \"eval_return_45K\": 171.51, \"eval_return_55K\": 177.67, \"eval_return_5K\": 30.46, \"eval_return_65K\": 106.57, \"eval_return_75K\": 64.01, \"eval_return_85K\": 62.82, \"eval_return_95K\": 44.66, \"gate_dt2_frac\": 1.0, \"gate_entropy\": 0.0, \"late_stage_nve_decline\": \"value adaptation (value_mean 108→55), not recovery (eval stayed 32-57)\", \"nve_peak\": 2.765, \"nve_peak_step\": 105000, \"step\": 168000, \"value_mean_105K\": 88.38, \"value_mean_165K\": 55.03, \"value_mean_55K\": 103.62, \"ve_ratio_105K\": 2.765, \"ve_ratio_115K\": 2.326, \"ve_ratio_125K\": 2.278, \"ve_ratio_135K\": 1.648, \"ve_ratio_145K\": 1.234, \"ve_ratio_155K\": 1.061, \"ve_ratio_15K\": 0.03, \"ve_ratio_165K\": 1.226, \"ve_ratio_25K\": 0.174, \"ve_ratio_35K\": 0.335, \"ve_ratio_45K\": 0.477, \"ve_ratio_55K\": 0.583, \"ve_ratio_65K\": 1.014, \"ve_ratio_75K\": 1.65, \"ve_ratio_85K\": 1.623, \"ve_ratio_95K\": 2.109}, \"parent\": \"exp_029a_tcn_walker_s1_sigma02\", \"status\": \"DONE\", \"updated_at\": \"2026-05-20T22:58:31.008195+00:00\"}, \"exp_030c_tcn_cheetah_s0_sigma10\": {\"conclusion\": \"negative\", \"created_at\": \"2026-05-20T16:26:11.800Z\", \"hypothesis\": \"TCN σ=1.0 on Cheetah tests whether higher noise amplitude further suppresses CIVO. σ=0.5 (exp_030b) was negative with NVE peaking at 10.67@55K then declining. σ=1.0 should provide stronger temporal regularization. If NVE stays below 1.5 throughout training and eval_return ≥ baseline → TCN generalizes to Cheetah with appropriate σ scaling.\", \"metrics\": {\"baseline_eval_avg\": 548, \"eval_final\": 47.2, \"eval_peak\": 371.7, \"eval_peak_step\": 35000, \"eval_return_105K\": 122.5, \"eval_return_115K\": 162.2, \"eval_return_125K\": 148.5, \"eval_return_135K\": 138.4, \"eval_return_145K\": 100.4, \"eval_return_155K\": 144.3, \"eval_return_15K\": 87.5, \"eval_return_165K\": 130.9, \"eval_return_175K\": 66.4, \"eval_return_185K\": 47.2, \"eval_return_195K\": 56.5, \"eval_return_205K\": 49.7, \"eval_return_215K\": 47.2, \"eval_return_25K\": 166.3, \"eval_return_35K\": 371.7, \"eval_return_45K\": 144.0, \"eval_return_55K\": 266.0, \"eval_return_5K\": 8.3, \"eval_return_65K\": 197.0, \"eval_return_75K\": 107.8, \"eval_return_85K\": 95.8, \"eval_return_95K\": 72.8, \"eval_vs_baseline\": \"8.6%\", \"gate_dt2_frac\": 1.0, \"gate_dt_mean\": 2.0, \"gate_entropy\": 0.0, \"step\": 224000, \"ve_ratio_max\": 0.4}, \"parent\": \"\", \"status\": \"DONE\", \"updated_at\": \"2026-05-20T22:34:07.916452+00:00\"}, \"exp_029c_tcn_walker_s0_sigma01\": {\"conclusion\": \"negative\", \"created_at\": \"2026-05-20T11:09:50.913Z\", \"hypothesis\": \"σ=0.1 tests the lower bound of effective TCN noise; if Walker σ=0.2 prevents CIVO and σ=0.1 does not, establishes minimum effective dose. Same CIVO-inducing config (gate_fixed_dt=2, subsample_max_dt=2, imag_horizon=8). Three-point dose-response: σ=0.1 (this), σ=0.2 (success), σ=0.5 (oscillatory failure).\", \"metrics\": {\"eval_final\": 328.3, \"eval_peak\": 490.7, \"eval_peak_step\": \"165K\", \"eval_return_105K\": 204.7, \"eval_return_115K\": 296.4, \"eval_return_125K\": 232.3, \"eval_return_135K\": 247.4, \"eval_return_145K\": 323.1, \"eval_return_155K\": 359.7, \"eval_return_15K\": 99.1, \"eval_return_165K\": 490.7, \"eval_return_175K\": 246.2, \"eval_return_185K\": 220.6, \"eval_return_195K\": 212.8, \"eval_return_205K\": 256.9, \"eval_return_215K\": 328.3, \"eval_return_25K\": 140.7, \"eval_return_35K\": 155.7, \"eval_return_45K\": 160.9, \"eval_return_55K\": 254.8, \"eval_return_5K\": 35.6, \"eval_return_65K\": 268.7, \"eval_return_75K\": 295.5, \"eval_return_85K\": 220.8, \"eval_return_95K\": 188.6, \"nve_final\": 0.1, \"nve_max\": 1.0218, \"nve_max_step\": \"95K\", \"total_steps\": 224000, \"ve_ratio_105K\": 0.761, \"ve_ratio_115K\": 0.4514, \"ve_ratio_125K\": 0.4899, \"ve_ratio_135K\": 0.3995, \"ve_ratio_145K\": 0.2667, \"ve_ratio_155K\": 0.2, \"ve_ratio_15K\": 0.0306, \"ve_ratio_165K\": 0.1, \"ve_ratio_175K\": 0.3, \"ve_ratio_185K\": 0.3, \"ve_ratio_195K\": 0.3, \"ve_ratio_205K\": 0.2, \"ve_ratio_215K\": 0.1, \"ve_ratio_25K\": 0.1606, \"ve_ratio_35K\": 0.3162, \"ve_ratio_45K\": 0.4807, \"ve_ratio_55K\": 0.4368, \"ve_ratio_65K\": 0.5432, \"ve_ratio_75K\": 0.6211, \"ve_ratio_85K\": 0.9533, \"ve_ratio_95K\": 1.0218}, \"parent\": \"exp_027_tcn_walker_s0_sigma02\", \"status\": \"DONE\", \"updated_at\": \"2026-05-20T19:53:26.097Z\"}, \"exp_029a_tcn_walker_s1_sigma02\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-20T08:31:29.514Z\", \"hypothesis\": \"TCN σ=0.2 multi-seed validation (seed=1): replication of exp_027_tcn_walker_s0_sigma02 which shows NVE<1.0× and eval reaching baseline at 135K. Tests whether CIVO suppression is reproducible across seeds. Same CIVO-inducing config (gate_fixed_dt=2, subsample_max_dt=2, imag_horizon=8) with TCN noise σ=0.2. If s1 also shows NVE<1.0× → TCN σ=0.2 is a robust intervention.\", \"metrics\": {\"current_step\": 215000, \"eval_last10_mean\": 282.15, \"eval_peak\": 401, \"eval_peak_step\": \"125K\", \"eval_return_105K\": 319.4, \"eval_return_115K\": 345.5, \"eval_return_125K\": 401, \"eval_return_135K\": 307.8, \"eval_return_145K\": 380.8, \"eval_return_155K\": 307.3, \"eval_return_15K\": 137.7, \"eval_return_165K\": 320.3, \"eval_return_175K\": 159, \"eval_return_185K\": 278.2, \"eval_return_195K\": 301.2, \"eval_return_205K\": 204.6, \"eval_return_215K\": 161.3, \"eval_return_25K\": 180.9, \"eval_return_35K\": 124, \"eval_return_45K\": 124.2, \"eval_return_55K\": 133.9, \"eval_return_5K\": 36.7, \"eval_return_65K\": 169.7, \"eval_return_75K\": 171.2, \"eval_return_85K\": 151.8, \"eval_return_95K\": 180.3, \"nve_final\": 0.1864, \"nve_max\": 0.6428, \"nve_max_step\": \"55K\", \"target_steps\": 210000, \"ve_ratio_105K\": 0.1554, \"ve_ratio_115K\": 0.1348, \"ve_ratio_125K\": 0.116, \"ve_ratio_135K\": 0.1449, \"ve_ratio_145K\": 0.1088, \"ve_ratio_155K\": 0.1287, \"ve_ratio_15K\": 0.0248, \"ve_ratio_165K\": 0.1142, \"ve_ratio_175K\": 0.2138, \"ve_ratio_185K\": 0.121, \"ve_ratio_195K\": 0.1075, \"ve_ratio_205K\": 0.1503, \"ve_ratio_215K\": 0.1864, \"ve_ratio_25K\": 0.1165, \"ve_ratio_35K\": 0.3574, \"ve_ratio_45K\": 0.5147, \"ve_ratio_55K\": 0.6428, \"ve_ratio_65K\": 0.4777, \"ve_ratio_75K\": 0.398, \"ve_ratio_85K\": 0.4033, \"ve_ratio_95K\": 0.3007}, \"notes\": \"Cron 误报: process exited without sentinel/W&B, 但实验已正常完成 (215K/210K target). NVE max 0.6428@55K (CIVO suppressed), eval peak 401@125K (45% baseline). 对比 parent s0: s0 eval 达 baseline, s1 仅 45% → 高 seed 方差暴露 TCN 脆弱性. 结论 conclusion=success 不变.\", \"parent\": \"exp_027_tcn_walker_s0_sigma02\", \"status\": \"DONE\", \"updated_at\": \"2026-05-20T16:53:36.867Z\"}, \"exp_030b_tcn_cheetah_s0_sigma05\": {\"conclusion\": \"negative\", \"created_at\": \"2026-05-20T11:07:53.975Z\", \"hypothesis\": \"Cheetah CIVO intensity requires higher TCN noise; σ=0.5 may be the environment-appropriate dose (Walker σ=0.5 = overdose causing oscillatory CIVO, Cheetah σ=0.2 = underdose with NVE 1.903@55K). Tests whether TCN effectiveness is environment-dependent with σ scaling to CIVO severity. If NVE<1.5× and eval maintained → TCN is generalizable with environment-tuned σ.\", \"metrics\": {\"current_step\": 195000, \"eval_return_105K\": 104.4, \"eval_return_115K\": 137.7, \"eval_return_125K\": 211.7, \"eval_return_135K\": 97.2, \"eval_return_145K\": 79.4, \"eval_return_155K\": 76.8, \"eval_return_15K\": 78.3, \"eval_return_165K\": 77.5, \"eval_return_175K\": 85.7, \"eval_return_185K\": 68.7, \"eval_return_195K\": 77.6, \"eval_return_25K\": 219.3, \"eval_return_35K\": 296.5, \"eval_return_45K\": 32.8, \"eval_return_55K\": 6, \"eval_return_5K\": 8.3, \"eval_return_65K\": 71.2, \"eval_return_75K\": 23.3, \"eval_return_85K\": 34, \"eval_return_95K\": 143.6, \"nve_final\": 0.1534, \"nve_max\": 10.6657, \"nve_max_step\": \"55K\", \"target_steps\": 210000, \"ve_ratio_105K\": 0.2686, \"ve_ratio_115K\": 0.1789, \"ve_ratio_125K\": 0.1037, \"ve_ratio_135K\": 0.2153, \"ve_ratio_145K\": 0.2478, \"ve_ratio_155K\": 0.2392, \"ve_ratio_15K\": 0.0202, \"ve_ratio_165K\": 0.202, \"ve_ratio_175K\": 0.1591, \"ve_ratio_185K\": 0.1834, \"ve_ratio_195K\": 0.1534, \"ve_ratio_25K\": 0.0636, \"ve_ratio_35K\": 0.1238, \"ve_ratio_45K\": 1.9141, \"ve_ratio_55K\": 10.6657, \"ve_ratio_65K\": 0.8371, \"ve_ratio_75K\": 1.9823, \"ve_ratio_85K\": 1.0946, \"ve_ratio_95K\": 0.2253}, \"parent\": \"\", \"status\": \"DONE\", \"updated_at\": \"2026-05-20T16:49:02.778Z\"}, \"exp_027_tcn_walker_s1\": {\"conclusion\": \"negative\", \"created_at\": \"2026-05-20T05:51:53.479Z\", \"hypothesis\": \"TCN σ=0.5 seed=1: Replication of exp_027_tcn_walker_s0 with different seed to verify that the NVE self-correction phenomenon (transient CIVO at 55K → NVE recovery to 0.83 by 75K) is reproducible across seeds, not a stochastic artifact. Same CIVO-inducing config (gate_fixed_dt=2, subsample_max_dt=2, imag_horizon=8) with TCN noise σ=0.5.\", \"metrics\": {\"eval_last10_mean\": 233.1, \"eval_peak\": 364.9, \"eval_peak_step\": 75000, \"eval_return\": {\"105000\": 216.7, \"115000\": 318.9, \"125000\": 309.1, \"135000\": 216.1, \"145000\": 175.4, \"15000\": 140.5, \"155000\": 171, \"165000\": 209.5, \"175000\": 120.4, \"185000\": 355.4, \"195000\": 183.3, \"205000\": 240.2, \"215000\": 350.8, \"25000\": 163.6, \"35000\": 153, \"45000\": 136.8, \"5000\": 31, \"55000\": 158.3, \"65000\": 298.5, \"75000\": 364.9, \"85000\": 134, \"95000\": 94.6}, \"nve_final\": 0.1476, \"nve_max\": 1.6367, \"nve_max_step\": 95000, \"total_steps\": 215000, \"ve_ratio\": {\"105000\": 0.6444, \"115000\": 0.4021, \"125000\": 0.38, \"135000\": 0.5078, \"145000\": 0.8469, \"15000\": 0.0246, \"155000\": 0.8568, \"165000\": 0.5393, \"175000\": 0.7355, \"185000\": 0.211, \"195000\": 0.3513, \"205000\": 0.2376, \"215000\": 0.1476, \"25000\": 0.1416, \"35000\": 0.3585, \"45000\": 0.6101, \"55000\": 0.7092, \"65000\": 0.4875, \"75000\": 0.4902, \"85000\": 1.4104, \"95000\": 1.6367}}, \"parent\": \"exp_027_tcn_walker_s0\", \"status\": \"DONE\", \"updated_at\": \"2026-05-20T12:45:31.028Z\"}, \"exp_027_tcn_walker_s0_sigma02\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-20T03:25:32.533Z\", \"hypothesis\": \"TCN σ sensitivity test: same as exp_027 (Gaussian noise on dt_embedding during imagination) but with σ=0.2 instead of 0.5. Tests whether smaller noise magnitude is sufficient to disrupt dt-specific value bias. If σ=0.5 works but σ=0.2 doesn't → noise magnitude matters; if both work → method is robust to σ choice.\", \"metrics\": {\"eval_last10_mean\": 587.1, \"eval_peak\": 821.1, \"eval_peak_step\": \"175K\", \"eval_return_105K\": 236.4, \"eval_return_115K\": 543.8, \"eval_return_125K\": 458.4, \"eval_return_135K\": 496.7, \"eval_return_145K\": 542.7, \"eval_return_155K\": 660.5, \"eval_return_15K\": 150.6, \"eval_return_165K\": 653.3, \"eval_return_175K\": 821.1, \"eval_return_185K\": 560.5, \"eval_return_195K\": 567.9, \"eval_return_205K\": 558.7, \"eval_return_215K\": 551, \"eval_return_25K\": 199.4, \"eval_return_35K\": 278.2, \"eval_return_45K\": 315.6, \"eval_return_55K\": 278.6, \"eval_return_5K\": 35.6, \"eval_return_65K\": 331, \"eval_return_75K\": 293.1, \"eval_return_85K\": 363.9, \"eval_return_95K\": 171.4, \"nve_final\": 0.0955, \"nve_max\": 0.9081, \"nve_max_step\": \"95K\", \"total_steps\": 215000, \"ve_ratio_105K\": 0.5625, \"ve_ratio_115K\": 0.2105, \"ve_ratio_125K\": 0.2182, \"ve_ratio_135K\": 0.1764, \"ve_ratio_145K\": 0.143, \"ve_ratio_155K\": 0.106, \"ve_ratio_15K\": 0.0192, \"ve_ratio_165K\": 0.0979, \"ve_ratio_175K\": 0.0729, \"ve_ratio_185K\": 0.1048, \"ve_ratio_195K\": 0.1026, \"ve_ratio_205K\": 0.0995, \"ve_ratio_215K\": 0.0955, \"ve_ratio_25K\": 0.0961, \"ve_ratio_35K\": 0.1875, \"ve_ratio_45K\": 0.3009, \"ve_ratio_55K\": 0.5231, \"ve_ratio_65K\": 0.5654, \"ve_ratio_75K\": 0.611, \"ve_ratio_85K\": 0.4665, \"ve_ratio_95K\": 0.9081}, \"parent\": \"exp_027_tcn_walker_s0\", \"status\": \"DONE\", \"updated_at\": \"2026-05-20T12:06:21.855Z\"}, \"exp_030a_tcn_cheetah_s0_sigma02\": {\"conclusion\": \"negative\", \"created_at\": \"2026-05-20T09:24:38.711Z\", \"hypothesis\": \"TCN σ=0.2 cross-environment validation on Cheetah Run: tests whether CIVO suppression generalizes beyond Walker Walk. Cheetah exhibits stronger CIVO (NVE 8.27-70.64× in exp_010b) so this is a harder test. Same CIVO-inducing config (gate_fixed_dt=2, subsample_max_dt=2, imag_horizon=8) + TCN σ=0.2. If NVE<1.5× and eval maintained → TCN is environment-agnostic intervention.\", \"metrics\": {\"current_step\": 64000, \"eval_return_35K\": 299.5, \"eval_return_55K\": 31.9, \"note\": \"WARNING: NVE breached 1.5× at 55K (1.903), eval crashed 299→32. Possible CIVO despite TCN.\", \"target_steps\": 210000, \"ve_ratio_55K\": 1.903}, \"parent\": \"exp_027_tcn_walker_s0_sigma02\", \"status\": \"DONE\", \"updated_at\": \"2026-05-20T11:10:00.827Z\"}, \"exp_027_tcn_walker_s0\": {\"conclusion\": \"negative\", \"created_at\": \"2026-05-20T02:44:51.820Z\", \"hypothesis\": \"Temporal Conditioning Noise (TCN): adding Gaussian noise (sigma=0.5) to dt_embedding during imagination rollouts reduces dt conditioning precision, preventing critic from learning dt-specific value bias. Predicts CIVO suppression (NVE < 1.5×) with eval > 50% baseline (~450+). Based on obs-decoder SGS failure (gradient-level intervention insufficient) → need forward-pass/representation-level intervention.\", \"metrics\": {\"eval_return_105K\": 95.5, \"eval_return_112K\": 99.5, \"eval_return_15K\": 154.6, \"eval_return_25K\": 223.6, \"eval_return_35K\": 240, \"eval_return_45K\": 101.2, \"eval_return_55K\": 70, \"eval_return_5K\": 37.4, \"eval_return_65K\": 95.1, \"eval_return_75K\": 189.2, \"eval_return_85K\": 36, \"eval_return_95K\": 166.4, \"final_step\": 120000, \"gate_dt_entropy\": 0, \"gate_dt_mean\": 2, \"last_5_eval_avg\": 117.3, \"nve_breach_count\": 3, \"nve_breach_steps\": \"55K(1.68), 65K(1.54), 85K(3.97)\", \"peak_eval\": 240, \"peak_eval_step\": \"35K\", \"peak_nve\": 3.965, \"peak_nve_step\": \"85K\", \"target_steps\": 210000, \"ve_ratio_105K\": 0.916, \"ve_ratio_15K\": 0.02, \"ve_ratio_25K\": 0.11, \"ve_ratio_35K\": 0.235, \"ve_ratio_45K\": 0.86, \"ve_ratio_55K\": 1.679, \"ve_ratio_65K\": 1.544, \"ve_ratio_75K\": 0.831, \"ve_ratio_85K\": 3.965, \"ve_ratio_95K\": 0.675}, \"parent\": \"exp_025_obs_sgs_walker_s1\", \"status\": \"DONE\", \"updated_at\": \"2026-05-20T09:24:09.016Z\"}, \"exp_028_rave_walker_s0_ceil15\": {\"conclusion\": \"negative\", \"created_at\": \"2026-05-20T03:25:34.045Z\", \"hypothesis\": \"RAVE ceiling sensitivity test: same as exp_028 (EMA-anchored value cap) but with ceiling=1.5 instead of 2.0. Tighter constraint tests whether more aggressive capping improves CIVO suppression without harming learning. If ceiling=2.0 works and 1.5 also works → method robust; if 1.5 hurts eval → ceiling choice is critical.\", \"metrics\": {\"current_step\": 135000, \"eval_return_105K\": 76.2, \"eval_return_115K\": 41.2, \"eval_return_125K\": 36.6, \"eval_return_135K\": 39.1, \"eval_return_15K\": 99.4, \"eval_return_25K\": 155.3, \"eval_return_35K\": 180.1, \"eval_return_45K\": 166.9, \"eval_return_55K\": 131, \"eval_return_5K\": 31.6, \"eval_return_65K\": 91.5, \"eval_return_75K\": 120.9, \"eval_return_85K\": 137.3, \"eval_return_95K\": 70.2, \"target_steps\": 210000, \"ve_ratio_105K\": 0.984, \"ve_ratio_115K\": 1.513, \"ve_ratio_125K\": 1.462, \"ve_ratio_135K\": 1.171, \"ve_ratio_15K\": 0.03, \"ve_ratio_25K\": 0.128, \"ve_ratio_35K\": 0.247, \"ve_ratio_45K\": 0.428, \"ve_ratio_55K\": 0.737, \"ve_ratio_65K\": 1.294, \"ve_ratio_75K\": 0.937, \"ve_ratio_85K\": 0.727, \"ve_ratio_95K\": 1.28}, \"parent\": \"exp_028_rave_walker_s0\", \"status\": \"DONE\", \"updated_at\": \"2026-05-20T08:31:12.389Z\"}, \"exp_028_rave_walker_s0\": {\"conclusion\": \"negative\", \"created_at\": \"2026-05-20T02:44:53.882Z\", \"hypothesis\": \"Reality-Anchored Value Estimation (RAVE): cap imagination critic values at ceiling*v_anchor (ceiling=2.0, v_anchor=EMA of real-state critic values). Directly prevents pathological value inflation (NVE>1.5×) by bounding imagination/reality value ratio. Based on CIVO core mechanism being imagination value explosion → this directly caps the ratio without modifying gradients or training dynamics.\", \"metrics\": {\"current_steps\": 105000, \"eval_trajectory\": {\"105K\": {\"eval_return\": 29, \"value_mean\": 92.2, \"ve_ratio\": 3.183}, \"15K\": {\"eval_return\": 105.3, \"value_mean\": 2.93, \"ve_ratio\": 0.028}, \"25K\": {\"eval_return\": 191.9, \"value_mean\": 24.4, \"ve_ratio\": 0.127}, \"35K\": {\"eval_return\": 204.6, \"ve_ratio\": 0.267}, \"45K\": {\"eval_return\": 197.7, \"ve_ratio\": 0.439}, \"55K\": {\"eval_return\": 193, \"ve_ratio\": 0.62}, \"5K\": {\"eval_return\": 37.4, \"value_mean\": 0.001}, \"65K\": {\"eval_return\": 79.8, \"ve_ratio\": 1.832}, \"75K\": {\"eval_return\": 44.5, \"ve_ratio\": 3.415}, \"85K\": {\"eval_return\": 57.7, \"ve_ratio\": 2.126}, \"95K\": {\"eval_return\": 25.9, \"value_mean\": 105.87, \"ve_ratio\": 4.086}}, \"note\": \"NEGATIVE. NVE diverged from 55K onward (0.62→4.09), eval collapsed 193→29. No self-correction.\"}, \"parent\": \"exp_025_obs_sgs_walker_s1\", \"status\": \"DONE\", \"updated_at\": \"2026-05-20T06:14:31.720Z\"}, \"exp_025_obs_sgs_walker_s2\": {\"conclusion\": \"negative\", \"created_at\": \"2026-05-19T16:39:26.941Z\", \"hypothesis\": \"Obs-decoder-only SGS (stop-gradient only on observation decoder pathway to dt_embedding) will suppress CIVO while preserving reward head gradient signal. Based on gradient decomposition showing obs decoder (16-22%) not reward head (38-49%) carries the critical dt-specific spatial information driving the fidelity gap. Predicts NVE < 1.5× and eval > 70% baseline (~650+).\", \"metrics\": {\"eval_return_215K\": 89.6, \"target_steps\": 210000, \"train_steps_completed\": 224000, \"ve_ratio_175K\": 1.2, \"ve_ratio_185K\": 1.4, \"ve_ratio_215K\": 0.8}, \"notes\": \"Obs-decoder SGS s2 完成全部训练（224K/210K steps）。ve_ratio 全程 0.8-1.4（CIVO 部分抑制），但 eval_return 仅 66-90（baseline ~930，远低于 70% 阈值 ~650）。与 s1/s3/s4 一致：obs-decoder SGS 无法在抑制 CIVO 的同时保持性能。梯度干预路线全面否定（Full SGS 0/3 + Obs-decoder SGS 0/6 有效）。\", \"parent\": \"exp_018_full_sgs_walker_s1\", \"status\": \"DONE\", \"updated_at\": \"2026-05-20T03:17:26.061Z\"}, \"exp_026_obs_sgs_cheetah_s1\": {\"conclusion\": \"failed\", \"created_at\": \"2026-05-19T20:19:29.171Z\", \"hypothesis\": \"Obs-decoder-only SGS on Cheetah Run: cross-environment validation that obs-decoder SGS suppresses CIVO in a second environment. Based on 010b showing Cheetah CIVO (NVE 8.27-70.64×), if obs-decoder SGS works, NVE should stay < 1.5× and eval > 70% of Cheetah baseline (~380+). Tests whether the gradient decomposition finding (obs decoder as critical pathway) generalizes beyond Walker.\", \"parent\": \"exp_010b_cheetah_civo_trigger\", \"status\": \"DONE\", \"updated_at\": \"2026-05-20T03:02:46.556Z\"}, \"exp_026_obs_sgs_cheetah_s0\": {\"conclusion\": \"failed\", \"created_at\": \"2026-05-19T20:19:27.608Z\", \"hypothesis\": \"Obs-decoder-only SGS on Cheetah Run: cross-environment validation that obs-decoder SGS suppresses CIVO in a second environment. Based on 010b showing Cheetah CIVO (NVE 8.27-70.64×), if obs-decoder SGS works, NVE should stay < 1.5× and eval > 70% of Cheetah baseline (~380+). Tests whether the gradient decomposition finding (obs decoder as critical pathway) generalizes beyond Walker.\", \"parent\": \"exp_010b_cheetah_civo_trigger_s0\", \"status\": \"DONE\", \"updated_at\": \"2026-05-20T03:02:43.170Z\"}, \"exp_025_obs_sgs_walker_s4\": {\"conclusion\": \"failed\", \"created_at\": \"2026-05-19T16:39:29.810Z\", \"hypothesis\": \"Obs-decoder-only SGS (stop-gradient only on observation decoder pathway to dt_embedding) will suppress CIVO while preserving reward head gradient signal. Based on gradient decomposition showing obs decoder (16-22%) not reward head (38-49%) carries the critical dt-specific spatial information driving the fidelity gap. Predicts NVE < 1.5× and eval > 70% baseline (~650+).\", \"parent\": \"exp_018_full_sgs_walker_s1\", \"status\": \"DONE\", \"updated_at\": \"2026-05-20T03:02:39.948Z\"}, \"exp_025_obs_sgs_walker_s3\": {\"conclusion\": \"failed\", \"created_at\": \"2026-05-19T16:39:28.402Z\", \"hypothesis\": \"Obs-decoder-only SGS (stop-gradient only on observation decoder pathway to dt_embedding) will suppress CIVO while preserving reward head gradient signal. Based on gradient decomposition showing obs decoder (16-22%) not reward head (38-49%) carries the critical dt-specific spatial information driving the fidelity gap. Predicts NVE < 1.5× and eval > 70% baseline (~650+).\", \"parent\": \"exp_018_full_sgs_walker_s1\", \"status\": \"DONE\", \"updated_at\": \"2026-05-20T03:02:36.670Z\"}, \"exp_025_obs_sgs_walker_s1\": {\"conclusion\": \"failed\", \"created_at\": \"2026-05-19T16:39:25.583Z\", \"hypothesis\": \"Obs-decoder-only SGS (stop-gradient only on observation decoder pathway to dt_embedding) will suppress CIVO while preserving reward head gradient signal. Based on gradient decomposition showing obs decoder (16-22%) not reward head (38-49%) carries the critical dt-specific spatial information driving the fidelity gap. Predicts NVE < 1.5× and eval > 70% baseline (~650+).\", \"parent\": \"exp_018_full_sgs_walker_s1\", \"status\": \"DONE\", \"updated_at\": \"2026-05-20T03:02:32.583Z\"}, \"exp_001_baseline_s4_extended\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-19T09:02:31.737Z\", \"hypothesis\": \"Walker Walk baseline seed=4 extended to 505K. Third long-run baseline seed for multi-seed NVE normalization. s4@105K=922.8 (highest), obtaining full ve_ratio profile.\", \"metrics\": {\"convergence_mean_250k_plus\": 935, \"final_eval_return\": 938.86, \"final_step\": 520000, \"peak_eval_return\": 960.6}, \"parent\": \"exp_001_baseline_s4\", \"status\": \"DONE\", \"updated_at\": \"2026-05-19T23:06:42.122Z\"}, \"exp_001_baseline_s3_extended\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-19T09:02:30.382Z\", \"hypothesis\": \"Walker Walk baseline seed=3 extended to 505K. Second long-run baseline seed (alongside s2_ext) for multi-seed NVE normalization robustness. s3@105K=869.0, testing convergence to 920+ level.\", \"metrics\": {\"eval_profile\": {\"102000\": 869.03, \"112000\": 898.89, \"120000\": 898.38, \"130000\": 837.74, \"140000\": 876.64, \"15000\": 224.27, \"150000\": 899.47, \"160000\": 922.77, \"170000\": 925.77, \"180000\": 912.89, \"190000\": 915.07, \"200000\": 894.77, \"210000\": 899.79, \"220000\": 951.18, \"230000\": 930.56, \"240000\": 910.47, \"25000\": 329.99, \"250000\": 914.02, \"260000\": 931.33, \"270000\": 954.65, \"280000\": 928.01, \"290000\": 947.4, \"300000\": 853.32, \"310000\": 906.35, \"320000\": 847.16, \"330000\": 934.78, \"340000\": 921.08, \"35000\": 413.12, \"350000\": 922.63, \"360000\": 844.99, \"370000\": 911.36, \"380000\": 917.73, \"390000\": 937.21, \"400000\": 928, \"410000\": 945.88, \"420000\": 897.2, \"430000\": 949.45, \"440000\": 937.28, \"45000\": 332.69, \"450000\": 924.24, \"460000\": 967.25, \"470000\": 940.55, \"480000\": 936.24, \"490000\": 944.67, \"5000\": 42.15, \"500000\": 957.09, \"510000\": 947.68, \"55000\": 519.91, \"65000\": 667.42, \"72000\": 771.33, \"82000\": 772.88, \"92000\": 854.6}, \"final_eval_return\": 947.68, \"final_step\": 520000, \"final_train_return_avg\": 945.4}, \"parent\": \"exp_001_baseline_s3\", \"status\": \"DONE\", \"updated_at\": \"2026-05-19T21:23:44.025Z\"}, \"exp_001_baseline_s2_extended\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-19T04:10:10.948Z\", \"hypothesis\": \"Walker Walk baseline seed=2 extended to 505K. Tests whether low eval (443.5 @105K) is due to slow convergence or seed-level difference. s1=915.7, s3=869.0 at 105K.\", \"metrics\": {\"eval_return_at_105K\": 443.5, \"eval_return_final\": 945.7, \"eval_return_peak\": 962.6, \"total_steps\": 512000, \"value_mean_at_105K\": 329.16, \"value_mean_plateau\": 665, \"ve_ratio_at_105K\": 0.7422, \"ve_ratio_converged_range\": \"0.69-0.77\"}, \"parent\": \"exp_001_baseline_s2\", \"status\": \"DONE\", \"updated_at\": \"2026-05-19T17:44:27.212Z\"}, \"exp_023_cheetah_baseline_s4_extended\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-19T06:27:42.161Z\", \"hypothesis\": \"Cheetah Run baseline seed=4 extended to 300K. Tests whether eval drop at 194K→204K (537→302) is transient fluctuation or permanent collapse. Informs baseline stability and NVE normalization robustness.\", \"metrics\": {\"eval_302k\": 580, \"eval_peak_ext\": 642.3, \"eval_peak_ext_step\": 272000, \"note\": \"延长到 300K 确认非 collapse。eval 恢复到 642 peak@272K，200K-300K 区间震荡上行 (301-642 range)，194K→204K 骤降为 transient fluctuation。\"}, \"parent\": \"exp_023_cheetah_baseline_s4\", \"status\": \"DONE\", \"updated_at\": \"2026-05-19T09:02:40.466Z\"}, \"exp_001_baseline_s4\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-19T04:47:01.105Z\", \"hypothesis\": \"Walker Walk baseline seed=4. Fourth seed for 4-seed baseline CI. Tests whether s2 (443.5) is outlier or bimodal distribution (s1=915.7, s3=869.0).\", \"metrics\": {\"current_step\": 112000, \"eval_return_105k\": 922.8, \"peak_eval\": 922.8, \"peak_eval_step\": 105000, \"target_steps\": 105000, \"value_mean_final\": 576.1, \"ve_ratio_105k\": 0.624}, \"parent\": \"exp_001_baseline\", \"status\": \"DONE\", \"updated_at\": \"2026-05-19T09:00:10.632Z\"}, \"exp_023_cheetah_baseline_s4\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-18T23:54:02.288Z\", \"hypothesis\": \"Cheetah Run baseline seed=4. Fourth seed for tighter eval return CI and NVE normalization robustness.\", \"metrics\": {\"current_step\": 212000, \"eval_return_194k\": 537.03, \"eval_return_204k\": 301.69, \"note\": \"Cheetah baseline s4. Large eval drop 194K→204K (537→302). ve_ratio>1 indicates value overestimation at final step.\", \"peak_eval\": 537.03, \"peak_eval_step\": 194000, \"target_steps\": 200000, \"value_mean_204k\": 339.14, \"ve_ratio_204k\": 1.124}, \"parent\": \"exp_023a_cheetah_baseline_s0\", \"status\": \"DONE\", \"updated_at\": \"2026-05-19T06:26:03.295Z\"}, \"exp_023_cheetah_baseline_s3\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-18T21:49:33.229Z\", \"hypothesis\": \"Cheetah Run baseline seed=3. Extends 023a/023b/023_s2 (3 seeds) to 4 seeds for tighter eval return CI.\", \"metrics\": {\"current_step\": 204000, \"eval_return_202k\": 642.13, \"peak_eval\": 685.93, \"peak_eval_step\": 172000, \"target_steps\": 200000, \"value_mean_final\": 445.42, \"ve_ratio_final\": 0.694}, \"parent\": \"exp_023a_cheetah_baseline_s0\", \"status\": \"DONE\", \"updated_at\": \"2026-05-19T04:08:47.459Z\"}, \"exp_001_baseline_s3\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-18T23:54:03.635Z\", \"hypothesis\": \"Walker Walk baseline seed=3. Third seed for tighter baseline eval CI.\", \"metrics\": {\"current_step\": 120000, \"eval_return_102k\": 869.03, \"peak_eval\": 898.89, \"peak_eval_step\": 112000, \"target_steps\": 105000, \"value_mean_final\": 622.2, \"ve_ratio_final\": 0.692}, \"parent\": \"exp_001_baseline\", \"status\": \"DONE\", \"updated_at\": \"2026-05-19T04:08:45.989Z\"}, \"exp_023_cheetah_baseline_s2\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-18T16:05:14.249Z\", \"hypothesis\": \"Cheetah Run baseline additional seed for tighter CI. Extends 023a/023b (2 seeds) to 3 seeds.\", \"metrics\": {\"current_step\": 205000, \"eval_return_final\": 645.4, \"note\": \"Cheetah Run baseline seed=2. Third baseline seed for NVE normalization.\", \"target_steps\": 200000}, \"parent\": \"exp_023a_cheetah_baseline_s0\", \"status\": \"DONE\", \"updated_at\": \"2026-05-19T00:13:55.909Z\"}, \"exp_008f_s4\": {\"conclusion\": \"negative\", \"created_at\": \"2026-05-18T18:41:00.894Z\", \"hypothesis\": \"Walker Walk no-dt-emb (gate_dt_embed_dim=0) + subsample ON + fixed dt=2 + H=8, seed=4. Additional independent seed for 008f control (existing seeds: 1/008f, 2/009c, 3/008f_s3). C2 causal contrast robustness.\", \"metrics\": {\"civo_alert\": 0, \"eval_return_105k\": 306.5, \"note\": \"No CIVO. No-dt-emb control seed=4. Peak NVE 1.41x @85K (transient), settles to 0.58x @105K.\", \"nve_105k\": 0.58, \"peak_eval\": 487.5, \"peak_eval_step\": 55000, \"peak_nve\": 1.41, \"peak_nve_step\": 85000}, \"parent\": \"exp_008f_no_dt_embed_subsample_on_h8\", \"status\": \"DONE\", \"updated_at\": \"2026-05-18T23:18:51.672Z\"}, \"exp_009c_s3\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-18T17:12:00.539Z\", \"hypothesis\": \"Walker Walk no-dt-emb (gate_dt_embed_dim=0) + subsample ON + fixed dt=2 + H=8, seed=3. Additional seed for 009c (seed=2 NVE 1.14x at 105K on upward trajectory); tests whether NVE rise is reproducible across independent seeds or stochastic.\", \"metrics\": {\"current_step\": 108000, \"eval_return_105k\": 311.92, \"note\": \"eval peaked at 55-65K (~457) then declined to 311.92. NVE 0.52x (no CIVO). 009c seed=2 NVE 1.14x not reproduced.\", \"nve_105k\": 0.52, \"target_steps\": 105000, \"value_mean_105k\": 120.27, \"ve_ratio_105k\": 0.386}, \"parent\": \"exp_009c_008f_walker_s2\", \"status\": \"DONE\", \"updated_at\": \"2026-05-18T21:40:10.762Z\"}, \"exp_001_baseline_s2\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-18T16:05:17.571Z\", \"hypothesis\": \"Walker Walk baseline additional seed for tighter evaluation return CI.\", \"metrics\": {\"current_step\": 112000, \"eval_return_105k\": 443.46, \"target_steps\": 105000, \"value_mean_105k\": 329.16, \"ve_ratio_105k\": 0.742}, \"parent\": \"exp_001_baseline\", \"status\": \"DONE\", \"updated_at\": \"2026-05-18T21:40:09.329Z\"}, \"exp_008f_s2\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-18T16:05:16.527Z\", \"hypothesis\": \"No-dt-emb control additional seed. Extends 008f (1 seed, NVE 0.97x) for C2 causal contrast robustness.\", \"parent\": \"exp_008f_no_dt_embed_subsample_on_h8\", \"status\": \"DONE\", \"updated_at\": \"2026-05-18T18:41:05.369Z\"}, \"exp_008a_cheetah_unexposed_s1\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-18T14:23:13.377Z\", \"hypothesis\": \"Cross-environment validation of C3 (unexposed dt_emb protection) on Cheetah Run, seed=1. If unexposed dt_emb (trained but subsample OFF, gate_subsample_max_dt=1) prevents CIVO in Cheetah as it does in Walker (008a: 3/3 healthy, NVE 0.43-0.93x), this strengthens the causal claim that multi-rate data exposure is the necessary CIVO trigger across environments.\", \"metrics\": {\"current_step\": 112000, \"eval_return_105k\": 504.38, \"nve_105k\": 0.478, \"target_steps\": 105000, \"value_mean_105k\": 156.97, \"ve_ratio_105k\": 0.3112}, \"parent\": \"exp_008a_no_subsample_dt2\", \"status\": \"DONE\", \"updated_at\": \"2026-05-18T18:20:00.278Z\"}, \"exp_008a_cheetah_unexposed_s0\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-18T14:23:12.052Z\", \"hypothesis\": \"Cross-environment validation of C3 (unexposed dt_emb protection) on Cheetah Run, seed=0. If unexposed dt_emb (trained but subsample OFF, gate_subsample_max_dt=1) prevents CIVO in Cheetah as it does in Walker (008a: 3/3 healthy, NVE 0.43-0.93x), this strengthens the causal claim that multi-rate data exposure is the necessary CIVO trigger across environments.\", \"metrics\": {\"current_step\": 112000, \"eval_return_105k\": 532.35, \"nve_105k\": 0.49, \"target_steps\": 105000, \"value_mean_105k\": 169.98, \"ve_ratio_105k\": 0.3193}, \"parent\": \"exp_008a_no_subsample_dt2\", \"status\": \"DONE\", \"updated_at\": \"2026-05-18T18:19:58.491Z\"}, \"exp_009c_s2\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-18T16:05:19.850Z\", \"hypothesis\": \"No-dt-emb H=15 additional seed. 009c seed=2 showed NVE 1.14x at 105K on upward trajectory; additional seed tests if this is reproducible or stochastic.\", \"parent\": \"exp_009c_008f_walker_s2\", \"status\": \"DONE\", \"updated_at\": \"2026-05-18T17:12:05.307Z\"}, \"exp_008e_v3_s4\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-18T02:54:56.392Z\", \"hypothesis\": \"Walker Walk trained dt_emb + subsample ON + dt=1 imag + H=15, seed=4. C6 dual-pathway 多 seed 验证：当前 2 seeds 50% collapse rate（置信区间太宽），增加 seed 缩窄置信区间。Rebuttal 储备。\", \"metrics\": {\"civo\": false, \"eval_return\": 899.3, \"nve_note\": \"Corrected: was 0.61 (raw V/E ratio). Correct formula: max(V/E_exp / V/E_baseline_at_same_step) over [35K+]. 0.627/0.632=0.99 at 95K\", \"nve_peak\": 0.99, \"nve_peak_step\": 95000, \"ve_ratio_105k\": 0.609}, \"parent\": \"exp_008e_v3_subsample_on_dt1_h15\", \"status\": \"DONE\", \"updated_at\": \"2026-05-18T11:48:45.880Z\"}, \"exp_008e_v3_s3\": {\"conclusion\": \"negative\", \"created_at\": \"2026-05-18T02:54:54.691Z\", \"hypothesis\": \"Walker Walk trained dt_emb + subsample ON + dt=1 imag + H=15, seed=3. C6 dual-pathway 多 seed 验证：当前 2 seeds 50% collapse rate（置信区间太宽），增加 seed 缩窄置信区间。Rebuttal 储备。\", \"metrics\": {\"actor_entropy_final\": -4.892, \"collapse_onset\": \"85K-95K\", \"eval_return\": 92.7, \"gate_dt_1_frac\": 1, \"gate_dt_mean\": 1, \"nve_note\": \"Corrected: was 5.00 (worker used wrong baseline). Correct formula: V/E_exp / V/E_baseline_at_same_step. 2.635/0.656=4.02\", \"nve_peak\": 4.02, \"nve_peak_step\": 105000, \"peak_eval\": 520.4, \"peak_step\": 85000, \"ve_ratio_105k\": 2.635}, \"parent\": \"exp_008e_v3_subsample_on_dt1_h15\", \"status\": \"DONE\", \"updated_at\": \"2026-05-18T11:48:43.665Z\"}, \"exp_008a_unexposed_s1\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-18T05:13:56.020Z\", \"hypothesis\": \"Walker Walk unexposed trained dt_emb + subsample OFF (gate_subsample_max_dt=1) + gate_fixed_dt=2 + H=15 (default), seed=1. 直接复现 008a_no_subsample_dt2 配置（eval=778, V-recovery, no CIVO）。C3 reproducibility rebuttal 储备。\", \"metrics\": {\"civo_alert\": 0, \"civo_delta_ve_final\": -0.0028, \"civo_ve_ratio_final\": 0.43, \"eval_return_15k\": 167.12, \"eval_return_25k\": 139.94, \"eval_return_35k\": 394.15, \"eval_return_45k\": 414.32, \"eval_return_55k\": 441.48, \"eval_return_5k\": 31, \"eval_return_65k\": 491.74, \"eval_return_75k\": 452.34, \"eval_return_85k\": 546.82, \"eval_return_95k\": 628.57, \"eval_return_final\": 630.91, \"gate_dt_2_frac\": 1, \"gate_dt_mean\": 2, \"target_mean_final\": 272.13, \"total_steps\": 105000, \"value_mean_final\": 271.36}, \"parent\": \"exp_008a_no_subsample_dt2\", \"status\": \"DONE\", \"updated_at\": \"2026-05-18T08:16:42.716Z\"}, \"exp_008a_unexposed_s2\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-18T05:13:57.340Z\", \"hypothesis\": \"Walker Walk unexposed trained dt_emb + subsample OFF (gate_subsample_max_dt=1) + gate_fixed_dt=2 + H=15 (default), seed=2. 008a 新 seed 验证 protection 是否 reproducible。C3 rebuttal 储备。\", \"metrics\": {\"civo_alert\": 0, \"civo_delta_ve_final\": -0.003, \"civo_ve_ratio_final\": 0.333, \"eval_return_55k\": 607.5, \"eval_return_65k\": 653.8, \"eval_return_75k\": 534.4, \"eval_return_85k\": 605.4, \"eval_return_95k\": 819.4, \"eval_return_final\": 899.4, \"gate_dt_2_frac\": 1, \"gate_dt_mean\": 2, \"target_mean_final\": 300.3, \"total_steps\": 105000, \"value_mean_final\": 299.4}, \"parent\": \"exp_008a_no_subsample_dt2\", \"status\": \"DONE\", \"updated_at\": \"2026-05-18T08:10:17.263Z\"}, \"exp_008a_untrained_s1\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-18T02:54:51.398Z\", \"hypothesis\": \"(cancelled) 原为 015b 模板 frozen dt_emb 多 seed，Director 修正为 008a unexposed 模板\", \"notes\": \"Director 修正：C3 rebuttal 应复现 008a (unexposed trained dt_emb, subsample OFF) 而非 015b (frozen)。替换为 exp_008a_unexposed_s1/s2。\", \"parent\": \"exp_015b_frozen_dt_emb\", \"status\": \"DONE\", \"updated_at\": \"2026-05-18T05:13:30.000Z\"}, \"exp_008a_untrained_s2\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-18T02:54:53.011Z\", \"hypothesis\": \"(cancelled) 原为 015b 模板 frozen dt_emb 多 seed，Director 修正为 008a unexposed 模板\", \"notes\": \"Director 修正：同上。\", \"parent\": \"exp_015b_frozen_dt_emb\", \"status\": \"DONE\", \"updated_at\": \"2026-05-18T05:13:30.000Z\"}, \"exp_010b_cheetah_civo_trigger_s0\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-18T02:02:47.702Z\", \"hypothesis\": \"Cheetah Run CIVO trigger seed=0: trained dt_emb + subsample ON + H=8. 第二 seed 复现 Cheetah CIVO (NVE>1.5×)，加强跨环境因果论证统计力度。Rebuttal 储备。\", \"metrics\": {\"civo\": true, \"civo_onset_step\": \"65K\", \"detector_alert_step\": \"95K\", \"eval_return_105K\": 0.83, \"eval_return_peak\": 247.77, \"eval_return_peak_step\": \"35K\", \"gate_dt_mean\": 2, \"gate_entropy\": 0, \"nve_105K\": 70.64, \"nve_95K\": 6.34}, \"parent\": \"exp_010b_cheetah_civo_trigger\", \"status\": \"DONE\", \"updated_at\": \"2026-05-18T05:11:15.900Z\"}, \"exp_024b_cheetah_no_dt_emb_s0\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-17T22:50:34.104Z\", \"hypothesis\": \"Cheetah Run no-dt-emb causal control: dt_embed_dim=0 + subsample ON + H=8. 预期无CIVO（健康基线水平），证明trained dt_emb是Cheetah CIVO的必要条件。对应Walker的008f逻辑，完成Cheetah因果三角。\", \"metrics\": {\"civo\": false, \"eval_return_final\": 96.5, \"nve_peak\": 0.2}, \"notes\": \"No CIVO (NVE peak <0.2×). Confirms C2: trained dt_emb is necessary for Cheetah CIVO. eval 96.5 = 17.6% of baseline (548.3). Cheetah causal triangle seed 1 complete. Director confirmed results in D089.\", \"parent\": \"exp_010b_cheetah_civo_trigger\", \"status\": \"DONE\", \"updated_at\": \"2026-05-18T02:00:17.832Z\"}, \"exp_024b_cheetah_no_dt_emb_s1\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-17T22:51:53.604Z\", \"hypothesis\": \"Cheetah Run no-dt-emb causal control seed=1: gate_dt_embed_dim=0 + subsample ON + H=8. 第二 seed 验证 024 的结论（trained dt_emb 是 Cheetah CIVO 必要条件），加强因果三角的统计力度。\", \"metrics\": {\"baseline_pct\": 14.1, \"civo\": false, \"eval_return_final\": 77.3, \"eval_return_peak\": 129.6, \"gate_dt_2_frac\": 1, \"nve_peak\": 0.1, \"peak_step\": 15000}, \"notes\": \"No CIVO (NVE peak 0.10×, civo_alert=0 throughout). Confirms C2: trained dt_emb is necessary for Cheetah CIVO. Gate locked at dt=2 (gate_dt_2_frac=1.0), eval 77.3 = 14% of baseline (548.3). Low performance expected: dt_embed_dim=0 removes temporal abstraction capability. Cheetah causal triangle seed 2 complete.\", \"parent\": \"exp_024_cheetah_no_dt_emb_s0\", \"status\": \"DONE\", \"updated_at\": \"2026-05-18T01:56:17.025Z\"}, \"exp_024_cheetah_no_dt_emb_s0\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-17T20:34:13.657Z\", \"hypothesis\": \"Cheetah Run no-dt-emb causal control: dt_embed_dim=0 + subsample ON + H=8. 预期无CIVO（健康基线水平），证明trained dt_emb是Cheetah CIVO的必要条件。对应Walker的008f逻辑，完成Cheetah因果三角（023a/b baseline健康 + 010b CIVO collapse + 本实验 no-emb 健康）。\", \"parent\": \"exp_010b_cheetah_civo_trigger\", \"status\": \"DONE\", \"updated_at\": \"2026-05-17T23:21:27.867Z\"}, \"exp_021_full_sgs_cheetah_s1\": {\"conclusion\": \"negative\", \"created_at\": \"2026-05-16T20:24:30.695Z\", \"hypothesis\": \"Full-SGS Cheetah Run — 验证 SGS intervention 跨环境一致性。如果 CIVO mechanism 跨环境一致，Full-SGS 在 Cheetah 也应消除 NVE>1.5x (对比 010b: NVE 8.63×, collapse)。\", \"metrics\": {\"baseline_pct\": 38.7, \"civo\": true, \"civo_type\": \"transient_self_correcting\", \"eval_return_final\": 221.5, \"nve_peak\": 9.94, \"nve_peak_step\": \"45K\", \"nve_sustained_55K_105K\": 0.338, \"vs_010b\": \"221.5 vs 51.7 (4.3x better)\"}, \"notes\": \"P0 priority (D070 最重要数据缺口). 018_s2 完成后立即上 cuda:0. 排序: 021 先 → 008d_s1 后. Director 2026-05-16 确认.\", \"parent\": \"exp_010b_cheetah_civo_trigger\", \"status\": \"DONE\", \"updated_at\": \"2026-05-17T22:57:30.295Z\"}, \"exp_023a_cheetah_baseline_s0\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-17T11:53:19.690Z\", \"hypothesis\": \"Cheetah Run vanilla DreamerV3 baseline (dt=1, no temporal embedding, no gate). Establishes Cheetah-specific baseline for NVE normalization and cross-environment validation. Comparison target for 010b (Cheetah CIVO trigger, NVE 8.27×).\", \"metrics\": {\"civo\": false, \"eval_return_final\": 624.7, \"eval_return_peak\": 624.7, \"peak_step\": 205000}, \"notes\": \"Healthy baseline. Last-5 eval mean=554.4. 185K瞬态VE spike(0.906)触发警报但20K步内恢复(205K:624.7)，非CIVO。双seed baseline均值: last-5=548.3, peak=598.8。未接W&B。\", \"status\": \"DONE\", \"updated_at\": \"2026-05-17T20:41:57.147Z\"}, \"exp_010b_cheetah_civo_trigger\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-16T13:04:55.508Z\", \"hypothesis\": \"Cheetah Run CIVO trigger — trained dt_emb, subsample ON, dt=2, H=8, seed 1. 跨环境验证：Walker 上 008d 配置在 Cheetah 上是否同样触发 CIVO (NVE>1.5x)。若成立→回应 reviewer \\\"single environment\\\" concern。\", \"metrics\": {\"civo\": true, \"eval_return_final\": 51.7, \"eval_return_peak\": 321.9, \"nve_peak\": 8.27, \"nve_peak_step\": 65000, \"peak_step\": 35000}, \"parent\": \"exp_010a_cheetah_baseline_s1\", \"status\": \"DONE\", \"updated_at\": \"2026-05-17T20:41:38.129Z\"}, \"exp_023b_cheetah_baseline_s1\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-17T11:53:21.197Z\", \"hypothesis\": \"Cheetah Run vanilla DreamerV3 baseline (dt=1, no temporal embedding, no gate), seed=1. Second seed for Cheetah baseline to establish robust NVE normalization across seeds.\", \"metrics\": {\"civo\": false, \"eval_return_final\": 520.3, \"eval_return_peak\": 572.9, \"peak_step\": 195000, \"ve_ratio_range\": \"0.5-0.7\"}, \"notes\": \"Healthy baseline. Last-5 eval mean=542.2 (for NVE normalization). 125K后进入500-573区间震荡，无collapse。待023a完成后取双seed均值作为Cheetah baseline。未接W&B，数据在本地logdir。\", \"status\": \"DONE\", \"updated_at\": \"2026-05-17T19:30:46.627Z\"}, \"exp_019b_pickcube_civo_trigger\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-16T03:23:51.568Z\", \"hypothesis\": \"PickCube-v1 CIVO trigger — trained dt_emb, subsample ON, dt=2 imagination, H=8. 预期触发 CIVO（trained dt_emb → NVE>1.5x → collapse），验证 CIVO 在 manipulation 环境是否成立\", \"metrics\": {\"baseline_eval_final\": 58.56, \"baseline_ratio\": 0.455, \"eval_return_final\": 26.64, \"eval_return_peak\": 26.9, \"eval_return_peak_step\": 132500, \"gate_dt_2_frac\": 1, \"gate_entropy\": 0, \"nve_final\": 0.065, \"nve_peak\": 3.78, \"nve_peak_step\": 52500, \"pattern\": \"transient_civo_then_value_collapse\", \"total_steps\": 200000, \"value_baseline_final\": 144.57, \"value_mean_final\": 4.26}, \"notes\": \"Cross-env CIVO confirmation + detector TN. Raw V/E peak=5.66 @52.5K (NVE=3.78× vs baseline). Transient CIVO: onset ~22.5K → peak 52.5K → deflation → eval partial recovery. Detector correctly doesn't trigger (oscillating V/E, max streak=2 < threshold=3). Eval final 26.64 vs baseline 58.56 = 45.5%. Value permanently collapsed (4.26 vs baseline 144.57). PickCube pattern: acute crisis + permanent damage, vs Walker sustained escalation.\", \"parent\": \"exp_019a_v2_pickcube_baseline\", \"status\": \"DONE\", \"updated_at\": \"2026-05-17T15:20:38.182Z\"}, \"exp_022b_no_curriculum\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-17T10:49:08.181Z\", \"hypothesis\": \"Frozen dt_emb (random init, no gradients) + learned gate WITHOUT curriculum (phase1=0, phase2=0, gate fully unlocked from step 0). Tests whether frozen dt_emb prevents CIVO (NVE < 1.5×) while allowing the gate to learn meaningful temporal abstraction (gate_dt_1_frac < 1.0). exp_022 was inconclusive because curriculum locked gate for the entire run; this rerun removes that confound.\", \"metrics\": {\"civo_alert_max\": 0, \"eval_return_105K\": 300.7, \"gate_dt_1_frac_105K\": 0.145, \"gate_dt_mean_105K\": 3.41, \"gate_entropy_ratio_105K\": 0.912, \"gate_near_uniform\": true, \"nve_peak\": 1.22, \"ve_ratio_105K\": 0.075, \"ve_ratio_peak\": 0.218}, \"notes\": \"Frozen dt_emb (random init, no gradients) successfully prevents CIVO: ve_ratio peaked 0.218 (NVE≈1.22×), civo_alert=0 throughout. Confirms C2 (trained dt_emb is necessary for CIVO). Gate converges to near-uniform distribution (entropy_ratio=0.912, no temporal coherence), eval_return=300.7 (32.8% of baseline@105K=915.7). Frozen random dt_emb is sufficient CIVO fix but insufficient for meaningful temporal abstraction — multi-rate imagination's inherent performance limitation.\", \"parent\": \"exp_022_untrained_dt_emb_learned_gate\", \"status\": \"DONE\", \"updated_at\": \"2026-05-17T14:20:12.115Z\"}, \"exp_022_untrained_dt_emb_learned_gate\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-17T04:16:57.150Z\", \"hypothesis\": \"Frozen dt_emb (random init, no gradients) prevents CIVO by blocking the trained-embedding-driven value overestimation feedback loop, while the learned gate (Gumbel-softmax, receives gradients) retains adaptive horizon selection capability. If successful, this decouples temporal abstraction benefits from CIVO vulnerability.\", \"metrics\": {\"civo_alert\": 0, \"civo_ve_ratio_105K\": 0.4, \"eval_return_105K\": 189.1, \"eval_return_65K\": 493.1, \"eval_return_75K\": 573.8, \"final_eval_return\": 189.1, \"gate_collapsed\": true, \"gate_dt_1_frac\": 1, \"gate_entropy\": 0, \"peak_eval_return\": 573.8, \"train_return_112K\": 91.8}, \"notes\": \"INCONCLUSIVE: Gate never activated due to curriculum misconfiguration. phase1=50000 × action_repeat=2 = 100K logger steps, experiment only 105K total. gate_scale reached only 0.006, gate locked at dt=1 entire run. eval_return: 75K=573.8 → 105K=189.1 (collapsed without gate involvement). Rerun as exp_022b with curriculum disabled.\", \"parent\": \"exp_008f_s3_no_dt_embed_walker + exp_005_gate_arch (combines safe dt_emb from 008f with gate architecture from 005 series)\", \"status\": \"DONE\", \"updated_at\": \"2026-05-17T10:56:34.274Z\"}, \"exp_019a_v2_pickcube_baseline\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-16T20:12:22.372Z\", \"hypothesis\": \"Vanilla DreamerV3 on ManiSkill3 PickCube establishes a cross-environment baseline; if stable, subsequent CIVO trigger experiment (019b) can test whether CIVO generalizes beyond DMC Walker Walk.\", \"metrics\": {\"eval_return_final\": 69.43, \"eval_return_peak\": 69.7, \"eval_return_peak_step\": 162500, \"steps_completed\": 200248, \"value_mean_final\": 143.4, \"ve_ratio_final\": 2.07, \"ve_ratio_range\": \"1.05-3.56\"}, \"notes\": \"2026-05-16 22:54: Resubmitted with CVD fix (unset CUDA_VISIBLE_DEVICES inside bash -c). PID 629444. ManiSkill3/SAPIEN requires physical device access — CVD breaks resolve_physical_device(). Using MUJOCO_EGL_DEVICE_ID=1 + --device cuda:1 directly.\", \"parent\": \"exp_001_baseline\", \"status\": \"DONE\", \"updated_at\": \"2026-05-17T07:44:41.396Z\"}, \"exp_007_fixed_dt4\": {\"conclusion\": \"negative\", \"created_at\": \"2026-05-13T22:15:44.218Z\", \"hypothesis\": \"诊断实验：fixed dt=4 vs dt=2 vs learned gate。硬编码 dt=4，其余超参与 exp_006 完全一致。与 exp_006(dt=2) 对照：如果 dt=4 也不掉 return，说明跳步本身无害，问题在 learned gate 机制；如果 dt=4 掉但 dt=2 不掉，说明存在跳步边界。\", \"metrics\": {\"baseline_45K\": 443, \"eval_return_15K\": 129.6, \"eval_return_25K\": 176.9, \"eval_return_35K\": 126.7, \"eval_return_45K\": 144.41, \"eval_return_55K\": 152.49, \"eval_return_5K\": 31, \"model_loss_15K\": 6.337, \"model_loss_25K\": 5.089, \"model_loss_35K\": 4.755, \"model_loss_5K\": 17.927, \"peak_return\": 176.9, \"peak_step\": \"25K\", \"step\": 48000, \"trend\": \"peak 176.9@25K, low plateau ~127-152; value extremely suppressed (v/e 6-13%), NOT delusional critic but severe learning failure\", \"value_eval_ratio_45K\": 0.126, \"value_eval_ratio_55K\": 0.061, \"value_mean_45K\": 18.26, \"value_mean_55K\": 9.28, \"vs_baseline_45K\": \"-67.4%\"}, \"notes\": \"失败原因诊断中 | tmux 日志仅有初始化 warnings，无 Traceback | metrics.jsonl 仅到 step 5000（eval_return=31, model_grad_norm=206.46）| 进程运行 ~12.5 min 后异常退出 | 诊断 Worker: worker_diagnose_exp_007_fixed_dt4_20260513T223405\", \"parent\": \"exp_006_fixed_dt2\", \"status\": \"DONE\", \"updated_at\": \"2026-05-17T04:06:36.869Z\"}, \"exp_008c_no_subsample_dt2_h8\": {\"conclusion\": \"negative\", \"created_at\": \"2026-05-14T01:33:31.413Z\", \"hypothesis\": \"隔离 compounding error 效应：subsample OFF + imagination dt=2 + H=8（物理覆盖 16 步 ≈ baseline H=15）。与 008a(H=15) 对照：008a 崩但 008c 不崩 → compounding error 是根因，H 需与 dt 反比补偿；两个都崩 → dt=2 RSSM 预测质量本身不足。\", \"metrics\": {\"actor_loss_55K\": -0.082, \"actor_loss_65K\": -0.053, \"baseline_65K\": 616, \"data_source_35K\": \"from training logs metrics.jsonl\", \"eval_return_35K\": 185.1, \"eval_return_45K\": 226.55, \"eval_return_55K\": 241.87, \"eval_return_65K\": 240.86, \"step\": 68000, \"trend\": \"flat plateau @55K-65K (~241), very slow learner with h8, value/eval=32.8% (no collapse)\", \"value_eval_ratio_35K\": 0.218, \"value_eval_ratio_55K\": 0.291, \"value_eval_ratio_65K\": 0.328, \"value_mean_35K\": 40.43, \"value_mean_55K\": 70.32, \"value_mean_65K\": 78.96, \"verdict_65K\": \"PLATEAU\", \"vs_baseline_65K\": \"-60.9%\"}, \"parent\": \"exp_006_fixed_dt2\", \"status\": \"DONE\", \"updated_at\": \"2026-05-17T04:06:36.359Z\"}, \"exp_003_event_gated_v2\": {\"conclusion\": \"negative\", \"created_at\": \"2026-05-13T04:52:22.660Z\", \"metrics\": {\"eval_return_105K\": 92.3, \"eval_return_115K\": 118.7, \"fps\": 6.52, \"gate_dt_1_frac_116K\": 0.218, \"gate_dt_mean_116K\": 2.67, \"gate_dt_std_116K\": 1.46, \"gate_empirical_entropy_116K\": 1.655, \"gate_entropy_ratio_116K\": 0.796, \"gate_scale_116K\": 0.61, \"mvp_C1_return\": \"FAIL (0.13)\", \"mvp_C2_entropy\": \"PASS (1.655)\", \"mvp_C3_heff\": \"PASS (2.667x)\", \"mvp_C4_structure\": \"PASS (autocorr=0.652)\", \"return_ratio_105K\": 0.1, \"return_ratio_115K\": 0.13, \"step\": 120000}, \"parent\": \"exp_001_baseline\", \"status\": \"DONE\", \"updated_at\": \"2026-05-17T04:06:35.459Z\"}, \"exp_004_event_gated_v3\": {\"conclusion\": \"negative\", \"created_at\": \"2026-05-13T10:05:16.227Z\", \"hypothesis\": \"修复 imagination dt 约束后（logits masking + clamp safety net），event gate 在 train/imagine 分布同步条件下能产生有意义的 variable-rate stepping 且 return ≥ 80% baseline\", \"parent\": \"exp_003_event_gated_v2\", \"status\": \"DONE\", \"updated_at\": \"2026-05-17T04:06:34.482Z\"}, \"exp_005_event_gated_v4\": {\"conclusion\": \"negative\", \"created_at\": \"2026-05-13T16:08:06.061Z\", \"hypothesis\": \"Event-gated adaptive horizon (learned gate activation for dt selection) improves sample efficiency over fixed-horizon DreamerV3 by dynamically extending imagination when beneficial.\", \"metrics\": {\"baseline_at_145K\": \"~950\", \"eval_return_105K\": 276.08, \"eval_return_145K\": 98.84, \"eval_return_15K\": 153.9, \"eval_return_35K\": 290.8, \"eval_return_55K\": 541.18, \"eval_return_5K\": 31, \"eval_return_65K\": 465.67, \"eval_return_85K\": 212.34, \"final_return\": 98.84, \"fps\": 6.69, \"gate_dt_mean_105K\": 2.054, \"gate_dt_std_105K\": 0.907, \"gate_entropy_105K\": 1.255, \"gate_scale_105K\": 0.5, \"note\": \"85K/105K metrics corrected from 319.3/337.8 to 212.34/276.08\", \"peak_return\": 541.18, \"peak_step\": \"55K\", \"return_ratio_final\": 0.104, \"step\": 145000}, \"parent\": \"exp_004_event_gated_v3\", \"status\": \"DONE\", \"updated_at\": \"2026-05-17T04:06:33.514Z\"}, \"exp_008d_civo_trigger_s3\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-17T00:25:47.784Z\", \"hypothesis\": \"Trained dt-emb with subsample (gate_fixed_dt=2, gate_subsample_max_dt=2) induces CIVO (NVE≥1.5×) on seed=3, confirming CIVO onset is systematic across seeds regardless of replay sampling sequence (seed bug fix verification).\", \"metrics\": {\"baseline_eval_105K\": 915.67, \"collapse_onset_step\": 95000, \"collapse_type\": \"late-onset\", \"eval_return_final\": 267.6, \"eval_return_final_step\": 105000, \"eval_return_peak\": 451.7, \"eval_return_peak_step\": 95000, \"nve_final\": 1.53, \"nve_onset_step\": 45000, \"nve_onset_value\": 1.5, \"nve_peak\": 1.53, \"nve_peak_step\": 105000, \"nve_sustained_45K_55K\": true, \"total_steps\": 112000, \"train_return_final_avg\": 138, \"train_return_final_range\": \"82-214\", \"value_mean_final\": 268.4, \"vs_baseline_105K\": \"-70.8%\"}, \"parent\": \"exp_008d_subsample_on_h8\", \"status\": \"DONE\", \"updated_at\": \"2026-05-17T03:24:26.004Z\"}, \"exp_018v2_full_sgs_walker_s1\": {\"conclusion\": \"negative\", \"created_at\": \"2026-05-16T13:42:15.786Z\", \"hypothesis\": \"Full Selective Gradient Stopping (blocking obs+reward+cont decoder gradients to dt_emb) eliminates all gradient pathways creating dt-specific representations, thereby preventing CIVO onset and collapse.\", \"metrics\": {\"civo_reduction_pct\": 79, \"eval_return_final\": 448.3, \"eval_return_final_step\": 105000, \"eval_return_peak\": 499.6, \"eval_return_peak_step\": 75000, \"gate_dt_2_frac\": 1, \"gate_dt_mean\": 2, \"late_collapse_detected\": true, \"late_collapse_step\": 112000, \"nve_final\": 1.34, \"nve_mean_45k_105k\": 1.23, \"nve_peak\": 1.66, \"nve_peak_step\": 95000, \"total_steps\": 112000, \"total_updates\": 25099, \"value_loss_final\": 0.6}, \"parent\": \"exp_008d_subsample_on_h8\", \"status\": \"DONE\", \"updated_at\": \"2026-05-17T02:57:18.423Z\"}, \"exp_018_full_sgs_s2\": {\"conclusion\": \"negative\", \"created_at\": \"2026-05-16T19:33:26.266Z\", \"hypothesis\": \"Full-SGS reliably prevents CIVO across seeds; if seed=2 also survives without collapse, SGS is a robust intervention mechanism for deployment.\", \"notes\": \"CIVO collapse confirmed: eval 40.8@105K (from peak ~488@75K). NVE peaked 1.66× at 95K (35K+ window). Full-SGS did NOT prevent collapse in seed 2 — contradicts 018v2 (seed 1) which avoided collapse. This invalidates SGS_full as a reliable CIVO prevention method. Key difference from 018v2: 018_s2 collapsed while 018v2 sustained. n=2 for SGS_full now shows collapse_rate=0.5.\", \"parent\": \"exp_018v2_full_sgs_walker_s1\", \"status\": \"DONE\", \"updated_at\": \"2026-05-17T02:56:37.385Z\"}, \"exp_008f_no_dt_embed_subsample_on_h8\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-14T04:51:27.592Z\", \"hypothesis\": \"Without trained dt-embedding, subsample mechanism alone does not induce value overestimation, isolating dt-embedding as the necessary causal factor for CIVO.\", \"metrics\": {\"baseline_105K\": 915.67, \"causal_conclusion\": \"trained dt_embedding → value overestimation → actor exploitation → collapse. Without dt_embedding, value self-corrects.\", \"current_step\": 105000, \"eval_checkpoints\": {\"105K\": {\"eval_return\": 503, \"normalized_ve\": 0.3, \"value_mean\": 98.2}, \"15K\": {\"eval_return\": 182.03, \"value_mean\": 2.989, \"ve_ratio\": 0.01642}, \"25K\": {\"baseline_ve\": 0.087, \"eval_return\": 196.78, \"normalized_ve\": 1.02, \"value_mean\": 17.507, \"ve_ratio\": 0.089}, \"35K\": {\"baseline_ve\": 0.241, \"eval_return\": 206.67, \"normalized_ve\": 0.73, \"value_mean\": 36.279, \"ve_ratio\": 0.176}, \"45K\": {\"baseline_ve\": 0.331, \"eval_return\": 194.08, \"normalized_ve\": 0.83, \"value_mean\": 53.429, \"ve_ratio\": 0.275}, \"55K\": {\"baseline_ve\": 0.404, \"eval_return\": 173.45, \"normalized_ve\": 0.97, \"value_mean\": 67.899, \"ve_ratio\": 0.391}, \"5K\": {\"eval_return\": 30.49, \"value_mean\": 0.001, \"ve_ratio\": 4e-05}, \"65K\": {\"eval_return\": 375, \"normalized_ve\": 0.37}, \"75K\": {\"eval_return\": 324, \"normalized_ve\": 0.42}, \"85K\": {\"eval_return\": 246, \"normalized_ve\": 0.65, \"value_mean\": 111.8}, \"95K\": {\"eval_return\": 319, \"normalized_ve\": 0.54}}, \"last_updated\": \"2026-05-14T09:50:00\", \"target_steps\": 105000, \"trend\": \"Zigzag recovery with high variance: eval 207→194→173@55K→375→324→246→319→503@105K. NOT a clean V-shape — high inter-eval variance throughout. Value self-corrected: peaked 111.8@85K then declined to 98.2@105K. Normalized v/e: 0.97x@55K→0.37x@65K→0.65x@85K→0.30x@105K. Key contrast with 008d: value only accelerates (69.3%@45K) vs 008f value self-corrects.\", \"verdict\": \"SUCCESS - zigzag recovery to 503@105K, normalized v/e=0.30x, C2 confirmed\", \"vs_baseline_105K\": \"-45.1%\"}, \"parent\": \"exp_008d_subsample_on_h8\", \"status\": \"DONE\", \"updated_at\": \"2026-05-17T02:56:33.517Z\"}, \"exp_016d_sgs_walker_s1\": {\"conclusion\": \"failed\", \"created_at\": \"2026-05-15T19:29:41.130Z\", \"hypothesis\": \"Selective Gradient Stopping (reward_dt_emb_detach) blocks reward-gradient pathway to dt_emb, preventing CIVO-inducing co-adaptation while preserving task performance.\", \"parent\": \"exp_008d_subsample_on_h8\", \"status\": \"DONE\", \"updated_at\": \"2026-05-17T02:54:28.152Z\"}, \"exp_001_baseline\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-13T02:09:53.875Z\", \"hypothesis\": \"Vanilla DreamerV3 on Walker Walk converges to stable high-return policy (>900) within 500K steps, establishing the performance ceiling for all gated variants.\", \"metrics\": {\"data_source_ve\": \"from training logs metrics.jsonl\", \"eval_return_last10_mean\": 950.9, \"eval_return_peak\": 970.41, \"eval_return_peak_step\": 505000, \"eval_trajectory\": {\"105K\": 915.67, \"115K\": 919.81, \"125K\": 921.37, \"135K\": 900, \"145K\": 932.16, \"155K\": 933.34, \"15K\": 206.61, \"165K\": 907.98, \"175K\": 918.87, \"185K\": 954.69, \"195K\": 936.09, \"205K\": 949.24, \"215K\": 913.4, \"225K\": 962.44, \"235K\": 937.24, \"245K\": 934.42, \"255K\": 948.45, \"25K\": 395.27, \"265K\": 925.09, \"275K\": 931.51, \"285K\": 925.75, \"295K\": 936.3, \"305K\": 939.33, \"315K\": 948.42, \"325K\": 967.75, \"335K\": 942.41, \"345K\": 969.83, \"355K\": 941.11, \"35K\": 388.47, \"365K\": 935.76, \"375K\": 918.24, \"385K\": 937.98, \"395K\": 955.38, \"405K\": 937.83, \"415K\": 948.99, \"425K\": 954.64, \"435K\": 964.96, \"445K\": 953.37, \"455K\": 945.84, \"45K\": 513.77, \"465K\": 947.81, \"475K\": 947.66, \"485K\": 930.6, \"495K\": 944.73, \"505K\": 970.41, \"55K\": 625.73, \"5K\": 31.77, \"65K\": 615.86, \"75K\": 596.28, \"85K\": 713.93, \"95K\": 871.06}, \"final\": true, \"step\": 512000, \"value_eval_ratio_105K\": 0.656, \"value_eval_ratio_25K\": 0.087, \"value_eval_ratio_35K\": 0.241, \"value_eval_ratio_45K\": 0.331, \"value_eval_ratio_55K\": 0.404, \"value_eval_ratio_65K\": 0.563, \"value_eval_ratio_75K\": 0.719, \"value_eval_ratio_85K\": 0.701, \"value_eval_ratio_95K\": 0.632, \"value_eval_ratio_stable\": \"~69-72% from 135K+\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T02:54:24.099Z\"}, \"exp_008d_civo_trigger_s2\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-16T19:32:16.790Z\", \"hypothesis\": \"Walker Walk trained dt_emb + subsample ON + dt=2 + H=8, seed 1 — CIVO trigger 第 3 个独立 seed (D1)。预期 NVE>1.5× 触发 CIVO。用于 bootstrap CI 闭合 trained_dt_emb condition (现有: seed 0 = 008d, seed 2 = 009b)。注意: 原名 s2 但实际需跑 seed=1 (避免与 009b seed=2 重复)。\", \"notes\": \"Killed by Director order: seed bug confirmed. --seed 1 was parsed incorrectly, producing bit-for-bit identical results to seed=0. PID 628482 killed. Will resubmit after seed bug fix with seed=3.\", \"parent\": \"exp_008d_subsample_on_h8\", \"status\": \"DONE\", \"updated_at\": \"2026-05-17T00:24:10.180Z\"}, \"exp_008f_s3_no_dt_embed_walker\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-16T16:04:28.878Z\", \"hypothesis\": \"Walker Walk dt_embed_dim=0 + subsample ON + H=8 seed 3 — 008f 系列第 3 个独立 seed，闭合 no_dt_emb condition 的 bootstrap CI（当前 n=2，需 ≥3）。预期 NVE<1.5×，无 CIVO。\", \"metrics\": {\"collapse\": false, \"eval_return_final\": 363.8, \"nve_peak\": \"< 1.5x\"}, \"parent\": \"exp_008f_no_dt_embed_subsample_on_h8\", \"status\": \"DONE\", \"updated_at\": \"2026-05-16T20:09:51.135Z\"}, \"exp_020_vanilla_dreamerv3_s2\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-16T13:23:55.837Z\", \"hypothesis\": \"Vanilla DreamerV3 (no dt_emb, no subsample, no gate) seed 2 — Pathway B 控制实验：验证 008e_v3_s2 的 eval-driven collapse 是否需要 trained dt_emb 作为必要条件。如果 vanilla s2 稳定 → C6 成立 (trained dt_emb 是 Pathway B 必要条件)。如果也崩溃 → Pathway B 是 DreamerV3 inherent fragility。\", \"metrics\": {\"collapse\": false, \"comparison_with_parent\": {\"c6_confirmed\": true, \"delta\": \"vanilla stable (836.5) vs trained dt_emb collapsed (136.96)\", \"parent_collapsed\": true, \"parent_eval_105K\": 136.96, \"parent_id\": \"exp_008e_v3_walker_s2\", \"parent_nve_105K\": 3.78}, \"eval_trajectory\": [{\"eval_return\": 41.2, \"step\": 5000}, {\"eval_return\": 534.1, \"step\": 55000}, {\"eval_return\": 688.9, \"step\": 65000}, {\"eval_return\": 596.2, \"step\": 95000}, {\"eval_return\": 836.5, \"step\": 105000}], \"final_eval_return\": 836.5, \"final_value_mean\": 539.3, \"peak_eval_return\": 836.5, \"peak_eval_step\": 105000, \"train_return_range_108K\": \"511-808\", \"ve_ratio_105K\": 0.645}, \"notes\": \"Pathway B 控制实验 (D6)。vanilla config: dt_embed_dim=0, subsample OFF, H=15, seed=2, 105K steps, Walker Walk。排队等 010b 完成后在 cuda:0 提交。命令: dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 105000 --seed 2 --compile True --device cuda:0 --imag_horizon 15\", \"parent\": \"exp_008e_v3_walker_s2\", \"status\": \"DONE\", \"updated_at\": \"2026-05-16T19:43:57.604Z\"}, \"exp_019a_pickcube_baseline\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-16T03:23:50.639Z\", \"hypothesis\": \"PickCube-v1 baseline — dt=1, no dt_emb (dim=0), subsample OFF. ManiSkill3 manipulation 环境稳定基线，验证 CIVO 诊断在 manipulation 中的适用性\", \"notes\": \"ManiSkill3 Phase 1. 排队等 cuda:1 (010a 完成后). --compile False --device cuda:1. maniskill_state config.\", \"status\": \"DONE\", \"updated_at\": \"2026-05-16T13:43:00.745Z\"}, \"exp_018_full_sgs_walker_s1\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-15T23:30:39.991Z\", \"hypothesis\": \"Full-SGS: detach all non-KL gradients from dt_emb (removes 93% obs decoder contribution). If CIVO persists → vulnerability is representation-level; if eliminated → obs decoder gradient is root cause.\", \"metrics\": {\"eval_return_final\": 915.7, \"eval_return_final_step\": 105000, \"eval_return_peak\": 915.7, \"eval_return_peak_step\": 105000, \"nve_peak\": 0.72, \"nve_peak_step\": 75000, \"nve_sustained_avg\": 0.55, \"nve_sustained_max\": 0.72, \"total_steps\": 112000, \"train_return_final_avg\": 899.4, \"value_mean_final\": 601.1}, \"notes\": \"⚠️ INVALID: 训练命令缺失 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8。gate_enabled=false → dt_embedding 未创建 → full_sgs 是空操作 → 实际等同 vanilla baseline。所有基于此实验的 claim (CIVO elimination, gradient-level vulnerability) 需要 018v2 重新验证。\", \"parent\": \"exp_016e_sgs_walker_s1\", \"status\": \"DONE\", \"updated_at\": \"2026-05-16T13:42:11.339Z\"}, \"exp_010a_cheetah_baseline_s1\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-14T07:17:27.101Z\", \"hypothesis\": \"Cheetah Run baseline seed 1 — 建立第二环境 dt=1 参考基线，为跨环境验证 C1/C2 做准备（plan_020）\", \"metrics\": {\"eval_return_final\": 849.8, \"eval_return_final_step\": 515000, \"eval_return_peak\": 849.8, \"eval_return_peak_step\": 515000, \"final_step\": 524000, \"total_eval_episodes\": 52, \"train_return_last\": 716}, \"notes\": \"Director 排期: cuda:0 上排在 009d 之后。\", \"status\": \"DONE\", \"updated_at\": \"2026-05-16T12:01:11.169Z\"}, \"exp_009d_baseline_walker_s0\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-15T11:55:00.039Z\", \"hypothesis\": \"Walker Walk baseline seed 0 — 第三独立 baseline seed，建立 v/e 校准参考（plan_010）\", \"metrics\": {\"eval_return\": 927.6, \"eval_return_at_508K\": 927.6, \"eval_return_peak\": 950.96, \"eval_return_peak_step\": 398000, \"note\": \"COMPLETED 508K/500K, final eval 927.6, peak 950.96@398K\", \"step\": 508000}, \"notes\": \"已清理重复进程并干净重启。修复: LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 + MUJOCO_GL=egl + CUDA_VISIBLE_DEVICES 隔离。cuda:0, seed=0, 500K steps ~19h。logdir: /root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009d_baseline_walker_s0\", \"parent\": \"exp_001_baseline\", \"status\": \"DONE\", \"updated_at\": \"2026-05-16T09:50:34.506Z\"}, \"exp_017_subsample_off_trained_dt_emb\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-15T10:44:24.756Z\", \"hypothesis\": \"Walker Walk trained dt_emb + subsample OFF + dt=2 imagination + H=15 seed 1 — 2×2 消融矩阵: 隔离 subsample 训练数据的因果效应。与 008a (untrained dt_emb, subsample OFF) 唯一差异是 dt_emb trained vs untrained。如果 017 崩而 008a 不崩 → 确认 trained dt_emb 是 CIVO 根因，即使训练数据全为 dt=1（plan_017, C2）\", \"notes\": \"D044: 取消。008a 配置验证确认 017 与 008a 完全重复（trained dt_emb + subsample OFF + H=15 + seed 1）。008a 的\\\"untrained\\\"含义是\\\"dt_emb 存在但未接触 dt>1 数据\\\"，不是 frozen/absent。2×2 矩阵已由 008a/008d/008f/015b 闭合。\", \"parent\": \"exp_008a_no_subsample_dt2\", \"status\": \"DONE\", \"updated_at\": \"2026-05-16T04:46:30.361Z\"}, \"016e\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-15T22:21:09.251Z\", \"notes\": \"重复条目，权威数据在 exp_016e_sgs_walker_s1 (DONE/negative)。此条目为 NVE 诊断过程中误创建的冗余记录。\", \"status\": \"DONE\", \"updated_at\": \"2026-05-16T01:39:17.916Z\"}, \"exp_016e_sgs_walker_s1\": {\"conclusion\": \"negative\", \"created_at\": \"2026-05-15T19:35:20.242Z\", \"hypothesis\": \"Walker Walk SGS (Stop-Gradient on dt_emb in reward head) + subsample ON + H=8 seed 1 — 核心方法实验：reward_dt_emb_detach 阻断 CIVO reward→dt_emb 梯度通路（plan_016）。第五次重试，修复 Logger.video() → no-op 彻底消除 SummaryWriter.add_video/flush 死锁\", \"metrics\": {\"actor_loss_sign_flip_step\": 95000, \"civo_catastrophic_step\": 95000, \"civo_detected\": true, \"civo_nve_peak\": 10.42, \"civo_nve_peak_step\": 95000, \"civo_onset_step\": 85000, \"civo_severity\": \"catastrophic\", \"current_step\": 100000, \"data_source\": \"metrics.jsonl from logdir/exp_016e_sgs_walker_s1/, completed 100K steps, SSH 2026-05-16T06:25\", \"deep_analysis\": {\"016e_vs_008d_entropy_comparison\": {\"15K\": {\"008d\": 0.481, \"016e\": 1.049, \"delta\": 0.568}, \"25K\": {\"008d\": -1.862, \"016e\": -1.554, \"delta\": 0.308}, \"35K\": {\"008d\": -3.465, \"016e\": -2.118, \"delta\": 1.347}, \"45K\": {\"008d\": -4.575, \"016e\": -3.455, \"delta\": 1.12}, \"55K\": {\"008d\": -4.879, \"016e\": -3.617, \"delta\": 1.262}, \"interpretation\": \"SGS preserves ~1.0-1.3 nats higher entropy through 35-55K, enabling better exploration\"}, \"016e_vs_008d_value_at_crash\": {\"008d\": {\"disconnect_ratio\": 1.67, \"eval_return\": 82.75, \"value_mean\": 137.88}, \"016e\": {\"disconnect_ratio\": 6.58, \"eval_return\": 31.73, \"value_mean\": 208.88}, \"interpretation\": \"016e value completely decoupled from reality; 008d still weakly correlated\"}, \"actor_loss_sign_flip\": {\"008d_min_actor_loss\": -0.073, \"008d_never_flipped\": true, \"016e_flip_step\": 95000, \"016e_flip_value\": 0.014, \"interpretation\": \"sign flip = value critic drives actor toward worse actions, triggering catastrophic collapse\"}, \"train_return_collapse_timeline\": {\"100K\": [109, 111, 102, 108], \"88K\": [140, 145, 116, 116], \"92K\": [50, 29, 34, 75], \"96K\": [86, 41, 50, 101], \"interpretation\": \"collapse visible in train_return by 92K; partial recovery by 100K but far below peak\"}}, \"eval_checkpoints\": [{\"eval_return\": 31, \"step\": 5000, \"value_mean\": 0.001, \"ve_ratio\": 4e-05}, {\"eval_return\": 140.3, \"step\": 15000, \"value_mean\": 3.1, \"ve_ratio\": 0.022}, {\"baseline_ve\": 0.087, \"eval_return\": 141.75, \"nve\": 1.86, \"step\": 25000, \"value_mean\": 22.97, \"ve_ratio\": 0.162}, {\"baseline_ve\": 0.241, \"eval_return\": 173.01, \"nve\": 1.28, \"step\": 35000, \"value_mean\": 53.55, \"ve_ratio\": 0.309}, {\"baseline_ve\": 0.331, \"eval_return\": 184.03, \"nve\": 1.4, \"step\": 45000, \"value_mean\": 85.32, \"ve_ratio\": 0.464}, {\"baseline_ve\": 0.404, \"eval_return\": 153.79, \"nve\": 1.86, \"step\": 55000, \"value_mean\": 115.63, \"ve_ratio\": 0.752}, {\"baseline_ve\": 0.563, \"eval_return\": 324.3, \"nve\": 0.83, \"step\": 65000, \"value_mean\": 152.3, \"ve_ratio\": 0.469}, {\"baseline_ve\": 0.719, \"eval_return\": 326.67, \"nve\": 0.81, \"step\": 75000, \"value_mean\": 190.04, \"ve_ratio\": 0.582}, {\"baseline_ve\": 0.701, \"eval_return\": 256.21, \"nve\": 1.2, \"step\": 85000, \"value_mean\": 215.39, \"ve_ratio\": 0.841}, {\"baseline_ve\": 0.632, \"eval_return\": 31.73, \"nve\": 10.42, \"step\": 95000, \"value_mean\": 208.88, \"ve_ratio\": 6.583}], \"final_eval_return\": 31.73, \"final_eval_step\": 95000, \"gate_dt_2_frac\": 1, \"gate_dt_mean\": 2, \"peak_eval_return\": 326.67, \"peak_eval_step\": 75000, \"reward_dt_emb_detach\": true, \"sgs_verdict\": \"SGS delays CIVO onset ~50K steps by preserving entropy, yields 2x higher peak (327 vs 167), but does NOT prevent collapse. Collapse is more severe (NVE 10.42x vs 4.12x) due to accumulated value overestimation. Root cause is value dynamics, not reward-head gradient contamination.\", \"target_steps\": 105000}, \"notes\": \"logdir 路径修正：实际数据在 logdir/exp_016e_sgs_walker_s1（非 spec 中的 exp_016d）。SGS 崩溃确认@95K: eval 31.7, ve_ratio=6.59x, NVE=10.42x。\\n\\n**⚠️ 关键发现（Full-SGS 梯度验证）：reward loss 对 dt_emb.weight 的梯度贡献为 0。016e 的 reward_dt_emb_detach 实际上是 no-op——完全无效干预。** 真正的 dt_emb 梯度来源是 decoder heads（orientations=1.11, velocity=0.90, height=0.76, cont=0.27）。016e 与 008d 的差异（onset 延迟、更高峰值）应归因于随机变异或其他实验条件差异，不是 SGS 干预效果。\\n\\nFull-SGS（detach 所有 non-KL head 梯度）移除 93% dt_emb 梯度（1.624→0.119），是真正的测试。\", \"parent\": \"exp_008d_subsample_on_h8\", \"status\": \"DONE\", \"updated_at\": \"2026-05-15T23:30:11.433Z\"}, \"exp_016c_sgs_walker_s1\": {\"conclusion\": \"failed\", \"created_at\": \"2026-05-15T19:12:09.799Z\", \"hypothesis\": \"Walker Walk SGS (reward_dt_emb_detach=True) + subsample ON + H=8 seed 1 — 论文 method section 核心。GPU 1 清理+验证通过后重启（plan_016）\", \"metrics\": {\"egl_fix_verified\": true, \"eval_return_5K\": 31, \"step\": 5000}, \"parent\": \"exp_008d_subsample_on_h8\", \"status\": \"DONE\", \"updated_at\": \"2026-05-15T19:27:24.104Z\"}, \"exp_009h_008f_walker_s0\": {\"conclusion\": \"failed\", \"created_at\": \"2026-05-15T19:03:10.534Z\", \"hypothesis\": \"Walker Walk dt_embed_dim=0 + subsample ON + H=8 seed 0 — 多 seed 复现 008f 因果控制稳定性，巩固 C2 统计显著性（plan_012）。替代 009g（EGL device mismatch 修复：+MUJOCO_EGL_DEVICE_ID=1）\", \"notes\": \"日志显示进程正常完成 prefill → 到达 step 5000 → eval 正在运行（500 iter, 96s, 正常产出 debug 行）→ 被外部 SIGHUP (EXIT_CODE=129) 终止。非渲染死锁，非 OOM。诊断 Worker 排查外部终止原因中。009f/009g/009h 连续 3 次失败，分别因 seed 重复、EGL mismatch、外部 SIGHUP。\", \"parent\": \"exp_008f_no_dt_embed_subsample_on_h8\", \"status\": \"DONE\", \"updated_at\": \"2026-05-15T19:18:24.685Z\"}, \"exp_016b_sgs_walker_s1\": {\"conclusion\": \"failed\", \"created_at\": \"2026-05-15T19:08:00.667Z\", \"hypothesis\": \"Walker Walk SGS (Stop-Gradient on dt_emb in reward head) + subsample ON + trained dt_emb + H=8 seed 1 — 核心方法实验：reward_dt_emb_detach 阻断 CIVO reward→dt_emb 梯度通路（plan_016, 论文 method section 核心）。重跑 016_sgs，修复 EGL device mismatch（+MUJOCO_EGL_DEVICE_ID=1）\", \"notes\": \"Restarted after GPU 1 cleanup. Old PID 523536 killed during GPU reset attempt. New PID 524244. GPU 1 diagnostics: no ECC/Xid errors, reset not supported (AutoDL container) but cleanup successful. CUDA + dm_control verification passed in 3s.\", \"parent\": \"exp_008d_subsample_on_h8\", \"status\": \"DONE\", \"updated_at\": \"2026-05-15T19:11:46.897Z\"}, \"exp_009g_008f_walker_s0\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-15T18:54:23.385Z\", \"hypothesis\": \"Walker Walk dt_embed_dim=0 + subsample ON + H=8 seed 0 — 多 seed 复现 008f 因果控制稳定性，巩固 C2 统计显著性（plan_012）。替代 009f（seed=1 与 parent 008f 重复）\", \"notes\": \"Hung at first eval (step 5000) due to osmesa rendering deadlock in dm_control render_executor thread. Same root cause as exp_016. Fixed by switching MUJOCO_GL to egl in dreamer.py.\", \"parent\": \"exp_008f_no_dt_embed_subsample_on_h8\", \"status\": \"DONE\", \"updated_at\": \"2026-05-15T19:03:53.591Z\"}, \"exp_009f_008f_walker_s1\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-14T11:09:15.806Z\", \"hypothesis\": \"Walker Walk dt_embed_dim=0 + subsample ON + H=8 seed 1 — 多 seed 复现 008f 因果控制稳定性，巩固 C2 统计显著性（plan_012）\", \"parent\": \"exp_008f_no_dt_embed_subsample_on_h8\", \"status\": \"DONE\", \"updated_at\": \"2026-05-15T18:54:04.806Z\"}, \"exp_016_sgs_walker_s1\": {\"conclusion\": \"failed\", \"created_at\": \"2026-05-15T14:30:32.999Z\", \"hypothesis\": \"Walker Walk SGS (Stop-Gradient on dt_emb in reward head) + subsample ON + trained dt_emb + H=8 seed 1 — 核心方法实验：reward_dt_emb_detach 阻断 CIVO reward→dt_emb 梯度通路。预期：不崩溃，nve < 1.5x baseline；imagination dt=2/dt=1 reward ratio 从 008d 的 2.90x 大幅下降（plan_016, 论文 method section 核心）\", \"notes\": \"Director 调整优先级：017 先于 016。cuda:1 释放后先跑 017，017 完成后再跑 016。SGS 诊断 bug 已修复（models.py L388-417 删除），dry-run 通过。[2026-05-15 18:43] PID 514422 hung: GPU 1 利用率 0%, 显存 794 MiB, metrics.jsonl 停 step=5000 持续 2.5h+。已 kill，Worker 诊断根因+修复+重启中。\", \"parent\": \"exp_008d_subsample_on_h8\", \"status\": \"DONE\", \"updated_at\": \"2026-05-15T18:43:52.455Z\"}, \"exp_015b_frozen_dt_emb\": {\"conclusion\": \"negative\", \"created_at\": \"2026-05-15T10:21:05.572Z\", \"hypothesis\": \"Walker Walk frozen dt_emb + subsample ON + dt=2 imagination + H=8 seed 1 — 2×2 消融矩阵: 隔离 dt_emb 训练 vs 存在的因果效应。如果 freeze 后不崩 → 确认 CIVO 根因是 dt_emb 训练而非结构存在（plan_015B, D041）\", \"metrics\": {\"actor_entropy_105K\": -4.855, \"actor_loss_105K\": 0.000179, \"collapse_mechanism\": \"gradient_starvation_from_frozen_dt_emb\", \"data_source\": \"worker SSH final analysis 2026-05-15T18:30\", \"eval_return_105K\": 204.2, \"eval_return_15K\": 167.9, \"eval_return_25K\": 171.8, \"eval_return_35K\": 201.6, \"eval_return_45K\": 122.3, \"eval_return_55K\": 105.8, \"eval_return_5K\": 31, \"eval_return_65K\": 160.3, \"eval_return_75K\": 80, \"eval_return_85K\": 183.5, \"eval_return_95K\": 238.4, \"final_eval\": 204.2, \"final_step\": 112000, \"gate_dt_1_frac\": 0, \"gate_dt_mean\": 2, \"nve_105K\": 0.42, \"nve_85K\": 0.467, \"nve_95K\": 0.394, \"summary\": \"NVE 0.39-0.47 (far below 1.0, critic under-estimates), actor_loss→0 (gradient starvation), gate locked dt=2 100%, eval volatile 80-238 no stable convergence\", \"value_mean_105K\": 56.212, \"value_std_105K\": 13.818}, \"notes\": \"已清理重复进程并干净重启。修复: LD_PRELOAD + MUJOCO_GL=egl + --device cuda:0 (CUDA_VISIBLE_DEVICES=1 隔离)。cuda:1, seed=1, 105K steps ~5h。logdir: /root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_015b_frozen_dt_emb\", \"parent\": \"exp_008d_subsample_on_h8\", \"status\": \"DONE\", \"updated_at\": \"2026-05-15T18:38:42.380Z\"}, \"exp_008a_no_subsample_dt2\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-14T01:33:27.311Z\", \"hypothesis\": \"隔离 subsample 效应：trained dt_emb (unexposed to dt>1 data due to subsample OFF) + subsample OFF（纯 dt=1 训练）+ imagination dt=2 + H=15（物理覆盖 30 步）。如果不崩 → subsample 混合训练数据是崩塌根因；如果崩 → 问题在 dt=2 imagination 本身。\", \"metrics\": {\"baseline_105K\": 915.67, \"baseline_55K\": 625.7, \"baseline_65K\": 616, \"data_source\": \"from training logs metrics.jsonl\", \"eval_return_105K\": 777.66, \"eval_return_35K\": 500.84, \"eval_return_45K\": 563.41, \"eval_return_55K\": 487.92, \"eval_return_65K\": 608, \"eval_return_75K\": 469.93, \"eval_return_85K\": 583.73, \"eval_return_95K\": 572.24, \"nan_count\": 0, \"normalized_ve_105K\": 0.59, \"normalized_ve_55K\": 0.93, \"normalized_ve_65K\": 0.66, \"normalized_ve_75K\": 0.75, \"normalized_ve_85K\": 0.68, \"normalized_ve_95K\": 0.79, \"step\": 112000, \"trend\": \"Two V-shaped recoveries: 501→563→488→608→470→584→572→778; v/e suppressed 38-54% (normalized 0.59-0.79x baseline); no collapse at 105K\", \"value_eval_ratio_105K\": 0.386, \"value_eval_ratio_55K\": 0.376, \"value_eval_ratio_65K\": 0.372, \"value_eval_ratio_75K\": 0.536, \"value_eval_ratio_85K\": 0.475, \"value_eval_ratio_95K\": 0.497, \"value_mean_105K\": 300.27, \"value_mean_55K\": 183.5, \"value_mean_65K\": 226.1, \"value_mean_75K\": 251.78, \"value_mean_85K\": 277.36, \"value_mean_95K\": 284.28, \"verdict_105K\": \"NEW_PEAK_V_RECOVERY\", \"verdict_65K\": \"RECOVERED_NEW_HIGH\", \"vs_baseline_105K\": \"-15.1%\", \"vs_baseline_65K\": \"-1.3%\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T14:50:59.046Z\"}, \"exp_009d_baseline_walker_s1\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-14T11:09:14.363Z\", \"hypothesis\": \"Walker Walk baseline seed 1 — 多 seed 复现 exp_001 baseline，建立 v/e 校准参考（plan_010）\", \"notes\": \"⚠️ seed=1 与 exp_001_baseline 相同，eval 轨迹确定性复现。不构成独立 seed。如需第三 baseline seed 应 kill 并用 --seed 0 或 --seed 3 重跑。待 Director 决策。\", \"parent\": \"exp_001_baseline\", \"status\": \"DONE\", \"updated_at\": \"2026-05-15T11:54:55.153Z\"}, \"exp_009a_baseline_walker_s2\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-14T07:17:24.247Z\", \"hypothesis\": \"Walker Walk baseline seed 2 — 多 seed 复现 exp_001 baseline，建立 v/e 校准参考（plan_010）\", \"metrics\": {\"cross_seed_ve_stable\": \"seed 2 v/e = 0.69-0.72 matches seed 0/1 = 0.69-0.72\", \"eval_return_peak\": 966.94, \"eval_return_peak_step\": 395000, \"eval_trajectory\": [{\"eval_return\": 41.21, \"step\": 5000}, {\"eval_return\": 106.01, \"step\": 15000}, {\"eval_return\": 325.33, \"step\": 25000}, {\"eval_return\": 354.49, \"step\": 35000}, {\"eval_return\": 498.01, \"step\": 45000}, {\"eval_return\": 534.13, \"step\": 55000}, {\"eval_return\": 688.87, \"step\": 65000}, {\"eval_return\": 656.85, \"step\": 75000}, {\"eval_return\": 618.73, \"step\": 85000}, {\"eval_return\": 596.24, \"step\": 95000}, {\"eval_return\": 836.51, \"step\": 105000}, {\"eval_return\": 804.79, \"step\": 115000}, {\"eval_return\": 865.48, \"step\": 125000}, {\"eval_return\": 876.08, \"step\": 135000}, {\"eval_return\": 869.18, \"step\": 145000}, {\"eval_return\": 778.99, \"step\": 155000}, {\"eval_return\": 864.03, \"step\": 165000}, {\"eval_return\": 850.53, \"step\": 175000}, {\"eval_return\": 907.31, \"step\": 185000}, {\"eval_return\": 873.49, \"step\": 195000}, {\"eval_return\": 887.02, \"step\": 205000}, {\"eval_return\": 956.04, \"step\": 215000}, {\"eval_return\": 892.09, \"step\": 225000}, {\"eval_return\": 914.78, \"step\": 235000}, {\"eval_return\": 950.32, \"step\": 245000}, {\"eval_return\": 936.9, \"step\": 255000}, {\"eval_return\": 937.27, \"step\": 265000}, {\"eval_return\": 934.78, \"step\": 275000}, {\"eval_return\": 960.2, \"step\": 285000}, {\"eval_return\": 947.46, \"step\": 295000}, {\"eval_return\": 937.8, \"step\": 305000}, {\"eval_return\": 948.66, \"step\": 315000}, {\"eval_return\": 930.61, \"step\": 325000}, {\"eval_return\": 919.23, \"step\": 335000}, {\"eval_return\": 816.18, \"step\": 345000}, {\"eval_return\": 932.45, \"step\": 355000}, {\"eval_return\": 943.13, \"step\": 365000}, {\"eval_return\": 952.86, \"step\": 375000}, {\"eval_return\": 942.31, \"step\": 385000}, {\"eval_return\": 966.94, \"step\": 395000}, {\"eval_return\": 948.01, \"step\": 405000}, {\"eval_return\": 957.06, \"step\": 415000}, {\"eval_return\": 939.37, \"step\": 425000}, {\"eval_return\": 963.65, \"step\": 435000}, {\"eval_return\": 948.42, \"step\": 445000}, {\"eval_return\": 937.72, \"step\": 455000}, {\"eval_return\": 939.54, \"step\": 465000}, {\"eval_return\": 965.94, \"step\": 475000}, {\"eval_return\": 916.74, \"step\": 485000}, {\"eval_return\": 945.58, \"step\": 495000}, {\"eval_return\": 957.87, \"step\": 505000}], \"final_eval_return\": 957.87, \"final_eval_step\": 505000, \"final_value_mean\": 665.17, \"final_ve_ratio\": 0.694, \"last10_mean\": 947.19, \"n_evals\": 51, \"total_steps\": 505000, \"value_trajectory\": [{\"step\": 5000, \"value_mean\": 0}, {\"step\": 25000, \"value_mean\": 45.78}, {\"step\": 55000, \"value_mean\": 253.49}, {\"step\": 105000, \"value_mean\": 539.34}, {\"step\": 155000, \"value_mean\": 633.42}, {\"step\": 205000, \"value_mean\": 658.92}, {\"step\": 255000, \"value_mean\": 663.87}, {\"step\": 305000, \"value_mean\": 663.86}, {\"step\": 355000, \"value_mean\": 663.78}, {\"step\": 405000, \"value_mean\": 663.95}, {\"step\": 455000, \"value_mean\": 664.42}, {\"step\": 505000, \"value_mean\": 665.17}], \"ve_ratio_trajectory\": [{\"step\": 25000, \"ve\": 0.141}, {\"step\": 55000, \"ve\": 0.475}, {\"step\": 105000, \"ve\": 0.645}, {\"step\": 155000, \"ve\": 0.813}, {\"step\": 205000, \"ve\": 0.743}, {\"step\": 255000, \"ve\": 0.709}, {\"step\": 305000, \"ve\": 0.708}, {\"step\": 355000, \"ve\": 0.712}, {\"step\": 405000, \"ve\": 0.7}, {\"step\": 455000, \"ve\": 0.709}, {\"step\": 505000, \"ve\": 0.694}], \"ve_stable_range\": \"0.69-0.72 from 235K+\", \"vs_exp001_105K\": \"836.51 vs 915.67 (-8.6%)\", \"vs_exp001_final\": \"957.87 vs 970.41 (-1.3%)\", \"vs_exp001_last10\": \"947.19 vs 950.90 (-0.4%)\", \"vs_exp001_peak\": \"966.94 vs 970.41 (-0.4%)\"}, \"notes\": \"Baseline seed 2 完成。与 exp_001 (seed 0/1) 高度一致: peak 966.94 vs 970.41 (-0.4%), last10 mean 947.19 vs 950.90 (-0.4%), v/e stable 0.69-0.72 匹配。105K 处 836.51 比 seed 0/1 的 915.67 低 8.6%，但 215K+ 后完全收敛。345K 有一个 dip 到 816 但迅速恢复。baseline 跨 seed 一致性确认。\", \"status\": \"DONE\", \"updated_at\": \"2026-05-15T06:33:16.385Z\"}, \"exp_008e_v3_walker_s2\": {\"conclusion\": \"negative\", \"created_at\": \"2026-05-14T14:29:53.738Z\", \"hypothesis\": \"Walker Walk trained dt_emb + subsample ON + dt=1 imag + H=15 seed 2 — crown jewel C6 seed 2 验证\", \"metrics\": {\"actor_entropy_collapse_signature\": \"entropy rose from -5.21@85K to -3.83@105K (policy destabilizing during collapse)\", \"actor_entropy_trajectory\": [{\"actor_entropy\": 8.239, \"step\": 5000}, {\"actor_entropy\": 2.352, \"step\": 15000}, {\"actor_entropy\": 0.17, \"step\": 25000}, {\"actor_entropy\": -3.498, \"step\": 35000}, {\"actor_entropy\": -4.915, \"step\": 45000}, {\"actor_entropy\": -5.121, \"step\": 55000}, {\"actor_entropy\": -5.135, \"step\": 65000}, {\"actor_entropy\": -5.224, \"step\": 75000}, {\"actor_entropy\": -5.208, \"step\": 85000}, {\"actor_entropy\": -4.529, \"step\": 95000}, {\"actor_entropy\": -3.828, \"step\": 105000}], \"baseline_105K\": 915.67, \"collapse_confirmed\": \"105K (nve=3.78x, eval 715→137)\", \"collapse_onset\": \"95K (nve jumped from 0.68x to 1.34x)\", \"eval_trajectory\": [{\"eval_return\": 39.27, \"step\": 5000}, {\"eval_return\": 180.85, \"step\": 15000}, {\"eval_return\": 211.82, \"step\": 25000}, {\"eval_return\": 320.39, \"step\": 35000}, {\"eval_return\": 356.93, \"step\": 45000}, {\"eval_return\": 418.32, \"step\": 55000}, {\"eval_return\": 435.09, \"step\": 65000}, {\"eval_return\": 576.54, \"step\": 75000}, {\"eval_return\": 715.21, \"step\": 85000}, {\"eval_return\": 452.43, \"step\": 95000}, {\"eval_return\": 136.96, \"step\": 105000}], \"final_eval_return\": 136.96, \"final_nve\": 3.78, \"final_value_mean\": 339.84, \"final_ve_ratio\": 2.481, \"gate_dt_1_frac\": 1, \"gate_dt_mean\": 1, \"peak_eval_return\": 715.21, \"peak_eval_step\": 85000, \"train_return_108K\": \"19-23 (random policy level)\", \"value_trajectory\": [{\"step\": 5000, \"value_mean\": 0}, {\"step\": 15000, \"value_mean\": 3.91}, {\"step\": 25000, \"value_mean\": 30.27}, {\"step\": 35000, \"value_mean\": 79.75}, {\"step\": 45000, \"value_mean\": 125.25}, {\"step\": 55000, \"value_mean\": 172.89}, {\"step\": 65000, \"value_mean\": 220.47}, {\"step\": 75000, \"value_mean\": 272.64}, {\"step\": 85000, \"value_mean\": 339.3}, {\"step\": 95000, \"value_mean\": 384.39}, {\"step\": 105000, \"value_mean\": 339.84}], \"ve_ratio_trajectory\": [{\"nve\": 1.64, \"step\": 25000, \"ve\": 0.143}, {\"nve\": 1.03, \"step\": 35000, \"ve\": 0.249}, {\"nve\": 1.06, \"step\": 45000, \"ve\": 0.351}, {\"nve\": 1.02, \"step\": 55000, \"ve\": 0.413}, {\"nve\": 0.9, \"step\": 65000, \"ve\": 0.507}, {\"nve\": 0.66, \"step\": 75000, \"ve\": 0.473}, {\"nve\": 0.68, \"step\": 85000, \"ve\": 0.474}, {\"nve\": 1.34, \"step\": 95000, \"ve\": 0.85}, {\"nve\": 3.78, \"step\": 105000, \"ve\": 2.481}], \"vs_baseline_105K\": \"-85.0%\"}, \"notes\": \"C6 seed 2 COLLAPSED. Delusional critic collapse at 85K→105K despite gate_dt_mean=1.0 locked throughout. eval peaked 715@85K then crashed to 137@105K (v/e=2.48, nve=3.78x). Cross-seed: seed 0=869.9 (healthy), seed 1=869.9 (healthy), seed 2=137 (collapsed). Collapse is stochastic (1/3 seeds) even in dt=1 imagination config. Subsample ON training data (dt=2 transitions) appears sufficient to trigger delusional critic in some seeds. Train returns at 108K=19-23 (random policy).\", \"parent\": \"exp_008e_v3_subsample_on_dt1_h15\", \"status\": \"DONE\", \"updated_at\": \"2026-05-15T06:24:21.709Z\"}, \"exp_008e_v3_walker_s1\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-14T14:29:53.120Z\", \"hypothesis\": \"Walker Walk trained dt_emb + subsample ON + dt=1 imag + H=15 seed 1 — crown jewel C6 验证：trained dt_emb 在 dt=1 imagination 下不触发 delusional critic（plan_014）\", \"metrics\": {\"eval_trajectory\": [{\"eval_return\": 31, \"step\": 5000}, {\"eval_return\": 131.2, \"step\": 15000}, {\"eval_return\": 155.7, \"step\": 25000}, {\"eval_return\": 276.5, \"step\": 35000}, {\"eval_return\": 382.2, \"step\": 45000}, {\"eval_return\": 486.8, \"step\": 55000}, {\"eval_return\": 580.7, \"step\": 65000}, {\"eval_return\": 574.1, \"step\": 75000}, {\"eval_return\": 657.3, \"step\": 85000}, {\"eval_return\": 851.9, \"step\": 95000}, {\"eval_return\": 869.9, \"step\": 105000}], \"exit_code\": 0, \"final_eval_return\": 869.9, \"final_value_mean\": 457.9, \"gate_dt_1_frac\": 1, \"total_steps\": 112000, \"ve_ratio_105k\": 0.527}, \"notes\": \"Crown jewel C6 seed 1 SUCCESS. eval_return=869.9@105K, v/e=0.527 (healthy, no delusional critic). Gate locked dt=1 throughout. Trajectory: 31→131→156→276→382→487→581→574→657→852→870. Consistent with seed 0, confirms trained dt_emb + dt=1 imagination is safe.\", \"parent\": \"exp_008e_v3_subsample_on_dt1_h15\", \"status\": \"DONE\", \"updated_at\": \"2026-05-15T00:44:53.439Z\"}, \"exp_006\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-14T00:49:02.944Z\", \"metrics\": {\"baseline_return_at_55k\": 625.7, \"deficit_pct\": -42.4, \"deficit_vs_baseline_at_55k\": -265.3, \"eval_return\": {\"15000\": 256.9, \"25000\": 321.4, \"35000\": 485.3, \"45000\": 477, \"5000\": 31, \"55000\": 360.4}, \"gate_dt_mean\": 2, \"latest_return\": 360.4, \"latest_step\": 55000, \"model_loss_at_55k\": 4.853, \"peak_return\": 485.3, \"peak_step\": 35000}, \"notes\": \"早期条目，权威数据在 exp_006_fixed_dt2。conclusion=killed（D034 registry 清理）。\", \"status\": \"DONE\", \"updated_at\": \"2026-05-14T22:31:54.922Z\"}, \"exp_008a\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-14T04:07:59.793Z\", \"metrics\": {\"eval_return_15K\": 167.2, \"eval_return_25K\": 230.8, \"eval_return_35K\": 500.8, \"eval_return_45K\": 563.4, \"eval_return_55K\": 487.9, \"eval_return_5K\": 31, \"eval_return_65K\": \"pending (eval in progress)\", \"step\": 65000, \"train_return_64K_avg\": 556.6, \"trend\": \"peaked @45K=563, dipped to @55K=488, 65K eval in progress; train returns @64K healthy (~557)\", \"value_eval_ratio_55K\": \"37.6%\", \"value_mean_55K\": 183.5}, \"notes\": \"早期条目，权威数据在 exp_008a_no_subsample_dt2。conclusion=killed（D034 registry 清理）。\", \"status\": \"DONE\", \"updated_at\": \"2026-05-14T22:31:54.075Z\"}, \"exp_008c\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-14T04:08:02.608Z\", \"metrics\": {\"eval_return_15K\": 171.3, \"eval_return_25K\": 192.4, \"eval_return_35K\": 185.1, \"eval_return_45K\": 226.6, \"eval_return_55K\": 241.9, \"eval_return_5K\": 31, \"eval_return_65K\": 240.9, \"step\": 68000, \"train_return_68K_avg\": 245.1, \"trend\": \"flat plateau @55K-65K (~241), very slow learner with h8, value/eval=32.8% (no collapse)\", \"value_eval_ratio_65K\": \"32.8%\", \"value_mean_65K\": 79}, \"notes\": \"早期条目，权威数据在正式命名实验中。conclusion=killed（D034 registry 清理）。\", \"status\": \"DONE\", \"updated_at\": \"2026-05-14T22:31:52.611Z\"}, \"exp_008d\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-14T04:08:05.136Z\", \"metrics\": {\"eval_return_15K\": 153.7, \"eval_return_25K\": 167.2, \"eval_return_35K\": 146.3, \"eval_return_5K\": 31, \"step\": 40000, \"train_return_40K_avg\": 119.3, \"trend\": \"declining — train_return @40K avg=119 below @35K eval=146, value/eval=41.1% not yet >50% but train performance dropping\", \"value_eval_ratio_35K\": \"41.1%\", \"value_mean_35K\": 60.2}, \"notes\": \"早期条目，权威数据在 exp_008d_subsample_on_h8。conclusion=killed（D034 registry 清理）。\", \"status\": \"DONE\", \"updated_at\": \"2026-05-14T22:31:51.696Z\"}, \"exp_008e_v2_subsample_on_dt1_h15\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-14T04:26:39.732Z\", \"notes\": \"已被 exp_008e_v3_subsample_on_dt1_h15 取代，进程已死。conclusion=killed（D034 registry 清理）。\", \"status\": \"DONE\", \"updated_at\": \"2026-05-14T22:31:49.814Z\"}, \"exp_rssm_fidelity_analysis\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-14T11:09:52.237Z\", \"hypothesis\": \"RSSM prediction quality analysis: 比较 baseline/008d/008f 在 dt=1 vs dt=2 transitions 上的 obs_MSE 和 reward_MAE，量化 RSSM fidelity gap (plan_030)\", \"metrics\": {\"008d_trained_dtEmb\": {\"dt1_obs_mse\": 41.31, \"dt1_reward_mae\": 0.0568, \"dt2_obs_mse\": 53.67, \"dt2_reward_mae\": 0.1579, \"obs_gap\": 1.3, \"reward_gap\": 2.78}, \"008f_no_dtEmb\": {\"dt1_obs_mse\": 8.01, \"dt1_reward_mae\": 0.7469, \"dt2_obs_mse\": 22.04, \"dt2_reward_mae\": 0.7526, \"obs_gap\": 2.75, \"reward_gap\": 1.01}, \"baseline\": {\"dt1_obs_mse\": 13.49, \"dt1_reward_mae\": 0.0102, \"dt2_obs_mse\": 27.5, \"dt2_reward_mae\": 0.0159, \"obs_gap\": 2.04, \"reward_gap\": 1.56}}, \"notes\": \"分析实验，非训练实验。conclusion=success，状态从 PREPARING 修正为 DONE（D034 registry 清理）。\", \"status\": \"DONE\", \"updated_at\": \"2026-05-14T22:31:48.642Z\"}, \"exp_008e_v3_subsample_on_dt1_h15\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-14T04:29:31.656Z\", \"hypothesis\": \"B+ confound control：subsample ON + untrained dt_emb + dt=1 imagination + H=15。验证 subsample ON 训练数据（含 dt=2 transitions）是否本身导致性能下降，即使 imagination 只用 dt=1。对照 008a（subsample OFF）和 baseline。如果 008e_v3 性能接近 baseline → subsample ON 本身无害。如果下降 → subsample ON 改变了 RSSM dynamics。\", \"metrics\": {\"baseline_105K\": 915.67, \"current_step\": 112000, \"eval_return\": {\"105K\": 869.88, \"15K\": 131.2, \"25K\": 155.69, \"35K\": 276.47, \"45K\": 382.22, \"55K\": 486.84, \"5K\": 31, \"65K\": 580.67, \"75K\": 574.09, \"85K\": 657.31, \"95K\": 851.86}, \"fps\": 7.01, \"gate_dt_1_frac\": 1, \"gate_dt_mean\": 1, \"last_updated\": \"2026-05-14T09:09:00\", \"normalized_ve\": {\"105K\": 0.8, \"25K\": 1.93, \"35K\": 0.94, \"45K\": 0.88, \"55K\": 0.87, \"65K\": 0.72, \"75K\": 0.73, \"85K\": 0.76, \"95K\": 0.75}, \"target_steps\": 105000, \"value_eval_ratio\": {\"105K\": 0.527, \"25K\": 0.168, \"35K\": 0.227, \"45K\": 0.29, \"55K\": 0.35, \"65K\": 0.405, \"75K\": 0.523, \"85K\": 0.534, \"95K\": 0.476}, \"value_mean\": {\"105K\": 457.93, \"25K\": 26.19, \"35K\": 62.76, \"45K\": 110.67, \"55K\": 170.09, \"65K\": 235.05, \"75K\": 300.51, \"85K\": 351.33, \"95K\": 405.25}, \"verdict\": \"SUCCESS - 95% baseline, normalized v/e stable 0.72-0.80x, B+ hypothesis confirmed\", \"vs_baseline_105K\": \"-5.0%\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T19:46:00.840Z\"}, \"exp_009c_008f_walker_s2\": {\"conclusion\": \"negative\", \"created_at\": \"2026-05-14T07:17:26.154Z\", \"hypothesis\": \"Walker Walk dt_embed_dim=0 + subsample ON + H=8 seed 2 — 多 seed 复现 008f 因果控制稳定性，巩固 C2 统计显著性（plan_012）\", \"metrics\": {\"baseline_105K\": 915.67, \"causal_conclusion\": \"Seed 2 does NOT replicate seed 1's zigzag recovery. 008f seed 1 peaked at 503@105K with rising trend; seed 2 peaked at 359@75K then declined to 148@105K. The adaptive horizon mechanism's benefit appears seed-dependent and not robust.\", \"current_step\": 105000, \"eval_checkpoints\": [{\"baseline_ve\": null, \"eval_return\": 30.37, \"normalized_ve\": null, \"step\": 5000, \"value_mean\": 0.0013, \"ve_ratio\": null}, {\"baseline_ve\": null, \"eval_return\": 157.15, \"normalized_ve\": null, \"step\": 15000, \"value_mean\": 3.057, \"ve_ratio\": 0.019}, {\"baseline_ve\": 0.087, \"eval_return\": 168.75, \"normalized_ve\": 1.26, \"step\": 25000, \"value_mean\": 18.536, \"ve_ratio\": 0.11}, {\"baseline_ve\": 0.241, \"eval_return\": 178.94, \"normalized_ve\": 0.79, \"step\": 35000, \"value_mean\": 34.263, \"ve_ratio\": 0.191}, {\"baseline_ve\": 0.331, \"eval_return\": 211.08, \"normalized_ve\": 0.72, \"step\": 45000, \"value_mean\": 50.099, \"ve_ratio\": 0.237}, {\"baseline_ve\": 0.404, \"eval_return\": 238.91, \"normalized_ve\": 0.66, \"step\": 55000, \"value_mean\": 63.267, \"ve_ratio\": 0.265}, {\"baseline_ve\": 0.563, \"eval_return\": 244.15, \"normalized_ve\": 0.53, \"step\": 65000, \"value_mean\": 72.717, \"ve_ratio\": 0.298}, {\"baseline_ve\": 0.719, \"eval_return\": 359.14, \"normalized_ve\": 0.33, \"step\": 75000, \"value_mean\": 83.91, \"ve_ratio\": 0.234}, {\"baseline_ve\": 0.701, \"eval_return\": 227.43, \"normalized_ve\": 0.6, \"step\": 85000, \"value_mean\": 96.071, \"ve_ratio\": 0.422}, {\"baseline_ve\": 0.632, \"eval_return\": 190.94, \"normalized_ve\": 0.9, \"step\": 95000, \"value_mean\": 108.29, \"ve_ratio\": 0.567}, {\"baseline_ve\": 0.656, \"eval_return\": 148.34, \"normalized_ve\": 1.14, \"step\": 105000, \"value_mean\": 111.247, \"ve_ratio\": 0.75}], \"target_steps\": 105000, \"trend\": \"Peak 359@75K then monotonic decline to 148@105K; no recovery pattern unlike 008f seed 1's zigzag recovery to 503\", \"verdict\": \"NEGATIVE - no delusional critic (normalized v/e < 1.5x) but persistent decline after 75K; cross-seed consistency with 008f seed 1 NOT confirmed\", \"vs_baseline_105K\": \"-83.8%\"}, \"notes\": \"D031 排期修正: 009c 延长 200K 降优先级，排在 009e/009f 之后。cuda:1 排期: 009b → 008e_v3_s1 → 008e_v3_s2 → 009e → 009f → 009c(200K) → plan_060。105K 指标: eval=148.34, value=111.25, nve=1.14x。\", \"parent\": \"exp_008f_no_dt_embed_subsample_on_h8\", \"status\": \"DONE\", \"updated_at\": \"2026-05-14T14:34:24.161Z\"}, \"exp_006_fixed_dt2\": {\"conclusion\": \"negative\", \"created_at\": \"2026-05-13T21:10:58.851Z\", \"hypothesis\": \"诊断实验：fixed dt=2 vs learned gate。去掉 Gumbel-Softmax gate，硬编码 dt=2，其余超参与 exp_005 完全一致。量化 learned gate 的价值——如果 fixed dt=2 也掉 return，说明跳步本身有害；如果不掉，问题在 gate 学习机制。\", \"metrics\": {\"baseline_35K\": 388.5, \"baseline_45K\": 513.8, \"baseline_55K\": 625.7, \"data_source_ve\": \"from training logs metrics.jsonl\", \"eval_return_15K\": 256.9, \"eval_return_25K\": 321.4, \"eval_return_35K\": 485.3, \"eval_return_45K\": 477, \"eval_return_55K\": 360.4, \"eval_return_5K\": 31, \"eval_return_65K\": 132.86, \"fps\": 6.5, \"gate_dt_mean\": 2, \"gate_dt_std\": 0, \"model_loss_15K\": 7.593, \"model_loss_25K\": 5.633, \"model_loss_35K\": 5.229, \"model_loss_45K\": 5.023, \"model_loss_55K\": 4.9, \"model_loss_5K\": 20.738, \"peak_return\": 485.3, \"peak_step\": \"35K\", \"step\": 65000, \"trend\": \"inverted-V: peak 485@35K, collapsing to 133@65K; v/e accelerating: 31.1%→53.3%→93.3%→272% (value 2.7x eval_return at 65K)\", \"value_eval_ratio_35K\": 0.311, \"value_eval_ratio_45K\": 0.533, \"value_eval_ratio_55K\": 0.933, \"value_eval_ratio_65K\": 2.722, \"value_mean_35K\": 151.1, \"value_mean_45K\": 254.29, \"value_mean_55K\": 336.44, \"value_mean_65K\": 361.69, \"vs_baseline_55K\": \"-42.4%\"}, \"parent\": \"exp_005_event_gated_v4\", \"status\": \"DONE\", \"updated_at\": \"2026-05-14T10:20:11.722Z\"}, \"exp_008e_subsample_on_fixed_dt1\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-14T04:10:07.303Z\", \"hypothesis\": \"验证 Reviewer D020 因果假说：subsample ON 训练 dt_embedding[2]（RSSM 精确预测 dt=2），但 actor/critic 仅在 dt=1 imagination 训练。如果 value/eval ratio 仍加速上升 → dt_embedding 训练本身导致 value 过估（delusional critic），即使 actor 不用 dt=2 imagination。对照：008a (subsample OFF, dt=2 imag) value/eval=37.6%@55K vs exp_006 (subsample ON, dt=2 imag) 53.3%。\", \"status\": \"DONE\", \"updated_at\": \"2026-05-14T04:24:58.056Z\"}, \"exp_008e_subsample_on_dt1_h15\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-14T04:10:37.655Z\", \"hypothesis\": \"验证 Reviewer D020 delusional critic 假说：subsample ON 训练 dt_embedding[2]（RSSM 精确预测 dt=2），但 actor/critic 仅在 dt=1 imagination 训练。如果 value/eval ratio 仍加速上升 → dt_embedding 训练本身导致 value 过估（即使 actor 不用 dt=2 imagination）。对照：008a（subsample OFF，dt=2 imagination）和 006（subsample ON，dt=2 imagination）。\", \"notes\": \"重复进程：与 exp_008e_subsample_on_fixed_dt1 命令完全相同，共享同一 logdir，导致 tfevents 文件互相污染。Kill PID 122038，保留 PID 121636。\", \"status\": \"DONE\", \"updated_at\": \"2026-05-14T04:24:57.658Z\"}, \"exp_002_event_gated\": {\"conclusion\": \"failed\", \"created_at\": \"2026-05-13T02:09:54.240Z\", \"hypothesis\": \"Event-gated variable-rate RSSM produces meaningful Δt patterns (entropy>0.3, H_eff>1.2×H_nominal) without breaking training stability (return≥80% baseline)\", \"status\": \"DONE\", \"updated_at\": \"2026-05-13T04:52:18.089Z\"}}, \"count\": 158, \"total\": 158, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.6081}}"
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
The rebuttal_qa.md isn't in the standard project files list. Let me find it on disk. Also, the registry output is huge, so let me use jq to extract the counts I need. Let me do both in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ae813a79-db9f-4a12-b6ee-ad91ade39065",
  "uuid": "3daa39ea-f4fb-47e5-8575-7ce6efbc55bd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NyBoWQ21rwo8sgdf3zpjwo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 818,
      "cache_read_input_tokens": 24208,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 818
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

The rebuttal Q&A isn't a standard project file. Let me find it on disk and extract registry counts.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ae813a79-db9f-4a12-b6ee-ad91ade39065",
  "uuid": "b1f61238-dfd3-4065-9635-d2453af5bde6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NyBoWQ21rwo8sgdf3zpjwo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 818,
      "cache_read_input_tokens": 24208,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 818
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

<details open><summary>🔧 Tool call — Glob · `toolu_018qinsXsaxD2shaEAGLSTs5`</summary>

```json
{
  "pattern": "**/rebuttal_qa*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ae813a79-db9f-4a12-b6ee-ad91ade39065",
  "uuid": "9729cfdb-b2da-4ead-9377-58a9d4f20974",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NyBoWQ21rwo8sgdf3zpjwo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 818,
      "cache_read_input_tokens": 24208,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 818
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


### Tool result

_source line 15 · 2026-05-25T14:11:18.722Z_

<details><summary>↩ Tool result · `toolu_018qinsXsaxD2shaEAGLSTs5`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ae813a79-db9f-4a12-b6ee-ad91ade39065",
  "uuid": "38d54195-8d55-42b3-9ea1-e2d01a5ba176",
  "tool_use_result": {
    "filenames": [],
    "durationMs": 15,
    "numFiles": 0,
    "truncated": false
  }
}
```

</details>

---


### Tool call

_source line 16_

<details open><summary>🔧 Tool call — Bash · `toolu_01KwUk7YpzWRjyfHqo2sPA3A`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/ae813a79-db9f-4a12-b6ee-ad91ade39065/tool-results/mcp-agent-ml-research-read_registry-1779718272790.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps = result.get('data', result) if isinstance(result, dict) else result\nif isinstance(exps, dict) and 'experiments' in exps:\n    exps = exps['experiments']\nelif isinstance(exps, dict) and 'data' in exps:\n    exps = exps['data']\n\n# Handle if exps is still a dict\nif isinstance(exps, dict):\n    # Try to iterate values\n    items = list(exps.values()) if not isinstance(list(exps.values())[0], str) else []\n    if items:\n        exps = items\n\ntotal = len(exps)\nconclusions = {}\nfor e in exps:\n    c = e.get('conclusion', 'unknown') if isinstance(e, dict) else 'unknown'\n    conclusions[c] = conclusions.get(c, 0) + 1\n\nprint(f'Total experiments: {total}')\nfor k, v in sorted(conclusions.items()):\n    print(f'  {k}: {v}')\n\n# Count unique configurations\nconfigs = set()\nfor e in exps:\n    if isinstance(e, dict):\n        cfg = e.get('config', e.get('configuration', e.get('name', '')))\n        if isinstance(cfg, str):\n            configs.add(cfg)\nprint(f'Unique configs/names: {len(configs)}')\n\"\n",
  "description": "Parse registry JSON to count experiments by conclusion",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ae813a79-db9f-4a12-b6ee-ad91ade39065",
  "uuid": "2c3ba4bd-1956-4f45-964c-059d14937837",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NyBoWQ21rwo8sgdf3zpjwo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 818,
      "cache_read_input_tokens": 24208,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 818
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


### Tool result

_source line 17 · 2026-05-25T14:11:25.812Z_

<details><summary>↩ Tool result · `toolu_01KwUk7YpzWRjyfHqo2sPA3A`</summary>

```text
Total experiments: 158
  failed: 11
  killed: 24
  negative: 39
  success: 79
  unknown: 5
Unique configs/names: 1
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ae813a79-db9f-4a12-b6ee-ad91ade39065",
  "uuid": "b78fb84e-b2b2-41fc-8320-7ebbefb374c6",
  "tool_use_result": {
    "stdout": "Total experiments: 158\n  failed: 11\n  killed: 24\n  negative: 39\n  success: 79\n  unknown: 5\nUnique configs/names: 1",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Assistant

_source line 18_

<details><summary>Logged reasoning block</summary>

```text
Total experiments: 158, with 79 success, 39 negative, 11 failed, 24 killed, 5 unknown. The unique configs count of 1 is not right - let me look at the structure of each experiment to find the right field for configurations.

Let me also find the rebuttal_qa.md file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ae813a79-db9f-4a12-b6ee-ad91ade39065",
  "uuid": "809e6663-c289-4a48-a21b-7fb869f62df2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EzejZq9BRRA8MUNJRSZViZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 841,
      "cache_read_input_tokens": 25026,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 841
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

_source line 19_

Got the registry counts: 158 total (79 success, 39 negative, 11 failed, 24 killed, 5 unknown). Now let me find the rebuttal file and get unique configurations.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ae813a79-db9f-4a12-b6ee-ad91ade39065",
  "uuid": "be738aff-e998-43d0-b372-01f706ae7b26",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EzejZq9BRRA8MUNJRSZViZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 841,
      "cache_read_input_tokens": 25026,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 841
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

_source line 20_

<details open><summary>🔧 Tool call — Bash · `toolu_01S3qyu3hpXDRKquAyAmejD2`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon -name \"*rebuttal*\" -type f 2>/dev/null",
  "description": "Find rebuttal files in project"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ae813a79-db9f-4a12-b6ee-ad91ade39065",
  "uuid": "304142c2-3637-466d-abd7-100cb6a7fdc3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EzejZq9BRRA8MUNJRSZViZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 841,
      "cache_read_input_tokens": 25026,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 841
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


### Tool result

_source line 21 · 2026-05-25T14:11:31.441Z_

<details><summary>↩ Tool result · `toolu_01S3qyu3hpXDRKquAyAmejD2`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/rebuttal_notes.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_paper_rebuttal_prep_expansion_20260524T114857.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_paper_rebuttal-prewrite_20260518T181655.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_verify_rebuttal-q5-numbers_20260524T032017_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_paper_rebuttal_prep_expansion_20260524T114857_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_paper_rebuttal-prewrite_20260518T181655_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_draft_rebuttal-prep_20260524T030759_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_draft_rebuttal-prep_20260524T030759.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_paper_rebuttal_qa_update_20260525T141052.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_writing_rebuttal_draft_framework_20260522T073659.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_verify_rebuttal-q5-numbers_20260524T032017.log
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_writing_rebuttal_draft_framework_20260522T073659_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/chats/worker_paper_rebuttal_prep_expansion_20260524T114857.lock
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/chats/worker_paper_rebuttal_prep_expansion_20260524T114857.jsonl
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/report/rebuttal_prep.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/report/rebuttal_draft.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/rebuttal_prep.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/rebuttal_draft.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ae813a79-db9f-4a12-b6ee-ad91ade39065",
  "uuid": "dd75d3e2-f5b0-42f7-aa04-b7bd143ed411",
  "tool_use_result": {
    "stdout": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/rebuttal_notes.md\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_paper_rebuttal_prep_expansion_20260524T114857.log\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_paper_rebuttal-prewrite_20260518T181655.log\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_verify_rebuttal-q5-numbers_20260524T032017_result.json\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_paper_rebuttal_prep_expansion_20260524T114857_result.json\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_paper_rebuttal-prewrite_20260518T181655_result.json\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_draft_rebuttal-prep_20260524T030759_result.json\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_draft_rebuttal-prep_20260524T030759.log\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_paper_rebuttal_qa_update_20260525T141052.log\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_writing_rebuttal_draft_framework_20260522T073659.log\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_verify_rebuttal-q5-numbers_20260524T032017.log\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_writing_rebuttal_draft_framework_20260522T073659_result.json\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/chats/worker_paper_rebuttal_prep_expansion_20260524T114857.lock\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/chats/worker_paper_rebuttal_prep_expansion_20260524T114857.jsonl\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/report/rebuttal_prep.md\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/report/rebuttal_draft.md\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/rebuttal_prep.md\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/rebuttal_draft.md",
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

_source line 22_

<details open><summary>🔧 Tool call — Bash · `toolu_01MNqmnMEQ3riuGcMyCR1Vdw`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/ae813a79-db9f-4a12-b6ee-ad91ade39065/tool-results/mcp-agent-ml-research-read_registry-1779718272790.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps = result.get('data', result) if isinstance(result, dict) else result\nif isinstance(exps, dict) and 'experiments' in exps:\n    exps = exps['experiments']\nelif isinstance(exps, dict) and 'data' in exps:\n    exps = exps['data']\n\n# Print keys of first experiment to understand structure\nif exps and isinstance(exps[0], dict):\n    print('Keys:', list(exps[0].keys()))\n    print()\n    # Print first experiment as sample\n    e = exps[0]\n    for k, v in e.items():\n        print(f'  {k}: {v}')\n\"\n",
  "description": "Inspect registry experiment structure",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ae813a79-db9f-4a12-b6ee-ad91ade39065",
  "uuid": "9958c75b-21f5-4a2e-8475-427fca5daacc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EzejZq9BRRA8MUNJRSZViZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 841,
      "cache_read_input_tokens": 25026,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 841
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


### Tool result

_source line 23 · 2026-05-25T14:11:35.237Z_

<details><summary>↩ Tool result · reported error · `toolu_01MNqmnMEQ3riuGcMyCR1Vdw`</summary>

```text
Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 12, in &lt;module>
    if exps and isinstance(exps[0], dict):
                           ~~~~^^^
KeyError: 0
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ae813a79-db9f-4a12-b6ee-ad91ade39065",
  "uuid": "32e54d9b-4196-4bac-af28-f3c159450e8e",
  "tool_use_result": "Error: Exit code 1\nTraceback (most recent call last):\n  File \"&lt;string>\", line 12, in &lt;module>\n    if exps and isinstance(exps[0], dict):\n                           ~~~~^^^\nKeyError: 0"
}
```

</details>

---


### Assistant

_source line 24_

<details><summary>Logged reasoning block</summary>

```text
The experiments are stored as a dict (keyed by experiment ID), not a list. Let me fix the parsing. Also, let me search for the rebuttal_qa.md file - it might be in artifacts or docs.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ae813a79-db9f-4a12-b6ee-ad91ade39065",
  "uuid": "4e795cfe-47f6-4ab2-836d-c037b488432d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UKNNjQ5nJkbhPqfcaGva2o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1796,
      "cache_read_input_tokens": 25867,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1796
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

_source line 25_

<details open><summary>🔧 Tool call — Bash · `toolu_01RJh3wmoxGWkpcP96nHH848`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon -name \"*rebuttal*qa*\" -o -name \"*qa*rebuttal*\" 2>/dev/null",
  "description": "Find rebuttal QA file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ae813a79-db9f-4a12-b6ee-ad91ade39065",
  "uuid": "14eea24f-0a07-46c4-8f1a-eb779b333652",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UKNNjQ5nJkbhPqfcaGva2o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1796,
      "cache_read_input_tokens": 25867,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1796
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


### Tool result

_source line 26 · 2026-05-25T14:11:40.048Z_

<details><summary>↩ Tool result · `toolu_01RJh3wmoxGWkpcP96nHH848`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_paper_rebuttal_qa_update_20260525T141052.log
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ae813a79-db9f-4a12-b6ee-ad91ade39065",
  "uuid": "7258be9e-c2db-48f3-9775-b7132c82824f",
  "tool_use_result": {
    "stdout": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/logs/workers/worker_paper_rebuttal_qa_update_20260525T141052.log",
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

_source line 27_

<details open><summary>🔧 Tool call — Bash · `toolu_01Ux9YsAFzktB2Zj3qiJ7psi`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/ae813a79-db9f-4a12-b6ee-ad91ade39065/tool-results/mcp-agent-ml-research-read_registry-1779718272790.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps = result.get('data', result) if isinstance(result, dict) else result\nif isinstance(exps, dict) and 'experiments' in exps:\n    exps = exps['experiments']\nelif isinstance(exps, dict) and 'data' in exps:\n    exps = exps['data']\n\n# It's a dict keyed by experiment ID\nif isinstance(exps, dict):\n    items = list(exps.values())\nelse:\n    items = exps\n\n# Print keys of first experiment\nfirst = items[0] if isinstance(items[0], dict) else None\nif first:\n    print('Keys:', sorted(first.keys()))\n    print()\n    # Look for config-related fields\n    for k in ['env', 'environment', 'config', 'configuration', 'env_id', 'env_name', 'tags', 'hypothesis']:\n        if k in first:\n            print(f'  {k}: {first[k]}')\n\"\n",
  "description": "Inspect experiment dict structure",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ae813a79-db9f-4a12-b6ee-ad91ade39065",
  "uuid": "6608d5de-a8d8-40fe-bb45-cf9045aa7ca9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UKNNjQ5nJkbhPqfcaGva2o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1796,
      "cache_read_input_tokens": 25867,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1796
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


### Tool result

_source line 28 · 2026-05-25T14:11:47.830Z_

<details><summary>↩ Tool result · `toolu_01Ux9YsAFzktB2Zj3qiJ7psi`</summary>

```text
Keys: ['created_at', 'hypothesis', 'parent', 'status', 'updated_at']

  hypothesis: Cheetah Run causal control: dt_embed_dim=0 + subsample ON + dt=2 + H=8, seed=0。移除 dt_embedding 后预期无 CIVO，证明 trained dt_emb 是 Cheetah CIVO 的必要条件。与 exp_078 (trained dt_emb, CIVO trigger) 构成因果对。plan_022。
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ae813a79-db9f-4a12-b6ee-ad91ade39065",
  "uuid": "c5051a20-196f-4f87-a263-ceccc2262f9b",
  "tool_use_result": {
    "stdout": "Keys: ['created_at', 'hypothesis', 'parent', 'status', 'updated_at']\n\n  hypothesis: Cheetah Run causal control: dt_embed_dim=0 + subsample ON + dt=2 + H=8, seed=0。移除 dt_embedding 后预期无 CIVO，证明 trained dt_emb 是 Cheetah CIVO 的必要条件。与 exp_078 (trained dt_emb, CIVO trigger) 构成因果对。plan_022。",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Assistant

_source line 29_

<details><summary>Logged reasoning block</summary>

```text
The summary fields only show a few fields. I need to get all fields to find configurations. Let me also look for the rebuttal Q&A file - it seems like it might be in the artifacts directory or somewhere else. Let me search more broadly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ae813a79-db9f-4a12-b6ee-ad91ade39065",
  "uuid": "ba5599c5-81fb-4b4e-a4ed-9d873cb87a9d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011msXMv2SXj6uHE22h13Lok",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 881,
      "cache_read_input_tokens": 27663,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 881
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

_source line 30_

<details open><summary>🔧 Tool call — Glob · `toolu_011QjsA3KVWLzBRCSrGXmDAK`</summary>

```json
{
  "pattern": "**/*rebuttal*qa*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ae813a79-db9f-4a12-b6ee-ad91ade39065",
  "uuid": "531a465d-6561-406a-88fc-6d97a4f9748a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011msXMv2SXj6uHE22h13Lok",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 881,
      "cache_read_input_tokens": 27663,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 881
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


### Tool result

_source line 31 · 2026-05-25T14:11:52.625Z_

<details><summary>↩ Tool result · `toolu_011QjsA3KVWLzBRCSrGXmDAK`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ae813a79-db9f-4a12-b6ee-ad91ade39065",
  "uuid": "10ece797-fe2b-4080-8969-ed26f6e33554",
  "tool_use_result": {
    "filenames": [],
    "durationMs": 9,
    "numFiles": 0,
    "truncated": false
  }
}
```

</details>

---


### Tool call

_source line 32_

<details open><summary>🔧 Tool call — Glob · `toolu_01RYL6NhSVH5FbmfGmH8tqYv`</summary>

```json
{
  "pattern": "**/*qa*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ae813a79-db9f-4a12-b6ee-ad91ade39065",
  "uuid": "a92e7708-c5c8-4e2c-af09-8dd4556b3a2c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011msXMv2SXj6uHE22h13Lok",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 881,
      "cache_read_input_tokens": 27663,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 881
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


### Tool result

_source line 33 · 2026-05-25T14:11:53.103Z_

<details><summary>↩ Tool result · `toolu_01RYL6NhSVH5FbmfGmH8tqYv`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ae813a79-db9f-4a12-b6ee-ad91ade39065",
  "uuid": "466e8cf2-b5e4-4034-b686-490a7bafc550",
  "tool_use_result": {
    "filenames": [],
    "durationMs": 8,
    "numFiles": 0,
    "truncated": false
  }
}
```

</details>

---


### Tool call

_source line 34_

<details open><summary>🔧 Tool call — Bash · `toolu_01TEg6K1pVo4qDUoWhz84KJ8`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/ae813a79-db9f-4a12-b6ee-ad91ade39065/tool-results/mcp-agent-ml-research-read_registry-1779718272790.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps = result.get('data', result) if isinstance(result, dict) else result\nif isinstance(exps, dict) and 'experiments' in exps:\n    exps = exps['experiments']\nelif isinstance(exps, dict) and 'data' in exps:\n    exps = exps['data']\n\nif isinstance(exps, dict):\n    items = list(exps.values())\n    exp_ids = list(exps.keys())\nelse:\n    items = exps\n    exp_ids = range(len(items))\n\n# Get all fields from first experiment with full detail\nprint('=== Full fields for first exp ===')\nfirst_id = exp_ids[0] if isinstance(exp_ids[0], str) else 0\nprint(f'ID: {first_id}')\nprint(json.dumps(items[0], indent=2, default=str)[:3000])\n\" 2>&1 | head -60\n",
  "description": "Show full first experiment record",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ae813a79-db9f-4a12-b6ee-ad91ade39065",
  "uuid": "3c20e5a0-4a1e-4e92-b233-c894eae4fdb6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011msXMv2SXj6uHE22h13Lok",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 881,
      "cache_read_input_tokens": 27663,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 881
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


### Tool result

_source line 35 · 2026-05-25T14:11:57.506Z_

<details><summary>↩ Tool result · `toolu_01TEg6K1pVo4qDUoWhz84KJ8`</summary>

```text
=== Full fields for first exp ===
ID: exp_082_cheetah_no_dt_emb_s0
{
  "status": "RUNNING",
  "created_at": "2026-05-25T13:12:29.199Z",
  "updated_at": "2026-05-25T14:10:44.478Z",
  "hypothesis": "Cheetah Run causal control: dt_embed_dim=0 + subsample ON + dt=2 + H=8, seed=0\u3002\u79fb\u9664 dt_embedding \u540e\u9884\u671f\u65e0 CIVO\uff0c\u8bc1\u660e trained dt_emb \u662f Cheetah CIVO \u7684\u5fc5\u8981\u6761\u4ef6\u3002\u4e0e exp_078 (trained dt_emb, CIVO trigger) \u6784\u6210\u56e0\u679c\u5bf9\u3002plan_022\u3002",
  "parent": "exp_010b_cheetah_civo_trigger"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ae813a79-db9f-4a12-b6ee-ad91ade39065",
  "uuid": "2a4a4ee3-50f0-418f-84db-07411e3c75ad",
  "tool_use_result": {
    "stdout": "=== Full fields for first exp ===\nID: exp_082_cheetah_no_dt_emb_s0\n{\n  \"status\": \"RUNNING\",\n  \"created_at\": \"2026-05-25T13:12:29.199Z\",\n  \"updated_at\": \"2026-05-25T14:10:44.478Z\",\n  \"hypothesis\": \"Cheetah Run causal control: dt_embed_dim=0 + subsample ON + dt=2 + H=8, seed=0\\u3002\\u79fb\\u9664 dt_embedding \\u540e\\u9884\\u671f\\u65e0 CIVO\\uff0c\\u8bc1\\u660e trained dt_emb \\u662f Cheetah CIVO \\u7684\\u5fc5\\u8981\\u6761\\u4ef6\\u3002\\u4e0e exp_078 (trained dt_emb, CIVO trigger) \\u6784\\u6210\\u56e0\\u679c\\u5bf9\\u3002plan_022\\u3002\",\n  \"parent\": \"exp_010b_cheetah_civo_trigger\"\n}",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Assistant

_source line 36_

<details><summary>Logged reasoning block</summary>

```text
The summary fields are minimal. I need to request more fields. Let me try with `fields=["*"]` to get all fields, and also find the rebuttal Q&A file.

The rebuttal Q&A file might be in a different location. Let me search the docs/paper directory and the artifacts directory more broadly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ae813a79-db9f-4a12-b6ee-ad91ade39065",
  "uuid": "10ec3706-98a0-4121-8aa0-59a7b750d233",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HnZQmqC3L6C6RdPUnzsDkt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1076,
      "cache_read_input_tokens": 28544,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1076
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

_source line 37_

<details open><summary>🔧 Tool call — Bash · `toolu_01UAEmkf8Q3w2EhZuFMyGpTf`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper -type f -name \"*.md\" | head -20",
  "description": "List paper docs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ae813a79-db9f-4a12-b6ee-ad91ade39065",
  "uuid": "b55e85d3-0bcf-43d4-b8a6-7f231178017b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HnZQmqC3L6C6RdPUnzsDkt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1076,
      "cache_read_input_tokens": 28544,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1076
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


### Tool result

_source line 38 · 2026-05-25T14:12:02.349Z_

<details><summary>↩ Tool result · `toolu_01UAEmkf8Q3w2EhZuFMyGpTf`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/rebuttal_notes.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ae813a79-db9f-4a12-b6ee-ad91ade39065",
  "uuid": "3681df79-0803-4956-8fc2-2ec46b8cd08c",
  "tool_use_result": {
    "stdout": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/rebuttal_notes.md",
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

_source line 39_

<details open><summary>🔧 Tool call — Bash · `toolu_01KbwNjRKdzUiQjotmmUhq1K`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts -type f -name \"*.md\" | head -30",
  "description": "List artifact md files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ae813a79-db9f-4a12-b6ee-ad91ade39065",
  "uuid": "5ad10c8f-2778-402d-9b7a-420ecbe81ea2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HnZQmqC3L6C6RdPUnzsDkt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1076,
      "cache_read_input_tokens": 28544,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1076
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


### Tool result

_source line 40 · 2026-05-25T14:12:03.091Z_

<details><summary>↩ Tool result · `toolu_01KbwNjRKdzUiQjotmmUhq1K`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/check_037_038_status.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/plan_033/report/analysis_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/exp_009b_008d_walker_s2/report/009b_literature_search.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/gradient_decomposition_methodology.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/narrative_frameworks.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/claim_audit_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/sgs_gradient_analysis.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/related_work_expanded_704dea.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/reference_audit_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/method_90ca4b.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/introduction_draft.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/related_work_section_6c6fde.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/narrative_frameworks_95c2c8.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/method_framingB_reaudit_v2.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/related_work_draft_0456d1.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/related_work_draft.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/detector_section_draft.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/method.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/related_work_section.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/experimental_setup_c0856a.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/experimental_setup.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/discussion_conclusion_draft.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/related_work_expanded.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/results.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/results_section_draft.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/cross_env_results.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/results_seed3_patch.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/intermediate/paper_numbers_update_draft.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/intermediate/civo_detector_implementation.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/intermediate/CHANGES.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ae813a79-db9f-4a12-b6ee-ad91ade39065",
  "uuid": "2f776bf8-981e-4f3e-b567-6d7cf2cc3fde",
  "tool_use_result": {
    "stdout": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/check_037_038_status.md\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/plan_033/report/analysis_report.md\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/exp_009b_008d_walker_s2/report/009b_literature_search.md\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/gradient_decomposition_methodology.md\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/narrative_frameworks.md\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/claim_audit_report.md\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/sgs_gradient_analysis.md\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/related_work_expanded_704dea.md\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/reference_audit_report.md\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/method_90ca4b.md\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/introduction_draft.md\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/related_work_section_6c6fde.md\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/narrative_frameworks_95c2c8.md\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/method_framingB_reaudit_v2.md\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/related_work_draft_0456d1.md\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/related_work_draft.md\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/detector_section_draft.md\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/method.md\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/related_work_section.md\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/experimental_setup_c0856a.md\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/experimental_setup.md\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/discussion_conclusion_draft.md\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/related_work_expanded.md\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/results.md\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/results_section_draft.md\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/cross_env_results.md\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/results_seed3_patch.md\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/intermediate/paper_numbers_update_draft.md\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/intermediate/civo_detector_implementation.md\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/intermediate/CHANGES.md",
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

_source line 41_

<details open><summary>🔧 Tool call — Bash · `toolu_01NxJWgw8x2amz1ecNyKntc4`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts -type f -name \"*rebuttal*\" -o -name \"*qa*\" 2>/dev/null",
  "description": "Find rebuttal QA files in artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ae813a79-db9f-4a12-b6ee-ad91ade39065",
  "uuid": "3b20f180-ab99-43aa-bbaa-6ea0c49d8038",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RLSMgN898yfxd4rT84C8UW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1784,
      "cache_read_input_tokens": 29620,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1784
      },
      "output_tokens": 61,
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

_source line 42 · 2026-05-25T14:12:05.903Z_

<details><summary>↩ Tool result · `toolu_01NxJWgw8x2amz1ecNyKntc4`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/report/rebuttal_prep.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/report/rebuttal_draft.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/rebuttal_prep.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/rebuttal_draft.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ae813a79-db9f-4a12-b6ee-ad91ade39065",
  "uuid": "4b5a2d29-7e84-4f20-895c-8b97ccc72499",
  "tool_use_result": {
    "stdout": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/report/rebuttal_prep.md\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/report/rebuttal_draft.md\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/rebuttal_prep.md\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/rebuttal_draft.md",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Assistant

_source line 43_

<details><summary>Logged reasoning block</summary>

```text
Let me check the recent worker log that was about rebuttal QA update, and also check rebuttal_draft.md which is likely what contains the Q&A.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ae813a79-db9f-4a12-b6ee-ad91ade39065",
  "uuid": "3f0a2913-537a-4ad8-acae-104a7ab6adf8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RHRM1eC2nSmoEyAf93bNMS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 316,
      "cache_read_input_tokens": 31404,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 316
      },
      "output_tokens": 10,
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

_source line 44_

<details open><summary>🔧 Tool call — Read · `toolu_01K5ufGm5ZVXndipze4hKxKd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/rebuttal_draft.md",
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ae813a79-db9f-4a12-b6ee-ad91ade39065",
  "uuid": "c7ce5035-0a0e-4089-b09f-d640b145f61c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RHRM1eC2nSmoEyAf93bNMS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 316,
      "cache_read_input_tokens": 31404,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 316
      },
      "output_tokens": 10,
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

_source line 45 · 2026-05-25T14:12:10.601Z_

<details><summary>↩ Tool result · `toolu_01K5ufGm5ZVXndipze4hKxKd`</summary>

```text
1	# Rebuttal Response Draft — Round 1
2	
3	**Paper**: "Why Temporal Abstraction Fails in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3"
4	**Venue**: CoRL 2026
5	**Date**: 2026-05-22
6	**Status**: Draft framework — pending exp_040-043 final data
7	
8	---
9	
10	## Critical Issues
11	
12	### [W-C1] CoRL Venue Fit 严重不足
13	**Reviewer 原文摘要**: 全文仅在 DMC Walker Walk 上实验，无 robotics benchmark、无 real-robot、无 robotics motivation。不满足 CoRL CFP "focus on a core robotics problem" 要求，存在 desk reject 风险。
14	
15	**回复要点**:
16	- 已增加 PickCube-v1 (ManiSkill2) 作为 preliminary manipulation evidence（注意：仅 2 experiments — 1 CIVO trigger + 1 baseline，且 CIVO 行为在 PickCube 上是 transient/self-correcting，与 Walker/Cheetah 的持续性 CIVO 不同，这是 scope limitation）
17	- Introduction 已重写，增加 robotics motivation：temporal abstraction 对 robot learning 的重要性（DayDreamer 的 real-robot world-model RL、TD-MPC2 的 manipulation 成功案例）
18	- 新增 "Implications for Robot Learning" 段落，讨论 CIVO 对 real-world robot deployment 的风险（想象训练中的 value overestimation 导致 sim-to-real 不可靠）
19	- 引用 DayDreamer (Wu et al., 2023) 和 TD-MPC2 (Hansen et al., 2024) 建立 world-model RL 在 robotics 中的实际应用基础
20	
21	**证据**:
22	- exp_019b_civo_trigger (PickCube-v1): NVE peak 3.78 @52.5K, eval 26.6 vs baseline 58.6 (−55%)。CIVO 在 manipulation 环境中同样触发（transient, self-correcting at current scale）
23	- exp_019a_v2_pickcube_baseline: eval 69.43, 建立 healthy baseline
24	- exp_036_dual_critic_pickcube: dual-critic 在 PickCube 上 NVE 2.3（自修正），eval 27.7 — PickCube 不触发持续性 CIVO，作为 scope limitation 讨论
25	- 跨环境 CIVO 行为差异本身是发现：Walker (moderate, NVE 1.5-4.8), Cheetah (severe, NVE 8-70), PickCube (transient, self-correcting)
26	
27	**论文修改位置**: Section 1 (Introduction rewrite), Section 3.1 (PickCube environment description), Section 5 (PickCube results), Section 7 (Implications for Robot Learning)
28	
29	---
30	
31	### [W-C2] 统计检验力严重不足
32	**Reviewer 原文摘要**: 核心因果声明依赖 n=2 per group。"4/4 separating power" P=1/16≈6.25%，未达 p<0.05。频繁使用 "causal factor"、"triggers" 等措辞与 n=2 证据强度不匹配。
33	
34	**回复要点**:
35	- 样本量已从原始 n=8 扩展至 **n=29**（包含 Walker 13, Cheetah 5, PickCube 2, SGS/intervention experiments 9）
36	- 全样本 AUROC = **0.953** (95% Bootstrap CI: [0.867, 1.000])，精度 89.7% (26/29)，recall 100% (12/12 CIVO 全部检出)
37	- LOEO cross-validation mean AUROC = **0.981**，held-out accuracy = 0.974（详见 W-C4）
38	- Youden-optimal threshold (1.53×) 独立收敛到预设 1.5×
39	- 因果语言已全面弱化："causal factor" → "strongly associated factor"；"triggers" → "is associated with"；"necessary and sufficient" → 删除。保留 "causal direction" 仅用于描述 factorial ablation 设计意图
40	- IQM 报告已采用 Agarwal et al. (2021) 推荐方式
41	
42	**证据**:
43	- n=29 AUROC analysis: AUROC 0.953, 95% CI [0.867, 1.000]
44	  - TP=12, FP=3, FN=0, TN=14
45	  - 3 FPs 均为机制不同的非 CIVO 高 NVE：025_obs_sgs_s2 (SGS damage), 028_rave_ceil15 (EMA pollution), 008e_v3_s2 (IRD, eval-driven)
46	- artifact: `auroc_label_fix_report.md` — 标签一致性修复详情
47	- artifact: `nve_loeo_crossval_report.md` — 交叉验证完整报告
48	- Walker factorial experiments: exp_008d (4 seeds: s1 collapse, s2 self-correct, s3 late-onset, s4 collapse), exp_008f (4 seeds: s1-s4 all NVE<1.5), exp_008a (3 seeds: all NVE<1.0)
49	- Cheetah: exp_010b (2 seeds: s0 NVE=70.64, s1 NVE=8.27), exp_008a_cheetah (2 seeds: s0 NVE=0.49, s1 NVE=0.48)
50	- exp_042_frozen_dt_emb_walker: data pending, expected 5/23 — 补充 trained vs frozen vs removed 三向对比
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ae813a79-db9f-4a12-b6ee-ad91ade39065",
  "uuid": "f3c6e5b7-00db-48e9-a927-7f0ec472a5ce",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/rebuttal_draft.md",
      "content": "# Rebuttal Response Draft — Round 1\n\n**Paper**: \"Why Temporal Abstraction Fails in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3\"\n**Venue**: CoRL 2026\n**Date**: 2026-05-22\n**Status**: Draft framework — pending exp_040-043 final data\n\n---\n\n## Critical Issues\n\n### [W-C1] CoRL Venue Fit 严重不足\n**Reviewer 原文摘要**: 全文仅在 DMC Walker Walk 上实验，无 robotics benchmark、无 real-robot、无 robotics motivation。不满足 CoRL CFP \"focus on a core robotics problem\" 要求，存在 desk reject 风险。\n\n**回复要点**:\n- 已增加 PickCube-v1 (ManiSkill2) 作为 preliminary manipulation evidence（注意：仅 2 experiments — 1 CIVO trigger + 1 baseline，且 CIVO 行为在 PickCube 上是 transient/self-correcting，与 Walker/Cheetah 的持续性 CIVO 不同，这是 scope limitation）\n- Introduction 已重写，增加 robotics motivation：temporal abstraction 对 robot learning 的重要性（DayDreamer 的 real-robot world-model RL、TD-MPC2 的 manipulation 成功案例）\n- 新增 \"Implications for Robot Learning\" 段落，讨论 CIVO 对 real-world robot deployment 的风险（想象训练中的 value overestimation 导致 sim-to-real 不可靠）\n- 引用 DayDreamer (Wu et al., 2023) 和 TD-MPC2 (Hansen et al., 2024) 建立 world-model RL 在 robotics 中的实际应用基础\n\n**证据**:\n- exp_019b_civo_trigger (PickCube-v1): NVE peak 3.78 @52.5K, eval 26.6 vs baseline 58.6 (−55%)。CIVO 在 manipulation 环境中同样触发（transient, self-correcting at current scale）\n- exp_019a_v2_pickcube_baseline: eval 69.43, 建立 healthy baseline\n- exp_036_dual_critic_pickcube: dual-critic 在 PickCube 上 NVE 2.3（自修正），eval 27.7 — PickCube 不触发持续性 CIVO，作为 scope limitation 讨论\n- 跨环境 CIVO 行为差异本身是发现：Walker (moderate, NVE 1.5-4.8), Cheetah (severe, NVE 8-70), PickCube (transient, self-correcting)\n\n**论文修改位置**: Section 1 (Introduction rewrite), Section 3.1 (PickCube environment description), Section 5 (PickCube results), Section 7 (Implications for Robot Learning)\n\n---\n\n### [W-C2] 统计检验力严重不足\n**Reviewer 原文摘要**: 核心因果声明依赖 n=2 per group。\"4/4 separating power\" P=1/16≈6.25%，未达 p<0.05。频繁使用 \"causal factor\"、\"triggers\" 等措辞与 n=2 证据强度不匹配。\n\n**回复要点**:\n- 样本量已从原始 n=8 扩展至 **n=29**（包含 Walker 13, Cheetah 5, PickCube 2, SGS/intervention experiments 9）\n- 全样本 AUROC = **0.953** (95% Bootstrap CI: [0.867, 1.000])，精度 89.7% (26/29)，recall 100% (12/12 CIVO 全部检出)\n- LOEO cross-validation mean AUROC = **0.981**，held-out accuracy = 0.974（详见 W-C4）\n- Youden-optimal threshold (1.53×) 独立收敛到预设 1.5×\n- 因果语言已全面弱化：\"causal factor\" → \"strongly associated factor\"；\"triggers\" → \"is associated with\"；\"necessary and sufficient\" → 删除。保留 \"causal direction\" 仅用于描述 factorial ablation 设计意图\n- IQM 报告已采用 Agarwal et al. (2021) 推荐方式\n\n**证据**:\n- n=29 AUROC analysis: AUROC 0.953, 95% CI [0.867, 1.000]\n  - TP=12, FP=3, FN=0, TN=14\n  - 3 FPs 均为机制不同的非 CIVO 高 NVE：025_obs_sgs_s2 (SGS damage), 028_rave_ceil15 (EMA pollution), 008e_v3_s2 (IRD, eval-driven)\n- artifact: `auroc_label_fix_report.md` — 标签一致性修复详情\n- artifact: `nve_loeo_crossval_report.md` — 交叉验证完整报告\n- Walker factorial experiments: exp_008d (4 seeds: s1 collapse, s2 self-correct, s3 late-onset, s4 collapse), exp_008f (4 seeds: s1-s4 all NVE<1.5), exp_008a (3 seeds: all NVE<1.0)\n- Cheetah: exp_010b (2 seeds: s0 NVE=70.64, s1 NVE=8.27), exp_008a_cheetah (2 seeds: s0 NVE=0.49, s1 NVE=0.48)\n- exp_042_frozen_dt_emb_walker: data pending, expected 5/23 — 补充 trained vs frozen vs removed 三向对比",
      "numLines": 50,
      "startLine": 1,
      "totalLines": 420
    }
  }
}
```

</details>

---


### Tool call

_source line 46_

<details open><summary>🔧 Tool call — Read · `toolu_01Bb2jQgStRrZTuVg3Dt7Ad5`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/rebuttal_prep.md",
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ae813a79-db9f-4a12-b6ee-ad91ade39065",
  "uuid": "41d54422-4c9e-4ba0-993b-5cb622416d58",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RHRM1eC2nSmoEyAf93bNMS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 316,
      "cache_read_input_tokens": 31404,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 316
      },
      "output_tokens": 10,
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

_source line 47 · 2026-05-25T14:12:10.620Z_

<details><summary>↩ Tool result · `toolu_01Bb2jQgStRrZTuVg3Dt7Ad5`</summary>

```text
1	# Anticipated Reviewer Q&A — ICML 2026
2	
3	## Q1: Frozen dt_emb prevention rate is only 71% (5/7) — is this reliable enough as a diagnostic?
4	
5	**Anticipated question**: "Your frozen dt_emb only prevents NVE>1.5× in 5 of 7 seeds (71%). How can you claim it's a reliable diagnostic tool when it fails 29% of the time?"
6	
7	**Response**: The 71% figure counts *any* NVE>1.5× exceedance, including transient spikes that self-correct. The operationally relevant metric is *sustained* CIVO: 0/7 frozen seeds exhibit sustained CIVO (defined as NVE≥1.5× persisting over a ≥35K-step window). The 2/7 transient exceedances self-corrected within training — one Walker seed peaked at NVE 1.71 before returning to 0.56, another at 1.88→0.177. By contrast, all trained dt_emb seeds in the original validation exceeded NVE>1.5× (2/2 Walker trained seeds: 008d NVE 2.09×, 009b NVE 1.62×), and additional seeds (s3/s4/s5) confirm CIVO triggering across seeds. This yields sensitivity=1.0 and specificity=1.0 for the sustained-CIVO criterion in the original 4-experiment validation (2 trained + 2 removed). The transient exceedances actually *strengthen* the diagnostic: they demonstrate the system's self-corrective capacity when the trained-dt_emb amplification loop is absent.
8	
9	**Evidence**: Frozen locomotion — Walker s0 NVE 0.19, s1 NVE 1.71→0.56 (transient), s2 NVE 1.88→0.177 (transient); Cheetah s0 NVE 1.35, s1 NVE 0.78 (no CIVO). Trained locomotion — original validation 2/2 Walker trained seeds exceed NVE>1.5× (008d NVE 2.09×, 009b NVE 1.62×); additional seeds s3/s4/s5 all trigger CIVO (NVE 1.53–4.84×). Fisher exact test p=0.003 for three-way causal (trained/frozen/removed).
10	
11	---
12	
13	## Q2: Manipulation 0/5 CIVO — how do you know dt_emb-dependent CIVO doesn't exist there?
14	
15	**Anticipated question**: "You found 0/5 dt_emb-dependent CIVO in manipulation tasks. How can you distinguish 'CIVO doesn't exist here' from 'your protocol failed to detect it'? PegInsertion showed ve_ratio bursts — isn't that CIVO?"
16	
17	**Response**: The PegInsertion ve_ratio bursts are environment-driven transients, not dt_emb-dependent CIVO. Our evidence is a paired seed ordering reversal: frozen s1 peaked at 11.32 while trained s1 peaked at only 3.08 — the opposite of what dt_emb-dependent CIVO predicts. In s0 the ordering was as expected (trained 10.05 > frozen 1.82), but the reversal in s1 falsifies dt_emb causality (D146). Additionally, PickCube showed NVE self-correction to 0.2 regardless of dt_emb configuration. We interpret this as a genuine domain boundary: manipulation tasks have shorter effective horizons and dense reward shaping, reducing the temporal-gap prediction errors that drive CIVO in locomotion. We report this as a scope limitation, not a negative result.
18	
19	**Evidence**: D146 ordering reversal — exp_055 trained s1 peak 3.08, exp_056 frozen s1 peak 11.32 (frozen > trained). exp_050 trained s0 peak 10.05, exp_053 frozen s0 回落到 1.82. PickCube: NVE self-corrects to 0.2 in all configs (trained/frozen/dual-critic). 0/5 manipulation seeds show trained > frozen ordering consistently.
20	
21	---
22	
23	## Q3: All results are from DreamerV3 — how does this generalize to other MBRL algorithms?
24	
25	**Anticipated question**: "Your findings are limited to a single algorithm (DreamerV3) with a specific architecture (RSSM). Why should the community care if CIVO doesn't generalize beyond this one system?"
26	
27	**Response**: We deliberately scope claims to DreamerV3 and make the scope explicit. However, the *mechanism* — temporal conditioning amplifying world-model prediction errors into value overestimation via imagination-based critic bootstrapping — applies to any MBRL system that (a) uses learned temporal conditioning, (b) trains critics on imagined trajectories, and (c) has latent dynamics with temporal-gap fidelity degradation. The strongest generalization evidence is the MPC/imagination boundary: TAWM (Nhu et al., ICML 2025) successfully uses dt-conditioning in TD-MPC2 (MPC setting) because MPC re-plans from real states each step, breaking the bootstrapping feedback loop. This architectural contrast localizes CIVO to imagination-based actor-critic — not just DreamerV3, but the entire class. The gradient-causality dissociation finding (gradient magnitude ≠ causal importance) is architecture-agnostic and relevant to any multi-head MBRL system.
28	
29	**Evidence**: TAWM succeeds with dt-conditioning in MPC (re-planning from real states), fails in imagination (critic bootstrapping). Gradient decomposition: reward head 38–49% gradient share but causally irrelevant; obs decoder 16–22% but causally critical — this dissociation is a general methodological insight for multi-loss MBRL debugging.
30	
31	---
32	
33	## Q4: Only 2 locomotion environments — is n=2 sufficient to support the claims?
34	
35	**Anticipated question**: "Walker and Cheetah are both simple locomotion tasks from DeepMind Control Suite. Two environments is far too few to make general claims about CIVO."
36	
37	**Response**: Walker and Cheetah are chosen to represent qualitatively different CIVO regimes, not as a random sample. Walker exhibits moderate CIVO (NVE 2–5×) with self-correction capacity (170K steps to recover), while Cheetah exhibits extreme CIVO (NVE 8–70×) with irreversible damage (gate permanently collapsed, eval stuck at 23.4 after 300K steps). This severity continuum — not environment count — is the scientific contribution. The frozen diagnostic shows 100% prevention across both severity levels (5/5 locomotion seeds), and dual-critic shows environment-dependent efficacy (prevention in Walker, partial mitigation in Cheetah), revealing that intervention effectiveness scales with CIVO severity. Additionally, 3 ManiSkill manipulation tasks (PickCube, PegInsertion, StackCube) establish the domain boundary where CIVO does not trigger. Total: 5 environments, 133 experiments, 63 successful.
38	
39	**Evidence**: Walker moderate — exp_045 self-correction eval 35→868 over 170K steps. Cheetah extreme — exp_048 irreversible eval 23.4, NVE 2.75, gate permanently collapsed @300K. Severity continuum confirmed across dual-critic (Walker 2/2 prevented vs Cheetah partial), TCN (Walker 2/4 vs Cheetah 0/3), and frozen (both 100%). ManiSkill 3 tasks × 5 seeds = 0 dt_emb-dependent CIVO.
40	
41	---
42	
43	## Q5: Why not compare interventions head-to-head (e.g., TCN vs frozen vs dual-critic)?
44	
45	**Anticipated question**: "You test seven interventions but never compare them against each other on the same seeds. Without controlled head-to-head comparison, how can you rank the Intervention Hierarchy levels?"
46	
47	**Response**: The Intervention Hierarchy is ranked by success rate across all tested seeds, not by paired comparison — this is deliberate. The success rates are so disparate that head-to-head pairing adds no discriminative power: gradient-level SGS 1/11 (9%), output-level RAVE 0/2 (0%), representation-level TCN 4/11 (36%), architecture-level dual-critic 3/8 (38%), vs embedding removal 5/5 (100%). The hierarchy's contribution is taxonomic: it organizes methods into four mechanistic levels and demonstrates that each level fails for a *distinct* reason — gradient stopping fails because forward-pass representational damage is irreducible, RAVE fails because the EMA anchor is polluted by early overestimation, TCN fails because effective dose is environment-dependent with no universal Goldilocks zone, and architecture-level interventions (dual-critic) partially succeed in moderate-CIVO environments but fail in severe ones. A head-to-head comparison on matched seeds would confirm what aggregate rates already show, at the cost of doubling GPU budget with no new mechanistic insight.
48	
49	**Evidence**: Intervention Hierarchy table — L1 Gradient: Full SGS 0/3, Obs-decoder SGS 1/6, Reward SGS 0/2 (1/11). L2 Output: RAVE 0/2. L3 Representation: TCN 4/11 (σ=0.1 1/1 borderline NVE=1.02×, σ=0.2 2/6 Walker only 45–91% eval retention, σ=0.5 0/3, σ=1.0 1/1 pyrrhic). L4 Architecture: Wide dual 3/4, Narrow dual 0/2, Wide single 0/2 (3/8). Control: dt_emb removal 5/5. Total: 8/32 interventions succeed vs 5/5 removal. Cheetah "impossible dose" (exp_030c): σ=1.0 prevents CIVO (NVE≤0.30) but eval degrades 372→47 — no viable operating point exists.
50	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ae813a79-db9f-4a12-b6ee-ad91ade39065",
  "uuid": "78a2bc4e-5eac-4726-956a-d1aa8695ae8b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/rebuttal_prep.md",
      "content": "# Anticipated Reviewer Q&A — ICML 2026\n\n## Q1: Frozen dt_emb prevention rate is only 71% (5/7) — is this reliable enough as a diagnostic?\n\n**Anticipated question**: \"Your frozen dt_emb only prevents NVE>1.5× in 5 of 7 seeds (71%). How can you claim it's a reliable diagnostic tool when it fails 29% of the time?\"\n\n**Response**: The 71% figure counts *any* NVE>1.5× exceedance, including transient spikes that self-correct. The operationally relevant metric is *sustained* CIVO: 0/7 frozen seeds exhibit sustained CIVO (defined as NVE≥1.5× persisting over a ≥35K-step window). The 2/7 transient exceedances self-corrected within training — one Walker seed peaked at NVE 1.71 before returning to 0.56, another at 1.88→0.177. By contrast, all trained dt_emb seeds in the original validation exceeded NVE>1.5× (2/2 Walker trained seeds: 008d NVE 2.09×, 009b NVE 1.62×), and additional seeds (s3/s4/s5) confirm CIVO triggering across seeds. This yields sensitivity=1.0 and specificity=1.0 for the sustained-CIVO criterion in the original 4-experiment validation (2 trained + 2 removed). The transient exceedances actually *strengthen* the diagnostic: they demonstrate the system's self-corrective capacity when the trained-dt_emb amplification loop is absent.\n\n**Evidence**: Frozen locomotion — Walker s0 NVE 0.19, s1 NVE 1.71→0.56 (transient), s2 NVE 1.88→0.177 (transient); Cheetah s0 NVE 1.35, s1 NVE 0.78 (no CIVO). Trained locomotion — original validation 2/2 Walker trained seeds exceed NVE>1.5× (008d NVE 2.09×, 009b NVE 1.62×); additional seeds s3/s4/s5 all trigger CIVO (NVE 1.53–4.84×). Fisher exact test p=0.003 for three-way causal (trained/frozen/removed).\n\n---\n\n## Q2: Manipulation 0/5 CIVO — how do you know dt_emb-dependent CIVO doesn't exist there?\n\n**Anticipated question**: \"You found 0/5 dt_emb-dependent CIVO in manipulation tasks. How can you distinguish 'CIVO doesn't exist here' from 'your protocol failed to detect it'? PegInsertion showed ve_ratio bursts — isn't that CIVO?\"\n\n**Response**: The PegInsertion ve_ratio bursts are environment-driven transients, not dt_emb-dependent CIVO. Our evidence is a paired seed ordering reversal: frozen s1 peaked at 11.32 while trained s1 peaked at only 3.08 — the opposite of what dt_emb-dependent CIVO predicts. In s0 the ordering was as expected (trained 10.05 > frozen 1.82), but the reversal in s1 falsifies dt_emb causality (D146). Additionally, PickCube showed NVE self-correction to 0.2 regardless of dt_emb configuration. We interpret this as a genuine domain boundary: manipulation tasks have shorter effective horizons and dense reward shaping, reducing the temporal-gap prediction errors that drive CIVO in locomotion. We report this as a scope limitation, not a negative result.\n\n**Evidence**: D146 ordering reversal — exp_055 trained s1 peak 3.08, exp_056 frozen s1 peak 11.32 (frozen > trained). exp_050 trained s0 peak 10.05, exp_053 frozen s0 回落到 1.82. PickCube: NVE self-corrects to 0.2 in all configs (trained/frozen/dual-critic). 0/5 manipulation seeds show trained > frozen ordering consistently.\n\n---\n\n## Q3: All results are from DreamerV3 — how does this generalize to other MBRL algorithms?\n\n**Anticipated question**: \"Your findings are limited to a single algorithm (DreamerV3) with a specific architecture (RSSM). Why should the community care if CIVO doesn't generalize beyond this one system?\"\n\n**Response**: We deliberately scope claims to DreamerV3 and make the scope explicit. However, the *mechanism* — temporal conditioning amplifying world-model prediction errors into value overestimation via imagination-based critic bootstrapping — applies to any MBRL system that (a) uses learned temporal conditioning, (b) trains critics on imagined trajectories, and (c) has latent dynamics with temporal-gap fidelity degradation. The strongest generalization evidence is the MPC/imagination boundary: TAWM (Nhu et al., ICML 2025) successfully uses dt-conditioning in TD-MPC2 (MPC setting) because MPC re-plans from real states each step, breaking the bootstrapping feedback loop. This architectural contrast localizes CIVO to imagination-based actor-critic — not just DreamerV3, but the entire class. The gradient-causality dissociation finding (gradient magnitude ≠ causal importance) is architecture-agnostic and relevant to any multi-head MBRL system.\n\n**Evidence**: TAWM succeeds with dt-conditioning in MPC (re-planning from real states), fails in imagination (critic bootstrapping). Gradient decomposition: reward head 38–49% gradient share but causally irrelevant; obs decoder 16–22% but causally critical — this dissociation is a general methodological insight for multi-loss MBRL debugging.\n\n---\n\n## Q4: Only 2 locomotion environments — is n=2 sufficient to support the claims?\n\n**Anticipated question**: \"Walker and Cheetah are both simple locomotion tasks from DeepMind Control Suite. Two environments is far too few to make general claims about CIVO.\"\n\n**Response**: Walker and Cheetah are chosen to represent qualitatively different CIVO regimes, not as a random sample. Walker exhibits moderate CIVO (NVE 2–5×) with self-correction capacity (170K steps to recover), while Cheetah exhibits extreme CIVO (NVE 8–70×) with irreversible damage (gate permanently collapsed, eval stuck at 23.4 after 300K steps). This severity continuum — not environment count — is the scientific contribution. The frozen diagnostic shows 100% prevention across both severity levels (5/5 locomotion seeds), and dual-critic shows environment-dependent efficacy (prevention in Walker, partial mitigation in Cheetah), revealing that intervention effectiveness scales with CIVO severity. Additionally, 3 ManiSkill manipulation tasks (PickCube, PegInsertion, StackCube) establish the domain boundary where CIVO does not trigger. Total: 5 environments, 133 experiments, 63 successful.\n\n**Evidence**: Walker moderate — exp_045 self-correction eval 35→868 over 170K steps. Cheetah extreme — exp_048 irreversible eval 23.4, NVE 2.75, gate permanently collapsed @300K. Severity continuum confirmed across dual-critic (Walker 2/2 prevented vs Cheetah partial), TCN (Walker 2/4 vs Cheetah 0/3), and frozen (both 100%). ManiSkill 3 tasks × 5 seeds = 0 dt_emb-dependent CIVO.\n\n---\n\n## Q5: Why not compare interventions head-to-head (e.g., TCN vs frozen vs dual-critic)?\n\n**Anticipated question**: \"You test seven interventions but never compare them against each other on the same seeds. Without controlled head-to-head comparison, how can you rank the Intervention Hierarchy levels?\"\n\n**Response**: The Intervention Hierarchy is ranked by success rate across all tested seeds, not by paired comparison — this is deliberate. The success rates are so disparate that head-to-head pairing adds no discriminative power: gradient-level SGS 1/11 (9%), output-level RAVE 0/2 (0%), representation-level TCN 4/11 (36%), architecture-level dual-critic 3/8 (38%), vs embedding removal 5/5 (100%). The hierarchy's contribution is taxonomic: it organizes methods into four mechanistic levels and demonstrates that each level fails for a *distinct* reason — gradient stopping fails because forward-pass representational damage is irreducible, RAVE fails because the EMA anchor is polluted by early overestimation, TCN fails because effective dose is environment-dependent with no universal Goldilocks zone, and architecture-level interventions (dual-critic) partially succeed in moderate-CIVO environments but fail in severe ones. A head-to-head comparison on matched seeds would confirm what aggregate rates already show, at the cost of doubling GPU budget with no new mechanistic insight.\n\n**Evidence**: Intervention Hierarchy table — L1 Gradient: Full SGS 0/3, Obs-decoder SGS 1/6, Reward SGS 0/2 (1/11). L2 Output: RAVE 0/2. L3 Representation: TCN 4/11 (σ=0.1 1/1 borderline NVE=1.02×, σ=0.2 2/6 Walker only 45–91% eval retention, σ=0.5 0/3, σ=1.0 1/1 pyrrhic). L4 Architecture: Wide dual 3/4, Narrow dual 0/2, Wide single 0/2 (3/8). Control: dt_emb removal 5/5. Total: 8/32 interventions succeed vs 5/5 removal. Cheetah \"impossible dose\" (exp_030c): σ=1.0 prevents CIVO (NVE≤0.30) but eval degrades 372→47 — no viable operating point exists.\n",
      "numLines": 50,
      "startLine": 1,
      "totalLines": 150
    }
  }
}
```

</details>

---


### Assistant

_source line 48_

<details><summary>Logged reasoning block</summary>

```text
The rebuttal Q&A is in `rebuttal_prep.md`. Let me read the full file to find all the Q&A entries I need to update (Q4, Q6, Q7, Q10, Q14, Q15).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ae813a79-db9f-4a12-b6ee-ad91ade39065",
  "uuid": "1f93e2c4-1c87-4804-994d-e3414da1d1b4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014tU1kDV6WLPhAE6PpfxFKL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4662,
      "cache_read_input_tokens": 31720,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4662
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

_source line 49_

Found it — the Q&A is in `rebuttal_prep.md`. Let me read the rest of the file to find Q6, Q7, Q10, Q14, Q15.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ae813a79-db9f-4a12-b6ee-ad91ade39065",
  "uuid": "8d977a72-627f-43df-90ab-44cfc2b337c0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014tU1kDV6WLPhAE6PpfxFKL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4662,
      "cache_read_input_tokens": 31720,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4662
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

_source line 50_

<details open><summary>🔧 Tool call — Read · `toolu_012i3xa842cgokmNKSKjXMdv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/rebuttal_prep.md",
  "offset": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ae813a79-db9f-4a12-b6ee-ad91ade39065",
  "uuid": "04ce8de5-1683-4764-8dbe-46c9139ee57f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014tU1kDV6WLPhAE6PpfxFKL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4662,
      "cache_read_input_tokens": 31720,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4662
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


### Tool result

_source line 51 · 2026-05-25T14:12:19.485Z_

<details><summary>↩ Tool result · `toolu_012i3xa842cgokmNKSKjXMdv`</summary>

```text
50	
51	---
52	
53	## Q6: NVE 1.5× threshold — is this arbitrary? How sensitive are claims to this cutoff?
54	
55	**Anticipated question**: "Your entire diagnostic framework relies on the 1.5× NVE threshold. How was it chosen, and do your claims hold under different thresholds?"
56	
57	**Response**: The 1.5× threshold was not hand-tuned — it emerges from ROC analysis. Across 30 labeled data points (4 environments, multiple configs), Youden-optimal threshold is 1.53×, independently converging on our pre-specified 1.5×. LOEO (Leave-One-Environment-Out) cross-validation across Walker (n=15), Cheetah (n=5), and PickCube (n=2) yields mean AUROC 0.988 and mean accuracy 0.978, demonstrating robust separating power. The threshold falls within the optimal accuracy range for all three training folds. Claims are stable across a range: at 1.3× the only change is 2 additional borderline transients reclassified (no sustained CIVO misses); at 2.0× we lose early detection of moderate Walker CIVO but severe cases remain captured. The threshold's utility is as a *diagnostic alarm*, not a mechanistic boundary — sustained NVE>1.5× across consecutive checkpoints indicates dt_emb-driven CIVO with zero false positives in our dataset. We acknowledge in-sample calibration and validation as a limitation and recommend held-out validation on other architectures.
58	
59	**Evidence**: In-sample AUROC 0.957 (n=30, 2 environments). LOEO cross-validated mean AUROC 0.988, mean accuracy 0.978 (3 folds: Walker/Cheetah/PickCube). Youden-optimal 1.53× vs pre-specified 1.5×. Trained dt_emb: original validation 2/2 Walker seeds exceed 1.5× (008d NVE 2.09×, 009b NVE 1.62×); additional seeds s3–s5 also trigger CIVO. Frozen: 0/5 locomotion sustained (2/7 total transient, self-corrected). Removed: 0/4 exceed 1.5×. 4/4 perfect separation in the original 2-seed validation (008d+009b vs 008f+009c).
60	
61	---
62	
63	## Q7: Sample sizes are small (n=2–4 per condition) — are conclusions statistically reliable?
64	
65	**Anticipated question**: "Most conditions have only 2–4 seeds. With such small samples, your results could be driven by lucky/unlucky initializations. Why not run 10+ seeds?"
66	
67	**Response**: We report 133 experiments across 63 successful conditions — the aggregate evidence base is substantial even if individual conditions have few seeds. Key claims rely on *perfect separation*, not effect sizes: trained dt_emb triggers CIVO in all tested Walker seeds (2/2 original validation, 3 additional seeds s3–s5), frozen prevents in 5/5 — Fisher exact test p=0.003. For the intervention hierarchy, the signal is overwhelming: removal succeeds 5/5 while all other interventions combined succeed 8/32. Where seed variance matters (e.g., TCN Walker σ=0.2: 2/4 seeds succeed), we report it transparently as evidence of unreliability, not as a positive result. We follow Agarwal et al. (2021) in reporting IQM with stratified bootstrap CIs rather than claiming significance from small n. The compute budget (~40 GPU-days total) was allocated to maximize mechanistic coverage (7 methods × 3 levels × 5 environments) over per-condition replication.
68	
69	**Evidence**: Aggregate: 133 experiments, 63 success, 35 negative. Per-condition: trained CIVO 2/2 original validation + 3 additional seeds all trigger, frozen 0/5 CIVO (locomotion), removal 5/5 prevention. Fisher p=0.003 for trained-vs-frozen-vs-removed three-way. TCN seed variance (45–91% eval retention at σ=0.2 Walker) reported as instability evidence. Dual-critic 2×2 factorial fully populated.
70	
71	---
72	
73	## Q8: CIVO onset is universal but outcomes diverge — does this weaken the CIVO threat narrative?
74	
75	**Anticipated question**: "You show 5/5 Walker trained seeds trigger CIVO onset (NVE>1.5×), but only some lead to collapse while others self-correct. If CIVO self-corrects in some seeds, is it really a problem worth diagnosing?"
76	
77	**Response**: The onset/outcome divergence actually *strengthens* the contribution. CIVO onset (NVE exceeding the 1.5× threshold under step-matched baseline normalization) is deterministic: 5/5 Walker trained seeds trigger it, 0/5 frozen seeds do, establishing dt_emb as the causal factor (Fisher exact p<0.01). The downstream *outcome* — whether onset progresses to irreversible collapse or self-corrects — is stochastic and seed-dependent, but overwhelmingly destructive: 6/7 locomotion seeds (86%) suffer irreversible policy collapse despite NVE sometimes self-correcting. Seed 5 exemplifies this dissociation: its NVE drops from 4.72× to 1.22× (critic error self-corrects), yet eval remains at 95.8 (10.5% of baseline) — the policy damage inflicted during the CIVO episode is permanent. This is the expected behavior of a feedback loop operating near a bifurcation point: the critic anomaly may resolve, but the policy has already been driven into a degenerate attractor from which it cannot escape. The practical implication is that CIVO onset is a *necessary precursor* to collapse and almost always sufficient — practitioners cannot rely on NVE self-correction to save the run. The frozen dt_emb diagnostic eliminates onset entirely (0/5 seeds), removing both collapse risk and the false hope of self-correction. This makes the diagnostic more valuable, not less: it prevents a near-deterministic catastrophic failure mode.
78	
79	**Evidence**: Walker trained seeds — 5/5 onset (NVE 1.53–4.72×), outcomes: s1 collapse (eval 83@105K), s2 self-correct (eval 268@105K — unique recovery), s3 late-onset collapse then slow recovery over 300K (exp_045 eval 868), s4 late-spike collapse (NVE 4.44@105K endpoint), s5 collapse† (NVE 4.72→1.22×, eval 95.8 = 10.5% baseline — NVE self-corrected but policy did not recover). Cheetah: 2/2 collapse. Total: 6/7 collapse, 1/7 self-correction (s2 only). Frozen: 0/5 onset. The 86% collapse rate underscores CIVO as a near-deterministic failure mode once onset occurs.
80	
81	---
82	
83	## Q9: Why only test on DreamerV3? Do other MBRL algorithms also exhibit CIVO?
84	
85	**Anticipated question**: "You only test CIVO in DreamerV3 with the RSSM architecture. This is a single algorithm — how do we know this isn't an artifact of DreamerV3's specific implementation rather than a general MBRL phenomenon? Have you tested TD-MPC2, IRIS, or other imagination-based methods?"
86	
87	**Response**: We deliberately position this work as the first systematic identification and analysis of CIVO *within DreamerV3*, not as a universal MBRL claim. However, the mechanism we identify — temporal conditioning amplifying world-model prediction errors into value overestimation via imagination-based critic bootstrapping — is not DreamerV3-specific. It requires three architectural conditions: (a) learned temporal conditioning on dynamics, (b) imagination-based critic training (value bootstrap over model-generated trajectories), and (c) temporal-gap fidelity degradation in the latent dynamics model. Any MBRL system satisfying all three is theoretically susceptible. The strongest generalization evidence comes from the MPC/imagination boundary: TAWM (Nhu et al., ICML 2025) successfully uses dt-conditioning in TD-MPC2's MPC setting because MPC re-plans from real states at each step, breaking the bootstrapping feedback loop that accumulates errors. This architectural contrast localizes CIVO to imagination-based actor-critic as a class — not DreamerV3 alone. Testing TD-MPC2 in imagination mode, IRIS, and TWM is explicit future work; our contribution is establishing the causal mechanism and diagnostic framework that enables such testing.
88	
89	**Evidence**: CIVO mechanism requires (a) + (b) + (c) jointly (§Discussion). TAWM succeeds with dt-conditioning in MPC (re-planning from real states) but would face CIVO risk in imagination mode — this is the MPC-immunity prediction (Appendix §MPC Immune). The RSSM develops a 2.78× reward prediction gap under trained conditioning (Table: RSSM fidelity). Gradient-causality dissociation (gradient magnitude ≠ causal importance) is architecture-agnostic — applicable to any multi-head MBRL system. The three-condition framework provides a concrete testable prediction for other architectures.
90	
91	---
92	
93	## Q10: Environment diversity is limited — only 2 DMC + 3 ManiSkill tasks
94	
95	**Anticipated question**: "Five environments (2 locomotion, 3 manipulation) is a narrow evaluation. The locomotion environments are both simple DMC tasks. How can you claim generalizability with such limited environment diversity?"
96	
97	**Response**: The five environments serve distinct roles in the experimental design, and the evidence base is not five independent data points but 133 experiments across 43 configurations. Walker and Cheetah represent qualitatively different CIVO severity regimes: Walker exhibits moderate CIVO (NVE 2–5×) with self-correction capacity (170K steps to recover), while Cheetah exhibits extreme CIVO (NVE 8–108×) with irreversible damage (gate permanently collapsed, eval stuck at 23.4 after 300K steps). This severity continuum is a scientific finding, not a limitation. The three ManiSkill environments (PickCube, PegInsertion, StackCube) serve as negative controls that establish the domain boundary where dt_emb-dependent CIVO does not trigger. Crucially, the negative controls are *informative*: the D146 ordering reversal in PegInsertion (frozen seed 1 spike 11.32 > trained seed 1 spike 3.08) falsifies dt_emb causality for manipulation-task value spikes, confirming these are environment-driven transients rather than undetected CIVO. Each environment contributes multiple configurations (frozen, trained, removed, dual-critic, TCN, SGS), yielding 133 total experiments — the statistical power comes from systematic interventional variation, not environment count.
98	
99	**Evidence**: Walker moderate CIVO — 5/5 onset, NVE 1.53–4.72×, IQM=148.8 (n=5). Cheetah extreme CIVO — 2/2 collapse, NVE 8.27–108.52×, eval 23.4–51.7. ManiSkill negative controls — 0/5 dt_emb-dependent CIVO: PickCube NVE self-corrects to 0.2 regardless of config; PegInsertion D146 ordering reversal (exp_055 trained s1 peak 3.08 < exp_056 frozen s1 peak 11.32); StackCube frozen control shows identical spike (4.30×) to trained (5.05×). Total: 5 environments × multiple configs = 133 experiments, 63 successful. Fisher exact p=0.003 for three-way causal test across environments.
100	
101	---
102	
103	## Q11: How does CIVO relate to overestimation bias in model-free methods (TD3/SAC)?
104	
105	**Anticipated question**: "Value overestimation is a well-studied problem in model-free RL — TD3 and SAC already address it with clipped double Q-learning. How is CIVO different from standard overestimation bias? Why don't existing model-free solutions (twin critics with min operation) work?"
106	
107	**Response**: CIVO is mechanistically distinct from model-free overestimation bias. In TD3/SAC, overestimation arises from function approximation error in the critic — the max operator over noisy Q-estimates introduces a positive bias. The twin-critic min operation effectively counters this because the two critics have independent approximation errors. In CIVO, overestimation arises from *world-model prediction errors compounding over imagined trajectories*, amplified by temporal conditioning. The causal chain is: trained dt_emb → biased temporal conditioning on world model → compounding prediction error over imagination horizon → systematically inflated value targets → actor exploitation of inflated values → further world-model distortion (feedback loop). The critical difference: in CIVO, both critics are trained on the *same* RSSM-generated imagination trajectories, so they share the same systematic bias. Empirically, dual critics in DreamerV3 converge to ρ > 0.999 correlation across all 7 tested configurations, with pessimism at only 3–4% of the independent-critic bound (§Architecture-Level Ablation). The min operation is thus ineffective against CIVO because it addresses *independent* estimation noise, not *shared* systematic bias from a corrupted generative model. This is precisely why CIVO requires model-level or embedding-level intervention rather than critic-level fixes.
108	
109	**Evidence**: Dual-critic convergence — ρ > 0.999 across n=7 configurations, pessimism 3–4% of independent-critic bound (§Architecture-Level Ablation). Wide dual-critic provides regularization through uncharacterized mechanisms (3/4 Walker prevention) but fails on Cheetah (0/1). RAVE (value-level capping, analogous to model-free solutions) also fails: 0/2 seeds, EMA anchor tracks biased values during CIVO onset. RSSM reward prediction gap: 2.78× under trained conditioning — this is the upstream bias that twin critics cannot correct. Embedding removal (5/5 prevention) confirms the fix must target the bias source, not the critic.
110	
111	---
112	
113	## Q12: Why doesn't CIVO appear in ManiSkill manipulation tasks?
114	
115	**Anticipated question**: "You claim CIVO is absent in manipulation (0/5 seeds), but you don't convincingly explain why. Is it reward structure? Observation modality? Dynamics? Without understanding the boundary conditions, the result is merely an observation, not a mechanistic finding."
116	
117	**Response**: We acknowledge that identifying the precise mediator of the locomotion/manipulation boundary is an open question, and we state this explicitly in §Discussion. What we *can* rule out is reward sparsity: all five environments (DMC and ManiSkill) use dense shaped rewards, so reward density cannot explain the boundary. We identify three candidate mediators that differ systematically between the domains. First, action-space periodicity: locomotion requires sustained periodic coordination (gait cycles), where temporal conditioning errors accumulate coherently; manipulation involves episodic, contact-gated dynamics where the relevant horizon resets at each contact transition. Second, observation structure: DMC locomotion uses low-dimensional proprioceptive states where the RSSM can develop spurious temporal shortcuts; ManiSkill uses richer state representations including object poses. Third, continuous vs. contact-gated dynamics: locomotion dynamics evolve continuously (smooth state transitions amenable to temporal extrapolation), while manipulation involves discrete contact mode switches that limit temporal prediction utility. The value of the negative result is diagnostic: the frozen-embedding diagnostic correctly identifies ManiSkill value spikes as non-CIVO (environment-driven transients), validating NVE as a domain-aware diagnostic that does not produce false positives in manipulation tasks.
118	
119	**Evidence**: All 5 environments use dense shaped rewards — reward sparsity ruled out (§Discussion). PegInsertion D146 ordering reversal falsifies dt_emb causality: frozen s1 peak 11.32 > trained s1 peak 3.08. PickCube NVE self-corrects to 0.2 regardless of dt_emb config (trained/frozen/dual-critic). StackCube frozen control spike 4.30× ≈ trained spike 5.05× — no trained > frozen ordering. Candidate mediators identified: action-space periodicity, observation structure, continuous vs. contact-gated dynamics (§Discussion). 0/5 manipulation false positives validates NVE diagnostic specificity across domains.
120	
121	---
122	
123	## Q13: All SGS variants fail — what does this tell us about the mechanism?
124	
125	**Anticipated question**: "You test three SGS variants and achieve only 1/11 CIVO prevention (9% success rate). If gradient stopping doesn't work at any level, does this mean dt_emb isn't actually the cause? Or is your intervention methodology flawed?"
126	
127	**Response**: The SGS failure is itself a mechanistic finding, not a methodological shortcoming. Gradient stopping addresses *backward-pass* gradient flow to the dt_emb, but CIVO operates through *forward-pass* representational conditioning. In the forward pass, the trained dt_emb conditions every RSSM transition step — this conditioning biases latent state representations regardless of whether gradients flow back through the embedding. SGS confirms that the vulnerability is irreducible at the gradient level: even blocking all non-KL gradients (Full-pathway SGS, 0/3 seeds) cannot prevent the representational damage that a trained, exposed dt_emb inflicts on world-model predictions. The gradient decomposition analysis reveals a deeper insight: gradient magnitude does not predict causal importance. The reward head contributes 38–49% of the total gradient to dt_emb but is causally irrelevant — blocking it alone (Reward-only SGS, 0/2) and including it (Full-SGS) yield the same failure. The observation decoder contributes only 16–22% but carries the critical signal: obs-decoder-only SGS achieves the sole 1/6 success. This dissociation between gradient share and causal importance is a general methodological contribution applicable to any multi-head architecture — it warns against using gradient magnitude as a proxy for causal influence in multi-loss systems.
128	
129	**Evidence**: SGS results — Reward-only SGS 0/2, Full-pathway SGS 0/3, Obs-decoder SGS 1/6 → total 1/11 (9%) (Table: Intervention Hierarchy). Gradient decomposition at exp_008d_55K: reward 49.0%, KL 34.7%, observation 16.3%, continuation 0.0%. At exp_009e_112K: reward 38.1%, KL 40.4%, observation 21.5%. Reward-detach condition (exp_044): CIVO onset not prevented (peak NVE 4.45×), delayed self-correction (eval 44→538 over 224K, 59% baseline) — lower asymptote than spontaneous recovery (exp_045: 868, 95%). Full-SGS exp_018: s1 partial mitigation (eval 448, NVE 1.66×), s2 collapse. The forward-pass conditioning mechanism explains why gradient-level intervention is fundamentally insufficient.
130	
131	---
132	
133	## Q14: Seed count per condition is too small — are the statistics reliable?
134	
135	**Anticipated question**: "Individual conditions have 1–4 seeds. Fisher's exact test on such small samples has limited power. Your p=0.003 relies on pooling across conditions. Isn't the 100% onset rate (7/7) just an artifact of not running enough seeds to see failures?"
136	
137	**Response**: The statistical argument rests on multiple independent lines of evidence that converge, not on any single small-sample comparison. First, the *perfect separation* between trained (7/7 onset) and frozen/removed (0/5 CIVO-free in locomotion) is the relevant test — Fisher exact p=0.003 for the three-way comparison (trained/frozen/removed). Second, the 7/7 onset figure combines two independent environments (Walker 5/5, Cheetah 2/2), each with distinct CIVO severity profiles, so environment-specific luck is unlikely. Third, the aggregate intervention evidence shows overwhelming separation: embedding removal succeeds 5/5 while all other interventions combined succeed 8/32 — this is not a borderline effect. Fourth, where seed variance matters, we report it transparently as instability evidence: TCN σ=0.2 Walker shows 2/4 success with eval retention ranging 45–91%, which we interpret as unreliability, not as a positive result. We follow Agarwal et al. (2021) in reporting IQM with stratified bootstrap CIs (IQM=148.8 for trained Walker, n=5) rather than claiming significance from small n. The compute budget (~40 GPU-days) was allocated to maximize mechanistic coverage (7 intervention types × 4 hierarchy levels × 5 environments) over per-condition replication — a deliberate design choice that prioritizes breadth of causal evidence over depth of per-condition statistics.
138	
139	**Evidence**: Three-way Fisher exact p=0.003: trained 7/7 onset vs. frozen 5/7 transient-only (0/7 sustained) vs. removed 0/5. Walker onset: 5/5 seeds (s1–s5), NVE 1.53–4.72×. Cheetah onset: 2/2 seeds, NVE 8.27–108.52×. IQM=148.8 (Walker trained, n=5; Agarwal et al. 2021). Intervention aggregate: removal 5/5 vs. others 8/32. Total evidence: 133 experiments, 63 successful, 35 negative across 43 configurations. TCN instability reported: σ=0.2 Walker s2 NVE 2.11× vs. s3 NVE 3.04× (late-onset CIVO). Dual-critic 2×2 factorial fully populated (4 cells, n=2 each).
140	
141	---
142	
143	## Q15: The NVE 1.5× threshold — how sensitive are your claims to this specific cutoff?
144	
145	**Anticipated question**: "You claim AUROC=0.957 for NVE-based CIVO detection, but this is in-sample on n=30. The threshold 1.5× seems like it could be overfit. What happens at 1.3× or 2.0×? Is there held-out validation?"
146	
147	**Response**: The 1.5× threshold was not post-hoc selected to maximize accuracy — it was pre-specified based on the initial factorial experiments and independently validated. Youden-optimal threshold from ROC analysis is 1.53×, converging on our pre-specified 1.5× without tuning. In-sample AUROC is 0.957 (27/30 correct, n=30 configurations across 2 environments). Critically, we perform Leave-One-Environment-Out (LOEO) cross-validation across Walker (n=15), Cheetah (n=5), and PickCube (n=2): the threshold falls within the optimal accuracy range for all three training folds, yielding mean held-out AUROC=0.988 and mean accuracy=0.978. The single cross-validation error is exp_008e_v3 seed 2 — an Imagination-Reality Divergence (IRD) collapse mechanistically distinct from CIVO, which produces one of only three non-CIVO false positives. Claims are stable across a wide threshold range: at 1.3× the only change is 2 additional borderline transients reclassified (no sustained CIVO misses); at 2.0× we lose early detection of moderate Walker CIVO but all severe cases remain captured. We acknowledge in-sample calibration as a limitation and recommend held-out validation on other MBRL architectures as future work.
148	
149	**Evidence**: In-sample AUROC=0.957, accuracy 27/30 (n=30, 2 environments). LOEO cross-validation (3 folds): PickCube held-out 2/2 accuracy, AUROC 1.000; Cheetah held-out 5/5 accuracy, AUROC 1.000; Walker held-out 14/15 accuracy, AUROC 0.963. Mean LOEO AUROC=0.988, mean accuracy=0.978. Youden-optimal threshold 1.53× — within 2% of pre-specified 1.5×. Optimal threshold range in training folds: (1.45, 1.53] when Walker available, (1.00, 3.78) when training on Cheetah+PickCube only. Three in-sample FPs: exp_025 obs-SGS s2 (NVE 1.54×, borderline), exp_028 RAVE ceil15 (NVE 1.52×, borderline), exp_008e_v3 s2 (IRD, mechanistically distinct). Threshold sensitivity: 1.3× adds 2 FPs, 2.0× misses moderate Walker onset — claims stable across [1.3×, 2.0×] range.
150	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ae813a79-db9f-4a12-b6ee-ad91ade39065",
  "uuid": "5785da8b-d9c2-41a7-9227-fbac49aa6779",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/rebuttal_prep.md",
      "content": "\n---\n\n## Q6: NVE 1.5× threshold — is this arbitrary? How sensitive are claims to this cutoff?\n\n**Anticipated question**: \"Your entire diagnostic framework relies on the 1.5× NVE threshold. How was it chosen, and do your claims hold under different thresholds?\"\n\n**Response**: The 1.5× threshold was not hand-tuned — it emerges from ROC analysis. Across 30 labeled data points (4 environments, multiple configs), Youden-optimal threshold is 1.53×, independently converging on our pre-specified 1.5×. LOEO (Leave-One-Environment-Out) cross-validation across Walker (n=15), Cheetah (n=5), and PickCube (n=2) yields mean AUROC 0.988 and mean accuracy 0.978, demonstrating robust separating power. The threshold falls within the optimal accuracy range for all three training folds. Claims are stable across a range: at 1.3× the only change is 2 additional borderline transients reclassified (no sustained CIVO misses); at 2.0× we lose early detection of moderate Walker CIVO but severe cases remain captured. The threshold's utility is as a *diagnostic alarm*, not a mechanistic boundary — sustained NVE>1.5× across consecutive checkpoints indicates dt_emb-driven CIVO with zero false positives in our dataset. We acknowledge in-sample calibration and validation as a limitation and recommend held-out validation on other architectures.\n\n**Evidence**: In-sample AUROC 0.957 (n=30, 2 environments). LOEO cross-validated mean AUROC 0.988, mean accuracy 0.978 (3 folds: Walker/Cheetah/PickCube). Youden-optimal 1.53× vs pre-specified 1.5×. Trained dt_emb: original validation 2/2 Walker seeds exceed 1.5× (008d NVE 2.09×, 009b NVE 1.62×); additional seeds s3–s5 also trigger CIVO. Frozen: 0/5 locomotion sustained (2/7 total transient, self-corrected). Removed: 0/4 exceed 1.5×. 4/4 perfect separation in the original 2-seed validation (008d+009b vs 008f+009c).\n\n---\n\n## Q7: Sample sizes are small (n=2–4 per condition) — are conclusions statistically reliable?\n\n**Anticipated question**: \"Most conditions have only 2–4 seeds. With such small samples, your results could be driven by lucky/unlucky initializations. Why not run 10+ seeds?\"\n\n**Response**: We report 133 experiments across 63 successful conditions — the aggregate evidence base is substantial even if individual conditions have few seeds. Key claims rely on *perfect separation*, not effect sizes: trained dt_emb triggers CIVO in all tested Walker seeds (2/2 original validation, 3 additional seeds s3–s5), frozen prevents in 5/5 — Fisher exact test p=0.003. For the intervention hierarchy, the signal is overwhelming: removal succeeds 5/5 while all other interventions combined succeed 8/32. Where seed variance matters (e.g., TCN Walker σ=0.2: 2/4 seeds succeed), we report it transparently as evidence of unreliability, not as a positive result. We follow Agarwal et al. (2021) in reporting IQM with stratified bootstrap CIs rather than claiming significance from small n. The compute budget (~40 GPU-days total) was allocated to maximize mechanistic coverage (7 methods × 3 levels × 5 environments) over per-condition replication.\n\n**Evidence**: Aggregate: 133 experiments, 63 success, 35 negative. Per-condition: trained CIVO 2/2 original validation + 3 additional seeds all trigger, frozen 0/5 CIVO (locomotion), removal 5/5 prevention. Fisher p=0.003 for trained-vs-frozen-vs-removed three-way. TCN seed variance (45–91% eval retention at σ=0.2 Walker) reported as instability evidence. Dual-critic 2×2 factorial fully populated.\n\n---\n\n## Q8: CIVO onset is universal but outcomes diverge — does this weaken the CIVO threat narrative?\n\n**Anticipated question**: \"You show 5/5 Walker trained seeds trigger CIVO onset (NVE>1.5×), but only some lead to collapse while others self-correct. If CIVO self-corrects in some seeds, is it really a problem worth diagnosing?\"\n\n**Response**: The onset/outcome divergence actually *strengthens* the contribution. CIVO onset (NVE exceeding the 1.5× threshold under step-matched baseline normalization) is deterministic: 5/5 Walker trained seeds trigger it, 0/5 frozen seeds do, establishing dt_emb as the causal factor (Fisher exact p<0.01). The downstream *outcome* — whether onset progresses to irreversible collapse or self-corrects — is stochastic and seed-dependent, but overwhelmingly destructive: 6/7 locomotion seeds (86%) suffer irreversible policy collapse despite NVE sometimes self-correcting. Seed 5 exemplifies this dissociation: its NVE drops from 4.72× to 1.22× (critic error self-corrects), yet eval remains at 95.8 (10.5% of baseline) — the policy damage inflicted during the CIVO episode is permanent. This is the expected behavior of a feedback loop operating near a bifurcation point: the critic anomaly may resolve, but the policy has already been driven into a degenerate attractor from which it cannot escape. The practical implication is that CIVO onset is a *necessary precursor* to collapse and almost always sufficient — practitioners cannot rely on NVE self-correction to save the run. The frozen dt_emb diagnostic eliminates onset entirely (0/5 seeds), removing both collapse risk and the false hope of self-correction. This makes the diagnostic more valuable, not less: it prevents a near-deterministic catastrophic failure mode.\n\n**Evidence**: Walker trained seeds — 5/5 onset (NVE 1.53–4.72×), outcomes: s1 collapse (eval 83@105K), s2 self-correct (eval 268@105K — unique recovery), s3 late-onset collapse then slow recovery over 300K (exp_045 eval 868), s4 late-spike collapse (NVE 4.44@105K endpoint), s5 collapse† (NVE 4.72→1.22×, eval 95.8 = 10.5% baseline — NVE self-corrected but policy did not recover). Cheetah: 2/2 collapse. Total: 6/7 collapse, 1/7 self-correction (s2 only). Frozen: 0/5 onset. The 86% collapse rate underscores CIVO as a near-deterministic failure mode once onset occurs.\n\n---\n\n## Q9: Why only test on DreamerV3? Do other MBRL algorithms also exhibit CIVO?\n\n**Anticipated question**: \"You only test CIVO in DreamerV3 with the RSSM architecture. This is a single algorithm — how do we know this isn't an artifact of DreamerV3's specific implementation rather than a general MBRL phenomenon? Have you tested TD-MPC2, IRIS, or other imagination-based methods?\"\n\n**Response**: We deliberately position this work as the first systematic identification and analysis of CIVO *within DreamerV3*, not as a universal MBRL claim. However, the mechanism we identify — temporal conditioning amplifying world-model prediction errors into value overestimation via imagination-based critic bootstrapping — is not DreamerV3-specific. It requires three architectural conditions: (a) learned temporal conditioning on dynamics, (b) imagination-based critic training (value bootstrap over model-generated trajectories), and (c) temporal-gap fidelity degradation in the latent dynamics model. Any MBRL system satisfying all three is theoretically susceptible. The strongest generalization evidence comes from the MPC/imagination boundary: TAWM (Nhu et al., ICML 2025) successfully uses dt-conditioning in TD-MPC2's MPC setting because MPC re-plans from real states at each step, breaking the bootstrapping feedback loop that accumulates errors. This architectural contrast localizes CIVO to imagination-based actor-critic as a class — not DreamerV3 alone. Testing TD-MPC2 in imagination mode, IRIS, and TWM is explicit future work; our contribution is establishing the causal mechanism and diagnostic framework that enables such testing.\n\n**Evidence**: CIVO mechanism requires (a) + (b) + (c) jointly (§Discussion). TAWM succeeds with dt-conditioning in MPC (re-planning from real states) but would face CIVO risk in imagination mode — this is the MPC-immunity prediction (Appendix §MPC Immune). The RSSM develops a 2.78× reward prediction gap under trained conditioning (Table: RSSM fidelity). Gradient-causality dissociation (gradient magnitude ≠ causal importance) is architecture-agnostic — applicable to any multi-head MBRL system. The three-condition framework provides a concrete testable prediction for other architectures.\n\n---\n\n## Q10: Environment diversity is limited — only 2 DMC + 3 ManiSkill tasks\n\n**Anticipated question**: \"Five environments (2 locomotion, 3 manipulation) is a narrow evaluation. The locomotion environments are both simple DMC tasks. How can you claim generalizability with such limited environment diversity?\"\n\n**Response**: The five environments serve distinct roles in the experimental design, and the evidence base is not five independent data points but 133 experiments across 43 configurations. Walker and Cheetah represent qualitatively different CIVO severity regimes: Walker exhibits moderate CIVO (NVE 2–5×) with self-correction capacity (170K steps to recover), while Cheetah exhibits extreme CIVO (NVE 8–108×) with irreversible damage (gate permanently collapsed, eval stuck at 23.4 after 300K steps). This severity continuum is a scientific finding, not a limitation. The three ManiSkill environments (PickCube, PegInsertion, StackCube) serve as negative controls that establish the domain boundary where dt_emb-dependent CIVO does not trigger. Crucially, the negative controls are *informative*: the D146 ordering reversal in PegInsertion (frozen seed 1 spike 11.32 > trained seed 1 spike 3.08) falsifies dt_emb causality for manipulation-task value spikes, confirming these are environment-driven transients rather than undetected CIVO. Each environment contributes multiple configurations (frozen, trained, removed, dual-critic, TCN, SGS), yielding 133 total experiments — the statistical power comes from systematic interventional variation, not environment count.\n\n**Evidence**: Walker moderate CIVO — 5/5 onset, NVE 1.53–4.72×, IQM=148.8 (n=5). Cheetah extreme CIVO — 2/2 collapse, NVE 8.27–108.52×, eval 23.4–51.7. ManiSkill negative controls — 0/5 dt_emb-dependent CIVO: PickCube NVE self-corrects to 0.2 regardless of config; PegInsertion D146 ordering reversal (exp_055 trained s1 peak 3.08 < exp_056 frozen s1 peak 11.32); StackCube frozen control shows identical spike (4.30×) to trained (5.05×). Total: 5 environments × multiple configs = 133 experiments, 63 successful. Fisher exact p=0.003 for three-way causal test across environments.\n\n---\n\n## Q11: How does CIVO relate to overestimation bias in model-free methods (TD3/SAC)?\n\n**Anticipated question**: \"Value overestimation is a well-studied problem in model-free RL — TD3 and SAC already address it with clipped double Q-learning. How is CIVO different from standard overestimation bias? Why don't existing model-free solutions (twin critics with min operation) work?\"\n\n**Response**: CIVO is mechanistically distinct from model-free overestimation bias. In TD3/SAC, overestimation arises from function approximation error in the critic — the max operator over noisy Q-estimates introduces a positive bias. The twin-critic min operation effectively counters this because the two critics have independent approximation errors. In CIVO, overestimation arises from *world-model prediction errors compounding over imagined trajectories*, amplified by temporal conditioning. The causal chain is: trained dt_emb → biased temporal conditioning on world model → compounding prediction error over imagination horizon → systematically inflated value targets → actor exploitation of inflated values → further world-model distortion (feedback loop). The critical difference: in CIVO, both critics are trained on the *same* RSSM-generated imagination trajectories, so they share the same systematic bias. Empirically, dual critics in DreamerV3 converge to ρ > 0.999 correlation across all 7 tested configurations, with pessimism at only 3–4% of the independent-critic bound (§Architecture-Level Ablation). The min operation is thus ineffective against CIVO because it addresses *independent* estimation noise, not *shared* systematic bias from a corrupted generative model. This is precisely why CIVO requires model-level or embedding-level intervention rather than critic-level fixes.\n\n**Evidence**: Dual-critic convergence — ρ > 0.999 across n=7 configurations, pessimism 3–4% of independent-critic bound (§Architecture-Level Ablation). Wide dual-critic provides regularization through uncharacterized mechanisms (3/4 Walker prevention) but fails on Cheetah (0/1). RAVE (value-level capping, analogous to model-free solutions) also fails: 0/2 seeds, EMA anchor tracks biased values during CIVO onset. RSSM reward prediction gap: 2.78× under trained conditioning — this is the upstream bias that twin critics cannot correct. Embedding removal (5/5 prevention) confirms the fix must target the bias source, not the critic.\n\n---\n\n## Q12: Why doesn't CIVO appear in ManiSkill manipulation tasks?\n\n**Anticipated question**: \"You claim CIVO is absent in manipulation (0/5 seeds), but you don't convincingly explain why. Is it reward structure? Observation modality? Dynamics? Without understanding the boundary conditions, the result is merely an observation, not a mechanistic finding.\"\n\n**Response**: We acknowledge that identifying the precise mediator of the locomotion/manipulation boundary is an open question, and we state this explicitly in §Discussion. What we *can* rule out is reward sparsity: all five environments (DMC and ManiSkill) use dense shaped rewards, so reward density cannot explain the boundary. We identify three candidate mediators that differ systematically between the domains. First, action-space periodicity: locomotion requires sustained periodic coordination (gait cycles), where temporal conditioning errors accumulate coherently; manipulation involves episodic, contact-gated dynamics where the relevant horizon resets at each contact transition. Second, observation structure: DMC locomotion uses low-dimensional proprioceptive states where the RSSM can develop spurious temporal shortcuts; ManiSkill uses richer state representations including object poses. Third, continuous vs. contact-gated dynamics: locomotion dynamics evolve continuously (smooth state transitions amenable to temporal extrapolation), while manipulation involves discrete contact mode switches that limit temporal prediction utility. The value of the negative result is diagnostic: the frozen-embedding diagnostic correctly identifies ManiSkill value spikes as non-CIVO (environment-driven transients), validating NVE as a domain-aware diagnostic that does not produce false positives in manipulation tasks.\n\n**Evidence**: All 5 environments use dense shaped rewards — reward sparsity ruled out (§Discussion). PegInsertion D146 ordering reversal falsifies dt_emb causality: frozen s1 peak 11.32 > trained s1 peak 3.08. PickCube NVE self-corrects to 0.2 regardless of dt_emb config (trained/frozen/dual-critic). StackCube frozen control spike 4.30× ≈ trained spike 5.05× — no trained > frozen ordering. Candidate mediators identified: action-space periodicity, observation structure, continuous vs. contact-gated dynamics (§Discussion). 0/5 manipulation false positives validates NVE diagnostic specificity across domains.\n\n---\n\n## Q13: All SGS variants fail — what does this tell us about the mechanism?\n\n**Anticipated question**: \"You test three SGS variants and achieve only 1/11 CIVO prevention (9% success rate). If gradient stopping doesn't work at any level, does this mean dt_emb isn't actually the cause? Or is your intervention methodology flawed?\"\n\n**Response**: The SGS failure is itself a mechanistic finding, not a methodological shortcoming. Gradient stopping addresses *backward-pass* gradient flow to the dt_emb, but CIVO operates through *forward-pass* representational conditioning. In the forward pass, the trained dt_emb conditions every RSSM transition step — this conditioning biases latent state representations regardless of whether gradients flow back through the embedding. SGS confirms that the vulnerability is irreducible at the gradient level: even blocking all non-KL gradients (Full-pathway SGS, 0/3 seeds) cannot prevent the representational damage that a trained, exposed dt_emb inflicts on world-model predictions. The gradient decomposition analysis reveals a deeper insight: gradient magnitude does not predict causal importance. The reward head contributes 38–49% of the total gradient to dt_emb but is causally irrelevant — blocking it alone (Reward-only SGS, 0/2) and including it (Full-SGS) yield the same failure. The observation decoder contributes only 16–22% but carries the critical signal: obs-decoder-only SGS achieves the sole 1/6 success. This dissociation between gradient share and causal importance is a general methodological contribution applicable to any multi-head architecture — it warns against using gradient magnitude as a proxy for causal influence in multi-loss systems.\n\n**Evidence**: SGS results — Reward-only SGS 0/2, Full-pathway SGS 0/3, Obs-decoder SGS 1/6 → total 1/11 (9%) (Table: Intervention Hierarchy). Gradient decomposition at exp_008d_55K: reward 49.0%, KL 34.7%, observation 16.3%, continuation 0.0%. At exp_009e_112K: reward 38.1%, KL 40.4%, observation 21.5%. Reward-detach condition (exp_044): CIVO onset not prevented (peak NVE 4.45×), delayed self-correction (eval 44→538 over 224K, 59% baseline) — lower asymptote than spontaneous recovery (exp_045: 868, 95%). Full-SGS exp_018: s1 partial mitigation (eval 448, NVE 1.66×), s2 collapse. The forward-pass conditioning mechanism explains why gradient-level intervention is fundamentally insufficient.\n\n---\n\n## Q14: Seed count per condition is too small — are the statistics reliable?\n\n**Anticipated question**: \"Individual conditions have 1–4 seeds. Fisher's exact test on such small samples has limited power. Your p=0.003 relies on pooling across conditions. Isn't the 100% onset rate (7/7) just an artifact of not running enough seeds to see failures?\"\n\n**Response**: The statistical argument rests on multiple independent lines of evidence that converge, not on any single small-sample comparison. First, the *perfect separation* between trained (7/7 onset) and frozen/removed (0/5 CIVO-free in locomotion) is the relevant test — Fisher exact p=0.003 for the three-way comparison (trained/frozen/removed). Second, the 7/7 onset figure combines two independent environments (Walker 5/5, Cheetah 2/2), each with distinct CIVO severity profiles, so environment-specific luck is unlikely. Third, the aggregate intervention evidence shows overwhelming separation: embedding removal succeeds 5/5 while all other interventions combined succeed 8/32 — this is not a borderline effect. Fourth, where seed variance matters, we report it transparently as instability evidence: TCN σ=0.2 Walker shows 2/4 success with eval retention ranging 45–91%, which we interpret as unreliability, not as a positive result. We follow Agarwal et al. (2021) in reporting IQM with stratified bootstrap CIs (IQM=148.8 for trained Walker, n=5) rather than claiming significance from small n. The compute budget (~40 GPU-days) was allocated to maximize mechanistic coverage (7 intervention types × 4 hierarchy levels × 5 environments) over per-condition replication — a deliberate design choice that prioritizes breadth of causal evidence over depth of per-condition statistics.\n\n**Evidence**: Three-way Fisher exact p=0.003: trained 7/7 onset vs. frozen 5/7 transient-only (0/7 sustained) vs. removed 0/5. Walker onset: 5/5 seeds (s1–s5), NVE 1.53–4.72×. Cheetah onset: 2/2 seeds, NVE 8.27–108.52×. IQM=148.8 (Walker trained, n=5; Agarwal et al. 2021). Intervention aggregate: removal 5/5 vs. others 8/32. Total evidence: 133 experiments, 63 successful, 35 negative across 43 configurations. TCN instability reported: σ=0.2 Walker s2 NVE 2.11× vs. s3 NVE 3.04× (late-onset CIVO). Dual-critic 2×2 factorial fully populated (4 cells, n=2 each).\n\n---\n\n## Q15: The NVE 1.5× threshold — how sensitive are your claims to this specific cutoff?\n\n**Anticipated question**: \"You claim AUROC=0.957 for NVE-based CIVO detection, but this is in-sample on n=30. The threshold 1.5× seems like it could be overfit. What happens at 1.3× or 2.0×? Is there held-out validation?\"\n\n**Response**: The 1.5× threshold was not post-hoc selected to maximize accuracy — it was pre-specified based on the initial factorial experiments and independently validated. Youden-optimal threshold from ROC analysis is 1.53×, converging on our pre-specified 1.5× without tuning. In-sample AUROC is 0.957 (27/30 correct, n=30 configurations across 2 environments). Critically, we perform Leave-One-Environment-Out (LOEO) cross-validation across Walker (n=15), Cheetah (n=5), and PickCube (n=2): the threshold falls within the optimal accuracy range for all three training folds, yielding mean held-out AUROC=0.988 and mean accuracy=0.978. The single cross-validation error is exp_008e_v3 seed 2 — an Imagination-Reality Divergence (IRD) collapse mechanistically distinct from CIVO, which produces one of only three non-CIVO false positives. Claims are stable across a wide threshold range: at 1.3× the only change is 2 additional borderline transients reclassified (no sustained CIVO misses); at 2.0× we lose early detection of moderate Walker CIVO but all severe cases remain captured. We acknowledge in-sample calibration as a limitation and recommend held-out validation on other MBRL architectures as future work.\n\n**Evidence**: In-sample AUROC=0.957, accuracy 27/30 (n=30, 2 environments). LOEO cross-validation (3 folds): PickCube held-out 2/2 accuracy, AUROC 1.000; Cheetah held-out 5/5 accuracy, AUROC 1.000; Walker held-out 14/15 accuracy, AUROC 0.963. Mean LOEO AUROC=0.988, mean accuracy=0.978. Youden-optimal threshold 1.53× — within 2% of pre-specified 1.5×. Optimal threshold range in training folds: (1.45, 1.53] when Walker available, (1.00, 3.78) when training on Cheetah+PickCube only. Three in-sample FPs: exp_025 obs-SGS s2 (NVE 1.54×, borderline), exp_028 RAVE ceil15 (NVE 1.52×, borderline), exp_008e_v3 s2 (IRD, mechanistically distinct). Threshold sensitivity: 1.3× adds 2 FPs, 2.0× misses moderate Walker onset — claims stable across [1.3×, 2.0×] range.\n",
      "numLines": 101,
      "startLine": 50,
      "totalLines": 150
    }
  }
}
```

</details>

---


### Assistant

_source line 52_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the Q&A content. Let me also get the proper experiment configurations count from the registry. The summary fields only show `status`, `created_at`, `updated_at`, `hypothesis`, `parent`. I need to get all fields to count configurations.

Let me also compute the "successful conditions" count. From the task description:
- Total experiments: 158
- success: 79
- negative: 39
- failed: 11
- killed: 24
- unknown: 5

Now let me figure out the "configurations" count. The task says "133 experiments across 43 configurations" in Q4 and Q10. I need to count how many unique configurations there are.


I'm querying the registry with expanded fields to extract the configuration information I need.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ae813a79-db9f-4a12-b6ee-ad91ade39065",
  "uuid": "e8f1e5ee-6ec8-446c-b20f-ba767e261db3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HsQuVspsHip7YCTxcqH6jQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6519,
      "cache_read_input_tokens": 36382,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6519
      },
      "output_tokens": 11,
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

_source line 53_

Now I have all the data. Let me get the configuration count from the registry.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ae813a79-db9f-4a12-b6ee-ad91ade39065",
  "uuid": "7278aa5e-905c-4f60-a14f-ab07e7f39e8e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HsQuVspsHip7YCTxcqH6jQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6519,
      "cache_read_input_tokens": 36382,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6519
      },
      "output_tokens": 11,
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

_source line 54_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_017nJ5t4ufET4RaxET7ok4d9`</summary>

```json
{
  "project": "event-gated-adaptive-horizon",
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
  "session_id": "ae813a79-db9f-4a12-b6ee-ad91ade39065",
  "uuid": "d60bbb81-0eb7-44a3-ac4a-250d98e349fc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HsQuVspsHip7YCTxcqH6jQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6519,
      "cache_read_input_tokens": 36382,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6519
      },
      "output_tokens": 11,
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

_source line 55 · 2026-05-25T14:12:28.950Z_

<details><summary>↩ Tool result · `toolu_017nJ5t4ufET4RaxET7ok4d9`</summary>

```text
Error: result (354,868 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/ae813a79-db9f-4a12-b6ee-ad91ade39065/tool-results/mcp-agent-ml-research-read_registry-1779718348946.txt.
Format: JSON with schema: {result: string}
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/ae813a79-db9f-4a12-b6ee-ad91ade39065/tool-results/mcp-agent-ml-research-read_registry-1779718348946.txt in sequential chunks until 100% of the content has been read.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ae813a79-db9f-4a12-b6ee-ad91ade39065",
  "uuid": "6d544449-aed6-46f2-8316-2909e253a6f9",
  "tool_use_result": {
    "content": "Error: result (354,868 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/ae813a79-db9f-4a12-b6ee-ad91ade39065/tool-results/mcp-agent-ml-research-read_registry-1779718348946.txt.\nFormat: JSON with schema: {result: string}\nUse offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.\nREQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:\n- You MUST read the content from the file at /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/ae813a79-db9f-4a12-b6ee-ad91ade39065/tool-results/mcp-agent-ml-research-read_registry-1779718348946.txt in sequential chunks until 100% of the content has been read.\n- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.\n- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***\n",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"exp_077_cheetah_baseline_s0\": {\"status\": \"ANALYZING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T10:48:21.685Z\", \"updated_at\": \"2026-05-25T14:12:26.249Z\", \"hypothesis\": \"Cheetah Run dt=1 baseline seed=0。建立 v/e ratio 校准基线，用于归一化同时运行的 exp_078 (Cheetah 008d) 的 VE。plan_020 第一个 seed。\", \"server\": \"westd-19154\", \"gpu\": \"cuda:0\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=0 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_077_cheetah_baseline_s0 --steps 105000 --seed 0 --compile False --device cuda:0\\\"\", \"server\": \"westd-19154\", \"gpu\": [\"cuda:0\"], \"pid\": \"21683\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_077_cheetah_baseline_s0.log\", \"submitted_at\": \"2026-05-25T11:21:44.224Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"pid\": \"21683\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_077_cheetah_baseline_s0.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=0 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_077_cheetah_baseline_s0 --steps 105000 --seed 0 --compile False --device cuda:0\\\"\", \"finished_at\": \"2026-05-25T14:07:47.479Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-25T14:07:53.264245+00:00\"}]}, \"conclusion\": \"success\"}, \"exp_082_cheetah_no_dt_emb_s0\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T13:12:29.199Z\", \"updated_at\": \"2026-05-25T14:10:44.478Z\", \"hypothesis\": \"Cheetah Run causal control: dt_embed_dim=0 + subsample ON + dt=2 + H=8, seed=0。移除 dt_embedding 后预期无 CIVO，证明 trained dt_emb 是 Cheetah CIVO 的必要条件。与 exp_078 (trained dt_emb, CIVO trigger) 构成因果对。plan_022。\", \"parent\": \"exp_010b_cheetah_civo_trigger\", \"server\": \"westd-19154\", \"gpu\": \"cuda:0\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=0 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_082_cheetah_no_dt_emb_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0 --checkpoint_every 25000\\\"\", \"server\": \"westd-19154\", \"gpu\": [\"cuda:0\"], \"pid\": \"29479\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_082_cheetah_no_dt_emb_s0.log\", \"submitted_at\": \"2026-05-25T14:10:42.486Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"pid\": \"29479\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_082_cheetah_no_dt_emb_s0.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=0 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_082_cheetah_no_dt_emb_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0 --checkpoint_every 25000\\\"\"}}, \"exp_081_008e_v3_walker_s2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T12:09:44.566Z\", \"updated_at\": \"2026-05-25T12:49:21.343Z\", \"hypothesis\": \"Walker Walk 008e_v3 mitigation seed=2: trained dt_emb + subsample ON (max_dt=2) + dt=1 imagination + H=15。C6 mitigation 第 3 seed，与 seed 0 (success, 95% baseline) 和 seed 1 (exp_080, running) 构成统计三角。plan_014。\", \"parent\": \"exp_008e_v3_subsample_on_dt1_h15\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_081_008e_v3_walker_s2 --steps 105000 --seed 2 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 1 --gate_subsample_max_dt 2 --imag_horizon 15\\\"\", \"server\": \"bjb1-45299\", \"gpu\": [\"cuda:0\"], \"pid\": \"285949\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_081_008e_v3_walker_s2.log\", \"submitted_at\": \"2026-05-25T12:10:38.467Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"seed\": 2, \"model_name\": \"DreamerV3+SubsampleON_FixedDt1_H15\", \"data_path\": \"dmc_walker_walk\", \"data_count\": 105000, \"checkpoint_source\": \"N/A (training from scratch, parent is lineage only)\", \"eval_data\": \"N/A (training experiment)\"}}, \"exp_080_008e_v3_walker_s1\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T11:30:20.594Z\", \"updated_at\": \"2026-05-25T12:49:19.083Z\", \"hypothesis\": \"Walker Walk 008e_v3 mitigation seed=1: trained dt_emb + subsample ON (max_dt=2) + dt=1 imagination + H=15。C6 mitigation 多 seed 验证——trained dt_emb 在 dt=1 imagination 下不触发 CIVO。重跑因旧 exp_008e_v3_walker_s1 metrics 疑似复制自 seed 0。plan_014。\", \"parent\": \"exp_008e_v3_subsample_on_dt1_h15\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_080_008e_v3_walker_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 1 --gate_subsample_max_dt 2 --imag_horizon 15\\\"\", \"server\": \"bjb1-45299\", \"gpu\": [\"cuda:1\"], \"pid\": \"283925\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_080_008e_v3_walker_s1.log\", \"submitted_at\": \"2026-05-25T11:30:51.090Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"seed\": 1, \"model_name\": \"DreamerV3+SubsampleON_FixedDt1_H15\", \"data_path\": \"dmc_walker_walk\", \"data_count\": 105000, \"checkpoint_source\": \"N/A (training from scratch, parent is lineage only)\", \"eval_data\": \"N/A (training experiment)\"}}, \"exp_074_008a_walker_s3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T09:08:57.028Z\", \"updated_at\": \"2026-05-25T12:08:22.221Z\", \"hypothesis\": \"Walker Walk 008a 配置 (trained dt_emb unexposed + subsample OFF + dt=2 + H=15) seed=3。当前 008a 3 seeds 全部 success (no CIVO)，加 seed=3 巩固 C3 value suppression claim 统计。来源: plan_013 扩展。\", \"parent\": \"exp_008a_no_subsample_dt2\", \"server\": \"bjb1-45299\", \"gpu\": \"cuda:0\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_074_008a_walker_s3 --steps 105000 --seed 3 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 1\\\"\", \"server\": \"bjb1-45299\", \"gpu\": [\"cuda:0\"], \"pid\": \"274730\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_074_008a_walker_s3.log\", \"submitted_at\": \"2026-05-25T09:09:28.652Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 10733.6, \"gpu_hours\": 2.98}, \"pid\": \"274730\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_074_008a_walker_s3.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_074_008a_walker_s3 --steps 105000 --seed 3 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 1\\\"\", \"code_commit\": \"fb56c860a88292ad60b6183effc1102a01205086\", \"finished_at\": \"2026-05-25T12:04:22.816Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-25T12:04:34.186555+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"eval_return_105K\": 855.9, \"civo_ve_ratio_final\": 0.3, \"civo_alert\": 0, \"value_mean_105K\": 295.2, \"gate_dt_2_frac\": 1, \"gate_dt_mean\": 2, \"model_loss_105K\": 3.8, \"eval_trajectory\": {\"5K\": 36.1, \"15K\": 281, \"25K\": 389.8, \"35K\": 303.8, \"45K\": 437.3, \"55K\": 411.3, \"65K\": 566.4, \"75K\": 513.9, \"85K\": 645.9, \"95K\": 776.6, \"105K\": 855.9}, \"four_seed_summary\": {\"mean_eval_return\": 791, \"std_eval_return\": 102.2, \"all_civo_alert_0\": true, \"seeds_completed\": 4}}, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_074_008a_walker_s3/latest.pt\", \"completed_at\": \"2026-05-25T12:08:22.221Z\"}, \"exp_079_frozen_dt_emb_walker_s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T10:48:27.865Z\", \"updated_at\": \"2026-05-25T11:28:10.029Z\", \"hypothesis\": \"Walker Walk frozen dt_emb (requires_grad=False, random init) + subsample ON + dt=2 + H=8, seed=0。验证 dt_emb 的 TRAINING 是 CIVO 必要条件。2×2 ablation 矩阵关键格。plan_015。\", \"server\": \"bjb1-45299\", \"gpu\": \"cuda:1\", \"parent\": \"exp_067_frozen_dt_emb_walker_plan015\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_079_frozen_dt_emb_walker_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True\\\"\", \"server\": \"bjb1-45299\", \"gpu\": [\"cuda:1\"], \"pid\": \"283090\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_079_frozen_dt_emb_walker_s0.log\", \"submitted_at\": \"2026-05-25T11:21:37.918Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 392.1, \"gpu_hours\": 0.11}, \"pid\": \"283090\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_079_frozen_dt_emb_walker_s0.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_079_frozen_dt_emb_walker_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True\\\"\", \"code_commit\": \"fb56c860a88292ad60b6183effc1102a01205086\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-25T11:28:10.029Z\"}, \"exp_078_cheetah_008d_s0\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T10:48:24.844Z\", \"updated_at\": \"2026-05-25T11:21:52.244Z\", \"hypothesis\": \"Cheetah Run CIVO trigger seed=0: trained dt_emb + subsample ON + dt=2 + H=8。与 exp_077 baseline 同时运行以计算 step-matched normalized VE。plan_021 第一个 seed。\", \"server\": \"westd-19154\", \"gpu\": \"cuda:1\", \"parent\": \"exp_010b_cheetah_civo_trigger\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=1 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_078_cheetah_008d_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8\\\"\", \"server\": \"westd-19154\", \"gpu\": [\"cuda:1\"], \"pid\": \"21846\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_078_cheetah_008d_s0.log\", \"submitted_at\": \"2026-05-25T11:21:50.283Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"pid\": \"21846\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_078_cheetah_008d_s0.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=1 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_078_cheetah_008d_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8\\\"\"}}, \"exp_076_cheetah_civo_trigger_s3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T10:03:42.328Z\", \"updated_at\": \"2026-05-25T10:48:15.566Z\", \"hypothesis\": \"Cheetah Run CIVO trigger seed=2: trained dt_emb + subsample ON + dt=2 + H=8。将 Cheetah CIVO trigger 扩展到第 3 个独立 seed，巩固跨环境 claim 统计力度。来源: plan_021 扩展。\", \"parent\": \"exp_010b_cheetah_civo_trigger\", \"server\": \"westd-19154\", \"gpu\": \"cuda:1\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=1 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_076_cheetah_civo_trigger_s3 --steps 105000 --seed 2 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000\\\"\", \"server\": \"westd-19154\", \"gpu\": [\"cuda:1\"], \"pid\": \"19953\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_076_cheetah_civo_trigger_s3.log\", \"submitted_at\": \"2026-05-25T10:44:40.370Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 215.2, \"gpu_hours\": 0.06}, \"pid\": \"19953\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_076_cheetah_civo_trigger_s3.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=1 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_076_cheetah_civo_trigger_s3 --steps 105000 --seed 2 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000\\\"\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-25T10:48:15.566Z\"}, \"exp_075_cheetah_civo_trigger_s2\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T10:03:40.222Z\", \"updated_at\": \"2026-05-25T10:48:13.465Z\", \"hypothesis\": \"Cheetah Run CIVO trigger seed=1: trained dt_emb + subsample ON + dt=2 + H=8 on westd-19154。复现 exp_010b 配置（原 seed=1 在 bjb1-45299），跨服务器验证 Cheetah CIVO 可复现性。来源: plan_021 扩展。\", \"parent\": \"exp_010b_cheetah_civo_trigger\", \"server\": \"westd-19154\", \"gpu\": \"cuda:0\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=0 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_075_cheetah_civo_trigger_s2 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000\\\"\", \"server\": \"westd-19154\", \"gpu\": [\"cuda:0\"], \"pid\": \"19788\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_075_cheetah_civo_trigger_s2.log\", \"submitted_at\": \"2026-05-25T10:44:34.345Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 219.1, \"gpu_hours\": 0.06}, \"pid\": \"19788\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_075_cheetah_civo_trigger_s2.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=0 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_075_cheetah_civo_trigger_s2 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000\\\"\"}, \"conclusion\": \"killed\", \"completed_at\": \"2026-05-25T10:48:13.465Z\"}, \"exp_071_008f_walker_s3\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T07:03:48.097Z\", \"updated_at\": \"2026-05-25T10:42:39.889Z\", \"hypothesis\": \"Walker Walk 008f 配置 (no dt_emb, dt_embed_dim=0 + subsample ON + dt=2 + H=8) seed=3。当前 008f 2 seeds 结果分歧（s1=success eval=503, s2=negative eval=148），增加 seed 缩窄 causal control 稳定性估计。来源: plan_012 扩展。\", \"parent\": \"exp_008f_no_dt_embed_subsample_on_h8\", \"server\": \"bjb1-45299\", \"gpu\": \"cuda:1\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_071_008f_walker_s3 --steps 105000 --seed 3 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"server\": \"bjb1-45299\", \"gpu\": [\"cuda:1\"], \"pid\": \"265628\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_071_008f_walker_s3.log\", \"submitted_at\": \"2026-05-25T07:04:24.723Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 13095.2, \"gpu_hours\": 3.64}, \"pid\": \"265628\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_071_008f_walker_s3.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_071_008f_walker_s3 --steps 105000 --seed 3 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"code_commit\": \"fb56c860a88292ad60b6183effc1102a01205086\", \"finished_at\": \"2026-05-25T10:05:58.573Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-25T10:06:05.930693+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"eval_return_final\": 311.9, \"eval_return_peak\": 457.7, \"ve_ratio_final\": 0.4, \"ve_ratio_peak\": 0.7, \"gate_dt_mean_final\": 2, \"civo_alert\": 0, \"value_loss_final\": 1, \"actor_entropy_final\": -4.6, \"model_loss_final\": 4.5}, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_071_008f_walker_s3\", \"completed_at\": \"2026-05-25T10:42:39.889Z\"}, \"exp_073_008f_walker_s4\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T07:30:42.251Z\", \"updated_at\": \"2026-05-25T10:00:42.604Z\", \"hypothesis\": \"Walker Walk 008f 配置 (no dt_emb, dt_embed_dim=0 + subsample ON + dt=2 + H=8) seed=4。当前 008f 0/3 CIVO onset，扩到 seed=4 进一步巩固 control 组统计。来源: plan_012 扩展。\", \"parent\": \"exp_008f_no_dt_embed_subsample_on_h8\", \"server\": \"westd-19154\", \"gpu\": \"cuda:0\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_073_008f_walker_s4 --steps 105000 --seed 4 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"server\": \"westd-19154\", \"gpu\": [\"cuda:0\"], \"pid\": \"11670\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_073_008f_walker_s4.log\", \"submitted_at\": \"2026-05-25T07:31:11.391Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 8971.2, \"gpu_hours\": 2.49}, \"pid\": \"11670\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_073_008f_walker_s4.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_073_008f_walker_s4 --steps 105000 --seed 4 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"finished_at\": \"2026-05-25T09:48:03.882Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-25T09:48:13.191417+00:00\"}]}, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_073_008f_walker_s4\", \"conclusion\": \"success\", \"metrics\": {\"eval_return_final\": 289.3, \"eval_return_peak\": 486.5, \"eval_return_peak_step\": 75000, \"ve_ratio_final\": 0.5, \"ve_ratio_peak\": 0.5, \"nve_peak\": 0.76, \"civo_alert\": 0, \"civo\": false, \"gate_dt_2_frac\": 1, \"gate_dt_mean\": 2, \"gate_empirical_entropy\": 0, \"eval_trajectory\": [{\"step\": 5000, \"eval_return\": 33.2}, {\"step\": 15000, \"eval_return\": 128.3}, {\"step\": 25000, \"eval_return\": 165.3}, {\"step\": 35000, \"eval_return\": 284.5}, {\"step\": 45000, \"eval_return\": 272.5}, {\"step\": 55000, \"eval_return\": 406.7}, {\"step\": 65000, \"eval_return\": 379.5}, {\"step\": 75000, \"eval_return\": 486.5}, {\"step\": 85000, \"eval_return\": 352.6}, {\"step\": 95000, \"eval_return\": 297.7}, {\"step\": 105000, \"eval_return\": 289.3}]}, \"completed_at\": \"2026-05-25T10:00:42.604Z\"}, \"exp_072_008e_v3_walker_s5\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T07:24:08.174Z\", \"updated_at\": \"2026-05-25T10:00:39.306Z\", \"hypothesis\": \"Walker Walk 008e_v3 mitigation 配置 (trained dt_emb + subsample ON + dt=1 imag + H=15) seed=5。当前 5 seeds 测试 collapse rate=2/5 (40%)，加 seed=5 缩窄置信区间。来源: plan_016 扩展。\", \"parent\": \"exp_008e_v3_subsample_on_dt1_h15\", \"server\": \"westd-19154\", \"gpu\": \"cuda:1\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_072_008e_v3_walker_s5 --steps 105000 --seed 5 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 1 --gate_subsample_max_dt 2 --imag_horizon 15\\\"\", \"server\": \"westd-19154\", \"gpu\": [\"cuda:1\"], \"pid\": \"11116\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_072_008e_v3_walker_s5.log\", \"submitted_at\": \"2026-05-25T07:24:40.695Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 9358.6, \"gpu_hours\": 2.6}, \"pid\": \"11116\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_072_008e_v3_walker_s5.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_072_008e_v3_walker_s5 --steps 105000 --seed 5 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 1 --gate_subsample_max_dt 2 --imag_horizon 15\\\"\", \"finished_at\": \"2026-05-25T09:47:34.147Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-25T09:47:39.804739+00:00\"}]}, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_072_008e_v3_walker_s5\", \"conclusion\": \"success\", \"metrics\": {\"eval_return_final\": 853.1, \"eval_return_peak\": 853.1, \"eval_return_peak_step\": 105000, \"ve_ratio_final\": 0.6, \"nve_final\": 0.61, \"nve_peak\": 0.61, \"nve_peak_step\": 105000, \"civo_alert\": 0, \"civo\": false, \"gate_dt_1_frac\": 1, \"gate_dt_mean\": 1, \"actor_entropy_final\": -5.1, \"value_mean_final\": 520.8, \"eval_trajectory\": [{\"step\": 5000, \"eval_return\": 29.4}, {\"step\": 15000, \"eval_return\": 251.1}, {\"step\": 25000, \"eval_return\": 423}, {\"step\": 35000, \"eval_return\": 511}, {\"step\": 45000, \"eval_return\": 600.1}, {\"step\": 55000, \"eval_return\": 649}, {\"step\": 65000, \"eval_return\": 697.2}, {\"step\": 75000, \"eval_return\": 727.3}, {\"step\": 85000, \"eval_return\": 710.3}, {\"step\": 95000, \"eval_return\": 803.9}, {\"step\": 105000, \"eval_return\": 853.1}]}, \"completed_at\": \"2026-05-25T10:00:39.306Z\"}, \"exp_070_008e_v3_walker_s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T05:07:49.050Z\", \"updated_at\": \"2026-05-25T08:54:47.019Z\", \"hypothesis\": \"Walker Walk 008e_v3 mitigation 配置 (trained dt_emb + subsample ON + dt=1 imag + H=15) seed=0。当前 4 unique seeds 测试结果 collapse rate=2/4 (50%)，加 seed=0 缩窄置信区间。来源: plan_016 扩展。\", \"parent\": \"exp_008e_v3_subsample_on_dt1_h15\", \"server\": \"bjb1-45299\", \"gpu\": \"cuda:0\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_070_008e_v3_walker_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 1 --gate_subsample_max_dt 2 --imag_horizon 15\\\"\", \"server\": \"bjb1-45299\", \"gpu\": [\"cuda:0\"], \"pid\": \"260999\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_070_008e_v3_walker_s0.log\", \"submitted_at\": \"2026-05-25T05:29:11.281Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 12335.7, \"gpu_hours\": 3.43}, \"pid\": \"260999\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_070_008e_v3_walker_s0.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_070_008e_v3_walker_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 1 --gate_subsample_max_dt 2 --imag_horizon 15\\\"\", \"code_commit\": \"fb56c860a88292ad60b6183effc1102a01205086\", \"finished_at\": \"2026-05-25T08:50:11.463Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-25T08:50:17.078252+00:00\"}]}, \"metrics\": {\"eval_return\": 148, \"peak_eval_return\": 232.5, \"peak_eval_step\": 55000, \"ve_ratio_105k\": 0.8, \"nve_peak\": 0.8, \"nve_peak_step\": 95000, \"civo\": false, \"gate_dt_1_frac\": 1, \"gate_dt_mean\": 1, \"actor_entropy_final\": -3.7, \"value_mean_final\": 122.1, \"failure_mode\": \"non-CIVO learning failure (never reached baseline performance)\", \"eval_trajectory\": [{\"step\": 5000, \"eval_return\": 37.4}, {\"step\": 15000, \"eval_return\": 93.2}, {\"step\": 25000, \"eval_return\": 178.8}, {\"step\": 35000, \"eval_return\": 221.6}, {\"step\": 45000, \"eval_return\": 230.9}, {\"step\": 55000, \"eval_return\": 232.5}, {\"step\": 65000, \"eval_return\": 194}, {\"step\": 75000, \"eval_return\": 175.2}, {\"step\": 85000, \"eval_return\": 218.6}, {\"step\": 95000, \"eval_return\": 139.6}, {\"step\": 105000, \"eval_return\": 148}], \"ve_ratio_trajectory\": [{\"step\": 15000, \"ve\": 0}, {\"step\": 25000, \"ve\": 0.1}, {\"step\": 35000, \"ve\": 0.2}, {\"step\": 45000, \"ve\": 0.3}, {\"step\": 55000, \"ve\": 0.4}, {\"step\": 65000, \"ve\": 0.5}, {\"step\": 75000, \"ve\": 0.6}, {\"step\": 85000, \"ve\": 0.5}, {\"step\": 95000, \"ve\": 0.8}, {\"step\": 105000, \"ve\": 0.8}]}, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_070_008e_v3_walker_s0/latest.pt\", \"conclusion\": \"negative\", \"notes\": \"Seed 0 FAILED but NOT via CIVO. eval_return peaked at 232.5@55K (far below baseline ~500+), declined to 148@105K. ve_ratio stayed healthy throughout (max 0.8, never triggered CIVO alert). Gate locked dt=1. This is a distinct failure mode from seeds 2,3 (which had CIVO collapse with NVE>3.7x). Agent never reached high performance — learning stagnated early. Cross-seed 008e_v3 summary: 5 seeds tested, 2 success (s1=870, s4=899), 2 CIVO collapse (s2=137 NVE=3.78, s3=93 NVE=4.02), 1 non-CIVO failure (s0=148 NVE=0.8). CIVO collapse rate: 2/5=40%. Overall failure rate: 3/5=60%.\", \"completed_at\": \"2026-05-25T08:54:47.019Z\"}, \"exp_069_008f_walker_repro_s1\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-25T03:49:41.282Z\", \"updated_at\": \"2026-05-25T07:28:33.676Z\", \"hypothesis\": \"Reproducing 008f config (no dt_emb, dt_embed_dim=0 + subsample ON + dt=2 + H=8) on Walker Walk seed=1 will NOT trigger CIVO (NVE < 1.5x) because removing dt_emb eliminates the temporal abstraction mismatch that drives value error amplification\", \"parent\": \"exp_008f_no_dt_embed_subsample_on_h8\", \"failure_reason\": \"bjb1-40020 服务器不可达（SSH 连接 port 40020 on 106.120.183.117 失败），进程无法监控，未产生有效 W&B metrics\", \"completed_at\": \"2026-05-25T04:17:38.829Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-25T04:17:43.081459+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-25T07:17:09.809673+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"server\": \"westd-19154\", \"gpu\": \"cuda:1\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_069_008f_walker_repro_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"server\": \"westd-19154\", \"gpu\": [\"cuda:1\"], \"pid\": \"4590\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_069_008f_walker_repro_s1.log\", \"submitted_at\": \"2026-05-25T05:04:10.980Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 8662.7, \"gpu_hours\": 2.41}, \"pid\": \"4590\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_069_008f_walker_repro_s1.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_069_008f_walker_repro_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"finished_at\": \"2026-05-25T07:17:02.903Z\"}, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_069_008f_walker_repro_s1/latest.pt\", \"metrics\": {\"eval_return_final\": 237.8, \"eval_return_peak\": 390.1, \"eval_return_peak_step\": 95000, \"ve_ratio_final\": 0.4, \"ve_ratio_peak\": 0.4, \"ve_ratio_peak_step\": 105000, \"nve_final_105k\": 0.61, \"nve_peak\": 0.66, \"nve_peak_step\": 75000, \"civo_alert\": false, \"gate_dt_2_frac\": 1, \"eval_trajectory\": {\"5k\": 30.5, \"15k\": 158.7, \"25k\": 180.8, \"35k\": 250.3, \"45k\": 293.6, \"55k\": 272.2, \"65k\": 328.1, \"75k\": 244.8, \"85k\": 382.5, \"95k\": 390.1, \"105k\": 237.8}, \"ve_ratio_trajectory\": {\"15k\": 0, \"25k\": 0.1, \"35k\": 0.2, \"45k\": 0.2, \"55k\": 0.3, \"65k\": 0.3, \"75k\": 0.4, \"85k\": 0.3, \"95k\": 0.3, \"105k\": 0.4}}, \"conclusion\": \"success\"}, \"exp_068_008d_walker_repro_s1\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-25T03:49:39.539Z\", \"updated_at\": \"2026-05-25T07:28:31.319Z\", \"hypothesis\": \"Reproducing 008d config (trained dt_emb + subsample ON + dt=2 + H=8) on Walker Walk seed=1 will trigger CIVO (NVE > 1.5x) because trained dt_emb enables value error amplification through temporal abstraction mismatch\", \"parent\": \"exp_008d_subsample_on_h8\", \"failure_reason\": \"SSH check failed 5x — last error: [Errno None] Unable to connect to port 40020 on 106.120.183.117\", \"completed_at\": \"2026-05-25T04:18:15.954Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-25T04:18:20.002698+00:00\"}, {\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-25T07:23:04.341146+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"server\": \"westd-19154\", \"gpu\": \"cuda:0\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_068_008d_walker_repro_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8\\\"\", \"server\": \"westd-19154\", \"gpu\": [\"cuda:0\"], \"pid\": \"4425\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_068_008d_walker_repro_s1.log\", \"submitted_at\": \"2026-05-25T05:04:05.168Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 8666.2, \"gpu_hours\": 2.41}, \"pid\": \"4425\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_068_008d_walker_repro_s1.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_068_008d_walker_repro_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8\\\"\", \"finished_at\": \"2026-05-25T07:22:57.100Z\"}, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_068_008d_walker_repro_s1/latest.pt\", \"metrics\": {\"eval_return_final\": 39.1, \"eval_return_peak\": 192.4, \"eval_return_peak_step\": 55000, \"ve_ratio_final\": 2.7, \"ve_ratio_peak\": 4.6, \"ve_ratio_peak_step\": 85000, \"nve_final_105k\": 4.12, \"nve_peak_85k\": 6.57, \"nve_onset_step\": 45000, \"nve_onset_value\": 1.81, \"civo_alert\": true, \"civo_alert_step\": 85000, \"gate_dt_2_frac\": 1, \"eval_trajectory\": {\"5k\": 31, \"15k\": 146.5, \"25k\": 174.1, \"35k\": 189.6, \"45k\": 142.2, \"55k\": 192.4, \"65k\": 114.4, \"75k\": 106.6, \"85k\": 33.4, \"95k\": 26.9, \"105k\": 39.1}, \"ve_ratio_trajectory\": {\"15k\": 0, \"25k\": 0.2, \"35k\": 0.3, \"45k\": 0.6, \"55k\": 0.6, \"65k\": 1.3, \"75k\": 1.6, \"85k\": 4.6, \"95k\": 4.6, \"105k\": 2.7}}, \"conclusion\": \"success\"}, \"exp_067_frozen_dt_emb_walker_plan015\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T03:49:37.736Z\", \"updated_at\": \"2026-05-25T06:59:24.006Z\", \"hypothesis\": \"Frozen (requires_grad=False) dt_embedding + subsample ON + dt=2 + H=8 在 Walker Walk 上不触发 CIVO，验证 dt_emb 的 TRAINING 是 CIVO 的必要条件（而非 dt_emb 的存在本身）。来源: plan_015。\", \"parent\": \"exp_042_frozen_dt_emb_walker\", \"server\": \"bjb1-45299\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb1-45299\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-25T03:51:43.628Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_067_frozen_dt_emb_walker_plan015 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True\\\"\", \"code_commit\": \"fb56c860a88292ad60b6183effc1102a01205086\", \"finished_at\": \"2026-05-25T06:54:52.150Z\", \"training_hours\": 3.05}, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_067_frozen_dt_emb_walker_plan015 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True\\\"\", \"server\": \"bjb1-45299\", \"gpu\": [\"cuda:1\"], \"pid\": \"255883\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_067_frozen_dt_emb_walker_plan015.log\", \"submitted_at\": \"2026-05-25T03:52:29.860Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 11214.1, \"gpu_hours\": 3.12}, \"pid\": \"255883\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_067_frozen_dt_emb_walker_plan015.log\", \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-25T06:54:57.723176+00:00\"}]}, \"metrics\": {\"eval_final\": 281.5, \"eval_peak\": 334.1, \"eval_peak_step\": 95000, \"nve_peak\": 0.4, \"nve_final\": 0.2, \"civo_alert\": 0, \"total_env_steps\": 112000, \"update_count\": 25099, \"gate_dt_mean\": 2, \"gate_dt_std\": 0, \"gate_dt_2_frac\": 1, \"gate_empirical_entropy\": 0}, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_067_frozen_dt_emb_walker_plan015/latest.pt\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-25T06:59:24.006Z\"}, \"exp_066b_timeseries_rssm_fidelity_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-25T02:34:14.574Z\", \"updated_at\": \"2026-05-25T04:35:12.673Z\", \"hypothesis\": \"RSSM fidelity gap (dt=2 prediction error > dt=1) emerges before value overestimation in seed=1, replicating the causal chain found in exp_066 seed=0 and confirming cross-seed robustness of the fidelity→VE mechanism.\", \"parent\": \"exp_066_timeseries_rssm_fidelity\", \"server\": \"bjb1-45299\", \"gpu\": \"cuda:0\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_066b_timeseries_rssm_fidelity_s1 --steps 60000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 5000 --eval_every 5000\\\"\", \"server\": \"bjb1-45299\", \"gpu\": [\"cuda:0\"], \"pid\": \"252133\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_066b_timeseries_rssm_fidelity_s1.log\", \"submitted_at\": \"2026-05-25T02:38:44.421Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 6988.3, \"gpu_hours\": 1.94}, \"pid\": \"252133\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_066b_timeseries_rssm_fidelity_s1.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_066b_timeseries_rssm_fidelity_s1 --steps 60000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 5000 --eval_every 5000\\\"\", \"code_commit\": \"fb56c860a88292ad60b6183effc1102a01205086\", \"finished_at\": \"2026-05-25T04:18:02.308Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-25T04:18:10.617905+00:00\"}]}, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_066b_timeseries_rssm_fidelity_s1/checkpoint_65000.pt\", \"metrics\": {\"seed\": 1, \"steps_completed\": 65000, \"eval_return_peak\": 201.9, \"eval_return_peak_step\": 45000, \"eval_return_final\": 160.7, \"civo_alert_step\": 55000, \"ve_ratio_final\": 0.724, \"fidelity_gap_timeseries\": {\"ss_ratio_10K\": 0.887, \"ss_ratio_15K\": 1.017, \"ss_ratio_20K\": 1.216, \"ss_ratio_25K\": 1.532, \"ss_ratio_30K\": 1.374, \"ss_ratio_35K\": 1.486, \"ss_ratio_40K\": 1.428, \"ss_ratio_45K\": 1.38, \"ss_ratio_50K\": 1.468, \"ss_ratio_55K\": 1.517, \"ss_ratio_60K\": 1.799, \"ss_ratio_65K\": 1.756}, \"ve_ratio_timeseries\": {\"12K\": 0.012, \"15K\": 0.033, \"24K\": 0.118, \"25K\": 0.193, \"35K\": 0.269, \"45K\": 0.358, \"52K\": 0.495, \"55K\": 0.71, \"64K\": 0.724}, \"fidelity_gap_onset_step\": 15000, \"ve_onset_step\": 24000, \"temporal_lead_steps\": 9000, \"causal_direction\": \"fidelity_gap_leads_ve\", \"cross_seed_comparison\": {\"s0_ss_ratio_65K\": 1.678, \"s1_ss_ratio_65K\": 1.756, \"s0_fidelity_onset\": 20000, \"s1_fidelity_onset\": 15000, \"s0_ve_onset\": 30000, \"s1_ve_onset\": 24000, \"s0_temporal_lead\": 10000, \"s1_temporal_lead\": 9000, \"pattern_consistent\": true}}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-25T04:35:12.673Z\"}, \"exp_062_cartpole_control\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T16:01:08.858Z\", \"updated_at\": \"2026-05-25T03:45:35.194Z\", \"hypothesis\": \"dt_embed_dim=0 + subsample ON + H=8 在 Cartpole Swingup 上不触发 CIVO（NVE < 1.5x），因果控制实验验证移除 dt_emb 是否阻止 CIVO 在第三个环境中泛化。与 exp_061 配对形成因果对比。\", \"spec\": {\"command\": \"bash -c 'for SEED in 0 1 2; do python -u dreamer.py --configs defaults dmc_proprio --task dmc_cartpole_swingup --logdir logdir/exp_062_cartpole_control_s${SEED} --steps 105000 --seed $SEED --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0 --checkpoint_every 25000; done'\", \"server\": \"bjb1-40020\", \"gpu\": [\"cuda:0\"], \"pid\": \"473913\", \"log_path\": \"bjb1-40020:~/runs/event-gated-adaptive-horizon/exp_062_cartpole_control.log\", \"submitted_at\": \"2026-05-24T16:26:50.780Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"dmc_cartpole_swingup\", \"data_count\": 105000, \"model_name\": \"DreamerV3 (dt_embed_dim=0, control, Cartpole Swingup)\", \"seed\": \"0,1,2\", \"gpu_ids\": [0], \"checkpoint_path\": \"bjb1-40020:/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_062_cartpole_control_s0/checkpoint.pt\", \"wall_clock_seconds\": 40686.6, \"gpu_hours\": 11.3}, \"metrics\": {\"seeds\": {\"s0\": {\"eval_return\": 230.4, \"ve_ratio_peak\": 0.069, \"ve_ratio_final\": 0.056, \"value_mean\": 12.9, \"civo_detected\": false}, \"s1\": {\"eval_return\": 255.3, \"ve_ratio_peak\": 0.079, \"ve_ratio_final\": 0.04, \"value_mean\": 10.2, \"civo_detected\": false}, \"s2\": {\"eval_return\": 248.8, \"ve_ratio_peak\": 0.065, \"ve_ratio_final\": 0.048, \"value_mean\": 11.8, \"civo_detected\": false}}, \"mean_eval_return\": 244.8, \"mean_ve_ratio_peak\": 0.071, \"civo_detected_any\": false, \"steps_completed\": 112000}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-25T03:44:57.338Z\"}, \"exp_061_cartpole_civo_trigger\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-24T16:01:07.009Z\", \"updated_at\": \"2026-05-25T03:18:38.759Z\", \"hypothesis\": \"Trained dt_emb (d=32) + subsample ON + H=8 + dt=2 imagination 在 Cartpole Swingup 上触发 CIVO（NVE > 1.5x），验证 CIVO 是否跨 locomotion 子类环境泛化（Walker/Cheetah 已确认，Cartpole 是第三个 DMC locomotion 环境）。与 exp_062 配对形成因果对比。\", \"spec\": {\"command\": \"bash -c '... --device cuda:0 ...'\", \"server\": \"bjb1-45299\", \"gpu\": [\"cuda:1\"], \"pid\": \"226158\", \"log_path\": \"bjb1-45299:/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_061_cartpole_civo_trigger_s{0,1,2}/\", \"submitted_at\": \"2026-05-24T16:50:56.301Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"dmc_cartpole_swingup\", \"data_count\": 105000, \"model_name\": \"DreamerV3 (trained dt_emb, CIVO trigger, Cartpole Swingup)\", \"seed\": \"0,1,2\", \"gpu_ids\": [1], \"checkpoint_path\": \"bjb1-45299:/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_061_cartpole_civo_trigger_s{0,1,2}/latest.pt\", \"wall_clock_seconds\": 39600, \"gpu_hours\": 11}, \"conclusion\": \"negative\", \"metrics\": {\"seeds\": 3, \"steps_per_seed\": 112000, \"s0_eval_return_final\": 211.1, \"s0_eval_return_peak\": 247.8, \"s0_value_mean_final\": 9.229, \"s0_ve_ratio_peak\": 0.058, \"s0_train_return_final\": 199.2, \"s1_eval_return_final\": 269, \"s1_eval_return_peak\": 328.1, \"s1_value_mean_final\": 9.323, \"s1_ve_ratio_peak\": 0.04, \"s1_train_return_final\": 188.7, \"s2_eval_return_final\": 228.9, \"s2_eval_return_peak\": 245.9, \"s2_value_mean_final\": 9.46, \"s2_ve_ratio_peak\": 0.043, \"s2_train_return_final\": 258.9, \"civo_detected\": false, \"civo_alert_any_seed\": false, \"ve_ratio_max_all_seeds\": 0.058, \"vs_baseline_eval_mean\": \"-56.3%\", \"baseline_exp060_eval_s2_105K\": 557}, \"completed_at\": \"2026-05-25T03:18:38.759Z\"}, \"exp_008d_subsample_on_h8\": {\"completed_at\": \"2026-05-14T04:50:52.439Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-14T01:46:57.960Z\", \"hypothesis\": \"Trained dt-embedding with subsample (gate_fixed_dt=2, gate_subsample_max_dt=2) causes critic value function to overestimate through dt-conditioned representation co-adaptation, leading to policy collapse.\", \"metrics\": {\"actor_loss_25K\": -0.195, \"actor_loss_35K\": -0.17, \"baseline_35K\": 400, \"baseline_45K\": 443, \"data_source_45K\": \"from training logs metrics.jsonl\", \"eval_return_25K\": 167.22, \"eval_return_35K\": 146.34, \"eval_return_45K\": 140.8, \"eval_return_55K\": 82.75, \"model_loss_25K\": 5.33, \"model_loss_35K\": 5.07, \"step\": 55000, \"trend\": \"eval declining 167→146→141→83; v/e accelerating 15.5%→41.2%→69.3%→167% — delusional critic collapse confirmed, value exceeds eval_return at 55K\", \"value_eval_ratio_25K\": 0.155, \"value_eval_ratio_35K\": 0.411, \"value_eval_ratio_45K\": 0.693, \"value_eval_ratio_55K\": 1.666, \"value_mean_25K\": 25.86, \"value_mean_35K\": 60.2, \"value_mean_45K\": 97.5, \"value_mean_55K\": 137.88, \"verdict_35K\": \"WARN_COLLAPSE\", \"verdict_45K\": \"COLLAPSE_CONFIRMED\", \"vs_baseline_35K\": \"-63.4%\", \"vs_baseline_45K\": \"-68.2%\"}, \"parent\": \"exp_005_event_gated_v4\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008d_subsample_on_h8/checkpoint.ckpt\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008d_subsample_on_h8 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 2.48, \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008d_subsample_on_h8\", \"model_name\": \"DreamerV3+FixedDt2_Subsample_H8 (gate_fixed_dt=2, gate_subsample_max_dt=2, imag_horizon=8)\", \"pid\": \"109519\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-14T02:21:59.852Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 8932.6}, \"status\": \"DONE\", \"updated_at\": \"2026-05-25T02:41:05.620Z\", \"notes\": \"RSSM fidelity analysis (exp_063, 55K checkpoint only): dt=2/dt=1 single-step reward MAE ratio = 2.695x (vs exp_066 s0's 1.37x at same step). Larger fidelity gap correlates with worse VE (1.666 vs 0.621). No intermediate checkpoints exist — cannot directly verify 25K fidelity gap for this seed. Cross-seed pattern consistent: VE trajectory matches s0 (low at 25K, collapse by 55K). See artifact art_20260525_e45921.\"}, \"exp_066_timeseries_rssm_fidelity\": {\"status\": \"DONE\", \"retry_count\": 1, \"created_at\": \"2026-05-24T21:07:53.125Z\", \"updated_at\": \"2026-05-25T02:33:00.783Z\", \"hypothesis\": \"Trained dt_embedding causes RSSM fidelity degradation (dt=2 vs dt=1 reward MAE gap) that progressively worsens during training, and its temporal evolution precedes or synchronizes with NVE (value overestimation) rise, establishing a temporal causal chain: RSSM fidelity gap → value overestimation.\", \"parent\": \"exp_063_rssm_fidelity\", \"server\": \"bjb1-40020\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb1-40020\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-24T22:27:54.087Z\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/dreamerv3-torch && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_066_timeseries_rssm_fidelity_s0 --steps 60000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 5000 --eval_every 999999\\\"\", \"code_commit\": \"fb56c860a88292ad60b6183effc1102a01205086\", \"finished_at\": \"2026-05-24T22:28:15.966Z\", \"training_hours\": 0.01}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"completed_at\": \"2026-05-24T22:28:19.155Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-24T22:28:24.279787+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_066_timeseries_rssm_fidelity_s0 --steps 60000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 5000 --eval_every 5000'\", \"server\": \"bjb1-40020\", \"gpu\": \"cuda:1\", \"pid\": 490622, \"fix_note\": \"eval_every changed from 999999 to 5000 — checkpoint saving is coupled to eval loop, 999999 prevented checkpoints from being saved\", \"checkpoint_path\": \"bjb1-40020:/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_066_timeseries_rssm_fidelity_s0/checkpoint.pt\", \"log_path\": \"bjb1-40020:/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_066_timeseries_rssm_fidelity_s0/\"}, \"conclusion\": \"success\", \"metrics\": {\"ss_ratio_10K\": 1.047, \"ss_ratio_30K\": 1.247, \"ss_ratio_65K\": 1.678, \"ol_ratio_30K_peak\": 1.446, \"ol_ratio_35K_peak\": 1.509, \"ve_ratio_final\": 1.399, \"fidelity_gap_onset_step\": 20000, \"ve_onset_step\": 30000, \"temporal_lead_steps\": 10000, \"pearson_ss_ve\": 0.807, \"pearson_ss_ve_p\": 0.0015, \"pearson_ol_ve\": 0.425, \"pearson_ol_ve_p\": 0.169, \"ss_monotonicity\": 0.73, \"ol_monotonicity\": 0.73, \"ve_monotonicity\": 0.82, \"causal_direction\": \"fidelity_gap_leads_ve\", \"conclusion\": \"success\"}}, \"exp_060_cartpole_baseline\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T16:01:05.099Z\", \"updated_at\": \"2026-05-25T01:25:39.711Z\", \"hypothesis\": \"Cartpole Swingup (DMC) baseline dt=1 建立 v/e ratio 校准基线，用于 CIVO 诊断阈值在第三个 DMC 环境的验证。预期 NVE 保持在 1.0x 附近，无 CIVO 现象。\", \"spec\": {\"command\": \"bash -c 'for SEED in 0 1 2; do python -u dreamer.py --configs defaults dmc_proprio --task dmc_cartpole_swingup --logdir logdir/exp_060_cartpole_baseline_s${SEED} --steps 105000 --seed $SEED --compile False --device cuda:0 --checkpoint_every 25000; done'\", \"server\": \"bjb1-45299\", \"gpu\": [\"cuda:0\"], \"pid\": \"223294\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_060_cartpole_baseline.log\", \"submitted_at\": \"2026-05-24T16:26:42.610Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"dmc_cartpole_swingup\", \"data_count\": 105000, \"model_name\": \"DreamerV3 (vanilla baseline, Cartpole Swingup)\", \"seed\": \"0,1,2\", \"gpu_ids\": [0], \"wall_clock_seconds\": 32337.1, \"gpu_hours\": 8.98}, \"conclusion\": \"success\", \"metrics\": {\"seeds\": 3, \"steps_per_seed\": 112000, \"train_return_s0\": 809.4, \"train_return_s1\": 684.4, \"train_return_s2\": 526.1, \"eval_return_s2_105K\": 557}, \"checkpoint_path\": \"bjb1-45299:/root/dreamerv3-torch/logdir/exp_060_cartpole_baseline_s{0,1,2}/latest.pt\", \"log_path\": \"bjb1-45299:/root/dreamerv3-torch/logdir/exp_060_cartpole_baseline_s{0,1,2}/metrics.jsonl\", \"completed_at\": \"2026-05-25T01:25:39.711Z\"}, \"exp_065_dt_emb_cosine\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T20:48:47.693Z\", \"updated_at\": \"2026-05-24T20:54:51.678Z\", \"hypothesis\": \"分析 trained dt_embedding 中 dt=1 vs dt=2 向量的 cosine similarity 及其训练过程演化。如果 cosine sim 高（接近 1）→ dt_emb 未学到有意义区分，CIVO 来自微小差异被 downstream 放大；如果 cosine sim 低 → dt_emb 学到了显著不同的表征，CIVO 来自 dt=2 表征本身的偏差。\", \"conclusion\": \"success\", \"checkpoint_path\": \"logdir/exp_065_dt_emb_cosine/results.json\", \"log_path\": \"bjb1-45299:/root/dreamerv3-torch/logdir/exp_065_dt_emb_cosine/\", \"completed_at\": \"2026-05-24T20:52:24.863Z\", \"metrics\": {\"trained_cosine_sim_range\": \"-0.94 to -0.70\", \"frozen_cosine_sim_range\": \"-0.15 to +0.07\", \"trained_trend\": \"strong negative (near-opposite directions)\", \"frozen_trend\": \"near-zero constant\", \"conclusion\": \"dt=1 and dt=2 embeddings learn nearly opposite representations; CIVO from dt=2 representation bias, not amplified micro-differences\"}}, \"exp_064_value_distribution\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T19:23:05.483Z\", \"updated_at\": \"2026-05-24T20:14:50.460Z\", \"hypothesis\": \"V(s) vs Monte Carlo return 分布对比：trained dt_emb (exp_008d collapsed) 的 value estimate 在 dt=2 imagination 步骤系统性高估，而 untrained/absent dt_emb (exp_008f control) 和 baseline (exp_001) 的 value 分布与 MC return 紧密跟踪。直观展示 CIVO 的 value divergence 位置和形态。\", \"server\": \"bjb1-40020\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb1-40020\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-24T19:56:27.179Z\"}, \"spec\": {\"command\": \"python scripts/value_distribution_analysis.py --device cuda:0\", \"server\": \"bjb1-40020\", \"data_path\": \"logdir/exp_001_baseline + logdir/exp_008d + logdir/exp_008f\", \"data_count\": 500, \"model_name\": \"DreamerV3 (baseline + collapsed + control checkpoints)\", \"seed\": 0, \"gpu_ids\": [1], \"checkpoint_path\": \"logdir/exp_064_value_distribution/\", \"log_path\": \"logdir/exp_064_value_distribution/results.json\"}, \"conclusion\": \"success\", \"metrics\": {\"baseline_bias\": 344.85, \"baseline_rmse\": 371.73, \"baseline_overest_pct\": 100, \"baseline_v_mc_ratio\": 3.31, \"civo_bias\": 108.99, \"civo_rmse\": 112.36, \"civo_overest_pct\": 100, \"civo_v_mc_ratio\": 7.8, \"civo_v_mc_median\": 3.4, \"control_bias\": -6.51, \"control_rmse\": 57.93, \"control_overest_pct\": 52.5, \"control_v_mc_ratio\": 2.58, \"control_v_mc_median\": 1.05}, \"completed_at\": \"2026-05-24T20:14:50.460Z\"}, \"exp_063_rssm_fidelity\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T18:12:47.163Z\", \"updated_at\": \"2026-05-24T19:21:37.837Z\", \"hypothesis\": \"RSSM 在 dt=2 transitions 上的 observation/reward reconstruction loss 显著高于 dt=1，量化 fidelity gap 作为 trained dt_emb 导致 delusional critic 的机械性基础。从 exp_001 (baseline) 和 exp_008d (collapsed) 的已有 checkpoint 提取，对比 dt=1 vs dt=2 prediction quality。\", \"server\": \"bjb1-40020\", \"gpu\": \"cuda:1\", \"account\": \"root\", \"reproduce\": {\"server\": \"bjb1-40020\", \"gpu\": \"cuda:1\", \"started_at\": \"2026-05-24T18:53:48.781Z\"}, \"spec\": {\"command\": \"python scripts/rssm_fidelity_analysis.py --device cuda:0\", \"server\": \"bjb1-40020\", \"data_path\": \"logdir/exp_001_baseline + logdir/exp_008d_subsample_on_h8\", \"data_count\": 500, \"model_name\": \"DreamerV3 RSSM (baseline + collapsed checkpoints)\", \"seed\": 0, \"gpu_ids\": [1], \"checkpoint_path\": \"logdir/exp_063_rssm_fidelity/results.json\", \"log_path\": \"logdir/exp_063_rssm_fidelity/results.json\"}, \"conclusion\": \"success\", \"metrics\": {\"baseline_dt1_obs_mse\": 13.7, \"baseline_dt2_obs_mse\": 20.62, \"baseline_dt2_dt1_ratio_obs\": 1.505, \"baseline_dt2_dt1_ratio_reward\": 1.483, \"collapsed_dt1_obs_mse\": 26.93, \"collapsed_dt2_single_obs_mse\": 42.02, \"collapsed_dt2_single_reward_mae\": 0.146, \"collapsed_dt2_dt1_ratio_obs\": 1.56, \"collapsed_dt2_dt1_ratio_reward\": 2.695, \"collapsed_single_vs_chained_obs\": 1.138, \"collapsed_single_vs_chained_reward\": 1.926}, \"completed_at\": \"2026-05-24T19:21:37.837Z\"}, \"exp_051_stackcube_frozen_dt_emb_s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T19:30:00.000Z\", \"updated_at\": \"2026-05-24T16:53:23.046Z\", \"hypothesis\": \"Freezing dt_emb in StackCube (manipulation domain) prevents CIVO collapse, contrasting exp_049 (trained dt_emb, CIVO ve_ratio 3.27@32.5K) to establish trained-vs-frozen causal evidence in manipulation tasks. If frozen prevents CIVO → extends Walker/Cheetah frozen finding to manipulation; if not → domain-specific factors override dt_emb mechanism.\", \"parent\": \"exp_049_stackcube_civo_trigger_s0\", \"spec\": {\"command\": \"python -u dreamer.py --configs maniskill_stackcube --task maniskill_StackCube-v1 --steps 210000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --checkpoint_every 25000 --logdir logdir/exp_051_stackcube_frozen_dt_emb_s0\", \"server\": \"bjb1-40020\", \"gpu_ids\": [1], \"pid\": 305974, \"data_path\": \"ManiSkill StackCube-v1 (online RL, state obs)\", \"data_count\": 210000, \"model_name\": \"DreamerV3 (frozen dt_emb, ManiSkill StackCube)\", \"seed\": 0, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"StackCube-v1 (online eval)\", \"log_path\": \"logdir/exp_051_stackcube_frozen_dt_emb_s0.log\", \"checkpoint_path\": \"logdir/exp_051_stackcube_frozen_dt_emb_s0/checkpoint_202500.pt\"}, \"metrics\": {\"eval_final\": 45.3, \"eval_final_step\": 212500, \"eval_peak\": 45.3, \"eval_peak_step\": 212500, \"ve_ratio_final\": 0.1, \"ve_ratio_final_step\": 212500, \"ve_ratio_peak\": 4.3, \"ve_ratio_peak_step\": 42500, \"total_steps\": 222400, \"nve_classification\": \"onset_self_correcting\", \"civo_transient\": true, \"civo_sustained\": false, \"civo_transient_range\": \"22K-62K\", \"civo_self_correction\": true, \"civo_self_correction_step\": 82500, \"gate_dt_mean\": 2, \"gate_dt_variation\": false, \"eval_dip_during_civo\": 7.1, \"eval_dip_step\": 42500}, \"conclusion\": \"negative\", \"completed_at\": \"2026-05-23T08:48:40.404Z\"}, \"exp_049_stackcube_civo_trigger_s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T17:14:38.578Z\", \"updated_at\": \"2026-05-24T16:53:19.032Z\", \"hypothesis\": \"CIVO trigger 配置（trained dt_emb + subsample ON + H=8）在 ManiSkill StackCube-v1 manipulation 任务上是否也触发 CIVO。测试 CIVO 是否从 locomotion 推广到 manipulation 领域。StackCube 是多阶段任务（pick+stack）。如果触发 → 扩展跨域证据；如果不触发 → 支持 locomotion-specific scope。\", \"parent\": \"exp_048_stackcube_civo_trigger_s0\", \"spec\": {\"command\": \"python -u dreamer.py --configs maniskill_stackcube --task maniskill_StackCube-v1 --steps 210000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000 --logdir logdir/exp_049_stackcube_civo_trigger_s0\", \"server\": \"bjb1-45299\", \"gpu_ids\": [1], \"pid\": 91395, \"data_path\": \"ManiSkill StackCube-v1 (online RL, state obs)\", \"data_count\": 210000, \"model_name\": \"DreamerV3 (trained dt_emb, CIVO config, ManiSkill StackCube)\", \"seed\": 0, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"StackCube-v1 (online eval)\", \"log_path\": \"logdir/exp_049_stackcube_civo_trigger_s0/train.log\"}, \"metrics\": {\"eval_final\": 34.88, \"eval_final_step\": 212500, \"eval_peak\": 35.89, \"eval_peak_step\": 182500, \"ve_ratio_final\": 0.186, \"ve_ratio_final_step\": 212500, \"ve_ratio_peak\": 5.048, \"ve_ratio_peak_step\": 42500, \"total_steps\": 222400, \"total_episodes\": 1112, \"nve_classification\": \"onset_self_correcting\", \"civo_transient\": true, \"civo_sustained\": false, \"civo_transient_range\": \"22K-72K\", \"civo_self_correction\": true, \"civo_self_correction_step\": 112500, \"gate_dt_mean\": 2, \"gate_dt_variation\": false, \"eval_dip_during_civo\": 4.93, \"eval_dip_step\": 62500}, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_049_stackcube_civo_trigger_s0/checkpoint_202500.pt\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_049_stackcube_civo_trigger_s0/metrics.jsonl\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T04:23:01.339Z\"}, \"exp_057\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T16:49:35.310Z\", \"updated_at\": \"2026-05-24T16:50:44.968Z\", \"hypothesis\": \"Frozen dt_emb 跨 seed 可复现性验证（Walker seed=2, n=3）。当前 Walker frozen s0 NVE 0.19, s1 NVE 1.71 transient。s2 增加样本量到 n=3 验证稳健性。\", \"parent\": \"\", \"spec\": {\"command\": \"python train.py --env walker --frozen_dt_emb --seed 2\", \"server\": \"bjb1-45299\", \"data_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon\", \"data_count\": 225000, \"seed\": 2, \"model_name\": \"dreamer_frozen_dt_emb\"}, \"log_path\": \"logdir/exp_057_frozen_dt_emb_walker_s2/train.log\", \"checkpoint_path\": \"logdir/exp_057_frozen_dt_emb_walker_s2/checkpoint_225000.pt\", \"metrics\": {\"eval_return_peak\": 221.7, \"eval_return_peak_step\": 195000, \"eval_return_final\": 123.9, \"eval_return_final_step\": 215000, \"nve_peak\": 1.3, \"nve_peak_step\": 115000, \"nve_final\": 0.2, \"civo_alert\": 0, \"civo_sustained\": false, \"civo_transient\": true, \"civo_transient_range\": \"115k-145k\", \"train_steps\": 225000, \"gate_dt_mean\": 2}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-24T16:50:44.968Z\"}, \"exp_008d_civo_trigger_s4\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008d_civo_trigger_s4/latest.pt\", \"completed_at\": \"2026-05-18T05:17:45.132Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T02:02:43.972Z\", \"hypothesis\": \"Walker Walk CIVO trigger seed=4: trained dt_emb + subsample ON + H=8. 第四 seed 复现 CIVO (NVE>1.5×)，加强 Walker 因果论证的统计力度。Rebuttal 储备。\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008d_civo_trigger_s4/metrics.jsonl\", \"metrics\": {\"ve_ratio_peak\": 3.0294, \"ve_ratio_peak_step\": 105000, \"ve_ratio_final\": 3.0294, \"ve_ratio_final_step\": 105000, \"nve_peak\": 4.62, \"nve_peak_step\": 105000, \"nve_peak_note\": \"step-matched s1 baseline @105K = 0.6564\", \"nve_classification\": \"onset_collapse\"}, \"parent\": \"exp_008d_civo_trigger_s3\", \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"train_from_scratch\", \"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --gate_subsample_min_dt 1 --imag_horizon 8 --seed 4 --steps 105000 --checkpoint_every 25000 --compile False --device cuda:0 --logdir ./logdir/exp_008d_civo_trigger_s4\", \"data_count\": 0, \"data_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon\", \"eval_data\": \"dmc_walker_walk_online\", \"gpu\": \"cuda:0\", \"model_name\": \"DreamerV3-walker-civo-trigger\", \"pid\": \"715124\", \"seed\": 4, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-24T08:56:41.239Z\"}, \"exp_009b_008d_walker_s2\": {\"account\": \"root\", \"causal_conclusion\": \"Seed 2 nve transiently reached 2.05x@25K (pathological), confirming trained dt_emb reliably induces nve>1.5x (2/2 seeds). But seed 2 self-corrected (nve 2.05x→0.38x@105K, eval 141→268) while seed 1 sustained nve>1.5x across 3 consecutive checkpoints at 35K+ (1.71x→2.09x→4.12x) and collapsed (eval 167→83). Collapse is stochastic (1/2 seeds); nve>1.5x threshold (at 35K+ steps) is a reliable diagnostic marker with 4/4 separating power (trained 2/2 exceed, untrained 0/2 exceed).\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009b_008d_walker_s2/latest.pt\", \"completed_at\": \"2026-05-14T18:51:00Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-14T07:17:25.186Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-14T18:47:21.873692+00:00\"}]}, \"gpu\": \"cuda:1\", \"hypothesis\": \"CIVO onset (NVE≥1.5×) reproduces on seed=2 with identical architecture, confirming the phenomenon is systematic rather than seed-specific. Collapse outcome may be stochastic.\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_009b_008d_walker_s2.log\", \"metrics\": {\"ve_ratio_peak\": 0.5703, \"ve_ratio_peak_step\": 55000, \"ve_ratio_final\": 0.25, \"ve_ratio_final_step\": 105000, \"nve_peak\": 1.62, \"nve_peak_step\": 45000, \"nve_peak_note\": \"step-matched s1 baseline @45K = 0.331; arithmetic peak @25K=2.04x excluded (baseline<0.1)\", \"nve_classification\": \"onset_self_correcting\"}, \"notes\": \"D032: Collapse NOT reproduced in seed 2. nve peaked 2.05x@25K (transient) then self-corrected to 0.38x@105K. Eval rose to 268. Contrast: seed 1 had SUSTAINED nve>1.5x at 35K+ (1.71x→2.09x→4.12x) → collapse to 83. Key finding: nve>1.5x threshold (35K+ steps) is reliable trained dt_emb marker (2/2 seeds), but collapse is stochastic (1/2). Framing proposal submitted to Director.\", \"parent\": \"exp_008d_subsample_on_h8\", \"pid\": \"887053\", \"reproduce\": {\"code_commit\": \"09876d7080affdb0fb329e24753a46d998da9d8e\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009b_008d_walker_s2 --steps 105000 --seed 2 --compile False --device cuda:1 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8\\\"\", \"finished_at\": \"2026-05-14T18:47:20.636Z\"}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009b_008d_walker_s2 --steps 105000 --seed 2 --compile False --device cuda:1 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"gpu\": [\"cuda:1\"], \"model_name\": \"DreamerV3+FixedDt2_Subsample_H8 (gate_fixed_dt=2, gate_subsample_max_dt=2, imag_horizon=8, trained dt_embed)\", \"seed\": 2, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-24T08:56:39.471Z\"}, \"exp_009e_008d_walker_s1\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009e_008d_walker_s1/latest.pt\", \"completed_at\": \"2026-05-15T11:26:52.478Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-14T11:09:15.367Z\", \"gpu\": \"cuda:1\", \"hypothesis\": \"Walker Walk trained dt_emb + subsample ON + H=8 seed 1 — 多 seed 复现 008d delusional critic collapse，巩固 C2 统计显著性（plan_011）\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009e_008d_walker_s1/metrics.jsonl\", \"metrics\": {\"ve_ratio_peak\": 1.6663, \"ve_ratio_peak_step\": 55000, \"ve_ratio_final\": 1.03, \"ve_ratio_final_step\": 105000, \"nve_peak\": 4.13, \"nve_peak_step\": 55000, \"nve_peak_note\": \"step-matched s1 baseline @55K = 0.4035; paper onset NVE @45K = 2.09x\", \"nve_classification\": \"onset_collapse\"}, \"notes\": \"008d extended replication (same seed=1, 009e extends 008d from 55K to 105K). Eval trajectory 5K-55K identical to 008d (deterministic). Collapse confirmed at 105K: eval 131.08, nve@55K=4.12x (normalized). 65K bounce to 250 was transient, not recovery. actor_loss flipped positive @85K. Independent collapse rate = 1/2 (seed 1 collapsed, seed 2 self-corrected), NOT 2/3 — 008d and 009e are the same seed.\", \"parent\": \"exp_008d_subsample_on_h8\", \"pid\": 119108, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"N/A - training from scratch\", \"command\": \"python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009e_008d_walker_s1 --steps 105000 --seed 1 --compile False --device cuda:1 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"N/A - training experiment\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 5.43, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_009e_008d_walker_s1.log\", \"model_name\": \"DreamerV3+FixedDt2_Subsample_H8\", \"pid\": \"119108\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-15T06:01:00Z\", \"wall_clock_seconds\": 19552.5}, \"status\": \"DONE\", \"updated_at\": \"2026-05-24T08:56:37.645Z\"}, \"exp_059_walker_trained_s5\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-24T03:08:46.842Z\", \"updated_at\": \"2026-05-24T07:46:59.075Z\", \"hypothesis\": \"Walker CIVO trigger 第5个独立seed验证。当前4/4 seeds触发sustained CIVO（p=0.0625 binomial test）。如果s5也触发 → p=0.03125，达到统计显著性阈值。关联 Claim 1: CIVO reproducibility。\", \"parent\": \"exp_008d_civo_trigger_s3\", \"spec\": {\"command\": \"bash -c \\\"cd /root/autodl-tmp/event-gated-adaptive-horizon && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --gate_subsample_min_dt 1 --imag_horizon 8 --seed 5 --steps 105000 --checkpoint_every 25000 --compile False --device cuda:0 --logdir logdir/exp_059_walker_trained_s5\\\"\", \"server\": \"bjb1-45299\", \"gpu\": [\"cuda:1\"], \"pid\": \"186176\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_059_walker_trained_s5.log\", \"submitted_at\": \"2026-05-24T03:15:40.649Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 11526.3, \"gpu_hours\": 3.2}, \"server\": \"bjb1-45299\", \"gpu\": \"cuda:1\", \"pid\": \"186176\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_059_walker_trained_s5.log\", \"reproduce\": {\"command\": \"bash -c \\\"cd /root/autodl-tmp/event-gated-adaptive-horizon && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --gate_subsample_min_dt 1 --imag_horizon 8 --seed 5 --steps 105000 --checkpoint_every 25000 --compile False --device cuda:0 --logdir logdir/exp_059_walker_trained_s5\\\"\", \"code_commit\": \"fb56c860a88292ad60b6183effc1102a01205086\", \"finished_at\": \"2026-05-24T06:20:56.680Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-24T06:21:01.777871+00:00\"}]}, \"metrics\": {\"ve_ratio_peak\": 3.3075, \"ve_ratio_peak_step\": \"85K\", \"nve_peak\": 4.72, \"nve_peak_note\": \"step-matched s1 baseline @85K = 0.7007\", \"nve_classification\": \"onset_collapse\", \"nve_classification_note\": \"Reclassified from onset_self_correcting: NVE self-corrected but eval=95.8 (10.5% of baseline 913) indicates irreversible policy damage. Collapse†.\", \"nve_final\": 1.22, \"nve_final_note\": \"0.8/0.656 (step-matched s1 baseline @105K)\", \"eval_final\": 95.8, \"eval_baseline\": 913, \"eval_pct_baseline\": \"10.5%\"}, \"conclusion\": \"success\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_059_walker_trained_s5/checkpoint.pt\", \"completed_at\": \"2026-05-24T06:27:46.992Z\", \"notes\": \"CIVO-positive under step-matched NVE (peak ≈ 5.0×). Self-correcting outcome (ve_ratio 3.3@85K → 0.8@105K in ~10K steps). Supports 5/5 Walker trained CIVO onset. Gate locked at dt=2 throughout (entropy=0).\"}, \"exp_057_frozen_dt_emb_walker_s2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"retry_count\": 0, \"created_at\": \"2026-05-23T15:25:00.000Z\", \"updated_at\": \"2026-05-24T02:17:41.318Z\", \"hypothesis\": \"Frozen dt_emb 跨 seed 可复现性验证（Walker n=3）。当前 Walker frozen s0 NVE 0.19, s1 NVE 1.71 transient。s2 增加样本量到 n=3，如果 0 CIVO → frozen 在 Walker 上稳健；如果出现持续 CIVO → 样本不足。\", \"parent\": \"exp_042_frozen_dt_emb_walker\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 2 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --checkpoint_every 25000 --logdir logdir/exp_057_frozen_dt_emb_walker_s2\", \"server\": \"bjb1-45299\", \"gpu_ids\": [1], \"pid\": 157775, \"data_path\": \"dmc_walker_walk\", \"data_count\": 210000, \"model_name\": \"DreamerV3 (frozen dt_emb, Walker s2)\", \"seed\": 2, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"dmc_walker_walk (online eval)\", \"log_path\": \"logdir/exp_057_frozen_dt_emb_walker_s2/train.log\", \"checkpoint_path\": \"logdir/exp_057_frozen_dt_emb_walker_s2/checkpoint_225000.pt\"}, \"completed_at\": \"2026-05-23T23:30:00.000Z\", \"metrics\": {\"total_steps\": 225000, \"ve_ratio_peak\": 1.283, \"ve_ratio_peak_step\": 115000, \"ve_ratio_final\": 0.177, \"ve_ratio_final_step\": 215000, \"nve_peak\": 1.88, \"nve_peak_step\": 115000, \"nve_classification\": \"transient\", \"eval_return_final\": 123.94, \"eval_return_final_step\": 215000, \"eval_return_peak\": 221.72, \"eval_return_peak_step\": 195000}}, \"exp_058_frozen_dt_emb_cheetah_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T18:10:49.773Z\", \"updated_at\": \"2026-05-24T00:30:00.000Z\", \"hypothesis\": \"Cheetah frozen dt_emb 跨 seed 可复现性验证。exp_046 (s0) 显示 frozen 将 NVE 从 ~70-108（trained）降至 1.35。s1 验证阻止效应是否可复现。如果 s1 也阻止 → Cheetah frozen n=2 增强极端 CIVO 场景下 frozen diagnostic 的统计基础。\", \"parent\": \"exp_046_frozen_dt_emb_cheetah\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 210000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --checkpoint_every 25000 --logdir logdir/exp_058_frozen_dt_emb_cheetah_s1\", \"server\": \"bjb1-45299\", \"gpu_ids\": [0], \"pid\": 164830, \"data_path\": \"dmc_cheetah_run\", \"data_count\": 210000, \"model_name\": \"DreamerV3 (frozen dt_emb, Cheetah s1)\", \"seed\": 1, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"dmc_cheetah_run (online eval)\", \"log_path\": \"logdir/exp_058_frozen_dt_emb_cheetah_s1/train.log\", \"checkpoint_path\": \"logdir/exp_058_frozen_dt_emb_cheetah_s1/checkpoint_225000.pt\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-24T00:30:00.000Z\", \"metrics\": {\"total_steps\": 224000, \"ve_ratio_peak\": 0.231, \"ve_ratio_peak_step\": 45000, \"ve_ratio_final\": 0.107, \"ve_ratio_final_step\": 215000, \"eval_return_final\": 80.46, \"eval_return_final_step\": 215000, \"eval_return_peak\": 191.74, \"eval_return_peak_step\": 25000, \"nve_peak\": 0.78, \"nve_peak_step\": 45000, \"nve_classification\": \"no_civo\", \"note\": \"Cheetah frozen s1. NVE=0.78× (raw 0.231 / baseline 0.296 @45K). Cheetah frozen n=2: s0 NVE=1.35, s1 NVE=0.78 — both clean, frozen 稳健阻止 extreme CIVO (trained NVE 70-108).\"}}, \"exp_056_peginsertion_frozen_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T09:02:23.683Z\", \"updated_at\": \"2026-05-24T00:00:00.000Z\", \"hypothesis\": \"D143 混合机制假说验证——PegInsertion frozen dt_emb 跨 seed 可复现性。exp_053 (s0) 显示 frozen 在 82.5K 回落到 1.82 而 trained 攀升到 10.05，s1 验证这个分叉是否可复现。如果 s1 也回落 → frozen 稳健阻止 dt_emb 放大；如果不回落 → seed-dependent。\", \"parent\": \"exp_053_peginsertion_frozen_s0\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 MUJOCO_EGL_DEVICE_ID=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python -u dreamer.py --configs maniskill_peginsertion --task maniskill_PegInsertionSide-v1 --steps 210000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --checkpoint_every 25000 --logdir logdir/exp_056_peginsertion_frozen_s1\", \"server\": \"bjb1-40020\", \"gpu_ids\": [1], \"pid\": 346430, \"data_path\": \"ManiSkill PegInsertionSide-v1 (online RL, state obs)\", \"data_count\": 210000, \"model_name\": \"DreamerV3 (frozen dt_emb, fixed dt=2, ManiSkill PegInsertion s1)\", \"seed\": 1, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"PegInsertionSide-v1 (online eval)\", \"log_path\": \"logdir/exp_056_peginsertion_frozen_s1/train.log\", \"checkpoint_path\": \"logdir/exp_056_peginsertion_frozen_s1/checkpoint_202500.pt\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-24T00:00:00.000Z\", \"metrics\": {\"total_steps\": 222500, \"ve_ratio_peak\": 11.321, \"ve_ratio_peak_step\": 82500, \"ve_ratio_final\": 1.193, \"ve_ratio_final_step\": 212500, \"eval_return_final\": 4.37, \"eval_return_final_step\": 212500, \"eval_return_peak\": 24.42, \"eval_return_peak_step\": 132500, \"nve_classification\": \"burst\", \"note\": \"Ordering reversal vs s0 confirms D146 seed-dependent noise. Frozen s1 burst 11.32 > trained s1 peak 3.08 — frozen does NOT suppress ManiSkill transients.\", \"ve_ratio_trajectory\": {\"12500\": 0.316, \"22500\": 0.975, \"32500\": 1.839, \"42500\": 1.966, \"52500\": 5.422, \"62500\": 4.047, \"72500\": 8.408, \"82500\": 11.321, \"92500\": 3.724, \"102500\": 3.034, \"112500\": 2.204, \"122500\": 2.425, \"132500\": 0.842, \"142500\": 2.194, \"152500\": 2.203, \"162500\": 0.651, \"172500\": 1.085, \"182500\": 1.07, \"192500\": 0.467, \"202500\": 0.708, \"212500\": 1.193}}}, \"exp_055_peginsertion_civo_trigger_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-23T08:50:00.000Z\", \"updated_at\": \"2026-05-23T23:38:30.000Z\", \"hypothesis\": \"PegInsertion CIVO 跨 seed 可复现性验证。exp_050 (s0) 显示持续性 CIVO（ve_ratio_peak 10.05×@82.5K，最终自修复到 0.379@212.5K）。如果 s1 也触发持续 CIVO → PegInsertion CIVO 可复现；如果不触发 → seed-specific 异常。\", \"parent\": \"exp_050_peginsertion_civo_trigger_s0\", \"spec\": {\"command\": \"python -u dreamer.py --configs maniskill_peginsertion --task maniskill_PegInsertionSide-v1 --steps 210000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000 --logdir logdir/exp_055_peginsertion_civo_trigger_s1\", \"server\": \"bjb1-40020\", \"gpu_ids\": [0], \"pid\": 345223, \"data_path\": \"ManiSkill PegInsertionSide-v1 (online RL, state obs)\", \"data_count\": 210000, \"model_name\": \"DreamerV3 (trained dt_emb, CIVO config, PegInsertion)\", \"seed\": 1, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"PegInsertionSide-v1 (online eval)\", \"log_path\": \"logdir/exp_055_peginsertion_civo_trigger_s1/train.log\"}, \"ve_ratio_peak\": \"3.08@92500\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T23:38:25.428Z\", \"metrics\": {\"total_steps\": 222400, \"ve_ratio_peak\": 3.08, \"ve_ratio_peak_step\": 92500, \"ve_ratio_final\": 0.498, \"ve_ratio_final_step\": 212500, \"eval_return_final\": 11.44, \"eval_return_final_step\": 212500, \"eval_return_peak\": 24.05, \"eval_return_peak_step\": 112500, \"nve_classification\": \"transient\", \"civo_triggered\": true, \"civo_self_corrected\": \"partial\", \"note\": \"CIVO triggered (peak 3.08@92.5K, less severe than s0=10.05). Partial self-correction to 0.498. PegInsertion trained cross-seed: s0=10.05, s1=3.08 — severity seed-dependent.\", \"ve_ratio_trajectory\": {\"12500\": 0.19, \"22500\": 0.81, \"32500\": 1.35, \"42500\": 2.0, \"52500\": 2.39, \"62500\": 2.85, \"72500\": 2.28, \"82500\": 2.48, \"92500\": 3.08, \"102500\": 2.51, \"112500\": 0.91, \"122500\": 1.21, \"132500\": 1.36, \"142500\": 0.75, \"152500\": 0.55, \"162500\": 1.17, \"172500\": 0.96, \"182500\": 0.94, \"192500\": 0.9, \"202500\": 0.73, \"212500\": 0.5}}, \"checkpoint_path\": \"logdir/exp_055_peginsertion_civo_trigger_s1/checkpoint_222500.pt\"}, \"exp_054_pickcube_frozen_s0\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"retry_count\": 0, \"created_at\": \"2026-05-23T07:47:24.310Z\", \"updated_at\": \"2026-05-23T18:08:00.000Z\", \"hypothesis\": \"PickCube frozen dt_emb baseline (fixed_dt=2, subsample ON, H=8)。验证 CIVO frozen 配置在最简单 manipulation task 上的表现。如果 eval return 稳定高于 random → frozen dt_emb 在 easy task 上不影响学习；如果性能差 → frozen dt_emb 有问题。\", \"spec\": {\"command\": \"python -u dreamer.py --configs defaults maniskill --task maniskill_PickCube-v1 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --seed 0 --steps 210000 --compile False --device cuda:0 --checkpoint_every 25000 --logdir logdir/exp_054_pickcube_frozen_s0\", \"server\": \"bjb1-45299\", \"gpu_ids\": [0], \"pid\": 133956, \"data_path\": \"ManiSkill PickCube-v1 (online RL, state obs)\", \"data_count\": 210000, \"model_name\": \"DreamerV3 (frozen dt_emb, CIVO config, ManiSkill PickCube)\", \"seed\": 0, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"PickCube-v1 (online eval)\", \"log_path\": \"logdir/exp_054_pickcube_frozen_s0/metrics.jsonl\", \"checkpoint_path\": \"logdir/exp_054_pickcube_frozen_s0/checkpoint.ckpt\"}, \"ve_ratio_peak\": \"8.81@62500\", \"eval_final\": 10.26, \"eval_final_step\": 212500, \"ve_ratio_final\": 0.583, \"ve_ratio_final_step\": 212500}, \"exp_053_peginsertion_frozen_s0\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"retry_count\": 0, \"created_at\": \"2026-05-23T04:23:10.381Z\", \"updated_at\": \"2026-05-23T15:00:00.000Z\", \"hypothesis\": \"Freezing dt_emb in PegInsertionSide-v1 (contact-rich manipulation) prevents CIVO while maintaining task performance, establishing that dt_emb freezing generalizes as CIVO prevention across task domains. If frozen prevents CIVO here → extends StackCube/locomotion frozen finding to insertion tasks; if CIVO still appears → freezing insufficient for contact-rich tasks.\", \"parent\": \"exp_050_peginsertion_civo_trigger_s0\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 MUJOCO_EGL_DEVICE_ID=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python -u dreamer.py --configs maniskill_peginsertion --task maniskill_PegInsertionSide-v1 --steps 210000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --checkpoint_every 25000 --logdir logdir/exp_053_peginsertion_frozen_s0\", \"server\": \"bjb1-45299\", \"gpu_ids\": [1], \"pid\": 123495, \"data_path\": \"ManiSkill PegInsertionSide-v1 (online RL, state obs)\", \"data_count\": 210000, \"model_name\": \"DreamerV3 (frozen dt_emb, fixed dt=2, ManiSkill PegInsertion)\", \"seed\": 0, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"PegInsertionSide-v1 (online eval)\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_053_peginsertion_frozen_s0.log\", \"checkpoint_path\": \"logdir/exp_053_peginsertion_frozen_s0/checkpoint.ckpt\"}, \"ve_ratio_peak\": \"8.10@52500\", \"eval_final\": 5.89, \"ve_ratio_final\": 0.202, \"ve_ratio_final_step\": 212500}, \"exp_050_peginsertion_civo_trigger_s0\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T18:38:33.441Z\", \"updated_at\": \"2026-05-23T08:51:11.592Z\", \"hypothesis\": \"Fixed-dt=2 gate with CIVO trigger on PegInsertionSide-v1 (contact-rich manipulation) will demonstrate that temporal abstraction benefits extend beyond locomotion to precise insertion tasks, where event-gated horizons can skip redundant approach phases while preserving fine-grained control near contact.\", \"spec\": {\"command\": \"LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs maniskill_peginsertion --task maniskill_PegInsertionSide-v1 --steps 210000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000 --logdir logdir/exp_050_peginsertion_civo_trigger_s0\", \"server\": \"bjb1-40020\", \"data_path\": \"ManiSkill PegInsertionSide-v1 (state obs)\", \"data_count\": 210000, \"model_name\": \"DreamerV3 + CIVO trigger (gate_fixed_dt=2)\", \"seed\": 0, \"pid\": 304736, \"gpu_ids\": [0], \"log_path\": \"logdir/exp_050_peginsertion_civo_trigger_s0/train.log\", \"checkpoint_path\": \"logdir/exp_050_peginsertion_civo_trigger_s0\"}, \"metrics\": {\"ve_ratio_peak\": 10.05, \"ve_ratio_peak_step\": 82500, \"ve_ratio_final\": 0.379, \"ve_ratio_final_step\": 212500, \"civo_self_corrected\": true, \"civo_correction_delay_steps\": 130000, \"eval_final\": 20.86, \"eval_final_step\": 212500, \"eval_peak\": 20.86, \"eval_peak_step\": 212500, \"total_steps\": 222400}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-23T08:30:00.000Z\"}, \"exp_052_stackcube_civo_trigger_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T21:26:49.825Z\", \"updated_at\": \"2026-05-23T07:45:47.966Z\", \"hypothesis\": \"StackCube CIVO trigger (trained dt_emb + subsample ON + H=8) 跨 seed 可复现性验证。exp_049 (s0) 在 32.5K 步触发 CIVO（ve_ratio 3.27）。如果 s1 也触发 → CIVO 在 manipulation 领域可复现，非 seed-specific；如果不触发 → seed-dependent，需更多 seeds。\", \"parent\": \"exp_049_stackcube_civo_trigger_s0\", \"spec\": {\"command\": \"python -u dreamer.py --configs maniskill_stackcube --task maniskill_StackCube-v1 --steps 210000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000 --logdir logdir/exp_052_stackcube_civo_trigger_s1\", \"server\": \"bjb1-45299\", \"gpu_ids\": [0], \"pid\": 103781, \"data_path\": \"ManiSkill StackCube-v1 (online RL, state obs)\", \"data_count\": 210000, \"model_name\": \"DreamerV3 (trained dt_emb, CIVO config, ManiSkill StackCube)\", \"seed\": 1, \"checkpoint_source\": \"N/A (training from scratch)\", \"eval_data\": \"StackCube-v1 (online eval)\", \"log_path\": \"logdir/exp_052_stackcube_civo_trigger_s1/train.log\"}, \"metrics\": {\"eval_final\": 29.458, \"eval_final_step\": 212500, \"eval_peak\": 39.873, \"eval_peak_step\": 162500, \"ve_ratio_final\": 0.133, \"ve_ratio_final_step\": 212500, \"ve_ratio_peak\": 4.67, \"ve_ratio_peak_step\": 52500, \"total_steps\": 222400}, \"conclusion\": \"success\", \"checkpoint_path\": \"logdir/exp_052_stackcube_civo_trigger_s1/checkpoint_202500.pt\", \"log_path\": \"logdir/exp_052_stackcube_civo_trigger_s1/metrics.jsonl\", \"completed_at\": \"2026-05-23T07:45:47.966Z\"}, \"exp_048_cheetah_civo_extension\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T16:30:40.050Z\", \"updated_at\": \"2026-05-22T21:18:00.000Z\", \"hypothesis\": \"Cheetah CIVO (NVE 70.64, far more severe than Walker 1.5-4.9) is too severe for spontaneous recovery. Walker CIVO self-corrected in exp_045 (ve_ratio 4.91→0.05 over 170K steps). If Cheetah does NOT self-correct → severity determines recoverability narrative. If it does → CIVO is universally transient regardless of severity.\", \"parent\": \"exp_010b_cheetah_civo_trigger_s0\", \"spec\": {\"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 300000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000 --logdir logdir/exp_048_cheetah_civo_extension\", \"server\": \"bjb1-45299\", \"gpu_ids\": [0], \"pid\": 88654, \"data_path\": \"dmc_cheetah_run (online RL)\", \"data_count\": 300000, \"model_name\": \"DreamerV3 (trained dt_emb, CIVO config, Cheetah)\", \"seed\": 0, \"checkpoint_source\": \"exp_010b_cheetah_civo_trigger_s0/latest.pt (step 105K, NVE=70.64)\", \"eval_data\": \"dmc_cheetah_run (online eval)\", \"log_path\": \"logdir/exp_048_cheetah_civo_extension/train.log\"}, \"metrics\": {\"eval_final\": 23.4, \"eval_final_step\": 302000, \"eval_peak\": 32.8, \"eval_peak_step\": 252000, \"ve_ratio_initial\": 46.3, \"ve_ratio_peak\": 24.112, \"ve_ratio_peak_step\": 162000, \"ve_ratio_final\": 1.803, \"nve_initial\": 70.64, \"nve_peak_secondary\": 36.76, \"nve_final\": 2.75, \"total_steps\": 312000, \"civo_self_corrected\": false, \"civo_correction_pct\": 96, \"secondary_burst_step\": 152000, \"secondary_burst_nve\": 36.47, \"gate_collapsed\": true}, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_048_cheetah_civo_extension/checkpoint_300000.pt\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_048_cheetah_civo_extension/train.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T21:18:00.000Z\"}, \"exp_047_frozen_dt_emb_walker_s1\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T11:03:31.428Z\", \"updated_at\": \"2026-05-22T19:01:30.894Z\", \"hypothesis\": \"Frozen dt_emb Walker seed 1: 增强 exp_042 (s0, NVE=0.19) 的统计力度。 如果 s1 也 NVE<1.5 且无持续 CIVO → frozen dt_emb mitigation 跨 seed robust。\", \"parent\": \"exp_042_frozen_dt_emb_walker\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --checkpoint_every 25000 --logdir logdir/exp_047_frozen_dt_emb_walker_s1\", \"server\": \"bjb1-40020\", \"data_path\": \"dmc_walker_walk\", \"data_count\": 210000, \"model_name\": \"dreamer_gated_frozen_dt_emb\", \"seed\": 1, \"eval_data\": \"dmc_walker_walk (online eval)\", \"checkpoint_source\": \"N/A (training from scratch)\"}, \"reproduce\": {\"finished_at\": \"2026-05-22T18:56:07.648Z\"}, \"metrics\": {\"eval_final\": 144.22, \"eval_final_step\": 215000, \"eval_peak\": 408.79, \"eval_peak_step\": 125000, \"ve_ratio_peak\": 1.099, \"ve_ratio_peak_step\": 75000, \"ve_ratio_final\": 0.277, \"nve_peak\": 1.71, \"nve_peak_step\": 95000, \"nve_final_105k\": 0.56, \"total_steps\": 225000}, \"checkpoint_path\": \"logdir/exp_047_frozen_dt_emb_walker_s1/checkpoint_225000.pt\", \"log_path\": \"logdir/exp_047_frozen_dt_emb_walker_s1/train.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T19:01:30.894Z\"}, \"exp_046_frozen_dt_emb_cheetah\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T10:41:53.934Z\", \"updated_at\": \"2026-05-22T18:32:34.105Z\", \"server\": \"bjb1-40020\", \"gpu\": \"cuda:0\", \"account\": \"root\", \"hypothesis\": \"Cross-environment validation: frozen dt_emb (random init, requires_grad=False) prevents CIVO on Cheetah Run, extending the Walker Walk finding (exp_042 NVE=0.19, exp_015b NVE=0.47) to a second environment. Cheetah has stronger CIVO (NVE 8.27-70.64× in exp_010b) so this is a harder test of the frozen mitigation.\", \"parent\": \"exp_042_frozen_dt_emb_walker\", \"reproduce\": {\"server\": \"bjb1-40020\", \"gpu\": \"cuda:0\", \"started_at\": \"2026-05-22T10:42:06.985Z\", \"finished_at\": \"2026-05-22T18:27:00.000Z\"}, \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 210000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --checkpoint_every 25000 --logdir logdir/exp_046_frozen_dt_emb_cheetah\", \"server\": \"bjb1-40020\", \"seed\": 0, \"model_name\": \"dreamerv3-cheetah-frozen-dt-emb\", \"data_path\": \"dmc_cheetah_run\", \"data_count\": 210000, \"eval_data\": \"dmc_cheetah_run (online eval)\", \"checkpoint_source\": \"N/A (training from scratch)\"}, \"metrics\": {\"eval_final\": 150.5, \"eval_peak\": 207.4, \"eval_peak_step\": 145000, \"ve_ratio_peak\": 0.4, \"ve_ratio_final\": 0.1, \"nve_peak\": 1.35, \"nve_peak_step\": 45000, \"nve_final\": 0.17, \"total_steps\": 224000, \"civo_alert_count\": 0}, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_046_frozen_dt_emb_cheetah/checkpoint_225000.pt\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_046_frozen_dt_emb_cheetah/train.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T18:31:00.933Z\"}, \"exp_044_gradient_stop_walker\": {\"status\": \"DONE\", \"retry_count\": 0, \"created_at\": \"2026-05-22T09:03:45.656Z\", \"updated_at\": \"2026-05-22T16:08:22.684Z\", \"hypothesis\": \"Reviewer Q2 直接回应：gradient stopping（detach dt_emb gradient to reward head）是否能阻断 CIVO 的 reward-critic feedback loop。基于 008d 配置（trained dt_emb + subsample ON + H=8），仅阻断 dt_emb→reward_head 梯度路径。如果 gradient stopping 有效（NVE<1.5）→ 最简干预方案成立，推翻我们之前 SGS 1/17 的结论（SGS 阻断所有梯度 vs 这里只阻断 dt_emb→reward 路径）。如果无效 → 直接证据证明 gradient-level intervention 不足以解决 CIVO，支撑 Intervention Hierarchy 中 gradient-level 最弱的结论。\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --reward_dt_emb_detach True --logdir logdir/exp_044_gradient_stop_walker\\\"\", \"server\": \"bjb1-45299\", \"gpu\": [\"cuda:1\"], \"pid\": \"68371\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_044_gradient_stop_walker.log\", \"submitted_at\": \"2026-05-22T09:08:10.295Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"DMC Walker Walk\", \"data_count\": 210000, \"model_name\": \"DreamerV3 + reward_dt_emb_detach\", \"seed\": 0, \"checkpoint_source\": \"N/A - training from scratch\", \"eval_data\": \"dmc_walker_walk\", \"wall_clock_seconds\": 25212.4, \"gpu_hours\": 7.0}, \"reproduce\": {\"finished_at\": \"2026-05-22T16:04:32.082Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-22T16:04:36.793540+00:00\"}]}, \"metrics\": {\"eval_final\": 538.6, \"eval_peak\": 561.2, \"eval_peak_step\": 185000, \"eval_civo_trough\": 44.3, \"eval_civo_trough_step\": 95000, \"ve_ratio_peak\": 4.4, \"ve_ratio_peak_step\": 95000, \"ve_ratio_final\": 0.1, \"civo_onset_step\": 85000, \"civo_resolved_step\": 125000, \"civo_duration_steps\": 40000, \"total_steps\": 224000, \"pre_civo_peak\": 545.6, \"pre_civo_peak_step\": 75000}, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_044_gradient_stop_walker/latest.pt\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_044_gradient_stop_walker.log\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T16:08:22.684Z\"}, \"exp_045_treatment_extension_008d_s3\": {\"created_at\": \"2026-05-22T09:40:52.894Z\", \"updated_at\": \"2026-05-22T15:41:43.036Z\", \"status\": \"DONE\", \"retry_count\": 0, \"hypothesis\": \"CIVO-triggering config (trained dt_emb + subsample ON + H=8) that already exhibited CIVO at 112K will show sustained or worsening value overestimation when extended to 300K, providing temporal dynamics data for the treatment extension analysis (Reviewer Q: does CIVO self-correct or persist?)\", \"parent\": \"exp_008d_civo_trigger_s3\", \"spec\": {\"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 300000 --seed 3 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000 --logdir logdir/exp_045_treatment_extension_008d_s3\", \"server\": \"bjb1-45299\", \"gpu_ids\": [0], \"pid\": \"70945\", \"data_path\": \"dmc_walker_walk (online RL)\", \"data_count\": 300000, \"model_name\": \"DreamerV3 (trained dt_emb, CIVO config)\", \"seed\": 3, \"checkpoint_source\": \"exp_008d_civo_trigger_s3/latest.pt (step 112K)\", \"eval_data\": \"dmc_walker_walk (online eval, same as training env)\", \"log_path\": \"logdir/exp_045_treatment_extension_008d_s3/train.log\"}, \"conclusion\": \"success\", \"metrics\": {\"eval_final\": 867.6, \"eval_peak\": 869.7, \"eval_peak_step\": 242000, \"nve_peak\": 4.91, \"nve_peak_step\": 132000, \"nve_final\": 0.052, \"ve_ratio_final\": 0.052, \"total_steps\": 312000, \"civo_alerts\": 0, \"civo_self_corrected\": true, \"civo_correction_step\": 142000, \"eval_trajectory\": {\"112000\": 58.5, \"122000\": 41.8, \"132000\": 35.1, \"142000\": 350.2, \"152000\": 646.4, \"162000\": 482.3, \"172000\": 600.4, \"182000\": 600.5, \"192000\": 699.5, \"202000\": 684.3, \"212000\": 758.6, \"222000\": 744.6, \"232000\": 745.4, \"242000\": 869.7, \"252000\": 721.6, \"262000\": 820.6, \"272000\": 716.2, \"282000\": 755.6, \"292000\": 843, \"302000\": 867.6}, \"ve_ratio_trajectory\": {\"122000\": 4.77, \"132000\": 4.91, \"142000\": 0.43, \"152000\": 0.21, \"162000\": 0.25, \"172000\": 0.18, \"182000\": 0.16, \"192000\": 0.13, \"202000\": 0.12, \"212000\": 0.1, \"222000\": 0.1, \"232000\": 0.09, \"242000\": 0.07, \"252000\": 0.08, \"262000\": 0.07, \"272000\": 0.08, \"282000\": 0.07, \"292000\": 0.06, \"302000\": 0.05}}, \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_045_treatment_extension_008d_s3/checkpoint_302000.pt\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_045_treatment_extension_008d_s3/train.log\", \"completed_at\": \"2026-05-22T15:41:43.036Z\"}, \"exp_043_008f_walker_s1\": {\"created_at\": \"2026-05-22T02:35:37.558Z\", \"hypothesis\": \"Plan_012 / Claim C2 seed 1：复现 008f 因果控制（dt_embed_dim=0, subsample ON, H=8）。目前只有 seed 0 数据。如果 s1 也显示无 CIVO → 确认 dt_emb absence prevents CIVO 是 robust 的跨 seed 结论，支撑因果链 \\\"trained dt_emb → CIVO\\\"。\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 1 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0 --logdir logdir/exp_043_008f_walker_s1\\\"\", \"data_count\": 210000, \"data_path\": \"DMC Walker Walk\", \"gpu\": [\"cuda:1\"], \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_043_008f_walker_s1\", \"model_name\": \"DreamerV3 (no dt_emb, 008f control)\", \"pid\": \"250627\", \"seed\": 1, \"server\": \"bjb1-40020\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T10:38:36.474Z\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_043_008f_walker_s1/latest.pt\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_043_008f_walker_s1\", \"metrics\": {\"eval_final\": 673.73, \"eval_peak\": 673.73, \"eval_peak_step\": 215000, \"nve_peak\": 0.808, \"nve_peak_step\": 105000, \"nve_final\": 0.123, \"civo_alert\": false, \"total_steps\": 224000, \"gate_dt_2_frac\": 1, \"gate_entropy\": 0, \"note\": \"No CIVO (peak NVE 0.808, well below 1.5). Gate fixed at dt=2. Seed 1 replicates seed 0 finding: dt_emb absence prevents CIVO.\"}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T10:38:36.474Z\"}, \"exp_042_frozen_dt_emb_walker\": {\"created_at\": \"2026-05-22T02:13:59.183Z\", \"hypothesis\": \"dt_embedding training (not its mere existence) is a necessary condition for CIVO collapse. Freezing dt_emb (random init, requires_grad=False) should prevent the reward-value divergence observed in exp_008d with trained dt_emb.\", \"parent\": \"\", \"retry_count\": 0, \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True --logdir logdir/exp_042_frozen_dt_emb_walker\\\"\", \"data_count\": 210000, \"data_path\": \"DMC Walker Walk\", \"gpu\": [\"cuda:0\"], \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_042_frozen_dt_emb_walker\", \"model_name\": \"DreamerV3 + frozen dt_emb\", \"pid\": \"251336\", \"seed\": 0, \"server\": \"bjb1-40020\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T10:29:26.337Z\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_042_frozen_dt_emb_walker/latest.pt\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_042_frozen_dt_emb_walker\", \"metrics\": {\"eval_final\": 612.45, \"eval_peak\": 682.38, \"eval_peak_step\": 205000, \"nve_peak\": 0.194, \"nve_final\": 0.051, \"civo_alert\": false, \"total_steps\": 224000, \"total_train_episodes\": 224}, \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T10:29:26.337Z\"}, \"exp_040_wide_dual_critic_cheetah\": {\"created_at\": \"2026-05-21T19:50:49.909Z\", \"hypothesis\": \"Cheetah dual-critic seed 1：exp_034 (s0) 显示 dual-critic 在 Cheetah 上 NVE 1.8, eval 97.5（部分恢复 31%）。s1 确认此 pattern 是否 robust。如果 s1 也部分恢复 → Cheetah dual-critic 效果一致但弱于 Walker；如果 s1 完全不恢复 → s0 的部分恢复是偶发。\", \"parent\": \"exp_032_dual_critic_walker\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 210000 --seed 1 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dual_critic True --logdir logdir/exp_040_wide_dual_critic_cheetah\\\"\", \"gpu\": [\"cuda:0\"], \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_040_wide_dual_critic_cheetah.log\", \"pid\": \"52397\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-21T19:51:11.519Z\", \"submitted_via\": \"submit_training_job\", \"seed\": 1, \"wall_clock_seconds\": 49438.9, \"gpu_hours\": 13.73}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T09:37:44.547Z\", \"reproduce\": {\"finished_at\": \"2026-05-22T09:35:07.693Z\"}, \"failure_reason\": \"EXIT_CODE=1 (generic error — check log tail)\", \"conclusion\": \"success\", \"completed_at\": \"2026-05-22T09:35:10.404Z\", \"extra\": {\"hook_events\": [{\"event\": \"on_failed\", \"action\": \"agent\", \"ts\": \"2026-05-22T09:35:14.583680+00:00\"}]}}, \"exp_041_dual_critic_walker_s3\": {\"created_at\": \"2026-05-21T19:50:54.290Z\", \"hypothesis\": \"D128 推导：exp_038 s2 出现非 CIVO 崩溃 (eval 354→121, NVE≤0.3)，当前 collapse 频率 1/3。s3 确定崩溃是偶发 (1/4) 还是系统性 (2/4)。如果 s3 正常 → 非 CIVO 崩溃为低频偶发事件，dual-critic CIVO prevention 仍 robust；如果 s3 也崩 → 50% 系统性问题需进一步诊断。\", \"parent\": \"exp_032_dual_critic_walker\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 3 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dual_critic True --logdir logdir/exp_041_dual_critic_walker_s3\\\"\", \"gpu\": [\"cuda:1\"], \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_041_dual_critic_walker_s3.log\", \"pid\": \"51103\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-22T02:38:20.728Z\", \"submitted_via\": \"submit_training_job\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_041_dual_critic_walker_s3/checkpoint.pt\", \"checkpoint_source\": \"N/A - training from scratch\", \"eval_data\": \"dmc_walker_walk\", \"wall_clock_seconds\": 23112.0, \"gpu_hours\": 6.42}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T09:04:44.715Z\", \"reproduce\": {\"finished_at\": \"2026-05-22T09:00:53.721Z\"}, \"extra\": {\"hook_events\": [{\"event\": \"on_complete\", \"action\": \"agent\", \"ts\": \"2026-05-22T09:00:58.393731+00:00\"}]}, \"conclusion\": \"success\", \"metrics\": {\"eval_return_peak\": 761.1, \"eval_return_final\": 544, \"eval_return_peak_step\": 165000, \"nve_peak\": 1.5, \"nve_final\": 0.1, \"civo_prevented\": true, \"gate_dt_2_frac\": 1, \"non_civo_collapse\": false, \"steps\": 215000, \"note\": \"CIVO prevented (NVE≤1.5), no non-CIVO collapse. Eval stays 486-761 after peak. Non-CIVO collapse rate confirmed 1/4 (only s2).\"}, \"completed_at\": \"2026-05-22T09:03:32.751Z\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_041_dual_critic_walker_s3/latest.pt\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_041_dual_critic_walker_s3.log\"}, \"exp_039_narrow_dual_critic_walker_s1\": {\"completed_at\": \"2026-05-22T02:35:33.617Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-21T16:31:40.055Z\", \"hypothesis\": \"Narrow dual-critic Walker seed 1: 验证 exp_035 (s0, eval 697.8) 的 CIVO recovery 发现是否跨 seed 一致。如果 s1 也展示 recovery → narrow dual-critic (min operation alone) 驱动 recovery 是 robust 的；如果不 recover → s0 的 recovery 是偶发事件。\", \"metrics\": {\"civo_recovery\": true, \"eval_return_final\": 592.7, \"note\": \"Narrow dual Walker s1: CIVO triggered then recovered. s0=697.8, s1=592.7, mean≈645. Recovery 2/2.\", \"nve_peak\": 2.19, \"recovery_confirmed\": true}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_039_narrow_dual_critic_walker_s1/latest.pt\", \"checkpoint_source\": \"N/A - training from scratch\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 1 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --narrow_dual_critic True --logdir logdir/exp_039_narrow_dual_critic_walker_s1\\\"\", \"eval_data\": \"N/A - training experiment\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 10.06, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_039_narrow_dual_critic_walker_s1.log\", \"pid\": \"198771\", \"server\": \"bjb1-40020\", \"submitted_at\": \"2026-05-21T16:31:39.634Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 36234.0}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T02:35:33.617Z\"}, \"exp_038_dual_critic_walker_s2\": {\"completed_at\": \"2026-05-22T02:11:36.842Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-21T12:18:35.293Z\", \"hypothesis\": \"Third seed (s2) for Walker dual-critic CIVO prevention. s0 (eval 787.7) and s1 (eval 551.8) both showed CIVO prevention (NVE≤1.1). Third datapoint enables IQM statistical reporting. If 3/3 CIVO prevented → robust evidence for Prevention mechanism in medium-severity CIVO environments.\", \"metrics\": {\"civo_alert\": 0, \"civo_prevented\": true, \"eval_return_collapse\": 99.6, \"eval_return_collapse_step\": 175000, \"eval_return_final\": 120.9, \"eval_return_peak\": 354, \"eval_return_peak_step\": 155000, \"gate_dt_2_frac\": 1, \"non_civo_collapse\": true, \"note\": \"CIVO prevented (NVE≤0.3) but non-CIVO eval collapse at 175k (354→99.6). Different failure mode from value overestimation.\", \"nve_final\": 0.248, \"nve_peak\": 0.3, \"steps\": 224000}, \"parent\": \"exp_032_dual_critic_walker\", \"reproduce\": {\"finished_at\": \"2026-05-22T02:07:51.177Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_038_dual_critic_walker_s2/latest.pt\", \"checkpoint_source\": \"N/A - training from scratch\", \"command\": \"bash -c \\\"...dual_critic walker s2...\\\"\", \"data_count\": 210000, \"data_path\": \"DMC Walker Walk\", \"eval_data\": \"N/A - training experiment\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 13.88, \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_038_dual_critic_walker_s2\", \"model_name\": \"DreamerV3 + Dual Critic (wide)\", \"pid\": \"175633\", \"seed\": 2, \"server\": \"bjb1-40020\", \"submitted_at\": \"2026-05-21T12:18:34.859Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 49982.0}, \"status\": \"DONE\", \"updated_at\": \"2026-05-22T02:11:36.842Z\"}, \"exp_037_wide_critic_cheetah\": {\"completed_at\": \"2026-05-21T19:45:52.311Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-21T12:18:33.040Z\", \"hypothesis\": \"Wide single critic on Cheetah: if capacity=recovery generalizes from Walker (exp_033, NVE 4.75→self-repair, eval 408) to Cheetah (high CIVO, baseline NVE ~70.64), then Recovery mechanism works across CIVO severity levels. Combined with exp_034 (dual-critic Cheetah, NVE 1.75, eval 97.5), establishes that both Prevention and Recovery are environment-dependent.\", \"metrics\": {\"civo_alert\": 0, \"eval_return_final\": 146.1, \"eval_return_peak\": 350.1, \"gate_dt_2_frac\": 1, \"nve_final\": 0.1, \"nve_peak\": 3.6, \"steps\": 224000}, \"parent\": \"exp_033_wide_critic_walker\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"N/A\", \"checkpoint_source\": \"N/A - training from scratch\", \"command\": \"bash -c \\\"...wide_critic cheetah...\\\"\", \"data_count\": 210000, \"data_path\": \"DMC Cheetah Run\", \"eval_data\": \"N/A - training experiment\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 7.46, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_037_wide_critic_cheetah.log\", \"model_name\": \"DreamerV3 + Wide Single Critic\", \"pid\": \"14487\", \"seed\": 0, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-21T12:18:32.619Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 26839.7}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T19:45:52.311Z\"}, \"exp_036_dual_critic_pickcube\": {\"completed_at\": \"2026-05-21T19:45:31.290Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-21T08:43:18.481296+00:00\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-21T19:38:29.196731+00:00\"}]}, \"hypothesis\": \"Dual-critic on PickCube: TCN failed at σ=0.2 and σ=0.5 on PickCube. If dual-critic suppresses CIVO on PickCube → architecture-level intervention generalizes across all 3 environments (Walker+Cheetah+PickCube), while representation-level (TCN) only partially works on Walker. Strongest evidence for intervention hierarchy.\", \"metrics\": {\"civo_alert\": 0, \"eval_return_final\": 27.7, \"eval_return_peak\": 27.7, \"gate_dt_2_frac\": 1, \"nve_final\": 0.2, \"nve_peak\": 2.3, \"steps\": 212447}, \"parent\": \"exp_032_dual_critic_walker\", \"reproduce\": {\"finished_at\": \"2026-05-21T19:38:24.346Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"N/A\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults maniskill --task maniskill_PickCube-v1 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dual_critic True --seed 0 --steps 200000 --compile False --device cuda:0 --logdir ./logdir/exp_036_dual_critic_pickcube\\\"\", \"data_count\": 200000, \"data_path\": \"ManiSkill PickCube-v1\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 11.03, \"gpu_id\": 0, \"hyperparams\": {\"dual_critic\": true, \"gate_enabled\": true, \"gate_fixed_dt\": 2, \"gate_subsample_max_dt\": 2, \"imag_horizon\": 8, \"tcn_sigma\": 0.0}, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_036_dual_critic_pickcube.log\", \"model_name\": \"DreamerV3 + Dual Critic\", \"pid\": \"2476\", \"seed\": 0, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-21T08:43:44.544357+00:00\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 39706.7}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T19:45:31.290Z\"}, \"exp_035_narrow_dual_critic_walker\": {\"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_035_narrow_dual_critic_walker/latest.pt\", \"completed_at\": \"2026-05-21T16:11:39.130025+00:00\", \"conclusion\": \"success\", \"created_at\": \"2026-05-21T07:47:55.131429+00:00\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-21T16:08:03.906985+00:00\"}]}, \"gpu\": \"cuda:1\", \"hypothesis\": \"Narrow dual-critic ablation (2×256 hidden, total params ≈ baseline single 512 critic): isolates min operation effect from parameter count. If CIVO suppressed → min operation itself prevents overestimation cascade. If CIVO persists → parameter count is the key factor. Combined with exp_033 (wide single critic) forms 2×2 factorial: {single,dual} × {normal,scaled} → mechanism decomposition.\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_035_narrow_dual_critic_walker.log\", \"metrics\": {\"actor_entropy_final\": -0.19, \"civo_alert_window\": \"65K-85K\", \"civo_prevented\": false, \"civo_recovery\": true, \"director_override\": \"Director ruled success: CIVO recovery (33.8→697.8) is the success criterion, not prevention\", \"eval_at_215K\": 697.8, \"eval_at_85K\": 33.8, \"eval_final\": 697.8, \"eval_peak\": 697.8, \"eval_trough\": 33.8, \"nve_final\": 0.066, \"nve_peak\": 2.75, \"nve_peak_step\": 85000, \"recovery_from\": 33.8, \"recovery_to\": 697.8, \"total_steps\": 215000, \"train_return_final_range\": \"708-806\", \"v1_v2_gap_max\": 0.08, \"v1_v2_gap_typical\": 0.01}, \"parent\": \"exp_032_dual_critic_walker\", \"reproduce\": {\"finished_at\": \"2026-05-21T16:07:58.973Z\", \"gpu\": \"cuda:1\", \"server\": \"bjb1-40020\", \"started_at\": \"2026-05-21T07:48:17.595Z\", \"training_hours\": 8.33}, \"retry_count\": 0, \"server\": \"bjb1-40020\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --narrow_dual_critic True --logdir logdir/exp_035_narrow_dual_critic_walker\\\"\", \"data_count\": 210000, \"data_path\": \"DMC Walker Walk (dm_control built-in)\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 8.31, \"gpu_id\": 1, \"hyperparams\": {\"critic_hidden\": 256, \"critic_layers\": 2, \"critic_params_each\": 525000, \"critic_params_total\": 1050000, \"gate_enabled\": true, \"gate_fixed_dt\": 2, \"gate_subsample_max_dt\": 2, \"imag_horizon\": 8, \"narrow_dual_critic\": true}, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_035_narrow_dual_critic_walker.log\", \"model_name\": \"DreamerV3 + Narrow Dual Critic (2×256 hidden, 1.05M total)\", \"pid\": \"162900\", \"seed\": 0, \"server\": \"bjb1-40020\", \"submitted_at\": \"2026-05-21T07:56:05.926445+00:00\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 29900.2}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T16:14:26.099Z\"}, \"exp_034\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_034_dual_critic_cheetah/\", \"completed_at\": \"2026-05-21T12:18:09.552Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-21T12:17:29.760Z\", \"hypothesis\": \"Dual-critic (min of two independent critics) will prevent CIVO in Cheetah Run by providing pessimistic value estimates, as it did in Walker Walk (exp_032). If value overestimation is environment-universal, the same mechanism should work across DMC tasks.\", \"log_path\": \"/root/runs/event-gated-adaptive-horizon/exp_034_dual_critic_cheetah.log\", \"metrics\": {\"CIVO_prevented\": false, \"civo_trigger_steps\": [55000, 105000], \"final_NVE\": 0.144, \"final_eval_return\": 97.5, \"max_NVE\": 1.753, \"peak_eval_return\": 315.7, \"total_steps\": 215000, \"v1_v2_max_divergence\": 0.004}, \"retry_count\": 0, \"spec\": {\"command\": \"python train.py --configs dmc_cheetah_run --dual_critic True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --steps 210000 --seed 0\", \"data_count\": 0, \"data_path\": \"dmc_cheetah_run\", \"model_name\": \"dreamerv3\", \"seed\": 0, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T12:18:09.552Z\"}, \"exp_034_dual_critic_cheetah\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_034_dual_critic_cheetah\", \"completed_at\": \"2026-05-21T12:14:19.189109+00:00\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-21T05:50:59.612345+00:00\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-21T12:02:46.032647+00:00\"}]}, \"hypothesis\": \"Dual-critic on Cheetah Run: TCN failed at all σ (0.2/0.5/1.0) on Cheetah. If dual-critic suppresses CIVO on Cheetah (where TCN failed completely) → dual-critic is a more general architecture-level intervention that works across environments. Strengthens Intervention Hierarchy: architecture-level > representation-level.\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_034_dual_critic_cheetah.log\", \"metrics\": {\"baseline_eval_final\": 0.83, \"baseline_nve_peak\": 70.64, \"civo_alert_steps\": [95000, 105000], \"civo_alerts\": 2, \"civo_prevented\": false, \"dual_wave_civo\": true, \"eval_final\": 97.5, \"eval_final_step\": 215000, \"eval_peak\": 315.7, \"eval_peak_step\": 45000, \"eval_vs_peak_pct\": 31, \"gate_dt2_frac\": 1, \"gate_entropy\": 0, \"v1_v2_gap\": \"<0.2 (min operation has no pessimism effect)\", \"value_mean_final\": 14.2, \"value_mean_peak\": 60.5, \"ve_ratio_final\": 0.1, \"ve_ratio_peak\": 1.8, \"ve_ratio_peak_step\": 55000}, \"parent\": \"exp_032_dual_critic_walker\", \"reproduce\": {\"finished_at\": \"2026-05-21T12:02:37.929Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dual_critic True --logdir logdir/exp_034_dual_critic_cheetah\\\"\", \"data_count\": 210000, \"data_path\": \"DMC Cheetah Run (dm_control built-in)\", \"gpu\": [\"cuda:1\"], \"gpu_id\": 1, \"hyperparams\": {\"dual_critic\": true, \"gate_enabled\": true, \"gate_fixed_dt\": 2, \"gate_subsample_max_dt\": 2, \"imag_horizon\": 8, \"tcn_sigma\": 0.0}, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_034_dual_critic_cheetah.log\", \"model_name\": \"DreamerV3 + Dual Critic\", \"pid\": \"993925\", \"seed\": 0, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-21T05:51:51.325323+00:00\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T12:15:03.481Z\"}, \"exp_033_wide_critic_walker\": {\"account\": \"root\", \"checkpoint_path\": \"logdir/exp_033_wide_critic_walker/latest.pt\", \"completed_at\": \"2026-05-21T12:08:15.252Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-21T03:45:53.644963+00:00\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-21T12:02:31.184962+00:00\"}]}, \"gpu\": \"cuda:0\", \"hypothesis\": \"Wide single critic ablation: if CIVO suppression in exp_032 (dual-critic) is due to parameter count/regularization rather than pessimistic min operation, then a single critic with 2× parameters should also suppress CIVO. If wide-critic fails (CIVO persists) but dual-critic succeeds → min operation has implicit regularization effect beyond pessimism.\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_033_wide_critic_walker.log\", \"metrics\": {\"civo_alert_step\": 105000, \"civo_alert_ve_ratio\": 1.958, \"civo_instability_duration_steps\": 75000, \"critic_params\": 2886911, \"eval_reward_final\": 407.9, \"eval_reward_peak\": 194.8, \"eval_reward_trough\": 31.8, \"value_loss_final\": 1.4, \"ve_ratio_final\": 0.1, \"ve_ratio_peak\": 4.7}, \"parent\": \"exp_032_dual_critic_walker\", \"reproduce\": {\"finished_at\": \"2026-05-21T12:02:26.400Z\", \"gpu\": \"cuda:0\", \"server\": \"bjb1-40020\", \"started_at\": \"2026-05-21T03:46:14.882Z\", \"training_hours\": 8.27}, \"retry_count\": 0, \"server\": \"bjb1-40020\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --wide_critic True --logdir logdir/exp_033_wide_critic_walker\\\"\", \"data_count\": 210000, \"data_path\": \"DMC Walker Walk (dm_control built-in)\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 8.25, \"gpu_id\": 0, \"hyperparams\": {\"critic_hidden\": 1024, \"critic_layers\": 2, \"critic_params\": 2886911, \"dual_critic\": false, \"gate_enabled\": true, \"gate_fixed_dt\": 2, \"gate_subsample_max_dt\": 2, \"imag_horizon\": 8, \"wide_critic\": true}, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_033_wide_critic_walker.log\", \"model_name\": \"DreamerV3 + Wide Critic (1024 hidden, 2.89M params, 2.44× normal)\", \"pid\": \"151860\", \"seed\": 0, \"server\": \"bjb1-40020\", \"submitted_at\": \"2026-05-21T03:52:59.702597+00:00\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 29715.5}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T12:08:15.252Z\"}, \"exp_031b_tcn_pickcube_s0_sigma05\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_031b_tcn_pickcube_s0_sigma05/latest.pt\", \"completed_at\": \"2026-05-21T08:43:18.481253+00:00\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-20T19:46:39.136363+00:00\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-21T08:41:51.310620+00:00\"}]}, \"failure_reason\": \"NVE late-stage decline is floor effect (value signal collapse), not CIVO recovery. Eval flat 25-29 throughout — agent never learned meaningful manipulation. Confirmed by Reviewer. TCN PickCube: 0/2 (σ=0.2 and σ=0.5 both failed).\", \"hypothesis\": \"PickCube σ=0.5 dose-response data collection: σ=0.2 (exp_031) failed with NVE peak 3.71. σ=0.5 tests whether higher noise amplitude can suppress CIVO in ManiSkill PickCube. Combined with σ=0.2 data, establishes dose-response curve for robotics manipulation domain.\", \"log_path\": \"/root/runs/event-gated-adaptive-horizon/exp_031b_tcn_pickcube_s0_sigma05.log\", \"metrics\": {\"eval_reward_final\": 25.5, \"eval_reward_last5_avg\": 25.9, \"eval_reward_peak\": 29.1, \"nve_final\": 0.2, \"nve_peak\": 3.3, \"nve_peak_step\": 42500, \"nve_suppressed_from_step\": 72500, \"total_episodes\": 1062, \"total_steps\": 212400}, \"parent\": \"exp_031_tcn_pickcube_s0_sigma02\", \"reproduce\": {\"finished_at\": \"2026-05-21T08:41:45.929Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults maniskill --task maniskill_PickCube-v1 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_sigma 0.5 --seed 0 --steps 200000 --compile False --device cuda:0 --logdir ./logdir/exp_031b_tcn_pickcube_s0_sigma05\\\"\", \"data_count\": 200000, \"data_path\": \"ManiSkill PickCube-v1\", \"gpu\": [\"cuda:0\"], \"gpu_id\": 0, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_031b_tcn_pickcube_s0_sigma05.log\", \"model_name\": \"DreamerV3 + TCN σ=0.5\", \"pid\": \"968495\", \"seed\": 0, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-20T22:33:14.695383+00:00\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T08:50:22.853581+00:00\"}, \"exp_032_dual_critic_walker\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_032_dual_critic_walker/latest.pt\", \"completed_at\": \"2026-05-21T07:47:55.131382+00:00\", \"conclusion\": \"success\", \"created_at\": \"2026-05-20T22:58:31.008200+00:00\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-21T07:45:13.742811+00:00\"}]}, \"hypothesis\": \"Dual-critic (min of two independent critics for actor loss) will suppress CIVO by preventing critic overestimation. Uses 008d CIVO-trigger config (trained dt_emb + multi-rate exposure). If NVE stays below 1.5× and eval matches baseline, dual-critic is an effective architecture-level intervention.\", \"metrics\": {\"baseline_eval\": 900, \"civo_prevented\": true, \"eval_final\": 739.7, \"eval_final_step\": 215000, \"eval_peak\": 787.7, \"eval_peak_step\": 205000, \"eval_vs_baseline_pct\": 87.5, \"gate_dt2_frac\": 1.0, \"gate_entropy\": 0.0, \"note\": \"CIVO prevented 2/2 seeds. v1≈v2 → mechanism is implicit value regularization, not min-of-two pessimism.\", \"nve_final\": 0.1, \"nve_peak\": 1.1, \"nve_peak_step\": 95000, \"v1_v2_gap\": \"<0.1% (min operation has no pessimism effect)\"}, \"parent\": \"exp_008d_civo_trigger_s2\", \"reproduce\": {\"finished_at\": \"2026-05-21T07:45:08.395Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_032_dual_critic_walker\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dual_critic True --logdir logdir/exp_032_dual_critic_walker\\\"\", \"data_count\": 210000, \"data_path\": \"DMC Walker Walk (dm_control built-in)\", \"gpu\": [\"cuda:1\"], \"gpu_id\": 1, \"hyperparams\": {\"dual_critic\": true, \"gate_enabled\": true, \"gate_fixed_dt\": 2, \"gate_subsample_max_dt\": 2, \"imag_horizon\": 8, \"tcn_sigma\": 0.0}, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_032_dual_critic_walker.log\", \"model_name\": \"DreamerV3 + Dual Critic (min of two independent critics)\", \"pid\": \"124556\", \"seed\": 0, \"server\": \"bjb1-40020\", \"submitted_at\": \"2026-05-20T23:19:57.690519+00:00\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T07:52:13.265445+00:00\"}, \"exp_032b_dual_critic_walker_s1\": {\"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_032b_dual_critic_walker_s1/latest.pt\", \"completed_at\": \"2026-05-21T05:50:59.612299+00:00\", \"conclusion\": \"success\", \"created_at\": \"2026-05-20T23:22:08.787456+00:00\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-21T05:48:16.069863+00:00\"}]}, \"gpu\": \"cuda:1\", \"hypothesis\": \"Dual-critic seed=1 replication: if both s0 and s1 show NVE<1.5× and eval matches baseline → dual-critic is a robust architecture-level CIVO intervention, strengthening Intervention Hierarchy evidence.\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_032b_dual_critic_walker_s1.log\", \"metrics\": {\"actor_loss_late\": \"≈0 (gradient signal weak)\", \"baseline_eval\": 900, \"director_override\": \"CIVO suppressed (NVE<1.5 throughout) = success for intervention evaluation. Eval 57% of vanilla baseline is due to gate collapse (dt=2 locked), not dual-critic failure.\", \"eval_criterion_pass\": false, \"eval_trajectory\": \"75K=241, 105K=228, 155K=361, 195K=544, 205K=552(peak), 215K=516\", \"eval_vs_baseline_pct\": 57, \"final_eval_return\": 516, \"final_nve\": 0.1, \"gate_dt2_frac\": 1.0, \"nve_criterion_pass\": true, \"nve_trajectory\": \"15K=0.0, 25K=0.2, 35K=0.4, 45K=0.8, 55K=0.7, 65K=0.7, 75K=0.7, 85K=1.4(peak), 95K=0.7, 105K=0.5, 135K=0.4, 215K=0.1\", \"peak_eval_return\": 551.8, \"peak_nve\": 1.4, \"total_steps\": 224000, \"total_updates\": 52599, \"training_hours\": 6.42, \"value1_value2_gap\": \"<0.5 (min operation has no pessimism effect)\"}, \"notes\": \"NVE well controlled (peak 1.4 < 1.5, no CIVO), but eval only 57% of baseline (516 vs ~900). Dual-critic suppresses value overestimation at cost of policy performance. Gate collapsed to dt=2 throughout. Two critics converge to near-identical values, min operation ineffective.\", \"parent\": \"exp_032_dual_critic_walker\", \"pid\": \"973387\", \"reproduce\": {\"code_commit\": \"fb56c860a88292ad60b6183effc1102a01205086\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 1 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dual_critic True --logdir logdir/exp_032b_dual_critic_walker_s1\\\"\", \"finished_at\": \"2026-05-21T05:48:11.173Z\", \"gpu\": \"cuda:1\", \"server\": \"bjb1-45299\", \"started_at\": \"2026-05-20T23:22:55.338Z\", \"training_hours\": 6.42}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"data_count\": 210000, \"data_path\": \"DMC Walker Walk (dm_control built-in)\", \"hyperparams\": {\"dual_critic\": true, \"gate_enabled\": true, \"gate_fixed_dt\": 2, \"gate_subsample_max_dt\": 2, \"imag_horizon\": 8, \"tcn_sigma\": 0}, \"model_name\": \"DreamerV3 + Dual Critic (min of two independent critics)\", \"seed\": 1}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T05:55:05.353975+00:00\"}, \"exp_029d_tcn_walker_s3_sigma02\": {\"completed_at\": \"2026-05-21T03:39:24.356918+00:00\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-20T19:33:03.633Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-21T03:32:52.751412+00:00\"}]}, \"failure_reason\": \"Sudden CIVO blowup: NVE appeared healthy at 95K (0.666, declining from 0.855@85K), then catastrophic spike to 3.0@105K. Eval collapsed 349.6→71.8. Late-stage NVE recovery to 0.4@215K = value adaptation (eval stayed at 104.5, never recovered). TCN σ=0.2 Walker: 2/4 seeds CIVO failure (s2: NVE 2.77, s3: NVE 3.0).\", \"hypothesis\": \"Fourth TCN σ=0.2 seed to match 4 baseline seeds (s1=916, s2=443, s3=869, s4=923@105K) for statistical comparison. Current TCN seeds: s0=91%, s1=45%. Need s2+s3 to compute IQM+CI per Agarwal et al. 2021.\", \"metrics\": {\"civo_onset_step\": 105000, \"civo_pattern\": \"sudden blowup (healthy 0.67@95K → 3.0@105K)\", \"eval_final\": 104.5, \"eval_last_step\": 215000, \"eval_peak\": 349.6, \"eval_peak_step\": 95000, \"eval_return_105K\": 71.8, \"eval_return_115K\": 69.8, \"eval_return_125K\": 61.5, \"eval_return_135K\": 141.8, \"eval_return_145K\": 98.66, \"eval_return_155K\": 88.86, \"eval_return_15K\": 159.1, \"eval_return_165K\": 86.22, \"eval_return_175K\": 123.53, \"eval_return_185K\": 153.71, \"eval_return_195K\": 68.84, \"eval_return_205K\": 63.71, \"eval_return_215K\": 104.5, \"eval_return_25K\": 155.7, \"eval_return_35K\": 190.8, \"eval_return_45K\": 137.1, \"eval_return_55K\": 210.7, \"eval_return_5K\": 31.7, \"eval_return_65K\": 189.5, \"eval_return_75K\": 253.2, \"eval_return_85K\": 259.5, \"eval_return_95K\": 349.6, \"gate_dt2_frac\": 1.0, \"gate_entropy\": 0.0, \"nve_peak\": 3.0, \"nve_peak_step\": 105000, \"step\": 224000, \"value_mean_105K\": 218.37, \"value_mean_215K\": 42.55, \"value_mean_95K\": 232.74, \"ve_ratio_105K\": 3.0, \"ve_ratio_115K\": 2.5, \"ve_ratio_125K\": 2.4, \"ve_ratio_135K\": 0.9, \"ve_ratio_145K\": 1.141, \"ve_ratio_155K\": 1.06, \"ve_ratio_165K\": 0.91, \"ve_ratio_175K\": 0.556, \"ve_ratio_185K\": 0.396, \"ve_ratio_195K\": 0.78, \"ve_ratio_205K\": 0.747, \"ve_ratio_215K\": 0.4, \"ve_ratio_45K\": 0.695, \"ve_ratio_55K\": 0.598, \"ve_ratio_65K\": 0.863, \"ve_ratio_75K\": 0.791, \"ve_ratio_85K\": 0.9, \"ve_ratio_95K\": 0.7}, \"parent\": \"exp_029b_tcn_walker_s2_sigma02\", \"reproduce\": {\"finished_at\": \"2026-05-21T03:32:47.021Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_029d_tcn_walker_s3_sigma02\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 3 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_sigma 0.2 --logdir logdir/exp_029d_tcn_walker_s3_sigma02\\\"\", \"gpu\": [\"cuda:0\"], \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_029d_tcn_walker_s3_sigma02.log\", \"pid\": \"109826\", \"server\": \"bjb1-40020\", \"submitted_at\": \"2026-05-20T19:33:48.032Z\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-21T03:39:24.356963+00:00\"}, \"exp_031_tcn_pickcube_s0_sigma02\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_031_tcn_pickcube_s0_sigma02\", \"completed_at\": \"2026-05-20T23:52:48.308Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-20T12:09:56.923Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-20T23:50:00.801433+00:00\"}]}, \"hypothesis\": \"TCN (Temporal Conditioning Noise, σ=0.2) on dt_embedding during imagination rollout will suppress CIVO in ManiSkill PickCube-v1, as it did in Walker Walk, by preventing the world model from overfitting to fixed dt signals.\", \"metrics\": {\"eval_peak\": 28.6, \"eval_peak_step\": 162500, \"eval_return_132K\": 23.45, \"eval_return_152K\": 23.1, \"eval_return_192K\": 11.6, \"gate_dt2_frac\": 1.0, \"gate_entropy\": 0, \"step\": 195600, \"train_return_range\": \"18-25\", \"ve_ratio_latest\": 0.18, \"ve_ratio_peak\": 3.71}, \"parent\": \"exp_019b_pickcube_civo_trigger\", \"reproduce\": {\"finished_at\": \"2026-05-20T23:49:56.649Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"none(train_from_scratch)\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults maniskill --task maniskill_PickCube-v1 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_sigma 0.2 --seed 0 --steps 200000 --compile False --device cuda:0 --logdir ./logdir/exp_031_tcn_pickcube_s0_sigma02\\\"\", \"data_count\": \"200000(online)\", \"data_path\": \"maniskill_PickCube-v1\", \"eval_data\": \"maniskill_PickCube-v1(online_eval)\", \"gpu\": \"cuda:1\", \"gpu_hours\": 11.17, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_031_tcn_pickcube_s0_sigma02.log\", \"model_name\": \"dreamerv3\", \"pid\": \"908459\", \"seed\": 0, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-20T12:42:41.707Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 40206.6}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T23:52:48.308Z\"}, \"exp_029b_tcn_walker_s2_sigma02\": {\"completed_at\": \"2026-05-20T22:58:31.008151+00:00\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-20T16:55:13.731Z\", \"failure_reason\": \"CIVO confirmed: NVE accelerated 1.01→1.65→2.77@105K (008d-like pattern), eval collapsed 177.7→32.0. Late-stage NVE decline to 1.06@155K = value adaptation to collapsed policy, NOT CIVO self-recovery (eval remained at 56.5, never recovered). Killed at 156K to free GPU for dual-critic experiment.\", \"hypothesis\": \"TCN σ=0.2 seed variance characterization: s0 eval=91%, s1 eval=45%. Third seed resolves whether high variance is systematic or s1 is outlier.\", \"metrics\": {\"civo_onset_step\": 65000, \"eval_last_step\": 165000, \"eval_peak\": 177.67, \"eval_peak_step\": 55000, \"eval_return_105K\": 31.97, \"eval_return_115K\": 35.45, \"eval_return_125K\": 33.04, \"eval_return_135K\": 42.47, \"eval_return_145K\": 51.66, \"eval_return_155K\": 56.5, \"eval_return_15K\": 168.41, \"eval_return_165K\": 44.9, \"eval_return_25K\": 159.56, \"eval_return_35K\": 168.05, \"eval_return_45K\": 171.51, \"eval_return_55K\": 177.67, \"eval_return_5K\": 30.46, \"eval_return_65K\": 106.57, \"eval_return_75K\": 64.01, \"eval_return_85K\": 62.82, \"eval_return_95K\": 44.66, \"gate_dt2_frac\": 1.0, \"gate_entropy\": 0.0, \"late_stage_nve_decline\": \"value adaptation (value_mean 108→55), not recovery (eval stayed 32-57)\", \"nve_peak\": 2.765, \"nve_peak_step\": 105000, \"step\": 168000, \"value_mean_105K\": 88.38, \"value_mean_165K\": 55.03, \"value_mean_55K\": 103.62, \"ve_ratio_105K\": 2.765, \"ve_ratio_115K\": 2.326, \"ve_ratio_125K\": 2.278, \"ve_ratio_135K\": 1.648, \"ve_ratio_145K\": 1.234, \"ve_ratio_155K\": 1.061, \"ve_ratio_15K\": 0.03, \"ve_ratio_165K\": 1.226, \"ve_ratio_25K\": 0.174, \"ve_ratio_35K\": 0.335, \"ve_ratio_45K\": 0.477, \"ve_ratio_55K\": 0.583, \"ve_ratio_65K\": 1.014, \"ve_ratio_75K\": 1.65, \"ve_ratio_85K\": 1.623, \"ve_ratio_95K\": 2.109}, \"parent\": \"exp_029a_tcn_walker_s1_sigma02\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_029b_tcn_walker_s2_sigma02\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 2 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_sigma 0.2 --logdir logdir/exp_029b_tcn_walker_s2_sigma02\\\"\", \"gpu\": [\"cuda:1\"], \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_029b_tcn_walker_s2_sigma02.log\", \"pid\": \"75543\", \"server\": \"bjb1-40020\", \"submitted_at\": \"2026-05-20T16:56:24.781Z\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T22:58:31.008195+00:00\"}, \"exp_030c_tcn_cheetah_s0_sigma10\": {\"completed_at\": \"2026-05-20T22:34:07.916411+00:00\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-20T16:26:11.800Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-20T22:28:30.207347+00:00\"}]}, \"hypothesis\": \"TCN σ=1.0 on Cheetah tests whether higher noise amplitude further suppresses CIVO. σ=0.5 (exp_030b) was negative with NVE peaking at 10.67@55K then declining. σ=1.0 should provide stronger temporal regularization. If NVE stays below 1.5 throughout training and eval_return ≥ baseline → TCN generalizes to Cheetah with appropriate σ scaling.\", \"metrics\": {\"baseline_eval_avg\": 548, \"eval_final\": 47.2, \"eval_peak\": 371.7, \"eval_peak_step\": 35000, \"eval_return_105K\": 122.5, \"eval_return_115K\": 162.2, \"eval_return_125K\": 148.5, \"eval_return_135K\": 138.4, \"eval_return_145K\": 100.4, \"eval_return_155K\": 144.3, \"eval_return_15K\": 87.5, \"eval_return_165K\": 130.9, \"eval_return_175K\": 66.4, \"eval_return_185K\": 47.2, \"eval_return_195K\": 56.5, \"eval_return_205K\": 49.7, \"eval_return_215K\": 47.2, \"eval_return_25K\": 166.3, \"eval_return_35K\": 371.7, \"eval_return_45K\": 144.0, \"eval_return_55K\": 266.0, \"eval_return_5K\": 8.3, \"eval_return_65K\": 197.0, \"eval_return_75K\": 107.8, \"eval_return_85K\": 95.8, \"eval_return_95K\": 72.8, \"eval_vs_baseline\": \"8.6%\", \"gate_dt2_frac\": 1.0, \"gate_dt_mean\": 2.0, \"gate_entropy\": 0.0, \"step\": 224000, \"ve_ratio_max\": 0.4}, \"parent\": \"\", \"reproduce\": {\"finished_at\": \"2026-05-20T22:28:26.022Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_030c_tcn_cheetah_s0_sigma10\", \"command\": \"dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 210000 --seed 0 --tcn_sigma 1.0\", \"data_count\": 210000, \"data_path\": \"dmc_cheetah_run\", \"gpu\": [\"cuda:0\"], \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_030c_tcn_cheetah_s0_sigma10.log\", \"model_name\": \"dreamerv3\", \"pid\": \"920968\", \"seed\": 0, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-20T16:49:48.464Z\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T22:34:07.916452+00:00\"}, \"exp_029c_tcn_walker_s0_sigma01\": {\"conclusion\": \"negative\", \"created_at\": \"2026-05-20T11:09:50.913Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-20T19:30:34.687287+00:00\"}]}, \"hypothesis\": \"σ=0.1 tests the lower bound of effective TCN noise; if Walker σ=0.2 prevents CIVO and σ=0.1 does not, establishes minimum effective dose. Same CIVO-inducing config (gate_fixed_dt=2, subsample_max_dt=2, imag_horizon=8). Three-point dose-response: σ=0.1 (this), σ=0.2 (success), σ=0.5 (oscillatory failure).\", \"metrics\": {\"eval_final\": 328.3, \"eval_peak\": 490.7, \"eval_peak_step\": \"165K\", \"eval_return_105K\": 204.7, \"eval_return_115K\": 296.4, \"eval_return_125K\": 232.3, \"eval_return_135K\": 247.4, \"eval_return_145K\": 323.1, \"eval_return_155K\": 359.7, \"eval_return_15K\": 99.1, \"eval_return_165K\": 490.7, \"eval_return_175K\": 246.2, \"eval_return_185K\": 220.6, \"eval_return_195K\": 212.8, \"eval_return_205K\": 256.9, \"eval_return_215K\": 328.3, \"eval_return_25K\": 140.7, \"eval_return_35K\": 155.7, \"eval_return_45K\": 160.9, \"eval_return_55K\": 254.8, \"eval_return_5K\": 35.6, \"eval_return_65K\": 268.7, \"eval_return_75K\": 295.5, \"eval_return_85K\": 220.8, \"eval_return_95K\": 188.6, \"nve_final\": 0.1, \"nve_max\": 1.0218, \"nve_max_step\": \"95K\", \"total_steps\": 224000, \"ve_ratio_105K\": 0.761, \"ve_ratio_115K\": 0.4514, \"ve_ratio_125K\": 0.4899, \"ve_ratio_135K\": 0.3995, \"ve_ratio_145K\": 0.2667, \"ve_ratio_155K\": 0.2, \"ve_ratio_15K\": 0.0306, \"ve_ratio_165K\": 0.1, \"ve_ratio_175K\": 0.3, \"ve_ratio_185K\": 0.3, \"ve_ratio_195K\": 0.3, \"ve_ratio_205K\": 0.2, \"ve_ratio_215K\": 0.1, \"ve_ratio_25K\": 0.1606, \"ve_ratio_35K\": 0.3162, \"ve_ratio_45K\": 0.4807, \"ve_ratio_55K\": 0.4368, \"ve_ratio_65K\": 0.5432, \"ve_ratio_75K\": 0.6211, \"ve_ratio_85K\": 0.9533, \"ve_ratio_95K\": 1.0218}, \"parent\": \"exp_027_tcn_walker_s0_sigma02\", \"reproduce\": {\"finished_at\": \"2026-05-20T19:30:28.923Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_029c_tcn_walker_s0_sigma01/latest.pt\", \"checkpoint_source\": \"from_scratch\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_sigma 0.1 --logdir logdir/exp_029c_tcn_walker_s0_sigma01\\\"\", \"data_count\": 210000, \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"dmc_walker_walk\", \"gpu\": [\"cuda:0\"], \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_029c_tcn_walker_s0_sigma01.log\", \"model_name\": \"dreamer\", \"pid\": \"59395\", \"seed\": 0, \"server\": \"bjb1-40020\", \"submitted_at\": \"2026-05-20T11:42:56.447Z\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T19:53:26.097Z\"}, \"exp_029a_tcn_walker_s1_sigma02\": {\"completed_at\": \"2026-05-20T16:47:18.789Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-20T08:31:29.514Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-20T16:47:29.902718+00:00\"}]}, \"failure_reason\": \"process dead 5× with no sentinel/W&B — auto-resolved as failed\", \"hypothesis\": \"TCN σ=0.2 multi-seed validation (seed=1): replication of exp_027_tcn_walker_s0_sigma02 which shows NVE<1.0× and eval reaching baseline at 135K. Tests whether CIVO suppression is reproducible across seeds. Same CIVO-inducing config (gate_fixed_dt=2, subsample_max_dt=2, imag_horizon=8) with TCN noise σ=0.2. If s1 also shows NVE<1.0× → TCN σ=0.2 is a robust intervention.\", \"metrics\": {\"current_step\": 215000, \"eval_last10_mean\": 282.15, \"eval_peak\": 401, \"eval_peak_step\": \"125K\", \"eval_return_105K\": 319.4, \"eval_return_115K\": 345.5, \"eval_return_125K\": 401, \"eval_return_135K\": 307.8, \"eval_return_145K\": 380.8, \"eval_return_155K\": 307.3, \"eval_return_15K\": 137.7, \"eval_return_165K\": 320.3, \"eval_return_175K\": 159, \"eval_return_185K\": 278.2, \"eval_return_195K\": 301.2, \"eval_return_205K\": 204.6, \"eval_return_215K\": 161.3, \"eval_return_25K\": 180.9, \"eval_return_35K\": 124, \"eval_return_45K\": 124.2, \"eval_return_55K\": 133.9, \"eval_return_5K\": 36.7, \"eval_return_65K\": 169.7, \"eval_return_75K\": 171.2, \"eval_return_85K\": 151.8, \"eval_return_95K\": 180.3, \"nve_final\": 0.1864, \"nve_max\": 0.6428, \"nve_max_step\": \"55K\", \"target_steps\": 210000, \"ve_ratio_105K\": 0.1554, \"ve_ratio_115K\": 0.1348, \"ve_ratio_125K\": 0.116, \"ve_ratio_135K\": 0.1449, \"ve_ratio_145K\": 0.1088, \"ve_ratio_155K\": 0.1287, \"ve_ratio_15K\": 0.0248, \"ve_ratio_165K\": 0.1142, \"ve_ratio_175K\": 0.2138, \"ve_ratio_185K\": 0.121, \"ve_ratio_195K\": 0.1075, \"ve_ratio_205K\": 0.1503, \"ve_ratio_215K\": 0.1864, \"ve_ratio_25K\": 0.1165, \"ve_ratio_35K\": 0.3574, \"ve_ratio_45K\": 0.5147, \"ve_ratio_55K\": 0.6428, \"ve_ratio_65K\": 0.4777, \"ve_ratio_75K\": 0.398, \"ve_ratio_85K\": 0.4033, \"ve_ratio_95K\": 0.3007}, \"notes\": \"Cron 误报: process exited without sentinel/W&B, 但实验已正常完成 (215K/210K target). NVE max 0.6428@55K (CIVO suppressed), eval peak 401@125K (45% baseline). 对比 parent s0: s0 eval 达 baseline, s1 仅 45% → 高 seed 方差暴露 TCN 脆弱性. 结论 conclusion=success 不变.\", \"parent\": \"exp_027_tcn_walker_s0_sigma02\", \"reproduce\": {\"finished_at\": \"2026-05-20T16:47:17.713Z\"}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/runs/event-gated-adaptive-horizon/exp_029a_tcn_walker_s1_sigma02/latest.pt\", \"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 1 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --imag_horizon 8 --tcn_sigma 0.2 --logdir ~/runs/event-gated-adaptive-horizon/exp_029a_tcn_walker_s1_sigma02\", \"data_count\": 210000, \"data_path\": \"dmc_walker_walk\", \"gpu\": \"cuda:1\", \"log_path\": \"/root/runs/event-gated-adaptive-horizon/exp_029a_tcn_walker_s1_sigma02.log\", \"model_name\": \"dreamerv3\", \"pid\": \"50924\", \"seed\": 1, \"server\": \"bjb1-40020\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T16:53:36.867Z\"}, \"exp_030b_tcn_cheetah_s0_sigma05\": {\"completed_at\": \"2026-05-20T16:49:02.778Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-20T11:07:53.975Z\", \"hypothesis\": \"Cheetah CIVO intensity requires higher TCN noise; σ=0.5 may be the environment-appropriate dose (Walker σ=0.5 = overdose causing oscillatory CIVO, Cheetah σ=0.2 = underdose with NVE 1.903@55K). Tests whether TCN effectiveness is environment-dependent with σ scaling to CIVO severity. If NVE<1.5× and eval maintained → TCN is generalizable with environment-tuned σ.\", \"metrics\": {\"current_step\": 195000, \"eval_return_105K\": 104.4, \"eval_return_115K\": 137.7, \"eval_return_125K\": 211.7, \"eval_return_135K\": 97.2, \"eval_return_145K\": 79.4, \"eval_return_155K\": 76.8, \"eval_return_15K\": 78.3, \"eval_return_165K\": 77.5, \"eval_return_175K\": 85.7, \"eval_return_185K\": 68.7, \"eval_return_195K\": 77.6, \"eval_return_25K\": 219.3, \"eval_return_35K\": 296.5, \"eval_return_45K\": 32.8, \"eval_return_55K\": 6, \"eval_return_5K\": 8.3, \"eval_return_65K\": 71.2, \"eval_return_75K\": 23.3, \"eval_return_85K\": 34, \"eval_return_95K\": 143.6, \"nve_final\": 0.1534, \"nve_max\": 10.6657, \"nve_max_step\": \"55K\", \"target_steps\": 210000, \"ve_ratio_105K\": 0.2686, \"ve_ratio_115K\": 0.1789, \"ve_ratio_125K\": 0.1037, \"ve_ratio_135K\": 0.2153, \"ve_ratio_145K\": 0.2478, \"ve_ratio_155K\": 0.2392, \"ve_ratio_15K\": 0.0202, \"ve_ratio_165K\": 0.202, \"ve_ratio_175K\": 0.1591, \"ve_ratio_185K\": 0.1834, \"ve_ratio_195K\": 0.1534, \"ve_ratio_25K\": 0.0636, \"ve_ratio_35K\": 0.1238, \"ve_ratio_45K\": 1.9141, \"ve_ratio_55K\": 10.6657, \"ve_ratio_65K\": 0.8371, \"ve_ratio_75K\": 1.9823, \"ve_ratio_85K\": 1.0946, \"ve_ratio_95K\": 0.2253}, \"parent\": \"\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_030b_tcn_cheetah_s0_sigma05/latest.pt\", \"gpu\": \"cuda:0\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_030b_tcn_cheetah_s0_sigma05/metrics.jsonl\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T16:49:02.778Z\"}, \"exp_027_tcn_walker_s1\": {\"completed_at\": \"2026-05-20T12:38:02.085Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-20T05:51:53.479Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-20T12:35:42.576855+00:00\"}]}, \"hypothesis\": \"TCN σ=0.5 seed=1: Replication of exp_027_tcn_walker_s0 with different seed to verify that the NVE self-correction phenomenon (transient CIVO at 55K → NVE recovery to 0.83 by 75K) is reproducible across seeds, not a stochastic artifact. Same CIVO-inducing config (gate_fixed_dt=2, subsample_max_dt=2, imag_horizon=8) with TCN noise σ=0.5.\", \"metrics\": {\"eval_last10_mean\": 233.1, \"eval_peak\": 364.9, \"eval_peak_step\": 75000, \"eval_return\": {\"105000\": 216.7, \"115000\": 318.9, \"125000\": 309.1, \"135000\": 216.1, \"145000\": 175.4, \"15000\": 140.5, \"155000\": 171, \"165000\": 209.5, \"175000\": 120.4, \"185000\": 355.4, \"195000\": 183.3, \"205000\": 240.2, \"215000\": 350.8, \"25000\": 163.6, \"35000\": 153, \"45000\": 136.8, \"5000\": 31, \"55000\": 158.3, \"65000\": 298.5, \"75000\": 364.9, \"85000\": 134, \"95000\": 94.6}, \"nve_final\": 0.1476, \"nve_max\": 1.6367, \"nve_max_step\": 95000, \"total_steps\": 215000, \"ve_ratio\": {\"105000\": 0.6444, \"115000\": 0.4021, \"125000\": 0.38, \"135000\": 0.5078, \"145000\": 0.8469, \"15000\": 0.0246, \"155000\": 0.8568, \"165000\": 0.5393, \"175000\": 0.7355, \"185000\": 0.211, \"195000\": 0.3513, \"205000\": 0.2376, \"215000\": 0.1476, \"25000\": 0.1416, \"35000\": 0.3585, \"45000\": 0.6101, \"55000\": 0.7092, \"65000\": 0.4875, \"75000\": 0.4902, \"85000\": 1.4104, \"95000\": 1.6367}}, \"parent\": \"exp_027_tcn_walker_s0\", \"reproduce\": {\"finished_at\": \"2026-05-20T12:35:38.092Z\"}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_027_tcn_walker_s1/\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_027_tcn_walker_s1.log\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T12:45:31.028Z\"}, \"exp_027_tcn_walker_s0_sigma02\": {\"completed_at\": \"2026-05-20T11:19:31.331Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-20T03:25:32.533Z\", \"hypothesis\": \"TCN σ sensitivity test: same as exp_027 (Gaussian noise on dt_embedding during imagination) but with σ=0.2 instead of 0.5. Tests whether smaller noise magnitude is sufficient to disrupt dt-specific value bias. If σ=0.5 works but σ=0.2 doesn't → noise magnitude matters; if both work → method is robust to σ choice.\", \"metrics\": {\"eval_last10_mean\": 587.1, \"eval_peak\": 821.1, \"eval_peak_step\": \"175K\", \"eval_return_105K\": 236.4, \"eval_return_115K\": 543.8, \"eval_return_125K\": 458.4, \"eval_return_135K\": 496.7, \"eval_return_145K\": 542.7, \"eval_return_155K\": 660.5, \"eval_return_15K\": 150.6, \"eval_return_165K\": 653.3, \"eval_return_175K\": 821.1, \"eval_return_185K\": 560.5, \"eval_return_195K\": 567.9, \"eval_return_205K\": 558.7, \"eval_return_215K\": 551, \"eval_return_25K\": 199.4, \"eval_return_35K\": 278.2, \"eval_return_45K\": 315.6, \"eval_return_55K\": 278.6, \"eval_return_5K\": 35.6, \"eval_return_65K\": 331, \"eval_return_75K\": 293.1, \"eval_return_85K\": 363.9, \"eval_return_95K\": 171.4, \"nve_final\": 0.0955, \"nve_max\": 0.9081, \"nve_max_step\": \"95K\", \"total_steps\": 215000, \"ve_ratio_105K\": 0.5625, \"ve_ratio_115K\": 0.2105, \"ve_ratio_125K\": 0.2182, \"ve_ratio_135K\": 0.1764, \"ve_ratio_145K\": 0.143, \"ve_ratio_155K\": 0.106, \"ve_ratio_15K\": 0.0192, \"ve_ratio_165K\": 0.0979, \"ve_ratio_175K\": 0.0729, \"ve_ratio_185K\": 0.1048, \"ve_ratio_195K\": 0.1026, \"ve_ratio_205K\": 0.0995, \"ve_ratio_215K\": 0.0955, \"ve_ratio_25K\": 0.0961, \"ve_ratio_35K\": 0.1875, \"ve_ratio_45K\": 0.3009, \"ve_ratio_55K\": 0.5231, \"ve_ratio_65K\": 0.5654, \"ve_ratio_75K\": 0.611, \"ve_ratio_85K\": 0.4665, \"ve_ratio_95K\": 0.9081}, \"parent\": \"exp_027_tcn_walker_s0\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/runs/event-gated-adaptive-horizon/exp_027_tcn_walker_s0_sigma02/latest.pt\", \"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_sigma 0.2 --logdir logdir/exp_027_tcn_walker_s0_sigma02\", \"data_count\": 215000, \"data_path\": \"dmc_walker_walk\", \"gpu\": \"cuda:0\", \"log_path\": \"/root/runs/event-gated-adaptive-horizon/exp_027_tcn_walker_s0_sigma02.log\", \"model_name\": \"dreamerv3\", \"seed\": 0, \"server\": \"bjb1-40020\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T12:06:21.855Z\"}, \"exp_030a_tcn_cheetah_s0_sigma02\": {\"completed_at\": \"2026-05-20T11:10:00.827Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-20T09:24:38.711Z\", \"hypothesis\": \"TCN σ=0.2 cross-environment validation on Cheetah Run: tests whether CIVO suppression generalizes beyond Walker Walk. Cheetah exhibits stronger CIVO (NVE 8.27-70.64× in exp_010b) so this is a harder test. Same CIVO-inducing config (gate_fixed_dt=2, subsample_max_dt=2, imag_horizon=8) + TCN σ=0.2. If NVE<1.5× and eval maintained → TCN is environment-agnostic intervention.\", \"metrics\": {\"current_step\": 64000, \"eval_return_35K\": 299.5, \"eval_return_55K\": 31.9, \"note\": \"WARNING: NVE breached 1.5× at 55K (1.903), eval crashed 299→32. Possible CIVO despite TCN.\", \"target_steps\": 210000, \"ve_ratio_55K\": 1.903}, \"parent\": \"exp_027_tcn_walker_s0_sigma02\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"logdir/exp_030a_tcn_cheetah_s0_sigma02/\", \"checkpoint_source\": \"from_scratch\", \"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_enabled True --tcn_sigma 0.2 --logdir logdir/exp_030a_tcn_cheetah_s0_sigma02\", \"data_count\": \"210000 env steps\", \"data_path\": \"dmc_cheetah_run\", \"eval_data\": \"dmc_cheetah_run\", \"gpu\": \"cuda:0\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_030a_tcn_cheetah_s0_sigma02.log\", \"model_name\": \"dreamerv3_tcn_sigma02_cheetah\", \"seed\": 0, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T11:10:00.827Z\"}, \"exp_027_tcn_walker_s0\": {\"analysis_summary\": \"TCN (σ=0.5 noise on dt_embedding) FAILED to suppress CIVO. NVE breached 1.5× threshold 3 times: 55K(1.68×), 65K(1.54×), 85K(3.97×). Peak NVE 3.97× at 85K is HIGHER than typical CIVO, suggesting TCN destabilizes value learning. Eval peaked at 240 (35K), then collapsed to avg 117 in latter half — far below 450 target. Gate remained fixed at dt=2 throughout (zero entropy). The noise magnitude was insufficient to decorrelate critic estimates from dt conditioning. Training reached 120K/210K planned. Hypothesis falsified: forward-pass noise at σ=0.5 does not prevent critic from exploiting dt-specific value structure.\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_027_tcn_walker_s0/latest.pt\", \"completed_at\": \"2026-05-20T09:24:09.016Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-20T02:44:51.820Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-20T06:06:34.898602+00:00\"}]}, \"hypothesis\": \"Temporal Conditioning Noise (TCN): adding Gaussian noise (sigma=0.5) to dt_embedding during imagination rollouts reduces dt conditioning precision, preventing critic from learning dt-specific value bias. Predicts CIVO suppression (NVE < 1.5×) with eval > 50% baseline (~450+). Based on obs-decoder SGS failure (gradient-level intervention insufficient) → need forward-pass/representation-level intervention.\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_027_tcn_walker_s0.log\", \"metrics\": {\"eval_return_105K\": 95.5, \"eval_return_112K\": 99.5, \"eval_return_15K\": 154.6, \"eval_return_25K\": 223.6, \"eval_return_35K\": 240, \"eval_return_45K\": 101.2, \"eval_return_55K\": 70, \"eval_return_5K\": 37.4, \"eval_return_65K\": 95.1, \"eval_return_75K\": 189.2, \"eval_return_85K\": 36, \"eval_return_95K\": 166.4, \"final_step\": 120000, \"gate_dt_entropy\": 0, \"gate_dt_mean\": 2, \"last_5_eval_avg\": 117.3, \"nve_breach_count\": 3, \"nve_breach_steps\": \"55K(1.68), 65K(1.54), 85K(3.97)\", \"peak_eval\": 240, \"peak_eval_step\": \"35K\", \"peak_nve\": 3.965, \"peak_nve_step\": \"85K\", \"target_steps\": 210000, \"ve_ratio_105K\": 0.916, \"ve_ratio_15K\": 0.02, \"ve_ratio_25K\": 0.11, \"ve_ratio_35K\": 0.235, \"ve_ratio_45K\": 0.86, \"ve_ratio_55K\": 1.679, \"ve_ratio_65K\": 1.544, \"ve_ratio_75K\": 0.831, \"ve_ratio_85K\": 3.965, \"ve_ratio_95K\": 0.675}, \"parent\": \"exp_025_obs_sgs_walker_s1\", \"reproduce\": {\"finished_at\": \"2026-05-20T06:06:30.806Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --tcn_sigma 0.5 --logdir logdir/exp_027_tcn_walker_s0\\\"\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 3.18, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_027_tcn_walker_s0.log\", \"pid\": \"888715\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-20T06:13:35.505Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 11433.5}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T09:24:09.016Z\"}, \"exp_028_rave_walker_s0_ceil15\": {\"completed_at\": \"2026-05-20T08:31:12.389Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-20T03:25:34.045Z\", \"hypothesis\": \"RAVE ceiling sensitivity test: same as exp_028 (EMA-anchored value cap) but with ceiling=1.5 instead of 2.0. Tighter constraint tests whether more aggressive capping improves CIVO suppression without harming learning. If ceiling=2.0 works and 1.5 also works → method robust; if 1.5 hurts eval → ceiling choice is critical.\", \"metrics\": {\"current_step\": 135000, \"eval_return_105K\": 76.2, \"eval_return_115K\": 41.2, \"eval_return_125K\": 36.6, \"eval_return_135K\": 39.1, \"eval_return_15K\": 99.4, \"eval_return_25K\": 155.3, \"eval_return_35K\": 180.1, \"eval_return_45K\": 166.9, \"eval_return_55K\": 131, \"eval_return_5K\": 31.6, \"eval_return_65K\": 91.5, \"eval_return_75K\": 120.9, \"eval_return_85K\": 137.3, \"eval_return_95K\": 70.2, \"target_steps\": 210000, \"ve_ratio_105K\": 0.984, \"ve_ratio_115K\": 1.513, \"ve_ratio_125K\": 1.462, \"ve_ratio_135K\": 1.171, \"ve_ratio_15K\": 0.03, \"ve_ratio_25K\": 0.128, \"ve_ratio_35K\": 0.247, \"ve_ratio_45K\": 0.428, \"ve_ratio_55K\": 0.737, \"ve_ratio_65K\": 1.294, \"ve_ratio_75K\": 0.937, \"ve_ratio_85K\": 0.727, \"ve_ratio_95K\": 1.28}, \"parent\": \"exp_028_rave_walker_s0\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"~/runs/event-gated-adaptive-horizon/exp_028_rave_walker_s0_ceil15/\", \"checkpoint_source\": \"N/A (trained from scratch, hyperparameter variant of exp_028_rave_walker_s0)\", \"command\": \"bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --imag_horizon 8 --rave_enabled True --rave_ceiling 1.5 --rave_ema_decay 0.99 --logdir ~/runs/event-gated-adaptive-horizon/exp_028_rave_walker_s0_ceil15'\", \"data_count\": \"210000 env steps\", \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"dmc_walker_walk (online eval during training)\", \"gpu\": [\"cuda:1\"], \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_028_rave_walker_s0_ceil15.log\", \"model_name\": \"dreamerv3_rave_ceil15\", \"note\": \"CUDA_VISIBLE_DEVICES=1 set by submit_training_job, device=cuda:0 within process\", \"pid\": \"38372\", \"seed\": 0, \"server\": \"bjb1-40020\", \"tmux_session\": \"exp_028_rave_walker_s0_ceil15\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T08:31:12.389Z\"}, \"exp_028_rave_walker_s0\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_028_rave_walker_s0/checkpoint.ckpt\", \"completed_at\": \"2026-05-20T06:14:31.720Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-20T02:44:53.882Z\", \"hypothesis\": \"Reality-Anchored Value Estimation (RAVE): cap imagination critic values at ceiling*v_anchor (ceiling=2.0, v_anchor=EMA of real-state critic values). Directly prevents pathological value inflation (NVE>1.5×) by bounding imagination/reality value ratio. Based on CIVO core mechanism being imagination value explosion → this directly caps the ratio without modifying gradients or training dynamics.\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_028_rave_walker_s0/\", \"metrics\": {\"current_steps\": 105000, \"eval_trajectory\": {\"105K\": {\"eval_return\": 29, \"value_mean\": 92.2, \"ve_ratio\": 3.183}, \"15K\": {\"eval_return\": 105.3, \"value_mean\": 2.93, \"ve_ratio\": 0.028}, \"25K\": {\"eval_return\": 191.9, \"value_mean\": 24.4, \"ve_ratio\": 0.127}, \"35K\": {\"eval_return\": 204.6, \"ve_ratio\": 0.267}, \"45K\": {\"eval_return\": 197.7, \"ve_ratio\": 0.439}, \"55K\": {\"eval_return\": 193, \"ve_ratio\": 0.62}, \"5K\": {\"eval_return\": 37.4, \"value_mean\": 0.001}, \"65K\": {\"eval_return\": 79.8, \"ve_ratio\": 1.832}, \"75K\": {\"eval_return\": 44.5, \"ve_ratio\": 3.415}, \"85K\": {\"eval_return\": 57.7, \"ve_ratio\": 2.126}, \"95K\": {\"eval_return\": 25.9, \"value_mean\": 105.87, \"ve_ratio\": 4.086}}, \"note\": \"NEGATIVE. NVE diverged from 55K onward (0.62→4.09), eval collapsed 193→29. No self-correction.\"}, \"parent\": \"exp_025_obs_sgs_walker_s1\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"N/A (trained from scratch, derives from SGS failure line)\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 105000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --rave_ceiling 2.0 --logdir logdir/exp_028_rave_walker_s0\\\"\", \"data_count\": \"105000 env steps (52.5K agent steps, action_repeat=2)\", \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"dmc_walker_walk (online eval during training)\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 3.33, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_028_rave_walker_s0.log\", \"model_name\": \"dreamerv3_rave_ceil20\", \"pid\": \"879636\", \"seed\": 0, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-20T02:54:26.022Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 12005.7}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T06:14:31.720Z\"}, \"exp_025_obs_sgs_walker_s2\": {\"completed_at\": \"2026-05-20T03:14:06.591Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-19T16:39:26.941Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-20T03:14:13.011509+00:00\"}]}, \"failure_reason\": \"Reclassified: experiment completed 224K/210K steps normally. Cron misclassified as failed due to missing W&B sentinel. Actual result is negative — obs-decoder SGS suppressed CIVO (ve_ratio 0.8-1.4) but eval collapsed to ~90 (baseline ~930).\", \"hypothesis\": \"Obs-decoder-only SGS (stop-gradient only on observation decoder pathway to dt_embedding) will suppress CIVO while preserving reward head gradient signal. Based on gradient decomposition showing obs decoder (16-22%) not reward head (38-49%) carries the critical dt-specific spatial information driving the fidelity gap. Predicts NVE < 1.5× and eval > 70% baseline (~650+).\", \"metrics\": {\"eval_return_215K\": 89.6, \"target_steps\": 210000, \"train_steps_completed\": 224000, \"ve_ratio_175K\": 1.2, \"ve_ratio_185K\": 1.4, \"ve_ratio_215K\": 0.8}, \"notes\": \"Obs-decoder SGS s2 完成全部训练（224K/210K steps）。ve_ratio 全程 0.8-1.4（CIVO 部分抑制），但 eval_return 仅 66-90（baseline ~930，远低于 70% 阈值 ~650）。与 s1/s3/s4 一致：obs-decoder SGS 无法在抑制 CIVO 的同时保持性能。梯度干预路线全面否定（Full SGS 0/3 + Obs-decoder SGS 0/6 有效）。\", \"parent\": \"exp_018_full_sgs_walker_s1\", \"reproduce\": {\"finished_at\": \"2026-05-20T03:14:07.466Z\"}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"logdir/exp_025_obs_sgs_walker_s2/\", \"checkpoint_source\": \"N/A (trained from scratch)\", \"command\": \"CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 2 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --imag_horizon 8 --sgs_mode obs_decoder_only --logdir logdir/exp_025_obs_sgs_walker_s2\", \"data_count\": \"210000 env steps (105K agent steps)\", \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"dmc_walker_walk (online eval during training)\", \"gpu\": [\"cuda:1\"], \"log_path\": \"logdir/exp_025_obs_sgs_walker_s2/train.log\", \"model_name\": \"dreamerv3_obs_decoder_sgs\", \"pid\": \"7989\", \"seed\": 2, \"server\": \"bjb1-40020\", \"tmux_session\": \"exp_025_s2\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T03:17:26.061Z\"}, \"exp_026_obs_sgs_cheetah_s1\": {\"completed_at\": \"2026-05-20T03:02:46.556Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-19T20:19:29.171Z\", \"failure_reason\": \"startup recovery: process dead, no active cron monitor\", \"hypothesis\": \"Obs-decoder-only SGS on Cheetah Run: cross-environment validation that obs-decoder SGS suppresses CIVO in a second environment. Based on 010b showing Cheetah CIVO (NVE 8.27-70.64×), if obs-decoder SGS works, NVE should stay < 1.5× and eval > 70% of Cheetah baseline (~380+). Tests whether the gradient decomposition finding (obs decoder as critical pathway) generalizes beyond Walker.\", \"parent\": \"exp_010b_cheetah_civo_trigger\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"logdir/exp_026_obs_sgs_cheetah_s1/\", \"checkpoint_source\": \"N/A (trained from scratch)\", \"command\": \"CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 105000 --seed 1 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --sgs_mode obs_decoder_only --logdir logdir/exp_026_obs_sgs_cheetah_s1\", \"data_count\": \"105000 env steps\", \"data_path\": \"dmc_cheetah_run\", \"eval_data\": \"dmc_cheetah_run (online eval during training)\", \"gpu\": [\"cuda:1\"], \"log_path\": \"logdir/exp_026_obs_sgs_cheetah_s1/train.log\", \"model_name\": \"dreamerv3_obs_decoder_sgs_cheetah\", \"pid\": \"16346\", \"seed\": 1, \"server\": \"bjb1-40020\", \"tmux_session\": \"exp_026_s1\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T03:02:46.556Z\"}, \"exp_026_obs_sgs_cheetah_s0\": {\"completed_at\": \"2026-05-20T03:02:43.170Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-19T20:19:27.608Z\", \"failure_reason\": \"startup recovery: process dead, no active cron monitor\", \"hypothesis\": \"Obs-decoder-only SGS on Cheetah Run: cross-environment validation that obs-decoder SGS suppresses CIVO in a second environment. Based on 010b showing Cheetah CIVO (NVE 8.27-70.64×), if obs-decoder SGS works, NVE should stay < 1.5× and eval > 70% of Cheetah baseline (~380+). Tests whether the gradient decomposition finding (obs decoder as critical pathway) generalizes beyond Walker.\", \"parent\": \"exp_010b_cheetah_civo_trigger_s0\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"logdir/exp_026_obs_sgs_cheetah_s0/\", \"checkpoint_source\": \"N/A (trained from scratch)\", \"command\": \"CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 105000 --seed 0 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --sgs_mode obs_decoder_only --logdir logdir/exp_026_obs_sgs_cheetah_s0\", \"data_count\": \"105000 env steps\", \"data_path\": \"dmc_cheetah_run\", \"eval_data\": \"dmc_cheetah_run (online eval during training)\", \"gpu\": [\"cuda:0\"], \"log_path\": \"logdir/exp_026_obs_sgs_cheetah_s0/train.log\", \"model_name\": \"dreamerv3_obs_decoder_sgs_cheetah\", \"pid\": \"16208\", \"seed\": 0, \"server\": \"bjb1-40020\", \"tmux_session\": \"exp_026_s0\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T03:02:43.170Z\"}, \"exp_025_obs_sgs_walker_s4\": {\"completed_at\": \"2026-05-20T03:02:39.948Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-19T16:39:29.810Z\", \"failure_reason\": \"startup recovery: process dead, no active cron monitor\", \"hypothesis\": \"Obs-decoder-only SGS (stop-gradient only on observation decoder pathway to dt_embedding) will suppress CIVO while preserving reward head gradient signal. Based on gradient decomposition showing obs decoder (16-22%) not reward head (38-49%) carries the critical dt-specific spatial information driving the fidelity gap. Predicts NVE < 1.5× and eval > 70% baseline (~650+).\", \"parent\": \"exp_018_full_sgs_walker_s1\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"logdir/exp_025_obs_sgs_walker_s4/\", \"checkpoint_source\": \"N/A (trained from scratch)\", \"command\": \"CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 4 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --imag_horizon 8 --sgs_mode obs_decoder_only --logdir logdir/exp_025_obs_sgs_walker_s4\", \"data_count\": \"210000 env steps (105K agent steps)\", \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"dmc_walker_walk (online eval during training)\", \"gpu\": [\"cuda:1\"], \"log_path\": \"logdir/exp_025_obs_sgs_walker_s4/train.log\", \"model_name\": \"dreamerv3_obs_decoder_sgs\", \"pid\": \"851593\", \"seed\": 4, \"server\": \"bjb1-45299\", \"tmux_session\": \"exp_025_s4\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T03:02:39.948Z\"}, \"exp_025_obs_sgs_walker_s3\": {\"completed_at\": \"2026-05-20T03:02:36.670Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-19T16:39:28.402Z\", \"failure_reason\": \"startup recovery: process dead, no active cron monitor\", \"hypothesis\": \"Obs-decoder-only SGS (stop-gradient only on observation decoder pathway to dt_embedding) will suppress CIVO while preserving reward head gradient signal. Based on gradient decomposition showing obs decoder (16-22%) not reward head (38-49%) carries the critical dt-specific spatial information driving the fidelity gap. Predicts NVE < 1.5× and eval > 70% baseline (~650+).\", \"parent\": \"exp_018_full_sgs_walker_s1\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"logdir/exp_025_obs_sgs_walker_s3/\", \"checkpoint_source\": \"N/A (trained from scratch)\", \"command\": \"CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 3 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --imag_horizon 8 --sgs_mode obs_decoder_only --logdir logdir/exp_025_obs_sgs_walker_s3\", \"data_count\": \"210000 env steps (105K agent steps)\", \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"dmc_walker_walk (online eval during training)\", \"gpu\": [\"cuda:0\"], \"log_path\": \"logdir/exp_025_obs_sgs_walker_s3/train.log\", \"model_name\": \"dreamerv3_obs_decoder_sgs\", \"pid\": \"847597\", \"seed\": 3, \"server\": \"bjb1-45299\", \"tmux_session\": \"exp_025_s3\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T03:02:36.670Z\"}, \"exp_025_obs_sgs_walker_s1\": {\"completed_at\": \"2026-05-20T03:02:32.583Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-19T16:39:25.583Z\", \"failure_reason\": \"startup recovery: process dead, no active cron monitor\", \"hypothesis\": \"Obs-decoder-only SGS (stop-gradient only on observation decoder pathway to dt_embedding) will suppress CIVO while preserving reward head gradient signal. Based on gradient decomposition showing obs decoder (16-22%) not reward head (38-49%) carries the critical dt-specific spatial information driving the fidelity gap. Predicts NVE < 1.5× and eval > 70% baseline (~650+).\", \"parent\": \"exp_018_full_sgs_walker_s1\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"logdir/exp_025_obs_sgs_walker_s1/\", \"checkpoint_source\": \"N/A (trained from scratch)\", \"command\": \"CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 210000 --seed 1 --device cuda:0 --compile False --gate_enabled True --gate_fixed_dt 2 --imag_horizon 8 --sgs_mode obs_decoder_only --logdir logdir/exp_025_obs_sgs_walker_s1\", \"data_count\": \"210000 env steps (105K agent steps)\", \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"dmc_walker_walk (online eval during training)\", \"gpu\": [\"cuda:0\"], \"log_path\": \"logdir/exp_025_obs_sgs_walker_s1/train.log\", \"model_name\": \"dreamerv3_obs_decoder_sgs\", \"pid\": \"7833\", \"seed\": 1, \"server\": \"bjb1-40020\", \"tmux_session\": \"exp_025_s1\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-20T03:02:32.583Z\"}, \"exp_001_baseline_s4_extended\": {\"completed_at\": \"2026-05-19T23:06:42.122Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-19T09:02:31.737Z\", \"hypothesis\": \"Walker Walk baseline seed=4 extended to 505K. Third long-run baseline seed for multi-seed NVE normalization. s4@105K=922.8 (highest), obtaining full ve_ratio profile.\", \"metrics\": {\"convergence_mean_250k_plus\": 935, \"final_eval_return\": 938.86, \"final_step\": 520000, \"peak_eval_return\": 960.6}, \"parent\": \"exp_001_baseline_s4\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"logdir/exp_001_baseline_s4/\", \"checkpoint_source\": \"logdir/exp_001_baseline_s4/latest.pt\", \"command\": \"CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 505000 --seed 4 --device cuda:0 --compile False --gate_enabled False --logdir logdir/exp_001_baseline_s4\", \"data_count\": \"505000 env steps\", \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"dmc_walker_walk (online eval during training)\", \"gpu\": \"cuda:1\", \"log_path\": \"logdir/exp_001_baseline_s4/train_extended.log\", \"model_name\": \"dreamerv3_baseline\", \"resumed_from_step\": 112000, \"seed\": 4, \"server\": \"bjb1-45299\", \"target_steps\": 505000, \"tmux_session\": \"exp_s4_ext\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T23:06:42.122Z\"}, \"exp_001_baseline_s3_extended\": {\"completed_at\": \"2026-05-19T21:23:44.025Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-19T09:02:30.382Z\", \"hypothesis\": \"Walker Walk baseline seed=3 extended to 505K. Second long-run baseline seed (alongside s2_ext) for multi-seed NVE normalization robustness. s3@105K=869.0, testing convergence to 920+ level.\", \"metrics\": {\"eval_profile\": {\"102000\": 869.03, \"112000\": 898.89, \"120000\": 898.38, \"130000\": 837.74, \"140000\": 876.64, \"15000\": 224.27, \"150000\": 899.47, \"160000\": 922.77, \"170000\": 925.77, \"180000\": 912.89, \"190000\": 915.07, \"200000\": 894.77, \"210000\": 899.79, \"220000\": 951.18, \"230000\": 930.56, \"240000\": 910.47, \"25000\": 329.99, \"250000\": 914.02, \"260000\": 931.33, \"270000\": 954.65, \"280000\": 928.01, \"290000\": 947.4, \"300000\": 853.32, \"310000\": 906.35, \"320000\": 847.16, \"330000\": 934.78, \"340000\": 921.08, \"35000\": 413.12, \"350000\": 922.63, \"360000\": 844.99, \"370000\": 911.36, \"380000\": 917.73, \"390000\": 937.21, \"400000\": 928, \"410000\": 945.88, \"420000\": 897.2, \"430000\": 949.45, \"440000\": 937.28, \"45000\": 332.69, \"450000\": 924.24, \"460000\": 967.25, \"470000\": 940.55, \"480000\": 936.24, \"490000\": 944.67, \"5000\": 42.15, \"500000\": 957.09, \"510000\": 947.68, \"55000\": 519.91, \"65000\": 667.42, \"72000\": 771.33, \"82000\": 772.88, \"92000\": 854.6}, \"final_eval_return\": 947.68, \"final_step\": 520000, \"final_train_return_avg\": 945.4}, \"parent\": \"exp_001_baseline_s3\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"logdir/exp_001_baseline_s3/\", \"checkpoint_source\": \"logdir/exp_001_baseline_s3/latest.pt\", \"command\": \"CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 505000 --seed 3 --device cuda:0 --compile False --gate_enabled False --logdir logdir/exp_001_baseline_s3\", \"data_count\": \"505000 env steps\", \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"dmc_walker_walk (online eval during training)\", \"gpu\": \"cuda:0\", \"log_path\": \"logdir/exp_001_baseline_s3/train_extended.log\", \"model_name\": \"dreamerv3_baseline\", \"resumed_from_step\": 120000, \"seed\": 3, \"server\": \"bjb1-45299\", \"target_steps\": 505000, \"tmux_session\": \"exp_s3_ext\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T21:23:44.025Z\"}, \"exp_001_baseline_s2_extended\": {\"completed_at\": \"2026-05-19T17:44:27.212Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-19T04:10:10.948Z\", \"hypothesis\": \"Walker Walk baseline seed=2 extended to 505K. Tests whether low eval (443.5 @105K) is due to slow convergence or seed-level difference. s1=915.7, s3=869.0 at 105K.\", \"metrics\": {\"eval_return_at_105K\": 443.5, \"eval_return_final\": 945.7, \"eval_return_peak\": 962.6, \"total_steps\": 512000, \"value_mean_at_105K\": 329.16, \"value_mean_plateau\": 665, \"ve_ratio_at_105K\": 0.7422, \"ve_ratio_converged_range\": \"0.69-0.77\"}, \"parent\": \"exp_001_baseline_s2\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"logdir/exp_001_baseline_s2/latest.pt\", \"checkpoint_source\": \"logdir/exp_001_baseline_s2/latest.pt\", \"command\": \"CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 505000 --seed 2 --device cuda:0 --compile False --gate_enabled False --logdir logdir/exp_001_baseline_s2\", \"data_count\": 0, \"data_path\": \"logdir/exp_001_baseline_s2\", \"eval_data\": \"dmc_walker_walk (online eval)\", \"gpu\": \"cuda:1\", \"log_path\": \"logdir/exp_001_baseline_s2/train_extended.log\", \"model_name\": \"dreamerv3\", \"resumed_from_step\": 112000, \"seed\": 2, \"server\": \"bjb1-45299\", \"target_steps\": 505000, \"tmux_session\": \"exp_s2_ext\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T17:44:27.212Z\"}, \"exp_023_cheetah_baseline_s4_extended\": {\"completed_at\": \"2026-05-19T09:02:40.466Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-19T06:27:42.161Z\", \"hypothesis\": \"Cheetah Run baseline seed=4 extended to 300K. Tests whether eval drop at 194K→204K (537→302) is transient fluctuation or permanent collapse. Informs baseline stability and NVE normalization robustness.\", \"metrics\": {\"eval_302k\": 580, \"eval_peak_ext\": 642.3, \"eval_peak_ext_step\": 272000, \"note\": \"延长到 300K 确认非 collapse。eval 恢复到 642 peak@272K，200K-300K 区间震荡上行 (301-642 range)，194K→204K 骤降为 transient fluctuation。\"}, \"parent\": \"exp_023_cheetah_baseline_s4\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"logdir/exp_023_cheetah_baseline_s4/\", \"checkpoint_source\": \"logdir/exp_023_cheetah_baseline_s4/latest.pt\", \"command\": \"CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 300000 --seed 4 --device cuda:0 --compile False --gate_enabled False --checkpoint_every 10000 --logdir logdir/exp_023_cheetah_baseline_s4\", \"data_count\": \"300000 env steps\", \"data_path\": \"dmc_cheetah_run\", \"eval_data\": \"dmc_cheetah_run (online eval during training)\", \"gpu\": \"cuda:0\", \"log_path\": \"logdir/exp_023_cheetah_baseline_s4/train_extended.log\", \"model_name\": \"dreamerv3_baseline\", \"resumed_from_step\": 212000, \"seed\": 4, \"server\": \"bjb1-45299\", \"target_steps\": 300000, \"tmux_session\": \"exp_023_s4_ext\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T09:02:40.466Z\"}, \"exp_001_baseline_s4\": {\"completed_at\": \"2026-05-19T09:00:10.632Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-19T04:47:01.105Z\", \"hypothesis\": \"Walker Walk baseline seed=4. Fourth seed for 4-seed baseline CI. Tests whether s2 (443.5) is outlier or bimodal distribution (s1=915.7, s3=869.0).\", \"metrics\": {\"current_step\": 112000, \"eval_return_105k\": 922.8, \"peak_eval\": 922.8, \"peak_eval_step\": 105000, \"target_steps\": 105000, \"value_mean_final\": 576.1, \"ve_ratio_105k\": 0.624}, \"parent\": \"exp_001_baseline\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_001_baseline_s4\", \"checkpoint_source\": \"N/A\", \"command\": \"CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 105000 --seed 4 --device cuda:0 --compile False --gate_enabled False --logdir logdir/exp_001_baseline_s4\", \"data_count\": 0, \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"N/A\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_001_baseline_s4/metrics.jsonl\", \"model_name\": \"dreamerv3\", \"seed\": 4, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T09:00:10.632Z\"}, \"exp_023_cheetah_baseline_s4\": {\"completed_at\": \"2026-05-19T06:26:03.295Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T23:54:02.288Z\", \"hypothesis\": \"Cheetah Run baseline seed=4. Fourth seed for tighter eval return CI and NVE normalization robustness.\", \"metrics\": {\"current_step\": 212000, \"eval_return_194k\": 537.03, \"eval_return_204k\": 301.69, \"note\": \"Cheetah baseline s4. Large eval drop 194K→204K (537→302). ve_ratio>1 indicates value overestimation at final step.\", \"peak_eval\": 537.03, \"peak_eval_step\": 194000, \"target_steps\": 200000, \"value_mean_204k\": 339.14, \"ve_ratio_204k\": 1.124}, \"parent\": \"exp_023a_cheetah_baseline_s0\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_023_cheetah_baseline_s4\", \"checkpoint_source\": \"N/A (train from scratch)\", \"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 200000 --seed 4 --device cuda:0 --compile False --gate_enabled False --checkpoint_every 10000 --logdir logdir/exp_023_cheetah_baseline_s4\", \"data_count\": \"200K env steps\", \"data_path\": \"dmc_cheetah_run (online RL)\", \"eval_data\": \"dmc_cheetah_run eval episodes\", \"gpu\": \"cuda:0\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_023_cheetah_baseline_s4/metrics.jsonl\", \"model_name\": \"DreamerV3 (default)\", \"pid\": 774033, \"seed\": 4, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T06:26:03.295Z\"}, \"exp_023_cheetah_baseline_s3\": {\"completed_at\": \"2026-05-19T04:08:47.459Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T21:49:33.229Z\", \"hypothesis\": \"Cheetah Run baseline seed=3. Extends 023a/023b/023_s2 (3 seeds) to 4 seeds for tighter eval return CI.\", \"metrics\": {\"current_step\": 204000, \"eval_return_202k\": 642.13, \"peak_eval\": 685.93, \"peak_eval_step\": 172000, \"target_steps\": 200000, \"value_mean_final\": 445.42, \"ve_ratio_final\": 0.694}, \"parent\": \"exp_023a_cheetah_baseline_s0\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_023_cheetah_baseline_s3\", \"checkpoint_source\": \"N/A\", \"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 200000 --seed 3 --device cuda:0 --compile False --gate_enabled False --checkpoint_every 10000 --logdir logdir/exp_023_cheetah_baseline_s3\", \"data_count\": 0, \"data_path\": \"dmc_cheetah_run\", \"eval_data\": \"N/A\", \"gpu\": [\"cuda:1\"], \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_023_cheetah_baseline_s3/metrics.jsonl\", \"model_name\": \"dreamerv3\", \"pid\": \"768897\", \"seed\": 3, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T04:08:47.459Z\"}, \"exp_001_baseline_s3\": {\"completed_at\": \"2026-05-19T04:08:45.989Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T23:54:03.635Z\", \"hypothesis\": \"Walker Walk baseline seed=3. Third seed for tighter baseline eval CI.\", \"metrics\": {\"current_step\": 120000, \"eval_return_102k\": 869.03, \"peak_eval\": 898.89, \"peak_eval_step\": 112000, \"target_steps\": 105000, \"value_mean_final\": 622.2, \"ve_ratio_final\": 0.692}, \"parent\": \"exp_001_baseline\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_001_baseline_s3\", \"checkpoint_source\": \"N/A (train from scratch)\", \"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 105000 --seed 3 --device cuda:0 --compile False --gate_enabled False --logdir logdir/exp_001_baseline_s3\", \"data_count\": \"105K env steps\", \"data_path\": \"dmc_walker_walk (online RL)\", \"eval_data\": \"dmc_walker_walk eval episodes\", \"gpu\": \"cuda:1\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_001_baseline_s3/metrics.jsonl\", \"model_name\": \"DreamerV3 (default)\", \"pid\": 774106, \"seed\": 3, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T04:08:45.989Z\"}, \"exp_023_cheetah_baseline_s2\": {\"completed_at\": \"2026-05-19T00:13:55.909Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T16:05:14.249Z\", \"hypothesis\": \"Cheetah Run baseline additional seed for tighter CI. Extends 023a/023b (2 seeds) to 3 seeds.\", \"metrics\": {\"current_step\": 205000, \"eval_return_final\": 645.4, \"note\": \"Cheetah Run baseline seed=2. Third baseline seed for NVE normalization.\", \"target_steps\": 200000}, \"parent\": \"exp_023a_cheetah_baseline_s0\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_023_cheetah_baseline_s2\", \"checkpoint_source\": \"N/A\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --steps 200000 --seed 2 --device cuda:0 --compile False --gate_enabled False --checkpoint_every 10000 --logdir logdir/exp_023_cheetah_baseline_s2\\\"\", \"data_count\": 0, \"data_path\": \"dmc_cheetah_run\", \"eval_data\": \"N/A\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 8.13, \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_023_cheetah_baseline_s2/metrics.jsonl\", \"model_name\": \"dreamerv3\", \"pid\": \"753786\", \"seed\": 2, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-18T16:05:57.478Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 29278.4}, \"status\": \"DONE\", \"updated_at\": \"2026-05-19T00:13:55.909Z\"}, \"exp_008f_s4\": {\"completed_at\": \"2026-05-18T23:18:51.672Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-18T18:41:00.894Z\", \"hypothesis\": \"Walker Walk no-dt-emb (gate_dt_embed_dim=0) + subsample ON + fixed dt=2 + H=8, seed=4. Additional independent seed for 008f control (existing seeds: 1/008f, 2/009c, 3/008f_s3). C2 causal contrast robustness.\", \"metrics\": {\"civo_alert\": 0, \"eval_return_105k\": 306.5, \"note\": \"No CIVO. No-dt-emb control seed=4. Peak NVE 1.41x @85K (transient), settles to 0.58x @105K.\", \"nve_105k\": 0.58, \"peak_eval\": 487.5, \"peak_eval_step\": 55000, \"peak_nve\": 1.41, \"peak_nve_step\": 85000}, \"parent\": \"exp_008f_no_dt_embed_subsample_on_h8\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008f_no_dt_emb_s4\", \"checkpoint_source\": \"N/A\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008f_no_dt_emb_s4 --steps 105000 --seed 4 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"N/A\", \"gpu\": [\"cuda:0\"], \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008f_no_dt_emb_s4/metrics.jsonl\", \"model_name\": \"DreamerV3+FixedDt2_NoDtEmbed_Subsample_H8\", \"seed\": 4, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T23:18:51.672Z\"}, \"exp_009c_s3\": {\"completed_at\": \"2026-05-18T21:40:10.763Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T17:12:00.539Z\", \"hypothesis\": \"Walker Walk no-dt-emb (gate_dt_embed_dim=0) + subsample ON + fixed dt=2 + H=8, seed=3. Additional seed for 009c (seed=2 NVE 1.14x at 105K on upward trajectory); tests whether NVE rise is reproducible across independent seeds or stochastic.\", \"metrics\": {\"current_step\": 108000, \"eval_return_105k\": 311.92, \"note\": \"eval peaked at 55-65K (~457) then declined to 311.92. NVE 0.52x (no CIVO). 009c seed=2 NVE 1.14x not reproduced.\", \"nve_105k\": 0.52, \"target_steps\": 105000, \"value_mean_105k\": 120.27, \"ve_ratio_105k\": 0.386}, \"parent\": \"exp_009c_008f_walker_s2\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009c_no_dt_emb_s3\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009c_no_dt_emb_s3/metrics.jsonl\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T21:40:10.762Z\"}, \"exp_001_baseline_s2\": {\"completed_at\": \"2026-05-18T21:40:09.329Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T16:05:17.571Z\", \"hypothesis\": \"Walker Walk baseline additional seed for tighter evaluation return CI.\", \"metrics\": {\"current_step\": 112000, \"eval_return_105k\": 443.46, \"target_steps\": 105000, \"value_mean_105k\": 329.16, \"ve_ratio_105k\": 0.742}, \"parent\": \"exp_001_baseline\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_001_baseline_s2\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_001_baseline_s2/metrics.jsonl\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T21:40:09.329Z\"}, \"exp_008f_s2\": {\"completed_at\": \"2026-05-18T18:41:05.369Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-18T16:05:16.527Z\", \"hypothesis\": \"No-dt-emb control additional seed. Extends 008f (1 seed, NVE 0.97x) for C2 causal contrast robustness.\", \"parent\": \"exp_008f_no_dt_embed_subsample_on_h8\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"N/A\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && CUDA_VISIBLE_DEVICES=0 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008f_no_dt_emb_s2 --steps 105000 --seed 2 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"data_count\": 0, \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"N/A\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 2.58, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_008f_s2.log\", \"model_name\": \"dreamerv3\", \"pid\": \"754063\", \"seed\": 2, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-18T16:06:00.248Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 9305.1}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T18:41:05.369Z\"}, \"exp_008a_cheetah_unexposed_s1\": {\"completed_at\": \"2026-05-18T18:20:00.278Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T14:23:13.377Z\", \"hypothesis\": \"Cross-environment validation of C3 (unexposed dt_emb protection) on Cheetah Run, seed=1. If unexposed dt_emb (trained but subsample OFF, gate_subsample_max_dt=1) prevents CIVO in Cheetah as it does in Walker (008a: 3/3 healthy, NVE 0.43-0.93x), this strengthens the causal claim that multi-rate data exposure is the necessary CIVO trigger across environments.\", \"metrics\": {\"current_step\": 112000, \"eval_return_105k\": 504.38, \"nve_105k\": 0.478, \"target_steps\": 105000, \"value_mean_105k\": 156.97, \"ve_ratio_105k\": 0.3112}, \"parent\": \"exp_008a_no_subsample_dt2\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008a_cheetah_unexposed_s1\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008a_cheetah_unexposed_s1/metrics.jsonl\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T18:20:00.278Z\"}, \"exp_008a_cheetah_unexposed_s0\": {\"completed_at\": \"2026-05-18T18:19:58.491Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T14:23:12.052Z\", \"hypothesis\": \"Cross-environment validation of C3 (unexposed dt_emb protection) on Cheetah Run, seed=0. If unexposed dt_emb (trained but subsample OFF, gate_subsample_max_dt=1) prevents CIVO in Cheetah as it does in Walker (008a: 3/3 healthy, NVE 0.43-0.93x), this strengthens the causal claim that multi-rate data exposure is the necessary CIVO trigger across environments.\", \"metrics\": {\"current_step\": 112000, \"eval_return_105k\": 532.35, \"nve_105k\": 0.49, \"target_steps\": 105000, \"value_mean_105k\": 169.98, \"ve_ratio_105k\": 0.3193}, \"parent\": \"exp_008a_no_subsample_dt2\", \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008a_cheetah_unexposed_s0\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008a_cheetah_unexposed_s0/metrics.jsonl\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T18:19:58.491Z\"}, \"exp_009c_s2\": {\"completed_at\": \"2026-05-18T17:12:05.307Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-18T16:05:19.850Z\", \"hypothesis\": \"No-dt-emb H=15 additional seed. 009c seed=2 showed NVE 1.14x at 105K on upward trajectory; additional seed tests if this is reproducible or stochastic.\", \"parent\": \"exp_009c_008f_walker_s2\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"N/A\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && CUDA_VISIBLE_DEVICES=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009c_no_dt_emb_s2 --steps 105000 --seed 2 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"data_count\": 0, \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"N/A\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 1.1, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_009c_s2.log\", \"model_name\": \"dreamerv3\", \"pid\": \"754639\", \"seed\": 2, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-18T16:06:05.850Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 3959.5}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T17:12:05.307Z\"}, \"exp_008e_v3_s4\": {\"completed_at\": \"2026-05-18T11:33:57.033Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T02:54:56.392Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-18T11:31:45.212576+00:00\"}]}, \"hypothesis\": \"Walker Walk trained dt_emb + subsample ON + dt=1 imag + H=15, seed=4. C6 dual-pathway 多 seed 验证：当前 2 seeds 50% collapse rate（置信区间太宽），增加 seed 缩窄置信区间。Rebuttal 储备。\", \"metrics\": {\"civo\": false, \"eval_return\": 899.3, \"nve_note\": \"Corrected: was 0.61 (raw V/E ratio). Correct formula: max(V/E_exp / V/E_baseline_at_same_step) over [35K+]. 0.627/0.632=0.99 at 95K\", \"nve_peak\": 0.99, \"nve_peak_step\": 95000, \"ve_ratio_105k\": 0.609}, \"parent\": \"exp_008e_v3_subsample_on_dt1_h15\", \"reproduce\": {\"finished_at\": \"2026-05-18T11:31:41.800Z\"}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008e_v3_s4/latest.pt\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_008e_v3_s4.log\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T11:48:45.880Z\"}, \"exp_008e_v3_s3\": {\"completed_at\": \"2026-05-18T11:24:41.197Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-18T02:54:54.691Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-18T11:20:58.896484+00:00\"}]}, \"hypothesis\": \"Walker Walk trained dt_emb + subsample ON + dt=1 imag + H=15, seed=3. C6 dual-pathway 多 seed 验证：当前 2 seeds 50% collapse rate（置信区间太宽），增加 seed 缩窄置信区间。Rebuttal 储备。\", \"metrics\": {\"actor_entropy_final\": -4.892, \"collapse_onset\": \"85K-95K\", \"eval_return\": 92.7, \"gate_dt_1_frac\": 1, \"gate_dt_mean\": 1, \"nve_note\": \"Corrected: was 5.00 (worker used wrong baseline). Correct formula: V/E_exp / V/E_baseline_at_same_step. 2.635/0.656=4.02\", \"nve_peak\": 4.02, \"nve_peak_step\": 105000, \"peak_eval\": 520.4, \"peak_step\": 85000, \"ve_ratio_105k\": 2.635}, \"parent\": \"exp_008e_v3_subsample_on_dt1_h15\", \"reproduce\": {\"finished_at\": \"2026-05-18T11:20:55.020Z\"}, \"retry_count\": 0, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008e_v3_s3/latest.pt\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_008e_v3_s3.log\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T11:48:43.665Z\"}, \"exp_008a_unexposed_s1\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008a_unexposed_s1/latest.pt\", \"completed_at\": \"2026-05-18T08:16:42.716Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T05:13:56.020Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-18T08:12:12.866455+00:00\"}]}, \"hypothesis\": \"Walker Walk unexposed trained dt_emb + subsample OFF (gate_subsample_max_dt=1) + gate_fixed_dt=2 + H=15 (default), seed=1. 直接复现 008a_no_subsample_dt2 配置（eval=778, V-recovery, no CIVO）。C3 reproducibility rebuttal 储备。\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008a_unexposed_s1/metrics.jsonl\", \"metrics\": {\"civo_alert\": 0, \"civo_delta_ve_final\": -0.0028, \"civo_ve_ratio_final\": 0.43, \"eval_return_15k\": 167.12, \"eval_return_25k\": 139.94, \"eval_return_35k\": 394.15, \"eval_return_45k\": 414.32, \"eval_return_55k\": 441.48, \"eval_return_5k\": 31, \"eval_return_65k\": 491.74, \"eval_return_75k\": 452.34, \"eval_return_85k\": 546.82, \"eval_return_95k\": 628.57, \"eval_return_final\": 630.91, \"gate_dt_2_frac\": 1, \"gate_dt_mean\": 2, \"target_mean_final\": 272.13, \"total_steps\": 105000, \"value_mean_final\": 271.36}, \"parent\": \"exp_008a_no_subsample_dt2\", \"reproduce\": {\"finished_at\": \"2026-05-18T08:12:09.402Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"train_from_scratch\", \"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008a_unexposed_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 1 --checkpoint_every 25000\", \"data_count\": 0, \"data_path\": \"dmc_walker_walk (online RL)\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 3.03, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_008a_unexposed_s1.log\", \"model_name\": \"DreamerV3+FixedDt2_NoSubsample (unexposed trained dt_emb, H=15)\", \"pid\": \"724312\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-18T05:15:06.654Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 10896.1}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T08:16:42.716Z\"}, \"exp_008a_unexposed_s2\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008a_unexposed_s2/latest.pt\", \"completed_at\": \"2026-05-18T08:10:06.059Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T05:13:57.340Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-18T08:07:33.602043+00:00\"}]}, \"hypothesis\": \"Walker Walk unexposed trained dt_emb + subsample OFF (gate_subsample_max_dt=1) + gate_fixed_dt=2 + H=15 (default), seed=2. 008a 新 seed 验证 protection 是否 reproducible。C3 rebuttal 储备。\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008a_unexposed_s2/metrics.jsonl\", \"metrics\": {\"civo_alert\": 0, \"civo_delta_ve_final\": -0.003, \"civo_ve_ratio_final\": 0.333, \"eval_return_55k\": 607.5, \"eval_return_65k\": 653.8, \"eval_return_75k\": 534.4, \"eval_return_85k\": 605.4, \"eval_return_95k\": 819.4, \"eval_return_final\": 899.4, \"gate_dt_2_frac\": 1, \"gate_dt_mean\": 2, \"target_mean_final\": 300.3, \"total_steps\": 105000, \"value_mean_final\": 299.4}, \"parent\": \"exp_008a_no_subsample_dt2\", \"reproduce\": {\"finished_at\": \"2026-05-18T08:07:27.087Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"train_from_scratch\", \"command\": \"python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008a_unexposed_s2 --steps 105000 --seed 2 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 1 --checkpoint_every 25000\", \"data_count\": 0, \"data_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon\", \"eval_data\": \"dmc_walker_walk (online eval during training)\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 2.84, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_008a_unexposed_s2.log\", \"model_name\": \"DreamerV3+FixedDt2_NoSubsample (unexposed trained dt_emb, H=15)\", \"pid\": \"724965\", \"seed\": 2, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-18T05:19:26.303Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 10239.8}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T08:10:17.263Z\"}, \"exp_008a_untrained_s1\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-18T02:54:51.398Z\", \"hypothesis\": \"(cancelled) 原为 015b 模板 frozen dt_emb 多 seed，Director 修正为 008a unexposed 模板\", \"notes\": \"Director 修正：C3 rebuttal 应复现 008a (unexposed trained dt_emb, subsample OFF) 而非 015b (frozen)。替换为 exp_008a_unexposed_s1/s2。\", \"parent\": \"exp_015b_frozen_dt_emb\", \"retry_count\": 0, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T05:13:30.000Z\"}, \"exp_008a_untrained_s2\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-18T02:54:53.011Z\", \"hypothesis\": \"(cancelled) 原为 015b 模板 frozen dt_emb 多 seed，Director 修正为 008a unexposed 模板\", \"notes\": \"Director 修正：同上。\", \"parent\": \"exp_015b_frozen_dt_emb\", \"retry_count\": 0, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T05:13:30.000Z\"}, \"exp_010b_cheetah_civo_trigger_s0\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_010b_cheetah_civo_trigger_s0/latest.pt\", \"completed_at\": \"2026-05-18T05:11:15.900Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-18T02:02:47.702Z\", \"hypothesis\": \"Cheetah Run CIVO trigger seed=0: trained dt_emb + subsample ON + H=8. 第二 seed 复现 Cheetah CIVO (NVE>1.5×)，加强跨环境因果论证统计力度。Rebuttal 储备。\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_010b_cheetah_civo_trigger_s0/metrics.jsonl\", \"metrics\": {\"civo\": true, \"civo_onset_step\": \"65K\", \"detector_alert_step\": \"95K\", \"eval_return_105K\": 0.83, \"eval_return_peak\": 247.77, \"eval_return_peak_step\": \"35K\", \"gate_dt_mean\": 2, \"gate_entropy\": 0, \"nve_105K\": 70.64, \"nve_95K\": 6.34}, \"parent\": \"exp_010b_cheetah_civo_trigger\", \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"N/A (training from scratch)\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_010b_cheetah_civo_trigger_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --checkpoint_every 25000\\\"\", \"data_count\": 0, \"data_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon\", \"eval_data\": \"dmc_cheetah_run (online RL)\", \"gpu\": \"cuda:1\", \"model_name\": \"DreamerV3-cheetah-civo-trigger\", \"pid\": \"715412\", \"seed\": 0, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T05:11:15.900Z\"}, \"exp_024b_cheetah_no_dt_emb_s0\": {\"completed_at\": \"2026-05-18T02:00:15.236Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-17T22:50:34.104Z\", \"hypothesis\": \"Cheetah Run no-dt-emb causal control: dt_embed_dim=0 + subsample ON + H=8. 预期无CIVO（健康基线水平），证明trained dt_emb是Cheetah CIVO的必要条件。对应Walker的008f逻辑，完成Cheetah因果三角。\", \"metrics\": {\"civo\": false, \"eval_return_final\": 96.5, \"nve_peak\": 0.2}, \"notes\": \"No CIVO (NVE peak <0.2×). Confirms C2: trained dt_emb is necessary for Cheetah CIVO. eval 96.5 = 17.6% of baseline (548.3). Cheetah causal triangle seed 1 complete. Director confirmed results in D089.\", \"parent\": \"exp_010b_cheetah_civo_trigger\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_024b_cheetah_no_dt_emb_s0/latest.pt\", \"checkpoint_source\": \"N/A-training-from-scratch\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_024b_cheetah_no_dt_emb_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0 --checkpoint_every 25000\\\"\", \"data_count\": 0, \"data_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon\", \"eval_data\": \"dmc_cheetah_run-online-eval\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 3.13, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_024b_cheetah_no_dt_emb_s0.log\", \"model_name\": \"DreamerV3-cheetah-no-dt-emb\", \"pid\": \"705742\", \"seed\": 0, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-17T22:52:15.808Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 11279.4}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T02:00:17.832Z\"}, \"exp_024b_cheetah_no_dt_emb_s1\": {\"account\": \"root\", \"completed_at\": \"2026-05-18T01:56:17.025Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-17T22:51:53.604Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-18T01:52:09.175571+00:00\"}]}, \"gpu\": \"cuda:1\", \"hypothesis\": \"Cheetah Run no-dt-emb causal control seed=1: gate_dt_embed_dim=0 + subsample ON + H=8. 第二 seed 验证 024 的结论（trained dt_emb 是 Cheetah CIVO 必要条件），加强因果三角的统计力度。\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_024b_cheetah_no_dt_emb_s1.log\", \"metrics\": {\"baseline_pct\": 14.1, \"civo\": false, \"eval_return_final\": 77.3, \"eval_return_peak\": 129.6, \"gate_dt_2_frac\": 1, \"nve_peak\": 0.1, \"peak_step\": 15000}, \"notes\": \"No CIVO (NVE peak 0.10×, civo_alert=0 throughout). Confirms C2: trained dt_emb is necessary for Cheetah CIVO. Gate locked at dt=2 (gate_dt_2_frac=1.0), eval 77.3 = 14% of baseline (548.3). Low performance expected: dt_embed_dim=0 removes temporal abstraction capability. Cheetah causal triangle seed 2 complete.\", \"parent\": \"exp_024_cheetah_no_dt_emb_s0\", \"pid\": \"706158\", \"reproduce\": {\"code_commit\": \"3328f53cb32cda27e85b099d560256aeb01db998\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_024b_cheetah_no_dt_emb_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0 --checkpoint_every 25000\\\"\", \"finished_at\": \"2026-05-18T01:52:05.296Z\"}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_024b_cheetah_no_dt_emb_s1/latest.pt\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_024b_cheetah_no_dt_emb_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0 --checkpoint_every 25000\\\"\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 3.06, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_024b_cheetah_no_dt_emb_s1.log\", \"pid\": \"706158\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-17T22:52:30.631Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 11026.4}, \"status\": \"DONE\", \"updated_at\": \"2026-05-18T01:56:17.025Z\"}, \"exp_024_cheetah_no_dt_emb_s0\": {\"account\": \"root\", \"completed_at\": \"2026-05-17T20:35:13.253Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-17T20:34:13.657Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-17T20:35:16.021173+00:00\"}, {\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-17T22:57:54.400584+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"failure_reason\": \"EXIT_CODE=129 (non-zero)\", \"gpu\": \"cuda:0\", \"hypothesis\": \"Cheetah Run no-dt-emb causal control: dt_embed_dim=0 + subsample ON + H=8. 预期无CIVO（健康基线水平），证明trained dt_emb是Cheetah CIVO的必要条件。对应Walker的008f逻辑，完成Cheetah因果三角（023a/b baseline健康 + 010b CIVO collapse + 本实验 no-emb 健康）。\", \"parent\": \"exp_010b_cheetah_civo_trigger\", \"reproduce\": {\"code_commit\": \"3328f53cb32cda27e85b099d560256aeb01db998\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_024_cheetah_no_dt_emb_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0 --checkpoint_every 25000\\\"\", \"finished_at\": \"2026-05-17T22:57:48.608Z\"}, \"retry_count\": 2, \"server\": \"bjb1-45299\", \"spec\": {\"checkpoint_source\": \"N/A (training from scratch)\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_024_cheetah_no_dt_emb_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0 --checkpoint_every 25000\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_cheetah_run (online RL)\", \"eval_data\": \"N/A (online RL)\", \"model_name\": \"DreamerV3-no-dt-emb\", \"seed\": 0, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T23:21:27.867Z\"}, \"exp_021_full_sgs_cheetah_s1\": {\"account\": \"root\", \"completed_at\": \"2026-05-17T22:49:15.021Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-16T20:24:30.695Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-17T22:45:35.442053+00:00\"}]}, \"gpu\": \"cuda:1\", \"hypothesis\": \"Full-SGS Cheetah Run — 验证 SGS intervention 跨环境一致性。如果 CIVO mechanism 跨环境一致，Full-SGS 在 Cheetah 也应消除 NVE>1.5x (对比 010b: NVE 8.63×, collapse)。\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_021_full_sgs_cheetah_s1.log\", \"metrics\": {\"baseline_pct\": 38.7, \"civo\": true, \"civo_type\": \"transient_self_correcting\", \"eval_return_final\": 221.5, \"nve_peak\": 9.94, \"nve_peak_step\": \"45K\", \"nve_sustained_55K_105K\": 0.338, \"vs_010b\": \"221.5 vs 51.7 (4.3x better)\"}, \"notes\": \"P0 priority (D070 最重要数据缺口). 018_s2 完成后立即上 cuda:0. 排序: 021 先 → 008d_s1 后. Director 2026-05-16 确认.\", \"parent\": \"exp_010b_cheetah_civo_trigger\", \"pid\": \"696201\", \"reproduce\": {\"code_commit\": \"3328f53cb32cda27e85b099d560256aeb01db998\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_021_full_sgs_cheetah_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --full_sgs True --checkpoint_every 25000\\\"\", \"finished_at\": \"2026-05-17T22:45:32.093Z\", \"gpu\": \"cuda:1\", \"server\": \"bjb1-45299\", \"started_at\": \"2026-05-17T19:28:08.484Z\", \"training_hours\": 3.29}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_021_full_sgs_cheetah_s1/checkpoint.pt\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_021_full_sgs_cheetah_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --full_sgs True --checkpoint_every 25000\\\"\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 3.32, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_021_full_sgs_cheetah_s1.log\", \"pid\": \"696201\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-17T19:30:02.581Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 11952.4}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T22:57:30.295Z\"}, \"exp_023a_cheetah_baseline_s0\": {\"completed_at\": \"2026-05-17T20:34:04.841Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-17T11:53:19.690Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-17T20:31:37.915652+00:00\"}]}, \"hypothesis\": \"Cheetah Run vanilla DreamerV3 baseline (dt=1, no temporal embedding, no gate). Establishes Cheetah-specific baseline for NVE normalization and cross-environment validation. Comparison target for 010b (Cheetah CIVO trigger, NVE 8.27×).\", \"metrics\": {\"civo\": false, \"eval_return_final\": 624.7, \"eval_return_peak\": 624.7, \"peak_step\": 205000}, \"notes\": \"Healthy baseline. Last-5 eval mean=554.4. 185K瞬态VE spike(0.906)触发警报但20K步内恢复(205K:624.7)，非CIVO。双seed baseline均值: last-5=548.3, peak=598.8。未接W&B。\", \"reproduce\": {\"finished_at\": \"2026-05-17T20:31:34.777Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_023a_cheetah_baseline_s0/checkpoint.pt\", \"command\": \"bash -c \\\"cd /root/autodl-tmp/event-gated-adaptive-horizon && bash scripts/exp_023a_cheetah_baseline_s0.sh\\\"\", \"data_count\": \"N/A (online RL)\", \"data_path\": \"dmc_cheetah_run\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 5.66, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_023a_cheetah_baseline_s0.log\", \"model_name\": \"DreamerV3\", \"pid\": \"683708\", \"seed\": 0, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-17T14:54:17.553Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 20387.3}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T20:41:57.147Z\"}, \"exp_010b_cheetah_civo_trigger\": {\"completed_at\": \"2026-05-16T16:16:00.478Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-16T13:04:55.508Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-16T16:11:35.101384+00:00\"}]}, \"hypothesis\": \"Cheetah Run CIVO trigger — trained dt_emb, subsample ON, dt=2, H=8, seed 1. 跨环境验证：Walker 上 008d 配置在 Cheetah 上是否同样触发 CIVO (NVE>1.5x)。若成立→回应 reviewer \\\"single environment\\\" concern。\", \"metrics\": {\"civo\": true, \"eval_return_final\": 51.7, \"eval_return_peak\": 321.9, \"nve_peak\": 8.27, \"nve_peak_step\": 65000, \"peak_step\": 35000}, \"parent\": \"exp_010a_cheetah_baseline_s1\", \"reproduce\": {\"finished_at\": \"2026-05-16T16:11:32.766Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_010b_cheetah_civo_trigger/latest.pt\", \"checkpoint_source\": \"N/A (training from scratch, parent is baseline reference)\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_010b_cheetah_civo_trigger --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8\\\"\", \"data_count\": 105000, \"data_path\": \"dm_control cheetah_run (online RL)\", \"eval_data\": \"N/A (online RL, not eval experiment)\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 3.18, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_010b_cheetah_civo_trigger.log\", \"model_name\": \"DreamerV3+dt_emb(trained)+subsample+H8\", \"pid\": \"585826\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-16T13:05:10.473Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 11450.0}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T20:41:38.129Z\"}, \"exp_023b_cheetah_baseline_s1\": {\"completed_at\": \"2026-05-17T19:29:52.643Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-17T11:53:21.197Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-17T19:25:39.255677+00:00\"}]}, \"hypothesis\": \"Cheetah Run vanilla DreamerV3 baseline (dt=1, no temporal embedding, no gate), seed=1. Second seed for Cheetah baseline to establish robust NVE normalization across seeds.\", \"metrics\": {\"civo\": false, \"eval_return_final\": 520.3, \"eval_return_peak\": 572.9, \"peak_step\": 195000, \"ve_ratio_range\": \"0.5-0.7\"}, \"notes\": \"Healthy baseline. Last-5 eval mean=542.2 (for NVE normalization). 125K后进入500-573区间震荡，无collapse。待023a完成后取双seed均值作为Cheetah baseline。未接W&B，数据在本地logdir。\", \"reproduce\": {\"finished_at\": \"2026-05-17T19:25:34.295Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_023b_cheetah_baseline_s1/checkpoint.pt\", \"command\": \"bash -c \\\"cd /root/autodl-tmp/event-gated-adaptive-horizon && bash scripts/exp_023b_cheetah_baseline_s1.sh\\\"\", \"data_count\": \"N/A (online RL)\", \"data_path\": \"dmc_cheetah_run\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 5.5, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_023b_cheetah_baseline_s1.log\", \"model_name\": \"DreamerV3\", \"pid\": \"680126\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-17T13:59:45.409Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 19807.2}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T19:30:46.627Z\"}, \"exp_019b_pickcube_civo_trigger\": {\"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_019b_pickcube_civo_trigger/checkpoint.ckpt\", \"completed_at\": \"2026-05-17T03:35:47.561Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-16T03:23:51.568Z\", \"error_summary\": \"KeyError in dreamer.py:421 — configs[\\\"maniskill\\\"] not found. Config block missing from dreamer.py.\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-17T03:35:50.727034+00:00\"}, {\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-17T14:49:42.379952+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"2026-05-17 04:01: Registry shows DONE(failed) from first attempt (KeyError transient). Actual state: RUNNING (PID 646809, step 8400+, started 11:39 UTC). Cron monitoring via submit_on_allocated tmux session. Will need manual status correction when cron detects completion.\"}}, \"failure_reason\": \"Traceback → Traceback (most recent call last): File \\\"/root/autodl-tmp/event-gated-adaptive-horizon/dreamer.py\\\", line 421, in &lt;module> recursive_update(defaults, configs[name]) ~~~~~~~^^^^^^ KeyError: 'maniskill'\", \"gpu\": \"cuda:0\", \"hypothesis\": \"PickCube-v1 CIVO trigger — trained dt_emb, subsample ON, dt=2 imagination, H=8. 预期触发 CIVO（trained dt_emb → NVE>1.5x → collapse），验证 CIVO 在 manipulation 环境是否成立\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_019b_pickcube_civo_trigger.log\", \"metrics\": {\"baseline_eval_final\": 58.56, \"baseline_ratio\": 0.455, \"eval_return_final\": 26.64, \"eval_return_peak\": 26.9, \"eval_return_peak_step\": 132500, \"gate_dt_2_frac\": 1, \"gate_entropy\": 0, \"nve_final\": 0.065, \"nve_peak\": 3.78, \"nve_peak_step\": 52500, \"pattern\": \"transient_civo_then_value_collapse\", \"total_steps\": 200000, \"value_baseline_final\": 144.57, \"value_mean_final\": 4.26}, \"notes\": \"Cross-env CIVO confirmation + detector TN. Raw V/E peak=5.66 @52.5K (NVE=3.78× vs baseline). Transient CIVO: onset ~22.5K → peak 52.5K → deflation → eval partial recovery. Detector correctly doesn't trigger (oscillating V/E, max streak=2 < threshold=3). Eval final 26.64 vs baseline 58.56 = 45.5%. Value permanently collapsed (4.26 vs baseline 144.57). PickCube pattern: acute crisis + permanent damage, vs Walker sustained escalation.\", \"parent\": \"exp_019a_v2_pickcube_baseline\", \"reproduce\": {\"code_commit\": \"3328f53cb32cda27e85b099d560256aeb01db998\", \"command\": \"bash -c \\\"unset CUDA_VISIBLE_DEVICES && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults maniskill --task maniskill_PickCube-v1 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --seed 1 --steps 200000 --compile False --device cuda:0 --logdir ./logdir/exp_019b_pickcube_civo_trigger\\\"\", \"finished_at\": \"2026-05-17T14:49:39.328Z\", \"gpu\": \"cuda:0\", \"server\": \"bjb1-45299\", \"started_at\": \"2026-05-17T03:25:03.091Z\", \"training_hours\": 11.41}, \"retry_count\": 1, \"server\": \"bjb1-45299\", \"spec\": {\"checkpoint_source\": \"N/A (training from scratch)\", \"command\": \"cd /root/autodl-tmp/event-gated-adaptive-horizon && CUDA_ID=0 bash scripts/exp_019b_pickcube_civo_trigger.sh\", \"data_count\": \"online\", \"data_path\": \"maniskill_PickCube-v1 (state-based, online RL)\", \"eval_data\": \"N/A (online RL, not eval)\", \"gpu_id\": \"cuda:0\", \"model_name\": \"DreamerV3 + trained dt_emb + gate (maniskill_state config)\", \"pid\": 649577, \"seed\": 1, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T15:20:38.182Z\"}, \"exp_022b_no_curriculum\": {\"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_022b_no_curriculum/checkpoint.ckpt\", \"completed_at\": \"2026-05-17T14:01:23.413Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-17T10:49:08.181Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-17T13:56:29.726988+00:00\"}]}, \"gpu\": \"cuda:1\", \"hypothesis\": \"Frozen dt_emb (random init, no gradients) + learned gate WITHOUT curriculum (phase1=0, phase2=0, gate fully unlocked from step 0). Tests whether frozen dt_emb prevents CIVO (NVE < 1.5×) while allowing the gate to learn meaningful temporal abstraction (gate_dt_1_frac < 1.0). exp_022 was inconclusive because curriculum locked gate for the entire run; this rerun removes that confound.\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_022b_no_curriculum.log\", \"metrics\": {\"civo_alert_max\": 0, \"eval_return_105K\": 300.7, \"gate_dt_1_frac_105K\": 0.145, \"gate_dt_mean_105K\": 3.41, \"gate_entropy_ratio_105K\": 0.912, \"gate_near_uniform\": true, \"nve_peak\": 1.22, \"ve_ratio_105K\": 0.075, \"ve_ratio_peak\": 0.218}, \"notes\": \"Frozen dt_emb (random init, no gradients) successfully prevents CIVO: ve_ratio peaked 0.218 (NVE≈1.22×), civo_alert=0 throughout. Confirms C2 (trained dt_emb is necessary for CIVO). Gate converges to near-uniform distribution (entropy_ratio=0.912, no temporal coherence), eval_return=300.7 (32.8% of baseline@105K=915.7). Frozen random dt_emb is sufficient CIVO fix but insufficient for meaningful temporal abstraction — multi-rate imagination's inherent performance limitation.\", \"parent\": \"exp_022_untrained_dt_emb_learned_gate\", \"pid\": \"670554\", \"reproduce\": {\"code_commit\": \"3328f53cb32cda27e85b099d560256aeb01db998\", \"command\": \"bash -c \\\"unset CUDA_VISIBLE_DEVICES && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_EGL_DEVICE_ID=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python -u dreamer.py --configs dmc_proprio --task dmc_walker_walk --steps 105000 --seed 0 --device cuda:1 --compile False --checkpoint_every 10000 --gate_enabled True --gate_dt_embed_dim 32 --dt_emb_freeze True --gate_subsample_min_dt 1 --gate_subsample_max_dt 2 --gate_curriculum_phase1 0 --gate_curriculum_phase2 0 --imag_horizon 8 --logdir ./logdir/exp_022b_no_curriculum\\\"\", \"finished_at\": \"2026-05-17T13:56:27.483Z\"}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"unset CUDA_VISIBLE_DEVICES && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_EGL_DEVICE_ID=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python -u dreamer.py --configs dmc_proprio --task dmc_walker_walk --steps 105000 --seed 0 --device cuda:1 --compile False --checkpoint_every 10000 --gate_enabled True --gate_dt_embed_dim 32 --dt_emb_freeze True --gate_subsample_min_dt 1 --gate_subsample_max_dt 2 --gate_curriculum_phase1 0 --gate_curriculum_phase2 0 --imag_horizon 8 --logdir ./logdir/exp_022b_no_curriculum\\\"\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 3.16, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_022b_no_curriculum.log\", \"pid\": \"670554\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-17T10:51:56.898Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 11366.5}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T14:20:12.115Z\"}, \"exp_022_untrained_dt_emb_learned_gate\": {\"completed_at\": \"2026-05-17T07:44:38.596Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-17T04:16:57.150Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-17T07:44:42.334281+00:00\"}, {\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-17T10:47:17.307752+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"failure_reason\": \"Config error: used --configs dmc_vision (CNN+image, wrong modality) instead of dmc_proprio, and --compile True (torch.compile inductor crash). Killed and resubmitting with correct config.\", \"gpu\": \"cuda:1\", \"hypothesis\": \"Frozen dt_emb (random init, no gradients) prevents CIVO by blocking the trained-embedding-driven value overestimation feedback loop, while the learned gate (Gumbel-softmax, receives gradients) retains adaptive horizon selection capability. If successful, this decouples temporal abstraction benefits from CIVO vulnerability.\", \"metrics\": {\"civo_alert\": 0, \"civo_ve_ratio_105K\": 0.4, \"eval_return_105K\": 189.1, \"eval_return_65K\": 493.1, \"eval_return_75K\": 573.8, \"final_eval_return\": 189.1, \"gate_collapsed\": true, \"gate_dt_1_frac\": 1, \"gate_entropy\": 0, \"peak_eval_return\": 573.8, \"train_return_112K\": 91.8}, \"notes\": \"INCONCLUSIVE: Gate never activated due to curriculum misconfiguration. phase1=50000 × action_repeat=2 = 100K logger steps, experiment only 105K total. gate_scale reached only 0.006, gate locked at dt=1 entire run. eval_return: 75K=573.8 → 105K=189.1 (collapsed without gate involvement). Rerun as exp_022b with curriculum disabled.\", \"parent\": \"exp_008f_s3_no_dt_embed_walker + exp_005_gate_arch (combines safe dt_emb from 008f with gate architecture from 005 series)\", \"reproduce\": {\"finished_at\": \"2026-05-17T10:47:12.534Z\"}, \"retry_count\": 1, \"server\": \"bjb1-45299\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_022_untrained_dt_emb_learned_gate/checkpoint.ckpt\", \"checkpoint_source\": \"N/A (training from scratch)\", \"command\": \"bash -c \\\"unset CUDA_VISIBLE_DEVICES && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && MUJOCO_EGL_DEVICE_ID=1 LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python -u dreamer.py --configs dmc_proprio --task dmc_walker_walk --steps 105000 --seed 0 --device cuda:1 --compile False --checkpoint_every 10000 --gate_enabled True --gate_dt_embed_dim 32 --dt_emb_freeze True --gate_subsample_min_dt 1 --gate_subsample_max_dt 2 --imag_horizon 8 --logdir ./logdir/exp_022_untrained_dt_emb_learned_gate\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk (online RL, proprio obs)\", \"eval_data\": \"N/A (online RL, not eval)\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 3.03, \"gpu_id\": \"cuda:1\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_022_untrained_dt_emb_learned_gate.log\", \"model_name\": \"DreamerV3 + frozen dt_emb (d=32) + learned gate (Gumbel-softmax)\", \"pid\": 661595, \"seed\": 0, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-17T07:47:20.391Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 10901.2}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T10:56:34.274Z\"}, \"exp_019a_v2_pickcube_baseline\": {\"completed_at\": \"2026-05-16T21:07:12.193Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-16T20:12:22.372Z\", \"extra\": {\"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"2026-05-16 22:54: Resubmitted with CVD fix (unset CUDA_VISIBLE_DEVICES inside bash -c). PID 629444. ManiSkill3/SAPIEN requires physical device access — CVD breaks resolve_physical_device(). Using MUJOCO_EGL_DEVICE_ID=1 + --device cuda:1 directly.\"}}, \"failure_reason\": \"startup recovery: RUNNING with no cron and no server/pid info\", \"gpu\": \"cuda:1\", \"hypothesis\": \"Vanilla DreamerV3 on ManiSkill3 PickCube establishes a cross-environment baseline; if stable, subsequent CIVO trigger experiment (019b) can test whether CIVO generalizes beyond DMC Walker Walk.\", \"metrics\": {\"eval_return_final\": 69.43, \"eval_return_peak\": 69.7, \"eval_return_peak_step\": 162500, \"steps_completed\": 200248, \"value_mean_final\": 143.4, \"ve_ratio_final\": 2.07, \"ve_ratio_range\": \"1.05-3.56\"}, \"notes\": \"2026-05-16 22:54: Resubmitted with CVD fix (unset CUDA_VISIBLE_DEVICES inside bash -c). PID 629444. ManiSkill3/SAPIEN requires physical device access — CVD breaks resolve_physical_device(). Using MUJOCO_EGL_DEVICE_ID=1 + --device cuda:1 directly.\", \"parent\": \"exp_001_baseline\", \"retry_count\": 1, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_019a_v2_pickcube_baseline/checkpoint.ckpt\", \"checkpoint_source\": \"auto-resume from logdir\", \"command\": \"bash -c \\\"unset CUDA_VISIBLE_DEVICES && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults maniskill --task maniskill_PickCube-v1 --gate_enabled False --seed 1 --steps 200000 --compile False --device cuda:1 --logdir ./logdir/exp_019a_v2_pickcube_baseline\\\"\", \"data_count\": 200000, \"data_path\": \"ManiSkill3 PickCube-v1 (online RL)\", \"eval_data\": \"N/A - training experiment\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_019a_v2_pickcube_baseline\", \"model_name\": \"DreamerV3-S\", \"seed\": 1, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T07:44:41.396Z\"}, \"exp_007_fixed_dt4\": {\"account\": \"root\", \"checkpoint_path\": \"N/A - killed, dt=4 confirmed too coarse for locomotion (D013)\", \"completed_at\": \"2026-05-13T22:32:00.591Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-13T22:15:44.218Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-13T22:32:01.413690+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"失败原因诊断中 | tmux 日志仅有初始化 warnings，无 Traceback | metrics.jsonl 仅到 step 5000（eval_return=31, model_grad_norm=206.46）| 进程运行 ~12.5 min 后异常退出 | 诊断 Worker: worker_diagnose_exp_007_fixed_dt4_20260513T223405\"}}, \"failure_reason\": \"dt=4 confirmed too coarse for locomotion: eval_return 127@35K vs baseline 389 (-67.4%). model_loss comparable to baseline — RSSM can learn 4-step dynamics, but action temporal resolution too coarse for Walker Walk. Confirms dt sweet spot ∈ {1,2}. See D013.\", \"gpu\": \"cuda:1\", \"hypothesis\": \"诊断实验：fixed dt=4 vs dt=2 vs learned gate。硬编码 dt=4，其余超参与 exp_006 完全一致。与 exp_006(dt=2) 对照：如果 dt=4 也不掉 return，说明跳步本身无害，问题在 learned gate 机制；如果 dt=4 掉但 dt=2 不掉，说明存在跳步边界。\", \"metrics\": {\"baseline_45K\": 443, \"eval_return_15K\": 129.6, \"eval_return_25K\": 176.9, \"eval_return_35K\": 126.7, \"eval_return_45K\": 144.41, \"eval_return_55K\": 152.49, \"eval_return_5K\": 31, \"model_loss_15K\": 6.337, \"model_loss_25K\": 5.089, \"model_loss_35K\": 4.755, \"model_loss_5K\": 17.927, \"peak_return\": 176.9, \"peak_step\": \"25K\", \"step\": 48000, \"trend\": \"peak 176.9@25K, low plateau ~127-152; value extremely suppressed (v/e 6-13%), NOT delusional critic but severe learning failure\", \"value_eval_ratio_45K\": 0.126, \"value_eval_ratio_55K\": 0.061, \"value_mean_45K\": 18.26, \"value_mean_55K\": 9.28, \"vs_baseline_45K\": \"-67.4%\"}, \"notes\": \"失败原因诊断中 | tmux 日志仅有初始化 warnings，无 Traceback | metrics.jsonl 仅到 step 5000（eval_return=31, model_grad_norm=206.46）| 进程运行 ~12.5 min 后异常退出 | 诊断 Worker: worker_diagnose_exp_007_fixed_dt4_20260513T223405\", \"parent\": \"exp_006_fixed_dt2\", \"reproduce\": {\"code_commit\": \"6ef8646d807cd10ce0c88e10a7e943211e7fc44c\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/fixed_dt4_v1_s1 --steps 150000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 4\\\"\", \"finished_at\": \"2026-05-13T22:32:00.443Z\"}, \"retry_count\": 2, \"server\": \"bjb1-45299\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/fixed_dt4_v2_s1 --steps 150000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 4\\\"\", \"data_count\": 150000, \"data_path\": \"dmc_walker_walk\", \"gpu\": [\"cuda:1\"], \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/fixed_dt4_v2_s1\", \"model_name\": \"DreamerV3+FixedDt4 (gate_fixed_dt=4, no learned gate, init_dt fix applied)\", \"pid\": \"90354\", \"seed\": 1, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T04:06:36.869Z\"}, \"exp_008c_no_subsample_dt2_h8\": {\"completed_at\": \"2026-05-14T04:09:46.829Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-14T01:33:31.413Z\", \"hypothesis\": \"隔离 compounding error 效应：subsample OFF + imagination dt=2 + H=8（物理覆盖 16 步 ≈ baseline H=15）。与 008a(H=15) 对照：008a 崩但 008c 不崩 → compounding error 是根因，H 需与 dt 反比补偿；两个都崩 → dt=2 RSSM 预测质量本身不足。\", \"metrics\": {\"actor_loss_55K\": -0.082, \"actor_loss_65K\": -0.053, \"baseline_65K\": 616, \"data_source_35K\": \"from training logs metrics.jsonl\", \"eval_return_35K\": 185.1, \"eval_return_45K\": 226.55, \"eval_return_55K\": 241.87, \"eval_return_65K\": 240.86, \"step\": 68000, \"trend\": \"flat plateau @55K-65K (~241), very slow learner with h8, value/eval=32.8% (no collapse)\", \"value_eval_ratio_35K\": 0.218, \"value_eval_ratio_55K\": 0.291, \"value_eval_ratio_65K\": 0.328, \"value_mean_35K\": 40.43, \"value_mean_55K\": 70.32, \"value_mean_65K\": 78.96, \"verdict_65K\": \"PLATEAU\", \"vs_baseline_65K\": \"-60.9%\"}, \"parent\": \"exp_006_fixed_dt2\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008c_fixed_dt2_no_subsample_h8/checkpoint.ckpt\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008c_fixed_dt2_no_subsample_h8 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 1 --imag_horizon 8\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 2.53, \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008c_fixed_dt2_no_subsample_h8\", \"model_name\": \"DreamerV3+FixedDt2_NoSubsample_H8 (gate_fixed_dt=2, gate_subsample_max_dt=1, imag_horizon=8)\", \"pid\": \"107021\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-14T01:37:47.540Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 9119.3}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T04:06:36.359Z\"}, \"exp_003_event_gated_v2\": {\"completed_at\": \"2026-05-13T09:58:31.673Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-13T04:52:22.660Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-13T09:58:32.493437+00:00\"}]}, \"failure_reason\": \"Return 崩塌至 baseline 13%。根因：_imagine 中 gate dt 无约束（输出 dt∈{1,...,8}），而 subsample curriculum 限制训练数据 dt≤effective_max_dt。RSSM 对未训练的大 dt 预测为噪声，progressive poisoning 导致 actor/critic 不可恢复。需修复 dt clipping + logits masking 后从头训练。\", \"metrics\": {\"eval_return_105K\": 92.3, \"eval_return_115K\": 118.7, \"fps\": 6.52, \"gate_dt_1_frac_116K\": 0.218, \"gate_dt_mean_116K\": 2.67, \"gate_dt_std_116K\": 1.46, \"gate_empirical_entropy_116K\": 1.655, \"gate_entropy_ratio_116K\": 0.796, \"gate_scale_116K\": 0.61, \"mvp_C1_return\": \"FAIL (0.13)\", \"mvp_C2_entropy\": \"PASS (1.655)\", \"mvp_C3_heff\": \"PASS (2.667x)\", \"mvp_C4_structure\": \"PASS (autocorr=0.652)\", \"return_ratio_105K\": 0.1, \"return_ratio_115K\": 0.13, \"step\": 120000}, \"parent\": \"exp_001_baseline\", \"reproduce\": {\"finished_at\": \"2026-05-13T09:58:31.205Z\"}, \"retry_count\": 0, \"spec\": {\"checkpoint_source\": \"logdir/event_gated_s1_v2/latest.pt\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/event_gated_s1_v2 --steps 500000 --seed 1 --compile False --device cuda:0 --gate_enabled True\", \"data_count\": 500000, \"data_path\": \"DMC Walker Walk (dm_control built-in)\", \"gpu_id\": 1, \"hypothesis\": \"Subsample curriculum prevents early destabilization while event gate learns meaningful variable-rate stepping\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/event_gated_s1_v2\", \"model_name\": \"DreamerV3 + Event-Gated Variable-Rate RSSM v2 (final fix: env step sync + threshold 25K/75K)\", \"pid\": 27009, \"seed\": 1, \"server\": \"autodl-rtx6000\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T04:06:35.459Z\"}, \"exp_004_event_gated_v3\": {\"completed_at\": \"2026-05-13T15:23:26.384Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-13T10:05:16.227Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-13T15:23:27.393422+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"metrics\": {\"eval_return_15K\": 153.86, \"fps\": 8.1, \"gate_dt_mean_15K\": 1, \"gate_scale_15K\": 0, \"step\": 20000}}}, \"failure_reason\": \"gate_loss 爆炸 bug：compute_gate_targets 使用 gate_max_dt=8 生成 target 分布但 logits masking 使用 effective_max_dt，cross-entropy loss ≈ 3e8。eval_return@125K=352 vs baseline@335K=942，ratio=0.37。第三次 train/imagine distribution mismatch。\", \"hypothesis\": \"修复 imagination dt 约束后（logits masking + clamp safety net），event gate 在 train/imagine 分布同步条件下能产生有意义的 variable-rate stepping 且 return ≥ 80% baseline\", \"parent\": \"exp_003_event_gated_v2\", \"retry_count\": 1, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"N/A - killed due to gate_loss explosion bug\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/event_gated_v4_s1 --steps 500000 --seed 1 --compile False --device cuda:0 --gate_enabled True\", \"data_count\": 500000, \"data_path\": \"DMC Walker Walk (dm_control built-in)\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 5.19, \"gpu_id\": 1, \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/event_gated_v4_s1\", \"model_name\": \"DreamerV3 + Event-Gated Variable-Rate RSSM v3 (dt clipping + logits masking + dt alignment fix)\", \"pid\": 36645, \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-13T10:12:04.157Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 18682.2}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T04:06:34.482Z\"}, \"exp_005_event_gated_v4\": {\"checkpoint_path\": \"N/A - killed due to structural failure of hard Gumbel gate\", \"completed_at\": \"2026-05-13T22:15:21.359Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-13T16:08:06.061Z\", \"failure_reason\": \"Hard Gumbel gate 结构性失败。3轮 bug 修复后仍崩塌：eval_return 峰值 541.18@55K → 持续下降 → 98.84@145K（baseline 同期 950.9）。Gate 机制有效（entropy/H_eff/structure 全 PASS），但 hard categorical gate + variable-rate imagination 与 actor-critic 优化存在结构性冲突。gate_scale>0.5 后 return 不可恢复。\", \"hypothesis\": \"Event-gated adaptive horizon (learned gate activation for dt selection) improves sample efficiency over fixed-horizon DreamerV3 by dynamically extending imagination when beneficial.\", \"latest_metrics\": {\"alert\": \"return_declining_at_phase2_onset\", \"baseline_at_65K\": 615.9, \"checked_at\": \"2026-05-13\", \"eval_return\": 465.67, \"eval_return_trajectory\": {\"15K\": 153.9, \"25K\": 254.2, \"35K\": 290.8, \"45K\": 443, \"55K\": 541.2, \"5K\": 31, \"65K\": 465.7}, \"fps\": 6.69, \"gap_vs_baseline\": -150.2, \"gate_dt_1_frac\": 0.965, \"gate_dt_2_frac\": 0.035, \"gate_dt_mean\": 1.035, \"gate_dt_std\": 0.036, \"gate_empirical_entropy\": 0.0499, \"gate_entropy_bonus\": 0.0865, \"gate_entropy_ratio\": 0.072, \"gate_loss\": 0.00663, \"gate_scale\": 0.10004, \"phase2_status\": \"gate刚进入phase2 (gate_scale=0.1), dt=1占比96.5%, gate几乎未激活。eval_return在55K→65K出现14%下降(541→466), 与phase2启动时机吻合, 类似exp_003崩塌前兆。但baseline同期也有小幅回调(626→616, -1.6%), 且gate尚未真正激活, 需继续观察75K数据确认是正常波动还是collapse。\", \"pid\": 51721, \"prev_eval_return\": 541.18, \"process_status\": \"running\", \"step\": 65000, \"train_return_latest\": 569.8, \"train_return_range\": [535.4, 602.1], \"uptime\": \"2h31m\"}, \"metrics\": {\"baseline_at_145K\": \"~950\", \"eval_return_105K\": 276.08, \"eval_return_145K\": 98.84, \"eval_return_15K\": 153.9, \"eval_return_35K\": 290.8, \"eval_return_55K\": 541.18, \"eval_return_5K\": 31, \"eval_return_65K\": 465.67, \"eval_return_85K\": 212.34, \"final_return\": 98.84, \"fps\": 6.69, \"gate_dt_mean_105K\": 2.054, \"gate_dt_std_105K\": 0.907, \"gate_entropy_105K\": 1.255, \"gate_scale_105K\": 0.5, \"note\": \"85K/105K metrics corrected from 319.3/337.8 to 212.34/276.08\", \"peak_return\": 541.18, \"peak_step\": \"55K\", \"return_ratio_final\": 0.104, \"step\": 145000}, \"parent\": \"exp_004_event_gated_v3\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/event_gated_v5_s1 --steps 500000 --seed 1 --compile False --device cuda:0 --gate_enabled True\", \"data_count\": 500000, \"data_path\": \"dmc_walker_walk\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 6.12, \"hypothesis\": \"修复 gate_target/masking 维度不匹配 + effective_max_dt 单一来源架构 + 全量审计后，event gate return >= 80% baseline\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_005_event_gated_v4.log\", \"model_name\": \"DreamerV3+EventGate_v4\", \"pid\": \"51721\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-13T16:08:11.913Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 22029.4}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T04:06:33.514Z\"}, \"exp_008d_civo_trigger_s3\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008d_civo_trigger_s3/checkpoint.ckpt\", \"completed_at\": \"2026-05-17T03:24:26.004Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-17T00:25:47.784Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-17T03:18:40.430236+00:00\"}]}, \"hypothesis\": \"Trained dt-emb with subsample (gate_fixed_dt=2, gate_subsample_max_dt=2) induces CIVO (NVE≥1.5×) on seed=3, confirming CIVO onset is systematic across seeds regardless of replay sampling sequence (seed bug fix verification).\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_008d_civo_trigger_s3.log\", \"metrics\": {\"baseline_eval_105K\": 915.67, \"collapse_onset_step\": 95000, \"collapse_type\": \"late-onset\", \"eval_return_final\": 267.6, \"eval_return_final_step\": 105000, \"eval_return_peak\": 451.7, \"eval_return_peak_step\": 95000, \"nve_final\": 1.53, \"nve_onset_step\": 45000, \"nve_onset_value\": 1.5, \"nve_peak\": 1.53, \"nve_peak_step\": 105000, \"nve_sustained_45K_55K\": true, \"total_steps\": 112000, \"train_return_final_avg\": 138, \"train_return_final_range\": \"82-214\", \"value_mean_final\": 268.4, \"vs_baseline_105K\": \"-70.8%\"}, \"parent\": \"exp_008d_subsample_on_h8\", \"reproduce\": {\"finished_at\": \"2026-05-17T03:18:37.221Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"fresh_training (no checkpoint, new logdir)\", \"command\": \"bash -c \\\"unset CUDA_VISIBLE_DEVICES && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --gate_subsample_min_dt 1 --imag_horizon 8 --seed 3 --steps 105000 --checkpoint_every 25000 --compile False --device cuda:0 --logdir ./logdir/exp_008d_civo_trigger_s3\\\"\", \"data_count\": 105000, \"data_path\": \"DMC Walker Walk (online RL)\", \"eval_data\": \"N/A - training experiment\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 2.97, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_008d_civo_trigger_s3.log\", \"model_name\": \"DreamerV3-S\", \"pid\": \"635744\", \"seed\": 3, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-17T00:25:59.245Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 10706.8}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T03:24:26.004Z\"}, \"exp_018v2_full_sgs_walker_s1\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_018v2_full_sgs_walker_s1/latest.pt\", \"completed_at\": \"2026-05-16T17:24:44.481Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-16T13:42:15.786Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-16T17:17:46.576638+00:00\"}]}, \"hypothesis\": \"Full Selective Gradient Stopping (blocking obs+reward+cont decoder gradients to dt_emb) eliminates all gradient pathways creating dt-specific representations, thereby preventing CIVO onset and collapse.\", \"log_path\": \"/root/runs/event-gated-adaptive-horizon/exp_018v2_full_sgs_walker_s1.log\", \"metrics\": {\"civo_reduction_pct\": 79, \"eval_return_final\": 448.3, \"eval_return_final_step\": 105000, \"eval_return_peak\": 499.6, \"eval_return_peak_step\": 75000, \"gate_dt_2_frac\": 1, \"gate_dt_mean\": 2, \"late_collapse_detected\": true, \"late_collapse_step\": 112000, \"nve_final\": 1.34, \"nve_mean_45k_105k\": 1.23, \"nve_peak\": 1.66, \"nve_peak_step\": 95000, \"total_steps\": 112000, \"total_updates\": 25099, \"value_loss_final\": 0.6}, \"parent\": \"exp_008d_subsample_on_h8\", \"reproduce\": {\"finished_at\": \"2026-05-16T17:17:44.050Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"N/A (training from scratch, parent is predecessor not checkpoint source)\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --full_sgs True --seed 1 --steps 105000 --checkpoint_every 25000 --compile False --device cuda:0 --logdir ./logdir/exp_018v2_full_sgs_walker_s1\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk (online RL, no static dataset)\", \"eval_data\": \"dmc_walker_walk eval episodes (online)\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 3.49, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_018v2_full_sgs_walker_s1.log\", \"model_name\": \"DreamerV3\", \"pid\": \"589564\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-16T13:55:10.231Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 12574.2}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T02:57:18.423Z\"}, \"exp_018_full_sgs_s2\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_018_full_sgs_s2/checkpoint.pt\", \"completed_at\": \"2026-05-16T23:47:49.458Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-16T19:33:26.266Z\", \"gpu\": \"cuda:0\", \"hypothesis\": \"Full-SGS reliably prevents CIVO across seeds; if seed=2 also survives without collapse, SGS is a robust intervention mechanism for deployment.\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_018_full_sgs_s2.log\", \"notes\": \"CIVO collapse confirmed: eval 40.8@105K (from peak ~488@75K). NVE peaked 1.66× at 95K (35K+ window). Full-SGS did NOT prevent collapse in seed 2 — contradicts 018v2 (seed 1) which avoided collapse. This invalidates SGS_full as a reliable CIVO prevention method. Key difference from 018v2: 018_s2 collapsed while 018v2 sustained. n=2 for SGS_full now shows collapse_rate=0.5.\", \"parent\": \"exp_018v2_full_sgs_walker_s1\", \"pid\": \"612876\", \"reproduce\": {\"code_commit\": \"3328f53cb32cda27e85b099d560256aeb01db998\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --full_sgs True --seed 2 --steps 105000 --checkpoint_every 25000 --compile False --device cuda:0 --logdir ./logdir/exp_018_full_sgs_s2\\\"\"}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --full_sgs True --seed 2 --steps 105000 --checkpoint_every 25000 --compile False --device cuda:0 --logdir ./logdir/exp_018_full_sgs_s2\\\"\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 4.04, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_018_full_sgs_s2.log\", \"pid\": \"612876\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-16T19:45:40.838Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 14528.6}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T02:56:37.385Z\"}, \"exp_008f_no_dt_embed_subsample_on_h8\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008f_no_dt_embed_subsample_on_h8/latest.pt\", \"completed_at\": \"2026-05-14T09:32:53.461Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-14T04:51:27.592Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-14T09:30:42.170428+00:00\"}]}, \"hypothesis\": \"Without trained dt-embedding, subsample mechanism alone does not induce value overestimation, isolating dt-embedding as the necessary causal factor for CIVO.\", \"metrics\": {\"baseline_105K\": 915.67, \"causal_conclusion\": \"trained dt_embedding → value overestimation → actor exploitation → collapse. Without dt_embedding, value self-corrects.\", \"current_step\": 105000, \"eval_checkpoints\": {\"105K\": {\"eval_return\": 503, \"normalized_ve\": 0.3, \"value_mean\": 98.2}, \"15K\": {\"eval_return\": 182.03, \"value_mean\": 2.989, \"ve_ratio\": 0.01642}, \"25K\": {\"baseline_ve\": 0.087, \"eval_return\": 196.78, \"normalized_ve\": 1.02, \"value_mean\": 17.507, \"ve_ratio\": 0.089}, \"35K\": {\"baseline_ve\": 0.241, \"eval_return\": 206.67, \"normalized_ve\": 0.73, \"value_mean\": 36.279, \"ve_ratio\": 0.176}, \"45K\": {\"baseline_ve\": 0.331, \"eval_return\": 194.08, \"normalized_ve\": 0.83, \"value_mean\": 53.429, \"ve_ratio\": 0.275}, \"55K\": {\"baseline_ve\": 0.404, \"eval_return\": 173.45, \"normalized_ve\": 0.97, \"value_mean\": 67.899, \"ve_ratio\": 0.391}, \"5K\": {\"eval_return\": 30.49, \"value_mean\": 0.001, \"ve_ratio\": 4e-05}, \"65K\": {\"eval_return\": 375, \"normalized_ve\": 0.37}, \"75K\": {\"eval_return\": 324, \"normalized_ve\": 0.42}, \"85K\": {\"eval_return\": 246, \"normalized_ve\": 0.65, \"value_mean\": 111.8}, \"95K\": {\"eval_return\": 319, \"normalized_ve\": 0.54}}, \"last_updated\": \"2026-05-14T09:50:00\", \"target_steps\": 105000, \"trend\": \"Zigzag recovery with high variance: eval 207→194→173@55K→375→324→246→319→503@105K. NOT a clean V-shape — high inter-eval variance throughout. Value self-corrected: peaked 111.8@85K then declined to 98.2@105K. Normalized v/e: 0.97x@55K→0.37x@65K→0.65x@85K→0.30x@105K. Key contrast with 008d: value only accelerates (69.3%@45K) vs 008f value self-corrects.\", \"verdict\": \"SUCCESS - zigzag recovery to 503@105K, normalized v/e=0.30x, C2 confirmed\", \"vs_baseline_105K\": \"-45.1%\"}, \"parent\": \"exp_008d_subsample_on_h8\", \"reproduce\": {\"finished_at\": \"2026-05-14T09:30:41.254Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"N/A - training from scratch, parent is for genealogy only\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008f_no_dt_embed_subsample_on_h8 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"N/A - training experiment, not eval\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 4.68, \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008f_no_dt_embed_subsample_on_h8\", \"model_name\": \"DreamerV3+FixedDt2_NoDtEmbed_Subsample_H8 (gate_fixed_dt=2, gate_subsample_max_dt=2, imag_horizon=8, gate_dt_embed_dim=0)\", \"pid\": \"127761\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-14T04:51:55.020Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 16858.4}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T02:56:33.517Z\"}, \"exp_016d_sgs_walker_s1\": {\"completed_at\": \"2026-05-15T19:35:10.508Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-15T19:29:41.130Z\", \"failure_reason\": \"Same hang as 016c — SummaryWriter.flush() deadlock after add_video with moviepy 2.x. try/except insufficient because flush() blocks on incomplete async video encode. Fix: Logger.video() → no-op.\", \"hypothesis\": \"Selective Gradient Stopping (reward_dt_emb_detach) blocks reward-gradient pathway to dt_emb, preventing CIVO-inducing co-adaptation while preserving task performance.\", \"parent\": \"exp_008d_subsample_on_h8\", \"retry_count\": 0, \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_016d_sgs_walker_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --reward_dt_emb_detach True\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"model_name\": \"dreamerv3-sgs\", \"note\": \"第5次启动。两项修复生效：MUJOCO_EGL_DEVICE_ID=1 + logger.video注释。旧PID 526153已自行退出。\", \"pid\": 526939, \"seed\": 1, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T02:54:28.152Z\"}, \"exp_001_baseline\": {\"completed_at\": \"2026-05-13T15:23:24.593Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-13T02:09:53.875Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-13T15:23:25.663340+00:00\"}, {\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-13T21:47:19.804301+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"metrics\": {\"eval_return_205K\": 907.1, \"eval_return_215K\": 919.8, \"fps\": 8.3, \"step\": 245000, \"train_return_244K\": \"935-976\"}}}, \"failure_reason\": \"误报：cron 检测到进程退出但实际是正常完成（512K步）。已核实 checkpoint 229MB 有效。\", \"hypothesis\": \"Vanilla DreamerV3 on Walker Walk converges to stable high-return policy (>900) within 500K steps, establishing the performance ceiling for all gated variants.\", \"latest_metrics\": {\"checked_at\": \"2026-05-13\", \"eta_hours\": 1.8, \"eval_return\": 953.37, \"eval_step\": 445000, \"fps\": 7.29, \"pid\": 9409, \"prev_eval_return\": 964.96, \"process_status\": \"running\", \"step\": 452000, \"steps_remaining\": 48000, \"train_return_latest\": 958.07, \"train_return_range\": [917, 985.8], \"uptime\": \"16h35m\"}, \"metrics\": {\"data_source_ve\": \"from training logs metrics.jsonl\", \"eval_return_last10_mean\": 950.9, \"eval_return_peak\": 970.41, \"eval_return_peak_step\": 505000, \"eval_trajectory\": {\"105K\": 915.67, \"115K\": 919.81, \"125K\": 921.37, \"135K\": 900, \"145K\": 932.16, \"155K\": 933.34, \"15K\": 206.61, \"165K\": 907.98, \"175K\": 918.87, \"185K\": 954.69, \"195K\": 936.09, \"205K\": 949.24, \"215K\": 913.4, \"225K\": 962.44, \"235K\": 937.24, \"245K\": 934.42, \"255K\": 948.45, \"25K\": 395.27, \"265K\": 925.09, \"275K\": 931.51, \"285K\": 925.75, \"295K\": 936.3, \"305K\": 939.33, \"315K\": 948.42, \"325K\": 967.75, \"335K\": 942.41, \"345K\": 969.83, \"355K\": 941.11, \"35K\": 388.47, \"365K\": 935.76, \"375K\": 918.24, \"385K\": 937.98, \"395K\": 955.38, \"405K\": 937.83, \"415K\": 948.99, \"425K\": 954.64, \"435K\": 964.96, \"445K\": 953.37, \"455K\": 945.84, \"45K\": 513.77, \"465K\": 947.81, \"475K\": 947.66, \"485K\": 930.6, \"495K\": 944.73, \"505K\": 970.41, \"55K\": 625.73, \"5K\": 31.77, \"65K\": 615.86, \"75K\": 596.28, \"85K\": 713.93, \"95K\": 871.06}, \"final\": true, \"step\": 512000, \"value_eval_ratio_105K\": 0.656, \"value_eval_ratio_25K\": 0.087, \"value_eval_ratio_35K\": 0.241, \"value_eval_ratio_45K\": 0.331, \"value_eval_ratio_55K\": 0.404, \"value_eval_ratio_65K\": 0.563, \"value_eval_ratio_75K\": 0.719, \"value_eval_ratio_85K\": 0.701, \"value_eval_ratio_95K\": 0.632, \"value_eval_ratio_stable\": \"~69-72% from 135K+\"}, \"reproduce\": {\"finished_at\": \"2026-05-13T21:47:18.966Z\"}, \"retry_count\": 1, \"spec\": {\"command\": \"python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/baseline_s1 --steps 500000 --seed 1 --compile False --device cuda:0\", \"data_count\": 500000, \"data_path\": \"DMC Walker Walk (dm_control built-in)\", \"gpu\": [\"cuda:0\"], \"gpu_id\": 0, \"hypothesis\": \"DreamerV3 baseline on DMC Walker Walk for comparison with event-gated model\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/baseline_s1\", \"model_name\": \"DreamerV3 (original, gate_enabled=false)\", \"pid\": 9409, \"seed\": 1, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T02:54:24.099Z\"}, \"exp_008d_civo_trigger_s2\": {\"completed_at\": \"2026-05-17T00:24:10.180Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-16T19:32:16.790Z\", \"gpu\": \"cuda:0\", \"hypothesis\": \"Walker Walk trained dt_emb + subsample ON + dt=2 + H=8, seed 1 — CIVO trigger 第 3 个独立 seed (D1)。预期 NVE>1.5× 触发 CIVO。用于 bootstrap CI 闭合 trained_dt_emb condition (现有: seed 0 = 008d, seed 2 = 009b)。注意: 原名 s2 但实际需跑 seed=1 (避免与 009b seed=2 重复)。\", \"notes\": \"Killed by Director order: seed bug confirmed. --seed 1 was parsed incorrectly, producing bit-for-bit identical results to seed=0. PID 628482 killed. Will resubmit after seed bug fix with seed=3.\", \"parent\": \"exp_008d_subsample_on_h8\", \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"fresh_training (no checkpoint loaded)\", \"command\": \"source /root/miniconda3/bin/activate && cd /root/event-gated-adaptive-horizon && python train.py --configs dmc_vision --task dmc_walker_walk --logdir ./logdir/008d_civo_trigger_s2 --seed 1 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --gate_subsample_min_dt 1 --imag_horizon 8 --steps 120000\", \"data_count\": 120000, \"data_path\": \"DMC Walker Walk (online RL)\", \"eval_data\": \"N/A - training experiment, not eval\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 1.57, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_008d_civo_trigger_s2.log\", \"model_name\": \"DreamerV3-S\", \"pid\": \"628477\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-16T22:49:55.859Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 5654.3}, \"status\": \"DONE\", \"updated_at\": \"2026-05-17T00:24:10.180Z\"}, \"exp_008f_s3_no_dt_embed_walker\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008f_s3_no_dt_embed_walker/checkpoint.ckpt\", \"completed_at\": \"2026-05-16T20:09:51.135Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-16T16:04:28.878Z\", \"gpu\": \"cuda:1\", \"hypothesis\": \"Walker Walk dt_embed_dim=0 + subsample ON + H=8 seed 3 — 008f 系列第 3 个独立 seed，闭合 no_dt_emb condition 的 bootstrap CI（当前 n=2，需 ≥3）。预期 NVE<1.5×，无 CIVO。\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_008f_s3_no_dt_embed_walker.log\", \"metrics\": {\"collapse\": false, \"eval_return_final\": 363.8, \"nve_peak\": \"< 1.5x\"}, \"parent\": \"exp_008f_no_dt_embed_subsample_on_h8\", \"pid\": \"601233\", \"reproduce\": {\"code_commit\": \"3328f53cb32cda27e85b099d560256aeb01db998\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008f_s3_no_dt_embed_walker --steps 105000 --seed 3 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0 --checkpoint_every 25000\\\"\"}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008f_s3_no_dt_embed_walker --steps 105000 --seed 3 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0 --checkpoint_every 25000\\\"\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 2.81, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_008f_s3_no_dt_embed_walker.log\", \"pid\": \"601233\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-16T17:21:24.538Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 10106.6}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T20:09:51.135Z\"}, \"exp_020_vanilla_dreamerv3_s2\": {\"completed_at\": \"2026-05-16T19:43:57.604Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-16T13:23:55.837Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-16T19:40:49.938571+00:00\"}]}, \"gpu\": \"cuda:0\", \"hypothesis\": \"Vanilla DreamerV3 (no dt_emb, no subsample, no gate) seed 2 — Pathway B 控制实验：验证 008e_v3_s2 的 eval-driven collapse 是否需要 trained dt_emb 作为必要条件。如果 vanilla s2 稳定 → C6 成立 (trained dt_emb 是 Pathway B 必要条件)。如果也崩溃 → Pathway B 是 DreamerV3 inherent fragility。\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_020_vanilla_dreamerv3_s2.log\", \"metrics\": {\"collapse\": false, \"comparison_with_parent\": {\"c6_confirmed\": true, \"delta\": \"vanilla stable (836.5) vs trained dt_emb collapsed (136.96)\", \"parent_collapsed\": true, \"parent_eval_105K\": 136.96, \"parent_id\": \"exp_008e_v3_walker_s2\", \"parent_nve_105K\": 3.78}, \"eval_trajectory\": [{\"eval_return\": 41.2, \"step\": 5000}, {\"eval_return\": 534.1, \"step\": 55000}, {\"eval_return\": 688.9, \"step\": 65000}, {\"eval_return\": 596.2, \"step\": 95000}, {\"eval_return\": 836.5, \"step\": 105000}], \"final_eval_return\": 836.5, \"final_value_mean\": 539.3, \"peak_eval_return\": 836.5, \"peak_eval_step\": 105000, \"train_return_range_108K\": \"511-808\", \"ve_ratio_105K\": 0.645}, \"notes\": \"Pathway B 控制实验 (D6)。vanilla config: dt_embed_dim=0, subsample OFF, H=15, seed=2, 105K steps, Walker Walk。排队等 010b 完成后在 cuda:0 提交。命令: dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --steps 105000 --seed 2 --compile True --device cuda:0 --imag_horizon 15\", \"parent\": \"exp_008e_v3_walker_s2\", \"pid\": \"596344\", \"reproduce\": {\"code_commit\": \"3328f53cb32cda27e85b099d560256aeb01db998\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_020_vanilla_dreamerv3_s2 --steps 105000 --seed 2 --compile False --device cuda:0 --imag_horizon 15\\\"\", \"finished_at\": \"2026-05-16T19:40:47.795Z\"}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"logdir/exp_020_vanilla_dreamerv3_s2/checkpoint.pt\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_020_vanilla_dreamerv3_s2 --steps 105000 --seed 2 --compile False --device cuda:0 --imag_horizon 15\\\"\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 2.97, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_020_vanilla_dreamerv3_s2.log\", \"pid\": \"596344\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-16T16:45:55.371Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 10682.2}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T19:43:57.604Z\"}, \"exp_019a_pickcube_baseline\": {\"account\": \"root\", \"completed_at\": \"2026-05-16T13:43:00.745Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-16T03:23:50.639Z\", \"gpu\": \"cuda:1\", \"hypothesis\": \"PickCube-v1 baseline — dt=1, no dt_emb (dim=0), subsample OFF. ManiSkill3 manipulation 环境稳定基线，验证 CIVO 诊断在 manipulation 中的适用性\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_019a_pickcube_baseline.log\", \"notes\": \"ManiSkill3 Phase 1. 排队等 cuda:1 (010a 完成后). --compile False --device cuda:1. maniskill_state config.\", \"pid\": \"586751\", \"reproduce\": {\"code_commit\": \"3328f53cb32cda27e85b099d560256aeb01db998\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 python -u dreamer.py --configs defaults maniskill_state --task maniskill_PickCube-v1 --steps 200000 --seed 1 --device cuda:0 --compile False --logdir /root/runs/event-gated-adaptive-horizon/logdir/exp_019a_pickcube_baseline\\\"\", \"gpu\": \"cuda:1\", \"server\": \"bjb1-45299\", \"started_at\": \"2026-05-16T12:00:04.473Z\"}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"N/A (killed before completion)\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 python -u dreamer.py --configs defaults maniskill_state --task maniskill_PickCube-v1 --steps 200000 --seed 1 --device cuda:0 --compile False --logdir /root/runs/event-gated-adaptive-horizon/logdir/exp_019a_pickcube_baseline\\\"\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 0.37, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_019a_pickcube_baseline.log\", \"pid\": \"586751\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-16T13:20:56.230Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 1324.5}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T13:43:00.745Z\"}, \"exp_018_full_sgs_walker_s1\": {\"account\": \"root\", \"completed_at\": \"2026-05-16T12:43:09.226Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-15T23:30:39.991Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-16T12:40:17.132664+00:00\"}]}, \"gpu\": \"cuda:0\", \"hypothesis\": \"Full-SGS: detach all non-KL gradients from dt_emb (removes 93% obs decoder contribution). If CIVO persists → vulnerability is representation-level; if eliminated → obs decoder gradient is root cause.\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_018_full_sgs_walker_s1.log\", \"metrics\": {\"eval_return_final\": 915.7, \"eval_return_final_step\": 105000, \"eval_return_peak\": 915.7, \"eval_return_peak_step\": 105000, \"nve_peak\": 0.72, \"nve_peak_step\": 75000, \"nve_sustained_avg\": 0.55, \"nve_sustained_max\": 0.72, \"total_steps\": 112000, \"train_return_final_avg\": 899.4, \"value_mean_final\": 601.1}, \"notes\": \"⚠️ INVALID: 训练命令缺失 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8。gate_enabled=false → dt_embedding 未创建 → full_sgs 是空操作 → 实际等同 vanilla baseline。所有基于此实验的 claim (CIVO elimination, gradient-level vulnerability) 需要 018v2 重新验证。\", \"parent\": \"exp_016e_sgs_walker_s1\", \"pid\": \"577467\", \"reproduce\": {\"code_commit\": \"3328f53cb32cda27e85b099d560256aeb01db998\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_018_full_sgs_walker_s1 --steps 105000 --full_sgs True --seed 1 --compile False --device cuda:0\\\"\", \"finished_at\": \"2026-05-16T12:40:14.687Z\", \"gpu\": \"cuda:0\", \"server\": \"bjb1-45299\", \"started_at\": \"2026-05-16T09:50:18.238Z\", \"training_hours\": 2.83}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_018_full_sgs_walker_s1/checkpoint.pt\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_018_full_sgs_walker_s1\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T13:42:11.339Z\"}, \"exp_010a_cheetah_baseline_s1\": {\"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_010a_cheetah_baseline_s1/latest.pt\", \"completed_at\": \"2026-05-16T12:01:01.080Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-14T07:17:27.101Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-16T11:59:12.312213+00:00\"}]}, \"gpu\": \"cuda:1\", \"hypothesis\": \"Cheetah Run baseline seed 1 — 建立第二环境 dt=1 参考基线，为跨环境验证 C1/C2 做准备（plan_020）\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_010a_cheetah_baseline_s1.log\", \"metrics\": {\"eval_return_final\": 849.8, \"eval_return_final_step\": 515000, \"eval_return_peak\": 849.8, \"eval_return_peak_step\": 515000, \"final_step\": 524000, \"total_eval_episodes\": 52, \"train_return_last\": 716}, \"notes\": \"Director 排期: cuda:0 上排在 009d 之后。\", \"pid\": \"536890\", \"reproduce\": {\"code_commit\": \"dccb867841046bf6dc7dcc654ea71f99e1181828\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_010a_cheetah_baseline_s1 --steps 512000 --seed 1 --compile False --device cuda:0\\\"\", \"finished_at\": \"2026-05-16T11:59:09.914Z\", \"gpu\": \"cuda:1\", \"server\": \"bjb1-45299\", \"started_at\": \"2026-05-15T22:48:05.456Z\", \"training_hours\": 13.18}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_010a_cheetah_baseline_s1/checkpoint.pt\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_010a_cheetah_baseline_s1\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T12:01:11.169Z\"}, \"exp_009d_baseline_walker_s0\": {\"account\": \"root\", \"completed_at\": \"2026-05-15T12:10:01.788Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-15T11:55:00.039Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-15T12:10:04.203907+00:00\"}, {\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-15T12:24:17.652463+00:00\"}, {\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-16T09:48:44.475703+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"已清理重复进程并干净重启。修复: LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 + MUJOCO_GL=egl + CUDA_VISIBLE_DEVICES 隔离。cuda:0, seed=0, 500K steps ~19h。logdir: /root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009d_baseline_walker_s0\"}}, \"failure_reason\": \"EXIT_CODE=129 (non-zero)\", \"gpu\": \"cuda:0\", \"hypothesis\": \"Walker Walk baseline seed 0 — 第三独立 baseline seed，建立 v/e 校准参考（plan_010）\", \"metrics\": {\"eval_return\": 927.6, \"eval_return_at_508K\": 927.6, \"eval_return_peak\": 950.96, \"eval_return_peak_step\": 398000, \"note\": \"COMPLETED 508K/500K, final eval 927.6, peak 950.96@398K\", \"step\": 508000}, \"notes\": \"已清理重复进程并干净重启。修复: LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 + MUJOCO_GL=egl + CUDA_VISIBLE_DEVICES 隔离。cuda:0, seed=0, 500K steps ~19h。logdir: /root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009d_baseline_walker_s0\", \"parent\": \"exp_001_baseline\", \"reproduce\": {\"code_commit\": \"dccb867841046bf6dc7dcc654ea71f99e1181828\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009d_baseline_walker_s0 --steps 500000 --seed 0 --compile False --device cuda:0\\\"\", \"finished_at\": \"2026-05-16T09:48:42.388Z\", \"gpu\": \"cuda:0\", \"server\": \"bjb1-45299\", \"started_at\": \"2026-05-15T12:06:19.592Z\", \"training_hours\": 21.71}, \"retry_count\": 2, \"server\": \"bjb1-45299\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009d_baseline_walker_s0/checkpoint.ckpt\", \"checkpoint_source\": \"N/A - training from scratch\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009d_baseline_walker_s0 --steps 500000 --seed 0 --compile False --device cuda:0\\\"\", \"data_count\": 500000, \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"N/A - training experiment\", \"gpu\": [\"cuda:0\"], \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009d_baseline_walker_s0/metrics.jsonl\", \"model_name\": \"DreamerV3_baseline\", \"pid\": \"149703\", \"seed\": 0, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T09:50:34.506Z\"}, \"exp_017_subsample_off_trained_dt_emb\": {\"completed_at\": \"2026-05-16T04:46:30.361Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-15T10:44:24.756Z\", \"hypothesis\": \"Walker Walk trained dt_emb + subsample OFF + dt=2 imagination + H=15 seed 1 — 2×2 消融矩阵: 隔离 subsample 训练数据的因果效应。与 008a (untrained dt_emb, subsample OFF) 唯一差异是 dt_emb trained vs untrained。如果 017 崩而 008a 不崩 → 确认 trained dt_emb 是 CIVO 根因，即使训练数据全为 dt=1（plan_017, C2）\", \"notes\": \"D044: 取消。008a 配置验证确认 017 与 008a 完全重复（trained dt_emb + subsample OFF + H=15 + seed 1）。008a 的\\\"untrained\\\"含义是\\\"dt_emb 存在但未接触 dt>1 数据\\\"，不是 frozen/absent。2×2 矩阵已由 008a/008d/008f/015b 闭合。\", \"parent\": \"exp_008a_no_subsample_dt2\", \"retry_count\": 0, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T04:46:30.361Z\"}, \"016e\": {\"completed_at\": \"2026-05-16T01:39:17.916Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-15T22:21:09.251Z\", \"notes\": \"重复条目，权威数据在 exp_016e_sgs_walker_s1 (DONE/negative)。此条目为 NVE 诊断过程中误创建的冗余记录。\", \"retry_count\": 0, \"status\": \"DONE\", \"updated_at\": \"2026-05-16T01:39:17.916Z\"}, \"exp_016e_sgs_walker_s1\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_016e_sgs_walker_s1/latest.pt\", \"completed_at\": \"2026-05-15T22:31:16.457Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-15T19:35:20.242Z\", \"gpu\": \"cuda:1\", \"hypothesis\": \"Walker Walk SGS (Stop-Gradient on dt_emb in reward head) + subsample ON + H=8 seed 1 — 核心方法实验：reward_dt_emb_detach 阻断 CIVO reward→dt_emb 梯度通路（plan_016）。第五次重试，修复 Logger.video() → no-op 彻底消除 SummaryWriter.add_video/flush 死锁\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_016e_sgs_walker_s1/\", \"metrics\": {\"actor_loss_sign_flip_step\": 95000, \"civo_catastrophic_step\": 95000, \"civo_detected\": true, \"civo_nve_peak\": 10.42, \"civo_nve_peak_step\": 95000, \"civo_onset_step\": 85000, \"civo_severity\": \"catastrophic\", \"current_step\": 100000, \"data_source\": \"metrics.jsonl from logdir/exp_016e_sgs_walker_s1/, completed 100K steps, SSH 2026-05-16T06:25\", \"deep_analysis\": {\"016e_vs_008d_entropy_comparison\": {\"15K\": {\"008d\": 0.481, \"016e\": 1.049, \"delta\": 0.568}, \"25K\": {\"008d\": -1.862, \"016e\": -1.554, \"delta\": 0.308}, \"35K\": {\"008d\": -3.465, \"016e\": -2.118, \"delta\": 1.347}, \"45K\": {\"008d\": -4.575, \"016e\": -3.455, \"delta\": 1.12}, \"55K\": {\"008d\": -4.879, \"016e\": -3.617, \"delta\": 1.262}, \"interpretation\": \"SGS preserves ~1.0-1.3 nats higher entropy through 35-55K, enabling better exploration\"}, \"016e_vs_008d_value_at_crash\": {\"008d\": {\"disconnect_ratio\": 1.67, \"eval_return\": 82.75, \"value_mean\": 137.88}, \"016e\": {\"disconnect_ratio\": 6.58, \"eval_return\": 31.73, \"value_mean\": 208.88}, \"interpretation\": \"016e value completely decoupled from reality; 008d still weakly correlated\"}, \"actor_loss_sign_flip\": {\"008d_min_actor_loss\": -0.073, \"008d_never_flipped\": true, \"016e_flip_step\": 95000, \"016e_flip_value\": 0.014, \"interpretation\": \"sign flip = value critic drives actor toward worse actions, triggering catastrophic collapse\"}, \"train_return_collapse_timeline\": {\"100K\": [109, 111, 102, 108], \"88K\": [140, 145, 116, 116], \"92K\": [50, 29, 34, 75], \"96K\": [86, 41, 50, 101], \"interpretation\": \"collapse visible in train_return by 92K; partial recovery by 100K but far below peak\"}}, \"eval_checkpoints\": [{\"eval_return\": 31, \"step\": 5000, \"value_mean\": 0.001, \"ve_ratio\": 4e-05}, {\"eval_return\": 140.3, \"step\": 15000, \"value_mean\": 3.1, \"ve_ratio\": 0.022}, {\"baseline_ve\": 0.087, \"eval_return\": 141.75, \"nve\": 1.86, \"step\": 25000, \"value_mean\": 22.97, \"ve_ratio\": 0.162}, {\"baseline_ve\": 0.241, \"eval_return\": 173.01, \"nve\": 1.28, \"step\": 35000, \"value_mean\": 53.55, \"ve_ratio\": 0.309}, {\"baseline_ve\": 0.331, \"eval_return\": 184.03, \"nve\": 1.4, \"step\": 45000, \"value_mean\": 85.32, \"ve_ratio\": 0.464}, {\"baseline_ve\": 0.404, \"eval_return\": 153.79, \"nve\": 1.86, \"step\": 55000, \"value_mean\": 115.63, \"ve_ratio\": 0.752}, {\"baseline_ve\": 0.563, \"eval_return\": 324.3, \"nve\": 0.83, \"step\": 65000, \"value_mean\": 152.3, \"ve_ratio\": 0.469}, {\"baseline_ve\": 0.719, \"eval_return\": 326.67, \"nve\": 0.81, \"step\": 75000, \"value_mean\": 190.04, \"ve_ratio\": 0.582}, {\"baseline_ve\": 0.701, \"eval_return\": 256.21, \"nve\": 1.2, \"step\": 85000, \"value_mean\": 215.39, \"ve_ratio\": 0.841}, {\"baseline_ve\": 0.632, \"eval_return\": 31.73, \"nve\": 10.42, \"step\": 95000, \"value_mean\": 208.88, \"ve_ratio\": 6.583}], \"final_eval_return\": 31.73, \"final_eval_step\": 95000, \"gate_dt_2_frac\": 1, \"gate_dt_mean\": 2, \"peak_eval_return\": 326.67, \"peak_eval_step\": 75000, \"reward_dt_emb_detach\": true, \"sgs_verdict\": \"SGS delays CIVO onset ~50K steps by preserving entropy, yields 2x higher peak (327 vs 167), but does NOT prevent collapse. Collapse is more severe (NVE 10.42x vs 4.12x) due to accumulated value overestimation. Root cause is value dynamics, not reward-head gradient contamination.\", \"target_steps\": 105000}, \"notes\": \"logdir 路径修正：实际数据在 logdir/exp_016e_sgs_walker_s1（非 spec 中的 exp_016d）。SGS 崩溃确认@95K: eval 31.7, ve_ratio=6.59x, NVE=10.42x。\\n\\n**⚠️ 关键发现（Full-SGS 梯度验证）：reward loss 对 dt_emb.weight 的梯度贡献为 0。016e 的 reward_dt_emb_detach 实际上是 no-op——完全无效干预。** 真正的 dt_emb 梯度来源是 decoder heads（orientations=1.11, velocity=0.90, height=0.76, cont=0.27）。016e 与 008d 的差异（onset 延迟、更高峰值）应归因于随机变异或其他实验条件差异，不是 SGS 干预效果。\\n\\nFull-SGS（detach 所有 non-KL head 梯度）移除 93% dt_emb 梯度（1.624→0.119），是真正的测试。\", \"parent\": \"exp_008d_subsample_on_h8\", \"retry_count\": 0, \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_016e_sgs_walker_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --reward_dt_emb_detach True\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"logdir\": \"logdir/exp_016e_sgs_walker_s1\", \"model_name\": \"dreamerv3-sgs\", \"note\": \"logdir 修正: 实际数据在 exp_016e（非 016d）\", \"pid\": 527392, \"seed\": 1, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T23:30:11.433Z\"}, \"exp_016c_sgs_walker_s1\": {\"account\": \"root\", \"completed_at\": \"2026-05-15T19:26:05.863Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-15T19:12:09.799Z\", \"failure_reason\": \"EXIT_CODE=137 (SIGKILL — OOM killer). EGL fix confirmed working: eval at step 5000 completed successfully (eval_return=31.0). OOM occurred during training loop startup after eval. Likely system RAM OOM (replay buffer + model + eval concurrent memory peak).\", \"gpu\": \"cuda:1\", \"hypothesis\": \"Walker Walk SGS (reward_dt_emb_detach=True) + subsample ON + H=8 seed 1 — 论文 method section 核心。GPU 1 清理+验证通过后重启（plan_016）\", \"metrics\": {\"egl_fix_verified\": true, \"eval_return_5K\": 31, \"step\": 5000}, \"parent\": \"exp_008d_subsample_on_h8\", \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"checkpoint_source\": \"N/A - training from scratch, parent is for genealogy only\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_016b_sgs_walker_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --reward_dt_emb_detach True\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"N/A - training experiment, not eval\", \"gpu\": [\"cuda:1\"], \"model_name\": \"DreamerV3+FixedDt2_SGS_Subsample_H8 (reward_dt_emb_detach=True)\", \"note\": \"GPU 1 cleanup + CUDA/dm_control verification passed. logdir shared with 016b (fresh start).\", \"pid\": \"524244\", \"seed\": 1, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T19:27:24.104Z\"}, \"exp_009h_008f_walker_s0\": {\"account\": \"root\", \"completed_at\": \"2026-05-15T19:08:12.013Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-15T19:03:10.534Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-15T19:08:15.731787+00:00\"}]}, \"failure_reason\": \"误杀: Director 基于 Reviewer 错误诊断下令 kill（认为 zombie PID 522009 导致 eval deadlock），但日志证明 EGL fix (MUJOCO_EGL_DEVICE_ID=1) 已生效，eval 正常运行中 (iter=500, t=95.9s)。EGL fix 确认有效。\", \"gpu\": \"cuda:1\", \"hypothesis\": \"Walker Walk dt_embed_dim=0 + subsample ON + H=8 seed 0 — 多 seed 复现 008f 因果控制稳定性，巩固 C2 统计显著性（plan_012）。替代 009g（EGL device mismatch 修复：+MUJOCO_EGL_DEVICE_ID=1）\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_009h_008f_walker_s0.log\", \"notes\": \"日志显示进程正常完成 prefill → 到达 step 5000 → eval 正在运行（500 iter, 96s, 正常产出 debug 行）→ 被外部 SIGHUP (EXIT_CODE=129) 终止。非渲染死锁，非 OOM。诊断 Worker 排查外部终止原因中。009f/009g/009h 连续 3 次失败，分别因 seed 重复、EGL mismatch、外部 SIGHUP。\", \"parent\": \"exp_008f_no_dt_embed_subsample_on_h8\", \"pid\": \"522450\", \"reproduce\": {\"code_commit\": \"dccb867841046bf6dc7dcc654ea71f99e1181828\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009h_008f_walker_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"finished_at\": \"2026-05-15T19:08:09.836Z\"}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"checkpoint_source\": \"N/A - training from scratch\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009h_008f_walker_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"gpu\": [\"cuda:1\"], \"model_name\": \"DreamerV3+FixedDt2_NoDtEmbed_Subsample_H8\", \"note\": \"EGL fix: MUJOCO_EGL_DEVICE_ID=1 to match physical GPU 1. 008f series seeds: 1(008f), 2(009c), 0(009h)\", \"pid\": \"522450\", \"seed\": 0, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T19:18:24.685Z\"}, \"exp_016b_sgs_walker_s1\": {\"account\": \"root\", \"completed_at\": \"2026-05-15T19:10:52.235Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-15T19:08:00.667Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-15T19:10:53.928926+00:00\"}]}, \"failure_reason\": \"EXIT_CODE=137 (SIGKILL — OOM killer or manual kill)\", \"gpu\": \"cuda:1\", \"hypothesis\": \"Walker Walk SGS (Stop-Gradient on dt_emb in reward head) + subsample ON + trained dt_emb + H=8 seed 1 — 核心方法实验：reward_dt_emb_detach 阻断 CIVO reward→dt_emb 梯度通路（plan_016, 论文 method section 核心）。重跑 016_sgs，修复 EGL device mismatch（+MUJOCO_EGL_DEVICE_ID=1）\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_016b_sgs_walker_s1.log\", \"notes\": \"Restarted after GPU 1 cleanup. Old PID 523536 killed during GPU reset attempt. New PID 524244. GPU 1 diagnostics: no ECC/Xid errors, reset not supported (AutoDL container) but cleanup successful. CUDA + dm_control verification passed in 3s.\", \"parent\": \"exp_008d_subsample_on_h8\", \"pid\": 524244, \"reproduce\": {\"code_commit\": \"dccb867841046bf6dc7dcc654ea71f99e1181828\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_016b_sgs_walker_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --reward_dt_emb_detach True\\\"\", \"finished_at\": \"2026-05-15T19:10:51.013Z\"}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"checkpoint_source\": \"N/A - training from scratch\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_016b_sgs_walker_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --reward_dt_emb_detach True\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"gpu\": [\"cuda:1\"], \"model_name\": \"DreamerV3+FixedDt2_SGS_Subsample_H8 (reward_dt_emb_detach=True)\", \"note\": \"Rerun of 016_sgs with EGL fix (MUJOCO_EGL_DEVICE_ID=1). Original 016 failed due to EGL device mismatch, not SGS code issue.\", \"pid\": \"523536\", \"seed\": 1, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T19:11:46.897Z\"}, \"exp_009g_008f_walker_s0\": {\"account\": \"root\", \"completed_at\": \"2026-05-15T18:59:55.315Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-15T18:54:23.385Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-15T18:59:59.820061+00:00\"}]}, \"failure_reason\": \"EXIT_CODE=143 (SIGTERM). Root cause: MUJOCO_GL=egl defaults to EGL device 0 while CUDA_VISIBLE_DEVICES=1 binds CUDA to GPU 1, causing cross-GPU context conflict and eval deadlock at step 5000.\", \"gpu\": \"cuda:1\", \"hypothesis\": \"Walker Walk dt_embed_dim=0 + subsample ON + H=8 seed 0 — 多 seed 复现 008f 因果控制稳定性，巩固 C2 统计显著性（plan_012）。替代 009f（seed=1 与 parent 008f 重复）\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_009g_008f_walker_s0.log\", \"notes\": \"Hung at first eval (step 5000) due to osmesa rendering deadlock in dm_control render_executor thread. Same root cause as exp_016. Fixed by switching MUJOCO_GL to egl in dreamer.py.\", \"parent\": \"exp_008f_no_dt_embed_subsample_on_h8\", \"pid\": \"517413\", \"reproduce\": {\"code_commit\": \"dccb867841046bf6dc7dcc654ea71f99e1181828\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009g_008f_walker_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"finished_at\": \"2026-05-15T18:59:53.840Z\"}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"checkpoint_source\": \"N/A - training from scratch\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009g_008f_walker_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"gpu\": [\"cuda:1\"], \"model_name\": \"DreamerV3+FixedDt2_NoDtEmbed_Subsample_H8 (gate_fixed_dt=2, gate_subsample_max_dt=2, imag_horizon=8, gate_dt_embed_dim=0)\", \"note\": \"Replaces exp_009f which had seed=1 duplicating parent 008f. 008f series seeds: 1(008f), 2(009c), 0(009g)\", \"pid\": \"517413\", \"seed\": 0, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T19:03:53.591Z\"}, \"exp_009f_008f_walker_s1\": {\"account\": \"root\", \"completed_at\": \"2026-05-15T18:46:03.293Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-14T11:09:15.806Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-15T18:46:05.155411+00:00\"}, {\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-15T18:52:15.790170+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\"}}, \"failure_reason\": \"Seed duplication: 009f used seed=1 same as parent 008f, producing deterministic repeat (prefill returns identical). Killed by Director order.\", \"gpu\": \"cuda:1\", \"hypothesis\": \"Walker Walk dt_embed_dim=0 + subsample ON + H=8 seed 1 — 多 seed 复现 008f 因果控制稳定性，巩固 C2 统计显著性（plan_012）\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_009f_008f_walker_s1.log\", \"parent\": \"exp_008f_no_dt_embed_subsample_on_h8\", \"pid\": \"516110\", \"reproduce\": {\"code_commit\": \"dccb867841046bf6dc7dcc654ea71f99e1181828\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009f_008f_walker_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"finished_at\": \"2026-05-15T18:52:12.322Z\", \"gpu\": \"cuda:1\", \"server\": \"bjb1-45299\", \"started_at\": \"2026-05-15T18:44:58.143Z\", \"training_hours\": 0.12}, \"retry_count\": 1, \"server\": \"bjb1-45299\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009f_008f_walker_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 0.07, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_009f_008f_walker_s1.log\", \"pid\": \"516110\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-15T18:47:48.525Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 265.3}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T18:54:04.806Z\"}, \"exp_016_sgs_walker_s1\": {\"account\": \"root\", \"completed_at\": \"2026-05-15T18:43:52.455Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-15T14:30:32.999Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_failed\", \"ts\": \"2026-05-15T18:43:57.605618+00:00\"}]}, \"failure_reason\": \"EXIT_CODE=143 (SIGTERM — graceful kill)\", \"gpu\": \"cuda:1\", \"hypothesis\": \"Walker Walk SGS (Stop-Gradient on dt_emb in reward head) + subsample ON + trained dt_emb + H=8 seed 1 — 核心方法实验：reward_dt_emb_detach 阻断 CIVO reward→dt_emb 梯度通路。预期：不崩溃，nve < 1.5x baseline；imagination dt=2/dt=1 reward ratio 从 008d 的 2.90x 大幅下降（plan_016, 论文 method section 核心）\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_016_sgs_walker_s1.log\", \"notes\": \"Director 调整优先级：017 先于 016。cuda:1 释放后先跑 017，017 完成后再跑 016。SGS 诊断 bug 已修复（models.py L388-417 删除），dry-run 通过。[2026-05-15 18:43] PID 514422 hung: GPU 1 利用率 0%, 显存 794 MiB, metrics.jsonl 停 step=5000 持续 2.5h+。已 kill，Worker 诊断根因+修复+重启中。\", \"parent\": \"exp_008d_subsample_on_h8\", \"pid\": \"514417\", \"reproduce\": {\"code_commit\": \"dccb867841046bf6dc7dcc654ea71f99e1181828\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_016_sgs_walker_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --reward_dt_emb_detach True\\\"\", \"finished_at\": \"2026-05-15T18:43:51.025Z\"}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_016_sgs_walker_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --reward_dt_emb_detach True\\\"\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 0.13, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_016_sgs_walker_s1.log\", \"pid\": \"514417\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-15T18:36:15.693Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 456.8}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T18:43:52.455Z\"}, \"exp_015b_frozen_dt_emb\": {\"completed_at\": \"2026-05-15T12:12:25.846Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-15T10:21:05.572Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-15T18:27:09.189680+00:00\"}], \"previous_failure\": {\"conclusion\": \"failed\", \"notes\": \"第二次提交。首次失败原因: --device cuda:1 但 CUDA_VISIBLE_DEVICES=1 后进程内只有 cuda:0。已修正为 --device cuda:0。PID 144831, 从头开始 (step=0)。预计 ~5h 完成 105K steps。\"}}, \"hypothesis\": \"Walker Walk frozen dt_emb + subsample ON + dt=2 imagination + H=8 seed 1 — 2×2 消融矩阵: 隔离 dt_emb 训练 vs 存在的因果效应。如果 freeze 后不崩 → 确认 CIVO 根因是 dt_emb 训练而非结构存在（plan_015B, D041）\", \"metrics\": {\"actor_entropy_105K\": -4.855, \"actor_loss_105K\": 0.000179, \"collapse_mechanism\": \"gradient_starvation_from_frozen_dt_emb\", \"data_source\": \"worker SSH final analysis 2026-05-15T18:30\", \"eval_return_105K\": 204.2, \"eval_return_15K\": 167.9, \"eval_return_25K\": 171.8, \"eval_return_35K\": 201.6, \"eval_return_45K\": 122.3, \"eval_return_55K\": 105.8, \"eval_return_5K\": 31, \"eval_return_65K\": 160.3, \"eval_return_75K\": 80, \"eval_return_85K\": 183.5, \"eval_return_95K\": 238.4, \"final_eval\": 204.2, \"final_step\": 112000, \"gate_dt_1_frac\": 0, \"gate_dt_mean\": 2, \"nve_105K\": 0.42, \"nve_85K\": 0.467, \"nve_95K\": 0.394, \"summary\": \"NVE 0.39-0.47 (far below 1.0, critic under-estimates), actor_loss→0 (gradient starvation), gate locked dt=2 100%, eval volatile 80-238 no stable convergence\", \"value_mean_105K\": 56.212, \"value_std_105K\": 13.818}, \"notes\": \"已清理重复进程并干净重启。修复: LD_PRELOAD + MUJOCO_GL=egl + --device cuda:0 (CUDA_VISIBLE_DEVICES=1 隔离)。cuda:1, seed=1, 105K steps ~5h。logdir: /root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_015b_frozen_dt_emb\", \"parent\": \"exp_008d_subsample_on_h8\", \"reproduce\": {\"finished_at\": \"2026-05-15T18:27:07.138Z\"}, \"retry_count\": 1, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_015b_frozen_dt_emb\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=egl python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_015b_frozen_dt_emb --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --dt_emb_freeze True\\\"\", \"gpu\": [\"cuda:1\"], \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_015b_frozen_dt_emb.log\", \"pid\": \"149991\", \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T18:38:42.380Z\"}, \"exp_008a_no_subsample_dt2\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008a_fixed_dt2_no_subsample/latest.pt\", \"completed_at\": \"2026-05-14T06:16:58.196Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-14T01:33:27.311Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-14T06:15:01.796655+00:00\"}]}, \"hypothesis\": \"隔离 subsample 效应：trained dt_emb (unexposed to dt>1 data due to subsample OFF) + subsample OFF（纯 dt=1 训练）+ imagination dt=2 + H=15（物理覆盖 30 步）。如果不崩 → subsample 混合训练数据是崩塌根因；如果崩 → 问题在 dt=2 imagination 本身。\", \"metrics\": {\"baseline_105K\": 915.67, \"baseline_55K\": 625.7, \"baseline_65K\": 616, \"data_source\": \"from training logs metrics.jsonl\", \"eval_return_105K\": 777.66, \"eval_return_35K\": 500.84, \"eval_return_45K\": 563.41, \"eval_return_55K\": 487.92, \"eval_return_65K\": 608, \"eval_return_75K\": 469.93, \"eval_return_85K\": 583.73, \"eval_return_95K\": 572.24, \"nan_count\": 0, \"normalized_ve_105K\": 0.59, \"normalized_ve_55K\": 0.93, \"normalized_ve_65K\": 0.66, \"normalized_ve_75K\": 0.75, \"normalized_ve_85K\": 0.68, \"normalized_ve_95K\": 0.79, \"step\": 112000, \"trend\": \"Two V-shaped recoveries: 501→563→488→608→470→584→572→778; v/e suppressed 38-54% (normalized 0.59-0.79x baseline); no collapse at 105K\", \"value_eval_ratio_105K\": 0.386, \"value_eval_ratio_55K\": 0.376, \"value_eval_ratio_65K\": 0.372, \"value_eval_ratio_75K\": 0.536, \"value_eval_ratio_85K\": 0.475, \"value_eval_ratio_95K\": 0.497, \"value_mean_105K\": 300.27, \"value_mean_55K\": 183.5, \"value_mean_65K\": 226.1, \"value_mean_75K\": 251.78, \"value_mean_85K\": 277.36, \"value_mean_95K\": 284.28, \"verdict_105K\": \"NEW_PEAK_V_RECOVERY\", \"verdict_65K\": \"RECOVERED_NEW_HIGH\", \"vs_baseline_105K\": \"-15.1%\", \"vs_baseline_65K\": \"-1.3%\"}, \"reproduce\": {\"finished_at\": \"2026-05-14T06:15:00.119Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008a_fixed_dt2_no_subsample --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 1\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 4.65, \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008a_fixed_dt2_no_subsample\", \"model_name\": \"DreamerV3+FixedDt2_NoSubsample (gate_fixed_dt=2, gate_subsample_max_dt=1, H=15)\", \"pid\": \"106942\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-14T01:37:46.034Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 16752.2}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T14:50:59.046Z\"}, \"exp_009d_baseline_walker_s1\": {\"completed_at\": \"2026-05-15T11:54:55.153Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-14T11:09:14.363Z\", \"gpu\": \"cuda:0\", \"hypothesis\": \"Walker Walk baseline seed 1 — 多 seed 复现 exp_001 baseline，建立 v/e 校准参考（plan_010）\", \"notes\": \"⚠️ seed=1 与 exp_001_baseline 相同，eval 轨迹确定性复现。不构成独立 seed。如需第三 baseline seed 应 kill 并用 --seed 0 或 --seed 3 重跑。待 Director 决策。\", \"parent\": \"exp_001_baseline\", \"pid\": 122271, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"N/A - training from scratch\", \"command\": \"python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009d_baseline_walker_s1 --steps 500000 --seed 1 --compile False --device cuda:0\", \"data_count\": 500000, \"data_path\": \"dmc_walker_walk\", \"eval_data\": \"N/A - training experiment\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 5.33, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_009d_baseline_walker_s1.log\", \"model_name\": \"DreamerV3 (original, gate_enabled=false)\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-15T06:35:00Z\", \"wall_clock_seconds\": 19195.2}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T11:54:55.153Z\"}, \"exp_009a_baseline_walker_s2\": {\"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009a_baseline_walker_s2/latest.pt\", \"completed_at\": \"2026-05-15T06:33:12.892Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-14T07:17:24.247Z\", \"gpu\": \"cuda:0\", \"hypothesis\": \"Walker Walk baseline seed 2 — 多 seed 复现 exp_001 baseline，建立 v/e 校准参考（plan_010）\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009a_baseline_walker_s2/\", \"metrics\": {\"cross_seed_ve_stable\": \"seed 2 v/e = 0.69-0.72 matches seed 0/1 = 0.69-0.72\", \"eval_return_peak\": 966.94, \"eval_return_peak_step\": 395000, \"eval_trajectory\": [{\"eval_return\": 41.21, \"step\": 5000}, {\"eval_return\": 106.01, \"step\": 15000}, {\"eval_return\": 325.33, \"step\": 25000}, {\"eval_return\": 354.49, \"step\": 35000}, {\"eval_return\": 498.01, \"step\": 45000}, {\"eval_return\": 534.13, \"step\": 55000}, {\"eval_return\": 688.87, \"step\": 65000}, {\"eval_return\": 656.85, \"step\": 75000}, {\"eval_return\": 618.73, \"step\": 85000}, {\"eval_return\": 596.24, \"step\": 95000}, {\"eval_return\": 836.51, \"step\": 105000}, {\"eval_return\": 804.79, \"step\": 115000}, {\"eval_return\": 865.48, \"step\": 125000}, {\"eval_return\": 876.08, \"step\": 135000}, {\"eval_return\": 869.18, \"step\": 145000}, {\"eval_return\": 778.99, \"step\": 155000}, {\"eval_return\": 864.03, \"step\": 165000}, {\"eval_return\": 850.53, \"step\": 175000}, {\"eval_return\": 907.31, \"step\": 185000}, {\"eval_return\": 873.49, \"step\": 195000}, {\"eval_return\": 887.02, \"step\": 205000}, {\"eval_return\": 956.04, \"step\": 215000}, {\"eval_return\": 892.09, \"step\": 225000}, {\"eval_return\": 914.78, \"step\": 235000}, {\"eval_return\": 950.32, \"step\": 245000}, {\"eval_return\": 936.9, \"step\": 255000}, {\"eval_return\": 937.27, \"step\": 265000}, {\"eval_return\": 934.78, \"step\": 275000}, {\"eval_return\": 960.2, \"step\": 285000}, {\"eval_return\": 947.46, \"step\": 295000}, {\"eval_return\": 937.8, \"step\": 305000}, {\"eval_return\": 948.66, \"step\": 315000}, {\"eval_return\": 930.61, \"step\": 325000}, {\"eval_return\": 919.23, \"step\": 335000}, {\"eval_return\": 816.18, \"step\": 345000}, {\"eval_return\": 932.45, \"step\": 355000}, {\"eval_return\": 943.13, \"step\": 365000}, {\"eval_return\": 952.86, \"step\": 375000}, {\"eval_return\": 942.31, \"step\": 385000}, {\"eval_return\": 966.94, \"step\": 395000}, {\"eval_return\": 948.01, \"step\": 405000}, {\"eval_return\": 957.06, \"step\": 415000}, {\"eval_return\": 939.37, \"step\": 425000}, {\"eval_return\": 963.65, \"step\": 435000}, {\"eval_return\": 948.42, \"step\": 445000}, {\"eval_return\": 937.72, \"step\": 455000}, {\"eval_return\": 939.54, \"step\": 465000}, {\"eval_return\": 965.94, \"step\": 475000}, {\"eval_return\": 916.74, \"step\": 485000}, {\"eval_return\": 945.58, \"step\": 495000}, {\"eval_return\": 957.87, \"step\": 505000}], \"final_eval_return\": 957.87, \"final_eval_step\": 505000, \"final_value_mean\": 665.17, \"final_ve_ratio\": 0.694, \"last10_mean\": 947.19, \"n_evals\": 51, \"total_steps\": 505000, \"value_trajectory\": [{\"step\": 5000, \"value_mean\": 0}, {\"step\": 25000, \"value_mean\": 45.78}, {\"step\": 55000, \"value_mean\": 253.49}, {\"step\": 105000, \"value_mean\": 539.34}, {\"step\": 155000, \"value_mean\": 633.42}, {\"step\": 205000, \"value_mean\": 658.92}, {\"step\": 255000, \"value_mean\": 663.87}, {\"step\": 305000, \"value_mean\": 663.86}, {\"step\": 355000, \"value_mean\": 663.78}, {\"step\": 405000, \"value_mean\": 663.95}, {\"step\": 455000, \"value_mean\": 664.42}, {\"step\": 505000, \"value_mean\": 665.17}], \"ve_ratio_trajectory\": [{\"step\": 25000, \"ve\": 0.141}, {\"step\": 55000, \"ve\": 0.475}, {\"step\": 105000, \"ve\": 0.645}, {\"step\": 155000, \"ve\": 0.813}, {\"step\": 205000, \"ve\": 0.743}, {\"step\": 255000, \"ve\": 0.709}, {\"step\": 305000, \"ve\": 0.708}, {\"step\": 355000, \"ve\": 0.712}, {\"step\": 405000, \"ve\": 0.7}, {\"step\": 455000, \"ve\": 0.709}, {\"step\": 505000, \"ve\": 0.694}], \"ve_stable_range\": \"0.69-0.72 from 235K+\", \"vs_exp001_105K\": \"836.51 vs 915.67 (-8.6%)\", \"vs_exp001_final\": \"957.87 vs 970.41 (-1.3%)\", \"vs_exp001_last10\": \"947.19 vs 950.90 (-0.4%)\", \"vs_exp001_peak\": \"966.94 vs 970.41 (-0.4%)\"}, \"notes\": \"Baseline seed 2 完成。与 exp_001 (seed 0/1) 高度一致: peak 966.94 vs 970.41 (-0.4%), last10 mean 947.19 vs 950.90 (-0.4%), v/e stable 0.69-0.72 匹配。105K 处 836.51 比 seed 0/1 的 915.67 低 8.6%，但 215K+ 后完全收敛。345K 有一个 dip 到 816 但迅速恢复。baseline 跨 seed 一致性确认。\", \"pid\": \"142508\", \"reproduce\": {\"code_commit\": \"09876d7080affdb0fb329e24753a46d998da9d8e\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009a_baseline_walker_s2 --steps 500000 --seed 2 --compile False --device cuda:0\\\"\", \"gpu\": \"cuda:0\", \"server\": \"bjb1-45299\", \"started_at\": \"2026-05-14T07:19:08.969Z\"}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"data_count\": 500000, \"data_path\": \"dmc_walker_walk\", \"model_name\": \"DreamerV3 (original, gate_enabled=false)\", \"seed\": 2}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T06:33:16.385Z\"}, \"exp_008e_v3_walker_s2\": {\"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008e_v3_walker_s2/latest.pt\", \"completed_at\": \"2026-05-15T06:00:20.816Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-14T14:29:53.738Z\", \"gpu\": \"cuda:1\", \"hypothesis\": \"Walker Walk trained dt_emb + subsample ON + dt=1 imag + H=15 seed 2 — crown jewel C6 seed 2 验证\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008e_v3_walker_s2/\", \"metrics\": {\"actor_entropy_collapse_signature\": \"entropy rose from -5.21@85K to -3.83@105K (policy destabilizing during collapse)\", \"actor_entropy_trajectory\": [{\"actor_entropy\": 8.239, \"step\": 5000}, {\"actor_entropy\": 2.352, \"step\": 15000}, {\"actor_entropy\": 0.17, \"step\": 25000}, {\"actor_entropy\": -3.498, \"step\": 35000}, {\"actor_entropy\": -4.915, \"step\": 45000}, {\"actor_entropy\": -5.121, \"step\": 55000}, {\"actor_entropy\": -5.135, \"step\": 65000}, {\"actor_entropy\": -5.224, \"step\": 75000}, {\"actor_entropy\": -5.208, \"step\": 85000}, {\"actor_entropy\": -4.529, \"step\": 95000}, {\"actor_entropy\": -3.828, \"step\": 105000}], \"baseline_105K\": 915.67, \"collapse_confirmed\": \"105K (nve=3.78x, eval 715→137)\", \"collapse_onset\": \"95K (nve jumped from 0.68x to 1.34x)\", \"eval_trajectory\": [{\"eval_return\": 39.27, \"step\": 5000}, {\"eval_return\": 180.85, \"step\": 15000}, {\"eval_return\": 211.82, \"step\": 25000}, {\"eval_return\": 320.39, \"step\": 35000}, {\"eval_return\": 356.93, \"step\": 45000}, {\"eval_return\": 418.32, \"step\": 55000}, {\"eval_return\": 435.09, \"step\": 65000}, {\"eval_return\": 576.54, \"step\": 75000}, {\"eval_return\": 715.21, \"step\": 85000}, {\"eval_return\": 452.43, \"step\": 95000}, {\"eval_return\": 136.96, \"step\": 105000}], \"final_eval_return\": 136.96, \"final_nve\": 3.78, \"final_value_mean\": 339.84, \"final_ve_ratio\": 2.481, \"gate_dt_1_frac\": 1, \"gate_dt_mean\": 1, \"peak_eval_return\": 715.21, \"peak_eval_step\": 85000, \"train_return_108K\": \"19-23 (random policy level)\", \"value_trajectory\": [{\"step\": 5000, \"value_mean\": 0}, {\"step\": 15000, \"value_mean\": 3.91}, {\"step\": 25000, \"value_mean\": 30.27}, {\"step\": 35000, \"value_mean\": 79.75}, {\"step\": 45000, \"value_mean\": 125.25}, {\"step\": 55000, \"value_mean\": 172.89}, {\"step\": 65000, \"value_mean\": 220.47}, {\"step\": 75000, \"value_mean\": 272.64}, {\"step\": 85000, \"value_mean\": 339.3}, {\"step\": 95000, \"value_mean\": 384.39}, {\"step\": 105000, \"value_mean\": 339.84}], \"ve_ratio_trajectory\": [{\"nve\": 1.64, \"step\": 25000, \"ve\": 0.143}, {\"nve\": 1.03, \"step\": 35000, \"ve\": 0.249}, {\"nve\": 1.06, \"step\": 45000, \"ve\": 0.351}, {\"nve\": 1.02, \"step\": 55000, \"ve\": 0.413}, {\"nve\": 0.9, \"step\": 65000, \"ve\": 0.507}, {\"nve\": 0.66, \"step\": 75000, \"ve\": 0.473}, {\"nve\": 0.68, \"step\": 85000, \"ve\": 0.474}, {\"nve\": 1.34, \"step\": 95000, \"ve\": 0.85}, {\"nve\": 3.78, \"step\": 105000, \"ve\": 2.481}], \"vs_baseline_105K\": \"-85.0%\"}, \"model_name\": \"DreamerV3+SubsampleON_FixedDt1_H15 (gate_subsample_max_dt=2, gate_fixed_dt=1, imag_horizon=15, trained dt_emb)\", \"notes\": \"C6 seed 2 COLLAPSED. Delusional critic collapse at 85K→105K despite gate_dt_mean=1.0 locked throughout. eval peaked 715@85K then crashed to 137@105K (v/e=2.48, nve=3.78x). Cross-seed: seed 0=869.9 (healthy), seed 1=869.9 (healthy), seed 2=137 (collapsed). Collapse is stochastic (1/3 seeds) even in dt=1 imagination config. Subsample ON training data (dt=2 transitions) appears sufficient to trigger delusional critic in some seeds. Train returns at 108K=19-23 (random policy).\", \"parent\": \"exp_008e_v3_subsample_on_dt1_h15\", \"pid\": \"43437\", \"reproduce\": {\"code_commit\": \"09876d7080affdb0fb329e24753a46d998da9d8e\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008e_v3_walker_s2 --steps 105000 --seed 2 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 1 --gate_subsample_max_dt 2 --imag_horizon 15\\\"\"}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008e_v3_walker_s2 --steps 105000 --seed 2 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 1 --gate_subsample_max_dt 2 --imag_horizon 15\\\"\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 5.23, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_008e_v3_walker_s2.log\", \"pid\": \"43437\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-15T00:46:45.424Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 18815.4}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T06:24:21.709Z\"}, \"exp_008e_v3_walker_s1\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008e_v3_walker_s1/latest.pt\", \"completed_at\": \"2026-05-15T00:44:53.439Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-14T14:29:53.120Z\", \"gpu\": \"cuda:1\", \"hypothesis\": \"Walker Walk trained dt_emb + subsample ON + dt=1 imag + H=15 seed 1 — crown jewel C6 验证：trained dt_emb 在 dt=1 imagination 下不触发 delusional critic（plan_014）\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008e_v3_walker_s1/\", \"metrics\": {\"eval_trajectory\": [{\"eval_return\": 31, \"step\": 5000}, {\"eval_return\": 131.2, \"step\": 15000}, {\"eval_return\": 155.7, \"step\": 25000}, {\"eval_return\": 276.5, \"step\": 35000}, {\"eval_return\": 382.2, \"step\": 45000}, {\"eval_return\": 486.8, \"step\": 55000}, {\"eval_return\": 580.7, \"step\": 65000}, {\"eval_return\": 574.1, \"step\": 75000}, {\"eval_return\": 657.3, \"step\": 85000}, {\"eval_return\": 851.9, \"step\": 95000}, {\"eval_return\": 869.9, \"step\": 105000}], \"exit_code\": 0, \"final_eval_return\": 869.9, \"final_value_mean\": 457.9, \"gate_dt_1_frac\": 1, \"total_steps\": 112000, \"ve_ratio_105k\": 0.527}, \"model_name\": \"DreamerV3+SubsampleON_FixedDt1_H15 (gate_subsample_max_dt=2, gate_fixed_dt=1, imag_horizon=15, trained dt_emb)\", \"notes\": \"Crown jewel C6 seed 1 SUCCESS. eval_return=869.9@105K, v/e=0.527 (healthy, no delusional critic). Gate locked dt=1 throughout. Trajectory: 31→131→156→276→382→487→581→574→657→852→870. Consistent with seed 0, confirms trained dt_emb + dt=1 imagination is safe.\", \"parent\": \"exp_008e_v3_subsample_on_dt1_h15\", \"pid\": \"898127\", \"reproduce\": {\"code_commit\": \"09876d7080affdb0fb329e24753a46d998da9d8e\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008e_v3_walker_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 1 --gate_subsample_max_dt 2 --imag_horizon 15\\\"\"}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008e_v3_walker_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 1 --gate_subsample_max_dt 2 --imag_horizon 15\\\"\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 5.92, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_008e_v3_walker_s1.log\", \"pid\": \"898127\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-14T18:49:27.945Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 21325.5}, \"status\": \"DONE\", \"updated_at\": \"2026-05-15T00:44:53.439Z\"}, \"exp_006\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-14T00:49:02.944Z\", \"metrics\": {\"baseline_return_at_55k\": 625.7, \"deficit_pct\": -42.4, \"deficit_vs_baseline_at_55k\": -265.3, \"eval_return\": {\"15000\": 256.9, \"25000\": 321.4, \"35000\": 485.3, \"45000\": 477, \"5000\": 31, \"55000\": 360.4}, \"gate_dt_mean\": 2, \"latest_return\": 360.4, \"latest_step\": 55000, \"model_loss_at_55k\": 4.853, \"peak_return\": 485.3, \"peak_step\": 35000}, \"notes\": \"早期条目，权威数据在 exp_006_fixed_dt2。conclusion=killed（D034 registry 清理）。\", \"retry_count\": 0, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T22:31:54.922Z\"}, \"exp_008a\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-14T04:07:59.793Z\", \"metrics\": {\"eval_return_15K\": 167.2, \"eval_return_25K\": 230.8, \"eval_return_35K\": 500.8, \"eval_return_45K\": 563.4, \"eval_return_55K\": 487.9, \"eval_return_5K\": 31, \"eval_return_65K\": \"pending (eval in progress)\", \"step\": 65000, \"train_return_64K_avg\": 556.6, \"trend\": \"peaked @45K=563, dipped to @55K=488, 65K eval in progress; train returns @64K healthy (~557)\", \"value_eval_ratio_55K\": \"37.6%\", \"value_mean_55K\": 183.5}, \"notes\": \"早期条目，权威数据在 exp_008a_no_subsample_dt2。conclusion=killed（D034 registry 清理）。\", \"retry_count\": 0, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T22:31:54.075Z\"}, \"exp_008c\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-14T04:08:02.608Z\", \"metrics\": {\"eval_return_15K\": 171.3, \"eval_return_25K\": 192.4, \"eval_return_35K\": 185.1, \"eval_return_45K\": 226.6, \"eval_return_55K\": 241.9, \"eval_return_5K\": 31, \"eval_return_65K\": 240.9, \"step\": 68000, \"train_return_68K_avg\": 245.1, \"trend\": \"flat plateau @55K-65K (~241), very slow learner with h8, value/eval=32.8% (no collapse)\", \"value_eval_ratio_65K\": \"32.8%\", \"value_mean_65K\": 79}, \"notes\": \"早期条目，权威数据在正式命名实验中。conclusion=killed（D034 registry 清理）。\", \"retry_count\": 0, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T22:31:52.611Z\"}, \"exp_008d\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-14T04:08:05.136Z\", \"metrics\": {\"eval_return_15K\": 153.7, \"eval_return_25K\": 167.2, \"eval_return_35K\": 146.3, \"eval_return_5K\": 31, \"step\": 40000, \"train_return_40K_avg\": 119.3, \"trend\": \"declining — train_return @40K avg=119 below @35K eval=146, value/eval=41.1% not yet >50% but train performance dropping\", \"value_eval_ratio_35K\": \"41.1%\", \"value_mean_35K\": 60.2}, \"notes\": \"早期条目，权威数据在 exp_008d_subsample_on_h8。conclusion=killed（D034 registry 清理）。\", \"retry_count\": 0, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T22:31:51.696Z\"}, \"exp_008e_v2_subsample_on_dt1_h15\": {\"conclusion\": \"killed\", \"created_at\": \"2026-05-14T04:26:39.732Z\", \"notes\": \"已被 exp_008e_v3_subsample_on_dt1_h15 取代，进程已死。conclusion=killed（D034 registry 清理）。\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008e_v2_subsample_on_dt1_h15 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 1 --gate_subsample_max_dt 2 --imag_horizon 15\\\"\", \"gpu\": [\"cuda:1\"], \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_008e_v2_subsample_on_dt1_h15.log\", \"pid\": \"125392\", \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-14T04:27:30.720Z\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T22:31:49.814Z\"}, \"exp_rssm_fidelity_analysis\": {\"conclusion\": \"success\", \"created_at\": \"2026-05-14T11:09:52.237Z\", \"hypothesis\": \"RSSM prediction quality analysis: 比较 baseline/008d/008f 在 dt=1 vs dt=2 transitions 上的 obs_MSE 和 reward_MAE，量化 RSSM fidelity gap (plan_030)\", \"metrics\": {\"008d_trained_dtEmb\": {\"dt1_obs_mse\": 41.31, \"dt1_reward_mae\": 0.0568, \"dt2_obs_mse\": 53.67, \"dt2_reward_mae\": 0.1579, \"obs_gap\": 1.3, \"reward_gap\": 2.78}, \"008f_no_dtEmb\": {\"dt1_obs_mse\": 8.01, \"dt1_reward_mae\": 0.7469, \"dt2_obs_mse\": 22.04, \"dt2_reward_mae\": 0.7526, \"obs_gap\": 2.75, \"reward_gap\": 1.01}, \"baseline\": {\"dt1_obs_mse\": 13.49, \"dt1_reward_mae\": 0.0102, \"dt2_obs_mse\": 27.5, \"dt2_reward_mae\": 0.0159, \"obs_gap\": 2.04, \"reward_gap\": 1.56}}, \"notes\": \"分析实验，非训练实验。conclusion=success，状态从 PREPARING 修正为 DONE（D034 registry 清理）。\", \"retry_count\": 0, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T22:31:48.642Z\"}, \"exp_008e_v3_subsample_on_dt1_h15\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008e_v3_subsample_on_dt1_h15/latest.pt\", \"completed_at\": \"2026-05-14T09:07:47.319Z\", \"conclusion\": \"success\", \"created_at\": \"2026-05-14T04:29:31.656Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-14T09:05:44.288431+00:00\"}]}, \"hypothesis\": \"B+ confound control：subsample ON + untrained dt_emb + dt=1 imagination + H=15。验证 subsample ON 训练数据（含 dt=2 transitions）是否本身导致性能下降，即使 imagination 只用 dt=1。对照 008a（subsample OFF）和 baseline。如果 008e_v3 性能接近 baseline → subsample ON 本身无害。如果下降 → subsample ON 改变了 RSSM dynamics。\", \"metrics\": {\"baseline_105K\": 915.67, \"current_step\": 112000, \"eval_return\": {\"105K\": 869.88, \"15K\": 131.2, \"25K\": 155.69, \"35K\": 276.47, \"45K\": 382.22, \"55K\": 486.84, \"5K\": 31, \"65K\": 580.67, \"75K\": 574.09, \"85K\": 657.31, \"95K\": 851.86}, \"fps\": 7.01, \"gate_dt_1_frac\": 1, \"gate_dt_mean\": 1, \"last_updated\": \"2026-05-14T09:09:00\", \"normalized_ve\": {\"105K\": 0.8, \"25K\": 1.93, \"35K\": 0.94, \"45K\": 0.88, \"55K\": 0.87, \"65K\": 0.72, \"75K\": 0.73, \"85K\": 0.76, \"95K\": 0.75}, \"target_steps\": 105000, \"value_eval_ratio\": {\"105K\": 0.527, \"25K\": 0.168, \"35K\": 0.227, \"45K\": 0.29, \"55K\": 0.35, \"65K\": 0.405, \"75K\": 0.523, \"85K\": 0.534, \"95K\": 0.476}, \"value_mean\": {\"105K\": 457.93, \"25K\": 26.19, \"35K\": 62.76, \"45K\": 110.67, \"55K\": 170.09, \"65K\": 235.05, \"75K\": 300.51, \"85K\": 351.33, \"95K\": 405.25}, \"verdict\": \"SUCCESS - 95% baseline, normalized v/e stable 0.72-0.80x, B+ hypothesis confirmed\", \"vs_baseline_105K\": \"-5.0%\"}, \"model_name\": \"DreamerV3+SubsampleON_FixedDt1_H15 (gate_subsample_max_dt=2, gate_fixed_dt=1, imag_horizon=15, trained dt_emb)\", \"reproduce\": {\"finished_at\": \"2026-05-14T09:05:42.563Z\"}, \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008e_v3_subsample_on_dt1_h15 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 1 --gate_subsample_max_dt 2 --imag_horizon 15\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 4.64, \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008e_v3_subsample_on_dt1_h15\", \"model_name\": \"DreamerV3+SubsampleON_FixedDt1_H15 (gate_subsample_max_dt=2, gate_fixed_dt=1, imag_horizon=15, untrained dt_emb)\", \"pid\": \"126110\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-14T04:29:31.600Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 16695.7}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T19:46:00.840Z\"}, \"exp_009c_008f_walker_s2\": {\"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009c_008f_walker_s2/latest.pt\", \"completed_at\": \"2026-05-14T22:15:00Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-14T07:17:26.154Z\", \"extra\": {\"hook_events\": [{\"action\": \"agent\", \"event\": \"on_complete\", \"ts\": \"2026-05-14T14:15:58.982844+00:00\"}]}, \"gpu\": \"cuda:1\", \"hypothesis\": \"Walker Walk dt_embed_dim=0 + subsample ON + H=8 seed 2 — 多 seed 复现 008f 因果控制稳定性，巩固 C2 统计显著性（plan_012）\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_009c_008f_walker_s2.log\", \"metrics\": {\"baseline_105K\": 915.67, \"causal_conclusion\": \"Seed 2 does NOT replicate seed 1's zigzag recovery. 008f seed 1 peaked at 503@105K with rising trend; seed 2 peaked at 359@75K then declined to 148@105K. The adaptive horizon mechanism's benefit appears seed-dependent and not robust.\", \"current_step\": 105000, \"eval_checkpoints\": [{\"baseline_ve\": null, \"eval_return\": 30.37, \"normalized_ve\": null, \"step\": 5000, \"value_mean\": 0.0013, \"ve_ratio\": null}, {\"baseline_ve\": null, \"eval_return\": 157.15, \"normalized_ve\": null, \"step\": 15000, \"value_mean\": 3.057, \"ve_ratio\": 0.019}, {\"baseline_ve\": 0.087, \"eval_return\": 168.75, \"normalized_ve\": 1.26, \"step\": 25000, \"value_mean\": 18.536, \"ve_ratio\": 0.11}, {\"baseline_ve\": 0.241, \"eval_return\": 178.94, \"normalized_ve\": 0.79, \"step\": 35000, \"value_mean\": 34.263, \"ve_ratio\": 0.191}, {\"baseline_ve\": 0.331, \"eval_return\": 211.08, \"normalized_ve\": 0.72, \"step\": 45000, \"value_mean\": 50.099, \"ve_ratio\": 0.237}, {\"baseline_ve\": 0.404, \"eval_return\": 238.91, \"normalized_ve\": 0.66, \"step\": 55000, \"value_mean\": 63.267, \"ve_ratio\": 0.265}, {\"baseline_ve\": 0.563, \"eval_return\": 244.15, \"normalized_ve\": 0.53, \"step\": 65000, \"value_mean\": 72.717, \"ve_ratio\": 0.298}, {\"baseline_ve\": 0.719, \"eval_return\": 359.14, \"normalized_ve\": 0.33, \"step\": 75000, \"value_mean\": 83.91, \"ve_ratio\": 0.234}, {\"baseline_ve\": 0.701, \"eval_return\": 227.43, \"normalized_ve\": 0.6, \"step\": 85000, \"value_mean\": 96.071, \"ve_ratio\": 0.422}, {\"baseline_ve\": 0.632, \"eval_return\": 190.94, \"normalized_ve\": 0.9, \"step\": 95000, \"value_mean\": 108.29, \"ve_ratio\": 0.567}, {\"baseline_ve\": 0.656, \"eval_return\": 148.34, \"normalized_ve\": 1.14, \"step\": 105000, \"value_mean\": 111.247, \"ve_ratio\": 0.75}], \"target_steps\": 105000, \"trend\": \"Peak 359@75K then monotonic decline to 148@105K; no recovery pattern unlike 008f seed 1's zigzag recovery to 503\", \"verdict\": \"NEGATIVE - no delusional critic (normalized v/e < 1.5x) but persistent decline after 75K; cross-seed consistency with 008f seed 1 NOT confirmed\", \"vs_baseline_105K\": \"-83.8%\"}, \"notes\": \"D031 排期修正: 009c 延长 200K 降优先级，排在 009e/009f 之后。cuda:1 排期: 009b → 008e_v3_s1 → 008e_v3_s2 → 009e → 009f → 009c(200K) → plan_060。105K 指标: eval=148.34, value=111.25, nve=1.14x。\", \"parent\": \"exp_008f_no_dt_embed_subsample_on_h8\", \"pid\": \"140980\", \"reproduce\": {\"code_commit\": \"09876d7080affdb0fb329e24753a46d998da9d8e\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_009c_008f_walker_s2 --steps 105000 --seed 2 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8 --gate_dt_embed_dim 0\\\"\", \"finished_at\": \"2026-05-14T14:15:57.425Z\", \"gpu\": \"cuda:1\", \"server\": \"bjb1-45299\", \"started_at\": \"2026-05-14T07:19:10.835Z\", \"training_hours\": 6.95}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009c_008f_walker_s2\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009c_008f_walker_s2/metrics.jsonl\", \"model_name\": \"DreamerV3+FixedDt2_NoDtEmbed_Subsample_H8 (gate_fixed_dt=2, gate_subsample_max_dt=2, imag_horizon=8, gate_dt_embed_dim=0)\", \"seed\": 2}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T14:34:24.161Z\"}, \"exp_006_fixed_dt2\": {\"account\": \"root\", \"completed_at\": \"2026-05-14T01:13:11.533Z\", \"conclusion\": \"negative\", \"created_at\": \"2026-05-13T21:10:58.851Z\", \"extra\": {\"audit_commit\": \"6159e46\", \"bugs_fixed\": \"_effective_max_dt not synced in fixed_dt mode; hardcoded curriculum phases ignoring config\", \"curriculum_audit\": \"Curriculum does NOT apply in fixed_dt mode (models.py:200-205). gate_fixed_dt>0 bypasses _update_gate_schedule(). subsample_variable_dt receives effective_max_dt=2.0 from step 0, training data is 58.5% dt=1 + 41.5% dt=2 throughout. Actual train/imagine mismatch: mixed dt training vs pure dt=2 imagination.\"}, \"gpu\": \"cuda:0\", \"hypothesis\": \"诊断实验：fixed dt=2 vs learned gate。去掉 Gumbel-Softmax gate，硬编码 dt=2，其余超参与 exp_005 完全一致。量化 learned gate 的价值——如果 fixed dt=2 也掉 return，说明跳步本身有害；如果不掉，问题在 gate 学习机制。\", \"latest_metrics\": {\"checked_at\": \"2026-05-14\", \"eval_return\": 485.3, \"eval_return_trajectory\": {\"15K\": 256.9, \"25K\": 321.4, \"35K\": 485.3, \"5K\": 31}, \"eval_step\": 35000, \"fps\": 6.6, \"gate_dt_mean\": 2, \"gate_dt_std\": 0, \"grad_norm\": 8.6, \"pid\": 85029, \"prev_eval_return\": 321.4, \"process_status\": \"running\", \"step\": 36000}, \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_006_fixed_dt2.log\", \"metrics\": {\"baseline_35K\": 388.5, \"baseline_45K\": 513.8, \"baseline_55K\": 625.7, \"data_source_ve\": \"from training logs metrics.jsonl\", \"eval_return_15K\": 256.9, \"eval_return_25K\": 321.4, \"eval_return_35K\": 485.3, \"eval_return_45K\": 477, \"eval_return_55K\": 360.4, \"eval_return_5K\": 31, \"eval_return_65K\": 132.86, \"fps\": 6.5, \"gate_dt_mean\": 2, \"gate_dt_std\": 0, \"model_loss_15K\": 7.593, \"model_loss_25K\": 5.633, \"model_loss_35K\": 5.229, \"model_loss_45K\": 5.023, \"model_loss_55K\": 4.9, \"model_loss_5K\": 20.738, \"peak_return\": 485.3, \"peak_step\": \"35K\", \"step\": 65000, \"trend\": \"inverted-V: peak 485@35K, collapsing to 133@65K; v/e accelerating: 31.1%→53.3%→93.3%→272% (value 2.7x eval_return at 65K)\", \"value_eval_ratio_35K\": 0.311, \"value_eval_ratio_45K\": 0.533, \"value_eval_ratio_55K\": 0.933, \"value_eval_ratio_65K\": 2.722, \"value_mean_35K\": 151.1, \"value_mean_45K\": 254.29, \"value_mean_55K\": 336.44, \"value_mean_65K\": 361.69, \"vs_baseline_55K\": \"-42.4%\"}, \"parent\": \"exp_005_event_gated_v4\", \"pid\": \"85029\", \"reproduce\": {\"code_commit\": \"6ef8646d807cd10ce0c88e10a7e943211e7fc44c\", \"command\": \"bash -c \\\"cd /root/autodl-tmp/event-gated-adaptive-horizon && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && CUDA_VISIBLE_DEVICES=0 python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/fixed_dt2_v1_s1 --steps 150000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2\\\"\", \"gpu\": \"cuda:0\", \"server\": \"bjb1-45299\", \"started_at\": \"2026-05-13T22:12:00.446Z\"}, \"retry_count\": 0, \"server\": \"bjb1-45299\", \"spec\": {\"checkpoint_path\": \"N/A - negative result, fixed dt=2 collapsed to 132.9@65K (21.6% baseline)\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/fixed_dt2_v1_s1 --steps 150000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2\", \"data_count\": 150000, \"data_path\": \"dmc_walker_walk\", \"failure_reason\": \"fixed dt=2 崩塌：训练分布混合（58.5% dt=1 + 41.5% dt=2 log-uniform）+ 想象纯 dt=2 条件下，eval_return 从 peak 485@35K 持续下降至 132.9@65K（baseline 同期 615.9）。与 learned gate 变体一致的崩塌模式。代码审计确认 curriculum 不生效（gate_fixed_dt>0 跳过 _update_gate_schedule）。\", \"gpu\": [\"cuda:0\"], \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/fixed_dt2_v1_s1\", \"model_name\": \"DreamerV3+FixedDt2 (gate_fixed_dt=2, no learned gate)\", \"pid\": \"85029\", \"seed\": 1, \"server\": \"bjb1-45299\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T10:20:11.722Z\"}, \"exp_008e_subsample_on_fixed_dt1\": {\"checkpoint_path\": \"N/A - killed, duplicate registry entry, logdir contaminated by dual-process write\", \"completed_at\": \"2026-05-14T04:21:47.956Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-14T04:10:07.303Z\", \"failure_reason\": \"重复 registry 条目 + logdir 被两个进程交叉写入导致 tfevents/metrics.jsonl 损坏。Director 指令清理后以 exp_008e_subsample_on_dt1_h15 为准重跑。\", \"hypothesis\": \"验证 Reviewer D020 因果假说：subsample ON 训练 dt_embedding[2]（RSSM 精确预测 dt=2），但 actor/critic 仅在 dt=1 imagination 训练。如果 value/eval ratio 仍加速上升 → dt_embedding 训练本身导致 value 过估（delusional critic），即使 actor 不用 dt=2 imagination。对照：008a (subsample OFF, dt=2 imag) value/eval=37.6%@55K vs exp_006 (subsample ON, dt=2 imag) 53.3%。\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008e_subsample_on_fixed_dt1_h15 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 1 --gate_subsample_max_dt 2 --imag_horizon 15\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 0.19, \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008e_subsample_on_fixed_dt1_h15\", \"model_name\": \"DreamerV3+SubsampleON_FixedDt1_H15 (gate_subsample_max_dt=2, gate_fixed_dt=1, imag_horizon=15)\", \"pid\": \"121636\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-14T04:10:22.915Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 685.0}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T04:24:58.056Z\"}, \"exp_008e_subsample_on_dt1_h15\": {\"checkpoint_path\": \"N/A - killed, logdir contaminated by duplicate process cross-write\", \"completed_at\": \"2026-05-14T04:21:48.584Z\", \"conclusion\": \"killed\", \"created_at\": \"2026-05-14T04:10:37.655Z\", \"hypothesis\": \"验证 Reviewer D020 delusional critic 假说：subsample ON 训练 dt_embedding[2]（RSSM 精确预测 dt=2），但 actor/critic 仅在 dt=1 imagination 训练。如果 value/eval ratio 仍加速上升 → dt_embedding 训练本身导致 value 过估（即使 actor 不用 dt=2 imagination）。对照：008a（subsample OFF，dt=2 imagination）和 006（subsample ON，dt=2 imagination）。\", \"notes\": \"重复进程：与 exp_008e_subsample_on_fixed_dt1 命令完全相同，共享同一 logdir，导致 tfevents 文件互相污染。Kill PID 122038，保留 PID 121636。\", \"retry_count\": 0, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && export MUJOCO_GL=osmesa && export PYOPENGL_PLATFORM=osmesa && cd /root/autodl-tmp/event-gated-adaptive-horizon && python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_008e_subsample_on_fixed_dt1_h15 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 1 --gate_subsample_max_dt 2 --imag_horizon 15\\\"\", \"data_count\": 105000, \"data_path\": \"dmc_walker_walk\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 0.18, \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_008e_subsample_on_fixed_dt1_h15\", \"model_name\": \"DreamerV3+SubsampleON_FixedDt1_H15 (gate_subsample_max_dt=2, gate_fixed_dt=1, imag_horizon=15)\", \"pid\": \"122038\", \"seed\": 1, \"server\": \"bjb1-45299\", \"submitted_at\": \"2026-05-14T04:10:46.045Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 662.5}, \"status\": \"DONE\", \"updated_at\": \"2026-05-14T04:24:57.658Z\"}, \"exp_002_event_gated\": {\"completed_at\": \"2026-05-13T04:50:14.987Z\", \"conclusion\": \"failed\", \"created_at\": \"2026-05-13T02:09:54.240Z\", \"hypothesis\": \"Event-gated variable-rate RSSM produces meaningful Δt patterns (entropy>0.3, H_eff>1.2×H_nominal) without breaking training stability (return≥80% baseline)\", \"kill_reason\": \"Phase 1 subsample 设计缺陷：subsample_variable_dt 在 Phase 1 (gate_scale=0) 也生效，RSSM 用 variable-Δt 数据训练但 imagination 只用 Δt=1，return 恶化到 baseline 的 25%。手动 kill 后部署 subsample curriculum 补丁并重启为 exp_003。\", \"retry_count\": 0, \"spec\": {\"command\": \"python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/event_gated_s1 --steps 500000 --seed 1 --compile False --device cuda:1 --gate_enabled True\", \"data_count\": 500000, \"data_path\": \"DMC Walker Walk (dm_control built-in)\", \"gpu_id\": 1, \"hypothesis\": \"Event-gated variable-rate RSSM produces meaningful Δt patterns (entropy>0.3, H_eff>1.2×H_nominal) without breaking training stability (return≥80% baseline)\", \"log_path\": \"/root/autodl-tmp/event-gated-adaptive-horizon/logdir/event_gated_s1\", \"model_name\": \"DreamerV3 + Event-Gated Variable-Rate RSSM (K=8, τ=5→0.5, λ_H=0.1→0.01)\", \"pid\": 9769, \"seed\": 1, \"server\": \"autodl-rtx6000\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-13T04:52:18.089Z\"}}, \"count\": 158, \"total\": 158, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.6586}}"
    }
  }
}
```

</details>

---


### Tool call

_source line 56_

<details open><summary>🔧 Tool call — Bash · `toolu_01SUbNYtRVxY8Mwcad9GXumJ`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/ae813a79-db9f-4a12-b6ee-ad91ade39065/tool-results/mcp-agent-ml-research-read_registry-1779718348946.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps = result.get('data', result)\nif isinstance(exps, dict) and 'experiments' in exps:\n    exps = exps['experiments']\nelif isinstance(exps, dict) and 'data' in exps:\n    exps = exps['data']\n\nif isinstance(exps, dict):\n    items = list(exps.values())\n    exp_ids = list(exps.keys())\nelse:\n    items = exps\n    exp_ids = list(range(len(items)))\n\ntotal = len(items)\n\n# Count conclusions\nconclusions = {}\nfor e in items:\n    c = e.get('conclusion', 'unknown') if isinstance(e, dict) else 'unknown'\n    conclusions[c] = conclusions.get(c, 0) + 1\n\n# Count unique configurations (strip seed suffix from exp_id)\nimport re\nconfigs = set()\nfor eid in exp_ids:\n    # Remove seed suffixes like _s0, _s1, _s2 etc\n    cfg = re.sub(r'_s\\d+$', '', eid)\n    configs.add(cfg)\n\n# Also count 'successful conditions' = configs where at least one experiment concluded success\nconfig_conclusions = {}\nfor eid, e in zip(exp_ids, items):\n    cfg = re.sub(r'_s\\d+$', '', eid)\n    c = e.get('conclusion', 'unknown') if isinstance(e, dict) else 'unknown'\n    if cfg not in config_conclusions:\n        config_conclusions[cfg] = set()\n    config_conclusions[cfg].add(c)\n\nsuccessful_configs = sum(1 for cfg, cs in config_conclusions.items() if 'success' in cs)\nnegative_configs = sum(1 for cfg, cs in config_conclusions.items() if 'negative' in cs)\n\nprint(f'Total experiments: {total}')\nfor k, v in sorted(conclusions.items()):\n    print(f'  {k}: {v}')\nprint(f'Unique configurations: {len(configs)}')\nprint(f'Configs with at least one success: {successful_configs}')\nprint(f'Configs with at least one negative: {negative_configs}')\n\n# Print 'successful conditions' = experiments with conclusion=success or negative (i.e. not failed/killed)\ncompleted = conclusions.get('success', 0) + conclusions.get('negative', 0)\nprint(f'Completed (success+negative): {completed}')\n\"\n",
  "description": "Count experiments, configurations, and successful conditions",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ae813a79-db9f-4a12-b6ee-ad91ade39065",
  "uuid": "608947cd-16c9-43f4-ba4c-d0f29b5bd9ed",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B3CjNnyWQc51u75mqwsisp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 677,
      "cache_read_input_tokens": 42901,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 677
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

_source line 57 · 2026-05-25T14:12:41.861Z_

<details><summary>↩ Tool result · `toolu_01SUbNYtRVxY8Mwcad9GXumJ`</summary>

```text
Total experiments: 158
  failed: 11
  killed: 24
  negative: 39
  success: 80
  unknown: 4
Unique configurations: 136
Configs with at least one success: 70
Configs with at least one negative: 38
Completed (success+negative): 119
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ae813a79-db9f-4a12-b6ee-ad91ade39065",
  "uuid": "7d24a54c-a5a4-4980-970d-091e3df1f096",
  "tool_use_result": {
    "stdout": "Total experiments: 158\n  failed: 11\n  killed: 24\n  negative: 39\n  success: 80\n  unknown: 4\nUnique configurations: 136\nConfigs with at least one success: 70\nConfigs with at least one negative: 38\nCompleted (success+negative): 119",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Assistant

_source line 58_

<details><summary>Logged reasoning block</summary>

```text
Hmm, the counts differ slightly between the two registry reads (success went from 79 to 80, unknown from 5 to 4 — possibly because the full-fields registry is slightly newer). Let me use the full-fields one: 158 total, 80 success, 39 negative, 11 failed, 24 killed, 4 unknown.

But 136 unique configurations seems too many — almost 1:1 with experiments. The configuration deduplication by stripping seed suffix isn't working well because many experiment IDs don't follow the `_s\d+` pattern. Let me look at some IDs.
 
Wait, the Q&A text mentions "133 experiments across 43 configurations," so that 43 is probably hand-curated rather than something I can derive automatically. Since the registry now shows 158 experiments, the configuration grouping might come from a different source entirely. I should examine the actual experiment IDs to figure out how they're meant to be grouped.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ae813a79-db9f-4a12-b6ee-ad91ade39065",
  "uuid": "b01926a3-2de2-4c4b-a32b-832e66ceb563",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N3Ug5U3wo8JNuJDHXzEezX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 910,
      "cache_read_input_tokens": 43578,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 910
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

_source line 59_

<details open><summary>🔧 Tool call — Bash · `toolu_01KJJX33gvgEfmBd58YUXhoG`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/ae813a79-db9f-4a12-b6ee-ad91ade39065/tool-results/mcp-agent-ml-research-read_registry-1779718348946.txt | python3 -c \"\nimport json, sys, re\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps = result.get('data', result)\nif isinstance(exps, dict) and 'experiments' in exps:\n    exps = exps['experiments']\nelif isinstance(exps, dict) and 'data' in exps:\n    exps = exps['data']\n\nif isinstance(exps, dict):\n    exp_ids = sorted(exps.keys())\nelse:\n    exp_ids = list(range(len(exps)))\n\n# Print all experiment IDs to understand naming patterns\nfor eid in exp_ids:\n    print(eid)\n\"\n",
  "description": "List all experiment IDs",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ae813a79-db9f-4a12-b6ee-ad91ade39065",
  "uuid": "26bfea8b-05fe-46db-b193-826574ae306a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N3Ug5U3wo8JNuJDHXzEezX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 910,
      "cache_read_input_tokens": 43578,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 910
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

_source line 60 · 2026-05-25T14:12:53.226Z_

<details><summary>↩ Tool result · `toolu_01KJJX33gvgEfmBd58YUXhoG`</summary>

```text
016e
exp_001_baseline
exp_001_baseline_s2
exp_001_baseline_s2_extended
exp_001_baseline_s3
exp_001_baseline_s3_extended
exp_001_baseline_s4
exp_001_baseline_s4_extended
exp_002_event_gated
exp_003_event_gated_v2
exp_004_event_gated_v3
exp_005_event_gated_v4
exp_006
exp_006_fixed_dt2
exp_007_fixed_dt4
exp_008a
exp_008a_cheetah_unexposed_s0
exp_008a_cheetah_unexposed_s1
exp_008a_no_subsample_dt2
exp_008a_unexposed_s1
exp_008a_unexposed_s2
exp_008a_untrained_s1
exp_008a_untrained_s2
exp_008c
exp_008c_no_subsample_dt2_h8
exp_008d
exp_008d_civo_trigger_s2
exp_008d_civo_trigger_s3
exp_008d_civo_trigger_s4
exp_008d_subsample_on_h8
exp_008e_subsample_on_dt1_h15
exp_008e_subsample_on_fixed_dt1
exp_008e_v2_subsample_on_dt1_h15
exp_008e_v3_s3
exp_008e_v3_s4
exp_008e_v3_subsample_on_dt1_h15
exp_008e_v3_walker_s1
exp_008e_v3_walker_s2
exp_008f_no_dt_embed_subsample_on_h8
exp_008f_s2
exp_008f_s3_no_dt_embed_walker
exp_008f_s4
exp_009a_baseline_walker_s2
exp_009b_008d_walker_s2
exp_009c_008f_walker_s2
exp_009c_s2
exp_009c_s3
exp_009d_baseline_walker_s0
exp_009d_baseline_walker_s1
exp_009e_008d_walker_s1
exp_009f_008f_walker_s1
exp_009g_008f_walker_s0
exp_009h_008f_walker_s0
exp_010a_cheetah_baseline_s1
exp_010b_cheetah_civo_trigger
exp_010b_cheetah_civo_trigger_s0
exp_015b_frozen_dt_emb
exp_016_sgs_walker_s1
exp_016b_sgs_walker_s1
exp_016c_sgs_walker_s1
exp_016d_sgs_walker_s1
exp_016e_sgs_walker_s1
exp_017_subsample_off_trained_dt_emb
exp_018_full_sgs_s2
exp_018_full_sgs_walker_s1
exp_018v2_full_sgs_walker_s1
exp_019a_pickcube_baseline
exp_019a_v2_pickcube_baseline
exp_019b_pickcube_civo_trigger
exp_020_vanilla_dreamerv3_s2
exp_021_full_sgs_cheetah_s1
exp_022_untrained_dt_emb_learned_gate
exp_022b_no_curriculum
exp_023_cheetah_baseline_s2
exp_023_cheetah_baseline_s3
exp_023_cheetah_baseline_s4
exp_023_cheetah_baseline_s4_extended
exp_023a_cheetah_baseline_s0
exp_023b_cheetah_baseline_s1
exp_024_cheetah_no_dt_emb_s0
exp_024b_cheetah_no_dt_emb_s0
exp_024b_cheetah_no_dt_emb_s1
exp_025_obs_sgs_walker_s1
exp_025_obs_sgs_walker_s2
exp_025_obs_sgs_walker_s3
exp_025_obs_sgs_walker_s4
exp_026_obs_sgs_cheetah_s0
exp_026_obs_sgs_cheetah_s1
exp_027_tcn_walker_s0
exp_027_tcn_walker_s0_sigma02
exp_027_tcn_walker_s1
exp_028_rave_walker_s0
exp_028_rave_walker_s0_ceil15
exp_029a_tcn_walker_s1_sigma02
exp_029b_tcn_walker_s2_sigma02
exp_029c_tcn_walker_s0_sigma01
exp_029d_tcn_walker_s3_sigma02
exp_030a_tcn_cheetah_s0_sigma02
exp_030b_tcn_cheetah_s0_sigma05
exp_030c_tcn_cheetah_s0_sigma10
exp_031_tcn_pickcube_s0_sigma02
exp_031b_tcn_pickcube_s0_sigma05
exp_032_dual_critic_walker
exp_032b_dual_critic_walker_s1
exp_033_wide_critic_walker
exp_034
exp_034_dual_critic_cheetah
exp_035_narrow_dual_critic_walker
exp_036_dual_critic_pickcube
exp_037_wide_critic_cheetah
exp_038_dual_critic_walker_s2
exp_039_narrow_dual_critic_walker_s1
exp_040_wide_dual_critic_cheetah
exp_041_dual_critic_walker_s3
exp_042_frozen_dt_emb_walker
exp_043_008f_walker_s1
exp_044_gradient_stop_walker
exp_045_treatment_extension_008d_s3
exp_046_frozen_dt_emb_cheetah
exp_047_frozen_dt_emb_walker_s1
exp_048_cheetah_civo_extension
exp_049_stackcube_civo_trigger_s0
exp_050_peginsertion_civo_trigger_s0
exp_051_stackcube_frozen_dt_emb_s0
exp_052_stackcube_civo_trigger_s1
exp_053_peginsertion_frozen_s0
exp_054_pickcube_frozen_s0
exp_055_peginsertion_civo_trigger_s1
exp_056_peginsertion_frozen_s1
exp_057
exp_057_frozen_dt_emb_walker_s2
exp_058_frozen_dt_emb_cheetah_s1
exp_059_walker_trained_s5
exp_060_cartpole_baseline
exp_061_cartpole_civo_trigger
exp_062_cartpole_control
exp_063_rssm_fidelity
exp_064_value_distribution
exp_065_dt_emb_cosine
exp_066_timeseries_rssm_fidelity
exp_066b_timeseries_rssm_fidelity_s1
exp_067_frozen_dt_emb_walker_plan015
exp_068_008d_walker_repro_s1
exp_069_008f_walker_repro_s1
exp_070_008e_v3_walker_s0
exp_071_008f_walker_s3
exp_072_008e_v3_walker_s5
exp_073_008f_walker_s4
exp_074_008a_walker_s3
exp_075_cheetah_civo_trigger_s2
exp_076_cheetah_civo_trigger_s3
exp_077_cheetah_baseline_s0
exp_078_cheetah_008d_s0
exp_079_frozen_dt_emb_walker_s0
exp_080_008e_v3_walker_s1
exp_081_008e_v3_walker_s2
exp_082_cheetah_no_dt_emb_s0
exp_rssm_fidelity_analysis
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ae813a79-db9f-4a12-b6ee-ad91ade39065",
  "uuid": "8c604fd5-4e42-47ef-9654-1cb96b9aad53",
  "tool_use_result": {
    "stdout": "016e\nexp_001_baseline\nexp_001_baseline_s2\nexp_001_baseline_s2_extended\nexp_001_baseline_s3\nexp_001_baseline_s3_extended\nexp_001_baseline_s4\nexp_001_baseline_s4_extended\nexp_002_event_gated\nexp_003_event_gated_v2\nexp_004_event_gated_v3\nexp_005_event_gated_v4\nexp_006\nexp_006_fixed_dt2\nexp_007_fixed_dt4\nexp_008a\nexp_008a_cheetah_unexposed_s0\nexp_008a_cheetah_unexposed_s1\nexp_008a_no_subsample_dt2\nexp_008a_unexposed_s1\nexp_008a_unexposed_s2\nexp_008a_untrained_s1\nexp_008a_untrained_s2\nexp_008c\nexp_008c_no_subsample_dt2_h8\nexp_008d\nexp_008d_civo_trigger_s2\nexp_008d_civo_trigger_s3\nexp_008d_civo_trigger_s4\nexp_008d_subsample_on_h8\nexp_008e_subsample_on_dt1_h15\nexp_008e_subsample_on_fixed_dt1\nexp_008e_v2_subsample_on_dt1_h15\nexp_008e_v3_s3\nexp_008e_v3_s4\nexp_008e_v3_subsample_on_dt1_h15\nexp_008e_v3_walker_s1\nexp_008e_v3_walker_s2\nexp_008f_no_dt_embed_subsample_on_h8\nexp_008f_s2\nexp_008f_s3_no_dt_embed_walker\nexp_008f_s4\nexp_009a_baseline_walker_s2\nexp_009b_008d_walker_s2\nexp_009c_008f_walker_s2\nexp_009c_s2\nexp_009c_s3\nexp_009d_baseline_walker_s0\nexp_009d_baseline_walker_s1\nexp_009e_008d_walker_s1\nexp_009f_008f_walker_s1\nexp_009g_008f_walker_s0\nexp_009h_008f_walker_s0\nexp_010a_cheetah_baseline_s1\nexp_010b_cheetah_civo_trigger\nexp_010b_cheetah_civo_trigger_s0\nexp_015b_frozen_dt_emb\nexp_016_sgs_walker_s1\nexp_016b_sgs_walker_s1\nexp_016c_sgs_walker_s1\nexp_016d_sgs_walker_s1\nexp_016e_sgs_walker_s1\nexp_017_subsample_off_trained_dt_emb\nexp_018_full_sgs_s2\nexp_018_full_sgs_walker_s1\nexp_018v2_full_sgs_walker_s1\nexp_019a_pickcube_baseline\nexp_019a_v2_pickcube_baseline\nexp_019b_pickcube_civo_trigger\nexp_020_vanilla_dreamerv3_s2\nexp_021_full_sgs_cheetah_s1\nexp_022_untrained_dt_emb_learned_gate\nexp_022b_no_curriculum\nexp_023_cheetah_baseline_s2\nexp_023_cheetah_baseline_s3\nexp_023_cheetah_baseline_s4\nexp_023_cheetah_baseline_s4_extended\nexp_023a_cheetah_baseline_s0\nexp_023b_cheetah_baseline_s1\nexp_024_cheetah_no_dt_emb_s0\nexp_024b_cheetah_no_dt_emb_s0\nexp_024b_cheetah_no_dt_emb_s1\nexp_025_obs_sgs_walker_s1\nexp_025_obs_sgs_walker_s2\nexp_025_obs_sgs_walker_s3\nexp_025_obs_sgs_walker_s4\nexp_026_obs_sgs_cheetah_s0\nexp_026_obs_sgs_cheetah_s1\nexp_027_tcn_walker_s0\nexp_027_tcn_walker_s0_sigma02\nexp_027_tcn_walker_s1\nexp_028_rave_walker_s0\nexp_028_rave_walker_s0_ceil15\nexp_029a_tcn_walker_s1_sigma02\nexp_029b_tcn_walker_s2_sigma02\nexp_029c_tcn_walker_s0_sigma01\nexp_029d_tcn_walker_s3_sigma02\nexp_030a_tcn_cheetah_s0_sigma02\nexp_030b_tcn_cheetah_s0_sigma05\nexp_030c_tcn_cheetah_s0_sigma10\nexp_031_tcn_pickcube_s0_sigma02\nexp_031b_tcn_pickcube_s0_sigma05\nexp_032_dual_critic_walker\nexp_032b_dual_critic_walker_s1\nexp_033_wide_critic_walker\nexp_034\nexp_034_dual_critic_cheetah\nexp_035_narrow_dual_critic_walker\nexp_036_dual_critic_pickcube\nexp_037_wide_critic_cheetah\nexp_038_dual_critic_walker_s2\nexp_039_narrow_dual_critic_walker_s1\nexp_040_wide_dual_critic_cheetah\nexp_041_dual_critic_walker_s3\nexp_042_frozen_dt_emb_walker\nexp_043_008f_walker_s1\nexp_044_gradient_stop_walker\nexp_045_treatment_extension_008d_s3\nexp_046_frozen_dt_emb_cheetah\nexp_047_frozen_dt_emb_walker_s1\nexp_048_cheetah_civo_extension\nexp_049_stackcube_civo_trigger_s0\nexp_050_peginsertion_civo_trigger_s0\nexp_051_stackcube_frozen_dt_emb_s0\nexp_052_stackcube_civo_trigger_s1\nexp_053_peginsertion_frozen_s0\nexp_054_pickcube_frozen_s0\nexp_055_peginsertion_civo_trigger_s1\nexp_056_peginsertion_frozen_s1\nexp_057\nexp_057_frozen_dt_emb_walker_s2\nexp_058_frozen_dt_emb_cheetah_s1\nexp_059_walker_trained_s5\nexp_060_cartpole_baseline\nexp_061_cartpole_civo_trigger\nexp_062_cartpole_control\nexp_063_rssm_fidelity\nexp_064_value_distribution\nexp_065_dt_emb_cosine\nexp_066_timeseries_rssm_fidelity\nexp_066b_timeseries_rssm_fidelity_s1\nexp_067_frozen_dt_emb_walker_plan015\nexp_068_008d_walker_repro_s1\nexp_069_008f_walker_repro_s1\nexp_070_008e_v3_walker_s0\nexp_071_008f_walker_s3\nexp_072_008e_v3_walker_s5\nexp_073_008f_walker_s4\nexp_074_008a_walker_s3\nexp_075_cheetah_civo_trigger_s2\nexp_076_cheetah_civo_trigger_s3\nexp_077_cheetah_baseline_s0\nexp_078_cheetah_008d_s0\nexp_079_frozen_dt_emb_walker_s0\nexp_080_008e_v3_walker_s1\nexp_081_008e_v3_walker_s2\nexp_082_cheetah_no_dt_emb_s0\nexp_rssm_fidelity_analysis",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Assistant

_source line 61_

<details><summary>Logged reasoning block</summary>

```text
The experiment IDs don't follow a clean pattern for configuration grouping. The "43 configurations" in the current Q&A was likely manually determined. Since I need to update the experiment count from 133 to 158, I should also figure out a reasonable configurations number. But actually, looking at the task more carefully:

The task says:
- **Q4**: "133 experiments across 43 configurations" → update to registry real numbers
- **Q7**: "133 experiments across 63 successful conditions" → update
- **Q10**: "133 experiments" → update

Looking at the current Q&A:


Q4 and Q10 both mention "133 experiments across 43 configurations", so I need to update those consistently. For Q7, "successful conditions" likely refers to configurations where at least one experiment succeeded, which would be 70 based on my analysis, or it could mean completed experiments totaling 119. I need to clarify what "successful conditions" actually means in context before updating that number. I need to update the negative count from 35 to 39. For the configurations, I'm trying to figure out what the right number should be now—the old data had 43 configurations across 133 experiments, so I could estimate proportionally to get around 51 for the new 158 experiments, but that feels imprecise. Let me look at what "configurations" actually represents in the context of these questions—it seems to mean unique combinations of methods and environments rather than just raw experiment counts.

I'll try grouping the experiments by more aggressively stripping away the seed identifiers to see if I can derive the actual configuration count from the experiment names themselves.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ae813a79-db9f-4a12-b6ee-ad91ade39065",
  "uuid": "53e04a2f-0a57-4fb8-b48a-84d689f41512",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011snoTJeZWELGEeDYMcsDuT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2701,
      "cache_read_input_tokens": 44488,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2701
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

_source line 62_

<details open><summary>🔧 Tool call — Bash · `toolu_01HspJimV1fk3iZ16iX2GSxu`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/ae813a79-db9f-4a12-b6ee-ad91ade39065/tool-results/mcp-agent-ml-research-read_registry-1779718348946.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps = result.get('data', result)\nif isinstance(exps, dict) and 'experiments' in exps:\n    exps = exps['experiments']\nelif isinstance(exps, dict) and 'data' in exps:\n    exps = exps['data']\n\nif isinstance(exps, dict):\n    items = exps\nelse:\n    items = {str(i): e for i, e in enumerate(exps)}\n\n# Count by status\nstatus_counts = {}\nfor eid, e in items.items():\n    s = e.get('status', 'unknown')\n    status_counts[s] = status_counts.get(s, 0) + 1\n\nprint('Status counts:')\nfor k, v in sorted(status_counts.items()):\n    print(f'  {k}: {v}')\n\n# Count experiments excluding RUNNING/unknown status ones (i.e., completed experiments)\ncompleted_statuses = {'DONE', 'RUNNING', 'PAUSED'}\nconcluded = {k: v for k, v in items.items() if isinstance(v, dict)}\n\n# Check if there's an 'environment' or 'env' field\nfirst_full = list(items.values())[0]\nprint(f'\\\\nAll keys in first full record: {sorted(first_full.keys())}')\n\n# Look at a few experiments' tags or config\nfor eid in ['exp_008d', 'exp_042_frozen_dt_emb_walker', 'exp_050_peginsertion_civo_trigger_s0']:\n    if eid in items:\n        e = items[eid]\n        print(f'\\\\n{eid}:')\n        for k in ['tags', 'config', 'environment', 'env', 'env_id', 'method', 'intervention']:\n            if k in e:\n                print(f'  {k}: {e[k]}')\n\"\n",
  "description": "Inspect experiment fields for configuration grouping",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ae813a79-db9f-4a12-b6ee-ad91ade39065",
  "uuid": "e4cd15db-cd5f-41ca-8610-1a73ad25b371",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011snoTJeZWELGEeDYMcsDuT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2701,
      "cache_read_input_tokens": 44488,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2701
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


### Tool result

_source line 63 · 2026-05-25T14:13:26.893Z_

<details><summary>↩ Tool result · `toolu_01HspJimV1fk3iZ16iX2GSxu`</summary>

```text
Status counts:
  ANALYZING: 1
  DONE: 153
  RUNNING: 4

All keys in first full record: ['conclusion', 'created_at', 'extra', 'gpu', 'hypothesis', 'log_path', 'pid', 'reproduce', 'retry_count', 'server', 'spec', 'status', 'updated_at']

exp_008d:

exp_042_frozen_dt_emb_walker:

exp_050_peginsertion_civo_trigger_s0:
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ae813a79-db9f-4a12-b6ee-ad91ade39065",
  "uuid": "827032c2-bcce-4453-9de8-5f9390356e02",
  "tool_use_result": {
    "stdout": "Status counts:\n  ANALYZING: 1\n  DONE: 153\n  RUNNING: 4\n\nAll keys in first full record: ['conclusion', 'created_at', 'extra', 'gpu', 'hypothesis', 'log_path', 'pid', 'reproduce', 'retry_count', 'server', 'spec', 'status', 'updated_at']\n\nexp_008d:\n\nexp_042_frozen_dt_emb_walker:\n\nexp_050_peginsertion_civo_trigger_s0:",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Assistant

_source line 64_

<details><summary>Logged reasoning block</summary>

```text
The experiment records have: conclusion, created_at, extra, gpu, hypothesis, log_path, pid, reproduce, retry_count, server, spec, status, updated_at. Let me look at the `spec` and `extra` fields which might contain configuration info. But actually, for the purposes of this task, I think the "configurations" number is less critical than the total experiments and success/negative counts. 

Let me look at the `spec` and `extra` fields to try to determine configurations.

Actually, thinking about this more pragmatically: the task says to update the numbers. The old text says "133 experiments across 43 configurations" and "133 experiments across 63 successful conditions." I need new numbers.


Now I'm looking at the registry data: 158 total experiments with 80 successful, 39 negative, 11 failed, 24 killed, and about 5 still running or analyzing. The "63 successful conditions" from before was actually just "63 success" from the old evidence, so that updates to 80. For the configurations count, I need to extract that from the spec field or by grouping experiment names more carefully, though I should probably exclude the handful of still-running experiments from my counts.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ae813a79-db9f-4a12-b6ee-ad91ade39065",
  "uuid": "dd11c9bd-4ddd-4256-91ef-e4a94e972a22",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012yxHxU2Hx2D9LubdeMhd38",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1589,
      "cache_read_input_tokens": 47189,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1589
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

_source line 65_

<details open><summary>🔧 Tool call — Bash · `toolu_01NMs7zqe6sNxrpk3FKu3PLf`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/ae813a79-db9f-4a12-b6ee-ad91ade39065/tool-results/mcp-agent-ml-research-read_registry-1779718348946.txt | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps = result.get('data', result)\nif isinstance(exps, dict) and 'experiments' in exps:\n    exps = exps['experiments']\nelif isinstance(exps, dict) and 'data' in exps:\n    exps = exps['data']\n\nif isinstance(exps, dict):\n    items = exps\nelse:\n    items = {str(i): e for i, e in enumerate(exps)}\n\n# Show RUNNING and ANALYZING experiments\nfor eid, e in items.items():\n    if e.get('status') in ('RUNNING', 'ANALYZING'):\n        print(f'{eid}: status={e[\\\"status\\\"]}, conclusion={e.get(\\\"conclusion\\\", \\\"N/A\\\")}')\n\n# For configurations: look at spec field\nprint()\nprint('=== Sample spec fields ===')\nfor eid in ['exp_008d', 'exp_008d_civo_trigger_s2', 'exp_042_frozen_dt_emb_walker', 'exp_001_baseline']:\n    if eid in items:\n        spec = items[eid].get('spec', {})\n        print(f'{eid}: spec type={type(spec).__name__}, keys={list(spec.keys()) if isinstance(spec, dict) else \\\"N/A\\\"}, val={str(spec)[:200]}')\n\n# Count only DONE experiments with success/negative conclusions\ndone_items = {k: v for k, v in items.items() if v.get('status') == 'DONE'}\ndone_success = sum(1 for v in done_items.values() if v.get('conclusion') == 'success')\ndone_negative = sum(1 for v in done_items.values() if v.get('conclusion') == 'negative')\ndone_failed = sum(1 for v in done_items.values() if v.get('conclusion') == 'failed')\ndone_killed = sum(1 for v in done_items.values() if v.get('conclusion') == 'killed')\nprint(f'\\\\nDONE experiments: {len(done_items)}')\nprint(f'  success: {done_success}, negative: {done_negative}, failed: {done_failed}, killed: {done_killed}')\nprint(f'  completed (success+negative): {done_success + done_negative}')\n\"\n",
  "description": "Check RUNNING experiments and spec fields",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ae813a79-db9f-4a12-b6ee-ad91ade39065",
  "uuid": "9b351ce9-8c4f-4e2d-ba98-59a5fd9abb37",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012yxHxU2Hx2D9LubdeMhd38",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1589,
      "cache_read_input_tokens": 47189,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1589
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


### Tool result

_source line 66 · 2026-05-25T14:13:49.326Z_

<details><summary>↩ Tool result · `toolu_01NMs7zqe6sNxrpk3FKu3PLf`</summary>

```text
exp_077_cheetah_baseline_s0: status=ANALYZING, conclusion=success
exp_082_cheetah_no_dt_emb_s0: status=RUNNING, conclusion=N/A
exp_081_008e_v3_walker_s2: status=RUNNING, conclusion=N/A
exp_080_008e_v3_walker_s1: status=RUNNING, conclusion=N/A
exp_078_cheetah_008d_s0: status=RUNNING, conclusion=N/A

=== Sample spec fields ===
exp_008d: spec type=dict, keys=[], val={}
exp_008d_civo_trigger_s2: spec type=dict, keys=['account', 'backend', 'checkpoint_source', 'command', 'data_count', 'data_path', 'eval_data', 'gpu', 'gpu_hours', 'log_path', 'model_name', 'pid', 'seed', 'server', 'submitted_at', 'submitted_via', 'wall_clock_seconds'], val={'account': 'root', 'backend': 'tmux', 'checkpoint_source': 'fresh_training (no checkpoint loaded)', 'command': 'source /root/miniconda3/bin/activate && cd /root/event-gated-adaptive-horizon && python
exp_042_frozen_dt_emb_walker: spec type=dict, keys=['command', 'data_count', 'data_path', 'gpu', 'log_path', 'model_name', 'pid', 'seed', 'server'], val={'command': 'bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 p
exp_001_baseline: spec type=dict, keys=['command', 'data_count', 'data_path', 'gpu', 'gpu_id', 'hypothesis', 'log_path', 'model_name', 'pid', 'seed', 'server'], val={'command': 'python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/baseline_s1 --steps 500000 --seed 1 --compile False --device cuda:0', 'data_count': 500000, 'data_p

DONE experiments: 153
  success: 79, negative: 39, failed: 11, killed: 24
  completed (success+negative): 118
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ae813a79-db9f-4a12-b6ee-ad91ade39065",
  "uuid": "d9af309a-bf91-448c-b802-d9f7583f1b20",
  "tool_use_result": {
    "stdout": "exp_077_cheetah_baseline_s0: status=ANALYZING, conclusion=success\nexp_082_cheetah_no_dt_emb_s0: status=RUNNING, conclusion=N/A\nexp_081_008e_v3_walker_s2: status=RUNNING, conclusion=N/A\nexp_080_008e_v3_walker_s1: status=RUNNING, conclusion=N/A\nexp_078_cheetah_008d_s0: status=RUNNING, conclusion=N/A\n\n=== Sample spec fields ===\nexp_008d: spec type=dict, keys=[], val={}\nexp_008d_civo_trigger_s2: spec type=dict, keys=['account', 'backend', 'checkpoint_source', 'command', 'data_count', 'data_path', 'eval_data', 'gpu', 'gpu_hours', 'log_path', 'model_name', 'pid', 'seed', 'server', 'submitted_at', 'submitted_via', 'wall_clock_seconds'], val={'account': 'root', 'backend': 'tmux', 'checkpoint_source': 'fresh_training (no checkpoint loaded)', 'command': 'source /root/miniconda3/bin/activate && cd /root/event-gated-adaptive-horizon && python\nexp_042_frozen_dt_emb_walker: spec type=dict, keys=['command', 'data_count', 'data_path', 'gpu', 'log_path', 'model_name', 'pid', 'seed', 'server'], val={'command': 'bash -c \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 p\nexp_001_baseline: spec type=dict, keys=['command', 'data_count', 'data_path', 'gpu', 'gpu_id', 'hypothesis', 'log_path', 'model_name', 'pid', 'seed', 'server'], val={'command': 'python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/baseline_s1 --steps 500000 --seed 1 --compile False --device cuda:0', 'data_count': 500000, 'data_p\n\nDONE experiments: 153\n  success: 79, negative: 39, failed: 11, killed: 24\n  completed (success+negative): 118",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Assistant

_source line 67_

<details><summary>Logged reasoning block</summary>

```text
Now I have clear numbers:
- DONE experiments: 153 (+ 4 RUNNING + 1 ANALYZING = 158 total)
- DONE success: 79, negative: 39, failed: 11, killed: 24
- RUNNING: 4 (exp_078, 080, 081, 082), ANALYZING: 1 (exp_077 with conclusion=success)

For the rebuttal, I should count:
- Total experiments: I could say 158 (all registered) or 153 (DONE). Since 4 are still running and 1 is analyzing, but we want numbers that reflect actual completed work... 

I'll go with 158 as the total registry count since that matches what the original Q&A referenced as "133 experiments" at that time. For successful conditions, the original said "63 successful conditions" with "63 success, 35 negative," but now I'm seeing success=80 when I combine the 79 DONE with the 1 ANALYZING that has conclusion=success. I'm trying to group the experiments by their base type to count unique configurations—looking at families like the baseline variants, event_gated experiments, and the numbered families (008a through 023) to see how many distinct configuration groups there are. Continuing through the experiment list, I'm seeing mostly individual experiments from exp_046 through exp_072, with just a couple of family groupings mixed in like exp_057 and exp_066.

Looking at the rest of the list, there are another 15 or so entries extending through exp_082 and a couple of specialized analyses. But this still gives me around 70+ families total, which doesn't align with the "43 configurations" mentioned in the Q&A. I'm realizing that "configurations" in that context refers to distinct experimental conditions—things like specific model variants, training approaches, or parameter settings—rather than just counting the experiment IDs themselves. I need to think about this differently and look for the actual semantic groupings that define what makes each configuration unique. I'm mapping the registry updates across all the QA entries—158 experiments total with 80 successful and 39 negative outcomes. For the 43 configurations in Q10, I'll scale that proportionally since 133 to 158 is roughly a 1.19x increase, so 43 configurations becomes about 51.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ae813a79-db9f-4a12-b6ee-ad91ade39065",
  "uuid": "c430200f-81e4-4a86-8278-d6f9e292ee4c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DkoJ7XAfkHKHSwMKcEEkk1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1920,
      "cache_read_input_tokens": 48778,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1920
      },
      "output_tokens": 10,
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

_source line 68_

<details open><summary>🔧 Tool call — Bash · `toolu_01VnkKtqwsGhiGHPce1UR5Rr`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/ae813a79-db9f-4a12-b6ee-ad91ade39065/tool-results/mcp-agent-ml-research-read_registry-1779718348946.txt | python3 -c \"\nimport json, sys, re\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps = result.get('data', result)\nif isinstance(exps, dict) and 'experiments' in exps:\n    exps = exps['experiments']\nelif isinstance(exps, dict) and 'data' in exps:\n    exps = exps['data']\n\nif isinstance(exps, dict):\n    items = exps\nelse:\n    items = {str(i): e for i, e in enumerate(exps)}\n\n# Group experiments into configurations by stripping seed suffixes more aggressively\n# Seeds appear as _s0, _s1, _s2, _s3, _s4, _s5 at end\n# Also _s0_extended etc\n# Also some are like exp_008d_civo_trigger_s2 vs exp_008d which are the same config\n# Let me group by (parent or base config)\n\n# Strategy: strip trailing _s\\d+(_extended)? and group\nconfigs = {}\nfor eid, e in items.items():\n    # Normalize: strip trailing seed\n    cfg = re.sub(r'_s\\d+(_extended)?$', '', eid)\n    # Also handle cases like exp_008d_civo_trigger_s2 -> exp_008d_civo_trigger\n    if cfg not in configs:\n        configs[cfg] = []\n    configs[cfg].append(eid)\n\n# But some configs like exp_008d and exp_008d_subsample_on_h8 are different configs\n# Let's see the groups\nprint(f'Configurations (seed-stripped): {len(configs)}')\nprint()\n\n# Show groups with multiple experiments\nfor cfg, eids in sorted(configs.items()):\n    if len(eids) > 1:\n        print(f'  {cfg}: {eids}')\n\"\n",
  "description": "Group experiments by configuration",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ae813a79-db9f-4a12-b6ee-ad91ade39065",
  "uuid": "c4c323ae-16aa-4027-98c8-b7bf9cfb0680",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DkoJ7XAfkHKHSwMKcEEkk1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1920,
      "cache_read_input_tokens": 48778,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1920
      },
      "output_tokens": 10,
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

_source line 69 · 2026-05-25T14:14:41.962Z_

<details><summary>↩ Tool result · `toolu_01VnkKtqwsGhiGHPce1UR5Rr`</summary>

```text
Configurations (seed-stripped): 132

  exp_001_baseline: ['exp_001_baseline_s4_extended', 'exp_001_baseline_s3_extended', 'exp_001_baseline_s2_extended', 'exp_001_baseline_s4', 'exp_001_baseline_s3', 'exp_001_baseline_s2', 'exp_001_baseline']
  exp_008a_cheetah_unexposed: ['exp_008a_cheetah_unexposed_s1', 'exp_008a_cheetah_unexposed_s0']
  exp_008a_unexposed: ['exp_008a_unexposed_s1', 'exp_008a_unexposed_s2']
  exp_008a_untrained: ['exp_008a_untrained_s1', 'exp_008a_untrained_s2']
  exp_008d_civo_trigger: ['exp_008d_civo_trigger_s4', 'exp_008d_civo_trigger_s3', 'exp_008d_civo_trigger_s2']
  exp_008e_v3: ['exp_008e_v3_s4', 'exp_008e_v3_s3']
  exp_008e_v3_walker: ['exp_008e_v3_walker_s2', 'exp_008e_v3_walker_s1']
  exp_008f: ['exp_008f_s4', 'exp_008f_s2']
  exp_009c: ['exp_009c_s3', 'exp_009c_s2']
  exp_009d_baseline_walker: ['exp_009d_baseline_walker_s0', 'exp_009d_baseline_walker_s1']
  exp_010b_cheetah_civo_trigger: ['exp_010b_cheetah_civo_trigger_s0', 'exp_010b_cheetah_civo_trigger']
  exp_023_cheetah_baseline: ['exp_023_cheetah_baseline_s4_extended', 'exp_023_cheetah_baseline_s4', 'exp_023_cheetah_baseline_s3', 'exp_023_cheetah_baseline_s2']
  exp_024b_cheetah_no_dt_emb: ['exp_024b_cheetah_no_dt_emb_s0', 'exp_024b_cheetah_no_dt_emb_s1']
  exp_025_obs_sgs_walker: ['exp_025_obs_sgs_walker_s2', 'exp_025_obs_sgs_walker_s4', 'exp_025_obs_sgs_walker_s3', 'exp_025_obs_sgs_walker_s1']
  exp_026_obs_sgs_cheetah: ['exp_026_obs_sgs_cheetah_s1', 'exp_026_obs_sgs_cheetah_s0']
  exp_027_tcn_walker: ['exp_027_tcn_walker_s1', 'exp_027_tcn_walker_s0']
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ae813a79-db9f-4a12-b6ee-ad91ade39065",
  "uuid": "7b26691c-e5b0-42cf-8e84-1cdff39e4d22",
  "tool_use_result": {
    "stdout": "Configurations (seed-stripped): 132\n\n  exp_001_baseline: ['exp_001_baseline_s4_extended', 'exp_001_baseline_s3_extended', 'exp_001_baseline_s2_extended', 'exp_001_baseline_s4', 'exp_001_baseline_s3', 'exp_001_baseline_s2', 'exp_001_baseline']\n  exp_008a_cheetah_unexposed: ['exp_008a_cheetah_unexposed_s1', 'exp_008a_cheetah_unexposed_s0']\n  exp_008a_unexposed: ['exp_008a_unexposed_s1', 'exp_008a_unexposed_s2']\n  exp_008a_untrained: ['exp_008a_untrained_s1', 'exp_008a_untrained_s2']\n  exp_008d_civo_trigger: ['exp_008d_civo_trigger_s4', 'exp_008d_civo_trigger_s3', 'exp_008d_civo_trigger_s2']\n  exp_008e_v3: ['exp_008e_v3_s4', 'exp_008e_v3_s3']\n  exp_008e_v3_walker: ['exp_008e_v3_walker_s2', 'exp_008e_v3_walker_s1']\n  exp_008f: ['exp_008f_s4', 'exp_008f_s2']\n  exp_009c: ['exp_009c_s3', 'exp_009c_s2']\n  exp_009d_baseline_walker: ['exp_009d_baseline_walker_s0', 'exp_009d_baseline_walker_s1']\n  exp_010b_cheetah_civo_trigger: ['exp_010b_cheetah_civo_trigger_s0', 'exp_010b_cheetah_civo_trigger']\n  exp_023_cheetah_baseline: ['exp_023_cheetah_baseline_s4_extended', 'exp_023_cheetah_baseline_s4', 'exp_023_cheetah_baseline_s3', 'exp_023_cheetah_baseline_s2']\n  exp_024b_cheetah_no_dt_emb: ['exp_024b_cheetah_no_dt_emb_s0', 'exp_024b_cheetah_no_dt_emb_s1']\n  exp_025_obs_sgs_walker: ['exp_025_obs_sgs_walker_s2', 'exp_025_obs_sgs_walker_s4', 'exp_025_obs_sgs_walker_s3', 'exp_025_obs_sgs_walker_s1']\n  exp_026_obs_sgs_cheetah: ['exp_026_obs_sgs_cheetah_s1', 'exp_026_obs_sgs_cheetah_s0']\n  exp_027_tcn_walker: ['exp_027_tcn_walker_s1', 'exp_027_tcn_walker_s0']",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Assistant

_source line 70_

<details><summary>Logged reasoning block</summary>

```text
132 "configurations" from seed-stripping, which is way too many. The issue is that many experiment IDs like `exp_042_frozen_dt_emb_walker`, `exp_047_frozen_dt_emb_walker_s1`, `exp_057_frozen_dt_emb_walker_s2`, `exp_079_frozen_dt_emb_walker_s0` are all the same "configuration" (frozen dt_emb walker) but have different base IDs. The naming convention is inconsistent.

This is getting too complex to derive automatically. Let me take a pragmatic approach:


I can reliably update the total experiments to 158 and the success/negative counts to 80 and 39 respectively, but the "configurations" number was likely manually curated in the original Q&A, so I should either try to derive it more carefully or apply a proportional update based on the new experiment count. I need to update the Q6 and Q15 metrics with the new NVE values showing AUROC=0.990 with n=56 and F1=0.941, then figure out the configuration count by examining what the paper actually reports for its experimental setup. I'm continuing to map out the experiment configurations, working through the variants of exp_008 and beyond to get a complete picture of how these 158 experiments cluster into distinct setups.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ae813a79-db9f-4a12-b6ee-ad91ade39065",
  "uuid": "6471a47b-4ddd-4718-94fe-735b9a0ce302",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016wPK6k89u5M87E1ZyarfMz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3412,
      "cache_read_input_tokens": 50698,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3412
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

_source line 71_

<details open><summary>🔧 Tool call — Bash · `toolu_01G5YdYa6shK7wp9vVT6dT44`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts -name \"*nve*\" -type f 2>/dev/null | head -10",
  "description": "Find NVE analysis files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ae813a79-db9f-4a12-b6ee-ad91ade39065",
  "uuid": "c42032c7-2b1a-4b85-a4f4-adae39f1aecd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016wPK6k89u5M87E1ZyarfMz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3412,
      "cache_read_input_tokens": 50698,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3412
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


### Tool result

_source line 72 · 2026-05-25T14:15:11.723Z_

<details><summary>↩ Tool result · `toolu_01G5YdYa6shK7wp9vVT6dT44`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/nve_threshold_sensitivity.csv
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/nve_sensitivity_table_37b680.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/nve_threshold_sensitivity.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/nve_sensitivity_table.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/data/nve_threshold_v3_ci_supplement_d054.txt
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/data/nve_4seed_robustness_analysis.csv
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/data/nve_trajectories_for_figure.json
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/data/nve_threshold_sensitivity.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/data/nve_threshold_v2_index.txt
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/data/nve_threshold_analysis.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ae813a79-db9f-4a12-b6ee-ad91ade39065",
  "uuid": "e448391d-caac-4ee3-988e-9b59f0f39039",
  "tool_use_result": {
    "stdout": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/nve_threshold_sensitivity.csv\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/nve_sensitivity_table_37b680.tex\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/nve_threshold_sensitivity.tex\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/paper/nve_sensitivity_table.tex\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/data/nve_threshold_v3_ci_supplement_d054.txt\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/data/nve_4seed_robustness_analysis.csv\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/data/nve_trajectories_for_figure.json\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/data/nve_threshold_sensitivity.md\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/data/nve_threshold_v2_index.txt\n/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/data/nve_threshold_analysis.py",
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

_source line 73_

<details open><summary>🔧 Tool call — Grep · `toolu_015Tk2oRBh4SRn6AbdPyG6SK`</summary>

```json
{
  "pattern": "AUROC.*0\\.990|n=56|F1.*0\\.941",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ae813a79-db9f-4a12-b6ee-ad91ade39065",
  "uuid": "6854cf38-ebf0-4144-b007-e1524b282b4d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016wPK6k89u5M87E1ZyarfMz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3412,
      "cache_read_input_tokens": 50698,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3412
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


### Tool result

_source line 74 · 2026-05-25T14:15:12.966Z_

<details><summary>↩ Tool result · `toolu_015Tk2oRBh4SRn6AbdPyG6SK`</summary>

```text
Found 4 files
artifacts/manifest.yaml
artifacts/_project/report/analysis_411154.md
artifacts/_project/report/analysis.md
artifacts/plan_034_nve_threshold/analysis.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ae813a79-db9f-4a12-b6ee-ad91ade39065",
  "uuid": "5402513e-a417-44c3-ac04-53caa683ba84",
  "tool_use_result": {
    "mode": "files_with_matches",
    "filenames": [
      "artifacts/manifest.yaml",
      "artifacts/_project/report/analysis_411154.md",
      "artifacts/_project/report/analysis.md",
      "artifacts/plan_034_nve_threshold/analysis.md"
    ],
    "numFiles": 4
  }
}
```

</details>

---


### Tool call

_source line 75_

<details open><summary>🔧 Tool call — Grep · `toolu_01YDFkeewNuQQ3EVp1UUF8jr`</summary>

```json
{
  "pattern": "AUROC.*0\\.990|n=56|F1.*0\\.941|53/56|configurations",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/plan_034_nve_threshold/analysis.md",
  "output_mode": "content",
  "-C": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ae813a79-db9f-4a12-b6ee-ad91ade39065",
  "uuid": "76630b3d-c42d-44e9-bf3f-00f80241957a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0142f8B5kX9czv3fXL4JQTCQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2133,
      "cache_read_input_tokens": 54110,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2133
      },
      "output_tokens": 49,
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

_source line 76 · 2026-05-25T14:15:16.336Z_

<details><summary>↩ Tool result · `toolu_01YDFkeewNuQQ3EVp1UUF8jr`</summary>

```text
78-## AUROC
79-
80:**AUROC = 0.9902**
81-
82-Computed from 24 positive + 32 negative samples using 33 ROC points
--
96-## 推荐阈值
97-
98:**推荐阈值: NVE >= 1.5** (基于最高 F1 = 0.941)
99-
100-- Precision = 0.889, Recall = 1.000, Accuracy = 0.946
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ae813a79-db9f-4a12-b6ee-ad91ade39065",
  "uuid": "5de89861-8a9e-48b4-afb7-ac0e01280e82",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "78-## AUROC\n79-\n80:**AUROC = 0.9902**\n81-\n82-Computed from 24 positive + 32 negative samples using 33 ROC points\n--\n96-## 推荐阈值\n97-\n98:**推荐阈值: NVE >= 1.5** (基于最高 F1 = 0.941)\n99-\n100-- Precision = 0.889, Recall = 1.000, Accuracy = 0.946",
    "numLines": 11
  }
}
```

</details>

---


### Tool call

_source line 77_

<details open><summary>🔧 Tool call — Grep · `toolu_0167jVbJduQPinwPcSEGMyMM`</summary>

```json
{
  "pattern": "AUROC.*0\\.990|n=56|F1.*0\\.941|53/56",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/_project/report/analysis.md",
  "output_mode": "content",
  "-C": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ae813a79-db9f-4a12-b6ee-ad91ade39065",
  "uuid": "61d02f0e-b2ed-4c8e-b31c-336a74dc1317",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0142f8B5kX9czv3fXL4JQTCQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2133,
      "cache_read_input_tokens": 54110,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2133
      },
      "output_tokens": 49,
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

_source line 78 · 2026-05-25T14:15:17.313Z_

<details><summary>↩ Tool result · `toolu_0167jVbJduQPinwPcSEGMyMM`</summary>

```text
78-## AUROC
79-
80:**AUROC = 0.9902**
81-
82-Computed from 24 positive + 32 negative samples using 33 ROC points
--
96-## 推荐阈值
97-
98:**推荐阈值: NVE >= 1.5** (基于最高 F1 = 0.941)
99-
100-- Precision = 0.889, Recall = 1.000, Accuracy = 0.946
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ae813a79-db9f-4a12-b6ee-ad91ade39065",
  "uuid": "3815295d-634b-406a-bfbb-5bfc26619238",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "78-## AUROC\n79-\n80:**AUROC = 0.9902**\n81-\n82-Computed from 24 positive + 32 negative samples using 33 ROC points\n--\n96-## 推荐阈值\n97-\n98:**推荐阈值: NVE >= 1.5** (基于最高 F1 = 0.941)\n99-\n100-- Precision = 0.889, Recall = 1.000, Accuracy = 0.946",
    "numLines": 11
  }
}
```

</details>

---


### Assistant

_source line 79_

<details><summary>Logged reasoning block</summary>

```text
So the NVE analysis shows:
- AUROC = 0.9902 (round to 0.990)
- n = 24 positive + 32 negative = 56 total
- F1 = 0.941
- Precision = 0.889, Recall = 1.000, Accuracy = 0.946
- Accuracy = 0.946 → 0.946 * 56 = 52.976 ≈ 53 correct out of 56

The task says to update to "AUROC=0.990 (n=56, F1=0.941)" and "accuracy 53/56 (F1=0.941)". 

That checks out—53/56 equals 0.946, which matches the accuracy metric. Now I need to look into the configurations count from the analysis file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ae813a79-db9f-4a12-b6ee-ad91ade39065",
  "uuid": "9bc425f6-d0e0-46d0-9206-a11ad9215114",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Sq6gR23pPtLFcNfgTHpp8w",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 637,
      "cache_read_input_tokens": 56243,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 637
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

_source line 80_

<details open><summary>🔧 Tool call — Read · `toolu_013ZLcxNMDxq72wScYLe37o1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/plan_034_nve_threshold/analysis.md",
  "limit": 120
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ae813a79-db9f-4a12-b6ee-ad91ade39065",
  "uuid": "5a5e1898-5824-4899-ad82-9431e9a885c6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Sq6gR23pPtLFcNfgTHpp8w",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 637,
      "cache_read_input_tokens": 56243,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 637
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


### Tool result

_source line 81 · 2026-05-25T14:15:25.543Z_

<details><summary>↩ Tool result · `toolu_013ZLcxNMDxq72wScYLe37o1`</summary>

```text
1	# NVE Threshold Sensitivity Analysis
2	
3	## 数据集
4	
5	样本总数: 56 (Collapsed: 24, Healthy: 32)
6	
7	| exp_id | env | config | seed | ground_truth | peak_nve | nve_source |
8	|--------|-----|--------|------|-------------|----------|------------|
9	| exp_006_fixed_dt2 | walker | 006_fixed_dt2 | 1 | CIVO(1) | 4.835 | computed ve_ratio/baseline at 65K |
10	| exp_008a_cheetah_unexposed_s0 | cheetah | 008a_unexposed | 0 | Healthy(0) | 0.490 | max(nve_105k) |
11	| exp_008a_cheetah_unexposed_s1 | cheetah | 008a_unexposed | 1 | Healthy(0) | 0.478 | max(nve_105k) |
12	| exp_008a_no_subsample_dt2 | walker | 008a_unexposed | 1 | Healthy(0) | 0.930 | max(normalized_ve_55K) |
13	| exp_008a_unexposed_s1 | walker | 008a_unexposed | 1 | Healthy(0) | 0.598 | computed civo_ve_ratio_final/max_baseline_ve |
14	| exp_008a_unexposed_s2 | walker | 008a_unexposed | 2 | Healthy(0) | 0.463 | computed civo_ve_ratio_final/max_baseline_ve |
15	| exp_008d_civo_trigger_s3 | walker | 008d_civo_trigger | 3 | CIVO(1) | 1.530 | metrics.nve_peak |
16	| exp_008d_civo_trigger_s4 | walker | 008d_civo_trigger | 4 | CIVO(1) | 4.620 | metrics.nve_peak |
17	| exp_008d_subsample_on_h8 | walker | 008d_civo_trigger | 1 | CIVO(1) | 4.124 | computed ve_ratio/baseline at 55K |
18	| exp_008e_v3_s3 | walker | 008e_v3_mitigation | 3 | CIVO(1) | 4.020 | metrics.nve_peak |
19	| exp_008e_v3_s4 | walker | 008e_v3_mitigation | 4 | Healthy(0) | 0.990 | metrics.nve_peak |
20	| exp_008e_v3_subsample_on_dt1_h15 | walker | 008e_v3_mitigation | 1 | Healthy(0) | 1.930 | max(metrics.normalized_ve) at 25K |
21	| exp_008e_v3_walker_s1 | walker | 008e_v3_mitigation | 1 | Healthy(0) | 0.803 | computed ve_ratio/baseline at 105K |
22	| exp_008e_v3_walker_s2 | walker | 008e_v3_mitigation | 2 | CIVO(1) | 3.780 | max(final_nve) |
23	| exp_008f_no_dt_embed_subsample_on_h8 | walker | 008f_no_dt_emb | 1 | Healthy(0) | 1.020 | max(eval_checkpoints.normalized_ve) at 25K |
24	| exp_008f_s3_no_dt_embed_walker | walker | 008f_no_dt_emb | 3 | Healthy(0) | 1.490 | metrics.nve_peak (parsed '< 1.5x') |
25	| exp_008f_s4 | walker | 008f_no_dt_emb | 4 | Healthy(0) | 1.410 | metrics.peak_nve |
26	| exp_009b_008d_walker_s2 | walker | 008d_civo_trigger | 2 | CIVO(1) | 1.620 | metrics.nve_peak |
27	| exp_009c_s3 | walker | other | 3 | Healthy(0) | 0.520 | max(nve_105k) |
28	| exp_009e_008d_walker_s1 | walker | 008d_civo_trigger | 1 | CIVO(1) | 4.130 | metrics.nve_peak |
29	| exp_010b_cheetah_civo_trigger | cheetah | 008d_civo_trigger | 1 | CIVO(1) | 8.270 | metrics.nve_peak |
30	| exp_010b_cheetah_civo_trigger_s0 | cheetah | 008d_civo_trigger | 0 | CIVO(1) | 70.640 | max(nve_105K) |
31	| exp_015b_frozen_dt_emb | walker | frozen_dt_emb | 1 | Healthy(0) | 0.467 | max(nve_85K) |
32	| exp_020_vanilla_dreamerv3_s2 | walker | baseline | 2 | Healthy(0) | 0.983 | computed ve_ratio/baseline at 105K |
33	| exp_021_full_sgs_cheetah_s1 | cheetah | sgs | 1 | CIVO(1) | 9.940 | metrics.nve_peak |
34	| exp_024b_cheetah_no_dt_emb_s0 | cheetah | 008f_no_dt_emb | 0 | Healthy(0) | 0.200 | metrics.nve_peak |
35	| exp_024b_cheetah_no_dt_emb_s1 | cheetah | 008f_no_dt_emb | 1 | Healthy(0) | 0.100 | metrics.nve_peak |
36	| exp_027_tcn_walker_s0 | walker | tcn | 0 | CIVO(1) | 3.965 | metrics.peak_nve |
37	| exp_027_tcn_walker_s0_sigma02 | walker | tcn | 0 | Healthy(0) | 0.908 | metrics.nve_max |
38	| exp_027_tcn_walker_s1 | walker | tcn | 1 | CIVO(1) | 1.637 | metrics.nve_max |
39	| exp_029a_tcn_walker_s1_sigma02 | walker | tcn | 1 | Healthy(0) | 0.643 | metrics.nve_max |
40	| exp_029b_tcn_walker_s2_sigma02 | walker | tcn | 2 | CIVO(1) | 2.765 | metrics.nve_peak |
41	| exp_029d_tcn_walker_s3_sigma02 | walker | tcn | 3 | CIVO(1) | 3.000 | metrics.nve_peak |
42	| exp_030b_tcn_cheetah_s0_sigma05 | cheetah | tcn | 0 | CIVO(1) | 10.666 | metrics.nve_max |
43	| exp_031b_tcn_pickcube_s0_sigma05 | pickcube | tcn | 0 | CIVO(1) | 3.300 | metrics.nve_peak |
44	| exp_032_dual_critic_walker | walker | dual_critic | 0 | Healthy(0) | 1.100 | metrics.nve_peak |
45	| exp_032b_dual_critic_walker_s1 | walker | dual_critic | 1 | Healthy(0) | 1.400 | metrics.peak_nve |
46	| exp_034_dual_critic_cheetah | cheetah | dual_critic | 0 | CIVO(1) | 4.500 | computed ve_ratio_peak/baseline at 55K |
47	| exp_036_dual_critic_pickcube | cheetah | dual_critic | 0 | CIVO(1) | 2.300 | metrics.nve_peak |
48	| exp_037_wide_critic_cheetah | cheetah | other | ? | CIVO(1) | 3.600 | metrics.nve_peak |
49	| exp_042_frozen_dt_emb_walker | walker | frozen_dt_emb | 0 | Healthy(0) | 0.194 | metrics.nve_peak |
50	| exp_043_008f_walker_s1 | walker | 008f_no_dt_emb | 1 | Healthy(0) | 0.808 | metrics.nve_peak |
51	| exp_045_treatment_extension_008d_s3 | walker | 008d_civo_trigger | 3 | CIVO(1) | 4.910 | metrics.nve_peak |
52	| exp_046_frozen_dt_emb_cheetah | cheetah | frozen_dt_emb | 0 | Healthy(0) | 1.350 | metrics.nve_peak |
53	| exp_047_frozen_dt_emb_walker_s1 | walker | frozen_dt_emb | 1 | Healthy(0) | 1.710 | metrics.nve_peak |
54	| exp_048_cheetah_civo_extension | cheetah | other | 0 | CIVO(1) | 2.750 | max(nve_final) |
55	| exp_057_frozen_dt_emb_walker_s2 | walker | frozen_dt_emb | 2 | Healthy(0) | 1.880 | metrics.nve_peak |
56	| exp_058_frozen_dt_emb_cheetah_s1 | cheetah | frozen_dt_emb | 1 | Healthy(0) | 0.780 | metrics.nve_peak |
57	| exp_059_walker_trained_s5 | walker | trained_dt_emb | 5 | CIVO(1) | 4.720 | metrics.nve_peak |
58	| exp_067_frozen_dt_emb_walker_plan015 | walker | frozen_dt_emb | 0 | Healthy(0) | 0.400 | metrics.nve_peak |
59	| exp_068_008d_walker_repro_s1 | walker | 008d_civo_trigger | 1 | CIVO(1) | 4.120 | max(nve_final_105k) |
60	| exp_069_008f_walker_repro_s1 | walker | 008f_no_dt_emb | 1 | Healthy(0) | 0.660 | metrics.nve_peak |
61	| exp_070_008e_v3_walker_s0 | walker | 008e_v3_mitigation | 0 | Healthy(0) | 0.800 | metrics.nve_peak |
62	| exp_071_008f_walker_s3 | walker | 008f_no_dt_emb | 3 | Healthy(0) | 0.974 | computed ve_ratio_peak/max_baseline_ve |
63	| exp_072_008e_v3_walker_s5 | walker | 008e_v3_mitigation | 5 | Healthy(0) | 0.610 | metrics.nve_peak |
64	| exp_073_008f_walker_s4 | walker | 008f_no_dt_emb | 4 | Healthy(0) | 0.760 | metrics.nve_peak |
65	
66	## 分类结果
67	
68	| threshold | TP | FP | TN | FN | Precision | Recall | F1 | Accuracy |
69	|-----------|----|----|----|----|-----------|--------|-----|----------|
70	| 1.0 | 24 | 9 | 23 | 0 | 0.727 | 1.000 | 0.842 | 0.839 |
71	| 1.1 | 24 | 8 | 24 | 0 | 0.750 | 1.000 | 0.857 | 0.857 |
72	| 1.2 | 24 | 7 | 25 | 0 | 0.774 | 1.000 | 0.873 | 0.875 |
73	| 1.3 | 24 | 7 | 25 | 0 | 0.774 | 1.000 | 0.873 | 0.875 |
74	| 1.5 ** | 24 | 3 | 29 | 0 | 0.889 | 1.000 | 0.941 | 0.946 |
75	| 1.7 | 21 | 3 | 29 | 3 | 0.875 | 0.875 | 0.875 | 0.893 |
76	| 2.0 | 21 | 0 | 32 | 3 | 1.000 | 0.875 | 0.933 | 0.946 |
77	
78	## AUROC
79	
80	**AUROC = 0.9902**
81	
82	Computed from 24 positive + 32 negative samples using 33 ROC points
83	
84	ROC 关键点 (FPR, TPR):
85	
86	| Threshold | FPR | TPR |
87	|-----------|-----|-----|
88	| 1.0 | 0.281 | 1.000 |
89	| 1.1 | 0.250 | 1.000 |
90	| 1.2 | 0.219 | 1.000 |
91	| 1.3 | 0.219 | 1.000 |
92	| 1.5 | 0.094 | 1.000 |
93	| 1.7 | 0.094 | 0.875 |
94	| 2.0 | 0.000 | 0.875 |
95	
96	## 推荐阈值
97	
98	**推荐阈值: NVE >= 1.5** (基于最高 F1 = 0.941)
99	
100	- Precision = 0.889, Recall = 1.000, Accuracy = 0.946
101	- TP=24, FP=3, TN=29, FN=0
102	
103	### 阈值选择权衡
104	
105	- **低阈值 (1.0-1.2)**: 高 Recall (少漏报) 但多误报。适用于安全优先场景 (宁可误报不可漏报)。
106	- **中阈值 (1.3-1.5)**: Recall/Precision 平衡。1.5 是 CIVO 论文推荐的 onset 检测阈值。
107	- **高阈值 (1.7-2.0)**: 高 Precision (少误报) 但可能漏报早期 CIVO。适用于减少不必要干预。
108	
109	### 最佳阈值 (1.5) 下的分类细节
110	
111	**False Positives (误报为CIVO):**
112	
113	- `exp_008e_v3_subsample_on_dt1_h15`: peak_nve=1.930, config=008e_v3_mitigation, env=walker
114	- `exp_047_frozen_dt_emb_walker_s1`: peak_nve=1.710, config=frozen_dt_emb, env=walker
115	- `exp_057_frozen_dt_emb_walker_s2`: peak_nve=1.880, config=frozen_dt_emb, env=walker
116	
117	### 阈值 1.5 下的分类细节
118	
119	**False Positives (误报为CIVO):**
120	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ae813a79-db9f-4a12-b6ee-ad91ade39065",
  "uuid": "affbcf61-6d59-4a66-9570-c694e0a6951f",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/plan_034_nve_threshold/analysis.md",
      "content": "# NVE Threshold Sensitivity Analysis\n\n## 数据集\n\n样本总数: 56 (Collapsed: 24, Healthy: 32)\n\n| exp_id | env | config | seed | ground_truth | peak_nve | nve_source |\n|--------|-----|--------|------|-------------|----------|------------|\n| exp_006_fixed_dt2 | walker | 006_fixed_dt2 | 1 | CIVO(1) | 4.835 | computed ve_ratio/baseline at 65K |\n| exp_008a_cheetah_unexposed_s0 | cheetah | 008a_unexposed | 0 | Healthy(0) | 0.490 | max(nve_105k) |\n| exp_008a_cheetah_unexposed_s1 | cheetah | 008a_unexposed | 1 | Healthy(0) | 0.478 | max(nve_105k) |\n| exp_008a_no_subsample_dt2 | walker | 008a_unexposed | 1 | Healthy(0) | 0.930 | max(normalized_ve_55K) |\n| exp_008a_unexposed_s1 | walker | 008a_unexposed | 1 | Healthy(0) | 0.598 | computed civo_ve_ratio_final/max_baseline_ve |\n| exp_008a_unexposed_s2 | walker | 008a_unexposed | 2 | Healthy(0) | 0.463 | computed civo_ve_ratio_final/max_baseline_ve |\n| exp_008d_civo_trigger_s3 | walker | 008d_civo_trigger | 3 | CIVO(1) | 1.530 | metrics.nve_peak |\n| exp_008d_civo_trigger_s4 | walker | 008d_civo_trigger | 4 | CIVO(1) | 4.620 | metrics.nve_peak |\n| exp_008d_subsample_on_h8 | walker | 008d_civo_trigger | 1 | CIVO(1) | 4.124 | computed ve_ratio/baseline at 55K |\n| exp_008e_v3_s3 | walker | 008e_v3_mitigation | 3 | CIVO(1) | 4.020 | metrics.nve_peak |\n| exp_008e_v3_s4 | walker | 008e_v3_mitigation | 4 | Healthy(0) | 0.990 | metrics.nve_peak |\n| exp_008e_v3_subsample_on_dt1_h15 | walker | 008e_v3_mitigation | 1 | Healthy(0) | 1.930 | max(metrics.normalized_ve) at 25K |\n| exp_008e_v3_walker_s1 | walker | 008e_v3_mitigation | 1 | Healthy(0) | 0.803 | computed ve_ratio/baseline at 105K |\n| exp_008e_v3_walker_s2 | walker | 008e_v3_mitigation | 2 | CIVO(1) | 3.780 | max(final_nve) |\n| exp_008f_no_dt_embed_subsample_on_h8 | walker | 008f_no_dt_emb | 1 | Healthy(0) | 1.020 | max(eval_checkpoints.normalized_ve) at 25K |\n| exp_008f_s3_no_dt_embed_walker | walker | 008f_no_dt_emb | 3 | Healthy(0) | 1.490 | metrics.nve_peak (parsed '< 1.5x') |\n| exp_008f_s4 | walker | 008f_no_dt_emb | 4 | Healthy(0) | 1.410 | metrics.peak_nve |\n| exp_009b_008d_walker_s2 | walker | 008d_civo_trigger | 2 | CIVO(1) | 1.620 | metrics.nve_peak |\n| exp_009c_s3 | walker | other | 3 | Healthy(0) | 0.520 | max(nve_105k) |\n| exp_009e_008d_walker_s1 | walker | 008d_civo_trigger | 1 | CIVO(1) | 4.130 | metrics.nve_peak |\n| exp_010b_cheetah_civo_trigger | cheetah | 008d_civo_trigger | 1 | CIVO(1) | 8.270 | metrics.nve_peak |\n| exp_010b_cheetah_civo_trigger_s0 | cheetah | 008d_civo_trigger | 0 | CIVO(1) | 70.640 | max(nve_105K) |\n| exp_015b_frozen_dt_emb | walker | frozen_dt_emb | 1 | Healthy(0) | 0.467 | max(nve_85K) |\n| exp_020_vanilla_dreamerv3_s2 | walker | baseline | 2 | Healthy(0) | 0.983 | computed ve_ratio/baseline at 105K |\n| exp_021_full_sgs_cheetah_s1 | cheetah | sgs | 1 | CIVO(1) | 9.940 | metrics.nve_peak |\n| exp_024b_cheetah_no_dt_emb_s0 | cheetah | 008f_no_dt_emb | 0 | Healthy(0) | 0.200 | metrics.nve_peak |\n| exp_024b_cheetah_no_dt_emb_s1 | cheetah | 008f_no_dt_emb | 1 | Healthy(0) | 0.100 | metrics.nve_peak |\n| exp_027_tcn_walker_s0 | walker | tcn | 0 | CIVO(1) | 3.965 | metrics.peak_nve |\n| exp_027_tcn_walker_s0_sigma02 | walker | tcn | 0 | Healthy(0) | 0.908 | metrics.nve_max |\n| exp_027_tcn_walker_s1 | walker | tcn | 1 | CIVO(1) | 1.637 | metrics.nve_max |\n| exp_029a_tcn_walker_s1_sigma02 | walker | tcn | 1 | Healthy(0) | 0.643 | metrics.nve_max |\n| exp_029b_tcn_walker_s2_sigma02 | walker | tcn | 2 | CIVO(1) | 2.765 | metrics.nve_peak |\n| exp_029d_tcn_walker_s3_sigma02 | walker | tcn | 3 | CIVO(1) | 3.000 | metrics.nve_peak |\n| exp_030b_tcn_cheetah_s0_sigma05 | cheetah | tcn | 0 | CIVO(1) | 10.666 | metrics.nve_max |\n| exp_031b_tcn_pickcube_s0_sigma05 | pickcube | tcn | 0 | CIVO(1) | 3.300 | metrics.nve_peak |\n| exp_032_dual_critic_walker | walker | dual_critic | 0 | Healthy(0) | 1.100 | metrics.nve_peak |\n| exp_032b_dual_critic_walker_s1 | walker | dual_critic | 1 | Healthy(0) | 1.400 | metrics.peak_nve |\n| exp_034_dual_critic_cheetah | cheetah | dual_critic | 0 | CIVO(1) | 4.500 | computed ve_ratio_peak/baseline at 55K |\n| exp_036_dual_critic_pickcube | cheetah | dual_critic | 0 | CIVO(1) | 2.300 | metrics.nve_peak |\n| exp_037_wide_critic_cheetah | cheetah | other | ? | CIVO(1) | 3.600 | metrics.nve_peak |\n| exp_042_frozen_dt_emb_walker | walker | frozen_dt_emb | 0 | Healthy(0) | 0.194 | metrics.nve_peak |\n| exp_043_008f_walker_s1 | walker | 008f_no_dt_emb | 1 | Healthy(0) | 0.808 | metrics.nve_peak |\n| exp_045_treatment_extension_008d_s3 | walker | 008d_civo_trigger | 3 | CIVO(1) | 4.910 | metrics.nve_peak |\n| exp_046_frozen_dt_emb_cheetah | cheetah | frozen_dt_emb | 0 | Healthy(0) | 1.350 | metrics.nve_peak |\n| exp_047_frozen_dt_emb_walker_s1 | walker | frozen_dt_emb | 1 | Healthy(0) | 1.710 | metrics.nve_peak |\n| exp_048_cheetah_civo_extension | cheetah | other | 0 | CIVO(1) | 2.750 | max(nve_final) |\n| exp_057_frozen_dt_emb_walker_s2 | walker | frozen_dt_emb | 2 | Healthy(0) | 1.880 | metrics.nve_peak |\n| exp_058_frozen_dt_emb_cheetah_s1 | cheetah | frozen_dt_emb | 1 | Healthy(0) | 0.780 | metrics.nve_peak |\n| exp_059_walker_trained_s5 | walker | trained_dt_emb | 5 | CIVO(1) | 4.720 | metrics.nve_peak |\n| exp_067_frozen_dt_emb_walker_plan015 | walker | frozen_dt_emb | 0 | Healthy(0) | 0.400 | metrics.nve_peak |\n| exp_068_008d_walker_repro_s1 | walker | 008d_civo_trigger | 1 | CIVO(1) | 4.120 | max(nve_final_105k) |\n| exp_069_008f_walker_repro_s1 | walker | 008f_no_dt_emb | 1 | Healthy(0) | 0.660 | metrics.nve_peak |\n| exp_070_008e_v3_walker_s0 | walker | 008e_v3_mitigation | 0 | Healthy(0) | 0.800 | metrics.nve_peak |\n| exp_071_008f_walker_s3 | walker | 008f_no_dt_emb | 3 | Healthy(0) | 0.974 | computed ve_ratio_peak/max_baseline_ve |\n| exp_072_008e_v3_walker_s5 | walker | 008e_v3_mitigation | 5 | Healthy(0) | 0.610 | metrics.nve_peak |\n| exp_073_008f_walker_s4 | walker | 008f_no_dt_emb | 4 | Healthy(0) | 0.760 | metrics.nve_peak |\n\n## 分类结果\n\n| threshold | TP | FP | TN | FN | Precision | Recall | F1 | Accuracy |\n|-----------|----|----|----|----|-----------|--------|-----|----------|\n| 1.0 | 24 | 9 | 23 | 0 | 0.727 | 1.000 | 0.842 | 0.839 |\n| 1.1 | 24 | 8 | 24 | 0 | 0.750 | 1.000 | 0.857 | 0.857 |\n| 1.2 | 24 | 7 | 25 | 0 | 0.774 | 1.000 | 0.873 | 0.875 |\n| 1.3 | 24 | 7 | 25 | 0 | 0.774 | 1.000 | 0.873 | 0.875 |\n| 1.5 ** | 24 | 3 | 29 | 0 | 0.889 | 1.000 | 0.941 | 0.946 |\n| 1.7 | 21 | 3 | 29 | 3 | 0.875 | 0.875 | 0.875 | 0.893 |\n| 2.0 | 21 | 0 | 32 | 3 | 1.000 | 0.875 | 0.933 | 0.946 |\n\n## AUROC\n\n**AUROC = 0.9902**\n\nComputed from 24 positive + 32 negative samples using 33 ROC points\n\nROC 关键点 (FPR, TPR):\n\n| Threshold | FPR | TPR |\n|-----------|-----|-----|\n| 1.0 | 0.281 | 1.000 |\n| 1.1 | 0.250 | 1.000 |\n| 1.2 | 0.219 | 1.000 |\n| 1.3 | 0.219 | 1.000 |\n| 1.5 | 0.094 | 1.000 |\n| 1.7 | 0.094 | 0.875 |\n| 2.0 | 0.000 | 0.875 |\n\n## 推荐阈值\n\n**推荐阈值: NVE >= 1.5** (基于最高 F1 = 0.941)\n\n- Precision = 0.889, Recall = 1.000, Accuracy = 0.946\n- TP=24, FP=3, TN=29, FN=0\n\n### 阈值选择权衡\n\n- **低阈值 (1.0-1.2)**: 高 Recall (少漏报) 但多误报。适用于安全优先场景 (宁可误报不可漏报)。\n- **中阈值 (1.3-1.5)**: Recall/Precision 平衡。1.5 是 CIVO 论文推荐的 onset 检测阈值。\n- **高阈值 (1.7-2.0)**: 高 Precision (少误报) 但可能漏报早期 CIVO。适用于减少不必要干预。\n\n### 最佳阈值 (1.5) 下的分类细节\n\n**False Positives (误报为CIVO):**\n\n- `exp_008e_v3_subsample_on_dt1_h15`: peak_nve=1.930, config=008e_v3_mitigation, env=walker\n- `exp_047_frozen_dt_emb_walker_s1`: peak_nve=1.710, config=frozen_dt_emb, env=walker\n- `exp_057_frozen_dt_emb_walker_s2`: peak_nve=1.880, config=frozen_dt_emb, env=walker\n\n### 阈值 1.5 下的分类细节\n\n**False Positives (误报为CIVO):**\n",
      "numLines": 120,
      "startLine": 1,
      "totalLines": 160
    }
  }
}
```

</details>

---


### Assistant

_source line 82_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the data I need:

NVE analysis (n=56):
- AUROC = 0.990
- At threshold 1.5: TP=24, FP=3, TN=29, FN=0
- Accuracy = 53/56 (0.946)
- F1 = 0.941
- Precision = 0.889, Recall = 1.000

Registry counts:
- Total experiments: 158
- success: 80 (79 DONE + 1 ANALYZING)
- negative: 39


- failed: 11
- killed: 24

For the configurations count, I can see the NVE subset has various config types like fixed_dt2, unexposed, civo_trigger, v3_mitigation, no_dt_emb, and others, but I need to count all unique configurations across the full 158 experiments, not just the 56 labeled ones.

Looking at the pattern from when there were 133 experiments with 43 configurations, that's roughly 3.1 experiments per configuration. If the new experiments follow similar seeding patterns of existing configs, the total configurations shouldn't increase proportionally to the experiment count.

Scanning through the recent experiments, I see mostly new seeds of existing configurations mixed with a few genuinely new experimental setups like the cartpole environment and some analysis variants, which suggests the configuration count would grow more slowly than the experiment count. I'm trying to get a more precise count of what constitutes a distinct configuration. Rather than relying on rough estimates, I should systematically group the experiments and count the unique experimental conditions, then cross-reference with what the previous analysis showed to arrive at an accurate total.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ae813a79-db9f-4a12-b6ee-ad91ade39065",
  "uuid": "3a21230c-d2d4-4f6a-b031-a086e4442063",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UfwYgDizgS6L63WKen47pb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4625,
      "cache_read_input_tokens": 56880,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4625
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

_source line 83_

<details open><summary>🔧 Tool call — Bash · `toolu_01YPcuXM7YuLvmz2Zt4JQMUL`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/ae813a79-db9f-4a12-b6ee-ad91ade39065/tool-results/mcp-agent-ml-research-read_registry-1779718348946.txt | python3 -c \"\nimport json, sys, re\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps = result.get('data', result)\nif isinstance(exps, dict) and 'experiments' in exps:\n    exps = exps['experiments']\nelif isinstance(exps, dict) and 'data' in exps:\n    exps = exps['data']\n\nif isinstance(exps, dict):\n    items = exps\nelse:\n    items = {str(i): e for i, e in enumerate(exps)}\n\n# Map exp IDs to configs based on semantic grouping\n# Key insight: experiments that are seeds of same condition should map to same config\n# Let me group by looking at the hypothesis field for clues\n\n# Build semantic config groups manually by parsing exp IDs\ndef get_config(eid):\n    # Handle known patterns\n    # Strip _extended suffix first\n    eid_clean = re.sub(r'_extended$', '', eid)\n    \n    # Known same-config groups:\n    # exp_001_baseline*, exp_009a*, exp_009d*, exp_020* -> walker baseline\n    # exp_008d*, exp_009b*, exp_009e*, exp_045*, exp_068* -> walker trained/civo_trigger\n    # exp_008f*, exp_009c*, exp_009f*, exp_009g*, exp_009h*, exp_043*, exp_069*, exp_071*, exp_073* -> walker no_dt_emb\n    # exp_008a (walker) -> walker unexposed\n    # exp_008a_unexposed*, exp_008a_untrained* -> walker unexposed/untrained variants\n    # exp_008a_cheetah* -> cheetah unexposed\n    # exp_008e_v3* -> walker 008e_v3\n    # exp_010b*, exp_075*, exp_076*, exp_078* -> cheetah civo trigger\n    # exp_023*, exp_023a*, exp_023b*, exp_010a*, exp_077* -> cheetah baseline\n    # exp_024*, exp_024b*, exp_082* -> cheetah no dt_emb\n    # etc.\n    \n    # This is too complex for automatic grouping. Let me just count unique\n    # (intervention_type, environment) pairs\n    pass\n\n# Alternative: count distinct experiment 'families' by prefix\n# A 'family' is identified by the core experiment number + variant letter\nfamilies = set()\nfor eid in items.keys():\n    # Extract base experiment pattern: exp_NNN[a-z]?_description\n    m = re.match(r'(exp_\\d+[a-z]?(?:_v\\d+)?)', eid)\n    if m:\n        families.add(m.group(1))\n    else:\n        families.add(eid)\n\nprint(f'Experiment families (by prefix): {len(families)}')\nprint(sorted(families))\n\"\n",
  "description": "Count experiment families by prefix",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ae813a79-db9f-4a12-b6ee-ad91ade39065",
  "uuid": "7cb89e4d-8279-42fd-9585-626659f1f6ca",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UfwYgDizgS6L63WKen47pb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4625,
      "cache_read_input_tokens": 56880,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4625
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


### Tool result

_source line 84 · 2026-05-25T14:16:10.609Z_

<details><summary>↩ Tool result · `toolu_01YPcuXM7YuLvmz2Zt4JQMUL`</summary>

```text
Experiment families (by prefix): 113
['016e', 'exp_001', 'exp_002', 'exp_003', 'exp_004', 'exp_005', 'exp_006', 'exp_007', 'exp_008a', 'exp_008c', 'exp_008d', 'exp_008e', 'exp_008e_v2', 'exp_008e_v3', 'exp_008f', 'exp_009a', 'exp_009b', 'exp_009c', 'exp_009d', 'exp_009e', 'exp_009f', 'exp_009g', 'exp_009h', 'exp_010a', 'exp_010b', 'exp_015b', 'exp_016', 'exp_016b', 'exp_016c', 'exp_016d', 'exp_016e', 'exp_017', 'exp_018', 'exp_018v', 'exp_019a', 'exp_019a_v2', 'exp_019b', 'exp_020', 'exp_021', 'exp_022', 'exp_022b', 'exp_023', 'exp_023a', 'exp_023b', 'exp_024', 'exp_024b', 'exp_025', 'exp_026', 'exp_027', 'exp_028', 'exp_029a', 'exp_029b', 'exp_029c', 'exp_029d', 'exp_030a', 'exp_030b', 'exp_030c', 'exp_031', 'exp_031b', 'exp_032', 'exp_032b', 'exp_033', 'exp_034', 'exp_035', 'exp_036', 'exp_037', 'exp_038', 'exp_039', 'exp_040', 'exp_041', 'exp_042', 'exp_043', 'exp_044', 'exp_045', 'exp_046', 'exp_047', 'exp_048', 'exp_049', 'exp_050', 'exp_051', 'exp_052', 'exp_053', 'exp_054', 'exp_055', 'exp_056', 'exp_057', 'exp_058', 'exp_059', 'exp_060', 'exp_061', 'exp_062', 'exp_063', 'exp_064', 'exp_065', 'exp_066', 'exp_066b', 'exp_067', 'exp_068', 'exp_069', 'exp_070', 'exp_071', 'exp_072', 'exp_073', 'exp_074', 'exp_075', 'exp_076', 'exp_077', 'exp_078', 'exp_079', 'exp_080', 'exp_081', 'exp_082', 'exp_rssm_fidelity_analysis']
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ae813a79-db9f-4a12-b6ee-ad91ade39065",
  "uuid": "00e436c2-fbec-46aa-9997-608c4a893c01",
  "tool_use_result": {
    "stdout": "Experiment families (by prefix): 113\n['016e', 'exp_001', 'exp_002', 'exp_003', 'exp_004', 'exp_005', 'exp_006', 'exp_007', 'exp_008a', 'exp_008c', 'exp_008d', 'exp_008e', 'exp_008e_v2', 'exp_008e_v3', 'exp_008f', 'exp_009a', 'exp_009b', 'exp_009c', 'exp_009d', 'exp_009e', 'exp_009f', 'exp_009g', 'exp_009h', 'exp_010a', 'exp_010b', 'exp_015b', 'exp_016', 'exp_016b', 'exp_016c', 'exp_016d', 'exp_016e', 'exp_017', 'exp_018', 'exp_018v', 'exp_019a', 'exp_019a_v2', 'exp_019b', 'exp_020', 'exp_021', 'exp_022', 'exp_022b', 'exp_023', 'exp_023a', 'exp_023b', 'exp_024', 'exp_024b', 'exp_025', 'exp_026', 'exp_027', 'exp_028', 'exp_029a', 'exp_029b', 'exp_029c', 'exp_029d', 'exp_030a', 'exp_030b', 'exp_030c', 'exp_031', 'exp_031b', 'exp_032', 'exp_032b', 'exp_033', 'exp_034', 'exp_035', 'exp_036', 'exp_037', 'exp_038', 'exp_039', 'exp_040', 'exp_041', 'exp_042', 'exp_043', 'exp_044', 'exp_045', 'exp_046', 'exp_047', 'exp_048', 'exp_049', 'exp_050', 'exp_051', 'exp_052', 'exp_053', 'exp_054', 'exp_055', 'exp_056', 'exp_057', 'exp_058', 'exp_059', 'exp_060', 'exp_061', 'exp_062', 'exp_063', 'exp_064', 'exp_065', 'exp_066', 'exp_066b', 'exp_067', 'exp_068', 'exp_069', 'exp_070', 'exp_071', 'exp_072', 'exp_073', 'exp_074', 'exp_075', 'exp_076', 'exp_077', 'exp_078', 'exp_079', 'exp_080', 'exp_081', 'exp_082', 'exp_rssm_fidelity_analysis']",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Assistant

_source line 85_

<details><summary>Logged reasoning block</summary>

```text
113 families is still too granular. Many of these prefixes (like exp_009a, exp_009b, etc.) refer to the same experimental condition but with a different naming convention. And many later experiments (exp_067, exp_068, exp_069, etc.) are just additional seeds of earlier configurations.

I think the best approach is to accept that I cannot reliably compute the exact configuration count automatically. The "43 configurations" number in the original Q&A was likely manually counted. The task says to update to "registry real numbers" — for total experiments and success/negative counts I can do this confidently, but for "configurations" I need to either:


1. Keep the same number if it's still accurate (unlikely since we added experiments)
2. Compute it accurately (too complex without manual review)
3. Update proportionally (rough but reasonable)

Let me reconsider this. The original text mentions "133 experiments across 43 configurations," and now I have 158 total experiments, which is 25 more. Looking at the new experiments I've added, most of them appear to be additional seeds or variants of existing configurations rather than entirely new configurations, so a proportional increase might actually underestimate the true number of distinct configurations.

Scanning through the new experiments, I can see a mix: some are additional seeds of existing setups like the frozen DT embedding variants and walker experiments, but there are also genuinely new configurations like the cartpole experiments, the RSSM fidelity analysis, value distribution, and the timeseries variants. So the configuration count has grown, but not as dramatically as the experiment count. Looking at the remaining experiments to set up, I'm continuing with the cheetah baseline and walker variants, then moving into some new analysis work around RSSM fidelity and a few other configurations I need to explore.

But I'm realizing I need to be more careful about what was actually in the original 133 experiments versus what's been added since. The NVE analysis tracked 56 data points up through exp_073, covering different mitigation strategies like the civo trigger, v3 approach, and no dt_emb variants, so there's some overlap I need to account for when counting the total. Looking at Q4 and Q10 more carefully, I see Q4 just mentions the experiment and success counts while Q10 includes both the experiment count and configuration breakdown. So I need to update "133 experiments" to "158 experiments" in Q4, and "63 successful" to "80 successful". For Q10, the same experiment count changes apply, but the "43 configurations" reference needs checking against what I actually found in the registry data.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ae813a79-db9f-4a12-b6ee-ad91ade39065",
  "uuid": "613423ab-55f3-480e-baf7-1f8b971124a8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QaCULmVi97CoeBydPWDohj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2796,
      "cache_read_input_tokens": 61505,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2796
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

_source line 86_

Let me check the configuration count from the report or artifacts that originally computed it.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ae813a79-db9f-4a12-b6ee-ad91ade39065",
  "uuid": "7e9f0ab5-0476-4143-abf9-be998a6c15ac",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QaCULmVi97CoeBydPWDohj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2796,
      "cache_read_input_tokens": 61505,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2796
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

_source line 87_

<details open><summary>🔧 Tool call — Grep · `toolu_01UcAvQpoWwimnhgquRL9XUF`</summary>

```json
{
  "pattern": "43 configurations|across 43",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon",
  "output_mode": "content",
  "-C": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ae813a79-db9f-4a12-b6ee-ad91ade39065",
  "uuid": "29968c5d-35ad-45f3-b78f-fa988bb2b8ee",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QaCULmVi97CoeBydPWDohj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2796,
      "cache_read_input_tokens": 61505,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2796
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
