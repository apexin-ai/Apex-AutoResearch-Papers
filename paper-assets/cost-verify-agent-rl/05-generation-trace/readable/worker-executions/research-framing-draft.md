# research framing draft

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 25
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/workers/worker_research_framing_draft_20260515T184252.log`
- **Structured JSON:** [`24920c922ee57582d86c.json`](../../sessions/24/24920c922ee57582d86c.json)

## Before a recorded user message

25 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "session_id": "12f481e3-4249-4909-b494-860766cbf5b8",
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
    "mcp__agent-ml-research__register_artifact",
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
  "uuid": "0a3f867f-d11a-4b1d-bb27-22d7ce72bcd7",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-6/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-1-projects-cost-verify-agent-rl/memory/"
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
    "resetsAt": 1778888400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "d204828c-530a-455d-9059-342628987a57",
  "session_id": "12f481e3-4249-4909-b494-860766cbf5b8"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading all the required background materials before writing the framing draft.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "12f481e3-4249-4909-b494-860766cbf5b8",
  "uuid": "fa76b64f-67aa-446e-9754-209d581f3a85",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NtBSeV1GvSXw9x8kvwSkEC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12391,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12391
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

_source line 5_

先读取所有前置材料。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "12f481e3-4249-4909-b494-860766cbf5b8",
  "uuid": "e2d6cff0-b2a6-41f3-99c4-dfd827a90e74",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NtBSeV1GvSXw9x8kvwSkEC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12391,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12391
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

_source line 6_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01JNRVAxAMGLgPMa2YbdobLe`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
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
  "session_id": "12f481e3-4249-4909-b494-860766cbf5b8",
  "uuid": "acb6d14c-58be-4f31-913f-4a0eea0875c3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NtBSeV1GvSXw9x8kvwSkEC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12391,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12391
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

_source line 7 · 2026-05-15T18:43:05.970Z_

