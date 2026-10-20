# knowledge sync experiment plan d112

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 22
- **Recorded user turns:** 0
- **Tool calls:** 6
- **Original source:** `logs/workers/worker_knowledge_sync_experiment_plan_d112_20260518T232310.log`
- **Structured JSON:** [`a3e4f98c966c57ff92da.json`](../../sessions/a3/a3e4f98c966c57ff92da.json)

## Before a recorded user message

22 recorded events

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
  "session_id": "63fd573c-c7f6-4f02-a14f-3fba9cafb494",
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
  "uuid": "bed41794-5d4d-41d8-a79e-e67f4f7079b0",
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
    "resetsAt": 1779162600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "51c0e9db-91c2-4d50-8b10-9d92e6a271ff",
  "session_id": "63fd573c-c7f6-4f02-a14f-3fba9cafb494"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me find the experiment_plan.yaml file first, then read it and make the requested changes.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "63fd573c-c7f6-4f02-a14f-3fba9cafb494",
  "uuid": "43675d62-7754-403f-9058-1f48cc53aed9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019NZ5WYPHBcyyzY156weRRv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13675,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13675
      },
      "output_tokens": 36,
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

<details open><summary>🔧 Tool call — Glob · `toolu_01AWAdsZSTVebiFxEj329sdX`</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/**/experiment_plan.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "63fd573c-c7f6-4f02-a14f-3fba9cafb494",
  "uuid": "d0a98da3-3bf1-4e05-9a60-2f04e09ea04c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019NZ5WYPHBcyyzY156weRRv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13675,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13675
      },
      "output_tokens": 36,
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

_source line 6 · 2026-05-18T23:23:22.979Z_

