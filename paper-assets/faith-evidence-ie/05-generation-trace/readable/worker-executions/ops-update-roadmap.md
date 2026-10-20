# ops update roadmap

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 34
- **Recorded user turns:** 0
- **Tool calls:** 9
- **Original source:** `logs/workers/worker_ops_update_roadmap_20260519T171259.log`
- **Structured JSON:** [`f7dac0087446143998a9.json`](../../sessions/f7/f7dac0087446143998a9.json)

## Before a recorded user message

34 recorded events

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
  "session_id": "ac6c3eaa-1181-4230-9499-9a3dbe044d7c",
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
  "uuid": "c9f1d890-3be9-4b40-81cc-bf4b4b10f115",
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
  "uuid": "2a456dc9-2441-4415-b484-02823a9edc08",
  "session_id": "ac6c3eaa-1181-4230-9499-9a3dbe044d7c"
}
```

---

### Assistant

_source line 4_

I'll read the current ROADMAP.md first.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ac6c3eaa-1181-4230-9499-9a3dbe044d7c",
  "uuid": "eccd255c-a0a4-4d91-a184-81ca2da15a5c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MuDn2UNEipMhSBX6NZYJnd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13005,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13005
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_017Aafpo5uxdt9AS77Xo3ECn`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file",
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
  "session_id": "ac6c3eaa-1181-4230-9499-9a3dbe044d7c",
  "uuid": "100aab3e-b400-422b-a6dc-523e50918b5e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MuDn2UNEipMhSBX6NZYJnd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13005,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13005
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

_source line 6 · 2026-05-19T17:13:10.429Z_

