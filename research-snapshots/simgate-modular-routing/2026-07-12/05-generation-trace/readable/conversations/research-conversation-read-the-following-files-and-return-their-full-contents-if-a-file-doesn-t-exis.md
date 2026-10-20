# Research conversation: Read the following files and return their full contents. If a file doesn't exist, say so. 1. /home/ubuntu/.agent-ml-rese

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a6463d3ca736dcafb.jsonl`
- **Structured JSON:** [`6a6871e533f78a3a93fa.json`](../../sessions/6a/6a6871e533f78a3a93fa.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

13 recorded events

### User

_source line 1 · 2026-05-14T11:19:27.487Z_

Read the following files and return their full contents. If a file doesn't exist, say so.

1. /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/registry.yaml
2. /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/report.md
3. /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/ROADMAP.md
4. /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/memory.md
5. /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/experiment_plan.yaml

Just read and return contents, no analysis needed.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "34ec326b-764d-435d-9ba6-0f4441293077",
  "agentId": "a6463d3ca736dcafb",
  "type": "user",
  "uuid": "5b28faf9-6e2b-4f05-a6c7-f8bd94fc4b9f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_da8ac8a0",
  "sessionId": "892078bb-1c00-49df-bb59-5753637855bb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-14T11:19:28.913Z_

I'll read all five files for you.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5b28faf9-6e2b-4f05-a6c7-f8bd94fc4b9f",
  "isSidechain": true,
  "agentId": "a6463d3ca736dcafb",
  "requestId": "req_011Cb2NT65m3N1PZSpXAAqcS",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "897581b3-345d-4f66-80f8-adee08a37b92",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_da8ac8a0",
  "sessionId": "892078bb-1c00-49df-bb59-5753637855bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011vaRmHEsXYdCmApbr62d3t",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1430,
      "cache_read_input_tokens": 30820,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1430,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-14T11:19:29.140Z_

<details open><summary>🔧 Tool call — Read · `toolu_01A662WN4nhR1o9EZ4Vacv4j`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/registry.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "897581b3-345d-4f66-80f8-adee08a37b92",
  "isSidechain": true,
  "agentId": "a6463d3ca736dcafb",
  "requestId": "req_011Cb2NT65m3N1PZSpXAAqcS",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8e3412f5-dd0f-4ca3-8461-627c72504ad9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_da8ac8a0",
  "sessionId": "892078bb-1c00-49df-bb59-5753637855bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011vaRmHEsXYdCmApbr62d3t",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1430,
      "cache_read_input_tokens": 30820,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1430,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-14T11:19:29.158Z_

<details><summary>↩ Tool result · reported error · `toolu_01A662WN4nhR1o9EZ4Vacv4j`</summary>

```text
File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_da8ac8a0.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8e3412f5-dd0f-4ca3-8461-627c72504ad9",
  "isSidechain": true,
  "promptId": "34ec326b-764d-435d-9ba6-0f4441293077",
  "agentId": "a6463d3ca736dcafb",
  "type": "user",
  "uuid": "6fac14c8-93a9-4fec-8b23-d2d6844713ec",
  "toolUseResult": "Error: File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_da8ac8a0.",
  "sourceToolAssistantUUID": "8e3412f5-dd0f-4ca3-8461-627c72504ad9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_da8ac8a0",
  "sessionId": "892078bb-1c00-49df-bb59-5753637855bb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-14T11:19:29.347Z_

<details open><summary>🔧 Tool call — Read · `toolu_01AxQ8kL6EbzHV2pFF3XJUf5`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6fac14c8-93a9-4fec-8b23-d2d6844713ec",
  "isSidechain": true,
  "agentId": "a6463d3ca736dcafb",
  "requestId": "req_011Cb2NT65m3N1PZSpXAAqcS",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d2015591-434c-4f5e-995d-22aa342bbdee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_da8ac8a0",
  "sessionId": "892078bb-1c00-49df-bb59-5753637855bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011vaRmHEsXYdCmApbr62d3t",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1430,
      "cache_read_input_tokens": 30820,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1430,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-14T11:19:29.354Z_

<details><summary>↩ Tool result · reported error · `toolu_01AxQ8kL6EbzHV2pFF3XJUf5`</summary>

```text
File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_da8ac8a0.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d2015591-434c-4f5e-995d-22aa342bbdee",
  "isSidechain": true,
  "promptId": "34ec326b-764d-435d-9ba6-0f4441293077",
  "agentId": "a6463d3ca736dcafb",
  "type": "user",
  "uuid": "df320e9b-bb1b-40e8-a665-d068e885a1e3",
  "toolUseResult": "Error: File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_da8ac8a0.",
  "sourceToolAssistantUUID": "d2015591-434c-4f5e-995d-22aa342bbdee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_da8ac8a0",
  "sessionId": "892078bb-1c00-49df-bb59-5753637855bb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-14T11:19:29.557Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VH56CL21PeLDS7xjLUCb5W`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/ROADMAP.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "df320e9b-bb1b-40e8-a665-d068e885a1e3",
  "isSidechain": true,
  "agentId": "a6463d3ca736dcafb",
  "requestId": "req_011Cb2NT65m3N1PZSpXAAqcS",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "3f62a2fc-7800-4948-a4c3-e970d4f420ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_da8ac8a0",
  "sessionId": "892078bb-1c00-49df-bb59-5753637855bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011vaRmHEsXYdCmApbr62d3t",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1430,
      "cache_read_input_tokens": 30820,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1430,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-14T11:19:29.575Z_

<details><summary>↩ Tool result · `toolu_01VH56CL21PeLDS7xjLUCb5W`</summary>

