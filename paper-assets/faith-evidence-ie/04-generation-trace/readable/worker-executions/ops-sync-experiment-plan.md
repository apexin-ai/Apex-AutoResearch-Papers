# ops sync experiment plan

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 27
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/workers/worker_ops_sync_experiment_plan_20260519T165209.log`
- **Structured JSON:** [`dc3d361bc4cc9c3ffab2.json`](../../sessions/dc/dc3d361bc4cc9c3ffab2.json)

## Before a recorded user message

27 recorded events

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
  "session_id": "39f8a4ed-6d6b-4c23-9e46-167a8118c922",
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
  "uuid": "d24b6ad6-20ac-4c48-8733-712d53073e8b",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/memory/"
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
    "resetsAt": 1779216600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "96bc6163-5130-43aa-9135-fe67db75f5f5",
  "session_id": "39f8a4ed-6d6b-4c23-9e46-167a8118c922"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to sync the experiment_plan.yaml with the registry state. Let me start by reading both files.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "39f8a4ed-6d6b-4c23-9e46-167a8118c922",
  "uuid": "4609ca9c-a42d-426c-80d3-001f1ca0a699",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0176vKMoJDTBQhajQxvvXuCo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12663,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12663
      },
      "output_tokens": 42,
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

Reading experiment_plan.yaml and registry in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "39f8a4ed-6d6b-4c23-9e46-167a8118c922",
  "uuid": "319a3d4a-0b0f-49ab-8e02-a078731c121c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0176vKMoJDTBQhajQxvvXuCo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12663,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12663
      },
      "output_tokens": 42,
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Rn4qcRSivKA6pmCiefCErC`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__save_project_file",
  "max_results": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "39f8a4ed-6d6b-4c23-9e46-167a8118c922",
  "uuid": "62df229d-16da-4bee-8431-38d76673deca",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0176vKMoJDTBQhajQxvvXuCo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12663,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12663
      },
      "output_tokens": 42,
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

_source line 7 · 2026-05-19T16:52:20.286Z_

<details><summary>↩ Tool result · `toolu_01Rn4qcRSivKA6pmCiefCErC`</summary>

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
  "session_id": "39f8a4ed-6d6b-4c23-9e46-167a8118c922",
  "uuid": "564f73e3-5a0f-4df5-81b1-dc96c15224e8",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_registry,mcp__agent-ml-research__save_project_file",
    "total_deferred_tools": 25
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01TcWfpWmtqjyXw9cDgiB9C9`</summary>

```json
{
  "project": "faith-evidence-ie",
  "file": "experiment_plan.yaml",
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
  "session_id": "39f8a4ed-6d6b-4c23-9e46-167a8118c922",
  "uuid": "4696b1a0-c0f2-4892-bd9f-d951ea8e518a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UjH6AmCcZJRaUPd7QDSNnN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1098,
      "cache_read_input_tokens": 24504,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1098
      },
      "output_tokens": 68,
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

_source line 9 · 2026-05-19T16:52:24.095Z_

<details><summary>↩ Tool result · `toolu_01TcWfpWmtqjyXw9cDgiB9C9`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'experiment_plan.yaml'\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "39f8a4ed-6d6b-4c23-9e46-167a8118c922",
  "uuid": "c82a3f74-b18d-4779-8199-2995da1b4847",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'experiment_plan.yaml'\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'experiment_plan.yaml'\", \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01VEXeynQ1SBwaiLysokoMDR`</summary>

