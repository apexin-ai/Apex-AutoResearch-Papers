# paper research cluster 5 llm evaluation

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 71
- **Recorded user turns:** 1
- **Tool calls:** 22
- **Original source:** `logs/workers/worker_paper_research_cluster_5_llm_evaluation_20260521T034721.log`
- **Structured JSON:** [`45390c28a98c4d771cc7.json`](../../sessions/45/45390c28a98c4d771cc7.json)

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "session_id": "ca6fa12b-f060-44ff-a3f8-2be93538cabe",
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
    "mcp__agent-ml-research__auto_build_provenance",
    "mcp__agent-ml-research__bootstrap_provenance",
    "mcp__agent-ml-research__check_figures_and_layout",
    "mcp__agent-ml-research__check_paper_consistency",
    "mcp__agent-ml-research__check_provenance_completeness",
    "mcp__agent-ml-research__cleanup_pdf_images",
    "mcp__agent-ml-research__compute_coverage_matrix",
    "mcp__agent-ml-research__edit_paper_section",
    "mcp__agent-ml-research__get_image_info",
    "mcp__agent-ml-research__get_worker_status",
    "mcp__agent-ml-research__list_artifacts",
    "mcp__agent-ml-research__list_workers",
    "mcp__agent-ml-research__load_project_config",
    "mcp__agent-ml-research__overleaf_init",
    "mcp__agent-ml-research__overleaf_pull",
    "mcp__agent-ml-research__overleaf_push",
    "mcp__agent-ml-research__overleaf_status",
    "mcp__agent-ml-research__overleaf_sync",
    "mcp__agent-ml-research__paper_agent_post_to_director",
    "mcp__agent-ml-research__paper_agent_request_review",
    "mcp__agent-ml-research__paper_compile_and_check",
    "mcp__agent-ml-research__pdf_to_images",
    "mcp__agent-ml-research__read_experiment_plan_with_status",
    "mcp__agent-ml-research__read_project_file",
    "mcp__agent-ml-research__read_registry",
    "mcp__agent-ml-research__read_roadmap",
    "mcp__agent-ml-research__register_artifact",
    "mcp__agent-ml-research__save_project_file",
    "mcp__agent-ml-research__send_progress",
    "mcp__agent-ml-research__spawn_worker",
    "mcp__agent-ml-research__verify_references",
    "mcp__agent-ml-research__write_paper_section"
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
  "uuid": "68e9311b-f098-4346-8d6e-859a0ec3a298",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0520-2-projects-irt-equated-bench-regen/memory/"
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
    "resetsAt": 1779351600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "cf869c1b-2289-431a-b4fa-166d15f7a20f",
  "session_id": "ca6fa12b-f060-44ff-a3f8-2be93538cabe"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by reading the reference-audit skill as instructed, then proceed to find and verify 5 papers on LLM evaluation methodology.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ca6fa12b-f060-44ff-a3f8-2be93538cabe",
  "uuid": "052a84f1-4c9a-4790-af69-4859f6e0747f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011PpuNg2iz9oPHib9eQabsQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11742,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11742
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

I'll read the reference-audit skill first, then search for papers in this cluster.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ca6fa12b-f060-44ff-a3f8-2be93538cabe",
  "uuid": "576957f6-c0bb-43a8-a429-c181e2d82fdf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011PpuNg2iz9oPHib9eQabsQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11742,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11742
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

<details open><summary>🔧 Tool call — Read · `toolu_01N2xAHdbgtDbebQs5rYxsdu`</summary>

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
  "session_id": "ca6fa12b-f060-44ff-a3f8-2be93538cabe",
  "uuid": "5c95ddac-b02f-4054-8d9f-cb6378cfca06",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011PpuNg2iz9oPHib9eQabsQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11742,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11742
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

_source line 7 · 2026-05-21T03:47:34.507Z_

<details><summary>↩ Tool result · `toolu_01N2xAHdbgtDbebQs5rYxsdu`</summary>

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
  "session_id": "ca6fa12b-f060-44ff-a3f8-2be93538cabe",
  "uuid": "ff6ff5b2-c597-4061-b833-9e35e8d2b97a",
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

<details open><summary>🔧 Tool call — Read · `toolu_011nbiZkNYm5jCfymcZw1SQp`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/literature_map.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ca6fa12b-f060-44ff-a3f8-2be93538cabe",
  "uuid": "cb928170-aa26-4724-a343-aa6e00700adb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011PpuNg2iz9oPHib9eQabsQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11742,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11742
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

_source line 9 · 2026-05-21T03:47:35.240Z_

<details><summary>↩ Tool result · reported error · `toolu_011nbiZkNYm5jCfymcZw1SQp`</summary>

```text
File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ca6fa12b-f060-44ff-a3f8-2be93538cabe",
  "uuid": "abc77d3d-ccc7-403a-a7f9-423c7d5ece39",
  "tool_use_result": "Error: File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen."
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — Agent · `toolu_01HEMacAuxLS4KWqW5b4EsLA`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Find literature_map.yaml location",
  "prompt": "Find the literature_map.yaml file in the project directory /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/. Search broadly — it might be in artifacts/, paper/, or root level. Also check if there's a core/tools/literature.py or similar module under /home/ubuntu/agent-ml-research/."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ca6fa12b-f060-44ff-a3f8-2be93538cabe",
  "uuid": "743991a9-5c01-42a9-8919-d53832adcb2e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MJeAzmYZmCpEUbs3wTNre9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2309,
      "cache_read_input_tokens": 23583,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2309
      },
      "output_tokens": 40,
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

_source line 11_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "a5a664161719b85a9",
  "tool_use_id": "toolu_01HEMacAuxLS4KWqW5b4EsLA",
  "description": "Find literature_map.yaml location",
  "task_type": "local_agent",
  "prompt": "Find the literature_map.yaml file in the project directory /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/. Search broadly — it might be in artifacts/, paper/, or root level. Also check if there's a core/tools/literature.py or similar module under /home/ubuntu/agent-ml-research/.",
  "uuid": "09843bcc-c78f-4b2f-8c64-ae9a10b18069",
  "session_id": "ca6fa12b-f060-44ff-a3f8-2be93538cabe"
}
```

---

## Round 1

60 recorded events

### User

_source line 12 · 2026-05-21T03:47:40.950Z_

Find the literature_map.yaml file in the project directory /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/. Search broadly — it might be in artifacts/, paper/, or root level. Also check if there's a core/tools/literature.py or similar module under /home/ubuntu/agent-ml-research/.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01HEMacAuxLS4KWqW5b4EsLA",
  "session_id": "ca6fa12b-f060-44ff-a3f8-2be93538cabe",
  "uuid": "d25666a4-36ec-440b-92fe-142ab4326ed6"
}
```

</details>

---

### System

_source line 13_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a5a664161719b85a9",
  "tool_use_id": "toolu_01HEMacAuxLS4KWqW5b4EsLA",
  "description": "Finding **/literature_map.yaml",
  "usage": {
    "total_tokens": 27711,
    "tool_uses": 1,
    "duration_ms": 2083
  },
  "last_tool_name": "Glob",
  "uuid": "4f2f0161-f86d-4009-a0ee-9597a0690909",
  "session_id": "ca6fa12b-f060-44ff-a3f8-2be93538cabe"
}
```

---

### Tool call

_source line 14_

<details open><summary>🔧 Tool call — Glob · `toolu_01BEJrYhGm5cwnvSYJK32ztw`</summary>

```json
{
  "pattern": "**/literature_map.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01HEMacAuxLS4KWqW5b4EsLA",
  "session_id": "ca6fa12b-f060-44ff-a3f8-2be93538cabe",
  "uuid": "09da1c56-87fe-432f-a3d8-ab88f8a24656",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01LZGmQBznd7VwwTj9sFSWQv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 27702,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 27702,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 15 · 2026-05-21T03:47:43.063Z_

<details><summary>↩ Tool result · `toolu_01BEJrYhGm5cwnvSYJK32ztw`</summary>

```text
literature_map.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01HEMacAuxLS4KWqW5b4EsLA",
  "session_id": "ca6fa12b-f060-44ff-a3f8-2be93538cabe",
  "uuid": "868ea32f-627a-42db-915d-2a8e2988014f"
}
```

</details>

---

### System

_source line 16_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a5a664161719b85a9",
  "tool_use_id": "toolu_01HEMacAuxLS4KWqW5b4EsLA",
  "description": "Finding **/literature*",
  "usage": {
    "total_tokens": 27714,
    "tool_uses": 2,
    "duration_ms": 2293
  },
  "last_tool_name": "Glob",
  "uuid": "7955fdb5-235e-4bf7-8f45-e8d26d0fdf97",
  "session_id": "ca6fa12b-f060-44ff-a3f8-2be93538cabe"
}
```

---

### Tool call

_source line 17_

<details open><summary>🔧 Tool call — Glob · `toolu_01Tvsba9Ho4T2rmHRXXqRHh1`</summary>

```json
{
  "pattern": "**/literature*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01HEMacAuxLS4KWqW5b4EsLA",
  "session_id": "ca6fa12b-f060-44ff-a3f8-2be93538cabe",
  "uuid": "57c8495f-a3fb-4d96-8640-72b764b41a12",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01LZGmQBznd7VwwTj9sFSWQv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 27702,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 27702,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 18 · 2026-05-21T03:47:43.257Z_

<details><summary>↩ Tool result · `toolu_01Tvsba9Ho4T2rmHRXXqRHh1`</summary>

```text
artifacts/_project/report/literature_survey_d011.md
artifacts/_project/report/literature_survey_d011_167b57.md
artifacts/literature_survey_d011.md
literature_map.lock
literature_map.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01HEMacAuxLS4KWqW5b4EsLA",
  "session_id": "ca6fa12b-f060-44ff-a3f8-2be93538cabe",
  "uuid": "fc699435-6b26-449b-b6df-068205a8b302"
}
```

</details>

---

### System

_source line 19_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a5a664161719b85a9",
  "tool_use_id": "toolu_01HEMacAuxLS4KWqW5b4EsLA",
  "description": "Finding **/literature.py",
  "usage": {
    "total_tokens": 27717,
    "tool_uses": 3,
    "duration_ms": 2512
  },
  "last_tool_name": "Glob",
  "uuid": "608c85a2-47f5-486e-8856-39824205fc74",
  "session_id": "ca6fa12b-f060-44ff-a3f8-2be93538cabe"
}
```

---

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — Glob · `toolu_01MMRMSoY5VMVPVj6CNcnNwg`</summary>

```json
{
  "pattern": "**/literature.py",
  "path": "/home/ubuntu/agent-ml-research"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01HEMacAuxLS4KWqW5b4EsLA",
  "session_id": "ca6fa12b-f060-44ff-a3f8-2be93538cabe",
  "uuid": "c7e1facc-d477-46c6-8544-7a28f9612fff",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01LZGmQBznd7VwwTj9sFSWQv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 27702,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 27702,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 21 · 2026-05-21T03:47:43.531Z_

<details><summary>↩ Tool result · `toolu_01MMRMSoY5VMVPVj6CNcnNwg`</summary>

```text
/home/ubuntu/agent-ml-research/core/tools/literature.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01HEMacAuxLS4KWqW5b4EsLA",
  "session_id": "ca6fa12b-f060-44ff-a3f8-2be93538cabe",
  "uuid": "37d9b26e-b983-412b-9799-ea667d448e9f"
}
```

</details>

---

### System

_source line 22_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a5a664161719b85a9",
  "tool_use_id": "toolu_01HEMacAuxLS4KWqW5b4EsLA",
  "description": "Running find /home/ubuntu/agent-ml-research -name \"litera…",
  "usage": {
    "total_tokens": 27720,
    "tool_uses": 4,
    "duration_ms": 2664
  },
  "last_tool_name": "Bash",
  "uuid": "039451d5-9f99-4692-90a1-0ddc3327d127",
  "session_id": "ca6fa12b-f060-44ff-a3f8-2be93538cabe"
}
```

---

### Tool call

_source line 23_

<details open><summary>🔧 Tool call — Bash · `toolu_01UYxaktFa6a2WN9KwMQapsY`</summary>

```json
{
  "command": "find /home/ubuntu/agent-ml-research -name \"literature*\" -type f 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01HEMacAuxLS4KWqW5b4EsLA",
  "session_id": "ca6fa12b-f060-44ff-a3f8-2be93538cabe",
  "uuid": "3755188e-28e3-4eb0-b855-17c37200f61d",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01LZGmQBznd7VwwTj9sFSWQv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 27702,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 27702,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 24 · 2026-05-21T03:47:43.851Z_

<details><summary>↩ Tool result · `toolu_01UYxaktFa6a2WN9KwMQapsY`</summary>

```text
/home/ubuntu/agent-ml-research/core/tools/__pycache__/literature.cpython-314.pyc
/home/ubuntu/agent-ml-research/core/tools/literature.py
/home/ubuntu/agent-ml-research/skills/global/literature-scan.skill.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01HEMacAuxLS4KWqW5b4EsLA",
  "session_id": "ca6fa12b-f060-44ff-a3f8-2be93538cabe",
  "uuid": "4fe2a9d5-65c0-48b9-a446-72cf4871b034"
}
```

</details>

---

### System

_source line 25_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a5a664161719b85a9",
  "tool_use_id": "toolu_01HEMacAuxLS4KWqW5b4EsLA",
  "description": "Reading literature_map.yaml",
  "usage": {
    "total_tokens": 29158,
    "tool_uses": 5,
    "duration_ms": 5330
  },
  "last_tool_name": "Read",
  "uuid": "6ded12d2-a0db-4ff5-8e79-678c8195fe06",
  "session_id": "ca6fa12b-f060-44ff-a3f8-2be93538cabe"
}
```

---

### Tool call

_source line 26_

<details open><summary>🔧 Tool call — Read · `toolu_01HEneRTG7YQi7qxybzZuni1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/literature_map.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01HEMacAuxLS4KWqW5b4EsLA",
  "session_id": "ca6fa12b-f060-44ff-a3f8-2be93538cabe",
  "uuid": "caa34e77-a7c3-4ed1-83c3-b19d3f7944c2",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Y3RxNbnYv9wXBtkybk7yPp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1432,
      "cache_read_input_tokens": 27702,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1432,
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

### System

_source line 27_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a5a664161719b85a9",
  "tool_use_id": "toolu_01HEMacAuxLS4KWqW5b4EsLA",
  "description": "Reading ~/agent-ml-research/core/tools/literature.py",
  "usage": {
    "total_tokens": 29159,
    "tool_uses": 6,
    "duration_ms": 5521
  },
  "last_tool_name": "Read",
  "uuid": "8ded7efc-6bf1-49d4-9ea8-93910aa52723",
  "session_id": "ca6fa12b-f060-44ff-a3f8-2be93538cabe"
}
```

---

### Tool call

_source line 28_

<details open><summary>🔧 Tool call — Read · `toolu_01JLApBeVKFHKwvyL8wcb66F`</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/core/tools/literature.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01HEMacAuxLS4KWqW5b4EsLA",
  "session_id": "ca6fa12b-f060-44ff-a3f8-2be93538cabe",
  "uuid": "af04debd-12d3-457c-9268-9337b49ee7b2",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Y3RxNbnYv9wXBtkybk7yPp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1432,
      "cache_read_input_tokens": 27702,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1432,
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

_source line 29 · 2026-05-21T03:47:46.517Z_

<details><summary>↩ Tool result · `toolu_01JLApBeVKFHKwvyL8wcb66F`</summary>