```text
1	# simgate-modular-routing — Research Dashboard
2	
3	> 最后更新: 2026-05-14 09:19 UTC | 更新原因: D035/D036: trained-router e2e negative + seed 方差确认，Reviewer 行动项派发
4	
5	## 核心方向
6	Episode-level counterfactual analysis 揭示 LLM agent routing 的本质：death avoidance 占 ~90% routing signal（Δ_full=+29.60, Δ_nd=+2.84, DAF=90.41%, r=0.9698 p=8.12e-07），non-death 场景两种 modality 近似等效（例外：find-non-living-thing 零死亡仍有 Δ=+9.58）。论文贡献 = empirical finding + diagnostic methodology，非 router 架构。详见 paper_framing.md。
7	
8	## 投稿目标
9	EMNLP 2026 ARR short paper (4 pages)，DDL: 2026-05-25（剩余 11 天）
10	
11	## 当前阶段
12	**Paper Writing Sprint** — 核心实验全部完成。Paper Agent 写作中。Agent 处理 Reviewer 行动项（D032 核实 + seed 补注册）。
13	
14	## Router 训练总结 (D029 + D035 + D036)
15	- Classification head (v3-v6): 全退化为 always-det (D025)
16	- Generative SFT (v1): ga=8/ga=1 双对照均 NEGATIVE
17	- Ablation-b: 唯一非退化 (internal_recall=51.5%, seed 42)
18	  - **e2e eval NEGATIVE (D035)**: trained-router=-12.84 vs always-det=-9.47，16个 internal 决策增加 deaths (19.2% vs 16.3%)
19	  - **跨 seed 不稳定 (D036)**: balanced_acc 稳定 57-59%（学到信号），但 internal_recall 30pp+ 方差（决策边界 seed-dependent）
20	  - ga=8 确认为非退化必要条件 (vs v5 ga=1 → 26.7%)
21	- ⚠️ D032 准确性待查：v5 可能也用了 WeightedTrainer，真差异仅 ga
22	
23	## Death Decomposition 定稿结果（plan-012, 11 tasks / 245 episodes）
24	- Δ_full = **+29.60**, Δ_nd = **+2.84**, DAF = **90.41%**
25	- r = **0.9698**, p = 8.12e-07
26	- Label: det-preferred 86 / internal-preferred 9 / no-preference 150
27	- 例外: find-non-living-thing (n=40, 零死亡, Δ=+9.58)
28	
29	## Keywords v2
30	v1 ≈ always-det (85.8%), v2 ≈ always-internal (4.9%). Keyword heuristic 结构性失效。
31	
32	## 近期任务
33	- [x] plan-012 全量 death decomposition ✅
34	- [x] plan-011 rule-based keyword baseline ✅
35	- [x] Router 训练路线全面评估 (D029) ✅
36	- [x] plan-003-baseline-245eps baselines ✅
37	- [x] ablation-b generation-level eval ✅
38	- [x] ablation-b e2e eval (D035: negative, -12.84 vs -9.47) ✅
39	- [x] ablation-b 3-seed 复制 (D036: 非退化可复现，方差大) ✅
40	- [ ] **D032 核实**（Agent: git history 查 v5 WeightedTrainer）
41	- [ ] **3 seed 实验补注册 registry**
42	- [ ] Paper Agent Patch: Table 1 trained-router + Section 3.3 seed 稳定性
43	- [ ] Paper Agent Full Draft → 目标 5/17 初稿
44	- [ ] Review + 迭代 (5/17-24)
45	
46	## Critical Path
47	| 时间 | 任务 |
48	|------|------|
49	| 5/14 | D032 核实 + seed 补注册 + Paper Agent Experiments patch |
50	| 5/15-16 | Paper Agent 写作 (Method/Intro/RW/Conclusion/Abstract) |
51	| 5/17 | Paper Agent 交初稿 |
52	| 5/17-22 | Review 对抗迭代 |
53	| 5/23-24 | 终稿 + 提交 |
54	
55	## GPU 预算
56	- 服务器: westb-13313, 2× RTX 5090 32GB (cuda:0, cuda:1)
57	- 写作期间 GPU 空闲，可用于补充实验（logit-level seed eval 等）
58	
59	## 关键决策日志
60	
61	| ID | 日期 | 摘要 | 关联实验 |
62	|----|------|------|----------|
63	| D038 | 2026-05-14 | Table 1 统一用 eval_end_to_end.py: trained-router = - | plan-003-eval-implicit, plan-003-e2e-ablation-b-correct |
64	| D037 | 2026-05-14 | Table 1 统一使用 eval_end_to_end.py，trained-router = - | plan-003-eval-implicit, plan-003-e2e-ablation-b-correct |
65	| D036 | 2026-05-14 | Ablation-b 跨 seed 复制确认非退化可复现，但 internal_recall 方差  | plan-004-ablation-b, ablation-b-seed123, ablation-b-seed456, ablation-b-seed789 |
66	| D035 | 2026-05-14 | Trained router e2e 确认 negative (-12.84 vs always-d | plan-003-eval-implicit, plan-004-ablation-b |
67	| D034 | 2026-05-14 | D027 更正: ablation-b 使用 gradient_accumulation_steps | plan-004-ablation-b |
68	| D033 | 2026-05-14 | Framing 定稿 Option B (方法论贡献): Reviewer seed 变体分析确认  | plan-004-ablation-b, plan-004-v5, plan-002-generative-v1, plan-002-formal-v6, plan-012-decomposition |
69	| D032 | 2026-05-14 | 确认 v5 与 ablation-b 代码级差异：loss 计算(WeightedTrainer v | ablation-b, v5 |
70	| D031 | 2026-05-14 | 发现 v5 未真正复现 ablation-b 配置：ga=8→1 (effective batch  | ablation-b, v5 |
71	| D030 | 2026-05-14 | Generative routing negative 结果纳入 C1 叙事：router 训练失败 | plan-004-v5, plan-002-generative-v1, plan-004-ablation-b, plan-002-formal-v6 |
72	| D029 | 2026-05-14 | Router 训练路线全面评估完毕：classification head 全退化(D025)、ge | plan-002-generative-v1, plan-004-v5, plan-004-ablation-b, plan-002-formal-v6, plan-012-decomposition |
73	
74	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3f62a2fc-7800-4948-a4c3-e970d4f420ce",
  "isSidechain": true,
  "promptId": "34ec326b-764d-435d-9ba6-0f4441293077",
  "agentId": "a6463d3ca736dcafb",
  "type": "user",
  "uuid": "27a39f25-572e-462b-ab91-f83713c5da95",
  "sourceToolAssistantUUID": "3f62a2fc-7800-4948-a4c3-e970d4f420ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_da8ac8a0",
  "sessionId": "892078bb-1c00-49df-bb59-5753637855bb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-14T11:19:29.766Z_

<details open><summary>🔧 Tool call — Read · `toolu_016Vz8v3oSGzsEHtSmFA48E8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/memory.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "27a39f25-572e-462b-ab91-f83713c5da95",
  "isSidechain": true,
  "agentId": "a6463d3ca736dcafb",
  "requestId": "req_011Cb2NT65m3N1PZSpXAAqcS",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f0efc939-4fac-407f-a5a1-85e29ee2e6b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_da8ac8a0",
  "sessionId": "892078bb-1c00-49df-bb59-5753637855bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011vaRmHEsXYdCmApbr62d3t",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1430,
      "cache_read_input_tokens": 30820,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1430,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-14T11:19:29.774Z_

<details><summary>↩ Tool result · `toolu_016Vz8v3oSGzsEHtSmFA48E8`</summary>

