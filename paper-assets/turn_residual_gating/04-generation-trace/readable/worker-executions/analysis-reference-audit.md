# analysis reference audit

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 75
- **Recorded user turns:** 0
- **Tool calls:** 28
- **Original source:** `logs/workers/worker_analysis_reference_audit_20260522T042955.log`
- **Structured JSON:** [`32aa6645d8de1065459c.json`](../../sessions/32/32aa6645d8de1065459c.json)

## Before a recorded user message

75 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating",
  "session_id": "652e1b48-5425-4360-9d09-b4c254656213",
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
    "mcp__agent-ml-research__save_project_file",
    "mcp__agent-ml-research__verify_references"
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
  "uuid": "cdb20d27-d176-48d4-a447-73469bed0f12",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-turn-residual-gating/memory/"
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
    "resetsAt": 1779441600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "5762d046-f165-42f3-b2c8-16486dd20523",
  "session_id": "652e1b48-5425-4360-9d09-b4c254656213"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the reference audit skill file, then proceed with the audit.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "652e1b48-5425-4360-9d09-b4c254656213",
  "uuid": "367206f7-a5db-44c3-a063-3a7a325e76b4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L3ZAu5epWTpoQfm2cRopsM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12802,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12802
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

读取 skill 文件和 bib 文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "652e1b48-5425-4360-9d09-b4c254656213",
  "uuid": "d992d8be-1f6d-454e-ade2-2bbea7b00bff",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L3ZAu5epWTpoQfm2cRopsM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12802,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12802
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

<details open><summary>🔧 Tool call — Read · `toolu_01QWDayE7VhiyYo68v2dmcm9`</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/reference-audit.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "652e1b48-5425-4360-9d09-b4c254656213",
  "uuid": "2867bf2c-44f1-4e67-b87b-4766deb08e5f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L3ZAu5epWTpoQfm2cRopsM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12802,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12802
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

_source line 7 · 2026-05-22T04:30:08.114Z_

<details><summary>↩ Tool result · `toolu_01QWDayE7VhiyYo68v2dmcm9`</summary>

````text
1	---
2	name: reference-audit
3	description: 引用验证与审计——检查 bib 条目完整性、引用真实性、格式一致性。写论文、审查论文、提交前检查引用时使用。关键词：citation verification、引用检查、bib 审计、fake citation、引用格式。
4	scope: global
5	tags:
6	- workflow
7	- submission
8	- writing
9	- quality
10	priority: 6
11	version: 2
12	roles:
13	- agent
14	- paper_agent
15	- review_reviewer
16	- worker
17	---
18	
19	# 引用验证与审计（Reference Audit）
20	
21	## 核心原则
22	
23	**写时验证，而非写后检查。** 每添加一条引用，立即验证真实性。AI 生成的引用约 40% 存在错误——绝不信任记忆中的引用信息。
24	
25	## 触发条件
26	
27	- 写论文时添加引用
28	- Review Reviewer 审查论文引用质量
29	- 提交前最终检查
30	- 发现可疑引用（年份不对、作者不存在、找不到原文）
31	
32	## 验证流程
33	
34	### 1. 单条引用验证（写论文时）
35	
36	每次需要引用时：
37	
38	1. **WebSearch 查找**：搜索论文标题 + 第一作者
39	2. **Google Scholar 确认**：`site:scholar.google.com [论文标题] [作者]`
40	3. **核对关键信息**：标题、第一作者、年份（±1 年）、venue
41	4. **获取 BibTeX**：从 Google Scholar 或 DBLP 获取标准格式
42	5. **验证 claim**（如果引用了具体结论）：确认该 claim 确实出现在原文中
43	
44	### 2. 全文引用审计（批量检查）
45	
46	**Step 1：调用 `verify_references(paper_dir)`**
47	
48	这是首选方式。该工具自动完成：
49	- 解析所有 .bib 文件，提取结构化条目
50	- 解析所有 .tex 文件，提取 `\cite{}`/`\citep{}`/`\citet{}` 引用
51	- 交叉检查：找出 orphan（.bib 有但未引用）和 missing（引用了但 .bib 没有）
52	- 调 OpenAlex API 在线验证每条引用是否存在（返回 verified/not_found/mismatch）
53	
54	如果只需快速离线检查，传 `skip_online=True`。
55	
56	**Step 2：人工复核工具报告中的问题条目**
57	
58	重点关注：
59	- `status: not_found` — 可能是幻觉引用，用 WebSearch 二次验证
60	- `status: mismatch` — 年份等信息不一致，检查 preprint vs published 版本
61	- `missing_bib` — 正文引用了但 .bib 中不存在，编译会报错
62	- `orphan_bib` — .bib 中有但正文未引用，清理或补引用
63	
64	**Step 3：语义验证**（优先级排序）
65	1. 首先验证 Introduction 和 Related Work 中的高频引用
66	2. 然后验证 Method 中支撑技术 claim 的引用
67	3. 最后验证其余引用
68	
69	对于 OpenAlex 未找到的条目，用 WebSearch 补充验证（arXiv、DOI、DBLP）。
70	
71	### 3. 验证失败处理
72	
73	**找不到论文时**：
74	1. 检查拼写——标题或作者名是否有误？
75	2. 尝试不同查询组合（WebSearch + Google Scholar + DBLP）
76	3. 标记为 `[CITATION NEEDED]`
77	4. 明确告知——说明哪条引用无法验证
78	
79	**信息不匹配时**：
80	1. 确认是否找对了论文
81	2. 检查版本——preprint vs published 版本
82	3. 用最准确的版本更新信息
83	
84	**绝不做的事**：
85	- 从记忆生成 BibTeX——AI 生成引用 40% 错误率
86	- 跳过验证步骤
87	- 假设论文存在
88	- 对无法验证的引用不做标记
89	
90	## 常见引用问题模式
91	
92	| 问题类型 | 特征 | 风险 |
93	|---------|------|------|
94	| **幻觉引用** | 论文不存在，作者或标题是 AI 编造的 | 严重——直接影响学术诚信 |
95	| **信息错位** | 作者、年份、venue 不匹配 | 中等——reviewer 一查就发现 |
96	| **孤立引用** | .bib 有但正文没引用 | 轻微——但显得不够整洁 |
97	| **缺失引用** | 正文引用但 .bib 没有 | 编译错误——必须修复 |
98	| **Claim 不匹配** | 引用了论文但声称的结论不在原文中 | 严重——误导性引用 |
99	
100	## 输出格式
101	
102	审计完成后，生成结构化报告：
103	
104	```
105	## 引用审计报告
106	
107	**总数**: X 条引用
108	**已验证**: Y 条（OpenAlex confirmed）
109	**问题**: Z 条
110	
111	### 问题列表
112	
113	1. [severity: critical] `\cite{xxx}` — OpenAlex 未找到，WebSearch 也无结果，疑似幻觉引用
114	   - 建议：删除或替换为已验证的替代引用
115	
116	2. [severity: warning] `\cite{yyy}` — 年份不匹配（bib: 2023, OpenAlex: 2022）
117	   - 建议：更新为正确年份
118	
119	3. [severity: info] `\cite{zzz}` — bib 中存在但正文未引用
120	   - 建议：删除或在相关段落补充引用
121	```
122	
123	## 设计参考
124	
125	本 skill 的验证原则参考了 Dr. Claw (K-Dense Inc.) 的 inno-reference-audit skill。
126	
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "652e1b48-5425-4360-9d09-b4c254656213",
  "uuid": "72e76717-642d-4c61-9d47-15b83d6ddfab",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/agent-ml-research/skills/global/reference-audit.skill.md",
      "content": "---\nname: reference-audit\ndescription: 引用验证与审计——检查 bib 条目完整性、引用真实性、格式一致性。写论文、审查论文、提交前检查引用时使用。关键词：citation verification、引用检查、bib 审计、fake citation、引用格式。\nscope: global\ntags:\n- workflow\n- submission\n- writing\n- quality\npriority: 6\nversion: 2\nroles:\n- agent\n- paper_agent\n- review_reviewer\n- worker\n---\n\n# 引用验证与审计（Reference Audit）\n\n## 核心原则\n\n**写时验证，而非写后检查。** 每添加一条引用，立即验证真实性。AI 生成的引用约 40% 存在错误——绝不信任记忆中的引用信息。\n\n## 触发条件\n\n- 写论文时添加引用\n- Review Reviewer 审查论文引用质量\n- 提交前最终检查\n- 发现可疑引用（年份不对、作者不存在、找不到原文）\n\n## 验证流程\n\n### 1. 单条引用验证（写论文时）\n\n每次需要引用时：\n\n1. **WebSearch 查找**：搜索论文标题 + 第一作者\n2. **Google Scholar 确认**：`site:scholar.google.com [论文标题] [作者]`\n3. **核对关键信息**：标题、第一作者、年份（±1 年）、venue\n4. **获取 BibTeX**：从 Google Scholar 或 DBLP 获取标准格式\n5. **验证 claim**（如果引用了具体结论）：确认该 claim 确实出现在原文中\n\n### 2. 全文引用审计（批量检查）\n\n**Step 1：调用 `verify_references(paper_dir)`**\n\n这是首选方式。该工具自动完成：\n- 解析所有 .bib 文件，提取结构化条目\n- 解析所有 .tex 文件，提取 `\\cite{}`/`\\citep{}`/`\\citet{}` 引用\n- 交叉检查：找出 orphan（.bib 有但未引用）和 missing（引用了但 .bib 没有）\n- 调 OpenAlex API 在线验证每条引用是否存在（返回 verified/not_found/mismatch）\n\n如果只需快速离线检查，传 `skip_online=True`。\n\n**Step 2：人工复核工具报告中的问题条目**\n\n重点关注：\n- `status: not_found` — 可能是幻觉引用，用 WebSearch 二次验证\n- `status: mismatch` — 年份等信息不一致，检查 preprint vs published 版本\n- `missing_bib` — 正文引用了但 .bib 中不存在，编译会报错\n- `orphan_bib` — .bib 中有但正文未引用，清理或补引用\n\n**Step 3：语义验证**（优先级排序）\n1. 首先验证 Introduction 和 Related Work 中的高频引用\n2. 然后验证 Method 中支撑技术 claim 的引用\n3. 最后验证其余引用\n\n对于 OpenAlex 未找到的条目，用 WebSearch 补充验证（arXiv、DOI、DBLP）。\n\n### 3. 验证失败处理\n\n**找不到论文时**：\n1. 检查拼写——标题或作者名是否有误？\n2. 尝试不同查询组合（WebSearch + Google Scholar + DBLP）\n3. 标记为 `[CITATION NEEDED]`\n4. 明确告知——说明哪条引用无法验证\n\n**信息不匹配时**：\n1. 确认是否找对了论文\n2. 检查版本——preprint vs published 版本\n3. 用最准确的版本更新信息\n\n**绝不做的事**：\n- 从记忆生成 BibTeX——AI 生成引用 40% 错误率\n- 跳过验证步骤\n- 假设论文存在\n- 对无法验证的引用不做标记\n\n## 常见引用问题模式\n\n| 问题类型 | 特征 | 风险 |\n|---------|------|------|\n| **幻觉引用** | 论文不存在，作者或标题是 AI 编造的 | 严重——直接影响学术诚信 |\n| **信息错位** | 作者、年份、venue 不匹配 | 中等——reviewer 一查就发现 |\n| **孤立引用** | .bib 有但正文没引用 | 轻微——但显得不够整洁 |\n| **缺失引用** | 正文引用但 .bib 没有 | 编译错误——必须修复 |\n| **Claim 不匹配** | 引用了论文但声称的结论不在原文中 | 严重——误导性引用 |\n\n## 输出格式\n\n审计完成后，生成结构化报告：\n\n```\n## 引用审计报告\n\n**总数**: X 条引用\n**已验证**: Y 条（OpenAlex confirmed）\n**问题**: Z 条\n\n### 问题列表\n\n1. [severity: critical] `\\cite{xxx}` — OpenAlex 未找到，WebSearch 也无结果，疑似幻觉引用\n   - 建议：删除或替换为已验证的替代引用\n\n2. [severity: warning] `\\cite{yyy}` — 年份不匹配（bib: 2023, OpenAlex: 2022）\n   - 建议：更新为正确年份\n\n3. [severity: info] `\\cite{zzz}` — bib 中存在但正文未引用\n   - 建议：删除或在相关段落补充引用\n```\n\n## 设计参考\n\n本 skill 的验证原则参考了 Dr. Claw (K-Dense Inc.) 的 inno-reference-audit skill。\n",
      "numLines": 126,
      "startLine": 1,
      "totalLines": 126
    }
  }
}
````

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — Read · `toolu_01SQp8RHH6WRbidKiTN6moEJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "652e1b48-5425-4360-9d09-b4c254656213",
  "uuid": "6ad12c99-3463-4454-b96d-a142b1bb20bc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L3ZAu5epWTpoQfm2cRopsM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12802,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12802
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

_source line 9 · 2026-05-22T04:30:08.325Z_

<details><summary>↩ Tool result · `toolu_01SQp8RHH6WRbidKiTN6moEJ`</summary>

```text
1	% ============================================================
2	% Layer Importance
3	% ============================================================
4	
5	@inproceedings{gromov2024deeper,
6	  author    = {Gromov and others},
7	  title     = {{The Unreasonable Ineffectiveness of the Deeper Layers}},
8	  booktitle = {International Conference on Learning Representations},
9	  year      = {2024},
10	  url       = {https://arxiv.org/abs/2403.17887}
11	}
12	
13	@article{men2024shortgpt,
14	  author  = {Men and others},
15	  title   = {{ShortGPT: Layers in Large Language Models are More Redundant Than You Expect}},
16	  journal = {arXiv preprint arXiv:2403.03853},
17	  year    = {2024},
18	  url     = {https://arxiv.org/abs/2403.03853}
19	}
20	
21	@inproceedings{sun2025curse,
22	  author    = {Sun and others},
23	  title     = {{The Curse of Depth in Large Language Models}},
24	  booktitle = {Advances in Neural Information Processing Systems},
25	  year      = {2025},
26	  url       = {https://arxiv.org/abs/2502.05795}
27	}
28	
29	@article{anonymous2024reassessing,
30	  author  = {{Anonymous}},
31	  title   = {{Reassessing Layer Pruning in LLMs: New Insights and Methods}},
32	  journal = {arXiv preprint arXiv:2411.15558},
33	  year    = {2024},
34	  url     = {https://arxiv.org/abs/2411.15558}
35	}
36	
37	@inproceedings{fan2020layerdrop,
38	  author    = {Fan and others},
39	  title     = {{Reducing Transformer Depth on Demand with Structured Dropout (LayerDrop)}},
40	  booktitle = {International Conference on Learning Representations},
41	  year      = {2020},
42	  url       = {https://arxiv.org/abs/1909.11556}
43	}
44	
45	% ============================================================
46	% Multi-Turn Attention
47	% ============================================================
48	
49	@article{dongre2026attention,
50	  author  = {Dongre and Hsieh and Lai and Yoon and Bui and Hakkani-Tur},
51	  title   = {{When Attention Closes: How LLMs Lose the Thread in Multi-Turn Interaction}},
52	  journal = {arXiv preprint arXiv:2605.12922},
53	  year    = {2026},
54	  url     = {https://arxiv.org/abs/2605.12922}
55	}
56	
57	@article{levy2025lost,
58	  author  = {Levy and others},
59	  title   = {{LLMs Get Lost In Multi-Turn Conversation}},
60	  journal = {arXiv preprint arXiv:2505.06120},
61	  year    = {2025},
62	  url     = {https://arxiv.org/abs/2505.06120}
63	}
64	
65	@article{liu2026intent,
66	  author  = {Liu and others},
67	  title   = {{Intent Mismatch Causes LLMs to Get Lost in Multi-Turn Conversation}},
68	  journal = {arXiv preprint arXiv:2602.07338},
69	  year    = {2026},
70	  url     = {https://arxiv.org/abs/2602.07338}
71	}
72	
73	@article{liu2023lost,
74	  author  = {Liu and others},
75	  title   = {{Lost in the Middle: How Language Models Use Long Contexts}},
76	  journal = {Transactions of the Association for Computational Linguistics},
77	  year    = {2023},
78	  url     = {https://arxiv.org/abs/2307.03172}
79	}
80	
81	@article{anonymous2025style,
82	  author  = {{Anonymous}},
83	  title   = {{Style Amnesia: Investigating Speaking Style Degradation and Mitigation in Multi-Turn Spoken Language Models}},
84	  journal = {arXiv preprint arXiv:2512.23578},
85	  year    = {2025},
86	  url     = {https://arxiv.org/abs/2512.23578}
87	}
88	
89	% ============================================================
90	% Residual Gating
91	% ============================================================
92	
93	@article{raposo2024mixture,
94	  author  = {Raposo and others},
95	  title   = {{Mixture-of-Depths: Dynamically Allocating Compute in Transformer-Based Language Models}},
96	  journal = {arXiv preprint arXiv:2404.02258},
97	  year    = {2024},
98	  url     = {https://arxiv.org/abs/2404.02258}
99	}
100	
101	@inproceedings{schuster2022calm,
102	  author    = {Schuster and others},
103	  title     = {{Confident Adaptive Language Modeling}},
104	  booktitle = {Advances in Neural Information Processing Systems},
105	  year      = {2022},
106	  url       = {https://arxiv.org/abs/2207.07061}
107	}
108	
109	@inproceedings{qiu2025gated,
110	  author    = {Qiu and others},
111	  title     = {{Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free}},
112	  booktitle = {Advances in Neural Information Processing Systems},
113	  year      = {2025},
114	  url       = {https://arxiv.org/abs/2505.06708}
115	}
116	
117	@inproceedings{wang2018skipnet,
118	  author    = {Wang and others},
119	  title     = {{SkipNet: Learning Dynamic Routing in Convolutional Networks}},
120	  booktitle = {European Conference on Computer Vision},
121	  year      = {2018},
122	  url       = {https://arxiv.org/abs/1711.09485}
123	}
124	
125	@article{luo2025flexidepth,
126	  author  = {Luo and others},
127	  title   = {{Adaptive Layer-skipping in Pre-trained LLMs (FlexiDepth)}},
128	  journal = {arXiv preprint arXiv:2503.23798},
129	  year    = {2025},
130	  url     = {https://arxiv.org/abs/2503.23798}
131	}
132	
133	@article{lawson2025skip,
134	  author  = {Lawson and others},
135	  title   = {{Learning to Skip the Middle Layers of Transformers}},
136	  journal = {arXiv preprint arXiv:2506.21103},
137	  year    = {2025},
138	  url     = {https://arxiv.org/abs/2506.21103}
139	}
140	
141	% ============================================================
142	% Attention Manipulation
143	% ============================================================
144	
145	@inproceedings{press2022alibi,
146	  author    = {Press and others},
147	  title     = {{Train Short, Test Long: Attention with Linear Biases Enables Input Length Extrapolation}},
148	  booktitle = {International Conference on Learning Representations},
149	  year      = {2022},
150	  url       = {https://arxiv.org/abs/2108.12409}
151	}
152	
153	@article{chen2023positional,
154	  author  = {Chen and others},
155	  title   = {{Extending Context Window of Large Language Models via Positional Interpolation}},
156	  journal = {arXiv preprint arXiv:2306.15595},
157	  year    = {2023},
158	  url     = {https://arxiv.org/abs/2306.15595}
159	}
160	
161	@inproceedings{peng2024yarn,
162	  author    = {Peng and others},
163	  title     = {{YaRN: Efficient Context Window Extension of Large Language Models}},
164	  booktitle = {International Conference on Learning Representations},
165	  year      = {2024},
166	  url       = {https://arxiv.org/abs/2309.00071}
167	}
168	
169	@inproceedings{xiao2024streaming,
170	  author    = {Xiao and others},
171	  title     = {{Efficient Streaming Language Models with Attention Sinks}},
172	  booktitle = {International Conference on Learning Representations},
173	  year      = {2024},
174	  url       = {https://arxiv.org/abs/2309.17453}
175	}
176	
177	@inproceedings{han2024lminfinite,
178	  author    = {Han and others},
179	  title     = {{LM-Infinite: Zero-Shot Extreme Length Generalization for Large Language Models}},
180	  booktitle = {Annual Meeting of the Association for Computational Linguistics},
181	  year      = {2024},
182	  url       = {https://arxiv.org/abs/2308.16137}
183	}
184	
185	@article{ko2024found,
186	  author  = {Ko and others},
187	  title   = {{Found in the Middle: Calibrating Positional Attention Bias Improves Long Context Utilization}},
188	  journal = {arXiv preprint arXiv:2406.16008},
189	  year    = {2024},
190	  url     = {https://arxiv.org/abs/2406.16008}
191	}
192	
193	% ============================================================
194	% Theoretical Foundations
195	% ============================================================
196	
197	@article{elhage2021framework,
198	  author  = {Elhage and others},
199	  title   = {{A Mathematical Framework for Transformer Circuits}},
200	  journal = {Anthropic Blog},
201	  year    = {2021},
202	  url     = {https://transformer-circuits.pub/2021/framework/index.html}
203	}
204	
205	@article{elhage2022superposition,
206	  author  = {Elhage and others},
207	  title   = {{Toy Models of Superposition}},
208	  journal = {arXiv preprint arXiv:2209.10652},
209	  year    = {2022},
210	  url     = {https://arxiv.org/abs/2209.10652}
211	}
212	
213	@article{belrose2023tuned,
214	  author  = {Belrose and others},
215	  title   = {{Eliciting Latent Predictions from Transformers with the Tuned Lens}},
216	  journal = {arXiv preprint arXiv:2303.08112},
217	  year    = {2023},
218	  url     = {https://arxiv.org/abs/2303.08112}
219	}
220	
221	@article{yu2023residual,
222	  author  = {Yu and others},
223	  title   = {{Exploring the Residual Stream of Transformers}},
224	  journal = {arXiv preprint arXiv:2312.12141},
225	  year    = {2023},
226	  url     = {https://arxiv.org/abs/2312.12141}
227	}
228	
229	@inproceedings{makkuva2025markov,
230	  author    = {Makkuva and others},
231	  title     = {{Attention with Markov: A Framework for Principled Analysis of Transformers via Markov Chains}},
232	  booktitle = {International Conference on Learning Representations},
233	  year      = {2025},
234	  url       = {https://arxiv.org/abs/2402.04161}
235	}
236	
237	@inproceedings{ildiz2024markov,
238	  author    = {Ildiz and others},
239	  title     = {{From Self-Attention to Markov Models: Unveiling the Dynamics of Generative Transformers}},
240	  booktitle = {International Conference on Machine Learning},
241	  year      = {2024},
242	  url       = {https://arxiv.org/abs/2402.13512}
243	}
244	
245	% ============================================================
246	% Evaluation Benchmarks
247	% ============================================================
248	
249	@inproceedings{zheng2023mtbench,
250	  author    = {Zheng and others},
251	  title     = {{Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena}},
252	  booktitle = {Advances in Neural Information Processing Systems},
253	  year      = {2023},
254	  url       = {https://arxiv.org/abs/2306.05685}
255	}
256	
257	@inproceedings{chiang2024arena,
258	  author    = {Chiang and others},
259	  title     = {{Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference}},
260	  booktitle = {International Conference on Machine Learning},
261	  year      = {2024},
262	  url       = {https://arxiv.org/abs/2403.04132}
263	}
264	
265	@inproceedings{dubois2024alpacaeval,
266	  author    = {Dubois and others},
267	  title     = {{Length-Controlled AlpacaEval: A Simple Way to Debias Automatic Evaluators}},
268	  booktitle = {Conference on Language Modeling},
269	  year      = {2024},
270	  url       = {https://arxiv.org/abs/2404.04475}
271	}
272	
273	@article{lin2024wildbench,
274	  author  = {Lin and others},
275	  title   = {{WildBench: Benchmarking LLMs with Challenging Tasks from Real Users in the Wild}},
276	  journal = {arXiv preprint arXiv:2406.04770},
277	  year    = {2024},
278	  url     = {https://arxiv.org/abs/2406.04770}
279	}
280	
281	@inproceedings{bai2024mtbench101,
282	  author    = {Bai and others},
283	  title     = {{MT-Bench-101: A Fine-Grained Benchmark for Evaluating Large Language Models in Multi-Turn Dialogues}},
284	  booktitle = {Annual Meeting of the Association for Computational Linguistics},
285	  year      = {2024},
286	  url       = {https://arxiv.org/abs/2402.14762}
287	}
288	
289	@article{sirdeshmukh2025multichallenge,
290	  author  = {Sirdeshmukh and others},
291	  title   = {{MultiChallenge: A Realistic Multi-Turn Conversation Evaluation Benchmark Challenging to Frontier LLMs}},
292	  journal = {arXiv preprint arXiv:2501.17399},
293	  year    = {2025},
294	  url     = {https://arxiv.org/abs/2501.17399}
295	}
296	
297	% ============================================================
298	% Exposure Bias
299	% ============================================================
300	
301	@inproceedings{bengio2015scheduled,
302	  author    = {Bengio and Vinyals and Jaitly and Shazeer},
303	  title     = {{Scheduled Sampling for Sequence Prediction with Recurrent Neural Networks}},
304	  booktitle = {Advances in Neural Information Processing Systems},
305	  year      = {2015},
306	  url       = {https://arxiv.org/abs/1506.03099}
307	}
308	
309	@inproceedings{ranzato2016sequence,
310	  author    = {Ranzato and Chopra and Auli and Zaremba},
311	  title     = {{Sequence Level Training with Recurrent Neural Networks}},
312	  booktitle = {International Conference on Learning Representations},
313	  year      = {2016},
314	  url       = {https://arxiv.org/abs/1511.06732}
315	}
316	
317	@inproceedings{lamb2016professor,
318	  author    = {Lamb and Goyal and Zhang and Zhang and Courville and Bengio},
319	  title     = {{Professor Forcing: A New Algorithm for Training Recurrent Networks}},
320	  booktitle = {Advances in Neural Information Processing Systems},
321	  year      = {2016},
322	  url       = {https://arxiv.org/abs/1610.09038}
323	}
324	
325	@inproceedings{leblond2018searnn,
326	  author    = {Leblond and Alayrac and Osokin and Lacoste-Julien},
327	  title     = {{SEARNN: Training RNNs with Global-Local Losses}},
328	  booktitle = {International Conference on Learning Representations},
329	  year      = {2018},
330	  url       = {https://arxiv.org/abs/1706.04499}
331	}
332	
333	@article{he2019exposure,
334	  author  = {He and Zhang and Zhou and Glass},
335	  title   = {{Quantifying Exposure Bias for Neural Language Generation}},
336	  journal = {arXiv preprint arXiv:1905.10617},
337	  year    = {2019},
338	  url     = {https://arxiv.org/abs/1905.10617}
339	}
340	
341	% ============================================================
342	% Gradient Conflict / Multi-Task Learning
343	% ============================================================
344	
345	@inproceedings{yu2020pcgrad,
346	  author    = {Yu and Kumar and Gupta and Levine and Hausman and Finn},
347	  title     = {{Gradient Surgery for Multi-Task Learning}},
348	  booktitle = {Advances in Neural Information Processing Systems},
349	  year      = {2020},
350	  url       = {https://arxiv.org/abs/2001.06782}
351	}
352	
353	@inproceedings{chen2018gradnorm,
354	  author    = {Chen and Badrinarayanan and Lee and Rabinovich},
355	  title     = {{GradNorm: Gradient Normalization for Adaptive Loss Balancing in Deep Multitask Networks}},
356	  booktitle = {International Conference on Machine Learning},
357	  year      = {2018},
358	  url       = {https://arxiv.org/abs/1711.02257}
359	}
360	
361	@inproceedings{liu2021cagrad,
362	  author    = {Liu and Liu and Jin and Stone and Liu},
363	  title     = {{Conflict-Averse Gradient Descent for Multi-task Learning}},
364	  booktitle = {Advances in Neural Information Processing Systems},
365	  year      = {2021},
366	  url       = {https://arxiv.org/abs/2110.14048}
367	}
368	
369	@inproceedings{navon2022nash,
370	  author    = {Navon and Shamsian and Achituve and Maron and Kawaguchi and Chechik and Fetaya},
371	  title     = {{Multi-Task Learning as a Bargaining Game}},
372	  booktitle = {International Conference on Machine Learning},
373	  year      = {2022},
374	  url       = {https://arxiv.org/abs/2202.01017}
375	}
376	
377	% ============================================================
378	% Residual Scaling
379	% ============================================================
380	
381	@inproceedings{bachlechner2021rezero,
382	  author    = {Bachlechner and Majumder and Mao and Cottrell and McAuley},
383	  title     = {{ReZero is All You Need: Fast Convergence at Large Depth}},
384	  booktitle = {Uncertainty in Artificial Intelligence},
385	  year      = {2021},
386	  url       = {https://arxiv.org/abs/2003.04887}
387	}
388	
389	@inproceedings{zhang2019fixup,
390	  author    = {Zhang and Dauphin and Ma},
391	  title     = {{Fixup Initialization: Residual Learning Without Normalization}},
392	  booktitle = {International Conference on Learning Representations},
393	  year      = {2019},
394	  url       = {https://arxiv.org/abs/1901.09321}
395	}
396	
397	@article{grattafiori2024llama3,
398	  author  = {Grattafiori and 1 others},
399	  title   = {{The Llama 3 Herd of Models}},
400	  journal = {arXiv preprint arXiv:2407.21783},
401	  year    = {2024}
402	}
403	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "652e1b48-5425-4360-9d09-b4c254656213",
  "uuid": "d962bfee-c98b-4b77-8900-1b3a198d49e9",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/references.bib",
      "content": "% ============================================================\n% Layer Importance\n% ============================================================\n\n@inproceedings{gromov2024deeper,\n  author    = {Gromov and others},\n  title     = {{The Unreasonable Ineffectiveness of the Deeper Layers}},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2403.17887}\n}\n\n@article{men2024shortgpt,\n  author  = {Men and others},\n  title   = {{ShortGPT: Layers in Large Language Models are More Redundant Than You Expect}},\n  journal = {arXiv preprint arXiv:2403.03853},\n  year    = {2024},\n  url     = {https://arxiv.org/abs/2403.03853}\n}\n\n@inproceedings{sun2025curse,\n  author    = {Sun and others},\n  title     = {{The Curse of Depth in Large Language Models}},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2502.05795}\n}\n\n@article{anonymous2024reassessing,\n  author  = {{Anonymous}},\n  title   = {{Reassessing Layer Pruning in LLMs: New Insights and Methods}},\n  journal = {arXiv preprint arXiv:2411.15558},\n  year    = {2024},\n  url     = {https://arxiv.org/abs/2411.15558}\n}\n\n@inproceedings{fan2020layerdrop,\n  author    = {Fan and others},\n  title     = {{Reducing Transformer Depth on Demand with Structured Dropout (LayerDrop)}},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2020},\n  url       = {https://arxiv.org/abs/1909.11556}\n}\n\n% ============================================================\n% Multi-Turn Attention\n% ============================================================\n\n@article{dongre2026attention,\n  author  = {Dongre and Hsieh and Lai and Yoon and Bui and Hakkani-Tur},\n  title   = {{When Attention Closes: How LLMs Lose the Thread in Multi-Turn Interaction}},\n  journal = {arXiv preprint arXiv:2605.12922},\n  year    = {2026},\n  url     = {https://arxiv.org/abs/2605.12922}\n}\n\n@article{levy2025lost,\n  author  = {Levy and others},\n  title   = {{LLMs Get Lost In Multi-Turn Conversation}},\n  journal = {arXiv preprint arXiv:2505.06120},\n  year    = {2025},\n  url     = {https://arxiv.org/abs/2505.06120}\n}\n\n@article{liu2026intent,\n  author  = {Liu and others},\n  title   = {{Intent Mismatch Causes LLMs to Get Lost in Multi-Turn Conversation}},\n  journal = {arXiv preprint arXiv:2602.07338},\n  year    = {2026},\n  url     = {https://arxiv.org/abs/2602.07338}\n}\n\n@article{liu2023lost,\n  author  = {Liu and others},\n  title   = {{Lost in the Middle: How Language Models Use Long Contexts}},\n  journal = {Transactions of the Association for Computational Linguistics},\n  year    = {2023},\n  url     = {https://arxiv.org/abs/2307.03172}\n}\n\n@article{anonymous2025style,\n  author  = {{Anonymous}},\n  title   = {{Style Amnesia: Investigating Speaking Style Degradation and Mitigation in Multi-Turn Spoken Language Models}},\n  journal = {arXiv preprint arXiv:2512.23578},\n  year    = {2025},\n  url     = {https://arxiv.org/abs/2512.23578}\n}\n\n% ============================================================\n% Residual Gating\n% ============================================================\n\n@article{raposo2024mixture,\n  author  = {Raposo and others},\n  title   = {{Mixture-of-Depths: Dynamically Allocating Compute in Transformer-Based Language Models}},\n  journal = {arXiv preprint arXiv:2404.02258},\n  year    = {2024},\n  url     = {https://arxiv.org/abs/2404.02258}\n}\n\n@inproceedings{schuster2022calm,\n  author    = {Schuster and others},\n  title     = {{Confident Adaptive Language Modeling}},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2022},\n  url       = {https://arxiv.org/abs/2207.07061}\n}\n\n@inproceedings{qiu2025gated,\n  author    = {Qiu and others},\n  title     = {{Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free}},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2505.06708}\n}\n\n@inproceedings{wang2018skipnet,\n  author    = {Wang and others},\n  title     = {{SkipNet: Learning Dynamic Routing in Convolutional Networks}},\n  booktitle = {European Conference on Computer Vision},\n  year      = {2018},\n  url       = {https://arxiv.org/abs/1711.09485}\n}\n\n@article{luo2025flexidepth,\n  author  = {Luo and others},\n  title   = {{Adaptive Layer-skipping in Pre-trained LLMs (FlexiDepth)}},\n  journal = {arXiv preprint arXiv:2503.23798},\n  year    = {2025},\n  url     = {https://arxiv.org/abs/2503.23798}\n}\n\n@article{lawson2025skip,\n  author  = {Lawson and others},\n  title   = {{Learning to Skip the Middle Layers of Transformers}},\n  journal = {arXiv preprint arXiv:2506.21103},\n  year    = {2025},\n  url     = {https://arxiv.org/abs/2506.21103}\n}\n\n% ============================================================\n% Attention Manipulation\n% ============================================================\n\n@inproceedings{press2022alibi,\n  author    = {Press and others},\n  title     = {{Train Short, Test Long: Attention with Linear Biases Enables Input Length Extrapolation}},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2022},\n  url       = {https://arxiv.org/abs/2108.12409}\n}\n\n@article{chen2023positional,\n  author  = {Chen and others},\n  title   = {{Extending Context Window of Large Language Models via Positional Interpolation}},\n  journal = {arXiv preprint arXiv:2306.15595},\n  year    = {2023},\n  url     = {https://arxiv.org/abs/2306.15595}\n}\n\n@inproceedings{peng2024yarn,\n  author    = {Peng and others},\n  title     = {{YaRN: Efficient Context Window Extension of Large Language Models}},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2309.00071}\n}\n\n@inproceedings{xiao2024streaming,\n  author    = {Xiao and others},\n  title     = {{Efficient Streaming Language Models with Attention Sinks}},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2309.17453}\n}\n\n@inproceedings{han2024lminfinite,\n  author    = {Han and others},\n  title     = {{LM-Infinite: Zero-Shot Extreme Length Generalization for Large Language Models}},\n  booktitle = {Annual Meeting of the Association for Computational Linguistics},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2308.16137}\n}\n\n@article{ko2024found,\n  author  = {Ko and others},\n  title   = {{Found in the Middle: Calibrating Positional Attention Bias Improves Long Context Utilization}},\n  journal = {arXiv preprint arXiv:2406.16008},\n  year    = {2024},\n  url     = {https://arxiv.org/abs/2406.16008}\n}\n\n% ============================================================\n% Theoretical Foundations\n% ============================================================\n\n@article{elhage2021framework,\n  author  = {Elhage and others},\n  title   = {{A Mathematical Framework for Transformer Circuits}},\n  journal = {Anthropic Blog},\n  year    = {2021},\n  url     = {https://transformer-circuits.pub/2021/framework/index.html}\n}\n\n@article{elhage2022superposition,\n  author  = {Elhage and others},\n  title   = {{Toy Models of Superposition}},\n  journal = {arXiv preprint arXiv:2209.10652},\n  year    = {2022},\n  url     = {https://arxiv.org/abs/2209.10652}\n}\n\n@article{belrose2023tuned,\n  author  = {Belrose and others},\n  title   = {{Eliciting Latent Predictions from Transformers with the Tuned Lens}},\n  journal = {arXiv preprint arXiv:2303.08112},\n  year    = {2023},\n  url     = {https://arxiv.org/abs/2303.08112}\n}\n\n@article{yu2023residual,\n  author  = {Yu and others},\n  title   = {{Exploring the Residual Stream of Transformers}},\n  journal = {arXiv preprint arXiv:2312.12141},\n  year    = {2023},\n  url     = {https://arxiv.org/abs/2312.12141}\n}\n\n@inproceedings{makkuva2025markov,\n  author    = {Makkuva and others},\n  title     = {{Attention with Markov: A Framework for Principled Analysis of Transformers via Markov Chains}},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2025},\n  url       = {https://arxiv.org/abs/2402.04161}\n}\n\n@inproceedings{ildiz2024markov,\n  author    = {Ildiz and others},\n  title     = {{From Self-Attention to Markov Models: Unveiling the Dynamics of Generative Transformers}},\n  booktitle = {International Conference on Machine Learning},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2402.13512}\n}\n\n% ============================================================\n% Evaluation Benchmarks\n% ============================================================\n\n@inproceedings{zheng2023mtbench,\n  author    = {Zheng and others},\n  title     = {{Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena}},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2023},\n  url       = {https://arxiv.org/abs/2306.05685}\n}\n\n@inproceedings{chiang2024arena,\n  author    = {Chiang and others},\n  title     = {{Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference}},\n  booktitle = {International Conference on Machine Learning},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2403.04132}\n}\n\n@inproceedings{dubois2024alpacaeval,\n  author    = {Dubois and others},\n  title     = {{Length-Controlled AlpacaEval: A Simple Way to Debias Automatic Evaluators}},\n  booktitle = {Conference on Language Modeling},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2404.04475}\n}\n\n@article{lin2024wildbench,\n  author  = {Lin and others},\n  title   = {{WildBench: Benchmarking LLMs with Challenging Tasks from Real Users in the Wild}},\n  journal = {arXiv preprint arXiv:2406.04770},\n  year    = {2024},\n  url     = {https://arxiv.org/abs/2406.04770}\n}\n\n@inproceedings{bai2024mtbench101,\n  author    = {Bai and others},\n  title     = {{MT-Bench-101: A Fine-Grained Benchmark for Evaluating Large Language Models in Multi-Turn Dialogues}},\n  booktitle = {Annual Meeting of the Association for Computational Linguistics},\n  year      = {2024},\n  url       = {https://arxiv.org/abs/2402.14762}\n}\n\n@article{sirdeshmukh2025multichallenge,\n  author  = {Sirdeshmukh and others},\n  title   = {{MultiChallenge: A Realistic Multi-Turn Conversation Evaluation Benchmark Challenging to Frontier LLMs}},\n  journal = {arXiv preprint arXiv:2501.17399},\n  year    = {2025},\n  url     = {https://arxiv.org/abs/2501.17399}\n}\n\n% ============================================================\n% Exposure Bias\n% ============================================================\n\n@inproceedings{bengio2015scheduled,\n  author    = {Bengio and Vinyals and Jaitly and Shazeer},\n  title     = {{Scheduled Sampling for Sequence Prediction with Recurrent Neural Networks}},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2015},\n  url       = {https://arxiv.org/abs/1506.03099}\n}\n\n@inproceedings{ranzato2016sequence,\n  author    = {Ranzato and Chopra and Auli and Zaremba},\n  title     = {{Sequence Level Training with Recurrent Neural Networks}},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2016},\n  url       = {https://arxiv.org/abs/1511.06732}\n}\n\n@inproceedings{lamb2016professor,\n  author    = {Lamb and Goyal and Zhang and Zhang and Courville and Bengio},\n  title     = {{Professor Forcing: A New Algorithm for Training Recurrent Networks}},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2016},\n  url       = {https://arxiv.org/abs/1610.09038}\n}\n\n@inproceedings{leblond2018searnn,\n  author    = {Leblond and Alayrac and Osokin and Lacoste-Julien},\n  title     = {{SEARNN: Training RNNs with Global-Local Losses}},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2018},\n  url       = {https://arxiv.org/abs/1706.04499}\n}\n\n@article{he2019exposure,\n  author  = {He and Zhang and Zhou and Glass},\n  title   = {{Quantifying Exposure Bias for Neural Language Generation}},\n  journal = {arXiv preprint arXiv:1905.10617},\n  year    = {2019},\n  url     = {https://arxiv.org/abs/1905.10617}\n}\n\n% ============================================================\n% Gradient Conflict / Multi-Task Learning\n% ============================================================\n\n@inproceedings{yu2020pcgrad,\n  author    = {Yu and Kumar and Gupta and Levine and Hausman and Finn},\n  title     = {{Gradient Surgery for Multi-Task Learning}},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2020},\n  url       = {https://arxiv.org/abs/2001.06782}\n}\n\n@inproceedings{chen2018gradnorm,\n  author    = {Chen and Badrinarayanan and Lee and Rabinovich},\n  title     = {{GradNorm: Gradient Normalization for Adaptive Loss Balancing in Deep Multitask Networks}},\n  booktitle = {International Conference on Machine Learning},\n  year      = {2018},\n  url       = {https://arxiv.org/abs/1711.02257}\n}\n\n@inproceedings{liu2021cagrad,\n  author    = {Liu and Liu and Jin and Stone and Liu},\n  title     = {{Conflict-Averse Gradient Descent for Multi-task Learning}},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year      = {2021},\n  url       = {https://arxiv.org/abs/2110.14048}\n}\n\n@inproceedings{navon2022nash,\n  author    = {Navon and Shamsian and Achituve and Maron and Kawaguchi and Chechik and Fetaya},\n  title     = {{Multi-Task Learning as a Bargaining Game}},\n  booktitle = {International Conference on Machine Learning},\n  year      = {2022},\n  url       = {https://arxiv.org/abs/2202.01017}\n}\n\n% ============================================================\n% Residual Scaling\n% ============================================================\n\n@inproceedings{bachlechner2021rezero,\n  author    = {Bachlechner and Majumder and Mao and Cottrell and McAuley},\n  title     = {{ReZero is All You Need: Fast Convergence at Large Depth}},\n  booktitle = {Uncertainty in Artificial Intelligence},\n  year      = {2021},\n  url       = {https://arxiv.org/abs/2003.04887}\n}\n\n@inproceedings{zhang2019fixup,\n  author    = {Zhang and Dauphin and Ma},\n  title     = {{Fixup Initialization: Residual Learning Without Normalization}},\n  booktitle = {International Conference on Learning Representations},\n  year      = {2019},\n  url       = {https://arxiv.org/abs/1901.09321}\n}\n\n@article{grattafiori2024llama3,\n  author  = {Grattafiori and 1 others},\n  title   = {{The Llama 3 Herd of Models}},\n  journal = {arXiv preprint arXiv:2407.21783},\n  year    = {2024}\n}\n",
      "numLines": 403,
      "startLine": 1,
      "totalLines": 403
    }
  }
}
```

</details>

---

### Assistant

_source line 10_

<details><summary>Logged reasoning block</summary>

```text
Now I need to:
1. Use `verify_references` tool to do automated checking
2. Search all .tex files for \cite{} references
3. Do WebSearch verification for each bib entry

Let me first get the tex files to find all citations, and also call verify_references.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "652e1b48-5425-4360-9d09-b4c254656213",
  "uuid": "5d29e26c-c190-4af5-8a1d-af6e3d77c74d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GdRod7yc5wyz5y5RaURyCB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7874,
      "cache_read_input_tokens": 24643,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7874
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

_source line 11_

先用 `verify_references` 工具做自动检查，同时搜索 tex 文件中的所有引用。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "652e1b48-5425-4360-9d09-b4c254656213",
  "uuid": "785133a2-2063-419e-a40a-d5fb729dadc6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GdRod7yc5wyz5y5RaURyCB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7874,
      "cache_read_input_tokens": 24643,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7874
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

_source line 12_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Hw5PC5Xj7biejLJRvhcTno`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__verify_references",
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
  "session_id": "652e1b48-5425-4360-9d09-b4c254656213",
  "uuid": "ff0d1b74-3fe6-4fd5-b1db-c93509984044",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GdRod7yc5wyz5y5RaURyCB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7874,
      "cache_read_input_tokens": 24643,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7874
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

_source line 13 · 2026-05-22T04:30:16.100Z_

<details><summary>↩ Tool result · `toolu_01Hw5PC5Xj7biejLJRvhcTno`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__verify_references"
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
  "session_id": "652e1b48-5425-4360-9d09-b4c254656213",
  "uuid": "ff5fc1c3-c5d3-4ac0-aa87-2081c597d608",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__verify_references"
    ],
    "query": "select:mcp__agent-ml-research__verify_references",
    "total_deferred_tools": 23
  }
}
```

</details>

---

### Tool call

_source line 14_

<details open><summary>🔧 Tool call — Grep · `toolu_01Vk87HJWWqdtEr2RBz7VpGH`</summary>

```json
{
  "pattern": "\\\\cite[pt]?\\{[^}]+\\}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper",
  "output_mode": "content",
  "glob": "*.tex",
  "head_limit": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "652e1b48-5425-4360-9d09-b4c254656213",
  "uuid": "c827a636-8524-4413-aca6-e78323c814dd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GdRod7yc5wyz5y5RaURyCB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7874,
      "cache_read_input_tokens": 24643,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7874
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

_source line 15 · 2026-05-22T04:30:18.394Z_

<details><summary>↩ Tool result · `toolu_01Vk87HJWWqdtEr2RBz7VpGH`</summary>

```text
paper/sections/analysis.tex:22:[Omitted long matching line]
paper/sections/analysis.tex:39:[Omitted long matching line]
paper/sections/analysis.tex:53:[Omitted long matching line]
paper/sections/related_work.tex:4:[Omitted long matching line]
paper/sections/related_work.tex:7:ReZero \citep{bachlechner2021rezero} showed that residual scaling shapes optimization dynamics. Subsequent work targets computational efficiency: LayerDrop \citep{fan2020layerdrop}, Mixture-of-Depths \citep{raposo2024mixture}, FlexiDepth \citep{luo2025flexidepth}, and CALM \citep{schuster2022calm}. ThreadGate applies residual gating to a different objective: recovering attention patterns in multi-turn dialogue.
paper/sections/related_work.tex:10:[Omitted long matching line]
paper/sections/related_work.tex:13:GradNorm \citep{chen2018gradnorm}, PCGrad \citep{yu2020pcgrad}, CAGrad \citep{liu2021cagrad}, and Nash-MTL \citep{navon2022nash} treat gradient conflict between competing losses as a root cause to be resolved through better optimization. We repurpose PCGrad as a causal analysis tool: eliminating directional conflict between NTP and GAR gradients does not improve GAR convergence. Gradient conflict is a symptom rather than the cause.
paper/sections/related_work.tex:16:[Omitted long matching line]
paper/sections/experiments.tex:8:[Omitted long matching line]
paper/sections/experiments.tex:14:[Omitted long matching line]
paper/sections/experiments.tex:21:\caption{Five-way comparison on Qwen-2.5-7B-Instruct. IID evaluation uses teacher-forced UltraChat text; held-out uses 50 non-overlapping conversations. All four fine-tuned variants converge to within 0.75\,pp on GAR-ours; PPL is indistinguishable. GAR-O = GAR-ours; GAR-D = GAR-Dongre \citep{dongre2026attention}.}
paper/sections/discussion.tex:5:[Omitted long matching line]
paper/sections/discussion.tex:9:TRC analysis (\S\ref{subsec:mechanism-specificity}) confirms the mismatch targets attention routing without disrupting hidden-state coherence. We scope claims to GAR losses on Qwen-2.5-7B and Llama-3.1-8B; magnitude imbalance \citep{chen2018gradnorm} and Nash equilibria \citep{navon2022nash} remain untested. Remaining directions include adaptive $\beta$ scheduling and layer-selective steering.
paper/sections/method.tex:6:We denote the task specification tokens in the system prompt as \emph{goal tokens} $\mathcal{G}$. \citet{dongre2026attention} defined the Goal Attention Ratio (GAR) for a model with $L$ layers and $H$ heads at turn $\tau$ as
paper/sections/method.tex:21:Inspired by the residual scaling idea of ReZero \citep{bachlechner2021rezero}, ThreadGate modulates the residual stream with a content-and-turn-conditioned gate at each transformer layer. The gated residual update at layer $l$ is
paper/sections/background.tex:4:[Omitted long matching line]
paper/sections/background.tex:18:\citet{dongre2026attention} showed that goal-relevant information persists in the residual stream (probe AUC\,=\,0.98) even at late turns where GAR has collapsed. The information is present but the attention mechanism fails to route it. This dissociation motivates an intervention that targets the residual pathway directly.
paper/sections/introduction.tex:3:[Omitted long matching line]
paper/sections/introduction.tex:5:[Omitted long matching line]
paper/sections/introduction.tex:14:[Omitted long matching line]
paper/sections/introduction.tex:16:[Omitted long matching line]
paper/sections/introduction.tex:18:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "652e1b48-5425-4360-9d09-b4c254656213",
  "uuid": "bb4c0409-4950-4196-9ae2-ea04b64085b7",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "paper/sections/analysis.tex:22:[Omitted long matching line]\npaper/sections/analysis.tex:39:[Omitted long matching line]\npaper/sections/analysis.tex:53:[Omitted long matching line]\npaper/sections/related_work.tex:4:[Omitted long matching line]\npaper/sections/related_work.tex:7:ReZero \\citep{bachlechner2021rezero} showed that residual scaling shapes optimization dynamics. Subsequent work targets computational efficiency: LayerDrop \\citep{fan2020layerdrop}, Mixture-of-Depths \\citep{raposo2024mixture}, FlexiDepth \\citep{luo2025flexidepth}, and CALM \\citep{schuster2022calm}. ThreadGate applies residual gating to a different objective: recovering attention patterns in multi-turn dialogue.\npaper/sections/related_work.tex:10:[Omitted long matching line]\npaper/sections/related_work.tex:13:GradNorm \\citep{chen2018gradnorm}, PCGrad \\citep{yu2020pcgrad}, CAGrad \\citep{liu2021cagrad}, and Nash-MTL \\citep{navon2022nash} treat gradient conflict between competing losses as a root cause to be resolved through better optimization. We repurpose PCGrad as a causal analysis tool: eliminating directional conflict between NTP and GAR gradients does not improve GAR convergence. Gradient conflict is a symptom rather than the cause.\npaper/sections/related_work.tex:16:[Omitted long matching line]\npaper/sections/experiments.tex:8:[Omitted long matching line]\npaper/sections/experiments.tex:14:[Omitted long matching line]\npaper/sections/experiments.tex:21:\\caption{Five-way comparison on Qwen-2.5-7B-Instruct. IID evaluation uses teacher-forced UltraChat text; held-out uses 50 non-overlapping conversations. All four fine-tuned variants converge to within 0.75\\,pp on GAR-ours; PPL is indistinguishable. GAR-O = GAR-ours; GAR-D = GAR-Dongre \\citep{dongre2026attention}.}\npaper/sections/discussion.tex:5:[Omitted long matching line]\npaper/sections/discussion.tex:9:TRC analysis (\\S\\ref{subsec:mechanism-specificity}) confirms the mismatch targets attention routing without disrupting hidden-state coherence. We scope claims to GAR losses on Qwen-2.5-7B and Llama-3.1-8B; magnitude imbalance \\citep{chen2018gradnorm} and Nash equilibria \\citep{navon2022nash} remain untested. Remaining directions include adaptive $\\beta$ scheduling and layer-selective steering.\npaper/sections/method.tex:6:We denote the task specification tokens in the system prompt as \\emph{goal tokens} $\\mathcal{G}$. \\citet{dongre2026attention} defined the Goal Attention Ratio (GAR) for a model with $L$ layers and $H$ heads at turn $\\tau$ as\npaper/sections/method.tex:21:Inspired by the residual scaling idea of ReZero \\citep{bachlechner2021rezero}, ThreadGate modulates the residual stream with a content-and-turn-conditioned gate at each transformer layer. The gated residual update at layer $l$ is\npaper/sections/background.tex:4:[Omitted long matching line]\npaper/sections/background.tex:18:\\citet{dongre2026attention} showed that goal-relevant information persists in the residual stream (probe AUC\\,=\\,0.98) even at late turns where GAR has collapsed. The information is present but the attention mechanism fails to route it. This dissociation motivates an intervention that targets the residual pathway directly.\npaper/sections/introduction.tex:3:[Omitted long matching line]\npaper/sections/introduction.tex:5:[Omitted long matching line]\npaper/sections/introduction.tex:14:[Omitted long matching line]\npaper/sections/introduction.tex:16:[Omitted long matching line]\npaper/sections/introduction.tex:18:[Omitted long matching line]",
    "numLines": 22
  }
}
```

</details>

---

### Tool call

_source line 16_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references · `toolu_01NapQCPF4aWAsNfowLjmamL`</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "652e1b48-5425-4360-9d09-b4c254656213",
  "uuid": "07bcd7bb-66ab-4391-8029-127ced863e93",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015XG6bAp4m7a72YEctX1qN7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1767,
      "cache_read_input_tokens": 32517,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1767
      },
      "output_tokens": 41,
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

_source line 17 · 2026-05-22T04:36:38.077Z_

<details><summary>↩ Tool result · `toolu_01NapQCPF4aWAsNfowLjmamL`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 91, \"total_citations\": 46, \"unique_cited_keys\": 22, \"orphan_bib\": 24, \"missing_bib\": 0, \"duplicate_keys\": 45, \"online_verified\": 33, \"online_not_found\": 3, \"online_mismatch\": 10, \"online_error\": 0, \"online_checked\": 46, \"online_total\": 46, \"online_verified_by_doi\": 0, \"online_verified_by_arxiv\": 20, \"online_verified_by_search\": 13}, \"cross_check\": {\"orphan_bib\": [\"anonymous2024reassessing\", \"anonymous2025style\", \"belrose2023tuned\", \"chen2023positional\", \"chiang2024arena\", \"dubois2024alpacaeval\", \"elhage2021framework\", \"elhage2022superposition\", \"gromov2024deeper\", \"han2024lminfinite\", \"ildiz2024markov\", \"lawson2025skip\", \"lin2024wildbench\", \"liu2023lost\", \"makkuva2025markov\", \"men2024shortgpt\", \"peng2024yarn\", \"press2022alibi\", \"sirdeshmukh2025multichallenge\", \"sun2025curse\", \"wang2018skipnet\", \"yu2023residual\", \"zhang2019fixup\", \"zheng2023mtbench\"], \"missing_bib\": [], \"orphan_count\": 24, \"missing_count\": 0}, \"bib_problems\": [{\"key\": \"gromov2024deeper\", \"type\": \"inproceedings\", \"title\": \"The Unreasonable Ineffectiveness of the Deeper Layers\", \"authors\": \"Gromov and others\", \"year\": \"2024\", \"issue\": \"orphan\"}, {\"key\": \"men2024shortgpt\", \"type\": \"article\", \"title\": \"ShortGPT: Layers in Large Language Models are More Redundant Than You Expect\", \"authors\": \"Men and others\", \"year\": \"2024\", \"issue\": \"orphan\"}, {\"key\": \"sun2025curse\", \"type\": \"inproceedings\", \"title\": \"The Curse of Depth in Large Language Models\", \"authors\": \"Sun and others\", \"year\": \"2025\", \"issue\": \"orphan\"}, {\"key\": \"anonymous2024reassessing\", \"type\": \"article\", \"title\": \"Reassessing Layer Pruning in LLMs: New Insights and Methods\", \"authors\": \"Anonymous\", \"year\": \"2024\", \"issue\": \"orphan\"}, {\"key\": \"fan2020layerdrop\", \"type\": \"inproceedings\", \"title\": \"Reducing Transformer Depth on Demand with Structured Dropout (LayerDrop)\", \"authors\": \"Fan and others\", \"year\": \"2020\", \"issue\": \"duplicate\"}, {\"key\": \"dongre2026attention\", \"type\": \"article\", \"title\": \"When Attention Closes: How LLMs Lose the Thread in Multi-Turn Interaction\", \"authors\": \"Dongre and Hsieh and Lai and Yoon and Bui and Hakkani-Tur\", \"year\": \"2026\", \"issue\": \"duplicate\"}, {\"key\": \"levy2025lost\", \"type\": \"article\", \"title\": \"LLMs Get Lost In Multi-Turn Conversation\", \"authors\": \"Levy and others\", \"year\": \"2025\", \"issue\": \"duplicate\"}, {\"key\": \"liu2026intent\", \"type\": \"article\", \"title\": \"Intent Mismatch Causes LLMs to Get Lost in Multi-Turn Conversation\", \"authors\": \"Liu and others\", \"year\": \"2026\", \"issue\": \"duplicate\"}, {\"key\": \"liu2023lost\", \"type\": \"article\", \"title\": \"Lost in the Middle: How Language Models Use Long Contexts\", \"authors\": \"Liu and others\", \"year\": \"2023\", \"issue\": \"orphan\"}, {\"key\": \"anonymous2025style\", \"type\": \"article\", \"title\": \"Style Amnesia: Investigating Speaking Style Degradation and Mitigation in Multi-Turn Spoken Language Models\", \"authors\": \"Anonymous\", \"year\": \"2025\", \"issue\": \"orphan\"}, {\"key\": \"raposo2024mixture\", \"type\": \"article\", \"title\": \"Mixture-of-Depths: Dynamically Allocating Compute in Transformer-Based Language Models\", \"authors\": \"Raposo and others\", \"year\": \"2024\", \"issue\": \"duplicate\"}, {\"key\": \"schuster2022calm\", \"type\": \"inproceedings\", \"title\": \"Confident Adaptive Language Modeling\", \"authors\": \"Schuster and others\", \"year\": \"2022\", \"issue\": \"duplicate\"}, {\"key\": \"qiu2025gated\", \"type\": \"inproceedings\", \"title\": \"Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free\", \"authors\": \"Qiu and others\", \"year\": \"2025\", \"issue\": \"duplicate\"}, {\"key\": \"wang2018skipnet\", \"type\": \"inproceedings\", \"title\": \"SkipNet: Learning Dynamic Routing in Convolutional Networks\", \"authors\": \"Wang and others\", \"year\": \"2018\", \"issue\": \"orphan\"}, {\"key\": \"luo2025flexidepth\", \"type\": \"article\", \"title\": \"Adaptive Layer-skipping in Pre-trained LLMs (FlexiDepth)\", \"authors\": \"Luo and others\", \"year\": \"2025\", \"issue\": \"duplicate\"}, {\"key\": \"lawson2025skip\", \"type\": \"article\", \"title\": \"Learning to Skip the Middle Layers of Transformers\", \"authors\": \"Lawson and others\", \"year\": \"2025\", \"issue\": \"orphan\"}, {\"key\": \"press2022alibi\", \"type\": \"inproceedings\", \"title\": \"Train Short, Test Long: Attention with Linear Biases Enables Input Length Extrapolation\", \"authors\": \"Press and others\", \"year\": \"2022\", \"issue\": \"orphan\"}, {\"key\": \"chen2023positional\", \"type\": \"article\", \"title\": \"Extending Context Window of Large Language Models via Positional Interpolation\", \"authors\": \"Chen and others\", \"year\": \"2023\", \"issue\": \"orphan\"}, {\"key\": \"peng2024yarn\", \"type\": \"inproceedings\", \"title\": \"YaRN: Efficient Context Window Extension of Large Language Models\", \"authors\": \"Peng and others\", \"year\": \"2024\", \"issue\": \"orphan\"}, {\"key\": \"xiao2024streaming\", \"type\": \"inproceedings\", \"title\": \"Efficient Streaming Language Models with Attention Sinks\", \"authors\": \"Xiao and others\", \"year\": \"2024\", \"issue\": \"duplicate\"}, {\"key\": \"han2024lminfinite\", \"type\": \"inproceedings\", \"title\": \"LM-Infinite: Zero-Shot Extreme Length Generalization for Large Language Models\", \"authors\": \"Han and others\", \"year\": \"2024\", \"issue\": \"orphan\"}, {\"key\": \"ko2024found\", \"type\": \"article\", \"title\": \"Found in the Middle: Calibrating Positional Attention Bias Improves Long Context Utilization\", \"authors\": \"Ko and others\", \"year\": \"2024\", \"issue\": \"duplicate\"}, {\"key\": \"elhage2021framework\", \"type\": \"article\", \"title\": \"A Mathematical Framework for Transformer Circuits\", \"authors\": \"Elhage and others\", \"year\": \"2021\", \"issue\": \"orphan\"}, {\"key\": \"elhage2022superposition\", \"type\": \"article\", \"title\": \"Toy Models of Superposition\", \"authors\": \"Elhage and others\", \"year\": \"2022\", \"issue\": \"orphan\"}, {\"key\": \"belrose2023tuned\", \"type\": \"article\", \"title\": \"Eliciting Latent Predictions from Transformers with the Tuned Lens\", \"authors\": \"Belrose and others\", \"year\": \"2023\", \"issue\": \"orphan\"}, {\"key\": \"yu2023residual\", \"type\": \"article\", \"title\": \"Exploring the Residual Stream of Transformers\", \"authors\": \"Yu and others\", \"year\": \"2023\", \"issue\": \"orphan\"}, {\"key\": \"makkuva2025markov\", \"type\": \"inproceedings\", \"title\": \"Attention with Markov: A Framework for Principled Analysis of Transformers via Markov Chains\", \"authors\": \"Makkuva and others\", \"year\": \"2025\", \"issue\": \"orphan\"}, {\"key\": \"ildiz2024markov\", \"type\": \"inproceedings\", \"title\": \"From Self-Attention to Markov Models: Unveiling the Dynamics of Generative Transformers\", \"authors\": \"Ildiz and others\", \"year\": \"2024\", \"issue\": \"orphan\"}, {\"key\": \"zheng2023mtbench\", \"type\": \"inproceedings\", \"title\": \"Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena\", \"authors\": \"Zheng and others\", \"year\": \"2023\", \"issue\": \"orphan\"}, {\"key\": \"chiang2024arena\", \"type\": \"inproceedings\", \"title\": \"Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference\", \"authors\": \"Chiang and others\", \"year\": \"2024\", \"issue\": \"orphan\"}, {\"key\": \"dubois2024alpacaeval\", \"type\": \"inproceedings\", \"title\": \"Length-Controlled AlpacaEval: A Simple Way to Debias Automatic Evaluators\", \"authors\": \"Dubois and others\", \"year\": \"2024\", \"issue\": \"orphan\"}, {\"key\": \"lin2024wildbench\", \"type\": \"article\", \"title\": \"WildBench: Benchmarking LLMs with Challenging Tasks from Real Users in the Wild\", \"authors\": \"Lin and others\", \"year\": \"2024\", \"issue\": \"orphan\"}, {\"key\": \"bai2024mtbench101\", \"type\": \"inproceedings\", \"title\": \"MT-Bench-101: A Fine-Grained Benchmark for Evaluating Large Language Models in Multi-Turn Dialogues\", \"authors\": \"Bai and others\", \"year\": \"2024\", \"issue\": \"duplicate\"}, {\"key\": \"sirdeshmukh2025multichallenge\", \"type\": \"article\", \"title\": \"MultiChallenge: A Realistic Multi-Turn Conversation Evaluation Benchmark Challenging to Frontier LLMs\", \"authors\": \"Sirdeshmukh and others\", \"year\": \"2025\", \"issue\": \"orphan\"}, {\"key\": \"bengio2015scheduled\", \"type\": \"inproceedings\", \"title\": \"Scheduled Sampling for Sequence Prediction with Recurrent Neural Networks\", \"authors\": \"Bengio and Vinyals and Jaitly and Shazeer\", \"year\": \"2015\", \"issue\": \"duplicate\"}, {\"key\": \"ranzato2016sequence\", \"type\": \"inproceedings\", \"title\": \"Sequence Level Training with Recurrent Neural Networks\", \"authors\": \"Ranzato and Chopra and Auli and Zaremba\", \"year\": \"2016\", \"issue\": \"duplicate\"}, {\"key\": \"lamb2016professor\", \"type\": \"inproceedings\", \"title\": \"Professor Forcing: A New Algorithm for Training Recurrent Networks\", \"authors\": \"Lamb and Goyal and Zhang and Zhang and Courville and Bengio\", \"year\": \"2016\", \"issue\": \"duplicate\"}, {\"key\": \"leblond2018searnn\", \"type\": \"inproceedings\", \"title\": \"SEARNN: Training RNNs with Global-Local Losses\", \"authors\": \"Leblond and Alayrac and Osokin and Lacoste-Julien\", \"year\": \"2018\", \"issue\": \"duplicate\"}, {\"key\": \"he2019exposure\", \"type\": \"article\", \"title\": \"Quantifying Exposure Bias for Neural Language Generation\", \"authors\": \"He and Zhang and Zhou and Glass\", \"year\": \"2019\", \"issue\": \"duplicate\"}, {\"key\": \"yu2020pcgrad\", \"type\": \"inproceedings\", \"title\": \"Gradient Surgery for Multi-Task Learning\", \"authors\": \"Yu and Kumar and Gupta and Levine and Hausman and Finn\", \"year\": \"2020\", \"issue\": \"duplicate\"}, {\"key\": \"chen2018gradnorm\", \"type\": \"inproceedings\", \"title\": \"GradNorm: Gradient Normalization for Adaptive Loss Balancing in Deep Multitask Networks\", \"authors\": \"Chen and Badrinarayanan and Lee and Rabinovich\", \"year\": \"2018\", \"issue\": \"duplicate\"}, {\"key\": \"liu2021cagrad\", \"type\": \"inproceedings\", \"title\": \"Conflict-Averse Gradient Descent for Multi-task Learning\", \"authors\": \"Liu and Liu and Jin and Stone and Liu\", \"year\": \"2021\", \"issue\": \"duplicate\"}, {\"key\": \"navon2022nash\", \"type\": \"inproceedings\", \"title\": \"Multi-Task Learning as a Bargaining Game\", \"authors\": \"Navon and Shamsian and Achituve and Maron and Kawaguchi and Chechik and Fetaya\", \"year\": \"2022\", \"issue\": \"duplicate\"}, {\"key\": \"bachlechner2021rezero\", \"type\": \"inproceedings\", \"title\": \"ReZero is All You Need: Fast Convergence at Large Depth\", \"authors\": \"Bachlechner and Majumder and Mao and Cottrell and McAuley\", \"year\": \"2021\", \"issue\": \"duplicate\"}, {\"key\": \"zhang2019fixup\", \"type\": \"inproceedings\", \"title\": \"Fixup Initialization: Residual Learning Without Normalization\", \"authors\": \"Zhang and Dauphin and Ma\", \"year\": \"2019\", \"issue\": \"orphan\"}, {\"key\": \"gromov2024deeper\", \"type\": \"inproceedings\", \"title\": \"The Unreasonable Ineffectiveness of the Deeper Layers\", \"authors\": \"Gromov and others\", \"year\": \"2024\", \"issue\": \"orphan\"}, {\"key\": \"men2024shortgpt\", \"type\": \"article\", \"title\": \"ShortGPT: Layers in Large Language Models are More Redundant Than You Expect\", \"authors\": \"Men and others\", \"year\": \"2024\", \"issue\": \"orphan\"}, {\"key\": \"sun2025curse\", \"type\": \"inproceedings\", \"title\": \"The Curse of Depth in Large Language Models\", \"authors\": \"Sun and others\", \"year\": \"2025\", \"issue\": \"orphan\"}, {\"key\": \"anonymous2024reassessing\", \"type\": \"article\", \"title\": \"Reassessing Layer Pruning in LLMs: New Insights and Methods\", \"authors\": \"Anonymous\", \"year\": \"2024\", \"issue\": \"orphan\"}, {\"key\": \"fan2020layerdrop\", \"type\": \"inproceedings\", \"title\": \"Reducing Transformer Depth on Demand with Structured Dropout (LayerDrop)\", \"authors\": \"Fan and others\", \"year\": \"2020\", \"issue\": \"duplicate\"}, {\"key\": \"dongre2026attention\", \"type\": \"article\", \"title\": \"When Attention Closes: How LLMs Lose the Thread in Multi-Turn Interaction\", \"authors\": \"Dongre and Hsieh and Lai and Yoon and Bui and Hakkani-Tur\", \"year\": \"2026\", \"issue\": \"duplicate\"}, {\"key\": \"levy2025lost\", \"type\": \"article\", \"title\": \"LLMs Get Lost In Multi-Turn Conversation\", \"authors\": \"Levy and others\", \"year\": \"2025\", \"issue\": \"duplicate\"}, {\"key\": \"liu2026intent\", \"type\": \"article\", \"title\": \"Intent Mismatch Causes LLMs to Get Lost in Multi-Turn Conversation\", \"authors\": \"Liu and others\", \"year\": \"2026\", \"issue\": \"duplicate\"}, {\"key\": \"liu2023lost\", \"type\": \"article\", \"title\": \"Lost in the Middle: How Language Models Use Long Contexts\", \"authors\": \"Liu and others\", \"year\": \"2023\", \"issue\": \"orphan\"}, {\"key\": \"anonymous2025style\", \"type\": \"article\", \"title\": \"Style Amnesia: Investigating Speaking Style Degradation and Mitigation in Multi-Turn Spoken Language Models\", \"authors\": \"Anonymous\", \"year\": \"2025\", \"issue\": \"orphan\"}, {\"key\": \"raposo2024mixture\", \"type\": \"article\", \"title\": \"Mixture-of-Depths: Dynamically Allocating Compute in Transformer-Based Language Models\", \"authors\": \"Raposo and others\", \"year\": \"2024\", \"issue\": \"duplicate\"}, {\"key\": \"schuster2022calm\", \"type\": \"inproceedings\", \"title\": \"Confident Adaptive Language Modeling\", \"authors\": \"Schuster and others\", \"year\": \"2022\", \"issue\": \"duplicate\"}, {\"key\": \"qiu2025gated\", \"type\": \"inproceedings\", \"title\": \"Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free\", \"authors\": \"Qiu and others\", \"year\": \"2025\", \"issue\": \"duplicate\"}, {\"key\": \"wang2018skipnet\", \"type\": \"inproceedings\", \"title\": \"SkipNet: Learning Dynamic Routing in Convolutional Networks\", \"authors\": \"Wang and others\", \"year\": \"2018\", \"issue\": \"orphan\"}, {\"key\": \"luo2025flexidepth\", \"type\": \"article\", \"title\": \"Adaptive Layer-skipping in Pre-trained LLMs (FlexiDepth)\", \"authors\": \"Luo and others\", \"year\": \"2025\", \"issue\": \"duplicate\"}, {\"key\": \"lawson2025skip\", \"type\": \"article\", \"title\": \"Learning to Skip the Middle Layers of Transformers\", \"authors\": \"Lawson and others\", \"year\": \"2025\", \"issue\": \"orphan\"}, {\"key\": \"press2022alibi\", \"type\": \"inproceedings\", \"title\": \"Train Short, Test Long: Attention with Linear Biases Enables Input Length Extrapolation\", \"authors\": \"Press and others\", \"year\": \"2022\", \"issue\": \"orphan\"}, {\"key\": \"chen2023positional\", \"type\": \"article\", \"title\": \"Extending Context Window of Large Language Models via Positional Interpolation\", \"authors\": \"Chen and others\", \"year\": \"2023\", \"issue\": \"orphan\"}, {\"key\": \"peng2024yarn\", \"type\": \"inproceedings\", \"title\": \"YaRN: Efficient Context Window Extension of Large Language Models\", \"authors\": \"Peng and others\", \"year\": \"2024\", \"issue\": \"orphan\"}, {\"key\": \"xiao2024streaming\", \"type\": \"inproceedings\", \"title\": \"Efficient Streaming Language Models with Attention Sinks\", \"authors\": \"Xiao and others\", \"year\": \"2024\", \"issue\": \"duplicate\"}, {\"key\": \"han2024lminfinite\", \"type\": \"inproceedings\", \"title\": \"LM-Infinite: Zero-Shot Extreme Length Generalization for Large Language Models\", \"authors\": \"Han and others\", \"year\": \"2024\", \"issue\": \"orphan\"}, {\"key\": \"ko2024found\", \"type\": \"article\", \"title\": \"Found in the Middle: Calibrating Positional Attention Bias Improves Long Context Utilization\", \"authors\": \"Ko and others\", \"year\": \"2024\", \"issue\": \"duplicate\"}, {\"key\": \"elhage2021framework\", \"type\": \"article\", \"title\": \"A Mathematical Framework for Transformer Circuits\", \"authors\": \"Elhage and others\", \"year\": \"2021\", \"issue\": \"orphan\"}, {\"key\": \"elhage2022superposition\", \"type\": \"article\", \"title\": \"Toy Models of Superposition\", \"authors\": \"Elhage and others\", \"year\": \"2022\", \"issue\": \"orphan\"}, {\"key\": \"belrose2023tuned\", \"type\": \"article\", \"title\": \"Eliciting Latent Predictions from Transformers with the Tuned Lens\", \"authors\": \"Belrose and others\", \"year\": \"2023\", \"issue\": \"orphan\"}, {\"key\": \"yu2023residual\", \"type\": \"article\", \"title\": \"Exploring the Residual Stream of Transformers\", \"authors\": \"Yu and others\", \"year\": \"2023\", \"issue\": \"orphan\"}, {\"key\": \"makkuva2025markov\", \"type\": \"inproceedings\", \"title\": \"Attention with Markov: A Framework for Principled Analysis of Transformers via Markov Chains\", \"authors\": \"Makkuva and others\", \"year\": \"2025\", \"issue\": \"orphan\"}, {\"key\": \"ildiz2024markov\", \"type\": \"inproceedings\", \"title\": \"From Self-Attention to Markov Models: Unveiling the Dynamics of Generative Transformers\", \"authors\": \"Ildiz and others\", \"year\": \"2024\", \"issue\": \"orphan\"}, {\"key\": \"zheng2023mtbench\", \"type\": \"inproceedings\", \"title\": \"Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena\", \"authors\": \"Zheng and others\", \"year\": \"2023\", \"issue\": \"orphan\"}, {\"key\": \"chiang2024arena\", \"type\": \"inproceedings\", \"title\": \"Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference\", \"authors\": \"Chiang and others\", \"year\": \"2024\", \"issue\": \"orphan\"}, {\"key\": \"dubois2024alpacaeval\", \"type\": \"inproceedings\", \"title\": \"Length-Controlled AlpacaEval: A Simple Way to Debias Automatic Evaluators\", \"authors\": \"Dubois and others\", \"year\": \"2024\", \"issue\": \"orphan\"}, {\"key\": \"lin2024wildbench\", \"type\": \"article\", \"title\": \"WildBench: Benchmarking LLMs with Challenging Tasks from Real Users in the Wild\", \"authors\": \"Lin and others\", \"year\": \"2024\", \"issue\": \"orphan\"}, {\"key\": \"bai2024mtbench101\", \"type\": \"inproceedings\", \"title\": \"MT-Bench-101: A Fine-Grained Benchmark for Evaluating Large Language Models in Multi-Turn Dialogues\", \"authors\": \"Bai and others\", \"year\": \"2024\", \"issue\": \"duplicate\"}, {\"key\": \"sirdeshmukh2025multichallenge\", \"type\": \"article\", \"title\": \"MultiChallenge: A Realistic Multi-Turn Conversation Evaluation Benchmark Challenging to Frontier LLMs\", \"authors\": \"Sirdeshmukh and others\", \"year\": \"2025\", \"issue\": \"orphan\"}, {\"key\": \"bengio2015scheduled\", \"type\": \"inproceedings\", \"title\": \"Scheduled Sampling for Sequence Prediction with Recurrent Neural Networks\", \"authors\": \"Bengio and Vinyals and Jaitly and Shazeer\", \"year\": \"2015\", \"issue\": \"duplicate\"}, {\"key\": \"ranzato2016sequence\", \"type\": \"inproceedings\", \"title\": \"Sequence Level Training with Recurrent Neural Networks\", \"authors\": \"Ranzato and Chopra and Auli and Zaremba\", \"year\": \"2016\", \"issue\": \"duplicate\"}, {\"key\": \"lamb2016professor\", \"type\": \"inproceedings\", \"title\": \"Professor Forcing: A New Algorithm for Training Recurrent Networks\", \"authors\": \"Lamb and Goyal and Zhang and Zhang and Courville and Bengio\", \"year\": \"2016\", \"issue\": \"duplicate\"}, {\"key\": \"leblond2018searnn\", \"type\": \"inproceedings\", \"title\": \"SEARNN: Training RNNs with Global-Local Losses\", \"authors\": \"Leblond and Alayrac and Osokin and Lacoste-Julien\", \"year\": \"2018\", \"issue\": \"duplicate\"}, {\"key\": \"he2019exposure\", \"type\": \"article\", \"title\": \"Quantifying Exposure Bias for Neural Language Generation\", \"authors\": \"He and Zhang and Zhou and Glass\", \"year\": \"2019\", \"issue\": \"duplicate\"}, {\"key\": \"yu2020pcgrad\", \"type\": \"inproceedings\", \"title\": \"Gradient Surgery for Multi-Task Learning\", \"authors\": \"Yu and Kumar and Gupta and Levine and Hausman and Finn\", \"year\": \"2020\", \"issue\": \"duplicate\"}, {\"key\": \"chen2018gradnorm\", \"type\": \"inproceedings\", \"title\": \"GradNorm: Gradient Normalization for Adaptive Loss Balancing in Deep Multitask Networks\", \"authors\": \"Chen and Badrinarayanan and Lee and Rabinovich\", \"year\": \"2018\", \"issue\": \"duplicate\"}, {\"key\": \"liu2021cagrad\", \"type\": \"inproceedings\", \"title\": \"Conflict-Averse Gradient Descent for Multi-task Learning\", \"authors\": \"Liu and Liu and Jin and Stone and Liu\", \"year\": \"2021\", \"issue\": \"duplicate\"}, {\"key\": \"navon2022nash\", \"type\": \"inproceedings\", \"title\": \"Multi-Task Learning as a Bargaining Game\", \"authors\": \"Navon and Shamsian and Achituve and Maron and Kawaguchi and Chechik and Fetaya\", \"year\": \"2022\", \"issue\": \"duplicate\"}, {\"key\": \"bachlechner2021rezero\", \"type\": \"inproceedings\", \"title\": \"ReZero is All You Need: Fast Convergence at Large Depth\", \"authors\": \"Bachlechner and Majumder and Mao and Cottrell and McAuley\", \"year\": \"2021\", \"issue\": \"duplicate\"}, {\"key\": \"zhang2019fixup\", \"type\": \"inproceedings\", \"title\": \"Fixup Initialization: Residual Learning Without Normalization\", \"authors\": \"Zhang and Dauphin and Ma\", \"year\": \"2019\", \"issue\": \"orphan\"}], \"duplicate_keys\": {\"gromov2024deeper\": [\"inproceedings\", \"inproceedings\"], \"men2024shortgpt\": [\"article\", \"article\"], \"sun2025curse\": [\"inproceedings\", \"inproceedings\"], \"anonymous2024reassessing\": [\"article\", \"article\"], \"fan2020layerdrop\": [\"inproceedings\", \"inproceedings\"], \"dongre2026attention\": [\"article\", \"article\"], \"levy2025lost\": [\"article\", \"article\"], \"liu2026intent\": [\"article\", \"article\"], \"liu2023lost\": [\"article\", \"article\"], \"anonymous2025style\": [\"article\", \"article\"], \"raposo2024mixture\": [\"article\", \"article\"], \"schuster2022calm\": [\"inproceedings\", \"inproceedings\"], \"qiu2025gated\": [\"inproceedings\", \"inproceedings\"], \"wang2018skipnet\": [\"inproceedings\", \"inproceedings\"], \"luo2025flexidepth\": [\"article\", \"article\"], \"lawson2025skip\": [\"article\", \"article\"], \"press2022alibi\": [\"inproceedings\", \"inproceedings\"], \"chen2023positional\": [\"article\", \"article\"], \"peng2024yarn\": [\"inproceedings\", \"inproceedings\"], \"xiao2024streaming\": [\"inproceedings\", \"inproceedings\"], \"han2024lminfinite\": [\"inproceedings\", \"inproceedings\"], \"ko2024found\": [\"article\", \"article\"], \"elhage2021framework\": [\"article\", \"article\"], \"elhage2022superposition\": [\"article\", \"article\"], \"belrose2023tuned\": [\"article\", \"article\"], \"yu2023residual\": [\"article\", \"article\"], \"makkuva2025markov\": [\"inproceedings\", \"inproceedings\"], \"ildiz2024markov\": [\"inproceedings\", \"inproceedings\"], \"zheng2023mtbench\": [\"inproceedings\", \"inproceedings\"], \"chiang2024arena\": [\"inproceedings\", \"inproceedings\"], \"dubois2024alpacaeval\": [\"inproceedings\", \"inproceedings\"], \"lin2024wildbench\": [\"article\", \"article\"], \"bai2024mtbench101\": [\"inproceedings\", \"inproceedings\"], \"sirdeshmukh2025multichallenge\": [\"article\", \"article\"], \"bengio2015scheduled\": [\"inproceedings\", \"inproceedings\"], \"ranzato2016sequence\": [\"inproceedings\", \"inproceedings\"], \"lamb2016professor\": [\"inproceedings\", \"inproceedings\"], \"leblond2018searnn\": [\"inproceedings\", \"inproceedings\"], \"he2019exposure\": [\"article\", \"article\"], \"yu2020pcgrad\": [\"inproceedings\", \"inproceedings\"], \"chen2018gradnorm\": [\"inproceedings\", \"inproceedings\"], \"liu2021cagrad\": [\"inproceedings\", \"inproceedings\"], \"navon2022nash\": [\"inproceedings\", \"inproceedings\"], \"bachlechner2021rezero\": [\"inproceedings\", \"inproceedings\"], \"zhang2019fixup\": [\"inproceedings\", \"inproceedings\"]}, \"online_problems\": [{\"key\": \"anonymous2024reassessing\", \"title\": \"Reassessing Layer Pruning in LLMs: New Insights and Methods\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Reassessing Layer Pruning in LLMs: New Insights and Methods\", \"matched_year\": \"2024\", \"mismatch_fields\": [\"first_author: bib=anonymous vs api=lu\"], \"note\": \"\", \"source\": \"openalex\"}, {\"key\": \"fan2020layerdrop\", \"title\": \"Reducing Transformer Depth on Demand with Structured Dropout (LayerDrop)\", \"status\": \"not_found\", \"confidence\": 0.299, \"matched_title\": \"DeeBERT: Dynamic Early Exiting for Accelerating BERT Inference\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.30 below threshold 0.82\", \"source\": \"openalex\"}, {\"key\": \"levy2025lost\", \"title\": \"LLMs Get Lost In Multi-Turn Conversation\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"LLMs Get Lost In Multi-Turn Conversation\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"first_author: bib=levy vs api=laban\"], \"note\": \"\", \"source\": \"openalex\"}, {\"key\": \"anonymous2025style\", \"title\": \"Style Amnesia: Investigating Speaking Style Degradation and Mitigation in Multi-Turn Spoken Language Models\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Style Amnesia: Investigating Speaking Style Degradation and Mitigation in Multi-Turn Spoken Language Models\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"first_author: bib=anonymous vs api=lin\"], \"note\": \"\", \"source\": \"openalex\"}, {\"key\": \"schuster2022calm\", \"title\": \"Confident Adaptive Language Modeling\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Confident Adaptive Language Modeling\", \"matched_year\": \"2022\", \"mismatch_fields\": [\"first_author: bib=schuster vs api=bahri\"], \"note\": \"\", \"source\": \"crossref_search\"}, {\"key\": \"luo2025flexidepth\", \"title\": \"Adaptive Layer-skipping in Pre-trained LLMs (FlexiDepth)\", \"status\": \"not_found\", \"confidence\": 0.409, \"matched_title\": \"Dr.LLM: Dynamic Layer Routing in LLMs\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.41 below threshold 0.82\", \"source\": \"openalex\"}, {\"key\": \"chen2023positional\", \"title\": \"Extending Context Window of Large Language Models via Positional Interpolation\", \"status\": \"mismatch\", \"confidence\": 0.838, \"matched_title\": \"PSC: Extending Context Window of Large Language Models via Phase Shift Calibration\", \"matched_year\": \"2024\", \"mismatch_fields\": [\"first_author: bib=chen vs api=zhu\"], \"note\": \"\", \"source\": \"crossref_search\"}, {\"key\": \"xiao2024streaming\", \"title\": \"Efficient Streaming Language Models with Attention Sinks\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Efficient Streaming Language Models with Attention Sinks\", \"matched_year\": \"2023\", \"mismatch_fields\": [\"first_author: bib=xiao vs api=leonardo\"], \"note\": \"\", \"source\": \"openalex\"}, {\"key\": \"ko2024found\", \"title\": \"Found in the Middle: Calibrating Positional Attention Bias Improves Long Context Utilization\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Found in the middle: Calibrating Positional Attention Bias Improves Long Context Utilization\", \"matched_year\": \"2024\", \"mismatch_fields\": [\"first_author: bib=ko vs api=hsieh\"], \"note\": \"\", \"source\": \"crossref_search\"}, {\"key\": \"elhage2021framework\", \"title\": \"A Mathematical Framework for Transformer Circuits\", \"status\": \"not_found\", \"confidence\": 0.219, \"matched_title\": \"Review of deep learning: concepts, CNN architectures, challenges, applications, future directions\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.22 below threshold 0.82\", \"source\": \"openalex\"}, {\"key\": \"yu2023residual\", \"title\": \"Exploring the Residual Stream of Transformers\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Neuron-Level Knowledge Attribution in Large Language Models\", \"matched_year\": \"2023\", \"mismatch_fields\": [\"title: similarity=0.21 (possible wrong arXiv ID)\"], \"note\": \"\", \"source\": \"arxiv\"}, {\"key\": \"he2019exposure\", \"title\": \"Quantifying Exposure Bias for Neural Language Generation\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Exposure Bias versus Self-Recovery: Are Distortions Really Incremental for Autoregressive Text Generation?\", \"matched_year\": \"2019\", \"mismatch_fields\": [\"title: similarity=0.41 (possible wrong arXiv ID)\"], \"note\": \"\", \"source\": \"arxiv\"}, {\"key\": \"grattafiori2024llama3\", \"title\": \"The Llama 3 Herd of Models\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"The Llama 3 herd of models\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"first_author: bib=grattafiori vs api=aaron\"], \"note\": \"\", \"source\": \"openalex\"}]}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "652e1b48-5425-4360-9d09-b4c254656213",
  "uuid": "8c10c2e1-17cb-48c0-a8bd-a09ac2cad2f8",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"summary\\\": {\\\"total_bib_entries\\\": 91, \\\"total_citations\\\": 46, \\\"unique_cited_keys\\\": 22, \\\"orphan_bib\\\": 24, \\\"missing_bib\\\": 0, \\\"duplicate_keys\\\": 45, \\\"online_verified\\\": 33, \\\"online_not_found\\\": 3, \\\"online_mismatch\\\": 10, \\\"online_error\\\": 0, \\\"online_checked\\\": 46, \\\"online_total\\\": 46, \\\"online_verified_by_doi\\\": 0, \\\"online_verified_by_arxiv\\\": 20, \\\"online_verified_by_search\\\": 13}, \\\"cross_check\\\": {\\\"orphan_bib\\\": [\\\"anonymous2024reassessing\\\", \\\"anonymous2025style\\\", \\\"belrose2023tuned\\\", \\\"chen2023positional\\\", \\\"chiang2024arena\\\", \\\"dubois2024alpacaeval\\\", \\\"elhage2021framework\\\", \\\"elhage2022superposition\\\", \\\"gromov2024deeper\\\", \\\"han2024lminfinite\\\", \\\"ildiz2024markov\\\", \\\"lawson2025skip\\\", \\\"lin2024wildbench\\\", \\\"liu2023lost\\\", \\\"makkuva2025markov\\\", \\\"men2024shortgpt\\\", \\\"peng2024yarn\\\", \\\"press2022alibi\\\", \\\"sirdeshmukh2025multichallenge\\\", \\\"sun2025curse\\\", \\\"wang2018skipnet\\\", \\\"yu2023residual\\\", \\\"zhang2019fixup\\\", \\\"zheng2023mtbench\\\"], \\\"missing_bib\\\": [], \\\"orphan_count\\\": 24, \\\"missing_count\\\": 0}, \\\"bib_problems\\\": [{\\\"key\\\": \\\"gromov2024deeper\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"The Unreasonable Ineffectiveness of the Deeper Layers\\\", \\\"authors\\\": \\\"Gromov and others\\\", \\\"year\\\": \\\"2024\\\", \\\"issue\\\": \\\"orphan\\\"}, {\\\"key\\\": \\\"men2024shortgpt\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"ShortGPT: Layers in Large Language Models are More Redundant Than You Expect\\\", \\\"authors\\\": \\\"Men and others\\\", \\\"year\\\": \\\"2024\\\", \\\"issue\\\": \\\"orphan\\\"}, {\\\"key\\\": \\\"sun2025curse\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"The Curse of Depth in Large Language Models\\\", \\\"authors\\\": \\\"Sun and others\\\", \\\"year\\\": \\\"2025\\\", \\\"issue\\\": \\\"orphan\\\"}, {\\\"key\\\": \\\"anonymous2024reassessing\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Reassessing Layer Pruning in LLMs: New Insights and Methods\\\", \\\"authors\\\": \\\"Anonymous\\\", \\\"year\\\": \\\"2024\\\", \\\"issue\\\": \\\"orphan\\\"}, {\\\"key\\\": \\\"fan2020layerdrop\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Reducing Transformer Depth on Demand with Structured Dropout (LayerDrop)\\\", \\\"authors\\\": \\\"Fan and others\\\", \\\"year\\\": \\\"2020\\\", \\\"issue\\\": \\\"duplicate\\\"}, {\\\"key\\\": \\\"dongre2026attention\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"When Attention Closes: How LLMs Lose the Thread in Multi-Turn Interaction\\\", \\\"authors\\\": \\\"Dongre and Hsieh and Lai and Yoon and Bui and Hakkani-Tur\\\", \\\"year\\\": \\\"2026\\\", \\\"issue\\\": \\\"duplicate\\\"}, {\\\"key\\\": \\\"levy2025lost\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"LLMs Get Lost In Multi-Turn Conversation\\\", \\\"authors\\\": \\\"Levy and others\\\", \\\"year\\\": \\\"2025\\\", \\\"issue\\\": \\\"duplicate\\\"}, {\\\"key\\\": \\\"liu2026intent\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Intent Mismatch Causes LLMs to Get Lost in Multi-Turn Conversation\\\", \\\"authors\\\": \\\"Liu and others\\\", \\\"year\\\": \\\"2026\\\", \\\"issue\\\": \\\"duplicate\\\"}, {\\\"key\\\": \\\"liu2023lost\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Lost in the Middle: How Language Models Use Long Contexts\\\", \\\"authors\\\": \\\"Liu and others\\\", \\\"year\\\": \\\"2023\\\", \\\"issue\\\": \\\"orphan\\\"}, {\\\"key\\\": \\\"anonymous2025style\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Style Amnesia: Investigating Speaking Style Degradation and Mitigation in Multi-Turn Spoken Language Models\\\", \\\"authors\\\": \\\"Anonymous\\\", \\\"year\\\": \\\"2025\\\", \\\"issue\\\": \\\"orphan\\\"}, {\\\"key\\\": \\\"raposo2024mixture\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Mixture-of-Depths: Dynamically Allocating Compute in Transformer-Based Language Models\\\", \\\"authors\\\": \\\"Raposo and others\\\", \\\"year\\\": \\\"2024\\\", \\\"issue\\\": \\\"duplicate\\\"}, {\\\"key\\\": \\\"schuster2022calm\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Confident Adaptive Language Modeling\\\", \\\"authors\\\": \\\"Schuster and others\\\", \\\"year\\\": \\\"2022\\\", \\\"issue\\\": \\\"duplicate\\\"}, {\\\"key\\\": \\\"qiu2025gated\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free\\\", \\\"authors\\\": \\\"Qiu and others\\\", \\\"year\\\": \\\"2025\\\", \\\"issue\\\": \\\"duplicate\\\"}, {\\\"key\\\": \\\"wang2018skipnet\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"SkipNet: Learning Dynamic Routing in Convolutional Networks\\\", \\\"authors\\\": \\\"Wang and others\\\", \\\"year\\\": \\\"2018\\\", \\\"issue\\\": \\\"orphan\\\"}, {\\\"key\\\": \\\"luo2025flexidepth\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Adaptive Layer-skipping in Pre-trained LLMs (FlexiDepth)\\\", \\\"authors\\\": \\\"Luo and others\\\", \\\"year\\\": \\\"2025\\\", \\\"issue\\\": \\\"duplicate\\\"}, {\\\"key\\\": \\\"lawson2025skip\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Learning to Skip the Middle Layers of Transformers\\\", \\\"authors\\\": \\\"Lawson and others\\\", \\\"year\\\": \\\"2025\\\", \\\"issue\\\": \\\"orphan\\\"}, {\\\"key\\\": \\\"press2022alibi\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Train Short, Test Long: Attention with Linear Biases Enables Input Length Extrapolation\\\", \\\"authors\\\": \\\"Press and others\\\", \\\"year\\\": \\\"2022\\\", \\\"issue\\\": \\\"orphan\\\"}, {\\\"key\\\": \\\"chen2023positional\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Extending Context Window of Large Language Models via Positional Interpolation\\\", \\\"authors\\\": \\\"Chen and others\\\", \\\"year\\\": \\\"2023\\\", \\\"issue\\\": \\\"orphan\\\"}, {\\\"key\\\": \\\"peng2024yarn\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"YaRN: Efficient Context Window Extension of Large Language Models\\\", \\\"authors\\\": \\\"Peng and others\\\", \\\"year\\\": \\\"2024\\\", \\\"issue\\\": \\\"orphan\\\"}, {\\\"key\\\": \\\"xiao2024streaming\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Efficient Streaming Language Models with Attention Sinks\\\", \\\"authors\\\": \\\"Xiao and others\\\", \\\"year\\\": \\\"2024\\\", \\\"issue\\\": \\\"duplicate\\\"}, {\\\"key\\\": \\\"han2024lminfinite\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"LM-Infinite: Zero-Shot Extreme Length Generalization for Large Language Models\\\", \\\"authors\\\": \\\"Han and others\\\", \\\"year\\\": \\\"2024\\\", \\\"issue\\\": \\\"orphan\\\"}, {\\\"key\\\": \\\"ko2024found\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Found in the Middle: Calibrating Positional Attention Bias Improves Long Context Utilization\\\", \\\"authors\\\": \\\"Ko and others\\\", \\\"year\\\": \\\"2024\\\", \\\"issue\\\": \\\"duplicate\\\"}, {\\\"key\\\": \\\"elhage2021framework\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"A Mathematical Framework for Transformer Circuits\\\", \\\"authors\\\": \\\"Elhage and others\\\", \\\"year\\\": \\\"2021\\\", \\\"issue\\\": \\\"orphan\\\"}, {\\\"key\\\": \\\"elhage2022superposition\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Toy Models of Superposition\\\", \\\"authors\\\": \\\"Elhage and others\\\", \\\"year\\\": \\\"2022\\\", \\\"issue\\\": \\\"orphan\\\"}, {\\\"key\\\": \\\"belrose2023tuned\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Eliciting Latent Predictions from Transformers with the Tuned Lens\\\", \\\"authors\\\": \\\"Belrose and others\\\", \\\"year\\\": \\\"2023\\\", \\\"issue\\\": \\\"orphan\\\"}, {\\\"key\\\": \\\"yu2023residual\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Exploring the Residual Stream of Transformers\\\", \\\"authors\\\": \\\"Yu and others\\\", \\\"year\\\": \\\"2023\\\", \\\"issue\\\": \\\"orphan\\\"}, {\\\"key\\\": \\\"makkuva2025markov\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Attention with Markov: A Framework for Principled Analysis of Transformers via Markov Chains\\\", \\\"authors\\\": \\\"Makkuva and others\\\", \\\"year\\\": \\\"2025\\\", \\\"issue\\\": \\\"orphan\\\"}, {\\\"key\\\": \\\"ildiz2024markov\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"From Self-Attention to Markov Models: Unveiling the Dynamics of Generative Transformers\\\", \\\"authors\\\": \\\"Ildiz and others\\\", \\\"year\\\": \\\"2024\\\", \\\"issue\\\": \\\"orphan\\\"}, {\\\"key\\\": \\\"zheng2023mtbench\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena\\\", \\\"authors\\\": \\\"Zheng and others\\\", \\\"year\\\": \\\"2023\\\", \\\"issue\\\": \\\"orphan\\\"}, {\\\"key\\\": \\\"chiang2024arena\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference\\\", \\\"authors\\\": \\\"Chiang and others\\\", \\\"year\\\": \\\"2024\\\", \\\"issue\\\": \\\"orphan\\\"}, {\\\"key\\\": \\\"dubois2024alpacaeval\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Length-Controlled AlpacaEval: A Simple Way to Debias Automatic Evaluators\\\", \\\"authors\\\": \\\"Dubois and others\\\", \\\"year\\\": \\\"2024\\\", \\\"issue\\\": \\\"orphan\\\"}, {\\\"key\\\": \\\"lin2024wildbench\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"WildBench: Benchmarking LLMs with Challenging Tasks from Real Users in the Wild\\\", \\\"authors\\\": \\\"Lin and others\\\", \\\"year\\\": \\\"2024\\\", \\\"issue\\\": \\\"orphan\\\"}, {\\\"key\\\": \\\"bai2024mtbench101\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"MT-Bench-101: A Fine-Grained Benchmark for Evaluating Large Language Models in Multi-Turn Dialogues\\\", \\\"authors\\\": \\\"Bai and others\\\", \\\"year\\\": \\\"2024\\\", \\\"issue\\\": \\\"duplicate\\\"}, {\\\"key\\\": \\\"sirdeshmukh2025multichallenge\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"MultiChallenge: A Realistic Multi-Turn Conversation Evaluation Benchmark Challenging to Frontier LLMs\\\", \\\"authors\\\": \\\"Sirdeshmukh and others\\\", \\\"year\\\": \\\"2025\\\", \\\"issue\\\": \\\"orphan\\\"}, {\\\"key\\\": \\\"bengio2015scheduled\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Scheduled Sampling for Sequence Prediction with Recurrent Neural Networks\\\", \\\"authors\\\": \\\"Bengio and Vinyals and Jaitly and Shazeer\\\", \\\"year\\\": \\\"2015\\\", \\\"issue\\\": \\\"duplicate\\\"}, {\\\"key\\\": \\\"ranzato2016sequence\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Sequence Level Training with Recurrent Neural Networks\\\", \\\"authors\\\": \\\"Ranzato and Chopra and Auli and Zaremba\\\", \\\"year\\\": \\\"2016\\\", \\\"issue\\\": \\\"duplicate\\\"}, {\\\"key\\\": \\\"lamb2016professor\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Professor Forcing: A New Algorithm for Training Recurrent Networks\\\", \\\"authors\\\": \\\"Lamb and Goyal and Zhang and Zhang and Courville and Bengio\\\", \\\"year\\\": \\\"2016\\\", \\\"issue\\\": \\\"duplicate\\\"}, {\\\"key\\\": \\\"leblond2018searnn\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"SEARNN: Training RNNs with Global-Local Losses\\\", \\\"authors\\\": \\\"Leblond and Alayrac and Osokin and Lacoste-Julien\\\", \\\"year\\\": \\\"2018\\\", \\\"issue\\\": \\\"duplicate\\\"}, {\\\"key\\\": \\\"he2019exposure\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Quantifying Exposure Bias for Neural Language Generation\\\", \\\"authors\\\": \\\"He and Zhang and Zhou and Glass\\\", \\\"year\\\": \\\"2019\\\", \\\"issue\\\": \\\"duplicate\\\"}, {\\\"key\\\": \\\"yu2020pcgrad\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Gradient Surgery for Multi-Task Learning\\\", \\\"authors\\\": \\\"Yu and Kumar and Gupta and Levine and Hausman and Finn\\\", \\\"year\\\": \\\"2020\\\", \\\"issue\\\": \\\"duplicate\\\"}, {\\\"key\\\": \\\"chen2018gradnorm\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"GradNorm: Gradient Normalization for Adaptive Loss Balancing in Deep Multitask Networks\\\", \\\"authors\\\": \\\"Chen and Badrinarayanan and Lee and Rabinovich\\\", \\\"year\\\": \\\"2018\\\", \\\"issue\\\": \\\"duplicate\\\"}, {\\\"key\\\": \\\"liu2021cagrad\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Conflict-Averse Gradient Descent for Multi-task Learning\\\", \\\"authors\\\": \\\"Liu and Liu and Jin and Stone and Liu\\\", \\\"year\\\": \\\"2021\\\", \\\"issue\\\": \\\"duplicate\\\"}, {\\\"key\\\": \\\"navon2022nash\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Multi-Task Learning as a Bargaining Game\\\", \\\"authors\\\": \\\"Navon and Shamsian and Achituve and Maron and Kawaguchi and Chechik and Fetaya\\\", \\\"year\\\": \\\"2022\\\", \\\"issue\\\": \\\"duplicate\\\"}, {\\\"key\\\": \\\"bachlechner2021rezero\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"ReZero is All You Need: Fast Convergence at Large Depth\\\", \\\"authors\\\": \\\"Bachlechner and Majumder and Mao and Cottrell and McAuley\\\", \\\"year\\\": \\\"2021\\\", \\\"issue\\\": \\\"duplicate\\\"}, {\\\"key\\\": \\\"zhang2019fixup\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Fixup Initialization: Residual Learning Without Normalization\\\", \\\"authors\\\": \\\"Zhang and Dauphin and Ma\\\", \\\"year\\\": \\\"2019\\\", \\\"issue\\\": \\\"orphan\\\"}, {\\\"key\\\": \\\"gromov2024deeper\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"The Unreasonable Ineffectiveness of the Deeper Layers\\\", \\\"authors\\\": \\\"Gromov and others\\\", \\\"year\\\": \\\"2024\\\", \\\"issue\\\": \\\"orphan\\\"}, {\\\"key\\\": \\\"men2024shortgpt\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"ShortGPT: Layers in Large Language Models are More Redundant Than You Expect\\\", \\\"authors\\\": \\\"Men and others\\\", \\\"year\\\": \\\"2024\\\", \\\"issue\\\": \\\"orphan\\\"}, {\\\"key\\\": \\\"sun2025curse\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"The Curse of Depth in Large Language Models\\\", \\\"authors\\\": \\\"Sun and others\\\", \\\"year\\\": \\\"2025\\\", \\\"issue\\\": \\\"orphan\\\"}, {\\\"key\\\": \\\"anonymous2024reassessing\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Reassessing Layer Pruning in LLMs: New Insights and Methods\\\", \\\"authors\\\": \\\"Anonymous\\\", \\\"year\\\": \\\"2024\\\", \\\"issue\\\": \\\"orphan\\\"}, {\\\"key\\\": \\\"fan2020layerdrop\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Reducing Transformer Depth on Demand with Structured Dropout (LayerDrop)\\\", \\\"authors\\\": \\\"Fan and others\\\", \\\"year\\\": \\\"2020\\\", \\\"issue\\\": \\\"duplicate\\\"}, {\\\"key\\\": \\\"dongre2026attention\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"When Attention Closes: How LLMs Lose the Thread in Multi-Turn Interaction\\\", \\\"authors\\\": \\\"Dongre and Hsieh and Lai and Yoon and Bui and Hakkani-Tur\\\", \\\"year\\\": \\\"2026\\\", \\\"issue\\\": \\\"duplicate\\\"}, {\\\"key\\\": \\\"levy2025lost\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"LLMs Get Lost In Multi-Turn Conversation\\\", \\\"authors\\\": \\\"Levy and others\\\", \\\"year\\\": \\\"2025\\\", \\\"issue\\\": \\\"duplicate\\\"}, {\\\"key\\\": \\\"liu2026intent\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Intent Mismatch Causes LLMs to Get Lost in Multi-Turn Conversation\\\", \\\"authors\\\": \\\"Liu and others\\\", \\\"year\\\": \\\"2026\\\", \\\"issue\\\": \\\"duplicate\\\"}, {\\\"key\\\": \\\"liu2023lost\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Lost in the Middle: How Language Models Use Long Contexts\\\", \\\"authors\\\": \\\"Liu and others\\\", \\\"year\\\": \\\"2023\\\", \\\"issue\\\": \\\"orphan\\\"}, {\\\"key\\\": \\\"anonymous2025style\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Style Amnesia: Investigating Speaking Style Degradation and Mitigation in Multi-Turn Spoken Language Models\\\", \\\"authors\\\": \\\"Anonymous\\\", \\\"year\\\": \\\"2025\\\", \\\"issue\\\": \\\"orphan\\\"}, {\\\"key\\\": \\\"raposo2024mixture\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Mixture-of-Depths: Dynamically Allocating Compute in Transformer-Based Language Models\\\", \\\"authors\\\": \\\"Raposo and others\\\", \\\"year\\\": \\\"2024\\\", \\\"issue\\\": \\\"duplicate\\\"}, {\\\"key\\\": \\\"schuster2022calm\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Confident Adaptive Language Modeling\\\", \\\"authors\\\": \\\"Schuster and others\\\", \\\"year\\\": \\\"2022\\\", \\\"issue\\\": \\\"duplicate\\\"}, {\\\"key\\\": \\\"qiu2025gated\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free\\\", \\\"authors\\\": \\\"Qiu and others\\\", \\\"year\\\": \\\"2025\\\", \\\"issue\\\": \\\"duplicate\\\"}, {\\\"key\\\": \\\"wang2018skipnet\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"SkipNet: Learning Dynamic Routing in Convolutional Networks\\\", \\\"authors\\\": \\\"Wang and others\\\", \\\"year\\\": \\\"2018\\\", \\\"issue\\\": \\\"orphan\\\"}, {\\\"key\\\": \\\"luo2025flexidepth\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Adaptive Layer-skipping in Pre-trained LLMs (FlexiDepth)\\\", \\\"authors\\\": \\\"Luo and others\\\", \\\"year\\\": \\\"2025\\\", \\\"issue\\\": \\\"duplicate\\\"}, {\\\"key\\\": \\\"lawson2025skip\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Learning to Skip the Middle Layers of Transformers\\\", \\\"authors\\\": \\\"Lawson and others\\\", \\\"year\\\": \\\"2025\\\", \\\"issue\\\": \\\"orphan\\\"}, {\\\"key\\\": \\\"press2022alibi\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Train Short, Test Long: Attention with Linear Biases Enables Input Length Extrapolation\\\", \\\"authors\\\": \\\"Press and others\\\", \\\"year\\\": \\\"2022\\\", \\\"issue\\\": \\\"orphan\\\"}, {\\\"key\\\": \\\"chen2023positional\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Extending Context Window of Large Language Models via Positional Interpolation\\\", \\\"authors\\\": \\\"Chen and others\\\", \\\"year\\\": \\\"2023\\\", \\\"issue\\\": \\\"orphan\\\"}, {\\\"key\\\": \\\"peng2024yarn\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"YaRN: Efficient Context Window Extension of Large Language Models\\\", \\\"authors\\\": \\\"Peng and others\\\", \\\"year\\\": \\\"2024\\\", \\\"issue\\\": \\\"orphan\\\"}, {\\\"key\\\": \\\"xiao2024streaming\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Efficient Streaming Language Models with Attention Sinks\\\", \\\"authors\\\": \\\"Xiao and others\\\", \\\"year\\\": \\\"2024\\\", \\\"issue\\\": \\\"duplicate\\\"}, {\\\"key\\\": \\\"han2024lminfinite\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"LM-Infinite: Zero-Shot Extreme Length Generalization for Large Language Models\\\", \\\"authors\\\": \\\"Han and others\\\", \\\"year\\\": \\\"2024\\\", \\\"issue\\\": \\\"orphan\\\"}, {\\\"key\\\": \\\"ko2024found\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Found in the Middle: Calibrating Positional Attention Bias Improves Long Context Utilization\\\", \\\"authors\\\": \\\"Ko and others\\\", \\\"year\\\": \\\"2024\\\", \\\"issue\\\": \\\"duplicate\\\"}, {\\\"key\\\": \\\"elhage2021framework\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"A Mathematical Framework for Transformer Circuits\\\", \\\"authors\\\": \\\"Elhage and others\\\", \\\"year\\\": \\\"2021\\\", \\\"issue\\\": \\\"orphan\\\"}, {\\\"key\\\": \\\"elhage2022superposition\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Toy Models of Superposition\\\", \\\"authors\\\": \\\"Elhage and others\\\", \\\"year\\\": \\\"2022\\\", \\\"issue\\\": \\\"orphan\\\"}, {\\\"key\\\": \\\"belrose2023tuned\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Eliciting Latent Predictions from Transformers with the Tuned Lens\\\", \\\"authors\\\": \\\"Belrose and others\\\", \\\"year\\\": \\\"2023\\\", \\\"issue\\\": \\\"orphan\\\"}, {\\\"key\\\": \\\"yu2023residual\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Exploring the Residual Stream of Transformers\\\", \\\"authors\\\": \\\"Yu and others\\\", \\\"year\\\": \\\"2023\\\", \\\"issue\\\": \\\"orphan\\\"}, {\\\"key\\\": \\\"makkuva2025markov\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Attention with Markov: A Framework for Principled Analysis of Transformers via Markov Chains\\\", \\\"authors\\\": \\\"Makkuva and others\\\", \\\"year\\\": \\\"2025\\\", \\\"issue\\\": \\\"orphan\\\"}, {\\\"key\\\": \\\"ildiz2024markov\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"From Self-Attention to Markov Models: Unveiling the Dynamics of Generative Transformers\\\", \\\"authors\\\": \\\"Ildiz and others\\\", \\\"year\\\": \\\"2024\\\", \\\"issue\\\": \\\"orphan\\\"}, {\\\"key\\\": \\\"zheng2023mtbench\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena\\\", \\\"authors\\\": \\\"Zheng and others\\\", \\\"year\\\": \\\"2023\\\", \\\"issue\\\": \\\"orphan\\\"}, {\\\"key\\\": \\\"chiang2024arena\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference\\\", \\\"authors\\\": \\\"Chiang and others\\\", \\\"year\\\": \\\"2024\\\", \\\"issue\\\": \\\"orphan\\\"}, {\\\"key\\\": \\\"dubois2024alpacaeval\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Length-Controlled AlpacaEval: A Simple Way to Debias Automatic Evaluators\\\", \\\"authors\\\": \\\"Dubois and others\\\", \\\"year\\\": \\\"2024\\\", \\\"issue\\\": \\\"orphan\\\"}, {\\\"key\\\": \\\"lin2024wildbench\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"WildBench: Benchmarking LLMs with Challenging Tasks from Real Users in the Wild\\\", \\\"authors\\\": \\\"Lin and others\\\", \\\"year\\\": \\\"2024\\\", \\\"issue\\\": \\\"orphan\\\"}, {\\\"key\\\": \\\"bai2024mtbench101\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"MT-Bench-101: A Fine-Grained Benchmark for Evaluating Large Language Models in Multi-Turn Dialogues\\\", \\\"authors\\\": \\\"Bai and others\\\", \\\"year\\\": \\\"2024\\\", \\\"issue\\\": \\\"duplicate\\\"}, {\\\"key\\\": \\\"sirdeshmukh2025multichallenge\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"MultiChallenge: A Realistic Multi-Turn Conversation Evaluation Benchmark Challenging to Frontier LLMs\\\", \\\"authors\\\": \\\"Sirdeshmukh and others\\\", \\\"year\\\": \\\"2025\\\", \\\"issue\\\": \\\"orphan\\\"}, {\\\"key\\\": \\\"bengio2015scheduled\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Scheduled Sampling for Sequence Prediction with Recurrent Neural Networks\\\", \\\"authors\\\": \\\"Bengio and Vinyals and Jaitly and Shazeer\\\", \\\"year\\\": \\\"2015\\\", \\\"issue\\\": \\\"duplicate\\\"}, {\\\"key\\\": \\\"ranzato2016sequence\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Sequence Level Training with Recurrent Neural Networks\\\", \\\"authors\\\": \\\"Ranzato and Chopra and Auli and Zaremba\\\", \\\"year\\\": \\\"2016\\\", \\\"issue\\\": \\\"duplicate\\\"}, {\\\"key\\\": \\\"lamb2016professor\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Professor Forcing: A New Algorithm for Training Recurrent Networks\\\", \\\"authors\\\": \\\"Lamb and Goyal and Zhang and Zhang and Courville and Bengio\\\", \\\"year\\\": \\\"2016\\\", \\\"issue\\\": \\\"duplicate\\\"}, {\\\"key\\\": \\\"leblond2018searnn\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"SEARNN: Training RNNs with Global-Local Losses\\\", \\\"authors\\\": \\\"Leblond and Alayrac and Osokin and Lacoste-Julien\\\", \\\"year\\\": \\\"2018\\\", \\\"issue\\\": \\\"duplicate\\\"}, {\\\"key\\\": \\\"he2019exposure\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Quantifying Exposure Bias for Neural Language Generation\\\", \\\"authors\\\": \\\"He and Zhang and Zhou and Glass\\\", \\\"year\\\": \\\"2019\\\", \\\"issue\\\": \\\"duplicate\\\"}, {\\\"key\\\": \\\"yu2020pcgrad\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Gradient Surgery for Multi-Task Learning\\\", \\\"authors\\\": \\\"Yu and Kumar and Gupta and Levine and Hausman and Finn\\\", \\\"year\\\": \\\"2020\\\", \\\"issue\\\": \\\"duplicate\\\"}, {\\\"key\\\": \\\"chen2018gradnorm\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"GradNorm: Gradient Normalization for Adaptive Loss Balancing in Deep Multitask Networks\\\", \\\"authors\\\": \\\"Chen and Badrinarayanan and Lee and Rabinovich\\\", \\\"year\\\": \\\"2018\\\", \\\"issue\\\": \\\"duplicate\\\"}, {\\\"key\\\": \\\"liu2021cagrad\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Conflict-Averse Gradient Descent for Multi-task Learning\\\", \\\"authors\\\": \\\"Liu and Liu and Jin and Stone and Liu\\\", \\\"year\\\": \\\"2021\\\", \\\"issue\\\": \\\"duplicate\\\"}, {\\\"key\\\": \\\"navon2022nash\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Multi-Task Learning as a Bargaining Game\\\", \\\"authors\\\": \\\"Navon and Shamsian and Achituve and Maron and Kawaguchi and Chechik and Fetaya\\\", \\\"year\\\": \\\"2022\\\", \\\"issue\\\": \\\"duplicate\\\"}, {\\\"key\\\": \\\"bachlechner2021rezero\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"ReZero is All You Need: Fast Convergence at Large Depth\\\", \\\"authors\\\": \\\"Bachlechner and Majumder and Mao and Cottrell and McAuley\\\", \\\"year\\\": \\\"2021\\\", \\\"issue\\\": \\\"duplicate\\\"}, {\\\"key\\\": \\\"zhang2019fixup\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Fixup Initialization: Residual Learning Without Normalization\\\", \\\"authors\\\": \\\"Zhang and Dauphin and Ma\\\", \\\"year\\\": \\\"2019\\\", \\\"issue\\\": \\\"orphan\\\"}], \\\"duplicate_keys\\\": {\\\"gromov2024deeper\\\": [\\\"inproceedings\\\", \\\"inproceedings\\\"], \\\"men2024shortgpt\\\": [\\\"article\\\", \\\"article\\\"], \\\"sun2025curse\\\": [\\\"inproceedings\\\", \\\"inproceedings\\\"], \\\"anonymous2024reassessing\\\": [\\\"article\\\", \\\"article\\\"], \\\"fan2020layerdrop\\\": [\\\"inproceedings\\\", \\\"inproceedings\\\"], \\\"dongre2026attention\\\": [\\\"article\\\", \\\"article\\\"], \\\"levy2025lost\\\": [\\\"article\\\", \\\"article\\\"], \\\"liu2026intent\\\": [\\\"article\\\", \\\"article\\\"], \\\"liu2023lost\\\": [\\\"article\\\", \\\"article\\\"], \\\"anonymous2025style\\\": [\\\"article\\\", \\\"article\\\"], \\\"raposo2024mixture\\\": [\\\"article\\\", \\\"article\\\"], \\\"schuster2022calm\\\": [\\\"inproceedings\\\", \\\"inproceedings\\\"], \\\"qiu2025gated\\\": [\\\"inproceedings\\\", \\\"inproceedings\\\"], \\\"wang2018skipnet\\\": [\\\"inproceedings\\\", \\\"inproceedings\\\"], \\\"luo2025flexidepth\\\": [\\\"article\\\", \\\"article\\\"], \\\"lawson2025skip\\\": [\\\"article\\\", \\\"article\\\"], \\\"press2022alibi\\\": [\\\"inproceedings\\\", \\\"inproceedings\\\"], \\\"chen2023positional\\\": [\\\"article\\\", \\\"article\\\"], \\\"peng2024yarn\\\": [\\\"inproceedings\\\", \\\"inproceedings\\\"], \\\"xiao2024streaming\\\": [\\\"inproceedings\\\", \\\"inproceedings\\\"], \\\"han2024lminfinite\\\": [\\\"inproceedings\\\", \\\"inproceedings\\\"], \\\"ko2024found\\\": [\\\"article\\\", \\\"article\\\"], \\\"elhage2021framework\\\": [\\\"article\\\", \\\"article\\\"], \\\"elhage2022superposition\\\": [\\\"article\\\", \\\"article\\\"], \\\"belrose2023tuned\\\": [\\\"article\\\", \\\"article\\\"], \\\"yu2023residual\\\": [\\\"article\\\", \\\"article\\\"], \\\"makkuva2025markov\\\": [\\\"inproceedings\\\", \\\"inproceedings\\\"], \\\"ildiz2024markov\\\": [\\\"inproceedings\\\", \\\"inproceedings\\\"], \\\"zheng2023mtbench\\\": [\\\"inproceedings\\\", \\\"inproceedings\\\"], \\\"chiang2024arena\\\": [\\\"inproceedings\\\", \\\"inproceedings\\\"], \\\"dubois2024alpacaeval\\\": [\\\"inproceedings\\\", \\\"inproceedings\\\"], \\\"lin2024wildbench\\\": [\\\"article\\\", \\\"article\\\"], \\\"bai2024mtbench101\\\": [\\\"inproceedings\\\", \\\"inproceedings\\\"], \\\"sirdeshmukh2025multichallenge\\\": [\\\"article\\\", \\\"article\\\"], \\\"bengio2015scheduled\\\": [\\\"inproceedings\\\", \\\"inproceedings\\\"], \\\"ranzato2016sequence\\\": [\\\"inproceedings\\\", \\\"inproceedings\\\"], \\\"lamb2016professor\\\": [\\\"inproceedings\\\", \\\"inproceedings\\\"], \\\"leblond2018searnn\\\": [\\\"inproceedings\\\", \\\"inproceedings\\\"], \\\"he2019exposure\\\": [\\\"article\\\", \\\"article\\\"], \\\"yu2020pcgrad\\\": [\\\"inproceedings\\\", \\\"inproceedings\\\"], \\\"chen2018gradnorm\\\": [\\\"inproceedings\\\", \\\"inproceedings\\\"], \\\"liu2021cagrad\\\": [\\\"inproceedings\\\", \\\"inproceedings\\\"], \\\"navon2022nash\\\": [\\\"inproceedings\\\", \\\"inproceedings\\\"], \\\"bachlechner2021rezero\\\": [\\\"inproceedings\\\", \\\"inproceedings\\\"], \\\"zhang2019fixup\\\": [\\\"inproceedings\\\", \\\"inproceedings\\\"]}, \\\"online_problems\\\": [{\\\"key\\\": \\\"anonymous2024reassessing\\\", \\\"title\\\": \\\"Reassessing Layer Pruning in LLMs: New Insights and Methods\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Reassessing Layer Pruning in LLMs: New Insights and Methods\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=anonymous vs api=lu\\\"], \\\"note\\\": \\\"\\\", \\\"source\\\": \\\"openalex\\\"}, {\\\"key\\\": \\\"fan2020layerdrop\\\", \\\"title\\\": \\\"Reducing Transformer Depth on Demand with Structured Dropout (LayerDrop)\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.299, \\\"matched_title\\\": \\\"DeeBERT: Dynamic Early Exiting for Accelerating BERT Inference\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.30 below threshold 0.82\\\", \\\"source\\\": \\\"openalex\\\"}, {\\\"key\\\": \\\"levy2025lost\\\", \\\"title\\\": \\\"LLMs Get Lost In Multi-Turn Conversation\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"LLMs Get Lost In Multi-Turn Conversation\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=levy vs api=laban\\\"], \\\"note\\\": \\\"\\\", \\\"source\\\": \\\"openalex\\\"}, {\\\"key\\\": \\\"anonymous2025style\\\", \\\"title\\\": \\\"Style Amnesia: Investigating Speaking Style Degradation and Mitigation in Multi-Turn Spoken Language Models\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Style Amnesia: Investigating Speaking Style Degradation and Mitigation in Multi-Turn Spoken Language Models\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=anonymous vs api=lin\\\"], \\\"note\\\": \\\"\\\", \\\"source\\\": \\\"openalex\\\"}, {\\\"key\\\": \\\"schuster2022calm\\\", \\\"title\\\": \\\"Confident Adaptive Language Modeling\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Confident Adaptive Language Modeling\\\", \\\"matched_year\\\": \\\"2022\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=schuster vs api=bahri\\\"], \\\"note\\\": \\\"\\\", \\\"source\\\": \\\"crossref_search\\\"}, {\\\"key\\\": \\\"luo2025flexidepth\\\", \\\"title\\\": \\\"Adaptive Layer-skipping in Pre-trained LLMs (FlexiDepth)\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.409, \\\"matched_title\\\": \\\"Dr.LLM: Dynamic Layer Routing in LLMs\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.41 below threshold 0.82\\\", \\\"source\\\": \\\"openalex\\\"}, {\\\"key\\\": \\\"chen2023positional\\\", \\\"title\\\": \\\"Extending Context Window of Large Language Models via Positional Interpolation\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 0.838, \\\"matched_title\\\": \\\"PSC: Extending Context Window of Large Language Models via Phase Shift Calibration\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=chen vs api=zhu\\\"], \\\"note\\\": \\\"\\\", \\\"source\\\": \\\"crossref_search\\\"}, {\\\"key\\\": \\\"xiao2024streaming\\\", \\\"title\\\": \\\"Efficient Streaming Language Models with Attention Sinks\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Efficient Streaming Language Models with Attention Sinks\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=xiao vs api=leonardo\\\"], \\\"note\\\": \\\"\\\", \\\"source\\\": \\\"openalex\\\"}, {\\\"key\\\": \\\"ko2024found\\\", \\\"title\\\": \\\"Found in the Middle: Calibrating Positional Attention Bias Improves Long Context Utilization\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Found in the middle: Calibrating Positional Attention Bias Improves Long Context Utilization\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=ko vs api=hsieh\\\"], \\\"note\\\": \\\"\\\", \\\"source\\\": \\\"crossref_search\\\"}, {\\\"key\\\": \\\"elhage2021framework\\\", \\\"title\\\": \\\"A Mathematical Framework for Transformer Circuits\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.219, \\\"matched_title\\\": \\\"Review of deep learning: concepts, CNN architectures, challenges, applications, future directions\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.22 below threshold 0.82\\\", \\\"source\\\": \\\"openalex\\\"}, {\\\"key\\\": \\\"yu2023residual\\\", \\\"title\\\": \\\"Exploring the Residual Stream of Transformers\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Neuron-Level Knowledge Attribution in Large Language Models\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [\\\"title: similarity=0.21 (possible wrong arXiv ID)\\\"], \\\"note\\\": \\\"\\\", \\\"source\\\": \\\"arxiv\\\"}, {\\\"key\\\": \\\"he2019exposure\\\", \\\"title\\\": \\\"Quantifying Exposure Bias for Neural Language Generation\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Exposure Bias versus Self-Recovery: Are Distortions Really Incremental for Autoregressive Text Generation?\\\", \\\"matched_year\\\": \\\"2019\\\", \\\"mismatch_fields\\\": [\\\"title: similarity=0.41 (possible wrong arXiv ID)\\\"], \\\"note\\\": \\\"\\\", \\\"source\\\": \\\"arxiv\\\"}, {\\\"key\\\": \\\"grattafiori2024llama3\\\", \\\"title\\\": \\\"The Llama 3 Herd of Models\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"The Llama 3 herd of models\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=grattafiori vs api=aaron\\\"], \\\"note\\\": \\\"\\\", \\\"source\\\": \\\"openalex\\\"}]}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 91, \"total_citations\": 46, \"unique_cited_keys\": 22, \"orphan_bib\": 24, \"missing_bib\": 0, \"duplicate_keys\": 45, \"online_verified\": 33, \"online_not_found\": 3, \"online_mismatch\": 10, \"online_error\": 0, \"online_checked\": 46, \"online_total\": 46, \"online_verified_by_doi\": 0, \"online_verified_by_arxiv\": 20, \"online_verified_by_search\": 13}, \"cross_check\": {\"orphan_bib\": [\"anonymous2024reassessing\", \"anonymous2025style\", \"belrose2023tuned\", \"chen2023positional\", \"chiang2024arena\", \"dubois2024alpacaeval\", \"elhage2021framework\", \"elhage2022superposition\", \"gromov2024deeper\", \"han2024lminfinite\", \"ildiz2024markov\", \"lawson2025skip\", \"lin2024wildbench\", \"liu2023lost\", \"makkuva2025markov\", \"men2024shortgpt\", \"peng2024yarn\", \"press2022alibi\", \"sirdeshmukh2025multichallenge\", \"sun2025curse\", \"wang2018skipnet\", \"yu2023residual\", \"zhang2019fixup\", \"zheng2023mtbench\"], \"missing_bib\": [], \"orphan_count\": 24, \"missing_count\": 0}, \"bib_problems\": [{\"key\": \"gromov2024deeper\", \"type\": \"inproceedings\", \"title\": \"The Unreasonable Ineffectiveness of the Deeper Layers\", \"authors\": \"Gromov and others\", \"year\": \"2024\", \"issue\": \"orphan\"}, {\"key\": \"men2024shortgpt\", \"type\": \"article\", \"title\": \"ShortGPT: Layers in Large Language Models are More Redundant Than You Expect\", \"authors\": \"Men and others\", \"year\": \"2024\", \"issue\": \"orphan\"}, {\"key\": \"sun2025curse\", \"type\": \"inproceedings\", \"title\": \"The Curse of Depth in Large Language Models\", \"authors\": \"Sun and others\", \"year\": \"2025\", \"issue\": \"orphan\"}, {\"key\": \"anonymous2024reassessing\", \"type\": \"article\", \"title\": \"Reassessing Layer Pruning in LLMs: New Insights and Methods\", \"authors\": \"Anonymous\", \"year\": \"2024\", \"issue\": \"orphan\"}, {\"key\": \"fan2020layerdrop\", \"type\": \"inproceedings\", \"title\": \"Reducing Transformer Depth on Demand with Structured Dropout (LayerDrop)\", \"authors\": \"Fan and others\", \"year\": \"2020\", \"issue\": \"duplicate\"}, {\"key\": \"dongre2026attention\", \"type\": \"article\", \"title\": \"When Attention Closes: How LLMs Lose the Thread in Multi-Turn Interaction\", \"authors\": \"Dongre and Hsieh and Lai and Yoon and Bui and Hakkani-Tur\", \"year\": \"2026\", \"issue\": \"duplicate\"}, {\"key\": \"levy2025lost\", \"type\": \"article\", \"title\": \"LLMs Get Lost In Multi-Turn Conversation\", \"authors\": \"Levy and others\", \"year\": \"2025\", \"issue\": \"duplicate\"}, {\"key\": \"liu2026intent\", \"type\": \"article\", \"title\": \"Intent Mismatch Causes LLMs to Get Lost in Multi-Turn Conversation\", \"authors\": \"Liu and others\", \"year\": \"2026\", \"issue\": \"duplicate\"}, {\"key\": \"liu2023lost\", \"type\": \"article\", \"title\": \"Lost in the Middle: How Language Models Use Long Contexts\", \"authors\": \"Liu and others\", \"year\": \"2023\", \"issue\": \"orphan\"}, {\"key\": \"anonymous2025style\", \"type\": \"article\", \"title\": \"Style Amnesia: Investigating Speaking Style Degradation and Mitigation in Multi-Turn Spoken Language Models\", \"authors\": \"Anonymous\", \"year\": \"2025\", \"issue\": \"orphan\"}, {\"key\": \"raposo2024mixture\", \"type\": \"article\", \"title\": \"Mixture-of-Depths: Dynamically Allocating Compute in Transformer-Based Language Models\", \"authors\": \"Raposo and others\", \"year\": \"2024\", \"issue\": \"duplicate\"}, {\"key\": \"schuster2022calm\", \"type\": \"inproceedings\", \"title\": \"Confident Adaptive Language Modeling\", \"authors\": \"Schuster and others\", \"year\": \"2022\", \"issue\": \"duplicate\"}, {\"key\": \"qiu2025gated\", \"type\": \"inproceedings\", \"title\": \"Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free\", \"authors\": \"Qiu and others\", \"year\": \"2025\", \"issue\": \"duplicate\"}, {\"key\": \"wang2018skipnet\", \"type\": \"inproceedings\", \"title\": \"SkipNet: Learning Dynamic Routing in Convolutional Networks\", \"authors\": \"Wang and others\", \"year\": \"2018\", \"issue\": \"orphan\"}, {\"key\": \"luo2025flexidepth\", \"type\": \"article\", \"title\": \"Adaptive Layer-skipping in Pre-trained LLMs (FlexiDepth)\", \"authors\": \"Luo and others\", \"year\": \"2025\", \"issue\": \"duplicate\"}, {\"key\": \"lawson2025skip\", \"type\": \"article\", \"title\": \"Learning to Skip the Middle Layers of Transformers\", \"authors\": \"Lawson and others\", \"year\": \"2025\", \"issue\": \"orphan\"}, {\"key\": \"press2022alibi\", \"type\": \"inproceedings\", \"title\": \"Train Short, Test Long: Attention with Linear Biases Enables Input Length Extrapolation\", \"authors\": \"Press and others\", \"year\": \"2022\", \"issue\": \"orphan\"}, {\"key\": \"chen2023positional\", \"type\": \"article\", \"title\": \"Extending Context Window of Large Language Models via Positional Interpolation\", \"authors\": \"Chen and others\", \"year\": \"2023\", \"issue\": \"orphan\"}, {\"key\": \"peng2024yarn\", \"type\": \"inproceedings\", \"title\": \"YaRN: Efficient Context Window Extension of Large Language Models\", \"authors\": \"Peng and others\", \"year\": \"2024\", \"issue\": \"orphan\"}, {\"key\": \"xiao2024streaming\", \"type\": \"inproceedings\", \"title\": \"Efficient Streaming Language Models with Attention Sinks\", \"authors\": \"Xiao and others\", \"year\": \"2024\", \"issue\": \"duplicate\"}, {\"key\": \"han2024lminfinite\", \"type\": \"inproceedings\", \"title\": \"LM-Infinite: Zero-Shot Extreme Length Generalization for Large Language Models\", \"authors\": \"Han and others\", \"year\": \"2024\", \"issue\": \"orphan\"}, {\"key\": \"ko2024found\", \"type\": \"article\", \"title\": \"Found in the Middle: Calibrating Positional Attention Bias Improves Long Context Utilization\", \"authors\": \"Ko and others\", \"year\": \"2024\", \"issue\": \"duplicate\"}, {\"key\": \"elhage2021framework\", \"type\": \"article\", \"title\": \"A Mathematical Framework for Transformer Circuits\", \"authors\": \"Elhage and others\", \"year\": \"2021\", \"issue\": \"orphan\"}, {\"key\": \"elhage2022superposition\", \"type\": \"article\", \"title\": \"Toy Models of Superposition\", \"authors\": \"Elhage and others\", \"year\": \"2022\", \"issue\": \"orphan\"}, {\"key\": \"belrose2023tuned\", \"type\": \"article\", \"title\": \"Eliciting Latent Predictions from Transformers with the Tuned Lens\", \"authors\": \"Belrose and others\", \"year\": \"2023\", \"issue\": \"orphan\"}, {\"key\": \"yu2023residual\", \"type\": \"article\", \"title\": \"Exploring the Residual Stream of Transformers\", \"authors\": \"Yu and others\", \"year\": \"2023\", \"issue\": \"orphan\"}, {\"key\": \"makkuva2025markov\", \"type\": \"inproceedings\", \"title\": \"Attention with Markov: A Framework for Principled Analysis of Transformers via Markov Chains\", \"authors\": \"Makkuva and others\", \"year\": \"2025\", \"issue\": \"orphan\"}, {\"key\": \"ildiz2024markov\", \"type\": \"inproceedings\", \"title\": \"From Self-Attention to Markov Models: Unveiling the Dynamics of Generative Transformers\", \"authors\": \"Ildiz and others\", \"year\": \"2024\", \"issue\": \"orphan\"}, {\"key\": \"zheng2023mtbench\", \"type\": \"inproceedings\", \"title\": \"Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena\", \"authors\": \"Zheng and others\", \"year\": \"2023\", \"issue\": \"orphan\"}, {\"key\": \"chiang2024arena\", \"type\": \"inproceedings\", \"title\": \"Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference\", \"authors\": \"Chiang and others\", \"year\": \"2024\", \"issue\": \"orphan\"}, {\"key\": \"dubois2024alpacaeval\", \"type\": \"inproceedings\", \"title\": \"Length-Controlled AlpacaEval: A Simple Way to Debias Automatic Evaluators\", \"authors\": \"Dubois and others\", \"year\": \"2024\", \"issue\": \"orphan\"}, {\"key\": \"lin2024wildbench\", \"type\": \"article\", \"title\": \"WildBench: Benchmarking LLMs with Challenging Tasks from Real Users in the Wild\", \"authors\": \"Lin and others\", \"year\": \"2024\", \"issue\": \"orphan\"}, {\"key\": \"bai2024mtbench101\", \"type\": \"inproceedings\", \"title\": \"MT-Bench-101: A Fine-Grained Benchmark for Evaluating Large Language Models in Multi-Turn Dialogues\", \"authors\": \"Bai and others\", \"year\": \"2024\", \"issue\": \"duplicate\"}, {\"key\": \"sirdeshmukh2025multichallenge\", \"type\": \"article\", \"title\": \"MultiChallenge: A Realistic Multi-Turn Conversation Evaluation Benchmark Challenging to Frontier LLMs\", \"authors\": \"Sirdeshmukh and others\", \"year\": \"2025\", \"issue\": \"orphan\"}, {\"key\": \"bengio2015scheduled\", \"type\": \"inproceedings\", \"title\": \"Scheduled Sampling for Sequence Prediction with Recurrent Neural Networks\", \"authors\": \"Bengio and Vinyals and Jaitly and Shazeer\", \"year\": \"2015\", \"issue\": \"duplicate\"}, {\"key\": \"ranzato2016sequence\", \"type\": \"inproceedings\", \"title\": \"Sequence Level Training with Recurrent Neural Networks\", \"authors\": \"Ranzato and Chopra and Auli and Zaremba\", \"year\": \"2016\", \"issue\": \"duplicate\"}, {\"key\": \"lamb2016professor\", \"type\": \"inproceedings\", \"title\": \"Professor Forcing: A New Algorithm for Training Recurrent Networks\", \"authors\": \"Lamb and Goyal and Zhang and Zhang and Courville and Bengio\", \"year\": \"2016\", \"issue\": \"duplicate\"}, {\"key\": \"leblond2018searnn\", \"type\": \"inproceedings\", \"title\": \"SEARNN: Training RNNs with Global-Local Losses\", \"authors\": \"Leblond and Alayrac and Osokin and Lacoste-Julien\", \"year\": \"2018\", \"issue\": \"duplicate\"}, {\"key\": \"he2019exposure\", \"type\": \"article\", \"title\": \"Quantifying Exposure Bias for Neural Language Generation\", \"authors\": \"He and Zhang and Zhou and Glass\", \"year\": \"2019\", \"issue\": \"duplicate\"}, {\"key\": \"yu2020pcgrad\", \"type\": \"inproceedings\", \"title\": \"Gradient Surgery for Multi-Task Learning\", \"authors\": \"Yu and Kumar and Gupta and Levine and Hausman and Finn\", \"year\": \"2020\", \"issue\": \"duplicate\"}, {\"key\": \"chen2018gradnorm\", \"type\": \"inproceedings\", \"title\": \"GradNorm: Gradient Normalization for Adaptive Loss Balancing in Deep Multitask Networks\", \"authors\": \"Chen and Badrinarayanan and Lee and Rabinovich\", \"year\": \"2018\", \"issue\": \"duplicate\"}, {\"key\": \"liu2021cagrad\", \"type\": \"inproceedings\", \"title\": \"Conflict-Averse Gradient Descent for Multi-task Learning\", \"authors\": \"Liu and Liu and Jin and Stone and Liu\", \"year\": \"2021\", \"issue\": \"duplicate\"}, {\"key\": \"navon2022nash\", \"type\": \"inproceedings\", \"title\": \"Multi-Task Learning as a Bargaining Game\", \"authors\": \"Navon and Shamsian and Achituve and Maron and Kawaguchi and Chechik and Fetaya\", \"year\": \"2022\", \"issue\": \"duplicate\"}, {\"key\": \"bachlechner2021rezero\", \"type\": \"inproceedings\", \"title\": \"ReZero is All You Need: Fast Convergence at Large Depth\", \"authors\": \"Bachlechner and Majumder and Mao and Cottrell and McAuley\", \"year\": \"2021\", \"issue\": \"duplicate\"}, {\"key\": \"zhang2019fixup\", \"type\": \"inproceedings\", \"title\": \"Fixup Initialization: Residual Learning Without Normalization\", \"authors\": \"Zhang and Dauphin and Ma\", \"year\": \"2019\", \"issue\": \"orphan\"}, {\"key\": \"gromov2024deeper\", \"type\": \"inproceedings\", \"title\": \"The Unreasonable Ineffectiveness of the Deeper Layers\", \"authors\": \"Gromov and others\", \"year\": \"2024\", \"issue\": \"orphan\"}, {\"key\": \"men2024shortgpt\", \"type\": \"article\", \"title\": \"ShortGPT: Layers in Large Language Models are More Redundant Than You Expect\", \"authors\": \"Men and others\", \"year\": \"2024\", \"issue\": \"orphan\"}, {\"key\": \"sun2025curse\", \"type\": \"inproceedings\", \"title\": \"The Curse of Depth in Large Language Models\", \"authors\": \"Sun and others\", \"year\": \"2025\", \"issue\": \"orphan\"}, {\"key\": \"anonymous2024reassessing\", \"type\": \"article\", \"title\": \"Reassessing Layer Pruning in LLMs: New Insights and Methods\", \"authors\": \"Anonymous\", \"year\": \"2024\", \"issue\": \"orphan\"}, {\"key\": \"fan2020layerdrop\", \"type\": \"inproceedings\", \"title\": \"Reducing Transformer Depth on Demand with Structured Dropout (LayerDrop)\", \"authors\": \"Fan and others\", \"year\": \"2020\", \"issue\": \"duplicate\"}, {\"key\": \"dongre2026attention\", \"type\": \"article\", \"title\": \"When Attention Closes: How LLMs Lose the Thread in Multi-Turn Interaction\", \"authors\": \"Dongre and Hsieh and Lai and Yoon and Bui and Hakkani-Tur\", \"year\": \"2026\", \"issue\": \"duplicate\"}, {\"key\": \"levy2025lost\", \"type\": \"article\", \"title\": \"LLMs Get Lost In Multi-Turn Conversation\", \"authors\": \"Levy and others\", \"year\": \"2025\", \"issue\": \"duplicate\"}, {\"key\": \"liu2026intent\", \"type\": \"article\", \"title\": \"Intent Mismatch Causes LLMs to Get Lost in Multi-Turn Conversation\", \"authors\": \"Liu and others\", \"year\": \"2026\", \"issue\": \"duplicate\"}, {\"key\": \"liu2023lost\", \"type\": \"article\", \"title\": \"Lost in the Middle: How Language Models Use Long Contexts\", \"authors\": \"Liu and others\", \"year\": \"2023\", \"issue\": \"orphan\"}, {\"key\": \"anonymous2025style\", \"type\": \"article\", \"title\": \"Style Amnesia: Investigating Speaking Style Degradation and Mitigation in Multi-Turn Spoken Language Models\", \"authors\": \"Anonymous\", \"year\": \"2025\", \"issue\": \"orphan\"}, {\"key\": \"raposo2024mixture\", \"type\": \"article\", \"title\": \"Mixture-of-Depths: Dynamically Allocating Compute in Transformer-Based Language Models\", \"authors\": \"Raposo and others\", \"year\": \"2024\", \"issue\": \"duplicate\"}, {\"key\": \"schuster2022calm\", \"type\": \"inproceedings\", \"title\": \"Confident Adaptive Language Modeling\", \"authors\": \"Schuster and others\", \"year\": \"2022\", \"issue\": \"duplicate\"}, {\"key\": \"qiu2025gated\", \"type\": \"inproceedings\", \"title\": \"Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free\", \"authors\": \"Qiu and others\", \"year\": \"2025\", \"issue\": \"duplicate\"}, {\"key\": \"wang2018skipnet\", \"type\": \"inproceedings\", \"title\": \"SkipNet: Learning Dynamic Routing in Convolutional Networks\", \"authors\": \"Wang and others\", \"year\": \"2018\", \"issue\": \"orphan\"}, {\"key\": \"luo2025flexidepth\", \"type\": \"article\", \"title\": \"Adaptive Layer-skipping in Pre-trained LLMs (FlexiDepth)\", \"authors\": \"Luo and others\", \"year\": \"2025\", \"issue\": \"duplicate\"}, {\"key\": \"lawson2025skip\", \"type\": \"article\", \"title\": \"Learning to Skip the Middle Layers of Transformers\", \"authors\": \"Lawson and others\", \"year\": \"2025\", \"issue\": \"orphan\"}, {\"key\": \"press2022alibi\", \"type\": \"inproceedings\", \"title\": \"Train Short, Test Long: Attention with Linear Biases Enables Input Length Extrapolation\", \"authors\": \"Press and others\", \"year\": \"2022\", \"issue\": \"orphan\"}, {\"key\": \"chen2023positional\", \"type\": \"article\", \"title\": \"Extending Context Window of Large Language Models via Positional Interpolation\", \"authors\": \"Chen and others\", \"year\": \"2023\", \"issue\": \"orphan\"}, {\"key\": \"peng2024yarn\", \"type\": \"inproceedings\", \"title\": \"YaRN: Efficient Context Window Extension of Large Language Models\", \"authors\": \"Peng and others\", \"year\": \"2024\", \"issue\": \"orphan\"}, {\"key\": \"xiao2024streaming\", \"type\": \"inproceedings\", \"title\": \"Efficient Streaming Language Models with Attention Sinks\", \"authors\": \"Xiao and others\", \"year\": \"2024\", \"issue\": \"duplicate\"}, {\"key\": \"han2024lminfinite\", \"type\": \"inproceedings\", \"title\": \"LM-Infinite: Zero-Shot Extreme Length Generalization for Large Language Models\", \"authors\": \"Han and others\", \"year\": \"2024\", \"issue\": \"orphan\"}, {\"key\": \"ko2024found\", \"type\": \"article\", \"title\": \"Found in the Middle: Calibrating Positional Attention Bias Improves Long Context Utilization\", \"authors\": \"Ko and others\", \"year\": \"2024\", \"issue\": \"duplicate\"}, {\"key\": \"elhage2021framework\", \"type\": \"article\", \"title\": \"A Mathematical Framework for Transformer Circuits\", \"authors\": \"Elhage and others\", \"year\": \"2021\", \"issue\": \"orphan\"}, {\"key\": \"elhage2022superposition\", \"type\": \"article\", \"title\": \"Toy Models of Superposition\", \"authors\": \"Elhage and others\", \"year\": \"2022\", \"issue\": \"orphan\"}, {\"key\": \"belrose2023tuned\", \"type\": \"article\", \"title\": \"Eliciting Latent Predictions from Transformers with the Tuned Lens\", \"authors\": \"Belrose and others\", \"year\": \"2023\", \"issue\": \"orphan\"}, {\"key\": \"yu2023residual\", \"type\": \"article\", \"title\": \"Exploring the Residual Stream of Transformers\", \"authors\": \"Yu and others\", \"year\": \"2023\", \"issue\": \"orphan\"}, {\"key\": \"makkuva2025markov\", \"type\": \"inproceedings\", \"title\": \"Attention with Markov: A Framework for Principled Analysis of Transformers via Markov Chains\", \"authors\": \"Makkuva and others\", \"year\": \"2025\", \"issue\": \"orphan\"}, {\"key\": \"ildiz2024markov\", \"type\": \"inproceedings\", \"title\": \"From Self-Attention to Markov Models: Unveiling the Dynamics of Generative Transformers\", \"authors\": \"Ildiz and others\", \"year\": \"2024\", \"issue\": \"orphan\"}, {\"key\": \"zheng2023mtbench\", \"type\": \"inproceedings\", \"title\": \"Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena\", \"authors\": \"Zheng and others\", \"year\": \"2023\", \"issue\": \"orphan\"}, {\"key\": \"chiang2024arena\", \"type\": \"inproceedings\", \"title\": \"Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference\", \"authors\": \"Chiang and others\", \"year\": \"2024\", \"issue\": \"orphan\"}, {\"key\": \"dubois2024alpacaeval\", \"type\": \"inproceedings\", \"title\": \"Length-Controlled AlpacaEval: A Simple Way to Debias Automatic Evaluators\", \"authors\": \"Dubois and others\", \"year\": \"2024\", \"issue\": \"orphan\"}, {\"key\": \"lin2024wildbench\", \"type\": \"article\", \"title\": \"WildBench: Benchmarking LLMs with Challenging Tasks from Real Users in the Wild\", \"authors\": \"Lin and others\", \"year\": \"2024\", \"issue\": \"orphan\"}, {\"key\": \"bai2024mtbench101\", \"type\": \"inproceedings\", \"title\": \"MT-Bench-101: A Fine-Grained Benchmark for Evaluating Large Language Models in Multi-Turn Dialogues\", \"authors\": \"Bai and others\", \"year\": \"2024\", \"issue\": \"duplicate\"}, {\"key\": \"sirdeshmukh2025multichallenge\", \"type\": \"article\", \"title\": \"MultiChallenge: A Realistic Multi-Turn Conversation Evaluation Benchmark Challenging to Frontier LLMs\", \"authors\": \"Sirdeshmukh and others\", \"year\": \"2025\", \"issue\": \"orphan\"}, {\"key\": \"bengio2015scheduled\", \"type\": \"inproceedings\", \"title\": \"Scheduled Sampling for Sequence Prediction with Recurrent Neural Networks\", \"authors\": \"Bengio and Vinyals and Jaitly and Shazeer\", \"year\": \"2015\", \"issue\": \"duplicate\"}, {\"key\": \"ranzato2016sequence\", \"type\": \"inproceedings\", \"title\": \"Sequence Level Training with Recurrent Neural Networks\", \"authors\": \"Ranzato and Chopra and Auli and Zaremba\", \"year\": \"2016\", \"issue\": \"duplicate\"}, {\"key\": \"lamb2016professor\", \"type\": \"inproceedings\", \"title\": \"Professor Forcing: A New Algorithm for Training Recurrent Networks\", \"authors\": \"Lamb and Goyal and Zhang and Zhang and Courville and Bengio\", \"year\": \"2016\", \"issue\": \"duplicate\"}, {\"key\": \"leblond2018searnn\", \"type\": \"inproceedings\", \"title\": \"SEARNN: Training RNNs with Global-Local Losses\", \"authors\": \"Leblond and Alayrac and Osokin and Lacoste-Julien\", \"year\": \"2018\", \"issue\": \"duplicate\"}, {\"key\": \"he2019exposure\", \"type\": \"article\", \"title\": \"Quantifying Exposure Bias for Neural Language Generation\", \"authors\": \"He and Zhang and Zhou and Glass\", \"year\": \"2019\", \"issue\": \"duplicate\"}, {\"key\": \"yu2020pcgrad\", \"type\": \"inproceedings\", \"title\": \"Gradient Surgery for Multi-Task Learning\", \"authors\": \"Yu and Kumar and Gupta and Levine and Hausman and Finn\", \"year\": \"2020\", \"issue\": \"duplicate\"}, {\"key\": \"chen2018gradnorm\", \"type\": \"inproceedings\", \"title\": \"GradNorm: Gradient Normalization for Adaptive Loss Balancing in Deep Multitask Networks\", \"authors\": \"Chen and Badrinarayanan and Lee and Rabinovich\", \"year\": \"2018\", \"issue\": \"duplicate\"}, {\"key\": \"liu2021cagrad\", \"type\": \"inproceedings\", \"title\": \"Conflict-Averse Gradient Descent for Multi-task Learning\", \"authors\": \"Liu and Liu and Jin and Stone and Liu\", \"year\": \"2021\", \"issue\": \"duplicate\"}, {\"key\": \"navon2022nash\", \"type\": \"inproceedings\", \"title\": \"Multi-Task Learning as a Bargaining Game\", \"authors\": \"Navon and Shamsian and Achituve and Maron and Kawaguchi and Chechik and Fetaya\", \"year\": \"2022\", \"issue\": \"duplicate\"}, {\"key\": \"bachlechner2021rezero\", \"type\": \"inproceedings\", \"title\": \"ReZero is All You Need: Fast Convergence at Large Depth\", \"authors\": \"Bachlechner and Majumder and Mao and Cottrell and McAuley\", \"year\": \"2021\", \"issue\": \"duplicate\"}, {\"key\": \"zhang2019fixup\", \"type\": \"inproceedings\", \"title\": \"Fixup Initialization: Residual Learning Without Normalization\", \"authors\": \"Zhang and Dauphin and Ma\", \"year\": \"2019\", \"issue\": \"orphan\"}], \"duplicate_keys\": {\"gromov2024deeper\": [\"inproceedings\", \"inproceedings\"], \"men2024shortgpt\": [\"article\", \"article\"], \"sun2025curse\": [\"inproceedings\", \"inproceedings\"], \"anonymous2024reassessing\": [\"article\", \"article\"], \"fan2020layerdrop\": [\"inproceedings\", \"inproceedings\"], \"dongre2026attention\": [\"article\", \"article\"], \"levy2025lost\": [\"article\", \"article\"], \"liu2026intent\": [\"article\", \"article\"], \"liu2023lost\": [\"article\", \"article\"], \"anonymous2025style\": [\"article\", \"article\"], \"raposo2024mixture\": [\"article\", \"article\"], \"schuster2022calm\": [\"inproceedings\", \"inproceedings\"], \"qiu2025gated\": [\"inproceedings\", \"inproceedings\"], \"wang2018skipnet\": [\"inproceedings\", \"inproceedings\"], \"luo2025flexidepth\": [\"article\", \"article\"], \"lawson2025skip\": [\"article\", \"article\"], \"press2022alibi\": [\"inproceedings\", \"inproceedings\"], \"chen2023positional\": [\"article\", \"article\"], \"peng2024yarn\": [\"inproceedings\", \"inproceedings\"], \"xiao2024streaming\": [\"inproceedings\", \"inproceedings\"], \"han2024lminfinite\": [\"inproceedings\", \"inproceedings\"], \"ko2024found\": [\"article\", \"article\"], \"elhage2021framework\": [\"article\", \"article\"], \"elhage2022superposition\": [\"article\", \"article\"], \"belrose2023tuned\": [\"article\", \"article\"], \"yu2023residual\": [\"article\", \"article\"], \"makkuva2025markov\": [\"inproceedings\", \"inproceedings\"], \"ildiz2024markov\": [\"inproceedings\", \"inproceedings\"], \"zheng2023mtbench\": [\"inproceedings\", \"inproceedings\"], \"chiang2024arena\": [\"inproceedings\", \"inproceedings\"], \"dubois2024alpacaeval\": [\"inproceedings\", \"inproceedings\"], \"lin2024wildbench\": [\"article\", \"article\"], \"bai2024mtbench101\": [\"inproceedings\", \"inproceedings\"], \"sirdeshmukh2025multichallenge\": [\"article\", \"article\"], \"bengio2015scheduled\": [\"inproceedings\", \"inproceedings\"], \"ranzato2016sequence\": [\"inproceedings\", \"inproceedings\"], \"lamb2016professor\": [\"inproceedings\", \"inproceedings\"], \"leblond2018searnn\": [\"inproceedings\", \"inproceedings\"], \"he2019exposure\": [\"article\", \"article\"], \"yu2020pcgrad\": [\"inproceedings\", \"inproceedings\"], \"chen2018gradnorm\": [\"inproceedings\", \"inproceedings\"], \"liu2021cagrad\": [\"inproceedings\", \"inproceedings\"], \"navon2022nash\": [\"inproceedings\", \"inproceedings\"], \"bachlechner2021rezero\": [\"inproceedings\", \"inproceedings\"], \"zhang2019fixup\": [\"inproceedings\", \"inproceedings\"]}, \"online_problems\": [{\"key\": \"anonymous2024reassessing\", \"title\": \"Reassessing Layer Pruning in LLMs: New Insights and Methods\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Reassessing Layer Pruning in LLMs: New Insights and Methods\", \"matched_year\": \"2024\", \"mismatch_fields\": [\"first_author: bib=anonymous vs api=lu\"], \"note\": \"\", \"source\": \"openalex\"}, {\"key\": \"fan2020layerdrop\", \"title\": \"Reducing Transformer Depth on Demand with Structured Dropout (LayerDrop)\", \"status\": \"not_found\", \"confidence\": 0.299, \"matched_title\": \"DeeBERT: Dynamic Early Exiting for Accelerating BERT Inference\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.30 below threshold 0.82\", \"source\": \"openalex\"}, {\"key\": \"levy2025lost\", \"title\": \"LLMs Get Lost In Multi-Turn Conversation\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"LLMs Get Lost In Multi-Turn Conversation\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"first_author: bib=levy vs api=laban\"], \"note\": \"\", \"source\": \"openalex\"}, {\"key\": \"anonymous2025style\", \"title\": \"Style Amnesia: Investigating Speaking Style Degradation and Mitigation in Multi-Turn Spoken Language Models\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Style Amnesia: Investigating Speaking Style Degradation and Mitigation in Multi-Turn Spoken Language Models\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"first_author: bib=anonymous vs api=lin\"], \"note\": \"\", \"source\": \"openalex\"}, {\"key\": \"schuster2022calm\", \"title\": \"Confident Adaptive Language Modeling\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Confident Adaptive Language Modeling\", \"matched_year\": \"2022\", \"mismatch_fields\": [\"first_author: bib=schuster vs api=bahri\"], \"note\": \"\", \"source\": \"crossref_search\"}, {\"key\": \"luo2025flexidepth\", \"title\": \"Adaptive Layer-skipping in Pre-trained LLMs (FlexiDepth)\", \"status\": \"not_found\", \"confidence\": 0.409, \"matched_title\": \"Dr.LLM: Dynamic Layer Routing in LLMs\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.41 below threshold 0.82\", \"source\": \"openalex\"}, {\"key\": \"chen2023positional\", \"title\": \"Extending Context Window of Large Language Models via Positional Interpolation\", \"status\": \"mismatch\", \"confidence\": 0.838, \"matched_title\": \"PSC: Extending Context Window of Large Language Models via Phase Shift Calibration\", \"matched_year\": \"2024\", \"mismatch_fields\": [\"first_author: bib=chen vs api=zhu\"], \"note\": \"\", \"source\": \"crossref_search\"}, {\"key\": \"xiao2024streaming\", \"title\": \"Efficient Streaming Language Models with Attention Sinks\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Efficient Streaming Language Models with Attention Sinks\", \"matched_year\": \"2023\", \"mismatch_fields\": [\"first_author: bib=xiao vs api=leonardo\"], \"note\": \"\", \"source\": \"openalex\"}, {\"key\": \"ko2024found\", \"title\": \"Found in the Middle: Calibrating Positional Attention Bias Improves Long Context Utilization\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Found in the middle: Calibrating Positional Attention Bias Improves Long Context Utilization\", \"matched_year\": \"2024\", \"mismatch_fields\": [\"first_author: bib=ko vs api=hsieh\"], \"note\": \"\", \"source\": \"crossref_search\"}, {\"key\": \"elhage2021framework\", \"title\": \"A Mathematical Framework for Transformer Circuits\", \"status\": \"not_found\", \"confidence\": 0.219, \"matched_title\": \"Review of deep learning: concepts, CNN architectures, challenges, applications, future directions\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.22 below threshold 0.82\", \"source\": \"openalex\"}, {\"key\": \"yu2023residual\", \"title\": \"Exploring the Residual Stream of Transformers\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Neuron-Level Knowledge Attribution in Large Language Models\", \"matched_year\": \"2023\", \"mismatch_fields\": [\"title: similarity=0.21 (possible wrong arXiv ID)\"], \"note\": \"\", \"source\": \"arxiv\"}, {\"key\": \"he2019exposure\", \"title\": \"Quantifying Exposure Bias for Neural Language Generation\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Exposure Bias versus Self-Recovery: Are Distortions Really Incremental for Autoregressive Text Generation?\", \"matched_year\": \"2019\", \"mismatch_fields\": [\"title: similarity=0.41 (possible wrong arXiv ID)\"], \"note\": \"\", \"source\": \"arxiv\"}, {\"key\": \"grattafiori2024llama3\", \"title\": \"The Llama 3 Herd of Models\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"The Llama 3 herd of models\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"first_author: bib=grattafiori vs api=aaron\"], \"note\": \"\", \"source\": \"openalex\"}]}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 18_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the results. The tool found:
- 91 total bib entries (but only 46 unique - there are 45 duplicate keys, meaning the bib file is likely included twice or there are duplicate entries)
- 22 unique cited keys
- 24 orphan entries (in bib but not cited)
- 0 missing entries (cited but not in bib)
- Online: 33 verified, 3 not_found, 10 mismatch

Wait, the bib file I read only has ~46 entries. 

So the 91 total with 45 duplicates suggests there's a second bib file or the same file is being included twice. Looking at the specific issues, three entries couldn't be verified in OpenAlex: `fan2020layerdrop` about LayerDrop, `luo2025flexidepth` about FlexiDepth, and `elhage2021framework` which is actually a blog post rather than a published paper.

Beyond those, there are ten entries with mismatches between what's in the bib file and what the API found. Most are author name discrepancies—like `anonymous2024reassessing` should be attributed to Lu, `levy2025lost` to Laban, and `anonymous2025style` to Lin. A few have year or title issues that might stem from incorrect arXiv IDs or Crossref data, and one entry for `grattafiori2024llama3` appears to have the wrong year.

I'm also noticing there are 24 orphan entries that exist in the bib file but aren't cited anywhere, and 45 duplicate keys suggesting the bib file might be duplicated somewhere in the project. I should search the web to verify the problematic entries and track down whether there's a second copy of the bibliography file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "652e1b48-5425-4360-9d09-b4c254656213",
  "uuid": "8ad41187-d2e8-4a82-9feb-6418b339a02e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DmGBQBiwfWbqJikqCBDeNc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10422,
      "cache_read_input_tokens": 34284,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10422
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

工具返回了初步结果。发现 45 个重复 key（可能有第二份 bib 文件）、3 个 not_found、10 个 mismatch。让我检查是否有多个 bib 文件，并对问题条目做 WebSearch 验证。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "652e1b48-5425-4360-9d09-b4c254656213",
  "uuid": "24a5b6c6-82f9-4934-915a-e627a18a215f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DmGBQBiwfWbqJikqCBDeNc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10422,
      "cache_read_input_tokens": 34284,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10422
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

<details open><summary>🔧 Tool call — Glob · `toolu_01WKfftitm1znVQ2sCFdTCvA`</summary>

```json
{
  "pattern": "**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "652e1b48-5425-4360-9d09-b4c254656213",
  "uuid": "7cb7ffa6-6910-41c4-9cbe-c2733b62eda3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DmGBQBiwfWbqJikqCBDeNc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10422,
      "cache_read_input_tokens": 34284,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10422
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

_source line 21 · 2026-05-22T04:36:58.103Z_

<details><summary>↩ Tool result · `toolu_01WKfftitm1znVQ2sCFdTCvA`</summary>

```text
paper/sections/references.bib
paper/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "652e1b48-5425-4360-9d09-b4c254656213",
  "uuid": "938d6907-754f-4276-acf8-157b23e52f3a",
  "tool_use_result": {
    "filenames": [
      "paper/sections/references.bib",
      "paper/references.bib"
    ],
    "durationMs": 16,
    "numFiles": 2,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 22_

<details open><summary>🔧 Tool call — Grep · `toolu_01HfQX3Z6pGGMYcjcrZ4TrH9`</summary>

```json
{
  "pattern": "\\\\bibliography\\{|\\\\addbibresource",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper",
  "output_mode": "content",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "652e1b48-5425-4360-9d09-b4c254656213",
  "uuid": "198d0ed9-74a7-44c9-b5f6-61c1e5c420ba",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DmGBQBiwfWbqJikqCBDeNc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10422,
      "cache_read_input_tokens": 34284,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10422
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

_source line 23 · 2026-05-22T04:36:59.269Z_

<details><summary>↩ Tool result · `toolu_01HfQX3Z6pGGMYcjcrZ4TrH9`</summary>

```text
paper/main.tex:38:\bibliography{references}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "652e1b48-5425-4360-9d09-b4c254656213",
  "uuid": "9d9caba9-2414-4e2c-9823-c4638f03438f",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "paper/main.tex:38:\\bibliography{references}",
    "numLines": 1
  }
}
```

</details>

---

### Assistant

_source line 24_

<details><summary>Logged reasoning block</summary>

```text
There are two bib files - `paper/references.bib` and `paper/sections/references.bib`. The main.tex references `\bibliography{references}` which points to `paper/references.bib`. The `paper/sections/references.bib` is likely a duplicate. That explains the 45 duplicate keys.

Now let me do WebSearch for the problematic entries. Let me focus on:
1. Not Found: fan2020layerdrop, luo2025flexidepth, elhage2021framework
2. Mismatch with potential issues: yu2023residual (arXiv ID wrong), he2019exposure (arXiv ID wrong), levy2025lost (author wrong), anonymous2024reassessing (should have real author), anonymous2025style (should have real author), ko2024found (author wrong), xiao2024streaming (year wrong), chen2023positional (may have matched wrong paper), schuster2022calm (author issue), grattafiori2024llama3 (year wrong)


I'll run WebSearch queries in parallel for the most critical entries to verify and correct the metadata.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "652e1b48-5425-4360-9d09-b4c254656213",
  "uuid": "a57f8abc-90e8-4a9a-b5c9-700ea8642d49",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D8rnq1ZcnsbvBLtZ1HyrgM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1137,
      "cache_read_input_tokens": 44706,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1137
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

_source line 25_

两份 bib 文件（`paper/references.bib` 和 `paper/sections/references.bib`）导致 45 个 duplicate。`main.tex` 只引用 `paper/references.bib`。

现在对 13 个问题条目做 WebSearch 验证。分批并行搜索。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "652e1b48-5425-4360-9d09-b4c254656213",
  "uuid": "92ff2f17-aaa9-44eb-b924-237de20e4950",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D8rnq1ZcnsbvBLtZ1HyrgM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1137,
      "cache_read_input_tokens": 44706,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1137
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

_source line 26_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01XWuHLqPU5UHsjBTwVNetvG`</summary>

```json
{
  "query": "select:WebSearch",
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
  "session_id": "652e1b48-5425-4360-9d09-b4c254656213",
  "uuid": "355f04d1-50ca-4f42-a42c-e988d8dec6da",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D8rnq1ZcnsbvBLtZ1HyrgM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1137,
      "cache_read_input_tokens": 44706,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1137
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

_source line 27 · 2026-05-22T04:37:07.598Z_

<details><summary>↩ Tool result · `toolu_01XWuHLqPU5UHsjBTwVNetvG`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
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
  "session_id": "652e1b48-5425-4360-9d09-b4c254656213",
  "uuid": "72e7b6e6-3de6-4511-ab0d-5b4ed2c9e916",
  "tool_use_result": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 23
  }
}
```

</details>

---

### Assistant

_source line 28_

<details><summary>Logged reasoning block</summary>

```text
Now let me do WebSearch for the problematic entries. I'll batch them into parallel searches.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "652e1b48-5425-4360-9d09-b4c254656213",
  "uuid": "855e8062-6569-45e9-81e3-02d77df8dbc2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NDvZnMYhYCvL9X3FvJdkkZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 954,
      "cache_read_input_tokens": 45843,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 954
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

_source line 29_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Y4QqAuYTLzBFJPDShFTERP`</summary>

```json
{
  "query": "LayerDrop \"Reducing Transformer Depth on Demand with Structured Dropout\" Fan 2020"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "652e1b48-5425-4360-9d09-b4c254656213",
  "uuid": "d26e3e8b-5903-48fb-beeb-26f733994f80",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NDvZnMYhYCvL9X3FvJdkkZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 954,
      "cache_read_input_tokens": 45843,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 954
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

_source line 30_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TfZzvYGgjgTpbyPMDdgASW`</summary>

```json
{
  "query": "FlexiDepth \"Adaptive Layer-skipping in Pre-trained LLMs\" Luo 2025 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "652e1b48-5425-4360-9d09-b4c254656213",
  "uuid": "af63173c-287a-4a44-a820-a47be4ac56ee",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NDvZnMYhYCvL9X3FvJdkkZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 954,
      "cache_read_input_tokens": 45843,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 954
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

_source line 31_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MD32yM7YsxxuDNvuhvpraQ`</summary>

```json
{
  "query": "\"A Mathematical Framework for Transformer Circuits\" Elhage Anthropic 2021"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "652e1b48-5425-4360-9d09-b4c254656213",
  "uuid": "e129c09f-c5d7-40ac-ab95-872aeb4ac79c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NDvZnMYhYCvL9X3FvJdkkZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 954,
      "cache_read_input_tokens": 45843,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 954
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

_source line 32_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WhcFehyVyggRdoZtNCSzYN`</summary>

```json
{
  "query": "\"Exploring the Residual Stream of Transformers\" arXiv 2312.12141"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "652e1b48-5425-4360-9d09-b4c254656213",
  "uuid": "6ea386a3-cfef-4791-8c37-8f00c9f9b558",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NDvZnMYhYCvL9X3FvJdkkZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 954,
      "cache_read_input_tokens": 45843,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 954
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

_source line 33_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WWofUTt3Ej2qYr7Lttb5Z1`</summary>

```json
{
  "query": "\"Quantifying Exposure Bias for Neural Language Generation\" He 2019 arXiv 1905.10617"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "652e1b48-5425-4360-9d09-b4c254656213",
  "uuid": "8cbff9c4-1258-4f64-9fea-5dff136b44da",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NDvZnMYhYCvL9X3FvJdkkZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 954,
      "cache_read_input_tokens": 45843,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 954
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

_source line 34_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014u2qprE9sp174EPJ1qiysR`</summary>

```json
{
  "query": "\"LLMs Get Lost In Multi-Turn Conversation\" 2025 arXiv first author"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "652e1b48-5425-4360-9d09-b4c254656213",
  "uuid": "f3ba826a-5224-4217-811e-46e8f8015da7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NDvZnMYhYCvL9X3FvJdkkZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 954,
      "cache_read_input_tokens": 45843,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 954
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

_source line 35_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014QufV9iWY5ZsD7nWQZHYWT`</summary>

```json
{
  "query": "\"Found in the Middle: Calibrating Positional Attention Bias\" first author 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "652e1b48-5425-4360-9d09-b4c254656213",
  "uuid": "90482471-8eb4-4424-ae74-0254df8ed573",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NDvZnMYhYCvL9X3FvJdkkZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 954,
      "cache_read_input_tokens": 45843,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 954
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

_source line 36 · 2026-05-22T04:37:17.361Z_

<details><summary>↩ Tool result · `toolu_01Y4QqAuYTLzBFJPDShFTERP`</summary>

```text
Web search results for query: "LayerDrop "Reducing Transformer Depth on Demand with Structured Dropout" Fan 2020"

Links: [{"title":"LayerDrop: Reducing Transformer Depth on Demand | SERP AI","url":"https://serp.ai/posts/layerdrop/"},{"title":"[1909.11556] Reducing Transformer Depth on Demand with Structured Dropout","url":"https://arxiv.org/abs/1909.11556"},{"title":"Reducing Transformer Depth on Demand with Structured Dropout | Request PDF","url":"https://www.researchgate.net/publication/336056561_Reducing_Transformer_Depth_on_Demand_with_Structured_Dropout"},{"title":"Reducing Transformer Depth on Demand with Structured Dropout","url":"https://papertalk.org/papertalks/4168"},{"title":"Reducing Transformer Depth on Demand with Structured Dropout | OpenReview","url":"https://openreview.net/forum?id=SylO2yStDr"},{"title":"Paper page - Reducing Transformer Depth on Demand with Structured Dropout","url":"https://huggingface.co/papers/1909.11556"},{"title":"REDUCING TRANSFORMER DEPTH ON DEMAND WITH STRUCTURED DROPOUT Angela Fan","url":"https://arxiv.org/pdf/1909.11556"},{"title":"ICLR: Reducing Transformer Depth on Demand with Structured Dropout","url":"https://iclr.cc/virtual_2020/poster_SylO2yStDr.html"},{"title":"Dropout layers, not weights or nodes! \"LayerDrop\" proposal | AI-SCHOLAR | AI: (Artificial Intelligence) Articles and technical information media","url":"https://ai-scholar.tech/en/articles/dropout/LayerDrop"}]

I found several comprehensive sources about the LayerDrop paper. Here's what the search results show:

## Overview

LayerDrop is a form of structured dropout which has a regularization effect during training and allows for efficient pruning at inference time. The paper was published at the ICLR 2020 virtual conference.

## Key Findings

The technique enables selecting sub-networks of any depth from one large network without having to finetune them and with limited impact on performance. LayerDrop applies structured dropout directly to the Transformer layers, maintaining computational simplicity while achieving significant model compression.

## Applications and Results

The approach demonstrates effectiveness by improving the state of the art on machine translation, language modeling, summarization, question answering, and language understanding benchmarks. Additionally, the approach leads to small BERT-like models of higher quality than when training from scratch or using distillation.

## Technical Details

During training, it employs an "every other" strategy that drops layers at a constant 10% pruning rate, effectively preventing overfitting and improving generalization.

The paper was authored by Angela Fan, Edouard Grave, and Armand Joulin, with the original submission on September 25, 2019.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "652e1b48-5425-4360-9d09-b4c254656213",
  "uuid": "450a3cb7-59d7-45ab-a960-82961a6d2e10",
  "tool_use_result": {
    "query": "LayerDrop \"Reducing Transformer Depth on Demand with Structured Dropout\" Fan 2020",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Ej64uiv2qZveyqBx6Jnvgg",
        "content": [
          {
            "title": "LayerDrop: Reducing Transformer Depth on Demand | SERP AI",
            "url": "https://serp.ai/posts/layerdrop/"
          },
          {
            "title": "[1909.11556] Reducing Transformer Depth on Demand with Structured Dropout",
            "url": "https://arxiv.org/abs/1909.11556"
          },
          {
            "title": "Reducing Transformer Depth on Demand with Structured Dropout | Request PDF",
            "url": "https://www.researchgate.net/publication/336056561_Reducing_Transformer_Depth_on_Demand_with_Structured_Dropout"
          },
          {
            "title": "Reducing Transformer Depth on Demand with Structured Dropout",
            "url": "https://papertalk.org/papertalks/4168"
          },
          {
            "title": "Reducing Transformer Depth on Demand with Structured Dropout | OpenReview",
            "url": "https://openreview.net/forum?id=SylO2yStDr"
          },
          {
            "title": "Paper page - Reducing Transformer Depth on Demand with Structured Dropout",
            "url": "https://huggingface.co/papers/1909.11556"
          },
          {
            "title": "REDUCING TRANSFORMER DEPTH ON DEMAND WITH STRUCTURED DROPOUT Angela Fan",
            "url": "https://arxiv.org/pdf/1909.11556"
          },
          {
            "title": "ICLR: Reducing Transformer Depth on Demand with Structured Dropout",
            "url": "https://iclr.cc/virtual_2020/poster_SylO2yStDr.html"
          },
          {
            "title": "Dropout layers, not weights or nodes! \"LayerDrop\" proposal | AI-SCHOLAR | AI: (Artificial Intelligence) Articles and technical information media",
            "url": "https://ai-scholar.tech/en/articles/dropout/LayerDrop"
          }
        ]
      },
      "I found several comprehensive sources about the LayerDrop paper. Here's what the search results show:\n\n## Overview\n\nLayerDrop is a form of structured dropout which has a regularization effect during training and allows for efficient pruning at inference time. The paper was published at the ICLR 2020 virtual conference.\n\n## Key Findings\n\nThe technique enables selecting sub-networks of any depth from one large network without having to finetune them and with limited impact on performance. LayerDrop applies structured dropout directly to the Transformer layers, maintaining computational simplicity while achieving significant model compression.\n\n## Applications and Results\n\nThe approach demonstrates effectiveness by improving the state of the art on machine translation, language modeling, summarization, question answering, and language understanding benchmarks. Additionally, the approach leads to small BERT-like models of higher quality than when training from scratch or using distillation.\n\n## Technical Details\n\nDuring training, it employs an \"every other\" strategy that drops layers at a constant 10% pruning rate, effectively preventing overfitting and improving generalization.\n\nThe paper was authored by Angela Fan, Edouard Grave, and Armand Joulin, with the original submission on September 25, 2019."
    ],
    "durationSeconds": 5.734889089000004
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-22T04:37:18.192Z_

<details><summary>↩ Tool result · `toolu_01TfZzvYGgjgTpbyPMDdgASW`</summary>

```text
Web search results for query: "FlexiDepth "Adaptive Layer-skipping in Pre-trained LLMs" Luo 2025 arXiv"

Links: [{"title":"[2503.23798] Adaptive Layer-skipping in Pre-trained LLMs","url":"https://arxiv.org/abs/2503.23798"},{"title":"Adaptive Layer-skipping in Pre-trained LLMs - Paper Reading","url":"http://paperreading.club/page?id=296091"},{"title":"Adaptive Layer-skipping in Pre-trained LLMs Xuan Luo, Weizhi Wang, Xifeng Yan","url":"https://arxiv.org/pdf/2503.23798"},{"title":"Adaptive Layer-skipping in Pre-trained LLMs","url":"https://arxiv.org/html/2503.23798v1"},{"title":"GitHub - luoxuan-cs/Flexidepth: The official repo for the paper \"Adaptive Layer-skipping in Pre-trained LLMs\" · GitHub","url":"https://github.com/luoxuan-cs/Flexidepth"},{"title":"Adaptive Layer-skipping in Pre-trained LLMs - Xuan Luo","url":"https://luoxuan-cs.github.io/flexidepth/"},{"title":"Adaptive Layer-skipping in Pre-trained LLMs","url":"https://openreview.net/pdf?id=Gu0XSax2YS"},{"title":"Adaptive Layer-skipping in Pre-trained LLMs | OpenReview","url":"https://openreview.net/forum?id=Gu0XSax2YS"},{"title":"Adaptive Layer-skipping in Pre-trained LLMs | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/adaptive-layer-skipping-pre-trained-llms"},{"title":"Adaptive Inference in Pre-trained LLMs Layer-skipping","url":"https://sites.cs.ucsb.edu/~xyan/presentation/Colm2025_Adaptive.pdf"}]

I found comprehensive information about the FlexiDepth paper. Here's what the search revealed:

## Overview

FlexiDepth is a method that dynamically adjusts the number of Transformer layers used in text generation by incorporating a plug-in router and adapter, enabling adaptive computation in LLMs without modifying their original parameters.

## Key Results

Applied to Llama-3-8B, it skips 8 out of 32 layers while maintaining full benchmark performance.

## Main Findings

Computational demands in LLMs significantly vary based on token type, with generating repetitive tokens or fixed phrases requiring fewer layers, whereas producing tokens involving computation or high uncertainty requiring more layers.

## Authors and Publication

The paper is by Xuan Luo, Weizhi Wang, and Xifeng Yan from UC Santa Barbara. The paper was first submitted on March 31, 2025, with the most recent version dated October 8, 2025.

## Open Source Release

The authors open-sourced FlexiDepth and a dataset documenting its layer allocation patterns. The official repository is available on GitHub at `github.com/luoxuan-cs/Flexidepth`.

The paper is available on arXiv at: https://arxiv.org/abs/2503.23798


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "652e1b48-5425-4360-9d09-b4c254656213",
  "uuid": "d1aa1f7d-7444-48fd-93e7-7f27f87464c5",
  "tool_use_result": {
    "query": "FlexiDepth \"Adaptive Layer-skipping in Pre-trained LLMs\" Luo 2025 arXiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_011ex41dBi95fdEdQbKH4Qx9",
        "content": [
          {
            "title": "[2503.23798] Adaptive Layer-skipping in Pre-trained LLMs",
            "url": "https://arxiv.org/abs/2503.23798"
          },
          {
            "title": "Adaptive Layer-skipping in Pre-trained LLMs - Paper Reading",
            "url": "http://paperreading.club/page?id=296091"
          },
          {
            "title": "Adaptive Layer-skipping in Pre-trained LLMs Xuan Luo, Weizhi Wang, Xifeng Yan",
            "url": "https://arxiv.org/pdf/2503.23798"
          },
          {
            "title": "Adaptive Layer-skipping in Pre-trained LLMs",
            "url": "https://arxiv.org/html/2503.23798v1"
          },
          {
            "title": "GitHub - luoxuan-cs/Flexidepth: The official repo for the paper \"Adaptive Layer-skipping in Pre-trained LLMs\" · GitHub",
            "url": "https://github.com/luoxuan-cs/Flexidepth"
          },
          {
            "title": "Adaptive Layer-skipping in Pre-trained LLMs - Xuan Luo",
            "url": "https://luoxuan-cs.github.io/flexidepth/"
          },
          {
            "title": "Adaptive Layer-skipping in Pre-trained LLMs",
            "url": "https://openreview.net/pdf?id=Gu0XSax2YS"
          },
          {
            "title": "Adaptive Layer-skipping in Pre-trained LLMs | OpenReview",
            "url": "https://openreview.net/forum?id=Gu0XSax2YS"
          },
          {
            "title": "Adaptive Layer-skipping in Pre-trained LLMs | AI Research Paper Details",
            "url": "https://www.aimodels.fyi/papers/arxiv/adaptive-layer-skipping-pre-trained-llms"
          },
          {
            "title": "Adaptive Inference in Pre-trained LLMs Layer-skipping",
            "url": "https://sites.cs.ucsb.edu/~xyan/presentation/Colm2025_Adaptive.pdf"
          }
        ]
      },
      "I found comprehensive information about the FlexiDepth paper. Here's what the search revealed:\n\n## Overview\n\nFlexiDepth is a method that dynamically adjusts the number of Transformer layers used in text generation by incorporating a plug-in router and adapter, enabling adaptive computation in LLMs without modifying their original parameters.\n\n## Key Results\n\nApplied to Llama-3-8B, it skips 8 out of 32 layers while maintaining full benchmark performance.\n\n## Main Findings\n\nComputational demands in LLMs significantly vary based on token type, with generating repetitive tokens or fixed phrases requiring fewer layers, whereas producing tokens involving computation or high uncertainty requiring more layers.\n\n## Authors and Publication\n\nThe paper is by Xuan Luo, Weizhi Wang, and Xifeng Yan from UC Santa Barbara. The paper was first submitted on March 31, 2025, with the most recent version dated October 8, 2025.\n\n## Open Source Release\n\nThe authors open-sourced FlexiDepth and a dataset documenting its layer allocation patterns. The official repository is available on GitHub at `github.com/luoxuan-cs/Flexidepth`.\n\nThe paper is available on arXiv at: https://arxiv.org/abs/2503.23798"
    ],
    "durationSeconds": 5.621876432999969
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-22T04:37:19.506Z_

<details><summary>↩ Tool result · `toolu_01MD32yM7YsxxuDNvuhvpraQ`</summary>

```text
Web search results for query: ""A Mathematical Framework for Transformer Circuits" Elhage Anthropic 2021"

Links: [{"title":"Transformer Circuits: A Mathematical Framework","url":"https://studylib.net/doc/27496897/transformer-circui...--1-"},{"title":"Arxiv Dives - A Mathematical Framework for Transformer Circuits - Part 1","url":"https://ghost.oxen.ai/arxiv-dives-a-mathematical-framework-for-transformer-circuits/"},{"title":"Studypool Homework Help - A mathematical framework for transformer circuits","url":"https://www.studypool.com/documents/43042208/a-mathematical-framework-for-transformer-circuits"},{"title":"JongGeun Lee, Jungwoo Yang, Haesung Pyun A Mathematical Framework","url":"https://jungwooyang.com/assets/files/framework-transformer-circuits.pdf"},{"title":"A Mathematical Framework for Transformer Circuits","url":"https://www.scribd.com/document/866284321/A-Mathematical-Framework-for-Transformer-Circuits"},{"title":"1 Introduction","url":"https://arxiv.org/html/2402.02619v3"},{"title":"A Mathematical Framework for Transformer Circuits","url":"https://transformer-circuits.pub/2021/framework/index.html"},{"title":"Efficient Automated Circuit Discovery in Transformers using Contextual   Decomposition","url":"https://arxiv.org/pdf/2407.00886"},{"title":"A Mathematical Framework for Transformer Circuits \\ Anthropic","url":"https://www.anthropic.com/research/a-mathematical-framework-for-transformer-circuits"}]

Based on the search results, I found information about this paper:

The paper "A Mathematical Framework for Transformer Circuits" was authored by Nelson Elhage, Neel Nanda, Catherine Olsson, Tom Henighan, Nicholas Joseph, Ben Mann, Amanda Askell, Yuntao Bai, Anna Chen, Tom Conerly, Nova DasSarma, Dawn Drain, Deep Ganguli, Zac Hatfield-Dodds, Danny Hernandez, Andy Jones, Jackson Kernion, Liane Lovitt, Kamal Ndousse, Dario Amodei, Tom Brown, Jack Clark, Jared Kaplan, Sam McCandlish, and Chris Olah from Anthropic and was published on December 22, 2021.

The paper addresses transformer language models, which are gaining broad real-world use in systems like GPT-3, LaMDA, Codex, Meena, and Gopher. However, as these models scale, their open-endedness and high capacity create an increasing scope for unexpected and sometimes harmful behaviors.

The paper introduced a mathematical framework to represent how transformer attention heads can work with each other to implement complex algorithms. The framework supports mechanistic interpretability, which is the process of attempting to reverse engineer the detailed computations performed by transformers.

The official version of this paper is available at the Transformer Circuits website (transformer-circuits.pub/2021/framework/index.html).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "652e1b48-5425-4360-9d09-b4c254656213",
  "uuid": "1ba49cf6-23e8-4f97-bbdd-1b07a35afacc",
  "tool_use_result": {
    "query": "\"A Mathematical Framework for Transformer Circuits\" Elhage Anthropic 2021",
    "results": [
      {
        "tool_use_id": "srvtoolu_01MaF656jv8itD9hhA212hDp",
        "content": [
          {
            "title": "Transformer Circuits: A Mathematical Framework",
            "url": "https://studylib.net/doc/27496897/transformer-circui...--1-"
          },
          {
            "title": "Arxiv Dives - A Mathematical Framework for Transformer Circuits - Part 1",
            "url": "https://ghost.oxen.ai/arxiv-dives-a-mathematical-framework-for-transformer-circuits/"
          },
          {
            "title": "Studypool Homework Help - A mathematical framework for transformer circuits",
            "url": "https://www.studypool.com/documents/43042208/a-mathematical-framework-for-transformer-circuits"
          },
          {
            "title": "JongGeun Lee, Jungwoo Yang, Haesung Pyun A Mathematical Framework",
            "url": "https://jungwooyang.com/assets/files/framework-transformer-circuits.pdf"
          },
          {
            "title": "A Mathematical Framework for Transformer Circuits",
            "url": "https://www.scribd.com/document/866284321/A-Mathematical-Framework-for-Transformer-Circuits"
          },
          {
            "title": "1 Introduction",
            "url": "https://arxiv.org/html/2402.02619v3"
          },
          {
            "title": "A Mathematical Framework for Transformer Circuits",
            "url": "https://transformer-circuits.pub/2021/framework/index.html"
          },
          {
            "title": "Efficient Automated Circuit Discovery in Transformers using Contextual   Decomposition",
            "url": "https://arxiv.org/pdf/2407.00886"
          },
          {
            "title": "A Mathematical Framework for Transformer Circuits \\ Anthropic",
            "url": "https://www.anthropic.com/research/a-mathematical-framework-for-transformer-circuits"
          }
        ]
      },
      "Based on the search results, I found information about this paper:\n\nThe paper \"A Mathematical Framework for Transformer Circuits\" was authored by Nelson Elhage, Neel Nanda, Catherine Olsson, Tom Henighan, Nicholas Joseph, Ben Mann, Amanda Askell, Yuntao Bai, Anna Chen, Tom Conerly, Nova DasSarma, Dawn Drain, Deep Ganguli, Zac Hatfield-Dodds, Danny Hernandez, Andy Jones, Jackson Kernion, Liane Lovitt, Kamal Ndousse, Dario Amodei, Tom Brown, Jack Clark, Jared Kaplan, Sam McCandlish, and Chris Olah from Anthropic and was published on December 22, 2021.\n\nThe paper addresses transformer language models, which are gaining broad real-world use in systems like GPT-3, LaMDA, Codex, Meena, and Gopher. However, as these models scale, their open-endedness and high capacity create an increasing scope for unexpected and sometimes harmful behaviors.\n\nThe paper introduced a mathematical framework to represent how transformer attention heads can work with each other to implement complex algorithms. The framework supports mechanistic interpretability, which is the process of attempting to reverse engineer the detailed computations performed by transformers.\n\nThe official version of this paper is available at the Transformer Circuits website (transformer-circuits.pub/2021/framework/index.html)."
    ],
    "durationSeconds": 6.453028448999976
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-22T04:37:19.518Z_

<details><summary>↩ Tool result · `toolu_014u2qprE9sp174EPJ1qiysR`</summary>

```text
Web search results for query: ""LLMs Get Lost In Multi-Turn Conversation" 2025 arXiv first author"

Links: [{"title":"[2505.06120v1] LLMs Get Lost In Multi-Turn Conversation","url":"https://arxiv.org/abs/2505.06120v1"},{"title":"[2505.06120] LLMs Get Lost In Multi-Turn Conversation","url":"https://arxiv.org/abs/2505.06120"},{"title":"Why LLMs Fail in Multi-Turn Conversations and a Simple Fix","url":"https://www.keywordsai.co/blog/how-to-fix-it-when-llms-get-lost-in-multi-turn-conversation"},{"title":"[PDF] LLMs Get Lost In Multi-Turn Conversation | Semantic Scholar","url":"https://www.semanticscholar.org/paper/LLMs-Get-Lost-In-Multi-Turn-Conversation-Laban-Hayashi/bb5d81576c113f0b16234fd0db4238a4281c8388"},{"title":"Intent Mismatch Causes LLMs to Get Lost in Multi-Turn Conversation","url":"https://arxiv.org/html/2602.07338v1"},{"title":"[2602.07338] Intent Mismatch Causes LLMs to Get Lost in Multi-Turn Conversation","url":"https://arxiv.org/abs/2602.07338"},{"title":"Intent Mismatch Causes LLMs to Get Lost in Multi-Turn Conversation","url":"https://arxiv.org/pdf/2602.07338"}]

Based on the search results, the first author of the 2025 arXiv paper "LLMs Get Lost In Multi-Turn Conversation" is Philippe Laban. The paper was submitted on May 9, 2025 with arXiv ID 2505.06120.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "652e1b48-5425-4360-9d09-b4c254656213",
  "uuid": "b5969b9e-644f-4d43-8ac5-88068da91c7c",
  "tool_use_result": {
    "query": "\"LLMs Get Lost In Multi-Turn Conversation\" 2025 arXiv first author",
    "results": [
      {
        "tool_use_id": "srvtoolu_01EMMvfsrtHxGiKXcGJ73jmG",
        "content": [
          {
            "title": "[2505.06120v1] LLMs Get Lost In Multi-Turn Conversation",
            "url": "https://arxiv.org/abs/2505.06120v1"
          },
          {
            "title": "[2505.06120] LLMs Get Lost In Multi-Turn Conversation",
            "url": "https://arxiv.org/abs/2505.06120"
          },
          {
            "title": "Why LLMs Fail in Multi-Turn Conversations and a Simple Fix",
            "url": "https://www.keywordsai.co/blog/how-to-fix-it-when-llms-get-lost-in-multi-turn-conversation"
          },
          {
            "title": "[PDF] LLMs Get Lost In Multi-Turn Conversation | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/LLMs-Get-Lost-In-Multi-Turn-Conversation-Laban-Hayashi/bb5d81576c113f0b16234fd0db4238a4281c8388"
          },
          {
            "title": "Intent Mismatch Causes LLMs to Get Lost in Multi-Turn Conversation",
            "url": "https://arxiv.org/html/2602.07338v1"
          },
          {
            "title": "[2602.07338] Intent Mismatch Causes LLMs to Get Lost in Multi-Turn Conversation",
            "url": "https://arxiv.org/abs/2602.07338"
          },
          {
            "title": "Intent Mismatch Causes LLMs to Get Lost in Multi-Turn Conversation",
            "url": "https://arxiv.org/pdf/2602.07338"
          }
        ]
      },
      "Based on the search results, the first author of the 2025 arXiv paper \"LLMs Get Lost In Multi-Turn Conversation\" is Philippe Laban. The paper was submitted on May 9, 2025 with arXiv ID 2505.06120."
    ],
    "durationSeconds": 3.5846352390000247
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-22T04:37:20.269Z_

<details><summary>↩ Tool result · `toolu_01WhcFehyVyggRdoZtNCSzYN`</summary>

```text
Web search results for query: ""Exploring the Residual Stream of Transformers" arXiv 2312.12141"

Links: [{"title":"Exploring the Residual Stream of Transformers - Paper Reading","url":"https://paperreading.club/page?id=200769"},{"title":"[2312.12141v1] Exploring the Residual Stream of Transformers","url":"https://arxiv.org/abs/2312.12141v1"},{"title":"Exploring the Residual Stream of Transformers","url":"https://arxiv.org/html/2312.12141v1"},{"title":"Exploring the Residual Stream of Transformers | Zendy","url":"https://zendy.io/pdf-viewer/2312.12141"},{"title":"Exploring the Residual Stream of Transformers for Mechanistic Interpretability — Explained | by Zeping Yu | Medium","url":"https://medium.com/@zepingyu/123-cb62513f5d50"},{"title":"Transformers represent belief state geometry in their residual stream","url":"https://arxiv.org/pdf/2405.15943"},{"title":"Residual Streams in Transformer Models","url":"https://retr0sushi04.netlify.app/blogs/residualstreamsblog/residualstreams"},{"title":"Patterns and Messages - Part 5 - The Residual Stream · Chris McCormick","url":"https://mccormickml.com/2025/02/20/patterns-and-messages-part-5-the-residual-stream/"},{"title":"Residual Matrix Transformers: Scaling the Size of the Residual Stream","url":"https://arxiv.org/pdf/2506.22696"},{"title":"Characterizing stable regions in the residual stream of LLMs","url":"https://arxiv.org/pdf/2409.17113"}]

Based on the search results, here's what I found about the paper "Exploring the Residual Stream of Transformers" (arXiv 2312.12141):

## Overview

The paper was submitted on December 19, 2023, and authored by Zeping Yu, Kailai Yang, Zhiwei Liu, and Sophia Ananiadou.

## Research Focus

The paper explores the residual stream of transformers to increase the interpretability. The authors address the challenge of locating models' important parameters storing the knowledge for predicting the next word, and whether these parameters are stored on the same layer/module or different ones.

## Key Findings

The paper finds that the mechanism behind residual connection is a direct addition function on before-softmax values, so the probabilities of tokens with larger before-softmax values will increase. Additionally, the authors prove that using log probability increase as contribution scores is reasonable, and based on this they can locate important parameters.

The paper is available on arXiv at https://arxiv.org/abs/2312.12141.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "652e1b48-5425-4360-9d09-b4c254656213",
  "uuid": "5d7f69fc-570f-4732-b0c6-72587f02a255",
  "tool_use_result": {
    "query": "\"Exploring the Residual Stream of Transformers\" arXiv 2312.12141",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Y6EY2R7CgEyRgDBN738ChV",
        "content": [
          {
            "title": "Exploring the Residual Stream of Transformers - Paper Reading",
            "url": "https://paperreading.club/page?id=200769"
          },
          {
            "title": "[2312.12141v1] Exploring the Residual Stream of Transformers",
            "url": "https://arxiv.org/abs/2312.12141v1"
          },
          {
            "title": "Exploring the Residual Stream of Transformers",
            "url": "https://arxiv.org/html/2312.12141v1"
          },
          {
            "title": "Exploring the Residual Stream of Transformers | Zendy",
            "url": "https://zendy.io/pdf-viewer/2312.12141"
          },
          {
            "title": "Exploring the Residual Stream of Transformers for Mechanistic Interpretability — Explained | by Zeping Yu | Medium",
            "url": "https://medium.com/@zepingyu/123-cb62513f5d50"
          },
          {
            "title": "Transformers represent belief state geometry in their residual stream",
            "url": "https://arxiv.org/pdf/2405.15943"
          },
          {
            "title": "Residual Streams in Transformer Models",
            "url": "https://retr0sushi04.netlify.app/blogs/residualstreamsblog/residualstreams"
          },
          {
            "title": "Patterns and Messages - Part 5 - The Residual Stream · Chris McCormick",
            "url": "https://mccormickml.com/2025/02/20/patterns-and-messages-part-5-the-residual-stream/"
          },
          {
            "title": "Residual Matrix Transformers: Scaling the Size of the Residual Stream",
            "url": "https://arxiv.org/pdf/2506.22696"
          },
          {
            "title": "Characterizing stable regions in the residual stream of LLMs",
            "url": "https://arxiv.org/pdf/2409.17113"
          }
        ]
      },
      "Based on the search results, here's what I found about the paper \"Exploring the Residual Stream of Transformers\" (arXiv 2312.12141):\n\n## Overview\n\nThe paper was submitted on December 19, 2023, and authored by Zeping Yu, Kailai Yang, Zhiwei Liu, and Sophia Ananiadou.\n\n## Research Focus\n\nThe paper explores the residual stream of transformers to increase the interpretability. The authors address the challenge of locating models' important parameters storing the knowledge for predicting the next word, and whether these parameters are stored on the same layer/module or different ones.\n\n## Key Findings\n\nThe paper finds that the mechanism behind residual connection is a direct addition function on before-softmax values, so the probabilities of tokens with larger before-softmax values will increase. Additionally, the authors prove that using log probability increase as contribution scores is reasonable, and based on this they can locate important parameters.\n\nThe paper is available on arXiv at https://arxiv.org/abs/2312.12141."
    ],
    "durationSeconds": 6.196480836000003
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-22T04:37:21.095Z_

<details><summary>↩ Tool result · `toolu_01WWofUTt3Ej2qYr7Lttb5Z1`</summary>

```text
Web search results for query: ""Quantifying Exposure Bias for Neural Language Generation" He 2019 arXiv 1905.10617"

Links: [{"title":"[1905.10617v1] Quantifying Exposure Bias for Neural Language Generation","url":"https://arxiv.org/abs/1905.10617v1"},{"title":"[1905.10617v4] Quantifying Exposure Bias for Neural Language Generation","url":"https://arxiv.org/abs/1905.10617v4"},{"title":"Quantifying Exposure Bias for Neural Language Generation","url":"https://arxiv.org/pdf/1905.10617v4"},{"title":"Quantifying Exposure Bias for Neural Language Generation | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Quantifying-Exposure-Bias-for-Neural-Language-He-Zhang/cbb1a1a80d26043867bb8bf2b7227c9139710ee5"},{"title":"Quantifying Exposure Bias for Neural Language Generation | Request PDF","url":"https://www.researchgate.net/publication/333418764_Quantifying_Exposure_Bias_for_Neural_Language_Generation"},{"title":"Quantifying Exposure Bias for Neural Language Generation | OpenReview","url":"https://openreview.net/forum?id=rJg2fTNtwr"},{"title":"[1905.10617] Exposure Bias versus Self-Recovery: Are Distortions Really Incremental for Autoregressive Text Generation?","url":"https://arxiv.org/abs/1905.10617"},{"title":"Why Exposure Bias Matters: An Imitation Learning Perspective of Error","url":"https://arxiv.org/pdf/2204.01171"},{"title":"Quantifying Exposure Bias for Neural Language Generation - Paper Detail","url":"https://deeplearn.org/arxiv/127105/quantifying-exposure-bias-for-neural-language-generation"},{"title":"Rethinking Exposure Bias In Language Modeling","url":"https://arxiv.org/pdf/1910.11235"}]

I found the paper you were looking for. Here's what the search results show about this work:

"Quantifying Exposure Bias for Neural Language Generation" by He et al. (2019) addresses the exposure bias problem, which refers to the training-inference discrepancy caused by teacher forcing in maximum likelihood estimation (MLE) training for recurrent neural network language models.

The paper proposes two simple and intuitive approaches to quantify exposure bias for MLE-trained language models. 

Interestingly, the results indicate that either exposure bias is trivial (indistinguishable from the mismatch between model and data distribution), or is not as significant as it is presumed to be (with a measured performance gap of 3%).

The paper is available on arXiv as paper 1905.10617 and was submitted on May 25, 2019. There are multiple versions of the paper available, with later versions providing more refined metrics and expanded experiments.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "652e1b48-5425-4360-9d09-b4c254656213",
  "uuid": "dffd8952-e085-4cdf-a741-7deecf7ae644",
  "tool_use_result": {
    "query": "\"Quantifying Exposure Bias for Neural Language Generation\" He 2019 arXiv 1905.10617",
    "results": [
      {
        "tool_use_id": "srvtoolu_017nXVxL2bGrhXH3j3KXUkkn",
        "content": [
          {
            "title": "[1905.10617v1] Quantifying Exposure Bias for Neural Language Generation",
            "url": "https://arxiv.org/abs/1905.10617v1"
          },
          {
            "title": "[1905.10617v4] Quantifying Exposure Bias for Neural Language Generation",
            "url": "https://arxiv.org/abs/1905.10617v4"
          },
          {
            "title": "Quantifying Exposure Bias for Neural Language Generation",
            "url": "https://arxiv.org/pdf/1905.10617v4"
          },
          {
            "title": "Quantifying Exposure Bias for Neural Language Generation | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Quantifying-Exposure-Bias-for-Neural-Language-He-Zhang/cbb1a1a80d26043867bb8bf2b7227c9139710ee5"
          },
          {
            "title": "Quantifying Exposure Bias for Neural Language Generation | Request PDF",
            "url": "https://www.researchgate.net/publication/333418764_Quantifying_Exposure_Bias_for_Neural_Language_Generation"
          },
          {
            "title": "Quantifying Exposure Bias for Neural Language Generation | OpenReview",
            "url": "https://openreview.net/forum?id=rJg2fTNtwr"
          },
          {
            "title": "[1905.10617] Exposure Bias versus Self-Recovery: Are Distortions Really Incremental for Autoregressive Text Generation?",
            "url": "https://arxiv.org/abs/1905.10617"
          },
          {
            "title": "Why Exposure Bias Matters: An Imitation Learning Perspective of Error",
            "url": "https://arxiv.org/pdf/2204.01171"
          },
          {
            "title": "Quantifying Exposure Bias for Neural Language Generation - Paper Detail",
            "url": "https://deeplearn.org/arxiv/127105/quantifying-exposure-bias-for-neural-language-generation"
          },
          {
            "title": "Rethinking Exposure Bias In Language Modeling",
            "url": "https://arxiv.org/pdf/1910.11235"
          }
        ]
      },
      "I found the paper you were looking for. Here's what the search results show about this work:\n\n\"Quantifying Exposure Bias for Neural Language Generation\" by He et al. (2019) addresses the exposure bias problem, which refers to the training-inference discrepancy caused by teacher forcing in maximum likelihood estimation (MLE) training for recurrent neural network language models.\n\nThe paper proposes two simple and intuitive approaches to quantify exposure bias for MLE-trained language models. \n\nInterestingly, the results indicate that either exposure bias is trivial (indistinguishable from the mismatch between model and data distribution), or is not as significant as it is presumed to be (with a measured performance gap of 3%).\n\nThe paper is available on arXiv as paper 1905.10617 and was submitted on May 25, 2019. There are multiple versions of the paper available, with later versions providing more refined metrics and expanded experiments."
    ],
    "durationSeconds": 6.090271795000008
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-22T04:37:21.944Z_

<details><summary>↩ Tool result · `toolu_014QufV9iWY5ZsD7nWQZHYWT`</summary>

```text
Web search results for query: ""Found in the Middle: Calibrating Positional Attention Bias" first author 2024"

Links: [{"title":"[2406.16008] Found in the Middle: Calibrating Positional Attention Bias Improves Long Context Utilization","url":"https://arxiv.org/abs/2406.16008"},{"title":"Found in the Middle: Calibrating Positional Attention Bias Improves Long Context Utilization | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/found-middle-calibrating-positional-attention-bias-improves"},{"title":"Found in the middle: Calibrating Positional Attention Bias Improves Long Context Utilization - ACL Anthology","url":"https://aclanthology.org/2024.findings-acl.890/"},{"title":"Paper page - Found in the Middle: Calibrating Positional Attention Bias Improves Long Context Utilization","url":"https://huggingface.co/papers/2406.16008"},{"title":"Found in the middle: Calibrating Positional Attention Bias Improves Long Context Utilization | Request PDF","url":"https://www.researchgate.net/publication/384206851_Found_in_the_middle_Calibrating_Positional_Attention_Bias_Improves_Long_Context_Utilization"},{"title":"Found in the Middle: Calibrating Positional Attention Bias Improves Long-Context RAG - Beancount.io","url":"https://beancount.io/bean-labs/research-logs/2026/07/02/found-in-the-middle-calibrating-positional-attention-bias"},{"title":"Found in the Middle: Calibrating Positional Attention Bias Improves Long Context Utilization","url":"https://arxiv.org/html/2406.16008v2"},{"title":"Found in the Middle: Calibrating Positional Attention Bias","url":"https://arxiv.org/pdf/2406.16008"}]

Based on the search results, I found the paper you're looking for:

**Title:** Found in the Middle: Calibrating Positional Attention Bias Improves Long Context Utilization

**First Author:** Cheng-Yu Hsieh

**Publication Details:** The paper was published in Findings of the Association for Computational Linguistics: ACL 2024, and it was posted on arXiv on June 23, 2024.

**Main Focus:** The paper addresses how LLMs struggle to capture relevant information in the middle of their input, establishing a connection between this "lost-in-the-middle" problem and LLMs' intrinsic attention bias where tokens at the beginning and end receive higher attention regardless of relevance.

**Key Contributions:** The authors propose a calibration mechanism called "found-in-the-middle" that allows models to attend to contexts according to their relevance even when in the middle, achieving better performance in locating relevant information and improving retrieval-augmented generation (RAG) performance across various tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "652e1b48-5425-4360-9d09-b4c254656213",
  "uuid": "f9adaacb-b7b7-4315-a574-f9a3e4766a95",
  "tool_use_result": {
    "query": "\"Found in the Middle: Calibrating Positional Attention Bias\" first author 2024",
    "results": [
      {
        "tool_use_id": "srvtoolu_01S8LiJNqc5bPkLnkYH9ozKr",
        "content": [
          {
            "title": "[2406.16008] Found in the Middle: Calibrating Positional Attention Bias Improves Long Context Utilization",
            "url": "https://arxiv.org/abs/2406.16008"
          },
          {
            "title": "Found in the Middle: Calibrating Positional Attention Bias Improves Long Context Utilization | AI Research Paper Details",
            "url": "https://www.aimodels.fyi/papers/arxiv/found-middle-calibrating-positional-attention-bias-improves"
          },
          {
            "title": "Found in the middle: Calibrating Positional Attention Bias Improves Long Context Utilization - ACL Anthology",
            "url": "https://aclanthology.org/2024.findings-acl.890/"
          },
          {
            "title": "Paper page - Found in the Middle: Calibrating Positional Attention Bias Improves Long Context Utilization",
            "url": "https://huggingface.co/papers/2406.16008"
          },
          {
            "title": "Found in the middle: Calibrating Positional Attention Bias Improves Long Context Utilization | Request PDF",
            "url": "https://www.researchgate.net/publication/384206851_Found_in_the_middle_Calibrating_Positional_Attention_Bias_Improves_Long_Context_Utilization"
          },
          {
            "title": "Found in the Middle: Calibrating Positional Attention Bias Improves Long-Context RAG - Beancount.io",
            "url": "https://beancount.io/bean-labs/research-logs/2026/07/02/found-in-the-middle-calibrating-positional-attention-bias"
          },
          {
            "title": "Found in the Middle: Calibrating Positional Attention Bias Improves Long Context Utilization",
            "url": "https://arxiv.org/html/2406.16008v2"
          },
          {
            "title": "Found in the Middle: Calibrating Positional Attention Bias",
            "url": "https://arxiv.org/pdf/2406.16008"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\n**Title:** Found in the Middle: Calibrating Positional Attention Bias Improves Long Context Utilization\n\n**First Author:** Cheng-Yu Hsieh\n\n**Publication Details:** The paper was published in Findings of the Association for Computational Linguistics: ACL 2024, and it was posted on arXiv on June 23, 2024.\n\n**Main Focus:** The paper addresses how LLMs struggle to capture relevant information in the middle of their input, establishing a connection between this \"lost-in-the-middle\" problem and LLMs' intrinsic attention bias where tokens at the beginning and end receive higher attention regardless of relevance.\n\n**Key Contributions:** The authors propose a calibration mechanism called \"found-in-the-middle\" that allows models to attend to contexts according to their relevance even when in the middle, achieving better performance in locating relevant information and improving retrieval-augmented generation (RAG) performance across various tasks."
    ],
    "durationSeconds": 5.211612612000026
  }
}
```

</details>

---

### Assistant

_source line 43_

<details><summary>Logged reasoning block</summary>

```text
Good. Now let me search for the remaining problematic entries:
- `schuster2022calm` - first author mismatch (bib=Schuster vs api=Bahri)
- `xiao2024streaming` - year issue, first author issue
- `chen2023positional` - need to verify
- `anonymous2025style` - need real author
- `grattafiori2024llama3` - year mismatch


- I should check a few more entries while I'm at it.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "652e1b48-5425-4360-9d09-b4c254656213",
  "uuid": "6567c7b0-07df-49fb-8841-4adf637fdf8d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QyeM2GWY3Bm5C58iz9Dtrb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5624,
      "cache_read_input_tokens": 46797,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5624
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

_source line 44_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NVomwCcWVaudQ89GC4haSs`</summary>

```json
{
  "query": "\"Confident Adaptive Language Modeling\" Schuster 2022 arXiv NeurIPS"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "652e1b48-5425-4360-9d09-b4c254656213",
  "uuid": "1e12abed-e356-490b-b100-a7ebf2295ac1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QyeM2GWY3Bm5C58iz9Dtrb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5624,
      "cache_read_input_tokens": 46797,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5624
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

_source line 45_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TPZmkeMBDm1uJ3enk2DKvY`</summary>

```json
{
  "query": "\"Efficient Streaming Language Models with Attention Sinks\" Xiao 2024 arXiv 2309.17453"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "652e1b48-5425-4360-9d09-b4c254656213",
  "uuid": "ebfbb4b1-9aa8-46b7-88db-c78da46f8256",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QyeM2GWY3Bm5C58iz9Dtrb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5624,
      "cache_read_input_tokens": 46797,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5624
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

_source line 46_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UDy4jmXoCc99vofF35wiDk`</summary>

```json
{
  "query": "\"Extending Context Window of Large Language Models via Positional Interpolation\" Chen 2023 arXiv 2306.15595"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "652e1b48-5425-4360-9d09-b4c254656213",
  "uuid": "13d1e794-779d-4312-a379-69492bfc3232",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QyeM2GWY3Bm5C58iz9Dtrb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5624,
      "cache_read_input_tokens": 46797,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5624
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

_source line 47_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Rg55H54n31v56jE8PW7Whc`</summary>

```json
{
  "query": "\"Style Amnesia\" \"Speaking Style Degradation\" \"Multi-Turn Spoken Language Models\" arXiv 2512"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "652e1b48-5425-4360-9d09-b4c254656213",
  "uuid": "514573ba-1789-4030-acdb-2459c85b02c9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QyeM2GWY3Bm5C58iz9Dtrb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5624,
      "cache_read_input_tokens": 46797,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5624
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

_source line 48_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EHsTRT5i7C3wgkYBDAVNTJ`</summary>

```json
{
  "query": "\"The Llama 3 Herd of Models\" Grattafiori 2024 arXiv 2407.21783"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "652e1b48-5425-4360-9d09-b4c254656213",
  "uuid": "6ebf64f0-5f10-4318-a427-767695ea53e4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QyeM2GWY3Bm5C58iz9Dtrb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5624,
      "cache_read_input_tokens": 46797,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5624
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

_source line 49_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GYGPPj6zAehAf8yBUNpoHu`</summary>

```json
{
  "query": "\"Reassessing Layer Pruning in LLMs: New Insights and Methods\" arXiv 2411.15558 author"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "652e1b48-5425-4360-9d09-b4c254656213",
  "uuid": "e9af613a-6f83-42e1-b940-ac8a2eed9ec1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QyeM2GWY3Bm5C58iz9Dtrb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5624,
      "cache_read_input_tokens": 46797,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5624
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

_source line 50_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KzuKt9bPVQnVQ5ELZzykYB`</summary>

```json
{
  "query": "\"When Attention Closes\" Dongre 2026 arXiv 2605.12922 \"Multi-Turn\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "652e1b48-5425-4360-9d09-b4c254656213",
  "uuid": "3e1ca8a3-1402-4804-a52f-34f39491b023",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QyeM2GWY3Bm5C58iz9Dtrb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5624,
      "cache_read_input_tokens": 46797,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5624
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

_source line 51 · 2026-05-22T04:37:38.245Z_

<details><summary>↩ Tool result · `toolu_01TPZmkeMBDm1uJ3enk2DKvY`</summary>

```text
Web search results for query: ""Efficient Streaming Language Models with Attention Sinks" Xiao 2024 arXiv 2309.17453"

Links: [{"title":"[2309.17453] Efficient Streaming Language Models with Attention Sinks","url":"https://arxiv.org/abs/2309.17453"},{"title":"Efficient Streaming Language Models with Attention Sinks","url":"https://arxiv.org/html/2309.17453v4"},{"title":"[2309.17453v2] Efficient Streaming Language Models with Attention Sinks","url":"https://arxiv.org/abs/2309.17453v2"},{"title":"[2309.17453v3] Efficient Streaming Language Models with Attention Sinks","url":"https://arxiv.org/abs/2309.17453v3"},{"title":"[2309.17453v4] Efficient Streaming Language Models with Attention Sinks","url":"http://arxiv.org/abs/2309.17453v4"},{"title":"[PDF] Efficient Streaming Language Models with Attention Sinks | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Efficient-Streaming-Language-Models-with-Attention-Xiao-Tian/fdc53c2c10742464087c0525f77e32604827a21d"},{"title":"Efficient Streaming Language Models with Attention Sinks - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv230917453X/abstract"}]

I've found the paper you're searching for. Here are the key details:

**Paper Information:**
- **Title:** Efficient Streaming Language Models with Attention Sinks
- **Authors:** Guangxuan Xiao, Yuandong Tian, Beidi Chen, Song Han, and Mike Lewis
- **ArXiv ID:** 2309.17453
- **Latest Version:** v4 (April 7, 2024)
- **Submitted:** September 29, 2023

**Main Focus:**
The paper addresses deploying Large Language Models (LLMs) in streaming applications such as multi-round dialogue, where long interactions are expected. 

**Key Challenges Addressed:**
Firstly, during the decoding stage, caching previous tokens' Key and Value states (KV) consumes extensive memory. Secondly, popular LLMs cannot generalize to longer texts than the training sequence length.

**Proposed Solution:**
StreamingLLM is an efficient framework that enables LLMs trained with a finite length attention window to generalize to infinite sequence lengths without any fine-tuning and can enable Llama-2, MPT, Falcon, and Pythia to perform stable and efficient language modeling with up to 4 million tokens and more.

The paper is available on arXiv at https://arxiv.org/abs/2309.17453, and the code is available on GitHub at https://github.com/mit-han-lab/streaming-llm.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "652e1b48-5425-4360-9d09-b4c254656213",
  "uuid": "1e24b3c4-926e-4eac-8a3e-ef3fd386cd6f",
  "tool_use_result": {
    "query": "\"Efficient Streaming Language Models with Attention Sinks\" Xiao 2024 arXiv 2309.17453",
    "results": [
      {
        "tool_use_id": "srvtoolu_01UExV57tFUEcPDwZVS98p3j",
        "content": [
          {
            "title": "[2309.17453] Efficient Streaming Language Models with Attention Sinks",
            "url": "https://arxiv.org/abs/2309.17453"
          },
          {
            "title": "Efficient Streaming Language Models with Attention Sinks",
            "url": "https://arxiv.org/html/2309.17453v4"
          },
          {
            "title": "[2309.17453v2] Efficient Streaming Language Models with Attention Sinks",
            "url": "https://arxiv.org/abs/2309.17453v2"
          },
          {
            "title": "[2309.17453v3] Efficient Streaming Language Models with Attention Sinks",
            "url": "https://arxiv.org/abs/2309.17453v3"
          },
          {
            "title": "[2309.17453v4] Efficient Streaming Language Models with Attention Sinks",
            "url": "http://arxiv.org/abs/2309.17453v4"
          },
          {
            "title": "[PDF] Efficient Streaming Language Models with Attention Sinks | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Efficient-Streaming-Language-Models-with-Attention-Xiao-Tian/fdc53c2c10742464087c0525f77e32604827a21d"
          },
          {
            "title": "Efficient Streaming Language Models with Attention Sinks - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2023arXiv230917453X/abstract"
          }
        ]
      },
      "I've found the paper you're searching for. Here are the key details:\n\n**Paper Information:**\n- **Title:** Efficient Streaming Language Models with Attention Sinks\n- **Authors:** Guangxuan Xiao, Yuandong Tian, Beidi Chen, Song Han, and Mike Lewis\n- **ArXiv ID:** 2309.17453\n- **Latest Version:** v4 (April 7, 2024)\n- **Submitted:** September 29, 2023\n\n**Main Focus:**\nThe paper addresses deploying Large Language Models (LLMs) in streaming applications such as multi-round dialogue, where long interactions are expected. \n\n**Key Challenges Addressed:**\nFirstly, during the decoding stage, caching previous tokens' Key and Value states (KV) consumes extensive memory. Secondly, popular LLMs cannot generalize to longer texts than the training sequence length.\n\n**Proposed Solution:**\nStreamingLLM is an efficient framework that enables LLMs trained with a finite length attention window to generalize to infinite sequence lengths without any fine-tuning and can enable Llama-2, MPT, Falcon, and Pythia to perform stable and efficient language modeling with up to 4 million tokens and more.\n\nThe paper is available on arXiv at https://arxiv.org/abs/2309.17453, and the code is available on GitHub at https://github.com/mit-han-lab/streaming-llm."
    ],
    "durationSeconds": 5.429751714000012
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-22T04:37:38.898Z_

<details><summary>↩ Tool result · `toolu_01NVomwCcWVaudQ89GC4haSs`</summary>

```text
Web search results for query: ""Confident Adaptive Language Modeling" Schuster 2022 arXiv NeurIPS"

Links: [{"title":"Confident Adaptive Language Modeling","url":"https://papers.neurips.cc/paper_files/paper/2022/file/6fac9e316a4ae75ea244ddcef1982c71-Paper-Conference.pdf"},{"title":"Confident Adaptive Language Modeling","url":"https://arxiv.org/pdf/2207.07061"},{"title":"[2207.07061] Confident Adaptive Language Modeling","url":"https://arxiv.org/abs/2207.07061"},{"title":"Confident Adaptive Language Modeling | Request PDF","url":"https://www.researchgate.net/publication/362011497_Confident_Adaptive_Language_Modeling"},{"title":"Accelerating text generation with Confident Adaptive Language Modeling (CALM)","url":"https://research.google/blog/accelerating-text-generation-with-confident-adaptive-language-modeling-calm/"},{"title":"Confident adaptive language modeling | Proceedings of the 36th International Conference on Neural Information Processing Systems","url":"https://dl.acm.org/doi/10.5555/3600270.3601539"},{"title":"Confident Adaptive Language Modeling | OpenReview","url":"https://openreview.net/forum?id=uLYc4L3C81A"}]

I found the paper you're looking for! Here are the key details:

**Paper:** "Confident Adaptive Language Modeling" was presented at NeurIPS 2022

**Authors:** Tal Schuster, Adam Fisch, Jai Gupta, Mostafa Dehghani, Dara Bahri, Vinh Q. Tran, Yi Tay, and Donald Metzler

**arXiv ID:** The paper is available as arXiv paper 2207.07061

**Overview:** The paper introduces Confident Adaptive Language Modeling (CALM), a framework for dynamically allocating different amounts of compute per input and generation timestep. The method is motivated by the intuition that some next word predictions are easier than others, and CALM dynamically distributes computational effort across generation timesteps, generating text faster while preserving output quality by selectively allocating more computational resources only to harder predictions.

The paper addresses key challenges in early exit decoding and uses distribution-free risk control techniques to maintain sequence-level performance constraints.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "652e1b48-5425-4360-9d09-b4c254656213",
  "uuid": "a4cbe39e-a82e-47e2-a42a-e1e3a103dd60",
  "tool_use_result": {
    "query": "\"Confident Adaptive Language Modeling\" Schuster 2022 arXiv NeurIPS",
    "results": [
      {
        "tool_use_id": "srvtoolu_013S2PnKbUp297nJhkcJTBSb",
        "content": [
          {
            "title": "Confident Adaptive Language Modeling",
            "url": "https://papers.neurips.cc/paper_files/paper/2022/file/6fac9e316a4ae75ea244ddcef1982c71-Paper-Conference.pdf"
          },
          {
            "title": "Confident Adaptive Language Modeling",
            "url": "https://arxiv.org/pdf/2207.07061"
          },
          {
            "title": "[2207.07061] Confident Adaptive Language Modeling",
            "url": "https://arxiv.org/abs/2207.07061"
          },
          {
            "title": "Confident Adaptive Language Modeling | Request PDF",
            "url": "https://www.researchgate.net/publication/362011497_Confident_Adaptive_Language_Modeling"
          },
          {
            "title": "Accelerating text generation with Confident Adaptive Language Modeling (CALM)",
            "url": "https://research.google/blog/accelerating-text-generation-with-confident-adaptive-language-modeling-calm/"
          },
          {
            "title": "Confident adaptive language modeling | Proceedings of the 36th International Conference on Neural Information Processing Systems",
            "url": "https://dl.acm.org/doi/10.5555/3600270.3601539"
          },
          {
            "title": "Confident Adaptive Language Modeling | OpenReview",
            "url": "https://openreview.net/forum?id=uLYc4L3C81A"
          }
        ]
      },
      "I found the paper you're looking for! Here are the key details:\n\n**Paper:** \"Confident Adaptive Language Modeling\" was presented at NeurIPS 2022\n\n**Authors:** Tal Schuster, Adam Fisch, Jai Gupta, Mostafa Dehghani, Dara Bahri, Vinh Q. Tran, Yi Tay, and Donald Metzler\n\n**arXiv ID:** The paper is available as arXiv paper 2207.07061\n\n**Overview:** The paper introduces Confident Adaptive Language Modeling (CALM), a framework for dynamically allocating different amounts of compute per input and generation timestep. The method is motivated by the intuition that some next word predictions are easier than others, and CALM dynamically distributes computational effort across generation timesteps, generating text faster while preserving output quality by selectively allocating more computational resources only to harder predictions.\n\nThe paper addresses key challenges in early exit decoding and uses distribution-free risk control techniques to maintain sequence-level performance constraints."
    ],
    "durationSeconds": 6.226370998999977
  }
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-22T04:37:40.208Z_

<details><summary>↩ Tool result · `toolu_01UDy4jmXoCc99vofF35wiDk`</summary>

```text
Web search results for query: ""Extending Context Window of Large Language Models via Positional Interpolation" Chen 2023 arXiv 2306.15595"

Links: [{"title":"GitHub - Math1019/Extend_Context_Window_Position_Interpolation: An overview of the Extending Context Window of Large Language Models via Positional Interpolation paper","url":"https://github.com/Math1019/Extend_Context_Window_Position_Interpolation"},{"title":"[2306.15595] Extending Context Window of Large Language Models via Positional Interpolation","url":"https://arxiv.org/abs/2306.15595"},{"title":"[PDF] Extending Context Window of Large Language Models via Positional Interpolation | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Extending-Context-Window-of-Large-Language-Models-Chen-Wong/f5afaccfe90268485a9961c5771ec5e71e9b806c"},{"title":"(PDF) Extending Context Window of Large Language Models via Positional Interpolation","url":"https://www.researchgate.net/publication/371909431_Extending_Context_Window_of_Large_Language_Models_via_Positional_Interpolation"},{"title":"[2306.15595] Extending Context Window of Large Language Models via Position Interpolation","url":"https://ar5iv.labs.arxiv.org/html/2306.15595"},{"title":"Extending Context Window of Large Language Models via Position Interpolation","url":"https://arxiv.org/html/2306.15595"},{"title":"Paper page - Extending Context Window of Large Language Models via Positional Interpolation","url":"https://huggingface.co/papers/2306.15595"},{"title":"EXTENDING CONTEXT WINDOW OF LARGE LAN- GUAGE MODELS VIA POSITION INTERPOLATION","url":"https://arxiv.org/pdf/2306.15595"}]

I found the paper! Here's what I discovered about "Extending Context Window of Large Language Models via Positional Interpolation":

**Paper Details:**
- Authors: Chen, S., Wong, S., Chen, L., & Tian, Y.
- Published: June 27, 2023 (arXiv:2306.15595)
- All authors are from Meta Platforms Inc.

**Main Contribution:**
The paper presents Position Interpolation (PI) that extends the context window sizes of RoPE-based pretrained LLMs such as LLaMA models to up to 32768 with minimal fine-tuning (within 1000 steps), while demonstrating strong empirical results on various tasks that require long context, including passkey retrieval, language modeling, and long document summarization from LLaMA 7B to 65B.

**Key Technical Approach:**
Position Interpolation linearly down-scales the input position indices to match the original context window size, rather than extrapolating beyond the trained context length which may lead to catastrophically high attention scores that completely ruin the self-attention mechanism.

**Performance:**
The extended model by Position Interpolation preserves quality relatively well on tasks within its original context window.

The paper is available directly on arXiv at https://arxiv.org/abs/2306.15595.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "652e1b48-5425-4360-9d09-b4c254656213",
  "uuid": "08b89fe4-116d-4bd4-94b9-df87a9e8b43e",
  "tool_use_result": {
    "query": "\"Extending Context Window of Large Language Models via Positional Interpolation\" Chen 2023 arXiv 2306.15595",
    "results": [
      {
        "tool_use_id": "srvtoolu_011duv1xTYckmbmH3dTRe5XR",
        "content": [
          {
            "title": "GitHub - Math1019/Extend_Context_Window_Position_Interpolation: An overview of the Extending Context Window of Large Language Models via Positional Interpolation paper",
            "url": "https://github.com/Math1019/Extend_Context_Window_Position_Interpolation"
          },
          {
            "title": "[2306.15595] Extending Context Window of Large Language Models via Positional Interpolation",
            "url": "https://arxiv.org/abs/2306.15595"
          },
          {
            "title": "[PDF] Extending Context Window of Large Language Models via Positional Interpolation | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Extending-Context-Window-of-Large-Language-Models-Chen-Wong/f5afaccfe90268485a9961c5771ec5e71e9b806c"
          },
          {
            "title": "(PDF) Extending Context Window of Large Language Models via Positional Interpolation",
            "url": "https://www.researchgate.net/publication/371909431_Extending_Context_Window_of_Large_Language_Models_via_Positional_Interpolation"
          },
          {
            "title": "[2306.15595] Extending Context Window of Large Language Models via Position Interpolation",
            "url": "https://ar5iv.labs.arxiv.org/html/2306.15595"
          },
          {
            "title": "Extending Context Window of Large Language Models via Position Interpolation",
            "url": "https://arxiv.org/html/2306.15595"
          },
          {
            "title": "Paper page - Extending Context Window of Large Language Models via Positional Interpolation",
            "url": "https://huggingface.co/papers/2306.15595"
          },
          {
            "title": "EXTENDING CONTEXT WINDOW OF LARGE LAN- GUAGE MODELS VIA POSITION INTERPOLATION",
            "url": "https://arxiv.org/pdf/2306.15595"
          }
        ]
      },
      "I found the paper! Here's what I discovered about \"Extending Context Window of Large Language Models via Positional Interpolation\":\n\n**Paper Details:**\n- Authors: Chen, S., Wong, S., Chen, L., & Tian, Y.\n- Published: June 27, 2023 (arXiv:2306.15595)\n- All authors are from Meta Platforms Inc.\n\n**Main Contribution:**\nThe paper presents Position Interpolation (PI) that extends the context window sizes of RoPE-based pretrained LLMs such as LLaMA models to up to 32768 with minimal fine-tuning (within 1000 steps), while demonstrating strong empirical results on various tasks that require long context, including passkey retrieval, language modeling, and long document summarization from LLaMA 7B to 65B.\n\n**Key Technical Approach:**\nPosition Interpolation linearly down-scales the input position indices to match the original context window size, rather than extrapolating beyond the trained context length which may lead to catastrophically high attention scores that completely ruin the self-attention mechanism.\n\n**Performance:**\nThe extended model by Position Interpolation preserves quality relatively well on tasks within its original context window.\n\nThe paper is available directly on arXiv at https://arxiv.org/abs/2306.15595."
    ],
    "durationSeconds": 6.627155765999982
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-22T04:37:40.585Z_

<details><summary>↩ Tool result · `toolu_01GYGPPj6zAehAf8yBUNpoHu`</summary>

```text
Web search results for query: ""Reassessing Layer Pruning in LLMs: New Insights and Methods" arXiv 2411.15558 author"

Links: [{"title":"[2411.15558v1] Reassessing Layer Pruning in LLMs: New Insights and Methods","url":"https://arxiv.org/abs/2411.15558v1"},{"title":"[2411.15558] Reassessing Layer Pruning in LLMs: New Insights and Methods","url":"https://arxiv.org/abs/2411.15558"},{"title":"Computer Science Nov 2024","url":"https://arxiv.org/list/cs/2024-11?skip=6800&show=500"},{"title":"Work in Progress REASSESSING LAYER PRUNING IN LLMS: NEW INSIGHTS AND METHODS","url":"https://arxiv.org/pdf/2411.15558"},{"title":"Machine Learning Nov 2024","url":"https://www.arxiv.org/list/cs.LG/2024-11?skip=1225&show=250"},{"title":"Common-token Optimized Model Pruning Across Channels ...","url":"https://arxiv.org/pdf/2509.06836"},{"title":"Reassessing Layer Pruning in LLMs: New Insights and Methods | Request PDF","url":"https://www.researchgate.net/publication/386112944_Reassessing_Layer_Pruning_in_LLMs_New_Insights_and_Methods"}]

Based on the search results, I found the paper "Reassessing Layer Pruning in LLMs: New Insights and Methods" (arXiv 2411.15558). 

The authors of this paper are: Yao Lu, Hao Cheng, Yujie Fang, Zeyu Wang, Jiaheng Wei, Dongwei Xu, Qi Xuan, Xiaoniu Yang, and Zhaowei Zhu.

The paper was published on November 23, 2024, and addresses best practices for layer pruning in large language models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "652e1b48-5425-4360-9d09-b4c254656213",
  "uuid": "b5064e26-c3ce-4923-b7e0-dd439b6322a8",
  "tool_use_result": {
    "query": "\"Reassessing Layer Pruning in LLMs: New Insights and Methods\" arXiv 2411.15558 author",
    "results": [
      {
        "tool_use_id": "srvtoolu_01MjgHnhx99m6uqxd4bEowE2",
        "content": [
          {
            "title": "[2411.15558v1] Reassessing Layer Pruning in LLMs: New Insights and Methods",
            "url": "https://arxiv.org/abs/2411.15558v1"
          },
          {
            "title": "[2411.15558] Reassessing Layer Pruning in LLMs: New Insights and Methods",
            "url": "https://arxiv.org/abs/2411.15558"
          },
          {
            "title": "Computer Science Nov 2024",
            "url": "https://arxiv.org/list/cs/2024-11?skip=6800&show=500"
          },
          {
            "title": "Work in Progress REASSESSING LAYER PRUNING IN LLMS: NEW INSIGHTS AND METHODS",
            "url": "https://arxiv.org/pdf/2411.15558"
          },
          {
            "title": "Machine Learning Nov 2024",
            "url": "https://www.arxiv.org/list/cs.LG/2024-11?skip=1225&show=250"
          },
          {
            "title": "Common-token Optimized Model Pruning Across Channels ...",
            "url": "https://arxiv.org/pdf/2509.06836"
          },
          {
            "title": "Reassessing Layer Pruning in LLMs: New Insights and Methods | Request PDF",
            "url": "https://www.researchgate.net/publication/386112944_Reassessing_Layer_Pruning_in_LLMs_New_Insights_and_Methods"
          }
        ]
      },
      "Based on the search results, I found the paper \"Reassessing Layer Pruning in LLMs: New Insights and Methods\" (arXiv 2411.15558). \n\nThe authors of this paper are: Yao Lu, Hao Cheng, Yujie Fang, Zeyu Wang, Jiaheng Wei, Dongwei Xu, Qi Xuan, Xiaoniu Yang, and Zhaowei Zhu.\n\nThe paper was published on November 23, 2024, and addresses best practices for layer pruning in large language models."
    ],
    "durationSeconds": 4.107763640999969
  }
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-22T04:37:41.172Z_

<details><summary>↩ Tool result · `toolu_01Rg55H54n31v56jE8PW7Whc`</summary>

```text
Web search results for query: ""Style Amnesia" "Speaking Style Degradation" "Multi-Turn Spoken Language Models" arXiv 2512"

Links: [{"title":"Style Amnesia: Investigating Speaking Style Degradation and Mitigation in Multi-Turn Spoken Language Models | alphaXiv","url":"https://www.alphaxiv.org/overview/2512.23578"},{"title":"[2512.23578] Style Amnesia: Investigating Speaking Style Degradation and Mitigation in Multi-Turn Spoken Language Models","url":"https://arxiv.org/abs/2512.23578"},{"title":"Style Amnesia: Investigating Speaking Style Degradation and Mitigation in Multi-Turn Spoken Language Models","url":"https://arxiv.org/pdf/2512.23578"},{"title":"Style Amnesia: Investigating Speaking Style Degradation and Mitigation in Multi-Turn Spoken Language Models","url":"https://arxiv.org/html/2512.23578v3"},{"title":"StyleBench: Evaluating Speech Language Models on Conversational Speaking Style Control","url":"https://arxiv.org/pdf/2603.07599"}]

Based on the search results, I found the paper you're looking for:

"Style Amnesia: Investigating Speaking Style Degradation and Mitigation in Multi-Turn Spoken Language Models" is authored by Yu-Xiang Lin, Cheng-Han Chiang, and Hung-yi Lee from National Taiwan University.

The paper demonstrates that when spoken language models (SLMs) are instructed to speak in a specific speaking style at the beginning of a multi-turn conversation, they cannot maintain the required speaking styles after several turns of interaction. The researchers focus on paralinguistic speaking styles, including emotion, accent, volume, and speaking speed.

The research evaluates three proprietary and two open-source SLMs, showing that none of these models can maintain a consistent speaking style when instructed to do so. However, explicitly asking the model to recall the style instruction can partially mitigate style amnesia.

The paper is available on arXiv with identifier 2512.23578 and was published in early January 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "652e1b48-5425-4360-9d09-b4c254656213",
  "uuid": "71b218e7-2064-4003-b852-483171392ff1",
  "tool_use_result": {
    "query": "\"Style Amnesia\" \"Speaking Style Degradation\" \"Multi-Turn Spoken Language Models\" arXiv 2512",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Sx5DJ3uhgTSUf2sg6ejMMX",
        "content": [
          {
            "title": "Style Amnesia: Investigating Speaking Style Degradation and Mitigation in Multi-Turn Spoken Language Models | alphaXiv",
            "url": "https://www.alphaxiv.org/overview/2512.23578"
          },
          {
            "title": "[2512.23578] Style Amnesia: Investigating Speaking Style Degradation and Mitigation in Multi-Turn Spoken Language Models",
            "url": "https://arxiv.org/abs/2512.23578"
          },
          {
            "title": "Style Amnesia: Investigating Speaking Style Degradation and Mitigation in Multi-Turn Spoken Language Models",
            "url": "https://arxiv.org/pdf/2512.23578"
          },
          {
            "title": "Style Amnesia: Investigating Speaking Style Degradation and Mitigation in Multi-Turn Spoken Language Models",
            "url": "https://arxiv.org/html/2512.23578v3"
          },
          {
            "title": "StyleBench: Evaluating Speech Language Models on Conversational Speaking Style Control",
            "url": "https://arxiv.org/pdf/2603.07599"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\n\"Style Amnesia: Investigating Speaking Style Degradation and Mitigation in Multi-Turn Spoken Language Models\" is authored by Yu-Xiang Lin, Cheng-Han Chiang, and Hung-yi Lee from National Taiwan University.\n\nThe paper demonstrates that when spoken language models (SLMs) are instructed to speak in a specific speaking style at the beginning of a multi-turn conversation, they cannot maintain the required speaking styles after several turns of interaction. The researchers focus on paralinguistic speaking styles, including emotion, accent, volume, and speaking speed.\n\nThe research evaluates three proprietary and two open-source SLMs, showing that none of these models can maintain a consistent speaking style when instructed to do so. However, explicitly asking the model to recall the style instruction can partially mitigate style amnesia.\n\nThe paper is available on arXiv with identifier 2512.23578 and was published in early January 2026."
    ],
    "durationSeconds": 6.594043536999961
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-22T04:37:41.287Z_

<details><summary>↩ Tool result · `toolu_01EHsTRT5i7C3wgkYBDAVNTJ`</summary>

```text
Web search results for query: ""The Llama 3 Herd of Models" Grattafiori 2024 arXiv 2407.21783"

Links: [{"title":"[2407.21783] The Llama 3 Herd of Models","url":"https://arxiv.org/abs/2407.21783"},{"title":"[2407.21783v3] The Llama 3 Herd of Models","url":"https://arxiv.org/abs/2407.21783v3"},{"title":"[2407.21783] The Llama 3 Herd of Models - ar5iv - arXiv","url":"https://ar5iv.labs.arxiv.org/html/2407.21783"},{"title":"The Llama 3 Herd of Models - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240721783G/abstract"},{"title":"[2407.21783v1] The Llama 3 Herd of Models","url":"https://arxiv.org/abs/2407.21783v1"},{"title":"[2407.21783v2] The Llama 3 Herd of Models","url":"https://arxiv.org/abs/2407.21783v2"},{"title":"Paper page - The Llama 3 Herd of Models","url":"https://huggingface.co/papers/2407.21783"},{"title":"(PDF) The Llama 3 Herd of Models","url":"https://www.researchgate.net/publication/382739128_The_Llama_3_Herd_of_Models"},{"title":"The Llama 3 Herd of Models Llama Team, AI @ Meta1","url":"https://arxiv.org/pdf/2407.21783"}]

I found the paper you're looking for! Here's what I found:

**"The Llama 3 Herd of Models"** by Aaron Grattafiori and 558 other authors (arXiv 2407.21783) is a research paper about Meta's Llama 3 language models.

Key details about the paper:

- **Release date:** The paper was submitted on July 31, 2024, with the latest version (v3) revised on November 23, 2024
- **Main contribution:** The paper presents a new set of foundation models called Llama 3, a herd of language models that natively support multilinguality, coding, reasoning, and tool usage.

- **Model specifications:** The largest model is a dense Transformer with 405B parameters and a context window of up to 128K tokens.

- **Performance:** Llama 3 delivers comparable quality to leading language models such as GPT-4 on a plethora of tasks.

- **Additional capabilities:** The paper also presents the results of experiments in which we integrate image, video, and speech capabilities into Llama 3 via a compositional approach.

- **Public release:** Llama 3, including pre-trained and post-trained versions of the 405B parameter language model and Llama Guard 3 model for input and output safety, was publicly released.

The paper can be accessed directly at https://arxiv.org/abs/2407.21783


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "652e1b48-5425-4360-9d09-b4c254656213",
  "uuid": "48380551-e4f0-434c-b16c-97e5102adf5e",
  "tool_use_result": {
    "query": "\"The Llama 3 Herd of Models\" Grattafiori 2024 arXiv 2407.21783",
    "results": [
      {
        "tool_use_id": "srvtoolu_01PH1RtEKKKG6ywmTDYEHnHE",
        "content": [
          {
            "title": "[2407.21783] The Llama 3 Herd of Models",
            "url": "https://arxiv.org/abs/2407.21783"
          },
          {
            "title": "[2407.21783v3] The Llama 3 Herd of Models",
            "url": "https://arxiv.org/abs/2407.21783v3"
          },
          {
            "title": "[2407.21783] The Llama 3 Herd of Models - ar5iv - arXiv",
            "url": "https://ar5iv.labs.arxiv.org/html/2407.21783"
          },
          {
            "title": "The Llama 3 Herd of Models - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2024arXiv240721783G/abstract"
          },
          {
            "title": "[2407.21783v1] The Llama 3 Herd of Models",
            "url": "https://arxiv.org/abs/2407.21783v1"
          },
          {
            "title": "[2407.21783v2] The Llama 3 Herd of Models",
            "url": "https://arxiv.org/abs/2407.21783v2"
          },
          {
            "title": "Paper page - The Llama 3 Herd of Models",
            "url": "https://huggingface.co/papers/2407.21783"
          },
          {
            "title": "(PDF) The Llama 3 Herd of Models",
            "url": "https://www.researchgate.net/publication/382739128_The_Llama_3_Herd_of_Models"
          },
          {
            "title": "The Llama 3 Herd of Models Llama Team, AI @ Meta1",
            "url": "https://arxiv.org/pdf/2407.21783"
          }
        ]
      },
      "I found the paper you're looking for! Here's what I found:\n\n**\"The Llama 3 Herd of Models\"** by Aaron Grattafiori and 558 other authors (arXiv 2407.21783) is a research paper about Meta's Llama 3 language models.\n\nKey details about the paper:\n\n- **Release date:** The paper was submitted on July 31, 2024, with the latest version (v3) revised on November 23, 2024\n- **Main contribution:** The paper presents a new set of foundation models called Llama 3, a herd of language models that natively support multilinguality, coding, reasoning, and tool usage.\n\n- **Model specifications:** The largest model is a dense Transformer with 405B parameters and a context window of up to 128K tokens.\n\n- **Performance:** Llama 3 delivers comparable quality to leading language models such as GPT-4 on a plethora of tasks.\n\n- **Additional capabilities:** The paper also presents the results of experiments in which we integrate image, video, and speech capabilities into Llama 3 via a compositional approach.\n\n- **Public release:** Llama 3, including pre-trained and post-trained versions of the 405B parameter language model and Llama Guard 3 model for input and output safety, was publicly released.\n\nThe paper can be accessed directly at https://arxiv.org/abs/2407.21783"
    ],
    "durationSeconds": 6.2324734259999826
  }
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-22T04:37:43.715Z_

<details><summary>↩ Tool result · `toolu_01KzuKt9bPVQnVQ5ELZzykYB`</summary>

```text
Web search results for query: ""When Attention Closes" Dongre 2026 arXiv 2605.12922 "Multi-Turn""

Links: [{"title":"[2605.12922] When Attention Closes: How LLMs Lose the Thread in Multi-Turn Interaction","url":"https://arxiv.org/abs/2605.12922"},{"title":"When Attention Closes: How LLMs Lose the Thread in Multi-Turn Interaction","url":"https://arxiv.org/html/2605.12922"},{"title":"LoopServe: An Adaptive Dual-phase LLM Inference Acceleration System for Multi-Turn Dialogues","url":"https://arxiv.org/pdf/2507.13681"},{"title":"Evaluating and Improving Context Attention Distribution on Multi-Turn   Response Generation using Self-Contained Distractions","url":"https://arxiv.org/pdf/2211.04943"},{"title":"A Static and Dynamic Attention Framework for Multi Turn Dialogue   Generation","url":"https://arxiv.org/pdf/2410.20766"}]

Based on the search results, I found the paper you're looking for:

"When Attention Closes: How LLMs Lose the Thread in Multi-Turn Interaction" is an arXiv paper (2605.12922) submitted on May 13, 2026, authored by Vardhan Dongre and 5 other authors.

The paper addresses how large language models can follow complex instructions in a single turn, yet over long multi-turn interactions they often lose the thread of instructions, persona, and rules. The authors propose a channel-transition account: goal-defining tokens become less accessible through attention, while goal-related information may persist in residual representations.

They introduce the Goal Accessibility Ratio (GAR), measuring attention from generated tokens to task-defining goal tokens, and combine it with sliding-window ablations and residual-stream probes. Across architectures, the transition yields qualitatively distinct failure modes: some models preserve goal-conditioned behavior at vanishing attention, others fail despite decodable residual goal information, and the layer at which this encoding emerges varies from 2 to 27.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "652e1b48-5425-4360-9d09-b4c254656213",
  "uuid": "4e0212c2-3814-45e5-afcc-d6893db2fdbc",
  "tool_use_result": {
    "query": "\"When Attention Closes\" Dongre 2026 arXiv 2605.12922 \"Multi-Turn\"",
    "results": [
      {
        "tool_use_id": "srvtoolu_01AJAiVAhu4Tvu62hoU2PNiX",
        "content": [
          {
            "title": "[2605.12922] When Attention Closes: How LLMs Lose the Thread in Multi-Turn Interaction",
            "url": "https://arxiv.org/abs/2605.12922"
          },
          {
            "title": "When Attention Closes: How LLMs Lose the Thread in Multi-Turn Interaction",
            "url": "https://arxiv.org/html/2605.12922"
          },
          {
            "title": "LoopServe: An Adaptive Dual-phase LLM Inference Acceleration System for Multi-Turn Dialogues",
            "url": "https://arxiv.org/pdf/2507.13681"
          },
          {
            "title": "Evaluating and Improving Context Attention Distribution on Multi-Turn   Response Generation using Self-Contained Distractions",
            "url": "https://arxiv.org/pdf/2211.04943"
          },
          {
            "title": "A Static and Dynamic Attention Framework for Multi Turn Dialogue   Generation",
            "url": "https://arxiv.org/pdf/2410.20766"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\n\"When Attention Closes: How LLMs Lose the Thread in Multi-Turn Interaction\" is an arXiv paper (2605.12922) submitted on May 13, 2026, authored by Vardhan Dongre and 5 other authors.\n\nThe paper addresses how large language models can follow complex instructions in a single turn, yet over long multi-turn interactions they often lose the thread of instructions, persona, and rules. The authors propose a channel-transition account: goal-defining tokens become less accessible through attention, while goal-related information may persist in residual representations.\n\nThey introduce the Goal Accessibility Ratio (GAR), measuring attention from generated tokens to task-defining goal tokens, and combine it with sliding-window ablations and residual-stream probes. Across architectures, the transition yields qualitatively distinct failure modes: some models preserve goal-conditioned behavior at vanishing attention, others fail despite decodable residual goal information, and the layer at which this encoding emerges varies from 2 to 27."
    ],
    "durationSeconds": 6.616930320000043
  }
}
```

</details>

---

### Assistant

_source line 58_

<details><summary>Logged reasoning block</summary>

```text
Now let me also verify the remaining entries and check for specific issues. Let me also read the omitted lines from the grep output to get the full list of cited keys.

Let me also check a few more:
- `lawson2025skip` - "Learning to Skip the Middle Layers of Transformers" arXiv 2506.21103
- `qiu2025gated` - "Gated Attention for Large Language Models" arXiv 2505.06708

And I need to read all the tex files to get the full citations list.

Actually, from the verify_references output, I already have a fairly complete picture. 

Now I'm putting together the audit report. The main issues are the duplicate bib files creating 45 duplicate keys, and a few entries that OpenAlex couldn't verify online but are actually legitimate papers—like the LayerDrop paper by Fan et al. from ICLR 2020 and the FlexiDepth paper by Luo and others.

There are also several mismatches where author names don't match what's in the bibliography—some entries incorrectly list "Anonymous" when they should have actual author names like Lu et al. or Lin et al., and a few have the wrong first author listed. The title for `yu2023residual` is correct, and the arXiv ID matches. For `he2019exposure`, the title in the bib matches the original arXiv version, though the latest version changed it to something about self-recovery—I need to verify which version is actually being cited here.

Looking at `grattafiori2024llama3`, the submission year of 2024 is correct for arXiv, even though OpenAlex lists it as 2025. The author attribution should say "and others" rather than "and 1 others" given this is a 559-author paper. I'm also noticing there are orphan entries in the bibliography that aren't cited anywhere in the tex files.

Now I'm going through the list of uncited entries to understand what's being referenced but not actually used in the document. There are quite a few of them spanning different topics and years. I should also check the author formatting since there seem to be inconsistencies in how names are being presented across the bibliography. I need to review the full list of cited references from the tex files to see which bibliography entries are actually being used in the document.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "652e1b48-5425-4360-9d09-b4c254656213",
  "uuid": "d3d7624b-60e1-48fc-9244-f3285aaaca17",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015Fd3RcpSYfgLPRPa7fQBj8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5368,
      "cache_read_input_tokens": 52421,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5368
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

_source line 59_

现在读取被截断的 tex 行获取完整引用列表。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "652e1b48-5425-4360-9d09-b4c254656213",
  "uuid": "ecbab883-2940-4db3-b6c0-f2b951cd5bda",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015Fd3RcpSYfgLPRPa7fQBj8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5368,
      "cache_read_input_tokens": 52421,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5368
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

_source line 60_

<details open><summary>🔧 Tool call — Grep · `toolu_01CSg1oVyZiCnQwHu6yeVY5L`</summary>

```json
{
  "pattern": "\\\\cite[pt]?\\{[^}]+\\}",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper",
  "output_mode": "content",
  "glob": "*.tex",
  "head_limit": 0,
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
  "session_id": "652e1b48-5425-4360-9d09-b4c254656213",
  "uuid": "b269e014-c2c2-417b-aeb0-249a1cab76fa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015Fd3RcpSYfgLPRPa7fQBj8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5368,
      "cache_read_input_tokens": 52421,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5368
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

_source line 61 · 2026-05-22T04:38:30.886Z_

<details><summary>↩ Tool result · `toolu_01CSg1oVyZiCnQwHu6yeVY5L`</summary>

```text
paper/sections/analysis.tex:22:[Omitted long matching line]
paper/sections/analysis.tex:39:[Omitted long matching line]
paper/sections/analysis.tex:53:[Omitted long matching line]
paper/sections/related_work.tex:4:[Omitted long matching line]
paper/sections/related_work.tex:7:ReZero \citep{bachlechner2021rezero} showed that residual scaling shapes optimization dynamics. Subsequent work targets computational efficiency: LayerDrop \citep{fan2020layerdrop}, Mixture-of-Depths \citep{raposo2024mixture}, FlexiDepth \citep{luo2025flexidepth}, and CALM \citep{schuster2022calm}. ThreadGate applies residual gating to a different objective: recovering attention patterns in multi-turn dialogue.
paper/sections/related_work.tex:10:[Omitted long matching line]
paper/sections/related_work.tex:13:GradNorm \citep{chen2018gradnorm}, PCGrad \citep{yu2020pcgrad}, CAGrad \citep{liu2021cagrad}, and Nash-MTL \citep{navon2022nash} treat gradient conflict between competing losses as a root cause to be resolved through better optimization. We repurpose PCGrad as a causal analysis tool: eliminating directional conflict between NTP and GAR gradients does not improve GAR convergence. Gradient conflict is a symptom rather than the cause.
paper/sections/related_work.tex:16:[Omitted long matching line]
paper/sections/experiments.tex:8:[Omitted long matching line]
paper/sections/experiments.tex:14:[Omitted long matching line]
paper/sections/experiments.tex:21:\caption{Five-way comparison on Qwen-2.5-7B-Instruct. IID evaluation uses teacher-forced UltraChat text; held-out uses 50 non-overlapping conversations. All four fine-tuned variants converge to within 0.75\,pp on GAR-ours; PPL is indistinguishable. GAR-O = GAR-ours; GAR-D = GAR-Dongre \citep{dongre2026attention}.}
paper/sections/discussion.tex:5:[Omitted long matching line]
paper/sections/discussion.tex:9:TRC analysis (\S\ref{subsec:mechanism-specificity}) confirms the mismatch targets attention routing without disrupting hidden-state coherence. We scope claims to GAR losses on Qwen-2.5-7B and Llama-3.1-8B; magnitude imbalance \citep{chen2018gradnorm} and Nash equilibria \citep{navon2022nash} remain untested. Remaining directions include adaptive $\beta$ scheduling and layer-selective steering.
paper/sections/method.tex:6:We denote the task specification tokens in the system prompt as \emph{goal tokens} $\mathcal{G}$. \citet{dongre2026attention} defined the Goal Attention Ratio (GAR) for a model with $L$ layers and $H$ heads at turn $\tau$ as
paper/sections/method.tex:21:Inspired by the residual scaling idea of ReZero \citep{bachlechner2021rezero}, ThreadGate modulates the residual stream with a content-and-turn-conditioned gate at each transformer layer. The gated residual update at layer $l$ is
paper/sections/background.tex:4:[Omitted long matching line]
paper/sections/background.tex:18:\citet{dongre2026attention} showed that goal-relevant information persists in the residual stream (probe AUC\,=\,0.98) even at late turns where GAR has collapsed. The information is present but the attention mechanism fails to route it. This dissociation motivates an intervention that targets the residual pathway directly.
paper/sections/introduction.tex:3:[Omitted long matching line]
paper/sections/introduction.tex:5:[Omitted long matching line]
paper/sections/introduction.tex:14:[Omitted long matching line]
paper/sections/introduction.tex:16:[Omitted long matching line]
paper/sections/introduction.tex:18:[Omitted long matching line]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "652e1b48-5425-4360-9d09-b4c254656213",
  "uuid": "c0ad3c82-c312-4f2e-b2b8-688971981636",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "paper/sections/analysis.tex:22:[Omitted long matching line]\npaper/sections/analysis.tex:39:[Omitted long matching line]\npaper/sections/analysis.tex:53:[Omitted long matching line]\npaper/sections/related_work.tex:4:[Omitted long matching line]\npaper/sections/related_work.tex:7:ReZero \\citep{bachlechner2021rezero} showed that residual scaling shapes optimization dynamics. Subsequent work targets computational efficiency: LayerDrop \\citep{fan2020layerdrop}, Mixture-of-Depths \\citep{raposo2024mixture}, FlexiDepth \\citep{luo2025flexidepth}, and CALM \\citep{schuster2022calm}. ThreadGate applies residual gating to a different objective: recovering attention patterns in multi-turn dialogue.\npaper/sections/related_work.tex:10:[Omitted long matching line]\npaper/sections/related_work.tex:13:GradNorm \\citep{chen2018gradnorm}, PCGrad \\citep{yu2020pcgrad}, CAGrad \\citep{liu2021cagrad}, and Nash-MTL \\citep{navon2022nash} treat gradient conflict between competing losses as a root cause to be resolved through better optimization. We repurpose PCGrad as a causal analysis tool: eliminating directional conflict between NTP and GAR gradients does not improve GAR convergence. Gradient conflict is a symptom rather than the cause.\npaper/sections/related_work.tex:16:[Omitted long matching line]\npaper/sections/experiments.tex:8:[Omitted long matching line]\npaper/sections/experiments.tex:14:[Omitted long matching line]\npaper/sections/experiments.tex:21:\\caption{Five-way comparison on Qwen-2.5-7B-Instruct. IID evaluation uses teacher-forced UltraChat text; held-out uses 50 non-overlapping conversations. All four fine-tuned variants converge to within 0.75\\,pp on GAR-ours; PPL is indistinguishable. GAR-O = GAR-ours; GAR-D = GAR-Dongre \\citep{dongre2026attention}.}\npaper/sections/discussion.tex:5:[Omitted long matching line]\npaper/sections/discussion.tex:9:TRC analysis (\\S\\ref{subsec:mechanism-specificity}) confirms the mismatch targets attention routing without disrupting hidden-state coherence. We scope claims to GAR losses on Qwen-2.5-7B and Llama-3.1-8B; magnitude imbalance \\citep{chen2018gradnorm} and Nash equilibria \\citep{navon2022nash} remain untested. Remaining directions include adaptive $\\beta$ scheduling and layer-selective steering.\npaper/sections/method.tex:6:We denote the task specification tokens in the system prompt as \\emph{goal tokens} $\\mathcal{G}$. \\citet{dongre2026attention} defined the Goal Attention Ratio (GAR) for a model with $L$ layers and $H$ heads at turn $\\tau$ as\npaper/sections/method.tex:21:Inspired by the residual scaling idea of ReZero \\citep{bachlechner2021rezero}, ThreadGate modulates the residual stream with a content-and-turn-conditioned gate at each transformer layer. The gated residual update at layer $l$ is\npaper/sections/background.tex:4:[Omitted long matching line]\npaper/sections/background.tex:18:\\citet{dongre2026attention} showed that goal-relevant information persists in the residual stream (probe AUC\\,=\\,0.98) even at late turns where GAR has collapsed. The information is present but the attention mechanism fails to route it. This dissociation motivates an intervention that targets the residual pathway directly.\npaper/sections/introduction.tex:3:[Omitted long matching line]\npaper/sections/introduction.tex:5:[Omitted long matching line]\npaper/sections/introduction.tex:14:[Omitted long matching line]\npaper/sections/introduction.tex:16:[Omitted long matching line]\npaper/sections/introduction.tex:18:[Omitted long matching line]",
    "numLines": 22
  }
}
```

</details>

---

### Assistant

_source line 62_

<details><summary>Logged reasoning block</summary>

```text
Many lines are omitted because they're too long. Let me read the specific lines that were omitted to get the full citation keys.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "652e1b48-5425-4360-9d09-b4c254656213",
  "uuid": "14359bd2-3dff-4275-9132-6490b61273b2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NFJZ7vdQBnx5pz2V6cgxg9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2823,
      "cache_read_input_tokens": 57789,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2823
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

_source line 63_

<details open><summary>🔧 Tool call — Read · `toolu_01KPGNevT2uV82bF9jLhT1Q8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "652e1b48-5425-4360-9d09-b4c254656213",
  "uuid": "2a4afc38-201d-47cc-87c9-816f24892305",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NFJZ7vdQBnx5pz2V6cgxg9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2823,
      "cache_read_input_tokens": 57789,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2823
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

_source line 64 · 2026-05-22T04:38:36.223Z_

<details><summary>↩ Tool result · `toolu_01KPGNevT2uV82bF9jLhT1Q8`</summary>

```text
1	\section{Analysis}\label{sec:analysis}
2	
3	The five-way comparison in \S\ref{sec:experiments} established that gating produces no measurable benefit over LoRA-only fine-tuning. This section traces the failure through a three-step causal chain: we first show that gates learn behavior opposite to the design intent (\S\ref{subsec:gate-conditioning}), then rule out gradient conflict as the explanation through a causal exclusion experiment (\S\ref{subsec:pcgrad}), and finally identify distribution shift as the root cause (\S\ref{subsec:dist-shift}). \S\ref{subsec:mechanism-specificity} confirms this selectivity with an orthogonal hidden-state metric, and \S\ref{subsec:cross-model} confirms the failure generalizes across architecturally distinct LLMs.
4	
5	\subsection{Gate Turn Conditioning}\label{subsec:gate-conditioning}
6	
7	The design intent of ThreadGate is to modulate the residual stream more aggressively at late conversation turns, where GAR naturally decays (\S\ref{sec:background}). We test whether the learned gates achieve this by comparing gate values at turn~1 (early) and turn~21 (late) across all 28 layers of the trained model.
8	
9	The gates do the opposite. In 27 of 28 layers, the gate value at turn~1 is lower than at turn~21 (Wilcoxon signed-rank test: $p = 3.73 \times 10^{-8}$, effect size $r = 0.975$). At layer~23, the gate is 0.769 at turn~1 and 0.979 at turn~21; at layer~14, it is 0.747 at turn~1 and 0.928 at turn~21. The pattern is consistent: gates suppress the residual stream more at early turns (where GAR is already high) and become nearly passive at late turns (where intervention is most needed). This inversion has a straightforward explanation. NTP loss pressure is highest at late turns, where the model must predict tokens conditioned on a long context. The NTP gradient pushes gates toward 1.0 to preserve the full sublayer computation, and this pressure is strongest precisely where GAR-based attenuation would be most useful.
10	
11	The resulting inference-time gate values range from 0.93 to 0.98 (2--7\% attenuation), far below what meaningful modulation would require; this explains the convergence with LoRA-only in Table~\ref{tab:four-way}. Figure~\ref{fig:gate-shift}(a) visualizes the per-layer gate difference. The inverted turn conditioning raises a natural question: does the NTP-GAR gradient conflict prevent gates from learning the intended behavior? If gradient conflict is the root cause, resolving it should rescue gate conditioning.
12	
13	\begin{figure}[t]
14	  \centering
15	  \includegraphics[width=\columnwidth]{fig3_gate_shift.pdf}
16	  \caption{(a)~Gate turn conditioning: per-layer gate values at turn~1 vs turn~21. In 27/28 layers, gates approach 1.0 at late turns, inverting the design intent ($p = 3.73 \times 10^{-8}$). (b)~Distribution shift: the 20--33$\times$ GAR gap persists across all five variants (TG, +PCGrad, UG, LoRA-only, Base), the failure is universal across all configurations.}
17	  \label{fig:gate-shift}
18	\end{figure}
19	
20	\subsection{PCGrad Causal Exclusion}\label{subsec:pcgrad}
21	
22	The NTP and GAR gradients point in opposing directions across 68--79\% of layers throughout training, with mean cosine similarity ranging from $-$0.089 (epoch~0) to $-$0.042 (epoch~2). The NTP gradient magnitude dominates by 7.5--14.7$\times$. This raises a natural hypothesis: perhaps opposing gradient directions prevent the GAR objective from converging. If so, eliminating direction conflict should prevent the collapse. We test this using PCGrad \citep{yu2020pcgrad}, which projects the gradient of one task onto the normal plane of the other whenever two task gradients conflict. We apply PCGrad to gate parameters only, scoping our claim to direction conflict; magnitude imbalance \citep{chen2018gradnorm} and Nash equilibrium violations \citep{navon2022nash} remain untested.
23	
24	Eliminating direction conflict via PCGrad shifts per-step cosine similarity from consistently negative ($-$0.089) to oscillating around zero ($-$0.15 to $+$0.09), yet all outcomes remain unchanged: IID GAR-ours (0.50 vs 0.50), PPL (2.780 vs 2.784), and autoregressive GAR (0.015 vs 0.016) are indistinguishable (Table~\ref{tab:four-way}). $\mathcal{L}_\text{GAR}$ follows a nearly identical training trajectory and collapses in the same manner (Figure~\ref{fig:training-pcgrad}b). The causal exclusion follows by \emph{modus tollens}: if direction conflict causes the failure, removing it should prevent it; PCGrad removes it; the failure persists; therefore direction conflict is not the cause. Direction conflict is neither necessary (removing it does not rescue GAR) nor sufficient ($\mathcal{L}_\text{GAR}$ converges during training despite persistent conflict). The 7.5--14.7$\times$ NTP magnitude dominance renders directional interference inconsequential. With gradient conflict ruled out, the question narrows: the training dynamics are not the problem (GAR converges under teacher forcing), so the failure must occur at the transition from training to inference.
25	
26	\begin{figure}[t]
27	  \centering
28	  \includegraphics[width=\columnwidth]{fig2_training_pcgrad.pdf}
29	  \caption{(a)~Gradient cosine similarity between NTP and GAR objectives. ThreadGate remains consistently negative; +PCGrad oscillates around zero. (b)~IID evaluation outcomes are indistinguishable: eliminating direction conflict changes nothing.}
30	  \label{fig:training-pcgrad}
31	\end{figure}
32	
33	\subsection{Distribution Shift Analysis}\label{subsec:dist-shift}
34	
35	Gates are ineffective because NTP pressure pushes them toward identity (\S\ref{subsec:gate-conditioning}), and this is not caused by gradient direction conflict (\S\ref{subsec:pcgrad}). The remaining question: why do GAR improvements under teacher forcing fail to transfer to autoregressive generation?
36	
37	The 20--33$\times$ GAR gap (Table~\ref{tab:four-way}) persists across all training strategies: the model learns the intended attention pattern on the training distribution but collapses under model-generated text. GAR-Dongre provides a revealing control: under standard teacher-forced training it remains uniformly low (0.01--0.02) with no distribution gap, so the shift selectively destroys the concentrated last-token attention pattern while leaving diffuse attention unaffected (scheduled sampling breaks this pattern; \S\ref{sec:discussion}).
38	
39	The mechanism is exposure bias \citep{bengio2015scheduled}: during training, the model conditions on ground-truth prefixes; at inference, on its own outputs. The statistical properties diverge, and the 2--7\% gate attenuation (\S\ref{subsec:gate-conditioning}) cannot compensate. \citet{he2019exposure} showed that language models exhibit token-level self-recovery from exposure bias, and our PPL results confirm this (Table~\ref{tab:four-way}). The critical distinction is between primary and auxiliary objectives: NTP is robust because it is the same task at both training and inference time, while GAR optimizes a distributional property of the input prefix that has no counterpart under autoregressive generation. Figure~\ref{fig:attention-heatmap} confirms teacher-forced GAR-ours remains near $\tau = 0.5$ (7--8\% decay, $N$\,=\,45), yet autoregressive GAR collapses for all variants (Figure~\ref{fig:gate-shift}b).
40	
41	\subsection{Mechanism Specificity}\label{subsec:mechanism-specificity}
42	
43	\S\ref{subsec:dist-shift} showed that exposure bias selectively destroys GAR-ours (20--33$\times$ gap) while, under standard training, GAR-Dongre remains unaffected. We test whether this selectivity extends beyond attention with an orthogonal hidden-state probe.
44	
45	We define Turn-level Residual Coherence (TRC) as the cosine similarity between hidden states at the last-token position of adjacent assistant turns. If exposure bias caused broad representational failure, TRC should show a comparable gap. It does not. For ThreadGate, teacher-forced TRC is 0.334 and autoregressive TRC is 0.332 (gap $= +0.002$). For LoRA-only, teacher-forced TRC is 0.349 and autoregressive TRC is 0.411 (gap $= -0.062$, reversed): autoregressive generation does not degrade hidden-state coherence. Neither checkpoint shows a TRC gap comparable to the 20--33$\times$ GAR collapse.
46	
47	The slightly elevated autoregressive TRC for LoRA-only likely reflects higher token-level predictability in model-generated text, which produces more self-similar hidden states. These results confirm the selectivity from \S\ref{subsec:dist-shift} with an orthogonal metric: exposure bias disrupts a specific learned routing behavior (summary-position attention to goal tokens) while leaving internal representations intact.
48	
49	Cross-model evaluation extends this selectivity: GAR-Dongre shows negligible distribution shift on both Llama-3.1-8B (AR/TF ratio 1.002$\times$) and Qwen-2.5-7B (1.28$\times$), compared to the 12.5--33$\times$ collapse in GAR-ours, confirming that exposure bias primarily disrupts attention concentration at generation boundaries rather than aggregate attention patterns (the scheduled sampling experiment in \S\ref{sec:discussion} breaks this pattern, with GAR-Dongre rising to 0.353).
50	
51	\subsection{Cross-Model Generality}\label{subsec:cross-model}
52	
53	To test whether the exposure bias failure generalizes, we replicate the full evaluation pipeline on Llama-3.1-8B-Instruct \citep{grattafiori2024llama3}. Phase~1 diagnostics confirm goal attention decay (GAR: 0.026$\to$0.003 over 10 turns, 90.1\% decline vs.\ Qwen's 84.7\%). A matched evaluation ($N$\,=\,50, $T$\,=\,4) quantifies the exposure bias gap: teacher-forced GAR-ours is 0.484, autoregressive is 0.039, a 12.5$\times$ gap directionally consistent with Qwen's 20--33$\times$. The gate profile differs---Qwen's minimum at layers~3--4, Llama's at layer~25---yet both converge toward identity under NTP pressure. The exposure bias gap is consistent across architecturally distinct LLMs.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "652e1b48-5425-4360-9d09-b4c254656213",
  "uuid": "c3733ec2-e131-4031-8879-8d27ca43cdd2",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex",
      "content": "\\section{Analysis}\\label{sec:analysis}\n\nThe five-way comparison in \\S\\ref{sec:experiments} established that gating produces no measurable benefit over LoRA-only fine-tuning. This section traces the failure through a three-step causal chain: we first show that gates learn behavior opposite to the design intent (\\S\\ref{subsec:gate-conditioning}), then rule out gradient conflict as the explanation through a causal exclusion experiment (\\S\\ref{subsec:pcgrad}), and finally identify distribution shift as the root cause (\\S\\ref{subsec:dist-shift}). \\S\\ref{subsec:mechanism-specificity} confirms this selectivity with an orthogonal hidden-state metric, and \\S\\ref{subsec:cross-model} confirms the failure generalizes across architecturally distinct LLMs.\n\n\\subsection{Gate Turn Conditioning}\\label{subsec:gate-conditioning}\n\nThe design intent of ThreadGate is to modulate the residual stream more aggressively at late conversation turns, where GAR naturally decays (\\S\\ref{sec:background}). We test whether the learned gates achieve this by comparing gate values at turn~1 (early) and turn~21 (late) across all 28 layers of the trained model.\n\nThe gates do the opposite. In 27 of 28 layers, the gate value at turn~1 is lower than at turn~21 (Wilcoxon signed-rank test: $p = 3.73 \\times 10^{-8}$, effect size $r = 0.975$). At layer~23, the gate is 0.769 at turn~1 and 0.979 at turn~21; at layer~14, it is 0.747 at turn~1 and 0.928 at turn~21. The pattern is consistent: gates suppress the residual stream more at early turns (where GAR is already high) and become nearly passive at late turns (where intervention is most needed). This inversion has a straightforward explanation. NTP loss pressure is highest at late turns, where the model must predict tokens conditioned on a long context. The NTP gradient pushes gates toward 1.0 to preserve the full sublayer computation, and this pressure is strongest precisely where GAR-based attenuation would be most useful.\n\nThe resulting inference-time gate values range from 0.93 to 0.98 (2--7\\% attenuation), far below what meaningful modulation would require; this explains the convergence with LoRA-only in Table~\\ref{tab:four-way}. Figure~\\ref{fig:gate-shift}(a) visualizes the per-layer gate difference. The inverted turn conditioning raises a natural question: does the NTP-GAR gradient conflict prevent gates from learning the intended behavior? If gradient conflict is the root cause, resolving it should rescue gate conditioning.\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{fig3_gate_shift.pdf}\n  \\caption{(a)~Gate turn conditioning: per-layer gate values at turn~1 vs turn~21. In 27/28 layers, gates approach 1.0 at late turns, inverting the design intent ($p = 3.73 \\times 10^{-8}$). (b)~Distribution shift: the 20--33$\\times$ GAR gap persists across all five variants (TG, +PCGrad, UG, LoRA-only, Base), the failure is universal across all configurations.}\n  \\label{fig:gate-shift}\n\\end{figure}\n\n\\subsection{PCGrad Causal Exclusion}\\label{subsec:pcgrad}\n\nThe NTP and GAR gradients point in opposing directions across 68--79\\% of layers throughout training, with mean cosine similarity ranging from $-$0.089 (epoch~0) to $-$0.042 (epoch~2). The NTP gradient magnitude dominates by 7.5--14.7$\\times$. This raises a natural hypothesis: perhaps opposing gradient directions prevent the GAR objective from converging. If so, eliminating direction conflict should prevent the collapse. We test this using PCGrad \\citep{yu2020pcgrad}, which projects the gradient of one task onto the normal plane of the other whenever two task gradients conflict. We apply PCGrad to gate parameters only, scoping our claim to direction conflict; magnitude imbalance \\citep{chen2018gradnorm} and Nash equilibrium violations \\citep{navon2022nash} remain untested.\n\nEliminating direction conflict via PCGrad shifts per-step cosine similarity from consistently negative ($-$0.089) to oscillating around zero ($-$0.15 to $+$0.09), yet all outcomes remain unchanged: IID GAR-ours (0.50 vs 0.50), PPL (2.780 vs 2.784), and autoregressive GAR (0.015 vs 0.016) are indistinguishable (Table~\\ref{tab:four-way}). $\\mathcal{L}_\\text{GAR}$ follows a nearly identical training trajectory and collapses in the same manner (Figure~\\ref{fig:training-pcgrad}b). The causal exclusion follows by \\emph{modus tollens}: if direction conflict causes the failure, removing it should prevent it; PCGrad removes it; the failure persists; therefore direction conflict is not the cause. Direction conflict is neither necessary (removing it does not rescue GAR) nor sufficient ($\\mathcal{L}_\\text{GAR}$ converges during training despite persistent conflict). The 7.5--14.7$\\times$ NTP magnitude dominance renders directional interference inconsequential. With gradient conflict ruled out, the question narrows: the training dynamics are not the problem (GAR converges under teacher forcing), so the failure must occur at the transition from training to inference.\n\n\\begin{figure}[t]\n  \\centering\n  \\includegraphics[width=\\columnwidth]{fig2_training_pcgrad.pdf}\n  \\caption{(a)~Gradient cosine similarity between NTP and GAR objectives. ThreadGate remains consistently negative; +PCGrad oscillates around zero. (b)~IID evaluation outcomes are indistinguishable: eliminating direction conflict changes nothing.}\n  \\label{fig:training-pcgrad}\n\\end{figure}\n\n\\subsection{Distribution Shift Analysis}\\label{subsec:dist-shift}\n\nGates are ineffective because NTP pressure pushes them toward identity (\\S\\ref{subsec:gate-conditioning}), and this is not caused by gradient direction conflict (\\S\\ref{subsec:pcgrad}). The remaining question: why do GAR improvements under teacher forcing fail to transfer to autoregressive generation?\n\nThe 20--33$\\times$ GAR gap (Table~\\ref{tab:four-way}) persists across all training strategies: the model learns the intended attention pattern on the training distribution but collapses under model-generated text. GAR-Dongre provides a revealing control: under standard teacher-forced training it remains uniformly low (0.01--0.02) with no distribution gap, so the shift selectively destroys the concentrated last-token attention pattern while leaving diffuse attention unaffected (scheduled sampling breaks this pattern; \\S\\ref{sec:discussion}).\n\nThe mechanism is exposure bias \\citep{bengio2015scheduled}: during training, the model conditions on ground-truth prefixes; at inference, on its own outputs. The statistical properties diverge, and the 2--7\\% gate attenuation (\\S\\ref{subsec:gate-conditioning}) cannot compensate. \\citet{he2019exposure} showed that language models exhibit token-level self-recovery from exposure bias, and our PPL results confirm this (Table~\\ref{tab:four-way}). The critical distinction is between primary and auxiliary objectives: NTP is robust because it is the same task at both training and inference time, while GAR optimizes a distributional property of the input prefix that has no counterpart under autoregressive generation. Figure~\\ref{fig:attention-heatmap} confirms teacher-forced GAR-ours remains near $\\tau = 0.5$ (7--8\\% decay, $N$\\,=\\,45), yet autoregressive GAR collapses for all variants (Figure~\\ref{fig:gate-shift}b).\n\n\\subsection{Mechanism Specificity}\\label{subsec:mechanism-specificity}\n\n\\S\\ref{subsec:dist-shift} showed that exposure bias selectively destroys GAR-ours (20--33$\\times$ gap) while, under standard training, GAR-Dongre remains unaffected. We test whether this selectivity extends beyond attention with an orthogonal hidden-state probe.\n\nWe define Turn-level Residual Coherence (TRC) as the cosine similarity between hidden states at the last-token position of adjacent assistant turns. If exposure bias caused broad representational failure, TRC should show a comparable gap. It does not. For ThreadGate, teacher-forced TRC is 0.334 and autoregressive TRC is 0.332 (gap $= +0.002$). For LoRA-only, teacher-forced TRC is 0.349 and autoregressive TRC is 0.411 (gap $= -0.062$, reversed): autoregressive generation does not degrade hidden-state coherence. Neither checkpoint shows a TRC gap comparable to the 20--33$\\times$ GAR collapse.\n\nThe slightly elevated autoregressive TRC for LoRA-only likely reflects higher token-level predictability in model-generated text, which produces more self-similar hidden states. These results confirm the selectivity from \\S\\ref{subsec:dist-shift} with an orthogonal metric: exposure bias disrupts a specific learned routing behavior (summary-position attention to goal tokens) while leaving internal representations intact.\n\nCross-model evaluation extends this selectivity: GAR-Dongre shows negligible distribution shift on both Llama-3.1-8B (AR/TF ratio 1.002$\\times$) and Qwen-2.5-7B (1.28$\\times$), compared to the 12.5--33$\\times$ collapse in GAR-ours, confirming that exposure bias primarily disrupts attention concentration at generation boundaries rather than aggregate attention patterns (the scheduled sampling experiment in \\S\\ref{sec:discussion} breaks this pattern, with GAR-Dongre rising to 0.353).\n\n\\subsection{Cross-Model Generality}\\label{subsec:cross-model}\n\nTo test whether the exposure bias failure generalizes, we replicate the full evaluation pipeline on Llama-3.1-8B-Instruct \\citep{grattafiori2024llama3}. Phase~1 diagnostics confirm goal attention decay (GAR: 0.026$\\to$0.003 over 10 turns, 90.1\\% decline vs.\\ Qwen's 84.7\\%). A matched evaluation ($N$\\,=\\,50, $T$\\,=\\,4) quantifies the exposure bias gap: teacher-forced GAR-ours is 0.484, autoregressive is 0.039, a 12.5$\\times$ gap directionally consistent with Qwen's 20--33$\\times$. The gate profile differs---Qwen's minimum at layers~3--4, Llama's at layer~25---yet both converge toward identity under NTP pressure. The exposure bias gap is consistent across architecturally distinct LLMs.",
      "numLines": 53,
      "startLine": 1,
      "totalLines": 53
    }
  }
}
```

</details>

---

### Tool call

_source line 65_

<details open><summary>🔧 Tool call — Read · `toolu_017RUKbfjXJaAiuGmvxPva4Z`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "652e1b48-5425-4360-9d09-b4c254656213",
  "uuid": "6d73865e-0837-49ec-9728-1bdf34b460fb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NFJZ7vdQBnx5pz2V6cgxg9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2823,
      "cache_read_input_tokens": 57789,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2823
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

_source line 66 · 2026-05-22T04:38:37.193Z_

<details><summary>↩ Tool result · `toolu_017RUKbfjXJaAiuGmvxPva4Z`</summary>

```text
1	\section{Introduction}\label{sec:introduction}
2	
3	Multi-turn dialogue is the dominant mode of interaction with large language models (LLMs), and system prompts that specify task goals form the foundation of instruction following. As conversations grow longer, however, models progressively lose track of these goal specifications. \citet{dongre2026attention} quantified this degradation across 12 models: the Goal Attention Ratio (GAR), which measures how much attention the model allocates to goal tokens in the system prompt, declines by 27--48\% between early and mid-conversation turns. We replicate and extend this finding on Qwen-2.5-7B-Instruct, observing a 70.8\% relative decline in GAR from 0.0418 at turn~1 to 0.0122 at mid-conversation. We attribute the steeper decline partly to our use of last-token GAR, which captures summary-position attention more sensitively than the all-token average of \citet{dongre2026attention}, and partly to Qwen-2.5-7B's stronger instruction-following fidelity in early turns. This attention decay represents a systematic failure of multi-turn models to maintain task coherence, and it grows worse with each additional turn.
4	
5	A striking aspect of this degradation is what it does \emph{not} affect. \citet{dongre2026attention} showed that goal-relevant information persists in the residual stream throughout the conversation: linear discriminant analysis probes recover goal content with AUC\,=\,0.98 even at late turns where attention to goal tokens has collapsed. The information is present in the hidden states, but the attention mechanism fails to route it toward the output computation. This dissociation between information availability and information utilization suggests a natural intervention: if the residual stream already carries goal information, a learnable gate on the residual pathway could amplify or attenuate layer contributions to recover goal attention. This reasoning motivates ThreadGate, which modulates each residual update with a content-and-turn-conditioned MLP gate: $x_{l+1} = x_l + g_l \cdot f_l(x_l)$, where $g_l$ is produced by a two-layer network conditioned on the hidden state and turn features, inspired by the residual scaling idea of ReZero \citep{bachlechner2021rezero}.
6	
7	\begin{figure*}[t]
8	  \centering
9	  \includegraphics[width=\textwidth]{fig1_overview.pdf}
10	  \caption{Overview of ThreadGate and its failure mode. (Left) ThreadGate adds per-layer content-and-turn-conditioned MLP gates to the residual stream, trained jointly with an auxiliary GAR loss that targets goal attention. (Right) Under teacher-forced evaluation, GAR-ours reaches 0.50 across all fine-tuned variants; under autoregressive generation, it drops to 0.015--0.025, a 20--33$\times$ gap. The five-way comparison (ThreadGate, +PCGrad, Uniform Gate, LoRA-only, Base) shows that no intervention provides measurable benefit over LoRA-only fine-tuning.}
11	  \label{fig:overview}
12	\end{figure*}
13	
14	ThreadGate combines per-layer MLP gate networks with a joint training objective: next-token prediction (NTP), an auxiliary GAR loss ($\tau = 0.5$), and a gate diversity loss (\S\ref{sec:method}). The final formulation emerged from seven iterations spanning four loss families; only MSE target with gate diversity converged stably. To diagnose the failure, we construct a five-way factorial comparison (ThreadGate, +PCGrad, Uniform Gate, LoRA-only, Base) where each pair isolates one causal factor (\S\ref{sec:experiments}). PCGrad \citep{yu2020pcgrad} serves a dual role: training strategy and causal exclusion tool that rules out gradient direction conflict.
15	
16	Training succeeds: teacher-forced GAR-ours reaches 0.50 across all fine-tuned variants. The factorial comparison reveals that the failure is specific to autoregressive generation, where GAR-ours drops to 0.015--0.025, a 20--33$\times$ gap that persists across all training strategies. All four fine-tuned variants achieve indistinguishable performance (0.75\,pp spread on GAR-ours, identical PPL at 2.78); the gating contrast confirms that gates contribute zero measurable benefit. The PCGrad causal exclusion eliminates gradient direction conflict without altering any outcome, establishing that conflict is neither necessary nor sufficient for the failure. These four contrasts converge on a single root cause: exposure bias \citep{bengio2015scheduled}, where attention patterns optimized under teacher-forced prefixes do not transfer to model-generated text (Figure~\ref{fig:overview}). An inference-time steering experiment provides constructive evidence that attention misallocation is the proximal cause: additive attention bias recovers autoregressive GAR from 0.064 to 0.727, bypassing the exposure bias barrier (\S\ref{subsec:steering}). A preliminary scheduled sampling experiment confirms that the gap is also mitigable at training time: GAR-ours increases from 0.016 to 0.318 (20$\times$), compressing the ${\sim}$31$\times$ gap to 1.57$\times$ with no PPL cost (single seed; \S\ref{sec:discussion}).
17	
18	Our contributions: (1)~a systematic causal diagnostic framework for analyzing auxiliary objective failures in multi-turn dialogue, comprising a five-way factorial comparison that isolates four causal factors (turn conditioning, gating mechanism, gradient conflict, and fine-tuning), PCGrad-based causal exclusion via gradient surgery \citep{yu2020pcgrad}, and per-layer gradient conflict quantification; this design pattern is in principle applicable to other auxiliary objective analyses (\S\ref{sec:method}, \S\ref{sec:experiments}, \S\ref{sec:analysis}); (2)~using this framework, the first empirical characterization of how exposure bias selectively destroys auxiliary attention loss generalization (20--33$\times$ gap) while leaving NTP robust, with evidence that token-level self-recovery \citep{he2019exposure} does not extend to auxiliary objectives, a preliminary demonstration that scheduled sampling compresses this gap from ${\sim}$31$\times$ to 1.57$\times$ (single seed), and cross-model confirmation on Llama-3.1-8B (12.5$\times$ gap); (3)~an inference-time steering experiment: additive attention bias at $\beta$\,=\,5 recovers autoregressive GAR from 0.064 to 0.727, providing constructive evidence that attention misallocation---not representation degradation---is the proximal cause under the tested conditions (Qwen-2.5-7B and Llama-3.1-8B, UltraChat, GAR-family losses; \S\ref{subsec:steering}); (4)~a principled negative baseline for future attention steering research: ThreadGate with seven loss formulations and four training configurations ruled out (\S\ref{sec:method}, \S\ref{sec:experiments}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "652e1b48-5425-4360-9d09-b4c254656213",
  "uuid": "f6486a63-b076-4a42-9f70-c3d7118dbfb0",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/introduction.tex",
      "content": "\\section{Introduction}\\label{sec:introduction}\n\nMulti-turn dialogue is the dominant mode of interaction with large language models (LLMs), and system prompts that specify task goals form the foundation of instruction following. As conversations grow longer, however, models progressively lose track of these goal specifications. \\citet{dongre2026attention} quantified this degradation across 12 models: the Goal Attention Ratio (GAR), which measures how much attention the model allocates to goal tokens in the system prompt, declines by 27--48\\% between early and mid-conversation turns. We replicate and extend this finding on Qwen-2.5-7B-Instruct, observing a 70.8\\% relative decline in GAR from 0.0418 at turn~1 to 0.0122 at mid-conversation. We attribute the steeper decline partly to our use of last-token GAR, which captures summary-position attention more sensitively than the all-token average of \\citet{dongre2026attention}, and partly to Qwen-2.5-7B's stronger instruction-following fidelity in early turns. This attention decay represents a systematic failure of multi-turn models to maintain task coherence, and it grows worse with each additional turn.\n\nA striking aspect of this degradation is what it does \\emph{not} affect. \\citet{dongre2026attention} showed that goal-relevant information persists in the residual stream throughout the conversation: linear discriminant analysis probes recover goal content with AUC\\,=\\,0.98 even at late turns where attention to goal tokens has collapsed. The information is present in the hidden states, but the attention mechanism fails to route it toward the output computation. This dissociation between information availability and information utilization suggests a natural intervention: if the residual stream already carries goal information, a learnable gate on the residual pathway could amplify or attenuate layer contributions to recover goal attention. This reasoning motivates ThreadGate, which modulates each residual update with a content-and-turn-conditioned MLP gate: $x_{l+1} = x_l + g_l \\cdot f_l(x_l)$, where $g_l$ is produced by a two-layer network conditioned on the hidden state and turn features, inspired by the residual scaling idea of ReZero \\citep{bachlechner2021rezero}.\n\n\\begin{figure*}[t]\n  \\centering\n  \\includegraphics[width=\\textwidth]{fig1_overview.pdf}\n  \\caption{Overview of ThreadGate and its failure mode. (Left) ThreadGate adds per-layer content-and-turn-conditioned MLP gates to the residual stream, trained jointly with an auxiliary GAR loss that targets goal attention. (Right) Under teacher-forced evaluation, GAR-ours reaches 0.50 across all fine-tuned variants; under autoregressive generation, it drops to 0.015--0.025, a 20--33$\\times$ gap. The five-way comparison (ThreadGate, +PCGrad, Uniform Gate, LoRA-only, Base) shows that no intervention provides measurable benefit over LoRA-only fine-tuning.}\n  \\label{fig:overview}\n\\end{figure*}\n\nThreadGate combines per-layer MLP gate networks with a joint training objective: next-token prediction (NTP), an auxiliary GAR loss ($\\tau = 0.5$), and a gate diversity loss (\\S\\ref{sec:method}). The final formulation emerged from seven iterations spanning four loss families; only MSE target with gate diversity converged stably. To diagnose the failure, we construct a five-way factorial comparison (ThreadGate, +PCGrad, Uniform Gate, LoRA-only, Base) where each pair isolates one causal factor (\\S\\ref{sec:experiments}). PCGrad \\citep{yu2020pcgrad} serves a dual role: training strategy and causal exclusion tool that rules out gradient direction conflict.\n\nTraining succeeds: teacher-forced GAR-ours reaches 0.50 across all fine-tuned variants. The factorial comparison reveals that the failure is specific to autoregressive generation, where GAR-ours drops to 0.015--0.025, a 20--33$\\times$ gap that persists across all training strategies. All four fine-tuned variants achieve indistinguishable performance (0.75\\,pp spread on GAR-ours, identical PPL at 2.78); the gating contrast confirms that gates contribute zero measurable benefit. The PCGrad causal exclusion eliminates gradient direction conflict without altering any outcome, establishing that conflict is neither necessary nor sufficient for the failure. These four contrasts converge on a single root cause: exposure bias \\citep{bengio2015scheduled}, where attention patterns optimized under teacher-forced prefixes do not transfer to model-generated text (Figure~\\ref{fig:overview}). An inference-time steering experiment provides constructive evidence that attention misallocation is the proximal cause: additive attention bias recovers autoregressive GAR from 0.064 to 0.727, bypassing the exposure bias barrier (\\S\\ref{subsec:steering}). A preliminary scheduled sampling experiment confirms that the gap is also mitigable at training time: GAR-ours increases from 0.016 to 0.318 (20$\\times$), compressing the ${\\sim}$31$\\times$ gap to 1.57$\\times$ with no PPL cost (single seed; \\S\\ref{sec:discussion}).\n\nOur contributions: (1)~a systematic causal diagnostic framework for analyzing auxiliary objective failures in multi-turn dialogue, comprising a five-way factorial comparison that isolates four causal factors (turn conditioning, gating mechanism, gradient conflict, and fine-tuning), PCGrad-based causal exclusion via gradient surgery \\citep{yu2020pcgrad}, and per-layer gradient conflict quantification; this design pattern is in principle applicable to other auxiliary objective analyses (\\S\\ref{sec:method}, \\S\\ref{sec:experiments}, \\S\\ref{sec:analysis}); (2)~using this framework, the first empirical characterization of how exposure bias selectively destroys auxiliary attention loss generalization (20--33$\\times$ gap) while leaving NTP robust, with evidence that token-level self-recovery \\citep{he2019exposure} does not extend to auxiliary objectives, a preliminary demonstration that scheduled sampling compresses this gap from ${\\sim}$31$\\times$ to 1.57$\\times$ (single seed), and cross-model confirmation on Llama-3.1-8B (12.5$\\times$ gap); (3)~an inference-time steering experiment: additive attention bias at $\\beta$\\,=\\,5 recovers autoregressive GAR from 0.064 to 0.727, providing constructive evidence that attention misallocation---not representation degradation---is the proximal cause under the tested conditions (Qwen-2.5-7B and Llama-3.1-8B, UltraChat, GAR-family losses; \\S\\ref{subsec:steering}); (4)~a principled negative baseline for future attention steering research: ThreadGate with seven loss formulations and four training configurations ruled out (\\S\\ref{sec:method}, \\S\\ref{sec:experiments}).",
      "numLines": 18,
      "startLine": 1,
      "totalLines": 18
    }
  }
}
```

</details>

---

### Tool call

_source line 67_

<details open><summary>🔧 Tool call — Read · `toolu_01Nrkk3A6BmkhSpjaSDHEnZe`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "652e1b48-5425-4360-9d09-b4c254656213",
  "uuid": "8654a6c3-2e5e-479b-912a-8465492f44b8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NFJZ7vdQBnx5pz2V6cgxg9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2823,
      "cache_read_input_tokens": 57789,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2823
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

_source line 68 · 2026-05-22T04:38:37.722Z_

<details><summary>↩ Tool result · `toolu_01Nrkk3A6BmkhSpjaSDHEnZe`</summary>

```text
1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Multi-turn attention degradation.}
4	Recent work has established that LLMs systematically degrade across conversation turns. \citet{levy2025lost} showed that model performance drops on tasks placed in later turns, even when the tasks are identical to earlier ones. \citet{liu2026intent} traced a related failure to intent mismatch, where models progressively shift from the user's original intent as dialogue extends. MT-Bench-101 \citep{bai2024mtbench101} provides fine-grained multi-turn evaluation across 1388 turn-level instances, revealing that capability varies substantially across task categories. \citet{dongre2026attention} established the quantitative foundation for this line of work: they defined the Goal Attention Ratio (GAR) and showed that attention to system-prompt goal tokens decays by 27--48\% across turns in 12 models, while residual stream probes retain goal information with AUC\,=\,0.98. We observe a steeper 70.8\% decline on Qwen-2.5-7B-Instruct (\S\ref{sec:experiments}). This dissociation between attention collapse and residual persistence motivates our gating intervention. Their work characterizes the phenomenon; ours attempts the first systematic cure and, in doing so, uncovers why lightweight interventions fail to transfer from training to inference.
5	
6	\paragraph{Residual gating and adaptive depth.}
7	ReZero \citep{bachlechner2021rezero} showed that residual scaling shapes optimization dynamics. Subsequent work targets computational efficiency: LayerDrop \citep{fan2020layerdrop}, Mixture-of-Depths \citep{raposo2024mixture}, FlexiDepth \citep{luo2025flexidepth}, and CALM \citep{schuster2022calm}. ThreadGate applies residual gating to a different objective: recovering attention patterns in multi-turn dialogue.
8	
9	\paragraph{Attention manipulation.}
10	StreamingLLM \citep{xiao2024streaming} identified attention sinks and proposed anchor token retention; \citet{ko2024found} showed positional bias against middle-positioned information; \citet{qiu2025gated} replaced softmax with a learned gate for sparse attention. These approaches intervene inside the attention mechanism, while ThreadGate operates on the residual stream. Our results suggest that neither pathway alone overcomes the distributional gap between teacher-forced training and autoregressive inference.
11	
12	\paragraph{Multi-task gradient conflict.}
13	GradNorm \citep{chen2018gradnorm}, PCGrad \citep{yu2020pcgrad}, CAGrad \citep{liu2021cagrad}, and Nash-MTL \citep{navon2022nash} treat gradient conflict between competing losses as a root cause to be resolved through better optimization. We repurpose PCGrad as a causal analysis tool: eliminating directional conflict between NTP and GAR gradients does not improve GAR convergence. Gradient conflict is a symptom rather than the cause.
14	
15	\paragraph{Exposure bias.}
16	Teacher forcing creates a distributional mismatch between training and inference that compounds over sequence length. Scheduled Sampling \citep{bengio2015scheduled} introduced curriculum-based mixing of ground-truth and model-generated tokens. MIXER \citep{ranzato2016sequence} combined token-level and sequence-level objectives, and Professor Forcing \citep{lamb2016professor} used adversarial regularization to align hidden state distributions under both regimes. \citet{he2019exposure} showed that autoregressive models exhibit self-recovery from exposure bias at the token prediction level. SEARNN \citep{leblond2018searnn} proposed locally recurrent search-based training to avoid the mismatch entirely. This literature focuses on generation quality degradation in primary objectives. No prior work examines how exposure bias affects auxiliary objectives that target attention distributions, nor how it manifests in multi-turn dialogue settings. Our work identifies a distinct failure mode: auxiliary attention losses that converge under teacher forcing fail completely under autoregressive generation, even when NTP remains robust, because token-level self-recovery does not extend to distributional properties of attention.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "652e1b48-5425-4360-9d09-b4c254656213",
  "uuid": "38e812f4-9056-48d7-8cfe-f9e63cb17bce",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/related_work.tex",
      "content": "\\section{Related Work}\\label{sec:related}\n\n\\paragraph{Multi-turn attention degradation.}\nRecent work has established that LLMs systematically degrade across conversation turns. \\citet{levy2025lost} showed that model performance drops on tasks placed in later turns, even when the tasks are identical to earlier ones. \\citet{liu2026intent} traced a related failure to intent mismatch, where models progressively shift from the user's original intent as dialogue extends. MT-Bench-101 \\citep{bai2024mtbench101} provides fine-grained multi-turn evaluation across 1388 turn-level instances, revealing that capability varies substantially across task categories. \\citet{dongre2026attention} established the quantitative foundation for this line of work: they defined the Goal Attention Ratio (GAR) and showed that attention to system-prompt goal tokens decays by 27--48\\% across turns in 12 models, while residual stream probes retain goal information with AUC\\,=\\,0.98. We observe a steeper 70.8\\% decline on Qwen-2.5-7B-Instruct (\\S\\ref{sec:experiments}). This dissociation between attention collapse and residual persistence motivates our gating intervention. Their work characterizes the phenomenon; ours attempts the first systematic cure and, in doing so, uncovers why lightweight interventions fail to transfer from training to inference.\n\n\\paragraph{Residual gating and adaptive depth.}\nReZero \\citep{bachlechner2021rezero} showed that residual scaling shapes optimization dynamics. Subsequent work targets computational efficiency: LayerDrop \\citep{fan2020layerdrop}, Mixture-of-Depths \\citep{raposo2024mixture}, FlexiDepth \\citep{luo2025flexidepth}, and CALM \\citep{schuster2022calm}. ThreadGate applies residual gating to a different objective: recovering attention patterns in multi-turn dialogue.\n\n\\paragraph{Attention manipulation.}\nStreamingLLM \\citep{xiao2024streaming} identified attention sinks and proposed anchor token retention; \\citet{ko2024found} showed positional bias against middle-positioned information; \\citet{qiu2025gated} replaced softmax with a learned gate for sparse attention. These approaches intervene inside the attention mechanism, while ThreadGate operates on the residual stream. Our results suggest that neither pathway alone overcomes the distributional gap between teacher-forced training and autoregressive inference.\n\n\\paragraph{Multi-task gradient conflict.}\nGradNorm \\citep{chen2018gradnorm}, PCGrad \\citep{yu2020pcgrad}, CAGrad \\citep{liu2021cagrad}, and Nash-MTL \\citep{navon2022nash} treat gradient conflict between competing losses as a root cause to be resolved through better optimization. We repurpose PCGrad as a causal analysis tool: eliminating directional conflict between NTP and GAR gradients does not improve GAR convergence. Gradient conflict is a symptom rather than the cause.\n\n\\paragraph{Exposure bias.}\nTeacher forcing creates a distributional mismatch between training and inference that compounds over sequence length. Scheduled Sampling \\citep{bengio2015scheduled} introduced curriculum-based mixing of ground-truth and model-generated tokens. MIXER \\citep{ranzato2016sequence} combined token-level and sequence-level objectives, and Professor Forcing \\citep{lamb2016professor} used adversarial regularization to align hidden state distributions under both regimes. \\citet{he2019exposure} showed that autoregressive models exhibit self-recovery from exposure bias at the token prediction level. SEARNN \\citep{leblond2018searnn} proposed locally recurrent search-based training to avoid the mismatch entirely. This literature focuses on generation quality degradation in primary objectives. No prior work examines how exposure bias affects auxiliary objectives that target attention distributions, nor how it manifests in multi-turn dialogue settings. Our work identifies a distinct failure mode: auxiliary attention losses that converge under teacher forcing fail completely under autoregressive generation, even when NTP remains robust, because token-level self-recovery does not extend to distributional properties of attention.",
      "numLines": 16,
      "startLine": 1,
      "totalLines": 16
    }
  }
}
```

</details>

---

### Tool call

_source line 69_

<details open><summary>🔧 Tool call — Read · `toolu_01Chby794CU8ycWhc9QurmvU`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "652e1b48-5425-4360-9d09-b4c254656213",
  "uuid": "35ab7c13-bbb1-437c-bf07-d24c24568376",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NFJZ7vdQBnx5pz2V6cgxg9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2823,
      "cache_read_input_tokens": 57789,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2823
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

_source line 70 · 2026-05-22T04:38:38.107Z_

<details><summary>↩ Tool result · `toolu_01Chby794CU8ycWhc9QurmvU`</summary>

```text
1	\section{Discussion}\label{sec:discussion}
2	
3	The failure traces to an incompatibility between teacher-forcing and GAR-family auxiliary losses, not to the gating architecture. NTP gradient pressure (7.5--14.7$\times$ the GAR magnitude) pushes gates toward identity (2--7\% attenuation), while inference-time steering ($\beta$\,=\,5) recovers GAR from 0.064 to 0.727, providing constructive evidence that attention misallocation is the proximal cause (\S\ref{subsec:steering}).
4	
5	\paragraph{Scheduled sampling as training-time mitigation.} A preliminary experiment (single seed) applies scheduled sampling \citep{bengio2015scheduled}, linearly mixing teacher-forced and model-generated contexts. Autoregressive GAR-ours increases from 0.016 to 0.318 (20$\times$), compressing the ${\sim}$31$\times$ gap to 1.57$\times$ with negligible PPL change (1.38 vs.\ 1.36). GAR-Dongre also rises (0.019$\to$0.353), suggesting indirect improvement of all-token goal attention. The two paths are complementary: $\beta$\,=\,5 achieves the strongest GAR recovery but incurs 24\% PPL cost (1.43\,$\to$\,1.77); $\beta$\,=\,3 offers a more balanced tradeoff (PPL +9\%). Scheduled sampling incurs no fluency cost but requires retraining. A second seed trained from scratch (rather than resumed from a standard-trained epoch) yields AR GAR\,=\,0.418 (gap 1.20$\times$), versus 5\% seed variance in standard ThreadGate training, suggesting that early scheduled sampling exposure---before the model consolidates teacher-forced attention patterns---may further compress the gap; systematic schedule ablation is deferred.
6	
7	\paragraph{Instruction retention under steering.} Across 18 system-prompt constraint types, $\beta$\,=\,3 steering increases content constraint compliance by +23.8\,pp (GAR-compliance $r$\,=\,0.200, $p$\,=\,0.007; McNemar $p$\,=\,0.077), providing exploratory evidence for downstream benefit pending multi-model confirmation.
8	
9	TRC analysis (\S\ref{subsec:mechanism-specificity}) confirms the mismatch targets attention routing without disrupting hidden-state coherence. We scope claims to GAR losses on Qwen-2.5-7B and Llama-3.1-8B; magnitude imbalance \citep{chen2018gradnorm} and Nash equilibria \citep{navon2022nash} remain untested. Remaining directions include adaptive $\beta$ scheduling and layer-selective steering.
10	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "652e1b48-5425-4360-9d09-b4c254656213",
  "uuid": "edcd73d1-4f28-454a-a9b1-9bd37afe570e",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/discussion.tex",
      "content": "\\section{Discussion}\\label{sec:discussion}\n\nThe failure traces to an incompatibility between teacher-forcing and GAR-family auxiliary losses, not to the gating architecture. NTP gradient pressure (7.5--14.7$\\times$ the GAR magnitude) pushes gates toward identity (2--7\\% attenuation), while inference-time steering ($\\beta$\\,=\\,5) recovers GAR from 0.064 to 0.727, providing constructive evidence that attention misallocation is the proximal cause (\\S\\ref{subsec:steering}).\n\n\\paragraph{Scheduled sampling as training-time mitigation.} A preliminary experiment (single seed) applies scheduled sampling \\citep{bengio2015scheduled}, linearly mixing teacher-forced and model-generated contexts. Autoregressive GAR-ours increases from 0.016 to 0.318 (20$\\times$), compressing the ${\\sim}$31$\\times$ gap to 1.57$\\times$ with negligible PPL change (1.38 vs.\\ 1.36). GAR-Dongre also rises (0.019$\\to$0.353), suggesting indirect improvement of all-token goal attention. The two paths are complementary: $\\beta$\\,=\\,5 achieves the strongest GAR recovery but incurs 24\\% PPL cost (1.43\\,$\\to$\\,1.77); $\\beta$\\,=\\,3 offers a more balanced tradeoff (PPL +9\\%). Scheduled sampling incurs no fluency cost but requires retraining. A second seed trained from scratch (rather than resumed from a standard-trained epoch) yields AR GAR\\,=\\,0.418 (gap 1.20$\\times$), versus 5\\% seed variance in standard ThreadGate training, suggesting that early scheduled sampling exposure---before the model consolidates teacher-forced attention patterns---may further compress the gap; systematic schedule ablation is deferred.\n\n\\paragraph{Instruction retention under steering.} Across 18 system-prompt constraint types, $\\beta$\\,=\\,3 steering increases content constraint compliance by +23.8\\,pp (GAR-compliance $r$\\,=\\,0.200, $p$\\,=\\,0.007; McNemar $p$\\,=\\,0.077), providing exploratory evidence for downstream benefit pending multi-model confirmation.\n\nTRC analysis (\\S\\ref{subsec:mechanism-specificity}) confirms the mismatch targets attention routing without disrupting hidden-state coherence. We scope claims to GAR losses on Qwen-2.5-7B and Llama-3.1-8B; magnitude imbalance \\citep{chen2018gradnorm} and Nash equilibria \\citep{navon2022nash} remain untested. Remaining directions include adaptive $\\beta$ scheduling and layer-selective steering.\n",
      "numLines": 10,
      "startLine": 1,
      "totalLines": 10
    }
  }
}
```

</details>

---

### Tool call

_source line 71_

<details open><summary>🔧 Tool call — Read · `toolu_01QkK8dtyeidEQqPsizfsuuY`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/background.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "652e1b48-5425-4360-9d09-b4c254656213",
  "uuid": "f8e8ebe4-abde-4c82-8d92-136c5559906d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NFJZ7vdQBnx5pz2V6cgxg9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2823,
      "cache_read_input_tokens": 57789,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2823
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

_source line 72 · 2026-05-22T04:38:38.511Z_

<details><summary>↩ Tool result · `toolu_01QkK8dtyeidEQqPsizfsuuY`</summary>

```text
1	\section{Background}\label{sec:background}
2	
3	\paragraph{Goal Attention Ratio.}
4	Multi-turn instruction-following models receive a system prompt that specifies the task objective. We denote the token subsequence corresponding to the task specification within this system prompt as the \emph{goal tokens} $\mathcal{G}$, excluding formatting markers and role tags. \citet{dongre2026attention} introduced the Goal Attention Ratio (GAR) to quantify how much attention a model allocates to these goal tokens during response generation. Given a model with $L$ layers and $H$ attention heads, GAR at conversation turn $\tau$ is
5	\begin{equation}\label{eq:gar}
6	  \text{GAR}(\tau) = \frac{1}{L \cdot H \cdot |\mathcal{R}_\tau|} \sum_{\ell=1}^{L} \sum_{h=1}^{H} \sum_{i \in \mathcal{R}_\tau} \sum_{j \in \mathcal{G}} A_{i,j}^{(\ell,h)},
7	\end{equation}
8	where $\mathcal{R}_\tau$ is the set of response tokens at turn $\tau$ and $A_{i,j}^{(\ell,h)}$ is the attention weight from token $i$ to token $j$ at layer $\ell$, head $h$. This definition averages attention to goal tokens over all response positions, all layers, and all heads.
9	
10	\paragraph{Two GAR variants.}
11	We distinguish two measurement variants throughout this paper. \textbf{GAR-Dongre} refers to the original definition in Equation~\ref{eq:gar}, which averages over the full response token set $\mathcal{R}_\tau$. \textbf{GAR-ours} restricts the measurement to the \emph{last token} of each assistant turn:
12	\begin{equation}\label{eq:gar-ours}
13	  \text{GAR\text{-}ours}(\tau) = \frac{1}{L \cdot H} \sum_{\ell=1}^{L} \sum_{h=1}^{H} \sum_{j \in \mathcal{G}} A_{t_\tau,\, j}^{(\ell,h)},
14	\end{equation}
15	where $t_\tau$ is the index of the last token in the assistant response at turn $\tau$. The last token is the position at which the model conditions its next generation step, so attention patterns at this position most directly reflect the information the model draws upon for continuation. We use GAR-ours as the optimization target for the auxiliary loss $\mathcal{L}_\text{GAR}$ (\S\ref{sec:loss}), while GAR-Dongre provides a complementary aggregate measure for comparison.
16	
17	\paragraph{Residual stream persistence.}
18	\citet{dongre2026attention} showed that goal-relevant information persists in the residual stream (probe AUC\,=\,0.98) even at late turns where GAR has collapsed. The information is present but the attention mechanism fails to route it. This dissociation motivates an intervention that targets the residual pathway directly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "652e1b48-5425-4360-9d09-b4c254656213",
  "uuid": "e2727784-ebdf-4302-a952-dcbdb33aa633",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/background.tex",
      "content": "\\section{Background}\\label{sec:background}\n\n\\paragraph{Goal Attention Ratio.}\nMulti-turn instruction-following models receive a system prompt that specifies the task objective. We denote the token subsequence corresponding to the task specification within this system prompt as the \\emph{goal tokens} $\\mathcal{G}$, excluding formatting markers and role tags. \\citet{dongre2026attention} introduced the Goal Attention Ratio (GAR) to quantify how much attention a model allocates to these goal tokens during response generation. Given a model with $L$ layers and $H$ attention heads, GAR at conversation turn $\\tau$ is\n\\begin{equation}\\label{eq:gar}\n  \\text{GAR}(\\tau) = \\frac{1}{L \\cdot H \\cdot |\\mathcal{R}_\\tau|} \\sum_{\\ell=1}^{L} \\sum_{h=1}^{H} \\sum_{i \\in \\mathcal{R}_\\tau} \\sum_{j \\in \\mathcal{G}} A_{i,j}^{(\\ell,h)},\n\\end{equation}\nwhere $\\mathcal{R}_\\tau$ is the set of response tokens at turn $\\tau$ and $A_{i,j}^{(\\ell,h)}$ is the attention weight from token $i$ to token $j$ at layer $\\ell$, head $h$. This definition averages attention to goal tokens over all response positions, all layers, and all heads.\n\n\\paragraph{Two GAR variants.}\nWe distinguish two measurement variants throughout this paper. \\textbf{GAR-Dongre} refers to the original definition in Equation~\\ref{eq:gar}, which averages over the full response token set $\\mathcal{R}_\\tau$. \\textbf{GAR-ours} restricts the measurement to the \\emph{last token} of each assistant turn:\n\\begin{equation}\\label{eq:gar-ours}\n  \\text{GAR\\text{-}ours}(\\tau) = \\frac{1}{L \\cdot H} \\sum_{\\ell=1}^{L} \\sum_{h=1}^{H} \\sum_{j \\in \\mathcal{G}} A_{t_\\tau,\\, j}^{(\\ell,h)},\n\\end{equation}\nwhere $t_\\tau$ is the index of the last token in the assistant response at turn $\\tau$. The last token is the position at which the model conditions its next generation step, so attention patterns at this position most directly reflect the information the model draws upon for continuation. We use GAR-ours as the optimization target for the auxiliary loss $\\mathcal{L}_\\text{GAR}$ (\\S\\ref{sec:loss}), while GAR-Dongre provides a complementary aggregate measure for comparison.\n\n\\paragraph{Residual stream persistence.}\n\\citet{dongre2026attention} showed that goal-relevant information persists in the residual stream (probe AUC\\,=\\,0.98) even at late turns where GAR has collapsed. The information is present but the attention mechanism fails to route it. This dissociation motivates an intervention that targets the residual pathway directly.",
      "numLines": 18,
      "startLine": 1,
      "totalLines": 18
    }
  }
}
```

</details>

---

### Assistant

_source line 73_

<details><summary>Logged reasoning block</summary>

```text
Now I have a complete picture. Let me compile the full list of cited keys and cross-reference with the bib.

**Cited keys from all tex files:**

From introduction.tex:
- dongre2026attention (multiple times)
- bachlechner2021rezero
- yu2020pcgrad
- bengio2015scheduled
- he2019exposure

From background.tex:
- dongre2026attention (multiple times)

From method.tex:
- dongre2026attention
- bachlechner2021rezero

From related_work.tex:
- levy2025lost


- liu2026intent
- bai2024mtbench101
- fan2020layerdrop
- raposo2024mixture
- luo2025flexidepth
- schuster2022calm
- xiao2024streaming
- ko2024found
- qiu2025gated
- chen2018gradnorm
- liu2021cagrad
- navon2022nash
- ranzato2016sequence
- lamb2016professor
- leblond2018searnn

From experiments.tex:
- dongre2026attention

From analysis.tex:
- yu2020pcgrad
- chen2...

Now I'm cross-referencing citations across the different sections—experiments, analysis, and discussion—to identify which papers appear multiple times and which are unique to specific parts of the document. I'm also noticing a few citations that span across sections like bengio2015scheduled, chen2018gradnorm, and navon2022nash, while others like levy2025lost and grattafiori2024llama3 appear only in certain sections. Compiling the full list of unique citations across all sections. I've identified the remaining 24 orphan entries in the bibliography that aren't cited anywhere in the document. Now I'm compiling the audit report and verifying the citations—all 22 cited entries check out as real papers with no hallucinations, though I'm finding some format and accuracy issues that need attention, starting with the he2019exposure entry where the arXiv title was updated in later versions. Looking at the search results more carefully, the versioning is confusing—v4 still shows the original title while the latest version has a different one, so I'll just note this as a potential discrepancy. Now I'm spotting several author attribution errors in the bibliography: the first author for `levy2025lost` is actually Laban, not Levy; `ko2024found` should be credited to Hsieh; and a couple entries incorrectly list "Anonymous" when the actual first authors are Lu and Lin respectively.

For `grattafiori2024llama3`, the author field awkwardly says "1 others" which isn't standard formatting—it should either list the co-authors or use "and others" properly. I'm also noting some warnings about potential false positives from OpenAlex mismatches and one arXiv paper where the latest version might have a different title than what's currently recorded.

There's also an inconsistency in how authors are formatted across entries—some list all names while others use "and others"—so I should standardize that. The `grattafiori2024llama3` entry is missing a URL field entirely, and `elhage2021framework` is technically a blog post rather than a journal article, though using "Anthropic Blog" as the journal is acceptable if unconventional.

I've spotted a duplicate bibliography file at `paper/sections/references.bib` that mirrors `paper/references.bib`, but only the latter is actually used by the main document, so the duplicate should be removed or kept synchronized to avoid confusion.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "652e1b48-5425-4360-9d09-b4c254656213",
  "uuid": "f64c3e28-af8a-4073-a0bd-3941f63e7154",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C592YggBpgV9pNgbvYAfyn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7640,
      "cache_read_input_tokens": 60612,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7640
      },
      "output_tokens": 12,
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

_source line 74_

所有数据收集完毕。下面是审计报告。

---

## 引用审计报告

**总数**: 46 条 bib 条目（22 条被引用，24 条 orphan）  
**真实性**: 22/22 被引用条目均为真实论文  
**格式问题**: 5 条需修复  
**结构问题**: 1 个重复 bib 文件

---

### A. 真实性验证

所有 22 条被引用条目通过 WebSearch 验证为真实论文，无幻觉引用。

OpenAlex 报告 3 条 `not_found`，均为索引问题而非真实性问题：

| Key | 原因 |
|-----|------|
| `fan2020layerdrop` | Fan, Grave, Joulin. ICLR 2020. OpenAlex 索引缺失，论文真实 |
| `luo2025flexidepth` | Xuan Luo et al. arXiv 2503.23798. OpenAlex 未收录，论文真实 |
| `elhage2021framework` | Elhage et al. Anthropic blog post，非正式论文，不在 OpenAlex 中 |

---

### B. 需修复的错误（5 条）

**1. [severity: critical] `levy2025lost` — 第一作者错误**
- bib 写 `Levy and others`，实际第一作者是 **Philippe Laban**
- 修复: `author = {Laban and others}`

**2. [severity: critical] `ko2024found` — 第一作者错误**
- bib 写 `Ko and others`，实际第一作者是 **Cheng-Yu Hsieh**
- 修复: `author = {Hsieh and others}`

**3. [severity: warning] `anonymous2024reassessing` — 应使用真实作者**
- 论文已公开，第一作者是 Yao Lu
- 修复: `author = {Lu and others}`

**4. [severity: warning] `anonymous2025style` — 应使用真实作者**
- 论文已公开，第一作者是 Yu-Xiang Lin
- 修复: `author = {Lin and others}`

**5. [severity: warning] `grattafiori2024llama3` — author 字段异常 + 缺 URL**
- `author = {Grattafiori and 1 others}` 中 `1 others` 非标准
- 修复: `author = {Grattafiori and others}`, 补 `url = {https://arxiv.org/abs/2407.21783}`

---

### C. 格式一致性

**Author 格式不统一**：部分条目列全部作者（如 `Bengio and Vinyals and Jaitly and Shazeer`），部分用 `Last and others`。建议统一为其中一种风格。当前引用的 22 条中：
- 全部作者列表: bengio2015scheduled, ranzato2016sequence, lamb2016professor, leblond2018searnn, he2019exposure, yu2020pcgrad, chen2018gradnorm, liu2021cagrad, navon2022nash, bachlechner2021rezero, dongre2026attention
- `and others` 缩写: 其余 11 条

**`he2019exposure` arXiv 标题变更**：arXiv 1905.10617 最新版标题改为 "Exposure Bias versus Self-Recovery..."，bib 中使用 v1 标题。如论文引用的是 v1 内容则可保留，否则建议更新。

---

### D. 完整性

**Missing（引用了但 bib 没有）**: 0 条

**Orphan（bib 有但未引用）**: 24 条

| 分类 | 条目 |
|------|------|
| Layer Importance | gromov2024deeper, men2024shortgpt, sun2025curse, anonymous2024reassessing |
| Multi-Turn | liu2023lost, anonymous2025style |
| Residual Gating | wang2018skipnet, lawson2025skip |
| Attention Manipulation | press2022alibi, chen2023positional, peng2024yarn, han2024lminfinite |
| Theoretical | elhage2021framework, elhage2022superposition, belrose2023tuned, yu2023residual, makkuva2025markov, ildiz2024markov |
| Benchmarks | zheng2023mtbench, chiang2024arena, dubois2024alpacaeval, lin2024wildbench, sirdeshmukh2025multichallenge |
| Residual Scaling | zhang2019fixup |

建议：删除 orphan 条目，或在正文中补充引用。

**重复 bib 文件**: `paper/sections/references.bib` 是 `paper/references.bib` 的副本。`main.tex` 只引用后者。建议删除 `paper/sections/references.bib` 以避免维护不一致。

---

### E. 修复优先级

1. **立即修复**: `levy2025lost` 和 `ko2024found` 的第一作者错误（reviewer 一查即发现）
2. **应修复**: anonymous 条目替换为真实作者、`grattafiori2024llama3` 格式修正
3. **建议修复**: 清理 24 条 orphan 条目、统一 author 格式、删除重复 bib 文件

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "652e1b48-5425-4360-9d09-b4c254656213",
  "uuid": "45b35f99-82b4-4251-9592-22674ad30496",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C592YggBpgV9pNgbvYAfyn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7640,
      "cache_read_input_tokens": 60612,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7640
      },
      "output_tokens": 12,
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

_source line 75_

所有数据收集完毕。下面是审计报告。

---

## 引用审计报告

**总数**: 46 条 bib 条目（22 条被引用，24 条 orphan）  
**真实性**: 22/22 被引用条目均为真实论文  
**格式问题**: 5 条需修复  
**结构问题**: 1 个重复 bib 文件

---

### A. 真实性验证

所有 22 条被引用条目通过 WebSearch 验证为真实论文，无幻觉引用。

OpenAlex 报告 3 条 `not_found`，均为索引问题而非真实性问题：

| Key | 原因 |
|-----|------|
| `fan2020layerdrop` | Fan, Grave, Joulin. ICLR 2020. OpenAlex 索引缺失，论文真实 |
| `luo2025flexidepth` | Xuan Luo et al. arXiv 2503.23798. OpenAlex 未收录，论文真实 |
| `elhage2021framework` | Elhage et al. Anthropic blog post，非正式论文，不在 OpenAlex 中 |

---

### B. 需修复的错误（5 条）

**1. [severity: critical] `levy2025lost` — 第一作者错误**
- bib 写 `Levy and others`，实际第一作者是 **Philippe Laban**
- 修复: `author = {Laban and others}`

**2. [severity: critical] `ko2024found` — 第一作者错误**
- bib 写 `Ko and others`，实际第一作者是 **Cheng-Yu Hsieh**
- 修复: `author = {Hsieh and others}`

**3. [severity: warning] `anonymous2024reassessing` — 应使用真实作者**
- 论文已公开，第一作者是 Yao Lu
- 修复: `author = {Lu and others}`

**4. [severity: warning] `anonymous2025style` — 应使用真实作者**
- 论文已公开，第一作者是 Yu-Xiang Lin
- 修复: `author = {Lin and others}`

**5. [severity: warning] `grattafiori2024llama3` — author 字段异常 + 缺 URL**
- `author = {Grattafiori and 1 others}` 中 `1 others` 非标准
- 修复: `author = {Grattafiori and others}`, 补 `url = {https://arxiv.org/abs/2407.21783}`

---

### C. 格式一致性

**Author 格式不统一**：部分条目列全部作者（如 `Bengio and Vinyals and Jaitly and Shazeer`），部分用 `Last and others`。建议统一为其中一种风格。当前引用的 22 条中：
- 全部作者列表: bengio2015scheduled, ranzato2016sequence, lamb2016professor, leblond2018searnn, he2019exposure, yu2020pcgrad, chen2018gradnorm, liu2021cagrad, navon2022nash, bachlechner2021rezero, dongre2026attention
- `and others` 缩写: 其余 11 条

**`he2019exposure` arXiv 标题变更**：arXiv 1905.10617 最新版标题改为 "Exposure Bias versus Self-Recovery..."，bib 中使用 v1 标题。如论文引用的是 v1 内容则可保留，否则建议更新。

---

### D. 完整性

**Missing（引用了但 bib 没有）**: 0 条

**Orphan（bib 有但未引用）**: 24 条

| 分类 | 条目 |
|------|------|
| Layer Importance | gromov2024deeper, men2024shortgpt, sun2025curse, anonymous2024reassessing |
| Multi-Turn | liu2023lost, anonymous2025style |
| Residual Gating | wang2018skipnet, lawson2025skip |
| Attention Manipulation | press2022alibi, chen2023positional, peng2024yarn, han2024lminfinite |
| Theoretical | elhage2021framework, elhage2022superposition, belrose2023tuned, yu2023residual, makkuva2025markov, ildiz2024markov |
| Benchmarks | zheng2023mtbench, chiang2024arena, dubois2024alpacaeval, lin2024wildbench, sirdeshmukh2025multichallenge |
| Residual Scaling | zhang2019fixup |

建议：删除 orphan 条目，或在正文中补充引用。

**重复 bib 文件**: `paper/sections/references.bib` 是 `paper/references.bib` 的副本。`main.tex` 只引用后者。建议删除 `paper/sections/references.bib` 以避免维护不一致。

---

### E. 修复优先级

1. **立即修复**: `levy2025lost` 和 `ko2024found` 的第一作者错误（reviewer 一查即发现）
2. **应修复**: anonymous 条目替换为真实作者、`grattafiori2024llama3` 格式修正
3. **建议修复**: 清理 24 条 orphan 条目、统一 author 格式、删除重复 bib 文件

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 580490,
  "duration_api_ms": 279142,
  "num_turns": 29,
  "stop_reason": "end_turn",
  "session_id": "652e1b48-5425-4360-9d09-b4c254656213",
  "total_cost_usd": 1.0814052500000002,
  "usage": {
    "input_tokens": 15,
    "cache_creation_input_tokens": 56411,
    "cache_read_input_tokens": 411453,
    "output_tokens": 8551,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 56411,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 3281,
        "cache_read_input_tokens": 60612,
        "cache_creation_input_tokens": 7640,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 7640
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 142580,
      "outputTokens": 5336,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 14,
      "costUSD": 0.3092599999999999,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 15,
      "outputTokens": 8551,
      "cacheReadInputTokens": 411453,
      "cacheCreationInputTokens": 56411,
      "webSearchRequests": 0,
      "costUSD": 0.7721452500000001,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "913c4414-e0df-4636-acac-c08e66e89115"
}
```

</details>

---