<details><summary>↩ Tool result · `toolu_01JNRVAxAMGLgPMa2YbdobLe`</summary>

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
  "session_id": "12f481e3-4249-4909-b494-860766cbf5b8",
  "uuid": "dd571cdc-e275-4267-b17f-4dae7750e007",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
    "total_deferred_tools": 23
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_013manAjZ5z3Lm9co2i5uGLG`</summary>

```json
{
  "project": "cost-verify-agent-rl",
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
  "session_id": "12f481e3-4249-4909-b494-860766cbf5b8",
  "uuid": "bc22d509-86a1-4dc7-9d70-52991dd8256f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RutUDz7KQNrG6PEc8QiGan",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1355,
      "cache_read_input_tokens": 24232,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1355
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

_source line 9 · 2026-05-15T18:43:08.964Z_

<details><summary>↩ Tool result · `toolu_013manAjZ5z3Lm9co2i5uGLG`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/ROADMAP.md\", \"content\": \"# cost-verify-agent-rl — Research Dashboard\\n\\n> 最后更新: 2026-05-15 16:58 UTC | 更新原因: 文献调研完成，竞争格局分析，framing 方向锁定 (D039)\\n\\n> 最后更新: 2026-05-15 | 更新原因: 文献调研完成，竞争格局分析，framing 方向锁定 (D039)\\n\\n## 核心方向\\nB-IAVR: 训练 interactive agent 选择性自我验证，基于行为改变信号（action change）作为 verification informativeness 的 reward。基于 Self-Guide (arXiv 2604.03098) 框架，Qwen3-1.7B + ALFWorld + verl-agent GRPO。\\n\\n**论文 framing（D039）**：cost-efficiency story，不走 performance story。ALFWorld SOTA 88-93%，Self-Guide 1.7B 72.7%，performance 竞争无意义。核心 claim：\\\"RL-trained selective verification 在接近 baseline 性能的前提下显著减少 verification 开销\\\"。与 ARES (2603.07915) 差异化：binary decision + action-change reward + interactive agent 场景。\\n\\n## 当前阶段\\n🧪 **MVP 验证 — Phase A: Always-On Self-Guidance baseline**\\n目标：ALFWorld success ≥ 20%（GRPO 训练后）\\n\\n### exp027_stable_grpo（正在训练）\\n- 针对 exp026 死亡螺旋：128 rollouts + entropy 0.01 + LR 5e-7 + KL 0.005\\n- PID 789790, tmux: exp027_stable_grpo, cuda:0+cuda:1, W&B y7jiibqk\\n- save_freq=5, 50 steps, 预估 42-58h wall time\\n- Step 5 val 预计 ~4-5h 后出结果\\n\\n### MVP 判定（D037）\\n- < 20%: fail → 决策申请新服务器 / 重评项目\\n- 20-25%: weak pass（≈SFT baseline，需更多证据）\\n- 30%+: strong pass → complete_mvp() → Phase B\\n\\n### SFT 基线（C003 compliant 16-episode eval）\\n- exp021: success=6.25%, action_is_valid=68.75%\\n\\n## 竞争格局（文献调研 2026-05-15）\\n| 竞争者 | 方法 | ALFWorld | 与我们的关系 |\\n|--------|------|----------|-------------|\\n| ReflAct (EMNLP'25) | Prompting GPT-4 | 93.3% | 不同赛道（大模型 prompting） |\\n| AgentPRM (ACM Web'26) | 3B trained PRM | 88-91% | 不同方向（process reward） |\\n| Self-Guide (2026) | Always-on verification | 72.7% (1.7B) | 直接基础框架，我们做 selective |\\n| ARES (2603.07915) | SFT router, continuous effort | 52.7% token↓ | 最近竞争者，需实验对比 |\\n| Thinkless (NeurIPS'25) | RL-trained control token | reasoning | 方法论最相近，不同场景 |\\n\\n**核心 novelty**：三条线交汇处——首个用 RL 训练 interactive agent 的 selective verification policy，action-change 作为 verification informativeness reward。\\n\\n## 空窗期产出（exp027 等待期）\\n- ✅ failure_taxonomy.md — 51 实验失败模式分类（4 类 + 5 个跨实验 pattern）\\n- ✅ related_work_survey.md — 21 篇文献 3 条线 + gap 分析 + novelty 定位\\n- ✅ Reviewer claim 强度评估 — 当前零 A 类 claim，exp027 仅证基础设施可行\\n- ✅ D039 framing 方向决策\\n\\n## 近期任务\\n- [ ] exp027 前 5 步 KL 监控（KL < 0.005 → 立即汇报）\\n- [ ] exp027 结果判定 → success ≥20% 则 complete_mvp()\\n- [ ] 如 exp027 pass → 启动 Phase B (B-IAVR) + 评估 GPU 需求（预估 600+ GPU-h）\\n- [ ] 如 exp027 fail → 24h deadline 后决策\\n- [ ] 引用真实性抽查（ARES/CorrectBench/AutoThink 等 arXiv ID 验证）\\n\\n## GPU 预算\\n- 分配：bjb1-17606 cuda:0,1（2× RTX PRO 6000 Blackwell 98GB）\\n- 当前：exp027 训练中，双卡满载\\n- 累计使用：~40 GPU-h\\n- exp027 预估：~84 GPU-h（2卡 × 42h）\\n- Post-MVP 预估（Reviewer 评估）：600-2000 GPU-h（B-IAVR ablations + multi-seed + 对比实验）\\n\\n## 关键风险\\n1. **exp027 训练稳定性**：128 rollouts 能否解决零奖励死亡螺旋？\\n2. **baseline 性能 gap**：cost-efficiency story 前提是 baseline ≥50%，当前 6.25%\\n3. **ARES 竞争**：需实验对比差异化\\n4. **GPU 预算缺口**：post-MVP 需 600+ GPU-h，当前仅 2 卡\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D040 | 2026-05-15 | 修正 exp027 step 3 判定框架为三层阈值，Plan B kl_coef 上调至 0.01 | exp027_stable_grpo, exp026_step_independent_grpo |\\n| D039 | 2026-05-15 | 论文 framing 方向锁定：cost-efficiency story，不走 performan | exp027_stable_grpo, exp026_step_independent_grpo, exp021_ragen_sft_v4 |\\n| D038 | 2026-05-15 | Reviewer 评估 exp027 pass/fail 论文可行性：修正 claim 强度阈值，确 | exp027_stable_grpo, exp026_step_independent_grpo, exp021_ragen_sft_v4, exp019b_expert_sft_v3 |\\n| D037 | 2026-05-15 | exp027 val 判定阈值：<20% fail、20-25% weak (=SFT)、30%+  | exp027_stable_grpo, exp026_step_independent_grpo, exp019b_expert_sft_v3 |\\n| D036 | 2026-05-15 | Reviewer critical 确认 exp026 GRPO 死亡螺旋：step 4 succe | exp026_step_independent_grpo, exp027_stable_grpo |\\n| D035 | 2026-05-15 | exp026 训练不稳定（step 2 峰值 32.81% → step 4 归零），准备 exp0 | exp026_step_independent_grpo |\\n| D034 | 2026-05-15 | 建立两级阈值：MVP=20% val（训练可行性 checkpoint），论文 baseline 最 | exp026_step_independent_grpo |\\n| D033 | 2026-05-15 | exp026 registry 误判修复：cron 因 WANDB_MODE=disabled +  | exp026_step_independent_grpo |\\n| D032 | 2026-05-15 | exp026 前 2 步训练指标强正向（success 6.25%→32.81%，entropy 未 | exp026_step_independent_grpo |\\n| D031 | 2026-05-15 | B-IAVR 代码审查通过（Reviewer info），Phase B 前必须解决两个 warni | exp026_step_independent_grpo |\\n\\n\", \"total_chars\": 4088, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "12f481e3-4249-4909-b494-860766cbf5b8",
  "uuid": "c00c42fe-f532-4eeb-b9fd-b22adcf5d3f3",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/ROADMAP.md\\\", \\\"content\\\": \\\"# cost-verify-agent-rl — Research Dashboard\\\\n\\\\n> 最后更新: 2026-05-15 16:58 UTC | 更新原因: 文献调研完成，竞争格局分析，framing 方向锁定 (D039)\\\\n\\\\n> 最后更新: 2026-05-15 | 更新原因: 文献调研完成，竞争格局分析，framing 方向锁定 (D039)\\\\n\\\\n## 核心方向\\\\nB-IAVR: 训练 interactive agent 选择性自我验证，基于行为改变信号（action change）作为 verification informativeness 的 reward。基于 Self-Guide (arXiv 2604.03098) 框架，Qwen3-1.7B + ALFWorld + verl-agent GRPO。\\\\n\\\\n**论文 framing（D039）**：cost-efficiency story，不走 performance story。ALFWorld SOTA 88-93%，Self-Guide 1.7B 72.7%，performance 竞争无意义。核心 claim：\\\\\\\"RL-trained selective verification 在接近 baseline 性能的前提下显著减少 verification 开销\\\\\\\"。与 ARES (2603.07915) 差异化：binary decision + action-change reward + interactive agent 场景。\\\\n\\\\n## 当前阶段\\\\n🧪 **MVP 验证 — Phase A: Always-On Self-Guidance baseline**\\\\n目标：ALFWorld success ≥ 20%（GRPO 训练后）\\\\n\\\\n### exp027_stable_grpo（正在训练）\\\\n- 针对 exp026 死亡螺旋：128 rollouts + entropy 0.01 + LR 5e-7 + KL 0.005\\\\n- PID 789790, tmux: exp027_stable_grpo, cuda:0+cuda:1, W&B y7jiibqk\\\\n- save_freq=5, 50 steps, 预估 42-58h wall time\\\\n- Step 5 val 预计 ~4-5h 后出结果\\\\n\\\\n### MVP 判定（D037）\\\\n- < 20%: fail → 决策申请新服务器 / 重评项目\\\\n- 20-25%: weak pass（≈SFT baseline，需更多证据）\\\\n- 30%+: strong pass → complete_mvp() → Phase B\\\\n\\\\n### SFT 基线（C003 compliant 16-episode eval）\\\\n- exp021: success=6.25%, action_is_valid=68.75%\\\\n\\\\n## 竞争格局（文献调研 2026-05-15）\\\\n| 竞争者 | 方法 | ALFWorld | 与我们的关系 |\\\\n|--------|------|----------|-------------|\\\\n| ReflAct (EMNLP'25) | Prompting GPT-4 | 93.3% | 不同赛道（大模型 prompting） |\\\\n| AgentPRM (ACM Web'26) | 3B trained PRM | 88-91% | 不同方向（process reward） |\\\\n| Self-Guide (2026) | Always-on verification | 72.7% (1.7B) | 直接基础框架，我们做 selective |\\\\n| ARES (2603.07915) | SFT router, continuous effort | 52.7% token↓ | 最近竞争者，需实验对比 |\\\\n| Thinkless (NeurIPS'25) | RL-trained control token | reasoning | 方法论最相近，不同场景 |\\\\n\\\\n**核心 novelty**：三条线交汇处——首个用 RL 训练 interactive agent 的 selective verification policy，action-change 作为 verification informativeness reward。\\\\n\\\\n## 空窗期产出（exp027 等待期）\\\\n- ✅ failure_taxonomy.md — 51 实验失败模式分类（4 类 + 5 个跨实验 pattern）\\\\n- ✅ related_work_survey.md — 21 篇文献 3 条线 + gap 分析 + novelty 定位\\\\n- ✅ Reviewer claim 强度评估 — 当前零 A 类 claim，exp027 仅证基础设施可行\\\\n- ✅ D039 framing 方向决策\\\\n\\\\n## 近期任务\\\\n- [ ] exp027 前 5 步 KL 监控（KL < 0.005 → 立即汇报）\\\\n- [ ] exp027 结果判定 → success ≥20% 则 complete_mvp()\\\\n- [ ] 如 exp027 pass → 启动 Phase B (B-IAVR) + 评估 GPU 需求（预估 600+ GPU-h）\\\\n- [ ] 如 exp027 fail → 24h deadline 后决策\\\\n- [ ] 引用真实性抽查（ARES/CorrectBench/AutoThink 等 arXiv ID 验证）\\\\n\\\\n## GPU 预算\\\\n- 分配：bjb1-17606 cuda:0,1（2× RTX PRO 6000 Blackwell 98GB）\\\\n- 当前：exp027 训练中，双卡满载\\\\n- 累计使用：~40 GPU-h\\\\n- exp027 预估：~84 GPU-h（2卡 × 42h）\\\\n- Post-MVP 预估（Reviewer 评估）：600-2000 GPU-h（B-IAVR ablations + multi-seed + 对比实验）\\\\n\\\\n## 关键风险\\\\n1. **exp027 训练稳定性**：128 rollouts 能否解决零奖励死亡螺旋？\\\\n2. **baseline 性能 gap**：cost-efficiency story 前提是 baseline ≥50%，当前 6.25%\\\\n3. **ARES 竞争**：需实验对比差异化\\\\n4. **GPU 预算缺口**：post-MVP 需 600+ GPU-h，当前仅 2 卡\\\\n\\\\n## 关键决策日志\\\\n\\\\n| ID | 日期 | 摘要 | 关联实验 |\\\\n|----|------|------|----------|\\\\n| D040 | 2026-05-15 | 修正 exp027 step 3 判定框架为三层阈值，Plan B kl_coef 上调至 0.01 | exp027_stable_grpo, exp026_step_independent_grpo |\\\\n| D039 | 2026-05-15 | 论文 framing 方向锁定：cost-efficiency story，不走 performan | exp027_stable_grpo, exp026_step_independent_grpo, exp021_ragen_sft_v4 |\\\\n| D038 | 2026-05-15 | Reviewer 评估 exp027 pass/fail 论文可行性：修正 claim 强度阈值，确 | exp027_stable_grpo, exp026_step_independent_grpo, exp021_ragen_sft_v4, exp019b_expert_sft_v3 |\\\\n| D037 | 2026-05-15 | exp027 val 判定阈值：<20% fail、20-25% weak (=SFT)、30%+  | exp027_stable_grpo, exp026_step_independent_grpo, exp019b_expert_sft_v3 |\\\\n| D036 | 2026-05-15 | Reviewer critical 确认 exp026 GRPO 死亡螺旋：step 4 succe | exp026_step_independent_grpo, exp027_stable_grpo |\\\\n| D035 | 2026-05-15 | exp026 训练不稳定（step 2 峰值 32.81% → step 4 归零），准备 exp0 | exp026_step_independent_grpo |\\\\n| D034 | 2026-05-15 | 建立两级阈值：MVP=20% val（训练可行性 checkpoint），论文 baseline 最 | exp026_step_independent_grpo |\\\\n| D033 | 2026-05-15 | exp026 registry 误判修复：cron 因 WANDB_MODE=disabled +  | exp026_step_independent_grpo |\\\\n| D032 | 2026-05-15 | exp026 前 2 步训练指标强正向（success 6.25%→32.81%，entropy 未 | exp026_step_independent_grpo |\\\\n| D031 | 2026-05-15 | B-IAVR 代码审查通过（Reviewer info），Phase B 前必须解决两个 warni | exp026_step_independent_grpo |\\\\n\\\\n\\\", \\\"total_chars\\\": 4088, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/ROADMAP.md\", \"content\": \"# cost-verify-agent-rl — Research Dashboard\\n\\n> 最后更新: 2026-05-15 16:58 UTC | 更新原因: 文献调研完成，竞争格局分析，framing 方向锁定 (D039)\\n\\n> 最后更新: 2026-05-15 | 更新原因: 文献调研完成，竞争格局分析，framing 方向锁定 (D039)\\n\\n## 核心方向\\nB-IAVR: 训练 interactive agent 选择性自我验证，基于行为改变信号（action change）作为 verification informativeness 的 reward。基于 Self-Guide (arXiv 2604.03098) 框架，Qwen3-1.7B + ALFWorld + verl-agent GRPO。\\n\\n**论文 framing（D039）**：cost-efficiency story，不走 performance story。ALFWorld SOTA 88-93%，Self-Guide 1.7B 72.7%，performance 竞争无意义。核心 claim：\\\"RL-trained selective verification 在接近 baseline 性能的前提下显著减少 verification 开销\\\"。与 ARES (2603.07915) 差异化：binary decision + action-change reward + interactive agent 场景。\\n\\n## 当前阶段\\n🧪 **MVP 验证 — Phase A: Always-On Self-Guidance baseline**\\n目标：ALFWorld success ≥ 20%（GRPO 训练后）\\n\\n### exp027_stable_grpo（正在训练）\\n- 针对 exp026 死亡螺旋：128 rollouts + entropy 0.01 + LR 5e-7 + KL 0.005\\n- PID 789790, tmux: exp027_stable_grpo, cuda:0+cuda:1, W&B y7jiibqk\\n- save_freq=5, 50 steps, 预估 42-58h wall time\\n- Step 5 val 预计 ~4-5h 后出结果\\n\\n### MVP 判定（D037）\\n- < 20%: fail → 决策申请新服务器 / 重评项目\\n- 20-25%: weak pass（≈SFT baseline，需更多证据）\\n- 30%+: strong pass → complete_mvp() → Phase B\\n\\n### SFT 基线（C003 compliant 16-episode eval）\\n- exp021: success=6.25%, action_is_valid=68.75%\\n\\n## 竞争格局（文献调研 2026-05-15）\\n| 竞争者 | 方法 | ALFWorld | 与我们的关系 |\\n|--------|------|----------|-------------|\\n| ReflAct (EMNLP'25) | Prompting GPT-4 | 93.3% | 不同赛道（大模型 prompting） |\\n| AgentPRM (ACM Web'26) | 3B trained PRM | 88-91% | 不同方向（process reward） |\\n| Self-Guide (2026) | Always-on verification | 72.7% (1.7B) | 直接基础框架，我们做 selective |\\n| ARES (2603.07915) | SFT router, continuous effort | 52.7% token↓ | 最近竞争者，需实验对比 |\\n| Thinkless (NeurIPS'25) | RL-trained control token | reasoning | 方法论最相近，不同场景 |\\n\\n**核心 novelty**：三条线交汇处——首个用 RL 训练 interactive agent 的 selective verification policy，action-change 作为 verification informativeness reward。\\n\\n## 空窗期产出（exp027 等待期）\\n- ✅ failure_taxonomy.md — 51 实验失败模式分类（4 类 + 5 个跨实验 pattern）\\n- ✅ related_work_survey.md — 21 篇文献 3 条线 + gap 分析 + novelty 定位\\n- ✅ Reviewer claim 强度评估 — 当前零 A 类 claim，exp027 仅证基础设施可行\\n- ✅ D039 framing 方向决策\\n\\n## 近期任务\\n- [ ] exp027 前 5 步 KL 监控（KL < 0.005 → 立即汇报）\\n- [ ] exp027 结果判定 → success ≥20% 则 complete_mvp()\\n- [ ] 如 exp027 pass → 启动 Phase B (B-IAVR) + 评估 GPU 需求（预估 600+ GPU-h）\\n- [ ] 如 exp027 fail → 24h deadline 后决策\\n- [ ] 引用真实性抽查（ARES/CorrectBench/AutoThink 等 arXiv ID 验证）\\n\\n## GPU 预算\\n- 分配：bjb1-17606 cuda:0,1（2× RTX PRO 6000 Blackwell 98GB）\\n- 当前：exp027 训练中，双卡满载\\n- 累计使用：~40 GPU-h\\n- exp027 预估：~84 GPU-h（2卡 × 42h）\\n- Post-MVP 预估（Reviewer 评估）：600-2000 GPU-h（B-IAVR ablations + multi-seed + 对比实验）\\n\\n## 关键风险\\n1. **exp027 训练稳定性**：128 rollouts 能否解决零奖励死亡螺旋？\\n2. **baseline 性能 gap**：cost-efficiency story 前提是 baseline ≥50%，当前 6.25%\\n3. **ARES 竞争**：需实验对比差异化\\n4. **GPU 预算缺口**：post-MVP 需 600+ GPU-h，当前仅 2 卡\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D040 | 2026-05-15 | 修正 exp027 step 3 判定框架为三层阈值，Plan B kl_coef 上调至 0.01 | exp027_stable_grpo, exp026_step_independent_grpo |\\n| D039 | 2026-05-15 | 论文 framing 方向锁定：cost-efficiency story，不走 performan | exp027_stable_grpo, exp026_step_independent_grpo, exp021_ragen_sft_v4 |\\n| D038 | 2026-05-15 | Reviewer 评估 exp027 pass/fail 论文可行性：修正 claim 强度阈值，确 | exp027_stable_grpo, exp026_step_independent_grpo, exp021_ragen_sft_v4, exp019b_expert_sft_v3 |\\n| D037 | 2026-05-15 | exp027 val 判定阈值：<20% fail、20-25% weak (=SFT)、30%+  | exp027_stable_grpo, exp026_step_independent_grpo, exp019b_expert_sft_v3 |\\n| D036 | 2026-05-15 | Reviewer critical 确认 exp026 GRPO 死亡螺旋：step 4 succe | exp026_step_independent_grpo, exp027_stable_grpo |\\n| D035 | 2026-05-15 | exp026 训练不稳定（step 2 峰值 32.81% → step 4 归零），准备 exp0 | exp026_step_independent_grpo |\\n| D034 | 2026-05-15 | 建立两级阈值：MVP=20% val（训练可行性 checkpoint），论文 baseline 最 | exp026_step_independent_grpo |\\n| D033 | 2026-05-15 | exp026 registry 误判修复：cron 因 WANDB_MODE=disabled +  | exp026_step_independent_grpo |\\n| D032 | 2026-05-15 | exp026 前 2 步训练指标强正向（success 6.25%→32.81%，entropy 未 | exp026_step_independent_grpo |\\n| D031 | 2026-05-15 | B-IAVR 代码审查通过（Reviewer info），Phase B 前必须解决两个 warni | exp026_step_independent_grpo |\\n\\n\", \"total_chars\": 4088, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_0125MYQVJfVCCBZfpa9KeJSD`</summary>

```json
{
  "project": "cost-verify-agent-rl",
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
  "session_id": "12f481e3-4249-4909-b494-860766cbf5b8",
  "uuid": "f8be9517-4edd-4d99-9221-c615d1f619bd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RutUDz7KQNrG6PEc8QiGan",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1355,
      "cache_read_input_tokens": 24232,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1355
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

_source line 11 · 2026-05-15T18:43:09.861Z_

<details><summary>↩ Tool result · `toolu_0125MYQVJfVCCBZfpa9KeJSD`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/memory.md\", \"content\": \"# Citation Audit — 2026-05-15\\n\\n完整审计结果已写入 artifacts/citation_audit.md。\\n\\n## 审计摘要\\n\\n- 验证论文：27 篇（literature_map.yaml 全部条目）+ 1 篇额外（Thinkless）\\n- 验证通过：20 篇\\n- 需要修正：7 篇（3 个严重问题，2 个中等问题，2 个轻微问题）\\n- 关键发现：AgentPRM arXiv ID/作者/标题全错；Huang2024 作者不匹配；DAPO 标题错误；CFGM 会议和年份错误\\n\", \"total_chars\": 256, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "12f481e3-4249-4909-b494-860766cbf5b8",
  "uuid": "615f19f5-4473-46e3-beda-20b08dc7dda4",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/memory.md\\\", \\\"content\\\": \\\"# Citation Audit — 2026-05-15\\\\n\\\\n完整审计结果已写入 artifacts/citation_audit.md。\\\\n\\\\n## 审计摘要\\\\n\\\\n- 验证论文：27 篇（literature_map.yaml 全部条目）+ 1 篇额外（Thinkless）\\\\n- 验证通过：20 篇\\\\n- 需要修正：7 篇（3 个严重问题，2 个中等问题，2 个轻微问题）\\\\n- 关键发现：AgentPRM arXiv ID/作者/标题全错；Huang2024 作者不匹配；DAPO 标题错误；CFGM 会议和年份错误\\\\n\\\", \\\"total_chars\\\": 256, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/memory.md\", \"content\": \"# Citation Audit — 2026-05-15\\n\\n完整审计结果已写入 artifacts/citation_audit.md。\\n\\n## 审计摘要\\n\\n- 验证论文：27 篇（literature_map.yaml 全部条目）+ 1 篇额外（Thinkless）\\n- 验证通过：20 篇\\n- 需要修正：7 篇（3 个严重问题，2 个中等问题，2 个轻微问题）\\n- 关键发现：AgentPRM arXiv ID/作者/标题全错；Huang2024 作者不匹配；DAPO 标题错误；CFGM 会议和年份错误\\n\", \"total_chars\": 256, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01JV1z1GTc6zgWXxhAHJmrL3`</summary>

```json
{
  "project": "cost-verify-agent-rl",
  "file": "ideas.md",
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
  "session_id": "12f481e3-4249-4909-b494-860766cbf5b8",
  "uuid": "8c403347-a5be-453c-95a9-c396518cf094",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RutUDz7KQNrG6PEc8QiGan",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1355,
      "cache_read_input_tokens": 24232,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1355
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

_source line 13 · 2026-05-15T18:43:10.335Z_

<details><summary>↩ Tool result · `toolu_01JV1z1GTc6zgWXxhAHJmrL3`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'cost-verify-agent-rl'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "12f481e3-4249-4909-b494-860766cbf5b8",
  "uuid": "2291ed45-39ca-44b7-8315-a414fc9c9c83",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"No ideas.md found for 'cost-verify-agent-rl'.\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'cost-verify-agent-rl'.\", \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 14_

<details open><summary>🔧 Tool call — Read · `toolu_01HXkXu5GTZozjAHoPExp4ec`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/analysis/related_work_survey.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "12f481e3-4249-4909-b494-860766cbf5b8",
  "uuid": "e6fac6d5-1154-4627-ab64-2238cc71f825",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RutUDz7KQNrG6PEc8QiGan",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1355,
      "cache_read_input_tokens": 24232,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1355
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

_source line 15 · 2026-05-15T18:43:10.828Z_

<details><summary>↩ Tool result · `toolu_01HXkXu5GTZozjAHoPExp4ec`</summary>

```text
1	# Related Work Survey — B-IAVR Project
2	
3	> 调研日期: 2026-05-15 | 覆盖范围: 2024-2026
4	
5	---
6	
7	## 1. Self-verification / Self-correction in LLM Agents
8	
9	### 1.1 Co-Evolution of Policy and Internal Reward for Language Agents (Self-Guide) (arXiv 2025)
10	- **作者**: (见 arXiv 2604.03098)
11	- **arXiv**: 2604.03098
12	- **核心方法**: 提出 Self-Guide，agent 在推理时生成短 self-guidance signal 指导下一步 action，训练时将同一 signal 转为 step-level internal reward 用于 GRPO 优化。形成 co-evolving loop：better policy → better guidance → better internal reward → better policy。在 ALFWorld 等三个 agent benchmark 上，inference-time guidance 已有明显提升，联合 GRPO 训练进一步提升 8%。
13	- **与我们的关系**: **强竞争 / 直接对标** — B-IAVR 基于 Self-Guide 框架
14	- **关键差异**: Self-Guide 是 always-on verification（每步都生成 guidance），不区分"何时值得验证"。B-IAVR 学习 selective verification policy，仅在 verification informative 时触发。Self-Guide 的 reward 来自 guidance 与 outcome 的 co-evolution，B-IAVR 用 action change 作为 verification informativeness 的 reward signal。
15	- **可借鉴点**: (1) co-evolving policy + reward 的框架设计 (2) step-level internal reward 的具体实现方式 (3) ALFWorld 上的实验设置和 baseline 数据
16	
17	### 1.2 S²R: Teaching LLMs to Self-verify and Self-correct via Reinforcement Learning (ACL 2025)
18	- **作者**: Ruotian Ma, Peisong Wang, Cheng Liu, Xingyan Liu, Jiaqi Chen, Bang Zhang, Xin Zhou, Nan Du, Jia Li
19	- **arXiv**: 2502.12853
20	- **核心方法**: 两阶段：(1) SFT 用 3.1k 样本初始化 self-verify + self-correct 行为 (2) outcome-level 和 process-level RL 强化这两个能力。Qwen2.5-math-7B 从 51.0% 提升到 81.6%，超过等量 long-CoT distilled data 训练的模型。
21	- **与我们的关系**: 互补 / 可借鉴
22	- **关键差异**: S²R 聚焦 math reasoning，self-correction 是对推理结果的修正；B-IAVR 聚焦 interactive agent 的 action-level verification，且核心创新是 selective（学习何时验证），S²R 未涉及选择性问题。S²R 使用 SFT 初始化 + RL 强化的两阶段方法，B-IAVR 使用纯 RL（GRPO）。
23	- **可借鉴点**: (1) SFT 初始化 self-verification 行为的 cold-start 策略 (2) process-level RL 的设计（可作为 B-IAVR 的 step-level reward 参考）
24	
25	### 1.3 SCoRe: Training Language Models to Self-Correct via Reinforcement Learning (Google, 2024)
26	- **作者**: Aviral Kumar, Vincent Zhuang, Rishabh Agarwal 等 (Google DeepMind)
27	- **arXiv**: 2409.12917
28	- **核心方法**: Multi-turn online RL，在模型自身生成的 correction traces 上训练。包含两阶段：初始 multi-turn RL on base model 生成 policy initialization（抗 collapse），再用 reward bonus 放大 self-correction。Gemini 1.0 Pro/1.5 Flash 上 self-correction 提升 15.6%/9.1%（MATH/HumanEval）。
29	- **与我们的关系**: 互补 / 可借鉴
30	- **关键差异**: SCoRe 训练模型"如何更好地 self-correct"（always-on），B-IAVR 训练模型"何时触发 verification"（selective）。SCoRe 面向静态 reasoning task，B-IAVR 面向 interactive agent。SCoRe 的 reward bonus 机制与 B-IAVR 的 action-change reward 目标不同。
31	- **可借鉴点**: (1) multi-turn RL 防止 policy collapse 的初始化策略 (2) on-policy correction traces 的训练范式
32	
33	### 1.4 Trust, But Verify (RISE): A Self-Verification Approach to RLVR (NeurIPS 2025)
34	- **作者**: (见 arXiv 2505.13445)
35	- **arXiv**: 2505.13445
36	- **核心方法**: 提出 RISE，在 online RL 中同时训练 problem-solving 和 self-verification。每轮迭代：模型生成 solutions → 自我 critique on-policy solutions → 两类 trajectories 共同更新 policy。用 verifiable rewards 同时监督 solution generation 和 self-verification。
37	- **与我们的关系**: 竞争 / 可借鉴
38	- **关键差异**: RISE 将 verification 作为 joint training objective 但不区分"何时验证"；B-IAVR 核心是学习 when to verify。RISE 面向 math reasoning + RLVR，B-IAVR 面向 interactive agent。RISE 的 verification target 是 solution correctness，B-IAVR 的是 action informativeness。
39	- **可借鉴点**: (1) joint training solver + verifier 的框架 (2) on-the-fly feedback for verification 的设计
40	
41	### 1.5 Incentivizing LLMs to Self-Verify Their Answers (arXiv 2025)
42	- **作者**: Fuxiang Zhang, Jiacheng Xu, Chaojie Wang, Ce Cui, Yang Liu, Bo An
43	- **arXiv**: 2506.01369
44	- **核心方法**: 在单一 RL 过程中统一 answer generation 和 verification training。设计 online policy-aligned buffer 和 dynamic verification rewards 稳定联合训练。训练后的模型可在推理时自我验证，无需外部 verifier。
45	- **与我们的关系**: 竞争 / 互补
46	- **关键差异**: 该工作统一 generation 和 verification 训练，但验证是 always-on 的（训练后的模型总是验证自己的输出）；B-IAVR 的核心创新是 selective verification。该工作面向 reasoning，B-IAVR 面向 interactive agent。
47	- **可借鉴点**: (1) policy-aligned buffer 的设计 (2) dynamic verification reward 的稳定训练技巧
48	
49	### 1.6 Self-Verification Dilemma: Experience-Driven Suppression of Overused Checking (arXiv 2026)
50	- **作者**: Quanyu Long, Kai Jie Jiang, Jianda Chen, Xu Guo, Leilei Gan, Wenya Wang
51	- **arXiv**: 2602.03485
52	- **核心方法**: 大规模实证分析发现 LRM 中大量 self-verification steps 是 confirmatory 而非 corrective，实际很少改变推理结果。提出 experience-driven test-time framework：检测 recheck 行为激活 → 查询离线经验池 → 估计 recheck 是否可能无用 → 选择性抑制。
53	- **与我们的关系**: **高度相关 / 互补** — 核心问题一致
54	- **关键差异**: 该工作是 test-time framework（不训练，基于检索经验池决定是否 recheck），B-IAVR 是 RL-trained policy（训练模型内化何时验证的决策）。该工作面向 reasoning chains 中的 recheck steps，B-IAVR 面向 interactive agent 的 action verification。该工作的"有用性"指标是 recheck 是否改变结论，与 B-IAVR 的 action change signal 思路相似但层级不同。
55	- **可借鉴点**: (1) "大多数 verification 是 confirmatory" 的实证发现可作为 B-IAVR motivation 的有力支持 (2) experience-driven suppression 的思路可作为 B-IAVR 的 test-time baseline
56	
57	### 1.7 When Does Verification Pay Off? A Closer Look at LLMs as Solution Verifiers (arXiv 2025)
58	- **作者**: Jack Lu, Ryan Teehan, Jinran Jin, Mengye Ren (NYU)
59	- **arXiv**: 2512.02304
60	- **核心方法**: 系统研究 37 个模型 × 9 个 benchmark 上 verification 的收益。提出 verifier gain 指标（比 verification accuracy 更完整）。发现 self-verification/同族 verification 的 gain 低于跨族 verification；solver 和 verifier 的 solution distribution 越相似，gain 越低。
61	- **与我们的关系**: 互补 — 提供理论和实证基础
62	- **关键差异**: 该工作是 empirical study，不训练 verification policy；B-IAVR 是 RL 训练框架。该工作面向 static task verification，B-IAVR 面向 interactive agent 的 action verification。
63	- **可借鉴点**: (1) verifier gain 指标可用于评估 B-IAVR 的 verification 效果 (2) "self-verification gain 较低"的发现解释了为什么 selective verification 比 always-on 更优 (3) 实验设计和评估方法论
64	
65	### Gap 分析
66	- **空白**: 现有 self-verification 工作几乎全部是 always-on（S²R, SCoRe, RISE, Self-Guide, Incentivizing LLMs）或 test-time heuristic（Self-Verification Dilemma）。**没有工作用 RL 训练 selective verification policy**——即学习 "when to verify" 而非 "how to verify"。
67	- **B-IAVR 填补的空白**: (1) 首个 RL-trained selective verification policy for interactive agents (2) 首次提出 action change 作为 verification informativeness 的 reward signal (3) 将 verification 从 always-on 转为 cost-aware 的 adaptive decision
68	- **Novelty claim 定位**: B-IAVR 在 "how to verify"（已被大量研究）和 "when to verify"（几乎空白）之间架起桥梁。Self-Verification Dilemma 提供了 "overused checking" 的 problem motivation，B-IAVR 提供了 learning-based solution。
69	
70	---
71	
72	## 2. RL for Interactive Agents (ALFWorld / WebShop / TextWorld)
73	
74	### 2.1 Group-in-Group Policy Optimization (GiGPO) for LLM Agent Training (NeurIPS 2025)
75	- **作者**: Lang Feng 等
76	- **arXiv**: 2505.10978
77	- **核心方法**: 在 GRPO 基础上引入两级优势估计：episode-level macro advantage（基于完整 trajectory 组）+ step-level micro advantage（通过 anchor state grouping 追溯构建 step-level 组）。在 ALFWorld 上比 GRPO 提升 >12%，WebShop 上提升 >9%，保持相同 GPU 内存开销。基于 Qwen2.5-1.5B/3B/7B-Instruct。
78	- **与我们的关系**: 互补 / 可借鉴
79	- **关键差异**: GiGPO 解决 credit assignment 问题（如何分配 reward），B-IAVR 解决 verification timing 问题（何时验证）。两者正交，可组合使用。
80	- **可借鉴点**: (1) step-level credit assignment 的 anchor state grouping 机制 (2) ALFWorld/WebShop 上的 GRPO baseline 数据（直接可比） (3) verl-agent 框架
81	
82	### 2.2 SPEAR: Self-imitation with Progressive Exploration for Agentic RL (ICLR 2026)
83	- **作者**: (Tencent Youtu Research)
84	- **arXiv**: 2509.22601
85	- **核心方法**: 在 SIL（Self-Imitation Learning）基础上，通过 progressive exploration-exploitation balance 解决 multi-turn RL 的不稳定性。早期用 auxiliary tool call reward 积累 tool-use skills + 上升 entropy trend，后期加强 self-imitation 利用成功经验。ALFWorld 上将 GRPO/GiGPO 分别提升 16.1%/5.1%，WebShop 上提升 20.7%/11.8%。
86	- **与我们的关系**: 互补 / 可借鉴
87	- **关键差异**: SPEAR 解决 exploration-exploitation balance 和训练稳定性，B-IAVR 解决 verification policy learning。B-IAVR 可将 SPEAR 的稳定性技巧整合进 GRPO 训练。
88	- **可借鉴点**: (1) progressive entropy management 策略 (2) auxiliary tool call reward 的设计 (3) ALFWorld/WebShop 的最新 SOTA 数据
89	
90	### 2.3 A Practitioner's Guide to Multi-turn Agentic Reinforcement Learning (arXiv 2025)
91	- **作者**: Ruiyi Wang, Prithviraj Ammanabrolu
92	- **arXiv**: 2510.01132
93	- **核心方法**: 系统拆解 multi-turn agentic RL 的设计空间为 environment / reward / policy 三个维度。在 TextWorld、ALFWorld、SWE-gym 上进行大规模实证研究。7 个主要发现：multi-turn RL 性能随环境复杂度 scale；简单环境训练可泛化到复杂环境；dense turn-level reward 加速训练；biased 和 unbiased 算法都能稳定学习。
94	- **与我们的关系**: 互补 — 提供方法论参考
95	- **关键差异**: 该工作是 systematic study，不提出新算法；B-IAVR 提出新的 verification policy + reward signal。
96	- **可借鉴点**: (1) dense turn-level reward 的设计建议（B-IAVR 的 action change reward 可视为一种 dense signal） (2) SFT:RL ratio 的 optimal balance (3) TextWorld/ALFWorld 的实验方法论和 baseline
97	
98	### 2.4 Self-Distilled Agentic Reinforcement Learning (SDAR) (arXiv 2026)
99	- **作者**: (ZJU REAL Lab)
100	- **arXiv**: 2605.15155
101	- **核心方法**: 将 On-Policy Self-Distillation (OPSD) 与 RL 结合。SDAR 用 sigmoid gate 将 teacher 的 token-level signals 映射到 gated auxiliary objective，加强 teacher-endorsed positive-gap tokens 的 distillation，软性衰减 negative teacher rejections。ALFWorld +9.4%，WebShop-Acc +10.2%（vs GRPO）。
102	- **与我们的关系**: 互补 / 可借鉴
103	- **关键差异**: SDAR 通过 self-distillation 增强 RL 训练信号密度，B-IAVR 通过 verification action change 增强。两者解决不同层面的问题。
104	- **可借鉴点**: (1) gated distillation 处理 noisy teacher signal 的方法 (2) Qwen2.5/Qwen3 在 ALFWorld 上的最新实验数据
105	
106	### 2.5 Agent-R1: Training Powerful LLM Agents with End-to-End Reinforcement Learning (arXiv 2025)
107	- **作者**: Mingyue Cheng 等
108	- **arXiv**: 2511.14460
109	- **核心方法**: 提出 modular RL framework，将 MDP 框架系统扩展到 LLM agent 场景（multi-turn, tool-use, imperfect info）。兼容多种 RL 算法，在 multihop QA 上验证。
110	- **与我们的关系**: 互补 — 框架层面
111	- **关键差异**: Agent-R1 是通用 agentic RL 框架，不涉及 verification；B-IAVR 聚焦 verification policy 的 RL 训练。
112	- **可借鉴点**: (1) MDP 扩展到 agent 场景的形式化方法 (2) multi-turn RL 的工程实现
113	
114	### 2.6 SkillRL: Evolving Agents via Recursive Skill-Augmented Reinforcement Learning (arXiv 2026)
115	- **作者**: (AIMING Lab)
116	- **arXiv**: 2602.08234
117	- **核心方法**: 自动 skill discovery + recursive evolution。将成功 trajectories 蒸馏为 strategic patterns，失败的蒸馏为 lessons。构建 hierarchical skill library (SkillBank)，包含 General Skills 和 Task-Specific Skills。ALFWorld/WebShop 上超过 strong baselines >15.3%。
118	- **与我们的关系**: 互补
119	- **关键差异**: SkillRL 学习 reusable skills/heuristics，B-IAVR 学习 verification policy。SkillRL 的 skill library 可能包含 verification 相关的 skill，但不是显式学习 "when to verify"。
120	- **可借鉴点**: (1) 从失败 trajectories 学习 lessons 的方法（可用于理解 B-IAVR 中 verification 失败的 patterns）
121	
122	### 2.7 Reinforcement World Model Learning (RWML) for LLM-based Agents (arXiv 2026)
123	- **作者**: Xiao Yu, Baolin Peng, Ruize Xu, Yelong Shen 等
124	- **arXiv**: 2602.05842
125	- **核心方法**: 自监督方法，训练 action-conditioned world models。对齐模型预测的 next state 和环境实际 next state（在 pre-trained embedding space 中）。ALFWorld 上结合 task-success reward 比纯 RL 高 6.9 points。
126	- **与我们的关系**: 互补
127	- **关键差异**: RWML 学习 world model 来辅助 policy，B-IAVR 学习 verification policy。RWML 的 world model 可以为 B-IAVR 提供"预测 next state"的能力，但 B-IAVR 不依赖显式 world model。
128	- **可借鉴点**: (1) sim-to-real gap reward 的设计 (2) semantic equivalence vs token-level fidelity 的对比思路
129	
130	### Gap 分析
131	- **空白**: 现有 RL for interactive agents 工作集中在 (a) 更好的 credit assignment（GiGPO）(b) 更好的 exploration（SPEAR）(c) 更丰富的训练信号（SDAR, RWML）。**没有工作将 verification 作为 agent 的可学习 action**，也没有工作将 verification timing 作为 RL 训练目标。
132	- **B-IAVR 填补的空白**: 在 ALFWorld 生态中引入 learned verification policy 这一新维度。Verification 不是训练技巧（如 reward shaping），而是 agent 的一个 actionable capability。
133	- **Novelty claim 定位**: GiGPO/SPEAR/SDAR 都在优化 "how to act better"，B-IAVR 在优化 "when to check before acting"。这是 ALFWorld RL 训练文献中尚未被探索的方向。
134	
135	---
136	
137	## 3. Cost-aware / Selective Computation in LLMs
138	
139	### 3.1 When To Solve, When To Verify: Compute-Optimal Problem Solving and Generative Verification (ICML 2025)
140	- **作者**: Nishad Singhi 等
141	- **arXiv**: 2504.01005
142	- **核心方法**: 在有限 inference budget 下，分析如何在 Self-Consistency (生成更多 solutions) 和 GenRM (verification) 之间最优分配 compute。发现 sampling 太少降低 coverage，verification 太少降低 precision，存在 optimal allocation。
143	- **与我们的关系**: **高度相关 / 理论基础**
144	- **关键差异**: 该工作是 compute-allocation analysis for static reasoning tasks，不涉及 interactive agent 也不用 RL 训练 allocation policy。B-IAVR 将类似的 "when to verify" 问题放到 interactive agent 场景中，并用 RL 训练 selective policy。
145	- **可借鉴点**: (1) solve-vs-verify tradeoff 的理论框架可作为 B-IAVR 的 motivation (2) compute-optimal 分析方法可用于评估 B-IAVR 的 verification frequency
146	
147	### 3.2 Thinkless: LLM Learns When to Think (NeurIPS 2025)
148	- **作者**: Gongfan Fang, Xinyin Ma, Xinchao Wang (NUS)
149	- **arXiv**: 2505.13379
150	- **核心方法**: 训练 LLM 用两个 control tokens 自适应选择 short-form 或 long-form reasoning。提出 Decoupled Group Relative Policy Optimization (DeGRPO)，将 control token loss 和 response loss 解耦。减少 long-chain thinking 50%-90%，部分 benchmark 上准确率还提升。
151	- **与我们的关系**: **高度相关 / 方法论最相近**
152	- **关键差异**: Thinkless 学习 "when to think more"（token-level），B-IAVR 学习 "when to verify"（action-level in interactive agent）。Thinkless 的决策单位是 reasoning mode（short vs long），B-IAVR 的决策单位是 verification action（verify vs not verify）。Thinkless 面向 static reasoning，B-IAVR 面向 interactive agent。
153	- **可借鉴点**: (1) DeGRPO 中 control token loss 解耦的设计——可直接应用于 B-IAVR 的 verification token training (2) control token 作为 adaptive computation gate 的范式
154	
155	### 3.3 Learning When to Think: Shaping Adaptive Reasoning via Multi-Stage RL (AutoThink) (arXiv 2025)
156	- **作者**: (见 arXiv 2505.10832)
157	- **arXiv**: 2505.10832
158	- **核心方法**: Multi-stage RL framework (AutoThink)，通过 stage-wise reward shaping 逐步优化 reasoning policy。模型学习仅在必要时触发 explicit reasoning，简单任务默认 succinct response。DeepSeek-R1-Distill-Qwen-1.5B 上 relative accuracy +6.4%，token 使用 -52%。
159	- **与我们的关系**: 互补 / 方法论可借鉴
160	- **关键差异**: AutoThink 的 "when to think" 是 reasoning depth 的选择，B-IAVR 的 "when to verify" 是 verification action 的选择。AutoThink 面向 reasoning，B-IAVR 面向 interactive agent。
161	- **可借鉴点**: (1) multi-stage reward shaping 策略 (2) progressive training curriculum
162	
163	### 3.4 SelfBudgeter: Adaptive Token Allocation for Efficient LLM Reasoning (arXiv 2025)
164	- **作者**: (见 arXiv 2505.11274)
165	- **arXiv**: 2505.11274
166	- **核心方法**: 双阶段训练：cold-start 阶段学习根据 query 预估 token budget，RL 阶段用 budget-guided GRPO 训练模型自主规划 budget 并遵守。显著减少 response 长度同时保持或提升准确率。
167	- **与我们的关系**: 互补
168	- **关键差异**: SelfBudgeter 控制 reasoning token 预算，B-IAVR 控制 verification action 的触发。SelfBudgeter 的 budget 是 token 数量，B-IAVR 的 "budget" 是 verification frequency。
169	- **可借鉴点**: (1) cold-start 阶段预估 budget 的设计（可用于 B-IAVR 的 verification probability 初始化）(2) budget-guided GRPO
170	
171	### 3.5 Dynamic Early Exit in Reasoning Models (arXiv 2025)
172	- **作者**: (见 arXiv 2504.15895)
173	- **arXiv**: 2504.15895
174	- **核心方法**: 无需额外训练，在 reasoning transition points 监控模型行为，当模型对 trial answer 有高 confidence 时动态终止 next reasoning chain 生成。CoT 长度减少 31%-43%，准确率提升 1.7%-5.7%。
175	- **与我们的关系**: 互补
176	- **关键差异**: Dynamic Early Exit 是 training-free 的 heuristic method，B-IAVR 是 RL-trained policy。Dynamic Early Exit 的判断基于 confidence heuristic，B-IAVR 基于 learned verification policy。
177	- **可借鉴点**: (1) "confidence at transition points" 的信号设计 (2) 可作为 B-IAVR 的 non-learned baseline
178	
179	### 3.6 Adaptive Test-Time Compute Allocation via Constrained Policy Optimization (arXiv 2026)
180	- **作者**: Zhiyuan Zhai, Bingcong Li, Bingnan Xiao, Ming Li, Xin Wang
181	- **arXiv**: 2604.14853
182	- **核心方法**: 将 adaptive compute allocation 形式化为 constrained optimization（最大化 expected accuracy，约束 average compute budget）。两阶段 Solve-then-Learn pipeline。解决 uniform budget 浪费问题：简单问题消耗与难题相同资源。
183	- **与我们的关系**: 互补 / 理论框架可借鉴
184	- **关键差异**: 该工作在 reasoning task 上分配 compute budget，B-IAVR 在 interactive agent 上分配 verification compute。两者都面向 "adaptive resource allocation" 但应用场景不同。
185	- **可借鉴点**: (1) constrained optimization 框架——B-IAVR 的 verification cost budget 可类似形式化 (2) Solve-then-Learn pipeline 思路
186	
187	### 3.7 Putting the Value Back in RL (RLV): Unifying LLM Reasoners with Verifiers (arXiv 2026)
188	- **作者**: Sareen, Moss 等 (Microsoft Research)
189	- **arXiv**: 2505.04842
190	- **核心方法**: 在 RL 训练中同时训练 LLM 作为 reasoner 和 generative verifier。利用 RL 生成的 abundant data 训练 verification 能力，无显著额外开销。MATH 上 parallel sampling 准确率提升 >20%，8-32x efficient test-time compute scaling。
191	- **与我们的关系**: 互补 / 可借鉴
192	- **关键差异**: RLV 在 reasoning 场景中 jointly train reasoner + verifier（always-on verification at test time），B-IAVR 在 interactive agent 场景中 train selective verification policy。RLV 关注 "how to verify better"，B-IAVR 关注 "when to verify"。
193	- **可借鉴点**: (1) 利用 RL-generated data 训练 verifier 的思路——B-IAVR 可借鉴这种 data-efficient 方法 (2) reasoner + verifier joint training 的 loss 设计
194	
195	### 3.8 Self-Verification Dilemma: Experience-Driven Suppression of Overused Checking (arXiv 2026)
196	- *(已在 1.6 详述，此处标注跨线相关性)*
197	- **与线 3 的关系**: 该工作实证证明了 "大多数 verification 是浪费的"（confirmatory 而非 corrective），直接支持 cost-aware / selective verification 的必要性。是 B-IAVR 的核心 motivation paper 之一。
198	
199	### Gap 分析
200	- **空白**: Cost-aware computation 工作集中在两类：(a) reasoning depth/token budget 控制（Thinkless, AutoThink, SelfBudgeter, Dynamic Early Exit）(b) solve-vs-verify compute allocation（When To Solve When To Verify, RLV）。**没有工作将 cost-aware 思想应用到 interactive agent 的 verification decision**，也没有工作用 action change 作为 verification cost-benefit 的评价信号。
201	- **B-IAVR 填补的空白**: (1) 将 "when to compute more" 从 reasoning depth 扩展到 agent verification action (2) 用 action change 作为 verification informativeness 的天然 cost-benefit signal（action 没变 = verification 没信息价值 = 计算浪费）
202	- **Novelty claim 定位**: Thinkless 回答 "when to think deeper"，When To Solve When To Verify 回答 "solve vs verify 的 optimal ratio"，B-IAVR 回答 "when to verify in interactive agents"。三者在 selective computation 的谱系上互补，B-IAVR 是唯一面向 interactive agent 场景的。
203	
204	---
205	
206	## 4. 综合定位
207	
208	### B-IAVR 的独特贡献（综合三条线的 gap）
209	
210	1. **首个 RL-trained selective verification policy for interactive agents**: 线 1 的 self-verification 工作都是 always-on；线 3 的 cost-aware 工作都面向 static reasoning。B-IAVR 首次在 interactive agent 场景中用 RL 训练 "when to verify"。
211	
212	2. **Action change 作为 verification informativeness 的 reward signal**: 这是全新的 reward design。现有工作的 verification reward 要么基于 outcome correctness（RISE, S²R），要么基于 confidence heuristic（Dynamic Early Exit），要么基于 compute budget（SelfBudgeter）。B-IAVR 的 action change 信号是直接衡量 verification 是否影响 agent 后续行为的天然指标。
213	
214	3. **Cost-benefit framing for agent verification**: 将 verification 从 "accuracy tool" 重新定义为 "cost-benefit decision"。When To Solve When To Verify 在 reasoning 中做了类似分析，B-IAVR 在 interactive agent 中做了实践。
215	
216	### 最强竞争对手分析
217	
218	| 竞争对手 | 威胁程度 | 核心差异 |
219	|---------|---------|---------|
220	| **Self-Guide** (2604.03098) | ★★★★★ | 直接基础框架。B-IAVR 的增量创新需清晰论证 selective > always-on |
221	| **Thinkless** (2505.13379) | ★★★★☆ | 方法论最相近（RL-trained "when to X"），但面向 reasoning 不是 agent |
222	| **Self-Verification Dilemma** (2602.03485) | ★★★☆☆ | Problem motivation 高度重叠，但 solution 不同（heuristic vs learned） |
223	| **RISE** (2505.13445) | ★★★☆☆ | Joint train solver + verifier，但不是 selective |
224	| **When To Solve When To Verify** (2504.01005) | ★★★☆☆ | Theoretical framing 相近，但面向 static reasoning |
225	
226	### 建议的 Related Work 叙事结构
227	
228	1. **Self-verification in LLM agents** — 从 SCoRe/S²R 的 self-correction 到 Self-Guide 的 agent self-guidance，指出现有方法均为 always-on verification。引出 Self-Verification Dilemma 的实证发现：大多数 verification 是浪费的。
229	
230	2. **RL for interactive agents** — 从 GRPO 到 GiGPO/SPEAR/SDAR 的进展，指出 credit assignment、exploration、dense reward 等问题被充分研究，但 verification as learnable action 尚未被探索。
231	
232	3. **Cost-aware / selective computation** — 从 Thinkless/AutoThink 的 adaptive reasoning depth 到 When To Solve When To Verify 的 compute allocation，指出 "when to compute more" 的思想尚未被应用到 interactive agent verification。
233	
234	4. **Our work: B-IAVR** — 位于三条线的交汇处：(a) 从线 1 继承 self-verification 能力 (b) 在线 2 的 ALFWorld/GRPO 生态中实现 (c) 用线 3 的 cost-aware 思想指导 selective verification policy。
235	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "12f481e3-4249-4909-b494-860766cbf5b8",
  "uuid": "e800afba-7386-4bb8-a78d-7d331e38aa66",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/analysis/related_work_survey.md",
      "content": "# Related Work Survey — B-IAVR Project\n\n> 调研日期: 2026-05-15 | 覆盖范围: 2024-2026\n\n---\n\n## 1. Self-verification / Self-correction in LLM Agents\n\n### 1.1 Co-Evolution of Policy and Internal Reward for Language Agents (Self-Guide) (arXiv 2025)\n- **作者**: (见 arXiv 2604.03098)\n- **arXiv**: 2604.03098\n- **核心方法**: 提出 Self-Guide，agent 在推理时生成短 self-guidance signal 指导下一步 action，训练时将同一 signal 转为 step-level internal reward 用于 GRPO 优化。形成 co-evolving loop：better policy → better guidance → better internal reward → better policy。在 ALFWorld 等三个 agent benchmark 上，inference-time guidance 已有明显提升，联合 GRPO 训练进一步提升 8%。\n- **与我们的关系**: **强竞争 / 直接对标** — B-IAVR 基于 Self-Guide 框架\n- **关键差异**: Self-Guide 是 always-on verification（每步都生成 guidance），不区分\"何时值得验证\"。B-IAVR 学习 selective verification policy，仅在 verification informative 时触发。Self-Guide 的 reward 来自 guidance 与 outcome 的 co-evolution，B-IAVR 用 action change 作为 verification informativeness 的 reward signal。\n- **可借鉴点**: (1) co-evolving policy + reward 的框架设计 (2) step-level internal reward 的具体实现方式 (3) ALFWorld 上的实验设置和 baseline 数据\n\n### 1.2 S²R: Teaching LLMs to Self-verify and Self-correct via Reinforcement Learning (ACL 2025)\n- **作者**: Ruotian Ma, Peisong Wang, Cheng Liu, Xingyan Liu, Jiaqi Chen, Bang Zhang, Xin Zhou, Nan Du, Jia Li\n- **arXiv**: 2502.12853\n- **核心方法**: 两阶段：(1) SFT 用 3.1k 样本初始化 self-verify + self-correct 行为 (2) outcome-level 和 process-level RL 强化这两个能力。Qwen2.5-math-7B 从 51.0% 提升到 81.6%，超过等量 long-CoT distilled data 训练的模型。\n- **与我们的关系**: 互补 / 可借鉴\n- **关键差异**: S²R 聚焦 math reasoning，self-correction 是对推理结果的修正；B-IAVR 聚焦 interactive agent 的 action-level verification，且核心创新是 selective（学习何时验证），S²R 未涉及选择性问题。S²R 使用 SFT 初始化 + RL 强化的两阶段方法，B-IAVR 使用纯 RL（GRPO）。\n- **可借鉴点**: (1) SFT 初始化 self-verification 行为的 cold-start 策略 (2) process-level RL 的设计（可作为 B-IAVR 的 step-level reward 参考）\n\n### 1.3 SCoRe: Training Language Models to Self-Correct via Reinforcement Learning (Google, 2024)\n- **作者**: Aviral Kumar, Vincent Zhuang, Rishabh Agarwal 等 (Google DeepMind)\n- **arXiv**: 2409.12917\n- **核心方法**: Multi-turn online RL，在模型自身生成的 correction traces 上训练。包含两阶段：初始 multi-turn RL on base model 生成 policy initialization（抗 collapse），再用 reward bonus 放大 self-correction。Gemini 1.0 Pro/1.5 Flash 上 self-correction 提升 15.6%/9.1%（MATH/HumanEval）。\n- **与我们的关系**: 互补 / 可借鉴\n- **关键差异**: SCoRe 训练模型\"如何更好地 self-correct\"（always-on），B-IAVR 训练模型\"何时触发 verification\"（selective）。SCoRe 面向静态 reasoning task，B-IAVR 面向 interactive agent。SCoRe 的 reward bonus 机制与 B-IAVR 的 action-change reward 目标不同。\n- **可借鉴点**: (1) multi-turn RL 防止 policy collapse 的初始化策略 (2) on-policy correction traces 的训练范式\n\n### 1.4 Trust, But Verify (RISE): A Self-Verification Approach to RLVR (NeurIPS 2025)\n- **作者**: (见 arXiv 2505.13445)\n- **arXiv**: 2505.13445\n- **核心方法**: 提出 RISE，在 online RL 中同时训练 problem-solving 和 self-verification。每轮迭代：模型生成 solutions → 自我 critique on-policy solutions → 两类 trajectories 共同更新 policy。用 verifiable rewards 同时监督 solution generation 和 self-verification。\n- **与我们的关系**: 竞争 / 可借鉴\n- **关键差异**: RISE 将 verification 作为 joint training objective 但不区分\"何时验证\"；B-IAVR 核心是学习 when to verify。RISE 面向 math reasoning + RLVR，B-IAVR 面向 interactive agent。RISE 的 verification target 是 solution correctness，B-IAVR 的是 action informativeness。\n- **可借鉴点**: (1) joint training solver + verifier 的框架 (2) on-the-fly feedback for verification 的设计\n\n### 1.5 Incentivizing LLMs to Self-Verify Their Answers (arXiv 2025)\n- **作者**: Fuxiang Zhang, Jiacheng Xu, Chaojie Wang, Ce Cui, Yang Liu, Bo An\n- **arXiv**: 2506.01369\n- **核心方法**: 在单一 RL 过程中统一 answer generation 和 verification training。设计 online policy-aligned buffer 和 dynamic verification rewards 稳定联合训练。训练后的模型可在推理时自我验证，无需外部 verifier。\n- **与我们的关系**: 竞争 / 互补\n- **关键差异**: 该工作统一 generation 和 verification 训练，但验证是 always-on 的（训练后的模型总是验证自己的输出）；B-IAVR 的核心创新是 selective verification。该工作面向 reasoning，B-IAVR 面向 interactive agent。\n- **可借鉴点**: (1) policy-aligned buffer 的设计 (2) dynamic verification reward 的稳定训练技巧\n\n### 1.6 Self-Verification Dilemma: Experience-Driven Suppression of Overused Checking (arXiv 2026)\n- **作者**: Quanyu Long, Kai Jie Jiang, Jianda Chen, Xu Guo, Leilei Gan, Wenya Wang\n- **arXiv**: 2602.03485\n- **核心方法**: 大规模实证分析发现 LRM 中大量 self-verification steps 是 confirmatory 而非 corrective，实际很少改变推理结果。提出 experience-driven test-time framework：检测 recheck 行为激活 → 查询离线经验池 → 估计 recheck 是否可能无用 → 选择性抑制。\n- **与我们的关系**: **高度相关 / 互补** — 核心问题一致\n- **关键差异**: 该工作是 test-time framework（不训练，基于检索经验池决定是否 recheck），B-IAVR 是 RL-trained policy（训练模型内化何时验证的决策）。该工作面向 reasoning chains 中的 recheck steps，B-IAVR 面向 interactive agent 的 action verification。该工作的\"有用性\"指标是 recheck 是否改变结论，与 B-IAVR 的 action change signal 思路相似但层级不同。\n- **可借鉴点**: (1) \"大多数 verification 是 confirmatory\" 的实证发现可作为 B-IAVR motivation 的有力支持 (2) experience-driven suppression 的思路可作为 B-IAVR 的 test-time baseline\n\n### 1.7 When Does Verification Pay Off? A Closer Look at LLMs as Solution Verifiers (arXiv 2025)\n- **作者**: Jack Lu, Ryan Teehan, Jinran Jin, Mengye Ren (NYU)\n- **arXiv**: 2512.02304\n- **核心方法**: 系统研究 37 个模型 × 9 个 benchmark 上 verification 的收益。提出 verifier gain 指标（比 verification accuracy 更完整）。发现 self-verification/同族 verification 的 gain 低于跨族 verification；solver 和 verifier 的 solution distribution 越相似，gain 越低。\n- **与我们的关系**: 互补 — 提供理论和实证基础\n- **关键差异**: 该工作是 empirical study，不训练 verification policy；B-IAVR 是 RL 训练框架。该工作面向 static task verification，B-IAVR 面向 interactive agent 的 action verification。\n- **可借鉴点**: (1) verifier gain 指标可用于评估 B-IAVR 的 verification 效果 (2) \"self-verification gain 较低\"的发现解释了为什么 selective verification 比 always-on 更优 (3) 实验设计和评估方法论\n\n### Gap 分析\n- **空白**: 现有 self-verification 工作几乎全部是 always-on（S²R, SCoRe, RISE, Self-Guide, Incentivizing LLMs）或 test-time heuristic（Self-Verification Dilemma）。**没有工作用 RL 训练 selective verification policy**——即学习 \"when to verify\" 而非 \"how to verify\"。\n- **B-IAVR 填补的空白**: (1) 首个 RL-trained selective verification policy for interactive agents (2) 首次提出 action change 作为 verification informativeness 的 reward signal (3) 将 verification 从 always-on 转为 cost-aware 的 adaptive decision\n- **Novelty claim 定位**: B-IAVR 在 \"how to verify\"（已被大量研究）和 \"when to verify\"（几乎空白）之间架起桥梁。Self-Verification Dilemma 提供了 \"overused checking\" 的 problem motivation，B-IAVR 提供了 learning-based solution。\n\n---\n\n## 2. RL for Interactive Agents (ALFWorld / WebShop / TextWorld)\n\n### 2.1 Group-in-Group Policy Optimization (GiGPO) for LLM Agent Training (NeurIPS 2025)\n- **作者**: Lang Feng 等\n- **arXiv**: 2505.10978\n- **核心方法**: 在 GRPO 基础上引入两级优势估计：episode-level macro advantage（基于完整 trajectory 组）+ step-level micro advantage（通过 anchor state grouping 追溯构建 step-level 组）。在 ALFWorld 上比 GRPO 提升 >12%，WebShop 上提升 >9%，保持相同 GPU 内存开销。基于 Qwen2.5-1.5B/3B/7B-Instruct。\n- **与我们的关系**: 互补 / 可借鉴\n- **关键差异**: GiGPO 解决 credit assignment 问题（如何分配 reward），B-IAVR 解决 verification timing 问题（何时验证）。两者正交，可组合使用。\n- **可借鉴点**: (1) step-level credit assignment 的 anchor state grouping 机制 (2) ALFWorld/WebShop 上的 GRPO baseline 数据（直接可比） (3) verl-agent 框架\n\n### 2.2 SPEAR: Self-imitation with Progressive Exploration for Agentic RL (ICLR 2026)\n- **作者**: (Tencent Youtu Research)\n- **arXiv**: 2509.22601\n- **核心方法**: 在 SIL（Self-Imitation Learning）基础上，通过 progressive exploration-exploitation balance 解决 multi-turn RL 的不稳定性。早期用 auxiliary tool call reward 积累 tool-use skills + 上升 entropy trend，后期加强 self-imitation 利用成功经验。ALFWorld 上将 GRPO/GiGPO 分别提升 16.1%/5.1%，WebShop 上提升 20.7%/11.8%。\n- **与我们的关系**: 互补 / 可借鉴\n- **关键差异**: SPEAR 解决 exploration-exploitation balance 和训练稳定性，B-IAVR 解决 verification policy learning。B-IAVR 可将 SPEAR 的稳定性技巧整合进 GRPO 训练。\n- **可借鉴点**: (1) progressive entropy management 策略 (2) auxiliary tool call reward 的设计 (3) ALFWorld/WebShop 的最新 SOTA 数据\n\n### 2.3 A Practitioner's Guide to Multi-turn Agentic Reinforcement Learning (arXiv 2025)\n- **作者**: Ruiyi Wang, Prithviraj Ammanabrolu\n- **arXiv**: 2510.01132\n- **核心方法**: 系统拆解 multi-turn agentic RL 的设计空间为 environment / reward / policy 三个维度。在 TextWorld、ALFWorld、SWE-gym 上进行大规模实证研究。7 个主要发现：multi-turn RL 性能随环境复杂度 scale；简单环境训练可泛化到复杂环境；dense turn-level reward 加速训练；biased 和 unbiased 算法都能稳定学习。\n- **与我们的关系**: 互补 — 提供方法论参考\n- **关键差异**: 该工作是 systematic study，不提出新算法；B-IAVR 提出新的 verification policy + reward signal。\n- **可借鉴点**: (1) dense turn-level reward 的设计建议（B-IAVR 的 action change reward 可视为一种 dense signal） (2) SFT:RL ratio 的 optimal balance (3) TextWorld/ALFWorld 的实验方法论和 baseline\n\n### 2.4 Self-Distilled Agentic Reinforcement Learning (SDAR) (arXiv 2026)\n- **作者**: (ZJU REAL Lab)\n- **arXiv**: 2605.15155\n- **核心方法**: 将 On-Policy Self-Distillation (OPSD) 与 RL 结合。SDAR 用 sigmoid gate 将 teacher 的 token-level signals 映射到 gated auxiliary objective，加强 teacher-endorsed positive-gap tokens 的 distillation，软性衰减 negative teacher rejections。ALFWorld +9.4%，WebShop-Acc +10.2%（vs GRPO）。\n- **与我们的关系**: 互补 / 可借鉴\n- **关键差异**: SDAR 通过 self-distillation 增强 RL 训练信号密度，B-IAVR 通过 verification action change 增强。两者解决不同层面的问题。\n- **可借鉴点**: (1) gated distillation 处理 noisy teacher signal 的方法 (2) Qwen2.5/Qwen3 在 ALFWorld 上的最新实验数据\n\n### 2.5 Agent-R1: Training Powerful LLM Agents with End-to-End Reinforcement Learning (arXiv 2025)\n- **作者**: Mingyue Cheng 等\n- **arXiv**: 2511.14460\n- **核心方法**: 提出 modular RL framework，将 MDP 框架系统扩展到 LLM agent 场景（multi-turn, tool-use, imperfect info）。兼容多种 RL 算法，在 multihop QA 上验证。\n- **与我们的关系**: 互补 — 框架层面\n- **关键差异**: Agent-R1 是通用 agentic RL 框架，不涉及 verification；B-IAVR 聚焦 verification policy 的 RL 训练。\n- **可借鉴点**: (1) MDP 扩展到 agent 场景的形式化方法 (2) multi-turn RL 的工程实现\n\n### 2.6 SkillRL: Evolving Agents via Recursive Skill-Augmented Reinforcement Learning (arXiv 2026)\n- **作者**: (AIMING Lab)\n- **arXiv**: 2602.08234\n- **核心方法**: 自动 skill discovery + recursive evolution。将成功 trajectories 蒸馏为 strategic patterns，失败的蒸馏为 lessons。构建 hierarchical skill library (SkillBank)，包含 General Skills 和 Task-Specific Skills。ALFWorld/WebShop 上超过 strong baselines >15.3%。\n- **与我们的关系**: 互补\n- **关键差异**: SkillRL 学习 reusable skills/heuristics，B-IAVR 学习 verification policy。SkillRL 的 skill library 可能包含 verification 相关的 skill，但不是显式学习 \"when to verify\"。\n- **可借鉴点**: (1) 从失败 trajectories 学习 lessons 的方法（可用于理解 B-IAVR 中 verification 失败的 patterns）\n\n### 2.7 Reinforcement World Model Learning (RWML) for LLM-based Agents (arXiv 2026)\n- **作者**: Xiao Yu, Baolin Peng, Ruize Xu, Yelong Shen 等\n- **arXiv**: 2602.05842\n- **核心方法**: 自监督方法，训练 action-conditioned world models。对齐模型预测的 next state 和环境实际 next state（在 pre-trained embedding space 中）。ALFWorld 上结合 task-success reward 比纯 RL 高 6.9 points。\n- **与我们的关系**: 互补\n- **关键差异**: RWML 学习 world model 来辅助 policy，B-IAVR 学习 verification policy。RWML 的 world model 可以为 B-IAVR 提供\"预测 next state\"的能力，但 B-IAVR 不依赖显式 world model。\n- **可借鉴点**: (1) sim-to-real gap reward 的设计 (2) semantic equivalence vs token-level fidelity 的对比思路\n\n### Gap 分析\n- **空白**: 现有 RL for interactive agents 工作集中在 (a) 更好的 credit assignment（GiGPO）(b) 更好的 exploration（SPEAR）(c) 更丰富的训练信号（SDAR, RWML）。**没有工作将 verification 作为 agent 的可学习 action**，也没有工作将 verification timing 作为 RL 训练目标。\n- **B-IAVR 填补的空白**: 在 ALFWorld 生态中引入 learned verification policy 这一新维度。Verification 不是训练技巧（如 reward shaping），而是 agent 的一个 actionable capability。\n- **Novelty claim 定位**: GiGPO/SPEAR/SDAR 都在优化 \"how to act better\"，B-IAVR 在优化 \"when to check before acting\"。这是 ALFWorld RL 训练文献中尚未被探索的方向。\n\n---\n\n## 3. Cost-aware / Selective Computation in LLMs\n\n### 3.1 When To Solve, When To Verify: Compute-Optimal Problem Solving and Generative Verification (ICML 2025)\n- **作者**: Nishad Singhi 等\n- **arXiv**: 2504.01005\n- **核心方法**: 在有限 inference budget 下，分析如何在 Self-Consistency (生成更多 solutions) 和 GenRM (verification) 之间最优分配 compute。发现 sampling 太少降低 coverage，verification 太少降低 precision，存在 optimal allocation。\n- **与我们的关系**: **高度相关 / 理论基础**\n- **关键差异**: 该工作是 compute-allocation analysis for static reasoning tasks，不涉及 interactive agent 也不用 RL 训练 allocation policy。B-IAVR 将类似的 \"when to verify\" 问题放到 interactive agent 场景中，并用 RL 训练 selective policy。\n- **可借鉴点**: (1) solve-vs-verify tradeoff 的理论框架可作为 B-IAVR 的 motivation (2) compute-optimal 分析方法可用于评估 B-IAVR 的 verification frequency\n\n### 3.2 Thinkless: LLM Learns When to Think (NeurIPS 2025)\n- **作者**: Gongfan Fang, Xinyin Ma, Xinchao Wang (NUS)\n- **arXiv**: 2505.13379\n- **核心方法**: 训练 LLM 用两个 control tokens 自适应选择 short-form 或 long-form reasoning。提出 Decoupled Group Relative Policy Optimization (DeGRPO)，将 control token loss 和 response loss 解耦。减少 long-chain thinking 50%-90%，部分 benchmark 上准确率还提升。\n- **与我们的关系**: **高度相关 / 方法论最相近**\n- **关键差异**: Thinkless 学习 \"when to think more\"（token-level），B-IAVR 学习 \"when to verify\"（action-level in interactive agent）。Thinkless 的决策单位是 reasoning mode（short vs long），B-IAVR 的决策单位是 verification action（verify vs not verify）。Thinkless 面向 static reasoning，B-IAVR 面向 interactive agent。\n- **可借鉴点**: (1) DeGRPO 中 control token loss 解耦的设计——可直接应用于 B-IAVR 的 verification token training (2) control token 作为 adaptive computation gate 的范式\n\n### 3.3 Learning When to Think: Shaping Adaptive Reasoning via Multi-Stage RL (AutoThink) (arXiv 2025)\n- **作者**: (见 arXiv 2505.10832)\n- **arXiv**: 2505.10832\n- **核心方法**: Multi-stage RL framework (AutoThink)，通过 stage-wise reward shaping 逐步优化 reasoning policy。模型学习仅在必要时触发 explicit reasoning，简单任务默认 succinct response。DeepSeek-R1-Distill-Qwen-1.5B 上 relative accuracy +6.4%，token 使用 -52%。\n- **与我们的关系**: 互补 / 方法论可借鉴\n- **关键差异**: AutoThink 的 \"when to think\" 是 reasoning depth 的选择，B-IAVR 的 \"when to verify\" 是 verification action 的选择。AutoThink 面向 reasoning，B-IAVR 面向 interactive agent。\n- **可借鉴点**: (1) multi-stage reward shaping 策略 (2) progressive training curriculum\n\n### 3.4 SelfBudgeter: Adaptive Token Allocation for Efficient LLM Reasoning (arXiv 2025)\n- **作者**: (见 arXiv 2505.11274)\n- **arXiv**: 2505.11274\n- **核心方法**: 双阶段训练：cold-start 阶段学习根据 query 预估 token budget，RL 阶段用 budget-guided GRPO 训练模型自主规划 budget 并遵守。显著减少 response 长度同时保持或提升准确率。\n- **与我们的关系**: 互补\n- **关键差异**: SelfBudgeter 控制 reasoning token 预算，B-IAVR 控制 verification action 的触发。SelfBudgeter 的 budget 是 token 数量，B-IAVR 的 \"budget\" 是 verification frequency。\n- **可借鉴点**: (1) cold-start 阶段预估 budget 的设计（可用于 B-IAVR 的 verification probability 初始化）(2) budget-guided GRPO\n\n### 3.5 Dynamic Early Exit in Reasoning Models (arXiv 2025)\n- **作者**: (见 arXiv 2504.15895)\n- **arXiv**: 2504.15895\n- **核心方法**: 无需额外训练，在 reasoning transition points 监控模型行为，当模型对 trial answer 有高 confidence 时动态终止 next reasoning chain 生成。CoT 长度减少 31%-43%，准确率提升 1.7%-5.7%。\n- **与我们的关系**: 互补\n- **关键差异**: Dynamic Early Exit 是 training-free 的 heuristic method，B-IAVR 是 RL-trained policy。Dynamic Early Exit 的判断基于 confidence heuristic，B-IAVR 基于 learned verification policy。\n- **可借鉴点**: (1) \"confidence at transition points\" 的信号设计 (2) 可作为 B-IAVR 的 non-learned baseline\n\n### 3.6 Adaptive Test-Time Compute Allocation via Constrained Policy Optimization (arXiv 2026)\n- **作者**: Zhiyuan Zhai, Bingcong Li, Bingnan Xiao, Ming Li, Xin Wang\n- **arXiv**: 2604.14853\n- **核心方法**: 将 adaptive compute allocation 形式化为 constrained optimization（最大化 expected accuracy，约束 average compute budget）。两阶段 Solve-then-Learn pipeline。解决 uniform budget 浪费问题：简单问题消耗与难题相同资源。\n- **与我们的关系**: 互补 / 理论框架可借鉴\n- **关键差异**: 该工作在 reasoning task 上分配 compute budget，B-IAVR 在 interactive agent 上分配 verification compute。两者都面向 \"adaptive resource allocation\" 但应用场景不同。\n- **可借鉴点**: (1) constrained optimization 框架——B-IAVR 的 verification cost budget 可类似形式化 (2) Solve-then-Learn pipeline 思路\n\n### 3.7 Putting the Value Back in RL (RLV): Unifying LLM Reasoners with Verifiers (arXiv 2026)\n- **作者**: Sareen, Moss 等 (Microsoft Research)\n- **arXiv**: 2505.04842\n- **核心方法**: 在 RL 训练中同时训练 LLM 作为 reasoner 和 generative verifier。利用 RL 生成的 abundant data 训练 verification 能力，无显著额外开销。MATH 上 parallel sampling 准确率提升 >20%，8-32x efficient test-time compute scaling。\n- **与我们的关系**: 互补 / 可借鉴\n- **关键差异**: RLV 在 reasoning 场景中 jointly train reasoner + verifier（always-on verification at test time），B-IAVR 在 interactive agent 场景中 train selective verification policy。RLV 关注 \"how to verify better\"，B-IAVR 关注 \"when to verify\"。\n- **可借鉴点**: (1) 利用 RL-generated data 训练 verifier 的思路——B-IAVR 可借鉴这种 data-efficient 方法 (2) reasoner + verifier joint training 的 loss 设计\n\n### 3.8 Self-Verification Dilemma: Experience-Driven Suppression of Overused Checking (arXiv 2026)\n- *(已在 1.6 详述，此处标注跨线相关性)*\n- **与线 3 的关系**: 该工作实证证明了 \"大多数 verification 是浪费的\"（confirmatory 而非 corrective），直接支持 cost-aware / selective verification 的必要性。是 B-IAVR 的核心 motivation paper 之一。\n\n### Gap 分析\n- **空白**: Cost-aware computation 工作集中在两类：(a) reasoning depth/token budget 控制（Thinkless, AutoThink, SelfBudgeter, Dynamic Early Exit）(b) solve-vs-verify compute allocation（When To Solve When To Verify, RLV）。**没有工作将 cost-aware 思想应用到 interactive agent 的 verification decision**，也没有工作用 action change 作为 verification cost-benefit 的评价信号。\n- **B-IAVR 填补的空白**: (1) 将 \"when to compute more\" 从 reasoning depth 扩展到 agent verification action (2) 用 action change 作为 verification informativeness 的天然 cost-benefit signal（action 没变 = verification 没信息价值 = 计算浪费）\n- **Novelty claim 定位**: Thinkless 回答 \"when to think deeper\"，When To Solve When To Verify 回答 \"solve vs verify 的 optimal ratio\"，B-IAVR 回答 \"when to verify in interactive agents\"。三者在 selective computation 的谱系上互补，B-IAVR 是唯一面向 interactive agent 场景的。\n\n---\n\n## 4. 综合定位\n\n### B-IAVR 的独特贡献（综合三条线的 gap）\n\n1. **首个 RL-trained selective verification policy for interactive agents**: 线 1 的 self-verification 工作都是 always-on；线 3 的 cost-aware 工作都面向 static reasoning。B-IAVR 首次在 interactive agent 场景中用 RL 训练 \"when to verify\"。\n\n2. **Action change 作为 verification informativeness 的 reward signal**: 这是全新的 reward design。现有工作的 verification reward 要么基于 outcome correctness（RISE, S²R），要么基于 confidence heuristic（Dynamic Early Exit），要么基于 compute budget（SelfBudgeter）。B-IAVR 的 action change 信号是直接衡量 verification 是否影响 agent 后续行为的天然指标。\n\n3. **Cost-benefit framing for agent verification**: 将 verification 从 \"accuracy tool\" 重新定义为 \"cost-benefit decision\"。When To Solve When To Verify 在 reasoning 中做了类似分析，B-IAVR 在 interactive agent 中做了实践。\n\n### 最强竞争对手分析\n\n| 竞争对手 | 威胁程度 | 核心差异 |\n|---------|---------|---------|\n| **Self-Guide** (2604.03098) | ★★★★★ | 直接基础框架。B-IAVR 的增量创新需清晰论证 selective > always-on |\n| **Thinkless** (2505.13379) | ★★★★☆ | 方法论最相近（RL-trained \"when to X\"），但面向 reasoning 不是 agent |\n| **Self-Verification Dilemma** (2602.03485) | ★★★☆☆ | Problem motivation 高度重叠，但 solution 不同（heuristic vs learned） |\n| **RISE** (2505.13445) | ★★★☆☆ | Joint train solver + verifier，但不是 selective |\n| **When To Solve When To Verify** (2504.01005) | ★★★☆☆ | Theoretical framing 相近，但面向 static reasoning |\n\n### 建议的 Related Work 叙事结构\n\n1. **Self-verification in LLM agents** — 从 SCoRe/S²R 的 self-correction 到 Self-Guide 的 agent self-guidance，指出现有方法均为 always-on verification。引出 Self-Verification Dilemma 的实证发现：大多数 verification 是浪费的。\n\n2. **RL for interactive agents** — 从 GRPO 到 GiGPO/SPEAR/SDAR 的进展，指出 credit assignment、exploration、dense reward 等问题被充分研究，但 verification as learnable action 尚未被探索。\n\n3. **Cost-aware / selective computation** — 从 Thinkless/AutoThink 的 adaptive reasoning depth 到 When To Solve When To Verify 的 compute allocation，指出 \"when to compute more\" 的思想尚未被应用到 interactive agent verification。\n\n4. **Our work: B-IAVR** — 位于三条线的交汇处：(a) 从线 1 继承 self-verification 能力 (b) 在线 2 的 ALFWorld/GRPO 生态中实现 (c) 用线 3 的 cost-aware 思想指导 selective verification policy。\n",
      "numLines": 235,
      "startLine": 1,
      "totalLines": 235
    }
  }
}
```

</details>

---

### Tool call

_source line 16_

<details open><summary>🔧 Tool call — Read · `toolu_01XvR5gvVD273sfKkqF63uJN`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/analysis/failure_taxonomy.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "12f481e3-4249-4909-b494-860766cbf5b8",
  "uuid": "b3c81d16-6de8-4718-b666-5c152d7aa8a1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RutUDz7KQNrG6PEc8QiGan",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1355,
      "cache_read_input_tokens": 24232,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1355
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

_source line 17 · 2026-05-15T18:43:11.254Z_

<details><summary>↩ Tool result · `toolu_01XvR5gvVD273sfKkqF63uJN`</summary>

````text
1	# Experiment Failure Taxonomy — cost-verify-agent-rl
2	
3	> 基于 51 个实验的系统分析 | 生成日期: 2026-05-15 | 数据来源: project registry + decisions.yaml + memory.md
4	
5	## 概览
6	
7	| 结论 | 数量 | 占比 |
8	|------|------|------|
9	| success | 3 | 5.9% |
10	| negative | 5 | 9.8% |
11	| failed | 28 | 54.9% |
12	| killed | 11 | 21.6% |
13	| N/A (preparing/pending) | 4 | 7.8% |
14	| **总计** | **51** | **100%** |
15	
16	排除 4 个未执行实验和 1 个运行中 (exp027)，46 个已结论实验中：
17	- 3 成功 (6.5%)
18	- 5 负向结果 (10.9%)
19	- 38 失败/终止 (82.6%)
20	
21	失败模式分布（38 个失败/终止实验，部分实验涉及多个类别）：
22	
23	| 失败类别 | 实验数 | 占失败总数 |
24	|----------|--------|-----------|
25	| 工程类 | 24 | 63.2% |
26	| GRPO 训练不稳定类 | 9 | 23.7% |
27	| SFT 格式/数据类 | 4 | 10.5% |
28	| 奖励设计类 | 3 | 7.9% |
29	
30	---
31	
32	## 1. 工程类失败 (24 个)
33	
34	### 1.1 早期环境/框架搭建失败 (7 个)
35	
36	| Exp ID | 失败描述 | 根因 | 修复 | 决策 |
37	|--------|---------|------|------|------|
38	| exp_001 | 训练启动失败 | 未知（早期搭建） | — | — |
39	| exp_001b | 训练启动失败 | 未知（早期搭建） | — | — |
40	| exp_002 | 训练启动失败 | 未知（早期搭建） | — | — |
41	| exp_003 | 95.3% invalid actions, pg_loss≈0 | Qwen3-1.7B 原生输出 `&lt;think>` 后不生成 `&lt;answer>` 标签，RAGEN 解析器正则要求 `&lt;answer>` | 修改解析器适配 Qwen3 格式 (D004) | D003, D004 |
42	| exp_003 (underscore) | 启动失败 | 早期配置错误 | — | — |
43	| exp_003_dryrun* (3个) | dry run 失败 | 早期配置调试 | — | — |
44	
45	**模式总结**: 项目启动期的框架适配问题。exp003 的 Qwen3 格式不兼容是最关键发现——95% invalid action 完全阻断了学习信号。修复后所有后续实验不再出现此问题。
46	
47	### 1.2 磁盘空间耗尽 (3 个)
48	
49	| Exp ID | 触发位置 | 磁盘路径 | 根因 | 修复 |
50	|--------|---------|---------|------|------|
51	| exp007 | step 10 | `/tmp` (30GB root) | Ray session 文件填满根分区 | `RAY_TMPDIR=/root/autodl-tmp/tmp` |
52	| exp010 | step 11 | `/tmp` (30GB root) | fast_downward 同样路径，修复未完全 | `TMPDIR=/root/autodl-tmp/tmp` |
53	| exp023c | step 9 | `/root/autodl-tmp` (94%, 233G/250G) | checkpoint + 模型文件累积 | 清理旧 checkpoint |
54	
55	**模式总结**: AutoDL 实例根分区仅 30GB，数据盘 250GB。两种磁盘满路径：(1) `/tmp` 被 Ray/PDDL planner 填满 (exp007/010)；(2) 数据盘被 checkpoint 累积填满 (exp023c)。D009 pre-flight checklist 中加入了 `df -h` 检查。
56	
57	### 1.3 依赖/版本不兼容 (2 个)
58	
59	| Exp ID | 错误 | 根因 | 修复 |
60	|--------|------|------|------|
61	| exp012 | `TypeError: EngineArgs.__init__() got unexpected keyword argument 'disable_mm_preprocessor_cache'` | vLLM 版本与 RAGEN 代码不兼容 | 固定 vLLM 版本 |
62	| exp023_grpo_parallel | `tatsu FailedToken: expecting 'action', got template "take {o} from {r}"` | val env_groups=16 加载了更多 ALFWorld game files，触发 PDDL parser 不兼容 | 降回 env_groups=4，使用 serial 模式 (exp023c) |
63	
64	### 1.4 错误入口点/配置参数 (4 个)
65	
66	| Exp ID | 错误 | 根因 | 修复 | 决策 |
67	|--------|------|------|------|------|
68	| exp012 | 使用 agent_proxy 而非 train.py | Worker 使用错误入口点 | 引入 pre-flight checklist | D009 |
69	| exp020 | `AssertionError: model_path doesn't contain "qwen"` | checkpoint 软链接路径不含 "qwen" 字符串 | 修改软链接命名 | — |
70	| exp020c | Hydra key path 错误 | 配置参数路径写错 | — | 放弃，转 exp020d |
71	| exp020d | 放弃 | exp020b 已证明 RAGEN 格式不兼容 | — | D021 |
72	
73	### 1.5 Ray/AutoDL 容器限制 (7 个)
74	
75	| Exp ID | 错误 | 根因 | 修复 |
76	|--------|------|------|------|
77	| exp013b | Raylet killed by cgroup OOM | Ray object_store 70GB + memory 164GB = 234GB > cgroup 220GB 限制 | env_groups 8→4 |
78	| exp013c | 预防性终止 | 确认同 exp013b 的 cgroup 根因 | 降 env_groups + 降 object_store |
79	| exp013d | RAY_object_store_memory 环境变量无效 | Ray 忽略环境变量，需通过 Hydra 配置 | 改用 Hydra config override |
80	| exp013e | `ActorUnavailableError: RPC Socket closed` | vLLM worker 在 val→train 切换时 memory peak 超限 | 禁用 Ray MemoryMonitor, 清理旧 session |
81	| exp025 | `ModuleNotFoundError` | 激活错误 conda 环境 (base vs verl-agent) | `which python` 验证 |
82	| exp025b | `EAGAIN: Resource temporarily unavailable` (36+ 次) | AutoDL cgroup pids.max=20480，verl-agent Ray 多进程超限 | 无法修复，放弃 verl-agent |
83	| exp025c | 同上 | pids.max 硬限制确认 | pivot 到 Track B cherry-pick |
84	
85	**模式总结**: AutoDL 容器两个硬限制阻碍了训练：(1) cgroup 内存 220GB，Ray 默认 object_store 分配可超限；(2) pids.max=20480，verl-agent 架构在此限制下不可行。最终导致 verl-agent 方案被放弃 (D028)，转向 cherry-pick step-independent rollout 到 RAGEN。6 次失败、10+ GPU-h 空转。
86	
87	### 1.6 监控/Cron 误判 (2 个)
88	
89	| Exp ID | 问题 | 根因 | 修复 | 决策 |
90	|--------|------|------|------|------|
91	| exp019_expert_sft_v2 | cron 报告 process dead | 监控了 shell wrapper PID 而非训练进程 PID | 监控正确 PID | — |
92	| exp026 | cron 5 次误判 failed，registry 标记 DONE(failed) | `WANDB_MODE=disabled` + 监控错误 PID | 启用 W&B + 监控正确 PID | D029, D033 |
93	
94	**模式总结**: 监控 PID 必须是实际训练进程（非 shell wrapper）。`WANDB_MODE=disabled` 与 cron 监控不兼容——已建立硬规则禁止同时使用 (memory.md)。
95	
96	### 1.7 资源冲突 (2 个)
97	
98	| Exp ID | 问题 | 根因 |
99	|--------|------|------|
100	| exp009 | response_mask assertion + GPU 冲突 | 与 exp010 同时占用 cuda:0+1，写同一 checkpoint 目录 |
101	| exp019c | GPU 被占用 | exp019b 的 nohup 进程仍在运行 |
102	
103	---
104	
105	## 2. GRPO 训练不稳定类 (9 个)
106	
107	### 2.1 稀疏奖励冷启动 / 零梯度死锁 (3 个)
108	
109	| Exp ID | 假设 | 关键配置 | 失败描述 | 根因 | 决策 |
110	|--------|------|---------|---------|------|------|
111	| exp012b | format_penalty=0 isolate impact | format_penalty=0, group_size=16, LR=1e-6 | step 6 success=8.59%, step 7 pg_loss=0, grad_norm 1.48→0.09 | format_penalty=0 消除了组内 reward 方差，GRPO 无梯度信号 | D010 |
112	| exp015 | 极低 LR 防 collapse | LR=1e-7, KL=0.1, grad_clip=1.0 | step 3-5 连续零梯度 | LR=1e-7 参数更新量 ~5e-12，模型行为无可观测变化 | D014 |
113	| exp016 | LR 折中方案 | LR=5e-7, KL=0.1, 从 exp015 恢复 | 12 步中 11 步 pg_loss=0, 仅 step 7 有 4.7% success | base success ~4.7% 太稀疏，GRPO 在此 sparsity 下无法产生有效学习 | D015, D016 |
114	
115	**模式总结**: LR 搜索区间穷尽 — 1e-6 (collapse) / 5e-7 (无效学习) / 1e-7 (零梯度)。根因不是超参选择，而是 base success rate (~1-5%) 过低，sparse binary reward 下 GRPO 无法产生有效梯度。最终 pivot 到 Expert SFT warmup (D016)。
116	
117	### 2.2 灾难性 collapse / 死亡螺旋 (3 个)
118	
119	| Exp ID | 假设 | 关键配置 | 峰值 → 崩塌 | 根因 | 决策 |
120	|--------|------|---------|------------|------|------|
121	| exp010 | 首次 GRPO after SFT | format_penalty=-0.1, LR=1e-6 | step 1 success=4.7% → step 10 success=0% | format_penalty 劫持梯度 + /tmp 磁盘满 | D007 |
122	| exp011 | exp010 从 step 10 恢复 | 同 exp010 reward config | — (preemptive kill) | 同 exp010 reward 问题会重复 | D007 |
123	| exp026 | step-independent GRPO | LR=1e-6, KL=0.01, env_groups=4 (64 rollouts), save_freq=25 | step 2 success=**32.81%** → step 4 success=**0%** | sparse reward + 小 env_groups → 全零 batch 概率高 → 负 advantage → 策略被推回 reference | D035, D036 |
124	
125	**模式总结**: 两种 collapse 机制：(1) format_penalty 梯度劫持（exp010/011）——模型优化格式而非任务；(2) 稀疏奖励死亡螺旋（exp026）——偶然的全零 batch 产生纯负 advantage，策略保守化 → success 进一步降低 → 恶性循环。exp026 的 save_freq=25 导致峰值 checkpoint 丢失，是最大教训。
126	
127	### 2.3 RAGEN full-history 导致的 entropy collapse (3 个)
128	
129	| Exp ID | 假设 | 关键配置 | 指标退化 | 根因 | 决策 |
130	|--------|------|---------|---------|------|------|
131	| exp020b | GRPO from SFT (20% baseline) | LR=5e-7, KL=0.1, sparse reward | entropy 0.107→0.042 (-61%), train success 18.75%→4.69%, val=0% 始终 | RAGEN full-history concatenation → context 随步数爆炸 → 1.7B 模型推理退化 | D022 |
132	| exp022 | GRPO from RAGEN SFT (25% baseline) | LR=5e-7, KL=0.5, sparse reward | action_is_valid 48.75% (远低于 SFT 87.5%) | 同上，KL=0.5 仅减缓退化未改变方向 | D025 |
133	| exp023c | Serial GRPO, 同 exp022 config | LR=5e-7, KL=0.5, serial mode | train success 29.7%→23.4%, entropy 下降, step 9 磁盘满 | 同上，8 步已显示退化趋势 | D025, D026 |
134	
135	**模式总结**: RAGEN 框架的 full-history concatenation 是 3/3 GRPO 退化的共因 (D025, D026)。KL 从 0.1 到 0.5 仅减缓退化速度，未改变方向。KL 仅 0.0005 时 success 已退化，说明是算法-任务结构性不匹配。Self-Guide 论文在 verl-agent (step-independent context) 上达到 72.7%，确认问题在 RAGEN 而非 GRPO 本身。这是 pivot 到 step-independent rollout cherry-pick 的核心依据。
136	
137	---
138	
139	## 3. SFT 数据/格式类 (4 个)
140	
141	### 3.1 训练数据格式与推理框架不匹配
142	
143	| Exp ID | 假设 | 问题 | 影响 | 修复 | 决策 |
144	|--------|------|------|------|------|------|
145	| exp017 | Expert trajectory SFT | expert 数据无 RAGEN `&lt;think>`/`&lt;answer>` 结构 | format_ok 100%→75%, valid 90%→63.8%, success 仅 5% | 两阶段 SFT：先 format SFT 再 expert SFT | D018 |
146	| exp019 | 修复 expert 数据 (v2) | move→put 替换方向错误，admissible_commands 中是 "move" 不是 "put" | 训练数据 2157 条错误替换，会恶化 valid | 保留 "move" 原样 + admissible actions augmentation | D019 |
147	| exp020b-d | SFT ckpt → RAGEN GRPO | SFT 数据无 Turn/State/Reward 包装，RAGEN eval 0% vs eval_sft_fast 20% | GRPO 从错误 baseline 启动，全程 val=0% | 将 SFT 数据转换为 RAGEN 格式重训 (exp021) | D021, D022 |
148	| exp021 | RAGEN 格式 SFT (v4) | 4-episode eval 报 25% success（高方差幸运值），16-episode eval 仅 6.25% | exp022 基于不可靠 baseline 启动 | 强制 ≥16 episodes eval (C003) | D024 |
149	
150	**模式总结**: SFT 数据必须严格对齐推理框架格式。eval_sft_fast 和 RAGEN val 是两个不同框架，结果不可比（exp019b: 20% vs 0%）。4-episode eval 方差过大，不可作为 pass/fail 判定依据——C003 约束由此而来。
151	
152	---
153	
154	## 4. 奖励设计类 (3 个)
155	
156	### 4.1 Format penalty 梯度劫持
157	
158	| Exp ID | 奖励配置 | 现象 | 根因 | 决策 |
159	|--------|---------|------|------|------|
160	| exp010 | format_penalty=-0.1/turn, success=10.0 | valid 58.8%→68.3% 但 success 4.7%→0% | 零 success group 中 format_penalty 是唯一 reward 方差来源，GRPO 梯度指向格式优化 | D007, D008 |
161	| exp011 | 同 exp010 | 预防性终止 | 同 exp010 | D007 |
162	
163	### 4.2 Dense reward gaming
164	
165	| Exp ID | 奖励配置 | 现象 | 根因 | 决策 |
166	|--------|---------|------|------|------|
167	| exp013f | valid_action_bonus=0.15/action, success=10.0, format_penalty=0 | valid 60%→97.5%, success→0%, reward_mean=4.388 ≈ 29×0.15 | dense reward 可被独立最大化：模型学会产生合法但无效动作循环，回避高风险 success | D012 |
168	
169	**模式总结**: 奖励设计面临两难——(1) format_penalty 在零 success 下劫持梯度；(2) unconditional dense bonus 被 gaming。Success-gated bonus 在 success≈0% 下退化为 sparse reward (D013)。最终方案：放弃 reward shaping，转向 step-independent rollout 从架构层面解决 credit assignment (D026)。
170	
171	---
172	
173	## 5. 跨实验关键发现
174	
175	### Pattern 1: LR-stability 不可能三角 — sparse reward + GRPO 无安全 LR 区间
176	LR=1e-6 → collapse (exp012b step 7), LR=5e-7 → 无效学习 (exp016), LR=1e-7 → 零梯度 (exp015)。三个量级均失败，证明 sparse binary reward 下 GRPO 的 LR 搜索是无解的——根因是 reward signal 本身不足。(涉及: exp012b, exp015, exp016; 决策: D014, D016)
177	
178	### Pattern 2: RAGEN full-history concatenation 是 GRPO 退化的结构性根因
179	3/3 RAGEN GRPO 实验 (exp020b/022/023c) 呈现一致退化模式：entropy 收缩 + success 退化 + KL 极低。KL 从 0.1 到 0.5 仅减缓退化。而 Self-Guide 论文使用 step-independent context 达到 72.7%。exp026 切换到 step-independent rollout 后，2 步内 train success 达 32.81%（前 3 次 RAGEN GRPO 从未超越 SFT baseline）。(涉及: exp020b, exp022, exp023c, exp026; 决策: D025, D026)
180	
181	### Pattern 3: AutoDL 容器限制是不可绕过的硬约束
182	cgroup pids.max=20480 (verl-agent 不可用) + 内存 220GB (Ray object_store 需手动限制) + 根分区 30GB (/tmp 极易满) + 数据盘 250GB (checkpoint 需主动清理)。6 次 verl-agent 尝试、10+ GPU-h 空转后确认。(涉及: exp025, exp025b, exp025c, exp007, exp010, exp013b-e; 决策: D028)
183	
184	### Pattern 4: 工程失败的可预防性
185	D009 pre-flight checklist 引入前：18 个实验仅 1 成功。多数失败为入口点错误 (exp012)、磁盘满 (exp007/010)、格式不兼容 (exp003) 等可在提交前拦截的问题。(涉及: exp003, exp007, exp010, exp012; 决策: D009)
186	
187	### Pattern 5: 4-episode eval 的高方差陷阱
188	exp021 两次 eval 严重矛盾：4-ep 25% vs 16-ep 6.25%。基于 4-ep 结果启动的 exp022 浪费了计算资源。C003 约束（≥16 episodes）由此建立。(涉及: exp021, exp022; 决策: D024)
189	
190	---
191	
192	## 6. 正向结论（已验证有效的配置/方法）
193	
194	### 发现 1: 两阶段 SFT 有效提升 ALFWorld baseline
195	- **方法**: 先 format SFT (exp008_sft) 教模型 RAGEN `&lt;think>`/`&lt;answer>` 格式，再 expert SFT (exp019b) 教 ALFWorld 任务知识
196	- **证据**: exp008_sft format_ok=100%, valid=90%; exp019b success=20%, format_ok=100%, valid=85.3%
197	- **关键因素**: admissible actions augmentation 是 success 从 5% (exp017, 无 augmentation) 到 20% (exp019b, 有 augmentation) 的关键差异
198	
199	### 发现 2: Step-independent rollout 突破 RAGEN GRPO 天花板
200	- **方法**: Cherry-pick verl-agent 的 step-independent context + discounted returns 到 RAGEN
201	- **证据**: exp026 step 1-2 train success 21.88%→32.81%（前 3 次 RAGEN GRPO 从未超越 SFT baseline 6.25%）
202	- **对比**: RAGEN GRPO (exp020b/022/023c) 均退化，step-independent (exp026) 2 步内突破
203	
204	### 发现 3: Qwen3 解析器适配方案有效且稳定
205	- **方法**: 修改 RAGEN 解析器适配 Qwen3 的 `&lt;think>` + 自然语言输出（无 `&lt;answer>` 标签）
206	- **证据**: exp003 invalid_action 95%→exp007 invalid_action 1.6%，修复后所有实验均不再出现此问题 (D004)
207	
208	### 发现 4: 跨框架 baseline 一致性验证
209	- **发现**: Qwen3-1.7B raw baseline success≈6.25%，在 RAGEN (exp021 16-ep eval) 和 verl-agent (exp025b val_before_train=6.2%) 中一致
210	- **意义**: 模型基础能力跨框架稳定，训练算法/框架是关键差异因素 (D028)
211	
212	---
213	
214	## 7. 对 exp027 的启示
215	
216	### 已规避的失败模式
217	
218	| 失败模式 | exp027 中的规避措施 | 来源 |
219	|----------|-------------------|------|
220	| 全零 batch 死亡螺旋 | env_groups 4→8 (128 rollouts)，降低全零概率 | exp026 |
221	| LR 过激导致 collapse | LR 1e-6→5e-7 | exp012b, exp026 |
222	| save_freq 过大丢 checkpoint | save_freq 25→5 | exp026 |
223	| format_penalty 梯度劫持 | 使用 invalid_action_penalty=0.1（非 format_penalty） | exp010/011 |
224	| RAGEN full-history context 爆炸 | 使用 step-independent context | exp020b/022/023c |
225	| 4-ep eval 误判 | val env_groups=16 (≥16 episodes) | exp021, C003 |
226	| WANDB_MODE=disabled cron 误判 | W&B 已启用 (run id: y7jiibqk) | exp026, D033 |
227	
228	### 仍需警惕的风险
229	
230	| 风险 | 原因 | 监控指标 |
231	|------|------|---------|
232	| 稀疏奖励死亡螺旋仍可能发生 | env_groups=8 降低但未消除全零 batch 概率，LR=5e-7 仍可能过激 | 连续 2 步 success=0% 即触发 fail 条件 |
233	| entropy bonus 可能引入新 gaming | 0.01 entropy bonus 是未经验证的新参数 | entropy 持续上升但 success 不跟随 |
234	| train-val gap | 所有 GRPO 实验均存在显著 train-val gap (exp023c: 29.7% vs 6.25%) | step 5 val 是关键判定点 |
235	| 磁盘空间 | checkpoint 每 5 步保存，50 步 = 10 个 checkpoint × ~3.3GB = 33GB | df -h 定期检查 |
236	| KL=0.005 可能过低 | exp022 KL=0.5 仍 collapse，但 step-independent 框架下行为可能不同 | KL 持续接近 0 预示策略退化 |
237	
238	---
239	
240	## 附录: 实验时间线
241	
242	```
243	Day 1 (05-13): exp_001 → exp003  [环境搭建 + Qwen3 格式发现]
244	Day 2 (05-14): exp007 → exp019b  [SFT pipeline + reward 设计迭代]
245	               - exp007-016: GRPO LR 搜索穷尽，pivot to SFT
246	               - exp010-013f: reward shaping 探索（penalty劫持 → gaming）
247	               - exp017-019b: Expert SFT 三版迭代
248	Day 3 (05-15): exp020 → exp027   [RAGEN GRPO 失败 → step-independent pivot]
249	               - exp020-023c: RAGEN GRPO 3/3 退化
250	               - exp025-025c: verl-agent 6次失败，放弃
251	               - exp026: step-independent 首次突破，但不稳定
252	               - exp027: 稳定化配置，运行中
253	```
254	
255	**总 GPU 时间估算**: ~120 GPU-h（含 verl-agent 空转 10+ GPU-h、exp013f 30 步完整 reward gaming 实验 ~3h、exp023c 8 步 ~0.8h 等）
256	
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "12f481e3-4249-4909-b494-860766cbf5b8",
  "uuid": "1f8207f6-5def-4bde-aa3b-7d9dca2b2a91",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/analysis/failure_taxonomy.md",
      "content": "# Experiment Failure Taxonomy — cost-verify-agent-rl\n\n> 基于 51 个实验的系统分析 | 生成日期: 2026-05-15 | 数据来源: project registry + decisions.yaml + memory.md\n\n## 概览\n\n| 结论 | 数量 | 占比 |\n|------|------|------|\n| success | 3 | 5.9% |\n| negative | 5 | 9.8% |\n| failed | 28 | 54.9% |\n| killed | 11 | 21.6% |\n| N/A (preparing/pending) | 4 | 7.8% |\n| **总计** | **51** | **100%** |\n\n排除 4 个未执行实验和 1 个运行中 (exp027)，46 个已结论实验中：\n- 3 成功 (6.5%)\n- 5 负向结果 (10.9%)\n- 38 失败/终止 (82.6%)\n\n失败模式分布（38 个失败/终止实验，部分实验涉及多个类别）：\n\n| 失败类别 | 实验数 | 占失败总数 |\n|----------|--------|-----------|\n| 工程类 | 24 | 63.2% |\n| GRPO 训练不稳定类 | 9 | 23.7% |\n| SFT 格式/数据类 | 4 | 10.5% |\n| 奖励设计类 | 3 | 7.9% |\n\n---\n\n## 1. 工程类失败 (24 个)\n\n### 1.1 早期环境/框架搭建失败 (7 个)\n\n| Exp ID | 失败描述 | 根因 | 修复 | 决策 |\n|--------|---------|------|------|------|\n| exp_001 | 训练启动失败 | 未知（早期搭建） | — | — |\n| exp_001b | 训练启动失败 | 未知（早期搭建） | — | — |\n| exp_002 | 训练启动失败 | 未知（早期搭建） | — | — |\n| exp_003 | 95.3% invalid actions, pg_loss≈0 | Qwen3-1.7B 原生输出 `&lt;think>` 后不生成 `&lt;answer>` 标签，RAGEN 解析器正则要求 `&lt;answer>` | 修改解析器适配 Qwen3 格式 (D004) | D003, D004 |\n| exp_003 (underscore) | 启动失败 | 早期配置错误 | — | — |\n| exp_003_dryrun* (3个) | dry run 失败 | 早期配置调试 | — | — |\n\n**模式总结**: 项目启动期的框架适配问题。exp003 的 Qwen3 格式不兼容是最关键发现——95% invalid action 完全阻断了学习信号。修复后所有后续实验不再出现此问题。\n\n### 1.2 磁盘空间耗尽 (3 个)\n\n| Exp ID | 触发位置 | 磁盘路径 | 根因 | 修复 |\n|--------|---------|---------|------|------|\n| exp007 | step 10 | `/tmp` (30GB root) | Ray session 文件填满根分区 | `RAY_TMPDIR=/root/autodl-tmp/tmp` |\n| exp010 | step 11 | `/tmp` (30GB root) | fast_downward 同样路径，修复未完全 | `TMPDIR=/root/autodl-tmp/tmp` |\n| exp023c | step 9 | `/root/autodl-tmp` (94%, 233G/250G) | checkpoint + 模型文件累积 | 清理旧 checkpoint |\n\n**模式总结**: AutoDL 实例根分区仅 30GB，数据盘 250GB。两种磁盘满路径：(1) `/tmp` 被 Ray/PDDL planner 填满 (exp007/010)；(2) 数据盘被 checkpoint 累积填满 (exp023c)。D009 pre-flight checklist 中加入了 `df -h` 检查。\n\n### 1.3 依赖/版本不兼容 (2 个)\n\n| Exp ID | 错误 | 根因 | 修复 |\n|--------|------|------|------|\n| exp012 | `TypeError: EngineArgs.__init__() got unexpected keyword argument 'disable_mm_preprocessor_cache'` | vLLM 版本与 RAGEN 代码不兼容 | 固定 vLLM 版本 |\n| exp023_grpo_parallel | `tatsu FailedToken: expecting 'action', got template \"take {o} from {r}\"` | val env_groups=16 加载了更多 ALFWorld game files，触发 PDDL parser 不兼容 | 降回 env_groups=4，使用 serial 模式 (exp023c) |\n\n### 1.4 错误入口点/配置参数 (4 个)\n\n| Exp ID | 错误 | 根因 | 修复 | 决策 |\n|--------|------|------|------|------|\n| exp012 | 使用 agent_proxy 而非 train.py | Worker 使用错误入口点 | 引入 pre-flight checklist | D009 |\n| exp020 | `AssertionError: model_path doesn't contain \"qwen\"` | checkpoint 软链接路径不含 \"qwen\" 字符串 | 修改软链接命名 | — |\n| exp020c | Hydra key path 错误 | 配置参数路径写错 | — | 放弃，转 exp020d |\n| exp020d | 放弃 | exp020b 已证明 RAGEN 格式不兼容 | — | D021 |\n\n### 1.5 Ray/AutoDL 容器限制 (7 个)\n\n| Exp ID | 错误 | 根因 | 修复 |\n|--------|------|------|------|\n| exp013b | Raylet killed by cgroup OOM | Ray object_store 70GB + memory 164GB = 234GB > cgroup 220GB 限制 | env_groups 8→4 |\n| exp013c | 预防性终止 | 确认同 exp013b 的 cgroup 根因 | 降 env_groups + 降 object_store |\n| exp013d | RAY_object_store_memory 环境变量无效 | Ray 忽略环境变量，需通过 Hydra 配置 | 改用 Hydra config override |\n| exp013e | `ActorUnavailableError: RPC Socket closed` | vLLM worker 在 val→train 切换时 memory peak 超限 | 禁用 Ray MemoryMonitor, 清理旧 session |\n| exp025 | `ModuleNotFoundError` | 激活错误 conda 环境 (base vs verl-agent) | `which python` 验证 |\n| exp025b | `EAGAIN: Resource temporarily unavailable` (36+ 次) | AutoDL cgroup pids.max=20480，verl-agent Ray 多进程超限 | 无法修复，放弃 verl-agent |\n| exp025c | 同上 | pids.max 硬限制确认 | pivot 到 Track B cherry-pick |\n\n**模式总结**: AutoDL 容器两个硬限制阻碍了训练：(1) cgroup 内存 220GB，Ray 默认 object_store 分配可超限；(2) pids.max=20480，verl-agent 架构在此限制下不可行。最终导致 verl-agent 方案被放弃 (D028)，转向 cherry-pick step-independent rollout 到 RAGEN。6 次失败、10+ GPU-h 空转。\n\n### 1.6 监控/Cron 误判 (2 个)\n\n| Exp ID | 问题 | 根因 | 修复 | 决策 |\n|--------|------|------|------|------|\n| exp019_expert_sft_v2 | cron 报告 process dead | 监控了 shell wrapper PID 而非训练进程 PID | 监控正确 PID | — |\n| exp026 | cron 5 次误判 failed，registry 标记 DONE(failed) | `WANDB_MODE=disabled` + 监控错误 PID | 启用 W&B + 监控正确 PID | D029, D033 |\n\n**模式总结**: 监控 PID 必须是实际训练进程（非 shell wrapper）。`WANDB_MODE=disabled` 与 cron 监控不兼容——已建立硬规则禁止同时使用 (memory.md)。\n\n### 1.7 资源冲突 (2 个)\n\n| Exp ID | 问题 | 根因 |\n|--------|------|------|\n| exp009 | response_mask assertion + GPU 冲突 | 与 exp010 同时占用 cuda:0+1，写同一 checkpoint 目录 |\n| exp019c | GPU 被占用 | exp019b 的 nohup 进程仍在运行 |\n\n---\n\n## 2. GRPO 训练不稳定类 (9 个)\n\n### 2.1 稀疏奖励冷启动 / 零梯度死锁 (3 个)\n\n| Exp ID | 假设 | 关键配置 | 失败描述 | 根因 | 决策 |\n|--------|------|---------|---------|------|------|\n| exp012b | format_penalty=0 isolate impact | format_penalty=0, group_size=16, LR=1e-6 | step 6 success=8.59%, step 7 pg_loss=0, grad_norm 1.48→0.09 | format_penalty=0 消除了组内 reward 方差，GRPO 无梯度信号 | D010 |\n| exp015 | 极低 LR 防 collapse | LR=1e-7, KL=0.1, grad_clip=1.0 | step 3-5 连续零梯度 | LR=1e-7 参数更新量 ~5e-12，模型行为无可观测变化 | D014 |\n| exp016 | LR 折中方案 | LR=5e-7, KL=0.1, 从 exp015 恢复 | 12 步中 11 步 pg_loss=0, 仅 step 7 有 4.7% success | base success ~4.7% 太稀疏，GRPO 在此 sparsity 下无法产生有效学习 | D015, D016 |\n\n**模式总结**: LR 搜索区间穷尽 — 1e-6 (collapse) / 5e-7 (无效学习) / 1e-7 (零梯度)。根因不是超参选择，而是 base success rate (~1-5%) 过低，sparse binary reward 下 GRPO 无法产生有效梯度。最终 pivot 到 Expert SFT warmup (D016)。\n\n### 2.2 灾难性 collapse / 死亡螺旋 (3 个)\n\n| Exp ID | 假设 | 关键配置 | 峰值 → 崩塌 | 根因 | 决策 |\n|--------|------|---------|------------|------|------|\n| exp010 | 首次 GRPO after SFT | format_penalty=-0.1, LR=1e-6 | step 1 success=4.7% → step 10 success=0% | format_penalty 劫持梯度 + /tmp 磁盘满 | D007 |\n| exp011 | exp010 从 step 10 恢复 | 同 exp010 reward config | — (preemptive kill) | 同 exp010 reward 问题会重复 | D007 |\n| exp026 | step-independent GRPO | LR=1e-6, KL=0.01, env_groups=4 (64 rollouts), save_freq=25 | step 2 success=**32.81%** → step 4 success=**0%** | sparse reward + 小 env_groups → 全零 batch 概率高 → 负 advantage → 策略被推回 reference | D035, D036 |\n\n**模式总结**: 两种 collapse 机制：(1) format_penalty 梯度劫持（exp010/011）——模型优化格式而非任务；(2) 稀疏奖励死亡螺旋（exp026）——偶然的全零 batch 产生纯负 advantage，策略保守化 → success 进一步降低 → 恶性循环。exp026 的 save_freq=25 导致峰值 checkpoint 丢失，是最大教训。\n\n### 2.3 RAGEN full-history 导致的 entropy collapse (3 个)\n\n| Exp ID | 假设 | 关键配置 | 指标退化 | 根因 | 决策 |\n|--------|------|---------|---------|------|------|\n| exp020b | GRPO from SFT (20% baseline) | LR=5e-7, KL=0.1, sparse reward | entropy 0.107→0.042 (-61%), train success 18.75%→4.69%, val=0% 始终 | RAGEN full-history concatenation → context 随步数爆炸 → 1.7B 模型推理退化 | D022 |\n| exp022 | GRPO from RAGEN SFT (25% baseline) | LR=5e-7, KL=0.5, sparse reward | action_is_valid 48.75% (远低于 SFT 87.5%) | 同上，KL=0.5 仅减缓退化未改变方向 | D025 |\n| exp023c | Serial GRPO, 同 exp022 config | LR=5e-7, KL=0.5, serial mode | train success 29.7%→23.4%, entropy 下降, step 9 磁盘满 | 同上，8 步已显示退化趋势 | D025, D026 |\n\n**模式总结**: RAGEN 框架的 full-history concatenation 是 3/3 GRPO 退化的共因 (D025, D026)。KL 从 0.1 到 0.5 仅减缓退化速度，未改变方向。KL 仅 0.0005 时 success 已退化，说明是算法-任务结构性不匹配。Self-Guide 论文在 verl-agent (step-independent context) 上达到 72.7%，确认问题在 RAGEN 而非 GRPO 本身。这是 pivot 到 step-independent rollout cherry-pick 的核心依据。\n\n---\n\n## 3. SFT 数据/格式类 (4 个)\n\n### 3.1 训练数据格式与推理框架不匹配\n\n| Exp ID | 假设 | 问题 | 影响 | 修复 | 决策 |\n|--------|------|------|------|------|------|\n| exp017 | Expert trajectory SFT | expert 数据无 RAGEN `&lt;think>`/`&lt;answer>` 结构 | format_ok 100%→75%, valid 90%→63.8%, success 仅 5% | 两阶段 SFT：先 format SFT 再 expert SFT | D018 |\n| exp019 | 修复 expert 数据 (v2) | move→put 替换方向错误，admissible_commands 中是 \"move\" 不是 \"put\" | 训练数据 2157 条错误替换，会恶化 valid | 保留 \"move\" 原样 + admissible actions augmentation | D019 |\n| exp020b-d | SFT ckpt → RAGEN GRPO | SFT 数据无 Turn/State/Reward 包装，RAGEN eval 0% vs eval_sft_fast 20% | GRPO 从错误 baseline 启动，全程 val=0% | 将 SFT 数据转换为 RAGEN 格式重训 (exp021) | D021, D022 |\n| exp021 | RAGEN 格式 SFT (v4) | 4-episode eval 报 25% success（高方差幸运值），16-episode eval 仅 6.25% | exp022 基于不可靠 baseline 启动 | 强制 ≥16 episodes eval (C003) | D024 |\n\n**模式总结**: SFT 数据必须严格对齐推理框架格式。eval_sft_fast 和 RAGEN val 是两个不同框架，结果不可比（exp019b: 20% vs 0%）。4-episode eval 方差过大，不可作为 pass/fail 判定依据——C003 约束由此而来。\n\n---\n\n## 4. 奖励设计类 (3 个)\n\n### 4.1 Format penalty 梯度劫持\n\n| Exp ID | 奖励配置 | 现象 | 根因 | 决策 |\n|--------|---------|------|------|------|\n| exp010 | format_penalty=-0.1/turn, success=10.0 | valid 58.8%→68.3% 但 success 4.7%→0% | 零 success group 中 format_penalty 是唯一 reward 方差来源，GRPO 梯度指向格式优化 | D007, D008 |\n| exp011 | 同 exp010 | 预防性终止 | 同 exp010 | D007 |\n\n### 4.2 Dense reward gaming\n\n| Exp ID | 奖励配置 | 现象 | 根因 | 决策 |\n|--------|---------|------|------|------|\n| exp013f | valid_action_bonus=0.15/action, success=10.0, format_penalty=0 | valid 60%→97.5%, success→0%, reward_mean=4.388 ≈ 29×0.15 | dense reward 可被独立最大化：模型学会产生合法但无效动作循环，回避高风险 success | D012 |\n\n**模式总结**: 奖励设计面临两难——(1) format_penalty 在零 success 下劫持梯度；(2) unconditional dense bonus 被 gaming。Success-gated bonus 在 success≈0% 下退化为 sparse reward (D013)。最终方案：放弃 reward shaping，转向 step-independent rollout 从架构层面解决 credit assignment (D026)。\n\n---\n\n## 5. 跨实验关键发现\n\n### Pattern 1: LR-stability 不可能三角 — sparse reward + GRPO 无安全 LR 区间\nLR=1e-6 → collapse (exp012b step 7), LR=5e-7 → 无效学习 (exp016), LR=1e-7 → 零梯度 (exp015)。三个量级均失败，证明 sparse binary reward 下 GRPO 的 LR 搜索是无解的——根因是 reward signal 本身不足。(涉及: exp012b, exp015, exp016; 决策: D014, D016)\n\n### Pattern 2: RAGEN full-history concatenation 是 GRPO 退化的结构性根因\n3/3 RAGEN GRPO 实验 (exp020b/022/023c) 呈现一致退化模式：entropy 收缩 + success 退化 + KL 极低。KL 从 0.1 到 0.5 仅减缓退化。而 Self-Guide 论文使用 step-independent context 达到 72.7%。exp026 切换到 step-independent rollout 后，2 步内 train success 达 32.81%（前 3 次 RAGEN GRPO 从未超越 SFT baseline）。(涉及: exp020b, exp022, exp023c, exp026; 决策: D025, D026)\n\n### Pattern 3: AutoDL 容器限制是不可绕过的硬约束\ncgroup pids.max=20480 (verl-agent 不可用) + 内存 220GB (Ray object_store 需手动限制) + 根分区 30GB (/tmp 极易满) + 数据盘 250GB (checkpoint 需主动清理)。6 次 verl-agent 尝试、10+ GPU-h 空转后确认。(涉及: exp025, exp025b, exp025c, exp007, exp010, exp013b-e; 决策: D028)\n\n### Pattern 4: 工程失败的可预防性\nD009 pre-flight checklist 引入前：18 个实验仅 1 成功。多数失败为入口点错误 (exp012)、磁盘满 (exp007/010)、格式不兼容 (exp003) 等可在提交前拦截的问题。(涉及: exp003, exp007, exp010, exp012; 决策: D009)\n\n### Pattern 5: 4-episode eval 的高方差陷阱\nexp021 两次 eval 严重矛盾：4-ep 25% vs 16-ep 6.25%。基于 4-ep 结果启动的 exp022 浪费了计算资源。C003 约束（≥16 episodes）由此建立。(涉及: exp021, exp022; 决策: D024)\n\n---\n\n## 6. 正向结论（已验证有效的配置/方法）\n\n### 发现 1: 两阶段 SFT 有效提升 ALFWorld baseline\n- **方法**: 先 format SFT (exp008_sft) 教模型 RAGEN `&lt;think>`/`&lt;answer>` 格式，再 expert SFT (exp019b) 教 ALFWorld 任务知识\n- **证据**: exp008_sft format_ok=100%, valid=90%; exp019b success=20%, format_ok=100%, valid=85.3%\n- **关键因素**: admissible actions augmentation 是 success 从 5% (exp017, 无 augmentation) 到 20% (exp019b, 有 augmentation) 的关键差异\n\n### 发现 2: Step-independent rollout 突破 RAGEN GRPO 天花板\n- **方法**: Cherry-pick verl-agent 的 step-independent context + discounted returns 到 RAGEN\n- **证据**: exp026 step 1-2 train success 21.88%→32.81%（前 3 次 RAGEN GRPO 从未超越 SFT baseline 6.25%）\n- **对比**: RAGEN GRPO (exp020b/022/023c) 均退化，step-independent (exp026) 2 步内突破\n\n### 发现 3: Qwen3 解析器适配方案有效且稳定\n- **方法**: 修改 RAGEN 解析器适配 Qwen3 的 `&lt;think>` + 自然语言输出（无 `&lt;answer>` 标签）\n- **证据**: exp003 invalid_action 95%→exp007 invalid_action 1.6%，修复后所有实验均不再出现此问题 (D004)\n\n### 发现 4: 跨框架 baseline 一致性验证\n- **发现**: Qwen3-1.7B raw baseline success≈6.25%，在 RAGEN (exp021 16-ep eval) 和 verl-agent (exp025b val_before_train=6.2%) 中一致\n- **意义**: 模型基础能力跨框架稳定，训练算法/框架是关键差异因素 (D028)\n\n---\n\n## 7. 对 exp027 的启示\n\n### 已规避的失败模式\n\n| 失败模式 | exp027 中的规避措施 | 来源 |\n|----------|-------------------|------|\n| 全零 batch 死亡螺旋 | env_groups 4→8 (128 rollouts)，降低全零概率 | exp026 |\n| LR 过激导致 collapse | LR 1e-6→5e-7 | exp012b, exp026 |\n| save_freq 过大丢 checkpoint | save_freq 25→5 | exp026 |\n| format_penalty 梯度劫持 | 使用 invalid_action_penalty=0.1（非 format_penalty） | exp010/011 |\n| RAGEN full-history context 爆炸 | 使用 step-independent context | exp020b/022/023c |\n| 4-ep eval 误判 | val env_groups=16 (≥16 episodes) | exp021, C003 |\n| WANDB_MODE=disabled cron 误判 | W&B 已启用 (run id: y7jiibqk) | exp026, D033 |\n\n### 仍需警惕的风险\n\n| 风险 | 原因 | 监控指标 |\n|------|------|---------|\n| 稀疏奖励死亡螺旋仍可能发生 | env_groups=8 降低但未消除全零 batch 概率，LR=5e-7 仍可能过激 | 连续 2 步 success=0% 即触发 fail 条件 |\n| entropy bonus 可能引入新 gaming | 0.01 entropy bonus 是未经验证的新参数 | entropy 持续上升但 success 不跟随 |\n| train-val gap | 所有 GRPO 实验均存在显著 train-val gap (exp023c: 29.7% vs 6.25%) | step 5 val 是关键判定点 |\n| 磁盘空间 | checkpoint 每 5 步保存，50 步 = 10 个 checkpoint × ~3.3GB = 33GB | df -h 定期检查 |\n| KL=0.005 可能过低 | exp022 KL=0.5 仍 collapse，但 step-independent 框架下行为可能不同 | KL 持续接近 0 预示策略退化 |\n\n---\n\n## 附录: 实验时间线\n\n```\nDay 1 (05-13): exp_001 → exp003  [环境搭建 + Qwen3 格式发现]\nDay 2 (05-14): exp007 → exp019b  [SFT pipeline + reward 设计迭代]\n               - exp007-016: GRPO LR 搜索穷尽，pivot to SFT\n               - exp010-013f: reward shaping 探索（penalty劫持 → gaming）\n               - exp017-019b: Expert SFT 三版迭代\nDay 3 (05-15): exp020 → exp027   [RAGEN GRPO 失败 → step-independent pivot]\n               - exp020-023c: RAGEN GRPO 3/3 退化\n               - exp025-025c: verl-agent 6次失败，放弃\n               - exp026: step-independent 首次突破，但不稳定\n               - exp027: 稳定化配置，运行中\n```\n\n**总 GPU 时间估算**: ~120 GPU-h（含 verl-agent 空转 10+ GPU-h、exp013f 30 步完整 reward gaming 实验 ~3h、exp023c 8 步 ~0.8h 等）\n",
      "numLines": 256,
      "startLine": 1,
      "totalLines": 256
    }
  }
}
````

