# research paper update locations

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 89
- **Recorded user turns:** 1
- **Tool calls:** 32
- **Original source:** `logs/workers/worker_research_paper_update_locations_20260514T214853.log`
- **Structured JSON:** [`4e77f139c4450bdc1ecf.json`](../../sessions/4e/4e77f139c4450bdc1ecf.json)

## Before a recorded user message

6 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "session_id": "10233ec7-5d03-448a-9224-b6173ea0cbe8",
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
  "uuid": "6911fdcf-9b27-4976-bc1f-37b7ccddde43",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse/memory/"
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
    "resetsAt": 1778812800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "44999736-8b77-442a-843d-0da1c946f39c",
  "session_id": "10233ec7-5d03-448a-9224-b6173ea0cbe8"
}
```

---

### Assistant

_source line 4_

I'll start by reading the existing checklist and then systematically go through all .tex files to build the precise location map.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10233ec7-5d03-448a-9224-b6173ea0cbe8",
  "uuid": "dfd367e1-b25c-4a16-97fb-f7067d4d151b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017kHCvv7YQDvNJ9WM3P7iA3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12483,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12483
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

<details open><summary>🔧 Tool call — Agent · `toolu_014G9a6m4Szoqsuk1hAsUCbW`</summary>

```json
{
  "description": "Read existing checklist and project context",
  "prompt": "Read the following files and return their full contents:\n1. /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/n500_update_checklist.md\n2. /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper_framing.md (if exists)\n\nAlso list all .tex files in /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/ and report their names.\n\nReport everything verbatim — I need the full content of each file.",
  "subagent_type": "Explore"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10233ec7-5d03-448a-9224-b6173ea0cbe8",
  "uuid": "70ab3962-3f17-42fa-8224-3c546595f8ff",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017kHCvv7YQDvNJ9WM3P7iA3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12483,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12483
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

### System

_source line 6_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "acde2f40d7c479977",
  "tool_use_id": "toolu_014G9a6m4Szoqsuk1hAsUCbW",
  "description": "Read existing checklist and project context",
  "task_type": "local_agent",
  "prompt": "Read the following files and return their full contents:\n1. /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/n500_update_checklist.md\n2. /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper_framing.md (if exists)\n\nAlso list all .tex files in /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/ and report their names.\n\nReport everything verbatim — I need the full content of each file.",
  "uuid": "86ef8b7d-8f7c-4ac5-827f-2986431a4b3f",
  "session_id": "10233ec7-5d03-448a-9224-b6173ea0cbe8"
}
```

---

## Round 1

83 recorded events

### User

_source line 7 · 2026-05-14T21:49:08.290Z_

Read the following files and return their full contents:
1. /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/n500_update_checklist.md
2. /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper_framing.md (if exists)

Also list all .tex files in /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/ and report their names.

Report everything verbatim — I need the full content of each file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_014G9a6m4Szoqsuk1hAsUCbW",
  "session_id": "10233ec7-5d03-448a-9224-b6173ea0cbe8",
  "uuid": "91b7f669-35a1-47f8-bf14-ac6b00a8941c"
}
```

</details>

---

### System

_source line 8_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "acde2f40d7c479977",
  "tool_use_id": "toolu_014G9a6m4Szoqsuk1hAsUCbW",
  "description": "Reading artifacts/n500_update_checklist.md",
  "usage": {
    "total_tokens": 17937,
    "tool_uses": 1,
    "duration_ms": 2048
  },
  "last_tool_name": "Read",
  "uuid": "cdfe0721-071b-4826-8ad3-e577d03b0ca3",
  "session_id": "10233ec7-5d03-448a-9224-b6173ea0cbe8"
}
```

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — Read · `toolu_01KrjMQS1kQuK2wBmqFERAw3`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/n500_update_checklist.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_014G9a6m4Szoqsuk1hAsUCbW",
  "session_id": "10233ec7-5d03-448a-9224-b6173ea0cbe8",
  "uuid": "678879f0-407d-4b03-92a2-a135b1d8e06f",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01C7xoST66UBjZWsSLoNWgcV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17926,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17926,
        "ephemeral_1h_input_tokens": 0
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

_source line 10 · 2026-05-14T21:49:10.416Z_

<details><summary>↩ Tool result · `toolu_01KrjMQS1kQuK2wBmqFERAw3`</summary>

````text
1	# n=500 更新清单
2	
3	> 论文：Phase-Modulated Compound Sparsity (EMNLP 2026 ARR)
4	> 当前数据：n=50 MATH-500（DeepSeek n=49, Qwen n=46, LLaMA n=49）
5	> 目标数据：n=500 MATH-500
6	> 生成日期：2026-05-14
7	> 硬约束：D054 (median only), D059 (within-imp d_z only), D015 (emergent interaction framing), D056 (C5b→future work), D060 (LLaMA→suggests)
8	
9	---
10	
11	## 统计汇总
12	
13	| 分类 | 数量 |
14	|------|------|
15	| data_update（数字替换） | 48 |
16	| figure_update（重新生成） | 5 |
17	| claim_update（措辞调整） | 8 |
18	| structural（结构变动） | 3 |
19	| constraint_check（硬约束合规） | 6 |
20	| **总计** | **70** |
21	
22	---
23	
24	## §0 Abstract (abstract.tex)
25	
26	### A01 [data_update] Line 6 — 样本量
27	- **当前**: `50 MATH-500 problems`
28	- **替换**: `500 MATH-500 problems`
29	- **依赖**: n=500 DeepSeek/Qwen 有效样本量（扣除 degenerate phase 后实际 n）
30	
31	### A02 [data_update] Line 7 — DeepSeek 主结果
32	- **当前**: `median Interaction Index difference between low-sparsity and high-sparsity reasoning phases increases monotonically from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$`
33	- **替换**: n=500 DeepSeek importance Δ 值（4 个 sparsity level）
34	- **来源**: experiment_summary_table.json → median_diff
35	
36	### A03 [data_update] Line 7 — DeepSeek d_z 和 p
37	- **当前**: `paired Cohen's $d_z$ growing from $0.44$ (small) to $0.80$ (large); Bonferroni-corrected permutation tests yield $p < 0.005$`
38	- **替换**: n=500 DeepSeek within-importance paired d_z（4 值）+ 新 p-values
39	- **注意**: D059 — 此处 d_z 是 within-importance (low−high)，合规 ✓
40	
41	### A04 [data_update] Line 8 — Random baseline 统计
42	- **当前**: `Random eviction produces no significant phase modulation in 7/8 conditions; the single exception (Qwen $s{=}0.30$, $p{=}0.012$) shows negligible effect size ($d_z{=}{-}0.04$)`
43	- **替换**: n=500 random 条件的 PASS/FAIL 计数 + 例外条件的 p 和效应量
44	- **注意**: D059 — random 条件不报 d_z，改为 Wilcoxon p + median_diff
45	
46	### A05 [data_update] Line 9 — Crossover 数值
47	- **当前**: `$\widetilde{\mathrm{II}} = 0.032$ vs.\ $0.818$` 和 `$7.196$ vs.\ $1.363$`
48	- **替换**: n=500 s=0.25 crossover 的 4 个 II 中位数
49	
50	### A06 [data_update] Line 10 — Qwen 复现
51	- **当前**: `$d_z \geq 0.55$; Spearman $\rho = 1.0$; gradient permutation $p = 0.043$`
52	- **替换**: n=500 Qwen within-importance d_z + Spearman ρ + permutation p
53	
54	### A07 [data_update] Line 10 — LLaMA 数值
55	- **当前**: `$d_z$ ($0.19 \to 0.34$; $s{=}0.30$ Wilcoxon $p_{\text{Bonf}} = 0.029$)`
56	- **替换**: LLaMA 数据未变（n=49），但需确认是否也跑 n=500
57	- **注意**: D059 违规 ⚠️ — 此 d_z 是 imp-vs-rand，应改为 Wilcoxon p + median_diff
58	- **注意**: D060 — 当前用 "suggests"，合规 ✓
59	
60	### A08 [data_update] Line 10 — LLaMA 倍数比
61	- **当前**: `${\sim}$1/40 the absolute magnitude`
62	- **替换**: 用 n=500 DeepSeek 数据重算 LLaMA/DeepSeek 比值
63	
64	---
65	
66	## §1 Introduction (introduction.tex)
67	
68	### I01 [data_update] Line 14 — DeepSeek 主结果
69	- **当前**: `$0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$ ($d_z$: $0.44 \to 0.80$; Bonferroni-corrected $p < 0.005$)`
70	- **替换**: 与 A02/A03 同步
71	
72	### I02 [data_update] Line 15 — Qwen d_z
73	- **当前**: `$d_z \geq 0.55$`
74	- **替换**: n=500 Qwen within-importance d_z 下界
75	
76	### I03 [data_update] Line 15 — LLaMA 倍数
77	- **当前**: `$\sim$1/40 the magnitude`
78	- **替换**: 与 A08 同步
79	
80	### I04 [data_update] Line 16 — Random PASS/FAIL 统计
81	- **当前**: `7/8 conditions non-significant`
82	- **替换**: n=500 random PASS/FAIL 计数
83	
84	---
85	
86	## §4 Experimental Setup (methodology.tex)
87	
88	### M01 [data_update] Line 10 — 样本量
89	- **当前**: `50 problems stratified from MATH-500`
90	- **替换**: `500 problems from MATH-500`（去掉 "stratified"，500 ≈ 全集）
91	
92	### M02 [data_update] Line 18 — 偏度统计
93	- **当前**: `mean/median ratios up to 43:1`
94	- **替换**: n=500 的 mean/median ratio
95	- **注意**: D054 — 此处引用 mean/median 比作为选择 median 的理由，合规 ✓
96	
97	### M03 [data_update] Line 22 — p-value 总结
98	- **当前**: `All tests yield $p_{\text{Bonf}} < 0.005$ at every sparsity level.`
99	- **替换**: n=500 permutation test 结果
100	
101	---
102	
103	## §5 Results (results.tex)
104	
105	### R01 [data_update] Lines 8 — §5.1 aggregate Δ
106	- **当前**: `$\Delta$ increases from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$---a $37{\times}$ amplification`
107	- **替换**: n=500 Δ 值 + 新倍数
108	
109	### R02 [data_update] Line 8 — Random Δ 范围
110	- **当前**: `$-0.02$ to $1.54$`
111	- **替换**: n=500 random Δ 范围
112	
113	### R03 [data_update] Line 13 — Table 1 标题样本量
114	- **当前**: `$n{=}50$ MATH-500 problems`
115	- **替换**: `$n{=}500$`（或实际有效 n）
116	
117	### R04 [data_update] Lines 19-20 — Table 1 (aggregate-ii) 全部数据
118	- **当前**:
119	  ```
120	  Importance & 0.39 & 1.48 & 7.16 & 14.59
121	  Random     & 0.01 & −0.02 & 0.54 & 1.54
122	  ```
123	- **替换**: n=500 median Δ 值（8 个数字）
124	
125	### R05 [data_update] Line 29 — §5.2 severity gradient G
126	- **当前**: `$69{\times}$ at $s{=}0.15$ to $274{\times}$ at $s{=}0.30$`
127	- **替换**: n=500 G 值
128	- **注意**: D031/D033 决定 gradient ratio 仅作辅助描述；确认 n=500 是否仍报 G
129	
130	### R06 [data_update] Line 29 — high-phase II 范围
131	- **当前**: `$\widetilde{\mathrm{II}}_{\textit{high}}$ ranges from $0.006$ to $0.053$`
132	- **替换**: n=500 high-phase median II 范围
133	
134	### R07 [data_update] Line 29 — Random G 范围
135	- **当前**: `$G \approx 0.9$--$1.7{\times}$`
136	- **替换**: n=500 random G 范围
137	
138	### R08 [data_update] Lines 34, 40-50 — Table 2 (main-results) 全部数据
139	- **当前**: "50 problems" + 24 个数据单元格（6列×4组）
140	- **替换**: n=500 全部 per-phase median II + Δ + G（24 个数字 + caption 中 n）
141	
142	### R09 [figure_update] Lines 55-60 — Figure 1 (fig1_dose_response.pdf)
143	- **当前**: 基于 n=50 bf16 数据
144	- **操作**: 用 n=500 数据重新生成 fig1_dose_response.pdf
145	- **注意**: caption 中 "$69{\times}$ to $274{\times}$" 需同步更新
146	
147	### R10 [data_update] Line 66 — §5.3 Crossover 数值
148	- **当前**: `$0.032$ vs.\ $0.818$`, `$7.196$ vs.\ $1.363$---a $5.3{\times}$ reversal`
149	- **替换**: n=500 s=0.25 crossover 值 + 倍数
150	
151	### R11 [data_update] Line 71 — §5.4 Qwen Δ 范围
152	- **当前**: `$\Delta$ increases from $0.04$ at $s{=}0.15$ to $2.94$ at $s{=}0.30$`
153	- **替换**: n=500 Qwen Δ 值
154	
155	### R12 [data_update] Line 71 — DeepSeek/Qwen 倍数比
156	- **当前**: `${\sim}1/5$ the magnitude`
157	- **替换**: n=500 Qwen/DeepSeek 比值
158	
159	### R13 [data_update] Line 71 — Qwen 统计
160	- **当前**: `Spearman $\rho = 1.0$; gradient permutation $p = 0.043$`
161	- **替换**: n=500 Qwen 对应统计量
162	
163	### R14 [data_update] Line 71 — Qwen s015 d_z
164	- **当前**: `$d_z{=}0.28$, CI includes zero`
165	- **替换**: n=500 Qwen s015 d_z + CI
166	- **注意**: D052 预注册——若 s015 仍 ns，叙事改为 "emerges above threshold"
167	
168	### R15 [data_update] Line 71 — Qwen d_z 下界
169	- **当前**: `$d_z \geq 0.55$`
170	- **替换**: n=500 Qwen s≥0.20 d_z 值
171	
172	### R16 [data_update] Line 77 — §5.5 LLaMA 样本量
173	- **当前**: `$n{=}49$ paired problems`
174	- **替换**: 确认 LLaMA 是否也跑 n=500；若仍 n=49 则保留
175	
176	### R17 [constraint_check] Lines 79 — §5.5 LLaMA d_z（D059 违规 ⚠️）
177	- **当前**: `monotonically increasing paired $d_z$ ($0.19 \to 0.26 \to 0.29 \to 0.34$)`
178	- **问题**: 此 d_z 是 imp-vs-rand paired Cohen's d，D059 禁止报告
179	- **修改**: 删除 imp-vs-rand d_z，改为 Wilcoxon p + median_diff
180	
181	### R18 [constraint_check] Lines 79 — LLaMA within-importance d_z
182	- **当前**: `within-strategy phase gradient $d_z$ (low $-$ high) is consistently large at all sparsity levels ($d_z \in [1.00, 1.12]$)`
183	- **状态**: 合规 ✓（within-importance），数值可能需更新（若 LLaMA 重跑）
184	
185	### R19 [constraint_check] Lines 79 — LLaMA random d_z
186	- **当前**: `$d_z \in [0.35, 0.45]$`
187	- **问题**: D059 — random 不报 d_z
188	- **修改**: 改为 "random eviction also shows non-trivial phase gradient" + Wilcoxon p
189	
190	### R20 [data_update] Lines 81 — LLaMA 倍数比
191	- **当前**: `${\sim}40{\times}$ smaller than DeepSeek and ${\sim}7{\times}$ smaller than Qwen`
192	- **替换**: 用 n=500 DeepSeek/Qwen 数据重算比值
193	
194	### R21 [structural] Lines 83-98 — Table 3 (llama-cross-arch) 重构
195	- **当前**: d_z 列报告 imp-vs-rand Cohen's d
196	- **问题**: D059 违规 — 整列需要替换
197	- **修改**: d_z 列改为 within-importance d_z（或删除 d_z 列，改为 Wilcoxon p + median_diff）
198	- **数据**: 若 LLaMA 不重跑，数值不变但列定义需改
199	
200	### R22 [data_update] Lines 92-95 — Table 3 数据行
201	- **当前**: 4 行 (d_z, Δ̃ [CI], p_Bonf)
202	- **替换**: 若 LLaMA 重跑则全部更新；若不重跑，仅结构变动
203	
204	### R23 [data_update] Line 104 — §5.6 permutation test 结果
205	- **当前**: `$p_{\text{Bonf}} < 0.005$`, `$0.37$ at $s{=}0.15$ to $9.85$ at $s{=}0.30$`
206	- **替换**: n=500 permutation test 统计
207	
208	### R24 [data_update] Lines 106 — DeepSeek d_z 范围
209	- **当前**: `$d_z{=}0.44$ (small) to $d_z{=}0.80$ (large)`
210	- **替换**: n=500 DeepSeek within-importance d_z
211	
212	### R25 [data_update] Lines 106 — Qwen d_z
213	- **当前**: `$d_z{=}0.28$, CI includes zero`, `$d_z \geq 0.55$`, `$d_z{=}0.89$/$1.02$ vs.\ $0.68$/$0.80$`
214	- **替换**: n=500 Qwen d_z 值
215	
216	### R26 [data_update] Lines 113-123 — Table 4 (cohens-d) 全部数据
217	- **当前**: 4 行 × (DS d_z, Δ̃ [CI], QW d_z, Δ̃ [CI])
218	- **替换**: n=500 paired d_z + bootstrap Δ̃ + CI（16 个数字）
219	
220	---
221	
222	## §6 Analysis (analysis.tex)
223	
224	### AN01 [data_update] Line 4 — Gini 系数范围
225	- **当前**: `$0.030$--$0.081$ (DeepSeek) and $0.010$--$0.020$ (Qwen)`
226	- **替换**: n=500 Gini Δ 范围（若 C4 entropy 分析基于 n=500 重跑）
227	- **注意**: C4 已降为 supporting analysis (D045/D046)，数值可能不变
228	
229	### AN02 [data_update] Line 6 — DeepSeek entropy Δ 范围
230	- **当前**: `$\Delta\mathcal{H} \in [-0.047, -0.040]$`
231	- **替换**: 若 C4 基于 n=500 重跑则更新
232	
233	### AN03 [data_update] Line 6 — Qwen entropy 反转
234	- **当前**: `$s{=}0.25$ ($\Delta\mathcal{H} = +0.045$)`
235	- **替换**: 若 C4 基于 n=500 重跑则更新
236	
237	---
238	
239	## §7 Discussion (discussion.tex)
240	
241	### D01 [data_update] Line 5 — Gradient 范围
242	- **当前**: `$69$--$274{\times}$`
243	- **替换**: 与 R05 同步
244	
245	### D02 [data_update] Line 5 — Crossover 数值
246	- **当前**: `$\widetilde{\mathrm{II}} = 0.032$ vs.\ $0.818$` 和 `$7.196$ vs.\ $1.363$`
247	- **替换**: 与 R10 同步
248	
249	### D03 [data_update] Line 11 — LLaMA 倍数
250	- **当前**: `${\sim}40{\times}$ smaller than DeepSeek, ${\sim}7{\times}$ smaller than Qwen`
251	- **替换**: 与 R20 同步
252	
253	### D04 [constraint_check] Line 11 — LLaMA d_z（D059 违规 ⚠️）
254	- **当前**: `within-strategy phase gradient $d_z \geq 1.0$`
255	- **状态**: 这是 within-importance d_z，合规 ✓
256	
257	### D05 [constraint_check] Line 11 — LLaMA random d_z（D059 违规 ⚠️）
258	- **当前**: `$d_z \in [0.35, 0.45]$`
259	- **修改**: 与 R19 同步——删除 d_z，改为定性描述 + Wilcoxon p
260	
261	### D06 [claim_update] Line 11 — LLaMA 语言（D060）
262	- **当前**: `provides partial support for the qualitative pattern`
263	- **状态**: 合规 ✓（"partial support"）
264	
265	---
266	
267	## §8 Conclusion (conclusion.tex)
268	
269	### C01 [data_update] Line 4 — Gradient 范围
270	- **当前**: `$69{\times}$ to $274{\times}$`
271	- **替换**: 与 R05 同步
272	
273	### C02 [data_update] Line 4 — d_z 范围
274	- **当前**: `$d_z$: $0.44 \to 0.80$`
275	- **替换**: 与 R24 同步
276	
277	### C03 [data_update] Line 4 — Random PASS/FAIL
278	- **当前**: `7/8 conditions non-significant`
279	- **替换**: 与 I04 同步
280	
281	### C04 [data_update] Line 4 — Qwen d_z
282	- **当前**: `$d_z \geq 0.55$`
283	- **替换**: 与 R15 同步
284	
285	### C05 [data_update] Line 4 — LLaMA 倍数
286	- **当前**: `$\sim$1/40 the magnitude`
287	- **替换**: 与 A08 同步
288	
289	### C06 [constraint_check] — C5b future work（D056）
290	- **当前**: `These findings motivate phase-aware sparsity allocation for reasoning model deployment.`
291	- **状态**: 合规 ✓ — 作为 motivation 而非 contribution claim
292	
293	---
294	
295	## Limitations (limitations.tex)
296	
297	### L01 [data_update] Line 1 — 架构描述
298	- **状态**: 无直接 n=50 数据，无需数字更新
299	
300	### L02 [claim_update] Line 4 — 样本量描述
301	- **当前**: 未直接提及 n=50，但 "exclusively on MATH-500" 成立
302	- **替换**: n=500 后可加 "using 500 problems from MATH-500"
303	
304	---
305	
306	## Appendix A (appendix.tex) — Formulation + Multiplicative Null
307	
308	### AP01 [data_update] Line 38 — Multiplicative null G 范围
309	- **当前**: `$G_{\times} = 58$--$241{\times}$`
310	- **替换**: n=500 multiplicative null G 值（需重算）
311	
312	---
313	
314	## Appendix B (appendix_results.tex) — Cross-Model Summary
315	
316	### AR01 [data_update] Line 7 — Per-problem concordance
317	- **当前**: `mean $\rho = -0.11$, $p = 0.926$`
318	- **替换**: n=500 cross-model concordance（Spearman ρ + p）
319	
320	### AR02 [data_update] Line 10 — Random PASS/FAIL 模式
321	- **当前**: `3/4 FAIL`, `4/4 FAIL`
322	- **替换**: n=500 random PASS/FAIL 计数
323	
324	### AR03 [data_update] Line 10 — Qwen random s030 例外
325	- **当前**: `$p = 0.012$`, `$d_z = -0.04$`
326	- **替换**: n=500 结果
327	- **注意**: D059 — 不报 d_z，改为 Wilcoxon p + median_diff
328	
329	---
330	
331	## Appendix C (appendix_moved.tex) — Crossover + Cross-Model + Permutation + Analysis
332	
333	### AM01 [data_update] Line 11 — Crossover 全部数值
334	- **当前**: `$0.032$ vs.\ $0.818$`, `$7.196$ vs.\ $1.363$`, `$5.3{\times}$`, `$3.9{\times}$, $5.4{\times}$, $5.3{\times}$, $3.6{\times}$`
335	- **替换**: n=500 crossover 值（所有 4 个 sparsity level 的 reversal magnitude）
336	
337	### AM02 [figure_update] Lines 13-18 — Figure 3 (fig3_crossover.pdf)
338	- **操作**: 用 n=500 数据重新生成
339	- **caption**: `$5.3{\times}$` 需同步更新
340	
341	### AM03 [data_update] Line 26 — Qwen 排除数
342	- **当前**: `Four of the 50 problems are excluded`, `$n{=}46$`, `$n{=}49$`
343	- **替换**: n=500 的 DeepSeek/Qwen 有效 n
344	
345	### AM04 [data_update] Lines 39-40 — Table (cross-model) 全部数据
346	- **当前**: DeepSeek [0.39, 1.48, 7.16, 14.59], Qwen [0.04, 0.23, 1.27, 2.94]
347	- **替换**: n=500 median Δ 值（8 个数字）
348	
349	### AM05 [figure_update] Lines 45-50 — Figure 5 (fig5_crossmodel.pdf)
350	- **操作**: 用 n=500 数据重新生成
351	- **caption**: "one-fifth" 比例需同步更新
352	
353	### AM06 [data_update] Lines 52-53 — Per-problem concordance（重复 AR01）
354	- **替换**: 与 AR01 同步
355	
356	### AM07 [data_update] Lines 55-56 — Random PASS/FAIL（重复 AR02/AR03）
357	- **替换**: 与 AR02/AR03 同步
358	
359	### AM08 [data_update] Lines 62, 73 — Permutation test 样本量
360	- **当前**: `$n{=}49$`
361	- **替换**: n=500 有效 n
362	
363	### AM09 [data_update] Lines 68 — CI lower bounds
364	- **当前**: `$0.19 \to 0.69 \to 1.66 \to 6.70$`
365	- **替换**: n=500 CI lower bounds
366	
367	### AM10 [data_update] Lines 79-82 — Table (permutation) 全部数据
368	- **当前**: 4 行 (observed Δ̃, 95% CI, p_Bonf)
369	- **替换**: n=500 permutation test 结果（12 个数字）
370	
371	### AM11 [figure_update] Lines 87-92 — Figure 4 (fig4_bootstrap.pdf)
372	- **操作**: 用 n=500 数据重新生成
373	
374	### AM12 [data_update] Lines 111-122 — Table (discrimination-metrics-full) 全部数据
375	- **当前**: 8 行 (ΔGini, ΔCV)
376	- **替换**: 若 C4 分析基于 n=500 重跑则更新（16 个数字）
377	
378	### AM13 [data_update] Lines 137-139 — Entropy delta 描述
379	- **当前**: DeepSeek `$\Delta\mathcal{H} \in [-0.047, -0.040]$`, Qwen s025 `$+0.045$`
380	- **替换**: 若 C4 分析基于 n=500 重跑则更新
381	
382	### AM14 [data_update] Lines 149-162 — Table (entropy-deltas) 全部数据
383	- **当前**: 8 行
384	- **替换**: 若 C4 分析基于 n=500 重跑则更新
385	
386	---
387	
388	## Appendix D (appendix_disc_analysis.tex) — Extended Discussion + Limitations
389	
390	### AD01 [data_update] Line 4 — Random Gini 范围
391	- **当前**: `$-0.031$ to $-0.073$; Qwen: $-0.019$ to $-0.045$`
392	- **替换**: 若 C4 基于 n=500 重跑则更新
393	
394	### AD02 [data_update] Line 11 — High-phase II 上限
395	- **当前**: `$\widetilde{\mathrm{II}}_{\text{high}} < 0.06$ at $s \leq 0.30$`; `$s = 0.35$, high-phase II rises to $0.105$`
396	- **替换**: n=500 high-phase median II 值
397	
398	### AD03 [data_update] Line 14 — Random 7/8 统计
399	- **当前**: `7/8`, `$p{=}0.012$`, `$d_z{=}{-}0.04$`
400	- **替换**: 与 A04 同步
401	- **注意**: D059 — 不报 d_z
402	
403	### AD04 [data_update] Lines 44-47 — 统计范围详情
404	- **当前**: `$n{=}49$ ... $n{=}46$`, mean/median ratio `${\sim}1.6{:}1$`, permutation CI 值
405	- **替换**: n=500 统计
406	
407	### AD05 [data_update] Line 49 — Qwen random s030 例外
408	- **当前**: `$p{=}0.012$`, `$d_z{=}{-}0.04$`
409	- **替换**: 与 AR03 同步
410	- **注意**: D059 — 不报 d_z
411	
412	### AD06 [data_update] Lines 53-57 — Growth rate 描述
413	- **当前**: `$3.8{\times} \to 4.8{\times} \to 2.0{\times}$`
414	- **替换**: n=500 Δ growth rate
415	
416	---
417	
418	## 图表重新生成清单
419	
420	| # | 文件名 | 数据来源 | 引用位置 |
421	|---|--------|----------|----------|
422	| F1 | fig1_dose_response.pdf | n=500 DeepSeek imp+rand G vs s | results.tex:57, caption:58 |
423	| F2 | fig3_crossover.pdf | n=500 DeepSeek s=0.25 crossover | appendix_moved.tex:15 |
424	| F3 | fig4_bootstrap.pdf | n=500 permutation test forest plot | appendix_moved.tex:89 |
425	| F4 | fig5_crossmodel.pdf | n=500 DeepSeek+Qwen Δ comparison | appendix_moved.tex:47 |
426	| F5 | (unnamed hero figure if separate) | 确认是否与 fig1 相同 | results.tex:57 |
427	
428	---
429	
430	## 硬约束合规审查
431	
432	### HC01 [D054] II 只报 median + median bootstrap CI ✅
433	- abstract/results/discussion 全文使用 median ($\widetilde{\mathrm{II}}$)
434	- methodology.tex:18 提及 mean/median ratio 作为选择 median 的理由 ✓
435	- **注意**: n=500 更新时确认所有新数字均为 median
436	
437	### HC02 [D059] d_z 只报 within-importance ⚠️ 6 处违规
438	| 位置 | 当前内容 | 问题 |
439	|------|---------|------|
440	| abstract.tex:8 | random `$d_z{=}{-}0.04$` | imp-vs-rand d_z |
441	| results.tex:79 | LLaMA `$d_z$ ($0.19 \to 0.34$)` | imp-vs-rand d_z |
442	| results.tex:79 | random `$d_z \in [0.35, 0.45]$` | random d_z |
443	| results.tex:88-97 | Table 3 d_z 列 | imp-vs-rand d_z |
444	| discussion.tex:11 | `$d_z \in [0.35, 0.45]$` | random d_z |
445	| appendix_disc_analysis.tex:14,49 | `$d_z{=}{-}0.04$` | random d_z |
446	
447	**修改方案**: 所有 imp-vs-rand 和 random d_z 替换为 Wilcoxon p + median_diff；Table 3 d_z 列替换为 within-importance d_z 或移除
448	
449	### HC03 [D015] Framing: emergent phase-strategy interaction ✅
450	- abstract.tex:4 使用 "emergent phase-strategy interaction" ✓
451	- 全文无 "importance is broken" 叙事 ✓
452	
453	### HC04 [D056] C5b 已降为 §8 future work ✅
454	- discussion.tex:8 讨论 phase-aware budget 作为 implication（未 claim 实现）✓
455	- conclusion.tex:5 "motivate phase-aware sparsity allocation" ✓
456	- **注意**: D056 确认 c5b_pilot gate_failed (oracle 18% < 30%)，论文不应 claim C5b 成功
457	
458	### HC05 [D060] C8 LLaMA 用 suggests/partial support ✅
459	- abstract.tex:10 "suggests cross-architecture generalization" ✓
460	- discussion.tex:11 "provides partial support" ✓
461	- conclusion.tex:4 "partially extends" ✓
462	- results.tex:77-81 "The qualitative pattern replicates" — **borderline**，建议改为 "The qualitative pattern is directionally consistent"
463	
464	### HC06 [硬约束 #6] Random 也有正 II，区分信号是 gradient ✅
465	- results.tex Table 2 显示 random 有正 II ✓
466	- 叙事正确区分："compound severity depends qualitatively on eviction strategy" ✓
467	- **注意**: n=500 random 数据可能有不同 pattern，需重新验证此叙事
468	
469	---
470	
471	## 按 Section 分布
472	
473	| Section | 更新点数 |
474	|---------|---------|
475	| Abstract | 8 |
476	| Introduction | 4 |
477	| Methodology | 3 |
478	| Results | 26 |
479	| Analysis | 3 |
480	| Discussion | 6 |
481	| Conclusion | 6 |
482	| Limitations | 2 |
483	| Appendix (formulation) | 1 |
484	| Appendix (results summary) | 3 |
485	| Appendix (moved content) | 14 |
486	| Appendix (disc+limitations) | 6 |
487	| **Total** | **82** (含重复引用) |
488	| **Unique** | **~70** |
489	
490	---
491	
492	## 高风险点（可能需要改叙事）
493	
494	### RISK-1: Qwen s015 是否仍然 non-significant
495	- D052 预注册：若 n=500 Qwen s015 仍 ns，叙事改为 "compound effect emerges above a model-dependent threshold"
496	- D061 已确认 n=500 下 Qwen s015 显著 (p<0.0001)——**如果最终数据确认，此风险解除**
497	- 影响范围：abstract, introduction, results §5.4, §5.6, conclusion
498	
499	### RISK-2: Random PASS/FAIL 模式可能变化
500	- n=50 下 7/8 FAIL（Qwen s030 borderline PASS d≈0）
501	- n=500 功效更高，可能检测到更多 borderline 显著
502	- 影响范围：需重新评估 "no significant phase modulation" 叙事
503	- D059 保护：不报 random d_z，用 Wilcoxon p + median_diff 更 robust
504	
505	### RISK-3: LLaMA 数据是否跑 n=500
506	- 当前 LLaMA 仅 n=49
507	- 若不重跑：DeepSeek/Qwen 倍数比需重算（分母变了）
508	- 若重跑：全部 LLaMA 数据需更新
509	
510	### RISK-4: D059 Table 3 重构
511	- Table 3 (llama-cross-arch) 的核心组织方式围绕 imp-vs-rand d_z
512	- 删除 d_z 列后需要替代结构，可能影响 §5.5 整段叙事
513	
514	### RISK-5: Crossover pattern 在 n=500 是否稳定
515	- crossover 是论文的一个 key finding
516	- n=500 的 crossover 倍数和位置可能变化
517	- 影响范围：abstract, results §5.3, discussion, appendix
518	
519	### RISK-6: C4 entropy 分析是否需要基于 n=500 重跑
520	- 当前 C4 降级为 supporting analysis (D045/D046)
521	- 若不重跑：analysis.tex 和 appendix 表格保留 n=50 数据，需标注
522	- 若重跑：AN01-AN03, AM12-AM14, AD01 全部更新
523	
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_014G9a6m4Szoqsuk1hAsUCbW",
  "session_id": "10233ec7-5d03-448a-9224-b6173ea0cbe8",
  "uuid": "01b7eed7-4230-4d76-a041-258b00639829"
}
```

</details>

---

### System

_source line 11_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "acde2f40d7c479977",
  "tool_use_id": "toolu_014G9a6m4Szoqsuk1hAsUCbW",
  "description": "Reading artifacts/_project/paper_framing.md",
  "usage": {
    "total_tokens": 17941,
    "tool_uses": 2,
    "duration_ms": 2262
  },
  "last_tool_name": "Read",
  "uuid": "f3bf9050-2f87-4282-b862-006ab777bdb1",
  "session_id": "10233ec7-5d03-448a-9224-b6173ea0cbe8"
}
```

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — Read · `toolu_011WdWrG6vrhFLSnNV3uAazt`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_014G9a6m4Szoqsuk1hAsUCbW",
  "session_id": "10233ec7-5d03-448a-9224-b6173ea0cbe8",
  "uuid": "aeaf6f86-0500-4656-838e-eb91c825bff3",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01C7xoST66UBjZWsSLoNWgcV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17926,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17926,
        "ephemeral_1h_input_tokens": 0
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

_source line 13 · 2026-05-14T21:49:10.581Z_

<details><summary>↩ Tool result · reported error · `toolu_011WdWrG6vrhFLSnNV3uAazt`</summary>

```text
File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_014G9a6m4Szoqsuk1hAsUCbW",
  "session_id": "10233ec7-5d03-448a-9224-b6173ea0cbe8",
  "uuid": "ff4bcfa6-9ad3-407b-8285-e67a2593df7b",
  "tool_use_result": "Error: File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse."
}
```

</details>

---

### System

_source line 14_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "acde2f40d7c479977",
  "tool_use_id": "toolu_014G9a6m4Szoqsuk1hAsUCbW",
  "description": "Finding /home/ubuntu/.agent-ml-research-idea_gen_0509_11/…",
  "usage": {
    "total_tokens": 17945,
    "tool_uses": 3,
    "duration_ms": 2450
  },
  "last_tool_name": "Glob",
  "uuid": "523c9c91-b060-47e4-b4b7-14f68fd5332d",
  "session_id": "10233ec7-5d03-448a-9224-b6173ea0cbe8"
}
```

---

### Tool call

_source line 15_

<details open><summary>🔧 Tool call — Glob · `toolu_0196sufrxTXduTZeeZXgcaRK`</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_014G9a6m4Szoqsuk1hAsUCbW",
  "session_id": "10233ec7-5d03-448a-9224-b6173ea0cbe8",
  "uuid": "0faa93d2-7bcd-45d7-830b-4d8f3b2f61b9",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01C7xoST66UBjZWsSLoNWgcV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17926,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17926,
        "ephemeral_1h_input_tokens": 0
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

_source line 16 · 2026-05-14T21:49:10.801Z_

<details><summary>↩ Tool result · `toolu_0196sufrxTXduTZeeZXgcaRK`</summary>

```text
artifacts/_project/paper/methodology.tex
artifacts/_project/paper/appendix_results.tex
artifacts/_project/paper/appendix.tex
artifacts/_project/paper/background.tex
artifacts/_project/paper/analysis.tex
artifacts/_project/paper/main.tex
artifacts/_project/paper/appendix_moved.tex
artifacts/_project/paper/abstract.tex
artifacts/_project/paper/discussion.tex
artifacts/_project/paper/results.tex
artifacts/_project/paper/conclusion.tex
artifacts/_project/paper/appendix_disc_analysis.tex
artifacts/_project/paper/introduction.tex
artifacts/_project/paper/limitations.tex
artifacts/_project/paper/related_work.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_014G9a6m4Szoqsuk1hAsUCbW",
  "session_id": "10233ec7-5d03-448a-9224-b6173ea0cbe8",
  "uuid": "184b0816-8b4f-47ce-8a1f-2a65da26913c"
}
```

</details>

---

### System

_source line 17_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "acde2f40d7c479977",
  "tool_use_id": "toolu_014G9a6m4Szoqsuk1hAsUCbW",
  "status": "completed",
  "output_file": "",
  "summary": "Read existing checklist and project context",
  "usage": {
    "total_tokens": 30042,
    "tool_uses": 3,
    "duration_ms": 12336
  },
  "uuid": "cf1b6efe-af4c-45fd-a32e-80639aed2c45",
  "session_id": "10233ec7-5d03-448a-9224-b6173ea0cbe8"
}
```

---

### Tool result

_source line 18 · 2026-05-14T21:49:20.632Z_

<details><summary>↩ Tool result · `toolu_014G9a6m4Szoqsuk1hAsUCbW`</summary>

```text
## Summary

I've retrieved the requested files and information. Here are the results:

### 1. Full Content of n500_update_checklist.md

The file contains a comprehensive Chinese-language checklist for updating a research paper titled "Phase-Modulated Compound Sparsity" (EMNLP 2026 ARR submission) from n=50 to n=500 samples. It includes:

**Key Statistics:**
- 70 total update points across the paper
- 48 data updates, 5 figure regenerations, 8 claim/wording updates, 3 structural changes, 6 constraint checks

**Sections with Updates Required:**
- Abstract (8 updates)
- Introduction (4 updates)
- Methodology (3 updates)
- Results (26 updates)
- Analysis (3 updates)
- Discussion (6 updates)
- Conclusion (6 updates)
- Multiple Appendices (24 updates total)

**Key Constraints Being Checked:**
- D054: Median-only reporting for Interaction Index (II)
- D059: d_z statistics only for within-importance comparisons (6 compliance violations identified)
- D015: Emergent interaction framing
- D056: C5b relegated to future work
- D060: LLaMA cross-architecture results use cautious language ("suggests")

**High-Risk Items:**
- Qwen s=0.15 significance threshold (D052)
- Random baseline PASS/FAIL pattern changes
- LLaMA data not yet run at n=500
- D059 Table 3 restructuring
- Crossover pattern stability
- C4 entropy analysis recomputation needs

**Figures Requiring Regeneration:**
- fig1_dose_response.pdf
- fig3_crossover.pdf
- fig4_bootstrap.pdf
- fig5_crossmodel.pdf

### 2. Paper_framing.md

This file does not exist at the path `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper_framing.md`

### 3. .tex Files in Paper Directory

The following 15 .tex files exist in `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/`:

1. abstract.tex
2. analysis.tex
3. appendix.tex
4. appendix_disc_analysis.tex
5. appendix_moved.tex
6. appendix_results.tex
7. background.tex
8. conclusion.tex
9. discussion.tex
10. introduction.tex
11. limitations.tex
12. main.tex
13. methodology.tex
14. related_work.tex
15. results.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10233ec7-5d03-448a-9224-b6173ea0cbe8",
  "uuid": "fd89a971-c75b-4c6f-81d4-6d23fbcf4b37",
  "tool_use_result": {
    "status": "completed",
    "prompt": "Read the following files and return their full contents:\n1. /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/n500_update_checklist.md\n2. /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper_framing.md (if exists)\n\nAlso list all .tex files in /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/ and report their names.\n\nReport everything verbatim — I need the full content of each file.",
    "agentId": "acde2f40d7c479977",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "## Summary\n\nI've retrieved the requested files and information. Here are the results:\n\n### 1. Full Content of n500_update_checklist.md\n\nThe file contains a comprehensive Chinese-language checklist for updating a research paper titled \"Phase-Modulated Compound Sparsity\" (EMNLP 2026 ARR submission) from n=50 to n=500 samples. It includes:\n\n**Key Statistics:**\n- 70 total update points across the paper\n- 48 data updates, 5 figure regenerations, 8 claim/wording updates, 3 structural changes, 6 constraint checks\n\n**Sections with Updates Required:**\n- Abstract (8 updates)\n- Introduction (4 updates)\n- Methodology (3 updates)\n- Results (26 updates)\n- Analysis (3 updates)\n- Discussion (6 updates)\n- Conclusion (6 updates)\n- Multiple Appendices (24 updates total)\n\n**Key Constraints Being Checked:**\n- D054: Median-only reporting for Interaction Index (II)\n- D059: d_z statistics only for within-importance comparisons (6 compliance violations identified)\n- D015: Emergent interaction framing\n- D056: C5b relegated to future work\n- D060: LLaMA cross-architecture results use cautious language (\"suggests\")\n\n**High-Risk Items:**\n- Qwen s=0.15 significance threshold (D052)\n- Random baseline PASS/FAIL pattern changes\n- LLaMA data not yet run at n=500\n- D059 Table 3 restructuring\n- Crossover pattern stability\n- C4 entropy analysis recomputation needs\n\n**Figures Requiring Regeneration:**\n- fig1_dose_response.pdf\n- fig3_crossover.pdf\n- fig4_bootstrap.pdf\n- fig5_crossmodel.pdf\n\n### 2. Paper_framing.md\n\nThis file does not exist at the path `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper_framing.md`\n\n### 3. .tex Files in Paper Directory\n\nThe following 15 .tex files exist in `/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/`:\n\n1. abstract.tex\n2. analysis.tex\n3. appendix.tex\n4. appendix_disc_analysis.tex\n5. appendix_moved.tex\n6. appendix_results.tex\n7. background.tex\n8. conclusion.tex\n9. discussion.tex\n10. introduction.tex\n11. limitations.tex\n12. main.tex\n13. methodology.tex\n14. related_work.tex\n15. results.tex"
      }
    ],
    "totalDurationMs": 12345,
    "totalTokens": 30692,
    "totalToolUseCount": 3,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 12092,
      "cache_read_input_tokens": 17926,
      "output_tokens": 667,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 12092
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 667,
          "cache_read_input_tokens": 17926,
          "cache_creation_input_tokens": 12092,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 12092,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 2,
      "searchCount": 1,
      "bashCount": 0,
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

### Assistant

_source line 19_

Now I'll read all .tex files in parallel to find precise line numbers for each update point.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10233ec7-5d03-448a-9224-b6173ea0cbe8",
  "uuid": "8b8c341d-bffb-4b2b-82aa-a979ef43b468",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KbrgPnqywm3btXbv2qV1P3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 968,
      "cache_read_input_tokens": 23930,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 968
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

_source line 20_

<details open><summary>🔧 Tool call — Read · `toolu_01GT9a4BhqV6b5hEtzQnsVdt`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10233ec7-5d03-448a-9224-b6173ea0cbe8",
  "uuid": "987269db-9c52-413d-ae58-241609f35006",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KbrgPnqywm3btXbv2qV1P3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 968,
      "cache_read_input_tokens": 23930,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 968
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

_source line 21 · 2026-05-14T21:49:24.580Z_

<details><summary>↩ Tool result · `toolu_01GT9a4BhqV6b5hEtzQnsVdt`</summary>

```text
1	\begin{abstract}
2	Compound sparsity---simultaneously pruning attention heads and evicting KV cache entries---is essential for efficient LLM inference but produces super-additive quality degradation whose structure is poorly understood.
3	Prior work treats compound interaction magnitude as approximately constant across the generation process.
4	We show that this assumption is wrong: compound sparsity severity is an emergent phase-strategy interaction that varies by over an order of magnitude across reasoning phases.
5	
6	We evaluate compound sparsity on three models---DeepSeek-R1-Distill-Qwen-7B, Qwen2.5-7B-Instruct (both Qwen2ForCausalLM), and DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM)---spanning two architectures, using 50 MATH-500 problems, measuring the Interaction Index---a super-additivity metric---across quantile-segmented reasoning phases at sparsity levels $s \in \{0.15, 0.20, 0.25, 0.30\}$.
7	Under importance-based KV cache eviction, the median Interaction Index difference between low-sparsity and high-sparsity reasoning phases increases monotonically from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$, with paired Cohen's $d_z$ growing from $0.44$ (small) to $0.80$ (large); Bonferroni-corrected permutation tests yield $p < 0.005$ at all four sparsity levels.
8	Random eviction produces no significant phase modulation in 7/8 conditions; the single exception (Qwen $s{=}0.30$, $p{=}0.012$) shows negligible effect size ($d_z{=}{-}0.04$), confirming that the severity gradient is strategy-specific, not an inherent property of compound sparsity.
9	At $s{=}0.25$, a crossover emerges: importance-based eviction outperforms random in high-sparsity phases ($\widetilde{\mathrm{II}} = 0.032$ vs.\ $0.818$) yet underperforms in low-sparsity phases ($\widetilde{\mathrm{II}} = 7.196$ vs.\ $1.363$)---a qualitative reversal in strategy ranking.
10	The pattern replicates on Qwen2.5-7B-Instruct at $s \geq 0.20$ ($d_z \geq 0.55$; Spearman $\rho = 1.0$; gradient permutation $p = 0.043$) and on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM), where monotonically increasing $d_z$ ($0.19 \to 0.34$; $s{=}0.30$ Wilcoxon $p_{\text{Bonf}} = 0.029$) suggests cross-architecture generalization, though at ${\sim}$1/40 the absolute magnitude and with substantially weaker interaction than in Qwen2-based architectures. % exp_id: c3_llama
11	
12	We propose entropy-discrimination collapse as an explanatory mechanism: head pruning flattens cumulative importance scores in phases where attention is already broadly distributed, degrading the discriminative power of importance-based eviction in a phase-dependent manner.
13	These findings challenge the phase-invariance assumption in compound sparsity deployment and motivate phase-aware compression budgets for reasoning models.
14	\end{abstract}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10233ec7-5d03-448a-9224-b6173ea0cbe8",
  "uuid": "5dd99fb4-f64b-4dd4-a67b-acf82970cd3d",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/abstract.tex",
      "content": "\\begin{abstract}\nCompound sparsity---simultaneously pruning attention heads and evicting KV cache entries---is essential for efficient LLM inference but produces super-additive quality degradation whose structure is poorly understood.\nPrior work treats compound interaction magnitude as approximately constant across the generation process.\nWe show that this assumption is wrong: compound sparsity severity is an emergent phase-strategy interaction that varies by over an order of magnitude across reasoning phases.\n\nWe evaluate compound sparsity on three models---DeepSeek-R1-Distill-Qwen-7B, Qwen2.5-7B-Instruct (both Qwen2ForCausalLM), and DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM)---spanning two architectures, using 50 MATH-500 problems, measuring the Interaction Index---a super-additivity metric---across quantile-segmented reasoning phases at sparsity levels $s \\in \\{0.15, 0.20, 0.25, 0.30\\}$.\nUnder importance-based KV cache eviction, the median Interaction Index difference between low-sparsity and high-sparsity reasoning phases increases monotonically from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$, with paired Cohen's $d_z$ growing from $0.44$ (small) to $0.80$ (large); Bonferroni-corrected permutation tests yield $p < 0.005$ at all four sparsity levels.\nRandom eviction produces no significant phase modulation in 7/8 conditions; the single exception (Qwen $s{=}0.30$, $p{=}0.012$) shows negligible effect size ($d_z{=}{-}0.04$), confirming that the severity gradient is strategy-specific, not an inherent property of compound sparsity.\nAt $s{=}0.25$, a crossover emerges: importance-based eviction outperforms random in high-sparsity phases ($\\widetilde{\\mathrm{II}} = 0.032$ vs.\\ $0.818$) yet underperforms in low-sparsity phases ($\\widetilde{\\mathrm{II}} = 7.196$ vs.\\ $1.363$)---a qualitative reversal in strategy ranking.\nThe pattern replicates on Qwen2.5-7B-Instruct at $s \\geq 0.20$ ($d_z \\geq 0.55$; Spearman $\\rho = 1.0$; gradient permutation $p = 0.043$) and on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM), where monotonically increasing $d_z$ ($0.19 \\to 0.34$; $s{=}0.30$ Wilcoxon $p_{\\text{Bonf}} = 0.029$) suggests cross-architecture generalization, though at ${\\sim}$1/40 the absolute magnitude and with substantially weaker interaction than in Qwen2-based architectures. % exp_id: c3_llama\n\nWe propose entropy-discrimination collapse as an explanatory mechanism: head pruning flattens cumulative importance scores in phases where attention is already broadly distributed, degrading the discriminative power of importance-based eviction in a phase-dependent manner.\nThese findings challenge the phase-invariance assumption in compound sparsity deployment and motivate phase-aware compression budgets for reasoning models.\n\\end{abstract}",
      "numLines": 14,
      "startLine": 1,
      "totalLines": 14
    }
  }
}
```

</details>

---

### Tool call

_source line 22_

<details open><summary>🔧 Tool call — Read · `toolu_01X9DxBN5KeuyyXdSL28u15J`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10233ec7-5d03-448a-9224-b6173ea0cbe8",
  "uuid": "299bfe88-a2de-4746-9c15-03f58ba9b4a0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KbrgPnqywm3btXbv2qV1P3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 968,
      "cache_read_input_tokens": 23930,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 968
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

_source line 23 · 2026-05-14T21:49:25.173Z_

<details><summary>↩ Tool result · `toolu_01X9DxBN5KeuyyXdSL28u15J`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Long-context language models place acute pressure on the key--value (KV) cache, which grows linearly with sequence length \cite{kwon-sosp2023, pope-mlsys2023}.
5	Two complementary responses---\emph{attention head pruning} \cite{voita-acl2019, michel-neurips2019} and \emph{KV cache eviction} \cite{snapkv-neurips2024, adakv-neurips2025}---can be deployed simultaneously as \emph{compound sparsity}, but the resulting quality degradation is often super-additive \cite{spark-aaai2026, slim-icml2025}. Recent evaluations confirm that reasoning capabilities degrade disproportionately under compound compression \cite{unicomp-2026}, and that per-dimension safe zones intersect to form a smaller joint safe region \cite{phase-transition-compression-2026}.
6	
7	Prior work treats compound interaction magnitude as roughly constant across generation \cite{spark-aaai2026, unicomp-2026}, despite evidence that pruning sensitivity depends on representational phase \cite{decision-repr-transition-2026} and that no single sparse attention strategy dominates across generation stages \cite{sparse-frontier-2025}.
8	This assumption is problematic for reasoning models, whose generations alternate between broadly distributed attention (exploratory reasoning) and sharply concentrated attention (structured computation) \cite{thinkv-iclr2026}.
9	Phase-aware methods like ThinKV \cite{thinkv-iclr2026} apply different KV strategies per phase but without considering compound interaction, while importance-based eviction itself faces challenges from greedy bias \cite{greedy-bias-kvcache-2026}, deferred importance \cite{retentivekv-2026}, and temporal dynamics in long generations \cite{lethe-aaai2026}. These methods each optimize a single pruning axis; we characterize the interaction when multiple mechanisms are composed.
10	If compound severity varies across these phases, a uniform sparsity budget may be safe in one phase yet destructive in another.
11	
12	We show that compound sparsity severity is strongly modulated by reasoning phase and eviction strategy.
13	Under importance-based KV cache eviction, the Interaction Index---a measure of super-additive degradation---concentrates in low-sparsity phases and is largely absent in high-sparsity phases.
14	On DeepSeek-R1-Distill-Qwen-7B, the median phase difference rises from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$ ($d_z$: $0.44 \to 0.80$; Bonferroni-corrected $p < 0.005$ at all levels).
15	The pattern replicates at $s \geq 0.20$ on Qwen2.5-7B-Instruct ($d_z \geq 0.55$) and partially extends to a distinct architecture (DeepSeek-R1-Distill-Llama-8B, LlamaForCausalLM) with a qualitatively consistent but substantially weaker trend at $\sim$1/40 the magnitude.
16	Critically, random eviction produces no such gradient (7/8 conditions non-significant), confirming the gradient is an emergent phase-strategy interaction.
17	
18	We propose \emph{entropy-discrimination collapse} as a mechanism: head pruning flattens cumulative importance scores in phases where attention is broadly distributed, degrading the discriminative power of importance-based eviction in a phase-dependent manner.
19	Random eviction is immune because its decisions are independent of attention patterns.
20	Our contributions:
21	\begin{enumerate}[nosep,leftmargin=*]
22	    \item We identify a \textbf{phase--strategy interaction}: importance-based eviction exhibits a severity gradient across reasoning phases that is absent under random eviction (\S\ref{sec:results}).
23	    \item We show this gradient \textbf{increases monotonically with sparsity} and replicates across three models spanning two architectures (\S\ref{sec:results}).
24	    \item We propose \textbf{entropy-discrimination collapse} as a mechanistic explanation (\S\ref{sec:analysis}).
25	\end{enumerate}
26	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10233ec7-5d03-448a-9224-b6173ea0cbe8",
  "uuid": "8f95dce5-b61d-4edf-aa41-c317b85de4b8",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nLong-context language models place acute pressure on the key--value (KV) cache, which grows linearly with sequence length \\cite{kwon-sosp2023, pope-mlsys2023}.\nTwo complementary responses---\\emph{attention head pruning} \\cite{voita-acl2019, michel-neurips2019} and \\emph{KV cache eviction} \\cite{snapkv-neurips2024, adakv-neurips2025}---can be deployed simultaneously as \\emph{compound sparsity}, but the resulting quality degradation is often super-additive \\cite{spark-aaai2026, slim-icml2025}. Recent evaluations confirm that reasoning capabilities degrade disproportionately under compound compression \\cite{unicomp-2026}, and that per-dimension safe zones intersect to form a smaller joint safe region \\cite{phase-transition-compression-2026}.\n\nPrior work treats compound interaction magnitude as roughly constant across generation \\cite{spark-aaai2026, unicomp-2026}, despite evidence that pruning sensitivity depends on representational phase \\cite{decision-repr-transition-2026} and that no single sparse attention strategy dominates across generation stages \\cite{sparse-frontier-2025}.\nThis assumption is problematic for reasoning models, whose generations alternate between broadly distributed attention (exploratory reasoning) and sharply concentrated attention (structured computation) \\cite{thinkv-iclr2026}.\nPhase-aware methods like ThinKV \\cite{thinkv-iclr2026} apply different KV strategies per phase but without considering compound interaction, while importance-based eviction itself faces challenges from greedy bias \\cite{greedy-bias-kvcache-2026}, deferred importance \\cite{retentivekv-2026}, and temporal dynamics in long generations \\cite{lethe-aaai2026}. These methods each optimize a single pruning axis; we characterize the interaction when multiple mechanisms are composed.\nIf compound severity varies across these phases, a uniform sparsity budget may be safe in one phase yet destructive in another.\n\nWe show that compound sparsity severity is strongly modulated by reasoning phase and eviction strategy.\nUnder importance-based KV cache eviction, the Interaction Index---a measure of super-additive degradation---concentrates in low-sparsity phases and is largely absent in high-sparsity phases.\nOn DeepSeek-R1-Distill-Qwen-7B, the median phase difference rises from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$ ($d_z$: $0.44 \\to 0.80$; Bonferroni-corrected $p < 0.005$ at all levels).\nThe pattern replicates at $s \\geq 0.20$ on Qwen2.5-7B-Instruct ($d_z \\geq 0.55$) and partially extends to a distinct architecture (DeepSeek-R1-Distill-Llama-8B, LlamaForCausalLM) with a qualitatively consistent but substantially weaker trend at $\\sim$1/40 the magnitude.\nCritically, random eviction produces no such gradient (7/8 conditions non-significant), confirming the gradient is an emergent phase-strategy interaction.\n\nWe propose \\emph{entropy-discrimination collapse} as a mechanism: head pruning flattens cumulative importance scores in phases where attention is broadly distributed, degrading the discriminative power of importance-based eviction in a phase-dependent manner.\nRandom eviction is immune because its decisions are independent of attention patterns.\nOur contributions:\n\\begin{enumerate}[nosep,leftmargin=*]\n    \\item We identify a \\textbf{phase--strategy interaction}: importance-based eviction exhibits a severity gradient across reasoning phases that is absent under random eviction (\\S\\ref{sec:results}).\n    \\item We show this gradient \\textbf{increases monotonically with sparsity} and replicates across three models spanning two architectures (\\S\\ref{sec:results}).\n    \\item We propose \\textbf{entropy-discrimination collapse} as a mechanistic explanation (\\S\\ref{sec:analysis}).\n\\end{enumerate}\n",
      "numLines": 26,
      "startLine": 1,
      "totalLines": 26
    }
  }
}
```

</details>

---

### Tool call

_source line 24_

<details open><summary>🔧 Tool call — Read · `toolu_01KDxqA2kYyG6wALgVBBn9Vr`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10233ec7-5d03-448a-9224-b6173ea0cbe8",
  "uuid": "43ec2ac0-13c2-4dc2-971e-2870abd80218",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KbrgPnqywm3btXbv2qV1P3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 968,
      "cache_read_input_tokens": 23930,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 968
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

_source line 25 · 2026-05-14T21:49:25.513Z_

<details><summary>↩ Tool result · `toolu_01KDxqA2kYyG6wALgVBBn9Vr`</summary>

```text
1	
2	\section{Results}
3	\label{sec:results}
4	
5	\subsection{Strategy-Dependent Severity}
6	\label{sec:strategy-severity}
7	
8	Table~\ref{tab:aggregate-ii} reports the median compound severity difference across strategies and sparsity levels. Under importance-based eviction, $\Delta$ increases from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$---a $37{\times}$ amplification. Under random eviction, no systematic growth is observed ($-0.02$ to $1.54$), confirming that compound severity depends qualitatively on eviction strategy. % exp_id: bf16_importance_s015..s030, bf16_ds_rand_s015..s030; source: experiment_summary_table.json
9	
10	\begin{table}[t]
11	\centering
12	\small
13	\caption{Median compound severity difference ($\Delta = \widetilde{\mathrm{II}}_{\textit{low}} - \widetilde{\mathrm{II}}_{\textit{high}}$) by eviction strategy and sparsity level on DeepSeek-R1-Distill-Qwen-7B ($n{=}50$ MATH-500 problems).}
14	\label{tab:aggregate-ii}
15	\begin{tabular}{@{}lcccc@{}}
16	\toprule
17	Strategy & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\
18	\midrule
19	Importance & 0.39 & 1.48 & 7.16 & 14.59 \\ % exp_id: bf16_importance_s015..s030; source: experiment_summary_table.json median_diff
20	Random     & 0.01 & $-$0.02 & 0.54 & 1.54 \\ % exp_id: bf16_ds_rand_s015..s030; source: experiment_summary_table.json median_diff
21	\bottomrule
22	\end{tabular}
23	\end{table}
24	
25	
26	\subsection{Phase-Modulated Amplification}
27	\label{sec:phase-amplification}
28	
29	Decomposing II by reasoning phase reveals that strategy-dependent severity is driven by amplification in the low-sparsity phase. Table~\ref{tab:main-results} reports the full per-phase breakdown. The severity gradient $G$ increases from $69{\times}$ at $s{=}0.15$ to $274{\times}$ at $s{=}0.30$ under importance-based eviction, while the high-sparsity phase experiences near-zero interaction ($\widetilde{\mathrm{II}}_{\textit{high}}$ ranges from $0.006$ to $0.053$). Under random eviction, $G \approx 0.9$--$1.7{\times}$ at all sparsity levels. Figure~\ref{fig:hero} visualizes this contrast. % exp_id: bf16_importance_s015..s030, bf16_ds_rand_s015..s030; source: experiment_summary_table.json
30	
31	\begin{table*}[t]
32	\centering
33	\small
34	\caption{Interaction index (II) by eviction strategy, reasoning phase, and sparsity level. II values are problem-level medians across 50 problems. $\Delta = \widetilde{\mathrm{II}}_{\textit{low}} - \widetilde{\mathrm{II}}_{\textit{high}}$. $G = \widetilde{\mathrm{II}}_{\textit{low}} / \widetilde{\mathrm{II}}_{\textit{high}}$.}
35	\label{tab:main-results}
36	\begin{tabular}{@{}llccccr@{}}
37	\toprule
38	$s$ & Strategy & $\widetilde{\mathrm{II}}_{\textit{high}}$ & $\widetilde{\mathrm{II}}_{\textit{mid}}$ & $\widetilde{\mathrm{II}}_{\textit{low}}$ & $\Delta$ & $G$ \\
39	\midrule
40	0.15 & Importance & 0.006 & 0.081 & 0.398 & 0.39 & $\mathbf{69}$ \\
41	0.15 & Random     & 0.093 & 0.097 & 0.103 & 0.01 & 1.1 \\
42	\addlinespace
43	0.20 & Importance & 0.015 & 0.203 & 1.496 & 1.48 & $\mathbf{103}$ \\
44	0.20 & Random     & 0.292 & 0.350 & 0.276 & $-$0.02 & 0.9 \\
45	\addlinespace
46	0.25 & Importance & 0.032 & 1.118 & 7.196 & 7.16 & $\mathbf{222}$ \\
47	0.25 & Random     & 0.818 & 0.932 & 1.363 & 0.54 & 1.7 \\
48	\addlinespace
49	0.30 & Importance & 0.053 & 2.283 & 14.639 & 14.59 & $\mathbf{274}$ \\
50	0.30 & Random     & 2.503 & 2.592 & 4.041 & 1.54 & 1.6 \\
51	\bottomrule
52	\end{tabular}
53	\end{table*}
54	
55	\begin{figure}[t]
56	\centering
57	\includegraphics[width=\columnwidth]{fig1_dose_response.pdf}
58	\caption{Severity gradient ($G$) as a function of sparsity level $s$. Importance-based eviction (solid) exhibits an increasing gradient from $69{\times}$ to $274{\times}$; random eviction (dashed) remains flat near $1{\times}$. Shaded regions: 95\% bootstrap CIs.} % exp_id: bf16_importance_s015..s030, bf16_ds_rand_s015..s030
59	\label{fig:hero}
60	\end{figure}
61	
62	
63	\subsection{Phase-Strategy Crossover}
64	\label{sec:crossover}
65	
66	A strategy ranking reversal emerges across all sparsity levels: at $s{=}0.25$, importance-based eviction yields \emph{lower} II than random in the high-sparsity phase ($0.032$ vs.\ $0.818$) but \emph{higher} II in the low-sparsity phase ($7.196$ vs.\ $1.363$---a $5.3{\times}$ reversal), demonstrating that no single strategy dominates uniformly. Full crossover analysis and visualization appear in Appendix~\ref{app:crossover-details}. % exp_id: bf16_importance_s025, bf16_ds_rand_s025; source: experiment_summary_table.json; 7.196/1.363=5.28
67	
68	\subsection{Cross-Model Replication}
69	\label{sec:cross-model}
70	
71	Qwen2.5-7B-Instruct (standard instruction tuning, same Qwen2 backbone) reproduces the monotonic severity gradient: $\Delta$ increases from $0.04$ at $s{=}0.15$ to $2.94$ at $s{=}0.30$, paralleling DeepSeek at ${\sim}1/5$ the magnitude. Both models yield strictly increasing $d_z$ trajectories (Spearman $\rho = 1.0$; gradient permutation $p = 0.043$). The effect is marginal at $s{=}0.15$ ($d_z{=}0.28$, CI includes zero) but reliable at $s \geq 0.20$ ($d_z \geq 0.55$). Full cross-model tables and figures appear in Appendix~\ref{app:cross-model-details}. % exp_id: cross_model_analysis.json; cohens_d_bf16_qwen.json
72	
73	
74	\subsection{Cross-Architecture Validation}
75	\label{sec:cross-arch}
76	
77	To test whether the phase-modulated severity pattern extends beyond the Qwen2 architecture, we replicate the experiment on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, 8B parameters; $n{=}49$ paired problems). Table~\ref{tab:llama-cross-arch} reports the strategy-dependent severity comparison across sparsity levels.
78	
79	The qualitative pattern replicates: importance-based eviction produces systematically larger phase-dependent severity than random eviction, with monotonically increasing paired $d_z$ ($0.19 \to 0.26 \to 0.29 \to 0.34$). At $s{=}0.30$, the Wilcoxon test reaches significance after Bonferroni correction ($p = 0.029$, $k{=}4$). At $s{=}0.15$, the median difference CI $[0.002, 0.043]$ excludes zero despite the small absolute magnitude ($\widetilde{\Delta} = 0.020$). Under importance-based eviction, the within-strategy phase gradient $d_z$ (low $-$ high) is consistently large at all sparsity levels ($d_z \in [1.00, 1.12]$), while random eviction yields only small phase gradients ($d_z \in [0.35, 0.45]$). % exp_id: c3_llama
80	
81	The absolute magnitude is architecture-dependent: LLaMA severity differences are ${\sim}40{\times}$ smaller than DeepSeek and ${\sim}7{\times}$ smaller than Qwen, and the interaction is substantially weaker---random pruning also shows a non-trivial phase gradient on LLaMA ($d_z \in [0.35, 0.45]$), reducing the strategy contrast observed in Qwen2 models. The directional pattern---monotonically increasing $d_z$, importance $>$ random, larger phase gradient under importance---is qualitatively consistent across all three models spanning two architectures (Qwen2ForCausalLM, LlamaForCausalLM), though the interaction magnitude is substantially weaker on LlamaForCausalLM. % exp_id: c3_llama; cross_model_analysis.json
82	
83	\begin{table}[t]
84	\centering
85	\small
86	\caption{Cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM). $d_z$: paired Cohen's $d$ for importance vs.\ random severity; $\widetilde{\Delta}$: median paired difference with bootstrap 95\% CI ($B{=}10{,}000$); $p$: Bonferroni-corrected Wilcoxon $p$ ($k{=}4$). $n{=}49$ paired problems.}
87	\label{tab:llama-cross-arch}
88	\begin{tabular}{@{}lccc@{}}
89	\toprule
90	$s$ & $d_z$ & $\widetilde{\Delta}$\; [95\% CI] & $p_{\text{Bonf}}$ \\
91	\midrule
92	0.15 & 0.19 & 0.020\; $[0.002, 0.043]$ & 0.219 \\
93	0.20 & 0.26 & 0.022\; $[-0.090, 0.187]$ & 0.253 \\
94	0.25 & 0.29 & 0.095\; $[-0.004, 0.303]$ & 0.083 \\
95	0.30 & 0.34 & 0.356\; $[-0.069, 0.544]$ & $\mathbf{0.029}$ \\
96	\bottomrule
97	\end{tabular}
98	\end{table}
99	
100	
101	\subsection{Statistical Validation}
102	\label{sec:stat-validation}
103	
104	Paired permutation tests ($10{,}000$ permutations, Bonferroni-corrected) confirm that importance-based eviction produces significantly larger phase-dependent severity than random eviction at all four sparsity levels ($p_{\text{Bonf}} < 0.005$), with observed median differences increasing monotonically from $0.37$ at $s{=}0.15$ to $9.85$ at $s{=}0.30$. Full permutation test results and forest plot appear in Appendix~\ref{app:permutation-details}. % exp_id: deepseek_bf16_permtest; source: permutation_test_results.json
105	
106	Table~\ref{tab:cohens-d} reports paired Cohen's $d_z$ for both models. For DeepSeek, effect sizes grow from $d_z{=}0.44$ (small) to $d_z{=}0.80$ (large). For Qwen, the effect is marginal at $s{=}0.15$ ($d_z{=}0.28$, CI includes zero), becoming reliable at $s \geq 0.20$ ($d_z \geq 0.55$). At $s \geq 0.25$, Qwen exhibits larger standardized effect sizes ($d_z{=}0.89$/$1.02$ vs.\ $0.68$/$0.80$), consistent with lower between-problem variance despite smaller absolute II values. % exp_id: cohens_d_bf16.json; cohens_d_bf16_qwen.json
107	
108	\begin{table}[t]
109	\centering
110	\small
111	\caption{Paired $d_z$ for phase-dependent II (low $-$ high) under importance-based eviction. Bootstrap 95\% CIs ($B{=}10{,}000$).}
112	\label{tab:cohens-d}
113	\begin{tabular}{@{}lcccc@{}}
114	\toprule
115	$s$ & DS $d_z$ & $\widetilde{\Delta}$ [CI] & QW $d_z$ & $\widetilde{\Delta}$ [CI] \\
116	\midrule
117	0.15 & 0.44 & 0.32\; $[0.20, 0.47]$ & 0.28 & 0.05\; $[-0.01, 0.11]$\textsuperscript{ns} \\ % exp_id: bf16_ds_imp_s015, bf16_qw_imp_s015
118	0.20 & 0.52 & 1.15\; $[0.66, 1.26]$ & 0.55 & 0.21\; $[0.07, 0.40]$ \\ % exp_id: bf16_ds_imp_s020, bf16_qw_imp_s020
119	0.25 & 0.68 & 3.97\; $[2.83, 5.29]$ & 0.89 & 1.11\; $[0.61, 1.47]$ \\ % exp_id: bf16_ds_imp_s025, bf16_qw_imp_s025
120	0.30 & 0.80 & 9.94\; $[8.39, 16.65]$ & 1.02 & 2.62\; $[1.72, 3.65]$ \\ % exp_id: bf16_ds_imp_s030, bf16_qw_imp_s030
121	\bottomrule
122	\multicolumn{5}{@{}l}{\footnotesize \textsuperscript{ns}Marginal at $s{=}0.15$; reliable at $s \geq 0.20$.}
123	\end{tabular}
124	\end{table}
125	
126	We provide a mechanistic analysis in terms of entropy-discrimination collapse in \S\ref{sec:analysis}.
127	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10233ec7-5d03-448a-9224-b6173ea0cbe8",
  "uuid": "a75fd66d-e109-4b83-a18a-19eb2c0350fa",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex",
      "content": "\n\\section{Results}\n\\label{sec:results}\n\n\\subsection{Strategy-Dependent Severity}\n\\label{sec:strategy-severity}\n\nTable~\\ref{tab:aggregate-ii} reports the median compound severity difference across strategies and sparsity levels. Under importance-based eviction, $\\Delta$ increases from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$---a $37{\\times}$ amplification. Under random eviction, no systematic growth is observed ($-0.02$ to $1.54$), confirming that compound severity depends qualitatively on eviction strategy. % exp_id: bf16_importance_s015..s030, bf16_ds_rand_s015..s030; source: experiment_summary_table.json\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Median compound severity difference ($\\Delta = \\widetilde{\\mathrm{II}}_{\\textit{low}} - \\widetilde{\\mathrm{II}}_{\\textit{high}}$) by eviction strategy and sparsity level on DeepSeek-R1-Distill-Qwen-7B ($n{=}50$ MATH-500 problems).}\n\\label{tab:aggregate-ii}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nStrategy & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\\\\n\\midrule\nImportance & 0.39 & 1.48 & 7.16 & 14.59 \\\\ % exp_id: bf16_importance_s015..s030; source: experiment_summary_table.json median_diff\nRandom     & 0.01 & $-$0.02 & 0.54 & 1.54 \\\\ % exp_id: bf16_ds_rand_s015..s030; source: experiment_summary_table.json median_diff\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\subsection{Phase-Modulated Amplification}\n\\label{sec:phase-amplification}\n\nDecomposing II by reasoning phase reveals that strategy-dependent severity is driven by amplification in the low-sparsity phase. Table~\\ref{tab:main-results} reports the full per-phase breakdown. The severity gradient $G$ increases from $69{\\times}$ at $s{=}0.15$ to $274{\\times}$ at $s{=}0.30$ under importance-based eviction, while the high-sparsity phase experiences near-zero interaction ($\\widetilde{\\mathrm{II}}_{\\textit{high}}$ ranges from $0.006$ to $0.053$). Under random eviction, $G \\approx 0.9$--$1.7{\\times}$ at all sparsity levels. Figure~\\ref{fig:hero} visualizes this contrast. % exp_id: bf16_importance_s015..s030, bf16_ds_rand_s015..s030; source: experiment_summary_table.json\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Interaction index (II) by eviction strategy, reasoning phase, and sparsity level. II values are problem-level medians across 50 problems. $\\Delta = \\widetilde{\\mathrm{II}}_{\\textit{low}} - \\widetilde{\\mathrm{II}}_{\\textit{high}}$. $G = \\widetilde{\\mathrm{II}}_{\\textit{low}} / \\widetilde{\\mathrm{II}}_{\\textit{high}}$.}\n\\label{tab:main-results}\n\\begin{tabular}{@{}llccccr@{}}\n\\toprule\n$s$ & Strategy & $\\widetilde{\\mathrm{II}}_{\\textit{high}}$ & $\\widetilde{\\mathrm{II}}_{\\textit{mid}}$ & $\\widetilde{\\mathrm{II}}_{\\textit{low}}$ & $\\Delta$ & $G$ \\\\\n\\midrule\n0.15 & Importance & 0.006 & 0.081 & 0.398 & 0.39 & $\\mathbf{69}$ \\\\\n0.15 & Random     & 0.093 & 0.097 & 0.103 & 0.01 & 1.1 \\\\\n\\addlinespace\n0.20 & Importance & 0.015 & 0.203 & 1.496 & 1.48 & $\\mathbf{103}$ \\\\\n0.20 & Random     & 0.292 & 0.350 & 0.276 & $-$0.02 & 0.9 \\\\\n\\addlinespace\n0.25 & Importance & 0.032 & 1.118 & 7.196 & 7.16 & $\\mathbf{222}$ \\\\\n0.25 & Random     & 0.818 & 0.932 & 1.363 & 0.54 & 1.7 \\\\\n\\addlinespace\n0.30 & Importance & 0.053 & 2.283 & 14.639 & 14.59 & $\\mathbf{274}$ \\\\\n0.30 & Random     & 2.503 & 2.592 & 4.041 & 1.54 & 1.6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig1_dose_response.pdf}\n\\caption{Severity gradient ($G$) as a function of sparsity level $s$. Importance-based eviction (solid) exhibits an increasing gradient from $69{\\times}$ to $274{\\times}$; random eviction (dashed) remains flat near $1{\\times}$. Shaded regions: 95\\% bootstrap CIs.} % exp_id: bf16_importance_s015..s030, bf16_ds_rand_s015..s030\n\\label{fig:hero}\n\\end{figure}\n\n\n\\subsection{Phase-Strategy Crossover}\n\\label{sec:crossover}\n\nA strategy ranking reversal emerges across all sparsity levels: at $s{=}0.25$, importance-based eviction yields \\emph{lower} II than random in the high-sparsity phase ($0.032$ vs.\\ $0.818$) but \\emph{higher} II in the low-sparsity phase ($7.196$ vs.\\ $1.363$---a $5.3{\\times}$ reversal), demonstrating that no single strategy dominates uniformly. Full crossover analysis and visualization appear in Appendix~\\ref{app:crossover-details}. % exp_id: bf16_importance_s025, bf16_ds_rand_s025; source: experiment_summary_table.json; 7.196/1.363=5.28\n\n\\subsection{Cross-Model Replication}\n\\label{sec:cross-model}\n\nQwen2.5-7B-Instruct (standard instruction tuning, same Qwen2 backbone) reproduces the monotonic severity gradient: $\\Delta$ increases from $0.04$ at $s{=}0.15$ to $2.94$ at $s{=}0.30$, paralleling DeepSeek at ${\\sim}1/5$ the magnitude. Both models yield strictly increasing $d_z$ trajectories (Spearman $\\rho = 1.0$; gradient permutation $p = 0.043$). The effect is marginal at $s{=}0.15$ ($d_z{=}0.28$, CI includes zero) but reliable at $s \\geq 0.20$ ($d_z \\geq 0.55$). Full cross-model tables and figures appear in Appendix~\\ref{app:cross-model-details}. % exp_id: cross_model_analysis.json; cohens_d_bf16_qwen.json\n\n\n\\subsection{Cross-Architecture Validation}\n\\label{sec:cross-arch}\n\nTo test whether the phase-modulated severity pattern extends beyond the Qwen2 architecture, we replicate the experiment on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, 8B parameters; $n{=}49$ paired problems). Table~\\ref{tab:llama-cross-arch} reports the strategy-dependent severity comparison across sparsity levels.\n\nThe qualitative pattern replicates: importance-based eviction produces systematically larger phase-dependent severity than random eviction, with monotonically increasing paired $d_z$ ($0.19 \\to 0.26 \\to 0.29 \\to 0.34$). At $s{=}0.30$, the Wilcoxon test reaches significance after Bonferroni correction ($p = 0.029$, $k{=}4$). At $s{=}0.15$, the median difference CI $[0.002, 0.043]$ excludes zero despite the small absolute magnitude ($\\widetilde{\\Delta} = 0.020$). Under importance-based eviction, the within-strategy phase gradient $d_z$ (low $-$ high) is consistently large at all sparsity levels ($d_z \\in [1.00, 1.12]$), while random eviction yields only small phase gradients ($d_z \\in [0.35, 0.45]$). % exp_id: c3_llama\n\nThe absolute magnitude is architecture-dependent: LLaMA severity differences are ${\\sim}40{\\times}$ smaller than DeepSeek and ${\\sim}7{\\times}$ smaller than Qwen, and the interaction is substantially weaker---random pruning also shows a non-trivial phase gradient on LLaMA ($d_z \\in [0.35, 0.45]$), reducing the strategy contrast observed in Qwen2 models. The directional pattern---monotonically increasing $d_z$, importance $>$ random, larger phase gradient under importance---is qualitatively consistent across all three models spanning two architectures (Qwen2ForCausalLM, LlamaForCausalLM), though the interaction magnitude is substantially weaker on LlamaForCausalLM. % exp_id: c3_llama; cross_model_analysis.json\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM). $d_z$: paired Cohen's $d$ for importance vs.\\ random severity; $\\widetilde{\\Delta}$: median paired difference with bootstrap 95\\% CI ($B{=}10{,}000$); $p$: Bonferroni-corrected Wilcoxon $p$ ($k{=}4$). $n{=}49$ paired problems.}\n\\label{tab:llama-cross-arch}\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\n$s$ & $d_z$ & $\\widetilde{\\Delta}$\\; [95\\% CI] & $p_{\\text{Bonf}}$ \\\\\n\\midrule\n0.15 & 0.19 & 0.020\\; $[0.002, 0.043]$ & 0.219 \\\\\n0.20 & 0.26 & 0.022\\; $[-0.090, 0.187]$ & 0.253 \\\\\n0.25 & 0.29 & 0.095\\; $[-0.004, 0.303]$ & 0.083 \\\\\n0.30 & 0.34 & 0.356\\; $[-0.069, 0.544]$ & $\\mathbf{0.029}$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\n\\subsection{Statistical Validation}\n\\label{sec:stat-validation}\n\nPaired permutation tests ($10{,}000$ permutations, Bonferroni-corrected) confirm that importance-based eviction produces significantly larger phase-dependent severity than random eviction at all four sparsity levels ($p_{\\text{Bonf}} < 0.005$), with observed median differences increasing monotonically from $0.37$ at $s{=}0.15$ to $9.85$ at $s{=}0.30$. Full permutation test results and forest plot appear in Appendix~\\ref{app:permutation-details}. % exp_id: deepseek_bf16_permtest; source: permutation_test_results.json\n\nTable~\\ref{tab:cohens-d} reports paired Cohen's $d_z$ for both models. For DeepSeek, effect sizes grow from $d_z{=}0.44$ (small) to $d_z{=}0.80$ (large). For Qwen, the effect is marginal at $s{=}0.15$ ($d_z{=}0.28$, CI includes zero), becoming reliable at $s \\geq 0.20$ ($d_z \\geq 0.55$). At $s \\geq 0.25$, Qwen exhibits larger standardized effect sizes ($d_z{=}0.89$/$1.02$ vs.\\ $0.68$/$0.80$), consistent with lower between-problem variance despite smaller absolute II values. % exp_id: cohens_d_bf16.json; cohens_d_bf16_qwen.json\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Paired $d_z$ for phase-dependent II (low $-$ high) under importance-based eviction. Bootstrap 95\\% CIs ($B{=}10{,}000$).}\n\\label{tab:cohens-d}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n$s$ & DS $d_z$ & $\\widetilde{\\Delta}$ [CI] & QW $d_z$ & $\\widetilde{\\Delta}$ [CI] \\\\\n\\midrule\n0.15 & 0.44 & 0.32\\; $[0.20, 0.47]$ & 0.28 & 0.05\\; $[-0.01, 0.11]$\\textsuperscript{ns} \\\\ % exp_id: bf16_ds_imp_s015, bf16_qw_imp_s015\n0.20 & 0.52 & 1.15\\; $[0.66, 1.26]$ & 0.55 & 0.21\\; $[0.07, 0.40]$ \\\\ % exp_id: bf16_ds_imp_s020, bf16_qw_imp_s020\n0.25 & 0.68 & 3.97\\; $[2.83, 5.29]$ & 0.89 & 1.11\\; $[0.61, 1.47]$ \\\\ % exp_id: bf16_ds_imp_s025, bf16_qw_imp_s025\n0.30 & 0.80 & 9.94\\; $[8.39, 16.65]$ & 1.02 & 2.62\\; $[1.72, 3.65]$ \\\\ % exp_id: bf16_ds_imp_s030, bf16_qw_imp_s030\n\\bottomrule\n\\multicolumn{5}{@{}l}{\\footnotesize \\textsuperscript{ns}Marginal at $s{=}0.15$; reliable at $s \\geq 0.20$.}\n\\end{tabular}\n\\end{table}\n\nWe provide a mechanistic analysis in terms of entropy-discrimination collapse in \\S\\ref{sec:analysis}.\n",
      "numLines": 127,
      "startLine": 1,
      "totalLines": 127
    }
  }
}
```

</details>

---

### Tool call

_source line 26_

<details open><summary>🔧 Tool call — Read · `toolu_019KfUdfEGs4GBjJmcfvpEJo`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/methodology.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10233ec7-5d03-448a-9224-b6173ea0cbe8",
  "uuid": "283779ca-edaf-4b11-8866-bfb95a8560b4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KbrgPnqywm3btXbv2qV1P3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 968,
      "cache_read_input_tokens": 23930,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 968
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

_source line 27 · 2026-05-14T21:49:25.985Z_

<details><summary>↩ Tool result · `toolu_019KfUdfEGs4GBjJmcfvpEJo`</summary>

```text
1	\section{Experimental Setup}
2	\label{sec:experimental-setup}
3	
4	\paragraph{Models.}
5	\label{sec:models}
6	We evaluate on two 7B-parameter models sharing the Qwen2 backbone (28 layers, 28 heads, 4-group GQA): \textbf{DeepSeek-R1-Distill-Qwen-7B}~\cite{deepseek-r1-2025}, distilled from DeepSeek-R1 with explicit chain-of-thought traces yielding pronounced phase structure; and \textbf{Qwen2.5-7B-Instruct}~\cite{qwen25-2024}, with standard instruction tuning, providing a cross-model replication target. Both are loaded in \texttt{bfloat16} with eager attention.\footnote{An earlier \texttt{float16} configuration produced sporadic NaN values; \texttt{bfloat16} eliminated all occurrences.}
7	
8	\paragraph{Dataset.}
9	\label{sec:dataset}
10	We use 50 problems stratified from MATH-500~\cite{math500-neurips2021}, sampling uniformly across categories with a fixed seed. Each problem is decoded greedily (\texttt{max\_new\_tokens}$=$2048).
11	
12	\paragraph{Sparsity configuration.}
13	\label{sec:sparsity-config}
14	We apply symmetric compound sparsity at $s \in \{0.15, 0.20, 0.25, 0.30\}$, computing perplexity under four conditions: dense, attention-only, KV-only, and compound. We compare \emph{importance-based} eviction (position-normalized cumulative attention score, Eq.~\ref{eq:kv-importance}; BOS always retained) and \emph{random} eviction (uniform). Heads are pruned per layer by Frobenius norm; under random eviction, both heads and positions are selected uniformly.
15	
16	\paragraph{Phase segmentation and metrics.}
17	\label{sec:phase-seg}
18	Each sequence is segmented into three phases using the quantile-based method (\S\ref{sec:phase-segmentation}), with $\texttt{min\_phase\_length}{=}10$. We compute segment-level perplexity, II (Eq.~\ref{eq:ii}), and $G$ (Eq.~\ref{eq:gradient}), reporting medians due to heavy right-skew (mean/median ratios up to 43:1).
19	
20	\paragraph{Statistical analysis.}
21	\label{sec:stats}
22	All confidence intervals and significance tests use nonparametric bootstrap ($B{=}10{,}000$)~\cite{efron-1993}. Paired bootstrap controls for problem-level variance. All tests yield $p_{\text{Bonf}} < 0.005$ at every sparsity level.\footnote{Experiments on 4$\times$ NVIDIA RTX PRO 6000 Blackwell 96\,GB GPUs.}
23	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10233ec7-5d03-448a-9224-b6173ea0cbe8",
  "uuid": "a31863f9-8810-45b9-aa3d-0581a3a24b49",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/methodology.tex",
      "content": "\\section{Experimental Setup}\n\\label{sec:experimental-setup}\n\n\\paragraph{Models.}\n\\label{sec:models}\nWe evaluate on two 7B-parameter models sharing the Qwen2 backbone (28 layers, 28 heads, 4-group GQA): \\textbf{DeepSeek-R1-Distill-Qwen-7B}~\\cite{deepseek-r1-2025}, distilled from DeepSeek-R1 with explicit chain-of-thought traces yielding pronounced phase structure; and \\textbf{Qwen2.5-7B-Instruct}~\\cite{qwen25-2024}, with standard instruction tuning, providing a cross-model replication target. Both are loaded in \\texttt{bfloat16} with eager attention.\\footnote{An earlier \\texttt{float16} configuration produced sporadic NaN values; \\texttt{bfloat16} eliminated all occurrences.}\n\n\\paragraph{Dataset.}\n\\label{sec:dataset}\nWe use 50 problems stratified from MATH-500~\\cite{math500-neurips2021}, sampling uniformly across categories with a fixed seed. Each problem is decoded greedily (\\texttt{max\\_new\\_tokens}$=$2048).\n\n\\paragraph{Sparsity configuration.}\n\\label{sec:sparsity-config}\nWe apply symmetric compound sparsity at $s \\in \\{0.15, 0.20, 0.25, 0.30\\}$, computing perplexity under four conditions: dense, attention-only, KV-only, and compound. We compare \\emph{importance-based} eviction (position-normalized cumulative attention score, Eq.~\\ref{eq:kv-importance}; BOS always retained) and \\emph{random} eviction (uniform). Heads are pruned per layer by Frobenius norm; under random eviction, both heads and positions are selected uniformly.\n\n\\paragraph{Phase segmentation and metrics.}\n\\label{sec:phase-seg}\nEach sequence is segmented into three phases using the quantile-based method (\\S\\ref{sec:phase-segmentation}), with $\\texttt{min\\_phase\\_length}{=}10$. We compute segment-level perplexity, II (Eq.~\\ref{eq:ii}), and $G$ (Eq.~\\ref{eq:gradient}), reporting medians due to heavy right-skew (mean/median ratios up to 43:1).\n\n\\paragraph{Statistical analysis.}\n\\label{sec:stats}\nAll confidence intervals and significance tests use nonparametric bootstrap ($B{=}10{,}000$)~\\cite{efron-1993}. Paired bootstrap controls for problem-level variance. All tests yield $p_{\\text{Bonf}} < 0.005$ at every sparsity level.\\footnote{Experiments on 4$\\times$ NVIDIA RTX PRO 6000 Blackwell 96\\,GB GPUs.}\n",
      "numLines": 23,
      "startLine": 1,
      "totalLines": 23
    }
  }
}
```

</details>

---

### Tool call

_source line 28_

<details open><summary>🔧 Tool call — Read · `toolu_01T6UCkBX1s4shMsopwQc2gg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10233ec7-5d03-448a-9224-b6173ea0cbe8",
  "uuid": "28ec0227-5e23-416f-bffe-93a6a7c78246",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KbrgPnqywm3btXbv2qV1P3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 968,
      "cache_read_input_tokens": 23930,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 968
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

_source line 29 · 2026-05-14T21:49:27.001Z_

<details><summary>↩ Tool result · `toolu_01T6UCkBX1s4shMsopwQc2gg`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Quantitative surprise.}
5	While the qualitative direction---importance scores degrade when attention is diffuse---may seem expected, the quantitative structure is not predictable from first principles. The severity gradient ($69$--$274{\times}$) far exceeds a naive ``somewhat worse'' prediction. The crossover---where importance-based eviction simultaneously outperforms random in high-sparsity phases ($\widetilde{\mathrm{II}} = 0.032$ vs.\ $0.818$) and underperforms in low-sparsity phases ($7.196$ vs.\ $1.363$)---cannot be derived from single-axis entropy reasoning. The flat random baseline ($G \approx 1$) confirms the amplification is strategy-specific, not inherent to compound sparsity. % exp_id: bf16_importance_s015..s030, bf16_importance_s025, bf16_ds_rand_s025; source: experiment_summary_table.json
6	
7	\paragraph{Implications for deployment.}
8	Applying a uniform compression budget across all inference steps implicitly accepts order-of-magnitude severity penalties during low-sparsity reasoning phases. A \emph{phase-aware compression budget}---allocating lower sparsity to phases with $G \gg 1$ and reclaiming budget in near-additive high-sparsity phases---could mitigate this interaction while preserving compression gains. The severity gradient provides a natural signal for such allocation. Discrimination collapse depends on attention-mass-based importance scoring shared by major KV cache methods (H$_2$O \cite{h2o-neurips2023}, SnapKV \cite{snapkv-neurips2024}, PyramidKV \cite{pyramidkv-2024}), suggesting broad applicability. Extended discussion in Appendix~\ref{app:extended-discussion}.
9	
10	\paragraph{Architecture-dependent magnitude.}
11	Cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM) provides partial support for the qualitative pattern---monotonically increasing severity gradient under importance-based eviction with within-strategy phase gradient $d_z \geq 1.0$---while revealing that absolute severity magnitudes are architecture-dependent (${\sim}40{\times}$ smaller than DeepSeek, ${\sim}7{\times}$ smaller than Qwen) and the strategy--phase interaction is substantially weaker than in Qwen2-based architectures. Notably, random pruning also exhibits a non-trivial phase gradient on LLaMA ($d_z \in [0.35, 0.45]$), reducing the contrast between strategies. This dissociation between qualitatively consistent directional trends and markedly different magnitudes suggests the phase-strategy interaction may be a general property of compound sparsity on reasoning models, while its quantitative impact---and the degree to which it is strategy-specific---depends on architecture-specific attention distributions and head specialization patterns. % exp_id: c3_llama
12	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10233ec7-5d03-448a-9224-b6173ea0cbe8",
  "uuid": "f2c43f88-5998-4d3d-9bff-4b15618bdbeb",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex",
      "content": "\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Quantitative surprise.}\nWhile the qualitative direction---importance scores degrade when attention is diffuse---may seem expected, the quantitative structure is not predictable from first principles. The severity gradient ($69$--$274{\\times}$) far exceeds a naive ``somewhat worse'' prediction. The crossover---where importance-based eviction simultaneously outperforms random in high-sparsity phases ($\\widetilde{\\mathrm{II}} = 0.032$ vs.\\ $0.818$) and underperforms in low-sparsity phases ($7.196$ vs.\\ $1.363$)---cannot be derived from single-axis entropy reasoning. The flat random baseline ($G \\approx 1$) confirms the amplification is strategy-specific, not inherent to compound sparsity. % exp_id: bf16_importance_s015..s030, bf16_importance_s025, bf16_ds_rand_s025; source: experiment_summary_table.json\n\n\\paragraph{Implications for deployment.}\nApplying a uniform compression budget across all inference steps implicitly accepts order-of-magnitude severity penalties during low-sparsity reasoning phases. A \\emph{phase-aware compression budget}---allocating lower sparsity to phases with $G \\gg 1$ and reclaiming budget in near-additive high-sparsity phases---could mitigate this interaction while preserving compression gains. The severity gradient provides a natural signal for such allocation. Discrimination collapse depends on attention-mass-based importance scoring shared by major KV cache methods (H$_2$O \\cite{h2o-neurips2023}, SnapKV \\cite{snapkv-neurips2024}, PyramidKV \\cite{pyramidkv-2024}), suggesting broad applicability. Extended discussion in Appendix~\\ref{app:extended-discussion}.\n\n\\paragraph{Architecture-dependent magnitude.}\nCross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM) provides partial support for the qualitative pattern---monotonically increasing severity gradient under importance-based eviction with within-strategy phase gradient $d_z \\geq 1.0$---while revealing that absolute severity magnitudes are architecture-dependent (${\\sim}40{\\times}$ smaller than DeepSeek, ${\\sim}7{\\times}$ smaller than Qwen) and the strategy--phase interaction is substantially weaker than in Qwen2-based architectures. Notably, random pruning also exhibits a non-trivial phase gradient on LLaMA ($d_z \\in [0.35, 0.45]$), reducing the contrast between strategies. This dissociation between qualitatively consistent directional trends and markedly different magnitudes suggests the phase-strategy interaction may be a general property of compound sparsity on reasoning models, while its quantitative impact---and the degree to which it is strategy-specific---depends on architecture-specific attention distributions and head specialization patterns. % exp_id: c3_llama\n",
      "numLines": 12,
      "startLine": 1,
      "totalLines": 12
    }
  }
}
```

</details>

---

### Tool call

_source line 30_

<details open><summary>🔧 Tool call — Read · `toolu_0123bPa8Bhsa7dC8sgWgt4jG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10233ec7-5d03-448a-9224-b6173ea0cbe8",
  "uuid": "5f6c8d7b-fadb-4f0f-888c-e9bd697269e7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KbrgPnqywm3btXbv2qV1P3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 968,
      "cache_read_input_tokens": 23930,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 968
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

_source line 31 · 2026-05-14T21:49:27.398Z_

<details><summary>↩ Tool result · `toolu_0123bPa8Bhsa7dC8sgWgt4jG`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We showed that compound sparsity severity---the super-additive interaction between head pruning and KV cache eviction---is not phase-invariant but exhibits an emergent phase-strategy interaction spanning over an order of magnitude within a single generation. Under importance-based eviction, the severity gradient grows from $69{\times}$ to $274{\times}$ across sparsity levels ($d_z$: $0.44 \to 0.80$); random eviction shows no such modulation (7/8 conditions non-significant). A crossover at $s{=}0.25$---where importance-based eviction reverses ranking across phases---demonstrates that no single strategy dominates uniformly. The pattern replicates on Qwen2.5-7B-Instruct at $s \geq 0.20$ ($d_z \geq 0.55$) and partially extends cross-architecture to DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM) with a qualitatively consistent but substantially weaker trend at $\sim$1/40 the magnitude. Discrimination collapse provides a mechanistic explanation supported by both Qwen2-based models; LLaMA results are directionally consistent but the interaction is weaker than in Qwen2 architectures.
5	These findings motivate phase-aware sparsity allocation for reasoning model deployment.
6	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10233ec7-5d03-448a-9224-b6173ea0cbe8",
  "uuid": "fab0184c-b703-4302-8840-1279d909ddbb",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/conclusion.tex",
      "content": "\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe showed that compound sparsity severity---the super-additive interaction between head pruning and KV cache eviction---is not phase-invariant but exhibits an emergent phase-strategy interaction spanning over an order of magnitude within a single generation. Under importance-based eviction, the severity gradient grows from $69{\\times}$ to $274{\\times}$ across sparsity levels ($d_z$: $0.44 \\to 0.80$); random eviction shows no such modulation (7/8 conditions non-significant). A crossover at $s{=}0.25$---where importance-based eviction reverses ranking across phases---demonstrates that no single strategy dominates uniformly. The pattern replicates on Qwen2.5-7B-Instruct at $s \\geq 0.20$ ($d_z \\geq 0.55$) and partially extends cross-architecture to DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM) with a qualitatively consistent but substantially weaker trend at $\\sim$1/40 the magnitude. Discrimination collapse provides a mechanistic explanation supported by both Qwen2-based models; LLaMA results are directionally consistent but the interaction is weaker than in Qwen2 architectures.\nThese findings motivate phase-aware sparsity allocation for reasoning model deployment.\n",
      "numLines": 6,
      "startLine": 1,
      "totalLines": 6
    }
  }
}
```

</details>

---

### Tool call

_source line 32_

<details open><summary>🔧 Tool call — Read · `toolu_01EJKZVcM1hAUfAyyZdmsQc8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10233ec7-5d03-448a-9224-b6173ea0cbe8",
  "uuid": "c35ebc30-a801-4d80-9c7f-66cbfaebb6b3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KbrgPnqywm3btXbv2qV1P3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 968,
      "cache_read_input_tokens": 23930,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 968
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

_source line 33 · 2026-05-14T21:49:27.874Z_

<details><summary>↩ Tool result · `toolu_01EJKZVcM1hAUfAyyZdmsQc8`</summary>

```text
1	\section{Analysis: Entropy-Discrimination Collapse}
2	\label{sec:analysis}
3	
4	We propose \emph{discrimination collapse} as the primary mechanism driving the phase-strategy interaction. Head pruning reduces the number of heads contributing to cumulative importance scores, flattening the score distribution: the Gini coefficient decreases by $0.030$--$0.081$ (DeepSeek) and $0.010$--$0.020$ (Qwen) across all sparsity levels, with consistent negative deltas in all 16 conditions (Appendix~\ref{app:analysis}, Table~\ref{tab:discrimination-metrics-full}). When importance scores lose discriminability, thresholding degenerates into noise-sensitive selection---functionally approaching biased random eviction. This effect is phase-dependent: in low-sparsity phases, attention is already broadly distributed, so pruning-induced flattening has maximum impact; in high-sparsity phases, concentration is preserved. Random eviction is immune because its decisions are independent of score quality, explaining $G \approx 1$. % exp_id: c4_entropy_deepseek, c4_entropy_qwen
5	
6	Beyond discrimination collapse, head pruning redistributes the attention entropy of surviving heads. For DeepSeek, the entropy delta is consistently negative ($\Delta\mathcal{H} \in [-0.047, -0.040]$), indicating that importance-based pruning systematically selects heads whose removal concentrates attention in survivors. For Qwen, the pattern partially replicates at $s \leq 0.20$ but reverses at $s{=}0.25$ ($\Delta\mathcal{H} = +0.045$), suggesting model-specific head specialization patterns (Appendix~\ref{app:analysis}, Table~\ref{tab:entropy-deltas}). We characterize discrimination collapse as the robust, model-independent driver, with entropy redistribution as a secondary, model-dependent amplifier. % exp_id: c4_entropy_deepseek, c4_entropy_qwen
7	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10233ec7-5d03-448a-9224-b6173ea0cbe8",
  "uuid": "4bd0a7b0-b8ea-409c-8e22-fa917d098a33",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/analysis.tex",
      "content": "\\section{Analysis: Entropy-Discrimination Collapse}\n\\label{sec:analysis}\n\nWe propose \\emph{discrimination collapse} as the primary mechanism driving the phase-strategy interaction. Head pruning reduces the number of heads contributing to cumulative importance scores, flattening the score distribution: the Gini coefficient decreases by $0.030$--$0.081$ (DeepSeek) and $0.010$--$0.020$ (Qwen) across all sparsity levels, with consistent negative deltas in all 16 conditions (Appendix~\\ref{app:analysis}, Table~\\ref{tab:discrimination-metrics-full}). When importance scores lose discriminability, thresholding degenerates into noise-sensitive selection---functionally approaching biased random eviction. This effect is phase-dependent: in low-sparsity phases, attention is already broadly distributed, so pruning-induced flattening has maximum impact; in high-sparsity phases, concentration is preserved. Random eviction is immune because its decisions are independent of score quality, explaining $G \\approx 1$. % exp_id: c4_entropy_deepseek, c4_entropy_qwen\n\nBeyond discrimination collapse, head pruning redistributes the attention entropy of surviving heads. For DeepSeek, the entropy delta is consistently negative ($\\Delta\\mathcal{H} \\in [-0.047, -0.040]$), indicating that importance-based pruning systematically selects heads whose removal concentrates attention in survivors. For Qwen, the pattern partially replicates at $s \\leq 0.20$ but reverses at $s{=}0.25$ ($\\Delta\\mathcal{H} = +0.045$), suggesting model-specific head specialization patterns (Appendix~\\ref{app:analysis}, Table~\\ref{tab:entropy-deltas}). We characterize discrimination collapse as the robust, model-independent driver, with entropy redistribution as a secondary, model-dependent amplifier. % exp_id: c4_entropy_deepseek, c4_entropy_qwen\n",
      "numLines": 7,
      "startLine": 1,
      "totalLines": 7
    }
  }
}
```

</details>

---

### Tool call

_source line 34_

<details open><summary>🔧 Tool call — Read · `toolu_01EjmV11MqD8yuUUHve1BkwT`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10233ec7-5d03-448a-9224-b6173ea0cbe8",
  "uuid": "0ba04565-28cc-48c9-b740-795d161e6032",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KbrgPnqywm3btXbv2qV1P3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 968,
      "cache_read_input_tokens": 23930,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 968
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

_source line 35 · 2026-05-14T21:49:28.207Z_

<details><summary>↩ Tool result · `toolu_01EjmV11MqD8yuUUHve1BkwT`</summary>

```text
1	\section{Compound Sparsity Formulation}
2	\label{app:formulation-details}
3	
4	\paragraph{Attention head pruning.}
5	Heads are ranked by Frobenius norm importance $w_j^{(\ell)} = \|\mathbf{A}_j^{(\ell)}\|_F$ \cite{voita-acl2019, michel-neurips2019}; a binary mask $m_j^{(\ell)} \in \{0,1\}$ retains the top-$(1{-}s)\cdot H$ heads:
6	\begin{equation}
7	    \tilde{\mathbf{o}}_j^{(\ell)} = m_j^{(\ell)} \cdot \mathbf{o}_j^{(\ell)}.
8	    \label{eq:head-mask}
9	\end{equation}
10	
11	\paragraph{KV cache eviction.}
12	A position mask $\mathbf{m}_k \in \{0,1\}^T$ retains the top-$(1{-}s)\cdot T$ positions (BOS always preserved):
13	\begin{equation}
14	    \tilde{a}_{ij} = a_{ij} \cdot m_{k,j}, \quad \forall\, i, j.
15	    \label{eq:kv-mask}
16	\end{equation}
17	Under importance-based eviction, each position $j$ is scored by its cumulative attention mass with position normalization:
18	\begin{equation}
19	    \mathrm{imp}(j) = \frac{\sum_{\ell, h, i} a_{ij}^{(\ell,h)}}{T - j},
20	    \label{eq:kv-importance}
21	\end{equation}
22	where the denominator compensates for causal bias---earlier positions are attended to by more queries \cite{thinkv-iclr2026, defensivekv-iclr2026}. Under random eviction, positions (excluding BOS) are evicted uniformly at random.
23	
24	\paragraph{Compound sparsity.}
25	Applying both mechanisms simultaneously yields compound sparsity. The two axes interact: head pruning redistributes attention mass, altering the importance ranking for KV eviction. Prior work \cite{spark-aaai2026} reports super-additive joint effects but treats interaction magnitude as a fixed property of $s$.
26	
27	\paragraph{Attention sparsity metric.}
28	For each query position $i$ and head $h$, we compute the fraction of key positions receiving negligible attention:
29	\begin{equation}
30	    \sigma_i^{(h)} = \frac{1}{T} \sum_{j=1}^{T} \mathbf{1}\!\left[a_{ij}^{(h)} < 0.01 \cdot \max_k a_{ik}^{(h)}\right].
31	    \label{eq:attn-sparsity}
32	\end{equation}
33	The per-position sparsity $\sigma_i = \frac{1}{H}\sum_h \sigma_i^{(h)}$ averages across all heads. Tokens are partitioned into high-, mid-, and low-sparsity phases by the tercile boundaries of $\{\sigma_i\}$; segments shorter than 10 tokens are merged into adjacent phases.
34	
35	\section{Multiplicative Null Verification}
36	\label{app:multiplicative-null}
37	
38	We verified that replacing the additive null $r_b = r_a + r_k - 1$ (Eq.~\ref{eq:ii}) with the multiplicative null $r_b = r_a \cdot r_k$ does not change qualitative conclusions. Under the multiplicative formulation, the interaction index becomes $\mathrm{II}_{\times} = r_b - r_a \cdot r_k$. Across all sparsity levels and both eviction strategies, the sign and relative ordering of $\mathrm{II}_{\times}$ match those of the additive II: importance-based eviction exhibits a monotonically increasing severity gradient ($G_{\times} = 58$--$241{\times}$), while random eviction remains flat ($G_{\times} \approx 1$). The crossover at $s{=}0.25$ is preserved. We adopt the additive formulation in the main text because the two sparsity axes operate on disjoint model dimensions (structural vs.\ positional), making additive independence the more natural null hypothesis at the sparsity levels studied.
39	
40	% Bootstrap and permutation details moved to main text \S\ref{sec:stat-validation}
41	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10233ec7-5d03-448a-9224-b6173ea0cbe8",
  "uuid": "3445f01b-de5d-405e-b0a2-86d197c176b8",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix.tex",
      "content": "\\section{Compound Sparsity Formulation}\n\\label{app:formulation-details}\n\n\\paragraph{Attention head pruning.}\nHeads are ranked by Frobenius norm importance $w_j^{(\\ell)} = \\|\\mathbf{A}_j^{(\\ell)}\\|_F$ \\cite{voita-acl2019, michel-neurips2019}; a binary mask $m_j^{(\\ell)} \\in \\{0,1\\}$ retains the top-$(1{-}s)\\cdot H$ heads:\n\\begin{equation}\n    \\tilde{\\mathbf{o}}_j^{(\\ell)} = m_j^{(\\ell)} \\cdot \\mathbf{o}_j^{(\\ell)}.\n    \\label{eq:head-mask}\n\\end{equation}\n\n\\paragraph{KV cache eviction.}\nA position mask $\\mathbf{m}_k \\in \\{0,1\\}^T$ retains the top-$(1{-}s)\\cdot T$ positions (BOS always preserved):\n\\begin{equation}\n    \\tilde{a}_{ij} = a_{ij} \\cdot m_{k,j}, \\quad \\forall\\, i, j.\n    \\label{eq:kv-mask}\n\\end{equation}\nUnder importance-based eviction, each position $j$ is scored by its cumulative attention mass with position normalization:\n\\begin{equation}\n    \\mathrm{imp}(j) = \\frac{\\sum_{\\ell, h, i} a_{ij}^{(\\ell,h)}}{T - j},\n    \\label{eq:kv-importance}\n\\end{equation}\nwhere the denominator compensates for causal bias---earlier positions are attended to by more queries \\cite{thinkv-iclr2026, defensivekv-iclr2026}. Under random eviction, positions (excluding BOS) are evicted uniformly at random.\n\n\\paragraph{Compound sparsity.}\nApplying both mechanisms simultaneously yields compound sparsity. The two axes interact: head pruning redistributes attention mass, altering the importance ranking for KV eviction. Prior work \\cite{spark-aaai2026} reports super-additive joint effects but treats interaction magnitude as a fixed property of $s$.\n\n\\paragraph{Attention sparsity metric.}\nFor each query position $i$ and head $h$, we compute the fraction of key positions receiving negligible attention:\n\\begin{equation}\n    \\sigma_i^{(h)} = \\frac{1}{T} \\sum_{j=1}^{T} \\mathbf{1}\\!\\left[a_{ij}^{(h)} < 0.01 \\cdot \\max_k a_{ik}^{(h)}\\right].\n    \\label{eq:attn-sparsity}\n\\end{equation}\nThe per-position sparsity $\\sigma_i = \\frac{1}{H}\\sum_h \\sigma_i^{(h)}$ averages across all heads. Tokens are partitioned into high-, mid-, and low-sparsity phases by the tercile boundaries of $\\{\\sigma_i\\}$; segments shorter than 10 tokens are merged into adjacent phases.\n\n\\section{Multiplicative Null Verification}\n\\label{app:multiplicative-null}\n\nWe verified that replacing the additive null $r_b = r_a + r_k - 1$ (Eq.~\\ref{eq:ii}) with the multiplicative null $r_b = r_a \\cdot r_k$ does not change qualitative conclusions. Under the multiplicative formulation, the interaction index becomes $\\mathrm{II}_{\\times} = r_b - r_a \\cdot r_k$. Across all sparsity levels and both eviction strategies, the sign and relative ordering of $\\mathrm{II}_{\\times}$ match those of the additive II: importance-based eviction exhibits a monotonically increasing severity gradient ($G_{\\times} = 58$--$241{\\times}$), while random eviction remains flat ($G_{\\times} \\approx 1$). The crossover at $s{=}0.25$ is preserved. We adopt the additive formulation in the main text because the two sparsity axes operate on disjoint model dimensions (structural vs.\\ positional), making additive independence the more natural null hypothesis at the sparsity levels studied.\n\n% Bootstrap and permutation details moved to main text \\S\\ref{sec:stat-validation}\n",
      "numLines": 41,
      "startLine": 1,
      "totalLines": 41
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
Let me continue reading the remaining .tex files to get complete coverage.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10233ec7-5d03-448a-9224-b6173ea0cbe8",
  "uuid": "5d670b8d-6c94-45d5-82c5-775bcb623667",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FsD7CPPuwEQCkUJRcvGJo5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10685,
      "cache_read_input_tokens": 24898,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10685
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

Let me continue reading the remaining .tex files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10233ec7-5d03-448a-9224-b6173ea0cbe8",
  "uuid": "66473cf5-86ea-446d-bed0-cc962a0c7289",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FsD7CPPuwEQCkUJRcvGJo5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10685,
      "cache_read_input_tokens": 24898,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10685
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

<details open><summary>🔧 Tool call — Read · `toolu_01Az6T3UtgyV4bqZXZQKYNrL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix.tex",
  "offset": 41
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10233ec7-5d03-448a-9224-b6173ea0cbe8",
  "uuid": "3b0810b5-7a90-4a07-88a8-de3d05896e9d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FsD7CPPuwEQCkUJRcvGJo5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10685,
      "cache_read_input_tokens": 24898,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10685
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

_source line 39 · 2026-05-14T21:49:34.477Z_

<details><summary>↩ Tool result · `toolu_01Az6T3UtgyV4bqZXZQKYNrL`</summary>

```text
&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (41). The file has 41 lines.&lt;/system-reminder>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10233ec7-5d03-448a-9224-b6173ea0cbe8",
  "uuid": "35aa6467-ee96-4193-b4a6-1200e1f8bcf7",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix.tex",
      "content": "",
      "numLines": 1,
      "startLine": 41,
      "totalLines": 41
    }
  }
}
```

</details>

---

### Tool call

_source line 40_

<details open><summary>🔧 Tool call — Read · `toolu_01JPqr9D6797jWnvm6jU1Xqc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10233ec7-5d03-448a-9224-b6173ea0cbe8",
  "uuid": "1a89f155-a8a7-401c-ad2e-6e8b4064ffb1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FsD7CPPuwEQCkUJRcvGJo5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10685,
      "cache_read_input_tokens": 24898,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10685
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

_source line 41 · 2026-05-14T21:49:35.022Z_

<details><summary>↩ Tool result · `toolu_01JPqr9D6797jWnvm6jU1Xqc`</summary>

```text
1	% Appendix: supplementary results details
2	
3	\section{Cross-Model Replication Details}
4	\label{app:cross-model-details}
5	
6	\paragraph{Per-problem concordance.}
7	The per-problem concordance across models is not significant (mean $\rho = -0.11$, $p = 0.926$), indicating that while the aggregate gradient direction replicates, the specific problems driving severity differ between models---consistent with model-specific attention patterns rather than a universal per-problem vulnerability ranking. % exp_id: cross_model_analysis.json (spearman_rho=1.0, gradient_permutation_p=0.043, per_problem_concordance_p=0.926, mean_rho=-0.107)
8	
9	\paragraph{Random eviction control.}
10	As a control, random eviction on Qwen yields no systematic phase gradient at three of four sparsity levels (3/4 FAIL), mirroring DeepSeek's 4/4 FAIL pattern. At $s{=}0.30$, Qwen random produces a borderline PASS (permutation $p = 0.012$) but with negligible effect size ($d_z = -0.04$, CI spans zero), indicating no meaningful phase modulation. % exp_id: bf16_qw_rand_s015..s030; source: experiment_summary_table.json
11	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10233ec7-5d03-448a-9224-b6173ea0cbe8",
  "uuid": "0dd160bb-fc3d-4f70-8e96-36bca65660fc",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_results.tex",
      "content": "% Appendix: supplementary results details\n\n\\section{Cross-Model Replication Details}\n\\label{app:cross-model-details}\n\n\\paragraph{Per-problem concordance.}\nThe per-problem concordance across models is not significant (mean $\\rho = -0.11$, $p = 0.926$), indicating that while the aggregate gradient direction replicates, the specific problems driving severity differ between models---consistent with model-specific attention patterns rather than a universal per-problem vulnerability ranking. % exp_id: cross_model_analysis.json (spearman_rho=1.0, gradient_permutation_p=0.043, per_problem_concordance_p=0.926, mean_rho=-0.107)\n\n\\paragraph{Random eviction control.}\nAs a control, random eviction on Qwen yields no systematic phase gradient at three of four sparsity levels (3/4 FAIL), mirroring DeepSeek's 4/4 FAIL pattern. At $s{=}0.30$, Qwen random produces a borderline PASS (permutation $p = 0.012$) but with negligible effect size ($d_z = -0.04$, CI spans zero), indicating no meaningful phase modulation. % exp_id: bf16_qw_rand_s015..s030; source: experiment_summary_table.json\n",
      "numLines": 11,
      "startLine": 1,
      "totalLines": 11
    }
  }
}
```

</details>

---

### Tool call

_source line 42_

<details open><summary>🔧 Tool call — Read · `toolu_01XNKaV3sXNRdiVDgFGyWaS2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_disc_analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10233ec7-5d03-448a-9224-b6173ea0cbe8",
  "uuid": "0a492582-9bbc-40cf-9171-0bc35794fe5e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FsD7CPPuwEQCkUJRcvGJo5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10685,
      "cache_read_input_tokens": 24898,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10685
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

_source line 43 · 2026-05-14T21:49:36.075Z_

<details><summary>↩ Tool result · `toolu_01XNKaV3sXNRdiVDgFGyWaS2`</summary>

```text
1	\section{Discrimination Collapse Details}
2	\label{app:discrimination-collapse-details}
3	
4	This cross-model consistency (Table~\ref{tab:discrimination-metrics-full}) establishes discrimination collapse as a robust consequence of compound sparsity. When importance scores lose discriminative power, thresholding the bottom-$s$ fraction becomes noise-sensitive: small perturbations change which positions cross the eviction boundary. In the limit of perfectly uniform scores, importance-based eviction degenerates into an arbitrary selection functionally equivalent to biased random eviction. The same pattern holds under random eviction (DeepSeek: $-0.031$ to $-0.073$; Qwen: $-0.019$ to $-0.045$), confirming that discrimination collapse is a consequence of head pruning \emph{per se}, not of the eviction strategy. % exp_id: c4_entropy_deepseek, c4_entropy_qwen
5	
6	
7	\section{Extended Discussion}
8	\label{app:extended-discussion}
9	
10	\paragraph{On the predictability of phase-modulated severity.}
11	The compound interaction is not uniformly fragile---it is selectively fragile in a phase-dependent manner ($\widetilde{\mathrm{II}}_{\text{high}} < 0.06$ at $s \leq 0.30$; at $s = 0.35$, high-phase II rises to $0.105$ in a supplementary experiment, indicating onset of compound interaction even in high-sparsity phases at extreme pruning rates). % exp_id: bf16_importance_s015..s030, bf16_ds_imp_s035; high-phase medians: 0.006, 0.015, 0.032, 0.053; s035 II_high=0.1051
12	
13	\paragraph{Random masking as falsification control.}
14	Random eviction fails 7/8 paired permutation tests across both models; the single exception (Qwen $s{=}0.30$, $p{=}0.012$) exhibits negligible effect size ($d_z{=}{-}0.04$). The absence of a phase gradient under random masking isolates the amplification as strategy-specific. % exp_id: bf16_ds_rand_s015..s030, bf16_qw_rand_s015..s030
15	
16	\paragraph{Entropy mechanism boundary conditions.}
17	Directly measuring per-head entropy shifts across architecturally distinct models---and identifying what training-time properties determine whether entropy concentrates or disperses under head pruning---would clarify the boundary conditions of the full mechanism.
18	
19	
20	\section{Extended Limitations}
21	\label{app:limitations}
22	
23	\paragraph{Model scale.}
24	All experiments are conducted at the 7B parameter scale.
25	Whether the phase-modulated severity patterns persist, amplify, or attenuate at larger scales (e.g., 70B) remains untested.
26	Larger models may exhibit different attention redundancy structures that alter the discrimination collapse dynamics (and the model-dependent entropy component may behave differently at scale).
27	% REVIEWER-ATTACK: "7B is too small to be relevant for production."
28	% REBUTTAL: 7B is the most-deployed scale for on-device and cost-constrained serving—exactly where compound sparsity is needed. The mechanism (entropy-discrimination collapse) is scale-agnostic in principle. Scaling experiments are future work.
29	
30	\paragraph{Architectural scope.}
31	Our two models---DeepSeek-R1-Distill-Qwen-7B and Qwen2.5-7B-Instruct---share the Qwen2ForCausalLM architecture.
32	The cross-model replication (\S\ref{sec:cross-model}) establishes that the findings are not artifacts of a single model's weights, though both models share the same Qwen2ForCausalLM architecture.
33	Cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, \S\ref{sec:cross-arch}) provides partial support: the directional pattern is qualitatively consistent but the interaction magnitude is substantially weaker than in Qwen2-based architectures, and random pruning also exhibits a non-trivial phase gradient on LLaMA. Further validation on more diverse architectures (e.g., Mistral, multi-latent attention architectures) is needed to establish the generality of the full interaction.
34	% REVIEWER-ATTACK: "Cross-model ≠ cross-architecture. Both are Qwen2ForCausalLM."
35	% REBUTTAL: We now include cross-architecture validation on LlamaForCausalLM (\S\ref{sec:cross-arch}), which shows a qualitatively consistent but substantially weaker pattern. We use qualified language ("partially supports") rather than claiming full generalization.
36	
37	\paragraph{Task coverage.}
38	We evaluate exclusively on MATH-500, a mathematical reasoning benchmark.
39	Different reasoning tasks---code generation, commonsense reasoning, multi-hop question answering---may induce different phase structures with different sparsity distributions, potentially altering the severity gradient profile.
40	Generalizing the phase-strategy interaction to broader reasoning domains is an important next step.
41	% REVIEWER-ATTACK: "Only MATH-500. How do we know this isn't a math-specific artifact?"
42	% REBUTTAL: The mechanism (entropy-discrimination collapse under head pruning) depends on attention distribution properties, not math-specific features. MATH-500 is a standard benchmark with diverse difficulty. However, different reasoning tasks may induce different phase structures—we state this limitation explicitly rather than overclaiming.
43	
44	\paragraph{Statistical scope.}
45	Bootstrap confidence intervals use $B{=}10{,}000$ resamples. The paired permutation test yields $n{=}49$ paired problems for DeepSeek (1 excluded) and $n{=}46$ for Qwen (4 excluded). % exp_id: cohens_d_bf16.json, cohens_d_bf16_qwen.json
46	The severity difference distribution is right-skewed (mean/median ratio ${\sim}1.6{:}1$ at $s{=}0.30$), motivating our use of medians and nonparametric tests rather than parametric alternatives. % exp_id: bf16_importance_s030; mean_diff=22.94, median_diff=14.59 (segment-level). Per-problem paired: median_diff=9.9436 at s030
47	All four permutation tests reject $H_0$ after Bonferroni correction ($p_{\text{Bonf}} < 0.005$; Table~\ref{tab:permutation}), with CI lower bounds increasing from $0.19$ to $6.70$---confirming the effect direction at every sparsity level. The permutation CIs at higher sparsity are wider (e.g., $[6.70,\; 16.29]$ at $s{=}0.30$), reflecting genuine variance in per-problem severity amplification. % exp_id: permutation_test_results.json; permutation CIs: s015=[0.19,0.62], s020=[0.69,1.49], s025=[1.66,6.64], s030=[6.70,16.29]
48	
49	A notable exception among the random baselines is the Qwen random condition at $s{=}0.30$, which yields a statistically significant result ($p{=}0.012$) despite negligible effect size ($d_z{=}{-}0.04$, bootstrap CI excluding zero). % exp_id: qw_rand_s030; B=10000, p=0.012, d=-0.035, negligible
50	This case illustrates that dichotomous significance testing can flag effects of no practical magnitude---reinforcing the importance of reporting effect sizes and confidence intervals alongside $p$-values.
51	
52	\paragraph{Sparsity range.}
53	Our experiments span $s \in \{0.15, 0.20, 0.25, 0.30\}$, a moderate range representative of practical deployment targets.
54	More extreme sparsity ($s > 0.50$) may exhibit qualitatively different interaction dynamics---the sub-exponential growth pattern suggests the severity gradient may plateau, but this remains unverified.
55	Conversely, the lower boundary at which phase-modulated amplification first emerges is not yet characterized.
56	% REVIEWER-ATTACK: "Why not test higher sparsity? 0.30 is conservative."
57	% REBUTTAL: Our focus is on the practically relevant regime where models retain usable quality. At s>0.30 both strategies degrade severely, making II measurement less informative. The sub-exponential growth (C6, $\Delta$ growth rate $3.8{\times} \to 4.8{\times} \to 2.0{\times}$) suggests saturation at higher sparsity, but confirming this is future work.
58	
59	\paragraph{No throughput evaluation.}
60	We do not report inference throughput or latency, which are necessary for deployment analysis but orthogonal to our severity characterization.
61	% REVIEWER-ATTACK: "No system evaluation. How do we know the severity amplification matters for real deployment?"
62	% REBUTTAL: This is an empirical finding paper, not a method/system paper. The contribution is characterizing *what happens* (phase-modulated severity) and *why* (entropy-discrimination collapse), not building a system to fix it. Phase-gated controllers are explicitly scoped as future work. The finding is actionable regardless: any compound sparsity deployment should be aware of phase-dependent severity.
63	
64	% Entropy redistribution analysis moved to main text \S\ref{sec:entropy-redistribution}
65	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10233ec7-5d03-448a-9224-b6173ea0cbe8",
  "uuid": "c10b836b-9eb5-4606-a499-dcf6546113b0",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_disc_analysis.tex",
      "content": "\\section{Discrimination Collapse Details}\n\\label{app:discrimination-collapse-details}\n\nThis cross-model consistency (Table~\\ref{tab:discrimination-metrics-full}) establishes discrimination collapse as a robust consequence of compound sparsity. When importance scores lose discriminative power, thresholding the bottom-$s$ fraction becomes noise-sensitive: small perturbations change which positions cross the eviction boundary. In the limit of perfectly uniform scores, importance-based eviction degenerates into an arbitrary selection functionally equivalent to biased random eviction. The same pattern holds under random eviction (DeepSeek: $-0.031$ to $-0.073$; Qwen: $-0.019$ to $-0.045$), confirming that discrimination collapse is a consequence of head pruning \\emph{per se}, not of the eviction strategy. % exp_id: c4_entropy_deepseek, c4_entropy_qwen\n\n\n\\section{Extended Discussion}\n\\label{app:extended-discussion}\n\n\\paragraph{On the predictability of phase-modulated severity.}\nThe compound interaction is not uniformly fragile---it is selectively fragile in a phase-dependent manner ($\\widetilde{\\mathrm{II}}_{\\text{high}} < 0.06$ at $s \\leq 0.30$; at $s = 0.35$, high-phase II rises to $0.105$ in a supplementary experiment, indicating onset of compound interaction even in high-sparsity phases at extreme pruning rates). % exp_id: bf16_importance_s015..s030, bf16_ds_imp_s035; high-phase medians: 0.006, 0.015, 0.032, 0.053; s035 II_high=0.1051\n\n\\paragraph{Random masking as falsification control.}\nRandom eviction fails 7/8 paired permutation tests across both models; the single exception (Qwen $s{=}0.30$, $p{=}0.012$) exhibits negligible effect size ($d_z{=}{-}0.04$). The absence of a phase gradient under random masking isolates the amplification as strategy-specific. % exp_id: bf16_ds_rand_s015..s030, bf16_qw_rand_s015..s030\n\n\\paragraph{Entropy mechanism boundary conditions.}\nDirectly measuring per-head entropy shifts across architecturally distinct models---and identifying what training-time properties determine whether entropy concentrates or disperses under head pruning---would clarify the boundary conditions of the full mechanism.\n\n\n\\section{Extended Limitations}\n\\label{app:limitations}\n\n\\paragraph{Model scale.}\nAll experiments are conducted at the 7B parameter scale.\nWhether the phase-modulated severity patterns persist, amplify, or attenuate at larger scales (e.g., 70B) remains untested.\nLarger models may exhibit different attention redundancy structures that alter the discrimination collapse dynamics (and the model-dependent entropy component may behave differently at scale).\n% REVIEWER-ATTACK: \"7B is too small to be relevant for production.\"\n% REBUTTAL: 7B is the most-deployed scale for on-device and cost-constrained serving—exactly where compound sparsity is needed. The mechanism (entropy-discrimination collapse) is scale-agnostic in principle. Scaling experiments are future work.\n\n\\paragraph{Architectural scope.}\nOur two models---DeepSeek-R1-Distill-Qwen-7B and Qwen2.5-7B-Instruct---share the Qwen2ForCausalLM architecture.\nThe cross-model replication (\\S\\ref{sec:cross-model}) establishes that the findings are not artifacts of a single model's weights, though both models share the same Qwen2ForCausalLM architecture.\nCross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, \\S\\ref{sec:cross-arch}) provides partial support: the directional pattern is qualitatively consistent but the interaction magnitude is substantially weaker than in Qwen2-based architectures, and random pruning also exhibits a non-trivial phase gradient on LLaMA. Further validation on more diverse architectures (e.g., Mistral, multi-latent attention architectures) is needed to establish the generality of the full interaction.\n% REVIEWER-ATTACK: \"Cross-model ≠ cross-architecture. Both are Qwen2ForCausalLM.\"\n% REBUTTAL: We now include cross-architecture validation on LlamaForCausalLM (\\S\\ref{sec:cross-arch}), which shows a qualitatively consistent but substantially weaker pattern. We use qualified language (\"partially supports\") rather than claiming full generalization.\n\n\\paragraph{Task coverage.}\nWe evaluate exclusively on MATH-500, a mathematical reasoning benchmark.\nDifferent reasoning tasks---code generation, commonsense reasoning, multi-hop question answering---may induce different phase structures with different sparsity distributions, potentially altering the severity gradient profile.\nGeneralizing the phase-strategy interaction to broader reasoning domains is an important next step.\n% REVIEWER-ATTACK: \"Only MATH-500. How do we know this isn't a math-specific artifact?\"\n% REBUTTAL: The mechanism (entropy-discrimination collapse under head pruning) depends on attention distribution properties, not math-specific features. MATH-500 is a standard benchmark with diverse difficulty. However, different reasoning tasks may induce different phase structures—we state this limitation explicitly rather than overclaiming.\n\n\\paragraph{Statistical scope.}\nBootstrap confidence intervals use $B{=}10{,}000$ resamples. The paired permutation test yields $n{=}49$ paired problems for DeepSeek (1 excluded) and $n{=}46$ for Qwen (4 excluded). % exp_id: cohens_d_bf16.json, cohens_d_bf16_qwen.json\nThe severity difference distribution is right-skewed (mean/median ratio ${\\sim}1.6{:}1$ at $s{=}0.30$), motivating our use of medians and nonparametric tests rather than parametric alternatives. % exp_id: bf16_importance_s030; mean_diff=22.94, median_diff=14.59 (segment-level). Per-problem paired: median_diff=9.9436 at s030\nAll four permutation tests reject $H_0$ after Bonferroni correction ($p_{\\text{Bonf}} < 0.005$; Table~\\ref{tab:permutation}), with CI lower bounds increasing from $0.19$ to $6.70$---confirming the effect direction at every sparsity level. The permutation CIs at higher sparsity are wider (e.g., $[6.70,\\; 16.29]$ at $s{=}0.30$), reflecting genuine variance in per-problem severity amplification. % exp_id: permutation_test_results.json; permutation CIs: s015=[0.19,0.62], s020=[0.69,1.49], s025=[1.66,6.64], s030=[6.70,16.29]\n\nA notable exception among the random baselines is the Qwen random condition at $s{=}0.30$, which yields a statistically significant result ($p{=}0.012$) despite negligible effect size ($d_z{=}{-}0.04$, bootstrap CI excluding zero). % exp_id: qw_rand_s030; B=10000, p=0.012, d=-0.035, negligible\nThis case illustrates that dichotomous significance testing can flag effects of no practical magnitude---reinforcing the importance of reporting effect sizes and confidence intervals alongside $p$-values.\n\n\\paragraph{Sparsity range.}\nOur experiments span $s \\in \\{0.15, 0.20, 0.25, 0.30\\}$, a moderate range representative of practical deployment targets.\nMore extreme sparsity ($s > 0.50$) may exhibit qualitatively different interaction dynamics---the sub-exponential growth pattern suggests the severity gradient may plateau, but this remains unverified.\nConversely, the lower boundary at which phase-modulated amplification first emerges is not yet characterized.\n% REVIEWER-ATTACK: \"Why not test higher sparsity? 0.30 is conservative.\"\n% REBUTTAL: Our focus is on the practically relevant regime where models retain usable quality. At s>0.30 both strategies degrade severely, making II measurement less informative. The sub-exponential growth (C6, $\\Delta$ growth rate $3.8{\\times} \\to 4.8{\\times} \\to 2.0{\\times}$) suggests saturation at higher sparsity, but confirming this is future work.\n\n\\paragraph{No throughput evaluation.}\nWe do not report inference throughput or latency, which are necessary for deployment analysis but orthogonal to our severity characterization.\n% REVIEWER-ATTACK: \"No system evaluation. How do we know the severity amplification matters for real deployment?\"\n% REBUTTAL: This is an empirical finding paper, not a method/system paper. The contribution is characterizing *what happens* (phase-modulated severity) and *why* (entropy-discrimination collapse), not building a system to fix it. Phase-gated controllers are explicitly scoped as future work. The finding is actionable regardless: any compound sparsity deployment should be aware of phase-dependent severity.\n\n% Entropy redistribution analysis moved to main text \\S\\ref{sec:entropy-redistribution}\n",
      "numLines": 65,
      "startLine": 1,
      "totalLines": 65
    }
  }
}
```

</details>

---

### Tool call

_source line 44_

<details open><summary>🔧 Tool call — Read · `toolu_01Ba3zCotyz4Z21GeoDS5mev`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_moved.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10233ec7-5d03-448a-9224-b6173ea0cbe8",
  "uuid": "fc01f438-106f-49b9-abf5-f27411cdffad",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FsD7CPPuwEQCkUJRcvGJo5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10685,
      "cache_read_input_tokens": 24898,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10685
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

_source line 45 · 2026-05-14T21:49:36.776Z_

<details><summary>↩ Tool result · `toolu_01Ba3zCotyz4Z21GeoDS5mev`</summary>

```text
1	% Content moved from main body to appendix:
2	% - Phase-strategy crossover details (from results §5.3)
3	% - Cross-model replication details with tables/figures (from results §5.4)
4	% - Permutation test details with table/forest plot (from results §5.5)
5	% - Full entropy-discrimination collapse analysis with tables (from analysis §6)
6	% Main body §6 (analysis.tex) contains a condensed summary referencing these tables.
7	
8	\section{Phase-Strategy Crossover Details}
9	\label{app:crossover-details}
10	
11	At $s{=}0.25$, a strategy ranking reversal emerges (Figure~\ref{fig:crossover}): importance-based eviction yields \emph{lower} II than random in the high-sparsity phase ($0.032$ vs.\ $0.818$) but \emph{higher} II in the low-sparsity phase ($7.196$ vs.\ $1.363$---a $5.3{\times}$ reversal). This crossover is present at all four sparsity levels, with reversal magnitude of $3.9{\times}$ at $s{=}0.15$, $5.4{\times}$ at $s{=}0.20$, $5.3{\times}$ at $s{=}0.25$, and $3.6{\times}$ at $s{=}0.30$ (as random eviction severity also rises). The reversal arises because head pruning redistributes attention mass, altering importance rankings in a way that couples the two sparsity mechanisms in low-sparsity phases (\S\ref{sec:discrimination-collapse}). % exp_id: bf16_importance_s025, bf16_ds_rand_s025; source: experiment_summary_table.json; 7.196/1.363=5.28
12	
13	\begin{figure}[t]
14	\centering
15	\includegraphics[width=\columnwidth]{fig3_crossover.pdf}
16	\caption{Strategy-dependent crossover at $s{=}0.25$. Grouped bar chart of median II by eviction strategy and reasoning phase. Importance-based eviction outperforms random in the high-sparsity phase but produces $5.3{\times}$ higher II in the low-sparsity phase, reversing the strategy ranking.}
17	\label{fig:crossover}
18	\end{figure}
19	
20	
21	\section{Cross-Model Replication Details}
22	\label{app:cross-model-details}
23	
24	Both models share the Qwen2ForCausalLM backbone (28 layers, 28 heads, 4-group GQA) but differ in training: DeepSeek uses reasoning distillation from DeepSeek-R1, while Qwen2.5 uses standard instruction tuning without explicit reasoning delimiters. This controlled comparison isolates the effect of training methodology on the compound sparsity interaction.
25	
26	Despite lacking explicit \texttt{&lt;think>} delimiters, Qwen2.5-7B-Instruct exhibits sufficient variation in attention sparsity to permit phase segmentation via the same quantile-based method (\S\ref{sec:phase-segmentation}). Four of the 50 problems are excluded due to degenerate phase assignments, yielding $n{=}46$ valid problems for Qwen (vs.\ $n{=}49$ for DeepSeek).
27	
28	Table~\ref{tab:cross-model} reports the cross-model comparison. Qwen reproduces the monotonic severity gradient at ${\sim}1/5$ of DeepSeek's magnitude. Figure~\ref{fig:cross-model} visualizes this comparison. % exp_id: cross_model_analysis.json; cohens_d_bf16_qwen.json
29	
30	\begin{table}[t]
31	\centering
32	\small
33	\caption{Cross-model comparison of median compound severity difference ($\Delta$) under importance-based eviction.}
34	\label{tab:cross-model}
35	\begin{tabular}{@{}lcccc@{}}
36	\toprule
37	Model & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\
38	\midrule
39	DeepSeek-R1-Distill-Qwen-7B & 0.39 & 1.48 & 7.16 & 14.59 \\ % exp_id: bf16_importance_s015..s030
40	Qwen2.5-7B-Instruct         & 0.04 & 0.23 & 1.27 & 2.94 \\ % exp_id: bf16_qw_imp_s015..s030
41	\bottomrule
42	\end{tabular}
43	\end{table}
44	
45	\begin{figure}[t]
46	\centering
47	\includegraphics[width=\columnwidth]{fig5_crossmodel.pdf}
48	\caption{Cross-model comparison of the median severity difference under importance-based eviction. Both DeepSeek (solid) and Qwen (dashed) exhibit monotonically increasing $\Delta$ with sparsity; Qwen's magnitude is approximately one-fifth of DeepSeek's.} % exp_id: bf16_importance_s015..s030, bf16_qw_imp_s015..s030
49	\label{fig:cross-model}
50	\end{figure}
51	
52	\paragraph{Per-problem concordance.}
53	The per-problem concordance across models is not significant (mean $\rho = -0.11$, $p = 0.926$), indicating that while the aggregate gradient direction replicates, the specific problems driving severity differ between models---consistent with model-specific attention patterns rather than a universal per-problem vulnerability ranking. % exp_id: cross_model_analysis.json (spearman_rho=1.0, gradient_permutation_p=0.043, per_problem_concordance_p=0.926, mean_rho=-0.107)
54	
55	\paragraph{Random eviction control.}
56	As a control, random eviction on Qwen yields no systematic phase gradient at three of four sparsity levels (3/4 FAIL), mirroring DeepSeek's 4/4 FAIL pattern. At $s{=}0.30$, Qwen random produces a borderline PASS (permutation $p = 0.012$) but with negligible effect size ($d_z = -0.04$, CI spans zero), indicating no meaningful phase modulation. % exp_id: bf16_qw_rand_s015..s030; source: experiment_summary_table.json
57	
58	
59	\section{Permutation Test Details}
60	\label{app:permutation-details}
61	
62	For each problem $i$ and sparsity level $s$, we compute the compound severity difference $\Delta_i^{(\text{strat})} = \mathrm{II}_{\textit{low},i} - \mathrm{II}_{\textit{high},i}$ under each eviction strategy. The test statistic is the median of the paired difference $\widetilde{\Delta} = \text{median}_i\!\bigl(\Delta_i^{(\text{imp})} - \Delta_i^{(\text{rand})}\bigr)$, measuring whether importance-based eviction produces systematically larger phase-dependent severity than random eviction. We permute strategy labels $10{,}000$ times to construct the null distribution and apply Bonferroni correction for 4 sparsity-level comparisons.
63	
64	Per-problem distributions of the paired severity difference $\Delta_i = \mathrm{II}_{\textit{low},i} - \mathrm{II}_{\textit{high},i}$ under importance-based eviction are right-skewed at all sparsity levels, with mean/median ratios ranging from $1.2{\times}$ ($s{=}0.15$) to $1.6{\times}$ ($s{=}0.30$) for DeepSeek and $1.1{\times}$ to $1.4{\times}$ for Qwen.
65	
66	The permutation null distributions are approximately symmetric around zero at all sparsity levels. At $s{=}0.15$, the observed statistic falls at the $99.92$th percentile of the null ($p_{\text{Bonf}} = 0.0032$); at $s \geq 0.20$, no permutation exceeds the observed statistic.
67	
68	Table~\ref{tab:permutation} reports the results. All four sparsity levels reject $H_0$ after Bonferroni correction ($p_{\text{Bonf}} < 0.005$), with observed median differences increasing monotonically from $0.37$ at $s{=}0.15$ to $9.85$ at $s{=}0.30$. The monotonic growth of both the point estimate and the CI lower bound ($0.19 \to 0.69 \to 1.66 \to 6.70$) confirms that compound severity amplification strengthens with sparsity---not merely in central tendency but also in worst-case lower bounds. Figure~\ref{fig:permtest-forest} presents these results as a forest plot. % exp_id: deepseek_bf16_permtest; source: permutation_test_results.json
69	
70	\begin{table}[t]
71	\centering
72	\small
73	\caption{Paired permutation test for compound severity: importance vs.\ random eviction on DeepSeek-R1-Distill-Qwen-7B ($n{=}49$, $10{,}000$ permutations, Bonferroni-corrected).}
74	\label{tab:permutation}
75	\begin{tabular}{@{}rrcl@{}}
76	\toprule
77	$s$ & Observed $\widetilde{\Delta}$ & 95\% CI & $p_{\text{Bonf}}$ \\
78	\midrule
79	0.15 & 0.37 & $[0.19,\; 0.62]$ & 0.0032 \\ % exp_id: deepseek_bf16_permtest_s015
80	0.20 & 0.97 & $[0.69,\; 1.49]$ & ${<}\,0.001$ \\ % exp_id: deepseek_bf16_permtest_s020
81	0.25 & 3.34 & $[1.66,\; 6.64]$ & ${<}\,0.001$ \\ % exp_id: deepseek_bf16_permtest_s025
82	0.30 & 9.85 & $[6.70,\; 16.29]$ & ${<}\,0.001$ \\ % exp_id: deepseek_bf16_permtest_s030
83	\bottomrule
84	\end{tabular}
85	\end{table}
86	
87	\begin{figure}[t]
88	\centering
89	\includegraphics[width=\columnwidth]{fig4_bootstrap.pdf}
90	\caption{Forest plot of permutation test results. Horizontal bars show 95\% permutation CIs; diamonds mark observed median differences $\widetilde{\Delta}$. All CIs lie entirely above zero, confirming significant strategy-dependent severity at every sparsity level.}
91	\label{fig:permtest-forest}
92	\end{figure}
93	
94	
95	\section{Analysis: Entropy-Discrimination Collapse}
96	\label{app:analysis}
97	
98	\subsection{Discrimination Collapse}
99	\label{sec:discrimination-collapse}
100	
101	Head pruning reduces the number of heads contributing to cumulative importance scores, flattening the score distribution. Table~\ref{tab:discrimination-metrics-full} quantifies this effect: the Gini coefficient decreases by $0.030$--$0.081$ (DeepSeek) and $0.010$--$0.020$ (Qwen) after pruning, with consistent negative deltas across all 16 conditions (both models $\times$ 4 sparsity levels $\times$ 2 strategies). The CV delta is likewise negative in all 8 importance-based conditions. The same pattern holds under random eviction, confirming that discrimination collapse is a consequence of head pruning \emph{per se}, not of the eviction strategy. % exp_id: c4_entropy_deepseek, c4_entropy_qwen
102	
103	\begin{table}[t]
104	\centering
105	\caption{Discrimination collapse under importance-based eviction. $\Delta\mathrm{Gini}$ and $\Delta\mathrm{CV}$ are post-pruning minus baseline; negative values indicate reduced discriminative power.}
106	\label{tab:discrimination-metrics-full}
107	\small
108	\begin{tabular}{llrr}
109	\toprule
110	Model & $s$ & $\Delta\mathrm{Gini}$ & $\Delta\mathrm{CV}$ \\
111	\midrule
112	DeepSeek & $0.15$ & $-0.030$ & $-0.56$ \\
113	DeepSeek & $0.20$ & $-0.040$ & $-0.77$ \\
114	DeepSeek & $0.25$ & $-0.065$ & $-1.29$ \\
115	DeepSeek & $0.30$ & $-0.081$ & $-1.66$ \\
116	\midrule
117	Qwen & $0.15$ & $-0.010$ & $-0.05$ \\
118	Qwen & $0.20$ & $-0.012$ & $-0.21$ \\
119	Qwen & $0.25$ & $-0.010$ & $-1.49$ \\
120	Qwen & $0.30$ & $-0.020$ & $-1.14$ \\
121	\bottomrule
122	\end{tabular}
123	\end{table}
124	
125	When importance scores lose discriminability, thresholding degenerates into noise-sensitive selection---functionally approaching biased random eviction. This is phase-dependent: in low-sparsity phases, attention is already broadly distributed, so pruning-induced flattening has maximum impact; in high-sparsity phases, concentration is preserved. Random eviction is immune because its decisions are independent of score quality, explaining $G \approx 1$. % exp_id: c4_entropy_deepseek, c4_entropy_qwen
126	
127	\subsection{Entropy Redistribution}
128	\label{sec:entropy-redistribution}
129	
130	Beyond discrimination collapse, we examine whether head pruning also redistributes the attention entropy of surviving heads. We measure the mean attention entropy per head:
131	\begin{equation}
132	    \mathcal{H}_i^{(h)} = -\sum_{j=1}^{T} a_{ij}^{(h)} \log a_{ij}^{(h)}
133	    \label{eq:attn-entropy}
134	\end{equation}
135	and compute $\Delta\mathcal{H}$ as the change from baseline (no pruning) to the pruned condition.
136	
137	For DeepSeek under importance-based eviction, the entropy delta is consistently negative across all four sparsity levels ($\Delta\mathcal{H} \in [-0.047, -0.040]$; Table~\ref{tab:entropy-deltas}), indicating that importance-based pruning systematically selects heads whose removal concentrates attention in the surviving heads, reinforcing discrimination collapse. % exp_id: c4_entropy_deepseek
138	
139	For Qwen, the entropy pattern only partially replicates. The delta is negative at $s{=}0.15$ ($\Delta\mathcal{H} = -0.073$) and $s{=}0.20$ ($-0.076$), consistent with DeepSeek. However, at $s{=}0.25$, the delta reverses to $+0.045$, with 22 of 30 problems showing positive entropy change. At $s{=}0.30$, the delta is near zero ($-0.007$). The $s{=}0.25$ reversal is systematic rather than a statistical artifact: it is consistent across all three reasoning phases (low: $+0.042$, mid: $+0.034$, high: $+0.017$). We interpret this as a genuine model-specific difference, possibly arising from distinct head specialization patterns: Qwen's instruction tuning (vs.\ DeepSeek's distillation-based training) may produce head configurations where removing 25\% of heads triggers compensatory broadening rather than concentration. % exp_id: c4_entropy_qwen
140	
141	We characterize discrimination collapse as the robust, model-independent driver of the phase-strategy interaction, with entropy redistribution as a secondary amplifier that is consistent in DeepSeek but model-dependent in Qwen.
142	
143	\begin{table}[t]
144	\centering
145	\caption{Attention entropy deltas ($\Delta\mathcal{H}$) under importance-based eviction. DeepSeek shows consistent entropy compression; Qwen partially replicates with a reversal at $s{=}0.25$.}
146	\label{tab:entropy-deltas}
147	\small
148	\begin{tabular}{llr}
149	\toprule
150	Model & $s$ & $\Delta\mathcal{H}$ \\
151	\midrule
152	DeepSeek & $0.15$ & $-0.040$ \\
153	DeepSeek & $0.20$ & $-0.047$ \\
154	DeepSeek & $0.25$ & $-0.045$ \\
155	DeepSeek & $0.30$ & $-0.044$ \\
156	\midrule
157	Qwen & $0.15$ & $-0.073$ \\
158	Qwen & $0.20$ & $-0.076$ \\
159	Qwen & $0.25$ & $+0.045$ \\
160	Qwen & $0.30$ & $-0.007$ \\
161	\bottomrule
162	\end{tabular}
163	\end{table}
164	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10233ec7-5d03-448a-9224-b6173ea0cbe8",
  "uuid": "0f00ce7a-9c41-4482-88fb-c294d711fd6b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_moved.tex",
      "content": "% Content moved from main body to appendix:\n% - Phase-strategy crossover details (from results §5.3)\n% - Cross-model replication details with tables/figures (from results §5.4)\n% - Permutation test details with table/forest plot (from results §5.5)\n% - Full entropy-discrimination collapse analysis with tables (from analysis §6)\n% Main body §6 (analysis.tex) contains a condensed summary referencing these tables.\n\n\\section{Phase-Strategy Crossover Details}\n\\label{app:crossover-details}\n\nAt $s{=}0.25$, a strategy ranking reversal emerges (Figure~\\ref{fig:crossover}): importance-based eviction yields \\emph{lower} II than random in the high-sparsity phase ($0.032$ vs.\\ $0.818$) but \\emph{higher} II in the low-sparsity phase ($7.196$ vs.\\ $1.363$---a $5.3{\\times}$ reversal). This crossover is present at all four sparsity levels, with reversal magnitude of $3.9{\\times}$ at $s{=}0.15$, $5.4{\\times}$ at $s{=}0.20$, $5.3{\\times}$ at $s{=}0.25$, and $3.6{\\times}$ at $s{=}0.30$ (as random eviction severity also rises). The reversal arises because head pruning redistributes attention mass, altering importance rankings in a way that couples the two sparsity mechanisms in low-sparsity phases (\\S\\ref{sec:discrimination-collapse}). % exp_id: bf16_importance_s025, bf16_ds_rand_s025; source: experiment_summary_table.json; 7.196/1.363=5.28\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig3_crossover.pdf}\n\\caption{Strategy-dependent crossover at $s{=}0.25$. Grouped bar chart of median II by eviction strategy and reasoning phase. Importance-based eviction outperforms random in the high-sparsity phase but produces $5.3{\\times}$ higher II in the low-sparsity phase, reversing the strategy ranking.}\n\\label{fig:crossover}\n\\end{figure}\n\n\n\\section{Cross-Model Replication Details}\n\\label{app:cross-model-details}\n\nBoth models share the Qwen2ForCausalLM backbone (28 layers, 28 heads, 4-group GQA) but differ in training: DeepSeek uses reasoning distillation from DeepSeek-R1, while Qwen2.5 uses standard instruction tuning without explicit reasoning delimiters. This controlled comparison isolates the effect of training methodology on the compound sparsity interaction.\n\nDespite lacking explicit \\texttt{&lt;think>} delimiters, Qwen2.5-7B-Instruct exhibits sufficient variation in attention sparsity to permit phase segmentation via the same quantile-based method (\\S\\ref{sec:phase-segmentation}). Four of the 50 problems are excluded due to degenerate phase assignments, yielding $n{=}46$ valid problems for Qwen (vs.\\ $n{=}49$ for DeepSeek).\n\nTable~\\ref{tab:cross-model} reports the cross-model comparison. Qwen reproduces the monotonic severity gradient at ${\\sim}1/5$ of DeepSeek's magnitude. Figure~\\ref{fig:cross-model} visualizes this comparison. % exp_id: cross_model_analysis.json; cohens_d_bf16_qwen.json\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-model comparison of median compound severity difference ($\\Delta$) under importance-based eviction.}\n\\label{tab:cross-model}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nModel & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\\\\n\\midrule\nDeepSeek-R1-Distill-Qwen-7B & 0.39 & 1.48 & 7.16 & 14.59 \\\\ % exp_id: bf16_importance_s015..s030\nQwen2.5-7B-Instruct         & 0.04 & 0.23 & 1.27 & 2.94 \\\\ % exp_id: bf16_qw_imp_s015..s030\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig5_crossmodel.pdf}\n\\caption{Cross-model comparison of the median severity difference under importance-based eviction. Both DeepSeek (solid) and Qwen (dashed) exhibit monotonically increasing $\\Delta$ with sparsity; Qwen's magnitude is approximately one-fifth of DeepSeek's.} % exp_id: bf16_importance_s015..s030, bf16_qw_imp_s015..s030\n\\label{fig:cross-model}\n\\end{figure}\n\n\\paragraph{Per-problem concordance.}\nThe per-problem concordance across models is not significant (mean $\\rho = -0.11$, $p = 0.926$), indicating that while the aggregate gradient direction replicates, the specific problems driving severity differ between models---consistent with model-specific attention patterns rather than a universal per-problem vulnerability ranking. % exp_id: cross_model_analysis.json (spearman_rho=1.0, gradient_permutation_p=0.043, per_problem_concordance_p=0.926, mean_rho=-0.107)\n\n\\paragraph{Random eviction control.}\nAs a control, random eviction on Qwen yields no systematic phase gradient at three of four sparsity levels (3/4 FAIL), mirroring DeepSeek's 4/4 FAIL pattern. At $s{=}0.30$, Qwen random produces a borderline PASS (permutation $p = 0.012$) but with negligible effect size ($d_z = -0.04$, CI spans zero), indicating no meaningful phase modulation. % exp_id: bf16_qw_rand_s015..s030; source: experiment_summary_table.json\n\n\n\\section{Permutation Test Details}\n\\label{app:permutation-details}\n\nFor each problem $i$ and sparsity level $s$, we compute the compound severity difference $\\Delta_i^{(\\text{strat})} = \\mathrm{II}_{\\textit{low},i} - \\mathrm{II}_{\\textit{high},i}$ under each eviction strategy. The test statistic is the median of the paired difference $\\widetilde{\\Delta} = \\text{median}_i\\!\\bigl(\\Delta_i^{(\\text{imp})} - \\Delta_i^{(\\text{rand})}\\bigr)$, measuring whether importance-based eviction produces systematically larger phase-dependent severity than random eviction. We permute strategy labels $10{,}000$ times to construct the null distribution and apply Bonferroni correction for 4 sparsity-level comparisons.\n\nPer-problem distributions of the paired severity difference $\\Delta_i = \\mathrm{II}_{\\textit{low},i} - \\mathrm{II}_{\\textit{high},i}$ under importance-based eviction are right-skewed at all sparsity levels, with mean/median ratios ranging from $1.2{\\times}$ ($s{=}0.15$) to $1.6{\\times}$ ($s{=}0.30$) for DeepSeek and $1.1{\\times}$ to $1.4{\\times}$ for Qwen.\n\nThe permutation null distributions are approximately symmetric around zero at all sparsity levels. At $s{=}0.15$, the observed statistic falls at the $99.92$th percentile of the null ($p_{\\text{Bonf}} = 0.0032$); at $s \\geq 0.20$, no permutation exceeds the observed statistic.\n\nTable~\\ref{tab:permutation} reports the results. All four sparsity levels reject $H_0$ after Bonferroni correction ($p_{\\text{Bonf}} < 0.005$), with observed median differences increasing monotonically from $0.37$ at $s{=}0.15$ to $9.85$ at $s{=}0.30$. The monotonic growth of both the point estimate and the CI lower bound ($0.19 \\to 0.69 \\to 1.66 \\to 6.70$) confirms that compound severity amplification strengthens with sparsity---not merely in central tendency but also in worst-case lower bounds. Figure~\\ref{fig:permtest-forest} presents these results as a forest plot. % exp_id: deepseek_bf16_permtest; source: permutation_test_results.json\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Paired permutation test for compound severity: importance vs.\\ random eviction on DeepSeek-R1-Distill-Qwen-7B ($n{=}49$, $10{,}000$ permutations, Bonferroni-corrected).}\n\\label{tab:permutation}\n\\begin{tabular}{@{}rrcl@{}}\n\\toprule\n$s$ & Observed $\\widetilde{\\Delta}$ & 95\\% CI & $p_{\\text{Bonf}}$ \\\\\n\\midrule\n0.15 & 0.37 & $[0.19,\\; 0.62]$ & 0.0032 \\\\ % exp_id: deepseek_bf16_permtest_s015\n0.20 & 0.97 & $[0.69,\\; 1.49]$ & ${<}\\,0.001$ \\\\ % exp_id: deepseek_bf16_permtest_s020\n0.25 & 3.34 & $[1.66,\\; 6.64]$ & ${<}\\,0.001$ \\\\ % exp_id: deepseek_bf16_permtest_s025\n0.30 & 9.85 & $[6.70,\\; 16.29]$ & ${<}\\,0.001$ \\\\ % exp_id: deepseek_bf16_permtest_s030\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig4_bootstrap.pdf}\n\\caption{Forest plot of permutation test results. Horizontal bars show 95\\% permutation CIs; diamonds mark observed median differences $\\widetilde{\\Delta}$. All CIs lie entirely above zero, confirming significant strategy-dependent severity at every sparsity level.}\n\\label{fig:permtest-forest}\n\\end{figure}\n\n\n\\section{Analysis: Entropy-Discrimination Collapse}\n\\label{app:analysis}\n\n\\subsection{Discrimination Collapse}\n\\label{sec:discrimination-collapse}\n\nHead pruning reduces the number of heads contributing to cumulative importance scores, flattening the score distribution. Table~\\ref{tab:discrimination-metrics-full} quantifies this effect: the Gini coefficient decreases by $0.030$--$0.081$ (DeepSeek) and $0.010$--$0.020$ (Qwen) after pruning, with consistent negative deltas across all 16 conditions (both models $\\times$ 4 sparsity levels $\\times$ 2 strategies). The CV delta is likewise negative in all 8 importance-based conditions. The same pattern holds under random eviction, confirming that discrimination collapse is a consequence of head pruning \\emph{per se}, not of the eviction strategy. % exp_id: c4_entropy_deepseek, c4_entropy_qwen\n\n\\begin{table}[t]\n\\centering\n\\caption{Discrimination collapse under importance-based eviction. $\\Delta\\mathrm{Gini}$ and $\\Delta\\mathrm{CV}$ are post-pruning minus baseline; negative values indicate reduced discriminative power.}\n\\label{tab:discrimination-metrics-full}\n\\small\n\\begin{tabular}{llrr}\n\\toprule\nModel & $s$ & $\\Delta\\mathrm{Gini}$ & $\\Delta\\mathrm{CV}$ \\\\\n\\midrule\nDeepSeek & $0.15$ & $-0.030$ & $-0.56$ \\\\\nDeepSeek & $0.20$ & $-0.040$ & $-0.77$ \\\\\nDeepSeek & $0.25$ & $-0.065$ & $-1.29$ \\\\\nDeepSeek & $0.30$ & $-0.081$ & $-1.66$ \\\\\n\\midrule\nQwen & $0.15$ & $-0.010$ & $-0.05$ \\\\\nQwen & $0.20$ & $-0.012$ & $-0.21$ \\\\\nQwen & $0.25$ & $-0.010$ & $-1.49$ \\\\\nQwen & $0.30$ & $-0.020$ & $-1.14$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nWhen importance scores lose discriminability, thresholding degenerates into noise-sensitive selection---functionally approaching biased random eviction. This is phase-dependent: in low-sparsity phases, attention is already broadly distributed, so pruning-induced flattening has maximum impact; in high-sparsity phases, concentration is preserved. Random eviction is immune because its decisions are independent of score quality, explaining $G \\approx 1$. % exp_id: c4_entropy_deepseek, c4_entropy_qwen\n\n\\subsection{Entropy Redistribution}\n\\label{sec:entropy-redistribution}\n\nBeyond discrimination collapse, we examine whether head pruning also redistributes the attention entropy of surviving heads. We measure the mean attention entropy per head:\n\\begin{equation}\n    \\mathcal{H}_i^{(h)} = -\\sum_{j=1}^{T} a_{ij}^{(h)} \\log a_{ij}^{(h)}\n    \\label{eq:attn-entropy}\n\\end{equation}\nand compute $\\Delta\\mathcal{H}$ as the change from baseline (no pruning) to the pruned condition.\n\nFor DeepSeek under importance-based eviction, the entropy delta is consistently negative across all four sparsity levels ($\\Delta\\mathcal{H} \\in [-0.047, -0.040]$; Table~\\ref{tab:entropy-deltas}), indicating that importance-based pruning systematically selects heads whose removal concentrates attention in the surviving heads, reinforcing discrimination collapse. % exp_id: c4_entropy_deepseek\n\nFor Qwen, the entropy pattern only partially replicates. The delta is negative at $s{=}0.15$ ($\\Delta\\mathcal{H} = -0.073$) and $s{=}0.20$ ($-0.076$), consistent with DeepSeek. However, at $s{=}0.25$, the delta reverses to $+0.045$, with 22 of 30 problems showing positive entropy change. At $s{=}0.30$, the delta is near zero ($-0.007$). The $s{=}0.25$ reversal is systematic rather than a statistical artifact: it is consistent across all three reasoning phases (low: $+0.042$, mid: $+0.034$, high: $+0.017$). We interpret this as a genuine model-specific difference, possibly arising from distinct head specialization patterns: Qwen's instruction tuning (vs.\\ DeepSeek's distillation-based training) may produce head configurations where removing 25\\% of heads triggers compensatory broadening rather than concentration. % exp_id: c4_entropy_qwen\n\nWe characterize discrimination collapse as the robust, model-independent driver of the phase-strategy interaction, with entropy redistribution as a secondary amplifier that is consistent in DeepSeek but model-dependent in Qwen.\n\n\\begin{table}[t]\n\\centering\n\\caption{Attention entropy deltas ($\\Delta\\mathcal{H}$) under importance-based eviction. DeepSeek shows consistent entropy compression; Qwen partially replicates with a reversal at $s{=}0.25$.}\n\\label{tab:entropy-deltas}\n\\small\n\\begin{tabular}{llr}\n\\toprule\nModel & $s$ & $\\Delta\\mathcal{H}$ \\\\\n\\midrule\nDeepSeek & $0.15$ & $-0.040$ \\\\\nDeepSeek & $0.20$ & $-0.047$ \\\\\nDeepSeek & $0.25$ & $-0.045$ \\\\\nDeepSeek & $0.30$ & $-0.044$ \\\\\n\\midrule\nQwen & $0.15$ & $-0.073$ \\\\\nQwen & $0.20$ & $-0.076$ \\\\\nQwen & $0.25$ & $+0.045$ \\\\\nQwen & $0.30$ & $-0.007$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n",
      "numLines": 164,
      "startLine": 1,
      "totalLines": 164
    }
  }
}
```

</details>

---

### Tool call

_source line 46_

<details open><summary>🔧 Tool call — Read · `toolu_019VLetUnJosEKy5dwrreu2j`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10233ec7-5d03-448a-9224-b6173ea0cbe8",
  "uuid": "2295fc1c-ad80-49b9-bcfd-d3802dfaf8e4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FsD7CPPuwEQCkUJRcvGJo5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10685,
      "cache_read_input_tokens": 24898,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10685
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

_source line 47 · 2026-05-14T21:49:36.998Z_

<details><summary>↩ Tool result · `toolu_019VLetUnJosEKy5dwrreu2j`</summary>

```text
1	\paragraph{Model scale and architecture.}
2	All experiments are conducted at the 7B parameter scale. Whether the phase-modulated severity patterns persist, amplify, or attenuate at larger scales (e.g., 70B) remains untested. Cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, \S\ref{sec:cross-arch}) partially extends the findings beyond the Qwen2 architecture: the directional pattern is qualitatively consistent but the interaction magnitude is substantially weaker and random pruning also exhibits a non-trivial phase gradient on LLaMA. The qualitative pattern has been tested on only two architecture families at the 7--8B scale; further validation on larger models and more diverse architectures (e.g., Mistral, multi-latent attention) is needed.
3	
4	\paragraph{Task coverage.}
5	We evaluate exclusively on MATH-500, a mathematical reasoning benchmark. Different reasoning tasks---code generation, commonsense reasoning, multi-hop question answering---may induce different phase structures with different sparsity distributions, potentially altering the severity gradient profile.
6	
7	\paragraph{Mechanism.}
8	The discrimination collapse mechanism is supported by correlational evidence (consistent Gini/CV reduction across all conditions); causal validation through controlled entropy manipulation is needed. The entropy redistribution component replicates on only 2/4 Qwen conditions, suggesting model-specific factors.
9	
10	\paragraph{Sparsity range.}
11	Our experiments span $s \in \{0.15, 0.20, 0.25, 0.30\}$. More extreme sparsity ($s > 0.50$) may exhibit qualitatively different interaction dynamics. We do not report inference throughput or latency measurements, which are necessary for a complete deployment analysis but orthogonal to our severity characterization. Extended limitations in Appendix~\ref{app:limitations}.
12	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10233ec7-5d03-448a-9224-b6173ea0cbe8",
  "uuid": "18ae834b-5adf-4588-b185-bb06cc02eb11",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/limitations.tex",
      "content": "\\paragraph{Model scale and architecture.}\nAll experiments are conducted at the 7B parameter scale. Whether the phase-modulated severity patterns persist, amplify, or attenuate at larger scales (e.g., 70B) remains untested. Cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, \\S\\ref{sec:cross-arch}) partially extends the findings beyond the Qwen2 architecture: the directional pattern is qualitatively consistent but the interaction magnitude is substantially weaker and random pruning also exhibits a non-trivial phase gradient on LLaMA. The qualitative pattern has been tested on only two architecture families at the 7--8B scale; further validation on larger models and more diverse architectures (e.g., Mistral, multi-latent attention) is needed.\n\n\\paragraph{Task coverage.}\nWe evaluate exclusively on MATH-500, a mathematical reasoning benchmark. Different reasoning tasks---code generation, commonsense reasoning, multi-hop question answering---may induce different phase structures with different sparsity distributions, potentially altering the severity gradient profile.\n\n\\paragraph{Mechanism.}\nThe discrimination collapse mechanism is supported by correlational evidence (consistent Gini/CV reduction across all conditions); causal validation through controlled entropy manipulation is needed. The entropy redistribution component replicates on only 2/4 Qwen conditions, suggesting model-specific factors.\n\n\\paragraph{Sparsity range.}\nOur experiments span $s \\in \\{0.15, 0.20, 0.25, 0.30\\}$. More extreme sparsity ($s > 0.50$) may exhibit qualitatively different interaction dynamics. We do not report inference throughput or latency measurements, which are necessary for a complete deployment analysis but orthogonal to our severity characterization. Extended limitations in Appendix~\\ref{app:limitations}.\n",
      "numLines": 12,
      "startLine": 1,
      "totalLines": 12
    }
  }
}
```

</details>

---

### Tool call

_source line 48_

<details open><summary>🔧 Tool call — Read · `toolu_0156yhgmLNBVGBcVqYajyDhX`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/background.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10233ec7-5d03-448a-9224-b6173ea0cbe8",
  "uuid": "07c398a5-0ec9-416d-8e79-bfae708274a3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FsD7CPPuwEQCkUJRcvGJo5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10685,
      "cache_read_input_tokens": 24898,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10685
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

_source line 49 · 2026-05-14T21:49:37.501Z_

<details><summary>↩ Tool result · `toolu_0156yhgmLNBVGBcVqYajyDhX`</summary>

```text
1	% Section 3: Background and Problem Setup
2	% Note: eq:ii and eq:gradient are the canonical definitions.
3	% Full formulation details in Appendix (app:formulation-details).
4	
5	\section{Background and Problem Setup}
6	\label{sec:background}
7	
8	We formalize compound sparsity, define the Interaction Index, and introduce phase segmentation. Full mathematical details appear in Appendix~\ref{app:formulation-details}.
9	
10	\paragraph{Compound sparsity.}
11	\label{sec:compound-sparsity}
12	Let $s \in (0,1)$ denote a unified sparsity budget. \emph{Attention head pruning} removes the bottom-$s$ fraction of heads per layer by Frobenius norm importance \cite{voita-acl2019, michel-neurips2019}. \emph{KV cache eviction} removes the bottom-$s$ fraction of token positions from the cache. We compare two strategies: \emph{importance-based}, which scores positions by position-normalized cumulative attention mass (Eq.~\ref{eq:kv-importance} in Appendix~\ref{app:formulation-details}), and \emph{random}, which evicts uniformly at random \cite{nacl-acl2024}. Applying both simultaneously yields \emph{compound sparsity}; the two axes interact because head pruning alters the importance ranking used for eviction \cite{spark-aaai2026}. Existing joint-pruning approaches such as GRASPrune \cite{graspune-acl2026} learn global budget-constrained gates but treat decisions as static across generation.
13	
14	\paragraph{Interaction Index.}
15	\label{sec:interaction-index}
16	For a text segment, let $\text{PPL}_c$ denote perplexity under condition $c \in \{d, a, k, b\}$ (dense, attention-only, KV-only, compound). Normalizing by the dense baseline yields $r_c = \text{PPL}_c / \text{PPL}_d$, and:
17	\begin{equation}
18	    \mathrm{II} = r_b - r_a - r_k + 1.
19	    \label{eq:ii}
20	\end{equation}
21	$\mathrm{II} > 0$ indicates super-additive degradation; $\mathrm{II} = 0$ indicates additive independence. We adopt the additive null because the two axes operate on disjoint dimensions; qualitative conclusions hold under the multiplicative null (Appendix~\ref{app:multiplicative-null}). Because the II distribution is heavily right-skewed, we report medians throughout.
22	
23	\paragraph{Severity gradient.}
24	To capture phase variation:
25	\begin{equation}
26	    G = \frac{\widetilde{\mathrm{II}}_{\,\textit{low}}}{\widetilde{\mathrm{II}}_{\,\textit{high}}},
27	    \label{eq:gradient}
28	\end{equation}
29	where $\widetilde{\mathrm{II}}_{\,\textit{low/high}}$ are median II in the low/high-sparsity phases. $G \gg 1$ indicates phase-concentrated severity.
30	
31	\paragraph{Phase segmentation.}
32	\label{sec:phase-segmentation}
33	Each generated sequence is partitioned into three phases (low-, mid-, high-sparsity) by tercile boundaries of per-position attention sparsity, following ThinKV~\cite{thinkv-iclr2026}. Low-sparsity phases correspond to broadly distributed attention (exploratory reasoning); high-sparsity phases to concentrated attention (structured computation). Details in Appendix~\ref{app:formulation-details}.
34	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10233ec7-5d03-448a-9224-b6173ea0cbe8",
  "uuid": "5dd88930-42e4-4184-a5ee-21313e4253e7",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/background.tex",
      "content": "% Section 3: Background and Problem Setup\n% Note: eq:ii and eq:gradient are the canonical definitions.\n% Full formulation details in Appendix (app:formulation-details).\n\n\\section{Background and Problem Setup}\n\\label{sec:background}\n\nWe formalize compound sparsity, define the Interaction Index, and introduce phase segmentation. Full mathematical details appear in Appendix~\\ref{app:formulation-details}.\n\n\\paragraph{Compound sparsity.}\n\\label{sec:compound-sparsity}\nLet $s \\in (0,1)$ denote a unified sparsity budget. \\emph{Attention head pruning} removes the bottom-$s$ fraction of heads per layer by Frobenius norm importance \\cite{voita-acl2019, michel-neurips2019}. \\emph{KV cache eviction} removes the bottom-$s$ fraction of token positions from the cache. We compare two strategies: \\emph{importance-based}, which scores positions by position-normalized cumulative attention mass (Eq.~\\ref{eq:kv-importance} in Appendix~\\ref{app:formulation-details}), and \\emph{random}, which evicts uniformly at random \\cite{nacl-acl2024}. Applying both simultaneously yields \\emph{compound sparsity}; the two axes interact because head pruning alters the importance ranking used for eviction \\cite{spark-aaai2026}. Existing joint-pruning approaches such as GRASPrune \\cite{graspune-acl2026} learn global budget-constrained gates but treat decisions as static across generation.\n\n\\paragraph{Interaction Index.}\n\\label{sec:interaction-index}\nFor a text segment, let $\\text{PPL}_c$ denote perplexity under condition $c \\in \\{d, a, k, b\\}$ (dense, attention-only, KV-only, compound). Normalizing by the dense baseline yields $r_c = \\text{PPL}_c / \\text{PPL}_d$, and:\n\\begin{equation}\n    \\mathrm{II} = r_b - r_a - r_k + 1.\n    \\label{eq:ii}\n\\end{equation}\n$\\mathrm{II} > 0$ indicates super-additive degradation; $\\mathrm{II} = 0$ indicates additive independence. We adopt the additive null because the two axes operate on disjoint dimensions; qualitative conclusions hold under the multiplicative null (Appendix~\\ref{app:multiplicative-null}). Because the II distribution is heavily right-skewed, we report medians throughout.\n\n\\paragraph{Severity gradient.}\nTo capture phase variation:\n\\begin{equation}\n    G = \\frac{\\widetilde{\\mathrm{II}}_{\\,\\textit{low}}}{\\widetilde{\\mathrm{II}}_{\\,\\textit{high}}},\n    \\label{eq:gradient}\n\\end{equation}\nwhere $\\widetilde{\\mathrm{II}}_{\\,\\textit{low/high}}$ are median II in the low/high-sparsity phases. $G \\gg 1$ indicates phase-concentrated severity.\n\n\\paragraph{Phase segmentation.}\n\\label{sec:phase-segmentation}\nEach generated sequence is partitioned into three phases (low-, mid-, high-sparsity) by tercile boundaries of per-position attention sparsity, following ThinKV~\\cite{thinkv-iclr2026}. Low-sparsity phases correspond to broadly distributed attention (exploratory reasoning); high-sparsity phases to concentrated attention (structured computation). Details in Appendix~\\ref{app:formulation-details}.\n",
      "numLines": 34,
      "startLine": 1,
      "totalLines": 34
    }
  }
}
```

</details>

---

### Tool call

_source line 50_

<details open><summary>🔧 Tool call — Read · `toolu_017eoZzkgr34KHmkF86oaikW`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10233ec7-5d03-448a-9224-b6173ea0cbe8",
  "uuid": "dfbae6f3-7334-4256-9e66-438105041598",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FsD7CPPuwEQCkUJRcvGJo5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10685,
      "cache_read_input_tokens": 24898,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10685
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

_source line 51 · 2026-05-14T21:49:38.368Z_

<details><summary>↩ Tool result · `toolu_017eoZzkgr34KHmkF86oaikW`</summary>

```text
1	\section{Related Work}
2	\label{sec:related}
3	
4	\paragraph{Compound compression.}
5	Combining multiple compression axes produces non-additive errors.
6	\cite{spark-aaai2026} report super-additive degradation when combining channel pruning with token eviction; \cite{slim-icml2025} formalize compound error for quantization and sparsity.
7	\cite{unicomp-2026} evaluate compound compression across 40+ benchmarks, revealing that reasoning capabilities degrade disproportionately.
8	\cite{phase-transition-compression-2026} characterize independent phase transition points per compression dimension, implying the joint safe region is the intersection of per-dimension safe zones.
9	GRASPrune~\cite{graspune-acl2026} learns global budget-constrained gates for joint pruning but treats decisions as static across generation.
10	These works establish compound interaction but share an implicit assumption: interaction magnitude is constant across the generation process.
11	
12	\paragraph{KV cache eviction.}
13	Most methods rely on importance scoring whose reliability is increasingly questioned.
14	Ada-KV~\cite{adakv-neurips2025} introduces per-head adaptive budgets; SnapKV~\cite{snapkv-neurips2024} compresses from a fixed observation window; \cite{defensivekv-iclr2026} show worst-case loss $2.3$--$4.3{\times}$ higher than expected under standard aggregation.
15	\cite{nacl-acl2024} combine proxy-token and random eviction to counter attention bias.
16	RetentiveKV~\cite{retentivekv-2026} identifies deferred importance, and \cite{greedy-bias-kvcache-2026} show that single importance metrics exhibit systematic greedy bias.
17	\cite{hies-2025} independently show that importance-based head discrimination collapses under heavy pruning, further questioning single-metric reliability.
18	Lethe~\cite{lethe-aaai2026} introduces temporal adaptivity with layer-wise multi-round pruning, and SparK~\cite{spark-aaai2026} extends eviction to the channel dimension with recoverable sparsity.
19	These methods each optimize a single pruning axis---whether aggregation, metric, temporal, or channel---without characterizing compound interactions when multiple mechanisms are simultaneously active.
20	
21	\paragraph{Phase-aware inference.}
22	ThinKV~\cite{thinkv-iclr2026} applies different KV strategies per phase but without compound interaction.
23	\cite{decision-repr-transition-2026} find pruning sensitivity depends on ``silent'' vs.\ ``decisive'' representation phases.
24	\cite{doing-more-with-less-2026} show pruning combined with test-time scaling can exceed unpruned baselines; \cite{sparse-frontier-2025} find no universally optimal sparse attention strategy across generation stages.
25	\cite{physics-kvcache-2026} identify a sharp phase transition in single-axis KV cache compression at high sparsity, characterizing the single-dimension failure mode that our compound analysis extends across multiple axes.
26	R-KV~\cite{rkv-neurips2025} exploits reasoning-specific redundancy for aggressive cache compression, targeting per-axis optimization rather than characterizing compound degradation.
27	These works establish phase-dependent compression tolerance along single axes.
28	Our work bridges this by quantifying how compound severity varies across phases and eviction strategies.
29	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10233ec7-5d03-448a-9224-b6173ea0cbe8",
  "uuid": "4dba6686-5ff1-4c84-b558-ec5cc163ee3a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/related_work.tex",
      "content": "\\section{Related Work}\n\\label{sec:related}\n\n\\paragraph{Compound compression.}\nCombining multiple compression axes produces non-additive errors.\n\\cite{spark-aaai2026} report super-additive degradation when combining channel pruning with token eviction; \\cite{slim-icml2025} formalize compound error for quantization and sparsity.\n\\cite{unicomp-2026} evaluate compound compression across 40+ benchmarks, revealing that reasoning capabilities degrade disproportionately.\n\\cite{phase-transition-compression-2026} characterize independent phase transition points per compression dimension, implying the joint safe region is the intersection of per-dimension safe zones.\nGRASPrune~\\cite{graspune-acl2026} learns global budget-constrained gates for joint pruning but treats decisions as static across generation.\nThese works establish compound interaction but share an implicit assumption: interaction magnitude is constant across the generation process.\n\n\\paragraph{KV cache eviction.}\nMost methods rely on importance scoring whose reliability is increasingly questioned.\nAda-KV~\\cite{adakv-neurips2025} introduces per-head adaptive budgets; SnapKV~\\cite{snapkv-neurips2024} compresses from a fixed observation window; \\cite{defensivekv-iclr2026} show worst-case loss $2.3$--$4.3{\\times}$ higher than expected under standard aggregation.\n\\cite{nacl-acl2024} combine proxy-token and random eviction to counter attention bias.\nRetentiveKV~\\cite{retentivekv-2026} identifies deferred importance, and \\cite{greedy-bias-kvcache-2026} show that single importance metrics exhibit systematic greedy bias.\n\\cite{hies-2025} independently show that importance-based head discrimination collapses under heavy pruning, further questioning single-metric reliability.\nLethe~\\cite{lethe-aaai2026} introduces temporal adaptivity with layer-wise multi-round pruning, and SparK~\\cite{spark-aaai2026} extends eviction to the channel dimension with recoverable sparsity.\nThese methods each optimize a single pruning axis---whether aggregation, metric, temporal, or channel---without characterizing compound interactions when multiple mechanisms are simultaneously active.\n\n\\paragraph{Phase-aware inference.}\nThinKV~\\cite{thinkv-iclr2026} applies different KV strategies per phase but without compound interaction.\n\\cite{decision-repr-transition-2026} find pruning sensitivity depends on ``silent'' vs.\\ ``decisive'' representation phases.\n\\cite{doing-more-with-less-2026} show pruning combined with test-time scaling can exceed unpruned baselines; \\cite{sparse-frontier-2025} find no universally optimal sparse attention strategy across generation stages.\n\\cite{physics-kvcache-2026} identify a sharp phase transition in single-axis KV cache compression at high sparsity, characterizing the single-dimension failure mode that our compound analysis extends across multiple axes.\nR-KV~\\cite{rkv-neurips2025} exploits reasoning-specific redundancy for aggressive cache compression, targeting per-axis optimization rather than characterizing compound degradation.\nThese works establish phase-dependent compression tolerance along single axes.\nOur work bridges this by quantifying how compound severity varies across phases and eviction strategies.\n",
      "numLines": 29,
      "startLine": 1,
      "totalLines": 29
    }
  }
}
```

</details>

---

### Tool call

_source line 52_

<details open><summary>🔧 Tool call — Read · `toolu_01E8XgGonsUzri4UH7wpgSp6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10233ec7-5d03-448a-9224-b6173ea0cbe8",
  "uuid": "83d98f4a-fc4f-4700-b119-154db8cc2a16",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FsD7CPPuwEQCkUJRcvGJo5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10685,
      "cache_read_input_tokens": 24898,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10685
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

_source line 53 · 2026-05-14T21:49:38.637Z_

<details><summary>↩ Tool result · `toolu_01E8XgGonsUzri4UH7wpgSp6`</summary>

```text
1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{inconsolata}
11	
12	\usepackage{amsmath}
13	\usepackage{amssymb}
14	\usepackage{graphicx}
15	\usepackage{booktabs}
16	\usepackage{enumitem}
17	\usepackage{multirow}
18	
19	\graphicspath{{figures/}}
20	
21	\title{Phase-Modulated Compound Sparsity:\\Strategy-Dependent Severity Gradients in Reasoning Models}
22	
23	\author{Anonymous}
24	
25	\begin{document}
26	
27	\maketitle
28	
29	\input{abstract}
30	
31	\input{introduction}
32	\input{related_work}
33	\input{background}
34	\input{methodology}
35	\input{results}
36	\input{analysis}
37	\input{discussion}
38	\input{conclusion}
39	
40	\bibliography{references}
41	
42	\section*{Limitations}
43	\input{limitations}
44	
45	\appendix
46	\input{appendix}
47	\input{appendix_moved}
48	\input{appendix_disc_analysis}
49	
50	\end{document}
51	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10233ec7-5d03-448a-9224-b6173ea0cbe8",
  "uuid": "1d84839a-2980-4e45-b763-ae3b79b2cb3b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main.tex",
      "content": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{inconsolata}\n\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{enumitem}\n\\usepackage{multirow}\n\n\\graphicspath{{figures/}}\n\n\\title{Phase-Modulated Compound Sparsity:\\\\Strategy-Dependent Severity Gradients in Reasoning Models}\n\n\\author{Anonymous}\n\n\\begin{document}\n\n\\maketitle\n\n\\input{abstract}\n\n\\input{introduction}\n\\input{related_work}\n\\input{background}\n\\input{methodology}\n\\input{results}\n\\input{analysis}\n\\input{discussion}\n\\input{conclusion}\n\n\\bibliography{references}\n\n\\section*{Limitations}\n\\input{limitations}\n\n\\appendix\n\\input{appendix}\n\\input{appendix_moved}\n\\input{appendix_disc_analysis}\n\n\\end{document}\n",
      "numLines": 51,
      "startLine": 1,
      "totalLines": 51
    }
  }
}
```

</details>

---

### Assistant

_source line 54_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive view of all the .tex files. Let me also check for any figure generation scripts and read the existing n500_update_checklist.md fully.

Let me now compile the precise patch plan. Let me organize my findings:

## A1. Tables (containing n=50 data)

1. **abstract.tex:6** — "using 50 MATH-500 problems" → n=500
2. **abstract.tex:7** — All numerical values: "median Interaction Index difference... from $0.39$... to $14.59$... $d_z$ growing from $0.44$... 

to $0.80$; Bonferroni-corrected permutation tests yield $p < 0.005$"
3. **abstract.tex:8** — "7/8 conditions", Qwen s=0.30 values
4. **abstract.tex:9** — Crossover values: "$\widetilde{\mathrm{II}} = 0.032$ vs.\ $0.818$" and "$7.196$ vs.\ $1.363$"
5. **abstract.tex:10** — Qwen and LLaMA replication stats

Tables:
- **results.tex:10-23** — Table 1 (tab:aggregate) with n=50 aggregate statistics
- **results.tex:25-40** — Table 2 (tab:conditions) with condition-level breakdowns
- **results.tex:42-57** — Table 3 (tab:replication) with replication results
- **results.tex:59-74** — Table 4 (tab:cross-model) with cross-model comparisons
- **results.tex:76-91** — Table 5 (tab:permutation) with permutation test results
- **results.tex:93-108** — Table 6 (tab:discrimination) with discrimination metrics

Now I'm reviewing the full table structure across the results and appendix sections, tracking the DeepSeek aggregate data, per-phase breakdowns, cross-architecture comparisons for LLaMA, and Cohen's d calculations for both models, along with the supporting permutation and cross-model analyses in the appendix.

Looking at the quantitative claims in the abstract, I'm checking the specific numerical values cited: the 50 MATH-500 problems, the performance metrics like 0.39 and 14.59, the statistical significance thresholds, effect sizes, and the various delta measurements for entropy and discrimination metrics.

Now I'm moving through the introduction section to verify those same claims are properly cited—the effect size improvements from 0.44 to 0.80, the significance levels, and the condition-specific results. Then I need to check the methodology section where the problem stratification is described. I'm continuing to catalog the numerical results across the remaining sections—LLaMA model statistics with effect sizes and p-values, permutation test outcomes, and Cohen's d comparisons. The discussion section references the performance multipliers and crossover thresholds I've already noted. Now I'm looking at the high-phase II values and concordance statistics across the appendix sections, checking the permutation test details and sample sizes to understand the statistical scope of the analysis.

I'm finding a D059 violation where d_z is being used for importance-versus-random comparisons when it should only be used within-importance comparisons. The table caption in results.tex explicitly describes d_z as paired Cohen's d for importance versus random severity, and the text references monotonically increasing d_z values across those comparisons—both violations of the rule that Wilcoxon p-values and median differences should be used instead for imp-vs-rand analysis. I'm tracking down where d_z is used for between-strategy comparisons versus within-strategy comparisons. The abstract mentions d_z values ranging from 0.44 to 0.80 for phase-dependent effects under importance-based eviction, which is fine, but the LLaMA results show d_z from 0.19 to 0.34 comparing importance versus random — that's the D059 violation I need to flag. Continuing through the document, I see the Introduction mentions extending to DeepSeek-R1-Distill-Llama-8B with a much weaker trend, but no d_z values there. The Discussion references within-strategy phase gradients and the Conclusion shows within-importance comparisons, both of which are fine. So I've identified two clear D059 violations: the abstract reporting d_z values for importance versus random severity, and the results section showing the paired d_z progression across those same strategy comparisons.

Now checking the table in results.tex — Table 3 uses d_z throughout for the importance-versus-random comparison, which is another violation of the same pattern.

Moving to the cautious language check for LLaMA claims, I'm seeing the abstract uses "suggests," the introduction uses "partially," and the results section employs "qualitatively consistent" and "directional pattern" — all appropriately hedged language.

But looking closer at line 79 in results.tex, "The qualitative pattern replicates" reads too definitive for a partially confirmed finding. The follow-up on line 81 does add "though the interaction magnitude is substantially weaker," which provides some qualification, but the verb "replicates" itself should probably be softened to "partially replicates" or "appears to replicate" to align with the partial confirmation status. Checking the rest of the document, discussion.tex, conclusion.tex, appendix_disc_analysis.tex, and limitations.tex all use appropriately cautious phrasing like "provides partial support" and "partially extends," so the issue is really just that one instance in results.tex that needs adjustment.

For the future work section, I notice there's no dedicated Future Work subsection anywhere. The discussion mentions a potential mitigation with phase-aware compression budgets but doesn't frame it as a pilot experiment, and the conclusion just briefly notes that the findings motivate phase-aware sparsity allocation. Since there's no §8 Future Work section currently, I'd need to either add one or integrate the future work discussion more explicitly into the existing conclusion.

Now I'm looking at the figures in the paper...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10233ec7-5d03-448a-9224-b6173ea0cbe8",
  "uuid": "ec848c97-ee27-431a-b21e-1c9fdca3f037",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018gX6anJTpLSPQbLf2mtLwH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11075,
      "cache_read_input_tokens": 35583,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11075
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

_source line 55_

Now let me find figure generation scripts and check the existing checklist for additional context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10233ec7-5d03-448a-9224-b6173ea0cbe8",
  "uuid": "0dcd2a65-fb88-4b92-8518-e97068645227",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018gX6anJTpLSPQbLf2mtLwH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11075,
      "cache_read_input_tokens": 35583,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11075
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

_source line 56_

<details open><summary>🔧 Tool call — Glob · `toolu_01LfxNBwo8XXFLyAzEgRfNpa`</summary>

```json
{
  "pattern": "**/*.py",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10233ec7-5d03-448a-9224-b6173ea0cbe8",
  "uuid": "255ef021-3eb3-491b-af03-1d984a98c6cb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018gX6anJTpLSPQbLf2mtLwH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11075,
      "cache_read_input_tokens": 35583,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11075
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

_source line 57 · 2026-05-14T21:50:58.432Z_

<details><summary>↩ Tool result · `toolu_01LfxNBwo8XXFLyAzEgRfNpa`</summary>

```text
artifacts/_project/intermediate/phase_segmentation.py
artifacts/pacs/profiling/__init__.py
artifacts/pacs/utils/__init__.py
artifacts/_project/intermediate/metrics.py
artifacts/_project/intermediate/run_profiling.py
artifacts/_project/intermediate/interaction_index.py
artifacts/pacs/__init__.py
artifacts/pacs/utils/data_utils.py
artifacts/pacs/compound/__init__.py
artifacts/pacs/compound/head_selector.py
artifacts/pacs/compound/kv_evictor.py
artifacts/pacs/compound/compound_forward.py
artifacts/pacs/profiling/phase_segmentation.py
artifacts/pacs/profiling/alt_segmentation.py
artifacts/pacs/compound/test_compound.py
artifacts/pacs/profiling/analyze_results.py
artifacts/pacs/profiling/analyze_v4_results.py
artifacts/pacs/profiling/run_profiling.py
artifacts/pacs/profiling/interaction_index.py
artifacts/pacs/utils/metrics.py
artifacts/bootstrap_phase_gradient.py
artifacts/compute_multiplicative_null.py
artifacts/analyze_c2_n500.py
artifacts/_project/intermediate/analyze_n500.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10233ec7-5d03-448a-9224-b6173ea0cbe8",
  "uuid": "7fe1b70f-9358-448e-a14a-fd986eb49499",
  "tool_use_result": {
    "filenames": [
      "artifacts/_project/intermediate/phase_segmentation.py",
      "artifacts/pacs/profiling/__init__.py",
      "artifacts/pacs/utils/__init__.py",
      "artifacts/_project/intermediate/metrics.py",
      "artifacts/_project/intermediate/run_profiling.py",
      "artifacts/_project/intermediate/interaction_index.py",
      "artifacts/pacs/__init__.py",
      "artifacts/pacs/utils/data_utils.py",
      "artifacts/pacs/compound/__init__.py",
      "artifacts/pacs/compound/head_selector.py",
      "artifacts/pacs/compound/kv_evictor.py",
      "artifacts/pacs/compound/compound_forward.py",
      "artifacts/pacs/profiling/phase_segmentation.py",
      "artifacts/pacs/profiling/alt_segmentation.py",
      "artifacts/pacs/compound/test_compound.py",
      "artifacts/pacs/profiling/analyze_results.py",
      "artifacts/pacs/profiling/analyze_v4_results.py",
      "artifacts/pacs/profiling/run_profiling.py",
      "artifacts/pacs/profiling/interaction_index.py",
      "artifacts/pacs/utils/metrics.py",
      "artifacts/bootstrap_phase_gradient.py",
      "artifacts/compute_multiplicative_null.py",
      "artifacts/analyze_c2_n500.py",
      "artifacts/_project/intermediate/analyze_n500.py"
    ],
    "durationMs": 13,
    "numFiles": 24,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 58_

<details open><summary>🔧 Tool call — Glob · `toolu_01E4QJJZUhxucHwSvA8yyjEZ`</summary>

```json
{
  "pattern": "**/*plot*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10233ec7-5d03-448a-9224-b6173ea0cbe8",
  "uuid": "2f9e303c-84f4-4775-afb0-53bf50bb31d9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018gX6anJTpLSPQbLf2mtLwH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11075,
      "cache_read_input_tokens": 35583,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11075
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

_source line 59 · 2026-05-14T21:50:59.363Z_

<details><summary>↩ Tool result · `toolu_01E4QJJZUhxucHwSvA8yyjEZ`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10233ec7-5d03-448a-9224-b6173ea0cbe8",
  "uuid": "ec642489-56ad-4174-9cf8-4634e22cd5ee",
  "tool_use_result": {
    "filenames": [],
    "durationMs": 9,
    "numFiles": 0,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 60_

<details open><summary>🔧 Tool call — Glob · `toolu_013RXLJUDPT8xgZSZ7ajZcse`</summary>

```json
{
  "pattern": "**/*fig*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10233ec7-5d03-448a-9224-b6173ea0cbe8",
  "uuid": "ae00582c-11b3-46c0-8896-704c4e91ca90",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018gX6anJTpLSPQbLf2mtLwH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11075,
      "cache_read_input_tokens": 35583,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11075
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

_source line 61 · 2026-05-14T21:50:59.844Z_

<details><summary>↩ Tool result · `toolu_013RXLJUDPT8xgZSZ7ajZcse`</summary>

```text
artifacts/_project/chart/paper_figures_manifest.txt
artifacts/_project/chart/paper_figures_v1_manifest.txt
artifacts/_project/chart/fig1_dose_response_info.txt
artifacts/_project/chart/fig2_cohens_d_info.txt
artifacts/_project/chart/fig3_crossover_info.txt
artifacts/_project/chart/fig4_per_problem_dist_info.txt
artifacts/_project/chart/fig2_cohens_d_location.txt
artifacts/_project/chart/fig2_cohens_d_paired_b10000_info.txt
artifacts/_project/chart/fig2_segment_level_backup_info.txt
artifacts/_project/chart/paper_figures_v2_manifest.txt
artifacts/_project/chart/fig1_dose_response_info_0e54ee.txt
artifacts/_project/chart/fig3_crossover_info_f6c838.txt
artifacts/_project/chart/fig4_bootstrap_info.txt
artifacts/_project/chart/fig5_crossmodel_info.txt
artifacts/_project/chart/fig1_dose_response_bf16.txt
artifacts/_project/chart/fig3_crossover_bf16.txt
artifacts/_project/chart/fig4_forest_paired_dz.txt
artifacts/_project/chart/fig5_crossmodel_bf16.txt
artifacts/_project/paper/figures/fig1_dose_response.pdf
artifacts/_project/paper/figures/fig3_crossover.pdf
artifacts/_project/paper/figures/fig4_bootstrap.pdf
artifacts/_project/paper/figures/fig5_crossmodel.pdf
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10233ec7-5d03-448a-9224-b6173ea0cbe8",
  "uuid": "7ec72559-7c3e-494e-88d2-c1d15735d432",
  "tool_use_result": {
    "filenames": [
      "artifacts/_project/chart/paper_figures_manifest.txt",
      "artifacts/_project/chart/paper_figures_v1_manifest.txt",
      "artifacts/_project/chart/fig1_dose_response_info.txt",
      "artifacts/_project/chart/fig2_cohens_d_info.txt",
      "artifacts/_project/chart/fig3_crossover_info.txt",
      "artifacts/_project/chart/fig4_per_problem_dist_info.txt",
      "artifacts/_project/chart/fig2_cohens_d_location.txt",
      "artifacts/_project/chart/fig2_cohens_d_paired_b10000_info.txt",
      "artifacts/_project/chart/fig2_segment_level_backup_info.txt",
      "artifacts/_project/chart/paper_figures_v2_manifest.txt",
      "artifacts/_project/chart/fig1_dose_response_info_0e54ee.txt",
      "artifacts/_project/chart/fig3_crossover_info_f6c838.txt",
      "artifacts/_project/chart/fig4_bootstrap_info.txt",
      "artifacts/_project/chart/fig5_crossmodel_info.txt",
      "artifacts/_project/chart/fig1_dose_response_bf16.txt",
      "artifacts/_project/chart/fig3_crossover_bf16.txt",
      "artifacts/_project/chart/fig4_forest_paired_dz.txt",
      "artifacts/_project/chart/fig5_crossmodel_bf16.txt",
      "artifacts/_project/paper/figures/fig1_dose_response.pdf",
      "artifacts/_project/paper/figures/fig3_crossover.pdf",
      "artifacts/_project/paper/figures/fig4_bootstrap.pdf",
      "artifacts/_project/paper/figures/fig5_crossmodel.pdf"
    ],
    "durationMs": 12,
    "numFiles": 22,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 62_

<details open><summary>🔧 Tool call — Read · `toolu_015beP29cJquSt9RofLTcYgA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/n500_update_checklist.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10233ec7-5d03-448a-9224-b6173ea0cbe8",
  "uuid": "3a22214c-22cf-46d9-9c4f-284160f4653e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018gX6anJTpLSPQbLf2mtLwH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11075,
      "cache_read_input_tokens": 35583,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11075
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

_source line 63 · 2026-05-14T21:51:00.342Z_

<details><summary>↩ Tool result · `toolu_015beP29cJquSt9RofLTcYgA`</summary>

````text
1	# n=500 更新清单
2	
3	> 论文：Phase-Modulated Compound Sparsity (EMNLP 2026 ARR)
4	> 当前数据：n=50 MATH-500（DeepSeek n=49, Qwen n=46, LLaMA n=49）
5	> 目标数据：n=500 MATH-500
6	> 生成日期：2026-05-14
7	> 硬约束：D054 (median only), D059 (within-imp d_z only), D015 (emergent interaction framing), D056 (C5b→future work), D060 (LLaMA→suggests)
8	
9	---
10	
11	## 统计汇总
12	
13	| 分类 | 数量 |
14	|------|------|
15	| data_update（数字替换） | 48 |
16	| figure_update（重新生成） | 5 |
17	| claim_update（措辞调整） | 8 |
18	| structural（结构变动） | 3 |
19	| constraint_check（硬约束合规） | 6 |
20	| **总计** | **70** |
21	
22	---
23	
24	## §0 Abstract (abstract.tex)
25	
26	### A01 [data_update] Line 6 — 样本量
27	- **当前**: `50 MATH-500 problems`
28	- **替换**: `500 MATH-500 problems`
29	- **依赖**: n=500 DeepSeek/Qwen 有效样本量（扣除 degenerate phase 后实际 n）
30	
31	### A02 [data_update] Line 7 — DeepSeek 主结果
32	- **当前**: `median Interaction Index difference between low-sparsity and high-sparsity reasoning phases increases monotonically from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$`
33	- **替换**: n=500 DeepSeek importance Δ 值（4 个 sparsity level）
34	- **来源**: experiment_summary_table.json → median_diff
35	
36	### A03 [data_update] Line 7 — DeepSeek d_z 和 p
37	- **当前**: `paired Cohen's $d_z$ growing from $0.44$ (small) to $0.80$ (large); Bonferroni-corrected permutation tests yield $p < 0.005$`
38	- **替换**: n=500 DeepSeek within-importance paired d_z（4 值）+ 新 p-values
39	- **注意**: D059 — 此处 d_z 是 within-importance (low−high)，合规 ✓
40	
41	### A04 [data_update] Line 8 — Random baseline 统计
42	- **当前**: `Random eviction produces no significant phase modulation in 7/8 conditions; the single exception (Qwen $s{=}0.30$, $p{=}0.012$) shows negligible effect size ($d_z{=}{-}0.04$)`
43	- **替换**: n=500 random 条件的 PASS/FAIL 计数 + 例外条件的 p 和效应量
44	- **注意**: D059 — random 条件不报 d_z，改为 Wilcoxon p + median_diff
45	
46	### A05 [data_update] Line 9 — Crossover 数值
47	- **当前**: `$\widetilde{\mathrm{II}} = 0.032$ vs.\ $0.818$` 和 `$7.196$ vs.\ $1.363$`
48	- **替换**: n=500 s=0.25 crossover 的 4 个 II 中位数
49	
50	### A06 [data_update] Line 10 — Qwen 复现
51	- **当前**: `$d_z \geq 0.55$; Spearman $\rho = 1.0$; gradient permutation $p = 0.043$`
52	- **替换**: n=500 Qwen within-importance d_z + Spearman ρ + permutation p
53	
54	### A07 [data_update] Line 10 — LLaMA 数值
55	- **当前**: `$d_z$ ($0.19 \to 0.34$; $s{=}0.30$ Wilcoxon $p_{\text{Bonf}} = 0.029$)`
56	- **替换**: LLaMA 数据未变（n=49），但需确认是否也跑 n=500
57	- **注意**: D059 违规 ⚠️ — 此 d_z 是 imp-vs-rand，应改为 Wilcoxon p + median_diff
58	- **注意**: D060 — 当前用 "suggests"，合规 ✓
59	
60	### A08 [data_update] Line 10 — LLaMA 倍数比
61	- **当前**: `${\sim}$1/40 the absolute magnitude`
62	- **替换**: 用 n=500 DeepSeek 数据重算 LLaMA/DeepSeek 比值
63	
64	---
65	
66	## §1 Introduction (introduction.tex)
67	
68	### I01 [data_update] Line 14 — DeepSeek 主结果
69	- **当前**: `$0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$ ($d_z$: $0.44 \to 0.80$; Bonferroni-corrected $p < 0.005$)`
70	- **替换**: 与 A02/A03 同步
71	
72	### I02 [data_update] Line 15 — Qwen d_z
73	- **当前**: `$d_z \geq 0.55$`
74	- **替换**: n=500 Qwen within-importance d_z 下界
75	
76	### I03 [data_update] Line 15 — LLaMA 倍数
77	- **当前**: `$\sim$1/40 the magnitude`
78	- **替换**: 与 A08 同步
79	
80	### I04 [data_update] Line 16 — Random PASS/FAIL 统计
81	- **当前**: `7/8 conditions non-significant`
82	- **替换**: n=500 random PASS/FAIL 计数
83	
84	---
85	
86	## §4 Experimental Setup (methodology.tex)
87	
88	### M01 [data_update] Line 10 — 样本量
89	- **当前**: `50 problems stratified from MATH-500`
90	- **替换**: `500 problems from MATH-500`（去掉 "stratified"，500 ≈ 全集）
91	
92	### M02 [data_update] Line 18 — 偏度统计
93	- **当前**: `mean/median ratios up to 43:1`
94	- **替换**: n=500 的 mean/median ratio
95	- **注意**: D054 — 此处引用 mean/median 比作为选择 median 的理由，合规 ✓
96	
97	### M03 [data_update] Line 22 — p-value 总结
98	- **当前**: `All tests yield $p_{\text{Bonf}} < 0.005$ at every sparsity level.`
99	- **替换**: n=500 permutation test 结果
100	
101	---
102	
103	## §5 Results (results.tex)
104	
105	### R01 [data_update] Lines 8 — §5.1 aggregate Δ
106	- **当前**: `$\Delta$ increases from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$---a $37{\times}$ amplification`
107	- **替换**: n=500 Δ 值 + 新倍数
108	
109	### R02 [data_update] Line 8 — Random Δ 范围
110	- **当前**: `$-0.02$ to $1.54$`
111	- **替换**: n=500 random Δ 范围
112	
113	### R03 [data_update] Line 13 — Table 1 标题样本量
114	- **当前**: `$n{=}50$ MATH-500 problems`
115	- **替换**: `$n{=}500$`（或实际有效 n）
116	
117	### R04 [data_update] Lines 19-20 — Table 1 (aggregate-ii) 全部数据
118	- **当前**:
119	  ```
120	  Importance & 0.39 & 1.48 & 7.16 & 14.59
121	  Random     & 0.01 & −0.02 & 0.54 & 1.54
122	  ```
123	- **替换**: n=500 median Δ 值（8 个数字）
124	
125	### R05 [data_update] Line 29 — §5.2 severity gradient G
126	- **当前**: `$69{\times}$ at $s{=}0.15$ to $274{\times}$ at $s{=}0.30$`
127	- **替换**: n=500 G 值
128	- **注意**: D031/D033 决定 gradient ratio 仅作辅助描述；确认 n=500 是否仍报 G
129	
130	### R06 [data_update] Line 29 — high-phase II 范围
131	- **当前**: `$\widetilde{\mathrm{II}}_{\textit{high}}$ ranges from $0.006$ to $0.053$`
132	- **替换**: n=500 high-phase median II 范围
133	
134	### R07 [data_update] Line 29 — Random G 范围
135	- **当前**: `$G \approx 0.9$--$1.7{\times}$`
136	- **替换**: n=500 random G 范围
137	
138	### R08 [data_update] Lines 34, 40-50 — Table 2 (main-results) 全部数据
139	- **当前**: "50 problems" + 24 个数据单元格（6列×4组）
140	- **替换**: n=500 全部 per-phase median II + Δ + G（24 个数字 + caption 中 n）
141	
142	### R09 [figure_update] Lines 55-60 — Figure 1 (fig1_dose_response.pdf)
143	- **当前**: 基于 n=50 bf16 数据
144	- **操作**: 用 n=500 数据重新生成 fig1_dose_response.pdf
145	- **注意**: caption 中 "$69{\times}$ to $274{\times}$" 需同步更新
146	
147	### R10 [data_update] Line 66 — §5.3 Crossover 数值
148	- **当前**: `$0.032$ vs.\ $0.818$`, `$7.196$ vs.\ $1.363$---a $5.3{\times}$ reversal`
149	- **替换**: n=500 s=0.25 crossover 值 + 倍数
150	
151	### R11 [data_update] Line 71 — §5.4 Qwen Δ 范围
152	- **当前**: `$\Delta$ increases from $0.04$ at $s{=}0.15$ to $2.94$ at $s{=}0.30$`
153	- **替换**: n=500 Qwen Δ 值
154	
155	### R12 [data_update] Line 71 — DeepSeek/Qwen 倍数比
156	- **当前**: `${\sim}1/5$ the magnitude`
157	- **替换**: n=500 Qwen/DeepSeek 比值
158	
159	### R13 [data_update] Line 71 — Qwen 统计
160	- **当前**: `Spearman $\rho = 1.0$; gradient permutation $p = 0.043$`
161	- **替换**: n=500 Qwen 对应统计量
162	
163	### R14 [data_update] Line 71 — Qwen s015 d_z
164	- **当前**: `$d_z{=}0.28$, CI includes zero`
165	- **替换**: n=500 Qwen s015 d_z + CI
166	- **注意**: D052 预注册——若 s015 仍 ns，叙事改为 "emerges above threshold"
167	
168	### R15 [data_update] Line 71 — Qwen d_z 下界
169	- **当前**: `$d_z \geq 0.55$`
170	- **替换**: n=500 Qwen s≥0.20 d_z 值
171	
172	### R16 [data_update] Line 77 — §5.5 LLaMA 样本量
173	- **当前**: `$n{=}49$ paired problems`
174	- **替换**: 确认 LLaMA 是否也跑 n=500；若仍 n=49 则保留
175	
176	### R17 [constraint_check] Lines 79 — §5.5 LLaMA d_z（D059 违规 ⚠️）
177	- **当前**: `monotonically increasing paired $d_z$ ($0.19 \to 0.26 \to 0.29 \to 0.34$)`
178	- **问题**: 此 d_z 是 imp-vs-rand paired Cohen's d，D059 禁止报告
179	- **修改**: 删除 imp-vs-rand d_z，改为 Wilcoxon p + median_diff
180	
181	### R18 [constraint_check] Lines 79 — LLaMA within-importance d_z
182	- **当前**: `within-strategy phase gradient $d_z$ (low $-$ high) is consistently large at all sparsity levels ($d_z \in [1.00, 1.12]$)`
183	- **状态**: 合规 ✓（within-importance），数值可能需更新（若 LLaMA 重跑）
184	
185	### R19 [constraint_check] Lines 79 — LLaMA random d_z
186	- **当前**: `$d_z \in [0.35, 0.45]$`
187	- **问题**: D059 — random 不报 d_z
188	- **修改**: 改为 "random eviction also shows non-trivial phase gradient" + Wilcoxon p
189	
190	### R20 [data_update] Lines 81 — LLaMA 倍数比
191	- **当前**: `${\sim}40{\times}$ smaller than DeepSeek and ${\sim}7{\times}$ smaller than Qwen`
192	- **替换**: 用 n=500 DeepSeek/Qwen 数据重算比值
193	
194	### R21 [structural] Lines 83-98 — Table 3 (llama-cross-arch) 重构
195	- **当前**: d_z 列报告 imp-vs-rand Cohen's d
196	- **问题**: D059 违规 — 整列需要替换
197	- **修改**: d_z 列改为 within-importance d_z（或删除 d_z 列，改为 Wilcoxon p + median_diff）
198	- **数据**: 若 LLaMA 不重跑，数值不变但列定义需改
199	
200	### R22 [data_update] Lines 92-95 — Table 3 数据行
201	- **当前**: 4 行 (d_z, Δ̃ [CI], p_Bonf)
202	- **替换**: 若 LLaMA 重跑则全部更新；若不重跑，仅结构变动
203	
204	### R23 [data_update] Line 104 — §5.6 permutation test 结果
205	- **当前**: `$p_{\text{Bonf}} < 0.005$`, `$0.37$ at $s{=}0.15$ to $9.85$ at $s{=}0.30$`
206	- **替换**: n=500 permutation test 统计
207	
208	### R24 [data_update] Lines 106 — DeepSeek d_z 范围
209	- **当前**: `$d_z{=}0.44$ (small) to $d_z{=}0.80$ (large)`
210	- **替换**: n=500 DeepSeek within-importance d_z
211	
212	### R25 [data_update] Lines 106 — Qwen d_z
213	- **当前**: `$d_z{=}0.28$, CI includes zero`, `$d_z \geq 0.55$`, `$d_z{=}0.89$/$1.02$ vs.\ $0.68$/$0.80$`
214	- **替换**: n=500 Qwen d_z 值
215	
216	### R26 [data_update] Lines 113-123 — Table 4 (cohens-d) 全部数据
217	- **当前**: 4 行 × (DS d_z, Δ̃ [CI], QW d_z, Δ̃ [CI])
218	- **替换**: n=500 paired d_z + bootstrap Δ̃ + CI（16 个数字）
219	
220	---
221	
222	## §6 Analysis (analysis.tex)
223	
224	### AN01 [data_update] Line 4 — Gini 系数范围
225	- **当前**: `$0.030$--$0.081$ (DeepSeek) and $0.010$--$0.020$ (Qwen)`
226	- **替换**: n=500 Gini Δ 范围（若 C4 entropy 分析基于 n=500 重跑）
227	- **注意**: C4 已降为 supporting analysis (D045/D046)，数值可能不变
228	
229	### AN02 [data_update] Line 6 — DeepSeek entropy Δ 范围
230	- **当前**: `$\Delta\mathcal{H} \in [-0.047, -0.040]$`
231	- **替换**: 若 C4 基于 n=500 重跑则更新
232	
233	### AN03 [data_update] Line 6 — Qwen entropy 反转
234	- **当前**: `$s{=}0.25$ ($\Delta\mathcal{H} = +0.045$)`
235	- **替换**: 若 C4 基于 n=500 重跑则更新
236	
237	---
238	
239	## §7 Discussion (discussion.tex)
240	
241	### D01 [data_update] Line 5 — Gradient 范围
242	- **当前**: `$69$--$274{\times}$`
243	- **替换**: 与 R05 同步
244	
245	### D02 [data_update] Line 5 — Crossover 数值
246	- **当前**: `$\widetilde{\mathrm{II}} = 0.032$ vs.\ $0.818$` 和 `$7.196$ vs.\ $1.363$`
247	- **替换**: 与 R10 同步
248	
249	### D03 [data_update] Line 11 — LLaMA 倍数
250	- **当前**: `${\sim}40{\times}$ smaller than DeepSeek, ${\sim}7{\times}$ smaller than Qwen`
251	- **替换**: 与 R20 同步
252	
253	### D04 [constraint_check] Line 11 — LLaMA d_z（D059 违规 ⚠️）
254	- **当前**: `within-strategy phase gradient $d_z \geq 1.0$`
255	- **状态**: 这是 within-importance d_z，合规 ✓
256	
257	### D05 [constraint_check] Line 11 — LLaMA random d_z（D059 违规 ⚠️）
258	- **当前**: `$d_z \in [0.35, 0.45]$`
259	- **修改**: 与 R19 同步——删除 d_z，改为定性描述 + Wilcoxon p
260	
261	### D06 [claim_update] Line 11 — LLaMA 语言（D060）
262	- **当前**: `provides partial support for the qualitative pattern`
263	- **状态**: 合规 ✓（"partial support"）
264	
265	---
266	
267	## §8 Conclusion (conclusion.tex)
268	
269	### C01 [data_update] Line 4 — Gradient 范围
270	- **当前**: `$69{\times}$ to $274{\times}$`
271	- **替换**: 与 R05 同步
272	
273	### C02 [data_update] Line 4 — d_z 范围
274	- **当前**: `$d_z$: $0.44 \to 0.80$`
275	- **替换**: 与 R24 同步
276	
277	### C03 [data_update] Line 4 — Random PASS/FAIL
278	- **当前**: `7/8 conditions non-significant`
279	- **替换**: 与 I04 同步
280	
281	### C04 [data_update] Line 4 — Qwen d_z
282	- **当前**: `$d_z \geq 0.55$`
283	- **替换**: 与 R15 同步
284	
285	### C05 [data_update] Line 4 — LLaMA 倍数
286	- **当前**: `$\sim$1/40 the magnitude`
287	- **替换**: 与 A08 同步
288	
289	### C06 [constraint_check] — C5b future work（D056）
290	- **当前**: `These findings motivate phase-aware sparsity allocation for reasoning model deployment.`
291	- **状态**: 合规 ✓ — 作为 motivation 而非 contribution claim
292	
293	---
294	
295	## Limitations (limitations.tex)
296	
297	### L01 [data_update] Line 1 — 架构描述
298	- **状态**: 无直接 n=50 数据，无需数字更新
299	
300	### L02 [claim_update] Line 4 — 样本量描述
301	- **当前**: 未直接提及 n=50，但 "exclusively on MATH-500" 成立
302	- **替换**: n=500 后可加 "using 500 problems from MATH-500"
303	
304	---
305	
306	## Appendix A (appendix.tex) — Formulation + Multiplicative Null
307	
308	### AP01 [data_update] Line 38 — Multiplicative null G 范围
309	- **当前**: `$G_{\times} = 58$--$241{\times}$`
310	- **替换**: n=500 multiplicative null G 值（需重算）
311	
312	---
313	
314	## Appendix B (appendix_results.tex) — Cross-Model Summary
315	
316	### AR01 [data_update] Line 7 — Per-problem concordance
317	- **当前**: `mean $\rho = -0.11$, $p = 0.926$`
318	- **替换**: n=500 cross-model concordance（Spearman ρ + p）
319	
320	### AR02 [data_update] Line 10 — Random PASS/FAIL 模式
321	- **当前**: `3/4 FAIL`, `4/4 FAIL`
322	- **替换**: n=500 random PASS/FAIL 计数
323	
324	### AR03 [data_update] Line 10 — Qwen random s030 例外
325	- **当前**: `$p = 0.012$`, `$d_z = -0.04$`
326	- **替换**: n=500 结果
327	- **注意**: D059 — 不报 d_z，改为 Wilcoxon p + median_diff
328	
329	---
330	
331	## Appendix C (appendix_moved.tex) — Crossover + Cross-Model + Permutation + Analysis
332	
333	### AM01 [data_update] Line 11 — Crossover 全部数值
334	- **当前**: `$0.032$ vs.\ $0.818$`, `$7.196$ vs.\ $1.363$`, `$5.3{\times}$`, `$3.9{\times}$, $5.4{\times}$, $5.3{\times}$, $3.6{\times}$`
335	- **替换**: n=500 crossover 值（所有 4 个 sparsity level 的 reversal magnitude）
336	
337	### AM02 [figure_update] Lines 13-18 — Figure 3 (fig3_crossover.pdf)
338	- **操作**: 用 n=500 数据重新生成
339	- **caption**: `$5.3{\times}$` 需同步更新
340	
341	### AM03 [data_update] Line 26 — Qwen 排除数
342	- **当前**: `Four of the 50 problems are excluded`, `$n{=}46$`, `$n{=}49$`
343	- **替换**: n=500 的 DeepSeek/Qwen 有效 n
344	
345	### AM04 [data_update] Lines 39-40 — Table (cross-model) 全部数据
346	- **当前**: DeepSeek [0.39, 1.48, 7.16, 14.59], Qwen [0.04, 0.23, 1.27, 2.94]
347	- **替换**: n=500 median Δ 值（8 个数字）
348	
349	### AM05 [figure_update] Lines 45-50 — Figure 5 (fig5_crossmodel.pdf)
350	- **操作**: 用 n=500 数据重新生成
351	- **caption**: "one-fifth" 比例需同步更新
352	
353	### AM06 [data_update] Lines 52-53 — Per-problem concordance（重复 AR01）
354	- **替换**: 与 AR01 同步
355	
356	### AM07 [data_update] Lines 55-56 — Random PASS/FAIL（重复 AR02/AR03）
357	- **替换**: 与 AR02/AR03 同步
358	
359	### AM08 [data_update] Lines 62, 73 — Permutation test 样本量
360	- **当前**: `$n{=}49$`
361	- **替换**: n=500 有效 n
362	
363	### AM09 [data_update] Lines 68 — CI lower bounds
364	- **当前**: `$0.19 \to 0.69 \to 1.66 \to 6.70$`
365	- **替换**: n=500 CI lower bounds
366	
367	### AM10 [data_update] Lines 79-82 — Table (permutation) 全部数据
368	- **当前**: 4 行 (observed Δ̃, 95% CI, p_Bonf)
369	- **替换**: n=500 permutation test 结果（12 个数字）
370	
371	### AM11 [figure_update] Lines 87-92 — Figure 4 (fig4_bootstrap.pdf)
372	- **操作**: 用 n=500 数据重新生成
373	
374	### AM12 [data_update] Lines 111-122 — Table (discrimination-metrics-full) 全部数据
375	- **当前**: 8 行 (ΔGini, ΔCV)
376	- **替换**: 若 C4 分析基于 n=500 重跑则更新（16 个数字）
377	
378	### AM13 [data_update] Lines 137-139 — Entropy delta 描述
379	- **当前**: DeepSeek `$\Delta\mathcal{H} \in [-0.047, -0.040]$`, Qwen s025 `$+0.045$`
380	- **替换**: 若 C4 分析基于 n=500 重跑则更新
381	
382	### AM14 [data_update] Lines 149-162 — Table (entropy-deltas) 全部数据
383	- **当前**: 8 行
384	- **替换**: 若 C4 分析基于 n=500 重跑则更新
385	
386	---
387	
388	## Appendix D (appendix_disc_analysis.tex) — Extended Discussion + Limitations
389	
390	### AD01 [data_update] Line 4 — Random Gini 范围
391	- **当前**: `$-0.031$ to $-0.073$; Qwen: $-0.019$ to $-0.045$`
392	- **替换**: 若 C4 基于 n=500 重跑则更新
393	
394	### AD02 [data_update] Line 11 — High-phase II 上限
395	- **当前**: `$\widetilde{\mathrm{II}}_{\text{high}} < 0.06$ at $s \leq 0.30$`; `$s = 0.35$, high-phase II rises to $0.105$`
396	- **替换**: n=500 high-phase median II 值
397	
398	### AD03 [data_update] Line 14 — Random 7/8 统计
399	- **当前**: `7/8`, `$p{=}0.012$`, `$d_z{=}{-}0.04$`
400	- **替换**: 与 A04 同步
401	- **注意**: D059 — 不报 d_z
402	
403	### AD04 [data_update] Lines 44-47 — 统计范围详情
404	- **当前**: `$n{=}49$ ... $n{=}46$`, mean/median ratio `${\sim}1.6{:}1$`, permutation CI 值
405	- **替换**: n=500 统计
406	
407	### AD05 [data_update] Line 49 — Qwen random s030 例外
408	- **当前**: `$p{=}0.012$`, `$d_z{=}{-}0.04$`
409	- **替换**: 与 AR03 同步
410	- **注意**: D059 — 不报 d_z
411	
412	### AD06 [data_update] Lines 53-57 — Growth rate 描述
413	- **当前**: `$3.8{\times} \to 4.8{\times} \to 2.0{\times}$`
414	- **替换**: n=500 Δ growth rate
415	
416	---
417	
418	## 图表重新生成清单
419	
420	| # | 文件名 | 数据来源 | 引用位置 |
421	|---|--------|----------|----------|
422	| F1 | fig1_dose_response.pdf | n=500 DeepSeek imp+rand G vs s | results.tex:57, caption:58 |
423	| F2 | fig3_crossover.pdf | n=500 DeepSeek s=0.25 crossover | appendix_moved.tex:15 |
424	| F3 | fig4_bootstrap.pdf | n=500 permutation test forest plot | appendix_moved.tex:89 |
425	| F4 | fig5_crossmodel.pdf | n=500 DeepSeek+Qwen Δ comparison | appendix_moved.tex:47 |
426	| F5 | (unnamed hero figure if separate) | 确认是否与 fig1 相同 | results.tex:57 |
427	
428	---
429	
430	## 硬约束合规审查
431	
432	### HC01 [D054] II 只报 median + median bootstrap CI ✅
433	- abstract/results/discussion 全文使用 median ($\widetilde{\mathrm{II}}$)
434	- methodology.tex:18 提及 mean/median ratio 作为选择 median 的理由 ✓
435	- **注意**: n=500 更新时确认所有新数字均为 median
436	
437	### HC02 [D059] d_z 只报 within-importance ⚠️ 6 处违规
438	| 位置 | 当前内容 | 问题 |
439	|------|---------|------|
440	| abstract.tex:8 | random `$d_z{=}{-}0.04$` | imp-vs-rand d_z |
441	| results.tex:79 | LLaMA `$d_z$ ($0.19 \to 0.34$)` | imp-vs-rand d_z |
442	| results.tex:79 | random `$d_z \in [0.35, 0.45]$` | random d_z |
443	| results.tex:88-97 | Table 3 d_z 列 | imp-vs-rand d_z |
444	| discussion.tex:11 | `$d_z \in [0.35, 0.45]$` | random d_z |
445	| appendix_disc_analysis.tex:14,49 | `$d_z{=}{-}0.04$` | random d_z |
446	
447	**修改方案**: 所有 imp-vs-rand 和 random d_z 替换为 Wilcoxon p + median_diff；Table 3 d_z 列替换为 within-importance d_z 或移除
448	
449	### HC03 [D015] Framing: emergent phase-strategy interaction ✅
450	- abstract.tex:4 使用 "emergent phase-strategy interaction" ✓
451	- 全文无 "importance is broken" 叙事 ✓
452	
453	### HC04 [D056] C5b 已降为 §8 future work ✅
454	- discussion.tex:8 讨论 phase-aware budget 作为 implication（未 claim 实现）✓
455	- conclusion.tex:5 "motivate phase-aware sparsity allocation" ✓
456	- **注意**: D056 确认 c5b_pilot gate_failed (oracle 18% < 30%)，论文不应 claim C5b 成功
457	
458	### HC05 [D060] C8 LLaMA 用 suggests/partial support ✅
459	- abstract.tex:10 "suggests cross-architecture generalization" ✓
460	- discussion.tex:11 "provides partial support" ✓
461	- conclusion.tex:4 "partially extends" ✓
462	- results.tex:77-81 "The qualitative pattern replicates" — **borderline**，建议改为 "The qualitative pattern is directionally consistent"
463	
464	### HC06 [硬约束 #6] Random 也有正 II，区分信号是 gradient ✅
465	- results.tex Table 2 显示 random 有正 II ✓
466	- 叙事正确区分："compound severity depends qualitatively on eviction strategy" ✓
467	- **注意**: n=500 random 数据可能有不同 pattern，需重新验证此叙事
468	
469	---
470	
471	## 按 Section 分布
472	
473	| Section | 更新点数 |
474	|---------|---------|
475	| Abstract | 8 |
476	| Introduction | 4 |
477	| Methodology | 3 |
478	| Results | 26 |
479	| Analysis | 3 |
480	| Discussion | 6 |
481	| Conclusion | 6 |
482	| Limitations | 2 |
483	| Appendix (formulation) | 1 |
484	| Appendix (results summary) | 3 |
485	| Appendix (moved content) | 14 |
486	| Appendix (disc+limitations) | 6 |
487	| **Total** | **82** (含重复引用) |
488	| **Unique** | **~70** |
489	
490	---
491	
492	## 高风险点（可能需要改叙事）
493	
494	### RISK-1: Qwen s015 是否仍然 non-significant
495	- D052 预注册：若 n=500 Qwen s015 仍 ns，叙事改为 "compound effect emerges above a model-dependent threshold"
496	- D061 已确认 n=500 下 Qwen s015 显著 (p<0.0001)——**如果最终数据确认，此风险解除**
497	- 影响范围：abstract, introduction, results §5.4, §5.6, conclusion
498	
499	### RISK-2: Random PASS/FAIL 模式可能变化
500	- n=50 下 7/8 FAIL（Qwen s030 borderline PASS d≈0）
501	- n=500 功效更高，可能检测到更多 borderline 显著
502	- 影响范围：需重新评估 "no significant phase modulation" 叙事
503	- D059 保护：不报 random d_z，用 Wilcoxon p + median_diff 更 robust
504	
505	### RISK-3: LLaMA 数据是否跑 n=500
506	- 当前 LLaMA 仅 n=49
507	- 若不重跑：DeepSeek/Qwen 倍数比需重算（分母变了）
508	- 若重跑：全部 LLaMA 数据需更新
509	
510	### RISK-4: D059 Table 3 重构
511	- Table 3 (llama-cross-arch) 的核心组织方式围绕 imp-vs-rand d_z
512	- 删除 d_z 列后需要替代结构，可能影响 §5.5 整段叙事
513	
514	### RISK-5: Crossover pattern 在 n=500 是否稳定
515	- crossover 是论文的一个 key finding
516	- n=500 的 crossover 倍数和位置可能变化
517	- 影响范围：abstract, results §5.3, discussion, appendix
518	
519	### RISK-6: C4 entropy 分析是否需要基于 n=500 重跑
520	- 当前 C4 降级为 supporting analysis (D045/D046)
521	- 若不重跑：analysis.tex 和 appendix 表格保留 n=50 数据，需标注
522	- 若重跑：AN01-AN03, AM12-AM14, AD01 全部更新
523	
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10233ec7-5d03-448a-9224-b6173ea0cbe8",
  "uuid": "2cc31d7e-6312-45e1-bb4e-90a41212c380",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/n500_update_checklist.md",
      "content": "# n=500 更新清单\n\n> 论文：Phase-Modulated Compound Sparsity (EMNLP 2026 ARR)\n> 当前数据：n=50 MATH-500（DeepSeek n=49, Qwen n=46, LLaMA n=49）\n> 目标数据：n=500 MATH-500\n> 生成日期：2026-05-14\n> 硬约束：D054 (median only), D059 (within-imp d_z only), D015 (emergent interaction framing), D056 (C5b→future work), D060 (LLaMA→suggests)\n\n---\n\n## 统计汇总\n\n| 分类 | 数量 |\n|------|------|\n| data_update（数字替换） | 48 |\n| figure_update（重新生成） | 5 |\n| claim_update（措辞调整） | 8 |\n| structural（结构变动） | 3 |\n| constraint_check（硬约束合规） | 6 |\n| **总计** | **70** |\n\n---\n\n## §0 Abstract (abstract.tex)\n\n### A01 [data_update] Line 6 — 样本量\n- **当前**: `50 MATH-500 problems`\n- **替换**: `500 MATH-500 problems`\n- **依赖**: n=500 DeepSeek/Qwen 有效样本量（扣除 degenerate phase 后实际 n）\n\n### A02 [data_update] Line 7 — DeepSeek 主结果\n- **当前**: `median Interaction Index difference between low-sparsity and high-sparsity reasoning phases increases monotonically from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$`\n- **替换**: n=500 DeepSeek importance Δ 值（4 个 sparsity level）\n- **来源**: experiment_summary_table.json → median_diff\n\n### A03 [data_update] Line 7 — DeepSeek d_z 和 p\n- **当前**: `paired Cohen's $d_z$ growing from $0.44$ (small) to $0.80$ (large); Bonferroni-corrected permutation tests yield $p < 0.005$`\n- **替换**: n=500 DeepSeek within-importance paired d_z（4 值）+ 新 p-values\n- **注意**: D059 — 此处 d_z 是 within-importance (low−high)，合规 ✓\n\n### A04 [data_update] Line 8 — Random baseline 统计\n- **当前**: `Random eviction produces no significant phase modulation in 7/8 conditions; the single exception (Qwen $s{=}0.30$, $p{=}0.012$) shows negligible effect size ($d_z{=}{-}0.04$)`\n- **替换**: n=500 random 条件的 PASS/FAIL 计数 + 例外条件的 p 和效应量\n- **注意**: D059 — random 条件不报 d_z，改为 Wilcoxon p + median_diff\n\n### A05 [data_update] Line 9 — Crossover 数值\n- **当前**: `$\\widetilde{\\mathrm{II}} = 0.032$ vs.\\ $0.818$` 和 `$7.196$ vs.\\ $1.363$`\n- **替换**: n=500 s=0.25 crossover 的 4 个 II 中位数\n\n### A06 [data_update] Line 10 — Qwen 复现\n- **当前**: `$d_z \\geq 0.55$; Spearman $\\rho = 1.0$; gradient permutation $p = 0.043$`\n- **替换**: n=500 Qwen within-importance d_z + Spearman ρ + permutation p\n\n### A07 [data_update] Line 10 — LLaMA 数值\n- **当前**: `$d_z$ ($0.19 \\to 0.34$; $s{=}0.30$ Wilcoxon $p_{\\text{Bonf}} = 0.029$)`\n- **替换**: LLaMA 数据未变（n=49），但需确认是否也跑 n=500\n- **注意**: D059 违规 ⚠️ — 此 d_z 是 imp-vs-rand，应改为 Wilcoxon p + median_diff\n- **注意**: D060 — 当前用 \"suggests\"，合规 ✓\n\n### A08 [data_update] Line 10 — LLaMA 倍数比\n- **当前**: `${\\sim}$1/40 the absolute magnitude`\n- **替换**: 用 n=500 DeepSeek 数据重算 LLaMA/DeepSeek 比值\n\n---\n\n## §1 Introduction (introduction.tex)\n\n### I01 [data_update] Line 14 — DeepSeek 主结果\n- **当前**: `$0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$ ($d_z$: $0.44 \\to 0.80$; Bonferroni-corrected $p < 0.005$)`\n- **替换**: 与 A02/A03 同步\n\n### I02 [data_update] Line 15 — Qwen d_z\n- **当前**: `$d_z \\geq 0.55$`\n- **替换**: n=500 Qwen within-importance d_z 下界\n\n### I03 [data_update] Line 15 — LLaMA 倍数\n- **当前**: `$\\sim$1/40 the magnitude`\n- **替换**: 与 A08 同步\n\n### I04 [data_update] Line 16 — Random PASS/FAIL 统计\n- **当前**: `7/8 conditions non-significant`\n- **替换**: n=500 random PASS/FAIL 计数\n\n---\n\n## §4 Experimental Setup (methodology.tex)\n\n### M01 [data_update] Line 10 — 样本量\n- **当前**: `50 problems stratified from MATH-500`\n- **替换**: `500 problems from MATH-500`（去掉 \"stratified\"，500 ≈ 全集）\n\n### M02 [data_update] Line 18 — 偏度统计\n- **当前**: `mean/median ratios up to 43:1`\n- **替换**: n=500 的 mean/median ratio\n- **注意**: D054 — 此处引用 mean/median 比作为选择 median 的理由，合规 ✓\n\n### M03 [data_update] Line 22 — p-value 总结\n- **当前**: `All tests yield $p_{\\text{Bonf}} < 0.005$ at every sparsity level.`\n- **替换**: n=500 permutation test 结果\n\n---\n\n## §5 Results (results.tex)\n\n### R01 [data_update] Lines 8 — §5.1 aggregate Δ\n- **当前**: `$\\Delta$ increases from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$---a $37{\\times}$ amplification`\n- **替换**: n=500 Δ 值 + 新倍数\n\n### R02 [data_update] Line 8 — Random Δ 范围\n- **当前**: `$-0.02$ to $1.54$`\n- **替换**: n=500 random Δ 范围\n\n### R03 [data_update] Line 13 — Table 1 标题样本量\n- **当前**: `$n{=}50$ MATH-500 problems`\n- **替换**: `$n{=}500$`（或实际有效 n）\n\n### R04 [data_update] Lines 19-20 — Table 1 (aggregate-ii) 全部数据\n- **当前**:\n  ```\n  Importance & 0.39 & 1.48 & 7.16 & 14.59\n  Random     & 0.01 & −0.02 & 0.54 & 1.54\n  ```\n- **替换**: n=500 median Δ 值（8 个数字）\n\n### R05 [data_update] Line 29 — §5.2 severity gradient G\n- **当前**: `$69{\\times}$ at $s{=}0.15$ to $274{\\times}$ at $s{=}0.30$`\n- **替换**: n=500 G 值\n- **注意**: D031/D033 决定 gradient ratio 仅作辅助描述；确认 n=500 是否仍报 G\n\n### R06 [data_update] Line 29 — high-phase II 范围\n- **当前**: `$\\widetilde{\\mathrm{II}}_{\\textit{high}}$ ranges from $0.006$ to $0.053$`\n- **替换**: n=500 high-phase median II 范围\n\n### R07 [data_update] Line 29 — Random G 范围\n- **当前**: `$G \\approx 0.9$--$1.7{\\times}$`\n- **替换**: n=500 random G 范围\n\n### R08 [data_update] Lines 34, 40-50 — Table 2 (main-results) 全部数据\n- **当前**: \"50 problems\" + 24 个数据单元格（6列×4组）\n- **替换**: n=500 全部 per-phase median II + Δ + G（24 个数字 + caption 中 n）\n\n### R09 [figure_update] Lines 55-60 — Figure 1 (fig1_dose_response.pdf)\n- **当前**: 基于 n=50 bf16 数据\n- **操作**: 用 n=500 数据重新生成 fig1_dose_response.pdf\n- **注意**: caption 中 \"$69{\\times}$ to $274{\\times}$\" 需同步更新\n\n### R10 [data_update] Line 66 — §5.3 Crossover 数值\n- **当前**: `$0.032$ vs.\\ $0.818$`, `$7.196$ vs.\\ $1.363$---a $5.3{\\times}$ reversal`\n- **替换**: n=500 s=0.25 crossover 值 + 倍数\n\n### R11 [data_update] Line 71 — §5.4 Qwen Δ 范围\n- **当前**: `$\\Delta$ increases from $0.04$ at $s{=}0.15$ to $2.94$ at $s{=}0.30$`\n- **替换**: n=500 Qwen Δ 值\n\n### R12 [data_update] Line 71 — DeepSeek/Qwen 倍数比\n- **当前**: `${\\sim}1/5$ the magnitude`\n- **替换**: n=500 Qwen/DeepSeek 比值\n\n### R13 [data_update] Line 71 — Qwen 统计\n- **当前**: `Spearman $\\rho = 1.0$; gradient permutation $p = 0.043$`\n- **替换**: n=500 Qwen 对应统计量\n\n### R14 [data_update] Line 71 — Qwen s015 d_z\n- **当前**: `$d_z{=}0.28$, CI includes zero`\n- **替换**: n=500 Qwen s015 d_z + CI\n- **注意**: D052 预注册——若 s015 仍 ns，叙事改为 \"emerges above threshold\"\n\n### R15 [data_update] Line 71 — Qwen d_z 下界\n- **当前**: `$d_z \\geq 0.55$`\n- **替换**: n=500 Qwen s≥0.20 d_z 值\n\n### R16 [data_update] Line 77 — §5.5 LLaMA 样本量\n- **当前**: `$n{=}49$ paired problems`\n- **替换**: 确认 LLaMA 是否也跑 n=500；若仍 n=49 则保留\n\n### R17 [constraint_check] Lines 79 — §5.5 LLaMA d_z（D059 违规 ⚠️）\n- **当前**: `monotonically increasing paired $d_z$ ($0.19 \\to 0.26 \\to 0.29 \\to 0.34$)`\n- **问题**: 此 d_z 是 imp-vs-rand paired Cohen's d，D059 禁止报告\n- **修改**: 删除 imp-vs-rand d_z，改为 Wilcoxon p + median_diff\n\n### R18 [constraint_check] Lines 79 — LLaMA within-importance d_z\n- **当前**: `within-strategy phase gradient $d_z$ (low $-$ high) is consistently large at all sparsity levels ($d_z \\in [1.00, 1.12]$)`\n- **状态**: 合规 ✓（within-importance），数值可能需更新（若 LLaMA 重跑）\n\n### R19 [constraint_check] Lines 79 — LLaMA random d_z\n- **当前**: `$d_z \\in [0.35, 0.45]$`\n- **问题**: D059 — random 不报 d_z\n- **修改**: 改为 \"random eviction also shows non-trivial phase gradient\" + Wilcoxon p\n\n### R20 [data_update] Lines 81 — LLaMA 倍数比\n- **当前**: `${\\sim}40{\\times}$ smaller than DeepSeek and ${\\sim}7{\\times}$ smaller than Qwen`\n- **替换**: 用 n=500 DeepSeek/Qwen 数据重算比值\n\n### R21 [structural] Lines 83-98 — Table 3 (llama-cross-arch) 重构\n- **当前**: d_z 列报告 imp-vs-rand Cohen's d\n- **问题**: D059 违规 — 整列需要替换\n- **修改**: d_z 列改为 within-importance d_z（或删除 d_z 列，改为 Wilcoxon p + median_diff）\n- **数据**: 若 LLaMA 不重跑，数值不变但列定义需改\n\n### R22 [data_update] Lines 92-95 — Table 3 数据行\n- **当前**: 4 行 (d_z, Δ̃ [CI], p_Bonf)\n- **替换**: 若 LLaMA 重跑则全部更新；若不重跑，仅结构变动\n\n### R23 [data_update] Line 104 — §5.6 permutation test 结果\n- **当前**: `$p_{\\text{Bonf}} < 0.005$`, `$0.37$ at $s{=}0.15$ to $9.85$ at $s{=}0.30$`\n- **替换**: n=500 permutation test 统计\n\n### R24 [data_update] Lines 106 — DeepSeek d_z 范围\n- **当前**: `$d_z{=}0.44$ (small) to $d_z{=}0.80$ (large)`\n- **替换**: n=500 DeepSeek within-importance d_z\n\n### R25 [data_update] Lines 106 — Qwen d_z\n- **当前**: `$d_z{=}0.28$, CI includes zero`, `$d_z \\geq 0.55$`, `$d_z{=}0.89$/$1.02$ vs.\\ $0.68$/$0.80$`\n- **替换**: n=500 Qwen d_z 值\n\n### R26 [data_update] Lines 113-123 — Table 4 (cohens-d) 全部数据\n- **当前**: 4 行 × (DS d_z, Δ̃ [CI], QW d_z, Δ̃ [CI])\n- **替换**: n=500 paired d_z + bootstrap Δ̃ + CI（16 个数字）\n\n---\n\n## §6 Analysis (analysis.tex)\n\n### AN01 [data_update] Line 4 — Gini 系数范围\n- **当前**: `$0.030$--$0.081$ (DeepSeek) and $0.010$--$0.020$ (Qwen)`\n- **替换**: n=500 Gini Δ 范围（若 C4 entropy 分析基于 n=500 重跑）\n- **注意**: C4 已降为 supporting analysis (D045/D046)，数值可能不变\n\n### AN02 [data_update] Line 6 — DeepSeek entropy Δ 范围\n- **当前**: `$\\Delta\\mathcal{H} \\in [-0.047, -0.040]$`\n- **替换**: 若 C4 基于 n=500 重跑则更新\n\n### AN03 [data_update] Line 6 — Qwen entropy 反转\n- **当前**: `$s{=}0.25$ ($\\Delta\\mathcal{H} = +0.045$)`\n- **替换**: 若 C4 基于 n=500 重跑则更新\n\n---\n\n## §7 Discussion (discussion.tex)\n\n### D01 [data_update] Line 5 — Gradient 范围\n- **当前**: `$69$--$274{\\times}$`\n- **替换**: 与 R05 同步\n\n### D02 [data_update] Line 5 — Crossover 数值\n- **当前**: `$\\widetilde{\\mathrm{II}} = 0.032$ vs.\\ $0.818$` 和 `$7.196$ vs.\\ $1.363$`\n- **替换**: 与 R10 同步\n\n### D03 [data_update] Line 11 — LLaMA 倍数\n- **当前**: `${\\sim}40{\\times}$ smaller than DeepSeek, ${\\sim}7{\\times}$ smaller than Qwen`\n- **替换**: 与 R20 同步\n\n### D04 [constraint_check] Line 11 — LLaMA d_z（D059 违规 ⚠️）\n- **当前**: `within-strategy phase gradient $d_z \\geq 1.0$`\n- **状态**: 这是 within-importance d_z，合规 ✓\n\n### D05 [constraint_check] Line 11 — LLaMA random d_z（D059 违规 ⚠️）\n- **当前**: `$d_z \\in [0.35, 0.45]$`\n- **修改**: 与 R19 同步——删除 d_z，改为定性描述 + Wilcoxon p\n\n### D06 [claim_update] Line 11 — LLaMA 语言（D060）\n- **当前**: `provides partial support for the qualitative pattern`\n- **状态**: 合规 ✓（\"partial support\"）\n\n---\n\n## §8 Conclusion (conclusion.tex)\n\n### C01 [data_update] Line 4 — Gradient 范围\n- **当前**: `$69{\\times}$ to $274{\\times}$`\n- **替换**: 与 R05 同步\n\n### C02 [data_update] Line 4 — d_z 范围\n- **当前**: `$d_z$: $0.44 \\to 0.80$`\n- **替换**: 与 R24 同步\n\n### C03 [data_update] Line 4 — Random PASS/FAIL\n- **当前**: `7/8 conditions non-significant`\n- **替换**: 与 I04 同步\n\n### C04 [data_update] Line 4 — Qwen d_z\n- **当前**: `$d_z \\geq 0.55$`\n- **替换**: 与 R15 同步\n\n### C05 [data_update] Line 4 — LLaMA 倍数\n- **当前**: `$\\sim$1/40 the magnitude`\n- **替换**: 与 A08 同步\n\n### C06 [constraint_check] — C5b future work（D056）\n- **当前**: `These findings motivate phase-aware sparsity allocation for reasoning model deployment.`\n- **状态**: 合规 ✓ — 作为 motivation 而非 contribution claim\n\n---\n\n## Limitations (limitations.tex)\n\n### L01 [data_update] Line 1 — 架构描述\n- **状态**: 无直接 n=50 数据，无需数字更新\n\n### L02 [claim_update] Line 4 — 样本量描述\n- **当前**: 未直接提及 n=50，但 \"exclusively on MATH-500\" 成立\n- **替换**: n=500 后可加 \"using 500 problems from MATH-500\"\n\n---\n\n## Appendix A (appendix.tex) — Formulation + Multiplicative Null\n\n### AP01 [data_update] Line 38 — Multiplicative null G 范围\n- **当前**: `$G_{\\times} = 58$--$241{\\times}$`\n- **替换**: n=500 multiplicative null G 值（需重算）\n\n---\n\n## Appendix B (appendix_results.tex) — Cross-Model Summary\n\n### AR01 [data_update] Line 7 — Per-problem concordance\n- **当前**: `mean $\\rho = -0.11$, $p = 0.926$`\n- **替换**: n=500 cross-model concordance（Spearman ρ + p）\n\n### AR02 [data_update] Line 10 — Random PASS/FAIL 模式\n- **当前**: `3/4 FAIL`, `4/4 FAIL`\n- **替换**: n=500 random PASS/FAIL 计数\n\n### AR03 [data_update] Line 10 — Qwen random s030 例外\n- **当前**: `$p = 0.012$`, `$d_z = -0.04$`\n- **替换**: n=500 结果\n- **注意**: D059 — 不报 d_z，改为 Wilcoxon p + median_diff\n\n---\n\n## Appendix C (appendix_moved.tex) — Crossover + Cross-Model + Permutation + Analysis\n\n### AM01 [data_update] Line 11 — Crossover 全部数值\n- **当前**: `$0.032$ vs.\\ $0.818$`, `$7.196$ vs.\\ $1.363$`, `$5.3{\\times}$`, `$3.9{\\times}$, $5.4{\\times}$, $5.3{\\times}$, $3.6{\\times}$`\n- **替换**: n=500 crossover 值（所有 4 个 sparsity level 的 reversal magnitude）\n\n### AM02 [figure_update] Lines 13-18 — Figure 3 (fig3_crossover.pdf)\n- **操作**: 用 n=500 数据重新生成\n- **caption**: `$5.3{\\times}$` 需同步更新\n\n### AM03 [data_update] Line 26 — Qwen 排除数\n- **当前**: `Four of the 50 problems are excluded`, `$n{=}46$`, `$n{=}49$`\n- **替换**: n=500 的 DeepSeek/Qwen 有效 n\n\n### AM04 [data_update] Lines 39-40 — Table (cross-model) 全部数据\n- **当前**: DeepSeek [0.39, 1.48, 7.16, 14.59], Qwen [0.04, 0.23, 1.27, 2.94]\n- **替换**: n=500 median Δ 值（8 个数字）\n\n### AM05 [figure_update] Lines 45-50 — Figure 5 (fig5_crossmodel.pdf)\n- **操作**: 用 n=500 数据重新生成\n- **caption**: \"one-fifth\" 比例需同步更新\n\n### AM06 [data_update] Lines 52-53 — Per-problem concordance（重复 AR01）\n- **替换**: 与 AR01 同步\n\n### AM07 [data_update] Lines 55-56 — Random PASS/FAIL（重复 AR02/AR03）\n- **替换**: 与 AR02/AR03 同步\n\n### AM08 [data_update] Lines 62, 73 — Permutation test 样本量\n- **当前**: `$n{=}49$`\n- **替换**: n=500 有效 n\n\n### AM09 [data_update] Lines 68 — CI lower bounds\n- **当前**: `$0.19 \\to 0.69 \\to 1.66 \\to 6.70$`\n- **替换**: n=500 CI lower bounds\n\n### AM10 [data_update] Lines 79-82 — Table (permutation) 全部数据\n- **当前**: 4 行 (observed Δ̃, 95% CI, p_Bonf)\n- **替换**: n=500 permutation test 结果（12 个数字）\n\n### AM11 [figure_update] Lines 87-92 — Figure 4 (fig4_bootstrap.pdf)\n- **操作**: 用 n=500 数据重新生成\n\n### AM12 [data_update] Lines 111-122 — Table (discrimination-metrics-full) 全部数据\n- **当前**: 8 行 (ΔGini, ΔCV)\n- **替换**: 若 C4 分析基于 n=500 重跑则更新（16 个数字）\n\n### AM13 [data_update] Lines 137-139 — Entropy delta 描述\n- **当前**: DeepSeek `$\\Delta\\mathcal{H} \\in [-0.047, -0.040]$`, Qwen s025 `$+0.045$`\n- **替换**: 若 C4 分析基于 n=500 重跑则更新\n\n### AM14 [data_update] Lines 149-162 — Table (entropy-deltas) 全部数据\n- **当前**: 8 行\n- **替换**: 若 C4 分析基于 n=500 重跑则更新\n\n---\n\n## Appendix D (appendix_disc_analysis.tex) — Extended Discussion + Limitations\n\n### AD01 [data_update] Line 4 — Random Gini 范围\n- **当前**: `$-0.031$ to $-0.073$; Qwen: $-0.019$ to $-0.045$`\n- **替换**: 若 C4 基于 n=500 重跑则更新\n\n### AD02 [data_update] Line 11 — High-phase II 上限\n- **当前**: `$\\widetilde{\\mathrm{II}}_{\\text{high}} < 0.06$ at $s \\leq 0.30$`; `$s = 0.35$, high-phase II rises to $0.105$`\n- **替换**: n=500 high-phase median II 值\n\n### AD03 [data_update] Line 14 — Random 7/8 统计\n- **当前**: `7/8`, `$p{=}0.012$`, `$d_z{=}{-}0.04$`\n- **替换**: 与 A04 同步\n- **注意**: D059 — 不报 d_z\n\n### AD04 [data_update] Lines 44-47 — 统计范围详情\n- **当前**: `$n{=}49$ ... $n{=}46$`, mean/median ratio `${\\sim}1.6{:}1$`, permutation CI 值\n- **替换**: n=500 统计\n\n### AD05 [data_update] Line 49 — Qwen random s030 例外\n- **当前**: `$p{=}0.012$`, `$d_z{=}{-}0.04$`\n- **替换**: 与 AR03 同步\n- **注意**: D059 — 不报 d_z\n\n### AD06 [data_update] Lines 53-57 — Growth rate 描述\n- **当前**: `$3.8{\\times} \\to 4.8{\\times} \\to 2.0{\\times}$`\n- **替换**: n=500 Δ growth rate\n\n---\n\n## 图表重新生成清单\n\n| # | 文件名 | 数据来源 | 引用位置 |\n|---|--------|----------|----------|\n| F1 | fig1_dose_response.pdf | n=500 DeepSeek imp+rand G vs s | results.tex:57, caption:58 |\n| F2 | fig3_crossover.pdf | n=500 DeepSeek s=0.25 crossover | appendix_moved.tex:15 |\n| F3 | fig4_bootstrap.pdf | n=500 permutation test forest plot | appendix_moved.tex:89 |\n| F4 | fig5_crossmodel.pdf | n=500 DeepSeek+Qwen Δ comparison | appendix_moved.tex:47 |\n| F5 | (unnamed hero figure if separate) | 确认是否与 fig1 相同 | results.tex:57 |\n\n---\n\n## 硬约束合规审查\n\n### HC01 [D054] II 只报 median + median bootstrap CI ✅\n- abstract/results/discussion 全文使用 median ($\\widetilde{\\mathrm{II}}$)\n- methodology.tex:18 提及 mean/median ratio 作为选择 median 的理由 ✓\n- **注意**: n=500 更新时确认所有新数字均为 median\n\n### HC02 [D059] d_z 只报 within-importance ⚠️ 6 处违规\n| 位置 | 当前内容 | 问题 |\n|------|---------|------|\n| abstract.tex:8 | random `$d_z{=}{-}0.04$` | imp-vs-rand d_z |\n| results.tex:79 | LLaMA `$d_z$ ($0.19 \\to 0.34$)` | imp-vs-rand d_z |\n| results.tex:79 | random `$d_z \\in [0.35, 0.45]$` | random d_z |\n| results.tex:88-97 | Table 3 d_z 列 | imp-vs-rand d_z |\n| discussion.tex:11 | `$d_z \\in [0.35, 0.45]$` | random d_z |\n| appendix_disc_analysis.tex:14,49 | `$d_z{=}{-}0.04$` | random d_z |\n\n**修改方案**: 所有 imp-vs-rand 和 random d_z 替换为 Wilcoxon p + median_diff；Table 3 d_z 列替换为 within-importance d_z 或移除\n\n### HC03 [D015] Framing: emergent phase-strategy interaction ✅\n- abstract.tex:4 使用 \"emergent phase-strategy interaction\" ✓\n- 全文无 \"importance is broken\" 叙事 ✓\n\n### HC04 [D056] C5b 已降为 §8 future work ✅\n- discussion.tex:8 讨论 phase-aware budget 作为 implication（未 claim 实现）✓\n- conclusion.tex:5 \"motivate phase-aware sparsity allocation\" ✓\n- **注意**: D056 确认 c5b_pilot gate_failed (oracle 18% < 30%)，论文不应 claim C5b 成功\n\n### HC05 [D060] C8 LLaMA 用 suggests/partial support ✅\n- abstract.tex:10 \"suggests cross-architecture generalization\" ✓\n- discussion.tex:11 \"provides partial support\" ✓\n- conclusion.tex:4 \"partially extends\" ✓\n- results.tex:77-81 \"The qualitative pattern replicates\" — **borderline**，建议改为 \"The qualitative pattern is directionally consistent\"\n\n### HC06 [硬约束 #6] Random 也有正 II，区分信号是 gradient ✅\n- results.tex Table 2 显示 random 有正 II ✓\n- 叙事正确区分：\"compound severity depends qualitatively on eviction strategy\" ✓\n- **注意**: n=500 random 数据可能有不同 pattern，需重新验证此叙事\n\n---\n\n## 按 Section 分布\n\n| Section | 更新点数 |\n|---------|---------|\n| Abstract | 8 |\n| Introduction | 4 |\n| Methodology | 3 |\n| Results | 26 |\n| Analysis | 3 |\n| Discussion | 6 |\n| Conclusion | 6 |\n| Limitations | 2 |\n| Appendix (formulation) | 1 |\n| Appendix (results summary) | 3 |\n| Appendix (moved content) | 14 |\n| Appendix (disc+limitations) | 6 |\n| **Total** | **82** (含重复引用) |\n| **Unique** | **~70** |\n\n---\n\n## 高风险点（可能需要改叙事）\n\n### RISK-1: Qwen s015 是否仍然 non-significant\n- D052 预注册：若 n=500 Qwen s015 仍 ns，叙事改为 \"compound effect emerges above a model-dependent threshold\"\n- D061 已确认 n=500 下 Qwen s015 显著 (p<0.0001)——**如果最终数据确认，此风险解除**\n- 影响范围：abstract, introduction, results §5.4, §5.6, conclusion\n\n### RISK-2: Random PASS/FAIL 模式可能变化\n- n=50 下 7/8 FAIL（Qwen s030 borderline PASS d≈0）\n- n=500 功效更高，可能检测到更多 borderline 显著\n- 影响范围：需重新评估 \"no significant phase modulation\" 叙事\n- D059 保护：不报 random d_z，用 Wilcoxon p + median_diff 更 robust\n\n### RISK-3: LLaMA 数据是否跑 n=500\n- 当前 LLaMA 仅 n=49\n- 若不重跑：DeepSeek/Qwen 倍数比需重算（分母变了）\n- 若重跑：全部 LLaMA 数据需更新\n\n### RISK-4: D059 Table 3 重构\n- Table 3 (llama-cross-arch) 的核心组织方式围绕 imp-vs-rand d_z\n- 删除 d_z 列后需要替代结构，可能影响 §5.5 整段叙事\n\n### RISK-5: Crossover pattern 在 n=500 是否稳定\n- crossover 是论文的一个 key finding\n- n=500 的 crossover 倍数和位置可能变化\n- 影响范围：abstract, results §5.3, discussion, appendix\n\n### RISK-6: C4 entropy 分析是否需要基于 n=500 重跑\n- 当前 C4 降级为 supporting analysis (D045/D046)\n- 若不重跑：analysis.tex 和 appendix 表格保留 n=50 数据，需标注\n- 若重跑：AN01-AN03, AM12-AM14, AD01 全部更新\n",
      "numLines": 523,
      "startLine": 1,
      "totalLines": 523
    }
  }
}
````

</details>

---

### Assistant

_source line 64_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive view of all the files. Let me also check for figure generation info files to understand the data dependencies.

Let me read a few of the figure info files to understand the generation scripts.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10233ec7-5d03-448a-9224-b6173ea0cbe8",
  "uuid": "4e479aa9-cec3-4a18-a3ec-b2c05bb86de6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QP4KvqT4f5cVRpEHj2Q7vV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15654,
      "cache_read_input_tokens": 46658,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15654
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

_source line 65_

Let me check the figure generation info files for data dependencies.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10233ec7-5d03-448a-9224-b6173ea0cbe8",
  "uuid": "d309d452-8c94-4d42-97e3-c58d62f0a138",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QP4KvqT4f5cVRpEHj2Q7vV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15654,
      "cache_read_input_tokens": 46658,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15654
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

_source line 66_

<details open><summary>🔧 Tool call — Read · `toolu_01STVBZi3Nhvc4coPxFWgLM8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/chart/fig1_dose_response_bf16.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10233ec7-5d03-448a-9224-b6173ea0cbe8",
  "uuid": "d8d8f1f1-a1e8-415a-87ca-7bac695f50db",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QP4KvqT4f5cVRpEHj2Q7vV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15654,
      "cache_read_input_tokens": 46658,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15654
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

_source line 67 · 2026-05-14T21:51:07.819Z_

<details><summary>↩ Tool result · `toolu_01STVBZi3Nhvc4coPxFWgLM8`</summary>

```text
1	Generated from bf16 canonical data. G values: imp=[5.6, 69.2, 103.1, 222.4, 274.2, 273.6], rand=[1.1, 0.95, 1.67, 1.61]. Bootstrap B=10000 CI in log space.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10233ec7-5d03-448a-9224-b6173ea0cbe8",
  "uuid": "594cb132-8758-491c-804e-d861a69c07cf",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/chart/fig1_dose_response_bf16.txt",
      "content": "Generated from bf16 canonical data. G values: imp=[5.6, 69.2, 103.1, 222.4, 274.2, 273.6], rand=[1.1, 0.95, 1.67, 1.61]. Bootstrap B=10000 CI in log space.",
      "numLines": 1,
      "startLine": 1,
      "totalLines": 1
    }
  }
}
```

</details>

---

### Tool call

_source line 68_

<details open><summary>🔧 Tool call — Read · `toolu_01UBwxsuXiZfZ8S62UqECMsQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/chart/fig3_crossover_bf16.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10233ec7-5d03-448a-9224-b6173ea0cbe8",
  "uuid": "f0bf3045-bfa1-4072-80e5-0faeb16de80d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QP4KvqT4f5cVRpEHj2Q7vV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15654,
      "cache_read_input_tokens": 46658,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15654
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

_source line 69 · 2026-05-14T21:51:08.813Z_

<details><summary>↩ Tool result · `toolu_01UBwxsuXiZfZ8S62UqECMsQ`</summary>

```text
1	imp_high=0.032, rand_high=0.818; imp_mid=1.118, rand_mid=0.932; imp_low=7.196, rand_low=1.363. Crossover: importance < random in high phase, 5.3x higher in low phase.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10233ec7-5d03-448a-9224-b6173ea0cbe8",
  "uuid": "3fa990c2-90d8-414c-8b9c-a20443ecdc77",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/chart/fig3_crossover_bf16.txt",
      "content": "imp_high=0.032, rand_high=0.818; imp_mid=1.118, rand_mid=0.932; imp_low=7.196, rand_low=1.363. Crossover: importance < random in high phase, 5.3x higher in low phase.",
      "numLines": 1,
      "startLine": 1,
      "totalLines": 1
    }
  }
}
```

</details>

---

### Tool call

_source line 70_

<details open><summary>🔧 Tool call — Read · `toolu_01WgCjrPzch1AnymAzMw1aMy`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/chart/fig4_forest_paired_dz.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10233ec7-5d03-448a-9224-b6173ea0cbe8",
  "uuid": "817c7da9-05e1-4441-9a88-aae07e700320",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QP4KvqT4f5cVRpEHj2Q7vV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15654,
      "cache_read_input_tokens": 46658,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15654
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

_source line 71 · 2026-05-14T21:51:09.862Z_

<details><summary>↩ Tool result · `toolu_01WgCjrPzch1AnymAzMw1aMy`</summary>

```text
1	DS d_z: 0.44/0.52/0.68/0.80. QW d_z: 0.28/0.55/0.89/1.02. All verified vs cohens_d_bf16.json. Paired sign-flip permutation test, all p<0.05 except QW s015 (p=0.0145).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10233ec7-5d03-448a-9224-b6173ea0cbe8",
  "uuid": "94b61523-b8a9-489e-ab91-420b47e90e52",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/chart/fig4_forest_paired_dz.txt",
      "content": "DS d_z: 0.44/0.52/0.68/0.80. QW d_z: 0.28/0.55/0.89/1.02. All verified vs cohens_d_bf16.json. Paired sign-flip permutation test, all p<0.05 except QW s015 (p=0.0145).",
      "numLines": 1,
      "startLine": 1,
      "totalLines": 1
    }
  }
}
```

</details>

---

### Tool call

_source line 72_

<details open><summary>🔧 Tool call — Read · `toolu_01BLE2d2Hf3PS9XNBGV5XSWB`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/chart/fig5_crossmodel_bf16.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10233ec7-5d03-448a-9224-b6173ea0cbe8",
  "uuid": "5d2158f4-2970-4cf2-8d90-a630c3eabc90",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QP4KvqT4f5cVRpEHj2Q7vV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 15654,
      "cache_read_input_tokens": 46658,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 15654
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

_source line 73 · 2026-05-14T21:51:10.120Z_

<details><summary>↩ Tool result · `toolu_01BLE2d2Hf3PS9XNBGV5XSWB`</summary>

```text
1	Paired median diffs: DS=[0.351, 1.136, 4.017, 9.954], QW=[0.062, 0.286, 1.155, 2.594]. Spearman rho=1.0, gradient permutation p=0.043 (permute sparsity ordering). d_z annotated per point.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10233ec7-5d03-448a-9224-b6173ea0cbe8",
  "uuid": "5ebd406d-1c1f-4ee8-a01e-b0ee0f27f79e",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/chart/fig5_crossmodel_bf16.txt",
      "content": "Paired median diffs: DS=[0.351, 1.136, 4.017, 9.954], QW=[0.062, 0.286, 1.155, 2.594]. Spearman rho=1.0, gradient permutation p=0.043 (permute sparsity ordering). d_z annotated per point.",
      "numLines": 1,
      "startLine": 1,
      "totalLines": 1
    }
  }
}
```

</details>

---

### Assistant

_source line 74_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information needed to create the comprehensive patch plan. Let me also check if there's a paper_framing.md or any constraint documentation.

Let me now write the comprehensive patch plan. I have thorough knowledge of all the .tex files and their exact line numbers. Let me compile everything.

Let me organize the patch plan document now. I need:

## A. Update Location List

### A1. Tables
All tables with n=50 data:
1. results.tex:10-23 — Table 1 (tab:aggregate-ii) — DeepSeek aggregate data, caption "n=50"


2. results.tex:31-53 — Table 2 (tab:main-results) — Per-phase breakdown, caption "50 problems"  
3. results.tex:83-98 — Table 3 (tab:llama-cross-arch) — LLaMA cross-arch, D059 violation in d_z column
4. results.tex:108-124 — Table 4 (tab:cohens-d) — Cohen's d_z for DS/QW
5. appendix_moved.tex:30-43 — Table (tab:cross-model) — Cross-model comparison
6. appendix_moved.tex continues with more table locations...

I'm cataloging the remaining tables in the appendix — permutation test results, discrimination metrics with Gini and CV deltas if the C4 reruns come through, and entropy delta breakdowns. Then I need to work through the quantitative claims line-by-line, identify where D059 violations occur with d_z in the imp-vs-rand comparisons, check the LLaMA language validation for C8, figure out where the new future work text should go for C5b, and finally document each figure with its generation details.

Now I'm moving into the pre-written text sections — the Qwen caveat, the C5b future work paragraph, and the mid-phase null rate — before assembling the complete document.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10233ec7-5d03-448a-9224-b6173ea0cbe8",
  "uuid": "a8d50bab-133c-4689-a8de-edcd756f90ec",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U4VakCQgtny3ieUG7x91jt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 844,
      "cache_read_input_tokens": 62312,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 844
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

_source line 75_

I now have complete information from all 15 .tex files. Let me compile the precise patch plan.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10233ec7-5d03-448a-9224-b6173ea0cbe8",
  "uuid": "937cdf13-9443-494e-ace7-ad25e11faa5f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U4VakCQgtny3ieUG7x91jt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 844,
      "cache_read_input_tokens": 62312,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 844
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

_source line 76_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01VtcYHw9HDmqMLWWxtXo4RE`</summary>

```json
{
  "query": "select:TodoWrite",
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
  "session_id": "10233ec7-5d03-448a-9224-b6173ea0cbe8",
  "uuid": "42d76199-ff0a-45d6-a13f-6f228eed7668",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U4VakCQgtny3ieUG7x91jt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 844,
      "cache_read_input_tokens": 62312,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 844
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

_source line 77 · 2026-05-14T21:51:26.616Z_

<details><summary>↩ Tool result · `toolu_01VtcYHw9HDmqMLWWxtXo4RE`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "TodoWrite"
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
  "session_id": "10233ec7-5d03-448a-9224-b6173ea0cbe8",
  "uuid": "2a4c320d-c30c-42c3-ba25-12c42d8aaa02",
  "tool_use_result": {
    "matches": [
      "TodoWrite"
    ],
    "query": "select:TodoWrite",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Assistant

_source line 78_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information I need. Let me write the comprehensive patch plan document. I'll organize it precisely with file:line references.

Let me compile everything into the output document.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10233ec7-5d03-448a-9224-b6173ea0cbe8",
  "uuid": "c9391005-4b8a-4425-8401-aff5ad2891d2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JTmHGFSQv4wCFCTHbAN6DT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3034,
      "cache_read_input_tokens": 63156,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3034
      },
      "output_tokens": 21,
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

_source line 79_

Now writing the complete patch plan document.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10233ec7-5d03-448a-9224-b6173ea0cbe8",
  "uuid": "3600ea53-e7e6-4d3d-9fb8-0ac73b71e8e9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JTmHGFSQv4wCFCTHbAN6DT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3034,
      "cache_read_input_tokens": 63156,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3034
      },
      "output_tokens": 21,
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

_source line 80_

<details open><summary>🔧 Tool call — Write · `toolu_01J7zAC8NYFZUnBswiKeTuby`</summary>

````json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/n500_paper_patch_plan.md",
  "content": "# n=500 Paper Patch Plan\n\n> 精确位置清单 + 预写文本\n> 基于论文目录：`artifacts/_project/paper/`\n> 生成日期：2026-05-14\n> 硬约束：D054 (median only), D059 (within-imp d_z only), D060 (C8=partially_confirmed)\n\n---\n\n## A. 更新位置清单\n\n### A1. Tables（含 n=50 数据的表格）\n\n| # | 文件:行号 | 表格 ID | 内容 | 操作 |\n|---|----------|---------|------|------|\n| T1 | results.tex:10-23 | tab:aggregate-ii | DeepSeek aggregate Δ by strategy (caption L13: \"n=50\") | 替换 8 个数据单元格 + caption n 值 |\n| T2 | results.tex:31-53 | tab:main-results | Per-phase II breakdown (caption L34: \"50 problems\") | 替换 24 个数据单元格 + caption n 值 |\n| T3 | results.tex:83-98 | tab:llama-cross-arch | LLaMA cross-arch (caption L86: \"n=49\") | **D059 重构**：d_z 列为 imp-vs-rand → 替换为 within-imp d_z 或改为 Wilcoxon p + median_diff；若 LLaMA 不重跑则数值不变但列定义必须改 |\n| T4 | results.tex:108-124 | tab:cohens-d | DS/QW paired d_z (within-imp, 合规) | 替换 16 个数据单元格（4行 × 4列） |\n| T5 | appendix_moved.tex:30-43 | tab:cross-model | Cross-model Δ comparison | 替换 8 个数据单元格 |\n| T6 | appendix_moved.tex:70-85 | tab:permutation | Permutation test results (caption L73: \"n=49\") | 替换 12 个数据单元格 + caption n 值 |\n| T7 | appendix_moved.tex:103-123 | tab:discrimination-metrics-full | Gini/CV deltas | 替换 16 个数据单元格（若 C4 基于 n=500 重跑） |\n| T8 | appendix_moved.tex:143-163 | tab:entropy-deltas | Entropy Δ𝓗 | 替换 8 个数据单元格（若 C4 基于 n=500 重跑） |\n\n---\n\n### A2. Quantitative Claims（文中引用具体数字的句子）\n\n#### abstract.tex\n| # | 行号 | 当前文本片段 | 替换说明 |\n|---|------|-------------|---------|\n| Q1 | 6 | `50 MATH-500 problems` | → `500 MATH-500 problems` |\n| Q2 | 6 | `$s \\in \\{0.15, 0.20, 0.25, 0.30\\}$` | 保留（sparsity levels 不变） |\n| Q3 | 7 | `from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$` | → n=500 DeepSeek importance Δ (4值) |\n| Q4 | 7 | `$d_z$ growing from $0.44$ (small) to $0.80$ (large)` | → n=500 within-imp d_z (合规 ✓) |\n| Q5 | 7 | `$p < 0.005$ at all four sparsity levels` | → n=500 permutation p |\n| Q6 | 8 | `7/8 conditions` | → n=500 random PASS/FAIL 计数 |\n| Q7 | 8 | `$p{=}0.012$` `$d_z{=}{-}0.04$` | → **D059**: 删 d_z，改为 Wilcoxon p + median_diff |\n| Q8 | 9 | `$\\widetilde{\\mathrm{II}} = 0.032$ vs.\\ $0.818$` + `$7.196$ vs.\\ $1.363$` | → n=500 crossover II 中位数 |\n| Q9 | 10 | `$d_z \\geq 0.55$; Spearman $\\rho = 1.0$; gradient permutation $p = 0.043$` | → n=500 Qwen within-imp 统计 |\n| Q10 | 10 | `$d_z$ ($0.19 \\to 0.34$; $s{=}0.30$ Wilcoxon $p_{\\text{Bonf}} = 0.029$)` | → **D059**: 删 imp-vs-rand d_z，保留 Wilcoxon p + median_diff |\n| Q11 | 10 | `${\\sim}$1/40 the absolute magnitude` | → 用 n=500 DeepSeek 重算 LLaMA/DeepSeek 比值 |\n\n#### introduction.tex\n| # | 行号 | 当前文本片段 | 替换说明 |\n|---|------|-------------|---------|\n| Q12 | 14 | `$0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$ ($d_z$: $0.44 \\to 0.80$; Bonferroni-corrected $p < 0.005$)` | → 与 Q3/Q4/Q5 同步 |\n| Q13 | 15 | `$d_z \\geq 0.55$` | → n=500 Qwen within-imp d_z 下界 |\n| Q14 | 15 | `$\\sim$1/40 the magnitude` | → 与 Q11 同步 |\n| Q15 | 16 | `7/8 conditions non-significant` | → 与 Q6 同步 |\n\n#### methodology.tex\n| # | 行号 | 当前文本片段 | 替换说明 |\n|---|------|-------------|---------|\n| Q16 | 10 | `50 problems stratified from MATH-500` | → `500 problems from MATH-500`（去 \"stratified\"，500≈全集） |\n| Q17 | 18 | `mean/median ratios up to 43:1` | → n=500 mean/median ratio |\n| Q18 | 22 | `All tests yield $p_{\\text{Bonf}} < 0.005$ at every sparsity level.` | → n=500 p 值 |\n\n#### results.tex（非表格部分）\n| # | 行号 | 当前文本片段 | 替换说明 |\n|---|------|-------------|---------|\n| Q19 | 8 | `$0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$---a $37{\\times}$ amplification` | → n=500 Δ + 倍数 |\n| Q20 | 8 | `$-0.02$ to $1.54$` | → n=500 random Δ 范围 |\n| Q21 | 29 | `$69{\\times}$ at $s{=}0.15$ to $274{\\times}$ at $s{=}0.30$` | → n=500 G 值 |\n| Q22 | 29 | `$\\widetilde{\\mathrm{II}}_{\\textit{high}}$ ranges from $0.006$ to $0.053$` | → n=500 high-phase II 范围 |\n| Q23 | 29 | `$G \\approx 0.9$--$1.7{\\times}$` | → n=500 random G 范围 |\n| Q24 | 58 | caption: `$69{\\times}$ to $274{\\times}$` | → 与 Q21 同步 |\n| Q25 | 66 | `$0.032$ vs.\\ $0.818$` + `$7.196$ vs.\\ $1.363$---a $5.3{\\times}$ reversal` | → 与 Q8 同步 |\n| Q26 | 71 | `$\\Delta$ increases from $0.04$ at $s{=}0.15$ to $2.94$ at $s{=}0.30$` | → n=500 Qwen Δ |\n| Q27 | 71 | `${\\sim}1/5$ the magnitude` | → n=500 Qwen/DeepSeek 比值 |\n| Q28 | 71 | `Spearman $\\rho = 1.0$; gradient permutation $p = 0.043$` | → n=500 Qwen 统计 |\n| Q29 | 71 | `$d_z{=}0.28$, CI includes zero` | → n=500 Qwen s015 d_z + CI（within-imp, 合规） |\n| Q30 | 71 | `$d_z \\geq 0.55$` | → n=500 Qwen d_z 下界 |\n| Q31 | 77 | `$n{=}49$ paired problems` | → 确认 LLaMA 是否重跑；若不重跑保留 |\n| Q32 | 79 | `$d_z$ ($0.19 \\to 0.26 \\to 0.29 \\to 0.34$)` | → **D059 违规**：删除 imp-vs-rand d_z，改为 Wilcoxon p + median_diff |\n| Q33 | 79 | `$p = 0.029$, $k{=}4$` | → 保留（Wilcoxon p 合规） |\n| Q34 | 79 | `$\\widetilde{\\Delta} = 0.020$` + CI `$[0.002, 0.043]$` | → 保留/更新 |\n| Q35 | 79 | `$d_z \\in [1.00, 1.12]$` | → within-imp d_z，合规 ✓；若 LLaMA 重跑则更新 |\n| Q36 | 79 | `$d_z \\in [0.35, 0.45]$` | → **D059**: random d_z，删除改为定性描述 |\n| Q37 | 81 | `${\\sim}40{\\times}$ smaller than DeepSeek and ${\\sim}7{\\times}$ smaller than Qwen` | → 用 n=500 DS/QW 重算 |\n| Q38 | 104 | `$p_{\\text{Bonf}} < 0.005$` + `$0.37$ at $s{=}0.15$ to $9.85$ at $s{=}0.30$` | → n=500 permutation 统计 |\n| Q39 | 106 | `$d_z{=}0.44$ (small) to $d_z{=}0.80$ (large)` | → n=500 DS within-imp d_z |\n| Q40 | 106 | `$d_z{=}0.28$, CI includes zero` + `$d_z \\geq 0.55$` + `$d_z{=}0.89$/$1.02$ vs.\\ $0.68$/$0.80$` | → n=500 QW d_z 全更新 |\n\n#### discussion.tex\n| # | 行号 | 当前文本片段 | 替换说明 |\n|---|------|-------------|---------|\n| Q41 | 5 | `$69$--$274{\\times}$` | → 与 Q21 同步 |\n| Q42 | 5 | `$\\widetilde{\\mathrm{II}} = 0.032$ vs.\\ $0.818$` + `$7.196$ vs.\\ $1.363$` | → 与 Q8 同步 |\n| Q43 | 5 | `$G \\approx 1$` | → 保留（定性描述） |\n| Q44 | 11 | `${\\sim}40{\\times}$ smaller than DeepSeek, ${\\sim}7{\\times}$ smaller than Qwen` | → 与 Q37 同步 |\n| Q45 | 11 | `$d_z \\geq 1.0$` | → within-imp，合规 ✓；若 LLaMA 重跑则更新 |\n| Q46 | 11 | `$d_z \\in [0.35, 0.45]$` | → **D059**: random d_z，删除改为定性描述 + Wilcoxon p |\n\n#### conclusion.tex\n| # | 行号 | 当前文本片段 | 替换说明 |\n|---|------|-------------|---------|\n| Q47 | 4 | `$69{\\times}$ to $274{\\times}$` | → 与 Q21 同步 |\n| Q48 | 4 | `$d_z$: $0.44 \\to 0.80$` | → within-imp，与 Q39 同步 |\n| Q49 | 4 | `7/8 conditions non-significant` | → 与 Q6 同步 |\n| Q50 | 4 | `$d_z \\geq 0.55$` | → 与 Q30 同步 |\n| Q51 | 4 | `$\\sim$1/40 the magnitude` | → 与 Q11 同步 |\n\n#### analysis.tex\n| # | 行号 | 当前文本片段 | 替换说明 |\n|---|------|-------------|---------|\n| Q52 | 4 | `$0.030$--$0.081$ (DeepSeek) and $0.010$--$0.020$ (Qwen)` | → 若 C4 基于 n=500 重跑则更新 |\n| Q53 | 6 | `$\\Delta\\mathcal{H} \\in [-0.047, -0.040]$` | → 若 C4 重跑则更新 |\n| Q54 | 6 | `$\\Delta\\mathcal{H} = +0.045$` | → 若 C4 重跑则更新 |\n\n#### appendix.tex\n| # | 行号 | 当前文本片段 | 替换说明 |\n|---|------|-------------|---------|\n| Q55 | 38 | `$G_{\\times} = 58$--$241{\\times}$` | → n=500 multiplicative null G 值 |\n\n#### appendix_results.tex\n| # | 行号 | 当前文本片段 | 替换说明 |\n|---|------|-------------|---------|\n| Q56 | 7 | `mean $\\rho = -0.11$, $p = 0.926$` | → n=500 cross-model concordance |\n| Q57 | 10 | `3/4 FAIL` + `4/4 FAIL` | → n=500 random PASS/FAIL |\n| Q58 | 10 | `$p = 0.012$` + `$d_z = -0.04$` | → **D059**: 删 d_z，改为 Wilcoxon p + median_diff |\n\n#### appendix_moved.tex（非表格部分）\n| # | 行号 | 当前文本片段 | 替换说明 |\n|---|------|-------------|---------|\n| Q59 | 11 | `$0.032$ vs.\\ $0.818$` + `$7.196$ vs.\\ $1.363$` + `$5.3{\\times}$` + `$3.9{\\times}$, $5.4{\\times}$, $5.3{\\times}$, $3.6{\\times}$` | → n=500 crossover 全部数值 |\n| Q60 | 16 | caption `$5.3{\\times}$` | → 与 Q59 同步 |\n| Q61 | 26 | `Four of the 50 problems are excluded` + `$n{=}46$` + `$n{=}49$` | → n=500 有效 n |\n| Q62 | 28 | `${\\sim}1/5$ of DeepSeek's magnitude` | → 与 Q27 同步 |\n| Q63 | 48 | caption: `one-fifth` | → 与 Q27 同步 |\n| Q64 | 53 | `mean $\\rho = -0.11$, $p = 0.926$`（重复 Q56） | → 与 Q56 同步 |\n| Q65 | 56 | `$p = 0.012$` + `$d_z = -0.04$`（重复 Q58） | → 与 Q58 同步 |\n| Q66 | 62+73 | `$n{=}49$` | → n=500 有效 n |\n| Q67 | 68 | `$0.19 \\to 0.69 \\to 1.66 \\to 6.70$` | → n=500 CI lower bounds |\n| Q68 | 101 | Gini: `$0.030$--$0.081$` + `$0.010$--$0.020$` | → 若 C4 重跑则更新 |\n| Q69 | 137-139 | DeepSeek `$[-0.047, -0.040]$` + Qwen `$+0.045$` + `$-0.007$` | → 若 C4 重跑则更新 |\n\n#### appendix_disc_analysis.tex\n| # | 行号 | 当前文本片段 | 替换说明 |\n|---|------|-------------|---------|\n| Q70 | 4 | `$-0.031$ to $-0.073$; Qwen: $-0.019$ to $-0.045$` | → 若 C4 重跑则更新 |\n| Q71 | 11 | `$\\widetilde{\\mathrm{II}}_{\\text{high}} < 0.06$` + `$0.105$` | → n=500 high-phase II |\n| Q72 | 14 | `7/8` + `$p{=}0.012$` + `$d_z{=}{-}0.04$` | → **D059**: 删 d_z，与 Q7 同步 |\n| Q73 | 45 | `$n{=}49$` + `$n{=}46$` | → n=500 有效 n |\n| Q74 | 46 | `${\\sim}1.6{:}1$` + `median_diff=14.59` | → n=500 偏度统计 |\n| Q75 | 47 | CI 值: `$[0.19,0.62]$, $[0.69,1.49]$, $[1.66,6.64]$, $[6.70,16.29]$` | → n=500 permutation CI |\n| Q76 | 49 | `$p{=}0.012$` + `$d_z{=}{-}0.04$` | → **D059**: 删 d_z，与 Q7 同步 |\n| Q77 | 57 | `$3.8{\\times} \\to 4.8{\\times} \\to 2.0{\\times}$` | → n=500 Δ growth rate |\n\n---\n\n### A3. D059 违规（imp-vs-rand 或 random 使用 d_z 的位置）\n\n共 **10 处**需修改，改为 Wilcoxon p + median_diff：\n\n| # | 文件:行号 | 当前内容 | 违规类型 |\n|---|----------|---------|---------|\n| D1 | abstract.tex:8 | `$d_z{=}{-}0.04$` | random d_z |\n| D2 | abstract.tex:10 | `$d_z$ ($0.19 \\to 0.34$` | imp-vs-rand d_z (LLaMA) |\n| D3 | results.tex:79 | `paired $d_z$ ($0.19 \\to 0.26 \\to 0.29 \\to 0.34$)` | imp-vs-rand d_z (LLaMA) |\n| D4 | results.tex:79 | `$d_z \\in [0.35, 0.45]$` | random d_z (LLaMA) |\n| D5 | results.tex:86-97 | Table 3 d_z 列 + caption `$d_z$: paired Cohen's $d$ for importance vs.\\ random` | imp-vs-rand d_z (整列) |\n| D6 | discussion.tex:11 | `$d_z \\in [0.35, 0.45]$` | random d_z (LLaMA) |\n| D7 | appendix_results.tex:10 | `$d_z = -0.04$` | random d_z |\n| D8 | appendix_moved.tex:56 | `$d_z = -0.04$` | random d_z |\n| D9 | appendix_disc_analysis.tex:14 | `$d_z{=}{-}0.04$` | random d_z |\n| D10 | appendix_disc_analysis.tex:49 | `$d_z{=}{-}0.04$` | random d_z |\n\n**修改方案**：\n- D1/D7/D8/D9/D10：删除 `$d_z{=}{-}0.04$`，替换为 `negligible median difference ($\\widetilde{\\Delta} = \\text{X}$)`\n- D2/D3：删除 imp-vs-rand d_z 序列，改为 `Wilcoxon signed-rank tests with median paired difference $\\widetilde{\\Delta}$ increasing from X to Y`\n- D4/D6：删除 random d_z，改为定性描述 `random eviction also shows a non-trivial phase gradient (Wilcoxon $p < \\text{X}$)`\n- D5：Table 3 重构——d_z 列替换为 within-importance d_z（low−high），或移除 d_z 列完全改为 Wilcoxon p + median_diff 结构\n\n---\n\n### A4. C8 partially_confirmed 限定语（LLaMA 相关断言检查）\n\n| # | 文件:行号 | 当前文本 | 状态 |\n|---|----------|---------|------|\n| C1 | abstract.tex:10 | `suggests cross-architecture generalization, though at...` | ✅ 合规 |\n| C2 | introduction.tex:15 | `partially extends to a distinct architecture` | ✅ 合规 |\n| C3 | results.tex:79 | `The qualitative pattern replicates` | ⚠️ **borderline** — 建议改为 `The qualitative pattern is directionally consistent` |\n| C4 | results.tex:81 | `The directional pattern...is qualitatively consistent across all three models` | ✅ 合规（后半句有 `substantially weaker` 限定） |\n| C5 | discussion.tex:11 | `provides partial support for the qualitative pattern` | ✅ 合规 |\n| C6 | conclusion.tex:4 | `partially extends cross-architecture` | ✅ 合规 |\n| C7 | limitations.tex:2 | `partially extends the findings beyond the Qwen2 architecture` | ✅ 合规 |\n| C8 | appendix_disc_analysis.tex:33 | `provides partial support` | ✅ 合规 |\n\n**唯一需修改**：results.tex:79 `The qualitative pattern replicates` → `The qualitative pattern is directionally consistent`\n\n---\n\n### A5. C5b Future Work 位置\n\n当前论文**没有独立的 Future Work section**。相关 mitigation 讨论分散在：\n\n| # | 文件:行号 | 当前内容 | 说明 |\n|---|----------|---------|------|\n| FW1 | discussion.tex:8 | `A phase-aware compression budget...could mitigate...` | mitigation 作为 implication 讨论 |\n| FW2 | conclusion.tex:5 | `These findings motivate phase-aware sparsity allocation...` | 一句话 motivation |\n\n**建议插入点**：conclusion.tex:5 之后（line 5 与 `\\end{document}` 之间），新增 Future Work 段落。或者在 discussion.tex:8 段落末尾追加 pilot 实验结果。\n\n具体推荐：**discussion.tex:8 段落末尾**追加 B2 文本（与 deployment implications 自然衔接），同时在 conclusion.tex:5 追加一句指向 discussion 的引用。\n\n---\n\n### A6. Figures（数据源与重生成需求）\n\n| # | 文件名 | 引用位置 | 数据源（n=50） | n=500 操作 |\n|---|--------|---------|---------------|-----------|\n| F1 | fig1_dose_response.pdf | results.tex:57, caption:58 | G values: imp=[5.6, 69.2, 103.1, 222.4, 274.2, 273.6], rand=[1.1, 0.95, 1.67, 1.61]. Bootstrap B=10000 CI in log space. 生成信息: `_project/chart/fig1_dose_response_bf16.txt` | 用 n=500 experiment_summary_table.json 重算 G 值 → 重新生成。Caption Q24 需同步更新 |\n| F2 | fig3_crossover.pdf | appendix_moved.tex:15, caption:16 | imp_high=0.032, rand_high=0.818; imp_mid=1.118, rand_mid=0.932; imp_low=7.196, rand_low=1.363. 生成信息: `_project/chart/fig3_crossover_bf16.txt` | 用 n=500 s=0.25 per-phase median II → 重新生成。Caption Q60 需同步更新 |\n| F3 | fig4_bootstrap.pdf | appendix_moved.tex:89, caption:90 | DS d_z: 0.44/0.52/0.68/0.80. QW d_z: 0.28/0.55/0.89/1.02. 生成信息: `_project/chart/fig4_forest_paired_dz.txt` | 用 n=500 paired d_z + permutation CI → 重新生成 |\n| F4 | fig5_crossmodel.pdf | appendix_moved.tex:47, caption:48 | DS Δ=[0.351, 1.136, 4.017, 9.954], QW Δ=[0.062, 0.286, 1.155, 2.594]. 生成信息: `_project/chart/fig5_crossmodel_bf16.txt` | 用 n=500 DS/QW paired median diffs → 重新生成。Caption Q63 需同步更新 |\n\n**注意**：所有 figure 生成脚本为服务器端执行（draw-paper-figure skill），无本地 .py 脚本。生成参数记录在 `_project/chart/` 目录下的 info 文件中。\n\n---\n\n## B. 预写文本\n\n### B1. Qwen Caveat（imp-vs-rand 不显著时使用）\n\n> **插入位置**：results.tex:71 之后（§5.4 Cross-Model Replication 末尾，Table/Figure 引用之前）\n\n```latex\nWhile Qwen2.5-7B-Instruct exhibits a significant within-importance severity gradient at $s \\geq 0.20$, the importance-versus-random contrast is attenuated relative to DeepSeek: the median paired difference remains modest across sparsity levels, and the permutation test reaches significance only at $s \\geq 0.25$. This attenuation likely reflects Qwen's lower compound interaction baseline under importance-based eviction at low sparsity---when the absolute severity is small, the strategy-dependent amplification has less room to manifest, even though the within-strategy phase gradient is robust.\n```\n\n### B2. C5b Future Work（Phase-Aware Mitigation Pilot）\n\n> **插入位置**：discussion.tex:8 段落末尾（`Extended discussion in Appendix~\\ref{app:extended-discussion}.` 之前），或 conclusion.tex:5 之前新起段落\n\n```latex\nA preliminary pilot experiment explored oracle phase-aware budget reallocation, shifting sparsity budget from high-severity low-sparsity phases to low-severity high-sparsity phases. The oracle recovery---measured as the fraction of compound interaction eliminated by phase-aware allocation---reached only 18\\%, well below a pre-registered 30\\% gate for claiming practical mitigation. This suggests that phase-aware budget reallocation alone is insufficient to neutralize the severity gradient, and that effective mitigation may require joint optimization of both budget allocation and eviction strategy selection across phases---a promising but open direction for future work.\n```\n\n### B3. Mid-Phase Null Rate（Qwen Mid-Phase 统计功效限制）\n\n> **插入位置**：results.tex:71 附近（Qwen 结果讨论中），或 appendix_moved.tex:26 之后（Cross-Model Replication Details）\n\n```latex\nOn Qwen2.5-7B-Instruct, approximately 45\\% of problems yield near-zero Interaction Index in the mid-sparsity phase, where attention patterns exhibit insufficient variation to produce measurable compound interaction. This elevated null rate reduces the effective sample size for mid-phase comparisons and limits statistical power for detecting phase gradients that span the mid-phase boundary; our primary analysis therefore focuses on the low--high phase contrast, which is unaffected by this limitation.\n```\n\n---\n\n## C. 按优先级排序的执行清单\n\n### 优先级 1（n=500 数据到手后立即执行）\n1. 替换 T1, T2, T5, T6 表格数据（DeepSeek/Qwen 核心表格）\n2. 更新 Q1-Q5, Q12, Q15-Q18, Q19-Q30, Q38-Q40, Q47-Q50, Q55-Q67, Q71-Q77（数值替换）\n3. 重新生成 F1-F4 图表\n\n### 优先级 2（D059 合规修复，不依赖 n=500 数据）\n4. 修复 D1-D10 全部 D059 违规\n5. 重构 T3 (Table 3) 列定义\n\n### 优先级 3（文本修改）\n6. 修复 C3（results.tex:79 LLaMA 限定语）\n7. 插入 B1（Qwen caveat，视 n=500 结果决定是否使用）\n8. 插入 B2（C5b future work）\n9. 插入 B3（mid-phase null rate）\n\n### 优先级 4（条件性更新）\n10. T4 (tab:cohens-d) — n=500 数据\n11. T7, T8 — 仅当 C4 entropy 分析基于 n=500 重跑时更新\n12. Q37, Q44, Q51 — LLaMA 倍数比（依赖 n=500 DS/QW 数据）\n13. 确认 LLaMA 是否重跑 n=500（影响 T3 数据、Q31-Q36）\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10233ec7-5d03-448a-9224-b6173ea0cbe8",
  "uuid": "d358066c-74b9-426f-b6a3-80204a11205d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JTmHGFSQv4wCFCTHbAN6DT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3034,
      "cache_read_input_tokens": 63156,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3034
      },
      "output_tokens": 21,
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

_source line 81 · 2026-05-14T21:54:11.469Z_

<details><summary>↩ Tool result · `toolu_01J7zAC8NYFZUnBswiKeTuby`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/n500_paper_patch_plan.md
```

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "10233ec7-5d03-448a-9224-b6173ea0cbe8",
  "uuid": "6174a4cd-a41c-4be8-8939-752b52676c30",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/n500_paper_patch_plan.md",
    "content": "# n=500 Paper Patch Plan\n\n> 精确位置清单 + 预写文本\n> 基于论文目录：`artifacts/_project/paper/`\n> 生成日期：2026-05-14\n> 硬约束：D054 (median only), D059 (within-imp d_z only), D060 (C8=partially_confirmed)\n\n---\n\n## A. 更新位置清单\n\n### A1. Tables（含 n=50 数据的表格）\n\n| # | 文件:行号 | 表格 ID | 内容 | 操作 |\n|---|----------|---------|------|------|\n| T1 | results.tex:10-23 | tab:aggregate-ii | DeepSeek aggregate Δ by strategy (caption L13: \"n=50\") | 替换 8 个数据单元格 + caption n 值 |\n| T2 | results.tex:31-53 | tab:main-results | Per-phase II breakdown (caption L34: \"50 problems\") | 替换 24 个数据单元格 + caption n 值 |\n| T3 | results.tex:83-98 | tab:llama-cross-arch | LLaMA cross-arch (caption L86: \"n=49\") | **D059 重构**：d_z 列为 imp-vs-rand → 替换为 within-imp d_z 或改为 Wilcoxon p + median_diff；若 LLaMA 不重跑则数值不变但列定义必须改 |\n| T4 | results.tex:108-124 | tab:cohens-d | DS/QW paired d_z (within-imp, 合规) | 替换 16 个数据单元格（4行 × 4列） |\n| T5 | appendix_moved.tex:30-43 | tab:cross-model | Cross-model Δ comparison | 替换 8 个数据单元格 |\n| T6 | appendix_moved.tex:70-85 | tab:permutation | Permutation test results (caption L73: \"n=49\") | 替换 12 个数据单元格 + caption n 值 |\n| T7 | appendix_moved.tex:103-123 | tab:discrimination-metrics-full | Gini/CV deltas | 替换 16 个数据单元格（若 C4 基于 n=500 重跑） |\n| T8 | appendix_moved.tex:143-163 | tab:entropy-deltas | Entropy Δ𝓗 | 替换 8 个数据单元格（若 C4 基于 n=500 重跑） |\n\n---\n\n### A2. Quantitative Claims（文中引用具体数字的句子）\n\n#### abstract.tex\n| # | 行号 | 当前文本片段 | 替换说明 |\n|---|------|-------------|---------|\n| Q1 | 6 | `50 MATH-500 problems` | → `500 MATH-500 problems` |\n| Q2 | 6 | `$s \\in \\{0.15, 0.20, 0.25, 0.30\\}$` | 保留（sparsity levels 不变） |\n| Q3 | 7 | `from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$` | → n=500 DeepSeek importance Δ (4值) |\n| Q4 | 7 | `$d_z$ growing from $0.44$ (small) to $0.80$ (large)` | → n=500 within-imp d_z (合规 ✓) |\n| Q5 | 7 | `$p < 0.005$ at all four sparsity levels` | → n=500 permutation p |\n| Q6 | 8 | `7/8 conditions` | → n=500 random PASS/FAIL 计数 |\n| Q7 | 8 | `$p{=}0.012$` `$d_z{=}{-}0.04$` | → **D059**: 删 d_z，改为 Wilcoxon p + median_diff |\n| Q8 | 9 | `$\\widetilde{\\mathrm{II}} = 0.032$ vs.\\ $0.818$` + `$7.196$ vs.\\ $1.363$` | → n=500 crossover II 中位数 |\n| Q9 | 10 | `$d_z \\geq 0.55$; Spearman $\\rho = 1.0$; gradient permutation $p = 0.043$` | → n=500 Qwen within-imp 统计 |\n| Q10 | 10 | `$d_z$ ($0.19 \\to 0.34$; $s{=}0.30$ Wilcoxon $p_{\\text{Bonf}} = 0.029$)` | → **D059**: 删 imp-vs-rand d_z，保留 Wilcoxon p + median_diff |\n| Q11 | 10 | `${\\sim}$1/40 the absolute magnitude` | → 用 n=500 DeepSeek 重算 LLaMA/DeepSeek 比值 |\n\n#### introduction.tex\n| # | 行号 | 当前文本片段 | 替换说明 |\n|---|------|-------------|---------|\n| Q12 | 14 | `$0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$ ($d_z$: $0.44 \\to 0.80$; Bonferroni-corrected $p < 0.005$)` | → 与 Q3/Q4/Q5 同步 |\n| Q13 | 15 | `$d_z \\geq 0.55$` | → n=500 Qwen within-imp d_z 下界 |\n| Q14 | 15 | `$\\sim$1/40 the magnitude` | → 与 Q11 同步 |\n| Q15 | 16 | `7/8 conditions non-significant` | → 与 Q6 同步 |\n\n#### methodology.tex\n| # | 行号 | 当前文本片段 | 替换说明 |\n|---|------|-------------|---------|\n| Q16 | 10 | `50 problems stratified from MATH-500` | → `500 problems from MATH-500`（去 \"stratified\"，500≈全集） |\n| Q17 | 18 | `mean/median ratios up to 43:1` | → n=500 mean/median ratio |\n| Q18 | 22 | `All tests yield $p_{\\text{Bonf}} < 0.005$ at every sparsity level.` | → n=500 p 值 |\n\n#### results.tex（非表格部分）\n| # | 行号 | 当前文本片段 | 替换说明 |\n|---|------|-------------|---------|\n| Q19 | 8 | `$0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$---a $37{\\times}$ amplification` | → n=500 Δ + 倍数 |\n| Q20 | 8 | `$-0.02$ to $1.54$` | → n=500 random Δ 范围 |\n| Q21 | 29 | `$69{\\times}$ at $s{=}0.15$ to $274{\\times}$ at $s{=}0.30$` | → n=500 G 值 |\n| Q22 | 29 | `$\\widetilde{\\mathrm{II}}_{\\textit{high}}$ ranges from $0.006$ to $0.053$` | → n=500 high-phase II 范围 |\n| Q23 | 29 | `$G \\approx 0.9$--$1.7{\\times}$` | → n=500 random G 范围 |\n| Q24 | 58 | caption: `$69{\\times}$ to $274{\\times}$` | → 与 Q21 同步 |\n| Q25 | 66 | `$0.032$ vs.\\ $0.818$` + `$7.196$ vs.\\ $1.363$---a $5.3{\\times}$ reversal` | → 与 Q8 同步 |\n| Q26 | 71 | `$\\Delta$ increases from $0.04$ at $s{=}0.15$ to $2.94$ at $s{=}0.30$` | → n=500 Qwen Δ |\n| Q27 | 71 | `${\\sim}1/5$ the magnitude` | → n=500 Qwen/DeepSeek 比值 |\n| Q28 | 71 | `Spearman $\\rho = 1.0$; gradient permutation $p = 0.043$` | → n=500 Qwen 统计 |\n| Q29 | 71 | `$d_z{=}0.28$, CI includes zero` | → n=500 Qwen s015 d_z + CI（within-imp, 合规） |\n| Q30 | 71 | `$d_z \\geq 0.55$` | → n=500 Qwen d_z 下界 |\n| Q31 | 77 | `$n{=}49$ paired problems` | → 确认 LLaMA 是否重跑；若不重跑保留 |\n| Q32 | 79 | `$d_z$ ($0.19 \\to 0.26 \\to 0.29 \\to 0.34$)` | → **D059 违规**：删除 imp-vs-rand d_z，改为 Wilcoxon p + median_diff |\n| Q33 | 79 | `$p = 0.029$, $k{=}4$` | → 保留（Wilcoxon p 合规） |\n| Q34 | 79 | `$\\widetilde{\\Delta} = 0.020$` + CI `$[0.002, 0.043]$` | → 保留/更新 |\n| Q35 | 79 | `$d_z \\in [1.00, 1.12]$` | → within-imp d_z，合规 ✓；若 LLaMA 重跑则更新 |\n| Q36 | 79 | `$d_z \\in [0.35, 0.45]$` | → **D059**: random d_z，删除改为定性描述 |\n| Q37 | 81 | `${\\sim}40{\\times}$ smaller than DeepSeek and ${\\sim}7{\\times}$ smaller than Qwen` | → 用 n=500 DS/QW 重算 |\n| Q38 | 104 | `$p_{\\text{Bonf}} < 0.005$` + `$0.37$ at $s{=}0.15$ to $9.85$ at $s{=}0.30$` | → n=500 permutation 统计 |\n| Q39 | 106 | `$d_z{=}0.44$ (small) to $d_z{=}0.80$ (large)` | → n=500 DS within-imp d_z |\n| Q40 | 106 | `$d_z{=}0.28$, CI includes zero` + `$d_z \\geq 0.55$` + `$d_z{=}0.89$/$1.02$ vs.\\ $0.68$/$0.80$` | → n=500 QW d_z 全更新 |\n\n#### discussion.tex\n| # | 行号 | 当前文本片段 | 替换说明 |\n|---|------|-------------|---------|\n| Q41 | 5 | `$69$--$274{\\times}$` | → 与 Q21 同步 |\n| Q42 | 5 | `$\\widetilde{\\mathrm{II}} = 0.032$ vs.\\ $0.818$` + `$7.196$ vs.\\ $1.363$` | → 与 Q8 同步 |\n| Q43 | 5 | `$G \\approx 1$` | → 保留（定性描述） |\n| Q44 | 11 | `${\\sim}40{\\times}$ smaller than DeepSeek, ${\\sim}7{\\times}$ smaller than Qwen` | → 与 Q37 同步 |\n| Q45 | 11 | `$d_z \\geq 1.0$` | → within-imp，合规 ✓；若 LLaMA 重跑则更新 |\n| Q46 | 11 | `$d_z \\in [0.35, 0.45]$` | → **D059**: random d_z，删除改为定性描述 + Wilcoxon p |\n\n#### conclusion.tex\n| # | 行号 | 当前文本片段 | 替换说明 |\n|---|------|-------------|---------|\n| Q47 | 4 | `$69{\\times}$ to $274{\\times}$` | → 与 Q21 同步 |\n| Q48 | 4 | `$d_z$: $0.44 \\to 0.80$` | → within-imp，与 Q39 同步 |\n| Q49 | 4 | `7/8 conditions non-significant` | → 与 Q6 同步 |\n| Q50 | 4 | `$d_z \\geq 0.55$` | → 与 Q30 同步 |\n| Q51 | 4 | `$\\sim$1/40 the magnitude` | → 与 Q11 同步 |\n\n#### analysis.tex\n| # | 行号 | 当前文本片段 | 替换说明 |\n|---|------|-------------|---------|\n| Q52 | 4 | `$0.030$--$0.081$ (DeepSeek) and $0.010$--$0.020$ (Qwen)` | → 若 C4 基于 n=500 重跑则更新 |\n| Q53 | 6 | `$\\Delta\\mathcal{H} \\in [-0.047, -0.040]$` | → 若 C4 重跑则更新 |\n| Q54 | 6 | `$\\Delta\\mathcal{H} = +0.045$` | → 若 C4 重跑则更新 |\n\n#### appendix.tex\n| # | 行号 | 当前文本片段 | 替换说明 |\n|---|------|-------------|---------|\n| Q55 | 38 | `$G_{\\times} = 58$--$241{\\times}$` | → n=500 multiplicative null G 值 |\n\n#### appendix_results.tex\n| # | 行号 | 当前文本片段 | 替换说明 |\n|---|------|-------------|---------|\n| Q56 | 7 | `mean $\\rho = -0.11$, $p = 0.926$` | → n=500 cross-model concordance |\n| Q57 | 10 | `3/4 FAIL` + `4/4 FAIL` | → n=500 random PASS/FAIL |\n| Q58 | 10 | `$p = 0.012$` + `$d_z = -0.04$` | → **D059**: 删 d_z，改为 Wilcoxon p + median_diff |\n\n#### appendix_moved.tex（非表格部分）\n| # | 行号 | 当前文本片段 | 替换说明 |\n|---|------|-------------|---------|\n| Q59 | 11 | `$0.032$ vs.\\ $0.818$` + `$7.196$ vs.\\ $1.363$` + `$5.3{\\times}$` + `$3.9{\\times}$, $5.4{\\times}$, $5.3{\\times}$, $3.6{\\times}$` | → n=500 crossover 全部数值 |\n| Q60 | 16 | caption `$5.3{\\times}$` | → 与 Q59 同步 |\n| Q61 | 26 | `Four of the 50 problems are excluded` + `$n{=}46$` + `$n{=}49$` | → n=500 有效 n |\n| Q62 | 28 | `${\\sim}1/5$ of DeepSeek's magnitude` | → 与 Q27 同步 |\n| Q63 | 48 | caption: `one-fifth` | → 与 Q27 同步 |\n| Q64 | 53 | `mean $\\rho = -0.11$, $p = 0.926$`（重复 Q56） | → 与 Q56 同步 |\n| Q65 | 56 | `$p = 0.012$` + `$d_z = -0.04$`（重复 Q58） | → 与 Q58 同步 |\n| Q66 | 62+73 | `$n{=}49$` | → n=500 有效 n |\n| Q67 | 68 | `$0.19 \\to 0.69 \\to 1.66 \\to 6.70$` | → n=500 CI lower bounds |\n| Q68 | 101 | Gini: `$0.030$--$0.081$` + `$0.010$--$0.020$` | → 若 C4 重跑则更新 |\n| Q69 | 137-139 | DeepSeek `$[-0.047, -0.040]$` + Qwen `$+0.045$` + `$-0.007$` | → 若 C4 重跑则更新 |\n\n#### appendix_disc_analysis.tex\n| # | 行号 | 当前文本片段 | 替换说明 |\n|---|------|-------------|---------|\n| Q70 | 4 | `$-0.031$ to $-0.073$; Qwen: $-0.019$ to $-0.045$` | → 若 C4 重跑则更新 |\n| Q71 | 11 | `$\\widetilde{\\mathrm{II}}_{\\text{high}} < 0.06$` + `$0.105$` | → n=500 high-phase II |\n| Q72 | 14 | `7/8` + `$p{=}0.012$` + `$d_z{=}{-}0.04$` | → **D059**: 删 d_z，与 Q7 同步 |\n| Q73 | 45 | `$n{=}49$` + `$n{=}46$` | → n=500 有效 n |\n| Q74 | 46 | `${\\sim}1.6{:}1$` + `median_diff=14.59` | → n=500 偏度统计 |\n| Q75 | 47 | CI 值: `$[0.19,0.62]$, $[0.69,1.49]$, $[1.66,6.64]$, $[6.70,16.29]$` | → n=500 permutation CI |\n| Q76 | 49 | `$p{=}0.012$` + `$d_z{=}{-}0.04$` | → **D059**: 删 d_z，与 Q7 同步 |\n| Q77 | 57 | `$3.8{\\times} \\to 4.8{\\times} \\to 2.0{\\times}$` | → n=500 Δ growth rate |\n\n---\n\n### A3. D059 违规（imp-vs-rand 或 random 使用 d_z 的位置）\n\n共 **10 处**需修改，改为 Wilcoxon p + median_diff：\n\n| # | 文件:行号 | 当前内容 | 违规类型 |\n|---|----------|---------|---------|\n| D1 | abstract.tex:8 | `$d_z{=}{-}0.04$` | random d_z |\n| D2 | abstract.tex:10 | `$d_z$ ($0.19 \\to 0.34$` | imp-vs-rand d_z (LLaMA) |\n| D3 | results.tex:79 | `paired $d_z$ ($0.19 \\to 0.26 \\to 0.29 \\to 0.34$)` | imp-vs-rand d_z (LLaMA) |\n| D4 | results.tex:79 | `$d_z \\in [0.35, 0.45]$` | random d_z (LLaMA) |\n| D5 | results.tex:86-97 | Table 3 d_z 列 + caption `$d_z$: paired Cohen's $d$ for importance vs.\\ random` | imp-vs-rand d_z (整列) |\n| D6 | discussion.tex:11 | `$d_z \\in [0.35, 0.45]$` | random d_z (LLaMA) |\n| D7 | appendix_results.tex:10 | `$d_z = -0.04$` | random d_z |\n| D8 | appendix_moved.tex:56 | `$d_z = -0.04$` | random d_z |\n| D9 | appendix_disc_analysis.tex:14 | `$d_z{=}{-}0.04$` | random d_z |\n| D10 | appendix_disc_analysis.tex:49 | `$d_z{=}{-}0.04$` | random d_z |\n\n**修改方案**：\n- D1/D7/D8/D9/D10：删除 `$d_z{=}{-}0.04$`，替换为 `negligible median difference ($\\widetilde{\\Delta} = \\text{X}$)`\n- D2/D3：删除 imp-vs-rand d_z 序列，改为 `Wilcoxon signed-rank tests with median paired difference $\\widetilde{\\Delta}$ increasing from X to Y`\n- D4/D6：删除 random d_z，改为定性描述 `random eviction also shows a non-trivial phase gradient (Wilcoxon $p < \\text{X}$)`\n- D5：Table 3 重构——d_z 列替换为 within-importance d_z（low−high），或移除 d_z 列完全改为 Wilcoxon p + median_diff 结构\n\n---\n\n### A4. C8 partially_confirmed 限定语（LLaMA 相关断言检查）\n\n| # | 文件:行号 | 当前文本 | 状态 |\n|---|----------|---------|------|\n| C1 | abstract.tex:10 | `suggests cross-architecture generalization, though at...` | ✅ 合规 |\n| C2 | introduction.tex:15 | `partially extends to a distinct architecture` | ✅ 合规 |\n| C3 | results.tex:79 | `The qualitative pattern replicates` | ⚠️ **borderline** — 建议改为 `The qualitative pattern is directionally consistent` |\n| C4 | results.tex:81 | `The directional pattern...is qualitatively consistent across all three models` | ✅ 合规（后半句有 `substantially weaker` 限定） |\n| C5 | discussion.tex:11 | `provides partial support for the qualitative pattern` | ✅ 合规 |\n| C6 | conclusion.tex:4 | `partially extends cross-architecture` | ✅ 合规 |\n| C7 | limitations.tex:2 | `partially extends the findings beyond the Qwen2 architecture` | ✅ 合规 |\n| C8 | appendix_disc_analysis.tex:33 | `provides partial support` | ✅ 合规 |\n\n**唯一需修改**：results.tex:79 `The qualitative pattern replicates` → `The qualitative pattern is directionally consistent`\n\n---\n\n### A5. C5b Future Work 位置\n\n当前论文**没有独立的 Future Work section**。相关 mitigation 讨论分散在：\n\n| # | 文件:行号 | 当前内容 | 说明 |\n|---|----------|---------|------|\n| FW1 | discussion.tex:8 | `A phase-aware compression budget...could mitigate...` | mitigation 作为 implication 讨论 |\n| FW2 | conclusion.tex:5 | `These findings motivate phase-aware sparsity allocation...` | 一句话 motivation |\n\n**建议插入点**：conclusion.tex:5 之后（line 5 与 `\\end{document}` 之间），新增 Future Work 段落。或者在 discussion.tex:8 段落末尾追加 pilot 实验结果。\n\n具体推荐：**discussion.tex:8 段落末尾**追加 B2 文本（与 deployment implications 自然衔接），同时在 conclusion.tex:5 追加一句指向 discussion 的引用。\n\n---\n\n### A6. Figures（数据源与重生成需求）\n\n| # | 文件名 | 引用位置 | 数据源（n=50） | n=500 操作 |\n|---|--------|---------|---------------|-----------|\n| F1 | fig1_dose_response.pdf | results.tex:57, caption:58 | G values: imp=[5.6, 69.2, 103.1, 222.4, 274.2, 273.6], rand=[1.1, 0.95, 1.67, 1.61]. Bootstrap B=10000 CI in log space. 生成信息: `_project/chart/fig1_dose_response_bf16.txt` | 用 n=500 experiment_summary_table.json 重算 G 值 → 重新生成。Caption Q24 需同步更新 |\n| F2 | fig3_crossover.pdf | appendix_moved.tex:15, caption:16 | imp_high=0.032, rand_high=0.818; imp_mid=1.118, rand_mid=0.932; imp_low=7.196, rand_low=1.363. 生成信息: `_project/chart/fig3_crossover_bf16.txt` | 用 n=500 s=0.25 per-phase median II → 重新生成。Caption Q60 需同步更新 |\n| F3 | fig4_bootstrap.pdf | appendix_moved.tex:89, caption:90 | DS d_z: 0.44/0.52/0.68/0.80. QW d_z: 0.28/0.55/0.89/1.02. 生成信息: `_project/chart/fig4_forest_paired_dz.txt` | 用 n=500 paired d_z + permutation CI → 重新生成 |\n| F4 | fig5_crossmodel.pdf | appendix_moved.tex:47, caption:48 | DS Δ=[0.351, 1.136, 4.017, 9.954], QW Δ=[0.062, 0.286, 1.155, 2.594]. 生成信息: `_project/chart/fig5_crossmodel_bf16.txt` | 用 n=500 DS/QW paired median diffs → 重新生成。Caption Q63 需同步更新 |\n\n**注意**：所有 figure 生成脚本为服务器端执行（draw-paper-figure skill），无本地 .py 脚本。生成参数记录在 `_project/chart/` 目录下的 info 文件中。\n\n---\n\n## B. 预写文本\n\n### B1. Qwen Caveat（imp-vs-rand 不显著时使用）\n\n> **插入位置**：results.tex:71 之后（§5.4 Cross-Model Replication 末尾，Table/Figure 引用之前）\n\n```latex\nWhile Qwen2.5-7B-Instruct exhibits a significant within-importance severity gradient at $s \\geq 0.20$, the importance-versus-random contrast is attenuated relative to DeepSeek: the median paired difference remains modest across sparsity levels, and the permutation test reaches significance only at $s \\geq 0.25$. This attenuation likely reflects Qwen's lower compound interaction baseline under importance-based eviction at low sparsity---when the absolute severity is small, the strategy-dependent amplification has less room to manifest, even though the within-strategy phase gradient is robust.\n```\n\n### B2. C5b Future Work（Phase-Aware Mitigation Pilot）\n\n> **插入位置**：discussion.tex:8 段落末尾（`Extended discussion in Appendix~\\ref{app:extended-discussion}.` 之前），或 conclusion.tex:5 之前新起段落\n\n```latex\nA preliminary pilot experiment explored oracle phase-aware budget reallocation, shifting sparsity budget from high-severity low-sparsity phases to low-severity high-sparsity phases. The oracle recovery---measured as the fraction of compound interaction eliminated by phase-aware allocation---reached only 18\\%, well below a pre-registered 30\\% gate for claiming practical mitigation. This suggests that phase-aware budget reallocation alone is insufficient to neutralize the severity gradient, and that effective mitigation may require joint optimization of both budget allocation and eviction strategy selection across phases---a promising but open direction for future work.\n```\n\n### B3. Mid-Phase Null Rate（Qwen Mid-Phase 统计功效限制）\n\n> **插入位置**：results.tex:71 附近（Qwen 结果讨论中），或 appendix_moved.tex:26 之后（Cross-Model Replication Details）\n\n```latex\nOn Qwen2.5-7B-Instruct, approximately 45\\% of problems yield near-zero Interaction Index in the mid-sparsity phase, where attention patterns exhibit insufficient variation to produce measurable compound interaction. This elevated null rate reduces the effective sample size for mid-phase comparisons and limits statistical power for detecting phase gradients that span the mid-phase boundary; our primary analysis therefore focuses on the low--high phase contrast, which is unaffected by this limitation.\n```\n\n---\n\n## C. 按优先级排序的执行清单\n\n### 优先级 1（n=500 数据到手后立即执行）\n1. 替换 T1, T2, T5, T6 表格数据（DeepSeek/Qwen 核心表格）\n2. 更新 Q1-Q5, Q12, Q15-Q18, Q19-Q30, Q38-Q40, Q47-Q50, Q55-Q67, Q71-Q77（数值替换）\n3. 重新生成 F1-F4 图表\n\n### 优先级 2（D059 合规修复，不依赖 n=500 数据）\n4. 修复 D1-D10 全部 D059 违规\n5. 重构 T3 (Table 3) 列定义\n\n### 优先级 3（文本修改）\n6. 修复 C3（results.tex:79 LLaMA 限定语）\n7. 插入 B1（Qwen caveat，视 n=500 结果决定是否使用）\n8. 插入 B2（C5b future work）\n9. 插入 B3（mid-phase null rate）\n\n### 优先级 4（条件性更新）\n10. T4 (tab:cohens-d) — n=500 数据\n11. T7, T8 — 仅当 C4 entropy 分析基于 n=500 重跑时更新\n12. Q37, Q44, Q51 — LLaMA 倍数比（依赖 n=500 DS/QW 数据）\n13. 确认 LLaMA 是否重跑 n=500（影响 T3 数据、Q31-Q36）\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
````

</details>

---

### Assistant

_source line 82_

Now register the artifact.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10233ec7-5d03-448a-9224-b6173ea0cbe8",
  "uuid": "bf05c0af-e756-466e-bb17-8368ff971f3c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kh7Ws7oGJbzjUo6ByFNkNE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8700,
      "cache_read_input_tokens": 66190,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8700
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

_source line 83_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01G7djfdVu7xxhjkPdNm7Jd1`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__save_project_file",
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
  "session_id": "10233ec7-5d03-448a-9224-b6173ea0cbe8",
  "uuid": "b65ba4cb-b987-48db-b088-50f9fa1f1d1c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kh7Ws7oGJbzjUo6ByFNkNE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8700,
      "cache_read_input_tokens": 66190,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8700
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

_source line 84 · 2026-05-14T21:54:17.683Z_

<details><summary>↩ Tool result · `toolu_01G7djfdVu7xxhjkPdNm7Jd1`</summary>

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
  "session_id": "10233ec7-5d03-448a-9224-b6173ea0cbe8",
  "uuid": "18a1bd47-b0b1-4e23-856e-2e46c0caee94",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "select:mcp__agent-ml-research__save_project_file",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Assistant

_source line 85_

<details><summary>Logged reasoning block</summary>

```text
The save_project_file tool only allows writing to memory.md, writing_plan.yaml, or paper_framing.md. The artifact is already saved to the artifacts directory. Let me just verify the file was written correctly and summarize for the user.

Actually, I should check if there's a register_artifact tool available.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10233ec7-5d03-448a-9224-b6173ea0cbe8",
  "uuid": "11f712eb-a9b6-45ac-a536-ad2f2f367bcf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DLq9SSvt6domdvyzxXLMSP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 471,
      "cache_read_input_tokens": 74890,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 471
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

_source line 86_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01XPazPiRnfJjiKMTRiMTXAz`</summary>

```json
{
  "query": "register artifact",
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
  "session_id": "10233ec7-5d03-448a-9224-b6173ea0cbe8",
  "uuid": "e97655f8-7cec-4585-85d2-6ff2db20a090",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DLq9SSvt6domdvyzxXLMSP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 471,
      "cache_read_input_tokens": 74890,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 471
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

_source line 87 · 2026-05-14T21:54:22.266Z_

<details><summary>↩ Tool result · `toolu_01XPazPiRnfJjiKMTRiMTXAz`</summary>

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
  "session_id": "10233ec7-5d03-448a-9224-b6173ea0cbe8",
  "uuid": "0eb07581-8afd-435a-a996-68ea0d9c14e3",
  "tool_use_result": {
    "matches": [],
    "query": "register artifact",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Assistant

_source line 88_

Artifact 已写入 `artifacts/n500_paper_patch_plan.md`。

**产出摘要**：

**Part A — 精确位置清单**：
- **8 张表格**需数据替换（T1-T8），其中 T3 (tab:llama-cross-arch) 需 D059 结构重构
- **77 处定量声明**（Q1-Q77），精确到 file:line
- **10 处 D059 违规**（D1-D10）：abstract/results/discussion/appendix 中 imp-vs-rand 或 random d_z，需改为 Wilcoxon p + median_diff
- **1 处 C8 限定语需修改**：results.tex:79 `The qualitative pattern replicates` → `is directionally consistent`
- **C5b 插入点**：discussion.tex:8 段落末尾或 conclusion.tex:5 之前
- **4 张 figure** 需 n=500 数据重生成（F1-F4），数据源和生成参数已记录

**Part B — 预写文本**：
- **B1 Qwen caveat**：~2 句，说明 imp-vs-rand 对比在 Qwen 上衰减的原因（低 baseline）
- **B2 C5b future work**：~3 句，oracle recovery 18% < 30% gate，phase-aware mitigation 是开放方向
- **B3 Mid-phase null rate**：~2 句，Qwen mid-phase ~45% null rate 限制统计功效

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "10233ec7-5d03-448a-9224-b6173ea0cbe8",
  "uuid": "d452335d-0fa4-42a2-819a-4ae9762fd18f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MrhqpqzNCbkSevbgxrfGfP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 179,
      "cache_read_input_tokens": 75361,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 179
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

_source line 89_

Artifact 已写入 `artifacts/n500_paper_patch_plan.md`。

**产出摘要**：

**Part A — 精确位置清单**：
- **8 张表格**需数据替换（T1-T8），其中 T3 (tab:llama-cross-arch) 需 D059 结构重构
- **77 处定量声明**（Q1-Q77），精确到 file:line
- **10 处 D059 违规**（D1-D10）：abstract/results/discussion/appendix 中 imp-vs-rand 或 random d_z，需改为 Wilcoxon p + median_diff
- **1 处 C8 限定语需修改**：results.tex:79 `The qualitative pattern replicates` → `is directionally consistent`
- **C5b 插入点**：discussion.tex:8 段落末尾或 conclusion.tex:5 之前
- **4 张 figure** 需 n=500 数据重生成（F1-F4），数据源和生成参数已记录

**Part B — 预写文本**：
- **B1 Qwen caveat**：~2 句，说明 imp-vs-rand 对比在 Qwen 上衰减的原因（低 baseline）
- **B2 C5b future work**：~3 句，oracle recovery 18% < 30% gate，phase-aware mitigation 是开放方向
- **B3 Mid-phase null rate**：~2 句，Qwen mid-phase ~45% null rate 限制统计功效

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 339649,
  "duration_api_ms": 341291,
  "num_turns": 30,
  "stop_reason": "end_turn",
  "session_id": "10233ec7-5d03-448a-9224-b6173ea0cbe8",
  "total_cost_usd": 1.0898328499999999,
  "usage": {
    "input_tokens": 16,
    "cache_creation_input_tokens": 64093,
    "cache_read_input_tokens": 484425,
    "output_tokens": 16039,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 64093,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 426,
        "cache_read_input_tokens": 75361,
        "cache_creation_input_tokens": 179,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 179
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1939,
      "outputTokens": 946,
      "cacheReadInputTokens": 17926,
      "cacheCreationInputTokens": 30018,
      "webSearchRequests": 0,
      "costUSD": 0.0459841,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 16,
      "outputTokens": 16039,
      "cacheReadInputTokens": 484425,
      "cacheCreationInputTokens": 64093,
      "webSearchRequests": 0,
      "costUSD": 1.04384875,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "8cb6fa4a-1e16-4ed7-89d7-d6bcdecec8a7"
}
```

</details>

---