<details><summary>↩ Tool result · `toolu_017Aafpo5uxdt9AS77Xo3ECn`</summary>

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
  "session_id": "ac6c3eaa-1181-4230-9499-9a3dbe044d7c",
  "uuid": "06224126-6580-4e3c-a7d1-daa364c30a18",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file",
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
Let me read the current ROADMAP.md first, then update it.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ac6c3eaa-1181-4230-9499-9a3dbe044d7c",
  "uuid": "0a33a5d9-a030-4c1f-a314-1e1aeb2497b5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FNkg3ZG2TFZCe8Y9GuCHS1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 712,
      "cache_read_input_tokens": 24846,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 712
      },
      "output_tokens": 40,
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01HcgL5SjxNMxGot8Sibtqu3`</summary>

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
  "session_id": "ac6c3eaa-1181-4230-9499-9a3dbe044d7c",
  "uuid": "558190a4-5f98-423a-8e0d-da850a5dcc64",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FNkg3ZG2TFZCe8Y9GuCHS1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 712,
      "cache_read_input_tokens": 24846,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 712
      },
      "output_tokens": 40,
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

_source line 9 · 2026-05-19T17:13:13.843Z_

<details><summary>↩ Tool result · `toolu_01HcgL5SjxNMxGot8Sibtqu3`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/ROADMAP.md\", \"content\": \"# faith-evidence-ie — Research Dashboard\\n\\n> 最后更新: 2026-05-19 05:43 UTC | 更新原因: D115 8B RSFT 完成 + D114 1.7B Method A 裁决 + D112 进展 + 14B SFT 启动 + Wave 1 全部完成\\n\\n## 核心方向\\nFREIGE: LLM-based evidence-grounded DocRE 系统性研究。3 贡献：RSFT+NLI 有效性 / Decoupling spectrum / Scale-dependent evidence tax。详见 paper_framing.md。\\n\\n## 当前进展\\n- **阶段**: 🚀 Research + 审稿并行（Round 1 = 3.0 Findings，目标 4.0 Main）\\n- **Wave 1**: ✅ 全部完成（SFT s43/s44, GRPO bf16 G=4, Random RSFT）\\n- **Scaling seeds (plan_019)**: 8B 2-seed RSFT 完成（D115: s44=0.5451, variance 0.53pp）；1.7B s43/s44 重跑中（D114 Method A）\\n- **D112 full pipeline**: Step 3 RSFT 训练中 cuda:0（验证 RSFT 在强 SFT base s44 上的泛化性）\\n- **14B SFT (plan_017)**: cuda:1+2 运行中（2-GPU ZeRO-3, D108）\\n- **关键数值汇总**:\\n\\n| Scale | SFT mean (seeds) | RSFT mean (seeds) | Δ ign_f1 | SFT std | RSFT std |\\n|-------|-------------------|--------------------|----------|---------|----------|\\n| 1.7B | 0.4464 (3) | 0.5122 (1, s42 base) | +6.58pp | 2.79pp | — |\\n| 4B | 0.4358 (3) | 0.4482 (3, Method A) | +1.24pp | 3.80pp | 0.51pp |\\n| 8B | 0.4866 (2) | 0.5414 (2, Method A) | +5.48pp | 2.62pp | 0.53pp |\\n\\n- **RSFT 稳定化效应**: 4B variance 3.80→0.51pp (7.5x)，8B variance 2.62→0.53pp (5x)\\n- **CED 价值**: CED RSFT (0.4482) > Random RSFT (0.4114) > SFT (0.3974)，+3.68pp gap\\n- **GRPO**: bf16 ckpt-100 ign_f1=0.4431 无 catastrophic forgetting（D110），QLoRA 是 confound\\n\\n## 投稿目标\\n- **EMNLP 2026 Main** (ARR July cycle, ~July 15-25, **~57 天**)\\n\\n## 实验路线（3 层优先级）\\n\\n### Tier 1 — Main 必要条件\\n| 实验 | Plan ID | 状态 |\\n|------|---------|------|\\n| D102 k=1 方法论修正 | D102 | ✅ 完成 |\\n| SFT 4B s43 + s44 + s42 reeval | plan_w3_sft_seeds | ✅ 完成 (D111) |\\n| GRPO bf16 G=4 clean control | plan_015 | ✅ 完成 (D110/D113) |\\n| Random k=1 RSFT baseline | plan_w18_random | ✅ 完成 (D109) |\\n| 8B RSFT s44 seed expansion | plan_019 (8B) | ✅ 完成 (D115) |\\n| D112 RSFT from SFT s44 | plan_d112 | 🟡 Step 3 训练中 cuda:0 |\\n| 1.7B RSFT s43/s44 重跑 | plan_019 (1.7B) | 🟡 s43_r2 提交中 cuda:3 |\\n| 14B SFT (第 4 尺度) | plan_017 | 🟡 训练中 cuda:1+2 |\\n\\n### Tier 2 — 大幅加分\\n| 实验 | Plan ID | 状态 |\\n|------|---------|------|\\n| 14B RSFT + no-evidence + eval | plan_017 (后续) | pending（等 SFT 完成） |\\n| NLI model ablation | plan_010 | pending |\\n| Evidence tax 机制分析 | plan_020 | pending |\\n| Deep error analysis | plan_021 | pending |\\n\\n### Tier 3 — 锦上添花\\n| 实验 | Plan ID | 状态 |\\n|------|---------|------|\\n| CDR/GDA 跨领域 | plan_018 | P2（无 evidence 标注） |\\n| 第三模型家族 | plan_022 | pending |\\n| DocKS-RAG/LMRC 复现 | plan_023 | pending |\\n\\n## 从 3.0 → 4.0 路径\\n| 里程碑 | 预期评分 | 状态 |\\n|--------|---------|------|\\n| Wave 1 完成 + D112 | 3.0 → 3.5 | 🟡 D112 step 3 训练中 |\\n| + 1.7B/8B multi-seed 统计力 | 3.5 | 🟡 8B done, 1.7B 重跑中 |\\n| + 14B 第 4 尺度档 | 3.5 → 3.75 | 🟡 SFT 训练中 |\\n| + Mechanistic + error analysis | 3.75 → 4.0 | pending |\\n\\n## GPU 预算\\n- 本项目：rtx5090-4x cuda:0-3（4 张 RTX 5090）\\n- 当前：4/4 在用（D112 step3 / 14B SFT×2 / 1.7B RSFT）\\n- 剩余估算：Tier 1 ~15h + Tier 2 ~65h + Tier 3 ~100h\\n\\n## 近期任务\\n- [x] Wave 1 全部完成（SFT seeds, GRPO bf16, Random RSFT）\\n- [x] 8B RSFT s44 eval (D115: 0.5451, variance 压缩 5x)\\n- [x] 4B SFT s42 D076 reeval (D111: 0.3974)\\n- [ ] D112 step 3 → step 4 eval（cuda:0, ~1.5h total）\\n- [ ] 1.7B RSFT s43_r2 + s44_r2 + eval（cuda:3, ~2-3h total）\\n- [ ] 14B SFT 完成 → 14B RSFT + no-evidence + eval（cuda:1+2, ~8h SFT + 后续）\\n- [ ] experiment_plan.yaml 全面同步 registry\\n- [ ] paper_framing.md 更新（D112 结果 + 8B 2-seed + variance 压缩 narrative）\\n- [ ] 重新提交论文审稿\\n\\n## 关键风险\\n- **D112 结果待定**: 如 RSFT-from-s44 > SFT s44 (0.4734) → Claim 1 robust；否则需 reframe\\n- **8B RSFT evidence quality trade-off**: EDCR 从 0.65-0.67 降到 0.62（RE↑/evidence precision↓），论文需讨论\\n- **1.7B surpasses claim**: 现在更强（1.7B RSFT 0.5122 > 8B SFT mean 0.4866 +2.56pp），但仍需 1.7B multi-seed 确认\\n- **14B 显存**: 2-GPU ZeRO-3 已启动且正常（D108 验证），后续 RSFT 可能需要调参\\n- **EDCR 缺人工验证**: plan_013 取消，用 per-relation 分析 + Limitations 缓解\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D118 | 2026-05-19 | D118: \\\"1.7B RSFT surpasses 8B SFT\\\" claim 降级为 \\\"appr | plan019_8b_sft_s43_eval, plan019_1_7b_rsft_s44_r2_eval |\\n| D117 | 2026-05-19 | D117: 14B SFT evidence tax = 0.03pp（本质为零），完成 4 尺度  | plan017_14b_sft_eval_r2, plan017_14b_sft_no_evidence_eval_r2 |\\n| D116 | 2026-05-19 | D116: D112 结果无效（QLoRA confound），必须用 bf16 LoRA 重跑 s | d112_rsft_s44_eval, d112_rsft_s44_train |\\n| D115 | 2026-05-19 | D115: 8B RSFT s44 ign_f1=0.5451 确认 RSFT 跨 seed 稳健， | plan019_8b_rsft_s44_eval, eval_rsft_ced_s42 |\\n| D114 | 2026-05-19 | D114: 1.7B RSFT s43/s44 应使用 Method A（s42 SFT base） | plan019_1_7b_rsft_s43, plan019_1_7b_rsft_s44, d112_rsft_s44_ced_score |\\n| D113 | 2026-05-18 | D113: GRPO bf16 ckpt-100 为最优 checkpoint，ckpt-200 无 | grpo_bf16_g4_ckpt100_eval, grpo_bf16_g4_ckpt200_eval |\\n| D112 | 2026-05-18 | D112: 4B RSFT ign_f1 claim 需重大 reframe——全部 RSFT 基于 | wave1_sft_4b_s43_eval_r2, wave1_sft_4b_s44_eval_r2, eval_rsft_ced_s42 |\\n| D111 | 2026-05-18 | D111: 4B SFT s42 必须用 D076 协议重新 eval，统一三 seed 参考基准 | wave1_sft_4b_s43_eval_r2, wave1_sft_4b_s44_eval_r2 |\\n| D110 | 2026-05-18 | D110: GRPO bf16 ckpt-100 ign_f1=0.4431 无 catastrop | wave1_grpo_bf16_g4, grpo_bf16_g4_ckpt100_eval |\\n| D109 | 2026-05-18 | D109: Random RSFT k=1 ign_f1=0.4114 确证 CED scoring | random_rsft_k1_baseline, eval_flat_nli_seed45 |\\n\\n\", \"total_chars\": 5100, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ac6c3eaa-1181-4230-9499-9a3dbe044d7c",
  "uuid": "1d99f970-f2c6-4e44-8616-2a94cb91257f",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/ROADMAP.md\\\", \\\"content\\\": \\\"# faith-evidence-ie — Research Dashboard\\\\n\\\\n> 最后更新: 2026-05-19 05:43 UTC | 更新原因: D115 8B RSFT 完成 + D114 1.7B Method A 裁决 + D112 进展 + 14B SFT 启动 + Wave 1 全部完成\\\\n\\\\n## 核心方向\\\\nFREIGE: LLM-based evidence-grounded DocRE 系统性研究。3 贡献：RSFT+NLI 有效性 / Decoupling spectrum / Scale-dependent evidence tax。详见 paper_framing.md。\\\\n\\\\n## 当前进展\\\\n- **阶段**: 🚀 Research + 审稿并行（Round 1 = 3.0 Findings，目标 4.0 Main）\\\\n- **Wave 1**: ✅ 全部完成（SFT s43/s44, GRPO bf16 G=4, Random RSFT）\\\\n- **Scaling seeds (plan_019)**: 8B 2-seed RSFT 完成（D115: s44=0.5451, variance 0.53pp）；1.7B s43/s44 重跑中（D114 Method A）\\\\n- **D112 full pipeline**: Step 3 RSFT 训练中 cuda:0（验证 RSFT 在强 SFT base s44 上的泛化性）\\\\n- **14B SFT (plan_017)**: cuda:1+2 运行中（2-GPU ZeRO-3, D108）\\\\n- **关键数值汇总**:\\\\n\\\\n| Scale | SFT mean (seeds) | RSFT mean (seeds) | Δ ign_f1 | SFT std | RSFT std |\\\\n|-------|-------------------|--------------------|----------|---------|----------|\\\\n| 1.7B | 0.4464 (3) | 0.5122 (1, s42 base) | +6.58pp | 2.79pp | — |\\\\n| 4B | 0.4358 (3) | 0.4482 (3, Method A) | +1.24pp | 3.80pp | 0.51pp |\\\\n| 8B | 0.4866 (2) | 0.5414 (2, Method A) | +5.48pp | 2.62pp | 0.53pp |\\\\n\\\\n- **RSFT 稳定化效应**: 4B variance 3.80→0.51pp (7.5x)，8B variance 2.62→0.53pp (5x)\\\\n- **CED 价值**: CED RSFT (0.4482) > Random RSFT (0.4114) > SFT (0.3974)，+3.68pp gap\\\\n- **GRPO**: bf16 ckpt-100 ign_f1=0.4431 无 catastrophic forgetting（D110），QLoRA 是 confound\\\\n\\\\n## 投稿目标\\\\n- **EMNLP 2026 Main** (ARR July cycle, ~July 15-25, **~57 天**)\\\\n\\\\n## 实验路线（3 层优先级）\\\\n\\\\n### Tier 1 — Main 必要条件\\\\n| 实验 | Plan ID | 状态 |\\\\n|------|---------|------|\\\\n| D102 k=1 方法论修正 | D102 | ✅ 完成 |\\\\n| SFT 4B s43 + s44 + s42 reeval | plan_w3_sft_seeds | ✅ 完成 (D111) |\\\\n| GRPO bf16 G=4 clean control | plan_015 | ✅ 完成 (D110/D113) |\\\\n| Random k=1 RSFT baseline | plan_w18_random | ✅ 完成 (D109) |\\\\n| 8B RSFT s44 seed expansion | plan_019 (8B) | ✅ 完成 (D115) |\\\\n| D112 RSFT from SFT s44 | plan_d112 | 🟡 Step 3 训练中 cuda:0 |\\\\n| 1.7B RSFT s43/s44 重跑 | plan_019 (1.7B) | 🟡 s43_r2 提交中 cuda:3 |\\\\n| 14B SFT (第 4 尺度) | plan_017 | 🟡 训练中 cuda:1+2 |\\\\n\\\\n### Tier 2 — 大幅加分\\\\n| 实验 | Plan ID | 状态 |\\\\n|------|---------|------|\\\\n| 14B RSFT + no-evidence + eval | plan_017 (后续) | pending（等 SFT 完成） |\\\\n| NLI model ablation | plan_010 | pending |\\\\n| Evidence tax 机制分析 | plan_020 | pending |\\\\n| Deep error analysis | plan_021 | pending |\\\\n\\\\n### Tier 3 — 锦上添花\\\\n| 实验 | Plan ID | 状态 |\\\\n|------|---------|------|\\\\n| CDR/GDA 跨领域 | plan_018 | P2（无 evidence 标注） |\\\\n| 第三模型家族 | plan_022 | pending |\\\\n| DocKS-RAG/LMRC 复现 | plan_023 | pending |\\\\n\\\\n## 从 3.0 → 4.0 路径\\\\n| 里程碑 | 预期评分 | 状态 |\\\\n|--------|---------|------|\\\\n| Wave 1 完成 + D112 | 3.0 → 3.5 | 🟡 D112 step 3 训练中 |\\\\n| + 1.7B/8B multi-seed 统计力 | 3.5 | 🟡 8B done, 1.7B 重跑中 |\\\\n| + 14B 第 4 尺度档 | 3.5 → 3.75 | 🟡 SFT 训练中 |\\\\n| + Mechanistic + error analysis | 3.75 → 4.0 | pending |\\\\n\\\\n## GPU 预算\\\\n- 本项目：rtx5090-4x cuda:0-3（4 张 RTX 5090）\\\\n- 当前：4/4 在用（D112 step3 / 14B SFT×2 / 1.7B RSFT）\\\\n- 剩余估算：Tier 1 ~15h + Tier 2 ~65h + Tier 3 ~100h\\\\n\\\\n## 近期任务\\\\n- [x] Wave 1 全部完成（SFT seeds, GRPO bf16, Random RSFT）\\\\n- [x] 8B RSFT s44 eval (D115: 0.5451, variance 压缩 5x)\\\\n- [x] 4B SFT s42 D076 reeval (D111: 0.3974)\\\\n- [ ] D112 step 3 → step 4 eval（cuda:0, ~1.5h total）\\\\n- [ ] 1.7B RSFT s43_r2 + s44_r2 + eval（cuda:3, ~2-3h total）\\\\n- [ ] 14B SFT 完成 → 14B RSFT + no-evidence + eval（cuda:1+2, ~8h SFT + 后续）\\\\n- [ ] experiment_plan.yaml 全面同步 registry\\\\n- [ ] paper_framing.md 更新（D112 结果 + 8B 2-seed + variance 压缩 narrative）\\\\n- [ ] 重新提交论文审稿\\\\n\\\\n## 关键风险\\\\n- **D112 结果待定**: 如 RSFT-from-s44 > SFT s44 (0.4734) → Claim 1 robust；否则需 reframe\\\\n- **8B RSFT evidence quality trade-off**: EDCR 从 0.65-0.67 降到 0.62（RE↑/evidence precision↓），论文需讨论\\\\n- **1.7B surpasses claim**: 现在更强（1.7B RSFT 0.5122 > 8B SFT mean 0.4866 +2.56pp），但仍需 1.7B multi-seed 确认\\\\n- **14B 显存**: 2-GPU ZeRO-3 已启动且正常（D108 验证），后续 RSFT 可能需要调参\\\\n- **EDCR 缺人工验证**: plan_013 取消，用 per-relation 分析 + Limitations 缓解\\\\n\\\\n## 关键决策日志\\\\n\\\\n| ID | 日期 | 摘要 | 关联实验 |\\\\n|----|------|------|----------|\\\\n| D118 | 2026-05-19 | D118: \\\\\\\"1.7B RSFT surpasses 8B SFT\\\\\\\" claim 降级为 \\\\\\\"appr | plan019_8b_sft_s43_eval, plan019_1_7b_rsft_s44_r2_eval |\\\\n| D117 | 2026-05-19 | D117: 14B SFT evidence tax = 0.03pp（本质为零），完成 4 尺度  | plan017_14b_sft_eval_r2, plan017_14b_sft_no_evidence_eval_r2 |\\\\n| D116 | 2026-05-19 | D116: D112 结果无效（QLoRA confound），必须用 bf16 LoRA 重跑 s | d112_rsft_s44_eval, d112_rsft_s44_train |\\\\n| D115 | 2026-05-19 | D115: 8B RSFT s44 ign_f1=0.5451 确认 RSFT 跨 seed 稳健， | plan019_8b_rsft_s44_eval, eval_rsft_ced_s42 |\\\\n| D114 | 2026-05-19 | D114: 1.7B RSFT s43/s44 应使用 Method A（s42 SFT base） | plan019_1_7b_rsft_s43, plan019_1_7b_rsft_s44, d112_rsft_s44_ced_score |\\\\n| D113 | 2026-05-18 | D113: GRPO bf16 ckpt-100 为最优 checkpoint，ckpt-200 无 | grpo_bf16_g4_ckpt100_eval, grpo_bf16_g4_ckpt200_eval |\\\\n| D112 | 2026-05-18 | D112: 4B RSFT ign_f1 claim 需重大 reframe——全部 RSFT 基于 | wave1_sft_4b_s43_eval_r2, wave1_sft_4b_s44_eval_r2, eval_rsft_ced_s42 |\\\\n| D111 | 2026-05-18 | D111: 4B SFT s42 必须用 D076 协议重新 eval，统一三 seed 参考基准 | wave1_sft_4b_s43_eval_r2, wave1_sft_4b_s44_eval_r2 |\\\\n| D110 | 2026-05-18 | D110: GRPO bf16 ckpt-100 ign_f1=0.4431 无 catastrop | wave1_grpo_bf16_g4, grpo_bf16_g4_ckpt100_eval |\\\\n| D109 | 2026-05-18 | D109: Random RSFT k=1 ign_f1=0.4114 确证 CED scoring | random_rsft_k1_baseline, eval_flat_nli_seed45 |\\\\n\\\\n\\\", \\\"total_chars\\\": 5100, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/ROADMAP.md\", \"content\": \"# faith-evidence-ie — Research Dashboard\\n\\n> 最后更新: 2026-05-19 05:43 UTC | 更新原因: D115 8B RSFT 完成 + D114 1.7B Method A 裁决 + D112 进展 + 14B SFT 启动 + Wave 1 全部完成\\n\\n## 核心方向\\nFREIGE: LLM-based evidence-grounded DocRE 系统性研究。3 贡献：RSFT+NLI 有效性 / Decoupling spectrum / Scale-dependent evidence tax。详见 paper_framing.md。\\n\\n## 当前进展\\n- **阶段**: 🚀 Research + 审稿并行（Round 1 = 3.0 Findings，目标 4.0 Main）\\n- **Wave 1**: ✅ 全部完成（SFT s43/s44, GRPO bf16 G=4, Random RSFT）\\n- **Scaling seeds (plan_019)**: 8B 2-seed RSFT 完成（D115: s44=0.5451, variance 0.53pp）；1.7B s43/s44 重跑中（D114 Method A）\\n- **D112 full pipeline**: Step 3 RSFT 训练中 cuda:0（验证 RSFT 在强 SFT base s44 上的泛化性）\\n- **14B SFT (plan_017)**: cuda:1+2 运行中（2-GPU ZeRO-3, D108）\\n- **关键数值汇总**:\\n\\n| Scale | SFT mean (seeds) | RSFT mean (seeds) | Δ ign_f1 | SFT std | RSFT std |\\n|-------|-------------------|--------------------|----------|---------|----------|\\n| 1.7B | 0.4464 (3) | 0.5122 (1, s42 base) | +6.58pp | 2.79pp | — |\\n| 4B | 0.4358 (3) | 0.4482 (3, Method A) | +1.24pp | 3.80pp | 0.51pp |\\n| 8B | 0.4866 (2) | 0.5414 (2, Method A) | +5.48pp | 2.62pp | 0.53pp |\\n\\n- **RSFT 稳定化效应**: 4B variance 3.80→0.51pp (7.5x)，8B variance 2.62→0.53pp (5x)\\n- **CED 价值**: CED RSFT (0.4482) > Random RSFT (0.4114) > SFT (0.3974)，+3.68pp gap\\n- **GRPO**: bf16 ckpt-100 ign_f1=0.4431 无 catastrophic forgetting（D110），QLoRA 是 confound\\n\\n## 投稿目标\\n- **EMNLP 2026 Main** (ARR July cycle, ~July 15-25, **~57 天**)\\n\\n## 实验路线（3 层优先级）\\n\\n### Tier 1 — Main 必要条件\\n| 实验 | Plan ID | 状态 |\\n|------|---------|------|\\n| D102 k=1 方法论修正 | D102 | ✅ 完成 |\\n| SFT 4B s43 + s44 + s42 reeval | plan_w3_sft_seeds | ✅ 完成 (D111) |\\n| GRPO bf16 G=4 clean control | plan_015 | ✅ 完成 (D110/D113) |\\n| Random k=1 RSFT baseline | plan_w18_random | ✅ 完成 (D109) |\\n| 8B RSFT s44 seed expansion | plan_019 (8B) | ✅ 完成 (D115) |\\n| D112 RSFT from SFT s44 | plan_d112 | 🟡 Step 3 训练中 cuda:0 |\\n| 1.7B RSFT s43/s44 重跑 | plan_019 (1.7B) | 🟡 s43_r2 提交中 cuda:3 |\\n| 14B SFT (第 4 尺度) | plan_017 | 🟡 训练中 cuda:1+2 |\\n\\n### Tier 2 — 大幅加分\\n| 实验 | Plan ID | 状态 |\\n|------|---------|------|\\n| 14B RSFT + no-evidence + eval | plan_017 (后续) | pending（等 SFT 完成） |\\n| NLI model ablation | plan_010 | pending |\\n| Evidence tax 机制分析 | plan_020 | pending |\\n| Deep error analysis | plan_021 | pending |\\n\\n### Tier 3 — 锦上添花\\n| 实验 | Plan ID | 状态 |\\n|------|---------|------|\\n| CDR/GDA 跨领域 | plan_018 | P2（无 evidence 标注） |\\n| 第三模型家族 | plan_022 | pending |\\n| DocKS-RAG/LMRC 复现 | plan_023 | pending |\\n\\n## 从 3.0 → 4.0 路径\\n| 里程碑 | 预期评分 | 状态 |\\n|--------|---------|------|\\n| Wave 1 完成 + D112 | 3.0 → 3.5 | 🟡 D112 step 3 训练中 |\\n| + 1.7B/8B multi-seed 统计力 | 3.5 | 🟡 8B done, 1.7B 重跑中 |\\n| + 14B 第 4 尺度档 | 3.5 → 3.75 | 🟡 SFT 训练中 |\\n| + Mechanistic + error analysis | 3.75 → 4.0 | pending |\\n\\n## GPU 预算\\n- 本项目：rtx5090-4x cuda:0-3（4 张 RTX 5090）\\n- 当前：4/4 在用（D112 step3 / 14B SFT×2 / 1.7B RSFT）\\n- 剩余估算：Tier 1 ~15h + Tier 2 ~65h + Tier 3 ~100h\\n\\n## 近期任务\\n- [x] Wave 1 全部完成（SFT seeds, GRPO bf16, Random RSFT）\\n- [x] 8B RSFT s44 eval (D115: 0.5451, variance 压缩 5x)\\n- [x] 4B SFT s42 D076 reeval (D111: 0.3974)\\n- [ ] D112 step 3 → step 4 eval（cuda:0, ~1.5h total）\\n- [ ] 1.7B RSFT s43_r2 + s44_r2 + eval（cuda:3, ~2-3h total）\\n- [ ] 14B SFT 完成 → 14B RSFT + no-evidence + eval（cuda:1+2, ~8h SFT + 后续）\\n- [ ] experiment_plan.yaml 全面同步 registry\\n- [ ] paper_framing.md 更新（D112 结果 + 8B 2-seed + variance 压缩 narrative）\\n- [ ] 重新提交论文审稿\\n\\n## 关键风险\\n- **D112 结果待定**: 如 RSFT-from-s44 > SFT s44 (0.4734) → Claim 1 robust；否则需 reframe\\n- **8B RSFT evidence quality trade-off**: EDCR 从 0.65-0.67 降到 0.62（RE↑/evidence precision↓），论文需讨论\\n- **1.7B surpasses claim**: 现在更强（1.7B RSFT 0.5122 > 8B SFT mean 0.4866 +2.56pp），但仍需 1.7B multi-seed 确认\\n- **14B 显存**: 2-GPU ZeRO-3 已启动且正常（D108 验证），后续 RSFT 可能需要调参\\n- **EDCR 缺人工验证**: plan_013 取消，用 per-relation 分析 + Limitations 缓解\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D118 | 2026-05-19 | D118: \\\"1.7B RSFT surpasses 8B SFT\\\" claim 降级为 \\\"appr | plan019_8b_sft_s43_eval, plan019_1_7b_rsft_s44_r2_eval |\\n| D117 | 2026-05-19 | D117: 14B SFT evidence tax = 0.03pp（本质为零），完成 4 尺度  | plan017_14b_sft_eval_r2, plan017_14b_sft_no_evidence_eval_r2 |\\n| D116 | 2026-05-19 | D116: D112 结果无效（QLoRA confound），必须用 bf16 LoRA 重跑 s | d112_rsft_s44_eval, d112_rsft_s44_train |\\n| D115 | 2026-05-19 | D115: 8B RSFT s44 ign_f1=0.5451 确认 RSFT 跨 seed 稳健， | plan019_8b_rsft_s44_eval, eval_rsft_ced_s42 |\\n| D114 | 2026-05-19 | D114: 1.7B RSFT s43/s44 应使用 Method A（s42 SFT base） | plan019_1_7b_rsft_s43, plan019_1_7b_rsft_s44, d112_rsft_s44_ced_score |\\n| D113 | 2026-05-18 | D113: GRPO bf16 ckpt-100 为最优 checkpoint，ckpt-200 无 | grpo_bf16_g4_ckpt100_eval, grpo_bf16_g4_ckpt200_eval |\\n| D112 | 2026-05-18 | D112: 4B RSFT ign_f1 claim 需重大 reframe——全部 RSFT 基于 | wave1_sft_4b_s43_eval_r2, wave1_sft_4b_s44_eval_r2, eval_rsft_ced_s42 |\\n| D111 | 2026-05-18 | D111: 4B SFT s42 必须用 D076 协议重新 eval，统一三 seed 参考基准 | wave1_sft_4b_s43_eval_r2, wave1_sft_4b_s44_eval_r2 |\\n| D110 | 2026-05-18 | D110: GRPO bf16 ckpt-100 ign_f1=0.4431 无 catastrop | wave1_grpo_bf16_g4, grpo_bf16_g4_ckpt100_eval |\\n| D109 | 2026-05-18 | D109: Random RSFT k=1 ign_f1=0.4114 确证 CED scoring | random_rsft_k1_baseline, eval_flat_nli_seed45 |\\n\\n\", \"total_chars\": 5100, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 10_

<details><summary>Logged reasoning block</summary>

```text
Now I have the current ROADMAP.md. Let me update it based on the task requirements:

1. 14B evidence tax discovery (D117) - already partially noted
2. "1.7B surpasses" claim downgrade (D118) - need to weaken the claim
3. D112 completion - step 4 eval done, ign_f1=0.5152, +4.18pp over SFT s44 baseline (0.4734)
4. Current GPU distribution
5. Scaling table update - add 14B row, update 8B to 3-seed mean, add D112 result


6. Task list update

I'm going through the document systematically to make these updates. The scaling table needs the 8B SFT mean adjusted from 0.4866 to 0.5019 based on three seeds, I'll add the 14B row with its evidence tax findings, and incorporate the D112 results for the 4B model. I also need to soften the language around the 1.7B surpassing claim and update the GPU allocation details, plus I'm checking the RSFT variance comparison for the 8B model.

Looking at the actual numbers from the data, the 8B SFT shows a standard deviation of 0.0372 across three seeds while RSFT comes in at 0.005, which is a meaningful difference in stability I should highlight.

For the 1.7B comparison claim, the RSFT score of 0.5122 versus the 8B SFT mean of 0.5019 gives only a 1.03 percentage point difference with a p-value around 0.34—not statistically significant, so I need to soften that language to say they're comparable rather than claiming one surpasses the other.

Now I'm checking the variance numbers: the 8B SFT runs across three seeds show a standard deviation of 3.72 percentage points, while the RSFT variance from the earlier experiment was much tighter at 0.53 percentage points. With those numbers confirmed, I can move forward with updating the roadmap to reflect the completed experiments and the revised claims.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ac6c3eaa-1181-4230-9499-9a3dbe044d7c",
  "uuid": "02a0756d-4b21-4be0-9a77-b4323e4e2dca",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016jbuCcEgJXkr5V1iGGXtZT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3455,
      "cache_read_input_tokens": 25558,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3455
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

_source line 11_

Now I'll write the updated ROADMAP.md.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ac6c3eaa-1181-4230-9499-9a3dbe044d7c",
  "uuid": "10d4a6b4-1257-4d59-a1a5-4dbf791ee051",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016jbuCcEgJXkr5V1iGGXtZT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3455,
      "cache_read_input_tokens": 25558,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3455
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

_source line 12_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__save_project_file · `toolu_01UqMbVys6SyF9c8mJTGFcwF`</summary>

```json
{
  "project": "faith-evidence-ie",
  "file": "ROADMAP.md",
  "content": "# faith-evidence-ie — Research Dashboard\n\n> 最后更新: 2026-05-19 09:30 UTC | 更新原因: D117 14B evidence tax=0 + D118 1.7B claim 降级 + D112 bf16 完成 (0.5152) + 8B SFT 3-seed + scaling table 更新\n\n## 核心方向\nFREIGE: LLM-based evidence-grounded DocRE 系统性研究。3 贡献：RSFT+NLI 有效性 / Decoupling spectrum / Scale-dependent evidence tax。详见 paper_framing.md。\n\n## 当前进展\n- **阶段**: 🚀 Research + 审稿并行（Round 1 = 3.0 Findings，目标 4.0 Main）\n- **Wave 1**: ✅ 全部完成（SFT seeds, GRPO bf16, Random RSFT）\n- **Scaling seeds (plan_019)**: 8B 2-seed RSFT 完成（D115: s44=0.5451, variance 0.53pp）；8B SFT 3-seed 完成（mean=0.5019±3.72pp）\n- **D112 full pipeline**: ✅ 完成（bf16 LoRA RSFT from SFT s44: ign_f1=0.5152, +4.18pp over SFT s44 baseline 0.4734）\n- **14B SFT (plan_017)**: ✅ 完成（D117: with-evidence 0.5507, no-evidence 0.551, evidence tax=0.03pp≈0）\n- **D118 claim 降级**: 1.7B RSFT (0.5122) vs 8B SFT mean (0.5019) Δ=+1.03pp, p≈0.34 不显著，降级为 \"comparable / on par with\"\n- **关键数值汇总**:\n\n| Scale | SFT mean (seeds) | RSFT mean (seeds) | Δ ign_f1 | SFT std | RSFT std |\n|-------|-------------------|--------------------|----------|---------|----------|\n| 1.7B | 0.4464 (3) | 0.5122 (1, s42 base) | +6.58pp | 2.79pp | — |\n| 4B | 0.4358 (3) | 0.4482 (3, Method A) / 0.5152 (1, Method B) | +1.24pp / +4.18pp (vs s44) | 3.80pp | 0.51pp |\n| 8B | 0.5019 (3) | 0.5414 (2, Method A) | +3.95pp | 3.72pp | 0.53pp |\n| 14B | 0.5507 (1) | pending | — | — | — |\n\n- **14B evidence tax**: 0.03pp（本质为零），14B 容量足够同时输出 evidence 和 RE\n- **RSFT variance 稳定化**: 8B SFT std=3.72pp → RSFT std=0.53pp (7x)；4B SFT std=3.80pp → RSFT std=0.51pp (7.5x)\n- **CED 价值**: CED RSFT (0.4482) > Random RSFT (0.4114) > SFT (0.3974)，+3.68pp gap\n- **GRPO**: bf16 ckpt-100 ign_f1=0.4431 无 catastrophic forgetting（D110），QLoRA 是 confound\n\n## 投稿目标\n- **EMNLP 2026 Main** (ARR July cycle, ~July 15-25, **~57 天**)\n\n## 实验路线（3 层优先级）\n\n### Tier 1 — Main 必要条件\n| 实验 | Plan ID | 状态 |\n|------|---------|------|\n| D102 k=1 方法论修正 | D102 | ✅ 完成 |\n| SFT 4B s43 + s44 + s42 reeval | plan_w3_sft_seeds | ✅ 完成 (D111) |\n| GRPO bf16 G=4 clean control | plan_015 | ✅ 完成 (D110/D113) |\n| Random k=1 RSFT baseline | plan_w18_random | ✅ 完成 (D109) |\n| 8B RSFT s44 seed expansion | plan_019 (8B) | ✅ 完成 (D115) |\n| 8B SFT s43 eval | plan_019 | ✅ 完成 (ign_f1=0.5324) |\n| D112 RSFT from SFT s44 (bf16) | plan_d112 | ✅ 完成 (ign_f1=0.5152) |\n| 14B SFT (第 4 尺度) | plan_017 | ✅ 完成 (D117: 0.5507, tax=0.03pp) |\n| 1.7B RSFT s43/s44 重跑 | plan_019 (1.7B) | 🟡 进行中 |\n\n### Tier 2 — 大幅加分\n| 实验 | Plan ID | 状态 |\n|------|---------|------|\n| 14B RSFT + no-evidence + eval | plan_017 (后续) | pending（等启动） |\n| 8B RSFT s43 补齐第 3 seed | plan_019 | pending |\n| NLI model ablation | plan_010 | pending |\n| Evidence tax 机制分析 | plan_020 | pending |\n| Deep error analysis | plan_021 | pending |\n\n### Tier 3 — 锦上添花\n| 实验 | Plan ID | 状态 |\n|------|---------|------|\n| CDR/GDA 跨领域 | plan_018 | P2（无 evidence 标注） |\n| 第三模型家族 | plan_022 | pending |\n| DocKS-RAG/LMRC 复现 | plan_023 | pending |\n\n## 从 3.0 → 4.0 路径\n| 里程碑 | 预期评分 | 状态 |\n|--------|---------|------|\n| Wave 1 完成 + D112 | 3.0 → 3.5 | ✅ D112 完成 (0.5152) |\n| + 1.7B/8B multi-seed 统计力 | 3.5 | 🟡 8B 3-seed done, 1.7B 进行中 |\n| + 14B 第 4 尺度档 | 3.5 → 3.75 | ✅ SFT 完成 (0.5507), RSFT pending |\n| + Mechanistic + error analysis | 3.75 → 4.0 | pending |\n\n## GPU 分布\n- cuda:0: 8B RSFT no-evidence eval r2（接近完成）\n- cuda:1: D112 no-evidence eval r3（44%）\n- cuda:2: 空闲\n- cuda:3: 1.7B no-evidence eval 2048（38%）\n\n## 近期任务\n- [x] Wave 1 全部完成（SFT seeds, GRPO bf16, Random RSFT）\n- [x] 8B RSFT s44 eval (D115: 0.5451, variance 压缩 5x)\n- [x] 4B SFT s42 D076 reeval (D111: 0.3974)\n- [x] D112 step 4 eval 完成 (bf16 LoRA: ign_f1=0.5152, +4.18pp)\n- [x] 8B SFT s43 eval 完成 (ign_f1=0.5324)\n- [x] 14B SFT eval 完成 (D117: ign_f1=0.5507, evidence tax=0.03pp)\n- [ ] 1.7B no-evidence eval 2048 重跑（排除截断，cuda:3）\n- [ ] 8B RSFT no-evidence eval（cuda:0，接近完成）\n- [ ] D112 no-evidence eval r3（cuda:1，44%）\n- [ ] 14B RSFT pipeline（待启动）\n- [ ] 8B RSFT s43 补齐第 3 seed\n- [ ] experiment_plan.yaml 全面同步 registry\n- [ ] paper_framing.md 更新（D112 + D117 + D118 narrative 调整）\n- [ ] 重新提交论文审稿\n\n## 关键风险\n- **D112 结果**: ✅ 已确认 RSFT-from-s44 (0.5152) > SFT s44 (0.4734) +4.18pp，Claim 1 robust\n- **1.7B \"surpasses\" claim 已降级 (D118)**: 1.7B RSFT vs 8B SFT Δ=+1.03pp, p≈0.34 不显著，改为 \"comparable\"；RSFT variance stabilization (SFT std=3.72pp vs RSFT std=0.53pp) 作为独立发现\n- **14B evidence tax = 0 (D117)**: 积极结果，14B 容量足够，论文 Claim 3 需调整为 \"tax scales inversely with model capacity\"\n- **8B RSFT evidence quality trade-off**: EDCR 从 0.65-0.67 降到 0.62（RE↑/evidence precision↓），论文需讨论\n- **14B RSFT 待启动**: SFT 已完成，RSFT pipeline 是 Tier 2 首要任务\n- **EDCR 缺人工验证**: plan_013 取消，用 per-relation 分析 + Limitations 缓解\n\n## 关键决策日志\n\n| ID | 日期 | 摘要 | 关联实验 |\n|----|------|------|----------|\n| D118 | 2026-05-19 | D118: \"1.7B RSFT surpasses 8B SFT\" claim 降级为 \"appr | plan019_8b_sft_s43_eval, plan019_1_7b_rsft_s44_r2_eval |\n| D117 | 2026-05-19 | D117: 14B SFT evidence tax = 0.03pp（本质为零），完成 4 尺度  | plan017_14b_sft_eval_r2, plan017_14b_sft_no_evidence_eval_r2 |\n| D116 | 2026-05-19 | D116: D112 结果无效（QLoRA confound），必须用 bf16 LoRA 重跑 s | d112_rsft_s44_eval, d112_rsft_s44_train |\n| D115 | 2026-05-19 | D115: 8B RSFT s44 ign_f1=0.5451 确认 RSFT 跨 seed 稳健， | plan019_8b_rsft_s44_eval, eval_rsft_ced_s42 |\n| D114 | 2026-05-19 | D114: 1.7B RSFT s43/s44 应使用 Method A（s42 SFT base） | plan019_1_7b_rsft_s43, plan019_1_7b_rsft_s44, d112_rsft_s44_ced_score |\n| D113 | 2026-05-18 | D113: GRPO bf16 ckpt-100 为最优 checkpoint，ckpt-200 无 | grpo_bf16_g4_ckpt100_eval, grpo_bf16_g4_ckpt200_eval |\n| D112 | 2026-05-18 | D112: 4B RSFT ign_f1 claim 需重大 reframe——全部 RSFT 基于 | wave1_sft_4b_s43_eval_r2, wave1_sft_4b_s44_eval_r2, eval_rsft_ced_s42 |\n| D111 | 2026-05-18 | D111: 4B SFT s42 必须用 D076 协议重新 eval，统一三 seed 参考基准 | wave1_sft_4b_s43_eval_r2, wave1_sft_4b_s44_eval_r2 |\n| D110 | 2026-05-18 | D110: GRPO bf16 ckpt-100 ign_f1=0.4431 无 catastrop | wave1_grpo_bf16_g4, grpo_bf16_g4_ckpt100_eval |\n| D109 | 2026-05-18 | D109: Random RSFT k=1 ign_f1=0.4114 确证 CED scoring | random_rsft_k1_baseline, eval_flat_nli_seed45 |\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ac6c3eaa-1181-4230-9499-9a3dbe044d7c",
  "uuid": "6e7212d5-3071-4898-8fa7-fd63d15b1469",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016jbuCcEgJXkr5V1iGGXtZT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3455,
      "cache_read_input_tokens": 25558,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3455
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

_source line 13 · 2026-05-19T17:14:16.884Z_

<details><summary>↩ Tool result · `toolu_01UqMbVys6SyF9c8mJTGFcwF`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"file 'ROADMAP.md' is not writable via save_project_file. Writable: ['memory.md', 'paper_framing.md', 'writing_plan.yaml']. Use update_roadmap instead.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ac6c3eaa-1181-4230-9499-9a3dbe044d7c",
  "uuid": "a38d6c46-61e7-4ec2-a897-d2e01145962d",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"file 'ROADMAP.md' is not writable via save_project_file. Writable: ['memory.md', 'paper_framing.md', 'writing_plan.yaml']. Use update_roadmap instead.\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"file 'ROADMAP.md' is not writable via save_project_file. Writable: ['memory.md', 'paper_framing.md', 'writing_plan.yaml']. Use update_roadmap instead.\", \"metadata\": {}}"
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
Need to use update_roadmap instead. Let me find that tool.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ac6c3eaa-1181-4230-9499-9a3dbe044d7c",
  "uuid": "58b8a6d7-851e-4c31-b55f-f3fe17e96828",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019iFqN9LRHTzKcWYP8C2oxL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4872,
      "cache_read_input_tokens": 29013,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4872
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

需要用 `update_roadmap` 工具。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ac6c3eaa-1181-4230-9499-9a3dbe044d7c",
  "uuid": "33f23f17-9a2e-43a5-8bf0-c89afdb5d8ed",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019iFqN9LRHTzKcWYP8C2oxL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4872,
      "cache_read_input_tokens": 29013,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4872
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01HLW4fzjv2CPLeFjAfdaPdc`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__update_registry",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ac6c3eaa-1181-4230-9499-9a3dbe044d7c",
  "uuid": "9dfd8cda-dd75-485b-9bef-d4465c85942c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019iFqN9LRHTzKcWYP8C2oxL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4872,
      "cache_read_input_tokens": 29013,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4872
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

