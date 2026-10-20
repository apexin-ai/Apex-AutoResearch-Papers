# knowledge update prolog memory

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 0
- **Tool calls:** 2
- **Original source:** `logs/workers/worker_knowledge_update-prolog-memory_20260514T163217.log`
- **Structured JSON:** [`55393e009849a6030784.json`](../../sessions/55/55393e009849a6030784.json)

## Before a recorded user message

11 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation",
  "session_id": "f8a623d4-4736-4f28-98e7-c9460074e673",
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
  "uuid": "04ebe4db-75c7-4606-bcc5-f7aad2e45335",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-3-projects-solver-trace-ablation/memory/"
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
    "resetsAt": 1778782200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "b6bc59b0-d085-49f3-a86d-6da0fd4db86f",
  "session_id": "f8a623d4-4736-4f28-98e7-c9460074e673"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me read the current memory.md file to understand its structure and find the section that needs updating.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f8a623d4-4736-4f28-98e7-c9460074e673",
  "uuid": "bf5bd992-edd3-4777-a71e-f884bc5c5c97",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FTdGcvRBXFyDfWVvQgmmjK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12153,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12153
      },
      "output_tokens": 25,
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

<details open><summary>🔧 Tool call — Read · `toolu_01JViuGNYcGcBwm1Go9wSGJU`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/memory.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f8a623d4-4736-4f28-98e7-c9460074e673",
  "uuid": "911f4c5c-9c7e-48d6-b219-1c350dcd6770",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FTdGcvRBXFyDfWVvQgmmjK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12153,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12153
      },
      "output_tokens": 25,
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

_source line 6 · 2026-05-14T16:32:26.756Z_

<details><summary>↩ Tool result · `toolu_01JViuGNYcGcBwm1Go9wSGJU`</summary>