```json
{
  "project": "faith-evidence-ie",
  "limit": 30
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "39f8a4ed-6d6b-4c23-9e46-167a8118c922",
  "uuid": "6bf7111d-14c7-485b-8878-72bfcd324ee0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UjH6AmCcZJRaUPd7QDSNnN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1098,
      "cache_read_input_tokens": 24504,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1098
      },
      "output_tokens": 68,
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

_source line 11 · 2026-05-19T16:52:25.389Z_

<details><summary>↩ Tool result · `toolu_01VEXeynQ1SBwaiLysokoMDR`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"d112_rsft_no_evidence_eval_r3\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-19T14:47:43.281Z\", \"updated_at\": \"2026-05-19T15:47:04.413Z\", \"hypothesis\": \"4B RSFT no-evidence eval r3 (D112 bf16 SFT s44 base): 移除 evidence 输出后测量 4B RSFT 的 evidence tax。对比 with-evidence 的 D112 RSFT ign_f1。r1/r2 因脚本路径错误失败 (EXIT_CODE=127)，r3 使用正确路径 scripts/seed_expansion/eval_4b_rsft_no_evidence.sh。\", \"parent\": \"d112_rsft_s44_eval_bf16\"}, \"plan019_8b_sft_s43_eval\": {\"status\": \"ANALYZING\", \"created_at\": \"2026-05-19T14:00:00.027Z\", \"updated_at\": \"2026-05-19T15:41:53.613Z\", \"hypothesis\": \"D076 eval for 8B SFT s43. 补齐第 3 个 8B SFT seed 的 eval 结果。8B SFT s42 ign_f1=0.5128, s44 ign_f1=0.4604. 3-seed mean 将决定 \\\"1.7B RSFT surpasses 8B SFT\\\" claim (Claim 3) 的统计力。\", \"parent\": \"plan019_8b_sft_s43\"}, \"plan019_1_7b_rsft_no_evidence_eval_2048\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-19T14:48:26.124Z\", \"updated_at\": \"2026-05-19T14:50:27.272Z\", \"hypothesis\": \"排除截断混淆后验证 1.7B RSFT negative evidence tax (-7.7pp) 是真实效应还是截断 artifact。原实验 max_new_tokens=1024 截断率 59.2% (583/985)，改用 2048 排除截断伪影。来源: Reviewer warning on plan019_1_7b_rsft_no_evidence_eval。\", \"parent\": \"plan019_1_7b_rsft_no_evidence_eval\"}, \"plan019_1_7b_rsft_no_evidence_eval\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T11:42:59.170Z\", \"updated_at\": \"2026-05-19T14:47:15.332Z\", \"hypothesis\": \"Removing evidence output at inference time should improve RE ign_f1 above 0.5122 (with-evidence baseline) for 1.7B RSFT, indicating an evidence tax where generating evidence hurts relation extraction performance\", \"metrics\": {\"ign_f1\": 0.4352, \"f1\": 0.4552, \"evi_f1_dreeam\": 0, \"evi_f1_tp\": 0, \"edcr\": 0, \"format_ok_rate\": 0.971, \"truncated_rate\": 0.592, \"predictions\": 25221}, \"conclusion\": \"killed\", \"notes\": \"Evidence tax measurement for 1.7B RSFT s42. Hypothesis rejected: no-evidence ign_f1=0.4352 < with-evidence ign_f1=0.5122, a DECREASE of 7.70pp. Removing evidence hurts 1.7B RE performance — evidence generation acts as beneficial chain-of-thought. Contrast with 14B SFT where evidence tax ≈ 0.03pp (nearly zero). This suggests smaller models rely more on evidence reasoning to achieve good RE. High truncation rate (59.2%) but 97.1% format compliance. No W&B run.\"}, \"plan019_8b_sft_s43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T12:04:31.830Z\", \"updated_at\": \"2026-05-19T14:01:26.124Z\", \"hypothesis\": \"8B SFT seed=43: 补齐第 3 seed 改善 '1.7B RSFT surpasses 8B SFT' claim 统计力（当前 p≈0.20，瓶颈在 8B SFT 仅 2 seeds）。Reviewer 建议，对应 plan_019 Claim 3。\", \"parent\": \"plan019_8b_sft_s44\", \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 0.5684, \"eval_loss\": 0.719, \"eval_mean_token_accuracy\": 0.8378, \"train_runtime_s\": 6639, \"epochs\": 3, \"train_steps\": 570}}, \"plan017_14b_sft_eval_r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T08:51:48.518Z\", \"updated_at\": \"2026-05-19T13:58:13.384Z\", \"hypothesis\": \"D076 eval for 14B SFT baseline (bf16, --no-quantize). 修正 r1 的 D076 违规（r1 用了 int8 量化）。14B 是第 4 个 scale 档，SFT baseline 用于计算 RSFT 增益和 evidence tax。预期 ign_f1 高于 8B SFT mean (0.4866)。\", \"parent\": \"plan017_14b_sft\", \"metrics\": {\"ign_f1\": 0.5507, \"ign_precision\": 0.5268, \"ign_recall\": 0.5768, \"f1\": 0.5611, \"precision\": 0.5481, \"recall\": 0.5748, \"format_compliance_rate\": 1, \"field_compliance_rate\": 0.8589, \"evidence_format_rate\": 0.8589, \"n_truncated\": 139, \"n_total\": 985, \"n_parseable\": 985, \"n_predictions\": 14081, \"inference_time_seconds\": 18011.3, \"evi_precision\": 0.8197, \"evi_recall\": 0.839, \"evi_f1\": 0.8292, \"evi_f1_joint\": 0.4453, \"evi_joint_precision\": 0.4174, \"evi_joint_recall\": 0.4772, \"edcr\": 0.597}, \"conclusion\": \"success\"}, \"plan019_8b_rsft_no_evidence_eval_r2\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-19T13:44:38.870Z\", \"updated_at\": \"2026-05-19T13:54:52.747Z\", \"hypothesis\": \"8B RSFT no-evidence eval r2: 移除 evidence 输出后测量 8B RSFT 的 evidence tax。8B RSFT with-evidence mean ign_f1=0.5414 (s42=0.5376, s44=0.5451)。若 no-evidence ign_f1 > with-evidence，证实 evidence 生成对 8B RE 的性能代价；与 1.7B/4B/14B evidence tax 配合构建跨尺度 scaling curve (Claim 3)。修正 r1 的 cuda:2 冲突问题，改用 cuda:0。\", \"parent\": \"plan019_8b_rsft_no_evidence_eval\"}, \"d112_rsft_no_evidence_eval_r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T13:41:03.808Z\", \"updated_at\": \"2026-05-19T13:45:20.995Z\", \"hypothesis\": \"4B RSFT no-evidence eval (D112 bf16 SFT s44 base): 移除 evidence 输出后测量 4B RSFT 的 evidence tax。对比 with-evidence 的 canonical 4B RSFT ign_f1，验证 evidence 生成对 4B RE 性能的代价。与 1.7B/8B/14B no-evidence eval 配合构建跨尺度 evidence tax scaling curve (Claim 3)。\", \"parent\": \"d112_rsft_s44_eval_bf16\", \"conclusion\": \"failed\"}, \"plan019_8b_rsft_no_evidence_eval\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T13:12:23.195Z\", \"updated_at\": \"2026-05-19T13:44:36.625Z\", \"hypothesis\": \"8B RSFT no-evidence eval: 移除 evidence 输出后测量 8B RSFT 的 evidence tax。8B RSFT with-evidence mean ign_f1=0.5414 (s42=0.5376, s44=0.5451)。若 no-evidence ign_f1 > with-evidence，证实 evidence 生成对 8B RE 的性能代价；与 1.7B/4B/14B evidence tax 配合构建跨尺度 scaling curve (Claim 3)。\", \"parent\": \"plan019_8b_rsft_s44_eval\", \"conclusion\": \"killed\"}, \"d112_rsft_no_evidence_eval\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T13:19:08.763Z\", \"updated_at\": \"2026-05-19T13:41:48.937Z\", \"hypothesis\": \"4B RSFT no-evidence eval (D112 bf16 SFT s44 base): 移除 evidence 输出后测量 4B RSFT 的 evidence tax。对比 with-evidence 的 canonical 4B RSFT ign_f1，验证 evidence 生成对 4B RE 性能的代价。与 1.7B/8B/14B no-evidence eval 配合构建跨尺度 evidence tax scaling curve (Claim 3)。\", \"parent\": \"d112_rsft_s44_eval_bf16\", \"conclusion\": \"failed\", \"notes\": \"EXIT_CODE=127 (command not found), wall_clock=17s. fix_worker_id: worker_diagnose_d112_rsft_no_evidence_eval_20260519T134139. 诊断中。\"}, \"d112_rsft_s44_eval_bf16\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-19T13:04:19.692Z\", \"updated_at\": \"2026-05-19T13:16:48.504Z\", \"hypothesis\": \"D112 step 4 bf16: D076 eval for RSFT trained on SFT s44 base with CED k=1 scored data (bf16 LoRA). 修正原 d112_rsft_s44_eval 的 QLoRA confound。预期 ign_f1 > 0.4734 (SFT s44 baseline)。\", \"parent\": \"d112_rsft_s44_train_bf16\"}, \"d112_rsft_s44_train_bf16\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T11:19:27.034Z\", \"updated_at\": \"2026-05-19T13:04:56.446Z\", \"hypothesis\": \"D112 step 3 bf16 重跑：RSFT training on SFT s44 base using CED k=1 scored data，使用 bf16 LoRA（非 QLoRA）与其他所有 RSFT 实验一致。修正原 d112_rsft_s44_train 的 QLoRA confound（--quantize 导致 adapter 适应 4-bit 量化误差，bf16 eval 下 ign_f1=0.2181 灾难性崩溃）。\", \"parent\": \"\", \"conclusion\": \"success\"}, \"plan017_14b_sft_no_evidence_eval_r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T08:51:50.451Z\", \"updated_at\": \"2026-05-19T12:57:54.516Z\", \"hypothesis\": \"14B SFT no-evidence eval (bf16, --no-quantize). 修正 r1 的 D076 违规。测量 14B SFT 在不提供 evidence 时的 ign_f1，用于计算 evidence tax (Claim 3)。\", \"parent\": \"plan017_14b_sft\", \"metrics\": {\"ign_f1\": 0.551, \"ign_precision\": 0.5149, \"ign_recall\": 0.5926, \"f1\": 0.5649, \"precision\": 0.5386, \"recall\": 0.5939, \"format_compliance_rate\": 0.9868, \"n_truncated\": 105, \"n_predictions\": 15605, \"inference_time_seconds\": 14497.8}, \"conclusion\": \"success\"}, \"d112_rsft_s44_eval\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T07:34:55.266Z\", \"updated_at\": \"2026-05-19T12:02:10.888Z\", \"hypothesis\": \"D112 step 4: D076 eval for RSFT trained on SFT s44 base with CED k=1 scored data. 验证 RSFT 在最强 SFT seed (s44, ign_f1=0.4734) 上的泛化效果。预期 ign_f1 > 0.4734 (SFT s44 baseline)。\", \"parent\": \"d112_rsft_s44_train\", \"conclusion\": \"failed\", \"metrics\": {\"ign_f1\": 0.2181, \"note\": \"INVALID: QLoRA confound — adapter trained on 4-bit quantized backbone evaluated in bf16\"}}, \"plan019_1_7b_rsft_s44_r2_eval\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T08:43:01.975Z\", \"updated_at\": \"2026-05-19T12:00:32.897Z\", \"hypothesis\": \"D076 eval for 1.7B RSFT s44_r2 (Method A: s42 SFT adapter + s42 CED k=1 data, RSFT seed=44). 预期 ign_f1 接近 s42 (0.5122) 和 s43 (0.5109)，完成 1.7B 3-seed RSFT 统计。\", \"parent\": \"plan019_1_7b_rsft_s44_r2\", \"metrics\": {\"ign_f1\": 0.5125, \"ign_precision\": 0.5173, \"ign_recall\": 0.5078, \"f1\": 0.5294, \"precision\": 0.5434, \"recall\": 0.5162, \"evi_precision\": 0.815, \"evi_recall\": 0.8387, \"evi_f1\": 0.8267, \"edcr\": 0.6181, \"evi_joint_precision\": 0.4284, \"evi_joint_recall\": 0.4294, \"evi_f1_joint\": 0.4289, \"format_compliance_rate\": 0.999, \"field_compliance_rate\": 0.7543, \"n_truncated\": 240, \"inference_time_seconds\": 8615.6}, \"conclusion\": \"success\"}, \"d112_rsft_s44_train\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T04:33:11.623Z\", \"updated_at\": \"2026-05-19T11:18:57.557Z\", \"hypothesis\": \"D112 step 3: RSFT training on SFT s44 base using CED k=1 scored data. 在最强 SFT seed (s44, ign_f1=0.4734) 上验证 RSFT 效果，参数与 canonical s42 RSFT 完全一致。\", \"parent\": \"d112_rsft_s44_ced_score\", \"conclusion\": \"failed\", \"metrics\": {\"train_loss\": 0.6488, \"global_step\": 567}}, \"plan017_14b_sft_eval\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T07:23:43.367Z\", \"updated_at\": \"2026-05-19T08:54:24.083Z\", \"hypothesis\": \"D076 eval for 14B SFT baseline. 14B 是第 4 个 scale 档（1.7B/4B/8B/14B），SFT baseline 用于计算 RSFT 增益和 evidence tax。预期 ign_f1 高于 8B SFT mean (0.4866)。\", \"parent\": \"plan017_14b_sft\", \"conclusion\": \"killed\"}, \"plan017_14b_sft_no_evidence_eval\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T07:23:46.290Z\", \"updated_at\": \"2026-05-19T08:49:48.692Z\", \"hypothesis\": \"14B SFT no-evidence eval: 测量 14B SFT 在不提供 evidence 时的 ign_f1，用于计算 evidence tax (Claim 3)。与 4B evidence tax (D107: 47.21% vs 39.74%) 对比，验证 scale-dependent evidence tax 趋势。\", \"parent\": \"plan017_14b_sft\", \"conclusion\": \"killed\"}, \"plan019_1_7b_rsft_s43_r2_eval\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T06:15:45.750Z\", \"updated_at\": \"2026-05-19T08:42:24.182Z\", \"hypothesis\": \"D076 eval for 1.7B RSFT s43_r2 (Method A: s42 SFT adapter + s42 CED k=1 data, RSFT seed=43). 预期 ign_f1 接近 s42 RSFT (0.5122)，验证 1.7B RSFT 跨 seed 稳健性。\", \"parent\": \"plan019_1_7b_rsft_s43_r2\", \"metrics\": {\"ign_f1\": 0.5109, \"ign_precision\": 0.5186, \"ign_recall\": 0.5035, \"f1\": 0.5271, \"precision\": 0.5444, \"recall\": 0.5109, \"evi_precision\": 0.8218, \"evi_recall\": 0.834, \"evi_f1\": 0.8278, \"edcr\": 0.6245, \"evi_joint_precision\": 0.4336, \"evi_joint_recall\": 0.4221, \"evi_f1_joint\": 0.4278, \"format_compliance_rate\": 0.999, \"field_compliance_rate\": 0.7503, \"n_truncated\": 244, \"inference_time_seconds\": 8498.2}, \"conclusion\": \"success\"}, \"plan017_14b_sft\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T04:22:05.400Z\", \"updated_at\": \"2026-05-19T07:19:50.806Z\", \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 0.5457, \"eval_loss\": 0.6292}, \"hypothesis\": \"Scaling from Qwen3-8B to Qwen3-14B with LoRA SFT on the same DocRED faith-evidence IE data will improve extraction quality because the larger model has greater capacity to learn complex relation extraction patterns with evidence grounding.\"}, \"plan019_1_7b_rsft_s44_r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T04:26:18.370Z\", \"updated_at\": \"2026-05-19T06:17:08.769Z\", \"hypothesis\": \"D114 Method A: 1.7B RSFT k=1 s44 重跑。使用 s42 SFT adapter (sft_output_qwen3_1_7b_bf16) + s42 CED k=1 scored data, RSFT seed=44。验证 1.7B 尺度 RSFT 增益跨 seed 稳健性。\", \"parent\": \"plan019_1_7b_rsft_s44\", \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 0.5538, \"final_step\": 567, \"epoch\": 3, \"mean_token_accuracy\": 0.8706}}, \"plan019_1_7b_rsft_s43_r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T04:26:17.166Z\", \"updated_at\": \"2026-05-19T05:59:49.377Z\", \"hypothesis\": \"D114 Method A: 1.7B RSFT k=1 s43 重跑。使用 s42 SFT adapter (sft_output_qwen3_1_7b_bf16) + s42 CED k=1 scored data, RSFT seed=43。原始运行输出被误删(Worker B 误判)，需重新训练。验证 1.7B 尺度 RSFT 增益跨 seed 稳健性。\", \"parent\": \"plan019_1_7b_rsft_s43\", \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 0.5526}}, \"plan019_1_7b_rsft_s44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T03:02:05.852Z\", \"updated_at\": \"2026-05-19T05:11:17.769Z\", \"hypothesis\": \"1.7B RSFT k=1 s44 (Option A seed expansion): 复用 s42 SFT adapter + s42 CED k=1 scored data，只变 RSFT 训练 seed 为 44。验证 1.7B 尺度 RSFT 增益跨 seed 稳健性。\", \"parent\": \"plan019_1_7b_sft_s44\", \"conclusion\": \"failed\"}, \"plan019_1_7b_rsft_s43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T02:51:57.316Z\", \"updated_at\": \"2026-05-19T05:11:16.432Z\", \"hypothesis\": \"1.7B RSFT k=1 s43 (Option A seed expansion): 复用 s42 SFT adapter + s42 CED k=1 scored data，只变 RSFT 训练 seed 为 43。验证 1.7B 尺度 RSFT 增益跨 seed 稳健性。\", \"parent\": \"plan019_1_7b_sft_s43_r2\", \"conclusion\": \"failed\"}, \"plan019_8b_rsft_s44_eval\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T02:11:06.132Z\", \"updated_at\": \"2026-05-19T05:08:07.693Z\", \"hypothesis\": \"8B RSFT s44 eval (Option A seed expansion). 预期 ign_f1 接近 canonical s42 (0.5376)，验证 RSFT 增益在 8B 尺度跨 seed 稳定。\", \"parent\": \"plan019_8b_rsft_s44\", \"conclusion\": \"success\", \"metrics\": {\"ign_f1\": 0.5451, \"f1\": 0.562, \"evi_f1_tp\": 0.8145, \"evi_f1_dreeam\": 0.4472, \"edcr\": 0.6233, \"format_ok\": \"985/985\", \"truncated\": \"230/985\", \"predictions\": 16254}, \"notes\": \"Cron 误报 failed (submit_training_job 脚本路径不存在 EXIT_CODE=127)，但 Worker 已通过 Python 直接执行 eval 成功。结果在 /root/autodl-tmp/eval_results/rsft_8b_k1_s44_eval.log。已更正为 success。8B RSFT s44 ign_f1=0.5451 vs canonical s42 0.5376 (+0.75pp)，跨 seed 稳健。\"}, \"d112_rsft_s44_ced_score\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T03:18:56.333Z\", \"updated_at\": \"2026-05-19T04:41:13.613Z\", \"hypothesis\": \"D112 step 2: CED scoring + k=1 selection on SFT s44 generation candidates. 使用 NLI-DeBERTa 对 N=8 候选打分，format_w=0.2, f1_w=0.4, ced_w=0.4，top_k=1 筛选最优样本用于后续 RSFT 训练。\", \"parent\": \"d112_rsft_s44_gen_shard0\", \"notes\": \"retry #2 running normally. 10000/24216 records scored as of 11:50 UTC. ETA ~12:33 UTC. Previous run failed at 03:28 UTC (process dead before scoring started). Current run healthy, no errors in log.\", \"conclusion\": \"success\"}, \"d111_4b_sft_s42_reeval\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T22:06:04.423Z\", \"updated_at\": \"2026-05-19T03:54:03.116Z\", \"hypothesis\": \"Re-evaluating 4B SFT s42 with D076 standardized protocol to establish fair 3-seed comparison with s43 and s44. Previous s42 evaluations gave inconsistent results (0.4106/0.4036/0.3974), so re-running with identical protocol resolves this.\", \"metrics\": {\"ign_f1\": 0.3974, \"rel_f1\": 0.4049, \"evi_f1\": 0.7986, \"evi_f1_joint\": 0.3147, \"edcr\": 0.6982}, \"conclusion\": \"success\"}, \"d112_rsft_s44_gen_shard3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T00:44:31.524Z\", \"updated_at\": \"2026-05-19T03:17:28.913Z\", \"hypothesis\": \"D112 shard 3: 并行候选生成 (docs [2268:3027])，用 SFT s44 adapter 生成 N=8 RSFT 候选。\", \"conclusion\": \"success\"}, \"d112_rsft_s44_gen_shard1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T23:43:46.463Z\", \"updated_at\": \"2026-05-19T03:01:57.420Z\", \"hypothesis\": \"D112 shard 1: 并行候选生成 (docs [756:1512])，用 SFT s44 adapter 生成 N=8 RSFT 候选。\", \"parent\": \"\", \"conclusion\": \"success\"}, \"d112_rsft_s44_gen_shard2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T23:43:47.622Z\", \"updated_at\": \"2026-05-19T02:48:30.925Z\", \"hypothesis\": \"D112 shard 2: 并行候选生成 (docs [1512:2268])，用 SFT s44 adapter 生成 N=8 RSFT 候选。\", \"parent\": \"\", \"conclusion\": \"success\"}}, \"count\": 30, \"total\": 255, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.9409}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "39f8a4ed-6d6b-4c23-9e46-167a8118c922",
  "uuid": "d17d6016-4419-4de3-a9e4-1c7204a4bdea",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"d112_rsft_no_evidence_eval_r3\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"created_at\\\": \\\"2026-05-19T14:47:43.281Z\\\", \\\"updated_at\\\": \\\"2026-05-19T15:47:04.413Z\\\", \\\"hypothesis\\\": \\\"4B RSFT no-evidence eval r3 (D112 bf16 SFT s44 base): 移除 evidence 输出后测量 4B RSFT 的 evidence tax。对比 with-evidence 的 D112 RSFT ign_f1。r1/r2 因脚本路径错误失败 (EXIT_CODE=127)，r3 使用正确路径 scripts/seed_expansion/eval_4b_rsft_no_evidence.sh。\\\", \\\"parent\\\": \\\"d112_rsft_s44_eval_bf16\\\"}, \\\"plan019_8b_sft_s43_eval\\\": {\\\"status\\\": \\\"ANALYZING\\\", \\\"created_at\\\": \\\"2026-05-19T14:00:00.027Z\\\", \\\"updated_at\\\": \\\"2026-05-19T15:41:53.613Z\\\", \\\"hypothesis\\\": \\\"D076 eval for 8B SFT s43. 补齐第 3 个 8B SFT seed 的 eval 结果。8B SFT s42 ign_f1=0.5128, s44 ign_f1=0.4604. 3-seed mean 将决定 \\\\\\\"1.7B RSFT surpasses 8B SFT\\\\\\\" claim (Claim 3) 的统计力。\\\", \\\"parent\\\": \\\"plan019_8b_sft_s43\\\"}, \\\"plan019_1_7b_rsft_no_evidence_eval_2048\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"created_at\\\": \\\"2026-05-19T14:48:26.124Z\\\", \\\"updated_at\\\": \\\"2026-05-19T14:50:27.272Z\\\", \\\"hypothesis\\\": \\\"排除截断混淆后验证 1.7B RSFT negative evidence tax (-7.7pp) 是真实效应还是截断 artifact。原实验 max_new_tokens=1024 截断率 59.2% (583/985)，改用 2048 排除截断伪影。来源: Reviewer warning on plan019_1_7b_rsft_no_evidence_eval。\\\", \\\"parent\\\": \\\"plan019_1_7b_rsft_no_evidence_eval\\\"}, \\\"plan019_1_7b_rsft_no_evidence_eval\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-19T11:42:59.170Z\\\", \\\"updated_at\\\": \\\"2026-05-19T14:47:15.332Z\\\", \\\"hypothesis\\\": \\\"Removing evidence output at inference time should improve RE ign_f1 above 0.5122 (with-evidence baseline) for 1.7B RSFT, indicating an evidence tax where generating evidence hurts relation extraction performance\\\", \\\"metrics\\\": {\\\"ign_f1\\\": 0.4352, \\\"f1\\\": 0.4552, \\\"evi_f1_dreeam\\\": 0, \\\"evi_f1_tp\\\": 0, \\\"edcr\\\": 0, \\\"format_ok_rate\\\": 0.971, \\\"truncated_rate\\\": 0.592, \\\"predictions\\\": 25221}, \\\"conclusion\\\": \\\"killed\\\", \\\"notes\\\": \\\"Evidence tax measurement for 1.7B RSFT s42. Hypothesis rejected: no-evidence ign_f1=0.4352 < with-evidence ign_f1=0.5122, a DECREASE of 7.70pp. Removing evidence hurts 1.7B RE performance — evidence generation acts as beneficial chain-of-thought. Contrast with 14B SFT where evidence tax ≈ 0.03pp (nearly zero). This suggests smaller models rely more on evidence reasoning to achieve good RE. High truncation rate (59.2%) but 97.1% format compliance. No W&B run.\\\"}, \\\"plan019_8b_sft_s43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-19T12:04:31.830Z\\\", \\\"updated_at\\\": \\\"2026-05-19T14:01:26.124Z\\\", \\\"hypothesis\\\": \\\"8B SFT seed=43: 补齐第 3 seed 改善 '1.7B RSFT surpasses 8B SFT' claim 统计力（当前 p≈0.20，瓶颈在 8B SFT 仅 2 seeds）。Reviewer 建议，对应 plan_019 Claim 3。\\\", \\\"parent\\\": \\\"plan019_8b_sft_s44\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"train_loss\\\": 0.5684, \\\"eval_loss\\\": 0.719, \\\"eval_mean_token_accuracy\\\": 0.8378, \\\"train_runtime_s\\\": 6639, \\\"epochs\\\": 3, \\\"train_steps\\\": 570}}, \\\"plan017_14b_sft_eval_r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-19T08:51:48.518Z\\\", \\\"updated_at\\\": \\\"2026-05-19T13:58:13.384Z\\\", \\\"hypothesis\\\": \\\"D076 eval for 14B SFT baseline (bf16, --no-quantize). 修正 r1 的 D076 违规（r1 用了 int8 量化）。14B 是第 4 个 scale 档，SFT baseline 用于计算 RSFT 增益和 evidence tax。预期 ign_f1 高于 8B SFT mean (0.4866)。\\\", \\\"parent\\\": \\\"plan017_14b_sft\\\", \\\"metrics\\\": {\\\"ign_f1\\\": 0.5507, \\\"ign_precision\\\": 0.5268, \\\"ign_recall\\\": 0.5768, \\\"f1\\\": 0.5611, \\\"precision\\\": 0.5481, \\\"recall\\\": 0.5748, \\\"format_compliance_rate\\\": 1, \\\"field_compliance_rate\\\": 0.8589, \\\"evidence_format_rate\\\": 0.8589, \\\"n_truncated\\\": 139, \\\"n_total\\\": 985, \\\"n_parseable\\\": 985, \\\"n_predictions\\\": 14081, \\\"inference_time_seconds\\\": 18011.3, \\\"evi_precision\\\": 0.8197, \\\"evi_recall\\\": 0.839, \\\"evi_f1\\\": 0.8292, \\\"evi_f1_joint\\\": 0.4453, \\\"evi_joint_precision\\\": 0.4174, \\\"evi_joint_recall\\\": 0.4772, \\\"edcr\\\": 0.597}, \\\"conclusion\\\": \\\"success\\\"}, \\\"plan019_8b_rsft_no_evidence_eval_r2\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"created_at\\\": \\\"2026-05-19T13:44:38.870Z\\\", \\\"updated_at\\\": \\\"2026-05-19T13:54:52.747Z\\\", \\\"hypothesis\\\": \\\"8B RSFT no-evidence eval r2: 移除 evidence 输出后测量 8B RSFT 的 evidence tax。8B RSFT with-evidence mean ign_f1=0.5414 (s42=0.5376, s44=0.5451)。若 no-evidence ign_f1 > with-evidence，证实 evidence 生成对 8B RE 的性能代价；与 1.7B/4B/14B evidence tax 配合构建跨尺度 scaling curve (Claim 3)。修正 r1 的 cuda:2 冲突问题，改用 cuda:0。\\\", \\\"parent\\\": \\\"plan019_8b_rsft_no_evidence_eval\\\"}, \\\"d112_rsft_no_evidence_eval_r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-19T13:41:03.808Z\\\", \\\"updated_at\\\": \\\"2026-05-19T13:45:20.995Z\\\", \\\"hypothesis\\\": \\\"4B RSFT no-evidence eval (D112 bf16 SFT s44 base): 移除 evidence 输出后测量 4B RSFT 的 evidence tax。对比 with-evidence 的 canonical 4B RSFT ign_f1，验证 evidence 生成对 4B RE 性能的代价。与 1.7B/8B/14B no-evidence eval 配合构建跨尺度 evidence tax scaling curve (Claim 3)。\\\", \\\"parent\\\": \\\"d112_rsft_s44_eval_bf16\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"plan019_8b_rsft_no_evidence_eval\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-19T13:12:23.195Z\\\", \\\"updated_at\\\": \\\"2026-05-19T13:44:36.625Z\\\", \\\"hypothesis\\\": \\\"8B RSFT no-evidence eval: 移除 evidence 输出后测量 8B RSFT 的 evidence tax。8B RSFT with-evidence mean ign_f1=0.5414 (s42=0.5376, s44=0.5451)。若 no-evidence ign_f1 > with-evidence，证实 evidence 生成对 8B RE 的性能代价；与 1.7B/4B/14B evidence tax 配合构建跨尺度 scaling curve (Claim 3)。\\\", \\\"parent\\\": \\\"plan019_8b_rsft_s44_eval\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"d112_rsft_no_evidence_eval\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-19T13:19:08.763Z\\\", \\\"updated_at\\\": \\\"2026-05-19T13:41:48.937Z\\\", \\\"hypothesis\\\": \\\"4B RSFT no-evidence eval (D112 bf16 SFT s44 base): 移除 evidence 输出后测量 4B RSFT 的 evidence tax。对比 with-evidence 的 canonical 4B RSFT ign_f1，验证 evidence 生成对 4B RE 性能的代价。与 1.7B/8B/14B no-evidence eval 配合构建跨尺度 evidence tax scaling curve (Claim 3)。\\\", \\\"parent\\\": \\\"d112_rsft_s44_eval_bf16\\\", \\\"conclusion\\\": \\\"failed\\\", \\\"notes\\\": \\\"EXIT_CODE=127 (command not found), wall_clock=17s. fix_worker_id: worker_diagnose_d112_rsft_no_evidence_eval_20260519T134139. 诊断中。\\\"}, \\\"d112_rsft_s44_eval_bf16\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"created_at\\\": \\\"2026-05-19T13:04:19.692Z\\\", \\\"updated_at\\\": \\\"2026-05-19T13:16:48.504Z\\\", \\\"hypothesis\\\": \\\"D112 step 4 bf16: D076 eval for RSFT trained on SFT s44 base with CED k=1 scored data (bf16 LoRA). 修正原 d112_rsft_s44_eval 的 QLoRA confound。预期 ign_f1 > 0.4734 (SFT s44 baseline)。\\\", \\\"parent\\\": \\\"d112_rsft_s44_train_bf16\\\"}, \\\"d112_rsft_s44_train_bf16\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-19T11:19:27.034Z\\\", \\\"updated_at\\\": \\\"2026-05-19T13:04:56.446Z\\\", \\\"hypothesis\\\": \\\"D112 step 3 bf16 重跑：RSFT training on SFT s44 base using CED k=1 scored data，使用 bf16 LoRA（非 QLoRA）与其他所有 RSFT 实验一致。修正原 d112_rsft_s44_train 的 QLoRA confound（--quantize 导致 adapter 适应 4-bit 量化误差，bf16 eval 下 ign_f1=0.2181 灾难性崩溃）。\\\", \\\"parent\\\": \\\"\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"plan017_14b_sft_no_evidence_eval_r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-19T08:51:50.451Z\\\", \\\"updated_at\\\": \\\"2026-05-19T12:57:54.516Z\\\", \\\"hypothesis\\\": \\\"14B SFT no-evidence eval (bf16, --no-quantize). 修正 r1 的 D076 违规。测量 14B SFT 在不提供 evidence 时的 ign_f1，用于计算 evidence tax (Claim 3)。\\\", \\\"parent\\\": \\\"plan017_14b_sft\\\", \\\"metrics\\\": {\\\"ign_f1\\\": 0.551, \\\"ign_precision\\\": 0.5149, \\\"ign_recall\\\": 0.5926, \\\"f1\\\": 0.5649, \\\"precision\\\": 0.5386, \\\"recall\\\": 0.5939, \\\"format_compliance_rate\\\": 0.9868, \\\"n_truncated\\\": 105, \\\"n_predictions\\\": 15605, \\\"inference_time_seconds\\\": 14497.8}, \\\"conclusion\\\": \\\"success\\\"}, \\\"d112_rsft_s44_eval\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-19T07:34:55.266Z\\\", \\\"updated_at\\\": \\\"2026-05-19T12:02:10.888Z\\\", \\\"hypothesis\\\": \\\"D112 step 4: D076 eval for RSFT trained on SFT s44 base with CED k=1 scored data. 验证 RSFT 在最强 SFT seed (s44, ign_f1=0.4734) 上的泛化效果。预期 ign_f1 > 0.4734 (SFT s44 baseline)。\\\", \\\"parent\\\": \\\"d112_rsft_s44_train\\\", \\\"conclusion\\\": \\\"failed\\\", \\\"metrics\\\": {\\\"ign_f1\\\": 0.2181, \\\"note\\\": \\\"INVALID: QLoRA confound — adapter trained on 4-bit quantized backbone evaluated in bf16\\\"}}, \\\"plan019_1_7b_rsft_s44_r2_eval\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-19T08:43:01.975Z\\\", \\\"updated_at\\\": \\\"2026-05-19T12:00:32.897Z\\\", \\\"hypothesis\\\": \\\"D076 eval for 1.7B RSFT s44_r2 (Method A: s42 SFT adapter + s42 CED k=1 data, RSFT seed=44). 预期 ign_f1 接近 s42 (0.5122) 和 s43 (0.5109)，完成 1.7B 3-seed RSFT 统计。\\\", \\\"parent\\\": \\\"plan019_1_7b_rsft_s44_r2\\\", \\\"metrics\\\": {\\\"ign_f1\\\": 0.5125, \\\"ign_precision\\\": 0.5173, \\\"ign_recall\\\": 0.5078, \\\"f1\\\": 0.5294, \\\"precision\\\": 0.5434, \\\"recall\\\": 0.5162, \\\"evi_precision\\\": 0.815, \\\"evi_recall\\\": 0.8387, \\\"evi_f1\\\": 0.8267, \\\"edcr\\\": 0.6181, \\\"evi_joint_precision\\\": 0.4284, \\\"evi_joint_recall\\\": 0.4294, \\\"evi_f1_joint\\\": 0.4289, \\\"format_compliance_rate\\\": 0.999, \\\"field_compliance_rate\\\": 0.7543, \\\"n_truncated\\\": 240, \\\"inference_time_seconds\\\": 8615.6}, \\\"conclusion\\\": \\\"success\\\"}, \\\"d112_rsft_s44_train\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-19T04:33:11.623Z\\\", \\\"updated_at\\\": \\\"2026-05-19T11:18:57.557Z\\\", \\\"hypothesis\\\": \\\"D112 step 3: RSFT training on SFT s44 base using CED k=1 scored data. 在最强 SFT seed (s44, ign_f1=0.4734) 上验证 RSFT 效果，参数与 canonical s42 RSFT 完全一致。\\\", \\\"parent\\\": \\\"d112_rsft_s44_ced_score\\\", \\\"conclusion\\\": \\\"failed\\\", \\\"metrics\\\": {\\\"train_loss\\\": 0.6488, \\\"global_step\\\": 567}}, \\\"plan017_14b_sft_eval\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-19T07:23:43.367Z\\\", \\\"updated_at\\\": \\\"2026-05-19T08:54:24.083Z\\\", \\\"hypothesis\\\": \\\"D076 eval for 14B SFT baseline. 14B 是第 4 个 scale 档（1.7B/4B/8B/14B），SFT baseline 用于计算 RSFT 增益和 evidence tax。预期 ign_f1 高于 8B SFT mean (0.4866)。\\\", \\\"parent\\\": \\\"plan017_14b_sft\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"plan017_14b_sft_no_evidence_eval\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-19T07:23:46.290Z\\\", \\\"updated_at\\\": \\\"2026-05-19T08:49:48.692Z\\\", \\\"hypothesis\\\": \\\"14B SFT no-evidence eval: 测量 14B SFT 在不提供 evidence 时的 ign_f1，用于计算 evidence tax (Claim 3)。与 4B evidence tax (D107: 47.21% vs 39.74%) 对比，验证 scale-dependent evidence tax 趋势。\\\", \\\"parent\\\": \\\"plan017_14b_sft\\\", \\\"conclusion\\\": \\\"killed\\\"}, \\\"plan019_1_7b_rsft_s43_r2_eval\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-19T06:15:45.750Z\\\", \\\"updated_at\\\": \\\"2026-05-19T08:42:24.182Z\\\", \\\"hypothesis\\\": \\\"D076 eval for 1.7B RSFT s43_r2 (Method A: s42 SFT adapter + s42 CED k=1 data, RSFT seed=43). 预期 ign_f1 接近 s42 RSFT (0.5122)，验证 1.7B RSFT 跨 seed 稳健性。\\\", \\\"parent\\\": \\\"plan019_1_7b_rsft_s43_r2\\\", \\\"metrics\\\": {\\\"ign_f1\\\": 0.5109, \\\"ign_precision\\\": 0.5186, \\\"ign_recall\\\": 0.5035, \\\"f1\\\": 0.5271, \\\"precision\\\": 0.5444, \\\"recall\\\": 0.5109, \\\"evi_precision\\\": 0.8218, \\\"evi_recall\\\": 0.834, \\\"evi_f1\\\": 0.8278, \\\"edcr\\\": 0.6245, \\\"evi_joint_precision\\\": 0.4336, \\\"evi_joint_recall\\\": 0.4221, \\\"evi_f1_joint\\\": 0.4278, \\\"format_compliance_rate\\\": 0.999, \\\"field_compliance_rate\\\": 0.7503, \\\"n_truncated\\\": 244, \\\"inference_time_seconds\\\": 8498.2}, \\\"conclusion\\\": \\\"success\\\"}, \\\"plan017_14b_sft\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-19T04:22:05.400Z\\\", \\\"updated_at\\\": \\\"2026-05-19T07:19:50.806Z\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"train_loss\\\": 0.5457, \\\"eval_loss\\\": 0.6292}, \\\"hypothesis\\\": \\\"Scaling from Qwen3-8B to Qwen3-14B with LoRA SFT on the same DocRED faith-evidence IE data will improve extraction quality because the larger model has greater capacity to learn complex relation extraction patterns with evidence grounding.\\\"}, \\\"plan019_1_7b_rsft_s44_r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-19T04:26:18.370Z\\\", \\\"updated_at\\\": \\\"2026-05-19T06:17:08.769Z\\\", \\\"hypothesis\\\": \\\"D114 Method A: 1.7B RSFT k=1 s44 重跑。使用 s42 SFT adapter (sft_output_qwen3_1_7b_bf16) + s42 CED k=1 scored data, RSFT seed=44。验证 1.7B 尺度 RSFT 增益跨 seed 稳健性。\\\", \\\"parent\\\": \\\"plan019_1_7b_rsft_s44\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"train_loss\\\": 0.5538, \\\"final_step\\\": 567, \\\"epoch\\\": 3, \\\"mean_token_accuracy\\\": 0.8706}}, \\\"plan019_1_7b_rsft_s43_r2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-19T04:26:17.166Z\\\", \\\"updated_at\\\": \\\"2026-05-19T05:59:49.377Z\\\", \\\"hypothesis\\\": \\\"D114 Method A: 1.7B RSFT k=1 s43 重跑。使用 s42 SFT adapter (sft_output_qwen3_1_7b_bf16) + s42 CED k=1 scored data, RSFT seed=43。原始运行输出被误删(Worker B 误判)，需重新训练。验证 1.7B 尺度 RSFT 增益跨 seed 稳健性。\\\", \\\"parent\\\": \\\"plan019_1_7b_rsft_s43\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"train_loss\\\": 0.5526}}, \\\"plan019_1_7b_rsft_s44\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-19T03:02:05.852Z\\\", \\\"updated_at\\\": \\\"2026-05-19T05:11:17.769Z\\\", \\\"hypothesis\\\": \\\"1.7B RSFT k=1 s44 (Option A seed expansion): 复用 s42 SFT adapter + s42 CED k=1 scored data，只变 RSFT 训练 seed 为 44。验证 1.7B 尺度 RSFT 增益跨 seed 稳健性。\\\", \\\"parent\\\": \\\"plan019_1_7b_sft_s44\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"plan019_1_7b_rsft_s43\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-19T02:51:57.316Z\\\", \\\"updated_at\\\": \\\"2026-05-19T05:11:16.432Z\\\", \\\"hypothesis\\\": \\\"1.7B RSFT k=1 s43 (Option A seed expansion): 复用 s42 SFT adapter + s42 CED k=1 scored data，只变 RSFT 训练 seed 为 43。验证 1.7B 尺度 RSFT 增益跨 seed 稳健性。\\\", \\\"parent\\\": \\\"plan019_1_7b_sft_s43_r2\\\", \\\"conclusion\\\": \\\"failed\\\"}, \\\"plan019_8b_rsft_s44_eval\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-19T02:11:06.132Z\\\", \\\"updated_at\\\": \\\"2026-05-19T05:08:07.693Z\\\", \\\"hypothesis\\\": \\\"8B RSFT s44 eval (Option A seed expansion). 预期 ign_f1 接近 canonical s42 (0.5376)，验证 RSFT 增益在 8B 尺度跨 seed 稳定。\\\", \\\"parent\\\": \\\"plan019_8b_rsft_s44\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"ign_f1\\\": 0.5451, \\\"f1\\\": 0.562, \\\"evi_f1_tp\\\": 0.8145, \\\"evi_f1_dreeam\\\": 0.4472, \\\"edcr\\\": 0.6233, \\\"format_ok\\\": \\\"985/985\\\", \\\"truncated\\\": \\\"230/985\\\", \\\"predictions\\\": 16254}, \\\"notes\\\": \\\"Cron 误报 failed (submit_training_job 脚本路径不存在 EXIT_CODE=127)，但 Worker 已通过 Python 直接执行 eval 成功。结果在 /root/autodl-tmp/eval_results/rsft_8b_k1_s44_eval.log。已更正为 success。8B RSFT s44 ign_f1=0.5451 vs canonical s42 0.5376 (+0.75pp)，跨 seed 稳健。\\\"}, \\\"d112_rsft_s44_ced_score\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-19T03:18:56.333Z\\\", \\\"updated_at\\\": \\\"2026-05-19T04:41:13.613Z\\\", \\\"hypothesis\\\": \\\"D112 step 2: CED scoring + k=1 selection on SFT s44 generation candidates. 使用 NLI-DeBERTa 对 N=8 候选打分，format_w=0.2, f1_w=0.4, ced_w=0.4，top_k=1 筛选最优样本用于后续 RSFT 训练。\\\", \\\"parent\\\": \\\"d112_rsft_s44_gen_shard0\\\", \\\"notes\\\": \\\"retry #2 running normally. 10000/24216 records scored as of 11:50 UTC. ETA ~12:33 UTC. Previous run failed at 03:28 UTC (process dead before scoring started). Current run healthy, no errors in log.\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"d111_4b_sft_s42_reeval\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-18T22:06:04.423Z\\\", \\\"updated_at\\\": \\\"2026-05-19T03:54:03.116Z\\\", \\\"hypothesis\\\": \\\"Re-evaluating 4B SFT s42 with D076 standardized protocol to establish fair 3-seed comparison with s43 and s44. Previous s42 evaluations gave inconsistent results (0.4106/0.4036/0.3974), so re-running with identical protocol resolves this.\\\", \\\"metrics\\\": {\\\"ign_f1\\\": 0.3974, \\\"rel_f1\\\": 0.4049, \\\"evi_f1\\\": 0.7986, \\\"evi_f1_joint\\\": 0.3147, \\\"edcr\\\": 0.6982}, \\\"conclusion\\\": \\\"success\\\"}, \\\"d112_rsft_s44_gen_shard3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-19T00:44:31.524Z\\\", \\\"updated_at\\\": \\\"2026-05-19T03:17:28.913Z\\\", \\\"hypothesis\\\": \\\"D112 shard 3: 并行候选生成 (docs [2268:3027])，用 SFT s44 adapter 生成 N=8 RSFT 候选。\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"d112_rsft_s44_gen_shard1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-18T23:43:46.463Z\\\", \\\"updated_at\\\": \\\"2026-05-19T03:01:57.420Z\\\", \\\"hypothesis\\\": \\\"D112 shard 1: 并行候选生成 (docs [756:1512])，用 SFT s44 adapter 生成 N=8 RSFT 候选。\\\", \\\"parent\\\": \\\"\\\", \\\"conclusion\\\": \\\"success\\\"}, \\\"d112_rsft_s44_gen_shard2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"created_at\\\": \\\"2026-05-18T23:43:47.622Z\\\", \\\"updated_at\\\": \\\"2026-05-19T02:48:30.925Z\\\", \\\"hypothesis\\\": \\\"D112 shard 2: 并行候选生成 (docs [1512:2268])，用 SFT s44 adapter 生成 N=8 RSFT 候选。\\\", \\\"parent\\\": \\\"\\\", \\\"conclusion\\\": \\\"success\\\"}}, \\\"count\\\": 30, \\\"total\\\": 255, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.9409}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"d112_rsft_no_evidence_eval_r3\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-19T14:47:43.281Z\", \"updated_at\": \"2026-05-19T15:47:04.413Z\", \"hypothesis\": \"4B RSFT no-evidence eval r3 (D112 bf16 SFT s44 base): 移除 evidence 输出后测量 4B RSFT 的 evidence tax。对比 with-evidence 的 D112 RSFT ign_f1。r1/r2 因脚本路径错误失败 (EXIT_CODE=127)，r3 使用正确路径 scripts/seed_expansion/eval_4b_rsft_no_evidence.sh。\", \"parent\": \"d112_rsft_s44_eval_bf16\"}, \"plan019_8b_sft_s43_eval\": {\"status\": \"ANALYZING\", \"created_at\": \"2026-05-19T14:00:00.027Z\", \"updated_at\": \"2026-05-19T15:41:53.613Z\", \"hypothesis\": \"D076 eval for 8B SFT s43. 补齐第 3 个 8B SFT seed 的 eval 结果。8B SFT s42 ign_f1=0.5128, s44 ign_f1=0.4604. 3-seed mean 将决定 \\\"1.7B RSFT surpasses 8B SFT\\\" claim (Claim 3) 的统计力。\", \"parent\": \"plan019_8b_sft_s43\"}, \"plan019_1_7b_rsft_no_evidence_eval_2048\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-19T14:48:26.124Z\", \"updated_at\": \"2026-05-19T14:50:27.272Z\", \"hypothesis\": \"排除截断混淆后验证 1.7B RSFT negative evidence tax (-7.7pp) 是真实效应还是截断 artifact。原实验 max_new_tokens=1024 截断率 59.2% (583/985)，改用 2048 排除截断伪影。来源: Reviewer warning on plan019_1_7b_rsft_no_evidence_eval。\", \"parent\": \"plan019_1_7b_rsft_no_evidence_eval\"}, \"plan019_1_7b_rsft_no_evidence_eval\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T11:42:59.170Z\", \"updated_at\": \"2026-05-19T14:47:15.332Z\", \"hypothesis\": \"Removing evidence output at inference time should improve RE ign_f1 above 0.5122 (with-evidence baseline) for 1.7B RSFT, indicating an evidence tax where generating evidence hurts relation extraction performance\", \"metrics\": {\"ign_f1\": 0.4352, \"f1\": 0.4552, \"evi_f1_dreeam\": 0, \"evi_f1_tp\": 0, \"edcr\": 0, \"format_ok_rate\": 0.971, \"truncated_rate\": 0.592, \"predictions\": 25221}, \"conclusion\": \"killed\", \"notes\": \"Evidence tax measurement for 1.7B RSFT s42. Hypothesis rejected: no-evidence ign_f1=0.4352 < with-evidence ign_f1=0.5122, a DECREASE of 7.70pp. Removing evidence hurts 1.7B RE performance — evidence generation acts as beneficial chain-of-thought. Contrast with 14B SFT where evidence tax ≈ 0.03pp (nearly zero). This suggests smaller models rely more on evidence reasoning to achieve good RE. High truncation rate (59.2%) but 97.1% format compliance. No W&B run.\"}, \"plan019_8b_sft_s43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T12:04:31.830Z\", \"updated_at\": \"2026-05-19T14:01:26.124Z\", \"hypothesis\": \"8B SFT seed=43: 补齐第 3 seed 改善 '1.7B RSFT surpasses 8B SFT' claim 统计力（当前 p≈0.20，瓶颈在 8B SFT 仅 2 seeds）。Reviewer 建议，对应 plan_019 Claim 3。\", \"parent\": \"plan019_8b_sft_s44\", \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 0.5684, \"eval_loss\": 0.719, \"eval_mean_token_accuracy\": 0.8378, \"train_runtime_s\": 6639, \"epochs\": 3, \"train_steps\": 570}}, \"plan017_14b_sft_eval_r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T08:51:48.518Z\", \"updated_at\": \"2026-05-19T13:58:13.384Z\", \"hypothesis\": \"D076 eval for 14B SFT baseline (bf16, --no-quantize). 修正 r1 的 D076 违规（r1 用了 int8 量化）。14B 是第 4 个 scale 档，SFT baseline 用于计算 RSFT 增益和 evidence tax。预期 ign_f1 高于 8B SFT mean (0.4866)。\", \"parent\": \"plan017_14b_sft\", \"metrics\": {\"ign_f1\": 0.5507, \"ign_precision\": 0.5268, \"ign_recall\": 0.5768, \"f1\": 0.5611, \"precision\": 0.5481, \"recall\": 0.5748, \"format_compliance_rate\": 1, \"field_compliance_rate\": 0.8589, \"evidence_format_rate\": 0.8589, \"n_truncated\": 139, \"n_total\": 985, \"n_parseable\": 985, \"n_predictions\": 14081, \"inference_time_seconds\": 18011.3, \"evi_precision\": 0.8197, \"evi_recall\": 0.839, \"evi_f1\": 0.8292, \"evi_f1_joint\": 0.4453, \"evi_joint_precision\": 0.4174, \"evi_joint_recall\": 0.4772, \"edcr\": 0.597}, \"conclusion\": \"success\"}, \"plan019_8b_rsft_no_evidence_eval_r2\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-19T13:44:38.870Z\", \"updated_at\": \"2026-05-19T13:54:52.747Z\", \"hypothesis\": \"8B RSFT no-evidence eval r2: 移除 evidence 输出后测量 8B RSFT 的 evidence tax。8B RSFT with-evidence mean ign_f1=0.5414 (s42=0.5376, s44=0.5451)。若 no-evidence ign_f1 > with-evidence，证实 evidence 生成对 8B RE 的性能代价；与 1.7B/4B/14B evidence tax 配合构建跨尺度 scaling curve (Claim 3)。修正 r1 的 cuda:2 冲突问题，改用 cuda:0。\", \"parent\": \"plan019_8b_rsft_no_evidence_eval\"}, \"d112_rsft_no_evidence_eval_r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T13:41:03.808Z\", \"updated_at\": \"2026-05-19T13:45:20.995Z\", \"hypothesis\": \"4B RSFT no-evidence eval (D112 bf16 SFT s44 base): 移除 evidence 输出后测量 4B RSFT 的 evidence tax。对比 with-evidence 的 canonical 4B RSFT ign_f1，验证 evidence 生成对 4B RE 性能的代价。与 1.7B/8B/14B no-evidence eval 配合构建跨尺度 evidence tax scaling curve (Claim 3)。\", \"parent\": \"d112_rsft_s44_eval_bf16\", \"conclusion\": \"failed\"}, \"plan019_8b_rsft_no_evidence_eval\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T13:12:23.195Z\", \"updated_at\": \"2026-05-19T13:44:36.625Z\", \"hypothesis\": \"8B RSFT no-evidence eval: 移除 evidence 输出后测量 8B RSFT 的 evidence tax。8B RSFT with-evidence mean ign_f1=0.5414 (s42=0.5376, s44=0.5451)。若 no-evidence ign_f1 > with-evidence，证实 evidence 生成对 8B RE 的性能代价；与 1.7B/4B/14B evidence tax 配合构建跨尺度 scaling curve (Claim 3)。\", \"parent\": \"plan019_8b_rsft_s44_eval\", \"conclusion\": \"killed\"}, \"d112_rsft_no_evidence_eval\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T13:19:08.763Z\", \"updated_at\": \"2026-05-19T13:41:48.937Z\", \"hypothesis\": \"4B RSFT no-evidence eval (D112 bf16 SFT s44 base): 移除 evidence 输出后测量 4B RSFT 的 evidence tax。对比 with-evidence 的 canonical 4B RSFT ign_f1，验证 evidence 生成对 4B RE 性能的代价。与 1.7B/8B/14B no-evidence eval 配合构建跨尺度 evidence tax scaling curve (Claim 3)。\", \"parent\": \"d112_rsft_s44_eval_bf16\", \"conclusion\": \"failed\", \"notes\": \"EXIT_CODE=127 (command not found), wall_clock=17s. fix_worker_id: worker_diagnose_d112_rsft_no_evidence_eval_20260519T134139. 诊断中。\"}, \"d112_rsft_s44_eval_bf16\": {\"status\": \"RUNNING\", \"created_at\": \"2026-05-19T13:04:19.692Z\", \"updated_at\": \"2026-05-19T13:16:48.504Z\", \"hypothesis\": \"D112 step 4 bf16: D076 eval for RSFT trained on SFT s44 base with CED k=1 scored data (bf16 LoRA). 修正原 d112_rsft_s44_eval 的 QLoRA confound。预期 ign_f1 > 0.4734 (SFT s44 baseline)。\", \"parent\": \"d112_rsft_s44_train_bf16\"}, \"d112_rsft_s44_train_bf16\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T11:19:27.034Z\", \"updated_at\": \"2026-05-19T13:04:56.446Z\", \"hypothesis\": \"D112 step 3 bf16 重跑：RSFT training on SFT s44 base using CED k=1 scored data，使用 bf16 LoRA（非 QLoRA）与其他所有 RSFT 实验一致。修正原 d112_rsft_s44_train 的 QLoRA confound（--quantize 导致 adapter 适应 4-bit 量化误差，bf16 eval 下 ign_f1=0.2181 灾难性崩溃）。\", \"parent\": \"\", \"conclusion\": \"success\"}, \"plan017_14b_sft_no_evidence_eval_r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T08:51:50.451Z\", \"updated_at\": \"2026-05-19T12:57:54.516Z\", \"hypothesis\": \"14B SFT no-evidence eval (bf16, --no-quantize). 修正 r1 的 D076 违规。测量 14B SFT 在不提供 evidence 时的 ign_f1，用于计算 evidence tax (Claim 3)。\", \"parent\": \"plan017_14b_sft\", \"metrics\": {\"ign_f1\": 0.551, \"ign_precision\": 0.5149, \"ign_recall\": 0.5926, \"f1\": 0.5649, \"precision\": 0.5386, \"recall\": 0.5939, \"format_compliance_rate\": 0.9868, \"n_truncated\": 105, \"n_predictions\": 15605, \"inference_time_seconds\": 14497.8}, \"conclusion\": \"success\"}, \"d112_rsft_s44_eval\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T07:34:55.266Z\", \"updated_at\": \"2026-05-19T12:02:10.888Z\", \"hypothesis\": \"D112 step 4: D076 eval for RSFT trained on SFT s44 base with CED k=1 scored data. 验证 RSFT 在最强 SFT seed (s44, ign_f1=0.4734) 上的泛化效果。预期 ign_f1 > 0.4734 (SFT s44 baseline)。\", \"parent\": \"d112_rsft_s44_train\", \"conclusion\": \"failed\", \"metrics\": {\"ign_f1\": 0.2181, \"note\": \"INVALID: QLoRA confound — adapter trained on 4-bit quantized backbone evaluated in bf16\"}}, \"plan019_1_7b_rsft_s44_r2_eval\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T08:43:01.975Z\", \"updated_at\": \"2026-05-19T12:00:32.897Z\", \"hypothesis\": \"D076 eval for 1.7B RSFT s44_r2 (Method A: s42 SFT adapter + s42 CED k=1 data, RSFT seed=44). 预期 ign_f1 接近 s42 (0.5122) 和 s43 (0.5109)，完成 1.7B 3-seed RSFT 统计。\", \"parent\": \"plan019_1_7b_rsft_s44_r2\", \"metrics\": {\"ign_f1\": 0.5125, \"ign_precision\": 0.5173, \"ign_recall\": 0.5078, \"f1\": 0.5294, \"precision\": 0.5434, \"recall\": 0.5162, \"evi_precision\": 0.815, \"evi_recall\": 0.8387, \"evi_f1\": 0.8267, \"edcr\": 0.6181, \"evi_joint_precision\": 0.4284, \"evi_joint_recall\": 0.4294, \"evi_f1_joint\": 0.4289, \"format_compliance_rate\": 0.999, \"field_compliance_rate\": 0.7543, \"n_truncated\": 240, \"inference_time_seconds\": 8615.6}, \"conclusion\": \"success\"}, \"d112_rsft_s44_train\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T04:33:11.623Z\", \"updated_at\": \"2026-05-19T11:18:57.557Z\", \"hypothesis\": \"D112 step 3: RSFT training on SFT s44 base using CED k=1 scored data. 在最强 SFT seed (s44, ign_f1=0.4734) 上验证 RSFT 效果，参数与 canonical s42 RSFT 完全一致。\", \"parent\": \"d112_rsft_s44_ced_score\", \"conclusion\": \"failed\", \"metrics\": {\"train_loss\": 0.6488, \"global_step\": 567}}, \"plan017_14b_sft_eval\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T07:23:43.367Z\", \"updated_at\": \"2026-05-19T08:54:24.083Z\", \"hypothesis\": \"D076 eval for 14B SFT baseline. 14B 是第 4 个 scale 档（1.7B/4B/8B/14B），SFT baseline 用于计算 RSFT 增益和 evidence tax。预期 ign_f1 高于 8B SFT mean (0.4866)。\", \"parent\": \"plan017_14b_sft\", \"conclusion\": \"killed\"}, \"plan017_14b_sft_no_evidence_eval\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T07:23:46.290Z\", \"updated_at\": \"2026-05-19T08:49:48.692Z\", \"hypothesis\": \"14B SFT no-evidence eval: 测量 14B SFT 在不提供 evidence 时的 ign_f1，用于计算 evidence tax (Claim 3)。与 4B evidence tax (D107: 47.21% vs 39.74%) 对比，验证 scale-dependent evidence tax 趋势。\", \"parent\": \"plan017_14b_sft\", \"conclusion\": \"killed\"}, \"plan019_1_7b_rsft_s43_r2_eval\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T06:15:45.750Z\", \"updated_at\": \"2026-05-19T08:42:24.182Z\", \"hypothesis\": \"D076 eval for 1.7B RSFT s43_r2 (Method A: s42 SFT adapter + s42 CED k=1 data, RSFT seed=43). 预期 ign_f1 接近 s42 RSFT (0.5122)，验证 1.7B RSFT 跨 seed 稳健性。\", \"parent\": \"plan019_1_7b_rsft_s43_r2\", \"metrics\": {\"ign_f1\": 0.5109, \"ign_precision\": 0.5186, \"ign_recall\": 0.5035, \"f1\": 0.5271, \"precision\": 0.5444, \"recall\": 0.5109, \"evi_precision\": 0.8218, \"evi_recall\": 0.834, \"evi_f1\": 0.8278, \"edcr\": 0.6245, \"evi_joint_precision\": 0.4336, \"evi_joint_recall\": 0.4221, \"evi_f1_joint\": 0.4278, \"format_compliance_rate\": 0.999, \"field_compliance_rate\": 0.7503, \"n_truncated\": 244, \"inference_time_seconds\": 8498.2}, \"conclusion\": \"success\"}, \"plan017_14b_sft\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T04:22:05.400Z\", \"updated_at\": \"2026-05-19T07:19:50.806Z\", \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 0.5457, \"eval_loss\": 0.6292}, \"hypothesis\": \"Scaling from Qwen3-8B to Qwen3-14B with LoRA SFT on the same DocRED faith-evidence IE data will improve extraction quality because the larger model has greater capacity to learn complex relation extraction patterns with evidence grounding.\"}, \"plan019_1_7b_rsft_s44_r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T04:26:18.370Z\", \"updated_at\": \"2026-05-19T06:17:08.769Z\", \"hypothesis\": \"D114 Method A: 1.7B RSFT k=1 s44 重跑。使用 s42 SFT adapter (sft_output_qwen3_1_7b_bf16) + s42 CED k=1 scored data, RSFT seed=44。验证 1.7B 尺度 RSFT 增益跨 seed 稳健性。\", \"parent\": \"plan019_1_7b_rsft_s44\", \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 0.5538, \"final_step\": 567, \"epoch\": 3, \"mean_token_accuracy\": 0.8706}}, \"plan019_1_7b_rsft_s43_r2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T04:26:17.166Z\", \"updated_at\": \"2026-05-19T05:59:49.377Z\", \"hypothesis\": \"D114 Method A: 1.7B RSFT k=1 s43 重跑。使用 s42 SFT adapter (sft_output_qwen3_1_7b_bf16) + s42 CED k=1 scored data, RSFT seed=43。原始运行输出被误删(Worker B 误判)，需重新训练。验证 1.7B 尺度 RSFT 增益跨 seed 稳健性。\", \"parent\": \"plan019_1_7b_rsft_s43\", \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 0.5526}}, \"plan019_1_7b_rsft_s44\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T03:02:05.852Z\", \"updated_at\": \"2026-05-19T05:11:17.769Z\", \"hypothesis\": \"1.7B RSFT k=1 s44 (Option A seed expansion): 复用 s42 SFT adapter + s42 CED k=1 scored data，只变 RSFT 训练 seed 为 44。验证 1.7B 尺度 RSFT 增益跨 seed 稳健性。\", \"parent\": \"plan019_1_7b_sft_s44\", \"conclusion\": \"failed\"}, \"plan019_1_7b_rsft_s43\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T02:51:57.316Z\", \"updated_at\": \"2026-05-19T05:11:16.432Z\", \"hypothesis\": \"1.7B RSFT k=1 s43 (Option A seed expansion): 复用 s42 SFT adapter + s42 CED k=1 scored data，只变 RSFT 训练 seed 为 43。验证 1.7B 尺度 RSFT 增益跨 seed 稳健性。\", \"parent\": \"plan019_1_7b_sft_s43_r2\", \"conclusion\": \"failed\"}, \"plan019_8b_rsft_s44_eval\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T02:11:06.132Z\", \"updated_at\": \"2026-05-19T05:08:07.693Z\", \"hypothesis\": \"8B RSFT s44 eval (Option A seed expansion). 预期 ign_f1 接近 canonical s42 (0.5376)，验证 RSFT 增益在 8B 尺度跨 seed 稳定。\", \"parent\": \"plan019_8b_rsft_s44\", \"conclusion\": \"success\", \"metrics\": {\"ign_f1\": 0.5451, \"f1\": 0.562, \"evi_f1_tp\": 0.8145, \"evi_f1_dreeam\": 0.4472, \"edcr\": 0.6233, \"format_ok\": \"985/985\", \"truncated\": \"230/985\", \"predictions\": 16254}, \"notes\": \"Cron 误报 failed (submit_training_job 脚本路径不存在 EXIT_CODE=127)，但 Worker 已通过 Python 直接执行 eval 成功。结果在 /root/autodl-tmp/eval_results/rsft_8b_k1_s44_eval.log。已更正为 success。8B RSFT s44 ign_f1=0.5451 vs canonical s42 0.5376 (+0.75pp)，跨 seed 稳健。\"}, \"d112_rsft_s44_ced_score\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T03:18:56.333Z\", \"updated_at\": \"2026-05-19T04:41:13.613Z\", \"hypothesis\": \"D112 step 2: CED scoring + k=1 selection on SFT s44 generation candidates. 使用 NLI-DeBERTa 对 N=8 候选打分，format_w=0.2, f1_w=0.4, ced_w=0.4，top_k=1 筛选最优样本用于后续 RSFT 训练。\", \"parent\": \"d112_rsft_s44_gen_shard0\", \"notes\": \"retry #2 running normally. 10000/24216 records scored as of 11:50 UTC. ETA ~12:33 UTC. Previous run failed at 03:28 UTC (process dead before scoring started). Current run healthy, no errors in log.\", \"conclusion\": \"success\"}, \"d111_4b_sft_s42_reeval\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T22:06:04.423Z\", \"updated_at\": \"2026-05-19T03:54:03.116Z\", \"hypothesis\": \"Re-evaluating 4B SFT s42 with D076 standardized protocol to establish fair 3-seed comparison with s43 and s44. Previous s42 evaluations gave inconsistent results (0.4106/0.4036/0.3974), so re-running with identical protocol resolves this.\", \"metrics\": {\"ign_f1\": 0.3974, \"rel_f1\": 0.4049, \"evi_f1\": 0.7986, \"evi_f1_joint\": 0.3147, \"edcr\": 0.6982}, \"conclusion\": \"success\"}, \"d112_rsft_s44_gen_shard3\": {\"status\": \"DONE\", \"created_at\": \"2026-05-19T00:44:31.524Z\", \"updated_at\": \"2026-05-19T03:17:28.913Z\", \"hypothesis\": \"D112 shard 3: 并行候选生成 (docs [2268:3027])，用 SFT s44 adapter 生成 N=8 RSFT 候选。\", \"conclusion\": \"success\"}, \"d112_rsft_s44_gen_shard1\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T23:43:46.463Z\", \"updated_at\": \"2026-05-19T03:01:57.420Z\", \"hypothesis\": \"D112 shard 1: 并行候选生成 (docs [756:1512])，用 SFT s44 adapter 生成 N=8 RSFT 候选。\", \"parent\": \"\", \"conclusion\": \"success\"}, \"d112_rsft_s44_gen_shard2\": {\"status\": \"DONE\", \"created_at\": \"2026-05-18T23:43:47.622Z\", \"updated_at\": \"2026-05-19T02:48:30.925Z\", \"hypothesis\": \"D112 shard 2: 并行候选生成 (docs [1512:2268])，用 SFT s44 adapter 生成 N=8 RSFT 候选。\", \"parent\": \"\", \"conclusion\": \"success\"}}, \"count\": 30, \"total\": 255, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.9409}}"
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
The `read_project_file` tool doesn't support `experiment_plan.yaml`. I need to read it directly from the filesystem. Let me find and read it.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "39f8a4ed-6d6b-4c23-9e46-167a8118c922",
  "uuid": "08dadc9b-499a-4bae-9fd2-3db033ad4826",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MZsdMmzXGxHdtU9PMWqBnH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8250,
      "cache_read_input_tokens": 25602,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8250
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

experiment_plan.yaml 不在 `read_project_file` 白名单里，直接从文件系统读取。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "39f8a4ed-6d6b-4c23-9e46-167a8118c922",
  "uuid": "a79c3d52-aa91-4582-bf73-ee05a0e55b66",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MZsdMmzXGxHdtU9PMWqBnH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8250,
      "cache_read_input_tokens": 25602,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8250
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

<details open><summary>🔧 Tool call — Glob · `toolu_01EGJKyofst8Las2e2jfd3de`</summary>

```json
{
  "pattern": "**/experiment_plan.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "39f8a4ed-6d6b-4c23-9e46-167a8118c922",
  "uuid": "c62b53e7-42c3-4abc-86e5-79fc80611afe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MZsdMmzXGxHdtU9PMWqBnH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8250,
      "cache_read_input_tokens": 25602,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8250
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

_source line 15 · 2026-05-19T16:52:30.573Z_

<details><summary>↩ Tool result · `toolu_01EGJKyofst8Las2e2jfd3de`</summary>

```text
experiment_plan.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "39f8a4ed-6d6b-4c23-9e46-167a8118c922",
  "uuid": "7b862472-e654-48b1-b573-713cb94d0cbf",
  "tool_use_result": {
    "filenames": [
      "experiment_plan.yaml"
    ],
    "durationMs": 29,
    "numFiles": 1,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 16_

<details open><summary>🔧 Tool call — Read · `toolu_013tDGM6LZMoLamp3ykyZuBv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/experiment_plan.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "39f8a4ed-6d6b-4c23-9e46-167a8118c922",
  "uuid": "b7ef6aeb-d31b-4f78-9ffd-5e94d30249a4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XDvD51onkAwVQ1k1mntNSD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 202,
      "cache_read_input_tokens": 33852,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 202
      },
      "output_tokens": 69,
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

