# knowledge roadmap update

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 18
- **Recorded user turns:** 0
- **Tool calls:** 6
- **Original source:** `logs/workers/worker_knowledge_roadmap-update_20260514T073530.log`
- **Structured JSON:** [`36dcb5dedb7ac6d5a5f3.json`](../../sessions/36/36dcb5dedb7ac6d5a5f3.json)

## Before a recorded user message

18 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement",
  "session_id": "f652a67f-4d9e-40df-a607-b3e5b9ea97e0",
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
  "uuid": "d1f69e54-cfd6-4320-8d69-1c4a131077f9",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/memory/"
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
    "resetsAt": 1778760600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "c1bf12ce-10c2-4dba-9b97-f792a4689914",
  "session_id": "f652a67f-4d9e-40df-a607-b3e5b9ea97e0"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me read the current ROADMAP.md first.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f652a67f-4d9e-40df-a607-b3e5b9ea97e0",
  "uuid": "b88d61af-ae60-4c7a-80e2-c3cfcd5f15de",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01No4cpMGTMp9FWZzgNP67Ta",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11383,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11383
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

_source line 5_

<details open><summary>🔧 Tool call — Read · `toolu_01VJnHVbW1mvfskU5VVi5v38`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f652a67f-4d9e-40df-a607-b3e5b9ea97e0",
  "uuid": "51b64238-1d4b-49d2-82f2-492e41f0a6a9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01No4cpMGTMp9FWZzgNP67Ta",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11383,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11383
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

_source line 6 · 2026-05-14T07:35:42.709Z_

<details><summary>↩ Tool result · `toolu_01VJnHVbW1mvfskU5VVi5v38`</summary>