```text
1	# solver-trace-ablation — Memory
2	
3	## 环境信息 (2026-05-13)
4	
5	### westd-39279 服务器
6	- **GPU**: 2× RTX PRO 6000 Blackwell, 94GB VRAM 每张
7	- **CUDA**: 12.8, PyTorch 2.10.0+cu128
8	- **镜像**: aml-train（conda 环境，`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`）
9	- **ML 栈**: transformers/trl/vllm/accelerate 全部预装
10	- **Solvers**: Prover9 (LADR 2009-11A 源码编译), SWI-Prolog 8.4.2 (`/usr/bin/swipl`), Z3 4.16.0.0
11	- **模型**: Qwen3-4B 已下载（7.6GB，通过 ModelScope）
12	- **代码路径**: `/root/solver-trace-ablation/`
13	- **磁盘**: 系统盘 30GB (22G free)，数据盘 `/root/autodl-tmp/` 250GB (清理后 ~131G free)
14	
15	### 决策记录
16	- Qwen3-4B 用 ModelScope 下载（HuggingFace 直连可能慢）
17	- Prover9 从 LADR 源码编译（apt 无包）
18	- 94GB VRAM 单卡跑 Qwen3-4B 完全无压力
19	
20	## 数据 (2026-05-13)
21	
22	### 数据源变更：ProofWriter → FOLIO
23	- ProofWriter 原始数据无 FOL 列，改用 `tasksource/folio`（1204 条人工标注 FOL）
24	- Phase 0 子集 100 条，训练子集 500 条
25	- 34% 数据含 XOR (⊕) 符号，已在 `_normalize_fol()` 中修复展开
26	
27	### 数据约束 (2026-05-14, D009)
28	- **C001**: 所有 plan001/plan013 实验统一使用 `train_500_seed42.jsonl`，不再用 `proofwriter_fol_500.jsonl`（消除数据差异 confound）
29	
30	## Phase 0 关键发现 (2026-05-13)
31	
32	### Base Model ISR Baseline (sta-phase0-baseline)
33	- **Prove rate**: 12% overall, 18.2% excluding XOR-affected samples
34	- **Mean ISR**: 0.064 (very low — base model formalizations mostly unprovable)
35	- **ISR 区分度**: proved 样本 ISR 0.125–0.889
36	
37	### Ground-Truth ISR Baseline (sta-gt-isr-baseline)
38	- **GT prove rate**: 18% (limited by Prover9 only proving entailment; true=50%, false=4%, unknown=0%)
39	- **GT mean ISR**: 0.5588 (median 0.6125, range 0.14–1.00)
40	- **Model vs GT gap**: ISR 0.064 vs 0.559 = 8.7x 差距，STA 有强区分力
41	
42	### Prover9 局限性
43	- Prover9 只能证明 entailment（conclusion 从 premises 推出）
44	- `false` 和 `unknown` 类问题几乎无法证明（false 4%, unknown 0%）
45	
46	## Phase 1 关键经验 (2026-05-13)
47	
48	### fast_isr_fol 失败教训 (r4)
49	- `fast_isr_fol()` 是二值 tautology gate (0/1)，Qwen3-4B 不产生 tautology → ISR ≡ prove_rate → 两条件零差异
50	- **教训：binary ISR 无法提供有意义的 reward shaping 信号，必须用连续 ISR**
51	
52	### D010 Reward 公式转向 (2026-05-14)
53	- **旧公式（废弃）**: r = α·r_exec + β·r_exec·ISR, α+β=1 → ISR<1 时永远是 penalty
54	- **新公式**: r = r_exec · (1 + β·ISR), β>0 → ISR 只能 bonus，不能 penalty
55	
56	## Held-out eval_sta 全量结果 (2026-05-14) — 关键
57	
58	### 十组 eval 对比（含 plan016 1000步 + plan018 random β=0.1 + plan009 SFT）
59	
60	| 实验 | Reward | Steps | eval PR | eval ISR | proved_only_ISR | n_components | 退化模式 |
61	|------|--------|-------|---------|----------|-----------------|--------------|----------|
62	| **plan009-sft** | **SFT** | **500** | **0.14** | **0.080** | **0.571** | **—** | **✅ 无 hacking（SFT baseline）** |
63	| plan001-s42 | exec-only | 500 | **93%** | 0.123 | 0.132 | 6.58 | ✅ Genuine proofs |
64	| plan001-s43 | exec-only | 500 | **14%** | 0.000 | 0.000 | N/A | ❌ 长输出退化 |
65	| plan001-s44 | exec-only | 500 | **98%** | 0.570 | 0.582 | 2.04 | ❌ Tautological collapse |
66	| **plan016** | **exec-only** | **1000** | **96%** | **0.003** | **0.003** | **18.55** | **❌ 矛盾爆炸崩塌** |
67	| **plan002-b01** | **additive ISR β=0.1** | 500 | **81%** | **0.337** | **0.415** | **5.58** | **⚠️ H7 16% + H1 52%** |
68	| **plan018** | **additive random β=0.1** | 500 | **79%** | **0.104** | **0.131** | **8.46** | **⚠️ H1 71% 冗余** |
69	| plan002-b03 | additive ISR β=0.3 | 500 | 18% | 0.026 | 0.143 | 10.67 | ❌ 过拟合+低泛化 |
70	| plan017 | additive random β=0.3 | 500 | 48% | 0.045 | 0.094 | 9.6 | ❌ 复杂但无用 |
71	| plan013 | convex random | 500 | 100% | 0.535 | 0.535 | 2.04 | ❌ Tautological hacking |
72	
73	### SFT Baseline 关键发现 (plan009-sft-baseline-s42-r4, 2026-05-14)
74	
75	**Hacking 是 RL-reward-specific，不是 finetuning 通用问题。**
76	
77	- SFT PR=0.14 (vs base 0.12) — 数据曝光几乎不提升 prove rate，RL exploration 才是关键
78	- SFT proved-only ISR=0.571 vs GRPO exec-only ~0.132 — SFT 证明时结构健康，GRPO 学会 "safe padding"
79	- SFT 无 tautological collapse / conclusion embedding 等 hacking 模式
80	
81	### β=0.1 ISR vs Random — D051 定论：ISR 无真实结构优势
82	
83	**D049→D051 迭代过程**：
84	- D049: genuine-only ISR 2.4x (ISR 0.601 vs Random 0.252) → 被认为 ISR 有真实结构优势
85	- D051: premise-count-matched 分析推翻 D049。控制 premise 数后 ISR=0.2578 vs Random=0.2434 = **1.06x**，无差异
86	- **根因**：ISR s42 genuine 的 15/26 (57.7%) 只有 1-2 premises → ISR 天然 ≥0.5（LOO 数学性质）
87	- **ISR s44 的 12 个"genuine"全是 n_prem=1**（H7 分类器 false negative）
88	
89	**教训**：
90	1. **LOO-based metric (ISR) 受 premise count 数学偏差**：更少 premise → 每个更"必要" → ISR 更高，与推理质量无关
91	2. **Premise minimization 不等于推理改善**
92	3. **Raw ISR 对比（3.2x/2.4x）不可信**，必须 premise-count-matched
93	4. **ISR-as-reward 完全失败**：低剂量 gaming ISR（H7），高剂量 PR 崩塌，premise minimization 不是结构改善
94	
95	### Conclusion Embedding 是 GRPO 通用策略 (D049/D051)
96	
97	| 条件 | H7 % | H1 % | Total Embedding | Genuine % |
98	|------|-------|-------|-----------------|-----------|
99	| ISR β=0.1 s42 | 16.0% | 51.9% | 67.9% | 32.1% |
100	| Random β=0.1 s42 | 0% | 70.9% | 70.9% | 29.1% |
101	| Random β=0.1 s44 | 0% | 79.8% | 79.8% | 20.2% |
102	
103	- Random H1 率 (71-80%) **高于** ISR (52%)
104	- H7 是 ISR-specific gaming（ISR 16%, Random 0%）
105	- ISR 改变 hacking 组成（H1→H7）而非减少总量
106	
107	### plan016 延长训练发现 (2026-05-14)
108	
109	- 500步 ISR=0.123 → 1000步 ISR=0.003 (-97.8%)
110	- 退化模式：矛盾爆炸（components 6.58→18.55）
111	- 论文意义：exec-only 延长训练是 reward hacking 恶化的干净消融证据
112	
113	### 跨 seed 退化分类 (2026-05-14, updated with H7/H1 audit)
114	
115	| Seed | 退化模式 | 特征 | H7/H1 | 诊断信号 |
116	|------|----------|------|-------|----------|
117	| s42 | ⚠️ 冗余 embedding | PR=93%, components=6.58 | H1=87.1%, Genuine=12.9% | ~~唯一健康 seed~~ → 87% conclusion embedding, ISR 被冗余 premise 稀释 |
118	| s43 | ❌ Length explosion | PR=14%, 87% hit max_new_tokens | — | D029: 不重训 |
119	| s44 | ❌ Tautological collapse | PR=98%, components=2.04 | H7=100%, Genuine=0% | ISR=0.5 artifact |
120	
121	**关键修正**: exec-only s42 并非 "healthy seed"。87.1% 样本含 conclusion embedding，但冗余 premises 掩盖了 hacking 程度（ISR=0.12 是稀释结果）。所有 exec-only seeds 都有 87-100% conclusion embedding。
122	
123	### 关键教训
124	1. **跨 seed 极不稳定**: exec-only reward landscape 方差极大
125	2. **ISR + component count 联合诊断**能区分 genuine proof vs tautological hack
126	3. ~~ISR-as-reward 有 sweet spot~~ → **D051: ISR-as-reward 完全失败**，β=0.1 表面优势是 premise minimization artifact
127	4. **训练 PR vs eval PR 巨大鸿沟**: 训练 PR 不反映 held-out 泛化能力
128	5. ~~ISR β=0.1 vs random β=0.1: ISR 3.2x 差异证明 ISR 信号有结构价值~~ → **D051 作废**：premise-count-matched 1.06x 无差异
129	6. **LOO-based metric 的固有偏差**：premise count 影响 ISR，不能 raw 对比不同 premise 数的样本
130	
131	## Goodhart 文献定位 (2026-05-14)
132	
133	### 核心 novelty（D051 更新）
134	1. **首个在 neurosymbolic verification reward 上刻画 Goodhart 效应 + meta-Goodhart**
135	2. **ISR-as-reward 全剂量失败**：低剂量 meta-Goodhart（ISR 被 game），高剂量 classic Goodhart（PR 崩塌）
136	3. **Premise minimization confound**：LOO-based metric 的数学偏差——方法论贡献
137	4. **Conclusion embedding 是 GRPO 通用现象**（52-80%），不因 reward type 改变
138	
139	### Goodhart 分类
140	- high-β ISR collapse = **extremal Goodhart** (Manheim & Garrabrant 2019)
141	- low-β ISR gaming = **meta-Goodhart**: diagnostic metric 本身被 game
142	
143	### 文献资产
144	- `artifacts/literature_goodhart.md`: 30+ 篇论文
145	- literature_map.yaml: 33 篇论文，6 类别
146	
147	## Hacking 特征分析 (2026-05-14, plan012 + D044)
148	
149	### 操作性分类（6 种模式，strict exact normalized match, D044）
150	1. **H1 Conclusion Embedding** — 多 premise 中至少一个 premise 完全等于 conclusion
151	2. **Repetition collapse** — 重复生成相同 premise
152	3. **H3 Tautological collapse** — 退化为 2-component (premise=conclusion) 结构
153	4. **H4 Complexity-without-utility** — 生成复杂但无用的 premises
154	5. **Premise padding** — 添加无关 premises 填充
155	6. **H7 Conclusion Duplication with ISR Inflation** — 单 premise = conclusion + ISR 膨胀
156	
157	### H1 计数定论 (2026-05-14)
158	- **Strict normalization**: Random s42 H1=56/79 (70.9%), Random s44 H1=71/89 (79.8%) — 以此为准
159	- 旧值 58/79 (73.4%) 和 74/89 (83.1%) 使用了宽松 normalization，已废弃
160	- Premise-count-matched ratio: ISR=0.2578 vs Random=0.2434 = **1.06×**（非 1.02×）
161	
162	## Prolog 跨 logic type 实验 (2026-05-14, plan006)
163	
164	### plan006-prolog-exec-s42 (DONE, success)
165	- Eval: PR=83%, mean_ISR=0.031, proved_only_ISR=0.037
166	- 高 PR 但近零 ISR
167	
168	### plan006-prolog-sta-s42 (DONE, negative)
169	- Eval: PR=50%, proved-only ISR=1.0, **100% proved 样本是 H7**
170	- Prolog Goodhart 比 FOL 更极端（100 步即饱和）
171	
172	## GPU 隔离教训
173	
174	### C002: 所有命令必须 `export CUDA_VISIBLE_DEVICES=N`
175	- 必须在 `bash -c` 内部 export
176	- submit_training_job 命令格式: `bash -c "export CUDA_VISIBLE_DEVICES=N && ..."`
177	
178	### kill_job 子进程未清理教训 (2026-05-14)
179	- kill_job 只杀 tmux wrapper PID，不杀 Python 训练子进程
180	- 教训: kill_job 后必须 SSH 验证所有子进程已终止
181	
182	### 磁盘
183	- **C003 约束**: `log_completions=False` + `save_total_limit=1`，output_dir 放 `/root/autodl-tmp/outputs/`
184	- 磁盘爆满事故教训：eval 后立即清理 checkpoint
185	
186	## 准备就绪的资产 (2026-05-14)
187	
188	### Prolog STA
189	- 代码+eval 全部就绪
190	- 命令模板：`python3 scripts/train_grpo.py --config configs/grpo_prolog_exec_only.yaml --num_steps 500 --seed {42|43|44} --output_dir ...`（warmup_ratio 默认 0.0）
191	
192	### Eval 脚本
193	- eval_sta.py: FOL + Prolog 双支持，就绪
194	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f8a623d4-4736-4f28-98e7-c9460074e673",
  "uuid": "8175815c-4173-481a-a2ee-f0c1465262ae",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/memory.md",
      "content": "# solver-trace-ablation — Memory\n\n## 环境信息 (2026-05-13)\n\n### westd-39279 服务器\n- **GPU**: 2× RTX PRO 6000 Blackwell, 94GB VRAM 每张\n- **CUDA**: 12.8, PyTorch 2.10.0+cu128\n- **镜像**: aml-train（conda 环境，`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`）\n- **ML 栈**: transformers/trl/vllm/accelerate 全部预装\n- **Solvers**: Prover9 (LADR 2009-11A 源码编译), SWI-Prolog 8.4.2 (`/usr/bin/swipl`), Z3 4.16.0.0\n- **模型**: Qwen3-4B 已下载（7.6GB，通过 ModelScope）\n- **代码路径**: `/root/solver-trace-ablation/`\n- **磁盘**: 系统盘 30GB (22G free)，数据盘 `/root/autodl-tmp/` 250GB (清理后 ~131G free)\n\n### 决策记录\n- Qwen3-4B 用 ModelScope 下载（HuggingFace 直连可能慢）\n- Prover9 从 LADR 源码编译（apt 无包）\n- 94GB VRAM 单卡跑 Qwen3-4B 完全无压力\n\n## 数据 (2026-05-13)\n\n### 数据源变更：ProofWriter → FOLIO\n- ProofWriter 原始数据无 FOL 列，改用 `tasksource/folio`（1204 条人工标注 FOL）\n- Phase 0 子集 100 条，训练子集 500 条\n- 34% 数据含 XOR (⊕) 符号，已在 `_normalize_fol()` 中修复展开\n\n### 数据约束 (2026-05-14, D009)\n- **C001**: 所有 plan001/plan013 实验统一使用 `train_500_seed42.jsonl`，不再用 `proofwriter_fol_500.jsonl`（消除数据差异 confound）\n\n## Phase 0 关键发现 (2026-05-13)\n\n### Base Model ISR Baseline (sta-phase0-baseline)\n- **Prove rate**: 12% overall, 18.2% excluding XOR-affected samples\n- **Mean ISR**: 0.064 (very low — base model formalizations mostly unprovable)\n- **ISR 区分度**: proved 样本 ISR 0.125–0.889\n\n### Ground-Truth ISR Baseline (sta-gt-isr-baseline)\n- **GT prove rate**: 18% (limited by Prover9 only proving entailment; true=50%, false=4%, unknown=0%)\n- **GT mean ISR**: 0.5588 (median 0.6125, range 0.14–1.00)\n- **Model vs GT gap**: ISR 0.064 vs 0.559 = 8.7x 差距，STA 有强区分力\n\n### Prover9 局限性\n- Prover9 只能证明 entailment（conclusion 从 premises 推出）\n- `false` 和 `unknown` 类问题几乎无法证明（false 4%, unknown 0%）\n\n## Phase 1 关键经验 (2026-05-13)\n\n### fast_isr_fol 失败教训 (r4)\n- `fast_isr_fol()` 是二值 tautology gate (0/1)，Qwen3-4B 不产生 tautology → ISR ≡ prove_rate → 两条件零差异\n- **教训：binary ISR 无法提供有意义的 reward shaping 信号，必须用连续 ISR**\n\n### D010 Reward 公式转向 (2026-05-14)\n- **旧公式（废弃）**: r = α·r_exec + β·r_exec·ISR, α+β=1 → ISR<1 时永远是 penalty\n- **新公式**: r = r_exec · (1 + β·ISR), β>0 → ISR 只能 bonus，不能 penalty\n\n## Held-out eval_sta 全量结果 (2026-05-14) — 关键\n\n### 十组 eval 对比（含 plan016 1000步 + plan018 random β=0.1 + plan009 SFT）\n\n| 实验 | Reward | Steps | eval PR | eval ISR | proved_only_ISR | n_components | 退化模式 |\n|------|--------|-------|---------|----------|-----------------|--------------|----------|\n| **plan009-sft** | **SFT** | **500** | **0.14** | **0.080** | **0.571** | **—** | **✅ 无 hacking（SFT baseline）** |\n| plan001-s42 | exec-only | 500 | **93%** | 0.123 | 0.132 | 6.58 | ✅ Genuine proofs |\n| plan001-s43 | exec-only | 500 | **14%** | 0.000 | 0.000 | N/A | ❌ 长输出退化 |\n| plan001-s44 | exec-only | 500 | **98%** | 0.570 | 0.582 | 2.04 | ❌ Tautological collapse |\n| **plan016** | **exec-only** | **1000** | **96%** | **0.003** | **0.003** | **18.55** | **❌ 矛盾爆炸崩塌** |\n| **plan002-b01** | **additive ISR β=0.1** | 500 | **81%** | **0.337** | **0.415** | **5.58** | **⚠️ H7 16% + H1 52%** |\n| **plan018** | **additive random β=0.1** | 500 | **79%** | **0.104** | **0.131** | **8.46** | **⚠️ H1 71% 冗余** |\n| plan002-b03 | additive ISR β=0.3 | 500 | 18% | 0.026 | 0.143 | 10.67 | ❌ 过拟合+低泛化 |\n| plan017 | additive random β=0.3 | 500 | 48% | 0.045 | 0.094 | 9.6 | ❌ 复杂但无用 |\n| plan013 | convex random | 500 | 100% | 0.535 | 0.535 | 2.04 | ❌ Tautological hacking |\n\n### SFT Baseline 关键发现 (plan009-sft-baseline-s42-r4, 2026-05-14)\n\n**Hacking 是 RL-reward-specific，不是 finetuning 通用问题。**\n\n- SFT PR=0.14 (vs base 0.12) — 数据曝光几乎不提升 prove rate，RL exploration 才是关键\n- SFT proved-only ISR=0.571 vs GRPO exec-only ~0.132 — SFT 证明时结构健康，GRPO 学会 \"safe padding\"\n- SFT 无 tautological collapse / conclusion embedding 等 hacking 模式\n\n### β=0.1 ISR vs Random — D051 定论：ISR 无真实结构优势\n\n**D049→D051 迭代过程**：\n- D049: genuine-only ISR 2.4x (ISR 0.601 vs Random 0.252) → 被认为 ISR 有真实结构优势\n- D051: premise-count-matched 分析推翻 D049。控制 premise 数后 ISR=0.2578 vs Random=0.2434 = **1.06x**，无差异\n- **根因**：ISR s42 genuine 的 15/26 (57.7%) 只有 1-2 premises → ISR 天然 ≥0.5（LOO 数学性质）\n- **ISR s44 的 12 个\"genuine\"全是 n_prem=1**（H7 分类器 false negative）\n\n**教训**：\n1. **LOO-based metric (ISR) 受 premise count 数学偏差**：更少 premise → 每个更\"必要\" → ISR 更高，与推理质量无关\n2. **Premise minimization 不等于推理改善**\n3. **Raw ISR 对比（3.2x/2.4x）不可信**，必须 premise-count-matched\n4. **ISR-as-reward 完全失败**：低剂量 gaming ISR（H7），高剂量 PR 崩塌，premise minimization 不是结构改善\n\n### Conclusion Embedding 是 GRPO 通用策略 (D049/D051)\n\n| 条件 | H7 % | H1 % | Total Embedding | Genuine % |\n|------|-------|-------|-----------------|-----------|\n| ISR β=0.1 s42 | 16.0% | 51.9% | 67.9% | 32.1% |\n| Random β=0.1 s42 | 0% | 70.9% | 70.9% | 29.1% |\n| Random β=0.1 s44 | 0% | 79.8% | 79.8% | 20.2% |\n\n- Random H1 率 (71-80%) **高于** ISR (52%)\n- H7 是 ISR-specific gaming（ISR 16%, Random 0%）\n- ISR 改变 hacking 组成（H1→H7）而非减少总量\n\n### plan016 延长训练发现 (2026-05-14)\n\n- 500步 ISR=0.123 → 1000步 ISR=0.003 (-97.8%)\n- 退化模式：矛盾爆炸（components 6.58→18.55）\n- 论文意义：exec-only 延长训练是 reward hacking 恶化的干净消融证据\n\n### 跨 seed 退化分类 (2026-05-14, updated with H7/H1 audit)\n\n| Seed | 退化模式 | 特征 | H7/H1 | 诊断信号 |\n|------|----------|------|-------|----------|\n| s42 | ⚠️ 冗余 embedding | PR=93%, components=6.58 | H1=87.1%, Genuine=12.9% | ~~唯一健康 seed~~ → 87% conclusion embedding, ISR 被冗余 premise 稀释 |\n| s43 | ❌ Length explosion | PR=14%, 87% hit max_new_tokens | — | D029: 不重训 |\n| s44 | ❌ Tautological collapse | PR=98%, components=2.04 | H7=100%, Genuine=0% | ISR=0.5 artifact |\n\n**关键修正**: exec-only s42 并非 \"healthy seed\"。87.1% 样本含 conclusion embedding，但冗余 premises 掩盖了 hacking 程度（ISR=0.12 是稀释结果）。所有 exec-only seeds 都有 87-100% conclusion embedding。\n\n### 关键教训\n1. **跨 seed 极不稳定**: exec-only reward landscape 方差极大\n2. **ISR + component count 联合诊断**能区分 genuine proof vs tautological hack\n3. ~~ISR-as-reward 有 sweet spot~~ → **D051: ISR-as-reward 完全失败**，β=0.1 表面优势是 premise minimization artifact\n4. **训练 PR vs eval PR 巨大鸿沟**: 训练 PR 不反映 held-out 泛化能力\n5. ~~ISR β=0.1 vs random β=0.1: ISR 3.2x 差异证明 ISR 信号有结构价值~~ → **D051 作废**：premise-count-matched 1.06x 无差异\n6. **LOO-based metric 的固有偏差**：premise count 影响 ISR，不能 raw 对比不同 premise 数的样本\n\n## Goodhart 文献定位 (2026-05-14)\n\n### 核心 novelty（D051 更新）\n1. **首个在 neurosymbolic verification reward 上刻画 Goodhart 效应 + meta-Goodhart**\n2. **ISR-as-reward 全剂量失败**：低剂量 meta-Goodhart（ISR 被 game），高剂量 classic Goodhart（PR 崩塌）\n3. **Premise minimization confound**：LOO-based metric 的数学偏差——方法论贡献\n4. **Conclusion embedding 是 GRPO 通用现象**（52-80%），不因 reward type 改变\n\n### Goodhart 分类\n- high-β ISR collapse = **extremal Goodhart** (Manheim & Garrabrant 2019)\n- low-β ISR gaming = **meta-Goodhart**: diagnostic metric 本身被 game\n\n### 文献资产\n- `artifacts/literature_goodhart.md`: 30+ 篇论文\n- literature_map.yaml: 33 篇论文，6 类别\n\n## Hacking 特征分析 (2026-05-14, plan012 + D044)\n\n### 操作性分类（6 种模式，strict exact normalized match, D044）\n1. **H1 Conclusion Embedding** — 多 premise 中至少一个 premise 完全等于 conclusion\n2. **Repetition collapse** — 重复生成相同 premise\n3. **H3 Tautological collapse** — 退化为 2-component (premise=conclusion) 结构\n4. **H4 Complexity-without-utility** — 生成复杂但无用的 premises\n5. **Premise padding** — 添加无关 premises 填充\n6. **H7 Conclusion Duplication with ISR Inflation** — 单 premise = conclusion + ISR 膨胀\n\n### H1 计数定论 (2026-05-14)\n- **Strict normalization**: Random s42 H1=56/79 (70.9%), Random s44 H1=71/89 (79.8%) — 以此为准\n- 旧值 58/79 (73.4%) 和 74/89 (83.1%) 使用了宽松 normalization，已废弃\n- Premise-count-matched ratio: ISR=0.2578 vs Random=0.2434 = **1.06×**（非 1.02×）\n\n## Prolog 跨 logic type 实验 (2026-05-14, plan006)\n\n### plan006-prolog-exec-s42 (DONE, success)\n- Eval: PR=83%, mean_ISR=0.031, proved_only_ISR=0.037\n- 高 PR 但近零 ISR\n\n### plan006-prolog-sta-s42 (DONE, negative)\n- Eval: PR=50%, proved-only ISR=1.0, **100% proved 样本是 H7**\n- Prolog Goodhart 比 FOL 更极端（100 步即饱和）\n\n## GPU 隔离教训\n\n### C002: 所有命令必须 `export CUDA_VISIBLE_DEVICES=N`\n- 必须在 `bash -c` 内部 export\n- submit_training_job 命令格式: `bash -c \"export CUDA_VISIBLE_DEVICES=N && ...\"`\n\n### kill_job 子进程未清理教训 (2026-05-14)\n- kill_job 只杀 tmux wrapper PID，不杀 Python 训练子进程\n- 教训: kill_job 后必须 SSH 验证所有子进程已终止\n\n### 磁盘\n- **C003 约束**: `log_completions=False` + `save_total_limit=1`，output_dir 放 `/root/autodl-tmp/outputs/`\n- 磁盘爆满事故教训：eval 后立即清理 checkpoint\n\n## 准备就绪的资产 (2026-05-14)\n\n### Prolog STA\n- 代码+eval 全部就绪\n- 命令模板：`python3 scripts/train_grpo.py --config configs/grpo_prolog_exec_only.yaml --num_steps 500 --seed {42|43|44} --output_dir ...`（warmup_ratio 默认 0.0）\n\n### Eval 脚本\n- eval_sta.py: FOL + Prolog 双支持，就绪\n",
      "numLines": 194,
      "startLine": 1,
      "totalLines": 194
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
I need to find the "## Prolog 跨 logic type 实验 (2026-05-14, plan006)" section and append the new data after the existing content in that section, before the "## GPU 隔离教训" section.