_source line 17 · 2026-05-19T17:14:21.187Z_

<details><summary>↩ Tool result · `toolu_01HLW4fzjv2CPLeFjAfdaPdc`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__update_registry"
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
  "session_id": "ac6c3eaa-1181-4230-9499-9a3dbe044d7c",
  "uuid": "de3d9ff7-13e7-48b2-baeb-c1873f441198",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__update_registry"
    ],
    "query": "select:mcp__agent-ml-research__update_registry",
    "total_deferred_tools": 25
  }
}
```

</details>

---

### Tool call

_source line 18_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01WBbJZ3MKB9ErJGhZCkpsLs`</summary>

```json
{
  "query": "update_roadmap",
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
  "session_id": "ac6c3eaa-1181-4230-9499-9a3dbe044d7c",
  "uuid": "cedbaa31-a650-489f-8865-53ab972821f3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019iFqN9LRHTzKcWYP8C2oxL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4872,
      "cache_read_input_tokens": 29013,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4872
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

_source line 19 · 2026-05-19T17:14:25.325Z_

<details><summary>↩ Tool result · `toolu_01WBbJZ3MKB9ErJGhZCkpsLs`</summary>

````text
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
  "session_id": "ac6c3eaa-1181-4230-9499-9a3dbe044d7c",
  "uuid": "c7e14871-cbd6-47ae-85f2-e7592174c222",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "update_roadmap",
    "total_deferred_tools": 25
  }
}
```

</details>

---

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_011qMaMbxUhfAUBNzwctrPsz`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__update_roadmap",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ac6c3eaa-1181-4230-9499-9a3dbe044d7c",
  "uuid": "4cfb287e-8093-4fd3-8e4f-1a4d0e8b4db7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RNxxApt3VXQqCjtJJUukWE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 990,
      "cache_read_input_tokens": 33885,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 990
      },
      "output_tokens": 71,
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

_source line 21 · 2026-05-19T17:14:31.423Z_

<details><summary>↩ Tool result · `toolu_011qMaMbxUhfAUBNzwctrPsz`</summary>

```text
No matching deferred tools found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ac6c3eaa-1181-4230-9499-9a3dbe044d7c",
  "uuid": "72f1abc1-ee44-4217-87a4-734761eb30f2",
  "tool_use_result": {
    "matches": [],
    "query": "select:mcp__agent-ml-research__update_roadmap",
    "total_deferred_tools": 25
  }
}
```

</details>

---

### Assistant

_source line 22_

<details><summary>Logged reasoning block</summary>

```text
The tool isn't available as a deferred tool. Let me try a different search.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ac6c3eaa-1181-4230-9499-9a3dbe044d7c",
  "uuid": "87e91c26-0e3d-4dd2-baea-e0e3a1a8cab8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JyEiJLmUCuASTKkGykF7Vx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 107,
      "cache_read_input_tokens": 34875,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 107
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

_source line 23_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Bydnjx5TtweSq3dDu5Uf24`</summary>

```json
{
  "query": "roadmap",
  "max_results": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ac6c3eaa-1181-4230-9499-9a3dbe044d7c",
  "uuid": "c5b57b0a-60ab-483c-b47c-8cea59027929",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JyEiJLmUCuASTKkGykF7Vx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 107,
      "cache_read_input_tokens": 34875,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 107
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

_source line 24 · 2026-05-19T17:14:34.492Z_

<details><summary>↩ Tool result · `toolu_01Bydnjx5TtweSq3dDu5Uf24`</summary>

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
  "session_id": "ac6c3eaa-1181-4230-9499-9a3dbe044d7c",
  "uuid": "9271561a-f6c6-42c3-bf8a-b038bbbf3854",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "roadmap",
    "total_deferred_tools": 25
  }
}
```

</details>

---

### Assistant

_source line 25_

<details><summary>Logged reasoning block</summary>

```text
The `update_roadmap` tool isn't showing up in ToolSearch. Let me try to find it with a different query, or just directly write the file since I know its path.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ac6c3eaa-1181-4230-9499-9a3dbe044d7c",
  "uuid": "185c4e3e-22fc-49e6-9437-98388f64231a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UJokF8j186d5UtjAHHFEyb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 803,
      "cache_read_input_tokens": 34982,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 803
      },
      "output_tokens": 34,
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

_source line 26_

`update_roadmap` 工具未找到。直接写文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ac6c3eaa-1181-4230-9499-9a3dbe044d7c",
  "uuid": "932d8d40-4e5a-4caf-9480-4f3bdcd1862f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UJokF8j186d5UtjAHHFEyb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 803,
      "cache_read_input_tokens": 34982,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 803
      },
      "output_tokens": 34,
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

_source line 27_

<details open><summary>🔧 Tool call — Read · `toolu_017pdtn6uDUBB94tR1dpJbMt`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/ROADMAP.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ac6c3eaa-1181-4230-9499-9a3dbe044d7c",
  "uuid": "e039d739-0d41-49d6-a591-6647e6f1b53b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UJokF8j186d5UtjAHHFEyb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 803,
      "cache_read_input_tokens": 34982,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 803
      },
      "output_tokens": 34,
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

_source line 28 · 2026-05-19T17:14:40.955Z_

<details><summary>↩ Tool result · `toolu_017pdtn6uDUBB94tR1dpJbMt`</summary>