</details>

---

### Assistant

_source line 18_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the materials. Let me synthesize them into the framing draft.

Key facts:
1. **Project**: B-IAVR (Behavior-Informed Active Verification via RL)
2. **Core method**: Train interactive agent to learn WHEN to self-verify, using action change as reward signal for verification informativeness
3. **Framework**: Self-Guide + Qwen3-1.7B + ALFWorld + GRPO
4. **Framing locked (D039)**: Cost-efficiency story, NOT performance story
5. **Current state**: exp027 running (MVP phase), 51 experiments with 82.6% failure rate


6. **Key competitors**: Self-Guide (always-on), Thinkless (RL "when to think"), ARES (self-eval for RAG)

The core insight is that while self-verification improves reliability, most verification steps are redundant—they don't actually change what the agent does. I'm framing this as an RL approach that learns to verify selectively, only when verification would likely shift the agent's behavior, achieving the same performance at much lower cost. The strongest claim is the cost-efficiency angle: RL-trained selective verification reduces verification overhead while maintaining task performance. The secondary claim validates that action change works as a reward signal for measuring verification informativeness.

Now I'm thinking through the reviewer concerns that could undermine this framing. The evaluation is limited to ALFWorld, which raises questions about whether this generalizes. There's also a significant performance gap compared to Self-Guide's 72.7% versus our current results. The bigger methodological question is whether action change actually captures verification quality or if it's just picking up on agent instability. And there's the risk that this looks too incremental—essentially just adding a gate to Self-Guide's approach.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "12f481e3-4249-4909-b494-860766cbf5b8",
  "uuid": "abbd621c-6b7e-4c6d-8091-87b03f94bc23",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BZbk9aai4kce4FqKgoLWVN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21358,
      "cache_read_input_tokens": 25587,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 21358
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

