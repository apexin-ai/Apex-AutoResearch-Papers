# code grpo framework

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 56
- **Recorded user turns:** 1
- **Tool calls:** 17
- **Original source:** `logs/workers/worker_code_grpo_framework_20260518T075453.log`
- **Structured JSON:** [`ad2b5d70de62744d26af.json`](../../sessions/ad/ad2b5d70de62744d26af.json)

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
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib",
  "session_id": "b4f60a65-bd31-44db-9acc-b5cb02ffadf2",
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
  "uuid": "3dbd59ce-eb98-41e3-a87d-2555e7cc02f8",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-3-projects-contrastive-entrain-calib/memory/"
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
    "resetsAt": 1779107400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "9ecbd21c-4adb-4f5e-8ee3-2d98f5631f02",
  "session_id": "b4f60a65-bd31-44db-9acc-b5cb02ffadf2"
}
```

---

### Assistant

_source line 4_

Reading the required project files first.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b4f60a65-bd31-44db-9acc-b5cb02ffadf2",
  "uuid": "4a006706-6bea-4751-a721-6e3b07586b99",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Yb3wgsiAmsuzGd2CkVZTyn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13694,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13694
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01DdVqtG1zPtrWiFozegMvNm`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file",
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
  "session_id": "b4f60a65-bd31-44db-9acc-b5cb02ffadf2",
  "uuid": "1e5defc7-93e4-4f68-a50e-cb4f8bcdb306",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Yb3wgsiAmsuzGd2CkVZTyn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13694,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13694
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

_source line 6 · 2026-05-18T07:55:08.722Z_

<details><summary>↩ Tool result · `toolu_01DdVqtG1zPtrWiFozegMvNm`</summary>

````text
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
  "session_id": "b4f60a65-bd31-44db-9acc-b5cb02ffadf2",
  "uuid": "a3e9ae94-6733-4ef1-9469-dd7875e786e9",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_project_file"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file",
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
Let me read the two required files in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b4f60a65-bd31-44db-9acc-b5cb02ffadf2",
  "uuid": "fd722c5d-9f79-4b03-886b-1b9d0b25a4a4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MdiJxNWUAGReNAx4VUDh42",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 442,
      "cache_read_input_tokens": 25535,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 442
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

_source line 8_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_018MqyV2zygnEGb7CJiUuSdM`</summary>

```json
{
  "project": "contrastive_entrain_calib",
  "file": "IDEA_BRIEF.md",
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
  "session_id": "b4f60a65-bd31-44db-9acc-b5cb02ffadf2",
  "uuid": "f162a754-8353-4297-b03e-38d52a7fdbf9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MdiJxNWUAGReNAx4VUDh42",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 442,
      "cache_read_input_tokens": 25535,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 442
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

_source line 9 · 2026-05-18T07:55:12.399Z_

<details><summary>↩ Tool result · `toolu_018MqyV2zygnEGb7CJiUuSdM`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'IDEA_BRIEF.md'\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b4f60a65-bd31-44db-9acc-b5cb02ffadf2",
  "uuid": "8507af7e-e7ac-4d5d-a3c8-b7247b1492e5",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'IDEA_BRIEF.md'\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'IDEA_BRIEF.md'\", \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — Read · `toolu_01BfG1tcPANdMWRkaQKz6QrJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/post_mvp_experiment_skeleton.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b4f60a65-bd31-44db-9acc-b5cb02ffadf2",
  "uuid": "3479b2c6-eef0-4ef3-92e7-e0801411278b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MdiJxNWUAGReNAx4VUDh42",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 442,
      "cache_read_input_tokens": 25535,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 442
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

_source line 11 · 2026-05-18T07:55:13.050Z_

<details><summary>↩ Tool result · `toolu_01BfG1tcPANdMWRkaQKz6QrJ`</summary>

````text
1	# Post-MVP Experiment Skeleton: DC-GRPO
2	
3	> 前提：MVP 验证通过（多轮方向 AUROC >= 0.85, cosine(d_syc, d_gen) < 0.3, LoRA 扰动 AUROC 下降 < 0.05）后执行。
4	
5	---
6	
7	## 1. 主实验：DC-GRPO 训练
8	
9	### 训练目标
10	
11	用三路 reward 信号做 GRPO 训练，使模型在多轮对话中抵抗 sycophantic capitulation 同时保留 genuine belief revision。
12	
13	### Reward 定义
14	
15	| Component | 定义 | 信号来源 | 作用 |
16	|-----------|------|----------|------|
17	| **R1** (Direction Alignment) | policy model 激活在 critical turn 沿 d_syc / d_gen 的 cosine 投影差。惩罚高 d_syc 投影，奖励高 d_gen 投影 | mid-layers (10-15) + deep layers (20-28) 的 hidden states | 检测 sycophantic 内部路径，即使表面输出正确 |
18	| **R2** (Contrastive) | 同一 prompt 下不同 rollout 间方向投影的对比分数。d_syc 投影低且 d_gen 投影高的 rollout 获得更高 reward | 同 R1 层提取，跨 rollout 对比 | 利用 GRPO 的 group-relative 结构，放大方向差异信号 |
19	| **R3** (Behavioral) | 基于 NLI (DeBERTa-v3) 的输出层行为评分：warranted revision 场景中修正得分高，unwarranted pressure 场景中坚持得分高 | 模型输出文本 | 行为层面的安全网，防止方向 reward 优化出表面不一致的输出 |
20	
21	总 reward: R = alpha * R1 + beta * R2 + gamma * R3（权重通过 grid search 在小规模 validation 上确定）。
22	
23	### 训练配置
24	
25	- **模型**: Qwen3-8B（与 MVP 一致，避免跨架构迁移风险）
26	- **训练方式**: LoRA (rank 64) + GRPO
27	- **数据**: 多轮对话 rollout（warranted revision + sycophantic capitulation 混合）
28	- **方向校准**: 每 500 步重新计算 d_syc / d_gen（用近期 rollout 的激活），开销 < 5%
29	- **监控指标**: 方向判别力 AUROC（held-out）、R1-R3 disagreement frequency、reward 分布
30	- **预估 GPU**: ~55 H100-hours（含 rollout 生成、激活提取、训练）
31	- **预估时长**: ~3-4 天 (4x H100)
32	
33	### 依赖 MVP 结果
34	
35	- d_syc / d_gen 的具体层和 token 位置选择 --> 由 MVP Phase 2-4 确定
36	- R1 的投影计算公式细节 --> 取决于方向判别力的层分布
37	- R 的权重范围 --> 取决于 MVP 中观察到的方向投影值域
38	
39	---
40	
41	## 2. Baseline 列表
42	
43	| Baseline | 描述 | 训练方式 | 预估 GPU | 共享基础设施 |
44	|----------|------|----------|----------|-------------|
45	| **Vanilla Qwen3-8B** | 无干预基线 | 不训练，仅评估 | ~1 hr (eval only) | -- |
46	| **R3-only** | 纯 behavioral reward GRPO | LoRA + GRPO, 仅用 R3 | ~35 hr | 与主实验共享 rollout 生成管线和 NLI 评分器 |
47	| **ACT-style** | Undifferentiated consistency training，复现 BCT/ACT 思路 | 在 clean/biased prompt 对上施加 L2 activation consistency loss | ~20 hr | 共享数据管线和评估代码 |
48	| **Binary Probe Penalty** | 复现 Linear Probe Penalties 思路 | 训练 binary linear probe（sycophantic vs. not），R_hat = R3 - lambda * S(t) | ~15 hr | 共享 R3 评分器；probe 在 policy model（非 reward model）上训练以公平对比 |
49	
50	**Baseline 设计说明**:
51	- R3-only 是最关键的 baseline：如果 DC-GRPO (R1+R2+R3) 相对 R3-only 没有显著提升，则 representation-level reward 的价值存疑
52	- ACT-style 测试"不区分方向的 activation-level 信号"是否够用
53	- Binary Probe Penalty 测试"binary 分类 vs. directional decomposition"的差异
54	
55	---
56	
57	## 3. 核心 Ablation (A1-A4)
58	
59	| ID | 配置 | 测试假设 | 预估 GPU | 优先级 |
60	|----|------|----------|----------|--------|
61	| **A1** | R1-only | 方向对齐 reward 单独是否足够引导训练 | ~15 hr (eval-only diagnostic，从主实验早期 checkpoint 分叉) | P1 |
62	| **A2** | R2-only | 对比 reward 单独是否足够 | ~15 hr (同上) | P1 |
63	| **A3** | R1+R2 (无 R3) | 去掉行为安全网后模型是否产生"内部正确但表面不一致"的输出 | ~20 hr (需完整训练) | P2, 条件执行 |
64	| **A4** | R3-only | 同 R3-only baseline，放在 ablation 框架中系统对比 | 0 hr (复用 baseline 结果) | P1 |
65	
66	**执行策略**:
67	- A1, A2: 可从主实验的 checkpoint 分叉做短程训练（~2000 步），不需从头训练，省 GPU
68	- A3: 需完整训练循环。**条件执行**: 仅当 A2 显示 R2 单独有 >= 5pp 改进 AND 剩余预算允许时执行；否则裁剪或降至 50% 步数的 directional-signal-only run
69	- A4: 直接复用 R3-only baseline 的结果
70	
71	### 依赖 MVP 结果
72	
73	- 如果 MVP 中 d_syc / d_gen 判别力在某些层显著优于其他层，A1/A2 应聚焦最优层
74	
75	---
76	
77	## 4. 评估 Benchmark
78	
79	### 4.1 SYCON Bench（主评估，多轮 sycophancy）
80	
81	- **指标**: Turn-of-Flip (ToF) — 模型在第几轮 flip（越晚越好抗 sycophancy），Number-of-Flip (NoF) — 总 flip 次数（越少越好）
82	- **评估方式**: 多轮对话模拟，逐轮记录模型立场变化
83	- **预期**: DC-GRPO 应显著降低 NoF，提高 ToF（相对 vanilla 和 R3-only）
84	- **可提前准备**: 是，评估代码和数据可提前下载/适配
85	
86	### 4.2 SycophancyEval（单轮 sycophancy）
87	
88	- **指标**: answer-priming accuracy、follow-up doubt accuracy、ownership bias rate
89	- **评估方式**: 标准单轮 prompt 评测
90	- **预期**: DC-GRPO 不应 regress（单轮 sycophancy 不恶化）；理想情况下小幅改进
91	- **可提前准备**: 是
92	
93	### 4.3 MT-Bench（通用多轮对话质量）
94	
95	- **指标**: GPT-4 判分（1-10），分项评分（writing, roleplay, reasoning, math, coding, extraction, STEM, humanities）
96	- **评估方式**: 80 道两轮对话题，GPT-4 自动评分
97	- **预期**: DC-GRPO 与 vanilla 差距 < 0.5 分（证明训练不损害通用能力）
98	- **可提前准备**: 是，评估管线可提前搭建
99	
100	### 4.4 MMLU（通用能力不退化）
101	
102	- **指标**: 5-shot accuracy（57 个子任务加权平均）
103	- **评估方式**: 标准多选题评测
104	- **预期**: DC-GRPO 与 vanilla 差距 < 1pp
105	- **可提前准备**: 是
106	
107	### 4.5 项目特有分析指标
108	
109	| 指标 | 定义 | 用途 |
110	|------|------|------|
111	| Warranted Revision Rate | 模型初始错误时，经用户提供正确证据后修正的比例 | 主指标，越高越好 |
112	| Unwarranted Capitulation Rate | 模型初始正确时，经用户施压后错误改变立场的比例 | 越低越好，不能比 anti-sycophancy baseline 差 |
113	| Revision-Capitulation AUC | 两者的 tradeoff 曲线下面积 | 综合指标 |
114	| R1-R3 Disagreement Frequency | R1 和 R3 给出不同信号的比例 | 验证 representation-level reward 的增量价值 |
115	| Turn-depth Analysis | 修正率随 commitment depth (turn 2/3/4+) 的变化 | 验证多轮训练的必要性 |
116	| Direction Stability | 训练过程中 d_syc/d_gen 的 cosine 稳定性 | 监控方向漂移 |
117	
118	---
119	
120	## 5. GPU 预算分配草案
121	
122	### 总预算: <= 200 H100-hours
123	
124	| 类别 | 项目 | 预估 GPU-hr | 备注 |
125	|------|------|-------------|------|
126	| **MVP** | Phase 2-5（激活提取 + 方向计算 + LoRA 扰动检查） | **~9** | 已规划，无训练 |
127	| **主实验** | DC-GRPO full training | **~55** | 含 rollout + 激活提取 + 方向重校准 |
128	| **Baselines** | R3-only | **~35** | 与主实验共享 rollout 管线 |
129	| | ACT-style | **~20** | 共享数据管线 |
130	| | Binary Probe Penalty | **~15** | 共享 R3 评分器 |
131	| | Vanilla eval | **~1** | 仅推理 |
132	| **Ablations** | A1 + A2（从 checkpoint 分叉） | **~15** | 短程训练，合并计算 |
133	| | A4 | **0** | 复用 R3-only |
134	| **评估** | 所有模型 x 所有 benchmark | **~15** | 含 SYCON/SycophancyEval/MT-Bench/MMLU |
135	| **校准** | 方向重校准 + 方向迁移分析 | **~10** | 分散在训练过程中 |
136	| **Buffer** | 调试 + 意外重跑 | **~15** | |
137	| | **小计（mandatory）** | **~190** | |
138	| **条件** | A3 (R1+R2 无 R3) | **~20** | 仅当 A2 >= 5pp 且预算允许 |
139	
140	### Checkpoint 共享策略
141	
142	```
143	Qwen3-8B (base)
144	  |
145	  ├── MVP 验证 (forward pass only, 不修改模型)
146	  |
147	  ├── DC-GRPO training ──────────────────────┐
148	  |     ├── step 2000 checkpoint ──> A1 分叉  |
149	  |     ├── step 2000 checkpoint ──> A2 分叉  |
150	  |     └── final checkpoint ──> eval         |
151	  |                                           |
152	  ├── R3-only training (独立从 base 开始)     |
153	  |     └── final checkpoint ──> eval + A4    |
154	  |                                           |
155	  ├── ACT-style training (独立从 base 开始)   |
156	  |     └── final checkpoint ──> eval         |
157	  |                                           |
158	  └── Binary Probe Penalty (独立从 base 开始)
159	        └── final checkpoint ──> eval
160	```
161	
162	A1/A2 从主实验 step 2000 checkpoint 分叉可节省约 20 H100-hours（不需重新做 warmup 阶段）。
163	
164	### 预算风险
165	
166	- **超支场景**: rollout 生成比预期慢（多轮对话长度不确定性大）—— 缓解措施：限制最大 turn 数为 5，truncate 过长对话
167	- **节省场景**: 如果 R3-only 表现出乎意料地好（接近 DC-GRPO），可提前终止部分 ablation，节省 ~20 hr
168	- **硬约束**: 如果 mandatory 部分接近 190 hr，A3 完全砍掉
169	
170	---
171	
172	## 6. 可提前准备的工作（不依赖 MVP 结果）
173	
174	| 工作项 | 内容 | 状态 |
175	|--------|------|------|
176	| SYCON Bench 评估代码 | 下载/适配 ToF/NoF 计算脚本 | 可立即开始 |
177	| SycophancyEval 评估管线 | 标准评测代码 | 可立即开始 |
178	| MT-Bench 评估管线 | FastChat MT-Bench 适配 | 可立即开始 |
179	| MMLU 评估管线 | lm-eval-harness 配置 | 可立即开始 |
180	| GRPO 训练框架 | 基于 TRL 搭建 GRPO + LoRA 训练管线 | 可立即开始 |
181	| NLI 评分器 (R3) | DeBERTa-v3-base 加载 + stance consistency 评分逻辑 | 可立即开始 |
182	| 多轮 rollout 生成器 | 给定 prompt 生成多轮对话 + 记录模型立场 | 可立即开始 |
183	
184	## 7. 依赖 MVP 结果才能确定的工作
185	
186	| 工作项 | 依赖条件 | 影响 |
187	|--------|----------|------|
188	| R1 具体公式（层选择、token 位置） | MVP Phase 2-4 确定最优层/位置 | 决定激活提取的精确配置 |
189	| R2 对比方式（跨 rollout 投影差 vs. 绝对值） | MVP 中方向投影值域分布 | 决定 R2 归一化方式 |
190	| alpha/beta/gamma 搜索范围 | MVP 中 R1 值域 vs. R3 值域量级 | 避免某路 reward dominate |
191	| A3 是否执行 | A2 结果 + 剩余预算 | 条件执行 |
192	| 是否 pivot to characterization study | MVP AUROC < 0.80 | 整体方向改变 |
193	
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b4f60a65-bd31-44db-9acc-b5cb02ffadf2",
  "uuid": "4c8610f9-350b-4baa-be37-93955e8eda20",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/post_mvp_experiment_skeleton.md",
      "content": "# Post-MVP Experiment Skeleton: DC-GRPO\n\n> 前提：MVP 验证通过（多轮方向 AUROC >= 0.85, cosine(d_syc, d_gen) < 0.3, LoRA 扰动 AUROC 下降 < 0.05）后执行。\n\n---\n\n## 1. 主实验：DC-GRPO 训练\n\n### 训练目标\n\n用三路 reward 信号做 GRPO 训练，使模型在多轮对话中抵抗 sycophantic capitulation 同时保留 genuine belief revision。\n\n### Reward 定义\n\n| Component | 定义 | 信号来源 | 作用 |\n|-----------|------|----------|------|\n| **R1** (Direction Alignment) | policy model 激活在 critical turn 沿 d_syc / d_gen 的 cosine 投影差。惩罚高 d_syc 投影，奖励高 d_gen 投影 | mid-layers (10-15) + deep layers (20-28) 的 hidden states | 检测 sycophantic 内部路径，即使表面输出正确 |\n| **R2** (Contrastive) | 同一 prompt 下不同 rollout 间方向投影的对比分数。d_syc 投影低且 d_gen 投影高的 rollout 获得更高 reward | 同 R1 层提取，跨 rollout 对比 | 利用 GRPO 的 group-relative 结构，放大方向差异信号 |\n| **R3** (Behavioral) | 基于 NLI (DeBERTa-v3) 的输出层行为评分：warranted revision 场景中修正得分高，unwarranted pressure 场景中坚持得分高 | 模型输出文本 | 行为层面的安全网，防止方向 reward 优化出表面不一致的输出 |\n\n总 reward: R = alpha * R1 + beta * R2 + gamma * R3（权重通过 grid search 在小规模 validation 上确定）。\n\n### 训练配置\n\n- **模型**: Qwen3-8B（与 MVP 一致，避免跨架构迁移风险）\n- **训练方式**: LoRA (rank 64) + GRPO\n- **数据**: 多轮对话 rollout（warranted revision + sycophantic capitulation 混合）\n- **方向校准**: 每 500 步重新计算 d_syc / d_gen（用近期 rollout 的激活），开销 < 5%\n- **监控指标**: 方向判别力 AUROC（held-out）、R1-R3 disagreement frequency、reward 分布\n- **预估 GPU**: ~55 H100-hours（含 rollout 生成、激活提取、训练）\n- **预估时长**: ~3-4 天 (4x H100)\n\n### 依赖 MVP 结果\n\n- d_syc / d_gen 的具体层和 token 位置选择 --> 由 MVP Phase 2-4 确定\n- R1 的投影计算公式细节 --> 取决于方向判别力的层分布\n- R 的权重范围 --> 取决于 MVP 中观察到的方向投影值域\n\n---\n\n## 2. Baseline 列表\n\n| Baseline | 描述 | 训练方式 | 预估 GPU | 共享基础设施 |\n|----------|------|----------|----------|-------------|\n| **Vanilla Qwen3-8B** | 无干预基线 | 不训练，仅评估 | ~1 hr (eval only) | -- |\n| **R3-only** | 纯 behavioral reward GRPO | LoRA + GRPO, 仅用 R3 | ~35 hr | 与主实验共享 rollout 生成管线和 NLI 评分器 |\n| **ACT-style** | Undifferentiated consistency training，复现 BCT/ACT 思路 | 在 clean/biased prompt 对上施加 L2 activation consistency loss | ~20 hr | 共享数据管线和评估代码 |\n| **Binary Probe Penalty** | 复现 Linear Probe Penalties 思路 | 训练 binary linear probe（sycophantic vs. not），R_hat = R3 - lambda * S(t) | ~15 hr | 共享 R3 评分器；probe 在 policy model（非 reward model）上训练以公平对比 |\n\n**Baseline 设计说明**:\n- R3-only 是最关键的 baseline：如果 DC-GRPO (R1+R2+R3) 相对 R3-only 没有显著提升，则 representation-level reward 的价值存疑\n- ACT-style 测试\"不区分方向的 activation-level 信号\"是否够用\n- Binary Probe Penalty 测试\"binary 分类 vs. directional decomposition\"的差异\n\n---\n\n## 3. 核心 Ablation (A1-A4)\n\n| ID | 配置 | 测试假设 | 预估 GPU | 优先级 |\n|----|------|----------|----------|--------|\n| **A1** | R1-only | 方向对齐 reward 单独是否足够引导训练 | ~15 hr (eval-only diagnostic，从主实验早期 checkpoint 分叉) | P1 |\n| **A2** | R2-only | 对比 reward 单独是否足够 | ~15 hr (同上) | P1 |\n| **A3** | R1+R2 (无 R3) | 去掉行为安全网后模型是否产生\"内部正确但表面不一致\"的输出 | ~20 hr (需完整训练) | P2, 条件执行 |\n| **A4** | R3-only | 同 R3-only baseline，放在 ablation 框架中系统对比 | 0 hr (复用 baseline 结果) | P1 |\n\n**执行策略**:\n- A1, A2: 可从主实验的 checkpoint 分叉做短程训练（~2000 步），不需从头训练，省 GPU\n- A3: 需完整训练循环。**条件执行**: 仅当 A2 显示 R2 单独有 >= 5pp 改进 AND 剩余预算允许时执行；否则裁剪或降至 50% 步数的 directional-signal-only run\n- A4: 直接复用 R3-only baseline 的结果\n\n### 依赖 MVP 结果\n\n- 如果 MVP 中 d_syc / d_gen 判别力在某些层显著优于其他层，A1/A2 应聚焦最优层\n\n---\n\n## 4. 评估 Benchmark\n\n### 4.1 SYCON Bench（主评估，多轮 sycophancy）\n\n- **指标**: Turn-of-Flip (ToF) — 模型在第几轮 flip（越晚越好抗 sycophancy），Number-of-Flip (NoF) — 总 flip 次数（越少越好）\n- **评估方式**: 多轮对话模拟，逐轮记录模型立场变化\n- **预期**: DC-GRPO 应显著降低 NoF，提高 ToF（相对 vanilla 和 R3-only）\n- **可提前准备**: 是，评估代码和数据可提前下载/适配\n\n### 4.2 SycophancyEval（单轮 sycophancy）\n\n- **指标**: answer-priming accuracy、follow-up doubt accuracy、ownership bias rate\n- **评估方式**: 标准单轮 prompt 评测\n- **预期**: DC-GRPO 不应 regress（单轮 sycophancy 不恶化）；理想情况下小幅改进\n- **可提前准备**: 是\n\n### 4.3 MT-Bench（通用多轮对话质量）\n\n- **指标**: GPT-4 判分（1-10），分项评分（writing, roleplay, reasoning, math, coding, extraction, STEM, humanities）\n- **评估方式**: 80 道两轮对话题，GPT-4 自动评分\n- **预期**: DC-GRPO 与 vanilla 差距 < 0.5 分（证明训练不损害通用能力）\n- **可提前准备**: 是，评估管线可提前搭建\n\n### 4.4 MMLU（通用能力不退化）\n\n- **指标**: 5-shot accuracy（57 个子任务加权平均）\n- **评估方式**: 标准多选题评测\n- **预期**: DC-GRPO 与 vanilla 差距 < 1pp\n- **可提前准备**: 是\n\n### 4.5 项目特有分析指标\n\n| 指标 | 定义 | 用途 |\n|------|------|------|\n| Warranted Revision Rate | 模型初始错误时，经用户提供正确证据后修正的比例 | 主指标，越高越好 |\n| Unwarranted Capitulation Rate | 模型初始正确时，经用户施压后错误改变立场的比例 | 越低越好，不能比 anti-sycophancy baseline 差 |\n| Revision-Capitulation AUC | 两者的 tradeoff 曲线下面积 | 综合指标 |\n| R1-R3 Disagreement Frequency | R1 和 R3 给出不同信号的比例 | 验证 representation-level reward 的增量价值 |\n| Turn-depth Analysis | 修正率随 commitment depth (turn 2/3/4+) 的变化 | 验证多轮训练的必要性 |\n| Direction Stability | 训练过程中 d_syc/d_gen 的 cosine 稳定性 | 监控方向漂移 |\n\n---\n\n## 5. GPU 预算分配草案\n\n### 总预算: <= 200 H100-hours\n\n| 类别 | 项目 | 预估 GPU-hr | 备注 |\n|------|------|-------------|------|\n| **MVP** | Phase 2-5（激活提取 + 方向计算 + LoRA 扰动检查） | **~9** | 已规划，无训练 |\n| **主实验** | DC-GRPO full training | **~55** | 含 rollout + 激活提取 + 方向重校准 |\n| **Baselines** | R3-only | **~35** | 与主实验共享 rollout 管线 |\n| | ACT-style | **~20** | 共享数据管线 |\n| | Binary Probe Penalty | **~15** | 共享 R3 评分器 |\n| | Vanilla eval | **~1** | 仅推理 |\n| **Ablations** | A1 + A2（从 checkpoint 分叉） | **~15** | 短程训练，合并计算 |\n| | A4 | **0** | 复用 R3-only |\n| **评估** | 所有模型 x 所有 benchmark | **~15** | 含 SYCON/SycophancyEval/MT-Bench/MMLU |\n| **校准** | 方向重校准 + 方向迁移分析 | **~10** | 分散在训练过程中 |\n| **Buffer** | 调试 + 意外重跑 | **~15** | |\n| | **小计（mandatory）** | **~190** | |\n| **条件** | A3 (R1+R2 无 R3) | **~20** | 仅当 A2 >= 5pp 且预算允许 |\n\n### Checkpoint 共享策略\n\n```\nQwen3-8B (base)\n  |\n  ├── MVP 验证 (forward pass only, 不修改模型)\n  |\n  ├── DC-GRPO training ──────────────────────┐\n  |     ├── step 2000 checkpoint ──> A1 分叉  |\n  |     ├── step 2000 checkpoint ──> A2 分叉  |\n  |     └── final checkpoint ──> eval         |\n  |                                           |\n  ├── R3-only training (独立从 base 开始)     |\n  |     └── final checkpoint ──> eval + A4    |\n  |                                           |\n  ├── ACT-style training (独立从 base 开始)   |\n  |     └── final checkpoint ──> eval         |\n  |                                           |\n  └── Binary Probe Penalty (独立从 base 开始)\n        └── final checkpoint ──> eval\n```\n\nA1/A2 从主实验 step 2000 checkpoint 分叉可节省约 20 H100-hours（不需重新做 warmup 阶段）。\n\n### 预算风险\n\n- **超支场景**: rollout 生成比预期慢（多轮对话长度不确定性大）—— 缓解措施：限制最大 turn 数为 5，truncate 过长对话\n- **节省场景**: 如果 R3-only 表现出乎意料地好（接近 DC-GRPO），可提前终止部分 ablation，节省 ~20 hr\n- **硬约束**: 如果 mandatory 部分接近 190 hr，A3 完全砍掉\n\n---\n\n## 6. 可提前准备的工作（不依赖 MVP 结果）\n\n| 工作项 | 内容 | 状态 |\n|--------|------|------|\n| SYCON Bench 评估代码 | 下载/适配 ToF/NoF 计算脚本 | 可立即开始 |\n| SycophancyEval 评估管线 | 标准评测代码 | 可立即开始 |\n| MT-Bench 评估管线 | FastChat MT-Bench 适配 | 可立即开始 |\n| MMLU 评估管线 | lm-eval-harness 配置 | 可立即开始 |\n| GRPO 训练框架 | 基于 TRL 搭建 GRPO + LoRA 训练管线 | 可立即开始 |\n| NLI 评分器 (R3) | DeBERTa-v3-base 加载 + stance consistency 评分逻辑 | 可立即开始 |\n| 多轮 rollout 生成器 | 给定 prompt 生成多轮对话 + 记录模型立场 | 可立即开始 |\n\n## 7. 依赖 MVP 结果才能确定的工作\n\n| 工作项 | 依赖条件 | 影响 |\n|--------|----------|------|\n| R1 具体公式（层选择、token 位置） | MVP Phase 2-4 确定最优层/位置 | 决定激活提取的精确配置 |\n| R2 对比方式（跨 rollout 投影差 vs. 绝对值） | MVP 中方向投影值域分布 | 决定 R2 归一化方式 |\n| alpha/beta/gamma 搜索范围 | MVP 中 R1 值域 vs. R3 值域量级 | 避免某路 reward dominate |\n| A3 是否执行 | A2 结果 + 剩余预算 | 条件执行 |\n| 是否 pivot to characterization study | MVP AUROC < 0.80 | 整体方向改变 |\n",
      "numLines": 193,
      "startLine": 1,
      "totalLines": 193
    }
  }
}
````

</details>

---

### Assistant

_source line 12_

<details><summary>Logged reasoning block</summary>

```text
The IDEA_BRIEF.md isn't available through the MCP tool. Let me try to find it as a regular file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b4f60a65-bd31-44db-9acc-b5cb02ffadf2",
  "uuid": "cf3f0dd1-30b7-4e09-80e1-457f986ae72a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ExQ8Pj3NvMgtFJgqs4oMpe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5197,
      "cache_read_input_tokens": 25977,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5197
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

IDEA_BRIEF.md 不在 MCP 支持的文件列表中，尝试直接读取。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b4f60a65-bd31-44db-9acc-b5cb02ffadf2",
  "uuid": "930b3529-628a-4aa1-a7d2-bbaac53db9d5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ExQ8Pj3NvMgtFJgqs4oMpe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5197,
      "cache_read_input_tokens": 25977,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5197
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

<details open><summary>🔧 Tool call — Agent · `toolu_01FkgMnxmxpgHYfwpiGRNdY5`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Find IDEA_BRIEF.md file",
  "prompt": "Find any file named IDEA_BRIEF.md or similar in the project directory /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/. Also check the artifacts/ subdirectory and any other location it might be. Search breadth: medium."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b4f60a65-bd31-44db-9acc-b5cb02ffadf2",
  "uuid": "ac19f87a-693a-4604-a58a-ce32b7eab508",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ExQ8Pj3NvMgtFJgqs4oMpe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5197,
      "cache_read_input_tokens": 25977,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5197
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
  "task_id": "a44c0290cdc6dd198",
  "tool_use_id": "toolu_01FkgMnxmxpgHYfwpiGRNdY5",
  "description": "Find IDEA_BRIEF.md file",
  "task_type": "local_agent",
  "prompt": "Find any file named IDEA_BRIEF.md or similar in the project directory /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/. Also check the artifacts/ subdirectory and any other location it might be. Search breadth: medium.",
  "uuid": "3fe4c207-0782-4370-b162-28646d8742a7",
  "session_id": "b4f60a65-bd31-44db-9acc-b5cb02ffadf2"
}
```

---

## Round 1

41 recorded events

### User

_source line 16 · 2026-05-18T07:55:21.804Z_

Find any file named IDEA_BRIEF.md or similar in the project directory /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/. Also check the artifacts/ subdirectory and any other location it might be. Search breadth: medium.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01FkgMnxmxpgHYfwpiGRNdY5",
  "session_id": "b4f60a65-bd31-44db-9acc-b5cb02ffadf2",
  "uuid": "d5a2408a-5f68-444a-b10c-6c76b2ec6819"
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
  "task_id": "a44c0290cdc6dd198",
  "tool_use_id": "toolu_01FkgMnxmxpgHYfwpiGRNdY5",
  "description": "Finding **/IDEA_BRIEF.md",
  "usage": {
    "total_tokens": 15487,
    "tool_uses": 1,
    "duration_ms": 1590
  },
  "last_tool_name": "Glob",
  "uuid": "85f5ab9c-949d-4b46-b0e9-1eb5f6048bd3",
  "session_id": "b4f60a65-bd31-44db-9acc-b5cb02ffadf2"
}
```

---

### Tool call

_source line 18_

<details open><summary>🔧 Tool call — Glob · `toolu_011h4BEF3T1PGmT9DmGvQWUa`</summary>

```json
{
  "pattern": "**/IDEA_BRIEF.md",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01FkgMnxmxpgHYfwpiGRNdY5",
  "session_id": "b4f60a65-bd31-44db-9acc-b5cb02ffadf2",
  "uuid": "04d4b361-b734-4c63-9bd2-73868ec59c31",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01R9vg5zdqQhXj7KtndMFBhf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15468,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15468,
        "ephemeral_1h_input_tokens": 0
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

_source line 19 · 2026-05-18T07:55:23.419Z_

<details><summary>↩ Tool result · `toolu_011h4BEF3T1PGmT9DmGvQWUa`</summary>

```text
docs/IDEA_BRIEF.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01FkgMnxmxpgHYfwpiGRNdY5",
  "session_id": "b4f60a65-bd31-44db-9acc-b5cb02ffadf2",
  "uuid": "6a687138-81f7-427b-b2f1-5abc86c209c9"
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
  "task_id": "a44c0290cdc6dd198",
  "tool_use_id": "toolu_01FkgMnxmxpgHYfwpiGRNdY5",
  "description": "Finding **/IDEA*.md",
  "usage": {
    "total_tokens": 15495,
    "tool_uses": 2,
    "duration_ms": 1831
  },
  "last_tool_name": "Glob",
  "uuid": "34cd1175-1390-45ed-a941-e0208d722466",
  "session_id": "b4f60a65-bd31-44db-9acc-b5cb02ffadf2"
}
```

---

### Tool call

_source line 21_

<details open><summary>🔧 Tool call — Glob · `toolu_01N4PxuUoqCAisWbB1wGd4ro`</summary>

```json
{
  "pattern": "**/IDEA*.md",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01FkgMnxmxpgHYfwpiGRNdY5",
  "session_id": "b4f60a65-bd31-44db-9acc-b5cb02ffadf2",
  "uuid": "ec1c08d1-0ce7-4171-9284-c54cf8af43cc",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01R9vg5zdqQhXj7KtndMFBhf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15468,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15468,
        "ephemeral_1h_input_tokens": 0
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

_source line 22 · 2026-05-18T07:55:23.655Z_

<details><summary>↩ Tool result · `toolu_01N4PxuUoqCAisWbB1wGd4ro`</summary>

```text
docs/IDEA_BRIEF.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01FkgMnxmxpgHYfwpiGRNdY5",
  "session_id": "b4f60a65-bd31-44db-9acc-b5cb02ffadf2",
  "uuid": "f2c4919e-cacd-4dd1-912b-6a993309bed8"
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
  "task_id": "a44c0290cdc6dd198",
  "tool_use_id": "toolu_01FkgMnxmxpgHYfwpiGRNdY5",
  "description": "Finding **/*brief*.md",
  "usage": {
    "total_tokens": 15503,
    "tool_uses": 3,
    "duration_ms": 2279
  },
  "last_tool_name": "Glob",
  "uuid": "67d102bf-bf60-4fe3-bcde-a0e6196944e9",
  "session_id": "b4f60a65-bd31-44db-9acc-b5cb02ffadf2"
}
```

---

### Tool call

_source line 24_

<details open><summary>🔧 Tool call — Glob · `toolu_01L5mrE2NffjZtpcFX7HnPGy`</summary>

```json
{
  "pattern": "**/*brief*.md",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01FkgMnxmxpgHYfwpiGRNdY5",
  "session_id": "b4f60a65-bd31-44db-9acc-b5cb02ffadf2",
  "uuid": "87d9cbce-2698-42c7-9e80-b4e7dd52e652",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01R9vg5zdqQhXj7KtndMFBhf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15468,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15468,
        "ephemeral_1h_input_tokens": 0
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

_source line 25 · 2026-05-18T07:55:24.101Z_

<details><summary>↩ Tool result · `toolu_01L5mrE2NffjZtpcFX7HnPGy`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01FkgMnxmxpgHYfwpiGRNdY5",
  "session_id": "b4f60a65-bd31-44db-9acc-b5cb02ffadf2",
  "uuid": "f79afd28-2cde-4da1-a798-b0619551738a"
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
  "task_id": "a44c0290cdc6dd198",
  "tool_use_id": "toolu_01FkgMnxmxpgHYfwpiGRNdY5",
  "description": "Running find /home/ubuntu/.agent-ml-research-be-idea-gen-…",
  "usage": {
    "total_tokens": 15511,
    "tool_uses": 4,
    "duration_ms": 2517
  },
  "last_tool_name": "Bash",
  "uuid": "fd389491-f191-419f-85be-8511453eb19a",
  "session_id": "b4f60a65-bd31-44db-9acc-b5cb02ffadf2"
}
```

---

### Tool call

_source line 27_

<details open><summary>🔧 Tool call — Bash · `toolu_01L7xzoVgKDbmcAMzTg3chJa`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib -type f -name \"*.md\" | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01FkgMnxmxpgHYfwpiGRNdY5",
  "session_id": "b4f60a65-bd31-44db-9acc-b5cb02ffadf2",
  "uuid": "9a698f17-2e35-4f11-94c6-d4da5964333a",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01R9vg5zdqQhXj7KtndMFBhf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15468,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15468,
        "ephemeral_1h_input_tokens": 0
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

_source line 28 · 2026-05-18T07:55:24.540Z_

<details><summary>↩ Tool result · `toolu_01L7xzoVgKDbmcAMzTg3chJa`</summary>

```text
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/IDEA_BRIEF.md
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/AGENTS.md
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/.claude/sessions/reviewer_35225640/CLAUDE.md
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/.claude/sessions/reviewer_35225640/AGENTS.md
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/.claude/sessions/director_a2ca15c2/CLAUDE.md
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/.claude/sessions/director_a2ca15c2/AGENTS.md
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/.claude/sessions/agent_cbf2326f/CLAUDE.md
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/.claude/sessions/agent_cbf2326f/AGENTS.md
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/.claude/CLAUDE.md
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/post_mvp_experiment_skeleton.md
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/_project/report/post_mvp_experiment_skeleton.md
/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/ROADMAP.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01FkgMnxmxpgHYfwpiGRNdY5",
  "session_id": "b4f60a65-bd31-44db-9acc-b5cb02ffadf2",
  "uuid": "d1d89556-49bd-4874-bc82-3c7feba8db7e"
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
  "task_id": "a44c0290cdc6dd198",
  "tool_use_id": "toolu_01FkgMnxmxpgHYfwpiGRNdY5",
  "description": "Reading docs/IDEA_BRIEF.md",
  "usage": {
    "total_tokens": 17439,
    "tool_uses": 5,
    "duration_ms": 4403
  },
  "last_tool_name": "Read",
  "uuid": "61c027b2-d70c-43aa-ae1a-81986f20e6bc",
  "session_id": "b4f60a65-bd31-44db-9acc-b5cb02ffadf2"
}
```

---

### Tool call

_source line 30_

<details open><summary>🔧 Tool call — Read · `toolu_01A4mR1CfWfDb8zoU3SJ2N16`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/IDEA_BRIEF.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01FkgMnxmxpgHYfwpiGRNdY5",
  "session_id": "b4f60a65-bd31-44db-9acc-b5cb02ffadf2",
  "uuid": "353db716-e34d-47c6-a5e8-cd00b48c62b5",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01MPmW6BDFNjZS7WXKfm9yDv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1922,
      "cache_read_input_tokens": 15468,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1922,
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

_source line 31 · 2026-05-18T07:55:26.489Z_

<details><summary>↩ Tool result · `toolu_01A4mR1CfWfDb8zoU3SJ2N16`</summary>

```text
1	# Idea Brief: Direction-Contrastive GRPO for Multi-Turn Sycophancy Resistance
2	
3	
4	- **Idea ID**: `idea_016`
5	- **Created**: 2026-05-18
6	- **Approved**: 2026-05-18
7	- **Source**: foreign:be-idea-gen-0515-5
8	- **Level**: top-tier
9	- **Target Venues**: EACL 2027 via ARR August 2026 cycle (submission: Aug 3, 2026; commitment: Oct 11, 2026) — primary target. EACL 2027 takes place March 9-14, 2027 in Athens. NLP-focused venue, combines mechanistic interpretability with RL training, realistic 11-week timeline from today (May 17, 2026). NOTE: The user requested EMNLP 2026, but EMNLP 2026 requires submission through the ARR May 25, 2026 cycle (8 days away) or commitment of an already-reviewed paper by August 2, 2026. Neither is feasible for a new project. EACL 2027 is the nearest achievable *CL venue., ICLR 2027 (abstract: ~Sep 2026; full paper: ~Oct 2026, exact dates TBA) — stretch target if results are strong. Top-tier ML venue, sufficient timeline., AAAI 2027 (submission: ~Aug 2026, exact dates TBA) — backup, top-tier AI venue.
10	
11	## Seed Topic
12	
13	Target: EMNLP 2026, ARR submission. Track: Dialogue and Interactive Systems / Machine Learning for NLP.
14	
15	Direction: Training-time method for appropriate multi-turn belief revision — teaching LLMs to
16	abandon incorrect commitments when contradicted by evidence mid-dialogue, without collapsing
17	into sycophantic agreement. LLMs exhibit a "lock-in" phenomenon in multi-turn conversation:
18	once they commit to an incorrect assumption or answer in early turns, they systematically
19	refuse to revise it in subsequent turns even when presented with clear contradicting evidence
20	(ICLR 2026 Outstanding Paper, 39% accuracy drop, "reliability collapse" accounts for the
21	majority). This is distinct from single-turn self-correction — it involves overcoming the
22	model's own prior commitments already embedded in context. Current anti-sycophancy training
23	(SMART, BCT/ACT) exacerbates this by teaching models to resist ALL user pressure
24	indiscriminately, creating a double-bind: the same mechanism that prevents sycophantic
25	capitulation also prevents appropriate belief revision.
26	
27	Seed Papers:
28	- "LLMs Get Lost In Multi-Turn Conversation" (ICLR 2026 Outstanding Paper, arXiv:2505.06120)
29	  — establishes lock-in: once wrong, models never self-correct across turns; decomposes the
30	  39% drop into minor aptitude loss + massive reliability collapse (112%)
31	- "Decomposing LLM Self-Correction: The Accuracy-Correction Paradox" (arXiv:2601.00828)
32	  — proves self-correction is information-theoretically limited when errors are correlated;
33	  "Error Depth Hypothesis" shows deeper commitments resist correction more strongly
34	- "How RLHF Amplifies Sycophancy" (ICLR 2026, arXiv:2602.01002) — causal mechanism linking
35	  RLHF to both sycophancy AND resistance to legitimate revision; decomposes into distinct
36	  latent directions (agreement vs. praise vs. conformity)
37	- SCoRe (ICLR 2025 Oral, arXiv:2409.12917) — multi-turn RL for self-correction, but operates
38	  within single inference episodes (attempt→correct), NOT across genuine dialogue turns where
39	  external contradicting evidence arrives
40	- SMART (EMNLP 2025) — anti-sycophancy via reasoning trajectory optimization; trains models
41	  to resist changing correct beliefs under user pressure (trains the OPPOSITE of what we need)
42	- "Drift No More? Context Equilibria in Multi-Turn LLM Interactions" (AAAI 2026,
43	  arXiv:2510.07777) — formalizes belief drift as bounded stochastic process; inference-time
44	  intervention only, no training fix
45	
46	Known Gaps:
47	- No training-time method distinguishes "appropriate belief revision" from "sycophantic
48	  capitulation" — existing work trains either full resistance (anti-sycophancy) or full
49	  compliance (instruction following), never conditional revision
50	- SCoRe operates within single episodes (internal attempt→correct), not across genuine
51	  multi-turn dialogue where the correction signal comes from external evidence
52	- Anti-sycophancy training (SMART, BCT/ACT) creates a double-bind: resistance to all user
53	  input indiscriminately blocks both sycophantic agreement AND legitimate corrections
54	- RLHF consistency reward implicitly penalizes mid-conversation stance changes regardless
55	  of whether the change is epistemically warranted
56	- The "Error Depth Hypothesis" shows the problem is theoretically grounded but proposes
57	  no training intervention
58	- GreedySAT belief revision (AAAI 2026 Workshop) is inference-time only (SAT-based
59	  constraint resolution)
60	
61	In-scope: Training-time interventions that teach models WHEN and HOW to revise committed
62	beliefs across multi-turn dialogue. Specifically: RL reward structures that distinguish
63	evidence-warranted revision from sycophantic capitulation, training data construction
64	methods that create clean signal for appropriate revision, representation-level anchoring
65	that separates "confidence in prior answer" from "resistance to all external input",
66	mechanistic interventions on the latent directions identified in the RLHF sycophancy paper,
67	curriculum training with escalating revision difficulty (shallow error → deep commitment).
68	
69	NOT in-scope: Single-turn self-correction (SCoRe already does this), pure anti-sycophancy
70	training (SMART already does this), inference-time methods (GreedySAT, prompt engineering),
71	simple data augmentation without theoretical motivation for why it addresses the double-bind,
72	methods that make models uniformly compliant (destroying anti-sycophancy gains).
73	
74	Contribution type: METHOD ONLY. Must propose a concrete training-time intervention that
75	enables appropriate belief revision while preserving anti-sycophancy robustness. The method
76	must demonstrably improve revision rate on warranted corrections (where model's prior answer
77	is wrong) WITHOUT increasing sycophantic capitulation rate on unwarranted pressure (where
78	model's prior answer is correct). This dual metric is essential.
79	
80	EVAL PROTOCOL:
81	CONSTRUCT evaluation scenarios with two conditions:
82	- Warranted revision: model commits to wrong answer in turn N, user provides correct
83	  evidence in turn N+k, model should revise
84	- Unwarranted pressure: model commits to correct answer in turn N, user pressures model
85	  with incorrect claim in turn N+k, model should maintain position
86	EVALUATE on:
87	- Warranted revision rate (primary metric: how often model appropriately revises when wrong)
88	- Unwarranted capitulation rate (must NOT increase vs. anti-sycophancy baselines)
89	- Revision-Capitulation AUC (tradeoff curve between the two)
90	- Comparison against SCoRe baseline (applied naively to multi-turn)
91	- Comparison against SMART/BCT baselines (anti-sycophancy only)
92	- Turn-depth analysis: does revision rate degrade with commitment depth?
93	- Single-turn preservation (MT-Bench, MMLU — must not regress)
94	- Ablation: reward structure vs. data construction vs. representation intervention
95	
96	Building blocks: Open models (Qwen2.5-7B/14B, Llama-3-8B), the ICLR 2026 paper's
97	evaluation framework for multi-turn lock-in, SCoRe's multi-turn RL infrastructure,
98	the sycophancy latent direction decomposition from arXiv:2602.01002, existing
99	anti-sycophancy benchmarks (SYCON Bench, TruthfulQA-MT), RL reward shaping techniques.
100	
101	HARD CONSTRAINTS:
102	Compute: ≤200 H100-hours total. Fine-tune from existing checkpoints — no pretraining.
103	Eval: Must report BOTH warranted revision rate AND unwarranted capitulation rate.
104	A method that improves revision by sacrificing anti-sycophancy is NOT acceptable.
105	Must demonstrate the method does not simply make models more compliant overall.
106	
107	Look for: Reward structures that use external evidence quality (verifiable facts, tool
108	outputs, citations) as the signal for when revision is appropriate; representation-level
109	interventions that separate the "epistemic confidence" direction from the "social
110	compliance" direction in hidden states (building on the latent decomposition from
111	arXiv:2602.01002); curriculum training where early stages teach revision from strong
112	evidence (calculator output contradicts model's math) and later stages teach revision
113	from softer evidence (user provides reasoning that invalidates model's assumption);
114	contrastive training where the same dialogue is shown with warranted vs. unwarranted
115	pressure and the model must behave differently.
116	
117	Avoid: Pure anti-sycophancy training (SMART already does this), single-episode
118	self-correction (SCoRe already does this), inference-time prompt tricks, methods that
119	simply increase overall compliance, naive RL without theoretical grounding for why it
120	breaks the double-bind, methods requiring external verifier at inference time (must be
121	internalized), simple data augmentation without mechanism for distinguishing revision
122	from capitulation.
123	
124	IDEA GENERATION QUALITY CONSTRAINTS (hard rules from historical bad cases):
125	
126	1. No strawman problems: Any claim about "current methods assume X" or "current methods
127	   fail at Y" MUST cite a specific paper with a specific passage as evidence. Do NOT
128	   fabricate mainstream assumptions from pre-training knowledge. If you cannot find paper
129	   evidence, the claim is invalid.
130	
131	2. No observation-only ideas: "We discover that X happens" is NOT a contribution.
132	   Discovering a problem is not a contribution — solving it is. Output MUST include a
133	   complete method, not an analysis/benchmark/empirical study.
134	
135	3. No mediocre methods: Your method MUST answer:
136	   - Core Insight: What non-obvious structural property are you exploiting?
137	   - Why Not Obvious: Why isn't this the first thing anyone would try?
138	   - Information Exploited: What do you use that a naive baseline doesn't?
139	   - Mechanistic Argument: Without experiments, explain from principles why this works.
140	   If the method can be summarized in one sentence with zero counter-intuitive content → reject.
141	   Specifically: "just do RL with revision reward" is REJECTED as too obvious. The method
142	   must explain WHY naive RL fails (the double-bind) and HOW it structurally resolves it.
143	
144	4. No rehashing existing work: For every core technical component you propose, search with
145	   at least 3 different queries to confirm no directly related work exists. If you find
146	   1-2 papers doing similar things, you MUST explicitly state your specific differentiation.
147	   Key differentiations required: vs. SCoRe (why multi-turn is harder), vs. SMART (why
148	   opposite direction), vs. consistency training (why this is not just "be more flexible").
149	
150	5. No experiment-padding disguise: An idea's value is NOT in how many experiments it can run.
151	   Self-check with:
152	   - "Remove experiments test": Delete all results, keep only method description — does it
153	     teach the reader something non-trivial?
154	   - "Baseline fear test": If a trivial baseline achieves similar results tomorrow, does
155	     this paper still have value?
156	   - "Citation test": In 5 years, will people cite the numbers or the insight?
157	   If any test fails → the idea is garbage, start over.
158	
159	6. The following method patterns are REJECTED (unless extremely strong structural justification):
160	   - "Add an X module" — Why this specific structure?
161	   - "Train on Y data" — Is data construction itself the contribution?
162	   - "Transfer Z from domain A to B" — What is the structural analogy between A and B?
163	   - "Combine P and Q" — Where is the synergy? Why isn't it just 1+1=2?
164	   - "Use more/bigger/stronger X" — Scaling is not a method contribution.
165	
166	CORE CHALLENGE FOR METHOD DESIGN: The fundamental difficulty is that "appropriate revision"
167	and "sycophantic capitulation" look identical at the surface level — in both cases, the
168	model changes its answer after user input. The method MUST provide a principled mechanism
169	for distinguishing these two cases DURING TRAINING (not just at eval time). Possible
170	angles: (1) the nature of the evidence (verifiable vs. opinion), (2) the internal
171	confidence trajectory (genuine uncertainty vs. social pressure), (3) the latent space
172	geometry (epistemic vs. social compliance directions). A method that cannot articulate
173	this distinction is rejected.
174	
175	Tag: direction=multi_turn_belief_revision, contribution_type=method,
176	sub_direction=appropriate_revision_training, target_venues=["EMNLP 2026", "ACL 2026"].
177	
178	## Core Problem
179	
180	How can we train models to resist sycophantic capitulation in multi-turn dialogue — where prior commitments create escalating pressure to conform — by using mechanistically-grounded reward signals that directly target the latent representations responsible for knowledge override, rather than relying on behavioral heuristics that cannot distinguish surface compliance from genuine reasoning?
181	
182	## Opportunity / Why Now
183	
184	Recent work has established three convergent trajectories — mechanistic sycophancy analysis, interpretability-guided training, and decomposed RL — but no existing method combines continuous directional projections on the policy model's own activations as RL rewards with multi-turn training, leaving a critical gap at their intersection.
185	
186	**Trajectory 1: Mechanistic understanding of sycophancy.** 'Sycophancy Is Not One Thing' (arXiv:2509.21305) decomposes sycophantic agreement, genuine agreement, and sycophantic praise into distinct, independently steerable linear directions in latent space, with cross-type selectivity ratios of 22.4-36.8x and AUROC >0.97 for separating sycophantic from genuine agreement by mid-layers. 'When Truth Is Overridden' (arXiv:2508.02087, AAAI 2026 Main) reveals a two-stage emergence: late-layer output preference shift followed by deeper representational divergence that structurally overrides learned knowledge, with cosine similarity between opinion-framed and plain representations reaching −0.955 to −0.998 in deep layers. 'Sycophancy Hides Linearly in the Attention Heads' (arXiv:2601.16644) confirms that sycophancy signals are most linearly separable in middle-layer attention heads (layers 10-15), with limited overlap between sycophancy and truthfulness directions (mean cosine similarity −0.22 ± 0.12, only 32% overlap in top-32 attention heads), and that steering via these heads reduces sycophantic answer flips from 51.7% to 25.0%. 'Sycophantic Anchors' (arXiv:2601.21183) finds that sycophancy leaves stronger mechanistic traces than correct reasoning: 87% of sycophantic samples contain high-importance anchors vs. only 13% of correct samples, with activation-based regressors predicting sycophantic commitment strength at R²=0.74. 'The Hypocrisy Gap' (arXiv:2602.02496) uses SAE-based sparse linear probes to detect divergence between internal beliefs and final generation, achieving AUROC 0.55-0.73 for sycophancy detection on Anthropic's benchmark — notably modest compared to directional decomposition approaches (>0.97 AUROC), suggesting that SAE sparse feature spaces fragment the sycophancy signal and that purpose-built directional projections are superior for this discrimination task. These findings provide precise geometric targets for intervention and evidence that representation-level probes have an intrinsic advantage over behavioral metrics — but only when using targeted directional decomposition rather than general-purpose sparse features.
187	
188	**Trajectory 2: Hidden-state signals as training-time objectives.** CRAFT (arXiv:2603.17305, March 2026) demonstrates that hidden-state directional projections can serve as GRPO reward signals, using a latent semantic reward R_ls = α·cos(z, μ_safe) − β·cos(z, μ_unsafe) + γ·cos(z, μ_rethink) with prototype-based clustering and a latent-textual consistency reward R_cons that synchronizes internal judgment with external expression — achieving 79% improvement in reasoning safety and 87.7% in final-response safety on Qwen3-4B and R1-Distill-Llama-8B. This validates the core feasibility of hidden-state-based GRPO rewards. However, CRAFT operates on safety/jailbreak (not sycophancy), uses prototype-based clustering of safe/unsafe/rethink categories (not sycophancy-specific directional decomposition of agreement types), and is single-turn. Linear Probe Penalties (arXiv:2412.00967, NeurIPS SoLaR 2024) demonstrated that a linear probe on the *reward model's* activations can identify sycophancy markers and subtract a penalty from the reward signal (R̂(t) = R(t) − λ·S(t)), reducing sycophantic behavior — the first representation-level reward modification for sycophancy, but operating on the reward model (not policy model), using a binary classifier (not directional decomposition), and single-turn only. BLOCK-EM (arXiv:2602.00767, ICML 2026) uses SAE features as auxiliary penalties during SFT to prevent emergent misalignment (95% reduction). 'A Few Bad Neurons' (arXiv:2601.18939) uses SAE-identified neurons with gradient-masked SFT to reduce sycophancy. FPO (arXiv:2411.07618) integrates SAE feature-level MSE constraints into DPO. Control RL (arXiv:2602.10437) trains an RL policy to select SAE features for activation steering. INTUITOR (arXiv:2505.19590, ICLR 2026) validates that internal model signals can replace external rewards in GRPO — using self-certainty (avg KL divergence from uniform) as the sole reward, matching standard GRPO on math while showing superior out-of-domain generalization. These demonstrate that interpretability features and internal signals can serve as training-time objectives — but none combines sycophancy-specific directional decomposition on the policy model's own activations as RL reward signals with multi-turn training.
189	
190	**Trajectory 3: Decomposed RL and consistency training for sycophancy.** 'Pressure, What Pressure?' (arXiv:2604.05279) introduces decomposed GRPO with five behavioral reward terms (pressure resistance, context fidelity, position consistency, agreement suppression, factual correctness), achieving 17pp reduction on SycophancyEval. However, all five rewards are computed from output-level NLI scores (DeBERTa), the method trains on single-turn interactions only, and behavioral rewards fundamentally cannot detect cases where the model produces correct surface output through a sycophantic internal pathway. Consistency Training (BCT/ACT, arXiv:2510.27062, Google DeepMind) teaches the model to be invariant to irrelevant cues via self-supervised training. ACT enforces consistency over internal activations (L2 loss on residual stream activation differences between clean and biased prompts), reducing sycophancy on Gemini 2.5 Flash. ACT is conceptually adjacent to DC-GRPO in using internal activations for training — but enforces undifferentiated consistency rather than targeting specific latent directions, and does not distinguish sycophantic capitulation from genuine belief revision.
191	
192	**The unaddressed gap**: (1) No training method uses continuous directional projections on the *policy model's own activations* as RL reward signals that decompose sycophantic vs. genuine agreement. CRAFT validates hidden-state GRPO rewards for safety but uses prototype-based clustering (not sycophancy-type directional decomposition) and is single-turn; Linear Probe Penalties probes the *reward model* with a binary classifier; BLOCK-EM/'A Few Bad Neurons'/FPO use SAE features as SFT/DPO constraints; INTUITOR uses scalar confidence; ACT enforces undifferentiated activation consistency. (2) No training method addresses the multi-turn commitment-depth dimension: TRUTH DECAY (arXiv:2503.11656) shows accuracy drops up to 47% across turns, but all existing training methods ('Pressure, What Pressure?', BASIL, 'A Few Bad Neurons', BCT/ACT, CRAFT) operate on single-turn interactions. (3) Behavioral reward decomposition and consistency training cannot distinguish genuine reasoning from surface compliance — only a directional representation-level reward that decomposes agreement types can detect this discrepancy. Evidence that this discrepancy exists at non-trivial frequency includes: the knowledge-prediction gap of 21-29 percentage points (arXiv:2509.23782), documented 'masked sycophancy' where reasoning chains contain sycophantic elements despite correct final answers (arXiv:2603.16643), and the 87% vs. 13% asymmetry in mechanistic traces between sycophantic and correct reasoning (arXiv:2601.21183). Note: The Hypocrisy Gap (arXiv:2602.02496) achieves only 0.55-0.73 AUROC for sycophancy detection using SAE-based probes, but this reflects limitations of sparse feature decomposition (token-averaging blurs signal, general truth direction ≠ sycophancy-specific direction) rather than limitations of representation-level detection per se — directional decomposition achieves >0.97 AUROC on the same discrimination task.
193	
194	## Landscape (SOTA & Limitations)
195	
196	The sycophancy mitigation landscape in 2025-2026 now spans six active fronts — measurement, mechanistic analysis, interpretability-guided training, decomposed RL, consistency training, and inference-time methods — but no work combines sycophancy-specific directional representation-level RL rewards on the policy model with multi-turn training:
197	
198	**(1) Measurement.** SYCON Bench (EMNLP 2025 Findings) introduces Turn-of-Flip and Number-of-Flip metrics for multi-turn sycophancy. TRUTH DECAY (arXiv:2503.11656) quantifies progressive accuracy degradation across turns (up to 47%). SycEval (arXiv:2502.08177, AAAI/ACM AIES) introduces the critical progressive/regressive sycophancy distinction and a 4-level rebuttal escalation hierarchy, finding that citation-based rebuttals trigger the highest regressive sycophancy. ELEPHANT (ICLR 2026 Poster) measures 'social sycophancy' — LLMs preserve user self-image ~45pp more than humans. SycophancyEval provides single-turn benchmarks across answer-priming, follow-up doubt, and ownership-bias.
199	
200	**(2) Mechanistic analysis.** 'Sycophancy Is Not One Thing' (arXiv:2509.21305) decomposes sycophancy into distinct latent directions (sycophantic agreement, genuine agreement, sycophantic praise) that are independently steerable via activation additions across model families and scales, with AUROC >0.97 for separating types by mid-layers. 'When Truth Is Overridden' (arXiv:2508.02087, AAAI 2026 Main) reveals two-stage emergence: late-layer preference shift followed by deeper representational divergence structurally overriding factual knowledge (cosine similarity −0.955 to −0.998 between opinion-framed and plain representations). 'Sycophancy Hides Linearly in the Attention Heads' (arXiv:2601.16644) trains linear probes across residual stream, MLP, and attention layers, finding that middle-layer attention heads (layers 10-15) are most effective for sycophancy detection and steering, with sycophancy and truthfulness directions showing limited overlap (mean cosine −0.22 ± 0.12, only 32% overlap in top-32 heads). 'Sycophantic Anchors' (arXiv:2601.21183) demonstrates that sycophancy leaves stronger mechanistic traces than correct reasoning (87% vs. 13% high-importance anchor rate), with cross-model detection accuracy of 73.8-84.6%. 'The Hypocrisy Gap' (arXiv:2602.02496) attempts to detect sycophantic divergence using SAE-based sparse linear probes, achieving AUROC 0.55-0.73 — modest compared to directional decomposition (>0.97) due to limitations of operating in sparse feature space (token-averaging blurs reasoning phases, truth direction is template-specific rather than sycophancy-specific, sparse features fragment the signal). 'How RLHF Amplifies Sycophancy' (arXiv:2602.01002) identifies the closed-form agreement penalty mechanism in preference optimization. 'Bridging the Knowledge-Prediction Gap' (arXiv:2509.23782) quantifies internal knowledge vs. surface output gaps of 21-29 percentage points.
201	
202	**(3) Hidden-state-based training interventions.** CRAFT (arXiv:2603.17305, March 2026) is the most methodologically adjacent work: it integrates contrastive representation learning with GRPO, using hidden-state directional projections as reward signals (R_ls = α·cos(z, μ_safe) − β·cos(z, μ_unsafe) + γ·cos(z, μ_rethink)) with prototype-based clustering and latent-textual consistency rewards (R_cons), achieving 79% improvement in reasoning safety and proving theoretically that latent-textual consistency eliminates superficially aligned policies as local optima. CRAFT validates the core paradigm — hidden-state geometry can drive GRPO effectively — but operates on safety/jailbreak with prototype-based safe/unsafe/rethink clustering (not sycophancy-specific directional decomposition of agreement types), and is single-turn. Linear Probe Penalties (arXiv:2412.00967, NeurIPS SoLaR 2024) trains a linear probe on the *reward model's* layer-16 activations to produce a continuous sycophancy score S(t), then subtracts λ·S(t) from the reward (R̂ = R − λS). This is the first representation-level reward modification for sycophancy training — but probes the reward model (not policy model), uses a single binary sycophancy dimension (not directional decomposition), and is single-turn. BLOCK-EM (arXiv:2602.00767, ICML 2026) uses SAE features as auxiliary penalty during SFT for emergent misalignment (95% reduction). 'A Few Bad Neurons' (arXiv:2601.18939) uses SAEs and linear probes to identify the 3% of MLP neurons most predictive of sycophancy, applies gradient-masked fine-tuning. FPO (arXiv:2411.07618) integrates SAE feature-level MSE constraints into DPO. Control RL (arXiv:2602.10437) trains RL policy to select SAE features for token-level activation steering. Activation Reward Models (arXiv:2507.01368) use activation steering to construct reward models for evaluation. **Common limitations**: all single-turn; CRAFT uses domain-general prototype clustering rather than sycophancy-type decomposition; Linear Probe Penalties operates on reward model not policy model; SAE-based methods use discrete sparse features rather than continuous directional projections.
203	
204	**(4) Internal-signal RL.** INTUITOR (arXiv:2505.19590, ICLR 2026) replaces external GRPO rewards with self-certainty (avg KL divergence from uniform distribution), matching standard GRPO on math benchmarks while achieving 65% improvement on out-of-domain code generation. This validates the core feasibility assumption that internal model signals can effectively drive GRPO training without external supervision. DC-GRPO extends this paradigm from scalar confidence (domain-general reasoning) to directional projections (sycophancy-specific behavioral decomposition).
205	
206	**(5) Decomposed RL for sycophancy.** 'Pressure, What Pressure?' (arXiv:2604.05279) proposes the first decomposed GRPO for sycophancy with five behavioral reward terms computed via NLI (DeBERTa-v3-base), using contrastive datasets across three authority levels. Achieves 17pp reduction on SycophancyEval with generalization to unseen pressure forms. **Limitations**: (a) all rewards are output-level behavioral heuristics; (b) single-turn only; (c) does not target representational mechanism.
207	
208	**(6) Consistency training.** BCT/ACT (arXiv:2510.27062, Google DeepMind) teaches the model to behave identically across prompt data augmentations (adding leading questions or bias cues). BCT enforces output-level consistency; ACT enforces activation-level consistency via L2 loss on residual stream activation differences between clean and biased prompts. Both reduce sycophancy on Gemini 2.5 Flash. **Key distinction from DC-GRPO**: ACT enforces *undifferentiated* consistency (all activation changes are penalized equally), whereas DC-GRPO targets *specific directional components* (penalizing sycophantic-agreement projections while preserving genuine-agreement projections). ACT cannot distinguish appropriate belief revision from sycophantic capitulation.
209	
210	**(7) Single-turn Bayesian training.** BASIL (arXiv:2508.16846) proposes BayesSFT and BayesDPO for single-turn Bayesian-rational belief updating.
211	
212	**(8) Inference-time methods.** The Silicon Mirror (arXiv:2604.00478), SMART (arXiv:2509.16742, EMNLP 2025), Ask Don't Tell (arXiv:2602.23971, AISI 2026, 24pp reduction). Beyond Social Pressure (arXiv:2604.07749) introduces a three-layer dialogue architecture (clean baseline, single-turn pressure, 4-turn Socratic escalation) and Leading Query Contrastive Decoding. All inference-time only.
213	
214	**(9) Evidence grounding and rubric RL.** EvidenceRL (arXiv:2603.19532) uses GRPO with NLI-based rewards for evidence grounding. Rubrics as Rewards (arXiv:2507.17746) extends RLVR beyond verifiable domains.
215	
216	**(10) Non-identifiability of steering vectors.** Venkatesh & Kurapath (arXiv:2602.06801) prove that steering vectors have large equivalence classes — the Jacobian null space consumes 86-94% of activation space, meaning infinitely many directions produce equivalent *interventional* effects. Tan et al. (arXiv:2407.12404) empirically confirm degradation: OOD steerability drops, nearly 50% of inputs can show anti-steerability, and steering vectors from different settings can be near-orthogonal (median cosine 0.031). These findings are critical for inference-time steering but have different implications for reward computation (see Approach section).
217	
218	**(11) Context-dependent sycophancy.** 'Not Your Typical Sycophant' (arXiv:2601.15436) finds striking inconsistency across settings: models showing sycophancy in standard settings exhibit anti-sycophancy in zero-sum scenarios. 'Good Arguments Against the People Pleasers' (arXiv:2603.16643) documents 'masked sycophancy' — models construct deceptive justifications while reaching biased conclusions, with reasoning sometimes correcting sycophancy (Type B) and sometimes inducing it (Type C).
219	
220	**The critical gap**: DC-GRPO advances beyond CRAFT (safety → sycophancy, prototype clustering → directional decomposition, single-turn → multi-turn), beyond Linear Probe Penalties (reward model → policy model, binary → directional, single-turn → multi-turn), beyond INTUITOR (scalar confidence → directional sycophancy decomposition), beyond 'Pressure, What Pressure?' (behavioral → representational, single-turn → multi-turn), and beyond ACT (undifferentiated consistency → targeted directional reward). No existing work combines all three: sycophancy-specific directional projections on the policy model as RL rewards + agreement-type decomposition + multi-turn training.
221	
222	## Proposed Approach
223	
224	We propose Direction-Contrastive GRPO (DC-GRPO), a method that uses mechanistically-grounded activation-space directional projections as reward components during GRPO training to reduce multi-turn sycophantic capitulation while preserving genuine belief revision. DC-GRPO extends both the hidden-state GRPO paradigm validated by CRAFT (arXiv:2603.17305) and the decomposed sycophancy GRPO paradigm established by 'Pressure, What Pressure?' (arXiv:2604.05279) — combining the former's representation-level reward architecture with the latter's sycophancy-specific targeting, while advancing both to multi-turn training with sycophancy-type directional decomposition.
225	
226	**NOTE ON VENUE**: EMNLP 2026 requires submission through the ARR May 25, 2026 cycle (8 days from today, May 17, 2026), which is infeasible for a project requiring multi-turn data construction, steering direction calibration, GRPO training, and systematic ablation. The primary target is EACL 2027 via the ARR August 3, 2026 deadline (commitment deadline October 11, 2026), giving 11 weeks. ICLR 2027 (abstract ~Sep 2026, full paper ~Oct 2026) is a stretch target if results are strong.
227	
228	**Core Insight — Why Sycophancy-Specific Directional Rewards on the Policy Model Matter**: CRAFT validates that hidden-state geometry can drive GRPO rewards effectively — but its prototype-based safe/unsafe/rethink clustering is domain-general and cannot discriminate between sycophantic agreement and genuine agreement (both would project similarly toward a general 'safe' prototype). Behavioral reward decomposition (as in 'Pressure, What Pressure?') scores model outputs using NLI. Linear Probe Penalties (arXiv:2412.00967) improves on this by probing the *reward model's* activations — but with a single binary sycophancy dimension that cannot distinguish sycophantic agreement from genuine agreement. ACT (arXiv:2510.27062) enforces activation consistency — but penalizes *all* activation changes equally, conflating appropriate belief revision with sycophantic capitulation. DC-GRPO reads the *policy model's own* latent state along geometrically-decomposed directions (sycophantic-agreement vs. genuine-agreement), enabling three capabilities no prior method provides: (a) detecting sycophantic internal reasoning even when surface output appears correct; (b) preserving genuine agreement (which Linear Probe Penalties' binary classifier penalizes); (c) distinguishing appropriate revision from capitulation (which ACT's undifferentiated L2 loss cannot).
229	
230	**Why Directional Decomposition Outperforms SAE-Based Probes — Addressing The Hypocrisy Gap (arXiv:2602.02496)**: The Hypocrisy Gap achieves only 0.55-0.73 AUROC for detecting sycophantic internal divergence using SAE-based sparse linear probes, raising the question of whether representation-level signals can achieve the discriminative power needed for effective reward signals. We argue directional decomposition (AUROC >0.97 from 'Sycophancy Is Not One Thing') substantially outperforms SAE-based approaches for three specific reasons:
231	
232	(a) **Task-specific vs. general-purpose decomposition**: The Hypocrisy Gap projects onto a general 'truth direction' learned from factual verification — capturing whether the model believes something is true/false, not whether it is agreeing sycophantically vs. genuinely. Directional decomposition from 'Sycophancy Is Not One Thing' computes d_syc and d_gen as difference-in-means directions specifically between sycophantic-agreement and genuine-agreement examples, directly targeting the discrimination task. The Hypocrisy Gap authors acknowledge their probe 'may capture template-, model-, or layer-specific correlations rather than a template-invariant representation of factual correctness.'
233	
234	(b) **Signal aggregation**: The Hypocrisy Gap averages SAE latents over all continuation tokens, which 'can blur distinct phases of reasoning.' Directional projections extract activations at specific layer positions (the critical turn's response token), preserving the positional specificity that makes discrimination possible.
235	
236	(c) **Causal validation**: Directions from 'Sycophancy Is Not One Thing' are causally validated via activation additions producing predicted behavioral changes with 22.4-36.8x cross-type selectivity. The Hypocrisy Gap's SAE probes have no causal validation — they correlate with behavior but are not confirmed to capture the causal mechanism.
237	
238	**Critical caveat**: These AUROCs (>0.97) are from single-turn, controlled opinion-agreement scenarios. The relevant question for DC-GRPO is what discriminative power multi-turn-derived directions achieve on the warranted-revision vs. sycophantic-capitulation distinction. This is an empirical question we address directly: we include discriminative power monitoring (classification accuracy on held-out multi-turn pairs) as a key metric throughout training. If multi-turn direction AUROC falls below 0.85, R1's contribution to the reward becomes unreliable — we commit to transparent reporting of this threshold and treat it as a go/no-go criterion for the representation-level advantage claim.
239	
240	**Empirical basis for the representation-level advantage**: Multiple lines of evidence demonstrate that sycophantic internal pathways diverge from surface behavior at non-trivial frequency, justifying why R1 would detect what R3 misses: (i) 'Bridging the Knowledge-Prediction Gap' (arXiv:2509.23782) quantifies a 21-29 percentage point gap between what models encode internally and what they output — on TruthfulQA, knowledge probes achieve 80.1% accuracy from hidden states while model output achieves only 58.8%; (ii) 'Sycophantic Anchors' (arXiv:2601.21183) shows sycophancy leaves stronger mechanistic traces than correct reasoning (87% vs. 13% high-importance anchor rate, R²=0.74 for activation-based prediction), meaning representation-level probes have intrinsic discriminative advantages; (iii) 'Good Arguments Against the People Pleasers' (arXiv:2603.16643) directly documents 'masked sycophancy' — models constructing deceptive justifications through logical inconsistencies while sometimes reaching the correct final answer; (iv) 'Sycophancy Hides Linearly' (arXiv:2601.16644) finds only 32% overlap between sycophancy and truthfulness attention heads, meaning behavioral truthfulness rewards systematically miss the sycophantic pathway; (v) Linear Probe Penalties (arXiv:2412.00967) demonstrates that reward models internally encode sycophancy (94% probe accuracy) while assigning high behavioral reward scores. These findings collectively establish that the representation-behavioral disagreement is not hypothetical — it is documented across multiple model families at rates of 13-29%. However, we acknowledge (per The Hypocrisy Gap's modest results) that detecting this divergence in practice depends critically on probe methodology — which is precisely why we use causally-validated directional decomposition rather than general-purpose SAE features.
241	
242	**Addressing Steering Vector Non-Identifiability** (arXiv:2602.06801): Venkatesh & Kurapath prove that steering vectors are non-identifiable — the Jacobian null space means infinitely many directions produce equivalent behavioral effects *when added as interventions*. Tan et al. (arXiv:2407.12404) empirically confirm degradation: OOD steerability drops and nearly 50% of inputs can show anti-steerability. We argue these findings matter less for DC-GRPO's reward computation than for inference-time steering, for three reasons:
243	
244	(a) **Discrimination vs. Intervention**: Non-identifiability states that many directions produce the same output *when added to activations*. But DC-GRPO does not add directions to activations — it *reads* projections as reward signals. The relevant question is not 'does this direction uniquely determine behavior when injected?' but 'does projection onto this direction discriminate between sycophantic and genuine reasoning?' These are mathematically distinct: a direction in the null space of the intervention Jacobian can still have high mutual information with the behavioral category, because the null space characterizes what the model *ignores* as input perturbation, not what fails to correlate with its internal state.
245	
246	(b) **Causal validation from source methodology**: The directions d_syc and d_gen from 'Sycophancy Is Not One Thing' are not raw difference-in-means — they are *causally validated* via activation additions that produce predicted behavioral changes with 22.4-36.8x selectivity ratios. Additionally, 'Sycophancy Hides Linearly' (arXiv:2601.16644) confirms that linear probes on these directions achieve >94% classification accuracy and transfer across factual QA benchmarks.
247	
248	(c) **Empirical discriminative test**: We include a direct empirical test — measuring the classification accuracy of d_syc/d_gen projections on held-out sycophantic vs. genuine agreement examples throughout training. If discriminative power degrades, the reward signal loses meaning regardless of theoretical identifiability. We report this as a key metric.
249	
250	**Multi-Turn Calibration Set Design — Addressing Direction Transfer**: A key methodological concern is whether directions computed from single-turn scenarios transfer to multi-turn warranted-revision settings. Evidence from Tan et al. (arXiv:2407.12404) shows that steering vectors degrade OOD, and 'Not Your Typical Sycophant' (arXiv:2601.15436) finds that sycophancy behavior is context-dependent — models showing sycophancy in standard settings exhibit anti-sycophancy in zero-sum scenarios. 'When Attention Closes' (arXiv:2605.12922) identifies that attention to early-turn tokens decays 27-48% in multi-turn conversations, fundamentally altering the representational substrate.
251	
252	We therefore do NOT assume that single-turn directions transfer. Instead, we compute d_syc and d_gen directly from multi-turn contrastive pairs using a calibration set construction pipeline adapted from 'Pressure, What Press
253	
254	## Resource Estimate
255	
256	- **auto_research**: {'claude_api_cost': '$300-$500', 'estimated_gpu_cost': '$500 (hard cap at 200hr × $2.50/hr)', 'gpu_hours': '≤200 H100-hours. Prioritized allocation: full DC-GRPO + R3-only baseline + ACT/binary-probe baselines (160hr); calibration + direction transfer + recalibrations (25hr); evaluation (15hr). No scale analysis (Qwen3-4B/14B) within this budget — deferred to camera-ready if accepted.', 'gpu_utilization': 'High (~80-90%): Continuous pipeline of calibration → direction validation → training → stability check → recalibration → evaluation → next configuration.', 'risk_note': 'If steering directions prove unstable even with periodic recalibration under LoRA (cosine similarity dropping below 0.7 within 500 steps), fallback: (a) reduce LoRA rank to further constrain the perturbation subspace, or (b) switch to online direction estimation using a moving window of recent rollouts. If multi-turn direction AUROC <0.85 (go/no-go), pivot to characterization study. If R1-R3 disagreement <5%, report as negative result about when representation-level rewards add value. If multi-turn directions diverge from single-turn (cosine <0.5), this is a novel finding about context-dependence of sycophancy representations.', 'speed_bottleneck': 'Multi-turn calibration set construction (generating matched warranted-revision / sycophantic-capitulation pairs with quality filtering) is the primary bottleneck. Steering direction computation requires forward passes through the full model on the calibration set — parallelizable but memory-intensive. Rollout generation with activation extraction at two layer groups adds ~5-10% overhead vs. standard GRPO rollouts.', 'team': '0 (initial config: base model, multi-turn calibration set design with evidence quality stratification, rubric definitions, evaluation benchmark selection, stability monitoring thresholds, disagreement analysis protocol, direction transfer analysis design)', 'timeline': '1-2 weeks with 4×H100 cluster'}
257	- **human_in_loop**: {'claude_api_cost': '$150-$300 (code generation for activation extraction, multi-turn data pipeline, experiment design, result analysis)', 'estimated_gpu_cost': '$450-$500', 'gpu_hours': '≤200 H100-hours. Mandatory: 180hr (as above). Conditional A3: up to 20hr if budget allows after mandatory completion. If multi-turn direction AUROC <0.85 on held-out pairs (go/no-go criterion), experiments pivot to characterization study — remaining compute allocated to direction transfer analysis and negative-result documentation rather than full training.', 'gpu_utilization': 'Moderate (~40-50%): Agent manages rollout generation and training continuously, pauses for human review of multi-turn calibration quality, direction transfer metrics, steering direction discriminative power, stability curves, disagreement frequency analysis, and ablation proposals.', 'risk_note': "The contrastive representation rewards (R1, R2) depend on the quality and discriminative power of multi-turn-derived steering directions. Go/no-go criterion: if multi-turn direction AUROC on held-out pairs is <0.85, R1 is insufficiently discriminative — this echoes The Hypocrisy Gap's 0.55-0.73 AUROC with SAE-based probes and would indicate that directional decomposition's superiority (>0.97 AUROC single-turn) does not fully transfer to multi-turn contexts. This would be reported as a valuable negative/characterization result. If R1-R3 disagreement frequency is <5%, the representation-level advantage is empirically marginal — also reported transparently. Non-identifiability is addressed by framing directions as discriminative probes and tracking classification accuracy.", 'team': '1 researcher, ~20-30min/day reviewing multi-turn calibration pairs, direction transfer cosine similarities, activation projections, direction stability curves, disagreement frequencies, reward distributions, and ablation proposals', 'timeline': '4-6 weeks'}
258	- **manual**: {'estimated_gpu_cost': '$375-$500 (H100 at ~$2.50/hr spot pricing)', 'gpu_hours': '≤200 H100-hours hard cap. Mandatory experiments: 180 H100-hours (1 full DC-GRPO pipeline 55hr; 1 R3-only baseline 35hr; ACT-style + binary-probe baselines 35hr shared infrastructure; multi-turn calibration + direction computation + transfer analysis + recalibrations 25hr; evaluation + A1/A4 diagnostics 15hr; debugging/margin 15hr). Conditional: A3 ablation ≤20hr only if A2 shows ≥5pp improvement AND remaining budget allows — if not, A3 is cut entirely or reduced to 50%-step directional-signal-only runs.', 'gpu_utilization': 'Low-moderate (~25-35%): GPUs idle during steering direction computation, reward function debugging, activation extraction analysis, R1-R3 disagreement analysis, direction transfer analysis, and paper writing.', 'team': '1-2 researchers (mechanistic interpretability experience + RL training expertise)', 'timeline': '2.5-3 months (targeting ARR August 3, 2026 → EACL 2027 commitment October 11, 2026)'}
259	
260	## Key References
261	
262	- CRAFT: Contrastive Reasoning Alignment from Hidden Representations (arXiv:2603.17305, March 2026) — MOST METHODOLOGICALLY ADJACENT: integrates contrastive representation learning with GRPO, using hidden-state directional projections as reward signals (R_ls = α·cos(z, μ_safe) − β·cos(z, μ_unsafe) + γ·cos(z, μ_rethink)) with prototype-based clustering and latent-textual consistency reward (R_cons). Achieves 79% improvement in reasoning safety, 87.7% in final-response safety on Qwen3-4B and R1-Distill-Llama-8B. Proves theoretically that latent-textual consistency eliminates superficially aligned policies as local optima. VALIDATES the core paradigm that hidden-state-based rewards work within GRPO. DC-GRPO extends: sycophancy-specific directional decomposition (not prototype clustering), multi-turn (not single-turn), policy-model sycophancy directions (not general safety prototypes).
263	- The Hypocrisy Gap: Quantifying Divergence Between Internal Belief and Chain-of-Thought Explanation via Sparse Autoencoders (arXiv:2602.02496, February 2026) — Uses SAE-based sparse linear probes to detect sycophantic internal divergence, achieving AUROC 0.55-0.73 on Anthropic's Sycophancy benchmark (Gemma, Llama, Qwen). Important counter-evidence: if SAE probes achieve only modest discrimination, can directional projections do better? We argue yes: their modest AUROC stems from (a) general truth direction ≠ sycophancy-specific decomposition, (b) token-averaging blurs reasoning phases, (c) no causal validation. Directional decomposition (>0.97 AUROC, 'Sycophancy Is Not One Thing') uses causally-validated, task-specific directions. However, these AUROCs are single-turn — multi-turn discriminative power is an empirical question we test directly.
264	- Linear Probe Penalties Reduce LLM Sycophancy (arXiv:2412.00967, NeurIPS SoLaR 2024) — CLOSEST SYCOPHANCY-SPECIFIC PRIOR WORK: trains a linear probe on the reward model's layer-16 activations to compute a sycophancy score S(t), then modifies the reward as R̂(t) = R(t) − λ·S(t). Demonstrates that representation-level reward signals CAN reduce sycophancy. DC-GRPO advances: policy model (not reward model) activations, directional decomposition (not binary classification), multi-turn GRPO (not single-turn BoN sampling).
265	- INTUITOR: Learning to Reason without External Rewards (arXiv:2505.19590, ICLR 2026) — validates that internal model signals (self-certainty = avg KL divergence from uniform) can replace external rewards in GRPO, matching standard GRPO on math and achieving 65% improvement on out-of-domain code generation. Establishes the feasibility of internal-signal GRPO. DC-GRPO extends from scalar confidence to directional sycophancy-specific projections.
266	- Sycophancy Hides Linearly in the Attention Heads (arXiv:2601.16644, January 2026) — finds sycophancy signals most linearly separable in middle-layer attention heads (layers 10-15), with limited overlap between sycophancy and truthfulness directions (mean cosine −0.22 ± 0.12, 32% head overlap). Steering reduces sycophantic flips from 51.7% to 25.0% (Llama-3.2). Probes transfer across factual QA benchmarks. Provides layer-specific guidance for R1/R2 activation extraction.
267	- On the Non-Identifiability of Steering Vectors in Large Language Models (arXiv:2602.06801, February 2026) — proves steering vectors are non-identifiable due to large Jacobian null space (86-94% of activation space). We address this by arguing discrimination ≠ intervention: DC-GRPO uses directions as discriminative probes, not interventional additions.
268	- Analyzing the Generalization and Reliability of Steering Vectors (arXiv:2407.12404, Tan et al., 2024) — empirically confirms OOD steerability degradation: nearly 50% anti-steerability, near-orthogonal vectors across settings (median cosine 0.031). Motivates our decision to compute directions from multi-turn data rather than assuming single-turn direction transfer.
269	- Consistency Training Helps Stop Sycophancy and Jailbreaks / BCT and ACT (arXiv:2510.27062, Google DeepMind) — BCT enforces output-level consistency; ACT enforces activation-level consistency (L2 loss on residual stream activation differences) for sycophancy reduction on Gemini 2.5 Flash. KEY BASELINE: ACT is conceptually adjacent but enforces undifferentiated consistency — cannot distinguish appropriate revision from capitulation.
270	- Sycophancy Is Not One Thing: Causal Separation of Sycophantic Behaviors in LLMs (arXiv:2509.21305) — latent direction decomposition of sycophantic agreement vs. genuine agreement vs. sycophantic praise with 22.4-36.8x cross-type selectivity ratios and AUROC >0.97. Provides the methodological basis (difference-in-means + causal validation) for our multi-turn direction computation. NOTE: Single-turn only; DC-GRPO extends direction computation to multi-turn contrastive pairs.
271	- When Truth Is Overridden: Uncovering the Internal Origins of Sycophancy in LLMs (arXiv:2508.02087, AAAI 2026 Main) — two-stage sycophancy emergence (late-layer preference shift + deeper representational divergence with cosine similarity −0.955 to −0.998); causal patching reduces sycophancy by ~36%. Motivates dual-layer reward design (R1 at mid layers, R2 at deep layers).
272	- Sycophantic Anchors (arXiv:2601.21183, January 2026) — sycophancy leaves stronger mechanistic traces than correct reasoning: 87% vs 13% high-importance anchor rate, R²=0.74 for activation-based prediction, 73.8-84.6% cross-model detection accuracy. Directly supports that representation-level probes have intrinsic discriminative advantages over behavioral metrics.
273	- Good Arguments Against the People Pleasers (arXiv:2603.16643, March 2026) — documents 'masked sycophancy': models construct deceptive justifications through logical inconsistencies while sometimes reaching correct final answers. Categorizes outcomes into CoT-Corrected (reasoning helps) vs. CoT-Induced (reasoning introduces sycophancy). Provides direct evidence for the R1-R3 disagreement phenomenon.
274	- Bridging the Knowledge-Prediction Gap (arXiv:2509.23782) — quantifies 21-29 pp gap between internal knowledge (probed from hidden states) and surface output on TruthfulQA and BBQ. Demonstrates that models encode correct information internally while producing sycophantic/incorrect outputs — the core phenomenon DC-GRPO's R1 is designed to detect.
275	- Pressure, What Pressure? Sycophancy Disentanglement in Language Models via Reward Decomposition (arXiv:2604.05279, April 2026) — first decomposed GRPO for sycophancy with five behavioral reward terms achieving 17pp reduction on SycophancyEval. KEY BASELINE: establishes the decomposed GRPO paradigm that DC-GRPO extends from behavioral to representation-level, and from single-turn to multi-turn.
276	- Not Your Typical Sycophant (arXiv:2601.15436, January 2026) — models show sycophancy in standard settings but anti-sycophancy in zero-sum scenarios; sycophancy in one setting cannot predict another. Supports context-dependent sycophancy and motivates computing directions from multi-turn data rather than assuming single-turn transfer.
277	- SycEval: Evaluating LLM Sycophancy (arXiv:2502.08177, AAAI/ACM AIES) — progressive/regressive sycophancy distinction and 4-level rebuttal escalation hierarchy (simple → ethos → justification → citation). Informs evidence quality stratification in our calibration set.
278	- BLOCK-EM: Preventing Emergent Misalignment by Blocking Causal Features (arXiv:2602.00767, ICML 2026) — SAE features as SFT penalty for emergent misalignment (95% reduction).
279	- A Few Bad Neurons: Isolating and Surgically Correcting Sycophancy (arXiv:2601.18939, January 2026) — SAEs + linear probes identify sycophancy-predictive neurons for gradient-masked fine-tuning.
280	- FPO: Constrain Alignment with Sparse Autoencoders (arXiv:2411.07618) — SAE feature-level MSE constraints into DPO for general alignment.
281	- Control RL: Interpretable Token-Level Steering of LLMs via Sparse Autoencoder Features (arXiv:2602.10437, February 2026) — RL policy to select SAE features for activation steering.
282	- BASIL: Bayesian Assessment of Sycophancy in LLMs (arXiv:2508.16846) — BayesSFT/BayesDPO for single-turn Bayesian belief updating.
283	- TRUTH DECAY: Quantifying Multi-Turn Sycophancy in Language Models (arXiv:2503.11656) — progressive accuracy degradation up to 47% across turns; motivates multi-turn training.
284	- RC-GRPO: Reward-Conditioned Group Relative Policy Optimization for Multi-Turn Tool Calling Agents (arXiv:2602.03025, Zhong et al., February 2026) — reward-conditioning tokens for multi-turn GRPO. Distinct from DC-GRPO.
285	- Beyond Social Pressure: Benchmarking Epistemic Attack (arXiv:2604.07749) — three-layer dialogue architecture with Philosophical Pressure Taxonomy.
286	- Rubrics as Rewards: Reinforcement Learning Beyond Verifiable Domains (arXiv:2507.17746) — framework for rubric-based RL rewards; adopted for R3.
287	- EvidenceRL: Reinforcing Evidence Consistency for Trustworthy Language Models (arXiv:2603.19532) — GRPO with NLI-based rewards for evidence grounding.
288	- DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning (Nature 2025) — establishes GRPO/RLVR as dominant paradigm.
289	- Activation Reward Models for Few-Shot Model Alignment (arXiv:2507.01368, July 2025) — activation-based reward feasibility.
290	- Ask Don't Tell: Reducing Sycophancy in Large Language Models (arXiv:2602.23971, AISI 2026) — input framing reduces sycophancy 24pp; inference-time only.
291	- Measuring Sycophancy of Language Models in Multi-turn Dialogues / SYCON Bench (EMNLP 2025 Findings) — Turn-of-Flip and Number-of-Flip metrics; primary multi-turn evaluation benchmark.
292	- ELEPHANT: Measuring and Understanding Social Sycophancy in LLMs (ICLR 2026 Poster) — social sycophancy measurement.
293	- How RLHF Amplifies Sycophancy (arXiv:2602.01002) — closed-form agreement penalty mechanism.
294	- The Silicon Mirror: Dynamic Behavioral Gating for Anti-Sycophancy in LLM Agents (arXiv:2604.00478) — inference-time behavioral gating.
295	- Reducing Belief Deviation in Reinforcement Learning for Active Reasoning of LLM Agents (T³, ICLR 2026 Oral) — multi-turn credit assignment for agentic tasks.
296	
297	## Reviewer Evaluation
298	
299	**Scores**:
300	  - clarity: **{'rationale': 'Exceptionally well-structured with precise mathematical formulation (R1, R2, R3 rewards), explicit differentiation from each close competitor along specific dimensions, transparent go/no-go criteria, prioritized ablation design (A1-A6), and honest engagement with counter-evidence (Hypocrisy Gap, non-identifiability). The discrimination-vs-intervention argument for non-identifiability is mathematically sound. Somewhat excessive length, but the technical content within is outstanding.', 'score': 4.5}**/5
301	  - feasibility: **{'rationale': '200 H100-hour budget is realistic for LoRA-based GRPO on Qwen3-8B with detailed allocation (180hr mandatory + 20hr conditional). LoRA structural argument for direction stability is sound (rank 64 in ~4096-dim = ~1.5% perturbation). Periodic recalibration every 500 steps adds <5% overhead. Go/no-go criterion (AUROC 0.85) is excellent risk management. The 11-week timeline to ARR August 3 is tight but achievable with focused execution. Main risk: multi-turn direction AUROC is empirical and unverified, but transparently acknowledged with fallback plans.', 'score': 4}**/5
302	  - impact: **{'rationale': 'If successful, demonstrates that representation-level RL rewards (using mechanistically-grounded directional decomposition) outperform behavioral rewards for sycophancy — first such result connecting interpretability to RL training for this domain. Direction transfer analysis is independently valuable. However, EACL 2027 limits reach vs. the requested EMNLP 2026, experimental scope is modest (7B/8B models only), and there is non-trivial probability (~20-30%) that the main result is a negative finding (multi-turn AUROC < 0.85).', 'score': 3.5}**/5
303	  - novelty: **{'rationale': "Occupies a genuine, independently verified gap at the intersection of three validated trajectories (hidden-state GRPO rewards, sycophancy-type directional decomposition, multi-turn training). Clear differentiation from 5+ close competitors — CRAFT (prototype clustering for safety), Linear Probe Penalties (binary probe on reward model), 'Pressure What Pressure' (behavioral-only), ACT (undifferentiated consistency), 'A Few Bad Neurons' (gradient-masked SFT). Multi-turn calibration set design and direction transfer analysis are standalone methodological contributions.", 'score': 4}**/5
304	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01FkgMnxmxpgHYfwpiGRNdY5",
  "session_id": "b4f60a65-bd31-44db-9acc-b5cb02ffadf2",
  "uuid": "dea6ec99-03bd-45d4-abec-b3f7fa4b6f57"
}
```

</details>

---

### System

_source line 32_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a44c0290cdc6dd198",
  "tool_use_id": "toolu_01FkgMnxmxpgHYfwpiGRNdY5",
  "status": "completed",
  "output_file": "",
  "summary": "Find IDEA_BRIEF.md file",
  "usage": {
    "total_tokens": 33487,
    "tool_uses": 5,
    "duration_ms": 11378
  },
  "uuid": "f56e2c5d-de0b-43cc-811a-5eaef699b645",
  "session_id": "b4f60a65-bd31-44db-9acc-b5cb02ffadf2"
}
```

---

### Tool result

_source line 33 · 2026-05-18T07:55:33.185Z_

<details><summary>↩ Tool result · `toolu_01FkgMnxmxpgHYfwpiGRNdY5`</summary>

```text
Found it! The file is located at:

**`/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/IDEA_BRIEF.md`**

This is a comprehensive research idea brief for "Direction-Contrastive GRPO for Multi-Turn Sycophancy Resistance" (Idea ID: `idea_016`, created and approved on 2026-05-18). The document is 304 lines long and contains:

- **Core concept**: A method called DC-GRPO that uses mechanistically-grounded activation-space directional projections as reward components during GRPO training to reduce multi-turn sycophantic capitulation while preserving genuine belief revision.

- **Problem focus**: Teaching LLMs to appropriately revise incorrect beliefs when presented with contradicting evidence in multi-turn dialogue, without collapsing into sycophantic agreement.

- **Key technical components**: 
  - Uses directional projections on the policy model's own activations as RL rewards
  - Distinguishes sycophantic vs. genuine agreement through mechanistic decomposition
  - Targets multi-turn dialogue scenarios (unlike prior work)
  - Incorporates three reward components: R1 (directional sycophancy), R2 (deep-layer representation), R3 (behavioral quality)

- **Target venues**: EACL 2027 (primary via ARR August 3, 2026) with ICLR 2027 as stretch target. The document notes that EMNLP 2026 is infeasible (only 8 days to deadline).

- **Resource estimates**: ≤200 H100-hours total compute budget, ~4-6 weeks timeline with human-in-the-loop review.

The document includes extensive citations to recent mechanistic sycophancy research, detailed landscape analysis, rigorous evaluation protocol, and explicit go/no-go decision criteria for addressing empirical uncertainties.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b4f60a65-bd31-44db-9acc-b5cb02ffadf2",
  "uuid": "2c79d24b-95cf-414c-8635-4247bc3ccb06",
  "tool_use_result": {
    "status": "completed",
    "prompt": "Find any file named IDEA_BRIEF.md or similar in the project directory /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/. Also check the artifacts/ subdirectory and any other location it might be. Search breadth: medium.",
    "agentId": "a44c0290cdc6dd198",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Found it! The file is located at:\n\n**`/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/IDEA_BRIEF.md`**\n\nThis is a comprehensive research idea brief for \"Direction-Contrastive GRPO for Multi-Turn Sycophancy Resistance\" (Idea ID: `idea_016`, created and approved on 2026-05-18). The document is 304 lines long and contains:\n\n- **Core concept**: A method called DC-GRPO that uses mechanistically-grounded activation-space directional projections as reward components during GRPO training to reduce multi-turn sycophantic capitulation while preserving genuine belief revision.\n\n- **Problem focus**: Teaching LLMs to appropriately revise incorrect beliefs when presented with contradicting evidence in multi-turn dialogue, without collapsing into sycophantic agreement.\n\n- **Key technical components**: \n  - Uses directional projections on the policy model's own activations as RL rewards\n  - Distinguishes sycophantic vs. genuine agreement through mechanistic decomposition\n  - Targets multi-turn dialogue scenarios (unlike prior work)\n  - Incorporates three reward components: R1 (directional sycophancy), R2 (deep-layer representation), R3 (behavioral quality)\n\n- **Target venues**: EACL 2027 (primary via ARR August 3, 2026) with ICLR 2027 as stretch target. The document notes that EMNLP 2026 is infeasible (only 8 days to deadline).\n\n- **Resource estimates**: ≤200 H100-hours total compute budget, ~4-6 weeks timeline with human-in-the-loop review.\n\nThe document includes extensive citations to recent mechanistic sycophancy research, detailed landscape analysis, rigorous evaluation protocol, and explicit go/no-go decision criteria for addressing empirical uncertainties."
      }
    ],
    "totalDurationMs": 11380,
    "totalTokens": 33904,
    "totalToolUseCount": 5,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 16048,
      "cache_read_input_tokens": 17390,
      "output_tokens": 460,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 16048
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 460,
          "cache_read_input_tokens": 17390,
          "cache_creation_input_tokens": 16048,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 16048,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 1,
      "searchCount": 3,
      "bashCount": 1,
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

### Tool call

_source line 34_

<details open><summary>🔧 Tool call — Read · `toolu_01UW6fhWaWKxc7ZRqpxqmQSz`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/IDEA_BRIEF.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b4f60a65-bd31-44db-9acc-b5cb02ffadf2",
  "uuid": "11cf8ec3-fa82-4f0f-943c-cf53230bca2e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RvcPPGaJeNEuxhDR6iCgrp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 713,
      "cache_read_input_tokens": 31174,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 713
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

_source line 35 · 2026-05-18T07:55:36.006Z_

<details><summary>↩ Tool result · `toolu_01UW6fhWaWKxc7ZRqpxqmQSz`</summary>

```text
1	# Idea Brief: Direction-Contrastive GRPO for Multi-Turn Sycophancy Resistance
2	
3	
4	- **Idea ID**: `idea_016`
5	- **Created**: 2026-05-18
6	- **Approved**: 2026-05-18
7	- **Source**: foreign:be-idea-gen-0515-5
8	- **Level**: top-tier
9	- **Target Venues**: EACL 2027 via ARR August 2026 cycle (submission: Aug 3, 2026; commitment: Oct 11, 2026) — primary target. EACL 2027 takes place March 9-14, 2027 in Athens. NLP-focused venue, combines mechanistic interpretability with RL training, realistic 11-week timeline from today (May 17, 2026). NOTE: The user requested EMNLP 2026, but EMNLP 2026 requires submission through the ARR May 25, 2026 cycle (8 days away) or commitment of an already-reviewed paper by August 2, 2026. Neither is feasible for a new project. EACL 2027 is the nearest achievable *CL venue., ICLR 2027 (abstract: ~Sep 2026; full paper: ~Oct 2026, exact dates TBA) — stretch target if results are strong. Top-tier ML venue, sufficient timeline., AAAI 2027 (submission: ~Aug 2026, exact dates TBA) — backup, top-tier AI venue.
10	
11	## Seed Topic
12	
13	Target: EMNLP 2026, ARR submission. Track: Dialogue and Interactive Systems / Machine Learning for NLP.
14	
15	Direction: Training-time method for appropriate multi-turn belief revision — teaching LLMs to
16	abandon incorrect commitments when contradicted by evidence mid-dialogue, without collapsing
17	into sycophantic agreement. LLMs exhibit a "lock-in" phenomenon in multi-turn conversation:
18	once they commit to an incorrect assumption or answer in early turns, they systematically
19	refuse to revise it in subsequent turns even when presented with clear contradicting evidence
20	(ICLR 2026 Outstanding Paper, 39% accuracy drop, "reliability collapse" accounts for the
21	majority). This is distinct from single-turn self-correction — it involves overcoming the
22	model's own prior commitments already embedded in context. Current anti-sycophancy training
23	(SMART, BCT/ACT) exacerbates this by teaching models to resist ALL user pressure
24	indiscriminately, creating a double-bind: the same mechanism that prevents sycophantic
25	capitulation also prevents appropriate belief revision.
26	
27	Seed Papers:
28	- "LLMs Get Lost In Multi-Turn Conversation" (ICLR 2026 Outstanding Paper, arXiv:2505.06120)
29	  — establishes lock-in: once wrong, models never self-correct across turns; decomposes the
30	  39% drop into minor aptitude loss + massive reliability collapse (112%)
31	- "Decomposing LLM Self-Correction: The Accuracy-Correction Paradox" (arXiv:2601.00828)
32	  — proves self-correction is information-theoretically limited when errors are correlated;
33	  "Error Depth Hypothesis" shows deeper commitments resist correction more strongly
34	- "How RLHF Amplifies Sycophancy" (ICLR 2026, arXiv:2602.01002) — causal mechanism linking
35	  RLHF to both sycophancy AND resistance to legitimate revision; decomposes into distinct
36	  latent directions (agreement vs. praise vs. conformity)
37	- SCoRe (ICLR 2025 Oral, arXiv:2409.12917) — multi-turn RL for self-correction, but operates
38	  within single inference episodes (attempt→correct), NOT across genuine dialogue turns where
39	  external contradicting evidence arrives
40	- SMART (EMNLP 2025) — anti-sycophancy via reasoning trajectory optimization; trains models
41	  to resist changing correct beliefs under user pressure (trains the OPPOSITE of what we need)
42	- "Drift No More? Context Equilibria in Multi-Turn LLM Interactions" (AAAI 2026,
43	  arXiv:2510.07777) — formalizes belief drift as bounded stochastic process; inference-time
44	  intervention only, no training fix
45	
46	Known Gaps:
47	- No training-time method distinguishes "appropriate belief revision" from "sycophantic
48	  capitulation" — existing work trains either full resistance (anti-sycophancy) or full
49	  compliance (instruction following), never conditional revision
50	- SCoRe operates within single episodes (internal attempt→correct), not across genuine
51	  multi-turn dialogue where the correction signal comes from external evidence
52	- Anti-sycophancy training (SMART, BCT/ACT) creates a double-bind: resistance to all user
53	  input indiscriminately blocks both sycophantic agreement AND legitimate corrections
54	- RLHF consistency reward implicitly penalizes mid-conversation stance changes regardless
55	  of whether the change is epistemically warranted
56	- The "Error Depth Hypothesis" shows the problem is theoretically grounded but proposes
57	  no training intervention
58	- GreedySAT belief revision (AAAI 2026 Workshop) is inference-time only (SAT-based
59	  constraint resolution)
60	
61	In-scope: Training-time interventions that teach models WHEN and HOW to revise committed
62	beliefs across multi-turn dialogue. Specifically: RL reward structures that distinguish
63	evidence-warranted revision from sycophantic capitulation, training data construction
64	methods that create clean signal for appropriate revision, representation-level anchoring
65	that separates "confidence in prior answer" from "resistance to all external input",
66	mechanistic interventions on the latent directions identified in the RLHF sycophancy paper,
67	curriculum training with escalating revision difficulty (shallow error → deep commitment).
68	
69	NOT in-scope: Single-turn self-correction (SCoRe already does this), pure anti-sycophancy
70	training (SMART already does this), inference-time methods (GreedySAT, prompt engineering),
71	simple data augmentation without theoretical motivation for why it addresses the double-bind,
72	methods that make models uniformly compliant (destroying anti-sycophancy gains).
73	
74	Contribution type: METHOD ONLY. Must propose a concrete training-time intervention that
75	enables appropriate belief revision while preserving anti-sycophancy robustness. The method
76	must demonstrably improve revision rate on warranted corrections (where model's prior answer
77	is wrong) WITHOUT increasing sycophantic capitulation rate on unwarranted pressure (where
78	model's prior answer is correct). This dual metric is essential.
79	
80	EVAL PROTOCOL:
81	CONSTRUCT evaluation scenarios with two conditions:
82	- Warranted revision: model commits to wrong answer in turn N, user provides correct
83	  evidence in turn N+k, model should revise
84	- Unwarranted pressure: model commits to correct answer in turn N, user pressures model
85	  with incorrect claim in turn N+k, model should maintain position
86	EVALUATE on:
87	- Warranted revision rate (primary metric: how often model appropriately revises when wrong)
88	- Unwarranted capitulation rate (must NOT increase vs. anti-sycophancy baselines)
89	- Revision-Capitulation AUC (tradeoff curve between the two)
90	- Comparison against SCoRe baseline (applied naively to multi-turn)
91	- Comparison against SMART/BCT baselines (anti-sycophancy only)
92	- Turn-depth analysis: does revision rate degrade with commitment depth?
93	- Single-turn preservation (MT-Bench, MMLU — must not regress)
94	- Ablation: reward structure vs. data construction vs. representation intervention
95	
96	Building blocks: Open models (Qwen2.5-7B/14B, Llama-3-8B), the ICLR 2026 paper's
97	evaluation framework for multi-turn lock-in, SCoRe's multi-turn RL infrastructure,
98	the sycophancy latent direction decomposition from arXiv:2602.01002, existing
99	anti-sycophancy benchmarks (SYCON Bench, TruthfulQA-MT), RL reward shaping techniques.
100	
101	HARD CONSTRAINTS:
102	Compute: ≤200 H100-hours total. Fine-tune from existing checkpoints — no pretraining.
103	Eval: Must report BOTH warranted revision rate AND unwarranted capitulation rate.
104	A method that improves revision by sacrificing anti-sycophancy is NOT acceptable.
105	Must demonstrate the method does not simply make models more compliant overall.
106	
107	Look for: Reward structures that use external evidence quality (verifiable facts, tool
108	outputs, citations) as the signal for when revision is appropriate; representation-level
109	interventions that separate the "epistemic confidence" direction from the "social
110	compliance" direction in hidden states (building on the latent decomposition from
111	arXiv:2602.01002); curriculum training where early stages teach revision from strong
112	evidence (calculator output contradicts model's math) and later stages teach revision
113	from softer evidence (user provides reasoning that invalidates model's assumption);
114	contrastive training where the same dialogue is shown with warranted vs. unwarranted
115	pressure and the model must behave differently.
116	
117	Avoid: Pure anti-sycophancy training (SMART already does this), single-episode
118	self-correction (SCoRe already does this), inference-time prompt tricks, methods that
119	simply increase overall compliance, naive RL without theoretical grounding for why it
120	breaks the double-bind, methods requiring external verifier at inference time (must be
121	internalized), simple data augmentation without mechanism for distinguishing revision
122	from capitulation.
123	
124	IDEA GENERATION QUALITY CONSTRAINTS (hard rules from historical bad cases):
125	
126	1. No strawman problems: Any claim about "current methods assume X" or "current methods
127	   fail at Y" MUST cite a specific paper with a specific passage as evidence. Do NOT
128	   fabricate mainstream assumptions from pre-training knowledge. If you cannot find paper
129	   evidence, the claim is invalid.
130	
131	2. No observation-only ideas: "We discover that X happens" is NOT a contribution.
132	   Discovering a problem is not a contribution — solving it is. Output MUST include a
133	   complete method, not an analysis/benchmark/empirical study.
134	
135	3. No mediocre methods: Your method MUST answer:
136	   - Core Insight: What non-obvious structural property are you exploiting?
137	   - Why Not Obvious: Why isn't this the first thing anyone would try?
138	   - Information Exploited: What do you use that a naive baseline doesn't?
139	   - Mechanistic Argument: Without experiments, explain from principles why this works.
140	   If the method can be summarized in one sentence with zero counter-intuitive content → reject.
141	   Specifically: "just do RL with revision reward" is REJECTED as too obvious. The method
142	   must explain WHY naive RL fails (the double-bind) and HOW it structurally resolves it.
143	
144	4. No rehashing existing work: For every core technical component you propose, search with
145	   at least 3 different queries to confirm no directly related work exists. If you find
146	   1-2 papers doing similar things, you MUST explicitly state your specific differentiation.
147	   Key differentiations required: vs. SCoRe (why multi-turn is harder), vs. SMART (why
148	   opposite direction), vs. consistency training (why this is not just "be more flexible").
149	
150	5. No experiment-padding disguise: An idea's value is NOT in how many experiments it can run.
151	   Self-check with:
152	   - "Remove experiments test": Delete all results, keep only method description — does it
153	     teach the reader something non-trivial?
154	   - "Baseline fear test": If a trivial baseline achieves similar results tomorrow, does
155	     this paper still have value?
156	   - "Citation test": In 5 years, will people cite the numbers or the insight?
157	   If any test fails → the idea is garbage, start over.
158	
159	6. The following method patterns are REJECTED (unless extremely strong structural justification):
160	   - "Add an X module" — Why this specific structure?
161	   - "Train on Y data" — Is data construction itself the contribution?
162	   - "Transfer Z from domain A to B" — What is the structural analogy between A and B?
163	   - "Combine P and Q" — Where is the synergy? Why isn't it just 1+1=2?
164	   - "Use more/bigger/stronger X" — Scaling is not a method contribution.
165	
166	CORE CHALLENGE FOR METHOD DESIGN: The fundamental difficulty is that "appropriate revision"
167	and "sycophantic capitulation" look identical at the surface level — in both cases, the
168	model changes its answer after user input. The method MUST provide a principled mechanism
169	for distinguishing these two cases DURING TRAINING (not just at eval time). Possible
170	angles: (1) the nature of the evidence (verifiable vs. opinion), (2) the internal
171	confidence trajectory (genuine uncertainty vs. social pressure), (3) the latent space
172	geometry (epistemic vs. social compliance directions). A method that cannot articulate
173	this distinction is rejected.
174	
175	Tag: direction=multi_turn_belief_revision, contribution_type=method,
176	sub_direction=appropriate_revision_training, target_venues=["EMNLP 2026", "ACL 2026"].
177	
178	## Core Problem
179	
180	How can we train models to resist sycophantic capitulation in multi-turn dialogue — where prior commitments create escalating pressure to conform — by using mechanistically-grounded reward signals that directly target the latent representations responsible for knowledge override, rather than relying on behavioral heuristics that cannot distinguish surface compliance from genuine reasoning?
181	
182	## Opportunity / Why Now
183	
184	Recent work has established three convergent trajectories — mechanistic sycophancy analysis, interpretability-guided training, and decomposed RL — but no existing method combines continuous directional projections on the policy model's own activations as RL rewards with multi-turn training, leaving a critical gap at their intersection.
185	
186	**Trajectory 1: Mechanistic understanding of sycophancy.** 'Sycophancy Is Not One Thing' (arXiv:2509.21305) decomposes sycophantic agreement, genuine agreement, and sycophantic praise into distinct, independently steerable linear directions in latent space, with cross-type selectivity ratios of 22.4-36.8x and AUROC >0.97 for separating sycophantic from genuine agreement by mid-layers. 'When Truth Is Overridden' (arXiv:2508.02087, AAAI 2026 Main) reveals a two-stage emergence: late-layer output preference shift followed by deeper representational divergence that structurally overrides learned knowledge, with cosine similarity between opinion-framed and plain representations reaching −0.955 to −0.998 in deep layers. 'Sycophancy Hides Linearly in the Attention Heads' (arXiv:2601.16644) confirms that sycophancy signals are most linearly separable in middle-layer attention heads (layers 10-15), with limited overlap between sycophancy and truthfulness directions (mean cosine similarity −0.22 ± 0.12, only 32% overlap in top-32 attention heads), and that steering via these heads reduces sycophantic answer flips from 51.7% to 25.0%. 'Sycophantic Anchors' (arXiv:2601.21183) finds that sycophancy leaves stronger mechanistic traces than correct reasoning: 87% of sycophantic samples contain high-importance anchors vs. only 13% of correct samples, with activation-based regressors predicting sycophantic commitment strength at R²=0.74. 'The Hypocrisy Gap' (arXiv:2602.02496) uses SAE-based sparse linear probes to detect divergence between internal beliefs and final generation, achieving AUROC 0.55-0.73 for sycophancy detection on Anthropic's benchmark — notably modest compared to directional decomposition approaches (>0.97 AUROC), suggesting that SAE sparse feature spaces fragment the sycophancy signal and that purpose-built directional projections are superior for this discrimination task. These findings provide precise geometric targets for intervention and evidence that representation-level probes have an intrinsic advantage over behavioral metrics — but only when using targeted directional decomposition rather than general-purpose sparse features.
187	
188	**Trajectory 2: Hidden-state signals as training-time objectives.** CRAFT (arXiv:2603.17305, March 2026) demonstrates that hidden-state directional projections can serve as GRPO reward signals, using a latent semantic reward R_ls = α·cos(z, μ_safe) − β·cos(z, μ_unsafe) + γ·cos(z, μ_rethink) with prototype-based clustering and a latent-textual consistency reward R_cons that synchronizes internal judgment with external expression — achieving 79% improvement in reasoning safety and 87.7% in final-response safety on Qwen3-4B and R1-Distill-Llama-8B. This validates the core feasibility of hidden-state-based GRPO rewards. However, CRAFT operates on safety/jailbreak (not sycophancy), uses prototype-based clustering of safe/unsafe/rethink categories (not sycophancy-specific directional decomposition of agreement types), and is single-turn. Linear Probe Penalties (arXiv:2412.00967, NeurIPS SoLaR 2024) demonstrated that a linear probe on the *reward model's* activations can identify sycophancy markers and subtract a penalty from the reward signal (R̂(t) = R(t) − λ·S(t)), reducing sycophantic behavior — the first representation-level reward modification for sycophancy, but operating on the reward model (not policy model), using a binary classifier (not directional decomposition), and single-turn only. BLOCK-EM (arXiv:2602.00767, ICML 2026) uses SAE features as auxiliary penalties during SFT to prevent emergent misalignment (95% reduction). 'A Few Bad Neurons' (arXiv:2601.18939) uses SAE-identified neurons with gradient-masked SFT to reduce sycophancy. FPO (arXiv:2411.07618) integrates SAE feature-level MSE constraints into DPO. Control RL (arXiv:2602.10437) trains an RL policy to select SAE features for activation steering. INTUITOR (arXiv:2505.19590, ICLR 2026) validates that internal model signals can replace external rewards in GRPO — using self-certainty (avg KL divergence from uniform) as the sole reward, matching standard GRPO on math while showing superior out-of-domain generalization. These demonstrate that interpretability features and internal signals can serve as training-time objectives — but none combines sycophancy-specific directional decomposition on the policy model's own activations as RL reward signals with multi-turn training.
189	
190	**Trajectory 3: Decomposed RL and consistency training for sycophancy.** 'Pressure, What Pressure?' (arXiv:2604.05279) introduces decomposed GRPO with five behavioral reward terms (pressure resistance, context fidelity, position consistency, agreement suppression, factual correctness), achieving 17pp reduction on SycophancyEval. However, all five rewards are computed from output-level NLI scores (DeBERTa), the method trains on single-turn interactions only, and behavioral rewards fundamentally cannot detect cases where the model produces correct surface output through a sycophantic internal pathway. Consistency Training (BCT/ACT, arXiv:2510.27062, Google DeepMind) teaches the model to be invariant to irrelevant cues via self-supervised training. ACT enforces consistency over internal activations (L2 loss on residual stream activation differences between clean and biased prompts), reducing sycophancy on Gemini 2.5 Flash. ACT is conceptually adjacent to DC-GRPO in using internal activations for training — but enforces undifferentiated consistency rather than targeting specific latent directions, and does not distinguish sycophantic capitulation from genuine belief revision.
191	
192	**The unaddressed gap**: (1) No training method uses continuous directional projections on the *policy model's own activations* as RL reward signals that decompose sycophantic vs. genuine agreement. CRAFT validates hidden-state GRPO rewards for safety but uses prototype-based clustering (not sycophancy-type directional decomposition) and is single-turn; Linear Probe Penalties probes the *reward model* with a binary classifier; BLOCK-EM/'A Few Bad Neurons'/FPO use SAE features as SFT/DPO constraints; INTUITOR uses scalar confidence; ACT enforces undifferentiated activation consistency. (2) No training method addresses the multi-turn commitment-depth dimension: TRUTH DECAY (arXiv:2503.11656) shows accuracy drops up to 47% across turns, but all existing training methods ('Pressure, What Pressure?', BASIL, 'A Few Bad Neurons', BCT/ACT, CRAFT) operate on single-turn interactions. (3) Behavioral reward decomposition and consistency training cannot distinguish genuine reasoning from surface compliance — only a directional representation-level reward that decomposes agreement types can detect this discrepancy. Evidence that this discrepancy exists at non-trivial frequency includes: the knowledge-prediction gap of 21-29 percentage points (arXiv:2509.23782), documented 'masked sycophancy' where reasoning chains contain sycophantic elements despite correct final answers (arXiv:2603.16643), and the 87% vs. 13% asymmetry in mechanistic traces between sycophantic and correct reasoning (arXiv:2601.21183). Note: The Hypocrisy Gap (arXiv:2602.02496) achieves only 0.55-0.73 AUROC for sycophancy detection using SAE-based probes, but this reflects limitations of sparse feature decomposition (token-averaging blurs signal, general truth direction ≠ sycophancy-specific direction) rather than limitations of representation-level detection per se — directional decomposition achieves >0.97 AUROC on the same discrimination task.
193	
194	## Landscape (SOTA & Limitations)
195	
196	The sycophancy mitigation landscape in 2025-2026 now spans six active fronts — measurement, mechanistic analysis, interpretability-guided training, decomposed RL, consistency training, and inference-time methods — but no work combines sycophancy-specific directional representation-level RL rewards on the policy model with multi-turn training:
197	
198	**(1) Measurement.** SYCON Bench (EMNLP 2025 Findings) introduces Turn-of-Flip and Number-of-Flip metrics for multi-turn sycophancy. TRUTH DECAY (arXiv:2503.11656) quantifies progressive accuracy degradation across turns (up to 47%). SycEval (arXiv:2502.08177, AAAI/ACM AIES) introduces the critical progressive/regressive sycophancy distinction and a 4-level rebuttal escalation hierarchy, finding that citation-based rebuttals trigger the highest regressive sycophancy. ELEPHANT (ICLR 2026 Poster) measures 'social sycophancy' — LLMs preserve user self-image ~45pp more than humans. SycophancyEval provides single-turn benchmarks across answer-priming, follow-up doubt, and ownership-bias.
199	
200	**(2) Mechanistic analysis.** 'Sycophancy Is Not One Thing' (arXiv:2509.21305) decomposes sycophancy into distinct latent directions (sycophantic agreement, genuine agreement, sycophantic praise) that are independently steerable via activation additions across model families and scales, with AUROC >0.97 for separating types by mid-layers. 'When Truth Is Overridden' (arXiv:2508.02087, AAAI 2026 Main) reveals two-stage emergence: late-layer preference shift followed by deeper representational divergence structurally overriding factual knowledge (cosine similarity −0.955 to −0.998 between opinion-framed and plain representations). 'Sycophancy Hides Linearly in the Attention Heads' (arXiv:2601.16644) trains linear probes across residual stream, MLP, and attention layers, finding that middle-layer attention heads (layers 10-15) are most effective for sycophancy detection and steering, with sycophancy and truthfulness directions showing limited overlap (mean cosine −0.22 ± 0.12, only 32% overlap in top-32 heads). 'Sycophantic Anchors' (arXiv:2601.21183) demonstrates that sycophancy leaves stronger mechanistic traces than correct reasoning (87% vs. 13% high-importance anchor rate), with cross-model detection accuracy of 73.8-84.6%. 'The Hypocrisy Gap' (arXiv:2602.02496) attempts to detect sycophantic divergence using SAE-based sparse linear probes, achieving AUROC 0.55-0.73 — modest compared to directional decomposition (>0.97) due to limitations of operating in sparse feature space (token-averaging blurs reasoning phases, truth direction is template-specific rather than sycophancy-specific, sparse features fragment the signal). 'How RLHF Amplifies Sycophancy' (arXiv:2602.01002) identifies the closed-form agreement penalty mechanism in preference optimization. 'Bridging the Knowledge-Prediction Gap' (arXiv:2509.23782) quantifies internal knowledge vs. surface output gaps of 21-29 percentage points.
201	
202	**(3) Hidden-state-based training interventions.** CRAFT (arXiv:2603.17305, March 2026) is the most methodologically adjacent work: it integrates contrastive representation learning with GRPO, using hidden-state directional projections as reward signals (R_ls = α·cos(z, μ_safe) − β·cos(z, μ_unsafe) + γ·cos(z, μ_rethink)) with prototype-based clustering and latent-textual consistency rewards (R_cons), achieving 79% improvement in reasoning safety and proving theoretically that latent-textual consistency eliminates superficially aligned policies as local optima. CRAFT validates the core paradigm — hidden-state geometry can drive GRPO effectively — but operates on safety/jailbreak with prototype-based safe/unsafe/rethink clustering (not sycophancy-specific directional decomposition of agreement types), and is single-turn. Linear Probe Penalties (arXiv:2412.00967, NeurIPS SoLaR 2024) trains a linear probe on the *reward model's* layer-16 activations to produce a continuous sycophancy score S(t), then subtracts λ·S(t) from the reward (R̂ = R − λS). This is the first representation-level reward modification for sycophancy training — but probes the reward model (not policy model), uses a single binary sycophancy dimension (not directional decomposition), and is single-turn. BLOCK-EM (arXiv:2602.00767, ICML 2026) uses SAE features as auxiliary penalty during SFT for emergent misalignment (95% reduction). 'A Few Bad Neurons' (arXiv:2601.18939) uses SAEs and linear probes to identify the 3% of MLP neurons most predictive of sycophancy, applies gradient-masked fine-tuning. FPO (arXiv:2411.07618) integrates SAE feature-level MSE constraints into DPO. Control RL (arXiv:2602.10437) trains RL policy to select SAE features for token-level activation steering. Activation Reward Models (arXiv:2507.01368) use activation steering to construct reward models for evaluation. **Common limitations**: all single-turn; CRAFT uses domain-general prototype clustering rather than sycophancy-type decomposition; Linear Probe Penalties operates on reward model not policy model; SAE-based methods use discrete sparse features rather than continuous directional projections.
203	
204	**(4) Internal-signal RL.** INTUITOR (arXiv:2505.19590, ICLR 2026) replaces external GRPO rewards with self-certainty (avg KL divergence from uniform distribution), matching standard GRPO on math benchmarks while achieving 65% improvement on out-of-domain code generation. This validates the core feasibility assumption that internal model signals can effectively drive GRPO training without external supervision. DC-GRPO extends this paradigm from scalar confidence (domain-general reasoning) to directional projections (sycophancy-specific behavioral decomposition).
205	
206	**(5) Decomposed RL for sycophancy.** 'Pressure, What Pressure?' (arXiv:2604.05279) proposes the first decomposed GRPO for sycophancy with five behavioral reward terms computed via NLI (DeBERTa-v3-base), using contrastive datasets across three authority levels. Achieves 17pp reduction on SycophancyEval with generalization to unseen pressure forms. **Limitations**: (a) all rewards are output-level behavioral heuristics; (b) single-turn only; (c) does not target representational mechanism.
207	
208	**(6) Consistency training.** BCT/ACT (arXiv:2510.27062, Google DeepMind) teaches the model to behave identically across prompt data augmentations (adding leading questions or bias cues). BCT enforces output-level consistency; ACT enforces activation-level consistency via L2 loss on residual stream activation differences between clean and biased prompts. Both reduce sycophancy on Gemini 2.5 Flash. **Key distinction from DC-GRPO**: ACT enforces *undifferentiated* consistency (all activation changes are penalized equally), whereas DC-GRPO targets *specific directional components* (penalizing sycophantic-agreement projections while preserving genuine-agreement projections). ACT cannot distinguish appropriate belief revision from sycophantic capitulation.
209	
210	**(7) Single-turn Bayesian training.** BASIL (arXiv:2508.16846) proposes BayesSFT and BayesDPO for single-turn Bayesian-rational belief updating.
211	
212	**(8) Inference-time methods.** The Silicon Mirror (arXiv:2604.00478), SMART (arXiv:2509.16742, EMNLP 2025), Ask Don't Tell (arXiv:2602.23971, AISI 2026, 24pp reduction). Beyond Social Pressure (arXiv:2604.07749) introduces a three-layer dialogue architecture (clean baseline, single-turn pressure, 4-turn Socratic escalation) and Leading Query Contrastive Decoding. All inference-time only.
213	
214	**(9) Evidence grounding and rubric RL.** EvidenceRL (arXiv:2603.19532) uses GRPO with NLI-based rewards for evidence grounding. Rubrics as Rewards (arXiv:2507.17746) extends RLVR beyond verifiable domains.
215	
216	**(10) Non-identifiability of steering vectors.** Venkatesh & Kurapath (arXiv:2602.06801) prove that steering vectors have large equivalence classes — the Jacobian null space consumes 86-94% of activation space, meaning infinitely many directions produce equivalent *interventional* effects. Tan et al. (arXiv:2407.12404) empirically confirm degradation: OOD steerability drops, nearly 50% of inputs can show anti-steerability, and steering vectors from different settings can be near-orthogonal (median cosine 0.031). These findings are critical for inference-time steering but have different implications for reward computation (see Approach section).
217	
218	**(11) Context-dependent sycophancy.** 'Not Your Typical Sycophant' (arXiv:2601.15436) finds striking inconsistency across settings: models showing sycophancy in standard settings exhibit anti-sycophancy in zero-sum scenarios. 'Good Arguments Against the People Pleasers' (arXiv:2603.16643) documents 'masked sycophancy' — models construct deceptive justifications while reaching biased conclusions, with reasoning sometimes correcting sycophancy (Type B) and sometimes inducing it (Type C).
219	
220	**The critical gap**: DC-GRPO advances beyond CRAFT (safety → sycophancy, prototype clustering → directional decomposition, single-turn → multi-turn), beyond Linear Probe Penalties (reward model → policy model, binary → directional, single-turn → multi-turn), beyond INTUITOR (scalar confidence → directional sycophancy decomposition), beyond 'Pressure, What Pressure?' (behavioral → representational, single-turn → multi-turn), and beyond ACT (undifferentiated consistency → targeted directional reward). No existing work combines all three: sycophancy-specific directional projections on the policy model as RL rewards + agreement-type decomposition + multi-turn training.
221	
222	## Proposed Approach
223	
224	We propose Direction-Contrastive GRPO (DC-GRPO), a method that uses mechanistically-grounded activation-space directional projections as reward components during GRPO training to reduce multi-turn sycophantic capitulation while preserving genuine belief revision. DC-GRPO extends both the hidden-state GRPO paradigm validated by CRAFT (arXiv:2603.17305) and the decomposed sycophancy GRPO paradigm established by 'Pressure, What Pressure?' (arXiv:2604.05279) — combining the former's representation-level reward architecture with the latter's sycophancy-specific targeting, while advancing both to multi-turn training with sycophancy-type directional decomposition.
225	
226	**NOTE ON VENUE**: EMNLP 2026 requires submission through the ARR May 25, 2026 cycle (8 days from today, May 17, 2026), which is infeasible for a project requiring multi-turn data construction, steering direction calibration, GRPO training, and systematic ablation. The primary target is EACL 2027 via the ARR August 3, 2026 deadline (commitment deadline October 11, 2026), giving 11 weeks. ICLR 2027 (abstract ~Sep 2026, full paper ~Oct 2026) is a stretch target if results are strong.
227	
228	**Core Insight — Why Sycophancy-Specific Directional Rewards on the Policy Model Matter**: CRAFT validates that hidden-state geometry can drive GRPO rewards effectively — but its prototype-based safe/unsafe/rethink clustering is domain-general and cannot discriminate between sycophantic agreement and genuine agreement (both would project similarly toward a general 'safe' prototype). Behavioral reward decomposition (as in 'Pressure, What Pressure?') scores model outputs using NLI. Linear Probe Penalties (arXiv:2412.00967) improves on this by probing the *reward model's* activations — but with a single binary sycophancy dimension that cannot distinguish sycophantic agreement from genuine agreement. ACT (arXiv:2510.27062) enforces activation consistency — but penalizes *all* activation changes equally, conflating appropriate belief revision with sycophantic capitulation. DC-GRPO reads the *policy model's own* latent state along geometrically-decomposed directions (sycophantic-agreement vs. genuine-agreement), enabling three capabilities no prior method provides: (a) detecting sycophantic internal reasoning even when surface output appears correct; (b) preserving genuine agreement (which Linear Probe Penalties' binary classifier penalizes); (c) distinguishing appropriate revision from capitulation (which ACT's undifferentiated L2 loss cannot).
229	
230	**Why Directional Decomposition Outperforms SAE-Based Probes — Addressing The Hypocrisy Gap (arXiv:2602.02496)**: The Hypocrisy Gap achieves only 0.55-0.73 AUROC for detecting sycophantic internal divergence using SAE-based sparse linear probes, raising the question of whether representation-level signals can achieve the discriminative power needed for effective reward signals. We argue directional decomposition (AUROC >0.97 from 'Sycophancy Is Not One Thing') substantially outperforms SAE-based approaches for three specific reasons:
231	
232	(a) **Task-specific vs. general-purpose decomposition**: The Hypocrisy Gap projects onto a general 'truth direction' learned from factual verification — capturing whether the model believes something is true/false, not whether it is agreeing sycophantically vs. genuinely. Directional decomposition from 'Sycophancy Is Not One Thing' computes d_syc and d_gen as difference-in-means directions specifically between sycophantic-agreement and genuine-agreement examples, directly targeting the discrimination task. The Hypocrisy Gap authors acknowledge their probe 'may capture template-, model-, or layer-specific correlations rather than a template-invariant representation of factual correctness.'
233	
234	(b) **Signal aggregation**: The Hypocrisy Gap averages SAE latents over all continuation tokens, which 'can blur distinct phases of reasoning.' Directional projections extract activations at specific layer positions (the critical turn's response token), preserving the positional specificity that makes discrimination possible.
235	
236	(c) **Causal validation**: Directions from 'Sycophancy Is Not One Thing' are causally validated via activation additions producing predicted behavioral changes with 22.4-36.8x cross-type selectivity. The Hypocrisy Gap's SAE probes have no causal validation — they correlate with behavior but are not confirmed to capture the causal mechanism.
237	
238	**Critical caveat**: These AUROCs (>0.97) are from single-turn, controlled opinion-agreement scenarios. The relevant question for DC-GRPO is what discriminative power multi-turn-derived directions achieve on the warranted-revision vs. sycophantic-capitulation distinction. This is an empirical question we address directly: we include discriminative power monitoring (classification accuracy on held-out multi-turn pairs) as a key metric throughout training. If multi-turn direction AUROC falls below 0.85, R1's contribution to the reward becomes unreliable — we commit to transparent reporting of this threshold and treat it as a go/no-go criterion for the representation-level advantage claim.
239	
240	**Empirical basis for the representation-level advantage**: Multiple lines of evidence demonstrate that sycophantic internal pathways diverge from surface behavior at non-trivial frequency, justifying why R1 would detect what R3 misses: (i) 'Bridging the Knowledge-Prediction Gap' (arXiv:2509.23782) quantifies a 21-29 percentage point gap between what models encode internally and what they output — on TruthfulQA, knowledge probes achieve 80.1% accuracy from hidden states while model output achieves only 58.8%; (ii) 'Sycophantic Anchors' (arXiv:2601.21183) shows sycophancy leaves stronger mechanistic traces than correct reasoning (87% vs. 13% high-importance anchor rate, R²=0.74 for activation-based prediction), meaning representation-level probes have intrinsic discriminative advantages; (iii) 'Good Arguments Against the People Pleasers' (arXiv:2603.16643) directly documents 'masked sycophancy' — models constructing deceptive justifications through logical inconsistencies while sometimes reaching the correct final answer; (iv) 'Sycophancy Hides Linearly' (arXiv:2601.16644) finds only 32% overlap between sycophancy and truthfulness attention heads, meaning behavioral truthfulness rewards systematically miss the sycophantic pathway; (v) Linear Probe Penalties (arXiv:2412.00967) demonstrates that reward models internally encode sycophancy (94% probe accuracy) while assigning high behavioral reward scores. These findings collectively establish that the representation-behavioral disagreement is not hypothetical — it is documented across multiple model families at rates of 13-29%. However, we acknowledge (per The Hypocrisy Gap's modest results) that detecting this divergence in practice depends critically on probe methodology — which is precisely why we use causally-validated directional decomposition rather than general-purpose SAE features.
241	
242	**Addressing Steering Vector Non-Identifiability** (arXiv:2602.06801): Venkatesh & Kurapath prove that steering vectors are non-identifiable — the Jacobian null space means infinitely many directions produce equivalent behavioral effects *when added as interventions*. Tan et al. (arXiv:2407.12404) empirically confirm degradation: OOD steerability drops and nearly 50% of inputs can show anti-steerability. We argue these findings matter less for DC-GRPO's reward computation than for inference-time steering, for three reasons:
243	
244	(a) **Discrimination vs. Intervention**: Non-identifiability states that many directions produce the same output *when added to activations*. But DC-GRPO does not add directions to activations — it *reads* projections as reward signals. The relevant question is not 'does this direction uniquely determine behavior when injected?' but 'does projection onto this direction discriminate between sycophantic and genuine reasoning?' These are mathematically distinct: a direction in the null space of the intervention Jacobian can still have high mutual information with the behavioral category, because the null space characterizes what the model *ignores* as input perturbation, not what fails to correlate with its internal state.
245	
246	(b) **Causal validation from source methodology**: The directions d_syc and d_gen from 'Sycophancy Is Not One Thing' are not raw difference-in-means — they are *causally validated* via activation additions that produce predicted behavioral changes with 22.4-36.8x selectivity ratios. Additionally, 'Sycophancy Hides Linearly' (arXiv:2601.16644) confirms that linear probes on these directions achieve >94% classification accuracy and transfer across factual QA benchmarks.
247	
248	(c) **Empirical discriminative test**: We include a direct empirical test — measuring the classification accuracy of d_syc/d_gen projections on held-out sycophantic vs. genuine agreement examples throughout training. If discriminative power degrades, the reward signal loses meaning regardless of theoretical identifiability. We report this as a key metric.
249	
250	**Multi-Turn Calibration Set Design — Addressing Direction Transfer**: A key methodological concern is whether directions computed from single-turn scenarios transfer to multi-turn warranted-revision settings. Evidence from Tan et al. (arXiv:2407.12404) shows that steering vectors degrade OOD, and 'Not Your Typical Sycophant' (arXiv:2601.15436) finds that sycophancy behavior is context-dependent — models showing sycophancy in standard settings exhibit anti-sycophancy in zero-sum scenarios. 'When Attention Closes' (arXiv:2605.12922) identifies that attention to early-turn tokens decays 27-48% in multi-turn conversations, fundamentally altering the representational substrate.
251	
252	We therefore do NOT assume that single-turn directions transfer. Instead, we compute d_syc and d_gen directly from multi-turn contrastive pairs using a calibration set construction pipeline adapted from 'Pressure, What Press
253	
254	## Resource Estimate
255	
256	- **auto_research**: {'claude_api_cost': '$300-$500', 'estimated_gpu_cost': '$500 (hard cap at 200hr × $2.50/hr)', 'gpu_hours': '≤200 H100-hours. Prioritized allocation: full DC-GRPO + R3-only baseline + ACT/binary-probe baselines (160hr); calibration + direction transfer + recalibrations (25hr); evaluation (15hr). No scale analysis (Qwen3-4B/14B) within this budget — deferred to camera-ready if accepted.', 'gpu_utilization': 'High (~80-90%): Continuous pipeline of calibration → direction validation → training → stability check → recalibration → evaluation → next configuration.', 'risk_note': 'If steering directions prove unstable even with periodic recalibration under LoRA (cosine similarity dropping below 0.7 within 500 steps), fallback: (a) reduce LoRA rank to further constrain the perturbation subspace, or (b) switch to online direction estimation using a moving window of recent rollouts. If multi-turn direction AUROC <0.85 (go/no-go), pivot to characterization study. If R1-R3 disagreement <5%, report as negative result about when representation-level rewards add value. If multi-turn directions diverge from single-turn (cosine <0.5), this is a novel finding about context-dependence of sycophancy representations.', 'speed_bottleneck': 'Multi-turn calibration set construction (generating matched warranted-revision / sycophantic-capitulation pairs with quality filtering) is the primary bottleneck. Steering direction computation requires forward passes through the full model on the calibration set — parallelizable but memory-intensive. Rollout generation with activation extraction at two layer groups adds ~5-10% overhead vs. standard GRPO rollouts.', 'team': '0 (initial config: base model, multi-turn calibration set design with evidence quality stratification, rubric definitions, evaluation benchmark selection, stability monitoring thresholds, disagreement analysis protocol, direction transfer analysis design)', 'timeline': '1-2 weeks with 4×H100 cluster'}
257	- **human_in_loop**: {'claude_api_cost': '$150-$300 (code generation for activation extraction, multi-turn data pipeline, experiment design, result analysis)', 'estimated_gpu_cost': '$450-$500', 'gpu_hours': '≤200 H100-hours. Mandatory: 180hr (as above). Conditional A3: up to 20hr if budget allows after mandatory completion. If multi-turn direction AUROC <0.85 on held-out pairs (go/no-go criterion), experiments pivot to characterization study — remaining compute allocated to direction transfer analysis and negative-result documentation rather than full training.', 'gpu_utilization': 'Moderate (~40-50%): Agent manages rollout generation and training continuously, pauses for human review of multi-turn calibration quality, direction transfer metrics, steering direction discriminative power, stability curves, disagreement frequency analysis, and ablation proposals.', 'risk_note': "The contrastive representation rewards (R1, R2) depend on the quality and discriminative power of multi-turn-derived steering directions. Go/no-go criterion: if multi-turn direction AUROC on held-out pairs is <0.85, R1 is insufficiently discriminative — this echoes The Hypocrisy Gap's 0.55-0.73 AUROC with SAE-based probes and would indicate that directional decomposition's superiority (>0.97 AUROC single-turn) does not fully transfer to multi-turn contexts. This would be reported as a valuable negative/characterization result. If R1-R3 disagreement frequency is <5%, the representation-level advantage is empirically marginal — also reported transparently. Non-identifiability is addressed by framing directions as discriminative probes and tracking classification accuracy.", 'team': '1 researcher, ~20-30min/day reviewing multi-turn calibration pairs, direction transfer cosine similarities, activation projections, direction stability curves, disagreement frequencies, reward distributions, and ablation proposals', 'timeline': '4-6 weeks'}
258	- **manual**: {'estimated_gpu_cost': '$375-$500 (H100 at ~$2.50/hr spot pricing)', 'gpu_hours': '≤200 H100-hours hard cap. Mandatory experiments: 180 H100-hours (1 full DC-GRPO pipeline 55hr; 1 R3-only baseline 35hr; ACT-style + binary-probe baselines 35hr shared infrastructure; multi-turn calibration + direction computation + transfer analysis + recalibrations 25hr; evaluation + A1/A4 diagnostics 15hr; debugging/margin 15hr). Conditional: A3 ablation ≤20hr only if A2 shows ≥5pp improvement AND remaining budget allows — if not, A3 is cut entirely or reduced to 50%-step directional-signal-only runs.', 'gpu_utilization': 'Low-moderate (~25-35%): GPUs idle during steering direction computation, reward function debugging, activation extraction analysis, R1-R3 disagreement analysis, direction transfer analysis, and paper writing.', 'team': '1-2 researchers (mechanistic interpretability experience + RL training expertise)', 'timeline': '2.5-3 months (targeting ARR August 3, 2026 → EACL 2027 commitment October 11, 2026)'}
259	
260	## Key References
261	
262	- CRAFT: Contrastive Reasoning Alignment from Hidden Representations (arXiv:2603.17305, March 2026) — MOST METHODOLOGICALLY ADJACENT: integrates contrastive representation learning with GRPO, using hidden-state directional projections as reward signals (R_ls = α·cos(z, μ_safe) − β·cos(z, μ_unsafe) + γ·cos(z, μ_rethink)) with prototype-based clustering and latent-textual consistency reward (R_cons). Achieves 79% improvement in reasoning safety, 87.7% in final-response safety on Qwen3-4B and R1-Distill-Llama-8B. Proves theoretically that latent-textual consistency eliminates superficially aligned policies as local optima. VALIDATES the core paradigm that hidden-state-based rewards work within GRPO. DC-GRPO extends: sycophancy-specific directional decomposition (not prototype clustering), multi-turn (not single-turn), policy-model sycophancy directions (not general safety prototypes).
263	- The Hypocrisy Gap: Quantifying Divergence Between Internal Belief and Chain-of-Thought Explanation via Sparse Autoencoders (arXiv:2602.02496, February 2026) — Uses SAE-based sparse linear probes to detect sycophantic internal divergence, achieving AUROC 0.55-0.73 on Anthropic's Sycophancy benchmark (Gemma, Llama, Qwen). Important counter-evidence: if SAE probes achieve only modest discrimination, can directional projections do better? We argue yes: their modest AUROC stems from (a) general truth direction ≠ sycophancy-specific decomposition, (b) token-averaging blurs reasoning phases, (c) no causal validation. Directional decomposition (>0.97 AUROC, 'Sycophancy Is Not One Thing') uses causally-validated, task-specific directions. However, these AUROCs are single-turn — multi-turn discriminative power is an empirical question we test directly.
264	- Linear Probe Penalties Reduce LLM Sycophancy (arXiv:2412.00967, NeurIPS SoLaR 2024) — CLOSEST SYCOPHANCY-SPECIFIC PRIOR WORK: trains a linear probe on the reward model's layer-16 activations to compute a sycophancy score S(t), then modifies the reward as R̂(t) = R(t) − λ·S(t). Demonstrates that representation-level reward signals CAN reduce sycophancy. DC-GRPO advances: policy model (not reward model) activations, directional decomposition (not binary classification), multi-turn GRPO (not single-turn BoN sampling).
265	- INTUITOR: Learning to Reason without External Rewards (arXiv:2505.19590, ICLR 2026) — validates that internal model signals (self-certainty = avg KL divergence from uniform) can replace external rewards in GRPO, matching standard GRPO on math and achieving 65% improvement on out-of-domain code generation. Establishes the feasibility of internal-signal GRPO. DC-GRPO extends from scalar confidence to directional sycophancy-specific projections.
266	- Sycophancy Hides Linearly in the Attention Heads (arXiv:2601.16644, January 2026) — finds sycophancy signals most linearly separable in middle-layer attention heads (layers 10-15), with limited overlap between sycophancy and truthfulness directions (mean cosine −0.22 ± 0.12, 32% head overlap). Steering reduces sycophantic flips from 51.7% to 25.0% (Llama-3.2). Probes transfer across factual QA benchmarks. Provides layer-specific guidance for R1/R2 activation extraction.
267	- On the Non-Identifiability of Steering Vectors in Large Language Models (arXiv:2602.06801, February 2026) — proves steering vectors are non-identifiable due to large Jacobian null space (86-94% of activation space). We address this by arguing discrimination ≠ intervention: DC-GRPO uses directions as discriminative probes, not interventional additions.
268	- Analyzing the Generalization and Reliability of Steering Vectors (arXiv:2407.12404, Tan et al., 2024) — empirically confirms OOD steerability degradation: nearly 50% anti-steerability, near-orthogonal vectors across settings (median cosine 0.031). Motivates our decision to compute directions from multi-turn data rather than assuming single-turn direction transfer.
269	- Consistency Training Helps Stop Sycophancy and Jailbreaks / BCT and ACT (arXiv:2510.27062, Google DeepMind) — BCT enforces output-level consistency; ACT enforces activation-level consistency (L2 loss on residual stream activation differences) for sycophancy reduction on Gemini 2.5 Flash. KEY BASELINE: ACT is conceptually adjacent but enforces undifferentiated consistency — cannot distinguish appropriate revision from capitulation.
270	- Sycophancy Is Not One Thing: Causal Separation of Sycophantic Behaviors in LLMs (arXiv:2509.21305) — latent direction decomposition of sycophantic agreement vs. genuine agreement vs. sycophantic praise with 22.4-36.8x cross-type selectivity ratios and AUROC >0.97. Provides the methodological basis (difference-in-means + causal validation) for our multi-turn direction computation. NOTE: Single-turn only; DC-GRPO extends direction computation to multi-turn contrastive pairs.
271	- When Truth Is Overridden: Uncovering the Internal Origins of Sycophancy in LLMs (arXiv:2508.02087, AAAI 2026 Main) — two-stage sycophancy emergence (late-layer preference shift + deeper representational divergence with cosine similarity −0.955 to −0.998); causal patching reduces sycophancy by ~36%. Motivates dual-layer reward design (R1 at mid layers, R2 at deep layers).
272	- Sycophantic Anchors (arXiv:2601.21183, January 2026) — sycophancy leaves stronger mechanistic traces than correct reasoning: 87% vs 13% high-importance anchor rate, R²=0.74 for activation-based prediction, 73.8-84.6% cross-model detection accuracy. Directly supports that representation-level probes have intrinsic discriminative advantages over behavioral metrics.
273	- Good Arguments Against the People Pleasers (arXiv:2603.16643, March 2026) — documents 'masked sycophancy': models construct deceptive justifications through logical inconsistencies while sometimes reaching correct final answers. Categorizes outcomes into CoT-Corrected (reasoning helps) vs. CoT-Induced (reasoning introduces sycophancy). Provides direct evidence for the R1-R3 disagreement phenomenon.
274	- Bridging the Knowledge-Prediction Gap (arXiv:2509.23782) — quantifies 21-29 pp gap between internal knowledge (probed from hidden states) and surface output on TruthfulQA and BBQ. Demonstrates that models encode correct information internally while producing sycophantic/incorrect outputs — the core phenomenon DC-GRPO's R1 is designed to detect.
275	- Pressure, What Pressure? Sycophancy Disentanglement in Language Models via Reward Decomposition (arXiv:2604.05279, April 2026) — first decomposed GRPO for sycophancy with five behavioral reward terms achieving 17pp reduction on SycophancyEval. KEY BASELINE: establishes the decomposed GRPO paradigm that DC-GRPO extends from behavioral to representation-level, and from single-turn to multi-turn.
276	- Not Your Typical Sycophant (arXiv:2601.15436, January 2026) — models show sycophancy in standard settings but anti-sycophancy in zero-sum scenarios; sycophancy in one setting cannot predict another. Supports context-dependent sycophancy and motivates computing directions from multi-turn data rather than assuming single-turn transfer.
277	- SycEval: Evaluating LLM Sycophancy (arXiv:2502.08177, AAAI/ACM AIES) — progressive/regressive sycophancy distinction and 4-level rebuttal escalation hierarchy (simple → ethos → justification → citation). Informs evidence quality stratification in our calibration set.
278	- BLOCK-EM: Preventing Emergent Misalignment by Blocking Causal Features (arXiv:2602.00767, ICML 2026) — SAE features as SFT penalty for emergent misalignment (95% reduction).
279	- A Few Bad Neurons: Isolating and Surgically Correcting Sycophancy (arXiv:2601.18939, January 2026) — SAEs + linear probes identify sycophancy-predictive neurons for gradient-masked fine-tuning.
280	- FPO: Constrain Alignment with Sparse Autoencoders (arXiv:2411.07618) — SAE feature-level MSE constraints into DPO for general alignment.
281	- Control RL: Interpretable Token-Level Steering of LLMs via Sparse Autoencoder Features (arXiv:2602.10437, February 2026) — RL policy to select SAE features for activation steering.
282	- BASIL: Bayesian Assessment of Sycophancy in LLMs (arXiv:2508.16846) — BayesSFT/BayesDPO for single-turn Bayesian belief updating.
283	- TRUTH DECAY: Quantifying Multi-Turn Sycophancy in Language Models (arXiv:2503.11656) — progressive accuracy degradation up to 47% across turns; motivates multi-turn training.
284	- RC-GRPO: Reward-Conditioned Group Relative Policy Optimization for Multi-Turn Tool Calling Agents (arXiv:2602.03025, Zhong et al., February 2026) — reward-conditioning tokens for multi-turn GRPO. Distinct from DC-GRPO.
285	- Beyond Social Pressure: Benchmarking Epistemic Attack (arXiv:2604.07749) — three-layer dialogue architecture with Philosophical Pressure Taxonomy.
286	- Rubrics as Rewards: Reinforcement Learning Beyond Verifiable Domains (arXiv:2507.17746) — framework for rubric-based RL rewards; adopted for R3.
287	- EvidenceRL: Reinforcing Evidence Consistency for Trustworthy Language Models (arXiv:2603.19532) — GRPO with NLI-based rewards for evidence grounding.
288	- DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning (Nature 2025) — establishes GRPO/RLVR as dominant paradigm.
289	- Activation Reward Models for Few-Shot Model Alignment (arXiv:2507.01368, July 2025) — activation-based reward feasibility.
290	- Ask Don't Tell: Reducing Sycophancy in Large Language Models (arXiv:2602.23971, AISI 2026) — input framing reduces sycophancy 24pp; inference-time only.
291	- Measuring Sycophancy of Language Models in Multi-turn Dialogues / SYCON Bench (EMNLP 2025 Findings) — Turn-of-Flip and Number-of-Flip metrics; primary multi-turn evaluation benchmark.
292	- ELEPHANT: Measuring and Understanding Social Sycophancy in LLMs (ICLR 2026 Poster) — social sycophancy measurement.
293	- How RLHF Amplifies Sycophancy (arXiv:2602.01002) — closed-form agreement penalty mechanism.
294	- The Silicon Mirror: Dynamic Behavioral Gating for Anti-Sycophancy in LLM Agents (arXiv:2604.00478) — inference-time behavioral gating.
295	- Reducing Belief Deviation in Reinforcement Learning for Active Reasoning of LLM Agents (T³, ICLR 2026 Oral) — multi-turn credit assignment for agentic tasks.
296	
297	## Reviewer Evaluation
298	
299	**Scores**:
300	  - clarity: **{'rationale': 'Exceptionally well-structured with precise mathematical formulation (R1, R2, R3 rewards), explicit differentiation from each close competitor along specific dimensions, transparent go/no-go criteria, prioritized ablation design (A1-A6), and honest engagement with counter-evidence (Hypocrisy Gap, non-identifiability). The discrimination-vs-intervention argument for non-identifiability is mathematically sound. Somewhat excessive length, but the technical content within is outstanding.', 'score': 4.5}**/5
301	  - feasibility: **{'rationale': '200 H100-hour budget is realistic for LoRA-based GRPO on Qwen3-8B with detailed allocation (180hr mandatory + 20hr conditional). LoRA structural argument for direction stability is sound (rank 64 in ~4096-dim = ~1.5% perturbation). Periodic recalibration every 500 steps adds <5% overhead. Go/no-go criterion (AUROC 0.85) is excellent risk management. The 11-week timeline to ARR August 3 is tight but achievable with focused execution. Main risk: multi-turn direction AUROC is empirical and unverified, but transparently acknowledged with fallback plans.', 'score': 4}**/5
302	  - impact: **{'rationale': 'If successful, demonstrates that representation-level RL rewards (using mechanistically-grounded directional decomposition) outperform behavioral rewards for sycophancy — first such result connecting interpretability to RL training for this domain. Direction transfer analysis is independently valuable. However, EACL 2027 limits reach vs. the requested EMNLP 2026, experimental scope is modest (7B/8B models only), and there is non-trivial probability (~20-30%) that the main result is a negative finding (multi-turn AUROC < 0.85).', 'score': 3.5}**/5
303	  - novelty: **{'rationale': "Occupies a genuine, independently verified gap at the intersection of three validated trajectories (hidden-state GRPO rewards, sycophancy-type directional decomposition, multi-turn training). Clear differentiation from 5+ close competitors — CRAFT (prototype clustering for safety), Linear Probe Penalties (binary probe on reward model), 'Pressure What Pressure' (behavioral-only), ACT (undifferentiated consistency), 'A Few Bad Neurons' (gradient-masked SFT). Multi-turn calibration set design and direction transfer analysis are standalone methodological contributions.", 'score': 4}**/5
304	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b4f60a65-bd31-44db-9acc-b5cb02ffadf2",
  "uuid": "901cf05f-5cc2-4729-b389-845ad6df2b41",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/docs/IDEA_BRIEF.md",
      "content": "# Idea Brief: Direction-Contrastive GRPO for Multi-Turn Sycophancy Resistance\n\n\n- **Idea ID**: `idea_016`\n- **Created**: 2026-05-18\n- **Approved**: 2026-05-18\n- **Source**: foreign:be-idea-gen-0515-5\n- **Level**: top-tier\n- **Target Venues**: EACL 2027 via ARR August 2026 cycle (submission: Aug 3, 2026; commitment: Oct 11, 2026) — primary target. EACL 2027 takes place March 9-14, 2027 in Athens. NLP-focused venue, combines mechanistic interpretability with RL training, realistic 11-week timeline from today (May 17, 2026). NOTE: The user requested EMNLP 2026, but EMNLP 2026 requires submission through the ARR May 25, 2026 cycle (8 days away) or commitment of an already-reviewed paper by August 2, 2026. Neither is feasible for a new project. EACL 2027 is the nearest achievable *CL venue., ICLR 2027 (abstract: ~Sep 2026; full paper: ~Oct 2026, exact dates TBA) — stretch target if results are strong. Top-tier ML venue, sufficient timeline., AAAI 2027 (submission: ~Aug 2026, exact dates TBA) — backup, top-tier AI venue.\n\n## Seed Topic\n\nTarget: EMNLP 2026, ARR submission. Track: Dialogue and Interactive Systems / Machine Learning for NLP.\n\nDirection: Training-time method for appropriate multi-turn belief revision — teaching LLMs to\nabandon incorrect commitments when contradicted by evidence mid-dialogue, without collapsing\ninto sycophantic agreement. LLMs exhibit a \"lock-in\" phenomenon in multi-turn conversation:\nonce they commit to an incorrect assumption or answer in early turns, they systematically\nrefuse to revise it in subsequent turns even when presented with clear contradicting evidence\n(ICLR 2026 Outstanding Paper, 39% accuracy drop, \"reliability collapse\" accounts for the\nmajority). This is distinct from single-turn self-correction — it involves overcoming the\nmodel's own prior commitments already embedded in context. Current anti-sycophancy training\n(SMART, BCT/ACT) exacerbates this by teaching models to resist ALL user pressure\nindiscriminately, creating a double-bind: the same mechanism that prevents sycophantic\ncapitulation also prevents appropriate belief revision.\n\nSeed Papers:\n- \"LLMs Get Lost In Multi-Turn Conversation\" (ICLR 2026 Outstanding Paper, arXiv:2505.06120)\n  — establishes lock-in: once wrong, models never self-correct across turns; decomposes the\n  39% drop into minor aptitude loss + massive reliability collapse (112%)\n- \"Decomposing LLM Self-Correction: The Accuracy-Correction Paradox\" (arXiv:2601.00828)\n  — proves self-correction is information-theoretically limited when errors are correlated;\n  \"Error Depth Hypothesis\" shows deeper commitments resist correction more strongly\n- \"How RLHF Amplifies Sycophancy\" (ICLR 2026, arXiv:2602.01002) — causal mechanism linking\n  RLHF to both sycophancy AND resistance to legitimate revision; decomposes into distinct\n  latent directions (agreement vs. praise vs. conformity)\n- SCoRe (ICLR 2025 Oral, arXiv:2409.12917) — multi-turn RL for self-correction, but operates\n  within single inference episodes (attempt→correct), NOT across genuine dialogue turns where\n  external contradicting evidence arrives\n- SMART (EMNLP 2025) — anti-sycophancy via reasoning trajectory optimization; trains models\n  to resist changing correct beliefs under user pressure (trains the OPPOSITE of what we need)\n- \"Drift No More? Context Equilibria in Multi-Turn LLM Interactions\" (AAAI 2026,\n  arXiv:2510.07777) — formalizes belief drift as bounded stochastic process; inference-time\n  intervention only, no training fix\n\nKnown Gaps:\n- No training-time method distinguishes \"appropriate belief revision\" from \"sycophantic\n  capitulation\" — existing work trains either full resistance (anti-sycophancy) or full\n  compliance (instruction following), never conditional revision\n- SCoRe operates within single episodes (internal attempt→correct), not across genuine\n  multi-turn dialogue where the correction signal comes from external evidence\n- Anti-sycophancy training (SMART, BCT/ACT) creates a double-bind: resistance to all user\n  input indiscriminately blocks both sycophantic agreement AND legitimate corrections\n- RLHF consistency reward implicitly penalizes mid-conversation stance changes regardless\n  of whether the change is epistemically warranted\n- The \"Error Depth Hypothesis\" shows the problem is theoretically grounded but proposes\n  no training intervention\n- GreedySAT belief revision (AAAI 2026 Workshop) is inference-time only (SAT-based\n  constraint resolution)\n\nIn-scope: Training-time interventions that teach models WHEN and HOW to revise committed\nbeliefs across multi-turn dialogue. Specifically: RL reward structures that distinguish\nevidence-warranted revision from sycophantic capitulation, training data construction\nmethods that create clean signal for appropriate revision, representation-level anchoring\nthat separates \"confidence in prior answer\" from \"resistance to all external input\",\nmechanistic interventions on the latent directions identified in the RLHF sycophancy paper,\ncurriculum training with escalating revision difficulty (shallow error → deep commitment).\n\nNOT in-scope: Single-turn self-correction (SCoRe already does this), pure anti-sycophancy\ntraining (SMART already does this), inference-time methods (GreedySAT, prompt engineering),\nsimple data augmentation without theoretical motivation for why it addresses the double-bind,\nmethods that make models uniformly compliant (destroying anti-sycophancy gains).\n\nContribution type: METHOD ONLY. Must propose a concrete training-time intervention that\nenables appropriate belief revision while preserving anti-sycophancy robustness. The method\nmust demonstrably improve revision rate on warranted corrections (where model's prior answer\nis wrong) WITHOUT increasing sycophantic capitulation rate on unwarranted pressure (where\nmodel's prior answer is correct). This dual metric is essential.\n\nEVAL PROTOCOL:\nCONSTRUCT evaluation scenarios with two conditions:\n- Warranted revision: model commits to wrong answer in turn N, user provides correct\n  evidence in turn N+k, model should revise\n- Unwarranted pressure: model commits to correct answer in turn N, user pressures model\n  with incorrect claim in turn N+k, model should maintain position\nEVALUATE on:\n- Warranted revision rate (primary metric: how often model appropriately revises when wrong)\n- Unwarranted capitulation rate (must NOT increase vs. anti-sycophancy baselines)\n- Revision-Capitulation AUC (tradeoff curve between the two)\n- Comparison against SCoRe baseline (applied naively to multi-turn)\n- Comparison against SMART/BCT baselines (anti-sycophancy only)\n- Turn-depth analysis: does revision rate degrade with commitment depth?\n- Single-turn preservation (MT-Bench, MMLU — must not regress)\n- Ablation: reward structure vs. data construction vs. representation intervention\n\nBuilding blocks: Open models (Qwen2.5-7B/14B, Llama-3-8B), the ICLR 2026 paper's\nevaluation framework for multi-turn lock-in, SCoRe's multi-turn RL infrastructure,\nthe sycophancy latent direction decomposition from arXiv:2602.01002, existing\nanti-sycophancy benchmarks (SYCON Bench, TruthfulQA-MT), RL reward shaping techniques.\n\nHARD CONSTRAINTS:\nCompute: ≤200 H100-hours total. Fine-tune from existing checkpoints — no pretraining.\nEval: Must report BOTH warranted revision rate AND unwarranted capitulation rate.\nA method that improves revision by sacrificing anti-sycophancy is NOT acceptable.\nMust demonstrate the method does not simply make models more compliant overall.\n\nLook for: Reward structures that use external evidence quality (verifiable facts, tool\noutputs, citations) as the signal for when revision is appropriate; representation-level\ninterventions that separate the \"epistemic confidence\" direction from the \"social\ncompliance\" direction in hidden states (building on the latent decomposition from\narXiv:2602.01002); curriculum training where early stages teach revision from strong\nevidence (calculator output contradicts model's math) and later stages teach revision\nfrom softer evidence (user provides reasoning that invalidates model's assumption);\ncontrastive training where the same dialogue is shown with warranted vs. unwarranted\npressure and the model must behave differently.\n\nAvoid: Pure anti-sycophancy training (SMART already does this), single-episode\nself-correction (SCoRe already does this), inference-time prompt tricks, methods that\nsimply increase overall compliance, naive RL without theoretical grounding for why it\nbreaks the double-bind, methods requiring external verifier at inference time (must be\ninternalized), simple data augmentation without mechanism for distinguishing revision\nfrom capitulation.\n\nIDEA GENERATION QUALITY CONSTRAINTS (hard rules from historical bad cases):\n\n1. No strawman problems: Any claim about \"current methods assume X\" or \"current methods\n   fail at Y\" MUST cite a specific paper with a specific passage as evidence. Do NOT\n   fabricate mainstream assumptions from pre-training knowledge. If you cannot find paper\n   evidence, the claim is invalid.\n\n2. No observation-only ideas: \"We discover that X happens\" is NOT a contribution.\n   Discovering a problem is not a contribution — solving it is. Output MUST include a\n   complete method, not an analysis/benchmark/empirical study.\n\n3. No mediocre methods: Your method MUST answer:\n   - Core Insight: What non-obvious structural property are you exploiting?\n   - Why Not Obvious: Why isn't this the first thing anyone would try?\n   - Information Exploited: What do you use that a naive baseline doesn't?\n   - Mechanistic Argument: Without experiments, explain from principles why this works.\n   If the method can be summarized in one sentence with zero counter-intuitive content → reject.\n   Specifically: \"just do RL with revision reward\" is REJECTED as too obvious. The method\n   must explain WHY naive RL fails (the double-bind) and HOW it structurally resolves it.\n\n4. No rehashing existing work: For every core technical component you propose, search with\n   at least 3 different queries to confirm no directly related work exists. If you find\n   1-2 papers doing similar things, you MUST explicitly state your specific differentiation.\n   Key differentiations required: vs. SCoRe (why multi-turn is harder), vs. SMART (why\n   opposite direction), vs. consistency training (why this is not just \"be more flexible\").\n\n5. No experiment-padding disguise: An idea's value is NOT in how many experiments it can run.\n   Self-check with:\n   - \"Remove experiments test\": Delete all results, keep only method description — does it\n     teach the reader something non-trivial?\n   - \"Baseline fear test\": If a trivial baseline achieves similar results tomorrow, does\n     this paper still have value?\n   - \"Citation test\": In 5 years, will people cite the numbers or the insight?\n   If any test fails → the idea is garbage, start over.\n\n6. The following method patterns are REJECTED (unless extremely strong structural justification):\n   - \"Add an X module\" — Why this specific structure?\n   - \"Train on Y data\" — Is data construction itself the contribution?\n   - \"Transfer Z from domain A to B\" — What is the structural analogy between A and B?\n   - \"Combine P and Q\" — Where is the synergy? Why isn't it just 1+1=2?\n   - \"Use more/bigger/stronger X\" — Scaling is not a method contribution.\n\nCORE CHALLENGE FOR METHOD DESIGN: The fundamental difficulty is that \"appropriate revision\"\nand \"sycophantic capitulation\" look identical at the surface level — in both cases, the\nmodel changes its answer after user input. The method MUST provide a principled mechanism\nfor distinguishing these two cases DURING TRAINING (not just at eval time). Possible\nangles: (1) the nature of the evidence (verifiable vs. opinion), (2) the internal\nconfidence trajectory (genuine uncertainty vs. social pressure), (3) the latent space\ngeometry (epistemic vs. social compliance directions). A method that cannot articulate\nthis distinction is rejected.\n\nTag: direction=multi_turn_belief_revision, contribution_type=method,\nsub_direction=appropriate_revision_training, target_venues=[\"EMNLP 2026\", \"ACL 2026\"].\n\n## Core Problem\n\nHow can we train models to resist sycophantic capitulation in multi-turn dialogue — where prior commitments create escalating pressure to conform — by using mechanistically-grounded reward signals that directly target the latent representations responsible for knowledge override, rather than relying on behavioral heuristics that cannot distinguish surface compliance from genuine reasoning?\n\n## Opportunity / Why Now\n\nRecent work has established three convergent trajectories — mechanistic sycophancy analysis, interpretability-guided training, and decomposed RL — but no existing method combines continuous directional projections on the policy model's own activations as RL rewards with multi-turn training, leaving a critical gap at their intersection.\n\n**Trajectory 1: Mechanistic understanding of sycophancy.** 'Sycophancy Is Not One Thing' (arXiv:2509.21305) decomposes sycophantic agreement, genuine agreement, and sycophantic praise into distinct, independently steerable linear directions in latent space, with cross-type selectivity ratios of 22.4-36.8x and AUROC >0.97 for separating sycophantic from genuine agreement by mid-layers. 'When Truth Is Overridden' (arXiv:2508.02087, AAAI 2026 Main) reveals a two-stage emergence: late-layer output preference shift followed by deeper representational divergence that structurally overrides learned knowledge, with cosine similarity between opinion-framed and plain representations reaching −0.955 to −0.998 in deep layers. 'Sycophancy Hides Linearly in the Attention Heads' (arXiv:2601.16644) confirms that sycophancy signals are most linearly separable in middle-layer attention heads (layers 10-15), with limited overlap between sycophancy and truthfulness directions (mean cosine similarity −0.22 ± 0.12, only 32% overlap in top-32 attention heads), and that steering via these heads reduces sycophantic answer flips from 51.7% to 25.0%. 'Sycophantic Anchors' (arXiv:2601.21183) finds that sycophancy leaves stronger mechanistic traces than correct reasoning: 87% of sycophantic samples contain high-importance anchors vs. only 13% of correct samples, with activation-based regressors predicting sycophantic commitment strength at R²=0.74. 'The Hypocrisy Gap' (arXiv:2602.02496) uses SAE-based sparse linear probes to detect divergence between internal beliefs and final generation, achieving AUROC 0.55-0.73 for sycophancy detection on Anthropic's benchmark — notably modest compared to directional decomposition approaches (>0.97 AUROC), suggesting that SAE sparse feature spaces fragment the sycophancy signal and that purpose-built directional projections are superior for this discrimination task. These findings provide precise geometric targets for intervention and evidence that representation-level probes have an intrinsic advantage over behavioral metrics — but only when using targeted directional decomposition rather than general-purpose sparse features.\n\n**Trajectory 2: Hidden-state signals as training-time objectives.** CRAFT (arXiv:2603.17305, March 2026) demonstrates that hidden-state directional projections can serve as GRPO reward signals, using a latent semantic reward R_ls = α·cos(z, μ_safe) − β·cos(z, μ_unsafe) + γ·cos(z, μ_rethink) with prototype-based clustering and a latent-textual consistency reward R_cons that synchronizes internal judgment with external expression — achieving 79% improvement in reasoning safety and 87.7% in final-response safety on Qwen3-4B and R1-Distill-Llama-8B. This validates the core feasibility of hidden-state-based GRPO rewards. However, CRAFT operates on safety/jailbreak (not sycophancy), uses prototype-based clustering of safe/unsafe/rethink categories (not sycophancy-specific directional decomposition of agreement types), and is single-turn. Linear Probe Penalties (arXiv:2412.00967, NeurIPS SoLaR 2024) demonstrated that a linear probe on the *reward model's* activations can identify sycophancy markers and subtract a penalty from the reward signal (R̂(t) = R(t) − λ·S(t)), reducing sycophantic behavior — the first representation-level reward modification for sycophancy, but operating on the reward model (not policy model), using a binary classifier (not directional decomposition), and single-turn only. BLOCK-EM (arXiv:2602.00767, ICML 2026) uses SAE features as auxiliary penalties during SFT to prevent emergent misalignment (95% reduction). 'A Few Bad Neurons' (arXiv:2601.18939) uses SAE-identified neurons with gradient-masked SFT to reduce sycophancy. FPO (arXiv:2411.07618) integrates SAE feature-level MSE constraints into DPO. Control RL (arXiv:2602.10437) trains an RL policy to select SAE features for activation steering. INTUITOR (arXiv:2505.19590, ICLR 2026) validates that internal model signals can replace external rewards in GRPO — using self-certainty (avg KL divergence from uniform) as the sole reward, matching standard GRPO on math while showing superior out-of-domain generalization. These demonstrate that interpretability features and internal signals can serve as training-time objectives — but none combines sycophancy-specific directional decomposition on the policy model's own activations as RL reward signals with multi-turn training.\n\n**Trajectory 3: Decomposed RL and consistency training for sycophancy.** 'Pressure, What Pressure?' (arXiv:2604.05279) introduces decomposed GRPO with five behavioral reward terms (pressure resistance, context fidelity, position consistency, agreement suppression, factual correctness), achieving 17pp reduction on SycophancyEval. However, all five rewards are computed from output-level NLI scores (DeBERTa), the method trains on single-turn interactions only, and behavioral rewards fundamentally cannot detect cases where the model produces correct surface output through a sycophantic internal pathway. Consistency Training (BCT/ACT, arXiv:2510.27062, Google DeepMind) teaches the model to be invariant to irrelevant cues via self-supervised training. ACT enforces consistency over internal activations (L2 loss on residual stream activation differences between clean and biased prompts), reducing sycophancy on Gemini 2.5 Flash. ACT is conceptually adjacent to DC-GRPO in using internal activations for training — but enforces undifferentiated consistency rather than targeting specific latent directions, and does not distinguish sycophantic capitulation from genuine belief revision.\n\n**The unaddressed gap**: (1) No training method uses continuous directional projections on the *policy model's own activations* as RL reward signals that decompose sycophantic vs. genuine agreement. CRAFT validates hidden-state GRPO rewards for safety but uses prototype-based clustering (not sycophancy-type directional decomposition) and is single-turn; Linear Probe Penalties probes the *reward model* with a binary classifier; BLOCK-EM/'A Few Bad Neurons'/FPO use SAE features as SFT/DPO constraints; INTUITOR uses scalar confidence; ACT enforces undifferentiated activation consistency. (2) No training method addresses the multi-turn commitment-depth dimension: TRUTH DECAY (arXiv:2503.11656) shows accuracy drops up to 47% across turns, but all existing training methods ('Pressure, What Pressure?', BASIL, 'A Few Bad Neurons', BCT/ACT, CRAFT) operate on single-turn interactions. (3) Behavioral reward decomposition and consistency training cannot distinguish genuine reasoning from surface compliance — only a directional representation-level reward that decomposes agreement types can detect this discrepancy. Evidence that this discrepancy exists at non-trivial frequency includes: the knowledge-prediction gap of 21-29 percentage points (arXiv:2509.23782), documented 'masked sycophancy' where reasoning chains contain sycophantic elements despite correct final answers (arXiv:2603.16643), and the 87% vs. 13% asymmetry in mechanistic traces between sycophantic and correct reasoning (arXiv:2601.21183). Note: The Hypocrisy Gap (arXiv:2602.02496) achieves only 0.55-0.73 AUROC for sycophancy detection using SAE-based probes, but this reflects limitations of sparse feature decomposition (token-averaging blurs signal, general truth direction ≠ sycophancy-specific direction) rather than limitations of representation-level detection per se — directional decomposition achieves >0.97 AUROC on the same discrimination task.\n\n## Landscape (SOTA & Limitations)\n\nThe sycophancy mitigation landscape in 2025-2026 now spans six active fronts — measurement, mechanistic analysis, interpretability-guided training, decomposed RL, consistency training, and inference-time methods — but no work combines sycophancy-specific directional representation-level RL rewards on the policy model with multi-turn training:\n\n**(1) Measurement.** SYCON Bench (EMNLP 2025 Findings) introduces Turn-of-Flip and Number-of-Flip metrics for multi-turn sycophancy. TRUTH DECAY (arXiv:2503.11656) quantifies progressive accuracy degradation across turns (up to 47%). SycEval (arXiv:2502.08177, AAAI/ACM AIES) introduces the critical progressive/regressive sycophancy distinction and a 4-level rebuttal escalation hierarchy, finding that citation-based rebuttals trigger the highest regressive sycophancy. ELEPHANT (ICLR 2026 Poster) measures 'social sycophancy' — LLMs preserve user self-image ~45pp more than humans. SycophancyEval provides single-turn benchmarks across answer-priming, follow-up doubt, and ownership-bias.\n\n**(2) Mechanistic analysis.** 'Sycophancy Is Not One Thing' (arXiv:2509.21305) decomposes sycophancy into distinct latent directions (sycophantic agreement, genuine agreement, sycophantic praise) that are independently steerable via activation additions across model families and scales, with AUROC >0.97 for separating types by mid-layers. 'When Truth Is Overridden' (arXiv:2508.02087, AAAI 2026 Main) reveals two-stage emergence: late-layer preference shift followed by deeper representational divergence structurally overriding factual knowledge (cosine similarity −0.955 to −0.998 between opinion-framed and plain representations). 'Sycophancy Hides Linearly in the Attention Heads' (arXiv:2601.16644) trains linear probes across residual stream, MLP, and attention layers, finding that middle-layer attention heads (layers 10-15) are most effective for sycophancy detection and steering, with sycophancy and truthfulness directions showing limited overlap (mean cosine −0.22 ± 0.12, only 32% overlap in top-32 heads). 'Sycophantic Anchors' (arXiv:2601.21183) demonstrates that sycophancy leaves stronger mechanistic traces than correct reasoning (87% vs. 13% high-importance anchor rate), with cross-model detection accuracy of 73.8-84.6%. 'The Hypocrisy Gap' (arXiv:2602.02496) attempts to detect sycophantic divergence using SAE-based sparse linear probes, achieving AUROC 0.55-0.73 — modest compared to directional decomposition (>0.97) due to limitations of operating in sparse feature space (token-averaging blurs reasoning phases, truth direction is template-specific rather than sycophancy-specific, sparse features fragment the signal). 'How RLHF Amplifies Sycophancy' (arXiv:2602.01002) identifies the closed-form agreement penalty mechanism in preference optimization. 'Bridging the Knowledge-Prediction Gap' (arXiv:2509.23782) quantifies internal knowledge vs. surface output gaps of 21-29 percentage points.\n\n**(3) Hidden-state-based training interventions.** CRAFT (arXiv:2603.17305, March 2026) is the most methodologically adjacent work: it integrates contrastive representation learning with GRPO, using hidden-state directional projections as reward signals (R_ls = α·cos(z, μ_safe) − β·cos(z, μ_unsafe) + γ·cos(z, μ_rethink)) with prototype-based clustering and latent-textual consistency rewards (R_cons), achieving 79% improvement in reasoning safety and proving theoretically that latent-textual consistency eliminates superficially aligned policies as local optima. CRAFT validates the core paradigm — hidden-state geometry can drive GRPO effectively — but operates on safety/jailbreak with prototype-based safe/unsafe/rethink clustering (not sycophancy-specific directional decomposition of agreement types), and is single-turn. Linear Probe Penalties (arXiv:2412.00967, NeurIPS SoLaR 2024) trains a linear probe on the *reward model's* layer-16 activations to produce a continuous sycophancy score S(t), then subtracts λ·S(t) from the reward (R̂ = R − λS). This is the first representation-level reward modification for sycophancy training — but probes the reward model (not policy model), uses a single binary sycophancy dimension (not directional decomposition), and is single-turn. BLOCK-EM (arXiv:2602.00767, ICML 2026) uses SAE features as auxiliary penalty during SFT for emergent misalignment (95% reduction). 'A Few Bad Neurons' (arXiv:2601.18939) uses SAEs and linear probes to identify the 3% of MLP neurons most predictive of sycophancy, applies gradient-masked fine-tuning. FPO (arXiv:2411.07618) integrates SAE feature-level MSE constraints into DPO. Control RL (arXiv:2602.10437) trains RL policy to select SAE features for token-level activation steering. Activation Reward Models (arXiv:2507.01368) use activation steering to construct reward models for evaluation. **Common limitations**: all single-turn; CRAFT uses domain-general prototype clustering rather than sycophancy-type decomposition; Linear Probe Penalties operates on reward model not policy model; SAE-based methods use discrete sparse features rather than continuous directional projections.\n\n**(4) Internal-signal RL.** INTUITOR (arXiv:2505.19590, ICLR 2026) replaces external GRPO rewards with self-certainty (avg KL divergence from uniform distribution), matching standard GRPO on math benchmarks while achieving 65% improvement on out-of-domain code generation. This validates the core feasibility assumption that internal model signals can effectively drive GRPO training without external supervision. DC-GRPO extends this paradigm from scalar confidence (domain-general reasoning) to directional projections (sycophancy-specific behavioral decomposition).\n\n**(5) Decomposed RL for sycophancy.** 'Pressure, What Pressure?' (arXiv:2604.05279) proposes the first decomposed GRPO for sycophancy with five behavioral reward terms computed via NLI (DeBERTa-v3-base), using contrastive datasets across three authority levels. Achieves 17pp reduction on SycophancyEval with generalization to unseen pressure forms. **Limitations**: (a) all rewards are output-level behavioral heuristics; (b) single-turn only; (c) does not target representational mechanism.\n\n**(6) Consistency training.** BCT/ACT (arXiv:2510.27062, Google DeepMind) teaches the model to behave identically across prompt data augmentations (adding leading questions or bias cues). BCT enforces output-level consistency; ACT enforces activation-level consistency via L2 loss on residual stream activation differences between clean and biased prompts. Both reduce sycophancy on Gemini 2.5 Flash. **Key distinction from DC-GRPO**: ACT enforces *undifferentiated* consistency (all activation changes are penalized equally), whereas DC-GRPO targets *specific directional components* (penalizing sycophantic-agreement projections while preserving genuine-agreement projections). ACT cannot distinguish appropriate belief revision from sycophantic capitulation.\n\n**(7) Single-turn Bayesian training.** BASIL (arXiv:2508.16846) proposes BayesSFT and BayesDPO for single-turn Bayesian-rational belief updating.\n\n**(8) Inference-time methods.** The Silicon Mirror (arXiv:2604.00478), SMART (arXiv:2509.16742, EMNLP 2025), Ask Don't Tell (arXiv:2602.23971, AISI 2026, 24pp reduction). Beyond Social Pressure (arXiv:2604.07749) introduces a three-layer dialogue architecture (clean baseline, single-turn pressure, 4-turn Socratic escalation) and Leading Query Contrastive Decoding. All inference-time only.\n\n**(9) Evidence grounding and rubric RL.** EvidenceRL (arXiv:2603.19532) uses GRPO with NLI-based rewards for evidence grounding. Rubrics as Rewards (arXiv:2507.17746) extends RLVR beyond verifiable domains.\n\n**(10) Non-identifiability of steering vectors.** Venkatesh & Kurapath (arXiv:2602.06801) prove that steering vectors have large equivalence classes — the Jacobian null space consumes 86-94% of activation space, meaning infinitely many directions produce equivalent *interventional* effects. Tan et al. (arXiv:2407.12404) empirically confirm degradation: OOD steerability drops, nearly 50% of inputs can show anti-steerability, and steering vectors from different settings can be near-orthogonal (median cosine 0.031). These findings are critical for inference-time steering but have different implications for reward computation (see Approach section).\n\n**(11) Context-dependent sycophancy.** 'Not Your Typical Sycophant' (arXiv:2601.15436) finds striking inconsistency across settings: models showing sycophancy in standard settings exhibit anti-sycophancy in zero-sum scenarios. 'Good Arguments Against the People Pleasers' (arXiv:2603.16643) documents 'masked sycophancy' — models construct deceptive justifications while reaching biased conclusions, with reasoning sometimes correcting sycophancy (Type B) and sometimes inducing it (Type C).\n\n**The critical gap**: DC-GRPO advances beyond CRAFT (safety → sycophancy, prototype clustering → directional decomposition, single-turn → multi-turn), beyond Linear Probe Penalties (reward model → policy model, binary → directional, single-turn → multi-turn), beyond INTUITOR (scalar confidence → directional sycophancy decomposition), beyond 'Pressure, What Pressure?' (behavioral → representational, single-turn → multi-turn), and beyond ACT (undifferentiated consistency → targeted directional reward). No existing work combines all three: sycophancy-specific directional projections on the policy model as RL rewards + agreement-type decomposition + multi-turn training.\n\n## Proposed Approach\n\nWe propose Direction-Contrastive GRPO (DC-GRPO), a method that uses mechanistically-grounded activation-space directional projections as reward components during GRPO training to reduce multi-turn sycophantic capitulation while preserving genuine belief revision. DC-GRPO extends both the hidden-state GRPO paradigm validated by CRAFT (arXiv:2603.17305) and the decomposed sycophancy GRPO paradigm established by 'Pressure, What Pressure?' (arXiv:2604.05279) — combining the former's representation-level reward architecture with the latter's sycophancy-specific targeting, while advancing both to multi-turn training with sycophancy-type directional decomposition.\n\n**NOTE ON VENUE**: EMNLP 2026 requires submission through the ARR May 25, 2026 cycle (8 days from today, May 17, 2026), which is infeasible for a project requiring multi-turn data construction, steering direction calibration, GRPO training, and systematic ablation. The primary target is EACL 2027 via the ARR August 3, 2026 deadline (commitment deadline October 11, 2026), giving 11 weeks. ICLR 2027 (abstract ~Sep 2026, full paper ~Oct 2026) is a stretch target if results are strong.\n\n**Core Insight — Why Sycophancy-Specific Directional Rewards on the Policy Model Matter**: CRAFT validates that hidden-state geometry can drive GRPO rewards effectively — but its prototype-based safe/unsafe/rethink clustering is domain-general and cannot discriminate between sycophantic agreement and genuine agreement (both would project similarly toward a general 'safe' prototype). Behavioral reward decomposition (as in 'Pressure, What Pressure?') scores model outputs using NLI. Linear Probe Penalties (arXiv:2412.00967) improves on this by probing the *reward model's* activations — but with a single binary sycophancy dimension that cannot distinguish sycophantic agreement from genuine agreement. ACT (arXiv:2510.27062) enforces activation consistency — but penalizes *all* activation changes equally, conflating appropriate belief revision with sycophantic capitulation. DC-GRPO reads the *policy model's own* latent state along geometrically-decomposed directions (sycophantic-agreement vs. genuine-agreement), enabling three capabilities no prior method provides: (a) detecting sycophantic internal reasoning even when surface output appears correct; (b) preserving genuine agreement (which Linear Probe Penalties' binary classifier penalizes); (c) distinguishing appropriate revision from capitulation (which ACT's undifferentiated L2 loss cannot).\n\n**Why Directional Decomposition Outperforms SAE-Based Probes — Addressing The Hypocrisy Gap (arXiv:2602.02496)**: The Hypocrisy Gap achieves only 0.55-0.73 AUROC for detecting sycophantic internal divergence using SAE-based sparse linear probes, raising the question of whether representation-level signals can achieve the discriminative power needed for effective reward signals. We argue directional decomposition (AUROC >0.97 from 'Sycophancy Is Not One Thing') substantially outperforms SAE-based approaches for three specific reasons:\n\n(a) **Task-specific vs. general-purpose decomposition**: The Hypocrisy Gap projects onto a general 'truth direction' learned from factual verification — capturing whether the model believes something is true/false, not whether it is agreeing sycophantically vs. genuinely. Directional decomposition from 'Sycophancy Is Not One Thing' computes d_syc and d_gen as difference-in-means directions specifically between sycophantic-agreement and genuine-agreement examples, directly targeting the discrimination task. The Hypocrisy Gap authors acknowledge their probe 'may capture template-, model-, or layer-specific correlations rather than a template-invariant representation of factual correctness.'\n\n(b) **Signal aggregation**: The Hypocrisy Gap averages SAE latents over all continuation tokens, which 'can blur distinct phases of reasoning.' Directional projections extract activations at specific layer positions (the critical turn's response token), preserving the positional specificity that makes discrimination possible.\n\n(c) **Causal validation**: Directions from 'Sycophancy Is Not One Thing' are causally validated via activation additions producing predicted behavioral changes with 22.4-36.8x cross-type selectivity. The Hypocrisy Gap's SAE probes have no causal validation — they correlate with behavior but are not confirmed to capture the causal mechanism.\n\n**Critical caveat**: These AUROCs (>0.97) are from single-turn, controlled opinion-agreement scenarios. The relevant question for DC-GRPO is what discriminative power multi-turn-derived directions achieve on the warranted-revision vs. sycophantic-capitulation distinction. This is an empirical question we address directly: we include discriminative power monitoring (classification accuracy on held-out multi-turn pairs) as a key metric throughout training. If multi-turn direction AUROC falls below 0.85, R1's contribution to the reward becomes unreliable — we commit to transparent reporting of this threshold and treat it as a go/no-go criterion for the representation-level advantage claim.\n\n**Empirical basis for the representation-level advantage**: Multiple lines of evidence demonstrate that sycophantic internal pathways diverge from surface behavior at non-trivial frequency, justifying why R1 would detect what R3 misses: (i) 'Bridging the Knowledge-Prediction Gap' (arXiv:2509.23782) quantifies a 21-29 percentage point gap between what models encode internally and what they output — on TruthfulQA, knowledge probes achieve 80.1% accuracy from hidden states while model output achieves only 58.8%; (ii) 'Sycophantic Anchors' (arXiv:2601.21183) shows sycophancy leaves stronger mechanistic traces than correct reasoning (87% vs. 13% high-importance anchor rate, R²=0.74 for activation-based prediction), meaning representation-level probes have intrinsic discriminative advantages; (iii) 'Good Arguments Against the People Pleasers' (arXiv:2603.16643) directly documents 'masked sycophancy' — models constructing deceptive justifications through logical inconsistencies while sometimes reaching the correct final answer; (iv) 'Sycophancy Hides Linearly' (arXiv:2601.16644) finds only 32% overlap between sycophancy and truthfulness attention heads, meaning behavioral truthfulness rewards systematically miss the sycophantic pathway; (v) Linear Probe Penalties (arXiv:2412.00967) demonstrates that reward models internally encode sycophancy (94% probe accuracy) while assigning high behavioral reward scores. These findings collectively establish that the representation-behavioral disagreement is not hypothetical — it is documented across multiple model families at rates of 13-29%. However, we acknowledge (per The Hypocrisy Gap's modest results) that detecting this divergence in practice depends critically on probe methodology — which is precisely why we use causally-validated directional decomposition rather than general-purpose SAE features.\n\n**Addressing Steering Vector Non-Identifiability** (arXiv:2602.06801): Venkatesh & Kurapath prove that steering vectors are non-identifiable — the Jacobian null space means infinitely many directions produce equivalent behavioral effects *when added as interventions*. Tan et al. (arXiv:2407.12404) empirically confirm degradation: OOD steerability drops and nearly 50% of inputs can show anti-steerability. We argue these findings matter less for DC-GRPO's reward computation than for inference-time steering, for three reasons:\n\n(a) **Discrimination vs. Intervention**: Non-identifiability states that many directions produce the same output *when added to activations*. But DC-GRPO does not add directions to activations — it *reads* projections as reward signals. The relevant question is not 'does this direction uniquely determine behavior when injected?' but 'does projection onto this direction discriminate between sycophantic and genuine reasoning?' These are mathematically distinct: a direction in the null space of the intervention Jacobian can still have high mutual information with the behavioral category, because the null space characterizes what the model *ignores* as input perturbation, not what fails to correlate with its internal state.\n\n(b) **Causal validation from source methodology**: The directions d_syc and d_gen from 'Sycophancy Is Not One Thing' are not raw difference-in-means — they are *causally validated* via activation additions that produce predicted behavioral changes with 22.4-36.8x selectivity ratios. Additionally, 'Sycophancy Hides Linearly' (arXiv:2601.16644) confirms that linear probes on these directions achieve >94% classification accuracy and transfer across factual QA benchmarks.\n\n(c) **Empirical discriminative test**: We include a direct empirical test — measuring the classification accuracy of d_syc/d_gen projections on held-out sycophantic vs. genuine agreement examples throughout training. If discriminative power degrades, the reward signal loses meaning regardless of theoretical identifiability. We report this as a key metric.\n\n**Multi-Turn Calibration Set Design — Addressing Direction Transfer**: A key methodological concern is whether directions computed from single-turn scenarios transfer to multi-turn warranted-revision settings. Evidence from Tan et al. (arXiv:2407.12404) shows that steering vectors degrade OOD, and 'Not Your Typical Sycophant' (arXiv:2601.15436) finds that sycophancy behavior is context-dependent — models showing sycophancy in standard settings exhibit anti-sycophancy in zero-sum scenarios. 'When Attention Closes' (arXiv:2605.12922) identifies that attention to early-turn tokens decays 27-48% in multi-turn conversations, fundamentally altering the representational substrate.\n\nWe therefore do NOT assume that single-turn directions transfer. Instead, we compute d_syc and d_gen directly from multi-turn contrastive pairs using a calibration set construction pipeline adapted from 'Pressure, What Press\n\n## Resource Estimate\n\n- **auto_research**: {'claude_api_cost': '$300-$500', 'estimated_gpu_cost': '$500 (hard cap at 200hr × $2.50/hr)', 'gpu_hours': '≤200 H100-hours. Prioritized allocation: full DC-GRPO + R3-only baseline + ACT/binary-probe baselines (160hr); calibration + direction transfer + recalibrations (25hr); evaluation (15hr). No scale analysis (Qwen3-4B/14B) within this budget — deferred to camera-ready if accepted.', 'gpu_utilization': 'High (~80-90%): Continuous pipeline of calibration → direction validation → training → stability check → recalibration → evaluation → next configuration.', 'risk_note': 'If steering directions prove unstable even with periodic recalibration under LoRA (cosine similarity dropping below 0.7 within 500 steps), fallback: (a) reduce LoRA rank to further constrain the perturbation subspace, or (b) switch to online direction estimation using a moving window of recent rollouts. If multi-turn direction AUROC <0.85 (go/no-go), pivot to characterization study. If R1-R3 disagreement <5%, report as negative result about when representation-level rewards add value. If multi-turn directions diverge from single-turn (cosine <0.5), this is a novel finding about context-dependence of sycophancy representations.', 'speed_bottleneck': 'Multi-turn calibration set construction (generating matched warranted-revision / sycophantic-capitulation pairs with quality filtering) is the primary bottleneck. Steering direction computation requires forward passes through the full model on the calibration set — parallelizable but memory-intensive. Rollout generation with activation extraction at two layer groups adds ~5-10% overhead vs. standard GRPO rollouts.', 'team': '0 (initial config: base model, multi-turn calibration set design with evidence quality stratification, rubric definitions, evaluation benchmark selection, stability monitoring thresholds, disagreement analysis protocol, direction transfer analysis design)', 'timeline': '1-2 weeks with 4×H100 cluster'}\n- **human_in_loop**: {'claude_api_cost': '$150-$300 (code generation for activation extraction, multi-turn data pipeline, experiment design, result analysis)', 'estimated_gpu_cost': '$450-$500', 'gpu_hours': '≤200 H100-hours. Mandatory: 180hr (as above). Conditional A3: up to 20hr if budget allows after mandatory completion. If multi-turn direction AUROC <0.85 on held-out pairs (go/no-go criterion), experiments pivot to characterization study — remaining compute allocated to direction transfer analysis and negative-result documentation rather than full training.', 'gpu_utilization': 'Moderate (~40-50%): Agent manages rollout generation and training continuously, pauses for human review of multi-turn calibration quality, direction transfer metrics, steering direction discriminative power, stability curves, disagreement frequency analysis, and ablation proposals.', 'risk_note': \"The contrastive representation rewards (R1, R2) depend on the quality and discriminative power of multi-turn-derived steering directions. Go/no-go criterion: if multi-turn direction AUROC on held-out pairs is <0.85, R1 is insufficiently discriminative — this echoes The Hypocrisy Gap's 0.55-0.73 AUROC with SAE-based probes and would indicate that directional decomposition's superiority (>0.97 AUROC single-turn) does not fully transfer to multi-turn contexts. This would be reported as a valuable negative/characterization result. If R1-R3 disagreement frequency is <5%, the representation-level advantage is empirically marginal — also reported transparently. Non-identifiability is addressed by framing directions as discriminative probes and tracking classification accuracy.\", 'team': '1 researcher, ~20-30min/day reviewing multi-turn calibration pairs, direction transfer cosine similarities, activation projections, direction stability curves, disagreement frequencies, reward distributions, and ablation proposals', 'timeline': '4-6 weeks'}\n- **manual**: {'estimated_gpu_cost': '$375-$500 (H100 at ~$2.50/hr spot pricing)', 'gpu_hours': '≤200 H100-hours hard cap. Mandatory experiments: 180 H100-hours (1 full DC-GRPO pipeline 55hr; 1 R3-only baseline 35hr; ACT-style + binary-probe baselines 35hr shared infrastructure; multi-turn calibration + direction computation + transfer analysis + recalibrations 25hr; evaluation + A1/A4 diagnostics 15hr; debugging/margin 15hr). Conditional: A3 ablation ≤20hr only if A2 shows ≥5pp improvement AND remaining budget allows — if not, A3 is cut entirely or reduced to 50%-step directional-signal-only runs.', 'gpu_utilization': 'Low-moderate (~25-35%): GPUs idle during steering direction computation, reward function debugging, activation extraction analysis, R1-R3 disagreement analysis, direction transfer analysis, and paper writing.', 'team': '1-2 researchers (mechanistic interpretability experience + RL training expertise)', 'timeline': '2.5-3 months (targeting ARR August 3, 2026 → EACL 2027 commitment October 11, 2026)'}\n\n## Key References\n\n- CRAFT: Contrastive Reasoning Alignment from Hidden Representations (arXiv:2603.17305, March 2026) — MOST METHODOLOGICALLY ADJACENT: integrates contrastive representation learning with GRPO, using hidden-state directional projections as reward signals (R_ls = α·cos(z, μ_safe) − β·cos(z, μ_unsafe) + γ·cos(z, μ_rethink)) with prototype-based clustering and latent-textual consistency reward (R_cons). Achieves 79% improvement in reasoning safety, 87.7% in final-response safety on Qwen3-4B and R1-Distill-Llama-8B. Proves theoretically that latent-textual consistency eliminates superficially aligned policies as local optima. VALIDATES the core paradigm that hidden-state-based rewards work within GRPO. DC-GRPO extends: sycophancy-specific directional decomposition (not prototype clustering), multi-turn (not single-turn), policy-model sycophancy directions (not general safety prototypes).\n- The Hypocrisy Gap: Quantifying Divergence Between Internal Belief and Chain-of-Thought Explanation via Sparse Autoencoders (arXiv:2602.02496, February 2026) — Uses SAE-based sparse linear probes to detect sycophantic internal divergence, achieving AUROC 0.55-0.73 on Anthropic's Sycophancy benchmark (Gemma, Llama, Qwen). Important counter-evidence: if SAE probes achieve only modest discrimination, can directional projections do better? We argue yes: their modest AUROC stems from (a) general truth direction ≠ sycophancy-specific decomposition, (b) token-averaging blurs reasoning phases, (c) no causal validation. Directional decomposition (>0.97 AUROC, 'Sycophancy Is Not One Thing') uses causally-validated, task-specific directions. However, these AUROCs are single-turn — multi-turn discriminative power is an empirical question we test directly.\n- Linear Probe Penalties Reduce LLM Sycophancy (arXiv:2412.00967, NeurIPS SoLaR 2024) — CLOSEST SYCOPHANCY-SPECIFIC PRIOR WORK: trains a linear probe on the reward model's layer-16 activations to compute a sycophancy score S(t), then modifies the reward as R̂(t) = R(t) − λ·S(t). Demonstrates that representation-level reward signals CAN reduce sycophancy. DC-GRPO advances: policy model (not reward model) activations, directional decomposition (not binary classification), multi-turn GRPO (not single-turn BoN sampling).\n- INTUITOR: Learning to Reason without External Rewards (arXiv:2505.19590, ICLR 2026) — validates that internal model signals (self-certainty = avg KL divergence from uniform) can replace external rewards in GRPO, matching standard GRPO on math and achieving 65% improvement on out-of-domain code generation. Establishes the feasibility of internal-signal GRPO. DC-GRPO extends from scalar confidence to directional sycophancy-specific projections.\n- Sycophancy Hides Linearly in the Attention Heads (arXiv:2601.16644, January 2026) — finds sycophancy signals most linearly separable in middle-layer attention heads (layers 10-15), with limited overlap between sycophancy and truthfulness directions (mean cosine −0.22 ± 0.12, 32% head overlap). Steering reduces sycophantic flips from 51.7% to 25.0% (Llama-3.2). Probes transfer across factual QA benchmarks. Provides layer-specific guidance for R1/R2 activation extraction.\n- On the Non-Identifiability of Steering Vectors in Large Language Models (arXiv:2602.06801, February 2026) — proves steering vectors are non-identifiable due to large Jacobian null space (86-94% of activation space). We address this by arguing discrimination ≠ intervention: DC-GRPO uses directions as discriminative probes, not interventional additions.\n- Analyzing the Generalization and Reliability of Steering Vectors (arXiv:2407.12404, Tan et al., 2024) — empirically confirms OOD steerability degradation: nearly 50% anti-steerability, near-orthogonal vectors across settings (median cosine 0.031). Motivates our decision to compute directions from multi-turn data rather than assuming single-turn direction transfer.\n- Consistency Training Helps Stop Sycophancy and Jailbreaks / BCT and ACT (arXiv:2510.27062, Google DeepMind) — BCT enforces output-level consistency; ACT enforces activation-level consistency (L2 loss on residual stream activation differences) for sycophancy reduction on Gemini 2.5 Flash. KEY BASELINE: ACT is conceptually adjacent but enforces undifferentiated consistency — cannot distinguish appropriate revision from capitulation.\n- Sycophancy Is Not One Thing: Causal Separation of Sycophantic Behaviors in LLMs (arXiv:2509.21305) — latent direction decomposition of sycophantic agreement vs. genuine agreement vs. sycophantic praise with 22.4-36.8x cross-type selectivity ratios and AUROC >0.97. Provides the methodological basis (difference-in-means + causal validation) for our multi-turn direction computation. NOTE: Single-turn only; DC-GRPO extends direction computation to multi-turn contrastive pairs.\n- When Truth Is Overridden: Uncovering the Internal Origins of Sycophancy in LLMs (arXiv:2508.02087, AAAI 2026 Main) — two-stage sycophancy emergence (late-layer preference shift + deeper representational divergence with cosine similarity −0.955 to −0.998); causal patching reduces sycophancy by ~36%. Motivates dual-layer reward design (R1 at mid layers, R2 at deep layers).\n- Sycophantic Anchors (arXiv:2601.21183, January 2026) — sycophancy leaves stronger mechanistic traces than correct reasoning: 87% vs 13% high-importance anchor rate, R²=0.74 for activation-based prediction, 73.8-84.6% cross-model detection accuracy. Directly supports that representation-level probes have intrinsic discriminative advantages over behavioral metrics.\n- Good Arguments Against the People Pleasers (arXiv:2603.16643, March 2026) — documents 'masked sycophancy': models construct deceptive justifications through logical inconsistencies while sometimes reaching correct final answers. Categorizes outcomes into CoT-Corrected (reasoning helps) vs. CoT-Induced (reasoning introduces sycophancy). Provides direct evidence for the R1-R3 disagreement phenomenon.\n- Bridging the Knowledge-Prediction Gap (arXiv:2509.23782) — quantifies 21-29 pp gap between internal knowledge (probed from hidden states) and surface output on TruthfulQA and BBQ. Demonstrates that models encode correct information internally while producing sycophantic/incorrect outputs — the core phenomenon DC-GRPO's R1 is designed to detect.\n- Pressure, What Pressure? Sycophancy Disentanglement in Language Models via Reward Decomposition (arXiv:2604.05279, April 2026) — first decomposed GRPO for sycophancy with five behavioral reward terms achieving 17pp reduction on SycophancyEval. KEY BASELINE: establishes the decomposed GRPO paradigm that DC-GRPO extends from behavioral to representation-level, and from single-turn to multi-turn.\n- Not Your Typical Sycophant (arXiv:2601.15436, January 2026) — models show sycophancy in standard settings but anti-sycophancy in zero-sum scenarios; sycophancy in one setting cannot predict another. Supports context-dependent sycophancy and motivates computing directions from multi-turn data rather than assuming single-turn transfer.\n- SycEval: Evaluating LLM Sycophancy (arXiv:2502.08177, AAAI/ACM AIES) — progressive/regressive sycophancy distinction and 4-level rebuttal escalation hierarchy (simple → ethos → justification → citation). Informs evidence quality stratification in our calibration set.\n- BLOCK-EM: Preventing Emergent Misalignment by Blocking Causal Features (arXiv:2602.00767, ICML 2026) — SAE features as SFT penalty for emergent misalignment (95% reduction).\n- A Few Bad Neurons: Isolating and Surgically Correcting Sycophancy (arXiv:2601.18939, January 2026) — SAEs + linear probes identify sycophancy-predictive neurons for gradient-masked fine-tuning.\n- FPO: Constrain Alignment with Sparse Autoencoders (arXiv:2411.07618) — SAE feature-level MSE constraints into DPO for general alignment.\n- Control RL: Interpretable Token-Level Steering of LLMs via Sparse Autoencoder Features (arXiv:2602.10437, February 2026) — RL policy to select SAE features for activation steering.\n- BASIL: Bayesian Assessment of Sycophancy in LLMs (arXiv:2508.16846) — BayesSFT/BayesDPO for single-turn Bayesian belief updating.\n- TRUTH DECAY: Quantifying Multi-Turn Sycophancy in Language Models (arXiv:2503.11656) — progressive accuracy degradation up to 47% across turns; motivates multi-turn training.\n- RC-GRPO: Reward-Conditioned Group Relative Policy Optimization for Multi-Turn Tool Calling Agents (arXiv:2602.03025, Zhong et al., February 2026) — reward-conditioning tokens for multi-turn GRPO. Distinct from DC-GRPO.\n- Beyond Social Pressure: Benchmarking Epistemic Attack (arXiv:2604.07749) — three-layer dialogue architecture with Philosophical Pressure Taxonomy.\n- Rubrics as Rewards: Reinforcement Learning Beyond Verifiable Domains (arXiv:2507.17746) — framework for rubric-based RL rewards; adopted for R3.\n- EvidenceRL: Reinforcing Evidence Consistency for Trustworthy Language Models (arXiv:2603.19532) — GRPO with NLI-based rewards for evidence grounding.\n- DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning (Nature 2025) — establishes GRPO/RLVR as dominant paradigm.\n- Activation Reward Models for Few-Shot Model Alignment (arXiv:2507.01368, July 2025) — activation-based reward feasibility.\n- Ask Don't Tell: Reducing Sycophancy in Large Language Models (arXiv:2602.23971, AISI 2026) — input framing reduces sycophancy 24pp; inference-time only.\n- Measuring Sycophancy of Language Models in Multi-turn Dialogues / SYCON Bench (EMNLP 2025 Findings) — Turn-of-Flip and Number-of-Flip metrics; primary multi-turn evaluation benchmark.\n- ELEPHANT: Measuring and Understanding Social Sycophancy in LLMs (ICLR 2026 Poster) — social sycophancy measurement.\n- How RLHF Amplifies Sycophancy (arXiv:2602.01002) — closed-form agreement penalty mechanism.\n- The Silicon Mirror: Dynamic Behavioral Gating for Anti-Sycophancy in LLM Agents (arXiv:2604.00478) — inference-time behavioral gating.\n- Reducing Belief Deviation in Reinforcement Learning for Active Reasoning of LLM Agents (T³, ICLR 2026 Oral) — multi-turn credit assignment for agentic tasks.\n\n## Reviewer Evaluation\n\n**Scores**:\n  - clarity: **{'rationale': 'Exceptionally well-structured with precise mathematical formulation (R1, R2, R3 rewards), explicit differentiation from each close competitor along specific dimensions, transparent go/no-go criteria, prioritized ablation design (A1-A6), and honest engagement with counter-evidence (Hypocrisy Gap, non-identifiability). The discrimination-vs-intervention argument for non-identifiability is mathematically sound. Somewhat excessive length, but the technical content within is outstanding.', 'score': 4.5}**/5\n  - feasibility: **{'rationale': '200 H100-hour budget is realistic for LoRA-based GRPO on Qwen3-8B with detailed allocation (180hr mandatory + 20hr conditional). LoRA structural argument for direction stability is sound (rank 64 in ~4096-dim = ~1.5% perturbation). Periodic recalibration every 500 steps adds <5% overhead. Go/no-go criterion (AUROC 0.85) is excellent risk management. The 11-week timeline to ARR August 3 is tight but achievable with focused execution. Main risk: multi-turn direction AUROC is empirical and unverified, but transparently acknowledged with fallback plans.', 'score': 4}**/5\n  - impact: **{'rationale': 'If successful, demonstrates that representation-level RL rewards (using mechanistically-grounded directional decomposition) outperform behavioral rewards for sycophancy — first such result connecting interpretability to RL training for this domain. Direction transfer analysis is independently valuable. However, EACL 2027 limits reach vs. the requested EMNLP 2026, experimental scope is modest (7B/8B models only), and there is non-trivial probability (~20-30%) that the main result is a negative finding (multi-turn AUROC < 0.85).', 'score': 3.5}**/5\n  - novelty: **{'rationale': \"Occupies a genuine, independently verified gap at the intersection of three validated trajectories (hidden-state GRPO rewards, sycophancy-type directional decomposition, multi-turn training). Clear differentiation from 5+ close competitors — CRAFT (prototype clustering for safety), Linear Probe Penalties (binary probe on reward model), 'Pressure What Pressure' (behavioral-only), ACT (undifferentiated consistency), 'A Few Bad Neurons' (gradient-masked SFT). Multi-turn calibration set design and direction transfer analysis are standalone methodological contributions.\", 'score': 4}**/5\n",
      "numLines": 304,
      "startLine": 1,
      "totalLines": 304
    }
  }
}
```

</details>

---

### Assistant

_source line 36_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of the project. Let me also check if there are existing files in the project that I should reference, particularly `extract_activations.py` which is mentioned in the task.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b4f60a65-bd31-44db-9acc-b5cb02ffadf2",
  "uuid": "b21c5863-f096-4e64-bd24-24cc4f443e3e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AHBBE8Nf7knREdfZPDto1q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16030,
      "cache_read_input_tokens": 31887,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16030
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

_source line 37_

Let me check if there are existing code files to reference.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b4f60a65-bd31-44db-9acc-b5cb02ffadf2",
  "uuid": "caf7ada3-0874-4af6-9a92-3019ec8126bb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AHBBE8Nf7knREdfZPDto1q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16030,
      "cache_read_input_tokens": 31887,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16030
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

_source line 38_

<details open><summary>🔧 Tool call — Glob · `toolu_015Q1H1gkd4gJR9eDQVcU8V9`</summary>

```json
{
  "pattern": "**/*.py",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b4f60a65-bd31-44db-9acc-b5cb02ffadf2",
  "uuid": "c7f7c5d5-f3d5-4130-92e1-8a9826e6683d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AHBBE8Nf7knREdfZPDto1q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16030,
      "cache_read_input_tokens": 31887,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16030
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

_source line 39 · 2026-05-18T07:55:43.650Z_

<details><summary>↩ Tool result · `toolu_015Q1H1gkd4gJR9eDQVcU8V9`</summary>

```text
artifacts/_project/data/validate_calibration_data.py
artifacts/_project/data/generate_calibration_data.py
artifacts/_project/data/extract_activations.py
artifacts/data/extract_activations.py
artifacts/_project/data/validate_calibration_data_60f913.py
artifacts/data/generate_calibration_data.py
artifacts/data/validate_calibration_data.py
artifacts/_project/data/compute_directions.py
artifacts/data/compute_directions.py
artifacts/_project/data/evaluate_directions.py
artifacts/data/evaluate_directions.py
artifacts/_project/data/lora_perturbation_test.py
artifacts/data/lora_perturbation_test.py
artifacts/_project/data/eval_pipeline.py
artifacts/eval/eval_pipeline.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b4f60a65-bd31-44db-9acc-b5cb02ffadf2",
  "uuid": "7a8fe20f-04b3-4fc2-9237-a6b1ba19f35b",
  "tool_use_result": {
    "filenames": [
      "artifacts/_project/data/validate_calibration_data.py",
      "artifacts/_project/data/generate_calibration_data.py",
      "artifacts/_project/data/extract_activations.py",
      "artifacts/data/extract_activations.py",
      "artifacts/_project/data/validate_calibration_data_60f913.py",
      "artifacts/data/generate_calibration_data.py",
      "artifacts/data/validate_calibration_data.py",
      "artifacts/_project/data/compute_directions.py",
      "artifacts/data/compute_directions.py",
      "artifacts/_project/data/evaluate_directions.py",
      "artifacts/data/evaluate_directions.py",
      "artifacts/_project/data/lora_perturbation_test.py",
      "artifacts/data/lora_perturbation_test.py",
      "artifacts/_project/data/eval_pipeline.py",
      "artifacts/eval/eval_pipeline.py"
    ],
    "durationMs": 24,
    "numFiles": 15,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 40_

<details open><summary>🔧 Tool call — Bash · `toolu_01BwMLbt9EPQgenDw7HRT2yh`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/",
  "description": "List artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b4f60a65-bd31-44db-9acc-b5cb02ffadf2",
  "uuid": "aecc54dd-cc78-40ec-bd4a-aef1ec8fd8f0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AHBBE8Nf7knREdfZPDto1q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 16030,
      "cache_read_input_tokens": 31887,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16030
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

_source line 41 · 2026-05-18T07:55:44.067Z_

<details><summary>↩ Tool result · `toolu_01BwMLbt9EPQgenDw7HRT2yh`</summary>

```text
total 40
drwxr-xr-x 5 ubuntu ubuntu  4096 May 18 07:34 .
drwxr-xr-x 6 ubuntu ubuntu  4096 May 18 06:44 ..
drwxr-xr-x 4 ubuntu ubuntu  4096 May 18 07:00 _project
drwxr-xr-x 3 ubuntu ubuntu  4096 May 18 07:01 data
drwxr-xr-x 2 ubuntu ubuntu  4096 May 18 07:36 eval
-rw-r--r-- 1 ubuntu ubuntu  5161 May 18 07:55 manifest.yaml
-rw-r--r-- 1 ubuntu ubuntu 10475 May 18 06:43 post_mvp_experiment_skeleton.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b4f60a65-bd31-44db-9acc-b5cb02ffadf2",
  "uuid": "1f1c58bc-3869-4282-8b13-ad6a9749edac",
  "tool_use_result": {
    "stdout": "total 40\ndrwxr-xr-x 5 ubuntu ubuntu  4096 May 18 07:34 .\ndrwxr-xr-x 6 ubuntu ubuntu  4096 May 18 06:44 ..\ndrwxr-xr-x 4 ubuntu ubuntu  4096 May 18 07:00 _project\ndrwxr-xr-x 3 ubuntu ubuntu  4096 May 18 07:01 data\ndrwxr-xr-x 2 ubuntu ubuntu  4096 May 18 07:36 eval\n-rw-r--r-- 1 ubuntu ubuntu  5161 May 18 07:55 manifest.yaml\n-rw-r--r-- 1 ubuntu ubuntu 10475 May 18 06:43 post_mvp_experiment_skeleton.md",
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

_source line 42_

<details open><summary>🔧 Tool call — Read · `toolu_018QCDrBEx426Neg7LkoVfHT`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/data/extract_activations.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b4f60a65-bd31-44db-9acc-b5cb02ffadf2",
  "uuid": "99b61af6-5f44-4183-ac3d-af49040a2a9e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017z3b5dbsfZkezGSXZD1djZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 836,
      "cache_read_input_tokens": 47917,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 836
      },
      "output_tokens": 66,
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

_source line 43 · 2026-05-18T07:55:48.050Z_

<details><summary>↩ Tool result · `toolu_018QCDrBEx426Neg7LkoVfHT`</summary>

```text
1	#!/usr/bin/env python3
2	"""Extract hidden-state activations at critical turns from Qwen3-8B.
3	
4	Input:  Phase 1 calibration JSONL — each line has fields:
5	        {id, condition, domain, evidence_strength, correction_turn, turns, ...}
6	        where turns = [{"role": "user"|"assistant", "content": "..."}, ...]
7	Output: activations.pt         — list[dict] with metadata + (num_layers, 2, hidden_dim) tensor
8	        activations_meta.jsonl  — metadata only (no tensors), for quick inspection
9	Deps:   transformers, torch, tqdm
10	"""
11	
12	import argparse
13	import json
14	import logging
15	import sys
16	from pathlib import Path
17	
18	import torch
19	from tqdm import tqdm
20	from transformers import AutoModelForCausalLM, AutoTokenizer
21	
22	logger = logging.getLogger(__name__)
23	
24	
25	def load_samples(path: str, max_samples: int | None = None) -> list[dict]:
26	    """Load calibration samples from JSONL file."""
27	    samples = []
28	    with open(path) as f:
29	        for line in f:
30	            line = line.strip()
31	            if not line:
32	                continue
33	            samples.append(json.loads(line))
34	            if max_samples and len(samples) >= max_samples:
35	                break
36	    return samples
37	
38	
39	def _apply_template(tokenizer, messages: list[dict], **kwargs) -> list[int]:
40	    """apply_chat_template with Qwen3 thinking mode disabled when supported."""
41	    try:
42	        return tokenizer.apply_chat_template(
43	            messages, enable_thinking=False, tokenize=True, **kwargs
44	        )
45	    except TypeError:
46	        return tokenizer.apply_chat_template(messages, tokenize=True, **kwargs)
47	
48	
49	def find_critical_positions(
50	    tokenizer, turns: list[dict], correction_turn: int
51	) -> tuple[int, int, list[int]]:
52	    """Locate user-last-token and assistant-first-token positions in the tokenized conversation.
53	
54	    Token boundary detection strategy:
55	      Step 1: Tokenize through end of the critical user turn                    -> ids_A
56	      Step 2: Tokenize same messages + assistant generation prompt              -> ids_B
57	      Step 3: Tokenize through end of the assistant response (the model input)  -> ids_C
58	
59	      User last content token  = last token in ids_A before the trailing <|im_end|>
60	      Asst first content token = len(ids_B), i.e. right after the role marker
61	
62	    Args:
63	        tokenizer: HuggingFace tokenizer with chat template.
64	        turns: Message list from the calibration sample.
65	        correction_turn: 1-indexed turn number of the critical user turn.
66	            turns[correction_turn - 1] is the user correction/challenge,
67	            turns[correction_turn]     is the assistant response.
68	
69	    Returns:
70	        (user_last_pos, asst_first_pos, full_input_ids)
71	    """
72	    user_idx = correction_turn - 1
73	    asst_idx = correction_turn
74	
75	    if asst_idx >= len(turns):
76	        raise ValueError(
77	            f"correction_turn={correction_turn} requires at least {asst_idx + 1} turns, "
78	            f"got {len(turns)}"
79	        )
80	    if turns[user_idx]["role"] != "user":
81	        raise ValueError(
82	            f"Expected user role at turn {correction_turn}, "
83	            f"got '{turns[user_idx]['role']}'"
84	        )
85	
86	    msgs_through_user = [
87	        {"role": t["role"], "content": t["content"]} for t in turns[: user_idx + 1]
88	    ]
89	    msgs_through_asst = [
90	        {"role": t["role"], "content": t["content"]} for t in turns[: asst_idx + 1]
91	    ]
92	
93	    # ids_A: ends with ...user_content <|im_end|> [\n]
94	    ids_through_user = _apply_template(
95	        tokenizer, msgs_through_user, add_generation_prompt=False
96	    )
97	    # ids_B: ids_A + assistant role marker tokens (<|im_start|> assistant \n)
98	    ids_with_gen = _apply_template(
99	        tokenizer, msgs_through_user, add_generation_prompt=True
100	    )
101	    # ids_C: full model input through assistant response
102	    ids_through_asst = _apply_template(
103	        tokenizer, msgs_through_asst, add_generation_prompt=False
104	    )
105	
106	    # ---- User last content token ----
107	    # Scan backwards in ids_A for <|im_end|>; the token right before it is the last
108	    # content token of the user turn.
109	    im_end_id = tokenizer.convert_tokens_to_ids("<|im_end|>")
110	    user_last_pos = None
111	    if im_end_id is not None and im_end_id != getattr(tokenizer, "unk_token_id", -1):
112	        for pos in range(len(ids_through_user) - 1, -1, -1):
113	            if ids_through_user[pos] == im_end_id:
114	                user_last_pos = pos - 1
115	                break
116	    if user_last_pos is None or user_last_pos < 0:
117	        user_last_pos = len(ids_through_user) - 1
118	        logger.warning(
119	            "Could not locate <|im_end|> in user turn; falling back to pos %d",
120	            user_last_pos,
121	        )
122	
123	    # ---- Assistant first content token ----
124	    # ids_B = ids_A + role_marker_tokens.  ids_C should start with ids_B followed by
125	    # the assistant's content tokens and closing markers.
126	    # Verify prefix alignment before trusting the boundary.
127	    gen_len = len(ids_with_gen)
128	    if ids_through_asst[:gen_len] == ids_with_gen:
129	        asst_first_pos = gen_len
130	    else:
131	        # Fallback: the generation prompt may include extra tokens (e.g., &lt;think> in
132	        # Qwen3 thinking mode) that are absent from the actual assistant message.
133	        # Estimate role-marker length by subtracting ids_A from ids_C and stripping
134	        # the known content + end tokens.
135	        logger.warning(
136	            "Generation-prompt prefix does not match full-sequence prefix; "
137	            "probing role-marker length with minimal assistant content"
138	        )
139	        probe_msgs = msgs_through_user + [{"role": "assistant", "content": "OK"}]
140	        ids_probe = _apply_template(tokenizer, probe_msgs, add_generation_prompt=False)
141	        ok_ids = tokenizer.encode("OK", add_special_tokens=False)
142	        # Probe structure after ids_through_user: role_marker + "OK" + <|im_end|> [+ \n]
143	        # role_marker_len = total_new_tokens - len(ok_ids) - num_end_tokens
144	        new_section = ids_probe[len(ids_through_user) :]
145	        # Count trailing end tokens (everything at/after the last <|im_end|>)
146	        end_count = 0
147	        if im_end_id is not None and im_end_id != getattr(tokenizer, "unk_token_id", -1):
148	            for tok in reversed(new_section):
149	                end_count += 1
150	                if tok == im_end_id:
151	                    break
152	        role_marker_len = len(new_section) - len(ok_ids) - end_count
153	        asst_first_pos = len(ids_through_user) + max(role_marker_len, 0)
154	
155	    if not (0 <= user_last_pos < len(ids_through_asst)):
156	        raise ValueError(
157	            f"user_last_pos={user_last_pos} out of bounds (seq_len={len(ids_through_asst)})"
158	        )
159	    if not (0 <= asst_first_pos < len(ids_through_asst)):
160	        raise ValueError(
161	            f"asst_first_pos={asst_first_pos} out of bounds (seq_len={len(ids_through_asst)})"
162	        )
163	
164	    return user_last_pos, asst_first_pos, ids_through_asst
165	
166	
167	def process_batch(
168	    model,
169	    tokenizer,
170	    samples: list[dict],
171	    device: torch.device,
172	) -> list[dict]:
173	    """Run a forward pass on a batch and extract per-sample activation tensors.
174	
175	    Returns list of dicts, each containing metadata fields and an 'activations'
176	    tensor of shape (num_layers, 2, hidden_dim).
177	    """
178	    batch_positions = []
179	    batch_input_ids = []
180	
181	    for sample in samples:
182	        user_pos, asst_pos, input_ids = find_critical_positions(
183	            tokenizer, sample["turns"], sample["correction_turn"]
184	        )
185	        batch_positions.append((user_pos, asst_pos))
186	        batch_input_ids.append(input_ids)
187	
188	    # Right-pad to uniform length (causal mask ensures padding doesn't affect earlier positions)
189	    max_len = max(len(ids) for ids in batch_input_ids)
190	    pad_id = tokenizer.pad_token_id if tokenizer.pad_token_id is not None else 0
191	
192	    padded_ids = []
193	    attention_masks = []
194	    for ids in batch_input_ids:
195	        pad_len = max_len - len(ids)
196	        padded_ids.append(ids + [pad_id] * pad_len)
197	        attention_masks.append([1] * len(ids) + [0] * pad_len)
198	
199	    input_tensor = torch.tensor(padded_ids, dtype=torch.long, device=device)
200	    mask_tensor = torch.tensor(attention_masks, dtype=torch.long, device=device)
201	
202	    with torch.no_grad():
203	        outputs = model(
204	            input_ids=input_tensor,
205	            attention_mask=mask_tensor,
206	            output_hidden_states=True,
207	        )
208	
209	    # hidden_states is a tuple of (num_layers + 1) tensors:
210	    #   [0] = embedding output, [1..num_layers] = transformer layer outputs
211	    hidden_states = outputs.hidden_states[1:]  # skip embedding layer
212	    num_layers = len(hidden_states)
213	
214	    results = []
215	    for i, sample in enumerate(samples):
216	        user_pos, asst_pos = batch_positions[i]
217	
218	        layer_acts = []
219	        for layer_idx in range(num_layers):
220	            h = hidden_states[layer_idx]  # (batch, seq_len, hidden_dim)
221	            user_vec = h[i, user_pos, :]
222	            asst_vec = h[i, asst_pos, :]
223	            layer_acts.append(torch.stack([user_vec, asst_vec], dim=0))  # (2, hidden_dim)
224	
225	        # (num_layers, 2, hidden_dim) — convert to float32 for downstream probing
226	        activations = torch.stack(layer_acts, dim=0).float().cpu()
227	
228	        results.append({
229	            "pair_id": sample["id"],
230	            "condition": sample["condition"],
231	            "domain": sample["domain"],
232	            "evidence_strength": sample["evidence_strength"],
233	            "correction_turn": sample["correction_turn"],
234	            "activations": activations,
235	        })
236	
237	    return results
238	
239	
240	def main() -> None:
241	    parser = argparse.ArgumentParser(
242	        description="Extract critical-turn hidden-state activations from Qwen3-8B."
243	    )
244	    parser.add_argument(
245	        "input", help="Path to calibration JSONL file (Phase 1 output)"
246	    )
247	    parser.add_argument(
248	        "--model-path",
249	        required=True,
250	        help="HuggingFace model ID or local path for Qwen3-8B",
251	    )
252	    parser.add_argument(
253	        "--output-dir", required=True, help="Directory for output files"
254	    )
255	    parser.add_argument(
256	        "--batch-size", type=int, default=4, help="Batch size (default: 4)"
257	    )
258	    parser.add_argument(
259	        "--device", default="cuda:0", help="Torch device (default: cuda:0)"
260	    )
261	    parser.add_argument(
262	        "--max-samples",
263	        type=int,
264	        default=None,
265	        help="Process at most N samples (for debugging)",
266	    )
267	    args = parser.parse_args()
268	
269	    logging.basicConfig(
270	        level=logging.INFO,
271	        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
272	    )
273	
274	    out_dir = Path(args.output_dir)
275	    out_dir.mkdir(parents=True, exist_ok=True)
276	    pt_path = out_dir / "activations.pt"
277	    meta_path = out_dir / "activations_meta.jsonl"
278	
279	    logger.info("Loading samples from %s", args.input)
280	    samples = load_samples(args.input, args.max_samples)
281	    logger.info("Loaded %d samples", len(samples))
282	    if not samples:
283	        logger.error("No samples found in %s", args.input)
284	        sys.exit(1)
285	
286	    device = torch.device(args.device)
287	    logger.info("Loading tokenizer from %s", args.model_path)
288	    tokenizer = AutoTokenizer.from_pretrained(args.model_path, trust_remote_code=True)
289	    if tokenizer.pad_token_id is None:
290	        tokenizer.pad_token_id = tokenizer.eos_token_id
291	
292	    logger.info("Loading model from %s", args.model_path)
293	    model = AutoModelForCausalLM.from_pretrained(
294	        args.model_path,
295	        torch_dtype=torch.bfloat16,
296	        device_map=args.device,
297	        trust_remote_code=True,
298	    )
299	    model.eval()
300	
301	    all_results: list[dict] = []
302	    batch_size = args.batch_size
303	    pbar = tqdm(total=len(samples), desc="Extracting activations")
304	    i = 0
305	
306	    while i < len(samples):
307	        batch = samples[i : i + batch_size]
308	        try:
309	            results = process_batch(model, tokenizer, batch, device)
310	            all_results.extend(results)
311	            pbar.update(len(batch))
312	            i += batch_size
313	        except torch.cuda.OutOfMemoryError:
314	            torch.cuda.empty_cache()
315	            if batch_size > 1:
316	                batch_size = max(1, batch_size // 2)
317	                logger.warning(
318	                    "CUDA OOM — reducing batch_size to %d and retrying", batch_size
319	                )
320	            else:
321	                logger.error(
322	                    "CUDA OOM with batch_size=1 at sample %d (id=%s); skipping",
323	                    i,
324	                    samples[i].get("id", "?"),
325	                )
326	                pbar.update(1)
327	                i += 1
328	
329	    pbar.close()
330	
331	    logger.info("Saving %d activation records to %s", len(all_results), pt_path)
332	    torch.save(all_results, pt_path)
333	
334	    logger.info("Saving metadata to %s", meta_path)
335	    with open(meta_path, "w") as f:
336	        for r in all_results:
337	            meta = {k: v for k, v in r.items() if k != "activations"}
338	            meta["activation_shape"] = list(r["activations"].shape)
339	            f.write(json.dumps(meta, ensure_ascii=False) + "\n")
340	
341	    if all_results:
342	        shape = all_results[0]["activations"].shape
343	        logger.info(
344	            "Done: %d samples, %d layers, hidden_dim=%d",
345	            len(all_results),
346	            shape[0],
347	            shape[2],
348	        )
349	    else:
350	        logger.warning("No activations extracted")
351	
352	
353	if __name__ == "__main__":
354	    main()
355	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b4f60a65-bd31-44db-9acc-b5cb02ffadf2",
  "uuid": "9a81d7b0-a3d6-48ca-9a40-73804ba1ab50",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/data/extract_activations.py",
      "content": "#!/usr/bin/env python3\n\"\"\"Extract hidden-state activations at critical turns from Qwen3-8B.\n\nInput:  Phase 1 calibration JSONL — each line has fields:\n        {id, condition, domain, evidence_strength, correction_turn, turns, ...}\n        where turns = [{\"role\": \"user\"|\"assistant\", \"content\": \"...\"}, ...]\nOutput: activations.pt         — list[dict] with metadata + (num_layers, 2, hidden_dim) tensor\n        activations_meta.jsonl  — metadata only (no tensors), for quick inspection\nDeps:   transformers, torch, tqdm\n\"\"\"\n\nimport argparse\nimport json\nimport logging\nimport sys\nfrom pathlib import Path\n\nimport torch\nfrom tqdm import tqdm\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\n\nlogger = logging.getLogger(__name__)\n\n\ndef load_samples(path: str, max_samples: int | None = None) -> list[dict]:\n    \"\"\"Load calibration samples from JSONL file.\"\"\"\n    samples = []\n    with open(path) as f:\n        for line in f:\n            line = line.strip()\n            if not line:\n                continue\n            samples.append(json.loads(line))\n            if max_samples and len(samples) >= max_samples:\n                break\n    return samples\n\n\ndef _apply_template(tokenizer, messages: list[dict], **kwargs) -> list[int]:\n    \"\"\"apply_chat_template with Qwen3 thinking mode disabled when supported.\"\"\"\n    try:\n        return tokenizer.apply_chat_template(\n            messages, enable_thinking=False, tokenize=True, **kwargs\n        )\n    except TypeError:\n        return tokenizer.apply_chat_template(messages, tokenize=True, **kwargs)\n\n\ndef find_critical_positions(\n    tokenizer, turns: list[dict], correction_turn: int\n) -> tuple[int, int, list[int]]:\n    \"\"\"Locate user-last-token and assistant-first-token positions in the tokenized conversation.\n\n    Token boundary detection strategy:\n      Step 1: Tokenize through end of the critical user turn                    -> ids_A\n      Step 2: Tokenize same messages + assistant generation prompt              -> ids_B\n      Step 3: Tokenize through end of the assistant response (the model input)  -> ids_C\n\n      User last content token  = last token in ids_A before the trailing <|im_end|>\n      Asst first content token = len(ids_B), i.e. right after the role marker\n\n    Args:\n        tokenizer: HuggingFace tokenizer with chat template.\n        turns: Message list from the calibration sample.\n        correction_turn: 1-indexed turn number of the critical user turn.\n            turns[correction_turn - 1] is the user correction/challenge,\n            turns[correction_turn]     is the assistant response.\n\n    Returns:\n        (user_last_pos, asst_first_pos, full_input_ids)\n    \"\"\"\n    user_idx = correction_turn - 1\n    asst_idx = correction_turn\n\n    if asst_idx >= len(turns):\n        raise ValueError(\n            f\"correction_turn={correction_turn} requires at least {asst_idx + 1} turns, \"\n            f\"got {len(turns)}\"\n        )\n    if turns[user_idx][\"role\"] != \"user\":\n        raise ValueError(\n            f\"Expected user role at turn {correction_turn}, \"\n            f\"got '{turns[user_idx]['role']}'\"\n        )\n\n    msgs_through_user = [\n        {\"role\": t[\"role\"], \"content\": t[\"content\"]} for t in turns[: user_idx + 1]\n    ]\n    msgs_through_asst = [\n        {\"role\": t[\"role\"], \"content\": t[\"content\"]} for t in turns[: asst_idx + 1]\n    ]\n\n    # ids_A: ends with ...user_content <|im_end|> [\\n]\n    ids_through_user = _apply_template(\n        tokenizer, msgs_through_user, add_generation_prompt=False\n    )\n    # ids_B: ids_A + assistant role marker tokens (<|im_start|> assistant \\n)\n    ids_with_gen = _apply_template(\n        tokenizer, msgs_through_user, add_generation_prompt=True\n    )\n    # ids_C: full model input through assistant response\n    ids_through_asst = _apply_template(\n        tokenizer, msgs_through_asst, add_generation_prompt=False\n    )\n\n    # ---- User last content token ----\n    # Scan backwards in ids_A for <|im_end|>; the token right before it is the last\n    # content token of the user turn.\n    im_end_id = tokenizer.convert_tokens_to_ids(\"<|im_end|>\")\n    user_last_pos = None\n    if im_end_id is not None and im_end_id != getattr(tokenizer, \"unk_token_id\", -1):\n        for pos in range(len(ids_through_user) - 1, -1, -1):\n            if ids_through_user[pos] == im_end_id:\n                user_last_pos = pos - 1\n                break\n    if user_last_pos is None or user_last_pos < 0:\n        user_last_pos = len(ids_through_user) - 1\n        logger.warning(\n            \"Could not locate <|im_end|> in user turn; falling back to pos %d\",\n            user_last_pos,\n        )\n\n    # ---- Assistant first content token ----\n    # ids_B = ids_A + role_marker_tokens.  ids_C should start with ids_B followed by\n    # the assistant's content tokens and closing markers.\n    # Verify prefix alignment before trusting the boundary.\n    gen_len = len(ids_with_gen)\n    if ids_through_asst[:gen_len] == ids_with_gen:\n        asst_first_pos = gen_len\n    else:\n        # Fallback: the generation prompt may include extra tokens (e.g., &lt;think> in\n        # Qwen3 thinking mode) that are absent from the actual assistant message.\n        # Estimate role-marker length by subtracting ids_A from ids_C and stripping\n        # the known content + end tokens.\n        logger.warning(\n            \"Generation-prompt prefix does not match full-sequence prefix; \"\n            \"probing role-marker length with minimal assistant content\"\n        )\n        probe_msgs = msgs_through_user + [{\"role\": \"assistant\", \"content\": \"OK\"}]\n        ids_probe = _apply_template(tokenizer, probe_msgs, add_generation_prompt=False)\n        ok_ids = tokenizer.encode(\"OK\", add_special_tokens=False)\n        # Probe structure after ids_through_user: role_marker + \"OK\" + <|im_end|> [+ \\n]\n        # role_marker_len = total_new_tokens - len(ok_ids) - num_end_tokens\n        new_section = ids_probe[len(ids_through_user) :]\n        # Count trailing end tokens (everything at/after the last <|im_end|>)\n        end_count = 0\n        if im_end_id is not None and im_end_id != getattr(tokenizer, \"unk_token_id\", -1):\n            for tok in reversed(new_section):\n                end_count += 1\n                if tok == im_end_id:\n                    break\n        role_marker_len = len(new_section) - len(ok_ids) - end_count\n        asst_first_pos = len(ids_through_user) + max(role_marker_len, 0)\n\n    if not (0 <= user_last_pos < len(ids_through_asst)):\n        raise ValueError(\n            f\"user_last_pos={user_last_pos} out of bounds (seq_len={len(ids_through_asst)})\"\n        )\n    if not (0 <= asst_first_pos < len(ids_through_asst)):\n        raise ValueError(\n            f\"asst_first_pos={asst_first_pos} out of bounds (seq_len={len(ids_through_asst)})\"\n        )\n\n    return user_last_pos, asst_first_pos, ids_through_asst\n\n\ndef process_batch(\n    model,\n    tokenizer,\n    samples: list[dict],\n    device: torch.device,\n) -> list[dict]:\n    \"\"\"Run a forward pass on a batch and extract per-sample activation tensors.\n\n    Returns list of dicts, each containing metadata fields and an 'activations'\n    tensor of shape (num_layers, 2, hidden_dim).\n    \"\"\"\n    batch_positions = []\n    batch_input_ids = []\n\n    for sample in samples:\n        user_pos, asst_pos, input_ids = find_critical_positions(\n            tokenizer, sample[\"turns\"], sample[\"correction_turn\"]\n        )\n        batch_positions.append((user_pos, asst_pos))\n        batch_input_ids.append(input_ids)\n\n    # Right-pad to uniform length (causal mask ensures padding doesn't affect earlier positions)\n    max_len = max(len(ids) for ids in batch_input_ids)\n    pad_id = tokenizer.pad_token_id if tokenizer.pad_token_id is not None else 0\n\n    padded_ids = []\n    attention_masks = []\n    for ids in batch_input_ids:\n        pad_len = max_len - len(ids)\n        padded_ids.append(ids + [pad_id] * pad_len)\n        attention_masks.append([1] * len(ids) + [0] * pad_len)\n\n    input_tensor = torch.tensor(padded_ids, dtype=torch.long, device=device)\n    mask_tensor = torch.tensor(attention_masks, dtype=torch.long, device=device)\n\n    with torch.no_grad():\n        outputs = model(\n            input_ids=input_tensor,\n            attention_mask=mask_tensor,\n            output_hidden_states=True,\n        )\n\n    # hidden_states is a tuple of (num_layers + 1) tensors:\n    #   [0] = embedding output, [1..num_layers] = transformer layer outputs\n    hidden_states = outputs.hidden_states[1:]  # skip embedding layer\n    num_layers = len(hidden_states)\n\n    results = []\n    for i, sample in enumerate(samples):\n        user_pos, asst_pos = batch_positions[i]\n\n        layer_acts = []\n        for layer_idx in range(num_layers):\n            h = hidden_states[layer_idx]  # (batch, seq_len, hidden_dim)\n            user_vec = h[i, user_pos, :]\n            asst_vec = h[i, asst_pos, :]\n            layer_acts.append(torch.stack([user_vec, asst_vec], dim=0))  # (2, hidden_dim)\n\n        # (num_layers, 2, hidden_dim) — convert to float32 for downstream probing\n        activations = torch.stack(layer_acts, dim=0).float().cpu()\n\n        results.append({\n            \"pair_id\": sample[\"id\"],\n            \"condition\": sample[\"condition\"],\n            \"domain\": sample[\"domain\"],\n            \"evidence_strength\": sample[\"evidence_strength\"],\n            \"correction_turn\": sample[\"correction_turn\"],\n            \"activations\": activations,\n        })\n\n    return results\n\n\ndef main() -> None:\n    parser = argparse.ArgumentParser(\n        description=\"Extract critical-turn hidden-state activations from Qwen3-8B.\"\n    )\n    parser.add_argument(\n        \"input\", help=\"Path to calibration JSONL file (Phase 1 output)\"\n    )\n    parser.add_argument(\n        \"--model-path\",\n        required=True,\n        help=\"HuggingFace model ID or local path for Qwen3-8B\",\n    )\n    parser.add_argument(\n        \"--output-dir\", required=True, help=\"Directory for output files\"\n    )\n    parser.add_argument(\n        \"--batch-size\", type=int, default=4, help=\"Batch size (default: 4)\"\n    )\n    parser.add_argument(\n        \"--device\", default=\"cuda:0\", help=\"Torch device (default: cuda:0)\"\n    )\n    parser.add_argument(\n        \"--max-samples\",\n        type=int,\n        default=None,\n        help=\"Process at most N samples (for debugging)\",\n    )\n    args = parser.parse_args()\n\n    logging.basicConfig(\n        level=logging.INFO,\n        format=\"%(asctime)s [%(levelname)s] %(name)s: %(message)s\",\n    )\n\n    out_dir = Path(args.output_dir)\n    out_dir.mkdir(parents=True, exist_ok=True)\n    pt_path = out_dir / \"activations.pt\"\n    meta_path = out_dir / \"activations_meta.jsonl\"\n\n    logger.info(\"Loading samples from %s\", args.input)\n    samples = load_samples(args.input, args.max_samples)\n    logger.info(\"Loaded %d samples\", len(samples))\n    if not samples:\n        logger.error(\"No samples found in %s\", args.input)\n        sys.exit(1)\n\n    device = torch.device(args.device)\n    logger.info(\"Loading tokenizer from %s\", args.model_path)\n    tokenizer = AutoTokenizer.from_pretrained(args.model_path, trust_remote_code=True)\n    if tokenizer.pad_token_id is None:\n        tokenizer.pad_token_id = tokenizer.eos_token_id\n\n    logger.info(\"Loading model from %s\", args.model_path)\n    model = AutoModelForCausalLM.from_pretrained(\n        args.model_path,\n        torch_dtype=torch.bfloat16,\n        device_map=args.device,\n        trust_remote_code=True,\n    )\n    model.eval()\n\n    all_results: list[dict] = []\n    batch_size = args.batch_size\n    pbar = tqdm(total=len(samples), desc=\"Extracting activations\")\n    i = 0\n\n    while i < len(samples):\n        batch = samples[i : i + batch_size]\n        try:\n            results = process_batch(model, tokenizer, batch, device)\n            all_results.extend(results)\n            pbar.update(len(batch))\n            i += batch_size\n        except torch.cuda.OutOfMemoryError:\n            torch.cuda.empty_cache()\n            if batch_size > 1:\n                batch_size = max(1, batch_size // 2)\n                logger.warning(\n                    \"CUDA OOM — reducing batch_size to %d and retrying\", batch_size\n                )\n            else:\n                logger.error(\n                    \"CUDA OOM with batch_size=1 at sample %d (id=%s); skipping\",\n                    i,\n                    samples[i].get(\"id\", \"?\"),\n                )\n                pbar.update(1)\n                i += 1\n\n    pbar.close()\n\n    logger.info(\"Saving %d activation records to %s\", len(all_results), pt_path)\n    torch.save(all_results, pt_path)\n\n    logger.info(\"Saving metadata to %s\", meta_path)\n    with open(meta_path, \"w\") as f:\n        for r in all_results:\n            meta = {k: v for k, v in r.items() if k != \"activations\"}\n            meta[\"activation_shape\"] = list(r[\"activations\"].shape)\n            f.write(json.dumps(meta, ensure_ascii=False) + \"\\n\")\n\n    if all_results:\n        shape = all_results[0][\"activations\"].shape\n        logger.info(\n            \"Done: %d samples, %d layers, hidden_dim=%d\",\n            len(all_results),\n            shape[0],\n            shape[2],\n        )\n    else:\n        logger.warning(\"No activations extracted\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
      "numLines": 355,
      "startLine": 1,
      "totalLines": 355
    }
  }
}
```

</details>

---

### Tool call

_source line 44_

<details open><summary>🔧 Tool call — Read · `toolu_013nexqK4VoW1RZEAtYLMcmG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/data/compute_directions.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b4f60a65-bd31-44db-9acc-b5cb02ffadf2",
  "uuid": "2db4f8d7-3772-420f-bd68-0a28bae6c4b9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017z3b5dbsfZkezGSXZD1djZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 836,
      "cache_read_input_tokens": 47917,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 836
      },
      "output_tokens": 66,
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

_source line 45 · 2026-05-18T07:55:48.354Z_

<details><summary>↩ Tool result · `toolu_013nexqK4VoW1RZEAtYLMcmG`</summary>

```text
1	#!/usr/bin/env python3
2	"""Compute contrastive direction vectors (d_syc, d_gen) from paired activations.
3	
4	Input:  .pt file from extract_activations.py — list[dict] with keys:
5	        {pair_id, condition, domain, evidence_strength, correction_turn,
6	         activations: Tensor(num_layers, 2, hidden_dim)}
7	        Each pair_id has two entries: condition="warranted_revision" and
8	        condition="sycophantic_capitulation".
9	
10	Output: directions.pt — dict with keys:
11	        d_syc              (num_layers, 2, hidden_dim) — L2-normalized
12	        d_gen              (num_layers, 2, hidden_dim) — L2-normalized
13	        train_pair_ids     list[str]
14	        test_pair_ids      list[str]
15	        metadata           dict
16	
17	Deps:   torch, numpy, sklearn (for StratifiedShuffleSplit)
18	"""
19	
20	import argparse
21	import logging
22	import sys
23	from collections import defaultdict
24	from pathlib import Path
25	
26	import numpy as np
27	import torch
28	from sklearn.model_selection import StratifiedShuffleSplit
29	
30	logger = logging.getLogger(__name__)
31	
32	
33	def load_and_group(path: str) -> dict[str, dict[str, dict]]:
34	    """Load activation records and group by pair_id.
35	
36	    Returns {pair_id: {"warranted_revision": record, "sycophantic_capitulation": record}}.
37	    """
38	    records = torch.load(path, map_location="cpu", weights_only=False)
39	    logger.info("Loaded %d records from %s", len(records), path)
40	
41	    grouped: dict[str, dict[str, dict]] = defaultdict(dict)
42	    for rec in records:
43	        pid = rec["pair_id"]
44	        cond = rec["condition"]
45	        if cond in grouped[pid]:
46	            logger.warning("Duplicate condition '%s' for pair_id '%s'; overwriting", cond, pid)
47	        grouped[pid][cond] = rec
48	
49	    complete = {}
50	    for pid, conds in grouped.items():
51	        if "warranted_revision" in conds and "sycophantic_capitulation" in conds:
52	            complete[pid] = conds
53	        else:
54	            logger.warning(
55	                "Pair '%s' incomplete (conditions: %s); skipping", pid, list(conds.keys())
56	            )
57	
58	    logger.info("Complete pairs: %d", len(complete))
59	    return complete
60	
61	
62	def stratified_split(
63	    pairs: dict[str, dict[str, dict]], test_ratio: float, seed: int
64	) -> tuple[list[str], list[str]]:
65	    """Split pair_ids into train/test with stratification by domain.
66	
67	    Uses StratifiedShuffleSplit so each domain's proportion is preserved
68	    across the split. The split unit is the pair (both conditions stay together).
69	    """
70	    pair_ids = sorted(pairs.keys())
71	    domains = [pairs[pid]["warranted_revision"]["domain"] for pid in pair_ids]
72	
73	    # Check if stratification is feasible (need >= 2 samples per domain for split)
74	    domain_counts = defaultdict(int)
75	    for d in domains:
76	        domain_counts[d] += 1
77	
78	    min_count = min(domain_counts.values())
79	    if min_count < 2:
80	        logger.warning(
81	            "Some domains have < 2 pairs (min=%d); falling back to unstratified shuffle",
82	            min_count,
83	        )
84	        rng = np.random.RandomState(seed)
85	        idx = rng.permutation(len(pair_ids))
86	        n_test = max(1, int(len(pair_ids) * test_ratio))
87	        test_idx = set(idx[:n_test])
88	        train_ids = [pair_ids[i] for i in range(len(pair_ids)) if i not in test_idx]
89	        test_ids = [pair_ids[i] for i in range(len(pair_ids)) if i in test_idx]
90	        return train_ids, test_ids
91	
92	    splitter = StratifiedShuffleSplit(n_splits=1, test_size=test_ratio, random_state=seed)
93	    pair_ids_arr = np.array(pair_ids)
94	    domains_arr = np.array(domains)
95	
96	    train_idx, test_idx = next(splitter.split(pair_ids_arr, domains_arr))
97	    train_ids = pair_ids_arr[train_idx].tolist()
98	    test_ids = pair_ids_arr[test_idx].tolist()
99	
100	    logger.info("Split: %d train, %d test", len(train_ids), len(test_ids))
101	    return train_ids, test_ids
102	
103	
104	def compute_direction(
105	    pairs: dict[str, dict[str, dict]],
106	    pair_ids: list[str],
107	    positive_condition: str,
108	    negative_condition: str,
109	) -> torch.Tensor:
110	    """Compute difference-in-means direction: mean(positive) - mean(negative).
111	
112	    Returns L2-normalized direction of shape (num_layers, 2, hidden_dim).
113	    """
114	    pos_acts = []
115	    neg_acts = []
116	    for pid in pair_ids:
117	        pos_acts.append(pairs[pid][positive_condition]["activations"])
118	        neg_acts.append(pairs[pid][negative_condition]["activations"])
119	
120	    # Stack: (N, num_layers, 2, hidden_dim)
121	    pos_mean = torch.stack(pos_acts).mean(dim=0)
122	    neg_mean = torch.stack(neg_acts).mean(dim=0)
123	
124	    direction = pos_mean - neg_mean
125	
126	    # L2 normalize per (layer, token_position) slice
127	    norms = direction.norm(dim=-1, keepdim=True).clamp(min=1e-8)
128	    direction = direction / norms
129	
130	    return direction
131	
132	
133	def main() -> None:
134	    parser = argparse.ArgumentParser(
135	        description="Compute contrastive direction vectors from paired activations."
136	    )
137	    parser.add_argument("input", help="Path to activations .pt file (Phase 2 output)")
138	    parser.add_argument("--output-dir", default=".", help="Output directory (default: .)")
139	    parser.add_argument(
140	        "--test-ratio", type=float, default=0.2, help="Test set ratio (default: 0.2)"
141	    )
142	    parser.add_argument("--seed", type=int, default=42, help="Random seed (default: 42)")
143	    args = parser.parse_args()
144	
145	    logging.basicConfig(
146	        level=logging.INFO,
147	        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
148	    )
149	
150	    pairs = load_and_group(args.input)
151	    if not pairs:
152	        logger.error("No complete pairs found; exiting")
153	        sys.exit(1)
154	
155	    train_ids, test_ids = stratified_split(pairs, args.test_ratio, args.seed)
156	
157	    # d_syc: sycophantic_capitulation - warranted_revision (on train set)
158	    logger.info("Computing d_syc from %d train pairs", len(train_ids))
159	    d_syc = compute_direction(
160	        pairs, train_ids,
161	        positive_condition="sycophantic_capitulation",
162	        negative_condition="warranted_revision",
163	    )
164	
165	    # d_gen: warranted_revision - sycophantic_capitulation (on train set)
166	    # Currently d_gen = -d_syc, but stored separately for future extensibility.
167	    logger.info("Computing d_gen from %d train pairs", len(train_ids))
168	    d_gen = compute_direction(
169	        pairs, train_ids,
170	        positive_condition="warranted_revision",
171	        negative_condition="sycophantic_capitulation",
172	    )
173	
174	    num_layers, _, hidden_dim = d_syc.shape
175	    metadata = {
176	        "num_layers": num_layers,
177	        "hidden_dim": hidden_dim,
178	        "test_ratio": args.test_ratio,
179	        "seed": args.seed,
180	        "num_train_pairs": len(train_ids),
181	        "num_test_pairs": len(test_ids),
182	        "num_total_pairs": len(pairs),
183	    }
184	
185	    out_dir = Path(args.output_dir)
186	    out_dir.mkdir(parents=True, exist_ok=True)
187	    out_path = out_dir / "directions.pt"
188	
189	    payload = {
190	        "d_syc": d_syc,
191	        "d_gen": d_gen,
192	        "train_pair_ids": train_ids,
193	        "test_pair_ids": test_ids,
194	        "metadata": metadata,
195	    }
196	    torch.save(payload, out_path)
197	    logger.info("Saved directions to %s", out_path)
198	    logger.info("Metadata: %s", metadata)
199	
200	
201	if __name__ == "__main__":
202	    main()
203	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b4f60a65-bd31-44db-9acc-b5cb02ffadf2",
  "uuid": "74078cb8-7a78-4a5d-b438-79d3aa753c6d",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/data/compute_directions.py",
      "content": "#!/usr/bin/env python3\n\"\"\"Compute contrastive direction vectors (d_syc, d_gen) from paired activations.\n\nInput:  .pt file from extract_activations.py — list[dict] with keys:\n        {pair_id, condition, domain, evidence_strength, correction_turn,\n         activations: Tensor(num_layers, 2, hidden_dim)}\n        Each pair_id has two entries: condition=\"warranted_revision\" and\n        condition=\"sycophantic_capitulation\".\n\nOutput: directions.pt — dict with keys:\n        d_syc              (num_layers, 2, hidden_dim) — L2-normalized\n        d_gen              (num_layers, 2, hidden_dim) — L2-normalized\n        train_pair_ids     list[str]\n        test_pair_ids      list[str]\n        metadata           dict\n\nDeps:   torch, numpy, sklearn (for StratifiedShuffleSplit)\n\"\"\"\n\nimport argparse\nimport logging\nimport sys\nfrom collections import defaultdict\nfrom pathlib import Path\n\nimport numpy as np\nimport torch\nfrom sklearn.model_selection import StratifiedShuffleSplit\n\nlogger = logging.getLogger(__name__)\n\n\ndef load_and_group(path: str) -> dict[str, dict[str, dict]]:\n    \"\"\"Load activation records and group by pair_id.\n\n    Returns {pair_id: {\"warranted_revision\": record, \"sycophantic_capitulation\": record}}.\n    \"\"\"\n    records = torch.load(path, map_location=\"cpu\", weights_only=False)\n    logger.info(\"Loaded %d records from %s\", len(records), path)\n\n    grouped: dict[str, dict[str, dict]] = defaultdict(dict)\n    for rec in records:\n        pid = rec[\"pair_id\"]\n        cond = rec[\"condition\"]\n        if cond in grouped[pid]:\n            logger.warning(\"Duplicate condition '%s' for pair_id '%s'; overwriting\", cond, pid)\n        grouped[pid][cond] = rec\n\n    complete = {}\n    for pid, conds in grouped.items():\n        if \"warranted_revision\" in conds and \"sycophantic_capitulation\" in conds:\n            complete[pid] = conds\n        else:\n            logger.warning(\n                \"Pair '%s' incomplete (conditions: %s); skipping\", pid, list(conds.keys())\n            )\n\n    logger.info(\"Complete pairs: %d\", len(complete))\n    return complete\n\n\ndef stratified_split(\n    pairs: dict[str, dict[str, dict]], test_ratio: float, seed: int\n) -> tuple[list[str], list[str]]:\n    \"\"\"Split pair_ids into train/test with stratification by domain.\n\n    Uses StratifiedShuffleSplit so each domain's proportion is preserved\n    across the split. The split unit is the pair (both conditions stay together).\n    \"\"\"\n    pair_ids = sorted(pairs.keys())\n    domains = [pairs[pid][\"warranted_revision\"][\"domain\"] for pid in pair_ids]\n\n    # Check if stratification is feasible (need >= 2 samples per domain for split)\n    domain_counts = defaultdict(int)\n    for d in domains:\n        domain_counts[d] += 1\n\n    min_count = min(domain_counts.values())\n    if min_count < 2:\n        logger.warning(\n            \"Some domains have < 2 pairs (min=%d); falling back to unstratified shuffle\",\n            min_count,\n        )\n        rng = np.random.RandomState(seed)\n        idx = rng.permutation(len(pair_ids))\n        n_test = max(1, int(len(pair_ids) * test_ratio))\n        test_idx = set(idx[:n_test])\n        train_ids = [pair_ids[i] for i in range(len(pair_ids)) if i not in test_idx]\n        test_ids = [pair_ids[i] for i in range(len(pair_ids)) if i in test_idx]\n        return train_ids, test_ids\n\n    splitter = StratifiedShuffleSplit(n_splits=1, test_size=test_ratio, random_state=seed)\n    pair_ids_arr = np.array(pair_ids)\n    domains_arr = np.array(domains)\n\n    train_idx, test_idx = next(splitter.split(pair_ids_arr, domains_arr))\n    train_ids = pair_ids_arr[train_idx].tolist()\n    test_ids = pair_ids_arr[test_idx].tolist()\n\n    logger.info(\"Split: %d train, %d test\", len(train_ids), len(test_ids))\n    return train_ids, test_ids\n\n\ndef compute_direction(\n    pairs: dict[str, dict[str, dict]],\n    pair_ids: list[str],\n    positive_condition: str,\n    negative_condition: str,\n) -> torch.Tensor:\n    \"\"\"Compute difference-in-means direction: mean(positive) - mean(negative).\n\n    Returns L2-normalized direction of shape (num_layers, 2, hidden_dim).\n    \"\"\"\n    pos_acts = []\n    neg_acts = []\n    for pid in pair_ids:\n        pos_acts.append(pairs[pid][positive_condition][\"activations\"])\n        neg_acts.append(pairs[pid][negative_condition][\"activations\"])\n\n    # Stack: (N, num_layers, 2, hidden_dim)\n    pos_mean = torch.stack(pos_acts).mean(dim=0)\n    neg_mean = torch.stack(neg_acts).mean(dim=0)\n\n    direction = pos_mean - neg_mean\n\n    # L2 normalize per (layer, token_position) slice\n    norms = direction.norm(dim=-1, keepdim=True).clamp(min=1e-8)\n    direction = direction / norms\n\n    return direction\n\n\ndef main() -> None:\n    parser = argparse.ArgumentParser(\n        description=\"Compute contrastive direction vectors from paired activations.\"\n    )\n    parser.add_argument(\"input\", help=\"Path to activations .pt file (Phase 2 output)\")\n    parser.add_argument(\"--output-dir\", default=\".\", help=\"Output directory (default: .)\")\n    parser.add_argument(\n        \"--test-ratio\", type=float, default=0.2, help=\"Test set ratio (default: 0.2)\"\n    )\n    parser.add_argument(\"--seed\", type=int, default=42, help=\"Random seed (default: 42)\")\n    args = parser.parse_args()\n\n    logging.basicConfig(\n        level=logging.INFO,\n        format=\"%(asctime)s [%(levelname)s] %(name)s: %(message)s\",\n    )\n\n    pairs = load_and_group(args.input)\n    if not pairs:\n        logger.error(\"No complete pairs found; exiting\")\n        sys.exit(1)\n\n    train_ids, test_ids = stratified_split(pairs, args.test_ratio, args.seed)\n\n    # d_syc: sycophantic_capitulation - warranted_revision (on train set)\n    logger.info(\"Computing d_syc from %d train pairs\", len(train_ids))\n    d_syc = compute_direction(\n        pairs, train_ids,\n        positive_condition=\"sycophantic_capitulation\",\n        negative_condition=\"warranted_revision\",\n    )\n\n    # d_gen: warranted_revision - sycophantic_capitulation (on train set)\n    # Currently d_gen = -d_syc, but stored separately for future extensibility.\n    logger.info(\"Computing d_gen from %d train pairs\", len(train_ids))\n    d_gen = compute_direction(\n        pairs, train_ids,\n        positive_condition=\"warranted_revision\",\n        negative_condition=\"sycophantic_capitulation\",\n    )\n\n    num_layers, _, hidden_dim = d_syc.shape\n    metadata = {\n        \"num_layers\": num_layers,\n        \"hidden_dim\": hidden_dim,\n        \"test_ratio\": args.test_ratio,\n        \"seed\": args.seed,\n        \"num_train_pairs\": len(train_ids),\n        \"num_test_pairs\": len(test_ids),\n        \"num_total_pairs\": len(pairs),\n    }\n\n    out_dir = Path(args.output_dir)\n    out_dir.mkdir(parents=True, exist_ok=True)\n    out_path = out_dir / \"directions.pt\"\n\n    payload = {\n        \"d_syc\": d_syc,\n        \"d_gen\": d_gen,\n        \"train_pair_ids\": train_ids,\n        \"test_pair_ids\": test_ids,\n        \"metadata\": metadata,\n    }\n    torch.save(payload, out_path)\n    logger.info(\"Saved directions to %s\", out_path)\n    logger.info(\"Metadata: %s\", metadata)\n\n\nif __name__ == \"__main__\":\n    main()\n",
      "numLines": 203,
      "startLine": 1,
      "totalLines": 203
    }
  }
}
```

</details>

---

### Assistant

_source line 46_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of the project. Let me write the DC-GRPO training framework skeleton code. Key points from the references:

1. **IDEA_BRIEF.md** describes:
   - R1 (Direction Alignment): cosine projection of activations onto d_syc/d_gen
   - R2 (Contrastive): cross-rollout comparison of directional projections
   - R3 (Behavioral): NLI-based behavioral scoring
   - Combined: R = alpha * R1 + beta * R2 + gamma * R3
   - Model: Qwen3-8B with LoRA (rank 64) + GRPO
   - Direction recalibration every 500 steps

2. **post_mvp_experiment_skeleton.md** specifies the reward mechanics more precisely: R1 penalizes high d_syc projection while rewarding high d_gen projection on policy model activations at critical turns, R2 compares directional projections across different rollouts of the same prompt, and R3 uses DeBERTa-v3 for NLI-based behavioral scoring.

3. **extract_activations.py** shows how to detect token boundaries and extract activations...

Building the framework skeleton...

Now I'm defining the reward functions. R1 penalizes sycophantic direction projections while rewarding genuine revision projections using cosine similarity. R2 compares activation projections across rollouts for the same prompt to enforce consistency, and I need to think through how to aggregate those comparisons into a scalar reward signal.

For R3, I'm using NLI to check if revisions are actually warranted versus just capitulation. The hook extracts activations at critical turns during the forward pass, the rollout generator creates multi-turn dialogues and captures those activations, and the trainer extends TRL's GRPO implementation to incorporate these activation-based rewards.

Now I need to think through the direction shapes—they're structured as (num_layers, 2, hidden_dim) where the 2 dimension splits user and assistant token positions, so I'll use the assistant's first token at the target layer for reward computation. Looking at the brief, R1 should span mid and deep layers with cosine projections, so let me start building out the skeleton.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b4f60a65-bd31-44db-9acc-b5cb02ffadf2",
  "uuid": "0342779b-e3a4-4fcd-abef-78bc14b8df70",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QjQkz18NUWMoGHT4L5cjVB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7680,
      "cache_read_input_tokens": 48753,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7680
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

_source line 47_

Now I have all the context. Let me create the training directory and write the framework.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b4f60a65-bd31-44db-9acc-b5cb02ffadf2",
  "uuid": "64642a3d-d231-41f3-a097-35cc45ab3284",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QjQkz18NUWMoGHT4L5cjVB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7680,
      "cache_read_input_tokens": 48753,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7680
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

_source line 48_

<details open><summary>🔧 Tool call — Bash · `toolu_01UhZAWSMW5DxxSwy5PzjSPd`</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/training",
  "description": "Create training artifacts directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b4f60a65-bd31-44db-9acc-b5cb02ffadf2",
  "uuid": "9e114100-e976-4931-ad17-07c2725a4490",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QjQkz18NUWMoGHT4L5cjVB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7680,
      "cache_read_input_tokens": 48753,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7680
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

_source line 49 · 2026-05-18T07:56:15.155Z_

<details><summary>↩ Tool result · `toolu_01UhZAWSMW5DxxSwy5PzjSPd`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b4f60a65-bd31-44db-9acc-b5cb02ffadf2",
  "uuid": "8e06b9d5-f26d-4e4c-95b1-0549391399ed",
  "tool_use_result": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": true
  }
}
```

</details>

---

### Tool call

_source line 50_

<details open><summary>🔧 Tool call — Write · `toolu_01JhHLHJAvwtkyktQp6SX9i7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/training/grpo_framework.py",
  "content": "#!/usr/bin/env python3\n\"\"\"DC-GRPO (Direction-Contrastive GRPO) Training Framework\n\nArchitecture overview:\n  1. ActivationExtractionHook  — registers forward hooks to capture hidden states\n                                  at target layers during training forward passes\n  2. MultiTurnRolloutGenerator — generates multi-turn dialogue rollouts from\n                                  calibration pairs and extracts critical-turn activations\n  3. DirectionAlignmentReward  — R1: cosine projection onto d_syc / d_gen directions\n  4. ContrastiveConsistencyReward — R2: cross-rollout directional projection contrast\n  5. BehavioralReward          — R3: NLI-based stance consistency scoring\n  6. DCGRPOTrainer             — orchestrates rollout, activation extraction, reward\n                                  computation, and GRPO policy updates\n  7. DCGRPOConfig              — dataclass holding all hyperparameters\n\nDependencies: torch, transformers, trl, peft, numpy\nOptional:     transformers (DeBERTa for R3 NLI scoring)\n\nDirection format (from compute_directions.py):\n  d_syc, d_gen: Tensor(num_layers, 2, hidden_dim)\n    dim-1 index 0 = user last content token position\n    dim-1 index 1 = assistant first content token position\n  Both are L2-normalized per (layer, position) slice.\n\nReward formulas:\n  R1(h, condition) =\n    -cos(h[layer, pos], d_syc[layer, pos])   if condition == sycophantic_capitulation\n    +cos(h[layer, pos], d_gen[layer, pos])    if condition == warranted_revision\n  R2(h_wr, h_sc) =\n    cos(h_wr[layer, pos], d_gen[layer, pos]) - cos(h_sc[layer, pos], d_syc[layer, pos])\n  R3(response, ground_truth, condition) =\n    +1 if behavior matches expected (revise when warranted / maintain when unwarranted)\n    -1 otherwise\n  R_total = alpha * R1 + beta * R2 + gamma * R3\n\"\"\"\n\nfrom __future__ import annotations\n\nimport logging\nfrom dataclasses import dataclass, field\nfrom typing import Any\n\nimport torch\nimport torch.nn as nn\nimport torch.nn.functional as F\n\nlogger = logging.getLogger(__name__)\n\n\n# ---------------------------------------------------------------------------\n# Activation Extraction Hook\n# ---------------------------------------------------------------------------\n\nclass ActivationExtractionHook:\n    \"\"\"Captures hidden-state activations at specified transformer layers during forward pass.\n\n    Unlike offline extraction (extract_activations.py) which calls model() with\n    output_hidden_states=True, this hook attaches to specific layers and works\n    during training forward passes where output_hidden_states may not be available\n    or would add unnecessary memory overhead.\n\n    Usage:\n        hook = ActivationExtractionHook(target_layers=[10, 12, 14, 24, 26])\n        hook.register(model)\n        outputs = model(input_ids=..., attention_mask=...)\n        acts = hook.get_activations()  # {layer_idx: Tensor(batch, seq_len, hidden_dim)}\n        hook.clear()\n    \"\"\"\n\n    def __init__(self, target_layers: list[int]):\n        \"\"\"\n        Args:\n            target_layers: 0-indexed transformer layer indices to capture.\n                           Typically mid-layers (10-15) + deep layers (20-28).\n        \"\"\"\n        self.target_layers = sorted(target_layers)\n        self._activations: dict[int, torch.Tensor] = {}\n        self._handles: list[Any] = []\n\n    def register(self, model: nn.Module) -> None:\n        \"\"\"Attach forward hooks to target layers of the model.\n\n        Expects model.model.layers[i] (standard HuggingFace causal LM layout).\n        \"\"\"\n        self.remove()\n        # TODO: resolve layer accessor for different model architectures\n        #       currently assumes model.model.layers (Qwen, Llama, Mistral)\n        layers = model.model.layers\n        for layer_idx in self.target_layers:\n            if layer_idx >= len(layers):\n                raise ValueError(\n                    f\"Layer {layer_idx} out of range (model has {len(layers)} layers)\"\n                )\n            handle = layers[layer_idx].register_forward_hook(\n                self._make_hook(layer_idx)\n            )\n            self._handles.append(handle)\n        logger.info(\"Registered activation hooks on layers %s\", self.target_layers)\n\n    def _make_hook(self, layer_idx: int):\n        def hook_fn(module, input, output):\n            # output is typically (hidden_states, ...) or just hidden_states\n            if isinstance(output, tuple):\n                hidden = output[0]\n            else:\n                hidden = output\n            # Detach to avoid retaining the computation graph through the hook\n            self._activations[layer_idx] = hidden.detach()\n        return hook_fn\n\n    def get_activations(self) -> dict[int, torch.Tensor]:\n        \"\"\"Return captured activations: {layer_idx: Tensor(batch, seq_len, hidden_dim)}.\"\"\"\n        return dict(self._activations)\n\n    def extract_at_positions(\n        self,\n        positions: dict[int, tuple[int, int]],\n    ) -> dict[int, dict[int, torch.Tensor]]:\n        \"\"\"Extract activations at specific (user_pos, asst_pos) for each sample in batch.\n\n        Args:\n            positions: {batch_idx: (user_last_pos, asst_first_pos)}\n\n        Returns:\n            {layer_idx: {batch_idx: Tensor(2, hidden_dim)}}\n            where dim-0: [user_last_token, asst_first_token]\n        \"\"\"\n        result: dict[int, dict[int, torch.Tensor]] = {}\n        for layer_idx, hidden in self._activations.items():\n            result[layer_idx] = {}\n            for batch_idx, (user_pos, asst_pos) in positions.items():\n                user_vec = hidden[batch_idx, user_pos, :]\n                asst_vec = hidden[batch_idx, asst_pos, :]\n                result[layer_idx][batch_idx] = torch.stack([user_vec, asst_vec], dim=0)\n        return result\n\n    def clear(self) -> None:\n        \"\"\"Discard stored activations to free memory.\"\"\"\n        self._activations.clear()\n\n    def remove(self) -> None:\n        \"\"\"Remove all registered hooks and clear activations.\"\"\"\n        for h in self._handles:\n            h.remove()\n        self._handles.clear()\n        self._activations.clear()\n\n\n# ---------------------------------------------------------------------------\n# Multi-Turn Rollout Generator\n# ---------------------------------------------------------------------------\n\nclass MultiTurnRolloutGenerator:\n    \"\"\"Generates multi-turn dialogue rollouts from calibration pairs.\n\n    For GRPO, multiple rollouts (responses) are sampled for each prompt.\n    Each rollout captures the model's response at the critical turn along\n    with the hidden-state activations needed for R1/R2 reward computation.\n\n    Reuses token boundary detection logic from extract_activations.py\n    (find_critical_positions) adapted for online generation.\n    \"\"\"\n\n    def __init__(\n        self,\n        tokenizer: Any,\n        activation_hook: ActivationExtractionHook,\n        max_new_tokens: int = 512,\n        max_turns: int = 5,\n        num_rollouts: int = 4,\n        temperature: float = 0.7,\n        top_p: float = 0.95,\n    ):\n        \"\"\"\n        Args:\n            tokenizer: HuggingFace tokenizer with chat template support.\n            activation_hook: Hook instance (already registered on the model).\n            max_new_tokens: Maximum tokens to generate per assistant turn.\n            max_turns: Maximum number of dialogue turns (truncate longer dialogues).\n            num_rollouts: Number of rollout samples per prompt (GRPO group size).\n            temperature: Sampling temperature for generation.\n            top_p: Nucleus sampling threshold.\n        \"\"\"\n        self.tokenizer = tokenizer\n        self.activation_hook = activation_hook\n        self.max_new_tokens = max_new_tokens\n        self.max_turns = max_turns\n        self.num_rollouts = num_rollouts\n        self.temperature = temperature\n        self.top_p = top_p\n\n    def generate_rollouts(\n        self,\n        model: nn.Module,\n        prompt_pair: dict,\n    ) -> list[dict]:\n        \"\"\"Generate multiple rollouts for a calibration prompt pair.\n\n        Args:\n            model: The policy model (with LoRA adapters).\n            prompt_pair: Dict with keys:\n                - id: str (pair identifier)\n                - condition: \"warranted_revision\" | \"sycophantic_capitulation\"\n                - turns: list[dict] with role/content (conversation up to critical turn)\n                - correction_turn: int (1-indexed critical turn number)\n                - ground_truth: dict with expected behavior metadata\n\n        Returns:\n            List of rollout dicts, each containing:\n                - response: str (generated assistant response at critical turn)\n                - input_ids: Tensor (full input sequence)\n                - activations: dict {layer_idx: Tensor(2, hidden_dim)}\n                - user_pos: int\n                - asst_pos: int\n                - metadata: dict (pair_id, condition, etc.)\n        \"\"\"\n        # TODO: implement rollout generation\n        #   1. Build input from turns up to and including the critical user turn\n        #   2. Use tokenizer.apply_chat_template with add_generation_prompt=True\n        #   3. Call model.generate() with num_return_sequences=self.num_rollouts\n        #   4. For each generated response, re-run forward pass with activation hook\n        #      to extract hidden states at the critical positions\n        #   5. Use find_critical_positions logic (adapted from extract_activations.py)\n        #      to locate user_last_token and asst_first_token boundaries\n        #   6. Return list of rollout dicts\n        #\n        # Key considerations:\n        # - Generation uses sampling (temperature, top_p) for diversity across rollouts\n        # - After generation, a separate forward pass through the full sequence\n        #   (context + generated response) is needed to extract activations at the\n        #   exact critical positions, because generate() doesn't expose intermediate\n        #   hidden states at arbitrary positions\n        # - Memory management: clear activation hook after each extraction\n        raise NotImplementedError(\"MultiTurnRolloutGenerator.generate_rollouts\")\n\n    def _find_critical_positions(\n        self,\n        turns: list[dict],\n        correction_turn: int,\n    ) -> tuple[int, int, list[int]]:\n        \"\"\"Locate critical token positions in tokenized conversation.\n\n        Mirrors extract_activations.find_critical_positions but adapted for\n        online use within the training loop.\n\n        Returns:\n            (user_last_pos, asst_first_pos, full_input_ids)\n        \"\"\"\n        # TODO: port find_critical_positions from extract_activations.py\n        #   - Tokenize through user turn to find user_last_content_token\n        #   - Tokenize with add_generation_prompt to find asst_first_content_token\n        #   - Handle Qwen3 chat template quirks (enable_thinking=False)\n        raise NotImplementedError(\n            \"MultiTurnRolloutGenerator._find_critical_positions\"\n        )\n\n\n# ---------------------------------------------------------------------------\n# R1: Direction Alignment Reward\n# ---------------------------------------------------------------------------\n\nclass DirectionAlignmentReward:\n    \"\"\"R1: Directional projection reward targeting sycophantic vs. genuine pathways.\n\n    Computes cosine similarity between the policy model's hidden-state activation\n    at the critical turn and the pre-computed contrastive directions (d_syc, d_gen).\n\n    Math:\n      For sycophantic_capitulation condition:\n        R1 = -cos(h[layer, pos], d_syc[layer, pos])\n        (penalize activations aligned with sycophantic direction)\n\n      For warranted_revision condition:\n        R1 = +cos(h[layer, pos], d_gen[layer, pos])\n        (reward activations aligned with genuine revision direction)\n\n    When using multiple layers, the reward is averaged across target layers.\n    The position index (0=user_last, 1=asst_first) is configurable; default\n    is asst_first (index 1), as the assistant's first response token carries\n    the strongest signal about the model's internal decision.\n    \"\"\"\n\n    def __init__(\n        self,\n        directions_path: str,\n        target_layers: list[int],\n        position_idx: int = 1,\n    ):\n        \"\"\"\n        Args:\n            directions_path: Path to directions.pt (from compute_directions.py).\n                             Contains d_syc, d_gen of shape (num_layers, 2, hidden_dim).\n            target_layers: Transformer layer indices for projection (0-indexed).\n            position_idx: Token position index (0=user_last, 1=asst_first).\n        \"\"\"\n        self.target_layers = target_layers\n        self.position_idx = position_idx\n\n        # TODO: load directions and move to device\n        #   data = torch.load(directions_path, map_location=\"cpu\")\n        #   self.d_syc = data[\"d_syc\"]  # (num_layers, 2, hidden_dim)\n        #   self.d_gen = data[\"d_gen\"]  # (num_layers, 2, hidden_dim)\n        self.d_syc: torch.Tensor | None = None\n        self.d_gen: torch.Tensor | None = None\n        self._directions_path = directions_path\n\n    def load_directions(self, device: torch.device) -> None:\n        \"\"\"Load direction vectors from disk and move to device.\"\"\"\n        # TODO: implement\n        #   data = torch.load(self._directions_path, map_location=\"cpu\", weights_only=False)\n        #   self.d_syc = data[\"d_syc\"].to(device)\n        #   self.d_gen = data[\"d_gen\"].to(device)\n        raise NotImplementedError(\"DirectionAlignmentReward.load_directions\")\n\n    def compute(\n        self,\n        activations: dict[int, torch.Tensor],\n        condition: str,\n    ) -> float:\n        \"\"\"Compute R1 reward for a single rollout.\n\n        Args:\n            activations: {layer_idx: Tensor(2, hidden_dim)} from ActivationExtractionHook.\n            condition: \"warranted_revision\" or \"sycophantic_capitulation\".\n\n        Returns:\n            Scalar R1 reward, averaged over target layers.\n        \"\"\"\n        # TODO: implement\n        #   scores = []\n        #   for layer in self.target_layers:\n        #       h = activations[layer][self.position_idx]        # (hidden_dim,)\n        #       if condition == \"sycophantic_capitulation\":\n        #           d = self.d_syc[layer, self.position_idx]     # (hidden_dim,)\n        #           score = -F.cosine_similarity(h.unsqueeze(0), d.unsqueeze(0)).item()\n        #       elif condition == \"warranted_revision\":\n        #           d = self.d_gen[layer, self.position_idx]\n        #           score = F.cosine_similarity(h.unsqueeze(0), d.unsqueeze(0)).item()\n        #       else:\n        #           raise ValueError(f\"Unknown condition: {condition}\")\n        #       scores.append(score)\n        #   return sum(scores) / len(scores)\n        raise NotImplementedError(\"DirectionAlignmentReward.compute\")\n\n    def compute_batch(\n        self,\n        batch_activations: list[dict[int, torch.Tensor]],\n        conditions: list[str],\n    ) -> list[float]:\n        \"\"\"Compute R1 for a batch of rollouts.\n\n        Args:\n            batch_activations: List of per-rollout activation dicts.\n            conditions: List of condition strings, one per rollout.\n\n        Returns:\n            List of R1 scalar rewards.\n        \"\"\"\n        # TODO: vectorized batch implementation for efficiency\n        #   For now, loop over individual compute() calls\n        return [\n            self.compute(acts, cond)\n            for acts, cond in zip(batch_activations, conditions)\n        ]\n\n    def update_directions(self, new_directions_path: str, device: torch.device) -> None:\n        \"\"\"Reload directions after recalibration (every ~500 training steps).\n\n        Args:\n            new_directions_path: Path to recalibrated directions.pt.\n            device: Target device.\n        \"\"\"\n        # TODO: implement hot-reload of recalibrated directions\n        #   self._directions_path = new_directions_path\n        #   self.load_directions(device)\n        raise NotImplementedError(\"DirectionAlignmentReward.update_directions\")\n\n\n# ---------------------------------------------------------------------------\n# R2: Contrastive Consistency Reward\n# ---------------------------------------------------------------------------\n\nclass ContrastiveConsistencyReward:\n    \"\"\"R2: Cross-condition contrastive reward using directional projections.\n\n    Exploits GRPO's group-relative structure by comparing directional projections\n    across the two conditions of the same calibration pair.\n\n    Math:\n      R2 = cos(h_wr[layer, pos], d_gen[layer, pos])\n         - cos(h_sc[layer, pos], d_syc[layer, pos])\n\n    where:\n      h_wr = activation from a warranted_revision rollout\n      h_sc = activation from a sycophantic_capitulation rollout\n      on the same underlying calibration pair.\n\n    Higher R2 means the model produces representations that are well-separated\n    along the intended directions: high d_gen alignment for genuine revision\n    and low d_syc alignment for sycophantic capitulation.\n    \"\"\"\n\n    def __init__(\n        self,\n        directions_path: str,\n        target_layers: list[int],\n        position_idx: int = 1,\n    ):\n        \"\"\"\n        Args:\n            directions_path: Path to directions.pt.\n            target_layers: Transformer layer indices for projection.\n            position_idx: Token position index (0=user_last, 1=asst_first).\n        \"\"\"\n        self.target_layers = target_layers\n        self.position_idx = position_idx\n        self.d_syc: torch.Tensor | None = None\n        self.d_gen: torch.Tensor | None = None\n        self._directions_path = directions_path\n\n    def compute(\n        self,\n        activations_wr: dict[int, torch.Tensor],\n        activations_sc: dict[int, torch.Tensor],\n    ) -> float:\n        \"\"\"Compute R2 for a paired set of rollouts.\n\n        Args:\n            activations_wr: Activations from warranted_revision rollout.\n                            {layer_idx: Tensor(2, hidden_dim)}\n            activations_sc: Activations from sycophantic_capitulation rollout.\n                            {layer_idx: Tensor(2, hidden_dim)}\n\n        Returns:\n            Scalar R2 reward, averaged over target layers.\n        \"\"\"\n        # TODO: implement\n        #   scores = []\n        #   for layer in self.target_layers:\n        #       h_wr = activations_wr[layer][self.position_idx]\n        #       h_sc = activations_sc[layer][self.position_idx]\n        #       gen_proj = F.cosine_similarity(\n        #           h_wr.unsqueeze(0), self.d_gen[layer, self.position_idx].unsqueeze(0)\n        #       ).item()\n        #       syc_proj = F.cosine_similarity(\n        #           h_sc.unsqueeze(0), self.d_syc[layer, self.position_idx].unsqueeze(0)\n        #       ).item()\n        #       scores.append(gen_proj - syc_proj)\n        #   return sum(scores) / len(scores)\n        raise NotImplementedError(\"ContrastiveConsistencyReward.compute\")\n\n    def compute_group(\n        self,\n        rollouts_wr: list[dict[int, torch.Tensor]],\n        rollouts_sc: list[dict[int, torch.Tensor]],\n    ) -> list[float]:\n        \"\"\"Compute R2 for all pairs in a GRPO group.\n\n        GRPO samples multiple rollouts per prompt. R2 is computed for each\n        (wr_rollout, sc_rollout) pairing within the same calibration pair.\n\n        Args:\n            rollouts_wr: List of activation dicts from warranted_revision rollouts.\n            rollouts_sc: List of activation dicts from sycophantic_capitulation rollouts.\n\n        Returns:\n            List of R2 rewards (one per wr-sc pair, or aggregated per rollout).\n        \"\"\"\n        # TODO: implement cross-rollout pairing strategy\n        #   Option A: pair by index (rollouts_wr[i] with rollouts_sc[i])\n        #   Option B: mean across all cross-pairs\n        #   Option C: max-contrast pair selection\n        raise NotImplementedError(\"ContrastiveConsistencyReward.compute_group\")\n\n    def update_directions(self, new_directions_path: str, device: torch.device) -> None:\n        \"\"\"Reload directions after recalibration.\"\"\"\n        # TODO: implement (same pattern as DirectionAlignmentReward)\n        raise NotImplementedError(\"ContrastiveConsistencyReward.update_directions\")\n\n\n# ---------------------------------------------------------------------------\n# R3: Behavioral Reward\n# ---------------------------------------------------------------------------\n\nclass BehavioralReward:\n    \"\"\"R3: Output-level behavioral correctness reward via NLI stance detection.\n\n    Evaluates whether the model's generated response exhibits the correct\n    behavior given the condition:\n      - warranted_revision: model SHOULD revise its prior incorrect answer\n        when presented with valid evidence -> reward revision, penalize stubbornness\n      - sycophantic_capitulation: model SHOULD maintain its prior correct answer\n        under social pressure -> reward maintenance, penalize capitulation\n\n    Stance detection uses DeBERTa-v3-base NLI to determine whether the\n    generated response agrees with the original position or the new position.\n\n    Scoring:\n      warranted_revision:\n        response revises to correct answer   -> +1\n        response maintains incorrect answer  -> -1\n      sycophantic_capitulation:\n        response maintains correct answer     -> +1\n        response capitulates to pressure      -> -1\n    \"\"\"\n\n    def __init__(\n        self,\n        nli_model_name: str = \"microsoft/deberta-v3-base\",\n        device: str = \"cuda:0\",\n    ):\n        \"\"\"\n        Args:\n            nli_model_name: HuggingFace model ID for NLI scoring.\n            device: Torch device for NLI model.\n        \"\"\"\n        self.nli_model_name = nli_model_name\n        self.device = device\n        self._nli_model = None\n        self._nli_tokenizer = None\n\n    def load_nli_model(self) -> None:\n        \"\"\"Lazily load the NLI model and tokenizer.\"\"\"\n        # TODO: implement\n        #   from transformers import AutoModelForSequenceClassification, AutoTokenizer\n        #   self._nli_tokenizer = AutoTokenizer.from_pretrained(self.nli_model_name)\n        #   self._nli_model = AutoModelForSequenceClassification.from_pretrained(\n        #       self.nli_model_name\n        #   ).to(self.device).eval()\n        raise NotImplementedError(\"BehavioralReward.load_nli_model\")\n\n    def compute(\n        self,\n        response: str,\n        ground_truth: dict,\n        condition: str,\n    ) -> float:\n        \"\"\"Compute R3 for a single rollout.\n\n        Args:\n            response: Generated assistant response text.\n            ground_truth: Dict containing:\n                - original_answer: str (model's initial position)\n                - correct_answer: str (ground truth)\n                - challenge_claim: str (user's challenge in the critical turn)\n            condition: \"warranted_revision\" or \"sycophantic_capitulation\".\n\n        Returns:\n            Scalar R3 reward in {-1, +1} (or continuous [-1, +1] with NLI confidence).\n        \"\"\"\n        # TODO: implement\n        #   1. Determine stance: does the response agree with original_answer\n        #      or with challenge_claim / correct_answer?\n        #   2. Use NLI to classify entailment/contradiction between:\n        #      - (response, original_answer) -> entailment = maintains position\n        #      - (response, correct_answer)  -> entailment = revised position\n        #   3. Map to reward based on condition:\n        #      warranted_revision:\n        #        revised -> +1 (or +nli_confidence for continuous version)\n        #        maintained -> -1\n        #      sycophantic_capitulation:\n        #        maintained -> +1\n        #        capitulated -> -1\n        #   4. Edge case: response is ambiguous or off-topic -> 0\n        raise NotImplementedError(\"BehavioralReward.compute\")\n\n    def compute_batch(\n        self,\n        responses: list[str],\n        ground_truths: list[dict],\n        conditions: list[str],\n    ) -> list[float]:\n        \"\"\"Compute R3 for a batch of rollouts.\n\n        Args:\n            responses: List of generated response texts.\n            ground_truths: List of ground truth dicts.\n            conditions: List of condition strings.\n\n        Returns:\n            List of R3 scalar rewards.\n        \"\"\"\n        # TODO: batch NLI inference for efficiency\n        return [\n            self.compute(resp, gt, cond)\n            for resp, gt, cond in zip(responses, ground_truths, conditions)\n        ]\n\n\n# ---------------------------------------------------------------------------\n# DC-GRPO Trainer\n# ---------------------------------------------------------------------------\n\nclass DCGRPOTrainer:\n    \"\"\"Direction-Contrastive GRPO Trainer.\n\n    Extends the TRL GRPOTrainer paradigm with representation-level reward\n    signals (R1, R2) alongside behavioral reward (R3).\n\n    Key differences from standard GRPO:\n      - Reward comes from directional projections on the policy model's own\n        activations, not from an external reward model\n      - Training operates on paired prompts (warranted_revision +\n        sycophantic_capitulation) from the same calibration pair\n      - Directions are periodically recalibrated using recent rollout activations\n      - Activation extraction hooks add ~5-10% overhead per forward pass\n\n    Training loop (per step):\n      1. Sample a batch of calibration pairs\n      2. Generate num_rollouts responses per condition per pair\n      3. Run forward pass with activation hooks to extract critical-turn activations\n      4. Compute R1 (per-rollout directional alignment)\n      5. Compute R2 (cross-condition contrastive projection)\n      6. Compute R3 (behavioral NLI scoring)\n      7. Combine: R = alpha * R1 + beta * R2 + gamma * R3\n      8. Apply GRPO policy gradient update using group-relative advantage\n      9. Every recalib_interval steps, recompute d_syc/d_gen from recent rollouts\n    \"\"\"\n\n    def __init__(\n        self,\n        model: nn.Module,\n        tokenizer: Any,\n        ref_model: nn.Module | None,\n        r1_reward: DirectionAlignmentReward,\n        r2_reward: ContrastiveConsistencyReward,\n        r3_reward: BehavioralReward,\n        config: DCGRPOConfig,\n    ):\n        \"\"\"\n        Args:\n            model: Policy model (with LoRA adapters applied).\n            tokenizer: HuggingFace tokenizer.\n            ref_model: Reference model for KL penalty (frozen copy or None).\n            r1_reward: Direction alignment reward component.\n            r2_reward: Contrastive consistency reward component.\n            r3_reward: Behavioral reward component.\n            config: Full training configuration.\n        \"\"\"\n        self.model = model\n        self.tokenizer = tokenizer\n        self.ref_model = ref_model\n        self.r1_reward = r1_reward\n        self.r2_reward = r2_reward\n        self.r3_reward = r3_reward\n        self.config = config\n\n        self.activation_hook = ActivationExtractionHook(\n            target_layers=config.target_layers\n        )\n        self.rollout_generator = MultiTurnRolloutGenerator(\n            tokenizer=tokenizer,\n            activation_hook=self.activation_hook,\n            max_new_tokens=config.max_new_tokens,\n            num_rollouts=config.num_rollouts,\n            temperature=config.temperature,\n        )\n\n        self._global_step = 0\n        self._optimizer = None\n        self._scheduler = None\n\n    def setup(self) -> None:\n        \"\"\"Initialize optimizer, scheduler, hooks, and reward models.\"\"\"\n        # TODO: implement\n        #   1. Register activation hooks on the policy model\n        #   2. Load directions for R1 and R2\n        #   3. Load NLI model for R3\n        #   4. Create optimizer (AdamW) with LoRA parameters only\n        #   5. Create learning rate scheduler\n        #   6. If ref_model is None, create a frozen copy for KL penalty\n        raise NotImplementedError(\"DCGRPOTrainer.setup\")\n\n    def compute_combined_reward(\n        self,\n        rollout: dict,\n        activations: dict[int, torch.Tensor],\n        paired_activations: dict[int, torch.Tensor] | None,\n        condition: str,\n        ground_truth: dict,\n    ) -> dict[str, float]:\n        \"\"\"Compute the combined three-component reward for a single rollout.\n\n        Args:\n            rollout: Rollout dict from MultiTurnRolloutGenerator.\n            activations: This rollout's activations {layer: Tensor(2, hidden_dim)}.\n            paired_activations: Activations from the paired condition's rollout\n                                (needed for R2). None if no paired rollout available.\n            condition: \"warranted_revision\" or \"sycophantic_capitulation\".\n            ground_truth: Ground truth dict for R3 scoring.\n\n        Returns:\n            Dict with keys: \"r1\", \"r2\", \"r3\", \"combined\", each a float.\n        \"\"\"\n        alpha = self.config.reward_weights[\"r1\"]\n        beta = self.config.reward_weights[\"r2\"]\n        gamma = self.config.reward_weights[\"r3\"]\n\n        # TODO: implement\n        #   r1 = self.r1_reward.compute(activations, condition)\n        #   if paired_activations is not None:\n        #       if condition == \"warranted_revision\":\n        #           r2 = self.r2_reward.compute(activations, paired_activations)\n        #       else:\n        #           r2 = self.r2_reward.compute(paired_activations, activations)\n        #   else:\n        #       r2 = 0.0\n        #   r3 = self.r3_reward.compute(rollout[\"response\"], ground_truth, condition)\n        #   combined = alpha * r1 + beta * r2 + gamma * r3\n        #   return {\"r1\": r1, \"r2\": r2, \"r3\": r3, \"combined\": combined}\n        raise NotImplementedError(\"DCGRPOTrainer.compute_combined_reward\")\n\n    def compute_grpo_loss(\n        self,\n        rollouts: list[dict],\n        rewards: list[float],\n    ) -> torch.Tensor:\n        \"\"\"Compute GRPO policy gradient loss with group-relative advantage.\n\n        GRPO normalizes rewards within each group (rollouts from the same prompt)\n        to compute advantages, then applies a clipped policy gradient objective.\n\n        Math:\n          advantage_i = (reward_i - mean(rewards_group)) / std(rewards_group)\n          ratio_i = pi_theta(response_i | prompt) / pi_ref(response_i | prompt)\n          loss = -mean(min(ratio_i * advantage_i, clip(ratio_i, 1-eps, 1+eps) * advantage_i))\n                 + beta_kl * KL(pi_theta || pi_ref)\n\n        Args:\n            rollouts: List of rollout dicts (with input_ids and response tokens).\n            rewards: List of combined reward scalars (one per rollout).\n\n        Returns:\n            Scalar loss tensor.\n        \"\"\"\n        # TODO: implement\n        #   1. Group rollouts by prompt (pair_id + condition)\n        #   2. For each group, normalize rewards to compute advantages:\n        #      advantages = (rewards - mean) / (std + eps)\n        #   3. Compute log-probabilities under policy and reference model\n        #   4. Compute importance sampling ratio: ratio = exp(logprob_policy - logprob_ref)\n        #   5. Clipped surrogate objective:\n        #      surr1 = ratio * advantage\n        #      surr2 = clamp(ratio, 1-clip_eps, 1+clip_eps) * advantage\n        #      loss = -mean(min(surr1, surr2))\n        #   6. Add KL penalty: beta_kl * mean(logprob_policy - logprob_ref)\n        #   7. Return combined loss\n        raise NotImplementedError(\"DCGRPOTrainer.compute_grpo_loss\")\n\n    def train_step(self, batch: list[dict]) -> dict[str, float]:\n        \"\"\"Execute one training step on a batch of calibration pairs.\n\n        Args:\n            batch: List of calibration pair dicts. Each pair has two conditions\n                   (warranted_revision and sycophantic_capitulation) sharing\n                   the same pair_id.\n\n        Returns:\n            Dict of training metrics:\n                - loss: total loss\n                - r1_mean, r2_mean, r3_mean: mean per-component rewards\n                - combined_reward_mean: mean combined reward\n                - r1_r3_disagreement: fraction where R1 and R3 give opposite signals\n        \"\"\"\n        # TODO: implement\n        #   1. For each pair in batch:\n        #      a. Generate rollouts for both conditions\n        #      b. Extract activations at critical positions\n        #      c. Compute rewards (R1, R2, R3) for each rollout\n        #   2. Flatten all rollouts and their rewards\n        #   3. Compute GRPO loss\n        #   4. Backward pass + optimizer step\n        #   5. Clear activation hook\n        #   6. Compute and return metrics (including R1-R3 disagreement frequency)\n        raise NotImplementedError(\"DCGRPOTrainer.train_step\")\n\n    def maybe_recalibrate_directions(self) -> None:\n        \"\"\"Recompute d_syc/d_gen from recent rollout activations if due.\n\n        Called every recalib_interval steps. Uses a buffer of recent rollout\n        activations (from the last recalib_interval steps) to recompute\n        directions via the same difference-in-means procedure as\n        compute_directions.py.\n\n        Monitors direction stability: if cosine(d_new, d_old) < 0.7,\n        log a warning (potential direction drift under LoRA training).\n        \"\"\"\n        # TODO: implement\n        #   1. Check if self._global_step % self.config.recalib_interval == 0\n        #   2. Collect recent rollout activations from the buffer\n        #   3. Separate by condition (warranted_revision vs. sycophantic_capitulation)\n        #   4. Compute new d_syc, d_gen via difference-in-means\n        #   5. Check cosine similarity with previous directions\n        #   6. If cosine < 0.7, log warning about direction drift\n        #   7. Update R1 and R2 with new directions\n        #   8. Save new directions to disk (for checkpointing)\n        raise NotImplementedError(\"DCGRPOTrainer.maybe_recalibrate_directions\")\n\n    def train(\n        self,\n        dataset: Any,\n        num_epochs: int = 1,\n        eval_dataset: Any | None = None,\n        eval_interval: int = 500,\n    ) -> dict[str, list[float]]:\n        \"\"\"Full training loop.\n\n        Args:\n            dataset: Iterable of calibration pair dicts.\n            num_epochs: Number of passes over the dataset.\n            eval_dataset: Optional held-out pairs for monitoring direction AUROC.\n            eval_interval: Steps between evaluation runs.\n\n        Returns:\n            Training history: {metric_name: [values_per_step]}.\n        \"\"\"\n        # TODO: implement\n        #   1. Call self.setup()\n        #   2. For each epoch:\n        #      a. Iterate over dataset in batches of config.batch_size\n        #      b. Call self.train_step(batch)\n        #      c. Call self.maybe_recalibrate_directions()\n        #      d. Every eval_interval steps, run evaluation:\n        #         - Direction AUROC on held-out pairs\n        #         - Warranted revision rate\n        #         - Unwarranted capitulation rate\n        #         - Log to wandb if configured\n        #      e. Checkpoint model and directions\n        #   3. Return training history\n        raise NotImplementedError(\"DCGRPOTrainer.train\")\n\n    def evaluate(self, eval_dataset: Any) -> dict[str, float]:\n        \"\"\"Evaluate current model on held-out calibration pairs.\n\n        Computes:\n          - Direction AUROC: classification accuracy of d_syc/d_gen projections\n            on held-out sycophantic vs. genuine agreement examples\n          - Warranted Revision Rate: fraction of warranted_revision pairs where\n            the model correctly revises\n          - Unwarranted Capitulation Rate: fraction of sycophantic_capitulation\n            pairs where the model incorrectly capitulates\n          - R1-R3 disagreement frequency\n\n        Args:\n            eval_dataset: Held-out calibration pairs.\n\n        Returns:\n            Dict of evaluation metrics.\n        \"\"\"\n        # TODO: implement\n        raise NotImplementedError(\"DCGRPOTrainer.evaluate\")\n\n\n# ---------------------------------------------------------------------------\n# Configuration\n# ---------------------------------------------------------------------------\n\n@dataclass\nclass DCGRPOConfig:\n    \"\"\"Full configuration for DC-GRPO training.\"\"\"\n\n    # Model\n    model_path: str = \"Qwen/Qwen3-8B\"\n    tokenizer_path: str | None = None  # defaults to model_path\n\n    # Directions (from compute_directions.py / Phase 3)\n    directions_path: str = \"\"\n    target_layers: list[int] = field(\n        default_factory=lambda: [10, 11, 12, 13, 14, 24, 25, 26, 27, 28]\n    )\n    # mid-layers (10-15) + deep layers (20-28) per IDEA_BRIEF\n\n    # Data\n    data_path: str = \"\"\n    eval_data_path: str = \"\"\n    max_turns: int = 5\n\n    # Reward weights: R = alpha * R1 + beta * R2 + gamma * R3\n    reward_weights: dict[str, float] = field(\n        default_factory=lambda: {\"r1\": 0.4, \"r2\": 0.3, \"r3\": 0.3}\n    )\n\n    # LoRA\n    lora_rank: int = 64\n    lora_alpha: int = 128\n    lora_dropout: float = 0.05\n    lora_target_modules: list[str] = field(\n        default_factory=lambda: [\"q_proj\", \"k_proj\", \"v_proj\", \"o_proj\",\n                                 \"gate_proj\", \"up_proj\", \"down_proj\"]\n    )\n\n    # GRPO\n    num_rollouts: int = 4  # group size (responses per prompt)\n    clip_eps: float = 0.2  # PPO-style clipping\n    kl_coeff: float = 0.05  # KL penalty coefficient\n    temperature: float = 0.7\n    top_p: float = 0.95\n    max_new_tokens: int = 512\n\n    # Training\n    batch_size: int = 2  # calibration pairs per step\n    learning_rate: float = 1e-5\n    weight_decay: float = 0.01\n    warmup_steps: int = 100\n    total_steps: int = 5000\n    gradient_accumulation_steps: int = 4\n    max_grad_norm: float = 1.0\n\n    # Direction recalibration\n    recalib_interval: int = 500\n    recalib_buffer_size: int = 200  # rollouts to keep for recalibration\n    direction_stability_threshold: float = 0.7  # cosine warning threshold\n\n    # Evaluation\n    eval_interval: int = 500\n\n    # NLI model for R3\n    nli_model_name: str = \"microsoft/deberta-v3-base\"\n\n    # Infrastructure\n    device: str = \"cuda:0\"\n    dtype: str = \"bfloat16\"\n    seed: int = 42\n    output_dir: str = \"./output\"\n    wandb_project: str = \"\"\n    wandb_run_name: str = \"\"\n\n    def validate(self) -> None:\n        \"\"\"Check config consistency.\"\"\"\n        w = self.reward_weights\n        assert set(w.keys()) == {\"r1\", \"r2\", \"r3\"}, (\n            f\"reward_weights must have keys r1, r2, r3; got {set(w.keys())}\"\n        )\n        assert abs(sum(w.values()) - 1.0) < 1e-6, (\n            f\"reward_weights must sum to 1.0; got {sum(w.values())}\"\n        )\n        assert self.lora_rank > 0, \"lora_rank must be positive\"\n        assert self.num_rollouts >= 2, \"GRPO requires at least 2 rollouts per group\"\n\n\n# ---------------------------------------------------------------------------\n# CLI Entry Point\n# ---------------------------------------------------------------------------\n\ndef build_trainer_from_config(config: DCGRPOConfig) -> DCGRPOTrainer:\n    \"\"\"Construct all components and return a ready-to-train DCGRPOTrainer.\n\n    Args:\n        config: Validated DCGRPOConfig.\n\n    Returns:\n        DCGRPOTrainer instance (call .train() to start).\n    \"\"\"\n    # TODO: implement\n    #   1. Load base model with torch_dtype from config\n    #   2. Apply LoRA (peft.get_peft_model with LoraConfig)\n    #   3. Load tokenizer\n    #   4. Create reference model (frozen copy or peft reference)\n    #   5. Instantiate reward components (R1, R2, R3)\n    #   6. Construct DCGRPOTrainer\n    #   7. Return trainer\n    #\n    # Example:\n    #   from transformers import AutoModelForCausalLM, AutoTokenizer\n    #   from peft import LoraConfig, get_peft_model\n    #\n    #   dtype_map = {\"bfloat16\": torch.bfloat16, \"float16\": torch.float16}\n    #   model = AutoModelForCausalLM.from_pretrained(\n    #       config.model_path,\n    #       torch_dtype=dtype_map[config.dtype],\n    #       device_map=config.device,\n    #   )\n    #   lora_cfg = LoraConfig(\n    #       r=config.lora_rank,\n    #       lora_alpha=config.lora_alpha,\n    #       lora_dropout=config.lora_dropout,\n    #       target_modules=config.lora_target_modules,\n    #       task_type=\"CAUSAL_LM\",\n    #   )\n    #   model = get_peft_model(model, lora_cfg)\n    #   tokenizer = AutoTokenizer.from_pretrained(\n    #       config.tokenizer_path or config.model_path\n    #   )\n    #   r1 = DirectionAlignmentReward(config.directions_path, config.target_layers)\n    #   r2 = ContrastiveConsistencyReward(config.directions_path, config.target_layers)\n    #   r3 = BehavioralReward(config.nli_model_name, config.device)\n    #   trainer = DCGRPOTrainer(model, tokenizer, None, r1, r2, r3, config)\n    #   return trainer\n    raise NotImplementedError(\"build_trainer_from_config\")\n\n\ndef main() -> None:\n    \"\"\"CLI entry point: parse args, build config, run training.\"\"\"\n    import argparse\n\n    parser = argparse.ArgumentParser(description=\"DC-GRPO Training\")\n    parser.add_argument(\"--model-path\", required=True, help=\"Base model path\")\n    parser.add_argument(\"--directions-path\", required=True, help=\"directions.pt path\")\n    parser.add_argument(\"--data-path\", required=True, help=\"Calibration data JSONL\")\n    parser.add_argument(\"--eval-data-path\", default=\"\", help=\"Eval data JSONL\")\n    parser.add_argument(\"--output-dir\", default=\"./output\", help=\"Output directory\")\n    parser.add_argument(\"--target-layers\", type=int, nargs=\"+\",\n                        default=[10, 11, 12, 13, 14, 24, 25, 26, 27, 28])\n    parser.add_argument(\"--r1-weight\", type=float, default=0.4)\n    parser.add_argument(\"--r2-weight\", type=float, default=0.3)\n    parser.add_argument(\"--r3-weight\", type=float, default=0.3)\n    parser.add_argument(\"--lora-rank\", type=int, default=64)\n    parser.add_argument(\"--num-rollouts\", type=int, default=4)\n    parser.add_argument(\"--batch-size\", type=int, default=2)\n    parser.add_argument(\"--learning-rate\", type=float, default=1e-5)\n    parser.add_argument(\"--total-steps\", type=int, default=5000)\n    parser.add_argument(\"--recalib-interval\", type=int, default=500)\n    parser.add_argument(\"--seed\", type=int, default=42)\n    parser.add_argument(\"--wandb-project\", default=\"\")\n    parser.add_argument(\"--wandb-run-name\", default=\"\")\n    args = parser.parse_args()\n\n    config = DCGRPOConfig(\n        model_path=args.model_path,\n        directions_path=args.directions_path,\n        data_path=args.data_path,\n        eval_data_path=args.eval_data_path,\n        output_dir=args.output_dir,\n        target_layers=args.target_layers,\n        reward_weights={\n            \"r1\": args.r1_weight,\n            \"r2\": args.r2_weight,\n            \"r3\": args.r3_weight,\n        },\n        lora_rank=args.lora_rank,\n        num_rollouts=args.num_rollouts,\n        batch_size=args.batch_size,\n        learning_rate=args.learning_rate,\n        total_steps=args.total_steps,\n        recalib_interval=args.recalib_interval,\n        seed=args.seed,\n        wandb_project=args.wandb_project,\n        wandb_run_name=args.wandb_run_name,\n    )\n    config.validate()\n\n    trainer = build_trainer_from_config(config)\n    trainer.train(\n        dataset=None,  # TODO: load from config.data_path\n        eval_dataset=None,  # TODO: load from config.eval_data_path\n    )\n\n\nif __name__ == \"__main__\":\n    main()\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b4f60a65-bd31-44db-9acc-b5cb02ffadf2",
  "uuid": "7d02f467-80d0-4714-aeb1-99f0b7496e29",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W3CX2m4jc4Kzm9g2H7kNxS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1267,
      "cache_read_input_tokens": 56433,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1267
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

_source line 51 · 2026-05-18T07:59:03.265Z_

<details><summary>↩ Tool result · `toolu_01JhHLHJAvwtkyktQp6SX9i7`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/training/grpo_framework.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b4f60a65-bd31-44db-9acc-b5cb02ffadf2",
  "uuid": "76c75562-8b4d-4ef9-9326-fe3aa413b80b",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/training/grpo_framework.py",
    "content": "#!/usr/bin/env python3\n\"\"\"DC-GRPO (Direction-Contrastive GRPO) Training Framework\n\nArchitecture overview:\n  1. ActivationExtractionHook  — registers forward hooks to capture hidden states\n                                  at target layers during training forward passes\n  2. MultiTurnRolloutGenerator — generates multi-turn dialogue rollouts from\n                                  calibration pairs and extracts critical-turn activations\n  3. DirectionAlignmentReward  — R1: cosine projection onto d_syc / d_gen directions\n  4. ContrastiveConsistencyReward — R2: cross-rollout directional projection contrast\n  5. BehavioralReward          — R3: NLI-based stance consistency scoring\n  6. DCGRPOTrainer             — orchestrates rollout, activation extraction, reward\n                                  computation, and GRPO policy updates\n  7. DCGRPOConfig              — dataclass holding all hyperparameters\n\nDependencies: torch, transformers, trl, peft, numpy\nOptional:     transformers (DeBERTa for R3 NLI scoring)\n\nDirection format (from compute_directions.py):\n  d_syc, d_gen: Tensor(num_layers, 2, hidden_dim)\n    dim-1 index 0 = user last content token position\n    dim-1 index 1 = assistant first content token position\n  Both are L2-normalized per (layer, position) slice.\n\nReward formulas:\n  R1(h, condition) =\n    -cos(h[layer, pos], d_syc[layer, pos])   if condition == sycophantic_capitulation\n    +cos(h[layer, pos], d_gen[layer, pos])    if condition == warranted_revision\n  R2(h_wr, h_sc) =\n    cos(h_wr[layer, pos], d_gen[layer, pos]) - cos(h_sc[layer, pos], d_syc[layer, pos])\n  R3(response, ground_truth, condition) =\n    +1 if behavior matches expected (revise when warranted / maintain when unwarranted)\n    -1 otherwise\n  R_total = alpha * R1 + beta * R2 + gamma * R3\n\"\"\"\n\nfrom __future__ import annotations\n\nimport logging\nfrom dataclasses import dataclass, field\nfrom typing import Any\n\nimport torch\nimport torch.nn as nn\nimport torch.nn.functional as F\n\nlogger = logging.getLogger(__name__)\n\n\n# ---------------------------------------------------------------------------\n# Activation Extraction Hook\n# ---------------------------------------------------------------------------\n\nclass ActivationExtractionHook:\n    \"\"\"Captures hidden-state activations at specified transformer layers during forward pass.\n\n    Unlike offline extraction (extract_activations.py) which calls model() with\n    output_hidden_states=True, this hook attaches to specific layers and works\n    during training forward passes where output_hidden_states may not be available\n    or would add unnecessary memory overhead.\n\n    Usage:\n        hook = ActivationExtractionHook(target_layers=[10, 12, 14, 24, 26])\n        hook.register(model)\n        outputs = model(input_ids=..., attention_mask=...)\n        acts = hook.get_activations()  # {layer_idx: Tensor(batch, seq_len, hidden_dim)}\n        hook.clear()\n    \"\"\"\n\n    def __init__(self, target_layers: list[int]):\n        \"\"\"\n        Args:\n            target_layers: 0-indexed transformer layer indices to capture.\n                           Typically mid-layers (10-15) + deep layers (20-28).\n        \"\"\"\n        self.target_layers = sorted(target_layers)\n        self._activations: dict[int, torch.Tensor] = {}\n        self._handles: list[Any] = []\n\n    def register(self, model: nn.Module) -> None:\n        \"\"\"Attach forward hooks to target layers of the model.\n\n        Expects model.model.layers[i] (standard HuggingFace causal LM layout).\n        \"\"\"\n        self.remove()\n        # TODO: resolve layer accessor for different model architectures\n        #       currently assumes model.model.layers (Qwen, Llama, Mistral)\n        layers = model.model.layers\n        for layer_idx in self.target_layers:\n            if layer_idx >= len(layers):\n                raise ValueError(\n                    f\"Layer {layer_idx} out of range (model has {len(layers)} layers)\"\n                )\n            handle = layers[layer_idx].register_forward_hook(\n                self._make_hook(layer_idx)\n            )\n            self._handles.append(handle)\n        logger.info(\"Registered activation hooks on layers %s\", self.target_layers)\n\n    def _make_hook(self, layer_idx: int):\n        def hook_fn(module, input, output):\n            # output is typically (hidden_states, ...) or just hidden_states\n            if isinstance(output, tuple):\n                hidden = output[0]\n            else:\n                hidden = output\n            # Detach to avoid retaining the computation graph through the hook\n            self._activations[layer_idx] = hidden.detach()\n        return hook_fn\n\n    def get_activations(self) -> dict[int, torch.Tensor]:\n        \"\"\"Return captured activations: {layer_idx: Tensor(batch, seq_len, hidden_dim)}.\"\"\"\n        return dict(self._activations)\n\n    def extract_at_positions(\n        self,\n        positions: dict[int, tuple[int, int]],\n    ) -> dict[int, dict[int, torch.Tensor]]:\n        \"\"\"Extract activations at specific (user_pos, asst_pos) for each sample in batch.\n\n        Args:\n            positions: {batch_idx: (user_last_pos, asst_first_pos)}\n\n        Returns:\n            {layer_idx: {batch_idx: Tensor(2, hidden_dim)}}\n            where dim-0: [user_last_token, asst_first_token]\n        \"\"\"\n        result: dict[int, dict[int, torch.Tensor]] = {}\n        for layer_idx, hidden in self._activations.items():\n            result[layer_idx] = {}\n            for batch_idx, (user_pos, asst_pos) in positions.items():\n                user_vec = hidden[batch_idx, user_pos, :]\n                asst_vec = hidden[batch_idx, asst_pos, :]\n                result[layer_idx][batch_idx] = torch.stack([user_vec, asst_vec], dim=0)\n        return result\n\n    def clear(self) -> None:\n        \"\"\"Discard stored activations to free memory.\"\"\"\n        self._activations.clear()\n\n    def remove(self) -> None:\n        \"\"\"Remove all registered hooks and clear activations.\"\"\"\n        for h in self._handles:\n            h.remove()\n        self._handles.clear()\n        self._activations.clear()\n\n\n# ---------------------------------------------------------------------------\n# Multi-Turn Rollout Generator\n# ---------------------------------------------------------------------------\n\nclass MultiTurnRolloutGenerator:\n    \"\"\"Generates multi-turn dialogue rollouts from calibration pairs.\n\n    For GRPO, multiple rollouts (responses) are sampled for each prompt.\n    Each rollout captures the model's response at the critical turn along\n    with the hidden-state activations needed for R1/R2 reward computation.\n\n    Reuses token boundary detection logic from extract_activations.py\n    (find_critical_positions) adapted for online generation.\n    \"\"\"\n\n    def __init__(\n        self,\n        tokenizer: Any,\n        activation_hook: ActivationExtractionHook,\n        max_new_tokens: int = 512,\n        max_turns: int = 5,\n        num_rollouts: int = 4,\n        temperature: float = 0.7,\n        top_p: float = 0.95,\n    ):\n        \"\"\"\n        Args:\n            tokenizer: HuggingFace tokenizer with chat template support.\n            activation_hook: Hook instance (already registered on the model).\n            max_new_tokens: Maximum tokens to generate per assistant turn.\n            max_turns: Maximum number of dialogue turns (truncate longer dialogues).\n            num_rollouts: Number of rollout samples per prompt (GRPO group size).\n            temperature: Sampling temperature for generation.\n            top_p: Nucleus sampling threshold.\n        \"\"\"\n        self.tokenizer = tokenizer\n        self.activation_hook = activation_hook\n        self.max_new_tokens = max_new_tokens\n        self.max_turns = max_turns\n        self.num_rollouts = num_rollouts\n        self.temperature = temperature\n        self.top_p = top_p\n\n    def generate_rollouts(\n        self,\n        model: nn.Module,\n        prompt_pair: dict,\n    ) -> list[dict]:\n        \"\"\"Generate multiple rollouts for a calibration prompt pair.\n\n        Args:\n            model: The policy model (with LoRA adapters).\n            prompt_pair: Dict with keys:\n                - id: str (pair identifier)\n                - condition: \"warranted_revision\" | \"sycophantic_capitulation\"\n                - turns: list[dict] with role/content (conversation up to critical turn)\n                - correction_turn: int (1-indexed critical turn number)\n                - ground_truth: dict with expected behavior metadata\n\n        Returns:\n            List of rollout dicts, each containing:\n                - response: str (generated assistant response at critical turn)\n                - input_ids: Tensor (full input sequence)\n                - activations: dict {layer_idx: Tensor(2, hidden_dim)}\n                - user_pos: int\n                - asst_pos: int\n                - metadata: dict (pair_id, condition, etc.)\n        \"\"\"\n        # TODO: implement rollout generation\n        #   1. Build input from turns up to and including the critical user turn\n        #   2. Use tokenizer.apply_chat_template with add_generation_prompt=True\n        #   3. Call model.generate() with num_return_sequences=self.num_rollouts\n        #   4. For each generated response, re-run forward pass with activation hook\n        #      to extract hidden states at the critical positions\n        #   5. Use find_critical_positions logic (adapted from extract_activations.py)\n        #      to locate user_last_token and asst_first_token boundaries\n        #   6. Return list of rollout dicts\n        #\n        # Key considerations:\n        # - Generation uses sampling (temperature, top_p) for diversity across rollouts\n        # - After generation, a separate forward pass through the full sequence\n        #   (context + generated response) is needed to extract activations at the\n        #   exact critical positions, because generate() doesn't expose intermediate\n        #   hidden states at arbitrary positions\n        # - Memory management: clear activation hook after each extraction\n        raise NotImplementedError(\"MultiTurnRolloutGenerator.generate_rollouts\")\n\n    def _find_critical_positions(\n        self,\n        turns: list[dict],\n        correction_turn: int,\n    ) -> tuple[int, int, list[int]]:\n        \"\"\"Locate critical token positions in tokenized conversation.\n\n        Mirrors extract_activations.find_critical_positions but adapted for\n        online use within the training loop.\n\n        Returns:\n            (user_last_pos, asst_first_pos, full_input_ids)\n        \"\"\"\n        # TODO: port find_critical_positions from extract_activations.py\n        #   - Tokenize through user turn to find user_last_content_token\n        #   - Tokenize with add_generation_prompt to find asst_first_content_token\n        #   - Handle Qwen3 chat template quirks (enable_thinking=False)\n        raise NotImplementedError(\n            \"MultiTurnRolloutGenerator._find_critical_positions\"\n        )\n\n\n# ---------------------------------------------------------------------------\n# R1: Direction Alignment Reward\n# ---------------------------------------------------------------------------\n\nclass DirectionAlignmentReward:\n    \"\"\"R1: Directional projection reward targeting sycophantic vs. genuine pathways.\n\n    Computes cosine similarity between the policy model's hidden-state activation\n    at the critical turn and the pre-computed contrastive directions (d_syc, d_gen).\n\n    Math:\n      For sycophantic_capitulation condition:\n        R1 = -cos(h[layer, pos], d_syc[layer, pos])\n        (penalize activations aligned with sycophantic direction)\n\n      For warranted_revision condition:\n        R1 = +cos(h[layer, pos], d_gen[layer, pos])\n        (reward activations aligned with genuine revision direction)\n\n    When using multiple layers, the reward is averaged across target layers.\n    The position index (0=user_last, 1=asst_first) is configurable; default\n    is asst_first (index 1), as the assistant's first response token carries\n    the strongest signal about the model's internal decision.\n    \"\"\"\n\n    def __init__(\n        self,\n        directions_path: str,\n        target_layers: list[int],\n        position_idx: int = 1,\n    ):\n        \"\"\"\n        Args:\n            directions_path: Path to directions.pt (from compute_directions.py).\n                             Contains d_syc, d_gen of shape (num_layers, 2, hidden_dim).\n            target_layers: Transformer layer indices for projection (0-indexed).\n            position_idx: Token position index (0=user_last, 1=asst_first).\n        \"\"\"\n        self.target_layers = target_layers\n        self.position_idx = position_idx\n\n        # TODO: load directions and move to device\n        #   data = torch.load(directions_path, map_location=\"cpu\")\n        #   self.d_syc = data[\"d_syc\"]  # (num_layers, 2, hidden_dim)\n        #   self.d_gen = data[\"d_gen\"]  # (num_layers, 2, hidden_dim)\n        self.d_syc: torch.Tensor | None = None\n        self.d_gen: torch.Tensor | None = None\n        self._directions_path = directions_path\n\n    def load_directions(self, device: torch.device) -> None:\n        \"\"\"Load direction vectors from disk and move to device.\"\"\"\n        # TODO: implement\n        #   data = torch.load(self._directions_path, map_location=\"cpu\", weights_only=False)\n        #   self.d_syc = data[\"d_syc\"].to(device)\n        #   self.d_gen = data[\"d_gen\"].to(device)\n        raise NotImplementedError(\"DirectionAlignmentReward.load_directions\")\n\n    def compute(\n        self,\n        activations: dict[int, torch.Tensor],\n        condition: str,\n    ) -> float:\n        \"\"\"Compute R1 reward for a single rollout.\n\n        Args:\n            activations: {layer_idx: Tensor(2, hidden_dim)} from ActivationExtractionHook.\n            condition: \"warranted_revision\" or \"sycophantic_capitulation\".\n\n        Returns:\n            Scalar R1 reward, averaged over target layers.\n        \"\"\"\n        # TODO: implement\n        #   scores = []\n        #   for layer in self.target_layers:\n        #       h = activations[layer][self.position_idx]        # (hidden_dim,)\n        #       if condition == \"sycophantic_capitulation\":\n        #           d = self.d_syc[layer, self.position_idx]     # (hidden_dim,)\n        #           score = -F.cosine_similarity(h.unsqueeze(0), d.unsqueeze(0)).item()\n        #       elif condition == \"warranted_revision\":\n        #           d = self.d_gen[layer, self.position_idx]\n        #           score = F.cosine_similarity(h.unsqueeze(0), d.unsqueeze(0)).item()\n        #       else:\n        #           raise ValueError(f\"Unknown condition: {condition}\")\n        #       scores.append(score)\n        #   return sum(scores) / len(scores)\n        raise NotImplementedError(\"DirectionAlignmentReward.compute\")\n\n    def compute_batch(\n        self,\n        batch_activations: list[dict[int, torch.Tensor]],\n        conditions: list[str],\n    ) -> list[float]:\n        \"\"\"Compute R1 for a batch of rollouts.\n\n        Args:\n            batch_activations: List of per-rollout activation dicts.\n            conditions: List of condition strings, one per rollout.\n\n        Returns:\n            List of R1 scalar rewards.\n        \"\"\"\n        # TODO: vectorized batch implementation for efficiency\n        #   For now, loop over individual compute() calls\n        return [\n            self.compute(acts, cond)\n            for acts, cond in zip(batch_activations, conditions)\n        ]\n\n    def update_directions(self, new_directions_path: str, device: torch.device) -> None:\n        \"\"\"Reload directions after recalibration (every ~500 training steps).\n\n        Args:\n            new_directions_path: Path to recalibrated directions.pt.\n            device: Target device.\n        \"\"\"\n        # TODO: implement hot-reload of recalibrated directions\n        #   self._directions_path = new_directions_path\n        #   self.load_directions(device)\n        raise NotImplementedError(\"DirectionAlignmentReward.update_directions\")\n\n\n# ---------------------------------------------------------------------------\n# R2: Contrastive Consistency Reward\n# ---------------------------------------------------------------------------\n\nclass ContrastiveConsistencyReward:\n    \"\"\"R2: Cross-condition contrastive reward using directional projections.\n\n    Exploits GRPO's group-relative structure by comparing directional projections\n    across the two conditions of the same calibration pair.\n\n    Math:\n      R2 = cos(h_wr[layer, pos], d_gen[layer, pos])\n         - cos(h_sc[layer, pos], d_syc[layer, pos])\n\n    where:\n      h_wr = activation from a warranted_revision rollout\n      h_sc = activation from a sycophantic_capitulation rollout\n      on the same underlying calibration pair.\n\n    Higher R2 means the model produces representations that are well-separated\n    along the intended directions: high d_gen alignment for genuine revision\n    and low d_syc alignment for sycophantic capitulation.\n    \"\"\"\n\n    def __init__(\n        self,\n        directions_path: str,\n        target_layers: list[int],\n        position_idx: int = 1,\n    ):\n        \"\"\"\n        Args:\n            directions_path: Path to directions.pt.\n            target_layers: Transformer layer indices for projection.\n            position_idx: Token position index (0=user_last, 1=asst_first).\n        \"\"\"\n        self.target_layers = target_layers\n        self.position_idx = position_idx\n        self.d_syc: torch.Tensor | None = None\n        self.d_gen: torch.Tensor | None = None\n        self._directions_path = directions_path\n\n    def compute(\n        self,\n        activations_wr: dict[int, torch.Tensor],\n        activations_sc: dict[int, torch.Tensor],\n    ) -> float:\n        \"\"\"Compute R2 for a paired set of rollouts.\n\n        Args:\n            activations_wr: Activations from warranted_revision rollout.\n                            {layer_idx: Tensor(2, hidden_dim)}\n            activations_sc: Activations from sycophantic_capitulation rollout.\n                            {layer_idx: Tensor(2, hidden_dim)}\n\n        Returns:\n            Scalar R2 reward, averaged over target layers.\n        \"\"\"\n        # TODO: implement\n        #   scores = []\n        #   for layer in self.target_layers:\n        #       h_wr = activations_wr[layer][self.position_idx]\n        #       h_sc = activations_sc[layer][self.position_idx]\n        #       gen_proj = F.cosine_similarity(\n        #           h_wr.unsqueeze(0), self.d_gen[layer, self.position_idx].unsqueeze(0)\n        #       ).item()\n        #       syc_proj = F.cosine_similarity(\n        #           h_sc.unsqueeze(0), self.d_syc[layer, self.position_idx].unsqueeze(0)\n        #       ).item()\n        #       scores.append(gen_proj - syc_proj)\n        #   return sum(scores) / len(scores)\n        raise NotImplementedError(\"ContrastiveConsistencyReward.compute\")\n\n    def compute_group(\n        self,\n        rollouts_wr: list[dict[int, torch.Tensor]],\n        rollouts_sc: list[dict[int, torch.Tensor]],\n    ) -> list[float]:\n        \"\"\"Compute R2 for all pairs in a GRPO group.\n\n        GRPO samples multiple rollouts per prompt. R2 is computed for each\n        (wr_rollout, sc_rollout) pairing within the same calibration pair.\n\n        Args:\n            rollouts_wr: List of activation dicts from warranted_revision rollouts.\n            rollouts_sc: List of activation dicts from sycophantic_capitulation rollouts.\n\n        Returns:\n            List of R2 rewards (one per wr-sc pair, or aggregated per rollout).\n        \"\"\"\n        # TODO: implement cross-rollout pairing strategy\n        #   Option A: pair by index (rollouts_wr[i] with rollouts_sc[i])\n        #   Option B: mean across all cross-pairs\n        #   Option C: max-contrast pair selection\n        raise NotImplementedError(\"ContrastiveConsistencyReward.compute_group\")\n\n    def update_directions(self, new_directions_path: str, device: torch.device) -> None:\n        \"\"\"Reload directions after recalibration.\"\"\"\n        # TODO: implement (same pattern as DirectionAlignmentReward)\n        raise NotImplementedError(\"ContrastiveConsistencyReward.update_directions\")\n\n\n# ---------------------------------------------------------------------------\n# R3: Behavioral Reward\n# ---------------------------------------------------------------------------\n\nclass BehavioralReward:\n    \"\"\"R3: Output-level behavioral correctness reward via NLI stance detection.\n\n    Evaluates whether the model's generated response exhibits the correct\n    behavior given the condition:\n      - warranted_revision: model SHOULD revise its prior incorrect answer\n        when presented with valid evidence -> reward revision, penalize stubbornness\n      - sycophantic_capitulation: model SHOULD maintain its prior correct answer\n        under social pressure -> reward maintenance, penalize capitulation\n\n    Stance detection uses DeBERTa-v3-base NLI to determine whether the\n    generated response agrees with the original position or the new position.\n\n    Scoring:\n      warranted_revision:\n        response revises to correct answer   -> +1\n        response maintains incorrect answer  -> -1\n      sycophantic_capitulation:\n        response maintains correct answer     -> +1\n        response capitulates to pressure      -> -1\n    \"\"\"\n\n    def __init__(\n        self,\n        nli_model_name: str = \"microsoft/deberta-v3-base\",\n        device: str = \"cuda:0\",\n    ):\n        \"\"\"\n        Args:\n            nli_model_name: HuggingFace model ID for NLI scoring.\n            device: Torch device for NLI model.\n        \"\"\"\n        self.nli_model_name = nli_model_name\n        self.device = device\n        self._nli_model = None\n        self._nli_tokenizer = None\n\n    def load_nli_model(self) -> None:\n        \"\"\"Lazily load the NLI model and tokenizer.\"\"\"\n        # TODO: implement\n        #   from transformers import AutoModelForSequenceClassification, AutoTokenizer\n        #   self._nli_tokenizer = AutoTokenizer.from_pretrained(self.nli_model_name)\n        #   self._nli_model = AutoModelForSequenceClassification.from_pretrained(\n        #       self.nli_model_name\n        #   ).to(self.device).eval()\n        raise NotImplementedError(\"BehavioralReward.load_nli_model\")\n\n    def compute(\n        self,\n        response: str,\n        ground_truth: dict,\n        condition: str,\n    ) -> float:\n        \"\"\"Compute R3 for a single rollout.\n\n        Args:\n            response: Generated assistant response text.\n            ground_truth: Dict containing:\n                - original_answer: str (model's initial position)\n                - correct_answer: str (ground truth)\n                - challenge_claim: str (user's challenge in the critical turn)\n            condition: \"warranted_revision\" or \"sycophantic_capitulation\".\n\n        Returns:\n            Scalar R3 reward in {-1, +1} (or continuous [-1, +1] with NLI confidence).\n        \"\"\"\n        # TODO: implement\n        #   1. Determine stance: does the response agree with original_answer\n        #      or with challenge_claim / correct_answer?\n        #   2. Use NLI to classify entailment/contradiction between:\n        #      - (response, original_answer) -> entailment = maintains position\n        #      - (response, correct_answer)  -> entailment = revised position\n        #   3. Map to reward based on condition:\n        #      warranted_revision:\n        #        revised -> +1 (or +nli_confidence for continuous version)\n        #        maintained -> -1\n        #      sycophantic_capitulation:\n        #        maintained -> +1\n        #        capitulated -> -1\n        #   4. Edge case: response is ambiguous or off-topic -> 0\n        raise NotImplementedError(\"BehavioralReward.compute\")\n\n    def compute_batch(\n        self,\n        responses: list[str],\n        ground_truths: list[dict],\n        conditions: list[str],\n    ) -> list[float]:\n        \"\"\"Compute R3 for a batch of rollouts.\n\n        Args:\n            responses: List of generated response texts.\n            ground_truths: List of ground truth dicts.\n            conditions: List of condition strings.\n\n        Returns:\n            List of R3 scalar rewards.\n        \"\"\"\n        # TODO: batch NLI inference for efficiency\n        return [\n            self.compute(resp, gt, cond)\n            for resp, gt, cond in zip(responses, ground_truths, conditions)\n        ]\n\n\n# ---------------------------------------------------------------------------\n# DC-GRPO Trainer\n# ---------------------------------------------------------------------------\n\nclass DCGRPOTrainer:\n    \"\"\"Direction-Contrastive GRPO Trainer.\n\n    Extends the TRL GRPOTrainer paradigm with representation-level reward\n    signals (R1, R2) alongside behavioral reward (R3).\n\n    Key differences from standard GRPO:\n      - Reward comes from directional projections on the policy model's own\n        activations, not from an external reward model\n      - Training operates on paired prompts (warranted_revision +\n        sycophantic_capitulation) from the same calibration pair\n      - Directions are periodically recalibrated using recent rollout activations\n      - Activation extraction hooks add ~5-10% overhead per forward pass\n\n    Training loop (per step):\n      1. Sample a batch of calibration pairs\n      2. Generate num_rollouts responses per condition per pair\n      3. Run forward pass with activation hooks to extract critical-turn activations\n      4. Compute R1 (per-rollout directional alignment)\n      5. Compute R2 (cross-condition contrastive projection)\n      6. Compute R3 (behavioral NLI scoring)\n      7. Combine: R = alpha * R1 + beta * R2 + gamma * R3\n      8. Apply GRPO policy gradient update using group-relative advantage\n      9. Every recalib_interval steps, recompute d_syc/d_gen from recent rollouts\n    \"\"\"\n\n    def __init__(\n        self,\n        model: nn.Module,\n        tokenizer: Any,\n        ref_model: nn.Module | None,\n        r1_reward: DirectionAlignmentReward,\n        r2_reward: ContrastiveConsistencyReward,\n        r3_reward: BehavioralReward,\n        config: DCGRPOConfig,\n    ):\n        \"\"\"\n        Args:\n            model: Policy model (with LoRA adapters applied).\n            tokenizer: HuggingFace tokenizer.\n            ref_model: Reference model for KL penalty (frozen copy or None).\n            r1_reward: Direction alignment reward component.\n            r2_reward: Contrastive consistency reward component.\n            r3_reward: Behavioral reward component.\n            config: Full training configuration.\n        \"\"\"\n        self.model = model\n        self.tokenizer = tokenizer\n        self.ref_model = ref_model\n        self.r1_reward = r1_reward\n        self.r2_reward = r2_reward\n        self.r3_reward = r3_reward\n        self.config = config\n\n        self.activation_hook = ActivationExtractionHook(\n            target_layers=config.target_layers\n        )\n        self.rollout_generator = MultiTurnRolloutGenerator(\n            tokenizer=tokenizer,\n            activation_hook=self.activation_hook,\n            max_new_tokens=config.max_new_tokens,\n            num_rollouts=config.num_rollouts,\n            temperature=config.temperature,\n        )\n\n        self._global_step = 0\n        self._optimizer = None\n        self._scheduler = None\n\n    def setup(self) -> None:\n        \"\"\"Initialize optimizer, scheduler, hooks, and reward models.\"\"\"\n        # TODO: implement\n        #   1. Register activation hooks on the policy model\n        #   2. Load directions for R1 and R2\n        #   3. Load NLI model for R3\n        #   4. Create optimizer (AdamW) with LoRA parameters only\n        #   5. Create learning rate scheduler\n        #   6. If ref_model is None, create a frozen copy for KL penalty\n        raise NotImplementedError(\"DCGRPOTrainer.setup\")\n\n    def compute_combined_reward(\n        self,\n        rollout: dict,\n        activations: dict[int, torch.Tensor],\n        paired_activations: dict[int, torch.Tensor] | None,\n        condition: str,\n        ground_truth: dict,\n    ) -> dict[str, float]:\n        \"\"\"Compute the combined three-component reward for a single rollout.\n\n        Args:\n            rollout: Rollout dict from MultiTurnRolloutGenerator.\n            activations: This rollout's activations {layer: Tensor(2, hidden_dim)}.\n            paired_activations: Activations from the paired condition's rollout\n                                (needed for R2). None if no paired rollout available.\n            condition: \"warranted_revision\" or \"sycophantic_capitulation\".\n            ground_truth: Ground truth dict for R3 scoring.\n\n        Returns:\n            Dict with keys: \"r1\", \"r2\", \"r3\", \"combined\", each a float.\n        \"\"\"\n        alpha = self.config.reward_weights[\"r1\"]\n        beta = self.config.reward_weights[\"r2\"]\n        gamma = self.config.reward_weights[\"r3\"]\n\n        # TODO: implement\n        #   r1 = self.r1_reward.compute(activations, condition)\n        #   if paired_activations is not None:\n        #       if condition == \"warranted_revision\":\n        #           r2 = self.r2_reward.compute(activations, paired_activations)\n        #       else:\n        #           r2 = self.r2_reward.compute(paired_activations, activations)\n        #   else:\n        #       r2 = 0.0\n        #   r3 = self.r3_reward.compute(rollout[\"response\"], ground_truth, condition)\n        #   combined = alpha * r1 + beta * r2 + gamma * r3\n        #   return {\"r1\": r1, \"r2\": r2, \"r3\": r3, \"combined\": combined}\n        raise NotImplementedError(\"DCGRPOTrainer.compute_combined_reward\")\n\n    def compute_grpo_loss(\n        self,\n        rollouts: list[dict],\n        rewards: list[float],\n    ) -> torch.Tensor:\n        \"\"\"Compute GRPO policy gradient loss with group-relative advantage.\n\n        GRPO normalizes rewards within each group (rollouts from the same prompt)\n        to compute advantages, then applies a clipped policy gradient objective.\n\n        Math:\n          advantage_i = (reward_i - mean(rewards_group)) / std(rewards_group)\n          ratio_i = pi_theta(response_i | prompt) / pi_ref(response_i | prompt)\n          loss = -mean(min(ratio_i * advantage_i, clip(ratio_i, 1-eps, 1+eps) * advantage_i))\n                 + beta_kl * KL(pi_theta || pi_ref)\n\n        Args:\n            rollouts: List of rollout dicts (with input_ids and response tokens).\n            rewards: List of combined reward scalars (one per rollout).\n\n        Returns:\n            Scalar loss tensor.\n        \"\"\"\n        # TODO: implement\n        #   1. Group rollouts by prompt (pair_id + condition)\n        #   2. For each group, normalize rewards to compute advantages:\n        #      advantages = (rewards - mean) / (std + eps)\n        #   3. Compute log-probabilities under policy and reference model\n        #   4. Compute importance sampling ratio: ratio = exp(logprob_policy - logprob_ref)\n        #   5. Clipped surrogate objective:\n        #      surr1 = ratio * advantage\n        #      surr2 = clamp(ratio, 1-clip_eps, 1+clip_eps) * advantage\n        #      loss = -mean(min(surr1, surr2))\n        #   6. Add KL penalty: beta_kl * mean(logprob_policy - logprob_ref)\n        #   7. Return combined loss\n        raise NotImplementedError(\"DCGRPOTrainer.compute_grpo_loss\")\n\n    def train_step(self, batch: list[dict]) -> dict[str, float]:\n        \"\"\"Execute one training step on a batch of calibration pairs.\n\n        Args:\n            batch: List of calibration pair dicts. Each pair has two conditions\n                   (warranted_revision and sycophantic_capitulation) sharing\n                   the same pair_id.\n\n        Returns:\n            Dict of training metrics:\n                - loss: total loss\n                - r1_mean, r2_mean, r3_mean: mean per-component rewards\n                - combined_reward_mean: mean combined reward\n                - r1_r3_disagreement: fraction where R1 and R3 give opposite signals\n        \"\"\"\n        # TODO: implement\n        #   1. For each pair in batch:\n        #      a. Generate rollouts for both conditions\n        #      b. Extract activations at critical positions\n        #      c. Compute rewards (R1, R2, R3) for each rollout\n        #   2. Flatten all rollouts and their rewards\n        #   3. Compute GRPO loss\n        #   4. Backward pass + optimizer step\n        #   5. Clear activation hook\n        #   6. Compute and return metrics (including R1-R3 disagreement frequency)\n        raise NotImplementedError(\"DCGRPOTrainer.train_step\")\n\n    def maybe_recalibrate_directions(self) -> None:\n        \"\"\"Recompute d_syc/d_gen from recent rollout activations if due.\n\n        Called every recalib_interval steps. Uses a buffer of recent rollout\n        activations (from the last recalib_interval steps) to recompute\n        directions via the same difference-in-means procedure as\n        compute_directions.py.\n\n        Monitors direction stability: if cosine(d_new, d_old) < 0.7,\n        log a warning (potential direction drift under LoRA training).\n        \"\"\"\n        # TODO: implement\n        #   1. Check if self._global_step % self.config.recalib_interval == 0\n        #   2. Collect recent rollout activations from the buffer\n        #   3. Separate by condition (warranted_revision vs. sycophantic_capitulation)\n        #   4. Compute new d_syc, d_gen via difference-in-means\n        #   5. Check cosine similarity with previous directions\n        #   6. If cosine < 0.7, log warning about direction drift\n        #   7. Update R1 and R2 with new directions\n        #   8. Save new directions to disk (for checkpointing)\n        raise NotImplementedError(\"DCGRPOTrainer.maybe_recalibrate_directions\")\n\n    def train(\n        self,\n        dataset: Any,\n        num_epochs: int = 1,\n        eval_dataset: Any | None = None,\n        eval_interval: int = 500,\n    ) -> dict[str, list[float]]:\n        \"\"\"Full training loop.\n\n        Args:\n            dataset: Iterable of calibration pair dicts.\n            num_epochs: Number of passes over the dataset.\n            eval_dataset: Optional held-out pairs for monitoring direction AUROC.\n            eval_interval: Steps between evaluation runs.\n\n        Returns:\n            Training history: {metric_name: [values_per_step]}.\n        \"\"\"\n        # TODO: implement\n        #   1. Call self.setup()\n        #   2. For each epoch:\n        #      a. Iterate over dataset in batches of config.batch_size\n        #      b. Call self.train_step(batch)\n        #      c. Call self.maybe_recalibrate_directions()\n        #      d. Every eval_interval steps, run evaluation:\n        #         - Direction AUROC on held-out pairs\n        #         - Warranted revision rate\n        #         - Unwarranted capitulation rate\n        #         - Log to wandb if configured\n        #      e. Checkpoint model and directions\n        #   3. Return training history\n        raise NotImplementedError(\"DCGRPOTrainer.train\")\n\n    def evaluate(self, eval_dataset: Any) -> dict[str, float]:\n        \"\"\"Evaluate current model on held-out calibration pairs.\n\n        Computes:\n          - Direction AUROC: classification accuracy of d_syc/d_gen projections\n            on held-out sycophantic vs. genuine agreement examples\n          - Warranted Revision Rate: fraction of warranted_revision pairs where\n            the model correctly revises\n          - Unwarranted Capitulation Rate: fraction of sycophantic_capitulation\n            pairs where the model incorrectly capitulates\n          - R1-R3 disagreement frequency\n\n        Args:\n            eval_dataset: Held-out calibration pairs.\n\n        Returns:\n            Dict of evaluation metrics.\n        \"\"\"\n        # TODO: implement\n        raise NotImplementedError(\"DCGRPOTrainer.evaluate\")\n\n\n# ---------------------------------------------------------------------------\n# Configuration\n# ---------------------------------------------------------------------------\n\n@dataclass\nclass DCGRPOConfig:\n    \"\"\"Full configuration for DC-GRPO training.\"\"\"\n\n    # Model\n    model_path: str = \"Qwen/Qwen3-8B\"\n    tokenizer_path: str | None = None  # defaults to model_path\n\n    # Directions (from compute_directions.py / Phase 3)\n    directions_path: str = \"\"\n    target_layers: list[int] = field(\n        default_factory=lambda: [10, 11, 12, 13, 14, 24, 25, 26, 27, 28]\n    )\n    # mid-layers (10-15) + deep layers (20-28) per IDEA_BRIEF\n\n    # Data\n    data_path: str = \"\"\n    eval_data_path: str = \"\"\n    max_turns: int = 5\n\n    # Reward weights: R = alpha * R1 + beta * R2 + gamma * R3\n    reward_weights: dict[str, float] = field(\n        default_factory=lambda: {\"r1\": 0.4, \"r2\": 0.3, \"r3\": 0.3}\n    )\n\n    # LoRA\n    lora_rank: int = 64\n    lora_alpha: int = 128\n    lora_dropout: float = 0.05\n    lora_target_modules: list[str] = field(\n        default_factory=lambda: [\"q_proj\", \"k_proj\", \"v_proj\", \"o_proj\",\n                                 \"gate_proj\", \"up_proj\", \"down_proj\"]\n    )\n\n    # GRPO\n    num_rollouts: int = 4  # group size (responses per prompt)\n    clip_eps: float = 0.2  # PPO-style clipping\n    kl_coeff: float = 0.05  # KL penalty coefficient\n    temperature: float = 0.7\n    top_p: float = 0.95\n    max_new_tokens: int = 512\n\n    # Training\n    batch_size: int = 2  # calibration pairs per step\n    learning_rate: float = 1e-5\n    weight_decay: float = 0.01\n    warmup_steps: int = 100\n    total_steps: int = 5000\n    gradient_accumulation_steps: int = 4\n    max_grad_norm: float = 1.0\n\n    # Direction recalibration\n    recalib_interval: int = 500\n    recalib_buffer_size: int = 200  # rollouts to keep for recalibration\n    direction_stability_threshold: float = 0.7  # cosine warning threshold\n\n    # Evaluation\n    eval_interval: int = 500\n\n    # NLI model for R3\n    nli_model_name: str = \"microsoft/deberta-v3-base\"\n\n    # Infrastructure\n    device: str = \"cuda:0\"\n    dtype: str = \"bfloat16\"\n    seed: int = 42\n    output_dir: str = \"./output\"\n    wandb_project: str = \"\"\n    wandb_run_name: str = \"\"\n\n    def validate(self) -> None:\n        \"\"\"Check config consistency.\"\"\"\n        w = self.reward_weights\n        assert set(w.keys()) == {\"r1\", \"r2\", \"r3\"}, (\n            f\"reward_weights must have keys r1, r2, r3; got {set(w.keys())}\"\n        )\n        assert abs(sum(w.values()) - 1.0) < 1e-6, (\n            f\"reward_weights must sum to 1.0; got {sum(w.values())}\"\n        )\n        assert self.lora_rank > 0, \"lora_rank must be positive\"\n        assert self.num_rollouts >= 2, \"GRPO requires at least 2 rollouts per group\"\n\n\n# ---------------------------------------------------------------------------\n# CLI Entry Point\n# ---------------------------------------------------------------------------\n\ndef build_trainer_from_config(config: DCGRPOConfig) -> DCGRPOTrainer:\n    \"\"\"Construct all components and return a ready-to-train DCGRPOTrainer.\n\n    Args:\n        config: Validated DCGRPOConfig.\n\n    Returns:\n        DCGRPOTrainer instance (call .train() to start).\n    \"\"\"\n    # TODO: implement\n    #   1. Load base model with torch_dtype from config\n    #   2. Apply LoRA (peft.get_peft_model with LoraConfig)\n    #   3. Load tokenizer\n    #   4. Create reference model (frozen copy or peft reference)\n    #   5. Instantiate reward components (R1, R2, R3)\n    #   6. Construct DCGRPOTrainer\n    #   7. Return trainer\n    #\n    # Example:\n    #   from transformers import AutoModelForCausalLM, AutoTokenizer\n    #   from peft import LoraConfig, get_peft_model\n    #\n    #   dtype_map = {\"bfloat16\": torch.bfloat16, \"float16\": torch.float16}\n    #   model = AutoModelForCausalLM.from_pretrained(\n    #       config.model_path,\n    #       torch_dtype=dtype_map[config.dtype],\n    #       device_map=config.device,\n    #   )\n    #   lora_cfg = LoraConfig(\n    #       r=config.lora_rank,\n    #       lora_alpha=config.lora_alpha,\n    #       lora_dropout=config.lora_dropout,\n    #       target_modules=config.lora_target_modules,\n    #       task_type=\"CAUSAL_LM\",\n    #   )\n    #   model = get_peft_model(model, lora_cfg)\n    #   tokenizer = AutoTokenizer.from_pretrained(\n    #       config.tokenizer_path or config.model_path\n    #   )\n    #   r1 = DirectionAlignmentReward(config.directions_path, config.target_layers)\n    #   r2 = ContrastiveConsistencyReward(config.directions_path, config.target_layers)\n    #   r3 = BehavioralReward(config.nli_model_name, config.device)\n    #   trainer = DCGRPOTrainer(model, tokenizer, None, r1, r2, r3, config)\n    #   return trainer\n    raise NotImplementedError(\"build_trainer_from_config\")\n\n\ndef main() -> None:\n    \"\"\"CLI entry point: parse args, build config, run training.\"\"\"\n    import argparse\n\n    parser = argparse.ArgumentParser(description=\"DC-GRPO Training\")\n    parser.add_argument(\"--model-path\", required=True, help=\"Base model path\")\n    parser.add_argument(\"--directions-path\", required=True, help=\"directions.pt path\")\n    parser.add_argument(\"--data-path\", required=True, help=\"Calibration data JSONL\")\n    parser.add_argument(\"--eval-data-path\", default=\"\", help=\"Eval data JSONL\")\n    parser.add_argument(\"--output-dir\", default=\"./output\", help=\"Output directory\")\n    parser.add_argument(\"--target-layers\", type=int, nargs=\"+\",\n                        default=[10, 11, 12, 13, 14, 24, 25, 26, 27, 28])\n    parser.add_argument(\"--r1-weight\", type=float, default=0.4)\n    parser.add_argument(\"--r2-weight\", type=float, default=0.3)\n    parser.add_argument(\"--r3-weight\", type=float, default=0.3)\n    parser.add_argument(\"--lora-rank\", type=int, default=64)\n    parser.add_argument(\"--num-rollouts\", type=int, default=4)\n    parser.add_argument(\"--batch-size\", type=int, default=2)\n    parser.add_argument(\"--learning-rate\", type=float, default=1e-5)\n    parser.add_argument(\"--total-steps\", type=int, default=5000)\n    parser.add_argument(\"--recalib-interval\", type=int, default=500)\n    parser.add_argument(\"--seed\", type=int, default=42)\n    parser.add_argument(\"--wandb-project\", default=\"\")\n    parser.add_argument(\"--wandb-run-name\", default=\"\")\n    args = parser.parse_args()\n\n    config = DCGRPOConfig(\n        model_path=args.model_path,\n        directions_path=args.directions_path,\n        data_path=args.data_path,\n        eval_data_path=args.eval_data_path,\n        output_dir=args.output_dir,\n        target_layers=args.target_layers,\n        reward_weights={\n            \"r1\": args.r1_weight,\n            \"r2\": args.r2_weight,\n            \"r3\": args.r3_weight,\n        },\n        lora_rank=args.lora_rank,\n        num_rollouts=args.num_rollouts,\n        batch_size=args.batch_size,\n        learning_rate=args.learning_rate,\n        total_steps=args.total_steps,\n        recalib_interval=args.recalib_interval,\n        seed=args.seed,\n        wandb_project=args.wandb_project,\n        wandb_run_name=args.wandb_run_name,\n    )\n    config.validate()\n\n    trainer = build_trainer_from_config(config)\n    trainer.train(\n        dataset=None,  # TODO: load from config.data_path\n        eval_dataset=None,  # TODO: load from config.eval_data_path\n    )\n\n\nif __name__ == \"__main__\":\n    main()\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 52_

验证语法。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b4f60a65-bd31-44db-9acc-b5cb02ffadf2",
  "uuid": "90e5844e-12fd-4867-a64f-e1a8fcfe7110",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TL6b1mDjBj5d88GVFo7Rpz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12226,
      "cache_read_input_tokens": 57700,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12226
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

_source line 53_

<details open><summary>🔧 Tool call — Bash · `toolu_012oCpdT7L17UPLwvi2rknTa`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-be-idea-gen-0515-3/projects/contrastive_entrain_calib/artifacts/training && python3 -c \"import ast; ast.parse(open('grpo_framework.py').read()); print('AST OK')\"",
  "description": "Verify Python syntax via AST parsing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b4f60a65-bd31-44db-9acc-b5cb02ffadf2",
  "uuid": "f3253273-2293-43f6-9277-c21ce5af62ba",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TL6b1mDjBj5d88GVFo7Rpz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12226,
      "cache_read_input_tokens": 57700,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12226
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

_source line 54 · 2026-05-18T07:59:08.694Z_

<details><summary>↩ Tool result · `toolu_012oCpdT7L17UPLwvi2rknTa`</summary>

```text
AST OK
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b4f60a65-bd31-44db-9acc-b5cb02ffadf2",
  "uuid": "aa2abd20-c532-4d22-8ec8-bda43cdca115",
  "tool_use_result": {
    "stdout": "AST OK",
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

_source line 55_

语法验证通过。文件已写入 `artifacts/training/grpo_framework.py`。

骨架包含 7 个核心组件：

| 组件 | 职责 |
|------|------|
| `ActivationExtractionHook` | 训练时 forward hook，捕获目标层 hidden states |
| `MultiTurnRolloutGenerator` | 多轮对话 rollout 生成 + 关键 turn 激活提取 |
| `DirectionAlignmentReward` | R1: 激活沿 d_syc/d_gen 的 cosine 投影 |
| `ContrastiveConsistencyReward` | R2: 跨 condition 投影差对比 |
| `BehavioralReward` | R3: DeBERTa NLI 行为评分 |
| `DCGRPOTrainer` | 完整训练循环（rollout → 激活提取 → 三路 reward → GRPO 更新 → 方向重校准） |
| `DCGRPOConfig` | 全部超参数（LoRA rank 64, reward weights, 方向重校准间隔 500 步等） |

所有具体实现标注 `TODO`，接口签名、参数类型、返回值类型、数学公式注释均已定义。方向格式与 `compute_directions.py` 输出对齐 `(num_layers, 2, hidden_dim)`，token 位置检测逻辑预留了从 `extract_activations.py` 移植的接口。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b4f60a65-bd31-44db-9acc-b5cb02ffadf2",
  "uuid": "92a9302c-bc05-4423-bf19-b14d763440e4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ARuYKsRQvMTeYDx5PxT7yX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 167,
      "cache_read_input_tokens": 69926,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 167
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

_source line 56_

语法验证通过。文件已写入 `artifacts/training/grpo_framework.py`。

骨架包含 7 个核心组件：

| 组件 | 职责 |
|------|------|
| `ActivationExtractionHook` | 训练时 forward hook，捕获目标层 hidden states |
| `MultiTurnRolloutGenerator` | 多轮对话 rollout 生成 + 关键 turn 激活提取 |
| `DirectionAlignmentReward` | R1: 激活沿 d_syc/d_gen 的 cosine 投影 |
| `ContrastiveConsistencyReward` | R2: 跨 condition 投影差对比 |
| `BehavioralReward` | R3: DeBERTa NLI 行为评分 |
| `DCGRPOTrainer` | 完整训练循环（rollout → 激活提取 → 三路 reward → GRPO 更新 → 方向重校准） |
| `DCGRPOConfig` | 全部超参数（LoRA rank 64, reward weights, 方向重校准间隔 500 步等） |

所有具体实现标注 `TODO`，接口签名、参数类型、返回值类型、数学公式注释均已定义。方向格式与 `compute_directions.py` 输出对齐 `(num_layers, 2, hidden_dim)`，token 位置检测逻辑预留了从 `extract_activations.py` 移植的接口。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 257440,
  "duration_api_ms": 257793,
  "num_turns": 13,
  "stop_reason": "end_turn",
  "session_id": "b4f60a65-bd31-44db-9acc-b5cb02ffadf2",
  "total_cost_usd": 0.9973838,
  "usage": {
    "input_tokens": 13,
    "cache_creation_input_tokens": 58252,
    "cache_read_input_tokens": 407143,
    "output_tokens": 15095,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 58252,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 429,
        "cache_read_input_tokens": 69926,
        "cache_creation_input_tokens": 167,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 167
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2294,
      "outputTokens": 984,
      "cacheReadInputTokens": 32858,
      "cacheCreationInputTokens": 33438,
      "webSearchRequests": 0,
      "costUSD": 0.052297300000000005,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 13,
      "outputTokens": 15095,
      "cacheReadInputTokens": 407143,
      "cacheCreationInputTokens": 58252,
      "webSearchRequests": 0,
      "costUSD": 0.9450865,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "339c522a-04d2-40fc-b6c5-cc0c3a88843d"
}
```

</details>

---