```text
1	# faith-evidence-ie — Research Dashboard
2	
3	> 最后更新: 2026-05-19 05:43 UTC | 更新原因: D115 8B RSFT 完成 + D114 1.7B Method A 裁决 + D112 进展 + 14B SFT 启动 + Wave 1 全部完成
4	
5	## 核心方向
6	FREIGE: LLM-based evidence-grounded DocRE 系统性研究。3 贡献：RSFT+NLI 有效性 / Decoupling spectrum / Scale-dependent evidence tax。详见 paper_framing.md。
7	
8	## 当前进展
9	- **阶段**: 🚀 Research + 审稿并行（Round 1 = 3.0 Findings，目标 4.0 Main）
10	- **Wave 1**: ✅ 全部完成（SFT s43/s44, GRPO bf16 G=4, Random RSFT）
11	- **Scaling seeds (plan_019)**: 8B 2-seed RSFT 完成（D115: s44=0.5451, variance 0.53pp）；1.7B s43/s44 重跑中（D114 Method A）
12	- **D112 full pipeline**: Step 3 RSFT 训练中 cuda:0（验证 RSFT 在强 SFT base s44 上的泛化性）
13	- **14B SFT (plan_017)**: cuda:1+2 运行中（2-GPU ZeRO-3, D108）
14	- **关键数值汇总**:
15	
16	| Scale | SFT mean (seeds) | RSFT mean (seeds) | Δ ign_f1 | SFT std | RSFT std |
17	|-------|-------------------|--------------------|----------|---------|----------|
18	| 1.7B | 0.4464 (3) | 0.5122 (1, s42 base) | +6.58pp | 2.79pp | — |
19	| 4B | 0.4358 (3) | 0.4482 (3, Method A) | +1.24pp | 3.80pp | 0.51pp |
20	| 8B | 0.4866 (2) | 0.5414 (2, Method A) | +5.48pp | 2.62pp | 0.53pp |
21	
22	- **RSFT 稳定化效应**: 4B variance 3.80→0.51pp (7.5x)，8B variance 2.62→0.53pp (5x)
23	- **CED 价值**: CED RSFT (0.4482) > Random RSFT (0.4114) > SFT (0.3974)，+3.68pp gap
24	- **GRPO**: bf16 ckpt-100 ign_f1=0.4431 无 catastrophic forgetting（D110），QLoRA 是 confound
25	
26	## 投稿目标
27	- **EMNLP 2026 Main** (ARR July cycle, ~July 15-25, **~57 天**)
28	
29	## 实验路线（3 层优先级）
30	
31	### Tier 1 — Main 必要条件
32	| 实验 | Plan ID | 状态 |
33	|------|---------|------|
34	| D102 k=1 方法论修正 | D102 | ✅ 完成 |
35	| SFT 4B s43 + s44 + s42 reeval | plan_w3_sft_seeds | ✅ 完成 (D111) |
36	| GRPO bf16 G=4 clean control | plan_015 | ✅ 完成 (D110/D113) |
37	| Random k=1 RSFT baseline | plan_w18_random | ✅ 完成 (D109) |
38	| 8B RSFT s44 seed expansion | plan_019 (8B) | ✅ 完成 (D115) |
39	| D112 RSFT from SFT s44 | plan_d112 | 🟡 Step 3 训练中 cuda:0 |
40	| 1.7B RSFT s43/s44 重跑 | plan_019 (1.7B) | 🟡 s43_r2 提交中 cuda:3 |
41	| 14B SFT (第 4 尺度) | plan_017 | 🟡 训练中 cuda:1+2 |
42	
43	### Tier 2 — 大幅加分
44	| 实验 | Plan ID | 状态 |
45	|------|---------|------|
46	| 14B RSFT + no-evidence + eval | plan_017 (后续) | pending（等 SFT 完成） |
47	| NLI model ablation | plan_010 | pending |
48	| Evidence tax 机制分析 | plan_020 | pending |
49	| Deep error analysis | plan_021 | pending |
50	
51	### Tier 3 — 锦上添花
52	| 实验 | Plan ID | 状态 |
53	|------|---------|------|
54	| CDR/GDA 跨领域 | plan_018 | P2（无 evidence 标注） |
55	| 第三模型家族 | plan_022 | pending |
56	| DocKS-RAG/LMRC 复现 | plan_023 | pending |
57	
58	## 从 3.0 → 4.0 路径
59	| 里程碑 | 预期评分 | 状态 |
60	|--------|---------|------|
61	| Wave 1 完成 + D112 | 3.0 → 3.5 | 🟡 D112 step 3 训练中 |
62	| + 1.7B/8B multi-seed 统计力 | 3.5 | 🟡 8B done, 1.7B 重跑中 |
63	| + 14B 第 4 尺度档 | 3.5 → 3.75 | 🟡 SFT 训练中 |
64	| + Mechanistic + error analysis | 3.75 → 4.0 | pending |
65	
66	## GPU 预算
67	- 本项目：rtx5090-4x cuda:0-3（4 张 RTX 5090）
68	- 当前：4/4 在用（D112 step3 / 14B SFT×2 / 1.7B RSFT）
69	- 剩余估算：Tier 1 ~15h + Tier 2 ~65h + Tier 3 ~100h
70	
71	## 近期任务
72	- [x] Wave 1 全部完成（SFT seeds, GRPO bf16, Random RSFT）
73	- [x] 8B RSFT s44 eval (D115: 0.5451, variance 压缩 5x)
74	- [x] 4B SFT s42 D076 reeval (D111: 0.3974)
75	- [ ] D112 step 3 → step 4 eval（cuda:0, ~1.5h total）
76	- [ ] 1.7B RSFT s43_r2 + s44_r2 + eval（cuda:3, ~2-3h total）
77	- [ ] 14B SFT 完成 → 14B RSFT + no-evidence + eval（cuda:1+2, ~8h SFT + 后续）
78	- [ ] experiment_plan.yaml 全面同步 registry
79	- [ ] paper_framing.md 更新（D112 结果 + 8B 2-seed + variance 压缩 narrative）
80	- [ ] 重新提交论文审稿
81	
82	## 关键风险
83	- **D112 结果待定**: 如 RSFT-from-s44 > SFT s44 (0.4734) → Claim 1 robust；否则需 reframe
84	- **8B RSFT evidence quality trade-off**: EDCR 从 0.65-0.67 降到 0.62（RE↑/evidence precision↓），论文需讨论
85	- **1.7B surpasses claim**: 现在更强（1.7B RSFT 0.5122 > 8B SFT mean 0.4866 +2.56pp），但仍需 1.7B multi-seed 确认
86	- **14B 显存**: 2-GPU ZeRO-3 已启动且正常（D108 验证），后续 RSFT 可能需要调参
87	- **EDCR 缺人工验证**: plan_013 取消，用 per-relation 分析 + Limitations 缓解
88	
89	## 关键决策日志
90	
91	| ID | 日期 | 摘要 | 关联实验 |
92	|----|------|------|----------|
93	| D119 | 2026-05-19 | D119: D112 bf16 eval ign_f1=0.5152 确认 Method B (RS | d112_rsft_s44_eval_bf16, d112_rsft_s44_eval |
94	| D118 | 2026-05-19 | D118: "1.7B RSFT surpasses 8B SFT" claim 降级为 "appr | plan019_8b_sft_s43_eval, plan019_1_7b_rsft_s44_r2_eval |
95	| D117 | 2026-05-19 | D117: 14B SFT evidence tax = 0.03pp（本质为零），完成 4 尺度  | plan017_14b_sft_eval_r2, plan017_14b_sft_no_evidence_eval_r2 |
96	| D116 | 2026-05-19 | D116: D112 结果无效（QLoRA confound），必须用 bf16 LoRA 重跑 s | d112_rsft_s44_eval, d112_rsft_s44_train |
97	| D115 | 2026-05-19 | D115: 8B RSFT s44 ign_f1=0.5451 确认 RSFT 跨 seed 稳健， | plan019_8b_rsft_s44_eval, eval_rsft_ced_s42 |
98	| D114 | 2026-05-19 | D114: 1.7B RSFT s43/s44 应使用 Method A（s42 SFT base） | plan019_1_7b_rsft_s43, plan019_1_7b_rsft_s44, d112_rsft_s44_ced_score |
99	| D113 | 2026-05-18 | D113: GRPO bf16 ckpt-100 为最优 checkpoint，ckpt-200 无 | grpo_bf16_g4_ckpt100_eval, grpo_bf16_g4_ckpt200_eval |
100	| D112 | 2026-05-18 | D112: 4B RSFT ign_f1 claim 需重大 reframe——全部 RSFT 基于 | wave1_sft_4b_s43_eval_r2, wave1_sft_4b_s44_eval_r2, eval_rsft_ced_s42 |
101	| D111 | 2026-05-18 | D111: 4B SFT s42 必须用 D076 协议重新 eval，统一三 seed 参考基准 | wave1_sft_4b_s43_eval_r2, wave1_sft_4b_s44_eval_r2 |
102	| D110 | 2026-05-18 | D110: GRPO bf16 ckpt-100 ign_f1=0.4431 无 catastrop | wave1_grpo_bf16_g4, grpo_bf16_g4_ckpt100_eval |
103	
104	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ac6c3eaa-1181-4230-9499-9a3dbe044d7c",
  "uuid": "134ac941-c66c-4519-9b75-864f6d02c64b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/ROADMAP.md",
      "content": "# faith-evidence-ie — Research Dashboard\n\n> 最后更新: 2026-05-19 05:43 UTC | 更新原因: D115 8B RSFT 完成 + D114 1.7B Method A 裁决 + D112 进展 + 14B SFT 启动 + Wave 1 全部完成\n\n## 核心方向\nFREIGE: LLM-based evidence-grounded DocRE 系统性研究。3 贡献：RSFT+NLI 有效性 / Decoupling spectrum / Scale-dependent evidence tax。详见 paper_framing.md。\n\n## 当前进展\n- **阶段**: 🚀 Research + 审稿并行（Round 1 = 3.0 Findings，目标 4.0 Main）\n- **Wave 1**: ✅ 全部完成（SFT s43/s44, GRPO bf16 G=4, Random RSFT）\n- **Scaling seeds (plan_019)**: 8B 2-seed RSFT 完成（D115: s44=0.5451, variance 0.53pp）；1.7B s43/s44 重跑中（D114 Method A）\n- **D112 full pipeline**: Step 3 RSFT 训练中 cuda:0（验证 RSFT 在强 SFT base s44 上的泛化性）\n- **14B SFT (plan_017)**: cuda:1+2 运行中（2-GPU ZeRO-3, D108）\n- **关键数值汇总**:\n\n| Scale | SFT mean (seeds) | RSFT mean (seeds) | Δ ign_f1 | SFT std | RSFT std |\n|-------|-------------------|--------------------|----------|---------|----------|\n| 1.7B | 0.4464 (3) | 0.5122 (1, s42 base) | +6.58pp | 2.79pp | — |\n| 4B | 0.4358 (3) | 0.4482 (3, Method A) | +1.24pp | 3.80pp | 0.51pp |\n| 8B | 0.4866 (2) | 0.5414 (2, Method A) | +5.48pp | 2.62pp | 0.53pp |\n\n- **RSFT 稳定化效应**: 4B variance 3.80→0.51pp (7.5x)，8B variance 2.62→0.53pp (5x)\n- **CED 价值**: CED RSFT (0.4482) > Random RSFT (0.4114) > SFT (0.3974)，+3.68pp gap\n- **GRPO**: bf16 ckpt-100 ign_f1=0.4431 无 catastrophic forgetting（D110），QLoRA 是 confound\n\n## 投稿目标\n- **EMNLP 2026 Main** (ARR July cycle, ~July 15-25, **~57 天**)\n\n## 实验路线（3 层优先级）\n\n### Tier 1 — Main 必要条件\n| 实验 | Plan ID | 状态 |\n|------|---------|------|\n| D102 k=1 方法论修正 | D102 | ✅ 完成 |\n| SFT 4B s43 + s44 + s42 reeval | plan_w3_sft_seeds | ✅ 完成 (D111) |\n| GRPO bf16 G=4 clean control | plan_015 | ✅ 完成 (D110/D113) |\n| Random k=1 RSFT baseline | plan_w18_random | ✅ 完成 (D109) |\n| 8B RSFT s44 seed expansion | plan_019 (8B) | ✅ 完成 (D115) |\n| D112 RSFT from SFT s44 | plan_d112 | 🟡 Step 3 训练中 cuda:0 |\n| 1.7B RSFT s43/s44 重跑 | plan_019 (1.7B) | 🟡 s43_r2 提交中 cuda:3 |\n| 14B SFT (第 4 尺度) | plan_017 | 🟡 训练中 cuda:1+2 |\n\n### Tier 2 — 大幅加分\n| 实验 | Plan ID | 状态 |\n|------|---------|------|\n| 14B RSFT + no-evidence + eval | plan_017 (后续) | pending（等 SFT 完成） |\n| NLI model ablation | plan_010 | pending |\n| Evidence tax 机制分析 | plan_020 | pending |\n| Deep error analysis | plan_021 | pending |\n\n### Tier 3 — 锦上添花\n| 实验 | Plan ID | 状态 |\n|------|---------|------|\n| CDR/GDA 跨领域 | plan_018 | P2（无 evidence 标注） |\n| 第三模型家族 | plan_022 | pending |\n| DocKS-RAG/LMRC 复现 | plan_023 | pending |\n\n## 从 3.0 → 4.0 路径\n| 里程碑 | 预期评分 | 状态 |\n|--------|---------|------|\n| Wave 1 完成 + D112 | 3.0 → 3.5 | 🟡 D112 step 3 训练中 |\n| + 1.7B/8B multi-seed 统计力 | 3.5 | 🟡 8B done, 1.7B 重跑中 |\n| + 14B 第 4 尺度档 | 3.5 → 3.75 | 🟡 SFT 训练中 |\n| + Mechanistic + error analysis | 3.75 → 4.0 | pending |\n\n## GPU 预算\n- 本项目：rtx5090-4x cuda:0-3（4 张 RTX 5090）\n- 当前：4/4 在用（D112 step3 / 14B SFT×2 / 1.7B RSFT）\n- 剩余估算：Tier 1 ~15h + Tier 2 ~65h + Tier 3 ~100h\n\n## 近期任务\n- [x] Wave 1 全部完成（SFT seeds, GRPO bf16, Random RSFT）\n- [x] 8B RSFT s44 eval (D115: 0.5451, variance 压缩 5x)\n- [x] 4B SFT s42 D076 reeval (D111: 0.3974)\n- [ ] D112 step 3 → step 4 eval（cuda:0, ~1.5h total）\n- [ ] 1.7B RSFT s43_r2 + s44_r2 + eval（cuda:3, ~2-3h total）\n- [ ] 14B SFT 完成 → 14B RSFT + no-evidence + eval（cuda:1+2, ~8h SFT + 后续）\n- [ ] experiment_plan.yaml 全面同步 registry\n- [ ] paper_framing.md 更新（D112 结果 + 8B 2-seed + variance 压缩 narrative）\n- [ ] 重新提交论文审稿\n\n## 关键风险\n- **D112 结果待定**: 如 RSFT-from-s44 > SFT s44 (0.4734) → Claim 1 robust；否则需 reframe\n- **8B RSFT evidence quality trade-off**: EDCR 从 0.65-0.67 降到 0.62（RE↑/evidence precision↓），论文需讨论\n- **1.7B surpasses claim**: 现在更强（1.7B RSFT 0.5122 > 8B SFT mean 0.4866 +2.56pp），但仍需 1.7B multi-seed 确认\n- **14B 显存**: 2-GPU ZeRO-3 已启动且正常（D108 验证），后续 RSFT 可能需要调参\n- **EDCR 缺人工验证**: plan_013 取消，用 per-relation 分析 + Limitations 缓解\n\n## 关键决策日志\n\n| ID | 日期 | 摘要 | 关联实验 |\n|----|------|------|----------|\n| D119 | 2026-05-19 | D119: D112 bf16 eval ign_f1=0.5152 确认 Method B (RS | d112_rsft_s44_eval_bf16, d112_rsft_s44_eval |\n| D118 | 2026-05-19 | D118: \"1.7B RSFT surpasses 8B SFT\" claim 降级为 \"appr | plan019_8b_sft_s43_eval, plan019_1_7b_rsft_s44_r2_eval |\n| D117 | 2026-05-19 | D117: 14B SFT evidence tax = 0.03pp（本质为零），完成 4 尺度  | plan017_14b_sft_eval_r2, plan017_14b_sft_no_evidence_eval_r2 |\n| D116 | 2026-05-19 | D116: D112 结果无效（QLoRA confound），必须用 bf16 LoRA 重跑 s | d112_rsft_s44_eval, d112_rsft_s44_train |\n| D115 | 2026-05-19 | D115: 8B RSFT s44 ign_f1=0.5451 确认 RSFT 跨 seed 稳健， | plan019_8b_rsft_s44_eval, eval_rsft_ced_s42 |\n| D114 | 2026-05-19 | D114: 1.7B RSFT s43/s44 应使用 Method A（s42 SFT base） | plan019_1_7b_rsft_s43, plan019_1_7b_rsft_s44, d112_rsft_s44_ced_score |\n| D113 | 2026-05-18 | D113: GRPO bf16 ckpt-100 为最优 checkpoint，ckpt-200 无 | grpo_bf16_g4_ckpt100_eval, grpo_bf16_g4_ckpt200_eval |\n| D112 | 2026-05-18 | D112: 4B RSFT ign_f1 claim 需重大 reframe——全部 RSFT 基于 | wave1_sft_4b_s43_eval_r2, wave1_sft_4b_s44_eval_r2, eval_rsft_ced_s42 |\n| D111 | 2026-05-18 | D111: 4B SFT s42 必须用 D076 协议重新 eval，统一三 seed 参考基准 | wave1_sft_4b_s43_eval_r2, wave1_sft_4b_s44_eval_r2 |\n| D110 | 2026-05-18 | D110: GRPO bf16 ckpt-100 ign_f1=0.4431 无 catastrop | wave1_grpo_bf16_g4, grpo_bf16_g4_ckpt100_eval |\n\n",
      "numLines": 104,
      "startLine": 1,
      "totalLines": 104
    }
  }
}
```

</details>

---

### Assistant

_source line 29_

<details><summary>Logged reasoning block</summary>

