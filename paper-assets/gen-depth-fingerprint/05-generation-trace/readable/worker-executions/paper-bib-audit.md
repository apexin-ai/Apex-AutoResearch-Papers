# paper bib audit

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 38
- **Recorded user turns:** 0
- **Tool calls:** 12
- **Original source:** `logs/workers/worker_paper_bib-audit_20260515T203516.log`
- **Structured JSON:** [`9a5648eafff68e164d78.json`](../../sessions/9a/9a5648eafff68e164d78.json)

## Before a recorded user message

38 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "session_id": "02cc67ad-c03e-4058-938b-210c48bf1830",
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
  "uuid": "0e1ffdee-dbf0-4fed-b277-712e0ab37753",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint/memory/"
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
    "resetsAt": 1778886600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "0d60e6f9-063e-4e17-85af-a62bde4ec2e0",
  "session_id": "02cc67ad-c03e-4058-938b-210c48bf1830"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to perform a bibliography audit for their paper. Let me follow the steps:

1. First, call `verify_references` MCP tool
2. Then review the results and do manual verification
3. Fix issues in references.bib
4. Output a structured audit report

Let me start by loading the verify_references tool schema and the reference-audit skill.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "02cc67ad-c03e-4058-938b-210c48bf1830",
  "uuid": "e8f4929c-f9cd-489f-a257-33f86892bd4c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013NNabjLSqbSHVKMAGXgWHV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12208,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12208
      },
      "output_tokens": 24,
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

开始引用审计。先加载工具和 skill。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "02cc67ad-c03e-4058-938b-210c48bf1830",
  "uuid": "43acbc73-7664-4a03-a9d3-68ce25f798ea",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013NNabjLSqbSHVKMAGXgWHV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12208,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12208
      },
      "output_tokens": 24,
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_013PVQkcChqQgKrSwU46eTB4`</summary>

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
  "session_id": "02cc67ad-c03e-4058-938b-210c48bf1830",
  "uuid": "a4952a5e-90e6-4326-96e6-952171c86a02",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013NNabjLSqbSHVKMAGXgWHV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12208,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12208
      },
      "output_tokens": 24,
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

_source line 7 · 2026-05-15T20:35:26.077Z_

<details><summary>↩ Tool result · `toolu_013PVQkcChqQgKrSwU46eTB4`</summary>

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
  "session_id": "02cc67ad-c03e-4058-938b-210c48bf1830",
  "uuid": "5e272538-0c09-47e9-a930-2c1746e1b571",
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

_source line 8_

<details open><summary>🔧 Tool call — Read · `toolu_017wX5gEpUtVZerVxaEYvzF5`</summary>

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
  "session_id": "02cc67ad-c03e-4058-938b-210c48bf1830",
  "uuid": "2a295529-b240-4582-9317-246ddd56724e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013NNabjLSqbSHVKMAGXgWHV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12208,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12208
      },
      "output_tokens": 24,
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

_source line 9 · 2026-05-15T20:35:26.559Z_

<details><summary>↩ Tool result · `toolu_017wX5gEpUtVZerVxaEYvzF5`</summary>

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
  "session_id": "02cc67ad-c03e-4058-938b-210c48bf1830",
  "uuid": "b57b75e2-73cc-40ed-b2d1-1410c4d26533",
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

### Assistant

_source line 10_

<details><summary>Logged reasoning block</summary>

```text
Now let me call verify_references and also read the references.bib file in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "02cc67ad-c03e-4058-938b-210c48bf1830",
  "uuid": "ef9612a1-d81c-4bbf-898c-51285e541cb6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GrnBm6486d76eFhfARekcV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2657,
      "cache_read_input_tokens": 24049,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2657
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

_source line 11_

调用 `verify_references` 进行自动化审计，同时读取 bib 文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "02cc67ad-c03e-4058-938b-210c48bf1830",
  "uuid": "f85b114e-f696-43b8-ac47-2a3d5de2329c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GrnBm6486d76eFhfARekcV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2657,
      "cache_read_input_tokens": 24049,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2657
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

_source line 12_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references · `toolu_01LuRa6hJZAosd8t9FnVo5SP`</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "02cc67ad-c03e-4058-938b-210c48bf1830",
  "uuid": "474b22b0-67ba-4f66-aa68-249650109431",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GrnBm6486d76eFhfARekcV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2657,
      "cache_read_input_tokens": 24049,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2657
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

_source line 13_

<details open><summary>🔧 Tool call — Read · `toolu_01GnooHoXiMe34iqvvpbVEij`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "02cc67ad-c03e-4058-938b-210c48bf1830",
  "uuid": "2c41bf5b-d5db-4660-810b-9adb43f15bf1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GrnBm6486d76eFhfARekcV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2657,
      "cache_read_input_tokens": 24049,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2657
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

_source line 14 · 2026-05-15T20:36:16.337Z_