全部材料已读取。开始撰写 framing 草稿。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "12f481e3-4249-4909-b494-860766cbf5b8",
  "uuid": "58a88542-5212-4b87-a06a-0b023d669dd0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BZbk9aai4kce4FqKgoLWVN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21358,
      "cache_read_input_tokens": 25587,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 21358
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

<details open><summary>🔧 Tool call — Write · `toolu_01NhfiPyTsRvQwjRLgTaCEy8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/docs/framing_draft.md",
  "content": "# B-IAVR Paper Framing Draft\n\n> 草稿日期: 2026-05-15 | 状态: 素材级，待 Director 审阅\n\n## Core Insight\n\nSelf-verification improves interactive agent reliability, but empirical evidence shows most verification steps are confirmatory rather than corrective—they consume compute without changing the agent's behavior. We show that RL can train agents to selectively verify only when verification is likely informative, using action change (whether the agent's next action differs after verification) as a natural cost-benefit signal, achieving comparable task performance at significantly reduced verification cost.\n\n## Core Claims（按强度排序）\n\n### Claim 1 (最强): RL-trained selective verification reduces verification cost while preserving task performance\n\n- 强度级别: **moderate**（需 exp027 pass + Phase B 完成后升级为 strong）\n- 所需最低实验证据:\n  - (a) Always-on Self-Guide baseline: ALFWorld success ≥ 50%（exp027 → Phase B prerequisite）\n  - (b) B-IAVR selective policy: success within 5% of always-on baseline, verification frequency ↓ ≥ 40%\n  - (c) Cost-performance Pareto curve: B-IAVR dominates always-on 在 cost-accuracy tradeoff 上\n- 当前证据状态: **缺失**。exp027 仍在训练 always-on baseline（MVP 阈值 20%）。Phase B（selective policy）尚未启动。当前 SFT baseline 仅 6.25%。\n\n### Claim 2: Action change 是 verification informativeness 的有效 reward signal\n\n- 强度级别: **moderate**\n- 所需最低实验证据:\n  - (a) Action change reward 下 GRPO 收敛且学到非平凡 verification policy（非全开/全关）\n  - (b) Ablation: action change reward vs. random verification vs. fixed-frequency verification\n  - (c) 分析: action change 与 episode outcome 的相关性（验证 action change 确实指示 informative verification）\n- 当前证据状态: **缺失**。Action change reward 仅存在于代码设计中，未经训练验证。\n\n### Claim 3: Learned selective verification outperforms heuristic baselines\n\n- 强度级别: **weak**（需完整 ablation）\n- 所需最低实验证据:\n  - (a) B-IAVR vs. always-on (Self-Guide): 性能相当但 cost 低\n  - (b) B-IAVR vs. no-verification: 性能优势显著\n  - (c) B-IAVR vs. random-p verification (p = B-IAVR 的平均 verify rate): 性能优势证明 learned policy > random at same budget\n  - (d) B-IAVR vs. confidence-threshold heuristic: 性能优势证明 learned > hand-crafted\n- 当前证据状态: **缺失**。所有 baseline 对比需 Phase B 完成后才能进行。\n\n## Anticipated Reviewer Concerns（至少 3 条）\n\n### Concern 1: Single-environment evaluation (ALFWorld only) — generalizability 存疑\n\n- 可能的攻击角度: \"Results on ALFWorld alone cannot support claims about interactive agents in general. ALFWorld is a text-based household environment with a discrete action space; it is unclear whether the findings transfer to web agents, code agents, or continuous-control settings.\"\n- 应对策略:\n  - (primary) 坦承 limitation，argue ALFWorld 是 interactive agent RL 的 standard testbed（GiGPO, SPEAR, SDAR, RWML 均用 ALFWorld），且 verification decision 的结构化特征（binary gate + action change signal）不依赖 ALFWorld-specific properties\n  - (secondary) 如果 GPU 预算允许，追加 WebShop 实验（同生态，verl-agent/RAGEN 均支持）\n- 需要的防御性实验: WebShop 上的 B-IAVR 复现（成本约 200-400 GPU-h，视 GPU 预算决定是否做）\n\n### Concern 2: Baseline performance insufficient — cost-efficiency claim 的前提脆弱\n\n- 可能的攻击角度: \"The cost-efficiency argument requires a strong baseline to be meaningful. If the always-on verification baseline only reaches 30% on ALFWorld (vs. Self-Guide's 72.7%), the 'reduced cost at similar performance' claim operates in a regime where the base system is already weak. Saving verification cost on a 30%-success agent is not practically interesting.\"\n- 应对策略:\n  - exp027 必须至少达到 50%+ 才能支撑 cost-efficiency story（D034 已设此阈值）\n  - 如果 exp027 仅达 20-30%，需要追加训练（更多 steps、curriculum learning、或更大模型）直到 baseline ≥ 50%\n  - 明确定位为 \"same model size, same framework\"——不与 GPT-4 prompting 方法比绝对性能\n- 需要的防御性实验: Always-on baseline ≥ 50% success rate（这是 paper 的 hard prerequisite，非 nice-to-have）\n\n### Concern 3: Action change reward 的有效性——是在衡量 verification quality 还是 policy instability？\n\n- 可能的攻击角度: \"An agent that changes its action after verification might simply be unstable rather than informed. A noisy policy changes actions frequently regardless of verification quality. Action change conflates 'verification revealed useful information' with 'the policy is stochastic near the decision boundary'.\"\n- 应对策略:\n  - 分析 action change 与 episode success 的条件相关性：informative verification → action change → higher success rate。如果 action change 只是 noise，它不应与 success 正相关\n  - Ablation: 在 converged policy（低 entropy）上测量 action change rate，排除 stochasticity 解释\n  - 引入 \"verification gain\" 指标（Lu et al. 2025 的 verifier gain 概念），量化 action change 对 outcome 的因果贡献\n- 需要的防御性实验: (a) action change rate vs. success rate 散点图 + 相关性分析 (b) entropy-controlled action change 分析 (c) 理想情况下，causal intervention 实验（强制 verify / 不 verify，观察 outcome 差异）\n\n### Concern 4: Incremental contribution over Self-Guide — \"just adding a gate\"\n\n- 可能的攻击角度: \"This is Self-Guide with a learned binary gate prepended. The selective verification policy is a thin wrapper around an existing framework. The novelty is limited to the gating mechanism and the action-change reward signal.\"\n- 应对策略:\n  - 强调 \"when to verify\" 是一个与 \"how to verify\" 正交的研究问题，Self-Verification Dilemma (Long et al. 2026) 实证证明大多数 verification 是 confirmatory，这不是 trivial gating\n  - 类比 Thinkless: \"when to think\" 被 NeurIPS 2025 接收，证明 \"when to X\" 方向有独立学术价值\n  - Action change reward 是技术贡献，不是简单 gate——它提供了 verification informativeness 的 training signal，这在 interactive agent 文献中尚无先例\n- 需要的防御性实验: ablation 证明 learned gate > fixed-rate gate > always-on（在 cost-performance Pareto 上），表明 gate 的学习本身有价值\n\n## 与 ARES 的差异化论述\n\nARES (arXiv 2603.07915) 训练一个 SFT router 来分配 self-evaluation effort across RAG pipeline stages，其 verification target 是 retrieval quality 和 answer faithfulness 的连续打分。B-IAVR 与 ARES 有三个本质区别：(1) **决策粒度**——ARES 分配连续 effort（多少 compute 给 evaluation），B-IAVR 做 binary decision（verify or not verify this step），这是更简洁的 formulation，直接对应 agent 的 action-level decision；(2) **训练方法**——ARES 用 SFT 训练 router（supervised by 人工标注的 effort allocation），B-IAVR 用 RL 从 environment reward 中自动学习 verification policy，不需要人工标注 \"何时该 verify\"；(3) **应用场景**——ARES 面向 single-turn RAG pipeline 的 self-evaluation，B-IAVR 面向 multi-turn interactive agent 的 action verification，后者的 verification decision 与环境状态动态耦合（每一步的 verify 价值取决于当前 state 和历史 trajectory）。\n\n## 与 Thinkless 的差异化论述\n\nThinkless (NeurIPS 2025) 用 RL 训练 LLM 在两个 control token 间选择，决定 \"when to think deeply\" (long-form reasoning) vs. \"when to answer directly\" (short-form)。B-IAVR 与 Thinkless 共享 \"RL-trained adaptive computation\" 的 meta-framework，但在三个维度上不同：(1) **决策对象**——Thinkless 控制 reasoning depth（token 级 budget），B-IAVR 控制 verification action（action 级 decision）；(2) **reward signal**——Thinkless 的 reward 是 task correctness + length penalty（鼓励用短回答解决简单问题），B-IAVR 的 reward 是 action change（衡量 verification 是否改变了 agent 行为），这是一个 informativeness-aware signal 而非纯粹的 cost signal；(3) **交互模式**——Thinkless 面向 single-turn static reasoning task，B-IAVR 面向 multi-turn interactive agent，verification 的价值随 episode 推进动态变化（早期探索阶段 verify 价值可能高于后期执行阶段），这种时序依赖性是 static reasoning 中不存在的。DeGRPO 中 control token loss 解耦的技术可直接借鉴用于 B-IAVR 的 verify token 训练。\n\n## 论文叙事骨架（建议）\n\n**Introduction 逻辑线：**\n\n1. **问题**：Self-verification 已被证明能提升 LLM agent 的可靠性（Self-Guide, S²R, SCoRe）。然而，现有方法采用 always-on verification——每一步都验证，不区分验证是否有价值。\n\n2. **现有方案的不足**：这种 always-on 策略有两个问题。第一，计算浪费严重——Long et al. (2026) 实证发现大多数 self-verification 是 confirmatory 而非 corrective，不改变模型行为。第二，在 interactive agent 场景中，verification cost 与 environment interaction 耦合（每次 verify 消耗一个 interaction step 的 budget），浪费的 verification 直接挤压有效行动的空间。\n\n3. **我们的洞察**：Verification 的价值不均匀分布——agent 在某些 state 下验证后会改变行动（informative verification），在另一些 state 下验证后行动不变（confirmatory verification）。Action change——验证前后 agent 是否选择不同的下一步动作——是 verification informativeness 的天然指标。\n\n4. **方法概述**：我们提出 B-IAVR，在 Self-Guide 框架上增加一个 RL-trained binary gate，让 agent 在每一步决定是否触发 self-verification。训练使用 GRPO，reward signal 结合 task outcome 和 action change：当 verification 改变了后续行动（informative），给予正向 reward；当 verification 未改变行动（confirmatory），该 verification step 的 reward 为零或负。\n\n5. **关键结果**（待实验填充）：在 ALFWorld 上，B-IAVR 在 task success rate 与 always-on Self-Guide 相当的前提下，将 verification frequency 降低 X%，总 interaction steps 减少 Y%，在 cost-performance Pareto frontier 上严格优于 always-on baseline。Learned verification policy 展现出可解释的 pattern：agent 倾向于在高不确定性 state（如首次接触新物品、面临多选择）时 verify，在重复性执行阶段跳过 verification。\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "12f481e3-4249-4909-b494-860766cbf5b8",
  "uuid": "e463743c-5238-42b3-a87d-6c6248d95dee",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BZbk9aai4kce4FqKgoLWVN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21358,
      "cache_read_input_tokens": 25587,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 21358
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

_source line 21 · 2026-05-15T18:44:44.396Z_

<details><summary>↩ Tool result · `toolu_01NhfiPyTsRvQwjRLgTaCEy8`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/docs/framing_draft.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "12f481e3-4249-4909-b494-860766cbf5b8",
  "uuid": "8736bf80-2bfc-4779-b395-e3a3b5157a68",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/docs/framing_draft.md",
    "content": "# B-IAVR Paper Framing Draft\n\n> 草稿日期: 2026-05-15 | 状态: 素材级，待 Director 审阅\n\n## Core Insight\n\nSelf-verification improves interactive agent reliability, but empirical evidence shows most verification steps are confirmatory rather than corrective—they consume compute without changing the agent's behavior. We show that RL can train agents to selectively verify only when verification is likely informative, using action change (whether the agent's next action differs after verification) as a natural cost-benefit signal, achieving comparable task performance at significantly reduced verification cost.\n\n## Core Claims（按强度排序）\n\n### Claim 1 (最强): RL-trained selective verification reduces verification cost while preserving task performance\n\n- 强度级别: **moderate**（需 exp027 pass + Phase B 完成后升级为 strong）\n- 所需最低实验证据:\n  - (a) Always-on Self-Guide baseline: ALFWorld success ≥ 50%（exp027 → Phase B prerequisite）\n  - (b) B-IAVR selective policy: success within 5% of always-on baseline, verification frequency ↓ ≥ 40%\n  - (c) Cost-performance Pareto curve: B-IAVR dominates always-on 在 cost-accuracy tradeoff 上\n- 当前证据状态: **缺失**。exp027 仍在训练 always-on baseline（MVP 阈值 20%）。Phase B（selective policy）尚未启动。当前 SFT baseline 仅 6.25%。\n\n### Claim 2: Action change 是 verification informativeness 的有效 reward signal\n\n- 强度级别: **moderate**\n- 所需最低实验证据:\n  - (a) Action change reward 下 GRPO 收敛且学到非平凡 verification policy（非全开/全关）\n  - (b) Ablation: action change reward vs. random verification vs. fixed-frequency verification\n  - (c) 分析: action change 与 episode outcome 的相关性（验证 action change 确实指示 informative verification）\n- 当前证据状态: **缺失**。Action change reward 仅存在于代码设计中，未经训练验证。\n\n### Claim 3: Learned selective verification outperforms heuristic baselines\n\n- 强度级别: **weak**（需完整 ablation）\n- 所需最低实验证据:\n  - (a) B-IAVR vs. always-on (Self-Guide): 性能相当但 cost 低\n  - (b) B-IAVR vs. no-verification: 性能优势显著\n  - (c) B-IAVR vs. random-p verification (p = B-IAVR 的平均 verify rate): 性能优势证明 learned policy > random at same budget\n  - (d) B-IAVR vs. confidence-threshold heuristic: 性能优势证明 learned > hand-crafted\n- 当前证据状态: **缺失**。所有 baseline 对比需 Phase B 完成后才能进行。\n\n## Anticipated Reviewer Concerns（至少 3 条）\n\n### Concern 1: Single-environment evaluation (ALFWorld only) — generalizability 存疑\n\n- 可能的攻击角度: \"Results on ALFWorld alone cannot support claims about interactive agents in general. ALFWorld is a text-based household environment with a discrete action space; it is unclear whether the findings transfer to web agents, code agents, or continuous-control settings.\"\n- 应对策略:\n  - (primary) 坦承 limitation，argue ALFWorld 是 interactive agent RL 的 standard testbed（GiGPO, SPEAR, SDAR, RWML 均用 ALFWorld），且 verification decision 的结构化特征（binary gate + action change signal）不依赖 ALFWorld-specific properties\n  - (secondary) 如果 GPU 预算允许，追加 WebShop 实验（同生态，verl-agent/RAGEN 均支持）\n- 需要的防御性实验: WebShop 上的 B-IAVR 复现（成本约 200-400 GPU-h，视 GPU 预算决定是否做）\n\n### Concern 2: Baseline performance insufficient — cost-efficiency claim 的前提脆弱\n\n- 可能的攻击角度: \"The cost-efficiency argument requires a strong baseline to be meaningful. If the always-on verification baseline only reaches 30% on ALFWorld (vs. Self-Guide's 72.7%), the 'reduced cost at similar performance' claim operates in a regime where the base system is already weak. Saving verification cost on a 30%-success agent is not practically interesting.\"\n- 应对策略:\n  - exp027 必须至少达到 50%+ 才能支撑 cost-efficiency story（D034 已设此阈值）\n  - 如果 exp027 仅达 20-30%，需要追加训练（更多 steps、curriculum learning、或更大模型）直到 baseline ≥ 50%\n  - 明确定位为 \"same model size, same framework\"——不与 GPT-4 prompting 方法比绝对性能\n- 需要的防御性实验: Always-on baseline ≥ 50% success rate（这是 paper 的 hard prerequisite，非 nice-to-have）\n\n### Concern 3: Action change reward 的有效性——是在衡量 verification quality 还是 policy instability？\n\n- 可能的攻击角度: \"An agent that changes its action after verification might simply be unstable rather than informed. A noisy policy changes actions frequently regardless of verification quality. Action change conflates 'verification revealed useful information' with 'the policy is stochastic near the decision boundary'.\"\n- 应对策略:\n  - 分析 action change 与 episode success 的条件相关性：informative verification → action change → higher success rate。如果 action change 只是 noise，它不应与 success 正相关\n  - Ablation: 在 converged policy（低 entropy）上测量 action change rate，排除 stochasticity 解释\n  - 引入 \"verification gain\" 指标（Lu et al. 2025 的 verifier gain 概念），量化 action change 对 outcome 的因果贡献\n- 需要的防御性实验: (a) action change rate vs. success rate 散点图 + 相关性分析 (b) entropy-controlled action change 分析 (c) 理想情况下，causal intervention 实验（强制 verify / 不 verify，观察 outcome 差异）\n\n### Concern 4: Incremental contribution over Self-Guide — \"just adding a gate\"\n\n- 可能的攻击角度: \"This is Self-Guide with a learned binary gate prepended. The selective verification policy is a thin wrapper around an existing framework. The novelty is limited to the gating mechanism and the action-change reward signal.\"\n- 应对策略:\n  - 强调 \"when to verify\" 是一个与 \"how to verify\" 正交的研究问题，Self-Verification Dilemma (Long et al. 2026) 实证证明大多数 verification 是 confirmatory，这不是 trivial gating\n  - 类比 Thinkless: \"when to think\" 被 NeurIPS 2025 接收，证明 \"when to X\" 方向有独立学术价值\n  - Action change reward 是技术贡献，不是简单 gate——它提供了 verification informativeness 的 training signal，这在 interactive agent 文献中尚无先例\n- 需要的防御性实验: ablation 证明 learned gate > fixed-rate gate > always-on（在 cost-performance Pareto 上），表明 gate 的学习本身有价值\n\n## 与 ARES 的差异化论述\n\nARES (arXiv 2603.07915) 训练一个 SFT router 来分配 self-evaluation effort across RAG pipeline stages，其 verification target 是 retrieval quality 和 answer faithfulness 的连续打分。B-IAVR 与 ARES 有三个本质区别：(1) **决策粒度**——ARES 分配连续 effort（多少 compute 给 evaluation），B-IAVR 做 binary decision（verify or not verify this step），这是更简洁的 formulation，直接对应 agent 的 action-level decision；(2) **训练方法**——ARES 用 SFT 训练 router（supervised by 人工标注的 effort allocation），B-IAVR 用 RL 从 environment reward 中自动学习 verification policy，不需要人工标注 \"何时该 verify\"；(3) **应用场景**——ARES 面向 single-turn RAG pipeline 的 self-evaluation，B-IAVR 面向 multi-turn interactive agent 的 action verification，后者的 verification decision 与环境状态动态耦合（每一步的 verify 价值取决于当前 state 和历史 trajectory）。\n\n## 与 Thinkless 的差异化论述\n\nThinkless (NeurIPS 2025) 用 RL 训练 LLM 在两个 control token 间选择，决定 \"when to think deeply\" (long-form reasoning) vs. \"when to answer directly\" (short-form)。B-IAVR 与 Thinkless 共享 \"RL-trained adaptive computation\" 的 meta-framework，但在三个维度上不同：(1) **决策对象**——Thinkless 控制 reasoning depth（token 级 budget），B-IAVR 控制 verification action（action 级 decision）；(2) **reward signal**——Thinkless 的 reward 是 task correctness + length penalty（鼓励用短回答解决简单问题），B-IAVR 的 reward 是 action change（衡量 verification 是否改变了 agent 行为），这是一个 informativeness-aware signal 而非纯粹的 cost signal；(3) **交互模式**——Thinkless 面向 single-turn static reasoning task，B-IAVR 面向 multi-turn interactive agent，verification 的价值随 episode 推进动态变化（早期探索阶段 verify 价值可能高于后期执行阶段），这种时序依赖性是 static reasoning 中不存在的。DeGRPO 中 control token loss 解耦的技术可直接借鉴用于 B-IAVR 的 verify token 训练。\n\n## 论文叙事骨架（建议）\n\n**Introduction 逻辑线：**\n\n1. **问题**：Self-verification 已被证明能提升 LLM agent 的可靠性（Self-Guide, S²R, SCoRe）。然而，现有方法采用 always-on verification——每一步都验证，不区分验证是否有价值。\n\n2. **现有方案的不足**：这种 always-on 策略有两个问题。第一，计算浪费严重——Long et al. (2026) 实证发现大多数 self-verification 是 confirmatory 而非 corrective，不改变模型行为。第二，在 interactive agent 场景中，verification cost 与 environment interaction 耦合（每次 verify 消耗一个 interaction step 的 budget），浪费的 verification 直接挤压有效行动的空间。\n\n3. **我们的洞察**：Verification 的价值不均匀分布——agent 在某些 state 下验证后会改变行动（informative verification），在另一些 state 下验证后行动不变（confirmatory verification）。Action change——验证前后 agent 是否选择不同的下一步动作——是 verification informativeness 的天然指标。\n\n4. **方法概述**：我们提出 B-IAVR，在 Self-Guide 框架上增加一个 RL-trained binary gate，让 agent 在每一步决定是否触发 self-verification。训练使用 GRPO，reward signal 结合 task outcome 和 action change：当 verification 改变了后续行动（informative），给予正向 reward；当 verification 未改变行动（confirmatory），该 verification step 的 reward 为零或负。\n\n5. **关键结果**（待实验填充）：在 ALFWorld 上，B-IAVR 在 task success rate 与 always-on Self-Guide 相当的前提下，将 verification frequency 降低 X%，总 interaction steps 减少 Y%，在 cost-performance Pareto frontier 上严格优于 always-on baseline。Learned verification policy 展现出可解释的 pattern：agent 倾向于在高不确定性 state（如首次接触新物品、面临多选择）时 verify，在重复性执行阶段跳过 verification。\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Tool call

_source line 22_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01N5mLX7D8naPseVrvrXz83B`</summary>