```text
Now I see the file has D119 in the decision log (line 93) which wasn't in the MCP read. The file on disk is slightly newer. Let me write the updated version now.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ac6c3eaa-1181-4230-9499-9a3dbe044d7c",
  "uuid": "7544bde3-3fb1-4fe7-9a43-053a78eb69b8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kit44nohpVUTBXTmGRfNXE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3488,
      "cache_read_input_tokens": 35785,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3488
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

_source line 30_

文件已读取（注意磁盘版本比 MCP 读取多了 D119）。现在写入更新。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ac6c3eaa-1181-4230-9499-9a3dbe044d7c",
  "uuid": "bde9b17c-1ea8-4dbd-b471-b8d029f6883d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kit44nohpVUTBXTmGRfNXE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3488,
      "cache_read_input_tokens": 35785,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3488
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

_source line 31_

<details open><summary>🔧 Tool call — Write · `toolu_016XsXRoWYUV1qMJZrNcx6zL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/ROADMAP.md",
  "content": "# faith-evidence-ie — Research Dashboard\n\n> 最后更新: 2026-05-19 09:30 UTC | 更新原因: D117 14B evidence tax=0 + D118 1.7B claim 降级 + D112 bf16 完成 (0.5152) + 8B SFT 3-seed (0.5019) + scaling table 4行\n\n## 核心方向\nFREIGE: LLM-based evidence-grounded DocRE 系统性研究。3 贡献：RSFT+NLI 有效性 / Decoupling spectrum / Scale-dependent evidence tax。详见 paper_framing.md。\n\n## 当前进展\n- **阶段**: 🚀 Research + 审稿并行（Round 1 = 3.0 Findings，目标 4.0 Main）\n- **Wave 1**: ✅ 全部完成（SFT seeds, GRPO bf16, Random RSFT）\n- **Scaling seeds (plan_019)**: 8B 3-seed SFT 完成（mean=0.5019±3.72pp）；8B 2-seed RSFT 完成（D115: s44=0.5451, variance 0.53pp）\n- **D112 full pipeline**: ✅ 完成（bf16 LoRA RSFT from SFT s44: ign_f1=0.5152, +4.18pp over SFT s44 baseline 0.4734）\n- **14B SFT (plan_017)**: ✅ 完成（D117: with-evidence 0.5507, no-evidence 0.551, evidence tax=0.03pp≈0）\n- **D118 claim 降级**: 1.7B RSFT (0.5122) vs 8B SFT mean (0.5019) Δ=+1.03pp, p≈0.34 不显著，降级为 \"comparable / on par with\"\n- **关键数值汇总**:\n\n| Scale | SFT mean (seeds) | RSFT mean (seeds) | Δ ign_f1 | SFT std | RSFT std |\n|-------|-------------------|--------------------|----------|---------|----------|\n| 1.7B | 0.4464 (3) | 0.5122 (1, s42 base) | +6.58pp | 2.79pp | — |\n| 4B | 0.4358 (3) | 0.4482 (3, Method A) / 0.5152 (1, Method B) | +1.24pp / +4.18pp (vs s44) | 3.80pp | 0.51pp |\n| 8B | 0.5019 (3) | 0.5414 (2, Method A) | +3.95pp | 3.72pp | 0.53pp |\n| 14B | 0.5507 (1) | pending | — | — | — |\n\n- **14B evidence tax**: 0.03pp（本质为零），14B 容量足够同时输出 evidence 和 RE\n- **RSFT variance 稳定化**: 8B SFT std=3.72pp → RSFT std=0.53pp (7x)；4B SFT std=3.80pp → RSFT std=0.51pp (7.5x)\n- **CED 价值**: CED RSFT (0.4482) > Random RSFT (0.4114) > SFT (0.3974)，+3.68pp gap\n- **GRPO**: bf16 ckpt-100 ign_f1=0.4431 无 catastrophic forgetting（D110），QLoRA 是 confound\n\n## 投稿目标\n- **EMNLP 2026 Main** (ARR July cycle, ~July 15-25, **~57 天**)\n\n## 实验路线（3 层优先级）\n\n### Tier 1 — Main 必要条件\n| 实验 | Plan ID | 状态 |\n|------|---------|------|\n| D102 k=1 方法论修正 | D102 | ✅ 完成 |\n| SFT 4B s43 + s44 + s42 reeval | plan_w3_sft_seeds | ✅ 完成 (D111) |\n| GRPO bf16 G=4 clean control | plan_015 | ✅ 完成 (D110/D113) |\n| Random k=1 RSFT baseline | plan_w18_random | ✅ 完成 (D109) |\n| 8B RSFT s44 seed expansion | plan_019 (8B) | ✅ 完成 (D115) |\n| 8B SFT s43 eval | plan_019 | ✅ 完成 (ign_f1=0.5324) |\n| D112 RSFT from SFT s44 (bf16) | plan_d112 | ✅ 完成 (D119: ign_f1=0.5152) |\n| 14B SFT (第 4 尺度) | plan_017 | ✅ 完成 (D117: 0.5507, tax=0.03pp) |\n| 1.7B RSFT s43/s44 重跑 | plan_019 (1.7B) | 🟡 进行中 |\n\n### Tier 2 — 大幅加分\n| 实验 | Plan ID | 状态 |\n|------|---------|------|\n| 14B RSFT + no-evidence + eval | plan_017 (后续) | pending（待启动） |\n| 8B RSFT s43 补齐第 3 seed | plan_019 | pending |\n| NLI model ablation | plan_010 | pending |\n| Evidence tax 机制分析 | plan_020 | pending |\n| Deep error analysis | plan_021 | pending |\n\n### Tier 3 — 锦上添花\n| 实验 | Plan ID | 状态 |\n|------|---------|------|\n| CDR/GDA 跨领域 | plan_018 | P2（无 evidence 标注） |\n| 第三模型家族 | plan_022 | pending |\n| DocKS-RAG/LMRC 复现 | plan_023 | pending |\n\n## 从 3.0 → 4.0 路径\n| 里程碑 | 预期评分 | 状态 |\n|--------|---------|------|\n| Wave 1 完成 + D112 | 3.0 → 3.5 | ✅ D112 完成 (0.5152, +4.18pp) |\n| + 1.7B/8B multi-seed 统计力 | 3.5 | 🟡 8B 3-seed done, 1.7B 进行中 |\n| + 14B 第 4 尺度档 | 3.5 → 3.75 | ✅ SFT 完成 (0.5507), RSFT pending |\n| + Mechanistic + error analysis | 3.75 → 4.0 | pending |\n\n## GPU 分布\n- cuda:0: 8B RSFT no-evidence eval r2（接近完成）\n- cuda:1: D112 no-evidence eval r3（44%）\n- cuda:2: 空闲\n- cuda:3: 1.7B no-evidence eval 2048（38%）\n\n## 近期任务\n- [x] Wave 1 全部完成（SFT seeds, GRPO bf16, Random RSFT）\n- [x] 8B RSFT s44 eval (D115: 0.5451, variance 压缩 5x)\n- [x] 4B SFT s42 D076 reeval (D111: 0.3974)\n- [x] D112 step 4 eval 完成 (bf16 LoRA: ign_f1=0.5152, +4.18pp)\n- [x] 8B SFT s43 eval 完成 (ign_f1=0.5324)\n- [x] 14B SFT eval 完成 (D117: ign_f1=0.5507, evidence tax=0.03pp)\n- [ ] 1.7B no-evidence eval 2048 重跑（排除截断，cuda:3）\n- [ ] 8B RSFT no-evidence eval（cuda:0，接近完成）\n- [ ] D112 no-evidence eval r3（cuda:1，44%）\n- [ ] 14B RSFT pipeline（待启动）\n- [ ] 8B RSFT s43 补齐第 3 seed\n- [ ] experiment_plan.yaml 全面同步 registry\n- [ ] paper_framing.md 更新（D112 + D117 + D118 narrative 调整）\n- [ ] 重新提交论文审稿\n\n## 关键风险\n- **D112 结果**: ✅ 已确认 RSFT-from-s44 (0.5152) > SFT s44 (0.4734) +4.18pp，Claim 1 robust\n- **1.7B claim 已降级 (D118)**: 1.7B RSFT vs 8B SFT Δ=+1.03pp, p≈0.34 不显著，改为 \"comparable\"；RSFT variance stabilization (SFT std=3.72pp vs RSFT std=0.53pp) 作为独立发现\n- **14B evidence tax = 0 (D117)**: 积极结果，14B 容量足够，Claim 3 需调整为 \"tax scales inversely with model capacity\"\n- **8B RSFT evidence quality trade-off**: EDCR 从 0.65-0.67 降到 0.62（RE↑/evidence precision↓），论文需讨论\n- **14B RSFT 待启动**: SFT 已完成，RSFT pipeline 是 Tier 2 首要任务\n- **EDCR 缺人工验证**: plan_013 取消，用 per-relation 分析 + Limitations 缓解\n\n## 关键决策日志\n\n| ID | 日期 | 摘要 | 关联实验 |\n|----|------|------|----------|\n| D119 | 2026-05-19 | D119: D112 bf16 eval ign_f1=0.5152 确认 Method B (RS | d112_rsft_s44_eval_bf16, d112_rsft_s44_eval |\n| D118 | 2026-05-19 | D118: \"1.7B RSFT surpasses 8B SFT\" claim 降级为 \"appr | plan019_8b_sft_s43_eval, plan019_1_7b_rsft_s44_r2_eval |\n| D117 | 2026-05-19 | D117: 14B SFT evidence tax = 0.03pp（本质为零），完成 4 尺度  | plan017_14b_sft_eval_r2, plan017_14b_sft_no_evidence_eval_r2 |\n| D116 | 2026-05-19 | D116: D112 结果无效（QLoRA confound），必须用 bf16 LoRA 重跑 s | d112_rsft_s44_eval, d112_rsft_s44_train |\n| D115 | 2026-05-19 | D115: 8B RSFT s44 ign_f1=0.5451 确认 RSFT 跨 seed 稳健， | plan019_8b_rsft_s44_eval, eval_rsft_ced_s42 |\n| D114 | 2026-05-19 | D114: 1.7B RSFT s43/s44 应使用 Method A（s42 SFT base） | plan019_1_7b_rsft_s43, plan019_1_7b_rsft_s44, d112_rsft_s44_ced_score |\n| D113 | 2026-05-18 | D113: GRPO bf16 ckpt-100 为最优 checkpoint，ckpt-200 无 | grpo_bf16_g4_ckpt100_eval, grpo_bf16_g4_ckpt200_eval |\n| D112 | 2026-05-18 | D112: 4B RSFT ign_f1 claim 需重大 reframe——全部 RSFT 基于 | wave1_sft_4b_s43_eval_r2, wave1_sft_4b_s44_eval_r2, eval_rsft_ced_s42 |\n| D111 | 2026-05-18 | D111: 4B SFT s42 必须用 D076 协议重新 eval，统一三 seed 参考基准 | wave1_sft_4b_s43_eval_r2, wave1_sft_4b_s44_eval_r2 |\n| D110 | 2026-05-18 | D110: GRPO bf16 ckpt-100 ign_f1=0.4431 无 catastrop | wave1_grpo_bf16_g4, grpo_bf16_g4_ckpt100_eval |\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ac6c3eaa-1181-4230-9499-9a3dbe044d7c",
  "uuid": "14888c4b-6d20-44c3-af3f-53203bd54463",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kit44nohpVUTBXTmGRfNXE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3488,
      "cache_read_input_tokens": 35785,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3488
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

_source line 32 · 2026-05-19T17:15:24.978Z_

