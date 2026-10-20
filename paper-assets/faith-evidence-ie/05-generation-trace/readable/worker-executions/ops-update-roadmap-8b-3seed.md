# ops update roadmap 8b 3seed

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 26
- **Recorded user turns:** 0
- **Tool calls:** 9
- **Original source:** `logs/workers/worker_ops_update_roadmap_8b_3seed_20260519T172913.log`
- **Structured JSON:** [`c37ad1b6671377bca21f.json`](../../sessions/c3/c37ad1b6671377bca21f.json)

## Before a recorded user message

26 recorded events

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
  "session_id": "b6fdd47b-2526-4425-9a48-a46eb2f42ea9",
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
  "uuid": "48d4480c-2ebe-4842-8827-dc1c1bac6981",
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
    "resetsAt": 1779229200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "ba70f22b-a8e7-43c1-a72e-323160cc4b1d",
  "session_id": "b6fdd47b-2526-4425-9a48-a46eb2f42ea9"
}
```

---

### Assistant

_source line 4_

Let me read the current ROADMAP first.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b6fdd47b-2526-4425-9a48-a46eb2f42ea9",
  "uuid": "2b0f187d-e4f9-45c0-ad58-f8af51083af0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J8azN2awCMM1HxKp3pXc19",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12908,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12908
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

<details open><summary>🔧 Tool call — Read · `toolu_015gzAkmYRU1rwkVK8WvxnbZ`</summary>

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
  "session_id": "b6fdd47b-2526-4425-9a48-a46eb2f42ea9",
  "uuid": "ec32dc19-32d9-4706-8450-4bee5bb41917",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J8azN2awCMM1HxKp3pXc19",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12908,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12908
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

_source line 6 · 2026-05-19T17:29:24.411Z_

<details><summary>↩ Tool result · `toolu_015gzAkmYRU1rwkVK8WvxnbZ`</summary>

```text
1	# faith-evidence-ie — Research Dashboard
2	
3	> 最后更新: 2026-05-19 09:30 UTC | 更新原因: D117 14B evidence tax=0 + D118 1.7B claim 降级 + D112 bf16 完成 (0.5152) + 8B SFT 3-seed (0.5019) + scaling table 4行
4	
5	## 核心方向
6	FREIGE: LLM-based evidence-grounded DocRE 系统性研究。3 贡献：RSFT+NLI 有效性 / Decoupling spectrum / Scale-dependent evidence tax。详见 paper_framing.md。
7	
8	## 当前进展
9	- **阶段**: 🚀 Research + 审稿并行（Round 1 = 3.0 Findings，目标 4.0 Main）
10	- **Wave 1**: ✅ 全部完成（SFT seeds, GRPO bf16, Random RSFT）
11	- **Scaling seeds (plan_019)**: 8B 3-seed SFT 完成（mean=0.5019±3.72pp）；8B 2-seed RSFT 完成（D115: s44=0.5451, variance 0.53pp）
12	- **D112 full pipeline**: ✅ 完成（bf16 LoRA RSFT from SFT s44: ign_f1=0.5152, +4.18pp over SFT s44 baseline 0.4734）
13	- **14B SFT (plan_017)**: ✅ 完成（D117: with-evidence 0.5507, no-evidence 0.551, evidence tax=0.03pp≈0）
14	- **D118 claim 降级**: 1.7B RSFT (0.5122) vs 8B SFT mean (0.5019) Δ=+1.03pp, p≈0.34 不显著，降级为 "comparable / on par with"
15	- **关键数值汇总**:
16	
17	| Scale | SFT mean (seeds) | RSFT mean (seeds) | Δ ign_f1 | SFT std | RSFT std |
18	|-------|-------------------|--------------------|----------|---------|----------|
19	| 1.7B | 0.4464 (3) | 0.5122 (1, s42 base) | +6.58pp | 2.79pp | — |
20	| 4B | 0.4358 (3) | 0.4482 (3, Method A) / 0.5152 (1, Method B) | +1.24pp / +4.18pp (vs s44) | 3.80pp | 0.51pp |
21	| 8B | 0.5019 (3) | 0.5414 (2, Method A) | +3.95pp | 3.72pp | 0.53pp |
22	| 14B | 0.5507 (1) | pending | — | — | — |
23	
24	- **14B evidence tax**: 0.03pp（本质为零），14B 容量足够同时输出 evidence 和 RE
25	- **RSFT variance 稳定化**: 8B SFT std=3.72pp → RSFT std=0.53pp (7x)；4B SFT std=3.80pp → RSFT std=0.51pp (7.5x)
26	- **CED 价值**: CED RSFT (0.4482) > Random RSFT (0.4114) > SFT (0.3974)，+3.68pp gap
27	- **GRPO**: bf16 ckpt-100 ign_f1=0.4431 无 catastrophic forgetting（D110），QLoRA 是 confound
28	
29	## 投稿目标
30	- **EMNLP 2026 Main** (ARR July cycle, ~July 15-25, **~57 天**)
31	
32	## 实验路线（3 层优先级）
33	
34	### Tier 1 — Main 必要条件
35	| 实验 | Plan ID | 状态 |
36	|------|---------|------|
37	| D102 k=1 方法论修正 | D102 | ✅ 完成 |
38	| SFT 4B s43 + s44 + s42 reeval | plan_w3_sft_seeds | ✅ 完成 (D111) |
39	| GRPO bf16 G=4 clean control | plan_015 | ✅ 完成 (D110/D113) |
40	| Random k=1 RSFT baseline | plan_w18_random | ✅ 完成 (D109) |
41	| 8B RSFT s44 seed expansion | plan_019 (8B) | ✅ 完成 (D115) |
42	| 8B SFT s43 eval | plan_019 | ✅ 完成 (ign_f1=0.5324) |
43	| D112 RSFT from SFT s44 (bf16) | plan_d112 | ✅ 完成 (D119: ign_f1=0.5152) |
44	| 14B SFT (第 4 尺度) | plan_017 | ✅ 完成 (D117: 0.5507, tax=0.03pp) |
45	| 1.7B RSFT s43/s44 重跑 | plan_019 (1.7B) | 🟡 进行中 |
46	
47	### Tier 2 — 大幅加分
48	| 实验 | Plan ID | 状态 |
49	|------|---------|------|
50	| 14B RSFT + no-evidence + eval | plan_017 (后续) | pending（待启动） |
51	| 8B RSFT s43 补齐第 3 seed | plan_019 | pending |
52	| NLI model ablation | plan_010 | pending |
53	| Evidence tax 机制分析 | plan_020 | pending |
54	| Deep error analysis | plan_021 | pending |
55	
56	### Tier 3 — 锦上添花
57	| 实验 | Plan ID | 状态 |
58	|------|---------|------|
59	| CDR/GDA 跨领域 | plan_018 | P2（无 evidence 标注） |
60	| 第三模型家族 | plan_022 | pending |
61	| DocKS-RAG/LMRC 复现 | plan_023 | pending |
62	
63	## 从 3.0 → 4.0 路径
64	| 里程碑 | 预期评分 | 状态 |
65	|--------|---------|------|
66	| Wave 1 完成 + D112 | 3.0 → 3.5 | ✅ D112 完成 (0.5152, +4.18pp) |
67	| + 1.7B/8B multi-seed 统计力 | 3.5 | 🟡 8B 3-seed done, 1.7B 进行中 |
68	| + 14B 第 4 尺度档 | 3.5 → 3.75 | ✅ SFT 完成 (0.5507), RSFT pending |
69	| + Mechanistic + error analysis | 3.75 → 4.0 | pending |
70	
71	## GPU 分布
72	- cuda:0: 8B RSFT no-evidence eval r2（接近完成）
73	- cuda:1: D112 no-evidence eval r3（44%）
74	- cuda:2: 空闲
75	- cuda:3: 1.7B no-evidence eval 2048（38%）
76	
77	## 近期任务
78	- [x] Wave 1 全部完成（SFT seeds, GRPO bf16, Random RSFT）
79	- [x] 8B RSFT s44 eval (D115: 0.5451, variance 压缩 5x)
80	- [x] 4B SFT s42 D076 reeval (D111: 0.3974)
81	- [x] D112 step 4 eval 完成 (bf16 LoRA: ign_f1=0.5152, +4.18pp)
82	- [x] 8B SFT s43 eval 完成 (ign_f1=0.5324)
83	- [x] 14B SFT eval 完成 (D117: ign_f1=0.5507, evidence tax=0.03pp)
84	- [ ] 1.7B no-evidence eval 2048 重跑（排除截断，cuda:3）
85	- [ ] 8B RSFT no-evidence eval（cuda:0，接近完成）
86	- [ ] D112 no-evidence eval r3（cuda:1，44%）
87	- [ ] 14B RSFT pipeline（待启动）
88	- [ ] 8B RSFT s43 补齐第 3 seed
89	- [ ] experiment_plan.yaml 全面同步 registry
90	- [ ] paper_framing.md 更新（D112 + D117 + D118 narrative 调整）
91	- [ ] 重新提交论文审稿
92	
93	## 关键风险
94	- **D112 结果**: ✅ 已确认 RSFT-from-s44 (0.5152) > SFT s44 (0.4734) +4.18pp，Claim 1 robust
95	- **1.7B claim 已降级 (D118)**: 1.7B RSFT vs 8B SFT Δ=+1.03pp, p≈0.34 不显著，改为 "comparable"；RSFT variance stabilization (SFT std=3.72pp vs RSFT std=0.53pp) 作为独立发现
96	- **14B evidence tax = 0 (D117)**: 积极结果，14B 容量足够，Claim 3 需调整为 "tax scales inversely with model capacity"
97	- **8B RSFT evidence quality trade-off**: EDCR 从 0.65-0.67 降到 0.62（RE↑/evidence precision↓），论文需讨论
98	- **14B RSFT 待启动**: SFT 已完成，RSFT pipeline 是 Tier 2 首要任务
99	- **EDCR 缺人工验证**: plan_013 取消，用 per-relation 分析 + Limitations 缓解
100	
101	## 关键决策日志
102	
103	| ID | 日期 | 摘要 | 关联实验 |
104	|----|------|------|----------|
105	| D120 | 2026-05-19 | D120: 8B RSFT 3-seed 确认 variance compression 7.4×， | d102_8b_rsft_k1_s43, plan019_8b_rsft_s44_eval |
106	| D119 | 2026-05-19 | D119: D112 bf16 eval ign_f1=0.5152 确认 Method B (RS | d112_rsft_s44_eval_bf16, d112_rsft_s44_eval |
107	| D118 | 2026-05-19 | D118: "1.7B RSFT surpasses 8B SFT" claim 降级为 "appr | plan019_8b_sft_s43_eval, plan019_1_7b_rsft_s44_r2_eval |
108	| D117 | 2026-05-19 | D117: 14B SFT evidence tax = 0.03pp（本质为零），完成 4 尺度  | plan017_14b_sft_eval_r2, plan017_14b_sft_no_evidence_eval_r2 |
109	| D116 | 2026-05-19 | D116: D112 结果无效（QLoRA confound），必须用 bf16 LoRA 重跑 s | d112_rsft_s44_eval, d112_rsft_s44_train |
110	| D115 | 2026-05-19 | D115: 8B RSFT s44 ign_f1=0.5451 确认 RSFT 跨 seed 稳健， | plan019_8b_rsft_s44_eval, eval_rsft_ced_s42 |
111	| D114 | 2026-05-19 | D114: 1.7B RSFT s43/s44 应使用 Method A（s42 SFT base） | plan019_1_7b_rsft_s43, plan019_1_7b_rsft_s44, d112_rsft_s44_ced_score |
112	| D113 | 2026-05-18 | D113: GRPO bf16 ckpt-100 为最优 checkpoint，ckpt-200 无 | grpo_bf16_g4_ckpt100_eval, grpo_bf16_g4_ckpt200_eval |
113	| D112 | 2026-05-18 | D112: 4B RSFT ign_f1 claim 需重大 reframe——全部 RSFT 基于 | wave1_sft_4b_s43_eval_r2, wave1_sft_4b_s44_eval_r2, eval_rsft_ced_s42 |
114	| D111 | 2026-05-18 | D111: 4B SFT s42 必须用 D076 协议重新 eval，统一三 seed 参考基准 | wave1_sft_4b_s43_eval_r2, wave1_sft_4b_s44_eval_r2 |
115	
116	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b6fdd47b-2526-4425-9a48-a46eb2f42ea9",
  "uuid": "25e77959-fe03-423b-a7da-8bac1592b407",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/ROADMAP.md",
      "content": "# faith-evidence-ie — Research Dashboard\n\n> 最后更新: 2026-05-19 09:30 UTC | 更新原因: D117 14B evidence tax=0 + D118 1.7B claim 降级 + D112 bf16 完成 (0.5152) + 8B SFT 3-seed (0.5019) + scaling table 4行\n\n## 核心方向\nFREIGE: LLM-based evidence-grounded DocRE 系统性研究。3 贡献：RSFT+NLI 有效性 / Decoupling spectrum / Scale-dependent evidence tax。详见 paper_framing.md。\n\n## 当前进展\n- **阶段**: 🚀 Research + 审稿并行（Round 1 = 3.0 Findings，目标 4.0 Main）\n- **Wave 1**: ✅ 全部完成（SFT seeds, GRPO bf16, Random RSFT）\n- **Scaling seeds (plan_019)**: 8B 3-seed SFT 完成（mean=0.5019±3.72pp）；8B 2-seed RSFT 完成（D115: s44=0.5451, variance 0.53pp）\n- **D112 full pipeline**: ✅ 完成（bf16 LoRA RSFT from SFT s44: ign_f1=0.5152, +4.18pp over SFT s44 baseline 0.4734）\n- **14B SFT (plan_017)**: ✅ 完成（D117: with-evidence 0.5507, no-evidence 0.551, evidence tax=0.03pp≈0）\n- **D118 claim 降级**: 1.7B RSFT (0.5122) vs 8B SFT mean (0.5019) Δ=+1.03pp, p≈0.34 不显著，降级为 \"comparable / on par with\"\n- **关键数值汇总**:\n\n| Scale | SFT mean (seeds) | RSFT mean (seeds) | Δ ign_f1 | SFT std | RSFT std |\n|-------|-------------------|--------------------|----------|---------|----------|\n| 1.7B | 0.4464 (3) | 0.5122 (1, s42 base) | +6.58pp | 2.79pp | — |\n| 4B | 0.4358 (3) | 0.4482 (3, Method A) / 0.5152 (1, Method B) | +1.24pp / +4.18pp (vs s44) | 3.80pp | 0.51pp |\n| 8B | 0.5019 (3) | 0.5414 (2, Method A) | +3.95pp | 3.72pp | 0.53pp |\n| 14B | 0.5507 (1) | pending | — | — | — |\n\n- **14B evidence tax**: 0.03pp（本质为零），14B 容量足够同时输出 evidence 和 RE\n- **RSFT variance 稳定化**: 8B SFT std=3.72pp → RSFT std=0.53pp (7x)；4B SFT std=3.80pp → RSFT std=0.51pp (7.5x)\n- **CED 价值**: CED RSFT (0.4482) > Random RSFT (0.4114) > SFT (0.3974)，+3.68pp gap\n- **GRPO**: bf16 ckpt-100 ign_f1=0.4431 无 catastrophic forgetting（D110），QLoRA 是 confound\n\n## 投稿目标\n- **EMNLP 2026 Main** (ARR July cycle, ~July 15-25, **~57 天**)\n\n## 实验路线（3 层优先级）\n\n### Tier 1 — Main 必要条件\n| 实验 | Plan ID | 状态 |\n|------|---------|------|\n| D102 k=1 方法论修正 | D102 | ✅ 完成 |\n| SFT 4B s43 + s44 + s42 reeval | plan_w3_sft_seeds | ✅ 完成 (D111) |\n| GRPO bf16 G=4 clean control | plan_015 | ✅ 完成 (D110/D113) |\n| Random k=1 RSFT baseline | plan_w18_random | ✅ 完成 (D109) |\n| 8B RSFT s44 seed expansion | plan_019 (8B) | ✅ 完成 (D115) |\n| 8B SFT s43 eval | plan_019 | ✅ 完成 (ign_f1=0.5324) |\n| D112 RSFT from SFT s44 (bf16) | plan_d112 | ✅ 完成 (D119: ign_f1=0.5152) |\n| 14B SFT (第 4 尺度) | plan_017 | ✅ 完成 (D117: 0.5507, tax=0.03pp) |\n| 1.7B RSFT s43/s44 重跑 | plan_019 (1.7B) | 🟡 进行中 |\n\n### Tier 2 — 大幅加分\n| 实验 | Plan ID | 状态 |\n|------|---------|------|\n| 14B RSFT + no-evidence + eval | plan_017 (后续) | pending（待启动） |\n| 8B RSFT s43 补齐第 3 seed | plan_019 | pending |\n| NLI model ablation | plan_010 | pending |\n| Evidence tax 机制分析 | plan_020 | pending |\n| Deep error analysis | plan_021 | pending |\n\n### Tier 3 — 锦上添花\n| 实验 | Plan ID | 状态 |\n|------|---------|------|\n| CDR/GDA 跨领域 | plan_018 | P2（无 evidence 标注） |\n| 第三模型家族 | plan_022 | pending |\n| DocKS-RAG/LMRC 复现 | plan_023 | pending |\n\n## 从 3.0 → 4.0 路径\n| 里程碑 | 预期评分 | 状态 |\n|--------|---------|------|\n| Wave 1 完成 + D112 | 3.0 → 3.5 | ✅ D112 完成 (0.5152, +4.18pp) |\n| + 1.7B/8B multi-seed 统计力 | 3.5 | 🟡 8B 3-seed done, 1.7B 进行中 |\n| + 14B 第 4 尺度档 | 3.5 → 3.75 | ✅ SFT 完成 (0.5507), RSFT pending |\n| + Mechanistic + error analysis | 3.75 → 4.0 | pending |\n\n## GPU 分布\n- cuda:0: 8B RSFT no-evidence eval r2（接近完成）\n- cuda:1: D112 no-evidence eval r3（44%）\n- cuda:2: 空闲\n- cuda:3: 1.7B no-evidence eval 2048（38%）\n\n## 近期任务\n- [x] Wave 1 全部完成（SFT seeds, GRPO bf16, Random RSFT）\n- [x] 8B RSFT s44 eval (D115: 0.5451, variance 压缩 5x)\n- [x] 4B SFT s42 D076 reeval (D111: 0.3974)\n- [x] D112 step 4 eval 完成 (bf16 LoRA: ign_f1=0.5152, +4.18pp)\n- [x] 8B SFT s43 eval 完成 (ign_f1=0.5324)\n- [x] 14B SFT eval 完成 (D117: ign_f1=0.5507, evidence tax=0.03pp)\n- [ ] 1.7B no-evidence eval 2048 重跑（排除截断，cuda:3）\n- [ ] 8B RSFT no-evidence eval（cuda:0，接近完成）\n- [ ] D112 no-evidence eval r3（cuda:1，44%）\n- [ ] 14B RSFT pipeline（待启动）\n- [ ] 8B RSFT s43 补齐第 3 seed\n- [ ] experiment_plan.yaml 全面同步 registry\n- [ ] paper_framing.md 更新（D112 + D117 + D118 narrative 调整）\n- [ ] 重新提交论文审稿\n\n## 关键风险\n- **D112 结果**: ✅ 已确认 RSFT-from-s44 (0.5152) > SFT s44 (0.4734) +4.18pp，Claim 1 robust\n- **1.7B claim 已降级 (D118)**: 1.7B RSFT vs 8B SFT Δ=+1.03pp, p≈0.34 不显著，改为 \"comparable\"；RSFT variance stabilization (SFT std=3.72pp vs RSFT std=0.53pp) 作为独立发现\n- **14B evidence tax = 0 (D117)**: 积极结果，14B 容量足够，Claim 3 需调整为 \"tax scales inversely with model capacity\"\n- **8B RSFT evidence quality trade-off**: EDCR 从 0.65-0.67 降到 0.62（RE↑/evidence precision↓），论文需讨论\n- **14B RSFT 待启动**: SFT 已完成，RSFT pipeline 是 Tier 2 首要任务\n- **EDCR 缺人工验证**: plan_013 取消，用 per-relation 分析 + Limitations 缓解\n\n## 关键决策日志\n\n| ID | 日期 | 摘要 | 关联实验 |\n|----|------|------|----------|\n| D120 | 2026-05-19 | D120: 8B RSFT 3-seed 确认 variance compression 7.4×， | d102_8b_rsft_k1_s43, plan019_8b_rsft_s44_eval |\n| D119 | 2026-05-19 | D119: D112 bf16 eval ign_f1=0.5152 确认 Method B (RS | d112_rsft_s44_eval_bf16, d112_rsft_s44_eval |\n| D118 | 2026-05-19 | D118: \"1.7B RSFT surpasses 8B SFT\" claim 降级为 \"appr | plan019_8b_sft_s43_eval, plan019_1_7b_rsft_s44_r2_eval |\n| D117 | 2026-05-19 | D117: 14B SFT evidence tax = 0.03pp（本质为零），完成 4 尺度  | plan017_14b_sft_eval_r2, plan017_14b_sft_no_evidence_eval_r2 |\n| D116 | 2026-05-19 | D116: D112 结果无效（QLoRA confound），必须用 bf16 LoRA 重跑 s | d112_rsft_s44_eval, d112_rsft_s44_train |\n| D115 | 2026-05-19 | D115: 8B RSFT s44 ign_f1=0.5451 确认 RSFT 跨 seed 稳健， | plan019_8b_rsft_s44_eval, eval_rsft_ced_s42 |\n| D114 | 2026-05-19 | D114: 1.7B RSFT s43/s44 应使用 Method A（s42 SFT base） | plan019_1_7b_rsft_s43, plan019_1_7b_rsft_s44, d112_rsft_s44_ced_score |\n| D113 | 2026-05-18 | D113: GRPO bf16 ckpt-100 为最优 checkpoint，ckpt-200 无 | grpo_bf16_g4_ckpt100_eval, grpo_bf16_g4_ckpt200_eval |\n| D112 | 2026-05-18 | D112: 4B RSFT ign_f1 claim 需重大 reframe——全部 RSFT 基于 | wave1_sft_4b_s43_eval_r2, wave1_sft_4b_s44_eval_r2, eval_rsft_ced_s42 |\n| D111 | 2026-05-18 | D111: 4B SFT s42 必须用 D076 协议重新 eval，统一三 seed 参考基准 | wave1_sft_4b_s43_eval_r2, wave1_sft_4b_s44_eval_r2 |\n\n",
      "numLines": 116,
      "startLine": 1,
      "totalLines": 116
    }
  }
}
```

</details>

---

### Assistant

_source line 7_

<details><summary>Logged reasoning block</summary>

```text
Now I have the full file. Let me identify all the edits needed:

1. **Line 3**: Update timestamp and reason
2. **Line 11**: Update "8B 2-seed RSFT" to "8B 3-seed RSFT" with new stats
3. **Line 21**: Scaling table 8B row: update RSFT mean, Δ, RSFT std, add seed details
4. **Line 25**: Variance compression claim update
5. **Line 51**: Tier 2 "8B RSFT s43 补齐第 3 seed" → ✅ 完成


6. **Line 67**: Checking the status line — it already says "8B 3-seed done, 1.7B 进行中" which appears correct, so this might not need changes depending on what the task specifies.

7. **Lines 72-75**: GPU distribution needs updating.

8. **Line 88**: The near-term task for "8B RSFT s43 补齐第 3 seed" should be marked as complete.

9. **Line 95**: The variance numbers in the risk section need adjustment — specifically changing the RSFT standard deviation from 3.72pp to 0.50pp.

Let me go through and make these edits now.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b6fdd47b-2526-4425-9a48-a46eb2f42ea9",
  "uuid": "67f70025-9c1f-44d8-ada6-9bb5e8af4ba6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AGZndQ8rivy4WbK2ocDhEz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3888,
      "cache_read_input_tokens": 24355,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3888
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

_source line 8_

Now I'll apply all the edits.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b6fdd47b-2526-4425-9a48-a46eb2f42ea9",
  "uuid": "811c4ce2-7f25-4f07-a83e-3dc61bc0a3e9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AGZndQ8rivy4WbK2ocDhEz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3888,
      "cache_read_input_tokens": 24355,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3888
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

_source line 9_

<details open><summary>🔧 Tool call — Edit · `toolu_01DiWjkMKCmorvS5fkeP93Fj`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/ROADMAP.md",
  "old_string": "> 最后更新: 2026-05-19 09:30 UTC | 更新原因: D117 14B evidence tax=0 + D118 1.7B claim 降级 + D112 bf16 完成 (0.5152) + 8B SFT 3-seed (0.5019) + scaling table 4行",
  "new_string": "> 最后更新: 2026-05-19 UTC | 更新原因: 8B RSFT 3-seed 完成 (mean=0.5433±0.50pp, 7.4x variance compression)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b6fdd47b-2526-4425-9a48-a46eb2f42ea9",
  "uuid": "1707f73a-ce31-4480-803b-c1c79b52eb10",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AGZndQ8rivy4WbK2ocDhEz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3888,
      "cache_read_input_tokens": 24355,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3888
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

_source line 10 · 2026-05-19T17:29:46.767Z_

<details><summary>↩ Tool result · `toolu_01DiWjkMKCmorvS5fkeP93Fj`</summary>

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
  "session_id": "b6fdd47b-2526-4425-9a48-a46eb2f42ea9",
  "uuid": "b8067dd3-66d9-418d-8403-a0793a2a80d0",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/ROADMAP.md",
    "oldString": "> 最后更新: 2026-05-19 09:30 UTC | 更新原因: D117 14B evidence tax=0 + D118 1.7B claim 降级 + D112 bf16 完成 (0.5152) + 8B SFT 3-seed (0.5019) + scaling table 4行",
    "newString": "> 最后更新: 2026-05-19 UTC | 更新原因: 8B RSFT 3-seed 完成 (mean=0.5433±0.50pp, 7.4x variance compression)",
    "originalFile": "# faith-evidence-ie — Research Dashboard\n\n> 最后更新: 2026-05-19 09:30 UTC | 更新原因: D117 14B evidence tax=0 + D118 1.7B claim 降级 + D112 bf16 完成 (0.5152) + 8B SFT 3-seed (0.5019) + scaling table 4行\n\n## 核心方向\nFREIGE: LLM-based evidence-grounded DocRE 系统性研究。3 贡献：RSFT+NLI 有效性 / Decoupling spectrum / Scale-dependent evidence tax。详见 paper_framing.md。\n\n## 当前进展\n- **阶段**: 🚀 Research + 审稿并行（Round 1 = 3.0 Findings，目标 4.0 Main）\n- **Wave 1**: ✅ 全部完成（SFT seeds, GRPO bf16, Random RSFT）\n- **Scaling seeds (plan_019)**: 8B 3-seed SFT 完成（mean=0.5019±3.72pp）；8B 2-seed RSFT 完成（D115: s44=0.5451, variance 0.53pp）\n- **D112 full pipeline**: ✅ 完成（bf16 LoRA RSFT from SFT s44: ign_f1=0.5152, +4.18pp over SFT s44 baseline 0.4734）\n- **14B SFT (plan_017)**: ✅ 完成（D117: with-evidence 0.5507, no-evidence 0.551, evidence tax=0.03pp≈0）\n- **D118 claim 降级**: 1.7B RSFT (0.5122) vs 8B SFT mean (0.5019) Δ=+1.03pp, p≈0.34 不显著，降级为 \"comparable / on par with\"\n- **关键数值汇总**:\n\n| Scale | SFT mean (seeds) | RSFT mean (seeds) | Δ ign_f1 | SFT std | RSFT std |\n|-------|-------------------|--------------------|----------|---------|----------|\n| 1.7B | 0.4464 (3) | 0.5122 (1, s42 base) | +6.58pp | 2.79pp | — |\n| 4B | 0.4358 (3) | 0.4482 (3, Method A) / 0.5152 (1, Method B) | +1.24pp / +4.18pp (vs s44) | 3.80pp | 0.51pp |\n| 8B | 0.5019 (3) | 0.5414 (2, Method A) | +3.95pp | 3.72pp | 0.53pp |\n| 14B | 0.5507 (1) | pending | — | — | — |\n\n- **14B evidence tax**: 0.03pp（本质为零），14B 容量足够同时输出 evidence 和 RE\n- **RSFT variance 稳定化**: 8B SFT std=3.72pp → RSFT std=0.53pp (7x)；4B SFT std=3.80pp → RSFT std=0.51pp (7.5x)\n- **CED 价值**: CED RSFT (0.4482) > Random RSFT (0.4114) > SFT (0.3974)，+3.68pp gap\n- **GRPO**: bf16 ckpt-100 ign_f1=0.4431 无 catastrophic forgetting（D110），QLoRA 是 confound\n\n## 投稿目标\n- **EMNLP 2026 Main** (ARR July cycle, ~July 15-25, **~57 天**)\n\n## 实验路线（3 层优先级）\n\n### Tier 1 — Main 必要条件\n| 实验 | Plan ID | 状态 |\n|------|---------|------|\n| D102 k=1 方法论修正 | D102 | ✅ 完成 |\n| SFT 4B s43 + s44 + s42 reeval | plan_w3_sft_seeds | ✅ 完成 (D111) |\n| GRPO bf16 G=4 clean control | plan_015 | ✅ 完成 (D110/D113) |\n| Random k=1 RSFT baseline | plan_w18_random | ✅ 完成 (D109) |\n| 8B RSFT s44 seed expansion | plan_019 (8B) | ✅ 完成 (D115) |\n| 8B SFT s43 eval | plan_019 | ✅ 完成 (ign_f1=0.5324) |\n| D112 RSFT from SFT s44 (bf16) | plan_d112 | ✅ 完成 (D119: ign_f1=0.5152) |\n| 14B SFT (第 4 尺度) | plan_017 | ✅ 完成 (D117: 0.5507, tax=0.03pp) |\n| 1.7B RSFT s43/s44 重跑 | plan_019 (1.7B) | 🟡 进行中 |\n\n### Tier 2 — 大幅加分\n| 实验 | Plan ID | 状态 |\n|------|---------|------|\n| 14B RSFT + no-evidence + eval | plan_017 (后续) | pending（待启动） |\n| 8B RSFT s43 补齐第 3 seed | plan_019 | pending |\n| NLI model ablation | plan_010 | pending |\n| Evidence tax 机制分析 | plan_020 | pending |\n| Deep error analysis | plan_021 | pending |\n\n### Tier 3 — 锦上添花\n| 实验 | Plan ID | 状态 |\n|------|---------|------|\n| CDR/GDA 跨领域 | plan_018 | P2（无 evidence 标注） |\n| 第三模型家族 | plan_022 | pending |\n| DocKS-RAG/LMRC 复现 | plan_023 | pending |\n\n## 从 3.0 → 4.0 路径\n| 里程碑 | 预期评分 | 状态 |\n|--------|---------|------|\n| Wave 1 完成 + D112 | 3.0 → 3.5 | ✅ D112 完成 (0.5152, +4.18pp) |\n| + 1.7B/8B multi-seed 统计力 | 3.5 | 🟡 8B 3-seed done, 1.7B 进行中 |\n| + 14B 第 4 尺度档 | 3.5 → 3.75 | ✅ SFT 完成 (0.5507), RSFT pending |\n| + Mechanistic + error analysis | 3.75 → 4.0 | pending |\n\n## GPU 分布\n- cuda:0: 8B RSFT no-evidence eval r2（接近完成）\n- cuda:1: D112 no-evidence eval r3（44%）\n- cuda:2: 空闲\n- cuda:3: 1.7B no-evidence eval 2048（38%）\n\n## 近期任务\n- [x] Wave 1 全部完成（SFT seeds, GRPO bf16, Random RSFT）\n- [x] 8B RSFT s44 eval (D115: 0.5451, variance 压缩 5x)\n- [x] 4B SFT s42 D076 reeval (D111: 0.3974)\n- [x] D112 step 4 eval 完成 (bf16 LoRA: ign_f1=0.5152, +4.18pp)\n- [x] 8B SFT s43 eval 完成 (ign_f1=0.5324)\n- [x] 14B SFT eval 完成 (D117: ign_f1=0.5507, evidence tax=0.03pp)\n- [ ] 1.7B no-evidence eval 2048 重跑（排除截断，cuda:3）\n- [ ] 8B RSFT no-evidence eval（cuda:0，接近完成）\n- [ ] D112 no-evidence eval r3（cuda:1，44%）\n- [ ] 14B RSFT pipeline（待启动）\n- [ ] 8B RSFT s43 补齐第 3 seed\n- [ ] experiment_plan.yaml 全面同步 registry\n- [ ] paper_framing.md 更新（D112 + D117 + D118 narrative 调整）\n- [ ] 重新提交论文审稿\n\n## 关键风险\n- **D112 结果**: ✅ 已确认 RSFT-from-s44 (0.5152) > SFT s44 (0.4734) +4.18pp，Claim 1 robust\n- **1.7B claim 已降级 (D118)**: 1.7B RSFT vs 8B SFT Δ=+1.03pp, p≈0.34 不显著，改为 \"comparable\"；RSFT variance stabilization (SFT std=3.72pp vs RSFT std=0.53pp) 作为独立发现\n- **14B evidence tax = 0 (D117)**: 积极结果，14B 容量足够，Claim 3 需调整为 \"tax scales inversely with model capacity\"\n- **8B RSFT evidence quality trade-off**: EDCR 从 0.65-0.67 降到 0.62（RE↑/evidence precision↓），论文需讨论\n- **14B RSFT 待启动**: SFT 已完成，RSFT pipeline 是 Tier 2 首要任务\n- **EDCR 缺人工验证**: plan_013 取消，用 per-relation 分析 + Limitations 缓解\n\n## 关键决策日志\n\n| ID | 日期 | 摘要 | 关联实验 |\n|----|------|------|----------|\n| D120 | 2026-05-19 | D120: 8B RSFT 3-seed 确认 variance compression 7.4×， | d102_8b_rsft_k1_s43, plan019_8b_rsft_s44_eval |\n| D119 | 2026-05-19 | D119: D112 bf16 eval ign_f1=0.5152 确认 Method B (RS | d112_rsft_s44_eval_bf16, d112_rsft_s44_eval |\n| D118 | 2026-05-19 | D118: \"1.7B RSFT surpasses 8B SFT\" claim 降级为 \"appr | plan019_8b_sft_s43_eval, plan019_1_7b_rsft_s44_r2_eval |\n| D117 | 2026-05-19 | D117: 14B SFT evidence tax = 0.03pp（本质为零），完成 4 尺度  | plan017_14b_sft_eval_r2, plan017_14b_sft_no_evidence_eval_r2 |\n| D116 | 2026-05-19 | D116: D112 结果无效（QLoRA confound），必须用 bf16 LoRA 重跑 s | d112_rsft_s44_eval, d112_rsft_s44_train |\n| D115 | 2026-05-19 | D115: 8B RSFT s44 ign_f1=0.5451 确认 RSFT 跨 seed 稳健， | plan019_8b_rsft_s44_eval, eval_rsft_ced_s42 |\n| D114 | 2026-05-19 | D114: 1.7B RSFT s43/s44 应使用 Method A（s42 SFT base） | plan019_1_7b_rsft_s43, plan019_1_7b_rsft_s44, d112_rsft_s44_ced_score |\n| D113 | 2026-05-18 | D113: GRPO bf16 ckpt-100 为最优 checkpoint，ckpt-200 无 | grpo_bf16_g4_ckpt100_eval, grpo_bf16_g4_ckpt200_eval |\n| D112 | 2026-05-18 | D112: 4B RSFT ign_f1 claim 需重大 reframe——全部 RSFT 基于 | wave1_sft_4b_s43_eval_r2, wave1_sft_4b_s44_eval_r2, eval_rsft_ced_s42 |\n| D111 | 2026-05-18 | D111: 4B SFT s42 必须用 D076 协议重新 eval，统一三 seed 参考基准 | wave1_sft_4b_s43_eval_r2, wave1_sft_4b_s44_eval_r2 |\n\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 6,
        "newStart": 1,
        "newLines": 6,
        "lines": [
          " # faith-evidence-ie — Research Dashboard",
          " ",
          "-> 最后更新: 2026-05-19 09:30 UTC | 更新原因: D117 14B evidence tax=0 + D118 1.7B claim 降级 + D112 bf16 完成 (0.5152) + 8B SFT 3-seed (0.5019) + scaling table 4行",
          "+> 最后更新: 2026-05-19 UTC | 更新原因: 8B RSFT 3-seed 完成 (mean=0.5433±0.50pp, 7.4x variance compression)",
          " ",
          " ## 核心方向",
          " FREIGE: LLM-based evidence-grounded DocRE 系统性研究。3 贡献：RSFT+NLI 有效性 / Decoupling spectrum / Scale-dependent evidence tax。详见 paper_framing.md。"
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

<details open><summary>🔧 Tool call — Edit · `toolu_016fzf45SnXEq1CHM1qPFewy`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/ROADMAP.md",
  "old_string": "8B 2-seed RSFT 完成（D115: s44=0.5451, variance 0.53pp）",
  "new_string": "8B 3-seed RSFT 完成（s42=0.5376, s43=0.5471, s44=0.5451; mean=0.5433±0.50pp）"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b6fdd47b-2526-4425-9a48-a46eb2f42ea9",
  "uuid": "d4478f9a-60b5-4c91-bc06-7439197923a9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U37CnKn4gEy3MJee1whfGH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 855,
      "cache_read_input_tokens": 28243,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 855
      },
      "output_tokens": 67,
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