```json
{
  "name": "framing_draft",
  "type": "report",
  "description": "B-IAVR paper framing draft: core insight, 3 claims with evidence requirements, 4 reviewer concerns with defense strategies, ARES/Thinkless differentiation, narrative skeleton",
  "project": "cost-verify-agent-rl",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/docs/framing_draft.md",
  "tags": [
    "paper",
    "framing",
    "draft"
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
  "session_id": "12f481e3-4249-4909-b494-860766cbf5b8",
  "uuid": "c2cf72f5-f113-413e-b507-8a0d183dbe34",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013Xr5BheVM81okCEocem9fg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4071,
      "cache_read_input_tokens": 46945,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4071
      },
      "output_tokens": 58,
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

_source line 23 · 2026-05-15T18:44:54.304Z_

<details><summary>↩ Tool result · `toolu_01N5mLX7D8naPseVrvrXz83B`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260515_ff7034\", \"name\": \"framing_draft\", \"type\": \"report\", \"description\": \"B-IAVR paper framing draft: core insight, 3 claims with evidence requirements, 4 reviewer concerns with defense strategies, ARES/Thinkless differentiation, narrative skeleton\", \"path\": \"projects/cost-verify-agent-rl/artifacts/_project/report/framing_draft.md\", \"url\": null, \"project\": \"cost-verify-agent-rl\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-15T18:44:54.199253+00:00\", \"tags\": [\"paper\", \"framing\", \"draft\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "12f481e3-4249-4909-b494-860766cbf5b8",
  "uuid": "3f685cdc-bc26-47f3-9d03-f818c171eaf6",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260515_ff7034\\\", \\\"name\\\": \\\"framing_draft\\\", \\\"type\\\": \\\"report\\\", \\\"description\\\": \\\"B-IAVR paper framing draft: core insight, 3 claims with evidence requirements, 4 reviewer concerns with defense strategies, ARES/Thinkless differentiation, narrative skeleton\\\", \\\"path\\\": \\\"projects/cost-verify-agent-rl/artifacts/_project/report/framing_draft.md\\\", \\\"url\\\": null, \\\"project\\\": \\\"cost-verify-agent-rl\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-15T18:44:54.199253+00:00\\\", \\\"tags\\\": [\\\"paper\\\", \\\"framing\\\", \\\"draft\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260515_ff7034\", \"name\": \"framing_draft\", \"type\": \"report\", \"description\": \"B-IAVR paper framing draft: core insight, 3 claims with evidence requirements, 4 reviewer concerns with defense strategies, ARES/Thinkless differentiation, narrative skeleton\", \"path\": \"projects/cost-verify-agent-rl/artifacts/_project/report/framing_draft.md\", \"url\": null, \"project\": \"cost-verify-agent-rl\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-15T18:44:54.199253+00:00\", \"tags\": [\"paper\", \"framing\", \"draft\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 24_

已完成。摘要：

**Core Insight**: 大多数 self-verification 是 confirmatory 而非 corrective——不改变 agent 行为。用 action change 作为 reward signal，RL 可以训练 agent 只在 verification 真正 informative 时触发验证，实现 cost-efficiency。

**三个 Claims**:
1. **Selective verification reduces cost while preserving performance** (moderate) — 最强 claim，需 always-on baseline ≥50% + B-IAVR verification ↓40%+ 且 success 持平。当前证据全部缺失，依赖 exp027 pass + Phase B。
2. **Action change 是有效的 verification informativeness reward** (moderate) — 需训练收敛 + ablation。尚未验证。
3. **Learned policy > heuristic baselines** (weak) — 需完整 ablation 矩阵（always-on / no-verify / random-p / confidence-threshold）。

**最大 Reviewer Concern**: **Baseline performance insufficient** — cost-efficiency story 的前提是 always-on baseline 本身要够强（≥50%）。如果 baseline 只有 20-30%，"省验证开销"在一个本就很弱的系统上没有实际意义。这是当前最大风险，因为 exp027 的 MVP 阈值仅 20%，距 50% 的论文门槛还有很大 gap。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "12f481e3-4249-4909-b494-860766cbf5b8",
  "uuid": "70911c86-39a5-4466-9546-e9f2883b7225",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K6PzcfgM6TvV7LReLQGJ2T",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 641,
      "cache_read_input_tokens": 51016,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 641
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

_source line 25_

已完成。摘要：

**Core Insight**: 大多数 self-verification 是 confirmatory 而非 corrective——不改变 agent 行为。用 action change 作为 reward signal，RL 可以训练 agent 只在 verification 真正 informative 时触发验证，实现 cost-efficiency。

**三个 Claims**:
1. **Selective verification reduces cost while preserving performance** (moderate) — 最强 claim，需 always-on baseline ≥50% + B-IAVR verification ↓40%+ 且 success 持平。当前证据全部缺失，依赖 exp027 pass + Phase B。
2. **Action change 是有效的 verification informativeness reward** (moderate) — 需训练收敛 + ablation。尚未验证。
3. **Learned policy > heuristic baselines** (weak) — 需完整 ablation 矩阵（always-on / no-verify / random-p / confidence-threshold）。

**最大 Reviewer Concern**: **Baseline performance insufficient** — cost-efficiency story 的前提是 always-on baseline 本身要够强（≥50%）。如果 baseline 只有 20-30%，"省验证开销"在一个本就很弱的系统上没有实际意义。这是当前最大风险，因为 exp027 的 MVP 阈值仅 20%，距 50% 的论文门槛还有很大 gap。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 124289,
  "duration_api_ms": 125637,
  "num_turns": 9,
  "stop_reason": "end_turn",
  "session_id": "12f481e3-4249-4909-b494-860766cbf5b8",
  "total_cost_usd": 0.4626895,
  "usage": {
    "input_tokens": 9,
    "cache_creation_input_tokens": 39816,
    "cache_read_input_tokens": 159621,
    "output_tokens": 5266,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 39816,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 394,
        "cache_read_input_tokens": 51016,
        "cache_creation_input_tokens": 641,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 641
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2234,
      "outputTokens": 20,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.0023339999999999997,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 9,
      "outputTokens": 5266,
      "cacheReadInputTokens": 159621,
      "cacheCreationInputTokens": 39816,
      "webSearchRequests": 0,
      "costUSD": 0.46035550000000003,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "7dcce03f-4652-473e-b286-56576a0babda"
}
```

</details>

---