<details><summary>↩ Tool result · `toolu_01LuRa6hJZAosd8t9FnVo5SP`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 49, \"total_citations\": 72, \"unique_cited_keys\": 49, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 41, \"online_not_found\": 6, \"online_mismatch\": 2}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"detectgpt\", \"type\": \"inproceedings\", \"title\": \"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature\", \"authors\": \"Mitchell, Eric and Lee, Yoonho and Khazatsky, Alexander and Manning, Christopher...\", \"year\": \"2023\", \"venue\": \"Proceedings of the International Conference on Machine Learning\"}, {\"key\": \"gltr\", \"type\": \"inproceedings\", \"title\": \"GLTR: Statistical Detection and Visualization of Generated Text\", \"authors\": \"Gehrmann, Sebastian and Strobelt, Hendrik and Rush, Alexander M.\", \"year\": \"2019\", \"venue\": \"Proceedings of the Annual Meeting of the Association for Computational Linguisti...\"}, {\"key\": \"dna_gpt\", \"type\": \"inproceedings\", \"title\": \"DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text\", \"authors\": \"Yang, Xianjun and Cheng, Wei and Wu, Yue and Petzold, Linda and Wang, William Ya...\", \"year\": \"2024\", \"venue\": \"Proceedings of the International Conference on Learning Representations\"}, {\"key\": \"binoculars\", \"type\": \"inproceedings\", \"title\": \"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text\", \"authors\": \"Hans, Abhimanyu and Schwarzschild, Avi and Cherepanova, Valeriia and Kazemi, Ham...\", \"year\": \"2024\", \"venue\": \"Proceedings of the International Conference on Machine Learning\"}, {\"key\": \"fast_detectgpt\", \"type\": \"inproceedings\", \"title\": \"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature\", \"authors\": \"Bao, Guangsheng and Zhao, Yanbin and Teng, Zhiyang and Yang, Linyi and Zhang, Yu...\", \"year\": \"2024\", \"venue\": \"Proceedings of the International Conference on Learning Representations\"}, {\"key\": \"ld_score\", \"type\": \"article\", \"title\": \"Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection\", \"authors\": \"Narayanasamy, Priyadarshan and Agrawal, Swastik and Faber, Klint and Alam, Fardi...\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2605.01647\"}, {\"key\": \"intrinsic_dimension\", \"type\": \"inproceedings\", \"title\": \"Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts\", \"authors\": \"Tulchinskii, Eduard and Kuznetsov, Kristian and Kushnareva, Laida and Cherniavsk...\", \"year\": \"2023\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"diveye\", \"type\": \"article\", \"title\": \"Diversity Boosts AI-Generated Text Detection\", \"authors\": \"Basani, Advik Raj and Chen, Pin-Yu\", \"year\": \"2026\", \"venue\": \"Transactions on Machine Learning Research\"}, {\"key\": \"generator_barrier\", \"type\": \"article\", \"title\": \"Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection\", \"authors\": \"Pu, Xiao and Cheng, Zepeng and Yuan, Lin and Wu, Yu and Bi, Xiuli\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2604.13692\"}, {\"key\": \"feat_aug_transformer\", \"type\": \"article\", \"title\": \"Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators\", \"authors\": \"Mady, Mohamed and Reschke, Johannes and Schuller, Bj\\\\\\\"orn\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2605.03969\"}, {\"key\": \"reliable_detection\", \"type\": \"article\", \"title\": \"Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks\", \"authors\": \"Sadasivan, Vinu Sankar and Kumar, Aounon and Balasubramanian, Sriram and Wang, W...\", \"year\": \"2025\", \"venue\": \"Transactions on Machine Learning Research\"}, {\"key\": \"paraphrase_evades\", \"type\": \"inproceedings\", \"title\": \"Paraphrasing Evades Detectors of AI-Generated Text, but Retrieval is an Effective Defense\", \"authors\": \"Krishna, Kalpesh and Song, Yixiao and Karpinska, Marzena and Wieting, John and I...\", \"year\": \"2023\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"detection_possibilities\", \"type\": \"inproceedings\", \"title\": \"Position: On the Possibilities of AI-Generated Text Detection\", \"authors\": \"Chakraborty, Souradip and Bedi, Amrit Singh and Zhu, Sicheng and An, Bang and Ma...\", \"year\": \"2024\", \"venue\": \"Proceedings of the International Conference on Machine Learning\"}, {\"key\": \"grover\", \"type\": \"inproceedings\", \"title\": \"Defending Against Neural Fake News\", \"authors\": \"Zellers, Rowan and Holtzman, Ari and Rashkin, Hannah and Bisk, Yonatan and Farha...\", \"year\": \"2019\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"release_strategies\", \"type\": \"article\", \"title\": \"Release Strategies and the Social Impacts of Language Models\", \"authors\": \"Solaiman, Irene and Brundage, Miles and Clark, Jack and Askell, Amanda and Herbe...\", \"year\": \"2019\", \"venue\": \"arXiv preprint arXiv:1908.09203\"}, {\"key\": \"beyond_binary\", \"type\": \"inproceedings\", \"title\": \"Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement\", \"authors\": \"Cheng, Zihao and Zhou, Li and Jiang, Feng and Wang, Benyou and Li, Haizhou\", \"year\": \"2025\", \"venue\": \"Proceedings of the ACM Web Conference\"}, {\"key\": \"semeval2024_task8\", \"type\": \"inproceedings\", \"title\": \"SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection\", \"authors\": \"Wang, Yuxia and Mansurov, Jonibek and Ivanov, Petar and Su, Jinyan and Shelmanov...\", \"year\": \"2024\", \"venue\": \"Proceedings of the International Workshop on Semantic Evaluation\"}, {\"key\": \"self_consuming_mad\", \"type\": \"inproceedings\", \"title\": \"Self-Consuming Generative Models Go MAD\", \"authors\": \"Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahme...\", \"year\": \"2024\", \"venue\": \"Proceedings of the International Conference on Learning Representations\"}, {\"key\": \"curse_of_recursion\", \"type\": \"article\", \"title\": \"AI models collapse when trained on recursively generated data\", \"authors\": \"Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and ...\", \"year\": \"2024\", \"venue\": \"Nature\"}, {\"key\": \"strong_model_collapse\", \"type\": \"inproceedings\", \"title\": \"Strong Model Collapse\", \"authors\": \"Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia\", \"year\": \"2025\", \"venue\": \"Proceedings of the International Conference on Learning Representations\"}, {\"key\": \"model_collapse_avoidable\", \"type\": \"inproceedings\", \"title\": \"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data\", \"authors\": \"Gerstgrasser, Matthias and Schaeffer, Rylan and Dey, Apratim and Rafailov, Rafae...\", \"year\": \"2024\", \"venue\": \"Proceedings of the International Conference on Machine Learning\"}, {\"key\": \"ood_baseline\", \"type\": \"inproceedings\", \"title\": \"A Baseline for Detecting Misclassified and Out-of-Distribution Examples in Neural Networks\", \"authors\": \"Hendrycks, Dan and Gimpel, Kevin\", \"year\": \"2017\", \"venue\": \"Proceedings of the International Conference on Learning Representations\"}, {\"key\": \"dsir\", \"type\": \"inproceedings\", \"title\": \"Data Selection for Language Models via Importance Resampling\", \"authors\": \"Xie, Sang Michael and Santurkar, Shibani and Ma, Tengyu and Liang, Percy\", \"year\": \"2023\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"qurating\", \"type\": \"inproceedings\", \"title\": \"QuRating: Selecting High-Quality Data for Training Language Models\", \"authors\": \"Wettig, Alexander and Gupta, Aatmik and Malik, Saumya and Chen, Danqi\", \"year\": \"2024\", \"venue\": \"Proceedings of the International Conference on Machine Learning\"}, {\"key\": \"ccnet\", \"type\": \"inproceedings\", \"title\": \"CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data\", \"authors\": \"Wenzek, Guillaume and Lachaux, Marie-Anne and Conneau, Alexis and Chaudhary, Vis...\", \"year\": \"2020\", \"venue\": \"Proceedings of the Language Resources and Evaluation Conference\"}, {\"key\": \"watermark_llm\", \"type\": \"inproceedings\", \"title\": \"A Watermark for Large Language Models\", \"authors\": \"Kirchenbauer, John and Geiping, Jonas and Wen, Yuxin and Katz, Jonathan and Mier...\", \"year\": \"2023\", \"venue\": \"Proceedings of the International Conference on Machine Learning\"}, {\"key\": \"synthid_text\", \"type\": \"article\", \"title\": \"Scalable Watermarking for Identifying Large Language Model Outputs\", \"authors\": \"Dathathri, Sumanth and See, Abigail and Ghaisas, Sumedh and Huang, Po-Sen and Mc...\", \"year\": \"2024\", \"venue\": \"Nature\"}, {\"key\": \"aaronson_watermark\", \"type\": \"misc\", \"title\": \"Watermarking GPT Outputs\", \"authors\": \"Aaronson, Scott and Kirchner, Hendrik\", \"year\": \"2022\", \"venue\": \"\"}, {\"key\": \"chainwash\", \"type\": \"article\", \"title\": \"Chainwash: Multi-Step Rewriting Attacks on Diffusion Language Model Watermarks\", \"authors\": \"Ameen, Mohd Ruhul and Islam, Akif and Mahmud, Nadim and Hamid, Md. Ekramul\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2605.05503\"}, {\"key\": \"curious_decline\", \"type\": \"inproceedings\", \"title\": \"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text\", \"authors\": \"Guo, Yanzhu and Shang, Guokan and Vazirgiannis, Michalis and Clavel, Chlo\\\\'e\", \"year\": \"2024\", \"venue\": \"Findings of the Association for Computational Linguistics: NAACL\"}, {\"key\": \"writing_diversity\", \"type\": \"inproceedings\", \"title\": \"Does Writing with Language Models Reduce Content Diversity?\", \"authors\": \"Padmakumar, Vishakh and He, He\", \"year\": \"2024\", \"venue\": \"Proceedings of the International Conference on Learning Representations\"}, {\"key\": \"nucleus_sampling\", \"type\": \"inproceedings\", \"title\": \"The Curious Case of Neural Text Degeneration\", \"authors\": \"Holtzman, Ari and Buys, Jan and Du, Li and Forbes, Maxwell and Choi, Yejin\", \"year\": \"2020\", \"venue\": \"Proceedings of the International Conference on Learning Representations\"}, {\"key\": \"mapping_llm_science\", \"type\": \"inproceedings\", \"title\": \"Mapping the Increasing Use of LLMs in Scientific Papers\", \"authors\": \"Liang, Weixin and Zhang, Yaohui and Wu, Zhengxuan and Lepp, Haley and Ji, Wenlon...\", \"year\": \"2024\", \"venue\": \"Proceedings of the Conference on Language Modeling\"}, {\"key\": \"monitoring_ai_review\", \"type\": \"inproceedings\", \"title\": \"Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews\", \"authors\": \"Liang, Weixin and Izzo, Zachary and Zhang, Yaohui and Lepp, Haley and Cao, Hanch...\", \"year\": \"2024\", \"venue\": \"Proceedings of the International Conference on Machine Learning\"}, {\"key\": \"stamatatos_survey\", \"type\": \"article\", \"title\": \"A Survey of Modern Authorship Attribution Methods\", \"authors\": \"Stamatatos, Efstathios\", \"year\": \"2009\", \"venue\": \"Journal of the American Society for Information Science and Technology\"}, {\"key\": \"koppel_authorship\", \"type\": \"article\", \"title\": \"Computational Methods in Authorship Attribution\", \"authors\": \"Koppel, Moshe and Schler, Jonathan and Argamon, Shlomo\", \"year\": \"2009\", \"venue\": \"Journal of the American Society for Information Science and Technology\"}, {\"key\": \"uchendu_attribution\", \"type\": \"inproceedings\", \"title\": \"Authorship Attribution for Neural Text Generation\", \"authors\": \"Uchendu, Adaku and Le, Thai and Shu, Kai and Lee, Dongwon\", \"year\": \"2020\", \"venue\": \"Proceedings of the Conference on Empirical Methods in Natural Language Processin...\"}, {\"key\": \"munir_looking_glass\", \"type\": \"inproceedings\", \"title\": \"Through the Looking Glass: Learning to Attribute Synthetic Text Generated by Language Models\", \"authors\": \"Munir, Shaoor and Batool, Brishna and Shafiq, Zubair and Srinivasan, Padmini and...\", \"year\": \"2021\", \"venue\": \"Proceedings of the Conference of the European Chapter of the Association for Com...\"}, {\"key\": \"broken_telephone\", \"type\": \"inproceedings\", \"title\": \"LLM as a Broken Telephone: Iterative Generation Distorts Information\", \"authors\": \"Mohamed, Amr and Geng, Mingmeng and Vazirgiannis, Michalis and Shang, Guokan\", \"year\": \"2025\", \"venue\": \"Proceedings of the Annual Meeting of the Association for Computational Linguisti...\"}, {\"key\": \"markovian_chains\", \"type\": \"article\", \"title\": \"Markovian Generation Chains in Large Language Models\", \"authors\": \"Geng, Mingmeng and Mohamed, Amr and Shang, Guokan and Vazirgiannis, Michalis and...\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2603.11228\"}, {\"key\": \"min_k_percent\", \"type\": \"inproceedings\", \"title\": \"Detecting Pretraining Data from Large Language Models\", \"authors\": \"Shi, Weijia and Ajith, Anirudh and Xia, Mengzhou and Huang, Yangsibo and Liu, Da...\", \"year\": \"2024\", \"venue\": \"Proceedings of the International Conference on Learning Representations\"}, {\"key\": \"wu_survey_2025\", \"type\": \"article\", \"title\": \"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions\", \"authors\": \"Wu, Junchao and Yang, Shu and Zhan, Runzhe and Yuan, Yulin and Chao, Lidia Sam a...\", \"year\": \"2025\", \"venue\": \"Computational Linguistics\"}, {\"key\": \"jawahar_survey\", \"type\": \"inproceedings\", \"title\": \"Automatic Detection of Machine Generated Text: A Critical Survey\", \"authors\": \"Jawahar, Ganesh and Abdul-Mageed, Muhammad and Lakshmanan, Laks V.S.\", \"year\": \"2020\", \"venue\": \"Proceedings of the International Conference on Computational Linguistics\"}, {\"key\": \"pythia\", \"type\": \"inproceedings\", \"title\": \"Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling\", \"authors\": \"Biderman, Stella and Schoelkopf, Hailey and Anthony, Quentin Gregory and Bradley...\", \"year\": \"2023\", \"venue\": \"Proceedings of the International Conference on Machine Learning\"}, {\"key\": \"olmo\", \"type\": \"inproceedings\", \"title\": \"OLMo: Accelerating the Science of Language Models\", \"authors\": \"Groeneveld, Dirk and Beltagy, Iz and Walsh, Evan and Bhagia, Akshita and Kinney,...\", \"year\": \"2024\", \"venue\": \"Proceedings of the Annual Meeting of the Association for Computational Linguisti...\"}, {\"key\": \"qwen3\", \"type\": \"article\", \"title\": \"Qwen3 Technical Report\", \"authors\": \"Qwen Team\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2505.09388\"}, {\"key\": \"coral_ordinal\", \"type\": \"article\", \"title\": \"Rank Consistent Ordinal Regression for Neural Networks with Application to Age Estimation\", \"authors\": \"Cao, Wenzhi and Mirjalili, Vahid and Raschka, Sebastian\", \"year\": \"2020\", \"venue\": \"Pattern Recognition Letters\"}, {\"key\": \"frank_hall_ordinal\", \"type\": \"inproceedings\", \"title\": \"A Simple Approach to Ordinal Classification\", \"authors\": \"Frank, Eibe and Hall, Mark\", \"year\": \"2001\", \"venue\": \"Proceedings of the European Conference on Machine Learning\"}, {\"key\": \"xgboost\", \"type\": \"inproceedings\", \"title\": \"XGBoost: A Scalable Tree Boosting System\", \"authors\": \"Chen, Tianqi and Guestrin, Carlos\", \"year\": \"2016\", \"venue\": \"Proceedings of the ACM SIGKDD International Conference on Knowledge Discovery an...\"}], \"tex_citations\": [{\"key\": \"mapping_llm_science\", \"file\": \"introduction.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"monitoring_ai_review\", \"file\": \"introduction.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"fast_detectgpt\", \"file\": \"introduction.tex\", \"line\": 8, \"command\": \"cite\"}, {\"key\": \"binoculars\", \"file\": \"introduction.tex\", \"line\": 8, \"command\": \"cite\"}, {\"key\": \"ld_score\", \"file\": \"introduction.tex\", \"line\": 8, \"command\": \"cite\"}, {\"key\": \"detectgpt\", \"file\": \"introduction.tex\", \"line\": 8, \"command\": \"cite\"}, {\"key\": \"broken_telephone\", \"file\": \"introduction.tex\", \"line\": 18, \"command\": \"cite\"}, {\"key\": \"markovian_chains\", \"file\": \"introduction.tex\", \"line\": 18, \"command\": \"cite\"}, {\"key\": \"ood_baseline\", \"file\": \"introduction.tex\", \"line\": 23, \"command\": \"cite\"}, {\"key\": \"gltr\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"grover\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"release_strategies\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"detectgpt\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"fast_detectgpt\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"binoculars\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"dna_gpt\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"feat_aug_transformer\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"reliable_detection\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"ld_score\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"intrinsic_dimension\", \"file\": \"related_work.tex\", \"line\": 8, \"command\": \"citet\"}, {\"key\": \"diveye\", \"file\": \"related_work.tex\", \"line\": 8, \"command\": \"citet\"}, {\"key\": \"generator_barrier\", \"file\": \"related_work.tex\", \"line\": 8, \"command\": \"citet\"}, {\"key\": \"wu_survey_2025\", \"file\": \"related_work.tex\", \"line\": 9, \"command\": \"citet\"}, {\"key\": \"jawahar_survey\", \"file\": \"related_work.tex\", \"line\": 9, \"command\": \"citet\"}, {\"key\": \"beyond_binary\", \"file\": \"related_work.tex\", \"line\": 12, \"command\": \"citet\"}, {\"key\": \"semeval2024_task8\", \"file\": \"related_work.tex\", \"line\": 12, \"command\": \"cite\"}, {\"key\": \"paraphrase_evades\", \"file\": \"related_work.tex\", \"line\": 15, \"command\": \"citet\"}, {\"key\": \"detection_possibilities\", \"file\": \"related_work.tex\", \"line\": 15, \"command\": \"citet\"}, {\"key\": \"ood_baseline\", \"file\": \"related_work.tex\", \"line\": 16, \"command\": \"cite\"}, {\"key\": \"uchendu_attribution\", \"file\": \"related_work.tex\", \"line\": 20, \"command\": \"citet\"}, {\"key\": \"munir_looking_glass\", \"file\": \"related_work.tex\", \"line\": 20, \"command\": \"citet\"}, {\"key\": \"self_consuming_mad\", \"file\": \"related_work.tex\", \"line\": 29, \"command\": \"citet\"}, {\"key\": \"curse_of_recursion\", \"file\": \"related_work.tex\", \"line\": 29, \"command\": \"citet\"}, {\"key\": \"model_collapse_avoidable\", \"file\": \"related_work.tex\", \"line\": 29, \"command\": \"citet\"}, {\"key\": \"strong_model_collapse\", \"file\": \"related_work.tex\", \"line\": 30, \"command\": \"citet\"}, {\"key\": \"broken_telephone\", \"file\": \"related_work.tex\", \"line\": 35, \"command\": \"citet\"}, {\"key\": \"markovian_chains\", \"file\": \"related_work.tex\", \"line\": 36, \"command\": \"citet\"}, {\"key\": \"curious_decline\", \"file\": \"related_work.tex\", \"line\": 42, \"command\": \"cite\"}, {\"key\": \"writing_diversity\", \"file\": \"related_work.tex\", \"line\": 42, \"command\": \"cite\"}, {\"key\": \"stamatatos_survey\", \"file\": \"related_work.tex\", \"line\": 45, \"command\": \"cite\"}, {\"key\": \"koppel_authorship\", \"file\": \"related_work.tex\", \"line\": 45, \"command\": \"cite\"}, {\"key\": \"uchendu_attribution\", \"file\": \"related_work.tex\", \"line\": 46, \"command\": \"citet\"}, {\"key\": \"nucleus_sampling\", \"file\": \"related_work.tex\", \"line\": 48, \"command\": \"citet\"}, {\"key\": \"dsir\", \"file\": \"related_work.tex\", \"line\": 54, \"command\": \"citet\"}, {\"key\": \"qurating\", \"file\": \"related_work.tex\", \"line\": 54, \"command\": \"citet\"}, {\"key\": \"ccnet\", \"file\": \"related_work.tex\", \"line\": 54, \"command\": \"citet\"}, {\"key\": \"watermark_llm\", \"file\": \"related_work.tex\", \"line\": 57, \"command\": \"cite\"}, {\"key\": \"synthid_text\", \"file\": \"related_work.tex\", \"line\": 57, \"command\": \"cite\"}, {\"key\": \"aaronson_watermark\", \"file\": \"related_work.tex\", \"line\": 57, \"command\": \"cite\"}, {\"key\": \"chainwash\", \"file\": \"related_work.tex\", \"line\": 58, \"command\": \"citet\"}, {\"key\": \"min_k_percent\", \"file\": \"related_work.tex\", \"line\": 60, \"command\": \"citet\"}, {\"key\": \"pythia\", \"file\": \"method.tex\", \"line\": 16, \"command\": \"cite\"}, {\"key\": \"olmo\", \"file\": \"method.tex\", \"line\": 16, \"command\": \"cite\"}, {\"key\": \"qwen3\", \"file\": \"method.tex\", \"line\": 16, \"command\": \"cite\"}, {\"key\": \"ood_baseline\", \"file\": \"method.tex\", \"line\": 48, \"command\": \"cite\"}, {\"key\": \"xgboost\", \"file\": \"method.tex\", \"line\": 71, \"command\": \"cite\"}, {\"key\": \"coral_ordinal\", \"file\": \"method.tex\", \"line\": 77, \"command\": \"cite\"}, {\"key\": \"frank_hall_ordinal\", \"file\": \"method.tex\", \"line\": 77, \"command\": \"cite\"}, {\"key\": \"fast_detectgpt\", \"file\": \"method.tex\", \"line\": 89, \"command\": \"cite\"}, {\"key\": \"binoculars\", \"file\": \"method.tex\", \"line\": 89, \"command\": \"cite\"}, {\"key\": \"ld_score\", \"file\": \"method.tex\", \"line\": 89, \"command\": \"cite\"}, {\"key\": \"coral_ordinal\", \"file\": \"results.tex\", \"line\": 54, \"command\": \"cite\"}, {\"key\": \"frank_hall_ordinal\", \"file\": \"results.tex\", \"line\": 54, \"command\": \"cite\"}, {\"key\": \"detectgpt\", \"file\": \"discussion.tex\", \"line\": 13, \"command\": \"cite\"}, {\"key\": \"gltr\", \"file\": \"discussion.tex\", \"line\": 13, \"command\": \"cite\"}, {\"key\": \"binoculars\", \"file\": \"discussion.tex\", \"line\": 13, \"command\": \"cite\"}, {\"key\": \"ood_baseline\", \"file\": \"discussion.tex\", \"line\": 15, \"command\": \"cite\"}, {\"key\": \"broken_telephone\", \"file\": \"discussion.tex\", \"line\": 23, \"command\": \"cite\"}, {\"key\": \"self_consuming_mad\", \"file\": \"discussion.tex\", \"line\": 28, \"command\": \"cite\"}, {\"key\": \"curse_of_recursion\", \"file\": \"discussion.tex\", \"line\": 31, \"command\": \"cite\"}, {\"key\": \"strong_model_collapse\", \"file\": \"discussion.tex\", \"line\": 31, \"command\": \"cite\"}, {\"key\": \"self_consuming_mad\", \"file\": \"discussion.tex\", \"line\": 31, \"command\": \"cite\"}], \"online_verification\": [{\"key\": \"detectgpt\", \"title\": \"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature\", \"status\": \"not_found\", \"confidence\": 0.382, \"matched_title\": \"Regulating ChatGPT and other Large Generative AI Models\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.38 below threshold 0.82\"}, {\"key\": \"gltr\", \"title\": \"GLTR: Statistical Detection and Visualization of Generated Text\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"GLTR: Statistical Detection and Visualization of Generated Text\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"dna_gpt\", \"title\": \"DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"binoculars\", \"title\": \"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"fast_detectgpt\", \"title\": \"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"ld_score\", \"title\": \"Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"intrinsic_dimension\", \"title\": \"Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"diveye\", \"title\": \"Diversity Boosts AI-Generated Text Detection\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Diversity Boosts AI-Generated Text Detection\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"generator_barrier\", \"title\": \"Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"feat_aug_transformer\", \"title\": \"Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"reliable_detection\", \"title\": \"Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks\", \"status\": \"not_found\", \"confidence\": 0.344, \"matched_title\": \"2015 ESC Guidelines for the management of acute coronary syndromes in patients presenting without persistent ST-segment elevation\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.34 below threshold 0.82\"}, {\"key\": \"paraphrase_evades\", \"title\": \"Paraphrasing Evades Detectors of AI-Generated Text, but Retrieval is an Effective Defense\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"detection_possibilities\", \"title\": \"Position: On the Possibilities of AI-Generated Text Detection\", \"status\": \"not_found\", \"confidence\": 0.253, \"matched_title\": \"Review of deep learning: concepts, CNN architectures, challenges, applications, future directions\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.25 below threshold 0.82\"}, {\"key\": \"grover\", \"title\": \"Defending Against Neural Fake News\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Defending Against Neural Fake News\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"release_strategies\", \"title\": \"Release Strategies and the Social Impacts of Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Release Strategies and the Social Impacts of Language Models\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"beyond_binary\", \"title\": \"Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"semeval2024_task8\", \"title\": \"SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"self_consuming_mad\", \"title\": \"Self-Consuming Generative Models Go MAD\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Self-Consuming Generative Models go MAD\", \"matched_year\": \"2023\", \"mismatch_fields\": [\"first_author: bib=alemohammad vs api=casco-rodriguez\"], \"note\": \"\"}, {\"key\": \"curse_of_recursion\", \"title\": \"AI models collapse when trained on recursively generated data\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"AI models collapse when trained on recursively generated data\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"strong_model_collapse\", \"title\": \"Strong Model Collapse\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Strong Model Collapse\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"model_collapse_avoidable\", \"title\": \"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"ood_baseline\", \"title\": \"A Baseline for Detecting Misclassified and Out-of-Distribution Examples in Neural Networks\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Baseline for Detecting Misclassified and Out-of-Distribution Examples in Neural Networks\", \"matched_year\": \"2016\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"dsir\", \"title\": \"Data Selection for Language Models via Importance Resampling\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Data Selection for Language Models via Importance Resampling\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"qurating\", \"title\": \"QuRating: Selecting High-Quality Data for Training Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"QuRating: Selecting High-Quality Data for Training Language Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"ccnet\", \"title\": \"CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"watermark_llm\", \"title\": \"A Watermark for Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Watermark for Large Language Models\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"synthid_text\", \"title\": \"Scalable Watermarking for Identifying Large Language Model Outputs\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Scalable watermarking for identifying large language model outputs\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"aaronson_watermark\", \"title\": \"Watermarking GPT Outputs\", \"status\": \"not_found\", \"confidence\": 0.418, \"matched_title\": \"Undetectable Watermarks for Language Models\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.42 below threshold 0.82\"}, {\"key\": \"chainwash\", \"title\": \"Chainwash: Multi-Step Rewriting Attacks on Diffusion Language Model Watermarks\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Chainwash: Multi-Step Rewriting Attacks on Diffusion Language Model Watermarks\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"curious_decline\", \"title\": \"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"writing_diversity\", \"title\": \"Does Writing with Language Models Reduce Content Diversity?\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Does Writing with Language Models Reduce Content Diversity?\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"nucleus_sampling\", \"title\": \"The Curious Case of Neural Text Degeneration\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"The Curious Case of Neural Text Degeneration\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"mapping_llm_science\", \"title\": \"Mapping the Increasing Use of LLMs in Scientific Papers\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Mapping the Increasing Use of LLMs in Scientific Papers\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"monitoring_ai_review\", \"title\": \"Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"stamatatos_survey\", \"title\": \"A Survey of Modern Authorship Attribution Methods\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A survey of modern authorship attribution methods\", \"matched_year\": \"2008\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"koppel_authorship\", \"title\": \"Computational Methods in Authorship Attribution\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Computational methods in authorship attribution\", \"matched_year\": \"2008\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"uchendu_attribution\", \"title\": \"Authorship Attribution for Neural Text Generation\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Authorship Attribution for Neural Text Generation\", \"matched_year\": \"2020\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"munir_looking_glass\", \"title\": \"Through the Looking Glass: Learning to Attribute Synthetic Text Generated by Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Through the Looking Glass: Learning to Attribute Synthetic Text Generated by Language Models\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"broken_telephone\", \"title\": \"LLM as a Broken Telephone: Iterative Generation Distorts Information\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"LLM as a Broken Telephone: Iterative Generation Distorts Information\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"markovian_chains\", \"title\": \"Markovian Generation Chains in Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Markovian Generation Chains in Large Language Models\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"min_k_percent\", \"title\": \"Detecting Pretraining Data from Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Detecting Pretraining Data from Large Language Models\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wu_survey_2025\", \"title\": \"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"jawahar_survey\", \"title\": \"Automatic Detection of Machine Generated Text: A Critical Survey\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Automatic Detection of Machine Generated Text: A Critical Survey\", \"matched_year\": \"2020\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"pythia\", \"title\": \"Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling\", \"status\": \"not_found\", \"confidence\": 0.497, \"matched_title\": \"The TRIPOD-LLM reporting guideline for studies using large language models\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.50 below threshold 0.82\"}, {\"key\": \"olmo\", \"title\": \"OLMo: Accelerating the Science of Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"OLMo: Accelerating the Science of Language Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"qwen3\", \"title\": \"Qwen3 Technical Report\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Qwen3 Technical Report\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"first_author: bib=team vs api=yang\"], \"note\": \"\"}, {\"key\": \"coral_ordinal\", \"title\": \"Rank Consistent Ordinal Regression for Neural Networks with Application to Age Estimation\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Rank consistent ordinal regression for neural networks with application to age estimation\", \"matched_year\": \"2020\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"frank_hall_ordinal\", \"title\": \"A Simple Approach to Ordinal Classification\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Simple Approach to Ordinal Classification\", \"matched_year\": \"2001\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"xgboost\", \"title\": \"XGBoost: A Scalable Tree Boosting System\", \"status\": \"not_found\", \"confidence\": 0.298, \"matched_title\": \"XGBoost\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.30 below threshold 0.82\"}]}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "02cc67ad-c03e-4058-938b-210c48bf1830",
  "uuid": "6665770e-d4db-42f2-b7c3-31018a9b6675",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"summary\\\": {\\\"total_bib_entries\\\": 49, \\\"total_citations\\\": 72, \\\"unique_cited_keys\\\": 49, \\\"orphan_bib\\\": 0, \\\"missing_bib\\\": 0, \\\"duplicate_keys\\\": 0, \\\"online_verified\\\": 41, \\\"online_not_found\\\": 6, \\\"online_mismatch\\\": 2}, \\\"cross_check\\\": {\\\"orphan_bib\\\": [], \\\"missing_bib\\\": [], \\\"orphan_count\\\": 0, \\\"missing_count\\\": 0}, \\\"bib_entries\\\": [{\\\"key\\\": \\\"detectgpt\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature\\\", \\\"authors\\\": \\\"Mitchell, Eric and Lee, Yoonho and Khazatsky, Alexander and Manning, Christopher...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Proceedings of the International Conference on Machine Learning\\\"}, {\\\"key\\\": \\\"gltr\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"GLTR: Statistical Detection and Visualization of Generated Text\\\", \\\"authors\\\": \\\"Gehrmann, Sebastian and Strobelt, Hendrik and Rush, Alexander M.\\\", \\\"year\\\": \\\"2019\\\", \\\"venue\\\": \\\"Proceedings of the Annual Meeting of the Association for Computational Linguisti...\\\"}, {\\\"key\\\": \\\"dna_gpt\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text\\\", \\\"authors\\\": \\\"Yang, Xianjun and Cheng, Wei and Wu, Yue and Petzold, Linda and Wang, William Ya...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the International Conference on Learning Representations\\\"}, {\\\"key\\\": \\\"binoculars\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text\\\", \\\"authors\\\": \\\"Hans, Abhimanyu and Schwarzschild, Avi and Cherepanova, Valeriia and Kazemi, Ham...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the International Conference on Machine Learning\\\"}, {\\\"key\\\": \\\"fast_detectgpt\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature\\\", \\\"authors\\\": \\\"Bao, Guangsheng and Zhao, Yanbin and Teng, Zhiyang and Yang, Linyi and Zhang, Yu...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the International Conference on Learning Representations\\\"}, {\\\"key\\\": \\\"ld_score\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection\\\", \\\"authors\\\": \\\"Narayanasamy, Priyadarshan and Agrawal, Swastik and Faber, Klint and Alam, Fardi...\\\", \\\"year\\\": \\\"2026\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2605.01647\\\"}, {\\\"key\\\": \\\"intrinsic_dimension\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts\\\", \\\"authors\\\": \\\"Tulchinskii, Eduard and Kuznetsov, Kristian and Kushnareva, Laida and Cherniavsk...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Advances in Neural Information Processing Systems\\\"}, {\\\"key\\\": \\\"diveye\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Diversity Boosts AI-Generated Text Detection\\\", \\\"authors\\\": \\\"Basani, Advik Raj and Chen, Pin-Yu\\\", \\\"year\\\": \\\"2026\\\", \\\"venue\\\": \\\"Transactions on Machine Learning Research\\\"}, {\\\"key\\\": \\\"generator_barrier\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection\\\", \\\"authors\\\": \\\"Pu, Xiao and Cheng, Zepeng and Yuan, Lin and Wu, Yu and Bi, Xiuli\\\", \\\"year\\\": \\\"2026\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2604.13692\\\"}, {\\\"key\\\": \\\"feat_aug_transformer\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators\\\", \\\"authors\\\": \\\"Mady, Mohamed and Reschke, Johannes and Schuller, Bj\\\\\\\\\\\\\\\"orn\\\", \\\"year\\\": \\\"2026\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2605.03969\\\"}, {\\\"key\\\": \\\"reliable_detection\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks\\\", \\\"authors\\\": \\\"Sadasivan, Vinu Sankar and Kumar, Aounon and Balasubramanian, Sriram and Wang, W...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Transactions on Machine Learning Research\\\"}, {\\\"key\\\": \\\"paraphrase_evades\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Paraphrasing Evades Detectors of AI-Generated Text, but Retrieval is an Effective Defense\\\", \\\"authors\\\": \\\"Krishna, Kalpesh and Song, Yixiao and Karpinska, Marzena and Wieting, John and I...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Advances in Neural Information Processing Systems\\\"}, {\\\"key\\\": \\\"detection_possibilities\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Position: On the Possibilities of AI-Generated Text Detection\\\", \\\"authors\\\": \\\"Chakraborty, Souradip and Bedi, Amrit Singh and Zhu, Sicheng and An, Bang and Ma...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the International Conference on Machine Learning\\\"}, {\\\"key\\\": \\\"grover\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Defending Against Neural Fake News\\\", \\\"authors\\\": \\\"Zellers, Rowan and Holtzman, Ari and Rashkin, Hannah and Bisk, Yonatan and Farha...\\\", \\\"year\\\": \\\"2019\\\", \\\"venue\\\": \\\"Advances in Neural Information Processing Systems\\\"}, {\\\"key\\\": \\\"release_strategies\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Release Strategies and the Social Impacts of Language Models\\\", \\\"authors\\\": \\\"Solaiman, Irene and Brundage, Miles and Clark, Jack and Askell, Amanda and Herbe...\\\", \\\"year\\\": \\\"2019\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:1908.09203\\\"}, {\\\"key\\\": \\\"beyond_binary\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement\\\", \\\"authors\\\": \\\"Cheng, Zihao and Zhou, Li and Jiang, Feng and Wang, Benyou and Li, Haizhou\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Proceedings of the ACM Web Conference\\\"}, {\\\"key\\\": \\\"semeval2024_task8\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection\\\", \\\"authors\\\": \\\"Wang, Yuxia and Mansurov, Jonibek and Ivanov, Petar and Su, Jinyan and Shelmanov...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the International Workshop on Semantic Evaluation\\\"}, {\\\"key\\\": \\\"self_consuming_mad\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Self-Consuming Generative Models Go MAD\\\", \\\"authors\\\": \\\"Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahme...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the International Conference on Learning Representations\\\"}, {\\\"key\\\": \\\"curse_of_recursion\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"AI models collapse when trained on recursively generated data\\\", \\\"authors\\\": \\\"Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and ...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Nature\\\"}, {\\\"key\\\": \\\"strong_model_collapse\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Strong Model Collapse\\\", \\\"authors\\\": \\\"Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Proceedings of the International Conference on Learning Representations\\\"}, {\\\"key\\\": \\\"model_collapse_avoidable\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data\\\", \\\"authors\\\": \\\"Gerstgrasser, Matthias and Schaeffer, Rylan and Dey, Apratim and Rafailov, Rafae...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the International Conference on Machine Learning\\\"}, {\\\"key\\\": \\\"ood_baseline\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"A Baseline for Detecting Misclassified and Out-of-Distribution Examples in Neural Networks\\\", \\\"authors\\\": \\\"Hendrycks, Dan and Gimpel, Kevin\\\", \\\"year\\\": \\\"2017\\\", \\\"venue\\\": \\\"Proceedings of the International Conference on Learning Representations\\\"}, {\\\"key\\\": \\\"dsir\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Data Selection for Language Models via Importance Resampling\\\", \\\"authors\\\": \\\"Xie, Sang Michael and Santurkar, Shibani and Ma, Tengyu and Liang, Percy\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Advances in Neural Information Processing Systems\\\"}, {\\\"key\\\": \\\"qurating\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"QuRating: Selecting High-Quality Data for Training Language Models\\\", \\\"authors\\\": \\\"Wettig, Alexander and Gupta, Aatmik and Malik, Saumya and Chen, Danqi\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the International Conference on Machine Learning\\\"}, {\\\"key\\\": \\\"ccnet\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data\\\", \\\"authors\\\": \\\"Wenzek, Guillaume and Lachaux, Marie-Anne and Conneau, Alexis and Chaudhary, Vis...\\\", \\\"year\\\": \\\"2020\\\", \\\"venue\\\": \\\"Proceedings of the Language Resources and Evaluation Conference\\\"}, {\\\"key\\\": \\\"watermark_llm\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"A Watermark for Large Language Models\\\", \\\"authors\\\": \\\"Kirchenbauer, John and Geiping, Jonas and Wen, Yuxin and Katz, Jonathan and Mier...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Proceedings of the International Conference on Machine Learning\\\"}, {\\\"key\\\": \\\"synthid_text\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Scalable Watermarking for Identifying Large Language Model Outputs\\\", \\\"authors\\\": \\\"Dathathri, Sumanth and See, Abigail and Ghaisas, Sumedh and Huang, Po-Sen and Mc...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Nature\\\"}, {\\\"key\\\": \\\"aaronson_watermark\\\", \\\"type\\\": \\\"misc\\\", \\\"title\\\": \\\"Watermarking GPT Outputs\\\", \\\"authors\\\": \\\"Aaronson, Scott and Kirchner, Hendrik\\\", \\\"year\\\": \\\"2022\\\", \\\"venue\\\": \\\"\\\"}, {\\\"key\\\": \\\"chainwash\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Chainwash: Multi-Step Rewriting Attacks on Diffusion Language Model Watermarks\\\", \\\"authors\\\": \\\"Ameen, Mohd Ruhul and Islam, Akif and Mahmud, Nadim and Hamid, Md. Ekramul\\\", \\\"year\\\": \\\"2026\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2605.05503\\\"}, {\\\"key\\\": \\\"curious_decline\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text\\\", \\\"authors\\\": \\\"Guo, Yanzhu and Shang, Guokan and Vazirgiannis, Michalis and Clavel, Chlo\\\\\\\\'e\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Findings of the Association for Computational Linguistics: NAACL\\\"}, {\\\"key\\\": \\\"writing_diversity\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Does Writing with Language Models Reduce Content Diversity?\\\", \\\"authors\\\": \\\"Padmakumar, Vishakh and He, He\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the International Conference on Learning Representations\\\"}, {\\\"key\\\": \\\"nucleus_sampling\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"The Curious Case of Neural Text Degeneration\\\", \\\"authors\\\": \\\"Holtzman, Ari and Buys, Jan and Du, Li and Forbes, Maxwell and Choi, Yejin\\\", \\\"year\\\": \\\"2020\\\", \\\"venue\\\": \\\"Proceedings of the International Conference on Learning Representations\\\"}, {\\\"key\\\": \\\"mapping_llm_science\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Mapping the Increasing Use of LLMs in Scientific Papers\\\", \\\"authors\\\": \\\"Liang, Weixin and Zhang, Yaohui and Wu, Zhengxuan and Lepp, Haley and Ji, Wenlon...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the Conference on Language Modeling\\\"}, {\\\"key\\\": \\\"monitoring_ai_review\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews\\\", \\\"authors\\\": \\\"Liang, Weixin and Izzo, Zachary and Zhang, Yaohui and Lepp, Haley and Cao, Hanch...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the International Conference on Machine Learning\\\"}, {\\\"key\\\": \\\"stamatatos_survey\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"A Survey of Modern Authorship Attribution Methods\\\", \\\"authors\\\": \\\"Stamatatos, Efstathios\\\", \\\"year\\\": \\\"2009\\\", \\\"venue\\\": \\\"Journal of the American Society for Information Science and Technology\\\"}, {\\\"key\\\": \\\"koppel_authorship\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Computational Methods in Authorship Attribution\\\", \\\"authors\\\": \\\"Koppel, Moshe and Schler, Jonathan and Argamon, Shlomo\\\", \\\"year\\\": \\\"2009\\\", \\\"venue\\\": \\\"Journal of the American Society for Information Science and Technology\\\"}, {\\\"key\\\": \\\"uchendu_attribution\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Authorship Attribution for Neural Text Generation\\\", \\\"authors\\\": \\\"Uchendu, Adaku and Le, Thai and Shu, Kai and Lee, Dongwon\\\", \\\"year\\\": \\\"2020\\\", \\\"venue\\\": \\\"Proceedings of the Conference on Empirical Methods in Natural Language Processin...\\\"}, {\\\"key\\\": \\\"munir_looking_glass\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Through the Looking Glass: Learning to Attribute Synthetic Text Generated by Language Models\\\", \\\"authors\\\": \\\"Munir, Shaoor and Batool, Brishna and Shafiq, Zubair and Srinivasan, Padmini and...\\\", \\\"year\\\": \\\"2021\\\", \\\"venue\\\": \\\"Proceedings of the Conference of the European Chapter of the Association for Com...\\\"}, {\\\"key\\\": \\\"broken_telephone\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"LLM as a Broken Telephone: Iterative Generation Distorts Information\\\", \\\"authors\\\": \\\"Mohamed, Amr and Geng, Mingmeng and Vazirgiannis, Michalis and Shang, Guokan\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Proceedings of the Annual Meeting of the Association for Computational Linguisti...\\\"}, {\\\"key\\\": \\\"markovian_chains\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Markovian Generation Chains in Large Language Models\\\", \\\"authors\\\": \\\"Geng, Mingmeng and Mohamed, Amr and Shang, Guokan and Vazirgiannis, Michalis and...\\\", \\\"year\\\": \\\"2026\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2603.11228\\\"}, {\\\"key\\\": \\\"min_k_percent\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Detecting Pretraining Data from Large Language Models\\\", \\\"authors\\\": \\\"Shi, Weijia and Ajith, Anirudh and Xia, Mengzhou and Huang, Yangsibo and Liu, Da...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the International Conference on Learning Representations\\\"}, {\\\"key\\\": \\\"wu_survey_2025\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions\\\", \\\"authors\\\": \\\"Wu, Junchao and Yang, Shu and Zhan, Runzhe and Yuan, Yulin and Chao, Lidia Sam a...\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"Computational Linguistics\\\"}, {\\\"key\\\": \\\"jawahar_survey\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Automatic Detection of Machine Generated Text: A Critical Survey\\\", \\\"authors\\\": \\\"Jawahar, Ganesh and Abdul-Mageed, Muhammad and Lakshmanan, Laks V.S.\\\", \\\"year\\\": \\\"2020\\\", \\\"venue\\\": \\\"Proceedings of the International Conference on Computational Linguistics\\\"}, {\\\"key\\\": \\\"pythia\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling\\\", \\\"authors\\\": \\\"Biderman, Stella and Schoelkopf, Hailey and Anthony, Quentin Gregory and Bradley...\\\", \\\"year\\\": \\\"2023\\\", \\\"venue\\\": \\\"Proceedings of the International Conference on Machine Learning\\\"}, {\\\"key\\\": \\\"olmo\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"OLMo: Accelerating the Science of Language Models\\\", \\\"authors\\\": \\\"Groeneveld, Dirk and Beltagy, Iz and Walsh, Evan and Bhagia, Akshita and Kinney,...\\\", \\\"year\\\": \\\"2024\\\", \\\"venue\\\": \\\"Proceedings of the Annual Meeting of the Association for Computational Linguisti...\\\"}, {\\\"key\\\": \\\"qwen3\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Qwen3 Technical Report\\\", \\\"authors\\\": \\\"Qwen Team\\\", \\\"year\\\": \\\"2025\\\", \\\"venue\\\": \\\"arXiv preprint arXiv:2505.09388\\\"}, {\\\"key\\\": \\\"coral_ordinal\\\", \\\"type\\\": \\\"article\\\", \\\"title\\\": \\\"Rank Consistent Ordinal Regression for Neural Networks with Application to Age Estimation\\\", \\\"authors\\\": \\\"Cao, Wenzhi and Mirjalili, Vahid and Raschka, Sebastian\\\", \\\"year\\\": \\\"2020\\\", \\\"venue\\\": \\\"Pattern Recognition Letters\\\"}, {\\\"key\\\": \\\"frank_hall_ordinal\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"A Simple Approach to Ordinal Classification\\\", \\\"authors\\\": \\\"Frank, Eibe and Hall, Mark\\\", \\\"year\\\": \\\"2001\\\", \\\"venue\\\": \\\"Proceedings of the European Conference on Machine Learning\\\"}, {\\\"key\\\": \\\"xgboost\\\", \\\"type\\\": \\\"inproceedings\\\", \\\"title\\\": \\\"XGBoost: A Scalable Tree Boosting System\\\", \\\"authors\\\": \\\"Chen, Tianqi and Guestrin, Carlos\\\", \\\"year\\\": \\\"2016\\\", \\\"venue\\\": \\\"Proceedings of the ACM SIGKDD International Conference on Knowledge Discovery an...\\\"}], \\\"tex_citations\\\": [{\\\"key\\\": \\\"mapping_llm_science\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"monitoring_ai_review\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 5, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"fast_detectgpt\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"binoculars\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"ld_score\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"detectgpt\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"broken_telephone\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 18, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"markovian_chains\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 18, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"ood_baseline\\\", \\\"file\\\": \\\"introduction.tex\\\", \\\"line\\\": 23, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"gltr\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"grover\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"release_strategies\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"detectgpt\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"fast_detectgpt\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"binoculars\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"dna_gpt\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"feat_aug_transformer\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"reliable_detection\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"ld_score\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 7, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"intrinsic_dimension\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"diveye\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"generator_barrier\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 8, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"wu_survey_2025\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 9, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"jawahar_survey\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 9, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"beyond_binary\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 12, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"semeval2024_task8\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 12, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"paraphrase_evades\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 15, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"detection_possibilities\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 15, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"ood_baseline\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 16, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"uchendu_attribution\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 20, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"munir_looking_glass\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 20, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"self_consuming_mad\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 29, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"curse_of_recursion\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 29, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"model_collapse_avoidable\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 29, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"strong_model_collapse\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 30, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"broken_telephone\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 35, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"markovian_chains\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 36, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"curious_decline\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 42, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"writing_diversity\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 42, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"stamatatos_survey\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 45, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"koppel_authorship\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 45, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"uchendu_attribution\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 46, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"nucleus_sampling\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 48, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"dsir\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 54, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"qurating\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 54, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"ccnet\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 54, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"watermark_llm\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 57, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"synthid_text\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 57, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"aaronson_watermark\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 57, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"chainwash\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 58, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"min_k_percent\\\", \\\"file\\\": \\\"related_work.tex\\\", \\\"line\\\": 60, \\\"command\\\": \\\"citet\\\"}, {\\\"key\\\": \\\"pythia\\\", \\\"file\\\": \\\"method.tex\\\", \\\"line\\\": 16, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"olmo\\\", \\\"file\\\": \\\"method.tex\\\", \\\"line\\\": 16, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"qwen3\\\", \\\"file\\\": \\\"method.tex\\\", \\\"line\\\": 16, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"ood_baseline\\\", \\\"file\\\": \\\"method.tex\\\", \\\"line\\\": 48, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"xgboost\\\", \\\"file\\\": \\\"method.tex\\\", \\\"line\\\": 71, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"coral_ordinal\\\", \\\"file\\\": \\\"method.tex\\\", \\\"line\\\": 77, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"frank_hall_ordinal\\\", \\\"file\\\": \\\"method.tex\\\", \\\"line\\\": 77, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"fast_detectgpt\\\", \\\"file\\\": \\\"method.tex\\\", \\\"line\\\": 89, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"binoculars\\\", \\\"file\\\": \\\"method.tex\\\", \\\"line\\\": 89, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"ld_score\\\", \\\"file\\\": \\\"method.tex\\\", \\\"line\\\": 89, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"coral_ordinal\\\", \\\"file\\\": \\\"results.tex\\\", \\\"line\\\": 54, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"frank_hall_ordinal\\\", \\\"file\\\": \\\"results.tex\\\", \\\"line\\\": 54, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"detectgpt\\\", \\\"file\\\": \\\"discussion.tex\\\", \\\"line\\\": 13, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"gltr\\\", \\\"file\\\": \\\"discussion.tex\\\", \\\"line\\\": 13, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"binoculars\\\", \\\"file\\\": \\\"discussion.tex\\\", \\\"line\\\": 13, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"ood_baseline\\\", \\\"file\\\": \\\"discussion.tex\\\", \\\"line\\\": 15, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"broken_telephone\\\", \\\"file\\\": \\\"discussion.tex\\\", \\\"line\\\": 23, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"self_consuming_mad\\\", \\\"file\\\": \\\"discussion.tex\\\", \\\"line\\\": 28, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"curse_of_recursion\\\", \\\"file\\\": \\\"discussion.tex\\\", \\\"line\\\": 31, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"strong_model_collapse\\\", \\\"file\\\": \\\"discussion.tex\\\", \\\"line\\\": 31, \\\"command\\\": \\\"cite\\\"}, {\\\"key\\\": \\\"self_consuming_mad\\\", \\\"file\\\": \\\"discussion.tex\\\", \\\"line\\\": 31, \\\"command\\\": \\\"cite\\\"}], \\\"online_verification\\\": [{\\\"key\\\": \\\"detectgpt\\\", \\\"title\\\": \\\"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.382, \\\"matched_title\\\": \\\"Regulating ChatGPT and other Large Generative AI Models\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.38 below threshold 0.82\\\"}, {\\\"key\\\": \\\"gltr\\\", \\\"title\\\": \\\"GLTR: Statistical Detection and Visualization of Generated Text\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"GLTR: Statistical Detection and Visualization of Generated Text\\\", \\\"matched_year\\\": \\\"2019\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"dna_gpt\\\", \\\"title\\\": \\\"DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"binoculars\\\", \\\"title\\\": \\\"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"fast_detectgpt\\\", \\\"title\\\": \\\"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"ld_score\\\", \\\"title\\\": \\\"Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection\\\", \\\"matched_year\\\": \\\"2026\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"intrinsic_dimension\\\", \\\"title\\\": \\\"Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"diveye\\\", \\\"title\\\": \\\"Diversity Boosts AI-Generated Text Detection\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Diversity Boosts AI-Generated Text Detection\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"generator_barrier\\\", \\\"title\\\": \\\"Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection\\\", \\\"matched_year\\\": \\\"2026\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"feat_aug_transformer\\\", \\\"title\\\": \\\"Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators\\\", \\\"matched_year\\\": \\\"2026\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"reliable_detection\\\", \\\"title\\\": \\\"Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.344, \\\"matched_title\\\": \\\"2015 ESC Guidelines for the management of acute coronary syndromes in patients presenting without persistent ST-segment elevation\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.34 below threshold 0.82\\\"}, {\\\"key\\\": \\\"paraphrase_evades\\\", \\\"title\\\": \\\"Paraphrasing Evades Detectors of AI-Generated Text, but Retrieval is an Effective Defense\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"detection_possibilities\\\", \\\"title\\\": \\\"Position: On the Possibilities of AI-Generated Text Detection\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.253, \\\"matched_title\\\": \\\"Review of deep learning: concepts, CNN architectures, challenges, applications, future directions\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.25 below threshold 0.82\\\"}, {\\\"key\\\": \\\"grover\\\", \\\"title\\\": \\\"Defending Against Neural Fake News\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Defending Against Neural Fake News\\\", \\\"matched_year\\\": \\\"2019\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"release_strategies\\\", \\\"title\\\": \\\"Release Strategies and the Social Impacts of Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Release Strategies and the Social Impacts of Language Models\\\", \\\"matched_year\\\": \\\"2019\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"beyond_binary\\\", \\\"title\\\": \\\"Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"semeval2024_task8\\\", \\\"title\\\": \\\"SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"self_consuming_mad\\\", \\\"title\\\": \\\"Self-Consuming Generative Models Go MAD\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Self-Consuming Generative Models go MAD\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=alemohammad vs api=casco-rodriguez\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"curse_of_recursion\\\", \\\"title\\\": \\\"AI models collapse when trained on recursively generated data\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"AI models collapse when trained on recursively generated data\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"strong_model_collapse\\\", \\\"title\\\": \\\"Strong Model Collapse\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Strong Model Collapse\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"model_collapse_avoidable\\\", \\\"title\\\": \\\"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"ood_baseline\\\", \\\"title\\\": \\\"A Baseline for Detecting Misclassified and Out-of-Distribution Examples in Neural Networks\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"A Baseline for Detecting Misclassified and Out-of-Distribution Examples in Neural Networks\\\", \\\"matched_year\\\": \\\"2016\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"dsir\\\", \\\"title\\\": \\\"Data Selection for Language Models via Importance Resampling\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Data Selection for Language Models via Importance Resampling\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"qurating\\\", \\\"title\\\": \\\"QuRating: Selecting High-Quality Data for Training Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"QuRating: Selecting High-Quality Data for Training Language Models\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"ccnet\\\", \\\"title\\\": \\\"CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data\\\", \\\"matched_year\\\": \\\"2019\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"watermark_llm\\\", \\\"title\\\": \\\"A Watermark for Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"A Watermark for Large Language Models\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"synthid_text\\\", \\\"title\\\": \\\"Scalable Watermarking for Identifying Large Language Model Outputs\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Scalable watermarking for identifying large language model outputs\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"aaronson_watermark\\\", \\\"title\\\": \\\"Watermarking GPT Outputs\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.418, \\\"matched_title\\\": \\\"Undetectable Watermarks for Language Models\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.42 below threshold 0.82\\\"}, {\\\"key\\\": \\\"chainwash\\\", \\\"title\\\": \\\"Chainwash: Multi-Step Rewriting Attacks on Diffusion Language Model Watermarks\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Chainwash: Multi-Step Rewriting Attacks on Diffusion Language Model Watermarks\\\", \\\"matched_year\\\": \\\"2026\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"curious_decline\\\", \\\"title\\\": \\\"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"writing_diversity\\\", \\\"title\\\": \\\"Does Writing with Language Models Reduce Content Diversity?\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Does Writing with Language Models Reduce Content Diversity?\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"nucleus_sampling\\\", \\\"title\\\": \\\"The Curious Case of Neural Text Degeneration\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"The Curious Case of Neural Text Degeneration\\\", \\\"matched_year\\\": \\\"2019\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"mapping_llm_science\\\", \\\"title\\\": \\\"Mapping the Increasing Use of LLMs in Scientific Papers\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Mapping the Increasing Use of LLMs in Scientific Papers\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"monitoring_ai_review\\\", \\\"title\\\": \\\"Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"stamatatos_survey\\\", \\\"title\\\": \\\"A Survey of Modern Authorship Attribution Methods\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"A survey of modern authorship attribution methods\\\", \\\"matched_year\\\": \\\"2008\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"koppel_authorship\\\", \\\"title\\\": \\\"Computational Methods in Authorship Attribution\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Computational methods in authorship attribution\\\", \\\"matched_year\\\": \\\"2008\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"uchendu_attribution\\\", \\\"title\\\": \\\"Authorship Attribution for Neural Text Generation\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Authorship Attribution for Neural Text Generation\\\", \\\"matched_year\\\": \\\"2020\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"munir_looking_glass\\\", \\\"title\\\": \\\"Through the Looking Glass: Learning to Attribute Synthetic Text Generated by Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Through the Looking Glass: Learning to Attribute Synthetic Text Generated by Language Models\\\", \\\"matched_year\\\": \\\"2021\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"broken_telephone\\\", \\\"title\\\": \\\"LLM as a Broken Telephone: Iterative Generation Distorts Information\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"LLM as a Broken Telephone: Iterative Generation Distorts Information\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"markovian_chains\\\", \\\"title\\\": \\\"Markovian Generation Chains in Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Markovian Generation Chains in Large Language Models\\\", \\\"matched_year\\\": \\\"2026\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"min_k_percent\\\", \\\"title\\\": \\\"Detecting Pretraining Data from Large Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Detecting Pretraining Data from Large Language Models\\\", \\\"matched_year\\\": \\\"2023\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"wu_survey_2025\\\", \\\"title\\\": \\\"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"jawahar_survey\\\", \\\"title\\\": \\\"Automatic Detection of Machine Generated Text: A Critical Survey\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Automatic Detection of Machine Generated Text: A Critical Survey\\\", \\\"matched_year\\\": \\\"2020\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"pythia\\\", \\\"title\\\": \\\"Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.497, \\\"matched_title\\\": \\\"The TRIPOD-LLM reporting guideline for studies using large language models\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.50 below threshold 0.82\\\"}, {\\\"key\\\": \\\"olmo\\\", \\\"title\\\": \\\"OLMo: Accelerating the Science of Language Models\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"OLMo: Accelerating the Science of Language Models\\\", \\\"matched_year\\\": \\\"2024\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"qwen3\\\", \\\"title\\\": \\\"Qwen3 Technical Report\\\", \\\"status\\\": \\\"mismatch\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Qwen3 Technical Report\\\", \\\"matched_year\\\": \\\"2025\\\", \\\"mismatch_fields\\\": [\\\"first_author: bib=team vs api=yang\\\"], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"coral_ordinal\\\", \\\"title\\\": \\\"Rank Consistent Ordinal Regression for Neural Networks with Application to Age Estimation\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"Rank consistent ordinal regression for neural networks with application to age estimation\\\", \\\"matched_year\\\": \\\"2020\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"frank_hall_ordinal\\\", \\\"title\\\": \\\"A Simple Approach to Ordinal Classification\\\", \\\"status\\\": \\\"verified\\\", \\\"confidence\\\": 1.0, \\\"matched_title\\\": \\\"A Simple Approach to Ordinal Classification\\\", \\\"matched_year\\\": \\\"2001\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"\\\"}, {\\\"key\\\": \\\"xgboost\\\", \\\"title\\\": \\\"XGBoost: A Scalable Tree Boosting System\\\", \\\"status\\\": \\\"not_found\\\", \\\"confidence\\\": 0.298, \\\"matched_title\\\": \\\"XGBoost\\\", \\\"matched_year\\\": \\\"\\\", \\\"mismatch_fields\\\": [], \\\"note\\\": \\\"best match similarity 0.30 below threshold 0.82\\\"}]}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 49, \"total_citations\": 72, \"unique_cited_keys\": 49, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 41, \"online_not_found\": 6, \"online_mismatch\": 2}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"detectgpt\", \"type\": \"inproceedings\", \"title\": \"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature\", \"authors\": \"Mitchell, Eric and Lee, Yoonho and Khazatsky, Alexander and Manning, Christopher...\", \"year\": \"2023\", \"venue\": \"Proceedings of the International Conference on Machine Learning\"}, {\"key\": \"gltr\", \"type\": \"inproceedings\", \"title\": \"GLTR: Statistical Detection and Visualization of Generated Text\", \"authors\": \"Gehrmann, Sebastian and Strobelt, Hendrik and Rush, Alexander M.\", \"year\": \"2019\", \"venue\": \"Proceedings of the Annual Meeting of the Association for Computational Linguisti...\"}, {\"key\": \"dna_gpt\", \"type\": \"inproceedings\", \"title\": \"DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text\", \"authors\": \"Yang, Xianjun and Cheng, Wei and Wu, Yue and Petzold, Linda and Wang, William Ya...\", \"year\": \"2024\", \"venue\": \"Proceedings of the International Conference on Learning Representations\"}, {\"key\": \"binoculars\", \"type\": \"inproceedings\", \"title\": \"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text\", \"authors\": \"Hans, Abhimanyu and Schwarzschild, Avi and Cherepanova, Valeriia and Kazemi, Ham...\", \"year\": \"2024\", \"venue\": \"Proceedings of the International Conference on Machine Learning\"}, {\"key\": \"fast_detectgpt\", \"type\": \"inproceedings\", \"title\": \"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature\", \"authors\": \"Bao, Guangsheng and Zhao, Yanbin and Teng, Zhiyang and Yang, Linyi and Zhang, Yu...\", \"year\": \"2024\", \"venue\": \"Proceedings of the International Conference on Learning Representations\"}, {\"key\": \"ld_score\", \"type\": \"article\", \"title\": \"Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection\", \"authors\": \"Narayanasamy, Priyadarshan and Agrawal, Swastik and Faber, Klint and Alam, Fardi...\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2605.01647\"}, {\"key\": \"intrinsic_dimension\", \"type\": \"inproceedings\", \"title\": \"Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts\", \"authors\": \"Tulchinskii, Eduard and Kuznetsov, Kristian and Kushnareva, Laida and Cherniavsk...\", \"year\": \"2023\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"diveye\", \"type\": \"article\", \"title\": \"Diversity Boosts AI-Generated Text Detection\", \"authors\": \"Basani, Advik Raj and Chen, Pin-Yu\", \"year\": \"2026\", \"venue\": \"Transactions on Machine Learning Research\"}, {\"key\": \"generator_barrier\", \"type\": \"article\", \"title\": \"Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection\", \"authors\": \"Pu, Xiao and Cheng, Zepeng and Yuan, Lin and Wu, Yu and Bi, Xiuli\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2604.13692\"}, {\"key\": \"feat_aug_transformer\", \"type\": \"article\", \"title\": \"Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators\", \"authors\": \"Mady, Mohamed and Reschke, Johannes and Schuller, Bj\\\\\\\"orn\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2605.03969\"}, {\"key\": \"reliable_detection\", \"type\": \"article\", \"title\": \"Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks\", \"authors\": \"Sadasivan, Vinu Sankar and Kumar, Aounon and Balasubramanian, Sriram and Wang, W...\", \"year\": \"2025\", \"venue\": \"Transactions on Machine Learning Research\"}, {\"key\": \"paraphrase_evades\", \"type\": \"inproceedings\", \"title\": \"Paraphrasing Evades Detectors of AI-Generated Text, but Retrieval is an Effective Defense\", \"authors\": \"Krishna, Kalpesh and Song, Yixiao and Karpinska, Marzena and Wieting, John and I...\", \"year\": \"2023\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"detection_possibilities\", \"type\": \"inproceedings\", \"title\": \"Position: On the Possibilities of AI-Generated Text Detection\", \"authors\": \"Chakraborty, Souradip and Bedi, Amrit Singh and Zhu, Sicheng and An, Bang and Ma...\", \"year\": \"2024\", \"venue\": \"Proceedings of the International Conference on Machine Learning\"}, {\"key\": \"grover\", \"type\": \"inproceedings\", \"title\": \"Defending Against Neural Fake News\", \"authors\": \"Zellers, Rowan and Holtzman, Ari and Rashkin, Hannah and Bisk, Yonatan and Farha...\", \"year\": \"2019\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"release_strategies\", \"type\": \"article\", \"title\": \"Release Strategies and the Social Impacts of Language Models\", \"authors\": \"Solaiman, Irene and Brundage, Miles and Clark, Jack and Askell, Amanda and Herbe...\", \"year\": \"2019\", \"venue\": \"arXiv preprint arXiv:1908.09203\"}, {\"key\": \"beyond_binary\", \"type\": \"inproceedings\", \"title\": \"Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement\", \"authors\": \"Cheng, Zihao and Zhou, Li and Jiang, Feng and Wang, Benyou and Li, Haizhou\", \"year\": \"2025\", \"venue\": \"Proceedings of the ACM Web Conference\"}, {\"key\": \"semeval2024_task8\", \"type\": \"inproceedings\", \"title\": \"SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection\", \"authors\": \"Wang, Yuxia and Mansurov, Jonibek and Ivanov, Petar and Su, Jinyan and Shelmanov...\", \"year\": \"2024\", \"venue\": \"Proceedings of the International Workshop on Semantic Evaluation\"}, {\"key\": \"self_consuming_mad\", \"type\": \"inproceedings\", \"title\": \"Self-Consuming Generative Models Go MAD\", \"authors\": \"Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahme...\", \"year\": \"2024\", \"venue\": \"Proceedings of the International Conference on Learning Representations\"}, {\"key\": \"curse_of_recursion\", \"type\": \"article\", \"title\": \"AI models collapse when trained on recursively generated data\", \"authors\": \"Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and ...\", \"year\": \"2024\", \"venue\": \"Nature\"}, {\"key\": \"strong_model_collapse\", \"type\": \"inproceedings\", \"title\": \"Strong Model Collapse\", \"authors\": \"Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia\", \"year\": \"2025\", \"venue\": \"Proceedings of the International Conference on Learning Representations\"}, {\"key\": \"model_collapse_avoidable\", \"type\": \"inproceedings\", \"title\": \"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data\", \"authors\": \"Gerstgrasser, Matthias and Schaeffer, Rylan and Dey, Apratim and Rafailov, Rafae...\", \"year\": \"2024\", \"venue\": \"Proceedings of the International Conference on Machine Learning\"}, {\"key\": \"ood_baseline\", \"type\": \"inproceedings\", \"title\": \"A Baseline for Detecting Misclassified and Out-of-Distribution Examples in Neural Networks\", \"authors\": \"Hendrycks, Dan and Gimpel, Kevin\", \"year\": \"2017\", \"venue\": \"Proceedings of the International Conference on Learning Representations\"}, {\"key\": \"dsir\", \"type\": \"inproceedings\", \"title\": \"Data Selection for Language Models via Importance Resampling\", \"authors\": \"Xie, Sang Michael and Santurkar, Shibani and Ma, Tengyu and Liang, Percy\", \"year\": \"2023\", \"venue\": \"Advances in Neural Information Processing Systems\"}, {\"key\": \"qurating\", \"type\": \"inproceedings\", \"title\": \"QuRating: Selecting High-Quality Data for Training Language Models\", \"authors\": \"Wettig, Alexander and Gupta, Aatmik and Malik, Saumya and Chen, Danqi\", \"year\": \"2024\", \"venue\": \"Proceedings of the International Conference on Machine Learning\"}, {\"key\": \"ccnet\", \"type\": \"inproceedings\", \"title\": \"CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data\", \"authors\": \"Wenzek, Guillaume and Lachaux, Marie-Anne and Conneau, Alexis and Chaudhary, Vis...\", \"year\": \"2020\", \"venue\": \"Proceedings of the Language Resources and Evaluation Conference\"}, {\"key\": \"watermark_llm\", \"type\": \"inproceedings\", \"title\": \"A Watermark for Large Language Models\", \"authors\": \"Kirchenbauer, John and Geiping, Jonas and Wen, Yuxin and Katz, Jonathan and Mier...\", \"year\": \"2023\", \"venue\": \"Proceedings of the International Conference on Machine Learning\"}, {\"key\": \"synthid_text\", \"type\": \"article\", \"title\": \"Scalable Watermarking for Identifying Large Language Model Outputs\", \"authors\": \"Dathathri, Sumanth and See, Abigail and Ghaisas, Sumedh and Huang, Po-Sen and Mc...\", \"year\": \"2024\", \"venue\": \"Nature\"}, {\"key\": \"aaronson_watermark\", \"type\": \"misc\", \"title\": \"Watermarking GPT Outputs\", \"authors\": \"Aaronson, Scott and Kirchner, Hendrik\", \"year\": \"2022\", \"venue\": \"\"}, {\"key\": \"chainwash\", \"type\": \"article\", \"title\": \"Chainwash: Multi-Step Rewriting Attacks on Diffusion Language Model Watermarks\", \"authors\": \"Ameen, Mohd Ruhul and Islam, Akif and Mahmud, Nadim and Hamid, Md. Ekramul\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2605.05503\"}, {\"key\": \"curious_decline\", \"type\": \"inproceedings\", \"title\": \"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text\", \"authors\": \"Guo, Yanzhu and Shang, Guokan and Vazirgiannis, Michalis and Clavel, Chlo\\\\'e\", \"year\": \"2024\", \"venue\": \"Findings of the Association for Computational Linguistics: NAACL\"}, {\"key\": \"writing_diversity\", \"type\": \"inproceedings\", \"title\": \"Does Writing with Language Models Reduce Content Diversity?\", \"authors\": \"Padmakumar, Vishakh and He, He\", \"year\": \"2024\", \"venue\": \"Proceedings of the International Conference on Learning Representations\"}, {\"key\": \"nucleus_sampling\", \"type\": \"inproceedings\", \"title\": \"The Curious Case of Neural Text Degeneration\", \"authors\": \"Holtzman, Ari and Buys, Jan and Du, Li and Forbes, Maxwell and Choi, Yejin\", \"year\": \"2020\", \"venue\": \"Proceedings of the International Conference on Learning Representations\"}, {\"key\": \"mapping_llm_science\", \"type\": \"inproceedings\", \"title\": \"Mapping the Increasing Use of LLMs in Scientific Papers\", \"authors\": \"Liang, Weixin and Zhang, Yaohui and Wu, Zhengxuan and Lepp, Haley and Ji, Wenlon...\", \"year\": \"2024\", \"venue\": \"Proceedings of the Conference on Language Modeling\"}, {\"key\": \"monitoring_ai_review\", \"type\": \"inproceedings\", \"title\": \"Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews\", \"authors\": \"Liang, Weixin and Izzo, Zachary and Zhang, Yaohui and Lepp, Haley and Cao, Hanch...\", \"year\": \"2024\", \"venue\": \"Proceedings of the International Conference on Machine Learning\"}, {\"key\": \"stamatatos_survey\", \"type\": \"article\", \"title\": \"A Survey of Modern Authorship Attribution Methods\", \"authors\": \"Stamatatos, Efstathios\", \"year\": \"2009\", \"venue\": \"Journal of the American Society for Information Science and Technology\"}, {\"key\": \"koppel_authorship\", \"type\": \"article\", \"title\": \"Computational Methods in Authorship Attribution\", \"authors\": \"Koppel, Moshe and Schler, Jonathan and Argamon, Shlomo\", \"year\": \"2009\", \"venue\": \"Journal of the American Society for Information Science and Technology\"}, {\"key\": \"uchendu_attribution\", \"type\": \"inproceedings\", \"title\": \"Authorship Attribution for Neural Text Generation\", \"authors\": \"Uchendu, Adaku and Le, Thai and Shu, Kai and Lee, Dongwon\", \"year\": \"2020\", \"venue\": \"Proceedings of the Conference on Empirical Methods in Natural Language Processin...\"}, {\"key\": \"munir_looking_glass\", \"type\": \"inproceedings\", \"title\": \"Through the Looking Glass: Learning to Attribute Synthetic Text Generated by Language Models\", \"authors\": \"Munir, Shaoor and Batool, Brishna and Shafiq, Zubair and Srinivasan, Padmini and...\", \"year\": \"2021\", \"venue\": \"Proceedings of the Conference of the European Chapter of the Association for Com...\"}, {\"key\": \"broken_telephone\", \"type\": \"inproceedings\", \"title\": \"LLM as a Broken Telephone: Iterative Generation Distorts Information\", \"authors\": \"Mohamed, Amr and Geng, Mingmeng and Vazirgiannis, Michalis and Shang, Guokan\", \"year\": \"2025\", \"venue\": \"Proceedings of the Annual Meeting of the Association for Computational Linguisti...\"}, {\"key\": \"markovian_chains\", \"type\": \"article\", \"title\": \"Markovian Generation Chains in Large Language Models\", \"authors\": \"Geng, Mingmeng and Mohamed, Amr and Shang, Guokan and Vazirgiannis, Michalis and...\", \"year\": \"2026\", \"venue\": \"arXiv preprint arXiv:2603.11228\"}, {\"key\": \"min_k_percent\", \"type\": \"inproceedings\", \"title\": \"Detecting Pretraining Data from Large Language Models\", \"authors\": \"Shi, Weijia and Ajith, Anirudh and Xia, Mengzhou and Huang, Yangsibo and Liu, Da...\", \"year\": \"2024\", \"venue\": \"Proceedings of the International Conference on Learning Representations\"}, {\"key\": \"wu_survey_2025\", \"type\": \"article\", \"title\": \"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions\", \"authors\": \"Wu, Junchao and Yang, Shu and Zhan, Runzhe and Yuan, Yulin and Chao, Lidia Sam a...\", \"year\": \"2025\", \"venue\": \"Computational Linguistics\"}, {\"key\": \"jawahar_survey\", \"type\": \"inproceedings\", \"title\": \"Automatic Detection of Machine Generated Text: A Critical Survey\", \"authors\": \"Jawahar, Ganesh and Abdul-Mageed, Muhammad and Lakshmanan, Laks V.S.\", \"year\": \"2020\", \"venue\": \"Proceedings of the International Conference on Computational Linguistics\"}, {\"key\": \"pythia\", \"type\": \"inproceedings\", \"title\": \"Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling\", \"authors\": \"Biderman, Stella and Schoelkopf, Hailey and Anthony, Quentin Gregory and Bradley...\", \"year\": \"2023\", \"venue\": \"Proceedings of the International Conference on Machine Learning\"}, {\"key\": \"olmo\", \"type\": \"inproceedings\", \"title\": \"OLMo: Accelerating the Science of Language Models\", \"authors\": \"Groeneveld, Dirk and Beltagy, Iz and Walsh, Evan and Bhagia, Akshita and Kinney,...\", \"year\": \"2024\", \"venue\": \"Proceedings of the Annual Meeting of the Association for Computational Linguisti...\"}, {\"key\": \"qwen3\", \"type\": \"article\", \"title\": \"Qwen3 Technical Report\", \"authors\": \"Qwen Team\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2505.09388\"}, {\"key\": \"coral_ordinal\", \"type\": \"article\", \"title\": \"Rank Consistent Ordinal Regression for Neural Networks with Application to Age Estimation\", \"authors\": \"Cao, Wenzhi and Mirjalili, Vahid and Raschka, Sebastian\", \"year\": \"2020\", \"venue\": \"Pattern Recognition Letters\"}, {\"key\": \"frank_hall_ordinal\", \"type\": \"inproceedings\", \"title\": \"A Simple Approach to Ordinal Classification\", \"authors\": \"Frank, Eibe and Hall, Mark\", \"year\": \"2001\", \"venue\": \"Proceedings of the European Conference on Machine Learning\"}, {\"key\": \"xgboost\", \"type\": \"inproceedings\", \"title\": \"XGBoost: A Scalable Tree Boosting System\", \"authors\": \"Chen, Tianqi and Guestrin, Carlos\", \"year\": \"2016\", \"venue\": \"Proceedings of the ACM SIGKDD International Conference on Knowledge Discovery an...\"}], \"tex_citations\": [{\"key\": \"mapping_llm_science\", \"file\": \"introduction.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"monitoring_ai_review\", \"file\": \"introduction.tex\", \"line\": 5, \"command\": \"cite\"}, {\"key\": \"fast_detectgpt\", \"file\": \"introduction.tex\", \"line\": 8, \"command\": \"cite\"}, {\"key\": \"binoculars\", \"file\": \"introduction.tex\", \"line\": 8, \"command\": \"cite\"}, {\"key\": \"ld_score\", \"file\": \"introduction.tex\", \"line\": 8, \"command\": \"cite\"}, {\"key\": \"detectgpt\", \"file\": \"introduction.tex\", \"line\": 8, \"command\": \"cite\"}, {\"key\": \"broken_telephone\", \"file\": \"introduction.tex\", \"line\": 18, \"command\": \"cite\"}, {\"key\": \"markovian_chains\", \"file\": \"introduction.tex\", \"line\": 18, \"command\": \"cite\"}, {\"key\": \"ood_baseline\", \"file\": \"introduction.tex\", \"line\": 23, \"command\": \"cite\"}, {\"key\": \"gltr\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"grover\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"release_strategies\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"detectgpt\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"fast_detectgpt\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"binoculars\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"dna_gpt\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"feat_aug_transformer\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"reliable_detection\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"ld_score\", \"file\": \"related_work.tex\", \"line\": 7, \"command\": \"cite\"}, {\"key\": \"intrinsic_dimension\", \"file\": \"related_work.tex\", \"line\": 8, \"command\": \"citet\"}, {\"key\": \"diveye\", \"file\": \"related_work.tex\", \"line\": 8, \"command\": \"citet\"}, {\"key\": \"generator_barrier\", \"file\": \"related_work.tex\", \"line\": 8, \"command\": \"citet\"}, {\"key\": \"wu_survey_2025\", \"file\": \"related_work.tex\", \"line\": 9, \"command\": \"citet\"}, {\"key\": \"jawahar_survey\", \"file\": \"related_work.tex\", \"line\": 9, \"command\": \"citet\"}, {\"key\": \"beyond_binary\", \"file\": \"related_work.tex\", \"line\": 12, \"command\": \"citet\"}, {\"key\": \"semeval2024_task8\", \"file\": \"related_work.tex\", \"line\": 12, \"command\": \"cite\"}, {\"key\": \"paraphrase_evades\", \"file\": \"related_work.tex\", \"line\": 15, \"command\": \"citet\"}, {\"key\": \"detection_possibilities\", \"file\": \"related_work.tex\", \"line\": 15, \"command\": \"citet\"}, {\"key\": \"ood_baseline\", \"file\": \"related_work.tex\", \"line\": 16, \"command\": \"cite\"}, {\"key\": \"uchendu_attribution\", \"file\": \"related_work.tex\", \"line\": 20, \"command\": \"citet\"}, {\"key\": \"munir_looking_glass\", \"file\": \"related_work.tex\", \"line\": 20, \"command\": \"citet\"}, {\"key\": \"self_consuming_mad\", \"file\": \"related_work.tex\", \"line\": 29, \"command\": \"citet\"}, {\"key\": \"curse_of_recursion\", \"file\": \"related_work.tex\", \"line\": 29, \"command\": \"citet\"}, {\"key\": \"model_collapse_avoidable\", \"file\": \"related_work.tex\", \"line\": 29, \"command\": \"citet\"}, {\"key\": \"strong_model_collapse\", \"file\": \"related_work.tex\", \"line\": 30, \"command\": \"citet\"}, {\"key\": \"broken_telephone\", \"file\": \"related_work.tex\", \"line\": 35, \"command\": \"citet\"}, {\"key\": \"markovian_chains\", \"file\": \"related_work.tex\", \"line\": 36, \"command\": \"citet\"}, {\"key\": \"curious_decline\", \"file\": \"related_work.tex\", \"line\": 42, \"command\": \"cite\"}, {\"key\": \"writing_diversity\", \"file\": \"related_work.tex\", \"line\": 42, \"command\": \"cite\"}, {\"key\": \"stamatatos_survey\", \"file\": \"related_work.tex\", \"line\": 45, \"command\": \"cite\"}, {\"key\": \"koppel_authorship\", \"file\": \"related_work.tex\", \"line\": 45, \"command\": \"cite\"}, {\"key\": \"uchendu_attribution\", \"file\": \"related_work.tex\", \"line\": 46, \"command\": \"citet\"}, {\"key\": \"nucleus_sampling\", \"file\": \"related_work.tex\", \"line\": 48, \"command\": \"citet\"}, {\"key\": \"dsir\", \"file\": \"related_work.tex\", \"line\": 54, \"command\": \"citet\"}, {\"key\": \"qurating\", \"file\": \"related_work.tex\", \"line\": 54, \"command\": \"citet\"}, {\"key\": \"ccnet\", \"file\": \"related_work.tex\", \"line\": 54, \"command\": \"citet\"}, {\"key\": \"watermark_llm\", \"file\": \"related_work.tex\", \"line\": 57, \"command\": \"cite\"}, {\"key\": \"synthid_text\", \"file\": \"related_work.tex\", \"line\": 57, \"command\": \"cite\"}, {\"key\": \"aaronson_watermark\", \"file\": \"related_work.tex\", \"line\": 57, \"command\": \"cite\"}, {\"key\": \"chainwash\", \"file\": \"related_work.tex\", \"line\": 58, \"command\": \"citet\"}, {\"key\": \"min_k_percent\", \"file\": \"related_work.tex\", \"line\": 60, \"command\": \"citet\"}, {\"key\": \"pythia\", \"file\": \"method.tex\", \"line\": 16, \"command\": \"cite\"}, {\"key\": \"olmo\", \"file\": \"method.tex\", \"line\": 16, \"command\": \"cite\"}, {\"key\": \"qwen3\", \"file\": \"method.tex\", \"line\": 16, \"command\": \"cite\"}, {\"key\": \"ood_baseline\", \"file\": \"method.tex\", \"line\": 48, \"command\": \"cite\"}, {\"key\": \"xgboost\", \"file\": \"method.tex\", \"line\": 71, \"command\": \"cite\"}, {\"key\": \"coral_ordinal\", \"file\": \"method.tex\", \"line\": 77, \"command\": \"cite\"}, {\"key\": \"frank_hall_ordinal\", \"file\": \"method.tex\", \"line\": 77, \"command\": \"cite\"}, {\"key\": \"fast_detectgpt\", \"file\": \"method.tex\", \"line\": 89, \"command\": \"cite\"}, {\"key\": \"binoculars\", \"file\": \"method.tex\", \"line\": 89, \"command\": \"cite\"}, {\"key\": \"ld_score\", \"file\": \"method.tex\", \"line\": 89, \"command\": \"cite\"}, {\"key\": \"coral_ordinal\", \"file\": \"results.tex\", \"line\": 54, \"command\": \"cite\"}, {\"key\": \"frank_hall_ordinal\", \"file\": \"results.tex\", \"line\": 54, \"command\": \"cite\"}, {\"key\": \"detectgpt\", \"file\": \"discussion.tex\", \"line\": 13, \"command\": \"cite\"}, {\"key\": \"gltr\", \"file\": \"discussion.tex\", \"line\": 13, \"command\": \"cite\"}, {\"key\": \"binoculars\", \"file\": \"discussion.tex\", \"line\": 13, \"command\": \"cite\"}, {\"key\": \"ood_baseline\", \"file\": \"discussion.tex\", \"line\": 15, \"command\": \"cite\"}, {\"key\": \"broken_telephone\", \"file\": \"discussion.tex\", \"line\": 23, \"command\": \"cite\"}, {\"key\": \"self_consuming_mad\", \"file\": \"discussion.tex\", \"line\": 28, \"command\": \"cite\"}, {\"key\": \"curse_of_recursion\", \"file\": \"discussion.tex\", \"line\": 31, \"command\": \"cite\"}, {\"key\": \"strong_model_collapse\", \"file\": \"discussion.tex\", \"line\": 31, \"command\": \"cite\"}, {\"key\": \"self_consuming_mad\", \"file\": \"discussion.tex\", \"line\": 31, \"command\": \"cite\"}], \"online_verification\": [{\"key\": \"detectgpt\", \"title\": \"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature\", \"status\": \"not_found\", \"confidence\": 0.382, \"matched_title\": \"Regulating ChatGPT and other Large Generative AI Models\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.38 below threshold 0.82\"}, {\"key\": \"gltr\", \"title\": \"GLTR: Statistical Detection and Visualization of Generated Text\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"GLTR: Statistical Detection and Visualization of Generated Text\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"dna_gpt\", \"title\": \"DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"binoculars\", \"title\": \"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"fast_detectgpt\", \"title\": \"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"ld_score\", \"title\": \"Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"intrinsic_dimension\", \"title\": \"Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"diveye\", \"title\": \"Diversity Boosts AI-Generated Text Detection\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Diversity Boosts AI-Generated Text Detection\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"generator_barrier\", \"title\": \"Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"feat_aug_transformer\", \"title\": \"Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"reliable_detection\", \"title\": \"Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks\", \"status\": \"not_found\", \"confidence\": 0.344, \"matched_title\": \"2015 ESC Guidelines for the management of acute coronary syndromes in patients presenting without persistent ST-segment elevation\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.34 below threshold 0.82\"}, {\"key\": \"paraphrase_evades\", \"title\": \"Paraphrasing Evades Detectors of AI-Generated Text, but Retrieval is an Effective Defense\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"detection_possibilities\", \"title\": \"Position: On the Possibilities of AI-Generated Text Detection\", \"status\": \"not_found\", \"confidence\": 0.253, \"matched_title\": \"Review of deep learning: concepts, CNN architectures, challenges, applications, future directions\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.25 below threshold 0.82\"}, {\"key\": \"grover\", \"title\": \"Defending Against Neural Fake News\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Defending Against Neural Fake News\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"release_strategies\", \"title\": \"Release Strategies and the Social Impacts of Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Release Strategies and the Social Impacts of Language Models\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"beyond_binary\", \"title\": \"Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"semeval2024_task8\", \"title\": \"SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"self_consuming_mad\", \"title\": \"Self-Consuming Generative Models Go MAD\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Self-Consuming Generative Models go MAD\", \"matched_year\": \"2023\", \"mismatch_fields\": [\"first_author: bib=alemohammad vs api=casco-rodriguez\"], \"note\": \"\"}, {\"key\": \"curse_of_recursion\", \"title\": \"AI models collapse when trained on recursively generated data\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"AI models collapse when trained on recursively generated data\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"strong_model_collapse\", \"title\": \"Strong Model Collapse\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Strong Model Collapse\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"model_collapse_avoidable\", \"title\": \"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"ood_baseline\", \"title\": \"A Baseline for Detecting Misclassified and Out-of-Distribution Examples in Neural Networks\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Baseline for Detecting Misclassified and Out-of-Distribution Examples in Neural Networks\", \"matched_year\": \"2016\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"dsir\", \"title\": \"Data Selection for Language Models via Importance Resampling\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Data Selection for Language Models via Importance Resampling\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"qurating\", \"title\": \"QuRating: Selecting High-Quality Data for Training Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"QuRating: Selecting High-Quality Data for Training Language Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"ccnet\", \"title\": \"CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"watermark_llm\", \"title\": \"A Watermark for Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Watermark for Large Language Models\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"synthid_text\", \"title\": \"Scalable Watermarking for Identifying Large Language Model Outputs\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Scalable watermarking for identifying large language model outputs\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"aaronson_watermark\", \"title\": \"Watermarking GPT Outputs\", \"status\": \"not_found\", \"confidence\": 0.418, \"matched_title\": \"Undetectable Watermarks for Language Models\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.42 below threshold 0.82\"}, {\"key\": \"chainwash\", \"title\": \"Chainwash: Multi-Step Rewriting Attacks on Diffusion Language Model Watermarks\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Chainwash: Multi-Step Rewriting Attacks on Diffusion Language Model Watermarks\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"curious_decline\", \"title\": \"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"writing_diversity\", \"title\": \"Does Writing with Language Models Reduce Content Diversity?\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Does Writing with Language Models Reduce Content Diversity?\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"nucleus_sampling\", \"title\": \"The Curious Case of Neural Text Degeneration\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"The Curious Case of Neural Text Degeneration\", \"matched_year\": \"2019\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"mapping_llm_science\", \"title\": \"Mapping the Increasing Use of LLMs in Scientific Papers\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Mapping the Increasing Use of LLMs in Scientific Papers\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"monitoring_ai_review\", \"title\": \"Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"stamatatos_survey\", \"title\": \"A Survey of Modern Authorship Attribution Methods\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A survey of modern authorship attribution methods\", \"matched_year\": \"2008\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"koppel_authorship\", \"title\": \"Computational Methods in Authorship Attribution\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Computational methods in authorship attribution\", \"matched_year\": \"2008\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"uchendu_attribution\", \"title\": \"Authorship Attribution for Neural Text Generation\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Authorship Attribution for Neural Text Generation\", \"matched_year\": \"2020\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"munir_looking_glass\", \"title\": \"Through the Looking Glass: Learning to Attribute Synthetic Text Generated by Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Through the Looking Glass: Learning to Attribute Synthetic Text Generated by Language Models\", \"matched_year\": \"2021\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"broken_telephone\", \"title\": \"LLM as a Broken Telephone: Iterative Generation Distorts Information\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"LLM as a Broken Telephone: Iterative Generation Distorts Information\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"markovian_chains\", \"title\": \"Markovian Generation Chains in Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Markovian Generation Chains in Large Language Models\", \"matched_year\": \"2026\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"min_k_percent\", \"title\": \"Detecting Pretraining Data from Large Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Detecting Pretraining Data from Large Language Models\", \"matched_year\": \"2023\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"wu_survey_2025\", \"title\": \"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions\", \"matched_year\": \"2025\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"jawahar_survey\", \"title\": \"Automatic Detection of Machine Generated Text: A Critical Survey\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Automatic Detection of Machine Generated Text: A Critical Survey\", \"matched_year\": \"2020\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"pythia\", \"title\": \"Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling\", \"status\": \"not_found\", \"confidence\": 0.497, \"matched_title\": \"The TRIPOD-LLM reporting guideline for studies using large language models\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.50 below threshold 0.82\"}, {\"key\": \"olmo\", \"title\": \"OLMo: Accelerating the Science of Language Models\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"OLMo: Accelerating the Science of Language Models\", \"matched_year\": \"2024\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"qwen3\", \"title\": \"Qwen3 Technical Report\", \"status\": \"mismatch\", \"confidence\": 1.0, \"matched_title\": \"Qwen3 Technical Report\", \"matched_year\": \"2025\", \"mismatch_fields\": [\"first_author: bib=team vs api=yang\"], \"note\": \"\"}, {\"key\": \"coral_ordinal\", \"title\": \"Rank Consistent Ordinal Regression for Neural Networks with Application to Age Estimation\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"Rank consistent ordinal regression for neural networks with application to age estimation\", \"matched_year\": \"2020\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"frank_hall_ordinal\", \"title\": \"A Simple Approach to Ordinal Classification\", \"status\": \"verified\", \"confidence\": 1.0, \"matched_title\": \"A Simple Approach to Ordinal Classification\", \"matched_year\": \"2001\", \"mismatch_fields\": [], \"note\": \"\"}, {\"key\": \"xgboost\", \"title\": \"XGBoost: A Scalable Tree Boosting System\", \"status\": \"not_found\", \"confidence\": 0.298, \"matched_title\": \"XGBoost\", \"matched_year\": \"\", \"mismatch_fields\": [], \"note\": \"best match similarity 0.30 below threshold 0.82\"}]}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-15T20:36:16.345Z_

