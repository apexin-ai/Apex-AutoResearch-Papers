# ops update roadmap 1 7b 2048

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 35
- **Recorded user turns:** 0
- **Tool calls:** 11
- **Original source:** `logs/workers/worker_ops_update_roadmap_1_7b_2048_20260519T201205.log`
- **Structured JSON:** [`dfefbe9686db121746ac.json`](../../sessions/df/dfefbe9686db121746ac.json)

## Before a recorded user message

35 recorded events

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
  "session_id": "bd67c934-a0d4-42da-9473-8ddc185c5800",
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
    "mcp__agent-ml-research__save_project_file"
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
  "uuid": "80ac7cfa-384b-49f4-b545-5e3cde39fe3a",
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
    "resetsAt": 1779235200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "bfd18243-b135-4e14-82b1-07aee0520ec5",
  "session_id": "bd67c934-a0d4-42da-9473-8ddc185c5800"
}
```

---

### Assistant

_source line 4_

Let me start by reading the current ROADMAP.md and checking available tools.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bd67c934-a0d4-42da-9473-8ddc185c5800",
  "uuid": "299ca014-1dfb-4f39-b887-5c288b3bba35",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014gRMA3W2vSJ7wYX3Pd77J7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12408,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12408
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01LQoAmNCwGLQkDTT1cmWQ29`</summary>

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
  "session_id": "bd67c934-a0d4-42da-9473-8ddc185c5800",
  "uuid": "acfeae4c-1271-4fbd-96cd-570648e68faf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014gRMA3W2vSJ7wYX3Pd77J7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12408,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12408
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

_source line 6 · 2026-05-19T20:12:15.626Z_

<details><summary>↩ Tool result · `toolu_01LQoAmNCwGLQkDTT1cmWQ29`</summary>

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
  "session_id": "bd67c934-a0d4-42da-9473-8ddc185c5800",
  "uuid": "f500e9af-f2de-4fc6-8a92-d7acf9c01125",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Assistant

_source line 7_

<details><summary>Logged reasoning block</summary>

```text
The tool description confirms ROADMAP.md needs `update_roadmap` tool. Let me search for that tool and also read the current ROADMAP.md in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bd67c934-a0d4-42da-9473-8ddc185c5800",
  "uuid": "4e04d19a-fe49-4fa4-92d0-ea6965b0c323",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E9ndSwc6xdA9D33NzcZxDa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 717,
      "cache_read_input_tokens": 24249,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 717
      },
      "output_tokens": 28,
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Nj7iMe4qYhhKgT3HHt1kdu`</summary>

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
  "session_id": "bd67c934-a0d4-42da-9473-8ddc185c5800",
  "uuid": "db234102-459e-4b46-acc7-91b0f68503f4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E9ndSwc6xdA9D33NzcZxDa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 717,
      "cache_read_input_tokens": 24249,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 717
      },
      "output_tokens": 28,
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

_source line 9 · 2026-05-19T20:12:20.846Z_