<details><summary>↩ Tool result · `toolu_016XsXRoWYUV1qMJZrNcx6zL`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/ROADMAP.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ac6c3eaa-1181-4230-9499-9a3dbe044d7c",
  "uuid": "51c0e811-e431-4ea1-9a88-2fec8982911b",
  "tool_use_result": {
    "type": "update",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/ROADMAP.md",
    "content": "# faith-evidence-ie — Research Dashboard\n\n> 最后更新: 2026-05-19 09:30 UTC | 更新原因: D117 14B evidence tax=0 + D118 1.7B claim 降级 + D112 bf16 完成 (0.5152) + 8B SFT 3-seed (0.5019) + scaling table 4行\n\n## 核心方向\nFREIGE: LLM-based evidence-grounded DocRE 系统性研究。3 贡献：RSFT+NLI 有效性 / Decoupling spectrum / Scale-dependent evidence tax。详见 paper_framing.md。\n\n## 当前进展\n- **阶段**: 🚀 Research + 审稿并行（Round 1 = 3.0 Findings，目标 4.0 Main）\n- **Wave 1**: ✅ 全部完成（SFT seeds, GRPO bf16, Random RSFT）\n- **Scaling seeds (plan_019)**: 8B 3-seed SFT 完成（mean=0.5019±3.72pp）；8B 2-seed RSFT 完成（D115: s44=0.5451, variance 0.53pp）\n- **D112 full pipeline**: ✅ 完成（bf16 LoRA RSFT from SFT s44: ign_f1=0.5152, +4.18pp over SFT s44 baseline 0.4734）\n- **14B SFT (plan_017)**: ✅ 完成（D117: with-evidence 0.5507, no-evidence 0.551, evidence tax=0.03pp≈0）\n- **D118 claim 降级**: 1.7B RSFT (0.5122) vs 8B SFT mean (0.5019) Δ=+1.03pp, p≈0.34 不显著，降级为 \"comparable / on par with\"\n- **关键数值汇总**:\n\n| Scale | SFT mean (seeds) | RSFT mean (seeds) | Δ ign_f1 | SFT std | RSFT std |\n|-------|-------------------|--------------------|----------|---------|----------|\n| 1.7B | 0.4464 (3) | 0.5122 (1, s42 base) | +6.58pp | 2.79pp | — |\n| 4B | 0.4358 (3) | 0.4482 (3, Method A) / 0.5152 (1, Method B) | +1.24pp / +4.18pp (vs s44) | 3.80pp | 0.51pp |\n| 8B | 0.5019 (3) | 0.5414 (2, Method A) | +3.95pp | 3.72pp | 0.53pp |\n| 14B | 0.5507 (1) | pending | — | — | — |\n\n- **14B evidence tax**: 0.03pp（本质为零），14B 容量足够同时输出 evidence 和 RE\n- **RSFT variance 稳定化**: 8B SFT std=3.72pp → RSFT std=0.53pp (7x)；4B SFT std=3.80pp → RSFT std=0.51pp (7.5x)\n- **CED 价值**: CED RSFT (0.4482) > Random RSFT (0.4114) > SFT (0.3974)，+3.68pp gap\n- **GRPO**: bf16 ckpt-100 ign_f1=0.4431 无 catastrophic forgetting（D110），QLoRA 是 confound\n\n## 投稿目标\n- **EMNLP 2026 Main** (ARR July cycle, ~July 15-25, **~57 天**)\n\n## 实验路线（3 层优先级）\n\n### Tier 1 — Main 必要条件\n| 实验 | Plan ID | 状态 |\n|------|---------|------|\n| D102 k=1 方法论修正 | D102 | ✅ 完成 |\n| SFT 4B s43 + s44 + s42 reeval | plan_w3_sft_seeds | ✅ 完成 (D111) |\n| GRPO bf16 G=4 clean control | plan_015 | ✅ 完成 (D110/D113) |\n| Random k=1 RSFT baseline | plan_w18_random | ✅ 完成 (D109) |\n| 8B RSFT s44 seed expansion | plan_019 (8B) | ✅ 完成 (D115) |\n| 8B SFT s43 eval | plan_019 | ✅ 完成 (ign_f1=0.5324) |\n| D112 RSFT from SFT s44 (bf16) | plan_d112 | ✅ 完成 (D119: ign_f1=0.5152) |\n| 14B SFT (第 4 尺度) | plan_017 | ✅ 完成 (D117: 0.5507, tax=0.03pp) |\n| 1.7B RSFT s43/s44 重跑 | plan_019 (1.7B) | 🟡 进行中 |\n\n### Tier 2 — 大幅加分\n| 实验 | Plan ID | 状态 |\n|------|---------|------|\n| 14B RSFT + no-evidence + eval | plan_017 (后续) | pending（待启动） |\n| 8B RSFT s43 补齐第 3 seed | plan_019 | pending |\n| NLI model ablation | plan_010 | pending |\n| Evidence tax 机制分析 | plan_020 | pending |\n| Deep error analysis | plan_021 | pending |\n\n### Tier 3 — 锦上添花\n| 实验 | Plan ID | 状态 |\n|------|---------|------|\n| CDR/GDA 跨领域 | plan_018 | P2（无 evidence 标注） |\n| 第三模型家族 | plan_022 | pending |\n| DocKS-RAG/LMRC 复现 | plan_023 | pending |\n\n## 从 3.0 → 4.0 路径\n| 里程碑 | 预期评分 | 状态 |\n|--------|---------|------|\n| Wave 1 完成 + D112 | 3.0 → 3.5 | ✅ D112 完成 (0.5152, +4.18pp) |\n| + 1.7B/8B multi-seed 统计力 | 3.5 | 🟡 8B 3-seed done, 1.7B 进行中 |\n| + 14B 第 4 尺度档 | 3.5 → 3.75 | ✅ SFT 完成 (0.5507), RSFT pending |\n| + Mechanistic + error analysis | 3.75 → 4.0 | pending |\n\n## GPU 分布\n- cuda:0: 8B RSFT no-evidence eval r2（接近完成）\n- cuda:1: D112 no-evidence eval r3（44%）\n- cuda:2: 空闲\n- cuda:3: 1.7B no-evidence eval 2048（38%）\n\n## 近期任务\n- [x] Wave 1 全部完成（SFT seeds, GRPO bf16, Random RSFT）\n- [x] 8B RSFT s44 eval (D115: 0.5451, variance 压缩 5x)\n- [x] 4B SFT s42 D076 reeval (D111: 0.3974)\n- [x] D112 step 4 eval 完成 (bf16 LoRA: ign_f1=0.5152, +4.18pp)\n- [x] 8B SFT s43 eval 完成 (ign_f1=0.5324)\n- [x] 14B SFT eval 完成 (D117: ign_f1=0.5507, evidence tax=0.03pp)\n- [ ] 1.7B no-evidence eval 2048 重跑（排除截断，cuda:3）\n- [ ] 8B RSFT no-evidence eval（cuda:0，接近完成）\n- [ ] D112 no-evidence eval r3（cuda:1，44%）\n- [ ] 14B RSFT pipeline（待启动）\n- [ ] 8B RSFT s43 补齐第 3 seed\n- [ ] experiment_plan.yaml 全面同步 registry\n- [ ] paper_framing.md 更新（D112 + D117 + D118 narrative 调整）\n- [ ] 重新提交论文审稿\n\n## 关键风险\n- **D112 结果**: ✅ 已确认 RSFT-from-s44 (0.5152) > SFT s44 (0.4734) +4.18pp，Claim 1 robust\n- **1.7B claim 已降级 (D118)**: 1.7B RSFT vs 8B SFT Δ=+1.03pp, p≈0.34 不显著，改为 \"comparable\"；RSFT variance stabilization (SFT std=3.72pp vs RSFT std=0.53pp) 作为独立发现\n- **14B evidence tax = 0 (D117)**: 积极结果，14B 容量足够，Claim 3 需调整为 \"tax scales inversely with model capacity\"\n- **8B RSFT evidence quality trade-off**: EDCR 从 0.65-0.67 降到 0.62（RE↑/evidence precision↓），论文需讨论\n- **14B RSFT 待启动**: SFT 已完成，RSFT pipeline 是 Tier 2 首要任务\n- **EDCR 缺人工验证**: plan_013 取消，用 per-relation 分析 + Limitations 缓解\n\n## 关键决策日志\n\n| ID | 日期 | 摘要 | 关联实验 |\n|----|------|------|----------|\n| D119 | 2026-05-19 | D119: D112 bf16 eval ign_f1=0.5152 确认 Method B (RS | d112_rsft_s44_eval_bf16, d112_rsft_s44_eval |\n| D118 | 2026-05-19 | D118: \"1.7B RSFT surpasses 8B SFT\" claim 降级为 \"appr | plan019_8b_sft_s43_eval, plan019_1_7b_rsft_s44_r2_eval |\n| D117 | 2026-05-19 | D117: 14B SFT evidence tax = 0.03pp（本质为零），完成 4 尺度  | plan017_14b_sft_eval_r2, plan017_14b_sft_no_evidence_eval_r2 |\n| D116 | 2026-05-19 | D116: D112 结果无效（QLoRA confound），必须用 bf16 LoRA 重跑 s | d112_rsft_s44_eval, d112_rsft_s44_train |\n| D115 | 2026-05-19 | D115: 8B RSFT s44 ign_f1=0.5451 确认 RSFT 跨 seed 稳健， | plan019_8b_rsft_s44_eval, eval_rsft_ced_s42 |\n| D114 | 2026-05-19 | D114: 1.7B RSFT s43/s44 应使用 Method A（s42 SFT base） | plan019_1_7b_rsft_s43, plan019_1_7b_rsft_s44, d112_rsft_s44_ced_score |\n| D113 | 2026-05-18 | D113: GRPO bf16 ckpt-100 为最优 checkpoint，ckpt-200 无 | grpo_bf16_g4_ckpt100_eval, grpo_bf16_g4_ckpt200_eval |\n| D112 | 2026-05-18 | D112: 4B RSFT ign_f1 claim 需重大 reframe——全部 RSFT 基于 | wave1_sft_4b_s43_eval_r2, wave1_sft_4b_s44_eval_r2, eval_rsft_ced_s42 |\n| D111 | 2026-05-18 | D111: 4B SFT s42 必须用 D076 协议重新 eval，统一三 seed 参考基准 | wave1_sft_4b_s43_eval_r2, wave1_sft_4b_s44_eval_r2 |\n| D110 | 2026-05-18 | D110: GRPO bf16 ckpt-100 ign_f1=0.4431 无 catastrop | wave1_grpo_bf16_g4, grpo_bf16_g4_ckpt100_eval |\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 25,
        "newStart": 1,
        "newLines": 28,
        "lines": [
          " # faith-evidence-ie — Research Dashboard",
          " ",
          "-> 最后更新: 2026-05-19 05:43 UTC | 更新原因: D115 8B RSFT 完成 + D114 1.7B Method A 裁决 + D112 进展 + 14B SFT 启动 + Wave 1 全部完成",
          "+> 最后更新: 2026-05-19 09:30 UTC | 更新原因: D117 14B evidence tax=0 + D118 1.7B claim 降级 + D112 bf16 完成 (0.5152) + 8B SFT 3-seed (0.5019) + scaling table 4行",
          " ",
          " ## 核心方向",
          " FREIGE: LLM-based evidence-grounded DocRE 系统性研究。3 贡献：RSFT+NLI 有效性 / Decoupling spectrum / Scale-dependent evidence tax。详见 paper_framing.md。",
          " ",
          " ## 当前进展",
          " - **阶段**: 🚀 Research + 审稿并行（Round 1 = 3.0 Findings，目标 4.0 Main）",
          "-- **Wave 1**: ✅ 全部完成（SFT s43/s44, GRPO bf16 G=4, Random RSFT）",
          "-- **Scaling seeds (plan_019)**: 8B 2-seed RSFT 完成（D115: s44=0.5451, variance 0.53pp）；1.7B s43/s44 重跑中（D114 Method A）",
          "-- **D112 full pipeline**: Step 3 RSFT 训练中 cuda:0（验证 RSFT 在强 SFT base s44 上的泛化性）",
          "-- **14B SFT (plan_017)**: cuda:1+2 运行中（2-GPU ZeRO-3, D108）",
          "+- **Wave 1**: ✅ 全部完成（SFT seeds, GRPO bf16, Random RSFT）",
          "+- **Scaling seeds (plan_019)**: 8B 3-seed SFT 完成（mean=0.5019±3.72pp）；8B 2-seed RSFT 完成（D115: s44=0.5451, variance 0.53pp）",
          "+- **D112 full pipeline**: ✅ 完成（bf16 LoRA RSFT from SFT s44: ign_f1=0.5152, +4.18pp over SFT s44 baseline 0.4734）",
          "+- **14B SFT (plan_017)**: ✅ 完成（D117: with-evidence 0.5507, no-evidence 0.551, evidence tax=0.03pp≈0）",
          "+- **D118 claim 降级**: 1.7B RSFT (0.5122) vs 8B SFT mean (0.5019) Δ=+1.03pp, p≈0.34 不显著，降级为 \"comparable / on par with\"",
          " - **关键数值汇总**:",
          " ",
          " | Scale | SFT mean (seeds) | RSFT mean (seeds) | Δ ign_f1 | SFT std | RSFT std |",
          " |-------|-------------------|--------------------|----------|---------|----------|",
          " | 1.7B | 0.4464 (3) | 0.5122 (1, s42 base) | +6.58pp | 2.79pp | — |",
          "-| 4B | 0.4358 (3) | 0.4482 (3, Method A) | +1.24pp | 3.80pp | 0.51pp |",
          "-| 8B | 0.4866 (2) | 0.5414 (2, Method A) | +5.48pp | 2.62pp | 0.53pp |",
          "+| 4B | 0.4358 (3) | 0.4482 (3, Method A) / 0.5152 (1, Method B) | +1.24pp / +4.18pp (vs s44) | 3.80pp | 0.51pp |",
          "+| 8B | 0.5019 (3) | 0.5414 (2, Method A) | +3.95pp | 3.72pp | 0.53pp |",
          "+| 14B | 0.5507 (1) | pending | — | — | — |",
          " ",
          "-- **RSFT 稳定化效应**: 4B variance 3.80→0.51pp (7.5x)，8B variance 2.62→0.53pp (5x)",
          "+- **14B evidence tax**: 0.03pp（本质为零），14B 容量足够同时输出 evidence 和 RE",
          "+- **RSFT variance 稳定化**: 8B SFT std=3.72pp → RSFT std=0.53pp (7x)；4B SFT std=3.80pp → RSFT std=0.51pp (7.5x)",
          " - **CED 价值**: CED RSFT (0.4482) > Random RSFT (0.4114) > SFT (0.3974)，+3.68pp gap",
          " - **GRPO**: bf16 ckpt-100 ign_f1=0.4431 无 catastrophic forgetting（D110），QLoRA 是 confound",
          " "
        ]
      },
      {
        "oldStart": 36,
        "oldLines": 14,
        "newStart": 39,
        "newLines": 16,
        "lines": [
          " | GRPO bf16 G=4 clean control | plan_015 | ✅ 完成 (D110/D113) |",
          " | Random k=1 RSFT baseline | plan_w18_random | ✅ 完成 (D109) |",
          " | 8B RSFT s44 seed expansion | plan_019 (8B) | ✅ 完成 (D115) |",
          "-| D112 RSFT from SFT s44 | plan_d112 | 🟡 Step 3 训练中 cuda:0 |",
          "-| 1.7B RSFT s43/s44 重跑 | plan_019 (1.7B) | 🟡 s43_r2 提交中 cuda:3 |",
          "-| 14B SFT (第 4 尺度) | plan_017 | 🟡 训练中 cuda:1+2 |",
          "+| 8B SFT s43 eval | plan_019 | ✅ 完成 (ign_f1=0.5324) |",
          "+| D112 RSFT from SFT s44 (bf16) | plan_d112 | ✅ 完成 (D119: ign_f1=0.5152) |",
          "+| 14B SFT (第 4 尺度) | plan_017 | ✅ 完成 (D117: 0.5507, tax=0.03pp) |",
          "+| 1.7B RSFT s43/s44 重跑 | plan_019 (1.7B) | 🟡 进行中 |",
          " ",
          " ### Tier 2 — 大幅加分",
          " | 实验 | Plan ID | 状态 |",
          " |------|---------|------|",
          "-| 14B RSFT + no-evidence + eval | plan_017 (后续) | pending（等 SFT 完成） |",
          "+| 14B RSFT + no-evidence + eval | plan_017 (后续) | pending（待启动） |",
          "+| 8B RSFT s43 补齐第 3 seed | plan_019 | pending |",
          " | NLI model ablation | plan_010 | pending |",
          " | Evidence tax 机制分析 | plan_020 | pending |",
          " | Deep error analysis | plan_021 | pending |"
        ]
      },
      {
        "oldStart": 58,
        "oldLines": 32,
        "newStart": 63,
        "newLines": 39,
        "lines": [
          " ## 从 3.0 → 4.0 路径",
          " | 里程碑 | 预期评分 | 状态 |",
          " |--------|---------|------|",
          "-| Wave 1 完成 + D112 | 3.0 → 3.5 | 🟡 D112 step 3 训练中 |",
          "-| + 1.7B/8B multi-seed 统计力 | 3.5 | 🟡 8B done, 1.7B 重跑中 |",
          "-| + 14B 第 4 尺度档 | 3.5 → 3.75 | 🟡 SFT 训练中 |",
          "+| Wave 1 完成 + D112 | 3.0 → 3.5 | ✅ D112 完成 (0.5152, +4.18pp) |",
          "+| + 1.7B/8B multi-seed 统计力 | 3.5 | 🟡 8B 3-seed done, 1.7B 进行中 |",
          "+| + 14B 第 4 尺度档 | 3.5 → 3.75 | ✅ SFT 完成 (0.5507), RSFT pending |",
          " | + Mechanistic + error analysis | 3.75 → 4.0 | pending |",
          " ",
          "-## GPU 预算",
          "-- 本项目：rtx5090-4x cuda:0-3（4 张 RTX 5090）",
          "-- 当前：4/4 在用（D112 step3 / 14B SFT×2 / 1.7B RSFT）",
          "-- 剩余估算：Tier 1 ~15h + Tier 2 ~65h + Tier 3 ~100h",
          "+## GPU 分布",
          "+- cuda:0: 8B RSFT no-evidence eval r2（接近完成）",
          "+- cuda:1: D112 no-evidence eval r3（44%）",
          "+- cuda:2: 空闲",
          "+- cuda:3: 1.7B no-evidence eval 2048（38%）",
          " ",
          " ## 近期任务",
          " - [x] Wave 1 全部完成（SFT seeds, GRPO bf16, Random RSFT）",
          " - [x] 8B RSFT s44 eval (D115: 0.5451, variance 压缩 5x)",
          " - [x] 4B SFT s42 D076 reeval (D111: 0.3974)",
          "-- [ ] D112 step 3 → step 4 eval（cuda:0, ~1.5h total）",
          "-- [ ] 1.7B RSFT s43_r2 + s44_r2 + eval（cuda:3, ~2-3h total）",
          "-- [ ] 14B SFT 完成 → 14B RSFT + no-evidence + eval（cuda:1+2, ~8h SFT + 后续）",
          "+- [x] D112 step 4 eval 完成 (bf16 LoRA: ign_f1=0.5152, +4.18pp)",
          "+- [x] 8B SFT s43 eval 完成 (ign_f1=0.5324)",
          "+- [x] 14B SFT eval 完成 (D117: ign_f1=0.5507, evidence tax=0.03pp)",
          "+- [ ] 1.7B no-evidence eval 2048 重跑（排除截断，cuda:3）",
          "+- [ ] 8B RSFT no-evidence eval（cuda:0，接近完成）",
          "+- [ ] D112 no-evidence eval r3（cuda:1，44%）",
          "+- [ ] 14B RSFT pipeline（待启动）",
          "+- [ ] 8B RSFT s43 补齐第 3 seed",
          " - [ ] experiment_plan.yaml 全面同步 registry",
          "-- [ ] paper_framing.md 更新（D112 结果 + 8B 2-seed + variance 压缩 narrative）",
          "+- [ ] paper_framing.md 更新（D112 + D117 + D118 narrative 调整）",
          " - [ ] 重新提交论文审稿",
          " ",
          " ## 关键风险",
          "-- **D112 结果待定**: 如 RSFT-from-s44 > SFT s44 (0.4734) → Claim 1 robust；否则需 reframe",
          "+- **D112 结果**: ✅ 已确认 RSFT-from-s44 (0.5152) > SFT s44 (0.4734) +4.18pp，Claim 1 robust",
          "+- **1.7B claim 已降级 (D118)**: 1.7B RSFT vs 8B SFT Δ=+1.03pp, p≈0.34 不显著，改为 \"comparable\"；RSFT variance stabilization (SFT std=3.72pp vs RSFT std=0.53pp) 作为独立发现",
          "+- **14B evidence tax = 0 (D117)**: 积极结果，14B 容量足够，Claim 3 需调整为 \"tax scales inversely with model capacity\"",
          " - **8B RSFT evidence quality trade-off**: EDCR 从 0.65-0.67 降到 0.62（RE↑/evidence precision↓），论文需讨论",
          "-- **1.7B surpasses claim**: 现在更强（1.7B RSFT 0.5122 > 8B SFT mean 0.4866 +2.56pp），但仍需 1.7B multi-seed 确认",
          "-- **14B 显存**: 2-GPU ZeRO-3 已启动且正常（D108 验证），后续 RSFT 可能需要调参",
          "+- **14B RSFT 待启动**: SFT 已完成，RSFT pipeline 是 Tier 2 首要任务",
          " - **EDCR 缺人工验证**: plan_013 取消，用 per-relation 分析 + Limitations 缓解",
          " ",
          " ## 关键决策日志"
        ]
      },
      {
        "oldStart": 100,
        "oldLines": 4,
        "newStart": 112,
        "newLines": 3,
        "lines": [
          " | D112 | 2026-05-18 | D112: 4B RSFT ign_f1 claim 需重大 reframe——全部 RSFT 基于 | wave1_sft_4b_s43_eval_r2, wave1_sft_4b_s44_eval_r2, eval_rsft_ced_s42 |",
          " | D111 | 2026-05-18 | D111: 4B SFT s42 必须用 D076 协议重新 eval，统一三 seed 参考基准 | wave1_sft_4b_s43_eval_r2, wave1_sft_4b_s44_eval_r2 |",
          " | D110 | 2026-05-18 | D110: GRPO bf16 ckpt-100 ign_f1=0.4431 无 catastrop | wave1_grpo_bf16_g4, grpo_bf16_g4_ckpt100_eval |",
          "-"
        ]
      }
    ],
    "originalFile": "# faith-evidence-ie — Research Dashboard\n\n> 最后更新: 2026-05-19 05:43 UTC | 更新原因: D115 8B RSFT 完成 + D114 1.7B Method A 裁决 + D112 进展 + 14B SFT 启动 + Wave 1 全部完成\n\n## 核心方向\nFREIGE: LLM-based evidence-grounded DocRE 系统性研究。3 贡献：RSFT+NLI 有效性 / Decoupling spectrum / Scale-dependent evidence tax。详见 paper_framing.md。\n\n## 当前进展\n- **阶段**: 🚀 Research + 审稿并行（Round 1 = 3.0 Findings，目标 4.0 Main）\n- **Wave 1**: ✅ 全部完成（SFT s43/s44, GRPO bf16 G=4, Random RSFT）\n- **Scaling seeds (plan_019)**: 8B 2-seed RSFT 完成（D115: s44=0.5451, variance 0.53pp）；1.7B s43/s44 重跑中（D114 Method A）\n- **D112 full pipeline**: Step 3 RSFT 训练中 cuda:0（验证 RSFT 在强 SFT base s44 上的泛化性）\n- **14B SFT (plan_017)**: cuda:1+2 运行中（2-GPU ZeRO-3, D108）\n- **关键数值汇总**:\n\n| Scale | SFT mean (seeds) | RSFT mean (seeds) | Δ ign_f1 | SFT std | RSFT std |\n|-------|-------------------|--------------------|----------|---------|----------|\n| 1.7B | 0.4464 (3) | 0.5122 (1, s42 base) | +6.58pp | 2.79pp | — |\n| 4B | 0.4358 (3) | 0.4482 (3, Method A) | +1.24pp | 3.80pp | 0.51pp |\n| 8B | 0.4866 (2) | 0.5414 (2, Method A) | +5.48pp | 2.62pp | 0.53pp |\n\n- **RSFT 稳定化效应**: 4B variance 3.80→0.51pp (7.5x)，8B variance 2.62→0.53pp (5x)\n- **CED 价值**: CED RSFT (0.4482) > Random RSFT (0.4114) > SFT (0.3974)，+3.68pp gap\n- **GRPO**: bf16 ckpt-100 ign_f1=0.4431 无 catastrophic forgetting（D110），QLoRA 是 confound\n\n## 投稿目标\n- **EMNLP 2026 Main** (ARR July cycle, ~July 15-25, **~57 天**)\n\n## 实验路线（3 层优先级）\n\n### Tier 1 — Main 必要条件\n| 实验 | Plan ID | 状态 |\n|------|---------|------|\n| D102 k=1 方法论修正 | D102 | ✅ 完成 |\n| SFT 4B s43 + s44 + s42 reeval | plan_w3_sft_seeds | ✅ 完成 (D111) |\n| GRPO bf16 G=4 clean control | plan_015 | ✅ 完成 (D110/D113) |\n| Random k=1 RSFT baseline | plan_w18_random | ✅ 完成 (D109) |\n| 8B RSFT s44 seed expansion | plan_019 (8B) | ✅ 完成 (D115) |\n| D112 RSFT from SFT s44 | plan_d112 | 🟡 Step 3 训练中 cuda:0 |\n| 1.7B RSFT s43/s44 重跑 | plan_019 (1.7B) | 🟡 s43_r2 提交中 cuda:3 |\n| 14B SFT (第 4 尺度) | plan_017 | 🟡 训练中 cuda:1+2 |\n\n### Tier 2 — 大幅加分\n| 实验 | Plan ID | 状态 |\n|------|---------|------|\n| 14B RSFT + no-evidence + eval | plan_017 (后续) | pending（等 SFT 完成） |\n| NLI model ablation | plan_010 | pending |\n| Evidence tax 机制分析 | plan_020 | pending |\n| Deep error analysis | plan_021 | pending |\n\n### Tier 3 — 锦上添花\n| 实验 | Plan ID | 状态 |\n|------|---------|------|\n| CDR/GDA 跨领域 | plan_018 | P2（无 evidence 标注） |\n| 第三模型家族 | plan_022 | pending |\n| DocKS-RAG/LMRC 复现 | plan_023 | pending |\n\n## 从 3.0 → 4.0 路径\n| 里程碑 | 预期评分 | 状态 |\n|--------|---------|------|\n| Wave 1 完成 + D112 | 3.0 → 3.5 | 🟡 D112 step 3 训练中 |\n| + 1.7B/8B multi-seed 统计力 | 3.5 | 🟡 8B done, 1.7B 重跑中 |\n| + 14B 第 4 尺度档 | 3.5 → 3.75 | 🟡 SFT 训练中 |\n| + Mechanistic + error analysis | 3.75 → 4.0 | pending |\n\n## GPU 预算\n- 本项目：rtx5090-4x cuda:0-3（4 张 RTX 5090）\n- 当前：4/4 在用（D112 step3 / 14B SFT×2 / 1.7B RSFT）\n- 剩余估算：Tier 1 ~15h + Tier 2 ~65h + Tier 3 ~100h\n\n## 近期任务\n- [x] Wave 1 全部完成（SFT seeds, GRPO bf16, Random RSFT）\n- [x] 8B RSFT s44 eval (D115: 0.5451, variance 压缩 5x)\n- [x] 4B SFT s42 D076 reeval (D111: 0.3974)\n- [ ] D112 step 3 → step 4 eval（cuda:0, ~1.5h total）\n- [ ] 1.7B RSFT s43_r2 + s44_r2 + eval（cuda:3, ~2-3h total）\n- [ ] 14B SFT 完成 → 14B RSFT + no-evidence + eval（cuda:1+2, ~8h SFT + 后续）\n- [ ] experiment_plan.yaml 全面同步 registry\n- [ ] paper_framing.md 更新（D112 结果 + 8B 2-seed + variance 压缩 narrative）\n- [ ] 重新提交论文审稿\n\n## 关键风险\n- **D112 结果待定**: 如 RSFT-from-s44 > SFT s44 (0.4734) → Claim 1 robust；否则需 reframe\n- **8B RSFT evidence quality trade-off**: EDCR 从 0.65-0.67 降到 0.62（RE↑/evidence precision↓），论文需讨论\n- **1.7B surpasses claim**: 现在更强（1.7B RSFT 0.5122 > 8B SFT mean 0.4866 +2.56pp），但仍需 1.7B multi-seed 确认\n- **14B 显存**: 2-GPU ZeRO-3 已启动且正常（D108 验证），后续 RSFT 可能需要调参\n- **EDCR 缺人工验证**: plan_013 取消，用 per-relation 分析 + Limitations 缓解\n\n## 关键决策日志\n\n| ID | 日期 | 摘要 | 关联实验 |\n|----|------|------|----------|\n| D119 | 2026-05-19 | D119: D112 bf16 eval ign_f1=0.5152 确认 Method B (RS | d112_rsft_s44_eval_bf16, d112_rsft_s44_eval |\n| D118 | 2026-05-19 | D118: \"1.7B RSFT surpasses 8B SFT\" claim 降级为 \"appr | plan019_8b_sft_s43_eval, plan019_1_7b_rsft_s44_r2_eval |\n| D117 | 2026-05-19 | D117: 14B SFT evidence tax = 0.03pp（本质为零），完成 4 尺度  | plan017_14b_sft_eval_r2, plan017_14b_sft_no_evidence_eval_r2 |\n| D116 | 2026-05-19 | D116: D112 结果无效（QLoRA confound），必须用 bf16 LoRA 重跑 s | d112_rsft_s44_eval, d112_rsft_s44_train |\n| D115 | 2026-05-19 | D115: 8B RSFT s44 ign_f1=0.5451 确认 RSFT 跨 seed 稳健， | plan019_8b_rsft_s44_eval, eval_rsft_ced_s42 |\n| D114 | 2026-05-19 | D114: 1.7B RSFT s43/s44 应使用 Method A（s42 SFT base） | plan019_1_7b_rsft_s43, plan019_1_7b_rsft_s44, d112_rsft_s44_ced_score |\n| D113 | 2026-05-18 | D113: GRPO bf16 ckpt-100 为最优 checkpoint，ckpt-200 无 | grpo_bf16_g4_ckpt100_eval, grpo_bf16_g4_ckpt200_eval |\n| D112 | 2026-05-18 | D112: 4B RSFT ign_f1 claim 需重大 reframe——全部 RSFT 基于 | wave1_sft_4b_s43_eval_r2, wave1_sft_4b_s44_eval_r2, eval_rsft_ced_s42 |\n| D111 | 2026-05-18 | D111: 4B SFT s42 必须用 D076 协议重新 eval，统一三 seed 参考基准 | wave1_sft_4b_s43_eval_r2, wave1_sft_4b_s44_eval_r2 |\n| D110 | 2026-05-18 | D110: GRPO bf16 ckpt-100 ign_f1=0.4431 无 catastrop | wave1_grpo_bf16_g4, grpo_bf16_g4_ckpt100_eval |\n\n",
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 33_