```text
1	# Memory — simgate-modular-routing
2	
3	## 决策记录
4	
5	### C1 claim 最终措辞 (2026-05-14, D018)
6	Director 决策：C1 改为 "death avoidance accounts for ~90% of routing signal"（从 ~99% 下调）。
7	- find-non-living-thing 是**正面案例**（不是异常）：零死亡 task 上 Δ_nd=9.58 → routing 价值超越单纯 death avoidance
8	- 与 plan-011 keyword heuristic 失效互相呼应：关键词无法捕获的 signal，router 可以
9	- 论文分两层展示：overall ~90% death-dominated + per-task breakdown（展示非死亡信号存在）
10	- 数据基础：11 tasks, 245 eps, Δ_full=29.60, Δ_nd=2.84, death_fraction=90.41%, r=0.9698
11	
12	### D025: Classification head 路线宣告失败 (2026-05-14)
13	plan-002-formal v3-v6 全部退化为 all-deterministic 预测。根因组合：
14	- class_weights + max_grad_norm 交互（D023）使 internal 有效学习率≈0
15	- 去掉 class_weights（v6）后，89.7/10.3 极端不平衡仍导致退化
16	- **结论：2-class classification head 在此 imbalance 下不可用，pivot 到 generative SFT**
17	
18	### D026: 训练数据损坏确认 (2026-05-14)
19	`results/plan_c_test_labels/implicit_sft.jsonl` 标签损坏：no-preference 被映射为 internal，导致标签比例反转（internal 67% vs 正确的 10.3%）。
20	- plan-004 v2/v3/v4 用此文件训练，初始 loss=48（正常应 0.5-0.7）
21	- **唯一可用数据文件：`data/plan-004-implicit/implicit_sft.jsonl`**（MD5: c9b59e04de78, 2040 samples, 与 ablation-b 一致）
22	
23	### D029: v5 vs ablation-b 代码重构根因 (2026-05-14)
24	ablation-b 到 v5 之间 `implicit_router_sft.py` 重构：
25	- ga 默认值从 `max(1, 32//batch_size)=8` 变为 `1` → effective batch 32→4 → 严重过拟合（train_loss=0.09）
26	- **logit-generation gap 确认是 ga=1 过拟合导致**，非 generative routing 系统性限制
27	- **D034 更正**：ablation-b ga=8（步数反推 165=ceil(434/8)×3 确认），D027 原文 ga=1 错误
28	- **Reviewer D032 待核实**：v5 是否也用了 WeightedTrainer（Worker 调查中）
29	
30	### D033: Framing 定稿 Option B（方法论贡献）(2026-05-14)
31	Director 确认 Option B。论文贡献 = counterfactual 分析方法论 + death avoidance empirical finding。
32	- Router near-random (balanced_acc=58.1±0.8%, 仅比随机高 8pp) IS the finding → 强化 C1
33	- 删除 "首个非退化 router" 或 "成功训练" 表述
34	- 训练实验 conclusion 保持 success（routing 非退化），e2e 部署 conclusion 为 negative（不同实验）
35	- Seed 方差数据（4 seeds）必须纳入论文 "Router Training as Diagnostic" 小节
36	
37	### D037: Table 1 权威数字来源 (2026-05-14)
38	论文 Table 1 所有数字必须来自 `eval_end_to_end.py`（baseline 和 trained-router 用同一脚本）。
39	- trained-router (ablation-b): **-10.70** [-15.25, -6.38], death_rate=17.6%, sim_ratio=97.0%
40	- always-det: -9.47, oracle: -6.58
41	- delta vs always-det: -1.23（negative）
42	- eval_implicit_router.py 产出的 -12.84 不用于 Table 1（脚本不同导致数字差异）
43	
44	### plan-003 baseline oracle 发现 (2026-05-14)
45	Oracle routing 仅比 always-deterministic 好 2.89 分（245-ep: -6.58 vs -9.47），且 96.2% episode 也选 deterministic。
46	- 说明 internal 仅在极少数 episode（~3.8%）上更优
47	- **直接支撑 C1：即使完美知道 ground truth label，optimal strategy 几乎等同于 always-deterministic**
48	
49	### plan-011 已关闭 (2026-05-13)
50	Director 决策：keyword baseline 结构性失效。v1 (always-det) + v2 (always-internal)。
51	展示用 match rate + precision + recall，v1 标注 "functionally equivalent to always-deterministic"。
52	
53	### D013 framing pivot (2026-05-13)
54	核心方向：death avoidance dominates routing signal。
55	论文贡献 = empirical finding + counterfactual methodology，非 router 架构。
56	
57	### 预筛最终结果 (2026-05-13, 25/25 tasks)
58	death-dom 25 / genuine-det 3 / internal-preferred 1 / no-signal 1
59	
60	### 文献扫描结果 (2026-05-14)
61	12 篇新论文扫描，**无 direct competitor，novelty confirmed**。
62	
63	## 经验教训
64	
65	### 🔴 Logit-generation gap 根因确认 (2026-05-14)
66	ga=1 → effective batch=4 → train_loss=0.09 严重过拟合 → generation 能力丧失。
67	ga=8 → effective batch=32 → train_loss=0.35 → gap=0（ablation-b, 复现 3/3 seeds）。
68	**教训：任何 router 训练实验必须跑 generation-level eval 才能定论**
69	
70	### 🔴 Checkpoint 路径混淆 (2026-05-14)
71	`checkpoints/plan-002-generative-v1/final_adapter` = gen-v1（失败）。
72	`checkpoints/plan-004-implicit/final_adapter` = ablation-b（成功）。
73	两者 eval_routing_metrics 相似（internal_recall ~51%）导致混淆。plan-003-e2e-ablation-b 因用错 checkpoint 被废弃。
74	
75	### 🔴 Qwen3 thinking mode 干扰推理 (2026-05-14)
76	所有 eval 脚本必须：`enable_thinking=False` + `re.sub` 兜底清理 `&lt;think>` tags。
77	
78	### 🔴 D023: class_weights + max_grad_norm 交互 (2026-05-14)
79	class_weights [4.5, 0.5625] → grad_norm 100-600 → max_grad_norm=1.0 裁剪 → internal 有效学习率≈0。
80	受影响：plan-002 v3-v6 全退化。
81	
82	### 数据量确认 (2026-05-14)
83	2040 samples = plan_c 正确全量（11 tasks）。
84	
85	### AutoDL 网络 (2026-05-14)
86	提交训练必须：(1) 本地模型路径，(2) source /etc/network_turbo，(3) HF_HOME=/root/autodl-tmp/.hf_cache。
87	
88	### Qwen3-1.7B LoRA 显存 (2026-05-14)
89	RTX 5090 32GB：batch_size=32 OOM，batch_size=4 正常。
90	
91	### 进程管理 (2026-05-14)
92	- 僵尸 tmux session：清理 GPU 时同时 `tmux ls`
93	- SIGHUP 误杀：禁止 `pkill -f` 宽泛 pattern
94	- 进程存活：必须 `ps -p PID`
95	- vLLM 孤儿：已有 cleanup_gpu_processes()
96	- Episode 收集速度：~4.7 min/ep
97	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f0efc939-4fac-407f-a5a1-85e29ee2e6b9",
  "isSidechain": true,
  "promptId": "34ec326b-764d-435d-9ba6-0f4441293077",
  "agentId": "a6463d3ca736dcafb",
  "type": "user",
  "uuid": "92d95d3e-3da8-4dcb-8a22-39341da0cd17",
  "sourceToolAssistantUUID": "f0efc939-4fac-407f-a5a1-85e29ee2e6b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_da8ac8a0",
  "sessionId": "892078bb-1c00-49df-bb59-5753637855bb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-14T11:19:30.005Z_

<details open><summary>🔧 Tool call — Read · `toolu_01EotwD7P9wphFnE8vyaNwGe`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/experiment_plan.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "92d95d3e-3da8-4dcb-8a22-39341da0cd17",
  "isSidechain": true,
  "agentId": "a6463d3ca736dcafb",
  "requestId": "req_011Cb2NT65m3N1PZSpXAAqcS",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "e004341a-b3a4-4c98-9456-c6d0ab660c85",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_da8ac8a0",
  "sessionId": "892078bb-1c00-49df-bb59-5753637855bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011vaRmHEsXYdCmApbr62d3t",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1430,
      "cache_read_input_tokens": 30820,
      "output_tokens": 375,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1430
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 375,
          "cache_read_input_tokens": 30820,
          "cache_creation_input_tokens": 1430,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1430,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-14T11:19:30.012Z_

<details><summary>↩ Tool result · `toolu_01EotwD7P9wphFnE8vyaNwGe`</summary>

```text
1	experiments:
2	- id: plan-001a
3	  claim:
4	  - C1
5	  registry_id: research-prescreening-gpu0
6	  description: 'Mini signal detection (pre-screening). Run 5 episodes per candidate
7	    task type (2-way: internal + deterministic only) to identify which tasks show
8	    det > internal signal. Screen ~20 ScienceWorld task types, keep those with positive
9	    effect direction. ~30min per task type, ~10h total for 20 types on dual GPU.
10	
11	    '
12	  priority: P0
13	  gpu_budget_hours: 10
14	  deps: []
15	  notes: 'Reviewer W3: avoid wasting GPU on no-signal tasks like grow-plant. MVP task
16	    types (boil, melt, change-state, mix-paint) auto-pass. grow-plant confirmed no-signal
17	    (control). Target: identify 10-15 task types with signal.
18	
19	    '
20	- id: plan-001b
21	  claim:
22	  - C1
23	  - C2
24	  description: 'Episode-level counterfactual trajectory collection for death decomposition
25	    analysis. 10-15 signal-positive task types from plan-001a, each 20 episodes/modality
26	    (always-internal + always-deterministic). Three-label scheme: det-preferred, internal-preferred,
27	    no-preference (ties RETAINED, not discarded — the ~60% no-preference rate IS the
28	    C1 finding). Save complete step-level data: observations, actions, scores, death
29	    events. Data feeds plan-012 (death decomposition), plan-005 (routing pattern analysis),
30	    plan-002 (router as diagnostic probe). Prescreening + MVP episodes directly reusable
31	    (format compatible).
32	
33	    '
34	  priority: P0
35	  gpu_budget_hours: 20
36	  deps:
37	  - plan-001a
38	  notes: 'D013: Purpose changed from "train balanced router" to "collect comprehensive
39	    data for death decomposition analysis." Key insight: 1.4% internal labels across
40	    175 paired episodes — the imbalance IS the finding (~93% det-preferred = death
41	    avoidance dominance). No class weighting needed. Three labels: det-preferred (~38%),
42	    internal-preferred (~1-2%), no-preference (~60%). Data reuse: prescreening 5 eps/task
43	    + MVP 20 eps/task directly count toward totals. Only collect additional episodes
44	    to reach 20/task/modality. vLLM backend on both GPUs.
45	
46	    '
47	  registry_id: plan-001b-gpu0
48	- id: plan-002
49	  claim: C2
50	  description: 'Router SFT training. Fine-tune Qwen3-1.7B on counterfactual labels
51	    from plan-001b. Cross-entropy loss, (history, observation) → {internal, deterministic}.
52	    Train/val split by task type (leave-one-out or 80/20).
53	
54	    '
55	  priority: P0
56	  gpu_budget_hours: 8
57	  deps:
58	  - plan-001b
59	  notes: 'Follow ARES training pipeline. Single GPU sufficient. Hyperparams: lr=2e-5,
60	    batch=32, epochs=3, max_seq_len=2048. 2-way classification (not 3-way) per W2
61	    decision.
62	
63	    '
64	- id: plan-003
65	  claim: C1
66	  description: 'SimGate end-to-end evaluation on ScienceWorld. Run trained router
67	    + Qwen2.5-7B backbone on held-out episodes. Compare against: always-internal,
68	    always-deterministic, oracle-routing, random-routing, confidence-threshold heuristic.
69	    Report: continuous score (CogRouter protocol), success rate, catastrophic failure
70	    rate, simulator invocation ratio, total LLM tokens. KEY: This confirms/denies
71	    C1''s "selective > unconditional" sub-claim (Reviewer W1).
72	
73	    '
74	  priority: P0
75	  gpu_budget_hours: 15
76	  deps:
77	  - plan-002
78	  notes: 'CogRouter (84.6) and ITP-R (62.58) cited from papers, not reproduced. Bootstrap
79	    90% CI on all comparisons. Per-task-type breakdown. If trained router ≤ always-det,
80	    C1 downgrades per paper_framing.md note.
81	
82	    '
83	- id: plan-004
84	  claim: C2
85	  description: 'Explicit vs implicit routing ablation (parameter-controlled). Three
86	    conditions: (a) 1.7B explicit router (SimGate) — Qwen3-1.7B, separate module (b)
87	    1.7B implicit router — Qwen3-1.7B SFT''d to output [SIMULATE] token inline (c)
88	    7B implicit routing — Qwen2.5-7B backbone decides via tool-use prompt All trained
89	    on same counterfactual data from plan-001b. Condition (b) is the parameter-matched
90	    control (Reviewer W4).
91	
92	    '
93	  priority: P0
94	  gpu_budget_hours: 12
95	  deps:
96	  - plan-001b
97	  notes: 'Reviewer W4: 7B implicit vs 1.7B explicit confounds architecture with capacity.
98	    Adding 1.7B implicit isolates explicit vs implicit architectural effect. Can run
99	    in parallel with plan-002 on second GPU.
100	
101	    '
102	  registry_id: plan-004-v5
103	- id: plan-005
104	  claim:
105	  - C1
106	  - C2
107	  description: 'Per-task routing pattern analysis. From plan-003 outputs, analyze:
108	    (a) which task categories trigger deterministic routing most, (b) at which episode
109	    phases (early/mid/late) routing decisions concentrate, (c) router-as-diagnostic-probe
110	    — cluster deterministic-routing steps to identify systematic LLM failure modes
111	    (e.g., multi-step physical reasoning failures). Output: routing heatmap figure
112	    + failure mode taxonomy.
113	
114	    '
115	  priority: P0
116	  gpu_budget_hours: 2
117	  deps:
118	  - plan-003
119	  notes: Analysis-only, minimal GPU. Main output is Figure 1 for the paper.
120	- id: plan-006
121	  claim: C2
122	  description: '2-way vs 3-way routing ablation. Supplement plan-001b data with deep-internal
123	    modality on subset of tasks. Compare {internal, deterministic} vs {fast-internal,
124	    deep-internal, deterministic}. Tests whether the fast/deep internal distinction
125	    adds value beyond binary routing.
126	
127	    '
128	  priority: P1
129	  gpu_budget_hours: 10
130	  deps:
131	  - plan-002
132	  notes: 'If 3-way > 2-way, retrain router as 3-way and update paper. If 2-way ≈ 3-way,
133	    simplifies the story (binary routing suffices). Requires supplemental trajectory
134	    data for deep-internal (~5h additional collection).
135	
136	    '
137	- id: plan-007
138	  claim: C1
139	  registry_id: research-boil-v3-gpu1
140	  description: 'Boil task rerun with v3 code. MVP boil data used old code (>= tie-break,
141	    death filter on all 3 modes). Rerun with clean v3 code for unified analysis.
142	
143	    '
144	  priority: P1
145	  gpu_budget_hours: 3
146	  deps: []
147	  notes: Can run in parallel with plan-001a as first batch.
148	- id: plan-008
149	  claim: C2
150	  description: 'Router size ablation. Compare Qwen3-1.7B vs Qwen2.5-1.5B vs Qwen2.5-3B
151	    as router. Tests sensitivity to router capacity.
152	
153	    '
154	  priority: P1
155	  gpu_budget_hours: 12
156	  deps:
157	  - plan-001b
158	  notes: 'Important for "lightweight" claim. If 1.5B matches 1.7B, strengthens "small
159	    router suffices". Low priority relative to core experiments.
160	
161	    '
162	- id: plan-011
163	  claim: C1
164	  description: 'Rule-based routing baseline (Dream all tiers). Keyword-matching heuristic:
165	    route actions containing state-change keywords (heat, cool, boil, melt, freeze,
166	    mix, react, pour, activate) to simulator, everything else to internal reasoning.
167	    Compares against learned router to demonstrate non-trivial learned signal.
168	
169	    '
170	  priority: P0
171	  gpu_budget_hours: 2
172	  deps:
173	  - plan-001b
174	  notes: 'Dream median + worst flagged this as missing. Critical for defending "the
175	    router learns beyond action-type keywords." Cheap — just inference, no training.
176	    PRE-REGISTERED keyword list at src/rule_based_keywords.json. Do NOT modify after
177	    experiment starts.
178	
179	    '
180	- id: plan-012
181	  claim: C1
182	  description: 'Death-decomposition analysis (CORE — D013). From plan-001b episode
183	    data: (a) gains on death-risk episodes only (episodes where always-internal scores
184	    -100) (b) gains on non-death episodes only (c) fraction of routing labels: det-preferred
185	    vs internal-preferred vs no-preference (d) correlation between per-task death
186	    rate and Δ(D-I) (r value) (e) scores with -100 penalty replaced by 0 (penalty-removed
187	    variant)
188	
189	    '
190	  priority: P0-CORE
191	  gpu_budget_hours: 0
192	  deps:
193	  - plan-001b
194	  notes: 'D013: This is now the CORE analysis — paper''s primary contribution. Deps
195	    changed from plan-003 to plan-001b (analysis runs on raw episode data, doesn''t
196	    need trained router). Three-label distribution (~38% det / ~1-2% int / ~60% tie)
197	    directly enters paper as Table 1. Death rate vs Δ correlation is the headline
198	    finding. Also report penalty-removed scores per Dream reviewer concern.
199	
200	    '
201	- id: plan-013
202	  claim:
203	  - C1
204	  - C2
205	  description: 'Labeling quality analysis (Dream best + worst). From plan-001b trajectory
206	    data, characterize: (a) fraction of steps where all modalities give identical
207	    score (tie rate) (b) fraction of "deterministic-preferred" labels from genuine
208	    score difference vs tie-break (c) sensitivity: retrain router on strict-only labels
209	    (excluding ties), compare performance
210	
211	    '
212	  priority: P1
213	  gpu_budget_hours: 4
214	  deps:
215	  - plan-001b
216	  notes: 'Addresses oracle circularity concern from worst case Dream. If strict-only
217	    labels produce similar router, tie-break is harmless. If dramatically different,
218	    must discuss.
219	
220	    '
221	- id: plan-009
222	  claim: C1
223	  description: 'MATH track — code interpreter as deterministic oracle. 500 Level 4-5
224	    MATH problems. 2-way routing: internal / code-interpreter. Demonstrates generalization
225	    beyond environment simulators.
226	
227	    '
228	  priority: P2
229	  gpu_budget_hours: 20
230	  deps:
231	  - plan-002
232	  notes: 'Human Review Note suggested MATH as secondary track. Only if ScienceWorld
233	    experiments finish by Day 8.
234	
235	    '
236	- id: plan-010
237	  claim: C2
238	  description: 'Cross-task transfer within ScienceWorld. Train router on chemistry
239	    tasks only, evaluate on physics tasks (and vice versa). Tests whether routing
240	    patterns transfer across task domains.
241	
242	    '
243	  priority: P2
244	  gpu_budget_hours: 5
245	  deps:
246	  - plan-002
247	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e004341a-b3a4-4c98-9456-c6d0ab660c85",
  "isSidechain": true,
  "promptId": "34ec326b-764d-435d-9ba6-0f4441293077",
  "agentId": "a6463d3ca736dcafb",
  "type": "user",
  "uuid": "e33eb7ef-0341-4aff-b539-270c8fcae8ff",
  "sourceToolAssistantUUID": "e004341a-b3a4-4c98-9456-c6d0ab660c85",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_da8ac8a0",
  "sessionId": "892078bb-1c00-49df-bb59-5753637855bb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-14T11:20:58.295Z_

Here are the file contents:

---

## 1. registry.yaml
**File does not exist** at `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/registry.yaml`

---

## 2. report.md
**File does not exist** at `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/report.md`

---

## 3. ROADMAP.md

```markdown
# simgate-modular-routing — Research Dashboard

> 最后更新: 2026-05-14 09:19 UTC | 更新原因: D035/D036: trained-router e2e negative + seed 方差确认，Reviewer 行动项派发

## 核心方向
Episode-level counterfactual analysis 揭示 LLM agent routing 的本质：death avoidance 占 ~90% routing signal（Δ_full=+29.60, Δ_nd=+2.84, DAF=90.41%, r=0.9698 p=8.12e-07），non-death 场景两种 modality 近似等效（例外：find-non-living-thing 零死亡仍有 Δ=+9.58）。论文贡献 = empirical finding + diagnostic methodology，非 router 架构。详见 paper_framing.md。

## 投稿目标
EMNLP 2026 ARR short paper (4 pages)，DDL: 2026-05-25（剩余 11 天）

## 当前阶段
**Paper Writing Sprint** — 核心实验全部完成。Paper Agent 写作中。Agent 处理 Reviewer 行动项（D032 核实 + seed 补注册）。

## Router 训练总结 (D029 + D035 + D036)
- Classification head (v3-v6): 全退化为 always-det (D025)
- Generative SFT (v1): ga=8/ga=1 双对照均 NEGATIVE
- Ablation-b: 唯一非退化 (internal_recall=51.5%, seed 42)
  - **e2e eval NEGATIVE (D035)**: trained-router=-12.84 vs always-det=-9.47，16个 internal 决策增加 deaths (19.2% vs 16.3%)
  - **跨 seed 不稳定 (D036)**: balanced_acc 稳定 57-59%（学到信号），但 internal_recall 30pp+ 方差（决策边界 seed-dependent）
  - ga=8 确认为非退化必要条件 (vs v5 ga=1 → 26.7%)
- ⚠️ D032 准确性待查：v5 可能也用了 WeightedTrainer，真差异仅 ga

## Death Decomposition 定稿结果（plan-012, 11 tasks / 245 episodes）
- Δ_full = **+29.60**, Δ_nd = **+2.84**, DAF = **90.41%**
- r = **0.9698**, p = 8.12e-07
- Label: det-preferred 86 / internal-preferred 9 / no-preference 150
- 例外: find-non-living-thing (n=40, 零死亡, Δ=+9.58)

## Keywords v2
v1 ≈ always-det (85.8%), v2 ≈ always-internal (4.9%). Keyword heuristic 结构性失效。

## 近期任务
- [x] plan-012 全量 death decomposition ✅
- [x] plan-011 rule-based keyword baseline ✅
- [x] Router 训练路线全面评估 (D029) ✅
- [x] plan-003-baseline-245eps baselines ✅
- [x] ablation-b generation-level eval ✅
- [x] ablation-b e2e eval (D035: negative, -12.84 vs -9.47) ✅
- [x] ablation-b 3-seed 复制 (D036: 非退化可复现，方差大) ✅
- [ ] **D032 核实**（Agent: git history 查 v5 WeightedTrainer）
- [ ] **3 seed 实验补注册 registry**
- [ ] Paper Agent Patch: Table 1 trained-router + Section 3.3 seed 稳定性
- [ ] Paper Agent Full Draft → 目标 5/17 初稿
- [ ] Review + 迭代 (5/17-24)

## Critical Path
| 时间 | 任务 |
|------|------|
| 5/14 | D032 核实 + seed 补注册 + Paper Agent Experiments patch |
| 5/15-16 | Paper Agent 写作 (Method/Intro/RW/Conclusion/Abstract) |
| 5/17 | Paper Agent 交初稿 |
| 5/17-22 | Review 对抗迭代 |
| 5/23-24 | 终稿 + 提交 |

## GPU 预算
- 服务器: westb-13313, 2× RTX 5090 32GB (cuda:0, cuda:1)
- 写作期间 GPU 空闲，可用于补充实验（logit-level seed eval 等）

## 关键决策日志

| ID | 日期 | 摘要 | 关联实验 |
|----|------|------|----------|
| D038 | 2026-05-14 | Table 1 统一用 eval_end_to_end.py: trained-router = - | plan-003-eval-implicit, plan-003-e2e-ablation-b-correct |
| D037 | 2026-05-14 | Table 1 统一使用 eval_end_to_end.py，trained-router = - | plan-003-eval-implicit, plan-003-e2e-ablation-b-correct |
| D036 | 2026-05-14 | Ablation-b 跨 seed 复制确认非退化可复现，但 internal_recall 方差  | plan-004-ablation-b, ablation-b-seed123, ablation-b-seed456, ablation-b-seed789 |
| D035 | 2026-05-14 | Trained router e2e 确认 negative (-12.84 vs always-d | plan-003-eval-implicit, plan-004-ablation-b |
| D034 | 2026-05-14 | D027 更正: ablation-b 使用 gradient_accumulation_steps | plan-004-ablation-b |
| D033 | 2026-05-14 | Framing 定稿 Option B (方法论贡献): Reviewer seed 变体分析确认  | plan-004-ablation-b, plan-004-v5, plan-002-generative-v1, plan-002-formal-v6, plan-012-decomposition |
| D032 | 2026-05-14 | 确认 v5 与 ablation-b 代码级差异：loss 计算(WeightedTrainer v | ablation-b, v5 |
| D031 | 2026-05-14 | 发现 v5 未真正复现 ablation-b 配置：ga=8→1 (effective batch  | ablation-b, v5 |
| D030 | 2026-05-14 | Generative routing negative 结果纳入 C1 叙事：router 训练失败 | plan-004-v5, plan-002-generative-v1, plan-004-ablation-b, plan-002-formal-v6 |
| D029 | 2026-05-14 | Router 训练路线全面评估完毕：classification head 全退化(D025)、ge | plan-002-generative-v1, plan-004-v5, plan-004-ablation-b, plan-002-formal-v6, plan-012-decomposition |
```

---

## 4. memory.md

```markdown
# Memory — simgate-modular-routing

## 决策记录

### C1 claim 最终措辞 (2026-05-14, D018)
Director 决策：C1 改为 "death avoidance accounts for ~90% of routing signal"（从 ~99% 下调）。
- find-non-living-thing 是**正面案例**（不是异常）：零死亡 task 上 Δ_nd=9.58 → routing 价值超越单纯 death avoidance
- 与 plan-011 keyword heuristic 失效互相呼应：关键词无法捕获的 signal，router 可以
- 论文分两层展示：overall ~90% death-dominated + per-task breakdown（展示非死亡信号存在）
- 数据基础：11 tasks, 245 eps, Δ_full=29.60, Δ_nd=2.84, death_fraction=90.41%, r=0.9698

### D025: Classification head 路线宣告失败 (2026-05-14)
plan-002-formal v3-v6 全部退化为 all-deterministic 预测。根因组合：
- class_weights + max_grad_norm 交互（D023）使 internal 有效学习率≈0
- 去掉 class_weights（v6）后，89.7/10.3 极端不平衡仍导致退化
- **结论：2-class classification head 在此 imbalance 下不可用，pivot 到 generative SFT**

### D026: 训练数据损坏确认 (2026-05-14)
`results/plan_c_test_labels/implicit_sft.jsonl` 标签损坏：no-preference 被映射为 internal，导致标签比例反转（internal 67% vs 正确的 10.3%）。
- plan-004 v2/v3/v4 用此文件训练，初始 loss=48（正常应 0.5-0.7）
- **唯一可用数据文件：`data/plan-004-implicit/implicit_sft.jsonl`**（MD5: c9b59e04de78, 2040 samples, 与 ablation-b 一致）

### D029: v5 vs ablation-b 代码重构根因 (2026-05-14)
ablation-b 到 v5 之间 `implicit_router_sft.py` 重构：
- ga 默认值从 `max(1, 32//batch_size)=8` 变为 `1` → effective batch 32→4 → 严重过拟合（train_loss=0.09）
- **logit-generation gap 确认是 ga=1 过拟合导致**，非 generative routing 系统性限制
- **D034 更正**：ablation-b ga=8（步数反推 165=ceil(434/8)×3 确认），D027 原文 ga=1 错误
- **Reviewer D032 待核实**：v5 是否也用了 WeightedTrainer（Worker 调查中）

### D033: Framing 定稿 Option B（方法论贡献）(2026-05-14)
Director 确认 Option B。论文贡献 = counterfactual 分析方法论 + death avoidance empirical finding。
- Router near-random (balanced_acc=58.1±0.8%, 仅比随机高 8pp) IS the finding → 强化 C1
- 删除 "首个非退化 router" 或 "成功训练" 表述
- 训练实验 conclusion 保持 success（routing 非退化），e2e 部署 conclusion 为 negative（不同实验）
- Seed 方差数据（4 seeds）必须纳入论文 "Router Training as Diagnostic" 小节

### D037: Table 1 权威数字来源 (2026-05-14)
论文 Table 1 所有数字必须来自 `eval_end_to_end.py`（baseline 和 trained-router 用同一脚本）。
- trained-router (ablation-b): **-10.70** [-15.25, -6.38], death_rate=17.6%, sim_ratio=97.0%
- always-det: -9.47, oracle: -6.58
- delta vs always-det: -1.23（negative）
- eval_implicit_router.py 产出的 -12.84 不用于 Table 1（脚本不同导致数字差异）

### plan-003 baseline oracle 发现 (2026-05-14)
Oracle routing 仅比 always-deterministic 好 2.89 分（245-ep: -6.58 vs -9.47），且 96.2% episode 也选 deterministic。
- 说明 internal 仅在极少数 episode（~3.8%）上更优
- **直接支撑 C1：即使完美知道 ground truth label，optimal strategy 几乎等同于 always-deterministic**

### plan-011 已关闭 (2026-05-13)
Director 决策：keyword baseline 结构性失效。v1 (always-det) + v2 (always-internal)。
展示用 match rate + precision + recall，v1 标注 "functionally equivalent to always-deterministic"。

### D013 framing pivot (2026-05-13)
核心方向：death avoidance dominates routing signal。
论文贡献 = empirical finding + counterfactual methodology，非 router 架构。

### 预筛最终结果 (2026-05-13, 25/25 tasks)
death-dom 25 / genuine-det 3 / internal-preferred 1 / no-signal 1

### 文献扫描结果 (2026-05-14)
12 篇新论文扫描，**无 direct competitor，novelty confirmed**。

## 经验教训

### 🔴 Logit-generation gap 根因确认 (2026-05-14)
ga=1 → effective batch=4 → train_loss=0.09 严重过拟合 → generation 能力丧失。
ga=8 → effective batch=32 → train_loss=0.35 → gap=0（ablation-b, 复现 3/3 seeds）。
**教训：任何 router 训练实验必须跑 generation-level eval 才能定论**

### 🔴 Checkpoint 路径混淆 (2026-05-14)
`checkpoints/plan-002-generative-v1/final_adapter` = gen-v1（失败）。
`checkpoints/plan-004-implicit/final_adapter` = ablation-b（成功）。
两者 eval_routing_metrics 相似（internal_recall ~51%）导致混淆。plan-003-e2e-ablation-b 因用错 checkpoint 被废弃。

### 🔴 Qwen3 thinking mode 干扰推理 (2026-05-14)
所有 eval 脚本必须：`enable_thinking=False` + `re.sub` 兜底清理 `&lt;think>` tags。

### 🔴 D023: class_weights + max_grad_norm 交互 (2026-05-14)
class_weights [4.5, 0.5625] → grad_norm 100-600 → max_grad_norm=1.0 裁剪 → internal 有效学习率≈0。
受影响：plan-002 v3-v6 全退化。

### 数据量确认 (2026-05-14)
2040 samples = plan_c 正确全量（11 tasks）。

### AutoDL 网络 (2026-05-14)
提交训练必须：(1) 本地模型路径，(2) source /etc/network_turbo，(3) HF_HOME=/root/autodl-tmp/.hf_cache。

### Qwen3-1.7B LoRA 显存 (2026-05-14)
RTX 5090 32GB：batch_size=32 OOM，batch_size=4 正常。

### 进程管理 (2026-05-14)
- 僵尸 tmux session：清理 GPU 时同时 `tmux ls`
- SIGHUP 误杀：禁止 `pkill -f` 宽泛 pattern
- 进程存活：必须 `ps -p PID`
- vLLM 孤儿：已有 cleanup_gpu_processes()
- Episode 收集速度：~4.7 min/ep
```

---

## 5. experiment_plan.yaml

```yaml
experiments:
- id: plan-001a
  claim:
  - C1
  registry_id: research-prescreening-gpu0
  description: 'Mini signal detection (pre-screening). Run 5 episodes per candidate
    task type (2-way: internal + deterministic only) to identify which tasks show
    det > internal signal. Screen ~20 ScienceWorld task types, keep those with positive
    effect direction. ~30min per task type, ~10h total for 20 types on dual GPU.

    '
  priority: P0
  gpu_budget_hours: 10
  deps: []
  notes: 'Reviewer W3: avoid wasting GPU on no-signal tasks like grow-plant. MVP task
    types (boil, melt, change-state, mix-paint) auto-pass. grow-plant confirmed no-signal
    (control). Target: identify 10-15 task types with signal.

    '
- id: plan-001b
  claim:
  - C1
  - C2
  description: 'Episode-level counterfactual trajectory collection for death decomposition
    analysis. 10-15 signal-positive task types from plan-001a, each 20 episodes/modality
    (always-internal + always-deterministic). Three-label scheme: det-preferred, internal-preferred,
    no-preference (ties RETAINED, not discarded — the ~60% no-preference rate IS the
    C1 finding). Save complete step-level data: observations, actions, scores, death
    events. Data feeds plan-012 (death decomposition), plan-005 (routing pattern analysis),
    plan-002 (router as diagnostic probe). Prescreening + MVP episodes directly reusable
    (format compatible).

    '
  priority: P0
  gpu_budget_hours: 20
  deps:
  - plan-001a
  notes: 'D013: Purpose changed from "train balanced router" to "collect comprehensive
    data for death decomposition analysis." Key insight: 1.4% internal labels across
    175 paired episodes — the imbalance IS the finding (~93% det-preferred = death
    avoidance dominance). No class weighting needed. Three labels: det-preferred (~38%),
    internal-preferred (~1-2%), no-preference (~60%). Data reuse: prescreening 5 eps/task
    + MVP 20 eps/task directly count toward totals. Only collect additional episodes
    to reach 20/task/modality. vLLM backend on both GPUs.

    '
  registry_id: plan-001b-gpu0
- id: plan-002
  claim: C2
  description: 'Router SFT training. Fine-tune Qwen3-1.7B on counterfactual labels
    from plan-001b. Cross-entropy loss, (history, observation) → {internal, deterministic}.
    Train/val split by task type (leave-one-out or 80/20).

    '
  priority: P0
  gpu_budget_hours: 8
  deps:
  - plan-001b
  notes: 'Follow ARES training pipeline. Single GPU sufficient. Hyperparams: lr=2e-5,
    batch=32, epochs=3, max_seq_len=2048. 2-way classification (not 3-way) per W2
    decision.

    '
- id: plan-003
  claim: C1
  description: 'SimGate end-to-end evaluation on ScienceWorld. Run trained router
    + Qwen2.5-7B backbone on held-out episodes. Compare against: always-internal,
    always-deterministic, oracle-routing, random-routing, confidence-threshold heuristic.
    Report: continuous score (CogRouter protocol), success rate, catastrophic failure
    rate, simulator invocation ratio, total LLM tokens. KEY: This confirms/denies
    C1''s "selective > unconditional" sub-claim (Reviewer W1).

    '
  priority: P0
  gpu_budget_hours: 15
  deps:
  - plan-002
  notes: 'CogRouter (84.6) and ITP-R (62.58) cited from papers, not reproduced. Bootstrap
    90% CI on all comparisons. Per-task-type breakdown. If trained router ≤ always-det,
    C1 downgrades per paper_framing.md note.

    '
- id: plan-004
  claim: C2
  description: 'Explicit vs implicit routing ablation (parameter-controlled). Three
    conditions: (a) 1.7B explicit router (SimGate) — Qwen3-1.7B, separate module (b)
    1.7B implicit router — Qwen3-1.7B SFT''d to output [SIMULATE] token inline (c)
    7B implicit routing — Qwen2.5-7B backbone decides via tool-use prompt All trained
    on same counterfactual data from plan-001b. Condition (b) is the parameter-matched
    control (Reviewer W4).

    '
  priority: P0
  gpu_budget_hours: 12
  deps:
  - plan-001b
  notes: 'Reviewer W4: 7B implicit vs 1.7B explicit confounds architecture with capacity.
    Adding 1.7B implicit isolates explicit vs implicit architectural effect. Can run
    in parallel with plan-002 on second GPU.

    '
  registry_id: plan-004-v5
- id: plan-005
  claim:
  - C1
  - C2
  description: 'Per-task routing pattern analysis. From plan-003 outputs, analyze:
    (a) which task categories trigger deterministic routing most, (b) at which episode
    phases (early/mid/late) routing decisions concentrate, (c) router-as-diagnostic-probe
    — cluster deterministic-routing steps to identify systematic LLM failure modes
    (e.g., multi-step physical reasoning failures). Output: routing heatmap figure
    + failure mode taxonomy.

    '
  priority: P0
  gpu_budget_hours: 2
  deps:
  - plan-003
  notes: Analysis-only, minimal GPU. Main output is Figure 1 for the paper.
- id: plan-006
  claim: C2
  description: '2-way vs 3-way routing ablation. Supplement plan-001b data with deep-internal
    modality on subset of tasks. Compare {internal, deterministic} vs {fast-internal,
    deep-internal, deterministic}. Tests whether the fast/deep internal distinction
    adds value beyond binary routing.

    '
  priority: P1
  gpu_budget_hours: 10
  deps:
  - plan-002
  notes: 'If 3-way > 2-way, retrain router as 3-way and update paper. If 2-way ≈ 3-way,
    simplifies the story (binary routing suffices). Requires supplemental trajectory
    data for deep-internal (~5h additional collection).

    '
- id: plan-007
  claim: C1
  registry_id: research-boil-v3-gpu1
  description: 'Boil task rerun with v3 code. MVP boil data used old code (>= tie-break,
    death filter on all 3 modes). Rerun with clean v3 code for unified analysis.

    '
  priority: P1
  gpu_budget_hours: 3
  deps: []
  notes: Can run in parallel with plan-001a as first batch.
- id: plan-008
  claim: C2
  description: 'Router size ablation. Compare Qwen3-1.7B vs Qwen2.5-1.5B vs Qwen2.5-3B
    as router. Tests sensitivity to router capacity.

    '
  priority: P1
  gpu_budget_hours: 12
  deps:
  - plan-001b
  notes: 'Important for "lightweight" claim. If 1.5B matches 1.7B, strengthens "small
    router suffices". Low priority relative to core experiments.

    '
- id: plan-011
  claim: C1
  description: 'Rule-based routing baseline (Dream all tiers). Keyword-matching heuristic:
    route actions containing state-change keywords (heat, cool, boil, melt, freeze,
    mix, react, pour, activate) to simulator, everything else to internal reasoning.
    Compares against learned router to demonstrate non-trivial learned signal.

    '
  priority: P0
  gpu_budget_hours: 2
  deps:
  - plan-001b
  notes: 'Dream median + worst flagged this as missing. Critical for defending "the
    router learns beyond action-type keywords." Cheap — just inference, no training.
    PRE-REGISTERED keyword list at src/rule_based_keywords.json. Do NOT modify after
    experiment starts.

    '
- id: plan-012
  claim: C1
  description: 'Death-decomposition analysis (CORE — D013). From plan-001b episode
    data: (a) gains on death-risk episodes only (episodes where always-internal scores
    -100) (b) gains on non-death episodes only (c) fraction of routing labels: det-preferred
    vs internal-preferred vs no-preference (d) correlation between per-task death
    rate and Δ(D-I) (r value) (e) scores with -100 penalty replaced by 0 (penalty-removed
    variant)

    '
  priority: P0-CORE
  gpu_budget_hours: 0
  deps:
  - plan-001b
  notes: 'D013: This is now the CORE analysis — paper''s primary contribution. Deps
    changed from plan-003 to plan-001b (analysis runs on raw episode data, doesn''t
    need trained router). Three-label distribution (~38% det / ~1-2% int / ~60% tie)
    directly enters paper as Table 1. Death rate vs Δ correlation is the headline
    finding. Also report penalty-removed scores per Dream reviewer concern.

    '
- id: plan-013
  claim:
  - C1
  - C2
  description: 'Labeling quality analysis (Dream best + worst). From plan-001b trajectory
    data, characterize: (a) fraction of steps where all modalities give identical
    score (tie rate) (b) fraction of "deterministic-preferred" labels from genuine
    score difference vs tie-break (c) sensitivity: retrain router on strict-only labels
    (excluding ties), compare performance

    '
  priority: P1
  gpu_budget_hours: 4
  deps:
  - plan-001b
  notes: 'Addresses oracle circularity concern from worst case Dream. If strict-only
    labels produce similar router, tie-break is harmless. If dramatically different,
    must discuss.

    '
- id: plan-009
  claim: C1
  description: 'MATH track — code interpreter as deterministic oracle. 500 Level 4-5
    MATH problems. 2-way routing: internal / code-interpreter. Demonstrates generalization
    beyond environment simulators.

    '
  priority: P2
  gpu_budget_hours: 20
  deps:
  - plan-002
  notes: 'Human Review Note suggested MATH as secondary track. Only if ScienceWorld
    experiments finish by Day 8.

    '
- id: plan-010
  claim: C2
  description: 'Cross-task transfer within ScienceWorld. Train router on chemistry
    tasks only, evaluate on physics tasks (and vice versa). Tests whether routing
    patterns transfer across task domains.

    '
  priority: P2
  gpu_budget_hours: 5
  deps:
  - plan-002
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e33eb7ef-0341-4aff-b539-270c8fcae8ff",
  "isSidechain": true,
  "agentId": "a6463d3ca736dcafb",
  "requestId": "req_011Cb2NTGwrrPJxBf3qLWy7g",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "fd1daa4c-0bd4-40ec-8409-c9aedd5db74c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/agent_da8ac8a0",
  "sessionId": "892078bb-1c00-49df-bb59-5753637855bb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014z2caBn3a76Ns8w6RWZFDE",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 9479,
      "cache_read_input_tokens": 32250,
      "output_tokens": 7356,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9479
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 7356,
          "cache_read_input_tokens": 32250,
          "cache_creation_input_tokens": 9479,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9479,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---