```text
1	"""Literature map — persistent, cross-stage knowledge base of papers.
2	
3	The literature_map.yaml is the single source of truth for papers a project
4	accumulates across the Idea → Research → Writing → Review pipeline. Each
5	entry is verified (or marked unverified) and carries enough metadata to
6	generate BibTeX entries and to drive Related Work / citation gap-fill in
7	the Paper Agent's writing pipeline.
8	
9	Two scopes:
10	
11	  - Project-level: ``projects/{project}/literature_map.yaml``
12	      Used during Research and Writing phases.
13	
14	  - Global (Idea phase): ``{WORKSPACE_ROOT}/literature_map.yaml``
15	      Used before a project exists. Each entry carries ``source_idea_id`` so
16	      multiple ideas can coexist. On project creation, matching entries are
17	      seeded into the project map.
18	
19	Design notes:
20	
21	  - Read paths support modes (summary / category:X / competitors / unverified
22	    / bib / full) so day-to-day reads stay token-cheap even when the map has
23	    grown to 40-60 papers.
24	
25	  - Writes hold an exclusive flock + use atomic temp→rename, modeled on
26	    ``core/tools/registry.py`` so the file never tears under concurrent
27	    Worker writes.
28	
29	  - Dedup happens on add: DOI exact match wins; otherwise normalized title
30	    match. Existing entries are merged (new fields fill empty existing
31	    fields) rather than overwritten.
32	"""
33	
34	from __future__ import annotations
35	
36	import fcntl
37	import logging
38	import os
39	import re
40	import tempfile
41	import unicodedata
42	from pathlib import Path
43	from typing import Any, Iterable
44	
45	import yaml
46	
47	from core import paths as _paths
48	from core.tools.result import ToolResult
49	
50	logger = logging.getLogger(__name__)
51	
52	
53	# ---------------------------------------------------------------------------
54	# Constants
55	# ---------------------------------------------------------------------------
56	
57	# Roles a paper can play relative to the project. Used by Related Work drafting
58	# (foundation papers anchor narratives; direct-competitor papers must be cited).
59	VALID_ROLES: frozenset[str] = frozenset(
60	    {"foundation", "direct-competitor", "method-component", "evaluation", "background"}
61	)
62	
63	# Modes for read_literature_map — keep token usage proportional to need.
64	VALID_READ_MODES: frozenset[str] = frozenset(
65	    {"summary", "competitors", "unverified", "bib", "full"}
66	)
67	
68	# Fields kept in summary mode (skips long fields like abstract, relevance).
69	_SUMMARY_FIELDS: tuple[str, ...] = (
70	    "title", "year", "venue", "category", "role", "verified", "bibtex_key",
71	)
72	
73	
74	# ---------------------------------------------------------------------------
75	# Path resolution
76	# ---------------------------------------------------------------------------
77	
78	def get_literature_map_path(project: str | None = None) -> Path:
79	    """Resolve the literature_map.yaml path.
80	
81	    Project name → ``projects/{project}/literature_map.yaml`` (V3 layout).
82	    No project   → ``{WORKSPACE_ROOT}/literature_map.yaml`` (global, idea phase).
83	    """
84	    if project:
85	        p = _paths.resolve_project_file(project, "literature_map.yaml")
86	        p.parent.mkdir(parents=True, exist_ok=True)
87	        return p
88	    return _paths.global_literature_map_path()
89	
90	
91	# ---------------------------------------------------------------------------
92	# Atomic file I/O — modeled on registry._read_modify_write_registry
93	# ---------------------------------------------------------------------------
94	
95	def _empty_map() -> dict:
96	    return {
97	        "meta": {"last_updated": None, "total_papers": 0},
98	        "categories": [],
99	        "papers": {},
100	    }
101	
102	
103	def _read_map(path: Path) -> dict:
104	    """Read literature_map.yaml without a lock (atomic single-syscall read).
105	
106	    Returns a fresh empty skeleton if the file doesn't exist or is unreadable.
107	    Writers use exclusive flock + atomic rename so readers always see a
108	    consistent snapshot.
109	    """
110	    if not path.exists():
111	        return _empty_map()
112	    try:
113	        data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
114	    except Exception:
115	        logger.warning("Failed to parse literature_map at %s", path, exc_info=True)
116	        return _empty_map()
117	    if isinstance(data, list):
118	        data = {"papers": data, "meta": {}, "categories": []}
119	    elif not isinstance(data, dict):
120	        logger.warning("literature_map at %s is %s, expected dict — resetting", path, type(data).__name__)
121	        return _empty_map()
122	    data.setdefault("meta", {})
123	    data["meta"].setdefault("last_updated", None)
124	    data["meta"].setdefault("total_papers", 0)
125	    data.setdefault("categories", [])
126	    data.setdefault("papers", {})
127	    return data
128	
129	
130	def _read_modify_write(path: Path, modifier) -> dict:
131	    """Read, apply ``modifier(data)`` in place, atomically write back.
132	
133	    Holds LOCK_EX on a sibling .lock file (not the data file — atomic rename
134	    swaps the inode and would invalidate locks held on it).
135	    """
136	    path.parent.mkdir(parents=True, exist_ok=True)
137	    lock_path = path.with_suffix(".lock")
138	
139	    with open(lock_path, "a+") as lock_f:
140	        fcntl.flock(lock_f, fcntl.LOCK_EX)
141	        try:
142	            data = _read_map(path)
143	            modifier(data)
144	            data["meta"]["total_papers"] = len(data.get("papers", {}))
145	            data["meta"]["last_updated"] = _paths.now_iso()
146	
147	            fd, tmp_path = tempfile.mkstemp(
148	                dir=str(path.parent), prefix=".literature_", suffix=".tmp"
149	            )
150	            try:
151	                with os.fdopen(fd, "w", encoding="utf-8") as tmp_f:
152	                    yaml.dump(
153	                        data, tmp_f,
154	                        default_flow_style=False, allow_unicode=True, sort_keys=False,
155	                    )
156	                    tmp_f.flush()
157	                    os.fsync(tmp_f.fileno())
158	                os.replace(tmp_path, str(path))
159	            except Exception:
160	                if os.path.exists(tmp_path):
161	                    os.unlink(tmp_path)
162	                raise
163	        finally:
164	            fcntl.flock(lock_f, fcntl.LOCK_UN)
165	
166	    return data
167	
168	
169	# ---------------------------------------------------------------------------
170	# Normalization & dedup
171	# ---------------------------------------------------------------------------
172	
173	_PUNCT_RE = re.compile(r"[^\w\s]")
174	_WS_RE = re.compile(r"\s+")
175	
176	
177	def _normalize_title(title: str) -> str:
178	    """Lowercase, strip diacritics + punctuation, collapse whitespace.
179	
180	    Used for fuzzy dedup when two records describe the same paper with
181	    slightly different titles (smart quotes, hyphens, capitalization).
182	    """
183	    if not title:
184	        return ""
185	    s = unicodedata.normalize("NFKD", title)
186	    s = "".join(c for c in s if not unicodedata.combining(c))
187	    s = s.lower()
188	    s = _PUNCT_RE.sub(" ", s)
189	    s = _WS_RE.sub(" ", s).strip()
190	    return s
191	
192	
193	def _normalize_doi(doi: str) -> str:
194	    """Lowercase DOI, strip common prefixes."""
195	    if not doi:
196	        return ""
197	    s = doi.strip().lower()
198	    for prefix in ("https://doi.org/", "http://doi.org/", "doi:"):
199	        if s.startswith(prefix):
200	            s = s[len(prefix):]
201	            break
202	    return s.strip()
203	
204	
205	def _slugify(s: str, max_len: int = 24) -> str:
206	    """First-word slug — lowercase, alnum only, truncated."""
207	    s = unicodedata.normalize("NFKD", s or "")
208	    s = "".join(c for c in s if not unicodedata.combining(c))
209	    s = re.sub(r"[^a-zA-Z0-9]+", "", s.split()[0] if s.split() else "")
210	    return s.lower()[:max_len]
211	
212	
213	def _generate_bibtex_key(paper: dict) -> str:
214	    """Generate a bibtex key like ``vaswani2017attention``.
215	
216	    Uses the first author's surname + year + the first significant word of
217	    the title. Falls back to ``paper_{hash}`` if metadata is missing.
218	    """
219	    authors = paper.get("authors") or []
220	    first_author = ""
221	    if authors:
222	        raw = authors[0]
223	        if isinstance(raw, str):
224	            # Could be "Vaswani, A." or "Ashish Vaswani"
225	            if "," in raw:
226	                first_author = raw.split(",", 1)[0].strip()
227	            else:
228	                first_author = raw.strip().split()[-1] if raw.strip() else ""
229	    surname = _slugify(first_author)
230	
231	    year = paper.get("year") or ""
232	    year_part = str(year) if year else ""
233	
234	    title = paper.get("title") or ""
235	    # Skip stop words for the title slug
236	    stop = {"a", "an", "the", "on", "in", "of", "for", "and", "or", "is", "to"}
237	    words = [w for w in re.split(r"\W+", title.lower()) if w and w not in stop]
238	    word = _slugify(words[0]) if words else ""
239	
240	    key = f"{surname}{year_part}{word}"
241	    if not key.strip():
242	        import hashlib
243	        h = hashlib.md5(title.encode("utf-8")).hexdigest()[:8]
244	        key = f"paper_{h}"
245	    return key
246	
247	
248	def _find_existing_key(papers: dict, candidate: dict) -> str | None:
249	    """Find a matching paper key in ``papers`` for the candidate dict.
250	
251	    Match order: DOI exact (normalized) → normalized title.
252	    Returns the existing key or None.
253	
254	    bibtex_key collisions are NOT treated as dedup signal — two different
255	    papers can share a naive bibtex_key (e.g. same first author + year), and
256	    we handle that with a suffix at insert time. Real dedup must be content
257	    based.
258	    """
259	    cand_doi = _normalize_doi(candidate.get("doi", ""))
260	    cand_title = _normalize_title(candidate.get("title", ""))
261	
262	    for key, entry in papers.items():
263	        if cand_doi:
264	            entry_doi = _normalize_doi(entry.get("doi", ""))
265	            if entry_doi and entry_doi == cand_doi:
266	                return key
267	        if cand_title:
268	            entry_title = _normalize_title(entry.get("title", ""))
269	            if entry_title and entry_title == cand_title:
270	                return key
271	    return None
272	
273	
274	def _merge_paper(existing: dict, new: dict) -> dict:
275	    """Merge new fields into existing — only fill empty slots, never overwrite.
276	
277	    Verified=True wins over False (a later verification cannot un-verify).
278	    """
279	    merged = dict(existing)
280	    for k, v in new.items():
281	        if v is None or v == "" or v == []:
282	            continue
283	        if k == "verified":
284	            merged["verified"] = bool(existing.get("verified")) or bool(v)
285	            continue
286	        if not merged.get(k):
287	            merged[k] = v
288	    return merged
289	
290	
291	# ---------------------------------------------------------------------------
292	# Public API
293	# ---------------------------------------------------------------------------
294	
295	def read_literature_map(
296	    project: str | None = None,
297	    mode: str = "summary",
298	) -> ToolResult:
299	    """Read the literature map with mode-controlled verbosity.
300	
301	    Args:
302	        project: Project name — None reads the global (idea-phase) map.
303	        mode:
304	          - "summary"        → categories + per-paper {title, year, venue,
305	                                category, role, verified, bibtex_key}
306	          - "category:&lt;key>" → full entries in the named category
307	          - "competitors"    → full entries with role=direct-competitor
308	          - "unverified"     → full entries with verified=False
309	          - "bib"            → list of bibtex_key strings (for citation lookups)
310	          - "full"           → everything (use sparingly — token-heavy)
311	
312	    Returns:
313	        ToolResult.data = {
314	            "categories": [...],
315	            "papers": {key: {...}, ...},
316	            "meta": {"last_updated", "total_papers"},
317	            "mode": &lt;effective mode>,
318	        }
319	    """
320	    path = get_literature_map_path(project)
321	    data = _read_map(path)
322	    papers: dict = data.get("papers", {})
323	    categories: list = data.get("categories", [])
324	
325	    # Category-scoped read: "category:&lt;key>"
326	    if mode.startswith("category:"):
327	        cat_key = mode.split(":", 1)[1].strip()
328	        filtered = {k: v for k, v in papers.items() if v.get("category") == cat_key}
329	        return ToolResult(success=True, data={
330	            "categories": [c for c in categories if c.get("key") == cat_key],
331	            "papers": filtered,
332	            "meta": data.get("meta", {}),
333	            "mode": mode,
334	        })
335	
336	    if mode not in VALID_READ_MODES:
337	        return ToolResult(
338	            success=False,
339	            error=(
340	                f"Unknown mode '{mode}'. Valid: {sorted(VALID_READ_MODES)} "
341	                "or 'category:&lt;key>'."
342	            ),
343	        )
344	
345	    if mode == "summary":
346	        compact = {
347	            k: {f: v.get(f) for f in _SUMMARY_FIELDS if f in v}
348	            for k, v in papers.items()
349	        }
350	        return ToolResult(success=True, data={
351	            "categories": categories,
352	            "papers": compact,
353	            "meta": data.get("meta", {}),
354	            "mode": mode,
355	        })
356	
357	    if mode == "competitors":
358	        filtered = {k: v for k, v in papers.items() if v.get("role") == "direct-competitor"}
359	        return ToolResult(success=True, data={
360	            "categories": categories,
361	            "papers": filtered,
362	            "meta": data.get("meta", {}),
363	            "mode": mode,
364	        })
365	
366	    if mode == "unverified":
367	        filtered = {k: v for k, v in papers.items() if not v.get("verified")}
368	        return ToolResult(success=True, data={
369	            "categories": categories,
370	            "papers": filtered,
371	            "meta": data.get("meta", {}),
372	            "mode": mode,
373	        })
374	
375	    if mode == "bib":
376	        keys = [v.get("bibtex_key") or k for k, v in papers.items()]
377	        return ToolResult(success=True, data={
378	            "bibtex_keys": keys,
379	            "meta": data.get("meta", {}),
380	            "mode": mode,
381	        })
382	
383	    # mode == "full"
384	    return ToolResult(success=True, data={
385	        "categories": categories,
386	        "papers": papers,
387	        "meta": data.get("meta", {}),
388	        "mode": mode,
389	    })
390	
391	
392	def add_to_literature_map(
393	    project: str | None = None,
394	    papers: Iterable[dict] | None = None,
395	    added_by: str = "",
396	) -> ToolResult:
397	    """Add (or merge) one or more papers into the literature map.
398	
399	    Dedup: DOI exact (normalized) → normalized title → bibtex_key collision.
400	    Existing entries are merged field-by-field, never overwritten.
401	
402	    Args:
403	        project: Project name — None writes to the global (idea-phase) map.
404	        papers: Iterable of paper dicts. Recognized fields:
405	                title, authors (list[str]), year, venue, url, doi,
406	                bibtex_key, category, role, relevance, abstract,
407	                semantic_scholar_id, source_idea_id, verified.
408	                Missing bibtex_key is auto-generated.
409	        added_by: Free-form tag for provenance ("paper-research",
410	                  "idea-generator", "user", etc.). Recorded on new entries.
411	
412	    Returns:
413	        ToolResult.data = {
414	            "added": [keys],            # newly inserted
415	            "merged": [keys],           # matched existing, fields merged
416	            "rejected": [{title, reason}],
417	            "total_papers": N,
418	        }
419	    """
420	    if not papers:
421	        return ToolResult(
422	            success=False, error="No papers provided.",
423	        )
424	
425	    paper_list = list(papers)
426	    added: list[str] = []
427	    merged: list[str] = []
428	    rejected: list[dict] = []
429	    now = _paths.now_iso()
430	
431	    def _apply(data: dict) -> None:
432	        existing = data.setdefault("papers", {})
433	        for cand in paper_list:
434	            if not isinstance(cand, dict):
435	                rejected.append({"title": str(cand), "reason": "not a dict"})
436	                continue
437	            title = (cand.get("title") or "").strip()
438	            if not title:
439	                rejected.append({"title": "", "reason": "missing title"})
440	                continue
441	            if cand.get("role") and cand["role"] not in VALID_ROLES:
442	                rejected.append({
443	                    "title": title,
444	                    "reason": f"invalid role '{cand['role']}', valid: {sorted(VALID_ROLES)}",
445	                })
446	                continue
447	
448	            existing_key = _find_existing_key(existing, cand)
449	            if existing_key:
450	                # Merge — fill empty fields, keep verified=True if either is True
451	                existing[existing_key] = _merge_paper(existing[existing_key], cand)
452	                merged.append(existing_key)
453	                continue
454	
455	            # New entry — assign a bibtex_key if missing, dedupe within file
456	            key = cand.get("bibtex_key") or _generate_bibtex_key(cand)
457	            base_key = key
458	            suffix = 1
459	            while key in existing:
460	                suffix += 1
461	                key = f"{base_key}_{suffix}"
462	
463	            entry = {
464	                "title": title,
465	                "authors": cand.get("authors") or [],
466	                "year": cand.get("year"),
467	                "venue": cand.get("venue") or "",
468	                "url": cand.get("url") or "",
469	                "doi": cand.get("doi") or "",
470	                "bibtex_key": key,
471	                "category": cand.get("category") or "",
472	                "role": cand.get("role") or "",
473	                "relevance": cand.get("relevance") or "",
474	                "abstract": cand.get("abstract") or "",
475	                "semantic_scholar_id": cand.get("semantic_scholar_id") or "",
476	                "verified": bool(cand.get("verified", False)),
477	                "added_by": cand.get("added_by") or added_by or "",
478	                "added_at": cand.get("added_at") or now,
479	            }
480	            # Optional source_idea_id (global map only) — keep if present
481	            if cand.get("source_idea_id"):
482	                entry["source_idea_id"] = cand["source_idea_id"]
483	
484	            existing[key] = entry
485	            added.append(key)
486	
487	    data = _read_modify_write(get_literature_map_path(project), _apply)
488	
489	    return ToolResult(success=True, data={
490	        "added": added,
491	        "merged": merged,
492	        "rejected": rejected,
493	        "total_papers": data["meta"]["total_papers"],
494	    })
495	
496	
497	def update_literature_category(
498	    paper_key: str,
499	    project: str | None = None,
500	    category: str | None = None,
501	    role: str | None = None,
502	    relevance: str | None = None,
503	    verified: bool | None = None,
504	) -> ToolResult:
505	    """Update a single paper's classification fields.
506	
507	    Only the fields you pass are changed — others are left intact. This is
508	    the preferred path for "re-classify this paper after reading it" or
509	    "mark verified=true after OpenAlex check" — it's smaller than rewriting
510	    the whole entry via add_to_literature_map.
511	
512	    Args:
513	        paper_key: The YAML key of the paper (e.g. "vaswani2017attention").
514	        project: Project name — None updates the global map.
515	        category: New category key (must match a categories[].key, or empty).
516	        role: New role (must be in VALID_ROLES, or empty to clear).
517	        relevance: One-line relevance description.
518	        verified: Mark verified/unverified (e.g. after OpenAlex check).
519	
520	    Returns:
521	        ToolResult.data = {"paper_key", "updated_fields": {...}}
522	        ToolResult.error if paper_key not found or role/category invalid.
523	    """
524	    if role is not None and role and role not in VALID_ROLES:
525	        return ToolResult(
526	            success=False,
527	            error=f"invalid role '{role}', valid: {sorted(VALID_ROLES)}",
528	        )
529	
530	    updated: dict[str, Any] = {}
531	    not_found = {"miss": False}
532	
533	    def _apply(data: dict) -> None:
534	        papers = data.setdefault("papers", {})
535	        if paper_key not in papers:
536	            not_found["miss"] = True
537	            return
538	        entry = papers[paper_key]
539	        if category is not None:
540	            entry["category"] = category
541	            updated["category"] = category
542	        if role is not None:
543	            entry["role"] = role
544	            updated["role"] = role
545	        if relevance is not None:
546	            entry["relevance"] = relevance
547	            updated["relevance"] = relevance
548	        if verified is not None:
549	            entry["verified"] = bool(verified)
550	            updated["verified"] = bool(verified)
551	
552	    _read_modify_write(get_literature_map_path(project), _apply)
553	
554	    if not_found["miss"]:
555	        return ToolResult(
556	            success=False,
557	            error=f"paper_key '{paper_key}' not found in literature_map",
558	        )
559	    return ToolResult(success=True, data={
560	        "paper_key": paper_key,
561	        "updated_fields": updated,
562	    })
563	
564	
565	def upsert_category(
566	    project: str | None = None,
567	    key: str = "",
568	    name: str = "",
569	    narrative: str = "",
570	) -> ToolResult:
571	    """Add or update a category entry in the categories[] list.
572	
573	    Categories define the Related Work subsection structure. A paper's
574	    ``category`` field references one of these by ``key``.
575	
576	    Args:
577	        project: Project name — None edits the global map.
578	        key: Category slug (e.g. "attention_mechanisms"). Required.
579	        name: Human-readable name (e.g. "Attention Mechanisms"). Required for new.
580	        narrative: One-line description of the category's narrative arc.
581	
582	    Returns:
583	        ToolResult.data = {"key", "action": "added"|"updated"}.
584	    """
585	    if not key:
586	        return ToolResult(success=False, error="key is required")
587	
588	    state = {"action": "added"}
589	
590	    def _apply(data: dict) -> None:
591	        cats = data.setdefault("categories", [])
592	        for c in cats:
593	            if c.get("key") == key:
594	                if name:
595	                    c["name"] = name
596	                if narrative:
597	                    c["narrative"] = narrative
598	                state["action"] = "updated"
599	                return
600	        cats.append({"key": key, "name": name or key, "narrative": narrative})
601	
602	    _read_modify_write(get_literature_map_path(project), _apply)
603	    return ToolResult(success=True, data={"key": key, "action": state["action"]})
604	
605	
606	def seed_literature_map(
607	    project: str,
608	    seed_papers: Iterable[dict],
609	    source_idea_id: str = "",
610	) -> ToolResult:
611	    """Bulk-seed a new project's literature_map from an idea's accumulated papers.
612	
613	    Called by the idea→project bootstrap hook. Each seed paper is added with
614	    ``added_by="idea_generator"`` so downstream consumers can distinguish
615	    seed papers from those discovered during research.
616	
617	    Args:
618	        project: Project name (required — seeding without a project is the
619	                 global map case, handled by add_to_literature_map directly).
620	        seed_papers: Iterable of paper dicts (same schema as add_to_literature_map).
621	        source_idea_id: Idea ID these papers came from. Stamped on entries so
622	                        a future "re-seed from idea" can find them.
623	
624	    Returns:
625	        Same shape as add_to_literature_map.
626	    """
627	    if not project:
628	        return ToolResult(success=False, error="project is required for seed_literature_map")
629	
630	    seeds = []
631	    for p in seed_papers:
632	        if not isinstance(p, dict):
633	            continue
634	        p2 = dict(p)
635	        if source_idea_id:
636	            p2.setdefault("source_idea_id", source_idea_id)
637	        seeds.append(p2)
638	
639	    return add_to_literature_map(
640	        project=project, papers=seeds, added_by="idea_generator",
641	    )
642	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01HEMacAuxLS4KWqW5b4EsLA",
  "session_id": "ca6fa12b-f060-44ff-a3f8-2be93538cabe",
  "uuid": "c595bed7-5ecf-41e7-be15-3b0cd830a9e0"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-21T03:47:46.602Z_

<details><summary>↩ Tool result · `toolu_01HEneRTG7YQi7qxybzZuni1`</summary>

```text
1	categories:
2	- key: contamination_detection
3	  name: Benchmark Contamination Detection
4	  narrative: Methods for detecting training data contamination in LLM benchmarks,
5	    including RL-robust approaches
6	- key: irt_equating
7	  name: IRT Methodology & Equating
8	  narrative: Item Response Theory models, calibration, equating, and their application
9	    to LLM evaluation
10	- key: benchmark_design
11	  name: Dynamic Benchmark Design
12	  narrative: Approaches for creating contamination-resistant or self-updating benchmarks
13	- key: dif_methodology
14	  name: DIF Statistical Methods
15	  narrative: Differential Item Functioning detection methods, power analysis, and
16	    small-sample strategies
17	- key: item_generation
18	  name: Automated Item Generation
19	  narrative: LLM-based test item generation with difficulty control and psychometric
20	    validation
21	meta:
22	  last_updated: '2026-05-21T03:43:39.944Z'
23	  total_papers: 40
24	papers:
25	  balloccu2024leak:
26	    abstract: ''
27	    added_at: '2026-05-21T01:40:37.987Z'
28	    added_by: literature-gap-fill
29	    authors:
30	    - Balloccu, S.
31	    - Schmidtova, P.
32	    - Lango, M.
33	    - Dusek, O.
34	    bibtex_key: balloccu2024leak
35	    category: contamination_detection
36	    doi: 10.18653/v1/2024.eacl-long.5
37	    relevance: Systematic survey of data leakage in closed-source LLMs covering 255
38	      papers and 263 benchmarks; establishes scope of contamination problem motivating
39	      our detection approach
40	    role: foundation
41	    semantic_scholar_id: 798feda076ad710df65d509a7884bd15937c8056
42	    title: 'Leak, Cheat, Repeat: Data Contamination and Evaluation Malpractices in
43	      Closed-Source LLMs'
44	    url: https://arxiv.org/abs/2402.03927
45	    venue: EACL 2024
46	    verified: true
47	    year: 2024
48	  belzak2020smallsample:
49	    abstract: ''
50	    added_at: '2026-05-20T17:30:00.000Z'
51	    added_by: director
52	    authors:
53	    - Belzak, W.
54	    bibtex_key: belzak2020smallsample
55	    category: dif_methodology
56	    doi: 10.1080/00273171.2019.1671162
57	    relevance: Parsimonious logistic regression with sum scores outperforms complex
58	      IRT models for DIF detection in small samples; directly applicable to our N=50-80
59	      model cohorts
60	    role: method-component
61	    semantic_scholar_id: 8f13882b6f37be1ade68c40539156277e5723395
62	    title: Testing Differential Item Functioning in Small Samples
63	    url: https://www.tandfonline.com/doi/abs/10.1080/00273171.2019.1671162
64	    venue: Multivariate Behavioral Research
65	    verified: true
66	    year: 2020
67	  dekoninck2024constat:
68	    abstract: ''
69	    added_at: '2026-05-21T01:40:37.987Z'
70	    added_by: literature-gap-fill
71	    authors:
72	    - Dekoninck, J.
73	    - Mueller, M. N.
74	    - Vechev, M.
75	    bibtex_key: dekoninck2024constat
76	    category: contamination_detection
77	    doi: ''
78	    relevance: Performance-based contamination detection via perturbation analysis;
79	      closest methodological parallel to our DIF approach in using behavioral patterns
80	      rather than memorization signals
81	    role: direct-competitor
82	    semantic_scholar_id: ''
83	    title: 'ConStat: Performance-Based Contamination Detection in Large Language Models'
84	    url: https://arxiv.org/abs/2405.16281
85	    venue: NeurIPS 2024
86	    verified: true
87	    year: 2024
88	  golchin2024timetravel:
89	    abstract: ''
90	    added_at: '2026-05-21T01:40:37.987Z'
91	    added_by: literature-gap-fill
92	    authors:
93	    - Golchin, S.
94	    - Surdeanu, M.
95	    bibtex_key: golchin2024timetravel
96	    category: contamination_detection
97	    doi: ''
98	    relevance: Instance-level contamination detection via guided completion prompts;
99	      baseline approach for individual-item detection that our group-level DIF method
100	      extends
101	    role: method-component
102	    semantic_scholar_id: d6d0fd994f37b630f35945736b5e1bb198148404
103	    title: 'Time Travel in LLMs: Tracing Data Contamination in Large Language Models'
104	    url: https://arxiv.org/abs/2308.08493
105	    venue: ICLR 2024
106	    verified: true
107	    year: 2024
108	  hardy2026scalability:
109	    abstract: ''
110	    added_at: '2026-05-20T17:30:00.000Z'
111	    added_by: director
112	    authors:
113	    - Hardy, M.
114	    - Gilbert, J.
115	    - Domingue, B.
116	    bibtex_key: hardy2026scalability
117	    category: irt_equating
118	    doi: 10.48550/arXiv.2603.24999
119	    relevance: Nonparametric signed isotonic R2 scalability coefficients outperform
120	      IRT item diagnostics; lightweight pre-filter for item quality before our parametric
121	      calibration
122	    role: method-component
123	    semantic_scholar_id: ''
124	    title: Efficient Detection of Bad Benchmark Items with Novel Scalability Coefficients
125	    url: https://arxiv.org/abs/2603.24999
126	    venue: arXiv
127	    verified: true
128	    year: 2026
129	  kim2019fpc:
130	    abstract: ''
131	    added_at: '2026-05-20T17:30:00.000Z'
132	    added_by: director
133	    authors:
134	    - Kim, S.
135	    - Kolen, M.
136	    bibtex_key: kim2019fpc
137	    category: irt_equating
138	    doi: 10.1080/08957347.2019.1660344
139	    relevance: Fixed-parameter calibration requires only N>=200 vs N>=500 for full
140	      calibration; core methodology for our bifactor IRT equating with anchor items
141	    role: method-component
142	    semantic_scholar_id: ''
143	    title: Application of IRT Fixed Parameter Calibration to Multiple-Group Test Data
144	    url: https://www.tandfonline.com/doi/abs/10.1080/08957347.2019.1660344
145	    venue: Applied Measurement in Education
146	    verified: true
147	    year: 2019
148	  li2024contamination:
149	    abstract: ''
150	    added_at: '2026-05-21T01:40:37.987Z'
151	    added_by: literature-gap-fill
152	    authors:
153	    - Li, Y.
154	    - Guo, Y.
155	    - Guerin, F.
156	    - Lin, C.
157	    bibtex_key: li2024contamination
158	    category: contamination_detection
159	    doi: 10.18653/v1/2024.findings-emnlp.30
160	    relevance: Provides web-overlap contamination labels for MMLU and other benchmarks
161	      via Common Crawl matching; primary ground-truth comparison for our DIF-based
162	      contamination detection
163	    role: foundation
164	    semantic_scholar_id: 32e11cf020021c225782a3b77b5cfed4ae8e14a0
165	    title: An Open-Source Data Contamination Report for Large Language Models
166	    url: https://aclanthology.org/2024.findings-emnlp.30/
167	    venue: Findings of EMNLP 2024
168	    verified: true
169	    year: 2024
170	  liang2026dvd:
171	    abstract: ''
172	    added_at: '2026-05-20T17:30:00.000Z'
173	    added_by: director
174	    authors:
175	    - Liang, R.
176	    bibtex_key: liang2026dvd
177	    category: contamination_detection
178	    doi: ''
179	    relevance: Detects variant contamination via generation variance (AUC 0.73-0.74
180	      vs Min-K++ 0.43-0.68); complementary signal in our ensemble but untested under
181	      RL training
182	    role: direct-competitor
183	    semantic_scholar_id: ''
184	    title: 'DVD: Detection via Variance of Generation Distribution for Variant Contamination'
185	    url: https://arxiv.org/abs/2601.04895
186	    venue: arXiv
187	    verified: true
188	    year: 2026
189	  shi2024mink:
190	    abstract: ''
191	    added_at: '2026-05-21T01:40:37.987Z'
192	    added_by: literature-gap-fill
193	    authors:
194	    - Shi, W.
195	    - Ajith, A.
196	    - Xia, M.
197	    - Huang, Y.
198	    - Liu, D.
199	    - Blevins, T.
200	    - Chen, D.
201	    - Zettlemoyer, L.
202	    bibtex_key: shi2024mink
203	    category: contamination_detection
204	    doi: ''
205	    relevance: Introduces Min-K% Prob method and WikiMIA benchmark for pretraining
206	      data detection; key baseline whose limitations under RL training motivate our
207	      DIF-based alternative
208	    role: foundation
209	    semantic_scholar_id: 3422d5e0cdfdc935d6a84a1e3d3f96659265fe3a
210	    title: Detecting Pretraining Data from Large Language Models
211	    url: https://arxiv.org/abs/2310.16789
212	    venue: ICLR 2024
213	    verified: true
214	    year: 2024
215	  tao2026selfcritique:
216	    abstract: ''
217	    added_at: '2026-05-20T17:30:00.000Z'
218	    added_by: director
219	    authors:
220	    - Tao, Y.
221	    bibtex_key: tao2026selfcritique
222	    category: contamination_detection
223	    doi: ''
224	    relevance: Self-Critique/RL-MIA partially addresses RL concealment via policy-collapse
225	      detection, but remains individual-model-level; our DIF is group-level and complementary
226	    role: direct-competitor
227	    semantic_scholar_id: ''
228	    title: Detecting Data Contamination from Reinforcement Learning Post-training
229	      for Large Language Models
230	    url: https://arxiv.org/abs/2510.09259
231	    venue: ICLR 2026
232	    verified: true
233	    year: 2026
234	  wang2026fragility:
235	    abstract: ''
236	    added_at: '2026-05-20T17:30:00.000Z'
237	    added_by: director
238	    authors:
239	    - Wang, H.
240	    - Li, H.
241	    - Ko, B.
242	    - Zhang, H.
243	    bibtex_key: wang2026fragility
244	    category: contamination_detection
245	    doi: ''
246	    relevance: Proves GRPO/PPO RL training conceals contamination signals (14-20pp
247	      AUROC degradation), motivating our DIF-based approach which operates on behavioral
248	      patterns immune to NLL smoothing
249	    role: foundation
250	    semantic_scholar_id: 9a5bf5d3c7116cc4a104c06599fbcef2d1b5abf3
251	    title: On The Fragility of Benchmark Contamination Detection in Reasoning Models
252	    url: https://arxiv.org/abs/2510.02386
253	    venue: ICLR 2026
254	    verified: true
255	    year: 2026
256	  white2025livebench:
257	    abstract: ''
258	    added_at: '2026-05-20T17:30:00.000Z'
259	    added_by: director
260	    authors:
261	    - White, C.
262	    bibtex_key: white2025livebench
263	    category: benchmark_design
264	    doi: 10.48550/arXiv.2406.19314
265	    relevance: Monthly-updated contamination-free benchmark with objective scoring;
266	      no difficulty calibration or psychometric equivalence across updates
267	    role: direct-competitor
268	    semantic_scholar_id: 4e5d86ea8eacd341d13123852d50d1ef62738744
269	    title: 'LiveBench: A Challenging, Contamination-Free LLM Benchmark'
270	    url: https://arxiv.org/abs/2406.19314
271	    venue: ICLR 2025
272	    verified: true
273	    year: 2025
274	  zhang2024gsm1k:
275	    abstract: ''
276	    added_at: '2026-05-20T17:30:00.000Z'
277	    added_by: director
278	    authors:
279	    - Zhang, H.
280	    bibtex_key: zhang2024gsm1k
281	    category: contamination_detection
282	    doi: ''
283	    relevance: GSM1K documents 10-13% average accuracy drops from contamination; provides
284	      ground-truth contamination evidence and item-level effect sizes (delta 0.8-1.4
285	      logits) critical for our DIF power analysis
286	    role: foundation
287	    semantic_scholar_id: ef62f95c16f668f031d649799cbd79081c6d2b0f
288	    title: A Careful Examination of Large Language Model Performance on Grade School
289	      Arithmetic
290	    url: https://arxiv.org/abs/2405.00332
291	    venue: arXiv
292	    verified: true
293	    year: 2024
294	  zhang2024minkpp:
295	    abstract: ''
296	    added_at: '2026-05-21T01:40:37.987Z'
297	    added_by: literature-gap-fill
298	    authors:
299	    - Zhang, J.
300	    - Sun, J.
301	    - Yeats, E.
302	    - Ouyang, Y.
303	    - Kuo, M.
304	    - Zhang, J.
305	    - Yang, H.
306	    - Li, H.
307	    bibtex_key: zhang2024minkpp
308	    category: contamination_detection
309	    doi: ''
310	    relevance: Improves Min-K% with vocabulary-normalized token probabilities; key
311	      baseline whose AUC degrades to 0.43-0.68 on RL-trained models, motivating our
312	      DIF-based alternative
313	    role: direct-competitor
314	    semantic_scholar_id: ''
315	    title: 'Min-K%++: Improved Baseline for Detecting Pre-Training Data from Large
316	      Language Models'
317	    url: https://arxiv.org/abs/2404.02936
318	    venue: arXiv
319	    verified: true
320	    year: 2024
321	  lalor2019irt:
322	    title: 'Learning Latent Parameters without Human Response Patterns: Item Response
323	      Theory with Artificial Crowds'
324	    authors:
325	    - Lalor, J.
326	    - Wu, H.
327	    - Yu, H.
328	    year: 2019
329	    venue: EMNLP-IJCNLP 2019
330	    url: https://aclanthology.org/D19-1434/
331	    doi: 10.18653/v1/D19-1434
332	    bibtex_key: lalor2019irt
333	    category: irt_equating
334	    role: foundation
335	    relevance: Pioneering application of IRT to NLP evaluation using artificial crowds
336	      of DNN models; establishes that IRT parameters from machine response patterns
337	      correlate with human-calibrated parameters
338	    abstract: ''
339	    semantic_scholar_id: df6cd8a8d836e75690141deb732f6d19f0176a2e
340	    verified: true
341	    added_by: literature-gap-fill
342	    added_at: '2026-05-21T02:29:19.632Z'
343	  vania2021irt:
344	    title: Comparing Test Sets with Item Response Theory
345	    authors:
346	    - Vania, C.
347	    - Htut, P.M.
348	    - Huang, W.
349	    - Mungra, D.
350	    - Pang, R.Y.
351	    - Phang, J.
352	    - Liu, H.
353	    - Cho, K.
354	    - Bowman, S.R.
355	    year: 2021
356	    venue: ACL 2021
357	    url: https://aclanthology.org/2021.acl-long.92/
358	    doi: 10.18653/v1/2021.acl-long.92
359	    bibtex_key: vania2021irt
360	    category: irt_equating
361	    role: foundation
362	    relevance: IRT-based analysis of NLU benchmark discriminability; shows which test
363	      sets remain effective at differentiating strong models and which are saturated
364	    abstract: ''
365	    semantic_scholar_id: 4ca39cf99747b8962fe37e7e025e284872df3425
366	    verified: true
367	    added_by: literature-gap-fill
368	    added_at: '2026-05-21T02:29:19.632Z'
369	  li2025atlas:
370	    title: 'Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static
371	      Benchmarks'
372	    authors:
373	    - Li, P.
374	    - Tang, X.
375	    - Chen, S.
376	    - Cheng, Y.
377	    - Metoyer, R.
378	    - Hua, T.
379	    - Chawla, N.V.
380	    year: 2025
381	    venue: arXiv
382	    url: https://arxiv.org/abs/2511.04689
383	    doi: 10.48550/arXiv.2511.04689
384	    bibtex_key: li2025atlas
385	    category: irt_equating
386	    role: method-component
387	    relevance: IRT-based adaptive testing framework (ATLAS) reduces benchmark items
388	      by 90% while preserving ability estimates; demonstrates IRT enables efficient
389	      LLM evaluation
390	    abstract: ''
391	    semantic_scholar_id: 087ce2837a0d5562bc95a40e77a327a6d033366c
392	    verified: true
393	    added_by: literature-gap-fill
394	    added_at: '2026-05-21T02:29:19.632Z'
395	  chen2025irtnet:
396	    title: Learning Compact Representations of LLM Abilities via Item Response Theory
397	    authors:
398	    - Chen, J.
399	    - Wang, C.
400	    - Zhang, G.
401	    - Ye, P.
402	    - Bai, L.
403	    - Hu, W.
404	    - Qu, Y.
405	    - Hu, S.
406	    year: 2025
407	    venue: arXiv
408	    url: https://arxiv.org/abs/2510.00844
409	    doi: 10.48550/arXiv.2510.00844
410	    bibtex_key: chen2025irtnet
411	    category: irt_equating
412	    role: method-component
413	    relevance: Multidimensional IRT with MoE network for learning LLM ability vectors
414	      and query discrimination/difficulty; demonstrates IRT-based model routing and
415	      benchmark prediction
416	    abstract: ''
417	    semantic_scholar_id: ''
418	    verified: true
419	    added_by: literature-gap-fill
420	    added_at: '2026-05-21T02:29:19.632Z'
421	  choi2026llmjudgeirt:
422	    title: Diagnosing the Reliability of LLM-as-a-Judge via Item Response Theory
423	    authors:
424	    - Choi, J.
425	    - Park, S.
426	    - Cho, C.
427	    - Park, H.
428	    - Kim, B.
429	    year: 2026
430	    venue: arXiv
431	    url: https://arxiv.org/abs/2602.00521
432	    doi: 10.48550/arXiv.2602.00521
433	    bibtex_key: choi2026llmjudgeirt
434	    category: irt_equating
435	    role: method-component
436	    relevance: Applies IRT Graded Response Model to diagnose LLM judge reliability;
437	      extends IRT application beyond benchmark scoring to evaluation pipeline quality
438	      assessment
439	    abstract: ''
440	    semantic_scholar_id: 4fc931a456c8162716deadbc9db6fd770189e632
441	    verified: true
442	    added_by: literature-gap-fill
443	    added_at: '2026-05-21T02:29:19.632Z'
444	  holland1988mh:
445	    title: Differential Item Functioning and the Mantel-Haenszel Procedure
446	    authors:
447	    - Holland, P.W.
448	    - Thayer, D.T.
449	    year: 1988
450	    venue: In H. Wainer & H.I. Braun (Eds.), Test Validity, Lawrence Erlbaum
451	    url: https://onlinelibrary.wiley.com/doi/abs/10.1002/j.2330-8516.1986.tb00186.x
452	    doi: 10.1002/j.2330-8516.1986.tb00186.x
453	    bibtex_key: holland1988mh
454	    category: dif_methodology
455	    role: foundation
456	    relevance: Seminal paper introducing the Mantel-Haenszel procedure for DIF detection;
457	      establishes the ETS classification system (A/B/C) used as standard DIF effect-size
458	      metric
459	    abstract: ''
460	    semantic_scholar_id: 5fbc064e7104036b77a2bf6f0ad509031965c275
461	    verified: true
462	    added_by: literature-gap-fill
463	    added_at: '2026-05-21T03:21:36.315Z'
464	  shealy1993sibtest:
465	    title: A Model-Based Standardization Approach that Separates True Bias/DIF from
466	      Group Ability Differences and Detects Test Bias/DTF as Well as Item Bias/DIF
467	    authors:
468	    - Shealy, R.
469	    - Stout, W.
470	    year: 1993
471	    venue: Psychometrika
472	    url: https://link.springer.com/article/10.1007/BF02294572
473	    doi: 10.1007/BF02294572
474	    bibtex_key: shealy1993sibtest
475	    category: dif_methodology
476	    role: foundation
477	    relevance: Introduces SIBTEST, a nonparametric DIF detection method that separates
478	      true item bias from group ability differences; alternative to MH that handles
479	      non-uniform DIF
480	    abstract: ''
481	    semantic_scholar_id: 82f3db496626afd828fedb01a41f719a50dbfc2c
482	    verified: true
483	    added_by: literature-gap-fill
484	    added_at: '2026-05-21T03:21:36.315Z'
485	  clauser1998dif:
486	    title: Using Statistical Procedures to Identify Differentially Functioning Test
487	      Items
488	    authors:
489	    - Clauser, B.E.
490	    - Mazor, K.M.
491	    year: 1998
492	    venue: 'Educational Measurement: Issues and Practice'
493	    url: https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1745-3992.1998.tb00619.x
494	    doi: 10.1111/j.1745-3992.1998.tb00619.x
495	    bibtex_key: clauser1998dif
496	    category: dif_methodology
497	    role: foundation
498	    relevance: Comprehensive review of DIF detection methods (MH, SIBTEST, logistic
499	      regression, IRT-based); standard reference for comparing statistical approaches
500	      to DIF
501	    abstract: ''
502	    semantic_scholar_id: c2377c505c95b924e972e61dadec81e9c87dea18
503	    verified: true
504	    added_by: literature-gap-fill
505	    added_at: '2026-05-21T03:21:36.315Z'
506	  zumbo1999handbook:
507	    title: 'A Handbook on the Theory and Methods of Differential Item Functioning
508	      (DIF): Logistic Regression Modeling as a Unitary Framework for Binary and Likert-Type
509	      (Ordinal) Item Scores'
510	    authors:
511	    - Zumbo, B.D.
512	    year: 1999
513	    venue: 'Ottawa: Directorate of Human Resources Research and Evaluation, Department
514	      of National Defense'
515	    url: https://faculty.educ.ubc.ca/zumbo/DIF/handbook.pdf
516	    doi: ''
517	    bibtex_key: zumbo1999handbook
518	    category: dif_methodology
519	    role: foundation
520	    relevance: Foundational DIF handbook presenting logistic regression as a unitary
521	      framework for DIF analysis; establishes the Zumbo-Thomas logistic regression
522	      approach widely used in applied DIF research
523	    abstract: ''
524	    semantic_scholar_id: 7f88fb0ad98645582665532600d7c46406fa2db6
525	    verified: true
526	    added_by: literature-gap-fill
527	    added_at: '2026-05-21T03:21:36.315Z'
528	  meredith1993invariance:
529	    title: Measurement Invariance, Factor Analysis and Factorial Invariance
530	    authors:
531	    - Meredith, W.
532	    year: 1993
533	    venue: Psychometrika
534	    url: https://link.springer.com/article/10.1007/BF02294825
535	    doi: 10.1007/BF02294825
536	    bibtex_key: meredith1993invariance
537	    category: dif_methodology
538	    role: foundation
539	    relevance: Defines the measurement invariance hierarchy (configural, metric, scalar,
540	      strict factorial invariance); theoretical foundation linking DIF to latent variable
541	      fairness
542	    abstract: ''
543	    semantic_scholar_id: 7eb541983de0a39586a699e255563b26e9291340
544	    verified: true
545	    added_by: literature-gap-fill
546	    added_at: '2026-05-21T03:21:36.315Z'
547	  vandenberg2000invariance:
548	    title: 'A Review and Synthesis of the Measurement Invariance Literature: Suggestions,
549	      Practices, and Recommendations for Organizational Research'
550	    authors:
551	    - Vandenberg, R.J.
552	    - Lance, C.E.
553	    year: 2000
554	    venue: Organizational Research Methods
555	    url: https://journals.sagepub.com/doi/10.1177/109442810031002
556	    doi: 10.1177/109442810031002
557	    bibtex_key: vandenberg2000invariance
558	    category: dif_methodology
559	    role: foundation
560	    relevance: Comprehensive review of measurement invariance testing practices; establishes
561	      CFA-based invariance testing as prerequisite for valid cross-group comparisons,
562	      analogous to our cross-model DIF analysis
563	    abstract: ''
564	    semantic_scholar_id: 1c9389250c1fac06eda5dcf39a8ea16cf8c92c89
565	    verified: true
566	    added_by: literature-gap-fill
567	    added_at: '2026-05-21T03:21:36.315Z'
568	  swaminathan1990logistic:
569	    title: Detecting Differential Item Functioning Using Logistic Regression Procedures
570	    authors:
571	    - Swaminathan, H.
572	    - Rogers, H.J.
573	    year: 1990
574	    venue: Journal of Educational Measurement
575	    url: https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1745-3984.1990.tb00754.x
576	    doi: 10.1111/j.1745-3984.1990.tb00754.x
577	    bibtex_key: swaminathan1990logistic
578	    category: dif_methodology
579	    role: foundation
580	    relevance: Introduces logistic regression for DIF detection, distinguishing uniform
581	      and non-uniform DIF; more powerful than MH for non-uniform DIF and directly
582	      applicable to our contamination-as-DIF framework
583	    abstract: ''
584	    semantic_scholar_id: d14b3b6e927ff8e51406fad1010244ecabc07da0
585	    verified: true
586	    added_by: literature-gap-fill
587	    added_at: '2026-05-21T03:21:36.315Z'
588	  teresi2007dif:
589	    title: Differential Item Functioning and Health Assessment
590	    authors:
591	    - Teresi, J.A.
592	    - Fleishman, J.A.
593	    year: 2007
594	    venue: Quality of Life Research
595	    url: https://link.springer.com/article/10.1007/s11136-007-9184-6
596	    doi: 10.1007/s11136-007-9184-6
597	    bibtex_key: teresi2007dif
598	    category: dif_methodology
599	    role: method-component
600	    relevance: Reviews DIF detection strategies including propensity score matching
601	      approaches for controlling confounders; methodological basis for our propensity-matched
602	      contamination group comparison
603	    abstract: ''
604	    semantic_scholar_id: 5ddbe080c2c0cdff671d9b9c2a795e366b6eb098
605	    verified: true
606	    added_by: literature-gap-fill
607	    added_at: '2026-05-21T03:21:36.315Z'
608	  lord1980irt:
609	    title: Applications of Item Response Theory to Practical Testing Problems
610	    authors:
611	    - Lord, F.M.
612	    year: 1980
613	    venue: 'Hillsdale, NJ: Lawrence Erlbaum Associates'
614	    url: https://www.routledge.com/Applications-of-Item-Response-Theory-To-Practical-Testing-Problems/Lord/p/book/9780898590067
615	    doi: ''
616	    bibtex_key: lord1980irt
617	    category: dif_methodology
618	    role: foundation
619	    relevance: Introduces Lord's chi-square test for IRT-based DIF detection by comparing
620	      item parameters across groups; foundational IRT reference for our parametric
621	      DIF approach
622	    abstract: ''
623	    semantic_scholar_id: ''
624	    verified: true
625	    added_by: literature-gap-fill
626	    added_at: '2026-05-21T03:21:36.315Z'
627	  raju1988area:
628	    title: The Area between Two Item Characteristic Curves
629	    authors:
630	    - Raju, N.S.
631	    year: 1988
632	    venue: Psychometrika
633	    url: https://link.springer.com/article/10.1007/BF02294403
634	    doi: 10.1007/BF02294403
635	    bibtex_key: raju1988area
636	    category: dif_methodology
637	    role: method-component
638	    relevance: Develops signed and unsigned area measures between item characteristic
639	      curves for IRT-based DIF quantification; provides effect-size metrics complementing
640	      statistical significance tests
641	    abstract: ''
642	    semantic_scholar_id: 545c20c1f2575833f81418f4757cb78446465cd7
643	    verified: true
644	    added_by: literature-gap-fill
645	    added_at: '2026-05-21T03:21:36.315Z'
646	  muthen1985mimic:
647	    title: A Method for Studying the Homogeneity of Test Items with Respect to Other
648	      Relevant Variables
649	    authors:
650	    - Muthén, B.
651	    year: 1985
652	    venue: Journal of Educational Statistics
653	    url: ''
654	    doi: 10.2307/1164966
655	    bibtex_key: muthen1985mimic
656	    category: dif_methodology
657	    role: method-component
658	    relevance: Seminal MIMIC model for DIF with continuous covariates; future-work
659	      alternative to failed θ-conditioning (plan_012)
660	    abstract: ''
661	    semantic_scholar_id: ''
662	    verified: true
663	    added_by: paper_agent
664	    added_at: '2026-05-21T03:34:08.189Z'
665	  woods2009mimic:
666	    title: Empirical Selection of Anchors for Tests of Differential Item Functioning
667	    authors:
668	    - Woods, C.M.
669	    year: 2009
670	    venue: Applied Psychological Measurement
671	    url: ''
672	    doi: 10.1177/0146621609331279
673	    bibtex_key: woods2009mimic
674	    category: dif_methodology
675	    role: method-component
676	    relevance: Modern MIMIC-based DIF detection with anchor selection; addresses impact-vs-DIF
677	      confound in our future work
678	    abstract: ''
679	    semantic_scholar_id: ''
680	    verified: true
681	    added_by: paper_agent
682	    added_at: '2026-05-21T03:34:08.189Z'
683	  habba2026growingpains:
684	    abstract: ''
685	    added_at: '2026-05-20T17:30:00.000Z'
686	    added_by: director
687	    authors:
688	    - Habba, E.
689	    - Itzhak, I.
690	    - Yehudai, A.
691	    - Perlitz, Y.
692	    - Bandel, E.
693	    - Shmueli-Scheuer, M.
694	    - Choshen, L.
695	    - Stanovsky, G.
696	    bibtex_key: habba2026growingpains
697	    category: irt_equating
698	    doi: 10.48550/arXiv.2604.12843
699	    relevance: Uses multidimensional IRT with fixed-parameter calibration and 100
700	      anchor items for extensible evaluation (rho>=0.9); addresses score comparability
701	      but NOT contamination detection or item regeneration
702	    role: direct-competitor
703	    semantic_scholar_id: ''
704	    title: 'Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter
705	      Calibration'
706	    url: https://arxiv.org/abs/2604.12843
707	    venue: arXiv
708	    verified: true
709	    year: 2026
710	  zhou2026psnirt:
711	    abstract: ''
712	    added_at: '2026-05-20T17:30:00.000Z'
713	    added_by: director
714	    authors:
715	    - Zhou, H.
716	    - Huang, H.
717	    - Zhao, Z.
718	    - Han, L.
719	    - Wang, H.
720	    - Chen, K.
721	    - Yang, M.
722	    - Bao, W.
723	    - Dong, J.
724	    - Xu, B.
725	    - Zhu, C.
726	    - Cao, H.
727	    - Zhao, T.
728	    bibtex_key: zhou2026psnirt
729	    category: irt_equating
730	    doi: ''
731	    relevance: PSN-IRT analyzes benchmark quality via 4PL IRT; provides published
732	      IRT parameters for MMLU we can use in semi-synthetic validation
733	    role: method-component
734	    semantic_scholar_id: ''
735	    title: Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item
736	      Response Theory
737	    url: https://arxiv.org/abs/2505.15055
738	    venue: AAAI 2026
739	    verified: true
740	    year: 2026
741	  kipnis2024metabench:
742	    title: metabench -- A Sparse Benchmark of Reasoning and Knowledge in Large Language
743	      Models
744	    authors:
745	    - Kipnis, A.
746	    - Voudouris, K.
747	    - Schulze Buschoff, L.M.
748	    - Schulz, E.
749	    year: 2024
750	    venue: arXiv
751	    url: https://arxiv.org/abs/2407.12844
752	    doi: 10.48550/arXiv.2407.12844
753	    bibtex_key: kipnis2024metabench
754	    category: benchmark_design
755	    role: foundation
756	    relevance: Primary data source providing item-level response matrix across 5000+
757	      LLMs on 6 benchmarks; IRT-based item selection methodology enables our DIF analysis
758	      on compressed benchmark items
759	    abstract: ''
760	    semantic_scholar_id: dfd5186def202285a0f23cd3f08415a5780895c1
761	    verified: true
762	    added_by: literature-gap-fill
763	    added_at: '2026-05-21T03:43:39.896Z'
764	  hendrycks2021mmlu:
765	    title: Measuring Massive Multitask Language Understanding
766	    authors:
767	    - Hendrycks, D.
768	    - Burns, C.
769	    - Basart, S.
770	    - Zou, A.
771	    - Mazeika, M.
772	    - Song, D.
773	    - Steinhardt, J.
774	    year: 2021
775	    venue: ICLR 2021
776	    url: https://arxiv.org/abs/2009.03300
777	    doi: ''
778	    bibtex_key: hendrycks2021mmlu
779	    category: benchmark_design
780	    role: foundation
781	    relevance: Seminal 57-subject benchmark for LLM evaluation; primary benchmark
782	      in our DIF analysis due to documented contamination and available IRT parameters
783	    abstract: ''
784	    semantic_scholar_id: 814a4f680b9ba6baba23b93499f4b48af1a27678
785	    verified: true
786	    added_by: literature-gap-fill
787	    added_at: '2026-05-21T03:43:39.896Z'
788	  liang2023helm:
789	    title: Holistic Evaluation of Language Models
790	    authors:
791	    - Liang, P.
792	    - Bommasani, R.
793	    - Lee, T.
794	    - Tsipras, D.
795	    - Soylu, D.
796	    - Yasunaga, M.
797	    - Zhang, Y.
798	    - Narayanan, D.
799	    - Wu, Y.
800	    - Kumar, A.
801	    year: 2023
802	    venue: TMLR 2023
803	    url: https://arxiv.org/abs/2211.09110
804	    doi: 10.1111/nyas.15007
805	    bibtex_key: liang2023helm
806	    category: benchmark_design
807	    role: foundation
808	    relevance: Holistic multi-metric evaluation framework covering accuracy, calibration,
809	      robustness, fairness, and bias; establishes multi-dimensional evaluation philosophy
810	      complementary to our psychometric approach
811	    abstract: ''
812	    semantic_scholar_id: ce913026f693101e54d3ab9152e107034d81fce1
813	    verified: true
814	    added_by: literature-gap-fill
815	    added_at: '2026-05-21T03:43:39.896Z'
816	  chiang2024chatbot:
817	    title: 'Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference'
818	    authors:
819	    - Chiang, W.-L.
820	    - Zheng, L.
821	    - Sheng, Y.
822	    - Angelopoulos, A.N.
823	    - Li, T.
824	    - Li, D.
825	    - Zhang, H.
826	    - Zhu, B.
827	    - Jordan, M.I.
828	    - Gonzalez, J.E.
829	    - Stoica, I.
830	    year: 2024
831	    venue: ICML 2024
832	    url: https://arxiv.org/abs/2403.04132
833	    doi: 10.48550/arXiv.2403.04132
834	    bibtex_key: chiang2024chatbot
835	    category: benchmark_design
836	    role: method-component
837	    relevance: Crowdsourced pairwise comparison with ELO ranking as contamination-resistant
838	      alternative to static benchmarks; contrasts with our item-level psychometric
839	      approach
840	    abstract: ''
841	    semantic_scholar_id: 53f4fb0e9972989194368faf288ff8e3cba5bd60
842	    verified: true
843	    added_by: literature-gap-fill
844	    added_at: '2026-05-21T03:43:39.896Z'
845	  mialon2023gaia:
846	    title: 'GAIA: a benchmark for General AI Assistants'
847	    authors:
848	    - Mialon, G.
849	    - Fourrier, C.
850	    - Swift, C.
851	    - Wolf, T.
852	    - LeCun, Y.
853	    - Scialom, T.
854	    year: 2023
855	    venue: arXiv
856	    url: https://arxiv.org/abs/2311.12983
857	    doi: 10.48550/arXiv.2311.12983
858	    bibtex_key: mialon2023gaia
859	    category: benchmark_design
860	    role: method-component
861	    relevance: Benchmark with verifiable ground-truth answers designed to resist memorization;
862	      exemplifies objective-scoring benchmark design philosophy shared by our regenerated
863	      items
864	    abstract: ''
865	    semantic_scholar_id: ab8169d6e4dfabfe7c30ebec1bb871bf3e1551cd
866	    verified: true
867	    added_by: literature-gap-fill
868	    added_at: '2026-05-21T03:43:39.896Z'
869	  li2024latesteval:
870	    title: 'LatestEval: Addressing Data Contamination in Language Model Evaluation
871	      through Dynamic and Time-Sensitive Test Construction'
872	    authors:
873	    - Li, Y.
874	    - Guerin, F.
875	    - Lin, C.
876	    year: 2024
877	    venue: AAAI 2024
878	    url: https://arxiv.org/abs/2312.12343
879	    doi: 10.48550/arXiv.2312.12343
880	    bibtex_key: li2024latesteval
881	    category: benchmark_design
882	    role: direct-competitor
883	    relevance: Automated dynamic test construction from recent texts to avoid contamination;
884	      addresses temporal contamination but lacks psychometric difficulty calibration
885	      across test versions
886	    abstract: ''
887	    semantic_scholar_id: 8106d03fb984afd8c3d066cd4f993eb2616a0da5
888	    verified: true
889	    added_by: literature-gap-fill
890	    added_at: '2026-05-21T03:43:39.896Z'
891	  kiela2021dynabench:
892	    title: 'Dynabench: Rethinking Benchmarking in NLP'
893	    authors:
894	    - Kiela, D.
895	    - Bartolo, M.
896	    - Nie, Y.
897	    - Kaushik, D.
898	    - Geiger, A.
899	    - Wu, Z.
900	    - Vidgen, B.
901	    - Prasad, G.
902	    - Singh, A.
903	    - Ringshia, P.
904	    - Ma, Z.
905	    - Thrush, T.
906	    - Riedel, S.
907	    - Talat, Z.
908	    - Stenetorp, P.
909	    - Jia, R.
910	    year: 2021
911	    venue: NAACL 2021
912	    url: https://arxiv.org/abs/2104.14337
913	    doi: 10.18653/v1/2021.naacl-main.324
914	    bibtex_key: kiela2021dynabench
915	    category: benchmark_design
916	    role: foundation
917	    relevance: Seminal dynamic adversarial benchmarking platform with human-and-model-in-the-loop
918	      dataset creation; establishes the paradigm of continuously evolving benchmarks
919	      that our IRT-equated regeneration extends with psychometric equivalence guarantees
920	    abstract: ''
921	    semantic_scholar_id: 77a096d80eb4dd4ccd103d1660c5a5498f7d026b
922	    verified: true
923	    added_by: literature-gap-fill
924	    added_at: '2026-05-21T03:43:39.896Z'
925	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01HEMacAuxLS4KWqW5b4EsLA",
  "session_id": "ca6fa12b-f060-44ff-a3f8-2be93538cabe",
  "uuid": "f025be82-87ac-46b6-9c53-12931e6ce645"
}
```

</details>

---

### System

_source line 31_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a5a664161719b85a9",
  "tool_use_id": "toolu_01HEMacAuxLS4KWqW5b4EsLA",
  "status": "completed",
  "output_file": "",
  "summary": "Find literature_map.yaml location",
  "usage": {
    "total_tokens": 50034,
    "tool_uses": 6,
    "duration_ms": 15786
  },
  "uuid": "aa104b26-f492-4daf-85ea-b7172426b864",
  "session_id": "ca6fa12b-f060-44ff-a3f8-2be93538cabe"
}
```