_source line 17 · 2026-05-19T16:52:33.487Z_

<details><summary>↩ Tool result · `toolu_013tDGM6LZMoLamp3ykyZuBv`</summary>

```text
1	experiments:
2	- id: plan_001
3	  claim: 2
4	  description: 'CED vs flat-NLI RSFT ablation: 用 flat-NLI scoring（非 contrastive）筛选
5	    RSFT 训练数据，对比 CED scoring。验证 CED 的对比性 margin 是否优于朴素 NLI。步骤: (1) rsft_score_filter.py
6	    用 flat-NLI 模式重新打分已有 candidates, (2) RSFT 训练, (3) 全量 dev eval。'
7	  priority: P0
8	  gpu_budget_hours: 20
9	  deps: []
10	  registry_id: eval_flat_nli_seed45
11	- id: plan_002
12	  claim: 1
13	  description: 'Test set evaluation: 用 RSFT best config（r2b 或 s44）在 DocRED test set
14	    上评估。提交 CodaLab 获得官方 F1/Ign-F1，同时本地计算 Evi-F1 和 EDCR。'
15	  priority: P0
16	  gpu_budget_hours: 4
17	  deps:
18	  - plan_001
19	  registry_id: plan_002_test_rsft_s44
20	- id: plan_003
21	  claim: 4
22	  description: 'EDCR pipeline 验证 + cross-method diagnostic table: 在所有 evidence-producing
23	    方法（SFT, RSFT-CED, RSFT-flatNLI, CED-reranker）上计算 EDCR，验证 EDCR 作为独立评估指标的诊断能力。'
24	  priority: P0
25	  gpu_budget_hours: 2
26	  deps:
27	  - plan_001
28	  registry_id: plan_003_edcr_diagnostic
29	- id: plan_004
30	  claim: 1
31	  description: 'DREEAM baseline reproduction: 在 DocRED dev set 上复现 DREEAM (RoBERTa-large)
32	    的 Evi-F1，确认 57.34 数字可复现，作为 Claim 1 的直接对比基线。'
33	  priority: P0
34	  gpu_budget_hours: 8
35	  deps: []
36	  registry_id: plan_004_dreeam_baseline
37	- id: plan_005
38	  claim: 1
39	  description: 'CED-as-reranker: 推理时用 CED 对 SFT 生成的 N=8 候选重排选最佳，无需额外训练。验证 CED 在推理时的价值。已在运行中。'
40	  priority: P1
41	  gpu_budget_hours: 6
42	  deps: []
43	  registry_id: mvp2_ced_reranker_poc
44	- id: plan_006
45	  claim: 1
46	  description: 'Model size ablation (D077 升 P0): Qwen3-1.7B 和 Qwen3-8B 上复现 SFT → RSFT
47	    → eval pipeline，验证 evidence tax + RSFT 增益 + decoupling 在不同模型规模下成立。应对 RC4 和 scope
48	    不足问题。'
49	  priority: P0
50	  gpu_budget_hours: 32
51	  deps: []
52	  registry_id: plan_006_qwen3_1_7b_no_evidence_eval_v3
53	- id: plan_007
54	  claim: 1
55	  description: 'Re-DocRED cross-dataset (D077 升 P0): 在 Re-DocRED 上用当前 best config
56	    做 SFT → RSFT → eval。数据已就绪（格式与 DocRED 兼容，96 relation types 一致）。⚠️ Re-DocRED ~55%
57	    triples 无 evidence 标注（修正的 false negative），必须报告两种模式：evidence_only（与 DocRED 可比的
58	    evi_f1，仅 43% triples）+ full（全部 triples 的 rel_f1，无 evi_f1）。转换脚本已支持 --mode full。'
59	  priority: P0
60	  gpu_budget_hours: 16
61	  deps: []
62	  registry_id: plan_007_redocred_rsft_eval_r5
63	- id: plan_016
64	  claim: 2
65	  description: 'LLaMA-3.1-8B cross-family validation (D077 新增): 在非 Qwen 家族模型上复现核心
66	    pipeline (SFT → RSFT → GRPO QLoRA)，验证 decoupling spectrum 跨模型家族成立。关键实验：LLaMA GRPO
67	    QLoRA 是否也出现 catastrophic forgetting。'
68	  priority: P0
69	  gpu_budget_hours: 40
70	  deps: []
71	  registry_id: plan_016_llama_grpo_qlora
72	- id: plan_008
73	  claim: 2
74	  description: 'top_k ablation: CED scoring 筛选 top_k=3（更多训练数据 ~8000 samples）vs top_k=1（更严格
75	    ~2718 samples），验证 CED 过滤严格度对 RSFT 质量的影响。'
76	  priority: P1
77	  gpu_budget_hours: 8
78	  deps: []
79	  registry_id: reeval_rsft_topk3
80	- id: plan_011
81	  claim: 3
82	  description: 'GRPO G=8 实验: Dream 三档一致指出 G=4 太小，标准 GRPO 用 G=8-16。用 G=8 + CED reward
83	    + kl_coef=0.01 重跑 GRPO，验证 failure 是否持续。如仍 fail → 加强 Claim 3；如改善 → 需修改论文结论。可能需要
84	    gradient_accumulation 适配显存。'
85	  priority: P0
86	  gpu_budget_hours: 8
87	  deps: []
88	  registry_id: plan_011_bf16_g8_step_eval
89	- id: plan_012
90	  claim: 3
91	  description: 'DPO+CED experiment: 用 RSFT 候选数据构造 preference pairs (CED-preferred
92	    vs CED-rejected)，DPO 训练。验证 DPO 是否避免 GRPO 的 catastrophic forgetting。Dream v2 三档要求
93	    DPO 作为 RL spectrum 关键数据点，必须补全训练超参（β, lr, epochs, pair construction）。D045 升 P0。'
94	  priority: P0
95	  gpu_budget_hours: 12
96	  deps: []
97	  registry_id: plan_012_dpo_ced
98	- id: plan_013
99	  claim: 4
100	  description: '[CANCELLED by D104] EDCR 人工标注验证: 用户决定不做。RC6 用 per-relation 分析 + Limitations
101	    说明替代。'
102	  priority: CANCELLED
103	  gpu_budget_hours: 0
104	  deps: []
105	  registry_id: null
106	- id: plan_009
107	  claim: 3
108	  description: 'GRPO forgetting dynamics figure: 整理全部 GRPO checkpoint（42个）的 rel_f1/evi_f1/EDCR/reward
109	    轨迹，绘制 training dynamics 可视化图。包含 G=4 vs G=8 对比、三种 reward 对比。Dream v2 三档一致要求此图作为论文核心
110	    figure。数据已有，只需汇总+画图。'
111	  priority: P0
112	  gpu_budget_hours: 2
113	  deps: []
114	  registry_id: plan_009_dynamics_figure
115	- id: plan_010
116	  claim: 1
117	  description: 'NLI model ablation: DeBERTa-v3-base vs DeBERTa-v3-large 作为 CED scorer
118	    的对比，验证 NLI 模型能力对 CED 打分质量的影响。应对 RC1。D104 升级。'
119	  priority: P1
120	  gpu_budget_hours: 4
121	  deps: []
122	  registry_id: null
123	- id: plan_014
124	  claim: 1
125	  description: 'SFT-without-evidence ablation: 训练 Qwen3-4B SFT 只输出 relation triples（不含
126	    evidence sentences），对比标准 SFT（含 evidence）的 rel_f1。隔离 evidence generation 对抽取性能的代价。Dream
127	    v2 三档一致要求。用于回答"43.2% vs LMRC 60.7% 的 gap 有多少来自 evidence 生成负担"。'
128	  priority: P0
129	  gpu_budget_hours: 8
130	  deps: []
131	  registry_id: plan_014_sft_no_evidence
132	- id: plan_015
133	  claim: 2
134	  description: 'bf16 LoRA GRPO clean control: 与原始 GRPO (QLoRA 4-bit, G=4, kl=0, CED
135	    reward) 只改一个变量——quantization 从 QLoRA 4-bit 改为 bf16 LoRA。G=4, kl_coef=0 不变。目的:
136	    隔离 QLoRA confound，判断 decoupling 是 QLoRA artifact 还是 genuine RL-for-IE 现象。Dream
137	    v2 三档一致的 critical 要求。如 decoupling 在 bf16 下仍持续 → 可泛化 claim；如消失 → QLoRA 特定，需 re-scope。优先级取决于
138	    plan_011 eval 结果。'
139	  priority: P0
140	  gpu_budget_hours: 8
141	  deps:
142	  - plan_011
143	  registry_id: wave1_grpo_bf16_g4
144	- id: plan_mvp1
145	  claim: 1
146	  description: 'MVP-1: CED signal verification — DeBERTa NLI 区分 gold evidence vs entity-sharing
147	    distractor 的能力验证'
148	  priority: P0
149	  gpu_budget_hours: 1
150	  deps: []
151	  registry_id: mvp1_ced_signal
152	- id: plan_mvp2_sft
153	  claim: 1
154	  description: 'SFT baseline: Qwen3-4B + LoRA SFT on DocRED gold, 建立抽取和证据质量基线'
155	  priority: P0
156	  gpu_budget_hours: 4
157	  deps: []
158	  registry_id: mvp2_sft_warmup
159	- id: plan_mvp2_rsft
160	  claim: 1
161	  description: 'RSFT+CED 端到端验证: CED-filtered rejection sampling fine-tuning, 4 组配置全部
162	    PASS。真实结果(D038修正后): r1 rel_f1=0.4449/evi_f1=0.8187, s44 rel_f1=0.4655/evi_f1=0.8087,
163	    r2a rel_f1=0.4494/evi_f1=0.8108, r2b rel_f1=0.4493/evi_f1=0.8128'
164	  priority: P0
165	  gpu_budget_hours: 20
166	  deps:
167	  - plan_mvp1
168	  - plan_mvp2_sft
169	  registry_id: mvp2_rsft_train_r1
170	- id: plan_mvp2_grpo
171	  claim: 3
172	  description: 'GRPO+QLoRA 全线失败（negative result = C3 核心证据）: 3 种 reward × 多 lr, rel_f1
173	    max=0.211(lr5e-5)/0.014(lr5e-6), evi_f1 在 GRPO 下反而提升至 0.850 但 rel_f1 catastrophic
174	    forgetting。D031/D033 完整轨迹支撑 Claim 3'
175	  priority: P0
176	  gpu_budget_hours: 60
177	  deps:
178	  - plan_mvp2_sft
179	  registry_id: mvp2_grpo_ced_kl001_r4
180	- id: plan_017
181	  claim: 3
182	  description: 'Qwen3-14B scaling study: SFT(with-evidence) + SFT(no-evidence) + RSFT
183	    + eval。 第 4 尺度档位（1.7B/4B/8B/14B），验证 evidence tax 在更大模型上是否继续趋近零或转正。 需评估 RTX 5090
184	    32GB 显存是否够 bf16 LoRA（14B×2=28GB base），不够则用 QLoRA。 至少 2 seeds。'
185	  priority: P0
186	  gpu_budget_hours: 50
187	  deps: []
188	  registry_id: plan017_14b_sft_no_evidence_eval_r2
189	- id: plan_018
190	  claim: 1
191	  description: 'Cross-domain DocRE validation: 在 CDR (Chemical-Disease Relations)
192	    或 GDA (Gene-Disease Associations) 等生物医学 DocRE 数据集上验证 FREIGE pipeline。 需要：数据格式适配、prompt
193	    模板调整、relation type 映射。 验证 evidence-grounded DocRE 跨领域泛化能力，回应 "only Wikipedia domain"
194	    审稿质疑。 ⚠️ CDR/GDA 均无 evidence sentence 标注，无法计算 evi_f1。降级 P2，Limitations 说明。'
195	  priority: P2
196	  gpu_budget_hours: 60
197	  deps: []
198	  registry_id: null
199	- id: plan_019
200	  claim: 3
201	  description: 'Scaling seeds supplement: 每个尺度补到 3+ seeds（k=1 RSFT）。 当前缺口：1.7B 需补
202	    s43/s44，LLaMA 需补 s43/s44。 4B 已有 4+ seeds 不需补。8B-Qwen 2-seed 已完成（s42+s44）。每个 seed
203	    含 SFT + RSFT + no-evidence eval ≈ 5 GPU-h。 目标：每个尺度的 evidence tax 有 mean ± std，scaling
204	    claim 有统计力。'
205	  priority: P0
206	  gpu_budget_hours: 25
207	  deps: []
208	  registry_id: plan019_1_7b_rsft_s44_r2_eval
209	  notes: '8B-Qwen RSFT 2-seed 完成 (2026-05-19): s42 ign_f1=0.5376, s44 ign_f1=0.5451,
210	    mean=0.5414, sample_std=0.53pp。SFT baseline: s42=0.5051, s44=0.4681, mean=0.4866,
211	    std=2.62pp。RSFT 将 seed variance 从 2.62pp 压缩到 0.53pp (~5x)。剩余：1.7B s43/s44, LLaMA
212	    s43/s44。'
213	- id: plan_020
214	  claim: 3
215	  description: 'Evidence tax mechanistic analysis: 解释 WHY 1.7B 获益而 4B 受损。 分析维度：(1)
216	    output length distribution with vs without evidence (2) truncation rate 差异（1.7B
217	    fair subset 已有基础） (3) hallucination rate（false positive relations 在 with/without
218	    evidence 中的比例） (4) per-document evidence 生成对 RE 的影响（按 doc length 分层） 主要是 CPU 分析
219	    + 少量补充 eval。'
220	  priority: P1
221	  gpu_budget_hours: 10
222	  deps: []
223	  registry_id: null
224	- id: plan_021
225	  claim: 1
226	  description: 'Deep error analysis: 按 relation type / document length / entity count
227	    / evidence distance 分层分析。扩展 D070 per-relation EDCR 分析到更多维度。 区分 Main 和 Findings
228	    的 insight 层——Main 论文解释 why，Findings 只报 what。'
229	  priority: P1
230	  gpu_budget_hours: 5
231	  deps: []
232	  registry_id: null
233	- id: plan_022
234	  claim: 3
235	  description: 'Third model family validation: Mistral-7B 或 Gemma-2-9B 上复现 SFT + RSFT
236	    + eval。 验证 scaling pattern 跨第三个模型家族成立。如果 14B（plan_017）已做则优先级下降。'
237	  priority: P2
238	  gpu_budget_hours: 30
239	  deps: []
240	  registry_id: null
241	- id: plan_023
242	  claim: 1
243	  description: 'DocKS-RAG / LMRC baseline reproduction: 在相同 eval protocol 下复现 generative
244	    DocRE SOTA（DocKS-RAG, LMRC）作为完整对比表。审稿人期望 same-condition comparison。'
245	  priority: P2
246	  gpu_budget_hours: 10
247	  deps: []
248	  registry_id: null
249	- id: plan_w3_sft_seeds
250	  claim: 1
251	  description: W3 修复：SFT 4B baseline seed43 + seed44 训练 + eval。 与 canonical SFT (seed42)
252	    配对，计算 bootstrap CI + Cohen d， 验证 RSFT +4.92pp 增益的统计显著性。Wave 1 实验。
253	  priority: P0
254	  gpu_budget_hours: 8
255	  deps: []
256	  registry_id: wave1_sft_4b_s44_eval_r2
257	- id: plan_d112
258	  claim: 1
259	  description: 'D112: Full RSFT pipeline from SFT s44 base (strongest seed, ign_f1=0.4734).
260	    所有现有 4B RSFT 都基于 SFT s42 (最弱 seed)。验证 RSFT 是否能在强 SFT base 上也产生提升。Steps: generate
261	    candidates (N=8) → CED score → k=1 filter → RSFT train → D076 eval。'
262	  priority: P0
263	  gpu_budget_hours: 8
264	  deps:
265	  - plan_w3_sft_seeds
266	  registry_id: d112_rsft_s44_eval
267	- id: plan_w18_random
268	  claim: 1
269	  description: W18 修复：Random k=1 RSFT baseline。从 k=1 候选中随机抽取（不用 NLI 分数）， 验证 NLI-based
270	    selection 的价值。如果 random 也提升 → NLI scoring 不关键； 如果 random 不提升 → NLI scoring 是 RSFT
271	    有效的关键。Wave 1 实验。
272	  priority: P0
273	  gpu_budget_hours: 4
274	  deps: []
275	  registry_id: random_rsft_k1_eval
276	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "39f8a4ed-6d6b-4c23-9e46-167a8118c922",
  "uuid": "e09ac7b9-2162-436b-b7e3-bc4de4de4596",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/experiment_plan.yaml",
      "content": "experiments:\n- id: plan_001\n  claim: 2\n  description: 'CED vs flat-NLI RSFT ablation: 用 flat-NLI scoring（非 contrastive）筛选\n    RSFT 训练数据，对比 CED scoring。验证 CED 的对比性 margin 是否优于朴素 NLI。步骤: (1) rsft_score_filter.py\n    用 flat-NLI 模式重新打分已有 candidates, (2) RSFT 训练, (3) 全量 dev eval。'\n  priority: P0\n  gpu_budget_hours: 20\n  deps: []\n  registry_id: eval_flat_nli_seed45\n- id: plan_002\n  claim: 1\n  description: 'Test set evaluation: 用 RSFT best config（r2b 或 s44）在 DocRED test set\n    上评估。提交 CodaLab 获得官方 F1/Ign-F1，同时本地计算 Evi-F1 和 EDCR。'\n  priority: P0\n  gpu_budget_hours: 4\n  deps:\n  - plan_001\n  registry_id: plan_002_test_rsft_s44\n- id: plan_003\n  claim: 4\n  description: 'EDCR pipeline 验证 + cross-method diagnostic table: 在所有 evidence-producing\n    方法（SFT, RSFT-CED, RSFT-flatNLI, CED-reranker）上计算 EDCR，验证 EDCR 作为独立评估指标的诊断能力。'\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - plan_001\n  registry_id: plan_003_edcr_diagnostic\n- id: plan_004\n  claim: 1\n  description: 'DREEAM baseline reproduction: 在 DocRED dev set 上复现 DREEAM (RoBERTa-large)\n    的 Evi-F1，确认 57.34 数字可复现，作为 Claim 1 的直接对比基线。'\n  priority: P0\n  gpu_budget_hours: 8\n  deps: []\n  registry_id: plan_004_dreeam_baseline\n- id: plan_005\n  claim: 1\n  description: 'CED-as-reranker: 推理时用 CED 对 SFT 生成的 N=8 候选重排选最佳，无需额外训练。验证 CED 在推理时的价值。已在运行中。'\n  priority: P1\n  gpu_budget_hours: 6\n  deps: []\n  registry_id: mvp2_ced_reranker_poc\n- id: plan_006\n  claim: 1\n  description: 'Model size ablation (D077 升 P0): Qwen3-1.7B 和 Qwen3-8B 上复现 SFT → RSFT\n    → eval pipeline，验证 evidence tax + RSFT 增益 + decoupling 在不同模型规模下成立。应对 RC4 和 scope\n    不足问题。'\n  priority: P0\n  gpu_budget_hours: 32\n  deps: []\n  registry_id: plan_006_qwen3_1_7b_no_evidence_eval_v3\n- id: plan_007\n  claim: 1\n  description: 'Re-DocRED cross-dataset (D077 升 P0): 在 Re-DocRED 上用当前 best config\n    做 SFT → RSFT → eval。数据已就绪（格式与 DocRED 兼容，96 relation types 一致）。⚠️ Re-DocRED ~55%\n    triples 无 evidence 标注（修正的 false negative），必须报告两种模式：evidence_only（与 DocRED 可比的\n    evi_f1，仅 43% triples）+ full（全部 triples 的 rel_f1，无 evi_f1）。转换脚本已支持 --mode full。'\n  priority: P0\n  gpu_budget_hours: 16\n  deps: []\n  registry_id: plan_007_redocred_rsft_eval_r5\n- id: plan_016\n  claim: 2\n  description: 'LLaMA-3.1-8B cross-family validation (D077 新增): 在非 Qwen 家族模型上复现核心\n    pipeline (SFT → RSFT → GRPO QLoRA)，验证 decoupling spectrum 跨模型家族成立。关键实验：LLaMA GRPO\n    QLoRA 是否也出现 catastrophic forgetting。'\n  priority: P0\n  gpu_budget_hours: 40\n  deps: []\n  registry_id: plan_016_llama_grpo_qlora\n- id: plan_008\n  claim: 2\n  description: 'top_k ablation: CED scoring 筛选 top_k=3（更多训练数据 ~8000 samples）vs top_k=1（更严格\n    ~2718 samples），验证 CED 过滤严格度对 RSFT 质量的影响。'\n  priority: P1\n  gpu_budget_hours: 8\n  deps: []\n  registry_id: reeval_rsft_topk3\n- id: plan_011\n  claim: 3\n  description: 'GRPO G=8 实验: Dream 三档一致指出 G=4 太小，标准 GRPO 用 G=8-16。用 G=8 + CED reward\n    + kl_coef=0.01 重跑 GRPO，验证 failure 是否持续。如仍 fail → 加强 Claim 3；如改善 → 需修改论文结论。可能需要\n    gradient_accumulation 适配显存。'\n  priority: P0\n  gpu_budget_hours: 8\n  deps: []\n  registry_id: plan_011_bf16_g8_step_eval\n- id: plan_012\n  claim: 3\n  description: 'DPO+CED experiment: 用 RSFT 候选数据构造 preference pairs (CED-preferred\n    vs CED-rejected)，DPO 训练。验证 DPO 是否避免 GRPO 的 catastrophic forgetting。Dream v2 三档要求\n    DPO 作为 RL spectrum 关键数据点，必须补全训练超参（β, lr, epochs, pair construction）。D045 升 P0。'\n  priority: P0\n  gpu_budget_hours: 12\n  deps: []\n  registry_id: plan_012_dpo_ced\n- id: plan_013\n  claim: 4\n  description: '[CANCELLED by D104] EDCR 人工标注验证: 用户决定不做。RC6 用 per-relation 分析 + Limitations\n    说明替代。'\n  priority: CANCELLED\n  gpu_budget_hours: 0\n  deps: []\n  registry_id: null\n- id: plan_009\n  claim: 3\n  description: 'GRPO forgetting dynamics figure: 整理全部 GRPO checkpoint（42个）的 rel_f1/evi_f1/EDCR/reward\n    轨迹，绘制 training dynamics 可视化图。包含 G=4 vs G=8 对比、三种 reward 对比。Dream v2 三档一致要求此图作为论文核心\n    figure。数据已有，只需汇总+画图。'\n  priority: P0\n  gpu_budget_hours: 2\n  deps: []\n  registry_id: plan_009_dynamics_figure\n- id: plan_010\n  claim: 1\n  description: 'NLI model ablation: DeBERTa-v3-base vs DeBERTa-v3-large 作为 CED scorer\n    的对比，验证 NLI 模型能力对 CED 打分质量的影响。应对 RC1。D104 升级。'\n  priority: P1\n  gpu_budget_hours: 4\n  deps: []\n  registry_id: null\n- id: plan_014\n  claim: 1\n  description: 'SFT-without-evidence ablation: 训练 Qwen3-4B SFT 只输出 relation triples（不含\n    evidence sentences），对比标准 SFT（含 evidence）的 rel_f1。隔离 evidence generation 对抽取性能的代价。Dream\n    v2 三档一致要求。用于回答\"43.2% vs LMRC 60.7% 的 gap 有多少来自 evidence 生成负担\"。'\n  priority: P0\n  gpu_budget_hours: 8\n  deps: []\n  registry_id: plan_014_sft_no_evidence\n- id: plan_015\n  claim: 2\n  description: 'bf16 LoRA GRPO clean control: 与原始 GRPO (QLoRA 4-bit, G=4, kl=0, CED\n    reward) 只改一个变量——quantization 从 QLoRA 4-bit 改为 bf16 LoRA。G=4, kl_coef=0 不变。目的:\n    隔离 QLoRA confound，判断 decoupling 是 QLoRA artifact 还是 genuine RL-for-IE 现象。Dream\n    v2 三档一致的 critical 要求。如 decoupling 在 bf16 下仍持续 → 可泛化 claim；如消失 → QLoRA 特定，需 re-scope。优先级取决于\n    plan_011 eval 结果。'\n  priority: P0\n  gpu_budget_hours: 8\n  deps:\n  - plan_011\n  registry_id: wave1_grpo_bf16_g4\n- id: plan_mvp1\n  claim: 1\n  description: 'MVP-1: CED signal verification — DeBERTa NLI 区分 gold evidence vs entity-sharing\n    distractor 的能力验证'\n  priority: P0\n  gpu_budget_hours: 1\n  deps: []\n  registry_id: mvp1_ced_signal\n- id: plan_mvp2_sft\n  claim: 1\n  description: 'SFT baseline: Qwen3-4B + LoRA SFT on DocRED gold, 建立抽取和证据质量基线'\n  priority: P0\n  gpu_budget_hours: 4\n  deps: []\n  registry_id: mvp2_sft_warmup\n- id: plan_mvp2_rsft\n  claim: 1\n  description: 'RSFT+CED 端到端验证: CED-filtered rejection sampling fine-tuning, 4 组配置全部\n    PASS。真实结果(D038修正后): r1 rel_f1=0.4449/evi_f1=0.8187, s44 rel_f1=0.4655/evi_f1=0.8087,\n    r2a rel_f1=0.4494/evi_f1=0.8108, r2b rel_f1=0.4493/evi_f1=0.8128'\n  priority: P0\n  gpu_budget_hours: 20\n  deps:\n  - plan_mvp1\n  - plan_mvp2_sft\n  registry_id: mvp2_rsft_train_r1\n- id: plan_mvp2_grpo\n  claim: 3\n  description: 'GRPO+QLoRA 全线失败（negative result = C3 核心证据）: 3 种 reward × 多 lr, rel_f1\n    max=0.211(lr5e-5)/0.014(lr5e-6), evi_f1 在 GRPO 下反而提升至 0.850 但 rel_f1 catastrophic\n    forgetting。D031/D033 完整轨迹支撑 Claim 3'\n  priority: P0\n  gpu_budget_hours: 60\n  deps:\n  - plan_mvp2_sft\n  registry_id: mvp2_grpo_ced_kl001_r4\n- id: plan_017\n  claim: 3\n  description: 'Qwen3-14B scaling study: SFT(with-evidence) + SFT(no-evidence) + RSFT\n    + eval。 第 4 尺度档位（1.7B/4B/8B/14B），验证 evidence tax 在更大模型上是否继续趋近零或转正。 需评估 RTX 5090\n    32GB 显存是否够 bf16 LoRA（14B×2=28GB base），不够则用 QLoRA。 至少 2 seeds。'\n  priority: P0\n  gpu_budget_hours: 50\n  deps: []\n  registry_id: plan017_14b_sft_no_evidence_eval_r2\n- id: plan_018\n  claim: 1\n  description: 'Cross-domain DocRE validation: 在 CDR (Chemical-Disease Relations)\n    或 GDA (Gene-Disease Associations) 等生物医学 DocRE 数据集上验证 FREIGE pipeline。 需要：数据格式适配、prompt\n    模板调整、relation type 映射。 验证 evidence-grounded DocRE 跨领域泛化能力，回应 \"only Wikipedia domain\"\n    审稿质疑。 ⚠️ CDR/GDA 均无 evidence sentence 标注，无法计算 evi_f1。降级 P2，Limitations 说明。'\n  priority: P2\n  gpu_budget_hours: 60\n  deps: []\n  registry_id: null\n- id: plan_019\n  claim: 3\n  description: 'Scaling seeds supplement: 每个尺度补到 3+ seeds（k=1 RSFT）。 当前缺口：1.7B 需补\n    s43/s44，LLaMA 需补 s43/s44。 4B 已有 4+ seeds 不需补。8B-Qwen 2-seed 已完成（s42+s44）。每个 seed\n    含 SFT + RSFT + no-evidence eval ≈ 5 GPU-h。 目标：每个尺度的 evidence tax 有 mean ± std，scaling\n    claim 有统计力。'\n  priority: P0\n  gpu_budget_hours: 25\n  deps: []\n  registry_id: plan019_1_7b_rsft_s44_r2_eval\n  notes: '8B-Qwen RSFT 2-seed 完成 (2026-05-19): s42 ign_f1=0.5376, s44 ign_f1=0.5451,\n    mean=0.5414, sample_std=0.53pp。SFT baseline: s42=0.5051, s44=0.4681, mean=0.4866,\n    std=2.62pp。RSFT 将 seed variance 从 2.62pp 压缩到 0.53pp (~5x)。剩余：1.7B s43/s44, LLaMA\n    s43/s44。'\n- id: plan_020\n  claim: 3\n  description: 'Evidence tax mechanistic analysis: 解释 WHY 1.7B 获益而 4B 受损。 分析维度：(1)\n    output length distribution with vs without evidence (2) truncation rate 差异（1.7B\n    fair subset 已有基础） (3) hallucination rate（false positive relations 在 with/without\n    evidence 中的比例） (4) per-document evidence 生成对 RE 的影响（按 doc length 分层） 主要是 CPU 分析\n    + 少量补充 eval。'\n  priority: P1\n  gpu_budget_hours: 10\n  deps: []\n  registry_id: null\n- id: plan_021\n  claim: 1\n  description: 'Deep error analysis: 按 relation type / document length / entity count\n    / evidence distance 分层分析。扩展 D070 per-relation EDCR 分析到更多维度。 区分 Main 和 Findings\n    的 insight 层——Main 论文解释 why，Findings 只报 what。'\n  priority: P1\n  gpu_budget_hours: 5\n  deps: []\n  registry_id: null\n- id: plan_022\n  claim: 3\n  description: 'Third model family validation: Mistral-7B 或 Gemma-2-9B 上复现 SFT + RSFT\n    + eval。 验证 scaling pattern 跨第三个模型家族成立。如果 14B（plan_017）已做则优先级下降。'\n  priority: P2\n  gpu_budget_hours: 30\n  deps: []\n  registry_id: null\n- id: plan_023\n  claim: 1\n  description: 'DocKS-RAG / LMRC baseline reproduction: 在相同 eval protocol 下复现 generative\n    DocRE SOTA（DocKS-RAG, LMRC）作为完整对比表。审稿人期望 same-condition comparison。'\n  priority: P2\n  gpu_budget_hours: 10\n  deps: []\n  registry_id: null\n- id: plan_w3_sft_seeds\n  claim: 1\n  description: W3 修复：SFT 4B baseline seed43 + seed44 训练 + eval。 与 canonical SFT (seed42)\n    配对，计算 bootstrap CI + Cohen d， 验证 RSFT +4.92pp 增益的统计显著性。Wave 1 实验。\n  priority: P0\n  gpu_budget_hours: 8\n  deps: []\n  registry_id: wave1_sft_4b_s44_eval_r2\n- id: plan_d112\n  claim: 1\n  description: 'D112: Full RSFT pipeline from SFT s44 base (strongest seed, ign_f1=0.4734).\n    所有现有 4B RSFT 都基于 SFT s42 (最弱 seed)。验证 RSFT 是否能在强 SFT base 上也产生提升。Steps: generate\n    candidates (N=8) → CED score → k=1 filter → RSFT train → D076 eval。'\n  priority: P0\n  gpu_budget_hours: 8\n  deps:\n  - plan_w3_sft_seeds\n  registry_id: d112_rsft_s44_eval\n- id: plan_w18_random\n  claim: 1\n  description: W18 修复：Random k=1 RSFT baseline。从 k=1 候选中随机抽取（不用 NLI 分数）， 验证 NLI-based\n    selection 的价值。如果 random 也提升 → NLI scoring 不关键； 如果 random 不提升 → NLI scoring 是 RSFT\n    有效的关键。Wave 1 实验。\n  priority: P0\n  gpu_budget_hours: 4\n  deps: []\n  registry_id: random_rsft_k1_eval\n",
      "numLines": 276,
      "startLine": 1,
      "totalLines": 276
    }
  }
}
```