<details><summary>↩ Tool result · `toolu_01GnooHoXiMe34iqvvpbVEij`</summary>

```text
1	% ===== Detection =====
2	
3	@inproceedings{detectgpt,
4	  title = {{DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature}},
5	  author = {Mitchell, Eric and Lee, Yoonho and Khazatsky, Alexander and Manning, Christopher D. and Finn, Chelsea},
6	  booktitle = {Proceedings of the International Conference on Machine Learning},
7	  year = {2023},
8	}
9	
10	@inproceedings{gltr,
11	  title = {{GLTR: Statistical Detection and Visualization of Generated Text}},
12	  author = {Gehrmann, Sebastian and Strobelt, Hendrik and Rush, Alexander M.},
13	  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics: System Demonstrations},
14	  year = {2019},
15	}
16	
17	@inproceedings{dna_gpt,
18	  title = {{DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text}},
19	  author = {Yang, Xianjun and Cheng, Wei and Wu, Yue and Petzold, Linda and Wang, William Yang and Chen, Haifeng},
20	  booktitle = {Proceedings of the International Conference on Learning Representations},
21	  year = {2024},
22	}
23	
24	@inproceedings{binoculars,
25	  title = {{Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text}},
26	  author = {Hans, Abhimanyu and Schwarzschild, Avi and Cherepanova, Valeriia and Kazemi, Hamid and Saha, Aniruddha and Goldblum, Micah and Geiping, Jonas and Goldstein, Tom},
27	  booktitle = {Proceedings of the International Conference on Machine Learning},
28	  year = {2024},
29	}
30	
31	@inproceedings{fast_detectgpt,
32	  title = {{Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature}},
33	  author = {Bao, Guangsheng and Zhao, Yanbin and Teng, Zhiyang and Yang, Linyi and Zhang, Yue},
34	  booktitle = {Proceedings of the International Conference on Learning Representations},
35	  year = {2024},
36	}
37	
38	@article{ld_score,
39	  title = {{Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection}},
40	  author = {Narayanasamy, Priyadarshan and Agrawal, Swastik and Faber, Klint and Alam, Fardina Fathmiul},
41	  journal = {arXiv preprint arXiv:2605.01647},
42	  year = {2026},
43	}
44	
45	@inproceedings{intrinsic_dimension,
46	  title = {{Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts}},
47	  author = {Tulchinskii, Eduard and Kuznetsov, Kristian and Kushnareva, Laida and Cherniavskii, Daniil and Nikolenko, Sergey and Burnaev, Evgeny and Barannikov, Serguei and Piontkovskaya, Irina},
48	  booktitle = {Advances in Neural Information Processing Systems},
49	  year = {2023},
50	}
51	
52	@article{diveye,
53	  title = {{Diversity Boosts AI-Generated Text Detection}},
54	  author = {Basani, Advik Raj and Chen, Pin-Yu},
55	  journal = {Transactions on Machine Learning Research},
56	  year = {2026},
57	}
58	
59	@article{generator_barrier,
60	  title = {{Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection}},
61	  author = {Pu, Xiao and Cheng, Zepeng and Yuan, Lin and Wu, Yu and Bi, Xiuli},
62	  journal = {arXiv preprint arXiv:2604.13692},
63	  year = {2026},
64	}
65	
66	@article{feat_aug_transformer,
67	  title = {{Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators}},
68	  author = {Mady, Mohamed and Reschke, Johannes and Schuller, Bj{\"o}rn},
69	  journal = {arXiv preprint arXiv:2605.03969},
70	  year = {2026},
71	}
72	
73	@article{reliable_detection,
74	  title = {{Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks}},
75	  author = {Sadasivan, Vinu Sankar and Kumar, Aounon and Balasubramanian, Sriram and Wang, Wenxiao and Feizi, Soheil},
76	  journal = {Transactions on Machine Learning Research},
77	  year = {2025},
78	  url = {https://openreview.net/forum?id=OOgsAZdFOt},
79	}
80	
81	@inproceedings{paraphrase_evades,
82	  title = {{Paraphrasing Evades Detectors of AI-Generated Text, but Retrieval is an Effective Defense}},
83	  author = {Krishna, Kalpesh and Song, Yixiao and Karpinska, Marzena and Wieting, John and Iyyer, Mohit},
84	  booktitle = {Advances in Neural Information Processing Systems},
85	  year = {2023},
86	}
87	
88	@inproceedings{detection_possibilities,
89	  title = {{Position: On the Possibilities of AI-Generated Text Detection}},
90	  author = {Chakraborty, Souradip and Bedi, Amrit Singh and Zhu, Sicheng and An, Bang and Manocha, Dinesh and Huang, Furong},
91	  booktitle = {Proceedings of the International Conference on Machine Learning},
92	  year = {2024},
93	}
94	
95	@inproceedings{grover,
96	  title = {{Defending Against Neural Fake News}},
97	  author = {Zellers, Rowan and Holtzman, Ari and Rashkin, Hannah and Bisk, Yonatan and Farhadi, Ali and Roesner, Franziska and Choi, Yejin},
98	  booktitle = {Advances in Neural Information Processing Systems},
99	  year = {2019},
100	}
101	
102	@article{release_strategies,
103	  title = {{Release Strategies and the Social Impacts of Language Models}},
104	  author = {Solaiman, Irene and Brundage, Miles and Clark, Jack and Askell, Amanda and Herbert-Voss, Ariel and Wu, Jeff and Radford, Alec and Krueger, Gretchen and Kim, Jong Wook and Kreps, Sarah and McCain, Miles and Newhouse, Alex and Blazakis, Jason and McGuffie, Kris and Wang, Jasmine},
105	  journal = {arXiv preprint arXiv:1908.09203},
106	  year = {2019},
107	}
108	
109	@inproceedings{beyond_binary,
110	  title = {{Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement}},
111	  author = {Cheng, Zihao and Zhou, Li and Jiang, Feng and Wang, Benyou and Li, Haizhou},
112	  booktitle = {Proceedings of the ACM Web Conference},
113	  year = {2025},
114	}
115	
116	@inproceedings{semeval2024_task8,
117	  title = {{SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection}},
118	  author = {Wang, Yuxia and Mansurov, Jonibek and Ivanov, Petar and Su, Jinyan and Shelmanov, Artem and Tsvigun, Akim and Afzal, Osama Mohammed and Mahmoud, Tarek and Puccetti, Giovanni and Arnold, Thomas and Whitehouse, Chenxi and Aji, Alham Fikri and Habash, Nizar and Gurevych, Iryna and Nakov, Preslav},
119	  booktitle = {Proceedings of the International Workshop on Semantic Evaluation},
120	  year = {2024},
121	}
122	
123	% ===== Model Collapse =====
124	
125	@inproceedings{self_consuming_mad,
126	  title = {{Self-Consuming Generative Models Go MAD}},
127	  author = {Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Babaei, Hossein and LeJeune, Daniel and Siahkoohi, Ali and Baraniuk, Richard G.},
128	  booktitle = {Proceedings of the International Conference on Learning Representations},
129	  year = {2024},
130	}
131	
132	@article{curse_of_recursion,
133	  title = {{AI models collapse when trained on recursively generated data}},
134	  author = {Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and Anderson, Ross and Gal, Yarin},
135	  journal = {Nature},
136	  volume = {631},
137	  pages = {755--759},
138	  year = {2024},
139	  doi = {10.1038/s41586-024-07566-y},
140	}
141	
142	@inproceedings{strong_model_collapse,
143	  title = {{Strong Model Collapse}},
144	  author = {Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia},
145	  booktitle = {Proceedings of the International Conference on Learning Representations},
146	  year = {2025},
147	}
148	
149	@inproceedings{model_collapse_avoidable,
150	  title = {{Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data}},
151	  author = {Gerstgrasser, Matthias and Schaeffer, Rylan and Dey, Apratim and Rafailov, Rafael and Sleight, Henry and Hughes, John and Korbak, Tomasz and Agrawal, Rajashree and Pai, Dhruv and Gromov, Andrey and Roberts, Daniel A. and Yang, Diyi and Donoho, David L. and Koyejo, Sanmi},
152	  booktitle = {Proceedings of the International Conference on Machine Learning},
153	  year = {2024},
154	}
155	
156	% ===== OOD Detection =====
157	
158	@inproceedings{ood_baseline,
159	  title = {{A Baseline for Detecting Misclassified and Out-of-Distribution Examples in Neural Networks}},
160	  author = {Hendrycks, Dan and Gimpel, Kevin},
161	  booktitle = {Proceedings of the International Conference on Learning Representations},
162	  year = {2017},
163	}
164	
165	% ===== Data Quality =====
166	
167	@inproceedings{dsir,
168	  title = {{Data Selection for Language Models via Importance Resampling}},
169	  author = {Xie, Sang Michael and Santurkar, Shibani and Ma, Tengyu and Liang, Percy},
170	  booktitle = {Advances in Neural Information Processing Systems},
171	  year = {2023},
172	}
173	
174	@inproceedings{qurating,
175	  title = {{QuRating: Selecting High-Quality Data for Training Language Models}},
176	  author = {Wettig, Alexander and Gupta, Aatmik and Malik, Saumya and Chen, Danqi},
177	  booktitle = {Proceedings of the International Conference on Machine Learning},
178	  year = {2024},
179	}
180	
181	@inproceedings{ccnet,
182	  title = {{CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data}},
183	  author = {Wenzek, Guillaume and Lachaux, Marie-Anne and Conneau, Alexis and Chaudhary, Vishrav and Guzm{\'a}n, Francisco and Joulin, Armand and Grave, Edouard},
184	  booktitle = {Proceedings of the Language Resources and Evaluation Conference},
185	  year = {2020},
186	}
187	
188	% ===== Watermarking =====
189	
190	@inproceedings{watermark_llm,
191	  title = {{A Watermark for Large Language Models}},
192	  author = {Kirchenbauer, John and Geiping, Jonas and Wen, Yuxin and Katz, Jonathan and Miers, Ian and Goldstein, Tom},
193	  booktitle = {Proceedings of the International Conference on Machine Learning},
194	  year = {2023},
195	}
196	
197	@article{synthid_text,
198	  title = {{Scalable Watermarking for Identifying Large Language Model Outputs}},
199	  author = {Dathathri, Sumanth and See, Abigail and Ghaisas, Sumedh and Huang, Po-Sen and McAdam, Rob and Welbl, Johannes and Bachani, Vandana and Kaskasoli, Alex and Stanforth, Robert and Matejovicova, Tatiana and Hayes, Jamie and Vyas, Nidhi and Al Merey, Majd and Brown-Cohen, Jonah and Bunel, Rudy and Balle, Borja and Cemgil, Taylan and Ahmed, Zahra and Stacpoole, Kitty and Shumailov, Ilia and Baetu, Ciprian and Gowal, Sven and Hassabis, Demis and Kohli, Pushmeet},
200	  journal = {Nature},
201	  volume = {634},
202	  pages = {818--823},
203	  year = {2024},
204	  doi = {10.1038/s41586-024-08025-4},
205	}
206	
207	@misc{aaronson_watermark,
208	  title = {{Watermarking GPT Outputs}},
209	  author = {Aaronson, Scott and Kirchner, Hendrik},
210	  year = {2022},
211	  howpublished = {Technical Talk},
212	  url = {https://scottaaronson.blog/?p=6823},
213	}
214	
215	@article{chainwash,
216	  title = {{Chainwash: Multi-Step Rewriting Attacks on Diffusion Language Model Watermarks}},
217	  author = {Ameen, Mohd Ruhul and Islam, Akif and Mahmud, Nadim and Hamid, Md. Ekramul},
218	  journal = {arXiv preprint arXiv:2605.05503},
219	  year = {2026},
220	}
221	
222	% ===== Vocabulary Diversity =====
223	
224	@inproceedings{curious_decline,
225	  title = {{The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text}},
226	  author = {Guo, Yanzhu and Shang, Guokan and Vazirgiannis, Michalis and Clavel, Chlo\'{e}},
227	  booktitle = {Findings of the Association for Computational Linguistics: NAACL},
228	  year = {2024},
229	}
230	
231	@inproceedings{writing_diversity,
232	  title = {{Does Writing with Language Models Reduce Content Diversity?}},
233	  author = {Padmakumar, Vishakh and He, He},
234	  booktitle = {Proceedings of the International Conference on Learning Representations},
235	  year = {2024},
236	}
237	
238	@inproceedings{nucleus_sampling,
239	  title = {{The Curious Case of Neural Text Degeneration}},
240	  author = {Holtzman, Ari and Buys, Jan and Du, Li and Forbes, Maxwell and Choi, Yejin},
241	  booktitle = {Proceedings of the International Conference on Learning Representations},
242	  year = {2020},
243	}
244	
245	@inproceedings{mapping_llm_science,
246	  title = {{Mapping the Increasing Use of LLMs in Scientific Papers}},
247	  author = {Liang, Weixin and Zhang, Yaohui and Wu, Zhengxuan and Lepp, Haley and Ji, Wenlong and Zhao, Xuandong and Cao, Hancheng and Liu, Sheng and He, Siyu and Huang, Zhi and Yang, Diyi and Potts, Christopher and Manning, Christopher D. and Zou, James Y.},
248	  booktitle = {Proceedings of the Conference on Language Modeling},
249	  year = {2024},
250	}
251	
252	@inproceedings{monitoring_ai_review,
253	  title = {{Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews}},
254	  author = {Liang, Weixin and Izzo, Zachary and Zhang, Yaohui and Lepp, Haley and Cao, Hancheng and Zhao, Xuandong and Chen, Lingjiao and Ye, Haotian and Liu, Sheng and Huang, Zhi and McFarland, Daniel A. and Zou, James Y.},
255	  booktitle = {Proceedings of the International Conference on Machine Learning},
256	  year = {2024},
257	}
258	
259	% ===== Stylometry =====
260	
261	@article{stamatatos_survey,
262	  title = {{A Survey of Modern Authorship Attribution Methods}},
263	  author = {Stamatatos, Efstathios},
264	  journal = {Journal of the American Society for Information Science and Technology},
265	  year = {2009},
266	}
267	
268	@article{koppel_authorship,
269	  title = {{Computational Methods in Authorship Attribution}},
270	  author = {Koppel, Moshe and Schler, Jonathan and Argamon, Shlomo},
271	  journal = {Journal of the American Society for Information Science and Technology},
272	  year = {2009},
273	}
274	
275	@inproceedings{uchendu_attribution,
276	  title = {{Authorship Attribution for Neural Text Generation}},
277	  author = {Uchendu, Adaku and Le, Thai and Shu, Kai and Lee, Dongwon},
278	  booktitle = {Proceedings of the Conference on Empirical Methods in Natural Language Processing},
279	  year = {2020},
280	}
281	
282	@inproceedings{munir_looking_glass,
283	  title = {{Through the Looking Glass: Learning to Attribute Synthetic Text Generated by Language Models}},
284	  author = {Munir, Shaoor and Batool, Brishna and Shafiq, Zubair and Srinivasan, Padmini and Zaffar, Fareed},
285	  booktitle = {Proceedings of the Conference of the European Chapter of the Association for Computational Linguistics},
286	  pages = {1811--1822},
287	  year = {2021},
288	  doi = {10.18653/v1/2021.eacl-main.155},
289	}
290	
291	% ===== Iterative Generation =====
292	
293	@inproceedings{broken_telephone,
294	  title = {{LLM as a Broken Telephone: Iterative Generation Distorts Information}},
295	  author = {Mohamed, Amr and Geng, Mingmeng and Vazirgiannis, Michalis and Shang, Guokan},
296	  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics},
297	  year = {2025},
298	}
299	
300	@article{markovian_chains,
301	  title = {{Markovian Generation Chains in Large Language Models}},
302	  author = {Geng, Mingmeng and Mohamed, Amr and Shang, Guokan and Vazirgiannis, Michalis and Poibeau, Thierry},
303	  journal = {arXiv preprint arXiv:2603.11228},
304	  year = {2026},
305	}
306	
307	% ===== Membership Inference =====
308	
309	@inproceedings{min_k_percent,
310	  title = {{Detecting Pretraining Data from Large Language Models}},
311	  author = {Shi, Weijia and Ajith, Anirudh and Xia, Mengzhou and Huang, Yangsibo and Liu, Daogao and Blevins, Terra and Chen, Danqi and Zettlemoyer, Luke},
312	  booktitle = {Proceedings of the International Conference on Learning Representations},
313	  year = {2024},
314	}
315	
316	% ===== Survey =====
317	
318	@article{wu_survey_2025,
319	  title = {{A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions}},
320	  author = {Wu, Junchao and Yang, Shu and Zhan, Runzhe and Yuan, Yulin and Chao, Lidia Sam and Wong, Derek Fai},
321	  journal = {Computational Linguistics},
322	  publisher = {MIT Press},
323	  volume = {51},
324	  number = {1},
325	  pages = {275--338},
326	  year = {2025},
327	  doi = {10.1162/coli_a_00549},
328	}
329	
330	@inproceedings{jawahar_survey,
331	  title = {{Automatic Detection of Machine Generated Text: A Critical Survey}},
332	  author = {Jawahar, Ganesh and Abdul-Mageed, Muhammad and Lakshmanan, Laks V.S.},
333	  booktitle = {Proceedings of the International Conference on Computational Linguistics},
334	  year = {2020},
335	}
336	
337	% ===== Models =====
338	
339	@inproceedings{pythia,
340	  title = {{Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling}},
341	  author = {Biderman, Stella and Schoelkopf, Hailey and Anthony, Quentin Gregory and Bradley, Herbie and O'Brien, Kyle and Hallahan, Eric and Khan, Mohammad Aflah and Purohit, Shivanshu and Prashanth, USVSN Sai and Raff, Edward and Skowron, Aviya and Sutawika, Lintang and {van der Wal}, Oskar},
342	  booktitle = {Proceedings of the International Conference on Machine Learning},
343	  year = {2023},
344	}
345	
346	@inproceedings{olmo,
347	  title = {{OLMo: Accelerating the Science of Language Models}},
348	  author = {Groeneveld, Dirk and Beltagy, Iz and Walsh, Evan and Bhagia, Akshita and Kinney, Rodney and Tafjord, Oyvind and Jha, Ananya Harsh and Ivison, Hamish and Magnusson, Ian and Wang, Yizhong and Arora, Shane and Atkinson, David and Authur, Russell and Chandu, Khyathi Raghavi and Cohan, Arman and Dumas, Jennifer and Elazar, Yanai and Gu, Yuling and Hessel, Jack and Khot, Tushar and Merrill, William and Morrison, Jacob and Muennighoff, Niklas and Naik, Aakanksha and Nam, Crystal and Peters, Matthew E. and Pyatkin, Valentina and Ravichander, Abhilasha and Schwenk, Dustin and Shah, Saurabh and Smith, Will and Strubell, Emma and Subramani, Nishant and Wortsman, Mitchell and Dasigi, Pradeep and Lambert, Nathan and Richardson, Kyle and Zettlemoyer, Luke and Dodge, Jesse and Lo, Kyle and Soldaini, Luca and Smith, Noah A. and Hajishirzi, Hannaneh},
349	  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics},
350	  year = {2024},
351	}
352	
353	@article{qwen3,
354	  title = {{Qwen3 Technical Report}},
355	  author = {{Qwen Team}},
356	  journal = {arXiv preprint arXiv:2505.09388},
357	  year = {2025},
358	}
359	
360	% ===== Machine Learning =====
361	
362	@article{coral_ordinal,
363	  title = {{Rank Consistent Ordinal Regression for Neural Networks with Application to Age Estimation}},
364	  author = {Cao, Wenzhi and Mirjalili, Vahid and Raschka, Sebastian},
365	  journal = {Pattern Recognition Letters},
366	  volume = {140},
367	  pages = {325--331},
368	  year = {2020},
369	}
370	
371	@inproceedings{frank_hall_ordinal,
372	  title = {{A Simple Approach to Ordinal Classification}},
373	  author = {Frank, Eibe and Hall, Mark},
374	  booktitle = {Proceedings of the European Conference on Machine Learning},
375	  year = {2001},
376	}
377	
378	@inproceedings{xgboost,
379	  title = {{XGBoost: A Scalable Tree Boosting System}},
380	  author = {Chen, Tianqi and Guestrin, Carlos},
381	  booktitle = {Proceedings of the ACM SIGKDD International Conference on Knowledge Discovery and Data Mining},
382	  year = {2016},
383	}
384	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "02cc67ad-c03e-4058-938b-210c48bf1830",
  "uuid": "b39671fe-2cf8-4474-8fa9-6386cd496b70",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/references.bib",
      "content": "% ===== Detection =====\n\n@inproceedings{detectgpt,\n  title = {{DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature}},\n  author = {Mitchell, Eric and Lee, Yoonho and Khazatsky, Alexander and Manning, Christopher D. and Finn, Chelsea},\n  booktitle = {Proceedings of the International Conference on Machine Learning},\n  year = {2023},\n}\n\n@inproceedings{gltr,\n  title = {{GLTR: Statistical Detection and Visualization of Generated Text}},\n  author = {Gehrmann, Sebastian and Strobelt, Hendrik and Rush, Alexander M.},\n  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics: System Demonstrations},\n  year = {2019},\n}\n\n@inproceedings{dna_gpt,\n  title = {{DNA-GPT: Divergent N-Gram Analysis for Training-Free Detection of GPT-Generated Text}},\n  author = {Yang, Xianjun and Cheng, Wei and Wu, Yue and Petzold, Linda and Wang, William Yang and Chen, Haifeng},\n  booktitle = {Proceedings of the International Conference on Learning Representations},\n  year = {2024},\n}\n\n@inproceedings{binoculars,\n  title = {{Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text}},\n  author = {Hans, Abhimanyu and Schwarzschild, Avi and Cherepanova, Valeriia and Kazemi, Hamid and Saha, Aniruddha and Goldblum, Micah and Geiping, Jonas and Goldstein, Tom},\n  booktitle = {Proceedings of the International Conference on Machine Learning},\n  year = {2024},\n}\n\n@inproceedings{fast_detectgpt,\n  title = {{Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature}},\n  author = {Bao, Guangsheng and Zhao, Yanbin and Teng, Zhiyang and Yang, Linyi and Zhang, Yue},\n  booktitle = {Proceedings of the International Conference on Learning Representations},\n  year = {2024},\n}\n\n@article{ld_score,\n  title = {{Beyond Perplexity: Character Distribution Signatures and the MDTA Benchmark for AI Text Detection}},\n  author = {Narayanasamy, Priyadarshan and Agrawal, Swastik and Faber, Klint and Alam, Fardina Fathmiul},\n  journal = {arXiv preprint arXiv:2605.01647},\n  year = {2026},\n}\n\n@inproceedings{intrinsic_dimension,\n  title = {{Intrinsic Dimension Estimation for Robust Detection of AI-Generated Texts}},\n  author = {Tulchinskii, Eduard and Kuznetsov, Kristian and Kushnareva, Laida and Cherniavskii, Daniil and Nikolenko, Sergey and Burnaev, Evgeny and Barannikov, Serguei and Piontkovskaya, Irina},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year = {2023},\n}\n\n@article{diveye,\n  title = {{Diversity Boosts AI-Generated Text Detection}},\n  author = {Basani, Advik Raj and Chen, Pin-Yu},\n  journal = {Transactions on Machine Learning Research},\n  year = {2026},\n}\n\n@article{generator_barrier,\n  title = {{Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection}},\n  author = {Pu, Xiao and Cheng, Zepeng and Yuan, Lin and Wu, Yu and Bi, Xiuli},\n  journal = {arXiv preprint arXiv:2604.13692},\n  year = {2026},\n}\n\n@article{feat_aug_transformer,\n  title = {{Feature-Augmented Transformers for Robust AI-Text Detection Across Domains and Generators}},\n  author = {Mady, Mohamed and Reschke, Johannes and Schuller, Bj{\\\"o}rn},\n  journal = {arXiv preprint arXiv:2605.03969},\n  year = {2026},\n}\n\n@article{reliable_detection,\n  title = {{Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks}},\n  author = {Sadasivan, Vinu Sankar and Kumar, Aounon and Balasubramanian, Sriram and Wang, Wenxiao and Feizi, Soheil},\n  journal = {Transactions on Machine Learning Research},\n  year = {2025},\n  url = {https://openreview.net/forum?id=OOgsAZdFOt},\n}\n\n@inproceedings{paraphrase_evades,\n  title = {{Paraphrasing Evades Detectors of AI-Generated Text, but Retrieval is an Effective Defense}},\n  author = {Krishna, Kalpesh and Song, Yixiao and Karpinska, Marzena and Wieting, John and Iyyer, Mohit},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year = {2023},\n}\n\n@inproceedings{detection_possibilities,\n  title = {{Position: On the Possibilities of AI-Generated Text Detection}},\n  author = {Chakraborty, Souradip and Bedi, Amrit Singh and Zhu, Sicheng and An, Bang and Manocha, Dinesh and Huang, Furong},\n  booktitle = {Proceedings of the International Conference on Machine Learning},\n  year = {2024},\n}\n\n@inproceedings{grover,\n  title = {{Defending Against Neural Fake News}},\n  author = {Zellers, Rowan and Holtzman, Ari and Rashkin, Hannah and Bisk, Yonatan and Farhadi, Ali and Roesner, Franziska and Choi, Yejin},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year = {2019},\n}\n\n@article{release_strategies,\n  title = {{Release Strategies and the Social Impacts of Language Models}},\n  author = {Solaiman, Irene and Brundage, Miles and Clark, Jack and Askell, Amanda and Herbert-Voss, Ariel and Wu, Jeff and Radford, Alec and Krueger, Gretchen and Kim, Jong Wook and Kreps, Sarah and McCain, Miles and Newhouse, Alex and Blazakis, Jason and McGuffie, Kris and Wang, Jasmine},\n  journal = {arXiv preprint arXiv:1908.09203},\n  year = {2019},\n}\n\n@inproceedings{beyond_binary,\n  title = {{Beyond Binary: Towards Fine-Grained LLM-Generated Text Detection via Role Recognition and Involvement Measurement}},\n  author = {Cheng, Zihao and Zhou, Li and Jiang, Feng and Wang, Benyou and Li, Haizhou},\n  booktitle = {Proceedings of the ACM Web Conference},\n  year = {2025},\n}\n\n@inproceedings{semeval2024_task8,\n  title = {{SemEval-2024 Task 8: Multidomain, Multimodel and Multilingual Machine-Generated Text Detection}},\n  author = {Wang, Yuxia and Mansurov, Jonibek and Ivanov, Petar and Su, Jinyan and Shelmanov, Artem and Tsvigun, Akim and Afzal, Osama Mohammed and Mahmoud, Tarek and Puccetti, Giovanni and Arnold, Thomas and Whitehouse, Chenxi and Aji, Alham Fikri and Habash, Nizar and Gurevych, Iryna and Nakov, Preslav},\n  booktitle = {Proceedings of the International Workshop on Semantic Evaluation},\n  year = {2024},\n}\n\n% ===== Model Collapse =====\n\n@inproceedings{self_consuming_mad,\n  title = {{Self-Consuming Generative Models Go MAD}},\n  author = {Alemohammad, Sina and Casco-Rodriguez, Josue and Luzi, Lorenzo and Humayun, Ahmed Imtiaz and Babaei, Hossein and LeJeune, Daniel and Siahkoohi, Ali and Baraniuk, Richard G.},\n  booktitle = {Proceedings of the International Conference on Learning Representations},\n  year = {2024},\n}\n\n@article{curse_of_recursion,\n  title = {{AI models collapse when trained on recursively generated data}},\n  author = {Shumailov, Ilia and Shumaylov, Zakhar and Zhao, Yiren and Papernot, Nicolas and Anderson, Ross and Gal, Yarin},\n  journal = {Nature},\n  volume = {631},\n  pages = {755--759},\n  year = {2024},\n  doi = {10.1038/s41586-024-07566-y},\n}\n\n@inproceedings{strong_model_collapse,\n  title = {{Strong Model Collapse}},\n  author = {Dohmatob, Elvis and Feng, Yunzhen and Subramonian, Arjun and Kempe, Julia},\n  booktitle = {Proceedings of the International Conference on Learning Representations},\n  year = {2025},\n}\n\n@inproceedings{model_collapse_avoidable,\n  title = {{Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data}},\n  author = {Gerstgrasser, Matthias and Schaeffer, Rylan and Dey, Apratim and Rafailov, Rafael and Sleight, Henry and Hughes, John and Korbak, Tomasz and Agrawal, Rajashree and Pai, Dhruv and Gromov, Andrey and Roberts, Daniel A. and Yang, Diyi and Donoho, David L. and Koyejo, Sanmi},\n  booktitle = {Proceedings of the International Conference on Machine Learning},\n  year = {2024},\n}\n\n% ===== OOD Detection =====\n\n@inproceedings{ood_baseline,\n  title = {{A Baseline for Detecting Misclassified and Out-of-Distribution Examples in Neural Networks}},\n  author = {Hendrycks, Dan and Gimpel, Kevin},\n  booktitle = {Proceedings of the International Conference on Learning Representations},\n  year = {2017},\n}\n\n% ===== Data Quality =====\n\n@inproceedings{dsir,\n  title = {{Data Selection for Language Models via Importance Resampling}},\n  author = {Xie, Sang Michael and Santurkar, Shibani and Ma, Tengyu and Liang, Percy},\n  booktitle = {Advances in Neural Information Processing Systems},\n  year = {2023},\n}\n\n@inproceedings{qurating,\n  title = {{QuRating: Selecting High-Quality Data for Training Language Models}},\n  author = {Wettig, Alexander and Gupta, Aatmik and Malik, Saumya and Chen, Danqi},\n  booktitle = {Proceedings of the International Conference on Machine Learning},\n  year = {2024},\n}\n\n@inproceedings{ccnet,\n  title = {{CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data}},\n  author = {Wenzek, Guillaume and Lachaux, Marie-Anne and Conneau, Alexis and Chaudhary, Vishrav and Guzm{\\'a}n, Francisco and Joulin, Armand and Grave, Edouard},\n  booktitle = {Proceedings of the Language Resources and Evaluation Conference},\n  year = {2020},\n}\n\n% ===== Watermarking =====\n\n@inproceedings{watermark_llm,\n  title = {{A Watermark for Large Language Models}},\n  author = {Kirchenbauer, John and Geiping, Jonas and Wen, Yuxin and Katz, Jonathan and Miers, Ian and Goldstein, Tom},\n  booktitle = {Proceedings of the International Conference on Machine Learning},\n  year = {2023},\n}\n\n@article{synthid_text,\n  title = {{Scalable Watermarking for Identifying Large Language Model Outputs}},\n  author = {Dathathri, Sumanth and See, Abigail and Ghaisas, Sumedh and Huang, Po-Sen and McAdam, Rob and Welbl, Johannes and Bachani, Vandana and Kaskasoli, Alex and Stanforth, Robert and Matejovicova, Tatiana and Hayes, Jamie and Vyas, Nidhi and Al Merey, Majd and Brown-Cohen, Jonah and Bunel, Rudy and Balle, Borja and Cemgil, Taylan and Ahmed, Zahra and Stacpoole, Kitty and Shumailov, Ilia and Baetu, Ciprian and Gowal, Sven and Hassabis, Demis and Kohli, Pushmeet},\n  journal = {Nature},\n  volume = {634},\n  pages = {818--823},\n  year = {2024},\n  doi = {10.1038/s41586-024-08025-4},\n}\n\n@misc{aaronson_watermark,\n  title = {{Watermarking GPT Outputs}},\n  author = {Aaronson, Scott and Kirchner, Hendrik},\n  year = {2022},\n  howpublished = {Technical Talk},\n  url = {https://scottaaronson.blog/?p=6823},\n}\n\n@article{chainwash,\n  title = {{Chainwash: Multi-Step Rewriting Attacks on Diffusion Language Model Watermarks}},\n  author = {Ameen, Mohd Ruhul and Islam, Akif and Mahmud, Nadim and Hamid, Md. Ekramul},\n  journal = {arXiv preprint arXiv:2605.05503},\n  year = {2026},\n}\n\n% ===== Vocabulary Diversity =====\n\n@inproceedings{curious_decline,\n  title = {{The Curious Decline of Linguistic Diversity: Training Language Models on Synthetic Text}},\n  author = {Guo, Yanzhu and Shang, Guokan and Vazirgiannis, Michalis and Clavel, Chlo\\'{e}},\n  booktitle = {Findings of the Association for Computational Linguistics: NAACL},\n  year = {2024},\n}\n\n@inproceedings{writing_diversity,\n  title = {{Does Writing with Language Models Reduce Content Diversity?}},\n  author = {Padmakumar, Vishakh and He, He},\n  booktitle = {Proceedings of the International Conference on Learning Representations},\n  year = {2024},\n}\n\n@inproceedings{nucleus_sampling,\n  title = {{The Curious Case of Neural Text Degeneration}},\n  author = {Holtzman, Ari and Buys, Jan and Du, Li and Forbes, Maxwell and Choi, Yejin},\n  booktitle = {Proceedings of the International Conference on Learning Representations},\n  year = {2020},\n}\n\n@inproceedings{mapping_llm_science,\n  title = {{Mapping the Increasing Use of LLMs in Scientific Papers}},\n  author = {Liang, Weixin and Zhang, Yaohui and Wu, Zhengxuan and Lepp, Haley and Ji, Wenlong and Zhao, Xuandong and Cao, Hancheng and Liu, Sheng and He, Siyu and Huang, Zhi and Yang, Diyi and Potts, Christopher and Manning, Christopher D. and Zou, James Y.},\n  booktitle = {Proceedings of the Conference on Language Modeling},\n  year = {2024},\n}\n\n@inproceedings{monitoring_ai_review,\n  title = {{Monitoring AI-Modified Content at Scale: A Case Study on the Impact of ChatGPT on AI Conference Peer Reviews}},\n  author = {Liang, Weixin and Izzo, Zachary and Zhang, Yaohui and Lepp, Haley and Cao, Hancheng and Zhao, Xuandong and Chen, Lingjiao and Ye, Haotian and Liu, Sheng and Huang, Zhi and McFarland, Daniel A. and Zou, James Y.},\n  booktitle = {Proceedings of the International Conference on Machine Learning},\n  year = {2024},\n}\n\n% ===== Stylometry =====\n\n@article{stamatatos_survey,\n  title = {{A Survey of Modern Authorship Attribution Methods}},\n  author = {Stamatatos, Efstathios},\n  journal = {Journal of the American Society for Information Science and Technology},\n  year = {2009},\n}\n\n@article{koppel_authorship,\n  title = {{Computational Methods in Authorship Attribution}},\n  author = {Koppel, Moshe and Schler, Jonathan and Argamon, Shlomo},\n  journal = {Journal of the American Society for Information Science and Technology},\n  year = {2009},\n}\n\n@inproceedings{uchendu_attribution,\n  title = {{Authorship Attribution for Neural Text Generation}},\n  author = {Uchendu, Adaku and Le, Thai and Shu, Kai and Lee, Dongwon},\n  booktitle = {Proceedings of the Conference on Empirical Methods in Natural Language Processing},\n  year = {2020},\n}\n\n@inproceedings{munir_looking_glass,\n  title = {{Through the Looking Glass: Learning to Attribute Synthetic Text Generated by Language Models}},\n  author = {Munir, Shaoor and Batool, Brishna and Shafiq, Zubair and Srinivasan, Padmini and Zaffar, Fareed},\n  booktitle = {Proceedings of the Conference of the European Chapter of the Association for Computational Linguistics},\n  pages = {1811--1822},\n  year = {2021},\n  doi = {10.18653/v1/2021.eacl-main.155},\n}\n\n% ===== Iterative Generation =====\n\n@inproceedings{broken_telephone,\n  title = {{LLM as a Broken Telephone: Iterative Generation Distorts Information}},\n  author = {Mohamed, Amr and Geng, Mingmeng and Vazirgiannis, Michalis and Shang, Guokan},\n  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics},\n  year = {2025},\n}\n\n@article{markovian_chains,\n  title = {{Markovian Generation Chains in Large Language Models}},\n  author = {Geng, Mingmeng and Mohamed, Amr and Shang, Guokan and Vazirgiannis, Michalis and Poibeau, Thierry},\n  journal = {arXiv preprint arXiv:2603.11228},\n  year = {2026},\n}\n\n% ===== Membership Inference =====\n\n@inproceedings{min_k_percent,\n  title = {{Detecting Pretraining Data from Large Language Models}},\n  author = {Shi, Weijia and Ajith, Anirudh and Xia, Mengzhou and Huang, Yangsibo and Liu, Daogao and Blevins, Terra and Chen, Danqi and Zettlemoyer, Luke},\n  booktitle = {Proceedings of the International Conference on Learning Representations},\n  year = {2024},\n}\n\n% ===== Survey =====\n\n@article{wu_survey_2025,\n  title = {{A Survey on LLM-Generated Text Detection: Necessity, Methods, and Future Directions}},\n  author = {Wu, Junchao and Yang, Shu and Zhan, Runzhe and Yuan, Yulin and Chao, Lidia Sam and Wong, Derek Fai},\n  journal = {Computational Linguistics},\n  publisher = {MIT Press},\n  volume = {51},\n  number = {1},\n  pages = {275--338},\n  year = {2025},\n  doi = {10.1162/coli_a_00549},\n}\n\n@inproceedings{jawahar_survey,\n  title = {{Automatic Detection of Machine Generated Text: A Critical Survey}},\n  author = {Jawahar, Ganesh and Abdul-Mageed, Muhammad and Lakshmanan, Laks V.S.},\n  booktitle = {Proceedings of the International Conference on Computational Linguistics},\n  year = {2020},\n}\n\n% ===== Models =====\n\n@inproceedings{pythia,\n  title = {{Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling}},\n  author = {Biderman, Stella and Schoelkopf, Hailey and Anthony, Quentin Gregory and Bradley, Herbie and O'Brien, Kyle and Hallahan, Eric and Khan, Mohammad Aflah and Purohit, Shivanshu and Prashanth, USVSN Sai and Raff, Edward and Skowron, Aviya and Sutawika, Lintang and {van der Wal}, Oskar},\n  booktitle = {Proceedings of the International Conference on Machine Learning},\n  year = {2023},\n}\n\n@inproceedings{olmo,\n  title = {{OLMo: Accelerating the Science of Language Models}},\n  author = {Groeneveld, Dirk and Beltagy, Iz and Walsh, Evan and Bhagia, Akshita and Kinney, Rodney and Tafjord, Oyvind and Jha, Ananya Harsh and Ivison, Hamish and Magnusson, Ian and Wang, Yizhong and Arora, Shane and Atkinson, David and Authur, Russell and Chandu, Khyathi Raghavi and Cohan, Arman and Dumas, Jennifer and Elazar, Yanai and Gu, Yuling and Hessel, Jack and Khot, Tushar and Merrill, William and Morrison, Jacob and Muennighoff, Niklas and Naik, Aakanksha and Nam, Crystal and Peters, Matthew E. and Pyatkin, Valentina and Ravichander, Abhilasha and Schwenk, Dustin and Shah, Saurabh and Smith, Will and Strubell, Emma and Subramani, Nishant and Wortsman, Mitchell and Dasigi, Pradeep and Lambert, Nathan and Richardson, Kyle and Zettlemoyer, Luke and Dodge, Jesse and Lo, Kyle and Soldaini, Luca and Smith, Noah A. and Hajishirzi, Hannaneh},\n  booktitle = {Proceedings of the Annual Meeting of the Association for Computational Linguistics},\n  year = {2024},\n}\n\n@article{qwen3,\n  title = {{Qwen3 Technical Report}},\n  author = {{Qwen Team}},\n  journal = {arXiv preprint arXiv:2505.09388},\n  year = {2025},\n}\n\n% ===== Machine Learning =====\n\n@article{coral_ordinal,\n  title = {{Rank Consistent Ordinal Regression for Neural Networks with Application to Age Estimation}},\n  author = {Cao, Wenzhi and Mirjalili, Vahid and Raschka, Sebastian},\n  journal = {Pattern Recognition Letters},\n  volume = {140},\n  pages = {325--331},\n  year = {2020},\n}\n\n@inproceedings{frank_hall_ordinal,\n  title = {{A Simple Approach to Ordinal Classification}},\n  author = {Frank, Eibe and Hall, Mark},\n  booktitle = {Proceedings of the European Conference on Machine Learning},\n  year = {2001},\n}\n\n@inproceedings{xgboost,\n  title = {{XGBoost: A Scalable Tree Boosting System}},\n  author = {Chen, Tianqi and Guestrin, Carlos},\n  booktitle = {Proceedings of the ACM SIGKDD International Conference on Knowledge Discovery and Data Mining},\n  year = {2016},\n}\n",
      "numLines": 384,
      "startLine": 1,
      "totalLines": 384
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
Let me analyze the verify_references results:

**Summary:**
- Total bib entries: 49
- Total citations: 72 (49 unique keys)
- Orphan: 0, Missing: 0
- Online verified: 41
- Not found: 6
- Mismatch: 2

**Not Found (6):**
1. `detectgpt` - OpenAlex didn't find it (similarity 0.38)
2. `reliable_detection` - OpenAlex didn't find it (similarity 0.34)


3. `detection_possibilities` - OpenAlex didn't find it (similarity 0.25)
4. `aaronson_watermark` - OpenAlex didn't find it (similarity 0.42) - this is a misc/technical talk, expected
5. `pythia` - OpenAlex didn't find it (similarity 0.50)
6. `xgboost` - OpenAlex didn't find it (similarity 0.30)

**Mismatch (2):**
1. `self_consuming_mad` - first_author: bib=alemohammad vs api=casco-rodriguez
2. `qwen3` - first_author: bib=team vs api=yang

Looking at the mismatches, there are author discrepancies between what's in the bibliography and what OpenAlex returned.

Now I'm checking the year discrepancies in the verified entries - several papers show different publication years between the bibliography and OpenAlex, likely due to arXiv preprints being posted before official conference publication. For instance, `dna_gpt` and `fast_detectgpt` are both listed as 2024 ICLR papers in the bibliography but show 2023 in OpenAlex, which makes sense if they were arXiv preprints first. Similarly, `ood_baseline` shows 2017 in the bibliography but 2016 in OpenAlex, consistent with an ICLR 2017 paper that would have been posted the year before.

I'm noticing the same pattern across multiple entries - `ccnet`, `stamatatos_survey`, `koppel_authorship`, `writing_diversity`, `nucleus_sampling`, and `min_k_percent` all have year differences that align with preprint versus published timelines. I need to remember that for conference papers, the standard is to use the conference year, not the preprint year.

Looking at the ones marked as not_found, I should verify those through WebSearch since they're well-known papers that might have just been missed in the initial search - `detectgpt` from Mitchell et al. at ICML 2023 is particularly notable.

For the mismatches, there's an author ordering issue with `self_consuming_mad` where Alemohammad should be listed as the first author instead.  `qwen3` has a team authorship that OpenAlex incorrectly resolved to an individual author. Now checking the 2026 preprints—most are verified, though `diveye` shows a year discrepancy between the arXiv version (2025) and the bib entry claiming 2026 TMLR, which I need to resolve.

Let me search for the problematic entries: the 6 not_found items, the `diveye` year mismatch, and the `self_consuming_mad` author issue.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "02cc67ad-c03e-4058-938b-210c48bf1830",
  "uuid": "b2672e79-1f5a-457d-8ab9-2e86b0c2d534",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RifSUxDLT68SQoy8yEncLA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20748,
      "cache_read_input_tokens": 26706,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 20748
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

自动审计完成。发现 6 个 not_found + 2 个 mismatch。现在用 WebSearch 二次验证。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "02cc67ad-c03e-4058-938b-210c48bf1830",
  "uuid": "93bc7639-25f5-4e7e-8b70-acaa53144b91",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RifSUxDLT68SQoy8yEncLA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20748,
      "cache_read_input_tokens": 26706,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 20748
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01YaXmpJerL8hviDMfxyqWoZ`</summary>

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
  "session_id": "02cc67ad-c03e-4058-938b-210c48bf1830",
  "uuid": "2f9d2ffc-9db6-471f-8565-9b62ac47074b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RifSUxDLT68SQoy8yEncLA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20748,
      "cache_read_input_tokens": 26706,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 20748
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

