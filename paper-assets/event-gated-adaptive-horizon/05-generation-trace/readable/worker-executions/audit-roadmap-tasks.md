# audit roadmap tasks

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 44
- **Recorded user turns:** 0
- **Tool calls:** 15
- **Original source:** `logs/workers/worker_audit_roadmap_tasks_20260525T134553.log`
- **Structured JSON:** [`f757c2abddfdc4a4a359.json`](../../sessions/f7/f757c2abddfdc4a4a359.json)

## Before a recorded user message

44 recorded events

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
  "session_id": "72aab3fa-ba3f-48a9-9029-1cec279461d0",
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
  "uuid": "443d68b9-6ffc-42bd-8358-6ed6b29cfbff",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon/memory/"
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
    "resetsAt": 1779734400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "4c9b93bf-6665-49c6-8d23-6e15b351250f",
  "session_id": "72aab3fa-ba3f-48a9-9029-1cec279461d0"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the ROADMAP and report.md, and checking for rebuttal_qa.md and appendix files.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72aab3fa-ba3f-48a9-9029-1cec279461d0",
  "uuid": "d119a03d-dda8-4895-8c8f-6b3430e9cc5f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M4ukJ8oFtPCxD1zFVepcPv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12023,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12023
      },
      "output_tokens": 26,
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

I'll read the ROADMAP, report.md, and check rebuttal/appendix files in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72aab3fa-ba3f-48a9-9029-1cec279461d0",
  "uuid": "2d9fbcff-3c68-4c74-8a42-4e2c668ec1bb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M4ukJ8oFtPCxD1zFVepcPv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12023,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12023
      },
      "output_tokens": 26,
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01SzNd6dMbbZp26p9nQhns2t`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__read_registry",
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
  "session_id": "72aab3fa-ba3f-48a9-9029-1cec279461d0",
  "uuid": "57b257f4-2b73-44a6-a397-e687adbd6d88",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M4ukJ8oFtPCxD1zFVepcPv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12023,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12023
      },
      "output_tokens": 26,
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

_source line 7 · 2026-05-25T13:46:04.363Z_

<details><summary>↩ Tool result · `toolu_01SzNd6dMbbZp26p9nQhns2t`</summary>

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
  "session_id": "72aab3fa-ba3f-48a9-9029-1cec279461d0",
  "uuid": "e8db32fd-2adc-4551-974b-b01f0961f747",
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

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01V8Kb7gVWvbxS8NPhiHkfYf`</summary>

```json
{
  "project": "event-gated-adaptive-horizon",
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
  "session_id": "72aab3fa-ba3f-48a9-9029-1cec279461d0",
  "uuid": "0155e197-8910-4417-ac77-e9475a09fc35",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FefrktDLSiXMCcPpgUNCr3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 850,
      "cache_read_input_tokens": 23864,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 850
      },
      "output_tokens": 50,
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

_source line 9 · 2026-05-25T13:46:07.178Z_

<details><summary>↩ Tool result · `toolu_01V8Kb7gVWvbxS8NPhiHkfYf`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/ROADMAP.md\", \"content\": \"# event-gated-adaptive-horizon — Research Dashboard\\n\\n> 最后更新: 2026-05-25 11:24 UTC | 更新原因: 更新运行中实验为 exp_074/077/078/079，规划完成后下一批\\n\\n## 核心方向\\nDreamerV3 中 trained dt_embedding 驱动的 CIVO（Compounded Imagination-driven Value Overestimation）是 multi-joint locomotion 特异性现象，frozen/removed dt_emb 可稳健阻止。详见 paper_framing.md。\\n\\n## 当前进展\\n**阶段**: 论文收尾 — Round 5 审稿中 + Cheetah 跨环境验证 + Walker 消融扩展\\n- **投稿目标**: ICML 2026（DDL 5/29，数据锁定 5/27）\\n- **实验统计**: 155 个（78 success / 多 negative / 4 running）\\n- **论文**: 7 页正文 + appendix，ICML 2026 模板，0 errors\\n- **审稿进展**: Round 1→2→3→4 (6/10 Weak Accept) → Round 5 审稿中\\n- **Rebuttal prep**: 15 条 Q&A 完成\\n\\n### 运行中实验（4/4 GPU 满载）\\n| exp_id | 目的 | 服务器 | 预计完成 |\\n|--------|------|--------|----------|\\n| exp_074_008a_walker_s3 | Walker 008a seed=3 额外 seed 数据 | bjb1-45299 cuda:0 | 进行中 |\\n| exp_079_frozen_dt_emb_walker_s0 | frozen dt_emb + subsample ON + dt=2 + H=8 (plan_015) | bjb1-45299 cuda:1 | ~3-4h |\\n| exp_077_cheetah_baseline_s0 | Cheetah baseline seed=0 (plan_020) | westd-19154 cuda:0 | ~3-4h |\\n| exp_078_cheetah_008d_s0 | Cheetah trained dt_emb + subsample ON (plan_021) | westd-19154 cuda:1 | ~3-4h |\\n\\n### 完成后下一批（按优先级）\\n1. **plan_022** Cheetah causal control (dt_embed_dim=0) — 若 078 确认 CIVO，立即跑控制组\\n2. **plan_034** NVE threshold sensitivity — 0 GPU 成本，可立即分析\\n3. **plan_011/012** Walker 008d/008f seeds 1-2 — 缩窄置信区间\\n4. **plan_014** Walker 008e_v3 seeds 1-2 — mitigation 多 seed 验证\\n\\n## 近期任务\\n- [ ] exp_074/077/078/079 完成 → 即时分析 + 更新论文\\n- [ ] Cheetah 结果确认后启动 plan_022 (causal control)\\n- [ ] plan_034 NVE threshold 分析（0 GPU 成本）\\n- [ ] 等待 Round 5 审稿结果\\n- [ ] Round 5 反馈 → 修正 → 数据锁定（5/27）\\n- [ ] ICML 2026 投稿（DDL 5/29）\\n\\n## GPU 预算\\n- bjb1-45299: 2 GPU（RTX PRO 6000 96GB）— cuda:0 exp_074, cuda:1 exp_079\\n- westd-19154: 2 GPU — cuda:0 exp_077, cuda:1 exp_078\\n- 共 4 张全满，保留至 5/29 投稿后释放\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D149 | 2026-05-25 | CIVO scope 精确化：从 \\\"DMC locomotion\\\" 改为 \\\"multi-joint  | exp_061_cartpole_civo_trigger, exp_060_cartpole_baseline, exp_062_cartpole_control |\\n| D148 | 2026-05-24 | 投稿目标确认为 ICML 2026（覆盖 D147 CoRL 记录）。论文已切换 icml2026. | — |\\n| D147 | 2026-05-24 | 用户决定继续投 CoRL 2026，不换 venue | exp_059 |\\n| D146 | 2026-05-23 | D143 混合机制 claim 正式撤回：exp_056 frozen s1 82.5K ve_ra | exp_056_peginsertion_frozen_s1, exp_055_peginsertion_civo_trigger_s1, exp_050_peginsertion_civo_trigger_s0, exp_053_peginsertion_frozen_s0 |\\n| D145 | 2026-05-23 | D143 混合机制受 s1 数据挑战（frozen s1 8.41 > trained s1 2.4 | exp_055_peginsertion_civo_trigger_s1, exp_056_peginsertion_frozen_s1 |\\n| D144 | 2026-05-23 | D143 混合机制完全确认：exp_053 frozen PegInsertion 全程无 seco | exp_053_peginsertion_frozen_s0, exp_054_pickcube_frozen_s0, exp_056_peginsertion_frozen_s1 |\\n| D143 | 2026-05-23 | PegInsertion 重分类为\\\"混合机制 CIVO\\\"（环境触发 + dt_emb 放大），修正  | exp_053_peginsertion_frozen_s0, exp_050_peginsertion_civo_trigger_s0 |\\n| D142 | 2026-05-23 | PegInsertion 初步重分类为环境特异性 transient（待 exp_053 82.5K | exp_053_peginsertion_frozen_s0, exp_050_peginsertion_civo_trigger_s0, exp_051_stackcube_frozen_s0 |\\n| D141 | 2026-05-23 | StackCube ve_ratio spike 重新分类为环境特异性 transient（非 CI | exp_049_stackcube_civo_trigger_s0, exp_052_stackcube_civo_trigger_s1, exp_051_stackcube_frozen_s0, exp_050_peginsertion_civo_trigger_s0 |\\n| D140 | 2026-05-22 | exp_048 Cheetah 不可逆确认(eval 23.4, NVE 2.75, gate 永久 | exp_048_cheetah_civo_extension, exp_052_stackcube_civo_trigger_s1 |\\n\\n\\n\\n\\n\", \"total_chars\": 3358, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "72aab3fa-ba3f-48a9-9029-1cec279461d0",
  "uuid": "cfd641a0-b1d6-4115-b86a-32bc73ed0de7",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/ROADMAP.md\\\", \\\"content\\\": \\\"# event-gated-adaptive-horizon — Research Dashboard\\\\n\\\\n> 最后更新: 2026-05-25 11:24 UTC | 更新原因: 更新运行中实验为 exp_074/077/078/079，规划完成后下一批\\\\n\\\\n## 核心方向\\\\nDreamerV3 中 trained dt_embedding 驱动的 CIVO（Compounded Imagination-driven Value Overestimation）是 multi-joint locomotion 特异性现象，frozen/removed dt_emb 可稳健阻止。详见 paper_framing.md。\\\\n\\\\n## 当前进展\\\\n**阶段**: 论文收尾 — Round 5 审稿中 + Cheetah 跨环境验证 + Walker 消融扩展\\\\n- **投稿目标**: ICML 2026（DDL 5/29，数据锁定 5/27）\\\\n- **实验统计**: 155 个（78 success / 多 negative / 4 running）\\\\n- **论文**: 7 页正文 + appendix，ICML 2026 模板，0 errors\\\\n- **审稿进展**: Round 1→2→3→4 (6/10 Weak Accept) → Round 5 审稿中\\\\n- **Rebuttal prep**: 15 条 Q&A 完成\\\\n\\\\n### 运行中实验（4/4 GPU 满载）\\\\n| exp_id | 目的 | 服务器 | 预计完成 |\\\\n|--------|------|--------|----------|\\\\n| exp_074_008a_walker_s3 | Walker 008a seed=3 额外 seed 数据 | bjb1-45299 cuda:0 | 进行中 |\\\\n| exp_079_frozen_dt_emb_walker_s0 | frozen dt_emb + subsample ON + dt=2 + H=8 (plan_015) | bjb1-45299 cuda:1 | ~3-4h |\\\\n| exp_077_cheetah_baseline_s0 | Cheetah baseline seed=0 (plan_020) | westd-19154 cuda:0 | ~3-4h |\\\\n| exp_078_cheetah_008d_s0 | Cheetah trained dt_emb + subsample ON (plan_021) | westd-19154 cuda:1 | ~3-4h |\\\\n\\\\n### 完成后下一批（按优先级）\\\\n1. **plan_022** Cheetah causal control (dt_embed_dim=0) — 若 078 确认 CIVO，立即跑控制组\\\\n2. **plan_034** NVE threshold sensitivity — 0 GPU 成本，可立即分析\\\\n3. **plan_011/012** Walker 008d/008f seeds 1-2 — 缩窄置信区间\\\\n4. **plan_014** Walker 008e_v3 seeds 1-2 — mitigation 多 seed 验证\\\\n\\\\n## 近期任务\\\\n- [ ] exp_074/077/078/079 完成 → 即时分析 + 更新论文\\\\n- [ ] Cheetah 结果确认后启动 plan_022 (causal control)\\\\n- [ ] plan_034 NVE threshold 分析（0 GPU 成本）\\\\n- [ ] 等待 Round 5 审稿结果\\\\n- [ ] Round 5 反馈 → 修正 → 数据锁定（5/27）\\\\n- [ ] ICML 2026 投稿（DDL 5/29）\\\\n\\\\n## GPU 预算\\\\n- bjb1-45299: 2 GPU（RTX PRO 6000 96GB）— cuda:0 exp_074, cuda:1 exp_079\\\\n- westd-19154: 2 GPU — cuda:0 exp_077, cuda:1 exp_078\\\\n- 共 4 张全满，保留至 5/29 投稿后释放\\\\n\\\\n## 关键决策日志\\\\n\\\\n| ID | 日期 | 摘要 | 关联实验 |\\\\n|----|------|------|----------|\\\\n| D149 | 2026-05-25 | CIVO scope 精确化：从 \\\\\\\"DMC locomotion\\\\\\\" 改为 \\\\\\\"multi-joint  | exp_061_cartpole_civo_trigger, exp_060_cartpole_baseline, exp_062_cartpole_control |\\\\n| D148 | 2026-05-24 | 投稿目标确认为 ICML 2026（覆盖 D147 CoRL 记录）。论文已切换 icml2026. | — |\\\\n| D147 | 2026-05-24 | 用户决定继续投 CoRL 2026，不换 venue | exp_059 |\\\\n| D146 | 2026-05-23 | D143 混合机制 claim 正式撤回：exp_056 frozen s1 82.5K ve_ra | exp_056_peginsertion_frozen_s1, exp_055_peginsertion_civo_trigger_s1, exp_050_peginsertion_civo_trigger_s0, exp_053_peginsertion_frozen_s0 |\\\\n| D145 | 2026-05-23 | D143 混合机制受 s1 数据挑战（frozen s1 8.41 > trained s1 2.4 | exp_055_peginsertion_civo_trigger_s1, exp_056_peginsertion_frozen_s1 |\\\\n| D144 | 2026-05-23 | D143 混合机制完全确认：exp_053 frozen PegInsertion 全程无 seco | exp_053_peginsertion_frozen_s0, exp_054_pickcube_frozen_s0, exp_056_peginsertion_frozen_s1 |\\\\n| D143 | 2026-05-23 | PegInsertion 重分类为\\\\\\\"混合机制 CIVO\\\\\\\"（环境触发 + dt_emb 放大），修正  | exp_053_peginsertion_frozen_s0, exp_050_peginsertion_civo_trigger_s0 |\\\\n| D142 | 2026-05-23 | PegInsertion 初步重分类为环境特异性 transient（待 exp_053 82.5K | exp_053_peginsertion_frozen_s0, exp_050_peginsertion_civo_trigger_s0, exp_051_stackcube_frozen_s0 |\\\\n| D141 | 2026-05-23 | StackCube ve_ratio spike 重新分类为环境特异性 transient（非 CI | exp_049_stackcube_civo_trigger_s0, exp_052_stackcube_civo_trigger_s1, exp_051_stackcube_frozen_s0, exp_050_peginsertion_civo_trigger_s0 |\\\\n| D140 | 2026-05-22 | exp_048 Cheetah 不可逆确认(eval 23.4, NVE 2.75, gate 永久 | exp_048_cheetah_civo_extension, exp_052_stackcube_civo_trigger_s1 |\\\\n\\\\n\\\\n\\\\n\\\\n\\\", \\\"total_chars\\\": 3358, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/ROADMAP.md\", \"content\": \"# event-gated-adaptive-horizon — Research Dashboard\\n\\n> 最后更新: 2026-05-25 11:24 UTC | 更新原因: 更新运行中实验为 exp_074/077/078/079，规划完成后下一批\\n\\n## 核心方向\\nDreamerV3 中 trained dt_embedding 驱动的 CIVO（Compounded Imagination-driven Value Overestimation）是 multi-joint locomotion 特异性现象，frozen/removed dt_emb 可稳健阻止。详见 paper_framing.md。\\n\\n## 当前进展\\n**阶段**: 论文收尾 — Round 5 审稿中 + Cheetah 跨环境验证 + Walker 消融扩展\\n- **投稿目标**: ICML 2026（DDL 5/29，数据锁定 5/27）\\n- **实验统计**: 155 个（78 success / 多 negative / 4 running）\\n- **论文**: 7 页正文 + appendix，ICML 2026 模板，0 errors\\n- **审稿进展**: Round 1→2→3→4 (6/10 Weak Accept) → Round 5 审稿中\\n- **Rebuttal prep**: 15 条 Q&A 完成\\n\\n### 运行中实验（4/4 GPU 满载）\\n| exp_id | 目的 | 服务器 | 预计完成 |\\n|--------|------|--------|----------|\\n| exp_074_008a_walker_s3 | Walker 008a seed=3 额外 seed 数据 | bjb1-45299 cuda:0 | 进行中 |\\n| exp_079_frozen_dt_emb_walker_s0 | frozen dt_emb + subsample ON + dt=2 + H=8 (plan_015) | bjb1-45299 cuda:1 | ~3-4h |\\n| exp_077_cheetah_baseline_s0 | Cheetah baseline seed=0 (plan_020) | westd-19154 cuda:0 | ~3-4h |\\n| exp_078_cheetah_008d_s0 | Cheetah trained dt_emb + subsample ON (plan_021) | westd-19154 cuda:1 | ~3-4h |\\n\\n### 完成后下一批（按优先级）\\n1. **plan_022** Cheetah causal control (dt_embed_dim=0) — 若 078 确认 CIVO，立即跑控制组\\n2. **plan_034** NVE threshold sensitivity — 0 GPU 成本，可立即分析\\n3. **plan_011/012** Walker 008d/008f seeds 1-2 — 缩窄置信区间\\n4. **plan_014** Walker 008e_v3 seeds 1-2 — mitigation 多 seed 验证\\n\\n## 近期任务\\n- [ ] exp_074/077/078/079 完成 → 即时分析 + 更新论文\\n- [ ] Cheetah 结果确认后启动 plan_022 (causal control)\\n- [ ] plan_034 NVE threshold 分析（0 GPU 成本）\\n- [ ] 等待 Round 5 审稿结果\\n- [ ] Round 5 反馈 → 修正 → 数据锁定（5/27）\\n- [ ] ICML 2026 投稿（DDL 5/29）\\n\\n## GPU 预算\\n- bjb1-45299: 2 GPU（RTX PRO 6000 96GB）— cuda:0 exp_074, cuda:1 exp_079\\n- westd-19154: 2 GPU — cuda:0 exp_077, cuda:1 exp_078\\n- 共 4 张全满，保留至 5/29 投稿后释放\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D149 | 2026-05-25 | CIVO scope 精确化：从 \\\"DMC locomotion\\\" 改为 \\\"multi-joint  | exp_061_cartpole_civo_trigger, exp_060_cartpole_baseline, exp_062_cartpole_control |\\n| D148 | 2026-05-24 | 投稿目标确认为 ICML 2026（覆盖 D147 CoRL 记录）。论文已切换 icml2026. | — |\\n| D147 | 2026-05-24 | 用户决定继续投 CoRL 2026，不换 venue | exp_059 |\\n| D146 | 2026-05-23 | D143 混合机制 claim 正式撤回：exp_056 frozen s1 82.5K ve_ra | exp_056_peginsertion_frozen_s1, exp_055_peginsertion_civo_trigger_s1, exp_050_peginsertion_civo_trigger_s0, exp_053_peginsertion_frozen_s0 |\\n| D145 | 2026-05-23 | D143 混合机制受 s1 数据挑战（frozen s1 8.41 > trained s1 2.4 | exp_055_peginsertion_civo_trigger_s1, exp_056_peginsertion_frozen_s1 |\\n| D144 | 2026-05-23 | D143 混合机制完全确认：exp_053 frozen PegInsertion 全程无 seco | exp_053_peginsertion_frozen_s0, exp_054_pickcube_frozen_s0, exp_056_peginsertion_frozen_s1 |\\n| D143 | 2026-05-23 | PegInsertion 重分类为\\\"混合机制 CIVO\\\"（环境触发 + dt_emb 放大），修正  | exp_053_peginsertion_frozen_s0, exp_050_peginsertion_civo_trigger_s0 |\\n| D142 | 2026-05-23 | PegInsertion 初步重分类为环境特异性 transient（待 exp_053 82.5K | exp_053_peginsertion_frozen_s0, exp_050_peginsertion_civo_trigger_s0, exp_051_stackcube_frozen_s0 |\\n| D141 | 2026-05-23 | StackCube ve_ratio spike 重新分类为环境特异性 transient（非 CI | exp_049_stackcube_civo_trigger_s0, exp_052_stackcube_civo_trigger_s1, exp_051_stackcube_frozen_s0, exp_050_peginsertion_civo_trigger_s0 |\\n| D140 | 2026-05-22 | exp_048 Cheetah 不可逆确认(eval 23.4, NVE 2.75, gate 永久 | exp_048_cheetah_civo_extension, exp_052_stackcube_civo_trigger_s1 |\\n\\n\\n\\n\\n\", \"total_chars\": 3358, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01BERUqytHTkaznEVfFYfRF4`</summary>

```json
{
  "project": "event-gated-adaptive-horizon",
  "file": "report.md",
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
  "session_id": "72aab3fa-ba3f-48a9-9029-1cec279461d0",
  "uuid": "e1f4eadc-fddd-4b1c-9a7b-80b00c4e6282",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FefrktDLSiXMCcPpgUNCr3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 850,
      "cache_read_input_tokens": 23864,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 850
      },
      "output_tokens": 50,
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

_source line 11 · 2026-05-25T13:46:07.622Z_

<details><summary>↩ Tool result · `toolu_01BERUqytHTkaznEVfFYfRF4`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/report.md\", \"content\": \"# Handover — 2026-05-25\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| exp_081_008e_v3_walker_s2 | Walker Walk 008e_v3 mitigation seed=2: trained dt_emb + subsample ON (max_dt=2) + dt=1 imagination + H=15。C6 mitigation 第 3 seed，与 seed 0 (success, 95% baseline) 和 seed 1 (exp_080, running) 构成统计三角。plan_014。 | — | — | — |\\n| exp_080_008e_v3_walker_s1 | Walker Walk 008e_v3 mitigation seed=1: trained dt_emb + subsample ON (max_dt=2) + dt=1 imagination + H=15。C6 mitigation 多 seed 验证——trained dt_emb 在 dt=1 imagination 下不触发 CIVO。重跑因旧 exp_008e_v3_walker_s1 metrics 疑似复制自 seed 0。plan_014。 | — | — | — |\\n| exp_078_cheetah_008d_s0 | Cheetah Run CIVO trigger seed=0: trained dt_emb + subsample ON + dt=2 + H=8。与 exp_077 baseline 同时运行以计算 step-matched normalized VE。plan_021 第一个 seed。 | — | — | — |\\n\\n## 待处理\\n- exp_082_cheetah_no_dt_emb_s0: Cheetah Run causal control: dt_embed_dim=0 + subsample ON + dt=2 + H=8, seed=0。移除 dt_embedding 后预期无 CIVO，证明 trained dt_emb 是 Cheetah CIVO 的必要条件。与 exp_078 (trained dt_emb, CIVO trigger) 构成因果对。plan_022。（已分配 ? GPU:?，等待提交）\\n\\n## 近期结论\\n- **exp_074_008a_walker_s3** (success): Walker Walk 008a 配置 (trained dt_emb unexposed + subsample OFF + dt=2 + H=15) seed=3。当前 008a 3 seeds 全部 success (no CIVO)，加 seed=3 巩固 C3 value suppression claim 统计。来源: plan_013 扩展。 ← 基于 exp_008a_no_subsample_dt2\\n- **exp_079_frozen_dt_emb_walker_s0** (killed): Walker Walk frozen dt_emb (requires_grad=False, random init) + subsample ON + dt=2 + H=8, seed=0。验证 dt_emb 的 TRAINING 是 CIVO 必要条件。2×2 ablation 矩阵关键格。plan_015。 ← 基于 exp_067_frozen_dt_emb_walker_plan015\\n- **exp_076_cheetah_civo_trigger_s3** (killed): Cheetah Run CIVO trigger seed=2: trained dt_emb + subsample ON + dt=2 + H=8。将 Cheetah CIVO trigger 扩展到第 3 个独立 seed，巩固跨环境 claim 统计力度。来源: plan_021 扩展。 ← 基于 exp_010b_cheetah_civo_trigger\\n\\n## 趋势\\n成功 79 / 负向 39 / 失败 11 / 共 153\\ncivo_alert: 0 →（近 3 次 success）\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nbjb1-45299: 无 GPU 信息\\nwestd-19154: 空闲 cuda:0, cuda:1\\n\\n## 告警\\n- 016e: 已被终止 — unknown\\n- exp_002_event_gated: 训练失败 — unknown\\n- exp_006: 已被终止 — unknown\\n- exp_008a: 已被终止 — unknown\\n- exp_008a_untrained_s1: 已被终止 — unknown\\n- exp_008a_untrained_s2: 已被终止 — unknown\\n- exp_008c: 已被终止 — unknown\\n- exp_008d: 已被终止 — unknown\\n- exp_008d_civo_trigger_s2: 已被终止 — unknown\\n- exp_008e_subsample_on_dt1_h15: 已被终止 — unknown\\n- exp_008e_subsample_on_fixed_dt1: 已被终止 — unknown\\n- exp_008e_v2_subsample_on_dt1_h15: 已被终止 — unknown\\n- exp_008f_s2: 已被终止 — unknown\\n- exp_009c_s2: 已被终止 — unknown\\n- exp_009d_baseline_walker_s1: 已被终止 — unknown\\n- exp_009f_008f_walker_s1: 已被终止 — unknown\\n- exp_009g_008f_walker_s0: 已被终止 — unknown\\n- exp_009h_008f_walker_s0: 训练失败 — unknown\\n- exp_016_sgs_walker_s1: 训练失败 — unknown\\n- exp_016b_sgs_walker_s1: 训练失败 — unknown\\n- exp_016c_sgs_walker_s1: 训练失败 — unknown\\n- exp_016d_sgs_walker_s1: 训练失败 — unknown\\n- exp_017_subsample_off_trained_dt_emb: 已被终止 — unknown\\n- exp_018_full_sgs_walker_s1: 已被终止 — unknown\\n- exp_019a_pickcube_baseline: 已被终止 — unknown\\n- exp_022_untrained_dt_emb_learned_gate: 已被终止 — unknown\\n- exp_024_cheetah_no_dt_emb_s0: 已被终止 — unknown\\n- exp_025_obs_sgs_walker_s1: 训练失败 — unknown\\n- exp_025_obs_sgs_walker_s3: 训练失败 — unknown\\n- exp_025_obs_sgs_walker_s4: 训练失败 — unknown\\n- exp_026_obs_sgs_cheetah_s0: 训练失败 — unknown\\n- exp_026_obs_sgs_cheetah_s1: 训练失败 — unknown\\n- exp_075_cheetah_civo_trigger_s2: 已被终止 — unknown\\n- exp_076_cheetah_civo_trigger_s3: 已被终止 — unknown\\n- exp_079_frozen_dt_emb_walker_s0: 已被终止 — unknown\\n\", \"total_chars\": 3488, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "72aab3fa-ba3f-48a9-9029-1cec279461d0",
  "uuid": "0b5ba1d5-c3bc-4c69-907f-7964a775304e",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/report.md\\\", \\\"content\\\": \\\"# Handover — 2026-05-25\\\\n\\\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\\\n\\\\n## 运行中\\\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\\\n|--------|------|------|---------|-----|\\\\n| exp_081_008e_v3_walker_s2 | Walker Walk 008e_v3 mitigation seed=2: trained dt_emb + subsample ON (max_dt=2) + dt=1 imagination + H=15。C6 mitigation 第 3 seed，与 seed 0 (success, 95% baseline) 和 seed 1 (exp_080, running) 构成统计三角。plan_014。 | — | — | — |\\\\n| exp_080_008e_v3_walker_s1 | Walker Walk 008e_v3 mitigation seed=1: trained dt_emb + subsample ON (max_dt=2) + dt=1 imagination + H=15。C6 mitigation 多 seed 验证——trained dt_emb 在 dt=1 imagination 下不触发 CIVO。重跑因旧 exp_008e_v3_walker_s1 metrics 疑似复制自 seed 0。plan_014。 | — | — | — |\\\\n| exp_078_cheetah_008d_s0 | Cheetah Run CIVO trigger seed=0: trained dt_emb + subsample ON + dt=2 + H=8。与 exp_077 baseline 同时运行以计算 step-matched normalized VE。plan_021 第一个 seed。 | — | — | — |\\\\n\\\\n## 待处理\\\\n- exp_082_cheetah_no_dt_emb_s0: Cheetah Run causal control: dt_embed_dim=0 + subsample ON + dt=2 + H=8, seed=0。移除 dt_embedding 后预期无 CIVO，证明 trained dt_emb 是 Cheetah CIVO 的必要条件。与 exp_078 (trained dt_emb, CIVO trigger) 构成因果对。plan_022。（已分配 ? GPU:?，等待提交）\\\\n\\\\n## 近期结论\\\\n- **exp_074_008a_walker_s3** (success): Walker Walk 008a 配置 (trained dt_emb unexposed + subsample OFF + dt=2 + H=15) seed=3。当前 008a 3 seeds 全部 success (no CIVO)，加 seed=3 巩固 C3 value suppression claim 统计。来源: plan_013 扩展。 ← 基于 exp_008a_no_subsample_dt2\\\\n- **exp_079_frozen_dt_emb_walker_s0** (killed): Walker Walk frozen dt_emb (requires_grad=False, random init) + subsample ON + dt=2 + H=8, seed=0。验证 dt_emb 的 TRAINING 是 CIVO 必要条件。2×2 ablation 矩阵关键格。plan_015。 ← 基于 exp_067_frozen_dt_emb_walker_plan015\\\\n- **exp_076_cheetah_civo_trigger_s3** (killed): Cheetah Run CIVO trigger seed=2: trained dt_emb + subsample ON + dt=2 + H=8。将 Cheetah CIVO trigger 扩展到第 3 个独立 seed，巩固跨环境 claim 统计力度。来源: plan_021 扩展。 ← 基于 exp_010b_cheetah_civo_trigger\\\\n\\\\n## 趋势\\\\n成功 79 / 负向 39 / 失败 11 / 共 153\\\\ncivo_alert: 0 →（近 3 次 success）\\\\n\\\\n## 下一步\\\\n（无活跃 idea，请通过 ideas.md 添加）\\\\n\\\\n## 资源状态\\\\nbjb1-45299: 无 GPU 信息\\\\nwestd-19154: 空闲 cuda:0, cuda:1\\\\n\\\\n## 告警\\\\n- 016e: 已被终止 — unknown\\\\n- exp_002_event_gated: 训练失败 — unknown\\\\n- exp_006: 已被终止 — unknown\\\\n- exp_008a: 已被终止 — unknown\\\\n- exp_008a_untrained_s1: 已被终止 — unknown\\\\n- exp_008a_untrained_s2: 已被终止 — unknown\\\\n- exp_008c: 已被终止 — unknown\\\\n- exp_008d: 已被终止 — unknown\\\\n- exp_008d_civo_trigger_s2: 已被终止 — unknown\\\\n- exp_008e_subsample_on_dt1_h15: 已被终止 — unknown\\\\n- exp_008e_subsample_on_fixed_dt1: 已被终止 — unknown\\\\n- exp_008e_v2_subsample_on_dt1_h15: 已被终止 — unknown\\\\n- exp_008f_s2: 已被终止 — unknown\\\\n- exp_009c_s2: 已被终止 — unknown\\\\n- exp_009d_baseline_walker_s1: 已被终止 — unknown\\\\n- exp_009f_008f_walker_s1: 已被终止 — unknown\\\\n- exp_009g_008f_walker_s0: 已被终止 — unknown\\\\n- exp_009h_008f_walker_s0: 训练失败 — unknown\\\\n- exp_016_sgs_walker_s1: 训练失败 — unknown\\\\n- exp_016b_sgs_walker_s1: 训练失败 — unknown\\\\n- exp_016c_sgs_walker_s1: 训练失败 — unknown\\\\n- exp_016d_sgs_walker_s1: 训练失败 — unknown\\\\n- exp_017_subsample_off_trained_dt_emb: 已被终止 — unknown\\\\n- exp_018_full_sgs_walker_s1: 已被终止 — unknown\\\\n- exp_019a_pickcube_baseline: 已被终止 — unknown\\\\n- exp_022_untrained_dt_emb_learned_gate: 已被终止 — unknown\\\\n- exp_024_cheetah_no_dt_emb_s0: 已被终止 — unknown\\\\n- exp_025_obs_sgs_walker_s1: 训练失败 — unknown\\\\n- exp_025_obs_sgs_walker_s3: 训练失败 — unknown\\\\n- exp_025_obs_sgs_walker_s4: 训练失败 — unknown\\\\n- exp_026_obs_sgs_cheetah_s0: 训练失败 — unknown\\\\n- exp_026_obs_sgs_cheetah_s1: 训练失败 — unknown\\\\n- exp_075_cheetah_civo_trigger_s2: 已被终止 — unknown\\\\n- exp_076_cheetah_civo_trigger_s3: 已被终止 — unknown\\\\n- exp_079_frozen_dt_emb_walker_s0: 已被终止 — unknown\\\\n\\\", \\\"total_chars\\\": 3488, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/report.md\", \"content\": \"# Handover — 2026-05-25\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| exp_081_008e_v3_walker_s2 | Walker Walk 008e_v3 mitigation seed=2: trained dt_emb + subsample ON (max_dt=2) + dt=1 imagination + H=15。C6 mitigation 第 3 seed，与 seed 0 (success, 95% baseline) 和 seed 1 (exp_080, running) 构成统计三角。plan_014。 | — | — | — |\\n| exp_080_008e_v3_walker_s1 | Walker Walk 008e_v3 mitigation seed=1: trained dt_emb + subsample ON (max_dt=2) + dt=1 imagination + H=15。C6 mitigation 多 seed 验证——trained dt_emb 在 dt=1 imagination 下不触发 CIVO。重跑因旧 exp_008e_v3_walker_s1 metrics 疑似复制自 seed 0。plan_014。 | — | — | — |\\n| exp_078_cheetah_008d_s0 | Cheetah Run CIVO trigger seed=0: trained dt_emb + subsample ON + dt=2 + H=8。与 exp_077 baseline 同时运行以计算 step-matched normalized VE。plan_021 第一个 seed。 | — | — | — |\\n\\n## 待处理\\n- exp_082_cheetah_no_dt_emb_s0: Cheetah Run causal control: dt_embed_dim=0 + subsample ON + dt=2 + H=8, seed=0。移除 dt_embedding 后预期无 CIVO，证明 trained dt_emb 是 Cheetah CIVO 的必要条件。与 exp_078 (trained dt_emb, CIVO trigger) 构成因果对。plan_022。（已分配 ? GPU:?，等待提交）\\n\\n## 近期结论\\n- **exp_074_008a_walker_s3** (success): Walker Walk 008a 配置 (trained dt_emb unexposed + subsample OFF + dt=2 + H=15) seed=3。当前 008a 3 seeds 全部 success (no CIVO)，加 seed=3 巩固 C3 value suppression claim 统计。来源: plan_013 扩展。 ← 基于 exp_008a_no_subsample_dt2\\n- **exp_079_frozen_dt_emb_walker_s0** (killed): Walker Walk frozen dt_emb (requires_grad=False, random init) + subsample ON + dt=2 + H=8, seed=0。验证 dt_emb 的 TRAINING 是 CIVO 必要条件。2×2 ablation 矩阵关键格。plan_015。 ← 基于 exp_067_frozen_dt_emb_walker_plan015\\n- **exp_076_cheetah_civo_trigger_s3** (killed): Cheetah Run CIVO trigger seed=2: trained dt_emb + subsample ON + dt=2 + H=8。将 Cheetah CIVO trigger 扩展到第 3 个独立 seed，巩固跨环境 claim 统计力度。来源: plan_021 扩展。 ← 基于 exp_010b_cheetah_civo_trigger\\n\\n## 趋势\\n成功 79 / 负向 39 / 失败 11 / 共 153\\ncivo_alert: 0 →（近 3 次 success）\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nbjb1-45299: 无 GPU 信息\\nwestd-19154: 空闲 cuda:0, cuda:1\\n\\n## 告警\\n- 016e: 已被终止 — unknown\\n- exp_002_event_gated: 训练失败 — unknown\\n- exp_006: 已被终止 — unknown\\n- exp_008a: 已被终止 — unknown\\n- exp_008a_untrained_s1: 已被终止 — unknown\\n- exp_008a_untrained_s2: 已被终止 — unknown\\n- exp_008c: 已被终止 — unknown\\n- exp_008d: 已被终止 — unknown\\n- exp_008d_civo_trigger_s2: 已被终止 — unknown\\n- exp_008e_subsample_on_dt1_h15: 已被终止 — unknown\\n- exp_008e_subsample_on_fixed_dt1: 已被终止 — unknown\\n- exp_008e_v2_subsample_on_dt1_h15: 已被终止 — unknown\\n- exp_008f_s2: 已被终止 — unknown\\n- exp_009c_s2: 已被终止 — unknown\\n- exp_009d_baseline_walker_s1: 已被终止 — unknown\\n- exp_009f_008f_walker_s1: 已被终止 — unknown\\n- exp_009g_008f_walker_s0: 已被终止 — unknown\\n- exp_009h_008f_walker_s0: 训练失败 — unknown\\n- exp_016_sgs_walker_s1: 训练失败 — unknown\\n- exp_016b_sgs_walker_s1: 训练失败 — unknown\\n- exp_016c_sgs_walker_s1: 训练失败 — unknown\\n- exp_016d_sgs_walker_s1: 训练失败 — unknown\\n- exp_017_subsample_off_trained_dt_emb: 已被终止 — unknown\\n- exp_018_full_sgs_walker_s1: 已被终止 — unknown\\n- exp_019a_pickcube_baseline: 已被终止 — unknown\\n- exp_022_untrained_dt_emb_learned_gate: 已被终止 — unknown\\n- exp_024_cheetah_no_dt_emb_s0: 已被终止 — unknown\\n- exp_025_obs_sgs_walker_s1: 训练失败 — unknown\\n- exp_025_obs_sgs_walker_s3: 训练失败 — unknown\\n- exp_025_obs_sgs_walker_s4: 训练失败 — unknown\\n- exp_026_obs_sgs_cheetah_s0: 训练失败 — unknown\\n- exp_026_obs_sgs_cheetah_s1: 训练失败 — unknown\\n- exp_075_cheetah_civo_trigger_s2: 已被终止 — unknown\\n- exp_076_cheetah_civo_trigger_s3: 已被终止 — unknown\\n- exp_079_frozen_dt_emb_walker_s0: 已被终止 — unknown\\n\", \"total_chars\": 3488, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_0132iht1ZGzEndeR7i1VSXH8`</summary>

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
  "session_id": "72aab3fa-ba3f-48a9-9029-1cec279461d0",
  "uuid": "edc839ea-a19a-4ba2-a95e-667dc285b226",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FefrktDLSiXMCcPpgUNCr3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 850,
      "cache_read_input_tokens": 23864,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 850
      },
      "output_tokens": 50,
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

_source line 13 · 2026-05-25T13:46:08.588Z_

<details><summary>↩ Tool result · `toolu_0132iht1ZGzEndeR7i1VSXH8`</summary>

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
  "session_id": "72aab3fa-ba3f-48a9-9029-1cec279461d0",
  "uuid": "a98644bb-40b0-4ee9-b3f9-a8fc09ad9dd6",
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

_source line 14_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_014Ud7K3WW9GozsN6bPQcNMi`</summary>

```json
{
  "project": "event-gated-adaptive-horizon",
  "filters": {
    "status": "RUNNING"
  },
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
  "session_id": "72aab3fa-ba3f-48a9-9029-1cec279461d0",
  "uuid": "e19cdd93-2154-4add-87a3-ff6c3aa52cb4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FefrktDLSiXMCcPpgUNCr3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 850,
      "cache_read_input_tokens": 23864,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 850
      },
      "output_tokens": 50,
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

_source line 15 · 2026-05-25T13:46:10.713Z_

<details><summary>↩ Tool result · `toolu_014Ud7K3WW9GozsN6bPQcNMi`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"exp_081_008e_v3_walker_s2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T12:09:44.566Z\", \"updated_at\": \"2026-05-25T12:49:21.343Z\", \"hypothesis\": \"Walker Walk 008e_v3 mitigation seed=2: trained dt_emb + subsample ON (max_dt=2) + dt=1 imagination + H=15。C6 mitigation 第 3 seed，与 seed 0 (success, 95% baseline) 和 seed 1 (exp_080, running) 构成统计三角。plan_014。\", \"parent\": \"exp_008e_v3_subsample_on_dt1_h15\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_081_008e_v3_walker_s2 --steps 105000 --seed 2 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 1 --gate_subsample_max_dt 2 --imag_horizon 15\\\"\", \"server\": \"bjb1-45299\", \"gpu\": [\"cuda:0\"], \"pid\": \"285949\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_081_008e_v3_walker_s2.log\", \"submitted_at\": \"2026-05-25T12:10:38.467Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"seed\": 2, \"model_name\": \"DreamerV3+SubsampleON_FixedDt1_H15\", \"data_path\": \"dmc_walker_walk\", \"data_count\": 105000, \"checkpoint_source\": \"N/A (training from scratch, parent is lineage only)\", \"eval_data\": \"N/A (training experiment)\"}}, \"exp_080_008e_v3_walker_s1\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T11:30:20.594Z\", \"updated_at\": \"2026-05-25T12:49:19.083Z\", \"hypothesis\": \"Walker Walk 008e_v3 mitigation seed=1: trained dt_emb + subsample ON (max_dt=2) + dt=1 imagination + H=15。C6 mitigation 多 seed 验证——trained dt_emb 在 dt=1 imagination 下不触发 CIVO。重跑因旧 exp_008e_v3_walker_s1 metrics 疑似复制自 seed 0。plan_014。\", \"parent\": \"exp_008e_v3_subsample_on_dt1_h15\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_080_008e_v3_walker_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 1 --gate_subsample_max_dt 2 --imag_horizon 15\\\"\", \"server\": \"bjb1-45299\", \"gpu\": [\"cuda:1\"], \"pid\": \"283925\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_080_008e_v3_walker_s1.log\", \"submitted_at\": \"2026-05-25T11:30:51.090Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"seed\": 1, \"model_name\": \"DreamerV3+SubsampleON_FixedDt1_H15\", \"data_path\": \"dmc_walker_walk\", \"data_count\": 105000, \"checkpoint_source\": \"N/A (training from scratch, parent is lineage only)\", \"eval_data\": \"N/A (training experiment)\"}}, \"exp_078_cheetah_008d_s0\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T10:48:24.844Z\", \"updated_at\": \"2026-05-25T11:21:52.244Z\", \"hypothesis\": \"Cheetah Run CIVO trigger seed=0: trained dt_emb + subsample ON + dt=2 + H=8。与 exp_077 baseline 同时运行以计算 step-matched normalized VE。plan_021 第一个 seed。\", \"server\": \"westd-19154\", \"gpu\": \"cuda:1\", \"parent\": \"exp_010b_cheetah_civo_trigger\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=1 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_078_cheetah_008d_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8\\\"\", \"server\": \"westd-19154\", \"gpu\": [\"cuda:1\"], \"pid\": \"21846\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_078_cheetah_008d_s0.log\", \"submitted_at\": \"2026-05-25T11:21:50.283Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"pid\": \"21846\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_078_cheetah_008d_s0.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=1 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_078_cheetah_008d_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8\\\"\"}}, \"exp_077_cheetah_baseline_s0\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T10:48:21.685Z\", \"updated_at\": \"2026-05-25T11:21:46.208Z\", \"hypothesis\": \"Cheetah Run dt=1 baseline seed=0。建立 v/e ratio 校准基线，用于归一化同时运行的 exp_078 (Cheetah 008d) 的 VE。plan_020 第一个 seed。\", \"server\": \"westd-19154\", \"gpu\": \"cuda:0\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=0 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_077_cheetah_baseline_s0 --steps 105000 --seed 0 --compile False --device cuda:0\\\"\", \"server\": \"westd-19154\", \"gpu\": [\"cuda:0\"], \"pid\": \"21683\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_077_cheetah_baseline_s0.log\", \"submitted_at\": \"2026-05-25T11:21:44.224Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"pid\": \"21683\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_077_cheetah_baseline_s0.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=0 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_077_cheetah_baseline_s0 --steps 105000 --seed 0 --compile False --device cuda:0\\\"\"}}}, \"count\": 4, \"total\": 4, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.5614}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "72aab3fa-ba3f-48a9-9029-1cec279461d0",
  "uuid": "19fae9e5-c7ab-4cb6-ab21-c488e7880d01",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"exp_081_008e_v3_walker_s2\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-25T12:09:44.566Z\\\", \\\"updated_at\\\": \\\"2026-05-25T12:49:21.343Z\\\", \\\"hypothesis\\\": \\\"Walker Walk 008e_v3 mitigation seed=2: trained dt_emb + subsample ON (max_dt=2) + dt=1 imagination + H=15。C6 mitigation 第 3 seed，与 seed 0 (success, 95% baseline) 和 seed 1 (exp_080, running) 构成统计三角。plan_014。\\\", \\\"parent\\\": \\\"exp_008e_v3_subsample_on_dt1_h15\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_081_008e_v3_walker_s2 --steps 105000 --seed 2 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 1 --gate_subsample_max_dt 2 --imag_horizon 15\\\\\\\"\\\", \\\"server\\\": \\\"bjb1-45299\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"285949\\\", \\\"log_path\\\": \\\"~/runs/event-gated-adaptive-horizon/exp_081_008e_v3_walker_s2.log\\\", \\\"submitted_at\\\": \\\"2026-05-25T12:10:38.467Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"seed\\\": 2, \\\"model_name\\\": \\\"DreamerV3+SubsampleON_FixedDt1_H15\\\", \\\"data_path\\\": \\\"dmc_walker_walk\\\", \\\"data_count\\\": 105000, \\\"checkpoint_source\\\": \\\"N/A (training from scratch, parent is lineage only)\\\", \\\"eval_data\\\": \\\"N/A (training experiment)\\\"}}, \\\"exp_080_008e_v3_walker_s1\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-25T11:30:20.594Z\\\", \\\"updated_at\\\": \\\"2026-05-25T12:49:19.083Z\\\", \\\"hypothesis\\\": \\\"Walker Walk 008e_v3 mitigation seed=1: trained dt_emb + subsample ON (max_dt=2) + dt=1 imagination + H=15。C6 mitigation 多 seed 验证——trained dt_emb 在 dt=1 imagination 下不触发 CIVO。重跑因旧 exp_008e_v3_walker_s1 metrics 疑似复制自 seed 0。plan_014。\\\", \\\"parent\\\": \\\"exp_008e_v3_subsample_on_dt1_h15\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_080_008e_v3_walker_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 1 --gate_subsample_max_dt 2 --imag_horizon 15\\\\\\\"\\\", \\\"server\\\": \\\"bjb1-45299\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"pid\\\": \\\"283925\\\", \\\"log_path\\\": \\\"~/runs/event-gated-adaptive-horizon/exp_080_008e_v3_walker_s1.log\\\", \\\"submitted_at\\\": \\\"2026-05-25T11:30:51.090Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\", \\\"seed\\\": 1, \\\"model_name\\\": \\\"DreamerV3+SubsampleON_FixedDt1_H15\\\", \\\"data_path\\\": \\\"dmc_walker_walk\\\", \\\"data_count\\\": 105000, \\\"checkpoint_source\\\": \\\"N/A (training from scratch, parent is lineage only)\\\", \\\"eval_data\\\": \\\"N/A (training experiment)\\\"}}, \\\"exp_078_cheetah_008d_s0\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-25T10:48:24.844Z\\\", \\\"updated_at\\\": \\\"2026-05-25T11:21:52.244Z\\\", \\\"hypothesis\\\": \\\"Cheetah Run CIVO trigger seed=0: trained dt_emb + subsample ON + dt=2 + H=8。与 exp_077 baseline 同时运行以计算 step-matched normalized VE。plan_021 第一个 seed。\\\", \\\"server\\\": \\\"westd-19154\\\", \\\"gpu\\\": \\\"cuda:1\\\", \\\"parent\\\": \\\"exp_010b_cheetah_civo_trigger\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=1 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_078_cheetah_008d_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8\\\\\\\"\\\", \\\"server\\\": \\\"westd-19154\\\", \\\"gpu\\\": [\\\"cuda:1\\\"], \\\"pid\\\": \\\"21846\\\", \\\"log_path\\\": \\\"~/runs/event-gated-adaptive-horizon/exp_078_cheetah_008d_s0.log\\\", \\\"submitted_at\\\": \\\"2026-05-25T11:21:50.283Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\"}, \\\"pid\\\": \\\"21846\\\", \\\"log_path\\\": \\\"~/runs/event-gated-adaptive-horizon/exp_078_cheetah_008d_s0.log\\\", \\\"reproduce\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=1 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_078_cheetah_008d_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8\\\\\\\"\\\"}}, \\\"exp_077_cheetah_baseline_s0\\\": {\\\"status\\\": \\\"RUNNING\\\", \\\"retry_count\\\": 0, \\\"created_at\\\": \\\"2026-05-25T10:48:21.685Z\\\", \\\"updated_at\\\": \\\"2026-05-25T11:21:46.208Z\\\", \\\"hypothesis\\\": \\\"Cheetah Run dt=1 baseline seed=0。建立 v/e ratio 校准基线，用于归一化同时运行的 exp_078 (Cheetah 008d) 的 VE。plan_020 第一个 seed。\\\", \\\"server\\\": \\\"westd-19154\\\", \\\"gpu\\\": \\\"cuda:0\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=0 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_077_cheetah_baseline_s0 --steps 105000 --seed 0 --compile False --device cuda:0\\\\\\\"\\\", \\\"server\\\": \\\"westd-19154\\\", \\\"gpu\\\": [\\\"cuda:0\\\"], \\\"pid\\\": \\\"21683\\\", \\\"log_path\\\": \\\"~/runs/event-gated-adaptive-horizon/exp_077_cheetah_baseline_s0.log\\\", \\\"submitted_at\\\": \\\"2026-05-25T11:21:44.224Z\\\", \\\"submitted_via\\\": \\\"submit_training_job\\\", \\\"backend\\\": \\\"tmux\\\", \\\"account\\\": \\\"root\\\"}, \\\"pid\\\": \\\"21683\\\", \\\"log_path\\\": \\\"~/runs/event-gated-adaptive-horizon/exp_077_cheetah_baseline_s0.log\\\", \\\"reproduce\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=0 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_077_cheetah_baseline_s0 --steps 105000 --seed 0 --compile False --device cuda:0\\\\\\\"\\\"}}}, \\\"count\\\": 4, \\\"total\\\": 4, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 1.5614}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"exp_081_008e_v3_walker_s2\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T12:09:44.566Z\", \"updated_at\": \"2026-05-25T12:49:21.343Z\", \"hypothesis\": \"Walker Walk 008e_v3 mitigation seed=2: trained dt_emb + subsample ON (max_dt=2) + dt=1 imagination + H=15。C6 mitigation 第 3 seed，与 seed 0 (success, 95% baseline) 和 seed 1 (exp_080, running) 构成统计三角。plan_014。\", \"parent\": \"exp_008e_v3_subsample_on_dt1_h15\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_081_008e_v3_walker_s2 --steps 105000 --seed 2 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 1 --gate_subsample_max_dt 2 --imag_horizon 15\\\"\", \"server\": \"bjb1-45299\", \"gpu\": [\"cuda:0\"], \"pid\": \"285949\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_081_008e_v3_walker_s2.log\", \"submitted_at\": \"2026-05-25T12:10:38.467Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"seed\": 2, \"model_name\": \"DreamerV3+SubsampleON_FixedDt1_H15\", \"data_path\": \"dmc_walker_walk\", \"data_count\": 105000, \"checkpoint_source\": \"N/A (training from scratch, parent is lineage only)\", \"eval_data\": \"N/A (training experiment)\"}}, \"exp_080_008e_v3_walker_s1\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T11:30:20.594Z\", \"updated_at\": \"2026-05-25T12:49:19.083Z\", \"hypothesis\": \"Walker Walk 008e_v3 mitigation seed=1: trained dt_emb + subsample ON (max_dt=2) + dt=1 imagination + H=15。C6 mitigation 多 seed 验证——trained dt_emb 在 dt=1 imagination 下不触发 CIVO。重跑因旧 exp_008e_v3_walker_s1 metrics 疑似复制自 seed 0。plan_014。\", \"parent\": \"exp_008e_v3_subsample_on_dt1_h15\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk --logdir logdir/exp_080_008e_v3_walker_s1 --steps 105000 --seed 1 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 1 --gate_subsample_max_dt 2 --imag_horizon 15\\\"\", \"server\": \"bjb1-45299\", \"gpu\": [\"cuda:1\"], \"pid\": \"283925\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_080_008e_v3_walker_s1.log\", \"submitted_at\": \"2026-05-25T11:30:51.090Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"seed\": 1, \"model_name\": \"DreamerV3+SubsampleON_FixedDt1_H15\", \"data_path\": \"dmc_walker_walk\", \"data_count\": 105000, \"checkpoint_source\": \"N/A (training from scratch, parent is lineage only)\", \"eval_data\": \"N/A (training experiment)\"}}, \"exp_078_cheetah_008d_s0\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T10:48:24.844Z\", \"updated_at\": \"2026-05-25T11:21:52.244Z\", \"hypothesis\": \"Cheetah Run CIVO trigger seed=0: trained dt_emb + subsample ON + dt=2 + H=8。与 exp_077 baseline 同时运行以计算 step-matched normalized VE。plan_021 第一个 seed。\", \"server\": \"westd-19154\", \"gpu\": \"cuda:1\", \"parent\": \"exp_010b_cheetah_civo_trigger\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=1 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_078_cheetah_008d_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8\\\"\", \"server\": \"westd-19154\", \"gpu\": [\"cuda:1\"], \"pid\": \"21846\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_078_cheetah_008d_s0.log\", \"submitted_at\": \"2026-05-25T11:21:50.283Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"pid\": \"21846\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_078_cheetah_008d_s0.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=1 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_078_cheetah_008d_s0 --steps 105000 --seed 0 --compile False --device cuda:0 --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 --imag_horizon 8\\\"\"}}, \"exp_077_cheetah_baseline_s0\": {\"status\": \"RUNNING\", \"retry_count\": 0, \"created_at\": \"2026-05-25T10:48:21.685Z\", \"updated_at\": \"2026-05-25T11:21:46.208Z\", \"hypothesis\": \"Cheetah Run dt=1 baseline seed=0。建立 v/e ratio 校准基线，用于归一化同时运行的 exp_078 (Cheetah 008d) 的 VE。plan_020 第一个 seed。\", \"server\": \"westd-19154\", \"gpu\": \"cuda:0\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=0 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_077_cheetah_baseline_s0 --steps 105000 --seed 0 --compile False --device cuda:0\\\"\", \"server\": \"westd-19154\", \"gpu\": [\"cuda:0\"], \"pid\": \"21683\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_077_cheetah_baseline_s0.log\", \"submitted_at\": \"2026-05-25T11:21:44.224Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"pid\": \"21683\", \"log_path\": \"~/runs/event-gated-adaptive-horizon/exp_077_cheetah_baseline_s0.log\", \"reproduce\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && export MUJOCO_GL=egl && export PYOPENGL_PLATFORM=egl && export MUJOCO_EGL_DEVICE_ID=0 && cd /root/autodl-tmp/event-gated-adaptive-horizon && python -u dreamer.py --configs defaults dmc_proprio --task dmc_cheetah_run --logdir logdir/exp_077_cheetah_baseline_s0 --steps 105000 --seed 0 --compile False --device cuda:0\\\"\"}}}, \"count\": 4, \"total\": 4, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 1.5614}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 16_

<details><summary>Logged reasoning block</summary>

```text
Now I have the ROADMAP, report.md, and the running experiments. The rebuttal_qa.md is not a supported file name for read_project_file. Let me check if it exists as a file in the project directory and also look for appendix files.

Let me also check the registry for completed experiments to cross-reference with paper data.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72aab3fa-ba3f-48a9-9029-1cec279461d0",
  "uuid": "e8cef026-97e6-4f10-bd6e-21f6115de38f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WPC8vbtWJZmhL5uC9n9AY2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7502,
      "cache_read_input_tokens": 24714,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7502
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

_source line 17_

Now let me check for rebuttal_qa.md and appendix files in the project directory, and get recent successful experiments from the registry.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72aab3fa-ba3f-48a9-9029-1cec279461d0",
  "uuid": "ca9aa6f9-3faf-4ada-812c-722ff84b2164",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WPC8vbtWJZmhL5uC9n9AY2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7502,
      "cache_read_input_tokens": 24714,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7502
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

_source line 18_

<details open><summary>🔧 Tool call — Glob · `toolu_01Dan16v9TwnMho4Coi4i5c2`</summary>

```json
{
  "pattern": "**/*rebuttal*",
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
  "session_id": "72aab3fa-ba3f-48a9-9029-1cec279461d0",
  "uuid": "8b23ad21-7e11-488d-adf6-65f716a9e002",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WPC8vbtWJZmhL5uC9n9AY2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7502,
      "cache_read_input_tokens": 24714,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7502
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

_source line 19 · 2026-05-25T13:46:18.561Z_

<details><summary>↩ Tool result · `toolu_01Dan16v9TwnMho4Coi4i5c2`</summary>

```text
logs/workers/worker_paper_rebuttal-prewrite_20260518T181655.log
logs/workers/worker_paper_rebuttal-prewrite_20260518T181655_result.json
docs/paper/rebuttal_notes.md
artifacts/_project/report/rebuttal_draft.md
logs/workers/worker_writing_rebuttal_draft_framework_20260522T073659.log
logs/workers/worker_writing_rebuttal_draft_framework_20260522T073659_result.json
artifacts/rebuttal_draft.md
logs/workers/worker_draft_rebuttal-prep_20260524T030759.log
logs/workers/worker_draft_rebuttal-prep_20260524T030759_result.json
logs/workers/worker_verify_rebuttal-q5-numbers_20260524T032017.log
logs/workers/worker_verify_rebuttal-q5-numbers_20260524T032017_result.json
artifacts/_project/report/rebuttal_prep.md
artifacts/rebuttal_prep.md
logs/workers/worker_paper_rebuttal_prep_expansion_20260524T114857.log
logs/chats/worker_paper_rebuttal_prep_expansion_20260524T114857.lock
logs/chats/worker_paper_rebuttal_prep_expansion_20260524T114857.jsonl
logs/workers/worker_paper_rebuttal_prep_expansion_20260524T114857_result.json
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "72aab3fa-ba3f-48a9-9029-1cec279461d0",
  "uuid": "157d7942-be17-44ca-b3fc-5373291cd275",
  "tool_use_result": {
    "filenames": [
      "logs/workers/worker_paper_rebuttal-prewrite_20260518T181655.log",
      "logs/workers/worker_paper_rebuttal-prewrite_20260518T181655_result.json",
      "docs/paper/rebuttal_notes.md",
      "artifacts/_project/report/rebuttal_draft.md",
      "logs/workers/worker_writing_rebuttal_draft_framework_20260522T073659.log",
      "logs/workers/worker_writing_rebuttal_draft_framework_20260522T073659_result.json",
      "artifacts/rebuttal_draft.md",
      "logs/workers/worker_draft_rebuttal-prep_20260524T030759.log",
      "logs/workers/worker_draft_rebuttal-prep_20260524T030759_result.json",
      "logs/workers/worker_verify_rebuttal-q5-numbers_20260524T032017.log",
      "logs/workers/worker_verify_rebuttal-q5-numbers_20260524T032017_result.json",
      "artifacts/_project/report/rebuttal_prep.md",
      "artifacts/rebuttal_prep.md",
      "logs/workers/worker_paper_rebuttal_prep_expansion_20260524T114857.log",
      "logs/chats/worker_paper_rebuttal_prep_expansion_20260524T114857.lock",
      "logs/chats/worker_paper_rebuttal_prep_expansion_20260524T114857.jsonl",
      "logs/workers/worker_paper_rebuttal_prep_expansion_20260524T114857_result.json"
    ],
    "durationMs": 50,
    "numFiles": 17,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — Glob · `toolu_01HaYFdMhB6bdAwZud3E115d`</summary>

```json
{
  "pattern": "**/*appendix*",
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
  "session_id": "72aab3fa-ba3f-48a9-9029-1cec279461d0",
  "uuid": "6f18b72f-b015-4557-b1ec-2471430889e0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WPC8vbtWJZmhL5uC9n9AY2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7502,
      "cache_read_input_tokens": 24714,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7502
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

_source line 21 · 2026-05-25T13:46:19.203Z_

<details><summary>↩ Tool result · `toolu_01HaYFdMhB6bdAwZud3E115d`</summary>

```text
logs/workers/worker_paper_appendix_nve_sensitivity_table_20260515T183716.log
logs/workers/worker_paper_appendix_nve_sensitivity_table_20260515T183716_result.json
logs/workers/worker_paper_appendix-task-b1_20260515T195419.log
logs/workers/worker_paper_appendix-task-b1_20260515T195419_result.json
logs/workers/worker_paper_appendix-auroc-revert_20260517T130453.log
logs/workers/worker_paper_appendix-auroc-revert_20260517T130453_result.json
logs/workers/worker_paper_021-appendix-table_20260517T234234.log
logs/workers/worker_paper_021-appendix-table_20260517T234234_result.json
logs/workers/worker_paper_c6-results-appendix-detector_20260518T113449.log
logs/workers/worker_fix_appendix-eval-data_20260524T021344.log
logs/workers/worker_fix_appendix-eval-data_20260524T021344_result.json
docs/paper/sections/appendix.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "72aab3fa-ba3f-48a9-9029-1cec279461d0",
  "uuid": "47f8716b-271f-47e8-a594-8fb290715a7b",
  "tool_use_result": {
    "filenames": [
      "logs/workers/worker_paper_appendix_nve_sensitivity_table_20260515T183716.log",
      "logs/workers/worker_paper_appendix_nve_sensitivity_table_20260515T183716_result.json",
      "logs/workers/worker_paper_appendix-task-b1_20260515T195419.log",
      "logs/workers/worker_paper_appendix-task-b1_20260515T195419_result.json",
      "logs/workers/worker_paper_appendix-auroc-revert_20260517T130453.log",
      "logs/workers/worker_paper_appendix-auroc-revert_20260517T130453_result.json",
      "logs/workers/worker_paper_021-appendix-table_20260517T234234.log",
      "logs/workers/worker_paper_021-appendix-table_20260517T234234_result.json",
      "logs/workers/worker_paper_c6-results-appendix-detector_20260518T113449.log",
      "logs/workers/worker_fix_appendix-eval-data_20260524T021344.log",
      "logs/workers/worker_fix_appendix-eval-data_20260524T021344_result.json",
      "docs/paper/sections/appendix.tex"
    ],
    "durationMs": 50,
    "numFiles": 12,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 22_

<details open><summary>🔧 Tool call — Glob · `toolu_0194WLRkwQsnP4nMJsbf7qT8`</summary>

```json
{
  "pattern": "**/*paper*",
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
  "session_id": "72aab3fa-ba3f-48a9-9029-1cec279461d0",
  "uuid": "e8c0d3d3-aa84-47d8-bd48-94f73a55c593",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WPC8vbtWJZmhL5uC9n9AY2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7502,
      "cache_read_input_tokens": 24714,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7502
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

_source line 23 · 2026-05-25T13:46:19.654Z_

<details><summary>↩ Tool result · `toolu_0194WLRkwQsnP4nMJsbf7qT8`</summary>

```text
logs/workers/worker_research_verify-papers_20260513T095035.log
logs/workers/worker_research_verify-papers_20260513T095035_result.json
logs/workers/worker_research_paper_framing_draft_20260514T040752.log
logs/workers/worker_research_paper_framing_draft_20260514T040752_result.json
logs/workers/worker_knowledge_paper_framing_update_20260514T041811.log
logs/workers/worker_knowledge_paper_framing_update_20260514T041811_result.json
artifacts/dream_reports/dream_20260514T062606/best/paper_framing.md
artifacts/dream_reports/dream_20260514T062606/best/paper.tex
artifacts/dream_reports/dream_20260514T062606/best/paper.aux
artifacts/dream_reports/dream_20260514T062606/best/paper.out
artifacts/dream_reports/dream_20260514T062606/best/paper.pdf
artifacts/dream_reports/dream_20260514T062606/best/paper.log
artifacts/dream_reports/dream_20260514T062606/logs/paper_agent_best.log
artifacts/dream_reports/dream_20260514T062606/median/paper_framing.md
artifacts/dream_reports/dream_20260514T062606/median/paper.tex
artifacts/dream_reports/dream_20260514T062606/median/paper.aux
artifacts/dream_reports/dream_20260514T062606/median/paper.out
artifacts/dream_reports/dream_20260514T062606/median/paper.pdf
artifacts/dream_reports/dream_20260514T062606/median/paper.log
artifacts/dream_reports/dream_20260514T062606/logs/paper_agent_median.log
artifacts/dream_reports/dream_20260514T062606/worst/paper_framing.md
artifacts/dream_reports/dream_20260514T062606/worst/paper.aux
artifacts/dream_reports/dream_20260514T062606/worst/paper.out
artifacts/dream_reports/dream_20260514T062606/worst/paper.pdf
artifacts/dream_reports/dream_20260514T062606/worst/paper.log
artifacts/dream_reports/dream_20260514T062606/logs/paper_agent_worst.log
logs/workers/worker_viz_paper-figures-wave1_20260514T094404.log
logs/chats/worker_viz_paper-figures-wave1_20260514T094404.lock
logs/chats/worker_viz_paper-figures-wave1_20260514T094404.jsonl
logs/workers/worker_viz_paper-figures-wave1_20260514T094404_result.json
artifacts/_project/data/paper_data_walker_walk_index.md
artifacts/_project/data/paper_figure_data_summary.txt
logs/workers/worker_analysis_paper-figure-data_20260514T185842.log
logs/workers/worker_analysis_paper-figure-data_20260514T185842_result.json
logs/workers/worker_fix_paper-figure-data-labels_20260514T193445.log
logs/workers/worker_fix_paper-figure-data-labels_20260514T193445_result.json
logs/workers/worker_fix_extract-paper-data-config_20260514T194737.log
logs/workers/worker_fix_extract-paper-data-config_20260514T194737_result.json
logs/workers/worker_research_paper-literature-prep_20260515T011405.log
logs/chats/worker_research_paper-literature-prep_20260515T011405.lock
logs/chats/worker_research_paper-literature-prep_20260515T011405.jsonl
logs/workers/worker_research_paper-literature-prep_20260515T011405_result.json
logs/workers/worker_research_paper-plan_20260515T011527.log
logs/chats/worker_research_paper-plan_20260515T011527.lock
logs/chats/worker_research_paper-plan_20260515T011527.jsonl
logs/workers/worker_research_paper-plan_20260515T011527_result.json
artifacts/dream_reports/dream_20260515T004704/best/paper_framing.md
artifacts/dream_reports/dream_20260515T004704/best/paper.tex
artifacts/dream_reports/dream_20260515T004704/best/paper.aux
artifacts/dream_reports/dream_20260515T004704/best/paper.out
artifacts/dream_reports/dream_20260515T004704/best/paper.pdf
artifacts/dream_reports/dream_20260515T004704/best/paper.log
artifacts/dream_reports/dream_20260515T004704/logs/paper_agent_best.log
artifacts/dream_reports/dream_20260515T004704/median/paper_framing.md
artifacts/dream_reports/dream_20260515T004704/median/paper.tex
artifacts/dream_reports/dream_20260515T004704/median/paper.aux
artifacts/dream_reports/dream_20260515T004704/median/paper.out
artifacts/dream_reports/dream_20260515T004704/median/paper.pdf
artifacts/dream_reports/dream_20260515T004704/median/paper.log
artifacts/dream_reports/dream_20260515T004704/logs/paper_agent_median.log
artifacts/dream_reports/dream_20260515T004704/worst/paper_framing.md
artifacts/dream_reports/dream_20260515T004704/worst/paper.tex
artifacts/dream_reports/dream_20260515T004704/worst/paper.aux
artifacts/dream_reports/dream_20260515T004704/worst/paper.out
artifacts/dream_reports/dream_20260515T004704/worst/paper.pdf
artifacts/dream_reports/dream_20260515T004704/worst/paper.log
artifacts/dream_reports/dream_20260515T004704/logs/paper_agent_worst.log
logs/workers/worker_research_paper-figure-prep_20260515T043852.log
logs/chats/worker_research_paper-figure-prep_20260515T043852.lock
logs/chats/worker_research_paper-figure-prep_20260515T043852.jsonl
logs/workers/worker_research_paper-figure-prep_20260515T043852_result.json
logs/chats/feishu_group_oc_e03655bc885f99dd8e838011bc2fffbb_paper_agent.lock
logs/workers/worker_paper_figure_fig6_multiple_pathways_20260515T064149.log
logs/chats/worker_paper_figure_fig6_multiple_pathways_20260515T064149.lock
logs/chats/worker_paper_figure_fig6_multiple_pathways_20260515T064149.jsonl
logs/workers/worker_paper_figure_fig6_multiple_pathways_20260515T064149_result.json
logs/workers/worker_paper_figure_fig1_learning_curves_20260515T070014.log
logs/workers/worker_paper_figure_fig1_learning_curves_20260515T070014_result.json
logs/workers/worker_paper_figure_fix-fig1-008e_v3-two-seeds_20260515T070324.log
logs/workers/worker_paper_figure_fix-fig1-008e_v3-two-seeds_20260515T070324_result.json
logs/workers/worker_paper_figure_fig5_dt_amplification_20260515T101813.log
logs/chats/worker_paper_figure_fig5_dt_amplification_20260515T101813.lock
logs/chats/worker_paper_figure_fig5_dt_amplification_20260515T101813.jsonl
logs/workers/worker_paper_figure_fig5_dt_amplification_20260515T101813_result.json
logs/workers/worker_paper_figure_fig5_dt_amplification_fix_20260515T102339.log
logs/chats/worker_paper_figure_fig5_dt_amplification_fix_20260515T102339.lock
logs/chats/worker_paper_figure_fig5_dt_amplification_fix_20260515T102339.jsonl
logs/workers/worker_paper_figure_fig5_dt_amplification_fix_20260515T102339_result.json
logs/workers/worker_paper_figure_fig2_nve_trajectory_20260515T102507.log
logs/chats/worker_paper_figure_fig2_nve_trajectory_20260515T102507.lock
logs/chats/worker_paper_figure_fig2_nve_trajectory_20260515T102507.jsonl
logs/workers/worker_paper_figure_fig2_nve_trajectory_20260515T102507_result.json
logs/workers/worker_paper_figure_fig2_nve_complete_20260515T105046.log
logs/chats/worker_paper_figure_fig2_nve_complete_20260515T105046.lock
logs/chats/worker_paper_figure_fig2_nve_complete_20260515T105046.jsonl
logs/workers/worker_paper_figure_fig2_nve_complete_20260515T105046_result.json
paper_provenance.lock
logs/workers/worker_paper_figure_fig2_three_fixes_20260515T111131.log
logs/workers/worker_paper_figure_fig2_three_fixes_20260515T111131_result.json
logs/workers/worker_paper_figure_fig2_force_fix_20260515T111647.log
(Results are truncated. Consider using a more specific path or pattern.)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "72aab3fa-ba3f-48a9-9029-1cec279461d0",
  "uuid": "29461bba-a3e7-4c63-b571-cf4a6ba8dd4c",
  "tool_use_result": {
    "filenames": [
      "logs/workers/worker_research_verify-papers_20260513T095035.log",
      "logs/workers/worker_research_verify-papers_20260513T095035_result.json",
      "logs/workers/worker_research_paper_framing_draft_20260514T040752.log",
      "logs/workers/worker_research_paper_framing_draft_20260514T040752_result.json",
      "logs/workers/worker_knowledge_paper_framing_update_20260514T041811.log",
      "logs/workers/worker_knowledge_paper_framing_update_20260514T041811_result.json",
      "artifacts/dream_reports/dream_20260514T062606/best/paper_framing.md",
      "artifacts/dream_reports/dream_20260514T062606/best/paper.tex",
      "artifacts/dream_reports/dream_20260514T062606/best/paper.aux",
      "artifacts/dream_reports/dream_20260514T062606/best/paper.out",
      "artifacts/dream_reports/dream_20260514T062606/best/paper.pdf",
      "artifacts/dream_reports/dream_20260514T062606/best/paper.log",
      "artifacts/dream_reports/dream_20260514T062606/logs/paper_agent_best.log",
      "artifacts/dream_reports/dream_20260514T062606/median/paper_framing.md",
      "artifacts/dream_reports/dream_20260514T062606/median/paper.tex",
      "artifacts/dream_reports/dream_20260514T062606/median/paper.aux",
      "artifacts/dream_reports/dream_20260514T062606/median/paper.out",
      "artifacts/dream_reports/dream_20260514T062606/median/paper.pdf",
      "artifacts/dream_reports/dream_20260514T062606/median/paper.log",
      "artifacts/dream_reports/dream_20260514T062606/logs/paper_agent_median.log",
      "artifacts/dream_reports/dream_20260514T062606/worst/paper_framing.md",
      "artifacts/dream_reports/dream_20260514T062606/worst/paper.aux",
      "artifacts/dream_reports/dream_20260514T062606/worst/paper.out",
      "artifacts/dream_reports/dream_20260514T062606/worst/paper.pdf",
      "artifacts/dream_reports/dream_20260514T062606/worst/paper.log",
      "artifacts/dream_reports/dream_20260514T062606/logs/paper_agent_worst.log",
      "logs/workers/worker_viz_paper-figures-wave1_20260514T094404.log",
      "logs/chats/worker_viz_paper-figures-wave1_20260514T094404.lock",
      "logs/chats/worker_viz_paper-figures-wave1_20260514T094404.jsonl",
      "logs/workers/worker_viz_paper-figures-wave1_20260514T094404_result.json",
      "artifacts/_project/data/paper_data_walker_walk_index.md",
      "artifacts/_project/data/paper_figure_data_summary.txt",
      "logs/workers/worker_analysis_paper-figure-data_20260514T185842.log",
      "logs/workers/worker_analysis_paper-figure-data_20260514T185842_result.json",
      "logs/workers/worker_fix_paper-figure-data-labels_20260514T193445.log",
      "logs/workers/worker_fix_paper-figure-data-labels_20260514T193445_result.json",
      "logs/workers/worker_fix_extract-paper-data-config_20260514T194737.log",
      "logs/workers/worker_fix_extract-paper-data-config_20260514T194737_result.json",
      "logs/workers/worker_research_paper-literature-prep_20260515T011405.log",
      "logs/chats/worker_research_paper-literature-prep_20260515T011405.lock",
      "logs/chats/worker_research_paper-literature-prep_20260515T011405.jsonl",
      "logs/workers/worker_research_paper-literature-prep_20260515T011405_result.json",
      "logs/workers/worker_research_paper-plan_20260515T011527.log",
      "logs/chats/worker_research_paper-plan_20260515T011527.lock",
      "logs/chats/worker_research_paper-plan_20260515T011527.jsonl",
      "logs/workers/worker_research_paper-plan_20260515T011527_result.json",
      "artifacts/dream_reports/dream_20260515T004704/best/paper_framing.md",
      "artifacts/dream_reports/dream_20260515T004704/best/paper.tex",
      "artifacts/dream_reports/dream_20260515T004704/best/paper.aux",
      "artifacts/dream_reports/dream_20260515T004704/best/paper.out",
      "artifacts/dream_reports/dream_20260515T004704/best/paper.pdf",
      "artifacts/dream_reports/dream_20260515T004704/best/paper.log",
      "artifacts/dream_reports/dream_20260515T004704/logs/paper_agent_best.log",
      "artifacts/dream_reports/dream_20260515T004704/median/paper_framing.md",
      "artifacts/dream_reports/dream_20260515T004704/median/paper.tex",
      "artifacts/dream_reports/dream_20260515T004704/median/paper.aux",
      "artifacts/dream_reports/dream_20260515T004704/median/paper.out",
      "artifacts/dream_reports/dream_20260515T004704/median/paper.pdf",
      "artifacts/dream_reports/dream_20260515T004704/median/paper.log",
      "artifacts/dream_reports/dream_20260515T004704/logs/paper_agent_median.log",
      "artifacts/dream_reports/dream_20260515T004704/worst/paper_framing.md",
      "artifacts/dream_reports/dream_20260515T004704/worst/paper.tex",
      "artifacts/dream_reports/dream_20260515T004704/worst/paper.aux",
      "artifacts/dream_reports/dream_20260515T004704/worst/paper.out",
      "artifacts/dream_reports/dream_20260515T004704/worst/paper.pdf",
      "artifacts/dream_reports/dream_20260515T004704/worst/paper.log",
      "artifacts/dream_reports/dream_20260515T004704/logs/paper_agent_worst.log",
      "logs/workers/worker_research_paper-figure-prep_20260515T043852.log",
      "logs/chats/worker_research_paper-figure-prep_20260515T043852.lock",
      "logs/chats/worker_research_paper-figure-prep_20260515T043852.jsonl",
      "logs/workers/worker_research_paper-figure-prep_20260515T043852_result.json",
      "logs/chats/feishu_group_oc_e03655bc885f99dd8e838011bc2fffbb_paper_agent.lock",
      "logs/workers/worker_paper_figure_fig6_multiple_pathways_20260515T064149.log",
      "logs/chats/worker_paper_figure_fig6_multiple_pathways_20260515T064149.lock",
      "logs/chats/worker_paper_figure_fig6_multiple_pathways_20260515T064149.jsonl",
      "logs/workers/worker_paper_figure_fig6_multiple_pathways_20260515T064149_result.json",
      "logs/workers/worker_paper_figure_fig1_learning_curves_20260515T070014.log",
      "logs/workers/worker_paper_figure_fig1_learning_curves_20260515T070014_result.json",
      "logs/workers/worker_paper_figure_fix-fig1-008e_v3-two-seeds_20260515T070324.log",
      "logs/workers/worker_paper_figure_fix-fig1-008e_v3-two-seeds_20260515T070324_result.json",
      "logs/workers/worker_paper_figure_fig5_dt_amplification_20260515T101813.log",
      "logs/chats/worker_paper_figure_fig5_dt_amplification_20260515T101813.lock",
      "logs/chats/worker_paper_figure_fig5_dt_amplification_20260515T101813.jsonl",
      "logs/workers/worker_paper_figure_fig5_dt_amplification_20260515T101813_result.json",
      "logs/workers/worker_paper_figure_fig5_dt_amplification_fix_20260515T102339.log",
      "logs/chats/worker_paper_figure_fig5_dt_amplification_fix_20260515T102339.lock",
      "logs/chats/worker_paper_figure_fig5_dt_amplification_fix_20260515T102339.jsonl",
      "logs/workers/worker_paper_figure_fig5_dt_amplification_fix_20260515T102339_result.json",
      "logs/workers/worker_paper_figure_fig2_nve_trajectory_20260515T102507.log",
      "logs/chats/worker_paper_figure_fig2_nve_trajectory_20260515T102507.lock",
      "logs/chats/worker_paper_figure_fig2_nve_trajectory_20260515T102507.jsonl",
      "logs/workers/worker_paper_figure_fig2_nve_trajectory_20260515T102507_result.json",
      "logs/workers/worker_paper_figure_fig2_nve_complete_20260515T105046.log",
      "logs/chats/worker_paper_figure_fig2_nve_complete_20260515T105046.lock",
      "logs/chats/worker_paper_figure_fig2_nve_complete_20260515T105046.jsonl",
      "logs/workers/worker_paper_figure_fig2_nve_complete_20260515T105046_result.json",
      "paper_provenance.lock",
      "logs/workers/worker_paper_figure_fig2_three_fixes_20260515T111131.log",
      "logs/workers/worker_paper_figure_fig2_three_fixes_20260515T111131_result.json",
      "logs/workers/worker_paper_figure_fig2_force_fix_20260515T111647.log"
    ],
    "durationMs": 40,
    "numFiles": 100,
    "truncated": true
  }
}
```

</details>

---

### Tool call

_source line 24_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01A3g3wDf9ou2mT5RqoqjuVU`</summary>

```json
{
  "project": "event-gated-adaptive-horizon",
  "filters": {
    "conclusion": "success"
  },
  "limit": 20,
  "fields": [
    "status",
    "conclusion",
    "hypothesis",
    "updated_at",
    "metrics"
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
  "session_id": "72aab3fa-ba3f-48a9-9029-1cec279461d0",
  "uuid": "ff3fbc93-3a36-4ff7-9e2d-2c2d1b84c62c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WPC8vbtWJZmhL5uC9n9AY2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7502,
      "cache_read_input_tokens": 24714,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7502
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

_source line 25 · 2026-05-25T13:46:21.475Z_

<details><summary>↩ Tool result · `toolu_01A3g3wDf9ou2mT5RqoqjuVU`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"exp_074_008a_walker_s3\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-25T12:08:22.221Z\", \"hypothesis\": \"Walker Walk 008a 配置 (trained dt_emb unexposed + subsample OFF + dt=2 + H=15) seed=3。当前 008a 3 seeds 全部 success (no CIVO)，加 seed=3 巩固 C3 value suppression claim 统计。来源: plan_013 扩展。\", \"conclusion\": \"success\", \"metrics\": {\"eval_return_105K\": 855.9, \"civo_ve_ratio_final\": 0.3, \"civo_alert\": 0, \"value_mean_105K\": 295.2, \"gate_dt_2_frac\": 1, \"gate_dt_mean\": 2, \"model_loss_105K\": 3.8, \"eval_trajectory\": {\"5K\": 36.1, \"15K\": 281, \"25K\": 389.8, \"35K\": 303.8, \"45K\": 437.3, \"55K\": 411.3, \"65K\": 566.4, \"75K\": 513.9, \"85K\": 645.9, \"95K\": 776.6, \"105K\": 855.9}, \"four_seed_summary\": {\"mean_eval_return\": 791, \"std_eval_return\": 102.2, \"all_civo_alert_0\": true, \"seeds_completed\": 4}}}, \"exp_071_008f_walker_s3\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-25T10:42:39.889Z\", \"hypothesis\": \"Walker Walk 008f 配置 (no dt_emb, dt_embed_dim=0 + subsample ON + dt=2 + H=8) seed=3。当前 008f 2 seeds 结果分歧（s1=success eval=503, s2=negative eval=148），增加 seed 缩窄 causal control 稳定性估计。来源: plan_012 扩展。\", \"conclusion\": \"success\", \"metrics\": {\"eval_return_final\": 311.9, \"eval_return_peak\": 457.7, \"ve_ratio_final\": 0.4, \"ve_ratio_peak\": 0.7, \"gate_dt_mean_final\": 2, \"civo_alert\": 0, \"value_loss_final\": 1, \"actor_entropy_final\": -4.6, \"model_loss_final\": 4.5}}, \"exp_073_008f_walker_s4\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-25T10:00:42.604Z\", \"hypothesis\": \"Walker Walk 008f 配置 (no dt_emb, dt_embed_dim=0 + subsample ON + dt=2 + H=8) seed=4。当前 008f 0/3 CIVO onset，扩到 seed=4 进一步巩固 control 组统计。来源: plan_012 扩展。\", \"conclusion\": \"success\", \"metrics\": {\"eval_return_final\": 289.3, \"eval_return_peak\": 486.5, \"eval_return_peak_step\": 75000, \"ve_ratio_final\": 0.5, \"ve_ratio_peak\": 0.5, \"nve_peak\": 0.76, \"civo_alert\": 0, \"civo\": false, \"gate_dt_2_frac\": 1, \"gate_dt_mean\": 2, \"gate_empirical_entropy\": 0, \"eval_trajectory\": [{\"step\": 5000, \"eval_return\": 33.2}, {\"step\": 15000, \"eval_return\": 128.3}, {\"step\": 25000, \"eval_return\": 165.3}, {\"step\": 35000, \"eval_return\": 284.5}, {\"step\": 45000, \"eval_return\": 272.5}, {\"step\": 55000, \"eval_return\": 406.7}, {\"step\": 65000, \"eval_return\": 379.5}, {\"step\": 75000, \"eval_return\": 486.5}, {\"step\": 85000, \"eval_return\": 352.6}, {\"step\": 95000, \"eval_return\": 297.7}, {\"step\": 105000, \"eval_return\": 289.3}]}}, \"exp_072_008e_v3_walker_s5\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-25T10:00:39.306Z\", \"hypothesis\": \"Walker Walk 008e_v3 mitigation 配置 (trained dt_emb + subsample ON + dt=1 imag + H=15) seed=5。当前 5 seeds 测试 collapse rate=2/5 (40%)，加 seed=5 缩窄置信区间。来源: plan_016 扩展。\", \"conclusion\": \"success\", \"metrics\": {\"eval_return_final\": 853.1, \"eval_return_peak\": 853.1, \"eval_return_peak_step\": 105000, \"ve_ratio_final\": 0.6, \"nve_final\": 0.61, \"nve_peak\": 0.61, \"nve_peak_step\": 105000, \"civo_alert\": 0, \"civo\": false, \"gate_dt_1_frac\": 1, \"gate_dt_mean\": 1, \"actor_entropy_final\": -5.1, \"value_mean_final\": 520.8, \"eval_trajectory\": [{\"step\": 5000, \"eval_return\": 29.4}, {\"step\": 15000, \"eval_return\": 251.1}, {\"step\": 25000, \"eval_return\": 423}, {\"step\": 35000, \"eval_return\": 511}, {\"step\": 45000, \"eval_return\": 600.1}, {\"step\": 55000, \"eval_return\": 649}, {\"step\": 65000, \"eval_return\": 697.2}, {\"step\": 75000, \"eval_return\": 727.3}, {\"step\": 85000, \"eval_return\": 710.3}, {\"step\": 95000, \"eval_return\": 803.9}, {\"step\": 105000, \"eval_return\": 853.1}]}}, \"exp_069_008f_walker_repro_s1\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-25T07:28:33.676Z\", \"hypothesis\": \"Reproducing 008f config (no dt_emb, dt_embed_dim=0 + subsample ON + dt=2 + H=8) on Walker Walk seed=1 will NOT trigger CIVO (NVE < 1.5x) because removing dt_emb eliminates the temporal abstraction mismatch that drives value error amplification\", \"metrics\": {\"eval_return_final\": 237.8, \"eval_return_peak\": 390.1, \"eval_return_peak_step\": 95000, \"ve_ratio_final\": 0.4, \"ve_ratio_peak\": 0.4, \"ve_ratio_peak_step\": 105000, \"nve_final_105k\": 0.61, \"nve_peak\": 0.66, \"nve_peak_step\": 75000, \"civo_alert\": false, \"gate_dt_2_frac\": 1, \"eval_trajectory\": {\"5k\": 30.5, \"15k\": 158.7, \"25k\": 180.8, \"35k\": 250.3, \"45k\": 293.6, \"55k\": 272.2, \"65k\": 328.1, \"75k\": 244.8, \"85k\": 382.5, \"95k\": 390.1, \"105k\": 237.8}, \"ve_ratio_trajectory\": {\"15k\": 0, \"25k\": 0.1, \"35k\": 0.2, \"45k\": 0.2, \"55k\": 0.3, \"65k\": 0.3, \"75k\": 0.4, \"85k\": 0.3, \"95k\": 0.3, \"105k\": 0.4}}, \"conclusion\": \"success\"}, \"exp_068_008d_walker_repro_s1\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-25T07:28:31.319Z\", \"hypothesis\": \"Reproducing 008d config (trained dt_emb + subsample ON + dt=2 + H=8) on Walker Walk seed=1 will trigger CIVO (NVE > 1.5x) because trained dt_emb enables value error amplification through temporal abstraction mismatch\", \"metrics\": {\"eval_return_final\": 39.1, \"eval_return_peak\": 192.4, \"eval_return_peak_step\": 55000, \"ve_ratio_final\": 2.7, \"ve_ratio_peak\": 4.6, \"ve_ratio_peak_step\": 85000, \"nve_final_105k\": 4.12, \"nve_peak_85k\": 6.57, \"nve_onset_step\": 45000, \"nve_onset_value\": 1.81, \"civo_alert\": true, \"civo_alert_step\": 85000, \"gate_dt_2_frac\": 1, \"eval_trajectory\": {\"5k\": 31, \"15k\": 146.5, \"25k\": 174.1, \"35k\": 189.6, \"45k\": 142.2, \"55k\": 192.4, \"65k\": 114.4, \"75k\": 106.6, \"85k\": 33.4, \"95k\": 26.9, \"105k\": 39.1}, \"ve_ratio_trajectory\": {\"15k\": 0, \"25k\": 0.2, \"35k\": 0.3, \"45k\": 0.6, \"55k\": 0.6, \"65k\": 1.3, \"75k\": 1.6, \"85k\": 4.6, \"95k\": 4.6, \"105k\": 2.7}}, \"conclusion\": \"success\"}, \"exp_067_frozen_dt_emb_walker_plan015\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-25T06:59:24.006Z\", \"hypothesis\": \"Frozen (requires_grad=False) dt_embedding + subsample ON + dt=2 + H=8 在 Walker Walk 上不触发 CIVO，验证 dt_emb 的 TRAINING 是 CIVO 的必要条件（而非 dt_emb 的存在本身）。来源: plan_015。\", \"metrics\": {\"eval_final\": 281.5, \"eval_peak\": 334.1, \"eval_peak_step\": 95000, \"nve_peak\": 0.4, \"nve_final\": 0.2, \"civo_alert\": 0, \"total_env_steps\": 112000, \"update_count\": 25099, \"gate_dt_mean\": 2, \"gate_dt_std\": 0, \"gate_dt_2_frac\": 1, \"gate_empirical_entropy\": 0}, \"conclusion\": \"success\"}, \"exp_066b_timeseries_rssm_fidelity_s1\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-25T04:35:12.673Z\", \"hypothesis\": \"RSSM fidelity gap (dt=2 prediction error > dt=1) emerges before value overestimation in seed=1, replicating the causal chain found in exp_066 seed=0 and confirming cross-seed robustness of the fidelity→VE mechanism.\", \"metrics\": {\"seed\": 1, \"steps_completed\": 65000, \"eval_return_peak\": 201.9, \"eval_return_peak_step\": 45000, \"eval_return_final\": 160.7, \"civo_alert_step\": 55000, \"ve_ratio_final\": 0.724, \"fidelity_gap_timeseries\": {\"ss_ratio_10K\": 0.887, \"ss_ratio_15K\": 1.017, \"ss_ratio_20K\": 1.216, \"ss_ratio_25K\": 1.532, \"ss_ratio_30K\": 1.374, \"ss_ratio_35K\": 1.486, \"ss_ratio_40K\": 1.428, \"ss_ratio_45K\": 1.38, \"ss_ratio_50K\": 1.468, \"ss_ratio_55K\": 1.517, \"ss_ratio_60K\": 1.799, \"ss_ratio_65K\": 1.756}, \"ve_ratio_timeseries\": {\"12K\": 0.012, \"15K\": 0.033, \"24K\": 0.118, \"25K\": 0.193, \"35K\": 0.269, \"45K\": 0.358, \"52K\": 0.495, \"55K\": 0.71, \"64K\": 0.724}, \"fidelity_gap_onset_step\": 15000, \"ve_onset_step\": 24000, \"temporal_lead_steps\": 9000, \"causal_direction\": \"fidelity_gap_leads_ve\", \"cross_seed_comparison\": {\"s0_ss_ratio_65K\": 1.678, \"s1_ss_ratio_65K\": 1.756, \"s0_fidelity_onset\": 20000, \"s1_fidelity_onset\": 15000, \"s0_ve_onset\": 30000, \"s1_ve_onset\": 24000, \"s0_temporal_lead\": 10000, \"s1_temporal_lead\": 9000, \"pattern_consistent\": true}}, \"conclusion\": \"success\"}, \"exp_008d_subsample_on_h8\": {\"conclusion\": \"success\", \"hypothesis\": \"Trained dt-embedding with subsample (gate_fixed_dt=2, gate_subsample_max_dt=2) causes critic value function to overestimate through dt-conditioned representation co-adaptation, leading to policy collapse.\", \"metrics\": {\"actor_loss_25K\": -0.195, \"actor_loss_35K\": -0.17, \"baseline_35K\": 400, \"baseline_45K\": 443, \"data_source_45K\": \"from training logs metrics.jsonl\", \"eval_return_25K\": 167.22, \"eval_return_35K\": 146.34, \"eval_return_45K\": 140.8, \"eval_return_55K\": 82.75, \"model_loss_25K\": 5.33, \"model_loss_35K\": 5.07, \"step\": 55000, \"trend\": \"eval declining 167→146→141→83; v/e accelerating 15.5%→41.2%→69.3%→167% — delusional critic collapse confirmed, value exceeds eval_return at 55K\", \"value_eval_ratio_25K\": 0.155, \"value_eval_ratio_35K\": 0.411, \"value_eval_ratio_45K\": 0.693, \"value_eval_ratio_55K\": 1.666, \"value_mean_25K\": 25.86, \"value_mean_35K\": 60.2, \"value_mean_45K\": 97.5, \"value_mean_55K\": 137.88, \"verdict_35K\": \"WARN_COLLAPSE\", \"verdict_45K\": \"COLLAPSE_CONFIRMED\", \"vs_baseline_35K\": \"-63.4%\", \"vs_baseline_45K\": \"-68.2%\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-25T02:41:05.620Z\"}, \"exp_066_timeseries_rssm_fidelity\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-25T02:33:00.783Z\", \"hypothesis\": \"Trained dt_embedding causes RSSM fidelity degradation (dt=2 vs dt=1 reward MAE gap) that progressively worsens during training, and its temporal evolution precedes or synchronizes with NVE (value overestimation) rise, establishing a temporal causal chain: RSSM fidelity gap → value overestimation.\", \"conclusion\": \"success\", \"metrics\": {\"ss_ratio_10K\": 1.047, \"ss_ratio_30K\": 1.247, \"ss_ratio_65K\": 1.678, \"ol_ratio_30K_peak\": 1.446, \"ol_ratio_35K_peak\": 1.509, \"ve_ratio_final\": 1.399, \"fidelity_gap_onset_step\": 20000, \"ve_onset_step\": 30000, \"temporal_lead_steps\": 10000, \"pearson_ss_ve\": 0.807, \"pearson_ss_ve_p\": 0.0015, \"pearson_ol_ve\": 0.425, \"pearson_ol_ve_p\": 0.169, \"ss_monotonicity\": 0.73, \"ol_monotonicity\": 0.73, \"ve_monotonicity\": 0.82, \"causal_direction\": \"fidelity_gap_leads_ve\", \"conclusion\": \"success\"}}, \"exp_060_cartpole_baseline\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-25T01:25:39.711Z\", \"hypothesis\": \"Cartpole Swingup (DMC) baseline dt=1 建立 v/e ratio 校准基线，用于 CIVO 诊断阈值在第三个 DMC 环境的验证。预期 NVE 保持在 1.0x 附近，无 CIVO 现象。\", \"conclusion\": \"success\", \"metrics\": {\"seeds\": 3, \"steps_per_seed\": 112000, \"train_return_s0\": 809.4, \"train_return_s1\": 684.4, \"train_return_s2\": 526.1, \"eval_return_s2_105K\": 557}}, \"exp_065_dt_emb_cosine\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-24T20:54:51.678Z\", \"hypothesis\": \"分析 trained dt_embedding 中 dt=1 vs dt=2 向量的 cosine similarity 及其训练过程演化。如果 cosine sim 高（接近 1）→ dt_emb 未学到有意义区分，CIVO 来自微小差异被 downstream 放大；如果 cosine sim 低 → dt_emb 学到了显著不同的表征，CIVO 来自 dt=2 表征本身的偏差。\", \"conclusion\": \"success\", \"metrics\": {\"trained_cosine_sim_range\": \"-0.94 to -0.70\", \"frozen_cosine_sim_range\": \"-0.15 to +0.07\", \"trained_trend\": \"strong negative (near-opposite directions)\", \"frozen_trend\": \"near-zero constant\", \"conclusion\": \"dt=1 and dt=2 embeddings learn nearly opposite representations; CIVO from dt=2 representation bias, not amplified micro-differences\"}}, \"exp_064_value_distribution\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-24T20:14:50.460Z\", \"hypothesis\": \"V(s) vs Monte Carlo return 分布对比：trained dt_emb (exp_008d collapsed) 的 value estimate 在 dt=2 imagination 步骤系统性高估，而 untrained/absent dt_emb (exp_008f control) 和 baseline (exp_001) 的 value 分布与 MC return 紧密跟踪。直观展示 CIVO 的 value divergence 位置和形态。\", \"conclusion\": \"success\", \"metrics\": {\"baseline_bias\": 344.85, \"baseline_rmse\": 371.73, \"baseline_overest_pct\": 100, \"baseline_v_mc_ratio\": 3.31, \"civo_bias\": 108.99, \"civo_rmse\": 112.36, \"civo_overest_pct\": 100, \"civo_v_mc_ratio\": 7.8, \"civo_v_mc_median\": 3.4, \"control_bias\": -6.51, \"control_rmse\": 57.93, \"control_overest_pct\": 52.5, \"control_v_mc_ratio\": 2.58, \"control_v_mc_median\": 1.05}}, \"exp_063_rssm_fidelity\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-24T19:21:37.837Z\", \"hypothesis\": \"RSSM 在 dt=2 transitions 上的 observation/reward reconstruction loss 显著高于 dt=1，量化 fidelity gap 作为 trained dt_emb 导致 delusional critic 的机械性基础。从 exp_001 (baseline) 和 exp_008d (collapsed) 的已有 checkpoint 提取，对比 dt=1 vs dt=2 prediction quality。\", \"conclusion\": \"success\", \"metrics\": {\"baseline_dt1_obs_mse\": 13.7, \"baseline_dt2_obs_mse\": 20.62, \"baseline_dt2_dt1_ratio_obs\": 1.505, \"baseline_dt2_dt1_ratio_reward\": 1.483, \"collapsed_dt1_obs_mse\": 26.93, \"collapsed_dt2_single_obs_mse\": 42.02, \"collapsed_dt2_single_reward_mae\": 0.146, \"collapsed_dt2_dt1_ratio_obs\": 1.56, \"collapsed_dt2_dt1_ratio_reward\": 2.695, \"collapsed_single_vs_chained_obs\": 1.138, \"collapsed_single_vs_chained_reward\": 1.926}}, \"exp_049_stackcube_civo_trigger_s0\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-24T16:53:19.032Z\", \"hypothesis\": \"CIVO trigger 配置（trained dt_emb + subsample ON + H=8）在 ManiSkill StackCube-v1 manipulation 任务上是否也触发 CIVO。测试 CIVO 是否从 locomotion 推广到 manipulation 领域。StackCube 是多阶段任务（pick+stack）。如果触发 → 扩展跨域证据；如果不触发 → 支持 locomotion-specific scope。\", \"metrics\": {\"eval_final\": 34.88, \"eval_final_step\": 212500, \"eval_peak\": 35.89, \"eval_peak_step\": 182500, \"ve_ratio_final\": 0.186, \"ve_ratio_final_step\": 212500, \"ve_ratio_peak\": 5.048, \"ve_ratio_peak_step\": 42500, \"total_steps\": 222400, \"total_episodes\": 1112, \"nve_classification\": \"onset_self_correcting\", \"civo_transient\": true, \"civo_sustained\": false, \"civo_transient_range\": \"22K-72K\", \"civo_self_correction\": true, \"civo_self_correction_step\": 112500, \"gate_dt_mean\": 2, \"gate_dt_variation\": false, \"eval_dip_during_civo\": 4.93, \"eval_dip_step\": 62500}, \"conclusion\": \"success\"}, \"exp_057\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-24T16:50:44.968Z\", \"hypothesis\": \"Frozen dt_emb 跨 seed 可复现性验证（Walker seed=2, n=3）。当前 Walker frozen s0 NVE 0.19, s1 NVE 1.71 transient。s2 增加样本量到 n=3 验证稳健性。\", \"metrics\": {\"eval_return_peak\": 221.7, \"eval_return_peak_step\": 195000, \"eval_return_final\": 123.9, \"eval_return_final_step\": 215000, \"nve_peak\": 1.3, \"nve_peak_step\": 115000, \"nve_final\": 0.2, \"civo_alert\": 0, \"civo_sustained\": false, \"civo_transient\": true, \"civo_transient_range\": \"115k-145k\", \"train_steps\": 225000, \"gate_dt_mean\": 2}, \"conclusion\": \"success\"}, \"exp_008d_civo_trigger_s4\": {\"conclusion\": \"success\", \"hypothesis\": \"Walker Walk CIVO trigger seed=4: trained dt_emb + subsample ON + H=8. 第四 seed 复现 CIVO (NVE>1.5×)，加强 Walker 因果论证的统计力度。Rebuttal 储备。\", \"metrics\": {\"ve_ratio_peak\": 3.0294, \"ve_ratio_peak_step\": 105000, \"ve_ratio_final\": 3.0294, \"ve_ratio_final_step\": 105000, \"nve_peak\": 4.62, \"nve_peak_step\": 105000, \"nve_peak_note\": \"step-matched s1 baseline @105K = 0.6564\", \"nve_classification\": \"onset_collapse\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-24T08:56:41.239Z\"}, \"exp_059_walker_trained_s5\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-24T07:46:59.075Z\", \"hypothesis\": \"Walker CIVO trigger 第5个独立seed验证。当前4/4 seeds触发sustained CIVO（p=0.0625 binomial test）。如果s5也触发 → p=0.03125，达到统计显著性阈值。关联 Claim 1: CIVO reproducibility。\", \"metrics\": {\"ve_ratio_peak\": 3.3075, \"ve_ratio_peak_step\": \"85K\", \"nve_peak\": 4.72, \"nve_peak_note\": \"step-matched s1 baseline @85K = 0.7007\", \"nve_classification\": \"onset_collapse\", \"nve_classification_note\": \"Reclassified from onset_self_correcting: NVE self-corrected but eval=95.8 (10.5% of baseline 913) indicates irreversible policy damage. Collapse†.\", \"nve_final\": 1.22, \"nve_final_note\": \"0.8/0.656 (step-matched s1 baseline @105K)\", \"eval_final\": 95.8, \"eval_baseline\": 913, \"eval_pct_baseline\": \"10.5%\"}, \"conclusion\": \"success\"}, \"exp_057_frozen_dt_emb_walker_s2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"updated_at\": \"2026-05-24T02:17:41.318Z\", \"hypothesis\": \"Frozen dt_emb 跨 seed 可复现性验证（Walker n=3）。当前 Walker frozen s0 NVE 0.19, s1 NVE 1.71 transient。s2 增加样本量到 n=3，如果 0 CIVO → frozen 在 Walker 上稳健；如果出现持续 CIVO → 样本不足。\", \"metrics\": {\"total_steps\": 225000, \"ve_ratio_peak\": 1.283, \"ve_ratio_peak_step\": 115000, \"ve_ratio_final\": 0.177, \"ve_ratio_final_step\": 215000, \"nve_peak\": 1.88, \"nve_peak_step\": 115000, \"nve_classification\": \"transient\", \"eval_return_final\": 123.94, \"eval_return_final_step\": 215000, \"eval_return_peak\": 221.72, \"eval_return_peak_step\": 195000}}, \"exp_058_frozen_dt_emb_cheetah_s1\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-24T00:30:00.000Z\", \"hypothesis\": \"Cheetah frozen dt_emb 跨 seed 可复现性验证。exp_046 (s0) 显示 frozen 将 NVE 从 ~70-108（trained）降至 1.35。s1 验证阻止效应是否可复现。如果 s1 也阻止 → Cheetah frozen n=2 增强极端 CIVO 场景下 frozen diagnostic 的统计基础。\", \"conclusion\": \"success\", \"metrics\": {\"total_steps\": 224000, \"ve_ratio_peak\": 0.231, \"ve_ratio_peak_step\": 45000, \"ve_ratio_final\": 0.107, \"ve_ratio_final_step\": 215000, \"eval_return_final\": 80.46, \"eval_return_final_step\": 215000, \"eval_return_peak\": 191.74, \"eval_return_peak_step\": 25000, \"nve_peak\": 0.78, \"nve_peak_step\": 45000, \"nve_classification\": \"no_civo\", \"note\": \"Cheetah frozen s1. NVE=0.78× (raw 0.231 / baseline 0.296 @45K). Cheetah frozen n=2: s0 NVE=1.35, s1 NVE=0.78 — both clean, frozen 稳健阻止 extreme CIVO (trained NVE 70-108).\"}}}, \"count\": 20, \"total\": 79, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5997}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "72aab3fa-ba3f-48a9-9029-1cec279461d0",
  "uuid": "b7ca0207-a88f-4464-b6c5-e822ab8ea27f",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"exp_074_008a_walker_s3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-25T12:08:22.221Z\\\", \\\"hypothesis\\\": \\\"Walker Walk 008a 配置 (trained dt_emb unexposed + subsample OFF + dt=2 + H=15) seed=3。当前 008a 3 seeds 全部 success (no CIVO)，加 seed=3 巩固 C3 value suppression claim 统计。来源: plan_013 扩展。\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"eval_return_105K\\\": 855.9, \\\"civo_ve_ratio_final\\\": 0.3, \\\"civo_alert\\\": 0, \\\"value_mean_105K\\\": 295.2, \\\"gate_dt_2_frac\\\": 1, \\\"gate_dt_mean\\\": 2, \\\"model_loss_105K\\\": 3.8, \\\"eval_trajectory\\\": {\\\"5K\\\": 36.1, \\\"15K\\\": 281, \\\"25K\\\": 389.8, \\\"35K\\\": 303.8, \\\"45K\\\": 437.3, \\\"55K\\\": 411.3, \\\"65K\\\": 566.4, \\\"75K\\\": 513.9, \\\"85K\\\": 645.9, \\\"95K\\\": 776.6, \\\"105K\\\": 855.9}, \\\"four_seed_summary\\\": {\\\"mean_eval_return\\\": 791, \\\"std_eval_return\\\": 102.2, \\\"all_civo_alert_0\\\": true, \\\"seeds_completed\\\": 4}}}, \\\"exp_071_008f_walker_s3\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-25T10:42:39.889Z\\\", \\\"hypothesis\\\": \\\"Walker Walk 008f 配置 (no dt_emb, dt_embed_dim=0 + subsample ON + dt=2 + H=8) seed=3。当前 008f 2 seeds 结果分歧（s1=success eval=503, s2=negative eval=148），增加 seed 缩窄 causal control 稳定性估计。来源: plan_012 扩展。\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"eval_return_final\\\": 311.9, \\\"eval_return_peak\\\": 457.7, \\\"ve_ratio_final\\\": 0.4, \\\"ve_ratio_peak\\\": 0.7, \\\"gate_dt_mean_final\\\": 2, \\\"civo_alert\\\": 0, \\\"value_loss_final\\\": 1, \\\"actor_entropy_final\\\": -4.6, \\\"model_loss_final\\\": 4.5}}, \\\"exp_073_008f_walker_s4\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-25T10:00:42.604Z\\\", \\\"hypothesis\\\": \\\"Walker Walk 008f 配置 (no dt_emb, dt_embed_dim=0 + subsample ON + dt=2 + H=8) seed=4。当前 008f 0/3 CIVO onset，扩到 seed=4 进一步巩固 control 组统计。来源: plan_012 扩展。\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"eval_return_final\\\": 289.3, \\\"eval_return_peak\\\": 486.5, \\\"eval_return_peak_step\\\": 75000, \\\"ve_ratio_final\\\": 0.5, \\\"ve_ratio_peak\\\": 0.5, \\\"nve_peak\\\": 0.76, \\\"civo_alert\\\": 0, \\\"civo\\\": false, \\\"gate_dt_2_frac\\\": 1, \\\"gate_dt_mean\\\": 2, \\\"gate_empirical_entropy\\\": 0, \\\"eval_trajectory\\\": [{\\\"step\\\": 5000, \\\"eval_return\\\": 33.2}, {\\\"step\\\": 15000, \\\"eval_return\\\": 128.3}, {\\\"step\\\": 25000, \\\"eval_return\\\": 165.3}, {\\\"step\\\": 35000, \\\"eval_return\\\": 284.5}, {\\\"step\\\": 45000, \\\"eval_return\\\": 272.5}, {\\\"step\\\": 55000, \\\"eval_return\\\": 406.7}, {\\\"step\\\": 65000, \\\"eval_return\\\": 379.5}, {\\\"step\\\": 75000, \\\"eval_return\\\": 486.5}, {\\\"step\\\": 85000, \\\"eval_return\\\": 352.6}, {\\\"step\\\": 95000, \\\"eval_return\\\": 297.7}, {\\\"step\\\": 105000, \\\"eval_return\\\": 289.3}]}}, \\\"exp_072_008e_v3_walker_s5\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-25T10:00:39.306Z\\\", \\\"hypothesis\\\": \\\"Walker Walk 008e_v3 mitigation 配置 (trained dt_emb + subsample ON + dt=1 imag + H=15) seed=5。当前 5 seeds 测试 collapse rate=2/5 (40%)，加 seed=5 缩窄置信区间。来源: plan_016 扩展。\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"eval_return_final\\\": 853.1, \\\"eval_return_peak\\\": 853.1, \\\"eval_return_peak_step\\\": 105000, \\\"ve_ratio_final\\\": 0.6, \\\"nve_final\\\": 0.61, \\\"nve_peak\\\": 0.61, \\\"nve_peak_step\\\": 105000, \\\"civo_alert\\\": 0, \\\"civo\\\": false, \\\"gate_dt_1_frac\\\": 1, \\\"gate_dt_mean\\\": 1, \\\"actor_entropy_final\\\": -5.1, \\\"value_mean_final\\\": 520.8, \\\"eval_trajectory\\\": [{\\\"step\\\": 5000, \\\"eval_return\\\": 29.4}, {\\\"step\\\": 15000, \\\"eval_return\\\": 251.1}, {\\\"step\\\": 25000, \\\"eval_return\\\": 423}, {\\\"step\\\": 35000, \\\"eval_return\\\": 511}, {\\\"step\\\": 45000, \\\"eval_return\\\": 600.1}, {\\\"step\\\": 55000, \\\"eval_return\\\": 649}, {\\\"step\\\": 65000, \\\"eval_return\\\": 697.2}, {\\\"step\\\": 75000, \\\"eval_return\\\": 727.3}, {\\\"step\\\": 85000, \\\"eval_return\\\": 710.3}, {\\\"step\\\": 95000, \\\"eval_return\\\": 803.9}, {\\\"step\\\": 105000, \\\"eval_return\\\": 853.1}]}}, \\\"exp_069_008f_walker_repro_s1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-25T07:28:33.676Z\\\", \\\"hypothesis\\\": \\\"Reproducing 008f config (no dt_emb, dt_embed_dim=0 + subsample ON + dt=2 + H=8) on Walker Walk seed=1 will NOT trigger CIVO (NVE < 1.5x) because removing dt_emb eliminates the temporal abstraction mismatch that drives value error amplification\\\", \\\"metrics\\\": {\\\"eval_return_final\\\": 237.8, \\\"eval_return_peak\\\": 390.1, \\\"eval_return_peak_step\\\": 95000, \\\"ve_ratio_final\\\": 0.4, \\\"ve_ratio_peak\\\": 0.4, \\\"ve_ratio_peak_step\\\": 105000, \\\"nve_final_105k\\\": 0.61, \\\"nve_peak\\\": 0.66, \\\"nve_peak_step\\\": 75000, \\\"civo_alert\\\": false, \\\"gate_dt_2_frac\\\": 1, \\\"eval_trajectory\\\": {\\\"5k\\\": 30.5, \\\"15k\\\": 158.7, \\\"25k\\\": 180.8, \\\"35k\\\": 250.3, \\\"45k\\\": 293.6, \\\"55k\\\": 272.2, \\\"65k\\\": 328.1, \\\"75k\\\": 244.8, \\\"85k\\\": 382.5, \\\"95k\\\": 390.1, \\\"105k\\\": 237.8}, \\\"ve_ratio_trajectory\\\": {\\\"15k\\\": 0, \\\"25k\\\": 0.1, \\\"35k\\\": 0.2, \\\"45k\\\": 0.2, \\\"55k\\\": 0.3, \\\"65k\\\": 0.3, \\\"75k\\\": 0.4, \\\"85k\\\": 0.3, \\\"95k\\\": 0.3, \\\"105k\\\": 0.4}}, \\\"conclusion\\\": \\\"success\\\"}, \\\"exp_068_008d_walker_repro_s1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-25T07:28:31.319Z\\\", \\\"hypothesis\\\": \\\"Reproducing 008d config (trained dt_emb + subsample ON + dt=2 + H=8) on Walker Walk seed=1 will trigger CIVO (NVE > 1.5x) because trained dt_emb enables value error amplification through temporal abstraction mismatch\\\", \\\"metrics\\\": {\\\"eval_return_final\\\": 39.1, \\\"eval_return_peak\\\": 192.4, \\\"eval_return_peak_step\\\": 55000, \\\"ve_ratio_final\\\": 2.7, \\\"ve_ratio_peak\\\": 4.6, \\\"ve_ratio_peak_step\\\": 85000, \\\"nve_final_105k\\\": 4.12, \\\"nve_peak_85k\\\": 6.57, \\\"nve_onset_step\\\": 45000, \\\"nve_onset_value\\\": 1.81, \\\"civo_alert\\\": true, \\\"civo_alert_step\\\": 85000, \\\"gate_dt_2_frac\\\": 1, \\\"eval_trajectory\\\": {\\\"5k\\\": 31, \\\"15k\\\": 146.5, \\\"25k\\\": 174.1, \\\"35k\\\": 189.6, \\\"45k\\\": 142.2, \\\"55k\\\": 192.4, \\\"65k\\\": 114.4, \\\"75k\\\": 106.6, \\\"85k\\\": 33.4, \\\"95k\\\": 26.9, \\\"105k\\\": 39.1}, \\\"ve_ratio_trajectory\\\": {\\\"15k\\\": 0, \\\"25k\\\": 0.2, \\\"35k\\\": 0.3, \\\"45k\\\": 0.6, \\\"55k\\\": 0.6, \\\"65k\\\": 1.3, \\\"75k\\\": 1.6, \\\"85k\\\": 4.6, \\\"95k\\\": 4.6, \\\"105k\\\": 2.7}}, \\\"conclusion\\\": \\\"success\\\"}, \\\"exp_067_frozen_dt_emb_walker_plan015\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-25T06:59:24.006Z\\\", \\\"hypothesis\\\": \\\"Frozen (requires_grad=False) dt_embedding + subsample ON + dt=2 + H=8 在 Walker Walk 上不触发 CIVO，验证 dt_emb 的 TRAINING 是 CIVO 的必要条件（而非 dt_emb 的存在本身）。来源: plan_015。\\\", \\\"metrics\\\": {\\\"eval_final\\\": 281.5, \\\"eval_peak\\\": 334.1, \\\"eval_peak_step\\\": 95000, \\\"nve_peak\\\": 0.4, \\\"nve_final\\\": 0.2, \\\"civo_alert\\\": 0, \\\"total_env_steps\\\": 112000, \\\"update_count\\\": 25099, \\\"gate_dt_mean\\\": 2, \\\"gate_dt_std\\\": 0, \\\"gate_dt_2_frac\\\": 1, \\\"gate_empirical_entropy\\\": 0}, \\\"conclusion\\\": \\\"success\\\"}, \\\"exp_066b_timeseries_rssm_fidelity_s1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-25T04:35:12.673Z\\\", \\\"hypothesis\\\": \\\"RSSM fidelity gap (dt=2 prediction error > dt=1) emerges before value overestimation in seed=1, replicating the causal chain found in exp_066 seed=0 and confirming cross-seed robustness of the fidelity→VE mechanism.\\\", \\\"metrics\\\": {\\\"seed\\\": 1, \\\"steps_completed\\\": 65000, \\\"eval_return_peak\\\": 201.9, \\\"eval_return_peak_step\\\": 45000, \\\"eval_return_final\\\": 160.7, \\\"civo_alert_step\\\": 55000, \\\"ve_ratio_final\\\": 0.724, \\\"fidelity_gap_timeseries\\\": {\\\"ss_ratio_10K\\\": 0.887, \\\"ss_ratio_15K\\\": 1.017, \\\"ss_ratio_20K\\\": 1.216, \\\"ss_ratio_25K\\\": 1.532, \\\"ss_ratio_30K\\\": 1.374, \\\"ss_ratio_35K\\\": 1.486, \\\"ss_ratio_40K\\\": 1.428, \\\"ss_ratio_45K\\\": 1.38, \\\"ss_ratio_50K\\\": 1.468, \\\"ss_ratio_55K\\\": 1.517, \\\"ss_ratio_60K\\\": 1.799, \\\"ss_ratio_65K\\\": 1.756}, \\\"ve_ratio_timeseries\\\": {\\\"12K\\\": 0.012, \\\"15K\\\": 0.033, \\\"24K\\\": 0.118, \\\"25K\\\": 0.193, \\\"35K\\\": 0.269, \\\"45K\\\": 0.358, \\\"52K\\\": 0.495, \\\"55K\\\": 0.71, \\\"64K\\\": 0.724}, \\\"fidelity_gap_onset_step\\\": 15000, \\\"ve_onset_step\\\": 24000, \\\"temporal_lead_steps\\\": 9000, \\\"causal_direction\\\": \\\"fidelity_gap_leads_ve\\\", \\\"cross_seed_comparison\\\": {\\\"s0_ss_ratio_65K\\\": 1.678, \\\"s1_ss_ratio_65K\\\": 1.756, \\\"s0_fidelity_onset\\\": 20000, \\\"s1_fidelity_onset\\\": 15000, \\\"s0_ve_onset\\\": 30000, \\\"s1_ve_onset\\\": 24000, \\\"s0_temporal_lead\\\": 10000, \\\"s1_temporal_lead\\\": 9000, \\\"pattern_consistent\\\": true}}, \\\"conclusion\\\": \\\"success\\\"}, \\\"exp_008d_subsample_on_h8\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"hypothesis\\\": \\\"Trained dt-embedding with subsample (gate_fixed_dt=2, gate_subsample_max_dt=2) causes critic value function to overestimate through dt-conditioned representation co-adaptation, leading to policy collapse.\\\", \\\"metrics\\\": {\\\"actor_loss_25K\\\": -0.195, \\\"actor_loss_35K\\\": -0.17, \\\"baseline_35K\\\": 400, \\\"baseline_45K\\\": 443, \\\"data_source_45K\\\": \\\"from training logs metrics.jsonl\\\", \\\"eval_return_25K\\\": 167.22, \\\"eval_return_35K\\\": 146.34, \\\"eval_return_45K\\\": 140.8, \\\"eval_return_55K\\\": 82.75, \\\"model_loss_25K\\\": 5.33, \\\"model_loss_35K\\\": 5.07, \\\"step\\\": 55000, \\\"trend\\\": \\\"eval declining 167→146→141→83; v/e accelerating 15.5%→41.2%→69.3%→167% — delusional critic collapse confirmed, value exceeds eval_return at 55K\\\", \\\"value_eval_ratio_25K\\\": 0.155, \\\"value_eval_ratio_35K\\\": 0.411, \\\"value_eval_ratio_45K\\\": 0.693, \\\"value_eval_ratio_55K\\\": 1.666, \\\"value_mean_25K\\\": 25.86, \\\"value_mean_35K\\\": 60.2, \\\"value_mean_45K\\\": 97.5, \\\"value_mean_55K\\\": 137.88, \\\"verdict_35K\\\": \\\"WARN_COLLAPSE\\\", \\\"verdict_45K\\\": \\\"COLLAPSE_CONFIRMED\\\", \\\"vs_baseline_35K\\\": \\\"-63.4%\\\", \\\"vs_baseline_45K\\\": \\\"-68.2%\\\"}, \\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-25T02:41:05.620Z\\\"}, \\\"exp_066_timeseries_rssm_fidelity\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-25T02:33:00.783Z\\\", \\\"hypothesis\\\": \\\"Trained dt_embedding causes RSSM fidelity degradation (dt=2 vs dt=1 reward MAE gap) that progressively worsens during training, and its temporal evolution precedes or synchronizes with NVE (value overestimation) rise, establishing a temporal causal chain: RSSM fidelity gap → value overestimation.\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"ss_ratio_10K\\\": 1.047, \\\"ss_ratio_30K\\\": 1.247, \\\"ss_ratio_65K\\\": 1.678, \\\"ol_ratio_30K_peak\\\": 1.446, \\\"ol_ratio_35K_peak\\\": 1.509, \\\"ve_ratio_final\\\": 1.399, \\\"fidelity_gap_onset_step\\\": 20000, \\\"ve_onset_step\\\": 30000, \\\"temporal_lead_steps\\\": 10000, \\\"pearson_ss_ve\\\": 0.807, \\\"pearson_ss_ve_p\\\": 0.0015, \\\"pearson_ol_ve\\\": 0.425, \\\"pearson_ol_ve_p\\\": 0.169, \\\"ss_monotonicity\\\": 0.73, \\\"ol_monotonicity\\\": 0.73, \\\"ve_monotonicity\\\": 0.82, \\\"causal_direction\\\": \\\"fidelity_gap_leads_ve\\\", \\\"conclusion\\\": \\\"success\\\"}}, \\\"exp_060_cartpole_baseline\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-25T01:25:39.711Z\\\", \\\"hypothesis\\\": \\\"Cartpole Swingup (DMC) baseline dt=1 建立 v/e ratio 校准基线，用于 CIVO 诊断阈值在第三个 DMC 环境的验证。预期 NVE 保持在 1.0x 附近，无 CIVO 现象。\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"seeds\\\": 3, \\\"steps_per_seed\\\": 112000, \\\"train_return_s0\\\": 809.4, \\\"train_return_s1\\\": 684.4, \\\"train_return_s2\\\": 526.1, \\\"eval_return_s2_105K\\\": 557}}, \\\"exp_065_dt_emb_cosine\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-24T20:54:51.678Z\\\", \\\"hypothesis\\\": \\\"分析 trained dt_embedding 中 dt=1 vs dt=2 向量的 cosine similarity 及其训练过程演化。如果 cosine sim 高（接近 1）→ dt_emb 未学到有意义区分，CIVO 来自微小差异被 downstream 放大；如果 cosine sim 低 → dt_emb 学到了显著不同的表征，CIVO 来自 dt=2 表征本身的偏差。\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"trained_cosine_sim_range\\\": \\\"-0.94 to -0.70\\\", \\\"frozen_cosine_sim_range\\\": \\\"-0.15 to +0.07\\\", \\\"trained_trend\\\": \\\"strong negative (near-opposite directions)\\\", \\\"frozen_trend\\\": \\\"near-zero constant\\\", \\\"conclusion\\\": \\\"dt=1 and dt=2 embeddings learn nearly opposite representations; CIVO from dt=2 representation bias, not amplified micro-differences\\\"}}, \\\"exp_064_value_distribution\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-24T20:14:50.460Z\\\", \\\"hypothesis\\\": \\\"V(s) vs Monte Carlo return 分布对比：trained dt_emb (exp_008d collapsed) 的 value estimate 在 dt=2 imagination 步骤系统性高估，而 untrained/absent dt_emb (exp_008f control) 和 baseline (exp_001) 的 value 分布与 MC return 紧密跟踪。直观展示 CIVO 的 value divergence 位置和形态。\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"baseline_bias\\\": 344.85, \\\"baseline_rmse\\\": 371.73, \\\"baseline_overest_pct\\\": 100, \\\"baseline_v_mc_ratio\\\": 3.31, \\\"civo_bias\\\": 108.99, \\\"civo_rmse\\\": 112.36, \\\"civo_overest_pct\\\": 100, \\\"civo_v_mc_ratio\\\": 7.8, \\\"civo_v_mc_median\\\": 3.4, \\\"control_bias\\\": -6.51, \\\"control_rmse\\\": 57.93, \\\"control_overest_pct\\\": 52.5, \\\"control_v_mc_ratio\\\": 2.58, \\\"control_v_mc_median\\\": 1.05}}, \\\"exp_063_rssm_fidelity\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-24T19:21:37.837Z\\\", \\\"hypothesis\\\": \\\"RSSM 在 dt=2 transitions 上的 observation/reward reconstruction loss 显著高于 dt=1，量化 fidelity gap 作为 trained dt_emb 导致 delusional critic 的机械性基础。从 exp_001 (baseline) 和 exp_008d (collapsed) 的已有 checkpoint 提取，对比 dt=1 vs dt=2 prediction quality。\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"baseline_dt1_obs_mse\\\": 13.7, \\\"baseline_dt2_obs_mse\\\": 20.62, \\\"baseline_dt2_dt1_ratio_obs\\\": 1.505, \\\"baseline_dt2_dt1_ratio_reward\\\": 1.483, \\\"collapsed_dt1_obs_mse\\\": 26.93, \\\"collapsed_dt2_single_obs_mse\\\": 42.02, \\\"collapsed_dt2_single_reward_mae\\\": 0.146, \\\"collapsed_dt2_dt1_ratio_obs\\\": 1.56, \\\"collapsed_dt2_dt1_ratio_reward\\\": 2.695, \\\"collapsed_single_vs_chained_obs\\\": 1.138, \\\"collapsed_single_vs_chained_reward\\\": 1.926}}, \\\"exp_049_stackcube_civo_trigger_s0\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-24T16:53:19.032Z\\\", \\\"hypothesis\\\": \\\"CIVO trigger 配置（trained dt_emb + subsample ON + H=8）在 ManiSkill StackCube-v1 manipulation 任务上是否也触发 CIVO。测试 CIVO 是否从 locomotion 推广到 manipulation 领域。StackCube 是多阶段任务（pick+stack）。如果触发 → 扩展跨域证据；如果不触发 → 支持 locomotion-specific scope。\\\", \\\"metrics\\\": {\\\"eval_final\\\": 34.88, \\\"eval_final_step\\\": 212500, \\\"eval_peak\\\": 35.89, \\\"eval_peak_step\\\": 182500, \\\"ve_ratio_final\\\": 0.186, \\\"ve_ratio_final_step\\\": 212500, \\\"ve_ratio_peak\\\": 5.048, \\\"ve_ratio_peak_step\\\": 42500, \\\"total_steps\\\": 222400, \\\"total_episodes\\\": 1112, \\\"nve_classification\\\": \\\"onset_self_correcting\\\", \\\"civo_transient\\\": true, \\\"civo_sustained\\\": false, \\\"civo_transient_range\\\": \\\"22K-72K\\\", \\\"civo_self_correction\\\": true, \\\"civo_self_correction_step\\\": 112500, \\\"gate_dt_mean\\\": 2, \\\"gate_dt_variation\\\": false, \\\"eval_dip_during_civo\\\": 4.93, \\\"eval_dip_step\\\": 62500}, \\\"conclusion\\\": \\\"success\\\"}, \\\"exp_057\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-24T16:50:44.968Z\\\", \\\"hypothesis\\\": \\\"Frozen dt_emb 跨 seed 可复现性验证（Walker seed=2, n=3）。当前 Walker frozen s0 NVE 0.19, s1 NVE 1.71 transient。s2 增加样本量到 n=3 验证稳健性。\\\", \\\"metrics\\\": {\\\"eval_return_peak\\\": 221.7, \\\"eval_return_peak_step\\\": 195000, \\\"eval_return_final\\\": 123.9, \\\"eval_return_final_step\\\": 215000, \\\"nve_peak\\\": 1.3, \\\"nve_peak_step\\\": 115000, \\\"nve_final\\\": 0.2, \\\"civo_alert\\\": 0, \\\"civo_sustained\\\": false, \\\"civo_transient\\\": true, \\\"civo_transient_range\\\": \\\"115k-145k\\\", \\\"train_steps\\\": 225000, \\\"gate_dt_mean\\\": 2}, \\\"conclusion\\\": \\\"success\\\"}, \\\"exp_008d_civo_trigger_s4\\\": {\\\"conclusion\\\": \\\"success\\\", \\\"hypothesis\\\": \\\"Walker Walk CIVO trigger seed=4: trained dt_emb + subsample ON + H=8. 第四 seed 复现 CIVO (NVE>1.5×)，加强 Walker 因果论证的统计力度。Rebuttal 储备。\\\", \\\"metrics\\\": {\\\"ve_ratio_peak\\\": 3.0294, \\\"ve_ratio_peak_step\\\": 105000, \\\"ve_ratio_final\\\": 3.0294, \\\"ve_ratio_final_step\\\": 105000, \\\"nve_peak\\\": 4.62, \\\"nve_peak_step\\\": 105000, \\\"nve_peak_note\\\": \\\"step-matched s1 baseline @105K = 0.6564\\\", \\\"nve_classification\\\": \\\"onset_collapse\\\"}, \\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-24T08:56:41.239Z\\\"}, \\\"exp_059_walker_trained_s5\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-24T07:46:59.075Z\\\", \\\"hypothesis\\\": \\\"Walker CIVO trigger 第5个独立seed验证。当前4/4 seeds触发sustained CIVO（p=0.0625 binomial test）。如果s5也触发 → p=0.03125，达到统计显著性阈值。关联 Claim 1: CIVO reproducibility。\\\", \\\"metrics\\\": {\\\"ve_ratio_peak\\\": 3.3075, \\\"ve_ratio_peak_step\\\": \\\"85K\\\", \\\"nve_peak\\\": 4.72, \\\"nve_peak_note\\\": \\\"step-matched s1 baseline @85K = 0.7007\\\", \\\"nve_classification\\\": \\\"onset_collapse\\\", \\\"nve_classification_note\\\": \\\"Reclassified from onset_self_correcting: NVE self-corrected but eval=95.8 (10.5% of baseline 913) indicates irreversible policy damage. Collapse†.\\\", \\\"nve_final\\\": 1.22, \\\"nve_final_note\\\": \\\"0.8/0.656 (step-matched s1 baseline @105K)\\\", \\\"eval_final\\\": 95.8, \\\"eval_baseline\\\": 913, \\\"eval_pct_baseline\\\": \\\"10.5%\\\"}, \\\"conclusion\\\": \\\"success\\\"}, \\\"exp_057_frozen_dt_emb_walker_s2\\\": {\\\"status\\\": \\\"DONE\\\", \\\"conclusion\\\": \\\"success\\\", \\\"updated_at\\\": \\\"2026-05-24T02:17:41.318Z\\\", \\\"hypothesis\\\": \\\"Frozen dt_emb 跨 seed 可复现性验证（Walker n=3）。当前 Walker frozen s0 NVE 0.19, s1 NVE 1.71 transient。s2 增加样本量到 n=3，如果 0 CIVO → frozen 在 Walker 上稳健；如果出现持续 CIVO → 样本不足。\\\", \\\"metrics\\\": {\\\"total_steps\\\": 225000, \\\"ve_ratio_peak\\\": 1.283, \\\"ve_ratio_peak_step\\\": 115000, \\\"ve_ratio_final\\\": 0.177, \\\"ve_ratio_final_step\\\": 215000, \\\"nve_peak\\\": 1.88, \\\"nve_peak_step\\\": 115000, \\\"nve_classification\\\": \\\"transient\\\", \\\"eval_return_final\\\": 123.94, \\\"eval_return_final_step\\\": 215000, \\\"eval_return_peak\\\": 221.72, \\\"eval_return_peak_step\\\": 195000}}, \\\"exp_058_frozen_dt_emb_cheetah_s1\\\": {\\\"status\\\": \\\"DONE\\\", \\\"updated_at\\\": \\\"2026-05-24T00:30:00.000Z\\\", \\\"hypothesis\\\": \\\"Cheetah frozen dt_emb 跨 seed 可复现性验证。exp_046 (s0) 显示 frozen 将 NVE 从 ~70-108（trained）降至 1.35。s1 验证阻止效应是否可复现。如果 s1 也阻止 → Cheetah frozen n=2 增强极端 CIVO 场景下 frozen diagnostic 的统计基础。\\\", \\\"conclusion\\\": \\\"success\\\", \\\"metrics\\\": {\\\"total_steps\\\": 224000, \\\"ve_ratio_peak\\\": 0.231, \\\"ve_ratio_peak_step\\\": 45000, \\\"ve_ratio_final\\\": 0.107, \\\"ve_ratio_final_step\\\": 215000, \\\"eval_return_final\\\": 80.46, \\\"eval_return_final_step\\\": 215000, \\\"eval_return_peak\\\": 191.74, \\\"eval_return_peak_step\\\": 25000, \\\"nve_peak\\\": 0.78, \\\"nve_peak_step\\\": 45000, \\\"nve_classification\\\": \\\"no_civo\\\", \\\"note\\\": \\\"Cheetah frozen s1. NVE=0.78× (raw 0.231 / baseline 0.296 @45K). Cheetah frozen n=2: s0 NVE=1.35, s1 NVE=0.78 — both clean, frozen 稳健阻止 extreme CIVO (trained NVE 70-108).\\\"}}}, \\\"count\\\": 20, \\\"total\\\": 79, \\\"baseline\\\": null}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.5997}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"exp_074_008a_walker_s3\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-25T12:08:22.221Z\", \"hypothesis\": \"Walker Walk 008a 配置 (trained dt_emb unexposed + subsample OFF + dt=2 + H=15) seed=3。当前 008a 3 seeds 全部 success (no CIVO)，加 seed=3 巩固 C3 value suppression claim 统计。来源: plan_013 扩展。\", \"conclusion\": \"success\", \"metrics\": {\"eval_return_105K\": 855.9, \"civo_ve_ratio_final\": 0.3, \"civo_alert\": 0, \"value_mean_105K\": 295.2, \"gate_dt_2_frac\": 1, \"gate_dt_mean\": 2, \"model_loss_105K\": 3.8, \"eval_trajectory\": {\"5K\": 36.1, \"15K\": 281, \"25K\": 389.8, \"35K\": 303.8, \"45K\": 437.3, \"55K\": 411.3, \"65K\": 566.4, \"75K\": 513.9, \"85K\": 645.9, \"95K\": 776.6, \"105K\": 855.9}, \"four_seed_summary\": {\"mean_eval_return\": 791, \"std_eval_return\": 102.2, \"all_civo_alert_0\": true, \"seeds_completed\": 4}}}, \"exp_071_008f_walker_s3\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-25T10:42:39.889Z\", \"hypothesis\": \"Walker Walk 008f 配置 (no dt_emb, dt_embed_dim=0 + subsample ON + dt=2 + H=8) seed=3。当前 008f 2 seeds 结果分歧（s1=success eval=503, s2=negative eval=148），增加 seed 缩窄 causal control 稳定性估计。来源: plan_012 扩展。\", \"conclusion\": \"success\", \"metrics\": {\"eval_return_final\": 311.9, \"eval_return_peak\": 457.7, \"ve_ratio_final\": 0.4, \"ve_ratio_peak\": 0.7, \"gate_dt_mean_final\": 2, \"civo_alert\": 0, \"value_loss_final\": 1, \"actor_entropy_final\": -4.6, \"model_loss_final\": 4.5}}, \"exp_073_008f_walker_s4\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-25T10:00:42.604Z\", \"hypothesis\": \"Walker Walk 008f 配置 (no dt_emb, dt_embed_dim=0 + subsample ON + dt=2 + H=8) seed=4。当前 008f 0/3 CIVO onset，扩到 seed=4 进一步巩固 control 组统计。来源: plan_012 扩展。\", \"conclusion\": \"success\", \"metrics\": {\"eval_return_final\": 289.3, \"eval_return_peak\": 486.5, \"eval_return_peak_step\": 75000, \"ve_ratio_final\": 0.5, \"ve_ratio_peak\": 0.5, \"nve_peak\": 0.76, \"civo_alert\": 0, \"civo\": false, \"gate_dt_2_frac\": 1, \"gate_dt_mean\": 2, \"gate_empirical_entropy\": 0, \"eval_trajectory\": [{\"step\": 5000, \"eval_return\": 33.2}, {\"step\": 15000, \"eval_return\": 128.3}, {\"step\": 25000, \"eval_return\": 165.3}, {\"step\": 35000, \"eval_return\": 284.5}, {\"step\": 45000, \"eval_return\": 272.5}, {\"step\": 55000, \"eval_return\": 406.7}, {\"step\": 65000, \"eval_return\": 379.5}, {\"step\": 75000, \"eval_return\": 486.5}, {\"step\": 85000, \"eval_return\": 352.6}, {\"step\": 95000, \"eval_return\": 297.7}, {\"step\": 105000, \"eval_return\": 289.3}]}}, \"exp_072_008e_v3_walker_s5\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-25T10:00:39.306Z\", \"hypothesis\": \"Walker Walk 008e_v3 mitigation 配置 (trained dt_emb + subsample ON + dt=1 imag + H=15) seed=5。当前 5 seeds 测试 collapse rate=2/5 (40%)，加 seed=5 缩窄置信区间。来源: plan_016 扩展。\", \"conclusion\": \"success\", \"metrics\": {\"eval_return_final\": 853.1, \"eval_return_peak\": 853.1, \"eval_return_peak_step\": 105000, \"ve_ratio_final\": 0.6, \"nve_final\": 0.61, \"nve_peak\": 0.61, \"nve_peak_step\": 105000, \"civo_alert\": 0, \"civo\": false, \"gate_dt_1_frac\": 1, \"gate_dt_mean\": 1, \"actor_entropy_final\": -5.1, \"value_mean_final\": 520.8, \"eval_trajectory\": [{\"step\": 5000, \"eval_return\": 29.4}, {\"step\": 15000, \"eval_return\": 251.1}, {\"step\": 25000, \"eval_return\": 423}, {\"step\": 35000, \"eval_return\": 511}, {\"step\": 45000, \"eval_return\": 600.1}, {\"step\": 55000, \"eval_return\": 649}, {\"step\": 65000, \"eval_return\": 697.2}, {\"step\": 75000, \"eval_return\": 727.3}, {\"step\": 85000, \"eval_return\": 710.3}, {\"step\": 95000, \"eval_return\": 803.9}, {\"step\": 105000, \"eval_return\": 853.1}]}}, \"exp_069_008f_walker_repro_s1\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-25T07:28:33.676Z\", \"hypothesis\": \"Reproducing 008f config (no dt_emb, dt_embed_dim=0 + subsample ON + dt=2 + H=8) on Walker Walk seed=1 will NOT trigger CIVO (NVE < 1.5x) because removing dt_emb eliminates the temporal abstraction mismatch that drives value error amplification\", \"metrics\": {\"eval_return_final\": 237.8, \"eval_return_peak\": 390.1, \"eval_return_peak_step\": 95000, \"ve_ratio_final\": 0.4, \"ve_ratio_peak\": 0.4, \"ve_ratio_peak_step\": 105000, \"nve_final_105k\": 0.61, \"nve_peak\": 0.66, \"nve_peak_step\": 75000, \"civo_alert\": false, \"gate_dt_2_frac\": 1, \"eval_trajectory\": {\"5k\": 30.5, \"15k\": 158.7, \"25k\": 180.8, \"35k\": 250.3, \"45k\": 293.6, \"55k\": 272.2, \"65k\": 328.1, \"75k\": 244.8, \"85k\": 382.5, \"95k\": 390.1, \"105k\": 237.8}, \"ve_ratio_trajectory\": {\"15k\": 0, \"25k\": 0.1, \"35k\": 0.2, \"45k\": 0.2, \"55k\": 0.3, \"65k\": 0.3, \"75k\": 0.4, \"85k\": 0.3, \"95k\": 0.3, \"105k\": 0.4}}, \"conclusion\": \"success\"}, \"exp_068_008d_walker_repro_s1\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-25T07:28:31.319Z\", \"hypothesis\": \"Reproducing 008d config (trained dt_emb + subsample ON + dt=2 + H=8) on Walker Walk seed=1 will trigger CIVO (NVE > 1.5x) because trained dt_emb enables value error amplification through temporal abstraction mismatch\", \"metrics\": {\"eval_return_final\": 39.1, \"eval_return_peak\": 192.4, \"eval_return_peak_step\": 55000, \"ve_ratio_final\": 2.7, \"ve_ratio_peak\": 4.6, \"ve_ratio_peak_step\": 85000, \"nve_final_105k\": 4.12, \"nve_peak_85k\": 6.57, \"nve_onset_step\": 45000, \"nve_onset_value\": 1.81, \"civo_alert\": true, \"civo_alert_step\": 85000, \"gate_dt_2_frac\": 1, \"eval_trajectory\": {\"5k\": 31, \"15k\": 146.5, \"25k\": 174.1, \"35k\": 189.6, \"45k\": 142.2, \"55k\": 192.4, \"65k\": 114.4, \"75k\": 106.6, \"85k\": 33.4, \"95k\": 26.9, \"105k\": 39.1}, \"ve_ratio_trajectory\": {\"15k\": 0, \"25k\": 0.2, \"35k\": 0.3, \"45k\": 0.6, \"55k\": 0.6, \"65k\": 1.3, \"75k\": 1.6, \"85k\": 4.6, \"95k\": 4.6, \"105k\": 2.7}}, \"conclusion\": \"success\"}, \"exp_067_frozen_dt_emb_walker_plan015\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-25T06:59:24.006Z\", \"hypothesis\": \"Frozen (requires_grad=False) dt_embedding + subsample ON + dt=2 + H=8 在 Walker Walk 上不触发 CIVO，验证 dt_emb 的 TRAINING 是 CIVO 的必要条件（而非 dt_emb 的存在本身）。来源: plan_015。\", \"metrics\": {\"eval_final\": 281.5, \"eval_peak\": 334.1, \"eval_peak_step\": 95000, \"nve_peak\": 0.4, \"nve_final\": 0.2, \"civo_alert\": 0, \"total_env_steps\": 112000, \"update_count\": 25099, \"gate_dt_mean\": 2, \"gate_dt_std\": 0, \"gate_dt_2_frac\": 1, \"gate_empirical_entropy\": 0}, \"conclusion\": \"success\"}, \"exp_066b_timeseries_rssm_fidelity_s1\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-25T04:35:12.673Z\", \"hypothesis\": \"RSSM fidelity gap (dt=2 prediction error > dt=1) emerges before value overestimation in seed=1, replicating the causal chain found in exp_066 seed=0 and confirming cross-seed robustness of the fidelity→VE mechanism.\", \"metrics\": {\"seed\": 1, \"steps_completed\": 65000, \"eval_return_peak\": 201.9, \"eval_return_peak_step\": 45000, \"eval_return_final\": 160.7, \"civo_alert_step\": 55000, \"ve_ratio_final\": 0.724, \"fidelity_gap_timeseries\": {\"ss_ratio_10K\": 0.887, \"ss_ratio_15K\": 1.017, \"ss_ratio_20K\": 1.216, \"ss_ratio_25K\": 1.532, \"ss_ratio_30K\": 1.374, \"ss_ratio_35K\": 1.486, \"ss_ratio_40K\": 1.428, \"ss_ratio_45K\": 1.38, \"ss_ratio_50K\": 1.468, \"ss_ratio_55K\": 1.517, \"ss_ratio_60K\": 1.799, \"ss_ratio_65K\": 1.756}, \"ve_ratio_timeseries\": {\"12K\": 0.012, \"15K\": 0.033, \"24K\": 0.118, \"25K\": 0.193, \"35K\": 0.269, \"45K\": 0.358, \"52K\": 0.495, \"55K\": 0.71, \"64K\": 0.724}, \"fidelity_gap_onset_step\": 15000, \"ve_onset_step\": 24000, \"temporal_lead_steps\": 9000, \"causal_direction\": \"fidelity_gap_leads_ve\", \"cross_seed_comparison\": {\"s0_ss_ratio_65K\": 1.678, \"s1_ss_ratio_65K\": 1.756, \"s0_fidelity_onset\": 20000, \"s1_fidelity_onset\": 15000, \"s0_ve_onset\": 30000, \"s1_ve_onset\": 24000, \"s0_temporal_lead\": 10000, \"s1_temporal_lead\": 9000, \"pattern_consistent\": true}}, \"conclusion\": \"success\"}, \"exp_008d_subsample_on_h8\": {\"conclusion\": \"success\", \"hypothesis\": \"Trained dt-embedding with subsample (gate_fixed_dt=2, gate_subsample_max_dt=2) causes critic value function to overestimate through dt-conditioned representation co-adaptation, leading to policy collapse.\", \"metrics\": {\"actor_loss_25K\": -0.195, \"actor_loss_35K\": -0.17, \"baseline_35K\": 400, \"baseline_45K\": 443, \"data_source_45K\": \"from training logs metrics.jsonl\", \"eval_return_25K\": 167.22, \"eval_return_35K\": 146.34, \"eval_return_45K\": 140.8, \"eval_return_55K\": 82.75, \"model_loss_25K\": 5.33, \"model_loss_35K\": 5.07, \"step\": 55000, \"trend\": \"eval declining 167→146→141→83; v/e accelerating 15.5%→41.2%→69.3%→167% — delusional critic collapse confirmed, value exceeds eval_return at 55K\", \"value_eval_ratio_25K\": 0.155, \"value_eval_ratio_35K\": 0.411, \"value_eval_ratio_45K\": 0.693, \"value_eval_ratio_55K\": 1.666, \"value_mean_25K\": 25.86, \"value_mean_35K\": 60.2, \"value_mean_45K\": 97.5, \"value_mean_55K\": 137.88, \"verdict_35K\": \"WARN_COLLAPSE\", \"verdict_45K\": \"COLLAPSE_CONFIRMED\", \"vs_baseline_35K\": \"-63.4%\", \"vs_baseline_45K\": \"-68.2%\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-25T02:41:05.620Z\"}, \"exp_066_timeseries_rssm_fidelity\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-25T02:33:00.783Z\", \"hypothesis\": \"Trained dt_embedding causes RSSM fidelity degradation (dt=2 vs dt=1 reward MAE gap) that progressively worsens during training, and its temporal evolution precedes or synchronizes with NVE (value overestimation) rise, establishing a temporal causal chain: RSSM fidelity gap → value overestimation.\", \"conclusion\": \"success\", \"metrics\": {\"ss_ratio_10K\": 1.047, \"ss_ratio_30K\": 1.247, \"ss_ratio_65K\": 1.678, \"ol_ratio_30K_peak\": 1.446, \"ol_ratio_35K_peak\": 1.509, \"ve_ratio_final\": 1.399, \"fidelity_gap_onset_step\": 20000, \"ve_onset_step\": 30000, \"temporal_lead_steps\": 10000, \"pearson_ss_ve\": 0.807, \"pearson_ss_ve_p\": 0.0015, \"pearson_ol_ve\": 0.425, \"pearson_ol_ve_p\": 0.169, \"ss_monotonicity\": 0.73, \"ol_monotonicity\": 0.73, \"ve_monotonicity\": 0.82, \"causal_direction\": \"fidelity_gap_leads_ve\", \"conclusion\": \"success\"}}, \"exp_060_cartpole_baseline\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-25T01:25:39.711Z\", \"hypothesis\": \"Cartpole Swingup (DMC) baseline dt=1 建立 v/e ratio 校准基线，用于 CIVO 诊断阈值在第三个 DMC 环境的验证。预期 NVE 保持在 1.0x 附近，无 CIVO 现象。\", \"conclusion\": \"success\", \"metrics\": {\"seeds\": 3, \"steps_per_seed\": 112000, \"train_return_s0\": 809.4, \"train_return_s1\": 684.4, \"train_return_s2\": 526.1, \"eval_return_s2_105K\": 557}}, \"exp_065_dt_emb_cosine\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-24T20:54:51.678Z\", \"hypothesis\": \"分析 trained dt_embedding 中 dt=1 vs dt=2 向量的 cosine similarity 及其训练过程演化。如果 cosine sim 高（接近 1）→ dt_emb 未学到有意义区分，CIVO 来自微小差异被 downstream 放大；如果 cosine sim 低 → dt_emb 学到了显著不同的表征，CIVO 来自 dt=2 表征本身的偏差。\", \"conclusion\": \"success\", \"metrics\": {\"trained_cosine_sim_range\": \"-0.94 to -0.70\", \"frozen_cosine_sim_range\": \"-0.15 to +0.07\", \"trained_trend\": \"strong negative (near-opposite directions)\", \"frozen_trend\": \"near-zero constant\", \"conclusion\": \"dt=1 and dt=2 embeddings learn nearly opposite representations; CIVO from dt=2 representation bias, not amplified micro-differences\"}}, \"exp_064_value_distribution\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-24T20:14:50.460Z\", \"hypothesis\": \"V(s) vs Monte Carlo return 分布对比：trained dt_emb (exp_008d collapsed) 的 value estimate 在 dt=2 imagination 步骤系统性高估，而 untrained/absent dt_emb (exp_008f control) 和 baseline (exp_001) 的 value 分布与 MC return 紧密跟踪。直观展示 CIVO 的 value divergence 位置和形态。\", \"conclusion\": \"success\", \"metrics\": {\"baseline_bias\": 344.85, \"baseline_rmse\": 371.73, \"baseline_overest_pct\": 100, \"baseline_v_mc_ratio\": 3.31, \"civo_bias\": 108.99, \"civo_rmse\": 112.36, \"civo_overest_pct\": 100, \"civo_v_mc_ratio\": 7.8, \"civo_v_mc_median\": 3.4, \"control_bias\": -6.51, \"control_rmse\": 57.93, \"control_overest_pct\": 52.5, \"control_v_mc_ratio\": 2.58, \"control_v_mc_median\": 1.05}}, \"exp_063_rssm_fidelity\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-24T19:21:37.837Z\", \"hypothesis\": \"RSSM 在 dt=2 transitions 上的 observation/reward reconstruction loss 显著高于 dt=1，量化 fidelity gap 作为 trained dt_emb 导致 delusional critic 的机械性基础。从 exp_001 (baseline) 和 exp_008d (collapsed) 的已有 checkpoint 提取，对比 dt=1 vs dt=2 prediction quality。\", \"conclusion\": \"success\", \"metrics\": {\"baseline_dt1_obs_mse\": 13.7, \"baseline_dt2_obs_mse\": 20.62, \"baseline_dt2_dt1_ratio_obs\": 1.505, \"baseline_dt2_dt1_ratio_reward\": 1.483, \"collapsed_dt1_obs_mse\": 26.93, \"collapsed_dt2_single_obs_mse\": 42.02, \"collapsed_dt2_single_reward_mae\": 0.146, \"collapsed_dt2_dt1_ratio_obs\": 1.56, \"collapsed_dt2_dt1_ratio_reward\": 2.695, \"collapsed_single_vs_chained_obs\": 1.138, \"collapsed_single_vs_chained_reward\": 1.926}}, \"exp_049_stackcube_civo_trigger_s0\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-24T16:53:19.032Z\", \"hypothesis\": \"CIVO trigger 配置（trained dt_emb + subsample ON + H=8）在 ManiSkill StackCube-v1 manipulation 任务上是否也触发 CIVO。测试 CIVO 是否从 locomotion 推广到 manipulation 领域。StackCube 是多阶段任务（pick+stack）。如果触发 → 扩展跨域证据；如果不触发 → 支持 locomotion-specific scope。\", \"metrics\": {\"eval_final\": 34.88, \"eval_final_step\": 212500, \"eval_peak\": 35.89, \"eval_peak_step\": 182500, \"ve_ratio_final\": 0.186, \"ve_ratio_final_step\": 212500, \"ve_ratio_peak\": 5.048, \"ve_ratio_peak_step\": 42500, \"total_steps\": 222400, \"total_episodes\": 1112, \"nve_classification\": \"onset_self_correcting\", \"civo_transient\": true, \"civo_sustained\": false, \"civo_transient_range\": \"22K-72K\", \"civo_self_correction\": true, \"civo_self_correction_step\": 112500, \"gate_dt_mean\": 2, \"gate_dt_variation\": false, \"eval_dip_during_civo\": 4.93, \"eval_dip_step\": 62500}, \"conclusion\": \"success\"}, \"exp_057\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-24T16:50:44.968Z\", \"hypothesis\": \"Frozen dt_emb 跨 seed 可复现性验证（Walker seed=2, n=3）。当前 Walker frozen s0 NVE 0.19, s1 NVE 1.71 transient。s2 增加样本量到 n=3 验证稳健性。\", \"metrics\": {\"eval_return_peak\": 221.7, \"eval_return_peak_step\": 195000, \"eval_return_final\": 123.9, \"eval_return_final_step\": 215000, \"nve_peak\": 1.3, \"nve_peak_step\": 115000, \"nve_final\": 0.2, \"civo_alert\": 0, \"civo_sustained\": false, \"civo_transient\": true, \"civo_transient_range\": \"115k-145k\", \"train_steps\": 225000, \"gate_dt_mean\": 2}, \"conclusion\": \"success\"}, \"exp_008d_civo_trigger_s4\": {\"conclusion\": \"success\", \"hypothesis\": \"Walker Walk CIVO trigger seed=4: trained dt_emb + subsample ON + H=8. 第四 seed 复现 CIVO (NVE>1.5×)，加强 Walker 因果论证的统计力度。Rebuttal 储备。\", \"metrics\": {\"ve_ratio_peak\": 3.0294, \"ve_ratio_peak_step\": 105000, \"ve_ratio_final\": 3.0294, \"ve_ratio_final_step\": 105000, \"nve_peak\": 4.62, \"nve_peak_step\": 105000, \"nve_peak_note\": \"step-matched s1 baseline @105K = 0.6564\", \"nve_classification\": \"onset_collapse\"}, \"status\": \"DONE\", \"updated_at\": \"2026-05-24T08:56:41.239Z\"}, \"exp_059_walker_trained_s5\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-24T07:46:59.075Z\", \"hypothesis\": \"Walker CIVO trigger 第5个独立seed验证。当前4/4 seeds触发sustained CIVO（p=0.0625 binomial test）。如果s5也触发 → p=0.03125，达到统计显著性阈值。关联 Claim 1: CIVO reproducibility。\", \"metrics\": {\"ve_ratio_peak\": 3.3075, \"ve_ratio_peak_step\": \"85K\", \"nve_peak\": 4.72, \"nve_peak_note\": \"step-matched s1 baseline @85K = 0.7007\", \"nve_classification\": \"onset_collapse\", \"nve_classification_note\": \"Reclassified from onset_self_correcting: NVE self-corrected but eval=95.8 (10.5% of baseline 913) indicates irreversible policy damage. Collapse†.\", \"nve_final\": 1.22, \"nve_final_note\": \"0.8/0.656 (step-matched s1 baseline @105K)\", \"eval_final\": 95.8, \"eval_baseline\": 913, \"eval_pct_baseline\": \"10.5%\"}, \"conclusion\": \"success\"}, \"exp_057_frozen_dt_emb_walker_s2\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"updated_at\": \"2026-05-24T02:17:41.318Z\", \"hypothesis\": \"Frozen dt_emb 跨 seed 可复现性验证（Walker n=3）。当前 Walker frozen s0 NVE 0.19, s1 NVE 1.71 transient。s2 增加样本量到 n=3，如果 0 CIVO → frozen 在 Walker 上稳健；如果出现持续 CIVO → 样本不足。\", \"metrics\": {\"total_steps\": 225000, \"ve_ratio_peak\": 1.283, \"ve_ratio_peak_step\": 115000, \"ve_ratio_final\": 0.177, \"ve_ratio_final_step\": 215000, \"nve_peak\": 1.88, \"nve_peak_step\": 115000, \"nve_classification\": \"transient\", \"eval_return_final\": 123.94, \"eval_return_final_step\": 215000, \"eval_return_peak\": 221.72, \"eval_return_peak_step\": 195000}}, \"exp_058_frozen_dt_emb_cheetah_s1\": {\"status\": \"DONE\", \"updated_at\": \"2026-05-24T00:30:00.000Z\", \"hypothesis\": \"Cheetah frozen dt_emb 跨 seed 可复现性验证。exp_046 (s0) 显示 frozen 将 NVE 从 ~70-108（trained）降至 1.35。s1 验证阻止效应是否可复现。如果 s1 也阻止 → Cheetah frozen n=2 增强极端 CIVO 场景下 frozen diagnostic 的统计基础。\", \"conclusion\": \"success\", \"metrics\": {\"total_steps\": 224000, \"ve_ratio_peak\": 0.231, \"ve_ratio_peak_step\": 45000, \"ve_ratio_final\": 0.107, \"ve_ratio_final_step\": 215000, \"eval_return_final\": 80.46, \"eval_return_final_step\": 215000, \"eval_return_peak\": 191.74, \"eval_return_peak_step\": 25000, \"nve_peak\": 0.78, \"nve_peak_step\": 45000, \"nve_classification\": \"no_civo\", \"note\": \"Cheetah frozen s1. NVE=0.78× (raw 0.231 / baseline 0.296 @45K). Cheetah frozen n=2: s0 NVE=1.35, s1 NVE=0.78 — both clean, frozen 稳健阻止 extreme CIVO (trained NVE 70-108).\"}}}, \"count\": 20, \"total\": 79, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.5997}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 26_

<details><summary>Logged reasoning block</summary>

```text
Now I have a good picture. Let me also read the rebuttal files and appendix to check completeness. Let me read the rebuttal prep and the appendix.tex.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72aab3fa-ba3f-48a9-9029-1cec279461d0",
  "uuid": "d0896f8c-1b3e-4f03-86f2-35cc20d92b00",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FKPT34bFQveB4vaHVfxyzp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12121,
      "cache_read_input_tokens": 32216,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12121
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

_source line 27_

Now let me read the rebuttal prep and appendix files, plus the paper_provenance.yaml for data consistency checks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72aab3fa-ba3f-48a9-9029-1cec279461d0",
  "uuid": "a15e2645-1561-4e79-b024-30d4c643a969",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FKPT34bFQveB4vaHVfxyzp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12121,
      "cache_read_input_tokens": 32216,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12121
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

_source line 28_

<details open><summary>🔧 Tool call — Read · `toolu_0114rv5K5wYbiyfK5Y1rTFaF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/rebuttal_prep.md",
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72aab3fa-ba3f-48a9-9029-1cec279461d0",
  "uuid": "e9e301a1-d29e-48e2-9a39-9aca04d5c0a0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FKPT34bFQveB4vaHVfxyzp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12121,
      "cache_read_input_tokens": 32216,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12121
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

_source line 29 · 2026-05-25T13:46:37.873Z_

<details><summary>↩ Tool result · `toolu_0114rv5K5wYbiyfK5Y1rTFaF`</summary>

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
  "session_id": "72aab3fa-ba3f-48a9-9029-1cec279461d0",
  "uuid": "1d877cf1-6142-4a42-a413-aae02f2fd8ef",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/rebuttal_prep.md",
      "content": "# Anticipated Reviewer Q&A — ICML 2026\n\n## Q1: Frozen dt_emb prevention rate is only 71% (5/7) — is this reliable enough as a diagnostic?\n\n**Anticipated question**: \"Your frozen dt_emb only prevents NVE>1.5× in 5 of 7 seeds (71%). How can you claim it's a reliable diagnostic tool when it fails 29% of the time?\"\n\n**Response**: The 71% figure counts *any* NVE>1.5× exceedance, including transient spikes that self-correct. The operationally relevant metric is *sustained* CIVO: 0/7 frozen seeds exhibit sustained CIVO (defined as NVE≥1.5× persisting over a ≥35K-step window). The 2/7 transient exceedances self-corrected within training — one Walker seed peaked at NVE 1.71 before returning to 0.56, another at 1.88→0.177. By contrast, all trained dt_emb seeds in the original validation exceeded NVE>1.5× (2/2 Walker trained seeds: 008d NVE 2.09×, 009b NVE 1.62×), and additional seeds (s3/s4/s5) confirm CIVO triggering across seeds. This yields sensitivity=1.0 and specificity=1.0 for the sustained-CIVO criterion in the original 4-experiment validation (2 trained + 2 removed). The transient exceedances actually *strengthen* the diagnostic: they demonstrate the system's self-corrective capacity when the trained-dt_emb amplification loop is absent.\n\n**Evidence**: Frozen locomotion — Walker s0 NVE 0.19, s1 NVE 1.71→0.56 (transient), s2 NVE 1.88→0.177 (transient); Cheetah s0 NVE 1.35, s1 NVE 0.78 (no CIVO). Trained locomotion — original validation 2/2 Walker trained seeds exceed NVE>1.5× (008d NVE 2.09×, 009b NVE 1.62×); additional seeds s3/s4/s5 all trigger CIVO (NVE 1.53–4.84×). Fisher exact test p=0.003 for three-way causal (trained/frozen/removed).\n\n---\n\n## Q2: Manipulation 0/5 CIVO — how do you know dt_emb-dependent CIVO doesn't exist there?\n\n**Anticipated question**: \"You found 0/5 dt_emb-dependent CIVO in manipulation tasks. How can you distinguish 'CIVO doesn't exist here' from 'your protocol failed to detect it'? PegInsertion showed ve_ratio bursts — isn't that CIVO?\"\n\n**Response**: The PegInsertion ve_ratio bursts are environment-driven transients, not dt_emb-dependent CIVO. Our evidence is a paired seed ordering reversal: frozen s1 peaked at 11.32 while trained s1 peaked at only 3.08 — the opposite of what dt_emb-dependent CIVO predicts. In s0 the ordering was as expected (trained 10.05 > frozen 1.82), but the reversal in s1 falsifies dt_emb causality (D146). Additionally, PickCube showed NVE self-correction to 0.2 regardless of dt_emb configuration. We interpret this as a genuine domain boundary: manipulation tasks have shorter effective horizons and dense reward shaping, reducing the temporal-gap prediction errors that drive CIVO in locomotion. We report this as a scope limitation, not a negative result.\n\n**Evidence**: D146 ordering reversal — exp_055 trained s1 peak 3.08, exp_056 frozen s1 peak 11.32 (frozen > trained). exp_050 trained s0 peak 10.05, exp_053 frozen s0 回落到 1.82. PickCube: NVE self-corrects to 0.2 in all configs (trained/frozen/dual-critic). 0/5 manipulation seeds show trained > frozen ordering consistently.\n\n---\n\n## Q3: All results are from DreamerV3 — how does this generalize to other MBRL algorithms?\n\n**Anticipated question**: \"Your findings are limited to a single algorithm (DreamerV3) with a specific architecture (RSSM). Why should the community care if CIVO doesn't generalize beyond this one system?\"\n\n**Response**: We deliberately scope claims to DreamerV3 and make the scope explicit. However, the *mechanism* — temporal conditioning amplifying world-model prediction errors into value overestimation via imagination-based critic bootstrapping — applies to any MBRL system that (a) uses learned temporal conditioning, (b) trains critics on imagined trajectories, and (c) has latent dynamics with temporal-gap fidelity degradation. The strongest generalization evidence is the MPC/imagination boundary: TAWM (Nhu et al., ICML 2025) successfully uses dt-conditioning in TD-MPC2 (MPC setting) because MPC re-plans from real states each step, breaking the bootstrapping feedback loop. This architectural contrast localizes CIVO to imagination-based actor-critic — not just DreamerV3, but the entire class. The gradient-causality dissociation finding (gradient magnitude ≠ causal importance) is architecture-agnostic and relevant to any multi-head MBRL system.\n\n**Evidence**: TAWM succeeds with dt-conditioning in MPC (re-planning from real states), fails in imagination (critic bootstrapping). Gradient decomposition: reward head 38–49% gradient share but causally irrelevant; obs decoder 16–22% but causally critical — this dissociation is a general methodological insight for multi-loss MBRL debugging.\n\n---\n\n## Q4: Only 2 locomotion environments — is n=2 sufficient to support the claims?\n\n**Anticipated question**: \"Walker and Cheetah are both simple locomotion tasks from DeepMind Control Suite. Two environments is far too few to make general claims about CIVO.\"\n\n**Response**: Walker and Cheetah are chosen to represent qualitatively different CIVO regimes, not as a random sample. Walker exhibits moderate CIVO (NVE 2–5×) with self-correction capacity (170K steps to recover), while Cheetah exhibits extreme CIVO (NVE 8–70×) with irreversible damage (gate permanently collapsed, eval stuck at 23.4 after 300K steps). This severity continuum — not environment count — is the scientific contribution. The frozen diagnostic shows 100% prevention across both severity levels (5/5 locomotion seeds), and dual-critic shows environment-dependent efficacy (prevention in Walker, partial mitigation in Cheetah), revealing that intervention effectiveness scales with CIVO severity. Additionally, 3 ManiSkill manipulation tasks (PickCube, PegInsertion, StackCube) establish the domain boundary where CIVO does not trigger. Total: 5 environments, 133 experiments, 63 successful.\n\n**Evidence**: Walker moderate — exp_045 self-correction eval 35→868 over 170K steps. Cheetah extreme — exp_048 irreversible eval 23.4, NVE 2.75, gate permanently collapsed @300K. Severity continuum confirmed across dual-critic (Walker 2/2 prevented vs Cheetah partial), TCN (Walker 2/4 vs Cheetah 0/3), and frozen (both 100%). ManiSkill 3 tasks × 5 seeds = 0 dt_emb-dependent CIVO.\n\n---\n\n## Q5: Why not compare interventions head-to-head (e.g., TCN vs frozen vs dual-critic)?\n\n**Anticipated question**: \"You test seven interventions but never compare them against each other on the same seeds. Without controlled head-to-head comparison, how can you rank the Intervention Hierarchy levels?\"\n\n**Response**: The Intervention Hierarchy is ranked by success rate across all tested seeds, not by paired comparison — this is deliberate. The success rates are so disparate that head-to-head pairing adds no discriminative power: gradient-level SGS 1/11 (9%), output-level RAVE 0/2 (0%), representation-level TCN 4/11 (36%), architecture-level dual-critic 3/8 (38%), vs embedding removal 5/5 (100%). The hierarchy's contribution is taxonomic: it organizes methods into four mechanistic levels and demonstrates that each level fails for a *distinct* reason — gradient stopping fails because forward-pass representational damage is irreducible, RAVE fails because the EMA anchor is polluted by early overestimation, TCN fails because effective dose is environment-dependent with no universal Goldilocks zone, and architecture-level interventions (dual-critic) partially succeed in moderate-CIVO environments but fail in severe ones. A head-to-head comparison on matched seeds would confirm what aggregate rates already show, at the cost of doubling GPU budget with no new mechanistic insight.\n\n**Evidence**: Intervention Hierarchy table — L1 Gradient: Full SGS 0/3, Obs-decoder SGS 1/6, Reward SGS 0/2 (1/11). L2 Output: RAVE 0/2. L3 Representation: TCN 4/11 (σ=0.1 1/1 borderline NVE=1.02×, σ=0.2 2/6 Walker only 45–91% eval retention, σ=0.5 0/3, σ=1.0 1/1 pyrrhic). L4 Architecture: Wide dual 3/4, Narrow dual 0/2, Wide single 0/2 (3/8). Control: dt_emb removal 5/5. Total: 8/32 interventions succeed vs 5/5 removal. Cheetah \"impossible dose\" (exp_030c): σ=1.0 prevents CIVO (NVE≤0.30) but eval degrades 372→47 — no viable operating point exists.\n\n---\n\n## Q6: NVE 1.5× threshold — is this arbitrary? How sensitive are claims to this cutoff?\n\n**Anticipated question**: \"Your entire diagnostic framework relies on the 1.5× NVE threshold. How was it chosen, and do your claims hold under different thresholds?\"\n\n**Response**: The 1.5× threshold was not hand-tuned — it emerges from ROC analysis. Across 30 labeled data points (4 environments, multiple configs), Youden-optimal threshold is 1.53×, independently converging on our pre-specified 1.5×. LOEO (Leave-One-Environment-Out) cross-validation across Walker (n=15), Cheetah (n=5), and PickCube (n=2) yields mean AUROC 0.988 and mean accuracy 0.978, demonstrating robust separating power. The threshold falls within the optimal accuracy range for all three training folds. Claims are stable across a range: at 1.3× the only change is 2 additional borderline transients reclassified (no sustained CIVO misses); at 2.0× we lose early detection of moderate Walker CIVO but severe cases remain captured. The threshold's utility is as a *diagnostic alarm*, not a mechanistic boundary — sustained NVE>1.5× across consecutive checkpoints indicates dt_emb-driven CIVO with zero false positives in our dataset. We acknowledge in-sample calibration and validation as a limitation and recommend held-out validation on other architectures.\n\n**Evidence**: In-sample AUROC 0.957 (n=30, 2 environments). LOEO cross-validated mean AUROC 0.988, mean accuracy 0.978 (3 folds: Walker/Cheetah/PickCube). Youden-optimal 1.53× vs pre-specified 1.5×. Trained dt_emb: original validation 2/2 Walker seeds exceed 1.5× (008d NVE 2.09×, 009b NVE 1.62×); additional seeds s3–s5 also trigger CIVO. Frozen: 0/5 locomotion sustained (2/7 total transient, self-corrected). Removed: 0/4 exceed 1.5×. 4/4 perfect separation in the original 2-seed validation (008d+009b vs 008f+009c).\n\n---\n\n## Q7: Sample sizes are small (n=2–4 per condition) — are conclusions statistically reliable?\n\n**Anticipated question**: \"Most conditions have only 2–4 seeds. With such small samples, your results could be driven by lucky/unlucky initializations. Why not run 10+ seeds?\"\n\n**Response**: We report 133 experiments across 63 successful conditions — the aggregate evidence base is substantial even if individual conditions have few seeds. Key claims rely on *perfect separation*, not effect sizes: trained dt_emb triggers CIVO in all tested Walker seeds (2/2 original validation, 3 additional seeds s3–s5), frozen prevents in 5/5 — Fisher exact test p=0.003. For the intervention hierarchy, the signal is overwhelming: removal succeeds 5/5 while all other interventions combined succeed 8/32. Where seed variance matters (e.g., TCN Walker σ=0.2: 2/4 seeds succeed), we report it transparently as evidence of unreliability, not as a positive result. We follow Agarwal et al. (2021) in reporting IQM with stratified bootstrap CIs rather than claiming significance from small n. The compute budget (~40 GPU-days total) was allocated to maximize mechanistic coverage (7 methods × 3 levels × 5 environments) over per-condition replication.\n\n**Evidence**: Aggregate: 133 experiments, 63 success, 35 negative. Per-condition: trained CIVO 2/2 original validation + 3 additional seeds all trigger, frozen 0/5 CIVO (locomotion), removal 5/5 prevention. Fisher p=0.003 for trained-vs-frozen-vs-removed three-way. TCN seed variance (45–91% eval retention at σ=0.2 Walker) reported as instability evidence. Dual-critic 2×2 factorial fully populated.\n\n---\n\n## Q8: CIVO onset is universal but outcomes diverge — does this weaken the CIVO threat narrative?\n\n**Anticipated question**: \"You show 5/5 Walker trained seeds trigger CIVO onset (NVE>1.5×), but only some lead to collapse while others self-correct. If CIVO self-corrects in some seeds, is it really a problem worth diagnosing?\"\n\n**Response**: The onset/outcome divergence actually *strengthens* the contribution. CIVO onset (NVE exceeding the 1.5× threshold under step-matched baseline normalization) is deterministic: 5/5 Walker trained seeds trigger it, 0/5 frozen seeds do, establishing dt_emb as the causal factor (Fisher exact p<0.01). The downstream *outcome* — whether onset progresses to irreversible collapse or self-corrects — is stochastic and seed-dependent, but overwhelmingly destructive: 6/7 locomotion seeds (86%) suffer irreversible policy collapse despite NVE sometimes self-correcting. Seed 5 exemplifies this dissociation: its NVE drops from 4.72× to 1.22× (critic error self-corrects), yet eval remains at 95.8 (10.5% of baseline) — the policy damage inflicted during the CIVO episode is permanent. This is the expected behavior of a feedback loop operating near a bifurcation point: the critic anomaly may resolve, but the policy has already been driven into a degenerate attractor from which it cannot escape. The practical implication is that CIVO onset is a *necessary precursor* to collapse and almost always sufficient — practitioners cannot rely on NVE self-correction to save the run. The frozen dt_emb diagnostic eliminates onset entirely (0/5 seeds), removing both collapse risk and the false hope of self-correction. This makes the diagnostic more valuable, not less: it prevents a near-deterministic catastrophic failure mode.\n\n**Evidence**: Walker trained seeds — 5/5 onset (NVE 1.53–4.72×), outcomes: s1 collapse (eval 83@105K), s2 self-correct (eval 268@105K — unique recovery), s3 late-onset collapse then slow recovery over 300K (exp_045 eval 868), s4 late-spike collapse (NVE 4.44@105K endpoint), s5 collapse† (NVE 4.72→1.22×, eval 95.8 = 10.5% baseline — NVE self-corrected but policy did not recover). Cheetah: 2/2 collapse. Total: 6/7 collapse, 1/7 self-correction (s2 only). Frozen: 0/5 onset. The 86% collapse rate underscores CIVO as a near-deterministic failure mode once onset occurs.\n\n---\n\n## Q9: Why only test on DreamerV3? Do other MBRL algorithms also exhibit CIVO?\n\n**Anticipated question**: \"You only test CIVO in DreamerV3 with the RSSM architecture. This is a single algorithm — how do we know this isn't an artifact of DreamerV3's specific implementation rather than a general MBRL phenomenon? Have you tested TD-MPC2, IRIS, or other imagination-based methods?\"\n\n**Response**: We deliberately position this work as the first systematic identification and analysis of CIVO *within DreamerV3*, not as a universal MBRL claim. However, the mechanism we identify — temporal conditioning amplifying world-model prediction errors into value overestimation via imagination-based critic bootstrapping — is not DreamerV3-specific. It requires three architectural conditions: (a) learned temporal conditioning on dynamics, (b) imagination-based critic training (value bootstrap over model-generated trajectories), and (c) temporal-gap fidelity degradation in the latent dynamics model. Any MBRL system satisfying all three is theoretically susceptible. The strongest generalization evidence comes from the MPC/imagination boundary: TAWM (Nhu et al., ICML 2025) successfully uses dt-conditioning in TD-MPC2's MPC setting because MPC re-plans from real states at each step, breaking the bootstrapping feedback loop that accumulates errors. This architectural contrast localizes CIVO to imagination-based actor-critic as a class — not DreamerV3 alone. Testing TD-MPC2 in imagination mode, IRIS, and TWM is explicit future work; our contribution is establishing the causal mechanism and diagnostic framework that enables such testing.\n\n**Evidence**: CIVO mechanism requires (a) + (b) + (c) jointly (§Discussion). TAWM succeeds with dt-conditioning in MPC (re-planning from real states) but would face CIVO risk in imagination mode — this is the MPC-immunity prediction (Appendix §MPC Immune). The RSSM develops a 2.78× reward prediction gap under trained conditioning (Table: RSSM fidelity). Gradient-causality dissociation (gradient magnitude ≠ causal importance) is architecture-agnostic — applicable to any multi-head MBRL system. The three-condition framework provides a concrete testable prediction for other architectures.\n\n---\n\n## Q10: Environment diversity is limited — only 2 DMC + 3 ManiSkill tasks\n\n**Anticipated question**: \"Five environments (2 locomotion, 3 manipulation) is a narrow evaluation. The locomotion environments are both simple DMC tasks. How can you claim generalizability with such limited environment diversity?\"\n\n**Response**: The five environments serve distinct roles in the experimental design, and the evidence base is not five independent data points but 133 experiments across 43 configurations. Walker and Cheetah represent qualitatively different CIVO severity regimes: Walker exhibits moderate CIVO (NVE 2–5×) with self-correction capacity (170K steps to recover), while Cheetah exhibits extreme CIVO (NVE 8–108×) with irreversible damage (gate permanently collapsed, eval stuck at 23.4 after 300K steps). This severity continuum is a scientific finding, not a limitation. The three ManiSkill environments (PickCube, PegInsertion, StackCube) serve as negative controls that establish the domain boundary where dt_emb-dependent CIVO does not trigger. Crucially, the negative controls are *informative*: the D146 ordering reversal in PegInsertion (frozen seed 1 spike 11.32 > trained seed 1 spike 3.08) falsifies dt_emb causality for manipulation-task value spikes, confirming these are environment-driven transients rather than undetected CIVO. Each environment contributes multiple configurations (frozen, trained, removed, dual-critic, TCN, SGS), yielding 133 total experiments — the statistical power comes from systematic interventional variation, not environment count.\n\n**Evidence**: Walker moderate CIVO — 5/5 onset, NVE 1.53–4.72×, IQM=148.8 (n=5). Cheetah extreme CIVO — 2/2 collapse, NVE 8.27–108.52×, eval 23.4–51.7. ManiSkill negative controls — 0/5 dt_emb-dependent CIVO: PickCube NVE self-corrects to 0.2 regardless of config; PegInsertion D146 ordering reversal (exp_055 trained s1 peak 3.08 < exp_056 frozen s1 peak 11.32); StackCube frozen control shows identical spike (4.30×) to trained (5.05×). Total: 5 environments × multiple configs = 133 experiments, 63 successful. Fisher exact p=0.003 for three-way causal test across environments.\n\n---\n\n## Q11: How does CIVO relate to overestimation bias in model-free methods (TD3/SAC)?\n\n**Anticipated question**: \"Value overestimation is a well-studied problem in model-free RL — TD3 and SAC already address it with clipped double Q-learning. How is CIVO different from standard overestimation bias? Why don't existing model-free solutions (twin critics with min operation) work?\"\n\n**Response**: CIVO is mechanistically distinct from model-free overestimation bias. In TD3/SAC, overestimation arises from function approximation error in the critic — the max operator over noisy Q-estimates introduces a positive bias. The twin-critic min operation effectively counters this because the two critics have independent approximation errors. In CIVO, overestimation arises from *world-model prediction errors compounding over imagined trajectories*, amplified by temporal conditioning. The causal chain is: trained dt_emb → biased temporal conditioning on world model → compounding prediction error over imagination horizon → systematically inflated value targets → actor exploitation of inflated values → further world-model distortion (feedback loop). The critical difference: in CIVO, both critics are trained on the *same* RSSM-generated imagination trajectories, so they share the same systematic bias. Empirically, dual critics in DreamerV3 converge to ρ > 0.999 correlation across all 7 tested configurations, with pessimism at only 3–4% of the independent-critic bound (§Architecture-Level Ablation). The min operation is thus ineffective against CIVO because it addresses *independent* estimation noise, not *shared* systematic bias from a corrupted generative model. This is precisely why CIVO requires model-level or embedding-level intervention rather than critic-level fixes.\n\n**Evidence**: Dual-critic convergence — ρ > 0.999 across n=7 configurations, pessimism 3–4% of independent-critic bound (§Architecture-Level Ablation). Wide dual-critic provides regularization through uncharacterized mechanisms (3/4 Walker prevention) but fails on Cheetah (0/1). RAVE (value-level capping, analogous to model-free solutions) also fails: 0/2 seeds, EMA anchor tracks biased values during CIVO onset. RSSM reward prediction gap: 2.78× under trained conditioning — this is the upstream bias that twin critics cannot correct. Embedding removal (5/5 prevention) confirms the fix must target the bias source, not the critic.\n\n---\n\n## Q12: Why doesn't CIVO appear in ManiSkill manipulation tasks?\n\n**Anticipated question**: \"You claim CIVO is absent in manipulation (0/5 seeds), but you don't convincingly explain why. Is it reward structure? Observation modality? Dynamics? Without understanding the boundary conditions, the result is merely an observation, not a mechanistic finding.\"\n\n**Response**: We acknowledge that identifying the precise mediator of the locomotion/manipulation boundary is an open question, and we state this explicitly in §Discussion. What we *can* rule out is reward sparsity: all five environments (DMC and ManiSkill) use dense shaped rewards, so reward density cannot explain the boundary. We identify three candidate mediators that differ systematically between the domains. First, action-space periodicity: locomotion requires sustained periodic coordination (gait cycles), where temporal conditioning errors accumulate coherently; manipulation involves episodic, contact-gated dynamics where the relevant horizon resets at each contact transition. Second, observation structure: DMC locomotion uses low-dimensional proprioceptive states where the RSSM can develop spurious temporal shortcuts; ManiSkill uses richer state representations including object poses. Third, continuous vs. contact-gated dynamics: locomotion dynamics evolve continuously (smooth state transitions amenable to temporal extrapolation), while manipulation involves discrete contact mode switches that limit temporal prediction utility. The value of the negative result is diagnostic: the frozen-embedding diagnostic correctly identifies ManiSkill value spikes as non-CIVO (environment-driven transients), validating NVE as a domain-aware diagnostic that does not produce false positives in manipulation tasks.\n\n**Evidence**: All 5 environments use dense shaped rewards — reward sparsity ruled out (§Discussion). PegInsertion D146 ordering reversal falsifies dt_emb causality: frozen s1 peak 11.32 > trained s1 peak 3.08. PickCube NVE self-corrects to 0.2 regardless of dt_emb config (trained/frozen/dual-critic). StackCube frozen control spike 4.30× ≈ trained spike 5.05× — no trained > frozen ordering. Candidate mediators identified: action-space periodicity, observation structure, continuous vs. contact-gated dynamics (§Discussion). 0/5 manipulation false positives validates NVE diagnostic specificity across domains.\n\n---\n\n## Q13: All SGS variants fail — what does this tell us about the mechanism?\n\n**Anticipated question**: \"You test three SGS variants and achieve only 1/11 CIVO prevention (9% success rate). If gradient stopping doesn't work at any level, does this mean dt_emb isn't actually the cause? Or is your intervention methodology flawed?\"\n\n**Response**: The SGS failure is itself a mechanistic finding, not a methodological shortcoming. Gradient stopping addresses *backward-pass* gradient flow to the dt_emb, but CIVO operates through *forward-pass* representational conditioning. In the forward pass, the trained dt_emb conditions every RSSM transition step — this conditioning biases latent state representations regardless of whether gradients flow back through the embedding. SGS confirms that the vulnerability is irreducible at the gradient level: even blocking all non-KL gradients (Full-pathway SGS, 0/3 seeds) cannot prevent the representational damage that a trained, exposed dt_emb inflicts on world-model predictions. The gradient decomposition analysis reveals a deeper insight: gradient magnitude does not predict causal importance. The reward head contributes 38–49% of the total gradient to dt_emb but is causally irrelevant — blocking it alone (Reward-only SGS, 0/2) and including it (Full-SGS) yield the same failure. The observation decoder contributes only 16–22% but carries the critical signal: obs-decoder-only SGS achieves the sole 1/6 success. This dissociation between gradient share and causal importance is a general methodological contribution applicable to any multi-head architecture — it warns against using gradient magnitude as a proxy for causal influence in multi-loss systems.\n\n**Evidence**: SGS results — Reward-only SGS 0/2, Full-pathway SGS 0/3, Obs-decoder SGS 1/6 → total 1/11 (9%) (Table: Intervention Hierarchy). Gradient decomposition at exp_008d_55K: reward 49.0%, KL 34.7%, observation 16.3%, continuation 0.0%. At exp_009e_112K: reward 38.1%, KL 40.4%, observation 21.5%. Reward-detach condition (exp_044): CIVO onset not prevented (peak NVE 4.45×), delayed self-correction (eval 44→538 over 224K, 59% baseline) — lower asymptote than spontaneous recovery (exp_045: 868, 95%). Full-SGS exp_018: s1 partial mitigation (eval 448, NVE 1.66×), s2 collapse. The forward-pass conditioning mechanism explains why gradient-level intervention is fundamentally insufficient.\n\n---\n\n## Q14: Seed count per condition is too small — are the statistics reliable?\n\n**Anticipated question**: \"Individual conditions have 1–4 seeds. Fisher's exact test on such small samples has limited power. Your p=0.003 relies on pooling across conditions. Isn't the 100% onset rate (7/7) just an artifact of not running enough seeds to see failures?\"\n\n**Response**: The statistical argument rests on multiple independent lines of evidence that converge, not on any single small-sample comparison. First, the *perfect separation* between trained (7/7 onset) and frozen/removed (0/5 CIVO-free in locomotion) is the relevant test — Fisher exact p=0.003 for the three-way comparison (trained/frozen/removed). Second, the 7/7 onset figure combines two independent environments (Walker 5/5, Cheetah 2/2), each with distinct CIVO severity profiles, so environment-specific luck is unlikely. Third, the aggregate intervention evidence shows overwhelming separation: embedding removal succeeds 5/5 while all other interventions combined succeed 8/32 — this is not a borderline effect. Fourth, where seed variance matters, we report it transparently as instability evidence: TCN σ=0.2 Walker shows 2/4 success with eval retention ranging 45–91%, which we interpret as unreliability, not as a positive result. We follow Agarwal et al. (2021) in reporting IQM with stratified bootstrap CIs (IQM=148.8 for trained Walker, n=5) rather than claiming significance from small n. The compute budget (~40 GPU-days) was allocated to maximize mechanistic coverage (7 intervention types × 4 hierarchy levels × 5 environments) over per-condition replication — a deliberate design choice that prioritizes breadth of causal evidence over depth of per-condition statistics.\n\n**Evidence**: Three-way Fisher exact p=0.003: trained 7/7 onset vs. frozen 5/7 transient-only (0/7 sustained) vs. removed 0/5. Walker onset: 5/5 seeds (s1–s5), NVE 1.53–4.72×. Cheetah onset: 2/2 seeds, NVE 8.27–108.52×. IQM=148.8 (Walker trained, n=5; Agarwal et al. 2021). Intervention aggregate: removal 5/5 vs. others 8/32. Total evidence: 133 experiments, 63 successful, 35 negative across 43 configurations. TCN instability reported: σ=0.2 Walker s2 NVE 2.11× vs. s3 NVE 3.04× (late-onset CIVO). Dual-critic 2×2 factorial fully populated (4 cells, n=2 each).\n\n---\n\n## Q15: The NVE 1.5× threshold — how sensitive are your claims to this specific cutoff?\n\n**Anticipated question**: \"You claim AUROC=0.957 for NVE-based CIVO detection, but this is in-sample on n=30. The threshold 1.5× seems like it could be overfit. What happens at 1.3× or 2.0×? Is there held-out validation?\"\n\n**Response**: The 1.5× threshold was not post-hoc selected to maximize accuracy — it was pre-specified based on the initial factorial experiments and independently validated. Youden-optimal threshold from ROC analysis is 1.53×, converging on our pre-specified 1.5× without tuning. In-sample AUROC is 0.957 (27/30 correct, n=30 configurations across 2 environments). Critically, we perform Leave-One-Environment-Out (LOEO) cross-validation across Walker (n=15), Cheetah (n=5), and PickCube (n=2): the threshold falls within the optimal accuracy range for all three training folds, yielding mean held-out AUROC=0.988 and mean accuracy=0.978. The single cross-validation error is exp_008e_v3 seed 2 — an Imagination-Reality Divergence (IRD) collapse mechanistically distinct from CIVO, which produces one of only three non-CIVO false positives. Claims are stable across a wide threshold range: at 1.3× the only change is 2 additional borderline transients reclassified (no sustained CIVO misses); at 2.0× we lose early detection of moderate Walker CIVO but all severe cases remain captured. We acknowledge in-sample calibration as a limitation and recommend held-out validation on other MBRL architectures as future work.\n\n**Evidence**: In-sample AUROC=0.957, accuracy 27/30 (n=30, 2 environments). LOEO cross-validation (3 folds): PickCube held-out 2/2 accuracy, AUROC 1.000; Cheetah held-out 5/5 accuracy, AUROC 1.000; Walker held-out 14/15 accuracy, AUROC 0.963. Mean LOEO AUROC=0.988, mean accuracy=0.978. Youden-optimal threshold 1.53× — within 2% of pre-specified 1.5×. Optimal threshold range in training folds: (1.45, 1.53] when Walker available, (1.00, 3.78) when training on Cheetah+PickCube only. Three in-sample FPs: exp_025 obs-SGS s2 (NVE 1.54×, borderline), exp_028 RAVE ceil15 (NVE 1.52×, borderline), exp_008e_v3 s2 (IRD, mechanistically distinct). Threshold sensitivity: 1.3× adds 2 FPs, 2.0× misses moderate Walker onset — claims stable across [1.3×, 2.0×] range.\n",
      "numLines": 150,
      "startLine": 1,
      "totalLines": 150
    }
  }
}
```

</details>

---

### Tool call

_source line 30_

<details open><summary>🔧 Tool call — Read · `toolu_01SXV9oKFsZdZWgjuPV7eu1J`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72aab3fa-ba3f-48a9-9029-1cec279461d0",
  "uuid": "dbfffa7b-5052-4e0c-ab5d-f281c44915e6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FKPT34bFQveB4vaHVfxyzp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12121,
      "cache_read_input_tokens": 32216,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12121
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

_source line 31 · 2026-05-25T13:46:38.154Z_

<details><summary>↩ Tool result · `toolu_01SXV9oKFsZdZWgjuPV7eu1J`</summary>

```text
1	% --- APPENDIX ---
2	
3	\section{Complete Experimental Results}
4	\label{sec:complete_results}
5	
6	Table~\ref{tab:complete_results} reports all 43 experimental configurations. The main text (Table~\ref{tab:main_results}) presents the subset most relevant to the causal argument; this table includes the additional variable-rate configurations (006, 007, 005), multi-seed factorial runs (009b, 008d\_s3, 008d\_s4), SGS interventions (018), cross-environment seeds (010b\_s0), and mitigation experiments (008e\_v3).
7	
8	\begin{table*}[t]
9	\centering
10	\caption{Complete experimental results. NVE reports peak $\nve$ in the 35K+ window (\S\ref{sec:metrics}). CIVO-positive seeds are shaded; $\dagger$\,marks a false positive (non-CIVO collapse with elevated NVE).}
11	\label{tab:complete_results}
12	\scriptsize
13	\setlength{\tabcolsep}{3pt}
14	\begin{tabular}{llcccccl}
15	\toprule
16	\textbf{Exp} & \textbf{Config} & \textbf{dt\_emb} & \textbf{Sub} & \textbf{H} & \textbf{Eval@final} & \textbf{NVE} & \textbf{Outcome} \\
17	\midrule
18	001 & Baseline ($\dt{=}1$, s1) & --- & --- & 15 & 915.7 @105K & 1.00$\times$ & Healthy \\
19	001 s2 & Baseline ($\dt{=}1$, s2) & --- & --- & 15 & 443.5 @105K & ---$^e$ & Healthy \\
20	\rowcolor{gray!15}
21	006 & Fixed $\dt{=}2$ & trn & ON & 15 & 132.9 @65K & 4.83$\times$ & Collapsed \\
22	007 & Fixed $\dt{=}4$ & trn & ON & 15 & 152.5 @55K & --- & Collapsed \\
23	005 & Learned gate & adaptive & OFF & 15 & 98.8 @145K & --- & Collapsed \\
24	\midrule
25	\rowcolor{gray!15}
26	008d & Factorial (s1) & trn & ON & 8 & 82.8 @55K$^\heartsuit$ & 4.12$\times$ & Full collapse \\
27	\rowcolor{gray!15}
28	009b & Factorial (s2) & trn & ON & 8 & 267.9 @105K & 1.62$\times$ & Transient CIVO \\
29	\rowcolor{gray!15}
30	008d\_s3 & Factorial (s3) & trn & ON & 8 & 268$^\diamond$ @105K & 1.53$\times$ & Late-onset collapse \\
31	\rowcolor{gray!15}
32	008d\_s4 & Factorial (s4) & trn & ON & 8 & 63.6 @105K & 4.62$\times$ & Full collapse \\
33	\rowcolor{gray!15}
34	059 & Factorial (s5) & trn & ON & 8 & 95.8 @105K & 4.72$\times$ & Collapse$^\dagger$ \\
35	008f & No dt\_emb (s1) & --- & ON & 8 & 503.0 @105K & 0.97$\times$ & Healthy \\
36	008f s4 & No dt\_emb (s4) & --- & ON & 8 & 306.5 @105K & 1.41$\times$ & Healthy \\
37	009c s3 & No dt\_emb (s3) & --- & ON & 8 & 311.9 @105K & 1.04$\times$ & Healthy \\
38	008a & Unexposed emb & exp$^a$ & OFF & 15 & 777.7 @105K & 0.93$\times$ & Healthy \\
39	008a\_s1 & Unexposed emb & exp$^a$ & OFF & 15 & 630.9 @105K & 0.83$\times$ & Healthy \\
40	008a\_s2 & Unexposed emb & exp$^a$ & OFF & 15 & 899.4 @105K & 0.89$\times$ & Healthy \\
41	015b & Frozen emb & frz$^b$ & ON & 8 & 204.2 @105K & 1.45$\times$ & Grad.\ starvation \\
42	022b & Frozen emb + Gumbel gate & frz$^b$ & ON & 8 & 300.7 @105K & 0.63$\times$ & No CIVO \\
43	042 & Frozen emb (dedicated) & frz$^b$ & ON & 8 & 612.0 @105K & 0.19$\times$ & Healthy \\
44	047 & Frozen emb (s1) & frz$^b$ & ON & 8 & 144.2 @215K & 1.71$\times$ & Transient (self-corr.) \\
45	057 & Frozen emb (s2) & frz$^b$ & ON & 8 & 123.9 @215K & 1.88$\times$ & Transient (self-corr.) \\
46	\midrule
47	018 s1 & Full-SGS & trn$^\ddagger$ & ON & 8 & \sgseval{} @105K & \sgsnve{}$\times$$^*$ & Partial mitig.\ (CIVO+) \\
48	\rowcolor{gray!15}
49	018 s2 & Full-SGS & trn$^\ddagger$ & ON & 8 & 40.8 @105K & --- & Collapsed \\
50	008e\_v3 s1 & Mitigation & trn & ON & 15 & 869.9 @105K & 0.94$\times$ & Healthy \\
51	008e\_v3 s2$^\dagger$ & Mitigation & trn & ON & 15 & 137.0 @105K & 3.78$\times$ & Non-CIVO collapse \\
52	\rowcolor{gray!15}
53	008e\_v3 s3 & Mitigation & trn & ON & 15 & 92.7 @105K & 4.02$\times$ & CIVO collapse \\
54	008e\_v3 s4 & Mitigation & trn & ON & 15 & 899.3 @105K & 0.99$\times$ & Healthy \\
55	\midrule
56	\multicolumn{8}{l}{\textit{Cross-environment validation}} \\
57	\rowcolor{gray!15}
58	010b & Cheetah Run & trn & ON & 8 & 51.7 @105K & 8.27$\times$ & Collapsed \\
59	\rowcolor{gray!15}
60	010b\_s0 & Cheetah Run & trn & ON & 8 & 0.83 @105K & 108.52$\times$ & Full collapse \\
61	\rowcolor{gray!15}
62	021 & Cheetah Run & trn$^\ddagger$ & ON & 8 & 221.5 @105K & 9.94$\times$$^d$ & Transient CIVO (self-corr.) \\
63	024b s0 & Cheetah Run & --- & ON & 8 & 96.5 @105K & $<$0.20$\times$ & Healthy \\
64	024b s1 & Cheetah Run & --- & ON & 8 & 77.3 @105K & 0.10$\times$ & Healthy \\
65	008a\_ch s0 & Cheetah Run & exp$^a$ & OFF & 15 & 532.4 @105K & 1.08$\times$ & Healthy \\
66	008a\_ch s1 & Cheetah Run & exp$^a$ & OFF & 15 & 504.4 @105K & 1.29$\times$ & Healthy \\
67	\rowcolor{gray!15}
68	019b & PickCube-v1 & trn & ON & 8 & 26.64 @200K & 3.78$\times$$^c$ & Transient onset \\
69	054 & PickCube-v1 & frz$^b$ & ON & 8 & --- & 8.81$\times$$^h$ & Env.\ transient (ctrl) \\
70	049 & StackCube-v1 & trn & ON & 8 & 34.9 @212K & 5.05$\times$$^f$ & Env.\ transient \\
71	052 & StackCube-v1 & trn & ON & 8 & --- & 4.67$\times$$^f$ & Env.\ transient \\
72	051 & StackCube-v1 & frz$^b$ & ON & 8 & 30.7 @155K & 4.30$\times$$^f$ & Env.\ transient (ctrl) \\
73	050 & PegInsertionSide-v1 & trn & ON & 8 & 20.86 @212K & 10.05$\times$$^g$ & Env.\ dynamics \\
74	053 & PegInsertionSide-v1 & frz$^b$ & ON & 8 & 5.89 & 8.10$\times$$^g$ & Env.\ dynamics (ctrl) \\
75	055 & PegInsertionSide-v1 & trn & ON & 8 & 11.44 @212K & 3.08$\times$$^g$ & Env.\ dynamics \\
76	056 & PegInsertionSide-v1 & frz$^b$ & ON & 8 & 4.37 @212K & 11.32$\times$$^g$ & Env.\ dynamics (ctrl) \\
77	046 & Cheetah Run & frz$^b$ & ON & 8 & 150.5 @215K & 1.35$\times$ & No CIVO \\
78	058 & Cheetah Run & frz$^b$ & ON & 8 & 80.46 @215K & 0.78$\times$ & No CIVO \\
79	\bottomrule
80	\end{tabular}
81	\vspace{1pt}
82	{\raggedright\footnotesize
83	trn = trained ($d{=}32$, subsample ON);
84	trn$^\ddagger$ = full-pathway SGS (all non-KL gradients detached);
85	exp$^a$ = trained, subsample OFF;
86	frz$^b$ = frozen ($d{=}32$, \texttt{requires\_grad=False});
87	--- = removed ($d{=}0$).\\
88	$^*$ Seed 1 only: peak NVE with transient exceedances (1.60$\times$ at 35K, 1.66$\times$ at 95K); self-correcting, no sustained escalation. Seed 2 collapsed.\\
89	$^\diamond$ Transitional; train returns still declining (peak 470 to 139 over final 8K steps). Collapse had not reached equilibrium at 105K.\\
90	$^\dagger$ NVE self-corrected ($4.72\times$ $\to$ $1.22\times$) but policy did not recover (eval 10.5\% of baseline).\\
91	$^c$ NVE normalized against exp\_019a\_v2 (vanilla DreamerV3 on PickCube-v1).\\
92	$^d$ Peak NVE $9.94\times$ at 45K (transient, self-correcting to $<$1$\times$ by 55K); final eval 221.5.\\
93	$^e$ Not used for NVE normalization; reported for completeness. Seed~1 (eval 915.7) is the NVE reference baseline.\\
94	$^f$ StackCube transient: frozen control (exp\_051, peak $4.30\times$ at 42.5K) matches trained (exp\_049/052), self-correcting by 82.5K; environment-specific, not $\dt$-embedding-driven.\\
95	$^g$ PegInsertion environment dynamics: seed~0 trained peaks at $10.05\times$ (82.5K); seed~1 trained (exp\_055) peaks at $3.08\times$ (92.5K), final $0.50\times$ at 212.5K; seed~1 frozen (exp\_056) peaks at $11.32\times$ (82.5K), final $1.19\times$ at 212.5K. Frozen final exceeds trained final; ordering is seed-dependent, ruling out $\dt$-embedding causation.\\
96	$^h$ PickCube environment transient: frozen control peak $8.81\times$ at 62.5K, self-correcting to $0.55\times$ at 72.5K; matches trained (exp\_019b) trajectory.\\
97	$^\heartsuit$ Evaluated at 55K steps due to early termination of exp\_008d; extended run (exp\_009e) reached 131.08 at 105K.\par}
98	\end{table*}
99	
100	\begin{table}[h]
101	\centering
102	\caption{Cross-domain CIVO reproducibility. ``$\dt$-emb-dep.'' indicates trained peaks consistently exceed frozen at matched timepoints across seeds.}
103	\label{tab:cross_domain}
104	\footnotesize
105	\begin{tabular}{llccc}
106	\toprule
107	\textbf{Domain} & \textbf{Environment} & \textbf{Trained} & \textbf{Frz ctrl} & \textbf{$\dt$-emb-dep.\ CIVO} \\
108	\midrule
109	Locomotion & Walker Walk & 5/5 & 0/3 & Yes (NVE $1.53$--$4.72\times$) \\
110	Locomotion & Cheetah Run & 2/2 & 0/2 & Yes (NVE $8.27$--$108.5\times$) \\
111	Manipulation & StackCube-v1 & 0/2 & 0/1 & No (frozen$\approx$trained) \\
112	Manipulation & PegInsertionSide & 0/2 & 0/2 & No (seed-dep.\ ordering) \\
113	Manipulation & PickCube-v1 & 0/1 & 0/1 & No (frozen spike similar) \\
114	\bottomrule
115	\end{tabular}
116	\end{table}
117	
118	\section{NVE Threshold Sensitivity Analysis}
119	\label{sec:appendix_sensitivity}
120	
121	We report the full sensitivity analysis for the NVE diagnostic framework introduced in Section~\ref{sec:results}. The main text reports Task~B2 (any CIVO detection, $\nve \geq 1.5\times$). Here we additionally present Task~B1, which restricts the positive class to \emph{sustained} CIVO, specifically experiments exhibiting persistent, accelerating value overestimation that progresses to performance collapse. Transient CIVO cases (e.g., exp~009b, which self-corrects after a brief excursion above the threshold) are classified as negative in B1.
122	
123	\subsection{Per-Experiment NVE Values}
124	
125	Table~\ref{tab:nve_raw} lists the NVE values at 35K+ training steps for all eleven factorial experiments (including four 008e\_v3 seeds and exp\_059). Experiments are sorted by descending NVE. Experiment 008e\_v3\_s2 exhibits elevated NVE ($3.78\times$) due to Imagination-Reality Divergence (IRD), a mechanistically distinct phenomenon from CIVO, and is classified as negative in both tasks. Experiment 008e\_v3\_s3 exhibits CIVO with NVE $4.02\times$ despite $\Delta t{=}1$ imagination.
126	
127	\begin{table}[ht]
128	\centering
129	\caption{Per-experiment NVE values (35K+ steps) and ground truth labels. $+$ = positive (CIVO), $-$ = negative. IRD = Imagination-Reality Divergence; trans.\ = transient CIVO with self-correction.}
130	\label{tab:nve_raw}
131	\small
132	\begin{tabular}{@{}lrccc@{}}
133	\toprule
134	Experiment & NVE & Mechanism & B1 & B2 \\
135	\midrule
136	006          & 4.83 & sustained CIVO & $+$ & $+$ \\
137	059          & 4.72 & self-correcting CIVO & $-$ & $+$ \\
138	008d         & 4.12 & sustained CIVO & $+$ & $+$ \\
139	008e\_v3\_s3 & 4.02 & CIVO           & $+$ & $+$ \\
140	008e\_v3\_s2 & 3.78 & IRD (non-CIVO) & $-$ & $-$ \\
141	009b         & 1.62 & transient CIVO & $-$ & $+$ \\
142	001          & 1.00 & non-CIVO       & $-$ & $-$ \\
143	008e\_v3\_s4 & 0.99 & non-CIVO       & $-$ & $-$ \\
144	008f         & 0.97 & non-CIVO       & $-$ & $-$ \\
145	008e\_v3\_s1 & 0.94 & non-CIVO       & $-$ & $-$ \\
146	008a         & 0.93 & non-CIVO       & $-$ & $-$ \\
147	\bottomrule
148	\end{tabular}
149	\end{table}
150	
151	\subsection{Multi-Threshold Classification Performance}
152	
153	Table~\ref{tab:sensitivity_b1} reports Task~B1 classification metrics across six NVE thresholds. Task~B1 achieves $\text{AUROC} = 0.917$ because exp\_059 (NVE${=}4.72\times$, self-correcting CIVO, B1-negative) ranks above two sustained-CIVO positives ($4.12\times$, $4.02\times$), breaking the perfect rank separation that held before its inclusion. The optimal threshold lies in the interval $(3.78, 4.02]$; we report $\geq 3.9\times$ as a representative value (accuracy $10/11 = 90.9\%$). Table~\ref{tab:sensitivity_b2} provides the corresponding analysis for Task~B2 ($\text{AUROC} = 0.967$, imperfect separation due to 008e\_v3\_s2).
154	
155	\begin{table*}[t]
156	\centering
157	\caption{\textbf{Task~B1}: Sustained CIVO detection sensitivity analysis ($n_{\text{pos}}=3$, $n_{\text{neg}}=8$, $n=11$, $\text{AUROC}=0.917$). All confidence intervals are two-sided Clopper-Pearson exact binomial ($\alpha=0.05$). $^\dagger$Optimal threshold in $(3.78, 4.02]$; exp\_059 (NVE${=}4.72\times$, B1-negative) is the sole false positive.}
158	\label{tab:sensitivity_b1}
159	\small
160	\setlength{\tabcolsep}{5pt}
161	\begin{tabular}{@{}lcccccccc@{}}
162	\toprule
163	Threshold & TP & FP & FN & TN & Accuracy [95\% CI] & Precision & Recall & F1 \\
164	\midrule
165	$\geq 1.0\times$ & 3 & 4 & 0 & 4 & 63.6\% \; [30.8, 89.1] & 42.9\% & 100\% & 60.0\% \\
166	$\geq 1.2\times$ & 3 & 3 & 0 & 5 & 72.7\% \; [39.0, 94.0] & 50.0\% & 100\% & 66.7\% \\
167	$\geq 1.5\times$ & 3 & 3 & 0 & 5 & 72.7\% \; [39.0, 94.0] & 50.0\% & 100\% & 66.7\% \\
168	\rowcolor{gray!15}
169	$\geq 1.7\times$ & 3 & 2 & 0 & 6 & 81.8\% \; [48.2, 97.7] & 60.0\% & 100\% & 75.0\% \\
170	$\geq 2.0\times$ & 3 & 2 & 0 & 6 & 81.8\% \; [48.2, 97.7] & 60.0\% & 100\% & 75.0\% \\
171	\rowcolor{gray!15}
172	$\geq 3.9\times^\dagger$ & 3 & 1 & 0 & 7 & 90.9\% \; [58.7, 99.8] & 75.0\% & 100\% & 85.7\% \\
173	\bottomrule
174	\end{tabular}
175	\end{table*}
176	
177	\begin{table*}[t]
178	\centering
179	\caption{\textbf{Task~B2}: Any CIVO detection sensitivity analysis ($n_{\text{pos}}=5$, $n_{\text{neg}}=6$, $n=11$, $\text{AUROC}=0.967$). The single false positive at $\geq 1.5\times$ is 008e\_v3\_s2 (IRD mechanism, not CIVO). The $1.5\times$ threshold (highlighted) maximizes F1 while maintaining perfect recall.}
180	\label{tab:sensitivity_b2}
181	\small
182	\setlength{\tabcolsep}{5pt}
183	\begin{tabular}{@{}lcccccccc@{}}
184	\toprule
185	Threshold & TP & FP & FN & TN & Accuracy [95\% CI] & Precision & Recall & F1 \\
186	\midrule
187	$\geq 1.0\times$ & 5 & 2 & 0 & 4 & 81.8\% \; [48.2, 97.7] & 71.4\% & 100\% & 83.3\% \\
188	$\geq 1.2\times$ & 5 & 1 & 0 & 5 & 90.9\% \; [58.7, 99.8] & 83.3\% & 100\% & 90.9\% \\
189	\rowcolor{gray!15}
190	$\geq 1.5\times$ & 5 & 1 & 0 & 5 & 90.9\% \; [58.7, 99.8] & 83.3\% & 100\% & 90.9\% \\
191	$\geq 1.7\times$ & 4 & 1 & 1 & 5 & 81.8\% \; [48.2, 97.7] & 80.0\% & 80.0\% & 80.0\% \\
192	$\geq 2.0\times$ & 4 & 1 & 1 & 5 & 81.8\% \; [48.2, 97.7] & 80.0\% & 80.0\% & 80.0\% \\
193	$\geq 3.9\times$ & 4 & 0 & 1 & 6 & 90.9\% \; [58.7, 99.8] & 100\% & 80.0\% & 88.9\% \\
194	\bottomrule
195	\end{tabular}
196	\end{table*}
197	
198	\begin{table*}[t]
199	\centering
200	\caption{\textbf{Task~B2 (full evaluation set)}: Any CIVO detection across two environments ($n_{\text{pos}}=9$, $n_{\text{neg}}=8$, $n=17$, $\text{AUROC}=0.972$). Includes Walker Walk (15 configurations) and Cheetah Run (2 configurations).}
201	\label{tab:sensitivity_b2_full}
202	\small
203	\setlength{\tabcolsep}{5pt}
204	\begin{tabular}{@{}lcccccccc@{}}
205	\toprule
206	Threshold & TP & FP & FN & TN & Accuracy [95\% CI] & Precision & Recall & F1 \\
207	\midrule
208	$\geq 1.0\times$ & 9 & 2 & 0 & 6 & 88.2\% \; [63.6, 98.5] & 81.8\% & 100\% & 90.0\% \\
209	$\geq 1.2\times$ & 9 & 1 & 0 & 7 & 94.1\% \; [71.3, 99.9] & 90.0\% & 100\% & 94.7\% \\
210	\rowcolor{gray!15}
211	$\geq 1.5\times$ & 9 & 1 & 0 & 7 & 94.1\% \; [71.3, 99.9] & 90.0\% & 100\% & 94.7\% \\
212	$\geq 1.7\times$ & 7 & 1 & 2 & 7 & 82.4\% \; [56.6, 96.2] & 87.5\% & 77.8\% & 82.4\% \\
213	$\geq 2.0\times$ & 7 & 1 & 2 & 7 & 82.4\% \; [56.6, 96.2] & 87.5\% & 77.8\% & 82.4\% \\
214	$\geq 3.9\times$ & 7 & 0 & 2 & 8 & 88.2\% \; [63.6, 98.5] & 100\% & 77.8\% & 87.5\% \\
215	\bottomrule
216	\end{tabular}
217	\end{table*}
218	
219	\subsection{Threshold Recommendation}
220	
221	For the main diagnostic (Task~B2), we recommend $\nve \geq 1.5\times$ as the operating threshold for three reasons:
222	
223	\begin{enumerate}[nosep,leftmargin=*]
224	\item \textbf{Maximum recall.} The $1.5\times$ threshold achieves 100\% recall, detecting all five CIVO cases including the transient case (009b, $\nve = 1.62\times$). Raising the threshold to $1.7\times$ loses 009b, dropping recall to 80.0\%.
225	\item \textbf{Best F1.} At $1.5\times$, F1 = 90.9\%, the highest among all tested thresholds for B2. The single false positive (008e\_v3\_s2) is mechanistically identifiable as IRD rather than CIVO.
226	\item \textbf{Sensitivity--specificity tradeoff.} Lower thresholds ($1.0\times$) add false positives without gaining true positives. Higher thresholds ($\geq 1.7\times$) sacrifice recall without eliminating the 008e\_v3\_s2 false positive (which requires $\tau > 3.78$).
227	\end{enumerate}
228	
229	For Task~B1 (sustained CIVO only), the optimal threshold $\nve \geq 3.9\times$ achieves $10/11$ accuracy ($90.9\%$, 95\% CI: [58.7\%, 99.8\%]); the sole false positive is exp\_059 (NVE${=}4.72\times$, self-correcting CIVO classified as B1-negative).
230	
231	\subsection{Expanded ROC Analysis}
232	\label{sec:roc_analysis}
233	
234	The original $n{=}17$ analysis (Tables~\ref{tab:sensitivity_b1}--\ref{tab:sensitivity_b2_full}) predates the SGS, RAVE, and TCN experiments. We extend the NVE diagnostic evaluation to $n{=}30$ configurations spanning all tested interventions. Figure~\ref{fig:nve_roc} shows the receiver operating characteristic curve with 95\% bootstrap confidence interval (10{,}000 resamples).
235	
236	\begin{figure}[h]
237	\centering
238	\includegraphics[width=0.7\columnwidth]{../../artifacts/figures/nve_roc_curve.pdf}
239	\caption{NVE ROC curve ($n{=}30$ configurations, AUROC${=}0.957$, in-sample, post-hoc). The preset $\nve \geq 1.5\times$ operating point (star) achieves TPR${=}1.00$, FPR${=}0.18$. Three false positives arise from non-CIVO value overestimation: RAVE anchor pollution, obs-decoder SGS side effects, and IRD eval-driven collapse (008e\_v3 seed~2). Threshold calibrated and validated in-sample, post-hoc; cross-architecture validation deferred.}
240	\label{fig:nve_roc}
241	\end{figure}
242	
243	We label a configuration as CIVO-positive if and only if (i)~it uses a trained $\dt$-embedding with multi-rate data exposure, and (ii)~NVE exceeds $1.5\times$ with co-occurring entropy collapse. Configurations exhibiting high NVE through other mechanisms (gradient truncation side effects, value anchor pollution) are labeled non-CIVO.
244	
245	The three false positives (FPR${=}0.18$) are mechanistically distinct from CIVO: (1)~RAVE anchor pollution (exp\_028, the EMA anchor becomes inflated, producing overestimation through a different pathway); (2)~obs-decoder SGS-induced value distortion (exp\_025 seed~2, blocking observation decoder gradients damages the RSSM latent space); (3)~IRD eval-driven collapse (exp\_008e\_v3 seed~2, actor entropy \emph{increases} with evaluation collapse, mechanistically distinct from CIVO's entropy \emph{decrease}). All three produce NVE $> 1.5\times$ through non-CIVO mechanisms, indicating that the NVE diagnostic detects value overestimation broadly rather than CIVO specifically---a feature rather than a limitation for practitioners monitoring deployment health. The closest sub-threshold case (008f seed~4, NVE${=}1.41\times$) lacks $\dt$-conditioning entirely ($d{=}0$); its elevated NVE reflects transient value noise that self-corrects without the positive feedback loop characteristic of CIVO. The closest above-threshold positive (008d seed~3, NVE${=}1.53\times$) exhibits the full CIVO causal chain: trained $\dt$-embedding, entropy decrease, and evaluation collapse to 14\% of baseline.
246	
247	\paragraph{Comprehensive validation ($n{=}56$).}
248	Expanding the evaluation set to all classifiable experiments yields $n{=}56$ ($n_{\text{pos}}{=}24$, $n_{\text{neg}}{=}32$), spanning Walker Walk, Cheetah Run, and multiple intervention configurations (SGS, TCN, dual-critic, frozen embedding). At the $1.5\times$ threshold: AUROC${=}0.990$, precision${=}0.889$, recall${=}1.000$, F1${=}0.941$, accuracy${=}53/56$. The three false positives are: exp\_008e\_v3\_subsample ($1.93\times$, mitigation config with transient VE spike), exp\_047 ($1.71\times$, frozen embedding transient), and exp\_057 ($1.88\times$, frozen embedding transient). All 24 CIVO-positive configurations are correctly detected (FN${=}0$), with CIVO-positive NVE ranging from $1.53\times$ (008d seed~3, late-onset) to $70.64\times$ (010b seed~0, Cheetah). The substantial increase in sample size from $n{=}32$ to $n{=}56$ strengthens confidence in the $1.5\times$ threshold as a robust diagnostic boundary.
249	
250	\subsection{NVE Normalization Robustness}
251	\label{sec:nve_robustness}
252	
253	To assess sensitivity to baseline seed choice, we extend the single-seed baseline (seed~1, eval 915.7 at 105K) to three additional seeds trained to 505K steps (Table~\ref{tab:baseline_seeds}).
254	
255	\begin{table}[h]
256	\centering
257	\caption{Walker Walk baseline seeds at 105K and 505K steps.}
258	\label{tab:baseline_seeds}
259	\footnotesize
260	\begin{tabular}{lcccc}
261	\toprule
262	\textbf{Seed} & \textbf{Eval@105K} & \textbf{Eval@505K} & \textbf{ve@65K} & \textbf{ve@105K} \\
263	\midrule
264	s1 & 915.7 & 970.4 & 0.563 & 0.656 \\
265	s2 & 443.5 & 945.7 & 0.898 & 0.742 \\
266	s3 & 869.0 & 947.7 & --- & 0.664 \\
267	s4 & 922.8 & 938.9 & --- & 0.624 \\
268	\bottomrule
269	\end{tabular}
270	\end{table}
271	
272	Seed~2 exhibits slow convergence (eval 443.5 at 105K, recovering to 945.7 by 512K), confirming non-pathological slow convergence rather than seed failure. Its elevated $v/e$ ratio at 65K (0.898 vs.\ 0.563 for seed~1) reflects the low evaluation denominator rather than pathological value overestimation. Using seed~2 as the sole normalization reference systematically deflates NVE values, causing two marginal CIVO-positive configurations (008d seed~3, peak NVE $1.53\times$; 009b seed~2, peak NVE $1.62\times$) to fall below the $1.5\times$ threshold. Core CIVO cases (peak NVE $> 3\times$) remain correctly classified under all baseline seeds.
273	
274	Single-seed normalization (s1) yields AUROC $= 0.933$ and accuracy 7/8 (87.5\%) on the Walker subset. Four-seed mean normalization yields AUROC $= 0.867$ and accuracy 6/8 (75.0\%): the boundary case exp\_009b flips from $\nve = 1.62\times$ (s1) to $1.23\times$ (4-seed mean), because its peak occurs at 45K when the s1 $v/e$ ratio (0.331) is well below the 4-seed mean (0.436). All high-NVE configurations remain correctly classified (006: $4.84\times \to 4.52\times$; 008d: $4.12\times \to 3.54\times$). The $1.5\times$ threshold thus correctly identifies all strong CIVO cases regardless of baseline choice; sensitivity is confined to configurations within 10\% of the threshold.
275	
276	\paragraph{Normalization conventions.} Walker NVE is normalized against the single-seed baseline (seed~1, exp\_001, 505K steps). Cheetah NVE is normalized against a 5-seed mean baseline (seeds~0--4, each run to ${\sim}$210K steps). The differing seed counts reflect available baseline data; both provide sufficient coverage of the respective experimental windows (Walker: 210K analysis window; Cheetah: 105K analysis window).
277	
278	\paragraph{Limitations.} The initial $n{=}11$ analysis had wide Clopper-Pearson confidence intervals (e.g., 90.9\% accuracy, 95\% CI [58.7\%, 99.8\%]). Progressive expansion to $n{=}30$ (in-sample, AUROC${=}0.957$; Figure~\ref{fig:nve_roc}) and ultimately $n{=}56$ (comprehensive validation, AUROC${=}0.990$, F1${=}0.941$) substantially tightens these bounds. Table~\ref{tab:sensitivity_b2_full} reports the $n{=}17$ two-environment core evaluation. Cross-architecture validation is deferred to future work.
279	
280	\subsection{Leave-One-Environment-Out Cross-Validation}
281	\label{sec:nve_loeo}
282	
283	To assess whether $\theta{=}1.5\times$ generalizes beyond the in-sample evaluation, we perform leave-one-environment-out (LOEO) cross-validation across Walker ($n{=}15$), Cheetah ($n{=}5$), and PickCube ($n{=}2$). For each fold, we hold out all experiments from one environment, select the optimal accuracy-maximizing threshold range on the remaining training set, and evaluate the fixed $\theta{=}1.5\times$ on the held-out environment.
284	
285	\begin{table}[h]
286	\centering
287	\caption{Leave-one-environment-out cross-validation of NVE threshold $\theta=1.5\times$.
288	For each fold, the threshold is validated on an environment whose data was \emph{not} used
289	to select $\theta$. The optimal threshold range on each training set is reported;
290	$\theta=1.5$ falls within the optimal range in all three folds.}
291	\label{tab:nve_loeo}
292	\begin{tabular}{lccccc}
293	\toprule
294	Held-out & $N_{\text{train}}$ & $N_{\text{test}}$ & $\theta_{\text{opt}}$ range & Test Accuracy & Test AUROC \\
295	\midrule
296	PickCube & 20 & 2 & $(1.45,\, 1.53]$ & 2/2 (1.000) & 1.000 \\
297	Cheetah  & 17 & 5 & $(1.45,\, 1.53]$ & 5/5 (1.000) & 1.000 \\
298	Walker   &  7 & 15 & $(1.00,\, 3.78)$ & 14/15 (0.933) & 0.963 \\
299	\midrule
300	\textbf{Mean} & — & — & — & \textbf{0.978} & \textbf{0.988} \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "72aab3fa-ba3f-48a9-9029-1cec279461d0",
  "uuid": "fb5c96ae-426c-4980-b0ec-3333cc770201",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/appendix.tex",
      "content": "% --- APPENDIX ---\n\n\\section{Complete Experimental Results}\n\\label{sec:complete_results}\n\nTable~\\ref{tab:complete_results} reports all 43 experimental configurations. The main text (Table~\\ref{tab:main_results}) presents the subset most relevant to the causal argument; this table includes the additional variable-rate configurations (006, 007, 005), multi-seed factorial runs (009b, 008d\\_s3, 008d\\_s4), SGS interventions (018), cross-environment seeds (010b\\_s0), and mitigation experiments (008e\\_v3).\n\n\\begin{table*}[t]\n\\centering\n\\caption{Complete experimental results. NVE reports peak $\\nve$ in the 35K+ window (\\S\\ref{sec:metrics}). CIVO-positive seeds are shaded; $\\dagger$\\,marks a false positive (non-CIVO collapse with elevated NVE).}\n\\label{tab:complete_results}\n\\scriptsize\n\\setlength{\\tabcolsep}{3pt}\n\\begin{tabular}{llcccccl}\n\\toprule\n\\textbf{Exp} & \\textbf{Config} & \\textbf{dt\\_emb} & \\textbf{Sub} & \\textbf{H} & \\textbf{Eval@final} & \\textbf{NVE} & \\textbf{Outcome} \\\\\n\\midrule\n001 & Baseline ($\\dt{=}1$, s1) & --- & --- & 15 & 915.7 @105K & 1.00$\\times$ & Healthy \\\\\n001 s2 & Baseline ($\\dt{=}1$, s2) & --- & --- & 15 & 443.5 @105K & ---$^e$ & Healthy \\\\\n\\rowcolor{gray!15}\n006 & Fixed $\\dt{=}2$ & trn & ON & 15 & 132.9 @65K & 4.83$\\times$ & Collapsed \\\\\n007 & Fixed $\\dt{=}4$ & trn & ON & 15 & 152.5 @55K & --- & Collapsed \\\\\n005 & Learned gate & adaptive & OFF & 15 & 98.8 @145K & --- & Collapsed \\\\\n\\midrule\n\\rowcolor{gray!15}\n008d & Factorial (s1) & trn & ON & 8 & 82.8 @55K$^\\heartsuit$ & 4.12$\\times$ & Full collapse \\\\\n\\rowcolor{gray!15}\n009b & Factorial (s2) & trn & ON & 8 & 267.9 @105K & 1.62$\\times$ & Transient CIVO \\\\\n\\rowcolor{gray!15}\n008d\\_s3 & Factorial (s3) & trn & ON & 8 & 268$^\\diamond$ @105K & 1.53$\\times$ & Late-onset collapse \\\\\n\\rowcolor{gray!15}\n008d\\_s4 & Factorial (s4) & trn & ON & 8 & 63.6 @105K & 4.62$\\times$ & Full collapse \\\\\n\\rowcolor{gray!15}\n059 & Factorial (s5) & trn & ON & 8 & 95.8 @105K & 4.72$\\times$ & Collapse$^\\dagger$ \\\\\n008f & No dt\\_emb (s1) & --- & ON & 8 & 503.0 @105K & 0.97$\\times$ & Healthy \\\\\n008f s4 & No dt\\_emb (s4) & --- & ON & 8 & 306.5 @105K & 1.41$\\times$ & Healthy \\\\\n009c s3 & No dt\\_emb (s3) & --- & ON & 8 & 311.9 @105K & 1.04$\\times$ & Healthy \\\\\n008a & Unexposed emb & exp$^a$ & OFF & 15 & 777.7 @105K & 0.93$\\times$ & Healthy \\\\\n008a\\_s1 & Unexposed emb & exp$^a$ & OFF & 15 & 630.9 @105K & 0.83$\\times$ & Healthy \\\\\n008a\\_s2 & Unexposed emb & exp$^a$ & OFF & 15 & 899.4 @105K & 0.89$\\times$ & Healthy \\\\\n015b & Frozen emb & frz$^b$ & ON & 8 & 204.2 @105K & 1.45$\\times$ & Grad.\\ starvation \\\\\n022b & Frozen emb + Gumbel gate & frz$^b$ & ON & 8 & 300.7 @105K & 0.63$\\times$ & No CIVO \\\\\n042 & Frozen emb (dedicated) & frz$^b$ & ON & 8 & 612.0 @105K & 0.19$\\times$ & Healthy \\\\\n047 & Frozen emb (s1) & frz$^b$ & ON & 8 & 144.2 @215K & 1.71$\\times$ & Transient (self-corr.) \\\\\n057 & Frozen emb (s2) & frz$^b$ & ON & 8 & 123.9 @215K & 1.88$\\times$ & Transient (self-corr.) \\\\\n\\midrule\n018 s1 & Full-SGS & trn$^\\ddagger$ & ON & 8 & \\sgseval{} @105K & \\sgsnve{}$\\times$$^*$ & Partial mitig.\\ (CIVO+) \\\\\n\\rowcolor{gray!15}\n018 s2 & Full-SGS & trn$^\\ddagger$ & ON & 8 & 40.8 @105K & --- & Collapsed \\\\\n008e\\_v3 s1 & Mitigation & trn & ON & 15 & 869.9 @105K & 0.94$\\times$ & Healthy \\\\\n008e\\_v3 s2$^\\dagger$ & Mitigation & trn & ON & 15 & 137.0 @105K & 3.78$\\times$ & Non-CIVO collapse \\\\\n\\rowcolor{gray!15}\n008e\\_v3 s3 & Mitigation & trn & ON & 15 & 92.7 @105K & 4.02$\\times$ & CIVO collapse \\\\\n008e\\_v3 s4 & Mitigation & trn & ON & 15 & 899.3 @105K & 0.99$\\times$ & Healthy \\\\\n\\midrule\n\\multicolumn{8}{l}{\\textit{Cross-environment validation}} \\\\\n\\rowcolor{gray!15}\n010b & Cheetah Run & trn & ON & 8 & 51.7 @105K & 8.27$\\times$ & Collapsed \\\\\n\\rowcolor{gray!15}\n010b\\_s0 & Cheetah Run & trn & ON & 8 & 0.83 @105K & 108.52$\\times$ & Full collapse \\\\\n\\rowcolor{gray!15}\n021 & Cheetah Run & trn$^\\ddagger$ & ON & 8 & 221.5 @105K & 9.94$\\times$$^d$ & Transient CIVO (self-corr.) \\\\\n024b s0 & Cheetah Run & --- & ON & 8 & 96.5 @105K & $<$0.20$\\times$ & Healthy \\\\\n024b s1 & Cheetah Run & --- & ON & 8 & 77.3 @105K & 0.10$\\times$ & Healthy \\\\\n008a\\_ch s0 & Cheetah Run & exp$^a$ & OFF & 15 & 532.4 @105K & 1.08$\\times$ & Healthy \\\\\n008a\\_ch s1 & Cheetah Run & exp$^a$ & OFF & 15 & 504.4 @105K & 1.29$\\times$ & Healthy \\\\\n\\rowcolor{gray!15}\n019b & PickCube-v1 & trn & ON & 8 & 26.64 @200K & 3.78$\\times$$^c$ & Transient onset \\\\\n054 & PickCube-v1 & frz$^b$ & ON & 8 & --- & 8.81$\\times$$^h$ & Env.\\ transient (ctrl) \\\\\n049 & StackCube-v1 & trn & ON & 8 & 34.9 @212K & 5.05$\\times$$^f$ & Env.\\ transient \\\\\n052 & StackCube-v1 & trn & ON & 8 & --- & 4.67$\\times$$^f$ & Env.\\ transient \\\\\n051 & StackCube-v1 & frz$^b$ & ON & 8 & 30.7 @155K & 4.30$\\times$$^f$ & Env.\\ transient (ctrl) \\\\\n050 & PegInsertionSide-v1 & trn & ON & 8 & 20.86 @212K & 10.05$\\times$$^g$ & Env.\\ dynamics \\\\\n053 & PegInsertionSide-v1 & frz$^b$ & ON & 8 & 5.89 & 8.10$\\times$$^g$ & Env.\\ dynamics (ctrl) \\\\\n055 & PegInsertionSide-v1 & trn & ON & 8 & 11.44 @212K & 3.08$\\times$$^g$ & Env.\\ dynamics \\\\\n056 & PegInsertionSide-v1 & frz$^b$ & ON & 8 & 4.37 @212K & 11.32$\\times$$^g$ & Env.\\ dynamics (ctrl) \\\\\n046 & Cheetah Run & frz$^b$ & ON & 8 & 150.5 @215K & 1.35$\\times$ & No CIVO \\\\\n058 & Cheetah Run & frz$^b$ & ON & 8 & 80.46 @215K & 0.78$\\times$ & No CIVO \\\\\n\\bottomrule\n\\end{tabular}\n\\vspace{1pt}\n{\\raggedright\\footnotesize\ntrn = trained ($d{=}32$, subsample ON);\ntrn$^\\ddagger$ = full-pathway SGS (all non-KL gradients detached);\nexp$^a$ = trained, subsample OFF;\nfrz$^b$ = frozen ($d{=}32$, \\texttt{requires\\_grad=False});\n--- = removed ($d{=}0$).\\\\\n$^*$ Seed 1 only: peak NVE with transient exceedances (1.60$\\times$ at 35K, 1.66$\\times$ at 95K); self-correcting, no sustained escalation. Seed 2 collapsed.\\\\\n$^\\diamond$ Transitional; train returns still declining (peak 470 to 139 over final 8K steps). Collapse had not reached equilibrium at 105K.\\\\\n$^\\dagger$ NVE self-corrected ($4.72\\times$ $\\to$ $1.22\\times$) but policy did not recover (eval 10.5\\% of baseline).\\\\\n$^c$ NVE normalized against exp\\_019a\\_v2 (vanilla DreamerV3 on PickCube-v1).\\\\\n$^d$ Peak NVE $9.94\\times$ at 45K (transient, self-correcting to $<$1$\\times$ by 55K); final eval 221.5.\\\\\n$^e$ Not used for NVE normalization; reported for completeness. Seed~1 (eval 915.7) is the NVE reference baseline.\\\\\n$^f$ StackCube transient: frozen control (exp\\_051, peak $4.30\\times$ at 42.5K) matches trained (exp\\_049/052), self-correcting by 82.5K; environment-specific, not $\\dt$-embedding-driven.\\\\\n$^g$ PegInsertion environment dynamics: seed~0 trained peaks at $10.05\\times$ (82.5K); seed~1 trained (exp\\_055) peaks at $3.08\\times$ (92.5K), final $0.50\\times$ at 212.5K; seed~1 frozen (exp\\_056) peaks at $11.32\\times$ (82.5K), final $1.19\\times$ at 212.5K. Frozen final exceeds trained final; ordering is seed-dependent, ruling out $\\dt$-embedding causation.\\\\\n$^h$ PickCube environment transient: frozen control peak $8.81\\times$ at 62.5K, self-correcting to $0.55\\times$ at 72.5K; matches trained (exp\\_019b) trajectory.\\\\\n$^\\heartsuit$ Evaluated at 55K steps due to early termination of exp\\_008d; extended run (exp\\_009e) reached 131.08 at 105K.\\par}\n\\end{table*}\n\n\\begin{table}[h]\n\\centering\n\\caption{Cross-domain CIVO reproducibility. ``$\\dt$-emb-dep.'' indicates trained peaks consistently exceed frozen at matched timepoints across seeds.}\n\\label{tab:cross_domain}\n\\footnotesize\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Domain} & \\textbf{Environment} & \\textbf{Trained} & \\textbf{Frz ctrl} & \\textbf{$\\dt$-emb-dep.\\ CIVO} \\\\\n\\midrule\nLocomotion & Walker Walk & 5/5 & 0/3 & Yes (NVE $1.53$--$4.72\\times$) \\\\\nLocomotion & Cheetah Run & 2/2 & 0/2 & Yes (NVE $8.27$--$108.5\\times$) \\\\\nManipulation & StackCube-v1 & 0/2 & 0/1 & No (frozen$\\approx$trained) \\\\\nManipulation & PegInsertionSide & 0/2 & 0/2 & No (seed-dep.\\ ordering) \\\\\nManipulation & PickCube-v1 & 0/1 & 0/1 & No (frozen spike similar) \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{NVE Threshold Sensitivity Analysis}\n\\label{sec:appendix_sensitivity}\n\nWe report the full sensitivity analysis for the NVE diagnostic framework introduced in Section~\\ref{sec:results}. The main text reports Task~B2 (any CIVO detection, $\\nve \\geq 1.5\\times$). Here we additionally present Task~B1, which restricts the positive class to \\emph{sustained} CIVO, specifically experiments exhibiting persistent, accelerating value overestimation that progresses to performance collapse. Transient CIVO cases (e.g., exp~009b, which self-corrects after a brief excursion above the threshold) are classified as negative in B1.\n\n\\subsection{Per-Experiment NVE Values}\n\nTable~\\ref{tab:nve_raw} lists the NVE values at 35K+ training steps for all eleven factorial experiments (including four 008e\\_v3 seeds and exp\\_059). Experiments are sorted by descending NVE. Experiment 008e\\_v3\\_s2 exhibits elevated NVE ($3.78\\times$) due to Imagination-Reality Divergence (IRD), a mechanistically distinct phenomenon from CIVO, and is classified as negative in both tasks. Experiment 008e\\_v3\\_s3 exhibits CIVO with NVE $4.02\\times$ despite $\\Delta t{=}1$ imagination.\n\n\\begin{table}[ht]\n\\centering\n\\caption{Per-experiment NVE values (35K+ steps) and ground truth labels. $+$ = positive (CIVO), $-$ = negative. IRD = Imagination-Reality Divergence; trans.\\ = transient CIVO with self-correction.}\n\\label{tab:nve_raw}\n\\small\n\\begin{tabular}{@{}lrccc@{}}\n\\toprule\nExperiment & NVE & Mechanism & B1 & B2 \\\\\n\\midrule\n006          & 4.83 & sustained CIVO & $+$ & $+$ \\\\\n059          & 4.72 & self-correcting CIVO & $-$ & $+$ \\\\\n008d         & 4.12 & sustained CIVO & $+$ & $+$ \\\\\n008e\\_v3\\_s3 & 4.02 & CIVO           & $+$ & $+$ \\\\\n008e\\_v3\\_s2 & 3.78 & IRD (non-CIVO) & $-$ & $-$ \\\\\n009b         & 1.62 & transient CIVO & $-$ & $+$ \\\\\n001          & 1.00 & non-CIVO       & $-$ & $-$ \\\\\n008e\\_v3\\_s4 & 0.99 & non-CIVO       & $-$ & $-$ \\\\\n008f         & 0.97 & non-CIVO       & $-$ & $-$ \\\\\n008e\\_v3\\_s1 & 0.94 & non-CIVO       & $-$ & $-$ \\\\\n008a         & 0.93 & non-CIVO       & $-$ & $-$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Multi-Threshold Classification Performance}\n\nTable~\\ref{tab:sensitivity_b1} reports Task~B1 classification metrics across six NVE thresholds. Task~B1 achieves $\\text{AUROC} = 0.917$ because exp\\_059 (NVE${=}4.72\\times$, self-correcting CIVO, B1-negative) ranks above two sustained-CIVO positives ($4.12\\times$, $4.02\\times$), breaking the perfect rank separation that held before its inclusion. The optimal threshold lies in the interval $(3.78, 4.02]$; we report $\\geq 3.9\\times$ as a representative value (accuracy $10/11 = 90.9\\%$). Table~\\ref{tab:sensitivity_b2} provides the corresponding analysis for Task~B2 ($\\text{AUROC} = 0.967$, imperfect separation due to 008e\\_v3\\_s2).\n\n\\begin{table*}[t]\n\\centering\n\\caption{\\textbf{Task~B1}: Sustained CIVO detection sensitivity analysis ($n_{\\text{pos}}=3$, $n_{\\text{neg}}=8$, $n=11$, $\\text{AUROC}=0.917$). All confidence intervals are two-sided Clopper-Pearson exact binomial ($\\alpha=0.05$). $^\\dagger$Optimal threshold in $(3.78, 4.02]$; exp\\_059 (NVE${=}4.72\\times$, B1-negative) is the sole false positive.}\n\\label{tab:sensitivity_b1}\n\\small\n\\setlength{\\tabcolsep}{5pt}\n\\begin{tabular}{@{}lcccccccc@{}}\n\\toprule\nThreshold & TP & FP & FN & TN & Accuracy [95\\% CI] & Precision & Recall & F1 \\\\\n\\midrule\n$\\geq 1.0\\times$ & 3 & 4 & 0 & 4 & 63.6\\% \\; [30.8, 89.1] & 42.9\\% & 100\\% & 60.0\\% \\\\\n$\\geq 1.2\\times$ & 3 & 3 & 0 & 5 & 72.7\\% \\; [39.0, 94.0] & 50.0\\% & 100\\% & 66.7\\% \\\\\n$\\geq 1.5\\times$ & 3 & 3 & 0 & 5 & 72.7\\% \\; [39.0, 94.0] & 50.0\\% & 100\\% & 66.7\\% \\\\\n\\rowcolor{gray!15}\n$\\geq 1.7\\times$ & 3 & 2 & 0 & 6 & 81.8\\% \\; [48.2, 97.7] & 60.0\\% & 100\\% & 75.0\\% \\\\\n$\\geq 2.0\\times$ & 3 & 2 & 0 & 6 & 81.8\\% \\; [48.2, 97.7] & 60.0\\% & 100\\% & 75.0\\% \\\\\n\\rowcolor{gray!15}\n$\\geq 3.9\\times^\\dagger$ & 3 & 1 & 0 & 7 & 90.9\\% \\; [58.7, 99.8] & 75.0\\% & 100\\% & 85.7\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\begin{table*}[t]\n\\centering\n\\caption{\\textbf{Task~B2}: Any CIVO detection sensitivity analysis ($n_{\\text{pos}}=5$, $n_{\\text{neg}}=6$, $n=11$, $\\text{AUROC}=0.967$). The single false positive at $\\geq 1.5\\times$ is 008e\\_v3\\_s2 (IRD mechanism, not CIVO). The $1.5\\times$ threshold (highlighted) maximizes F1 while maintaining perfect recall.}\n\\label{tab:sensitivity_b2}\n\\small\n\\setlength{\\tabcolsep}{5pt}\n\\begin{tabular}{@{}lcccccccc@{}}\n\\toprule\nThreshold & TP & FP & FN & TN & Accuracy [95\\% CI] & Precision & Recall & F1 \\\\\n\\midrule\n$\\geq 1.0\\times$ & 5 & 2 & 0 & 4 & 81.8\\% \\; [48.2, 97.7] & 71.4\\% & 100\\% & 83.3\\% \\\\\n$\\geq 1.2\\times$ & 5 & 1 & 0 & 5 & 90.9\\% \\; [58.7, 99.8] & 83.3\\% & 100\\% & 90.9\\% \\\\\n\\rowcolor{gray!15}\n$\\geq 1.5\\times$ & 5 & 1 & 0 & 5 & 90.9\\% \\; [58.7, 99.8] & 83.3\\% & 100\\% & 90.9\\% \\\\\n$\\geq 1.7\\times$ & 4 & 1 & 1 & 5 & 81.8\\% \\; [48.2, 97.7] & 80.0\\% & 80.0\\% & 80.0\\% \\\\\n$\\geq 2.0\\times$ & 4 & 1 & 1 & 5 & 81.8\\% \\; [48.2, 97.7] & 80.0\\% & 80.0\\% & 80.0\\% \\\\\n$\\geq 3.9\\times$ & 4 & 0 & 1 & 6 & 90.9\\% \\; [58.7, 99.8] & 100\\% & 80.0\\% & 88.9\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\begin{table*}[t]\n\\centering\n\\caption{\\textbf{Task~B2 (full evaluation set)}: Any CIVO detection across two environments ($n_{\\text{pos}}=9$, $n_{\\text{neg}}=8$, $n=17$, $\\text{AUROC}=0.972$). Includes Walker Walk (15 configurations) and Cheetah Run (2 configurations).}\n\\label{tab:sensitivity_b2_full}\n\\small\n\\setlength{\\tabcolsep}{5pt}\n\\begin{tabular}{@{}lcccccccc@{}}\n\\toprule\nThreshold & TP & FP & FN & TN & Accuracy [95\\% CI] & Precision & Recall & F1 \\\\\n\\midrule\n$\\geq 1.0\\times$ & 9 & 2 & 0 & 6 & 88.2\\% \\; [63.6, 98.5] & 81.8\\% & 100\\% & 90.0\\% \\\\\n$\\geq 1.2\\times$ & 9 & 1 & 0 & 7 & 94.1\\% \\; [71.3, 99.9] & 90.0\\% & 100\\% & 94.7\\% \\\\\n\\rowcolor{gray!15}\n$\\geq 1.5\\times$ & 9 & 1 & 0 & 7 & 94.1\\% \\; [71.3, 99.9] & 90.0\\% & 100\\% & 94.7\\% \\\\\n$\\geq 1.7\\times$ & 7 & 1 & 2 & 7 & 82.4\\% \\; [56.6, 96.2] & 87.5\\% & 77.8\\% & 82.4\\% \\\\\n$\\geq 2.0\\times$ & 7 & 1 & 2 & 7 & 82.4\\% \\; [56.6, 96.2] & 87.5\\% & 77.8\\% & 82.4\\% \\\\\n$\\geq 3.9\\times$ & 7 & 0 & 2 & 8 & 88.2\\% \\; [63.6, 98.5] & 100\\% & 77.8\\% & 87.5\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\subsection{Threshold Recommendation}\n\nFor the main diagnostic (Task~B2), we recommend $\\nve \\geq 1.5\\times$ as the operating threshold for three reasons:\n\n\\begin{enumerate}[nosep,leftmargin=*]\n\\item \\textbf{Maximum recall.} The $1.5\\times$ threshold achieves 100\\% recall, detecting all five CIVO cases including the transient case (009b, $\\nve = 1.62\\times$). Raising the threshold to $1.7\\times$ loses 009b, dropping recall to 80.0\\%.\n\\item \\textbf{Best F1.} At $1.5\\times$, F1 = 90.9\\%, the highest among all tested thresholds for B2. The single false positive (008e\\_v3\\_s2) is mechanistically identifiable as IRD rather than CIVO.\n\\item \\textbf{Sensitivity--specificity tradeoff.} Lower thresholds ($1.0\\times$) add false positives without gaining true positives. Higher thresholds ($\\geq 1.7\\times$) sacrifice recall without eliminating the 008e\\_v3\\_s2 false positive (which requires $\\tau > 3.78$).\n\\end{enumerate}\n\nFor Task~B1 (sustained CIVO only), the optimal threshold $\\nve \\geq 3.9\\times$ achieves $10/11$ accuracy ($90.9\\%$, 95\\% CI: [58.7\\%, 99.8\\%]); the sole false positive is exp\\_059 (NVE${=}4.72\\times$, self-correcting CIVO classified as B1-negative).\n\n\\subsection{Expanded ROC Analysis}\n\\label{sec:roc_analysis}\n\nThe original $n{=}17$ analysis (Tables~\\ref{tab:sensitivity_b1}--\\ref{tab:sensitivity_b2_full}) predates the SGS, RAVE, and TCN experiments. We extend the NVE diagnostic evaluation to $n{=}30$ configurations spanning all tested interventions. Figure~\\ref{fig:nve_roc} shows the receiver operating characteristic curve with 95\\% bootstrap confidence interval (10{,}000 resamples).\n\n\\begin{figure}[h]\n\\centering\n\\includegraphics[width=0.7\\columnwidth]{../../artifacts/figures/nve_roc_curve.pdf}\n\\caption{NVE ROC curve ($n{=}30$ configurations, AUROC${=}0.957$, in-sample, post-hoc). The preset $\\nve \\geq 1.5\\times$ operating point (star) achieves TPR${=}1.00$, FPR${=}0.18$. Three false positives arise from non-CIVO value overestimation: RAVE anchor pollution, obs-decoder SGS side effects, and IRD eval-driven collapse (008e\\_v3 seed~2). Threshold calibrated and validated in-sample, post-hoc; cross-architecture validation deferred.}\n\\label{fig:nve_roc}\n\\end{figure}\n\nWe label a configuration as CIVO-positive if and only if (i)~it uses a trained $\\dt$-embedding with multi-rate data exposure, and (ii)~NVE exceeds $1.5\\times$ with co-occurring entropy collapse. Configurations exhibiting high NVE through other mechanisms (gradient truncation side effects, value anchor pollution) are labeled non-CIVO.\n\nThe three false positives (FPR${=}0.18$) are mechanistically distinct from CIVO: (1)~RAVE anchor pollution (exp\\_028, the EMA anchor becomes inflated, producing overestimation through a different pathway); (2)~obs-decoder SGS-induced value distortion (exp\\_025 seed~2, blocking observation decoder gradients damages the RSSM latent space); (3)~IRD eval-driven collapse (exp\\_008e\\_v3 seed~2, actor entropy \\emph{increases} with evaluation collapse, mechanistically distinct from CIVO's entropy \\emph{decrease}). All three produce NVE $> 1.5\\times$ through non-CIVO mechanisms, indicating that the NVE diagnostic detects value overestimation broadly rather than CIVO specifically---a feature rather than a limitation for practitioners monitoring deployment health. The closest sub-threshold case (008f seed~4, NVE${=}1.41\\times$) lacks $\\dt$-conditioning entirely ($d{=}0$); its elevated NVE reflects transient value noise that self-corrects without the positive feedback loop characteristic of CIVO. The closest above-threshold positive (008d seed~3, NVE${=}1.53\\times$) exhibits the full CIVO causal chain: trained $\\dt$-embedding, entropy decrease, and evaluation collapse to 14\\% of baseline.\n\n\\paragraph{Comprehensive validation ($n{=}56$).}\nExpanding the evaluation set to all classifiable experiments yields $n{=}56$ ($n_{\\text{pos}}{=}24$, $n_{\\text{neg}}{=}32$), spanning Walker Walk, Cheetah Run, and multiple intervention configurations (SGS, TCN, dual-critic, frozen embedding). At the $1.5\\times$ threshold: AUROC${=}0.990$, precision${=}0.889$, recall${=}1.000$, F1${=}0.941$, accuracy${=}53/56$. The three false positives are: exp\\_008e\\_v3\\_subsample ($1.93\\times$, mitigation config with transient VE spike), exp\\_047 ($1.71\\times$, frozen embedding transient), and exp\\_057 ($1.88\\times$, frozen embedding transient). All 24 CIVO-positive configurations are correctly detected (FN${=}0$), with CIVO-positive NVE ranging from $1.53\\times$ (008d seed~3, late-onset) to $70.64\\times$ (010b seed~0, Cheetah). The substantial increase in sample size from $n{=}32$ to $n{=}56$ strengthens confidence in the $1.5\\times$ threshold as a robust diagnostic boundary.\n\n\\subsection{NVE Normalization Robustness}\n\\label{sec:nve_robustness}\n\nTo assess sensitivity to baseline seed choice, we extend the single-seed baseline (seed~1, eval 915.7 at 105K) to three additional seeds trained to 505K steps (Table~\\ref{tab:baseline_seeds}).\n\n\\begin{table}[h]\n\\centering\n\\caption{Walker Walk baseline seeds at 105K and 505K steps.}\n\\label{tab:baseline_seeds}\n\\footnotesize\n\\begin{tabular}{lcccc}\n\\toprule\n\\textbf{Seed} & \\textbf{Eval@105K} & \\textbf{Eval@505K} & \\textbf{ve@65K} & \\textbf{ve@105K} \\\\\n\\midrule\ns1 & 915.7 & 970.4 & 0.563 & 0.656 \\\\\ns2 & 443.5 & 945.7 & 0.898 & 0.742 \\\\\ns3 & 869.0 & 947.7 & --- & 0.664 \\\\\ns4 & 922.8 & 938.9 & --- & 0.624 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nSeed~2 exhibits slow convergence (eval 443.5 at 105K, recovering to 945.7 by 512K), confirming non-pathological slow convergence rather than seed failure. Its elevated $v/e$ ratio at 65K (0.898 vs.\\ 0.563 for seed~1) reflects the low evaluation denominator rather than pathological value overestimation. Using seed~2 as the sole normalization reference systematically deflates NVE values, causing two marginal CIVO-positive configurations (008d seed~3, peak NVE $1.53\\times$; 009b seed~2, peak NVE $1.62\\times$) to fall below the $1.5\\times$ threshold. Core CIVO cases (peak NVE $> 3\\times$) remain correctly classified under all baseline seeds.\n\nSingle-seed normalization (s1) yields AUROC $= 0.933$ and accuracy 7/8 (87.5\\%) on the Walker subset. Four-seed mean normalization yields AUROC $= 0.867$ and accuracy 6/8 (75.0\\%): the boundary case exp\\_009b flips from $\\nve = 1.62\\times$ (s1) to $1.23\\times$ (4-seed mean), because its peak occurs at 45K when the s1 $v/e$ ratio (0.331) is well below the 4-seed mean (0.436). All high-NVE configurations remain correctly classified (006: $4.84\\times \\to 4.52\\times$; 008d: $4.12\\times \\to 3.54\\times$). The $1.5\\times$ threshold thus correctly identifies all strong CIVO cases regardless of baseline choice; sensitivity is confined to configurations within 10\\% of the threshold.\n\n\\paragraph{Normalization conventions.} Walker NVE is normalized against the single-seed baseline (seed~1, exp\\_001, 505K steps). Cheetah NVE is normalized against a 5-seed mean baseline (seeds~0--4, each run to ${\\sim}$210K steps). The differing seed counts reflect available baseline data; both provide sufficient coverage of the respective experimental windows (Walker: 210K analysis window; Cheetah: 105K analysis window).\n\n\\paragraph{Limitations.} The initial $n{=}11$ analysis had wide Clopper-Pearson confidence intervals (e.g., 90.9\\% accuracy, 95\\% CI [58.7\\%, 99.8\\%]). Progressive expansion to $n{=}30$ (in-sample, AUROC${=}0.957$; Figure~\\ref{fig:nve_roc}) and ultimately $n{=}56$ (comprehensive validation, AUROC${=}0.990$, F1${=}0.941$) substantially tightens these bounds. Table~\\ref{tab:sensitivity_b2_full} reports the $n{=}17$ two-environment core evaluation. Cross-architecture validation is deferred to future work.\n\n\\subsection{Leave-One-Environment-Out Cross-Validation}\n\\label{sec:nve_loeo}\n\nTo assess whether $\\theta{=}1.5\\times$ generalizes beyond the in-sample evaluation, we perform leave-one-environment-out (LOEO) cross-validation across Walker ($n{=}15$), Cheetah ($n{=}5$), and PickCube ($n{=}2$). For each fold, we hold out all experiments from one environment, select the optimal accuracy-maximizing threshold range on the remaining training set, and evaluate the fixed $\\theta{=}1.5\\times$ on the held-out environment.\n\n\\begin{table}[h]\n\\centering\n\\caption{Leave-one-environment-out cross-validation of NVE threshold $\\theta=1.5\\times$.\nFor each fold, the threshold is validated on an environment whose data was \\emph{not} used\nto select $\\theta$. The optimal threshold range on each training set is reported;\n$\\theta=1.5$ falls within the optimal range in all three folds.}\n\\label{tab:nve_loeo}\n\\begin{tabular}{lccccc}\n\\toprule\nHeld-out & $N_{\\text{train}}$ & $N_{\\text{test}}$ & $\\theta_{\\text{opt}}$ range & Test Accuracy & Test AUROC \\\\\n\\midrule\nPickCube & 20 & 2 & $(1.45,\\, 1.53]$ & 2/2 (1.000) & 1.000 \\\\\nCheetah  & 17 & 5 & $(1.45,\\, 1.53]$ & 5/5 (1.000) & 1.000 \\\\\nWalker   &  7 & 15 & $(1.00,\\, 3.78)$ & 14/15 (0.933) & 0.963 \\\\\n\\midrule\n\\textbf{Mean} & — & — & — & \\textbf{0.978} & \\textbf{0.988} \\\\",
      "numLines": 300,
      "startLine": 1,
      "totalLines": 1140
    }
  }
}
```

</details>

---

### Tool call

_source line 32_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01MzaKhh3ewMjKjazN37RcnY`</summary>

```json
{
  "project": "event-gated-adaptive-horizon",
  "file": "paper_provenance.yaml",
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
  "session_id": "72aab3fa-ba3f-48a9-9029-1cec279461d0",
  "uuid": "1c99de28-2bb4-4326-9eb8-98633bc09267",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FKPT34bFQveB4vaHVfxyzp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12121,
      "cache_read_input_tokens": 32216,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12121
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

_source line 33 · 2026-05-25T13:46:38.793Z_

<details><summary>↩ Tool result · `toolu_01MzaKhh3ewMjKjazN37RcnY`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper_provenance.yaml\", \"content\": \"paper:\\n  title: 'Why Temporal Abstraction Fails in Imagination-Based RL: A Diagnostic Analysis\\n    of Variable-Rate DreamerV3'\\n  version: 38\\n  generated_at: '2026-05-25T03:36:26.589946+00:00'\\n  source: manual build by Paper Agent — schema v3 matching check_provenance_completeness\\nclaims:\\n- id: C001\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 0\\n  text: every variable-rate configuration of DreamerV3 degrades performance\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_006_fixed_dt2\\n    metric: eval_return_65K\\n    value: 132.86\\n    role: primary_evidence\\n  - exp_id: exp_007_fixed_dt4\\n    metric: peak_return\\n    value: 176.9\\n    role: primary_evidence\\n  - exp_id: exp_005_event_gated_v4\\n    metric: eval_return_145K\\n    value: 98.84\\n    role: primary_evidence\\n  decisions:\\n  - D009\\n  - D015\\n  deprecated: false\\n- id: C002\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 2\\n  text: trained temporal embedding as the causal factor\\n  type: methodological\\n  evidence:\\n  - exp_id: exp_008d_subsample_on_h8\\n    metric: eval_return_55K\\n    value: 82.75\\n    role: primary_evidence\\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\\n    metric: eval_return_105K\\n    value: 503.0\\n    role: control\\n  decisions:\\n  - D021\\n  deprecated: false\\n- id: C003\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 3\\n  text: 2.78x prediction gap between dt=1 and dt=2\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_rssm_fidelity_analysis\\n    metric: 008d_trained_dtEmb.reward_gap\\n    value: 2.78\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C004\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 4\\n  text: 7/8 classification (n=8)\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_008d_subsample_on_h8\\n    metric: peak_nve\\n    value: 4.12\\n    role: true_positive\\n  - exp_id: exp_006_fixed_dt2\\n    metric: model_loss_at_55k\\n    value: 4.853\\n    role: true_positive\\n  - exp_id: exp_009b_008d_walker_s2\\n    metric: peak_nve\\n    value: 1.62\\n    role: true_positive\\n  - exp_id: exp_008e_v3_walker_s2\\n    metric: final_nve\\n    value: 3.78\\n    role: false_positive\\n  decisions:\\n  - D053\\n  deprecated: false\\n- id: C005\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 5\\n  text: stochastic downstream outcomes — full collapse, transient CIVO, oscillatory\\n    degradation\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_008d_subsample_on_h8\\n    metric: eval_return_55K\\n    value: 82.75\\n    role: full_collapse\\n  - exp_id: exp_009b_008d_walker_s2\\n    metric: final_eval_return\\n    value: 267.93\\n    role: transient_civo\\n  - exp_id: exp_009e_008d_walker_s1\\n    metric: final_eval_return\\n    value: 131.08\\n    role: oscillatory\\n  decisions: []\\n  deprecated: false\\n- id: C006\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 6\\n  text: 'restricting imagination to dt=1 does not prevent collapse: one of two seeds\\n    fails'\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_008e_v3_walker_s1\\n    metric: final_eval_return\\n    value: 869.9\\n    role: healthy\\n  - exp_id: exp_008e_v3_walker_s2\\n    metric: final_eval_return\\n    value: 136.96\\n    role: collapsed\\n  - exp_id: exp_009a_baseline_walker_s2\\n    metric: final_eval_return\\n    value: 836.51\\n    role: control\\n  decisions: []\\n  deprecated: false\\n- id: C007\\n  location:\\n    section: introduction\\n    paragraph: 1\\n    sentence: 1\\n  text: fixed dt=2 collapses to 14% of baseline\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_006_fixed_dt2\\n    metric: eval_return_65K\\n    value: 132.86\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C008\\n  location:\\n    section: introduction\\n    paragraph: 1\\n    sentence: 1\\n  text: fixed dt=4 never exceeds 19% of baseline\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_007_fixed_dt4\\n    metric: peak_return\\n    value: 176.9\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C009\\n  location:\\n    section: introduction\\n    paragraph: 1\\n    sentence: 1\\n  text: learned Gumbel-Softmax gate collapses to 11%\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_005_event_gated_v4\\n    metric: eval_return_145K\\n    value: 98.84\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C010\\n  location:\\n    section: methodology\\n    paragraph: 8\\n    sentence: 0\\n  text: baseline runs for 500K steps, peak return 970.4\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_001_baseline\\n    metric: eval_return_peak\\n    value: 970.41\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C011\\n  location:\\n    section: methodology\\n    paragraph: 6\\n    sentence: 3\\n  text: 7/8 accuracy (AUROC=0.933)\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_008d_subsample_on_h8\\n    metric: peak_nve\\n    value: 4.12\\n    role: true_positive\\n  - exp_id: exp_009b_008d_walker_s2\\n    metric: peak_nve\\n    value: 1.62\\n    role: true_positive\\n  decisions:\\n  - D053\\n  - D054\\n  deprecated: false\\n- id: C012\\n  location:\\n    section: results\\n    paragraph: 0\\n    sentence: 1\\n  text: baseline reaches 915.7 at 105K and peaks at 970.4 at 505K\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_001_baseline\\n    metric: eval_return_peak\\n    value: 970.41\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C013\\n  location:\\n    section: results\\n    paragraph: 0\\n    sentence: 2\\n  text: fixed dt=2 peaks at 485.3 at 35K before collapsing to 132.9 by 65K\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_006_fixed_dt2\\n    metric: peak_return\\n    value: 485.3\\n    role: primary_evidence\\n  - exp_id: exp_006_fixed_dt2\\n    metric: eval_return_65K\\n    value: 132.86\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C014\\n  location:\\n    section: results\\n    paragraph: 0\\n    sentence: 3\\n  text: fixed dt=4 peaks at 176.9 at 25K\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_007_fixed_dt4\\n    metric: peak_return\\n    value: 176.9\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C015\\n  location:\\n    section: results\\n    paragraph: 0\\n    sentence: 4\\n  text: learned-gate peaks at 541.2 at 55K collapses to 98.8 by 145K\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_005_event_gated_v4\\n    metric: peak_return\\n    value: 541.18\\n    role: primary_evidence\\n  - exp_id: exp_005_event_gated_v4\\n    metric: eval_return_145K\\n    value: 98.84\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C016\\n  location:\\n    section: results\\n    paragraph: 3\\n    sentence: 0\\n  text: 008d NVE=4.12x at 55K, collapse eval 167→82.8\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_008d_subsample_on_h8\\n    metric: eval_return_55K\\n    value: 82.75\\n    role: primary_evidence\\n  - exp_id: exp_008d_subsample_on_h8\\n    metric: eval_return_25K\\n    value: 167.22\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C017\\n  location:\\n    section: results\\n    paragraph: 3\\n    sentence: 1\\n  text: 008f NVE=0.30x at 105K, no collapse eval 503.0\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\\n    metric: eval_return_105K\\n    value: 503.0\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C018\\n  location:\\n    section: results\\n    paragraph: 4\\n    sentence: 0\\n  text: AUROC=0.933, Clopper-Pearson 95% CI [0.47, 1.0]\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_008d_subsample_on_h8\\n    metric: peak_nve\\n    value: 4.12\\n    role: true_positive\\n  - exp_id: exp_009b_008d_walker_s2\\n    metric: peak_nve\\n    value: 1.62\\n    role: true_positive\\n  - exp_id: exp_008e_v3_walker_s2\\n    metric: final_nve\\n    value: 3.78\\n    role: false_positive\\n  decisions:\\n  - D054\\n  deprecated: false\\n- id: C019\\n  location:\\n    section: results\\n    paragraph: 4\\n    sentence: 1\\n  text: gap between lowest TP (1.62x) and highest TN (1.00x) is 0.62\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_009b_008d_walker_s2\\n    metric: peak_nve\\n    value: 1.62\\n    role: true_positive\\n  decisions: []\\n  deprecated: false\\n- id: C020\\n  location:\\n    section: results\\n    paragraph: 6\\n    sentence: 0\\n  text: 'Seed 0 (008d) full collapse: eval 167→82.8, value +130%'\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_008d_subsample_on_h8\\n    metric: eval_return_55K\\n    value: 82.75\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C021\\n  location:\\n    section: results\\n    paragraph: 7\\n    sentence: 0\\n  text: 'Seed 2 (009b) transient CIVO: NVE 1.62x at 45K, self-corrects to 0.38x, eval\\n    267.9'\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_009b_008d_walker_s2\\n    metric: final_eval_return\\n    value: 267.93\\n    role: primary_evidence\\n  - exp_id: exp_009b_008d_walker_s2\\n    metric: final_nve\\n    value: 0.38\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C022\\n  location:\\n    section: results\\n    paragraph: 8\\n    sentence: 0\\n  text: 'Seed 1 (009e) oscillatory: eval 82.7-250, settles 131.1, peak NVE=4.12x,\\n    final 1.57x'\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_009e_008d_walker_s1\\n    metric: final_eval_return\\n    value: 131.08\\n    role: primary_evidence\\n  - exp_id: exp_009e_008d_walker_s1\\n    metric: final_nve\\n    value: 1.57\\n    role: primary_evidence\\n  - exp_id: exp_009e_008d_walker_s1\\n    metric: peak_nve\\n    value: 4.12\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C023\\n  location:\\n    section: results\\n    paragraph: 10\\n    sentence: 0\\n  text: 008a reaches 777.7 (NVE=0.59x)\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_008a_no_subsample_dt2\\n    metric: eval_return_105K\\n    value: 777.66\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C024\\n  location:\\n    section: results\\n    paragraph: 10\\n    sentence: 0\\n  text: 008c reaches 240.9 (NVE=0.58x)\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_008c_no_subsample_dt2_h8\\n    metric: eval_return_65K\\n    value: 240.86\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C025\\n  location:\\n    section: results\\n    paragraph: 12\\n    sentence: 0\\n  text: dt=1 (915.7) > dt=2 (485.3, -47%) > dt=4 (176.9, -81%)\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_006_fixed_dt2\\n    metric: peak_return\\n    value: 485.3\\n    role: primary_evidence\\n  - exp_id: exp_007_fixed_dt4\\n    metric: peak_return\\n    value: 176.9\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C026\\n  location:\\n    section: results\\n    paragraph: 14\\n    sentence: 0\\n  text: 008d collapses NVE=4.12x vs untrained configs NVE<0.6x\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_008d_subsample_on_h8\\n    metric: eval_return_55K\\n    value: 82.75\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C027\\n  location:\\n    section: results\\n    paragraph: 14\\n    sentence: 1\\n  text: 'cross-seed variance: 008f 503.0 vs 009c 148.3'\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\\n    metric: eval_return_105K\\n    value: 503.0\\n    role: primary_evidence\\n  - exp_id: exp_009c_008f_walker_s2\\n    metric: final_eval_return\\n    value: 148.34\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C028\\n  location:\\n    section: results\\n    paragraph: 16\\n    sentence: 0\\n  text: '008e_v3 s1 healthy: eval 869.9 (95% of baseline), NVE=0.80x'\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_008e_v3_walker_s1\\n    metric: final_eval_return\\n    value: 869.9\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C029\\n  location:\\n    section: results\\n    paragraph: 16\\n    sentence: 1\\n  text: '008e_v3 s2 collapsed: eval 715→137, NVE=3.78x'\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_008e_v3_walker_s2\\n    metric: final_eval_return\\n    value: 136.96\\n    role: primary_evidence\\n  - exp_id: exp_008e_v3_walker_s2\\n    metric: peak_eval_return\\n    value: 715.21\\n    role: primary_evidence\\n  - exp_id: exp_008e_v3_walker_s2\\n    metric: final_nve\\n    value: 3.78\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C030\\n  location:\\n    section: results\\n    paragraph: 17\\n    sentence: 0\\n  text: baseline seed 2 (009a) stable at 836.5\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_009a_baseline_walker_s2\\n    metric: final_eval_return\\n    value: 836.51\\n    role: control\\n  decisions: []\\n  deprecated: false\\n- id: C031\\n  location:\\n    section: results\\n    paragraph: 18\\n    sentence: 1\\n  text: '008e_v3_s2 Pathway B: entropy increases (-5.21→-3.83)'\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_008e_v3_walker_s2\\n    metric: final_eval_return\\n    value: 136.96\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C032\\n  location:\\n    section: results\\n    paragraph: 19\\n    sentence: 0\\n  text: 008e_v3_s2 NVE=3.78x false positive (non-CIVO)\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_008e_v3_walker_s2\\n    metric: final_nve\\n    value: 3.78\\n    role: false_positive\\n  decisions:\\n  - D053\\n  deprecated: false\\n- id: C033\\n  location:\\n    section: results\\n    paragraph: 21\\n    sentence: 0\\n  text: 008d reward gap 2.78x (dt1 MAE=0.0568, dt2 MAE=0.1579)\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_rssm_fidelity_analysis\\n    metric: 008d_trained_dtEmb.reward_gap\\n    value: 2.78\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C034\\n  location:\\n    section: results\\n    paragraph: 21\\n    sentence: 1\\n  text: 008f reward gap 1.01x (MAE 0.7469)\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_rssm_fidelity_analysis\\n    metric: 008f_no_dtEmb.reward_gap\\n    value: 1.01\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C035\\n  location:\\n    section: results\\n    paragraph: 21\\n    sentence: 1\\n  text: 008f absolute MAE 0.7469 vs 008d 0.0568 at dt=1\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_rssm_fidelity_analysis\\n    metric: 008f_no_dtEmb.dt1_reward_mae\\n    value: 0.7469\\n    role: primary_evidence\\n  - exp_id: exp_rssm_fidelity_analysis\\n    metric: 008d_trained_dtEmb.dt1_reward_mae\\n    value: 0.0568\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C036\\n  location:\\n    section: analysis\\n    paragraph: 2\\n    sentence: 0\\n  text: 'two-stage amplification: Stage 1 dynamics bias 1.68x, Stage 2 actor exploitation\\n    2.90x'\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_008d_subsample_on_h8\\n    metric: random_policy_reward_ratio\\n    value: 1.68\\n    role: stage1\\n  - exp_id: exp_008d_subsample_on_h8\\n    metric: trained_actor_reward_ratio\\n    value: 2.9\\n    role: stage2\\n  decisions:\\n  - D042\\n  deprecated: false\\n- id: C037\\n  location:\\n    section: analysis\\n    paragraph: 2\\n    sentence: 1\\n  text: ~36% dynamics bias, ~64% actor exploitation\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_008d_subsample_on_h8\\n    metric: dynamics_bias_fraction\\n    value: 0.36\\n    role: primary_evidence\\n  decisions:\\n  - D042\\n  deprecated: false\\n- id: C038\\n  location:\\n    section: analysis\\n    paragraph: 2\\n    sentence: 2\\n  text: '008f control: random 1.11x, trained 0.98x — no effect'\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\\n    metric: random_policy_reward_ratio\\n    value: 1.11\\n    role: control\\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\\n    metric: trained_actor_reward_ratio\\n    value: 0.98\\n    role: control\\n  decisions:\\n  - D042\\n  deprecated: false\\n- id: C039\\n  location:\\n    section: analysis\\n    paragraph: 4\\n    sentence: 0\\n  text: all runs cross NVE>1.5x — CIVO triggers deterministically\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_008d_subsample_on_h8\\n    metric: peak_nve\\n    value: 4.12\\n    role: primary_evidence\\n  - exp_id: exp_009b_008d_walker_s2\\n    metric: peak_nve\\n    value: 1.62\\n    role: primary_evidence\\n  - exp_id: exp_009e_008d_walker_s1\\n    metric: peak_nve\\n    value: 4.12\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C040\\n  location:\\n    section: analysis\\n    paragraph: 7\\n    sentence: 0\\n  text: 'removing dt_emb: 13x cost to reward prediction (0.7469 vs 0.0568)'\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_rssm_fidelity_analysis\\n    metric: 008f_no_dtEmb.dt1_reward_mae\\n    value: 0.7469\\n    role: primary_evidence\\n  - exp_id: exp_rssm_fidelity_analysis\\n    metric: 008d_trained_dtEmb.dt1_reward_mae\\n    value: 0.0568\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C041\\n  location:\\n    section: analysis\\n    paragraph: 8\\n    sentence: 1\\n  text: 'Pathway B FP: 008e_v3_s2 NVE=3.78x non-CIVO'\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_008e_v3_walker_s2\\n    metric: final_nve\\n    value: 3.78\\n    role: false_positive\\n  decisions:\\n  - D053\\n  deprecated: false\\n- id: C042\\n  location:\\n    section: conclusion\\n    paragraph: 0\\n    sentence: 2\\n  text: 7/8 CIVO classification (n=8, 87.5%)\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_008d_subsample_on_h8\\n    metric: peak_nve\\n    value: 4.12\\n    role: true_positive\\n  - exp_id: exp_009b_008d_walker_s2\\n    metric: peak_nve\\n    value: 1.62\\n    role: true_positive\\n  decisions:\\n  - D053\\n  deprecated: false\\n- id: C043\\n  location:\\n    section: conclusion\\n    paragraph: 2\\n    sentence: 1\\n  text: NVE margin 0.62 excluding outlier\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_009b_008d_walker_s2\\n    metric: peak_nve\\n    value: 1.62\\n    role: lowest_true_positive\\n  decisions: []\\n  deprecated: false\\n- id: C044\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: Extended NVE validation (n=32) achieves F1=0.880 at 1.5x threshold\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C045\\n  location:\\n    section: sections/analysis\\n    paragraph: 0\\n    sentence: 0\\n  text: NVE diagnostic extended validation n=32 AUROC=0.961 F1=0.880\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C046\\n  location:\\n    section: sections/analysis\\n    paragraph: 0\\n    sentence: 0\\n  text: 'Entropy explosion is lagging indicator: +2.1 nats/10K collapsed vs +0.07-0.22\\n    healthy, return collapses ~35K steps before entropy rises'\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C047\\n  location:\\n    section: sections/methodology\\n    paragraph: 0\\n    sentence: 0\\n  text: NVE threshold 29/32 accuracy (AUROC=0.961, F1=0.880) at n=32\\n  type: quantitative\\n  evidence:\\n  - exp_id: plan_034_nve_threshold\\n    metric: auroc_n32\\n    value: 0.961\\n    role: primary_evidence\\n  - exp_id: plan_034_nve_threshold\\n    metric: f1_at_1.5x\\n    value: 0.88\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C048\\n  location:\\n    section: sections/results\\n    paragraph: 0\\n    sentence: 0\\n  text: NVE threshold 29/32 classification (n=32, AUROC=0.961, F1=0.880)\\n  type: quantitative\\n  evidence:\\n  - exp_id: plan_034_nve_threshold\\n    metric: auroc_n32\\n    value: 0.961\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C049\\n  location:\\n    section: sections/abstract_body\\n    paragraph: 0\\n    sentence: 0\\n  text: CIVO classification 29/32 AUROC=0.961 F1=0.880\\n  type: quantitative\\n  evidence:\\n  - exp_id: plan_034_nve_threshold\\n    metric: auroc_n32\\n    value: 0.961\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C050\\n  location:\\n    section: sections/introduction\\n    paragraph: 0\\n    sentence: 0\\n  text: NVE threshold 29/32 classification in introduction\\n  type: quantitative\\n  evidence:\\n  - exp_id: plan_034_nve_threshold\\n    metric: auroc_n32\\n    value: 0.961\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C051\\n  location:\\n    section: sections/introduction\\n    paragraph: 0\\n    sentence: 0\\n  text: Contribution 1 AUROC updated to 0.961\\n  type: quantitative\\n  evidence:\\n  - exp_id: plan_034_nve_threshold\\n    metric: auroc_n32\\n    value: 0.961\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C052\\n  location:\\n    section: sections/conclusion\\n    paragraph: 0\\n    sentence: 0\\n  text: Conclusion NVE updated to 29/32 AUROC=0.961\\n  type: quantitative\\n  evidence:\\n  - exp_id: plan_034_nve_threshold\\n    metric: auroc_n32\\n    value: 0.961\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C053\\n  location:\\n    section: sections/analysis\\n    paragraph: 0\\n    sentence: 0\\n  text: Discussion NVE diagnostic consolidated to n=32 AUROC=0.961\\n  type: quantitative\\n  evidence:\\n  - exp_id: plan_034_nve_threshold\\n    metric: auroc_n32\\n    value: 0.961\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C054\\n  location:\\n    section: sections/results\\n    paragraph: 0\\n    sentence: 0\\n  text: RSSM reward prediction gap 2.78x corroborated at 3.11x with 600-sample validation\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_rssm_fidelity_analysis\\n    metric: 008d_trained_dtEmb.reward_gap\\n    value: 2.78\\n    role: primary_evidence\\n  - exp_id: exp_063_rssm_fidelity\\n    metric: collapsed_reward_gap\\n    value: 3.11\\n    role: corroboration\\n  decisions: []\\n  deprecated: false\\n- id: C055\\n  location:\\n    section: sections/results\\n    paragraph: 0\\n    sentence: 0\\n  text: CIVO model median V(s)/MC-return ratio 3.40 vs no-dt-emb control 1.05\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_064_value_distribution\\n    metric: civo_median_v_mc_ratio\\n    value: 3.4\\n    role: primary_evidence\\n  - exp_id: exp_064_value_distribution\\n    metric: control_median_v_mc_ratio\\n    value: 1.05\\n    role: control\\n  decisions: []\\n  deprecated: false\\n- id: C056\\n  location:\\n    section: sections/results\\n    paragraph: 0\\n    sentence: 0\\n  text: 'Return collapses ~35K steps before entropy rises: +2.1 nats/10K collapsed\\n    vs +0.07-0.22 healthy'\\n  type: quantitative\\n  evidence:\\n  - exp_id: plan_031_actor_entropy\\n    metric: collapsed_entropy_rate\\n    value: 2.1\\n    role: primary_evidence\\n  - exp_id: plan_031_actor_entropy\\n    metric: healthy_entropy_rate_range\\n    value: 0.07-0.22\\n    role: control\\n  decisions: []\\n  deprecated: false\\n- id: C057\\n  location:\\n    section: sections/analysis\\n    paragraph: 0\\n    sentence: 0\\n  text: RSSM reward gap 2.78-3.11x range across two independent analyses\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_rssm_fidelity_analysis\\n    metric: 008d_trained_dtEmb.reward_gap\\n    value: 2.78\\n    role: primary_evidence\\n  - exp_id: exp_063_rssm_fidelity\\n    metric: collapsed_reward_gap\\n    value: 3.11\\n    role: corroboration\\n  decisions: []\\n  deprecated: false\\n- id: C058\\n  location:\\n    section: sections/analysis\\n    paragraph: 0\\n    sentence: 0\\n  text: 'Obs-decoder SGS compensatory amplification: NVE from 8.3x to 21.9-30.2x on\\n    Cheetah'\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_026_obs_sgs_cheetah\\n    metric: nve_amplification\\n    value: 21.9-30.2\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C059\\n  location:\\n    section: sections/analysis\\n    paragraph: 0\\n    sentence: 0\\n  text: 'TCN impossible dose: sigma=1.0 Cheetah suppresses CIVO (NVE<=0.3x) but eval→15%\\n    baseline'\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_030c_tcn_cheetah\\n    metric: nve_suppressed\\n    value: 0.3\\n    role: primary_evidence\\n  - exp_id: exp_030c_tcn_cheetah\\n    metric: eval_pct_baseline\\n    value: 15\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C060\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: 'Trained dt_emb cosine similarity: cos(dt1,dt2) = -0.87 to -0.94 at 25K, -0.70\\n    to -0.86 at 75K'\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_065_dt_emb_cosine\\n    metric: trained_cos_25k_range\\n    value: -0.87 to -0.94\\n    role: primary_evidence\\n  - exp_id: exp_065_dt_emb_cosine\\n    metric: trained_cos_75k_range\\n    value: -0.70 to -0.86\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C061\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: 'Frozen dt_emb cosine similarity: near-zero (-0.15 to +0.07), constant'\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_065_dt_emb_cosine\\n    metric: frozen_cos_constant\\n    value: -0.15 to +0.07\\n    role: control\\n  decisions: []\\n  deprecated: false\\n- id: C062\\n  location:\\n    section: sections/introduction\\n    paragraph: 0\\n    sentence: 0\\n  text: RSSM reward prediction gap 2.78-3.11x in introduction\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_rssm_fidelity_analysis\\n    metric: 008d_trained_dtEmb.reward_gap\\n    value: 2.78\\n    role: primary_evidence\\n  - exp_id: exp_063_rssm_fidelity\\n    metric: collapsed_reward_gap\\n    value: 3.11\\n    role: corroboration\\n  decisions: []\\n  deprecated: false\\n- id: C063\\n  location:\\n    section: sections/results\\n    paragraph: 0\\n    sentence: 0\\n  text: RSSM reward MAE increases from 0.057 to 0.178 (3.11x gap) at dt=2 under trained\\n    conditioning\\n  type: quantitative\\n  evidence: exp_063 rssm_fidelity_analysis, 600-sample validation\\n  decisions: []\\n  deprecated: false\\n- id: C064\\n  location:\\n    section: sections/results\\n    paragraph: 0\\n    sentence: 0\\n  text: Observation reconstruction gap improves with temporal conditioning (1.33x\\n    vs baseline 1.46x)\\n  type: quantitative\\n  evidence: exp_063 obs_mse data\\n  decisions: []\\n  deprecated: false\\n- id: C065\\n  location:\\n    section: sections/results\\n    paragraph: 0\\n    sentence: 0\\n  text: CIVO model mean V/MC ratio = 7.80x (median 3.40x, 100% overestimated) vs control\\n    median 1.05x (52.5% overestimated)\\n  type: quantitative\\n  evidence: exp_064 value_distribution results_summary\\n  decisions: []\\n  deprecated: false\\n- id: C066\\n  location:\\n    section: sections/analysis\\n    paragraph: 0\\n    sentence: 0\\n  text: RSSM reward MAE 0.057→0.178 at dt=2; obs gap 1.33x vs baseline 1.46x — reward-specific\\n    pathology\\n  type: quantitative\\n  evidence: exp_063 rssm_fidelity_analysis\\n  decisions: []\\n  deprecated: false\\n- id: C067\\n  location:\\n    section: sections/results\\n    paragraph: 0\\n    sentence: 0\\n  text: SS fidelity ratio crosses 1.1x at 20K steps, VE ratio first exceeds 1.5x at\\n    40K steps — ~10-15K step lag (r=0.81, p=0.002, n=1)\\n  type: quantitative\\n  evidence: exp_066 timeseries analysis, 12 dense checkpoints\\n  decisions: []\\n  deprecated: false\\n- id: C068\\n  location:\\n    section: sections/results\\n    paragraph: 0\\n    sentence: 0\\n  text: dt=1 MAE decreases 0.093→0.047 while dt=2 MAE plateaus ~0.08 — gap from differential\\n    improvement\\n  type: quantitative\\n  evidence: exp_066 timeseries analysis\\n  decisions: []\\n  deprecated: false\\n- id: C069\\n  location:\\n    section: sections/analysis\\n    paragraph: 0\\n    sentence: 0\\n  text: 'Three-stage causal chain: fidelity gap (20K) → value overestimation (40K)\\n    → entropy destabilization (~35K later), n=1'\\n  type: quantitative\\n  evidence: exp_066 timeseries + actor entropy analysis\\n  decisions: []\\n  deprecated: false\\n- id: C070\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: 'exp_066 timeseries: SS fidelity ratio grows 1.05→1.68 over 10K-65K steps;\\n    VE ratio near zero until 40K spike (1.59x)'\\n  type: quantitative\\n  evidence: exp_066 12-checkpoint timeseries analysis\\n  decisions: []\\n  deprecated: false\\n- id: C071\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: dt=1 MAE 0.090→0.047 (monotonic decrease), dt=2 MAE plateaus ~0.08; gap from\\n    selective improvement not worsening\\n  type: quantitative\\n  evidence: exp_066 timeseries MAE data\\n  decisions: []\\n  deprecated: false\\ntables:\\n- id: T001\\n  location:\\n    section: methodology\\n    table_number: 1\\n  caption: Factorial design — 9 configurations\\n  cells:\\n  - row: 0\\n    col: 0\\n    value: '001'\\n    source:\\n      exp_id: exp_001_baseline\\n      metric: exp_id\\n  - row: 1\\n    col: 0\\n    value: '006'\\n    source:\\n      exp_id: exp_006_fixed_dt2\\n      metric: exp_id\\n  - row: 2\\n    col: 0\\n    value: '007'\\n    source:\\n      exp_id: exp_007_fixed_dt4\\n      metric: exp_id\\n  - row: 3\\n    col: 0\\n    value: '005'\\n    source:\\n      exp_id: exp_005_event_gated_v4\\n      metric: exp_id\\n  - row: 4\\n    col: 0\\n    value: 008d\\n    source:\\n      exp_id: exp_008d_subsample_on_h8\\n      metric: exp_id\\n  - row: 5\\n    col: 0\\n    value: 008f\\n    source:\\n      exp_id: exp_008f_no_dt_embed_subsample_on_h8\\n      metric: exp_id\\n  - row: 6\\n    col: 0\\n    value: 008a\\n    source:\\n      exp_id: exp_008a_no_subsample_dt2\\n      metric: exp_id\\n  - row: 7\\n    col: 0\\n    value: 008c\\n    source:\\n      exp_id: exp_008c_no_subsample_dt2_h8\\n      metric: exp_id\\n  - row: 8\\n    col: 0\\n    value: 008e_v3\\n    source:\\n      exp_id: exp_008e_v3_subsample_on_dt1_h15\\n      metric: exp_id\\n  deprecated: false\\n- id: T002\\n  location:\\n    section: results\\n    table_number: 1\\n  caption: All configurations and outcomes\\n  cells:\\n  - row: 0\\n    col: 5\\n    value: 915.7\\n    source:\\n      exp_id: exp_001_baseline\\n      metric: eval_return_105K\\n  - row: 1\\n    col: 5\\n    value: 132.9\\n    source:\\n      exp_id: exp_006_fixed_dt2\\n      metric: eval_return_65K\\n  - row: 1\\n    col: 6\\n    value: 4.83\\n    source:\\n      exp_id: exp_006_fixed_dt2\\n      metric: peak_nve\\n  - row: 2\\n    col: 5\\n    value: 152.5\\n    source:\\n      exp_id: exp_007_fixed_dt4\\n      metric: eval_return_55K\\n  - row: 3\\n    col: 5\\n    value: 98.8\\n    source:\\n      exp_id: exp_005_event_gated_v4\\n      metric: eval_return_145K\\n  - row: 4\\n    col: 5\\n    value: 82.8\\n    source:\\n      exp_id: exp_008d_subsample_on_h8\\n      metric: eval_return_55K\\n  - row: 4\\n    col: 6\\n    value: 4.12\\n    source:\\n      exp_id: exp_008d_subsample_on_h8\\n      metric: peak_nve\\n  - row: 5\\n    col: 5\\n    value: 267.9\\n    source:\\n      exp_id: exp_009b_008d_walker_s2\\n      metric: final_eval_return\\n  - row: 5\\n    col: 6\\n    value: 1.62\\n    source:\\n      exp_id: exp_009b_008d_walker_s2\\n      metric: peak_nve\\n  - row: 6\\n    col: 5\\n    value: 131.1\\n    source:\\n      exp_id: exp_009e_008d_walker_s1\\n      metric: final_eval_return\\n  - row: 6\\n    col: 6\\n    value: 4.12\\n    source:\\n      exp_id: exp_009e_008d_walker_s1\\n      metric: peak_nve\\n  - row: 7\\n    col: 5\\n    value: 503.0\\n    source:\\n      exp_id: exp_008f_no_dt_embed_subsample_on_h8\\n      metric: eval_return_105K\\n  - row: 8\\n    col: 5\\n    value: 148.3\\n    source:\\n      exp_id: exp_009c_008f_walker_s2\\n      metric: final_eval_return\\n  - row: 9\\n    col: 5\\n    value: 777.7\\n    source:\\n      exp_id: exp_008a_no_subsample_dt2\\n      metric: eval_return_105K\\n  - row: 10\\n    col: 5\\n    value: 240.9\\n    source:\\n      exp_id: exp_008c_no_subsample_dt2_h8\\n      metric: eval_return_65K\\n  - row: 11\\n    col: 5\\n    value: 869.9\\n    source:\\n      exp_id: exp_008e_v3_walker_s1\\n      metric: final_eval_return\\n  - row: 12\\n    col: 5\\n    value: 137.0\\n    source:\\n      exp_id: exp_008e_v3_walker_s2\\n      metric: final_eval_return\\n  - row: 12\\n    col: 6\\n    value: 3.78\\n    source:\\n      exp_id: exp_008e_v3_walker_s2\\n      metric: final_nve\\n  - row: 13\\n    col: 5\\n    value: 836.5\\n    source:\\n      exp_id: exp_009a_baseline_walker_s2\\n      metric: final_eval_return\\n  deprecated: false\\n- id: T003\\n  location:\\n    section: results\\n    table_number: 2\\n  caption: RSSM fidelity at dt=1 vs dt=2\\n  cells:\\n  - row: 0\\n    col: 0\\n    value: 13.49\\n    source:\\n      exp_id: exp_rssm_fidelity_analysis\\n      metric: baseline.dt1_obs_mse\\n  - row: 0\\n    col: 1\\n    value: 27.5\\n    source:\\n      exp_id: exp_rssm_fidelity_analysis\\n      metric: baseline.dt2_obs_mse\\n  - row: 0\\n    col: 2\\n    value: 2.04\\n    source:\\n      exp_id: exp_rssm_fidelity_analysis\\n      metric: baseline.obs_gap\\n  - row: 0\\n    col: 3\\n    value: 0.0102\\n    source:\\n      exp_id: exp_rssm_fidelity_analysis\\n      metric: baseline.dt1_reward_mae\\n  - row: 0\\n    col: 4\\n    value: 0.0159\\n    source:\\n      exp_id: exp_rssm_fidelity_analysis\\n      metric: baseline.dt2_reward_mae\\n  - row: 0\\n    col: 5\\n    value: 1.56\\n    source:\\n      exp_id: exp_rssm_fidelity_analysis\\n      metric: baseline.reward_gap\\n  - row: 1\\n    col: 0\\n    value: 41.31\\n    source:\\n      exp_id: exp_rssm_fidelity_analysis\\n      metric: 008d_trained_dtEmb.dt1_obs_mse\\n  - row: 1\\n    col: 1\\n    value: 53.67\\n    source:\\n      exp_id: exp_rssm_fidelity_analysis\\n      metric: 008d_trained_dtEmb.dt2_obs_mse\\n  - row: 1\\n    col: 2\\n    value: 1.3\\n    source:\\n      exp_id: exp_rssm_fidelity_analysis\\n      metric: 008d_trained_dtEmb.obs_gap\\n  - row: 1\\n    col: 3\\n    value: 0.0568\\n    source:\\n      exp_id: exp_rssm_fidelity_analysis\\n      metric: 008d_trained_dtEmb.dt1_reward_mae\\n  - row: 1\\n    col: 4\\n    value: 0.1579\\n    source:\\n      exp_id: exp_rssm_fidelity_analysis\\n      metric: 008d_trained_dtEmb.dt2_reward_mae\\n  - row: 1\\n    col: 5\\n    value: 2.78\\n    source:\\n      exp_id: exp_rssm_fidelity_analysis\\n      metric: 008d_trained_dtEmb.reward_gap\\n  - row: 2\\n    col: 0\\n    value: 8.01\\n    source:\\n      exp_id: exp_rssm_fidelity_analysis\\n      metric: 008f_no_dtEmb.dt1_obs_mse\\n  - row: 2\\n    col: 1\\n    value: 22.04\\n    source:\\n      exp_id: exp_rssm_fidelity_analysis\\n      metric: 008f_no_dtEmb.dt2_obs_mse\\n  - row: 2\\n    col: 2\\n    value: 2.75\\n    source:\\n      exp_id: exp_rssm_fidelity_analysis\\n      metric: 008f_no_dtEmb.obs_gap\\n  - row: 2\\n    col: 3\\n    value: 0.7469\\n    source:\\n      exp_id: exp_rssm_fidelity_analysis\\n      metric: 008f_no_dtEmb.dt1_reward_mae\\n  - row: 2\\n    col: 4\\n    value: 0.7526\\n    source:\\n      exp_id: exp_rssm_fidelity_analysis\\n      metric: 008f_no_dtEmb.dt2_reward_mae\\n  - row: 2\\n    col: 5\\n    value: 1.01\\n    source:\\n      exp_id: exp_rssm_fidelity_analysis\\n      metric: 008f_no_dtEmb.reward_gap\\n  deprecated: false\\n- id: T004\\n  location:\\n    section: results\\n    table_number: 3\\n  caption: Post-CIVO outcomes for 008d configuration\\n  cells:\\n  - row: 0\\n    col: 0\\n    value: 4.12\\n    source:\\n      exp_id: exp_008d_subsample_on_h8\\n      metric: peak_nve\\n  - row: 0\\n    col: 1\\n    value: 4.12\\n    source:\\n      exp_id: exp_008d_subsample_on_h8\\n      metric: peak_nve\\n  - row: 0\\n    col: 2\\n    value: 82.8\\n    source:\\n      exp_id: exp_008d_subsample_on_h8\\n      metric: eval_return_55K\\n  - row: 1\\n    col: 0\\n    value: 1.62\\n    source:\\n      exp_id: exp_009b_008d_walker_s2\\n      metric: peak_nve\\n  - row: 1\\n    col: 1\\n    value: 0.38\\n    source:\\n      exp_id: exp_009b_008d_walker_s2\\n      metric: final_nve\\n  - row: 1\\n    col: 2\\n    value: 267.9\\n    source:\\n      exp_id: exp_009b_008d_walker_s2\\n      metric: final_eval_return\\n  - row: 2\\n    col: 0\\n    value: 4.12\\n    source:\\n      exp_id: exp_009e_008d_walker_s1\\n      metric: peak_nve\\n  - row: 2\\n    col: 1\\n    value: 1.57\\n    source:\\n      exp_id: exp_009e_008d_walker_s1\\n      metric: final_nve\\n  - row: 2\\n    col: 2\\n    value: 131.1\\n    source:\\n      exp_id: exp_009e_008d_walker_s1\\n      metric: final_eval_return\\n  deprecated: false\\nfigures:\\n- id: F001\\n  location:\\n    section: results\\n    figure_number: 1\\n  caption: Learning curves for all configurations\\n  type: result\\n  source:\\n    experiments:\\n    - exp_id: exp_001_baseline\\n    - exp_id: exp_006_fixed_dt2\\n    - exp_id: exp_007_fixed_dt4\\n    - exp_id: exp_005_event_gated_v4\\n    - exp_id: exp_008d_subsample_on_h8\\n    - exp_id: exp_008f_no_dt_embed_subsample_on_h8\\n    - exp_id: exp_008a_no_subsample_dt2\\n    - exp_id: exp_008e_v3_walker_s1\\n  output_path: figures/paper/fig1_learning_curves.pdf\\n  deprecated: false\\n- id: F002\\n  location:\\n    section: results\\n    figure_number: 2\\n  caption: Normalized value-to-eval ratio trajectories\\n  type: result\\n  source:\\n    experiments:\\n    - exp_id: exp_008d_subsample_on_h8\\n    - exp_id: exp_008f_no_dt_embed_subsample_on_h8\\n    - exp_id: exp_008a_no_subsample_dt2\\n    - exp_id: exp_008e_v3_walker_s1\\n    - exp_id: exp_009b_008d_walker_s2\\n  output_path: figures/paper/fig2_nve_trajectory.pdf\\n  deprecated: false\\n- id: F003\\n  location:\\n    section: results\\n    figure_number: 3\\n  caption: Factorial experiment summary grid\\n  type: result\\n  source:\\n    experiments:\\n    - exp_id: exp_008d_subsample_on_h8\\n    - exp_id: exp_008f_no_dt_embed_subsample_on_h8\\n    - exp_id: exp_008a_no_subsample_dt2\\n    - exp_id: exp_008c_no_subsample_dt2_h8\\n  output_path: figures/paper/fig3_factorial_grid.pdf\\n  deprecated: false\\n- id: F004\\n  location:\\n    section: results\\n    figure_number: 4\\n  caption: Peak evaluation return as function of imagination dt\\n  type: result\\n  source:\\n    experiments:\\n    - exp_id: exp_001_baseline\\n    - exp_id: exp_006_fixed_dt2\\n    - exp_id: exp_007_fixed_dt4\\n  output_path: figures/paper/fig5_dt_amplification.pdf\\n  deprecated: false\\n- id: F005\\n  location:\\n    section: results\\n    figure_number: 5\\n  caption: 'Contrasting collapse dynamics: CIVO vs non-CIVO'\\n  type: result\\n  source:\\n    experiments:\\n    - exp_id: exp_008d_subsample_on_h8\\n    - exp_id: exp_008e_v3_walker_s2\\n    - exp_id: exp_009a_baseline_walker_s2\\n  output_path: figures/paper/fig6_multiple_pathways.pdf\\n  deprecated: false\\n- id: F006\\n  location:\\n    section: sections/appendix\\n    figure_number: 0\\n  caption: ''\\n  type: other\\n  source: {}\\n  output_path: ''\\n  deprecated: false\\n_completeness:\\n  coverage: 73/77\\n  claims: 71\\n  tables: 4\\n  figures: 6\\n  tier_counts:\\n    tier1: 0\\n    tier2: 73\\n    tier3: 4\\n    tierX: 0\\n  last_checked: '2026-05-25T03:36:26.590002+00:00'\\n\", \"total_chars\": 36692, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "72aab3fa-ba3f-48a9-9029-1cec279461d0",
  "uuid": "1cb49430-fcb6-4499-a065-ed6d888e6fa5",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper_provenance.yaml\\\", \\\"content\\\": \\\"paper:\\\\n  title: 'Why Temporal Abstraction Fails in Imagination-Based RL: A Diagnostic Analysis\\\\n    of Variable-Rate DreamerV3'\\\\n  version: 38\\\\n  generated_at: '2026-05-25T03:36:26.589946+00:00'\\\\n  source: manual build by Paper Agent — schema v3 matching check_provenance_completeness\\\\nclaims:\\\\n- id: C001\\\\n  location:\\\\n    section: abstract\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: every variable-rate configuration of DreamerV3 degrades performance\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_006_fixed_dt2\\\\n    metric: eval_return_65K\\\\n    value: 132.86\\\\n    role: primary_evidence\\\\n  - exp_id: exp_007_fixed_dt4\\\\n    metric: peak_return\\\\n    value: 176.9\\\\n    role: primary_evidence\\\\n  - exp_id: exp_005_event_gated_v4\\\\n    metric: eval_return_145K\\\\n    value: 98.84\\\\n    role: primary_evidence\\\\n  decisions:\\\\n  - D009\\\\n  - D015\\\\n  deprecated: false\\\\n- id: C002\\\\n  location:\\\\n    section: abstract\\\\n    paragraph: 0\\\\n    sentence: 2\\\\n  text: trained temporal embedding as the causal factor\\\\n  type: methodological\\\\n  evidence:\\\\n  - exp_id: exp_008d_subsample_on_h8\\\\n    metric: eval_return_55K\\\\n    value: 82.75\\\\n    role: primary_evidence\\\\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\\\\n    metric: eval_return_105K\\\\n    value: 503.0\\\\n    role: control\\\\n  decisions:\\\\n  - D021\\\\n  deprecated: false\\\\n- id: C003\\\\n  location:\\\\n    section: abstract\\\\n    paragraph: 0\\\\n    sentence: 3\\\\n  text: 2.78x prediction gap between dt=1 and dt=2\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_rssm_fidelity_analysis\\\\n    metric: 008d_trained_dtEmb.reward_gap\\\\n    value: 2.78\\\\n    role: primary_evidence\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C004\\\\n  location:\\\\n    section: abstract\\\\n    paragraph: 0\\\\n    sentence: 4\\\\n  text: 7/8 classification (n=8)\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_008d_subsample_on_h8\\\\n    metric: peak_nve\\\\n    value: 4.12\\\\n    role: true_positive\\\\n  - exp_id: exp_006_fixed_dt2\\\\n    metric: model_loss_at_55k\\\\n    value: 4.853\\\\n    role: true_positive\\\\n  - exp_id: exp_009b_008d_walker_s2\\\\n    metric: peak_nve\\\\n    value: 1.62\\\\n    role: true_positive\\\\n  - exp_id: exp_008e_v3_walker_s2\\\\n    metric: final_nve\\\\n    value: 3.78\\\\n    role: false_positive\\\\n  decisions:\\\\n  - D053\\\\n  deprecated: false\\\\n- id: C005\\\\n  location:\\\\n    section: abstract\\\\n    paragraph: 0\\\\n    sentence: 5\\\\n  text: stochastic downstream outcomes — full collapse, transient CIVO, oscillatory\\\\n    degradation\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_008d_subsample_on_h8\\\\n    metric: eval_return_55K\\\\n    value: 82.75\\\\n    role: full_collapse\\\\n  - exp_id: exp_009b_008d_walker_s2\\\\n    metric: final_eval_return\\\\n    value: 267.93\\\\n    role: transient_civo\\\\n  - exp_id: exp_009e_008d_walker_s1\\\\n    metric: final_eval_return\\\\n    value: 131.08\\\\n    role: oscillatory\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C006\\\\n  location:\\\\n    section: abstract\\\\n    paragraph: 0\\\\n    sentence: 6\\\\n  text: 'restricting imagination to dt=1 does not prevent collapse: one of two seeds\\\\n    fails'\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_008e_v3_walker_s1\\\\n    metric: final_eval_return\\\\n    value: 869.9\\\\n    role: healthy\\\\n  - exp_id: exp_008e_v3_walker_s2\\\\n    metric: final_eval_return\\\\n    value: 136.96\\\\n    role: collapsed\\\\n  - exp_id: exp_009a_baseline_walker_s2\\\\n    metric: final_eval_return\\\\n    value: 836.51\\\\n    role: control\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C007\\\\n  location:\\\\n    section: introduction\\\\n    paragraph: 1\\\\n    sentence: 1\\\\n  text: fixed dt=2 collapses to 14% of baseline\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_006_fixed_dt2\\\\n    metric: eval_return_65K\\\\n    value: 132.86\\\\n    role: primary_evidence\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C008\\\\n  location:\\\\n    section: introduction\\\\n    paragraph: 1\\\\n    sentence: 1\\\\n  text: fixed dt=4 never exceeds 19% of baseline\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_007_fixed_dt4\\\\n    metric: peak_return\\\\n    value: 176.9\\\\n    role: primary_evidence\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C009\\\\n  location:\\\\n    section: introduction\\\\n    paragraph: 1\\\\n    sentence: 1\\\\n  text: learned Gumbel-Softmax gate collapses to 11%\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_005_event_gated_v4\\\\n    metric: eval_return_145K\\\\n    value: 98.84\\\\n    role: primary_evidence\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C010\\\\n  location:\\\\n    section: methodology\\\\n    paragraph: 8\\\\n    sentence: 0\\\\n  text: baseline runs for 500K steps, peak return 970.4\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_001_baseline\\\\n    metric: eval_return_peak\\\\n    value: 970.41\\\\n    role: primary_evidence\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C011\\\\n  location:\\\\n    section: methodology\\\\n    paragraph: 6\\\\n    sentence: 3\\\\n  text: 7/8 accuracy (AUROC=0.933)\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_008d_subsample_on_h8\\\\n    metric: peak_nve\\\\n    value: 4.12\\\\n    role: true_positive\\\\n  - exp_id: exp_009b_008d_walker_s2\\\\n    metric: peak_nve\\\\n    value: 1.62\\\\n    role: true_positive\\\\n  decisions:\\\\n  - D053\\\\n  - D054\\\\n  deprecated: false\\\\n- id: C012\\\\n  location:\\\\n    section: results\\\\n    paragraph: 0\\\\n    sentence: 1\\\\n  text: baseline reaches 915.7 at 105K and peaks at 970.4 at 505K\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_001_baseline\\\\n    metric: eval_return_peak\\\\n    value: 970.41\\\\n    role: primary_evidence\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C013\\\\n  location:\\\\n    section: results\\\\n    paragraph: 0\\\\n    sentence: 2\\\\n  text: fixed dt=2 peaks at 485.3 at 35K before collapsing to 132.9 by 65K\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_006_fixed_dt2\\\\n    metric: peak_return\\\\n    value: 485.3\\\\n    role: primary_evidence\\\\n  - exp_id: exp_006_fixed_dt2\\\\n    metric: eval_return_65K\\\\n    value: 132.86\\\\n    role: primary_evidence\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C014\\\\n  location:\\\\n    section: results\\\\n    paragraph: 0\\\\n    sentence: 3\\\\n  text: fixed dt=4 peaks at 176.9 at 25K\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_007_fixed_dt4\\\\n    metric: peak_return\\\\n    value: 176.9\\\\n    role: primary_evidence\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C015\\\\n  location:\\\\n    section: results\\\\n    paragraph: 0\\\\n    sentence: 4\\\\n  text: learned-gate peaks at 541.2 at 55K collapses to 98.8 by 145K\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_005_event_gated_v4\\\\n    metric: peak_return\\\\n    value: 541.18\\\\n    role: primary_evidence\\\\n  - exp_id: exp_005_event_gated_v4\\\\n    metric: eval_return_145K\\\\n    value: 98.84\\\\n    role: primary_evidence\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C016\\\\n  location:\\\\n    section: results\\\\n    paragraph: 3\\\\n    sentence: 0\\\\n  text: 008d NVE=4.12x at 55K, collapse eval 167→82.8\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_008d_subsample_on_h8\\\\n    metric: eval_return_55K\\\\n    value: 82.75\\\\n    role: primary_evidence\\\\n  - exp_id: exp_008d_subsample_on_h8\\\\n    metric: eval_return_25K\\\\n    value: 167.22\\\\n    role: primary_evidence\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C017\\\\n  location:\\\\n    section: results\\\\n    paragraph: 3\\\\n    sentence: 1\\\\n  text: 008f NVE=0.30x at 105K, no collapse eval 503.0\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\\\\n    metric: eval_return_105K\\\\n    value: 503.0\\\\n    role: primary_evidence\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C018\\\\n  location:\\\\n    section: results\\\\n    paragraph: 4\\\\n    sentence: 0\\\\n  text: AUROC=0.933, Clopper-Pearson 95% CI [0.47, 1.0]\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_008d_subsample_on_h8\\\\n    metric: peak_nve\\\\n    value: 4.12\\\\n    role: true_positive\\\\n  - exp_id: exp_009b_008d_walker_s2\\\\n    metric: peak_nve\\\\n    value: 1.62\\\\n    role: true_positive\\\\n  - exp_id: exp_008e_v3_walker_s2\\\\n    metric: final_nve\\\\n    value: 3.78\\\\n    role: false_positive\\\\n  decisions:\\\\n  - D054\\\\n  deprecated: false\\\\n- id: C019\\\\n  location:\\\\n    section: results\\\\n    paragraph: 4\\\\n    sentence: 1\\\\n  text: gap between lowest TP (1.62x) and highest TN (1.00x) is 0.62\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_009b_008d_walker_s2\\\\n    metric: peak_nve\\\\n    value: 1.62\\\\n    role: true_positive\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C020\\\\n  location:\\\\n    section: results\\\\n    paragraph: 6\\\\n    sentence: 0\\\\n  text: 'Seed 0 (008d) full collapse: eval 167→82.8, value +130%'\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_008d_subsample_on_h8\\\\n    metric: eval_return_55K\\\\n    value: 82.75\\\\n    role: primary_evidence\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C021\\\\n  location:\\\\n    section: results\\\\n    paragraph: 7\\\\n    sentence: 0\\\\n  text: 'Seed 2 (009b) transient CIVO: NVE 1.62x at 45K, self-corrects to 0.38x, eval\\\\n    267.9'\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_009b_008d_walker_s2\\\\n    metric: final_eval_return\\\\n    value: 267.93\\\\n    role: primary_evidence\\\\n  - exp_id: exp_009b_008d_walker_s2\\\\n    metric: final_nve\\\\n    value: 0.38\\\\n    role: primary_evidence\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C022\\\\n  location:\\\\n    section: results\\\\n    paragraph: 8\\\\n    sentence: 0\\\\n  text: 'Seed 1 (009e) oscillatory: eval 82.7-250, settles 131.1, peak NVE=4.12x,\\\\n    final 1.57x'\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_009e_008d_walker_s1\\\\n    metric: final_eval_return\\\\n    value: 131.08\\\\n    role: primary_evidence\\\\n  - exp_id: exp_009e_008d_walker_s1\\\\n    metric: final_nve\\\\n    value: 1.57\\\\n    role: primary_evidence\\\\n  - exp_id: exp_009e_008d_walker_s1\\\\n    metric: peak_nve\\\\n    value: 4.12\\\\n    role: primary_evidence\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C023\\\\n  location:\\\\n    section: results\\\\n    paragraph: 10\\\\n    sentence: 0\\\\n  text: 008a reaches 777.7 (NVE=0.59x)\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_008a_no_subsample_dt2\\\\n    metric: eval_return_105K\\\\n    value: 777.66\\\\n    role: primary_evidence\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C024\\\\n  location:\\\\n    section: results\\\\n    paragraph: 10\\\\n    sentence: 0\\\\n  text: 008c reaches 240.9 (NVE=0.58x)\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_008c_no_subsample_dt2_h8\\\\n    metric: eval_return_65K\\\\n    value: 240.86\\\\n    role: primary_evidence\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C025\\\\n  location:\\\\n    section: results\\\\n    paragraph: 12\\\\n    sentence: 0\\\\n  text: dt=1 (915.7) > dt=2 (485.3, -47%) > dt=4 (176.9, -81%)\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_006_fixed_dt2\\\\n    metric: peak_return\\\\n    value: 485.3\\\\n    role: primary_evidence\\\\n  - exp_id: exp_007_fixed_dt4\\\\n    metric: peak_return\\\\n    value: 176.9\\\\n    role: primary_evidence\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C026\\\\n  location:\\\\n    section: results\\\\n    paragraph: 14\\\\n    sentence: 0\\\\n  text: 008d collapses NVE=4.12x vs untrained configs NVE<0.6x\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_008d_subsample_on_h8\\\\n    metric: eval_return_55K\\\\n    value: 82.75\\\\n    role: primary_evidence\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C027\\\\n  location:\\\\n    section: results\\\\n    paragraph: 14\\\\n    sentence: 1\\\\n  text: 'cross-seed variance: 008f 503.0 vs 009c 148.3'\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\\\\n    metric: eval_return_105K\\\\n    value: 503.0\\\\n    role: primary_evidence\\\\n  - exp_id: exp_009c_008f_walker_s2\\\\n    metric: final_eval_return\\\\n    value: 148.34\\\\n    role: primary_evidence\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C028\\\\n  location:\\\\n    section: results\\\\n    paragraph: 16\\\\n    sentence: 0\\\\n  text: '008e_v3 s1 healthy: eval 869.9 (95% of baseline), NVE=0.80x'\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_008e_v3_walker_s1\\\\n    metric: final_eval_return\\\\n    value: 869.9\\\\n    role: primary_evidence\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C029\\\\n  location:\\\\n    section: results\\\\n    paragraph: 16\\\\n    sentence: 1\\\\n  text: '008e_v3 s2 collapsed: eval 715→137, NVE=3.78x'\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_008e_v3_walker_s2\\\\n    metric: final_eval_return\\\\n    value: 136.96\\\\n    role: primary_evidence\\\\n  - exp_id: exp_008e_v3_walker_s2\\\\n    metric: peak_eval_return\\\\n    value: 715.21\\\\n    role: primary_evidence\\\\n  - exp_id: exp_008e_v3_walker_s2\\\\n    metric: final_nve\\\\n    value: 3.78\\\\n    role: primary_evidence\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C030\\\\n  location:\\\\n    section: results\\\\n    paragraph: 17\\\\n    sentence: 0\\\\n  text: baseline seed 2 (009a) stable at 836.5\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_009a_baseline_walker_s2\\\\n    metric: final_eval_return\\\\n    value: 836.51\\\\n    role: control\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C031\\\\n  location:\\\\n    section: results\\\\n    paragraph: 18\\\\n    sentence: 1\\\\n  text: '008e_v3_s2 Pathway B: entropy increases (-5.21→-3.83)'\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_008e_v3_walker_s2\\\\n    metric: final_eval_return\\\\n    value: 136.96\\\\n    role: primary_evidence\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C032\\\\n  location:\\\\n    section: results\\\\n    paragraph: 19\\\\n    sentence: 0\\\\n  text: 008e_v3_s2 NVE=3.78x false positive (non-CIVO)\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_008e_v3_walker_s2\\\\n    metric: final_nve\\\\n    value: 3.78\\\\n    role: false_positive\\\\n  decisions:\\\\n  - D053\\\\n  deprecated: false\\\\n- id: C033\\\\n  location:\\\\n    section: results\\\\n    paragraph: 21\\\\n    sentence: 0\\\\n  text: 008d reward gap 2.78x (dt1 MAE=0.0568, dt2 MAE=0.1579)\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_rssm_fidelity_analysis\\\\n    metric: 008d_trained_dtEmb.reward_gap\\\\n    value: 2.78\\\\n    role: primary_evidence\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C034\\\\n  location:\\\\n    section: results\\\\n    paragraph: 21\\\\n    sentence: 1\\\\n  text: 008f reward gap 1.01x (MAE 0.7469)\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_rssm_fidelity_analysis\\\\n    metric: 008f_no_dtEmb.reward_gap\\\\n    value: 1.01\\\\n    role: primary_evidence\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C035\\\\n  location:\\\\n    section: results\\\\n    paragraph: 21\\\\n    sentence: 1\\\\n  text: 008f absolute MAE 0.7469 vs 008d 0.0568 at dt=1\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_rssm_fidelity_analysis\\\\n    metric: 008f_no_dtEmb.dt1_reward_mae\\\\n    value: 0.7469\\\\n    role: primary_evidence\\\\n  - exp_id: exp_rssm_fidelity_analysis\\\\n    metric: 008d_trained_dtEmb.dt1_reward_mae\\\\n    value: 0.0568\\\\n    role: primary_evidence\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C036\\\\n  location:\\\\n    section: analysis\\\\n    paragraph: 2\\\\n    sentence: 0\\\\n  text: 'two-stage amplification: Stage 1 dynamics bias 1.68x, Stage 2 actor exploitation\\\\n    2.90x'\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_008d_subsample_on_h8\\\\n    metric: random_policy_reward_ratio\\\\n    value: 1.68\\\\n    role: stage1\\\\n  - exp_id: exp_008d_subsample_on_h8\\\\n    metric: trained_actor_reward_ratio\\\\n    value: 2.9\\\\n    role: stage2\\\\n  decisions:\\\\n  - D042\\\\n  deprecated: false\\\\n- id: C037\\\\n  location:\\\\n    section: analysis\\\\n    paragraph: 2\\\\n    sentence: 1\\\\n  text: ~36% dynamics bias, ~64% actor exploitation\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_008d_subsample_on_h8\\\\n    metric: dynamics_bias_fraction\\\\n    value: 0.36\\\\n    role: primary_evidence\\\\n  decisions:\\\\n  - D042\\\\n  deprecated: false\\\\n- id: C038\\\\n  location:\\\\n    section: analysis\\\\n    paragraph: 2\\\\n    sentence: 2\\\\n  text: '008f control: random 1.11x, trained 0.98x — no effect'\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\\\\n    metric: random_policy_reward_ratio\\\\n    value: 1.11\\\\n    role: control\\\\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\\\\n    metric: trained_actor_reward_ratio\\\\n    value: 0.98\\\\n    role: control\\\\n  decisions:\\\\n  - D042\\\\n  deprecated: false\\\\n- id: C039\\\\n  location:\\\\n    section: analysis\\\\n    paragraph: 4\\\\n    sentence: 0\\\\n  text: all runs cross NVE>1.5x — CIVO triggers deterministically\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_008d_subsample_on_h8\\\\n    metric: peak_nve\\\\n    value: 4.12\\\\n    role: primary_evidence\\\\n  - exp_id: exp_009b_008d_walker_s2\\\\n    metric: peak_nve\\\\n    value: 1.62\\\\n    role: primary_evidence\\\\n  - exp_id: exp_009e_008d_walker_s1\\\\n    metric: peak_nve\\\\n    value: 4.12\\\\n    role: primary_evidence\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C040\\\\n  location:\\\\n    section: analysis\\\\n    paragraph: 7\\\\n    sentence: 0\\\\n  text: 'removing dt_emb: 13x cost to reward prediction (0.7469 vs 0.0568)'\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_rssm_fidelity_analysis\\\\n    metric: 008f_no_dtEmb.dt1_reward_mae\\\\n    value: 0.7469\\\\n    role: primary_evidence\\\\n  - exp_id: exp_rssm_fidelity_analysis\\\\n    metric: 008d_trained_dtEmb.dt1_reward_mae\\\\n    value: 0.0568\\\\n    role: primary_evidence\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C041\\\\n  location:\\\\n    section: analysis\\\\n    paragraph: 8\\\\n    sentence: 1\\\\n  text: 'Pathway B FP: 008e_v3_s2 NVE=3.78x non-CIVO'\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_008e_v3_walker_s2\\\\n    metric: final_nve\\\\n    value: 3.78\\\\n    role: false_positive\\\\n  decisions:\\\\n  - D053\\\\n  deprecated: false\\\\n- id: C042\\\\n  location:\\\\n    section: conclusion\\\\n    paragraph: 0\\\\n    sentence: 2\\\\n  text: 7/8 CIVO classification (n=8, 87.5%)\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_008d_subsample_on_h8\\\\n    metric: peak_nve\\\\n    value: 4.12\\\\n    role: true_positive\\\\n  - exp_id: exp_009b_008d_walker_s2\\\\n    metric: peak_nve\\\\n    value: 1.62\\\\n    role: true_positive\\\\n  decisions:\\\\n  - D053\\\\n  deprecated: false\\\\n- id: C043\\\\n  location:\\\\n    section: conclusion\\\\n    paragraph: 2\\\\n    sentence: 1\\\\n  text: NVE margin 0.62 excluding outlier\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_009b_008d_walker_s2\\\\n    metric: peak_nve\\\\n    value: 1.62\\\\n    role: lowest_true_positive\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C044\\\\n  location:\\\\n    section: sections/appendix\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Extended NVE validation (n=32) achieves F1=0.880 at 1.5x threshold\\\\n  type: quantitative\\\\n  evidence: []\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C045\\\\n  location:\\\\n    section: sections/analysis\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: NVE diagnostic extended validation n=32 AUROC=0.961 F1=0.880\\\\n  type: quantitative\\\\n  evidence: []\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C046\\\\n  location:\\\\n    section: sections/analysis\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 'Entropy explosion is lagging indicator: +2.1 nats/10K collapsed vs +0.07-0.22\\\\n    healthy, return collapses ~35K steps before entropy rises'\\\\n  type: quantitative\\\\n  evidence: []\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C047\\\\n  location:\\\\n    section: sections/methodology\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: NVE threshold 29/32 accuracy (AUROC=0.961, F1=0.880) at n=32\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: plan_034_nve_threshold\\\\n    metric: auroc_n32\\\\n    value: 0.961\\\\n    role: primary_evidence\\\\n  - exp_id: plan_034_nve_threshold\\\\n    metric: f1_at_1.5x\\\\n    value: 0.88\\\\n    role: primary_evidence\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C048\\\\n  location:\\\\n    section: sections/results\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: NVE threshold 29/32 classification (n=32, AUROC=0.961, F1=0.880)\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: plan_034_nve_threshold\\\\n    metric: auroc_n32\\\\n    value: 0.961\\\\n    role: primary_evidence\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C049\\\\n  location:\\\\n    section: sections/abstract_body\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: CIVO classification 29/32 AUROC=0.961 F1=0.880\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: plan_034_nve_threshold\\\\n    metric: auroc_n32\\\\n    value: 0.961\\\\n    role: primary_evidence\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C050\\\\n  location:\\\\n    section: sections/introduction\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: NVE threshold 29/32 classification in introduction\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: plan_034_nve_threshold\\\\n    metric: auroc_n32\\\\n    value: 0.961\\\\n    role: primary_evidence\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C051\\\\n  location:\\\\n    section: sections/introduction\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Contribution 1 AUROC updated to 0.961\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: plan_034_nve_threshold\\\\n    metric: auroc_n32\\\\n    value: 0.961\\\\n    role: primary_evidence\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C052\\\\n  location:\\\\n    section: sections/conclusion\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Conclusion NVE updated to 29/32 AUROC=0.961\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: plan_034_nve_threshold\\\\n    metric: auroc_n32\\\\n    value: 0.961\\\\n    role: primary_evidence\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C053\\\\n  location:\\\\n    section: sections/analysis\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Discussion NVE diagnostic consolidated to n=32 AUROC=0.961\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: plan_034_nve_threshold\\\\n    metric: auroc_n32\\\\n    value: 0.961\\\\n    role: primary_evidence\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C054\\\\n  location:\\\\n    section: sections/results\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: RSSM reward prediction gap 2.78x corroborated at 3.11x with 600-sample validation\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_rssm_fidelity_analysis\\\\n    metric: 008d_trained_dtEmb.reward_gap\\\\n    value: 2.78\\\\n    role: primary_evidence\\\\n  - exp_id: exp_063_rssm_fidelity\\\\n    metric: collapsed_reward_gap\\\\n    value: 3.11\\\\n    role: corroboration\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C055\\\\n  location:\\\\n    section: sections/results\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: CIVO model median V(s)/MC-return ratio 3.40 vs no-dt-emb control 1.05\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_064_value_distribution\\\\n    metric: civo_median_v_mc_ratio\\\\n    value: 3.4\\\\n    role: primary_evidence\\\\n  - exp_id: exp_064_value_distribution\\\\n    metric: control_median_v_mc_ratio\\\\n    value: 1.05\\\\n    role: control\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C056\\\\n  location:\\\\n    section: sections/results\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 'Return collapses ~35K steps before entropy rises: +2.1 nats/10K collapsed\\\\n    vs +0.07-0.22 healthy'\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: plan_031_actor_entropy\\\\n    metric: collapsed_entropy_rate\\\\n    value: 2.1\\\\n    role: primary_evidence\\\\n  - exp_id: plan_031_actor_entropy\\\\n    metric: healthy_entropy_rate_range\\\\n    value: 0.07-0.22\\\\n    role: control\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C057\\\\n  location:\\\\n    section: sections/analysis\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: RSSM reward gap 2.78-3.11x range across two independent analyses\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_rssm_fidelity_analysis\\\\n    metric: 008d_trained_dtEmb.reward_gap\\\\n    value: 2.78\\\\n    role: primary_evidence\\\\n  - exp_id: exp_063_rssm_fidelity\\\\n    metric: collapsed_reward_gap\\\\n    value: 3.11\\\\n    role: corroboration\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C058\\\\n  location:\\\\n    section: sections/analysis\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 'Obs-decoder SGS compensatory amplification: NVE from 8.3x to 21.9-30.2x on\\\\n    Cheetah'\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_026_obs_sgs_cheetah\\\\n    metric: nve_amplification\\\\n    value: 21.9-30.2\\\\n    role: primary_evidence\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C059\\\\n  location:\\\\n    section: sections/analysis\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 'TCN impossible dose: sigma=1.0 Cheetah suppresses CIVO (NVE<=0.3x) but eval→15%\\\\n    baseline'\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_030c_tcn_cheetah\\\\n    metric: nve_suppressed\\\\n    value: 0.3\\\\n    role: primary_evidence\\\\n  - exp_id: exp_030c_tcn_cheetah\\\\n    metric: eval_pct_baseline\\\\n    value: 15\\\\n    role: primary_evidence\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C060\\\\n  location:\\\\n    section: sections/appendix\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 'Trained dt_emb cosine similarity: cos(dt1,dt2) = -0.87 to -0.94 at 25K, -0.70\\\\n    to -0.86 at 75K'\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_065_dt_emb_cosine\\\\n    metric: trained_cos_25k_range\\\\n    value: -0.87 to -0.94\\\\n    role: primary_evidence\\\\n  - exp_id: exp_065_dt_emb_cosine\\\\n    metric: trained_cos_75k_range\\\\n    value: -0.70 to -0.86\\\\n    role: primary_evidence\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C061\\\\n  location:\\\\n    section: sections/appendix\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 'Frozen dt_emb cosine similarity: near-zero (-0.15 to +0.07), constant'\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_065_dt_emb_cosine\\\\n    metric: frozen_cos_constant\\\\n    value: -0.15 to +0.07\\\\n    role: control\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C062\\\\n  location:\\\\n    section: sections/introduction\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: RSSM reward prediction gap 2.78-3.11x in introduction\\\\n  type: quantitative\\\\n  evidence:\\\\n  - exp_id: exp_rssm_fidelity_analysis\\\\n    metric: 008d_trained_dtEmb.reward_gap\\\\n    value: 2.78\\\\n    role: primary_evidence\\\\n  - exp_id: exp_063_rssm_fidelity\\\\n    metric: collapsed_reward_gap\\\\n    value: 3.11\\\\n    role: corroboration\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C063\\\\n  location:\\\\n    section: sections/results\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: RSSM reward MAE increases from 0.057 to 0.178 (3.11x gap) at dt=2 under trained\\\\n    conditioning\\\\n  type: quantitative\\\\n  evidence: exp_063 rssm_fidelity_analysis, 600-sample validation\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C064\\\\n  location:\\\\n    section: sections/results\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: Observation reconstruction gap improves with temporal conditioning (1.33x\\\\n    vs baseline 1.46x)\\\\n  type: quantitative\\\\n  evidence: exp_063 obs_mse data\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C065\\\\n  location:\\\\n    section: sections/results\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: CIVO model mean V/MC ratio = 7.80x (median 3.40x, 100% overestimated) vs control\\\\n    median 1.05x (52.5% overestimated)\\\\n  type: quantitative\\\\n  evidence: exp_064 value_distribution results_summary\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C066\\\\n  location:\\\\n    section: sections/analysis\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: RSSM reward MAE 0.057→0.178 at dt=2; obs gap 1.33x vs baseline 1.46x — reward-specific\\\\n    pathology\\\\n  type: quantitative\\\\n  evidence: exp_063 rssm_fidelity_analysis\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C067\\\\n  location:\\\\n    section: sections/results\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: SS fidelity ratio crosses 1.1x at 20K steps, VE ratio first exceeds 1.5x at\\\\n    40K steps — ~10-15K step lag (r=0.81, p=0.002, n=1)\\\\n  type: quantitative\\\\n  evidence: exp_066 timeseries analysis, 12 dense checkpoints\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C068\\\\n  location:\\\\n    section: sections/results\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: dt=1 MAE decreases 0.093→0.047 while dt=2 MAE plateaus ~0.08 — gap from differential\\\\n    improvement\\\\n  type: quantitative\\\\n  evidence: exp_066 timeseries analysis\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C069\\\\n  location:\\\\n    section: sections/analysis\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 'Three-stage causal chain: fidelity gap (20K) → value overestimation (40K)\\\\n    → entropy destabilization (~35K later), n=1'\\\\n  type: quantitative\\\\n  evidence: exp_066 timeseries + actor entropy analysis\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C070\\\\n  location:\\\\n    section: sections/appendix\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: 'exp_066 timeseries: SS fidelity ratio grows 1.05→1.68 over 10K-65K steps;\\\\n    VE ratio near zero until 40K spike (1.59x)'\\\\n  type: quantitative\\\\n  evidence: exp_066 12-checkpoint timeseries analysis\\\\n  decisions: []\\\\n  deprecated: false\\\\n- id: C071\\\\n  location:\\\\n    section: sections/appendix\\\\n    paragraph: 0\\\\n    sentence: 0\\\\n  text: dt=1 MAE 0.090→0.047 (monotonic decrease), dt=2 MAE plateaus ~0.08; gap from\\\\n    selective improvement not worsening\\\\n  type: quantitative\\\\n  evidence: exp_066 timeseries MAE data\\\\n  decisions: []\\\\n  deprecated: false\\\\ntables:\\\\n- id: T001\\\\n  location:\\\\n    section: methodology\\\\n    table_number: 1\\\\n  caption: Factorial design — 9 configurations\\\\n  cells:\\\\n  - row: 0\\\\n    col: 0\\\\n    value: '001'\\\\n    source:\\\\n      exp_id: exp_001_baseline\\\\n      metric: exp_id\\\\n  - row: 1\\\\n    col: 0\\\\n    value: '006'\\\\n    source:\\\\n      exp_id: exp_006_fixed_dt2\\\\n      metric: exp_id\\\\n  - row: 2\\\\n    col: 0\\\\n    value: '007'\\\\n    source:\\\\n      exp_id: exp_007_fixed_dt4\\\\n      metric: exp_id\\\\n  - row: 3\\\\n    col: 0\\\\n    value: '005'\\\\n    source:\\\\n      exp_id: exp_005_event_gated_v4\\\\n      metric: exp_id\\\\n  - row: 4\\\\n    col: 0\\\\n    value: 008d\\\\n    source:\\\\n      exp_id: exp_008d_subsample_on_h8\\\\n      metric: exp_id\\\\n  - row: 5\\\\n    col: 0\\\\n    value: 008f\\\\n    source:\\\\n      exp_id: exp_008f_no_dt_embed_subsample_on_h8\\\\n      metric: exp_id\\\\n  - row: 6\\\\n    col: 0\\\\n    value: 008a\\\\n    source:\\\\n      exp_id: exp_008a_no_subsample_dt2\\\\n      metric: exp_id\\\\n  - row: 7\\\\n    col: 0\\\\n    value: 008c\\\\n    source:\\\\n      exp_id: exp_008c_no_subsample_dt2_h8\\\\n      metric: exp_id\\\\n  - row: 8\\\\n    col: 0\\\\n    value: 008e_v3\\\\n    source:\\\\n      exp_id: exp_008e_v3_subsample_on_dt1_h15\\\\n      metric: exp_id\\\\n  deprecated: false\\\\n- id: T002\\\\n  location:\\\\n    section: results\\\\n    table_number: 1\\\\n  caption: All configurations and outcomes\\\\n  cells:\\\\n  - row: 0\\\\n    col: 5\\\\n    value: 915.7\\\\n    source:\\\\n      exp_id: exp_001_baseline\\\\n      metric: eval_return_105K\\\\n  - row: 1\\\\n    col: 5\\\\n    value: 132.9\\\\n    source:\\\\n      exp_id: exp_006_fixed_dt2\\\\n      metric: eval_return_65K\\\\n  - row: 1\\\\n    col: 6\\\\n    value: 4.83\\\\n    source:\\\\n      exp_id: exp_006_fixed_dt2\\\\n      metric: peak_nve\\\\n  - row: 2\\\\n    col: 5\\\\n    value: 152.5\\\\n    source:\\\\n      exp_id: exp_007_fixed_dt4\\\\n      metric: eval_return_55K\\\\n  - row: 3\\\\n    col: 5\\\\n    value: 98.8\\\\n    source:\\\\n      exp_id: exp_005_event_gated_v4\\\\n      metric: eval_return_145K\\\\n  - row: 4\\\\n    col: 5\\\\n    value: 82.8\\\\n    source:\\\\n      exp_id: exp_008d_subsample_on_h8\\\\n      metric: eval_return_55K\\\\n  - row: 4\\\\n    col: 6\\\\n    value: 4.12\\\\n    source:\\\\n      exp_id: exp_008d_subsample_on_h8\\\\n      metric: peak_nve\\\\n  - row: 5\\\\n    col: 5\\\\n    value: 267.9\\\\n    source:\\\\n      exp_id: exp_009b_008d_walker_s2\\\\n      metric: final_eval_return\\\\n  - row: 5\\\\n    col: 6\\\\n    value: 1.62\\\\n    source:\\\\n      exp_id: exp_009b_008d_walker_s2\\\\n      metric: peak_nve\\\\n  - row: 6\\\\n    col: 5\\\\n    value: 131.1\\\\n    source:\\\\n      exp_id: exp_009e_008d_walker_s1\\\\n      metric: final_eval_return\\\\n  - row: 6\\\\n    col: 6\\\\n    value: 4.12\\\\n    source:\\\\n      exp_id: exp_009e_008d_walker_s1\\\\n      metric: peak_nve\\\\n  - row: 7\\\\n    col: 5\\\\n    value: 503.0\\\\n    source:\\\\n      exp_id: exp_008f_no_dt_embed_subsample_on_h8\\\\n      metric: eval_return_105K\\\\n  - row: 8\\\\n    col: 5\\\\n    value: 148.3\\\\n    source:\\\\n      exp_id: exp_009c_008f_walker_s2\\\\n      metric: final_eval_return\\\\n  - row: 9\\\\n    col: 5\\\\n    value: 777.7\\\\n    source:\\\\n      exp_id: exp_008a_no_subsample_dt2\\\\n      metric: eval_return_105K\\\\n  - row: 10\\\\n    col: 5\\\\n    value: 240.9\\\\n    source:\\\\n      exp_id: exp_008c_no_subsample_dt2_h8\\\\n      metric: eval_return_65K\\\\n  - row: 11\\\\n    col: 5\\\\n    value: 869.9\\\\n    source:\\\\n      exp_id: exp_008e_v3_walker_s1\\\\n      metric: final_eval_return\\\\n  - row: 12\\\\n    col: 5\\\\n    value: 137.0\\\\n    source:\\\\n      exp_id: exp_008e_v3_walker_s2\\\\n      metric: final_eval_return\\\\n  - row: 12\\\\n    col: 6\\\\n    value: 3.78\\\\n    source:\\\\n      exp_id: exp_008e_v3_walker_s2\\\\n      metric: final_nve\\\\n  - row: 13\\\\n    col: 5\\\\n    value: 836.5\\\\n    source:\\\\n      exp_id: exp_009a_baseline_walker_s2\\\\n      metric: final_eval_return\\\\n  deprecated: false\\\\n- id: T003\\\\n  location:\\\\n    section: results\\\\n    table_number: 2\\\\n  caption: RSSM fidelity at dt=1 vs dt=2\\\\n  cells:\\\\n  - row: 0\\\\n    col: 0\\\\n    value: 13.49\\\\n    source:\\\\n      exp_id: exp_rssm_fidelity_analysis\\\\n      metric: baseline.dt1_obs_mse\\\\n  - row: 0\\\\n    col: 1\\\\n    value: 27.5\\\\n    source:\\\\n      exp_id: exp_rssm_fidelity_analysis\\\\n      metric: baseline.dt2_obs_mse\\\\n  - row: 0\\\\n    col: 2\\\\n    value: 2.04\\\\n    source:\\\\n      exp_id: exp_rssm_fidelity_analysis\\\\n      metric: baseline.obs_gap\\\\n  - row: 0\\\\n    col: 3\\\\n    value: 0.0102\\\\n    source:\\\\n      exp_id: exp_rssm_fidelity_analysis\\\\n      metric: baseline.dt1_reward_mae\\\\n  - row: 0\\\\n    col: 4\\\\n    value: 0.0159\\\\n    source:\\\\n      exp_id: exp_rssm_fidelity_analysis\\\\n      metric: baseline.dt2_reward_mae\\\\n  - row: 0\\\\n    col: 5\\\\n    value: 1.56\\\\n    source:\\\\n      exp_id: exp_rssm_fidelity_analysis\\\\n      metric: baseline.reward_gap\\\\n  - row: 1\\\\n    col: 0\\\\n    value: 41.31\\\\n    source:\\\\n      exp_id: exp_rssm_fidelity_analysis\\\\n      metric: 008d_trained_dtEmb.dt1_obs_mse\\\\n  - row: 1\\\\n    col: 1\\\\n    value: 53.67\\\\n    source:\\\\n      exp_id: exp_rssm_fidelity_analysis\\\\n      metric: 008d_trained_dtEmb.dt2_obs_mse\\\\n  - row: 1\\\\n    col: 2\\\\n    value: 1.3\\\\n    source:\\\\n      exp_id: exp_rssm_fidelity_analysis\\\\n      metric: 008d_trained_dtEmb.obs_gap\\\\n  - row: 1\\\\n    col: 3\\\\n    value: 0.0568\\\\n    source:\\\\n      exp_id: exp_rssm_fidelity_analysis\\\\n      metric: 008d_trained_dtEmb.dt1_reward_mae\\\\n  - row: 1\\\\n    col: 4\\\\n    value: 0.1579\\\\n    source:\\\\n      exp_id: exp_rssm_fidelity_analysis\\\\n      metric: 008d_trained_dtEmb.dt2_reward_mae\\\\n  - row: 1\\\\n    col: 5\\\\n    value: 2.78\\\\n    source:\\\\n      exp_id: exp_rssm_fidelity_analysis\\\\n      metric: 008d_trained_dtEmb.reward_gap\\\\n  - row: 2\\\\n    col: 0\\\\n    value: 8.01\\\\n    source:\\\\n      exp_id: exp_rssm_fidelity_analysis\\\\n      metric: 008f_no_dtEmb.dt1_obs_mse\\\\n  - row: 2\\\\n    col: 1\\\\n    value: 22.04\\\\n    source:\\\\n      exp_id: exp_rssm_fidelity_analysis\\\\n      metric: 008f_no_dtEmb.dt2_obs_mse\\\\n  - row: 2\\\\n    col: 2\\\\n    value: 2.75\\\\n    source:\\\\n      exp_id: exp_rssm_fidelity_analysis\\\\n      metric: 008f_no_dtEmb.obs_gap\\\\n  - row: 2\\\\n    col: 3\\\\n    value: 0.7469\\\\n    source:\\\\n      exp_id: exp_rssm_fidelity_analysis\\\\n      metric: 008f_no_dtEmb.dt1_reward_mae\\\\n  - row: 2\\\\n    col: 4\\\\n    value: 0.7526\\\\n    source:\\\\n      exp_id: exp_rssm_fidelity_analysis\\\\n      metric: 008f_no_dtEmb.dt2_reward_mae\\\\n  - row: 2\\\\n    col: 5\\\\n    value: 1.01\\\\n    source:\\\\n      exp_id: exp_rssm_fidelity_analysis\\\\n      metric: 008f_no_dtEmb.reward_gap\\\\n  deprecated: false\\\\n- id: T004\\\\n  location:\\\\n    section: results\\\\n    table_number: 3\\\\n  caption: Post-CIVO outcomes for 008d configuration\\\\n  cells:\\\\n  - row: 0\\\\n    col: 0\\\\n    value: 4.12\\\\n    source:\\\\n      exp_id: exp_008d_subsample_on_h8\\\\n      metric: peak_nve\\\\n  - row: 0\\\\n    col: 1\\\\n    value: 4.12\\\\n    source:\\\\n      exp_id: exp_008d_subsample_on_h8\\\\n      metric: peak_nve\\\\n  - row: 0\\\\n    col: 2\\\\n    value: 82.8\\\\n    source:\\\\n      exp_id: exp_008d_subsample_on_h8\\\\n      metric: eval_return_55K\\\\n  - row: 1\\\\n    col: 0\\\\n    value: 1.62\\\\n    source:\\\\n      exp_id: exp_009b_008d_walker_s2\\\\n      metric: peak_nve\\\\n  - row: 1\\\\n    col: 1\\\\n    value: 0.38\\\\n    source:\\\\n      exp_id: exp_009b_008d_walker_s2\\\\n      metric: final_nve\\\\n  - row: 1\\\\n    col: 2\\\\n    value: 267.9\\\\n    source:\\\\n      exp_id: exp_009b_008d_walker_s2\\\\n      metric: final_eval_return\\\\n  - row: 2\\\\n    col: 0\\\\n    value: 4.12\\\\n    source:\\\\n      exp_id: exp_009e_008d_walker_s1\\\\n      metric: peak_nve\\\\n  - row: 2\\\\n    col: 1\\\\n    value: 1.57\\\\n    source:\\\\n      exp_id: exp_009e_008d_walker_s1\\\\n      metric: final_nve\\\\n  - row: 2\\\\n    col: 2\\\\n    value: 131.1\\\\n    source:\\\\n      exp_id: exp_009e_008d_walker_s1\\\\n      metric: final_eval_return\\\\n  deprecated: false\\\\nfigures:\\\\n- id: F001\\\\n  location:\\\\n    section: results\\\\n    figure_number: 1\\\\n  caption: Learning curves for all configurations\\\\n  type: result\\\\n  source:\\\\n    experiments:\\\\n    - exp_id: exp_001_baseline\\\\n    - exp_id: exp_006_fixed_dt2\\\\n    - exp_id: exp_007_fixed_dt4\\\\n    - exp_id: exp_005_event_gated_v4\\\\n    - exp_id: exp_008d_subsample_on_h8\\\\n    - exp_id: exp_008f_no_dt_embed_subsample_on_h8\\\\n    - exp_id: exp_008a_no_subsample_dt2\\\\n    - exp_id: exp_008e_v3_walker_s1\\\\n  output_path: figures/paper/fig1_learning_curves.pdf\\\\n  deprecated: false\\\\n- id: F002\\\\n  location:\\\\n    section: results\\\\n    figure_number: 2\\\\n  caption: Normalized value-to-eval ratio trajectories\\\\n  type: result\\\\n  source:\\\\n    experiments:\\\\n    - exp_id: exp_008d_subsample_on_h8\\\\n    - exp_id: exp_008f_no_dt_embed_subsample_on_h8\\\\n    - exp_id: exp_008a_no_subsample_dt2\\\\n    - exp_id: exp_008e_v3_walker_s1\\\\n    - exp_id: exp_009b_008d_walker_s2\\\\n  output_path: figures/paper/fig2_nve_trajectory.pdf\\\\n  deprecated: false\\\\n- id: F003\\\\n  location:\\\\n    section: results\\\\n    figure_number: 3\\\\n  caption: Factorial experiment summary grid\\\\n  type: result\\\\n  source:\\\\n    experiments:\\\\n    - exp_id: exp_008d_subsample_on_h8\\\\n    - exp_id: exp_008f_no_dt_embed_subsample_on_h8\\\\n    - exp_id: exp_008a_no_subsample_dt2\\\\n    - exp_id: exp_008c_no_subsample_dt2_h8\\\\n  output_path: figures/paper/fig3_factorial_grid.pdf\\\\n  deprecated: false\\\\n- id: F004\\\\n  location:\\\\n    section: results\\\\n    figure_number: 4\\\\n  caption: Peak evaluation return as function of imagination dt\\\\n  type: result\\\\n  source:\\\\n    experiments:\\\\n    - exp_id: exp_001_baseline\\\\n    - exp_id: exp_006_fixed_dt2\\\\n    - exp_id: exp_007_fixed_dt4\\\\n  output_path: figures/paper/fig5_dt_amplification.pdf\\\\n  deprecated: false\\\\n- id: F005\\\\n  location:\\\\n    section: results\\\\n    figure_number: 5\\\\n  caption: 'Contrasting collapse dynamics: CIVO vs non-CIVO'\\\\n  type: result\\\\n  source:\\\\n    experiments:\\\\n    - exp_id: exp_008d_subsample_on_h8\\\\n    - exp_id: exp_008e_v3_walker_s2\\\\n    - exp_id: exp_009a_baseline_walker_s2\\\\n  output_path: figures/paper/fig6_multiple_pathways.pdf\\\\n  deprecated: false\\\\n- id: F006\\\\n  location:\\\\n    section: sections/appendix\\\\n    figure_number: 0\\\\n  caption: ''\\\\n  type: other\\\\n  source: {}\\\\n  output_path: ''\\\\n  deprecated: false\\\\n_completeness:\\\\n  coverage: 73/77\\\\n  claims: 71\\\\n  tables: 4\\\\n  figures: 6\\\\n  tier_counts:\\\\n    tier1: 0\\\\n    tier2: 73\\\\n    tier3: 4\\\\n    tierX: 0\\\\n  last_checked: '2026-05-25T03:36:26.590002+00:00'\\\\n\\\", \\\"total_chars\\\": 36692, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/paper_provenance.yaml\", \"content\": \"paper:\\n  title: 'Why Temporal Abstraction Fails in Imagination-Based RL: A Diagnostic Analysis\\n    of Variable-Rate DreamerV3'\\n  version: 38\\n  generated_at: '2026-05-25T03:36:26.589946+00:00'\\n  source: manual build by Paper Agent — schema v3 matching check_provenance_completeness\\nclaims:\\n- id: C001\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 0\\n  text: every variable-rate configuration of DreamerV3 degrades performance\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_006_fixed_dt2\\n    metric: eval_return_65K\\n    value: 132.86\\n    role: primary_evidence\\n  - exp_id: exp_007_fixed_dt4\\n    metric: peak_return\\n    value: 176.9\\n    role: primary_evidence\\n  - exp_id: exp_005_event_gated_v4\\n    metric: eval_return_145K\\n    value: 98.84\\n    role: primary_evidence\\n  decisions:\\n  - D009\\n  - D015\\n  deprecated: false\\n- id: C002\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 2\\n  text: trained temporal embedding as the causal factor\\n  type: methodological\\n  evidence:\\n  - exp_id: exp_008d_subsample_on_h8\\n    metric: eval_return_55K\\n    value: 82.75\\n    role: primary_evidence\\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\\n    metric: eval_return_105K\\n    value: 503.0\\n    role: control\\n  decisions:\\n  - D021\\n  deprecated: false\\n- id: C003\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 3\\n  text: 2.78x prediction gap between dt=1 and dt=2\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_rssm_fidelity_analysis\\n    metric: 008d_trained_dtEmb.reward_gap\\n    value: 2.78\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C004\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 4\\n  text: 7/8 classification (n=8)\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_008d_subsample_on_h8\\n    metric: peak_nve\\n    value: 4.12\\n    role: true_positive\\n  - exp_id: exp_006_fixed_dt2\\n    metric: model_loss_at_55k\\n    value: 4.853\\n    role: true_positive\\n  - exp_id: exp_009b_008d_walker_s2\\n    metric: peak_nve\\n    value: 1.62\\n    role: true_positive\\n  - exp_id: exp_008e_v3_walker_s2\\n    metric: final_nve\\n    value: 3.78\\n    role: false_positive\\n  decisions:\\n  - D053\\n  deprecated: false\\n- id: C005\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 5\\n  text: stochastic downstream outcomes — full collapse, transient CIVO, oscillatory\\n    degradation\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_008d_subsample_on_h8\\n    metric: eval_return_55K\\n    value: 82.75\\n    role: full_collapse\\n  - exp_id: exp_009b_008d_walker_s2\\n    metric: final_eval_return\\n    value: 267.93\\n    role: transient_civo\\n  - exp_id: exp_009e_008d_walker_s1\\n    metric: final_eval_return\\n    value: 131.08\\n    role: oscillatory\\n  decisions: []\\n  deprecated: false\\n- id: C006\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 6\\n  text: 'restricting imagination to dt=1 does not prevent collapse: one of two seeds\\n    fails'\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_008e_v3_walker_s1\\n    metric: final_eval_return\\n    value: 869.9\\n    role: healthy\\n  - exp_id: exp_008e_v3_walker_s2\\n    metric: final_eval_return\\n    value: 136.96\\n    role: collapsed\\n  - exp_id: exp_009a_baseline_walker_s2\\n    metric: final_eval_return\\n    value: 836.51\\n    role: control\\n  decisions: []\\n  deprecated: false\\n- id: C007\\n  location:\\n    section: introduction\\n    paragraph: 1\\n    sentence: 1\\n  text: fixed dt=2 collapses to 14% of baseline\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_006_fixed_dt2\\n    metric: eval_return_65K\\n    value: 132.86\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C008\\n  location:\\n    section: introduction\\n    paragraph: 1\\n    sentence: 1\\n  text: fixed dt=4 never exceeds 19% of baseline\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_007_fixed_dt4\\n    metric: peak_return\\n    value: 176.9\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C009\\n  location:\\n    section: introduction\\n    paragraph: 1\\n    sentence: 1\\n  text: learned Gumbel-Softmax gate collapses to 11%\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_005_event_gated_v4\\n    metric: eval_return_145K\\n    value: 98.84\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C010\\n  location:\\n    section: methodology\\n    paragraph: 8\\n    sentence: 0\\n  text: baseline runs for 500K steps, peak return 970.4\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_001_baseline\\n    metric: eval_return_peak\\n    value: 970.41\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C011\\n  location:\\n    section: methodology\\n    paragraph: 6\\n    sentence: 3\\n  text: 7/8 accuracy (AUROC=0.933)\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_008d_subsample_on_h8\\n    metric: peak_nve\\n    value: 4.12\\n    role: true_positive\\n  - exp_id: exp_009b_008d_walker_s2\\n    metric: peak_nve\\n    value: 1.62\\n    role: true_positive\\n  decisions:\\n  - D053\\n  - D054\\n  deprecated: false\\n- id: C012\\n  location:\\n    section: results\\n    paragraph: 0\\n    sentence: 1\\n  text: baseline reaches 915.7 at 105K and peaks at 970.4 at 505K\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_001_baseline\\n    metric: eval_return_peak\\n    value: 970.41\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C013\\n  location:\\n    section: results\\n    paragraph: 0\\n    sentence: 2\\n  text: fixed dt=2 peaks at 485.3 at 35K before collapsing to 132.9 by 65K\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_006_fixed_dt2\\n    metric: peak_return\\n    value: 485.3\\n    role: primary_evidence\\n  - exp_id: exp_006_fixed_dt2\\n    metric: eval_return_65K\\n    value: 132.86\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C014\\n  location:\\n    section: results\\n    paragraph: 0\\n    sentence: 3\\n  text: fixed dt=4 peaks at 176.9 at 25K\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_007_fixed_dt4\\n    metric: peak_return\\n    value: 176.9\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C015\\n  location:\\n    section: results\\n    paragraph: 0\\n    sentence: 4\\n  text: learned-gate peaks at 541.2 at 55K collapses to 98.8 by 145K\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_005_event_gated_v4\\n    metric: peak_return\\n    value: 541.18\\n    role: primary_evidence\\n  - exp_id: exp_005_event_gated_v4\\n    metric: eval_return_145K\\n    value: 98.84\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C016\\n  location:\\n    section: results\\n    paragraph: 3\\n    sentence: 0\\n  text: 008d NVE=4.12x at 55K, collapse eval 167→82.8\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_008d_subsample_on_h8\\n    metric: eval_return_55K\\n    value: 82.75\\n    role: primary_evidence\\n  - exp_id: exp_008d_subsample_on_h8\\n    metric: eval_return_25K\\n    value: 167.22\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C017\\n  location:\\n    section: results\\n    paragraph: 3\\n    sentence: 1\\n  text: 008f NVE=0.30x at 105K, no collapse eval 503.0\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\\n    metric: eval_return_105K\\n    value: 503.0\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C018\\n  location:\\n    section: results\\n    paragraph: 4\\n    sentence: 0\\n  text: AUROC=0.933, Clopper-Pearson 95% CI [0.47, 1.0]\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_008d_subsample_on_h8\\n    metric: peak_nve\\n    value: 4.12\\n    role: true_positive\\n  - exp_id: exp_009b_008d_walker_s2\\n    metric: peak_nve\\n    value: 1.62\\n    role: true_positive\\n  - exp_id: exp_008e_v3_walker_s2\\n    metric: final_nve\\n    value: 3.78\\n    role: false_positive\\n  decisions:\\n  - D054\\n  deprecated: false\\n- id: C019\\n  location:\\n    section: results\\n    paragraph: 4\\n    sentence: 1\\n  text: gap between lowest TP (1.62x) and highest TN (1.00x) is 0.62\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_009b_008d_walker_s2\\n    metric: peak_nve\\n    value: 1.62\\n    role: true_positive\\n  decisions: []\\n  deprecated: false\\n- id: C020\\n  location:\\n    section: results\\n    paragraph: 6\\n    sentence: 0\\n  text: 'Seed 0 (008d) full collapse: eval 167→82.8, value +130%'\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_008d_subsample_on_h8\\n    metric: eval_return_55K\\n    value: 82.75\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C021\\n  location:\\n    section: results\\n    paragraph: 7\\n    sentence: 0\\n  text: 'Seed 2 (009b) transient CIVO: NVE 1.62x at 45K, self-corrects to 0.38x, eval\\n    267.9'\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_009b_008d_walker_s2\\n    metric: final_eval_return\\n    value: 267.93\\n    role: primary_evidence\\n  - exp_id: exp_009b_008d_walker_s2\\n    metric: final_nve\\n    value: 0.38\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C022\\n  location:\\n    section: results\\n    paragraph: 8\\n    sentence: 0\\n  text: 'Seed 1 (009e) oscillatory: eval 82.7-250, settles 131.1, peak NVE=4.12x,\\n    final 1.57x'\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_009e_008d_walker_s1\\n    metric: final_eval_return\\n    value: 131.08\\n    role: primary_evidence\\n  - exp_id: exp_009e_008d_walker_s1\\n    metric: final_nve\\n    value: 1.57\\n    role: primary_evidence\\n  - exp_id: exp_009e_008d_walker_s1\\n    metric: peak_nve\\n    value: 4.12\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C023\\n  location:\\n    section: results\\n    paragraph: 10\\n    sentence: 0\\n  text: 008a reaches 777.7 (NVE=0.59x)\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_008a_no_subsample_dt2\\n    metric: eval_return_105K\\n    value: 777.66\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C024\\n  location:\\n    section: results\\n    paragraph: 10\\n    sentence: 0\\n  text: 008c reaches 240.9 (NVE=0.58x)\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_008c_no_subsample_dt2_h8\\n    metric: eval_return_65K\\n    value: 240.86\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C025\\n  location:\\n    section: results\\n    paragraph: 12\\n    sentence: 0\\n  text: dt=1 (915.7) > dt=2 (485.3, -47%) > dt=4 (176.9, -81%)\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_006_fixed_dt2\\n    metric: peak_return\\n    value: 485.3\\n    role: primary_evidence\\n  - exp_id: exp_007_fixed_dt4\\n    metric: peak_return\\n    value: 176.9\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C026\\n  location:\\n    section: results\\n    paragraph: 14\\n    sentence: 0\\n  text: 008d collapses NVE=4.12x vs untrained configs NVE<0.6x\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_008d_subsample_on_h8\\n    metric: eval_return_55K\\n    value: 82.75\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C027\\n  location:\\n    section: results\\n    paragraph: 14\\n    sentence: 1\\n  text: 'cross-seed variance: 008f 503.0 vs 009c 148.3'\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\\n    metric: eval_return_105K\\n    value: 503.0\\n    role: primary_evidence\\n  - exp_id: exp_009c_008f_walker_s2\\n    metric: final_eval_return\\n    value: 148.34\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C028\\n  location:\\n    section: results\\n    paragraph: 16\\n    sentence: 0\\n  text: '008e_v3 s1 healthy: eval 869.9 (95% of baseline), NVE=0.80x'\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_008e_v3_walker_s1\\n    metric: final_eval_return\\n    value: 869.9\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C029\\n  location:\\n    section: results\\n    paragraph: 16\\n    sentence: 1\\n  text: '008e_v3 s2 collapsed: eval 715→137, NVE=3.78x'\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_008e_v3_walker_s2\\n    metric: final_eval_return\\n    value: 136.96\\n    role: primary_evidence\\n  - exp_id: exp_008e_v3_walker_s2\\n    metric: peak_eval_return\\n    value: 715.21\\n    role: primary_evidence\\n  - exp_id: exp_008e_v3_walker_s2\\n    metric: final_nve\\n    value: 3.78\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C030\\n  location:\\n    section: results\\n    paragraph: 17\\n    sentence: 0\\n  text: baseline seed 2 (009a) stable at 836.5\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_009a_baseline_walker_s2\\n    metric: final_eval_return\\n    value: 836.51\\n    role: control\\n  decisions: []\\n  deprecated: false\\n- id: C031\\n  location:\\n    section: results\\n    paragraph: 18\\n    sentence: 1\\n  text: '008e_v3_s2 Pathway B: entropy increases (-5.21→-3.83)'\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_008e_v3_walker_s2\\n    metric: final_eval_return\\n    value: 136.96\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C032\\n  location:\\n    section: results\\n    paragraph: 19\\n    sentence: 0\\n  text: 008e_v3_s2 NVE=3.78x false positive (non-CIVO)\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_008e_v3_walker_s2\\n    metric: final_nve\\n    value: 3.78\\n    role: false_positive\\n  decisions:\\n  - D053\\n  deprecated: false\\n- id: C033\\n  location:\\n    section: results\\n    paragraph: 21\\n    sentence: 0\\n  text: 008d reward gap 2.78x (dt1 MAE=0.0568, dt2 MAE=0.1579)\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_rssm_fidelity_analysis\\n    metric: 008d_trained_dtEmb.reward_gap\\n    value: 2.78\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C034\\n  location:\\n    section: results\\n    paragraph: 21\\n    sentence: 1\\n  text: 008f reward gap 1.01x (MAE 0.7469)\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_rssm_fidelity_analysis\\n    metric: 008f_no_dtEmb.reward_gap\\n    value: 1.01\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C035\\n  location:\\n    section: results\\n    paragraph: 21\\n    sentence: 1\\n  text: 008f absolute MAE 0.7469 vs 008d 0.0568 at dt=1\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_rssm_fidelity_analysis\\n    metric: 008f_no_dtEmb.dt1_reward_mae\\n    value: 0.7469\\n    role: primary_evidence\\n  - exp_id: exp_rssm_fidelity_analysis\\n    metric: 008d_trained_dtEmb.dt1_reward_mae\\n    value: 0.0568\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C036\\n  location:\\n    section: analysis\\n    paragraph: 2\\n    sentence: 0\\n  text: 'two-stage amplification: Stage 1 dynamics bias 1.68x, Stage 2 actor exploitation\\n    2.90x'\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_008d_subsample_on_h8\\n    metric: random_policy_reward_ratio\\n    value: 1.68\\n    role: stage1\\n  - exp_id: exp_008d_subsample_on_h8\\n    metric: trained_actor_reward_ratio\\n    value: 2.9\\n    role: stage2\\n  decisions:\\n  - D042\\n  deprecated: false\\n- id: C037\\n  location:\\n    section: analysis\\n    paragraph: 2\\n    sentence: 1\\n  text: ~36% dynamics bias, ~64% actor exploitation\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_008d_subsample_on_h8\\n    metric: dynamics_bias_fraction\\n    value: 0.36\\n    role: primary_evidence\\n  decisions:\\n  - D042\\n  deprecated: false\\n- id: C038\\n  location:\\n    section: analysis\\n    paragraph: 2\\n    sentence: 2\\n  text: '008f control: random 1.11x, trained 0.98x — no effect'\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\\n    metric: random_policy_reward_ratio\\n    value: 1.11\\n    role: control\\n  - exp_id: exp_008f_no_dt_embed_subsample_on_h8\\n    metric: trained_actor_reward_ratio\\n    value: 0.98\\n    role: control\\n  decisions:\\n  - D042\\n  deprecated: false\\n- id: C039\\n  location:\\n    section: analysis\\n    paragraph: 4\\n    sentence: 0\\n  text: all runs cross NVE>1.5x — CIVO triggers deterministically\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_008d_subsample_on_h8\\n    metric: peak_nve\\n    value: 4.12\\n    role: primary_evidence\\n  - exp_id: exp_009b_008d_walker_s2\\n    metric: peak_nve\\n    value: 1.62\\n    role: primary_evidence\\n  - exp_id: exp_009e_008d_walker_s1\\n    metric: peak_nve\\n    value: 4.12\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C040\\n  location:\\n    section: analysis\\n    paragraph: 7\\n    sentence: 0\\n  text: 'removing dt_emb: 13x cost to reward prediction (0.7469 vs 0.0568)'\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_rssm_fidelity_analysis\\n    metric: 008f_no_dtEmb.dt1_reward_mae\\n    value: 0.7469\\n    role: primary_evidence\\n  - exp_id: exp_rssm_fidelity_analysis\\n    metric: 008d_trained_dtEmb.dt1_reward_mae\\n    value: 0.0568\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C041\\n  location:\\n    section: analysis\\n    paragraph: 8\\n    sentence: 1\\n  text: 'Pathway B FP: 008e_v3_s2 NVE=3.78x non-CIVO'\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_008e_v3_walker_s2\\n    metric: final_nve\\n    value: 3.78\\n    role: false_positive\\n  decisions:\\n  - D053\\n  deprecated: false\\n- id: C042\\n  location:\\n    section: conclusion\\n    paragraph: 0\\n    sentence: 2\\n  text: 7/8 CIVO classification (n=8, 87.5%)\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_008d_subsample_on_h8\\n    metric: peak_nve\\n    value: 4.12\\n    role: true_positive\\n  - exp_id: exp_009b_008d_walker_s2\\n    metric: peak_nve\\n    value: 1.62\\n    role: true_positive\\n  decisions:\\n  - D053\\n  deprecated: false\\n- id: C043\\n  location:\\n    section: conclusion\\n    paragraph: 2\\n    sentence: 1\\n  text: NVE margin 0.62 excluding outlier\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_009b_008d_walker_s2\\n    metric: peak_nve\\n    value: 1.62\\n    role: lowest_true_positive\\n  decisions: []\\n  deprecated: false\\n- id: C044\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: Extended NVE validation (n=32) achieves F1=0.880 at 1.5x threshold\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C045\\n  location:\\n    section: sections/analysis\\n    paragraph: 0\\n    sentence: 0\\n  text: NVE diagnostic extended validation n=32 AUROC=0.961 F1=0.880\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C046\\n  location:\\n    section: sections/analysis\\n    paragraph: 0\\n    sentence: 0\\n  text: 'Entropy explosion is lagging indicator: +2.1 nats/10K collapsed vs +0.07-0.22\\n    healthy, return collapses ~35K steps before entropy rises'\\n  type: quantitative\\n  evidence: []\\n  decisions: []\\n  deprecated: false\\n- id: C047\\n  location:\\n    section: sections/methodology\\n    paragraph: 0\\n    sentence: 0\\n  text: NVE threshold 29/32 accuracy (AUROC=0.961, F1=0.880) at n=32\\n  type: quantitative\\n  evidence:\\n  - exp_id: plan_034_nve_threshold\\n    metric: auroc_n32\\n    value: 0.961\\n    role: primary_evidence\\n  - exp_id: plan_034_nve_threshold\\n    metric: f1_at_1.5x\\n    value: 0.88\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C048\\n  location:\\n    section: sections/results\\n    paragraph: 0\\n    sentence: 0\\n  text: NVE threshold 29/32 classification (n=32, AUROC=0.961, F1=0.880)\\n  type: quantitative\\n  evidence:\\n  - exp_id: plan_034_nve_threshold\\n    metric: auroc_n32\\n    value: 0.961\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C049\\n  location:\\n    section: sections/abstract_body\\n    paragraph: 0\\n    sentence: 0\\n  text: CIVO classification 29/32 AUROC=0.961 F1=0.880\\n  type: quantitative\\n  evidence:\\n  - exp_id: plan_034_nve_threshold\\n    metric: auroc_n32\\n    value: 0.961\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C050\\n  location:\\n    section: sections/introduction\\n    paragraph: 0\\n    sentence: 0\\n  text: NVE threshold 29/32 classification in introduction\\n  type: quantitative\\n  evidence:\\n  - exp_id: plan_034_nve_threshold\\n    metric: auroc_n32\\n    value: 0.961\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C051\\n  location:\\n    section: sections/introduction\\n    paragraph: 0\\n    sentence: 0\\n  text: Contribution 1 AUROC updated to 0.961\\n  type: quantitative\\n  evidence:\\n  - exp_id: plan_034_nve_threshold\\n    metric: auroc_n32\\n    value: 0.961\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C052\\n  location:\\n    section: sections/conclusion\\n    paragraph: 0\\n    sentence: 0\\n  text: Conclusion NVE updated to 29/32 AUROC=0.961\\n  type: quantitative\\n  evidence:\\n  - exp_id: plan_034_nve_threshold\\n    metric: auroc_n32\\n    value: 0.961\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C053\\n  location:\\n    section: sections/analysis\\n    paragraph: 0\\n    sentence: 0\\n  text: Discussion NVE diagnostic consolidated to n=32 AUROC=0.961\\n  type: quantitative\\n  evidence:\\n  - exp_id: plan_034_nve_threshold\\n    metric: auroc_n32\\n    value: 0.961\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C054\\n  location:\\n    section: sections/results\\n    paragraph: 0\\n    sentence: 0\\n  text: RSSM reward prediction gap 2.78x corroborated at 3.11x with 600-sample validation\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_rssm_fidelity_analysis\\n    metric: 008d_trained_dtEmb.reward_gap\\n    value: 2.78\\n    role: primary_evidence\\n  - exp_id: exp_063_rssm_fidelity\\n    metric: collapsed_reward_gap\\n    value: 3.11\\n    role: corroboration\\n  decisions: []\\n  deprecated: false\\n- id: C055\\n  location:\\n    section: sections/results\\n    paragraph: 0\\n    sentence: 0\\n  text: CIVO model median V(s)/MC-return ratio 3.40 vs no-dt-emb control 1.05\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_064_value_distribution\\n    metric: civo_median_v_mc_ratio\\n    value: 3.4\\n    role: primary_evidence\\n  - exp_id: exp_064_value_distribution\\n    metric: control_median_v_mc_ratio\\n    value: 1.05\\n    role: control\\n  decisions: []\\n  deprecated: false\\n- id: C056\\n  location:\\n    section: sections/results\\n    paragraph: 0\\n    sentence: 0\\n  text: 'Return collapses ~35K steps before entropy rises: +2.1 nats/10K collapsed\\n    vs +0.07-0.22 healthy'\\n  type: quantitative\\n  evidence:\\n  - exp_id: plan_031_actor_entropy\\n    metric: collapsed_entropy_rate\\n    value: 2.1\\n    role: primary_evidence\\n  - exp_id: plan_031_actor_entropy\\n    metric: healthy_entropy_rate_range\\n    value: 0.07-0.22\\n    role: control\\n  decisions: []\\n  deprecated: false\\n- id: C057\\n  location:\\n    section: sections/analysis\\n    paragraph: 0\\n    sentence: 0\\n  text: RSSM reward gap 2.78-3.11x range across two independent analyses\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_rssm_fidelity_analysis\\n    metric: 008d_trained_dtEmb.reward_gap\\n    value: 2.78\\n    role: primary_evidence\\n  - exp_id: exp_063_rssm_fidelity\\n    metric: collapsed_reward_gap\\n    value: 3.11\\n    role: corroboration\\n  decisions: []\\n  deprecated: false\\n- id: C058\\n  location:\\n    section: sections/analysis\\n    paragraph: 0\\n    sentence: 0\\n  text: 'Obs-decoder SGS compensatory amplification: NVE from 8.3x to 21.9-30.2x on\\n    Cheetah'\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_026_obs_sgs_cheetah\\n    metric: nve_amplification\\n    value: 21.9-30.2\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C059\\n  location:\\n    section: sections/analysis\\n    paragraph: 0\\n    sentence: 0\\n  text: 'TCN impossible dose: sigma=1.0 Cheetah suppresses CIVO (NVE<=0.3x) but eval→15%\\n    baseline'\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_030c_tcn_cheetah\\n    metric: nve_suppressed\\n    value: 0.3\\n    role: primary_evidence\\n  - exp_id: exp_030c_tcn_cheetah\\n    metric: eval_pct_baseline\\n    value: 15\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C060\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: 'Trained dt_emb cosine similarity: cos(dt1,dt2) = -0.87 to -0.94 at 25K, -0.70\\n    to -0.86 at 75K'\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_065_dt_emb_cosine\\n    metric: trained_cos_25k_range\\n    value: -0.87 to -0.94\\n    role: primary_evidence\\n  - exp_id: exp_065_dt_emb_cosine\\n    metric: trained_cos_75k_range\\n    value: -0.70 to -0.86\\n    role: primary_evidence\\n  decisions: []\\n  deprecated: false\\n- id: C061\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: 'Frozen dt_emb cosine similarity: near-zero (-0.15 to +0.07), constant'\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_065_dt_emb_cosine\\n    metric: frozen_cos_constant\\n    value: -0.15 to +0.07\\n    role: control\\n  decisions: []\\n  deprecated: false\\n- id: C062\\n  location:\\n    section: sections/introduction\\n    paragraph: 0\\n    sentence: 0\\n  text: RSSM reward prediction gap 2.78-3.11x in introduction\\n  type: quantitative\\n  evidence:\\n  - exp_id: exp_rssm_fidelity_analysis\\n    metric: 008d_trained_dtEmb.reward_gap\\n    value: 2.78\\n    role: primary_evidence\\n  - exp_id: exp_063_rssm_fidelity\\n    metric: collapsed_reward_gap\\n    value: 3.11\\n    role: corroboration\\n  decisions: []\\n  deprecated: false\\n- id: C063\\n  location:\\n    section: sections/results\\n    paragraph: 0\\n    sentence: 0\\n  text: RSSM reward MAE increases from 0.057 to 0.178 (3.11x gap) at dt=2 under trained\\n    conditioning\\n  type: quantitative\\n  evidence: exp_063 rssm_fidelity_analysis, 600-sample validation\\n  decisions: []\\n  deprecated: false\\n- id: C064\\n  location:\\n    section: sections/results\\n    paragraph: 0\\n    sentence: 0\\n  text: Observation reconstruction gap improves with temporal conditioning (1.33x\\n    vs baseline 1.46x)\\n  type: quantitative\\n  evidence: exp_063 obs_mse data\\n  decisions: []\\n  deprecated: false\\n- id: C065\\n  location:\\n    section: sections/results\\n    paragraph: 0\\n    sentence: 0\\n  text: CIVO model mean V/MC ratio = 7.80x (median 3.40x, 100% overestimated) vs control\\n    median 1.05x (52.5% overestimated)\\n  type: quantitative\\n  evidence: exp_064 value_distribution results_summary\\n  decisions: []\\n  deprecated: false\\n- id: C066\\n  location:\\n    section: sections/analysis\\n    paragraph: 0\\n    sentence: 0\\n  text: RSSM reward MAE 0.057→0.178 at dt=2; obs gap 1.33x vs baseline 1.46x — reward-specific\\n    pathology\\n  type: quantitative\\n  evidence: exp_063 rssm_fidelity_analysis\\n  decisions: []\\n  deprecated: false\\n- id: C067\\n  location:\\n    section: sections/results\\n    paragraph: 0\\n    sentence: 0\\n  text: SS fidelity ratio crosses 1.1x at 20K steps, VE ratio first exceeds 1.5x at\\n    40K steps — ~10-15K step lag (r=0.81, p=0.002, n=1)\\n  type: quantitative\\n  evidence: exp_066 timeseries analysis, 12 dense checkpoints\\n  decisions: []\\n  deprecated: false\\n- id: C068\\n  location:\\n    section: sections/results\\n    paragraph: 0\\n    sentence: 0\\n  text: dt=1 MAE decreases 0.093→0.047 while dt=2 MAE plateaus ~0.08 — gap from differential\\n    improvement\\n  type: quantitative\\n  evidence: exp_066 timeseries analysis\\n  decisions: []\\n  deprecated: false\\n- id: C069\\n  location:\\n    section: sections/analysis\\n    paragraph: 0\\n    sentence: 0\\n  text: 'Three-stage causal chain: fidelity gap (20K) → value overestimation (40K)\\n    → entropy destabilization (~35K later), n=1'\\n  type: quantitative\\n  evidence: exp_066 timeseries + actor entropy analysis\\n  decisions: []\\n  deprecated: false\\n- id: C070\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: 'exp_066 timeseries: SS fidelity ratio grows 1.05→1.68 over 10K-65K steps;\\n    VE ratio near zero until 40K spike (1.59x)'\\n  type: quantitative\\n  evidence: exp_066 12-checkpoint timeseries analysis\\n  decisions: []\\n  deprecated: false\\n- id: C071\\n  location:\\n    section: sections/appendix\\n    paragraph: 0\\n    sentence: 0\\n  text: dt=1 MAE 0.090→0.047 (monotonic decrease), dt=2 MAE plateaus ~0.08; gap from\\n    selective improvement not worsening\\n  type: quantitative\\n  evidence: exp_066 timeseries MAE data\\n  decisions: []\\n  deprecated: false\\ntables:\\n- id: T001\\n  location:\\n    section: methodology\\n    table_number: 1\\n  caption: Factorial design — 9 configurations\\n  cells:\\n  - row: 0\\n    col: 0\\n    value: '001'\\n    source:\\n      exp_id: exp_001_baseline\\n      metric: exp_id\\n  - row: 1\\n    col: 0\\n    value: '006'\\n    source:\\n      exp_id: exp_006_fixed_dt2\\n      metric: exp_id\\n  - row: 2\\n    col: 0\\n    value: '007'\\n    source:\\n      exp_id: exp_007_fixed_dt4\\n      metric: exp_id\\n  - row: 3\\n    col: 0\\n    value: '005'\\n    source:\\n      exp_id: exp_005_event_gated_v4\\n      metric: exp_id\\n  - row: 4\\n    col: 0\\n    value: 008d\\n    source:\\n      exp_id: exp_008d_subsample_on_h8\\n      metric: exp_id\\n  - row: 5\\n    col: 0\\n    value: 008f\\n    source:\\n      exp_id: exp_008f_no_dt_embed_subsample_on_h8\\n      metric: exp_id\\n  - row: 6\\n    col: 0\\n    value: 008a\\n    source:\\n      exp_id: exp_008a_no_subsample_dt2\\n      metric: exp_id\\n  - row: 7\\n    col: 0\\n    value: 008c\\n    source:\\n      exp_id: exp_008c_no_subsample_dt2_h8\\n      metric: exp_id\\n  - row: 8\\n    col: 0\\n    value: 008e_v3\\n    source:\\n      exp_id: exp_008e_v3_subsample_on_dt1_h15\\n      metric: exp_id\\n  deprecated: false\\n- id: T002\\n  location:\\n    section: results\\n    table_number: 1\\n  caption: All configurations and outcomes\\n  cells:\\n  - row: 0\\n    col: 5\\n    value: 915.7\\n    source:\\n      exp_id: exp_001_baseline\\n      metric: eval_return_105K\\n  - row: 1\\n    col: 5\\n    value: 132.9\\n    source:\\n      exp_id: exp_006_fixed_dt2\\n      metric: eval_return_65K\\n  - row: 1\\n    col: 6\\n    value: 4.83\\n    source:\\n      exp_id: exp_006_fixed_dt2\\n      metric: peak_nve\\n  - row: 2\\n    col: 5\\n    value: 152.5\\n    source:\\n      exp_id: exp_007_fixed_dt4\\n      metric: eval_return_55K\\n  - row: 3\\n    col: 5\\n    value: 98.8\\n    source:\\n      exp_id: exp_005_event_gated_v4\\n      metric: eval_return_145K\\n  - row: 4\\n    col: 5\\n    value: 82.8\\n    source:\\n      exp_id: exp_008d_subsample_on_h8\\n      metric: eval_return_55K\\n  - row: 4\\n    col: 6\\n    value: 4.12\\n    source:\\n      exp_id: exp_008d_subsample_on_h8\\n      metric: peak_nve\\n  - row: 5\\n    col: 5\\n    value: 267.9\\n    source:\\n      exp_id: exp_009b_008d_walker_s2\\n      metric: final_eval_return\\n  - row: 5\\n    col: 6\\n    value: 1.62\\n    source:\\n      exp_id: exp_009b_008d_walker_s2\\n      metric: peak_nve\\n  - row: 6\\n    col: 5\\n    value: 131.1\\n    source:\\n      exp_id: exp_009e_008d_walker_s1\\n      metric: final_eval_return\\n  - row: 6\\n    col: 6\\n    value: 4.12\\n    source:\\n      exp_id: exp_009e_008d_walker_s1\\n      metric: peak_nve\\n  - row: 7\\n    col: 5\\n    value: 503.0\\n    source:\\n      exp_id: exp_008f_no_dt_embed_subsample_on_h8\\n      metric: eval_return_105K\\n  - row: 8\\n    col: 5\\n    value: 148.3\\n    source:\\n      exp_id: exp_009c_008f_walker_s2\\n      metric: final_eval_return\\n  - row: 9\\n    col: 5\\n    value: 777.7\\n    source:\\n      exp_id: exp_008a_no_subsample_dt2\\n      metric: eval_return_105K\\n  - row: 10\\n    col: 5\\n    value: 240.9\\n    source:\\n      exp_id: exp_008c_no_subsample_dt2_h8\\n      metric: eval_return_65K\\n  - row: 11\\n    col: 5\\n    value: 869.9\\n    source:\\n      exp_id: exp_008e_v3_walker_s1\\n      metric: final_eval_return\\n  - row: 12\\n    col: 5\\n    value: 137.0\\n    source:\\n      exp_id: exp_008e_v3_walker_s2\\n      metric: final_eval_return\\n  - row: 12\\n    col: 6\\n    value: 3.78\\n    source:\\n      exp_id: exp_008e_v3_walker_s2\\n      metric: final_nve\\n  - row: 13\\n    col: 5\\n    value: 836.5\\n    source:\\n      exp_id: exp_009a_baseline_walker_s2\\n      metric: final_eval_return\\n  deprecated: false\\n- id: T003\\n  location:\\n    section: results\\n    table_number: 2\\n  caption: RSSM fidelity at dt=1 vs dt=2\\n  cells:\\n  - row: 0\\n    col: 0\\n    value: 13.49\\n    source:\\n      exp_id: exp_rssm_fidelity_analysis\\n      metric: baseline.dt1_obs_mse\\n  - row: 0\\n    col: 1\\n    value: 27.5\\n    source:\\n      exp_id: exp_rssm_fidelity_analysis\\n      metric: baseline.dt2_obs_mse\\n  - row: 0\\n    col: 2\\n    value: 2.04\\n    source:\\n      exp_id: exp_rssm_fidelity_analysis\\n      metric: baseline.obs_gap\\n  - row: 0\\n    col: 3\\n    value: 0.0102\\n    source:\\n      exp_id: exp_rssm_fidelity_analysis\\n      metric: baseline.dt1_reward_mae\\n  - row: 0\\n    col: 4\\n    value: 0.0159\\n    source:\\n      exp_id: exp_rssm_fidelity_analysis\\n      metric: baseline.dt2_reward_mae\\n  - row: 0\\n    col: 5\\n    value: 1.56\\n    source:\\n      exp_id: exp_rssm_fidelity_analysis\\n      metric: baseline.reward_gap\\n  - row: 1\\n    col: 0\\n    value: 41.31\\n    source:\\n      exp_id: exp_rssm_fidelity_analysis\\n      metric: 008d_trained_dtEmb.dt1_obs_mse\\n  - row: 1\\n    col: 1\\n    value: 53.67\\n    source:\\n      exp_id: exp_rssm_fidelity_analysis\\n      metric: 008d_trained_dtEmb.dt2_obs_mse\\n  - row: 1\\n    col: 2\\n    value: 1.3\\n    source:\\n      exp_id: exp_rssm_fidelity_analysis\\n      metric: 008d_trained_dtEmb.obs_gap\\n  - row: 1\\n    col: 3\\n    value: 0.0568\\n    source:\\n      exp_id: exp_rssm_fidelity_analysis\\n      metric: 008d_trained_dtEmb.dt1_reward_mae\\n  - row: 1\\n    col: 4\\n    value: 0.1579\\n    source:\\n      exp_id: exp_rssm_fidelity_analysis\\n      metric: 008d_trained_dtEmb.dt2_reward_mae\\n  - row: 1\\n    col: 5\\n    value: 2.78\\n    source:\\n      exp_id: exp_rssm_fidelity_analysis\\n      metric: 008d_trained_dtEmb.reward_gap\\n  - row: 2\\n    col: 0\\n    value: 8.01\\n    source:\\n      exp_id: exp_rssm_fidelity_analysis\\n      metric: 008f_no_dtEmb.dt1_obs_mse\\n  - row: 2\\n    col: 1\\n    value: 22.04\\n    source:\\n      exp_id: exp_rssm_fidelity_analysis\\n      metric: 008f_no_dtEmb.dt2_obs_mse\\n  - row: 2\\n    col: 2\\n    value: 2.75\\n    source:\\n      exp_id: exp_rssm_fidelity_analysis\\n      metric: 008f_no_dtEmb.obs_gap\\n  - row: 2\\n    col: 3\\n    value: 0.7469\\n    source:\\n      exp_id: exp_rssm_fidelity_analysis\\n      metric: 008f_no_dtEmb.dt1_reward_mae\\n  - row: 2\\n    col: 4\\n    value: 0.7526\\n    source:\\n      exp_id: exp_rssm_fidelity_analysis\\n      metric: 008f_no_dtEmb.dt2_reward_mae\\n  - row: 2\\n    col: 5\\n    value: 1.01\\n    source:\\n      exp_id: exp_rssm_fidelity_analysis\\n      metric: 008f_no_dtEmb.reward_gap\\n  deprecated: false\\n- id: T004\\n  location:\\n    section: results\\n    table_number: 3\\n  caption: Post-CIVO outcomes for 008d configuration\\n  cells:\\n  - row: 0\\n    col: 0\\n    value: 4.12\\n    source:\\n      exp_id: exp_008d_subsample_on_h8\\n      metric: peak_nve\\n  - row: 0\\n    col: 1\\n    value: 4.12\\n    source:\\n      exp_id: exp_008d_subsample_on_h8\\n      metric: peak_nve\\n  - row: 0\\n    col: 2\\n    value: 82.8\\n    source:\\n      exp_id: exp_008d_subsample_on_h8\\n      metric: eval_return_55K\\n  - row: 1\\n    col: 0\\n    value: 1.62\\n    source:\\n      exp_id: exp_009b_008d_walker_s2\\n      metric: peak_nve\\n  - row: 1\\n    col: 1\\n    value: 0.38\\n    source:\\n      exp_id: exp_009b_008d_walker_s2\\n      metric: final_nve\\n  - row: 1\\n    col: 2\\n    value: 267.9\\n    source:\\n      exp_id: exp_009b_008d_walker_s2\\n      metric: final_eval_return\\n  - row: 2\\n    col: 0\\n    value: 4.12\\n    source:\\n      exp_id: exp_009e_008d_walker_s1\\n      metric: peak_nve\\n  - row: 2\\n    col: 1\\n    value: 1.57\\n    source:\\n      exp_id: exp_009e_008d_walker_s1\\n      metric: final_nve\\n  - row: 2\\n    col: 2\\n    value: 131.1\\n    source:\\n      exp_id: exp_009e_008d_walker_s1\\n      metric: final_eval_return\\n  deprecated: false\\nfigures:\\n- id: F001\\n  location:\\n    section: results\\n    figure_number: 1\\n  caption: Learning curves for all configurations\\n  type: result\\n  source:\\n    experiments:\\n    - exp_id: exp_001_baseline\\n    - exp_id: exp_006_fixed_dt2\\n    - exp_id: exp_007_fixed_dt4\\n    - exp_id: exp_005_event_gated_v4\\n    - exp_id: exp_008d_subsample_on_h8\\n    - exp_id: exp_008f_no_dt_embed_subsample_on_h8\\n    - exp_id: exp_008a_no_subsample_dt2\\n    - exp_id: exp_008e_v3_walker_s1\\n  output_path: figures/paper/fig1_learning_curves.pdf\\n  deprecated: false\\n- id: F002\\n  location:\\n    section: results\\n    figure_number: 2\\n  caption: Normalized value-to-eval ratio trajectories\\n  type: result\\n  source:\\n    experiments:\\n    - exp_id: exp_008d_subsample_on_h8\\n    - exp_id: exp_008f_no_dt_embed_subsample_on_h8\\n    - exp_id: exp_008a_no_subsample_dt2\\n    - exp_id: exp_008e_v3_walker_s1\\n    - exp_id: exp_009b_008d_walker_s2\\n  output_path: figures/paper/fig2_nve_trajectory.pdf\\n  deprecated: false\\n- id: F003\\n  location:\\n    section: results\\n    figure_number: 3\\n  caption: Factorial experiment summary grid\\n  type: result\\n  source:\\n    experiments:\\n    - exp_id: exp_008d_subsample_on_h8\\n    - exp_id: exp_008f_no_dt_embed_subsample_on_h8\\n    - exp_id: exp_008a_no_subsample_dt2\\n    - exp_id: exp_008c_no_subsample_dt2_h8\\n  output_path: figures/paper/fig3_factorial_grid.pdf\\n  deprecated: false\\n- id: F004\\n  location:\\n    section: results\\n    figure_number: 4\\n  caption: Peak evaluation return as function of imagination dt\\n  type: result\\n  source:\\n    experiments:\\n    - exp_id: exp_001_baseline\\n    - exp_id: exp_006_fixed_dt2\\n    - exp_id: exp_007_fixed_dt4\\n  output_path: figures/paper/fig5_dt_amplification.pdf\\n  deprecated: false\\n- id: F005\\n  location:\\n    section: results\\n    figure_number: 5\\n  caption: 'Contrasting collapse dynamics: CIVO vs non-CIVO'\\n  type: result\\n  source:\\n    experiments:\\n    - exp_id: exp_008d_subsample_on_h8\\n    - exp_id: exp_008e_v3_walker_s2\\n    - exp_id: exp_009a_baseline_walker_s2\\n  output_path: figures/paper/fig6_multiple_pathways.pdf\\n  deprecated: false\\n- id: F006\\n  location:\\n    section: sections/appendix\\n    figure_number: 0\\n  caption: ''\\n  type: other\\n  source: {}\\n  output_path: ''\\n  deprecated: false\\n_completeness:\\n  coverage: 73/77\\n  claims: 71\\n  tables: 4\\n  figures: 6\\n  tier_counts:\\n    tier1: 0\\n    tier2: 73\\n    tier3: 4\\n    tierX: 0\\n  last_checked: '2026-05-25T03:36:26.590002+00:00'\\n\", \"total_chars\": 36692, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 34_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive view. Let me also check what ROADMAP says vs current state. Let me check the ROADMAP notes about running experiments — it says exp_074/077/078/079 are running, but the actual registry shows exp_077/078/080/081 running, and exp_074/079 are DONE. So the ROADMAP is slightly outdated.

Let me now read the key parts of the paper to check data consistency. Let me look at the paper's main tex file for any numbers I can cross-reference.

Actually, I have enough information now. Let me compile the audit report.

## Summary of findings:


The ROADMAP is out of sync with the actual registry. It lists exp_074, exp_077, exp_078, and exp_079 as running, but the registry shows exp_077, exp_078, exp_080, and exp_081 are currently active. Meanwhile, exp_074 completed successfully and exp_079 was killed, both ready for analysis. The near-term task mentions analyzing these experiments once they're done, and since exp_074 and exp_079 have already finished, that work can proceed immediately.

The Cheetah results task is blocked waiting on exp_078 to complete. For the NVE threshold analysis, it looks like plan_034 was already finished based on the provenance records and the extensive analysis already documented in the appendix, so that's not actually a pending task. should be marked complete

4. `等待 Round 5 审稿结果`
   - Pure waiting → **blocked** (external dependency)

5. `Round 5 反馈 → 修正 → 数据锁定（5/27）`
   - Depends on Round 5 results → **blocked**

6. `ICML 2026 投稿（DDL 5/29）`
   - **blocked** on everything else completing

### ROADMAP "完成后下一批" evaluation:
1. plan_022 Cheetah causal control — blocked on exp_078
2. plan_034 NVE threshold sensitivity — **already done** (n=56, AUROC=0.990 in appendix)
3. plan_011/012 Walker 008d/008f seeds 1-2 — most reproductions are finished, with exp_071/073 covering the remaining 008f variants
4. plan_014 Walker 008e_v3 seeds 1-2 — **currently running** as exp_080 (s1) and exp_081 (s2)

### Rebuttal Q&A Check:

Going through the 15 Q&As, I'm checking Q1 about the frozen diagnostic 71% rate. The current data shows 5/7 frozen seeds with the original validation plus three additional seeds all triggering the issue, and exp_067 already captured the successful NVE=0.19 result without CIVO.

For Q5 on intervention hierarchy, the success rates look stable with no updates needed.

Q6 on NVE threshold needs updating — the rebuttal currently cites AUROC=0.957 at n=30, but the appendix now shows AUROC=0.990 at n=56, so I need to update that.

Q7 on sample sizes is stale — the rebuttal says 133 experiments with 63 successful, but the report shows 153 total experiments with 79 successful, so that needs updating too.

For Q8 on onset/outcome, the Walker seed statement seems current, but I should verify the locomotion seeds claim against the latest data, particularly checking exp_074.

Q10 on environment diversity references 133 experiments across 43 configurations, which is now outdated since we're at 153 experiments.

Q14 on seed count also uses the old 133 experiment figure with 63 successes and 35 negatives — needs the updated counts.

Q15 on NVE threshold has the same stale AUROC reference as Q6, so both need the n=56 numbers.

Looking at the appendix table, I notice 008a only shows three seed entries (008a, 008a_s1, 008a_s2), but exp_074 adds 008a_s3 as a fourth seed, so the appendix table is incomplete and needs that row added.

Now checking 008f entries — the appendix lists 008f (s1), 008f s4, and 009c s3, but I'm seeing exp_071 has 008f_s3 with eval 311.9 and exp_073 has 008f_s4 with eval 289.3. The appendix shows 008f s4 at 306.5, which doesn't match exp_073's 289.3, so these might be from different experimental runs. I need to clarify which results actually belong in the appendix and reconcile these discrepancies.

Looking at what's missing from the appendix: exp_074 (008a_walker_s3 with eval 855.9), exp_068 (008d_walker_repro_s1 with eval 39.1), exp_072 (008e_v3_walker_s5 with eval 853.1), and the list continues but got cut off.

I'm realizing some of these are analysis experiments rather than training runs, so they wouldn't belong in the complete_results table anyway. The key training run I need to track down is exp_074_008a_walker_s3, which is the third seed for the 008a configuration.

For exp_068, I'm seeing it's a reproduction of the 008d config on Walker Walk with seed=1, showing eval 39.1 and NVE ~0.3. This is distinct from exp_009e, which appears to be the seed=1 run of 008d itself, though they have different performance metrics (39.1 vs 131.1 eval return), suggesting they might be different seeds or separate runs entirely. (extended), exp_009b is seed=2. exp_068 is also seed=1 but a reproduction. So it's a duplicate of 009e config but different run.
   - Not necessarily needed if 009e already covers it.
3. **exp_072_008e_v3_walker_s5**: 008e_v3 seed=5. Appendix only has s1-s4 for 008e_v3. Should be added.
4. **exp_059_walker_trained_s5**: Already in appendix as row "059" — yes it's there.
5. **exp_069_008f_walker_repro_s1**: 008f seed=1 reproduction, eval 237.8. Appendix already has "008f" (s1, eval 503.0). Different run of same config? Different eval values suggest different runs.
6. **exp_071_008f_walker_s3**: 008f seed=3, eval 311.9. Appendix has "009c s3" at 311.9 — same eval value but different config labels, so there's a potential naming mismatch. exp_073 is 008f seed=4 with eval 289.3.

Looking at what's actually missing from the appendix: 008a_s3 from exp_074 with eval 855.9 confirms the no-CIVO pattern holds across all four seeds, 008e_v3 s5 from exp_072 at 853.1 adds another data point for the mitigation strategy, and 008f seeds 3 and 4 might need inclusion depending on whether they're duplicates or distinct runs.

The Cartpole experiments aren't in the appendix at all, and exp_067 with its frozen embedding configuration and eval 281.5 appears to be a different run from the dedicated frozen setup in the appendix, which shows much higher performance at 612.0.

Now I'm checking the data consistency across the key provenance claims. The C039 claim about CIVO triggering deterministically only lists three experiments as evidence, but we actually have five or more seeds now — the appendix table does include s3, s4, and s5, so the supporting data is there even if the provenance evidence is incomplete. For the AUROC claims across C004, C011, C018, and C042, there's a discrepancy: the original claims reference a 7/8 classification with n=8 and AUROC=0.933, but the current appendix and rebuttal show n=56 with AUROC=0.990, which is a significant difference I need to reconcile.

Looking more carefully at the appendix, the "Expanded ROC Analysis" section breaks down the results into n=30 in-sample (AUROC=0.957) and n=56 comprehensive validation (AUROC=0.990), while the paper body and provenance C047-C053 reference n=32 with AUROC=0.961. The provenance claim C047 specifically mentions "NVE threshold 29/32 accuracy (AUROC=0.961..." so there's a mismatch between what the provenance claims (n=32) and what the appendix now shows (n=56 for the comprehensive validation). The experiment counts are all over the place—ROADMAP lists 155 total with 78 successes, the report shows 79 successful out of 153 total, and the rebuttal claims 133 experiments. Plus the ROADMAP is outdated with some experiments marked as running when they're actually finished, and others running but not even listed. I need to reconcile these numbers and document the inconsistencies in the audit.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72aab3fa-ba3f-48a9-9029-1cec279461d0",
  "uuid": "14c6c2e4-0e6d-4a72-ae33-f254f4b16837",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018RJUS8k757VEC7wmGsEdKm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 35454,
      "cache_read_input_tokens": 44337,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 35454
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

_source line 35_

Now let me check the actual paper body for the NVE numbers referenced in provenance.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72aab3fa-ba3f-48a9-9029-1cec279461d0",
  "uuid": "0331f9fb-d95c-4b67-8b25-e5482abd14e9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018RJUS8k757VEC7wmGsEdKm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 35454,
      "cache_read_input_tokens": 44337,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 35454
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

_source line 36_

<details open><summary>🔧 Tool call — Glob · `toolu_01CpHJhKphCHikQgTrviDKJC`</summary>

```json
{
  "pattern": "docs/paper/sections/*.tex",
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
  "session_id": "72aab3fa-ba3f-48a9-9029-1cec279461d0",
  "uuid": "ea7b6187-fce4-451f-9cdd-05db60adc79e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018RJUS8k757VEC7wmGsEdKm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 35454,
      "cache_read_input_tokens": 44337,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 35454
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

_source line 37 · 2026-05-25T13:48:16.169Z_

<details><summary>↩ Tool result · `toolu_01CpHJhKphCHikQgTrviDKJC`</summary>

```text
docs/paper/sections/related_work.tex
docs/paper/sections/abstract_body.tex
docs/paper/sections/introduction.tex
docs/paper/sections/methodology.tex
docs/paper/sections/results.tex
docs/paper/sections/analysis.tex
docs/paper/sections/conclusion.tex
docs/paper/sections/appendix.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "72aab3fa-ba3f-48a9-9029-1cec279461d0",
  "uuid": "686d593c-f73d-4b5b-8aa3-e7baa922205b",
  "tool_use_result": {
    "filenames": [
      "docs/paper/sections/related_work.tex",
      "docs/paper/sections/abstract_body.tex",
      "docs/paper/sections/introduction.tex",
      "docs/paper/sections/methodology.tex",
      "docs/paper/sections/results.tex",
      "docs/paper/sections/analysis.tex",
      "docs/paper/sections/conclusion.tex",
      "docs/paper/sections/appendix.tex"
    ],
    "durationMs": 17,
    "numFiles": 8,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 38_

<details open><summary>🔧 Tool call — Grep · `toolu_01GTHmottXvkJWJnGDTixUh6`</summary>

```json
{
  "pattern": "AUROC|0\\.961|0\\.957|0\\.990|29/32|27/30|n=32|n=30|n=56",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72aab3fa-ba3f-48a9-9029-1cec279461d0",
  "uuid": "b92bd2b0-1796-47bb-b52b-36455bb88298",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nji8XugdoMGUXGxBm4VKGv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4097,
      "cache_read_input_tokens": 79791,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4097
      },
      "output_tokens": 50,
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

_source line 39 · 2026-05-25T13:48:19.686Z_

<details><summary>↩ Tool result · `toolu_01GTHmottXvkJWJnGDTixUh6`</summary>

```text
docs/paper/sections/analysis.tex:14:Monitor via NVE diagnostic ($\geq 1.5\times$, AUROC${=}0.990$, F1${=}0.941$ at $n{=}56$ across two environments; Table~\ref{tab:nve_loeo}). Freezing the $\dt$-embedding converts CIVO onset (7/7 trained locomotion, NVE $1.53$--$108\times$) to transient spikes that self-correct within 20K steps (2/3 frozen Walker, $1.71$--$1.88\times$; 0/2 frozen Cheetah); untreated, extreme CIVO ($70.6\times$) causes irrecoverable damage (Appendix~\ref{sec:appendix_analysis}).
docs/paper/sections/abstract_body.tex:1:[Omitted long matching line]
docs/paper/sections/conclusion.tex:4:[Omitted long matching line]
docs/paper/sections/conclusion.tex:10:Statistical power is limited (4--5 seeds per configuration) \citep{colas2018seeds}; the NVE threshold (AUROC${=}0.990$, $n{=}56$) may require recalibration for different reward scales.
docs/paper/sections/methodology.tex:38:We define $\nve_t = (v/e)_{\text{config},t} / (v/e)_{\text{baseline},t}$, where $v/e$ is the critic's mean imagined value divided by mean evaluation return, and the baseline is the highest-performing seed (exp\_001, seed~1, 505K steps). We restrict to a \textbf{35K+ window} to avoid early-training inflation. The $\nve \geq 1.5\times$ threshold achieves 53/56 accuracy across two environments ($n{=}56$; AUROC${=}0.990$, F1${=}0.941$; Appendix~\ref{sec:appendix_sensitivity}).
docs/paper/sections/appendix.tex:153:[Omitted long matching line]
docs/paper/sections/appendix.tex:157:\caption{\textbf{Task~B1}: Sustained CIVO detection sensitivity analysis ($n_{\text{pos}}=3$, $n_{\text{neg}}=8$, $n=11$, $\text{AUROC}=0.917$). All confidence intervals are two-sided Clopper-Pearson exact binomial ($\alpha=0.05$). $^\dagger$Optimal threshold in $(3.78, 4.02]$; exp\_059 (NVE${=}4.72\times$, B1-negative) is the sole false positive.}
docs/paper/sections/appendix.tex:179:\caption{\textbf{Task~B2}: Any CIVO detection sensitivity analysis ($n_{\text{pos}}=5$, $n_{\text{neg}}=6$, $n=11$, $\text{AUROC}=0.967$). The single false positive at $\geq 1.5\times$ is 008e\_v3\_s2 (IRD mechanism, not CIVO). The $1.5\times$ threshold (highlighted) maximizes F1 while maintaining perfect recall.}
docs/paper/sections/appendix.tex:200:\caption{\textbf{Task~B2 (full evaluation set)}: Any CIVO detection across two environments ($n_{\text{pos}}=9$, $n_{\text{neg}}=8$, $n=17$, $\text{AUROC}=0.972$). Includes Walker Walk (15 configurations) and Cheetah Run (2 configurations).}
docs/paper/sections/appendix.tex:239:\caption{NVE ROC curve ($n{=}30$ configurations, AUROC${=}0.957$, in-sample, post-hoc). The preset $\nve \geq 1.5\times$ operating point (star) achieves TPR${=}1.00$, FPR${=}0.18$. Three false positives arise from non-CIVO value overestimation: RAVE anchor pollution, obs-decoder SGS side effects, and IRD eval-driven collapse (008e\_v3 seed~2). Threshold calibrated and validated in-sample, post-hoc; cross-architecture validation deferred.}
docs/paper/sections/appendix.tex:248:[Omitted long matching line]
docs/paper/sections/appendix.tex:274:[Omitted long matching line]
docs/paper/sections/appendix.tex:278:[Omitted long matching line]
docs/paper/sections/appendix.tex:294:Held-out & $N_{\text{train}}$ & $N_{\text{test}}$ & $\theta_{\text{opt}}$ range & Test Accuracy & Test AUROC \\
docs/paper/sections/appendix.tex:305:[Omitted long matching line]
docs/paper/sections/introduction.tex:6:[Omitted long matching line]
docs/paper/sections/introduction.tex:11:[Omitted long matching line]
docs/paper/sections/results.tex:74:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "72aab3fa-ba3f-48a9-9029-1cec279461d0",
  "uuid": "27d08424-89bb-4658-b487-e09cef31dad5",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "docs/paper/sections/analysis.tex:14:Monitor via NVE diagnostic ($\\geq 1.5\\times$, AUROC${=}0.990$, F1${=}0.941$ at $n{=}56$ across two environments; Table~\\ref{tab:nve_loeo}). Freezing the $\\dt$-embedding converts CIVO onset (7/7 trained locomotion, NVE $1.53$--$108\\times$) to transient spikes that self-correct within 20K steps (2/3 frozen Walker, $1.71$--$1.88\\times$; 0/2 frozen Cheetah); untreated, extreme CIVO ($70.6\\times$) causes irrecoverable damage (Appendix~\\ref{sec:appendix_analysis}).\ndocs/paper/sections/abstract_body.tex:1:[Omitted long matching line]\ndocs/paper/sections/conclusion.tex:4:[Omitted long matching line]\ndocs/paper/sections/conclusion.tex:10:Statistical power is limited (4--5 seeds per configuration) \\citep{colas2018seeds}; the NVE threshold (AUROC${=}0.990$, $n{=}56$) may require recalibration for different reward scales.\ndocs/paper/sections/methodology.tex:38:We define $\\nve_t = (v/e)_{\\text{config},t} / (v/e)_{\\text{baseline},t}$, where $v/e$ is the critic's mean imagined value divided by mean evaluation return, and the baseline is the highest-performing seed (exp\\_001, seed~1, 505K steps). We restrict to a \\textbf{35K+ window} to avoid early-training inflation. The $\\nve \\geq 1.5\\times$ threshold achieves 53/56 accuracy across two environments ($n{=}56$; AUROC${=}0.990$, F1${=}0.941$; Appendix~\\ref{sec:appendix_sensitivity}).\ndocs/paper/sections/appendix.tex:153:[Omitted long matching line]\ndocs/paper/sections/appendix.tex:157:\\caption{\\textbf{Task~B1}: Sustained CIVO detection sensitivity analysis ($n_{\\text{pos}}=3$, $n_{\\text{neg}}=8$, $n=11$, $\\text{AUROC}=0.917$). All confidence intervals are two-sided Clopper-Pearson exact binomial ($\\alpha=0.05$). $^\\dagger$Optimal threshold in $(3.78, 4.02]$; exp\\_059 (NVE${=}4.72\\times$, B1-negative) is the sole false positive.}\ndocs/paper/sections/appendix.tex:179:\\caption{\\textbf{Task~B2}: Any CIVO detection sensitivity analysis ($n_{\\text{pos}}=5$, $n_{\\text{neg}}=6$, $n=11$, $\\text{AUROC}=0.967$). The single false positive at $\\geq 1.5\\times$ is 008e\\_v3\\_s2 (IRD mechanism, not CIVO). The $1.5\\times$ threshold (highlighted) maximizes F1 while maintaining perfect recall.}\ndocs/paper/sections/appendix.tex:200:\\caption{\\textbf{Task~B2 (full evaluation set)}: Any CIVO detection across two environments ($n_{\\text{pos}}=9$, $n_{\\text{neg}}=8$, $n=17$, $\\text{AUROC}=0.972$). Includes Walker Walk (15 configurations) and Cheetah Run (2 configurations).}\ndocs/paper/sections/appendix.tex:239:\\caption{NVE ROC curve ($n{=}30$ configurations, AUROC${=}0.957$, in-sample, post-hoc). The preset $\\nve \\geq 1.5\\times$ operating point (star) achieves TPR${=}1.00$, FPR${=}0.18$. Three false positives arise from non-CIVO value overestimation: RAVE anchor pollution, obs-decoder SGS side effects, and IRD eval-driven collapse (008e\\_v3 seed~2). Threshold calibrated and validated in-sample, post-hoc; cross-architecture validation deferred.}\ndocs/paper/sections/appendix.tex:248:[Omitted long matching line]\ndocs/paper/sections/appendix.tex:274:[Omitted long matching line]\ndocs/paper/sections/appendix.tex:278:[Omitted long matching line]\ndocs/paper/sections/appendix.tex:294:Held-out & $N_{\\text{train}}$ & $N_{\\text{test}}$ & $\\theta_{\\text{opt}}$ range & Test Accuracy & Test AUROC \\\\\ndocs/paper/sections/appendix.tex:305:[Omitted long matching line]\ndocs/paper/sections/introduction.tex:6:[Omitted long matching line]\ndocs/paper/sections/introduction.tex:11:[Omitted long matching line]\ndocs/paper/sections/results.tex:74:[Omitted long matching line]",
    "numLines": 18
  }
}
```

</details>

---

### Tool call

_source line 40_

<details open><summary>🔧 Tool call — Grep · `toolu_01MRVodJTMH8N7fDcJ35oCha`</summary>

```json
{
  "pattern": "133 experiment|153 experiment|155 experiment|78 success|79 success|63 success",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon",
  "output_mode": "content",
  "-i": true,
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72aab3fa-ba3f-48a9-9029-1cec279461d0",
  "uuid": "a891a16b-a4dc-487e-9502-c2676d0c233d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nji8XugdoMGUXGxBm4VKGv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4097,
      "cache_read_input_tokens": 79791,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4097
      },
      "output_tokens": 50,
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

_source line 41 · 2026-05-25T13:48:21.040Z_

<details><summary>↩ Tool result · `toolu_01MRVodJTMH8N7fDcJ35oCha`</summary>

```text
ROADMAP.md:11:- **实验统计**: 155 个（78 success / 多 negative / 4 running）
artifacts/_project/report/rebuttal_prep.md:37:[Omitted long matching line]
artifacts/_project/report/rebuttal_prep.md:67:[Omitted long matching line]
artifacts/_project/report/rebuttal_prep.md:69:**Evidence**: Aggregate: 133 experiments, 63 success, 35 negative. Per-condition: trained CIVO 2/2 original validation + 3 additional seeds all trigger, frozen 0/5 CIVO (locomotion), removal 5/5 prevention. Fisher p=0.003 for trained-vs-frozen-vs-removed three-way. TCN seed variance (45–91% eval retention at σ=0.2 Walker) reported as instability evidence. Dual-critic 2×2 factorial fully populated.
artifacts/_project/report/rebuttal_prep.md:97:[Omitted long matching line]
artifacts/_project/report/rebuttal_prep.md:99:[Omitted long matching line]
artifacts/_project/report/rebuttal_prep.md:139:[Omitted long matching line]
logs/chats/feishu_group_oc_e03655bc885f99dd8e838011bc2fffbb_reviewer.jsonl:535:[Omitted long matching line]
logs/chats/worker_paper_rebuttal_prep_expansion_20260524T114857.jsonl:79:{"ts": "2026-05-24T11:54:37.393413+00:00", "role": "tool", "session": "worker_paper_rebuttal_prep_expansion_20260524T114857", "text": "called Edit", "tool": "Edit", "tool_args": {"replace_all": "False", "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/rebuttal_prep.md", "old_string": "We report 132 experiments across 62 successful conditions", "new_string": "We report 133 experiments across 63 successful conditions"}}
logs/chats/worker_paper_rebuttal_prep_expansion_20260524T114857.jsonl:81:[Omitted long matching line]
logs/chats/feishu_group_oc_5e879064da2e47dad864c1f891eb37a8_director.jsonl:446:[Omitted long matching line]
logs/chats/feishu_group_oc_5e879064da2e47dad864c1f891eb37a8_director.jsonl:542:[Omitted long matching line]
logs/chats/archive/feishu_group_oc_5e879064da2e47dad864c1f891eb37a8_director_20260525T032314_098072.jsonl:419:[Omitted long matching line]
logs/chats/archive/feishu_group_oc_5e879064da2e47dad864c1f891eb37a8_director_20260525T032314_098072.jsonl:431:[Omitted long matching line]
logs/chats/archive/feishu_group_oc_5e879064da2e47dad864c1f891eb37a8_director_20260525T032314_098072.jsonl:712:[Omitted long matching line]
logs/chats/archive/feishu_group_oc_e03655bc885f99dd8e838011bc2fffbb_reviewer_20260525T032737_513980.jsonl:1057:[Omitted long matching line]
logs/chats/archive/feishu_group_oc_e03655bc885f99dd8e838011bc2fffbb_reviewer_20260525T032737_513980.jsonl:1102:[Omitted long matching line]
logs/chats/cron_hook_exp_074_008a_walker_s3.jsonl:12:[Omitted long matching line]
logs/chats/feishu_group_oc_e03655bc885f99dd8e838011bc2fffbb.jsonl:2306:{"ts": "2026-05-24T07:48:04.290988+00:00", "role": "tool", "session": "feishu:group:oc_e03655bc885f99dd8e838011bc2fffbb", "text": "called Edit", "tool": "Edit", "tool_args": {"replace_all": "False", "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/rebuttal_prep.md", "old_string": "Total: 5 environments, 132 experiments, 62 successful.", "new_string": "Total: 5 environments, 133 experiments, 63 successful."}}
logs/chats/feishu_group_oc_e03655bc885f99dd8e838011bc2fffbb.jsonl:2308:{"ts": "2026-05-24T07:48:05.396231+00:00", "role": "tool", "session": "feishu:group:oc_e03655bc885f99dd8e838011bc2fffbb", "text": "called Edit", "tool": "Edit", "tool_args": {"replace_all": "False", "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/rebuttal_prep.md", "old_string": "Aggregate: 132 experiments, 62 success, 35 negative.", "new_string": "Aggregate: 133 experiments, 63 success, 35 negative."}}
logs/chats/feishu_group_oc_e03655bc885f99dd8e838011bc2fffbb.jsonl:2312:[Omitted long matching line]
logs/chats/feishu_group_oc_e03655bc885f99dd8e838011bc2fffbb.jsonl:2332:[Omitted long matching line]
logs/chats/feishu_group_oc_e03655bc885f99dd8e838011bc2fffbb.jsonl:2513:[Omitted long matching line]
artifacts/rebuttal_prep.md:37:[Omitted long matching line]
artifacts/rebuttal_prep.md:67:[Omitted long matching line]
artifacts/rebuttal_prep.md:69:**Evidence**: Aggregate: 133 experiments, 63 success, 35 negative. Per-condition: trained CIVO 2/2 original validation + 3 additional seeds all trigger, frozen 0/5 CIVO (locomotion), removal 5/5 prevention. Fisher p=0.003 for trained-vs-frozen-vs-removed three-way. TCN seed variance (45–91% eval retention at σ=0.2 Walker) reported as instability evidence. Dual-critic 2×2 factorial fully populated.
artifacts/rebuttal_prep.md:97:[Omitted long matching line]
artifacts/rebuttal_prep.md:99:[Omitted long matching line]
artifacts/rebuttal_prep.md:139:[Omitted long matching line]
logs/workers/worker_paper_rebuttal_prep_expansion_20260524T114857.log:6:[Omitted long matching line]
logs/workers/worker_paper_rebuttal_prep_expansion_20260524T114857.log:116:[Omitted long matching line]
logs/workers/worker_paper_rebuttal_prep_expansion_20260524T114857.log:119:[Omitted long matching line]
logs/workers/worker_paper_rebuttal_prep_expansion_20260524T114857.log:121:[Omitted long matching line]
logs/workers/worker_paper_rebuttal_prep_expansion_20260524T114857.log:123:[Omitted long matching line]
logs/workers/worker_paper_rebuttal_prep_expansion_20260524T114857.log:124:[Omitted long matching line]
logs/workers/worker_paper_rebuttal_prep_expansion_20260524T114857.log:125:[Omitted long matching line]
logs/workers/worker_paper_rebuttal_prep_expansion_20260524T114857.log:127:[Omitted long matching line]
logs/workers/worker_paper_rebuttal_prep_expansion_20260524T114857.log:128:[Omitted long matching line]
logs/workers/worker_audit_roadmap_tasks_20260525T134553.log:9:[Omitted long matching line]
logs/workers/worker_audit_roadmap_tasks_20260525T134553.log:29:[Omitted long matching line]
logs/workers/worker_audit_roadmap_tasks_20260525T134553.log:34:[Omitted long matching line]
logs/workers/worker_audit_roadmap_tasks_20260525T134553.log:40:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "72aab3fa-ba3f-48a9-9029-1cec279461d0",
  "uuid": "7d3228d4-89ee-4046-8b78-cce588308e8a",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "ROADMAP.md:11:- **实验统计**: 155 个（78 success / 多 negative / 4 running）\nartifacts/_project/report/rebuttal_prep.md:37:[Omitted long matching line]\nartifacts/_project/report/rebuttal_prep.md:67:[Omitted long matching line]\nartifacts/_project/report/rebuttal_prep.md:69:**Evidence**: Aggregate: 133 experiments, 63 success, 35 negative. Per-condition: trained CIVO 2/2 original validation + 3 additional seeds all trigger, frozen 0/5 CIVO (locomotion), removal 5/5 prevention. Fisher p=0.003 for trained-vs-frozen-vs-removed three-way. TCN seed variance (45–91% eval retention at σ=0.2 Walker) reported as instability evidence. Dual-critic 2×2 factorial fully populated.\nartifacts/_project/report/rebuttal_prep.md:97:[Omitted long matching line]\nartifacts/_project/report/rebuttal_prep.md:99:[Omitted long matching line]\nartifacts/_project/report/rebuttal_prep.md:139:[Omitted long matching line]\nlogs/chats/feishu_group_oc_e03655bc885f99dd8e838011bc2fffbb_reviewer.jsonl:535:[Omitted long matching line]\nlogs/chats/worker_paper_rebuttal_prep_expansion_20260524T114857.jsonl:79:{\"ts\": \"2026-05-24T11:54:37.393413+00:00\", \"role\": \"tool\", \"session\": \"worker_paper_rebuttal_prep_expansion_20260524T114857\", \"text\": \"called Edit\", \"tool\": \"Edit\", \"tool_args\": {\"replace_all\": \"False\", \"file_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/rebuttal_prep.md\", \"old_string\": \"We report 132 experiments across 62 successful conditions\", \"new_string\": \"We report 133 experiments across 63 successful conditions\"}}\nlogs/chats/worker_paper_rebuttal_prep_expansion_20260524T114857.jsonl:81:[Omitted long matching line]\nlogs/chats/feishu_group_oc_5e879064da2e47dad864c1f891eb37a8_director.jsonl:446:[Omitted long matching line]\nlogs/chats/feishu_group_oc_5e879064da2e47dad864c1f891eb37a8_director.jsonl:542:[Omitted long matching line]\nlogs/chats/archive/feishu_group_oc_5e879064da2e47dad864c1f891eb37a8_director_20260525T032314_098072.jsonl:419:[Omitted long matching line]\nlogs/chats/archive/feishu_group_oc_5e879064da2e47dad864c1f891eb37a8_director_20260525T032314_098072.jsonl:431:[Omitted long matching line]\nlogs/chats/archive/feishu_group_oc_5e879064da2e47dad864c1f891eb37a8_director_20260525T032314_098072.jsonl:712:[Omitted long matching line]\nlogs/chats/archive/feishu_group_oc_e03655bc885f99dd8e838011bc2fffbb_reviewer_20260525T032737_513980.jsonl:1057:[Omitted long matching line]\nlogs/chats/archive/feishu_group_oc_e03655bc885f99dd8e838011bc2fffbb_reviewer_20260525T032737_513980.jsonl:1102:[Omitted long matching line]\nlogs/chats/cron_hook_exp_074_008a_walker_s3.jsonl:12:[Omitted long matching line]\nlogs/chats/feishu_group_oc_e03655bc885f99dd8e838011bc2fffbb.jsonl:2306:{\"ts\": \"2026-05-24T07:48:04.290988+00:00\", \"role\": \"tool\", \"session\": \"feishu:group:oc_e03655bc885f99dd8e838011bc2fffbb\", \"text\": \"called Edit\", \"tool\": \"Edit\", \"tool_args\": {\"replace_all\": \"False\", \"file_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/rebuttal_prep.md\", \"old_string\": \"Total: 5 environments, 132 experiments, 62 successful.\", \"new_string\": \"Total: 5 environments, 133 experiments, 63 successful.\"}}\nlogs/chats/feishu_group_oc_e03655bc885f99dd8e838011bc2fffbb.jsonl:2308:{\"ts\": \"2026-05-24T07:48:05.396231+00:00\", \"role\": \"tool\", \"session\": \"feishu:group:oc_e03655bc885f99dd8e838011bc2fffbb\", \"text\": \"called Edit\", \"tool\": \"Edit\", \"tool_args\": {\"replace_all\": \"False\", \"file_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/rebuttal_prep.md\", \"old_string\": \"Aggregate: 132 experiments, 62 success, 35 negative.\", \"new_string\": \"Aggregate: 133 experiments, 63 success, 35 negative.\"}}\nlogs/chats/feishu_group_oc_e03655bc885f99dd8e838011bc2fffbb.jsonl:2312:[Omitted long matching line]\nlogs/chats/feishu_group_oc_e03655bc885f99dd8e838011bc2fffbb.jsonl:2332:[Omitted long matching line]\nlogs/chats/feishu_group_oc_e03655bc885f99dd8e838011bc2fffbb.jsonl:2513:[Omitted long matching line]\nartifacts/rebuttal_prep.md:37:[Omitted long matching line]\nartifacts/rebuttal_prep.md:67:[Omitted long matching line]\nartifacts/rebuttal_prep.md:69:**Evidence**: Aggregate: 133 experiments, 63 success, 35 negative. Per-condition: trained CIVO 2/2 original validation + 3 additional seeds all trigger, frozen 0/5 CIVO (locomotion), removal 5/5 prevention. Fisher p=0.003 for trained-vs-frozen-vs-removed three-way. TCN seed variance (45–91% eval retention at σ=0.2 Walker) reported as instability evidence. Dual-critic 2×2 factorial fully populated.\nartifacts/rebuttal_prep.md:97:[Omitted long matching line]\nartifacts/rebuttal_prep.md:99:[Omitted long matching line]\nartifacts/rebuttal_prep.md:139:[Omitted long matching line]\nlogs/workers/worker_paper_rebuttal_prep_expansion_20260524T114857.log:6:[Omitted long matching line]\nlogs/workers/worker_paper_rebuttal_prep_expansion_20260524T114857.log:116:[Omitted long matching line]\nlogs/workers/worker_paper_rebuttal_prep_expansion_20260524T114857.log:119:[Omitted long matching line]\nlogs/workers/worker_paper_rebuttal_prep_expansion_20260524T114857.log:121:[Omitted long matching line]\nlogs/workers/worker_paper_rebuttal_prep_expansion_20260524T114857.log:123:[Omitted long matching line]\nlogs/workers/worker_paper_rebuttal_prep_expansion_20260524T114857.log:124:[Omitted long matching line]\nlogs/workers/worker_paper_rebuttal_prep_expansion_20260524T114857.log:125:[Omitted long matching line]\nlogs/workers/worker_paper_rebuttal_prep_expansion_20260524T114857.log:127:[Omitted long matching line]\nlogs/workers/worker_paper_rebuttal_prep_expansion_20260524T114857.log:128:[Omitted long matching line]\nlogs/workers/worker_audit_roadmap_tasks_20260525T134553.log:9:[Omitted long matching line]\nlogs/workers/worker_audit_roadmap_tasks_20260525T134553.log:29:[Omitted long matching line]\nlogs/workers/worker_audit_roadmap_tasks_20260525T134553.log:34:[Omitted long matching line]\nlogs/workers/worker_audit_roadmap_tasks_20260525T134553.log:40:[Omitted long matching line]",
    "numLines": 42
  }
}
```

</details>

---

### Assistant

_source line 42_

<details><summary>Logged reasoning block</summary>

```text
Good. Now I have all the data I need. The paper body has been updated to use n=56 AUROC=0.990. The rebuttal still uses the older numbers (n=30, AUROC=0.957, and "133 experiments, 63 success"). Let me compile the full audit report.

Let me also check what the Cartpole cross-environment results look like since the rebuttal mentions it.

Actually, I have enough to compile the report. Let me proceed.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72aab3fa-ba3f-48a9-9029-1cec279461d0",
  "uuid": "ef916071-ada0-43cb-86db-135db0ea638f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nm2j3DQbjDYTrbHZ7DwQ2p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3947,
      "cache_read_input_tokens": 83888,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3947
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

_source line 43_

I have all the data needed. Here's the audit:

## ROADMAP 任务审计

### ROADMAP 状态本身已过时
ROADMAP 列出 exp_074/077/078/079 为运行中，但实际：
- exp_074 (008a Walker s3): **已完成** (success, eval 855.9)
- exp_079 (frozen dt_emb Walker s0): **已完成** (killed)
- exp_080/081 (008e_v3 Walker s1/s2): **运行中但未列入 ROADMAP**
- exp_077/078 (Cheetah baseline/008d): 仍运行中

ROADMAP 实验统计写 "155 个（78 success）"，report.md 写 "成功 79 / 共 153"，两者不一致。

---

### 可立即执行的任务

1. **ROADMAP 自身更新** — 将 exp_074/079 从 "运行中" 移除，加入 exp_080/081，统一实验计数
2. **exp_074 结果纳入论文** — 008a 现在有 4 seeds (mean eval 791, std 102.2, all civo_alert=0)。appendix Table complete_results 缺 008a_s3 行，需添加：`008a\_s3 & Unexposed emb & exp$^a$ & OFF & 15 & 855.9 @105K & --- & Healthy`
3. **exp_072 (008e_v3 s5) 纳入 appendix** — 008e_v3 现有 s1-s4 在 appendix 中，s5 (eval 853.1, NVE 0.61, healthy) 缺失
4. **008f 额外 seeds 纳入 appendix** — exp_071 (s3, eval 311.9) 和 exp_073 (s4, eval 289.3) 未在 appendix 表中
5. **plan_034 标记完成** — ROADMAP "完成后下一批" 仍列 plan_034 NVE threshold 分析，但 appendix 已包含完整 n=56 AUROC=0.990 分析，provenance 也引用了 plan_034 结果。应从待办移除
6. **Rebuttal Q&A 实验计数更新**（见下方详细列表）

### Blocked 任务（依赖在跑实验）

1. **plan_022 Cheetah causal control (dt_embed_dim=0)** — 依赖 exp_078 (Cheetah 008d) 确认 CIVO
2. **exp_077/078 完成后分析 + 更新论文** — 依赖 exp_077/078 完成
3. **exp_080/081 完成后更新 008e_v3 multi-seed 统计** — 依赖 exp_080 (s1)/081 (s2) 完成，完成后 008e_v3 将有 6+ seeds
4. **等待 Round 5 审稿结果** — 外部依赖
5. **Round 5 反馈 → 修正 → 数据锁定 (5/27)** — 依赖 Round 5
6. **ICML 投稿 (5/29)** — 依赖一切完成

---

### Rebuttal Q&A 更新需求

**Q4** (环境数量): 引用 "133 experiments across 43 configurations" → 应更新为当前计数 (~153 experiments)

**Q6** (NVE threshold): 引用 "In-sample AUROC 0.957 (n=30)" 和 "LOEO mean AUROC 0.988" → 论文正文已更新到 n=56 AUROC=0.990 F1=0.941。Rebuttal 应同步，或至少在 response 中引用最新数字

**Q7** (样本量): 引用 "133 experiments across 63 successful conditions" → 应更新为 ~153/79

**Q10** (环境多样性): 同 Q4，引用 "133 experiments" → 过时

**Q14** (Seed count 统计可靠性): 引用 "133 experiments, 63 success, 35 negative" → 过时。另外 "Fisher exact p=0.003: trained 7/7 onset" — 如果 Cheetah exp_078 确认 CIVO 则更新为 8/8 或更多

**Q15** (NVE threshold 敏感度): 引用 "In-sample AUROC=0.957, accuracy 27/30" → 论文已用 n=56 AUROC=0.990 53/56。Rebuttal 同步

**Q1** (Frozen diagnostic): 引用 "2/2 original validation + 3 additional seeds s3-s5" — exp_068 (008d repro s1) 现在提供第 6 个 trained seed 数据 (NVE 4.12, collapse)。可考虑补充

---

### Appendix 缺失

以下已完成实验 (conclusion=success) 不在 appendix Table complete_results 中：

| 缺失实验 | 配置 | 关键指标 |
|----------|------|---------|
| exp_074 (008a_s3) | Unexposed emb s3 | eval 855.9, no CIVO |
| exp_072 (008e_v3_s5) | Mitigation s5 | eval 853.1, NVE 0.61, healthy |
| exp_071 (008f_s3) | No dt_emb s3 | eval 311.9, NVE 0.4, healthy |
| exp_073 (008f_s4) | No dt_emb s4 | eval 289.3, NVE 0.76, healthy |
| exp_068 (008d repro s1) | Trained s1 repro | eval 39.1, NVE 4.12, collapse |
| exp_067 (frozen plan015) | Frozen s0 dedicated | eval 281.5, NVE 0.19, healthy |
| Cartpole exps (060-062) | 跨环境验证 | 未在 appendix 中出现 |

注：exp_066/066b (RSSM fidelity timeseries)、exp_064 (value distribution)、exp_065 (cosine) 是分析实验，内容已在 appendix 正文引用，无需加入训练结果表。

---

### 数据一致性问题

1. **实验总数不一致**：ROADMAP 写 155/78 success，report 写 153/79 success，rebuttal 写 133/63 success → 三处数字互不相同，需统一

2. **NVE 指标版本分歧**：
   - 论文正文 (methodology/analysis/conclusion)：n=56, AUROC=0.990, F1=0.941 ✓
   - Appendix §ROC figure caption：n=30, AUROC=0.957（ROC 图本身）
   - Appendix §Comprehensive validation 段落：n=56, AUROC=0.990 ✓
   - Provenance C047-C053：n=32, AUROC=0.961 ← **过时**，与论文正文 (0.990) 和 appendix (0.957/0.990) 均不一致
   - Rebuttal：n=30, AUROC=0.957 ← **过时**

3. **Provenance C004/C011/C018/C042**：仍引用旧的 "7/8 classification (n=8)" 和 "AUROC=0.933"。论文正文和 appendix 已更新到更大样本量，但这些 provenance 条目未同步

4. **Appendix cross-domain table (Tab cross_domain)**：Walker trained 列 "5/5"，但现在有 exp_068 (s1 repro) 和 exp_059 (s5) 等额外 seeds。如果论文声称 "7/7 onset"（rebuttal Q8/Q14），appendix 表格应反映完整 seed count

5. **008a seed count**：appendix 仅列 3 seeds (008a, 008a_s1, 008a_s2)。exp_074 完成后应为 4 seeds。provenance C023 引用 008a eval=777.7 只是 s0 数据，4-seed summary (mean 791, std 102.2) 可加强 C3 claim

---

### 优先级建议

**数据锁定 5/27 前必须完成（不依赖在跑实验）：**
1. 统一实验计数（ROADMAP/report/rebuttal 三处对齐）
2. Appendix table 补充 exp_074/072/071/073/068/067 行
3. Rebuttal Q&A 实验计数和 NVE 数字更新到最新
4. Provenance C047-C053 从 n=32/AUROC=0.961 更新到 n=56/AUROC=0.990
5. ROADMAP 更新运行状态

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "72aab3fa-ba3f-48a9-9029-1cec279461d0",
  "uuid": "9e20877c-70bd-4aca-ae99-2cab050f21a9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nm2j3DQbjDYTrbHZ7DwQ2p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3947,
      "cache_read_input_tokens": 83888,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3947
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

### Task result

_source line 44_

I have all the data needed. Here's the audit:

## ROADMAP 任务审计

### ROADMAP 状态本身已过时
ROADMAP 列出 exp_074/077/078/079 为运行中，但实际：
- exp_074 (008a Walker s3): **已完成** (success, eval 855.9)
- exp_079 (frozen dt_emb Walker s0): **已完成** (killed)
- exp_080/081 (008e_v3 Walker s1/s2): **运行中但未列入 ROADMAP**
- exp_077/078 (Cheetah baseline/008d): 仍运行中

ROADMAP 实验统计写 "155 个（78 success）"，report.md 写 "成功 79 / 共 153"，两者不一致。

---

### 可立即执行的任务

1. **ROADMAP 自身更新** — 将 exp_074/079 从 "运行中" 移除，加入 exp_080/081，统一实验计数
2. **exp_074 结果纳入论文** — 008a 现在有 4 seeds (mean eval 791, std 102.2, all civo_alert=0)。appendix Table complete_results 缺 008a_s3 行，需添加：`008a\_s3 & Unexposed emb & exp$^a$ & OFF & 15 & 855.9 @105K & --- & Healthy`
3. **exp_072 (008e_v3 s5) 纳入 appendix** — 008e_v3 现有 s1-s4 在 appendix 中，s5 (eval 853.1, NVE 0.61, healthy) 缺失
4. **008f 额外 seeds 纳入 appendix** — exp_071 (s3, eval 311.9) 和 exp_073 (s4, eval 289.3) 未在 appendix 表中
5. **plan_034 标记完成** — ROADMAP "完成后下一批" 仍列 plan_034 NVE threshold 分析，但 appendix 已包含完整 n=56 AUROC=0.990 分析，provenance 也引用了 plan_034 结果。应从待办移除
6. **Rebuttal Q&A 实验计数更新**（见下方详细列表）

### Blocked 任务（依赖在跑实验）

1. **plan_022 Cheetah causal control (dt_embed_dim=0)** — 依赖 exp_078 (Cheetah 008d) 确认 CIVO
2. **exp_077/078 完成后分析 + 更新论文** — 依赖 exp_077/078 完成
3. **exp_080/081 完成后更新 008e_v3 multi-seed 统计** — 依赖 exp_080 (s1)/081 (s2) 完成，完成后 008e_v3 将有 6+ seeds
4. **等待 Round 5 审稿结果** — 外部依赖
5. **Round 5 反馈 → 修正 → 数据锁定 (5/27)** — 依赖 Round 5
6. **ICML 投稿 (5/29)** — 依赖一切完成

---

### Rebuttal Q&A 更新需求

**Q4** (环境数量): 引用 "133 experiments across 43 configurations" → 应更新为当前计数 (~153 experiments)

**Q6** (NVE threshold): 引用 "In-sample AUROC 0.957 (n=30)" 和 "LOEO mean AUROC 0.988" → 论文正文已更新到 n=56 AUROC=0.990 F1=0.941。Rebuttal 应同步，或至少在 response 中引用最新数字

**Q7** (样本量): 引用 "133 experiments across 63 successful conditions" → 应更新为 ~153/79

**Q10** (环境多样性): 同 Q4，引用 "133 experiments" → 过时

**Q14** (Seed count 统计可靠性): 引用 "133 experiments, 63 success, 35 negative" → 过时。另外 "Fisher exact p=0.003: trained 7/7 onset" — 如果 Cheetah exp_078 确认 CIVO 则更新为 8/8 或更多

**Q15** (NVE threshold 敏感度): 引用 "In-sample AUROC=0.957, accuracy 27/30" → 论文已用 n=56 AUROC=0.990 53/56。Rebuttal 同步

**Q1** (Frozen diagnostic): 引用 "2/2 original validation + 3 additional seeds s3-s5" — exp_068 (008d repro s1) 现在提供第 6 个 trained seed 数据 (NVE 4.12, collapse)。可考虑补充

---

### Appendix 缺失

以下已完成实验 (conclusion=success) 不在 appendix Table complete_results 中：

| 缺失实验 | 配置 | 关键指标 |
|----------|------|---------|
| exp_074 (008a_s3) | Unexposed emb s3 | eval 855.9, no CIVO |
| exp_072 (008e_v3_s5) | Mitigation s5 | eval 853.1, NVE 0.61, healthy |
| exp_071 (008f_s3) | No dt_emb s3 | eval 311.9, NVE 0.4, healthy |
| exp_073 (008f_s4) | No dt_emb s4 | eval 289.3, NVE 0.76, healthy |
| exp_068 (008d repro s1) | Trained s1 repro | eval 39.1, NVE 4.12, collapse |
| exp_067 (frozen plan015) | Frozen s0 dedicated | eval 281.5, NVE 0.19, healthy |
| Cartpole exps (060-062) | 跨环境验证 | 未在 appendix 中出现 |

注：exp_066/066b (RSSM fidelity timeseries)、exp_064 (value distribution)、exp_065 (cosine) 是分析实验，内容已在 appendix 正文引用，无需加入训练结果表。

---

### 数据一致性问题

1. **实验总数不一致**：ROADMAP 写 155/78 success，report 写 153/79 success，rebuttal 写 133/63 success → 三处数字互不相同，需统一

2. **NVE 指标版本分歧**：
   - 论文正文 (methodology/analysis/conclusion)：n=56, AUROC=0.990, F1=0.941 ✓
   - Appendix §ROC figure caption：n=30, AUROC=0.957（ROC 图本身）
   - Appendix §Comprehensive validation 段落：n=56, AUROC=0.990 ✓
   - Provenance C047-C053：n=32, AUROC=0.961 ← **过时**，与论文正文 (0.990) 和 appendix (0.957/0.990) 均不一致
   - Rebuttal：n=30, AUROC=0.957 ← **过时**

3. **Provenance C004/C011/C018/C042**：仍引用旧的 "7/8 classification (n=8)" 和 "AUROC=0.933"。论文正文和 appendix 已更新到更大样本量，但这些 provenance 条目未同步

4. **Appendix cross-domain table (Tab cross_domain)**：Walker trained 列 "5/5"，但现在有 exp_068 (s1 repro) 和 exp_059 (s5) 等额外 seeds。如果论文声称 "7/7 onset"（rebuttal Q8/Q14），appendix 表格应反映完整 seed count

5. **008a seed count**：appendix 仅列 3 seeds (008a, 008a_s1, 008a_s2)。exp_074 完成后应为 4 seeds。provenance C023 引用 008a eval=777.7 只是 s0 数据，4-seed summary (mean 791, std 102.2) 可加强 C3 claim

---

### 优先级建议

**数据锁定 5/27 前必须完成（不依赖在跑实验）：**
1. 统一实验计数（ROADMAP/report/rebuttal 三处对齐）
2. Appendix table 补充 exp_074/072/071/073/068/067 行
3. Rebuttal Q&A 实验计数和 NVE 数字更新到最新
4. Provenance C047-C053 从 n=32/AUROC=0.961 更新到 n=56/AUROC=0.990
5. ROADMAP 更新运行状态

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 203373,
  "duration_api_ms": 202701,
  "num_turns": 16,
  "stop_reason": "end_turn",
  "session_id": "72aab3fa-ba3f-48a9-9029-1cec279461d0",
  "total_cost_usd": 0.838287,
  "usage": {
    "input_tokens": 10,
    "cache_creation_input_tokens": 75994,
    "cache_read_input_tokens": 300651,
    "output_tokens": 8444,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 75994,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 2637,
        "cache_read_input_tokens": 83888,
        "cache_creation_input_tokens": 3947,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 3947
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1749,
      "outputTokens": 20,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001849,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 10,
      "outputTokens": 8444,
      "cacheReadInputTokens": 300651,
      "cacheCreationInputTokens": 75994,
      "webSearchRequests": 0,
      "costUSD": 0.836438,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "f9ab8ac7-8b77-449e-b25f-3f9b0fd330ba"
}
```

</details>

---