</details>

---

### Assistant

_source line 18_

<details><summary>Logged reasoning block</summary>

```text
Now I have both the experiment_plan.yaml and the registry. Let me analyze the discrepancies.

Let me map out the relevant experiments from the plan and compare with registry:

**plan_019 (8B experiments)**:
- registry_id in plan: `plan019_1_7b_rsft_s44_r2_eval`
- Registry shows plan019 related experiments:
  - plan019_8b_sft_s43: DONE/success (train_loss=0.5684) ✓
  - plan019_8b_sft_s43_eval: ANALYZING (not DONE/success as task says)
  - plan019_8b_rsft_s44_eval: DONE/success (ign_f1=0.5451) ✓
  - plan019_8b_rsft_no_evidence_eval: DONE/killed ✓
  - plan019_8b_rsft_no_evidence_eval_r2: RUNNING ✓
  - plan019_1_7b_rsft_no_evidence_eval: DONE/killed (truncation 59.2%) ✓
  - plan019_1_7b_rsft_no_evidence_eval_r2: appears to be cut off in the registry listing
  - plan019_1_7b_rsft_s43_r2: DONE/success
  - plan019_1_7b_rsft_s43_r2_eval: DONE/success (ign_f1=0.5109)
  - plan019_1_7b_rsft_s44_r2: DONE/success
  - plan019_1_7b_rsft_s44_r2_eval: DONE/success (ign_f1=0.5125)

Now I'm checking the D112 experiments, looking at the registry entries for the d112_rsft_s44_eval plan and seeing the shard generation tasks completed successfully.

The training and evaluation runs for D112 show mixed results—the initial QLoRA runs failed with a confound issue, but the bf16 variant succeeded and is currently evaluating. The no-evidence baseline experiments are failing or still running, and I'm also tracking the 14B model experiments with their own evaluation pipeline.

Looking at the 14B plan results, the training completed successfully with a loss of 0.5457, and after handling some D076 violations in the initial eval runs, the second round evaluations both succeeded with comparable ignore F1 scores around 0.55. I need to update the experiment plan to reflect that plan017_14b_sft_no_evidence_eval_r2 is the current stable state.

For plan_019, I'm checking what the current registry_id points to and whether it needs updating based on the latest successful experiment runs. notes say "8B-Qwen RSFT 2-seed 完成" with mean=0.5414
- But now we have: plan019_8b_sft_s43 DONE (3rd seed), plan019_8b_sft_s43_eval ANALYZING
- 1.7B RSFT: s43_r2_eval DONE (0.5109), s44_r2_eval DONE (0.5125) → 3 seeds complete
- 8B SFT: now 3 seeds (s42, s43 done, s44)
- 8B RSFT: still 2 seeds (s42, s44)
- No-evidence evals: 1.7B killed (truncation), 8B killed (cuda conflict), both have retries running

For plan_d112, the registry_id points to d112_rsft_s44_eval which failed due to QLoRA confound, but the bf16 redo is progressing—d112_rsft_s44_train_bf16 succeeded and d112_rsft_s44_eval_bf16 is running, with the no-evidence eval's r3 attempt still in progress. For plan_017, the registry_id correctly references plan017_14b_sft_no_evidence_eval_r2 which is done and successful, though the description hasn't been updated with results yet. I need to figure out which fields I can actually update since the save_project_file tool has limited file support. I need to update the notes for plan_019 with the latest experimental results—the 8B SFT third seed finished with a training loss of 0.5684 and eval metrics showing 0.5324 ign_f1 per task, while the 8B RSFT runs have two seeds completed with scores around 0.537-0.545. The no-evidence evaluations are partially done with some runs killed due to truncation or CUDA conflicts and others still running. For plan_d112, I should update the registry_id to reflect the newer bf16 variant that's currently running instead of the older failed version. since that's the canonical one now
   - Update description to note QLoRA confound in original run, bf16 redo in progress
   - Add notes about current status

Let me draft the changes for these plans. For plan_017, I need to add a notes field documenting the SFT training results. For plan_019, I'll update the notes with the completion status of the 1.7B and 8B runs plus the evaluation status. For plan_d112, I'm updating the registry ID to reflect the bf16 version and adding notes about the QLoRA issue and the ongoing redo.

Now I'm looking at the specific YAML structure for plan_017 to make sure I capture the scaling study details correctly—this is the 14B model evaluation across different model sizes testing whether the evidence tax effect persists or reverses at larger scales. Looking at the 8B model results across different seeds and configurations—the SFT runs show some variance with s42 at 0.5128, s43 still analyzing at 0.5324, and s44 dropping to 0.4604. The RSFT results are more stable with s42 and s44 averaging around 0.5414. The no-evidence evaluations are having issues though: the 1.7B run hit truncation problems and is retrying with a longer token limit, while the 8B runs are dealing with CUDA conflicts but one is progressing on a different device. I'm realizing the "已知" updates are the user's explicit corrections to what's actually happened, so those should take priority over the registry when they conflict. For the experiment_plan.yaml, I'll use these known updates as the source of truth since the registry may just be lagging behind.

Since `save_project_file` won't work for experiment_plan.yaml, I'll need to use the Edit function to make the changes directly. I'm planning three edits: adding a notes field to plan_017, updating the notes for plan_019 with the correct status, and fixing plan_d112's registry_id while adding notes.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "39f8a4ed-6d6b-4c23-9e46-167a8118c922",
  "uuid": "39950aed-d8a7-4a01-a51a-c24677aceff8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Uk7yNcNnFTRNLuc6zUQM3X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6009,
      "cache_read_input_tokens": 33852,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6009
      },
      "output_tokens": 8,
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

### Assistant

_source line 19_

Registry 已读取。现在对比 plan 与 registry，执行更新。

需要更新的内容：

1. **plan_017**: 添加 notes（14B SFT/eval/no-evidence 结果）
2. **plan_019**: 更新 notes（1.7B 3-seed 完成，8B 3rd seed，no-evidence eval 状态）
3. **plan_d112**: 更新 registry_id（原 QLoRA 版 failed → bf16 版），添加 notes

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "39f8a4ed-6d6b-4c23-9e46-167a8118c922",
  "uuid": "1b6cff0d-7b0a-4c48-84df-5af91008a421",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Uk7yNcNnFTRNLuc6zUQM3X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6009,
      "cache_read_input_tokens": 33852,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6009
      },
      "output_tokens": 8,
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

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — Edit · `toolu_01Fv4ihTqWZBxGcEQVewdtnb`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/experiment_plan.yaml",
  "old_string": "- id: plan_017\n  claim: 3\n  description: 'Qwen3-14B scaling study: SFT(with-evidence) + SFT(no-evidence) + RSFT\n    + eval。 第 4 尺度档位（1.7B/4B/8B/14B），验证 evidence tax 在更大模型上是否继续趋近零或转正。 需评估 RTX 5090\n    32GB 显存是否够 bf16 LoRA（14B×2=28GB base），不够则用 QLoRA。 至少 2 seeds。'\n  priority: P0\n  gpu_budget_hours: 50\n  deps: []\n  registry_id: plan017_14b_sft_no_evidence_eval_r2",
  "new_string": "- id: plan_017\n  claim: 3\n  description: 'Qwen3-14B scaling study: SFT(with-evidence) + SFT(no-evidence) + RSFT\n    + eval。 第 4 尺度档位（1.7B/4B/8B/14B），验证 evidence tax 在更大模型上是否继续趋近零或转正。 需评估 RTX 5090\n    32GB 显存是否够 bf16 LoRA（14B×2=28GB base），不够则用 QLoRA。 至少 2 seeds。'\n  priority: P0\n  gpu_budget_hours: 50\n  deps: []\n  registry_id: plan017_14b_sft_no_evidence_eval_r2\n  notes: '14B SFT DONE (train_loss=0.5457). Eval r2 DONE (bf16 --no-quantize): ign_f1=0.5507.\n    No-evidence eval r2 DONE: ign_f1=0.5510. Evidence tax = -0.03pp (nearly zero at\n    14B scale). r1 killed due to D076 int8 quantization violation, r2 corrected with\n    bf16. 剩余: RSFT training + eval 未开始。'"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "39f8a4ed-6d6b-4c23-9e46-167a8118c922",
  "uuid": "683754b4-ce45-4121-b8f7-a4da2a9d9fe1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Uk7yNcNnFTRNLuc6zUQM3X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6009,
      "cache_read_input_tokens": 33852,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6009
      },
      "output_tokens": 8,
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

_source line 21 · 2026-05-19T16:53:42.422Z_

<details><summary>↩ Tool result · `toolu_01Fv4ihTqWZBxGcEQVewdtnb`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/experiment_plan.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "39f8a4ed-6d6b-4c23-9e46-167a8118c922",
  "uuid": "22fa9f31-263d-4f31-8778-648f5f7594f2",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/experiment_plan.yaml",
    "oldString": "- id: plan_017\n  claim: 3\n  description: 'Qwen3-14B scaling study: SFT(with-evidence) + SFT(no-evidence) + RSFT\n    + eval。 第 4 尺度档位（1.7B/4B/8B/14B），验证 evidence tax 在更大模型上是否继续趋近零或转正。 需评估 RTX 5090\n    32GB 显存是否够 bf16 LoRA（14B×2=28GB base），不够则用 QLoRA。 至少 2 seeds。'\n  priority: P0\n  gpu_budget_hours: 50\n  deps: []\n  registry_id: plan017_14b_sft_no_evidence_eval_r2",
    "newString": "- id: plan_017\n  claim: 3\n  description: 'Qwen3-14B scaling study: SFT(with-evidence) + SFT(no-evidence) + RSFT\n    + eval。 第 4 尺度档位（1.7B/4B/8B/14B），验证 evidence tax 在更大模型上是否继续趋近零或转正。 需评估 RTX 5090\n    32GB 显存是否够 bf16 LoRA（14B×2=28GB base），不够则用 QLoRA。 至少 2 seeds。'\n  priority: P0\n  gpu_budget_hours: 50\n  deps: []\n  registry_id: plan017_14b_sft_no_evidence_eval_r2\n  notes: '14B SFT DONE (train_loss=0.5457). Eval r2 DONE (bf16 --no-quantize): ign_f1=0.5507.\n    No-evidence eval r2 DONE: ign_f1=0.5510. Evidence tax = -0.03pp (nearly zero at\n    14B scale). r1 killed due to D076 int8 quantization violation, r2 corrected with\n    bf16. 剩余: RSFT training + eval 未开始。'",
    "originalFile": "experiments:\n- id: plan_001\n  claim: 2\n  description: 'CED vs flat-NLI RSFT ablation: 用 flat-NLI scoring（非 contrastive）筛选\n    RSFT 训练数据，对比 CED scoring。验证 CED 的对比性 margin 是否优于朴素 NLI。步骤: (1) rsft_score_filter.py\n    用 flat-NLI 模式重新打分已有 candidates, (2) RSFT 训练, (3) 全量 dev eval。'\n  priority: P0\n  gpu_budget_hours: 20\n  deps: []\n  registry_id: eval_flat_nli_seed45\n- id: plan_002\n  claim: 1\n  description: 'Test set evaluation: 用 RSFT best config（r2b 或 s44）在 DocRED test set\n    上评估。提交 CodaLab 获得官方 F1/Ign-F1，同时本地计算 Evi-F1 和 EDCR。'\n  priority: P0\n  gpu_budget_hours: 4\n  deps:\n  - plan_001\n  registry_id: plan_002_test_rsft_s44\n- id: plan_003\n  claim: 4\n  description: 'EDCR pipeline 验证 + cross-method diagnostic table: 在所有 evidence-producing\n    方法（SFT, RSFT-CED, RSFT-flatNLI, CED-reranker）上计算 EDCR，验证 EDCR 作为独立评估指标的诊断能力。'\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - plan_001\n  registry_id: plan_003_edcr_diagnostic\n- id: plan_004\n  claim: 1\n  description: 'DREEAM baseline reproduction: 在 DocRED dev set 上复现 DREEAM (RoBERTa-large)\n    的 Evi-F1，确认 57.34 数字可复现，作为 Claim 1 的直接对比基线。'\n  priority: P0\n  gpu_budget_hours: 8\n  deps: []\n  registry_id: plan_004_dreeam_baseline\n- id: plan_005\n  claim: 1\n  description: 'CED-as-reranker: 推理时用 CED 对 SFT 生成的 N=8 候选重排选最佳，无需额外训练。验证 CED 在推理时的价值。已在运行中。'\n  priority: P1\n  gpu_budget_hours: 6\n  deps: []\n  registry_id: mvp2_ced_reranker_poc\n- id: plan_006\n  claim: 1\n  description: 'Model size ablation (D077 升 P0): Qwen3-1.7B 和 Qwen3-8B 上复现 SFT → RSFT\n    → eval pipeline，验证 evidence tax + RSFT 增益 + decoupling 在不同模型规模下成立。应对 RC4 和 scope\n    不足问题。'\n  priority: P0\n  gpu_budget_hours: 32\n  deps: []\n  registry_id: plan_006_qwen3_1_7b_no_evidence_eval_v3\n- id: plan_007\n  claim: 1\n  description: 'Re-DocRED cross-dataset (D077 升 P0): 在 Re-DocRED 上用当前 best config\n    做 SFT → RSFT → eval。数据已就绪（格式与 DocRED 兼容，96 relation types 一致）。⚠️ Re-DocRED ~55%\n    triples 无 evidence 标注（修正的 false negative），必须报告两种模式：evidence_only（与 DocRED 可比的\n    evi_f1，仅 43% triples）+ full（全部 triples 的 rel_f1，无 evi_f1）。转换脚本已支持 --mode full。'\n  priority: P0\n  gpu_budget_hours: 16\n  deps: []\n  registry_id: plan_007_redocred_rsft_eval_r5\n- id: plan_016\n  claim: 2\n  description: 'LLaMA-3.1-8B cross-family validation (D077 新增): 在非 Qwen 家族模型上复现核心\n    pipeline (SFT → RSFT → GRPO QLoRA)，验证 decoupling spectrum 跨模型家族成立。关键实验：LLaMA GRPO\n    QLoRA 是否也出现 catastrophic forgetting。'\n  priority: P0\n  gpu_budget_hours: 40\n  deps: []\n  registry_id: plan_016_llama_grpo_qlora\n- id: plan_008\n  claim: 2\n  description: 'top_k ablation: CED scoring 筛选 top_k=3（更多训练数据 ~8000 samples）vs top_k=1（更严格\n    ~2718 samples），验证 CED 过滤严格度对 RSFT 质量的影响。'\n  priority: P1\n  gpu_budget_hours: 8\n  deps: []\n  registry_id: reeval_rsft_topk3\n- id: plan_011\n  claim: 3\n  description: 'GRPO G=8 实验: Dream 三档一致指出 G=4 太小，标准 GRPO 用 G=8-16。用 G=8 + CED reward\n    + kl_coef=0.01 重跑 GRPO，验证 failure 是否持续。如仍 fail → 加强 Claim 3；如改善 → 需修改论文结论。可能需要\n    gradient_accumulation 适配显存。'\n  priority: P0\n  gpu_budget_hours: 8\n  deps: []\n  registry_id: plan_011_bf16_g8_step_eval\n- id: plan_012\n  claim: 3\n  description: 'DPO+CED experiment: 用 RSFT 候选数据构造 preference pairs (CED-preferred\n    vs CED-rejected)，DPO 训练。验证 DPO 是否避免 GRPO 的 catastrophic forgetting。Dream v2 三档要求\n    DPO 作为 RL spectrum 关键数据点，必须补全训练超参（β, lr, epochs, pair construction）。D045 升 P0。'\n  priority: P0\n  gpu_budget_hours: 12\n  deps: []\n  registry_id: plan_012_dpo_ced\n- id: plan_013\n  claim: 4\n  description: '[CANCELLED by D104] EDCR 人工标注验证: 用户决定不做。RC6 用 per-relation 分析 + Limitations\n    说明替代。'\n  priority: CANCELLED\n  gpu_budget_hours: 0\n  deps: []\n  registry_id: null\n- id: plan_009\n  claim: 3\n  description: 'GRPO forgetting dynamics figure: 整理全部 GRPO checkpoint（42个）的 rel_f1/evi_f1/EDCR/reward\n    轨迹，绘制 training dynamics 可视化图。包含 G=4 vs G=8 对比、三种 reward 对比。Dream v2 三档一致要求此图作为论文核心\n    figure。数据已有，只需汇总+画图。'\n  priority: P0\n  gpu_budget_hours: 2\n  deps: []\n  registry_id: plan_009_dynamics_figure\n- id: plan_010\n  claim: 1\n  description: 'NLI model ablation: DeBERTa-v3-base vs DeBERTa-v3-large 作为 CED scorer\n    的对比，验证 NLI 模型能力对 CED 打分质量的影响。应对 RC1。D104 升级。'\n  priority: P1\n  gpu_budget_hours: 4\n  deps: []\n  registry_id: null\n- id: plan_014\n  claim: 1\n  description: 'SFT-without-evidence ablation: 训练 Qwen3-4B SFT 只输出 relation triples（不含\n    evidence sentences），对比标准 SFT（含 evidence）的 rel_f1。隔离 evidence generation 对抽取性能的代价。Dream\n    v2 三档一致要求。用于回答\"43.2% vs LMRC 60.7% 的 gap 有多少来自 evidence 生成负担\"。'\n  priority: P0\n  gpu_budget_hours: 8\n  deps: []\n  registry_id: plan_014_sft_no_evidence\n- id: plan_015\n  claim: 2\n  description: 'bf16 LoRA GRPO clean control: 与原始 GRPO (QLoRA 4-bit, G=4, kl=0, CED\n    reward) 只改一个变量——quantization 从 QLoRA 4-bit 改为 bf16 LoRA。G=4, kl_coef=0 不变。目的:\n    隔离 QLoRA confound，判断 decoupling 是 QLoRA artifact 还是 genuine RL-for-IE 现象。Dream\n    v2 三档一致的 critical 要求。如 decoupling 在 bf16 下仍持续 → 可泛化 claim；如消失 → QLoRA 特定，需 re-scope。优先级取决于\n    plan_011 eval 结果。'\n  priority: P0\n  gpu_budget_hours: 8\n  deps:\n  - plan_011\n  registry_id: wave1_grpo_bf16_g4\n- id: plan_mvp1\n  claim: 1\n  description: 'MVP-1: CED signal verification — DeBERTa NLI 区分 gold evidence vs entity-sharing\n    distractor 的能力验证'\n  priority: P0\n  gpu_budget_hours: 1\n  deps: []\n  registry_id: mvp1_ced_signal\n- id: plan_mvp2_sft\n  claim: 1\n  description: 'SFT baseline: Qwen3-4B + LoRA SFT on DocRED gold, 建立抽取和证据质量基线'\n  priority: P0\n  gpu_budget_hours: 4\n  deps: []\n  registry_id: mvp2_sft_warmup\n- id: plan_mvp2_rsft\n  claim: 1\n  description: 'RSFT+CED 端到端验证: CED-filtered rejection sampling fine-tuning, 4 组配置全部\n    PASS。真实结果(D038修正后): r1 rel_f1=0.4449/evi_f1=0.8187, s44 rel_f1=0.4655/evi_f1=0.8087,\n    r2a rel_f1=0.4494/evi_f1=0.8108, r2b rel_f1=0.4493/evi_f1=0.8128'\n  priority: P0\n  gpu_budget_hours: 20\n  deps:\n  - plan_mvp1\n  - plan_mvp2_sft\n  registry_id: mvp2_rsft_train_r1\n- id: plan_mvp2_grpo\n  claim: 3\n  description: 'GRPO+QLoRA 全线失败（negative result = C3 核心证据）: 3 种 reward × 多 lr, rel_f1\n    max=0.211(lr5e-5)/0.014(lr5e-6), evi_f1 在 GRPO 下反而提升至 0.850 但 rel_f1 catastrophic\n    forgetting。D031/D033 完整轨迹支撑 Claim 3'\n  priority: P0\n  gpu_budget_hours: 60\n  deps:\n  - plan_mvp2_sft\n  registry_id: mvp2_grpo_ced_kl001_r4\n- id: plan_017\n  claim: 3\n  description: 'Qwen3-14B scaling study: SFT(with-evidence) + SFT(no-evidence) + RSFT\n    + eval。 第 4 尺度档位（1.7B/4B/8B/14B），验证 evidence tax 在更大模型上是否继续趋近零或转正。 需评估 RTX 5090\n    32GB 显存是否够 bf16 LoRA（14B×2=28GB base），不够则用 QLoRA。 至少 2 seeds。'\n  priority: P0\n  gpu_budget_hours: 50\n  deps: []\n  registry_id: plan017_14b_sft_no_evidence_eval_r2\n- id: plan_018\n  claim: 1\n  description: 'Cross-domain DocRE validation: 在 CDR (Chemical-Disease Relations)\n    或 GDA (Gene-Disease Associations) 等生物医学 DocRE 数据集上验证 FREIGE pipeline。 需要：数据格式适配、prompt\n    模板调整、relation type 映射。 验证 evidence-grounded DocRE 跨领域泛化能力，回应 \"only Wikipedia domain\"\n    审稿质疑。 ⚠️ CDR/GDA 均无 evidence sentence 标注，无法计算 evi_f1。降级 P2，Limitations 说明。'\n  priority: P2\n  gpu_budget_hours: 60\n  deps: []\n  registry_id: null\n- id: plan_019\n  claim: 3\n  description: 'Scaling seeds supplement: 每个尺度补到 3+ seeds（k=1 RSFT）。 当前缺口：1.7B 需补\n    s43/s44，LLaMA 需补 s43/s44。 4B 已有 4+ seeds 不需补。8B-Qwen 2-seed 已完成（s42+s44）。每个 seed\n    含 SFT + RSFT + no-evidence eval ≈ 5 GPU-h。 目标：每个尺度的 evidence tax 有 mean ± std，scaling\n    claim 有统计力。'\n  priority: P0\n  gpu_budget_hours: 25\n  deps: []\n  registry_id: plan019_1_7b_rsft_s44_r2_eval\n  notes: '8B-Qwen RSFT 2-seed 完成 (2026-05-19): s42 ign_f1=0.5376, s44 ign_f1=0.5451,\n    mean=0.5414, sample_std=0.53pp。SFT baseline: s42=0.5051, s44=0.4681, mean=0.4866,\n    std=2.62pp。RSFT 将 seed variance 从 2.62pp 压缩到 0.53pp (~5x)。剩余：1.7B s43/s44, LLaMA\n    s43/s44。'\n- id: plan_020\n  claim: 3\n  description: 'Evidence tax mechanistic analysis: 解释 WHY 1.7B 获益而 4B 受损。 分析维度：(1)\n    output length distribution with vs without evidence (2) truncation rate 差异（1.7B\n    fair subset 已有基础） (3) hallucination rate（false positive relations 在 with/without\n    evidence 中的比例） (4) per-document evidence 生成对 RE 的影响（按 doc length 分层） 主要是 CPU 分析\n    + 少量补充 eval。'\n  priority: P1\n  gpu_budget_hours: 10\n  deps: []\n  registry_id: null\n- id: plan_021\n  claim: 1\n  description: 'Deep error analysis: 按 relation type / document length / entity count\n    / evidence distance 分层分析。扩展 D070 per-relation EDCR 分析到更多维度。 区分 Main 和 Findings\n    的 insight 层——Main 论文解释 why，Findings 只报 what。'\n  priority: P1\n  gpu_budget_hours: 5\n  deps: []\n  registry_id: null\n- id: plan_022\n  claim: 3\n  description: 'Third model family validation: Mistral-7B 或 Gemma-2-9B 上复现 SFT + RSFT\n    + eval。 验证 scaling pattern 跨第三个模型家族成立。如果 14B（plan_017）已做则优先级下降。'\n  priority: P2\n  gpu_budget_hours: 30\n  deps: []\n  registry_id: null\n- id: plan_023\n  claim: 1\n  description: 'DocKS-RAG / LMRC baseline reproduction: 在相同 eval protocol 下复现 generative\n    DocRE SOTA（DocKS-RAG, LMRC）作为完整对比表。审稿人期望 same-condition comparison。'\n  priority: P2\n  gpu_budget_hours: 10\n  deps: []\n  registry_id: null\n- id: plan_w3_sft_seeds\n  claim: 1\n  description: W3 修复：SFT 4B baseline seed43 + seed44 训练 + eval。 与 canonical SFT (seed42)\n    配对，计算 bootstrap CI + Cohen d， 验证 RSFT +4.92pp 增益的统计显著性。Wave 1 实验。\n  priority: P0\n  gpu_budget_hours: 8\n  deps: []\n  registry_id: wave1_sft_4b_s44_eval_r2\n- id: plan_d112\n  claim: 1\n  description: 'D112: Full RSFT pipeline from SFT s44 base (strongest seed, ign_f1=0.4734).\n    所有现有 4B RSFT 都基于 SFT s42 (最弱 seed)。验证 RSFT 是否能在强 SFT base 上也产生提升。Steps: generate\n    candidates (N=8) → CED score → k=1 filter → RSFT train → D076 eval。'\n  priority: P0\n  gpu_budget_hours: 8\n  deps:\n  - plan_w3_sft_seeds\n  registry_id: d112_rsft_s44_eval\n- id: plan_w18_random\n  claim: 1\n  description: W18 修复：Random k=1 RSFT baseline。从 k=1 候选中随机抽取（不用 NLI 分数）， 验证 NLI-based\n    selection 的价值。如果 random 也提升 → NLI scoring 不关键； 如果 random 不提升 → NLI scoring 是 RSFT\n    有效的关键。Wave 1 实验。\n  priority: P0\n  gpu_budget_hours: 4\n  deps: []\n  registry_id: random_rsft_k1_eval\n",
    "structuredPatch": [
      {
        "oldStart": 186,
        "oldLines": 6,
        "newStart": 186,
        "newLines": 10,
        "lines": [
          "   gpu_budget_hours: 50",
          "   deps: []",
          "   registry_id: plan017_14b_sft_no_evidence_eval_r2",
          "+  notes: '14B SFT DONE (train_loss=0.5457). Eval r2 DONE (bf16 --no-quantize): ign_f1=0.5507.",
          "+    No-evidence eval r2 DONE: ign_f1=0.5510. Evidence tax = -0.03pp (nearly zero at",
          "+    14B scale). r1 killed due to D076 int8 quantization violation, r2 corrected with",
          "+    bf16. 剩余: RSFT training + eval 未开始。'",
          " - id: plan_018",
          "   claim: 1",
          "   description: 'Cross-domain DocRE validation: 在 CDR (Chemical-Disease Relations)"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 22_

<details open><summary>🔧 Tool call — Edit · `toolu_016biF3hbhWS5mhBqny5Nxw6`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/experiment_plan.yaml",
  "old_string": "  notes: '8B-Qwen RSFT 2-seed 完成 (2026-05-19): s42 ign_f1=0.5376, s44 ign_f1=0.5451,\n    mean=0.5414, sample_std=0.53pp。SFT baseline: s42=0.5051, s44=0.4681, mean=0.4866,\n    std=2.62pp。RSFT 将 seed variance 从 2.62pp 压缩到 0.53pp (~5x)。剩余：1.7B s43/s44, LLaMA\n    s43/s44。'",
  "new_string": "  notes: '1.7B RSFT 3-seed 完成 (2026-05-19): s42=0.5122, s43=0.5109, s44=0.5125,\n    mean=0.5119, std=0.09pp。8B SFT 3-seed: s42=0.5128, s43 DONE (loss=0.5684) eval\n    DONE (ign_f1=0.5324), s44=0.4604。8B RSFT 2-seed: s42=0.5376, s44=0.5451, mean=0.5414,\n    std=0.53pp。No-evidence evals: 1.7B DONE/killed (59.2% truncation), 2048-token retry\n    RUNNING (cuda:3); 8B r1 DONE/killed (cuda:2 冲突), r2 RUNNING (cuda:0); 14B no-evi\n    eval DONE (ign_f1=0.5510)。剩余: LLaMA s43/s44, 8B 3rd RSFT seed。'"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "39f8a4ed-6d6b-4c23-9e46-167a8118c922",
  "uuid": "22378bc5-2b28-4f97-9926-8606787e4327",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Uk7yNcNnFTRNLuc6zUQM3X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6009,
      "cache_read_input_tokens": 33852,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6009
      },
      "output_tokens": 8,
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

_source line 23 · 2026-05-19T16:53:48.127Z_

<details><summary>↩ Tool result · `toolu_016biF3hbhWS5mhBqny5Nxw6`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/experiment_plan.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "39f8a4ed-6d6b-4c23-9e46-167a8118c922",
  "uuid": "91731ec1-eeae-4fc4-8b8b-174a6855fb6a",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/experiment_plan.yaml",
    "oldString": "  notes: '8B-Qwen RSFT 2-seed 完成 (2026-05-19): s42 ign_f1=0.5376, s44 ign_f1=0.5451,\n    mean=0.5414, sample_std=0.53pp。SFT baseline: s42=0.5051, s44=0.4681, mean=0.4866,\n    std=2.62pp。RSFT 将 seed variance 从 2.62pp 压缩到 0.53pp (~5x)。剩余：1.7B s43/s44, LLaMA\n    s43/s44。'",
    "newString": "  notes: '1.7B RSFT 3-seed 完成 (2026-05-19): s42=0.5122, s43=0.5109, s44=0.5125,\n    mean=0.5119, std=0.09pp。8B SFT 3-seed: s42=0.5128, s43 DONE (loss=0.5684) eval\n    DONE (ign_f1=0.5324), s44=0.4604。8B RSFT 2-seed: s42=0.5376, s44=0.5451, mean=0.5414,\n    std=0.53pp。No-evidence evals: 1.7B DONE/killed (59.2% truncation), 2048-token retry\n    RUNNING (cuda:3); 8B r1 DONE/killed (cuda:2 冲突), r2 RUNNING (cuda:0); 14B no-evi\n    eval DONE (ign_f1=0.5510)。剩余: LLaMA s43/s44, 8B 3rd RSFT seed。'",
    "originalFile": "experiments:\n- id: plan_001\n  claim: 2\n  description: 'CED vs flat-NLI RSFT ablation: 用 flat-NLI scoring（非 contrastive）筛选\n    RSFT 训练数据，对比 CED scoring。验证 CED 的对比性 margin 是否优于朴素 NLI。步骤: (1) rsft_score_filter.py\n    用 flat-NLI 模式重新打分已有 candidates, (2) RSFT 训练, (3) 全量 dev eval。'\n  priority: P0\n  gpu_budget_hours: 20\n  deps: []\n  registry_id: eval_flat_nli_seed45\n- id: plan_002\n  claim: 1\n  description: 'Test set evaluation: 用 RSFT best config（r2b 或 s44）在 DocRED test set\n    上评估。提交 CodaLab 获得官方 F1/Ign-F1，同时本地计算 Evi-F1 和 EDCR。'\n  priority: P0\n  gpu_budget_hours: 4\n  deps:\n  - plan_001\n  registry_id: plan_002_test_rsft_s44\n- id: plan_003\n  claim: 4\n  description: 'EDCR pipeline 验证 + cross-method diagnostic table: 在所有 evidence-producing\n    方法（SFT, RSFT-CED, RSFT-flatNLI, CED-reranker）上计算 EDCR，验证 EDCR 作为独立评估指标的诊断能力。'\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - plan_001\n  registry_id: plan_003_edcr_diagnostic\n- id: plan_004\n  claim: 1\n  description: 'DREEAM baseline reproduction: 在 DocRED dev set 上复现 DREEAM (RoBERTa-large)\n    的 Evi-F1，确认 57.34 数字可复现，作为 Claim 1 的直接对比基线。'\n  priority: P0\n  gpu_budget_hours: 8\n  deps: []\n  registry_id: plan_004_dreeam_baseline\n- id: plan_005\n  claim: 1\n  description: 'CED-as-reranker: 推理时用 CED 对 SFT 生成的 N=8 候选重排选最佳，无需额外训练。验证 CED 在推理时的价值。已在运行中。'\n  priority: P1\n  gpu_budget_hours: 6\n  deps: []\n  registry_id: mvp2_ced_reranker_poc\n- id: plan_006\n  claim: 1\n  description: 'Model size ablation (D077 升 P0): Qwen3-1.7B 和 Qwen3-8B 上复现 SFT → RSFT\n    → eval pipeline，验证 evidence tax + RSFT 增益 + decoupling 在不同模型规模下成立。应对 RC4 和 scope\n    不足问题。'\n  priority: P0\n  gpu_budget_hours: 32\n  deps: []\n  registry_id: plan_006_qwen3_1_7b_no_evidence_eval_v3\n- id: plan_007\n  claim: 1\n  description: 'Re-DocRED cross-dataset (D077 升 P0): 在 Re-DocRED 上用当前 best config\n    做 SFT → RSFT → eval。数据已就绪（格式与 DocRED 兼容，96 relation types 一致）。⚠️ Re-DocRED ~55%\n    triples 无 evidence 标注（修正的 false negative），必须报告两种模式：evidence_only（与 DocRED 可比的\n    evi_f1，仅 43% triples）+ full（全部 triples 的 rel_f1，无 evi_f1）。转换脚本已支持 --mode full。'\n  priority: P0\n  gpu_budget_hours: 16\n  deps: []\n  registry_id: plan_007_redocred_rsft_eval_r5\n- id: plan_016\n  claim: 2\n  description: 'LLaMA-3.1-8B cross-family validation (D077 新增): 在非 Qwen 家族模型上复现核心\n    pipeline (SFT → RSFT → GRPO QLoRA)，验证 decoupling spectrum 跨模型家族成立。关键实验：LLaMA GRPO\n    QLoRA 是否也出现 catastrophic forgetting。'\n  priority: P0\n  gpu_budget_hours: 40\n  deps: []\n  registry_id: plan_016_llama_grpo_qlora\n- id: plan_008\n  claim: 2\n  description: 'top_k ablation: CED scoring 筛选 top_k=3（更多训练数据 ~8000 samples）vs top_k=1（更严格\n    ~2718 samples），验证 CED 过滤严格度对 RSFT 质量的影响。'\n  priority: P1\n  gpu_budget_hours: 8\n  deps: []\n  registry_id: reeval_rsft_topk3\n- id: plan_011\n  claim: 3\n  description: 'GRPO G=8 实验: Dream 三档一致指出 G=4 太小，标准 GRPO 用 G=8-16。用 G=8 + CED reward\n    + kl_coef=0.01 重跑 GRPO，验证 failure 是否持续。如仍 fail → 加强 Claim 3；如改善 → 需修改论文结论。可能需要\n    gradient_accumulation 适配显存。'\n  priority: P0\n  gpu_budget_hours: 8\n  deps: []\n  registry_id: plan_011_bf16_g8_step_eval\n- id: plan_012\n  claim: 3\n  description: 'DPO+CED experiment: 用 RSFT 候选数据构造 preference pairs (CED-preferred\n    vs CED-rejected)，DPO 训练。验证 DPO 是否避免 GRPO 的 catastrophic forgetting。Dream v2 三档要求\n    DPO 作为 RL spectrum 关键数据点，必须补全训练超参（β, lr, epochs, pair construction）。D045 升 P0。'\n  priority: P0\n  gpu_budget_hours: 12\n  deps: []\n  registry_id: plan_012_dpo_ced\n- id: plan_013\n  claim: 4\n  description: '[CANCELLED by D104] EDCR 人工标注验证: 用户决定不做。RC6 用 per-relation 分析 + Limitations\n    说明替代。'\n  priority: CANCELLED\n  gpu_budget_hours: 0\n  deps: []\n  registry_id: null\n- id: plan_009\n  claim: 3\n  description: 'GRPO forgetting dynamics figure: 整理全部 GRPO checkpoint（42个）的 rel_f1/evi_f1/EDCR/reward\n    轨迹，绘制 training dynamics 可视化图。包含 G=4 vs G=8 对比、三种 reward 对比。Dream v2 三档一致要求此图作为论文核心\n    figure。数据已有，只需汇总+画图。'\n  priority: P0\n  gpu_budget_hours: 2\n  deps: []\n  registry_id: plan_009_dynamics_figure\n- id: plan_010\n  claim: 1\n  description: 'NLI model ablation: DeBERTa-v3-base vs DeBERTa-v3-large 作为 CED scorer\n    的对比，验证 NLI 模型能力对 CED 打分质量的影响。应对 RC1。D104 升级。'\n  priority: P1\n  gpu_budget_hours: 4\n  deps: []\n  registry_id: null\n- id: plan_014\n  claim: 1\n  description: 'SFT-without-evidence ablation: 训练 Qwen3-4B SFT 只输出 relation triples（不含\n    evidence sentences），对比标准 SFT（含 evidence）的 rel_f1。隔离 evidence generation 对抽取性能的代价。Dream\n    v2 三档一致要求。用于回答\"43.2% vs LMRC 60.7% 的 gap 有多少来自 evidence 生成负担\"。'\n  priority: P0\n  gpu_budget_hours: 8\n  deps: []\n  registry_id: plan_014_sft_no_evidence\n- id: plan_015\n  claim: 2\n  description: 'bf16 LoRA GRPO clean control: 与原始 GRPO (QLoRA 4-bit, G=4, kl=0, CED\n    reward) 只改一个变量——quantization 从 QLoRA 4-bit 改为 bf16 LoRA。G=4, kl_coef=0 不变。目的:\n    隔离 QLoRA confound，判断 decoupling 是 QLoRA artifact 还是 genuine RL-for-IE 现象。Dream\n    v2 三档一致的 critical 要求。如 decoupling 在 bf16 下仍持续 → 可泛化 claim；如消失 → QLoRA 特定，需 re-scope。优先级取决于\n    plan_011 eval 结果。'\n  priority: P0\n  gpu_budget_hours: 8\n  deps:\n  - plan_011\n  registry_id: wave1_grpo_bf16_g4\n- id: plan_mvp1\n  claim: 1\n  description: 'MVP-1: CED signal verification — DeBERTa NLI 区分 gold evidence vs entity-sharing\n    distractor 的能力验证'\n  priority: P0\n  gpu_budget_hours: 1\n  deps: []\n  registry_id: mvp1_ced_signal\n- id: plan_mvp2_sft\n  claim: 1\n  description: 'SFT baseline: Qwen3-4B + LoRA SFT on DocRED gold, 建立抽取和证据质量基线'\n  priority: P0\n  gpu_budget_hours: 4\n  deps: []\n  registry_id: mvp2_sft_warmup\n- id: plan_mvp2_rsft\n  claim: 1\n  description: 'RSFT+CED 端到端验证: CED-filtered rejection sampling fine-tuning, 4 组配置全部\n    PASS。真实结果(D038修正后): r1 rel_f1=0.4449/evi_f1=0.8187, s44 rel_f1=0.4655/evi_f1=0.8087,\n    r2a rel_f1=0.4494/evi_f1=0.8108, r2b rel_f1=0.4493/evi_f1=0.8128'\n  priority: P0\n  gpu_budget_hours: 20\n  deps:\n  - plan_mvp1\n  - plan_mvp2_sft\n  registry_id: mvp2_rsft_train_r1\n- id: plan_mvp2_grpo\n  claim: 3\n  description: 'GRPO+QLoRA 全线失败（negative result = C3 核心证据）: 3 种 reward × 多 lr, rel_f1\n    max=0.211(lr5e-5)/0.014(lr5e-6), evi_f1 在 GRPO 下反而提升至 0.850 但 rel_f1 catastrophic\n    forgetting。D031/D033 完整轨迹支撑 Claim 3'\n  priority: P0\n  gpu_budget_hours: 60\n  deps:\n  - plan_mvp2_sft\n  registry_id: mvp2_grpo_ced_kl001_r4\n- id: plan_017\n  claim: 3\n  description: 'Qwen3-14B scaling study: SFT(with-evidence) + SFT(no-evidence) + RSFT\n    + eval。 第 4 尺度档位（1.7B/4B/8B/14B），验证 evidence tax 在更大模型上是否继续趋近零或转正。 需评估 RTX 5090\n    32GB 显存是否够 bf16 LoRA（14B×2=28GB base），不够则用 QLoRA。 至少 2 seeds。'\n  priority: P0\n  gpu_budget_hours: 50\n  deps: []\n  registry_id: plan017_14b_sft_no_evidence_eval_r2\n  notes: '14B SFT DONE (train_loss=0.5457). Eval r2 DONE (bf16 --no-quantize): ign_f1=0.5507.\n    No-evidence eval r2 DONE: ign_f1=0.5510. Evidence tax = -0.03pp (nearly zero at\n    14B scale). r1 killed due to D076 int8 quantization violation, r2 corrected with\n    bf16. 剩余: RSFT training + eval 未开始。'\n- id: plan_018\n  claim: 1\n  description: 'Cross-domain DocRE validation: 在 CDR (Chemical-Disease Relations)\n    或 GDA (Gene-Disease Associations) 等生物医学 DocRE 数据集上验证 FREIGE pipeline。 需要：数据格式适配、prompt\n    模板调整、relation type 映射。 验证 evidence-grounded DocRE 跨领域泛化能力，回应 \"only Wikipedia domain\"\n    审稿质疑。 ⚠️ CDR/GDA 均无 evidence sentence 标注，无法计算 evi_f1。降级 P2，Limitations 说明。'\n  priority: P2\n  gpu_budget_hours: 60\n  deps: []\n  registry_id: null\n- id: plan_019\n  claim: 3\n  description: 'Scaling seeds supplement: 每个尺度补到 3+ seeds（k=1 RSFT）。 当前缺口：1.7B 需补\n    s43/s44，LLaMA 需补 s43/s44。 4B 已有 4+ seeds 不需补。8B-Qwen 2-seed 已完成（s42+s44）。每个 seed\n    含 SFT + RSFT + no-evidence eval ≈ 5 GPU-h。 目标：每个尺度的 evidence tax 有 mean ± std，scaling\n    claim 有统计力。'\n  priority: P0\n  gpu_budget_hours: 25\n  deps: []\n  registry_id: plan019_1_7b_rsft_s44_r2_eval\n  notes: '8B-Qwen RSFT 2-seed 完成 (2026-05-19): s42 ign_f1=0.5376, s44 ign_f1=0.5451,\n    mean=0.5414, sample_std=0.53pp。SFT baseline: s42=0.5051, s44=0.4681, mean=0.4866,\n    std=2.62pp。RSFT 将 seed variance 从 2.62pp 压缩到 0.53pp (~5x)。剩余：1.7B s43/s44, LLaMA\n    s43/s44。'\n- id: plan_020\n  claim: 3\n  description: 'Evidence tax mechanistic analysis: 解释 WHY 1.7B 获益而 4B 受损。 分析维度：(1)\n    output length distribution with vs without evidence (2) truncation rate 差异（1.7B\n    fair subset 已有基础） (3) hallucination rate（false positive relations 在 with/without\n    evidence 中的比例） (4) per-document evidence 生成对 RE 的影响（按 doc length 分层） 主要是 CPU 分析\n    + 少量补充 eval。'\n  priority: P1\n  gpu_budget_hours: 10\n  deps: []\n  registry_id: null\n- id: plan_021\n  claim: 1\n  description: 'Deep error analysis: 按 relation type / document length / entity count\n    / evidence distance 分层分析。扩展 D070 per-relation EDCR 分析到更多维度。 区分 Main 和 Findings\n    的 insight 层——Main 论文解释 why，Findings 只报 what。'\n  priority: P1\n  gpu_budget_hours: 5\n  deps: []\n  registry_id: null\n- id: plan_022\n  claim: 3\n  description: 'Third model family validation: Mistral-7B 或 Gemma-2-9B 上复现 SFT + RSFT\n    + eval。 验证 scaling pattern 跨第三个模型家族成立。如果 14B（plan_017）已做则优先级下降。'\n  priority: P2\n  gpu_budget_hours: 30\n  deps: []\n  registry_id: null\n- id: plan_023\n  claim: 1\n  description: 'DocKS-RAG / LMRC baseline reproduction: 在相同 eval protocol 下复现 generative\n    DocRE SOTA（DocKS-RAG, LMRC）作为完整对比表。审稿人期望 same-condition comparison。'\n  priority: P2\n  gpu_budget_hours: 10\n  deps: []\n  registry_id: null\n- id: plan_w3_sft_seeds\n  claim: 1\n  description: W3 修复：SFT 4B baseline seed43 + seed44 训练 + eval。 与 canonical SFT (seed42)\n    配对，计算 bootstrap CI + Cohen d， 验证 RSFT +4.92pp 增益的统计显著性。Wave 1 实验。\n  priority: P0\n  gpu_budget_hours: 8\n  deps: []\n  registry_id: wave1_sft_4b_s44_eval_r2\n- id: plan_d112\n  claim: 1\n  description: 'D112: Full RSFT pipeline from SFT s44 base (strongest seed, ign_f1=0.4734).\n    所有现有 4B RSFT 都基于 SFT s42 (最弱 seed)。验证 RSFT 是否能在强 SFT base 上也产生提升。Steps: generate\n    candidates (N=8) → CED score → k=1 filter → RSFT train → D076 eval。'\n  priority: P0\n  gpu_budget_hours: 8\n  deps:\n  - plan_w3_sft_seeds\n  registry_id: d112_rsft_s44_eval\n- id: plan_w18_random\n  claim: 1\n  description: W18 修复：Random k=1 RSFT baseline。从 k=1 候选中随机抽取（不用 NLI 分数）， 验证 NLI-based\n    selection 的价值。如果 random 也提升 → NLI scoring 不关键； 如果 random 不提升 → NLI scoring 是 RSFT\n    有效的关键。Wave 1 实验。\n  priority: P0\n  gpu_budget_hours: 4\n  deps: []\n  registry_id: random_rsft_k1_eval\n",
    "structuredPatch": [
      {
        "oldStart": 210,
        "oldLines": 10,
        "newStart": 210,
        "newLines": 12,
        "lines": [
          "   gpu_budget_hours: 25",
          "   deps: []",
          "   registry_id: plan019_1_7b_rsft_s44_r2_eval",
          "-  notes: '8B-Qwen RSFT 2-seed 完成 (2026-05-19): s42 ign_f1=0.5376, s44 ign_f1=0.5451,",
          "-    mean=0.5414, sample_std=0.53pp。SFT baseline: s42=0.5051, s44=0.4681, mean=0.4866,",
          "-    std=2.62pp。RSFT 将 seed variance 从 2.62pp 压缩到 0.53pp (~5x)。剩余：1.7B s43/s44, LLaMA",
          "-    s43/s44。'",
          "+  notes: '1.7B RSFT 3-seed 完成 (2026-05-19): s42=0.5122, s43=0.5109, s44=0.5125,",
          "+    mean=0.5119, std=0.09pp。8B SFT 3-seed: s42=0.5128, s43 DONE (loss=0.5684) eval",
          "+    DONE (ign_f1=0.5324), s44=0.4604。8B RSFT 2-seed: s42=0.5376, s44=0.5451, mean=0.5414,",
          "+    std=0.53pp。No-evidence evals: 1.7B DONE/killed (59.2% truncation), 2048-token retry",
          "+    RUNNING (cuda:3); 8B r1 DONE/killed (cuda:2 冲突), r2 RUNNING (cuda:0); 14B no-evi",
          "+    eval DONE (ign_f1=0.5510)。剩余: LLaMA s43/s44, 8B 3rd RSFT seed。'",
          " - id: plan_020",
          "   claim: 3",
          "   description: 'Evidence tax mechanistic analysis: 解释 WHY 1.7B 获益而 4B 受损。 分析维度：(1)"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 24_

<details open><summary>🔧 Tool call — Edit · `toolu_01K7wUjxjpwmikKuVsMd3DmW`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/experiment_plan.yaml",
  "old_string": "- id: plan_d112\n  claim: 1\n  description: 'D112: Full RSFT pipeline from SFT s44 base (strongest seed, ign_f1=0.4734).\n    所有现有 4B RSFT 都基于 SFT s42 (最弱 seed)。验证 RSFT 是否能在强 SFT base 上也产生提升。Steps: generate\n    candidates (N=8) → CED score → k=1 filter → RSFT train → D076 eval。'\n  priority: P0\n  gpu_budget_hours: 8\n  deps:\n  - plan_w3_sft_seeds\n  registry_id: d112_rsft_s44_eval",
  "new_string": "- id: plan_d112\n  claim: 1\n  description: 'D112: Full RSFT pipeline from SFT s44 base (strongest seed, ign_f1=0.4734).\n    所有现有 4B RSFT 都基于 SFT s42 (最弱 seed)。验证 RSFT 是否能在强 SFT base 上也产生提升。Steps: generate\n    candidates (N=8) → CED score → k=1 filter → RSFT train → D076 eval。'\n  priority: P0\n  gpu_budget_hours: 8\n  deps:\n  - plan_w3_sft_seeds\n  registry_id: d112_rsft_s44_eval_bf16\n  notes: '原 QLoRA 版 d112_rsft_s44_train DONE/failed (QLoRA confound: adapter 适应 4-bit\n    量化误差, bf16 eval 下 ign_f1=0.2181 灾难性崩溃)。bf16 重跑: d112_rsft_s44_train_bf16 DONE/success,\n    d112_rsft_s44_eval_bf16 RUNNING (cuda:2)。No-evidence eval: r1/r2 failed (EXIT_CODE=127\n    脚本路径错误), r3 RUNNING (cuda:1)。'"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "39f8a4ed-6d6b-4c23-9e46-167a8118c922",
  "uuid": "9d2242c1-bbf2-4beb-acac-c2033bba16e7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Uk7yNcNnFTRNLuc6zUQM3X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6009,
      "cache_read_input_tokens": 33852,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6009
      },
      "output_tokens": 8,
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

_source line 25 · 2026-05-19T16:53:54.672Z_

<details><summary>↩ Tool result · `toolu_01K7wUjxjpwmikKuVsMd3DmW`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/experiment_plan.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "39f8a4ed-6d6b-4c23-9e46-167a8118c922",
  "uuid": "80c2ab90-e922-4d30-9f3c-3ae46ad3fa74",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/experiment_plan.yaml",
    "oldString": "- id: plan_d112\n  claim: 1\n  description: 'D112: Full RSFT pipeline from SFT s44 base (strongest seed, ign_f1=0.4734).\n    所有现有 4B RSFT 都基于 SFT s42 (最弱 seed)。验证 RSFT 是否能在强 SFT base 上也产生提升。Steps: generate\n    candidates (N=8) → CED score → k=1 filter → RSFT train → D076 eval。'\n  priority: P0\n  gpu_budget_hours: 8\n  deps:\n  - plan_w3_sft_seeds\n  registry_id: d112_rsft_s44_eval",
    "newString": "- id: plan_d112\n  claim: 1\n  description: 'D112: Full RSFT pipeline from SFT s44 base (strongest seed, ign_f1=0.4734).\n    所有现有 4B RSFT 都基于 SFT s42 (最弱 seed)。验证 RSFT 是否能在强 SFT base 上也产生提升。Steps: generate\n    candidates (N=8) → CED score → k=1 filter → RSFT train → D076 eval。'\n  priority: P0\n  gpu_budget_hours: 8\n  deps:\n  - plan_w3_sft_seeds\n  registry_id: d112_rsft_s44_eval_bf16\n  notes: '原 QLoRA 版 d112_rsft_s44_train DONE/failed (QLoRA confound: adapter 适应 4-bit\n    量化误差, bf16 eval 下 ign_f1=0.2181 灾难性崩溃)。bf16 重跑: d112_rsft_s44_train_bf16 DONE/success,\n    d112_rsft_s44_eval_bf16 RUNNING (cuda:2)。No-evidence eval: r1/r2 failed (EXIT_CODE=127\n    脚本路径错误), r3 RUNNING (cuda:1)。'",
    "originalFile": "experiments:\n- id: plan_001\n  claim: 2\n  description: 'CED vs flat-NLI RSFT ablation: 用 flat-NLI scoring（非 contrastive）筛选\n    RSFT 训练数据，对比 CED scoring。验证 CED 的对比性 margin 是否优于朴素 NLI。步骤: (1) rsft_score_filter.py\n    用 flat-NLI 模式重新打分已有 candidates, (2) RSFT 训练, (3) 全量 dev eval。'\n  priority: P0\n  gpu_budget_hours: 20\n  deps: []\n  registry_id: eval_flat_nli_seed45\n- id: plan_002\n  claim: 1\n  description: 'Test set evaluation: 用 RSFT best config（r2b 或 s44）在 DocRED test set\n    上评估。提交 CodaLab 获得官方 F1/Ign-F1，同时本地计算 Evi-F1 和 EDCR。'\n  priority: P0\n  gpu_budget_hours: 4\n  deps:\n  - plan_001\n  registry_id: plan_002_test_rsft_s44\n- id: plan_003\n  claim: 4\n  description: 'EDCR pipeline 验证 + cross-method diagnostic table: 在所有 evidence-producing\n    方法（SFT, RSFT-CED, RSFT-flatNLI, CED-reranker）上计算 EDCR，验证 EDCR 作为独立评估指标的诊断能力。'\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - plan_001\n  registry_id: plan_003_edcr_diagnostic\n- id: plan_004\n  claim: 1\n  description: 'DREEAM baseline reproduction: 在 DocRED dev set 上复现 DREEAM (RoBERTa-large)\n    的 Evi-F1，确认 57.34 数字可复现，作为 Claim 1 的直接对比基线。'\n  priority: P0\n  gpu_budget_hours: 8\n  deps: []\n  registry_id: plan_004_dreeam_baseline\n- id: plan_005\n  claim: 1\n  description: 'CED-as-reranker: 推理时用 CED 对 SFT 生成的 N=8 候选重排选最佳，无需额外训练。验证 CED 在推理时的价值。已在运行中。'\n  priority: P1\n  gpu_budget_hours: 6\n  deps: []\n  registry_id: mvp2_ced_reranker_poc\n- id: plan_006\n  claim: 1\n  description: 'Model size ablation (D077 升 P0): Qwen3-1.7B 和 Qwen3-8B 上复现 SFT → RSFT\n    → eval pipeline，验证 evidence tax + RSFT 增益 + decoupling 在不同模型规模下成立。应对 RC4 和 scope\n    不足问题。'\n  priority: P0\n  gpu_budget_hours: 32\n  deps: []\n  registry_id: plan_006_qwen3_1_7b_no_evidence_eval_v3\n- id: plan_007\n  claim: 1\n  description: 'Re-DocRED cross-dataset (D077 升 P0): 在 Re-DocRED 上用当前 best config\n    做 SFT → RSFT → eval。数据已就绪（格式与 DocRED 兼容，96 relation types 一致）。⚠️ Re-DocRED ~55%\n    triples 无 evidence 标注（修正的 false negative），必须报告两种模式：evidence_only（与 DocRED 可比的\n    evi_f1，仅 43% triples）+ full（全部 triples 的 rel_f1，无 evi_f1）。转换脚本已支持 --mode full。'\n  priority: P0\n  gpu_budget_hours: 16\n  deps: []\n  registry_id: plan_007_redocred_rsft_eval_r5\n- id: plan_016\n  claim: 2\n  description: 'LLaMA-3.1-8B cross-family validation (D077 新增): 在非 Qwen 家族模型上复现核心\n    pipeline (SFT → RSFT → GRPO QLoRA)，验证 decoupling spectrum 跨模型家族成立。关键实验：LLaMA GRPO\n    QLoRA 是否也出现 catastrophic forgetting。'\n  priority: P0\n  gpu_budget_hours: 40\n  deps: []\n  registry_id: plan_016_llama_grpo_qlora\n- id: plan_008\n  claim: 2\n  description: 'top_k ablation: CED scoring 筛选 top_k=3（更多训练数据 ~8000 samples）vs top_k=1（更严格\n    ~2718 samples），验证 CED 过滤严格度对 RSFT 质量的影响。'\n  priority: P1\n  gpu_budget_hours: 8\n  deps: []\n  registry_id: reeval_rsft_topk3\n- id: plan_011\n  claim: 3\n  description: 'GRPO G=8 实验: Dream 三档一致指出 G=4 太小，标准 GRPO 用 G=8-16。用 G=8 + CED reward\n    + kl_coef=0.01 重跑 GRPO，验证 failure 是否持续。如仍 fail → 加强 Claim 3；如改善 → 需修改论文结论。可能需要\n    gradient_accumulation 适配显存。'\n  priority: P0\n  gpu_budget_hours: 8\n  deps: []\n  registry_id: plan_011_bf16_g8_step_eval\n- id: plan_012\n  claim: 3\n  description: 'DPO+CED experiment: 用 RSFT 候选数据构造 preference pairs (CED-preferred\n    vs CED-rejected)，DPO 训练。验证 DPO 是否避免 GRPO 的 catastrophic forgetting。Dream v2 三档要求\n    DPO 作为 RL spectrum 关键数据点，必须补全训练超参（β, lr, epochs, pair construction）。D045 升 P0。'\n  priority: P0\n  gpu_budget_hours: 12\n  deps: []\n  registry_id: plan_012_dpo_ced\n- id: plan_013\n  claim: 4\n  description: '[CANCELLED by D104] EDCR 人工标注验证: 用户决定不做。RC6 用 per-relation 分析 + Limitations\n    说明替代。'\n  priority: CANCELLED\n  gpu_budget_hours: 0\n  deps: []\n  registry_id: null\n- id: plan_009\n  claim: 3\n  description: 'GRPO forgetting dynamics figure: 整理全部 GRPO checkpoint（42个）的 rel_f1/evi_f1/EDCR/reward\n    轨迹，绘制 training dynamics 可视化图。包含 G=4 vs G=8 对比、三种 reward 对比。Dream v2 三档一致要求此图作为论文核心\n    figure。数据已有，只需汇总+画图。'\n  priority: P0\n  gpu_budget_hours: 2\n  deps: []\n  registry_id: plan_009_dynamics_figure\n- id: plan_010\n  claim: 1\n  description: 'NLI model ablation: DeBERTa-v3-base vs DeBERTa-v3-large 作为 CED scorer\n    的对比，验证 NLI 模型能力对 CED 打分质量的影响。应对 RC1。D104 升级。'\n  priority: P1\n  gpu_budget_hours: 4\n  deps: []\n  registry_id: null\n- id: plan_014\n  claim: 1\n  description: 'SFT-without-evidence ablation: 训练 Qwen3-4B SFT 只输出 relation triples（不含\n    evidence sentences），对比标准 SFT（含 evidence）的 rel_f1。隔离 evidence generation 对抽取性能的代价。Dream\n    v2 三档一致要求。用于回答\"43.2% vs LMRC 60.7% 的 gap 有多少来自 evidence 生成负担\"。'\n  priority: P0\n  gpu_budget_hours: 8\n  deps: []\n  registry_id: plan_014_sft_no_evidence\n- id: plan_015\n  claim: 2\n  description: 'bf16 LoRA GRPO clean control: 与原始 GRPO (QLoRA 4-bit, G=4, kl=0, CED\n    reward) 只改一个变量——quantization 从 QLoRA 4-bit 改为 bf16 LoRA。G=4, kl_coef=0 不变。目的:\n    隔离 QLoRA confound，判断 decoupling 是 QLoRA artifact 还是 genuine RL-for-IE 现象。Dream\n    v2 三档一致的 critical 要求。如 decoupling 在 bf16 下仍持续 → 可泛化 claim；如消失 → QLoRA 特定，需 re-scope。优先级取决于\n    plan_011 eval 结果。'\n  priority: P0\n  gpu_budget_hours: 8\n  deps:\n  - plan_011\n  registry_id: wave1_grpo_bf16_g4\n- id: plan_mvp1\n  claim: 1\n  description: 'MVP-1: CED signal verification — DeBERTa NLI 区分 gold evidence vs entity-sharing\n    distractor 的能力验证'\n  priority: P0\n  gpu_budget_hours: 1\n  deps: []\n  registry_id: mvp1_ced_signal\n- id: plan_mvp2_sft\n  claim: 1\n  description: 'SFT baseline: Qwen3-4B + LoRA SFT on DocRED gold, 建立抽取和证据质量基线'\n  priority: P0\n  gpu_budget_hours: 4\n  deps: []\n  registry_id: mvp2_sft_warmup\n- id: plan_mvp2_rsft\n  claim: 1\n  description: 'RSFT+CED 端到端验证: CED-filtered rejection sampling fine-tuning, 4 组配置全部\n    PASS。真实结果(D038修正后): r1 rel_f1=0.4449/evi_f1=0.8187, s44 rel_f1=0.4655/evi_f1=0.8087,\n    r2a rel_f1=0.4494/evi_f1=0.8108, r2b rel_f1=0.4493/evi_f1=0.8128'\n  priority: P0\n  gpu_budget_hours: 20\n  deps:\n  - plan_mvp1\n  - plan_mvp2_sft\n  registry_id: mvp2_rsft_train_r1\n- id: plan_mvp2_grpo\n  claim: 3\n  description: 'GRPO+QLoRA 全线失败（negative result = C3 核心证据）: 3 种 reward × 多 lr, rel_f1\n    max=0.211(lr5e-5)/0.014(lr5e-6), evi_f1 在 GRPO 下反而提升至 0.850 但 rel_f1 catastrophic\n    forgetting。D031/D033 完整轨迹支撑 Claim 3'\n  priority: P0\n  gpu_budget_hours: 60\n  deps:\n  - plan_mvp2_sft\n  registry_id: mvp2_grpo_ced_kl001_r4\n- id: plan_017\n  claim: 3\n  description: 'Qwen3-14B scaling study: SFT(with-evidence) + SFT(no-evidence) + RSFT\n    + eval。 第 4 尺度档位（1.7B/4B/8B/14B），验证 evidence tax 在更大模型上是否继续趋近零或转正。 需评估 RTX 5090\n    32GB 显存是否够 bf16 LoRA（14B×2=28GB base），不够则用 QLoRA。 至少 2 seeds。'\n  priority: P0\n  gpu_budget_hours: 50\n  deps: []\n  registry_id: plan017_14b_sft_no_evidence_eval_r2\n  notes: '14B SFT DONE (train_loss=0.5457). Eval r2 DONE (bf16 --no-quantize): ign_f1=0.5507.\n    No-evidence eval r2 DONE: ign_f1=0.5510. Evidence tax = -0.03pp (nearly zero at\n    14B scale). r1 killed due to D076 int8 quantization violation, r2 corrected with\n    bf16. 剩余: RSFT training + eval 未开始。'\n- id: plan_018\n  claim: 1\n  description: 'Cross-domain DocRE validation: 在 CDR (Chemical-Disease Relations)\n    或 GDA (Gene-Disease Associations) 等生物医学 DocRE 数据集上验证 FREIGE pipeline。 需要：数据格式适配、prompt\n    模板调整、relation type 映射。 验证 evidence-grounded DocRE 跨领域泛化能力，回应 \"only Wikipedia domain\"\n    审稿质疑。 ⚠️ CDR/GDA 均无 evidence sentence 标注，无法计算 evi_f1。降级 P2，Limitations 说明。'\n  priority: P2\n  gpu_budget_hours: 60\n  deps: []\n  registry_id: null\n- id: plan_019\n  claim: 3\n  description: 'Scaling seeds supplement: 每个尺度补到 3+ seeds（k=1 RSFT）。 当前缺口：1.7B 需补\n    s43/s44，LLaMA 需补 s43/s44。 4B 已有 4+ seeds 不需补。8B-Qwen 2-seed 已完成（s42+s44）。每个 seed\n    含 SFT + RSFT + no-evidence eval ≈ 5 GPU-h。 目标：每个尺度的 evidence tax 有 mean ± std，scaling\n    claim 有统计力。'\n  priority: P0\n  gpu_budget_hours: 25\n  deps: []\n  registry_id: plan019_1_7b_rsft_s44_r2_eval\n  notes: '1.7B RSFT 3-seed 完成 (2026-05-19): s42=0.5122, s43=0.5109, s44=0.5125,\n    mean=0.5119, std=0.09pp。8B SFT 3-seed: s42=0.5128, s43 DONE (loss=0.5684) eval\n    DONE (ign_f1=0.5324), s44=0.4604。8B RSFT 2-seed: s42=0.5376, s44=0.5451, mean=0.5414,\n    std=0.53pp。No-evidence evals: 1.7B DONE/killed (59.2% truncation), 2048-token retry\n    RUNNING (cuda:3); 8B r1 DONE/killed (cuda:2 冲突), r2 RUNNING (cuda:0); 14B no-evi\n    eval DONE (ign_f1=0.5510)。剩余: LLaMA s43/s44, 8B 3rd RSFT seed。'\n- id: plan_020\n  claim: 3\n  description: 'Evidence tax mechanistic analysis: 解释 WHY 1.7B 获益而 4B 受损。 分析维度：(1)\n    output length distribution with vs without evidence (2) truncation rate 差异（1.7B\n    fair subset 已有基础） (3) hallucination rate（false positive relations 在 with/without\n    evidence 中的比例） (4) per-document evidence 生成对 RE 的影响（按 doc length 分层） 主要是 CPU 分析\n    + 少量补充 eval。'\n  priority: P1\n  gpu_budget_hours: 10\n  deps: []\n  registry_id: null\n- id: plan_021\n  claim: 1\n  description: 'Deep error analysis: 按 relation type / document length / entity count\n    / evidence distance 分层分析。扩展 D070 per-relation EDCR 分析到更多维度。 区分 Main 和 Findings\n    的 insight 层——Main 论文解释 why，Findings 只报 what。'\n  priority: P1\n  gpu_budget_hours: 5\n  deps: []\n  registry_id: null\n- id: plan_022\n  claim: 3\n  description: 'Third model family validation: Mistral-7B 或 Gemma-2-9B 上复现 SFT + RSFT\n    + eval。 验证 scaling pattern 跨第三个模型家族成立。如果 14B（plan_017）已做则优先级下降。'\n  priority: P2\n  gpu_budget_hours: 30\n  deps: []\n  registry_id: null\n- id: plan_023\n  claim: 1\n  description: 'DocKS-RAG / LMRC baseline reproduction: 在相同 eval protocol 下复现 generative\n    DocRE SOTA（DocKS-RAG, LMRC）作为完整对比表。审稿人期望 same-condition comparison。'\n  priority: P2\n  gpu_budget_hours: 10\n  deps: []\n  registry_id: null\n- id: plan_w3_sft_seeds\n  claim: 1\n  description: W3 修复：SFT 4B baseline seed43 + seed44 训练 + eval。 与 canonical SFT (seed42)\n    配对，计算 bootstrap CI + Cohen d， 验证 RSFT +4.92pp 增益的统计显著性。Wave 1 实验。\n  priority: P0\n  gpu_budget_hours: 8\n  deps: []\n  registry_id: wave1_sft_4b_s44_eval_r2\n- id: plan_d112\n  claim: 1\n  description: 'D112: Full RSFT pipeline from SFT s44 base (strongest seed, ign_f1=0.4734).\n    所有现有 4B RSFT 都基于 SFT s42 (最弱 seed)。验证 RSFT 是否能在强 SFT base 上也产生提升。Steps: generate\n    candidates (N=8) → CED score → k=1 filter → RSFT train → D076 eval。'\n  priority: P0\n  gpu_budget_hours: 8\n  deps:\n  - plan_w3_sft_seeds\n  registry_id: d112_rsft_s44_eval\n- id: plan_w18_random\n  claim: 1\n  description: W18 修复：Random k=1 RSFT baseline。从 k=1 候选中随机抽取（不用 NLI 分数）， 验证 NLI-based\n    selection 的价值。如果 random 也提升 → NLI scoring 不关键； 如果 random 不提升 → NLI scoring 是 RSFT\n    有效的关键。Wave 1 实验。\n  priority: P0\n  gpu_budget_hours: 4\n  deps: []\n  registry_id: random_rsft_k1_eval\n",
    "structuredPatch": [
      {
        "oldStart": 269,
        "oldLines": 7,
        "newStart": 269,
        "newLines": 11,
        "lines": [
          "   gpu_budget_hours: 8",
          "   deps:",
          "   - plan_w3_sft_seeds",
          "-  registry_id: d112_rsft_s44_eval",
          "+  registry_id: d112_rsft_s44_eval_bf16",
          "+  notes: '原 QLoRA 版 d112_rsft_s44_train DONE/failed (QLoRA confound: adapter 适应 4-bit",
          "+    量化误差, bf16 eval 下 ign_f1=0.2181 灾难性崩溃)。bf16 重跑: d112_rsft_s44_train_bf16 DONE/success,",
          "+    d112_rsft_s44_eval_bf16 RUNNING (cuda:2)。No-evidence eval: r1/r2 failed (EXIT_CODE=127",
          "+    脚本路径错误), r3 RUNNING (cuda:1)。'",
          " - id: plan_w18_random",
          "   claim: 1",
          "   description: W18 修复：Random k=1 RSFT baseline。从 k=1 候选中随机抽取（不用 NLI 分数）， 验证 NLI-based"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Assistant

_source line 26_

已更新 3 处：

| 实验 | 变更 |
|------|------|
| **plan_017** | 添加 notes: 14B SFT/eval/no-evidence 全部 DONE，evidence tax = -0.03pp |
| **plan_019** | 更新 notes: 1.7B 3-seed 完成 (mean=0.5119)，8B SFT s43 eval DONE (0.5324)，no-evidence eval 状态同步 |
| **plan_d112** | registry_id 从 `d112_rsft_s44_eval` (failed) 改为 `d112_rsft_s44_eval_bf16` (RUNNING)，添加 notes 记录 QLoRA confound 和 bf16 重跑进度 |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "39f8a4ed-6d6b-4c23-9e46-167a8118c922",
  "uuid": "59a907fc-8f83-454e-bf7e-b95c048f98d6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017eF5FV2yZKqYeNnhPMwGNz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5899,
      "cache_read_input_tokens": 39861,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5899
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

_source line 27_

已更新 3 处：

| 实验 | 变更 |
|------|------|
| **plan_017** | 添加 notes: 14B SFT/eval/no-evidence 全部 DONE，evidence tax = -0.03pp |
| **plan_019** | 更新 notes: 1.7B 3-seed 完成 (mean=0.5119)，8B SFT s43 eval DONE (0.5324)，no-evidence eval 状态同步 |
| **plan_d112** | registry_id 从 `d112_rsft_s44_eval` (failed) 改为 `d112_rsft_s44_eval_bf16` (RUNNING)，添加 notes 记录 QLoRA confound 和 bf16 重跑进度 |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 102821,
  "duration_api_ms": 102940,
  "num_turns": 9,
  "stop_reason": "end_turn",
  "session_id": "39f8a4ed-6d6b-4c23-9e46-167a8118c922",
  "total_cost_usd": 0.45955425,
  "usage": {
    "input_tokens": 10,
    "cache_creation_input_tokens": 34121,
    "cache_read_input_tokens": 169512,
    "output_tokens": 6380,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 34121,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 216,
        "cache_read_input_tokens": 39861,
        "cache_creation_input_tokens": 5899,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 5899
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1917,
      "outputTokens": 15,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.0019920000000000003,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 10,
      "outputTokens": 6380,
      "cacheReadInputTokens": 169512,
      "cacheCreationInputTokens": 34121,
      "webSearchRequests": 0,
      "costUSD": 0.45756225,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "2845cd2b-9a03-4288-a392-3b6431c2ac8b"
}
```

</details>

---