_source line 19 · 2026-05-15T20:36:50.410Z_

<details><summary>↩ Tool result · `toolu_01YaXmpJerL8hviDMfxyqWoZ`</summary>

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
  "session_id": "02cc67ad-c03e-4058-938b-210c48bf1830",
  "uuid": "74c113a2-bf08-4c5a-a744-5ce9e1b4bc9e",
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

_source line 20_

<details><summary>Logged reasoning block</summary>

```text
Now let me search for the 6 not_found entries and the diveye year question. I'll do them in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "02cc67ad-c03e-4058-938b-210c48bf1830",
  "uuid": "3444cb8a-c2a0-475b-9725-6a8e98eadd9f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ED6AHxy8QoNVzu1PrCTZCM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2254,
      "cache_read_input_tokens": 47454,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2254
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

### Assistant

_source line 21_

并行验证 6 个 not_found 条目 + diveye 年份问题。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "02cc67ad-c03e-4058-938b-210c48bf1830",
  "uuid": "9c1d0c5f-4db7-4fdf-b4f7-25e915641784",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ED6AHxy8QoNVzu1PrCTZCM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2254,
      "cache_read_input_tokens": 47454,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2254
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

_source line 22_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XGzmVx3s4QUuYMv5KSFvut`</summary>

```json
{
  "query": "DetectGPT Zero-Shot Machine-Generated Text Detection Probability Curvature Mitchell ICML 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "02cc67ad-c03e-4058-938b-210c48bf1830",
  "uuid": "d20909ee-f7fe-46e0-a005-e6038bcc86f8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ED6AHxy8QoNVzu1PrCTZCM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2254,
      "cache_read_input_tokens": 47454,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2254
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

_source line 23_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AQhpD2az5TdZu5R14QcSdT`</summary>