<details><summary>↩ Tool result · `toolu_01Nj7iMe4qYhhKgT3HHt1kdu`</summary>

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
  "session_id": "bd67c934-a0d4-42da-9473-8ddc185c5800",
  "uuid": "6359af19-3b6e-4020-a95f-cd27ce8793a1",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "update_roadmap",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_018fovvA6wDN2DeLW4dBAJSh`</summary>

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
  "session_id": "bd67c934-a0d4-42da-9473-8ddc185c5800",
  "uuid": "8f6c19ec-1822-4f38-9fa0-2b14fc1b7781",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01E9ndSwc6xdA9D33NzcZxDa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 717,
      "cache_read_input_tokens": 24249,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 717
      },
      "output_tokens": 28,
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

_source line 11 · 2026-05-19T20:12:21.207Z_

<details><summary>↩ Tool result · `toolu_018fovvA6wDN2DeLW4dBAJSh`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/ROADMAP.md\", \"content\": \"# faith-evidence-ie — Research Dashboard\\n\\n> 最后更新: 2026-05-19 18:21 UTC | 更新原因: Fix contribution count: variance compression folded into C3, not separate 4th contribution\\n\\n## 核心方向\\nFREIGE: LLM-based evidence-grounded DocRE 系统性研究。3 贡献：(1) RSFT+NLI 有效性 (2) Decoupling spectrum (3) Scale-dependent evidence tax + variance compression。详见 paper_framing.md。\\n\\n## 当前进展\\n- **阶段**: 🚀 Research + 审稿并行（Round 1 = 3.0 Findings，目标 4.0 Main）\\n- **Scaling table 完成度**: 4/4 尺度 SFT 完成，3/4 尺度 RSFT 完成（14B RSFT pipeline running）\\n- **D118 claim 降级**: \\\"surpasses\\\" → \\\"approaches\\\"（1.7B RSFT 0.5119 vs 8B SFT 0.5019, Δ=1.0pp, p=0.69）\\n- **D118 核心发现升级**: Variance compression 7-31× across scales（归入 C3）\\n- **D117**: 14B evidence tax=+0.03pp（零），4 尺度 tax curve 完整（含 RSFT tax 列）\\n- **D119**: D112 Method B bf16 ign_f1=0.5152, RSFT pipeline 可复现\\n- **Mechanistic analysis (plan_020)**: ✅ 完成——duplication regularization / truncation asymmetry / fair comparison residual\\n- **Deep error analysis (plan_021)**: ✅ 完成——truncation FN↓ / hallucinated FP↓ / duplicate↓\\n\\n| Scale | SFT mean (seeds) | RSFT mean (seeds) | Δ ign_f1 | Variance compression |\\n|-------|-------------------|--------------------|----------|---------------------|\\n| 1.7B | 0.4464 (3) | 0.5119 (3) | +6.55pp | **31×** (2.79→0.09pp) |\\n| 4B | 0.4358 (3) | 0.4482 (3, A) / 0.5152 (1, B) | +1.24 / +4.18pp | **7.5×** (3.80→0.51pp) |\\n| 8B | 0.5019 (3) | 0.5433 (3) | +4.14pp | **7.4×** (3.72→0.50pp) |\\n| 14B | 0.5507 (1) | 🔄 pipeline running | — | — |\\n\\n## 投稿目标\\n- **EMNLP 2026 Main** (ARR July cycle, ~July 15-25, **~57 天**)\\n\\n## 实验路线（3 层优先级）\\n\\n### Tier 1 — Main 必要条件\\n| 实验 | 状态 |\\n|------|------|\\n| D102 k=1 方法论修正 | ✅ |\\n| SFT 4B s43+s44+s42 reeval | ✅ D111 |\\n| GRPO bf16 G=4 clean control | ✅ D110/D113 |\\n| Random k=1 RSFT baseline | ✅ D109 |\\n| 8B RSFT 3-seed (s42/s43/s44) | ✅ D115/D120 |\\n| D112 RSFT from SFT s44 (bf16) | ✅ D119 |\\n| 14B SFT (第 4 尺度) | ✅ D117 |\\n| 1.7B RSFT 3-seed | ✅ |\\n| 14B RSFT pipeline | 🔄 Step 1 gen (3.8%, ETA ~18.5h, cuda:0+2) |\\n\\n### Tier 2 — 大幅加分\\n| 实验 | 状态 |\\n|------|------|\\n| Evidence tax mechanistic analysis | ✅ plan_020（⚠️ 缺 registry 记录，需补） |\\n| Deep error analysis | ✅ plan_021（⚠️ 缺 registry 记录，需补） |\\n| NLI model ablation | plan_010, 🔄 cuda:1 释放后启动 |\\n| Evidence tax 全 scale curve + RSFT 列 | 🔄 d112 no-evi eval (cuda:1, 97%) + 1.7B 2048 (cuda:3, 66%) |\\n| 14B RSFT eval + no-evidence | pending（14B gen 完成后） |\\n\\n### Tier 3 — 锦上添花\\n| 实验 | 状态 |\\n|------|------|\\n| CDR/GDA 跨领域 | P2（无 evidence 标注） |\\n| 第三模型家族 | pending |\\n\\n## 从 3.0 → 4.0 路径\\n| 里程碑 | 预期评分 | 状态 |\\n|--------|---------|------|\\n| Wave 1 + D112 + multi-seed | 3.0 → 3.5 | ✅ |\\n| + 14B 第 4 尺度档 | 3.5 → 3.75 | 🔄 SFT ✅, RSFT pipeline running |\\n| + Mechanistic + error analysis | → 3.75 | ✅ plan_020 + plan_021 |\\n| + NLI ablation + variance compression narrative | → 4.0 | 🔄 plan_010 启动中 |\\n\\n## GPU 分布\\n- cuda:0 + cuda:2: plan017_14b_rsft_generate (3.8%, ETA ~18.5h)\\n- cuda:1: d112_rsft_no_evidence_eval_r3 (97%, ~5min) → plan_010 NLI ablation\\n- cuda:3: plan019_1_7b_rsft_no_evidence_eval_2048 (66%, ~1h46m)\\n\\n## 近期任务\\n- [x] paper_framing.md D117-D120 更新\\n- [x] Paper Agent briefed on Claim 5 reframing patch\\n- [x] ROADMAP 贡献数量与 paper_framing.md 对齐（3 贡献）\\n- [ ] d112 no-evidence eval 完成 → 4B RSFT evidence tax\\n- [ ] plan_010 NLI ablation 启动 (cuda:1)\\n- [ ] 1.7B no-evidence 2048 完成 → 确认/排除 negative tax\\n- [ ] 14B RSFT pipeline 完成 → scaling table 最后一行\\n- [ ] plan_020/021 补 registry 记录 + decision\\n- [ ] experiment_plan.yaml 同步\\n- [ ] 重新提交论文审稿\\n\\n## 关键风险\\n- **1.7B evidence tax confounded**: 59.2% truncation@1024，2048 rerun 在跑\\n- **14B RSFT gen ETA 18.5h**: 比预期长，cuda:0+2 长期锁定\\n- **plan_020/021 可追溯性**: 分析数据在 paper_framing.md 但缺 registry/decision 记录\\n- **EDCR 缺人工验证**: plan_013 取消，用 per-relation 分析 + Limitations 缓解\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D122 | 2026-05-19 | D122: Negative results audit 完成——16/19 RESOLVED, 1 | mvp2_eval_rsft_r2b_maxtok1536_r2 |\\n| D121 | 2026-05-19 | D121: 4B RSFT evidence tax = +0.94pp (near zero),  | d112_rsft_no_evidence_eval_r3, d112_rsft_s44_eval_bf16 |\\n| D120 | 2026-05-19 | D120: 8B RSFT 3-seed 确认 variance compression 7.4×， | d102_8b_rsft_k1_s43, plan019_8b_rsft_s44_eval |\\n| D119 | 2026-05-19 | D119: D112 bf16 eval ign_f1=0.5152 确认 Method B (RS | d112_rsft_s44_eval_bf16, d112_rsft_s44_eval |\\n| D118 | 2026-05-19 | D118: \\\"1.7B RSFT surpasses 8B SFT\\\" claim 降级为 \\\"appr | plan019_8b_sft_s43_eval, plan019_1_7b_rsft_s44_r2_eval |\\n| D117 | 2026-05-19 | D117: 14B SFT evidence tax = 0.03pp（本质为零），完成 4 尺度  | plan017_14b_sft_eval_r2, plan017_14b_sft_no_evidence_eval_r2 |\\n| D116 | 2026-05-19 | D116: D112 结果无效（QLoRA confound），必须用 bf16 LoRA 重跑 s | d112_rsft_s44_eval, d112_rsft_s44_train |\\n| D115 | 2026-05-19 | D115: 8B RSFT s44 ign_f1=0.5451 确认 RSFT 跨 seed 稳健， | plan019_8b_rsft_s44_eval, eval_rsft_ced_s42 |\\n| D114 | 2026-05-19 | D114: 1.7B RSFT s43/s44 应使用 Method A（s42 SFT base） | plan019_1_7b_rsft_s43, plan019_1_7b_rsft_s44, d112_rsft_s44_ced_score |\\n| D113 | 2026-05-18 | D113: GRPO bf16 ckpt-100 为最优 checkpoint，ckpt-200 无 | grpo_bf16_g4_ckpt100_eval, grpo_bf16_g4_ckpt200_eval |\\n\\n\", \"total_chars\": 5028, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bd67c934-a0d4-42da-9473-8ddc185c5800",
  "uuid": "61e409ba-8c44-447d-8795-b5d02dbca2fb",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/ROADMAP.md\\\", \\\"content\\\": \\\"# faith-evidence-ie — Research Dashboard\\\\n\\\\n> 最后更新: 2026-05-19 18:21 UTC | 更新原因: Fix contribution count: variance compression folded into C3, not separate 4th contribution\\\\n\\\\n## 核心方向\\\\nFREIGE: LLM-based evidence-grounded DocRE 系统性研究。3 贡献：(1) RSFT+NLI 有效性 (2) Decoupling spectrum (3) Scale-dependent evidence tax + variance compression。详见 paper_framing.md。\\\\n\\\\n## 当前进展\\\\n- **阶段**: 🚀 Research + 审稿并行（Round 1 = 3.0 Findings，目标 4.0 Main）\\\\n- **Scaling table 完成度**: 4/4 尺度 SFT 完成，3/4 尺度 RSFT 完成（14B RSFT pipeline running）\\\\n- **D118 claim 降级**: \\\\\\\"surpasses\\\\\\\" → \\\\\\\"approaches\\\\\\\"（1.7B RSFT 0.5119 vs 8B SFT 0.5019, Δ=1.0pp, p=0.69）\\\\n- **D118 核心发现升级**: Variance compression 7-31× across scales（归入 C3）\\\\n- **D117**: 14B evidence tax=+0.03pp（零），4 尺度 tax curve 完整（含 RSFT tax 列）\\\\n- **D119**: D112 Method B bf16 ign_f1=0.5152, RSFT pipeline 可复现\\\\n- **Mechanistic analysis (plan_020)**: ✅ 完成——duplication regularization / truncation asymmetry / fair comparison residual\\\\n- **Deep error analysis (plan_021)**: ✅ 完成——truncation FN↓ / hallucinated FP↓ / duplicate↓\\\\n\\\\n| Scale | SFT mean (seeds) | RSFT mean (seeds) | Δ ign_f1 | Variance compression |\\\\n|-------|-------------------|--------------------|----------|---------------------|\\\\n| 1.7B | 0.4464 (3) | 0.5119 (3) | +6.55pp | **31×** (2.79→0.09pp) |\\\\n| 4B | 0.4358 (3) | 0.4482 (3, A) / 0.5152 (1, B) | +1.24 / +4.18pp | **7.5×** (3.80→0.51pp) |\\\\n| 8B | 0.5019 (3) | 0.5433 (3) | +4.14pp | **7.4×** (3.72→0.50pp) |\\\\n| 14B | 0.5507 (1) | 🔄 pipeline running | — | — |\\\\n\\\\n## 投稿目标\\\\n- **EMNLP 2026 Main** (ARR July cycle, ~July 15-25, **~57 天**)\\\\n\\\\n## 实验路线（3 层优先级）\\\\n\\\\n### Tier 1 — Main 必要条件\\\\n| 实验 | 状态 |\\\\n|------|------|\\\\n| D102 k=1 方法论修正 | ✅ |\\\\n| SFT 4B s43+s44+s42 reeval | ✅ D111 |\\\\n| GRPO bf16 G=4 clean control | ✅ D110/D113 |\\\\n| Random k=1 RSFT baseline | ✅ D109 |\\\\n| 8B RSFT 3-seed (s42/s43/s44) | ✅ D115/D120 |\\\\n| D112 RSFT from SFT s44 (bf16) | ✅ D119 |\\\\n| 14B SFT (第 4 尺度) | ✅ D117 |\\\\n| 1.7B RSFT 3-seed | ✅ |\\\\n| 14B RSFT pipeline | 🔄 Step 1 gen (3.8%, ETA ~18.5h, cuda:0+2) |\\\\n\\\\n### Tier 2 — 大幅加分\\\\n| 实验 | 状态 |\\\\n|------|------|\\\\n| Evidence tax mechanistic analysis | ✅ plan_020（⚠️ 缺 registry 记录，需补） |\\\\n| Deep error analysis | ✅ plan_021（⚠️ 缺 registry 记录，需补） |\\\\n| NLI model ablation | plan_010, 🔄 cuda:1 释放后启动 |\\\\n| Evidence tax 全 scale curve + RSFT 列 | 🔄 d112 no-evi eval (cuda:1, 97%) + 1.7B 2048 (cuda:3, 66%) |\\\\n| 14B RSFT eval + no-evidence | pending（14B gen 完成后） |\\\\n\\\\n### Tier 3 — 锦上添花\\\\n| 实验 | 状态 |\\\\n|------|------|\\\\n| CDR/GDA 跨领域 | P2（无 evidence 标注） |\\\\n| 第三模型家族 | pending |\\\\n\\\\n## 从 3.0 → 4.0 路径\\\\n| 里程碑 | 预期评分 | 状态 |\\\\n|--------|---------|------|\\\\n| Wave 1 + D112 + multi-seed | 3.0 → 3.5 | ✅ |\\\\n| + 14B 第 4 尺度档 | 3.5 → 3.75 | 🔄 SFT ✅, RSFT pipeline running |\\\\n| + Mechanistic + error analysis | → 3.75 | ✅ plan_020 + plan_021 |\\\\n| + NLI ablation + variance compression narrative | → 4.0 | 🔄 plan_010 启动中 |\\\\n\\\\n## GPU 分布\\\\n- cuda:0 + cuda:2: plan017_14b_rsft_generate (3.8%, ETA ~18.5h)\\\\n- cuda:1: d112_rsft_no_evidence_eval_r3 (97%, ~5min) → plan_010 NLI ablation\\\\n- cuda:3: plan019_1_7b_rsft_no_evidence_eval_2048 (66%, ~1h46m)\\\\n\\\\n## 近期任务\\\\n- [x] paper_framing.md D117-D120 更新\\\\n- [x] Paper Agent briefed on Claim 5 reframing patch\\\\n- [x] ROADMAP 贡献数量与 paper_framing.md 对齐（3 贡献）\\\\n- [ ] d112 no-evidence eval 完成 → 4B RSFT evidence tax\\\\n- [ ] plan_010 NLI ablation 启动 (cuda:1)\\\\n- [ ] 1.7B no-evidence 2048 完成 → 确认/排除 negative tax\\\\n- [ ] 14B RSFT pipeline 完成 → scaling table 最后一行\\\\n- [ ] plan_020/021 补 registry 记录 + decision\\\\n- [ ] experiment_plan.yaml 同步\\\\n- [ ] 重新提交论文审稿\\\\n\\\\n## 关键风险\\\\n- **1.7B evidence tax confounded**: 59.2% truncation@1024，2048 rerun 在跑\\\\n- **14B RSFT gen ETA 18.5h**: 比预期长，cuda:0+2 长期锁定\\\\n- **plan_020/021 可追溯性**: 分析数据在 paper_framing.md 但缺 registry/decision 记录\\\\n- **EDCR 缺人工验证**: plan_013 取消，用 per-relation 分析 + Limitations 缓解\\\\n\\\\n## 关键决策日志\\\\n\\\\n| ID | 日期 | 摘要 | 关联实验 |\\\\n|----|------|------|----------|\\\\n| D122 | 2026-05-19 | D122: Negative results audit 完成——16/19 RESOLVED, 1 | mvp2_eval_rsft_r2b_maxtok1536_r2 |\\\\n| D121 | 2026-05-19 | D121: 4B RSFT evidence tax = +0.94pp (near zero),  | d112_rsft_no_evidence_eval_r3, d112_rsft_s44_eval_bf16 |\\\\n| D120 | 2026-05-19 | D120: 8B RSFT 3-seed 确认 variance compression 7.4×， | d102_8b_rsft_k1_s43, plan019_8b_rsft_s44_eval |\\\\n| D119 | 2026-05-19 | D119: D112 bf16 eval ign_f1=0.5152 确认 Method B (RS | d112_rsft_s44_eval_bf16, d112_rsft_s44_eval |\\\\n| D118 | 2026-05-19 | D118: \\\\\\\"1.7B RSFT surpasses 8B SFT\\\\\\\" claim 降级为 \\\\\\\"appr | plan019_8b_sft_s43_eval, plan019_1_7b_rsft_s44_r2_eval |\\\\n| D117 | 2026-05-19 | D117: 14B SFT evidence tax = 0.03pp（本质为零），完成 4 尺度  | plan017_14b_sft_eval_r2, plan017_14b_sft_no_evidence_eval_r2 |\\\\n| D116 | 2026-05-19 | D116: D112 结果无效（QLoRA confound），必须用 bf16 LoRA 重跑 s | d112_rsft_s44_eval, d112_rsft_s44_train |\\\\n| D115 | 2026-05-19 | D115: 8B RSFT s44 ign_f1=0.5451 确认 RSFT 跨 seed 稳健， | plan019_8b_rsft_s44_eval, eval_rsft_ced_s42 |\\\\n| D114 | 2026-05-19 | D114: 1.7B RSFT s43/s44 应使用 Method A（s42 SFT base） | plan019_1_7b_rsft_s43, plan019_1_7b_rsft_s44, d112_rsft_s44_ced_score |\\\\n| D113 | 2026-05-18 | D113: GRPO bf16 ckpt-100 为最优 checkpoint，ckpt-200 无 | grpo_bf16_g4_ckpt100_eval, grpo_bf16_g4_ckpt200_eval |\\\\n\\\\n\\\", \\\"total_chars\\\": 5028, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/ROADMAP.md\", \"content\": \"# faith-evidence-ie — Research Dashboard\\n\\n> 最后更新: 2026-05-19 18:21 UTC | 更新原因: Fix contribution count: variance compression folded into C3, not separate 4th contribution\\n\\n## 核心方向\\nFREIGE: LLM-based evidence-grounded DocRE 系统性研究。3 贡献：(1) RSFT+NLI 有效性 (2) Decoupling spectrum (3) Scale-dependent evidence tax + variance compression。详见 paper_framing.md。\\n\\n## 当前进展\\n- **阶段**: 🚀 Research + 审稿并行（Round 1 = 3.0 Findings，目标 4.0 Main）\\n- **Scaling table 完成度**: 4/4 尺度 SFT 完成，3/4 尺度 RSFT 完成（14B RSFT pipeline running）\\n- **D118 claim 降级**: \\\"surpasses\\\" → \\\"approaches\\\"（1.7B RSFT 0.5119 vs 8B SFT 0.5019, Δ=1.0pp, p=0.69）\\n- **D118 核心发现升级**: Variance compression 7-31× across scales（归入 C3）\\n- **D117**: 14B evidence tax=+0.03pp（零），4 尺度 tax curve 完整（含 RSFT tax 列）\\n- **D119**: D112 Method B bf16 ign_f1=0.5152, RSFT pipeline 可复现\\n- **Mechanistic analysis (plan_020)**: ✅ 完成——duplication regularization / truncation asymmetry / fair comparison residual\\n- **Deep error analysis (plan_021)**: ✅ 完成——truncation FN↓ / hallucinated FP↓ / duplicate↓\\n\\n| Scale | SFT mean (seeds) | RSFT mean (seeds) | Δ ign_f1 | Variance compression |\\n|-------|-------------------|--------------------|----------|---------------------|\\n| 1.7B | 0.4464 (3) | 0.5119 (3) | +6.55pp | **31×** (2.79→0.09pp) |\\n| 4B | 0.4358 (3) | 0.4482 (3, A) / 0.5152 (1, B) | +1.24 / +4.18pp | **7.5×** (3.80→0.51pp) |\\n| 8B | 0.5019 (3) | 0.5433 (3) | +4.14pp | **7.4×** (3.72→0.50pp) |\\n| 14B | 0.5507 (1) | 🔄 pipeline running | — | — |\\n\\n## 投稿目标\\n- **EMNLP 2026 Main** (ARR July cycle, ~July 15-25, **~57 天**)\\n\\n## 实验路线（3 层优先级）\\n\\n### Tier 1 — Main 必要条件\\n| 实验 | 状态 |\\n|------|------|\\n| D102 k=1 方法论修正 | ✅ |\\n| SFT 4B s43+s44+s42 reeval | ✅ D111 |\\n| GRPO bf16 G=4 clean control | ✅ D110/D113 |\\n| Random k=1 RSFT baseline | ✅ D109 |\\n| 8B RSFT 3-seed (s42/s43/s44) | ✅ D115/D120 |\\n| D112 RSFT from SFT s44 (bf16) | ✅ D119 |\\n| 14B SFT (第 4 尺度) | ✅ D117 |\\n| 1.7B RSFT 3-seed | ✅ |\\n| 14B RSFT pipeline | 🔄 Step 1 gen (3.8%, ETA ~18.5h, cuda:0+2) |\\n\\n### Tier 2 — 大幅加分\\n| 实验 | 状态 |\\n|------|------|\\n| Evidence tax mechanistic analysis | ✅ plan_020（⚠️ 缺 registry 记录，需补） |\\n| Deep error analysis | ✅ plan_021（⚠️ 缺 registry 记录，需补） |\\n| NLI model ablation | plan_010, 🔄 cuda:1 释放后启动 |\\n| Evidence tax 全 scale curve + RSFT 列 | 🔄 d112 no-evi eval (cuda:1, 97%) + 1.7B 2048 (cuda:3, 66%) |\\n| 14B RSFT eval + no-evidence | pending（14B gen 完成后） |\\n\\n### Tier 3 — 锦上添花\\n| 实验 | 状态 |\\n|------|------|\\n| CDR/GDA 跨领域 | P2（无 evidence 标注） |\\n| 第三模型家族 | pending |\\n\\n## 从 3.0 → 4.0 路径\\n| 里程碑 | 预期评分 | 状态 |\\n|--------|---------|------|\\n| Wave 1 + D112 + multi-seed | 3.0 → 3.5 | ✅ |\\n| + 14B 第 4 尺度档 | 3.5 → 3.75 | 🔄 SFT ✅, RSFT pipeline running |\\n| + Mechanistic + error analysis | → 3.75 | ✅ plan_020 + plan_021 |\\n| + NLI ablation + variance compression narrative | → 4.0 | 🔄 plan_010 启动中 |\\n\\n## GPU 分布\\n- cuda:0 + cuda:2: plan017_14b_rsft_generate (3.8%, ETA ~18.5h)\\n- cuda:1: d112_rsft_no_evidence_eval_r3 (97%, ~5min) → plan_010 NLI ablation\\n- cuda:3: plan019_1_7b_rsft_no_evidence_eval_2048 (66%, ~1h46m)\\n\\n## 近期任务\\n- [x] paper_framing.md D117-D120 更新\\n- [x] Paper Agent briefed on Claim 5 reframing patch\\n- [x] ROADMAP 贡献数量与 paper_framing.md 对齐（3 贡献）\\n- [ ] d112 no-evidence eval 完成 → 4B RSFT evidence tax\\n- [ ] plan_010 NLI ablation 启动 (cuda:1)\\n- [ ] 1.7B no-evidence 2048 完成 → 确认/排除 negative tax\\n- [ ] 14B RSFT pipeline 完成 → scaling table 最后一行\\n- [ ] plan_020/021 补 registry 记录 + decision\\n- [ ] experiment_plan.yaml 同步\\n- [ ] 重新提交论文审稿\\n\\n## 关键风险\\n- **1.7B evidence tax confounded**: 59.2% truncation@1024，2048 rerun 在跑\\n- **14B RSFT gen ETA 18.5h**: 比预期长，cuda:0+2 长期锁定\\n- **plan_020/021 可追溯性**: 分析数据在 paper_framing.md 但缺 registry/decision 记录\\n- **EDCR 缺人工验证**: plan_013 取消，用 per-relation 分析 + Limitations 缓解\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D122 | 2026-05-19 | D122: Negative results audit 完成——16/19 RESOLVED, 1 | mvp2_eval_rsft_r2b_maxtok1536_r2 |\\n| D121 | 2026-05-19 | D121: 4B RSFT evidence tax = +0.94pp (near zero),  | d112_rsft_no_evidence_eval_r3, d112_rsft_s44_eval_bf16 |\\n| D120 | 2026-05-19 | D120: 8B RSFT 3-seed 确认 variance compression 7.4×， | d102_8b_rsft_k1_s43, plan019_8b_rsft_s44_eval |\\n| D119 | 2026-05-19 | D119: D112 bf16 eval ign_f1=0.5152 确认 Method B (RS | d112_rsft_s44_eval_bf16, d112_rsft_s44_eval |\\n| D118 | 2026-05-19 | D118: \\\"1.7B RSFT surpasses 8B SFT\\\" claim 降级为 \\\"appr | plan019_8b_sft_s43_eval, plan019_1_7b_rsft_s44_r2_eval |\\n| D117 | 2026-05-19 | D117: 14B SFT evidence tax = 0.03pp（本质为零），完成 4 尺度  | plan017_14b_sft_eval_r2, plan017_14b_sft_no_evidence_eval_r2 |\\n| D116 | 2026-05-19 | D116: D112 结果无效（QLoRA confound），必须用 bf16 LoRA 重跑 s | d112_rsft_s44_eval, d112_rsft_s44_train |\\n| D115 | 2026-05-19 | D115: 8B RSFT s44 ign_f1=0.5451 确认 RSFT 跨 seed 稳健， | plan019_8b_rsft_s44_eval, eval_rsft_ced_s42 |\\n| D114 | 2026-05-19 | D114: 1.7B RSFT s43/s44 应使用 Method A（s42 SFT base） | plan019_1_7b_rsft_s43, plan019_1_7b_rsft_s44, d112_rsft_s44_ced_score |\\n| D113 | 2026-05-18 | D113: GRPO bf16 ckpt-100 为最优 checkpoint，ckpt-200 无 | grpo_bf16_g4_ckpt100_eval, grpo_bf16_g4_ckpt200_eval |\\n\\n\", \"total_chars\": 5028, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
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
No `update_roadmap` tool was found in the search. The `save_project_file` description says ROADMAP.md should use `update_roadmap`, but that tool doesn't seem to exist in the available MCP tools. Let me try searching more specifically for it.

Actually, looking at the ToolSearch results, it only returned `save_project_file` - no `update_roadmap` tool was found. Let me try to use `save_project_file` with file="ROADMAP.md" anyway - it might work or it might error. Alternatively, I can write directly to the file path since I know it: `/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/ROADMAP.md`.


I'll write the file directly using the Write tool since I've already read the content. I need to update the roadmap with the latest results: marking the evidence tax scale curve as complete with full results, confirming the 1.7B 2048 rerun conclusion about the evidence tax effect, and updating the GPU distribution status with the current running experiments. I'm updating the ROADMAP.md file to reflect the current experiment status and resolved items.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bd67c934-a0d4-42da-9473-8ddc185c5800",
  "uuid": "6536c528-e184-4e37-945f-2630c60c8591",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NFoq93Nbh2yA2jcXAz7xCN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3567,
      "cache_read_input_tokens": 24966,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3567
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

_source line 13_

`update_roadmap` tool not found. I'll write the file directly.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bd67c934-a0d4-42da-9473-8ddc185c5800",
  "uuid": "5e82d6ca-4e8e-4861-9a81-fd4fadeaaf7e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NFoq93Nbh2yA2jcXAz7xCN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3567,
      "cache_read_input_tokens": 24966,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3567
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

_source line 14_

<details open><summary>🔧 Tool call — Read · `toolu_01V6w6e6ZRgkFWyjuRTEKVn4`</summary>

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
  "session_id": "bd67c934-a0d4-42da-9473-8ddc185c5800",
  "uuid": "970c9d34-da82-4fb4-9da9-f36c87ae3bac",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NFoq93Nbh2yA2jcXAz7xCN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3567,
      "cache_read_input_tokens": 24966,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3567
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

_source line 15 · 2026-05-19T20:12:35.529Z_

<details><summary>↩ Tool result · `toolu_01V6w6e6ZRgkFWyjuRTEKVn4`</summary>

```text
1	# faith-evidence-ie — Research Dashboard
2	
3	> 最后更新: 2026-05-19 18:21 UTC | 更新原因: Fix contribution count: variance compression folded into C3, not separate 4th contribution
4	
5	## 核心方向
6	FREIGE: LLM-based evidence-grounded DocRE 系统性研究。3 贡献：(1) RSFT+NLI 有效性 (2) Decoupling spectrum (3) Scale-dependent evidence tax + variance compression。详见 paper_framing.md。
7	
8	## 当前进展
9	- **阶段**: 🚀 Research + 审稿并行（Round 1 = 3.0 Findings，目标 4.0 Main）
10	- **Scaling table 完成度**: 4/4 尺度 SFT 完成，3/4 尺度 RSFT 完成（14B RSFT pipeline running）
11	- **D118 claim 降级**: "surpasses" → "approaches"（1.7B RSFT 0.5119 vs 8B SFT 0.5019, Δ=1.0pp, p=0.69）
12	- **D118 核心发现升级**: Variance compression 7-31× across scales（归入 C3）
13	- **D117**: 14B evidence tax=+0.03pp（零），4 尺度 tax curve 完整（含 RSFT tax 列）
14	- **D119**: D112 Method B bf16 ign_f1=0.5152, RSFT pipeline 可复现
15	- **Mechanistic analysis (plan_020)**: ✅ 完成——duplication regularization / truncation asymmetry / fair comparison residual
16	- **Deep error analysis (plan_021)**: ✅ 完成——truncation FN↓ / hallucinated FP↓ / duplicate↓
17	
18	| Scale | SFT mean (seeds) | RSFT mean (seeds) | Δ ign_f1 | Variance compression |
19	|-------|-------------------|--------------------|----------|---------------------|
20	| 1.7B | 0.4464 (3) | 0.5119 (3) | +6.55pp | **31×** (2.79→0.09pp) |
21	| 4B | 0.4358 (3) | 0.4482 (3, A) / 0.5152 (1, B) | +1.24 / +4.18pp | **7.5×** (3.80→0.51pp) |
22	| 8B | 0.5019 (3) | 0.5433 (3) | +4.14pp | **7.4×** (3.72→0.50pp) |
23	| 14B | 0.5507 (1) | 🔄 pipeline running | — | — |
24	
25	## 投稿目标
26	- **EMNLP 2026 Main** (ARR July cycle, ~July 15-25, **~57 天**)
27	
28	## 实验路线（3 层优先级）
29	
30	### Tier 1 — Main 必要条件
31	| 实验 | 状态 |
32	|------|------|
33	| D102 k=1 方法论修正 | ✅ |
34	| SFT 4B s43+s44+s42 reeval | ✅ D111 |
35	| GRPO bf16 G=4 clean control | ✅ D110/D113 |
36	| Random k=1 RSFT baseline | ✅ D109 |
37	| 8B RSFT 3-seed (s42/s43/s44) | ✅ D115/D120 |
38	| D112 RSFT from SFT s44 (bf16) | ✅ D119 |
39	| 14B SFT (第 4 尺度) | ✅ D117 |
40	| 1.7B RSFT 3-seed | ✅ |
41	| 14B RSFT pipeline | 🔄 Step 1 gen (3.8%, ETA ~18.5h, cuda:0+2) |
42	
43	### Tier 2 — 大幅加分
44	| 实验 | 状态 |
45	|------|------|
46	| Evidence tax mechanistic analysis | ✅ plan_020（⚠️ 缺 registry 记录，需补） |
47	| Deep error analysis | ✅ plan_021（⚠️ 缺 registry 记录，需补） |
48	| NLI model ablation | plan_010, 🔄 cuda:1 释放后启动 |
49	| Evidence tax 全 scale curve + RSFT 列 | 🔄 d112 no-evi eval (cuda:1, 97%) + 1.7B 2048 (cuda:3, 66%) |
50	| 14B RSFT eval + no-evidence | pending（14B gen 完成后） |
51	
52	### Tier 3 — 锦上添花
53	| 实验 | 状态 |
54	|------|------|
55	| CDR/GDA 跨领域 | P2（无 evidence 标注） |
56	| 第三模型家族 | pending |
57	
58	## 从 3.0 → 4.0 路径
59	| 里程碑 | 预期评分 | 状态 |
60	|--------|---------|------|
61	| Wave 1 + D112 + multi-seed | 3.0 → 3.5 | ✅ |
62	| + 14B 第 4 尺度档 | 3.5 → 3.75 | 🔄 SFT ✅, RSFT pipeline running |
63	| + Mechanistic + error analysis | → 3.75 | ✅ plan_020 + plan_021 |
64	| + NLI ablation + variance compression narrative | → 4.0 | 🔄 plan_010 启动中 |
65	
66	## GPU 分布
67	- cuda:0 + cuda:2: plan017_14b_rsft_generate (3.8%, ETA ~18.5h)
68	- cuda:1: d112_rsft_no_evidence_eval_r3 (97%, ~5min) → plan_010 NLI ablation
69	- cuda:3: plan019_1_7b_rsft_no_evidence_eval_2048 (66%, ~1h46m)
70	
71	## 近期任务
72	- [x] paper_framing.md D117-D120 更新
73	- [x] Paper Agent briefed on Claim 5 reframing patch
74	- [x] ROADMAP 贡献数量与 paper_framing.md 对齐（3 贡献）
75	- [ ] d112 no-evidence eval 完成 → 4B RSFT evidence tax
76	- [ ] plan_010 NLI ablation 启动 (cuda:1)
77	- [ ] 1.7B no-evidence 2048 完成 → 确认/排除 negative tax
78	- [ ] 14B RSFT pipeline 完成 → scaling table 最后一行
79	- [ ] plan_020/021 补 registry 记录 + decision
80	- [ ] experiment_plan.yaml 同步
81	- [ ] 重新提交论文审稿
82	
83	## 关键风险
84	- **1.7B evidence tax confounded**: 59.2% truncation@1024，2048 rerun 在跑
85	- **14B RSFT gen ETA 18.5h**: 比预期长，cuda:0+2 长期锁定
86	- **plan_020/021 可追溯性**: 分析数据在 paper_framing.md 但缺 registry/decision 记录
87	- **EDCR 缺人工验证**: plan_013 取消，用 per-relation 分析 + Limitations 缓解
88	
89	## 关键决策日志
90	
91	| ID | 日期 | 摘要 | 关联实验 |
92	|----|------|------|----------|
93	| D122 | 2026-05-19 | D122: Negative results audit 完成——16/19 RESOLVED, 1 | mvp2_eval_rsft_r2b_maxtok1536_r2 |
94	| D121 | 2026-05-19 | D121: 4B RSFT evidence tax = +0.94pp (near zero),  | d112_rsft_no_evidence_eval_r3, d112_rsft_s44_eval_bf16 |
95	| D120 | 2026-05-19 | D120: 8B RSFT 3-seed 确认 variance compression 7.4×， | d102_8b_rsft_k1_s43, plan019_8b_rsft_s44_eval |
96	| D119 | 2026-05-19 | D119: D112 bf16 eval ign_f1=0.5152 确认 Method B (RS | d112_rsft_s44_eval_bf16, d112_rsft_s44_eval |
97	| D118 | 2026-05-19 | D118: "1.7B RSFT surpasses 8B SFT" claim 降级为 "appr | plan019_8b_sft_s43_eval, plan019_1_7b_rsft_s44_r2_eval |
98	| D117 | 2026-05-19 | D117: 14B SFT evidence tax = 0.03pp（本质为零），完成 4 尺度  | plan017_14b_sft_eval_r2, plan017_14b_sft_no_evidence_eval_r2 |
99	| D116 | 2026-05-19 | D116: D112 结果无效（QLoRA confound），必须用 bf16 LoRA 重跑 s | d112_rsft_s44_eval, d112_rsft_s44_train |
100	| D115 | 2026-05-19 | D115: 8B RSFT s44 ign_f1=0.5451 确认 RSFT 跨 seed 稳健， | plan019_8b_rsft_s44_eval, eval_rsft_ced_s42 |
101	| D114 | 2026-05-19 | D114: 1.7B RSFT s43/s44 应使用 Method A（s42 SFT base） | plan019_1_7b_rsft_s43, plan019_1_7b_rsft_s44, d112_rsft_s44_ced_score |
102	| D113 | 2026-05-18 | D113: GRPO bf16 ckpt-100 为最优 checkpoint，ckpt-200 无 | grpo_bf16_g4_ckpt100_eval, grpo_bf16_g4_ckpt200_eval |
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
  "session_id": "bd67c934-a0d4-42da-9473-8ddc185c5800",
  "uuid": "5bb1b5a5-9e9b-4e08-a579-700ae4f65a7d",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/ROADMAP.md",
      "content": "# faith-evidence-ie — Research Dashboard\n\n> 最后更新: 2026-05-19 18:21 UTC | 更新原因: Fix contribution count: variance compression folded into C3, not separate 4th contribution\n\n## 核心方向\nFREIGE: LLM-based evidence-grounded DocRE 系统性研究。3 贡献：(1) RSFT+NLI 有效性 (2) Decoupling spectrum (3) Scale-dependent evidence tax + variance compression。详见 paper_framing.md。\n\n## 当前进展\n- **阶段**: 🚀 Research + 审稿并行（Round 1 = 3.0 Findings，目标 4.0 Main）\n- **Scaling table 完成度**: 4/4 尺度 SFT 完成，3/4 尺度 RSFT 完成（14B RSFT pipeline running）\n- **D118 claim 降级**: \"surpasses\" → \"approaches\"（1.7B RSFT 0.5119 vs 8B SFT 0.5019, Δ=1.0pp, p=0.69）\n- **D118 核心发现升级**: Variance compression 7-31× across scales（归入 C3）\n- **D117**: 14B evidence tax=+0.03pp（零），4 尺度 tax curve 完整（含 RSFT tax 列）\n- **D119**: D112 Method B bf16 ign_f1=0.5152, RSFT pipeline 可复现\n- **Mechanistic analysis (plan_020)**: ✅ 完成——duplication regularization / truncation asymmetry / fair comparison residual\n- **Deep error analysis (plan_021)**: ✅ 完成——truncation FN↓ / hallucinated FP↓ / duplicate↓\n\n| Scale | SFT mean (seeds) | RSFT mean (seeds) | Δ ign_f1 | Variance compression |\n|-------|-------------------|--------------------|----------|---------------------|\n| 1.7B | 0.4464 (3) | 0.5119 (3) | +6.55pp | **31×** (2.79→0.09pp) |\n| 4B | 0.4358 (3) | 0.4482 (3, A) / 0.5152 (1, B) | +1.24 / +4.18pp | **7.5×** (3.80→0.51pp) |\n| 8B | 0.5019 (3) | 0.5433 (3) | +4.14pp | **7.4×** (3.72→0.50pp) |\n| 14B | 0.5507 (1) | 🔄 pipeline running | — | — |\n\n## 投稿目标\n- **EMNLP 2026 Main** (ARR July cycle, ~July 15-25, **~57 天**)\n\n## 实验路线（3 层优先级）\n\n### Tier 1 — Main 必要条件\n| 实验 | 状态 |\n|------|------|\n| D102 k=1 方法论修正 | ✅ |\n| SFT 4B s43+s44+s42 reeval | ✅ D111 |\n| GRPO bf16 G=4 clean control | ✅ D110/D113 |\n| Random k=1 RSFT baseline | ✅ D109 |\n| 8B RSFT 3-seed (s42/s43/s44) | ✅ D115/D120 |\n| D112 RSFT from SFT s44 (bf16) | ✅ D119 |\n| 14B SFT (第 4 尺度) | ✅ D117 |\n| 1.7B RSFT 3-seed | ✅ |\n| 14B RSFT pipeline | 🔄 Step 1 gen (3.8%, ETA ~18.5h, cuda:0+2) |\n\n### Tier 2 — 大幅加分\n| 实验 | 状态 |\n|------|------|\n| Evidence tax mechanistic analysis | ✅ plan_020（⚠️ 缺 registry 记录，需补） |\n| Deep error analysis | ✅ plan_021（⚠️ 缺 registry 记录，需补） |\n| NLI model ablation | plan_010, 🔄 cuda:1 释放后启动 |\n| Evidence tax 全 scale curve + RSFT 列 | 🔄 d112 no-evi eval (cuda:1, 97%) + 1.7B 2048 (cuda:3, 66%) |\n| 14B RSFT eval + no-evidence | pending（14B gen 完成后） |\n\n### Tier 3 — 锦上添花\n| 实验 | 状态 |\n|------|------|\n| CDR/GDA 跨领域 | P2（无 evidence 标注） |\n| 第三模型家族 | pending |\n\n## 从 3.0 → 4.0 路径\n| 里程碑 | 预期评分 | 状态 |\n|--------|---------|------|\n| Wave 1 + D112 + multi-seed | 3.0 → 3.5 | ✅ |\n| + 14B 第 4 尺度档 | 3.5 → 3.75 | 🔄 SFT ✅, RSFT pipeline running |\n| + Mechanistic + error analysis | → 3.75 | ✅ plan_020 + plan_021 |\n| + NLI ablation + variance compression narrative | → 4.0 | 🔄 plan_010 启动中 |\n\n## GPU 分布\n- cuda:0 + cuda:2: plan017_14b_rsft_generate (3.8%, ETA ~18.5h)\n- cuda:1: d112_rsft_no_evidence_eval_r3 (97%, ~5min) → plan_010 NLI ablation\n- cuda:3: plan019_1_7b_rsft_no_evidence_eval_2048 (66%, ~1h46m)\n\n## 近期任务\n- [x] paper_framing.md D117-D120 更新\n- [x] Paper Agent briefed on Claim 5 reframing patch\n- [x] ROADMAP 贡献数量与 paper_framing.md 对齐（3 贡献）\n- [ ] d112 no-evidence eval 完成 → 4B RSFT evidence tax\n- [ ] plan_010 NLI ablation 启动 (cuda:1)\n- [ ] 1.7B no-evidence 2048 完成 → 确认/排除 negative tax\n- [ ] 14B RSFT pipeline 完成 → scaling table 最后一行\n- [ ] plan_020/021 补 registry 记录 + decision\n- [ ] experiment_plan.yaml 同步\n- [ ] 重新提交论文审稿\n\n## 关键风险\n- **1.7B evidence tax confounded**: 59.2% truncation@1024，2048 rerun 在跑\n- **14B RSFT gen ETA 18.5h**: 比预期长，cuda:0+2 长期锁定\n- **plan_020/021 可追溯性**: 分析数据在 paper_framing.md 但缺 registry/decision 记录\n- **EDCR 缺人工验证**: plan_013 取消，用 per-relation 分析 + Limitations 缓解\n\n## 关键决策日志\n\n| ID | 日期 | 摘要 | 关联实验 |\n|----|------|------|----------|\n| D122 | 2026-05-19 | D122: Negative results audit 完成——16/19 RESOLVED, 1 | mvp2_eval_rsft_r2b_maxtok1536_r2 |\n| D121 | 2026-05-19 | D121: 4B RSFT evidence tax = +0.94pp (near zero),  | d112_rsft_no_evidence_eval_r3, d112_rsft_s44_eval_bf16 |\n| D120 | 2026-05-19 | D120: 8B RSFT 3-seed 确认 variance compression 7.4×， | d102_8b_rsft_k1_s43, plan019_8b_rsft_s44_eval |\n| D119 | 2026-05-19 | D119: D112 bf16 eval ign_f1=0.5152 确认 Method B (RS | d112_rsft_s44_eval_bf16, d112_rsft_s44_eval |\n| D118 | 2026-05-19 | D118: \"1.7B RSFT surpasses 8B SFT\" claim 降级为 \"appr | plan019_8b_sft_s43_eval, plan019_1_7b_rsft_s44_r2_eval |\n| D117 | 2026-05-19 | D117: 14B SFT evidence tax = 0.03pp（本质为零），完成 4 尺度  | plan017_14b_sft_eval_r2, plan017_14b_sft_no_evidence_eval_r2 |\n| D116 | 2026-05-19 | D116: D112 结果无效（QLoRA confound），必须用 bf16 LoRA 重跑 s | d112_rsft_s44_eval, d112_rsft_s44_train |\n| D115 | 2026-05-19 | D115: 8B RSFT s44 ign_f1=0.5451 确认 RSFT 跨 seed 稳健， | plan019_8b_rsft_s44_eval, eval_rsft_ced_s42 |\n| D114 | 2026-05-19 | D114: 1.7B RSFT s43/s44 应使用 Method A（s42 SFT base） | plan019_1_7b_rsft_s43, plan019_1_7b_rsft_s44, d112_rsft_s44_ced_score |\n| D113 | 2026-05-18 | D113: GRPO bf16 ckpt-100 为最优 checkpoint，ckpt-200 无 | grpo_bf16_g4_ckpt100_eval, grpo_bf16_g4_ckpt200_eval |\n\n",
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

_source line 16_

Now I'll apply all 4 updates.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bd67c934-a0d4-42da-9473-8ddc185c5800",
  "uuid": "859db403-bf7d-4e8d-95e0-3abd69fc7699",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AU6rUNV9HTFtufnviGUskV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3667,
      "cache_read_input_tokens": 28533,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3667
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

_source line 17_

<details open><summary>🔧 Tool call — Edit · `toolu_01B7BLzf6ZqRFNaeFvwycNuC`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/ROADMAP.md",
  "old_string": "> 最后更新: 2026-05-19 18:21 UTC | 更新原因: Fix contribution count: variance compression folded into C3, not separate 4th contribution",
  "new_string": "> 最后更新: 2026-05-19 UTC | 更新原因: 1.7B 2048 eval 完成，evidence tax curve 全 scale 确认"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bd67c934-a0d4-42da-9473-8ddc185c5800",
  "uuid": "02275f88-d832-4608-b0b8-93af3f6990ee",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AU6rUNV9HTFtufnviGUskV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3667,
      "cache_read_input_tokens": 28533,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3667
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

_source line 18 · 2026-05-19T20:12:39.730Z_

<details><summary>↩ Tool result · `toolu_01B7BLzf6ZqRFNaeFvwycNuC`</summary>

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
  "session_id": "bd67c934-a0d4-42da-9473-8ddc185c5800",
  "uuid": "5892ef4e-93a0-49f8-aa73-eeb3b4dab23c",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/ROADMAP.md",
    "oldString": "> 最后更新: 2026-05-19 18:21 UTC | 更新原因: Fix contribution count: variance compression folded into C3, not separate 4th contribution",
    "newString": "> 最后更新: 2026-05-19 UTC | 更新原因: 1.7B 2048 eval 完成，evidence tax curve 全 scale 确认",
    "originalFile": "# faith-evidence-ie — Research Dashboard\n\n> 最后更新: 2026-05-19 18:21 UTC | 更新原因: Fix contribution count: variance compression folded into C3, not separate 4th contribution\n\n## 核心方向\nFREIGE: LLM-based evidence-grounded DocRE 系统性研究。3 贡献：(1) RSFT+NLI 有效性 (2) Decoupling spectrum (3) Scale-dependent evidence tax + variance compression。详见 paper_framing.md。\n\n## 当前进展\n- **阶段**: 🚀 Research + 审稿并行（Round 1 = 3.0 Findings，目标 4.0 Main）\n- **Scaling table 完成度**: 4/4 尺度 SFT 完成，3/4 尺度 RSFT 完成（14B RSFT pipeline running）\n- **D118 claim 降级**: \"surpasses\" → \"approaches\"（1.7B RSFT 0.5119 vs 8B SFT 0.5019, Δ=1.0pp, p=0.69）\n- **D118 核心发现升级**: Variance compression 7-31× across scales（归入 C3）\n- **D117**: 14B evidence tax=+0.03pp（零），4 尺度 tax curve 完整（含 RSFT tax 列）\n- **D119**: D112 Method B bf16 ign_f1=0.5152, RSFT pipeline 可复现\n- **Mechanistic analysis (plan_020)**: ✅ 完成——duplication regularization / truncation asymmetry / fair comparison residual\n- **Deep error analysis (plan_021)**: ✅ 完成——truncation FN↓ / hallucinated FP↓ / duplicate↓\n\n| Scale | SFT mean (seeds) | RSFT mean (seeds) | Δ ign_f1 | Variance compression |\n|-------|-------------------|--------------------|----------|---------------------|\n| 1.7B | 0.4464 (3) | 0.5119 (3) | +6.55pp | **31×** (2.79→0.09pp) |\n| 4B | 0.4358 (3) | 0.4482 (3, A) / 0.5152 (1, B) | +1.24 / +4.18pp | **7.5×** (3.80→0.51pp) |\n| 8B | 0.5019 (3) | 0.5433 (3) | +4.14pp | **7.4×** (3.72→0.50pp) |\n| 14B | 0.5507 (1) | 🔄 pipeline running | — | — |\n\n## 投稿目标\n- **EMNLP 2026 Main** (ARR July cycle, ~July 15-25, **~57 天**)\n\n## 实验路线（3 层优先级）\n\n### Tier 1 — Main 必要条件\n| 实验 | 状态 |\n|------|------|\n| D102 k=1 方法论修正 | ✅ |\n| SFT 4B s43+s44+s42 reeval | ✅ D111 |\n| GRPO bf16 G=4 clean control | ✅ D110/D113 |\n| Random k=1 RSFT baseline | ✅ D109 |\n| 8B RSFT 3-seed (s42/s43/s44) | ✅ D115/D120 |\n| D112 RSFT from SFT s44 (bf16) | ✅ D119 |\n| 14B SFT (第 4 尺度) | ✅ D117 |\n| 1.7B RSFT 3-seed | ✅ |\n| 14B RSFT pipeline | 🔄 Step 1 gen (3.8%, ETA ~18.5h, cuda:0+2) |\n\n### Tier 2 — 大幅加分\n| 实验 | 状态 |\n|------|------|\n| Evidence tax mechanistic analysis | ✅ plan_020（⚠️ 缺 registry 记录，需补） |\n| Deep error analysis | ✅ plan_021（⚠️ 缺 registry 记录，需补） |\n| NLI model ablation | plan_010, 🔄 cuda:1 释放后启动 |\n| Evidence tax 全 scale curve + RSFT 列 | 🔄 d112 no-evi eval (cuda:1, 97%) + 1.7B 2048 (cuda:3, 66%) |\n| 14B RSFT eval + no-evidence | pending（14B gen 完成后） |\n\n### Tier 3 — 锦上添花\n| 实验 | 状态 |\n|------|------|\n| CDR/GDA 跨领域 | P2（无 evidence 标注） |\n| 第三模型家族 | pending |\n\n## 从 3.0 → 4.0 路径\n| 里程碑 | 预期评分 | 状态 |\n|--------|---------|------|\n| Wave 1 + D112 + multi-seed | 3.0 → 3.5 | ✅ |\n| + 14B 第 4 尺度档 | 3.5 → 3.75 | 🔄 SFT ✅, RSFT pipeline running |\n| + Mechanistic + error analysis | → 3.75 | ✅ plan_020 + plan_021 |\n| + NLI ablation + variance compression narrative | → 4.0 | 🔄 plan_010 启动中 |\n\n## GPU 分布\n- cuda:0 + cuda:2: plan017_14b_rsft_generate (3.8%, ETA ~18.5h)\n- cuda:1: d112_rsft_no_evidence_eval_r3 (97%, ~5min) → plan_010 NLI ablation\n- cuda:3: plan019_1_7b_rsft_no_evidence_eval_2048 (66%, ~1h46m)\n\n## 近期任务\n- [x] paper_framing.md D117-D120 更新\n- [x] Paper Agent briefed on Claim 5 reframing patch\n- [x] ROADMAP 贡献数量与 paper_framing.md 对齐（3 贡献）\n- [ ] d112 no-evidence eval 完成 → 4B RSFT evidence tax\n- [ ] plan_010 NLI ablation 启动 (cuda:1)\n- [ ] 1.7B no-evidence 2048 完成 → 确认/排除 negative tax\n- [ ] 14B RSFT pipeline 完成 → scaling table 最后一行\n- [ ] plan_020/021 补 registry 记录 + decision\n- [ ] experiment_plan.yaml 同步\n- [ ] 重新提交论文审稿\n\n## 关键风险\n- **1.7B evidence tax confounded**: 59.2% truncation@1024，2048 rerun 在跑\n- **14B RSFT gen ETA 18.5h**: 比预期长，cuda:0+2 长期锁定\n- **plan_020/021 可追溯性**: 分析数据在 paper_framing.md 但缺 registry/decision 记录\n- **EDCR 缺人工验证**: plan_013 取消，用 per-relation 分析 + Limitations 缓解\n\n## 关键决策日志\n\n| ID | 日期 | 摘要 | 关联实验 |\n|----|------|------|----------|\n| D122 | 2026-05-19 | D122: Negative results audit 完成——16/19 RESOLVED, 1 | mvp2_eval_rsft_r2b_maxtok1536_r2 |\n| D121 | 2026-05-19 | D121: 4B RSFT evidence tax = +0.94pp (near zero),  | d112_rsft_no_evidence_eval_r3, d112_rsft_s44_eval_bf16 |\n| D120 | 2026-05-19 | D120: 8B RSFT 3-seed 确认 variance compression 7.4×， | d102_8b_rsft_k1_s43, plan019_8b_rsft_s44_eval |\n| D119 | 2026-05-19 | D119: D112 bf16 eval ign_f1=0.5152 确认 Method B (RS | d112_rsft_s44_eval_bf16, d112_rsft_s44_eval |\n| D118 | 2026-05-19 | D118: \"1.7B RSFT surpasses 8B SFT\" claim 降级为 \"appr | plan019_8b_sft_s43_eval, plan019_1_7b_rsft_s44_r2_eval |\n| D117 | 2026-05-19 | D117: 14B SFT evidence tax = 0.03pp（本质为零），完成 4 尺度  | plan017_14b_sft_eval_r2, plan017_14b_sft_no_evidence_eval_r2 |\n| D116 | 2026-05-19 | D116: D112 结果无效（QLoRA confound），必须用 bf16 LoRA 重跑 s | d112_rsft_s44_eval, d112_rsft_s44_train |\n| D115 | 2026-05-19 | D115: 8B RSFT s44 ign_f1=0.5451 确认 RSFT 跨 seed 稳健， | plan019_8b_rsft_s44_eval, eval_rsft_ced_s42 |\n| D114 | 2026-05-19 | D114: 1.7B RSFT s43/s44 应使用 Method A（s42 SFT base） | plan019_1_7b_rsft_s43, plan019_1_7b_rsft_s44, d112_rsft_s44_ced_score |\n| D113 | 2026-05-18 | D113: GRPO bf16 ckpt-100 为最优 checkpoint，ckpt-200 无 | grpo_bf16_g4_ckpt100_eval, grpo_bf16_g4_ckpt200_eval |\n\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 6,
        "newStart": 1,
        "newLines": 6,
        "lines": [
          " # faith-evidence-ie — Research Dashboard",
          " ",
          "-> 最后更新: 2026-05-19 18:21 UTC | 更新原因: Fix contribution count: variance compression folded into C3, not separate 4th contribution",
          "+> 最后更新: 2026-05-19 UTC | 更新原因: 1.7B 2048 eval 完成，evidence tax curve 全 scale 确认",
          " ",
          " ## 核心方向",
          " FREIGE: LLM-based evidence-grounded DocRE 系统性研究。3 贡献：(1) RSFT+NLI 有效性 (2) Decoupling spectrum (3) Scale-dependent evidence tax + variance compression。详见 paper_framing.md。"
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

_source line 19_

<details open><summary>🔧 Tool call — Edit · `toolu_01G3WhGxpkRtWdYB4XwjDKaL`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/ROADMAP.md",
  "old_string": "| Evidence tax 全 scale curve + RSFT 列 | 🔄 d112 no-evi eval (cuda:1, 97%) + 1.7B 2048 (cuda:3, 66%) |",
  "new_string": "| Evidence tax 全 scale curve + RSFT 列 | ✅ 完整 curve: 1.7B -7.75pp (confirmed real, not truncation artifact), 4B +0.94pp, 8B -0.78pp, 14B +0.03pp |"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bd67c934-a0d4-42da-9473-8ddc185c5800",
  "uuid": "4af87f0f-74e5-4323-8c42-ffc285fe640b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YCFUT6v71fx6BC27gcwW82",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 294,
      "cache_read_input_tokens": 32200,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 294
      },
      "output_tokens": 63,
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

_source line 20 · 2026-05-19T20:12:44.126Z_

<details><summary>↩ Tool result · `toolu_01G3WhGxpkRtWdYB4XwjDKaL`</summary>

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
  "session_id": "bd67c934-a0d4-42da-9473-8ddc185c5800",
  "uuid": "ce465281-0f85-47fa-9420-1d3816a9c66a",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/ROADMAP.md",
    "oldString": "| Evidence tax 全 scale curve + RSFT 列 | 🔄 d112 no-evi eval (cuda:1, 97%) + 1.7B 2048 (cuda:3, 66%) |",
    "newString": "| Evidence tax 全 scale curve + RSFT 列 | ✅ 完整 curve: 1.7B -7.75pp (confirmed real, not truncation artifact), 4B +0.94pp, 8B -0.78pp, 14B +0.03pp |",
    "originalFile": "# faith-evidence-ie — Research Dashboard\n\n> 最后更新: 2026-05-19 UTC | 更新原因: 1.7B 2048 eval 完成，evidence tax curve 全 scale 确认\n\n## 核心方向\nFREIGE: LLM-based evidence-grounded DocRE 系统性研究。3 贡献：(1) RSFT+NLI 有效性 (2) Decoupling spectrum (3) Scale-dependent evidence tax + variance compression。详见 paper_framing.md。\n\n## 当前进展\n- **阶段**: 🚀 Research + 审稿并行（Round 1 = 3.0 Findings，目标 4.0 Main）\n- **Scaling table 完成度**: 4/4 尺度 SFT 完成，3/4 尺度 RSFT 完成（14B RSFT pipeline running）\n- **D118 claim 降级**: \"surpasses\" → \"approaches\"（1.7B RSFT 0.5119 vs 8B SFT 0.5019, Δ=1.0pp, p=0.69）\n- **D118 核心发现升级**: Variance compression 7-31× across scales（归入 C3）\n- **D117**: 14B evidence tax=+0.03pp（零），4 尺度 tax curve 完整（含 RSFT tax 列）\n- **D119**: D112 Method B bf16 ign_f1=0.5152, RSFT pipeline 可复现\n- **Mechanistic analysis (plan_020)**: ✅ 完成——duplication regularization / truncation asymmetry / fair comparison residual\n- **Deep error analysis (plan_021)**: ✅ 完成——truncation FN↓ / hallucinated FP↓ / duplicate↓\n\n| Scale | SFT mean (seeds) | RSFT mean (seeds) | Δ ign_f1 | Variance compression |\n|-------|-------------------|--------------------|----------|---------------------|\n| 1.7B | 0.4464 (3) | 0.5119 (3) | +6.55pp | **31×** (2.79→0.09pp) |\n| 4B | 0.4358 (3) | 0.4482 (3, A) / 0.5152 (1, B) | +1.24 / +4.18pp | **7.5×** (3.80→0.51pp) |\n| 8B | 0.5019 (3) | 0.5433 (3) | +4.14pp | **7.4×** (3.72→0.50pp) |\n| 14B | 0.5507 (1) | 🔄 pipeline running | — | — |\n\n## 投稿目标\n- **EMNLP 2026 Main** (ARR July cycle, ~July 15-25, **~57 天**)\n\n## 实验路线（3 层优先级）\n\n### Tier 1 — Main 必要条件\n| 实验 | 状态 |\n|------|------|\n| D102 k=1 方法论修正 | ✅ |\n| SFT 4B s43+s44+s42 reeval | ✅ D111 |\n| GRPO bf16 G=4 clean control | ✅ D110/D113 |\n| Random k=1 RSFT baseline | ✅ D109 |\n| 8B RSFT 3-seed (s42/s43/s44) | ✅ D115/D120 |\n| D112 RSFT from SFT s44 (bf16) | ✅ D119 |\n| 14B SFT (第 4 尺度) | ✅ D117 |\n| 1.7B RSFT 3-seed | ✅ |\n| 14B RSFT pipeline | 🔄 Step 1 gen (3.8%, ETA ~18.5h, cuda:0+2) |\n\n### Tier 2 — 大幅加分\n| 实验 | 状态 |\n|------|------|\n| Evidence tax mechanistic analysis | ✅ plan_020（⚠️ 缺 registry 记录，需补） |\n| Deep error analysis | ✅ plan_021（⚠️ 缺 registry 记录，需补） |\n| NLI model ablation | plan_010, 🔄 cuda:1 释放后启动 |\n| Evidence tax 全 scale curve + RSFT 列 | 🔄 d112 no-evi eval (cuda:1, 97%) + 1.7B 2048 (cuda:3, 66%) |\n| 14B RSFT eval + no-evidence | pending（14B gen 完成后） |\n\n### Tier 3 — 锦上添花\n| 实验 | 状态 |\n|------|------|\n| CDR/GDA 跨领域 | P2（无 evidence 标注） |\n| 第三模型家族 | pending |\n\n## 从 3.0 → 4.0 路径\n| 里程碑 | 预期评分 | 状态 |\n|--------|---------|------|\n| Wave 1 + D112 + multi-seed | 3.0 → 3.5 | ✅ |\n| + 14B 第 4 尺度档 | 3.5 → 3.75 | 🔄 SFT ✅, RSFT pipeline running |\n| + Mechanistic + error analysis | → 3.75 | ✅ plan_020 + plan_021 |\n| + NLI ablation + variance compression narrative | → 4.0 | 🔄 plan_010 启动中 |\n\n## GPU 分布\n- cuda:0 + cuda:2: plan017_14b_rsft_generate (3.8%, ETA ~18.5h)\n- cuda:1: d112_rsft_no_evidence_eval_r3 (97%, ~5min) → plan_010 NLI ablation\n- cuda:3: plan019_1_7b_rsft_no_evidence_eval_2048 (66%, ~1h46m)\n\n## 近期任务\n- [x] paper_framing.md D117-D120 更新\n- [x] Paper Agent briefed on Claim 5 reframing patch\n- [x] ROADMAP 贡献数量与 paper_framing.md 对齐（3 贡献）\n- [ ] d112 no-evidence eval 完成 → 4B RSFT evidence tax\n- [ ] plan_010 NLI ablation 启动 (cuda:1)\n- [ ] 1.7B no-evidence 2048 完成 → 确认/排除 negative tax\n- [ ] 14B RSFT pipeline 完成 → scaling table 最后一行\n- [ ] plan_020/021 补 registry 记录 + decision\n- [ ] experiment_plan.yaml 同步\n- [ ] 重新提交论文审稿\n\n## 关键风险\n- **1.7B evidence tax confounded**: 59.2% truncation@1024，2048 rerun 在跑\n- **14B RSFT gen ETA 18.5h**: 比预期长，cuda:0+2 长期锁定\n- **plan_020/021 可追溯性**: 分析数据在 paper_framing.md 但缺 registry/decision 记录\n- **EDCR 缺人工验证**: plan_013 取消，用 per-relation 分析 + Limitations 缓解\n\n## 关键决策日志\n\n| ID | 日期 | 摘要 | 关联实验 |\n|----|------|------|----------|\n| D122 | 2026-05-19 | D122: Negative results audit 完成——16/19 RESOLVED, 1 | mvp2_eval_rsft_r2b_maxtok1536_r2 |\n| D121 | 2026-05-19 | D121: 4B RSFT evidence tax = +0.94pp (near zero),  | d112_rsft_no_evidence_eval_r3, d112_rsft_s44_eval_bf16 |\n| D120 | 2026-05-19 | D120: 8B RSFT 3-seed 确认 variance compression 7.4×， | d102_8b_rsft_k1_s43, plan019_8b_rsft_s44_eval |\n| D119 | 2026-05-19 | D119: D112 bf16 eval ign_f1=0.5152 确认 Method B (RS | d112_rsft_s44_eval_bf16, d112_rsft_s44_eval |\n| D118 | 2026-05-19 | D118: \"1.7B RSFT surpasses 8B SFT\" claim 降级为 \"appr | plan019_8b_sft_s43_eval, plan019_1_7b_rsft_s44_r2_eval |\n| D117 | 2026-05-19 | D117: 14B SFT evidence tax = 0.03pp（本质为零），完成 4 尺度  | plan017_14b_sft_eval_r2, plan017_14b_sft_no_evidence_eval_r2 |\n| D116 | 2026-05-19 | D116: D112 结果无效（QLoRA confound），必须用 bf16 LoRA 重跑 s | d112_rsft_s44_eval, d112_rsft_s44_train |\n| D115 | 2026-05-19 | D115: 8B RSFT s44 ign_f1=0.5451 确认 RSFT 跨 seed 稳健， | plan019_8b_rsft_s44_eval, eval_rsft_ced_s42 |\n| D114 | 2026-05-19 | D114: 1.7B RSFT s43/s44 应使用 Method A（s42 SFT base） | plan019_1_7b_rsft_s43, plan019_1_7b_rsft_s44, d112_rsft_s44_ced_score |\n| D113 | 2026-05-18 | D113: GRPO bf16 ckpt-100 为最优 checkpoint，ckpt-200 无 | grpo_bf16_g4_ckpt100_eval, grpo_bf16_g4_ckpt200_eval |\n\n",
    "structuredPatch": [
      {
        "oldStart": 46,
        "oldLines": 7,
        "newStart": 46,
        "newLines": 7,
        "lines": [
          " | Evidence tax mechanistic analysis | ✅ plan_020（⚠️ 缺 registry 记录，需补） |",
          " | Deep error analysis | ✅ plan_021（⚠️ 缺 registry 记录，需补） |",
          " | NLI model ablation | plan_010, 🔄 cuda:1 释放后启动 |",
          "-| Evidence tax 全 scale curve + RSFT 列 | 🔄 d112 no-evi eval (cuda:1, 97%) + 1.7B 2048 (cuda:3, 66%) |",
          "+| Evidence tax 全 scale curve + RSFT 列 | ✅ 完整 curve: 1.7B -7.75pp (confirmed real, not truncation artifact), 4B +0.94pp, 8B -0.78pp, 14B +0.03pp |",
          " | 14B RSFT eval + no-evidence | pending（14B gen 完成后） |",
          " ",
          " ### Tier 3 — 锦上添花"
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

_source line 21_

<details open><summary>🔧 Tool call — Edit · `toolu_01VD1iaY7hoFvk657V5ZSfDe`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/ROADMAP.md",
  "old_string": "## GPU 分布\n- cuda:0 + cuda:2: plan017_14b_rsft_generate (3.8%, ETA ~18.5h)\n- cuda:1: d112_rsft_no_evidence_eval_r3 (97%, ~5min) → plan_010 NLI ablation\n- cuda:3: plan019_1_7b_rsft_no_evidence_eval_2048 (66%, ~1h46m)",
  "new_string": "## GPU 分布\n- cuda:0 + cuda:2: plan017_14b_rsft_generate (running)\n- cuda:1: plan010_nli_large_ablation (running, Step 1 ~32%)\n- cuda:3: 空闲（plan019_1_7b_rsft_no_evidence_eval_2048 已完成）"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bd67c934-a0d4-42da-9473-8ddc185c5800",
  "uuid": "6a9cb74a-de7d-41f7-a538-29e9e2215e48",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KbaAp2mtyqebFDiNEJ3KHp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 319,
      "cache_read_input_tokens": 32494,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 319
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

_source line 22 · 2026-05-19T20:12:48.670Z_

<details><summary>↩ Tool result · reported error · `toolu_01VD1iaY7hoFvk657V5ZSfDe`</summary>

```text
&lt;tool_use_error>File has been modified since read, either by the user or by a linter. Read it again before attempting to write it.&lt;/tool_use_error>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "bd67c934-a0d4-42da-9473-8ddc185c5800",
  "uuid": "0e349856-a02b-42c2-93ed-4e52d4d15355",
  "tool_use_result": "Error: File has been modified since read, either by the user or by a linter. Read it again before attempting to write it."
}
```

</details>

---

### Assistant

_source line 23_

File was modified externally (D123 was added to the decision log). Let me re-read and apply remaining edits.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bd67c934-a0d4-42da-9473-8ddc185c5800",
  "uuid": "c889e37d-d0c1-42e2-a698-e3d0dc03cffb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M3gEjvNsYhPDiLjTRPdf8a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3651,
      "cache_read_input_tokens": 32813,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3651
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

### Tool call

_source line 24_

<details open><summary>🔧 Tool call — Edit · `toolu_01W1Qtto8cCKxwxuGk43Yq5g`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/ROADMAP.md",
  "old_string": "## GPU 分布\n- cuda:0 + cuda:2: plan017_14b_rsft_generate (3.8%, ETA ~18.5h)\n- cuda:1: d112_rsft_no_evidence_eval_r3 (97%, ~5min) → plan_010 NLI ablation\n- cuda:3: plan019_1_7b_rsft_no_evidence_eval_2048 (66%, ~1h46m)",
  "new_string": "## GPU 分布\n- cuda:0 + cuda:2: plan017_14b_rsft_generate (running)\n- cuda:1: plan010_nli_large_ablation (running, Step 1 ~32%)\n- cuda:3: 空闲（plan019_1_7b_rsft_no_evidence_eval_2048 已完成）"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bd67c934-a0d4-42da-9473-8ddc185c5800",
  "uuid": "38db6ad5-e7f8-4c8e-a30e-0c6b2869cd9d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M3gEjvNsYhPDiLjTRPdf8a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3651,
      "cache_read_input_tokens": 32813,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3651
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

_source line 25 · 2026-05-19T20:12:53.873Z_

<details><summary>↩ Tool result · `toolu_01W1Qtto8cCKxwxuGk43Yq5g`</summary>

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
  "session_id": "bd67c934-a0d4-42da-9473-8ddc185c5800",
  "uuid": "2d598dac-f8b4-4438-be53-e1c148c630f1",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/ROADMAP.md",
    "oldString": "## GPU 分布\n- cuda:0 + cuda:2: plan017_14b_rsft_generate (3.8%, ETA ~18.5h)\n- cuda:1: d112_rsft_no_evidence_eval_r3 (97%, ~5min) → plan_010 NLI ablation\n- cuda:3: plan019_1_7b_rsft_no_evidence_eval_2048 (66%, ~1h46m)",
    "newString": "## GPU 分布\n- cuda:0 + cuda:2: plan017_14b_rsft_generate (running)\n- cuda:1: plan010_nli_large_ablation (running, Step 1 ~32%)\n- cuda:3: 空闲（plan019_1_7b_rsft_no_evidence_eval_2048 已完成）",
    "originalFile": "# faith-evidence-ie — Research Dashboard\n\n> 最后更新: 2026-05-19 UTC | 更新原因: 1.7B 2048 eval 完成，evidence tax curve 全 scale 确认\n\n## 核心方向\nFREIGE: LLM-based evidence-grounded DocRE 系统性研究。3 贡献：(1) RSFT+NLI 有效性 (2) Decoupling spectrum (3) Scale-dependent evidence tax + variance compression。详见 paper_framing.md。\n\n## 当前进展\n- **阶段**: 🚀 Research + 审稿并行（Round 1 = 3.0 Findings，目标 4.0 Main）\n- **Scaling table 完成度**: 4/4 尺度 SFT 完成，3/4 尺度 RSFT 完成（14B RSFT pipeline running）\n- **D118 claim 降级**: \"surpasses\" → \"approaches\"（1.7B RSFT 0.5119 vs 8B SFT 0.5019, Δ=1.0pp, p=0.69）\n- **D118 核心发现升级**: Variance compression 7-31× across scales（归入 C3）\n- **D117**: 14B evidence tax=+0.03pp（零），4 尺度 tax curve 完整（含 RSFT tax 列）\n- **D119**: D112 Method B bf16 ign_f1=0.5152, RSFT pipeline 可复现\n- **Mechanistic analysis (plan_020)**: ✅ 完成——duplication regularization / truncation asymmetry / fair comparison residual\n- **Deep error analysis (plan_021)**: ✅ 完成——truncation FN↓ / hallucinated FP↓ / duplicate↓\n\n| Scale | SFT mean (seeds) | RSFT mean (seeds) | Δ ign_f1 | Variance compression |\n|-------|-------------------|--------------------|----------|---------------------|\n| 1.7B | 0.4464 (3) | 0.5119 (3) | +6.55pp | **31×** (2.79→0.09pp) |\n| 4B | 0.4358 (3) | 0.4482 (3, A) / 0.5152 (1, B) | +1.24 / +4.18pp | **7.5×** (3.80→0.51pp) |\n| 8B | 0.5019 (3) | 0.5433 (3) | +4.14pp | **7.4×** (3.72→0.50pp) |\n| 14B | 0.5507 (1) | 🔄 pipeline running | — | — |\n\n## 投稿目标\n- **EMNLP 2026 Main** (ARR July cycle, ~July 15-25, **~57 天**)\n\n## 实验路线（3 层优先级）\n\n### Tier 1 — Main 必要条件\n| 实验 | 状态 |\n|------|------|\n| D102 k=1 方法论修正 | ✅ |\n| SFT 4B s43+s44+s42 reeval | ✅ D111 |\n| GRPO bf16 G=4 clean control | ✅ D110/D113 |\n| Random k=1 RSFT baseline | ✅ D109 |\n| 8B RSFT 3-seed (s42/s43/s44) | ✅ D115/D120 |\n| D112 RSFT from SFT s44 (bf16) | ✅ D119 |\n| 14B SFT (第 4 尺度) | ✅ D117 |\n| 1.7B RSFT 3-seed | ✅ |\n| 14B RSFT pipeline | 🔄 Step 1 gen (3.8%, ETA ~18.5h, cuda:0+2) |\n\n### Tier 2 — 大幅加分\n| 实验 | 状态 |\n|------|------|\n| Evidence tax mechanistic analysis | ✅ plan_020（⚠️ 缺 registry 记录，需补） |\n| Deep error analysis | ✅ plan_021（⚠️ 缺 registry 记录，需补） |\n| NLI model ablation | plan_010, 🔄 cuda:1 释放后启动 |\n| Evidence tax 全 scale curve + RSFT 列 | ✅ 完整 curve: 1.7B -7.75pp (confirmed real, not truncation artifact), 4B +0.94pp, 8B -0.78pp, 14B +0.03pp |\n| 14B RSFT eval + no-evidence | pending（14B gen 完成后） |\n\n### Tier 3 — 锦上添花\n| 实验 | 状态 |\n|------|------|\n| CDR/GDA 跨领域 | P2（无 evidence 标注） |\n| 第三模型家族 | pending |\n\n## 从 3.0 → 4.0 路径\n| 里程碑 | 预期评分 | 状态 |\n|--------|---------|------|\n| Wave 1 + D112 + multi-seed | 3.0 → 3.5 | ✅ |\n| + 14B 第 4 尺度档 | 3.5 → 3.75 | 🔄 SFT ✅, RSFT pipeline running |\n| + Mechanistic + error analysis | → 3.75 | ✅ plan_020 + plan_021 |\n| + NLI ablation + variance compression narrative | → 4.0 | 🔄 plan_010 启动中 |\n\n## GPU 分布\n- cuda:0 + cuda:2: plan017_14b_rsft_generate (3.8%, ETA ~18.5h)\n- cuda:1: d112_rsft_no_evidence_eval_r3 (97%, ~5min) → plan_010 NLI ablation\n- cuda:3: plan019_1_7b_rsft_no_evidence_eval_2048 (66%, ~1h46m)\n\n## 近期任务\n- [x] paper_framing.md D117-D120 更新\n- [x] Paper Agent briefed on Claim 5 reframing patch\n- [x] ROADMAP 贡献数量与 paper_framing.md 对齐（3 贡献）\n- [ ] d112 no-evidence eval 完成 → 4B RSFT evidence tax\n- [ ] plan_010 NLI ablation 启动 (cuda:1)\n- [ ] 1.7B no-evidence 2048 完成 → 确认/排除 negative tax\n- [ ] 14B RSFT pipeline 完成 → scaling table 最后一行\n- [ ] plan_020/021 补 registry 记录 + decision\n- [ ] experiment_plan.yaml 同步\n- [ ] 重新提交论文审稿\n\n## 关键风险\n- **1.7B evidence tax confounded**: 59.2% truncation@1024，2048 rerun 在跑\n- **14B RSFT gen ETA 18.5h**: 比预期长，cuda:0+2 长期锁定\n- **plan_020/021 可追溯性**: 分析数据在 paper_framing.md 但缺 registry/decision 记录\n- **EDCR 缺人工验证**: plan_013 取消，用 per-relation 分析 + Limitations 缓解\n\n## 关键决策日志\n\n| ID | 日期 | 摘要 | 关联实验 |\n|----|------|------|----------|\n| D123 | 2026-05-19 | D123: 1.7B RSFT evidence tax = +7.75pp BENEFIT con | plan019_1_7b_rsft_no_evidence_eval_2048, plan019_1_7b_rsft_no_evidence_eval |\n| D122 | 2026-05-19 | D122: Negative results audit 完成——16/19 RESOLVED, 1 | mvp2_eval_rsft_r2b_maxtok1536_r2 |\n| D121 | 2026-05-19 | D121: 4B RSFT evidence tax = +0.94pp (near zero),  | d112_rsft_no_evidence_eval_r3, d112_rsft_s44_eval_bf16 |\n| D120 | 2026-05-19 | D120: 8B RSFT 3-seed 确认 variance compression 7.4×， | d102_8b_rsft_k1_s43, plan019_8b_rsft_s44_eval |\n| D119 | 2026-05-19 | D119: D112 bf16 eval ign_f1=0.5152 确认 Method B (RS | d112_rsft_s44_eval_bf16, d112_rsft_s44_eval |\n| D118 | 2026-05-19 | D118: \"1.7B RSFT surpasses 8B SFT\" claim 降级为 \"appr | plan019_8b_sft_s43_eval, plan019_1_7b_rsft_s44_r2_eval |\n| D117 | 2026-05-19 | D117: 14B SFT evidence tax = 0.03pp（本质为零），完成 4 尺度  | plan017_14b_sft_eval_r2, plan017_14b_sft_no_evidence_eval_r2 |\n| D116 | 2026-05-19 | D116: D112 结果无效（QLoRA confound），必须用 bf16 LoRA 重跑 s | d112_rsft_s44_eval, d112_rsft_s44_train |\n| D115 | 2026-05-19 | D115: 8B RSFT s44 ign_f1=0.5451 确认 RSFT 跨 seed 稳健， | plan019_8b_rsft_s44_eval, eval_rsft_ced_s42 |\n| D114 | 2026-05-19 | D114: 1.7B RSFT s43/s44 应使用 Method A（s42 SFT base） | plan019_1_7b_rsft_s43, plan019_1_7b_rsft_s44, d112_rsft_s44_ced_score |\n\n",
    "structuredPatch": [
      {
        "oldStart": 64,
        "oldLines": 9,
        "newStart": 64,
        "newLines": 9,
        "lines": [
          " | + NLI ablation + variance compression narrative | → 4.0 | 🔄 plan_010 启动中 |",
          " ",
          " ## GPU 分布",
          "-- cuda:0 + cuda:2: plan017_14b_rsft_generate (3.8%, ETA ~18.5h)",
          "-- cuda:1: d112_rsft_no_evidence_eval_r3 (97%, ~5min) → plan_010 NLI ablation",
          "-- cuda:3: plan019_1_7b_rsft_no_evidence_eval_2048 (66%, ~1h46m)",
          "+- cuda:0 + cuda:2: plan017_14b_rsft_generate (running)",
          "+- cuda:1: plan010_nli_large_ablation (running, Step 1 ~32%)",
          "+- cuda:3: 空闲（plan019_1_7b_rsft_no_evidence_eval_2048 已完成）",
          " ",
          " ## 近期任务",
          " - [x] paper_framing.md D117-D120 更新"
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

Now update the 近期任务 (check off 1.7B 2048 task) and 关键风险 (remove resolved 1.7B risk).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bd67c934-a0d4-42da-9473-8ddc185c5800",
  "uuid": "81376396-7486-45e9-80e5-8c6201867d9f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TFdWGoRxwW8UvZhEmwC8mX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 420,
      "cache_read_input_tokens": 36464,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 420
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

### Tool call

_source line 27_

<details open><summary>🔧 Tool call — Edit · `toolu_01EEjz8pXp9EE3qcezQB21VC`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/ROADMAP.md",
  "old_string": "- [ ] 1.7B no-evidence 2048 完成 → 确认/排除 negative tax",
  "new_string": "- [x] 1.7B no-evidence 2048 完成 → evidence tax = -7.75pp confirmed real"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bd67c934-a0d4-42da-9473-8ddc185c5800",
  "uuid": "516494e2-4e26-410b-8f66-dd33e21ac337",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TFdWGoRxwW8UvZhEmwC8mX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 420,
      "cache_read_input_tokens": 36464,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 420
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

_source line 28 · 2026-05-19T20:12:58.557Z_

<details><summary>↩ Tool result · `toolu_01EEjz8pXp9EE3qcezQB21VC`</summary>

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
  "session_id": "bd67c934-a0d4-42da-9473-8ddc185c5800",
  "uuid": "c35696cd-f119-4088-b2d6-e07c38af6292",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/ROADMAP.md",
    "oldString": "- [ ] 1.7B no-evidence 2048 完成 → 确认/排除 negative tax",
    "newString": "- [x] 1.7B no-evidence 2048 完成 → evidence tax = -7.75pp confirmed real",
    "originalFile": "# faith-evidence-ie — Research Dashboard\n\n> 最后更新: 2026-05-19 UTC | 更新原因: 1.7B 2048 eval 完成，evidence tax curve 全 scale 确认\n\n## 核心方向\nFREIGE: LLM-based evidence-grounded DocRE 系统性研究。3 贡献：(1) RSFT+NLI 有效性 (2) Decoupling spectrum (3) Scale-dependent evidence tax + variance compression。详见 paper_framing.md。\n\n## 当前进展\n- **阶段**: 🚀 Research + 审稿并行（Round 1 = 3.0 Findings，目标 4.0 Main）\n- **Scaling table 完成度**: 4/4 尺度 SFT 完成，3/4 尺度 RSFT 完成（14B RSFT pipeline running）\n- **D118 claim 降级**: \"surpasses\" → \"approaches\"（1.7B RSFT 0.5119 vs 8B SFT 0.5019, Δ=1.0pp, p=0.69）\n- **D118 核心发现升级**: Variance compression 7-31× across scales（归入 C3）\n- **D117**: 14B evidence tax=+0.03pp（零），4 尺度 tax curve 完整（含 RSFT tax 列）\n- **D119**: D112 Method B bf16 ign_f1=0.5152, RSFT pipeline 可复现\n- **Mechanistic analysis (plan_020)**: ✅ 完成——duplication regularization / truncation asymmetry / fair comparison residual\n- **Deep error analysis (plan_021)**: ✅ 完成——truncation FN↓ / hallucinated FP↓ / duplicate↓\n\n| Scale | SFT mean (seeds) | RSFT mean (seeds) | Δ ign_f1 | Variance compression |\n|-------|-------------------|--------------------|----------|---------------------|\n| 1.7B | 0.4464 (3) | 0.5119 (3) | +6.55pp | **31×** (2.79→0.09pp) |\n| 4B | 0.4358 (3) | 0.4482 (3, A) / 0.5152 (1, B) | +1.24 / +4.18pp | **7.5×** (3.80→0.51pp) |\n| 8B | 0.5019 (3) | 0.5433 (3) | +4.14pp | **7.4×** (3.72→0.50pp) |\n| 14B | 0.5507 (1) | 🔄 pipeline running | — | — |\n\n## 投稿目标\n- **EMNLP 2026 Main** (ARR July cycle, ~July 15-25, **~57 天**)\n\n## 实验路线（3 层优先级）\n\n### Tier 1 — Main 必要条件\n| 实验 | 状态 |\n|------|------|\n| D102 k=1 方法论修正 | ✅ |\n| SFT 4B s43+s44+s42 reeval | ✅ D111 |\n| GRPO bf16 G=4 clean control | ✅ D110/D113 |\n| Random k=1 RSFT baseline | ✅ D109 |\n| 8B RSFT 3-seed (s42/s43/s44) | ✅ D115/D120 |\n| D112 RSFT from SFT s44 (bf16) | ✅ D119 |\n| 14B SFT (第 4 尺度) | ✅ D117 |\n| 1.7B RSFT 3-seed | ✅ |\n| 14B RSFT pipeline | 🔄 Step 1 gen (3.8%, ETA ~18.5h, cuda:0+2) |\n\n### Tier 2 — 大幅加分\n| 实验 | 状态 |\n|------|------|\n| Evidence tax mechanistic analysis | ✅ plan_020（⚠️ 缺 registry 记录，需补） |\n| Deep error analysis | ✅ plan_021（⚠️ 缺 registry 记录，需补） |\n| NLI model ablation | plan_010, 🔄 cuda:1 释放后启动 |\n| Evidence tax 全 scale curve + RSFT 列 | ✅ 完整 curve: 1.7B -7.75pp (confirmed real, not truncation artifact), 4B +0.94pp, 8B -0.78pp, 14B +0.03pp |\n| 14B RSFT eval + no-evidence | pending（14B gen 完成后） |\n\n### Tier 3 — 锦上添花\n| 实验 | 状态 |\n|------|------|\n| CDR/GDA 跨领域 | P2（无 evidence 标注） |\n| 第三模型家族 | pending |\n\n## 从 3.0 → 4.0 路径\n| 里程碑 | 预期评分 | 状态 |\n|--------|---------|------|\n| Wave 1 + D112 + multi-seed | 3.0 → 3.5 | ✅ |\n| + 14B 第 4 尺度档 | 3.5 → 3.75 | 🔄 SFT ✅, RSFT pipeline running |\n| + Mechanistic + error analysis | → 3.75 | ✅ plan_020 + plan_021 |\n| + NLI ablation + variance compression narrative | → 4.0 | 🔄 plan_010 启动中 |\n\n## GPU 分布\n- cuda:0 + cuda:2: plan017_14b_rsft_generate (running)\n- cuda:1: plan010_nli_large_ablation (running, Step 1 ~32%)\n- cuda:3: 空闲（plan019_1_7b_rsft_no_evidence_eval_2048 已完成）\n\n## 近期任务\n- [x] paper_framing.md D117-D120 更新\n- [x] Paper Agent briefed on Claim 5 reframing patch\n- [x] ROADMAP 贡献数量与 paper_framing.md 对齐（3 贡献）\n- [ ] d112 no-evidence eval 完成 → 4B RSFT evidence tax\n- [ ] plan_010 NLI ablation 启动 (cuda:1)\n- [ ] 1.7B no-evidence 2048 完成 → 确认/排除 negative tax\n- [ ] 14B RSFT pipeline 完成 → scaling table 最后一行\n- [ ] plan_020/021 补 registry 记录 + decision\n- [ ] experiment_plan.yaml 同步\n- [ ] 重新提交论文审稿\n\n## 关键风险\n- **1.7B evidence tax confounded**: 59.2% truncation@1024，2048 rerun 在跑\n- **14B RSFT gen ETA 18.5h**: 比预期长，cuda:0+2 长期锁定\n- **plan_020/021 可追溯性**: 分析数据在 paper_framing.md 但缺 registry/decision 记录\n- **EDCR 缺人工验证**: plan_013 取消，用 per-relation 分析 + Limitations 缓解\n\n## 关键决策日志\n\n| ID | 日期 | 摘要 | 关联实验 |\n|----|------|------|----------|\n| D123 | 2026-05-19 | D123: 1.7B RSFT evidence tax = +7.75pp BENEFIT con | plan019_1_7b_rsft_no_evidence_eval_2048, plan019_1_7b_rsft_no_evidence_eval |\n| D122 | 2026-05-19 | D122: Negative results audit 完成——16/19 RESOLVED, 1 | mvp2_eval_rsft_r2b_maxtok1536_r2 |\n| D121 | 2026-05-19 | D121: 4B RSFT evidence tax = +0.94pp (near zero),  | d112_rsft_no_evidence_eval_r3, d112_rsft_s44_eval_bf16 |\n| D120 | 2026-05-19 | D120: 8B RSFT 3-seed 确认 variance compression 7.4×， | d102_8b_rsft_k1_s43, plan019_8b_rsft_s44_eval |\n| D119 | 2026-05-19 | D119: D112 bf16 eval ign_f1=0.5152 确认 Method B (RS | d112_rsft_s44_eval_bf16, d112_rsft_s44_eval |\n| D118 | 2026-05-19 | D118: \"1.7B RSFT surpasses 8B SFT\" claim 降级为 \"appr | plan019_8b_sft_s43_eval, plan019_1_7b_rsft_s44_r2_eval |\n| D117 | 2026-05-19 | D117: 14B SFT evidence tax = 0.03pp（本质为零），完成 4 尺度  | plan017_14b_sft_eval_r2, plan017_14b_sft_no_evidence_eval_r2 |\n| D116 | 2026-05-19 | D116: D112 结果无效（QLoRA confound），必须用 bf16 LoRA 重跑 s | d112_rsft_s44_eval, d112_rsft_s44_train |\n| D115 | 2026-05-19 | D115: 8B RSFT s44 ign_f1=0.5451 确认 RSFT 跨 seed 稳健， | plan019_8b_rsft_s44_eval, eval_rsft_ced_s42 |\n| D114 | 2026-05-19 | D114: 1.7B RSFT s43/s44 应使用 Method A（s42 SFT base） | plan019_1_7b_rsft_s43, plan019_1_7b_rsft_s44, d112_rsft_s44_ced_score |\n\n",
    "structuredPatch": [
      {
        "oldStart": 74,
        "oldLines": 7,
        "newStart": 74,
        "newLines": 7,
        "lines": [
          " - [x] ROADMAP 贡献数量与 paper_framing.md 对齐（3 贡献）",
          " - [ ] d112 no-evidence eval 完成 → 4B RSFT evidence tax",
          " - [ ] plan_010 NLI ablation 启动 (cuda:1)",
          "-- [ ] 1.7B no-evidence 2048 完成 → 确认/排除 negative tax",
          "+- [x] 1.7B no-evidence 2048 完成 → evidence tax = -7.75pp confirmed real",
          " - [ ] 14B RSFT pipeline 完成 → scaling table 最后一行",
          " - [ ] plan_020/021 补 registry 记录 + decision",
          " - [ ] experiment_plan.yaml 同步"
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

_source line 29_

<details open><summary>🔧 Tool call — Edit · `toolu_01Hf2xgxB7HoiHd6QvoVfocL`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/ROADMAP.md",
  "old_string": "- **1.7B evidence tax confounded**: 59.2% truncation@1024，2048 rerun 在跑",
  "new_string": "- ~~**1.7B evidence tax confounded**~~: ✅ 2048 rerun 确认 -7.75pp 是真实效应，非截断 artifact"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bd67c934-a0d4-42da-9473-8ddc185c5800",
  "uuid": "5190808c-5b69-498e-ac19-a6e15252fd06",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H7b4t5tM8VQHmmK3F6Bkg6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 290,
      "cache_read_input_tokens": 36884,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 290
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

_source line 30 · 2026-05-19T20:13:02.720Z_

<details><summary>↩ Tool result · `toolu_01Hf2xgxB7HoiHd6QvoVfocL`</summary>

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
  "session_id": "bd67c934-a0d4-42da-9473-8ddc185c5800",
  "uuid": "df33cbf9-2566-4668-ada3-e88b54f12818",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/ROADMAP.md",
    "oldString": "- **1.7B evidence tax confounded**: 59.2% truncation@1024，2048 rerun 在跑",
    "newString": "- ~~**1.7B evidence tax confounded**~~: ✅ 2048 rerun 确认 -7.75pp 是真实效应，非截断 artifact",
    "originalFile": "# faith-evidence-ie — Research Dashboard\n\n> 最后更新: 2026-05-19 UTC | 更新原因: 1.7B 2048 eval 完成，evidence tax curve 全 scale 确认\n\n## 核心方向\nFREIGE: LLM-based evidence-grounded DocRE 系统性研究。3 贡献：(1) RSFT+NLI 有效性 (2) Decoupling spectrum (3) Scale-dependent evidence tax + variance compression。详见 paper_framing.md。\n\n## 当前进展\n- **阶段**: 🚀 Research + 审稿并行（Round 1 = 3.0 Findings，目标 4.0 Main）\n- **Scaling table 完成度**: 4/4 尺度 SFT 完成，3/4 尺度 RSFT 完成（14B RSFT pipeline running）\n- **D118 claim 降级**: \"surpasses\" → \"approaches\"（1.7B RSFT 0.5119 vs 8B SFT 0.5019, Δ=1.0pp, p=0.69）\n- **D118 核心发现升级**: Variance compression 7-31× across scales（归入 C3）\n- **D117**: 14B evidence tax=+0.03pp（零），4 尺度 tax curve 完整（含 RSFT tax 列）\n- **D119**: D112 Method B bf16 ign_f1=0.5152, RSFT pipeline 可复现\n- **Mechanistic analysis (plan_020)**: ✅ 完成——duplication regularization / truncation asymmetry / fair comparison residual\n- **Deep error analysis (plan_021)**: ✅ 完成——truncation FN↓ / hallucinated FP↓ / duplicate↓\n\n| Scale | SFT mean (seeds) | RSFT mean (seeds) | Δ ign_f1 | Variance compression |\n|-------|-------------------|--------------------|----------|---------------------|\n| 1.7B | 0.4464 (3) | 0.5119 (3) | +6.55pp | **31×** (2.79→0.09pp) |\n| 4B | 0.4358 (3) | 0.4482 (3, A) / 0.5152 (1, B) | +1.24 / +4.18pp | **7.5×** (3.80→0.51pp) |\n| 8B | 0.5019 (3) | 0.5433 (3) | +4.14pp | **7.4×** (3.72→0.50pp) |\n| 14B | 0.5507 (1) | 🔄 pipeline running | — | — |\n\n## 投稿目标\n- **EMNLP 2026 Main** (ARR July cycle, ~July 15-25, **~57 天**)\n\n## 实验路线（3 层优先级）\n\n### Tier 1 — Main 必要条件\n| 实验 | 状态 |\n|------|------|\n| D102 k=1 方法论修正 | ✅ |\n| SFT 4B s43+s44+s42 reeval | ✅ D111 |\n| GRPO bf16 G=4 clean control | ✅ D110/D113 |\n| Random k=1 RSFT baseline | ✅ D109 |\n| 8B RSFT 3-seed (s42/s43/s44) | ✅ D115/D120 |\n| D112 RSFT from SFT s44 (bf16) | ✅ D119 |\n| 14B SFT (第 4 尺度) | ✅ D117 |\n| 1.7B RSFT 3-seed | ✅ |\n| 14B RSFT pipeline | 🔄 Step 1 gen (3.8%, ETA ~18.5h, cuda:0+2) |\n\n### Tier 2 — 大幅加分\n| 实验 | 状态 |\n|------|------|\n| Evidence tax mechanistic analysis | ✅ plan_020（⚠️ 缺 registry 记录，需补） |\n| Deep error analysis | ✅ plan_021（⚠️ 缺 registry 记录，需补） |\n| NLI model ablation | plan_010, 🔄 cuda:1 释放后启动 |\n| Evidence tax 全 scale curve + RSFT 列 | ✅ 完整 curve: 1.7B -7.75pp (confirmed real, not truncation artifact), 4B +0.94pp, 8B -0.78pp, 14B +0.03pp |\n| 14B RSFT eval + no-evidence | pending（14B gen 完成后） |\n\n### Tier 3 — 锦上添花\n| 实验 | 状态 |\n|------|------|\n| CDR/GDA 跨领域 | P2（无 evidence 标注） |\n| 第三模型家族 | pending |\n\n## 从 3.0 → 4.0 路径\n| 里程碑 | 预期评分 | 状态 |\n|--------|---------|------|\n| Wave 1 + D112 + multi-seed | 3.0 → 3.5 | ✅ |\n| + 14B 第 4 尺度档 | 3.5 → 3.75 | 🔄 SFT ✅, RSFT pipeline running |\n| + Mechanistic + error analysis | → 3.75 | ✅ plan_020 + plan_021 |\n| + NLI ablation + variance compression narrative | → 4.0 | 🔄 plan_010 启动中 |\n\n## GPU 分布\n- cuda:0 + cuda:2: plan017_14b_rsft_generate (running)\n- cuda:1: plan010_nli_large_ablation (running, Step 1 ~32%)\n- cuda:3: 空闲（plan019_1_7b_rsft_no_evidence_eval_2048 已完成）\n\n## 近期任务\n- [x] paper_framing.md D117-D120 更新\n- [x] Paper Agent briefed on Claim 5 reframing patch\n- [x] ROADMAP 贡献数量与 paper_framing.md 对齐（3 贡献）\n- [ ] d112 no-evidence eval 完成 → 4B RSFT evidence tax\n- [ ] plan_010 NLI ablation 启动 (cuda:1)\n- [x] 1.7B no-evidence 2048 完成 → evidence tax = -7.75pp confirmed real\n- [ ] 14B RSFT pipeline 完成 → scaling table 最后一行\n- [ ] plan_020/021 补 registry 记录 + decision\n- [ ] experiment_plan.yaml 同步\n- [ ] 重新提交论文审稿\n\n## 关键风险\n- **1.7B evidence tax confounded**: 59.2% truncation@1024，2048 rerun 在跑\n- **14B RSFT gen ETA 18.5h**: 比预期长，cuda:0+2 长期锁定\n- **plan_020/021 可追溯性**: 分析数据在 paper_framing.md 但缺 registry/decision 记录\n- **EDCR 缺人工验证**: plan_013 取消，用 per-relation 分析 + Limitations 缓解\n\n## 关键决策日志\n\n| ID | 日期 | 摘要 | 关联实验 |\n|----|------|------|----------|\n| D123 | 2026-05-19 | D123: 1.7B RSFT evidence tax = +7.75pp BENEFIT con | plan019_1_7b_rsft_no_evidence_eval_2048, plan019_1_7b_rsft_no_evidence_eval |\n| D122 | 2026-05-19 | D122: Negative results audit 完成——16/19 RESOLVED, 1 | mvp2_eval_rsft_r2b_maxtok1536_r2 |\n| D121 | 2026-05-19 | D121: 4B RSFT evidence tax = +0.94pp (near zero),  | d112_rsft_no_evidence_eval_r3, d112_rsft_s44_eval_bf16 |\n| D120 | 2026-05-19 | D120: 8B RSFT 3-seed 确认 variance compression 7.4×， | d102_8b_rsft_k1_s43, plan019_8b_rsft_s44_eval |\n| D119 | 2026-05-19 | D119: D112 bf16 eval ign_f1=0.5152 确认 Method B (RS | d112_rsft_s44_eval_bf16, d112_rsft_s44_eval |\n| D118 | 2026-05-19 | D118: \"1.7B RSFT surpasses 8B SFT\" claim 降级为 \"appr | plan019_8b_sft_s43_eval, plan019_1_7b_rsft_s44_r2_eval |\n| D117 | 2026-05-19 | D117: 14B SFT evidence tax = 0.03pp（本质为零），完成 4 尺度  | plan017_14b_sft_eval_r2, plan017_14b_sft_no_evidence_eval_r2 |\n| D116 | 2026-05-19 | D116: D112 结果无效（QLoRA confound），必须用 bf16 LoRA 重跑 s | d112_rsft_s44_eval, d112_rsft_s44_train |\n| D115 | 2026-05-19 | D115: 8B RSFT s44 ign_f1=0.5451 确认 RSFT 跨 seed 稳健， | plan019_8b_rsft_s44_eval, eval_rsft_ced_s42 |\n| D114 | 2026-05-19 | D114: 1.7B RSFT s43/s44 应使用 Method A（s42 SFT base） | plan019_1_7b_rsft_s43, plan019_1_7b_rsft_s44, d112_rsft_s44_ced_score |\n\n",
    "structuredPatch": [
      {
        "oldStart": 81,
        "oldLines": 7,
        "newStart": 81,
        "newLines": 7,
        "lines": [
          " - [ ] 重新提交论文审稿",
          " ",
          " ## 关键风险",
          "-- **1.7B evidence tax confounded**: 59.2% truncation@1024，2048 rerun 在跑",
          "+- ~~**1.7B evidence tax confounded**~~: ✅ 2048 rerun 确认 -7.75pp 是真实效应，非截断 artifact",
          " - **14B RSFT gen ETA 18.5h**: 比预期长，cuda:0+2 长期锁定",
          " - **plan_020/021 可追溯性**: 分析数据在 paper_framing.md 但缺 registry/decision 记录",
          " - **EDCR 缺人工验证**: plan_013 取消，用 per-relation 分析 + Limitations 缓解"
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

_source line 31_

Also update the NLI ablation status in Tier 2 since it's now running.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bd67c934-a0d4-42da-9473-8ddc185c5800",
  "uuid": "d460ace8-8e11-4f92-b0c0-95434fa72336",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015NDeYAdqhXGL6S4x5hzTeg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 558,
      "cache_read_input_tokens": 36884,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 558
      },
      "output_tokens": 1,
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

_source line 32_

<details open><summary>🔧 Tool call — Edit · `toolu_01JY5TytchaYNNB59vvtb2KQ`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/ROADMAP.md",
  "old_string": "| NLI model ablation | plan_010, 🔄 cuda:1 释放后启动 |",
  "new_string": "| NLI model ablation | 🔄 plan_010, cuda:1 running (Step 1 ~32%) |"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bd67c934-a0d4-42da-9473-8ddc185c5800",
  "uuid": "c8ebc9b0-f11f-4f7a-a753-97b9b6d6751a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015NDeYAdqhXGL6S4x5hzTeg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 558,
      "cache_read_input_tokens": 36884,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 558
      },
      "output_tokens": 1,
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

_source line 33 · 2026-05-19T20:13:06.616Z_

<details><summary>↩ Tool result · `toolu_01JY5TytchaYNNB59vvtb2KQ`</summary>

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
  "session_id": "bd67c934-a0d4-42da-9473-8ddc185c5800",
  "uuid": "ad508554-29f8-4512-8118-c64126ebcebd",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/ROADMAP.md",
    "oldString": "| NLI model ablation | plan_010, 🔄 cuda:1 释放后启动 |",
    "newString": "| NLI model ablation | 🔄 plan_010, cuda:1 running (Step 1 ~32%) |",
    "originalFile": "# faith-evidence-ie — Research Dashboard\n\n> 最后更新: 2026-05-19 UTC | 更新原因: 1.7B 2048 eval 完成，evidence tax curve 全 scale 确认\n\n## 核心方向\nFREIGE: LLM-based evidence-grounded DocRE 系统性研究。3 贡献：(1) RSFT+NLI 有效性 (2) Decoupling spectrum (3) Scale-dependent evidence tax + variance compression。详见 paper_framing.md。\n\n## 当前进展\n- **阶段**: 🚀 Research + 审稿并行（Round 1 = 3.0 Findings，目标 4.0 Main）\n- **Scaling table 完成度**: 4/4 尺度 SFT 完成，3/4 尺度 RSFT 完成（14B RSFT pipeline running）\n- **D118 claim 降级**: \"surpasses\" → \"approaches\"（1.7B RSFT 0.5119 vs 8B SFT 0.5019, Δ=1.0pp, p=0.69）\n- **D118 核心发现升级**: Variance compression 7-31× across scales（归入 C3）\n- **D117**: 14B evidence tax=+0.03pp（零），4 尺度 tax curve 完整（含 RSFT tax 列）\n- **D119**: D112 Method B bf16 ign_f1=0.5152, RSFT pipeline 可复现\n- **Mechanistic analysis (plan_020)**: ✅ 完成——duplication regularization / truncation asymmetry / fair comparison residual\n- **Deep error analysis (plan_021)**: ✅ 完成——truncation FN↓ / hallucinated FP↓ / duplicate↓\n\n| Scale | SFT mean (seeds) | RSFT mean (seeds) | Δ ign_f1 | Variance compression |\n|-------|-------------------|--------------------|----------|---------------------|\n| 1.7B | 0.4464 (3) | 0.5119 (3) | +6.55pp | **31×** (2.79→0.09pp) |\n| 4B | 0.4358 (3) | 0.4482 (3, A) / 0.5152 (1, B) | +1.24 / +4.18pp | **7.5×** (3.80→0.51pp) |\n| 8B | 0.5019 (3) | 0.5433 (3) | +4.14pp | **7.4×** (3.72→0.50pp) |\n| 14B | 0.5507 (1) | 🔄 pipeline running | — | — |\n\n## 投稿目标\n- **EMNLP 2026 Main** (ARR July cycle, ~July 15-25, **~57 天**)\n\n## 实验路线（3 层优先级）\n\n### Tier 1 — Main 必要条件\n| 实验 | 状态 |\n|------|------|\n| D102 k=1 方法论修正 | ✅ |\n| SFT 4B s43+s44+s42 reeval | ✅ D111 |\n| GRPO bf16 G=4 clean control | ✅ D110/D113 |\n| Random k=1 RSFT baseline | ✅ D109 |\n| 8B RSFT 3-seed (s42/s43/s44) | ✅ D115/D120 |\n| D112 RSFT from SFT s44 (bf16) | ✅ D119 |\n| 14B SFT (第 4 尺度) | ✅ D117 |\n| 1.7B RSFT 3-seed | ✅ |\n| 14B RSFT pipeline | 🔄 Step 1 gen (3.8%, ETA ~18.5h, cuda:0+2) |\n\n### Tier 2 — 大幅加分\n| 实验 | 状态 |\n|------|------|\n| Evidence tax mechanistic analysis | ✅ plan_020（⚠️ 缺 registry 记录，需补） |\n| Deep error analysis | ✅ plan_021（⚠️ 缺 registry 记录，需补） |\n| NLI model ablation | plan_010, 🔄 cuda:1 释放后启动 |\n| Evidence tax 全 scale curve + RSFT 列 | ✅ 完整 curve: 1.7B -7.75pp (confirmed real, not truncation artifact), 4B +0.94pp, 8B -0.78pp, 14B +0.03pp |\n| 14B RSFT eval + no-evidence | pending（14B gen 完成后） |\n\n### Tier 3 — 锦上添花\n| 实验 | 状态 |\n|------|------|\n| CDR/GDA 跨领域 | P2（无 evidence 标注） |\n| 第三模型家族 | pending |\n\n## 从 3.0 → 4.0 路径\n| 里程碑 | 预期评分 | 状态 |\n|--------|---------|------|\n| Wave 1 + D112 + multi-seed | 3.0 → 3.5 | ✅ |\n| + 14B 第 4 尺度档 | 3.5 → 3.75 | 🔄 SFT ✅, RSFT pipeline running |\n| + Mechanistic + error analysis | → 3.75 | ✅ plan_020 + plan_021 |\n| + NLI ablation + variance compression narrative | → 4.0 | 🔄 plan_010 启动中 |\n\n## GPU 分布\n- cuda:0 + cuda:2: plan017_14b_rsft_generate (running)\n- cuda:1: plan010_nli_large_ablation (running, Step 1 ~32%)\n- cuda:3: 空闲（plan019_1_7b_rsft_no_evidence_eval_2048 已完成）\n\n## 近期任务\n- [x] paper_framing.md D117-D120 更新\n- [x] Paper Agent briefed on Claim 5 reframing patch\n- [x] ROADMAP 贡献数量与 paper_framing.md 对齐（3 贡献）\n- [ ] d112 no-evidence eval 完成 → 4B RSFT evidence tax\n- [ ] plan_010 NLI ablation 启动 (cuda:1)\n- [x] 1.7B no-evidence 2048 完成 → evidence tax = -7.75pp confirmed real\n- [ ] 14B RSFT pipeline 完成 → scaling table 最后一行\n- [ ] plan_020/021 补 registry 记录 + decision\n- [ ] experiment_plan.yaml 同步\n- [ ] 重新提交论文审稿\n\n## 关键风险\n- ~~**1.7B evidence tax confounded**~~: ✅ 2048 rerun 确认 -7.75pp 是真实效应，非截断 artifact\n- **14B RSFT gen ETA 18.5h**: 比预期长，cuda:0+2 长期锁定\n- **plan_020/021 可追溯性**: 分析数据在 paper_framing.md 但缺 registry/decision 记录\n- **EDCR 缺人工验证**: plan_013 取消，用 per-relation 分析 + Limitations 缓解\n\n## 关键决策日志\n\n| ID | 日期 | 摘要 | 关联实验 |\n|----|------|------|----------|\n| D123 | 2026-05-19 | D123: 1.7B RSFT evidence tax = +7.75pp BENEFIT con | plan019_1_7b_rsft_no_evidence_eval_2048, plan019_1_7b_rsft_no_evidence_eval |\n| D122 | 2026-05-19 | D122: Negative results audit 完成——16/19 RESOLVED, 1 | mvp2_eval_rsft_r2b_maxtok1536_r2 |\n| D121 | 2026-05-19 | D121: 4B RSFT evidence tax = +0.94pp (near zero),  | d112_rsft_no_evidence_eval_r3, d112_rsft_s44_eval_bf16 |\n| D120 | 2026-05-19 | D120: 8B RSFT 3-seed 确认 variance compression 7.4×， | d102_8b_rsft_k1_s43, plan019_8b_rsft_s44_eval |\n| D119 | 2026-05-19 | D119: D112 bf16 eval ign_f1=0.5152 确认 Method B (RS | d112_rsft_s44_eval_bf16, d112_rsft_s44_eval |\n| D118 | 2026-05-19 | D118: \"1.7B RSFT surpasses 8B SFT\" claim 降级为 \"appr | plan019_8b_sft_s43_eval, plan019_1_7b_rsft_s44_r2_eval |\n| D117 | 2026-05-19 | D117: 14B SFT evidence tax = 0.03pp（本质为零），完成 4 尺度  | plan017_14b_sft_eval_r2, plan017_14b_sft_no_evidence_eval_r2 |\n| D116 | 2026-05-19 | D116: D112 结果无效（QLoRA confound），必须用 bf16 LoRA 重跑 s | d112_rsft_s44_eval, d112_rsft_s44_train |\n| D115 | 2026-05-19 | D115: 8B RSFT s44 ign_f1=0.5451 确认 RSFT 跨 seed 稳健， | plan019_8b_rsft_s44_eval, eval_rsft_ced_s42 |\n| D114 | 2026-05-19 | D114: 1.7B RSFT s43/s44 应使用 Method A（s42 SFT base） | plan019_1_7b_rsft_s43, plan019_1_7b_rsft_s44, d112_rsft_s44_ced_score |\n\n",
    "structuredPatch": [
      {
        "oldStart": 45,
        "oldLines": 7,
        "newStart": 45,
        "newLines": 7,
        "lines": [
          " |------|------|",
          " | Evidence tax mechanistic analysis | ✅ plan_020（⚠️ 缺 registry 记录，需补） |",
          " | Deep error analysis | ✅ plan_021（⚠️ 缺 registry 记录，需补） |",
          "-| NLI model ablation | plan_010, 🔄 cuda:1 释放后启动 |",
          "+| NLI model ablation | 🔄 plan_010, cuda:1 running (Step 1 ~32%) |",
          " | Evidence tax 全 scale curve + RSFT 列 | ✅ 完整 curve: 1.7B -7.75pp (confirmed real, not truncation artifact), 4B +0.94pp, 8B -0.78pp, 14B +0.03pp |",
          " | 14B RSFT eval + no-evidence | pending（14B gen 完成后） |",
          " "
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

_source line 34_

ROADMAP.md 已更新，4 处改动：

1. **Tier 2** "Evidence tax 全 scale curve + RSFT 列" → ✅，附完整 curve 数据
2. **GPU 分布** 更新为当前实际状态（cuda:3 空闲，cuda:1 NLI ablation running）
3. **近期任务** 1.7B 2048 项打勾，标注确认结论
4. **关键风险** 1.7B evidence tax confounded 标记已解决（-7.75pp confirmed real）

附带更新了 NLI ablation 状态为 running (Step 1 ~32%)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "bd67c934-a0d4-42da-9473-8ddc185c5800",
  "uuid": "f141c50b-2086-440c-998c-69dd7a684119",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vk27g3kpwQR69jn7ysUgpR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 272,
      "cache_read_input_tokens": 37442,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 272
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

_source line 35_

ROADMAP.md 已更新，4 处改动：

1. **Tier 2** "Evidence tax 全 scale curve + RSFT 列" → ✅，附完整 curve 数据
2. **GPU 分布** 更新为当前实际状态（cuda:3 空闲，cuda:1 NLI ablation running）
3. **近期任务** 1.7B 2048 项打勾，标注确认结论
4. **关键风险** 1.7B evidence tax confounded 标记已解决（-7.75pp confirmed real）

附带更新了 NLI ablation 状态为 running (Step 1 ~32%)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 59976,
  "duration_api_ms": 61626,
  "num_turns": 12,
  "stop_reason": "end_turn",
  "session_id": "bd67c934-a0d4-42da-9473-8ddc185c5800",
  "total_cost_usd": 0.40830975,
  "usage": {
    "input_tokens": 17,
    "cache_creation_input_tokens": 26163,
    "cache_read_input_tokens": 334770,
    "output_tokens": 3020,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 26163,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 184,
        "cache_read_input_tokens": 37442,
        "cache_creation_input_tokens": 272,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 272
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1701,
      "outputTokens": 24,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.0018210000000000001,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 17,
      "outputTokens": 3020,
      "cacheReadInputTokens": 334770,
      "cacheCreationInputTokens": 26163,
      "webSearchRequests": 0,
      "costUSD": 0.40648875,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "d858919a-41b0-47c8-aace-be1e56e6d095"
}
```

</details>

---