ROADMAP.md 已更新。主要变更：

- **Scaling table**: 新增 14B 行 (0.5507)，8B SFT 从 2-seed 0.4866 更新为 3-seed 0.5019，4B 加入 D112 Method B 结果 (0.5152)，8B Δ 从 +5.48pp 修正为 +3.95pp
- **D112**: 标记完成，ign_f1=0.5152 (+4.18pp over s44 baseline)
- **14B evidence tax (D117)**: tax=0.03pp≈0，14B 容量足够
- **1.7B claim (D118)**: "surpasses" 降级为 "comparable"，variance stabilization 独立化
- **Tier 1 实验**: D112、8B SFT s43、14B SFT 全部标记 ✅；8B RSFT s43 移入 Tier 2
- **GPU 分布**: 更新为当前状态（cuda:2 空闲）
- **关键风险**: D112 标记已解决，1.7B/14B 风险项更新为最新结论

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ac6c3eaa-1181-4230-9499-9a3dbe044d7c",
  "uuid": "09c6bb17-1a37-4ae1-a3bc-16409867c65f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BatfLXE94Vy7BNsB3vv6SP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3781,
      "cache_read_input_tokens": 39273,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3781
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

### Task result

_source line 34_

ROADMAP.md 已更新。主要变更：

- **Scaling table**: 新增 14B 行 (0.5507)，8B SFT 从 2-seed 0.4866 更新为 3-seed 0.5019，4B 加入 D112 Method B 结果 (0.5152)，8B Δ 从 +5.48pp 修正为 +3.95pp
- **D112**: 标记完成，ign_f1=0.5152 (+4.18pp over s44 baseline)
- **14B evidence tax (D117)**: tax=0.03pp≈0，14B 容量足够
- **1.7B claim (D118)**: "surpasses" 降级为 "comparable"，variance stabilization 独立化
- **Tier 1 实验**: D112、8B SFT s43、14B SFT 全部标记 ✅；8B RSFT s43 移入 Tier 2
- **GPU 分布**: 更新为当前状态（cuda:2 空闲）
- **关键风险**: D112 标记已解决，1.7B/14B 风险项更新为最新结论

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 146080,
  "duration_api_ms": 147062,
  "num_turns": 10,
  "stop_reason": "end_turn",
  "session_id": "ac6c3eaa-1181-4230-9499-9a3dbe044d7c",
  "total_cost_usd": 0.57348425,
  "usage": {
    "input_tokens": 17,
    "cache_creation_input_tokens": 31213,
    "cache_read_input_tokens": 270058,
    "output_tokens": 9638,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 31213,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 325,
        "cache_read_input_tokens": 39273,
        "cache_creation_input_tokens": 3781,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 3781
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2259,
      "outputTokens": 16,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002339,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 17,
      "outputTokens": 9638,
      "cacheReadInputTokens": 270058,
      "cacheCreationInputTokens": 31213,
      "webSearchRequests": 0,
      "costUSD": 0.57114525,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "6ecf8701-6b9f-4753-8842-fe03b44034e8"
}
```

</details>

---