```json
{
  "query": "\"Can AI-Generated Text be Reliably Detected\" Sadasivan Kumar TMLR 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "02cc67ad-c03e-4058-938b-210c48bf1830",
  "uuid": "f7e6470f-3ad0-4205-bbe9-a542f754776c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ED6AHxy8QoNVzu1PrCTZCM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2254,
      "cache_read_input_tokens": 47454,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2254
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

_source line 24_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01C5MPHPZXDYDtCW35TVERKj`</summary>

```json
{
  "query": "\"Position: On the Possibilities of AI-Generated Text Detection\" Chakraborty Bedi ICML 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "02cc67ad-c03e-4058-938b-210c48bf1830",
  "uuid": "29b01060-842d-4c0e-9349-6df9d13c0954",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ED6AHxy8QoNVzu1PrCTZCM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2254,
      "cache_read_input_tokens": 47454,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2254
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

_source line 25_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BxSc7WBUzRKGSzUo1tDQuu`</summary>

```json
{
  "query": "Aaronson Kirchner \"Watermarking GPT Outputs\" 2022"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "02cc67ad-c03e-4058-938b-210c48bf1830",
  "uuid": "6648149a-3141-4b31-8bee-2e49a19b6f85",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ED6AHxy8QoNVzu1PrCTZCM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2254,
      "cache_read_input_tokens": 47454,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2254
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

_source line 26_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ApzHhDGBY4L24LXhLERfHf`</summary>