---

### Tool result

_source line 32 · 2026-05-21T03:47:56.740Z_

<details><summary>↩ Tool result · `toolu_01HEMacAuxLS4KWqW5b4EsLA`</summary>

```text
Perfect! I've found and analyzed both files. Here's my report:

## Summary

**Files Found:**

1. **Project literature_map.yaml**: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/literature_map.yaml`
   - Contains 40 verified papers across 5 categories
   - Last updated: 2026-05-21T03:43:39.944Z
   - Categories: contamination_detection, irt_equating, benchmark_design, dif_methodology, item_generation

2. **Literature module**: `/home/ubuntu/agent-ml-research/core/tools/literature.py`
   - Core implementation (~640 lines)
   - Provides persistent, atomic literature map management

## Key Implementation Details

**Data Structure** (literature_map.yaml):
- `meta`: last_updated timestamp, total_papers count
- `categories`: list of {key, name, narrative} for Related Work subsections
- `papers`: dict with entries keyed by bibtex_key (e.g., `balloccu2024leak`)

**Paper Record Schema** (per entry):
- Core metadata: title, authors[], year, venue, url, doi, bibtex_key
- Classification: category, role (foundation|direct-competitor|method-component|evaluation|background), verified
- Research context: relevance, abstract, semantic_scholar_id
- Provenance: added_by, added_at timestamp, optional source_idea_id

**API Functions** (literature.py):
- `read_literature_map(project, mode)` — supports modes: summary, category:X, competitors, unverified, bib, full
- `add_to_literature_map(project, papers, added_by)` — dedup via DOI (exact) or normalized title
- `update_literature_category(paper_key, category, role, relevance, verified)` — partial updates
- `upsert_category(key, name, narrative)` — manage Related Work sections
- `seed_literature_map(project, seed_papers, source_idea_id)` — bulk-seed from ideas

**File I/O** (robust):
- Atomic reads via snapshot mechanism (no tearing under concurrent writes)
- Exclusive flock on .lock file + atomic temp→rename for writers
- Automatic merging (fill-empty-slots, never overwrite) when duplicate detected

**Dedup Strategy**:
- Match order: DOI exact (normalized) → normalized title → bibtex_key collision suffix
- Normalization: lowercase, diacritics removed, punctuation→spaces, whitespace collapsed