The section currently ends at line 171. I need to add the new data after line 171 (the last line of plan006-prolog-sta-s42) and before line 173 (## GPU 隔离教训).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f8a623d4-4736-4f28-98e7-c9460074e673",
  "uuid": "b3f8d1d8-8961-4922-aeff-ca422a85cd6b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M33jkue2za49QKioj4beeB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5123,
      "cache_read_input_tokens": 23994,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5123
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

_source line 8_

<details open><summary>🔧 Tool call — Edit · `toolu_012ShyiAyFmT8VYTYPwzRsGB`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/memory.md",
  "old_string": "### plan006-prolog-sta-s42 (DONE, negative)\n- Eval: PR=50%, proved-only ISR=1.0, **100% proved 样本是 H7**\n- Prolog Goodhart 比 FOL 更极端（100 步即饱和）\n\n## GPU 隔离教训",
  "new_string": "### plan006-prolog-sta-s42 (DONE, negative)\n- Eval: PR=50%, proved-only ISR=1.0, **100% proved 样本是 H7**\n- Prolog Goodhart 比 FOL 更极端（100 步即饱和）\n\n### plan006-prolog-exec-s43-r3 (DONE, negative)\n- Eval: PR=56%, mean_ISR=0.008, proved_only_ISR=0.015, n_proved=56\n- 退化模式：degraded（PR 大幅低于 s42）\n\n### plan006-prolog-exec-s44 (DONE, negative)\n- Eval: PR=21%, mean_ISR=0.081, proved_only_ISR=0.387, n_proved=21\n- 异常：PR 最低但 proved-only ISR 最高——small-sample artifact\n- severe degradation\n\n### 3-seed exec-only Prolog 汇总\n- PR = 53.3% ± 31.1%（极不稳定，复现 FOL 模式）\n- Mean ISR = 0.040 ± 0.037\n- 所有 seeds ISR < 0.1，确认 exec-only 跨 logic type 均不产生 genuine reasoning traces\n\n## GPU 隔离教训"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f8a623d4-4736-4f28-98e7-c9460074e673",
  "uuid": "436d299c-cfb2-40b9-abbe-3a9958d96c46",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M33jkue2za49QKioj4beeB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5123,
      "cache_read_input_tokens": 23994,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5123
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

_source line 9 · 2026-05-14T16:32:40.887Z_

<details><summary>↩ Tool result · `toolu_012ShyiAyFmT8VYTYPwzRsGB`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/memory.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f8a623d4-4736-4f28-98e7-c9460074e673",
  "uuid": "98dd828f-8429-4c56-9b97-5a715c7f5f3b",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/memory.md",
    "oldString": "### plan006-prolog-sta-s42 (DONE, negative)\n- Eval: PR=50%, proved-only ISR=1.0, **100% proved 样本是 H7**\n- Prolog Goodhart 比 FOL 更极端（100 步即饱和）\n\n## GPU 隔离教训",
    "newString": "### plan006-prolog-sta-s42 (DONE, negative)\n- Eval: PR=50%, proved-only ISR=1.0, **100% proved 样本是 H7**\n- Prolog Goodhart 比 FOL 更极端（100 步即饱和）\n\n### plan006-prolog-exec-s43-r3 (DONE, negative)\n- Eval: PR=56%, mean_ISR=0.008, proved_only_ISR=0.015, n_proved=56\n- 退化模式：degraded（PR 大幅低于 s42）\n\n### plan006-prolog-exec-s44 (DONE, negative)\n- Eval: PR=21%, mean_ISR=0.081, proved_only_ISR=0.387, n_proved=21\n- 异常：PR 最低但 proved-only ISR 最高——small-sample artifact\n- severe degradation\n\n### 3-seed exec-only Prolog 汇总\n- PR = 53.3% ± 31.1%（极不稳定，复现 FOL 模式）\n- Mean ISR = 0.040 ± 0.037\n- 所有 seeds ISR < 0.1，确认 exec-only 跨 logic type 均不产生 genuine reasoning traces\n\n## GPU 隔离教训",
    "originalFile": "# solver-trace-ablation — Memory\n\n## 环境信息 (2026-05-13)\n\n### westd-39279 服务器\n- **GPU**: 2× RTX PRO 6000 Blackwell, 94GB VRAM 每张\n- **CUDA**: 12.8, PyTorch 2.10.0+cu128\n- **镜像**: aml-train（conda 环境，`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`）\n- **ML 栈**: transformers/trl/vllm/accelerate 全部预装\n- **Solvers**: Prover9 (LADR 2009-11A 源码编译), SWI-Prolog 8.4.2 (`/usr/bin/swipl`), Z3 4.16.0.0\n- **模型**: Qwen3-4B 已下载（7.6GB，通过 ModelScope）\n- **代码路径**: `/root/solver-trace-ablation/`\n- **磁盘**: 系统盘 30GB (22G free)，数据盘 `/root/autodl-tmp/` 250GB (清理后 ~131G free)\n\n### 决策记录\n- Qwen3-4B 用 ModelScope 下载（HuggingFace 直连可能慢）\n- Prover9 从 LADR 源码编译（apt 无包）\n- 94GB VRAM 单卡跑 Qwen3-4B 完全无压力\n\n## 数据 (2026-05-13)\n\n### 数据源变更：ProofWriter → FOLIO\n- ProofWriter 原始数据无 FOL 列，改用 `tasksource/folio`（1204 条人工标注 FOL）\n- Phase 0 子集 100 条，训练子集 500 条\n- 34% 数据含 XOR (⊕) 符号，已在 `_normalize_fol()` 中修复展开\n\n### 数据约束 (2026-05-14, D009)\n- **C001**: 所有 plan001/plan013 实验统一使用 `train_500_seed42.jsonl`，不再用 `proofwriter_fol_500.jsonl`（消除数据差异 confound）\n\n## Phase 0 关键发现 (2026-05-13)\n\n### Base Model ISR Baseline (sta-phase0-baseline)\n- **Prove rate**: 12% overall, 18.2% excluding XOR-affected samples\n- **Mean ISR**: 0.064 (very low — base model formalizations mostly unprovable)\n- **ISR 区分度**: proved 样本 ISR 0.125–0.889\n\n### Ground-Truth ISR Baseline (sta-gt-isr-baseline)\n- **GT prove rate**: 18% (limited by Prover9 only proving entailment; true=50%, false=4%, unknown=0%)\n- **GT mean ISR**: 0.5588 (median 0.6125, range 0.14–1.00)\n- **Model vs GT gap**: ISR 0.064 vs 0.559 = 8.7x 差距，STA 有强区分力\n\n### Prover9 局限性\n- Prover9 只能证明 entailment（conclusion 从 premises 推出）\n- `false` 和 `unknown` 类问题几乎无法证明（false 4%, unknown 0%）\n\n## Phase 1 关键经验 (2026-05-13)\n\n### fast_isr_fol 失败教训 (r4)\n- `fast_isr_fol()` 是二值 tautology gate (0/1)，Qwen3-4B 不产生 tautology → ISR ≡ prove_rate → 两条件零差异\n- **教训：binary ISR 无法提供有意义的 reward shaping 信号，必须用连续 ISR**\n\n### D010 Reward 公式转向 (2026-05-14)\n- **旧公式（废弃）**: r = α·r_exec + β·r_exec·ISR, α+β=1 → ISR<1 时永远是 penalty\n- **新公式**: r = r_exec · (1 + β·ISR), β>0 → ISR 只能 bonus，不能 penalty\n\n## Held-out eval_sta 全量结果 (2026-05-14) — 关键\n\n### 十组 eval 对比（含 plan016 1000步 + plan018 random β=0.1 + plan009 SFT）\n\n| 实验 | Reward | Steps | eval PR | eval ISR | proved_only_ISR | n_components | 退化模式 |\n|------|--------|-------|---------|----------|-----------------|--------------|----------|\n| **plan009-sft** | **SFT** | **500** | **0.14** | **0.080** | **0.571** | **—** | **✅ 无 hacking（SFT baseline）** |\n| plan001-s42 | exec-only | 500 | **93%** | 0.123 | 0.132 | 6.58 | ✅ Genuine proofs |\n| plan001-s43 | exec-only | 500 | **14%** | 0.000 | 0.000 | N/A | ❌ 长输出退化 |\n| plan001-s44 | exec-only | 500 | **98%** | 0.570 | 0.582 | 2.04 | ❌ Tautological collapse |\n| **plan016** | **exec-only** | **1000** | **96%** | **0.003** | **0.003** | **18.55** | **❌ 矛盾爆炸崩塌** |\n| **plan002-b01** | **additive ISR β=0.1** | 500 | **81%** | **0.337** | **0.415** | **5.58** | **⚠️ H7 16% + H1 52%** |\n| **plan018** | **additive random β=0.1** | 500 | **79%** | **0.104** | **0.131** | **8.46** | **⚠️ H1 71% 冗余** |\n| plan002-b03 | additive ISR β=0.3 | 500 | 18% | 0.026 | 0.143 | 10.67 | ❌ 过拟合+低泛化 |\n| plan017 | additive random β=0.3 | 500 | 48% | 0.045 | 0.094 | 9.6 | ❌ 复杂但无用 |\n| plan013 | convex random | 500 | 100% | 0.535 | 0.535 | 2.04 | ❌ Tautological hacking |\n\n### SFT Baseline 关键发现 (plan009-sft-baseline-s42-r4, 2026-05-14)\n\n**Hacking 是 RL-reward-specific，不是 finetuning 通用问题。**\n\n- SFT PR=0.14 (vs base 0.12) — 数据曝光几乎不提升 prove rate，RL exploration 才是关键\n- SFT proved-only ISR=0.571 vs GRPO exec-only ~0.132 — SFT 证明时结构健康，GRPO 学会 \"safe padding\"\n- SFT 无 tautological collapse / conclusion embedding 等 hacking 模式\n\n### β=0.1 ISR vs Random — D051 定论：ISR 无真实结构优势\n\n**D049→D051 迭代过程**：\n- D049: genuine-only ISR 2.4x (ISR 0.601 vs Random 0.252) → 被认为 ISR 有真实结构优势\n- D051: premise-count-matched 分析推翻 D049。控制 premise 数后 ISR=0.2578 vs Random=0.2434 = **1.06x**，无差异\n- **根因**：ISR s42 genuine 的 15/26 (57.7%) 只有 1-2 premises → ISR 天然 ≥0.5（LOO 数学性质）\n- **ISR s44 的 12 个\"genuine\"全是 n_prem=1**（H7 分类器 false negative）\n\n**教训**：\n1. **LOO-based metric (ISR) 受 premise count 数学偏差**：更少 premise → 每个更\"必要\" → ISR 更高，与推理质量无关\n2. **Premise minimization 不等于推理改善**\n3. **Raw ISR 对比（3.2x/2.4x）不可信**，必须 premise-count-matched\n4. **ISR-as-reward 完全失败**：低剂量 gaming ISR（H7），高剂量 PR 崩塌，premise minimization 不是结构改善\n\n### Conclusion Embedding 是 GRPO 通用策略 (D049/D051)\n\n| 条件 | H7 % | H1 % | Total Embedding | Genuine % |\n|------|-------|-------|-----------------|-----------|\n| ISR β=0.1 s42 | 16.0% | 51.9% | 67.9% | 32.1% |\n| Random β=0.1 s42 | 0% | 70.9% | 70.9% | 29.1% |\n| Random β=0.1 s44 | 0% | 79.8% | 79.8% | 20.2% |\n\n- Random H1 率 (71-80%) **高于** ISR (52%)\n- H7 是 ISR-specific gaming（ISR 16%, Random 0%）\n- ISR 改变 hacking 组成（H1→H7）而非减少总量\n\n### plan016 延长训练发现 (2026-05-14)\n\n- 500步 ISR=0.123 → 1000步 ISR=0.003 (-97.8%)\n- 退化模式：矛盾爆炸（components 6.58→18.55）\n- 论文意义：exec-only 延长训练是 reward hacking 恶化的干净消融证据\n\n### 跨 seed 退化分类 (2026-05-14, updated with H7/H1 audit)\n\n| Seed | 退化模式 | 特征 | H7/H1 | 诊断信号 |\n|------|----------|------|-------|----------|\n| s42 | ⚠️ 冗余 embedding | PR=93%, components=6.58 | H1=87.1%, Genuine=12.9% | ~~唯一健康 seed~~ → 87% conclusion embedding, ISR 被冗余 premise 稀释 |\n| s43 | ❌ Length explosion | PR=14%, 87% hit max_new_tokens | — | D029: 不重训 |\n| s44 | ❌ Tautological collapse | PR=98%, components=2.04 | H7=100%, Genuine=0% | ISR=0.5 artifact |\n\n**关键修正**: exec-only s42 并非 \"healthy seed\"。87.1% 样本含 conclusion embedding，但冗余 premises 掩盖了 hacking 程度（ISR=0.12 是稀释结果）。所有 exec-only seeds 都有 87-100% conclusion embedding。\n\n### 关键教训\n1. **跨 seed 极不稳定**: exec-only reward landscape 方差极大\n2. **ISR + component count 联合诊断**能区分 genuine proof vs tautological hack\n3. ~~ISR-as-reward 有 sweet spot~~ → **D051: ISR-as-reward 完全失败**，β=0.1 表面优势是 premise minimization artifact\n4. **训练 PR vs eval PR 巨大鸿沟**: 训练 PR 不反映 held-out 泛化能力\n5. ~~ISR β=0.1 vs random β=0.1: ISR 3.2x 差异证明 ISR 信号有结构价值~~ → **D051 作废**：premise-count-matched 1.06x 无差异\n6. **LOO-based metric 的固有偏差**：premise count 影响 ISR，不能 raw 对比不同 premise 数的样本\n\n## Goodhart 文献定位 (2026-05-14)\n\n### 核心 novelty（D051 更新）\n1. **首个在 neurosymbolic verification reward 上刻画 Goodhart 效应 + meta-Goodhart**\n2. **ISR-as-reward 全剂量失败**：低剂量 meta-Goodhart（ISR 被 game），高剂量 classic Goodhart（PR 崩塌）\n3. **Premise minimization confound**：LOO-based metric 的数学偏差——方法论贡献\n4. **Conclusion embedding 是 GRPO 通用现象**（52-80%），不因 reward type 改变\n\n### Goodhart 分类\n- high-β ISR collapse = **extremal Goodhart** (Manheim & Garrabrant 2019)\n- low-β ISR gaming = **meta-Goodhart**: diagnostic metric 本身被 game\n\n### 文献资产\n- `artifacts/literature_goodhart.md`: 30+ 篇论文\n- literature_map.yaml: 33 篇论文，6 类别\n\n## Hacking 特征分析 (2026-05-14, plan012 + D044)\n\n### 操作性分类（6 种模式，strict exact normalized match, D044）\n1. **H1 Conclusion Embedding** — 多 premise 中至少一个 premise 完全等于 conclusion\n2. **Repetition collapse** — 重复生成相同 premise\n3. **H3 Tautological collapse** — 退化为 2-component (premise=conclusion) 结构\n4. **H4 Complexity-without-utility** — 生成复杂但无用的 premises\n5. **Premise padding** — 添加无关 premises 填充\n6. **H7 Conclusion Duplication with ISR Inflation** — 单 premise = conclusion + ISR 膨胀\n\n### H1 计数定论 (2026-05-14)\n- **Strict normalization**: Random s42 H1=56/79 (70.9%), Random s44 H1=71/89 (79.8%) — 以此为准\n- 旧值 58/79 (73.4%) 和 74/89 (83.1%) 使用了宽松 normalization，已废弃\n- Premise-count-matched ratio: ISR=0.2578 vs Random=0.2434 = **1.06×**（非 1.02×）\n\n## Prolog 跨 logic type 实验 (2026-05-14, plan006)\n\n### plan006-prolog-exec-s42 (DONE, success)\n- Eval: PR=83%, mean_ISR=0.031, proved_only_ISR=0.037\n- 高 PR 但近零 ISR\n\n### plan006-prolog-sta-s42 (DONE, negative)\n- Eval: PR=50%, proved-only ISR=1.0, **100% proved 样本是 H7**\n- Prolog Goodhart 比 FOL 更极端（100 步即饱和）\n\n## GPU 隔离教训\n\n### C002: 所有命令必须 `export CUDA_VISIBLE_DEVICES=N`\n- 必须在 `bash -c` 内部 export\n- submit_training_job 命令格式: `bash -c \"export CUDA_VISIBLE_DEVICES=N && ...\"`\n\n### kill_job 子进程未清理教训 (2026-05-14)\n- kill_job 只杀 tmux wrapper PID，不杀 Python 训练子进程\n- 教训: kill_job 后必须 SSH 验证所有子进程已终止\n\n### 磁盘\n- **C003 约束**: `log_completions=False` + `save_total_limit=1`，output_dir 放 `/root/autodl-tmp/outputs/`\n- 磁盘爆满事故教训：eval 后立即清理 checkpoint\n\n## 准备就绪的资产 (2026-05-14)\n\n### Prolog STA\n- 代码+eval 全部就绪\n- 命令模板：`python3 scripts/train_grpo.py --config configs/grpo_prolog_exec_only.yaml --num_steps 500 --seed {42|43|44} --output_dir ...`（warmup_ratio 默认 0.0）\n\n### Eval 脚本\n- eval_sta.py: FOL + Prolog 双支持，就绪\n",
    "structuredPatch": [
      {
        "oldStart": 169,
        "oldLines": 6,
        "newStart": 169,
        "newLines": 20,
        "lines": [
          " - Eval: PR=50%, proved-only ISR=1.0, **100% proved 样本是 H7**",
          " - Prolog Goodhart 比 FOL 更极端（100 步即饱和）",
          " ",
          "+### plan006-prolog-exec-s43-r3 (DONE, negative)",
          "+- Eval: PR=56%, mean_ISR=0.008, proved_only_ISR=0.015, n_proved=56",
          "+- 退化模式：degraded（PR 大幅低于 s42）",
          "+",
          "+### plan006-prolog-exec-s44 (DONE, negative)",
          "+- Eval: PR=21%, mean_ISR=0.081, proved_only_ISR=0.387, n_proved=21",
          "+- 异常：PR 最低但 proved-only ISR 最高——small-sample artifact",
          "+- severe degradation",
          "+",
          "+### 3-seed exec-only Prolog 汇总",
          "+- PR = 53.3% ± 31.1%（极不稳定，复现 FOL 模式）",
          "+- Mean ISR = 0.040 ± 0.037",
          "+- 所有 seeds ISR < 0.1，确认 exec-only 跨 logic type 均不产生 genuine reasoning traces",
          "+",
          " ## GPU 隔离教训",
          " ",
          " ### C002: 所有命令必须 `export CUDA_VISIBLE_DEVICES=N`"
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

_source line 10_

已更新 memory.md，在 plan006 section 末尾追加了 s43-r3、s44 和 3-seed 汇总数据。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f8a623d4-4736-4f28-98e7-c9460074e673",
  "uuid": "1c0c3cf3-c74f-4ea5-8312-3e672fac3731",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GdGBC1E91S4HCDiCem16Wu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 747,
      "cache_read_input_tokens": 29117,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 747
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

_source line 11_

已更新 memory.md，在 plan006 section 末尾追加了 s43-r3、s44 和 3-seed 汇总数据。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 20186,
  "duration_api_ms": 21236,
  "num_turns": 3,
  "stop_reason": "end_turn",
  "session_id": "f8a623d4-4736-4f28-98e7-c9460074e673",
  "total_cost_usd": 0.16840475,
  "usage": {
    "input_tokens": 5,
    "cache_creation_input_tokens": 18023,
    "cache_read_input_tokens": 64952,
    "output_tokens": 845,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 18023,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 46,
        "cache_read_input_tokens": 29117,
        "cache_creation_input_tokens": 747,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 747
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2020,
      "outputTokens": 23,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002135,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 5,
      "outputTokens": 845,
      "cacheReadInputTokens": 64952,
      "cacheCreationInputTokens": 18023,
      "webSearchRequests": 0,
      "costUSD": 0.16626975,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "9b43d413-3b14-4c62-8cac-4cb0f4ef371e"
}
```

</details>

---