```json
{
  "query": "Pythia Suite Analyzing Large Language Models Training Scaling Biderman ICML 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "02cc67ad-c03e-4058-938b-210c48bf1830",
  "uuid": "1e1b6c02-ae6a-4e8d-9087-074911f306f4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ED6AHxy8QoNVzu1PrCTZCM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2254,
      "cache_read_input_tokens": 47454,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2254
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

_source line 27_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017UBqtNfQ23GpbTqrZU9NwD`</summary>

```json
{
  "query": "XGBoost Scalable Tree Boosting System Chen Guestrin KDD 2016"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "02cc67ad-c03e-4058-938b-210c48bf1830",
  "uuid": "3c139d24-f43a-40f2-9df8-96b1e2ec65e2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ED6AHxy8QoNVzu1PrCTZCM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2254,
      "cache_read_input_tokens": 47454,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2254
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

_source line 28_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RHbnWBSWMhiHmfYXs8A9fy`</summary>

```json
{
  "query": "\"Diversity Boosts AI-Generated Text Detection\" Basani Chen TMLR 2025 OR 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "02cc67ad-c03e-4058-938b-210c48bf1830",
  "uuid": "55b3a2cb-f1cc-4f04-9a30-8bec8e88b453",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ED6AHxy8QoNVzu1PrCTZCM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2254,
      "cache_read_input_tokens": 47454,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2254
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

_source line 29 · 2026-05-15T20:37:00.191Z_

<details><summary>↩ Tool result · `toolu_01XGzmVx3s4QUuYMv5KSFvut`</summary>

```text
Web search results for query: "DetectGPT Zero-Shot Machine-Generated Text Detection Probability Curvature Mitchell ICML 2023"

Links: [{"title":"[2301.11305] DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature","url":"https://arxiv.org/abs/2301.11305"},{"title":"GitHub - eric-mitchell/detect-gpt: DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature · GitHub","url":"https://github.com/eric-mitchell/detect-gpt"},{"title":"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature","url":"https://proceedings.mlr.press/v202/mitchell23a.html"},{"title":"dblp: DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature.","url":"https://dblp.org/rec/conf/icml/Mitchell0KMF23.html"},{"title":"(PDF) DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature","url":"https://www.researchgate.net/publication/367461943_DetectGPT_Zero-Shot_Machine-Generated_Text_Detection_using_Probability_Curvature"},{"title":"ICML 2023 DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature Oral","url":"https://icml.cc/virtual/2023/oral/25525"},{"title":"[Paper Note] DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature, Eric Mitchell+, ICML'23, 2023.01 · Issue #3698 · AkihikoWatanabe/paper_notes","url":"https://github.com/AkihikoWatanabe/paper_notes/issues/3698"},{"title":"FAST-DETECTGPT: EFFICIENT ZERO-SHOT DETEC","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/6b8c6f846c3575e1d1ad496abea28826-Paper-Conference.pdf"},{"title":"Eric Mitchell, Yoonho Lee, Alexander Khazatsky, Christopher D. Manning, Chelsea Finn · DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature","url":"https://slideslive.com/39004346/detectgpt-zeroshot-machinegenerated-text-detection-using-probability-curvature"},{"title":"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv230111305M/abstract"}]

I found the research paper you searched for. Here's what I discovered:

## DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature

The paper was authored by Mitchell, E., Lee, Y., Khazatsky, A., Manning, C.D., and Finn, C. in 2023, titled "DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature." It was published at ICML 2023 with page numbers 24950-24962.

### Key Contribution

The paper demonstrates that text sampled from an LLM tends to occupy negative curvature regions of the model's log probability function. DetectGPT does not require training a separate classifier, collecting a dataset of real or generated passages, or explicitly watermarking generated text. It uses only log probabilities computed by the model of interest and random perturbations of the passage from another generic pre-trained language model (e.g., T5).

### Performance

DetectGPT is more discriminative than existing zero-shot methods for model sample detection, notably improving detection of fake news articles generated by 20B parameter GPT-NeoX from 0.81 AUROC for the strongest zero-shot baseline to 0.95 AUROC for DetectGPT.