_source line 12 · 2026-05-19T17:29:56.197Z_

<details><summary>↩ Tool result · `toolu_016fzf45SnXEq1CHM1qPFewy`</summary>

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
  "session_id": "b6fdd47b-2526-4425-9a48-a46eb2f42ea9",
  "uuid": "537f2be1-496f-404d-ae31-f01b4d2b9947",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/ROADMAP.md",
    "oldString": "8B 2-seed RSFT 完成（D115: s44=0.5451, variance 0.53pp）",
    "newString": "8B 3-seed RSFT 完成（s42=0.5376, s43=0.5471, s44=0.5451; mean=0.5433±0.50pp）",
    "originalFile": "# faith-evidence-ie — Research Dashboard\n\n> 最后更新: 2026-05-19 UTC | 更新原因: 8B RSFT 3-seed 完成 (mean=0.5433±0.50pp, 7.4x variance compression)\n\n## 核心方向\nFREIGE: LLM-based evidence-grounded DocRE 系统性研究。3 贡献：RSFT+NLI 有效性 / Decoupling spectrum / Scale-dependent evidence tax。详见 paper_framing.md。\n\n## 当前进展\n- **阶段**: 🚀 Research + 审稿并行（Round 1 = 3.0 Findings，目标 4.0 Main）\n- **Wave 1**: ✅ 全部完成（SFT seeds, GRPO bf16, Random RSFT）\n- **Scaling seeds (plan_019)**: 8B 3-seed SFT 完成（mean=0.5019±3.72pp）；8B 2-seed RSFT 完成（D115: s44=0.5451, variance 0.53pp）\n- **D112 full pipeline**: ✅ 完成（bf16 LoRA RSFT from SFT s44: ign_f1=0.5152, +4.18pp over SFT s44 baseline 0.4734）\n- **14B SFT (plan_017)**: ✅ 完成（D117: with-evidence 0.5507, no-evidence 0.551, evidence tax=0.03pp≈0）\n- **D118 claim 降级**: 1.7B RSFT (0.5122) vs 8B SFT mean (0.5019) Δ=+1.03pp, p≈0.34 不显著，降级为 \"comparable / on par with\"\n- **关键数值汇总**:\n\n| Scale | SFT mean (seeds) | RSFT mean (seeds) | Δ ign_f1 | SFT std | RSFT std |\n|-------|-------------------|--------------------|----------|---------|----------|\n| 1.7B | 0.4464 (3) | 0.5122 (1, s42 base) | +6.58pp | 2.79pp | — |\n| 4B | 0.4358 (3) | 0.4482 (3, Method A) / 0.5152 (1, Method B) | +1.24pp / +4.18pp (vs s44) | 3.80pp | 0.51pp |\n| 8B | 0.5019 (3) | 0.5414 (2, Method A) | +3.95pp | 3.72pp | 0.53pp |\n| 14B | 0.5507 (1) | pending | — | — | — |\n\n- **14B evidence tax**: 0.03pp（本质为零），14B 容量足够同时输出 evidence 和 RE\n- **RSFT variance 稳定化**: 8B SFT std=3.72pp → RSFT std=0.53pp (7x)；4B SFT std=3.80pp → RSFT std=0.51pp (7.5x)\n- **CED 价值**: CED RSFT (0.4482) > Random RSFT (0.4114) > SFT (0.3974)，+3.68pp gap\n- **GRPO**: bf16 ckpt-100 ign_f1=0.4431 无 catastrophic forgetting（D110），QLoRA 是 confound\n\n## 投稿目标\n- **EMNLP 2026 Main** (ARR July cycle, ~July 15-25, **~57 天**)\n\n## 实验路线（3 层优先级）\n\n### Tier 1 — Main 必要条件\n| 实验 | Plan ID | 状态 |\n|------|---------|------|\n| D102 k=1 方法论修正 | D102 | ✅ 完成 |\n| SFT 4B s43 + s44 + s42 reeval | plan_w3_sft_seeds | ✅ 完成 (D111) |\n| GRPO bf16 G=4 clean control | plan_015 | ✅ 完成 (D110/D113) |\n| Random k=1 RSFT baseline | plan_w18_random | ✅ 完成 (D109) |\n| 8B RSFT s44 seed expansion | plan_019 (8B) | ✅ 完成 (D115) |\n| 8B SFT s43 eval | plan_019 | ✅ 完成 (ign_f1=0.5324) |\n| D112 RSFT from SFT s44 (bf16) | plan_d112 | ✅ 完成 (D119: ign_f1=0.5152) |\n| 14B SFT (第 4 尺度) | plan_017 | ✅ 完成 (D117: 0.5507, tax=0.03pp) |\n| 1.7B RSFT s43/s44 重跑 | plan_019 (1.7B) | 🟡 进行中 |\n\n### Tier 2 — 大幅加分\n| 实验 | Plan ID | 状态 |\n|------|---------|------|\n| 14B RSFT + no-evidence + eval | plan_017 (后续) | pending（待启动） |\n| 8B RSFT s43 补齐第 3 seed | plan_019 | pending |\n| NLI model ablation | plan_010 | pending |\n| Evidence tax 机制分析 | plan_020 | pending |\n| Deep error analysis | plan_021 | pending |\n\n### Tier 3 — 锦上添花\n| 实验 | Plan ID | 状态 |\n|------|---------|------|\n| CDR/GDA 跨领域 | plan_018 | P2（无 evidence 标注） |\n| 第三模型家族 | plan_022 | pending |\n| DocKS-RAG/LMRC 复现 | plan_023 | pending |\n\n## 从 3.0 → 4.0 路径\n| 里程碑 | 预期评分 | 状态 |\n|--------|---------|------|\n| Wave 1 完成 + D112 | 3.0 → 3.5 | ✅ D112 完成 (0.5152, +4.18pp) |\n| + 1.7B/8B multi-seed 统计力 | 3.5 | 🟡 8B 3-seed done, 1.7B 进行中 |\n| + 14B 第 4 尺度档 | 3.5 → 3.75 | ✅ SFT 完成 (0.5507), RSFT pending |\n| + Mechanistic + error analysis | 3.75 → 4.0 | pending |\n\n## GPU 分布\n- cuda:0: 8B RSFT no-evidence eval r2（接近完成）\n- cuda:1: D112 no-evidence eval r3（44%）\n- cuda:2: 空闲\n- cuda:3: 1.7B no-evidence eval 2048（38%）\n\n## 近期任务\n- [x] Wave 1 全部完成（SFT seeds, GRPO bf16, Random RSFT）\n- [x] 8B RSFT s44 eval (D115: 0.5451, variance 压缩 5x)\n- [x] 4B SFT s42 D076 reeval (D111: 0.3974)\n- [x] D112 step 4 eval 完成 (bf16 LoRA: ign_f1=0.5152, +4.18pp)\n- [x] 8B SFT s43 eval 完成 (ign_f1=0.5324)\n- [x] 14B SFT eval 完成 (D117: ign_f1=0.5507, evidence tax=0.03pp)\n- [ ] 1.7B no-evidence eval 2048 重跑（排除截断，cuda:3）\n- [ ] 8B RSFT no-evidence eval（cuda:0，接近完成）\n- [ ] D112 no-evidence eval r3（cuda:1，44%）\n- [ ] 14B RSFT pipeline（待启动）\n- [ ] 8B RSFT s43 补齐第 3 seed\n- [ ] experiment_plan.yaml 全面同步 registry\n- [ ] paper_framing.md 更新（D112 + D117 + D118 narrative 调整）\n- [ ] 重新提交论文审稿\n\n## 关键风险\n- **D112 结果**: ✅ 已确认 RSFT-from-s44 (0.5152) > SFT s44 (0.4734) +4.18pp，Claim 1 robust\n- **1.7B claim 已降级 (D118)**: 1.7B RSFT vs 8B SFT Δ=+1.03pp, p≈0.34 不显著，改为 \"comparable\"；RSFT variance stabilization (SFT std=3.72pp vs RSFT std=0.53pp) 作为独立发现\n- **14B evidence tax = 0 (D117)**: 积极结果，14B 容量足够，Claim 3 需调整为 \"tax scales inversely with model capacity\"\n- **8B RSFT evidence quality trade-off**: EDCR 从 0.65-0.67 降到 0.62（RE↑/evidence precision↓），论文需讨论\n- **14B RSFT 待启动**: SFT 已完成，RSFT pipeline 是 Tier 2 首要任务\n- **EDCR 缺人工验证**: plan_013 取消，用 per-relation 分析 + Limitations 缓解\n\n## 关键决策日志\n\n| ID | 日期 | 摘要 | 关联实验 |\n|----|------|------|----------|\n| D120 | 2026-05-19 | D120: 8B RSFT 3-seed 确认 variance compression 7.4×， | d102_8b_rsft_k1_s43, plan019_8b_rsft_s44_eval |\n| D119 | 2026-05-19 | D119: D112 bf16 eval ign_f1=0.5152 确认 Method B (RS | d112_rsft_s44_eval_bf16, d112_rsft_s44_eval |\n| D118 | 2026-05-19 | D118: \"1.7B RSFT surpasses 8B SFT\" claim 降级为 \"appr | plan019_8b_sft_s43_eval, plan019_1_7b_rsft_s44_r2_eval |\n| D117 | 2026-05-19 | D117: 14B SFT evidence tax = 0.03pp（本质为零），完成 4 尺度  | plan017_14b_sft_eval_r2, plan017_14b_sft_no_evidence_eval_r2 |\n| D116 | 2026-05-19 | D116: D112 结果无效（QLoRA confound），必须用 bf16 LoRA 重跑 s | d112_rsft_s44_eval, d112_rsft_s44_train |\n| D115 | 2026-05-19 | D115: 8B RSFT s44 ign_f1=0.5451 确认 RSFT 跨 seed 稳健， | plan019_8b_rsft_s44_eval, eval_rsft_ced_s42 |\n| D114 | 2026-05-19 | D114: 1.7B RSFT s43/s44 应使用 Method A（s42 SFT base） | plan019_1_7b_rsft_s43, plan019_1_7b_rsft_s44, d112_rsft_s44_ced_score |\n| D113 | 2026-05-18 | D113: GRPO bf16 ckpt-100 为最优 checkpoint，ckpt-200 无 | grpo_bf16_g4_ckpt100_eval, grpo_bf16_g4_ckpt200_eval |\n| D112 | 2026-05-18 | D112: 4B RSFT ign_f1 claim 需重大 reframe——全部 RSFT 基于 | wave1_sft_4b_s43_eval_r2, wave1_sft_4b_s44_eval_r2, eval_rsft_ced_s42 |\n| D111 | 2026-05-18 | D111: 4B SFT s42 必须用 D076 协议重新 eval，统一三 seed 参考基准 | wave1_sft_4b_s43_eval_r2, wave1_sft_4b_s44_eval_r2 |\n\n",
    "structuredPatch": [
      {
        "oldStart": 8,
        "oldLines": 7,
        "newStart": 8,
        "newLines": 7,
        "lines": [
          " ## 当前进展",
          " - **阶段**: 🚀 Research + 审稿并行（Round 1 = 3.0 Findings，目标 4.0 Main）",
          " - **Wave 1**: ✅ 全部完成（SFT seeds, GRPO bf16, Random RSFT）",
          "-- **Scaling seeds (plan_019)**: 8B 3-seed SFT 完成（mean=0.5019±3.72pp）；8B 2-seed RSFT 完成（D115: s44=0.5451, variance 0.53pp）",
          "+- **Scaling seeds (plan_019)**: 8B 3-seed SFT 完成（mean=0.5019±3.72pp）；8B 3-seed RSFT 完成（s42=0.5376, s43=0.5471, s44=0.5451; mean=0.5433±0.50pp）",
          " - **D112 full pipeline**: ✅ 完成（bf16 LoRA RSFT from SFT s44: ign_f1=0.5152, +4.18pp over SFT s44 baseline 0.4734）",
          " - **14B SFT (plan_017)**: ✅ 完成（D117: with-evidence 0.5507, no-evidence 0.551, evidence tax=0.03pp≈0）",
          " - **D118 claim 降级**: 1.7B RSFT (0.5122) vs 8B SFT mean (0.5019) Δ=+1.03pp, p≈0.34 不显著，降级为 \"comparable / on par with\""
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

<details open><summary>🔧 Tool call — Edit · `toolu_01MUq8DTRuRirNWsr8ja77YY`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/ROADMAP.md",
  "old_string": "| 8B | 0.5019 (3) | 0.5414 (2, Method A) | +3.95pp | 3.72pp | 0.53pp |",
  "new_string": "| 8B | 0.5019 (3) | 0.5433 (3, Method A) | +4.14pp | 3.72pp | 0.50pp |"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b6fdd47b-2526-4425-9a48-a46eb2f42ea9",
  "uuid": "cb27b816-2244-4d26-859a-d944b5e7fb56",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VYcP5ZDy14h87XBmpxuTDZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 271,
      "cache_read_input_tokens": 29098,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 271
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

_source line 14 · 2026-05-19T17:30:02.198Z_

<details><summary>↩ Tool result · `toolu_01MUq8DTRuRirNWsr8ja77YY`</summary>

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
  "session_id": "b6fdd47b-2526-4425-9a48-a46eb2f42ea9",
  "uuid": "4cfe1290-21ae-4301-b75d-cb49abb6bd8e",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/ROADMAP.md",
    "oldString": "| 8B | 0.5019 (3) | 0.5414 (2, Method A) | +3.95pp | 3.72pp | 0.53pp |",
    "newString": "| 8B | 0.5019 (3) | 0.5433 (3, Method A) | +4.14pp | 3.72pp | 0.50pp |",
    "originalFile": "# faith-evidence-ie — Research Dashboard\n\n> 最后更新: 2026-05-19 UTC | 更新原因: 8B RSFT 3-seed 完成 (mean=0.5433±0.50pp, 7.4x variance compression)\n\n## 核心方向\nFREIGE: LLM-based evidence-grounded DocRE 系统性研究。3 贡献：RSFT+NLI 有效性 / Decoupling spectrum / Scale-dependent evidence tax。详见 paper_framing.md。\n\n## 当前进展\n- **阶段**: 🚀 Research + 审稿并行（Round 1 = 3.0 Findings，目标 4.0 Main）\n- **Wave 1**: ✅ 全部完成（SFT seeds, GRPO bf16, Random RSFT）\n- **Scaling seeds (plan_019)**: 8B 3-seed SFT 完成（mean=0.5019±3.72pp）；8B 3-seed RSFT 完成（s42=0.5376, s43=0.5471, s44=0.5451; mean=0.5433±0.50pp）\n- **D112 full pipeline**: ✅ 完成（bf16 LoRA RSFT from SFT s44: ign_f1=0.5152, +4.18pp over SFT s44 baseline 0.4734）\n- **14B SFT (plan_017)**: ✅ 完成（D117: with-evidence 0.5507, no-evidence 0.551, evidence tax=0.03pp≈0）\n- **D118 claim 降级**: 1.7B RSFT (0.5122) vs 8B SFT mean (0.5019) Δ=+1.03pp, p≈0.34 不显著，降级为 \"comparable / on par with\"\n- **关键数值汇总**:\n\n| Scale | SFT mean (seeds) | RSFT mean (seeds) | Δ ign_f1 | SFT std | RSFT std |\n|-------|-------------------|--------------------|----------|---------|----------|\n| 1.7B | 0.4464 (3) | 0.5122 (1, s42 base) | +6.58pp | 2.79pp | — |\n| 4B | 0.4358 (3) | 0.4482 (3, Method A) / 0.5152 (1, Method B) | +1.24pp / +4.18pp (vs s44) | 3.80pp | 0.51pp |\n| 8B | 0.5019 (3) | 0.5414 (2, Method A) | +3.95pp | 3.72pp | 0.53pp |\n| 14B | 0.5507 (1) | pending | — | — | — |\n\n- **14B evidence tax**: 0.03pp（本质为零），14B 容量足够同时输出 evidence 和 RE\n- **RSFT variance 稳定化**: 8B SFT std=3.72pp → RSFT std=0.53pp (7x)；4B SFT std=3.80pp → RSFT std=0.51pp (7.5x)\n- **CED 价值**: CED RSFT (0.4482) > Random RSFT (0.4114) > SFT (0.3974)，+3.68pp gap\n- **GRPO**: bf16 ckpt-100 ign_f1=0.4431 无 catastrophic forgetting（D110），QLoRA 是 confound\n\n## 投稿目标\n- **EMNLP 2026 Main** (ARR July cycle, ~July 15-25, **~57 天**)\n\n## 实验路线（3 层优先级）\n\n### Tier 1 — Main 必要条件\n| 实验 | Plan ID | 状态 |\n|------|---------|------|\n| D102 k=1 方法论修正 | D102 | ✅ 完成 |\n| SFT 4B s43 + s44 + s42 reeval | plan_w3_sft_seeds | ✅ 完成 (D111) |\n| GRPO bf16 G=4 clean control | plan_015 | ✅ 完成 (D110/D113) |\n| Random k=1 RSFT baseline | plan_w18_random | ✅ 完成 (D109) |\n| 8B RSFT s44 seed expansion | plan_019 (8B) | ✅ 完成 (D115) |\n| 8B SFT s43 eval | plan_019 | ✅ 完成 (ign_f1=0.5324) |\n| D112 RSFT from SFT s44 (bf16) | plan_d112 | ✅ 完成 (D119: ign_f1=0.5152) |\n| 14B SFT (第 4 尺度) | plan_017 | ✅ 完成 (D117: 0.5507, tax=0.03pp) |\n| 1.7B RSFT s43/s44 重跑 | plan_019 (1.7B) | 🟡 进行中 |\n\n### Tier 2 — 大幅加分\n| 实验 | Plan ID | 状态 |\n|------|---------|------|\n| 14B RSFT + no-evidence + eval | plan_017 (后续) | pending（待启动） |\n| 8B RSFT s43 补齐第 3 seed | plan_019 | pending |\n| NLI model ablation | plan_010 | pending |\n| Evidence tax 机制分析 | plan_020 | pending |\n| Deep error analysis | plan_021 | pending |\n\n### Tier 3 — 锦上添花\n| 实验 | Plan ID | 状态 |\n|------|---------|------|\n| CDR/GDA 跨领域 | plan_018 | P2（无 evidence 标注） |\n| 第三模型家族 | plan_022 | pending |\n| DocKS-RAG/LMRC 复现 | plan_023 | pending |\n\n## 从 3.0 → 4.0 路径\n| 里程碑 | 预期评分 | 状态 |\n|--------|---------|------|\n| Wave 1 完成 + D112 | 3.0 → 3.5 | ✅ D112 完成 (0.5152, +4.18pp) |\n| + 1.7B/8B multi-seed 统计力 | 3.5 | 🟡 8B 3-seed done, 1.7B 进行中 |\n| + 14B 第 4 尺度档 | 3.5 → 3.75 | ✅ SFT 完成 (0.5507), RSFT pending |\n| + Mechanistic + error analysis | 3.75 → 4.0 | pending |\n\n## GPU 分布\n- cuda:0: 8B RSFT no-evidence eval r2（接近完成）\n- cuda:1: D112 no-evidence eval r3（44%）\n- cuda:2: 空闲\n- cuda:3: 1.7B no-evidence eval 2048（38%）\n\n## 近期任务\n- [x] Wave 1 全部完成（SFT seeds, GRPO bf16, Random RSFT）\n- [x] 8B RSFT s44 eval (D115: 0.5451, variance 压缩 5x)\n- [x] 4B SFT s42 D076 reeval (D111: 0.3974)\n- [x] D112 step 4 eval 完成 (bf16 LoRA: ign_f1=0.5152, +4.18pp)\n- [x] 8B SFT s43 eval 完成 (ign_f1=0.5324)\n- [x] 14B SFT eval 完成 (D117: ign_f1=0.5507, evidence tax=0.03pp)\n- [ ] 1.7B no-evidence eval 2048 重跑（排除截断，cuda:3）\n- [ ] 8B RSFT no-evidence eval（cuda:0，接近完成）\n- [ ] D112 no-evidence eval r3（cuda:1，44%）\n- [ ] 14B RSFT pipeline（待启动）\n- [ ] 8B RSFT s43 补齐第 3 seed\n- [ ] experiment_plan.yaml 全面同步 registry\n- [ ] paper_framing.md 更新（D112 + D117 + D118 narrative 调整）\n- [ ] 重新提交论文审稿\n\n## 关键风险\n- **D112 结果**: ✅ 已确认 RSFT-from-s44 (0.5152) > SFT s44 (0.4734) +4.18pp，Claim 1 robust\n- **1.7B claim 已降级 (D118)**: 1.7B RSFT vs 8B SFT Δ=+1.03pp, p≈0.34 不显著，改为 \"comparable\"；RSFT variance stabilization (SFT std=3.72pp vs RSFT std=0.53pp) 作为独立发现\n- **14B evidence tax = 0 (D117)**: 积极结果，14B 容量足够，Claim 3 需调整为 \"tax scales inversely with model capacity\"\n- **8B RSFT evidence quality trade-off**: EDCR 从 0.65-0.67 降到 0.62（RE↑/evidence precision↓），论文需讨论\n- **14B RSFT 待启动**: SFT 已完成，RSFT pipeline 是 Tier 2 首要任务\n- **EDCR 缺人工验证**: plan_013 取消，用 per-relation 分析 + Limitations 缓解\n\n## 关键决策日志\n\n| ID | 日期 | 摘要 | 关联实验 |\n|----|------|------|----------|\n| D120 | 2026-05-19 | D120: 8B RSFT 3-seed 确认 variance compression 7.4×， | d102_8b_rsft_k1_s43, plan019_8b_rsft_s44_eval |\n| D119 | 2026-05-19 | D119: D112 bf16 eval ign_f1=0.5152 确认 Method B (RS | d112_rsft_s44_eval_bf16, d112_rsft_s44_eval |\n| D118 | 2026-05-19 | D118: \"1.7B RSFT surpasses 8B SFT\" claim 降级为 \"appr | plan019_8b_sft_s43_eval, plan019_1_7b_rsft_s44_r2_eval |\n| D117 | 2026-05-19 | D117: 14B SFT evidence tax = 0.03pp（本质为零），完成 4 尺度  | plan017_14b_sft_eval_r2, plan017_14b_sft_no_evidence_eval_r2 |\n| D116 | 2026-05-19 | D116: D112 结果无效（QLoRA confound），必须用 bf16 LoRA 重跑 s | d112_rsft_s44_eval, d112_rsft_s44_train |\n| D115 | 2026-05-19 | D115: 8B RSFT s44 ign_f1=0.5451 确认 RSFT 跨 seed 稳健， | plan019_8b_rsft_s44_eval, eval_rsft_ced_s42 |\n| D114 | 2026-05-19 | D114: 1.7B RSFT s43/s44 应使用 Method A（s42 SFT base） | plan019_1_7b_rsft_s43, plan019_1_7b_rsft_s44, d112_rsft_s44_ced_score |\n| D113 | 2026-05-18 | D113: GRPO bf16 ckpt-100 为最优 checkpoint，ckpt-200 无 | grpo_bf16_g4_ckpt100_eval, grpo_bf16_g4_ckpt200_eval |\n| D112 | 2026-05-18 | D112: 4B RSFT ign_f1 claim 需重大 reframe——全部 RSFT 基于 | wave1_sft_4b_s43_eval_r2, wave1_sft_4b_s44_eval_r2, eval_rsft_ced_s42 |\n| D111 | 2026-05-18 | D111: 4B SFT s42 必须用 D076 协议重新 eval，统一三 seed 参考基准 | wave1_sft_4b_s43_eval_r2, wave1_sft_4b_s44_eval_r2 |\n\n",
    "structuredPatch": [
      {
        "oldStart": 18,
        "oldLines": 7,
        "newStart": 18,
        "newLines": 7,
        "lines": [
          " |-------|-------------------|--------------------|----------|---------|----------|",
          " | 1.7B | 0.4464 (3) | 0.5122 (1, s42 base) | +6.58pp | 2.79pp | — |",
          " | 4B | 0.4358 (3) | 0.4482 (3, Method A) / 0.5152 (1, Method B) | +1.24pp / +4.18pp (vs s44) | 3.80pp | 0.51pp |",
          "-| 8B | 0.5019 (3) | 0.5414 (2, Method A) | +3.95pp | 3.72pp | 0.53pp |",
          "+| 8B | 0.5019 (3) | 0.5433 (3, Method A) | +4.14pp | 3.72pp | 0.50pp |",
          " | 14B | 0.5507 (1) | pending | — | — | — |",
          " ",
          " - **14B evidence tax**: 0.03pp（本质为零），14B 容量足够同时输出 evidence 和 RE"
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

<details open><summary>🔧 Tool call — Edit · `toolu_01TgYQSuRxdiTKQLEgz6CWnr`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/ROADMAP.md",
  "old_string": "- **RSFT variance 稳定化**: 8B SFT std=3.72pp → RSFT std=0.53pp (7x)；4B SFT std=3.80pp → RSFT std=0.51pp (7.5x)",
  "new_string": "- **RSFT variance 稳定化**: 8B SFT std=3.72pp → RSFT std=0.50pp (7.4x)；4B SFT std=3.80pp → RSFT std=0.51pp (7.5x)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b6fdd47b-2526-4425-9a48-a46eb2f42ea9",
  "uuid": "ffd49a9a-4b92-42d8-a2a7-9d7e27333149",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013SC3vBcPNMvFNjEARLnMCr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 283,
      "cache_read_input_tokens": 29369,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 283
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

_source line 16 · 2026-05-19T17:30:23.119Z_

<details><summary>↩ Tool result · `toolu_01TgYQSuRxdiTKQLEgz6CWnr`</summary>

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
  "session_id": "b6fdd47b-2526-4425-9a48-a46eb2f42ea9",
  "uuid": "5b102eee-ca7e-4fdc-bdb4-83b99d57628d",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/ROADMAP.md",
    "oldString": "- **RSFT variance 稳定化**: 8B SFT std=3.72pp → RSFT std=0.53pp (7x)；4B SFT std=3.80pp → RSFT std=0.51pp (7.5x)",
    "newString": "- **RSFT variance 稳定化**: 8B SFT std=3.72pp → RSFT std=0.50pp (7.4x)；4B SFT std=3.80pp → RSFT std=0.51pp (7.5x)",
    "originalFile": "# faith-evidence-ie — Research Dashboard\n\n> 最后更新: 2026-05-19 UTC | 更新原因: 8B RSFT 3-seed 完成 (mean=0.5433±0.50pp, 7.4x variance compression)\n\n## 核心方向\nFREIGE: LLM-based evidence-grounded DocRE 系统性研究。3 贡献：RSFT+NLI 有效性 / Decoupling spectrum / Scale-dependent evidence tax。详见 paper_framing.md。\n\n## 当前进展\n- **阶段**: 🚀 Research + 审稿并行（Round 1 = 3.0 Findings，目标 4.0 Main）\n- **Wave 1**: ✅ 全部完成（SFT seeds, GRPO bf16, Random RSFT）\n- **Scaling seeds (plan_019)**: 8B 3-seed SFT 完成（mean=0.5019±3.72pp）；8B 3-seed RSFT 完成（s42=0.5376, s43=0.5471, s44=0.5451; mean=0.5433±0.50pp）\n- **D112 full pipeline**: ✅ 完成（bf16 LoRA RSFT from SFT s44: ign_f1=0.5152, +4.18pp over SFT s44 baseline 0.4734）\n- **14B SFT (plan_017)**: ✅ 完成（D117: with-evidence 0.5507, no-evidence 0.551, evidence tax=0.03pp≈0）\n- **D118 claim 降级**: 1.7B RSFT (0.5122) vs 8B SFT mean (0.5019) Δ=+1.03pp, p≈0.34 不显著，降级为 \"comparable / on par with\"\n- **关键数值汇总**:\n\n| Scale | SFT mean (seeds) | RSFT mean (seeds) | Δ ign_f1 | SFT std | RSFT std |\n|-------|-------------------|--------------------|----------|---------|----------|\n| 1.7B | 0.4464 (3) | 0.5122 (1, s42 base) | +6.58pp | 2.79pp | — |\n| 4B | 0.4358 (3) | 0.4482 (3, Method A) / 0.5152 (1, Method B) | +1.24pp / +4.18pp (vs s44) | 3.80pp | 0.51pp |\n| 8B | 0.5019 (3) | 0.5433 (3, Method A) | +4.14pp | 3.72pp | 0.50pp |\n| 14B | 0.5507 (1) | pending | — | — | — |\n\n- **14B evidence tax**: 0.03pp（本质为零），14B 容量足够同时输出 evidence 和 RE\n- **RSFT variance 稳定化**: 8B SFT std=3.72pp → RSFT std=0.53pp (7x)；4B SFT std=3.80pp → RSFT std=0.51pp (7.5x)\n- **CED 价值**: CED RSFT (0.4482) > Random RSFT (0.4114) > SFT (0.3974)，+3.68pp gap\n- **GRPO**: bf16 ckpt-100 ign_f1=0.4431 无 catastrophic forgetting（D110），QLoRA 是 confound\n\n## 投稿目标\n- **EMNLP 2026 Main** (ARR July cycle, ~July 15-25, **~57 天**)\n\n## 实验路线（3 层优先级）\n\n### Tier 1 — Main 必要条件\n| 实验 | Plan ID | 状态 |\n|------|---------|------|\n| D102 k=1 方法论修正 | D102 | ✅ 完成 |\n| SFT 4B s43 + s44 + s42 reeval | plan_w3_sft_seeds | ✅ 完成 (D111) |\n| GRPO bf16 G=4 clean control | plan_015 | ✅ 完成 (D110/D113) |\n| Random k=1 RSFT baseline | plan_w18_random | ✅ 完成 (D109) |\n| 8B RSFT s44 seed expansion | plan_019 (8B) | ✅ 完成 (D115) |\n| 8B SFT s43 eval | plan_019 | ✅ 完成 (ign_f1=0.5324) |\n| D112 RSFT from SFT s44 (bf16) | plan_d112 | ✅ 完成 (D119: ign_f1=0.5152) |\n| 14B SFT (第 4 尺度) | plan_017 | ✅ 完成 (D117: 0.5507, tax=0.03pp) |\n| 1.7B RSFT s43/s44 重跑 | plan_019 (1.7B) | 🟡 进行中 |\n\n### Tier 2 — 大幅加分\n| 实验 | Plan ID | 状态 |\n|------|---------|------|\n| 14B RSFT + no-evidence + eval | plan_017 (后续) | pending（待启动） |\n| 8B RSFT s43 补齐第 3 seed | plan_019 | pending |\n| NLI model ablation | plan_010 | pending |\n| Evidence tax 机制分析 | plan_020 | pending |\n| Deep error analysis | plan_021 | pending |\n\n### Tier 3 — 锦上添花\n| 实验 | Plan ID | 状态 |\n|------|---------|------|\n| CDR/GDA 跨领域 | plan_018 | P2（无 evidence 标注） |\n| 第三模型家族 | plan_022 | pending |\n| DocKS-RAG/LMRC 复现 | plan_023 | pending |\n\n## 从 3.0 → 4.0 路径\n| 里程碑 | 预期评分 | 状态 |\n|--------|---------|------|\n| Wave 1 完成 + D112 | 3.0 → 3.5 | ✅ D112 完成 (0.5152, +4.18pp) |\n| + 1.7B/8B multi-seed 统计力 | 3.5 | 🟡 8B 3-seed done, 1.7B 进行中 |\n| + 14B 第 4 尺度档 | 3.5 → 3.75 | ✅ SFT 完成 (0.5507), RSFT pending |\n| + Mechanistic + error analysis | 3.75 → 4.0 | pending |\n\n## GPU 分布\n- cuda:0: 8B RSFT no-evidence eval r2（接近完成）\n- cuda:1: D112 no-evidence eval r3（44%）\n- cuda:2: 空闲\n- cuda:3: 1.7B no-evidence eval 2048（38%）\n\n## 近期任务\n- [x] Wave 1 全部完成（SFT seeds, GRPO bf16, Random RSFT）\n- [x] 8B RSFT s44 eval (D115: 0.5451, variance 压缩 5x)\n- [x] 4B SFT s42 D076 reeval (D111: 0.3974)\n- [x] D112 step 4 eval 完成 (bf16 LoRA: ign_f1=0.5152, +4.18pp)\n- [x] 8B SFT s43 eval 完成 (ign_f1=0.5324)\n- [x] 14B SFT eval 完成 (D117: ign_f1=0.5507, evidence tax=0.03pp)\n- [ ] 1.7B no-evidence eval 2048 重跑（排除截断，cuda:3）\n- [ ] 8B RSFT no-evidence eval（cuda:0，接近完成）\n- [ ] D112 no-evidence eval r3（cuda:1，44%）\n- [ ] 14B RSFT pipeline（待启动）\n- [ ] 8B RSFT s43 补齐第 3 seed\n- [ ] experiment_plan.yaml 全面同步 registry\n- [ ] paper_framing.md 更新（D112 + D117 + D118 narrative 调整）\n- [ ] 重新提交论文审稿\n\n## 关键风险\n- **D112 结果**: ✅ 已确认 RSFT-from-s44 (0.5152) > SFT s44 (0.4734) +4.18pp，Claim 1 robust\n- **1.7B claim 已降级 (D118)**: 1.7B RSFT vs 8B SFT Δ=+1.03pp, p≈0.34 不显著，改为 \"comparable\"；RSFT variance stabilization (SFT std=3.72pp vs RSFT std=0.53pp) 作为独立发现\n- **14B evidence tax = 0 (D117)**: 积极结果，14B 容量足够，Claim 3 需调整为 \"tax scales inversely with model capacity\"\n- **8B RSFT evidence quality trade-off**: EDCR 从 0.65-0.67 降到 0.62（RE↑/evidence precision↓），论文需讨论\n- **14B RSFT 待启动**: SFT 已完成，RSFT pipeline 是 Tier 2 首要任务\n- **EDCR 缺人工验证**: plan_013 取消，用 per-relation 分析 + Limitations 缓解\n\n## 关键决策日志\n\n| ID | 日期 | 摘要 | 关联实验 |\n|----|------|------|----------|\n| D120 | 2026-05-19 | D120: 8B RSFT 3-seed 确认 variance compression 7.4×， | d102_8b_rsft_k1_s43, plan019_8b_rsft_s44_eval |\n| D119 | 2026-05-19 | D119: D112 bf16 eval ign_f1=0.5152 确认 Method B (RS | d112_rsft_s44_eval_bf16, d112_rsft_s44_eval |\n| D118 | 2026-05-19 | D118: \"1.7B RSFT surpasses 8B SFT\" claim 降级为 \"appr | plan019_8b_sft_s43_eval, plan019_1_7b_rsft_s44_r2_eval |\n| D117 | 2026-05-19 | D117: 14B SFT evidence tax = 0.03pp（本质为零），完成 4 尺度  | plan017_14b_sft_eval_r2, plan017_14b_sft_no_evidence_eval_r2 |\n| D116 | 2026-05-19 | D116: D112 结果无效（QLoRA confound），必须用 bf16 LoRA 重跑 s | d112_rsft_s44_eval, d112_rsft_s44_train |\n| D115 | 2026-05-19 | D115: 8B RSFT s44 ign_f1=0.5451 确认 RSFT 跨 seed 稳健， | plan019_8b_rsft_s44_eval, eval_rsft_ced_s42 |\n| D114 | 2026-05-19 | D114: 1.7B RSFT s43/s44 应使用 Method A（s42 SFT base） | plan019_1_7b_rsft_s43, plan019_1_7b_rsft_s44, d112_rsft_s44_ced_score |\n| D113 | 2026-05-18 | D113: GRPO bf16 ckpt-100 为最优 checkpoint，ckpt-200 无 | grpo_bf16_g4_ckpt100_eval, grpo_bf16_g4_ckpt200_eval |\n| D112 | 2026-05-18 | D112: 4B RSFT ign_f1 claim 需重大 reframe——全部 RSFT 基于 | wave1_sft_4b_s43_eval_r2, wave1_sft_4b_s44_eval_r2, eval_rsft_ced_s42 |\n| D111 | 2026-05-18 | D111: 4B SFT s42 必须用 D076 协议重新 eval，统一三 seed 参考基准 | wave1_sft_4b_s43_eval_r2, wave1_sft_4b_s44_eval_r2 |\n\n",
    "structuredPatch": [
      {
        "oldStart": 22,
        "oldLines": 7,
        "newStart": 22,
        "newLines": 7,
        "lines": [
          " | 14B | 0.5507 (1) | pending | — | — | — |",
          " ",
          " - **14B evidence tax**: 0.03pp（本质为零），14B 容量足够同时输出 evidence 和 RE",
          "-- **RSFT variance 稳定化**: 8B SFT std=3.72pp → RSFT std=0.53pp (7x)；4B SFT std=3.80pp → RSFT std=0.51pp (7.5x)",
          "+- **RSFT variance 稳定化**: 8B SFT std=3.72pp → RSFT std=0.50pp (7.4x)；4B SFT std=3.80pp → RSFT std=0.51pp (7.5x)",
          " - **CED 价值**: CED RSFT (0.4482) > Random RSFT (0.4114) > SFT (0.3974)，+3.68pp gap",
          " - **GRPO**: bf16 ckpt-100 ign_f1=0.4431 无 catastrophic forgetting（D110），QLoRA 是 confound",
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

_source line 17_

<details open><summary>🔧 Tool call — Edit · `toolu_01Gjr28VBFcsg7M3sjy415iQ`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/ROADMAP.md",
  "old_string": "| 8B RSFT s43 补齐第 3 seed | plan_019 | pending |",
  "new_string": "| 8B RSFT s43 补齐第 3 seed | plan_019 | ✅ 完成 (d102_8b_rsft_k1_s43, ign_f1=0.5471) |"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b6fdd47b-2526-4425-9a48-a46eb2f42ea9",
  "uuid": "83829056-0a2d-41b9-9463-2bd745d5c59b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018ppZiPujoa7Hcjvh3X4nLJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 323,
      "cache_read_input_tokens": 29652,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 323
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

_source line 18 · 2026-05-19T17:30:30.412Z_

<details><summary>↩ Tool result · `toolu_01Gjr28VBFcsg7M3sjy415iQ`</summary>

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
  "session_id": "b6fdd47b-2526-4425-9a48-a46eb2f42ea9",
  "uuid": "c0a84be4-87d5-4165-bced-18bb809aeada",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/ROADMAP.md",
    "oldString": "| 8B RSFT s43 补齐第 3 seed | plan_019 | pending |",
    "newString": "| 8B RSFT s43 补齐第 3 seed | plan_019 | ✅ 完成 (d102_8b_rsft_k1_s43, ign_f1=0.5471) |",
    "originalFile": "# faith-evidence-ie — Research Dashboard\n\n> 最后更新: 2026-05-19 UTC | 更新原因: 8B RSFT 3-seed 完成 (mean=0.5433±0.50pp, 7.4x variance compression)\n\n## 核心方向\nFREIGE: LLM-based evidence-grounded DocRE 系统性研究。3 贡献：RSFT+NLI 有效性 / Decoupling spectrum / Scale-dependent evidence tax。详见 paper_framing.md。\n\n## 当前进展\n- **阶段**: 🚀 Research + 审稿并行（Round 1 = 3.0 Findings，目标 4.0 Main）\n- **Wave 1**: ✅ 全部完成（SFT seeds, GRPO bf16, Random RSFT）\n- **Scaling seeds (plan_019)**: 8B 3-seed SFT 完成（mean=0.5019±3.72pp）；8B 3-seed RSFT 完成（s42=0.5376, s43=0.5471, s44=0.5451; mean=0.5433±0.50pp）\n- **D112 full pipeline**: ✅ 完成（bf16 LoRA RSFT from SFT s44: ign_f1=0.5152, +4.18pp over SFT s44 baseline 0.4734）\n- **14B SFT (plan_017)**: ✅ 完成（D117: with-evidence 0.5507, no-evidence 0.551, evidence tax=0.03pp≈0）\n- **D118 claim 降级**: 1.7B RSFT (0.5122) vs 8B SFT mean (0.5019) Δ=+1.03pp, p≈0.34 不显著，降级为 \"comparable / on par with\"\n- **关键数值汇总**:\n\n| Scale | SFT mean (seeds) | RSFT mean (seeds) | Δ ign_f1 | SFT std | RSFT std |\n|-------|-------------------|--------------------|----------|---------|----------|\n| 1.7B | 0.4464 (3) | 0.5122 (1, s42 base) | +6.58pp | 2.79pp | — |\n| 4B | 0.4358 (3) | 0.4482 (3, Method A) / 0.5152 (1, Method B) | +1.24pp / +4.18pp (vs s44) | 3.80pp | 0.51pp |\n| 8B | 0.5019 (3) | 0.5433 (3, Method A) | +4.14pp | 3.72pp | 0.50pp |\n| 14B | 0.5507 (1) | pending | — | — | — |\n\n- **14B evidence tax**: 0.03pp（本质为零），14B 容量足够同时输出 evidence 和 RE\n- **RSFT variance 稳定化**: 8B SFT std=3.72pp → RSFT std=0.50pp (7.4x)；4B SFT std=3.80pp → RSFT std=0.51pp (7.5x)\n- **CED 价值**: CED RSFT (0.4482) > Random RSFT (0.4114) > SFT (0.3974)，+3.68pp gap\n- **GRPO**: bf16 ckpt-100 ign_f1=0.4431 无 catastrophic forgetting（D110），QLoRA 是 confound\n\n## 投稿目标\n- **EMNLP 2026 Main** (ARR July cycle, ~July 15-25, **~57 天**)\n\n## 实验路线（3 层优先级）\n\n### Tier 1 — Main 必要条件\n| 实验 | Plan ID | 状态 |\n|------|---------|------|\n| D102 k=1 方法论修正 | D102 | ✅ 完成 |\n| SFT 4B s43 + s44 + s42 reeval | plan_w3_sft_seeds | ✅ 完成 (D111) |\n| GRPO bf16 G=4 clean control | plan_015 | ✅ 完成 (D110/D113) |\n| Random k=1 RSFT baseline | plan_w18_random | ✅ 完成 (D109) |\n| 8B RSFT s44 seed expansion | plan_019 (8B) | ✅ 完成 (D115) |\n| 8B SFT s43 eval | plan_019 | ✅ 完成 (ign_f1=0.5324) |\n| D112 RSFT from SFT s44 (bf16) | plan_d112 | ✅ 完成 (D119: ign_f1=0.5152) |\n| 14B SFT (第 4 尺度) | plan_017 | ✅ 完成 (D117: 0.5507, tax=0.03pp) |\n| 1.7B RSFT s43/s44 重跑 | plan_019 (1.7B) | 🟡 进行中 |\n\n### Tier 2 — 大幅加分\n| 实验 | Plan ID | 状态 |\n|------|---------|------|\n| 14B RSFT + no-evidence + eval | plan_017 (后续) | pending（待启动） |\n| 8B RSFT s43 补齐第 3 seed | plan_019 | pending |\n| NLI model ablation | plan_010 | pending |\n| Evidence tax 机制分析 | plan_020 | pending |\n| Deep error analysis | plan_021 | pending |\n\n### Tier 3 — 锦上添花\n| 实验 | Plan ID | 状态 |\n|------|---------|------|\n| CDR/GDA 跨领域 | plan_018 | P2（无 evidence 标注） |\n| 第三模型家族 | plan_022 | pending |\n| DocKS-RAG/LMRC 复现 | plan_023 | pending |\n\n## 从 3.0 → 4.0 路径\n| 里程碑 | 预期评分 | 状态 |\n|--------|---------|------|\n| Wave 1 完成 + D112 | 3.0 → 3.5 | ✅ D112 完成 (0.5152, +4.18pp) |\n| + 1.7B/8B multi-seed 统计力 | 3.5 | 🟡 8B 3-seed done, 1.7B 进行中 |\n| + 14B 第 4 尺度档 | 3.5 → 3.75 | ✅ SFT 完成 (0.5507), RSFT pending |\n| + Mechanistic + error analysis | 3.75 → 4.0 | pending |\n\n## GPU 分布\n- cuda:0: 8B RSFT no-evidence eval r2（接近完成）\n- cuda:1: D112 no-evidence eval r3（44%）\n- cuda:2: 空闲\n- cuda:3: 1.7B no-evidence eval 2048（38%）\n\n## 近期任务\n- [x] Wave 1 全部完成（SFT seeds, GRPO bf16, Random RSFT）\n- [x] 8B RSFT s44 eval (D115: 0.5451, variance 压缩 5x)\n- [x] 4B SFT s42 D076 reeval (D111: 0.3974)\n- [x] D112 step 4 eval 完成 (bf16 LoRA: ign_f1=0.5152, +4.18pp)\n- [x] 8B SFT s43 eval 完成 (ign_f1=0.5324)\n- [x] 14B SFT eval 完成 (D117: ign_f1=0.5507, evidence tax=0.03pp)\n- [ ] 1.7B no-evidence eval 2048 重跑（排除截断，cuda:3）\n- [ ] 8B RSFT no-evidence eval（cuda:0，接近完成）\n- [ ] D112 no-evidence eval r3（cuda:1，44%）\n- [ ] 14B RSFT pipeline（待启动）\n- [ ] 8B RSFT s43 补齐第 3 seed\n- [ ] experiment_plan.yaml 全面同步 registry\n- [ ] paper_framing.md 更新（D112 + D117 + D118 narrative 调整）\n- [ ] 重新提交论文审稿\n\n## 关键风险\n- **D112 结果**: ✅ 已确认 RSFT-from-s44 (0.5152) > SFT s44 (0.4734) +4.18pp，Claim 1 robust\n- **1.7B claim 已降级 (D118)**: 1.7B RSFT vs 8B SFT Δ=+1.03pp, p≈0.34 不显著，改为 \"comparable\"；RSFT variance stabilization (SFT std=3.72pp vs RSFT std=0.53pp) 作为独立发现\n- **14B evidence tax = 0 (D117)**: 积极结果，14B 容量足够，Claim 3 需调整为 \"tax scales inversely with model capacity\"\n- **8B RSFT evidence quality trade-off**: EDCR 从 0.65-0.67 降到 0.62（RE↑/evidence precision↓），论文需讨论\n- **14B RSFT 待启动**: SFT 已完成，RSFT pipeline 是 Tier 2 首要任务\n- **EDCR 缺人工验证**: plan_013 取消，用 per-relation 分析 + Limitations 缓解\n\n## 关键决策日志\n\n| ID | 日期 | 摘要 | 关联实验 |\n|----|------|------|----------|\n| D120 | 2026-05-19 | D120: 8B RSFT 3-seed 确认 variance compression 7.4×， | d102_8b_rsft_k1_s43, plan019_8b_rsft_s44_eval |\n| D119 | 2026-05-19 | D119: D112 bf16 eval ign_f1=0.5152 确认 Method B (RS | d112_rsft_s44_eval_bf16, d112_rsft_s44_eval |\n| D118 | 2026-05-19 | D118: \"1.7B RSFT surpasses 8B SFT\" claim 降级为 \"appr | plan019_8b_sft_s43_eval, plan019_1_7b_rsft_s44_r2_eval |\n| D117 | 2026-05-19 | D117: 14B SFT evidence tax = 0.03pp（本质为零），完成 4 尺度  | plan017_14b_sft_eval_r2, plan017_14b_sft_no_evidence_eval_r2 |\n| D116 | 2026-05-19 | D116: D112 结果无效（QLoRA confound），必须用 bf16 LoRA 重跑 s | d112_rsft_s44_eval, d112_rsft_s44_train |\n| D115 | 2026-05-19 | D115: 8B RSFT s44 ign_f1=0.5451 确认 RSFT 跨 seed 稳健， | plan019_8b_rsft_s44_eval, eval_rsft_ced_s42 |\n| D114 | 2026-05-19 | D114: 1.7B RSFT s43/s44 应使用 Method A（s42 SFT base） | plan019_1_7b_rsft_s43, plan019_1_7b_rsft_s44, d112_rsft_s44_ced_score |\n| D113 | 2026-05-18 | D113: GRPO bf16 ckpt-100 为最优 checkpoint，ckpt-200 无 | grpo_bf16_g4_ckpt100_eval, grpo_bf16_g4_ckpt200_eval |\n| D112 | 2026-05-18 | D112: 4B RSFT ign_f1 claim 需重大 reframe——全部 RSFT 基于 | wave1_sft_4b_s43_eval_r2, wave1_sft_4b_s44_eval_r2, eval_rsft_ced_s42 |\n| D111 | 2026-05-18 | D111: 4B SFT s42 必须用 D076 协议重新 eval，统一三 seed 参考基准 | wave1_sft_4b_s43_eval_r2, wave1_sft_4b_s44_eval_r2 |\n\n",
    "structuredPatch": [
      {
        "oldStart": 48,
        "oldLines": 7,
        "newStart": 48,
        "newLines": 7,
        "lines": [
          " | 实验 | Plan ID | 状态 |",
          " |------|---------|------|",
          " | 14B RSFT + no-evidence + eval | plan_017 (后续) | pending（待启动） |",
          "-| 8B RSFT s43 补齐第 3 seed | plan_019 | pending |",
          "+| 8B RSFT s43 补齐第 3 seed | plan_019 | ✅ 完成 (d102_8b_rsft_k1_s43, ign_f1=0.5471) |",
          " | NLI model ablation | plan_010 | pending |",
          " | Evidence tax 机制分析 | plan_020 | pending |",
          " | Deep error analysis | plan_021 | pending |"
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

<details open><summary>🔧 Tool call — Edit · `toolu_01PAa5BuqWbAv5TCzNChxmAU`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/ROADMAP.md",
  "old_string": "- cuda:0: 8B RSFT no-evidence eval r2（接近完成）\n- cuda:1: D112 no-evidence eval r3（44%）\n- cuda:2: 空闲\n- cuda:3: 1.7B no-evidence eval 2048（38%）",
  "new_string": "- cuda:0: 空闲（等待 Director 分配）\n- cuda:1: d112_rsft_no_evidence_eval_r3 (60%, ~50min remaining)\n- cuda:2: 空闲（等待 Director 分配）\n- cuda:3: plan019_1_7b_rsft_no_evidence_eval_2048 (47%, ~2h30m remaining)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b6fdd47b-2526-4425-9a48-a46eb2f42ea9",
  "uuid": "bf073d3b-a979-4ea8-a216-0bf8c621e856",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SxHJcLNr4wtnpjLL2CR8sx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 277,
      "cache_read_input_tokens": 29975,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 277
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

_source line 20 · 2026-05-19T17:30:37.724Z_

<details><summary>↩ Tool result · `toolu_01PAa5BuqWbAv5TCzNChxmAU`</summary>

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
  "session_id": "b6fdd47b-2526-4425-9a48-a46eb2f42ea9",
  "uuid": "d77e3fd4-3e40-41aa-b582-06a2ca768d53",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/ROADMAP.md",
    "oldString": "- cuda:0: 8B RSFT no-evidence eval r2（接近完成）\n- cuda:1: D112 no-evidence eval r3（44%）\n- cuda:2: 空闲\n- cuda:3: 1.7B no-evidence eval 2048（38%）",
    "newString": "- cuda:0: 空闲（等待 Director 分配）\n- cuda:1: d112_rsft_no_evidence_eval_r3 (60%, ~50min remaining)\n- cuda:2: 空闲（等待 Director 分配）\n- cuda:3: plan019_1_7b_rsft_no_evidence_eval_2048 (47%, ~2h30m remaining)",
    "originalFile": "# faith-evidence-ie — Research Dashboard\n\n> 最后更新: 2026-05-19 UTC | 更新原因: 8B RSFT 3-seed 完成 (mean=0.5433±0.50pp, 7.4x variance compression)\n\n## 核心方向\nFREIGE: LLM-based evidence-grounded DocRE 系统性研究。3 贡献：RSFT+NLI 有效性 / Decoupling spectrum / Scale-dependent evidence tax。详见 paper_framing.md。\n\n## 当前进展\n- **阶段**: 🚀 Research + 审稿并行（Round 1 = 3.0 Findings，目标 4.0 Main）\n- **Wave 1**: ✅ 全部完成（SFT seeds, GRPO bf16, Random RSFT）\n- **Scaling seeds (plan_019)**: 8B 3-seed SFT 完成（mean=0.5019±3.72pp）；8B 3-seed RSFT 完成（s42=0.5376, s43=0.5471, s44=0.5451; mean=0.5433±0.50pp）\n- **D112 full pipeline**: ✅ 完成（bf16 LoRA RSFT from SFT s44: ign_f1=0.5152, +4.18pp over SFT s44 baseline 0.4734）\n- **14B SFT (plan_017)**: ✅ 完成（D117: with-evidence 0.5507, no-evidence 0.551, evidence tax=0.03pp≈0）\n- **D118 claim 降级**: 1.7B RSFT (0.5122) vs 8B SFT mean (0.5019) Δ=+1.03pp, p≈0.34 不显著，降级为 \"comparable / on par with\"\n- **关键数值汇总**:\n\n| Scale | SFT mean (seeds) | RSFT mean (seeds) | Δ ign_f1 | SFT std | RSFT std |\n|-------|-------------------|--------------------|----------|---------|----------|\n| 1.7B | 0.4464 (3) | 0.5122 (1, s42 base) | +6.58pp | 2.79pp | — |\n| 4B | 0.4358 (3) | 0.4482 (3, Method A) / 0.5152 (1, Method B) | +1.24pp / +4.18pp (vs s44) | 3.80pp | 0.51pp |\n| 8B | 0.5019 (3) | 0.5433 (3, Method A) | +4.14pp | 3.72pp | 0.50pp |\n| 14B | 0.5507 (1) | pending | — | — | — |\n\n- **14B evidence tax**: 0.03pp（本质为零），14B 容量足够同时输出 evidence 和 RE\n- **RSFT variance 稳定化**: 8B SFT std=3.72pp → RSFT std=0.50pp (7.4x)；4B SFT std=3.80pp → RSFT std=0.51pp (7.5x)\n- **CED 价值**: CED RSFT (0.4482) > Random RSFT (0.4114) > SFT (0.3974)，+3.68pp gap\n- **GRPO**: bf16 ckpt-100 ign_f1=0.4431 无 catastrophic forgetting（D110），QLoRA 是 confound\n\n## 投稿目标\n- **EMNLP 2026 Main** (ARR July cycle, ~July 15-25, **~57 天**)\n\n## 实验路线（3 层优先级）\n\n### Tier 1 — Main 必要条件\n| 实验 | Plan ID | 状态 |\n|------|---------|------|\n| D102 k=1 方法论修正 | D102 | ✅ 完成 |\n| SFT 4B s43 + s44 + s42 reeval | plan_w3_sft_seeds | ✅ 完成 (D111) |\n| GRPO bf16 G=4 clean control | plan_015 | ✅ 完成 (D110/D113) |\n| Random k=1 RSFT baseline | plan_w18_random | ✅ 完成 (D109) |\n| 8B RSFT s44 seed expansion | plan_019 (8B) | ✅ 完成 (D115) |\n| 8B SFT s43 eval | plan_019 | ✅ 完成 (ign_f1=0.5324) |\n| D112 RSFT from SFT s44 (bf16) | plan_d112 | ✅ 完成 (D119: ign_f1=0.5152) |\n| 14B SFT (第 4 尺度) | plan_017 | ✅ 完成 (D117: 0.5507, tax=0.03pp) |\n| 1.7B RSFT s43/s44 重跑 | plan_019 (1.7B) | 🟡 进行中 |\n\n### Tier 2 — 大幅加分\n| 实验 | Plan ID | 状态 |\n|------|---------|------|\n| 14B RSFT + no-evidence + eval | plan_017 (后续) | pending（待启动） |\n| 8B RSFT s43 补齐第 3 seed | plan_019 | ✅ 完成 (d102_8b_rsft_k1_s43, ign_f1=0.5471) |\n| NLI model ablation | plan_010 | pending |\n| Evidence tax 机制分析 | plan_020 | pending |\n| Deep error analysis | plan_021 | pending |\n\n### Tier 3 — 锦上添花\n| 实验 | Plan ID | 状态 |\n|------|---------|------|\n| CDR/GDA 跨领域 | plan_018 | P2（无 evidence 标注） |\n| 第三模型家族 | plan_022 | pending |\n| DocKS-RAG/LMRC 复现 | plan_023 | pending |\n\n## 从 3.0 → 4.0 路径\n| 里程碑 | 预期评分 | 状态 |\n|--------|---------|------|\n| Wave 1 完成 + D112 | 3.0 → 3.5 | ✅ D112 完成 (0.5152, +4.18pp) |\n| + 1.7B/8B multi-seed 统计力 | 3.5 | 🟡 8B 3-seed done, 1.7B 进行中 |\n| + 14B 第 4 尺度档 | 3.5 → 3.75 | ✅ SFT 完成 (0.5507), RSFT pending |\n| + Mechanistic + error analysis | 3.75 → 4.0 | pending |\n\n## GPU 分布\n- cuda:0: 8B RSFT no-evidence eval r2（接近完成）\n- cuda:1: D112 no-evidence eval r3（44%）\n- cuda:2: 空闲\n- cuda:3: 1.7B no-evidence eval 2048（38%）\n\n## 近期任务\n- [x] Wave 1 全部完成（SFT seeds, GRPO bf16, Random RSFT）\n- [x] 8B RSFT s44 eval (D115: 0.5451, variance 压缩 5x)\n- [x] 4B SFT s42 D076 reeval (D111: 0.3974)\n- [x] D112 step 4 eval 完成 (bf16 LoRA: ign_f1=0.5152, +4.18pp)\n- [x] 8B SFT s43 eval 完成 (ign_f1=0.5324)\n- [x] 14B SFT eval 完成 (D117: ign_f1=0.5507, evidence tax=0.03pp)\n- [ ] 1.7B no-evidence eval 2048 重跑（排除截断，cuda:3）\n- [ ] 8B RSFT no-evidence eval（cuda:0，接近完成）\n- [ ] D112 no-evidence eval r3（cuda:1，44%）\n- [ ] 14B RSFT pipeline（待启动）\n- [ ] 8B RSFT s43 补齐第 3 seed\n- [ ] experiment_plan.yaml 全面同步 registry\n- [ ] paper_framing.md 更新（D112 + D117 + D118 narrative 调整）\n- [ ] 重新提交论文审稿\n\n## 关键风险\n- **D112 结果**: ✅ 已确认 RSFT-from-s44 (0.5152) > SFT s44 (0.4734) +4.18pp，Claim 1 robust\n- **1.7B claim 已降级 (D118)**: 1.7B RSFT vs 8B SFT Δ=+1.03pp, p≈0.34 不显著，改为 \"comparable\"；RSFT variance stabilization (SFT std=3.72pp vs RSFT std=0.53pp) 作为独立发现\n- **14B evidence tax = 0 (D117)**: 积极结果，14B 容量足够，Claim 3 需调整为 \"tax scales inversely with model capacity\"\n- **8B RSFT evidence quality trade-off**: EDCR 从 0.65-0.67 降到 0.62（RE↑/evidence precision↓），论文需讨论\n- **14B RSFT 待启动**: SFT 已完成，RSFT pipeline 是 Tier 2 首要任务\n- **EDCR 缺人工验证**: plan_013 取消，用 per-relation 分析 + Limitations 缓解\n\n## 关键决策日志\n\n| ID | 日期 | 摘要 | 关联实验 |\n|----|------|------|----------|\n| D120 | 2026-05-19 | D120: 8B RSFT 3-seed 确认 variance compression 7.4×， | d102_8b_rsft_k1_s43, plan019_8b_rsft_s44_eval |\n| D119 | 2026-05-19 | D119: D112 bf16 eval ign_f1=0.5152 确认 Method B (RS | d112_rsft_s44_eval_bf16, d112_rsft_s44_eval |\n| D118 | 2026-05-19 | D118: \"1.7B RSFT surpasses 8B SFT\" claim 降级为 \"appr | plan019_8b_sft_s43_eval, plan019_1_7b_rsft_s44_r2_eval |\n| D117 | 2026-05-19 | D117: 14B SFT evidence tax = 0.03pp（本质为零），完成 4 尺度  | plan017_14b_sft_eval_r2, plan017_14b_sft_no_evidence_eval_r2 |\n| D116 | 2026-05-19 | D116: D112 结果无效（QLoRA confound），必须用 bf16 LoRA 重跑 s | d112_rsft_s44_eval, d112_rsft_s44_train |\n| D115 | 2026-05-19 | D115: 8B RSFT s44 ign_f1=0.5451 确认 RSFT 跨 seed 稳健， | plan019_8b_rsft_s44_eval, eval_rsft_ced_s42 |\n| D114 | 2026-05-19 | D114: 1.7B RSFT s43/s44 应使用 Method A（s42 SFT base） | plan019_1_7b_rsft_s43, plan019_1_7b_rsft_s44, d112_rsft_s44_ced_score |\n| D113 | 2026-05-18 | D113: GRPO bf16 ckpt-100 为最优 checkpoint，ckpt-200 无 | grpo_bf16_g4_ckpt100_eval, grpo_bf16_g4_ckpt200_eval |\n| D112 | 2026-05-18 | D112: 4B RSFT ign_f1 claim 需重大 reframe——全部 RSFT 基于 | wave1_sft_4b_s43_eval_r2, wave1_sft_4b_s44_eval_r2, eval_rsft_ced_s42 |\n| D111 | 2026-05-18 | D111: 4B SFT s42 必须用 D076 协议重新 eval，统一三 seed 参考基准 | wave1_sft_4b_s43_eval_r2, wave1_sft_4b_s44_eval_r2 |\n\n",
    "structuredPatch": [
      {
        "oldStart": 69,
        "oldLines": 10,
        "newStart": 69,
        "newLines": 10,
        "lines": [
          " | + Mechanistic + error analysis | 3.75 → 4.0 | pending |",
          " ",
          " ## GPU 分布",
          "-- cuda:0: 8B RSFT no-evidence eval r2（接近完成）",
          "-- cuda:1: D112 no-evidence eval r3（44%）",
          "-- cuda:2: 空闲",
          "-- cuda:3: 1.7B no-evidence eval 2048（38%）",
          "+- cuda:0: 空闲（等待 Director 分配）",
          "+- cuda:1: d112_rsft_no_evidence_eval_r3 (60%, ~50min remaining)",
          "+- cuda:2: 空闲（等待 Director 分配）",
          "+- cuda:3: plan019_1_7b_rsft_no_evidence_eval_2048 (47%, ~2h30m remaining)",
          " ",
          " ## 近期任务",
          " - [x] Wave 1 全部完成（SFT seeds, GRPO bf16, Random RSFT）"
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

<details open><summary>🔧 Tool call — Edit · `toolu_014xaDwTFAgHun6LJvV4PwLz`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/ROADMAP.md",
  "old_string": "- [ ] 8B RSFT s43 补齐第 3 seed",
  "new_string": "- [x] 8B RSFT s43 补齐第 3 seed（d102_8b_rsft_k1_s43, ign_f1=0.5471）"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b6fdd47b-2526-4425-9a48-a46eb2f42ea9",
  "uuid": "7fad213d-4440-49c8-bc3c-a848e595f4eb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bsz52hk95Ahauo6JU8pFpK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 366,
      "cache_read_input_tokens": 30252,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 366
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

_source line 22 · 2026-05-19T17:30:44.141Z_

<details><summary>↩ Tool result · `toolu_014xaDwTFAgHun6LJvV4PwLz`</summary>

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
  "session_id": "b6fdd47b-2526-4425-9a48-a46eb2f42ea9",
  "uuid": "28f02fea-5084-4cda-bb24-491cb26d181f",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/ROADMAP.md",
    "oldString": "- [ ] 8B RSFT s43 补齐第 3 seed",
    "newString": "- [x] 8B RSFT s43 补齐第 3 seed（d102_8b_rsft_k1_s43, ign_f1=0.5471）",
    "originalFile": "# faith-evidence-ie — Research Dashboard\n\n> 最后更新: 2026-05-19 UTC | 更新原因: 8B RSFT 3-seed 完成 (mean=0.5433±0.50pp, 7.4x variance compression)\n\n## 核心方向\nFREIGE: LLM-based evidence-grounded DocRE 系统性研究。3 贡献：RSFT+NLI 有效性 / Decoupling spectrum / Scale-dependent evidence tax。详见 paper_framing.md。\n\n## 当前进展\n- **阶段**: 🚀 Research + 审稿并行（Round 1 = 3.0 Findings，目标 4.0 Main）\n- **Wave 1**: ✅ 全部完成（SFT seeds, GRPO bf16, Random RSFT）\n- **Scaling seeds (plan_019)**: 8B 3-seed SFT 完成（mean=0.5019±3.72pp）；8B 3-seed RSFT 完成（s42=0.5376, s43=0.5471, s44=0.5451; mean=0.5433±0.50pp）\n- **D112 full pipeline**: ✅ 完成（bf16 LoRA RSFT from SFT s44: ign_f1=0.5152, +4.18pp over SFT s44 baseline 0.4734）\n- **14B SFT (plan_017)**: ✅ 完成（D117: with-evidence 0.5507, no-evidence 0.551, evidence tax=0.03pp≈0）\n- **D118 claim 降级**: 1.7B RSFT (0.5122) vs 8B SFT mean (0.5019) Δ=+1.03pp, p≈0.34 不显著，降级为 \"comparable / on par with\"\n- **关键数值汇总**:\n\n| Scale | SFT mean (seeds) | RSFT mean (seeds) | Δ ign_f1 | SFT std | RSFT std |\n|-------|-------------------|--------------------|----------|---------|----------|\n| 1.7B | 0.4464 (3) | 0.5122 (1, s42 base) | +6.58pp | 2.79pp | — |\n| 4B | 0.4358 (3) | 0.4482 (3, Method A) / 0.5152 (1, Method B) | +1.24pp / +4.18pp (vs s44) | 3.80pp | 0.51pp |\n| 8B | 0.5019 (3) | 0.5433 (3, Method A) | +4.14pp | 3.72pp | 0.50pp |\n| 14B | 0.5507 (1) | pending | — | — | — |\n\n- **14B evidence tax**: 0.03pp（本质为零），14B 容量足够同时输出 evidence 和 RE\n- **RSFT variance 稳定化**: 8B SFT std=3.72pp → RSFT std=0.50pp (7.4x)；4B SFT std=3.80pp → RSFT std=0.51pp (7.5x)\n- **CED 价值**: CED RSFT (0.4482) > Random RSFT (0.4114) > SFT (0.3974)，+3.68pp gap\n- **GRPO**: bf16 ckpt-100 ign_f1=0.4431 无 catastrophic forgetting（D110），QLoRA 是 confound\n\n## 投稿目标\n- **EMNLP 2026 Main** (ARR July cycle, ~July 15-25, **~57 天**)\n\n## 实验路线（3 层优先级）\n\n### Tier 1 — Main 必要条件\n| 实验 | Plan ID | 状态 |\n|------|---------|------|\n| D102 k=1 方法论修正 | D102 | ✅ 完成 |\n| SFT 4B s43 + s44 + s42 reeval | plan_w3_sft_seeds | ✅ 完成 (D111) |\n| GRPO bf16 G=4 clean control | plan_015 | ✅ 完成 (D110/D113) |\n| Random k=1 RSFT baseline | plan_w18_random | ✅ 完成 (D109) |\n| 8B RSFT s44 seed expansion | plan_019 (8B) | ✅ 完成 (D115) |\n| 8B SFT s43 eval | plan_019 | ✅ 完成 (ign_f1=0.5324) |\n| D112 RSFT from SFT s44 (bf16) | plan_d112 | ✅ 完成 (D119: ign_f1=0.5152) |\n| 14B SFT (第 4 尺度) | plan_017 | ✅ 完成 (D117: 0.5507, tax=0.03pp) |\n| 1.7B RSFT s43/s44 重跑 | plan_019 (1.7B) | 🟡 进行中 |\n\n### Tier 2 — 大幅加分\n| 实验 | Plan ID | 状态 |\n|------|---------|------|\n| 14B RSFT + no-evidence + eval | plan_017 (后续) | pending（待启动） |\n| 8B RSFT s43 补齐第 3 seed | plan_019 | ✅ 完成 (d102_8b_rsft_k1_s43, ign_f1=0.5471) |\n| NLI model ablation | plan_010 | pending |\n| Evidence tax 机制分析 | plan_020 | pending |\n| Deep error analysis | plan_021 | pending |\n\n### Tier 3 — 锦上添花\n| 实验 | Plan ID | 状态 |\n|------|---------|------|\n| CDR/GDA 跨领域 | plan_018 | P2（无 evidence 标注） |\n| 第三模型家族 | plan_022 | pending |\n| DocKS-RAG/LMRC 复现 | plan_023 | pending |\n\n## 从 3.0 → 4.0 路径\n| 里程碑 | 预期评分 | 状态 |\n|--------|---------|------|\n| Wave 1 完成 + D112 | 3.0 → 3.5 | ✅ D112 完成 (0.5152, +4.18pp) |\n| + 1.7B/8B multi-seed 统计力 | 3.5 | 🟡 8B 3-seed done, 1.7B 进行中 |\n| + 14B 第 4 尺度档 | 3.5 → 3.75 | ✅ SFT 完成 (0.5507), RSFT pending |\n| + Mechanistic + error analysis | 3.75 → 4.0 | pending |\n\n## GPU 分布\n- cuda:0: 空闲（等待 Director 分配）\n- cuda:1: d112_rsft_no_evidence_eval_r3 (60%, ~50min remaining)\n- cuda:2: 空闲（等待 Director 分配）\n- cuda:3: plan019_1_7b_rsft_no_evidence_eval_2048 (47%, ~2h30m remaining)\n\n## 近期任务\n- [x] Wave 1 全部完成（SFT seeds, GRPO bf16, Random RSFT）\n- [x] 8B RSFT s44 eval (D115: 0.5451, variance 压缩 5x)\n- [x] 4B SFT s42 D076 reeval (D111: 0.3974)\n- [x] D112 step 4 eval 完成 (bf16 LoRA: ign_f1=0.5152, +4.18pp)\n- [x] 8B SFT s43 eval 完成 (ign_f1=0.5324)\n- [x] 14B SFT eval 完成 (D117: ign_f1=0.5507, evidence tax=0.03pp)\n- [ ] 1.7B no-evidence eval 2048 重跑（排除截断，cuda:3）\n- [ ] 8B RSFT no-evidence eval（cuda:0，接近完成）\n- [ ] D112 no-evidence eval r3（cuda:1，44%）\n- [ ] 14B RSFT pipeline（待启动）\n- [ ] 8B RSFT s43 补齐第 3 seed\n- [ ] experiment_plan.yaml 全面同步 registry\n- [ ] paper_framing.md 更新（D112 + D117 + D118 narrative 调整）\n- [ ] 重新提交论文审稿\n\n## 关键风险\n- **D112 结果**: ✅ 已确认 RSFT-from-s44 (0.5152) > SFT s44 (0.4734) +4.18pp，Claim 1 robust\n- **1.7B claim 已降级 (D118)**: 1.7B RSFT vs 8B SFT Δ=+1.03pp, p≈0.34 不显著，改为 \"comparable\"；RSFT variance stabilization (SFT std=3.72pp vs RSFT std=0.53pp) 作为独立发现\n- **14B evidence tax = 0 (D117)**: 积极结果，14B 容量足够，Claim 3 需调整为 \"tax scales inversely with model capacity\"\n- **8B RSFT evidence quality trade-off**: EDCR 从 0.65-0.67 降到 0.62（RE↑/evidence precision↓），论文需讨论\n- **14B RSFT 待启动**: SFT 已完成，RSFT pipeline 是 Tier 2 首要任务\n- **EDCR 缺人工验证**: plan_013 取消，用 per-relation 分析 + Limitations 缓解\n\n## 关键决策日志\n\n| ID | 日期 | 摘要 | 关联实验 |\n|----|------|------|----------|\n| D120 | 2026-05-19 | D120: 8B RSFT 3-seed 确认 variance compression 7.4×， | d102_8b_rsft_k1_s43, plan019_8b_rsft_s44_eval |\n| D119 | 2026-05-19 | D119: D112 bf16 eval ign_f1=0.5152 确认 Method B (RS | d112_rsft_s44_eval_bf16, d112_rsft_s44_eval |\n| D118 | 2026-05-19 | D118: \"1.7B RSFT surpasses 8B SFT\" claim 降级为 \"appr | plan019_8b_sft_s43_eval, plan019_1_7b_rsft_s44_r2_eval |\n| D117 | 2026-05-19 | D117: 14B SFT evidence tax = 0.03pp（本质为零），完成 4 尺度  | plan017_14b_sft_eval_r2, plan017_14b_sft_no_evidence_eval_r2 |\n| D116 | 2026-05-19 | D116: D112 结果无效（QLoRA confound），必须用 bf16 LoRA 重跑 s | d112_rsft_s44_eval, d112_rsft_s44_train |\n| D115 | 2026-05-19 | D115: 8B RSFT s44 ign_f1=0.5451 确认 RSFT 跨 seed 稳健， | plan019_8b_rsft_s44_eval, eval_rsft_ced_s42 |\n| D114 | 2026-05-19 | D114: 1.7B RSFT s43/s44 应使用 Method A（s42 SFT base） | plan019_1_7b_rsft_s43, plan019_1_7b_rsft_s44, d112_rsft_s44_ced_score |\n| D113 | 2026-05-18 | D113: GRPO bf16 ckpt-100 为最优 checkpoint，ckpt-200 无 | grpo_bf16_g4_ckpt100_eval, grpo_bf16_g4_ckpt200_eval |\n| D112 | 2026-05-18 | D112: 4B RSFT ign_f1 claim 需重大 reframe——全部 RSFT 基于 | wave1_sft_4b_s43_eval_r2, wave1_sft_4b_s44_eval_r2, eval_rsft_ced_s42 |\n| D111 | 2026-05-18 | D111: 4B SFT s42 必须用 D076 协议重新 eval，统一三 seed 参考基准 | wave1_sft_4b_s43_eval_r2, wave1_sft_4b_s44_eval_r2 |\n\n",
    "structuredPatch": [
      {
        "oldStart": 85,
        "oldLines": 7,
        "newStart": 85,
        "newLines": 7,
        "lines": [
          " - [ ] 8B RSFT no-evidence eval（cuda:0，接近完成）",
          " - [ ] D112 no-evidence eval r3（cuda:1，44%）",
          " - [ ] 14B RSFT pipeline（待启动）",
          "-- [ ] 8B RSFT s43 补齐第 3 seed",
          "+- [x] 8B RSFT s43 补齐第 3 seed（d102_8b_rsft_k1_s43, ign_f1=0.5471）",
          " - [ ] experiment_plan.yaml 全面同步 registry",
          " - [ ] paper_framing.md 更新（D112 + D117 + D118 narrative 调整）",
          " - [ ] 重新提交论文审稿"
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

_source line 23_

<details open><summary>🔧 Tool call — Edit · `toolu_01TYTXys1FHafMpKMivJU43q`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/ROADMAP.md",
  "old_string": "RSFT variance stabilization (SFT std=3.72pp vs RSFT std=0.53pp)",
  "new_string": "RSFT variance stabilization (SFT std=3.72pp vs RSFT std=0.50pp)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b6fdd47b-2526-4425-9a48-a46eb2f42ea9",
  "uuid": "5c947962-9f1f-4155-88b8-a2ac8f4f16cd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011ERVt8T7tzaSWYyS8HXSu9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 363,
      "cache_read_input_tokens": 30618,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 363
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

_source line 24 · 2026-05-19T17:30:47.589Z_

<details><summary>↩ Tool result · `toolu_01TYTXys1FHafMpKMivJU43q`</summary>

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
  "session_id": "b6fdd47b-2526-4425-9a48-a46eb2f42ea9",
  "uuid": "b9a31658-9a0b-4c7c-a3bc-97410bb5c4c4",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/ROADMAP.md",
    "oldString": "RSFT variance stabilization (SFT std=3.72pp vs RSFT std=0.53pp)",
    "newString": "RSFT variance stabilization (SFT std=3.72pp vs RSFT std=0.50pp)",
    "originalFile": "# faith-evidence-ie — Research Dashboard\n\n> 最后更新: 2026-05-19 UTC | 更新原因: 8B RSFT 3-seed 完成 (mean=0.5433±0.50pp, 7.4x variance compression)\n\n## 核心方向\nFREIGE: LLM-based evidence-grounded DocRE 系统性研究。3 贡献：RSFT+NLI 有效性 / Decoupling spectrum / Scale-dependent evidence tax。详见 paper_framing.md。\n\n## 当前进展\n- **阶段**: 🚀 Research + 审稿并行（Round 1 = 3.0 Findings，目标 4.0 Main）\n- **Wave 1**: ✅ 全部完成（SFT seeds, GRPO bf16, Random RSFT）\n- **Scaling seeds (plan_019)**: 8B 3-seed SFT 完成（mean=0.5019±3.72pp）；8B 3-seed RSFT 完成（s42=0.5376, s43=0.5471, s44=0.5451; mean=0.5433±0.50pp）\n- **D112 full pipeline**: ✅ 完成（bf16 LoRA RSFT from SFT s44: ign_f1=0.5152, +4.18pp over SFT s44 baseline 0.4734）\n- **14B SFT (plan_017)**: ✅ 完成（D117: with-evidence 0.5507, no-evidence 0.551, evidence tax=0.03pp≈0）\n- **D118 claim 降级**: 1.7B RSFT (0.5122) vs 8B SFT mean (0.5019) Δ=+1.03pp, p≈0.34 不显著，降级为 \"comparable / on par with\"\n- **关键数值汇总**:\n\n| Scale | SFT mean (seeds) | RSFT mean (seeds) | Δ ign_f1 | SFT std | RSFT std |\n|-------|-------------------|--------------------|----------|---------|----------|\n| 1.7B | 0.4464 (3) | 0.5122 (1, s42 base) | +6.58pp | 2.79pp | — |\n| 4B | 0.4358 (3) | 0.4482 (3, Method A) / 0.5152 (1, Method B) | +1.24pp / +4.18pp (vs s44) | 3.80pp | 0.51pp |\n| 8B | 0.5019 (3) | 0.5433 (3, Method A) | +4.14pp | 3.72pp | 0.50pp |\n| 14B | 0.5507 (1) | pending | — | — | — |\n\n- **14B evidence tax**: 0.03pp（本质为零），14B 容量足够同时输出 evidence 和 RE\n- **RSFT variance 稳定化**: 8B SFT std=3.72pp → RSFT std=0.50pp (7.4x)；4B SFT std=3.80pp → RSFT std=0.51pp (7.5x)\n- **CED 价值**: CED RSFT (0.4482) > Random RSFT (0.4114) > SFT (0.3974)，+3.68pp gap\n- **GRPO**: bf16 ckpt-100 ign_f1=0.4431 无 catastrophic forgetting（D110），QLoRA 是 confound\n\n## 投稿目标\n- **EMNLP 2026 Main** (ARR July cycle, ~July 15-25, **~57 天**)\n\n## 实验路线（3 层优先级）\n\n### Tier 1 — Main 必要条件\n| 实验 | Plan ID | 状态 |\n|------|---------|------|\n| D102 k=1 方法论修正 | D102 | ✅ 完成 |\n| SFT 4B s43 + s44 + s42 reeval | plan_w3_sft_seeds | ✅ 完成 (D111) |\n| GRPO bf16 G=4 clean control | plan_015 | ✅ 完成 (D110/D113) |\n| Random k=1 RSFT baseline | plan_w18_random | ✅ 完成 (D109) |\n| 8B RSFT s44 seed expansion | plan_019 (8B) | ✅ 完成 (D115) |\n| 8B SFT s43 eval | plan_019 | ✅ 完成 (ign_f1=0.5324) |\n| D112 RSFT from SFT s44 (bf16) | plan_d112 | ✅ 完成 (D119: ign_f1=0.5152) |\n| 14B SFT (第 4 尺度) | plan_017 | ✅ 完成 (D117: 0.5507, tax=0.03pp) |\n| 1.7B RSFT s43/s44 重跑 | plan_019 (1.7B) | 🟡 进行中 |\n\n### Tier 2 — 大幅加分\n| 实验 | Plan ID | 状态 |\n|------|---------|------|\n| 14B RSFT + no-evidence + eval | plan_017 (后续) | pending（待启动） |\n| 8B RSFT s43 补齐第 3 seed | plan_019 | ✅ 完成 (d102_8b_rsft_k1_s43, ign_f1=0.5471) |\n| NLI model ablation | plan_010 | pending |\n| Evidence tax 机制分析 | plan_020 | pending |\n| Deep error analysis | plan_021 | pending |\n\n### Tier 3 — 锦上添花\n| 实验 | Plan ID | 状态 |\n|------|---------|------|\n| CDR/GDA 跨领域 | plan_018 | P2（无 evidence 标注） |\n| 第三模型家族 | plan_022 | pending |\n| DocKS-RAG/LMRC 复现 | plan_023 | pending |\n\n## 从 3.0 → 4.0 路径\n| 里程碑 | 预期评分 | 状态 |\n|--------|---------|------|\n| Wave 1 完成 + D112 | 3.0 → 3.5 | ✅ D112 完成 (0.5152, +4.18pp) |\n| + 1.7B/8B multi-seed 统计力 | 3.5 | 🟡 8B 3-seed done, 1.7B 进行中 |\n| + 14B 第 4 尺度档 | 3.5 → 3.75 | ✅ SFT 完成 (0.5507), RSFT pending |\n| + Mechanistic + error analysis | 3.75 → 4.0 | pending |\n\n## GPU 分布\n- cuda:0: 空闲（等待 Director 分配）\n- cuda:1: d112_rsft_no_evidence_eval_r3 (60%, ~50min remaining)\n- cuda:2: 空闲（等待 Director 分配）\n- cuda:3: plan019_1_7b_rsft_no_evidence_eval_2048 (47%, ~2h30m remaining)\n\n## 近期任务\n- [x] Wave 1 全部完成（SFT seeds, GRPO bf16, Random RSFT）\n- [x] 8B RSFT s44 eval (D115: 0.5451, variance 压缩 5x)\n- [x] 4B SFT s42 D076 reeval (D111: 0.3974)\n- [x] D112 step 4 eval 完成 (bf16 LoRA: ign_f1=0.5152, +4.18pp)\n- [x] 8B SFT s43 eval 完成 (ign_f1=0.5324)\n- [x] 14B SFT eval 完成 (D117: ign_f1=0.5507, evidence tax=0.03pp)\n- [ ] 1.7B no-evidence eval 2048 重跑（排除截断，cuda:3）\n- [ ] 8B RSFT no-evidence eval（cuda:0，接近完成）\n- [ ] D112 no-evidence eval r3（cuda:1，44%）\n- [ ] 14B RSFT pipeline（待启动）\n- [x] 8B RSFT s43 补齐第 3 seed（d102_8b_rsft_k1_s43, ign_f1=0.5471）\n- [ ] experiment_plan.yaml 全面同步 registry\n- [ ] paper_framing.md 更新（D112 + D117 + D118 narrative 调整）\n- [ ] 重新提交论文审稿\n\n## 关键风险\n- **D112 结果**: ✅ 已确认 RSFT-from-s44 (0.5152) > SFT s44 (0.4734) +4.18pp，Claim 1 robust\n- **1.7B claim 已降级 (D118)**: 1.7B RSFT vs 8B SFT Δ=+1.03pp, p≈0.34 不显著，改为 \"comparable\"；RSFT variance stabilization (SFT std=3.72pp vs RSFT std=0.53pp) 作为独立发现\n- **14B evidence tax = 0 (D117)**: 积极结果，14B 容量足够，Claim 3 需调整为 \"tax scales inversely with model capacity\"\n- **8B RSFT evidence quality trade-off**: EDCR 从 0.65-0.67 降到 0.62（RE↑/evidence precision↓），论文需讨论\n- **14B RSFT 待启动**: SFT 已完成，RSFT pipeline 是 Tier 2 首要任务\n- **EDCR 缺人工验证**: plan_013 取消，用 per-relation 分析 + Limitations 缓解\n\n## 关键决策日志\n\n| ID | 日期 | 摘要 | 关联实验 |\n|----|------|------|----------|\n| D120 | 2026-05-19 | D120: 8B RSFT 3-seed 确认 variance compression 7.4×， | d102_8b_rsft_k1_s43, plan019_8b_rsft_s44_eval |\n| D119 | 2026-05-19 | D119: D112 bf16 eval ign_f1=0.5152 确认 Method B (RS | d112_rsft_s44_eval_bf16, d112_rsft_s44_eval |\n| D118 | 2026-05-19 | D118: \"1.7B RSFT surpasses 8B SFT\" claim 降级为 \"appr | plan019_8b_sft_s43_eval, plan019_1_7b_rsft_s44_r2_eval |\n| D117 | 2026-05-19 | D117: 14B SFT evidence tax = 0.03pp（本质为零），完成 4 尺度  | plan017_14b_sft_eval_r2, plan017_14b_sft_no_evidence_eval_r2 |\n| D116 | 2026-05-19 | D116: D112 结果无效（QLoRA confound），必须用 bf16 LoRA 重跑 s | d112_rsft_s44_eval, d112_rsft_s44_train |\n| D115 | 2026-05-19 | D115: 8B RSFT s44 ign_f1=0.5451 确认 RSFT 跨 seed 稳健， | plan019_8b_rsft_s44_eval, eval_rsft_ced_s42 |\n| D114 | 2026-05-19 | D114: 1.7B RSFT s43/s44 应使用 Method A（s42 SFT base） | plan019_1_7b_rsft_s43, plan019_1_7b_rsft_s44, d112_rsft_s44_ced_score |\n| D113 | 2026-05-18 | D113: GRPO bf16 ckpt-100 为最优 checkpoint，ckpt-200 无 | grpo_bf16_g4_ckpt100_eval, grpo_bf16_g4_ckpt200_eval |\n| D112 | 2026-05-18 | D112: 4B RSFT ign_f1 claim 需重大 reframe——全部 RSFT 基于 | wave1_sft_4b_s43_eval_r2, wave1_sft_4b_s44_eval_r2, eval_rsft_ced_s42 |\n| D111 | 2026-05-18 | D111: 4B SFT s42 必须用 D076 协议重新 eval，统一三 seed 参考基准 | wave1_sft_4b_s43_eval_r2, wave1_sft_4b_s44_eval_r2 |\n\n",
    "structuredPatch": [
      {
        "oldStart": 92,
        "oldLines": 7,
        "newStart": 92,
        "newLines": 7,
        "lines": [
          " ",
          " ## 关键风险",
          " - **D112 结果**: ✅ 已确认 RSFT-from-s44 (0.5152) > SFT s44 (0.4734) +4.18pp，Claim 1 robust",
          "-- **1.7B claim 已降级 (D118)**: 1.7B RSFT vs 8B SFT Δ=+1.03pp, p≈0.34 不显著，改为 \"comparable\"；RSFT variance stabilization (SFT std=3.72pp vs RSFT std=0.53pp) 作为独立发现",
          "+- **1.7B claim 已降级 (D118)**: 1.7B RSFT vs 8B SFT Δ=+1.03pp, p≈0.34 不显著，改为 \"comparable\"；RSFT variance stabilization (SFT std=3.72pp vs RSFT std=0.50pp) 作为独立发现",
          " - **14B evidence tax = 0 (D117)**: 积极结果，14B 容量足够，Claim 3 需调整为 \"tax scales inversely with model capacity\"",
          " - **8B RSFT evidence quality trade-off**: EDCR 从 0.65-0.67 降到 0.62（RE↑/evidence precision↓），论文需讨论",
          " - **14B RSFT 待启动**: SFT 已完成，RSFT pipeline 是 Tier 2 首要任务"
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

_source line 25_

ROADMAP.md 已更新完毕，共 8 处修改：scaling table 8B 行（mean 0.5433/3seeds, Δ+4.14pp, std 0.50pp）、Tier 2 任务标记完成、近期任务勾选、variance compression 更新为 7.4x、GPU 分布刷新、风险区数值同步。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b6fdd47b-2526-4425-9a48-a46eb2f42ea9",
  "uuid": "f0359fa5-4065-4df3-8966-d3e36108cd99",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016CBXvy6o8V8q46snP77uJY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 243,
      "cache_read_input_tokens": 30981,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 243
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

### Task result

_source line 26_

ROADMAP.md 已更新完毕，共 8 处修改：scaling table 8B 行（mean 0.5433/3seeds, Δ+4.14pp, std 0.50pp）、Tier 2 任务标记完成、近期任务勾选、variance compression 更新为 7.4x、GPU 分布刷新、风险区数值同步。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 95148,
  "duration_api_ms": 96105,
  "num_turns": 10,
  "stop_reason": "end_turn",
  "session_id": "b6fdd47b-2526-4425-9a48-a46eb2f42ea9",
  "total_cost_usd": 0.32858925,
  "usage": {
    "input_tokens": 11,
    "cache_creation_input_tokens": 19777,
    "cache_read_input_tokens": 273990,
    "output_tokens": 2636,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 19777,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 107,
        "cache_read_input_tokens": 30981,
        "cache_creation_input_tokens": 243,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 243
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1913,
      "outputTokens": 24,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002033,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 11,
      "outputTokens": 2636,
      "cacheReadInputTokens": 273990,
      "cacheCreationInputTokens": 19777,
      "webSearchRequests": 0,
      "costUSD": 0.32655625,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "acf693ca-ecd8-4dc2-b91b-f4691b65150a"
}
```

</details>

---