The project's 40 papers span contamination detection (Min-K%, DIF methods), IRT equating (fixed-parameter calibration), benchmark design (MMLU, LiveBench), and DIF statistical foundations (Mantel-Haenszel, logistic regression).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ca6fa12b-f060-44ff-a3f8-2be93538cabe",
  "uuid": "53daafd7-f707-4240-b7b7-4b00520bbb42",
  "tool_use_result": {
    "status": "completed",
    "prompt": "Find the literature_map.yaml file in the project directory /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/. Search broadly — it might be in artifacts/, paper/, or root level. Also check if there's a core/tools/literature.py or similar module under /home/ubuntu/agent-ml-research/.",
    "agentId": "a5a664161719b85a9",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! I've found and analyzed both files. Here's my report:\n\n## Summary\n\n**Files Found:**\n\n1. **Project literature_map.yaml**: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/literature_map.yaml`\n   - Contains 40 verified papers across 5 categories\n   - Last updated: 2026-05-21T03:43:39.944Z\n   - Categories: contamination_detection, irt_equating, benchmark_design, dif_methodology, item_generation\n\n2. **Literature module**: `/home/ubuntu/agent-ml-research/core/tools/literature.py`\n   - Core implementation (~640 lines)\n   - Provides persistent, atomic literature map management\n\n## Key Implementation Details\n\n**Data Structure** (literature_map.yaml):\n- `meta`: last_updated timestamp, total_papers count\n- `categories`: list of {key, name, narrative} for Related Work subsections\n- `papers`: dict with entries keyed by bibtex_key (e.g., `balloccu2024leak`)\n\n**Paper Record Schema** (per entry):\n- Core metadata: title, authors[], year, venue, url, doi, bibtex_key\n- Classification: category, role (foundation|direct-competitor|method-component|evaluation|background), verified\n- Research context: relevance, abstract, semantic_scholar_id\n- Provenance: added_by, added_at timestamp, optional source_idea_id\n\n**API Functions** (literature.py):\n- `read_literature_map(project, mode)` — supports modes: summary, category:X, competitors, unverified, bib, full\n- `add_to_literature_map(project, papers, added_by)` — dedup via DOI (exact) or normalized title\n- `update_literature_category(paper_key, category, role, relevance, verified)` — partial updates\n- `upsert_category(key, name, narrative)` — manage Related Work sections\n- `seed_literature_map(project, seed_papers, source_idea_id)` — bulk-seed from ideas\n\n**File I/O** (robust):\n- Atomic reads via snapshot mechanism (no tearing under concurrent writes)\n- Exclusive flock on .lock file + atomic temp→rename for writers\n- Automatic merging (fill-empty-slots, never overwrite) when duplicate detected\n\n**Dedup Strategy**:\n- Match order: DOI exact (normalized) → normalized title → bibtex_key collision suffix\n- Normalization: lowercase, diacritics removed, punctuation→spaces, whitespace collapsed\n\nThe project's 40 papers span contamination detection (Min-K%, DIF methods), IRT equating (fixed-parameter calibration), benchmark design (MMLU, LiveBench), and DIF statistical foundations (Mantel-Haenszel, logistic regression)."
      }
    ],
    "totalDurationMs": 15788,
    "totalTokens": 50700,
    "totalToolUseCount": 6,
    "usage": {
      "input_tokens": 7786,
      "cache_creation_input_tokens": 13095,
      "cache_read_input_tokens": 29134,
      "output_tokens": 685,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 13095
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7786,
          "output_tokens": 685,
          "cache_read_input_tokens": 29134,
          "cache_creation_input_tokens": 13095,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 13095,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 2,
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

_source line 33_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Am4GtMo9wVJgfyqpZdz9Gx`</summary>

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
  "session_id": "ca6fa12b-f060-44ff-a3f8-2be93538cabe",
  "uuid": "f76b945d-eb77-4b1c-8b18-76f2ea652a6f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SdaaEM7d6j8mToNH9F4fFz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 878,
      "cache_read_input_tokens": 25892,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 878
      },
      "output_tokens": 40,
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

_source line 34 · 2026-05-21T03:48:00.059Z_

<details><summary>↩ Tool result · `toolu_01Am4GtMo9wVJgfyqpZdz9Gx`</summary>

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
  "session_id": "ca6fa12b-f060-44ff-a3f8-2be93538cabe",
  "uuid": "cd583edd-17fc-4d8b-b90c-c26868d48e26",
  "tool_use_result": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 51
  }
}
```

</details>

---

### Assistant

_source line 35_

Now let me search for the candidate papers in parallel to verify their metadata.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ca6fa12b-f060-44ff-a3f8-2be93538cabe",
  "uuid": "bccf0ace-a8f9-49cb-8590-7aef198c6bfd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DPPefYXUx2A7jFGe4sDRGU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 602,
      "cache_read_input_tokens": 26770,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 602
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

_source line 36_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YChF3jTba4MkoY7AunmEQV`</summary>

```json
{
  "query": "Burnell et al 2023 \"Rethink Reporting of Evaluation Results in AI\" paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ca6fa12b-f060-44ff-a3f8-2be93538cabe",
  "uuid": "0bd11bc6-0e79-4385-9910-1273e45c8af0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DPPefYXUx2A7jFGe4sDRGU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 602,
      "cache_read_input_tokens": 26770,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 602
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

_source line 37_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01U4hkXGVfpEWqb13k5eKuDn`</summary>

```json
{
  "query": "Chang et al 2024 \"A Survey on Evaluation of Large Language Models\" paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ca6fa12b-f060-44ff-a3f8-2be93538cabe",
  "uuid": "665943bb-0642-4008-802d-960b3a218c4e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DPPefYXUx2A7jFGe4sDRGU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 602,
      "cache_read_input_tokens": 26770,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 602
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

_source line 38_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VEvQEWeimGGwEBbP7L4r45`</summary>

```json
{
  "query": "Polo et al 2024 \"tinyBenchmarks\" efficient evaluation IRT paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ca6fa12b-f060-44ff-a3f8-2be93538cabe",
  "uuid": "242f32de-59f0-4478-b753-8896b09ad826",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DPPefYXUx2A7jFGe4sDRGU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 602,
      "cache_read_input_tokens": 26770,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 602
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

_source line 39_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RCziuRLnE2GuVnTWwAMKMQ`</summary>

```json
{
  "query": "MMLU-Pro Wang et al 2024 benchmark paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ca6fa12b-f060-44ff-a3f8-2be93538cabe",
  "uuid": "5b06a14a-d698-4f1c-8ee4-2d9a4ed3ece2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DPPefYXUx2A7jFGe4sDRGU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 602,
      "cache_read_input_tokens": 26770,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 602
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

_source line 40_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015vydRqX5T3LUkJw6FHacJ7`</summary>

```json
{
  "query": "Ott et al 2022 \"Mapping the Design Space\" evaluation benchmarks NLP"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ca6fa12b-f060-44ff-a3f8-2be93538cabe",
  "uuid": "2582052a-08e5-496c-b158-8efe97cfba12",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DPPefYXUx2A7jFGe4sDRGU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 602,
      "cache_read_input_tokens": 26770,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 602
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

_source line 41 · 2026-05-21T03:48:09.879Z_

<details><summary>↩ Tool result · `toolu_01YChF3jTba4MkoY7AunmEQV`</summary>

```text
Web search results for query: "Burnell et al 2023 "Rethink Reporting of Evaluation Results in AI" paper"

Links: [{"title":"Burnell, R. et al. (2023). Rethink Reporting of Evaluation Results in AI. Science, 380, 136-138. - References - Scientific Research Publishing","url":"https://www.scirp.org/reference/referencespapers?referenceid=3535042"},{"title":"Rethink reporting of evaluation results in AI - White Rose Research Online","url":"https://eprints.whiterose.ac.uk/198211/"},{"title":"Rethink reporting of evaluation results in AI | Science","url":"https://www.science.org/doi/10.1126/science.adf6369"},{"title":"(PDF) Rethink reporting of evaluation results in AI","url":"https://www.researchgate.net/publication/370002303_Rethink_reporting_of_evaluation_results_in_AI"},{"title":"eprints@whiterose.ac.uk https://eprints.whiterose.ac.uk","url":"https://eprints.whiterose.ac.uk/id/eprint/198211/1/Burnell%20et%20al%20-%202023%20-%20Rethink%20reporting%20of%20evaluation%20results%20in%20AI%20(Pre-print).pdf"},{"title":"Rethink reporting of evaluation results in AI Aggregate metrics and lack of access to results limit understanding - Polytechnic University of Valencia","url":"https://panorama.upv.es/en/ipublic/item/10192858"},{"title":"Audit Cards: Contextualizing AI Evaluations","url":"https://arxiv.org/pdf/2504.13839"},{"title":"Rethink reporting of evaluation results in AI","url":"https://ryanburnell.com/wp-content/uploads/Burnell-et-al-2023-Rethink-reporting-of-evaluation-results-in-AI.pdf"},{"title":"Rethink reporting of evaluation results in AI | Montreal AI Ethics Institute","url":"https://montrealethics.ai/rethink-reporting-of-evaluation-results-in-ai/"}]

I found the paper! Here are the key details about the Burnell et al. 2023 paper:

**Publication Details:**
Burnell, R. et al. (2023). Rethink Reporting of Evaluation Results in AI. Science, 380, 136-138.

**DOI:** 10.1126/science.adf6369

**Main Focus:**
The paper addresses how aggregate metrics and lack of access to results limit understanding of AI system evaluation. The paper details several key problems with common AI evaluation methods and suggests a broad range of solutions to help address them.

**Authors:**
The paper was authored by Ryan Burnell, Wout Schellaert, John Burden, Tomer D. Ullman, Fernando Martinez-Plumed, Joshua B. Tenenbaum, Danaja Rutar, Lucy G. Cheke, Jascha Sohl-Dickstein, Melanie Mitchell, Douwe Kiela, Murray Shanahan, Ellen M. Voorhees, Anthony G. Cohn, Joel Z. Leibo, and Jose Hernandez-Orallo, representing researchers from leading institutions including MIT, Harvard, Cambridge University, and others.

The paper is available through multiple sources including Science magazine, White Rose Research Online, and ResearchGate.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ca6fa12b-f060-44ff-a3f8-2be93538cabe",
  "uuid": "2ea9aa19-b41d-44ef-9064-3eb0a73bfa44",
  "tool_use_result": {
    "query": "Burnell et al 2023 \"Rethink Reporting of Evaluation Results in AI\" paper",
    "results": [
      {
        "tool_use_id": "srvtoolu_01U1VjCJtnHBcgp4WUHRSAPv",
        "content": [
          {
            "title": "Burnell, R. et al. (2023). Rethink Reporting of Evaluation Results in AI. Science, 380, 136-138. - References - Scientific Research Publishing",
            "url": "https://www.scirp.org/reference/referencespapers?referenceid=3535042"
          },
          {
            "title": "Rethink reporting of evaluation results in AI - White Rose Research Online",
            "url": "https://eprints.whiterose.ac.uk/198211/"
          },
          {
            "title": "Rethink reporting of evaluation results in AI | Science",
            "url": "https://www.science.org/doi/10.1126/science.adf6369"
          },
          {
            "title": "(PDF) Rethink reporting of evaluation results in AI",
            "url": "https://www.researchgate.net/publication/370002303_Rethink_reporting_of_evaluation_results_in_AI"
          },
          {
            "title": "eprints@whiterose.ac.uk https://eprints.whiterose.ac.uk",
            "url": "https://eprints.whiterose.ac.uk/id/eprint/198211/1/Burnell%20et%20al%20-%202023%20-%20Rethink%20reporting%20of%20evaluation%20results%20in%20AI%20(Pre-print).pdf"
          },
          {
            "title": "Rethink reporting of evaluation results in AI Aggregate metrics and lack of access to results limit understanding - Polytechnic University of Valencia",
            "url": "https://panorama.upv.es/en/ipublic/item/10192858"
          },
          {
            "title": "Audit Cards: Contextualizing AI Evaluations",
            "url": "https://arxiv.org/pdf/2504.13839"
          },
          {
            "title": "Rethink reporting of evaluation results in AI",
            "url": "https://ryanburnell.com/wp-content/uploads/Burnell-et-al-2023-Rethink-reporting-of-evaluation-results-in-AI.pdf"
          },
          {
            "title": "Rethink reporting of evaluation results in AI | Montreal AI Ethics Institute",
            "url": "https://montrealethics.ai/rethink-reporting-of-evaluation-results-in-ai/"
          }
        ]
      },
      "I found the paper! Here are the key details about the Burnell et al. 2023 paper:\n\n**Publication Details:**\nBurnell, R. et al. (2023). Rethink Reporting of Evaluation Results in AI. Science, 380, 136-138.\n\n**DOI:** 10.1126/science.adf6369\n\n**Main Focus:**\nThe paper addresses how aggregate metrics and lack of access to results limit understanding of AI system evaluation. The paper details several key problems with common AI evaluation methods and suggests a broad range of solutions to help address them.\n\n**Authors:**\nThe paper was authored by Ryan Burnell, Wout Schellaert, John Burden, Tomer D. Ullman, Fernando Martinez-Plumed, Joshua B. Tenenbaum, Danaja Rutar, Lucy G. Cheke, Jascha Sohl-Dickstein, Melanie Mitchell, Douwe Kiela, Murray Shanahan, Ellen M. Voorhees, Anthony G. Cohn, Joel Z. Leibo, and Jose Hernandez-Orallo, representing researchers from leading institutions including MIT, Harvard, Cambridge University, and others.\n\nThe paper is available through multiple sources including Science magazine, White Rose Research Online, and ResearchGate."
    ],
    "durationSeconds": 5.858654809
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-21T03:48:10.561Z_

<details><summary>↩ Tool result · `toolu_01U4hkXGVfpEWqb13k5eKuDn`</summary>

```text
Web search results for query: "Chang et al 2024 "A Survey on Evaluation of Large Language Models" paper"

Links: [{"title":"A Survey on Evaluation of Large Language Models","url":"https://arxiv.org/pdf/2307.03109"},{"title":"[PDF] A Survey on Evaluation of Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/A-Survey-on-Evaluation-of-Large-Language-Models-Chang-Wang/888728745dbb769e29ed475d4f7661eebe1a71cf"},{"title":"(PDF) A Survey on Evaluation of Large Language Models","url":"https://www.researchgate.net/publication/377639945_A_Survey_on_Evaluation_of_Large_Language_Models"},{"title":"Evaluating Large Language Models: A Comprehensive Survey","url":"https://arxiv.org/pdf/2310.19736"},{"title":"Human evaluation of large language models in healthcare: gaps, challenges, and the need for standardization | npj Health Systems","url":"https://www.nature.com/articles/s44401-025-00043-2"},{"title":"[2307.03109] A Survey on Evaluation of Large Language Models","url":"https://arxiv.org/abs/2307.03109"},{"title":"A Survey on Evaluation of Large Language Models | ACM Transactions on Intelligent Systems and Technology","url":"https://dl.acm.org/doi/full/10.1145/3641289"}]

I found the paper! Here are the key details:

**Paper Information:**

The paper is titled "A Survey on Evaluation of Large Language Models" by Yupeng Chang, Xu Wang, Jindong Wang, Yuan Wu, Kaijie Zhu, Hao Chen, Linyi Yang, Xiaoyuan Yi, Cunxiang Wang, Yidong Wang, Wei Ye, Yue Zhang, Yi Chang, Philip S. Yu, Qiang Yang, and Xing Xie.

It was published in ACM Transactions on Intelligent Systems and Technology, Volume 15, Issue 3, Article 39 in March 2024.

**Overview:**

The paper presents a comprehensive review of evaluation methods for LLMs, focusing on three key dimensions: what to evaluate, where to evaluate, and how to evaluate.

**Key Points:**

As LLMs continue to play a vital role in both research and daily use, their evaluation becomes increasingly critical, not only at the task level, but also at the society level for better understanding of their potential risks.

You can access the paper through multiple sources:
- The official ACM Transactions publication at dl.acm.org
- The arXiv version at https://arxiv.org/abs/2307.03109
- The authors maintain open-source materials at https://github.com/MLGroupJLU/LLM-eval-survey


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ca6fa12b-f060-44ff-a3f8-2be93538cabe",
  "uuid": "0479b649-3e88-490e-beda-f7faec26c8d0",
  "tool_use_result": {
    "query": "Chang et al 2024 \"A Survey on Evaluation of Large Language Models\" paper",
    "results": [
      {
        "tool_use_id": "srvtoolu_01RkNXst58n8yTnEJ2TnP9b1",
        "content": [
          {
            "title": "A Survey on Evaluation of Large Language Models",
            "url": "https://arxiv.org/pdf/2307.03109"
          },
          {
            "title": "[PDF] A Survey on Evaluation of Large Language Models | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/A-Survey-on-Evaluation-of-Large-Language-Models-Chang-Wang/888728745dbb769e29ed475d4f7661eebe1a71cf"
          },
          {
            "title": "(PDF) A Survey on Evaluation of Large Language Models",
            "url": "https://www.researchgate.net/publication/377639945_A_Survey_on_Evaluation_of_Large_Language_Models"
          },
          {
            "title": "Evaluating Large Language Models: A Comprehensive Survey",
            "url": "https://arxiv.org/pdf/2310.19736"
          },
          {
            "title": "Human evaluation of large language models in healthcare: gaps, challenges, and the need for standardization | npj Health Systems",
            "url": "https://www.nature.com/articles/s44401-025-00043-2"
          },
          {
            "title": "[2307.03109] A Survey on Evaluation of Large Language Models",
            "url": "https://arxiv.org/abs/2307.03109"
          },
          {
            "title": "A Survey on Evaluation of Large Language Models | ACM Transactions on Intelligent Systems and Technology",
            "url": "https://dl.acm.org/doi/full/10.1145/3641289"
          }
        ]
      },
      "I found the paper! Here are the key details:\n\n**Paper Information:**\n\nThe paper is titled \"A Survey on Evaluation of Large Language Models\" by Yupeng Chang, Xu Wang, Jindong Wang, Yuan Wu, Kaijie Zhu, Hao Chen, Linyi Yang, Xiaoyuan Yi, Cunxiang Wang, Yidong Wang, Wei Ye, Yue Zhang, Yi Chang, Philip S. Yu, Qiang Yang, and Xing Xie.\n\nIt was published in ACM Transactions on Intelligent Systems and Technology, Volume 15, Issue 3, Article 39 in March 2024.\n\n**Overview:**\n\nThe paper presents a comprehensive review of evaluation methods for LLMs, focusing on three key dimensions: what to evaluate, where to evaluate, and how to evaluate.\n\n**Key Points:**\n\nAs LLMs continue to play a vital role in both research and daily use, their evaluation becomes increasingly critical, not only at the task level, but also at the society level for better understanding of their potential risks.\n\nYou can access the paper through multiple sources:\n- The official ACM Transactions publication at dl.acm.org\n- The arXiv version at https://arxiv.org/abs/2307.03109\n- The authors maintain open-source materials at https://github.com/MLGroupJLU/LLM-eval-survey"
    ],
    "durationSeconds": 5.700570961999998
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-21T03:48:11.982Z_

<details><summary>↩ Tool result · `toolu_015vydRqX5T3LUkJw6FHacJ7`</summary>

```text
Web search results for query: "Ott et al 2022 "Mapping the Design Space" evaluation benchmarks NLP"

Links: [{"title":"A benchmark of expert-level academic questions to assess AI capabilities | Nature","url":"https://www.nature.com/articles/s41586-025-09962-4"},{"title":"Correlating and Predicting Human Evaluations of Language Models from   Natural Language Processing Benchmarks","url":"https://arxiv.org/pdf/2502.18339"},{"title":"ECBD: Evidence-Centered Benchmark Design for NLP","url":"https://arxiv.org/html/2406.08723v1"},{"title":"It Takes Two to Tango: Navigating Conceptualizations of NLP Tasks and   Measurements of Performance","url":"https://arxiv.org/pdf/2305.09022"},{"title":"Eval4NLP - 2022","url":"https://eval4nlp.github.io/2022/index.html"},{"title":"NLPBench: Evaluating Large Language Models on Solving NLP Problems","url":"https://arxiv.org/pdf/2309.15630"},{"title":"Vygotsky Distance: Measure for Benchmark Task Similarity","url":"https://arxiv.org/pdf/2402.14890"}]

Based on the search results, I found the Ott et al. 2022 paper. Ott, S., Barbosa-Silva, A., Blagec, K., Brauner, J. & Samwald, M. published "Mapping global dynamics of benchmark creation and saturation in artificial intelligence" in Nature Communications, volume 13, article 6793 (2022).

This paper appears to be focused on mapping the broader dynamics of how AI benchmarks are created and become saturated, rather than specifically evaluating a particular set of NLP benchmarks itself. The paper is cited as a reference work in studies examining benchmark evaluation practices in NLP and artificial intelligence more broadly.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ca6fa12b-f060-44ff-a3f8-2be93538cabe",
  "uuid": "ce3b6925-c85a-4542-93bc-eafcd35a6305",
  "tool_use_result": {
    "query": "Ott et al 2022 \"Mapping the Design Space\" evaluation benchmarks NLP",
    "results": [
      {
        "tool_use_id": "srvtoolu_01LdpFBhYTGEWbipEZo7ZDkg",
        "content": [
          {
            "title": "A benchmark of expert-level academic questions to assess AI capabilities | Nature",
            "url": "https://www.nature.com/articles/s41586-025-09962-4"
          },
          {
            "title": "Correlating and Predicting Human Evaluations of Language Models from   Natural Language Processing Benchmarks",
            "url": "https://arxiv.org/pdf/2502.18339"
          },
          {
            "title": "ECBD: Evidence-Centered Benchmark Design for NLP",
            "url": "https://arxiv.org/html/2406.08723v1"
          },
          {
            "title": "It Takes Two to Tango: Navigating Conceptualizations of NLP Tasks and   Measurements of Performance",
            "url": "https://arxiv.org/pdf/2305.09022"
          },
          {
            "title": "Eval4NLP - 2022",
            "url": "https://eval4nlp.github.io/2022/index.html"
          },
          {
            "title": "NLPBench: Evaluating Large Language Models on Solving NLP Problems",
            "url": "https://arxiv.org/pdf/2309.15630"
          },
          {
            "title": "Vygotsky Distance: Measure for Benchmark Task Similarity",
            "url": "https://arxiv.org/pdf/2402.14890"
          }
        ]
      },
      "Based on the search results, I found the Ott et al. 2022 paper. Ott, S., Barbosa-Silva, A., Blagec, K., Brauner, J. & Samwald, M. published \"Mapping global dynamics of benchmark creation and saturation in artificial intelligence\" in Nature Communications, volume 13, article 6793 (2022).\n\nThis paper appears to be focused on mapping the broader dynamics of how AI benchmarks are created and become saturated, rather than specifically evaluating a particular set of NLP benchmarks itself. The paper is cited as a reference work in studies examining benchmark evaluation practices in NLP and artificial intelligence more broadly."
    ],
    "durationSeconds": 5.499187672
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-21T03:48:12.246Z_

<details><summary>↩ Tool result · `toolu_01VEvQEWeimGGwEBbP7L4r45`</summary>

```text
Web search results for query: "Polo et al 2024 "tinyBenchmarks" efficient evaluation IRT paper"

Links: [{"title":"tinyBenchmarks: evaluating LLMs with fewer examples | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/tinybenchmarks-evaluating-llms-fewer-examples"},{"title":"(PDF) tinyBenchmarks: evaluating LLMs with fewer examples","url":"https://www.researchgate.net/publication/383238265_tinyBenchmarks_evaluating_LLMs_with_fewer_examples"},{"title":"tinyBenchmarks: evaluating LLMs with fewer examples for ICLR 2024 - IBM Research","url":"https://research.ibm.com/publications/tinybenchmarks-evaluating-llms-with-fewer-examples"},{"title":"Beyond the Singular: The Essential Role of Multiple Generations in Effective Benchmark Evaluation and Analysis","url":"https://arxiv.org/html/2502.08943v1"},{"title":"GitHub - felipemaiapolo/tinyBenchmarks: Evaluating LLMs with fewer examples · GitHub","url":"https://github.com/felipemaiapolo/tinyBenchmarks"},{"title":"tinyBenchmarks: evaluating LLMs with fewer examples","url":"https://proceedings.mlr.press/v235/maia-polo24a.html"},{"title":"tinyBenchmarks: evaluating LLMs with fewer examples","url":"https://arxiv.org/html/2402.14992v1"},{"title":"[2402.14992] tinyBenchmarks: evaluating LLMs with fewer examples","url":"https://arxiv.org/abs/2402.14992"},{"title":"How Reliable is Language Model Micro-Benchmarking?","url":"https://arxiv.org/html/2510.08730v1"}]

I've found the paper you're looking for! Here are the key details:

## Paper Information

The paper "tinyBenchmarks: evaluating LLMs with fewer examples" was published on 5/28/2024 by Felipe Maia Polo, Lucas Weber, Leshem Choshen, Yuekai Sun, Gongjun Xu, and Mikhail Yurochkin. It was presented at the Proceedings of the 41st International Conference on Machine Learning (ICML 2024), pages 34303-34326.

## Overview

The paper introduces a new benchmarking framework called tinyBenchmarks that leverages Item Response Theory (IRT) to efficiently evaluate the performance of large language models (LLMs) using fewer examples. For example, they show that to accurately estimate the performance of an LLM on MMLU, a popular multiple-choice QA benchmark consisting of 14K examples, it is sufficient to evaluate this LLM on 100 curated examples.

## Key Contribution

tinyBenchmarks is an efficient evaluation method that uses IRT to model the discriminative power of benchmark examples, allowing the selection of a small yet representative subset of items that can accurately estimate performance. The authors released evaluation tools and tiny versions of popular benchmarks: Open LLM Leaderboard, MMLU, HELM, and AlpacaEval 2.0.

The paper is available on arXiv as preprint 2402.14992.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ca6fa12b-f060-44ff-a3f8-2be93538cabe",
  "uuid": "35069d9b-48a0-4f00-9033-32a8b51a3ece",
  "tool_use_result": {
    "query": "Polo et al 2024 \"tinyBenchmarks\" efficient evaluation IRT paper",
    "results": [
      {
        "tool_use_id": "srvtoolu_01WusT7ghpXLEZsXFY3DtTzp",
        "content": [
          {
            "title": "tinyBenchmarks: evaluating LLMs with fewer examples | AI Research Paper Details",
            "url": "https://www.aimodels.fyi/papers/arxiv/tinybenchmarks-evaluating-llms-fewer-examples"
          },
          {
            "title": "(PDF) tinyBenchmarks: evaluating LLMs with fewer examples",
            "url": "https://www.researchgate.net/publication/383238265_tinyBenchmarks_evaluating_LLMs_with_fewer_examples"
          },
          {
            "title": "tinyBenchmarks: evaluating LLMs with fewer examples for ICLR 2024 - IBM Research",
            "url": "https://research.ibm.com/publications/tinybenchmarks-evaluating-llms-with-fewer-examples"
          },
          {
            "title": "Beyond the Singular: The Essential Role of Multiple Generations in Effective Benchmark Evaluation and Analysis",
            "url": "https://arxiv.org/html/2502.08943v1"
          },
          {
            "title": "GitHub - felipemaiapolo/tinyBenchmarks: Evaluating LLMs with fewer examples · GitHub",
            "url": "https://github.com/felipemaiapolo/tinyBenchmarks"
          },
          {
            "title": "tinyBenchmarks: evaluating LLMs with fewer examples",
            "url": "https://proceedings.mlr.press/v235/maia-polo24a.html"
          },
          {
            "title": "tinyBenchmarks: evaluating LLMs with fewer examples",
            "url": "https://arxiv.org/html/2402.14992v1"
          },
          {
            "title": "[2402.14992] tinyBenchmarks: evaluating LLMs with fewer examples",
            "url": "https://arxiv.org/abs/2402.14992"
          },
          {
            "title": "How Reliable is Language Model Micro-Benchmarking?",
            "url": "https://arxiv.org/html/2510.08730v1"
          }
        ]
      },
      "I've found the paper you're looking for! Here are the key details:\n\n## Paper Information\n\nThe paper \"tinyBenchmarks: evaluating LLMs with fewer examples\" was published on 5/28/2024 by Felipe Maia Polo, Lucas Weber, Leshem Choshen, Yuekai Sun, Gongjun Xu, and Mikhail Yurochkin. It was presented at the Proceedings of the 41st International Conference on Machine Learning (ICML 2024), pages 34303-34326.\n\n## Overview\n\nThe paper introduces a new benchmarking framework called tinyBenchmarks that leverages Item Response Theory (IRT) to efficiently evaluate the performance of large language models (LLMs) using fewer examples. For example, they show that to accurately estimate the performance of an LLM on MMLU, a popular multiple-choice QA benchmark consisting of 14K examples, it is sufficient to evaluate this LLM on 100 curated examples.\n\n## Key Contribution\n\ntinyBenchmarks is an efficient evaluation method that uses IRT to model the discriminative power of benchmark examples, allowing the selection of a small yet representative subset of items that can accurately estimate performance. The authors released evaluation tools and tiny versions of popular benchmarks: Open LLM Leaderboard, MMLU, HELM, and AlpacaEval 2.0.\n\nThe paper is available on arXiv as preprint 2402.14992."
    ],
    "durationSeconds": 6.926073807000001
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-21T03:48:13.162Z_

<details><summary>↩ Tool result · `toolu_01RCziuRLnE2GuVnTWwAMKMQ`</summary>

```text
Web search results for query: "MMLU-Pro Wang et al 2024 benchmark paper"

Links: [{"title":"GitHub - TIGER-AI-Lab/MMLU-Pro: The code and data for \"MMLU-Pro: A More Robust and Challenging Multi-Task Language Understanding Benchmark\" [NeurIPS 2024] · GitHub","url":"https://github.com/TIGER-AI-Lab/MMLU-Pro"},{"title":"MMLU-Pro Explained: The Advanced AI Benchmark for LLMs","url":"https://intuitionlabs.ai/pdfs/mmlu-pro-explained-the-advanced-ai-benchmark-for-llms.pdf"},{"title":"[2406.01574] MMLU-Pro: A More Robust and Challenging Multi-Task Language Understanding Benchmark","url":"https://arxiv.org/abs/2406.01574"},{"title":"[Quick Review] MMLU-Pro: A More Robust and Challenging Multi-Task Language Understanding Benchmark","url":"https://liner.com/review/mmlupro-a-more-robust-and-challenging-multitask-language-understanding-benchmark"},{"title":"MMLU-Pro Explained: The Advanced AI Benchmark for LLMs | IntuitionLabs","url":"https://intuitionlabs.ai/articles/mmlu-pro-ai-benchmark-explained"},{"title":"MMLU-Pro: A More Robust and Challenging Multi-Task Language Understanding Benchmark","url":"https://papers.nips.cc/paper_files/paper/2024/hash/ad236edc564f3e3156e1b2feafb99a24-Abstract-Datasets_and_Benchmarks_Track.html"},{"title":"MMLU-Pro | Proceedings of the 38th International Conference on Neural Information Processing Systems","url":"https://dl.acm.org/doi/10.5555/3737916.3740934"}]

I found the MMLU-Pro Wang et al. 2024 benchmark paper. Here are the key details:

## Paper Information

The paper "MMLU-Pro: A More Robust and Challenging Multi-Task Language Understanding Benchmark" was authored by Yubo Wang, Xueguang Ma, Ge Zhang, Yuansheng Ni, Abhranil Chandra, Shiguang Guo, Weiming Ren, Aaran Arulraj, Xuan He, Ziyan Jiang, Tianle Li, Max Ku, Kai Wang, Alex Zhuang, Rongqi Fan, Xiang Yue, and Wenhu Chen, and was introduced at the NeurIPS 2024 Datasets and Benchmarks track.

## Key Contributions

The paper introduces MMLU-Pro, an enhanced dataset designed to extend the mostly knowledge-driven MMLU benchmark by integrating more challenging, reasoning-focused questions and expanding the choice set from four to ten options.

Experimental results show that MMLU-Pro not only raises the challenge, causing a significant drop in accuracy by 16% to 33% compared to MMLU but also demonstrates greater stability under varying prompts.

## Available Resources

- **ArXiv**: The paper is available at https://arxiv.org/abs/2406.01574
- **GitHub Repository**: Code and data are available at https://github.com/TIGER-AI-Lab/MMLU-Pro
- **Official Conference**: The paper is published in the NeurIPS 2024 proceedings


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ca6fa12b-f060-44ff-a3f8-2be93538cabe",
  "uuid": "bf698601-2c38-473b-b76b-279991512579",
  "tool_use_result": {
    "query": "MMLU-Pro Wang et al 2024 benchmark paper",
    "results": [
      {
        "tool_use_id": "srvtoolu_01V8ttTtxcrxgHeKhUD4wTa3",
        "content": [
          {
            "title": "GitHub - TIGER-AI-Lab/MMLU-Pro: The code and data for \"MMLU-Pro: A More Robust and Challenging Multi-Task Language Understanding Benchmark\" [NeurIPS 2024] · GitHub",
            "url": "https://github.com/TIGER-AI-Lab/MMLU-Pro"
          },
          {
            "title": "MMLU-Pro Explained: The Advanced AI Benchmark for LLMs",
            "url": "https://intuitionlabs.ai/pdfs/mmlu-pro-explained-the-advanced-ai-benchmark-for-llms.pdf"
          },
          {
            "title": "[2406.01574] MMLU-Pro: A More Robust and Challenging Multi-Task Language Understanding Benchmark",
            "url": "https://arxiv.org/abs/2406.01574"
          },
          {
            "title": "[Quick Review] MMLU-Pro: A More Robust and Challenging Multi-Task Language Understanding Benchmark",
            "url": "https://liner.com/review/mmlupro-a-more-robust-and-challenging-multitask-language-understanding-benchmark"
          },
          {
            "title": "MMLU-Pro Explained: The Advanced AI Benchmark for LLMs | IntuitionLabs",
            "url": "https://intuitionlabs.ai/articles/mmlu-pro-ai-benchmark-explained"
          },
          {
            "title": "MMLU-Pro: A More Robust and Challenging Multi-Task Language Understanding Benchmark",
            "url": "https://papers.nips.cc/paper_files/paper/2024/hash/ad236edc564f3e3156e1b2feafb99a24-Abstract-Datasets_and_Benchmarks_Track.html"
          },
          {
            "title": "MMLU-Pro | Proceedings of the 38th International Conference on Neural Information Processing Systems",
            "url": "https://dl.acm.org/doi/10.5555/3737916.3740934"
          }
        ]
      },
      "I found the MMLU-Pro Wang et al. 2024 benchmark paper. Here are the key details:\n\n## Paper Information\n\nThe paper \"MMLU-Pro: A More Robust and Challenging Multi-Task Language Understanding Benchmark\" was authored by Yubo Wang, Xueguang Ma, Ge Zhang, Yuansheng Ni, Abhranil Chandra, Shiguang Guo, Weiming Ren, Aaran Arulraj, Xuan He, Ziyan Jiang, Tianle Li, Max Ku, Kai Wang, Alex Zhuang, Rongqi Fan, Xiang Yue, and Wenhu Chen, and was introduced at the NeurIPS 2024 Datasets and Benchmarks track.\n\n## Key Contributions\n\nThe paper introduces MMLU-Pro, an enhanced dataset designed to extend the mostly knowledge-driven MMLU benchmark by integrating more challenging, reasoning-focused questions and expanding the choice set from four to ten options.\n\nExperimental results show that MMLU-Pro not only raises the challenge, causing a significant drop in accuracy by 16% to 33% compared to MMLU but also demonstrates greater stability under varying prompts.\n\n## Available Resources\n\n- **ArXiv**: The paper is available at https://arxiv.org/abs/2406.01574\n- **GitHub Repository**: Code and data are available at https://github.com/TIGER-AI-Lab/MMLU-Pro\n- **Official Conference**: The paper is published in the NeurIPS 2024 proceedings"
    ],
    "durationSeconds": 7.370636872000003
  }
}
```

</details>

---

### Assistant

_source line 46_

<details><summary>Logged reasoning block</summary>

```text
Let me verify the Ott et al. paper more carefully, and also search for a 5th paper. I have good candidates:

1. Burnell et al. 2023 - "Rethink Reporting of Evaluation Results in AI" - Science, 380, 136-138. DOI: 10.1126/science.adf6369 ✓
2. Chang et al. 2024 - "A Survey on Evaluation of Large Language Models" - ACM TIST, Vol 15, Issue 3. ✓
3. Polo et al. 

2024 - "tinyBenchmarks: evaluating LLMs with fewer examples" - ICML 2024. arXiv: 2402.14992 ✓
4. Wang et al. 2024 - "MMLU-Pro: A More Robust and Challenging Multi-Task Language Understanding Benchmark" - NeurIPS 2024. arXiv: 2406.01574 ✓
5. Ott et al. 2022 - I found "Mapping global dynamics of benchmark creation and saturation in artificial intelligence" in Nature Communications, but I should double-check this is the right paper or look for alternatives.

I need to search more carefully for the Ott et al. 2022 paper on mapping the design space of LLM evaluation, and also explore recent work on psychometric approaches to evaluating LLMs as a potential fifth option.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ca6fa12b-f060-44ff-a3f8-2be93538cabe",
  "uuid": "ce0a075e-f732-412e-b3ce-3f0bea481ce8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RK2kDJ896FSuwp3FTjMiL9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 513,
      "cache_creation_input_tokens": 3721,
      "cache_read_input_tokens": 27372,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3721
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

_source line 47_

The Ott et al. 2022 result seems to be a different paper. Let me search more specifically and find a strong 5th candidate.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ca6fa12b-f060-44ff-a3f8-2be93538cabe",
  "uuid": "dd8d57cd-aeea-4aae-9979-56bd73680c24",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RK2kDJ896FSuwp3FTjMiL9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 513,
      "cache_creation_input_tokens": 3721,
      "cache_read_input_tokens": 27372,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3721
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BFEwBbdWWjWVGP5hR6eaMK`</summary>

```json
{
  "query": "Ott 2022 \"Mapping global dynamics of benchmark creation and saturation\" Nature Communications AI"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ca6fa12b-f060-44ff-a3f8-2be93538cabe",
  "uuid": "6369570e-362a-42fd-81ac-cc55999efe69",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RK2kDJ896FSuwp3FTjMiL9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 513,
      "cache_creation_input_tokens": 3721,
      "cache_read_input_tokens": 27372,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3721
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_013yvmBSJBoVfyymYTpDXo32`</summary>

```json
{
  "query": "psychometric analysis LLM evaluation item response theory benchmark 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ca6fa12b-f060-44ff-a3f8-2be93538cabe",
  "uuid": "263e47d8-9fe1-4bff-937e-c232effa3bd0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RK2kDJ896FSuwp3FTjMiL9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 513,
      "cache_creation_input_tokens": 3721,
      "cache_read_input_tokens": 27372,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3721
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

_source line 50 · 2026-05-21T03:48:32.419Z_

<details><summary>↩ Tool result · `toolu_01BFEwBbdWWjWVGP5hR6eaMK`</summary>

```text
Web search results for query: "Ott 2022 "Mapping global dynamics of benchmark creation and saturation" Nature Communications AI"

Links: [{"title":"Mapping global dynamics of benchmark creation and saturation in artificial intelligence | Nature Communications","url":"https://www.nature.com/articles/s41467-022-34591-0"},{"title":"(PDF) Mapping global dynamics of benchmark creation and saturation in artificial intelligence","url":"https://www.researchgate.net/publication/365295644_Mapping_global_dynamics_of_benchmark_creation_and_saturation_in_artificial_intelligence"},{"title":"Mapping global dynamics of benchmark creation and saturation in artificial intelligence - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC9649641/"},{"title":"[2203.04592v2] Mapping global dynamics of benchmark creation and saturation in artificial intelligence","url":"https://export.arxiv.org/abs/2203.04592v2"},{"title":"Mapping global dynamics of benchmark creation and saturation in artificial intelligence - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/36357391/"},{"title":"[2203.04592] Mapping global dynamics of benchmark creation and saturation in artificial intelligence","url":"https://arxiv.org/abs/2203.04592"},{"title":"Mapping global dynamics of benchmark creation and saturation ...","url":"https://www.researchgate.net/journal/Nature-Communications-2041-1723/publication/365295644_Mapping_global_dynamics_of_benchmark_creation_and_saturation_in_artificial_intelligence/links/636dc7092f4bca7fd04e0a24/Mapping-global-dynamics-of-benchmark-creation-and-saturation-in-artificial-intelligence.pdf"},{"title":"Scientific data articles within Nature Communications","url":"https://www.nature.com/subjects/scientific-data/ncomms"},{"title":"Mapping global dynamics of benchmark creation","url":"https://www.researchgate.net/publication/359129573_Mapping_global_dynamics_of_benchmark_creation_and_saturation_in_artificial_intelligence/fulltext/62296b7b97401151d20b5cd6/Mapping-global-dynamics-of-benchmark-creation-and-saturation-in-artificial-intelligence.pdf"}]

I found the paper! Here's what I discovered about the Ott et al. 2022 study:

"Mapping global dynamics of benchmark creation and saturation in artificial intelligence" was published in Nature Communications, volume 13, article 6793 in 2022.

The authors are Simon Ott, Adriano Barbosa-Silva, Kathrin Blagec, and others.

**Key findings:**

Benchmarks are crucial to measuring and steering progress in AI, but recent studies raised concerns over issues such as benchmark overfitting, benchmark saturation, and increasing centralization of benchmark dataset creation.

The researchers curated data for 3765 benchmarks covering computer vision and natural language processing, and found that a large fraction of benchmarks quickly trend towards near-saturation, many benchmarks fail to find widespread utilization, and benchmark performance gains are prone to unforeseen bursts.

They conclude that future benchmarks should emphasize versatility, breadth and real-world utility.

The paper is available at Nature Communications (DOI: 10.1038/s41467-022-34591-0) and the supplementary data has been deposited in the Zenodo database.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ca6fa12b-f060-44ff-a3f8-2be93538cabe",
  "uuid": "7ff53030-039e-478f-81f6-79d1edbb86e1",
  "tool_use_result": {
    "query": "Ott 2022 \"Mapping global dynamics of benchmark creation and saturation\" Nature Communications AI",
    "results": [
      {
        "tool_use_id": "srvtoolu_01C19pqY46J6rpd1sFkEGvE3",
        "content": [
          {
            "title": "Mapping global dynamics of benchmark creation and saturation in artificial intelligence | Nature Communications",
            "url": "https://www.nature.com/articles/s41467-022-34591-0"
          },
          {
            "title": "(PDF) Mapping global dynamics of benchmark creation and saturation in artificial intelligence",
            "url": "https://www.researchgate.net/publication/365295644_Mapping_global_dynamics_of_benchmark_creation_and_saturation_in_artificial_intelligence"
          },
          {
            "title": "Mapping global dynamics of benchmark creation and saturation in artificial intelligence - PMC",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC9649641/"
          },
          {
            "title": "[2203.04592v2] Mapping global dynamics of benchmark creation and saturation in artificial intelligence",
            "url": "https://export.arxiv.org/abs/2203.04592v2"
          },
          {
            "title": "Mapping global dynamics of benchmark creation and saturation in artificial intelligence - PubMed",
            "url": "https://pubmed.ncbi.nlm.nih.gov/36357391/"
          },
          {
            "title": "[2203.04592] Mapping global dynamics of benchmark creation and saturation in artificial intelligence",
            "url": "https://arxiv.org/abs/2203.04592"
          },
          {
            "title": "Mapping global dynamics of benchmark creation and saturation ...",
            "url": "https://www.researchgate.net/journal/Nature-Communications-2041-1723/publication/365295644_Mapping_global_dynamics_of_benchmark_creation_and_saturation_in_artificial_intelligence/links/636dc7092f4bca7fd04e0a24/Mapping-global-dynamics-of-benchmark-creation-and-saturation-in-artificial-intelligence.pdf"
          },
          {
            "title": "Scientific data articles within Nature Communications",
            "url": "https://www.nature.com/subjects/scientific-data/ncomms"
          },
          {
            "title": "Mapping global dynamics of benchmark creation",
            "url": "https://www.researchgate.net/publication/359129573_Mapping_global_dynamics_of_benchmark_creation_and_saturation_in_artificial_intelligence/fulltext/62296b7b97401151d20b5cd6/Mapping-global-dynamics-of-benchmark-creation-and-saturation-in-artificial-intelligence.pdf"
          }
        ]
      },
      "I found the paper! Here's what I discovered about the Ott et al. 2022 study:\n\n\"Mapping global dynamics of benchmark creation and saturation in artificial intelligence\" was published in Nature Communications, volume 13, article 6793 in 2022.\n\nThe authors are Simon Ott, Adriano Barbosa-Silva, Kathrin Blagec, and others.\n\n**Key findings:**\n\nBenchmarks are crucial to measuring and steering progress in AI, but recent studies raised concerns over issues such as benchmark overfitting, benchmark saturation, and increasing centralization of benchmark dataset creation.\n\nThe researchers curated data for 3765 benchmarks covering computer vision and natural language processing, and found that a large fraction of benchmarks quickly trend towards near-saturation, many benchmarks fail to find widespread utilization, and benchmark performance gains are prone to unforeseen bursts.\n\nThey conclude that future benchmarks should emphasize versatility, breadth and real-world utility.\n\nThe paper is available at Nature Communications (DOI: 10.1038/s41467-022-34591-0) and the supplementary data has been deposited in the Zenodo database."
    ],
    "durationSeconds": 6.135841945
  }
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-21T03:48:35.998Z_

<details><summary>↩ Tool result · `toolu_013yvmBSJBoVfyymYTpDXo32`</summary>

```text
Web search results for query: "psychometric analysis LLM evaluation item response theory benchmark 2024 2025"

Links: [{"title":"Lifting the benchmark iceberg with item-response theory | OpenReview","url":"https://openreview.net/forum?id=ZyVQqK7mcP"},{"title":"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://arxiv.org/html/2505.15055v2"},{"title":"Leveraging LLM-Respondents for Item Evaluation: a Psychometric Analysis","url":"https://arxiv.org/html/2407.10899v1"},{"title":"Leveraging LLM respondents for item evaluation: A psychometric analysis - Liu - 2025 - British Journal of Educational Technology - Wiley Online Library","url":"https://bera-journals.onlinelibrary.wiley.com/doi/10.1111/bjet.13570?af=R"},{"title":"Large Language Model Psychometrics: A Systematic Review of Evaluation, Validation, and Enhancement","url":"https://llm-psychometrics.com/"},{"title":"Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks","url":"https://arxiv.org/html/2511.04689v2"},{"title":"ERIC - EJ1467105 - Leveraging LLM Respondents for Item Evaluation: A Psychometric Analysis, British Journal of Educational Technology, 2025-May","url":"https://eric.ed.gov/default.aspx?q=descriptor:%22Item+Response+Theory%22&ff1=eduHigher+Education&id=EJ1467105"},{"title":"Measuring Competency, Not Performance: Item-Aware Evaluation Across Medical Benchmarks","url":"https://arxiv.org/pdf/2509.24186"}]

Based on the search results, here's what I found regarding psychometric analysis, LLM evaluation, and item response theory benchmarks from 2024-2025:

## Key Recent Research

**Major Frameworks and Studies:**

Researchers are adapting item response theory (IRT) to transform benchmarks from opaque leaderboards into transparent measurement instruments. PSN-IRT is a framework that combines psychometrics with neural networks to provide comprehensive and reliable analyses of LLM benchmarks, and through extensive experiments on 12 LLMs across 11 diverse datasets, current benchmarks often suffer from uneven measurement properties, insufficient difficulty ceilings, item saturation, and data contamination.

**IRT Applications in LLM Evaluation:**

Minor changes to implementation details can alter model rankings, which has prompted researchers to leverage psychometric principles from educational testing. A recent systematic review on Large Language Model Psychometrics covers evaluation, validation, and enhancement, including adoption of IRT models to improve LLM evaluation.

**Psychometric Validation of LLM Responses:**

Research exploring six different LLMs (GPT-3.5, GPT-4, Llama 2, Llama 3, Gemini-Pro, and Cohere Command R Plus) found that some exhibit proficiency comparable to human respondents, though they have narrow proficiency distributions, though an ensemble of LLMs can better approximate the broader ability distribution typical of college students.

**Benchmarking Challenges:**

Unlike prior IRT-based LLM benchmarks, recent work performs explicit psychometric validation to ensure calibration quality, addressing gaps in earlier approaches.

These developments represent an emerging trend in applying rigorous psychometric methodology to improve the reliability and interpretability of LLM evaluation benchmarks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ca6fa12b-f060-44ff-a3f8-2be93538cabe",
  "uuid": "fe1df6be-8fcb-4aba-961e-ba8d0f30ef2e",
  "tool_use_result": {
    "query": "psychometric analysis LLM evaluation item response theory benchmark 2024 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01MyL5rVFj21XhH1pqjNC97e",
        "content": [
          {
            "title": "Lifting the benchmark iceberg with item-response theory | OpenReview",
            "url": "https://openreview.net/forum?id=ZyVQqK7mcP"
          },
          {
            "title": "Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory",
            "url": "https://arxiv.org/html/2505.15055v2"
          },
          {
            "title": "Leveraging LLM-Respondents for Item Evaluation: a Psychometric Analysis",
            "url": "https://arxiv.org/html/2407.10899v1"
          },
          {
            "title": "Leveraging LLM respondents for item evaluation: A psychometric analysis - Liu - 2025 - British Journal of Educational Technology - Wiley Online Library",
            "url": "https://bera-journals.onlinelibrary.wiley.com/doi/10.1111/bjet.13570?af=R"
          },
          {
            "title": "Large Language Model Psychometrics: A Systematic Review of Evaluation, Validation, and Enhancement",
            "url": "https://llm-psychometrics.com/"
          },
          {
            "title": "Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks",
            "url": "https://arxiv.org/html/2511.04689v2"
          },
          {
            "title": "ERIC - EJ1467105 - Leveraging LLM Respondents for Item Evaluation: A Psychometric Analysis, British Journal of Educational Technology, 2025-May",
            "url": "https://eric.ed.gov/default.aspx?q=descriptor:%22Item+Response+Theory%22&ff1=eduHigher+Education&id=EJ1467105"
          },
          {
            "title": "Measuring Competency, Not Performance: Item-Aware Evaluation Across Medical Benchmarks",
            "url": "https://arxiv.org/pdf/2509.24186"
          }
        ]
      },
      "Based on the search results, here's what I found regarding psychometric analysis, LLM evaluation, and item response theory benchmarks from 2024-2025:\n\n## Key Recent Research\n\n**Major Frameworks and Studies:**\n\nResearchers are adapting item response theory (IRT) to transform benchmarks from opaque leaderboards into transparent measurement instruments. PSN-IRT is a framework that combines psychometrics with neural networks to provide comprehensive and reliable analyses of LLM benchmarks, and through extensive experiments on 12 LLMs across 11 diverse datasets, current benchmarks often suffer from uneven measurement properties, insufficient difficulty ceilings, item saturation, and data contamination.\n\n**IRT Applications in LLM Evaluation:**\n\nMinor changes to implementation details can alter model rankings, which has prompted researchers to leverage psychometric principles from educational testing. A recent systematic review on Large Language Model Psychometrics covers evaluation, validation, and enhancement, including adoption of IRT models to improve LLM evaluation.\n\n**Psychometric Validation of LLM Responses:**\n\nResearch exploring six different LLMs (GPT-3.5, GPT-4, Llama 2, Llama 3, Gemini-Pro, and Cohere Command R Plus) found that some exhibit proficiency comparable to human respondents, though they have narrow proficiency distributions, though an ensemble of LLMs can better approximate the broader ability distribution typical of college students.\n\n**Benchmarking Challenges:**\n\nUnlike prior IRT-based LLM benchmarks, recent work performs explicit psychometric validation to ensure calibration quality, addressing gaps in earlier approaches.\n\nThese developments represent an emerging trend in applying rigorous psychometric methodology to improve the reliability and interpretability of LLM evaluation benchmarks."
    ],
    "durationSeconds": 9.484967992999998
  }
}
```

</details>

---

### Assistant

_source line 52_

<details><summary>Logged reasoning block</summary>

```text
I found a very relevant paper: "Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory" - this is very directly related. Let me verify this paper. Also "Lifting the benchmark iceberg with item-response theory" on OpenReview looks relevant.

Let me decide on the 5 papers:

1. **Burnell et al. 2023** - "Rethink Reporting of Evaluation Results in AI" - Science, 380, 136-138. DOI: 10.1126/science.adf6369 ✓


2. **Chang et al. 2024** - "A Survey on Evaluation of Large Language Models" - ACM TIST ✓
3. **Polo et al. 2024** - "tinyBenchmarks: evaluating LLMs with fewer examples" - ICML 2024 ✓
4. **Wang et al. 2024** - "MMLU-Pro" - NeurIPS 2024 ✓
5. For the fifth paper, I'm weighing Ott et al. 2022 on benchmark saturation dynamics in Nature Communications against the other IRT-focused options I found.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ca6fa12b-f060-44ff-a3f8-2be93538cabe",
  "uuid": "2b7829c5-6d9c-4559-9d9c-9ecc2a2c2ee2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PTcUcn8DmoKgafAaswYPb4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2864,
      "cache_read_input_tokens": 31093,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2864
      },
      "output_tokens": 10,
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

_source line 53_

Found a highly relevant 5th candidate. Let me verify it.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ca6fa12b-f060-44ff-a3f8-2be93538cabe",
  "uuid": "2607ee35-6c75-4a6d-a2ab-410d9a4b0db2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PTcUcn8DmoKgafAaswYPb4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2864,
      "cache_read_input_tokens": 31093,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2864
      },
      "output_tokens": 10,
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

_source line 54_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TLReFE5CVYcGqWYkmX8Cqr`</summary>

```json
{
  "query": "\"Lost in Benchmarks\" \"Rethinking Large Language Model Benchmarking\" item response theory arxiv 2505"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ca6fa12b-f060-44ff-a3f8-2be93538cabe",
  "uuid": "3b7a8f7b-3708-406f-abc1-8546ee93e373",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PTcUcn8DmoKgafAaswYPb4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2864,
      "cache_read_input_tokens": 31093,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2864
      },
      "output_tokens": 10,
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

_source line 55 · 2026-05-21T03:48:54.121Z_

<details><summary>↩ Tool result · `toolu_01TLReFE5CVYcGqWYkmX8Cqr`</summary>

```text
Web search results for query: ""Lost in Benchmarks" "Rethinking Large Language Model Benchmarking" item response theory arxiv 2505"

Links: [{"title":"[2505.15055] Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://arxiv.org/abs/2505.15055"},{"title":"[Literature Review] Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://www.themoonlight.io/en/review/lost-in-benchmarks-rethinking-large-language-model-benchmarking-with-item-response-theory"},{"title":"Paper page - Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://huggingface.co/papers/2505.15055"},{"title":"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://arxiv.org/html/2505.15055v2"},{"title":"(PDF) Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://www.researchgate.net/publication/391954139_Lost_in_Benchmarks_Rethinking_Large_Language_Model_Benchmarking_with_Item_Response_Theory"},{"title":"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://www.emergentmind.com/papers/2505.15055"},{"title":"[PDF] Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Lost-in-Benchmarks-Rethinking-Large-Language-Model-Zhou-Huang/a43a21d3b8bcede381110da630421afca45c8e5d"},{"title":"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://chatpaper.com/paper/139423"},{"title":"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with","url":"https://arxiv.org/pdf/2505.15055"}]

I found the paper! Here are the search results for "Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory":

## Key Information:

**Paper Details:**
- The paper addresses inconsistencies between different leaderboards and poor separability among top models that raise concerns about benchmark ability to accurately reflect authentic model capabilities
- The paper was published on arXiv on May 21, 2025 (arXiv:2505.15055v1)
- Authors include Hongli Zhou, Hui Huang, Ziqing Zhao, and others from Harbin Institute of Technology and China Electronics Standardization Institute

**Main Contribution:**
- The authors propose Pseudo-Siamese Network for Item Response Theory (PSN-IRT), an enhanced Item Response Theory framework that incorporates a rich set of item parameters within an IRT-grounded architecture

**Key Results:**
- PSN-IRT can construct smaller benchmarks while maintaining stronger alignment with human preference
- The framework's design enables reliable parameter estimation even when model abilities deviate from normality, and supports downstream applications such as benchmark quality assessment and efficient item selection

The paper is available on arXiv at https://arxiv.org/abs/2505.15055


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ca6fa12b-f060-44ff-a3f8-2be93538cabe",
  "uuid": "00ba69c3-b43b-4330-8a20-f0b4f3673b50",
  "tool_use_result": {
    "query": "\"Lost in Benchmarks\" \"Rethinking Large Language Model Benchmarking\" item response theory arxiv 2505",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Ma6t4dYyvUqWT8HnSr9Zfd",
        "content": [
          {
            "title": "[2505.15055] Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory",
            "url": "https://arxiv.org/abs/2505.15055"
          },
          {
            "title": "[Literature Review] Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory",
            "url": "https://www.themoonlight.io/en/review/lost-in-benchmarks-rethinking-large-language-model-benchmarking-with-item-response-theory"
          },
          {
            "title": "Paper page - Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory",
            "url": "https://huggingface.co/papers/2505.15055"
          },
          {
            "title": "Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory",
            "url": "https://arxiv.org/html/2505.15055v2"
          },
          {
            "title": "(PDF) Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory",
            "url": "https://www.researchgate.net/publication/391954139_Lost_in_Benchmarks_Rethinking_Large_Language_Model_Benchmarking_with_Item_Response_Theory"
          },
          {
            "title": "Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory",
            "url": "https://www.emergentmind.com/papers/2505.15055"
          },
          {
            "title": "[PDF] Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Lost-in-Benchmarks-Rethinking-Large-Language-Model-Zhou-Huang/a43a21d3b8bcede381110da630421afca45c8e5d"
          },
          {
            "title": "Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory",
            "url": "https://chatpaper.com/paper/139423"
          },
          {
            "title": "Lost in Benchmarks? Rethinking Large Language Model Benchmarking with",
            "url": "https://arxiv.org/pdf/2505.15055"
          }
        ]
      },
      "I found the paper! Here are the search results for \"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory\":\n\n## Key Information:\n\n**Paper Details:**\n- The paper addresses inconsistencies between different leaderboards and poor separability among top models that raise concerns about benchmark ability to accurately reflect authentic model capabilities\n- The paper was published on arXiv on May 21, 2025 (arXiv:2505.15055v1)\n- Authors include Hongli Zhou, Hui Huang, Ziqing Zhao, and others from Harbin Institute of Technology and China Electronics Standardization Institute\n\n**Main Contribution:**\n- The authors propose Pseudo-Siamese Network for Item Response Theory (PSN-IRT), an enhanced Item Response Theory framework that incorporates a rich set of item parameters within an IRT-grounded architecture\n\n**Key Results:**\n- PSN-IRT can construct smaller benchmarks while maintaining stronger alignment with human preference\n- The framework's design enables reliable parameter estimation even when model abilities deviate from normality, and supports downstream applications such as benchmark quality assessment and efficient item selection\n\nThe paper is available on arXiv at https://arxiv.org/abs/2505.15055"
    ],
    "durationSeconds": 6.048438351000004
  }
}
```

</details>

---

### Assistant

_source line 56_

<details><summary>Logged reasoning block</summary>

```text
This "Lost in Benchmarks" paper is very recent (May 2025) and very directly relevant to the IRT-based benchmark analysis project. However, it's a preprint and not yet published at a venue. Let me think about whether to use this or Ott et al. 2022.

Actually, looking at the task again, the task says "Any recent (2024-2026) work on psychometric evaluation of LLMs" is a good candidate. The "Lost in Benchmarks" paper is highly relevant but it's very recent (May 2025, just days ago). Let me check if it has been peer-reviewed.


Ott et al. 2022 is published in Nature Communications and addresses benchmark saturation dynamics, making it a solid choice for the evaluation methodology category. However, I'm noticing the actual paper title is "Mapping global dynamics of benchmark creation and saturation in artificial intelligence" rather than "Mapping the Design Space of LLM Evaluation" as originally suggested, so I should verify this is the right paper before finalizing.

Now I'm compiling my final list of five papers, starting with Burnell et al. 2023 from Science on rethinking how we report evaluation results in AI. evaluation covering what/where/how to evaluate; provides landscape context for our psychometric approach. Now I'm looking at tinyBenchmarks, which uses item response theory to select representative subsets for efficient evaluation—directly relevant to our IRT-based equating method. I'm also noting MMLU-Pro as another benchmark refinement approach that's worth considering in this context. Continuing with the second paper, I'm noting the publication details and how it provides empirical support for the benchmark saturation problem—showing that static benchmarks become less useful over time, which reinforces why we need equated scoring approaches.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ca6fa12b-f060-44ff-a3f8-2be93538cabe",
  "uuid": "df10d03f-65c2-43a0-a0f2-0aa6ec3f27d4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014CyGy7MNeHysEv4BZmWxzy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1318,
      "cache_read_input_tokens": 33957,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1318
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

_source line 57_

Now let me check the existing literature map to avoid duplicates, then add the papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ca6fa12b-f060-44ff-a3f8-2be93538cabe",
  "uuid": "7220ac05-d7b6-4165-af0c-9f00b7c254ee",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014CyGy7MNeHysEv4BZmWxzy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1318,
      "cache_read_input_tokens": 33957,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1318
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

_source line 58_

<details open><summary>🔧 Tool call — Read · `toolu_011zpMwQ6cokFxEpNRUNNTC1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/literature_map.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ca6fa12b-f060-44ff-a3f8-2be93538cabe",
  "uuid": "7caa6afc-d131-480c-820f-9620af8c3480",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014CyGy7MNeHysEv4BZmWxzy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1318,
      "cache_read_input_tokens": 33957,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1318
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

_source line 59 · 2026-05-21T03:49:30.435Z_

<details><summary>↩ Tool result · `toolu_011zpMwQ6cokFxEpNRUNNTC1`</summary>

```text
1	categories:
2	- key: contamination_detection
3	  name: Benchmark Contamination Detection
4	  narrative: Methods for detecting training data contamination in LLM benchmarks,
5	    including RL-robust approaches
6	- key: irt_equating
7	  name: IRT Methodology & Equating
8	  narrative: Item Response Theory models, calibration, equating, and their application
9	    to LLM evaluation
10	- key: benchmark_design
11	  name: Dynamic Benchmark Design
12	  narrative: Approaches for creating contamination-resistant or self-updating benchmarks
13	- key: dif_methodology
14	  name: DIF Statistical Methods
15	  narrative: Differential Item Functioning detection methods, power analysis, and
16	    small-sample strategies
17	- key: item_generation
18	  name: Automated Item Generation
19	  narrative: LLM-based test item generation with difficulty control and psychometric
20	    validation
21	meta:
22	  last_updated: '2026-05-21T03:43:39.944Z'
23	  total_papers: 40
24	papers:
25	  balloccu2024leak:
26	    abstract: ''
27	    added_at: '2026-05-21T01:40:37.987Z'
28	    added_by: literature-gap-fill
29	    authors:
30	    - Balloccu, S.
31	    - Schmidtova, P.
32	    - Lango, M.
33	    - Dusek, O.
34	    bibtex_key: balloccu2024leak
35	    category: contamination_detection
36	    doi: 10.18653/v1/2024.eacl-long.5
37	    relevance: Systematic survey of data leakage in closed-source LLMs covering 255
38	      papers and 263 benchmarks; establishes scope of contamination problem motivating
39	      our detection approach
40	    role: foundation
41	    semantic_scholar_id: 798feda076ad710df65d509a7884bd15937c8056
42	    title: 'Leak, Cheat, Repeat: Data Contamination and Evaluation Malpractices in
43	      Closed-Source LLMs'
44	    url: https://arxiv.org/abs/2402.03927
45	    venue: EACL 2024
46	    verified: true
47	    year: 2024
48	  belzak2020smallsample:
49	    abstract: ''
50	    added_at: '2026-05-20T17:30:00.000Z'
51	    added_by: director
52	    authors:
53	    - Belzak, W.
54	    bibtex_key: belzak2020smallsample
55	    category: dif_methodology
56	    doi: 10.1080/00273171.2019.1671162
57	    relevance: Parsimonious logistic regression with sum scores outperforms complex
58	      IRT models for DIF detection in small samples; directly applicable to our N=50-80
59	      model cohorts
60	    role: method-component
61	    semantic_scholar_id: 8f13882b6f37be1ade68c40539156277e5723395
62	    title: Testing Differential Item Functioning in Small Samples
63	    url: https://www.tandfonline.com/doi/abs/10.1080/00273171.2019.1671162
64	    venue: Multivariate Behavioral Research
65	    verified: true
66	    year: 2020
67	  dekoninck2024constat:
68	    abstract: ''
69	    added_at: '2026-05-21T01:40:37.987Z'
70	    added_by: literature-gap-fill
71	    authors:
72	    - Dekoninck, J.
73	    - Mueller, M. N.
74	    - Vechev, M.
75	    bibtex_key: dekoninck2024constat
76	    category: contamination_detection
77	    doi: ''
78	    relevance: Performance-based contamination detection via perturbation analysis;
79	      closest methodological parallel to our DIF approach in using behavioral patterns
80	      rather than memorization signals
81	    role: direct-competitor
82	    semantic_scholar_id: ''
83	    title: 'ConStat: Performance-Based Contamination Detection in Large Language Models'
84	    url: https://arxiv.org/abs/2405.16281
85	    venue: NeurIPS 2024
86	    verified: true
87	    year: 2024
88	  golchin2024timetravel:
89	    abstract: ''
90	    added_at: '2026-05-21T01:40:37.987Z'
91	    added_by: literature-gap-fill
92	    authors:
93	    - Golchin, S.
94	    - Surdeanu, M.
95	    bibtex_key: golchin2024timetravel
96	    category: contamination_detection
97	    doi: ''
98	    relevance: Instance-level contamination detection via guided completion prompts;
99	      baseline approach for individual-item detection that our group-level DIF method
100	      extends
101	    role: method-component
102	    semantic_scholar_id: d6d0fd994f37b630f35945736b5e1bb198148404
103	    title: 'Time Travel in LLMs: Tracing Data Contamination in Large Language Models'
104	    url: https://arxiv.org/abs/2308.08493
105	    venue: ICLR 2024
106	    verified: true
107	    year: 2024
108	  hardy2026scalability:
109	    abstract: ''
110	    added_at: '2026-05-20T17:30:00.000Z'
111	    added_by: director
112	    authors:
113	    - Hardy, M.
114	    - Gilbert, J.
115	    - Domingue, B.
116	    bibtex_key: hardy2026scalability
117	    category: irt_equating
118	    doi: 10.48550/arXiv.2603.24999
119	    relevance: Nonparametric signed isotonic R2 scalability coefficients outperform
120	      IRT item diagnostics; lightweight pre-filter for item quality before our parametric
121	      calibration
122	    role: method-component
123	    semantic_scholar_id: ''
124	    title: Efficient Detection of Bad Benchmark Items with Novel Scalability Coefficients
125	    url: https://arxiv.org/abs/2603.24999
126	    venue: arXiv
127	    verified: true
128	    year: 2026
129	  kim2019fpc:
130	    abstract: ''
131	    added_at: '2026-05-20T17:30:00.000Z'
132	    added_by: director
133	    authors:
134	    - Kim, S.
135	    - Kolen, M.
136	    bibtex_key: kim2019fpc
137	    category: irt_equating
138	    doi: 10.1080/08957347.2019.1660344
139	    relevance: Fixed-parameter calibration requires only N>=200 vs N>=500 for full
140	      calibration; core methodology for our bifactor IRT equating with anchor items
141	    role: method-component
142	    semantic_scholar_id: ''
143	    title: Application of IRT Fixed Parameter Calibration to Multiple-Group Test Data
144	    url: https://www.tandfonline.com/doi/abs/10.1080/08957347.2019.1660344
145	    venue: Applied Measurement in Education
146	    verified: true
147	    year: 2019
148	  li2024contamination:
149	    abstract: ''
150	    added_at: '2026-05-21T01:40:37.987Z'
151	    added_by: literature-gap-fill
152	    authors:
153	    - Li, Y.
154	    - Guo, Y.
155	    - Guerin, F.
156	    - Lin, C.
157	    bibtex_key: li2024contamination
158	    category: contamination_detection
159	    doi: 10.18653/v1/2024.findings-emnlp.30
160	    relevance: Provides web-overlap contamination labels for MMLU and other benchmarks
161	      via Common Crawl matching; primary ground-truth comparison for our DIF-based
162	      contamination detection
163	    role: foundation
164	    semantic_scholar_id: 32e11cf020021c225782a3b77b5cfed4ae8e14a0
165	    title: An Open-Source Data Contamination Report for Large Language Models
166	    url: https://aclanthology.org/2024.findings-emnlp.30/
167	    venue: Findings of EMNLP 2024
168	    verified: true
169	    year: 2024
170	  liang2026dvd:
171	    abstract: ''
172	    added_at: '2026-05-20T17:30:00.000Z'
173	    added_by: director
174	    authors:
175	    - Liang, R.
176	    bibtex_key: liang2026dvd
177	    category: contamination_detection
178	    doi: ''
179	    relevance: Detects variant contamination via generation variance (AUC 0.73-0.74
180	      vs Min-K++ 0.43-0.68); complementary signal in our ensemble but untested under
181	      RL training
182	    role: direct-competitor
183	    semantic_scholar_id: ''
184	    title: 'DVD: Detection via Variance of Generation Distribution for Variant Contamination'
185	    url: https://arxiv.org/abs/2601.04895
186	    venue: arXiv
187	    verified: true
188	    year: 2026
189	  shi2024mink:
190	    abstract: ''
191	    added_at: '2026-05-21T01:40:37.987Z'
192	    added_by: literature-gap-fill
193	    authors:
194	    - Shi, W.
195	    - Ajith, A.
196	    - Xia, M.
197	    - Huang, Y.
198	    - Liu, D.
199	    - Blevins, T.
200	    - Chen, D.
201	    - Zettlemoyer, L.
202	    bibtex_key: shi2024mink
203	    category: contamination_detection
204	    doi: ''
205	    relevance: Introduces Min-K% Prob method and WikiMIA benchmark for pretraining
206	      data detection; key baseline whose limitations under RL training motivate our
207	      DIF-based alternative
208	    role: foundation
209	    semantic_scholar_id: 3422d5e0cdfdc935d6a84a1e3d3f96659265fe3a
210	    title: Detecting Pretraining Data from Large Language Models
211	    url: https://arxiv.org/abs/2310.16789
212	    venue: ICLR 2024
213	    verified: true
214	    year: 2024
215	  tao2026selfcritique:
216	    abstract: ''
217	    added_at: '2026-05-20T17:30:00.000Z'
218	    added_by: director
219	    authors:
220	    - Tao, Y.
221	    bibtex_key: tao2026selfcritique
222	    category: contamination_detection
223	    doi: ''
224	    relevance: Self-Critique/RL-MIA partially addresses RL concealment via policy-collapse
225	      detection, but remains individual-model-level; our DIF is group-level and complementary
226	    role: direct-competitor
227	    semantic_scholar_id: ''
228	    title: Detecting Data Contamination from Reinforcement Learning Post-training
229	      for Large Language Models
230	    url: https://arxiv.org/abs/2510.09259
231	    venue: ICLR 2026
232	    verified: true
233	    year: 2026
234	  wang2026fragility:
235	    abstract: ''
236	    added_at: '2026-05-20T17:30:00.000Z'
237	    added_by: director
238	    authors:
239	    - Wang, H.
240	    - Li, H.
241	    - Ko, B.
242	    - Zhang, H.
243	    bibtex_key: wang2026fragility
244	    category: contamination_detection
245	    doi: ''
246	    relevance: Proves GRPO/PPO RL training conceals contamination signals (14-20pp
247	      AUROC degradation), motivating our DIF-based approach which operates on behavioral
248	      patterns immune to NLL smoothing
249	    role: foundation
250	    semantic_scholar_id: 9a5bf5d3c7116cc4a104c06599fbcef2d1b5abf3
251	    title: On The Fragility of Benchmark Contamination Detection in Reasoning Models
252	    url: https://arxiv.org/abs/2510.02386
253	    venue: ICLR 2026
254	    verified: true
255	    year: 2026
256	  white2025livebench:
257	    abstract: ''
258	    added_at: '2026-05-20T17:30:00.000Z'
259	    added_by: director
260	    authors:
261	    - White, C.
262	    bibtex_key: white2025livebench
263	    category: benchmark_design
264	    doi: 10.48550/arXiv.2406.19314
265	    relevance: Monthly-updated contamination-free benchmark with objective scoring;
266	      no difficulty calibration or psychometric equivalence across updates
267	    role: direct-competitor
268	    semantic_scholar_id: 4e5d86ea8eacd341d13123852d50d1ef62738744
269	    title: 'LiveBench: A Challenging, Contamination-Free LLM Benchmark'
270	    url: https://arxiv.org/abs/2406.19314
271	    venue: ICLR 2025
272	    verified: true
273	    year: 2025
274	  zhang2024gsm1k:
275	    abstract: ''
276	    added_at: '2026-05-20T17:30:00.000Z'
277	    added_by: director
278	    authors:
279	    - Zhang, H.
280	    bibtex_key: zhang2024gsm1k
281	    category: contamination_detection
282	    doi: ''
283	    relevance: GSM1K documents 10-13% average accuracy drops from contamination; provides
284	      ground-truth contamination evidence and item-level effect sizes (delta 0.8-1.4
285	      logits) critical for our DIF power analysis
286	    role: foundation
287	    semantic_scholar_id: ef62f95c16f668f031d649799cbd79081c6d2b0f
288	    title: A Careful Examination of Large Language Model Performance on Grade School
289	      Arithmetic
290	    url: https://arxiv.org/abs/2405.00332
291	    venue: arXiv
292	    verified: true
293	    year: 2024
294	  zhang2024minkpp:
295	    abstract: ''
296	    added_at: '2026-05-21T01:40:37.987Z'
297	    added_by: literature-gap-fill
298	    authors:
299	    - Zhang, J.
300	    - Sun, J.
301	    - Yeats, E.
302	    - Ouyang, Y.
303	    - Kuo, M.
304	    - Zhang, J.
305	    - Yang, H.
306	    - Li, H.
307	    bibtex_key: zhang2024minkpp
308	    category: contamination_detection
309	    doi: ''
310	    relevance: Improves Min-K% with vocabulary-normalized token probabilities; key
311	      baseline whose AUC degrades to 0.43-0.68 on RL-trained models, motivating our
312	      DIF-based alternative
313	    role: direct-competitor
314	    semantic_scholar_id: ''
315	    title: 'Min-K%++: Improved Baseline for Detecting Pre-Training Data from Large
316	      Language Models'
317	    url: https://arxiv.org/abs/2404.02936
318	    venue: arXiv
319	    verified: true
320	    year: 2024
321	  lalor2019irt:
322	    title: 'Learning Latent Parameters without Human Response Patterns: Item Response
323	      Theory with Artificial Crowds'
324	    authors:
325	    - Lalor, J.
326	    - Wu, H.
327	    - Yu, H.
328	    year: 2019
329	    venue: EMNLP-IJCNLP 2019
330	    url: https://aclanthology.org/D19-1434/
331	    doi: 10.18653/v1/D19-1434
332	    bibtex_key: lalor2019irt
333	    category: irt_equating
334	    role: foundation
335	    relevance: Pioneering application of IRT to NLP evaluation using artificial crowds
336	      of DNN models; establishes that IRT parameters from machine response patterns
337	      correlate with human-calibrated parameters
338	    abstract: ''
339	    semantic_scholar_id: df6cd8a8d836e75690141deb732f6d19f0176a2e
340	    verified: true
341	    added_by: literature-gap-fill
342	    added_at: '2026-05-21T02:29:19.632Z'
343	  vania2021irt:
344	    title: Comparing Test Sets with Item Response Theory
345	    authors:
346	    - Vania, C.
347	    - Htut, P.M.
348	    - Huang, W.
349	    - Mungra, D.
350	    - Pang, R.Y.
351	    - Phang, J.
352	    - Liu, H.
353	    - Cho, K.
354	    - Bowman, S.R.
355	    year: 2021
356	    venue: ACL 2021
357	    url: https://aclanthology.org/2021.acl-long.92/
358	    doi: 10.18653/v1/2021.acl-long.92
359	    bibtex_key: vania2021irt
360	    category: irt_equating
361	    role: foundation
362	    relevance: IRT-based analysis of NLU benchmark discriminability; shows which test
363	      sets remain effective at differentiating strong models and which are saturated
364	    abstract: ''
365	    semantic_scholar_id: 4ca39cf99747b8962fe37e7e025e284872df3425
366	    verified: true
367	    added_by: literature-gap-fill
368	    added_at: '2026-05-21T02:29:19.632Z'
369	  li2025atlas:
370	    title: 'Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static
371	      Benchmarks'
372	    authors:
373	    - Li, P.
374	    - Tang, X.
375	    - Chen, S.
376	    - Cheng, Y.
377	    - Metoyer, R.
378	    - Hua, T.
379	    - Chawla, N.V.
380	    year: 2025
381	    venue: arXiv
382	    url: https://arxiv.org/abs/2511.04689
383	    doi: 10.48550/arXiv.2511.04689
384	    bibtex_key: li2025atlas
385	    category: irt_equating
386	    role: method-component
387	    relevance: IRT-based adaptive testing framework (ATLAS) reduces benchmark items
388	      by 90% while preserving ability estimates; demonstrates IRT enables efficient
389	      LLM evaluation
390	    abstract: ''
391	    semantic_scholar_id: 087ce2837a0d5562bc95a40e77a327a6d033366c
392	    verified: true
393	    added_by: literature-gap-fill
394	    added_at: '2026-05-21T02:29:19.632Z'
395	  chen2025irtnet:
396	    title: Learning Compact Representations of LLM Abilities via Item Response Theory
397	    authors:
398	    - Chen, J.
399	    - Wang, C.
400	    - Zhang, G.
401	    - Ye, P.
402	    - Bai, L.
403	    - Hu, W.
404	    - Qu, Y.
405	    - Hu, S.
406	    year: 2025
407	    venue: arXiv
408	    url: https://arxiv.org/abs/2510.00844
409	    doi: 10.48550/arXiv.2510.00844
410	    bibtex_key: chen2025irtnet
411	    category: irt_equating
412	    role: method-component
413	    relevance: Multidimensional IRT with MoE network for learning LLM ability vectors
414	      and query discrimination/difficulty; demonstrates IRT-based model routing and
415	      benchmark prediction
416	    abstract: ''
417	    semantic_scholar_id: ''
418	    verified: true
419	    added_by: literature-gap-fill
420	    added_at: '2026-05-21T02:29:19.632Z'
421	  choi2026llmjudgeirt:
422	    title: Diagnosing the Reliability of LLM-as-a-Judge via Item Response Theory
423	    authors:
424	    - Choi, J.
425	    - Park, S.
426	    - Cho, C.
427	    - Park, H.
428	    - Kim, B.
429	    year: 2026
430	    venue: arXiv
431	    url: https://arxiv.org/abs/2602.00521
432	    doi: 10.48550/arXiv.2602.00521
433	    bibtex_key: choi2026llmjudgeirt
434	    category: irt_equating
435	    role: method-component
436	    relevance: Applies IRT Graded Response Model to diagnose LLM judge reliability;
437	      extends IRT application beyond benchmark scoring to evaluation pipeline quality
438	      assessment
439	    abstract: ''
440	    semantic_scholar_id: 4fc931a456c8162716deadbc9db6fd770189e632
441	    verified: true
442	    added_by: literature-gap-fill
443	    added_at: '2026-05-21T02:29:19.632Z'
444	  holland1988mh:
445	    title: Differential Item Functioning and the Mantel-Haenszel Procedure
446	    authors:
447	    - Holland, P.W.
448	    - Thayer, D.T.
449	    year: 1988
450	    venue: In H. Wainer & H.I. Braun (Eds.), Test Validity, Lawrence Erlbaum
451	    url: https://onlinelibrary.wiley.com/doi/abs/10.1002/j.2330-8516.1986.tb00186.x
452	    doi: 10.1002/j.2330-8516.1986.tb00186.x
453	    bibtex_key: holland1988mh
454	    category: dif_methodology
455	    role: foundation
456	    relevance: Seminal paper introducing the Mantel-Haenszel procedure for DIF detection;
457	      establishes the ETS classification system (A/B/C) used as standard DIF effect-size
458	      metric
459	    abstract: ''
460	    semantic_scholar_id: 5fbc064e7104036b77a2bf6f0ad509031965c275
461	    verified: true
462	    added_by: literature-gap-fill
463	    added_at: '2026-05-21T03:21:36.315Z'
464	  shealy1993sibtest:
465	    title: A Model-Based Standardization Approach that Separates True Bias/DIF from
466	      Group Ability Differences and Detects Test Bias/DTF as Well as Item Bias/DIF
467	    authors:
468	    - Shealy, R.
469	    - Stout, W.
470	    year: 1993
471	    venue: Psychometrika
472	    url: https://link.springer.com/article/10.1007/BF02294572
473	    doi: 10.1007/BF02294572
474	    bibtex_key: shealy1993sibtest
475	    category: dif_methodology
476	    role: foundation
477	    relevance: Introduces SIBTEST, a nonparametric DIF detection method that separates
478	      true item bias from group ability differences; alternative to MH that handles
479	      non-uniform DIF
480	    abstract: ''
481	    semantic_scholar_id: 82f3db496626afd828fedb01a41f719a50dbfc2c
482	    verified: true
483	    added_by: literature-gap-fill
484	    added_at: '2026-05-21T03:21:36.315Z'
485	  clauser1998dif:
486	    title: Using Statistical Procedures to Identify Differentially Functioning Test
487	      Items
488	    authors:
489	    - Clauser, B.E.
490	    - Mazor, K.M.
491	    year: 1998
492	    venue: 'Educational Measurement: Issues and Practice'
493	    url: https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1745-3992.1998.tb00619.x
494	    doi: 10.1111/j.1745-3992.1998.tb00619.x
495	    bibtex_key: clauser1998dif
496	    category: dif_methodology
497	    role: foundation
498	    relevance: Comprehensive review of DIF detection methods (MH, SIBTEST, logistic
499	      regression, IRT-based); standard reference for comparing statistical approaches
500	      to DIF
501	    abstract: ''
502	    semantic_scholar_id: c2377c505c95b924e972e61dadec81e9c87dea18
503	    verified: true
504	    added_by: literature-gap-fill
505	    added_at: '2026-05-21T03:21:36.315Z'
506	  zumbo1999handbook:
507	    title: 'A Handbook on the Theory and Methods of Differential Item Functioning
508	      (DIF): Logistic Regression Modeling as a Unitary Framework for Binary and Likert-Type
509	      (Ordinal) Item Scores'
510	    authors:
511	    - Zumbo, B.D.
512	    year: 1999
513	    venue: 'Ottawa: Directorate of Human Resources Research and Evaluation, Department
514	      of National Defense'
515	    url: https://faculty.educ.ubc.ca/zumbo/DIF/handbook.pdf
516	    doi: ''
517	    bibtex_key: zumbo1999handbook
518	    category: dif_methodology
519	    role: foundation
520	    relevance: Foundational DIF handbook presenting logistic regression as a unitary
521	      framework for DIF analysis; establishes the Zumbo-Thomas logistic regression
522	      approach widely used in applied DIF research
523	    abstract: ''
524	    semantic_scholar_id: 7f88fb0ad98645582665532600d7c46406fa2db6
525	    verified: true
526	    added_by: literature-gap-fill
527	    added_at: '2026-05-21T03:21:36.315Z'
528	  meredith1993invariance:
529	    title: Measurement Invariance, Factor Analysis and Factorial Invariance
530	    authors:
531	    - Meredith, W.
532	    year: 1993
533	    venue: Psychometrika
534	    url: https://link.springer.com/article/10.1007/BF02294825
535	    doi: 10.1007/BF02294825
536	    bibtex_key: meredith1993invariance
537	    category: dif_methodology
538	    role: foundation
539	    relevance: Defines the measurement invariance hierarchy (configural, metric, scalar,
540	      strict factorial invariance); theoretical foundation linking DIF to latent variable
541	      fairness
542	    abstract: ''
543	    semantic_scholar_id: 7eb541983de0a39586a699e255563b26e9291340
544	    verified: true
545	    added_by: literature-gap-fill
546	    added_at: '2026-05-21T03:21:36.315Z'
547	  vandenberg2000invariance:
548	    title: 'A Review and Synthesis of the Measurement Invariance Literature: Suggestions,
549	      Practices, and Recommendations for Organizational Research'
550	    authors:
551	    - Vandenberg, R.J.
552	    - Lance, C.E.
553	    year: 2000
554	    venue: Organizational Research Methods
555	    url: https://journals.sagepub.com/doi/10.1177/109442810031002
556	    doi: 10.1177/109442810031002
557	    bibtex_key: vandenberg2000invariance
558	    category: dif_methodology
559	    role: foundation
560	    relevance: Comprehensive review of measurement invariance testing practices; establishes
561	      CFA-based invariance testing as prerequisite for valid cross-group comparisons,
562	      analogous to our cross-model DIF analysis
563	    abstract: ''
564	    semantic_scholar_id: 1c9389250c1fac06eda5dcf39a8ea16cf8c92c89
565	    verified: true
566	    added_by: literature-gap-fill
567	    added_at: '2026-05-21T03:21:36.315Z'
568	  swaminathan1990logistic:
569	    title: Detecting Differential Item Functioning Using Logistic Regression Procedures
570	    authors:
571	    - Swaminathan, H.
572	    - Rogers, H.J.
573	    year: 1990
574	    venue: Journal of Educational Measurement
575	    url: https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1745-3984.1990.tb00754.x
576	    doi: 10.1111/j.1745-3984.1990.tb00754.x
577	    bibtex_key: swaminathan1990logistic
578	    category: dif_methodology
579	    role: foundation
580	    relevance: Introduces logistic regression for DIF detection, distinguishing uniform
581	      and non-uniform DIF; more powerful than MH for non-uniform DIF and directly
582	      applicable to our contamination-as-DIF framework
583	    abstract: ''
584	    semantic_scholar_id: d14b3b6e927ff8e51406fad1010244ecabc07da0
585	    verified: true
586	    added_by: literature-gap-fill
587	    added_at: '2026-05-21T03:21:36.315Z'
588	  teresi2007dif:
589	    title: Differential Item Functioning and Health Assessment
590	    authors:
591	    - Teresi, J.A.
592	    - Fleishman, J.A.
593	    year: 2007
594	    venue: Quality of Life Research
595	    url: https://link.springer.com/article/10.1007/s11136-007-9184-6
596	    doi: 10.1007/s11136-007-9184-6
597	    bibtex_key: teresi2007dif
598	    category: dif_methodology
599	    role: method-component
600	    relevance: Reviews DIF detection strategies including propensity score matching
601	      approaches for controlling confounders; methodological basis for our propensity-matched
602	      contamination group comparison
603	    abstract: ''
604	    semantic_scholar_id: 5ddbe080c2c0cdff671d9b9c2a795e366b6eb098
605	    verified: true
606	    added_by: literature-gap-fill
607	    added_at: '2026-05-21T03:21:36.315Z'
608	  lord1980irt:
609	    title: Applications of Item Response Theory to Practical Testing Problems
610	    authors:
611	    - Lord, F.M.
612	    year: 1980
613	    venue: 'Hillsdale, NJ: Lawrence Erlbaum Associates'
614	    url: https://www.routledge.com/Applications-of-Item-Response-Theory-To-Practical-Testing-Problems/Lord/p/book/9780898590067
615	    doi: ''
616	    bibtex_key: lord1980irt
617	    category: dif_methodology
618	    role: foundation
619	    relevance: Introduces Lord's chi-square test for IRT-based DIF detection by comparing
620	      item parameters across groups; foundational IRT reference for our parametric
621	      DIF approach
622	    abstract: ''
623	    semantic_scholar_id: ''
624	    verified: true
625	    added_by: literature-gap-fill
626	    added_at: '2026-05-21T03:21:36.315Z'
627	  raju1988area:
628	    title: The Area between Two Item Characteristic Curves
629	    authors:
630	    - Raju, N.S.
631	    year: 1988
632	    venue: Psychometrika
633	    url: https://link.springer.com/article/10.1007/BF02294403
634	    doi: 10.1007/BF02294403
635	    bibtex_key: raju1988area
636	    category: dif_methodology
637	    role: method-component
638	    relevance: Develops signed and unsigned area measures between item characteristic
639	      curves for IRT-based DIF quantification; provides effect-size metrics complementing
640	      statistical significance tests
641	    abstract: ''
642	    semantic_scholar_id: 545c20c1f2575833f81418f4757cb78446465cd7
643	    verified: true
644	    added_by: literature-gap-fill
645	    added_at: '2026-05-21T03:21:36.315Z'
646	  muthen1985mimic:
647	    title: A Method for Studying the Homogeneity of Test Items with Respect to Other
648	      Relevant Variables
649	    authors:
650	    - Muthén, B.
651	    year: 1985
652	    venue: Journal of Educational Statistics
653	    url: ''
654	    doi: 10.2307/1164966
655	    bibtex_key: muthen1985mimic
656	    category: dif_methodology
657	    role: method-component
658	    relevance: Seminal MIMIC model for DIF with continuous covariates; future-work
659	      alternative to failed θ-conditioning (plan_012)
660	    abstract: ''
661	    semantic_scholar_id: ''
662	    verified: true
663	    added_by: paper_agent
664	    added_at: '2026-05-21T03:34:08.189Z'
665	  woods2009mimic:
666	    title: Empirical Selection of Anchors for Tests of Differential Item Functioning
667	    authors:
668	    - Woods, C.M.
669	    year: 2009
670	    venue: Applied Psychological Measurement
671	    url: ''
672	    doi: 10.1177/0146621609331279
673	    bibtex_key: woods2009mimic
674	    category: dif_methodology
675	    role: method-component
676	    relevance: Modern MIMIC-based DIF detection with anchor selection; addresses impact-vs-DIF
677	      confound in our future work
678	    abstract: ''
679	    semantic_scholar_id: ''
680	    verified: true
681	    added_by: paper_agent
682	    added_at: '2026-05-21T03:34:08.189Z'
683	  habba2026growingpains:
684	    abstract: ''
685	    added_at: '2026-05-20T17:30:00.000Z'
686	    added_by: director
687	    authors:
688	    - Habba, E.
689	    - Itzhak, I.
690	    - Yehudai, A.
691	    - Perlitz, Y.
692	    - Bandel, E.
693	    - Shmueli-Scheuer, M.
694	    - Choshen, L.
695	    - Stanovsky, G.
696	    bibtex_key: habba2026growingpains
697	    category: irt_equating
698	    doi: 10.48550/arXiv.2604.12843
699	    relevance: Uses multidimensional IRT with fixed-parameter calibration and 100
700	      anchor items for extensible evaluation (rho>=0.9); addresses score comparability
701	      but NOT contamination detection or item regeneration
702	    role: direct-competitor
703	    semantic_scholar_id: ''
704	    title: 'Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter
705	      Calibration'
706	    url: https://arxiv.org/abs/2604.12843
707	    venue: arXiv
708	    verified: true
709	    year: 2026
710	  zhou2026psnirt:
711	    abstract: ''
712	    added_at: '2026-05-20T17:30:00.000Z'
713	    added_by: director
714	    authors:
715	    - Zhou, H.
716	    - Huang, H.
717	    - Zhao, Z.
718	    - Han, L.
719	    - Wang, H.
720	    - Chen, K.
721	    - Yang, M.
722	    - Bao, W.
723	    - Dong, J.
724	    - Xu, B.
725	    - Zhu, C.
726	    - Cao, H.
727	    - Zhao, T.
728	    bibtex_key: zhou2026psnirt
729	    category: irt_equating
730	    doi: ''
731	    relevance: PSN-IRT analyzes benchmark quality via 4PL IRT; provides published
732	      IRT parameters for MMLU we can use in semi-synthetic validation
733	    role: method-component
734	    semantic_scholar_id: ''
735	    title: Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item
736	      Response Theory
737	    url: https://arxiv.org/abs/2505.15055
738	    venue: AAAI 2026
739	    verified: true
740	    year: 2026
741	  kipnis2024metabench:
742	    title: metabench -- A Sparse Benchmark of Reasoning and Knowledge in Large Language
743	      Models
744	    authors:
745	    - Kipnis, A.
746	    - Voudouris, K.
747	    - Schulze Buschoff, L.M.
748	    - Schulz, E.
749	    year: 2024
750	    venue: arXiv
751	    url: https://arxiv.org/abs/2407.12844
752	    doi: 10.48550/arXiv.2407.12844
753	    bibtex_key: kipnis2024metabench
754	    category: benchmark_design
755	    role: foundation
756	    relevance: Primary data source providing item-level response matrix across 5000+
757	      LLMs on 6 benchmarks; IRT-based item selection methodology enables our DIF analysis
758	      on compressed benchmark items
759	    abstract: ''
760	    semantic_scholar_id: dfd5186def202285a0f23cd3f08415a5780895c1
761	    verified: true
762	    added_by: literature-gap-fill
763	    added_at: '2026-05-21T03:43:39.896Z'
764	  hendrycks2021mmlu:
765	    title: Measuring Massive Multitask Language Understanding
766	    authors:
767	    - Hendrycks, D.
768	    - Burns, C.
769	    - Basart, S.
770	    - Zou, A.
771	    - Mazeika, M.
772	    - Song, D.
773	    - Steinhardt, J.
774	    year: 2021
775	    venue: ICLR 2021
776	    url: https://arxiv.org/abs/2009.03300
777	    doi: ''
778	    bibtex_key: hendrycks2021mmlu
779	    category: benchmark_design
780	    role: foundation
781	    relevance: Seminal 57-subject benchmark for LLM evaluation; primary benchmark
782	      in our DIF analysis due to documented contamination and available IRT parameters
783	    abstract: ''
784	    semantic_scholar_id: 814a4f680b9ba6baba23b93499f4b48af1a27678
785	    verified: true
786	    added_by: literature-gap-fill
787	    added_at: '2026-05-21T03:43:39.896Z'
788	  liang2023helm:
789	    title: Holistic Evaluation of Language Models
790	    authors:
791	    - Liang, P.
792	    - Bommasani, R.
793	    - Lee, T.
794	    - Tsipras, D.
795	    - Soylu, D.
796	    - Yasunaga, M.
797	    - Zhang, Y.
798	    - Narayanan, D.
799	    - Wu, Y.
800	    - Kumar, A.
801	    year: 2023
802	    venue: TMLR 2023
803	    url: https://arxiv.org/abs/2211.09110
804	    doi: 10.1111/nyas.15007
805	    bibtex_key: liang2023helm
806	    category: benchmark_design
807	    role: foundation
808	    relevance: Holistic multi-metric evaluation framework covering accuracy, calibration,
809	      robustness, fairness, and bias; establishes multi-dimensional evaluation philosophy
810	      complementary to our psychometric approach
811	    abstract: ''
812	    semantic_scholar_id: ce913026f693101e54d3ab9152e107034d81fce1
813	    verified: true
814	    added_by: literature-gap-fill
815	    added_at: '2026-05-21T03:43:39.896Z'
816	  chiang2024chatbot:
817	    title: 'Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference'
818	    authors:
819	    - Chiang, W.-L.
820	    - Zheng, L.
821	    - Sheng, Y.
822	    - Angelopoulos, A.N.
823	    - Li, T.
824	    - Li, D.
825	    - Zhang, H.
826	    - Zhu, B.
827	    - Jordan, M.I.
828	    - Gonzalez, J.E.
829	    - Stoica, I.
830	    year: 2024
831	    venue: ICML 2024
832	    url: https://arxiv.org/abs/2403.04132
833	    doi: 10.48550/arXiv.2403.04132
834	    bibtex_key: chiang2024chatbot
835	    category: benchmark_design
836	    role: method-component
837	    relevance: Crowdsourced pairwise comparison with ELO ranking as contamination-resistant
838	      alternative to static benchmarks; contrasts with our item-level psychometric
839	      approach
840	    abstract: ''
841	    semantic_scholar_id: 53f4fb0e9972989194368faf288ff8e3cba5bd60
842	    verified: true
843	    added_by: literature-gap-fill
844	    added_at: '2026-05-21T03:43:39.896Z'
845	  mialon2023gaia:
846	    title: 'GAIA: a benchmark for General AI Assistants'
847	    authors:
848	    - Mialon, G.
849	    - Fourrier, C.
850	    - Swift, C.
851	    - Wolf, T.
852	    - LeCun, Y.
853	    - Scialom, T.
854	    year: 2023
855	    venue: arXiv
856	    url: https://arxiv.org/abs/2311.12983
857	    doi: 10.48550/arXiv.2311.12983
858	    bibtex_key: mialon2023gaia
859	    category: benchmark_design
860	    role: method-component
861	    relevance: Benchmark with verifiable ground-truth answers designed to resist memorization;
862	      exemplifies objective-scoring benchmark design philosophy shared by our regenerated
863	      items
864	    abstract: ''
865	    semantic_scholar_id: ab8169d6e4dfabfe7c30ebec1bb871bf3e1551cd
866	    verified: true
867	    added_by: literature-gap-fill
868	    added_at: '2026-05-21T03:43:39.896Z'
869	  li2024latesteval:
870	    title: 'LatestEval: Addressing Data Contamination in Language Model Evaluation
871	      through Dynamic and Time-Sensitive Test Construction'
872	    authors:
873	    - Li, Y.
874	    - Guerin, F.
875	    - Lin, C.
876	    year: 2024
877	    venue: AAAI 2024
878	    url: https://arxiv.org/abs/2312.12343
879	    doi: 10.48550/arXiv.2312.12343
880	    bibtex_key: li2024latesteval
881	    category: benchmark_design
882	    role: direct-competitor
883	    relevance: Automated dynamic test construction from recent texts to avoid contamination;
884	      addresses temporal contamination but lacks psychometric difficulty calibration
885	      across test versions
886	    abstract: ''
887	    semantic_scholar_id: 8106d03fb984afd8c3d066cd4f993eb2616a0da5
888	    verified: true
889	    added_by: literature-gap-fill
890	    added_at: '2026-05-21T03:43:39.896Z'
891	  kiela2021dynabench:
892	    title: 'Dynabench: Rethinking Benchmarking in NLP'
893	    authors:
894	    - Kiela, D.
895	    - Bartolo, M.
896	    - Nie, Y.
897	    - Kaushik, D.
898	    - Geiger, A.
899	    - Wu, Z.
900	    - Vidgen, B.
901	    - Prasad, G.
902	    - Singh, A.
903	    - Ringshia, P.
904	    - Ma, Z.
905	    - Thrush, T.
906	    - Riedel, S.
907	    - Talat, Z.
908	    - Stenetorp, P.
909	    - Jia, R.
910	    year: 2021
911	    venue: NAACL 2021
912	    url: https://arxiv.org/abs/2104.14337
913	    doi: 10.18653/v1/2021.naacl-main.324
914	    bibtex_key: kiela2021dynabench
915	    category: benchmark_design
916	    role: foundation
917	    relevance: Seminal dynamic adversarial benchmarking platform with human-and-model-in-the-loop
918	      dataset creation; establishes the paradigm of continuously evolving benchmarks
919	      that our IRT-equated regeneration extends with psychometric equivalence guarantees
920	    abstract: ''
921	    semantic_scholar_id: 77a096d80eb4dd4ccd103d1660c5a5498f7d026b
922	    verified: true
923	    added_by: literature-gap-fill
924	    added_at: '2026-05-21T03:43:39.896Z'
925	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ca6fa12b-f060-44ff-a3f8-2be93538cabe",
  "uuid": "40956cf5-4851-4cec-9408-38c6650830ec",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/literature_map.yaml",
      "content": "categories:\n- key: contamination_detection\n  name: Benchmark Contamination Detection\n  narrative: Methods for detecting training data contamination in LLM benchmarks,\n    including RL-robust approaches\n- key: irt_equating\n  name: IRT Methodology & Equating\n  narrative: Item Response Theory models, calibration, equating, and their application\n    to LLM evaluation\n- key: benchmark_design\n  name: Dynamic Benchmark Design\n  narrative: Approaches for creating contamination-resistant or self-updating benchmarks\n- key: dif_methodology\n  name: DIF Statistical Methods\n  narrative: Differential Item Functioning detection methods, power analysis, and\n    small-sample strategies\n- key: item_generation\n  name: Automated Item Generation\n  narrative: LLM-based test item generation with difficulty control and psychometric\n    validation\nmeta:\n  last_updated: '2026-05-21T03:43:39.944Z'\n  total_papers: 40\npapers:\n  balloccu2024leak:\n    abstract: ''\n    added_at: '2026-05-21T01:40:37.987Z'\n    added_by: literature-gap-fill\n    authors:\n    - Balloccu, S.\n    - Schmidtova, P.\n    - Lango, M.\n    - Dusek, O.\n    bibtex_key: balloccu2024leak\n    category: contamination_detection\n    doi: 10.18653/v1/2024.eacl-long.5\n    relevance: Systematic survey of data leakage in closed-source LLMs covering 255\n      papers and 263 benchmarks; establishes scope of contamination problem motivating\n      our detection approach\n    role: foundation\n    semantic_scholar_id: 798feda076ad710df65d509a7884bd15937c8056\n    title: 'Leak, Cheat, Repeat: Data Contamination and Evaluation Malpractices in\n      Closed-Source LLMs'\n    url: https://arxiv.org/abs/2402.03927\n    venue: EACL 2024\n    verified: true\n    year: 2024\n  belzak2020smallsample:\n    abstract: ''\n    added_at: '2026-05-20T17:30:00.000Z'\n    added_by: director\n    authors:\n    - Belzak, W.\n    bibtex_key: belzak2020smallsample\n    category: dif_methodology\n    doi: 10.1080/00273171.2019.1671162\n    relevance: Parsimonious logistic regression with sum scores outperforms complex\n      IRT models for DIF detection in small samples; directly applicable to our N=50-80\n      model cohorts\n    role: method-component\n    semantic_scholar_id: 8f13882b6f37be1ade68c40539156277e5723395\n    title: Testing Differential Item Functioning in Small Samples\n    url: https://www.tandfonline.com/doi/abs/10.1080/00273171.2019.1671162\n    venue: Multivariate Behavioral Research\n    verified: true\n    year: 2020\n  dekoninck2024constat:\n    abstract: ''\n    added_at: '2026-05-21T01:40:37.987Z'\n    added_by: literature-gap-fill\n    authors:\n    - Dekoninck, J.\n    - Mueller, M. N.\n    - Vechev, M.\n    bibtex_key: dekoninck2024constat\n    category: contamination_detection\n    doi: ''\n    relevance: Performance-based contamination detection via perturbation analysis;\n      closest methodological parallel to our DIF approach in using behavioral patterns\n      rather than memorization signals\n    role: direct-competitor\n    semantic_scholar_id: ''\n    title: 'ConStat: Performance-Based Contamination Detection in Large Language Models'\n    url: https://arxiv.org/abs/2405.16281\n    venue: NeurIPS 2024\n    verified: true\n    year: 2024\n  golchin2024timetravel:\n    abstract: ''\n    added_at: '2026-05-21T01:40:37.987Z'\n    added_by: literature-gap-fill\n    authors:\n    - Golchin, S.\n    - Surdeanu, M.\n    bibtex_key: golchin2024timetravel\n    category: contamination_detection\n    doi: ''\n    relevance: Instance-level contamination detection via guided completion prompts;\n      baseline approach for individual-item detection that our group-level DIF method\n      extends\n    role: method-component\n    semantic_scholar_id: d6d0fd994f37b630f35945736b5e1bb198148404\n    title: 'Time Travel in LLMs: Tracing Data Contamination in Large Language Models'\n    url: https://arxiv.org/abs/2308.08493\n    venue: ICLR 2024\n    verified: true\n    year: 2024\n  hardy2026scalability:\n    abstract: ''\n    added_at: '2026-05-20T17:30:00.000Z'\n    added_by: director\n    authors:\n    - Hardy, M.\n    - Gilbert, J.\n    - Domingue, B.\n    bibtex_key: hardy2026scalability\n    category: irt_equating\n    doi: 10.48550/arXiv.2603.24999\n    relevance: Nonparametric signed isotonic R2 scalability coefficients outperform\n      IRT item diagnostics; lightweight pre-filter for item quality before our parametric\n      calibration\n    role: method-component\n    semantic_scholar_id: ''\n    title: Efficient Detection of Bad Benchmark Items with Novel Scalability Coefficients\n    url: https://arxiv.org/abs/2603.24999\n    venue: arXiv\n    verified: true\n    year: 2026\n  kim2019fpc:\n    abstract: ''\n    added_at: '2026-05-20T17:30:00.000Z'\n    added_by: director\n    authors:\n    - Kim, S.\n    - Kolen, M.\n    bibtex_key: kim2019fpc\n    category: irt_equating\n    doi: 10.1080/08957347.2019.1660344\n    relevance: Fixed-parameter calibration requires only N>=200 vs N>=500 for full\n      calibration; core methodology for our bifactor IRT equating with anchor items\n    role: method-component\n    semantic_scholar_id: ''\n    title: Application of IRT Fixed Parameter Calibration to Multiple-Group Test Data\n    url: https://www.tandfonline.com/doi/abs/10.1080/08957347.2019.1660344\n    venue: Applied Measurement in Education\n    verified: true\n    year: 2019\n  li2024contamination:\n    abstract: ''\n    added_at: '2026-05-21T01:40:37.987Z'\n    added_by: literature-gap-fill\n    authors:\n    - Li, Y.\n    - Guo, Y.\n    - Guerin, F.\n    - Lin, C.\n    bibtex_key: li2024contamination\n    category: contamination_detection\n    doi: 10.18653/v1/2024.findings-emnlp.30\n    relevance: Provides web-overlap contamination labels for MMLU and other benchmarks\n      via Common Crawl matching; primary ground-truth comparison for our DIF-based\n      contamination detection\n    role: foundation\n    semantic_scholar_id: 32e11cf020021c225782a3b77b5cfed4ae8e14a0\n    title: An Open-Source Data Contamination Report for Large Language Models\n    url: https://aclanthology.org/2024.findings-emnlp.30/\n    venue: Findings of EMNLP 2024\n    verified: true\n    year: 2024\n  liang2026dvd:\n    abstract: ''\n    added_at: '2026-05-20T17:30:00.000Z'\n    added_by: director\n    authors:\n    - Liang, R.\n    bibtex_key: liang2026dvd\n    category: contamination_detection\n    doi: ''\n    relevance: Detects variant contamination via generation variance (AUC 0.73-0.74\n      vs Min-K++ 0.43-0.68); complementary signal in our ensemble but untested under\n      RL training\n    role: direct-competitor\n    semantic_scholar_id: ''\n    title: 'DVD: Detection via Variance of Generation Distribution for Variant Contamination'\n    url: https://arxiv.org/abs/2601.04895\n    venue: arXiv\n    verified: true\n    year: 2026\n  shi2024mink:\n    abstract: ''\n    added_at: '2026-05-21T01:40:37.987Z'\n    added_by: literature-gap-fill\n    authors:\n    - Shi, W.\n    - Ajith, A.\n    - Xia, M.\n    - Huang, Y.\n    - Liu, D.\n    - Blevins, T.\n    - Chen, D.\n    - Zettlemoyer, L.\n    bibtex_key: shi2024mink\n    category: contamination_detection\n    doi: ''\n    relevance: Introduces Min-K% Prob method and WikiMIA benchmark for pretraining\n      data detection; key baseline whose limitations under RL training motivate our\n      DIF-based alternative\n    role: foundation\n    semantic_scholar_id: 3422d5e0cdfdc935d6a84a1e3d3f96659265fe3a\n    title: Detecting Pretraining Data from Large Language Models\n    url: https://arxiv.org/abs/2310.16789\n    venue: ICLR 2024\n    verified: true\n    year: 2024\n  tao2026selfcritique:\n    abstract: ''\n    added_at: '2026-05-20T17:30:00.000Z'\n    added_by: director\n    authors:\n    - Tao, Y.\n    bibtex_key: tao2026selfcritique\n    category: contamination_detection\n    doi: ''\n    relevance: Self-Critique/RL-MIA partially addresses RL concealment via policy-collapse\n      detection, but remains individual-model-level; our DIF is group-level and complementary\n    role: direct-competitor\n    semantic_scholar_id: ''\n    title: Detecting Data Contamination from Reinforcement Learning Post-training\n      for Large Language Models\n    url: https://arxiv.org/abs/2510.09259\n    venue: ICLR 2026\n    verified: true\n    year: 2026\n  wang2026fragility:\n    abstract: ''\n    added_at: '2026-05-20T17:30:00.000Z'\n    added_by: director\n    authors:\n    - Wang, H.\n    - Li, H.\n    - Ko, B.\n    - Zhang, H.\n    bibtex_key: wang2026fragility\n    category: contamination_detection\n    doi: ''\n    relevance: Proves GRPO/PPO RL training conceals contamination signals (14-20pp\n      AUROC degradation), motivating our DIF-based approach which operates on behavioral\n      patterns immune to NLL smoothing\n    role: foundation\n    semantic_scholar_id: 9a5bf5d3c7116cc4a104c06599fbcef2d1b5abf3\n    title: On The Fragility of Benchmark Contamination Detection in Reasoning Models\n    url: https://arxiv.org/abs/2510.02386\n    venue: ICLR 2026\n    verified: true\n    year: 2026\n  white2025livebench:\n    abstract: ''\n    added_at: '2026-05-20T17:30:00.000Z'\n    added_by: director\n    authors:\n    - White, C.\n    bibtex_key: white2025livebench\n    category: benchmark_design\n    doi: 10.48550/arXiv.2406.19314\n    relevance: Monthly-updated contamination-free benchmark with objective scoring;\n      no difficulty calibration or psychometric equivalence across updates\n    role: direct-competitor\n    semantic_scholar_id: 4e5d86ea8eacd341d13123852d50d1ef62738744\n    title: 'LiveBench: A Challenging, Contamination-Free LLM Benchmark'\n    url: https://arxiv.org/abs/2406.19314\n    venue: ICLR 2025\n    verified: true\n    year: 2025\n  zhang2024gsm1k:\n    abstract: ''\n    added_at: '2026-05-20T17:30:00.000Z'\n    added_by: director\n    authors:\n    - Zhang, H.\n    bibtex_key: zhang2024gsm1k\n    category: contamination_detection\n    doi: ''\n    relevance: GSM1K documents 10-13% average accuracy drops from contamination; provides\n      ground-truth contamination evidence and item-level effect sizes (delta 0.8-1.4\n      logits) critical for our DIF power analysis\n    role: foundation\n    semantic_scholar_id: ef62f95c16f668f031d649799cbd79081c6d2b0f\n    title: A Careful Examination of Large Language Model Performance on Grade School\n      Arithmetic\n    url: https://arxiv.org/abs/2405.00332\n    venue: arXiv\n    verified: true\n    year: 2024\n  zhang2024minkpp:\n    abstract: ''\n    added_at: '2026-05-21T01:40:37.987Z'\n    added_by: literature-gap-fill\n    authors:\n    - Zhang, J.\n    - Sun, J.\n    - Yeats, E.\n    - Ouyang, Y.\n    - Kuo, M.\n    - Zhang, J.\n    - Yang, H.\n    - Li, H.\n    bibtex_key: zhang2024minkpp\n    category: contamination_detection\n    doi: ''\n    relevance: Improves Min-K% with vocabulary-normalized token probabilities; key\n      baseline whose AUC degrades to 0.43-0.68 on RL-trained models, motivating our\n      DIF-based alternative\n    role: direct-competitor\n    semantic_scholar_id: ''\n    title: 'Min-K%++: Improved Baseline for Detecting Pre-Training Data from Large\n      Language Models'\n    url: https://arxiv.org/abs/2404.02936\n    venue: arXiv\n    verified: true\n    year: 2024\n  lalor2019irt:\n    title: 'Learning Latent Parameters without Human Response Patterns: Item Response\n      Theory with Artificial Crowds'\n    authors:\n    - Lalor, J.\n    - Wu, H.\n    - Yu, H.\n    year: 2019\n    venue: EMNLP-IJCNLP 2019\n    url: https://aclanthology.org/D19-1434/\n    doi: 10.18653/v1/D19-1434\n    bibtex_key: lalor2019irt\n    category: irt_equating\n    role: foundation\n    relevance: Pioneering application of IRT to NLP evaluation using artificial crowds\n      of DNN models; establishes that IRT parameters from machine response patterns\n      correlate with human-calibrated parameters\n    abstract: ''\n    semantic_scholar_id: df6cd8a8d836e75690141deb732f6d19f0176a2e\n    verified: true\n    added_by: literature-gap-fill\n    added_at: '2026-05-21T02:29:19.632Z'\n  vania2021irt:\n    title: Comparing Test Sets with Item Response Theory\n    authors:\n    - Vania, C.\n    - Htut, P.M.\n    - Huang, W.\n    - Mungra, D.\n    - Pang, R.Y.\n    - Phang, J.\n    - Liu, H.\n    - Cho, K.\n    - Bowman, S.R.\n    year: 2021\n    venue: ACL 2021\n    url: https://aclanthology.org/2021.acl-long.92/\n    doi: 10.18653/v1/2021.acl-long.92\n    bibtex_key: vania2021irt\n    category: irt_equating\n    role: foundation\n    relevance: IRT-based analysis of NLU benchmark discriminability; shows which test\n      sets remain effective at differentiating strong models and which are saturated\n    abstract: ''\n    semantic_scholar_id: 4ca39cf99747b8962fe37e7e025e284872df3425\n    verified: true\n    added_by: literature-gap-fill\n    added_at: '2026-05-21T02:29:19.632Z'\n  li2025atlas:\n    title: 'Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static\n      Benchmarks'\n    authors:\n    - Li, P.\n    - Tang, X.\n    - Chen, S.\n    - Cheng, Y.\n    - Metoyer, R.\n    - Hua, T.\n    - Chawla, N.V.\n    year: 2025\n    venue: arXiv\n    url: https://arxiv.org/abs/2511.04689\n    doi: 10.48550/arXiv.2511.04689\n    bibtex_key: li2025atlas\n    category: irt_equating\n    role: method-component\n    relevance: IRT-based adaptive testing framework (ATLAS) reduces benchmark items\n      by 90% while preserving ability estimates; demonstrates IRT enables efficient\n      LLM evaluation\n    abstract: ''\n    semantic_scholar_id: 087ce2837a0d5562bc95a40e77a327a6d033366c\n    verified: true\n    added_by: literature-gap-fill\n    added_at: '2026-05-21T02:29:19.632Z'\n  chen2025irtnet:\n    title: Learning Compact Representations of LLM Abilities via Item Response Theory\n    authors:\n    - Chen, J.\n    - Wang, C.\n    - Zhang, G.\n    - Ye, P.\n    - Bai, L.\n    - Hu, W.\n    - Qu, Y.\n    - Hu, S.\n    year: 2025\n    venue: arXiv\n    url: https://arxiv.org/abs/2510.00844\n    doi: 10.48550/arXiv.2510.00844\n    bibtex_key: chen2025irtnet\n    category: irt_equating\n    role: method-component\n    relevance: Multidimensional IRT with MoE network for learning LLM ability vectors\n      and query discrimination/difficulty; demonstrates IRT-based model routing and\n      benchmark prediction\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: literature-gap-fill\n    added_at: '2026-05-21T02:29:19.632Z'\n  choi2026llmjudgeirt:\n    title: Diagnosing the Reliability of LLM-as-a-Judge via Item Response Theory\n    authors:\n    - Choi, J.\n    - Park, S.\n    - Cho, C.\n    - Park, H.\n    - Kim, B.\n    year: 2026\n    venue: arXiv\n    url: https://arxiv.org/abs/2602.00521\n    doi: 10.48550/arXiv.2602.00521\n    bibtex_key: choi2026llmjudgeirt\n    category: irt_equating\n    role: method-component\n    relevance: Applies IRT Graded Response Model to diagnose LLM judge reliability;\n      extends IRT application beyond benchmark scoring to evaluation pipeline quality\n      assessment\n    abstract: ''\n    semantic_scholar_id: 4fc931a456c8162716deadbc9db6fd770189e632\n    verified: true\n    added_by: literature-gap-fill\n    added_at: '2026-05-21T02:29:19.632Z'\n  holland1988mh:\n    title: Differential Item Functioning and the Mantel-Haenszel Procedure\n    authors:\n    - Holland, P.W.\n    - Thayer, D.T.\n    year: 1988\n    venue: In H. Wainer & H.I. Braun (Eds.), Test Validity, Lawrence Erlbaum\n    url: https://onlinelibrary.wiley.com/doi/abs/10.1002/j.2330-8516.1986.tb00186.x\n    doi: 10.1002/j.2330-8516.1986.tb00186.x\n    bibtex_key: holland1988mh\n    category: dif_methodology\n    role: foundation\n    relevance: Seminal paper introducing the Mantel-Haenszel procedure for DIF detection;\n      establishes the ETS classification system (A/B/C) used as standard DIF effect-size\n      metric\n    abstract: ''\n    semantic_scholar_id: 5fbc064e7104036b77a2bf6f0ad509031965c275\n    verified: true\n    added_by: literature-gap-fill\n    added_at: '2026-05-21T03:21:36.315Z'\n  shealy1993sibtest:\n    title: A Model-Based Standardization Approach that Separates True Bias/DIF from\n      Group Ability Differences and Detects Test Bias/DTF as Well as Item Bias/DIF\n    authors:\n    - Shealy, R.\n    - Stout, W.\n    year: 1993\n    venue: Psychometrika\n    url: https://link.springer.com/article/10.1007/BF02294572\n    doi: 10.1007/BF02294572\n    bibtex_key: shealy1993sibtest\n    category: dif_methodology\n    role: foundation\n    relevance: Introduces SIBTEST, a nonparametric DIF detection method that separates\n      true item bias from group ability differences; alternative to MH that handles\n      non-uniform DIF\n    abstract: ''\n    semantic_scholar_id: 82f3db496626afd828fedb01a41f719a50dbfc2c\n    verified: true\n    added_by: literature-gap-fill\n    added_at: '2026-05-21T03:21:36.315Z'\n  clauser1998dif:\n    title: Using Statistical Procedures to Identify Differentially Functioning Test\n      Items\n    authors:\n    - Clauser, B.E.\n    - Mazor, K.M.\n    year: 1998\n    venue: 'Educational Measurement: Issues and Practice'\n    url: https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1745-3992.1998.tb00619.x\n    doi: 10.1111/j.1745-3992.1998.tb00619.x\n    bibtex_key: clauser1998dif\n    category: dif_methodology\n    role: foundation\n    relevance: Comprehensive review of DIF detection methods (MH, SIBTEST, logistic\n      regression, IRT-based); standard reference for comparing statistical approaches\n      to DIF\n    abstract: ''\n    semantic_scholar_id: c2377c505c95b924e972e61dadec81e9c87dea18\n    verified: true\n    added_by: literature-gap-fill\n    added_at: '2026-05-21T03:21:36.315Z'\n  zumbo1999handbook:\n    title: 'A Handbook on the Theory and Methods of Differential Item Functioning\n      (DIF): Logistic Regression Modeling as a Unitary Framework for Binary and Likert-Type\n      (Ordinal) Item Scores'\n    authors:\n    - Zumbo, B.D.\n    year: 1999\n    venue: 'Ottawa: Directorate of Human Resources Research and Evaluation, Department\n      of National Defense'\n    url: https://faculty.educ.ubc.ca/zumbo/DIF/handbook.pdf\n    doi: ''\n    bibtex_key: zumbo1999handbook\n    category: dif_methodology\n    role: foundation\n    relevance: Foundational DIF handbook presenting logistic regression as a unitary\n      framework for DIF analysis; establishes the Zumbo-Thomas logistic regression\n      approach widely used in applied DIF research\n    abstract: ''\n    semantic_scholar_id: 7f88fb0ad98645582665532600d7c46406fa2db6\n    verified: true\n    added_by: literature-gap-fill\n    added_at: '2026-05-21T03:21:36.315Z'\n  meredith1993invariance:\n    title: Measurement Invariance, Factor Analysis and Factorial Invariance\n    authors:\n    - Meredith, W.\n    year: 1993\n    venue: Psychometrika\n    url: https://link.springer.com/article/10.1007/BF02294825\n    doi: 10.1007/BF02294825\n    bibtex_key: meredith1993invariance\n    category: dif_methodology\n    role: foundation\n    relevance: Defines the measurement invariance hierarchy (configural, metric, scalar,\n      strict factorial invariance); theoretical foundation linking DIF to latent variable\n      fairness\n    abstract: ''\n    semantic_scholar_id: 7eb541983de0a39586a699e255563b26e9291340\n    verified: true\n    added_by: literature-gap-fill\n    added_at: '2026-05-21T03:21:36.315Z'\n  vandenberg2000invariance:\n    title: 'A Review and Synthesis of the Measurement Invariance Literature: Suggestions,\n      Practices, and Recommendations for Organizational Research'\n    authors:\n    - Vandenberg, R.J.\n    - Lance, C.E.\n    year: 2000\n    venue: Organizational Research Methods\n    url: https://journals.sagepub.com/doi/10.1177/109442810031002\n    doi: 10.1177/109442810031002\n    bibtex_key: vandenberg2000invariance\n    category: dif_methodology\n    role: foundation\n    relevance: Comprehensive review of measurement invariance testing practices; establishes\n      CFA-based invariance testing as prerequisite for valid cross-group comparisons,\n      analogous to our cross-model DIF analysis\n    abstract: ''\n    semantic_scholar_id: 1c9389250c1fac06eda5dcf39a8ea16cf8c92c89\n    verified: true\n    added_by: literature-gap-fill\n    added_at: '2026-05-21T03:21:36.315Z'\n  swaminathan1990logistic:\n    title: Detecting Differential Item Functioning Using Logistic Regression Procedures\n    authors:\n    - Swaminathan, H.\n    - Rogers, H.J.\n    year: 1990\n    venue: Journal of Educational Measurement\n    url: https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1745-3984.1990.tb00754.x\n    doi: 10.1111/j.1745-3984.1990.tb00754.x\n    bibtex_key: swaminathan1990logistic\n    category: dif_methodology\n    role: foundation\n    relevance: Introduces logistic regression for DIF detection, distinguishing uniform\n      and non-uniform DIF; more powerful than MH for non-uniform DIF and directly\n      applicable to our contamination-as-DIF framework\n    abstract: ''\n    semantic_scholar_id: d14b3b6e927ff8e51406fad1010244ecabc07da0\n    verified: true\n    added_by: literature-gap-fill\n    added_at: '2026-05-21T03:21:36.315Z'\n  teresi2007dif:\n    title: Differential Item Functioning and Health Assessment\n    authors:\n    - Teresi, J.A.\n    - Fleishman, J.A.\n    year: 2007\n    venue: Quality of Life Research\n    url: https://link.springer.com/article/10.1007/s11136-007-9184-6\n    doi: 10.1007/s11136-007-9184-6\n    bibtex_key: teresi2007dif\n    category: dif_methodology\n    role: method-component\n    relevance: Reviews DIF detection strategies including propensity score matching\n      approaches for controlling confounders; methodological basis for our propensity-matched\n      contamination group comparison\n    abstract: ''\n    semantic_scholar_id: 5ddbe080c2c0cdff671d9b9c2a795e366b6eb098\n    verified: true\n    added_by: literature-gap-fill\n    added_at: '2026-05-21T03:21:36.315Z'\n  lord1980irt:\n    title: Applications of Item Response Theory to Practical Testing Problems\n    authors:\n    - Lord, F.M.\n    year: 1980\n    venue: 'Hillsdale, NJ: Lawrence Erlbaum Associates'\n    url: https://www.routledge.com/Applications-of-Item-Response-Theory-To-Practical-Testing-Problems/Lord/p/book/9780898590067\n    doi: ''\n    bibtex_key: lord1980irt\n    category: dif_methodology\n    role: foundation\n    relevance: Introduces Lord's chi-square test for IRT-based DIF detection by comparing\n      item parameters across groups; foundational IRT reference for our parametric\n      DIF approach\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: literature-gap-fill\n    added_at: '2026-05-21T03:21:36.315Z'\n  raju1988area:\n    title: The Area between Two Item Characteristic Curves\n    authors:\n    - Raju, N.S.\n    year: 1988\n    venue: Psychometrika\n    url: https://link.springer.com/article/10.1007/BF02294403\n    doi: 10.1007/BF02294403\n    bibtex_key: raju1988area\n    category: dif_methodology\n    role: method-component\n    relevance: Develops signed and unsigned area measures between item characteristic\n      curves for IRT-based DIF quantification; provides effect-size metrics complementing\n      statistical significance tests\n    abstract: ''\n    semantic_scholar_id: 545c20c1f2575833f81418f4757cb78446465cd7\n    verified: true\n    added_by: literature-gap-fill\n    added_at: '2026-05-21T03:21:36.315Z'\n  muthen1985mimic:\n    title: A Method for Studying the Homogeneity of Test Items with Respect to Other\n      Relevant Variables\n    authors:\n    - Muthén, B.\n    year: 1985\n    venue: Journal of Educational Statistics\n    url: ''\n    doi: 10.2307/1164966\n    bibtex_key: muthen1985mimic\n    category: dif_methodology\n    role: method-component\n    relevance: Seminal MIMIC model for DIF with continuous covariates; future-work\n      alternative to failed θ-conditioning (plan_012)\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper_agent\n    added_at: '2026-05-21T03:34:08.189Z'\n  woods2009mimic:\n    title: Empirical Selection of Anchors for Tests of Differential Item Functioning\n    authors:\n    - Woods, C.M.\n    year: 2009\n    venue: Applied Psychological Measurement\n    url: ''\n    doi: 10.1177/0146621609331279\n    bibtex_key: woods2009mimic\n    category: dif_methodology\n    role: method-component\n    relevance: Modern MIMIC-based DIF detection with anchor selection; addresses impact-vs-DIF\n      confound in our future work\n    abstract: ''\n    semantic_scholar_id: ''\n    verified: true\n    added_by: paper_agent\n    added_at: '2026-05-21T03:34:08.189Z'\n  habba2026growingpains:\n    abstract: ''\n    added_at: '2026-05-20T17:30:00.000Z'\n    added_by: director\n    authors:\n    - Habba, E.\n    - Itzhak, I.\n    - Yehudai, A.\n    - Perlitz, Y.\n    - Bandel, E.\n    - Shmueli-Scheuer, M.\n    - Choshen, L.\n    - Stanovsky, G.\n    bibtex_key: habba2026growingpains\n    category: irt_equating\n    doi: 10.48550/arXiv.2604.12843\n    relevance: Uses multidimensional IRT with fixed-parameter calibration and 100\n      anchor items for extensible evaluation (rho>=0.9); addresses score comparability\n      but NOT contamination detection or item regeneration\n    role: direct-competitor\n    semantic_scholar_id: ''\n    title: 'Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter\n      Calibration'\n    url: https://arxiv.org/abs/2604.12843\n    venue: arXiv\n    verified: true\n    year: 2026\n  zhou2026psnirt:\n    abstract: ''\n    added_at: '2026-05-20T17:30:00.000Z'\n    added_by: director\n    authors:\n    - Zhou, H.\n    - Huang, H.\n    - Zhao, Z.\n    - Han, L.\n    - Wang, H.\n    - Chen, K.\n    - Yang, M.\n    - Bao, W.\n    - Dong, J.\n    - Xu, B.\n    - Zhu, C.\n    - Cao, H.\n    - Zhao, T.\n    bibtex_key: zhou2026psnirt\n    category: irt_equating\n    doi: ''\n    relevance: PSN-IRT analyzes benchmark quality via 4PL IRT; provides published\n      IRT parameters for MMLU we can use in semi-synthetic validation\n    role: method-component\n    semantic_scholar_id: ''\n    title: Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item\n      Response Theory\n    url: https://arxiv.org/abs/2505.15055\n    venue: AAAI 2026\n    verified: true\n    year: 2026\n  kipnis2024metabench:\n    title: metabench -- A Sparse Benchmark of Reasoning and Knowledge in Large Language\n      Models\n    authors:\n    - Kipnis, A.\n    - Voudouris, K.\n    - Schulze Buschoff, L.M.\n    - Schulz, E.\n    year: 2024\n    venue: arXiv\n    url: https://arxiv.org/abs/2407.12844\n    doi: 10.48550/arXiv.2407.12844\n    bibtex_key: kipnis2024metabench\n    category: benchmark_design\n    role: foundation\n    relevance: Primary data source providing item-level response matrix across 5000+\n      LLMs on 6 benchmarks; IRT-based item selection methodology enables our DIF analysis\n      on compressed benchmark items\n    abstract: ''\n    semantic_scholar_id: dfd5186def202285a0f23cd3f08415a5780895c1\n    verified: true\n    added_by: literature-gap-fill\n    added_at: '2026-05-21T03:43:39.896Z'\n  hendrycks2021mmlu:\n    title: Measuring Massive Multitask Language Understanding\n    authors:\n    - Hendrycks, D.\n    - Burns, C.\n    - Basart, S.\n    - Zou, A.\n    - Mazeika, M.\n    - Song, D.\n    - Steinhardt, J.\n    year: 2021\n    venue: ICLR 2021\n    url: https://arxiv.org/abs/2009.03300\n    doi: ''\n    bibtex_key: hendrycks2021mmlu\n    category: benchmark_design\n    role: foundation\n    relevance: Seminal 57-subject benchmark for LLM evaluation; primary benchmark\n      in our DIF analysis due to documented contamination and available IRT parameters\n    abstract: ''\n    semantic_scholar_id: 814a4f680b9ba6baba23b93499f4b48af1a27678\n    verified: true\n    added_by: literature-gap-fill\n    added_at: '2026-05-21T03:43:39.896Z'\n  liang2023helm:\n    title: Holistic Evaluation of Language Models\n    authors:\n    - Liang, P.\n    - Bommasani, R.\n    - Lee, T.\n    - Tsipras, D.\n    - Soylu, D.\n    - Yasunaga, M.\n    - Zhang, Y.\n    - Narayanan, D.\n    - Wu, Y.\n    - Kumar, A.\n    year: 2023\n    venue: TMLR 2023\n    url: https://arxiv.org/abs/2211.09110\n    doi: 10.1111/nyas.15007\n    bibtex_key: liang2023helm\n    category: benchmark_design\n    role: foundation\n    relevance: Holistic multi-metric evaluation framework covering accuracy, calibration,\n      robustness, fairness, and bias; establishes multi-dimensional evaluation philosophy\n      complementary to our psychometric approach\n    abstract: ''\n    semantic_scholar_id: ce913026f693101e54d3ab9152e107034d81fce1\n    verified: true\n    added_by: literature-gap-fill\n    added_at: '2026-05-21T03:43:39.896Z'\n  chiang2024chatbot:\n    title: 'Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference'\n    authors:\n    - Chiang, W.-L.\n    - Zheng, L.\n    - Sheng, Y.\n    - Angelopoulos, A.N.\n    - Li, T.\n    - Li, D.\n    - Zhang, H.\n    - Zhu, B.\n    - Jordan, M.I.\n    - Gonzalez, J.E.\n    - Stoica, I.\n    year: 2024\n    venue: ICML 2024\n    url: https://arxiv.org/abs/2403.04132\n    doi: 10.48550/arXiv.2403.04132\n    bibtex_key: chiang2024chatbot\n    category: benchmark_design\n    role: method-component\n    relevance: Crowdsourced pairwise comparison with ELO ranking as contamination-resistant\n      alternative to static benchmarks; contrasts with our item-level psychometric\n      approach\n    abstract: ''\n    semantic_scholar_id: 53f4fb0e9972989194368faf288ff8e3cba5bd60\n    verified: true\n    added_by: literature-gap-fill\n    added_at: '2026-05-21T03:43:39.896Z'\n  mialon2023gaia:\n    title: 'GAIA: a benchmark for General AI Assistants'\n    authors:\n    - Mialon, G.\n    - Fourrier, C.\n    - Swift, C.\n    - Wolf, T.\n    - LeCun, Y.\n    - Scialom, T.\n    year: 2023\n    venue: arXiv\n    url: https://arxiv.org/abs/2311.12983\n    doi: 10.48550/arXiv.2311.12983\n    bibtex_key: mialon2023gaia\n    category: benchmark_design\n    role: method-component\n    relevance: Benchmark with verifiable ground-truth answers designed to resist memorization;\n      exemplifies objective-scoring benchmark design philosophy shared by our regenerated\n      items\n    abstract: ''\n    semantic_scholar_id: ab8169d6e4dfabfe7c30ebec1bb871bf3e1551cd\n    verified: true\n    added_by: literature-gap-fill\n    added_at: '2026-05-21T03:43:39.896Z'\n  li2024latesteval:\n    title: 'LatestEval: Addressing Data Contamination in Language Model Evaluation\n      through Dynamic and Time-Sensitive Test Construction'\n    authors:\n    - Li, Y.\n    - Guerin, F.\n    - Lin, C.\n    year: 2024\n    venue: AAAI 2024\n    url: https://arxiv.org/abs/2312.12343\n    doi: 10.48550/arXiv.2312.12343\n    bibtex_key: li2024latesteval\n    category: benchmark_design\n    role: direct-competitor\n    relevance: Automated dynamic test construction from recent texts to avoid contamination;\n      addresses temporal contamination but lacks psychometric difficulty calibration\n      across test versions\n    abstract: ''\n    semantic_scholar_id: 8106d03fb984afd8c3d066cd4f993eb2616a0da5\n    verified: true\n    added_by: literature-gap-fill\n    added_at: '2026-05-21T03:43:39.896Z'\n  kiela2021dynabench:\n    title: 'Dynabench: Rethinking Benchmarking in NLP'\n    authors:\n    - Kiela, D.\n    - Bartolo, M.\n    - Nie, Y.\n    - Kaushik, D.\n    - Geiger, A.\n    - Wu, Z.\n    - Vidgen, B.\n    - Prasad, G.\n    - Singh, A.\n    - Ringshia, P.\n    - Ma, Z.\n    - Thrush, T.\n    - Riedel, S.\n    - Talat, Z.\n    - Stenetorp, P.\n    - Jia, R.\n    year: 2021\n    venue: NAACL 2021\n    url: https://arxiv.org/abs/2104.14337\n    doi: 10.18653/v1/2021.naacl-main.324\n    bibtex_key: kiela2021dynabench\n    category: benchmark_design\n    role: foundation\n    relevance: Seminal dynamic adversarial benchmarking platform with human-and-model-in-the-loop\n      dataset creation; establishes the paradigm of continuously evolving benchmarks\n      that our IRT-equated regeneration extends with psychometric equivalence guarantees\n    abstract: ''\n    semantic_scholar_id: 77a096d80eb4dd4ccd103d1660c5a5498f7d026b\n    verified: true\n    added_by: literature-gap-fill\n    added_at: '2026-05-21T03:43:39.896Z'\n",
      "numLines": 925,
      "startLine": 1,
      "totalLines": 925
    }
  }
}
```

</details>

---

### Assistant

_source line 60_

<details><summary>Logged reasoning block</summary>

```text
I can see that `zhou2026psnirt` (the "Lost in Benchmarks" paper) is already in the literature map under `irt_equating` category. So I should not add it again.

Now let me check which of my 5 candidates are already present:
1. Burnell et al. 2023 - NOT in the map
2. Chang et al. 2024 - NOT in the map
3. Polo et al. 2024 (tinyBenchmarks) - NOT in the map
4. Wang et al. 2024 (MMLU-Pro) - NOT in the map


5. Ott et al. 2022 - NOT in the map

All five are new additions. Now I'm gathering the DOI information and publication details for each paper to ensure accuracy before adding them to the map.

I've confirmed the details for most of them: Burnell et al. 2023 in Science, Chang et al. 2024 in ACM TIST, Maia Polo et al. 2024 from ICML proceedings, Wang et al. 2024 from NeurIPS, and Ott et al. 2022 in Nature Communications. Before I can add these to the literature map, I need to check whether the system automatically handles new categories or if I should create the 'llm_evaluation' category first through an upsert call.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ca6fa12b-f060-44ff-a3f8-2be93538cabe",
  "uuid": "2a41dac0-97a7-4b61-b6fb-f7c7129f1cd9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jev8iwSYiNQQFqj6kQR8U8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14319,
      "cache_read_input_tokens": 35275,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14319
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

_source line 61_

All 5 candidates are new to the literature map. I need to first add the `llm_evaluation` category, then add the papers. Let me check how `upsert_category` works.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ca6fa12b-f060-44ff-a3f8-2be93538cabe",
  "uuid": "b023fd66-1560-49d9-92a1-68c79505c6f5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jev8iwSYiNQQFqj6kQR8U8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14319,
      "cache_read_input_tokens": 35275,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14319
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

_source line 62_

<details open><summary>🔧 Tool call — Grep · `toolu_01Mbp4q4KNLCoPxGjEQurLk5`</summary>

```json
{
  "pattern": "def upsert_category",
  "path": "/home/ubuntu/agent-ml-research/core/tools/literature.py",
  "output_mode": "content",
  "-A": 10
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ca6fa12b-f060-44ff-a3f8-2be93538cabe",
  "uuid": "0c03fe2b-6a38-40e1-9d0b-bfe689909704",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jev8iwSYiNQQFqj6kQR8U8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14319,
      "cache_read_input_tokens": 35275,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14319
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

_source line 63 · 2026-05-21T03:49:55.382Z_

<details><summary>↩ Tool result · `toolu_01Mbp4q4KNLCoPxGjEQurLk5`</summary>

```text
565:def upsert_category(
566-    project: str | None = None,
567-    key: str = "",
568-    name: str = "",
569-    narrative: str = "",
570-) -> ToolResult:
571-    """Add or update a category entry in the categories[] list.
572-
573-    Categories define the Related Work subsection structure. A paper's
574-    ``category`` field references one of these by ``key``.
575-
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ca6fa12b-f060-44ff-a3f8-2be93538cabe",
  "uuid": "6a757897-043c-447b-a74e-11b963571772",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "565:def upsert_category(\n566-    project: str | None = None,\n567-    key: str = \"\",\n568-    name: str = \"\",\n569-    narrative: str = \"\",\n570-) -> ToolResult:\n571-    \"\"\"Add or update a category entry in the categories[] list.\n572-\n573-    Categories define the Related Work subsection structure. A paper's\n574-    ``category`` field references one of these by ``key``.\n575-",
    "numLines": 11
  }
}
```

</details>

---

### Assistant

_source line 64_

Now let me add the category and papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ca6fa12b-f060-44ff-a3f8-2be93538cabe",
  "uuid": "9bc41ff5-9441-4218-b6e2-a78f45523435",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BzZhLYpCpGh7nHBoH9QGAK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 847,
      "cache_read_input_tokens": 49594,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 847
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

_source line 65_

<details open><summary>🔧 Tool call — Bash · `toolu_01YRZJxidNtqPNCWxDRzBUYi`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0520_2 && python3 -c \"\nimport sys; sys.path.insert(0, '/home/ubuntu/agent-ml-research')\nfrom core.tools.literature import upsert_category\nresult = upsert_category(\n    project='irt_equated_bench_regen',\n    key='llm_evaluation',\n    name='LLM Evaluation Methodology',\n    narrative='General LLM evaluation methodology, benchmark psychometric analysis, evaluation surveys, and benchmark design principles'\n)\nprint(result)\n\"",
  "description": "Add llm_evaluation category to literature map"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ca6fa12b-f060-44ff-a3f8-2be93538cabe",
  "uuid": "23885450-240e-44c6-93e4-530e3a918510",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BzZhLYpCpGh7nHBoH9QGAK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 847,
      "cache_read_input_tokens": 49594,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 847
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

_source line 66 · 2026-05-21T03:50:01.167Z_

<details><summary>↩ Tool result · `toolu_01YRZJxidNtqPNCWxDRzBUYi`</summary>

```text
ToolResult(success=True, data={'key': 'llm_evaluation', 'action': 'added'}, error=None, metadata={})
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ca6fa12b-f060-44ff-a3f8-2be93538cabe",
  "uuid": "514a5753-00ab-4ac7-b739-b9992c816cda",
  "tool_use_result": {
    "stdout": "ToolResult(success=True, data={'key': 'llm_evaluation', 'action': 'added'}, error=None, metadata={})",
    "stderr": "\nShell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Assistant

_source line 67_

Category added. Now adding all 5 papers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ca6fa12b-f060-44ff-a3f8-2be93538cabe",
  "uuid": "eaee072d-5093-455f-b8c5-9f74674dfbdc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LWksF4j1F4BituBZScKPBM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 417,
      "cache_read_input_tokens": 50441,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 417
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

_source line 68_

<details open><summary>🔧 Tool call — Bash · `toolu_01GkNimNpmQr7tEhgnJCL63N`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0520_2 && python3 -c \"\nimport sys; sys.path.insert(0, '/home/ubuntu/agent-ml-research')\nfrom core.tools.literature import add_to_literature_map\nresult = add_to_literature_map(\n    project='irt_equated_bench_regen',\n    papers=[\n        {\n            'bibtex_key': 'burnell2023rethink',\n            'title': 'Rethink reporting of evaluation results in AI',\n            'authors': ['Burnell, R.', 'Schellaert, W.', 'Burden, J.', 'Ullman, T.D.', 'Martinez-Plumed, F.', 'Tenenbaum, J.B.', 'Rutar, D.', 'Cheke, L.G.', 'Sohl-Dickstein, J.', 'Mitchell, M.', 'Kiela, D.', 'Shanahan, M.', 'Voorhees, E.M.', 'Cohn, A.G.', 'Leibo, J.Z.', 'Hernandez-Orallo, J.'],\n            'year': 2023,\n            'venue': 'Science',\n            'category': 'llm_evaluation',\n            'role': 'background',\n            'relevance': 'Argues that aggregate metrics and lack of item-level transparency in AI evaluation limit understanding of model capabilities; motivates psychometric item-level analysis',\n            'doi': '10.1126/science.adf6369',\n            'url': 'https://www.science.org/doi/10.1126/science.adf6369',\n            'verified': True,\n        },\n        {\n            'bibtex_key': 'chang2024survey',\n            'title': 'A Survey on Evaluation of Large Language Models',\n            'authors': ['Chang, Y.', 'Wang, X.', 'Wang, J.', 'Wu, Y.', 'Zhu, K.', 'Chen, H.', 'Yang, L.', 'Yi, X.', 'Wang, C.', 'Wang, Y.', 'Ye, W.', 'Zhang, Y.', 'Chang, Y.', 'Yu, P.S.', 'Yang, Q.', 'Xie, X.'],\n            'year': 2024,\n            'venue': 'ACM Transactions on Intelligent Systems and Technology',\n            'category': 'llm_evaluation',\n            'role': 'background',\n            'relevance': 'Comprehensive survey covering what/where/how to evaluate LLMs across tasks and societal dimensions; provides landscape context for our psychometric evaluation approach',\n            'doi': '10.1145/3641289',\n            'url': 'https://dl.acm.org/doi/full/10.1145/3641289',\n            'verified': True,\n        },\n        {\n            'bibtex_key': 'maiapolo2024tinybenchmarks',\n            'title': 'tinyBenchmarks: evaluating LLMs with fewer examples',\n            'authors': ['Maia Polo, F.', 'Weber, L.', 'Choshen, L.', 'Sun, Y.', 'Xu, G.', 'Yurochkin, M.'],\n            'year': 2024,\n            'venue': 'ICML 2024',\n            'category': 'llm_evaluation',\n            'role': 'direct-competitor',\n            'relevance': 'Uses IRT to select representative benchmark subsets for efficient LLM evaluation with 100 items approximating full MMLU; directly related to our IRT-based equating methodology',\n            'doi': '',\n            'url': 'https://proceedings.mlr.press/v235/maia-polo24a.html',\n            'verified': True,\n        },\n        {\n            'bibtex_key': 'wang2024mmlupro',\n            'title': 'MMLU-Pro: A More Robust and Challenging Multi-Task Language Understanding Benchmark',\n            'authors': ['Wang, Y.', 'Ma, X.', 'Zhang, G.', 'Ni, Y.', 'Chandra, A.', 'Guo, S.', 'Ren, W.', 'Arulraj, A.', 'He, X.', 'Jiang, Z.', 'Li, T.', 'Ku, M.', 'Wang, K.', 'Zhuang, A.', 'Fan, R.', 'Xue, X.', 'Chen, W.'],\n            'year': 2024,\n            'venue': 'NeurIPS 2024',\n            'category': 'llm_evaluation',\n            'role': 'evaluation',\n            'relevance': 'Extends MMLU with harder reasoning items and 10-option format causing 16-33% accuracy drop; demonstrates benchmark evolution that motivates psychometric equating across versions',\n            'doi': '',\n            'url': 'https://arxiv.org/abs/2406.01574',\n            'verified': True,\n        },\n        {\n            'bibtex_key': 'ott2022benchmark',\n            'title': 'Mapping global dynamics of benchmark creation and saturation in artificial intelligence',\n            'authors': ['Ott, S.', 'Barbosa-Silva, A.', 'Blagec, K.', 'Brauner, J.', 'Samwald, M.'],\n            'year': 2022,\n            'venue': 'Nature Communications',\n            'category': 'llm_evaluation',\n            'role': 'background',\n            'relevance': 'Large-scale analysis of 3765 AI benchmarks showing rapid saturation dynamics; supports our argument that static benchmarks need psychometric equating and regeneration',\n            'doi': '10.1038/s41467-022-34591-0',\n            'url': 'https://www.nature.com/articles/s41467-022-34591-0',\n            'verified': True,\n        },\n    ],\n    added_by='paper_agent'\n)\nprint(result)\n\"",
  "description": "Add 5 llm_evaluation papers to literature map"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ca6fa12b-f060-44ff-a3f8-2be93538cabe",
  "uuid": "5b15a616-0955-427f-9809-9e1a09754d20",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LWksF4j1F4BituBZScKPBM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 417,
      "cache_read_input_tokens": 50441,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 417
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

_source line 69 · 2026-05-21T03:50:29.919Z_

<details><summary>↩ Tool result · `toolu_01GkNimNpmQr7tEhgnJCL63N`</summary>

```text
ToolResult(success=True, data={'added': ['burnell2023rethink', 'chang2024survey', 'maiapolo2024tinybenchmarks', 'wang2024mmlupro', 'ott2022benchmark'], 'merged': [], 'rejected': [], 'total_papers': 45}, error=None, metadata={})
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ca6fa12b-f060-44ff-a3f8-2be93538cabe",
  "uuid": "8de0b01d-0530-4b12-89e2-b4991e8fa9d2",
  "tool_use_result": {
    "stdout": "ToolResult(success=True, data={'added': ['burnell2023rethink', 'chang2024survey', 'maiapolo2024tinybenchmarks', 'wang2024mmlupro', 'ott2022benchmark'], 'merged': [], 'rejected': [], 'total_papers': 45}, error=None, metadata={})",
    "stderr": "\nShell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Assistant

_source line 70_

All 5 papers added successfully (total now 45). Here's what was added to the `llm_evaluation` cluster:

| Key | Paper | Venue | Role |
|-----|-------|-------|------|
| `burnell2023rethink` | Rethink reporting of evaluation results in AI | Science 2023 | background |
| `chang2024survey` | A Survey on Evaluation of Large Language Models | ACM TIST 2024 | background |
| `maiapolo2024tinybenchmarks` | tinyBenchmarks: evaluating LLMs with fewer examples | ICML 2024 | direct-competitor |
| `wang2024mmlupro` | MMLU-Pro: A More Robust and Challenging Multi-Task Language Understanding Benchmark | NeurIPS 2024 | evaluation |
| `ott2022benchmark` | Mapping global dynamics of benchmark creation and saturation in AI | Nature Communications 2022 | background |

All 5 verified via web search against publisher pages (Science, ACM DL, PMLR, NeurIPS proceedings, Nature). DOIs confirmed for 3; the ICML and NeurIPS entries use proceedings/arXiv URLs.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ca6fa12b-f060-44ff-a3f8-2be93538cabe",
  "uuid": "073f5142-9aea-4cf7-86b4-f0b2ca73c4f0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JfFa7F8SbdcCMTwquAL9TU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1787,
      "cache_read_input_tokens": 50858,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1787
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

_source line 71_

All 5 papers added successfully (total now 45). Here's what was added to the `llm_evaluation` cluster:

| Key | Paper | Venue | Role |
|-----|-------|-------|------|
| `burnell2023rethink` | Rethink reporting of evaluation results in AI | Science 2023 | background |
| `chang2024survey` | A Survey on Evaluation of Large Language Models | ACM TIST 2024 | background |
| `maiapolo2024tinybenchmarks` | tinyBenchmarks: evaluating LLMs with fewer examples | ICML 2024 | direct-competitor |
| `wang2024mmlupro` | MMLU-Pro: A More Robust and Challenging Multi-Task Language Understanding Benchmark | NeurIPS 2024 | evaluation |
| `ott2022benchmark` | Mapping global dynamics of benchmark creation and saturation in AI | Nature Communications 2022 | background |

All 5 verified via web search against publisher pages (Science, ACM DL, PMLR, NeurIPS proceedings, Nature). DOIs confirmed for 3; the ICML and NeurIPS entries use proceedings/arXiv URLs.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 188313,
  "duration_api_ms": 219215,
  "num_turns": 17,
  "stop_reason": "end_turn",
  "session_id": "ca6fa12b-f060-44ff-a3f8-2be93538cabe",
  "total_cost_usd": 0.85348885,
  "usage": {
    "input_tokens": 526,
    "cache_creation_input_tokens": 40804,
    "cache_read_input_tokens": 366676,
    "output_tokens": 6114,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 40804,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 289,
        "cache_read_input_tokens": 50858,
        "cache_creation_input_tokens": 1787,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1787
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 97851,
      "outputTokens": 4665,
      "cacheReadInputTokens": 56836,
      "cacheCreationInputTokens": 42229,
      "webSearchRequests": 8,
      "costUSD": 0.25964585,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 526,
      "outputTokens": 6114,
      "cacheReadInputTokens": 366676,
      "cacheCreationInputTokens": 40804,
      "webSearchRequests": 0,
      "costUSD": 0.5938430000000001,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "5d61f65f-6d97-4422-a9db-551024372d56"
}
```

</details>

---