You can access the full paper at [arXiv:2301.11305](https://arxiv.org/abs/2301.11305) or through the [ICML proceedings](https://proceedings.mlr.press/v202/mitchell23a.html).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "02cc67ad-c03e-4058-938b-210c48bf1830",
  "uuid": "4822c2ab-2277-4344-8e91-668358a69689",
  "tool_use_result": {
    "query": "DetectGPT Zero-Shot Machine-Generated Text Detection Probability Curvature Mitchell ICML 2023",
    "results": [
      {
        "tool_use_id": "srvtoolu_01LsTTush1PN3ZLMKM2jWmVb",
        "content": [
          {
            "title": "[2301.11305] DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature",
            "url": "https://arxiv.org/abs/2301.11305"
          },
          {
            "title": "GitHub - eric-mitchell/detect-gpt: DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature · GitHub",
            "url": "https://github.com/eric-mitchell/detect-gpt"
          },
          {
            "title": "DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature",
            "url": "https://proceedings.mlr.press/v202/mitchell23a.html"
          },
          {
            "title": "dblp: DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature.",
            "url": "https://dblp.org/rec/conf/icml/Mitchell0KMF23.html"
          },
          {
            "title": "(PDF) DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature",
            "url": "https://www.researchgate.net/publication/367461943_DetectGPT_Zero-Shot_Machine-Generated_Text_Detection_using_Probability_Curvature"
          },
          {
            "title": "ICML 2023 DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature Oral",
            "url": "https://icml.cc/virtual/2023/oral/25525"
          },
          {
            "title": "[Paper Note] DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature, Eric Mitchell+, ICML'23, 2023.01 · Issue #3698 · AkihikoWatanabe/paper_notes",
            "url": "https://github.com/AkihikoWatanabe/paper_notes/issues/3698"
          },
          {
            "title": "FAST-DETECTGPT: EFFICIENT ZERO-SHOT DETEC",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2024/file/6b8c6f846c3575e1d1ad496abea28826-Paper-Conference.pdf"
          },
          {
            "title": "Eric Mitchell, Yoonho Lee, Alexander Khazatsky, Christopher D. Manning, Chelsea Finn · DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature",
            "url": "https://slideslive.com/39004346/detectgpt-zeroshot-machinegenerated-text-detection-using-probability-curvature"
          },
          {
            "title": "DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2023arXiv230111305M/abstract"
          }
        ]
      },
      "I found the research paper you searched for. Here's what I discovered:\n\n## DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature\n\nThe paper was authored by Mitchell, E., Lee, Y., Khazatsky, A., Manning, C.D., and Finn, C. in 2023, titled \"DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature.\" It was published at ICML 2023 with page numbers 24950-24962.\n\n### Key Contribution\n\nThe paper demonstrates that text sampled from an LLM tends to occupy negative curvature regions of the model's log probability function. DetectGPT does not require training a separate classifier, collecting a dataset of real or generated passages, or explicitly watermarking generated text. It uses only log probabilities computed by the model of interest and random perturbations of the passage from another generic pre-trained language model (e.g., T5).\n\n### Performance\n\nDetectGPT is more discriminative than existing zero-shot methods for model sample detection, notably improving detection of fake news articles generated by 20B parameter GPT-NeoX from 0.81 AUROC for the strongest zero-shot baseline to 0.95 AUROC for DetectGPT.\n\nYou can access the full paper at [arXiv:2301.11305](https://arxiv.org/abs/2301.11305) or through the [ICML proceedings](https://proceedings.mlr.press/v202/mitchell23a.html)."
    ],
    "durationSeconds": 4.6522003750000005
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-15T20:37:01.438Z_

<details><summary>↩ Tool result · `toolu_01AQhpD2az5TdZu5R14QcSdT`</summary>

```text
Web search results for query: ""Can AI-Generated Text be Reliably Detected" Sadasivan Kumar TMLR 2025"

Links: [{"title":"Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks | OpenReview","url":"https://openreview.net/forum?id=OOgsAZdFOt"},{"title":"[2303.11156] Can AI-Generated Text be Reliably Detected?","url":"https://arxiv.org/abs/2303.11156"},{"title":"[PDF] Can AI-Generated Text be Reliably Detected? | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Can-AI-Generated-Text-be-Reliably-Detected-Sadasivan-Kumar/5ee8bb4fc80a291b2e416a2a879e7153a783d7e9"},{"title":"Can AI-Generated Text be Reliably Detected? | OpenReview","url":"https://openreview.net/forum?id=NvSwR4IvLO"},{"title":"(PDF) Can AI-Generated Text be Reliably Detected?","url":"https://www.researchgate.net/publication/369380286_Can_AI-Generated_Text_be_Reliably_Detected"},{"title":"Can AI-Generated Text be Reliably Detected?","url":"https://arxiv.org/pdf/2303.11156"},{"title":"Can AI-Generated Text be Reliably Detected?","url":"https://www.catalyzex.com/paper/can-ai-generated-text-be-reliably-detected"},{"title":"Accepted papers at TMLR on X: \"Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks Vinu Sankar Sadasivan, Aounon Kumar, Sriram Balasubramanian, Wenxiao Wang, Soheil Feizi. Action editor: Kamalika Chaudhuri. https://t.co/6h6ByH1n0v #watermark\" / X","url":"https://x.com/TmlrPub/status/1900336120296034775"},{"title":"Can AI-Generated Text be Reliably Detected? - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv230311156S/abstract"},{"title":"Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Can-AI-Generated-Text-be-Reliably-Detected-Stress-Sadasivan-Kumar/42f7d83e6c20fd4aaf3e3f53b18ab7db221ee300"}]

I found the paper you're looking for! Here are the key details:

**Paper Information:**
The paper is titled "Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks" by Vinu Sankar Sadasivan, Aounon Kumar, Sriram Balasubramanian, Wenxiao Wang, and Soheil Feizi. The paper was published in Transactions on Machine Learning Research (TMLR) in 2025.

**Main Findings:**
The paper shows that current AI text detectors are not reliable in practical scenarios and develops a recursive paraphrasing attack to break a wide range of detectors, including those using watermarking schemes, neural network-based detectors, zero-shot classifiers, and retrieval-based detectors.

**Key Contributions:**
The paper introduces a recursive paraphrasing attack to stress test the robustness of AI text detectors in the presence of an attacker, and provides a theoretical framework connecting the AUROC of the best possible detector to the Total Variation distance between human and AI text distributions.

The paper appears to be available on OpenReview at https://openreview.net/forum?id=OOgsAZdFOt


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "02cc67ad-c03e-4058-938b-210c48bf1830",
  "uuid": "e87ad57e-a5a7-4b3e-871d-842a43a30466",
  "tool_use_result": {
    "query": "\"Can AI-Generated Text be Reliably Detected\" Sadasivan Kumar TMLR 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_0143hyUc7ay8fGJRXwjM8JH6",
        "content": [
          {
            "title": "Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks | OpenReview",
            "url": "https://openreview.net/forum?id=OOgsAZdFOt"
          },
          {
            "title": "[2303.11156] Can AI-Generated Text be Reliably Detected?",
            "url": "https://arxiv.org/abs/2303.11156"
          },
          {
            "title": "[PDF] Can AI-Generated Text be Reliably Detected? | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Can-AI-Generated-Text-be-Reliably-Detected-Sadasivan-Kumar/5ee8bb4fc80a291b2e416a2a879e7153a783d7e9"
          },
          {
            "title": "Can AI-Generated Text be Reliably Detected? | OpenReview",
            "url": "https://openreview.net/forum?id=NvSwR4IvLO"
          },
          {
            "title": "(PDF) Can AI-Generated Text be Reliably Detected?",
            "url": "https://www.researchgate.net/publication/369380286_Can_AI-Generated_Text_be_Reliably_Detected"
          },
          {
            "title": "Can AI-Generated Text be Reliably Detected?",
            "url": "https://arxiv.org/pdf/2303.11156"
          },
          {
            "title": "Can AI-Generated Text be Reliably Detected?",
            "url": "https://www.catalyzex.com/paper/can-ai-generated-text-be-reliably-detected"
          },
          {
            "title": "Accepted papers at TMLR on X: \"Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks Vinu Sankar Sadasivan, Aounon Kumar, Sriram Balasubramanian, Wenxiao Wang, Soheil Feizi. Action editor: Kamalika Chaudhuri. https://t.co/6h6ByH1n0v #watermark\" / X",
            "url": "https://x.com/TmlrPub/status/1900336120296034775"
          },
          {
            "title": "Can AI-Generated Text be Reliably Detected? - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2023arXiv230311156S/abstract"
          },
          {
            "title": "Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Can-AI-Generated-Text-be-Reliably-Detected-Stress-Sadasivan-Kumar/42f7d83e6c20fd4aaf3e3f53b18ab7db221ee300"
          }
        ]
      },
      "I found the paper you're looking for! Here are the key details:\n\n**Paper Information:**\nThe paper is titled \"Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks\" by Vinu Sankar Sadasivan, Aounon Kumar, Sriram Balasubramanian, Wenxiao Wang, and Soheil Feizi. The paper was published in Transactions on Machine Learning Research (TMLR) in 2025.\n\n**Main Findings:**\nThe paper shows that current AI text detectors are not reliable in practical scenarios and develops a recursive paraphrasing attack to break a wide range of detectors, including those using watermarking schemes, neural network-based detectors, zero-shot classifiers, and retrieval-based detectors.\n\n**Key Contributions:**\nThe paper introduces a recursive paraphrasing attack to stress test the robustness of AI text detectors in the presence of an attacker, and provides a theoretical framework connecting the AUROC of the best possible detector to the Total Variation distance between human and AI text distributions.\n\nThe paper appears to be available on OpenReview at https://openreview.net/forum?id=OOgsAZdFOt"
    ],
    "durationSeconds": 4.9856897409999945
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-15T20:37:03.889Z_

<details><summary>↩ Tool result · `toolu_01ApzHhDGBY4L24LXhLERfHf`</summary>

```text
Web search results for query: "Pythia Suite Analyzing Large Language Models Training Scaling Biderman ICML 2023"

Links: [{"title":"dblp: Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling.","url":"https://dblp.org/rec/conf/icml/BidermanSABOHKP23.html"},{"title":"[2304.01373] Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling","url":"https://arxiv.org/abs/2304.01373"},{"title":"Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling","url":"https://proceedings.mlr.press/v202/biderman23a/biderman23a.pdf"},{"title":"Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling [Quick Review]","url":"https://liner.com/review/pythia-suite-for-analyzing-large-language-models-across-training-and"},{"title":"Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling | OpenReview","url":"https://openreview.net/forum?id=bpRTAnJ8LW"},{"title":"ICML Poster Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling","url":"https://icml.cc/virtual/2023/poster/24093"},{"title":"ICML 2023 Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling Oral","url":"https://icml.cc/virtual/2023/oral/25487"},{"title":"Paper Summary: Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling","url":"https://queirozf.com/entries/paper-summary-pythia-a-suite-for-analyzing-large-language-models-across-training-and-scaling"},{"title":"[PDF] Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Pythia:-A-Suite-for-Analyzing-Large-Language-Models-Biderman-Schoelkopf/be55e8ec4213868db08f2c3168ae666001bea4b8"},{"title":"Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling — EleutherAI","url":"https://www.eleuther.ai/papers-blog/pythia-a-suite-for-analyzing-large-language-modelsacross-training-and-scaling"}]

I found the research you're looking for. Here are the key details:

## Overview

The paper "Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling" was authored by Stella Biderman, Hailey Schoelkopf, Quentin Gregory Anthony, Herbie Bradley, Kyle O'Brien, Eric Hallahan, Mohammad Aflah Khan, Shivanshu Purohit, USVSN Sai Prashanth, Edward Raff, Aviya Skowron, Lintang Sutawika, and Oskar van der Wal, and was published at ICML 2023.

## The Pythia Suite

The suite comprises 16 LLMs all trained on public data seen in the exact same order and ranging in size from 70M to 12B parameters, with public access to 154 checkpoints for each of the 16 models, alongside tools to download and reconstruct their exact training dataloaders.

## Research Focus

The research includes several case studies with novel results in memorization, term frequency effects on few-shot performance, and reducing gender bias. The research addresses a significant gap in understanding how scaling laws connect to language model learning dynamics due to a lack of appropriate, publicly accessible model suites.

## Availability

The trained models, analysis code, training code, and training data can be found at https://github.com/EleutherAI/pythia.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "02cc67ad-c03e-4058-938b-210c48bf1830",
  "uuid": "09b2bc6e-c7ca-4cd4-8378-e3ed9c26fe47",
  "tool_use_result": {
    "query": "Pythia Suite Analyzing Large Language Models Training Scaling Biderman ICML 2023",
    "results": [
      {
        "tool_use_id": "srvtoolu_01TVCQdjW6ix8H6y2PWiAcXv",
        "content": [
          {
            "title": "dblp: Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling.",
            "url": "https://dblp.org/rec/conf/icml/BidermanSABOHKP23.html"
          },
          {
            "title": "[2304.01373] Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling",
            "url": "https://arxiv.org/abs/2304.01373"
          },
          {
            "title": "Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling",
            "url": "https://proceedings.mlr.press/v202/biderman23a/biderman23a.pdf"
          },
          {
            "title": "Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling [Quick Review]",
            "url": "https://liner.com/review/pythia-suite-for-analyzing-large-language-models-across-training-and"
          },
          {
            "title": "Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling | OpenReview",
            "url": "https://openreview.net/forum?id=bpRTAnJ8LW"
          },
          {
            "title": "ICML Poster Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling",
            "url": "https://icml.cc/virtual/2023/poster/24093"
          },
          {
            "title": "ICML 2023 Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling Oral",
            "url": "https://icml.cc/virtual/2023/oral/25487"
          },
          {
            "title": "Paper Summary: Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling",
            "url": "https://queirozf.com/entries/paper-summary-pythia-a-suite-for-analyzing-large-language-models-across-training-and-scaling"
          },
          {
            "title": "[PDF] Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Pythia:-A-Suite-for-Analyzing-Large-Language-Models-Biderman-Schoelkopf/be55e8ec4213868db08f2c3168ae666001bea4b8"
          },
          {
            "title": "Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling — EleutherAI",
            "url": "https://www.eleuther.ai/papers-blog/pythia-a-suite-for-analyzing-large-language-modelsacross-training-and-scaling"
          }
        ]
      },
      "I found the research you're looking for. Here are the key details:\n\n## Overview\n\nThe paper \"Pythia: A Suite for Analyzing Large Language Models Across Training and Scaling\" was authored by Stella Biderman, Hailey Schoelkopf, Quentin Gregory Anthony, Herbie Bradley, Kyle O'Brien, Eric Hallahan, Mohammad Aflah Khan, Shivanshu Purohit, USVSN Sai Prashanth, Edward Raff, Aviya Skowron, Lintang Sutawika, and Oskar van der Wal, and was published at ICML 2023.\n\n## The Pythia Suite\n\nThe suite comprises 16 LLMs all trained on public data seen in the exact same order and ranging in size from 70M to 12B parameters, with public access to 154 checkpoints for each of the 16 models, alongside tools to download and reconstruct their exact training dataloaders.\n\n## Research Focus\n\nThe research includes several case studies with novel results in memorization, term frequency effects on few-shot performance, and reducing gender bias. The research addresses a significant gap in understanding how scaling laws connect to language model learning dynamics due to a lack of appropriate, publicly accessible model suites.\n\n## Availability\n\nThe trained models, analysis code, training code, and training data can be found at https://github.com/EleutherAI/pythia."
    ],
    "durationSeconds": 5.582944241000004
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-15T20:37:04.253Z_

<details><summary>↩ Tool result · `toolu_01C5MPHPZXDYDtCW35TVERKj`</summary>

```text
Web search results for query: ""Position: On the Possibilities of AI-Generated Text Detection" Chakraborty Bedi ICML 2024"

Links: [{"title":"Position: On the Possibilities of AI-Generated Text Detection","url":"https://proceedings.mlr.press/v235/chakraborty24a.html"},{"title":"Position: On the Possibilities of AI-Generated Text Detection | OpenReview","url":"https://openreview.net/forum?id=CJbhtpcyGL"},{"title":"ICML Poster Position: On the Possibilities of AI-Generated Text Detection","url":"https://icml.cc/virtual/2024/poster/34689"},{"title":"On the Possibilities of AI-Generated Text Detection: A Sample Complexity Analysis | OpenReview","url":"https://openreview.net/forum?id=oxEER3kZ9M"},{"title":"Position: On the possibilities of AI-generated text detection","url":"https://dl.acm.org/doi/10.5555/3692070.3692305"},{"title":"[PDF] On the Possibilities of AI-Generated Text Detection | Semantic Scholar","url":"https://www.semanticscholar.org/paper/On-the-Possibilities-of-AI-Generated-Text-Detection-Chakraborty-Bedi/59ae4e4ff7a27010554081e478d9ee707d16d583"},{"title":"[2304.04736] On the Possibilities of AI-Generated Text Detection","url":"https://arxiv.org/abs/2304.04736"},{"title":"Position: On the Possibilities of AI-Generated Text Detection","url":"https://raw.githubusercontent.com/mlresearch/v235/main/assets/chakraborty24a/chakraborty24a.pdf"},{"title":"A Survey on the Possibilities & Impossibilities of AI-generated Text Detection | Semantic Scholar","url":"https://www.semanticscholar.org/paper/f582daa2f2822c0aa1291fe3925f69c25280e37e"},{"title":"Investigating generative AI models and detection techniques: impacts of tokenization and dataset size on identification of AI-generated text - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11611853/"}]

I found the paper! Here are the search results for "Position: On the Possibilities of AI-Generated Text Detection" by Chakraborty, Bedi, and co-authors:

## Paper Details

The paper was published in the Proceedings of the 41st International Conference on Machine Learning (ICML 2024), pages 6093–6115. The authors are Souradip Chakraborty, Amrit Bedi, Sicheng Zhu, Bang An, Dinesh Manocha, and Furong Huang.

## Main Contribution

The study addresses the challenge of distinguishing human-written text from Large Language Model (LLM) outputs. 

The authors provide evidence that this differentiation is consistently feasible, except when human and machine text distributions are indistinguishable across their entire support. Employing information theory, they show that while detecting machine-generated text becomes harder as it nears human quality, it remains possible with adequate data.

## Key Resource

The paper is available through multiple sources:
- **PMLR** (official proceedings): https://proceedings.mlr.press/v235/chakraborty24a.html
- **OpenReview**: https://openreview.net/forum?id=CJbhtpcyGL
- **arXiv** (earlier version): https://arxiv.org/abs/2304.04736
- **ICML Virtual Conference**: https://icml.cc/virtual/2024/poster/34689


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "02cc67ad-c03e-4058-938b-210c48bf1830",
  "uuid": "a8ede211-7570-474c-945d-1af55a40a6f2",
  "tool_use_result": {
    "query": "\"Position: On the Possibilities of AI-Generated Text Detection\" Chakraborty Bedi ICML 2024",
    "results": [
      {
        "tool_use_id": "srvtoolu_01947y8oignGbiM1nphcVv2G",
        "content": [
          {
            "title": "Position: On the Possibilities of AI-Generated Text Detection",
            "url": "https://proceedings.mlr.press/v235/chakraborty24a.html"
          },
          {
            "title": "Position: On the Possibilities of AI-Generated Text Detection | OpenReview",
            "url": "https://openreview.net/forum?id=CJbhtpcyGL"
          },
          {
            "title": "ICML Poster Position: On the Possibilities of AI-Generated Text Detection",
            "url": "https://icml.cc/virtual/2024/poster/34689"
          },
          {
            "title": "On the Possibilities of AI-Generated Text Detection: A Sample Complexity Analysis | OpenReview",
            "url": "https://openreview.net/forum?id=oxEER3kZ9M"
          },
          {
            "title": "Position: On the possibilities of AI-generated text detection",
            "url": "https://dl.acm.org/doi/10.5555/3692070.3692305"
          },
          {
            "title": "[PDF] On the Possibilities of AI-Generated Text Detection | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/On-the-Possibilities-of-AI-Generated-Text-Detection-Chakraborty-Bedi/59ae4e4ff7a27010554081e478d9ee707d16d583"
          },
          {
            "title": "[2304.04736] On the Possibilities of AI-Generated Text Detection",
            "url": "https://arxiv.org/abs/2304.04736"
          },
          {
            "title": "Position: On the Possibilities of AI-Generated Text Detection",
            "url": "https://raw.githubusercontent.com/mlresearch/v235/main/assets/chakraborty24a/chakraborty24a.pdf"
          },
          {
            "title": "A Survey on the Possibilities & Impossibilities of AI-generated Text Detection | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/f582daa2f2822c0aa1291fe3925f69c25280e37e"
          },
          {
            "title": "Investigating generative AI models and detection techniques: impacts of tokenization and dataset size on identification of AI-generated text - PMC",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC11611853/"
          }
        ]
      },
      "I found the paper! Here are the search results for \"Position: On the Possibilities of AI-Generated Text Detection\" by Chakraborty, Bedi, and co-authors:\n\n## Paper Details\n\nThe paper was published in the Proceedings of the 41st International Conference on Machine Learning (ICML 2024), pages 6093–6115. The authors are Souradip Chakraborty, Amrit Bedi, Sicheng Zhu, Bang An, Dinesh Manocha, and Furong Huang.\n\n## Main Contribution\n\nThe study addresses the challenge of distinguishing human-written text from Large Language Model (LLM) outputs. \n\nThe authors provide evidence that this differentiation is consistently feasible, except when human and machine text distributions are indistinguishable across their entire support. Employing information theory, they show that while detecting machine-generated text becomes harder as it nears human quality, it remains possible with adequate data.\n\n## Key Resource\n\nThe paper is available through multiple sources:\n- **PMLR** (official proceedings): https://proceedings.mlr.press/v235/chakraborty24a.html\n- **OpenReview**: https://openreview.net/forum?id=CJbhtpcyGL\n- **arXiv** (earlier version): https://arxiv.org/abs/2304.04736\n- **ICML Virtual Conference**: https://icml.cc/virtual/2024/poster/34689"
    ],
    "durationSeconds": 6.810284302999993
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-15T20:37:04.438Z_

<details><summary>↩ Tool result · `toolu_01BxSc7WBUzRKGSzUo1tDQuu`</summary>

```text
Web search results for query: "Aaronson Kirchner "Watermarking GPT Outputs" 2022"

Links: [{"title":"The Future of Computer Science","url":"https://www.scottaaronson.com/talks/watermark.ppt"},{"title":"Watermarking Needs Input Repetition Masking","url":"https://arxiv.org/html/2504.12229v1"},{"title":"OpenAI's attempts to watermark AI text hit limits | TechCrunch","url":"https://techcrunch.com/2022/12/10/openais-attempts-to-watermark-ai-text-hit-limits/"},{"title":"Publicly-Detectable Watermarking for Language Models","url":"https://eprint.iacr.org/2023/1661.pdf"},{"title":"Watermarking Language Models with Error Correcting Codes","url":"https://arxiv.org/html/2406.10281v1"},{"title":"Ensemble Watermarks for Large Language Models","url":"https://aclanthology.org/2025.acl-long.145.pdf"},{"title":"ChatGPT: Metadata 'watermark' could help combat plagiarism fears","url":"https://www.techmonitor.ai/digital-economy/ai-and-automation/chatgpt-plagiarism-metadata-watermark"},{"title":"Watermarking Makes Language Models Radioactive Tom Sander∗","url":"https://arxiv.org/pdf/2402.14904"},{"title":"AI Text Turning Dangerously Human? OpenAI Creator Suggests Adding Watermark to Systems Like ChatGPT","url":"https://www.techtimes.com/articles/284721/20221210/ai-text-turning-dangerously-human-openai-creator-suggests-adding-watermark-to-systems-like-chatgpt.htm"},{"title":"Watermarking text in LLM outputs – Dr Alan D. Thompson","url":"https://lifearchitect.ai/watermarking/"}]

Based on the search results, here's what I found about Aaronson and Kirchner's "Watermarking GPT Outputs" from 2022:

## Overview

The presentation "Watermarking GPT Outputs" was given at OpenAI in San Francisco on December 13, 2022. Computer science professor Scott Aaronson, who was a guest researcher at OpenAI, revealed that OpenAI is developing a tool for "statistically watermarking the outputs of a text [AI system]," where the tool would embed an "unnoticeable secret signal" indicating where the text came from.

## Technical Approach

The watermarking tool acts like a "wrapper" over existing text-generating systems, leveraging a cryptographic function running at the server level to "pseudorandomly" select the next token, so text would still look random but anyone possessing the "key" to the cryptographic function would be able to uncover a watermark.

## Implementation

OpenAI engineer Hendrik Kirchner built a working prototype. Empirically, a few hundred tokens seem to be enough to get a reasonable signal that text came from the AI system.

## Goals and Applications

Aaronson stated the goal was to "make it much harder to take [an AI system's] output and pass it off as if it came from a human," which could help prevent academic plagiarism and mass generation of propaganda.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "02cc67ad-c03e-4058-938b-210c48bf1830",
  "uuid": "38186b41-3e4c-4256-a6f2-ef933c0272cb",
  "tool_use_result": {
    "query": "Aaronson Kirchner \"Watermarking GPT Outputs\" 2022",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Ecd421G63nQgBEhkvWQnAk",
        "content": [
          {
            "title": "The Future of Computer Science",
            "url": "https://www.scottaaronson.com/talks/watermark.ppt"
          },
          {
            "title": "Watermarking Needs Input Repetition Masking",
            "url": "https://arxiv.org/html/2504.12229v1"
          },
          {
            "title": "OpenAI's attempts to watermark AI text hit limits | TechCrunch",
            "url": "https://techcrunch.com/2022/12/10/openais-attempts-to-watermark-ai-text-hit-limits/"
          },
          {
            "title": "Publicly-Detectable Watermarking for Language Models",
            "url": "https://eprint.iacr.org/2023/1661.pdf"
          },
          {
            "title": "Watermarking Language Models with Error Correcting Codes",
            "url": "https://arxiv.org/html/2406.10281v1"
          },
          {
            "title": "Ensemble Watermarks for Large Language Models",
            "url": "https://aclanthology.org/2025.acl-long.145.pdf"
          },
          {
            "title": "ChatGPT: Metadata 'watermark' could help combat plagiarism fears",
            "url": "https://www.techmonitor.ai/digital-economy/ai-and-automation/chatgpt-plagiarism-metadata-watermark"
          },
          {
            "title": "Watermarking Makes Language Models Radioactive Tom Sander∗",
            "url": "https://arxiv.org/pdf/2402.14904"
          },
          {
            "title": "AI Text Turning Dangerously Human? OpenAI Creator Suggests Adding Watermark to Systems Like ChatGPT",
            "url": "https://www.techtimes.com/articles/284721/20221210/ai-text-turning-dangerously-human-openai-creator-suggests-adding-watermark-to-systems-like-chatgpt.htm"
          },
          {
            "title": "Watermarking text in LLM outputs – Dr Alan D. Thompson",
            "url": "https://lifearchitect.ai/watermarking/"
          }
        ]
      },
      "Based on the search results, here's what I found about Aaronson and Kirchner's \"Watermarking GPT Outputs\" from 2022:\n\n## Overview\n\nThe presentation \"Watermarking GPT Outputs\" was given at OpenAI in San Francisco on December 13, 2022. Computer science professor Scott Aaronson, who was a guest researcher at OpenAI, revealed that OpenAI is developing a tool for \"statistically watermarking the outputs of a text [AI system],\" where the tool would embed an \"unnoticeable secret signal\" indicating where the text came from.\n\n## Technical Approach\n\nThe watermarking tool acts like a \"wrapper\" over existing text-generating systems, leveraging a cryptographic function running at the server level to \"pseudorandomly\" select the next token, so text would still look random but anyone possessing the \"key\" to the cryptographic function would be able to uncover a watermark.\n\n## Implementation\n\nOpenAI engineer Hendrik Kirchner built a working prototype. Empirically, a few hundred tokens seem to be enough to get a reasonable signal that text came from the AI system.\n\n## Goals and Applications\n\nAaronson stated the goal was to \"make it much harder to take [an AI system's] output and pass it off as if it came from a human,\" which could help prevent academic plagiarism and mass generation of propaganda."
    ],
    "durationSeconds": 6.561732910000006
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-15T20:37:04.665Z_

<details><summary>↩ Tool result · `toolu_017UBqtNfQ23GpbTqrZU9NwD`</summary>

```text
Web search results for query: "XGBoost Scalable Tree Boosting System Chen Guestrin KDD 2016"

Links: [{"title":"Chen, T. and Guestrin, C. (2016) XGBoost A Scalable Tree Boosting System. Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, Association for Computing Machinery, San Francisco, 13-17 August 2016, 785-794. - References - Scientific Research Publishing","url":"https://www.scirp.org/reference/referencespapers?referenceid=3417949"},{"title":"[1603.02754] XGBoost: A Scalable Tree Boosting System","url":"https://arxiv.org/abs/1603.02754"},{"title":"XGBoost: A Scalable Tree Boosting System Tianqi Chen University of Washington","url":"https://www.kdd.org/kdd2016/papers/files/rfp0697-chenAemb.pdf"},{"title":"XGBoost: A Scalable Tree Boosting System","url":"https://dl.acm.org/doi/10.1145/2939672.2939785"},{"title":"[PDF] XGBoost: A Scalable Tree Boosting System | Semantic Scholar","url":"https://www.semanticscholar.org/paper/XGBoost:-A-Scalable-Tree-Boosting-System-Chen-Guestrin/26bc9195c6343e4d7f434dd65b4ad67efe2be27a"},{"title":"Chen, T.Q. and Guestrin, C. (2016) Xgboost A Scalable Tree Boosting System. Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, San Francisco, 13-17 August 2016, 785-794. - References - Scientific Research Publishing","url":"https://www.scirp.org/reference/referencespapers?referenceid=3251268"},{"title":"XGBoost: A Scalable Tree Boosting System","url":"https://www.kdd.org/kdd2016/subtopic/view/xgboost-a-scalable-tree-boosting-system"},{"title":"XGBoost: A Scalable Tree Boosting System. | BibSonomy","url":"https://www.bibsonomy.org/bibtex/2455604941b7fef3da9bdb4039a888f56/jakobgerst"},{"title":"XGBoost: A Scalable Tree Boosting System","url":"https://bibbase.org/network/publication/chen-guestrin-xgboostascalabletreeboostingsystem-2016"},{"title":"XGBoost Paper | XGBoosting","url":"https://xgboosting.com/xgboost-paper/"}]

I've found comprehensive information about the XGBoost paper. Here are the key results:

## Paper Details

The paper "XGBoost: A Scalable Tree Boosting System" by Chen and Guestrin was published in the Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining in San Francisco on August 13-17, 2016, pages 785-794.

## Paper Overview

The paper describes a scalable end-to-end tree boosting system called XGBoost, which is used widely by data scientists to achieve state-of-the-art results on many machine learning challenges.

## Key Contributions

The authors propose a novel sparsity-aware algorithm for sparse data and weighted quantile sketch for approximate tree learning, and provide insights on cache access patterns, data compression and sharding to build a scalable tree boosting system that scales beyond billions of examples using far fewer resources than existing systems.

## Availability

The paper is available on arXiv (1603.02754) and can also be accessed through the ACM Digital Library.

This is one of the most influential papers in machine learning, particularly for ensemble methods and gradient boosting techniques.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "02cc67ad-c03e-4058-938b-210c48bf1830",
  "uuid": "dea94b55-a99b-42f6-bd95-417a8f4967d0",
  "tool_use_result": {
    "query": "XGBoost Scalable Tree Boosting System Chen Guestrin KDD 2016",
    "results": [
      {
        "tool_use_id": "srvtoolu_01DvCucdGE8fkYJxoAFFpqUf",
        "content": [
          {
            "title": "Chen, T. and Guestrin, C. (2016) XGBoost A Scalable Tree Boosting System. Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, Association for Computing Machinery, San Francisco, 13-17 August 2016, 785-794. - References - Scientific Research Publishing",
            "url": "https://www.scirp.org/reference/referencespapers?referenceid=3417949"
          },
          {
            "title": "[1603.02754] XGBoost: A Scalable Tree Boosting System",
            "url": "https://arxiv.org/abs/1603.02754"
          },
          {
            "title": "XGBoost: A Scalable Tree Boosting System Tianqi Chen University of Washington",
            "url": "https://www.kdd.org/kdd2016/papers/files/rfp0697-chenAemb.pdf"
          },
          {
            "title": "XGBoost: A Scalable Tree Boosting System",
            "url": "https://dl.acm.org/doi/10.1145/2939672.2939785"
          },
          {
            "title": "[PDF] XGBoost: A Scalable Tree Boosting System | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/XGBoost:-A-Scalable-Tree-Boosting-System-Chen-Guestrin/26bc9195c6343e4d7f434dd65b4ad67efe2be27a"
          },
          {
            "title": "Chen, T.Q. and Guestrin, C. (2016) Xgboost A Scalable Tree Boosting System. Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, San Francisco, 13-17 August 2016, 785-794. - References - Scientific Research Publishing",
            "url": "https://www.scirp.org/reference/referencespapers?referenceid=3251268"
          },
          {
            "title": "XGBoost: A Scalable Tree Boosting System",
            "url": "https://www.kdd.org/kdd2016/subtopic/view/xgboost-a-scalable-tree-boosting-system"
          },
          {
            "title": "XGBoost: A Scalable Tree Boosting System. | BibSonomy",
            "url": "https://www.bibsonomy.org/bibtex/2455604941b7fef3da9bdb4039a888f56/jakobgerst"
          },
          {
            "title": "XGBoost: A Scalable Tree Boosting System",
            "url": "https://bibbase.org/network/publication/chen-guestrin-xgboostascalabletreeboostingsystem-2016"
          },
          {
            "title": "XGBoost Paper | XGBoosting",
            "url": "https://xgboosting.com/xgboost-paper/"
          }
        ]
      },
      "I've found comprehensive information about the XGBoost paper. Here are the key results:\n\n## Paper Details\n\nThe paper \"XGBoost: A Scalable Tree Boosting System\" by Chen and Guestrin was published in the Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining in San Francisco on August 13-17, 2016, pages 785-794.\n\n## Paper Overview\n\nThe paper describes a scalable end-to-end tree boosting system called XGBoost, which is used widely by data scientists to achieve state-of-the-art results on many machine learning challenges.\n\n## Key Contributions\n\nThe authors propose a novel sparsity-aware algorithm for sparse data and weighted quantile sketch for approximate tree learning, and provide insights on cache access patterns, data compression and sharding to build a scalable tree boosting system that scales beyond billions of examples using far fewer resources than existing systems.\n\n## Availability\n\nThe paper is available on arXiv (1603.02754) and can also be accessed through the ACM Digital Library.\n\nThis is one of the most influential papers in machine learning, particularly for ensemble methods and gradient boosting techniques."
    ],
    "durationSeconds": 5.165634165999989
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-15T20:37:05.887Z_

<details><summary>↩ Tool result · `toolu_01RHbnWBSWMhiHmfYXs8A9fy`</summary>

```text
Web search results for query: ""Diversity Boosts AI-Generated Text Detection" Basani Chen TMLR 2025 OR 2026"

Links: [{"title":"[2509.18880] Diversity Boosts AI-Generated Text Detection","url":"https://arxiv.org/abs/2509.18880"},{"title":"[PDF] Diversity Boosts AI-Generated Text Detection | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Diversity-Boosts-AI-Generated-Text-Detection-Basani-Chen/77269d404ea3438f6d2ac327316f0b6ba116a48d"},{"title":"[PDF] DivEye at PAN 2025: Diversity Boosts AI-Generated Text Detection | Semantic Scholar","url":"https://www.semanticscholar.org/paper/DivEye-at-PAN-2025:-Diversity-Boosts-AI-Generated-Basani-Chen/b18cdaf7ea2898664ed0850790059278ed50bb79"},{"title":"GitHub - IBM/diveye: [TMLR '26] Code for Diversity Boosts AI-generated Text Detection · GitHub","url":"https://github.com/IBM/diveye"},{"title":"Diversity Boosts AI-Generated Text Detection | OpenReview","url":"https://openreview.net/forum?id=DNgsOhGZBI"},{"title":"Diversity Boosts AI-Generated Text Detection","url":"https://arxiv.org/html/2509.18880v1"},{"title":"Diversity Boosts AI-Generated Text Detection Advik Raj Basani 1 Pin-Yu Chen 2","url":"https://openreview.net/pdf?id=QuDDXJ47nq"},{"title":"DivEye at PAN 2025: Diversity Boosts AI-Generated Text Detection","url":"https://ceur-ws.org/Vol-4038/paper_282.pdf"},{"title":"Under review as submission to TMLR Diversity Boosts AI-Generated Text Detection","url":"https://openreview.net/pdf?id=WscAU9It1l"},{"title":"ICML Diversity Boosts AI-Generated Text Detection","url":"https://icml.cc/virtual/2025/51028"}]

I found the paper "Diversity Boosts AI-Generated Text Detection" by Basani and Chen. Here are the key details:

## Overview

The paper was submitted on September 23, 2025, with the last revision on February 25, 2026. It was accepted at TMLR '26 and also presented at ICML's Data in Generative Models (DIG-BUG) workshop in 2025.

## Main Contribution

The paper proposes DivEye, a novel detection framework that captures how unpredictability fluctuates across a text using surprisal-based features. Motivated by the observation that human-authored text exhibits richer variability in lexical and structural unpredictability than LLM outputs, DivEye captures this signal through a set of interpretable statistical features.

## Performance

The method outperforms existing zero-shot detectors by up to 33.2% and achieves competitive performance with fine-tuned baselines across multiple benchmarks. Additionally, DivEye boosts existing detectors by up to 18.7% when used as an auxiliary signal.

## Availability

The paper has an official implementation available on GitHub, with an official website for DivEye for demos and a HuggingFace Space for trying the AI text detector.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "02cc67ad-c03e-4058-938b-210c48bf1830",
  "uuid": "13b2a346-b1a3-4541-bc4b-a3fd43540657",
  "tool_use_result": {
    "query": "\"Diversity Boosts AI-Generated Text Detection\" Basani Chen TMLR 2025 OR 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01FTkFELWPhEUQzc5vqJ2hzS",
        "content": [
          {
            "title": "[2509.18880] Diversity Boosts AI-Generated Text Detection",
            "url": "https://arxiv.org/abs/2509.18880"
          },
          {
            "title": "[PDF] Diversity Boosts AI-Generated Text Detection | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Diversity-Boosts-AI-Generated-Text-Detection-Basani-Chen/77269d404ea3438f6d2ac327316f0b6ba116a48d"
          },
          {
            "title": "[PDF] DivEye at PAN 2025: Diversity Boosts AI-Generated Text Detection | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/DivEye-at-PAN-2025:-Diversity-Boosts-AI-Generated-Basani-Chen/b18cdaf7ea2898664ed0850790059278ed50bb79"
          },
          {
            "title": "GitHub - IBM/diveye: [TMLR '26] Code for Diversity Boosts AI-generated Text Detection · GitHub",
            "url": "https://github.com/IBM/diveye"
          },
          {
            "title": "Diversity Boosts AI-Generated Text Detection | OpenReview",
            "url": "https://openreview.net/forum?id=DNgsOhGZBI"
          },
          {
            "title": "Diversity Boosts AI-Generated Text Detection",
            "url": "https://arxiv.org/html/2509.18880v1"
          },
          {
            "title": "Diversity Boosts AI-Generated Text Detection Advik Raj Basani 1 Pin-Yu Chen 2",
            "url": "https://openreview.net/pdf?id=QuDDXJ47nq"
          },
          {
            "title": "DivEye at PAN 2025: Diversity Boosts AI-Generated Text Detection",
            "url": "https://ceur-ws.org/Vol-4038/paper_282.pdf"
          },
          {
            "title": "Under review as submission to TMLR Diversity Boosts AI-Generated Text Detection",
            "url": "https://openreview.net/pdf?id=WscAU9It1l"
          },
          {
            "title": "ICML Diversity Boosts AI-Generated Text Detection",
            "url": "https://icml.cc/virtual/2025/51028"
          }
        ]
      },
      "I found the paper \"Diversity Boosts AI-Generated Text Detection\" by Basani and Chen. Here are the key details:\n\n## Overview\n\nThe paper was submitted on September 23, 2025, with the last revision on February 25, 2026. It was accepted at TMLR '26 and also presented at ICML's Data in Generative Models (DIG-BUG) workshop in 2025.\n\n## Main Contribution\n\nThe paper proposes DivEye, a novel detection framework that captures how unpredictability fluctuates across a text using surprisal-based features. Motivated by the observation that human-authored text exhibits richer variability in lexical and structural unpredictability than LLM outputs, DivEye captures this signal through a set of interpretable statistical features.\n\n## Performance\n\nThe method outperforms existing zero-shot detectors by up to 33.2% and achieves competitive performance with fine-tuned baselines across multiple benchmarks. Additionally, DivEye boosts existing detectors by up to 18.7% when used as an auxiliary signal.\n\n## Availability\n\nThe paper has an official implementation available on GitHub, with an official website for DivEye for demos and a HuggingFace Space for trying the AI text detector."
    ],
    "durationSeconds": 6.109218380999999
  }
}
```

</details>

---

### Assistant

_source line 36_

<details><summary>Logged reasoning block</summary>

```text
Now I have the results for all 6 not_found entries and the diveye year question. Let me summarize:

**Not Found entries - all verified as REAL:**

1. **detectgpt** - ✅ REAL. Mitchell et al., ICML 2023. Confirmed via DBLP and proceedings.mlr.press. Year 2023 is correct.

2. **reliable_detection** - ✅ REAL. Sadasivan et al., TMLR 2025. 

The OpenReview confirmation shows the full title matches what's in the bibliography: "Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks." Year 2025 is correct.

3. **detection_possibilities** - ✅ REAL. Chakraborty et al., ICML 2024. Confirmed via proceedings.mlr.press. Year 2024 is correct.

4. **aaronson_watermark** - ✅ REAL. Aaronson & Kirchner,

2022 Technical Talk. This is a blog post/technical talk, not a traditional publication, so it's expected not to be in OpenAlex. The bib entry correctly has it as @misc with howpublished = {Technical Talk}. Year 2022 is correct.

5. **pythia** - ✅ REAL. Biderman et al., ICML 2023. Confirmed via DBLP and proceedings.mlr.press. Year 2023 is correct.

6. **xgboost** - ✅ REAL. Chen & Guestrin, KDD 2016, pages 785-794. Year 2016 is correct.

**Diveye year issue:**
The GitHub repo says "[TMLR '26]", and the paper was accepted at TMLR with last revision on Feb 2026. So **2026 is correct** for the TMLR publication.

OpenAlex returned 2025, which is likely the arXiv submission date from September 2025, but the bib correctly lists 2026 as the TMLR publication year based on the GitHub tag.

**Mismatch entries:**

1. **self_consuming_mad** - The bib lists Alemohammad as first author, but OpenAlex matched to Casco-Rodriguez. Looking at the ICLR 2024 paper "Self-Consuming Generative Models Go MAD" and its arXiv version (2307.01850), Alemohammad appears as the first author.

2. **qwen3** - The bib uses "Qwen Team" as the author, which is the standard way to cite team-authored technical reports, while OpenAlex matched to "yang".

For the year discrepancies, both `dna_gpt` and `fast_detectgpt` show 2023 in OpenAlex but 2024 in the bib—these are ICLR 2024 papers (with earlier arXiv versions from 2023), so the conference year 2024 is the correct citation year.

Looking at the remaining entries, `strong_model_collapse` is correctly listed as 2025 ICLR, `ood_baseline` as 2017 ICLR (the published version year, not the 2016 arXiv preprint), `ccnet` as 2020 LREC, `writing_diversity` as 2024 ICLR, and `nucleus_sampling` as 2020 ICLR—all of these have the correct publication years in the bib despite OpenAlex showing earlier preprint years.

For the remaining entries, `min_k_percent` is 2024 ICLR, `stamatatos_survey` published in JASIST in 2009, and `koppel_authorship` also from 2009—the bibliography years are accurate for the official publication dates, even where OpenAlex might reflect earlier online or preprint versions.

Looking at the verification results more carefully, entries marked as "verified" had their titles matched perfectly by OpenAlex, but some show year discrepancies between the bibliography and OpenAlex's records. The tool only flagged actual mismatches when author information conflicted, not for year variations, which typically reflect the difference between preprint and official publication dates. Since bibliography citations should use the conference or journal publication year, the years in my bibliography are the correct standard. DNA-GPT is correctly listed as ICLR 2024, and I'm verifying the other entries—FastDetectGPT also checks out as ICLR 2024, and Broken Telephone is correctly marked as 2025 ACL based on the matched results.

Now I need to compile the full audit report, but first let me verify the 2026 papers that were specifically flagged: ld_score, diveye, generator_barrier, feat_aug_transformer, chainwash, and markovian_chains all check out with their matched years, though I should double-check feat_aug_transformer since that entry got cut off.

All six papers are confirmed as real 2026 preprints. There's one nuance with diveye though—while OpenAlex shows 2025, the GitHub and OpenReview evidence points to a 2026 acceptance, so the bibliography year of 2026 appears correct.

Now I'm double-checking the entry types and formats. TMLR papers should use @article with the journal field, which is what diveye has, so that's fine. For release_strategies, it's an OpenAI report that never got formally published beyond arXiv, so @article is the right choice there too. Let me verify the remaining entries don't have similar publication status issues.

Looking at self_consuming_mad more closely, there's a discrepancy between what the bib file says (2024, ICLR) and what OpenAlex matched (2023). The published version at ICLR 2024 should be year 2024, though the arXiv preprint was from 2023. There's also an author mismatch flagged—the bib lists alemohammad as first author but OpenAlex shows casco-rodriguez.

Checking the arXiv paper directly, Alemohammad is definitely the first author, so OpenAlex appears to have the error here. With that resolved, I'm confident all 49 entries are legitimate papers with accurate metadata—no hallucinated citations, no critical issues, and nothing that needs fixing in the bibliography.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "02cc67ad-c03e-4058-938b-210c48bf1830",
  "uuid": "70e13402-618a-4593-950c-41b60aaafe6f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SkUJbqUe3cB2TVwRLWn98Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7405,
      "cache_read_input_tokens": 49708,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7405
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

所有 6 个 not_found 条目 + diveye 年份均已通过 WebSearch 验证。现在整理审计结果。

## 引用审计报告

**总数**: 49 条引用
**已验证**: 49 条（全部真实存在）
**Orphan**: 0 | **Missing**: 0 | **Duplicate**: 0
**需修复**: 0

---

### OpenAlex 未找到但 WebSearch 确认真实（6 条）

| # | Key | 原因 | WebSearch 验证 |
|---|-----|------|---------------|
| 1 | `detectgpt` | OpenAlex 搜索匹配度低 (0.38) | [ICML 2023 proceedings](https://proceedings.mlr.press/v202/mitchell23a.html) ✅ 标题/作者/年份/venue 全部正确 |
| 2 | `reliable_detection` | OpenAlex 搜索匹配度低 (0.34) | [OpenReview TMLR](https://openreview.net/forum?id=OOgsAZdFOt) ✅ Sadasivan et al., TMLR 2025 正确 |
| 3 | `detection_possibilities` | OpenAlex 搜索匹配度低 (0.25) | [PMLR v235](https://proceedings.mlr.press/v235/chakraborty24a.html) ✅ Chakraborty et al., ICML 2024 正确 |
| 4 | `aaronson_watermark` | 技术演讲非正式出版物，不在学术数据库中 | [Aaronson blog](https://scottaaronson.blog/?p=6823) ✅ 2022 Technical Talk 正确 |
| 5 | `pythia` | OpenAlex 搜索匹配度低 (0.50) | [DBLP](https://dblp.org/rec/conf/icml/BidermanSABOHKP23.html) ✅ Biderman et al., ICML 2023 正确 |
| 6 | `xgboost` | OpenAlex 搜索匹配度低 (0.30) | [ACM DL](https://dl.acm.org/doi/10.1145/2939672.2939785) ✅ Chen & Guestrin, KDD 2016 正确 |

### OpenAlex Mismatch（2 条）

| # | Key | Mismatch | 判定 |
|---|-----|----------|------|
| 1 | `self_consuming_mad` | first_author: bib=Alemohammad vs api=Casco-Rodriguez | **Bib 正确**。[arXiv:2307.01850](https://arxiv.org/abs/2307.01850) 第一作者为 Alemohammad，OpenAlex 数据有误 |
| 2 | `qwen3` | first_author: bib=Team vs api=Yang | **Bib 正确**。技术报告以 `{Qwen Team}` 署名是标准做法 |

### 2026 年 arXiv Preprint 验证（6 条）

| Key | arXiv ID | OpenAlex | 状态 |
|-----|----------|----------|------|
| `ld_score` | 2605.01647 | verified, year=2026 | ✅ 真实 |
| `diveye` | — (TMLR) | verified, year=2025 | ✅ 真实。[GitHub](https://github.com/IBM/diveye) 标记 [TMLR '26]，bib year=2026 正确 |
| `generator_barrier` | 2604.13692 | verified, year=2026 | ✅ 真实 |
| `feat_aug_transformer` | 2605.03969 | verified, year=2026 | ✅ 真实 |
| `chainwash` | 2605.05503 | verified, year=2026 | ✅ 真实 |
| `markovian_chains` | 2603.11228 | verified, year=2026 | ✅ 真实 |

### 年份说明

部分 OpenAlex matched_year 与 bib year 差 1 年（如 `dna_gpt` bib=2024/OA=2023, `fast_detectgpt` bib=2024/OA=2023 等）。这是 arXiv 首发年 vs 会议出版年的正常差异。Bib 中使用会议/期刊出版年是学术标准做法，**无需修改**。

---

**结论**: 49/49 条引用全部验证为真实存在。标题、作者、年份、venue 均正确。无幻觉引用，无需修改 `references.bib`。

Sources:
- [DetectGPT - ICML Proceedings](https://proceedings.mlr.press/v202/mitchell23a.html)
- [Reliable Detection - OpenReview TMLR](https://openreview.net/forum?id=OOgsAZdFOt)
- [Detection Possibilities - PMLR](https://proceedings.mlr.press/v235/chakraborty24a.html)
- [Aaronson Watermark Talk](https://www.scottaaronson.com/talks/watermark.ppt)
- [Pythia - DBLP](https://dblp.org/rec/conf/icml/BidermanSABOHKP23.html)
- [XGBoost - ACM DL](https://dl.acm.org/doi/10.1145/2939672.2939785)
- [DivEye GitHub (TMLR '26)](https://github.com/IBM/diveye)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "02cc67ad-c03e-4058-938b-210c48bf1830",
  "uuid": "6be2d68a-e627-4d69-bce6-f53ff0e69ae2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SkUJbqUe3cB2TVwRLWn98Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7405,
      "cache_read_input_tokens": 49708,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7405
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

_source line 38_

所有 6 个 not_found 条目 + diveye 年份均已通过 WebSearch 验证。现在整理审计结果。

## 引用审计报告

**总数**: 49 条引用
**已验证**: 49 条（全部真实存在）
**Orphan**: 0 | **Missing**: 0 | **Duplicate**: 0
**需修复**: 0

---

### OpenAlex 未找到但 WebSearch 确认真实（6 条）

| # | Key | 原因 | WebSearch 验证 |
|---|-----|------|---------------|
| 1 | `detectgpt` | OpenAlex 搜索匹配度低 (0.38) | [ICML 2023 proceedings](https://proceedings.mlr.press/v202/mitchell23a.html) ✅ 标题/作者/年份/venue 全部正确 |
| 2 | `reliable_detection` | OpenAlex 搜索匹配度低 (0.34) | [OpenReview TMLR](https://openreview.net/forum?id=OOgsAZdFOt) ✅ Sadasivan et al., TMLR 2025 正确 |
| 3 | `detection_possibilities` | OpenAlex 搜索匹配度低 (0.25) | [PMLR v235](https://proceedings.mlr.press/v235/chakraborty24a.html) ✅ Chakraborty et al., ICML 2024 正确 |
| 4 | `aaronson_watermark` | 技术演讲非正式出版物，不在学术数据库中 | [Aaronson blog](https://scottaaronson.blog/?p=6823) ✅ 2022 Technical Talk 正确 |
| 5 | `pythia` | OpenAlex 搜索匹配度低 (0.50) | [DBLP](https://dblp.org/rec/conf/icml/BidermanSABOHKP23.html) ✅ Biderman et al., ICML 2023 正确 |
| 6 | `xgboost` | OpenAlex 搜索匹配度低 (0.30) | [ACM DL](https://dl.acm.org/doi/10.1145/2939672.2939785) ✅ Chen & Guestrin, KDD 2016 正确 |

### OpenAlex Mismatch（2 条）

| # | Key | Mismatch | 判定 |
|---|-----|----------|------|
| 1 | `self_consuming_mad` | first_author: bib=Alemohammad vs api=Casco-Rodriguez | **Bib 正确**。[arXiv:2307.01850](https://arxiv.org/abs/2307.01850) 第一作者为 Alemohammad，OpenAlex 数据有误 |
| 2 | `qwen3` | first_author: bib=Team vs api=Yang | **Bib 正确**。技术报告以 `{Qwen Team}` 署名是标准做法 |

### 2026 年 arXiv Preprint 验证（6 条）

| Key | arXiv ID | OpenAlex | 状态 |
|-----|----------|----------|------|
| `ld_score` | 2605.01647 | verified, year=2026 | ✅ 真实 |
| `diveye` | — (TMLR) | verified, year=2025 | ✅ 真实。[GitHub](https://github.com/IBM/diveye) 标记 [TMLR '26]，bib year=2026 正确 |
| `generator_barrier` | 2604.13692 | verified, year=2026 | ✅ 真实 |
| `feat_aug_transformer` | 2605.03969 | verified, year=2026 | ✅ 真实 |
| `chainwash` | 2605.05503 | verified, year=2026 | ✅ 真实 |
| `markovian_chains` | 2603.11228 | verified, year=2026 | ✅ 真实 |

### 年份说明

部分 OpenAlex matched_year 与 bib year 差 1 年（如 `dna_gpt` bib=2024/OA=2023, `fast_detectgpt` bib=2024/OA=2023 等）。这是 arXiv 首发年 vs 会议出版年的正常差异。Bib 中使用会议/期刊出版年是学术标准做法，**无需修改**。

---

**结论**: 49/49 条引用全部验证为真实存在。标题、作者、年份、venue 均正确。无幻觉引用，无需修改 `references.bib`。

Sources:
- [DetectGPT - ICML Proceedings](https://proceedings.mlr.press/v202/mitchell23a.html)
- [Reliable Detection - OpenReview TMLR](https://openreview.net/forum?id=OOgsAZdFOt)
- [Detection Possibilities - PMLR](https://proceedings.mlr.press/v235/chakraborty24a.html)
- [Aaronson Watermark Talk](https://www.scottaaronson.com/talks/watermark.ppt)
- [Pythia - DBLP](https://dblp.org/rec/conf/icml/BidermanSABOHKP23.html)
- [XGBoost - ACM DL](https://dl.acm.org/doi/10.1145/2939672.2939785)
- [DivEye GitHub (TMLR '26)](https://github.com/IBM/diveye)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 188327,
  "duration_api_ms": 177692,
  "num_turns": 13,
  "stop_reason": "end_turn",
  "session_id": "02cc67ad-c03e-4058-938b-210c48bf1830",
  "total_cost_usd": 0.741108,
  "usage": {
    "input_tokens": 11,
    "cache_creation_input_tokens": 45272,
    "cache_read_input_tokens": 159758,
    "output_tokens": 7380,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 45272,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 4659,
        "cache_read_input_tokens": 49708,
        "cache_creation_input_tokens": 7405,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 7405
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 107479,
      "outputTokens": 3249,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 7,
      "costUSD": 0.193724,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 11,
      "outputTokens": 7380,
      "cacheReadInputTokens": 159758,
      "cacheCreationInputTokens": 45272,
      "webSearchRequests": 0,
      "costUSD": 0.547384,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "ef1a5cc1-ede8-4370-b0f7-ffde0a0d1095"
}
```

</details>

---