<details><summary>↩ Tool result · `toolu_01AWAdsZSTVebiFxEj329sdX`</summary>

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
  "session_id": "63fd573c-c7f6-4f02-a14f-3fba9cafb494",
  "uuid": "076f41c2-64ed-4979-bf40-ef99264657ee",
  "tool_use_result": {
    "filenames": [
      "experiment_plan.yaml"
    ],
    "durationMs": 22,
    "numFiles": 1,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — Read · `toolu_01Hn8rzcVoeELSqNaNtj2Wnj`</summary>

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
  "session_id": "63fd573c-c7f6-4f02-a14f-3fba9cafb494",
  "uuid": "5c5d6ef9-03c3-4e2e-a6e6-b8583617c789",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RyWtuXaScpvZUvFvHZQyhg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 140,
      "cache_read_input_tokens": 25516,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 140
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

_source line 8 · 2026-05-18T23:23:27.158Z_

<details><summary>↩ Tool result · `toolu_01Hn8rzcVoeELSqNaNtj2Wnj`</summary>

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
71	  registry_id: plan_016_llama_rsft_candidates
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
143	  registry_id: plan_015_grpo_g4_bf16_v3
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
179	  registry_id: mvp2_grpo_ced_lr5e6_r1
180	- id: plan_017
181	  claim: 3
182	  description: 'Qwen3-14B scaling study: SFT(with-evidence) + SFT(no-evidence) + RSFT
183	    + eval。 第 4 尺度档位（1.7B/4B/8B/14B），验证 evidence tax 在更大模型上是否继续趋近零或转正。 需评估 RTX 5090
184	    32GB 显存是否够 bf16 LoRA（14B×2=28GB base），不够则用 QLoRA。 至少 2 seeds。'
185	  priority: P0
186	  gpu_budget_hours: 50
187	  deps: []
188	  registry_id: null
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
202	    s43/s44，8B-Qwen 需补 s44，LLaMA 需补 s43/s44。 4B 已有 4+ seeds 不需补。每个 seed 含 SFT + RSFT
203	    + no-evidence eval ≈ 5 GPU-h。 目标：每个尺度的 evidence tax 有 mean ± std，scaling claim
204	    有统计力。'
205	  priority: P0
206	  gpu_budget_hours: 25
207	  deps: []
208	  registry_id: plan019_1_7b_sft_s43_r2
209	- id: plan_020
210	  claim: 3
211	  description: 'Evidence tax mechanistic analysis: 解释 WHY 1.7B 获益而 4B 受损。 分析维度：(1)
212	    output length distribution with vs without evidence (2) truncation rate 差异（1.7B
213	    fair subset 已有基础） (3) hallucination rate（false positive relations 在 with/without
214	    evidence 中的比例） (4) per-document evidence 生成对 RE 的影响（按 doc length 分层） 主要是 CPU 分析
215	    + 少量补充 eval。'
216	  priority: P1
217	  gpu_budget_hours: 10
218	  deps: []
219	  registry_id: null
220	- id: plan_021
221	  claim: 1
222	  description: 'Deep error analysis: 按 relation type / document length / entity count
223	    / evidence distance 分层分析。扩展 D070 per-relation EDCR 分析到更多维度。 区分 Main 和 Findings
224	    的 insight 层——Main 论文解释 why，Findings 只报 what。'
225	  priority: P1
226	  gpu_budget_hours: 5
227	  deps: []
228	  registry_id: null
229	- id: plan_022
230	  claim: 3
231	  description: 'Third model family validation: Mistral-7B 或 Gemma-2-9B 上复现 SFT + RSFT
232	    + eval。 验证 scaling pattern 跨第三个模型家族成立。如果 14B（plan_017）已做则优先级下降。'
233	  priority: P2
234	  gpu_budget_hours: 30
235	  deps: []
236	  registry_id: null
237	- id: plan_023
238	  claim: 1
239	  description: 'DocKS-RAG / LMRC baseline reproduction: 在相同 eval protocol 下复现 generative
240	    DocRE SOTA（DocKS-RAG, LMRC）作为完整对比表。审稿人期望 same-condition comparison。'
241	  priority: P2
242	  gpu_budget_hours: 10
243	  deps: []
244	  registry_id: null
245	- id: plan_w3_sft_seeds
246	  claim: 1
247	  description: W3 修复：SFT 4B baseline seed43 + seed44 训练 + eval。 与 canonical SFT (seed42)
248	    配对，计算 bootstrap CI + Cohen d， 验证 RSFT +4.92pp 增益的统计显著性。Wave 1 实验。
249	  priority: P0
250	  gpu_budget_hours: 8
251	  deps: []
252	  registry_id: null
253	- id: plan_w18_random
254	  claim: 1
255	  description: W18 修复：Random k=1 RSFT baseline。从 k=1 候选中随机抽取（不用 NLI 分数）， 验证 NLI-based
256	    selection 的价值。如果 random 也提升 → NLI scoring 不关键； 如果 random 不提升 → NLI scoring 是 RSFT
257	    有效的关键。Wave 1 实验。
258	  priority: P0
259	  gpu_budget_hours: 4
260	  deps: []
261	  registry_id: random_rsft_k1_baseline
262	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "63fd573c-c7f6-4f02-a14f-3fba9cafb494",
  "uuid": "5d3a442a-fb3f-437e-9120-1009d9040ef4",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/experiment_plan.yaml",
      "content": "experiments:\n- id: plan_001\n  claim: 2\n  description: 'CED vs flat-NLI RSFT ablation: 用 flat-NLI scoring（非 contrastive）筛选\n    RSFT 训练数据，对比 CED scoring。验证 CED 的对比性 margin 是否优于朴素 NLI。步骤: (1) rsft_score_filter.py\n    用 flat-NLI 模式重新打分已有 candidates, (2) RSFT 训练, (3) 全量 dev eval。'\n  priority: P0\n  gpu_budget_hours: 20\n  deps: []\n  registry_id: eval_flat_nli_seed45\n- id: plan_002\n  claim: 1\n  description: 'Test set evaluation: 用 RSFT best config（r2b 或 s44）在 DocRED test set\n    上评估。提交 CodaLab 获得官方 F1/Ign-F1，同时本地计算 Evi-F1 和 EDCR。'\n  priority: P0\n  gpu_budget_hours: 4\n  deps:\n  - plan_001\n  registry_id: plan_002_test_rsft_s44\n- id: plan_003\n  claim: 4\n  description: 'EDCR pipeline 验证 + cross-method diagnostic table: 在所有 evidence-producing\n    方法（SFT, RSFT-CED, RSFT-flatNLI, CED-reranker）上计算 EDCR，验证 EDCR 作为独立评估指标的诊断能力。'\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - plan_001\n  registry_id: plan_003_edcr_diagnostic\n- id: plan_004\n  claim: 1\n  description: 'DREEAM baseline reproduction: 在 DocRED dev set 上复现 DREEAM (RoBERTa-large)\n    的 Evi-F1，确认 57.34 数字可复现，作为 Claim 1 的直接对比基线。'\n  priority: P0\n  gpu_budget_hours: 8\n  deps: []\n  registry_id: plan_004_dreeam_baseline\n- id: plan_005\n  claim: 1\n  description: 'CED-as-reranker: 推理时用 CED 对 SFT 生成的 N=8 候选重排选最佳，无需额外训练。验证 CED 在推理时的价值。已在运行中。'\n  priority: P1\n  gpu_budget_hours: 6\n  deps: []\n  registry_id: mvp2_ced_reranker_poc\n- id: plan_006\n  claim: 1\n  description: 'Model size ablation (D077 升 P0): Qwen3-1.7B 和 Qwen3-8B 上复现 SFT → RSFT\n    → eval pipeline，验证 evidence tax + RSFT 增益 + decoupling 在不同模型规模下成立。应对 RC4 和 scope\n    不足问题。'\n  priority: P0\n  gpu_budget_hours: 32\n  deps: []\n  registry_id: plan_006_qwen3_1_7b_no_evidence_eval_v3\n- id: plan_007\n  claim: 1\n  description: 'Re-DocRED cross-dataset (D077 升 P0): 在 Re-DocRED 上用当前 best config\n    做 SFT → RSFT → eval。数据已就绪（格式与 DocRED 兼容，96 relation types 一致）。⚠️ Re-DocRED ~55%\n    triples 无 evidence 标注（修正的 false negative），必须报告两种模式：evidence_only（与 DocRED 可比的\n    evi_f1，仅 43% triples）+ full（全部 triples 的 rel_f1，无 evi_f1）。转换脚本已支持 --mode full。'\n  priority: P0\n  gpu_budget_hours: 16\n  deps: []\n  registry_id: plan_007_redocred_rsft_eval_r5\n- id: plan_016\n  claim: 2\n  description: 'LLaMA-3.1-8B cross-family validation (D077 新增): 在非 Qwen 家族模型上复现核心\n    pipeline (SFT → RSFT → GRPO QLoRA)，验证 decoupling spectrum 跨模型家族成立。关键实验：LLaMA GRPO\n    QLoRA 是否也出现 catastrophic forgetting。'\n  priority: P0\n  gpu_budget_hours: 40\n  deps: []\n  registry_id: plan_016_llama_rsft_candidates\n- id: plan_008\n  claim: 2\n  description: 'top_k ablation: CED scoring 筛选 top_k=3（更多训练数据 ~8000 samples）vs top_k=1（更严格\n    ~2718 samples），验证 CED 过滤严格度对 RSFT 质量的影响。'\n  priority: P1\n  gpu_budget_hours: 8\n  deps: []\n  registry_id: reeval_rsft_topk3\n- id: plan_011\n  claim: 3\n  description: 'GRPO G=8 实验: Dream 三档一致指出 G=4 太小，标准 GRPO 用 G=8-16。用 G=8 + CED reward\n    + kl_coef=0.01 重跑 GRPO，验证 failure 是否持续。如仍 fail → 加强 Claim 3；如改善 → 需修改论文结论。可能需要\n    gradient_accumulation 适配显存。'\n  priority: P0\n  gpu_budget_hours: 8\n  deps: []\n  registry_id: plan_011_bf16_g8_step_eval\n- id: plan_012\n  claim: 3\n  description: 'DPO+CED experiment: 用 RSFT 候选数据构造 preference pairs (CED-preferred\n    vs CED-rejected)，DPO 训练。验证 DPO 是否避免 GRPO 的 catastrophic forgetting。Dream v2 三档要求\n    DPO 作为 RL spectrum 关键数据点，必须补全训练超参（β, lr, epochs, pair construction）。D045 升 P0。'\n  priority: P0\n  gpu_budget_hours: 12\n  deps: []\n  registry_id: plan_012_dpo_ced\n- id: plan_013\n  claim: 4\n  description: '[CANCELLED by D104] EDCR 人工标注验证: 用户决定不做。RC6 用 per-relation 分析 + Limitations\n    说明替代。'\n  priority: CANCELLED\n  gpu_budget_hours: 0\n  deps: []\n  registry_id: null\n- id: plan_009\n  claim: 3\n  description: 'GRPO forgetting dynamics figure: 整理全部 GRPO checkpoint（42个）的 rel_f1/evi_f1/EDCR/reward\n    轨迹，绘制 training dynamics 可视化图。包含 G=4 vs G=8 对比、三种 reward 对比。Dream v2 三档一致要求此图作为论文核心\n    figure。数据已有，只需汇总+画图。'\n  priority: P0\n  gpu_budget_hours: 2\n  deps: []\n  registry_id: plan_009_dynamics_figure\n- id: plan_010\n  claim: 1\n  description: 'NLI model ablation: DeBERTa-v3-base vs DeBERTa-v3-large 作为 CED scorer\n    的对比，验证 NLI 模型能力对 CED 打分质量的影响。应对 RC1。D104 升级。'\n  priority: P1\n  gpu_budget_hours: 4\n  deps: []\n  registry_id: null\n- id: plan_014\n  claim: 1\n  description: 'SFT-without-evidence ablation: 训练 Qwen3-4B SFT 只输出 relation triples（不含\n    evidence sentences），对比标准 SFT（含 evidence）的 rel_f1。隔离 evidence generation 对抽取性能的代价。Dream\n    v2 三档一致要求。用于回答\"43.2% vs LMRC 60.7% 的 gap 有多少来自 evidence 生成负担\"。'\n  priority: P0\n  gpu_budget_hours: 8\n  deps: []\n  registry_id: plan_014_sft_no_evidence\n- id: plan_015\n  claim: 2\n  description: 'bf16 LoRA GRPO clean control: 与原始 GRPO (QLoRA 4-bit, G=4, kl=0, CED\n    reward) 只改一个变量——quantization 从 QLoRA 4-bit 改为 bf16 LoRA。G=4, kl_coef=0 不变。目的:\n    隔离 QLoRA confound，判断 decoupling 是 QLoRA artifact 还是 genuine RL-for-IE 现象。Dream\n    v2 三档一致的 critical 要求。如 decoupling 在 bf16 下仍持续 → 可泛化 claim；如消失 → QLoRA 特定，需 re-scope。优先级取决于\n    plan_011 eval 结果。'\n  priority: P0\n  gpu_budget_hours: 8\n  deps:\n  - plan_011\n  registry_id: plan_015_grpo_g4_bf16_v3\n- id: plan_mvp1\n  claim: 1\n  description: 'MVP-1: CED signal verification — DeBERTa NLI 区分 gold evidence vs entity-sharing\n    distractor 的能力验证'\n  priority: P0\n  gpu_budget_hours: 1\n  deps: []\n  registry_id: mvp1_ced_signal\n- id: plan_mvp2_sft\n  claim: 1\n  description: 'SFT baseline: Qwen3-4B + LoRA SFT on DocRED gold, 建立抽取和证据质量基线'\n  priority: P0\n  gpu_budget_hours: 4\n  deps: []\n  registry_id: mvp2_sft_warmup\n- id: plan_mvp2_rsft\n  claim: 1\n  description: 'RSFT+CED 端到端验证: CED-filtered rejection sampling fine-tuning, 4 组配置全部\n    PASS。真实结果(D038修正后): r1 rel_f1=0.4449/evi_f1=0.8187, s44 rel_f1=0.4655/evi_f1=0.8087,\n    r2a rel_f1=0.4494/evi_f1=0.8108, r2b rel_f1=0.4493/evi_f1=0.8128'\n  priority: P0\n  gpu_budget_hours: 20\n  deps:\n  - plan_mvp1\n  - plan_mvp2_sft\n  registry_id: mvp2_rsft_train_r1\n- id: plan_mvp2_grpo\n  claim: 3\n  description: 'GRPO+QLoRA 全线失败（negative result = C3 核心证据）: 3 种 reward × 多 lr, rel_f1\n    max=0.211(lr5e-5)/0.014(lr5e-6), evi_f1 在 GRPO 下反而提升至 0.850 但 rel_f1 catastrophic\n    forgetting。D031/D033 完整轨迹支撑 Claim 3'\n  priority: P0\n  gpu_budget_hours: 60\n  deps:\n  - plan_mvp2_sft\n  registry_id: mvp2_grpo_ced_lr5e6_r1\n- id: plan_017\n  claim: 3\n  description: 'Qwen3-14B scaling study: SFT(with-evidence) + SFT(no-evidence) + RSFT\n    + eval。 第 4 尺度档位（1.7B/4B/8B/14B），验证 evidence tax 在更大模型上是否继续趋近零或转正。 需评估 RTX 5090\n    32GB 显存是否够 bf16 LoRA（14B×2=28GB base），不够则用 QLoRA。 至少 2 seeds。'\n  priority: P0\n  gpu_budget_hours: 50\n  deps: []\n  registry_id: null\n- id: plan_018\n  claim: 1\n  description: 'Cross-domain DocRE validation: 在 CDR (Chemical-Disease Relations)\n    或 GDA (Gene-Disease Associations) 等生物医学 DocRE 数据集上验证 FREIGE pipeline。 需要：数据格式适配、prompt\n    模板调整、relation type 映射。 验证 evidence-grounded DocRE 跨领域泛化能力，回应 \"only Wikipedia domain\"\n    审稿质疑。 ⚠️ CDR/GDA 均无 evidence sentence 标注，无法计算 evi_f1。降级 P2，Limitations 说明。'\n  priority: P2\n  gpu_budget_hours: 60\n  deps: []\n  registry_id: null\n- id: plan_019\n  claim: 3\n  description: 'Scaling seeds supplement: 每个尺度补到 3+ seeds（k=1 RSFT）。 当前缺口：1.7B 需补\n    s43/s44，8B-Qwen 需补 s44，LLaMA 需补 s43/s44。 4B 已有 4+ seeds 不需补。每个 seed 含 SFT + RSFT\n    + no-evidence eval ≈ 5 GPU-h。 目标：每个尺度的 evidence tax 有 mean ± std，scaling claim\n    有统计力。'\n  priority: P0\n  gpu_budget_hours: 25\n  deps: []\n  registry_id: plan019_1_7b_sft_s43_r2\n- id: plan_020\n  claim: 3\n  description: 'Evidence tax mechanistic analysis: 解释 WHY 1.7B 获益而 4B 受损。 分析维度：(1)\n    output length distribution with vs without evidence (2) truncation rate 差异（1.7B\n    fair subset 已有基础） (3) hallucination rate（false positive relations 在 with/without\n    evidence 中的比例） (4) per-document evidence 生成对 RE 的影响（按 doc length 分层） 主要是 CPU 分析\n    + 少量补充 eval。'\n  priority: P1\n  gpu_budget_hours: 10\n  deps: []\n  registry_id: null\n- id: plan_021\n  claim: 1\n  description: 'Deep error analysis: 按 relation type / document length / entity count\n    / evidence distance 分层分析。扩展 D070 per-relation EDCR 分析到更多维度。 区分 Main 和 Findings\n    的 insight 层——Main 论文解释 why，Findings 只报 what。'\n  priority: P1\n  gpu_budget_hours: 5\n  deps: []\n  registry_id: null\n- id: plan_022\n  claim: 3\n  description: 'Third model family validation: Mistral-7B 或 Gemma-2-9B 上复现 SFT + RSFT\n    + eval。 验证 scaling pattern 跨第三个模型家族成立。如果 14B（plan_017）已做则优先级下降。'\n  priority: P2\n  gpu_budget_hours: 30\n  deps: []\n  registry_id: null\n- id: plan_023\n  claim: 1\n  description: 'DocKS-RAG / LMRC baseline reproduction: 在相同 eval protocol 下复现 generative\n    DocRE SOTA（DocKS-RAG, LMRC）作为完整对比表。审稿人期望 same-condition comparison。'\n  priority: P2\n  gpu_budget_hours: 10\n  deps: []\n  registry_id: null\n- id: plan_w3_sft_seeds\n  claim: 1\n  description: W3 修复：SFT 4B baseline seed43 + seed44 训练 + eval。 与 canonical SFT (seed42)\n    配对，计算 bootstrap CI + Cohen d， 验证 RSFT +4.92pp 增益的统计显著性。Wave 1 实验。\n  priority: P0\n  gpu_budget_hours: 8\n  deps: []\n  registry_id: null\n- id: plan_w18_random\n  claim: 1\n  description: W18 修复：Random k=1 RSFT baseline。从 k=1 候选中随机抽取（不用 NLI 分数）， 验证 NLI-based\n    selection 的价值。如果 random 也提升 → NLI scoring 不关键； 如果 random 不提升 → NLI scoring 是 RSFT\n    有效的关键。Wave 1 实验。\n  priority: P0\n  gpu_budget_hours: 4\n  deps: []\n  registry_id: random_rsft_k1_baseline\n",
      "numLines": 262,
      "startLine": 1,
      "totalLines": 262
    }
  }
}
```

</details>

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — Edit · `toolu_012Mr6dHLFVFRbNX9afbhjzL`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/experiment_plan.yaml",
  "old_string": "  registry_id: null\n- id: plan_w18_random",
  "new_string": "  registry_id: wave1_sft_4b_s44_eval_r2\n- id: plan_d112\n  claim: 1\n  description: \"D112: Full RSFT pipeline from SFT s44 base (strongest seed, ign_f1=0.4734).\\\n    \\ 所有现有 4B RSFT 都基于 SFT s42 (最弱\\\n    \\ seed)。验证 RSFT 是否能在强 SFT base 上\\\n    也产生提升。Steps: generate candidates (N=8) → CED\\\n    \\ score → k=1 filter → RSFT train → D076 eval。\"\n  priority: P0\n  gpu_budget_hours: 8\n  deps:\n  - plan_w3_sft_seeds\n  registry_id: d112_rsft_s44_generate\n- id: plan_w18_random"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "63fd573c-c7f6-4f02-a14f-3fba9cafb494",
  "uuid": "0dfb1094-69b7-4065-9f48-93f2f2ca7e89",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HT4pNenweJUbzzo3sy9EW9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5382,
      "cache_read_input_tokens": 25656,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5382
      },
      "output_tokens": 38,
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

_source line 10 · 2026-05-18T23:23:38.779Z_

<details><summary>↩ Tool result · `toolu_012Mr6dHLFVFRbNX9afbhjzL`</summary>

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
  "session_id": "63fd573c-c7f6-4f02-a14f-3fba9cafb494",
  "uuid": "01d47fb3-07e9-40b1-a60f-50b56b7b0b5f",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/experiment_plan.yaml",
    "oldString": "  registry_id: null\n- id: plan_w18_random",
    "newString": "  registry_id: wave1_sft_4b_s44_eval_r2\n- id: plan_d112\n  claim: 1\n  description: \"D112: Full RSFT pipeline from SFT s44 base (strongest seed, ign_f1=0.4734).\\\n    \\ 所有现有 4B RSFT 都基于 SFT s42 (最弱\\\n    \\ seed)。验证 RSFT 是否能在强 SFT base 上\\\n    也产生提升。Steps: generate candidates (N=8) → CED\\\n    \\ score → k=1 filter → RSFT train → D076 eval。\"\n  priority: P0\n  gpu_budget_hours: 8\n  deps:\n  - plan_w3_sft_seeds\n  registry_id: d112_rsft_s44_generate\n- id: plan_w18_random",
    "originalFile": "experiments:\n- id: plan_001\n  claim: 2\n  description: 'CED vs flat-NLI RSFT ablation: 用 flat-NLI scoring（非 contrastive）筛选\n    RSFT 训练数据，对比 CED scoring。验证 CED 的对比性 margin 是否优于朴素 NLI。步骤: (1) rsft_score_filter.py\n    用 flat-NLI 模式重新打分已有 candidates, (2) RSFT 训练, (3) 全量 dev eval。'\n  priority: P0\n  gpu_budget_hours: 20\n  deps: []\n  registry_id: eval_flat_nli_seed45\n- id: plan_002\n  claim: 1\n  description: 'Test set evaluation: 用 RSFT best config（r2b 或 s44）在 DocRED test set\n    上评估。提交 CodaLab 获得官方 F1/Ign-F1，同时本地计算 Evi-F1 和 EDCR。'\n  priority: P0\n  gpu_budget_hours: 4\n  deps:\n  - plan_001\n  registry_id: plan_002_test_rsft_s44\n- id: plan_003\n  claim: 4\n  description: 'EDCR pipeline 验证 + cross-method diagnostic table: 在所有 evidence-producing\n    方法（SFT, RSFT-CED, RSFT-flatNLI, CED-reranker）上计算 EDCR，验证 EDCR 作为独立评估指标的诊断能力。'\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - plan_001\n  registry_id: plan_003_edcr_diagnostic\n- id: plan_004\n  claim: 1\n  description: 'DREEAM baseline reproduction: 在 DocRED dev set 上复现 DREEAM (RoBERTa-large)\n    的 Evi-F1，确认 57.34 数字可复现，作为 Claim 1 的直接对比基线。'\n  priority: P0\n  gpu_budget_hours: 8\n  deps: []\n  registry_id: plan_004_dreeam_baseline\n- id: plan_005\n  claim: 1\n  description: 'CED-as-reranker: 推理时用 CED 对 SFT 生成的 N=8 候选重排选最佳，无需额外训练。验证 CED 在推理时的价值。已在运行中。'\n  priority: P1\n  gpu_budget_hours: 6\n  deps: []\n  registry_id: mvp2_ced_reranker_poc\n- id: plan_006\n  claim: 1\n  description: 'Model size ablation (D077 升 P0): Qwen3-1.7B 和 Qwen3-8B 上复现 SFT → RSFT\n    → eval pipeline，验证 evidence tax + RSFT 增益 + decoupling 在不同模型规模下成立。应对 RC4 和 scope\n    不足问题。'\n  priority: P0\n  gpu_budget_hours: 32\n  deps: []\n  registry_id: plan_006_qwen3_1_7b_no_evidence_eval_v3\n- id: plan_007\n  claim: 1\n  description: 'Re-DocRED cross-dataset (D077 升 P0): 在 Re-DocRED 上用当前 best config\n    做 SFT → RSFT → eval。数据已就绪（格式与 DocRED 兼容，96 relation types 一致）。⚠️ Re-DocRED ~55%\n    triples 无 evidence 标注（修正的 false negative），必须报告两种模式：evidence_only（与 DocRED 可比的\n    evi_f1，仅 43% triples）+ full（全部 triples 的 rel_f1，无 evi_f1）。转换脚本已支持 --mode full。'\n  priority: P0\n  gpu_budget_hours: 16\n  deps: []\n  registry_id: plan_007_redocred_rsft_eval_r5\n- id: plan_016\n  claim: 2\n  description: 'LLaMA-3.1-8B cross-family validation (D077 新增): 在非 Qwen 家族模型上复现核心\n    pipeline (SFT → RSFT → GRPO QLoRA)，验证 decoupling spectrum 跨模型家族成立。关键实验：LLaMA GRPO\n    QLoRA 是否也出现 catastrophic forgetting。'\n  priority: P0\n  gpu_budget_hours: 40\n  deps: []\n  registry_id: plan_016_llama_rsft_candidates\n- id: plan_008\n  claim: 2\n  description: 'top_k ablation: CED scoring 筛选 top_k=3（更多训练数据 ~8000 samples）vs top_k=1（更严格\n    ~2718 samples），验证 CED 过滤严格度对 RSFT 质量的影响。'\n  priority: P1\n  gpu_budget_hours: 8\n  deps: []\n  registry_id: reeval_rsft_topk3\n- id: plan_011\n  claim: 3\n  description: 'GRPO G=8 实验: Dream 三档一致指出 G=4 太小，标准 GRPO 用 G=8-16。用 G=8 + CED reward\n    + kl_coef=0.01 重跑 GRPO，验证 failure 是否持续。如仍 fail → 加强 Claim 3；如改善 → 需修改论文结论。可能需要\n    gradient_accumulation 适配显存。'\n  priority: P0\n  gpu_budget_hours: 8\n  deps: []\n  registry_id: plan_011_bf16_g8_step_eval\n- id: plan_012\n  claim: 3\n  description: 'DPO+CED experiment: 用 RSFT 候选数据构造 preference pairs (CED-preferred\n    vs CED-rejected)，DPO 训练。验证 DPO 是否避免 GRPO 的 catastrophic forgetting。Dream v2 三档要求\n    DPO 作为 RL spectrum 关键数据点，必须补全训练超参（β, lr, epochs, pair construction）。D045 升 P0。'\n  priority: P0\n  gpu_budget_hours: 12\n  deps: []\n  registry_id: plan_012_dpo_ced\n- id: plan_013\n  claim: 4\n  description: '[CANCELLED by D104] EDCR 人工标注验证: 用户决定不做。RC6 用 per-relation 分析 + Limitations\n    说明替代。'\n  priority: CANCELLED\n  gpu_budget_hours: 0\n  deps: []\n  registry_id: null\n- id: plan_009\n  claim: 3\n  description: 'GRPO forgetting dynamics figure: 整理全部 GRPO checkpoint（42个）的 rel_f1/evi_f1/EDCR/reward\n    轨迹，绘制 training dynamics 可视化图。包含 G=4 vs G=8 对比、三种 reward 对比。Dream v2 三档一致要求此图作为论文核心\n    figure。数据已有，只需汇总+画图。'\n  priority: P0\n  gpu_budget_hours: 2\n  deps: []\n  registry_id: plan_009_dynamics_figure\n- id: plan_010\n  claim: 1\n  description: 'NLI model ablation: DeBERTa-v3-base vs DeBERTa-v3-large 作为 CED scorer\n    的对比，验证 NLI 模型能力对 CED 打分质量的影响。应对 RC1。D104 升级。'\n  priority: P1\n  gpu_budget_hours: 4\n  deps: []\n  registry_id: null\n- id: plan_014\n  claim: 1\n  description: 'SFT-without-evidence ablation: 训练 Qwen3-4B SFT 只输出 relation triples（不含\n    evidence sentences），对比标准 SFT（含 evidence）的 rel_f1。隔离 evidence generation 对抽取性能的代价。Dream\n    v2 三档一致要求。用于回答\"43.2% vs LMRC 60.7% 的 gap 有多少来自 evidence 生成负担\"。'\n  priority: P0\n  gpu_budget_hours: 8\n  deps: []\n  registry_id: plan_014_sft_no_evidence\n- id: plan_015\n  claim: 2\n  description: 'bf16 LoRA GRPO clean control: 与原始 GRPO (QLoRA 4-bit, G=4, kl=0, CED\n    reward) 只改一个变量——quantization 从 QLoRA 4-bit 改为 bf16 LoRA。G=4, kl_coef=0 不变。目的:\n    隔离 QLoRA confound，判断 decoupling 是 QLoRA artifact 还是 genuine RL-for-IE 现象。Dream\n    v2 三档一致的 critical 要求。如 decoupling 在 bf16 下仍持续 → 可泛化 claim；如消失 → QLoRA 特定，需 re-scope。优先级取决于\n    plan_011 eval 结果。'\n  priority: P0\n  gpu_budget_hours: 8\n  deps:\n  - plan_011\n  registry_id: plan_015_grpo_g4_bf16_v3\n- id: plan_mvp1\n  claim: 1\n  description: 'MVP-1: CED signal verification — DeBERTa NLI 区分 gold evidence vs entity-sharing\n    distractor 的能力验证'\n  priority: P0\n  gpu_budget_hours: 1\n  deps: []\n  registry_id: mvp1_ced_signal\n- id: plan_mvp2_sft\n  claim: 1\n  description: 'SFT baseline: Qwen3-4B + LoRA SFT on DocRED gold, 建立抽取和证据质量基线'\n  priority: P0\n  gpu_budget_hours: 4\n  deps: []\n  registry_id: mvp2_sft_warmup\n- id: plan_mvp2_rsft\n  claim: 1\n  description: 'RSFT+CED 端到端验证: CED-filtered rejection sampling fine-tuning, 4 组配置全部\n    PASS。真实结果(D038修正后): r1 rel_f1=0.4449/evi_f1=0.8187, s44 rel_f1=0.4655/evi_f1=0.8087,\n    r2a rel_f1=0.4494/evi_f1=0.8108, r2b rel_f1=0.4493/evi_f1=0.8128'\n  priority: P0\n  gpu_budget_hours: 20\n  deps:\n  - plan_mvp1\n  - plan_mvp2_sft\n  registry_id: mvp2_rsft_train_r1\n- id: plan_mvp2_grpo\n  claim: 3\n  description: 'GRPO+QLoRA 全线失败（negative result = C3 核心证据）: 3 种 reward × 多 lr, rel_f1\n    max=0.211(lr5e-5)/0.014(lr5e-6), evi_f1 在 GRPO 下反而提升至 0.850 但 rel_f1 catastrophic\n    forgetting。D031/D033 完整轨迹支撑 Claim 3'\n  priority: P0\n  gpu_budget_hours: 60\n  deps:\n  - plan_mvp2_sft\n  registry_id: mvp2_grpo_ced_lr5e6_r1\n- id: plan_017\n  claim: 3\n  description: 'Qwen3-14B scaling study: SFT(with-evidence) + SFT(no-evidence) + RSFT\n    + eval。 第 4 尺度档位（1.7B/4B/8B/14B），验证 evidence tax 在更大模型上是否继续趋近零或转正。 需评估 RTX 5090\n    32GB 显存是否够 bf16 LoRA（14B×2=28GB base），不够则用 QLoRA。 至少 2 seeds。'\n  priority: P0\n  gpu_budget_hours: 50\n  deps: []\n  registry_id: null\n- id: plan_018\n  claim: 1\n  description: 'Cross-domain DocRE validation: 在 CDR (Chemical-Disease Relations)\n    或 GDA (Gene-Disease Associations) 等生物医学 DocRE 数据集上验证 FREIGE pipeline。 需要：数据格式适配、prompt\n    模板调整、relation type 映射。 验证 evidence-grounded DocRE 跨领域泛化能力，回应 \"only Wikipedia domain\"\n    审稿质疑。 ⚠️ CDR/GDA 均无 evidence sentence 标注，无法计算 evi_f1。降级 P2，Limitations 说明。'\n  priority: P2\n  gpu_budget_hours: 60\n  deps: []\n  registry_id: null\n- id: plan_019\n  claim: 3\n  description: 'Scaling seeds supplement: 每个尺度补到 3+ seeds（k=1 RSFT）。 当前缺口：1.7B 需补\n    s43/s44，8B-Qwen 需补 s44，LLaMA 需补 s43/s44。 4B 已有 4+ seeds 不需补。每个 seed 含 SFT + RSFT\n    + no-evidence eval ≈ 5 GPU-h。 目标：每个尺度的 evidence tax 有 mean ± std，scaling claim\n    有统计力。'\n  priority: P0\n  gpu_budget_hours: 25\n  deps: []\n  registry_id: plan019_1_7b_sft_s43_r2\n- id: plan_020\n  claim: 3\n  description: 'Evidence tax mechanistic analysis: 解释 WHY 1.7B 获益而 4B 受损。 分析维度：(1)\n    output length distribution with vs without evidence (2) truncation rate 差异（1.7B\n    fair subset 已有基础） (3) hallucination rate（false positive relations 在 with/without\n    evidence 中的比例） (4) per-document evidence 生成对 RE 的影响（按 doc length 分层） 主要是 CPU 分析\n    + 少量补充 eval。'\n  priority: P1\n  gpu_budget_hours: 10\n  deps: []\n  registry_id: null\n- id: plan_021\n  claim: 1\n  description: 'Deep error analysis: 按 relation type / document length / entity count\n    / evidence distance 分层分析。扩展 D070 per-relation EDCR 分析到更多维度。 区分 Main 和 Findings\n    的 insight 层——Main 论文解释 why，Findings 只报 what。'\n  priority: P1\n  gpu_budget_hours: 5\n  deps: []\n  registry_id: null\n- id: plan_022\n  claim: 3\n  description: 'Third model family validation: Mistral-7B 或 Gemma-2-9B 上复现 SFT + RSFT\n    + eval。 验证 scaling pattern 跨第三个模型家族成立。如果 14B（plan_017）已做则优先级下降。'\n  priority: P2\n  gpu_budget_hours: 30\n  deps: []\n  registry_id: null\n- id: plan_023\n  claim: 1\n  description: 'DocKS-RAG / LMRC baseline reproduction: 在相同 eval protocol 下复现 generative\n    DocRE SOTA（DocKS-RAG, LMRC）作为完整对比表。审稿人期望 same-condition comparison。'\n  priority: P2\n  gpu_budget_hours: 10\n  deps: []\n  registry_id: null\n- id: plan_w3_sft_seeds\n  claim: 1\n  description: W3 修复：SFT 4B baseline seed43 + seed44 训练 + eval。 与 canonical SFT (seed42)\n    配对，计算 bootstrap CI + Cohen d， 验证 RSFT +4.92pp 增益的统计显著性。Wave 1 实验。\n  priority: P0\n  gpu_budget_hours: 8\n  deps: []\n  registry_id: null\n- id: plan_w18_random\n  claim: 1\n  description: W18 修复：Random k=1 RSFT baseline。从 k=1 候选中随机抽取（不用 NLI 分数）， 验证 NLI-based\n    selection 的价值。如果 random 也提升 → NLI scoring 不关键； 如果 random 不提升 → NLI scoring 是 RSFT\n    有效的关键。Wave 1 实验。\n  priority: P0\n  gpu_budget_hours: 4\n  deps: []\n  registry_id: random_rsft_k1_baseline\n",
    "structuredPatch": [
      {
        "oldStart": 249,
        "oldLines": 7,
        "newStart": 249,
        "newLines": 19,
        "lines": [
          "   priority: P0",
          "   gpu_budget_hours: 8",
          "   deps: []",
          "-  registry_id: null",
          "+  registry_id: wave1_sft_4b_s44_eval_r2",
          "+- id: plan_d112",
          "+  claim: 1",
          "+  description: \"D112: Full RSFT pipeline from SFT s44 base (strongest seed, ign_f1=0.4734).\\",
          "+    \\ 所有现有 4B RSFT 都基于 SFT s42 (最弱\\",
          "+    \\ seed)。验证 RSFT 是否能在强 SFT base 上\\",
          "+    也产生提升。Steps: generate candidates (N=8) → CED\\",
          "+    \\ score → k=1 filter → RSFT train → D076 eval。\"",
          "+  priority: P0",
          "+  gpu_budget_hours: 8",
          "+  deps:",
          "+  - plan_w3_sft_seeds",
          "+  registry_id: d112_rsft_s44_generate",
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

_source line 11_

验证修改结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "63fd573c-c7f6-4f02-a14f-3fba9cafb494",
  "uuid": "7e6493a3-c93a-46a7-9a78-8033435ecb69",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FKhuSr9u13WrvTQP8cnBpy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 436,
      "cache_read_input_tokens": 31038,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 436
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

_source line 12_

<details open><summary>🔧 Tool call — Read · `toolu_01Biwf531t2CguEv4zQHNoCx`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/experiment_plan.yaml",
  "offset": 245
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "63fd573c-c7f6-4f02-a14f-3fba9cafb494",
  "uuid": "50a8dccc-b681-44d3-ba22-caebcbcc52c3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FKhuSr9u13WrvTQP8cnBpy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 436,
      "cache_read_input_tokens": 31038,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 436
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

_source line 13 · 2026-05-18T23:23:41.742Z_

<details><summary>↩ Tool result · `toolu_01Biwf531t2CguEv4zQHNoCx`</summary>

```text
245	- id: plan_w3_sft_seeds
246	  claim: 1
247	  description: W3 修复：SFT 4B baseline seed43 + seed44 训练 + eval。 与 canonical SFT (seed42)
248	    配对，计算 bootstrap CI + Cohen d， 验证 RSFT +4.92pp 增益的统计显著性。Wave 1 实验。
249	  priority: P0
250	  gpu_budget_hours: 8
251	  deps: []
252	  registry_id: wave1_sft_4b_s44_eval_r2
253	- id: plan_d112
254	  claim: 1
255	  description: "D112: Full RSFT pipeline from SFT s44 base (strongest seed, ign_f1=0.4734).\
256	    \ 所有现有 4B RSFT 都基于 SFT s42 (最弱\
257	    \ seed)。验证 RSFT 是否能在强 SFT base 上\
258	    也产生提升。Steps: generate candidates (N=8) → CED\
259	    \ score → k=1 filter → RSFT train → D076 eval。"
260	  priority: P0
261	  gpu_budget_hours: 8
262	  deps:
263	  - plan_w3_sft_seeds
264	  registry_id: d112_rsft_s44_generate
265	- id: plan_w18_random
266	  claim: 1
267	  description: W18 修复：Random k=1 RSFT baseline。从 k=1 候选中随机抽取（不用 NLI 分数）， 验证 NLI-based
268	    selection 的价值。如果 random 也提升 → NLI scoring 不关键； 如果 random 不提升 → NLI scoring 是 RSFT
269	    有效的关键。Wave 1 实验。
270	  priority: P0
271	  gpu_budget_hours: 4
272	  deps: []
273	  registry_id: random_rsft_k1_baseline
274	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "63fd573c-c7f6-4f02-a14f-3fba9cafb494",
  "uuid": "f364e06c-4c9a-40dd-90d4-a787eb31f7d4",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/experiment_plan.yaml",
      "content": "- id: plan_w3_sft_seeds\n  claim: 1\n  description: W3 修复：SFT 4B baseline seed43 + seed44 训练 + eval。 与 canonical SFT (seed42)\n    配对，计算 bootstrap CI + Cohen d， 验证 RSFT +4.92pp 增益的统计显著性。Wave 1 实验。\n  priority: P0\n  gpu_budget_hours: 8\n  deps: []\n  registry_id: wave1_sft_4b_s44_eval_r2\n- id: plan_d112\n  claim: 1\n  description: \"D112: Full RSFT pipeline from SFT s44 base (strongest seed, ign_f1=0.4734).\\\n    \\ 所有现有 4B RSFT 都基于 SFT s42 (最弱\\\n    \\ seed)。验证 RSFT 是否能在强 SFT base 上\\\n    也产生提升。Steps: generate candidates (N=8) → CED\\\n    \\ score → k=1 filter → RSFT train → D076 eval。\"\n  priority: P0\n  gpu_budget_hours: 8\n  deps:\n  - plan_w3_sft_seeds\n  registry_id: d112_rsft_s44_generate\n- id: plan_w18_random\n  claim: 1\n  description: W18 修复：Random k=1 RSFT baseline。从 k=1 候选中随机抽取（不用 NLI 分数）， 验证 NLI-based\n    selection 的价值。如果 random 也提升 → NLI scoring 不关键； 如果 random 不提升 → NLI scoring 是 RSFT\n    有效的关键。Wave 1 实验。\n  priority: P0\n  gpu_budget_hours: 4\n  deps: []\n  registry_id: random_rsft_k1_baseline\n",
      "numLines": 30,
      "startLine": 245,
      "totalLines": 274
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
The YAML description has some awkward line continuations. Let me check if the YAML is valid by looking at the formatting more carefully. The backslash continuations look a bit off - in YAML, the `\` at the end of lines inside double-quoted strings is a line continuation that removes the newline. But the way I wrote it has `\` followed by newline then spaces then `\` which might cause issues.

Let me fix the description to use the same flow style as other multi-line descriptions in the file. Looking at the existing entries, they use single-quoted strings with the content on one line, or the YAML flow scalar style. 

I need to rewrite this to match the existing style better - the backslash line continuation in double-quoted strings is problematic with trailing spaces, so I'll switch to the same single-quoted format the other entries use.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "63fd573c-c7f6-4f02-a14f-3fba9cafb494",
  "uuid": "75a944a2-d4a5-4670-a93a-cd6030f8a176",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VkPGSo6Y3ad1GnKgbGeucB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 696,
      "cache_read_input_tokens": 31474,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 696
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

description 的 YAML 格式不太干净，修正一下。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "63fd573c-c7f6-4f02-a14f-3fba9cafb494",
  "uuid": "3b14a1e4-445e-4dab-8291-22be05b61c62",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VkPGSo6Y3ad1GnKgbGeucB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 696,
      "cache_read_input_tokens": 31474,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 696
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

<details open><summary>🔧 Tool call — Edit · `toolu_017cZZWLWZeKwQZnV8XQkatS`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/experiment_plan.yaml",
  "old_string": "- id: plan_d112\n  claim: 1\n  description: \"D112: Full RSFT pipeline from SFT s44 base (strongest seed, ign_f1=0.4734).\\\n    \\ 所有现有 4B RSFT 都基于 SFT s42 (最弱\\\n    \\ seed)。验证 RSFT 是否能在强 SFT base 上\\\n    也产生提升。Steps: generate candidates (N=8) → CED\\\n    \\ score → k=1 filter → RSFT train → D076 eval。\"\n  priority: P0\n  gpu_budget_hours: 8\n  deps:\n  - plan_w3_sft_seeds\n  registry_id: d112_rsft_s44_generate",
  "new_string": "- id: plan_d112\n  claim: 1\n  description: 'D112: Full RSFT pipeline from SFT s44 base (strongest seed, ign_f1=0.4734).\n    所有现有 4B RSFT 都基于 SFT s42 (最弱 seed)。验证 RSFT 是否能在强 SFT base 上也产生提升。Steps:\n    generate candidates (N=8) → CED score → k=1 filter → RSFT train → D076 eval。'\n  priority: P0\n  gpu_budget_hours: 8\n  deps:\n  - plan_w3_sft_seeds\n  registry_id: d112_rsft_s44_generate"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "63fd573c-c7f6-4f02-a14f-3fba9cafb494",
  "uuid": "dfdcf308-349e-4334-915e-4c6940203d5f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VkPGSo6Y3ad1GnKgbGeucB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 696,
      "cache_read_input_tokens": 31474,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 696
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

_source line 17 · 2026-05-18T23:23:55.422Z_

<details><summary>↩ Tool result · `toolu_017cZZWLWZeKwQZnV8XQkatS`</summary>

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
  "session_id": "63fd573c-c7f6-4f02-a14f-3fba9cafb494",
  "uuid": "e0dc17d5-dcd2-4a53-a313-e5e6cd229108",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/experiment_plan.yaml",
    "oldString": "- id: plan_d112\n  claim: 1\n  description: \"D112: Full RSFT pipeline from SFT s44 base (strongest seed, ign_f1=0.4734).\\\n    \\ 所有现有 4B RSFT 都基于 SFT s42 (最弱\\\n    \\ seed)。验证 RSFT 是否能在强 SFT base 上\\\n    也产生提升。Steps: generate candidates (N=8) → CED\\\n    \\ score → k=1 filter → RSFT train → D076 eval。\"\n  priority: P0\n  gpu_budget_hours: 8\n  deps:\n  - plan_w3_sft_seeds\n  registry_id: d112_rsft_s44_generate",
    "newString": "- id: plan_d112\n  claim: 1\n  description: 'D112: Full RSFT pipeline from SFT s44 base (strongest seed, ign_f1=0.4734).\n    所有现有 4B RSFT 都基于 SFT s42 (最弱 seed)。验证 RSFT 是否能在强 SFT base 上也产生提升。Steps:\n    generate candidates (N=8) → CED score → k=1 filter → RSFT train → D076 eval。'\n  priority: P0\n  gpu_budget_hours: 8\n  deps:\n  - plan_w3_sft_seeds\n  registry_id: d112_rsft_s44_generate",
    "originalFile": "experiments:\n- id: plan_001\n  claim: 2\n  description: 'CED vs flat-NLI RSFT ablation: 用 flat-NLI scoring（非 contrastive）筛选\n    RSFT 训练数据，对比 CED scoring。验证 CED 的对比性 margin 是否优于朴素 NLI。步骤: (1) rsft_score_filter.py\n    用 flat-NLI 模式重新打分已有 candidates, (2) RSFT 训练, (3) 全量 dev eval。'\n  priority: P0\n  gpu_budget_hours: 20\n  deps: []\n  registry_id: eval_flat_nli_seed45\n- id: plan_002\n  claim: 1\n  description: 'Test set evaluation: 用 RSFT best config（r2b 或 s44）在 DocRED test set\n    上评估。提交 CodaLab 获得官方 F1/Ign-F1，同时本地计算 Evi-F1 和 EDCR。'\n  priority: P0\n  gpu_budget_hours: 4\n  deps:\n  - plan_001\n  registry_id: plan_002_test_rsft_s44\n- id: plan_003\n  claim: 4\n  description: 'EDCR pipeline 验证 + cross-method diagnostic table: 在所有 evidence-producing\n    方法（SFT, RSFT-CED, RSFT-flatNLI, CED-reranker）上计算 EDCR，验证 EDCR 作为独立评估指标的诊断能力。'\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - plan_001\n  registry_id: plan_003_edcr_diagnostic\n- id: plan_004\n  claim: 1\n  description: 'DREEAM baseline reproduction: 在 DocRED dev set 上复现 DREEAM (RoBERTa-large)\n    的 Evi-F1，确认 57.34 数字可复现，作为 Claim 1 的直接对比基线。'\n  priority: P0\n  gpu_budget_hours: 8\n  deps: []\n  registry_id: plan_004_dreeam_baseline\n- id: plan_005\n  claim: 1\n  description: 'CED-as-reranker: 推理时用 CED 对 SFT 生成的 N=8 候选重排选最佳，无需额外训练。验证 CED 在推理时的价值。已在运行中。'\n  priority: P1\n  gpu_budget_hours: 6\n  deps: []\n  registry_id: mvp2_ced_reranker_poc\n- id: plan_006\n  claim: 1\n  description: 'Model size ablation (D077 升 P0): Qwen3-1.7B 和 Qwen3-8B 上复现 SFT → RSFT\n    → eval pipeline，验证 evidence tax + RSFT 增益 + decoupling 在不同模型规模下成立。应对 RC4 和 scope\n    不足问题。'\n  priority: P0\n  gpu_budget_hours: 32\n  deps: []\n  registry_id: plan_006_qwen3_1_7b_no_evidence_eval_v3\n- id: plan_007\n  claim: 1\n  description: 'Re-DocRED cross-dataset (D077 升 P0): 在 Re-DocRED 上用当前 best config\n    做 SFT → RSFT → eval。数据已就绪（格式与 DocRED 兼容，96 relation types 一致）。⚠️ Re-DocRED ~55%\n    triples 无 evidence 标注（修正的 false negative），必须报告两种模式：evidence_only（与 DocRED 可比的\n    evi_f1，仅 43% triples）+ full（全部 triples 的 rel_f1，无 evi_f1）。转换脚本已支持 --mode full。'\n  priority: P0\n  gpu_budget_hours: 16\n  deps: []\n  registry_id: plan_007_redocred_rsft_eval_r5\n- id: plan_016\n  claim: 2\n  description: 'LLaMA-3.1-8B cross-family validation (D077 新增): 在非 Qwen 家族模型上复现核心\n    pipeline (SFT → RSFT → GRPO QLoRA)，验证 decoupling spectrum 跨模型家族成立。关键实验：LLaMA GRPO\n    QLoRA 是否也出现 catastrophic forgetting。'\n  priority: P0\n  gpu_budget_hours: 40\n  deps: []\n  registry_id: plan_016_llama_rsft_candidates\n- id: plan_008\n  claim: 2\n  description: 'top_k ablation: CED scoring 筛选 top_k=3（更多训练数据 ~8000 samples）vs top_k=1（更严格\n    ~2718 samples），验证 CED 过滤严格度对 RSFT 质量的影响。'\n  priority: P1\n  gpu_budget_hours: 8\n  deps: []\n  registry_id: reeval_rsft_topk3\n- id: plan_011\n  claim: 3\n  description: 'GRPO G=8 实验: Dream 三档一致指出 G=4 太小，标准 GRPO 用 G=8-16。用 G=8 + CED reward\n    + kl_coef=0.01 重跑 GRPO，验证 failure 是否持续。如仍 fail → 加强 Claim 3；如改善 → 需修改论文结论。可能需要\n    gradient_accumulation 适配显存。'\n  priority: P0\n  gpu_budget_hours: 8\n  deps: []\n  registry_id: plan_011_bf16_g8_step_eval\n- id: plan_012\n  claim: 3\n  description: 'DPO+CED experiment: 用 RSFT 候选数据构造 preference pairs (CED-preferred\n    vs CED-rejected)，DPO 训练。验证 DPO 是否避免 GRPO 的 catastrophic forgetting。Dream v2 三档要求\n    DPO 作为 RL spectrum 关键数据点，必须补全训练超参（β, lr, epochs, pair construction）。D045 升 P0。'\n  priority: P0\n  gpu_budget_hours: 12\n  deps: []\n  registry_id: plan_012_dpo_ced\n- id: plan_013\n  claim: 4\n  description: '[CANCELLED by D104] EDCR 人工标注验证: 用户决定不做。RC6 用 per-relation 分析 + Limitations\n    说明替代。'\n  priority: CANCELLED\n  gpu_budget_hours: 0\n  deps: []\n  registry_id: null\n- id: plan_009\n  claim: 3\n  description: 'GRPO forgetting dynamics figure: 整理全部 GRPO checkpoint（42个）的 rel_f1/evi_f1/EDCR/reward\n    轨迹，绘制 training dynamics 可视化图。包含 G=4 vs G=8 对比、三种 reward 对比。Dream v2 三档一致要求此图作为论文核心\n    figure。数据已有，只需汇总+画图。'\n  priority: P0\n  gpu_budget_hours: 2\n  deps: []\n  registry_id: plan_009_dynamics_figure\n- id: plan_010\n  claim: 1\n  description: 'NLI model ablation: DeBERTa-v3-base vs DeBERTa-v3-large 作为 CED scorer\n    的对比，验证 NLI 模型能力对 CED 打分质量的影响。应对 RC1。D104 升级。'\n  priority: P1\n  gpu_budget_hours: 4\n  deps: []\n  registry_id: null\n- id: plan_014\n  claim: 1\n  description: 'SFT-without-evidence ablation: 训练 Qwen3-4B SFT 只输出 relation triples（不含\n    evidence sentences），对比标准 SFT（含 evidence）的 rel_f1。隔离 evidence generation 对抽取性能的代价。Dream\n    v2 三档一致要求。用于回答\"43.2% vs LMRC 60.7% 的 gap 有多少来自 evidence 生成负担\"。'\n  priority: P0\n  gpu_budget_hours: 8\n  deps: []\n  registry_id: plan_014_sft_no_evidence\n- id: plan_015\n  claim: 2\n  description: 'bf16 LoRA GRPO clean control: 与原始 GRPO (QLoRA 4-bit, G=4, kl=0, CED\n    reward) 只改一个变量——quantization 从 QLoRA 4-bit 改为 bf16 LoRA。G=4, kl_coef=0 不变。目的:\n    隔离 QLoRA confound，判断 decoupling 是 QLoRA artifact 还是 genuine RL-for-IE 现象。Dream\n    v2 三档一致的 critical 要求。如 decoupling 在 bf16 下仍持续 → 可泛化 claim；如消失 → QLoRA 特定，需 re-scope。优先级取决于\n    plan_011 eval 结果。'\n  priority: P0\n  gpu_budget_hours: 8\n  deps:\n  - plan_011\n  registry_id: plan_015_grpo_g4_bf16_v3\n- id: plan_mvp1\n  claim: 1\n  description: 'MVP-1: CED signal verification — DeBERTa NLI 区分 gold evidence vs entity-sharing\n    distractor 的能力验证'\n  priority: P0\n  gpu_budget_hours: 1\n  deps: []\n  registry_id: mvp1_ced_signal\n- id: plan_mvp2_sft\n  claim: 1\n  description: 'SFT baseline: Qwen3-4B + LoRA SFT on DocRED gold, 建立抽取和证据质量基线'\n  priority: P0\n  gpu_budget_hours: 4\n  deps: []\n  registry_id: mvp2_sft_warmup\n- id: plan_mvp2_rsft\n  claim: 1\n  description: 'RSFT+CED 端到端验证: CED-filtered rejection sampling fine-tuning, 4 组配置全部\n    PASS。真实结果(D038修正后): r1 rel_f1=0.4449/evi_f1=0.8187, s44 rel_f1=0.4655/evi_f1=0.8087,\n    r2a rel_f1=0.4494/evi_f1=0.8108, r2b rel_f1=0.4493/evi_f1=0.8128'\n  priority: P0\n  gpu_budget_hours: 20\n  deps:\n  - plan_mvp1\n  - plan_mvp2_sft\n  registry_id: mvp2_rsft_train_r1\n- id: plan_mvp2_grpo\n  claim: 3\n  description: 'GRPO+QLoRA 全线失败（negative result = C3 核心证据）: 3 种 reward × 多 lr, rel_f1\n    max=0.211(lr5e-5)/0.014(lr5e-6), evi_f1 在 GRPO 下反而提升至 0.850 但 rel_f1 catastrophic\n    forgetting。D031/D033 完整轨迹支撑 Claim 3'\n  priority: P0\n  gpu_budget_hours: 60\n  deps:\n  - plan_mvp2_sft\n  registry_id: mvp2_grpo_ced_lr5e6_r1\n- id: plan_017\n  claim: 3\n  description: 'Qwen3-14B scaling study: SFT(with-evidence) + SFT(no-evidence) + RSFT\n    + eval。 第 4 尺度档位（1.7B/4B/8B/14B），验证 evidence tax 在更大模型上是否继续趋近零或转正。 需评估 RTX 5090\n    32GB 显存是否够 bf16 LoRA（14B×2=28GB base），不够则用 QLoRA。 至少 2 seeds。'\n  priority: P0\n  gpu_budget_hours: 50\n  deps: []\n  registry_id: null\n- id: plan_018\n  claim: 1\n  description: 'Cross-domain DocRE validation: 在 CDR (Chemical-Disease Relations)\n    或 GDA (Gene-Disease Associations) 等生物医学 DocRE 数据集上验证 FREIGE pipeline。 需要：数据格式适配、prompt\n    模板调整、relation type 映射。 验证 evidence-grounded DocRE 跨领域泛化能力，回应 \"only Wikipedia domain\"\n    审稿质疑。 ⚠️ CDR/GDA 均无 evidence sentence 标注，无法计算 evi_f1。降级 P2，Limitations 说明。'\n  priority: P2\n  gpu_budget_hours: 60\n  deps: []\n  registry_id: null\n- id: plan_019\n  claim: 3\n  description: 'Scaling seeds supplement: 每个尺度补到 3+ seeds（k=1 RSFT）。 当前缺口：1.7B 需补\n    s43/s44，8B-Qwen 需补 s44，LLaMA 需补 s43/s44。 4B 已有 4+ seeds 不需补。每个 seed 含 SFT + RSFT\n    + no-evidence eval ≈ 5 GPU-h。 目标：每个尺度的 evidence tax 有 mean ± std，scaling claim\n    有统计力。'\n  priority: P0\n  gpu_budget_hours: 25\n  deps: []\n  registry_id: plan019_1_7b_sft_s43_r2\n- id: plan_020\n  claim: 3\n  description: 'Evidence tax mechanistic analysis: 解释 WHY 1.7B 获益而 4B 受损。 分析维度：(1)\n    output length distribution with vs without evidence (2) truncation rate 差异（1.7B\n    fair subset 已有基础） (3) hallucination rate（false positive relations 在 with/without\n    evidence 中的比例） (4) per-document evidence 生成对 RE 的影响（按 doc length 分层） 主要是 CPU 分析\n    + 少量补充 eval。'\n  priority: P1\n  gpu_budget_hours: 10\n  deps: []\n  registry_id: null\n- id: plan_021\n  claim: 1\n  description: 'Deep error analysis: 按 relation type / document length / entity count\n    / evidence distance 分层分析。扩展 D070 per-relation EDCR 分析到更多维度。 区分 Main 和 Findings\n    的 insight 层——Main 论文解释 why，Findings 只报 what。'\n  priority: P1\n  gpu_budget_hours: 5\n  deps: []\n  registry_id: null\n- id: plan_022\n  claim: 3\n  description: 'Third model family validation: Mistral-7B 或 Gemma-2-9B 上复现 SFT + RSFT\n    + eval。 验证 scaling pattern 跨第三个模型家族成立。如果 14B（plan_017）已做则优先级下降。'\n  priority: P2\n  gpu_budget_hours: 30\n  deps: []\n  registry_id: null\n- id: plan_023\n  claim: 1\n  description: 'DocKS-RAG / LMRC baseline reproduction: 在相同 eval protocol 下复现 generative\n    DocRE SOTA（DocKS-RAG, LMRC）作为完整对比表。审稿人期望 same-condition comparison。'\n  priority: P2\n  gpu_budget_hours: 10\n  deps: []\n  registry_id: null\n- id: plan_w3_sft_seeds\n  claim: 1\n  description: W3 修复：SFT 4B baseline seed43 + seed44 训练 + eval。 与 canonical SFT (seed42)\n    配对，计算 bootstrap CI + Cohen d， 验证 RSFT +4.92pp 增益的统计显著性。Wave 1 实验。\n  priority: P0\n  gpu_budget_hours: 8\n  deps: []\n  registry_id: wave1_sft_4b_s44_eval_r2\n- id: plan_d112\n  claim: 1\n  description: \"D112: Full RSFT pipeline from SFT s44 base (strongest seed, ign_f1=0.4734).\\\n    \\ 所有现有 4B RSFT 都基于 SFT s42 (最弱\\\n    \\ seed)。验证 RSFT 是否能在强 SFT base 上\\\n    也产生提升。Steps: generate candidates (N=8) → CED\\\n    \\ score → k=1 filter → RSFT train → D076 eval。\"\n  priority: P0\n  gpu_budget_hours: 8\n  deps:\n  - plan_w3_sft_seeds\n  registry_id: d112_rsft_s44_generate\n- id: plan_w18_random\n  claim: 1\n  description: W18 修复：Random k=1 RSFT baseline。从 k=1 候选中随机抽取（不用 NLI 分数）， 验证 NLI-based\n    selection 的价值。如果 random 也提升 → NLI scoring 不关键； 如果 random 不提升 → NLI scoring 是 RSFT\n    有效的关键。Wave 1 实验。\n  priority: P0\n  gpu_budget_hours: 4\n  deps: []\n  registry_id: random_rsft_k1_baseline\n",
    "structuredPatch": [
      {
        "oldStart": 252,
        "oldLines": 11,
        "newStart": 252,
        "newLines": 9,
        "lines": [
          "   registry_id: wave1_sft_4b_s44_eval_r2",
          " - id: plan_d112",
          "   claim: 1",
          "-  description: \"D112: Full RSFT pipeline from SFT s44 base (strongest seed, ign_f1=0.4734).\\",
          "-    \\ 所有现有 4B RSFT 都基于 SFT s42 (最弱\\",
          "-    \\ seed)。验证 RSFT 是否能在强 SFT base 上\\",
          "-    也产生提升。Steps: generate candidates (N=8) → CED\\",
          "-    \\ score → k=1 filter → RSFT train → D076 eval。\"",
          "+  description: 'D112: Full RSFT pipeline from SFT s44 base (strongest seed, ign_f1=0.4734).",
          "+    所有现有 4B RSFT 都基于 SFT s42 (最弱 seed)。验证 RSFT 是否能在强 SFT base 上也产生提升。Steps:",
          "+    generate candidates (N=8) → CED score → k=1 filter → RSFT train → D076 eval。'",
          "   priority: P0",
          "   gpu_budget_hours: 8",
          "   deps:"
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

_source line 18_

YAML 验证一下。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "63fd573c-c7f6-4f02-a14f-3fba9cafb494",
  "uuid": "67db8c3e-ee45-4be3-8e07-3ade042d8019",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011eRbPoFDo7nXJzvJVFjp4y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 890,
      "cache_read_input_tokens": 32170,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 890
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

_source line 19_

<details open><summary>🔧 Tool call — Bash · `toolu_01WduHoodYJCT1vN4Rhj77UF`</summary>

```json
{
  "command": "python3 -c \"import yaml; yaml.safe_load(open('/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/experiment_plan.yaml')); print('YAML valid')\"",
  "description": "Validate YAML syntax"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "63fd573c-c7f6-4f02-a14f-3fba9cafb494",
  "uuid": "73e2516a-5d47-4c37-8f7e-87f31c077bde",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011eRbPoFDo7nXJzvJVFjp4y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 890,
      "cache_read_input_tokens": 32170,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 890
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

_source line 20 · 2026-05-18T23:23:59.456Z_

<details><summary>↩ Tool result · `toolu_01WduHoodYJCT1vN4Rhj77UF`</summary>

```text
YAML valid
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "63fd573c-c7f6-4f02-a14f-3fba9cafb494",
  "uuid": "c26c327b-b57e-48fe-a43a-4e214144b71c",
  "tool_use_result": {
    "stdout": "YAML valid",
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

_source line 21_

完成。修改了两处：

1. **plan_w3_sft_seeds**: `registry_id: null` → `registry_id: wave1_sft_4b_s44_eval_r2`
2. **plan_d112**: 新增条目，claim=1, P0, deps=[plan_w3_sft_seeds], registry_id=d112_rsft_s44_generate

plan_019 保持不变（registry_id: plan019_1_7b_sft_s43_r2）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "63fd573c-c7f6-4f02-a14f-3fba9cafb494",
  "uuid": "205de2aa-1f08-45ac-b16f-26d07aecc251",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QQRNth2q1jKibufbvj5af6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 154,
      "cache_read_input_tokens": 33060,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 154
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

_source line 22_

完成。修改了两处：

1. **plan_w3_sft_seeds**: `registry_id: null` → `registry_id: wave1_sft_4b_s44_eval_r2`
2. **plan_d112**: 新增条目，claim=1, P0, deps=[plan_w3_sft_seeds], registry_id=d112_rsft_s44_generate

plan_019 保持不变（registry_id: plan019_1_7b_sft_s43_r2）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 44584,
  "duration_api_ms": 45646,
  "num_turns": 7,
  "stop_reason": "end_turn",
  "session_id": "63fd573c-c7f6-4f02-a14f-3fba9cafb494",
  "total_cost_usd": 0.27794375000000004,
  "usage": {
    "input_tokens": 9,
    "cache_creation_input_tokens": 21373,
    "cache_read_input_tokens": 190755,
    "output_tokens": 1878,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 21373,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 136,
        "cache_read_input_tokens": 33060,
        "cache_creation_input_tokens": 154,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 154
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1885,
      "outputTokens": 21,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.00199,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 9,
      "outputTokens": 1878,
      "cacheReadInputTokens": 190755,
      "cacheCreationInputTokens": 21373,
      "webSearchRequests": 0,
      "costUSD": 0.27595375,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "36bb60ad-8c48-4ace-a480-db81cbdaa2dc"
}
```

</details>

---