```text
1	# acr-vla-conformal-refinement — Research Dashboard
2	
3	> 最后更新: 2026-05-14 03:23 UTC | 更新原因: Phase 2 spatial eval 进行中，补录 SFT Gate 决策，更新竞品发现
4	
5	## 核心方向
6	Per-DOF conformal statistics from multivariate CP on flow-matching VLA samples enable dimension-selective action correction. 详见 paper_framing.md。
7	
8	## 投稿目标
9	**ICLR 2027**（预计 DDL Sep-Oct 2026）。CoRL 2026 已放弃（D011）。
10	
11	## 当前进展
12	- **阶段**: Phase 2 — Spatial Eval 四路对比（ACR-VLA / SampleConsensus / Scalar-CRM / VLA-mean）
13	- **MVP**: PASS（plan_000, per-DOF > scalar > none 确认）
14	- **SFT Gate**: 30% baseline，决定继续（D015）
15	- **CRM 训练完成**: per-DOF val_loss=0.009, scalar_unc=0.008, obs_only=0.018（conformal features 2× 改善确认）
16	- **Baselines 锁定**: spatial 30% (K=1), object 13% (K=1)
17	- **早期信号（2/10 tasks，不构成结论）**: ACR-VLA 在简单任务上低于 baseline，per-DOF CRM 可能在简单任务上引入有害 correction
18	- **文献**: 发现两个直接竞品（SC-VLA, VLA-Pilot），LIBERO SOTA 已更新至 ACoT-VLA 84.1%
19	
20	## 近期任务
21	- [ ] eval-acr-spatial-v2 完成 → 核心 claim 判定（ACR-VLA vs baseline 30%）
22	- [ ] eval-reconvla-spatial-v3 完成 → SampleConsensus 对比
23	- [ ] eval-scalar-unc-spatial 完成 → scalar vs per-DOF 最终裁决
24	- [ ] crm-train-k5 完成 → K sensitivity ablation + 启动 eval-k5-spatial
25	- [ ] eval-vla-mean-spatial 完成 → 隔离多采样平均贡献
26	- [ ] 代码同步 bjb1→bjb2（evaluate.py + train_crm.py）
27	- [ ] 完整 spatial 四路对比表出炉 → 决定是否铺 object benchmark
28	- [ ] paper_framing.md 更新竞品定位（SC-VLA, VLA-Pilot, ACoT-VLA SOTA）
29	
30	## SFT Gate
31	D015: 30% baseline 继续推进。核心关注相对提升，非绝对值。
32	
33	## GPU 预算
34	- bjb1-18228 (4× RTX 4090): eval-acr(cuda:1) + eval-reconvla(cuda:2) + eval-scalar-unc(cuda:3) + crm-train-k5(cuda:0)
35	- bjb2-40593 (1× RTX 4090 D): eval-vla-mean-spatial(cuda:0)
36	- 总预算 ~200 GPU·h, 已用 ~80h, 剩余 ~120h
37	
38	## 关键路径
39	**当前**: 5 路 spatial eval 并行 → 完整对比表 → claim 判定 → object benchmark / framing 调整
40	**风险**: ACR-VLA 早期信号低于 baseline（仅 2/10 tasks），等完整结果
41	
42	## 关键决策日志
43	
44	| ID | 日期 | 摘要 | 关联实验 |
45	|----|------|------|----------|
46	| D015 | 2026-05-14 | D015: SFT Gate 30% — 继续推进，不换模型，关注相对提升 | eval-spatial-v7-full, eval-object-v8-full |
47	| D014 | 2026-05-13 | ReconVLA baseline 描述严重失实——重命名为 SampleConsensus，启动  | eval-reconvla-spatial-v2 |
48	| D013 | 2026-05-13 | D013: D012 的 55.6% 不可靠 — wrapper 需对齐 lerobot 标准推理管 | eval-smolvla-libero-spatial |
49	| D012 | 2026-05-13 | D012: smolvla_libero wrapper 修复后 55.6% — 取消 SFT，直接 | eval-smolvla-libero-spatial, sft-smolvla-libero |
50	| D011 | 2026-05-13 | D011: 正式放弃 CoRL 2026，目标 ICLR 2027 | — |
51	| D010 | 2026-05-13 | D010: 正式触发 SFT fallback — smolvla_libero 0% 确认不可用， | eval-smolvla-libero-spatial, sft-smolvla-libero |
52	| D009 | 2026-05-13 | D008 补充：优先尝试社区 checkpoint lerobot/smolvla_libero，> | plan_001, plan_014 |
53	| D008 | 2026-05-13 | SmolVLA 未 LIBERO fine-tuned，选方案 A：先 LoRA SFT SmolV | plan_001, plan_014 |
54	| D007 | 2026-05-13 | Precompute 加速策略：缩减数据(10 demos/task) + 4-GPU 并行 + 代 | plan_001, plan_014 |
55	| D006 | 2026-05-13 | Dream 审稿分析完成：proceed + 加 3 个新实验（ReconVLA baseline, | — |
56	
57	
58	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f652a67f-4d9e-40df-a607-b3e5b9ea97e0",
  "uuid": "a7a9cc09-a6f2-44be-b3de-5884c134e918",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md",
      "content": "# acr-vla-conformal-refinement — Research Dashboard\n\n> 最后更新: 2026-05-14 03:23 UTC | 更新原因: Phase 2 spatial eval 进行中，补录 SFT Gate 决策，更新竞品发现\n\n## 核心方向\nPer-DOF conformal statistics from multivariate CP on flow-matching VLA samples enable dimension-selective action correction. 详见 paper_framing.md。\n\n## 投稿目标\n**ICLR 2027**（预计 DDL Sep-Oct 2026）。CoRL 2026 已放弃（D011）。\n\n## 当前进展\n- **阶段**: Phase 2 — Spatial Eval 四路对比（ACR-VLA / SampleConsensus / Scalar-CRM / VLA-mean）\n- **MVP**: PASS（plan_000, per-DOF > scalar > none 确认）\n- **SFT Gate**: 30% baseline，决定继续（D015）\n- **CRM 训练完成**: per-DOF val_loss=0.009, scalar_unc=0.008, obs_only=0.018（conformal features 2× 改善确认）\n- **Baselines 锁定**: spatial 30% (K=1), object 13% (K=1)\n- **早期信号（2/10 tasks，不构成结论）**: ACR-VLA 在简单任务上低于 baseline，per-DOF CRM 可能在简单任务上引入有害 correction\n- **文献**: 发现两个直接竞品（SC-VLA, VLA-Pilot），LIBERO SOTA 已更新至 ACoT-VLA 84.1%\n\n## 近期任务\n- [ ] eval-acr-spatial-v2 完成 → 核心 claim 判定（ACR-VLA vs baseline 30%）\n- [ ] eval-reconvla-spatial-v3 完成 → SampleConsensus 对比\n- [ ] eval-scalar-unc-spatial 完成 → scalar vs per-DOF 最终裁决\n- [ ] crm-train-k5 完成 → K sensitivity ablation + 启动 eval-k5-spatial\n- [ ] eval-vla-mean-spatial 完成 → 隔离多采样平均贡献\n- [ ] 代码同步 bjb1→bjb2（evaluate.py + train_crm.py）\n- [ ] 完整 spatial 四路对比表出炉 → 决定是否铺 object benchmark\n- [ ] paper_framing.md 更新竞品定位（SC-VLA, VLA-Pilot, ACoT-VLA SOTA）\n\n## SFT Gate\nD015: 30% baseline 继续推进。核心关注相对提升，非绝对值。\n\n## GPU 预算\n- bjb1-18228 (4× RTX 4090): eval-acr(cuda:1) + eval-reconvla(cuda:2) + eval-scalar-unc(cuda:3) + crm-train-k5(cuda:0)\n- bjb2-40593 (1× RTX 4090 D): eval-vla-mean-spatial(cuda:0)\n- 总预算 ~200 GPU·h, 已用 ~80h, 剩余 ~120h\n\n## 关键路径\n**当前**: 5 路 spatial eval 并行 → 完整对比表 → claim 判定 → object benchmark / framing 调整\n**风险**: ACR-VLA 早期信号低于 baseline（仅 2/10 tasks），等完整结果\n\n## 关键决策日志\n\n| ID | 日期 | 摘要 | 关联实验 |\n|----|------|------|----------|\n| D015 | 2026-05-14 | D015: SFT Gate 30% — 继续推进，不换模型，关注相对提升 | eval-spatial-v7-full, eval-object-v8-full |\n| D014 | 2026-05-13 | ReconVLA baseline 描述严重失实——重命名为 SampleConsensus，启动  | eval-reconvla-spatial-v2 |\n| D013 | 2026-05-13 | D013: D012 的 55.6% 不可靠 — wrapper 需对齐 lerobot 标准推理管 | eval-smolvla-libero-spatial |\n| D012 | 2026-05-13 | D012: smolvla_libero wrapper 修复后 55.6% — 取消 SFT，直接 | eval-smolvla-libero-spatial, sft-smolvla-libero |\n| D011 | 2026-05-13 | D011: 正式放弃 CoRL 2026，目标 ICLR 2027 | — |\n| D010 | 2026-05-13 | D010: 正式触发 SFT fallback — smolvla_libero 0% 确认不可用， | eval-smolvla-libero-spatial, sft-smolvla-libero |\n| D009 | 2026-05-13 | D008 补充：优先尝试社区 checkpoint lerobot/smolvla_libero，> | plan_001, plan_014 |\n| D008 | 2026-05-13 | SmolVLA 未 LIBERO fine-tuned，选方案 A：先 LoRA SFT SmolV | plan_001, plan_014 |\n| D007 | 2026-05-13 | Precompute 加速策略：缩减数据(10 demos/task) + 4-GPU 并行 + 代 | plan_001, plan_014 |\n| D006 | 2026-05-13 | Dream 审稿分析完成：proceed + 加 3 个新实验（ReconVLA baseline, | — |\n\n\n",
      "numLines": 58,
      "startLine": 1,
      "totalLines": 58
    }
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — Edit · `toolu_01Noyvb6KnWZfpADd2tbZxje`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md",
  "old_string": "> 最后更新: 2026-05-14 03:23 UTC | 更新原因: Phase 2 spatial eval 进行中，补录 SFT Gate 决策，更新竞品发现",
  "new_string": "> 最后更新: 2026-05-14 16:00 UTC | 更新原因: crm-train-k5 完成 + eval-k5-spatial 启动，竞品分析完成，CRM correction 退化现象确认"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f652a67f-4d9e-40df-a607-b3e5b9ea97e0",
  "uuid": "7a73f31e-0a8e-4df0-8998-4312da8a7509",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H3Pi6aFKxrh18cVakGzALC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1835,
      "cache_read_input_tokens": 23224,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1835
      },
      "output_tokens": 65,
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

_source line 8 · 2026-05-14T07:35:47.006Z_

<details><summary>↩ Tool result · `toolu_01Noyvb6KnWZfpADd2tbZxje`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f652a67f-4d9e-40df-a607-b3e5b9ea97e0",
  "uuid": "f6ec8e92-f36f-41dc-bd2f-04711ee4f7d7",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md",
    "oldString": "> 最后更新: 2026-05-14 03:23 UTC | 更新原因: Phase 2 spatial eval 进行中，补录 SFT Gate 决策，更新竞品发现",
    "newString": "> 最后更新: 2026-05-14 16:00 UTC | 更新原因: crm-train-k5 完成 + eval-k5-spatial 启动，竞品分析完成，CRM correction 退化现象确认",
    "originalFile": "# acr-vla-conformal-refinement — Research Dashboard\n\n> 最后更新: 2026-05-14 03:23 UTC | 更新原因: Phase 2 spatial eval 进行中，补录 SFT Gate 决策，更新竞品发现\n\n## 核心方向\nPer-DOF conformal statistics from multivariate CP on flow-matching VLA samples enable dimension-selective action correction. 详见 paper_framing.md。\n\n## 投稿目标\n**ICLR 2027**（预计 DDL Sep-Oct 2026）。CoRL 2026 已放弃（D011）。\n\n## 当前进展\n- **阶段**: Phase 2 — Spatial Eval 四路对比（ACR-VLA / SampleConsensus / Scalar-CRM / VLA-mean）\n- **MVP**: PASS（plan_000, per-DOF > scalar > none 确认）\n- **SFT Gate**: 30% baseline，决定继续（D015）\n- **CRM 训练完成**: per-DOF val_loss=0.009, scalar_unc=0.008, obs_only=0.018（conformal features 2× 改善确认）\n- **Baselines 锁定**: spatial 30% (K=1), object 13% (K=1)\n- **早期信号（2/10 tasks，不构成结论）**: ACR-VLA 在简单任务上低于 baseline，per-DOF CRM 可能在简单任务上引入有害 correction\n- **文献**: 发现两个直接竞品（SC-VLA, VLA-Pilot），LIBERO SOTA 已更新至 ACoT-VLA 84.1%\n\n## 近期任务\n- [ ] eval-acr-spatial-v2 完成 → 核心 claim 判定（ACR-VLA vs baseline 30%）\n- [ ] eval-reconvla-spatial-v3 完成 → SampleConsensus 对比\n- [ ] eval-scalar-unc-spatial 完成 → scalar vs per-DOF 最终裁决\n- [ ] crm-train-k5 完成 → K sensitivity ablation + 启动 eval-k5-spatial\n- [ ] eval-vla-mean-spatial 完成 → 隔离多采样平均贡献\n- [ ] 代码同步 bjb1→bjb2（evaluate.py + train_crm.py）\n- [ ] 完整 spatial 四路对比表出炉 → 决定是否铺 object benchmark\n- [ ] paper_framing.md 更新竞品定位（SC-VLA, VLA-Pilot, ACoT-VLA SOTA）\n\n## SFT Gate\nD015: 30% baseline 继续推进。核心关注相对提升，非绝对值。\n\n## GPU 预算\n- bjb1-18228 (4× RTX 4090): eval-acr(cuda:1) + eval-reconvla(cuda:2) + eval-scalar-unc(cuda:3) + crm-train-k5(cuda:0)\n- bjb2-40593 (1× RTX 4090 D): eval-vla-mean-spatial(cuda:0)\n- 总预算 ~200 GPU·h, 已用 ~80h, 剩余 ~120h\n\n## 关键路径\n**当前**: 5 路 spatial eval 并行 → 完整对比表 → claim 判定 → object benchmark / framing 调整\n**风险**: ACR-VLA 早期信号低于 baseline（仅 2/10 tasks），等完整结果\n\n## 关键决策日志\n\n| ID | 日期 | 摘要 | 关联实验 |\n|----|------|------|----------|\n| D015 | 2026-05-14 | D015: SFT Gate 30% — 继续推进，不换模型，关注相对提升 | eval-spatial-v7-full, eval-object-v8-full |\n| D014 | 2026-05-13 | ReconVLA baseline 描述严重失实——重命名为 SampleConsensus，启动  | eval-reconvla-spatial-v2 |\n| D013 | 2026-05-13 | D013: D012 的 55.6% 不可靠 — wrapper 需对齐 lerobot 标准推理管 | eval-smolvla-libero-spatial |\n| D012 | 2026-05-13 | D012: smolvla_libero wrapper 修复后 55.6% — 取消 SFT，直接 | eval-smolvla-libero-spatial, sft-smolvla-libero |\n| D011 | 2026-05-13 | D011: 正式放弃 CoRL 2026，目标 ICLR 2027 | — |\n| D010 | 2026-05-13 | D010: 正式触发 SFT fallback — smolvla_libero 0% 确认不可用， | eval-smolvla-libero-spatial, sft-smolvla-libero |\n| D009 | 2026-05-13 | D008 补充：优先尝试社区 checkpoint lerobot/smolvla_libero，> | plan_001, plan_014 |\n| D008 | 2026-05-13 | SmolVLA 未 LIBERO fine-tuned，选方案 A：先 LoRA SFT SmolV | plan_001, plan_014 |\n| D007 | 2026-05-13 | Precompute 加速策略：缩减数据(10 demos/task) + 4-GPU 并行 + 代 | plan_001, plan_014 |\n| D006 | 2026-05-13 | Dream 审稿分析完成：proceed + 加 3 个新实验（ReconVLA baseline, | — |\n\n\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 6,
        "newStart": 1,
        "newLines": 6,
        "lines": [
          " # acr-vla-conformal-refinement — Research Dashboard",
          " ",
          "-> 最后更新: 2026-05-14 03:23 UTC | 更新原因: Phase 2 spatial eval 进行中，补录 SFT Gate 决策，更新竞品发现",
          "+> 最后更新: 2026-05-14 16:00 UTC | 更新原因: crm-train-k5 完成 + eval-k5-spatial 启动，竞品分析完成，CRM correction 退化现象确认",
          " ",
          " ## 核心方向",
          " Per-DOF conformal statistics from multivariate CP on flow-matching VLA samples enable dimension-selective action correction. 详见 paper_framing.md。"
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

_source line 9_

<details open><summary>🔧 Tool call — Edit · `toolu_01V1g79ktxW7KnHCGapG5KG6`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md",
  "old_string": "- **早期信号（2/10 tasks，不构成结论）**: ACR-VLA 在简单任务上低于 baseline，per-DOF CRM 可能在简单任务上引入有害 correction\n- **文献**: 发现两个直接竞品（SC-VLA, VLA-Pilot），LIBERO SOTA 已更新至 ACoT-VLA 84.1%",
  "new_string": "- **早期信号（2/10 tasks，不构成结论）**: ACR-VLA 在简单任务上低于 baseline，per-DOF CRM 可能在简单任务上引入有害 correction\n- **竞品分析完成** (art_20260514_621600): 核心竞品 ReconVLA（最直接）、SC-VLA、VLA-Pilot、ACoT-VLA\n- **CRM correction 退化现象**: ACR-VLA 中间结果 (23-26%) 低于 baseline (30%)，SampleConsensus 领先 (42.9%)\n- **文献调研完成** (art_20260514_d21dd2): correction degradation 可能原因与补救方向（correction clipping/gating 等）"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f652a67f-4d9e-40df-a607-b3e5b9ea97e0",
  "uuid": "d53fe8af-c0d6-462f-a62e-3cf0793d40d3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Uo5m6RgZDaiDP1yT76yZM6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 326,
      "cache_read_input_tokens": 25059,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 326
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

_source line 10 · 2026-05-14T07:35:52.849Z_

<details><summary>↩ Tool result · `toolu_01V1g79ktxW7KnHCGapG5KG6`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f652a67f-4d9e-40df-a607-b3e5b9ea97e0",
  "uuid": "9da6e46f-d490-4caa-8a1e-fc960ef08c58",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md",
    "oldString": "- **早期信号（2/10 tasks，不构成结论）**: ACR-VLA 在简单任务上低于 baseline，per-DOF CRM 可能在简单任务上引入有害 correction\n- **文献**: 发现两个直接竞品（SC-VLA, VLA-Pilot），LIBERO SOTA 已更新至 ACoT-VLA 84.1%",
    "newString": "- **早期信号（2/10 tasks，不构成结论）**: ACR-VLA 在简单任务上低于 baseline，per-DOF CRM 可能在简单任务上引入有害 correction\n- **竞品分析完成** (art_20260514_621600): 核心竞品 ReconVLA（最直接）、SC-VLA、VLA-Pilot、ACoT-VLA\n- **CRM correction 退化现象**: ACR-VLA 中间结果 (23-26%) 低于 baseline (30%)，SampleConsensus 领先 (42.9%)\n- **文献调研完成** (art_20260514_d21dd2): correction degradation 可能原因与补救方向（correction clipping/gating 等）",
    "originalFile": "# acr-vla-conformal-refinement — Research Dashboard\n\n> 最后更新: 2026-05-14 16:00 UTC | 更新原因: crm-train-k5 完成 + eval-k5-spatial 启动，竞品分析完成，CRM correction 退化现象确认\n\n## 核心方向\nPer-DOF conformal statistics from multivariate CP on flow-matching VLA samples enable dimension-selective action correction. 详见 paper_framing.md。\n\n## 投稿目标\n**ICLR 2027**（预计 DDL Sep-Oct 2026）。CoRL 2026 已放弃（D011）。\n\n## 当前进展\n- **阶段**: Phase 2 — Spatial Eval 四路对比（ACR-VLA / SampleConsensus / Scalar-CRM / VLA-mean）\n- **MVP**: PASS（plan_000, per-DOF > scalar > none 确认）\n- **SFT Gate**: 30% baseline，决定继续（D015）\n- **CRM 训练完成**: per-DOF val_loss=0.009, scalar_unc=0.008, obs_only=0.018（conformal features 2× 改善确认）\n- **Baselines 锁定**: spatial 30% (K=1), object 13% (K=1)\n- **早期信号（2/10 tasks，不构成结论）**: ACR-VLA 在简单任务上低于 baseline，per-DOF CRM 可能在简单任务上引入有害 correction\n- **文献**: 发现两个直接竞品（SC-VLA, VLA-Pilot），LIBERO SOTA 已更新至 ACoT-VLA 84.1%\n\n## 近期任务\n- [ ] eval-acr-spatial-v2 完成 → 核心 claim 判定（ACR-VLA vs baseline 30%）\n- [ ] eval-reconvla-spatial-v3 完成 → SampleConsensus 对比\n- [ ] eval-scalar-unc-spatial 完成 → scalar vs per-DOF 最终裁决\n- [ ] crm-train-k5 完成 → K sensitivity ablation + 启动 eval-k5-spatial\n- [ ] eval-vla-mean-spatial 完成 → 隔离多采样平均贡献\n- [ ] 代码同步 bjb1→bjb2（evaluate.py + train_crm.py）\n- [ ] 完整 spatial 四路对比表出炉 → 决定是否铺 object benchmark\n- [ ] paper_framing.md 更新竞品定位（SC-VLA, VLA-Pilot, ACoT-VLA SOTA）\n\n## SFT Gate\nD015: 30% baseline 继续推进。核心关注相对提升，非绝对值。\n\n## GPU 预算\n- bjb1-18228 (4× RTX 4090): eval-acr(cuda:1) + eval-reconvla(cuda:2) + eval-scalar-unc(cuda:3) + crm-train-k5(cuda:0)\n- bjb2-40593 (1× RTX 4090 D): eval-vla-mean-spatial(cuda:0)\n- 总预算 ~200 GPU·h, 已用 ~80h, 剩余 ~120h\n\n## 关键路径\n**当前**: 5 路 spatial eval 并行 → 完整对比表 → claim 判定 → object benchmark / framing 调整\n**风险**: ACR-VLA 早期信号低于 baseline（仅 2/10 tasks），等完整结果\n\n## 关键决策日志\n\n| ID | 日期 | 摘要 | 关联实验 |\n|----|------|------|----------|\n| D015 | 2026-05-14 | D015: SFT Gate 30% — 继续推进，不换模型，关注相对提升 | eval-spatial-v7-full, eval-object-v8-full |\n| D014 | 2026-05-13 | ReconVLA baseline 描述严重失实——重命名为 SampleConsensus，启动  | eval-reconvla-spatial-v2 |\n| D013 | 2026-05-13 | D013: D012 的 55.6% 不可靠 — wrapper 需对齐 lerobot 标准推理管 | eval-smolvla-libero-spatial |\n| D012 | 2026-05-13 | D012: smolvla_libero wrapper 修复后 55.6% — 取消 SFT，直接 | eval-smolvla-libero-spatial, sft-smolvla-libero |\n| D011 | 2026-05-13 | D011: 正式放弃 CoRL 2026，目标 ICLR 2027 | — |\n| D010 | 2026-05-13 | D010: 正式触发 SFT fallback — smolvla_libero 0% 确认不可用， | eval-smolvla-libero-spatial, sft-smolvla-libero |\n| D009 | 2026-05-13 | D008 补充：优先尝试社区 checkpoint lerobot/smolvla_libero，> | plan_001, plan_014 |\n| D008 | 2026-05-13 | SmolVLA 未 LIBERO fine-tuned，选方案 A：先 LoRA SFT SmolV | plan_001, plan_014 |\n| D007 | 2026-05-13 | Precompute 加速策略：缩减数据(10 demos/task) + 4-GPU 并行 + 代 | plan_001, plan_014 |\n| D006 | 2026-05-13 | Dream 审稿分析完成：proceed + 加 3 个新实验（ReconVLA baseline, | — |\n\n\n",
    "structuredPatch": [
      {
        "oldStart": 15,
        "oldLines": 7,
        "newStart": 15,
        "newLines": 9,
        "lines": [
          " - **CRM 训练完成**: per-DOF val_loss=0.009, scalar_unc=0.008, obs_only=0.018（conformal features 2× 改善确认）",
          " - **Baselines 锁定**: spatial 30% (K=1), object 13% (K=1)",
          " - **早期信号（2/10 tasks，不构成结论）**: ACR-VLA 在简单任务上低于 baseline，per-DOF CRM 可能在简单任务上引入有害 correction",
          "-- **文献**: 发现两个直接竞品（SC-VLA, VLA-Pilot），LIBERO SOTA 已更新至 ACoT-VLA 84.1%",
          "+- **竞品分析完成** (art_20260514_621600): 核心竞品 ReconVLA（最直接）、SC-VLA、VLA-Pilot、ACoT-VLA",
          "+- **CRM correction 退化现象**: ACR-VLA 中间结果 (23-26%) 低于 baseline (30%)，SampleConsensus 领先 (42.9%)",
          "+- **文献调研完成** (art_20260514_d21dd2): correction degradation 可能原因与补救方向（correction clipping/gating 等）",
          " ",
          " ## 近期任务",
          " - [ ] eval-acr-spatial-v2 完成 → 核心 claim 判定（ACR-VLA vs baseline 30%）"
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

_source line 11_

<details open><summary>🔧 Tool call — Edit · `toolu_01PSQS7TWGnrPfXMyq4pNBT6`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md",
  "old_string": "- [ ] crm-train-k5 完成 → K sensitivity ablation + 启动 eval-k5-spatial\n- [ ] eval-vla-mean-spatial 完成 → 隔离多采样平均贡献\n- [ ] 代码同步 bjb1→bjb2（evaluate.py + train_crm.py）",
  "new_string": "- [x] crm-train-k5 完成 → K sensitivity ablation + eval-k5-spatial 已启动\n- [ ] eval-k5-spatial 完成 → K=5 sensitivity ablation 结果\n- [ ] eval-vla-mean-spatial 完成 → 隔离多采样平均贡献\n- [x] 代码同步 bjb1→bjb2（evaluate.py + train_crm.py）— MD5 verified"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f652a67f-4d9e-40df-a607-b3e5b9ea97e0",
  "uuid": "6bb4314d-2fbd-43ba-81fe-20641b9b97f9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NbfwgEZxgAEpv8vPCmV8iF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 520,
      "cache_read_input_tokens": 25385,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 520
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

_source line 12 · 2026-05-14T07:35:58.418Z_

<details><summary>↩ Tool result · `toolu_01PSQS7TWGnrPfXMyq4pNBT6`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f652a67f-4d9e-40df-a607-b3e5b9ea97e0",
  "uuid": "fa9cb7cd-93e5-43d3-9439-fef74ed6a2fa",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md",
    "oldString": "- [ ] crm-train-k5 完成 → K sensitivity ablation + 启动 eval-k5-spatial\n- [ ] eval-vla-mean-spatial 完成 → 隔离多采样平均贡献\n- [ ] 代码同步 bjb1→bjb2（evaluate.py + train_crm.py）",
    "newString": "- [x] crm-train-k5 完成 → K sensitivity ablation + eval-k5-spatial 已启动\n- [ ] eval-k5-spatial 完成 → K=5 sensitivity ablation 结果\n- [ ] eval-vla-mean-spatial 完成 → 隔离多采样平均贡献\n- [x] 代码同步 bjb1→bjb2（evaluate.py + train_crm.py）— MD5 verified",
    "originalFile": "# acr-vla-conformal-refinement — Research Dashboard\n\n> 最后更新: 2026-05-14 16:00 UTC | 更新原因: crm-train-k5 完成 + eval-k5-spatial 启动，竞品分析完成，CRM correction 退化现象确认\n\n## 核心方向\nPer-DOF conformal statistics from multivariate CP on flow-matching VLA samples enable dimension-selective action correction. 详见 paper_framing.md。\n\n## 投稿目标\n**ICLR 2027**（预计 DDL Sep-Oct 2026）。CoRL 2026 已放弃（D011）。\n\n## 当前进展\n- **阶段**: Phase 2 — Spatial Eval 四路对比（ACR-VLA / SampleConsensus / Scalar-CRM / VLA-mean）\n- **MVP**: PASS（plan_000, per-DOF > scalar > none 确认）\n- **SFT Gate**: 30% baseline，决定继续（D015）\n- **CRM 训练完成**: per-DOF val_loss=0.009, scalar_unc=0.008, obs_only=0.018（conformal features 2× 改善确认）\n- **Baselines 锁定**: spatial 30% (K=1), object 13% (K=1)\n- **早期信号（2/10 tasks，不构成结论）**: ACR-VLA 在简单任务上低于 baseline，per-DOF CRM 可能在简单任务上引入有害 correction\n- **竞品分析完成** (art_20260514_621600): 核心竞品 ReconVLA（最直接）、SC-VLA、VLA-Pilot、ACoT-VLA\n- **CRM correction 退化现象**: ACR-VLA 中间结果 (23-26%) 低于 baseline (30%)，SampleConsensus 领先 (42.9%)\n- **文献调研完成** (art_20260514_d21dd2): correction degradation 可能原因与补救方向（correction clipping/gating 等）\n\n## 近期任务\n- [ ] eval-acr-spatial-v2 完成 → 核心 claim 判定（ACR-VLA vs baseline 30%）\n- [ ] eval-reconvla-spatial-v3 完成 → SampleConsensus 对比\n- [ ] eval-scalar-unc-spatial 完成 → scalar vs per-DOF 最终裁决\n- [ ] crm-train-k5 完成 → K sensitivity ablation + 启动 eval-k5-spatial\n- [ ] eval-vla-mean-spatial 完成 → 隔离多采样平均贡献\n- [ ] 代码同步 bjb1→bjb2（evaluate.py + train_crm.py）\n- [ ] 完整 spatial 四路对比表出炉 → 决定是否铺 object benchmark\n- [ ] paper_framing.md 更新竞品定位（SC-VLA, VLA-Pilot, ACoT-VLA SOTA）\n\n## SFT Gate\nD015: 30% baseline 继续推进。核心关注相对提升，非绝对值。\n\n## GPU 预算\n- bjb1-18228 (4× RTX 4090): eval-acr(cuda:1) + eval-reconvla(cuda:2) + eval-scalar-unc(cuda:3) + crm-train-k5(cuda:0)\n- bjb2-40593 (1× RTX 4090 D): eval-vla-mean-spatial(cuda:0)\n- 总预算 ~200 GPU·h, 已用 ~80h, 剩余 ~120h\n\n## 关键路径\n**当前**: 5 路 spatial eval 并行 → 完整对比表 → claim 判定 → object benchmark / framing 调整\n**风险**: ACR-VLA 早期信号低于 baseline（仅 2/10 tasks），等完整结果\n\n## 关键决策日志\n\n| ID | 日期 | 摘要 | 关联实验 |\n|----|------|------|----------|\n| D015 | 2026-05-14 | D015: SFT Gate 30% — 继续推进，不换模型，关注相对提升 | eval-spatial-v7-full, eval-object-v8-full |\n| D014 | 2026-05-13 | ReconVLA baseline 描述严重失实——重命名为 SampleConsensus，启动  | eval-reconvla-spatial-v2 |\n| D013 | 2026-05-13 | D013: D012 的 55.6% 不可靠 — wrapper 需对齐 lerobot 标准推理管 | eval-smolvla-libero-spatial |\n| D012 | 2026-05-13 | D012: smolvla_libero wrapper 修复后 55.6% — 取消 SFT，直接 | eval-smolvla-libero-spatial, sft-smolvla-libero |\n| D011 | 2026-05-13 | D011: 正式放弃 CoRL 2026，目标 ICLR 2027 | — |\n| D010 | 2026-05-13 | D010: 正式触发 SFT fallback — smolvla_libero 0% 确认不可用， | eval-smolvla-libero-spatial, sft-smolvla-libero |\n| D009 | 2026-05-13 | D008 补充：优先尝试社区 checkpoint lerobot/smolvla_libero，> | plan_001, plan_014 |\n| D008 | 2026-05-13 | SmolVLA 未 LIBERO fine-tuned，选方案 A：先 LoRA SFT SmolV | plan_001, plan_014 |\n| D007 | 2026-05-13 | Precompute 加速策略：缩减数据(10 demos/task) + 4-GPU 并行 + 代 | plan_001, plan_014 |\n| D006 | 2026-05-13 | Dream 审稿分析完成：proceed + 加 3 个新实验（ReconVLA baseline, | — |\n\n\n",
    "structuredPatch": [
      {
        "oldStart": 23,
        "oldLines": 9,
        "newStart": 23,
        "newLines": 10,
        "lines": [
          " - [ ] eval-acr-spatial-v2 完成 → 核心 claim 判定（ACR-VLA vs baseline 30%）",
          " - [ ] eval-reconvla-spatial-v3 完成 → SampleConsensus 对比",
          " - [ ] eval-scalar-unc-spatial 完成 → scalar vs per-DOF 最终裁决",
          "-- [ ] crm-train-k5 完成 → K sensitivity ablation + 启动 eval-k5-spatial",
          "+- [x] crm-train-k5 完成 → K sensitivity ablation + eval-k5-spatial 已启动",
          "+- [ ] eval-k5-spatial 完成 → K=5 sensitivity ablation 结果",
          " - [ ] eval-vla-mean-spatial 完成 → 隔离多采样平均贡献",
          "-- [ ] 代码同步 bjb1→bjb2（evaluate.py + train_crm.py）",
          "+- [x] 代码同步 bjb1→bjb2（evaluate.py + train_crm.py）— MD5 verified",
          " - [ ] 完整 spatial 四路对比表出炉 → 决定是否铺 object benchmark",
          " - [ ] paper_framing.md 更新竞品定位（SC-VLA, VLA-Pilot, ACoT-VLA SOTA）",
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

### Tool call

_source line 13_

<details open><summary>🔧 Tool call — Edit · `toolu_01AGJQAbw4br2mhuhVLm78Lq`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md",
  "old_string": "- bjb1-18228 (4× RTX 4090): eval-acr(cuda:1) + eval-reconvla(cuda:2) + eval-scalar-unc(cuda:3) + crm-train-k5(cuda:0)",
  "new_string": "- bjb1-18228 (4× RTX 4090): eval-k5-spatial(cuda:0) + eval-acr(cuda:1) + eval-reconvla(cuda:2) + eval-scalar-unc(cuda:3)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f652a67f-4d9e-40df-a607-b3e5b9ea97e0",
  "uuid": "cdab04d5-d7ea-4ebf-9f9f-2362c735f075",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014PXomrig8vu17r9dki7suc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 411,
      "cache_read_input_tokens": 25905,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 411
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

_source line 14 · 2026-05-14T07:36:03.058Z_

<details><summary>↩ Tool result · `toolu_01AGJQAbw4br2mhuhVLm78Lq`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f652a67f-4d9e-40df-a607-b3e5b9ea97e0",
  "uuid": "4b73ec36-d35c-4a12-a446-7a6abc744f8c",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md",
    "oldString": "- bjb1-18228 (4× RTX 4090): eval-acr(cuda:1) + eval-reconvla(cuda:2) + eval-scalar-unc(cuda:3) + crm-train-k5(cuda:0)",
    "newString": "- bjb1-18228 (4× RTX 4090): eval-k5-spatial(cuda:0) + eval-acr(cuda:1) + eval-reconvla(cuda:2) + eval-scalar-unc(cuda:3)",
    "originalFile": "# acr-vla-conformal-refinement — Research Dashboard\n\n> 最后更新: 2026-05-14 16:00 UTC | 更新原因: crm-train-k5 完成 + eval-k5-spatial 启动，竞品分析完成，CRM correction 退化现象确认\n\n## 核心方向\nPer-DOF conformal statistics from multivariate CP on flow-matching VLA samples enable dimension-selective action correction. 详见 paper_framing.md。\n\n## 投稿目标\n**ICLR 2027**（预计 DDL Sep-Oct 2026）。CoRL 2026 已放弃（D011）。\n\n## 当前进展\n- **阶段**: Phase 2 — Spatial Eval 四路对比（ACR-VLA / SampleConsensus / Scalar-CRM / VLA-mean）\n- **MVP**: PASS（plan_000, per-DOF > scalar > none 确认）\n- **SFT Gate**: 30% baseline，决定继续（D015）\n- **CRM 训练完成**: per-DOF val_loss=0.009, scalar_unc=0.008, obs_only=0.018（conformal features 2× 改善确认）\n- **Baselines 锁定**: spatial 30% (K=1), object 13% (K=1)\n- **早期信号（2/10 tasks，不构成结论）**: ACR-VLA 在简单任务上低于 baseline，per-DOF CRM 可能在简单任务上引入有害 correction\n- **竞品分析完成** (art_20260514_621600): 核心竞品 ReconVLA（最直接）、SC-VLA、VLA-Pilot、ACoT-VLA\n- **CRM correction 退化现象**: ACR-VLA 中间结果 (23-26%) 低于 baseline (30%)，SampleConsensus 领先 (42.9%)\n- **文献调研完成** (art_20260514_d21dd2): correction degradation 可能原因与补救方向（correction clipping/gating 等）\n\n## 近期任务\n- [ ] eval-acr-spatial-v2 完成 → 核心 claim 判定（ACR-VLA vs baseline 30%）\n- [ ] eval-reconvla-spatial-v3 完成 → SampleConsensus 对比\n- [ ] eval-scalar-unc-spatial 完成 → scalar vs per-DOF 最终裁决\n- [x] crm-train-k5 完成 → K sensitivity ablation + eval-k5-spatial 已启动\n- [ ] eval-k5-spatial 完成 → K=5 sensitivity ablation 结果\n- [ ] eval-vla-mean-spatial 完成 → 隔离多采样平均贡献\n- [x] 代码同步 bjb1→bjb2（evaluate.py + train_crm.py）— MD5 verified\n- [ ] 完整 spatial 四路对比表出炉 → 决定是否铺 object benchmark\n- [ ] paper_framing.md 更新竞品定位（SC-VLA, VLA-Pilot, ACoT-VLA SOTA）\n\n## SFT Gate\nD015: 30% baseline 继续推进。核心关注相对提升，非绝对值。\n\n## GPU 预算\n- bjb1-18228 (4× RTX 4090): eval-acr(cuda:1) + eval-reconvla(cuda:2) + eval-scalar-unc(cuda:3) + crm-train-k5(cuda:0)\n- bjb2-40593 (1× RTX 4090 D): eval-vla-mean-spatial(cuda:0)\n- 总预算 ~200 GPU·h, 已用 ~80h, 剩余 ~120h\n\n## 关键路径\n**当前**: 5 路 spatial eval 并行 → 完整对比表 → claim 判定 → object benchmark / framing 调整\n**风险**: ACR-VLA 早期信号低于 baseline（仅 2/10 tasks），等完整结果\n\n## 关键决策日志\n\n| ID | 日期 | 摘要 | 关联实验 |\n|----|------|------|----------|\n| D015 | 2026-05-14 | D015: SFT Gate 30% — 继续推进，不换模型，关注相对提升 | eval-spatial-v7-full, eval-object-v8-full |\n| D014 | 2026-05-13 | ReconVLA baseline 描述严重失实——重命名为 SampleConsensus，启动  | eval-reconvla-spatial-v2 |\n| D013 | 2026-05-13 | D013: D012 的 55.6% 不可靠 — wrapper 需对齐 lerobot 标准推理管 | eval-smolvla-libero-spatial |\n| D012 | 2026-05-13 | D012: smolvla_libero wrapper 修复后 55.6% — 取消 SFT，直接 | eval-smolvla-libero-spatial, sft-smolvla-libero |\n| D011 | 2026-05-13 | D011: 正式放弃 CoRL 2026，目标 ICLR 2027 | — |\n| D010 | 2026-05-13 | D010: 正式触发 SFT fallback — smolvla_libero 0% 确认不可用， | eval-smolvla-libero-spatial, sft-smolvla-libero |\n| D009 | 2026-05-13 | D008 补充：优先尝试社区 checkpoint lerobot/smolvla_libero，> | plan_001, plan_014 |\n| D008 | 2026-05-13 | SmolVLA 未 LIBERO fine-tuned，选方案 A：先 LoRA SFT SmolV | plan_001, plan_014 |\n| D007 | 2026-05-13 | Precompute 加速策略：缩减数据(10 demos/task) + 4-GPU 并行 + 代 | plan_001, plan_014 |\n| D006 | 2026-05-13 | Dream 审稿分析完成：proceed + 加 3 个新实验（ReconVLA baseline, | — |\n\n\n",
    "structuredPatch": [
      {
        "oldStart": 34,
        "oldLines": 7,
        "newStart": 34,
        "newLines": 7,
        "lines": [
          " D015: 30% baseline 继续推进。核心关注相对提升，非绝对值。",
          " ",
          " ## GPU 预算",
          "-- bjb1-18228 (4× RTX 4090): eval-acr(cuda:1) + eval-reconvla(cuda:2) + eval-scalar-unc(cuda:3) + crm-train-k5(cuda:0)",
          "+- bjb1-18228 (4× RTX 4090): eval-k5-spatial(cuda:0) + eval-acr(cuda:1) + eval-reconvla(cuda:2) + eval-scalar-unc(cuda:3)",
          " - bjb2-40593 (1× RTX 4090 D): eval-vla-mean-spatial(cuda:0)",
          " - 总预算 ~200 GPU·h, 已用 ~80h, 剩余 ~120h",
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

### Tool call

_source line 15_

<details open><summary>🔧 Tool call — Edit · `toolu_01M88DiaAzmNyX3g1QxoHyrW`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md",
  "old_string": "**当前**: 5 路 spatial eval 并行 → 完整对比表 → claim 判定 → object benchmark / framing 调整\n**风险**: ACR-VLA 早期信号低于 baseline（仅 2/10 tasks），等完整结果",
  "new_string": "**当前**: 5 路 eval 全部在跑 → 完整对比表 → 如果 ACR-VLA < baseline 确认，需要 framing 调整\n**风险 1**: ACR-VLA 早期信号低于 baseline（仅 2/10 tasks），等完整结果\n**风险 2**: CRM over-correction 退化（ACR 23-26% vs baseline 30%），可能需要 correction clipping/gating 实验"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f652a67f-4d9e-40df-a607-b3e5b9ea97e0",
  "uuid": "b870edb9-fbab-4503-ab46-af9172f8d368",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UiPLsi8YBSWm1UXMErhR2h",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 324,
      "cache_read_input_tokens": 26316,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 324
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

_source line 16 · 2026-05-14T07:36:07.905Z_

<details><summary>↩ Tool result · `toolu_01M88DiaAzmNyX3g1QxoHyrW`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f652a67f-4d9e-40df-a607-b3e5b9ea97e0",
  "uuid": "5a08d54e-6de0-46d4-9200-515cded8674c",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/ROADMAP.md",
    "oldString": "**当前**: 5 路 spatial eval 并行 → 完整对比表 → claim 判定 → object benchmark / framing 调整\n**风险**: ACR-VLA 早期信号低于 baseline（仅 2/10 tasks），等完整结果",
    "newString": "**当前**: 5 路 eval 全部在跑 → 完整对比表 → 如果 ACR-VLA < baseline 确认，需要 framing 调整\n**风险 1**: ACR-VLA 早期信号低于 baseline（仅 2/10 tasks），等完整结果\n**风险 2**: CRM over-correction 退化（ACR 23-26% vs baseline 30%），可能需要 correction clipping/gating 实验",
    "originalFile": "# acr-vla-conformal-refinement — Research Dashboard\n\n> 最后更新: 2026-05-14 16:00 UTC | 更新原因: crm-train-k5 完成 + eval-k5-spatial 启动，竞品分析完成，CRM correction 退化现象确认\n\n## 核心方向\nPer-DOF conformal statistics from multivariate CP on flow-matching VLA samples enable dimension-selective action correction. 详见 paper_framing.md。\n\n## 投稿目标\n**ICLR 2027**（预计 DDL Sep-Oct 2026）。CoRL 2026 已放弃（D011）。\n\n## 当前进展\n- **阶段**: Phase 2 — Spatial Eval 四路对比（ACR-VLA / SampleConsensus / Scalar-CRM / VLA-mean）\n- **MVP**: PASS（plan_000, per-DOF > scalar > none 确认）\n- **SFT Gate**: 30% baseline，决定继续（D015）\n- **CRM 训练完成**: per-DOF val_loss=0.009, scalar_unc=0.008, obs_only=0.018（conformal features 2× 改善确认）\n- **Baselines 锁定**: spatial 30% (K=1), object 13% (K=1)\n- **早期信号（2/10 tasks，不构成结论）**: ACR-VLA 在简单任务上低于 baseline，per-DOF CRM 可能在简单任务上引入有害 correction\n- **竞品分析完成** (art_20260514_621600): 核心竞品 ReconVLA（最直接）、SC-VLA、VLA-Pilot、ACoT-VLA\n- **CRM correction 退化现象**: ACR-VLA 中间结果 (23-26%) 低于 baseline (30%)，SampleConsensus 领先 (42.9%)\n- **文献调研完成** (art_20260514_d21dd2): correction degradation 可能原因与补救方向（correction clipping/gating 等）\n\n## 近期任务\n- [ ] eval-acr-spatial-v2 完成 → 核心 claim 判定（ACR-VLA vs baseline 30%）\n- [ ] eval-reconvla-spatial-v3 完成 → SampleConsensus 对比\n- [ ] eval-scalar-unc-spatial 完成 → scalar vs per-DOF 最终裁决\n- [x] crm-train-k5 完成 → K sensitivity ablation + eval-k5-spatial 已启动\n- [ ] eval-k5-spatial 完成 → K=5 sensitivity ablation 结果\n- [ ] eval-vla-mean-spatial 完成 → 隔离多采样平均贡献\n- [x] 代码同步 bjb1→bjb2（evaluate.py + train_crm.py）— MD5 verified\n- [ ] 完整 spatial 四路对比表出炉 → 决定是否铺 object benchmark\n- [ ] paper_framing.md 更新竞品定位（SC-VLA, VLA-Pilot, ACoT-VLA SOTA）\n\n## SFT Gate\nD015: 30% baseline 继续推进。核心关注相对提升，非绝对值。\n\n## GPU 预算\n- bjb1-18228 (4× RTX 4090): eval-k5-spatial(cuda:0) + eval-acr(cuda:1) + eval-reconvla(cuda:2) + eval-scalar-unc(cuda:3)\n- bjb2-40593 (1× RTX 4090 D): eval-vla-mean-spatial(cuda:0)\n- 总预算 ~200 GPU·h, 已用 ~80h, 剩余 ~120h\n\n## 关键路径\n**当前**: 5 路 spatial eval 并行 → 完整对比表 → claim 判定 → object benchmark / framing 调整\n**风险**: ACR-VLA 早期信号低于 baseline（仅 2/10 tasks），等完整结果\n\n## 关键决策日志\n\n| ID | 日期 | 摘要 | 关联实验 |\n|----|------|------|----------|\n| D015 | 2026-05-14 | D015: SFT Gate 30% — 继续推进，不换模型，关注相对提升 | eval-spatial-v7-full, eval-object-v8-full |\n| D014 | 2026-05-13 | ReconVLA baseline 描述严重失实——重命名为 SampleConsensus，启动  | eval-reconvla-spatial-v2 |\n| D013 | 2026-05-13 | D013: D012 的 55.6% 不可靠 — wrapper 需对齐 lerobot 标准推理管 | eval-smolvla-libero-spatial |\n| D012 | 2026-05-13 | D012: smolvla_libero wrapper 修复后 55.6% — 取消 SFT，直接 | eval-smolvla-libero-spatial, sft-smolvla-libero |\n| D011 | 2026-05-13 | D011: 正式放弃 CoRL 2026，目标 ICLR 2027 | — |\n| D010 | 2026-05-13 | D010: 正式触发 SFT fallback — smolvla_libero 0% 确认不可用， | eval-smolvla-libero-spatial, sft-smolvla-libero |\n| D009 | 2026-05-13 | D008 补充：优先尝试社区 checkpoint lerobot/smolvla_libero，> | plan_001, plan_014 |\n| D008 | 2026-05-13 | SmolVLA 未 LIBERO fine-tuned，选方案 A：先 LoRA SFT SmolV | plan_001, plan_014 |\n| D007 | 2026-05-13 | Precompute 加速策略：缩减数据(10 demos/task) + 4-GPU 并行 + 代 | plan_001, plan_014 |\n| D006 | 2026-05-13 | Dream 审稿分析完成：proceed + 加 3 个新实验（ReconVLA baseline, | — |\n\n\n",
    "structuredPatch": [
      {
        "oldStart": 39,
        "oldLines": 8,
        "newStart": 39,
        "newLines": 9,
        "lines": [
          " - 总预算 ~200 GPU·h, 已用 ~80h, 剩余 ~120h",
          " ",
          " ## 关键路径",
          "-**当前**: 5 路 spatial eval 并行 → 完整对比表 → claim 判定 → object benchmark / framing 调整",
          "-**风险**: ACR-VLA 早期信号低于 baseline（仅 2/10 tasks），等完整结果",
          "+**当前**: 5 路 eval 全部在跑 → 完整对比表 → 如果 ACR-VLA < baseline 确认，需要 framing 调整",
          "+**风险 1**: ACR-VLA 早期信号低于 baseline（仅 2/10 tasks），等完整结果",
          "+**风险 2**: CRM over-correction 退化（ACR 23-26% vs baseline 30%），可能需要 correction clipping/gating 实验",
          " ",
          " ## 关键决策日志",
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

_source line 17_

更新完成。变更摘要：
- 勾选 crm-train-k5 和代码同步两项，新增 eval-k5-spatial 任务
- GPU 预算：bjb1:cuda:0 从 crm-train-k5 改为 eval-k5-spatial
- 当前进展新增：竞品分析完成、CRM correction 退化现象、文献调研完成
- 关键路径新增 CRM over-correction 风险

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f652a67f-4d9e-40df-a607-b3e5b9ea97e0",
  "uuid": "fb0b2de5-59b9-4c95-89ca-dbba9498e9da",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P44K5nx8P774Gzh1pFWgD9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 403,
      "cache_read_input_tokens": 26640,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 403
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

_source line 18_

更新完成。变更摘要：
- 勾选 crm-train-k5 和代码同步两项，新增 eval-k5-spatial 任务
- GPU 预算：bjb1:cuda:0 从 crm-train-k5 改为 eval-k5-spatial
- 当前进展新增：竞品分析完成、CRM correction 退化现象、文献调研完成
- 关键路径新增 CRM over-correction 风险

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 31887,
  "duration_api_ms": 33863,
  "num_turns": 7,
  "stop_reason": "end_turn",
  "session_id": "f652a67f-4d9e-40df-a607-b3e5b9ea97e0",
  "total_cost_usd": 0.22685750000000002,
  "usage": {
    "input_tokens": 9,
    "cache_creation_input_tokens": 15202,
    "cache_read_input_tokens": 164370,
    "output_tokens": 1933,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 15202,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 134,
        "cache_read_input_tokens": 26640,
        "cache_creation_input_tokens": 403,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 403
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1215,
      "outputTokens": 15,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.00129,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 9,
      "outputTokens": 1933,
      "cacheReadInputTokens": 164370,
      "cacheCreationInputTokens": 15202,
      "webSearchRequests": 0,
      "costUSD": 0.22556750000000003,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "0ac62df9-02c0-4e98-8a4d-89dccd6e496b"
}
```

</details>

---
