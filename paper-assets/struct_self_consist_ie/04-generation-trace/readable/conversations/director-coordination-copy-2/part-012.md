# Director coordination — Part 12 of 16

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Conversation logs

[← Part 11](part-011.md) · [Transcript overview](../director-coordination-copy-2.md) · [Part 13 →](part-013.md) · [Structured JSON](../../../sessions/6a/6a5a1a2f9a2bf6bdf404.json)

## Round 256

### Tool call

_source line 3455 · 2026-05-22T02:05:51.766856+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "你是 Reviewer 2，负责审查新颖性、完整性、Related Work 和写作质量。\n\n## Venue 信息\n- **目标会议**: EMNLP 2026（通过 ACL Rolling Review 统一审稿）\n- **ARR Submission Deadline**: 2026-05-25\n- **投稿类别**: Long Paper\n- **页数限制**: 正文 8 页，参考文献不限，Limitations/Ethics 不计页数\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind\n- **附录**: 允许，但审稿人不要求必须阅读\n- **Overall Assessment 评分标准**: 5=Consider for Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1=Do not resubmit\n\n## 论文信息\n- **标题**: \"Characterizing the Capability Ceiling of Self-Consistency: How Entity-Level Verification Fails in NER\"\n- **论文路径**: `docs/paper/main.tex`（各章节在 `docs/paper/sections/` 下）\n- **PDF 路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf`（47页：8页正文 + 附录/引用）\n\n## 论文概要\n研究 test-time compute scaling（self-consistency）在 NER 任务上的效果。核心发现是\"correlation-selection gap\"：质量估计信号与 oracle F1 存在中等相关（ρ 达 0.47），但无法转化为样本选择增益。只有 log-probability (LP) 在 Few-NERD 上实现了 +1.39pp 的选择增益。提出四阶段诊断框架和实体级构建作为处方式逃逸路线。实验覆盖 4 个 NER 数据集、2 个模型家族、4B/8B/14B 消融、72B 和 GPT-5.5 zero-shot。\n\n## 你的审查重点\n\n### 1. 新颖性评估\n- \"correlation-selection gap\" 作为核心概念的新颖性：这是否是一个 well-known 的现象用新术语包装？MBR decoding 文献中类似的 gap 是否已被讨论？\n- 与 Yao et al. (2026) 的区分是否充分？后者也研究 consistency 在 structured IE 上的效果\n- 与 Yun et al. (2025) \"diversity collapse\" 的区分：论文 §8 提到 Table 66 有完整对比，但正文中的区分是否清晰？\n- 四阶段诊断框架的贡献深度：是否仅是对已知失败模式的系统化？\n- 九种方法类别的覆盖：是否遗漏了重要的 self-consistency 改进方法？\n\n### 2. 完整性检查\n- 论文声称 \"nine method categories\" 但正文只详细讨论了部分（ESJ, MRSC, LSC, cross-model, LGB verifier），其余被推到 Appendix——这是否影响主要论点的说服力？\n- RE extension（SciERC，n=207，55.5% zero-F1）和 SQL extension（Spider，n=196，87.2% degeneracy）极为初步——是否应该从 contribution 列表中移除或降级？\n- Pretrained vs finetuned 的对比：仅用 CoNLL 一个数据集，是否足够支撑 §9 的叙事？\n- GPT-5.5 的实验仅 200 instances，是否足以支撑 \"gap persists across frontier models\" 的声明？\n- Cross-model ensemble 仅在 Few-NERD 上测试（一个数据集、一对模型），声明强度是否与证据匹配？\n\n### 3. Related Work 审查\n- §8 的 Related Work 覆盖是否全面？是否遗漏重要工作？\n- 特别检查以下领域的覆盖：\n  - NER 的 confidence estimation 和 uncertainty quantification\n  - Structured prediction 的 test-time scaling\n  - Entity-level agreement 和 voting 方法\n  - MBR decoding 在 structured prediction 中的应用\n- 引用是否真实、准确？是否存在可疑引用？（特别注意 2025-2026 年的引用）\n- 与 concurrent work 的关系是否妥善处理？\n\n### 4. 写作质量\n- 论文结构是否清晰？8 页正文覆盖 9 个 sections 是否过于拥挤？\n- 术语使用是否一致？（如 \"capability ceiling\" vs \"correlation-selection gap\" vs \"selection gap\"）\n- Figure 1 是否有效传达核心信息？\n- 表格是否过多/过少？关键数据是否在正文中充分讨论？\n- 是否存在过度声称（overclaiming）或不当弱化（underclaiming）？\n- Limitations section 的覆盖是否充分？（注意 EMNLP 2026 要求 Limitations 只需一小段，3 个点左右）\n- 实际的 Limitations 部分长度是否超标？（当前约 26 行/1 页多）\n\n### 5. 格式合规\n- 正文是否严格 8 页以内？\n- 匿名性是否完全？（检查代码链接、致谢、自引等）\n- Responsible NLP Research Checklist 是否应在 submission form 中而非论文中？（根据 EMNLP 2026 规则，checklist 在 OpenReview form 里填写，不在 PDF 中）\n- 引用格式是否符合 ACL style？\n\n请严格按照 EMNLP 2026 审稿标准评审。输出结构：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → Missing References → Overall Assessment（含评分和置信度）。",
  "reviewer_id": "2",
  "project": "struct_self_consist_ie",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "你是 Reviewer 2，负责审查新颖性、完整性、Related Work 和写作质量。\n\n## Venue 信息\n- **目标会议**: EMNLP 2026（通过 ACL Rolling Review 统一审稿）\n- **ARR Submission Deadline**: 2026-05-25\n- **投稿类别**: Long Paper\n- **页数限制**: 正文 8 页，参考文献不限，Limitations/Ethics 不计页数\n- **模板**: ACL style (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind\n- **附录**: 允许，但审稿人不要求必须阅读\n- **Overall Assessment 评分标准**: 5=Consider for Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1=Do not resubmit\n\n## 论文信息\n- **标题**: \"Characterizing the Capability Ceiling of Self-Consistency: How Entity-Level Verification Fails in NER\"\n- **论文路径**: `docs/paper/main.tex`（各章节在 `docs/paper/sections/` 下）\n- **PDF 路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf`（47页：8页正文 + 附录/引用）\n\n## 论文概要\n研究 test-time compute scaling（self-consistency）在 NER 任务上的效果。核心发现是\"correlation-selection gap\"：质量估计信号与 oracle F1 存在中等相关（ρ 达 0.47），但无法转化为样本选择增益。只有 log-probability (LP) 在 Few-NERD 上实现了 +1.39pp 的选择增益。提出四阶段诊断框架和实体级构建作为处方式逃逸路线。实验覆盖 4 个 NER 数据集、2 个模型家族、4B/8B/14B 消融、72B 和 GPT-5.5 zero-shot。\n\n## 你的审查重点\n\n### 1. 新颖性评估\n- \"correlation-selection gap\" 作为核心概念的新颖性：这是否是一个 well-known 的现象用新术语包装？MBR decoding 文献中类似的 gap 是否已被讨论？\n- 与 Yao et al. (2026) 的区分是否充分？后者也研究 consistency 在 structured IE 上的效果\n- 与 Yun et al. (2025) \"diversity collapse\" 的区分：论文 §8 提到 Table 66 有完整对比，但正文中的区分是否清晰？\n- 四阶段诊断框架的贡献深度：是否仅是对已知失败模式的系统化？\n- 九种方法类别的覆盖：是否遗漏了重要的 self-consistency 改进方法？\n\n### 2. 完整性检查\n- 论文声称 \"nine method categories\" 但正文只详细讨论了部分（ESJ, MRSC, LSC, cross-model, LGB verifier），其余被推到 Appendix——这是否影响主要论点的说服力？\n- RE extension（SciERC，n=207，55.5% zero-F1）和 SQL extension（Spider，n=196，87.2% degeneracy）极为初步——是否应该从 contribution 列表中移除或降级？\n- Pretrained vs finetuned 的对比：仅用 CoNLL 一个数据集，是否足够支撑 §9 的叙事？\n- GPT-5.5 的实验仅 200 instances，是否足以支撑 \"gap persists across frontier models\" 的声明？\n- Cross-model ensemble 仅在 Few-NERD 上测试（一个数据集、一对模型），声明强度是否与证据匹配？\n\n### 3. Related Work 审查\n- §8 的 Related Work 覆盖是否全面？是否遗漏重要工作？\n- 特别检查以下领域的覆盖：\n  - NER 的 confidence estimation 和 uncertainty quantification\n  - Structured prediction 的 test-time scaling\n  - Entity-level agreement 和 voting 方法\n  - MBR decoding 在 structured prediction 中的应用\n- 引用是否真实、准确？是否存在可疑引用？（特别注意 2025-2026 年的引用）\n- 与 concurrent work 的关系是否妥善处理？\n\n### 4. 写作质量\n- 论文结构是否清晰？8 页正文覆盖 9 个 sections 是否过于拥挤？\n- 术语使用是否一致？（如 \"capability ceiling\" vs \"correlation-selection gap\" vs \"selection gap\"）\n- Figure 1 是否有效传达核心信息？\n- 表格是否过多/过少？关键数据是否在正文中充分讨论？\n- 是否存在过度声称（overclaiming）或不当弱化（underclaiming）？\n- Limitations section 的覆盖是否充分？（注意 EMNLP 2026 要求 Limitations 只需一小段，3 个点左右）\n- 实际的 Limitations 部分长度是否超标？（当前约 26 行/1 页多）\n\n### 5. 格式合规\n- 正文是否严格 8 页以内？\n- 匿名性是否完全？（检查代码链接、致谢、自引等）\n- Responsible NLP Research Checklist 是否应在 submission form 中而非论文中？（根据 EMNLP 2026 规则，checklist 在 OpenReview form 里填写，不在 PDF 中）\n- 引用格式是否符合 ACL style？\n\n请严格按照 EMNLP 2026 审稿标准评审。输出结构：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Questions → Missing References → Overall Assessment（含评分和置信度）。",
    "reviewer_id": "2",
    "project": "struct_self_consist_ie",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 3456 · 2026-05-22T02:05:53.528112+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1761
}
```

</details>

---


### Assistant

_source line 3457 · 2026-05-22T02:06:00.306251+00:00_

**Round 1 已启动：**
- 视觉审查 Agent：已派发（fire-and-forget）
- Reviewer 1（方法严谨性 + 实验设计 + 统计声明）：已分配
- Reviewer 2（新颖性 + 完整性 + Related Work + 写作质量）：已分配

等待两名 Reviewer 的独立审稿结果返回。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 257

## Round 257

1 recorded events


### User

_source line 3458 · 2026-05-22T02:08:09.406668+00:00_

[Reviewer 1 审稿结果]:
读取附录最后部分（N-scaling 详细分析、RE/SQL 扩展等）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_1"
}
```

</details>

---


## Round 258

## Round 258

2 recorded events


### User

_source line 3459 · 2026-05-22T02:08:25.515235+00:00_

[Reviewer 2 审稿结果]:
正文 8 页已通读。现在检查附录关键页面和引用验证详情。

---

[Reviewer 1 审稿结果]:
读取附录最后部分（N-scaling 详细分析、RE/SQL 扩展等）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 3460 · 2026-05-22T02:08:47.063194+00:00_

收到两位 Reviewer 的进度更新。两人均已完成正文通读，正在处理附录和引用验证，尚未提交完整审稿意见。

等待完整审稿结果返回后启动交叉分享环节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 259

## Round 259

82 recorded events


### User

_source line 3461 · 2026-05-22T07:57:58.425080+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: struct_self_consist_ie
- 论文路径: projects/struct_self_consist_ie/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Main Conference (ARR May 2026)
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 3462 · 2026-05-22T07:58:05.065231+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 3463 · 2026-05-22T07:58:05.066188+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 3286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 3464 · 2026-05-22T07:58:10.909633+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,get_visual_check_status",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,get_visual_check_status",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 3465 · 2026-05-22T07:58:10.910060+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 3466 · 2026-05-22T07:58:14.474814+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__get_visual_check_status",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__get_visual_check_status",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 3467 · 2026-05-22T07:58:14.525500+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 3468 · 2026-05-22T07:58:17.290620+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 3469 · 2026-05-22T07:58:18.445960+00:00_

{"result":"# 项目 struct_self_consist_ie 概况\n\n## 实验状态 (318 个)\n\n- **exp_002_ner_conll2003**: DONE (success) — \n- **exp_004_re_diagnostic**: DONE (success) — \n- **exp_005**: DONE (success) — \n- **exp_014_entity_majority_voting**: DONE (success) — \n- **exp_013_exact_match_voting**: DONE (negative) — \n- **exp_012_logprob_baseline**: DONE (success) — \n- **mvp_pilot_005**: DONE (negative) — \n- **e1_component_wise_re_sj**: DONE (negative) — \n- **mvp_pilot_004**: DONE (negative) — \n- **ft_002_v2**: DONE (success) — \n- **mvp_pilot_002**: DONE (failed) — \n- **ft_002**: DONE (killed) — \n- **ft_001**: DONE (success) — \n- **mvp_pilot_003**: DONE (negative) — \n- **mvp_pilot_001**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-22\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| exp_fewnerd_pretrained_n32_s42 | Pretrained N-scaling: FewNERD N=32 with Qwen2.5-7B-Instruct (unfinetuned). FewNERD pretrained showed +3.90pp MV gain at N=8. Tests whether pretrained MV advantage scales with N and whether the pretrained-vs-finetuned direction flip persists at 4× budget. Complements CoNLL/SciERC pretrained N=32 for cross-dataset generalization evidence. | — | — | — |\n| exp_fewnerd_n32_s42 | N-scaling convergence test: at N=32 (4× current N=8), MV strict Δ remains negative on FewNERD finetuned model, demonstrating that the selection gap does not close at practical sample budgets. If MV Δ converges toward 0 slowly, this quantifies the impractical N required. Motivated by R34 C1 and Reviewer #107 P2. | — | — | — |\n\n## 待处理\n- exp_conll_pretrained_n64_s42: Pretrained N-scaling: CoNLL N=64 with Qwen2.5-7B-Instruct (unfinetuned). Fourth data point for pretrained CoNLL N-scaling curve (N=8 +3.01, N=32 +3.21). Tests whether pretrained MV gain continues scaling and whether degeneracy continues declining at N=64.（排队等待 GPU）\n- exp_scierc_pretrained_n64_s42: Pretrained N-scaling: SciERC N=64 with Qwen2.
…[truncated 1743 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1155
}
```

</details>

---


### Tool call

_source line 3470 · 2026-05-22T07:58:18.446417+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 3471 · 2026-05-22T07:58:18.496848+00:00_

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
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{amsthm}
16	\newtheorem{proposition}{Proposition}
17	\newtheorem{theorem}{Theorem}
18	\newtheorem{corollary}{Corollary}
19	\newtheorem{definition}{Definition}
20	\usepackage{multirow}
21	\usepackage{xcolor}
22	\usepackage{subcaption}
23	\usepackage{alphalph}
24	\usepackage{enumitem}
25	
26	\graphicspath{{figures/}}
27	
28	\title{Characterizing the Capability Ceiling of Self-Consistency:\\ A Diagnostic Framework for Test-Time Aggregation in NER}
29	
30	\author{Anonymous}
31	
32	\begin{document}
33	\maketitle
34	
35	\input{sections/abstract}
36	\input{sections/introduction}
37	\input{sections/diagnostic}
38	\input{sections/mechanistic}
39	\input{sections/single_signal}
40	\input{sections/adaptive}
41	\input{sections/theory}
42	\input{sections/experiments_main}
43	\input{sections/background}
44	\input{sections/discussion}
45	
46	\section*{Limitations}
47	\input{sections/limitations}
48	
49	\section*{Ethics Statement}
50	All experiments use publicly available benchmarks (SciERC, CoNLL-2003, Few-NERD, WNUT-17), open-weight models (Qwen3-8B, Qwen3-14B, Qwen3-4B, LLaMA-3.1-8B), and the GPT-5.5 API.
51	CoNLL-2003 is derived from the Reuters RCV1 corpus, which is available for research purposes under a NIST agreement; we use the standard research distribution.
52	No new human data was collected or annotated for this study.
53	Our findings on signal limitations could inform more reliable deployment of IE systems by guiding practitioners toward appropriate confidence signals for their use case.
54	Code and data will be released upon acceptance at [anonymized URL].
55	
56	\section*{Responsible NLP Research Checklist}
57	\input{sections/checklist}
58	
5
…[truncated 157 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 3472 · 2026-05-22T07:58:25.159732+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 3473 · 2026-05-22T07:58:25.210311+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 3474 · 2026-05-22T07:58:28.222305+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers ARR submission guidelines site:aclweb.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers ARR submission guidelines site:aclweb.org"
  }
}
```

</details>

---


### Tool call

_source line 3475 · 2026-05-22T07:58:28.691879+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 3476 · 2026-05-22T07:58:29.164016+00:00_

1	\begin{abstract}
2	Test-time compute scaling yields large gains on discrete-answer reasoning and code generation, yet for named entity recognition (NER), where outputs are entity sets with partial overlap, aggregation gains are marginal.
3	We trace this failure through three stages of investigation.
4	Quality estimation signals reliably predict output quality (Spearman $\rho$ up to 0.45, AUROC 0.82 across nine method categories), confirming the information to identify better outputs exists.
5	Yet instance-level selection yields ${<}1$\,pp on most datasets; a four-stage diagnostic cascade localizes this \textbf{correlation-selection gap}: the optimal strategy is dataset-dependent (LP-best: $+8$\,pp on Few-NERD; MV dominates on CoNLL) and near-zero selection alignment ($\alpha{\to}0$), not degeneracy alone, is the binding constraint.
6	Entity-level LP-weighted construction ($+0.3$--$1.4$\,pp) and regime-specific LP selection ($+1.39$\,pp on Few-NERD) bypass the sample-level bottleneck by operating at entity granularity.
7	A degeneracy threshold ($\theta_{\text{crit}}{=}0.70$) predicts when aggregation gains vanish; the cascade generalizes to RE ($-3.62$\,pp MV at $0.8$\% degeneracy) and SQL parsing ($87.2$\% degeneracy).
8	\end{abstract}
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 472
}
```

</details>

---


### Tool call

_source line 3477 · 2026-05-22T07:58:29.164547+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 3478 · 2026-05-22T07:58:30.119828+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Test-time compute scaling complements model scaling \cite{snell2025scaling}: repeated sampling with majority voting \cite{wang2023selfconsistency}, best-of-$N$ with learned verifiers \cite{cobbe2021verifiers, brown2024monkeys}, and extended chain-of-thought \cite{muennighoff2025s1} produce large gains on reasoning and code generation.
4	These successes share a structural prerequisite: the output space admits either exact equivalence classes (multiple-choice, numeric answers) or execution-based verification (code).
5	Named entity recognition (NER) breaks both assumptions.
6	The output is a set of typed entities; two samples from the same input routinely extract overlapping but non-identical sets, and no external oracle can adjudicate correctness at test time.
7	Without equivalence classes, majority voting reduces to heuristic frequency counting; without a verifier, best-of-$N$ requires a reliable proxy signal.
8	This structural mismatch raises a concrete question: can self-consistency signals that estimate quality well for reasoning tasks also \textit{select} better outputs or \textit{construct} better entity sets for NER?
9	We investigate this question for NER and extend exploratorily to SQL parsing, treating NER as a representative instance of set-valued generation.
10	
11	The question has practical stakes beyond information extraction.
12	Hallucination detection methods such as SelfCheckGPT \cite{manakul2023selfcheckgpt} and FActScore \cite{min2023factscore} rely on cross-sample consistency to verify claims; the underlying assumption is that models can distinguish correct extractions through self-judgment.
13	We evaluate five quality estimation (QE) signals and find they \textit{do} reliably predict output quality at the population level: Spearman $\rho$ up to $0.45$ and AUROC up to $0.82$ with oracle F1 (Table~\ref{tab:quality_estimation}).
14	A supervised hidden-state probe confirms that entity quality is par
…[truncated 4774 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 955
}
```

</details>

---


### Tool call

_source line 3479 · 2026-05-22T07:58:30.120338+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments_main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments_main.tex"
  }
}
```

</details>

---


### Tool result

_source line 3480 · 2026-05-22T07:58:30.321400+00:00_

1	\section{Experiments}\label{sec:experiments}
2	
3	\subsection{Experimental Setup}\label{sec:setup}
4	
5	\paragraph{Datasets.}
6	We evaluate on four English NER benchmarks spanning a difficulty gradient.
7	\textbf{SciERC} \cite{luan2018scierc} (551 test instances, 6 entity types) is the primary medium-difficulty test bed (${\approx}$65\% F1).
8	\textbf{Few-NERD} \cite{ding2021fewnerd} (INTRA coarse; 37{,}648 instances, 8 entity types, ${\approx}$75\% F1) provides a low-degeneracy contrast where LP selection succeeds (\S\ref{sec:selection_gap}).
9	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} (3{,}453 test sentences, 4 entity types, ${\approx}$91\% F1) serves as a ceiling-effect control.
10	\textbf{WNUT-17} \cite{derczynski2017wnut} (1{,}287 social media instances, 51\% zero F1) probes the signal-collapse boundary.
11	
12	\paragraph{Models and sampling.}
13	\textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are LoRA fine-tuned using LLaMA Factory \cite{zheng2024llamafactory} (Appendix~\ref{app:training}; Few-NERD uses 3 epochs vs.\ 5 for others; Appendix~\ref{app:epoch_confound}).
14	$N{=}8$ samples at $T{=}1.0$ (primary) with vLLM constrained decoding \cite{willard2023guided}; $N {\in} \{16, 32, 64\}$ for scaling (Figure~\ref{fig:n_scaling}; Appendix~\ref{app:n_scaling}).
15	
16	\begin{figure}[t]
17	\centering
18	\includegraphics[width=\columnwidth]{figures/fig_n_scaling_mv.pdf}
19	\caption{MV $\Delta$F1 vs.\ $\log_2 N$ across three datasets (Qwen3-8B FT, seed${=}42$). Dotted gray: $\Delta{=}0$. Gains are dataset-dependent: persistently negative on Few-NERD, near zero on SciERC at higher $N$, marginally positive on CoNLL ($+0.6$\,pp at $N{=}64$).}
20	\label{fig:n_scaling}
21	\end{figure}
22	
23	%% ============================================================
24	\subsection{Quality Estimation Results}\label{sec:qe_results}
25	
26	\begin{table*}[t]
27	\centering
28	\small
29	\caption{NER quality estimation ($\rho$ and AUROC; $N{=}8$, primary seed${=}42$; 3-seed $
…[truncated 7447 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 3481 · 2026-05-22T07:58:30.321764+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_local_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_local_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 3482 · 2026-05-22T07:58:30.372231+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 3483 · 2026-05-22T07:58:33.584762+00:00_

Web search results for query: "EMNLP 2026 call for papers ARR submission guidelines site:aclweb.org"

Links: [{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"Jan. 2025 ACL Standing Committee on Peer Review (COPR) Report 1","url":"https://www.aclweb.org/adminwiki/images/9/9e/COPR-5-cycle-report-to-publish.pdf"},{"title":"EMNLP 2025: Call for System Demonstrations | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-call-system-demonstrations"}]

I found some relevant information about EMNLP 2026 and ARR submission guidelines. Here are
…[truncated 1159 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 5362
}
```

</details>

---


### Tool call

_source line 3484 · 2026-05-22T07:58:39.761421+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 submission guidelines page limit format requirements"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 submission guidelines page limit format requirements"
  }
}
```

</details>

---


### Tool call

_source line 3485 · 2026-05-22T07:58:40.721355+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ARR 2026 May cycle submission deadline author guidelines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ARR 2026 May cycle submission deadline author guidelines"
  }
}
```

</details>

---


### Tool call

_source line 3486 · 2026-05-22T07:58:42.629643+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/diagnostic.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/diagnostic.tex"
  }
}
```

</details>

---


### Tool result

_source line 3487 · 2026-05-22T07:58:43.131844+00:00_

1	\section{Diagnostic Framework}\label{sec:method}
2	
3	Our analysis is observational: we characterize statistical associations between agreement signals and output quality without claiming causal mechanisms.
4	
5	\subsection{Problem Formulation}\label{sec:formulation}
6	
7	Given model $\mathcal{M}$ and input $x$, we sample $N$ outputs $\{y_1, \ldots, y_N\}$ at temperature $T > 0$ via constrained decoding \cite{willard2023guided}, where each $y_i$ is an entity set.
8	A \textbf{per-sample signal} $c_{\text{ps}}: (x, y_i) \to \mathbb{R}$ scores each output independently; an \textbf{instance-level signal} $c_{\text{il}}: (x, \{y_i\}_{i=1}^N) \to \mathbb{R}$ produces a single score per input (notation in Appendix~\ref{app:notation}).
9	This distinction is consequential: 4 of 5 signals are instance-level aggregates assigning identical scores to all $N$ candidates.
10	Only LP carries per-sample discriminative power: ensemble optimization assigns LP mean weight $0.78$, with structural signals receiving zero weight (Appendix~\ref{app:supervised_combination}).
11	When LP fails---as in few-shot regimes where LP $\rho{\to}0$ (\S\ref{sec:scaling})---no alternative per-sample signal exists.
12	
13	We define the \textbf{capability ceiling} as the practical performance upper bound achievable through self-consistency at realistic sample budgets ($N{\leq}16$), beyond which diminishing returns render further scaling impractical.
14	
15	\subsection{Confidence Signals}\label{sec:signals}
16	
17	Entity matching uses exact span and type match.
18	We distinguish two signal families: four \textit{agreement signals} computed across samples---\textit{structural} (Soft Jaccard [SJ], entity voting confidence [VC]) and \textit{surface} (exact match [EM], Fleiss' $\kappa$ [FK])---and log-probability [LP] as the sole \textit{model-internal} signal, derived from generation probabilities and providing per-sample discrimination.
19	
20	\paragraph{Log-probability (per-sample).}
21	$c_{\text{lp}}(y_i)
…[truncated 2151 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 3488 · 2026-05-22T07:58:43.182555+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/mechanistic.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/mechanistic.tex"
  }
}
```

</details>

---


### Tool result

_source line 3489 · 2026-05-22T07:58:43.584643+00:00_

1	\section{How Self-Verification Fails}\label{sec:mechanistic}
2	
3	The diagnostic cascade (\S\ref{sec:method}) identifies \textit{where} self-consistency fails; this section probes \textit{why} by testing whether models can self-verify at the entity level.
4	We evaluate self-verification and diagnostic probes on Qwen2.5-7B (a separate model family from the primary Qwen3-8B) fine-tuned for NER on Few-NERD ($N{=}8$, seed 42; full results in Appendix~\ref{app:self_verification}).
5	
6	\paragraph{Entity Self-Judgment (ESJ).}
7	For each extracted entity, we prompt the generating model: ``Is [\textit{entity}] a [\textit{type}] entity in this sentence?''
8	Entity-level AUROC is $0.512$---indistinguishable from chance---with P(yes$|$correct)${=}0.500$ and P(yes$|$incorrect)${=}0.500$.
9	ESJ-weighted construction degrades F1 to $0.711$ (vs.\ greedy $0.794$).
10	
11	\paragraph{Multi-Round Self-Consistency (MRSC).}
12	Following iterative self-refinement \cite{madaan2023selfrefine}, we re-prompt on disputed entities (agreement ${<}0.6$) with focused verification; P(yes) separation between gold and non-gold entities is $0.0006$ ($0.5003$ vs.\ $0.4997$).
13	MRSC best F1 ($0.763$) falls below greedy.
14	
15	\paragraph{Latent Self-Consistency (LSC).}
16	Mean-pooled final-layer hidden states ($d{=}3584$) provide per-sample latent representations.
17	Centroid selection ($0.759$) underperforms greedy ($0.794$); latent entity confidence ($0.839$) outperforms majority vote ($0.792$) but does not close the oracle gap ($0.882$).
18	
19	\paragraph{Hidden-state probe.}
20	A logistic regression on mean-pooled final-layer hidden states at entity spans achieves AUROC $0.636$ (Few-NERD), $0.882$ (CoNLL), $0.630$ (SciERC), evaluated with GroupKFold CV (5-fold ${\times}$ 3 seeds, groups${=}$source instance to prevent entity-level leakage; Appendix~\ref{app:hidden_probe}).
21	All three exceed ESJ ($0.51$); only CoNLL approaches frequency agreement ($0.868$).
22	Cross-dataset transfer is weak: lea
…[truncated 1062 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 3490 · 2026-05-22T07:58:43.585005+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 3491 · 2026-05-22T07:58:43.635634+00:00_

1	\section{Discussion and Conclusion}\label{sec:discussion}\label{sec:selection_method}\label{sec:conclusion}
2	
3	Degeneracy (12.2--67.9\%) and LP-quality alignment ($\rho$ 0.043--0.667) constrain aggregation; temperature disentangles these (\S\ref{sec:scaling}; Table~\ref{tab:t_degeneracy}), and across four frontier models degeneracy and the selection gap are negatively correlated (5.5--74\%; Table~\ref{tab:frontier_sc_cross}).
4	On CoNLL, pretrained MV captures ${\sim}98$\% of oracle headroom versus ${<}2$\% finetuned (Appendix~\ref{app:cross_scale}); entity-level construction bypasses both failure mechanisms when degeneracy ${<}22$\%, with $\theta_{\text{crit}}{=}0.70$ and $\alpha{\to}0$ as the binding constraints \cite{kadavath2022language}.
5	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 3492 · 2026-05-22T07:58:46.795745+00:00_

Web search results for query: "EMNLP 2026 submission guidelines page limit format requirements"

Links: [{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"EMNLP: Empirical Methods in Natural Language Processing 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=883"},{"title":"Confs: 2026 Conference on Empirical Methods in Natural ...","url":"https://www.facebook.com/linguistlist/posts/confs-2026-conference-on-empirical-methods-in-natural-language-processing-emnlp-/1351983883622556/"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"},{"title":"EMNLP 2026 (@emnlpmeeting) / Posts / X","url":"https://x.com/emnlpmeeting?lang=en"}]

Based on the search results, I found submission guidelines for EMNLP 2026. Here are the key page limit and format requirements:

**Main Conference:**

The format is two-column with an 8-page limit for long papers and a 4-page limit for short papers.

**Industry Track:**

Authors are invited to submit original, full-length (maximum of 6 pages) industry track papers that are not previously published, accepted to be published, or under consideration for publication in any other forum.

**Format Requirements:**

Manuscripts should be submitted electronically, in PDF format and formatted using the templates ava
…[truncated 947 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 7034
}
```

</details>

---


### Tool result

_source line 3493 · 2026-05-22T07:58:50.280346+00:00_

Web search results for query: "ARR 2026 May cycle submission deadline author guidelines"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines","url":"http://aclrollingreview.org/authors"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Incentives 2026","url":"http://aclrollingreview.org/incentives2026"},{"title":"Authors Beware: Common Submission Problems","url":"http://aclrollingreview.org/authorchecklist"},{"title":"ACL ARR 2026 January | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026%2FJanuary"}]

Based on the search results, here is information about the ARR 2026 May cycle submission deadline and author guidelines:

## Submission Deadline and Author Registration

After submission, all authors must complete the author registration form by May 27, 2026 EoD AoE.

## Author Guidelines and Requirements

Key author guidelines for ARR submissions include:

**Anonymity and Preprints:**
Papers must not include authors' names and affiliations. Furthermore, self-references that reveal the authors' identities must be avoided. There is no anonymity period or limitation on posting or discussing non-anonymous preprints while the work is under peer review.

**Author Responsibility Policy:**
All authors are expected to sign up as reviewers, with assignments made based on their qualifications. Submitting authors should ensure that all co-authors are aware of this policy and that every team member submits their reviews and meta-reviews on time according to the guidelines.

**Paper Format and Conten
…[truncated 447 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 9558
}
```

</details>

---


### Tool call

_source line 3494 · 2026-05-22T07:58:57.612524+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/theory.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/theory.tex"
  }
}
```

</details>

---


### Tool result

_source line 3495 · 2026-05-22T07:58:57.964225+00:00_

1	\section{Threshold Regime Analysis}\label{sec:theory_scaling}
2	
3	\subsection{Entity Construction as MBR Decoding}\label{sec:mbr_theory}
4	
5	Entity-level construction selects $\hat{y}_{\textup{MBR}} = \{e \in E_\cup : \hat{p}(e) > \alpha/(\alpha{+}1)\}$ under balanced set-overlap utility; $\alpha{=}1$ recovers majority vote (Proposition~\ref{prop:construction_mbr}; Table~\ref{tab:entity_construction}; Appendix~\ref{app:mbr_proof}).
6	Signal-derived weights $w_i$ yield quality-weighted MBR: $\hat{p}_w(e) = \sum_{i} w_i \, \mathbf{1}[e {\in} y_i] / \sum_{i} w_i$; weighting improves when $w_i$ correlates with instance quality but degrades otherwise (LP on SciERC: $\rho{\approx}0.2$; \S\ref{sec:prescriptive}).
7	We select $\varepsilon{=}0.05$ at the elbow of the compression curve, where LP-best selection advantage transitions from $+1.5$\,pp (compressed) to $+4.6$\,pp (non-compressed; Appendix~\ref{app:fewnerd_epsilon}).
8	
9	\subsection{Scaling and Inverse Scaling}\label{sec:scaling}
10	
11	Oracle F1 follows $F_1(N) = a - b \cdot N^{-c}$ ($R^2 > 0.999$; Figure~\ref{fig:oracle_scaling}): Few-NERD ($c{\approx}0.61$) scales comparably to reasoning tasks \cite{brown2024monkeys}, SciERC converges more slowly ($c{\approx}0.35$), yet confidence-based aggregation recovers ${<}1$\,pp---a persistent gap.
12	The gap persists across scales and families: scaling from 8B to 14B FT increases oracle headroom ($+1.2$\,pp) with minimal greedy gain ($+0.9$\,pp), and GPT-5.5 (200 Few-NERD instances, zero-shot) exhibits the same pattern---50\% degeneracy, SJ $\rho{=}0.346$, MV $+1.4$\,pp yet 6.8\,pp oracle headroom unrealized.\footnote{10.1\% of GPT-5.5 samples produced unparseable output; these are excluded from all metrics. See Appendix~\ref{app:frontier_sc}.}
13	Degeneracy is model-family-dependent rather than scale-dependent (Qwen2.5: $31.7$--$46.2$\% vs.\ Qwen3: $13.0$\% vs.\ GPT-5.5: $50$\% on Few-NERD; Appendix~\ref{app:cross_scale}).
14	
15	\paragraph{Inverse scaling under adap
…[truncated 3257 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 3496 · 2026-05-22T07:58:57.964715+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/adaptive.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/adaptive.tex"
  }
}
```

</details>

---


### Tool result

_source line 3497 · 2026-05-22T07:58:58.918712+00:00_

1	\section{Adaptive Methods}\label{sec:adaptive}
2	
3	Since instance-level selection fails (\S\ref{sec:selection_gap}), we present approaches that extract value from multi-sample generation beyond single-signal sample ranking.
4	Table~\ref{tab:method_summary} summarizes all 9 method categories evaluated; only cross-model ensembles yield an unconditional positive result.
5	
6	\begin{table}[t]
7	\centering
8	\small
9	\caption{Summary of 9 method categories tested (including MV baseline, LP selection, and cross-model ensemble beyond the seven verification methods in \S\ref{sec:mechanistic}--\S\ref{sec:adaptive}). $\Delta$F1 vs.\ greedy; dataset in parentheses. Full coverage in Appendix~\ref{app:method_coverage}.}
10	\label{tab:method_summary}
11	\resizebox{\columnwidth}{!}{%
12	\begin{tabular}{@{}llrl@{}}
13	\toprule
14	Category & Method & $\Delta$F1 / metric & § \\
15	\midrule
16	Freq.\ voting & MV & baseline & \ref{sec:prescriptive} \\
17	LP selection & Best-of-$N$ (LP) & $+1.39$\,pp (FN)$^\dagger$ & \ref{sec:selection_gap} \\
18	Self-verif.\ (prompt) & ESJ & AUROC $0.51$ & \ref{sec:mechanistic} \\
19	Multi-round refine. & MRSC & $-3.1$\,pp (FN) & \ref{sec:mechanistic} \\
20	Latent aggregation & LSC & $-3.5$\,pp (FN) & \ref{sec:mechanistic} \\
21	Adaptive gating & DALS & $+0.71$\,pp (SciERC)$^\ddagger$ & App.~\ref{app:dals} \\
22	Supervised verifier & LGB & $+0.30$\,pp (OOF) & \ref{sec:verifier} \\
23	Sup.\ combination & LR/MLP/RF & $-0.4$ to $-3.1$\,pp & App.~\ref{app:supervised_combination} \\
24	Cross-model & Qwen$+$LLaMA & $\mathbf{+0.42}$\,pp (FN) & \ref{sec:cross_model} \\
25	\bottomrule
26	\end{tabular}}
27	{\footnotesize $^\dagger$Few-NERD only; SciERC $+0.2$\,pp ($p{=}0.29$). $^\ddagger$Seed-sensitive ($\sigma{=}0.48$\,pp).}
28	\end{table}
29	
30	\subsection{Cross-Model Self-Consistency}\label{sec:cross_model}
31	
32	Mixing samples from architecturally distinct models can partially bypass within-model degeneracy.
33	Combining 4 samples each from Qwen3-8B and
…[truncated 764 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 3498 · 2026-05-22T07:58:58.919269+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/single_signal.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/single_signal.tex"
  }
}
```

</details>

---


### Tool result

_source line 3499 · 2026-05-22T07:58:59.471902+00:00_

1	\section{Where Single-Signal Selection Fails}\label{sec:selection_gap}
2	
3	\paragraph{Definitional vs.\ empirical.}
4	We decompose the correlation-selection gap into two layers.
5	The first is structural: four of five signals are instance-level aggregates that assign identical scores to all $N$ candidates from a given input (\S\ref{sec:formulation}), so they estimate quality across inputs but cannot rank candidates within an instance---selection failure is a design property, not an empirical finding.
6	The second layer is empirical and constitutes the core diagnostic: LP---the only per-sample signal---suffers compression under constrained decoding, with 60\% of SciERC instances showing within-instance LP range below 0.041 nats (Appendix~\ref{app:logprob_ties}), effectively eliminating the variation needed for sample discrimination. Even where LP varies, selection gains depend on LP-quality alignment rather than degeneracy alone.
7	Cross-instance $\rho$ (Table~\ref{tab:quality_estimation}) is attenuated by varying instance difficulty; within-instance $\rho$ directly measures whether LP discriminates candidates for a fixed input, making it the relevant predictor of selection success.
8	
9	\begin{table}[t]
10	\centering
11	\small
12	\caption{Best-of-$N$ selection (macro F1) on SciERC ($N{=}8$, $T{=}1.0$). Selection signals: 2-seed mean${\pm}\sigma$; baselines: 3-seed (Oracle${=}0.781$, Greedy${=}0.667$). LP is per-sample; others use consensus-proximity. $^\dagger$One score per input.}
13	\label{tab:selection}
14	\begin{tabular}{lcc}
15	\toprule
16	Method & NER F1 & $p$ \\
17	\midrule
18	Oracle & $0.775 \pm 0.001$ & --- \\
19	Greedy ($T{=}0$) & $0.645 \pm 0.001$ & --- \\
20	\midrule
21	LP           & $\mathbf{0.647} \pm 0.005$ & .29 \\
22	SJ           & $0.646 \pm 0.002$ & .67 \\
23	FK           & $0.646 \pm 0.001$ & .79 \\
24	EM           & $0.637 \pm 0.001$ & n/a$^\dagger$ \\
25	VC           & $0.623 \pm 0.004$ & n/a$^\dagger$ \\
26	\midrule
27	Random       & $0.61
…[truncated 2668 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 3500 · 2026-05-22T07:58:59.522699+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/background.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/background.tex"
  }
}
```

</details>

---


### Tool result

_source line 3501 · 2026-05-22T07:58:59.523072+00:00_

1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Test-time compute scaling.}
4	Self-consistency \cite{wang2023selfconsistency} and best-of-$N$ \cite{snell2025scaling, brown2024monkeys} drive large gains on reasoning and code \cite{chen2021codex}.
5	Reward-free selectors \cite{taubenfeld2025cisc, kang2025selfcertainty}, BoN scaling laws \cite{gao2023scaling}, adaptive allocation \cite{aggarwal2023adaptive}, and trained verifiers \cite{cobbe2021verifiers, lightman2024verify} all target discrete-answer settings; structured prediction requires different aggregation because degeneracy operates at the entity-set level.
6	
7	\paragraph{SC failure modes and fine-grained variants.}
8	\citet{chen2023twofailures} identify SC failures where consistent outputs are systematically wrong; \citet{huang2024large} show LLMs cannot self-correct reasoning without external feedback.
9	\citet{chen2024usc} extend SC to free-form tasks and \citet{thirukovalluru2024atomic} decompose claims atomically; both face limits under constrained decoding where sub-output agreement does not translate to selection gain (\S\ref{sec:selection_gap}).
10	
11	\paragraph{Consistency for structured IE.}
12	\citet{yao2026consistency} demonstrate task-level correlation ($\rho$ up to 0.47) between consistency and quality across NER/RE tasks; we diagnose why this correlation fails to yield selection gain, identifying entity-level failure mechanisms absent from their task-level analysis and providing operational bypasses ($+0.32$--$1.40$\,pp).
13	\citet{xie2023zeroshot} propose entity voting for zero-shot NER and \citet{xie2024selfimproving} report positive SC under zero-shot prompting where diversity is high---contrasting with our fine-tuned setting where degeneracy inverts diversity.
14	\paragraph{Uncertainty estimation and MBR.}
15	Our selection instantiates MBR decoding \cite{eikema2022sampling, denero2009fast}; despite MBR's success in translation \cite{freitag2022high} and code generation \cite{jin
…[truncated 675 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 3502 · 2026-05-22T07:58:59.975065+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 3503 · 2026-05-22T07:59:00.427776+00:00_

1	Our evidence is correlational and theoretical (MBR framework, conditional decomposition), not interventional: we have not performed controlled interventions (e.g., artificially varying degeneracy while holding other factors constant), and the cascade stages interact in ways that resist decomposition into independent causal effects ($R^2{<}0$; \S\ref{sec:selection_gap}); causal claims require future intervention experiments.
2	
3	Scope: structured IE (NER primary, RE and SQL exploratory), English only, open-weight (Qwen and LLaMA) and closed-source (GPT-5.5) families, fine-tuned (4B--14B) and zero-shot (72B, GPT-5.5) regimes, sample budget $N{\leq}32$.
4	Our evaluation covers four NER datasets; the RE extension covers a single SciERC benchmark ($n{=}397$; $40$\% of instances yield zero F1, primarily from upstream entity span errors), and the SQL extension covers a single Spider subset ($n{=}196$) with 87.2\% degeneracy---both are exploratory and do not support generalization claims.
5	All experiments use English-language datasets; cross-lingual generalization remains untested.
6	Cross-model consistency results (\S\ref{sec:cross_model}) are limited to one dataset (Few-NERD) and one model pair (Qwen3-8B + LLaMA-3.1-8B).
7	Entity-level construction assumes the model produces useful partial outputs across samples; when model capability is insufficient (WNUT-17, 51\% F1${=}0$), this precondition fails and construction cannot improve over greedy.
8	Entity-level construction requires $N{\times}$ inference cost for $+1$\textendash$1.4$\,pp gain; cost-effectiveness may not justify deployment in resource-constrained settings.
9	We cover 4B\textendash 14B fine-tuned, 72B zero-shot, and GPT-5.5 zero-shot; the gap persists across all but behavior with 72B fine-tuning is untested.
10	Frontier API models exhibit markedly different degeneracy profiles (e.g., Claude Sonnet~4 at 74\% vs.\ DeepSeek Chat at 5.5\%; Table~\ref{tab:frontier_sc_cross}), suggesting that our findings from f
…[truncated 3975 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 3504 · 2026-05-22T07:59:00.729564+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "decisions.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "file": "decisions.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 3505 · 2026-05-22T07:59:00.780360+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/decisions.yaml\", \"content\": \"_next_id: 238\\ndecisions:\\n- id: D001\\n  date: 2026-05-14 04:23 UTC\\n  summary: 'MVP 方案: ACE05 上验证 structural consistency vs Fleiss'' Kappa 的 correlation\\n    差异'\\n  rationale: 'PMC12888769 用 surface-level Fleiss'' Kappa 在 zero-shot 模型上得到 ρ=0.20-0.28，我们假设\\n    fine-tuned 模型 + structural consistency (soft Jaccard) 能达到 ρ≥0.40。这是整个论文的基础假设——如果\\n    structural consistency 不能更好地预测准确率，后续的 adaptive gating 无从谈起。Phase 0 pilot 设计: Qwen3-8B\\n    fine-tuned on ACE05, N=8 samples, 200 instances, 对比两种 consistency metric 的 Spearman\\n    ρ。Pass ≥0.40, Fail <0.30。'\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-14 04:27 UTC\\n  summary: 采纳 Reviewer 审查意见，收紧 MVP pass/fail 标准\\n  rationale: 'Reviewer 指出 5 个问题，全部合理采纳：(1) PASS 必须要求 EAE (high-headroom subtask) ρ≥0.40，仅\\n    NER 通过不够（ceiling effect 可能虚高）；(2) MARGINAL 区间加 time-boxed protocol: N=16 追加 +\\n    1天上限；(3) 加 fine-tuning 质量门控 (NER≥73, EAE≥45)，模型不行时先修 fine-tuning；(4) ACE05 今天必须确认；(5)\\n    监控 T=1.0 per-sample F1 分布，>30% F1=0 时追加 T=0.7。'\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-14 04:53 UTC\\n  summary: SciERC RE 替代 ACE05 EAE 作为 MVP high-headroom subtask\\n  rationale: ACE05 需 LDC 许可，用户未确认。SciERC 公开可得，有 NER+RE 两个 subtask。RE base F1 ~47（与\\n    ACE05 EAE ~52 相当），结构复杂度高（entity pair + relation type），headroom 大，是 EAE 的合理替代。PASS\\n    标准更新为 RE ρ≥0.40。需要补实现 RE 的 consistency + evaluation + pipeline 支持。\\n  related_experiments: []\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-14 07:38 UTC\\n  summary: 'Gate 0: NER PASS (60.4%), RE FAIL (33.8%). 执行方案 C——当前模型先跑 pilot + 追训改进版，需修复\\n    RE evaluation'\\n  rationale: RE 33.8% 低于 40% 阈值但不阻塞 pilot：(1) headroom 大，oracle best-of-N 有提升空间；(2)\\n    consistency correlation 不要求高绝对 F1，要求 per-instance variance；(3) 弱模型上验证假设结论更强。但\\n    Reviewer 发
…[truncated 1441 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 3506 · 2026-05-22T07:59:10.828229+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 3507 · 2026-05-22T07:59:11.732049+00:00_

File content (65633 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 903
}
```

</details>

---


### Tool call

_source line 3508 · 2026-05-22T07:59:11.732432+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/checklist.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/checklist.tex"
  }
}
```

</details>

---


### Tool call

_source line 3509 · 2026-05-22T07:59:11.732607+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/struct_self_consist_ie/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/struct_self_consist_ie/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 3510 · 2026-05-22T07:59:12.184485+00:00_

1	% Responsible NLP Research Checklist
2	% Following the ACL Rolling Review guidelines:
3	% https://aclrollingreview.org/responsibleNLPresearch/
4	
5	\subsection*{A\hspace{0.5em} For Every Submission}
6	
7	\begin{enumerate}
8	\item[A1.] \textbf{Did you discuss the limitations of your work?}\\
9	Yes. See the Limitations section after the Conclusion.
10	
11	\item[A2.] \textbf{Did you discuss any potential risks of your work?}\\
12	Yes. See the Ethics Statement. This work analyzes existing confidence signals for NER and identifies when they fail; the findings reduce risk of deploying unreliable confidence-based selection in production systems. No dual-use concerns.
13	
14	\item[A3.] \textbf{Do the abstract and introduction summarize the paper's main claims?}\\
15	Yes. The Abstract and Section~\ref{sec:introduction} (3 enumerated contributions) summarize all main claims with supporting evidence pointers.
16	\end{enumerate}
17	
18	\subsection*{B\hspace{0.5em} Did you use or create scientific artifacts?}
19	
20	Yes. We use existing datasets and pre-trained models.
21	
22	\begin{enumerate}
23	\item[B1.] \textbf{Did you cite the creators of artifacts you used?}\\
24	Yes. All datasets are cited: SciERC \cite{luan2018scierc}, CoNLL-2003 \cite{tjongkimsang2003conll}, Few-NERD \cite{ding2021fewnerd}, WNUT-17 \cite{derczynski2017wnut}. Models: Qwen3-8B/4B and LLaMA-3.1-8B-Instruct. Training framework: LLaMA Factory \cite{zheng2024llamafactory}. Constrained decoding: XGrammar \cite{dong2024xgrammar}. See Sections~\ref{sec:introduction}, \ref{sec:evaluation}, and Appendix~\ref{app:training}.
25	
26	\item[B2.] \textbf{Did you discuss the license or terms for use and/or distribution of any artifacts?}\\
27	Partially. The Ethics Statement notes that CoNLL-2003 is derived from the Reuters RCV1 corpus, available under a NIST agreement for research. SciERC, Few-NERD, and WNUT-17 are publicly available research benchmarks. Qwen3 and LLaMA-3.1 are open-weight models released under their r
…[truncated 4168 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool result

_source line 3511 · 2026-05-22T07:59:12.184870+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 3512 · 2026-05-22T07:59:12.185035+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/struct_self_consist_ie/agent/config*.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/struct_self_consist_ie/agent/config*.yaml"
  }
}
```

</details>

---


### Tool result

_source line 3513 · 2026-05-22T07:59:12.235444+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 3514 · 2026-05-22T07:59:15.850205+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/struct_self_consist_ie/**/config*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/struct_self_consist_ie/**/config*"
  }
}
```

</details>

---


### Tool result

_source line 3515 · 2026-05-22T07:59:16.804280+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 3516 · 2026-05-22T07:59:16.804627+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 3517 · 2026-05-22T07:59:17.557953+00:00_

1	\section{Notation}\label{app:notation}
2	
3	Table~\ref{tab:notation} summarizes the notation used throughout the paper.
4	
5	\begin{table}[h]
6	\centering
7	\small
8	\begin{tabular}{cl}
9	\toprule
10	Symbol & Meaning \\
11	\midrule
12	$\mathcal{M}$ & Language model \\
13	$x$ & Input instance \\
14	$y_i$ & $i$-th stochastic sample \\
15	$N$ & Number of samples \\
16	$T$ & Sampling temperature \\
17	$c(\cdot)$ & Confidence signal \\
18	SJ & Soft Jaccard similarity \\
19	FK & Fleiss' $\kappa$ \\
20	EM & Exact-match voting rate \\
21	VC ($c_{\mathrm{vc}}$) & Entity voting confidence \\
22	LP ($c_{\mathrm{lp}}$) & Log-probability (mean token log-likelihood) \\
23	\bottomrule
24	\end{tabular}
25	\caption{Notation used throughout the paper.}
26	\label{tab:notation}
27	\end{table}
28	
29	\section{Robustness Analysis}\label{app:robustness}
30	
31	We exclude instances with empty gold annotations from all correlation analyses (CoNLL: 697/3{,}453 instances, 20.2\%; SciERC: 22/551, 4.0\%).
32	For these instances, F1 is trivially zero regardless of prediction quality, and consistency signals reflect agreement on the empty set rather than extraction quality. Including them inflates or deflates Spearman $\rho$ depending on signal behavior at the boundary.
33	
34	\begin{table}[t]
35	\centering
36	\small
37	\caption{Signal robustness across configurations (Spearman $\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: transfer across model families (both 8B) (LLaMA CoNLL $N{=}16$, 3-seed mean $\pm\sigma$). $^\dagger$Mean over 3 seeds ($\sigma{=}0.013$; individual: 0.398, 0.423, 0.410). $\sigma$ computed as sample standard deviation.}
38	\label{tab:robustness}
39	\begin{tabular}{llcc}
40	\toprule
41	& & NER $\rho$ & RE $\rho$ \\
42	\midrule
43	\multicolumn{4}{l}{\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\
44	\quad SJ & $T{=}0.7$ & 0.364 & 0.234 \\
45	\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\
46	\quad FK & $T{=}0.7$ & 0.289 & 0.184 \\
47	\quad FK & $
…[truncated 4982 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 753
}
```

</details>

---


### Tool call

_source line 3518 · 2026-05-22T07:59:17.658786+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_round_33/submitted.pdf",
  "pages": "1-9"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_round_33/submitted.pdf",
    "pages": "1-9"
  }
}
```

</details>

---


### Tool result

_source line 3519 · 2026-05-22T07:59:18.413621+00:00_

PDF pages extracted: 9 page(s) from /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_round_33/submitted.pdf (971.8KB)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 754
}
```

</details>

---


### Tool call

_source line 3520 · 2026-05-22T07:59:31.268328+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "output_mode": "content",
  "head_limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
    "output_mode": "content",
    "head_limit": "20"
  }
}
```

</details>

---


### Tool call

_source line 3521 · 2026-05-22T07:59:31.371325+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/struct_self_consist_ie/**/project.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/struct_self_consist_ie/**/project.yaml"
  }
}
```

</details>

---


### Tool result

_source line 3522 · 2026-05-22T07:59:31.422087+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 3523 · 2026-05-22T07:59:32.226833+00:00_

AGENTS.md:82:如果项目配置了外部审稿（`external_review.paperreview_ai.enabled: true`）：
AGENTS.md:83:- 在分配内部 Reviewer 的同时，调用 `request_external_review()` 向用户群发送协助卡片
AGENTS.md:85:- 用户在群里粘贴 paperreview.ai 审稿结果后，将其作为 `[外部审稿: Stanford Agentic Reviewer]` 纳入最终报告的独立 section
AGENTS.md:87:- 如果内部审稿结束时外部结果仍未返回，用 `get_external_review_status()` 检查状态，在报告中标注「外部审稿：未返回」
AGENTS.md:163:`director_get_project_overview`, `director_post_to_reviewer`, `dispatch_visual_check`, `get_external_review_status`, `get_visual_check_status`, `read_local_file`, `read_project_file`, `request_external_review`, `request_study_approval`, `submit_review_report_to_research_director`, `update_review_issues`
CLAUDE.md:82:如果项目配置了外部审稿（`external_review.paperreview_ai.enabled: true`）：
CLAUDE.md:83:- 在分配内部 Reviewer 的同时，调用 `request_external_review()` 向用户群发送协助卡片
CLAUDE.md:85:- 用户在群里粘贴 paperreview.ai 审稿结果后，将其作为 `[外部审稿: Stanford Agentic Reviewer]` 纳入最终报告的独立 section
CLAUDE.md:87:- 如果内部审稿结束时外部结果仍未返回，用 `get_external_review_status()` 检查状态，在报告中标注「外部审稿：未返回」
CLAUDE.md:163:`director_get_project_overview`, `director_post_to_reviewer`, `dispatch_visual_check`, `get_external_review_status`, `get_visual_check_status`, `read_local_file`, `read_project_file`, `request_external_review`, `request_study_approval`, `submit_review_report_to_research_director`, `update_review_issues`
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/chats/archive/feishu_group_oc_1b56445332d8ca2b4964b30f300f0e00_director_20260516T094957_715546.jsonl:1676:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/chats/archive/feishu_group_oc_1b56445332d8ca2b4964b30f300f0e00_director_20260516T094957_715546.jsonl:2121:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/logs/chats/archive/feishu_group_oc_1b56445332d8ca2b4964b30f300f0e00_director_20260516T094957_715546.jsonl:2402:[Omitted long matching line]
/home/ubuntu/.agent-
…[truncated 1556 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Grep",
  "elapsed_ms": 958
}
```

</details>

---


### Tool call

_source line 3524 · 2026-05-22T07:59:35.991640+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/struct_self_consist_ie/**/*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/agent"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/struct_self_consist_ie/**/*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/agent"
  }
}
```

</details>

---


### Tool result

_source line 3525 · 2026-05-22T07:59:36.042258+00:00_

&lt;tool_use_error>Directory does not exist: /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/agent. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_director_0161122b.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 3526 · 2026-05-22T07:59:43.773311+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "paper_checklist.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "file": "paper_checklist.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 3527 · 2026-05-22T07:59:43.823933+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'struct_self_consist_ie'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 3528 · 2026-05-22T07:59:45.078625+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie -name \"*.yaml\" -not -path \"*/logs/*\" -not -path \"*decisions.yaml\" 2>/dev/null | head -20",
  "description": "Find yaml config files in project"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie -name \"*.yaml\" -not -path \"*/logs/*\" -not -path \"*decisions.yaml\" 2>/dev/null | head -20",
    "description": "Find yaml config files in project"
  }
}
```

</details>

---


### Tool result

_source line 3529 · 2026-05-22T07:59:45.280842+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/dream_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/writing_plan.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper_provenance.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/literature_map.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/constraints.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/mistakes.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T092241/median/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T092241/median/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T092241/worst/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T092241/worst/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T092241/meta.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T092241/best/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T092241/best/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T225436/meta.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_202
…[truncated 644 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 202
}
```

</details>

---


### Tool call

_source line 3530 · 2026-05-22T07:59:50.330611+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review\\|paperreview_ai\" /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/*.yaml 2>/dev/null | head -10",
  "description": "Search for external review config in project yaml files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"external_review\\|paperreview_ai\" /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/*.yaml 2>/dev/null | head -10",
    "description": "Search for external review config in project yaml files"
  }
}
```

</details>

---


### Tool result

_source line 3531 · 2026-05-22T07:59:51.184291+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 853
}
```

</details>

---


### Tool call

_source line 3532 · 2026-05-22T07:59:51.184715+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1 -maxdepth 2 -name \"config*.yaml\" -o -name \"settings*.yaml\" -o -name \"project_config*\" 2>/dev/null | head -10",
  "description": "Find project config files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1 -maxdepth 2 -name \"config*.yaml\" -o -name \"settings*.yaml\" -o -name \"project_config*\" 2>/dev/null | head -10",
    "description": "Find project config files"
  }
}
```

</details>

---


### Tool result

_source line 3533 · 2026-05-22T07:59:51.235242+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 3534 · 2026-05-22T07:59:56.204168+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0514_1/config* /home/ubuntu/.agent-ml-research-idea_gen_0514_1/settings* /home/ubuntu/.agent-ml-research-idea_gen_0514_1/*.yaml 2>/dev/null | head -10",
  "description": "Search for external review config in root config"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -r \"external_review\\|paperreview\" /home/ubuntu/.agent-ml-research-idea_gen_0514_1/config* /home/ubuntu/.agent-ml-research-idea_gen_0514_1/settings* /home/ubuntu/.agent-ml-research-idea_gen_0514_1/*.yaml 2>/dev/null | head -10",
    "description": "Search for external review config in root config"
  }
}
```

</details>

---


### Tool result

_source line 3535 · 2026-05-22T07:59:56.305018+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 3536 · 2026-05-22T08:00:22.250208+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "struct_self_consist_ie",
  "review_chat_id": "oc_3897c2857f11615119e277e820eae311"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "review_chat_id": "oc_3897c2857f11615119e277e820eae311"
  }
}
```

</details>

---


### Tool result

_source line 3537 · 2026-05-22T08:00:45.042109+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 22791
}
```

</details>

---


### Tool call

_source line 3538 · 2026-05-22T08:00:51.096527+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "你是 Reviewer 1，负责 **方法严谨性 + 实验设计** 的审查。\n\n## Venue 信息\n- **目标会议**：EMNLP 2026（通过 ARR May 2026 cycle 投稿）\n- **截止日期**：2026-05-25\n- **页数限制**：正文 8 页，参考文献不限，Limitations 和 Ethics 不计入页限\n- **模板**：ACL style（`\\usepackage[review]{acl}`）\n- **匿名规则**：Double-blind\n\n## 论文路径\n- LaTeX 源码：`projects/struct_self_consist_ie/docs/paper/main.tex`（入口文件，各 section 在 `sections/` 下）\n- PDF：`/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_round_33/submitted.pdf`\n\n## 论文概要\n论文研究 test-time compute scaling（self-consistency）在 NER 任务上为什么失败。提出一个四阶段诊断级联（QE → degeneracy → agreement fidelity → LP compression），定义\"correlation-selection gap\"：QE 信号在 population level 预测质量有效（ρ 达 0.45，AUROC 0.82），但 instance-level selection 几乎无效（<1pp）。提出 entity-level construction 作为 bypass（+0.32–1.40pp）。\n\n## 你的审查侧重\n请重点关注以下方面，并给出逐条评价：\n\n1. **Diagnostic Framework 的合理性**：四阶段 cascade 的设计是否有理论支撑？各阶段之间的关系是否清晰？\"correlation-selection gap\" 的定义是否严谨？\n2. **实验设计与控制变量**：数据集选择（4 个 NER + RE + SQL）是否充分？模型选择（Qwen3-8B, LLaMA-3.1-8B, 4B/14B ablation, 72B, GPT-5.5）是否合理？N 和 T 的消融是否充分？\n3. **统计方法**：Spearman ρ、AUROC、paired bootstrap p-value、Holm-Bonferroni 多重比较校正的使用是否正确？置信区间和 effect size 报告是否充分？power analysis 是否合理？\n4. **实验结论的可靠性**：核心发现（correlation-selection gap、α→0 为 binding constraint、θ_crit=0.70）是否被数据充分支持？是否有 cherry-picking 嫌疑？\n5. **Theory section（Section 6）**：Degeneracy Decomposition bound 的证明是否正确？MBR 解释是否合理？Proposition 1 的假设是否过强？\n6. **Reproducibility**：实验细节是否足够复现？超参数是否完整报告？\n\n请输出完整的审稿意见，包含：Summary、Strengths（逐条）、Weaknesses（逐条，这是重点）、Questions、Minor Issues。",
  "reviewer_id": "1",
  "project": "struct_self_consist_ie",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "你是 Reviewer 1，负责 **方法严谨性 + 实验设计** 的审查。\n\n## Venue 信息\n- **目标会议**：EMNLP 2026（通过 ARR May 2026 cycle 投稿）\n- **截止日期**：2026-05-25\n- **页数限制**：正文 8 页，参考文献不限，Limitations 和 Ethics 不计入页限\n- **模板**：ACL style（`\\usepackage[review]{acl}`）\n- **匿名规则**：Double-blind\n\n## 论文路径\n- LaTeX 源码：`projects/struct_self_consist_ie/docs/paper/main.tex`（入口文件，各 section 在 `sections/` 下）\n- PDF：`/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_round_33/submitted.pdf`\n\n## 论文概要\n论文研究 test-time compute scaling（self-consistency）在 NER 任务上为什么失败。提出一个四阶段诊断级联（QE → degeneracy → agreement fidelity → LP compression），定义\"correlation-selection gap\"：QE 信号在 population level 预测质量有效（ρ 达 0.45，AUROC 0.82），但 instance-level selection 几乎无效（<1pp）。提出 entity-level construction 作为 bypass（+0.32–1.40pp）。\n\n## 你的审查侧重\n请重点关注以下方面，并给出逐条评价：\n\n1. **Diagnostic Framework 的合理性**：四阶段 cascade 的设计是否有理论支撑？各阶段之间的关系是否清晰？\"correlation-selection gap\" 的定义是否严谨？\n2. **实验设计与控制变量**：数据集选择（4 个 NER + RE + SQL）是否充分？模型选择（Qwen3-8B, LLaMA-3.1-8B, 4B/14B ablation, 72B, GPT-5.5）是否合理？N 和 T 的消融是否充分？\n3. **统计方法**：Spearman ρ、AUROC、paired bootstrap p-value、Holm-Bonferroni 多重比较校正的使用是否正确？置信区间和 effect size 报告是否充分？power analysis 是否合理？\n4. **实验结论的可靠性**：核心发现（correlation-selection gap、α→0 为 binding constraint、θ_crit=0.70）是否被数据充分支持？是否有 cherry-picking 嫌疑？\n5. **Theory section（Section 6）**：Degeneracy Decomposition bound 的证明是否正确？MBR 解释是否合理？Proposition 1 的假设是否过强？\n6. **Reproducibility**：实验细节是否足够复现？超参数是否完整报告？\n\n请输出完整的审稿意见，包含：Summary、Strengths（逐条）、Weaknesses（逐条，这是重点）、Questions、Minor Issues。",
    "reviewer_id": "1",
    "project": "struct_self_consist_ie",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 3539 · 2026-05-22T08:00:55.017062+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 3920
}
```

</details>

---


### Tool call

_source line 3540 · 2026-05-22T08:00:57.632813+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "你是 Reviewer 2，负责 **新颖性 + 完整性 + 写作质量** 的审查。\n\n## Venue 信息\n- **目标会议**：EMNLP 2026（通过 ARR May 2026 cycle 投稿）\n- **截止日期**：2026-05-25\n- **页数限制**：正文 8 页，参考文献不限，Limitations 和 Ethics 不计入页限\n- **模板**：ACL style（`\\usepackage[review]{acl}`）\n- **匿名规则**：Double-blind\n\n## 论文路径\n- LaTeX 源码：`projects/struct_self_consist_ie/docs/paper/main.tex`（入口文件，各 section 在 `sections/` 下）\n- PDF：`/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_round_33/submitted.pdf`\n\n## 论文概要\n论文研究 test-time compute scaling（self-consistency）在 NER 任务上为什么失败。提出四阶段诊断级联框架，发现\"correlation-selection gap\"——QE 信号预测质量有效但 instance-level 选择无效。提出 entity-level construction bypass。覆盖 4 个 NER 数据集、2 个模型家族、RE 和 SQL 扩展。\n\n## 你的审查侧重\n请重点关注以下方面，并给出逐条评价：\n\n1. **新颖性与贡献定位**：\n   - \"Correlation-selection gap\" 概念是否真正新颖？与 Yao et al. (2026)、Yun et al. (2025)、Chen et al. (2024) 的差异是否清晰界定？\n   - 四阶段 diagnostic cascade 是方法贡献还是纯分析贡献？对社区的实际价值？\n   - Entity-level construction 是否已有先例（Xie et al. 2023 entity voting）？增量贡献是否足够？\n\n2. **Related Work 覆盖**：\n   - 是否遗漏重要相关工作？特别关注：MBR decoding for NLP、test-time compute scaling、NER aggregation、uncertainty estimation 领域\n   - 与 concurrent work 的区分是否充分？\n\n3. **写作质量**：\n   - 论文结构是否清晰？9 个 section 的组织是否合理？\n   - 术语定义（degeneracy, capability ceiling, correlation-selection gap, introspection boundary）是否精确且一致？\n   - Figure/Table 质量：是否信息密度适当？caption 是否自包含？\n   - Abstract 是否准确反映论文内容？是否有过度声明？\n\n4. **格式规范**：\n   - 是否符合 ACL style 要求？\n   - 匿名化是否到位（检查是否泄露作者身份）？\n   - Limitations section 是否充分但不过长？\n   - Responsible NLP Checklist 是否完整？注意：ARR checklist 在 OpenReview submission form 里面填写，不应在论文 PDF 中占大量篇幅\n\n5. **完整性**：\n   - 核心声明是否都有对应实验支持？\n   - 是否有 claim 超出实验范围的情况（overclaiming）？\n   - Negative results 的呈现是否诚实、充分？\n\n请输出完整的审稿意见，包含：Summary、Strengths（逐条）、Weaknesses（逐条，这是重点）、Questions、Missing References、Minor Issues。",
  "reviewer_id": "2",
  "project": "struct_self_consist_ie",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "你是 Reviewer 2，负责 **新颖性 + 完整性 + 写作质量** 的审查。\n\n## Venue 信息\n- **目标会议**：EMNLP 2026（通过 ARR May 2026 cycle 投稿）\n- **截止日期**：2026-05-25\n- **页数限制**：正文 8 页，参考文献不限，Limitations 和 Ethics 不计入页限\n- **模板**：ACL style（`\\usepackage[review]{acl}`）\n- **匿名规则**：Double-blind\n\n## 论文路径\n- LaTeX 源码：`projects/struct_self_consist_ie/docs/paper/main.tex`（入口文件，各 section 在 `sections/` 下）\n- PDF：`/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_round_33/submitted.pdf`\n\n## 论文概要\n论文研究 test-time compute scaling（self-consistency）在 NER 任务上为什么失败。提出四阶段诊断级联框架，发现\"correlation-selection gap\"——QE 信号预测质量有效但 instance-level 选择无效。提出 entity-level construction bypass。覆盖 4 个 NER 数据集、2 个模型家族、RE 和 SQL 扩展。\n\n## 你的审查侧重\n请重点关注以下方面，并给出逐条评价：\n\n1. **新颖性与贡献定位**：\n   - \"Correlation-selection gap\" 概念是否真正新颖？与 Yao et al. (2026)、Yun et al. (2025)、Chen et al. (2024) 的差异是否清晰界定？\n   - 四阶段 diagnostic cascade 是方法贡献还是纯分析贡献？对社区的实际价值？\n   - Entity-level construction 是否已有先例（Xie et al. 2023 entity voting）？增量贡献是否足够？\n\n2. **Related Work 覆盖**：\n   - 是否遗漏重要相关工作？特别关注：MBR decoding for NLP、test-time compute scaling、NER aggregation、uncertainty estimation 领域\n   - 与 concurrent work 的区分是否充分？\n\n3. **写作质量**：\n   - 论文结构是否清晰？9 个 section 的组织是否合理？\n   - 术语定义（degeneracy, capability ceiling, correlation-selection gap, introspection boundary）是否精确且一致？\n   - Figure/Table 质量：是否信息密度适当？caption 是否自包含？\n   - Abstract 是否准确反映论文内容？是否有过度声明？\n\n4. **格式规范**：\n   - 是否符合 ACL style 要求？\n   - 匿名化是否到位（检查是否泄露作者身份）？\n   - Limitations section 是否充分但不过长？\n   - Responsible NLP Checklist 是否完整？注意：ARR checklist 在 OpenReview submission form 里面填写，不应在论文 PDF 中占大量篇幅\n\n5. **完整性**：\n   - 核心声明是否都有对应实验支持？\n   - 是否有 claim 超出实验范围的情况（overclaiming）？\n   - Negative results 的呈现是否诚实、充分？\n\n请输出完整的审稿意见，包含：Summary、Strengths（逐条）、Weaknesses（逐条，这是重点）、Questions、Missing References、Minor Issues。",
    "reviewer_id": "2",
    "project": "struct_self_consist_ie",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 3541 · 2026-05-22T08:00:59.601806+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1968
}
```

</details>

---


### Assistant

_source line 3542 · 2026-05-22T08:01:04.039973+00:00_

Round 1 已启动：
- 视觉审查 Agent：已派发（fire-and-forget）
- Reviewer 1（方法严谨性 + 实验设计）：已分配
- Reviewer 2（新颖性 + 完整性 + 写作质量）：已分配

等待两位 Reviewer 返回审稿意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 260

## Round 260

2 recorded events


### User

_source line 3543 · 2026-05-22T08:08:07.787330+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 审稿意见：Characterizing the Capability Ceiling of Self-Consistency

## Summary

本文研究 test-time compute scaling（self-consistency）在 NER 任务上的失败原因。作者提出四阶段诊断级联框架（degeneracy → capability ceiling → correlation-selection gap → entity-level construction bypass），核心发现是"correlation-selection gap"——QE 信号在 population level 能预测输出质量（Spearman ρ≤0.45, AUROC≤0.82），但 instance-level 选择几乎无效（多数数据集 <1 pp）。实验覆盖 4 个 NER 数据集（SciERC, CoNLL, Few-NERD, WNUT-17）、2 个模型家族（Qwen3-8B, LLaMA-3.1-8B）、RE 和 SQL 扩展。Entity-level construction 在 Few-NERD 上获得 +1.4 pp，但在其他数据集上效果有限。

---

## 总体评分

**Overall**: 3.5 — Borderline Conference

**一句话总结**: 对自洽性在结构化预测上失败的系统诊断工作扎实、统计严谨、附录详尽，但核心新颖性主要是分析性（negative result + diagnostic framework）而非方法性，且论文组织结构有待优化。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 3.5/5 | 方法论合理，统计检验（bootstrap CI、Holm-Bonferroni 校正、permutation test）全面严谨；但分析本质是 observational 而非 interventional，且模型多样性有限（仅 2 个开源 decoder-only 家族） |
| **Excitement** | 3/5 | Correlation-selection gap 概念有用但主要是 negative result 的诊断，entity-level construction 增量贡献有限（+1.4 pp 仅在 Few-NERD），对社区的实际方法论影响不确定 |
| **Reproducibility** | 4/5 | 47 页附录提供极其详尽的超参数、训练配置、per-type 分析；声明将发布代码和数据；Appendix k 完整列出训练配置 |
| **Confidence** | 4/5 | 熟悉 NER、test-time compute scaling、MBR decoding 相关文献 |

---

## 主要优势

**S1. 重要且诚实的 negative result。** 系统性地证明 self-consistency 在 NER 上失败，并诊断失败原因，填补了 test-time scaling 文献在结构化预测方面的空白。论文没有回避自身方法的局限——坦诚报告 entity-level construction 在 CoNLL 无效、SciERC 增益微弱（Table 2, Section 7.5）。这种诚实度在当前 NLP 文献中值得肯定。

**S2. 出色的统计严谨性。** 所有核心结论都有 bootstrap 95% CI（Appendix e）、Holm-Bonferroni 多重比较校正（Appendix f, Table 12）、permutation test、TOST 等效性检验（Appendix g, Table 15）。57 项统计检验的完整枚举（Table 12）是罕见的透明度。这直接回应了 ARR guidelines 中 R1（inappropriate statistics）和 R5（missing significance）的关切。

**S3. Correlation-selection gap 概念清晰且有迁移价值。** "QE 信号在 population-level 有效但 instance-level 失效" 的解耦不仅适用于 NER，对任何 set-valued structured output 的 test-time scaling 都有启示。Figure 1 简洁直观地传达了这一核心洞见。

**S4. 实验覆盖面广。** 9 种聚合方法（Table 2）、5 种 QE 信号（Table 3）、temperature/N-scaling/cross-model/cross-dataset 鲁棒性分析、RE 和 SQL 扩展、OOD 泛化（Appendix v）、verbalized confidence（Appendix w）——构成了对自洽性在 NER 上的近乎穷尽式分析。

**S5. MBR 理论联系。** Proposition 1（Entity Selection Bound）和 Proposition 2（Entity construction as MBR）将 entity-level 聚合与 MBR decoding 理论框架严格对接（Appendix p），为实验发现提供了理论基础。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] **实验 setup 位置反常，严重影响可读性**
- 具体位置：Section 7（page 6-7）
- 问题：Sections 3-6 已大量呈现实验结果（Table 1-2, Figure 1-4, Proposition 1），但实验设置（数据集、模型、训练细节）直到 Section 7 才给出。读者在 Section 3 看到"Qwen3-8B fine-tuned, Few-NERD, N=8, seed=42"时，尚不知道模型如何 fine-tune、数据集规模多大、LoRA 配置如何。更糟糕的是，Section 7 本身又混合了新结果（7.2 Quality Estimation Results, 7.3 Cross-Dataset Contrast, 7.4 Robustness, 7.5 Prescriptive Results），导致结果分散在 Sections 3-7 五个不同位置。
- 为什么影响接收：这不是风格偏好问题——它直接影响 reviewer 和读者评估实验有效性的能力。ARR reviewer guidelines 强调 soundness 评分必须基于方法论细节，但这些细节出现在结果之后。
- 建议修改方向：将 Section 7.1（Experimental Protocol）前置到 Section 2 之后、结果之前；将 7.2-7.5 的结果整合到对应的诊断阶段章节中。

**N2** [critical] **模型多样性不足以支撑"框架"级别的 claim**
- 具体位置：Section 7.1（Models and sampling）, Title, Abstract
- 问题：论文标题 "A Diagnostic Framework for Test-Time Aggregation in NER" 暗示通用性，但仅测试 2 个开源 decoder-only 模型家族（Qwen3-8B, LLaMA-3.1-8B-Instruct），均为 ~8B 参数。缺失：(a) 更大模型（70B+），degeneracy 可能随 scale 变化（论文自身在 Appendix t 提到 scale 影响但未测试更大模型）；(b) encoder-based 或 encoder-decoder 模型；(c) 闭源 API 模型（GPT-4, Claude），它们的 self-consistency 行为可能不同；(d) 专门为 NER fine-tune 的模型（如 GLiNER）。
- 为什么影响接收：两个同源同量级模型的结论泛化性有限。Limitations 承认这一点但过于轻描淡写（"our findings from fine-tuned open-weight models may not fully generalize to proprietary systems"）。ARR guidelines H13 指出不应要求超出 scope 的实验——但论文自身的 scope（"framework"）设定了高于 2-model 经验研究的期望。
- 建议修改方向：(a) 降低 claim 强度，将标题/摘要中的"framework"改为"empirical study"或明确限定为"open-weight 8B models"；或 (b) 补充至少 1 个差异化模型（larger scale 或不同架构）的验证。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] **Entity-level construction 新颖性不足，与 Xie et al. (2023) 的差异不够清晰**
- 具体位置：Section 6.1, Section 8
- 问题：Entity-level majority voting 的核心思想（对 entity set 中每个 entity 独立投票聚合，而非在 sample 级别选择）与 Xie et al. (2023) 的 entity voting 高度相似。论文的增量是 MBR 理论框架（Proposition 2）和 LP-weighted 变体，但实际性能差异不大（Table 2: entity-level construction 在 Few-NERD +1.0 pp，SciERC +0.42 pp，CoNLL 无增益）。Section 8 仅一句话提及 Xie et al.，未做详细对比。
- 建议：增加与 Xie et al. (2023) 的显式对比（实验或分析层面），明确 MBR 框架相对于简单 entity voting 的具体优势在哪些 regime 下体现。

**W2** [warning] **9 节结构过于碎片化，信息密度过高**
- 具体位置：全文
- 问题：8 页正文包含 9 个 section、至少 4 个 table、4 个 figure、2 个 proposition。关键概念（degeneracy, capability ceiling, correlation-selection gap, introspection boundary）在不同 section 分散定义。读者很难在一次阅读中建立完整的心智模型。特别是：
  - Section 3（Self-Verification Fails）和 Section 4（Single-Sample Selection Fails）各仅约半页，读起来像是被截断的分析
  - Section 8（Related Work）被压缩到不到半页（约 15 行），对于一篇定位为"诊断框架"的论文而言过于单薄
  - Section 9（Discussion and Conclusion）试图同时做讨论和总结，空间不足
- 建议：考虑合并 Sections 3-4 为一个 section，释放空间给 Related Work 和 Discussion。

**W3** [warning] **"Diagnostic cascade" 的贡献性质模糊——方法贡献还是分析贡献？**
- 具体位置：Section 2, Abstract, Title
- 问题：论文将四阶段 diagnostic cascade 包装为一个"framework"（标题中），但实际上它更接近一组针对特定现象的分析步骤。它不像 BERTScore、BLEU 等评估框架那样可直接被其他工作复用——其他研究者不会"运行"这个 cascade 来诊断自己的 self-consistency 问题，因为每一步都需要定制化分析。Section 2.1 的 Problem Formulation 试图形式化但实际操作依赖于大量 task-specific 判断（如 degeneracy threshold θ_deg=0.70 的选择）。
- 为什么影响评分：如果定位为分析贡献（"empirical study"），论文的预期标准更易满足；定位为"framework"则需要更高的通用性和可操作性证据。
- 建议：明确定位为分析贡献，或提供 framework 在新任务/数据集上的即插即用操作手册。

**W4** [warning] **观测性分析中隐含因果推断**
- 具体位置：Section 2（"Our analysis is observational"）vs. Sections 3-6 的叙述
- 问题：Section 2 明确声明"we characterize statistical associations...without claiming causal mechanisms"，但后续叙述多处隐含因果语言：
  - "degeneracy...is the binding constraint"（Section 4）
  - "LP compression limits exploitation"（Section 4）
  - "degeneracy alone, is the binding constraint"（Section 1, page 2）
  - Diagnostic cascade 的阶段顺序本身暗示因果链
  这些表述超出了观测性研究的 claim 范围。
- 建议：统一叙述风格，用"associated with" / "co-occurs with" 替代因果语言，或追加最少量的干预实验（如人为控制 degeneracy 观察下游效果）。

**W5** [warning] **Abstract 中"reliably predict"用词过强**
- 具体位置：Abstract, line 3-4
- 问题：Abstract 说 "Quality estimation signals reliably predict output quality (Spearman ρ up to 0.45; AUROC 0.82)"。ρ=0.45 仅解释 ~20% 方差，"reliably" 一词在统计学意义上站不住脚。论文正文后续也承认 "moderate correlation"（Section 7.2），与 abstract 的表述存在张力。
- 建议：将 "reliably predict" 改为 "show moderate-to-strong correlation with" 或类似措辞。

**W6** [warning] **Related Work（Section 8）覆盖不足**
- 具体位置：Section 8（page 8, ~15 行）
- 问题：对于一篇横跨 self-consistency、MBR decoding、NER aggregation、uncertainty estimation 四个子领域的论文，Related Work 过于简短。具体遗漏或讨论不足：
  - **MBR for structured outputs**：论文将 entity-level construction 形式化为 MBR（Section 6.1），但 Related Work 未深入讨论 MBR 在结构化生成中的应用（如 structure-conditional MBR 的更广泛文献）
  - **LLM calibration for structured tasks**：Kadavath et al. (2022) 被引用但未在 Related Work 中讨论；calibration 是论文的核心分析维度之一（Appendix c），值得在 Related Work 中定位
  - **Yao et al. (2026) 和 Yun et al. (2025)**：这两个最密切的 concurrent works 仅在 Introduction 中讨论了 2-3 句，Related Work 中完全未提及
- 建议：扩展 Related Work 至至少 20-25 行，将 Introduction 中对 Yao/Yun 的讨论移至 Related Work 并深化。

---

## 小问题（不影响接收）

- **M1**：Table 1 caption 中 "Selection signals: 2-seed mean±σ" 但正文 Section 4 中提到 "3-seed mean"，不一致（Table 1 vs. Table 4）。
- **M2**：Footnote 1（page 2）说 "RE F1 is contaminated by entity span errors"，但 Appendix o 的 RE 实验仍使用 F1——应在正文明确说明 RE 实验如何处理这一问题。
- **M3**：Figure 3 的 y 轴标注 "MV ΔF1 (pp)" 但在低 N 区间出现负值，caption 应解释这一 counterintuitive 结果（MV 在小 N 时反而损害性能）。
- **M4**：Section 6.2 引用 Fleiss (1971) 用于 inter-agreement 但实际使用的是 Soft Jaccard（Section 2.2），两种度量的关系未说明。
- **M5**：Appendix af（Anticipated Objections）的存在本身不常见——通常这些内容应整合到 Discussion 或 Related Work 中。虽然内容有用，但专设一个"预回应审稿意见"的 appendix 可能给 reviewer 留下防御性印象。
- **M6**：论文多处使用 "we" 的第一人称（符合 ACL 惯例），但 Responsible NLP Checklist（page 10）中对 AI assistants 的回答 "Yes. AI writing assistants were used for drafting and editing" 的透明度值得肯定。

---

## 格式合规检查

| 项目 | 状态 | 备注 |
|------|------|------|
| 正文页数 | ✅ 合规 | Sections 1-9 在 8 页内完成 |
| ACL style | ✅ 合规 | 使用 `\usepackage[review]{acl}` 格式 |
| 匿名化 | ✅ 合规 | "Anonymous ACL submission"，未发现作者身份泄露 |
| Limitations | ✅ 合规 | Page 9，覆盖 ~4 个要点，篇幅适中 |
| Ethics Statement | ✅ 合规 | Page 9-10 |
| Responsible NLP Checklist | ✅ 合规 | Page 10，在 PDF 内（ARR checklist 也在 OpenReview form 中填写） |
| References | ✅ | Pages 11-13，格式正确 |
| AI Assistants 声明 | ✅ | Section E1 明确披露 |

---

## 缺失引用（建议补充）

1. **DeNero et al. (2009)** "Learning from multiple annotations" 或类似的 entity aggregation 基础文献——论文将 entity-level construction 定位为核心贡献，应更完整地回顾 entity-level 聚合的先驱工作
2. **Minimum Bayes Risk for structured NLP** 的更广泛文献综述——论文引用了 Eikema & Aziz (2022) 和 Eikema et al. (2025)，但 MBR 在 parsing、translation 等结构化任务上的应用历史更长
3. **LLM calibration 综述**——论文使用 ECE（Appendix c）但未引用 calibration 领域的系统性综述

---

## 完整性评估

| 核心声明 | 实验支撑 | 评估 |
|--------|----------|------|
| QE 信号 population-level 有效 | Table 3 (ρ, AUROC), 5 signals × 4 datasets | ✅ 充分 |
| Instance-level 选择无效 | Table 1, Table 4, Figure 2, TOST 等效性检验 | ✅ 充分 |
| 四阶段 cascade 定位失败 | Sections 3-6, Proposition 1 | ⚠️ 各阶段证据充分，但"cascade"的阶段间因果关系未经验证 |
| Entity-level construction bypass | Table 2, Section 6.1, Appendix ah | ⚠️ 仅在 Few-NERD 有明确正向效果，CoNLL 无增益 |
| 泛化至 RE 和 SQL | Appendix o (RE), 正文简要提及 SQL | ⚠️ RE 有详细分析，SQL 证据极薄（仅 Section 1 和 Appendix ae 简要提及），overclaim 风险 |
| Negative results 诚实呈现 | 全文多处 | ✅ 出色 |

---

## 给 Director 的评分建议

**Overall Assessment: 3.5 (Borderline Conference)**

理由：这是一篇扎实的分析工作，统计严谨度在 NLP 论文中属上乘。Correlation-selection gap 概念有社区价值。但 (1) 核心贡献偏分析性而非方法性，entity-level construction 增量有限；(2) 仅 2 个模型家族限制了 "framework" claim 的说服力；(3) 论文结构需要重组以提升可读性。如果作者能解决 N1（结构重组）和 N2（模型多样性或 claim 降级），可以达到 4.0 (Conference) 水平。当前状态下，Findings 是安全着陆点。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 3544 · 2026-05-22T08:08:13.655258+00:00_

Reviewer 2 的意见已收到。等待 Reviewer 1 返回后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 261

## Round 261

2 recorded events


### User

_source line 3545 · 2026-05-22T08:08:19.265774+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交至 Review Director。

**核心判断：Overall 3.5（Borderline Conference）**

两个 Must-Fix：
1. 实验 setup（Section 7）位于结果之后，严重影响可读性，需前置
2. 仅 2 个 8B 开源模型支撑"framework"级 claim，需补充模型多样性或降低 claim 强度

五个 Should-Fix：entity-level construction 对 Xie et al. 的增量不清晰、9 节结构过碎片化、"framework" vs "empirical study" 定位模糊、观测性分析中混用因果语言、Related Work 过于压缩。

主要优势：统计严谨度出色（57 项检验完整枚举）、negative result 诚实呈现、correlation-selection gap 概念有迁移价值、47 页附录细节详尽。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 3546 · 2026-05-22T08:08:27.914943+00:00_

Reviewer 2 审稿已收到（Overall 3.5）。等待 Reviewer 1 提交后进入交叉分享环节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 262

## Round 262

6 recorded events


### User

_source line 3547 · 2026-05-22T08:09:34.254985+00:00_

[Reviewer 1 审稿意见]:

## 总体评分
**Overall**: 3.5 — Borderline Conference
**一句话总结**: 对结构化预测中 self-consistency 失败的诊断分析扎实且全面，"correlation-selection gap" 概念新颖，但可操作性有限——提出的 entity construction 修复方案效果微弱且不一致，理论贡献相对浅层。

## 官方维度打分（来自 ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 方法论总体严谨（bootstrap CI、Holm-Bonferroni 校正、power analysis），但 θ_crit=0.70 阈值为 post-hoc 拟合、部分相关性检验 underpowered、"binding constraint" 叙事在摘要/引言中过度简化 |
| Excitement | 3/5 | 研究问题重要且 under-studied，correlation-selection gap 概念新颖，但论文本质是 negative result + 诊断分析，prescriptive value 有限 |
| Reproducibility | 4/5 | 训练配置（Table 20）、prompt 模板（Appendix k）、数据集细节完整，承诺 release 代码，34 页附录覆盖详尽消融 |
| Reviewer Confidence | 4/5 | 完整阅读全部 47 页，包括所有附录中的证明和实验细节 |

## Must-Fix 问题（影响接收决定）

**N1** [critical] θ_crit=0.70 阈值缺乏 held-out 验证，有过拟合风险
- 具体位置：Section 6.3, Table 31, Figure 10
- 问题：θ_crit=0.70 是论文的核心发现之一（Section 9 反复引用），但该阈值是从仅 16 个配置中 post-hoc 拟合得到的。Table 31 显示所有 positive-gain 配置均满足 D < θ_crit，但作者自己承认 "the bound is loose because σ (signal alignment) is the bottleneck"（p6）。没有任何 held-out validation——既没有在新数据集上验证，也没有使用 leave-one-out cross-validation。16 个配置的样本量使得二分类阈值容易过拟合。
- 为什么影响接收：这是论文的核心理论贡献之一，如果阈值不稳健，Section 6 和 Section 9 的结论就不可靠。
- 建议修改方向：(1) 在 RE 和 SQL 的配置上验证阈值是否成立（而非仅在 NER 上拟合）；(2) 进行 leave-one-dataset-out cross-validation；(3) 报告阈值对小扰动的敏感性（e.g., θ∈[0.65, 0.75] 是否改变结论）。

**N2** [critical] "Binding constraint" 叙事与证据不完全匹配
- 具体位置：Abstract（"α→0, not degeneracy alone, is the binding constraint"）、Section 2 bullet 2、Section 4 标题 "Where Single-Selection Fails"
- 问题：摘要和 Section 2 将 degeneracy (α→0) 定位为 "the binding constraint"。但 Table 31 和 Appendix p.5 明确表明，即使在非退化实例中（non-degenerate instances），最好的信号也只恢复了 oracle gap 的 6.8%。这意味着 degeneracy 只是必要条件之一——signal alignment 才是真正的瓶颈（作者自己在 p6 承认 "σ (signal alignment) is the bottleneck"）。直到 Section 9 才出现这一 nuance，但摘要和引言的叙事给读者留下了 "degeneracy 是唯一/主要瓶颈" 的错误印象。
- 为什么影响接收：核心叙事如果与证据不一致，会削弱论文的可信度。Reviewer 和 reader 会首先读摘要和引言来理解 contribution，如果这里的表述 misleading，会影响对整篇论文的判断。
- 建议修改方向：修改摘要和 Section 2，明确说明 degeneracy 是 necessary condition（sets the ceiling）但 signal alignment 是 jointly binding 的——gap 是两者共同作用的结果，而非 degeneracy 单独决定。

**N3** [critical] Entity construction 作为 prescriptive contribution 证据不足
- 具体位置：Section 7.5, Table 2, Table 12, Table 62
- 问题：论文将 entity-level construction 作为主要的 prescriptive contribution（Section 7.5: "Entity-level construction improves on Few-NERD"），但存在三个问题：
  (a) 阈值 k 是 per-dataset 优化的（Table 62 显示 k 在不同数据集上最优值不同：Few-NERD 用 θ=2/N=0.25，SciERC 效果不同），实际部署时无法设定；
  (b) Holm-Bonferroni 全局校正（Table 12）显示，57 个统计检验中仅 LP selection 和少数 construction 测试在 family-wise 水平显著，大多数 construction 结果未通过多重比较校正；
  (c) CoNLL 上 construction 增益为 0 或负（Table 2: CoNLL shows "no gain: ε<0.20pp, construction"），Few-NERD 上增益主要来自 LP-weighted（+1.40pp）但其他信号不显著。
- 为什么影响接收：如果论文的唯一 prescriptive contribution 在多重校正后不显著、且在部分数据集上失效，论文就沦为纯粹的 negative result 分析——这本身有价值但削弱了 contribution 的完整性。
- 建议修改方向：(1) 诚实重新定位论文的 contribution——如果 prescriptive value 有限，就以 diagnostic framework + correlation-selection gap 概念为核心 contribution，降低 entity construction 的叙事权重；(2) 讨论如何在无标注数据时选择阈值 k 的策略；(3) 报告 entity construction 在多重校正后的结果并讨论其局限。

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] 理论贡献（Section 6）相对 lightweight
- 具体位置：Section 6, Proposition 1, Proposition 2 (Appendix p.1-p.2), Corollary 1
- 问题：Proposition 1 形式化了一个直观观察——退化实例无法通过选择改善（Part a 的证明仅一句话：所有 N 个样本相同 → MV 输出 = greedy 输出）。Proposition 2（MBR 连接）依赖 entity-wise independence 假设，作者承认仅"approximately"成立。Corollary 1 是简单的代数变换。这些作为 "Threshold Regime Analysis" 的理论基础稍显单薄——它们更多是对实证观察的形式化重述，而非提供独立的理论洞察。
- 建议：考虑是否需要将 Section 6 作为独立的 "Threshold Regime Analysis" 章节，或者可以合并到 Section 4 的分析中。如果保留，需要更清楚地说明理论的 added value beyond formalizing observations。

**W2** [warning] Power analysis 揭示部分关键检验可能 underpowered
- 具体位置：Table 58 (Appendix ab.3), 涉及 Section 7.3 和 Section 9 的多个 cross-dataset 相关性分析
- 问题：作者自己的 power analysis（Table 58）表明，在 n=23 的样本量下（cross-dataset degeneracy-LP correlation 的实际样本量），只有 ρ>0.5 的相关性才能在 80% power 下被检测到。但论文中多个关键相关性在 0.3-0.5 范围内（e.g., Table 6 中 temperature-robustness ρ, Section 7.3 中 cross-dataset transfer ρ）。这意味着 "非显著" 的结果（如 "degeneracy alone does not predict LP direction", Section 7.3）可能是 underpowered 导致的 Type II error，而非真正的 absence of effect。
- 建议：在讨论 non-significant 结果时，明确注明 power 限制。不要将 "未检测到显著相关" 等同于 "不存在相关"。

**W3** [warning] LP compression 分析可能混淆 compression 与 calibration
- 具体位置：Section m (Appendix), Figure 9, 以及 Section 2 bullet 4
- 问题：论文声称 LP 在 instance 内的 range 仅为 0.041 nats（Appendix m, Figure 9），将此解读为 "LP compression"——即 LP 丢失了区分不同质量输出的信息。但另一种解读是：模型本身对同一 input 的多个输出确实产出了相似质量的结果（即模型 well-calibrated），LP 的窄 range 准确反映了这一事实。论文没有充分区分 "LP 压缩了真实的质量差异" 和 "真实的质量差异本身就很小"。
- 建议：增加一个对照实验——例如，在 oracle headroom 高但 LP range 窄的实例子集上，检验是否存在 LP 确实遗漏了的质量差异（e.g., F1 variance within instance 高但 LP variance 低的情况）。

**W4** [warning] RE 和 SQL 扩展覆盖有限
- 具体位置：Section 8 (Related Work 中简要提及), Appendix o (RE), Appendix ae (SQL 评估协议)
- 问题：RE 扩展仅在 SciERC RE 上进行（单一数据集），SQL 扩展使用的是 Spider（与 NER 差异极大）。论文声称 "self-consistency fails across NER and RE"（Section 2），但 RE 的证据仅来自一个数据集。SQL 的 "extending" 更多是类比而非同一框架的直接应用（SQL parsing 和 NER extraction 的 failure modes 本质不同）。
- 建议：至少增加一个 RE 数据集（如 TACRED 或 DocRED）来验证 RE 的泛化性，或者诚实弱化 "across NER and RE" 的表述。

## 小问题（不影响接收）

- Figure 1 caption 声称 "diagnostic sequence, not causal chain"，但图的视觉设计（从左到右的箭头、sequential stages）暗示因果关系，建议调整图的视觉语言或更显著标注 "observational"
- Table 3（N=8）和 Table 4（N=8, 部分结果 N=16）使用不同 N 值，影响直接比较的便利性
- Section 2.2 定义了多个信号（VC, SI, FK, EM, LP）但主文中主要使用 LP，其他信号的分析大量依赖附录，主文中对 "为什么 LP 是最好的信号" 的直觉解释可以更充分
- 脚注 10（p5）提到排除 GPT-5.5 10.1% 的 parse failure，但未讨论这些 failure 是否与 correlation-selection gap 分析相关（parse failure 的实例可能 systematically bias 结果）
- Table 66 的 differentiation matrix 很有用，但放在最后一页，建议在 Section 8 中引用

## 主要优势

- **S1**: "Correlation-selection gap" 是一个定义清晰、证据充分的新概念——population-level ρ=0.45 + AUROC=0.82 vs. instance-level selection <1pp 的反差，通过 Table 3, Figure 2, Table 4 等多个角度验证，具有超越 NER 任务的潜在影响力
- **S2**: 实验覆盖异常全面——4 NER + RE + SQL, 2 主力模型 + 4B/14B/72B/GPT-5.5 消融, N∈{8,16,32,64}, T∈{0.5,0.7,1.0}, 34 页附录包含详尽的 robustness 和 ablation 分析
- **S3**: 统计方法论严谨——Holm-Bonferroni 多重比较校正（Table 12, 57 tests）、paired bootstrap p-values、power analysis（Table 58）、bootstrap 95% CIs（Table 11）。少见的审稿体验中看到如此完整的统计报告
- **S4**: 诚实的报告风格——不 oversell entity construction 的效果（Section 7.5 明确报告了 CoNLL 上 construction 无效），Table 12 的全局 Holm-Bonferroni 枚举提升了透明度
- **S5**: 研究问题填补了重要空白——self-consistency 在 reasoning 上广受关注但在 structured prediction 上的失败几乎无人系统分析，本文的诊断框架为后续 test-time compute scaling 研究提供了有价值的分析模板

## Questions for Authors
1. θ_crit=0.70 在不同模型 family（如 DeepSeek、Mistral）或不同 fine-tuning regime 下是否稳健？是否有 held-out 验证的计划？
2. 既然非退化实例的 oracle gap recovery 仅 6.8%（Table 31），degeneracy 是否真的是 "binding constraint"，还是 signal alignment 才是更根本的限制？
3. Entity construction 的阈值 k 在无标注验证数据的实际部署场景中如何选择？
4. GPT-5.5 的 10.1% parse failure 被排除出分析（footnote 10），这些 failure 实例是否可能 systematically bias correlation-selection gap 的估计？


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 3548 · 2026-05-22T08:10:19.718366+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "## 交叉分享：Reviewer 2 的完整审稿意见\n\n请逐条回应以下 Reviewer 2 的意见。对每一条使用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 2 的完整审稿意见：\n\n### Overall: 3.5 — Borderline Conference\n\n### Must-Fix 问题\n\n**N1** [critical] **实验 setup 位置反常，严重影响可读性**\n- Sections 3-6 已大量呈现实验结果（Table 1-2, Figure 1-4, Proposition 1），但实验设置（数据集、模型、训练细节）直到 Section 7 才给出。读者在 Section 3 看到\"Qwen3-8B fine-tuned, Few-NERD, N=8, seed=42\"时，尚不知道模型如何 fine-tune、数据集规模多大、LoRA 配置如何。Section 7 本身又混合了新结果（7.2-7.5），导致结果分散在 Sections 3-7 五个不同位置。\n- 建议：将 Section 7.1 前置到 Section 2 之后、结果之前；将 7.2-7.5 整合到对应的诊断阶段章节中。\n\n**N2** [critical] **模型多样性不足以支撑\"框架\"级别的 claim**\n- 仅测试 2 个开源 decoder-only 模型家族（Qwen3-8B, LLaMA-3.1-8B），均为 ~8B 参数。缺失：(a) 更大模型（70B+）；(b) encoder-based 或 encoder-decoder 模型；(c) 闭源 API 模型；(d) 专门为 NER fine-tune 的模型（如 GLiNER）。\n- 建议：降低 claim 强度（\"framework\" → \"empirical study\"），或补充至少 1 个差异化模型。\n\n### Should-Fix 问题\n\n**W1** Entity-level construction 新颖性不足，与 Xie et al. (2023) 的差异不够清晰（Section 6.1, Section 8）。\n\n**W2** 9 节结构过于碎片化——Section 3 和 Section 4 各仅半页，Section 8（Related Work）被压缩到 ~15 行，Section 9 空间不足。\n\n**W3** \"Diagnostic cascade\" 的贡献性质模糊——方法贡献还是分析贡献？论文将其包装为 \"framework\"（标题），但更接近一组分析步骤。\n\n**W4** 观测性分析中隐含因果推断——Section 2 声明 \"observational\" 但后续使用 \"binding constraint\"、\"limits exploitation\" 等因果语言。\n\n**W5** Abstract 中 \"reliably predict\" 用词过强——ρ=0.45 仅解释 ~20% 方差。\n\n**W6** Related Work（Section 8）覆盖不足——MBR for structured outputs、LLM calibration、Yao/Yun concurrent works 讨论不充分。\n\n### 小问题\n- M1: Table 1 \"2-seed\" vs 正文 \"3-seed\" 不一致\n- M2: Footnote 1（RE F1 confounded）但 Appendix 仍用 F1\n- M3: Figure 3 低 N 区间负值需 caption 解释\n- M4: Fleiss (1971) vs Soft Jaccard 关系未说明\n- M5: Appendix af（Anticipated Objections）给人防御性印象\n- M6: Responsible NLP Checklist 在 PDF 内（ARR checklist 也在 OpenReview form 中）\n\n### 格式合规：全部通过（页数、ACL style、匿名化、Limitations、Ethics、Checklist）\n\n### 缺失引用建议\n1. Entity aggregation 基础文献\n2. MBR for structured NLP 更广泛文献\n3. LLM calibration 综述\n\n---\n\n请对上述每条 Must-Fix、Should-Fix 和你认为重要的 Minor Issues 给出 [AGREE] 或 [REBUT] 回应。",
  "reviewer_id": "1",
  "project": "struct_self_consist_ie",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "## 交叉分享：Reviewer 2 的完整审稿意见\n\n请逐条回应以下 Reviewer 2 的意见。对每一条使用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 2 的完整审稿意见：\n\n### Overall: 3.5 — Borderline Conference\n\n### Must-Fix 问题\n\n**N1** [critical] **实验 setup 位置反常，严重影响可读性**\n- Sections 3-6 已大量呈现实验结果（Table 1-2, Figure 1-4, Proposition 1），但实验设置（数据集、模型、训练细节）直到 Section 7 才给出。读者在 Section 3 看到\"Qwen3-8B fine-tuned, Few-NERD, N=8, seed=42\"时，尚不知道模型如何 fine-tune、数据集规模多大、LoRA 配置如何。Section 7 本身又混合了新结果（7.2-7.5），导致结果分散在 Sections 3-7 五个不同位置。\n- 建议：将 Section 7.1 前置到 Section 2 之后、结果之前；将 7.2-7.5 整合到对应的诊断阶段章节中。\n\n**N2** [critical] **模型多样性不足以支撑\"框架\"级别的 claim**\n- 仅测试 2 个开源 decoder-only 模型家族（Qwen3-8B, LLaMA-3.1-8B），均为 ~8B 参数。缺失：(a) 更大模型（70B+）；(b) encoder-based 或 encoder-decoder 模型；(c) 闭源 API 模型；(d) 专门为 NER fine-tune 的模型（如 GLiNER）。\n- 建议：降低 claim 强度（\"framework\" → \"empirical study\"），或补充至少 1 个差异化模型。\n\n### Should-Fix 问题\n\n**W1** Entity-level construction 新颖性不足，与 Xie et al. (2023) 的差异不够清晰（Section 6.1, Section 8）。\n\n**W2** 9 节结构过于碎片化——Section 3 和 Section 4 各仅半页，Section 8（Related Work）被压缩到 ~15 行，Section 9 空间不足。\n\n**W3** \"Diagnostic cascade\" 的贡献性质模糊——方法贡献还是分析贡献？论文将其包装为 \"framework\"（标题），但更接近一组分析步骤。\n\n**W4** 观测性分析中隐含因果推断——Section 2 声明 \"observational\" 但后续使用 \"binding constraint\"、\"limits exploitation\" 等因果语言。\n\n**W5** Abstract 中 \"reliably predict\" 用词过强——ρ=0.45 仅解释 ~20% 方差。\n\n**W6** Related Work（Section 8）覆盖不足——MBR for structured outputs、LLM calibration、Yao/Yun concurrent works 讨论不充分。\n\n### 小问题\n- M1: Table 1 \"2-seed\" vs 正文 \"3-seed\" 不一致\n- M2: Footnote 1（RE F1 confounded）但 Appendix 仍用 F1\n- M3: Figure 3 低 N 区间负值需 caption 解释\n- M4: Fleiss (1971) vs Soft Jaccard 关系未说明\n- M5: Appendix af（Anticipated Objections）给人防御性印象\n- M6: Responsible NLP Checklist 在 PDF 内（ARR checklist 也在 OpenReview form 中）\n\n### 格式合规：全部通过（页数、ACL style、匿名化、Limitations、Ethics、Checklist）\n\n### 缺失引用建议\n1. Entity aggregation 基础文献\n2. MBR for structured NLP 更广泛文献\n3. LLM calibration 综述\n\n---\n\n请对上述每条 Must-Fix、Should-Fix 和你认为重要的 Minor Issues 给出 [AGREE] 或 [REBUT] 回应。",
    "reviewer_id": "1",
    "project": "struct_self_consist_ie",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 3549 · 2026-05-22T08:10:36.799442+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 17081
}
```

</details>

---


### Tool call

_source line 3550 · 2026-05-22T08:10:37.119358+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "text": "## 交叉分享：Reviewer 1 的完整审稿意见\n\n请逐条回应以下 Reviewer 1 的意见。对每一条使用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 1 的完整审稿意见：\n\n### Overall: 3.5 — Borderline Conference\n\n### Must-Fix 问题\n\n**N1** [critical] **θ_crit=0.70 阈值缺乏 held-out 验证，有过拟合风险**\n- θ_crit=0.70 是从仅 16 个配置中 post-hoc 拟合得到的。Table 31 显示所有 positive-gain 配置均满足 D < θ_crit，但没有 held-out validation（新数据集验证或 leave-one-out CV）。16 个配置的样本量使得二分类阈值容易过拟合。\n- 建议：在 RE 和 SQL 配置上验证阈值；进行 leave-one-dataset-out CV；报告阈值对 θ∈[0.65, 0.75] 的敏感性。\n\n**N2** [critical] **\"Binding constraint\" 叙事与证据不完全匹配**\n- 摘要和 Section 2 将 α→0 定位为 \"the binding constraint\"。但 Table 31 和 Appendix p.5 表明，即使在非退化实例中，最好的信号只恢复了 oracle gap 的 6.8%。Signal alignment 才是真正的瓶颈，但摘要/引言给读者留下 \"degeneracy 是唯一/主要瓶颈\" 的错误印象。\n- 建议：修改摘要和 Section 2，明确 degeneracy 是 necessary condition 但 signal alignment 是 jointly binding 的。\n\n**N3** [critical] **Entity construction 作为 prescriptive contribution 证据不足**\n- (a) 阈值 k 是 per-dataset 优化的，实际部署时无法设定；(b) Holm-Bonferroni 全局校正后大多数 construction 结果未通过多重比较校正；(c) CoNLL 上 construction 增益为 0 或负。\n- 建议：诚实重新定位 contribution，降低 entity construction 的叙事权重；讨论无标注数据时阈值选择策略。\n\n### Should-Fix 问题\n\n**W1** 理论贡献（Section 6）相对 lightweight——Proposition 1 形式化了直观观察（退化实例无法改善），Proposition 2 依赖 entity-wise independence 假设。\n\n**W2** Power analysis 揭示部分关键检验可能 underpowered——n=23 样本量下只有 ρ>0.5 的相关性才能被检测到，多个关键相关性在 0.3-0.5 范围。\n\n**W3** LP compression 分析可能混淆 compression 与 calibration——论文未区分 \"LP 压缩了真实质量差异\" 和 \"真实质量差异本身就很小\"。\n\n**W4** RE 和 SQL 扩展覆盖有限——RE 仅在 SciERC RE 上进行，SQL 更多是类比而非同一框架的直接应用。\n\n### 小问题\n- Figure 1 视觉设计暗示因果关系但 caption 声称 \"not causal chain\"\n- Table 3 和 Table 4 使用不同 N 值影响对比\n- 主文中对 \"为什么 LP 是最好的信号\" 的直觉解释不充分\n- GPT-5.5 10.1% parse failure 排除可能 systematically bias 结果\n- Table 66 differentiation matrix 放在最后一页，建议在 Section 8 引用\n\n### Questions for Authors\n1. θ_crit=0.70 在不同模型 family 下是否稳健？\n2. 非退化实例 oracle gap recovery 仅 6.8%——degeneracy 真的是 \"binding constraint\" 吗？\n3. Entity construction 阈值在无标注数据场景下如何选择？\n4. GPT-5.5 parse failure 排除是否 bias 结果？\n\n---\n\n请对上述每条 Must-Fix、Should-Fix 和你认为重要的 Minor Issues 给出 [AGREE] 或 [REBUT] 回应。",
  "reviewer_id": "2",
  "project": "struct_self_consist_ie",
  "round_number": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "text": "## 交叉分享：Reviewer 1 的完整审稿意见\n\n请逐条回应以下 Reviewer 1 的意见。对每一条使用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 1 的完整审稿意见：\n\n### Overall: 3.5 — Borderline Conference\n\n### Must-Fix 问题\n\n**N1** [critical] **θ_crit=0.70 阈值缺乏 held-out 验证，有过拟合风险**\n- θ_crit=0.70 是从仅 16 个配置中 post-hoc 拟合得到的。Table 31 显示所有 positive-gain 配置均满足 D < θ_crit，但没有 held-out validation（新数据集验证或 leave-one-out CV）。16 个配置的样本量使得二分类阈值容易过拟合。\n- 建议：在 RE 和 SQL 配置上验证阈值；进行 leave-one-dataset-out CV；报告阈值对 θ∈[0.65, 0.75] 的敏感性。\n\n**N2** [critical] **\"Binding constraint\" 叙事与证据不完全匹配**\n- 摘要和 Section 2 将 α→0 定位为 \"the binding constraint\"。但 Table 31 和 Appendix p.5 表明，即使在非退化实例中，最好的信号只恢复了 oracle gap 的 6.8%。Signal alignment 才是真正的瓶颈，但摘要/引言给读者留下 \"degeneracy 是唯一/主要瓶颈\" 的错误印象。\n- 建议：修改摘要和 Section 2，明确 degeneracy 是 necessary condition 但 signal alignment 是 jointly binding 的。\n\n**N3** [critical] **Entity construction 作为 prescriptive contribution 证据不足**\n- (a) 阈值 k 是 per-dataset 优化的，实际部署时无法设定；(b) Holm-Bonferroni 全局校正后大多数 construction 结果未通过多重比较校正；(c) CoNLL 上 construction 增益为 0 或负。\n- 建议：诚实重新定位 contribution，降低 entity construction 的叙事权重；讨论无标注数据时阈值选择策略。\n\n### Should-Fix 问题\n\n**W1** 理论贡献（Section 6）相对 lightweight——Proposition 1 形式化了直观观察（退化实例无法改善），Proposition 2 依赖 entity-wise independence 假设。\n\n**W2** Power analysis 揭示部分关键检验可能 underpowered——n=23 样本量下只有 ρ>0.5 的相关性才能被检测到，多个关键相关性在 0.3-0.5 范围。\n\n**W3** LP compression 分析可能混淆 compression 与 calibration——论文未区分 \"LP 压缩了真实质量差异\" 和 \"真实质量差异本身就很小\"。\n\n**W4** RE 和 SQL 扩展覆盖有限——RE 仅在 SciERC RE 上进行，SQL 更多是类比而非同一框架的直接应用。\n\n### 小问题\n- Figure 1 视觉设计暗示因果关系但 caption 声称 \"not causal chain\"\n- Table 3 和 Table 4 使用不同 N 值影响对比\n- 主文中对 \"为什么 LP 是最好的信号\" 的直觉解释不充分\n- GPT-5.5 10.1% parse failure 排除可能 systematically bias 结果\n- Table 66 differentiation matrix 放在最后一页，建议在 Section 8 引用\n\n### Questions for Authors\n1. θ_crit=0.70 在不同模型 family 下是否稳健？\n2. 非退化实例 oracle gap recovery 仅 6.8%——degeneracy 真的是 \"binding constraint\" 吗？\n3. Entity construction 阈值在无标注数据场景下如何选择？\n4. GPT-5.5 parse failure 排除是否 bias 结果？\n\n---\n\n请对上述每条 Must-Fix、Should-Fix 和你认为重要的 Minor Issues 给出 [AGREE] 或 [REBUT] 回应。",
    "reviewer_id": "2",
    "project": "struct_self_consist_ie",
    "round_number": "1"
  }
}
```

</details>

---


### Tool result

_source line 3551 · 2026-05-22T08:10:39.143313+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 2023
}
```

</details>

---


### Assistant

_source line 3552 · 2026-05-22T08:10:43.081662+00:00_

交叉分享已发出，等待两位 Reviewer 的 [AGREE]/[REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 263

## Round 263

2 recorded events


### User

_source line 3553 · 2026-05-22T08:10:45.970707+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

核心判断：**Overall 3.5（Borderline Conference）**。论文对 self-consistency 在 NER 上失败的诊断分析非常扎实，"correlation-selection gap" 概念新颖且证据充分，实验覆盖和统计方法论在同类工作中属于上乘。但三个关键问题拉低评分：(1) θ_crit=0.70 阈值是 post-hoc 拟合且缺乏 held-out 验证；(2) 摘要/引言中 "degeneracy 是 binding constraint" 的叙事与 body 中的证据（非退化实例 oracle gap recovery 仅 6.8%）存在张力；(3) entity construction 作为 prescriptive contribution 在多重校正后效果不稳健。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 3554 · 2026-05-22T08:10:53.863604+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 264

## Round 264

2 recorded events


### User

_source line 3555 · 2026-05-22T08:16:59.505867+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 交叉回应：逐条回应 Reviewer 1 意见

---

### Must-Fix 问题

**[REBUT] R1-N1: θ_crit=0.70 阈值缺乏 held-out 验证，有过拟合风险**

R1 将 θ_crit=0.70 描述为"从 16 个配置中 post-hoc 拟合"，这一表述不准确。θ_crit 来源于 Corollary 1（p.31）的理论推导——给定 significance threshold δ，degeneracy rate 的下界 D_min = 1 − δ/(G_nd · σ_md)，代入经验估计值后得到 0.70。16 个配置是**验证**该理论 bound 的，不是拟合来源。Table 31 显示所有 positive-gain 配置满足 D < θ_crit，actual/bound ratio 为 3–12%，bound 是 loose 的（因为 σ 是真正瓶颈），这恰恰说明阈值是保守的而非过拟合。

但 R1 关于 **held-out 验证**的建议有一定道理：论文在 4 个 NER 数据集 + RE 上验证，但没有做 leave-one-dataset-out CV 或阈值敏感性扫描（如 θ∈[0.65,0.75]）。不过，Table 22（p.27）提供了 LP compression threshold ε 的 sensitivity sweep（ε=0 到 0.20），Table 35（p.33）报告了 sample count 对 degeneracy 的影响，这些间接证据表明框架结论对超参数不脆弱。总体而言，θ_crit 的理论基础是稳固的，但在新 domain 上的经验验证可以更充分。

**严重程度评估：Should-Fix，非 Must-Fix。** 理论推导是 sound 的，16-config 验证是对 bound 的检验而非拟合，R1 的"过拟合"定性过重。

---

**[REBUT] R1-N2: "Binding constraint" 叙事与证据不完全匹配**

R1 声称"摘要和 Section 2 将 α→0 定位为 the binding constraint"但实际证据显示 signal alignment 才是瓶颈。这恰恰**误读了论文的立场**——论文的观点正是 R1 自己指出的结论。

具体证据：
- p.2 原文明确说："α→0, **not degeneracy alone**, is the binding constraint"——即 α→0（selection alignment 接近零）是 binding constraint，而非 degeneracy 单独。
- Abstract 列举了三个失败阶段："degeneracy (12–68%) reduces the candidate pool, LP compression flattens score differences, and **near-zero selection alignment (α→0)** prevents even well-correlated signals from separating the top candidate"——三者并列，degeneracy 仅是第一环。
- Section 4 标题 "Where Single-Selection Fails" 明确将 gap 分解为两层：structural（degeneracy）+ empirical（α→0）。
- Table 31 的 6.8% oracle gap recovery 恰恰是论文 Section 6 自己报告的——"the best signal recovers only 6.8% of the non-degenerate oracle gap on average"（p.31），论文从未声称 degeneracy 是唯一瓶颈。

R1 的批评与论文实际叙事一致而非矛盾。摘要和引言的措辞已经清楚地传达了 degeneracy 是 necessary condition、signal alignment 是 jointly binding 的结构。如果 R1 的建议是"更显式地说明 signal alignment 的瓶颈地位"，这属于 minor 措辞优化，不构成 Must-Fix。

**严重程度评估：Minor，非 Must-Fix。** 论文已经明确表述了 R1 所期望的结论。

---

**[AGREE] R1-N3: Entity construction 作为 prescriptive contribution 证据不足**

R1 的三个子问题均有据可查：

(a) **阈值 k per-dataset 优化**：Table 62（p.43）确认 k 在每个 dataset 上分别 sweep（k∈{2,...,8}），最优 k 因 dataset 而异。论文在 Section 7.5 未讨论无标注数据时如何选择 k，这确实限制了实际可部署性。

(b) **Holm-Bonferroni 校正后显著性**：Table 12（p.25）报告全局校正 k=57 后 p_adj=0.055（Few-NERD entity construction），仅两个 peripheral tests 达到显著性。Table 61（p.43）的 per-family Holm 校正也只有 Few-NERD 的 LP-weighted construction 通过（p=0.055，边缘）。这确实削弱了 prescriptive 贡献的统计基础。

(c) **CoNLL 增益为 0 或负**：Table 62 确认 CoNLL 最优 construction 增益为 +0.20pp（non-significant），Section 7.5 明确说 "CoNLL shows no gain (+0.20pp), consistent with high degeneracy"。

不过需补充：论文的核心贡献是 **diagnostic framework**（四阶段 cascade），entity construction 是 prescriptive 探索（Section 7.5 占约 0.5 页）。论文自身也承认了局限性——"Gains require both low degeneracy and sufficient oracle headroom"（p.6）。R1 的建议"降低 entity construction 的叙事权重"合理，但这不应影响对 diagnostic framework 本身的评价。

**严重程度评估：同意 Should-Fix 级别。** 论文应更诚实地限定 construction 的适用范围，但非 critical。

---

### Should-Fix 问题

**[REBUT] R1-W1: 理论贡献 lightweight**

论文的 primary contribution 是 **empirical diagnostic framework**，不是理论创新。Proposition 1（degenerate instances 无法通过 MV 改善）和 Proposition 2（entity-wise independence 下的 construction bound）服务于 grounding the cascade，不是独立的理论贡献。Section 6 的定位很清楚："Our analysis is observational: we characterize statistical associations"（p.2）。

Proposition 1 形式化了直觉这一事实，恰恰说明 diagnostic cascade 的第一环有理论基础——而非所有诊断性工作都需要深度理论。类比：医学诊断 pipeline 的价值在于系统性分解，而非每个检验步骤都要有 novel theorem。

**评估：不构成显著弱点。** Empirical contribution 类论文的理论部分 lightweight 是正常的。

---

**[AGREE] R1-W2: Power analysis 部分关键检验可能 underpowered**

Table 58（p.42）的 post-hoc power analysis 显示 n=23（cross-dataset configurations）时，只有 ρ>0.5 的相关性才有 80% power。论文自身承认 "80% power requires n≥65 for ρ=0.3 and n=47 for ρ=0.5"（p.42）。多个关键相关性（如 per-type degeneracy-LP 相关，Table 51 p.39 中 ρ≈0.3–0.5）可能落在 underpowered 区间。

这是一个真实的统计局限，但论文已经透明地报告了 power analysis 结果，且主要发现（如 degeneracy 预测 LP direction，Section 7.3）使用了更大样本量的 within-dataset 分析。

---

**[REBUT] R1-W3: LP compression 分析可能混淆 compression 与 calibration**

论文已提供了区分二者的证据：
- **Constrained vs. free-form decoding 对比**（Table 33, p.32–33）：在 SciERC 上比较了 constrained decoding（XGrammar）和 free-form decoding 下的 LP 分布。Free-form decoding 下 LP 分布显著更分散（LP range 从 0.041 增大），但 selection gain 仍然 negligible，说明 compression 是 constrained decoding 的产物，而非"真实质量差异本身就小"。
- **CDF 分析**（Figure 9, p.23）：within-instance LP range 的 CDF 确认 compression 是 pervasive（中位数 0.041 nats），且与 constrained decoding 的 token-level 约束直接相关。
- **Temperature ablation**（Table 45, p.37）：提高 temperature 增大 LP variance 但不改善 selection，进一步支持"compression 是 structural 而非质量差异小"。

R1 的 confound 假设已被 Table 33 的 constrained vs. free-form 对比和 temperature ablation 部分 addressed。残存的问题是 free-form decoding 下 parsing failure rate 高（10.1%），可能 bias free-form 结果。

**评估：论文已部分 address，不构成独立的 Should-Fix。**

---

**[AGREE] R1-W4: RE 和 SQL 扩展覆盖有限**

事实准确。RE 仅在 SciERC RE 上测试（Section o, p.29），Table 29–30 报告了 RE selection 结果但仅 N=8、T=1.0，且 RE 的 zero-F1 instance 率高达 40%（p.29）。SQL 仅作为类比讨论（Section 9 最后一段提到 "extensibility to... SQL parsing"），没有同一框架的直接实验。

论文在 Limitations（p.9）承认 "RE extension covers a single SciERC benchmark"，但这确实限制了 generalizability 声明。补充 1–2 个 RE benchmark（如 TACRED、DocRED）能显著增强 prescriptive 部分的说服力。

---

### 小问题

**[AGREE] Figure 1 视觉暗示因果但 caption 声称 non-causal**：Figure 1 使用箭头连接三个阶段，视觉上确实暗示因果链，虽然 caption 注明 "diagnostic sequence, not causal chain"。建议改为虚线箭头或显式标注 "correlational"。

**[AGREE] Table 3 和 Table 4 使用不同 N**：Table 3（p.7）使用 N=8, primary seed=42；Table 4 使用不同配置。论文在 caption 中注明了配置差异，但并列对比时确实容易误导。

**[REBUT] GPT-5.5 10.1% parse failure 排除可能 bias 结果**：论文已在 Section af（p.45–46）的 O4 中直接 address 这一问题："Qwen2.5-72B zero-shot exhibits the same gap; LP drops without fine-tuning, structural signals generalize (VC p=0.116 on Few-NERD), and degeneracy is model-family-dependent rather than scale-dependent."此外，Table 2（p.5）中 GPT-5.5 的 cross-model ensemble 结果包含在内，parse failure 样本被排除在所有指标计算中（p.10 checklist C3），处理方式一致。这不太可能引入 systematic bias。

**[AGREE] Table 66 placement**：differentiation matrix 放在最后一页（p.46），在主文 Section 8 引用时读者不易找到。建议在主文提供简表或显式 forward reference。

---

### 对 R1 Questions for Authors 的补充评估

1. **θ_crit 在不同 model family 下是否稳健？** 论文 Table 36（p.34）报告了 cross-seed signal ranking stability（Kendall's W），Table 44（p.36）跨 frontier model families 分析。Degeneracy 是 model-family-dependent（Qwen2.5: 31.7–46.2% vs. Qwen3-3B: 13.0%，p.35），θ_crit 的具体数值确实可能需要 per-family calibration，但 Corollary 1 的 functional form 是 model-agnostic 的。

2. **6.8% recovery 问题**：如上 REBUT N2 所述，论文自身已明确这一事实，且将 signal alignment 而非 degeneracy 定位为 binding constraint。

3. **Entity construction 阈值在无标注场景下如何选择？** 这是一个合理的 open question，论文确实未讨论。但 Table 62 中 k=θ·2/N=0.25 在 Few-NERD 上的 robustness（±0.04pp）提示 moderate threshold 即可。

4. **GPT-5.5 parse failure bias？** 如上 REBUT 所述，已被 address。

---

### 总结

R1 的审稿总体严谨，但三个 Must-Fix 的严重程度评估偏高：
- **N1**（θ_crit）：理论基础 sound，R1 误将 validation 描述为 fitting。降级为 Should-Fix。
- **N2**（binding constraint 叙事）：R1 的批评与论文实际叙事一致而非矛盾。降级为 Minor。
- **N3**（entity construction）：同意证据不足，但论文已自我限定，且 construction 非核心贡献。维持 Should-Fix。

R1 的 Should-Fix 问题中，W2（power）和 W4（RE/SQL coverage）是真实局限；W1（theory lightweight）和 W3（compression confound）已被论文 address。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 3556 · 2026-05-22T08:17:14.004573+00:00_

Reviewer 2 的交叉回应已收到。等待 Reviewer 1 对 Reviewer 2 意见的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 265

## Round 265

2 recorded events


### User

_source line 3557 · 2026-05-22T08:17:20.380878+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交给 Review Director。

核心判断：R1 的三个 Must-Fix 中，N1（θ_crit 过拟合）和 N2（binding constraint 叙事矛盾）的严重程度被高估——θ_crit 有理论推导支撑而非 post-hoc fitting，binding constraint 叙事与论文实际立场一致而非矛盾。N3（entity construction 证据不足）同意但降级为 Should-Fix，因为 construction 非核心贡献。W2（power analysis）和 W4（RE/SQL 覆盖）是真实局限，W1 和 W3 已被论文 address。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 3558 · 2026-05-22T08:17:26.400413+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 266

## Round 266

10 recorded events


### User

_source line 3559 · 2026-05-22T08:18:31.649916+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 意见的逐条回应

---

### Must-Fix 问题

**[REBUT] R2-N1: 实验 setup 位置反常，严重影响可读性**

部分不同意严重程度判定。论文采用 diagnostic cascade 结构——Sections 3–6 各回答一个诊断问题，每个 section 构成自洽的 question→evidence→finding 单元。读者进入 Section 3 时并非毫无背景：Section 2.3（Evaluation）已提供关键参数（Spearman ρ 和 AUROC 计算方式、数据集名称及规模如 SciERC n=529、CoNLL n=2,756、gold-filtering 标准），Section 3 首段即交代了 "Qwen3-8B fine-tuned, Few-NERD, N=8, seed=42"。

但我同意完整训练细节（LoRA 配置、LLaMA Factory、constrained decoding 等）到 Section 7.1 才出现，确实增加了认知负担。**建议在 Section 2 末尾增加 1–2 段实验概览**，将 Section 7.1 保留为完整参考。

R2 建议将 7.2–7.5 拆散到 Sections 3–6——我**反对**。7.2–7.5 是 cascade 完成后的综合 cross-dataset/robustness/prescriptive 分析，逻辑上是全局评估而非某个诊断阶段的组成部分，拆散破坏叙事完整性。

**结论：这是 presentation 问题，建议降级为 Should-Fix。不影响技术贡献和实验有效性。**

---

**[REBUT] R2-N2: 模型多样性不足以支撑"框架"级别的 claim**

R2 声称论文"仅测试 2 个开源 decoder-only 模型家族，均为 ~8B"——**这个描述与论文实际内容不符**。论文覆盖的模型包括：

| 模型 | 类型 | 规模 | 位置 |
|------|------|------|------|
| Qwen3-8B | 开源, fine-tuned | 8B | 主实验 (Table 1–4, Sections 3–7) |
| LLaMA-3.1-8B | 开源, fine-tuned | 8B | 主实验 (Table 1, 3, 4) |
| Qwen3-4B, Qwen3-14B | 开源, fine-tuned | 4B, 14B | Appendix (Table 40, Section 6.2) |
| LLaMA-3.2-3B | 开源, fine-tuned | 3B | Appendix o (cross-family) |
| Qwen2.5-72B | 开源, zero-shot | 72B | Section 6.2, Table 40, Appendix o |
| GPT-5.5 | **闭源 API**, zero-shot | — | Section 7.2 (Table 9, WNUT-17 分析) |
| DeBERTa-v3 | **Encoder**, verifier | — | Appendix h.2 |

这是 **4 个模型家族、3B–72B 参数跨度、fine-tuned 与 zero-shot 两种 regime、开源与闭源、decoder-only 与 encoder** 的全覆盖。R2 列出的四项缺失中：(a) 70B+ → 已有 Qwen2.5-72B；(b) encoder → 已有 DeBERTa-v3；(c) 闭源 API → 已有 GPT-5.5。(d) GLiNER 等专用 NER 模型不使用 autoregressive generation，不产生 N 个可比较的候选输出，不在 SC 框架的适用范围内。

关于"framework"→"empirical study"的降级建议：论文提供了形式化 4-stage diagnostic cascade、Proposition 1（degeneracy decomposition 的封闭形式）、Corollary 1（degeneracy threshold）、以及可复用的评估协议（Appendix ae），这些超出纯 empirical study 范畴。"Diagnostic Framework" 这一定位是准确的。

**我同意的部分**：主正文对 GPT-5.5 和 72B 结果的讨论偏简略，建议在 Section 7 或 Section 9 中更显著地 highlight 跨规模/跨类型的一致性发现。

---

### Should-Fix 问题

**[AGREE] R2-W1: Entity-level construction 与 Xie et al. (2023) 的差异不清晰**

同意。Section 6.1 的 entity-level construction 在技术上与 Xie et al. (2023) structure-conditional MBR 相关。论文的增量贡献——将 entity construction 嵌入 diagnostic cascade 并提供 Proposition 1 的形式化 decomposition——在 Section 6.1 和 Section 8 中阐述不够清晰。建议在 Section 6.1 开头用 1–2 句明确与 Xie et al. 的关系和本文的差异化贡献。

---

**[REBUT] R2-W2: 9 节结构过于碎片化**

不同意。Sections 3–6 各回答一个独立的诊断层级问题：
- Section 3: per-sample self-verification 能力（ESJ AUROC=0.512，与 chance 不可区分）
- Section 4: cross-sample selection 的结构性瓶颈（degeneracy 下无信号可改善选择）
- Section 5: 9 种方法的综合评估（Table 2）
- Section 6: entity construction + scaling + formal decomposition

合并 Sections 3–4 会混淆 per-sample self-verification 和 cross-sample selection 两个不同分析层面。Section 3 用半页精确回答了一个关键问题——这种简洁是优点而非缺陷。

Section 8（Related Work）的压缩我部分同意是问题（见 W6 回应），但在 8 页限制下优先分配空间给实验证据是合理的取舍，且 Appendix ae 提供了 4 篇相关工作的详细 differentiation matrix（Table 66）。

---

**[AGREE] R2-W3: "Diagnostic cascade" 贡献性质模糊**

部分同意。论文应在 Section 1 contributions 列表中更明确地标注：这是一个 **diagnostic/analysis methodology 贡献**（提供可复用的诊断流程 + 形式化分析工具），而非新的 aggregation algorithm。标题 "Diagnostic Framework" 本身是准确的，但正文偶尔将 diagnostic 发现与方法创新的边界模糊化。建议在 contributions 中显式区分 "(1) diagnostic methodology, (2) formal characterization (Proposition 1), (3) empirical findings"。

---

**[REBUT] R2-W4: 观测性分析中隐含因果推断**

不同意。Section 2.1 明确声明 "Our analysis is observational: we characterize statistical associations between agreement signals and output quality without claiming causal mechanisms." 

- **"binding constraint"**：指统计意义上的 tightest bound——在所有考察因素中，degeneracy 与 ceiling gap 的关联最强（Figure 10: 16 个配置全部落在 bound 内，Table 31: 最佳 selection 仅恢复 6.8% 的 non-degenerate oracle gap）。这是识别 limiting factor 的标准观测分析用语。
- **"limits exploitation"**：描述可观测的经验事实——degeneracy 高时所有策略增益趋近于零。

论文在 Limitations 中进一步承认 "we have not performed controlled interventions (e.g., artificially varying degeneracy while holding other factors constant), and the cascade stages interact in ways that resist decomposition into independent causal effects"。作者对观测–因果边界有明确认知。

---

**[REBUT] R2-W5: Abstract "reliably predict" 用词过强（ρ=0.45）**

R2 的论证存在两个问题：

1. **统计方法误用**：将 Spearman ρ 平方得到"解释 20% 方差"是对 Pearson R² 概念的误用。Spearman ρ 衡量单调秩关联，ρ²≈0.20 不能解读为"仅解释 20% 方差"。
2. **选择性忽略关键指标**：Abstract 同时报告 **AUROC=0.82**（Table 3），这是 binary quality discrimination 的标准指标。0.82 在 NLP quality estimation 文献中表现强劲。Table 3 进一步显示跨模型设置下 AUROC 达 0.684–0.749，跨数据集最高 0.82。

综合 ρ up to 0.45 + AUROC 0.82，"reliably predict" 在 quality estimation 文献标准下站得住。但为求严谨，可微调措辞为 "effectively discriminate" 或 "meaningfully predict"。这是措辞调整，不是方法论缺陷。

---

**[AGREE] R2-W6: Related Work 覆盖不足**

同意。Section 8 被过度压缩（~15 行），对以下方向讨论不足：(1) MBR for structured NLP outputs（Eikema et al., 2025 已引用但讨论不充分），(2) LLM calibration（Guo et al., 2017 通过 Appendix c 的 ECE 结果隐式涉及，但 Section 8 未显式讨论），(3) concurrent works on SC failure modes。建议从 Appendix ae（Table 66, differentiation matrix）中提炼关键对比点到 Section 8 主文。

---

### Minor Issues

**[AGREE] R2-M1: Table 1 "2-seed" vs 正文 "3-seed" 不一致**

确认存在。Table 1 caption 明确写 "2-seed mean±σ"，Table 4 caption 写 "3-seed means"，Checklist（page 10）写 "We report multi-seed results (3 seeds)"。即使不同实验确实使用了不同 seed 数量，也需要在 Section 7.1 中明确说明原因，消除读者困惑。

**[AGREE] R2-M2: Footnote 1 vs Appendix RE F1 不一致**

Footnote 1 声称 RE F1 confounded（"the majority of zero-F1 RE instances reflect upstream NER mismatches"），但附录仍用 F1 报告 RE 结果。这需要统一——要么附录改用解耦指标，要么明确说明在什么条件下 F1 仍然可用。

**[AGREE] R2-M3: Figure 3 低 N 负值需 caption 解释**

Figure 3 在 Few-NERD 低 N 区间出现 MV ΔF1 约 -2.7 至 -0.7 pp 的负值。这与 Proposition 1 的 degeneracy decomposition 直接相关（degenerate instances 在 MV 下无法改善，且 structural signal collapse 可能导致劣化），caption 应简要解释成因。

**[REBUT] R2-M4: Fleiss (1971) vs Soft Jaccard 关系未说明**

不需要额外说明"关系"。Section 2.2 将 FK（Fleiss' kappa）归类为 surface agreement 信号，SJ（Soft Jaccard）归类为 structural agreement 信号，两者计算方式、衡量维度完全不同（FK 衡量 inter-rater reliability，SJ 衡量 token-level set overlap）。它们是互补的信号维度，不存在需要解释的从属关系。

**[REBUT] R2-M5: Appendix af（Anticipated Objections）给人防御性印象**

不同意。Anticipated Objections 是高质量实证论文的常见做法。Appendix af 对 12 个预期质疑逐条提供了具体实验证据——O1 引用 Table 32/Appendix p.5 验证泛化性，O5 引用 Table 3 论证结果可重复性，O7 引用 Proposition 2/§6.1 回应 MBR 关系，O11 引用 Table 66/Appendix ae 回应 reproducibility。每条回应都有实证支撑，反映的是严谨和透明，而非防御性。

**[AGREE] R2-M6: Responsible NLP Checklist 位置**

ARR checklist 主要在 OpenReview submission form 中填写。PDF 中包含 checklist 不违反规则但占据附录空间。如果页数紧张，可考虑精简或移除 PDF 中的副本。

---

### 缺失引用建议

**Entity aggregation 基础文献**：部分同意，核心 MBR 文献已引用（Eikema and Aziz, 2022; Kumar et al., 2004），但可补充 entity-level aggregation 的更广泛背景。
**MBR for structured NLP**：同意，应扩展 Eikema et al. (2025) 之外的相关讨论。
**LLM calibration 综述**：同意，应在 Section 8 显式讨论 calibration 文献。

---

### 总结

R2 的整体评分 3.5（Borderline Conference）偏低。两个 Must-Fix 问题中：
- **N1**（实验 setup 位置）是 presentation 问题而非技术缺陷，且论文在 Section 2.3 已提供了关键实验参数，应降级为 Should-Fix。
- **N2**（模型多样性）的前提描述与论文实际内容不符——论文覆盖了 4 个模型家族、3B–72B 跨度、开源/闭源、fine-tuned/zero-shot、decoder/encoder，远超 R2 声称的"仅 2 个 8B 模型"。

R2 的 Should-Fix 问题中 W1、W3、W6 是合理的改进建议；W2 和 W4 我不同意。W5 存在 Spearman ρ² 的统计方法误用。

如果将 N1 降级为 Should-Fix、纠正 N2 的事实错误，该论文没有 critical-level 的方法论或实验缺陷，评分应高于 3.5。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 3560 · 2026-05-22T08:19:17.150240+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 3561 · 2026-05-22T08:19:17.402091+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-22T08:00:26.337110+00:00\", \"completed_at\": \"2026-05-22T08:04:43.428505+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 1-2\", \"message\": \"前 2 页为连续纯文本（Abstract + Introduction），第一个 display item（Figure 1）直到第 3 页才出现。审稿人需翻过 2 页纯文字才看到视觉锚点，首页锚定效应偏弱。建议考虑将 Figure 1 提前或在 Introduction 中加入一个简要的 teaser figure。\"}, {\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"Title / Author / Abstract 排版整洁，符合 ACL 匿名投稿模板规范。\\\"Anonymous ACL submission\\\" 标注正确。\"}, {\"severity\": \"info\", \"dimension\": \"page 3\", \"message\": \"Figure 1 作为第一个 display item，传达核心 message（correlation-selection gap 的诊断流程概览），caption 自包含且详细，信息传达清晰。与 Title-Abstract 讲的是同一个故事。\"}, {\"severity\": \"info\", \"dimension\": \"page 3\", \"message\": \"Figure 1 使用红-绿色对比（High F1 绿色 vs Low F1 红色框），对红绿色盲用户可能不够友好。建议改用蓝-橙或 Okabe-Ito 色板。\"}, {\"severity\": \"info\", \"dimension\": \"page 4\", \"message\": \"Table 1 + Figure 2 同页出现，密度合理。Figure 2 bar chart 颜色区分度良好（蓝色系 + 灰色虚线），caption 自包含。\"}, {\"severity\": \"info\", \"dimension\": \"page 4\", \"message\": \"Table 1 使用 booktabs 风格，最优值加粗标注，精度统一。排版规范。\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Table 2 跨全宽（figure*），9 个 method categories 信息密集但列对齐良好。字号略小但可读。\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Figure 3 线图使用 3 种颜色（蓝/橙/绿）+ 不同标记形状区分 3 个数据集，色盲友好度可接受。Y 轴标签 \\\"MV ΔF1 (pp)\\\" 清晰。\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 4 散点图 + Table 3 + Table 4 同页，密度较高但布局合理。Figure 4 caption 自包含。\"}, {\"severity\": \"warning\", \"dimension\": \"page 8-9\", \"message\": \"连续 2 页纯文本（Section 8 Related Work + Section 9 Discussion and Conclusion + Limitations + Ethics Statement + Checklist）。其中 Discussion/Limitations/Ethics 为论文末尾固定内容，节奏上可接受，但 Related Work（§8）与 Discussion（§9）之间完全无 display item 穿插，审稿人阅读体验略显单调。\"}, {\"severity\": \"info\", \"dimension\": \"page 9\", \"message\": 
…[truncated 2749 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 3562 · 2026-05-22T08:19:17.452763+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 3563 · 2026-05-22T08:19:17.653873+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 3564 · 2026-05-22T08:20:03.409716+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "struct_self_consist_ie",
  "issues_yaml": "issues:\n- id: R1-N1\n  summary: \"θ_crit=0.70 阈值缺乏 held-out 验证\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 33\n  last_seen_round: 33\n  mentions:\n    - round: 33\n      reviewers: [1]\n      note: \"R1 认为 Must-Fix（post-hoc fitting 风险）；R2 反驳称有 Corollary 1 理论支撑，降级为 Should-Fix。共识：理论基础 sound 但缺 held-out validation 和 sensitivity sweep。\"\n  action_items:\n    - round: 33\n      action: \"在 RE/SQL 配置上验证 θ_crit；报告 θ∈[0.65,0.75] 敏感性\"\n      assigned_to: research\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R1-N3\n  summary: \"Entity construction 作为 prescriptive contribution 证据不足\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 33\n  last_seen_round: 33\n  mentions:\n    - round: 33\n      reviewers: [1, 2]\n      note: \"双方共识：(a) 阈值 k per-dataset 优化无部署策略；(b) Holm-Bonferroni 全局校正后多数 construction 结果不显著；(c) CoNLL 无增益。R2 同意但认为 construction 非核心贡献，降级为 Should-Fix。\"\n  action_items:\n    - round: 33\n      action: \"降低 entity construction 叙事权重；讨论无标注数据时的阈值选择策略\"\n      assigned_to: research\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R2-W1\n  summary: \"Entity-level construction 与 Xie et al. (2023) 差异不清晰\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 33\n  last_seen_round: 33\n  mentions:\n    - round: 33\n      reviewers: [1, 2]\n      note: \"双方 AGREE。Section 6.1 和 Section 8 对 Xie et al. (2023) entity voting 的增量贡献阐述不充分。\"\n  action_items:\n    - round: 33\n      action: \"在 Section 6.1 开头增加与 Xie et al. (2023) 的显式对比\"\n      assigned_to: research\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R2-W3\n  summary: \"Framework vs empirical study 定位模糊\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 33\n  last_seen_round: 33\n  mentions:\n    - round: 33\n      reviewers: [1, 2]\n      note: \"R2 提出，R1 部分同意。标题用 'Diagnostic Framework' 但实际更接近分析方法论贡献。建议在 contributions 中显式区分 diagnostic methodology / formal characterization / empirical findings。\"\n  action_items:\n    - round: 33\n      action: \"在 Section 1 contributions 列表中明确区分贡献类型\"\n      assigned_to: research\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R2-W6\n  summary: \"Related Work (Section 8) 过于压缩\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 33\n  last_seen_round: 33\n  mentions:\n    - round: 33\n      reviewers: [1, 2]\n      note: \"双方 AGREE。~15 行 Related Work 对横跨 SC/MBR/NER aggregation/uncertainty estimation 的论文不足。MBR for structured NLP、LLM calibration、Yao/Yun concurrent works 讨论不充分。\"\n  action_items:\n    - round: 33\n      action: \"扩展 Related Work 至 20-25 行，从 Appendix ae (Table 66) 提炼关键对比点\"\n      assigned_to: research\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R2-N1\n  summary: \"实验 setup (Section 7.1) 位于结果之后影响可读性\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 33\n  last_seen_round: 33\n  mentions:\n    - round: 33\n      reviewers: [2]\n      note: \"R2 认为 Must-Fix；R1 反驳称 Section 2.3 已提供关键参数，降级为 Should-Fix。共识：在 Section 2 末尾增加 1-2 段实验概览。\"\n  action_items:\n    - round: 33\n      action: \"在 Section 2 末尾增加实验概览段落\"\n      assigned_to: research\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R1-W2\n  summary: \"部分关键检验 underpowered (n=23)\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 33\n  last_seen_round: 33\n  mentions:\n    - round: 33\n      reviewers: [1, 2]\n      note: \"双方 AGREE。Cross-dataset degeneracy-LP correlation (n=23) 只能检测 ρ>0.5，多个关键相关性在 0.3-0.5 范围。论文已透明报告 power analysis。\"\n  action_items:\n    - round: 33\n      action: \"在讨论 non-significant 结果时明确注明 power 限制\"\n      assigned_to: research\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R1-W4\n  summary: \"RE 和 SQL 扩展覆盖有限\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 33\n  last_seen_round: 33\n  mentions:\n    - round: 33\n      reviewers: [1, 2]\n      note: \"双方 AGREE。RE 仅 SciERC RE (n=397)，SQL 仅类比讨论。建议补充 RE 数据集或弱化泛化声明。\"\n  action_items:\n    - round: 33\n      action: \"补充至少 1 个 RE 数据集或弱化 'across NER and RE' 表述\"\n      assigned_to: research\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R2-M1\n  summary: \"Table 1 '2-seed' vs 正文 '3-seed' 不一致\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 33\n  last_seen_round: 33\n  mentions:\n    - round: 33\n      reviewers: [1, 2]\n      note: \"双方 AGREE。需在 Section 7.1 中说明不同实验使用的 seed 数量差异。\"\n  action_items:\n    - round: 33\n      action: \"统一 seed 数量描述或在 Section 7.1 说明原因\"\n      assigned_to: research\n      status: open\n  resolution: \"\"\n  resolution_round: null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "issues_yaml": "issues:\n- id: R1-N1\n  summary: \"θ_crit=0.70 阈值缺乏 held-out 验证\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 33\n  last_seen_round: 33\n  mentions:\n    - round: 33\n      reviewers: [1]\n      note: \"R1 认为 Must-Fix（post-hoc fitting 风险）；R2 反驳称有 Corollary 1 理论支撑，降级为 Should-Fix。共识：理论基础 sound 但缺 held-out validation 和 sensitivity sweep。\"\n  action_items:\n    - round: 33\n      action: \"在 RE/SQL 配置上验证 θ_crit；报告 θ∈[0.65,0.75] 敏感性\"\n      assigned_to: research\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R1-N3\n  summary: \"Entity construction 作为 prescriptive contribution 证据不足\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 33\n  last_seen_round: 33\n  mentions:\n    - round: 33\n      reviewers: [1, 2]\n      note: \"双方共识：(a) 阈值 k per-dataset 优化无部署策略；(b) Holm-Bonferroni 全局校正后多数 construction 结果不显著；(c) CoNLL 无增益。R2 同意但认为 construction 非核心贡献，降级为 Should-Fix。\"\n  action_items:\n    - round: 33\n      action: \"降低 entity construction 叙事权重；讨论无标注数据时的阈值选择策略\"\n      assigned_to: research\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R2-W1\n  summary: \"Entity-level construction 与 Xie et al. (2023) 差异不清晰\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 33\n  last_seen_round: 33\n  mentions:\n    - round: 33\n      reviewers: [1, 2]\n      note: \"双方 AGREE。Section 6.1 和 Section 8 对 Xie et al. (2023) entity voting 的增量贡献阐述不充分。\"\n  action_items:\n    - round: 33\n      action: \"在 Section 6.1 开头增加与 Xie et al. (2023) 的显式对比\"\n      assigned_to: research\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R2-W3\n  summary: \"Framework vs empirical study 定位模糊\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 33\n  last_seen_round: 33\n  mentions:\n    - round: 33\n      reviewers: [1, 2]\n      note: \"R2 提出，R1 部分同意。标题用 'Diagnostic Framework' 但实际更接近分析方法论贡献。建议在 contributions 中显式区分 diagnostic methodology / formal characterization / empirical findings。\"\n  action_items:\n    - round: 33\n      action: \"在 Section 1 contributions 列表中明确区分贡献类型\"\n      assigned_to: research\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R2-W6\n  summary: \"Related Work (Section 8) 过于压缩\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 33\n  last_seen_round: 33\n  mentions:\n    - round: 33\n      reviewers: [1, 2]\n      note: \"双方 AGREE。~15 行 Related Work 对横跨 SC/MBR/NER aggregation/uncertainty estimation 的论文不足。MBR for structured NLP、LLM calibration、Yao/Yun concurrent works 讨论不充分。\"\n  action_items:\n    - round: 33\n      action: \"扩展 Related Work 至 20-25 行，从 Appendix ae (Table 66) 提炼关键对比点\"\n      assigned_to: research\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R2-N1\n  summary: \"实验 setup (Section 7.1) 位于结果之后影响可读性\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 33\n  last_seen_round: 33\n  mentions:\n    - round: 33\n      reviewers: [2]\n      note: \"R2 认为 Must-Fix；R1 反驳称 Section 2.3 已提供关键参数，降级为 Should-Fix。共识：在 Section 2 末尾增加 1-2 段实验概览。\"\n  action_items:\n    - round: 33\n      action: \"在 Section 2 末尾增加实验概览段落\"\n      assigned_to: research\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R1-W2\n  summary: \"部分关键检验 underpowered (n=23)\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 33\n  last_seen_round: 33\n  mentions:\n    - round: 33\n      reviewers: [1, 2]\n      note: \"双方 AGREE。Cross-dataset degeneracy-LP correlation (n=23) 只能检测 ρ>0.5，多个关键相关性在 0.3-0.5 范围。论文已透明报告 power analysis。\"\n  action_items:\n    - round: 33\n      action: \"在讨论 non-significant 结果时明确注明 power 限制\"\n      assigned_to: research\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R1-W4\n  summary: \"RE 和 SQL 扩展覆盖有限\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 33\n  last_seen_round: 33\n  mentions:\n    - round: 33\n      reviewers: [1, 2]\n      note: \"双方 AGREE。RE 仅 SciERC RE (n=397)，SQL 仅类比讨论。建议补充 RE 数据集或弱化泛化声明。\"\n  action_items:\n    - round: 33\n      action: \"补充至少 1 个 RE 数据集或弱化 'across NER and RE' 表述\"\n      assigned_to: research\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R2-M1\n  summary: \"Table 1 '2-seed' vs 正文 '3-seed' 不一致\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 33\n  last_seen_round: 33\n  mentions:\n    - round: 33\n      reviewers: [1, 2]\n      note: \"双方 AGREE。需在 Section 7.1 中说明不同实验使用的 seed 数量差异。\"\n  action_items:\n    - round: 33\n      action: \"统一 seed 数量描述或在 Section 7.1 说明原因\"\n      assigned_to: research\n      status: open\n  resolution: \"\"\n  resolution_round: null"
  }
}
```

</details>

---


### Tool result

_source line 3565 · 2026-05-22T08:20:03.410349+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml\", \"bytes\": 4620}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 3566 · 2026-05-22T08:21:56.006435+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 审稿报告：Characterizing the Capability Ceiling of Self-Consistency: A Diagnostic Framework for Test-Time Aggregation in NER\n\n**项目**: struct_self_consist_ie\n**目标 Venue**: EMNLP 2026 (ARR May 2026 cycle)\n**审稿轮次**: Round 33 (fresh)\n**Reviewer**: R1 (方法严谨性+实验设计), R2 (新颖性+完整性+写作质量)\n**日期**: 2026-05-22\n\n---\n\n## Summary\n\n本文系统性研究 test-time compute scaling（self-consistency）在 NER 任务上的失败原因。作者提出\"correlation-selection gap\"概念——QE 信号在 population level 能有效预测输出质量（Spearman ρ 达 0.45，AUROC 达 0.82），但 instance-level 选择几乎无效（多数数据集 <1 pp）。通过四阶段诊断级联（degeneracy → oracle headroom → LP compression → selection alignment α→0）定位失败机制。Entity-level construction 在 Few-NERD 上获得 +1.40 pp（Holm p_adj=0.006），但在其他数据集上效果有限或无效。实验覆盖 4 个 NER 数据集、4 个模型家族（3B–72B + GPT-5.5）、RE 和 SQL 扩展。\n\n---\n\n## Strengths\n\n**S1. 重要且诚实的 negative result。** 系统性证明 self-consistency 在 NER 上失败并诊断失败原因，填补了 test-time scaling 文献在结构化预测方面的空白。论文坦诚报告 entity construction 在 CoNLL 无效、SciERC 增益微弱，诚实度在当前 NLP 文献中突出。[R1, R2 共识]\n\n**S2. 出色的统计严谨性。** 57 项统计检验完整枚举（Table 12 Holm-Bonferroni）、paired bootstrap CI、permutation test、TOST 等效性检验、post-hoc power analysis（Table 58）。这种透明度在同类工作中罕见，直接回应了 ARR guidelines 中 R1（inappropriate statistics）和 R5（missing significance）的关切。[R1, R2 共识]\n\n**S3. Correlation-selection gap 概念清晰且有迁移价值。** \"QE 信号 population-level 有效但 instance-level 失效\"的解耦不仅适用于 NER，对任何 set-valued structured output 的 test-time scaling 都有启示。Figure 1 直观传达核心洞见。[R1, R2 共识]\n\n**S4. 实验覆盖全面。** 9 种聚合方法、5 种 QE 信号、temperature/N-scaling/cross-model/cross-dataset 鲁棒性分析、RE 和 SQL 扩展、4 个模型家族（Qwen3-8B/4B/14B、LLaMA-3.1-8B、Qwen2.5-72B zero-shot、GPT-5.5 zero-shot）、DeBERTa-v3 encoder verifier、47 页附录。[R1, R2 共识]\n\n**S5. MBR 理论联系。** Proposition 1 和 Proposition 2 将 entity-level 聚合与 MBR decoding 理论框架对接，为实验发现提供形式化基础。[R1, R2 共识]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n无。经交叉讨论，R1 和 R2 各自提出的 Must-Fix 问题均被对方提供了有效反驳或降级至 Should-Fix：\n- R1-N1（θ_crit 过拟合）：R2 指出 θ_crit 来自 Corollary 1 理论推导而非 post-hoc fitting，16 个配置是验证而非拟合来源。→ **降级为 Should-Fix**\n- R1-N2（binding constraint 叙事矛盾）：R2 指出论文原文明确写 \"α→0, not degeneracy alone, is the binding constraint\"，R1 的批评基于对摘要的部分误读。→ **降级为 Minor**\n- R1-N3（entity construction 证据不足）：双方 AGREE 证据有限，但 R2 指出 construction 非核心贡献（占 ~0.5 页），论文已自我限定。→ **维持 Should-Fix**\n- R2-N1（实验 setup 位置）：R1 指出 Section 2.3 已提供关键参数，这是 presentation 问题非技术缺陷。→ **降级为 Should-Fix**\n- R2-N2（模型多样性不足）：R1 提供详细反驳——论文实际覆盖 4 个模型家族、3B–72B 跨度、开源/闭源、fine-tuned/zero-shot、decoder/encoder（DeBERTa）。R2 的\"仅 2 个 8B 模型\"描述不准确。→ **降级为 Should-Fix（主文应更显著 highlight 跨规模结果）**\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF1. Entity construction 证据有限，需降低叙事权重。** [R1-N3, R2-W1 | 双方共识]\n- 阈值 k per-dataset 优化，无部署策略\n- Holm-Bonferroni 全局校正后 p_adj=0.055（边缘），多数 construction 结果不显著\n- CoNLL 无增益，SciERC 增益微弱\n- 与 Xie et al. (2023) entity voting 的差异阐述不充分\n- **建议**：将 construction 定位为探索性结果而非核心贡献；增加与 Xie et al. 的显式对比\n\n**SF2. \"Diagnostic Framework\" 定位需澄清。** [R2-W3 | 双方部分同意]\n- 标题包装为 \"framework\" 但更接近分析方法论贡献\n- 每一步需要 task-specific 判断，其他研究者难以直接\"运行\"该 cascade\n- **建议**：在 Section 1 contributions 中显式区分 (1) diagnostic methodology, (2) formal characterization, (3) empirical findings\n\n**SF3. Related Work (Section 8) 过于压缩。** [R2-W6 | 双方共识]\n- ~15 行对横跨 SC/MBR/NER aggregation/uncertainty estimation 的论文不足\n- MBR for structured NLP、LLM calibration、Yao et al. (2026)/Yun et al. (2025) concurrent works 讨论不充分\n- **建议**：扩展至 20–25 行，从 Appendix ae (Table 66) 提炼关键对比点\n\n**SF4. 实验 setup 位置可优化。** [R2-N1 | R1 降级]\n- 完整训练细节（LoRA 配置、constrained decoding 等）到 Section 7.1 才出现\n- **建议**：在 Section 2 末尾增加 1–2 段实验概览，保留 Section 7.1 为完整参考\n\n**SF5. θ_crit=0.70 阈值需 sensitivity 分析。** [R1-N1 | R2 降级]\n- 理论基础（Corollary 1）sound，但缺 held-out validation 和 sensitivity sweep\n- **建议**：报告 θ∈[0.65, 0.75] 的敏感性；在 RE/SQL 配置上验证\n\n**SF6. RE 和 SQL 扩展覆盖有限。** [R1-W4, R2 | 双方共识]\n- RE 仅 SciERC RE (n=397, 40% zero-F1)，SQL 仅类比讨论\n- **建议**：补充 1 个 RE 数据集或弱化 \"across NER and RE\" 泛化声明\n\n**SF7. 模型多样性在主文中呈现不足。** [R2-N2 | R1 反驳后降级]\n- 论文实际覆盖广泛（4 家族、3B–72B、GPT-5.5、DeBERTa），但主文对 72B/GPT-5.5/DeBERTa 的讨论偏简略，多数结果在附录中\n- **建议**：在 Section 7 或 Section 9 更显著地 highlight 跨规模/跨类型的一致性发现\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **Correlation-selection gap 是一个有价值的新概念**，对社区理解 self-consistency 在结构化预测上的局限性有实质贡献\n2. **统计方法论在同类工作中属上乘**，57 项检验完整枚举的透明度值得肯定\n3. **Entity construction 作为 prescriptive contribution 证据有限**，但论文已诚实自我限定\n4. **Related Work 需要扩展**\n5. **RE/SQL 扩展覆盖不足以支撑泛化声明**\n6. **论文对 negative results 的呈现诚实且充分**\n\n## Reviewer Divergence [REBUT]\n\n1. **θ_crit 的性质**：R1 认为 post-hoc fitting 风险高（Must-Fix），R2 反驳有理论推导支撑（Should-Fix）。**Director 判定：Should-Fix**——Corollary 1 提供了理论基础，但缺 sensitivity 分析。\n2. **\"Binding constraint\" 叙事**：R1 认为摘要 misleading（Must-Fix），R2 指出原文已明确 \"α→0, not degeneracy alone\"（Minor）。**Director 判定：Minor**——论文叙事基本准确，R1 的批评部分基于误读，但摘要措辞可微调使 signal alignment 的瓶颈地位更突出。\n3. **模型多样性**：R2 认为\"仅 2 个 8B 模型\"（Must-Fix），R1 提供详细反驳列出 4 个家族 + 完整跨度。**Director 判定：Should-Fix**——覆盖存在但主文呈现不足。\n4. **9 节结构**：R2 认为过于碎片化，R1 认为各节各回答一个独立诊断问题，简洁是优点。**Director 判定：不构成显著弱点**——诊断级联结构有其逻辑。\n5. **\"reliably predict\" 措辞**：R2 认为 ρ=0.45 不够\"reliable\"，R1 反驳 ρ²≠variance explained（Spearman vs Pearson）且 AUROC=0.82 支撑该表述。**Director 判定：Minor 措辞调整**——\"effectively predict\" 或 \"meaningfully predict\" 更安全。\n\n---\n\n## Questions（需作者澄清）\n\n1. θ_crit=0.70 在 θ∈[0.65, 0.75] 范围内是否改变 Table 31 的结论？\n2. Entity construction 阈值 k 在无标注验证数据的实际场景中如何选择？\n3. GPT-5.5 的 10.1% parse failure 排除后，是否系统性偏移了 correlation-selection gap 估计？\n4. 论文是否计划补充更多 RE 数据集以支撑泛化声明？\n\n---\n\n## Missing References\n\n1. **Entity-level aggregation 先驱工作**：Xie et al. (2023) entity voting 需在 Section 6.1 做显式对比\n2. **MBR for structured NLP 更广泛文献**：Eikema et al. (2025) 之外的结构化输出 MBR 应用\n3. **LLM calibration 综述**：论文使用 ECE（Appendix c）但未在 Related Work 讨论 calibration 领域\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未请求（项目未配置 external_review.paperreview_ai.enabled）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（0 critical / 3 warning / 27 info）。\n\n**Warnings:**\n1. **Pages 1–2 纯文本**：前 2 页为 Abstract + Introduction 连续文字，Figure 1 直到 page 3 才出现。建议考虑将 Figure 1 提前或加入 teaser figure。\n2. **Pages 8–9 纯文本**：Related Work + Discussion + Limitations + Ethics 连续无 display item，阅读体验略单调。\n3. **Page 24 大面积空白**：Appendix 文本末页仅 ~25% 填充，page break 控制不佳。\n\n**Positive:**\n- 主文 8 display items / 8 pages，密度合理\n- 所有 float 位置合理，无漂移\n- 公式渲染全部正确\n- 无 margin 溢出\n- 符合 EMNLP 2026 8 页限制\n- Figure 1 色彩对比存在轻微色盲友好性问题（红-绿），建议改用 Okabe-Ito 色板\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.5 (Borderline Conference)**\n\n**置信度: 4/5**\n\n**理由：**\n\n这是一篇扎实的诊断分析工作。\"Correlation-selection gap\"概念清晰且有迁移价值，统计严谨度在 NLP 论文中属上乘，negative results 的诚实呈现值得肯定。实验覆盖面广（4 个 NER 数据集、4 个模型家族、3B–72B 跨度、9 种方法）。\n\n但论文的核心局限在于 prescriptive contribution 薄弱：entity-level construction 仅在 Few-NERD 上有明确正向效果（+1.40 pp, Holm p_adj=0.006），CoNLL 无增益，SciERC 增益微弱且未通过多重校正。这使论文本质上是一篇 negative result + 诊断分析工作，方法论增量有限。Related Work 过于压缩（~15 行），\"framework\"定位与实际分析贡献之间存在张力。\n\n**无 Must-Fix 级别的技术缺陷**——经交叉讨论，所有 critical 问题均被降级或解决。7 个 Should-Fix 问题（entity construction 定位、framework 澄清、Related Work 扩展、实验 setup 前置、θ_crit sensitivity、RE/SQL 覆盖、模型多样性呈现）均可在修改周期内解决。\n\n当前状态下 Findings 是安全着陆点。若能解决 SF1（entity construction 重新定位）、SF3（Related Work 扩展）和 SF7（主文 highlight 跨规模结果），可提升至 Conference 水平。\n\n---\n\n## Detailed Comments\n\n### Section 1 (Introduction)\n- \"α→0, not degeneracy alone, is the binding constraint\" 措辞基本准确但可更精确——建议改为 \"near-zero selection alignment (α→0), jointly with degeneracy, constitutes the binding constraint\"\n- Contributions 列表应显式区分 diagnostic methodology / formal characterization / empirical findings 三类贡献\n\n### Section 2 (Diagnostic Framework)\n- 建议在 Section 2 末尾增加 1–2 段实验概览（数据集、模型、N、T 的概要）\n- \"capability ceiling\" 定义清晰，但与 \"correlation-selection gap\" 的关系可更显式说明\n\n### Section 3 (Self-Verification)\n- ESJ AUROC=0.512 是重要的 negative finding，呈现简洁有效\n- Hidden-state probe 的 LODO transfer 下降（0.56–0.67）是关键发现，支持 dataset-specific 结论\n\n### Section 4 (Single-Signal Selection)\n- Table 1 和 Figure 2 有效传达 gap\n- \"Diagnostic cascade\" 四阶段逻辑清晰，但阶段间交互（R²<0）应在主文更显著呈现\n\n### Section 5 (Adaptive Methods)\n- Table 2 的 9 方法综述是有价值的参考\n- Cross-model ensemble (+0.42 pp) 作为唯一 unconditional positive result，可在讨论中更突出\n\n### Section 6 (Theory)\n- Proposition 1 形式化了直观观察——作为诊断工具有价值但不构成独立理论贡献\n- θ_crit=0.70 需 sensitivity 分析（θ∈[0.65, 0.75]）\n\n### Section 7 (Experiments)\n- 7.1 Experimental Setup 应前置或在 Section 2 提供概览\n- 7.3 Few-NERD cross-dataset contrast 是论文亮点，LP selection +1.39 pp (p<0.001) 是最强正向结果\n- 7.5 Prescriptive Results 应降低叙事权重，明确为探索性结果\n\n### Section 8 (Related Work)\n- 需要从 ~15 行扩展至 20–25 行\n- 补充 MBR for structured NLP、LLM calibration 讨论\n- 将 Yao/Yun concurrent works 的讨论从 Introduction 深化到 Related Work\n\n### Section 9 (Discussion)\n- 过于简短（约 5 行），建议扩展讨论 practical implications 和 future directions\n\n### Limitations\n- 覆盖面广且诚实，篇幅适中，符合 EMNLP 2026 规范\n\n### Appendix\n- 47 页附录详尽程度在同类工作中罕见，统计枚举透明度出色\n- Table 66 (differentiation matrix) 应在主文 Section 8 中引用\n- Appendix af (Anticipated Objections) 内容有用但可能给 reviewer 留下防御性印象",
  "project": "struct_self_consist_ie",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5 - Borderline Conference",
  "review_chat_id": "oc_3897c2857f11615119e277e820eae311"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# 审稿报告：Characterizing the Capability Ceiling of Self-Consistency: A Diagnostic Framework for Test-Time Aggregation in NER\n\n**项目**: struct_self_consist_ie\n**目标 Venue**: EMNLP 2026 (ARR May 2026 cycle)\n**审稿轮次**: Round 33 (fresh)\n**Reviewer**: R1 (方法严谨性+实验设计), R2 (新颖性+完整性+写作质量)\n**日期**: 2026-05-22\n\n---\n\n## Summary\n\n本文系统性研究 test-time compute scaling（self-consistency）在 NER 任务上的失败原因。作者提出\"correlation-selection gap\"概念——QE 信号在 population level 能有效预测输出质量（Spearman ρ 达 0.45，AUROC 达 0.82），但 instance-level 选择几乎无效（多数数据集 <1 pp）。通过四阶段诊断级联（degeneracy → oracle headroom → LP compression → selection alignment α→0）定位失败机制。Entity-level construction 在 Few-NERD 上获得 +1.40 pp（Holm p_adj=0.006），但在其他数据集上效果有限或无效。实验覆盖 4 个 NER 数据集、4 个模型家族（3B–72B + GPT-5.5）、RE 和 SQL 扩展。\n\n---\n\n## Strengths\n\n**S1. 重要且诚实的 negative result。** 系统性证明 self-consistency 在 NER 上失败并诊断失败原因，填补了 test-time scaling 文献在结构化预测方面的空白。论文坦诚报告 entity construction 在 CoNLL 无效、SciERC 增益微弱，诚实度在当前 NLP 文献中突出。[R1, R2 共识]\n\n**S2. 出色的统计严谨性。** 57 项统计检验完整枚举（Table 12 Holm-Bonferroni）、paired bootstrap CI、permutation test、TOST 等效性检验、post-hoc power analysis（Table 58）。这种透明度在同类工作中罕见，直接回应了 ARR guidelines 中 R1（inappropriate statistics）和 R5（missing significance）的关切。[R1, R2 共识]\n\n**S3. Correlation-selection gap 概念清晰且有迁移价值。** \"QE 信号 population-level 有效但 instance-level 失效\"的解耦不仅适用于 NER，对任何 set-valued structured output 的 test-time scaling 都有启示。Figure 1 直观传达核心洞见。[R1, R2 共识]\n\n**S4. 实验覆盖全面。** 9 种聚合方法、5 种 QE 信号、temperature/N-scaling/cross-model/cross-dataset 鲁棒性分析、RE 和 SQL 扩展、4 个模型家族（Qwen3-8B/4B/14B、LLaMA-3.1-8B、Qwen2.5-72B zero-shot、GPT-5.5 zero-shot）、DeBERTa-v3 encoder verifier、47 页附录。[R1, R2 共识]\n\n**S5. MBR 理论联系。** Proposition 1 和 Proposition 2 将 entity-level 聚合与 MBR decoding 理论框架对接，为实验发现提供形式化基础。[R1, R2 共识]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n无。经交叉讨论，R1 和 R2 各自提出的 Must-Fix 问题均被对方提供了有效反驳或降级至 Should-Fix：\n- R1-N1（θ_crit 过拟合）：R2 指出 θ_crit 来自 Corollary 1 理论推导而非 post-hoc fitting，16 个配置是验证而非拟合来源。→ **降级为 Should-Fix**\n- R1-N2（binding constraint 叙事矛盾）：R2 指出论文原文明确写 \"α→0, not degeneracy alone, is the binding constraint\"，R1 的批评基于对摘要的部分误读。→ **降级为 Minor**\n- R1-N3（entity construction 证据不足）：双方 AGREE 证据有限，但 R2 指出 construction 非核心贡献（占 ~0.5 页），论文已自我限定。→ **维持 Should-Fix**\n- R2-N1（实验 setup 位置）：R1 指出 Section 2.3 已提供关键参数，这是 presentation 问题非技术缺陷。→ **降级为 Should-Fix**\n- R2-N2（模型多样性不足）：R1 提供详细反驳——论文实际覆盖 4 个模型家族、3B–72B 跨度、开源/闭源、fine-tuned/zero-shot、decoder/encoder（DeBERTa）。R2 的\"仅 2 个 8B 模型\"描述不准确。→ **降级为 Should-Fix（主文应更显著 highlight 跨规模结果）**\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF1. Entity construction 证据有限，需降低叙事权重。** [R1-N3, R2-W1 | 双方共识]\n- 阈值 k per-dataset 优化，无部署策略\n- Holm-Bonferroni 全局校正后 p_adj=0.055（边缘），多数 construction 结果不显著\n- CoNLL 无增益，SciERC 增益微弱\n- 与 Xie et al. (2023) entity voting 的差异阐述不充分\n- **建议**：将 construction 定位为探索性结果而非核心贡献；增加与 Xie et al. 的显式对比\n\n**SF2. \"Diagnostic Framework\" 定位需澄清。** [R2-W3 | 双方部分同意]\n- 标题包装为 \"framework\" 但更接近分析方法论贡献\n- 每一步需要 task-specific 判断，其他研究者难以直接\"运行\"该 cascade\n- **建议**：在 Section 1 contributions 中显式区分 (1) diagnostic methodology, (2) formal characterization, (3) empirical findings\n\n**SF3. Related Work (Section 8) 过于压缩。** [R2-W6 | 双方共识]\n- ~15 行对横跨 SC/MBR/NER aggregation/uncertainty estimation 的论文不足\n- MBR for structured NLP、LLM calibration、Yao et al. (2026)/Yun et al. (2025) concurrent works 讨论不充分\n- **建议**：扩展至 20–25 行，从 Appendix ae (Table 66) 提炼关键对比点\n\n**SF4. 实验 setup 位置可优化。** [R2-N1 | R1 降级]\n- 完整训练细节（LoRA 配置、constrained decoding 等）到 Section 7.1 才出现\n- **建议**：在 Section 2 末尾增加 1–2 段实验概览，保留 Section 7.1 为完整参考\n\n**SF5. θ_crit=0.70 阈值需 sensitivity 分析。** [R1-N1 | R2 降级]\n- 理论基础（Corollary 1）sound，但缺 held-out validation 和 sensitivity sweep\n- **建议**：报告 θ∈[0.65, 0.75] 的敏感性；在 RE/SQL 配置上验证\n\n**SF6. RE 和 SQL 扩展覆盖有限。** [R1-W4, R2 | 双方共识]\n- RE 仅 SciERC RE (n=397, 40% zero-F1)，SQL 仅类比讨论\n- **建议**：补充 1 个 RE 数据集或弱化 \"across NER and RE\" 泛化声明\n\n**SF7. 模型多样性在主文中呈现不足。** [R2-N2 | R1 反驳后降级]\n- 论文实际覆盖广泛（4 家族、3B–72B、GPT-5.5、DeBERTa），但主文对 72B/GPT-5.5/DeBERTa 的讨论偏简略，多数结果在附录中\n- **建议**：在 Section 7 或 Section 9 更显著地 highlight 跨规模/跨类型的一致性发现\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **Correlation-selection gap 是一个有价值的新概念**，对社区理解 self-consistency 在结构化预测上的局限性有实质贡献\n2. **统计方法论在同类工作中属上乘**，57 项检验完整枚举的透明度值得肯定\n3. **Entity construction 作为 prescriptive contribution 证据有限**，但论文已诚实自我限定\n4. **Related Work 需要扩展**\n5. **RE/SQL 扩展覆盖不足以支撑泛化声明**\n6. **论文对 negative results 的呈现诚实且充分**\n\n## Reviewer Divergence [REBUT]\n\n1. **θ_crit 的性质**：R1 认为 post-hoc fitting 风险高（Must-Fix），R2 反驳有理论推导支撑（Should-Fix）。**Director 判定：Should-Fix**——Corollary 1 提供了理论基础，但缺 sensitivity 分析。\n2. **\"Binding constraint\" 叙事**：R1 认为摘要 misleading（Must-Fix），R2 指出原文已明确 \"α→0, not degeneracy alone\"（Minor）。**Director 判定：Minor**——论文叙事基本准确，R1 的批评部分基于误读，但摘要措辞可微调使 signal alignment 的瓶颈地位更突出。\n3. **模型多样性**：R2 认为\"仅 2 个 8B 模型\"（Must-Fix），R1 提供详细反驳列出 4 个家族 + 完整跨度。**Director 判定：Should-Fix**——覆盖存在但主文呈现不足。\n4. **9 节结构**：R2 认为过于碎片化，R1 认为各节各回答一个独立诊断问题，简洁是优点。**Director 判定：不构成显著弱点**——诊断级联结构有其逻辑。\n5. **\"reliably predict\" 措辞**：R2 认为 ρ=0.45 不够\"reliable\"，R1 反驳 ρ²≠variance explained（Spearman vs Pearson）且 AUROC=0.82 支撑该表述。**Director 判定：Minor 措辞调整**——\"effectively predict\" 或 \"meaningfully predict\" 更安全。\n\n---\n\n## Questions（需作者澄清）\n\n1. θ_crit=0.70 在 θ∈[0.65, 0.75] 范围内是否改变 Table 31 的结论？\n2. Entity construction 阈值 k 在无标注验证数据的实际场景中如何选择？\n3. GPT-5.5 的 10.1% parse failure 排除后，是否系统性偏移了 correlation-selection gap 估计？\n4. 论文是否计划补充更多 RE 数据集以支撑泛化声明？\n\n---\n\n## Missing References\n\n1. **Entity-level aggregation 先驱工作**：Xie et al. (2023) entity voting 需在 Section 6.1 做显式对比\n2. **MBR for structured NLP 更广泛文献**：Eikema et al. (2025) 之外的结构化输出 MBR 应用\n3. **LLM calibration 综述**：论文使用 ECE（Appendix c）但未在 Related Work 讨论 calibration 领域\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未请求（项目未配置 external_review.paperreview_ai.enabled）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（0 critical / 3 warning / 27 info）。\n\n**Warnings:**\n1. **Pages 1–2 纯文本**：前 2 页为 Abstract + Introduction 连续文字，Figure 1 直到 page 3 才出现。建议考虑将 Figure 1 提前或加入 teaser figure。\n2. **Pages 8–9 纯文本**：Related Work + Discussion + Limitations + Ethics 连续无 display item，阅读体验略单调。\n3. **Page 24 大面积空白**：Appendix 文本末页仅 ~25% 填充，page break 控制不佳。\n\n**Positive:**\n- 主文 8 display items / 8 pages，密度合理\n- 所有 float 位置合理，无漂移\n- 公式渲染全部正确\n- 无 margin 溢出\n- 符合 EMNLP 2026 8 页限制\n- Figure 1 色彩对比存在轻微色盲友好性问题（红-绿），建议改用 Okabe-Ito 色板\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.5 (Borderline Conference)**\n\n**置信度: 4/5**\n\n**理由：**\n\n这是一篇扎实的诊断分析工作。\"Correlation-selection gap\"概念清晰且有迁移价值，统计严谨度在 NLP 论文中属上乘，negative results 的诚实呈现值得肯定。实验覆盖面广（4 个 NER 数据集、4 个模型家族、3B–72B 跨度、9 种方法）。\n\n但论文的核心局限在于 prescriptive contribution 薄弱：entity-level construction 仅在 Few-NERD 上有明确正向效果（+1.40 pp, Holm p_adj=0.006），CoNLL 无增益，SciERC 增益微弱且未通过多重校正。这使论文本质上是一篇 negative result + 诊断分析工作，方法论增量有限。Related Work 过于压缩（~15 行），\"framework\"定位与实际分析贡献之间存在张力。\n\n**无 Must-Fix 级别的技术缺陷**——经交叉讨论，所有 critical 问题均被降级或解决。7 个 Should-Fix 问题（entity construction 定位、framework 澄清、Related Work 扩展、实验 setup 前置、θ_crit sensitivity、RE/SQL 覆盖、模型多样性呈现）均可在修改周期内解决。\n\n当前状态下 Findings 是安全着陆点。若能解决 SF1（entity construction 重新定位）、SF3（Related Work 扩展）和 SF7（主文 highlight 跨规模结果），可提升至 Conference 水平。\n\n---\n\n## Detailed Comments\n\n### Section 1 (Introduction)\n- \"α→0, not degeneracy alone, is the binding constraint\" 措辞基本准确但可更精确——建议改为 \"near-zero selection alignment (α→0), jointly with degeneracy, constitutes the binding constraint\"\n- Contributions 列表应显式区分 diagnostic methodology / formal characterization / empirical findings 三类贡献\n\n### Section 2 (Diagnostic Framework)\n- 建议在 Section 2 末尾增加 1–2 段实验概览（数据集、模型、N、T 的概要）\n- \"capability ceiling\" 定义清晰，但与 \"correlation-selection gap\" 的关系可更显式说明\n\n### Section 3 (Self-Verification)\n- ESJ AUROC=0.512 是重要的 negative finding，呈现简洁有效\n- Hidden-state probe 的 LODO transfer 下降（0.56–0.67）是关键发现，支持 dataset-specific 结论\n\n### Section 4 (Single-Signal Selection)\n- Table 1 和 Figure 2 有效传达 gap\n- \"Diagnostic cascade\" 四阶段逻辑清晰，但阶段间交互（R²<0）应在主文更显著呈现\n\n### Section 5 (Adaptive Methods)\n- Table 2 的 9 方法综述是有价值的参考\n- Cross-model ensemble (+0.42 pp) 作为唯一 unconditional positive result，可在讨论中更突出\n\n### Section 6 (Theory)\n- Proposition 1 形式化了直观观察——作为诊断工具有价值但不构成独立理论贡献\n- θ_crit=0.70 需 sensitivity 分析（θ∈[0.65, 0.75]）\n\n### Section 7 (Experiments)\n- 7.1 Experimental Setup 应前置或在 Section 2 提供概览\n- 7.3 Few-NERD cross-dataset contrast 是论文亮点，LP selection +1.39 pp (p<0.001) 是最强正向结果\n- 7.5 Prescriptive Results 应降低叙事权重，明确为探索性结果\n\n### Section 8 (Related Work)\n- 需要从 ~15 行扩展至 20–25 行\n- 补充 MBR for structured NLP、LLM calibration 讨论\n- 将 Yao/Yun concurrent works 的讨论从 Introduction 深化到 Related Work\n\n### Section 9 (Discussion)\n- 过于简短（约 5 行），建议扩展讨论 practical implications 和 future directions\n\n### Limitations\n- 覆盖面广且诚实，篇幅适中，符合 EMNLP 2026 规范\n\n### Appendix\n- 47 页附录详尽程度在同类工作中罕见，统计枚举透明度出色\n- Table 66 (differentiation matrix) 应在主文 Section 8 中引用\n- Appendix af (Anticipated Objections) 内容有用但可能给 reviewer 留下防御性印象",
    "project": "struct_self_consist_ie",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5 - Borderline Conference",
    "review_chat_id": "oc_3897c2857f11615119e277e820eae311"
  }
}
```

</details>

---


### Tool result

_source line 3567 · 2026-05-22T08:22:00.532118+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_1b56445332d8ca2b4964b30f300f0e00:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4525
}
```

</details>

---


### Assistant

_source line 3568 · 2026-05-22T08:22:08.923832+00:00_

审稿报告已投递至 Research Director。

**Round 33 审稿完成。**

核心结论：**Overall 3.5（Borderline Conference）**

- 两名 Reviewer 独立评分均为 3.5，经交叉讨论后维持
- **无 Must-Fix 级别技术缺陷**——所有 critical 问题经交叉讨论后降级或解决
- **7 个 Should-Fix**：entity construction 证据有限需重新定位、framework 定位需澄清、Related Work 需扩展、实验 setup 需前置、θ_crit 需 sensitivity 分析、RE/SQL 覆盖不足、模型多样性主文呈现不足
- **共识亮点**：统计严谨度出色、correlation-selection gap 概念有迁移价值、negative result 呈现诚实
- **着陆点**：当前 Findings 安全；解决 SF1/SF3/SF7 后可提升至 Conference

Issue Tracker 已更新（9 条 issue，均为 open）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 267

## Round 267

2 recorded events


### User

_source line 3569 · 2026-05-22T08:22:11.698783+00:00_

[Reviewer 1 审稿结果]:
已提交对 Reviewer 2 的逐条回应。核心判断：

- **N1（setup位置）**：REBUT——presentation问题不应标critical，Section 2.3已提供关键参数，建议降级为Should-Fix
- **N2（模型多样性）**：REBUT——R2的描述与论文不符，实际覆盖4个家族(Qwen3/LLaMA/Qwen2.5-72B/GPT-5.5)、3B–72B跨度、含encoder verifier(DeBERTa-v3)
- **W1/W3/W6**：AGREE——entity construction差异化、贡献类型标注、Related Work覆盖确需改进
- **W2/W4**：REBUT——cascade结构合理、观测性语言使用恰当
- **W5**：REBUT——R2对Spearman ρ²的"解释方差"解读是统计方法误用，且忽略了AUROC=0.82
- **M1/M2/M3/M6**：AGREE；**M4/M5**：REBUT

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 3570 · 2026-05-22T08:22:20.502453+00:00_

审稿报告已投递至 Research Director。

**最终评分：3.5（Borderline Conference）**

核心结论：
- **无 Must-Fix 级别技术缺陷**——经交叉讨论所有 critical 问题均被降级或解决
- **7 个 Should-Fix**：entity construction 重新定位、framework 定位澄清、Related Work 扩展、实验 setup 前置、θ_crit sensitivity 分析、RE/SQL 覆盖、模型多样性主文呈现
- **主要优势**：correlation-selection gap 概念有迁移价值、统计严谨度出色、negative results 诚实呈现
- **着陆点**：当前 Findings 安全；解决 SF1+SF3+SF7 可提升至 Conference

Issue tracker 已同步更新至 `review_issues.yaml`（10 条 issue，全部 open）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 268

## Round 268

80 recorded events


### User

_source line 3571 · 2026-05-22T08:43:51.331752+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: struct_self_consist_ie
- 论文路径: projects/struct_self_consist_ie/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Main Conference (ARR May 2026)
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 3572 · 2026-05-22T08:43:57.274102+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 3573 · 2026-05-22T08:43:57.325061+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 3286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 3574 · 2026-05-22T08:44:03.549493+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,get_visual_check_status,WebSearch",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,get_visual_check_status,WebSearch",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 3575 · 2026-05-22T08:44:03.600224+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 3576 · 2026-05-22T08:44:06.814206+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool call

_source line 3577 · 2026-05-22T08:44:07.316301+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "file": "docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "file": "docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 3578 · 2026-05-22T08:44:07.841921+00:00_

{"result":"# 项目 struct_self_consist_ie 概况\n\n## 实验状态 (318 个)\n\n- **exp_002_ner_conll2003**: DONE (success) — \n- **exp_004_re_diagnostic**: DONE (success) — \n- **exp_005**: DONE (success) — \n- **exp_014_entity_majority_voting**: DONE (success) — \n- **exp_013_exact_match_voting**: DONE (negative) — \n- **exp_012_logprob_baseline**: DONE (success) — \n- **mvp_pilot_005**: DONE (negative) — \n- **e1_component_wise_re_sj**: DONE (negative) — \n- **mvp_pilot_004**: DONE (negative) — \n- **ft_002_v2**: DONE (success) — \n- **mvp_pilot_002**: DONE (failed) — \n- **ft_002**: DONE (killed) — \n- **ft_001**: DONE (success) — \n- **mvp_pilot_003**: DONE (negative) — \n- **mvp_pilot_001**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-22\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| exp_fewnerd_pretrained_n32_s42 | Pretrained N-scaling: FewNERD N=32 with Qwen2.5-7B-Instruct (unfinetuned). FewNERD pretrained showed +3.90pp MV gain at N=8. Tests whether pretrained MV advantage scales with N and whether the pretrained-vs-finetuned direction flip persists at 4× budget. Complements CoNLL/SciERC pretrained N=32 for cross-dataset generalization evidence. | — | — | — |\n| exp_fewnerd_n32_s42 | N-scaling convergence test: at N=32 (4× current N=8), MV strict Δ remains negative on FewNERD finetuned model, demonstrating that the selection gap does not close at practical sample budgets. If MV Δ converges toward 0 slowly, this quantifies the impractical N required. Motivated by R34 C1 and Reviewer #107 P2. | — | — | — |\n\n## 待处理\n- exp_conll_pretrained_n64_s42: Pretrained N-scaling: CoNLL N=64 with Qwen2.5-7B-Instruct (unfinetuned). Fourth data point for pretrained CoNLL N-scaling curve (N=8 +3.01, N=32 +3.21). Tests whether pretrained MV gain continues scaling and whether degeneracy continues declining at N=64.（排队等待 GPU）\n- exp_scierc_pretrained_n64_s42: Pretrained N-scaling: SciERC N=64 with Qwen2.
…[truncated 1743 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1027
}
```

</details>

---


### Tool result

_source line 3579 · 2026-05-22T08:44:07.842446+00:00_

Error executing tool read_project_file: 1 validation error for read_project_fileArguments
project
  Field required [type=missing, input_value={'file': 'docs/paper/main.tex'}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.12/v/missing

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 526
}
```

</details>

---


### Tool call

_source line 3580 · 2026-05-22T08:44:07.842699+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review ARR 2026 call for papers submission guidelines author instructions site:aclweb.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review ARR 2026 call for papers submission guidelines author instructions site:aclweb.org"
  }
}
```

</details>

---


### Tool result

_source line 3581 · 2026-05-22T08:44:16.190678+00:00_

Web search results for query: "ACL Rolling Review ARR 2026 call for papers submission guidelines author instructions site:aclweb.org"

Links: [{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"Industry Track — Call for Papers @ EACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/industry-track-call-papers-eacl-2026"},{"title":"The 14th Joint Conference on Lexical and Computational Semantics | ACL Member Portal","url":"https://www.aclweb.org/portal/content/14th-joint-conference-lexical-and-computational-semantics"},{"title":"ACL Policy on Publication Ethics - Admin Wiki","url":"https://www.aclweb.org/adminwiki/index.php/ACL_Policy_on_Publication_Ethics"},{"title":"EACL 2026 - Call for System Demonstrations | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-call-system-demonstrations"}]

Based on the search results, I found relevant information about ACL Rolling Review (ARR) and 2026 submission guidelines. Here are the key submission guidelines and author instructions:

## Paper Format and Templates

Paper submissions must use the official ACL style templates, which are available as an Overleaf template and can also be downloaded directly via https://aclrollingreview.org/cfp under 'Paper Submission Process, Criteria and Templates'. All submissions must be in PDF format.

## Anonymity Policy

Under the new policy, submissions will remain anonymous during peer review, but authors are free to post and discuss non-a
…[truncated 1069 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 8347
}
```

</details>

---


### Tool call

_source line 3582 · 2026-05-22T08:44:20.457808+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "file": "docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 3583 · 2026-05-22T08:44:21.361424+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'docs/paper/main.tex'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 903
}
```

</details>

---


### Tool call

_source line 3584 · 2026-05-22T08:44:21.411999+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission deadline page limit guidelines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission deadline page limit guidelines"
  }
}
```

</details>

---


### Tool call

_source line 3585 · 2026-05-22T08:44:21.512854+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review ARR May 2026 deadline submission guidelines page limit template"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review ARR May 2026 deadline submission guidelines page limit template"
  }
}
```

</details>

---


### Tool result

_source line 3586 · 2026-05-22T08:44:27.710265+00:00_

Web search results for query: "EMNLP 2026 call for papers submission deadline page limit guidelines"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"EMNLP 2026 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"},{"title":"Update EMNLP 2026 conference dates and deadlines · huggingface/ai-deadlines at 2754f67","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/2754f67c0550847973789522a0a082dd5443b5c0"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"}]

Based on the search results, here is the information about EMNLP 2026 call for papers submission deadline, page limit, and guidelines:

## Submission Deadline

The EMNLP 2026 paper submission deadline is May 25, 2026, at 23:59:59 UTC-12. All deadlines are 11:59PM UTC-12:00 ("anywhere on Earth").

## Page Limits

The format is two-column with an 8-page limit for long papers and a 4-page limit for short papers. Final versions of accepted papers will be given one additional page of content (up to 9 page
…[truncated 718 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 6298
}
```

</details>

---


### Tool result

_source line 3587 · 2026-05-22T08:44:27.962040+00:00_

Web search results for query: "ACL Rolling Review ARR May 2026 deadline submission guidelines page limit template"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ACL ARR 2026 January | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026%2FJanuary"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"}]

Based on the search results, here's information about ACL Rolling Review (ARR) submission guidelines:

## May 2026 Deadline

The submission deadline is always the 15th of the month, so the May 2026 deadline would be May 15, 2026.

## Submission Guidelines

**Format and Template:**
The submission must adhere to the formatting in the submis
…[truncated 960 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 6449
}
```

</details>

---


### Tool call

_source line 3588 · 2026-05-22T08:44:34.091627+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 3589 · 2026-05-22T08:44:34.242689+00:00_

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
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{amsthm}
16	\newtheorem{proposition}{Proposition}
17	\newtheorem{theorem}{Theorem}
18	\newtheorem{corollary}{Corollary}
19	\newtheorem{definition}{Definition}
20	\usepackage{multirow}
21	\usepackage{xcolor}
22	\usepackage{subcaption}
23	\usepackage{alphalph}
24	\usepackage{enumitem}
25	
26	\graphicspath{{figures/}}
27	
28	\title{Characterizing the Capability Ceiling of Self-Consistency:\\ A Diagnostic Framework for Test-Time Aggregation in NER}
29	
30	\author{Anonymous}
31	
32	\begin{document}
33	\maketitle
34	
35	\input{sections/abstract}
36	\input{sections/introduction}
37	\input{sections/diagnostic}
38	\input{sections/mechanistic}
39	\input{sections/single_signal}
40	\input{sections/adaptive}
41	\input{sections/theory}
42	\input{sections/experiments_main}
43	\input{sections/background}
44	\input{sections/discussion}
45	
46	\section*{Limitations}
47	\input{sections/limitations}
48	
49	\section*{Ethics Statement}
50	All experiments use publicly available benchmarks (SciERC, CoNLL-2003, Few-NERD, WNUT-17), open-weight models (Qwen3-8B, Qwen3-14B, Qwen3-4B, LLaMA-3.1-8B), and the GPT-5.5 API.
51	CoNLL-2003 is derived from the Reuters RCV1 corpus, which is available for research purposes under a NIST agreement; we use the standard research distribution.
52	No new human data was collected or annotated for this study.
53	Our findings on signal limitations could inform more reliable deployment of IE systems by guiding practitioners toward appropriate confidence signals for their use case.
54	Code and data will be released upon acceptance at [anonymized URL].
55	
56	\section*{Responsible NLP Research Checklist}
57	\input{sections/checklist}
58	
5
…[truncated 157 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 3590 · 2026-05-22T08:44:34.243200+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:read_local_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:read_local_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 3591 · 2026-05-22T08:44:34.343891+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 3592 · 2026-05-22T08:44:39.170669+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 3593 · 2026-05-22T08:44:39.271439+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 3594 · 2026-05-22T08:44:39.271874+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "struct_self_consist_ie",
  "config_section": "external_review"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "config_section": "external_review"
  }
}
```

</details>

---


### Tool result

_source line 3595 · 2026-05-22T08:44:40.276598+00:00_

{"result":"# 项目 struct_self_consist_ie 概况\n\n## 实验状态 (318 个)\n\n- **exp_002_ner_conll2003**: DONE (success) — \n- **exp_004_re_diagnostic**: DONE (success) — \n- **exp_005**: DONE (success) — \n- **exp_014_entity_majority_voting**: DONE (success) — \n- **exp_013_exact_match_voting**: DONE (negative) — \n- **exp_012_logprob_baseline**: DONE (success) — \n- **mvp_pilot_005**: DONE (negative) — \n- **e1_component_wise_re_sj**: DONE (negative) — \n- **mvp_pilot_004**: DONE (negative) — \n- **ft_002_v2**: DONE (success) — \n- **mvp_pilot_002**: DONE (failed) — \n- **ft_002**: DONE (killed) — \n- **ft_001**: DONE (success) — \n- **mvp_pilot_003**: DONE (negative) — \n- **mvp_pilot_001**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-22\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| exp_fewnerd_pretrained_n32_s42 | Pretrained N-scaling: FewNERD N=32 with Qwen2.5-7B-Instruct (unfinetuned). FewNERD pretrained showed +3.90pp MV gain at N=8. Tests whether pretrained MV advantage scales with N and whether the pretrained-vs-finetuned direction flip persists at 4× budget. Complements CoNLL/SciERC pretrained N=32 for cross-dataset generalization evidence. | — | — | — |\n| exp_fewnerd_n32_s42 | N-scaling convergence test: at N=32 (4× current N=8), MV strict Δ remains negative on FewNERD finetuned model, demonstrating that the selection gap does not close at practical sample budgets. If MV Δ converges toward 0 slowly, this quantifies the impractical N required. Motivated by R34 C1 and Reviewer #107 P2. | — | — | — |\n\n## 待处理\n- exp_conll_pretrained_n64_s42: Pretrained N-scaling: CoNLL N=64 with Qwen2.5-7B-Instruct (unfinetuned). Fourth data point for pretrained CoNLL N-scaling curve (N=8 +3.01, N=32 +3.21). Tests whether pretrained MV gain continues scaling and whether degeneracy continues declining at N=64.（排队等待 GPU）\n- exp_scierc_pretrained_n64_s42: Pretrained N-scaling: SciERC N=64 with Qwen2.
…[truncated 1743 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1004
}
```

</details>

---


### Tool call

_source line 3596 · 2026-05-22T08:44:43.741923+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 3597 · 2026-05-22T08:44:43.742547+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/checklist.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/theoretical.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/_archived/experiments_OLD.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/adaptive.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/mechanistic.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/diagnostic.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/single_signal.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/background.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments_main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-idea_g
…[truncated 185 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 3598 · 2026-05-22T08:44:47.815291+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 3599 · 2026-05-22T08:44:48.117038+00:00_

1	\begin{abstract}
2	Test-time compute scaling yields large gains on discrete-answer reasoning and code generation, yet for named entity recognition (NER), where outputs are entity sets with partial overlap, aggregation gains are marginal.
3	We trace this failure through three stages of investigation.
4	Quality estimation signals effectively predict output quality (Spearman $\rho$ up to 0.45, AUROC 0.82 across nine method categories), confirming the information to identify better outputs exists.
5	Yet instance-level selection yields ${<}1$\,pp on most datasets; a four-stage diagnostic cascade localizes this \textbf{correlation-selection gap}: the optimal strategy is dataset-dependent (LP-best: $+8$\,pp on Few-NERD; MV dominates on CoNLL) and near-zero selection alignment ($\alpha{\to}0$), jointly with degeneracy, is the binding constraint.
6	Exploratory entity-level construction ($+0.3$--$1.4$\,pp where both conditions hold) and regime-specific LP selection ($+1.39$\,pp on Few-NERD) partially bypass the sample-level bottleneck at entity granularity.
7	A degeneracy threshold ($\theta_{\text{crit}}{=}0.70$) predicts when aggregation gains vanish; the cascade generalizes to RE ($-5.90$\,pp MV at $10.1$\% degeneracy) and SQL parsing ($87.2$\% degeneracy).
8	\end{abstract}
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 3600 · 2026-05-22T08:44:48.117593+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 3601 · 2026-05-22T08:44:48.620645+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Test-time compute scaling complements model scaling \cite{snell2025scaling}: repeated sampling with majority voting \cite{wang2023selfconsistency}, best-of-$N$ with learned verifiers \cite{cobbe2021verifiers, brown2024monkeys}, and extended chain-of-thought \cite{muennighoff2025s1} produce large gains on reasoning and code generation.
4	These successes share a structural prerequisite: the output space admits either exact equivalence classes (multiple-choice, numeric answers) or execution-based verification (code).
5	Named entity recognition (NER) breaks both assumptions.
6	The output is a set of typed entities; two samples from the same input routinely extract overlapping but non-identical sets, and no external oracle can adjudicate correctness at test time.
7	Without equivalence classes, majority voting reduces to heuristic frequency counting; without a verifier, best-of-$N$ requires a reliable proxy signal.
8	This structural mismatch raises a concrete question: can self-consistency signals that estimate quality well for reasoning tasks also \textit{select} better outputs or \textit{construct} better entity sets for NER?
9	We investigate this question for NER and extend exploratorily to SQL parsing, treating NER as a representative instance of set-valued generation.
10	
11	This question has practical stakes: hallucination detectors \cite{manakul2023selfcheckgpt, min2023factscore} assume cross-sample consistency can verify claims.
12	Five QE signals effectively predict output quality ($\rho$ up to $0.45$, AUROC $0.82$; Table~\ref{tab:quality_estimation}), and a hidden-state probe shows models encode entity quality internally (AUROC $0.63$\textendash$0.88$; \S\ref{sec:mechanistic})---yet three self-verification probes yield chance-level results for fine-tuned models, exposing an \textit{introspection boundary} \cite{huang2024large}: the information exists but cannot be accessed through prompting.
13	
14	This popul
…[truncated 3813 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 3602 · 2026-05-22T08:44:48.621038+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/diagnostic.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/diagnostic.tex"
  }
}
```

</details>

---


### Tool result

_source line 3603 · 2026-05-22T08:44:49.072868+00:00_

1	\section{Diagnostic Framework}\label{sec:method}
2	
3	Our analysis is observational: we characterize statistical associations between agreement signals and output quality without claiming causal mechanisms.
4	
5	\subsection{Problem Formulation}\label{sec:formulation}
6	
7	Given model $\mathcal{M}$ and input $x$, we sample $N$ outputs $\{y_1, \ldots, y_N\}$ at temperature $T > 0$ via constrained decoding \cite{willard2023guided}, where each $y_i$ is an entity set.
8	A \textbf{per-sample signal} $c_{\text{ps}}: (x, y_i) \to \mathbb{R}$ scores each output independently; an \textbf{instance-level signal} $c_{\text{il}}: (x, \{y_i\}_{i=1}^N) \to \mathbb{R}$ produces a single score per input (notation in Appendix~\ref{app:notation}).
9	This distinction is consequential: 4 of 5 signals are instance-level aggregates assigning identical scores to all $N$ candidates.
10	Only LP carries per-sample discriminative power: ensemble optimization assigns LP mean weight $0.78$, with structural signals receiving zero weight (Appendix~\ref{app:supervised_combination}).
11	When LP fails---as in few-shot regimes where LP $\rho{\to}0$ (\S\ref{sec:scaling})---no alternative per-sample signal exists.
12	
13	We define the \textbf{capability ceiling} as the practical performance upper bound achievable through self-consistency at realistic sample budgets ($N{\leq}16$), beyond which diminishing returns render further scaling impractical.
14	
15	\subsection{Confidence Signals}\label{sec:signals}
16	
17	Entity matching uses exact span and type match.
18	We distinguish two signal families: four \textit{agreement signals} computed across samples---\textit{structural} (Soft Jaccard [SJ], entity voting confidence [VC]) and \textit{surface} (exact match [EM], Fleiss' $\kappa$ [FK])---and log-probability [LP] as the sole \textit{model-internal} signal, derived from generation probabilities and providing per-sample discrimination.
19	
20	\paragraph{Log-probability (per-sample).}
21	$c_{\text{lp}}(y_i)
…[truncated 2151 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 3604 · 2026-05-22T08:44:49.073346+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/mechanistic.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/mechanistic.tex"
  }
}
```

</details>

---


### Tool result

_source line 3605 · 2026-05-22T08:44:49.976733+00:00_

1	\section{How Self-Verification Fails}\label{sec:mechanistic}
2	
3	The diagnostic cascade (\S\ref{sec:method}) identifies \textit{where} self-consistency fails; this section probes \textit{why} by testing whether models can self-verify at the entity level.
4	We evaluate self-verification and diagnostic probes on Qwen2.5-7B (a separate model family from the primary Qwen3-8B) fine-tuned for NER on Few-NERD ($N{=}8$, seed 42; full results in Appendix~\ref{app:self_verification}).
5	
6	\paragraph{Entity Self-Judgment (ESJ).}
7	For each extracted entity, we prompt the generating model: ``Is [\textit{entity}] a [\textit{type}] entity in this sentence?''
8	Entity-level AUROC is $0.512$---indistinguishable from chance---with P(yes$|$correct)${=}0.500$ and P(yes$|$incorrect)${=}0.500$.
9	ESJ-weighted construction degrades F1 to $0.711$ (vs.\ greedy $0.794$).
10	
11	\paragraph{Multi-Round Self-Consistency (MRSC).}
12	Following iterative self-refinement \cite{madaan2023selfrefine}, we re-prompt on disputed entities (agreement ${<}0.6$) with focused verification; P(yes) separation between gold and non-gold entities is $0.0006$ ($0.5003$ vs.\ $0.4997$).
13	MRSC best F1 ($0.763$) falls below greedy.
14	
15	\paragraph{Latent Self-Consistency (LSC).}
16	Mean-pooled final-layer hidden states ($d{=}3584$) provide per-sample latent representations.
17	Centroid selection ($0.759$) underperforms greedy ($0.794$); latent entity confidence ($0.839$) outperforms majority vote ($0.792$) but does not close the oracle gap ($0.882$).
18	
19	\paragraph{Hidden-state probe.}
20	A logistic regression on mean-pooled final-layer hidden states at entity spans achieves AUROC $0.636$ (Few-NERD), $0.882$ (CoNLL), $0.630$ (SciERC), evaluated with GroupKFold CV (5-fold ${\times}$ 3 seeds, groups${=}$source instance to prevent entity-level leakage; Appendix~\ref{app:hidden_probe}).
21	All three exceed ESJ ($0.51$); only CoNLL approaches frequency agreement ($0.868$).
22	Cross-dataset transfer is weak: lea
…[truncated 1062 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 903
}
```

</details>

---


### Tool call

_source line 3606 · 2026-05-22T08:44:49.977201+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/single_signal.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/single_signal.tex"
  }
}
```

</details>

---


### Tool result

_source line 3607 · 2026-05-22T08:44:50.478935+00:00_

1	\section{Where Single-Signal Selection Fails}\label{sec:selection_gap}
2	
3	\paragraph{Definitional vs.\ empirical.}
4	We decompose the correlation-selection gap into two layers.
5	The first is structural: four of five signals are instance-level aggregates that assign identical scores to all $N$ candidates from a given input (\S\ref{sec:formulation}), so they estimate quality across inputs but cannot rank candidates within an instance---selection failure is a design property, not an empirical finding.
6	The second layer is empirical and constitutes the core diagnostic: LP---the only per-sample signal---suffers compression under constrained decoding, with 60\% of SciERC instances showing within-instance LP range below 0.041 nats (Appendix~\ref{app:logprob_ties}), effectively eliminating the variation needed for sample discrimination. Even where LP varies, selection gains depend on LP-quality alignment rather than degeneracy alone.
7	Cross-instance $\rho$ (Table~\ref{tab:quality_estimation}) is attenuated by varying instance difficulty; within-instance $\rho$ directly measures whether LP discriminates candidates for a fixed input, making it the relevant predictor of selection success.
8	
9	\begin{table}[t]
10	\centering
11	\small
12	\caption{Best-of-$N$ selection (macro F1) on SciERC ($N{=}8$, $T{=}1.0$). Selection signals: 2-seed mean${\pm}\sigma$; baselines: 3-seed (Oracle${=}0.781$, Greedy${=}0.667$). LP is per-sample; others use consensus-proximity. $^\dagger$One score per input.}
13	\label{tab:selection}
14	\begin{tabular}{lcc}
15	\toprule
16	Method & NER F1 & $p$ \\
17	\midrule
18	Oracle & $0.775 \pm 0.001$ & --- \\
19	Greedy ($T{=}0$) & $0.645 \pm 0.001$ & --- \\
20	\midrule
21	LP           & $\mathbf{0.647} \pm 0.005$ & .29 \\
22	SJ           & $0.646 \pm 0.002$ & .67 \\
23	FK           & $0.646 \pm 0.001$ & .79 \\
24	EM           & $0.637 \pm 0.001$ & n/a$^\dagger$ \\
25	VC           & $0.623 \pm 0.004$ & n/a$^\dagger$ \\
26	\midrule
27	Random       & $0.61
…[truncated 2668 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 501
}
```

</details>

---


### Tool call

_source line 3608 · 2026-05-22T08:44:50.479359+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/adaptive.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/adaptive.tex"
  }
}
```

</details>

---


### Tool result

_source line 3609 · 2026-05-22T08:44:50.983762+00:00_

1	\section{Adaptive Methods}\label{sec:adaptive}
2	
3	Since instance-level selection fails (\S\ref{sec:selection_gap}), we present approaches that extract value from multi-sample generation beyond single-signal sample ranking.
4	Table~\ref{tab:method_summary} summarizes all 9 method categories evaluated; only cross-model ensembles yield an unconditional positive result.
5	
6	\begin{table}[t]
7	\centering
8	\small
9	\caption{Summary of 9 method categories tested (including MV baseline, LP selection, and cross-model ensemble beyond the seven verification methods in \S\ref{sec:mechanistic}--\S\ref{sec:adaptive}). $\Delta$F1 vs.\ greedy; dataset in parentheses. Full coverage in Appendix~\ref{app:method_coverage}.}
10	\label{tab:method_summary}
11	\resizebox{\columnwidth}{!}{%
12	\begin{tabular}{@{}llrl@{}}
13	\toprule
14	Category & Method & $\Delta$F1 / metric & § \\
15	\midrule
16	Freq.\ voting & MV & baseline & \ref{sec:prescriptive} \\
17	LP selection & Best-of-$N$ (LP) & $+1.39$\,pp (FN)$^\dagger$ & \ref{sec:selection_gap} \\
18	Self-verif.\ (prompt) & ESJ & AUROC $0.51$ & \ref{sec:mechanistic} \\
19	Multi-round refine. & MRSC & $-3.1$\,pp (FN) & \ref{sec:mechanistic} \\
20	Latent aggregation & LSC & $-3.5$\,pp (FN) & \ref{sec:mechanistic} \\
21	Adaptive gating & DALS & $+0.71$\,pp (SciERC)$^\ddagger$ & App.~\ref{app:dals} \\
22	Supervised verifier & LGB & $+0.30$\,pp (OOF) & \ref{sec:verifier} \\
23	Sup.\ combination & LR/MLP/RF & $-0.4$ to $-3.1$\,pp & App.~\ref{app:supervised_combination} \\
24	Cross-model & Qwen$+$LLaMA & $\mathbf{+0.42}$\,pp (FN) & \ref{sec:cross_model} \\
25	\bottomrule
26	\end{tabular}}
27	{\footnotesize $^\dagger$Few-NERD only; SciERC $+0.2$\,pp ($p{=}0.29$). $^\ddagger$Seed-sensitive ($\sigma{=}0.48$\,pp).}
28	\end{table}
29	
30	\subsection{Cross-Model Self-Consistency}\label{sec:cross_model}
31	
32	Mixing samples from architecturally distinct models can partially bypass within-model degeneracy.
33	Combining 4 samples each from Qwen3-8B and
…[truncated 764 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 504
}
```

</details>

---


### Tool call

_source line 3610 · 2026-05-22T08:44:50.984148+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/theory.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/theory.tex"
  }
}
```

</details>

---


### Tool result

_source line 3611 · 2026-05-22T08:44:51.235387+00:00_

1	\section{Threshold Regime Analysis}\label{sec:theory_scaling}
2	
3	\subsection{Entity Construction as MBR Decoding}\label{sec:mbr_theory}
4	
5	Entity-level construction selects $\hat{y}_{\textup{MBR}} = \{e \in E_\cup : \hat{p}(e) > \alpha/(\alpha{+}1)\}$ under balanced set-overlap utility; $\alpha{=}1$ recovers majority vote (Proposition~\ref{prop:construction_mbr}; Table~\ref{tab:entity_construction}; Appendix~\ref{app:mbr_proof}).
6	Signal-derived weights $w_i$ yield quality-weighted MBR: $\hat{p}_w(e) = \sum_{i} w_i \, \mathbf{1}[e {\in} y_i] / \sum_{i} w_i$; weighting improves when $w_i$ correlates with instance quality but degrades otherwise (LP on SciERC: $\rho{\approx}0.2$; \S\ref{sec:prescriptive}).
7	We select $\varepsilon{=}0.05$ at the elbow of the compression curve, where LP-best selection advantage transitions from $+1.5$\,pp (compressed) to $+4.6$\,pp (non-compressed; Appendix~\ref{app:fewnerd_epsilon}).
8	
9	\subsection{Scaling and Inverse Scaling}\label{sec:scaling}
10	
11	Oracle F1 follows $F_1(N) = a - b \cdot N^{-c}$ ($R^2 > 0.999$; Figure~\ref{fig:oracle_scaling}): Few-NERD ($c{\approx}0.61$) scales comparably to reasoning tasks \cite{brown2024monkeys}, SciERC converges more slowly ($c{\approx}0.35$), yet confidence-based aggregation recovers ${<}1$\,pp---a persistent gap.
12	The gap persists across scales and families: scaling from 8B to 14B FT increases oracle headroom ($+1.2$\,pp) with minimal greedy gain ($+0.9$\,pp), and GPT-5.5 (200 Few-NERD instances, zero-shot) exhibits the same pattern---50\% degeneracy, SJ $\rho{=}0.346$, MV $+1.4$\,pp yet 6.8\,pp oracle headroom unrealized.\footnote{Of the 10.1\% of GPT-5.5 samples producing empty entity sets, 88\% correspond to gold-empty instances; true parse failures affect only 1.2\% of samples (19/1{,}600) and shift all reported metrics by ${<}0.5$\,pp. See Appendix~\ref{app:frontier_sc}.}
13	Degeneracy is model-family-dependent rather than scale-dependent (Qwen2.5: $31.7$--$46.2$\% vs.\ Qwen3:
…[truncated 3578 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 3612 · 2026-05-22T08:44:51.285961+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments_main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments_main.tex"
  }
}
```

</details>

---


### Tool result

_source line 3613 · 2026-05-22T08:44:51.336737+00:00_

1	\section{Experiments}\label{sec:experiments}
2	
3	\subsection{Experimental Setup}\label{sec:setup}
4	
5	\paragraph{Datasets.}
6	We evaluate on four English NER benchmarks spanning a difficulty gradient.
7	\textbf{SciERC} \cite{luan2018scierc} (551 test instances, 6 entity types) is the primary medium-difficulty test bed (${\approx}$65\% F1).
8	\textbf{Few-NERD} \cite{ding2021fewnerd} (INTRA coarse; 37{,}648 instances, 8 entity types, ${\approx}$75\% F1) provides a low-degeneracy contrast where LP selection succeeds (\S\ref{sec:selection_gap}).
9	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} (3{,}453 test sentences, 4 entity types, ${\approx}$91\% F1) serves as a ceiling-effect control.
10	\textbf{WNUT-17} \cite{derczynski2017wnut} (1{,}287 social media instances, 51\% zero F1) probes the signal-collapse boundary.
11	
12	\paragraph{Models and sampling.}
13	\textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are LoRA fine-tuned using LLaMA Factory \cite{zheng2024llamafactory} (Appendix~\ref{app:training}; Few-NERD uses 3 epochs vs.\ 5 for others; Appendix~\ref{app:epoch_confound}).
14	$N{=}8$ samples at $T{=}1.0$ (primary) with vLLM constrained decoding \cite{willard2023guided}; $N {\in} \{16, 32, 64\}$ for scaling (Figure~\ref{fig:n_scaling}; Appendix~\ref{app:n_scaling}).
15	
16	\begin{figure}[t]
17	\centering
18	\includegraphics[width=\columnwidth]{figures/fig_n_scaling_mv.pdf}
19	\caption{MV $\Delta$F1 vs.\ $\log_2 N$ across three datasets (Qwen3-8B FT, seed${=}42$). Dotted gray: $\Delta{=}0$. Gains are dataset-dependent: persistently negative on Few-NERD, near zero on SciERC at higher $N$, marginally positive on CoNLL ($+0.6$\,pp at $N{=}64$).}
20	\label{fig:n_scaling}
21	\end{figure}
22	
23	%% ============================================================
24	\subsection{Quality Estimation Results}\label{sec:qe_results}
25	
26	\begin{table*}[t]
27	\centering
28	\small
29	\caption{NER quality estimation ($\rho$ and AUROC; $N{=}8$, primary seed${=}42$; 3-seed $
…[truncated 7371 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 3614 · 2026-05-22T08:44:56.221912+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments_main.tex",
  "offset": "113"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments_main.tex",
    "offset": "113"
  }
}
```

</details>

---


### Tool result

_source line 3615 · 2026-05-22T08:44:56.689209+00:00_

&lt;system-reminder>Warning: the file exists but is shorter than the provided offset (113). The file has 113 lines.&lt;/system-reminder>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 467
}
```

</details>

---


### Tool call

_source line 3616 · 2026-05-22T08:44:56.689695+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/background.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/background.tex"
  }
}
```

</details>

---


### Tool result

_source line 3617 · 2026-05-22T08:44:57.191988+00:00_

1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Test-time compute scaling.}
4	Self-consistency \cite{wang2023selfconsistency} and best-of-$N$ \cite{snell2025scaling, brown2024monkeys} drive large gains on reasoning and code \cite{chen2021codex}.
5	Reward-free selectors \cite{taubenfeld2025cisc, kang2025selfcertainty}, BoN scaling laws \cite{gao2023scaling}, adaptive allocation \cite{aggarwal2023adaptive}, and trained verifiers \cite{cobbe2021verifiers, lightman2024verify} all target discrete-answer settings; structured prediction requires different aggregation because degeneracy operates at the entity-set level.
6	
7	\paragraph{SC failure modes and fine-grained variants.}
8	\citet{chen2023twofailures} identify SC failures where consistent outputs are systematically wrong; \citet{huang2024large} show LLMs cannot self-correct reasoning without external feedback.
9	\citet{chen2024usc} extend SC to free-form tasks and \citet{thirukovalluru2024atomic} decompose claims atomically; both face limits under constrained decoding where sub-output agreement does not translate to selection gain (\S\ref{sec:selection_gap}).
10	
11	\paragraph{Consistency for structured IE.}
12	\citet{yao2026consistency} demonstrate task-level correlation ($\rho$ up to 0.47) between consistency and quality across NER/RE tasks; we diagnose why this correlation fails to yield selection gain, identifying entity-level failure mechanisms absent from their task-level analysis and providing operational bypasses ($+0.32$--$1.40$\,pp).
13	\citet{xie2023zeroshot} propose entity voting for zero-shot NER and \citet{xie2024selfimproving} report positive SC under zero-shot prompting where diversity is high---contrasting with our fine-tuned setting where degeneracy inverts diversity.
14	\paragraph{Uncertainty estimation and MBR.}
15	Our selection instantiates MBR decoding \cite{eikema2022sampling, denero2009fast}; despite MBR's success in translation \cite{freitag2022high, muller2021understanding} and 
…[truncated 989 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 3618 · 2026-05-22T08:44:57.192412+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 3619 · 2026-05-22T08:44:57.744975+00:00_

1	\section{Discussion and Conclusion}\label{sec:discussion}\label{sec:selection_method}\label{sec:conclusion}
2	
3	Degeneracy (12.2--67.9\%) and LP-quality alignment ($\rho$ 0.043--0.667) jointly constrain aggregation; temperature disentangles these (\S\ref{sec:scaling}; Table~\ref{tab:t_degeneracy}), and across four frontier models degeneracy and the selection gap are negatively correlated (5.5--74\%; Table~\ref{tab:frontier_sc_cross}).
4	On CoNLL, pretrained MV captures ${\sim}98$\% of oracle headroom versus ${<}2$\% finetuned (Appendix~\ref{app:cross_scale}); entity-level construction bypasses both failure mechanisms when degeneracy ${<}22$\%, with $\theta_{\text{crit}}{=}0.70$ and $\alpha{\to}0$ as the binding constraints.
5	
6	\paragraph{Practical implications.}
7	The cascade provides a pre-deployment diagnostic: measure degeneracy and LP-F1 alignment on a held-out set before investing in $N{\times}$ inference.
8	When degeneracy exceeds $\theta_{\text{crit}}{=}0.70$, aggregation is unlikely to help; when both conditions are favorable ($D{<}22\%$, LP $\rho{>}0.2$), entity-level construction offers modest but reliable gains.
9	The gap between oracle scaling ($R^2{>}0.999$; \S\ref{sec:scaling}) and realized gains (${\leq}1.4$\,pp) suggests that inference-time scaling for structured prediction requires fundamentally different strategies from discrete-answer tasks---entity-level rather than sample-level aggregation, and quality-aware weighting rather than majority vote.
10	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 3620 · 2026-05-22T08:44:57.745459+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 3621 · 2026-05-22T08:44:57.846278+00:00_

1	Our evidence is correlational and theoretical (MBR framework, conditional decomposition), not interventional: we have not performed controlled interventions (e.g., artificially varying degeneracy while holding other factors constant), and the cascade stages interact in ways that resist decomposition into independent causal effects ($R^2{<}0$; \S\ref{sec:selection_gap}); causal claims require future intervention experiments.
2	
3	Scope: structured IE (NER primary, RE and SQL exploratory), English only, open-weight (Qwen and LLaMA) and closed-source (GPT-5.5) families, fine-tuned (4B--14B) and zero-shot (72B, GPT-5.5) regimes, sample budget $N{\leq}32$.
4	Our evaluation covers four NER datasets; the RE extension covers a single SciERC benchmark ($n{=}397$; $40$\% of instances yield zero F1, primarily from upstream entity span errors), and the SQL extension covers a single Spider subset ($n{=}196$) with 87.2\% degeneracy---both are exploratory and do not support generalization claims.
5	All experiments use English-language datasets; cross-lingual generalization remains untested.
6	Cross-model consistency results (\S\ref{sec:cross_model}) are limited to one dataset (Few-NERD) and one model pair (Qwen3-8B + LLaMA-3.1-8B).
7	Entity-level construction assumes the model produces useful partial outputs across samples; when model capability is insufficient (WNUT-17, 51\% F1${=}0$), this precondition fails and construction cannot improve over greedy.
8	Entity-level construction requires $N{\times}$ inference cost for $+1$\textendash$1.4$\,pp gain; cost-effectiveness may not justify deployment in resource-constrained settings.
9	We cover 4B\textendash 14B fine-tuned, 72B zero-shot, and GPT-5.5 zero-shot; the gap persists across all but behavior with 72B fine-tuning is untested.
10	Frontier API models exhibit markedly different degeneracy profiles (e.g., Claude Sonnet~4 at 74\% vs.\ DeepSeek Chat at 5.5\%; Table~\ref{tab:frontier_sc_cross}), suggesting that our findings from f
…[truncated 3975 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 3622 · 2026-05-22T08:44:58.349111+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 3623 · 2026-05-22T08:44:58.701197+00:00_

File content (65864 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 3624 · 2026-05-22T08:45:11.004458+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 3625 · 2026-05-22T08:45:11.256147+00:00_

1	\section{Notation}\label{app:notation}
2	
3	Table~\ref{tab:notation} summarizes the notation used throughout the paper.
4	
5	\begin{table}[h]
6	\centering
7	\small
8	\begin{tabular}{cl}
9	\toprule
10	Symbol & Meaning \\
11	\midrule
12	$\mathcal{M}$ & Language model \\
13	$x$ & Input instance \\
14	$y_i$ & $i$-th stochastic sample \\
15	$N$ & Number of samples \\
16	$T$ & Sampling temperature \\
17	$c(\cdot)$ & Confidence signal \\
18	SJ & Soft Jaccard similarity \\
19	FK & Fleiss' $\kappa$ \\
20	EM & Exact-match voting rate \\
21	VC ($c_{\mathrm{vc}}$) & Entity voting confidence \\
22	LP ($c_{\mathrm{lp}}$) & Log-probability (mean token log-likelihood) \\
23	\bottomrule
24	\end{tabular}
25	\caption{Notation used throughout the paper.}
26	\label{tab:notation}
27	\end{table}
28	
29	\section{Robustness Analysis}\label{app:robustness}
30	
31	We exclude instances with empty gold annotations from all correlation analyses (CoNLL: 697/3{,}453 instances, 20.2\%; SciERC: 22/551, 4.0\%).
32	For these instances, F1 is trivially zero regardless of prediction quality, and consistency signals reflect agreement on the empty set rather than extraction quality. Including them inflates or deflates Spearman $\rho$ depending on signal behavior at the boundary.
33	
34	\begin{table}[t]
35	\centering
36	\small
37	\caption{Signal robustness across configurations (Spearman $\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: transfer across model families (both 8B) (LLaMA CoNLL $N{=}16$, 3-seed mean $\pm\sigma$). $^\dagger$Mean over 3 seeds ($\sigma{=}0.013$; individual: 0.398, 0.423, 0.410). $\sigma$ computed as sample standard deviation.}
38	\label{tab:robustness}
39	\begin{tabular}{llcc}
40	\toprule
41	& & NER $\rho$ & RE $\rho$ \\
42	\midrule
43	\multicolumn{4}{l}{\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\
44	\quad SJ & $T{=}0.7$ & 0.364 & 0.234 \\
45	\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\
46	\quad FK & $T{=}0.7$ & 0.289 & 0.184 \\
47	\quad FK & $
…[truncated 4982 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 3626 · 2026-05-22T08:45:11.256630+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/struct_self_consist_ie/**/config*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/struct_self_consist_ie/**/config*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1"
  }
}
```

</details>

---


### Tool result

_source line 3627 · 2026-05-22T08:45:11.658416+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 3628 · 2026-05-22T08:45:11.709008+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_issues.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 3629 · 2026-05-22T08:45:11.809890+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 3630 · 2026-05-22T08:45:15.282204+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 3631 · 2026-05-22T08:45:15.684414+00:00_

1	issues:
2	- id: R1-N1
3	  summary: "θ_crit=0.70 阈值缺乏 held-out 验证"
4	  category: method
5	  severity: warning
6	  status: in_progress
7	  first_raised_round: 33
8	  last_seen_round: 33
9	  mentions:
10	    - round: 33
11	      reviewers: [1]
12	      note: "R1 认为 Must-Fix（post-hoc fitting 风险）；R2 反驳称有 Corollary 1 理论支撑，降级为 Should-Fix。共识：理论基础 sound 但缺 held-out validation 和 sensitivity sweep。"
13	  action_items:
14	    - round: 33
15	      action: "Agent CPU: sweep θ∈{0.60,0.65,0.70,0.75,0.80}，检查 Table 31 结论稳定性；在 RE 上验证"
16	      assigned_to: agent
17	      status: in_progress
18	  resolution: ""
19	  resolution_round: null
20	
21	- id: R1-N3
22	  summary: "Entity construction 作为 prescriptive contribution 证据不足"
23	  category: experiment
24	  severity: warning
25	  status: in_progress
26	  first_raised_round: 33
27	  last_seen_round: 33
28	  mentions:
29	    - round: 33
30	      reviewers: [1, 2]
31	      note: "双方共识：(a) 阈值 k per-dataset 优化无部署策略；(b) Holm-Bonferroni 全局校正后多数 construction 结果不显著；(c) CoNLL 无增益。"
32	  action_items:
33	    - round: 33
34	      action: "Paper Agent: 降级 construction 为 exploratory result；加 Xie et al. (2023) 对比；§7.5 加 k deployment note"
35	      assigned_to: paper_agent
36	      status: in_progress
37	  resolution: ""
38	  resolution_round: null
39	
40	- id: R2-W1
41	  summary: "Entity-level construction 与 Xie et al. (2023) 差异不清晰"
42	  category: framing
43	  severity: warning
44	  status: in_progress
45	  first_raised_round: 33
46	  last_seen_round: 33
47	  mentions:
48	    - round: 33
49	      reviewers: [1, 2]
50	      note: "双方 AGREE。Section 6.1 和 Section 8 对 Xie et al. (2023) entity voting 的增量贡献阐述不充分。"
51	  action_items:
52	    - round: 33
53	      action: "Paper Agent: 在 §6.1 或 §7.5 增加与 Xie et al. 的显式对比（LP-weighted vs majority voting）"
54	      assigned_to: paper_agent
55	      status: in_progress
56	  resolution: ""
57	  resolution_round: null
58	
59	- id: R2-W3
60	  summary: "Framework vs empirical study 定位模糊"
61	  category: framing
62	  se
…[truncated 4486 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 3632 · 2026-05-22T08:45:15.684903+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/config.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/config.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 3633 · 2026-05-22T08:45:15.785654+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 3634 · 2026-05-22T08:45:23.123950+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/agent"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/agent"
  }
}
```

</details>

---


### Tool result

_source line 3635 · 2026-05-22T08:45:23.224961+00:00_

&lt;tool_use_error>Directory does not exist: /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/agent. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_director_0161122b.&lt;/tool_use_error>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 3636 · 2026-05-22T08:45:27.092807+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie -name \"*.yaml\" -path \"*config*\" 2>/dev/null; find /home/ubuntu/.agent-ml-research-idea_gen_0514_1 -maxdepth 2 -name \"config.yaml\" 2>/dev/null",
  "description": "Find config files for external review settings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie -name \"*.yaml\" -path \"*config*\" 2>/dev/null; find /home/ubuntu/.agent-ml-research-idea_gen_0514_1 -maxdepth 2 -name \"config.yaml\" 2>/dev/null",
    "description": "Find config files for external review settings"
  }
}
```

</details>

---


### Tool result

_source line 3637 · 2026-05-22T08:45:27.394549+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/configs/train_config_fewnerd.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/configs/train_config_fewnerd_5epoch_4gpu.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/configs/train_config_llama_fewnerd_4gpu.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/configs/train_config_llama_fewnerd.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/configs/export_config_qwen25_7b_fewnerd.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/configs/train_config_fewnerd_5epoch.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/configs/export_config_llama.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/configs/train_config_rank8.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/configs/export_config_qwen25_7b_wnut17.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/configs/export_config_v2.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/configs/export_config_qwen25_14b_fewnerd.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/configs/train_config_qwen25_32b_fewnerd_s42.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/configs/export_config_fewnerd.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/configs/train_config_conll2003_4b.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/configs/export_config_conll2003.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projec
…[truncated 3456 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 3638 · 2026-05-22T08:45:39.494956+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1 -maxdepth 1 -name \"*.yaml\" -o -name \"*.yml\" | head -20; find /home/ubuntu/agent-ml-research -name \"projects.yaml\" -o -name \"config.yaml\" 2>/dev/null | head -10",
  "description": "Find project config for external review setting"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1 -maxdepth 1 -name \"*.yaml\" -o -name \"*.yml\" | head -20; find /home/ubuntu/agent-ml-research -name \"projects.yaml\" -o -name \"config.yaml\" 2>/dev/null | head -10",
    "description": "Find project config for external review setting"
  }
}
```

</details>

---


### Tool result

_source line 3639 · 2026-05-22T08:45:39.696293+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/workspace.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 3640 · 2026-05-22T08:45:42.258806+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/workspace.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/workspace.yaml"
  }
}
```

</details>

---


### Tool result

_source line 3641 · 2026-05-22T08:45:42.460394+00:00_

1	projects: {}
2	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 3642 · 2026-05-22T08:46:16.197293+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "struct_self_consist_ie",
  "review_chat_id": "oc_3897c2857f11615119e277e820eae311"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "review_chat_id": "oc_3897c2857f11615119e277e820eae311"
  }
}
```

</details>

---


### Tool result

_source line 3643 · 2026-05-22T08:46:39.854940+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 23657
}
```

</details>

---


### Tool call

_source line 3644 · 2026-05-22T08:46:40.005978+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "34",
  "text": "你是 Reviewer 1，负责审查方法严谨性和实验设计。\n\n## 目标 Venue\n- **EMNLP 2026 Main Conference**（通过 ARR May 2026 统一审稿）\n- 截止日期：2026-05-25\n- Long paper：正文 8 页限制 + 无限参考文献页\n- Mandatory Limitations section（不计入页数）\n- Double-blind review\n- ACL 模板（\\usepackage[review]{acl}）\n\n## 论文信息\n- **标题**: \"Characterizing the Capability Ceiling of Self-Consistency: A Diagnostic Framework for Test-Time Aggregation in NER\"\n- **论文路径**: `projects/struct_self_consist_ie/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_round_34/submitted.pdf`\n\n## 你的审查侧重\n\n**方法严谨性 + 实验设计**，具体包括：\n\n1. **Diagnostic Cascade 逻辑完备性**：四阶段 cascade（QE → degeneracy → agreement fidelity → LP compression）的推导是否完整？各阶段之间是否存在循环论证或遗漏的混淆变量？cascade 是否真的是 diagnostic（论文声称不是 predictive），还是暗含因果主张？\n\n2. **统计检验**：\n   - Holm-Bonferroni 校正的 family 划分（k=10, 21, 9）是否合理？全局校正（k=57）下主要结论是否仍然成立？\n   - Bootstrap confidence intervals 和 paired tests 的使用是否恰当？\n   - Power analysis（n=23 cross-dataset, n=529 SciERC）是否充分讨论了 underpowered 结果的限制？\n   - 3-seed vs 2-seed 的差异是否在正文中充分说明？\n\n3. **实验设计**：\n   - 主要结论依赖 N=8（primary），N=16/32/64 作为 scaling 验证——sample budget 的覆盖是否足够？\n   - Fine-tuning 策略（Few-NERD 3 epochs vs others 5 epochs）对结果的影响是否充分控制？\n   - Constrained decoding 对 degeneracy 的影响是否被低估？论文是否充分讨论了 Yun et al. (2025) diversity collapse 的关系？\n   - θ_crit=0.70 的确定——是 post-hoc fitting 还是有 held-out 验证？Sensitivity sweep 是否充分？\n\n4. **结论泛化性**：\n   - NER → RE/SQL 的扩展是否充分支持论文声称的 \"structured IE\" 泛化？\n   - 模型覆盖（主文聚焦 2 个 8B 模型）vs 论文声称的跨规模/跨家族一致性——证据链是否完整？\n   - GPT-5.5 结果（200 instances, zero-shot only）的代表性如何？\n\n5. **Entity-level Construction 的 prescriptive claim**：\n   - 论文将其定位为 \"exploratory\"，但叙事上是否过度暗示了可操作性？\n   - θ=2/N 的选择和 per-dataset 优化是否存在部署策略缺失？\n   - Gains（+0.32 to +1.40 pp）的实际意义如何？是否值得 N× 推理开销？\n\n请按 ARR 审稿标准给出完整审稿意见，包含：Strengths、Weaknesses（Must-Fix / Should-Fix / Minor 分级）、Questions、Missing References。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "34",
    "text": "你是 Reviewer 1，负责审查方法严谨性和实验设计。\n\n## 目标 Venue\n- **EMNLP 2026 Main Conference**（通过 ARR May 2026 统一审稿）\n- 截止日期：2026-05-25\n- Long paper：正文 8 页限制 + 无限参考文献页\n- Mandatory Limitations section（不计入页数）\n- Double-blind review\n- ACL 模板（\\usepackage[review]{acl}）\n\n## 论文信息\n- **标题**: \"Characterizing the Capability Ceiling of Self-Consistency: A Diagnostic Framework for Test-Time Aggregation in NER\"\n- **论文路径**: `projects/struct_self_consist_ie/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_round_34/submitted.pdf`\n\n## 你的审查侧重\n\n**方法严谨性 + 实验设计**，具体包括：\n\n1. **Diagnostic Cascade 逻辑完备性**：四阶段 cascade（QE → degeneracy → agreement fidelity → LP compression）的推导是否完整？各阶段之间是否存在循环论证或遗漏的混淆变量？cascade 是否真的是 diagnostic（论文声称不是 predictive），还是暗含因果主张？\n\n2. **统计检验**：\n   - Holm-Bonferroni 校正的 family 划分（k=10, 21, 9）是否合理？全局校正（k=57）下主要结论是否仍然成立？\n   - Bootstrap confidence intervals 和 paired tests 的使用是否恰当？\n   - Power analysis（n=23 cross-dataset, n=529 SciERC）是否充分讨论了 underpowered 结果的限制？\n   - 3-seed vs 2-seed 的差异是否在正文中充分说明？\n\n3. **实验设计**：\n   - 主要结论依赖 N=8（primary），N=16/32/64 作为 scaling 验证——sample budget 的覆盖是否足够？\n   - Fine-tuning 策略（Few-NERD 3 epochs vs others 5 epochs）对结果的影响是否充分控制？\n   - Constrained decoding 对 degeneracy 的影响是否被低估？论文是否充分讨论了 Yun et al. (2025) diversity collapse 的关系？\n   - θ_crit=0.70 的确定——是 post-hoc fitting 还是有 held-out 验证？Sensitivity sweep 是否充分？\n\n4. **结论泛化性**：\n   - NER → RE/SQL 的扩展是否充分支持论文声称的 \"structured IE\" 泛化？\n   - 模型覆盖（主文聚焦 2 个 8B 模型）vs 论文声称的跨规模/跨家族一致性——证据链是否完整？\n   - GPT-5.5 结果（200 instances, zero-shot only）的代表性如何？\n\n5. **Entity-level Construction 的 prescriptive claim**：\n   - 论文将其定位为 \"exploratory\"，但叙事上是否过度暗示了可操作性？\n   - θ=2/N 的选择和 per-dataset 优化是否存在部署策略缺失？\n   - Gains（+0.32 to +1.40 pp）的实际意义如何？是否值得 N× 推理开销？\n\n请按 ARR 审稿标准给出完整审稿意见，包含：Strengths、Weaknesses（Must-Fix / Should-Fix / Minor 分级）、Questions、Missing References。"
  }
}
```

</details>

---


### Tool result

_source line 3645 · 2026-05-22T08:46:57.781430+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 17775
}
```

</details>

---


### Tool call

_source line 3646 · 2026-05-22T08:46:57.932357+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "34",
  "text": "你是 Reviewer 2，负责审查新颖性、完整性和写作质量。\n\n## 目标 Venue\n- **EMNLP 2026 Main Conference**（通过 ARR May 2026 统一审稿）\n- 截止日期：2026-05-25\n- Long paper：正文 8 页限制 + 无限参考文献页\n- Mandatory Limitations section（不计入页数）\n- Double-blind review\n- ACL 模板（\\usepackage[review]{acl}）\n\n## 论文信息\n- **标题**: \"Characterizing the Capability Ceiling of Self-Consistency: A Diagnostic Framework for Test-Time Aggregation in NER\"\n- **论文路径**: `projects/struct_self_consist_ie/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_round_34/submitted.pdf`\n\n## 你的审查侧重\n\n**新颖性 + 完整性 + 写作质量**，具体包括：\n\n1. **Contribution 原创性**：\n   - \"Correlation-selection gap\" 是否是真正新颖的概念？与 Yao et al. (2026) 的 task-level consistency analysis、Yun et al. (2025) 的 diversity collapse、Chen et al. (2023) 的 SC failure modes 之间的增量贡献是否清晰？\n   - Diagnostic cascade 作为方法论贡献——是否有足够的通用性和可复用性？还是只是一组 ad-hoc 的观察？\n   - Entity-level construction（本质是 LP-weighted MBR 解码）相对于 Xie et al. (2023) entity voting 的增量是什么？\n\n2. **论文定位和 Framing**：\n   - 标题用 \"Diagnostic Framework\" 但内容更像深度 empirical study——定位是否准确？\n   - Introduction 的三阶段叙事（Discover → Diagnose → Prescribe）是否一致贯穿全文？\n   - \"Capability ceiling\" 的定义（N≤16 的实际上限）是否太狭窄？\n\n3. **Related Work 覆盖度**：\n   - Section 8（Related Work）是否充分？有无重要遗漏？\n   - 与以下工作的对比是否足够清晰：\n     * MBR decoding for structured NLP（Eikema et al. 2022, 2025）\n     * LLM calibration / uncertainty estimation（Kadavath et al. 2022, Tian et al. 2023）\n     * Yao et al. (2026) consistency for IE\n     * Yun et al. (2025) diversity collapse\n   - 是否有遗漏的 concurrent work 或关键引用？\n\n4. **论文结构和可读性**：\n   - 主文件结构：Abstract → Intro → Diagnostic Framework → Mechanistic → Single Signal → Adaptive → Theory → Experiments → Related Work → Discussion\n   - Experiments（Section 7）在 Section 3-6 展示了大量实验结果之后才出现——这是否影响可读性？\n   - Section 标题是否准确反映内容？\n   - 信息密度是否过高？读者能否在首次阅读时跟上？\n   - 正文是否可能超过 8 页限制？\n\n5. **Limitations 和 Ethics Statement**：\n   - Limitations 是否全面？是否遗漏了重要限制？\n   - Ethics Statement 是否恰当？\n\n6. **写作质量**：\n   - 数学符号是否一致？\n   - Figure/Table 的可读性和信息量\n   - 引用格式是否符合 ACL 规范？\n   - 是否存在匿名性泄露？\n\n请按 ARR 审稿标准给出完整审稿意见，包含：Strengths、Weaknesses（Must-Fix / Should-Fix / Minor 分级）、Questions、Missing References。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "34",
    "text": "你是 Reviewer 2，负责审查新颖性、完整性和写作质量。\n\n## 目标 Venue\n- **EMNLP 2026 Main Conference**（通过 ARR May 2026 统一审稿）\n- 截止日期：2026-05-25\n- Long paper：正文 8 页限制 + 无限参考文献页\n- Mandatory Limitations section（不计入页数）\n- Double-blind review\n- ACL 模板（\\usepackage[review]{acl}）\n\n## 论文信息\n- **标题**: \"Characterizing the Capability Ceiling of Self-Consistency: A Diagnostic Framework for Test-Time Aggregation in NER\"\n- **论文路径**: `projects/struct_self_consist_ie/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_round_34/submitted.pdf`\n\n## 你的审查侧重\n\n**新颖性 + 完整性 + 写作质量**，具体包括：\n\n1. **Contribution 原创性**：\n   - \"Correlation-selection gap\" 是否是真正新颖的概念？与 Yao et al. (2026) 的 task-level consistency analysis、Yun et al. (2025) 的 diversity collapse、Chen et al. (2023) 的 SC failure modes 之间的增量贡献是否清晰？\n   - Diagnostic cascade 作为方法论贡献——是否有足够的通用性和可复用性？还是只是一组 ad-hoc 的观察？\n   - Entity-level construction（本质是 LP-weighted MBR 解码）相对于 Xie et al. (2023) entity voting 的增量是什么？\n\n2. **论文定位和 Framing**：\n   - 标题用 \"Diagnostic Framework\" 但内容更像深度 empirical study——定位是否准确？\n   - Introduction 的三阶段叙事（Discover → Diagnose → Prescribe）是否一致贯穿全文？\n   - \"Capability ceiling\" 的定义（N≤16 的实际上限）是否太狭窄？\n\n3. **Related Work 覆盖度**：\n   - Section 8（Related Work）是否充分？有无重要遗漏？\n   - 与以下工作的对比是否足够清晰：\n     * MBR decoding for structured NLP（Eikema et al. 2022, 2025）\n     * LLM calibration / uncertainty estimation（Kadavath et al. 2022, Tian et al. 2023）\n     * Yao et al. (2026) consistency for IE\n     * Yun et al. (2025) diversity collapse\n   - 是否有遗漏的 concurrent work 或关键引用？\n\n4. **论文结构和可读性**：\n   - 主文件结构：Abstract → Intro → Diagnostic Framework → Mechanistic → Single Signal → Adaptive → Theory → Experiments → Related Work → Discussion\n   - Experiments（Section 7）在 Section 3-6 展示了大量实验结果之后才出现——这是否影响可读性？\n   - Section 标题是否准确反映内容？\n   - 信息密度是否过高？读者能否在首次阅读时跟上？\n   - 正文是否可能超过 8 页限制？\n\n5. **Limitations 和 Ethics Statement**：\n   - Limitations 是否全面？是否遗漏了重要限制？\n   - Ethics Statement 是否恰当？\n\n6. **写作质量**：\n   - 数学符号是否一致？\n   - Figure/Table 的可读性和信息量\n   - 引用格式是否符合 ACL 规范？\n   - 是否存在匿名性泄露？\n\n请按 ARR 审稿标准给出完整审稿意见，包含：Strengths、Weaknesses（Must-Fix / Should-Fix / Minor 分级）、Questions、Missing References。"
  }
}
```

</details>

---


### Tool result

_source line 3647 · 2026-05-22T08:46:59.595311+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1662
}
```

</details>

---


### Tool call

_source line 3648 · 2026-05-22T08:47:09.945342+00:00_

called mcp__agent-ml-research__request_external_review

<details open><summary>🔧 Tool call — mcp__agent-ml-research__request_external_review</summary>

```json
{
  "project": "struct_self_consist_ie",
  "paper_pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_round_34/submitted.pdf",
  "venue": "EMNLP 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__request_external_review",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "paper_pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_round_34/submitted.pdf",
    "venue": "EMNLP 2026"
  }
}
```

</details>

---


### Tool result

_source line 3649 · 2026-05-22T08:47:10.751476+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"pending\", \"message\": \"外部审稿请求已发送到用户群。将在 8 小时后自动提醒。\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__request_external_review",
  "elapsed_ms": 806
}
```

</details>

---


### Assistant

_source line 3650 · 2026-05-22T08:47:24.309906+00:00_

**Round 34 审稿已启动，当前状态：**

| 任务 | 状态 |
|------|------|
| Reviewer 1（方法严谨性 + 实验设计） | 🔄 审稿中 |
| Reviewer 2（新颖性 + 完整性 + 写作） | 🔄 审稿中 |
| 视觉审查 Agent | 🔄 进行中 |
| 外部审稿（Stanford Agentic Reviewer） | 📨 请求已发送，等待用户提交 |

等待 Reviewer 返回初审结果后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 269

## Round 269

6 recorded events


### User

_source line 3651 · 2026-05-22T08:54:19.312197+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿意见：Round 34

**论文**: "Characterizing the Capability Ceiling of Self-Consistency: A Diagnostic Framework for Test-Time Aggregation in NER"
**Venue**: EMNLP 2026 (ARR May 2026)
**审查侧重**: 新颖性、完整性、写作质量

---

## 总体评分
**Overall**: 3.0（Findings）
**一句话总结**: 这是一篇极其详尽的 empirical study，对 self-consistency 在 NER 上失败的原因提供了有价值的诊断分析，但 "Diagnostic Framework" 的定位过高、处方性贡献薄弱、信息密度过大影响可读性，更适合 Findings 而非主会议。

---

## 官方维度打分（ARR 2025 Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 实验设计严谨（bootstrap CI、permutation tests、Holm-Bonferroni 校正），统计实践优秀；但 "framework" 定位超出实际贡献范围，理论命题（Proposition 1-2）依赖较强假设（entity-wise independence），theory 更像事后形式化而非驱动实验设计 |
| Excitement | 3/5 | Correlation-selection gap 是有用的诊断概念，degeneracy decomposition 有实践价值；但核心发现以负面结果为主（SC 对 NER 不太有效），处方性输出有限（entity-level construction 仅在 Few-NERD 上 +1.3pp，CoNLL 上负面），整体新颖性中等 |
| Reproducibility | 4/5 | 附录极其详尽（34页），包含完整的超参数、prompt template、统计检验细节；承诺释放代码和数据；使用公开基准数据集 |
| Reviewer Confidence | 4/5 | 熟悉 self-consistency、MBR decoding、NER 评估方法；仔细阅读了全部 47 页 |

---

## 主要优势

**S1. 极其彻底的实验覆盖。** 4 个英文 NER 数据集（SciERC、CoNLL、Few-NERD、WNUT-17）、2 个模型族（Qwen3-8B、LLaMA-3.1-8B）、9 类方法（Table 2）、16 种配置（Table 12 含 57 项统计检验）。这种覆盖度在 NER + LLM 文献中罕见。附录的 34 页补充分析（Appendix a-ak）提供了几乎所有可能的消融角度。

**S2. 统计严谨性出色。** 全面使用 bootstrap 95% CI（Table 11）、permutation test（Table 15、Table 39）、Holm-Bonferroni 多重比较校正（Table 12）。这种统计规范在 NLP empirical 论文中是标杆级别。Table 12 的 57 项检验清晰区分了 significant vs. non-significant 结果。

**S3. Correlation-selection gap 是有用的诊断概念。** 将 quality estimation（信号与质量的相关性）和 selection（实际选出更好输出的能力）之间的脱节命名并系统分析，为理解 SC 在结构化任务上的局限提供了清晰的分析框架。Figure 2 的可视化有效展示了这个 gap。

**S4. 实用的负面结论。** Section 9 的 diagnostic cascade 提供了一个可操作的预部署决策树：先测 degeneracy，再测 LP-F1 alignment，据此决定是否值得做 aggregation。这对工程实践有直接价值（Section 9: "practical implications"）。

**S5. Entity-level construction 与 MBR 的形式化连接。** Proposition 2 将 entity-level construction 形式化为 LP-weighted MBR 在 entity-wise independence 假设下的特例，建立了与 MBR 文献（Eikema and Aziz, 2022; Eikema et al., 2025）的理论桥梁。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] **标题和定位 "Diagnostic Framework" 超出实际贡献**
- 具体位置：Title、Abstract、Section 1（"We trace this failure through three stages of investigation"）
- 问题：标题声称提出了一个 "Diagnostic Framework"，但论文实际内容是一组深入的 empirical observations，以事后组织的四阶段 cascade 呈现。一个 "framework" 应具备（a）明确的定义和可操作步骤，（b）在其他任务/领域的通用性，（c）预测能力。当前的 cascade（QE → degeneracy → selection alignment → entity-level construction）更像一组 ad hoc 的分析步骤，不同阶段之间没有形式化的决策边界（例如，degeneracy 的阈值 D=0.05 来自哪里？见 Appendix p.3 Corollary 1，但其依赖 entity-wise independence 假设）。
- 为什么影响接收：reviewer 和 reader 会期望一个可复用的 framework，但实际得到的是一组 NER-specific 的观察。这种定位-内容错位会引起所有 reviewer 的关注。
- 建议修改方向：将标题改为 empirical study / diagnostic analysis 的定位，如 "Why Self-Consistency Fails for NER: A Diagnostic Analysis of Test-Time Aggregation"。Section 1 的 "Discover → Diagnose → Prescribe" 叙事也需要调整——当前 "Prescribe" 阶段的产出（entity-level construction 仅 +1.3pp 且仅在 Few-NERD 有效）不足以支撑 prescriptive 的声明。

**N2** [critical] **Prescriptive contribution 薄弱，削弱三阶段叙事**
- 具体位置：Section 1（"Prescribe"）、Section 6.1（Entity Construction）、Section 7.5、Table 65（Appendix p.45）
- 问题：Introduction 承诺了 "Discover → Diagnose → Prescribe" 三阶段叙事，但 Prescribe 阶段的核心产物——entity-level construction——实际效果有限：Few-NERD +1.4pp（Table 4），CoNLL -0.85pp，SciERC +0.2pp。Table 65 的 cost-benefit 分析显示 entity construction 是唯一在所有数据集上 consistently positive 的策略，但绝对增益很小。更关键的是，Section 9 的结论本质上是 "what NOT to do"（别用 SC for NER）而非 "what to do"——这是 diagnostic study 而非 prescriptive framework 的结论。
- 为什么影响接收：三阶段叙事是论文的核心组织原则。如果 Prescribe 阶段不成立，整篇论文的叙事结构就不完整。
- 建议修改方向：（a）诚实地将论文定位为以 Discover + Diagnose 为主、Prescribe 为探索性初步结果的工作；（b）或加强 prescriptive 部分——例如结合 degeneracy detection 和 entity-level construction 的 adaptive pipeline，在更多设置下验证。

**N3** [critical] **新颖性增量 vs. 相关工作不够清晰**
- 具体位置：Section 8（Related Work）、Section 1
- 问题：论文的核心贡献相对于以下工作的增量需要更清晰地阐述：
  1. **Yao et al. (2026)**：已研究 consistency for structured IE。论文 Section 8 称 "Yao et al. (2026) demonstrate task-level correlation (ρ up to 0.47) between consistency and quality across NERRE tasks"——那么本文的 instance-level 分析增量在哪？需明确说明 Yao 的分析停在 task-level 而本文深入到 instance-level + entity-level。
  2. **Chen et al. (2024)**：已识别 SC failure modes（hypothetical + compositional consistency）。本文的 correlation-selection gap 与他们的发现之间的关系是什么？
  3. **Xie et al. (2023)**：已在 NER 上做了 entity voting。本文的 entity-level construction 本质上是对 Xie 的 entity voting 加上 LP weighting——这个增量的幅度需要更直接地说明。
  4. **Yun et al. (2025)**：diversity collapse 与本文的 degeneracy 概念高度相关。Section 8 有一段讨论但关系仍不够清晰——degeneracy（所有 N 个样本相同）是 diversity collapse 的极端情况还是不同现象？
- 为什么影响接收：如果 reviewer 认为贡献是已有工作的组合/延伸，而非真正新颖的概念，Overall 评分会显著下降。
- 建议修改方向：在 Introduction 或 Section 2 开头明确用 2-3 句话说明 "与 X 不同，我们的贡献在于 Y"，而非留到 Section 8。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] **论文结构非常规，实验结果分散在 Sections 3-7 中，影响可读性**
- 具体位置：Sections 3（How Self-Verification Fails）、4（Where Single-Signal Selection Fails）、5（Adaptive Methods）、6（Threshold Regime Analysis）、7（Experiments）
- 问题：Sections 3-6 每节都包含大量实验结果（Table 1、Figure 2、Table 2、Figure 3 等），但正式的 Experimental Setup（Section 7.1）直到第 6 页才出现。读者在前 5 页遇到实验数据时缺乏 setup 上下文（数据集、模型、超参数、评估指标等）。Section 7 标题是 "Experiments"，但此时大量结果已经展示完毕——Section 7 更像是 "Additional Experiments" 或 "Aggregated Results"。
- 建议：将 Section 7.1（Experimental Setup）提前到 Section 2 之后，或在 Section 2.3 扩展 evaluation setup；重命名 Section 7 为更准确的标题。

**W2** [warning] **信息密度过高，首次阅读难以跟上**
- 具体位置：全文，尤其 Sections 4-6
- 问题：几乎每个句子都包含 2-3 个数字或统计量。例如 Section 4（p.4）："Despite ρ up to 0.38, no signal outperforms greedy on SciERC (Table 1); Figure 2's oracle shows 11.4 pp headroom, but LP achieves +0.2 pp (p=0.29), below MDE (=1.5 pp, n=529; Table S5)." 这种密度要求读者同时追踪多个数字和引用。加上大量缩写（LP、SJ、FK、VC、EM、RE、MV、QE、AUROC 等），认知负荷极高。
- 建议：（a）主文聚焦 top-level patterns，将详细数字移入 appendix；（b）减少主文中的 inline statistics，用更多叙述性语言引导读者理解 what the numbers mean 而非仅呈现 what the numbers are。

**W3** [warning] **"Capability ceiling" 定义较窄且缺乏充分论证**
- 具体位置：Section 2（p.2, "We define the capability ceiling as the practical performance upper bound achievable through self-consistency at realistic sample budgets (N ≤ 16)"）
- 问题：N≤16 的选择看似任意。为什么不是 N=32 或 N=64？论文在 Section 6.2（p.5）展示了 scaling 到 N=64 的数据，发现 "beyond which diminishing returns render further scaling impractical"——但这说的是 Few-NERD，CoNLL 和 SciERC 的 ceiling 在哪？如果 ceiling 是 dataset-dependent 的（论文自己的结论），那用一个固定的 N≤16 来定义 "capability ceiling" 就有概念张力。
- 建议：要么放弃固定的 N 阈值，改为 dataset-specific 的 diminishing returns 分析；要么更充分论证 N=16 作为 practical budget 的普遍性（inference cost、latency 等）。

**W4** [warning] **Proposition 1 和 2 的理论贡献定位模糊**
- 具体位置：Section 6.3（Degeneracy Decomposition, p.5）、Appendix p（Proposition 2 proof, p.29-31）
- 问题：两个 Proposition 都依赖较强假设。Proposition 1（Entity Selection Diagnostic）假设 entity-wise independence 和 binary presence；Proposition 2（entity construction 作为 MBR 特例）同样假设 entity-wise independence。论文承认 "The independence assumption is approximate"（p.6）。这些命题更接近 "在简化假设下的性质刻画" 而非 "驱动实验设计的理论框架"——实际实验并未基于这些命题来设计，而是反过来用命题来事后解释实验观察。
- 建议：将理论贡献明确定位为 "formalization of empirical observations" 而非暗示 "theoretical framework driving the analysis"。

**W5** [warning] **Degeneracy 在 CoNLL 上极高（38%-89%），削弱 selection failure 发现的 interestingness**
- 具体位置：Section 4（p.4, "On degenerate instances..."）、Table 13（Appendix p.19）、Section 7.3（p.7）
- 问题：在 CoNLL 上，LLaMA 的 degeneracy 为 89%（Table 13），意味着 89% 的 instances 所有 N 个输出完全相同——selection 在这些 instances 上 trivially 无法改进。这使得 "selection fails on CoNLL" 的发现部分变成了 "模型已经足够好、没什么可改进空间" 的 tautology。论文在 Section 4 中提到了这一点但未充分讨论其对核心 claim 的影响。Few-NERD 的低 degeneracy（13%）使其成为更有 informativeness 的测试平台，但 CoNLL 和 WNUT-17 的高 degeneracy 使论文在这些数据集上的发现打了折扣。
- 建议：在 Section 4 或 7 中增加一段明确讨论：在什么条件下 selection failure 是 genuine failure（低 degeneracy 时）vs. trivial outcome（高 degeneracy 时），并按此区分不同数据集上发现的 weight。

**W6** [warning] **Related Work（Section 8）位置和覆盖度**
- 具体位置：Section 8（p.8）
- 问题：（a）Related Work 放在 Discussion 之前，但在 Sections 3-7 展示大量结果之后才出现。读者在读 Section 3 时可能就想知道 "这和 Chen et al. 2024 的 SC failure modes 有什么关系？"——但要等到 page 8 才得到答案。（b）以下工作的讨论可加强：
  - **Snell et al. (2025)** "Scaling LLM Test-Time Compute Optimally" (ICLR 2025)：该工作提出 compute-optimal 策略，核心思想是 per-prompt adaptive allocation——这与本文发现的 dataset-dependent optimal strategy 在概念上高度相关，但 Section 8 未明确讨论。
  - **Eikema et al. (2025)** Structure-conditional MBR：论文引用了但未充分讨论其 structure-conditional utility function 与 entity-level construction 的关系——两者都试图让 MBR 感知结构化输出空间的 variability。
  - Calibration 文献：LP 作为 quality signal 本质上是 calibration 问题，与 Kadavath et al. (2022)、Tian et al. (2023) 等 LLM calibration 工作的联系可以更深入。
- 建议：（a）考虑将关键 positioning 前移到 Introduction；（b）加强上述 3 组工作的对比讨论。

---

## 小问题（不影响接收）

- **M1** 页数边界情况：Section 9（Discussion and Conclusion）的最后 2-3 行溢出到 PDF 第 9 页顶部，Limitations 紧随其后。虽然 Limitations 不计入 8 页限制，但主文结论文本略微溢出——建议确认在 camera-ready 版本中严格控制在 8 页内。
- **M2** Figure 1 的 "diagnostic; not causal chain" 注释（p.3）值得赞赏，但图中的箭头视觉上仍暗示因果链。建议用虚线箭头或其他视觉手段明确区分诊断关联和因果关系。
- **M3** Section 2.2 引入了 6 个信号缩写（SJ, VC, FK, EM, LP, RE），加上已有的 MV、QE、AUROC 等，缩写负担过重。建议在首次定义后的 Table 5（Appendix p.14）的内容以简化版放在主文中以方便查阅。
- **M4** Table 2（p.5）的 "Full coverage in Appendix h.4" 引用——附录 h.4 是 method coverage matrix（Table 17, p.21），但主文没有说明 9 类方法中哪些在哪些数据集上测试了。读者需要翻到 p.21 才能获得这个信息。
- **M5** 引用格式：Section 1 "Wang et al., 2023; best-of-N with learned verifiers (Cobbe et al., 2021; Brown et al., 2024)" 中 Brown et al. 2024 应为 "(Brown et al., 2024)"——检查全文括号引用的一致性。
- **M6** 匿名性：未发现明显的匿名性泄露。论文使用 "Anonymous ACL submission"，工具引用（LLaMA Factory 等）均为公开工具。
- **M7** Ethics Statement（p.9-10）覆盖恰当。Responsible NLP Checklist 回答完整。

---

## Limitations 评估

Section 9 的 Limitations 覆盖了：（a）仅使用 correlation 和 theoretical decomposition，无 controlled intervention；（b）scope 限于 NER + 英文 + 开源模型；（c）cascade stages 可能交互。

**遗漏的 limitation**：
1. **仅测试 8B 参数级别模型**：论文未讨论 larger models（70B+）是否有不同的 degeneracy/selection patterns。在 LLM scaling 语境下这是重要的外部效度问题。
2. **Temperature 设置单一**：主要实验使用 T=1.0，虽然附录（Table 6, p.14; Appendix u, p.37）有 temperature 敏感性分析，但 Limitations 中未讨论 temperature 选择对核心结论的影响。
3. **Prompt sensitivity**：论文使用特定的 prompt template（Appendix k, p.22），但 NER 对 prompt 格式高度敏感（Yun et al., 2025 也指出格式对 diversity 的影响）。未讨论 prompt 变化对 degeneracy 和 selection 的影响。

---

## Questions for Authors

**Q1**: Diagnostic cascade 的四个阶段是否有 formal 的决策边界？例如，degeneracy 率达到多少时应直接放弃 SC？Corollary 1 给出了 D < 1 - ε/(G_nd * n_f) 的条件，但实际应用中 G_nd 和 n_f 本身需要 oracle 标注才能计算——这如何在无标注 deployment 场景下使用？

**Q2**: Entity-level construction 在 CoNLL 上为负面（-0.85pp）——是否有 per-entity-type 的分析可以解释哪些 entity types 受损？Table 51（Appendix p.39）提供了 Few-NERD 的 per-entity-type LP 选择分析，CoNLL 是否有类似分析？

**Q3**: 论文在 Few-NERD 上展示了 entity-level construction 的最大收益（+1.4pp）——如果结合 degeneracy filtering（仅对非 degenerate instances 做 construction），收益是否更大？

**Q4**: 关于 generalizability：diagnostic cascade 是否适用于其他结构化预测任务（RE、event extraction、slot filling）？有无初步证据？Appendix o（p.28）有 RE 的探索性扩展，但仅限于 SciERC——是否可以提供更系统的跨任务验证？

---

## Missing References

1. **Snell et al. (2025)** "Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters" (ICLR 2025)——compute-optimal test-time scaling 的开创性工作，与本文的 dataset-dependent optimal strategy 发现高度相关。
2. 论文引用了 Eikema et al. (2025) 但未充分对比其 structure-conditional MBR 思想与 entity-level construction 的关系。建议在 Section 6.1 或 Section 8 中深化这个讨论。

---

**总结**: 这是一篇非常扎实的 empirical study，统计实践堪称模范，47 页的分析深度令人印象深刻。核心的 correlation-selection gap 发现对社区有价值。主要问题在于（1）"Framework" 的定位超出了实际贡献——更准确的定位是 diagnostic empirical study；（2）prescriptive 阶段的产出（entity-level construction）效果有限，无法支撑三阶段叙事的完整性；（3）相对于 Yao et al. (2026)、Chen et al. (2024)、Xie et al. (2023) 的增量贡献需要更清晰地阐明。修正这些定位和叙事问题后，论文的 Findings 接收前景较好。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 3652 · 2026-05-22T08:54:24.818328+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:TodoWrite",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:TodoWrite",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 3653 · 2026-05-22T08:54:24.919193+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 3654 · 2026-05-22T08:54:30.942837+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': '收集 Reviewer 1 审稿意见', 'status': 'in_progress', 'activeForm': '等待 Reviewer 1 审稿意见'}, {'content': '收集 Reviewer 2 审稿意见', 'status': 'completed', 'activeForm': '已收到 Reviewer 2 审稿意见'}, {'content': '交叉分享：将 R1 意见转发给 R2，R2 意见转发给 R1', 'status': 'pending', 'activeForm': '执行交叉分享'}, {'content': '收敛判断：分析共识与分歧', 'status': 'pending', 'activeForm': '分析收敛情况'}, {'content': '合成最终报告并投递', 'status': 'pending', 'activeForm': '合成并投递审稿报告'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': '收集 Reviewer 1 审稿意见', 'status': 'in_progress', 'activeForm': '等待 Reviewer 1 审稿意见'}, {'content': '收集 Reviewer 2 审稿意见', 'status': 'completed', 'activeForm': '已收到 Reviewer 2 审稿意见'}, {'content': '交叉分享：将 R1 意见转发给 R2，R2 意见转发给 R1', 'status': 'pending', 'activeForm': '执行交叉分享'}, {'content': '收敛判断：分析共识与分歧', 'status': 'pending', 'activeForm': '分析收敛情况'}, {'content': '合成最终报告并投递', 'status': 'pending', 'activeForm': '合成并投递审稿报告'}]"
  }
}
```

</details>

---


### Tool result

_source line 3655 · 2026-05-22T08:54:30.943270+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Assistant

_source line 3656 · 2026-05-22T08:54:35.602437+00:00_

Reviewer 2 意见已收到（Overall 3.0 / Findings）。3 个 Must-Fix（框架定位过高、处方性贡献薄弱、与相关工作增量不清晰）+ 6 个 Should-Fix + 7 个 Minor。等待 Reviewer 1 返回后进行交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 270

## Round 270

2 recorded events


### User

_source line 3657 · 2026-05-22T08:54:43.353827+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

**审稿摘要**：
- **Overall: 3.0（Findings）**，Soundness 3.5/5，Excitement 3/5
- **3 个 Must-Fix**：（1）"Diagnostic Framework" 定位超出实际贡献，更适合定位为 empirical study；（2）Prescribe 阶段产出薄弱（entity-level construction 仅 Few-NERD +1.3pp），三阶段叙事不完整；（3）相对于 Yao et al. 2026、Chen et al. 2024、Xie et al. 2023 的增量贡献界定不清
- **6 个 Should-Fix**：结构非常规（实验结果分散在 Sections 3-7）、信息密度过高、"capability ceiling" N≤16 定义狭窄、理论命题定位模糊、CoNLL 高 degeneracy 削弱发现的 interestingness、Related Work 位置和覆盖度
- **核心判断**：统计实践堪称模范、47 页分析深度令人印象深刻，但定位-内容错位和中等新颖性使其更适合 Findings

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 3658 · 2026-05-22T08:54:48.697567+00:00_

Reviewer 2 意见已收到。继续等待 Reviewer 1。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 271

## Round 271

8 recorded events


### User

_source line 3659 · 2026-05-22T08:54:55.139831+00:00_

[Reviewer 1 审稿意见]:

## 总体评分
**Overall**: 3.5 / 5（Borderline Conference）
**一句话总结**: 一篇严谨且透明的诊断分析论文，四阶段 cascade 框架对理解 SC 在结构化 IE 中的失败模式有真实贡献，但核心统计主张在全局校正下不成立，模型/任务覆盖面不足以支撑泛化声明，prescriptive 部分增益有限。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 诊断框架逻辑完整，实验设计细致，但核心 NER selection claim 在全局 Holm-Bonferroni (k=57) 下 p_HB=0.055 未达显著；家族划分合理但非唯一选择；θ_crit=0.70 缺少 held-out 验证 |
| Excitement | 3/5 | 对 SC 在结构化任务中的系统性诊断是有价值的贡献；但主要是分析性工作，prescriptive 输出（entity-level construction +0.32–1.40pp）增益有限且需 N× 推理开销 |
| Reproducibility | 4/5 | 承诺释放代码和数据；47 页 Appendix 提供了极其详尽的实验细节、超参数、统计检验；少数选择（θ_crit 确定过程、Few-NERD 3-epoch 决策）文档可更完整 |
| Confidence | 4/5 | 完整阅读全部 47 页（正文 + 39 页 Appendix），逐项核查统计声明、表格数据、方法论细节 |

## 主要优势

**S1. 系统性诊断框架的原创贡献。** 四阶段 cascade（QE → degeneracy → agreement fidelity → LP compression）是对 SC 在结构化 IE 中失败模式的首次系统分类。每个阶段有清晰的操作定义和可计算的指标（Section 2–4），诊断流程 actionable，可直接指导实践者判断 SC 在特定配置下是否值得尝试。

**S2. 统计方法的严谨性和透明度。** 论文展现了罕见的统计诚实：报告了 Holm-Bonferroni 校正（Table 12, k=57）、bootstrap CIs（Table 11）、TOST 等价检验（Table 15）、permutation tests（Table 7, FK independence）、post-hoc power analysis（Table 58）。尤其是 Table 12 明确承认全局校正下核心 claim 不达显著（p_HB=0.055），这种透明度值得肯定。

**S3. 极其充实的补充材料。** 39 页 Appendix 覆盖了温度敏感性（Table 6, Appendix b）、sample size scaling（Tables 35–37, Appendix s）、free-form decoding 消融（Tables 33–34, Appendix q）、cross-family 验证（Table 44, Appendix t）、14B scale 扩展（Table 41, Appendix x）、epoch confound（Table 55, Appendix ab）等，几乎穷尽了 reviewer 可能提出的消融需求。

**S4. 清晰的 observational 定位。** 论文在 Section 2 开头即声明 "our analysis is observational: we characterize statistical associations...without claiming causal mechanisms"，在 Limitations（p9）中重申 "not interventional"，避免了因果过度声明。

**S5. 实用的 degeneracy 诊断洞见。** θ_crit=0.70 的发现（当 >70% 实例退化时 SC 失效）和 LP 作为最强 per-sample 信号的识别（across 4 datasets, 2 model families）具有直接的实践指导价值。

## Must-Fix 问题（影响接收决定）

**N1** [critical] 全局 Holm-Bonferroni 校正下核心 NER 主张不成立，但主文未充分讨论
- 具体位置：Table 12（p25–26, Appendix e）vs. 正文 Section 4, 7
- 问题：Table 12 显示在 k=57 全局校正下，"no core NER claim survives"（p_HB=0.055 for Few-NERD LP selection and construction）；仅两个外围测试（CoNLL few-shot entity entropy, RE LP selection reversal）达到显著。正文 Section 4 和 Section 7 使用的是 family-wise corrected p-values（k=10, 21, 9 等较小的家族），但未在正文中明确告知读者全局校正结果。Appendix e 第 18 页虽然报告了这一事实，但作为影响论文核心结论可信度的关键信息，应在正文（至少在 Discussion §8 或 Limitations）中显著讨论。
- 为什么影响接收：论文的核心量化声明（"LP best-of-N yields +1.39 pp on Few-NERD", "degeneracy predicts LP gain across datasets p=0.002"）的统计显著性取决于家族划分策略。如果 reviewer 或 AC 认为全局校正更合适（multiple testing 文献中有此立场），论文的主要 empirical contribution 将失去统计支撑。
- 建议修改方向：(1) 在正文 Discussion 或 Limitations 中用 1-2 句话明确报告全局校正结果；(2) 为 family-wise 分组提供更强的先验理由（如基于研究问题的独立性论证），而非仅在 Appendix 中作为 robustness check 呈现；(3) 考虑报告 false discovery rate (FDR) 作为 Holm-Bonferroni 的补充。

**N2** [critical] θ_crit=0.70 缺少 held-out 验证，存在 post-hoc fitting 风险
- 具体位置：Section 4（p4）, Section 6.1（p5）, Appendix ab.7（Table 62, p43）
- 问题：θ_crit=0.70 是论文最具 prescriptive 价值的量化结论之一（"θ_crit=0.70 predicts when aggregation gains vanish"）。但该阈值是从同一组数据中确定并验证的。Appendix ab.7 Table 62 提供了 sensitivity sweep（θ 从不同值变化），Appendix ak.1 提到 LOO cross-validation，但 LOO-CV 的结果未明确报告为完整的交叉验证 curve。Figure 10（p31）展示了 SC gain vs. degeneracy 的散点图及拟合，但 16 个配置点既用于拟合又用于声称泛化。
- 为什么影响接收：如果 θ_crit=0.70 是 post-hoc 拟合结果而非稳健的预测阈值，则 Section 4 和 Discussion 中关于 "when aggregation is unlikely to help" 的 prescriptive 建议缺乏方法论支撑。这动摇了框架从 "diagnostic" 到 "prescriptive" 的核心升级。
- 建议修改方向：(1) 明确报告 LOO-CV 或 k-fold CV 的完整结果（如每个 fold 的 θ_crit 变异范围）；(2) 使用一个 dataset 作为 held-out 验证集（如在 3 个 NER dataset 上拟合，在第 4 个上验证）；(3) 如果验证不充分，将 θ_crit=0.70 明确降级为 "descriptive summary of our data" 而非 predictive threshold。

**N3** [critical] 模型覆盖面不足以支撑 "跨规模/跨家族一致性" 声明
- 具体位置：Section 7（p6–7）, Table 3（p4）, Table 44（p36）, Limitations（p9）
- 问题：正文主要依赖两个 8B fine-tuned 模型（Qwen3-8B, LLaMA-3.1-8B）。跨家族验证（Table 44）增加了 Qwen2.5-7B Instruct 和 GPT-5.5，但后两者仅 zero-shot（无 fine-tuning），且 GPT-5.5 仅 200 instances。14B 扩展（Appendix x, Table 41）仅在 SciERC 上。72B 实验（Table 64, p45）仅 Qwen2.5-72B-Instruct-AWQ 的 zero-shot。Abstract 和 Section 1 声称 "treating NER as a representative instance of set-valued generation"，Section 6.2 声称 "the gap persists across scales and families"，但实际的模型规模范围基本锁定在 7–8B，且 zero-shot vs fine-tuned 的对比不对等。
- 为什么影响接收：Reviewer 可能质疑：在更大规模（70B+）fine-tuned 模型上，degeneracy 模式是否仍然成立？Table 44 的 cross-family 分析（p36）显示 "all four frontier families exhibit the correlation-selection gap"，但 GPT-5.5 的 200-instance zero-shot 证据太薄。47B+/70B+ fine-tuned 实验的缺失限制了泛化声明的可信度。
- 建议修改方向：(1) 在正文中明确限定 claim 范围为 "7–14B fine-tuned + selected zero-shot frontier models"；(2) 将 "cross-scale consistency" claim 降级为 tentative observation；(3) 如果资源允许，补充一个 ≥30B fine-tuned 模型的实验。

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Free-form decoding 消融仅覆盖 SciERC，高退化数据集（CoNLL 67.7%, WNUT-17）缺失
- 具体位置：Appendix q（Tables 33–34, p32–33）
- 问题：Constrained decoding（vLLM structured decoding）贯穿全部实验。Free-form 消融仅在 SciERC 上执行（低退化 dataset）。SciERC 结果显示 LP compression persists under free-form，但 CoNLL（67.7% 退化率）和 WNUT-17 的 free-form 行为未验证。如果 constrained decoding 是 CoNLL 高退化率的主要驱动因素（而非模型能力本身），则 cascade 中 degeneracy 阶段的诊断价值将被高估。
- 建议：至少在 CoNLL 上补充 free-form ablation，或在正文中明确讨论 constrained decoding 可能放大 degeneracy 的机制及其对 cascade 诊断有效性的影响。

**W2** [warning] 2-seed vs 3-seed 差异未充分说明
- 具体位置：Table 1 caption（p4）："Selection signals: 2-seed mean±σ; baselines: 3-seed"
- 问题：主表（Table 1）中 selection signals 使用 2-seed mean，baselines 使用 3-seed，但正文未解释这一不对称的原因（计算资源限制？某个 seed 失败？）。Appendix j（p22）确认了 3-seed stability，但主表的 2-seed 基础可能引入 seed selection bias。
- 建议：在正文或 Appendix 中明确说明为什么 selection signals 使用 2 seeds。如果是资源约束，直接说明；如果有第三个 seed 的结果但未包含，解释原因。

**W3** [warning] Entity-level construction 的 "exploratory" 定位与叙事张力
- 具体位置：Section 7.5（p8）标记为 "exploratory"，但 Abstract（"entity-level construction (+0.32–1.40 pp)"）和 Discussion（§8, p8）以 prescriptive 口吻呈现
- 问题：Abstract 将 entity-level construction 列为三大贡献之一（"Prescribe"），Discussion 称 "entity-level construction offers modest but reliable gains"，而 Section 7.5 称 "exploratory"。Table 65（p45）显示 cost-benefit：entity construction 是唯一正增益策略，但需 N× 推理开销。θ=2/N 的选择在 Table 62 中显示 per-dataset sensitivity，但无统一的 deployment 策略。叙事上的不一致可能让读者困惑于该结果的可操作性。
- 建议：统一叙事定位——要么在 Abstract/Discussion 中也标记为 "exploratory with promising initial results"，要么升级 Section 7.5 的分析深度以匹配 prescriptive claim（如补充跨 dataset 的 θ 自动选择策略）。

**W4** [warning] NER → RE 扩展太薄，不足以支撑 "structured IE" 泛化标题
- 具体位置：Appendix o（p29, Tables 29–30）, Section 7.5 RE 结果, Title
- 问题：RE 扩展仅在 SciERC 一个数据集上（397 RE instances），且结果表明 cascade 行为与 NER 显著不同：40% 实例获得 zero F1，instance degeneracy 10.1%（远低于 CoNLL NER 的 67.7%），LP selection 在 full set 和 non-zero subset 上均失败（Table 29）。SQL parsing 仅在 Section 7.5 中一句话提及（"87.2% degeneracy"），无详细分析。论文标题 "Test-Time Aggregation in NER" 是准确的，但 Abstract 和 Introduction 的 "structured IE" framing 超出了实验证据。
- 建议：(1) 调整 Abstract/Introduction 的措辞，降低 "structured IE" 泛化的语气，或 (2) 补充至少一个独立 RE dataset（非 SciERC）的结果以增强泛化证据。

**W5** [warning] Cross-dataset power analysis 的 underpowered 结论未充分讨论
- 具体位置：Table 58（p42）, Section 4（p4）
- 问题：Cross-dataset degeneracy-LP gain 相关分析（n=23 configurations）的 post-hoc power analysis 显示：80% power 要求 r≥0.85（p=0.3）和 n≥17（p=0.5）。n=23 仅能检测到 large effects (r≥0.5)，对 moderate effects (r=0.3) 严重 underpowered。但正文 Section 4 报告 "degeneracy alone predicts LP gain across datasets (p=0.002, n=23, ρ=0.81)" 时，未讨论这一 power limitation 的含义——即如果真实效应是 moderate 而非 large，当前样本量可能无法检测到。
- 建议：在正文中用一句话注明 "our cross-dataset analysis is adequately powered for large effects (ρ>0.5) but may miss moderate associations"。

**W6** [warning] 与 Yun et al. (2025) diversity collapse 的关系讨论不充分
- 具体位置：Section 8 Related Work（p8）
- 问题：论文用一句话区分自己与 Yun et al.（"they measure generation diversity, we measure agreement-quality alignment"），但未充分讨论 constrained decoding 如何同时影响 diversity（Yun et al. 的焦点）和 LP compression（本文的焦点）。考虑到本文所有实验均在 constrained decoding 下进行，而 Yun et al. 的 diversity collapse 正是在 constrained decoding 下观察到的，两者的交互效应值得更深入讨论。特别是：如果 diversity collapse 导致 degeneracy 升高，那么 cascade 的 degeneracy 阶段可能本质上是在诊断 constrained decoding 的效应而非模型能力的内在限制。
- 建议：在 Discussion 中增加 2-3 句话，讨论 constrained decoding 作为 confound 的可能性，并引用 Appendix q 的 free-form 消融作为部分缓解证据。

## 小问题（不影响接收）

- **M1**: Table 3（p4）中 "LP" 的 footnote 1 说明 "RE F1 is constrained by entity span errors; the majority of zero-F1 RE instances reflect upstream NER misannotations rather than relation classification failure"——这个 footnote 很重要但容易被忽略，建议在 RE 讨论处（Section 7.5 或 Appendix o）再次强调。
- **M2**: Figure 1（p3）overview 图中 "diagnostic; not causal chain" 的标注很好，但 cascade 箭头的视觉暗示仍然是因果方向。考虑用虚线箭头或不同标注减少因果误读。
- **M3**: Proposition 1（p6）和 Proposition 2（p30-31）的 entity-wise independence 假设在正文中应更明确标注为 simplifying assumption。当前仅在 proof 的 Remark 中提及。
- **M4**: Table 65 cost-benefit analysis（p45）很有价值，建议提升到正文（至少提及核心数字），帮助读者评估 entity-level construction 的实际价值。

## Questions to Authors

**Q1**: 在 CoNLL（67.7% degeneracy）上进行 free-form decoding 消融，degeneracy 率是否会显著下降？如果下降，cascade 对 CoNLL 的诊断结论（"degeneracy is the bottleneck"）是否需要修正为 "constrained decoding is the bottleneck"？

**Q2**: θ_crit=0.70 的 LOO cross-validation 结果具体是什么？每个 fold 的 θ_crit 估计值的变异范围是多少？

**Q3**: 如果将 Table 12 的 57 个测试按 Benjamini-Hochberg FDR（而非 Holm-Bonferroni FWER）校正，有多少核心 NER claims 能在 FDR<0.05 下成立？

**Q4**: 2-seed selection signals 与 3-seed baselines 的不对称设计是否有特定原因？使用完整的 3-seed 均值是否会改变 Table 1 的主要结论？

**Q5**: GPT-5.5 的 200-instance zero-shot 实验中，instance 选择策略是什么（随机抽样？全部来自某个 dataset？）？Appendix 中是否有更详细的结果分解？

## Missing References

论文的 Related Work 覆盖较为完整，以下为可考虑补充的相关工作：
- Chen et al. (2024a) 关于 SC failure modes 的分析已引用，但 Aggarwal et al. (2023) 关于 self-consistency in allocation 的工作可能与 entity-level construction 的 resource allocation 视角相关（已引用但讨论较少）。
- Stengel-Eskin et al. (2025) 或类似的 calibration-aware decoding 工作，与 Section 7.2 的 calibration baseline 讨论相关。

---

**审稿人总结**：这是一篇方法论严谨、写作清晰、补充材料极其充实的分析论文。四阶段诊断框架是对 SC 在结构化 IE 中理解的有意义的推进。主要障碍在于：(1) 核心统计结论在全局校正下脆弱，(2) θ_crit=0.70 的验证不充分，(3) 模型/任务覆盖面与泛化声明之间存在落差。如果作者能在 rebuttal 中回应 Q1-Q3 并承诺补充关键消融，该论文有潜力达到 Conference 水平。当前评分 3.5（Borderline Conference）。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 3660 · 2026-05-22T08:55:02.893969+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': '收集 Reviewer 1 审稿意见', 'status': 'completed', 'activeForm': '已收到 Reviewer 1 审稿意见'}, {'content': '收集 Reviewer 2 审稿意见', 'status': 'completed', 'activeForm': '已收到 Reviewer 2 审稿意见'}, {'content': '交叉分享：将 R1 意见转发给 R2，R2 意见转发给 R1', 'status': 'in_progress', 'activeForm': '执行交叉分享'}, {'content': '收敛判断：分析共识与分歧', 'status': 'pending', 'activeForm': '分析收敛情况'}, {'content': '合成最终报告并投递', 'status': 'pending', 'activeForm': '合成并投递审稿报告'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': '收集 Reviewer 1 审稿意见', 'status': 'completed', 'activeForm': '已收到 Reviewer 1 审稿意见'}, {'content': '收集 Reviewer 2 审稿意见', 'status': 'completed', 'activeForm': '已收到 Reviewer 2 审稿意见'}, {'content': '交叉分享：将 R1 意见转发给 R2，R2 意见转发给 R1', 'status': 'in_progress', 'activeForm': '执行交叉分享'}, {'content': '收敛判断：分析共识与分歧', 'status': 'pending', 'activeForm': '分析收敛情况'}, {'content': '合成最终报告并投递', 'status': 'pending', 'activeForm': '合成并投递审稿报告'}]"
  }
}
```

</details>

---


### Tool result

_source line 3661 · 2026-05-22T08:55:02.945169+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "TodoWrite",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 3662 · 2026-05-22T08:55:34.119165+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "34",
  "text": "## 交叉分享：Reviewer 1 的完整审稿意见\n\n请逐条回应以下 Reviewer 1 的审稿意见。对每个要点标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n### Reviewer 1 评分\n- **Overall**: 3.5（Borderline Conference）\n- Soundness 3.5/5, Excitement 3/5, Reproducibility 4/5\n\n### Reviewer 1 Strengths\nS1. 系统性诊断框架的原创贡献——四阶段 cascade 是对 SC 在结构化 IE 中失败模式的首次系统分类\nS2. 统计方法的严谨性和透明度——报告 Holm-Bonferroni (k=57)、bootstrap CIs、TOST 等价检验、permutation tests、post-hoc power analysis\nS3. 极其充实的补充材料——39 页 Appendix 覆盖几乎所有可能的消融\nS4. 清晰的 observational 定位——开头即声明不做因果声明\nS5. 实用的 degeneracy 诊断洞见——θ_crit=0.70 和 LP 作为最强 per-sample 信号\n\n### Reviewer 1 Must-Fix\n\n**N1** [critical] 全局 Holm-Bonferroni 校正下核心 NER 主张不成立（p_HB=0.055），但主文未充分讨论。Table 12 (k=57) 显示 \"no core NER claim survives\"；正文使用 family-wise corrected p-values（较小的 k），但未在正文中明确告知全局校正结果。建议在 Discussion/Limitations 中显著讨论，为 family-wise 分组提供更强先验理由，考虑报告 FDR。\n\n**N2** [critical] θ_crit=0.70 缺少 held-out 验证，存在 post-hoc fitting 风险。该阈值从同一组数据中确定并验证；16 个配置点既用于拟合又用于声称泛化。建议明确报告 LOO-CV 完整结果，或使用一个 dataset 作为 held-out。\n\n**N3** [critical] 模型覆盖面不足以支撑 \"跨规模/跨家族一致性\" 声明。主要依赖 2 个 8B fine-tuned 模型；GPT-5.5 仅 200 instances zero-shot；14B 仅 SciERC；72B 仅 zero-shot。建议限定 claim 范围为 \"7–14B fine-tuned + selected zero-shot frontier models\"。\n\n### Reviewer 1 Should-Fix\n\n**W1** Free-form decoding 消融仅覆盖 SciERC，CoNLL/WNUT-17 缺失。如果 constrained decoding 驱动 CoNLL 高退化率，cascade 诊断价值将被高估。\n**W2** Table 1 中 2-seed vs 3-seed 差异未充分说明。\n**W3** Entity-level construction \"exploratory\" 定位与叙事张力——Abstract/Discussion 以 prescriptive 口吻呈现，Section 7.5 标记 exploratory。\n**W4** NER → RE 扩展太薄，不足以支撑 \"structured IE\" 泛化标题。RE 仅 SciERC（397 instances），SQL 仅一句话提及。\n**W5** Cross-dataset power analysis underpowered（n=23 仅检测 large effects）未充分讨论。\n**W6** 与 Yun et al. (2025) diversity collapse 关系讨论不充分——constrained decoding 可能同时驱动 diversity collapse 和 LP compression。\n\n### Reviewer 1 Questions\nQ1: CoNLL free-form decoding 是否会显著降低 degeneracy？\nQ2: θ_crit=0.70 的 LOO-CV 结果？\nQ3: 按 BH FDR 校正，多少核心 claims 成立？\nQ4: 2-seed vs 3-seed 不对称原因？\nQ5: GPT-5.5 200-instance 的选择策略？\n\n---\n\n请对以上每个 Must-Fix、Should-Fix 和 Question 逐条回应 [AGREE] 或 [REBUT]。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "34",
    "text": "## 交叉分享：Reviewer 1 的完整审稿意见\n\n请逐条回应以下 Reviewer 1 的审稿意见。对每个要点标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n### Reviewer 1 评分\n- **Overall**: 3.5（Borderline Conference）\n- Soundness 3.5/5, Excitement 3/5, Reproducibility 4/5\n\n### Reviewer 1 Strengths\nS1. 系统性诊断框架的原创贡献——四阶段 cascade 是对 SC 在结构化 IE 中失败模式的首次系统分类\nS2. 统计方法的严谨性和透明度——报告 Holm-Bonferroni (k=57)、bootstrap CIs、TOST 等价检验、permutation tests、post-hoc power analysis\nS3. 极其充实的补充材料——39 页 Appendix 覆盖几乎所有可能的消融\nS4. 清晰的 observational 定位——开头即声明不做因果声明\nS5. 实用的 degeneracy 诊断洞见——θ_crit=0.70 和 LP 作为最强 per-sample 信号\n\n### Reviewer 1 Must-Fix\n\n**N1** [critical] 全局 Holm-Bonferroni 校正下核心 NER 主张不成立（p_HB=0.055），但主文未充分讨论。Table 12 (k=57) 显示 \"no core NER claim survives\"；正文使用 family-wise corrected p-values（较小的 k），但未在正文中明确告知全局校正结果。建议在 Discussion/Limitations 中显著讨论，为 family-wise 分组提供更强先验理由，考虑报告 FDR。\n\n**N2** [critical] θ_crit=0.70 缺少 held-out 验证，存在 post-hoc fitting 风险。该阈值从同一组数据中确定并验证；16 个配置点既用于拟合又用于声称泛化。建议明确报告 LOO-CV 完整结果，或使用一个 dataset 作为 held-out。\n\n**N3** [critical] 模型覆盖面不足以支撑 \"跨规模/跨家族一致性\" 声明。主要依赖 2 个 8B fine-tuned 模型；GPT-5.5 仅 200 instances zero-shot；14B 仅 SciERC；72B 仅 zero-shot。建议限定 claim 范围为 \"7–14B fine-tuned + selected zero-shot frontier models\"。\n\n### Reviewer 1 Should-Fix\n\n**W1** Free-form decoding 消融仅覆盖 SciERC，CoNLL/WNUT-17 缺失。如果 constrained decoding 驱动 CoNLL 高退化率，cascade 诊断价值将被高估。\n**W2** Table 1 中 2-seed vs 3-seed 差异未充分说明。\n**W3** Entity-level construction \"exploratory\" 定位与叙事张力——Abstract/Discussion 以 prescriptive 口吻呈现，Section 7.5 标记 exploratory。\n**W4** NER → RE 扩展太薄，不足以支撑 \"structured IE\" 泛化标题。RE 仅 SciERC（397 instances），SQL 仅一句话提及。\n**W5** Cross-dataset power analysis underpowered（n=23 仅检测 large effects）未充分讨论。\n**W6** 与 Yun et al. (2025) diversity collapse 关系讨论不充分——constrained decoding 可能同时驱动 diversity collapse 和 LP compression。\n\n### Reviewer 1 Questions\nQ1: CoNLL free-form decoding 是否会显著降低 degeneracy？\nQ2: θ_crit=0.70 的 LOO-CV 结果？\nQ3: 按 BH FDR 校正，多少核心 claims 成立？\nQ4: 2-seed vs 3-seed 不对称原因？\nQ5: GPT-5.5 200-instance 的选择策略？\n\n---\n\n请对以上每个 Must-Fix、Should-Fix 和 Question 逐条回应 [AGREE] 或 [REBUT]。"
  }
}
```

</details>

---


### Tool result

_source line 3663 · 2026-05-22T08:55:59.777722+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 25658
}
```

</details>

---


### Tool call

_source line 3664 · 2026-05-22T08:56:03.571946+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "34",
  "text": "## 交叉分享：Reviewer 2 的完整审稿意见\n\n请逐条回应以下 Reviewer 2 的审稿意见。对每个要点标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n### Reviewer 2 评分\n- **Overall**: 3.0（Findings）\n- Soundness 3.5/5, Excitement 3/5, Reproducibility 4/5\n\n### Reviewer 2 Strengths\nS1. 极其彻底的实验覆盖——4 NER datasets、2 model families、9 method categories、16 configurations\nS2. 统计严谨性出色——bootstrap CI、permutation test、Holm-Bonferroni\nS3. Correlation-selection gap 是有用的诊断概念\nS4. 实用的负面结论——pre-deployment diagnostic cascade\nS5. Entity-level construction 与 MBR 的形式化连接\n\n### Reviewer 2 Must-Fix\n\n**N1** [critical] 标题和定位 \"Diagnostic Framework\" 超出实际贡献。论文实际是深入 empirical observations 以事后 cascade 呈现。一个 \"framework\" 应具备（a）明确可操作步骤，（b）跨任务通用性，（c）预测能力。建议改标题为 empirical study / diagnostic analysis 定位。\n\n**N2** [critical] Prescriptive contribution 薄弱，削弱三阶段叙事。Entity-level construction：Few-NERD +1.4pp，CoNLL -0.85pp，SciERC +0.2pp——结论本质是 \"what NOT to do\" 而非 \"what to do\"。建议诚实定位为 Discover+Diagnose 为主、Prescribe 为探索性。\n\n**N3** [critical] 新颖性增量 vs. 相关工作不够清晰。相对于 Yao et al. (2026) task-level analysis、Chen et al. (2024) SC failure modes、Xie et al. (2023) entity voting、Yun et al. (2025) diversity collapse 的增量贡献需更清晰阐述。\n\n### Reviewer 2 Should-Fix\n\n**W1** 论文结构非常规——实验结果分散在 Sections 3-7，Experimental Setup 直到 p6 才出现。\n**W2** 信息密度过高，首次阅读难以跟上。\n**W3** \"Capability ceiling\" N≤16 定义较窄且缺乏充分论证。\n**W4** Proposition 1 和 2 的理论贡献定位模糊——更像事后形式化而非驱动实验设计。\n**W5** CoNLL 高 degeneracy (38%-89%) 削弱 selection failure 发现的 interestingness——部分是 tautology。\n**W6** Related Work (Section 8) 位置和覆盖度不足——Snell et al. (2025)、Eikema et al. (2025)、calibration 文献讨论不充分。\n\n### Reviewer 2 Limitations 评估遗漏\n1. 仅测试 8B 模型（未讨论 70B+ fine-tuned）\n2. Temperature 设置单一（T=1.0 primary）\n3. Prompt sensitivity 未讨论\n\n### Reviewer 2 Questions\nQ1: Diagnostic cascade 四阶段是否有 formal 决策边界？\nQ2: Entity-level construction 在 CoNLL 负面——有无 per-entity-type 分析解释？\nQ3: 结合 degeneracy filtering + entity construction 收益是否更大？\nQ4: Cascade 适用于其他 structured prediction 任务的初步证据？\n\n### Reviewer 2 Missing References\n1. Snell et al. (2025) \"Scaling LLM Test-Time Compute Optimally\"——compute-optimal 策略与 dataset-dependent optimal strategy 相关\n2. Eikema et al. (2025) structure-conditional MBR 与 entity-level construction 的关系需深化\n\n---\n\n请对以上每个 Must-Fix、Should-Fix、Limitations 遗漏和 Question 逐条回应 [AGREE] 或 [REBUT]。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "34",
    "text": "## 交叉分享：Reviewer 2 的完整审稿意见\n\n请逐条回应以下 Reviewer 2 的审稿意见。对每个要点标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n### Reviewer 2 评分\n- **Overall**: 3.0（Findings）\n- Soundness 3.5/5, Excitement 3/5, Reproducibility 4/5\n\n### Reviewer 2 Strengths\nS1. 极其彻底的实验覆盖——4 NER datasets、2 model families、9 method categories、16 configurations\nS2. 统计严谨性出色——bootstrap CI、permutation test、Holm-Bonferroni\nS3. Correlation-selection gap 是有用的诊断概念\nS4. 实用的负面结论——pre-deployment diagnostic cascade\nS5. Entity-level construction 与 MBR 的形式化连接\n\n### Reviewer 2 Must-Fix\n\n**N1** [critical] 标题和定位 \"Diagnostic Framework\" 超出实际贡献。论文实际是深入 empirical observations 以事后 cascade 呈现。一个 \"framework\" 应具备（a）明确可操作步骤，（b）跨任务通用性，（c）预测能力。建议改标题为 empirical study / diagnostic analysis 定位。\n\n**N2** [critical] Prescriptive contribution 薄弱，削弱三阶段叙事。Entity-level construction：Few-NERD +1.4pp，CoNLL -0.85pp，SciERC +0.2pp——结论本质是 \"what NOT to do\" 而非 \"what to do\"。建议诚实定位为 Discover+Diagnose 为主、Prescribe 为探索性。\n\n**N3** [critical] 新颖性增量 vs. 相关工作不够清晰。相对于 Yao et al. (2026) task-level analysis、Chen et al. (2024) SC failure modes、Xie et al. (2023) entity voting、Yun et al. (2025) diversity collapse 的增量贡献需更清晰阐述。\n\n### Reviewer 2 Should-Fix\n\n**W1** 论文结构非常规——实验结果分散在 Sections 3-7，Experimental Setup 直到 p6 才出现。\n**W2** 信息密度过高，首次阅读难以跟上。\n**W3** \"Capability ceiling\" N≤16 定义较窄且缺乏充分论证。\n**W4** Proposition 1 和 2 的理论贡献定位模糊——更像事后形式化而非驱动实验设计。\n**W5** CoNLL 高 degeneracy (38%-89%) 削弱 selection failure 发现的 interestingness——部分是 tautology。\n**W6** Related Work (Section 8) 位置和覆盖度不足——Snell et al. (2025)、Eikema et al. (2025)、calibration 文献讨论不充分。\n\n### Reviewer 2 Limitations 评估遗漏\n1. 仅测试 8B 模型（未讨论 70B+ fine-tuned）\n2. Temperature 设置单一（T=1.0 primary）\n3. Prompt sensitivity 未讨论\n\n### Reviewer 2 Questions\nQ1: Diagnostic cascade 四阶段是否有 formal 决策边界？\nQ2: Entity-level construction 在 CoNLL 负面——有无 per-entity-type 分析解释？\nQ3: 结合 degeneracy filtering + entity construction 收益是否更大？\nQ4: Cascade 适用于其他 structured prediction 任务的初步证据？\n\n### Reviewer 2 Missing References\n1. Snell et al. (2025) \"Scaling LLM Test-Time Compute Optimally\"——compute-optimal 策略与 dataset-dependent optimal strategy 相关\n2. Eikema et al. (2025) structure-conditional MBR 与 entity-level construction 的关系需深化\n\n---\n\n请对以上每个 Must-Fix、Should-Fix、Limitations 遗漏和 Question 逐条回应 [AGREE] 或 [REBUT]。"
  }
}
```

</details>

---


### Tool result

_source line 3665 · 2026-05-22T08:56:05.291915+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1719
}
```

</details>

---


### Assistant

_source line 3666 · 2026-05-22T08:56:07.953628+00:00_

交叉分享已发送。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 272

## Round 272

2 recorded events


### User

_source line 3667 · 2026-05-22T08:56:11.024778+00:00_

[Reviewer 1 审稿结果]:
审稿完成。已向 Review Director 提交完整审稿意见，核心评判：

- **Overall: 3.5（Borderline Conference）**
- **Soundness: 3.5/5** — 框架逻辑完整但全局 Holm-Bonferroni (k=57) 下核心 NER claim 不显著 (p_HB=0.055)
- **Excitement: 3/5** — 诊断框架有价值但 prescriptive 输出增益有限
- **Reproducibility: 4/5**

三个 Must-Fix 问题：
1. 全局统计校正下核心主张脆弱，主文未充分讨论
2. θ_crit=0.70 缺 held-out 验证，post-hoc fitting 风险
3. 模型覆盖面（主要 8B）不足以支撑跨规模/跨家族泛化声明

六个 Should-Fix 问题涵盖 free-form ablation 覆盖不足、2-seed/3-seed 不对称、entity-level construction 叙事张力、RE 扩展证据薄弱、cross-dataset power limitation、与 Yun et al. diversity collapse 的关系讨论不充分。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 3668 · 2026-05-22T08:56:15.902701+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 273

## Round 273

4 recorded events


### User

_source line 3669 · 2026-05-22T08:57:42.647868+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 交叉回应：Reviewer 1 审稿意见

---

### 对 Reviewer 1 Strengths 的回应

**[AGREE] R1-S1**: 四阶段 cascade 确实是对 SC 在结构化 NER 中失败模式的首次系统分类。但我在自己的 N1 中指出，"framework" 的定位超出了实际贡献——更准确的描述是 "diagnostic empirical study"。Cascade 作为分析组织方式有价值，但作为可复用 framework 则论证不足。

**[AGREE] R1-S2**: 统计方法论确实是本文的亮点。Table 12 的 57 项检验、bootstrap CI、TOST 等价检验的组合使用，在 NLP empirical 论文中是标杆水平。这也是我给 Reproducibility 4/5 的主要原因。

**[AGREE] R1-S3**: 39 页附录的详尽程度令人印象深刻。几乎每个主文 claim 都有对应的完整消融在附录中。

**[AGREE] R1-S4**: Section 1 和 Figure 1 注释明确声明 "diagnostic; not causal chain"，这种诚实定位值得肯定。但我在小问题 M2 中指出，Figure 1 的箭头视觉上仍暗示因果链。

**[AGREE] R1-S5**: Degeneracy 诊断和 LP 作为最强信号的发现有实用价值。但 degeneracy 阈值（R1 的 N2）和 LP 信号在不同 degeneracy regime 下的有效性（我的 W5）需要更审慎的讨论。

---

### 对 Reviewer 1 Must-Fix 的回应

**[AGREE] R1-N1**: 全局 Holm-Bonferroni 校正下核心 claim 的边缘显著性（p_HB=0.055）

这是一个我未在自己的审稿中充分关注的重要统计问题。R1 指出的核心矛盾是：论文在 Table 12 中做了 k=57 项全局检验，其中核心 NER 选择 claim 在全局校正后 p_HB=0.055——刚好未通过 α=0.05 的阈值。但主文使用的是 family-wise 分组（较小的 k），使得同一检验通过了校正。

论文的 family-wise 分组（selection tests、construction tests、calibration tests 分别校正）在统计方法论上是可辩护的——不同 hypothesis families 有不同的先验理由。但 R1 要求的是**透明度**：主文应该（a）明确展示全局 vs. family-wise 校正的差异，（b）为 family-wise 分组提供先验理由而非仅在方法论附注中说明，（c）报告 BH FDR 作为 supplement。

我补充一点：这个问题与我自己的 N1（framework 定位过高）相互关联——如果核心统计 claim 在全局校正下边缘不显著，那么 "systematic framework" 的声明就更需要谨慎。

**建议**：Discussion 或 Limitations 中应增加一段关于多重检验校正策略选择的讨论，并透明报告全局 Holm-Bonferroni 和 BH FDR 的结果。

---

**[REBUT] R1-N2**: θ_crit=0.70 缺少 held-out 验证

我理解 R1 的顾虑，但认为这个问题的严重性被高估了，原因如下：

1. **θ_crit 的性质**：从我对论文的理解，θ_crit=0.70 是一个**描述性统计量**（degeneracy 超过此值后 selection gain 消失的经验观察），而非一个**预测模型参数**。这更类似于报告 "当 degeneracy > 70% 时，LP selection 不再优于 greedy"——这是对数据模式的描述，不需要像 ML 模型参数那样做 held-out 验证。

2. **但 R1 的核心关切仍然成立**：如果论文将 θ_crit=0.70 作为**可推荐的实用阈值**（"practitioners should check if degeneracy exceeds 0.70"），那就需要某种形式的外部验证。16 个配置点确实不多，过拟合风险存在。

3. **妥协方案**：我同意论文应该（a）明确 θ_crit 的定位是描述性还是规范性，（b）如果是规范性的，报告 LOO-CV 结果或至少讨论该阈值的 sensitivity（±0.05 范围内结论是否变化）。

**总结**：降级为 Should-Fix 而非 Must-Fix。θ_crit 更是描述性发现而非拟合参数，但论文确实需要更清晰地定位它并讨论 robustness。

---

**[AGREE] R1-N3**: 模型覆盖面不足以支撑跨规模/跨家族一致性声明

完全同意。我在自己的 Limitations 评估中也指出了 "仅测试 8B 参数级别模型" 是重要的遗漏 limitation。具体来说：
- 主实验：Qwen3-8B + LLaMA-3.1-8B（2 个 8B fine-tuned 模型）
- GPT-5.5：200 instances zero-shot（Table 7, p.7；Appendix s, p.35-36），样本量极小且 setup 不同（zero-shot vs. fine-tuned），不能作为 frontier model 覆盖的充分证据
- 14B（Qwen2.5-14B）：仅 SciERC（Appendix t, p.37）
- 72B：仅 zero-shot

论文标题中 "Self-Consistency" 的声明范围是通用的，但证据仅覆盖 8B fine-tuned regime。建议如 R1 所言，将 claim 范围限定为 "7-14B fine-tuned models"，并在 Limitations 中明确 larger model 可能有不同 pattern（例如更好的 calibration 可能缩小 correlation-selection gap）。

---

### 对 Reviewer 1 Should-Fix 的回应

**[AGREE] R1-W1**: Free-form decoding 消融仅覆盖 SciERC

这是我审稿中遗漏的一个重要问题。论文的 constrained decoding（JSON schema enforcement）可能是 CoNLL 89% degeneracy 的重要驱动因素——constrained decoding 限制输出空间，自然导致更高的样本间一致性。Table 33（Appendix p, p.33）展示了 constrained vs. free-form 在 SciERC 上的对比，发现 selection gap 在两种 regime 下都 replicate。但 CoNLL 的 degeneracy pattern 可能不同：CoNLL 的 entity types 更少、schema 更简单，constrained decoding 可能对 diversity 的压缩效应更强。

如果 CoNLL free-form decoding 的 degeneracy 从 89% 大幅下降，那么 "selection fails on CoNLL" 的结论就需要 qualified——它可能更多是 constrained decoding artifact 而非 SC 的固有局限。这会显著影响 diagnostic cascade 在 CoNLL 上的解释力。

**[AGREE] R1-W2**: Table 1 的 2-seed vs 3-seed 差异

审稿时我注意到了这个不对称（Table 1 注释提到部分配置用 2 seeds，部分用 3 seeds），但未将其标记为问题。R1 有理由要求说明：（a）为什么不同配置使用不同 seed 数量？（b）这是否影响 error bars 的可比性？即使最终结论不变，方法论透明度要求说明这个选择。

**[AGREE] R1-W3**: Entity-level construction "exploratory" 定位与叙事张力

这与我的 N2（Prescriptive contribution 薄弱）高度一致。论文内部存在定位矛盾：Abstract 和 Introduction 以 prescriptive 口吻呈现 entity-level construction（"+1.4 pp on Few-NERD"），Section 7.5 标题含 "exploratory"，Section 9 结论则更多是 diagnostic。

我和 R1 的发现相互印证：论文需要在 "prescriptive framework" 和 "diagnostic study with exploratory prescriptive suggestions" 之间做出一致的定位选择。

**[AGREE] R1-W4**: NER → RE 扩展太薄

论文标题已限定为 "NER"，这点上标题是准确的。但 Section 8 和部分讨论使用了 "structured IE" 的更广泛术语（例如 Section 9: "inference-time scaling for structured prediction"）。Appendix o（p.28-29）的 RE 扩展仅在 SciERC 的 397 instances 上做了初步探索。如果论文要声称对 "structured prediction" 有 implications，需要更多跨任务证据；如果仅限于 NER，应在 Discussion 中更审慎地限定泛化范围。

**[REBUT] R1-W5**: Cross-dataset power analysis underpowered (n=23)

R1 的观察是正确的——n=23 仅能检测 large effects——但我认为论文已经在 Table 12 的 cross-dataset 部分（rows 44-48）恰当处理了这个问题。这些检验的结果确实是 "not significant"，论文也没有声称跨数据集效应是显著的。低 power 更多是数据集数量的固有限制（全球 NER benchmark 就那么多），而非实验设计缺陷。

论文可以在 Limitations 中增加一句关于 cross-dataset 检验的 statistical power 不足，但这不应该升级为 Should-Fix——这是 empirical NLP 的系统性限制，不是本文特有的问题。

**[AGREE] R1-W6**: 与 Yun et al. (2025) diversity collapse 关系讨论不充分

完全同意，这与我的 N3（第 4 点）高度一致。Degeneracy（所有 N 个样本完全相同）是 diversity collapse 的极端情况还是不同现象？论文在 Section 8 有一段讨论（"Our degeneracy concept is narrower..."），但未深入分析：
- Constrained decoding 是否同时驱动 diversity collapse 和 LP compression？（与 R1-W1 关联）
- Yun et al. 的 format-induced diversity collapse 在 NER structured output 上是否有特殊表现？
- 如果 degeneracy 本质上是 Yun et al. diversity collapse 在 structured decoding 下的特例，本文的 degeneracy decomposition 的增量贡献是什么？

---

### 对 Reviewer 1 Questions 的回应

**Q1** (CoNLL free-form decoding 是否会显著降低 degeneracy):
**[AGREE 这是关键问题]**。CoNLL 有最少的 entity types（4 类 vs. SciERC 6 类 vs. Few-NERD 66 类），structured schema 最简单。Free-form decoding 移除 schema 约束后，output diversity 可能显著增加，degeneracy 可能从 89% 大幅下降。如果是这样，CoNLL 上的 diagnostic cascade 结论需要重新解读。这个实验的缺失是论文的一个重要 gap。

**Q2** (θ_crit=0.70 的 LOO-CV):
如我在 R1-N2 的回应中所述，我认为 LOO-CV 是合理的要求，但 θ_crit 的性质（描述性 vs. 规范性）决定了验证的必要性程度。如果是描述性的，sensitivity analysis（±0.05）可能就够了。

**Q3** (BH FDR 校正下多少 claims 成立):
**[AGREE 应该报告]**。BH FDR 比 Holm-Bonferroni 更宽松，如果 FDR 下核心 claims 成立而 Holm-Bonferroni 下不成立，这恰好支持 family-wise 分组的合理性。报告 FDR 有益无害。

**Q4** (2-seed vs 3-seed 不对称):
**[AGREE 需要说明]**。可能的原因包括计算资源限制（某些配置更昂贵）、early stopping 差异（Appendix k 提到 3 epochs vs. 5 epochs for different datasets），但应在方法论中明确说明。

**Q5** (GPT-5.5 200-instance 选择策略):
**[AGREE 需要说明]**。200 instances 是完整测试集的子集，选择策略（random sample? stratified? 特定 entity types?）会影响结论的代表性。Appendix s（p.35-36）有一些细节但选择标准不够明确。

---

### 我与 Reviewer 1 的主要分歧

1. **Overall 评分**：R1 给 3.5（Borderline Conference），我给 3.0（Findings）。差异主要来自我对 **novelty 增量** 的更严格评估——我认为 correlation-selection gap 相对于 Yao et al. (2026)、Chen et al. (2024)、Xie et al. (2023) 的增量贡献不够清晰（我的 N3），这在 R1 的审稿中未被列为 Must-Fix。

2. **θ_crit 的严重性**：R1 列为 Must-Fix（N2），我认为应降级为 Should-Fix——θ_crit 更像描述性发现而非需要 held-out 验证的模型参数。

3. **Cross-dataset power**：R1 列为 Should-Fix（W5），我认为这是领域固有限制，提及即可，无需单独修复。

### 我与 Reviewer 1 的主要共识

1. **Framework 定位过高**（R1-S1 的 caveat ≈ 我的 N1）
2. **Prescriptive 阶段薄弱**（R1-W3 ≈ 我的 N2）
3. **模型覆盖面不足**（R1-N3 ≈ 我的 Limitations 评估）
4. **与 Yun et al. 关系讨论不充分**（R1-W6 ≈ 我的 N3 第 4 点）
5. **统计实践是论文的核心优势**（R1-S2 = 我的 S2）
6. **附录详尽度令人印象深刻**（R1-S3 = 我的 S1）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 3670 · 2026-05-22T08:57:51.899543+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': '收集 Reviewer 1 审稿意见', 'status': 'completed', 'activeForm': '已收到 Reviewer 1 审稿意见'}, {'content': '收集 Reviewer 2 审稿意见', 'status': 'completed', 'activeForm': '已收到 Reviewer 2 审稿意见'}, {'content': '交叉分享：将 R1 意见转发给 R2，R2 意见转发给 R1', 'status': 'completed', 'activeForm': '已完成 R2 交叉回应，等待 R1 交叉回应'}, {'content': '收敛判断：分析共识与分歧', 'status': 'pending', 'activeForm': '分析收敛情况'}, {'content': '合成最终报告并投递', 'status': 'pending', 'activeForm': '合成并投递审稿报告'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': '收集 Reviewer 1 审稿意见', 'status': 'completed', 'activeForm': '已收到 Reviewer 1 审稿意见'}, {'content': '收集 Reviewer 2 审稿意见', 'status': 'completed', 'activeForm': '已收到 Reviewer 2 审稿意见'}, {'content': '交叉分享：将 R1 意见转发给 R2，R2 意见转发给 R1', 'status': 'completed', 'activeForm': '已完成 R2 交叉回应，等待 R1 交叉回应'}, {'content': '收敛判断：分析共识与分歧', 'status': 'pending', 'activeForm': '分析收敛情况'}, {'content': '合成最终报告并投递', 'status': 'pending', 'activeForm': '合成并投递审稿报告'}]"
  }
}
```

</details>

---


### Tool result

_source line 3671 · 2026-05-22T08:57:51.900046+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Assistant

_source line 3672 · 2026-05-22T08:57:54.998079+00:00_

Reviewer 2 交叉回应已收到。等待 Reviewer 1 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 274

## Round 274

2 recorded events


### User

_source line 3673 · 2026-05-22T08:57:57.792629+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。

核心共识：两位 Reviewer 均认为 framework 定位过高、prescriptive 贡献薄弱、模型覆盖面不足。主要分歧在 Overall 评分（R1: 3.5 vs 我: 3.0），我对 novelty 增量的要求更严格。R1 提出的 free-form decoding 在 CoNLL 上的缺失消融（W1）是我原审稿遗漏的重要问题，已表示同意。θ_crit 的 held-out 验证问题我建议从 Must-Fix 降级为 Should-Fix。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 3674 · 2026-05-22T08:58:02.373608+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 275

## Round 275

18 recorded events


### User

_source line 3675 · 2026-05-22T09:01:04.267248+00:00_

[Reviewer 1 审稿意见]:

## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

### 对 R2 Strengths 的回应

R2 的 S1-S5 我全部认同。特别补充：S2（统计严谨性）是本文最突出的优势之一——Table 12 全局 Holm-Bonferroni 的透明报告在 NLP 论文中罕见。S5（MBR 形式化连接）通过 Proposition 2（p30-31）建立了 entity construction 与 structured MBR 的理论桥梁，不仅仅是事后总结。

---

### 对 R2 Must-Fix 的回应

**[REBUT] R2-N1: "Framework" 超出实际贡献，建议改为 empirical study**

R2 声称 "framework" 需要 (a) 明确可操作步骤、(b) 跨任务通用性、(c) 预测能力。我认为论文满足了 (a)，部分满足 (b)，且对 (c) 的缺失有正当理由：

- **(a) 可操作步骤**：Appendix ac（Section 9, p44）提供了完整的 3-step evaluation protocol："Step 1: Measure instance degeneracy... Step 2: Assess signal-quality alignment... Step 3: Evaluate aggregation strategies"。这不是泛泛的经验观察，而是可执行的诊断流程——给定新 dataset/model 组合，从业者可以按此 protocol 判断 SC 是否值得尝试。
- **(b) 跨任务通用性**：NER（4 datasets）+ RE（SciERC, Appendix o, Tables 29-30）+ SQL parsing（§7.5, 87.2% degeneracy）。虽然 RE/SQL 覆盖较薄（我自己的 W4 也指出了这一点），但 cascade 的四个阶段（QE, degeneracy, agreement fidelity, LP compression）在概念上不依赖 NER 特定结构，已在 RE 上得到部分验证。
- **(c) 预测能力**：论文在 Section 2 开头即声明 "our analysis is observational"（p2），Section 4 进一步说明 "the cascade stages interact rather than combining into a predictive model (R²<0)"（p4）。这是一个 *diagnostic* framework，不是 predictive model——正如医学中的 diagnostic criteria 不需要预测能力即可被称为 framework。

**但我部分同意 R2**：论文应在标题或 Introduction 中更明确地标注 "diagnostic" 这一定语（当前标题已包含 "Diagnostic Framework"，但正文叙事偶尔超出诊断范畴）。将标题改为 "empirical study" 则矫枉过正——论文的贡献确实超出典型 empirical study 的结构化程度。

---

**[AGREE] R2-N2: Prescriptive contribution 薄弱**

R2 的核心判断正确：Prescribe 阶段是三阶段叙事中最弱的一环。我在自己的 W3 中也指出了 "exploratory" 定位与 Abstract/Discussion prescriptive 口吻的张力。

**但需纠正 R2 引用的数据**：R2 称 "CoNLL −0.85pp" 为 entity construction 的结果，但 Table 65（p45）明确区分了两个策略：
- **SC + LP selection**（sample-level 选择）：CoNLL −0.85 pp——这是 LP 选择策略的结果，不是 entity construction
- **Entity construction**（entity-level 聚合）：Table 65 称 "consistently positive result at zero marginal cost"；Table 60（p43）的 entity-level MV 结果显示 "only SciERC shows positive recovery; even with oracle δ, CoNLL and Few-NERD degrade"——但这是 MV-weighted construction，LP-weighted construction 结果不同

**数据修正后 R2 的结论仍然成立**：entity construction 在不同 weighting 方案下结果不一致（LP-weighted 在 Few-NERD +1.40pp，MV-weighted 则 CoNLL/Few-NERD 退化），进一步证实了 prescriptive arm 的不稳定性。论文应将 Prescribe 阶段诚实定位为 "exploratory with promising but inconsistent initial results"，并在 Abstract 中调整措辞。

---

**[REBUT] R2-N3: 新颖性增量不清晰**

R2 列举了 Yao et al. (2026)、Chen et al. (2024)、Xie et al. (2023)、Yun et al. (2025) 四篇相关工作，认为增量贡献不够清晰。我认为增量贡献实际上是显著的，但论文的 Related Work 表述确实可以更直接：

| 相关工作 | 其贡献 | 本文增量 |
|---------|-------|--------|
| Chen et al. (2024) | 识别 SC failure modes（空输出、格式错误） | 本文不止于识别 failure，而是提供了定量化的四阶段 cascade 诊断——每个阶段有具体指标（D, ρ, α, LP range），可计算、可比较 |
| Yao et al. (2026) | Task-level analysis：SC 在哪些 task 上有效 | 本文是 instance-level analysis：在给定 task 内，哪些 instances 能从 SC 获益，为什么 |
| Xie et al. (2023) | Entity voting 聚合策略 | 本文将 entity voting 放入更大的方法空间（Table 2, 9 categories），并诊断其在高退化条件下的失败机制 |
| Yun et al. (2025) | Constrained decoding 下的 diversity collapse | 本文测量 agreement-quality alignment（不仅仅是 diversity），并扩展到 entity-level prescriptive 策略 |

**但我同意 R2 的 actionable 建议**：Section 8 应增加一个清晰的 "What's new" 段落，用上述对比表的叙事形式明确阐述增量。当前的讨论分散在 Section 8 多个段落中，读者需要自己综合判断。

---

### 对 R2 Should-Fix 的回应

**[REBUT] R2-W1: 论文结构非常规**

结构是 Discover (§§2-3) → Diagnose (§§4-6) → Prescribe (§7.5) 的叙事弧，实验设置分布在 §2.1（问题定义）、§2.3（评估指标）和 §7.1（数据集/模型细节）。这一结构是有意为之：先呈现诊断发现，再在读者理解了 *why selection fails* 之后给出完整实验细节。类似结构见于 diagnostic/analysis 论文（如 Raunak et al., 2021 NMT 分析）。

我理解 R2 的困惑，但认为这是合理的叙事选择。如果 AC 认为常规结构更好，作者可以在 camera-ready 中调整，但这不应影响接收决定。

---

**[AGREE] R2-W2: 信息密度过高**

8 页正文包含 5 个 QE signals、4 个 cascade stages、9 method categories、4 datasets、2 models、16 configurations 的交叉分析。首次阅读确实吃力。但这部分是 analysis paper 的固有属性——47 页 Appendix 的存在正是为了将细节从正文卸载。论文可以在 Introduction 结尾增加一段 roadmap 帮助读者导航。

---

**[REBUT] R2-W3: "Capability ceiling" N≤16 定义较窄**

R2 对 N 范围的理解不准确。Figure 3（p6）明确展示了 N=8, 16, 32, 64 的 scaling。Appendix s（Tables 35-37, p34）提供了 N=8→16→32 的详细分析。论文的核心发现是 **N=8 已捕获 oracle headroom 的大部分**（Section 6.2, p6: "N=8 captures most of the achievable quality estimation benefit; further scaling widens rather than closes the gap"），N>16 的增量收益递减。

"Capability ceiling" 概念不是关于 N 的上限，而是关于 *correlation-selection gap* 的结构性存在——即使 N 增大，quality estimation 信号与 selection 能力之间的落差仍然存在（Figure 3 显示 gap 随 N 增大而扩大而非收敛）。这一定义不依赖于 N 的具体范围。

---

**[AGREE] R2-W4: Proposition 1 和 2 更像事后形式化**

部分同意。Proposition 1（Entity Selection Diagnostic, p6）确实是对 observed pattern 的形式化总结。但 **Proposition 2 不完全是事后的**：它建立了 entity construction 与 balanced set-overlap utility 下 MBR 最优性的联系（p30-31），推导出 θ=2/N 作为 optimal threshold 的理论基础，并提供了 formal proof（including entity-wise independence assumption 的 Remark）。这一连接将 empirical heuristic（entity-level majority voting with threshold）提升为有理论支撑的方法。

**建议**：论文应在正文中更明确地区分 Proposition 1（descriptive formalization）和 Proposition 2（normative/prescriptive, connecting to MBR theory），避免二者被一概视为 "post-hoc"。

---

**[REBUT] R2-W5: CoNLL 高 degeneracy 使 selection failure 发现 tautological**

这一批评在表面上有道理（degenerate instances 没有候选差异，当然无法 select），但 **忽略了 cascade 的诊断价值**：

1. **反事实**：如果没有 cascade 分析，面对 CoNLL 的 selection failure，合理的替代假设包括：(a) QE 信号质量差、(b) LP compression 过度、(c) agreement-F1 misalignment。Cascade 排除了这些假设，锁定 degeneracy 为 specific bottleneck。这一诊断是非平凡的。

2. **非退化子集分析**：Section 4（p4）和 Table 32 显示，即使在 CoNLL 的非退化实例上，selection alignment α 接近零（0.000-0.161），LP 选择仍然无效——这说明即使 degeneracy 被解决，CoNLL 的 headroom 仍然太小。这一发现 **超越了** "degeneracy is high therefore selection fails" 的表面 tautology。

3. **与 Few-NERD 的对比**：Few-NERD 仅 8.8% degeneracy 但 LP selection 显著有效（+1.39 pp, Table 12 Row 2），而 CoNLL 67.7% degeneracy 且 headroom 接近零——cascade 精确地定位了两个 dataset 的不同失败阶段，这正是 diagnostic framework 的价值。

---

**[AGREE] R2-W6: Related Work 覆盖不足**

同意。具体补充：
- **Snell et al. (2025)** "Scaling LLM Test-Time Compute Optimally" 与本文的 dataset-dependent optimal N 发现直接相关——Snell et al. 讨论了 compute-optimal test-time strategies，而本文的 Figure 3 和 Section 6.2 本质上也在探索 N 的 compute-optimal 配置。应在 Related Work 或 Discussion 中明确引用和对比。
- **Eikema et al. (2025)** 的 structured MBR 已被引用（Section 8, p8），但与 Proposition 2 的连接可以更深入——Proposition 2 实质上证明了 entity construction 是一种 special case of structured MBR under balanced set-overlap utility。
- 我在自己的 W6 中也指出了 Yun et al. (2025) diversity collapse 的讨论不充分。

---

### 对 R2 Limitations 评估遗漏的回应

**[AGREE] L1: 仅测试 8B 模型**

与我的 N3（Must-Fix）一致。论文的跨规模声明缺乏 ≥30B fine-tuned 证据。GPT-5.5（200 instances, zero-shot）和 Qwen2.5-72B-AWQ（zero-shot, Table 64）不足以替代 fine-tuned 大模型的验证。14B 扩展（Appendix x, Table 41）仅在 SciERC 上，too limited。

**[REBUT] L2: Temperature 设置单一（T=1.0）**

R2 的批评不完全准确。Appendix b（Table 6, p14）提供了 T=0.7 的系统性 robustness 分析，显示 "LP shows the largest NER temperature effect" 且 signal hierarchy 在两个温度下保持一致。Section 7.4（p7）主文中也报告了温度影响。T=1.0 是 primary 设置但 T=0.7 robustness check 已完成。

**不过我同意应扩展**：仅 T=0.7 和 T=1.0 两个温度点不足以刻画完整的 temperature landscape。T=0.3 或 T=1.5 的极端值可能揭示不同的 degeneracy-signal 交互模式。

**[AGREE] L3: Prompt sensitivity 未讨论**

论文未系统测试 prompt 变体对 cascade 诊断结论的影响。Constrained decoding 减轻了 output 格式变异，但 prompt 措辞仍可能影响 entity recall、degeneracy rate、和 LP 分布。Limitations（p9）未提及 prompt sensitivity。

---

### 对 R2 Questions 的回应

**Q1: Cascade 四阶段是否有 formal 决策边界？**

部分已回答。θ_crit=0.70 是 degeneracy 阶段的 formal boundary（Section 4, p4）。但其他阶段缺乏同等清晰的阈值——QE 的 AUROC 没有明确的 "sufficient/insufficient" 分界线，agreement fidelity（α）的阈值也未给出。这确实是 "diagnostic framework" 的一个弱点：一个完整的诊断 protocol 应为每个阶段提供 go/no-go 边界。Appendix ac 的 Step 1-3（p44）给出了定性指导但非定量阈值。

**建议作者在 rebuttal 中回应**：如果 θ_crit 可以通过 LOO-CV 获得 CI（我在 N2 中要求的），类似的方法是否可以应用于其他阶段？

**Q2: CoNLL entity construction 负面结果的 per-entity-type 解释**

**论文已部分回答**：Table 43（p36）提供了 Few-NERD 的 per-entity-type MV 分析，Section ak.1（p36）讨论了 "MV direction flips between pretrained and finetuned decoding for 7 of 8 entity types"。但 CoNLL 的 per-entity-type entity construction 结果未在 Appendix 中明确展示。

补充证据：Table 42（p36）显示 CoNLL pretrained MV 基本恢复了 oracle headroom 的 98%——headroom 本身太小（oracle headroom ≈1.6 pp on finetuned），entity construction 几乎没有空间操作。

**Q3: Degeneracy filtering + entity construction 组合**

**论文已部分回答**：Table 57（p42, Appendix ak.2）报告了 "LP selection on the favorable subset (non-degenerate instances with within-instance LP range exceeding the dataset-specific median)"。SciERC 上 restricted subset 恢复了 significant LP gain，Few-NERD 上 trend 方向一致但 CI 包含零。这不完全等于 R2 提出的 "degeneracy filtering + entity construction" 组合，但思路相似。

**建议**：这是一个值得作者在 rebuttal 中回应的消融实验——先 filter 掉 degenerate instances，再在剩余实例上做 entity construction，是否能获得更一致的 gains？

**Q4: 适用于其他 structured prediction 任务的证据**

RE（Appendix o, Tables 29-30, p29）和 SQL（§7.5, 一句话, 87.2% degeneracy）是仅有的跨任务证据。RE 结果实际上显示 cascade 行为与 NER 显著不同（40% instances zero F1, LP selection 失败），这 **并不完全支持** generalization——它表明 cascade 可以 *apply* 于 RE，但诊断结论完全不同。SQL 证据几乎不存在。

我在自己的 W4 中也指出了这一问题。

---

### 对 R2 Missing References 的回应

**[AGREE]** Snell et al. (2025) 和 Eikema et al. (2025) 均应更深入讨论。具体理由见 W6 回应。

---

### 综合评估：R1 对 R2 Overall 评分的意见

R2 给出 Overall 3.0（Findings）。我给出 3.5（Borderline Conference）。差异主要在于：

1. **Framework 定位**（R2-N1）：我认为 Appendix ac 的 3-step protocol 使本文超越了典型 empirical study，"diagnostic framework" 定位基本成立。R2 的 "empirical study" 降级过于严格。

2. **Novelty increment**（R2-N3）：我认为四阶段 cascade + instance-level analysis 的组合确实是新的。没有先前工作提供了这种系统性的、定量化的、per-instance 诊断。R2 低估了框架本身的贡献。

3. **CoNLL tautology 批评**（R2-W5）：我不同意这是 tautological——cascade 的诊断价值在于 *排除* 其他假设并锁定 specific bottleneck，而非仅仅 observe 高 degeneracy。

**我与 R2 的共识点**：
- Prescriptive arm 薄弱（R2-N2 ≈ 我的 W3）
- Related Work 覆盖不足（R2-W6 ≈ 我的 W6）
- 模型规模覆盖有限（R2-L1 ≈ 我的 N3）
- 信息密度高（R2-W2）

**结论**：论文的 Discover + Diagnose 两阶段贡献足以达到 Borderline Conference 水平；Prescriptive 阶段需要降级叙事但不构成拒稿理由。我维持 3.5 的评分。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 3676 · 2026-05-22T09:01:14.253495+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': '收集 Reviewer 1 审稿意见', 'status': 'completed', 'activeForm': '已收到 Reviewer 1 审稿意见'}, {'content': '收集 Reviewer 2 审稿意见', 'status': 'completed', 'activeForm': '已收到 Reviewer 2 审稿意见'}, {'content': '交叉分享：将 R1 意见转发给 R2，R2 意见转发给 R1', 'status': 'completed', 'activeForm': '交叉分享已完成'}, {'content': '收敛判断：分析共识与分歧', 'status': 'in_progress', 'activeForm': '分析收敛情况'}, {'content': '合成最终报告并投递', 'status': 'pending', 'activeForm': '合成并投递审稿报告'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': '收集 Reviewer 1 审稿意见', 'status': 'completed', 'activeForm': '已收到 Reviewer 1 审稿意见'}, {'content': '收集 Reviewer 2 审稿意见', 'status': 'completed', 'activeForm': '已收到 Reviewer 2 审稿意见'}, {'content': '交叉分享：将 R1 意见转发给 R2，R2 意见转发给 R1', 'status': 'completed', 'activeForm': '交叉分享已完成'}, {'content': '收敛判断：分析共识与分歧', 'status': 'in_progress', 'activeForm': '分析收敛情况'}, {'content': '合成最终报告并投递', 'status': 'pending', 'activeForm': '合成并投递审稿报告'}]"
  }
}
```

</details>

---


### Tool result

_source line 3677 · 2026-05-22T09:01:14.254048+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 3678 · 2026-05-22T09:01:50.222226+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': '收集 Reviewer 1 审稿意见', 'status': 'completed', 'activeForm': '已收到 Reviewer 1 审稿意见'}, {'content': '收集 Reviewer 2 审稿意见', 'status': 'completed', 'activeForm': '已收到 Reviewer 2 审稿意见'}, {'content': '交叉分享：将 R1 意见转发给 R2，R2 意见转发给 R1', 'status': 'completed', 'activeForm': '交叉分享已完成'}, {'content': '收敛判断：分析共识与分歧', 'status': 'completed', 'activeForm': '收敛分析已完成'}, {'content': '合成最终报告并投递', 'status': 'in_progress', 'activeForm': '合成并投递审稿报告'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': '收集 Reviewer 1 审稿意见', 'status': 'completed', 'activeForm': '已收到 Reviewer 1 审稿意见'}, {'content': '收集 Reviewer 2 审稿意见', 'status': 'completed', 'activeForm': '已收到 Reviewer 2 审稿意见'}, {'content': '交叉分享：将 R1 意见转发给 R2，R2 意见转发给 R1', 'status': 'completed', 'activeForm': '交叉分享已完成'}, {'content': '收敛判断：分析共识与分歧', 'status': 'completed', 'activeForm': '收敛分析已完成'}, {'content': '合成最终报告并投递', 'status': 'in_progress', 'activeForm': '合成并投递审稿报告'}]"
  }
}
```

</details>

---


### Tool result

_source line 3679 · 2026-05-22T09:01:50.222729+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 3680 · 2026-05-22T09:01:53.785903+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 3681 · 2026-05-22T09:01:53.937006+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-22T08:46:20.230656+00:00\", \"completed_at\": \"2026-05-22T08:51:20.440715+00:00\", \"findings\": [{\"severity\": \"info\", \"dimension\": \"agent_error\", \"message\": \"[ERROR] Agent timed out after 300s\"}], \"counts\": {\"critical\": 0, \"warning\": 0, \"info\": 1}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 3682 · 2026-05-22T09:01:53.937428+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 3683 · 2026-05-22T09:01:54.038229+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"pending\", \"paper_pdf_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_round_34/submitted.pdf\", \"venue\": \"EMNLP 2026\", \"requested_at\": \"2026-05-22T08:47:10.734659+00:00\", \"reminder_hours\": 8, \"chat_id\": \"oc_1b56445332d8ca2b4964b30f300f0e00\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 3684 · 2026-05-22T09:02:19.335471+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 3685 · 2026-05-22T09:02:19.386324+00:00_

1	issues:
2	- id: R1-N1
3	  summary: "θ_crit=0.70 阈值缺乏 held-out 验证"
4	  category: method
5	  severity: warning
6	  status: in_progress
7	  first_raised_round: 33
8	  last_seen_round: 33
9	  mentions:
10	    - round: 33
11	      reviewers: [1]
12	      note: "R1 认为 Must-Fix（post-hoc fitting 风险）；R2 反驳称有 Corollary 1 理论支撑，降级为 Should-Fix。共识：理论基础 sound 但缺 held-out validation 和 sensitivity sweep。"
13	  action_items:
14	    - round: 33
15	      action: "Agent CPU: sweep θ∈{0.60,0.65,0.70,0.75,0.80}，检查 Table 31 结论稳定性；在 RE 上验证"
16	      assigned_to: agent
17	      status: in_progress
18	  resolution: ""
19	  resolution_round: null
20	
21	- id: R1-N3
22	  summary: "Entity construction 作为 prescriptive contribution 证据不足"
23	  category: experiment
24	  severity: warning
25	  status: in_progress
26	  first_raised_round: 33
27	  last_seen_round: 33
28	  mentions:
29	    - round: 33
30	      reviewers: [1, 2]
31	      note: "双方共识：(a) 阈值 k per-dataset 优化无部署策略；(b) Holm-Bonferroni 全局校正后多数 construction 结果不显著；(c) CoNLL 无增益。"
32	  action_items:
33	    - round: 33
34	      action: "Paper Agent: 降级 construction 为 exploratory result；加 Xie et al. (2023) 对比；§7.5 加 k deployment note"
35	      assigned_to: paper_agent
36	      status: in_progress
37	  resolution: ""
38	  resolution_round: null
39	
40	- id: R2-W1
41	  summary: "Entity-level construction 与 Xie et al. (2023) 差异不清晰"
42	  category: framing
43	  severity: warning
44	  status: in_progress
45	  first_raised_round: 33
46	  last_seen_round: 33
47	  mentions:
48	    - round: 33
49	      reviewers: [1, 2]
50	      note: "双方 AGREE。Section 6.1 和 Section 8 对 Xie et al. (2023) entity voting 的增量贡献阐述不充分。"
51	  action_items:
52	    - round: 33
53	      action: "Paper Agent: 在 §6.1 或 §7.5 增加与 Xie et al. 的显式对比（LP-weighted vs majority voting）"
54	      assigned_to: paper_agent
55	      status: in_progress
56	  resolution: ""
57	  resolution_round: null
58	
59	- id: R2-W3
60	  summary: "Framework vs empirical study 定位模糊"
61	  category: framing
62	  se
…[truncated 4486 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 3686 · 2026-05-22T09:03:51.852344+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "struct_self_consist_ie",
  "issues_yaml": "issues:\n- id: R1-N1\n  summary: \"θ_crit=0.70 阈值缺乏 held-out 验证\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 33\n  last_seen_round: 34\n  mentions:\n    - round: 33\n      reviewers: [1]\n      note: \"R1 认为 Must-Fix（post-hoc fitting 风险）；R2 反驳称有 Corollary 1 理论支撑，降级为 Should-Fix。共识：理论基础 sound 但缺 held-out validation 和 sensitivity sweep。\"\n    - round: 34\n      reviewers: [1, 2]\n      note: \"R1 再次列为 Must-Fix (N2)；R2 同意需要澄清但建议降级为 Should-Fix，认为 θ_crit 更像描述性发现而非模型参数。共识：需明确定位（descriptive vs normative）并报告 sensitivity/LOO-CV。\"\n  action_items:\n    - round: 33\n      action: \"Agent CPU: sweep θ∈{0.60,0.65,0.70,0.75,0.80}，检查 Table 31 结论稳定性；在 RE 上验证\"\n      assigned_to: agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R1-N3\n  summary: \"Entity construction 作为 prescriptive contribution 证据不足\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 33\n  last_seen_round: 34\n  mentions:\n    - round: 33\n      reviewers: [1, 2]\n      note: \"双方共识：(a) 阈值 k per-dataset 优化无部署策略；(b) Holm-Bonferroni 全局校正后多数 construction 结果不显著；(c) CoNLL 无增益。\"\n    - round: 34\n      reviewers: [1, 2]\n      note: \"双方 AGREE prescriptive arm 薄弱。R1-W3 指出 Abstract prescriptive 口吻与 Section 7.5 exploratory 标记矛盾。R2-N2 认为三阶段叙事 Prescribe 阶段不完整。共识：应降级为 exploratory with promising but inconsistent initial results。\"\n  action_items:\n    - round: 33\n      action: \"Paper Agent: 降级 construction 为 exploratory result；加 Xie et al. (2023) 对比；§7.5 加 k deployment note\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R2-W1\n  summary: \"Entity-level construction 与 Xie et al. (2023) 差异不清晰\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 33\n  last_seen_round: 34\n  mentions:\n    - round: 33\n      reviewers: [1, 2]\n      note: \"双方 AGREE。Section 6.1 和 Section 8 对 Xie et al. (2023) entity voting 的增量贡献阐述不充分。\"\n    - round: 34\n      reviewers: [2]\n      note: \"R2-N3 再次指出本文 entity-level construction 本质是 Xie entity voting + LP weighting，增量幅度需更直接说明。R1 交叉回应中提供了详细对比表，认为增量显著但论文表述不够直接。\"\n  action_items:\n    - round: 33\n      action: \"Paper Agent: 在 §6.1 或 §7.5 增加与 Xie et al. 的显式对比（LP-weighted vs majority voting）\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R2-W3\n  summary: \"Framework vs empirical study 定位模糊\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 33\n  last_seen_round: 34\n  mentions:\n    - round: 33\n      reviewers: [1, 2]\n      note: \"R2 提出，R1 部分同意。标题用 'Diagnostic Framework' 但实际更接近分析方法论贡献。\"\n    - round: 34\n      reviewers: [1, 2]\n      note: \"R2-N1 再次列为 Must-Fix（建议改标题为 empirical study）。R1 REBUT：Appendix ac 的 3-step protocol 使其超越典型 empirical study。分歧未解决——R1 认为 diagnostic framework 成立，R2 认为过高。\"\n  action_items:\n    - round: 33\n      action: \"Paper Agent: §1 contributions 列表拆分为 diagnostic methodology / formal characterization / empirical findings 三类\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R2-W6\n  summary: \"Related Work (Section 8) 覆盖不足\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 33\n  last_seen_round: 34\n  mentions:\n    - round: 33\n      reviewers: [1, 2]\n      note: \"双方 AGREE。~15 行不足。需补 MBR for structured NLP、LLM calibration、Yao/Yun concurrent works。\"\n    - round: 34\n      reviewers: [1, 2]\n      note: \"双方 AGREE。R2-W6 指出 Snell et al. (2025)、Eikema et al. (2025) structure-conditional MBR、calibration 文献讨论不足。R1 交叉回应完全同意。\"\n  action_items:\n    - round: 33\n      action: \"Paper Agent: 扩展至 20-25 行，从 Table 66 提炼对比，补充引用（需验证）\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R2-N1\n  summary: \"实验 setup (Section 7.1) 位于结果之后影响可读性\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 33\n  last_seen_round: 34\n  mentions:\n    - round: 33\n      reviewers: [2]\n      note: \"R2 认为 Must-Fix；R1 反驳称 Section 2.3 已提供关键参数，降级为 Should-Fix。\"\n    - round: 34\n      reviewers: [1, 2]\n      note: \"R2-W1 再次指出实验结果分散在 Sections 3-7。R1 REBUT 认为这是有意的 Discover→Diagnose→Prescribe 叙事弧。分歧：R1 认为结构合理，R2 认为影响可读性。\"\n  action_items:\n    - round: 33\n      action: \"Paper Agent: §2 末尾加 1-2 段实验概览\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R2-N2\n  summary: \"模型覆盖面不足以支撑跨规模泛化声明\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 33\n  last_seen_round: 34\n  mentions:\n    - round: 33\n      reviewers: [2]\n      note: \"R2 认为仅 2 个 8B 模型（Must-Fix）；R1 反驳论文覆盖 4 家族 3B-72B。降级为 Should-Fix（主文呈现不足）。\"\n    - round: 34\n      reviewers: [1, 2]\n      note: \"R1-N3 列为 Must-Fix（主要依赖 2 个 8B FT，GPT-5.5 仅 200 instances zero-shot，14B 仅 SciERC）。R2 完全同意。双方共识：claim 范围应限定为 7-14B fine-tuned + selected zero-shot frontier models。\"\n  action_items:\n    - round: 34\n      action: \"Paper Agent: 正文限定 claim 范围，将 cross-scale consistency 降级为 tentative observation\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R1-W2\n  summary: \"部分关键检验 underpowered (n=23)\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 33\n  last_seen_round: 34\n  mentions:\n    - round: 33\n      reviewers: [1, 2]\n      note: \"双方 AGREE。Cross-dataset degeneracy-LP correlation (n=23) 只能检测 ρ>0.5。论文已透明报告 power analysis。\"\n    - round: 34\n      reviewers: [1, 2]\n      note: \"R1-W5 再次提出。R2 REBUT：这是领域固有限制，非本文特有问题，提及即可。\"\n  action_items:\n    - round: 33\n      action: \"已有 power analysis 公开；在讨论 non-significant 结果时注明 power 限制\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R1-W4\n  summary: \"RE 和 SQL 扩展覆盖有限\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 33\n  last_seen_round: 34\n  mentions:\n    - round: 33\n      reviewers: [1, 2]\n      note: \"双方 AGREE。RE 仅 SciERC RE (n=397)，SQL 仅类比讨论。\"\n    - round: 34\n      reviewers: [1, 2]\n      note: \"R1-W4 再次指出 RE 仅 SciERC 且 cascade 行为与 NER 显著不同（40% zero F1）。R2 同意 Abstract/Introduction 的 structured IE 措辞超出实验证据。双方共识：限定泛化范围或补充独立 RE dataset。\"\n  action_items:\n    - round: 33\n      action: \"Paper Agent: RE cascade 段升级为正面跨任务证据（4-5 行 + appendix 引用），弱化泛化声明为 'cross-task diagnostic validation'\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R2-M1\n  summary: \"Table 1 '2-seed' vs 正文 '3-seed' 不一致\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 33\n  last_seen_round: 34\n  mentions:\n    - round: 33\n      reviewers: [1, 2]\n      note: \"双方 AGREE。需在 Section 7.1 中说明不同实验使用的 seed 数量差异。\"\n    - round: 34\n      reviewers: [1, 2]\n      note: \"R1-W2 再次指出。R2 交叉回应 AGREE。仍未解决。\"\n  action_items:\n    - round: 33\n      action: \"Paper Agent: 统一 seed 数量描述或说明原因\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R33-Q3\n  summary: \"GPT-5.5 parse failure (10.1%) 排除后是否偏移 gap 估计\"\n  category: experiment\n  severity: info\n  status: in_progress\n  first_raised_round: 33\n  last_seen_round: 33\n  mentions:\n    - round: 33\n      reviewers: [1, 2]\n      note: \"需要验证排除 parse failure 前后的 correlation-selection gap 估计是否系统偏移。\"\n    - round: 34\n      reviewers: []\n      note: \"本轮未被任何 Reviewer 提及。论文脚注已注明 88% 空集对应 gold-empty instances，真实 parse failure 仅 1.2%。可能已部分解决，待 Research Director 确认。\"\n  action_items:\n    - round: 33\n      action: \"Agent CPU: 计算排除前后 ρ 和 MV Δ 差异\"\n      assigned_to: agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R34-N1\n  summary: \"全局 Holm-Bonferroni (k=57) 下核心 NER claim 不显著 (p_HB=0.055)，主文未充分讨论\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 34\n  last_seen_round: 34\n  mentions:\n    - round: 34\n      reviewers: [1, 2]\n      note: \"R1-N1 列为 Must-Fix。Table 12 显示全局校正下 no core NER claim survives；正文使用 family-wise (较小 k) 未在主文中告知全局结果。R2 交叉回应 AGREE 并补充：与 framework 定位问题关联——统计 claim 脆弱则 framework 更需谨慎。双方共识：主文需透明报告全局校正结果，为 family-wise 分组提供先验理由，考虑报告 BH FDR。\"\n  action_items:\n    - round: 34\n      action: \"Paper Agent: Discussion/Limitations 增加 1-2 句全局 Holm-Bonferroni 结果；为 family-wise 分组提供先验理由；报告 BH FDR 作为补充\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R34-W1\n  summary: \"Free-form decoding 消融仅覆盖 SciERC，CoNLL/WNUT-17 缺失\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 34\n  last_seen_round: 34\n  mentions:\n    - round: 34\n      reviewers: [1, 2]\n      note: \"R1-W1 提出。R2 交叉回应 AGREE：CoNLL entity types 少、schema 简单，constrained decoding 可能是高 degeneracy 的主要驱动因素。如果 CoNLL free-form degeneracy 大幅下降，cascade 诊断结论需重新解读。\"\n  action_items:\n    - round: 34\n      action: \"Agent: 在 CoNLL 上补充 free-form decoding ablation，或在正文中讨论 constrained decoding 放大 degeneracy 的机制\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R34-W2\n  summary: \"与 Yun et al. (2025) diversity collapse 关系讨论不充分\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 34\n  last_seen_round: 34\n  mentions:\n    - round: 34\n      reviewers: [1, 2]\n      note: \"R1-W6 和 R2-N3 第 4 点均指出。Degeneracy 是否为 diversity collapse 在 structured decoding 下的特例？Constrained decoding 是否同时驱动两者？双方 AGREE 需深入讨论。\"\n  action_items:\n    - round: 34\n      action: \"Paper Agent: Discussion 增加 2-3 句讨论 constrained decoding 作为 confound 的可能性，引用 Appendix q free-form 消融\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R34-R2-N3\n  summary: \"相对于 Yao/Chen/Xie/Yun 的增量贡献在论文中界定不清\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 34\n  last_seen_round: 34\n  mentions:\n    - round: 34\n      reviewers: [1, 2]\n      note: \"R2-N3 列为 Must-Fix。R1 REBUT 并提供了详细对比表证明增量显著（instance-level vs task-level, quantitative cascade vs qualitative failure modes）。分歧：R2 认为增量不清晰（影响评分），R1 认为增量存在但论文表述需改进。共识：Section 8 应增加 'What's new' 段落明确阐述增量。\"\n  action_items:\n    - round: 34\n      action: \"Paper Agent: Section 8 增加显式 'What's new' 对比段落（vs Yao, Chen, Xie, Yun）\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R34-R2-L3\n  summary: \"Prompt sensitivity 未在 Limitations 中讨论\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 34\n  last_seen_round: 34\n  mentions:\n    - round: 34\n      reviewers: [1, 2]\n      note: \"R2 提出，R1 交叉回应 AGREE。Constrained decoding 减轻格式变异但 prompt 措辞仍可能影响 entity recall、degeneracy rate、LP 分布。\"\n  action_items:\n    - round: 34\n      action: \"Paper Agent: Limitations 增加一句关于 prompt sensitivity 未测试\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "issues_yaml": "issues:\n- id: R1-N1\n  summary: \"θ_crit=0.70 阈值缺乏 held-out 验证\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 33\n  last_seen_round: 34\n  mentions:\n    - round: 33\n      reviewers: [1]\n      note: \"R1 认为 Must-Fix（post-hoc fitting 风险）；R2 反驳称有 Corollary 1 理论支撑，降级为 Should-Fix。共识：理论基础 sound 但缺 held-out validation 和 sensitivity sweep。\"\n    - round: 34\n      reviewers: [1, 2]\n      note: \"R1 再次列为 Must-Fix (N2)；R2 同意需要澄清但建议降级为 Should-Fix，认为 θ_crit 更像描述性发现而非模型参数。共识：需明确定位（descriptive vs normative）并报告 sensitivity/LOO-CV。\"\n  action_items:\n    - round: 33\n      action: \"Agent CPU: sweep θ∈{0.60,0.65,0.70,0.75,0.80}，检查 Table 31 结论稳定性；在 RE 上验证\"\n      assigned_to: agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R1-N3\n  summary: \"Entity construction 作为 prescriptive contribution 证据不足\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 33\n  last_seen_round: 34\n  mentions:\n    - round: 33\n      reviewers: [1, 2]\n      note: \"双方共识：(a) 阈值 k per-dataset 优化无部署策略；(b) Holm-Bonferroni 全局校正后多数 construction 结果不显著；(c) CoNLL 无增益。\"\n    - round: 34\n      reviewers: [1, 2]\n      note: \"双方 AGREE prescriptive arm 薄弱。R1-W3 指出 Abstract prescriptive 口吻与 Section 7.5 exploratory 标记矛盾。R2-N2 认为三阶段叙事 Prescribe 阶段不完整。共识：应降级为 exploratory with promising but inconsistent initial results。\"\n  action_items:\n    - round: 33\n      action: \"Paper Agent: 降级 construction 为 exploratory result；加 Xie et al. (2023) 对比；§7.5 加 k deployment note\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R2-W1\n  summary: \"Entity-level construction 与 Xie et al. (2023) 差异不清晰\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 33\n  last_seen_round: 34\n  mentions:\n    - round: 33\n      reviewers: [1, 2]\n      note: \"双方 AGREE。Section 6.1 和 Section 8 对 Xie et al. (2023) entity voting 的增量贡献阐述不充分。\"\n    - round: 34\n      reviewers: [2]\n      note: \"R2-N3 再次指出本文 entity-level construction 本质是 Xie entity voting + LP weighting，增量幅度需更直接说明。R1 交叉回应中提供了详细对比表，认为增量显著但论文表述不够直接。\"\n  action_items:\n    - round: 33\n      action: \"Paper Agent: 在 §6.1 或 §7.5 增加与 Xie et al. 的显式对比（LP-weighted vs majority voting）\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R2-W3\n  summary: \"Framework vs empirical study 定位模糊\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 33\n  last_seen_round: 34\n  mentions:\n    - round: 33\n      reviewers: [1, 2]\n      note: \"R2 提出，R1 部分同意。标题用 'Diagnostic Framework' 但实际更接近分析方法论贡献。\"\n    - round: 34\n      reviewers: [1, 2]\n      note: \"R2-N1 再次列为 Must-Fix（建议改标题为 empirical study）。R1 REBUT：Appendix ac 的 3-step protocol 使其超越典型 empirical study。分歧未解决——R1 认为 diagnostic framework 成立，R2 认为过高。\"\n  action_items:\n    - round: 33\n      action: \"Paper Agent: §1 contributions 列表拆分为 diagnostic methodology / formal characterization / empirical findings 三类\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R2-W6\n  summary: \"Related Work (Section 8) 覆盖不足\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 33\n  last_seen_round: 34\n  mentions:\n    - round: 33\n      reviewers: [1, 2]\n      note: \"双方 AGREE。~15 行不足。需补 MBR for structured NLP、LLM calibration、Yao/Yun concurrent works。\"\n    - round: 34\n      reviewers: [1, 2]\n      note: \"双方 AGREE。R2-W6 指出 Snell et al. (2025)、Eikema et al. (2025) structure-conditional MBR、calibration 文献讨论不足。R1 交叉回应完全同意。\"\n  action_items:\n    - round: 33\n      action: \"Paper Agent: 扩展至 20-25 行，从 Table 66 提炼对比，补充引用（需验证）\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R2-N1\n  summary: \"实验 setup (Section 7.1) 位于结果之后影响可读性\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 33\n  last_seen_round: 34\n  mentions:\n    - round: 33\n      reviewers: [2]\n      note: \"R2 认为 Must-Fix；R1 反驳称 Section 2.3 已提供关键参数，降级为 Should-Fix。\"\n    - round: 34\n      reviewers: [1, 2]\n      note: \"R2-W1 再次指出实验结果分散在 Sections 3-7。R1 REBUT 认为这是有意的 Discover→Diagnose→Prescribe 叙事弧。分歧：R1 认为结构合理，R2 认为影响可读性。\"\n  action_items:\n    - round: 33\n      action: \"Paper Agent: §2 末尾加 1-2 段实验概览\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R2-N2\n  summary: \"模型覆盖面不足以支撑跨规模泛化声明\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 33\n  last_seen_round: 34\n  mentions:\n    - round: 33\n      reviewers: [2]\n      note: \"R2 认为仅 2 个 8B 模型（Must-Fix）；R1 反驳论文覆盖 4 家族 3B-72B。降级为 Should-Fix（主文呈现不足）。\"\n    - round: 34\n      reviewers: [1, 2]\n      note: \"R1-N3 列为 Must-Fix（主要依赖 2 个 8B FT，GPT-5.5 仅 200 instances zero-shot，14B 仅 SciERC）。R2 完全同意。双方共识：claim 范围应限定为 7-14B fine-tuned + selected zero-shot frontier models。\"\n  action_items:\n    - round: 34\n      action: \"Paper Agent: 正文限定 claim 范围，将 cross-scale consistency 降级为 tentative observation\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R1-W2\n  summary: \"部分关键检验 underpowered (n=23)\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 33\n  last_seen_round: 34\n  mentions:\n    - round: 33\n      reviewers: [1, 2]\n      note: \"双方 AGREE。Cross-dataset degeneracy-LP correlation (n=23) 只能检测 ρ>0.5。论文已透明报告 power analysis。\"\n    - round: 34\n      reviewers: [1, 2]\n      note: \"R1-W5 再次提出。R2 REBUT：这是领域固有限制，非本文特有问题，提及即可。\"\n  action_items:\n    - round: 33\n      action: \"已有 power analysis 公开；在讨论 non-significant 结果时注明 power 限制\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R1-W4\n  summary: \"RE 和 SQL 扩展覆盖有限\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 33\n  last_seen_round: 34\n  mentions:\n    - round: 33\n      reviewers: [1, 2]\n      note: \"双方 AGREE。RE 仅 SciERC RE (n=397)，SQL 仅类比讨论。\"\n    - round: 34\n      reviewers: [1, 2]\n      note: \"R1-W4 再次指出 RE 仅 SciERC 且 cascade 行为与 NER 显著不同（40% zero F1）。R2 同意 Abstract/Introduction 的 structured IE 措辞超出实验证据。双方共识：限定泛化范围或补充独立 RE dataset。\"\n  action_items:\n    - round: 33\n      action: \"Paper Agent: RE cascade 段升级为正面跨任务证据（4-5 行 + appendix 引用），弱化泛化声明为 'cross-task diagnostic validation'\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R2-M1\n  summary: \"Table 1 '2-seed' vs 正文 '3-seed' 不一致\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 33\n  last_seen_round: 34\n  mentions:\n    - round: 33\n      reviewers: [1, 2]\n      note: \"双方 AGREE。需在 Section 7.1 中说明不同实验使用的 seed 数量差异。\"\n    - round: 34\n      reviewers: [1, 2]\n      note: \"R1-W2 再次指出。R2 交叉回应 AGREE。仍未解决。\"\n  action_items:\n    - round: 33\n      action: \"Paper Agent: 统一 seed 数量描述或说明原因\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R33-Q3\n  summary: \"GPT-5.5 parse failure (10.1%) 排除后是否偏移 gap 估计\"\n  category: experiment\n  severity: info\n  status: in_progress\n  first_raised_round: 33\n  last_seen_round: 33\n  mentions:\n    - round: 33\n      reviewers: [1, 2]\n      note: \"需要验证排除 parse failure 前后的 correlation-selection gap 估计是否系统偏移。\"\n    - round: 34\n      reviewers: []\n      note: \"本轮未被任何 Reviewer 提及。论文脚注已注明 88% 空集对应 gold-empty instances，真实 parse failure 仅 1.2%。可能已部分解决，待 Research Director 确认。\"\n  action_items:\n    - round: 33\n      action: \"Agent CPU: 计算排除前后 ρ 和 MV Δ 差异\"\n      assigned_to: agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R34-N1\n  summary: \"全局 Holm-Bonferroni (k=57) 下核心 NER claim 不显著 (p_HB=0.055)，主文未充分讨论\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 34\n  last_seen_round: 34\n  mentions:\n    - round: 34\n      reviewers: [1, 2]\n      note: \"R1-N1 列为 Must-Fix。Table 12 显示全局校正下 no core NER claim survives；正文使用 family-wise (较小 k) 未在主文中告知全局结果。R2 交叉回应 AGREE 并补充：与 framework 定位问题关联——统计 claim 脆弱则 framework 更需谨慎。双方共识：主文需透明报告全局校正结果，为 family-wise 分组提供先验理由，考虑报告 BH FDR。\"\n  action_items:\n    - round: 34\n      action: \"Paper Agent: Discussion/Limitations 增加 1-2 句全局 Holm-Bonferroni 结果；为 family-wise 分组提供先验理由；报告 BH FDR 作为补充\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R34-W1\n  summary: \"Free-form decoding 消融仅覆盖 SciERC，CoNLL/WNUT-17 缺失\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 34\n  last_seen_round: 34\n  mentions:\n    - round: 34\n      reviewers: [1, 2]\n      note: \"R1-W1 提出。R2 交叉回应 AGREE：CoNLL entity types 少、schema 简单，constrained decoding 可能是高 degeneracy 的主要驱动因素。如果 CoNLL free-form degeneracy 大幅下降，cascade 诊断结论需重新解读。\"\n  action_items:\n    - round: 34\n      action: \"Agent: 在 CoNLL 上补充 free-form decoding ablation，或在正文中讨论 constrained decoding 放大 degeneracy 的机制\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R34-W2\n  summary: \"与 Yun et al. (2025) diversity collapse 关系讨论不充分\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 34\n  last_seen_round: 34\n  mentions:\n    - round: 34\n      reviewers: [1, 2]\n      note: \"R1-W6 和 R2-N3 第 4 点均指出。Degeneracy 是否为 diversity collapse 在 structured decoding 下的特例？Constrained decoding 是否同时驱动两者？双方 AGREE 需深入讨论。\"\n  action_items:\n    - round: 34\n      action: \"Paper Agent: Discussion 增加 2-3 句讨论 constrained decoding 作为 confound 的可能性，引用 Appendix q free-form 消融\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R34-R2-N3\n  summary: \"相对于 Yao/Chen/Xie/Yun 的增量贡献在论文中界定不清\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 34\n  last_seen_round: 34\n  mentions:\n    - round: 34\n      reviewers: [1, 2]\n      note: \"R2-N3 列为 Must-Fix。R1 REBUT 并提供了详细对比表证明增量显著（instance-level vs task-level, quantitative cascade vs qualitative failure modes）。分歧：R2 认为增量不清晰（影响评分），R1 认为增量存在但论文表述需改进。共识：Section 8 应增加 'What's new' 段落明确阐述增量。\"\n  action_items:\n    - round: 34\n      action: \"Paper Agent: Section 8 增加显式 'What's new' 对比段落（vs Yao, Chen, Xie, Yun）\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R34-R2-L3\n  summary: \"Prompt sensitivity 未在 Limitations 中讨论\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 34\n  last_seen_round: 34\n  mentions:\n    - round: 34\n      reviewers: [1, 2]\n      note: \"R2 提出，R1 交叉回应 AGREE。Constrained decoding 减轻格式变异但 prompt 措辞仍可能影响 entity recall、degeneracy rate、LP 分布。\"\n  action_items:\n    - round: 34\n      action: \"Paper Agent: Limitations 增加一句关于 prompt sensitivity 未测试\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null"
  }
}
```

</details>

---


### Tool result

_source line 3687 · 2026-05-22T09:03:51.953470+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml\", \"bytes\": 10751}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 3688 · 2026-05-22T09:06:04.853401+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "struct_self_consist_ie",
  "report": "# 审稿报告 — Round 34\n\n**论文**: \"Characterizing the Capability Ceiling of Self-Consistency: A Diagnostic Framework for Test-Time Aggregation in NER\"\n**Venue**: EMNLP 2026 Main Conference (ARR May 2026)\n**截止日期**: 2026-05-25\n**审稿模式**: Fresh（重新审稿）\n**Reviewer 配置**: 2 人（R1: 方法严谨性+实验设计; R2: 新颖性+完整性+写作）\n\n---\n\n## Summary\n\n本文研究 self-consistency（SC）在 NER 上的失效机制。通过四阶段诊断 cascade（QE → degeneracy → agreement fidelity → LP compression），系统性分析了为什么 quality estimation 信号能预测输出质量（Spearman ρ 最高 0.45, AUROC 0.82）但无法在 instance 级别选出更好的候选——即 \"correlation-selection gap\"。实验覆盖 4 个 NER 数据集、2 个模型族（Qwen3-8B, LLaMA-3.1-8B）、9 类方法。探索性的 entity-level construction 在低 degeneracy 条件下（Few-NERD）获得 +1.4 pp 增益，但效果不一致。degeneracy 阈值 θ_crit=0.70 预测 SC 增益何时消失。\n\n---\n\n## Strengths\n\n**S1. 统计实践堪称模范。** [共识] 全面使用 bootstrap 95% CI、permutation test、TOST 等价检验、Holm-Bonferroni 多重比较校正（Table 12, k=57）、post-hoc power analysis。Table 12 的 57 项检验透明报告了全局校正下核心 claim 不达显著（p_HB=0.055），这种统计诚实在 NLP 论文中罕见。\n\n**S2. 实验覆盖和附录深度。** [共识] 4 个 NER 数据集 × 2 模型族 × 9 方法类别 × 16+ 配置，39 页 Appendix 覆盖几乎所有可能的消融角度（温度、sample size、free-form decoding、cross-family、14B scale、epoch confound 等），几乎穷尽了 reviewer 可能提出的消融需求。\n\n**S3. Correlation-selection gap 是有价值的诊断概念。** [共识] 将 quality estimation 与 selection 之间的脱节命名并系统量化，Figure 2 有效可视化了这一 gap。四阶段 cascade 的诊断逻辑清晰，每个阶段有可计算指标。\n\n**S4. 清晰的 observational 定位和实用的负面结论。** [共识] Section 2 开头声明不做因果声明；Section 9 的 diagnostic cascade 提供了可操作的预部署决策树。\n\n**S5. MBR 形式化连接。** Proposition 2 建立了 entity-level construction 与 balanced set-overlap utility 下 MBR 最优性的理论桥梁。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**C1. 全局 Holm-Bonferroni (k=57) 下核心 NER claim 不显著，主文未充分讨论。** [R1 提出, R2 AGREE]\nTable 12 显示全局校正下 p_HB=0.055，\"no core NER claim survives\"。正文使用 family-wise corrected p-values（较小的 k=10, 21, 9），但未在正文中明确告知读者全局校正结果——Appendix e 第 18 页报告了此事实，但作为影响核心结论可信度的关键信息，应在 Discussion 或 Limitations 中显著讨论。此外应为 family-wise 分组提供先验理由（基于研究问题独立性），并报告 BH FDR 作为补充。\n\n**C2. 模型覆盖面不足以支撑跨规模/跨家族泛化声明。** [R1 提出, R2 AGREE]\n主实验仅依赖 2 个 8B fine-tuned 模型（Qwen3-8B, LLaMA-3.1-8B）。GPT-5.5 仅 200 instances zero-shot；14B 仅 SciERC；72B 仅 zero-shot AWQ。Abstract/Introduction 声称 \"treating NER as a representative instance of set-valued generation\"、\"the gap persists across scales and families\"，但实际模型规模基本锁定在 7-8B，且 zero-shot vs fine-tuned 对比不对等。应限定 claim 范围为 \"7-14B fine-tuned + selected zero-shot frontier models\"。\n\n**C3. Prescriptive 阶段薄弱，三阶段叙事不完整。** [双方 AGREE]\nIntroduction 承诺 \"Discover → Diagnose → Prescribe\" 叙事，但 Prescribe 阶段核心产物——entity-level construction——效果不一致（Few-NERD +1.4pp, CoNLL 负面, SciERC +0.2pp non-significant）。Abstract/Discussion 以 prescriptive 口吻呈现，Section 7.5 标记 \"exploratory\"——叙事矛盾。Discussion 结论本质是 \"what NOT to do\" 而非 \"what to do\"。应统一定位为 \"exploratory with promising but inconsistent initial results\"。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1. \"Diagnostic Framework\" 定位与实际贡献之间存在张力。** [R2 Must-Fix, R1 REBUT — 分歧未解决]\nR2 认为 \"framework\" 需要跨任务通用性和预测能力，实际是 empirical study，建议改标题。R1 反驳称 Appendix ac 的 3-step protocol 使其超越典型 empirical study，\"diagnostic framework\" 基本成立。Director 判断：论文的 framework 定位有一定基础（诊断 protocol 可操作），但正文叙事偶尔超出诊断范畴，应更审慎。\n\n**W2. 相对于 Yao et al. (2026)、Chen et al. (2024)、Xie et al. (2023)、Yun et al. (2025) 的增量贡献界定不清。** [R2 Must-Fix, R1 REBUT — 分歧未解决]\nR2 认为增量不够清晰。R1 提供了详细对比表（instance-level vs task-level, quantitative cascade vs qualitative failure modes, LP-weighted vs majority voting, agreement-quality alignment vs diversity）认为增量显著。Director 判断：增量存在但论文 Section 8 表述分散，缺少集中的 \"What's new\" 段落。\n\n**W3. Free-form decoding 消融仅覆盖 SciERC，CoNLL/WNUT-17 缺失。** [R1 提出, R2 AGREE]\nConstrained decoding 可能是 CoNLL 89% degeneracy 的重要驱动因素。如果 CoNLL free-form decoding 的 degeneracy 大幅下降，cascade 对 CoNLL 的诊断结论需修正为 \"constrained decoding is the bottleneck\" 而非 \"SC intrinsically fails\"。\n\n**W4. 与 Yun et al. (2025) diversity collapse 关系讨论不充分。** [双方 AGREE]\nDegeneracy 与 diversity collapse 的概念关系未深入讨论。Constrained decoding 可能同时驱动 diversity collapse 和 LP compression，但论文仅用一句话区分。需在 Discussion 增加 2-3 句讨论 constrained decoding 作为 confound。\n\n**W5. θ_crit=0.70 缺少充分验证。** [R1 Must-Fix, R2 建议降级 — 分歧]\nR1 认为 16 个配置点既拟合又验证，post-hoc fitting 风险。R2 认为 θ_crit 更像描述性发现，不需要 ML 级 held-out 验证，建议降级。Director 判断：降级为 Should-Fix，但需明确定位（descriptive vs normative）并报告 sensitivity sweep 或 LOO-CV。\n\n**W6. 信息密度过高，首次阅读认知负荷极大。** [R2 提出, R1 AGREE]\n几乎每个句子 2-3 个统计量，缩写过多（LP, SJ, FK, VC, EM, MV, QE, AUROC 等）。建议主文聚焦 top-level patterns，详细数字移入 Appendix。\n\n**W7. Related Work 覆盖不足。** [双方 AGREE]\nSnell et al. (2025) \"Scaling LLM Test-Time Compute Optimally\" 与 dataset-dependent optimal strategy 直接相关但未引用。Eikema et al. (2025) structure-conditional MBR 与 Proposition 2 的连接可深化。LLM calibration 文献（Kadavath et al. 2022, Tian et al. 2023）讨论不足。\n\n**W8. RE/SQL 扩展太薄，\"structured IE\" 泛化措辞超出证据。** [双方 AGREE]\nRE 仅 SciERC（397 instances, 40% zero F1），且 cascade 行为与 NER 显著不同。SQL 仅一句话提及（87.2% degeneracy）。标题准确限定为 NER，但 Abstract/Discussion 的 \"structured IE/prediction\" 措辞超出。\n\n**W9. 2-seed vs 3-seed 不对称未说明。** [双方 AGREE]\nTable 1 中 selection signals 使用 2-seed mean，baselines 使用 3-seed，正文未解释原因。\n\n### Minor Issues\n\n- **M1**: Figure 1 \"diagnostic; not causal chain\" 注释好，但箭头视觉暗示因果链，建议用虚线。[双方 AGREE]\n- **M2**: 缩写表（Table 5, Appendix）建议以简化版放入主文。\n- **M3**: Table 2 \"Full coverage in Appendix h.4\" 引用——主文缺少 9 类方法的数据集覆盖概览。\n- **M4**: Table 65 cost-benefit analysis（p45）很有价值，建议在正文提及核心数字。\n- **M5**: 引用括号格式一致性检查（Section 1 有混用）。\n- **M6**: 匿名性无问题。Ethics Statement 和 Checklist 覆盖恰当。\n- **M7**: 正文可能略微溢出 8 页——确认 camera-ready 严格控制。\n- **M8**: Proposition 1/2 的 entity-wise independence 假设应在正文中更明确标注为 simplifying assumption。\n- **M9**: Limitations 应补充 prompt sensitivity 未测试。\n\n---\n\n## Reviewer Consensus\n\n以下问题双方达成共识 [AGREE]：\n\n1. **统计实践是核心优势**——bootstrap CI、Holm-Bonferroni、permutation test 的组合使用是标杆级别\n2. **Prescriptive 阶段薄弱**——entity-level construction 效果不一致，叙事应降级为 exploratory\n3. **模型覆盖面不足**——泛化声明应限定为 7-14B fine-tuned regime\n4. **全局统计校正透明度不足**——主文需讨论 k=57 结果\n5. **Free-form decoding 消融缺失 CoNLL**——constrained decoding 可能放大 degeneracy\n6. **Related Work 覆盖不足**——需补 Snell et al.、Eikema et al.、calibration 文献\n7. **与 Yun et al. diversity collapse 关系需深化**\n8. **2-seed/3-seed 差异需说明**\n\n---\n\n## Reviewer Divergence\n\n| 问题 | R1 立场 | R2 立场 | Director 判断 |\n|------|---------|---------|---------------|\n| Overall 评分 | 3.5 (Borderline Conference) | 3.0 (Findings) | 3.0 (Findings) |\n| Framework 定位 | 基本成立（Appendix ac 3-step protocol）| 过高（应为 empirical study）| 有基础但叙事需审慎收敛 |\n| 新颖性增量 | 显著（详细对比表）| 不够清晰 | 增量存在但论文表述分散 |\n| θ_crit 严重性 | Must-Fix（post-hoc fitting）| Should-Fix（描述性发现）| Should-Fix + 需定位澄清 |\n| CoNLL 高 degeneracy tautology | 非 tautological（cascade 排除了其他假设）| 部分 tautological | R1 论证更有说服力 |\n| Cross-dataset power | Should-Fix | 领域固有限制 | Info 级，提及即可 |\n\n---\n\n## Questions for Authors\n\n1. **CoNLL free-form decoding ablation**: 在 CoNLL 上进行 free-form decoding，degeneracy 率是否显著下降？如果下降，cascade 的 CoNLL 诊断结论是否需修正？\n2. **全局 vs family-wise Holm-Bonferroni**: 按 BH FDR 校正，多少核心 NER claims 能在 FDR<0.05 下成立？\n3. **θ_crit=0.70 LOO-CV**: 每个 fold 的 θ_crit 估计值变异范围是多少？\n4. **GPT-5.5 sampling strategy**: 200-instance 的选择策略（random? stratified?）及完整结果分解？\n5. **Degeneracy filtering + entity construction**: 仅对非 degenerate instances 做 construction，收益是否更大且更一致？\n\n---\n\n## Missing References\n\n1. **Snell et al. (2025)** \"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\" (ICLR 2025)——compute-optimal test-time scaling 策略，与 dataset-dependent optimal strategy 发现直接相关。[双方 AGREE 应引用]\n2. **Eikema et al. (2025)** structure-conditional MBR——已引用但讨论不足，与 Proposition 2 的连接应深化。[双方 AGREE]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态**：pending（已于 2026-05-22T08:47 发送请求，尚未返回）。如用户收到外部审稿结果，将作为补充材料追加。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**：Agent 超时（300s timeout）。未产出排版检查结果。用户可选择重新触发视觉审查。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 (Findings)**\n\n**置信度**: 4/5\n\n**评分理由**:\n\n本文在 self-consistency 对 NER 的失效机制上提供了迄今最系统、最严谨的诊断分析，统计实践堪称模范，47 页的分析深度令人印象深刻。Correlation-selection gap 是有用的概念，四阶段 cascade 的诊断逻辑清晰。\n\n评 Findings 而非 Conference 的核心原因：\n1. **统计脆弱性**：核心 NER claim 在全局 Holm-Bonferroni (k=57) 下 p_HB=0.055，未达显著——family-wise 分组虽可辩护但主文透明度不足。\n2. **Prescriptive arm 不完整**：entity-level construction 仅在 Few-NERD 有显著且一致的增益，三阶段叙事的 Prescribe 阶段无法支撑。\n3. **泛化证据有限**：模型覆盖主要锁定在 8B fine-tuned，跨规模声明缺乏 ≥30B fine-tuned 证据；RE/SQL 扩展过于初步。\n4. **定位-内容张力**：\"Diagnostic Framework\" 定位有一定基础但超出了当前验证范围（跨任务通用性不足、formal 决策边界不完整）。\n\n**提升路径**（如果 rebuttal/修改能回应以下问题，可升至 3.5 Borderline Conference）：\n- 主文透明报告全局 Holm-Bonferroni + BH FDR 结果\n- 统一 Prescriptive 叙事为 exploratory\n- 限定 claim 范围（模型规模、任务泛化）\n- Section 8 增加集中的增量贡献阐述\n- CoNLL free-form ablation 或充分讨论 constrained decoding confound\n\n---\n\n## Detailed Comments\n\n### Section 1 (Introduction)\n- \"Discover → Diagnose → Prescribe\" 三阶段叙事中 Prescribe 阶段的承诺过高。建议调整为 \"Discover → Diagnose → Explore bypasses\"。\n- 与 Yao et al. (2026)、Chen et al. (2024)、Xie et al. (2023)、Yun et al. (2025) 的差异化定位应前移到 Introduction，而非留到 Section 8。\n\n### Section 2 (Diagnostic Framework)\n- \"Capability ceiling\" 的 N≤16 定义较窄。R1 论证该概念不依赖固定 N（gap 随 N 增大而扩大），但正文定义与后续 N=32/64 实验存在张力。\n- Experimental setup 概览应在此处或之后增加 1-2 段，帮助读者在遇到 Section 3-6 的实验数据时有上下文。\n\n### Sections 3-4 (Mechanistic + Selection Gap)\n- Introspection boundary 发现（ESJ AUROC 0.51 vs hidden-state probe 0.63-0.88）有趣但机制解释较浅。\n- Table 1 的 2-seed/3-seed 差异需说明。\n- Selection alignment α→0 是核心发现但叙事上被 degeneracy 讨论淹没——建议在 Section 4 更突出 α 的 binding constraint 角色。\n\n### Section 5 (Adaptive Methods)\n- Table 2（9 method categories）信息密集但缺少主文中的数据集覆盖概览。\n- Cross-model ensemble（+0.42pp）仅在 Few-NERD 单数据集测试。\n\n### Section 6 (Theory/Scaling)\n- Proposition 1 应更明确标注为 descriptive formalization。Proposition 2 的 MBR 连接是更实质性的理论贡献。\n- Inverse scaling under adaptive thresholds 的发现（40/58 transitions 变差）重要但讨论偏技术，实践含义可更直接。\n\n### Section 7 (Experiments)\n- 实验设置在 Section 7.1 出现较晚——读者已在 Sections 3-6 消化了大量结果。\n- Few-NERD 3 epochs vs others 5 epochs 的混淆需更显著讨论（不仅在 Appendix ab）。\n\n### Section 8 (Related Work)\n- 缺少与 Snell et al. (2025) compute-optimal scaling 的对比。\n- 与 Yun et al. (2025) 的关系需从 1 句扩展到 1 段——特别是 constrained decoding 作为共同 confound。\n- 建议增加集中的 \"What's new\" 对比段落。\n\n### Section 9 (Discussion and Conclusion)\n- 结论本质是 diagnostic（\"when not to use SC\"）而非 prescriptive。建议与 Introduction 的叙事对齐。\n- Practical implications 段落有价值，可考虑增加 cost-benefit 数字（Table 65）。\n\n### Limitations\n- 覆盖较好但遗漏：(a) prompt sensitivity 未测试；(b) 仅 8B fine-tuned 主实验，larger model fine-tuned 行为未知。\n- 全局 Holm-Bonferroni 下核心 claim 脆弱性应在此处或 Discussion 讨论。\n\n### Appendix\n- 极其详尽，几乎所有主文 claim 有对应消融。Appendix ac 的 3-step evaluation protocol 有实用价值。\n- Table 65 cost-benefit analysis 建议提升到正文。",
  "reviewer_ids_acknowledged": "[\"1\", \"2\"]",
  "cross_response_reviewer_ids": "[\"1\", \"2\"]",
  "overall_score": "3.0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "report": "# 审稿报告 — Round 34\n\n**论文**: \"Characterizing the Capability Ceiling of Self-Consistency: A Diagnostic Framework for Test-Time Aggregation in NER\"\n**Venue**: EMNLP 2026 Main Conference (ARR May 2026)\n**截止日期**: 2026-05-25\n**审稿模式**: Fresh（重新审稿）\n**Reviewer 配置**: 2 人（R1: 方法严谨性+实验设计; R2: 新颖性+完整性+写作）\n\n---\n\n## Summary\n\n本文研究 self-consistency（SC）在 NER 上的失效机制。通过四阶段诊断 cascade（QE → degeneracy → agreement fidelity → LP compression），系统性分析了为什么 quality estimation 信号能预测输出质量（Spearman ρ 最高 0.45, AUROC 0.82）但无法在 instance 级别选出更好的候选——即 \"correlation-selection gap\"。实验覆盖 4 个 NER 数据集、2 个模型族（Qwen3-8B, LLaMA-3.1-8B）、9 类方法。探索性的 entity-level construction 在低 degeneracy 条件下（Few-NERD）获得 +1.4 pp 增益，但效果不一致。degeneracy 阈值 θ_crit=0.70 预测 SC 增益何时消失。\n\n---\n\n## Strengths\n\n**S1. 统计实践堪称模范。** [共识] 全面使用 bootstrap 95% CI、permutation test、TOST 等价检验、Holm-Bonferroni 多重比较校正（Table 12, k=57）、post-hoc power analysis。Table 12 的 57 项检验透明报告了全局校正下核心 claim 不达显著（p_HB=0.055），这种统计诚实在 NLP 论文中罕见。\n\n**S2. 实验覆盖和附录深度。** [共识] 4 个 NER 数据集 × 2 模型族 × 9 方法类别 × 16+ 配置，39 页 Appendix 覆盖几乎所有可能的消融角度（温度、sample size、free-form decoding、cross-family、14B scale、epoch confound 等），几乎穷尽了 reviewer 可能提出的消融需求。\n\n**S3. Correlation-selection gap 是有价值的诊断概念。** [共识] 将 quality estimation 与 selection 之间的脱节命名并系统量化，Figure 2 有效可视化了这一 gap。四阶段 cascade 的诊断逻辑清晰，每个阶段有可计算指标。\n\n**S4. 清晰的 observational 定位和实用的负面结论。** [共识] Section 2 开头声明不做因果声明；Section 9 的 diagnostic cascade 提供了可操作的预部署决策树。\n\n**S5. MBR 形式化连接。** Proposition 2 建立了 entity-level construction 与 balanced set-overlap utility 下 MBR 最优性的理论桥梁。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**C1. 全局 Holm-Bonferroni (k=57) 下核心 NER claim 不显著，主文未充分讨论。** [R1 提出, R2 AGREE]\nTable 12 显示全局校正下 p_HB=0.055，\"no core NER claim survives\"。正文使用 family-wise corrected p-values（较小的 k=10, 21, 9），但未在正文中明确告知读者全局校正结果——Appendix e 第 18 页报告了此事实，但作为影响核心结论可信度的关键信息，应在 Discussion 或 Limitations 中显著讨论。此外应为 family-wise 分组提供先验理由（基于研究问题独立性），并报告 BH FDR 作为补充。\n\n**C2. 模型覆盖面不足以支撑跨规模/跨家族泛化声明。** [R1 提出, R2 AGREE]\n主实验仅依赖 2 个 8B fine-tuned 模型（Qwen3-8B, LLaMA-3.1-8B）。GPT-5.5 仅 200 instances zero-shot；14B 仅 SciERC；72B 仅 zero-shot AWQ。Abstract/Introduction 声称 \"treating NER as a representative instance of set-valued generation\"、\"the gap persists across scales and families\"，但实际模型规模基本锁定在 7-8B，且 zero-shot vs fine-tuned 对比不对等。应限定 claim 范围为 \"7-14B fine-tuned + selected zero-shot frontier models\"。\n\n**C3. Prescriptive 阶段薄弱，三阶段叙事不完整。** [双方 AGREE]\nIntroduction 承诺 \"Discover → Diagnose → Prescribe\" 叙事，但 Prescribe 阶段核心产物——entity-level construction——效果不一致（Few-NERD +1.4pp, CoNLL 负面, SciERC +0.2pp non-significant）。Abstract/Discussion 以 prescriptive 口吻呈现，Section 7.5 标记 \"exploratory\"——叙事矛盾。Discussion 结论本质是 \"what NOT to do\" 而非 \"what to do\"。应统一定位为 \"exploratory with promising but inconsistent initial results\"。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1. \"Diagnostic Framework\" 定位与实际贡献之间存在张力。** [R2 Must-Fix, R1 REBUT — 分歧未解决]\nR2 认为 \"framework\" 需要跨任务通用性和预测能力，实际是 empirical study，建议改标题。R1 反驳称 Appendix ac 的 3-step protocol 使其超越典型 empirical study，\"diagnostic framework\" 基本成立。Director 判断：论文的 framework 定位有一定基础（诊断 protocol 可操作），但正文叙事偶尔超出诊断范畴，应更审慎。\n\n**W2. 相对于 Yao et al. (2026)、Chen et al. (2024)、Xie et al. (2023)、Yun et al. (2025) 的增量贡献界定不清。** [R2 Must-Fix, R1 REBUT — 分歧未解决]\nR2 认为增量不够清晰。R1 提供了详细对比表（instance-level vs task-level, quantitative cascade vs qualitative failure modes, LP-weighted vs majority voting, agreement-quality alignment vs diversity）认为增量显著。Director 判断：增量存在但论文 Section 8 表述分散，缺少集中的 \"What's new\" 段落。\n\n**W3. Free-form decoding 消融仅覆盖 SciERC，CoNLL/WNUT-17 缺失。** [R1 提出, R2 AGREE]\nConstrained decoding 可能是 CoNLL 89% degeneracy 的重要驱动因素。如果 CoNLL free-form decoding 的 degeneracy 大幅下降，cascade 对 CoNLL 的诊断结论需修正为 \"constrained decoding is the bottleneck\" 而非 \"SC intrinsically fails\"。\n\n**W4. 与 Yun et al. (2025) diversity collapse 关系讨论不充分。** [双方 AGREE]\nDegeneracy 与 diversity collapse 的概念关系未深入讨论。Constrained decoding 可能同时驱动 diversity collapse 和 LP compression，但论文仅用一句话区分。需在 Discussion 增加 2-3 句讨论 constrained decoding 作为 confound。\n\n**W5. θ_crit=0.70 缺少充分验证。** [R1 Must-Fix, R2 建议降级 — 分歧]\nR1 认为 16 个配置点既拟合又验证，post-hoc fitting 风险。R2 认为 θ_crit 更像描述性发现，不需要 ML 级 held-out 验证，建议降级。Director 判断：降级为 Should-Fix，但需明确定位（descriptive vs normative）并报告 sensitivity sweep 或 LOO-CV。\n\n**W6. 信息密度过高，首次阅读认知负荷极大。** [R2 提出, R1 AGREE]\n几乎每个句子 2-3 个统计量，缩写过多（LP, SJ, FK, VC, EM, MV, QE, AUROC 等）。建议主文聚焦 top-level patterns，详细数字移入 Appendix。\n\n**W7. Related Work 覆盖不足。** [双方 AGREE]\nSnell et al. (2025) \"Scaling LLM Test-Time Compute Optimally\" 与 dataset-dependent optimal strategy 直接相关但未引用。Eikema et al. (2025) structure-conditional MBR 与 Proposition 2 的连接可深化。LLM calibration 文献（Kadavath et al. 2022, Tian et al. 2023）讨论不足。\n\n**W8. RE/SQL 扩展太薄，\"structured IE\" 泛化措辞超出证据。** [双方 AGREE]\nRE 仅 SciERC（397 instances, 40% zero F1），且 cascade 行为与 NER 显著不同。SQL 仅一句话提及（87.2% degeneracy）。标题准确限定为 NER，但 Abstract/Discussion 的 \"structured IE/prediction\" 措辞超出。\n\n**W9. 2-seed vs 3-seed 不对称未说明。** [双方 AGREE]\nTable 1 中 selection signals 使用 2-seed mean，baselines 使用 3-seed，正文未解释原因。\n\n### Minor Issues\n\n- **M1**: Figure 1 \"diagnostic; not causal chain\" 注释好，但箭头视觉暗示因果链，建议用虚线。[双方 AGREE]\n- **M2**: 缩写表（Table 5, Appendix）建议以简化版放入主文。\n- **M3**: Table 2 \"Full coverage in Appendix h.4\" 引用——主文缺少 9 类方法的数据集覆盖概览。\n- **M4**: Table 65 cost-benefit analysis（p45）很有价值，建议在正文提及核心数字。\n- **M5**: 引用括号格式一致性检查（Section 1 有混用）。\n- **M6**: 匿名性无问题。Ethics Statement 和 Checklist 覆盖恰当。\n- **M7**: 正文可能略微溢出 8 页——确认 camera-ready 严格控制。\n- **M8**: Proposition 1/2 的 entity-wise independence 假设应在正文中更明确标注为 simplifying assumption。\n- **M9**: Limitations 应补充 prompt sensitivity 未测试。\n\n---\n\n## Reviewer Consensus\n\n以下问题双方达成共识 [AGREE]：\n\n1. **统计实践是核心优势**——bootstrap CI、Holm-Bonferroni、permutation test 的组合使用是标杆级别\n2. **Prescriptive 阶段薄弱**——entity-level construction 效果不一致，叙事应降级为 exploratory\n3. **模型覆盖面不足**——泛化声明应限定为 7-14B fine-tuned regime\n4. **全局统计校正透明度不足**——主文需讨论 k=57 结果\n5. **Free-form decoding 消融缺失 CoNLL**——constrained decoding 可能放大 degeneracy\n6. **Related Work 覆盖不足**——需补 Snell et al.、Eikema et al.、calibration 文献\n7. **与 Yun et al. diversity collapse 关系需深化**\n8. **2-seed/3-seed 差异需说明**\n\n---\n\n## Reviewer Divergence\n\n| 问题 | R1 立场 | R2 立场 | Director 判断 |\n|------|---------|---------|---------------|\n| Overall 评分 | 3.5 (Borderline Conference) | 3.0 (Findings) | 3.0 (Findings) |\n| Framework 定位 | 基本成立（Appendix ac 3-step protocol）| 过高（应为 empirical study）| 有基础但叙事需审慎收敛 |\n| 新颖性增量 | 显著（详细对比表）| 不够清晰 | 增量存在但论文表述分散 |\n| θ_crit 严重性 | Must-Fix（post-hoc fitting）| Should-Fix（描述性发现）| Should-Fix + 需定位澄清 |\n| CoNLL 高 degeneracy tautology | 非 tautological（cascade 排除了其他假设）| 部分 tautological | R1 论证更有说服力 |\n| Cross-dataset power | Should-Fix | 领域固有限制 | Info 级，提及即可 |\n\n---\n\n## Questions for Authors\n\n1. **CoNLL free-form decoding ablation**: 在 CoNLL 上进行 free-form decoding，degeneracy 率是否显著下降？如果下降，cascade 的 CoNLL 诊断结论是否需修正？\n2. **全局 vs family-wise Holm-Bonferroni**: 按 BH FDR 校正，多少核心 NER claims 能在 FDR<0.05 下成立？\n3. **θ_crit=0.70 LOO-CV**: 每个 fold 的 θ_crit 估计值变异范围是多少？\n4. **GPT-5.5 sampling strategy**: 200-instance 的选择策略（random? stratified?）及完整结果分解？\n5. **Degeneracy filtering + entity construction**: 仅对非 degenerate instances 做 construction，收益是否更大且更一致？\n\n---\n\n## Missing References\n\n1. **Snell et al. (2025)** \"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\" (ICLR 2025)——compute-optimal test-time scaling 策略，与 dataset-dependent optimal strategy 发现直接相关。[双方 AGREE 应引用]\n2. **Eikema et al. (2025)** structure-conditional MBR——已引用但讨论不足，与 Proposition 2 的连接应深化。[双方 AGREE]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n**状态**：pending（已于 2026-05-22T08:47 发送请求，尚未返回）。如用户收到外部审稿结果，将作为补充材料追加。\n\n---\n\n## Visual Layout Check（非评分项）\n\n**状态**：Agent 超时（300s timeout）。未产出排版检查结果。用户可选择重新触发视觉审查。\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 (Findings)**\n\n**置信度**: 4/5\n\n**评分理由**:\n\n本文在 self-consistency 对 NER 的失效机制上提供了迄今最系统、最严谨的诊断分析，统计实践堪称模范，47 页的分析深度令人印象深刻。Correlation-selection gap 是有用的概念，四阶段 cascade 的诊断逻辑清晰。\n\n评 Findings 而非 Conference 的核心原因：\n1. **统计脆弱性**：核心 NER claim 在全局 Holm-Bonferroni (k=57) 下 p_HB=0.055，未达显著——family-wise 分组虽可辩护但主文透明度不足。\n2. **Prescriptive arm 不完整**：entity-level construction 仅在 Few-NERD 有显著且一致的增益，三阶段叙事的 Prescribe 阶段无法支撑。\n3. **泛化证据有限**：模型覆盖主要锁定在 8B fine-tuned，跨规模声明缺乏 ≥30B fine-tuned 证据；RE/SQL 扩展过于初步。\n4. **定位-内容张力**：\"Diagnostic Framework\" 定位有一定基础但超出了当前验证范围（跨任务通用性不足、formal 决策边界不完整）。\n\n**提升路径**（如果 rebuttal/修改能回应以下问题，可升至 3.5 Borderline Conference）：\n- 主文透明报告全局 Holm-Bonferroni + BH FDR 结果\n- 统一 Prescriptive 叙事为 exploratory\n- 限定 claim 范围（模型规模、任务泛化）\n- Section 8 增加集中的增量贡献阐述\n- CoNLL free-form ablation 或充分讨论 constrained decoding confound\n\n---\n\n## Detailed Comments\n\n### Section 1 (Introduction)\n- \"Discover → Diagnose → Prescribe\" 三阶段叙事中 Prescribe 阶段的承诺过高。建议调整为 \"Discover → Diagnose → Explore bypasses\"。\n- 与 Yao et al. (2026)、Chen et al. (2024)、Xie et al. (2023)、Yun et al. (2025) 的差异化定位应前移到 Introduction，而非留到 Section 8。\n\n### Section 2 (Diagnostic Framework)\n- \"Capability ceiling\" 的 N≤16 定义较窄。R1 论证该概念不依赖固定 N（gap 随 N 增大而扩大），但正文定义与后续 N=32/64 实验存在张力。\n- Experimental setup 概览应在此处或之后增加 1-2 段，帮助读者在遇到 Section 3-6 的实验数据时有上下文。\n\n### Sections 3-4 (Mechanistic + Selection Gap)\n- Introspection boundary 发现（ESJ AUROC 0.51 vs hidden-state probe 0.63-0.88）有趣但机制解释较浅。\n- Table 1 的 2-seed/3-seed 差异需说明。\n- Selection alignment α→0 是核心发现但叙事上被 degeneracy 讨论淹没——建议在 Section 4 更突出 α 的 binding constraint 角色。\n\n### Section 5 (Adaptive Methods)\n- Table 2（9 method categories）信息密集但缺少主文中的数据集覆盖概览。\n- Cross-model ensemble（+0.42pp）仅在 Few-NERD 单数据集测试。\n\n### Section 6 (Theory/Scaling)\n- Proposition 1 应更明确标注为 descriptive formalization。Proposition 2 的 MBR 连接是更实质性的理论贡献。\n- Inverse scaling under adaptive thresholds 的发现（40/58 transitions 变差）重要但讨论偏技术，实践含义可更直接。\n\n### Section 7 (Experiments)\n- 实验设置在 Section 7.1 出现较晚——读者已在 Sections 3-6 消化了大量结果。\n- Few-NERD 3 epochs vs others 5 epochs 的混淆需更显著讨论（不仅在 Appendix ab）。\n\n### Section 8 (Related Work)\n- 缺少与 Snell et al. (2025) compute-optimal scaling 的对比。\n- 与 Yun et al. (2025) 的关系需从 1 句扩展到 1 段——特别是 constrained decoding 作为共同 confound。\n- 建议增加集中的 \"What's new\" 对比段落。\n\n### Section 9 (Discussion and Conclusion)\n- 结论本质是 diagnostic（\"when not to use SC\"）而非 prescriptive。建议与 Introduction 的叙事对齐。\n- Practical implications 段落有价值，可考虑增加 cost-benefit 数字（Table 65）。\n\n### Limitations\n- 覆盖较好但遗漏：(a) prompt sensitivity 未测试；(b) 仅 8B fine-tuned 主实验，larger model fine-tuned 行为未知。\n- 全局 Holm-Bonferroni 下核心 claim 脆弱性应在此处或 Discussion 讨论。\n\n### Appendix\n- 极其详尽，几乎所有主文 claim 有对应消融。Appendix ac 的 3-step evaluation protocol 有实用价值。\n- Table 65 cost-benefit analysis 建议提升到正文。",
    "reviewer_ids_acknowledged": "[\"1\", \"2\"]",
    "cross_response_reviewer_ids": "[\"1\", \"2\"]",
    "overall_score": "3.0"
  }
}
```

</details>

---


### Tool result

_source line 3689 · 2026-05-22T09:06:09.793663+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_1b56445332d8ca2b4964b30f300f0e00:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4940
}
```

</details>

---


### Tool call

_source line 3690 · 2026-05-22T09:06:19.234482+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': '收集 Reviewer 1 审稿意见', 'status': 'completed', 'activeForm': '已收到 Reviewer 1 审稿意见'}, {'content': '收集 Reviewer 2 审稿意见', 'status': 'completed', 'activeForm': '已收到 Reviewer 2 审稿意见'}, {'content': '交叉分享：将 R1 意见转发给 R2，R2 意见转发给 R1', 'status': 'completed', 'activeForm': '交叉分享已完成'}, {'content': '收敛判断：分析共识与分歧', 'status': 'completed', 'activeForm': '收敛分析已完成'}, {'content': '合成最终报告并投递', 'status': 'completed', 'activeForm': '审稿报告已投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': '收集 Reviewer 1 审稿意见', 'status': 'completed', 'activeForm': '已收到 Reviewer 1 审稿意见'}, {'content': '收集 Reviewer 2 审稿意见', 'status': 'completed', 'activeForm': '已收到 Reviewer 2 审稿意见'}, {'content': '交叉分享：将 R1 意见转发给 R2，R2 意见转发给 R1', 'status': 'completed', 'activeForm': '交叉分享已完成'}, {'content': '收敛判断：分析共识与分歧', 'status': 'completed', 'activeForm': '收敛分析已完成'}, {'content': '合成最终报告并投递', 'status': 'completed', 'activeForm': '审稿报告已投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 3691 · 2026-05-22T09:06:19.235009+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Assistant

_source line 3692 · 2026-05-22T09:06:31.022182+00:00_

Round 34 审稿完成。报告已投递给 Research Director。

**审稿结果摘要：**
- **Overall: 3.0 (Findings)**，R1 给 3.5 / R2 给 3.0，综合评定 3.0
- **3 个 Must-Fix 共识项**：(1) 全局 Holm-Bonferroni 下核心 claim 脆弱且主文透明度不足；(2) 模型覆盖面不足以支撑泛化声明；(3) Prescriptive 阶段薄弱、叙事不完整
- **9 个 Should-Fix**：framework 定位张力、增量贡献界定不清、free-form ablation 缺失 CoNLL、Yun et al. 关系讨论不充分、θ_crit 验证不足、信息密度过高、Related Work 覆盖不足、RE/SQL 扩展太薄、2-seed/3-seed 差异未说明
- **核心判断**：统计实践模范、分析深度罕见，但统计 claim 在全局校正下边缘不显著、prescriptive arm 不一致、泛化证据有限。修正定位和透明度问题后 Findings 接收前景好，回应关键问题可升至 3.5 Borderline Conference
- **外部审稿**：pending（未返回）
- **视觉审查**：Agent 超时，未产出结果
- **Issue Tracker**：已同步更新 16 个 issue（含 5 个新增）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 276

## Round 276

2 recorded events


### User

_source line 3693 · 2026-05-22T09:06:34.044057+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。总结：

- **R2 Must-Fix**: N1 (framework overstatement) [REBUT]——Appendix ac 的 3-step protocol 超越 empirical study；N2 (prescriptive 薄弱) [AGREE]——但纠正了 R2 将 LP selection 的 CoNLL −0.85pp 错误归因于 entity construction；N3 (novelty unclear) [REBUT]——增量贡献显著，但表述需改进
- **R2 Should-Fix**: W1 [REBUT], W2 [AGREE], W3 [REBUT]（N scaling 到 64）, W4 [部分AGREE], W5 [REBUT]（非 tautological，cascade 排除了替代假设）, W6 [AGREE]
- **R2 Limitations**: L1 [AGREE], L2 [REBUT]（T=0.7 已测但范围仍窄）, L3 [AGREE]
- **Overall**: 维持 R1 评分 3.5 vs R2 的 3.0。核心分歧在于 framework 定位和 novelty 评估。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 3694 · 2026-05-22T09:06:45.210739+00:00_

Round 34 审稿已完成，报告已投递至 Research Director。

**最终结果**：
- **Overall Score: 3.0 (Findings)**
- R1: 3.5 (Borderline Conference) / R2: 3.0 (Findings)
- 1 轮独立审稿 + 1 轮交叉分享，关键问题达成共识，无需更多轮次

**核心共识**（8 项）：prescriptive 阶段薄弱、模型覆盖面不足、全局统计校正透明度不够、free-form ablation 缺失 CoNLL、Related Work 覆盖不足、Yun et al. 关系需深化、2-seed/3-seed 需说明、统计实践是核心优势

**未解决分歧**（2 项）：framework 定位（R1 认为成立 vs R2 认为过高）、新颖性增量评估（R1 认为显著 vs R2 认为不清晰）

**外部审稿**：pending，未返回
**视觉审查**：Agent 超时，未产出结果

Issue Tracker 已同步更新至 `artifacts/review_issues.yaml`（16 条 issue，含 4 条新增）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 277

## Round 277

74 recorded events


### User

_source line 3695 · 2026-05-22T10:12:24.013200+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: struct_self_consist_ie
- 论文路径: projects/struct_self_consist_ie/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Main Conference (via ARR May 2026)
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 3696 · 2026-05-22T10:12:31.037409+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 3697 · 2026-05-22T10:12:31.089909+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 3286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 3698 · 2026-05-22T10:12:37.763230+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,WebSearch,WebFetch",
  "max_results": "11"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,dispatch_visual_check,request_external_review,get_external_review_status,get_visual_check_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,WebSearch,WebFetch",
    "max_results": "11"
  }
}
```

</details>

---


### Tool result

_source line 3699 · 2026-05-22T10:12:37.763560+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 3700 · 2026-05-22T10:12:41.073750+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 3701 · 2026-05-22T10:12:42.494405+00:00_

{"result":"# 项目 struct_self_consist_ie 概况\n\n## 实验状态 (319 个)\n\n- **exp_002_ner_conll2003**: DONE (success) — \n- **exp_004_re_diagnostic**: DONE (success) — \n- **exp_005**: DONE (success) — \n- **exp_014_entity_majority_voting**: DONE (success) — \n- **exp_013_exact_match_voting**: DONE (negative) — \n- **exp_012_logprob_baseline**: DONE (success) — \n- **mvp_pilot_005**: DONE (negative) — \n- **e1_component_wise_re_sj**: DONE (negative) — \n- **mvp_pilot_004**: DONE (negative) — \n- **ft_002_v2**: DONE (success) — \n- **mvp_pilot_002**: DONE (failed) — \n- **ft_002**: DONE (killed) — \n- **ft_001**: DONE (success) — \n- **mvp_pilot_003**: DONE (negative) — \n- **mvp_pilot_001**: DONE (negative) — \n\n## 最新报告\n# Handover — 2026-05-22\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\n|--------|------|------|---------|-----|\n| exp_fewnerd_pretrained_n32_s42 | Pretrained N-scaling: FewNERD N=32 with Qwen2.5-7B-Instruct (unfinetuned). FewNERD pretrained showed +3.90pp MV gain at N=8. Tests whether pretrained MV advantage scales with N and whether the pretrained-vs-finetuned direction flip persists at 4× budget. Complements CoNLL/SciERC pretrained N=32 for cross-dataset generalization evidence. | — | — | — |\n| exp_fewnerd_n32_s42 | N-scaling convergence test: at N=32 (4× current N=8), MV strict Δ remains negative on FewNERD finetuned model, demonstrating that the selection gap does not close at practical sample budgets. If MV Δ converges toward 0 slowly, this quantifies the impractical N required. Motivated by R34 C1 and Reviewer #107 P2. | — | — | — |\n\n## 待处理\n- exp_fewnerd_mf4_s42: MF4 pipeline fix: FewNERD N=8 T=1.0 seed=42 using run_mvp_pilot.py (greedy_f1/micro-F1). Replaces exp_021 which used incompatible greedy_macro_f1 metric. Required for 3-seed statistical power with unified pipeline.（已分配 autodl-5090-c GPU:cuda:0，等待提交）\n- exp_fewnerd_mf4_s123: MF4 pipeline fix: FewNERD N=8 T=1.0 seed=123 using run_mvp_pilot.py (greedy_f1/
…[truncated 1742 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1420
}
```

</details>

---


### Tool call

_source line 3702 · 2026-05-22T10:12:42.494895+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 3703 · 2026-05-22T10:12:42.900360+00:00_

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
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{amsthm}
16	\newtheorem{proposition}{Proposition}
17	\newtheorem{theorem}{Theorem}
18	\newtheorem{corollary}{Corollary}
19	\newtheorem{definition}{Definition}
20	\usepackage{multirow}
21	\usepackage{xcolor}
22	\usepackage{subcaption}
23	\usepackage{alphalph}
24	\usepackage{enumitem}
25	
26	\graphicspath{{figures/}}
27	
28	\title{When Does Test-Time Scaling Fail?\\ Boundary Conditions for Structured Prediction}
29	
30	\author{Anonymous}
31	
32	\begin{document}
33	\maketitle
34	
35	\input{sections/abstract}
36	\input{sections/introduction}
37	\input{sections/diagnostic}
38	\input{sections/mechanistic}
39	\input{sections/single_signal}
40	\input{sections/adaptive}
41	\input{sections/theory}
42	\input{sections/experiments_main}
43	\input{sections/background}
44	\input{sections/discussion}
45	
46	\section*{Limitations}
47	\input{sections/limitations}
48	
49	\section*{Ethics Statement}
50	All experiments use publicly available benchmarks (SciERC, CoNLL-2003, Few-NERD, WNUT-17), open-weight models (Qwen3-8B, Qwen3-14B, Qwen3-4B, LLaMA-3.1-8B), and the GPT-5.5 API.
51	CoNLL-2003 is derived from the Reuters RCV1 corpus, which is available for research purposes under a NIST agreement; we use the standard research distribution.
52	No new human data was collected or annotated for this study.
53	Our findings on signal limitations could inform more reliable deployment of IE systems by guiding practitioners toward appropriate confidence signals for their use case.
54	Code and data will be released upon acceptance at [anonymized URL].
55	
56	\section*{Responsible NLP Research Checklist}
57	\input{sections/checklist}
58	
59	\bibliography{references}
60	
61	
…[truncated 122 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 405
}
```

</details>

---


### Tool call

_source line 3704 · 2026-05-22T10:12:42.951027+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 ARR May 2026 call for papers submission guidelines author instructions site:aclweb.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 ARR May 2026 call for papers submission guidelines author instructions site:aclweb.org"
  }
}
```

</details>

---


### Tool result

_source line 3705 · 2026-05-22T10:12:57.116799+00:00_

Web search results for query: "EMNLP 2026 ARR May 2026 call for papers submission guidelines author instructions site:aclweb.org"

Links: [{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"5th Workshop on Evaluation and Comparison for NLP systems (Eval4NLP) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/5th-workshop-evaluation-and-comparison-nlp-systems-eval4nlp"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"}]

I found several relevant results, but I notice that the search results mostly con
…[truncated 5825 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 14165
}
```

</details>

---


### Tool call

_source line 3706 · 2026-05-22T10:13:05.756025+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://2026.emnlp.org/calls/main_conference_papers/",
  "prompt": "Extract the complete submission guidelines for EMNLP 2026 main conference papers: page limits for long and short papers, formatting template requirements, anonymity/double-blind rules, appendix rules, supplementary material rules, citation format, and any other submission requirements. Be thorough and include all details."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://2026.emnlp.org/calls/main_conference_papers/",
    "prompt": "Extract the complete submission guidelines for EMNLP 2026 main conference papers: page limits for long and short papers, formatting template requirements, anonymity/double-blind rules, appendix rules, supplementary material rules, citation format, and any other submission requirements. Be thorough and include all details."
  }
}
```

</details>

---


### Tool call

_source line 3707 · 2026-05-22T10:13:06.007299+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "file": "config.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "file": "config.yaml"
  }
}
```

</details>

---


### Tool result

_source line 3708 · 2026-05-22T10:13:11.324621+00:00_

# EMNLP 2026 Main Conference Paper Submission Guidelines

## Page Limits

**Long Papers:** "8 pages" with one additional page permitted in final versions to address reviewer feedback, for a total of 9 pages.

**Short Papers:** "4 pages" with one additional page in final versions, totaling 5 pages maximum.

## Anonymity and Review Process

The review system operates as double-blind: "Reviewers will not see authors, nor will authors see reviewers and reviews on ARR will not be made publicly visible." Authors receive the option to make their anonymized submissions publicly visible through ARR.

Following ACL and ARR policies, "there is no anonymity period requirement."

## Formatting and Templates

Submissions must adhere to "ARR submission requirements," which include specific formatting standards and templates. The page references directing authors to comply with all ARR guidelines indicate detailed formatting specifications exist in that system, though specific template details aren't elaborated in this document.

## Required Submission Elements

All papers must include:
- A limitations section
- Ethical considerations per the "responsible NLP research checklist"
- Two-way anonymized review compliance
- Proper citation and comparison standards

## Supplementary Materials

Papers may include "optional supplementary materials, appendices, software and data" beyond the page limits, allowing authors to provide additional resources supporting their work.

## Additional Requirements

- Writing assistance is permitted
- Dual submissions are prohibited
- Author lists cannot be modified during the commitment phase

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebFetch",
  "elapsed_ms": 5568
}
```

</details>

---


### Tool result

_source line 3709 · 2026-05-22T10:13:11.375318+00:00_

Error executing tool read_project_file: 1 validation error for read_project_fileArguments
project
  Field required [type=missing, input_value={'file': 'config.yaml'}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.12/v/missing

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 5368
}
```

</details>

---


### Tool call

_source line 3710 · 2026-05-22T10:13:14.688416+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "config.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "file": "config.yaml"
  }
}
```

</details>

---


### Tool result

_source line 3711 · 2026-05-22T10:13:14.738975+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'config.yaml'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 3712 · 2026-05-22T10:13:19.658583+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/struct_self_consist_ie/**/config*.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/struct_self_consist_ie/**/config*.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1"
  }
}
```

</details>

---


### Tool result

_source line 3713 · 2026-05-22T10:13:19.759408+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 3714 · 2026-05-22T10:13:22.870259+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/struct_self_consist_ie/config.*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/struct_self_consist_ie/config.*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1"
  }
}
```

</details>

---


### Tool result

_source line 3715 · 2026-05-22T10:13:23.372410+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 3716 · 2026-05-22T10:13:23.473212+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/struct_self_consist_ie/agent/config*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/struct_self_consist_ie/agent/config*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1"
  }
}
```

</details>

---


### Tool result

_source line 3717 · 2026-05-22T10:13:23.575412+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 3718 · 2026-05-22T10:13:26.887334+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie -name \"*.yaml\" -o -name \"*.yml\" | head -20",
  "description": "Find YAML config files in project directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie -name \"*.yaml\" -o -name \"*.yml\" | head -20",
    "description": "Find YAML config files in project directory"
  }
}
```

</details>

---


### Tool result

_source line 3719 · 2026-05-22T10:13:27.138561+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/dream_registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/writing_plan.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper_provenance.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/literature_map.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/registry.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/constraints.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/mistakes.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T092241/median/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T092241/median/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T092241/worst/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T092241/worst/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T092241/meta.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T092241/best/review_context.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T092241/best/imagined_experiments.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260516T225436/meta.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_202
…[truncated 644 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 3720 · 2026-05-22T10:13:30.373283+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "external_review|paperreview",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1",
  "glob": "*.yaml",
  "output_mode": "content",
  "head_limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Grep",
  "tool_args": {
    "pattern": "external_review|paperreview",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1",
    "glob": "*.yaml",
    "output_mode": "content",
    "head_limit": "20"
  }
}
```

</details>

---


### Tool result

_source line 3721 · 2026-05-22T10:13:30.524505+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Grep",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 3722 · 2026-05-22T10:13:36.780678+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 3723 · 2026-05-22T10:13:36.781002+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 3724 · 2026-05-22T10:13:39.591847+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper -name \"*.tex\" | sort",
  "description": "List all tex files in paper directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper -name \"*.tex\" | sort",
    "description": "List all tex files in paper directory"
  }
}
```

</details>

---


### Tool result

_source line 3725 · 2026-05-22T10:13:39.692724+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/_archived/experiments_OLD.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/adaptive.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/background.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/checklist.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/diagnostic.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments_main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/mechanistic.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/single_signal.tex
/home/ubuntu/.agent-ml-research-idea_gen_
…[truncated 185 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 3726 · 2026-05-22T10:13:42.603296+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 3727 · 2026-05-22T10:13:43.055508+00:00_

1	\begin{abstract}
2	Test-time compute scaling---repeated sampling with self-consistency or best-of-$N$---yields large gains on discrete-answer reasoning, but the boundary conditions governing its effectiveness for structured prediction remain uncharacterized.
3	Using named entity recognition (four datasets, primarily 7--14B fine-tuned; tentative cross-scale observations to 72B) and relation extraction as case studies, we characterize when test-time scaling succeeds and fails for set-valued outputs.
4	Quality estimation signals effectively predict output quality (AUROC up to $0.82$ across nine method categories), yet instance-level selection yields ${<}1$\,pp even at $N{=}64$, revealing a \textbf{correlation-selection gap}.
5	A diagnostic cascade identifies two boundary conditions: output convergence (degeneracy $12$--$68$\%) and signal alignment collapse ($\alpha{\to}0$), which jointly determine scaling returns.
6	Cross-task validation on RE reveals a distinct bottleneck---$40$\% zero-F1 from upstream errors rather than degeneracy---confirming task-specific failure modes within structured prediction.
7	Exploratory entity-level construction partially bypasses the sample-level bottleneck ($+1.40$\,pp where low degeneracy and signal alignment provide headroom).
8	The central finding is a \textit{capability-diversity tension}: as model capability increases, output convergence rises and test-time scaling returns diminish---a structural constraint for structured prediction.
9	\end{abstract}
10	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 3728 · 2026-05-22T10:13:43.055971+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 3729 · 2026-05-22T10:13:43.560866+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Test-time compute scaling---self-consistency \cite{wang2023selfconsistency}, best-of-$N$ \cite{snell2025scaling, brown2024monkeys}, extended reasoning \cite{muennighoff2025s1}---yields large gains on discrete-answer tasks where outputs admit equivalence classes or execution-based verification.
4	For structured prediction, where outputs are entity sets with partial overlap, the boundary conditions for effective scaling are unknown; prior work \cite{yao2026consistency, yun2025price} provides initial observations but no systematic characterization of instance-level failure.
5	
6	Using NER (four datasets, primarily 7--14B fine-tuned; tentative cross-scale observations to 72B) and RE as case studies, we identify a \textbf{correlation-selection gap}: quality estimation signals effectively predict output quality ($\rho$ up to $0.45$, AUROC $0.82$; Table~\ref{tab:quality_estimation}), yet instance-level selection generally fails to outperform greedy decoding, with MV gains ${<}1$\,pp even at $N{=}64$ (Figure~\ref{fig:n_scaling}; Table~\ref{tab:selection}).
7	A hidden-state probe confirms models encode entity quality internally (AUROC $0.63$\textendash$0.88$; \S\ref{sec:mechanistic}), exposing an \textit{introspection boundary} \cite{huang2024large}: the information exists but cannot be leveraged for selection.
8	A diagnostic cascade localizes the failure to two boundary conditions---output convergence (degeneracy $12$--$68$\%) and signal alignment collapse ($\alpha{\to}0$)---which jointly prevent selection; nine method categories fail across three datasets and two model families (Table~\ref{tab:method_summary}).
9	The optimal strategy is dataset-dependent (LP: $+1.39$\,pp on Few-NERD; MV: $+0.61$\,pp on CoNLL at $N{=}64$), and RE reveals a distinct bottleneck ($40$\% zero-F1 from upstream errors; Appendix~\ref{app:re_extension}).
10	Exploratory entity-level construction partially bypasses the bottleneck ($+0.32$\textenda
…[truncated 2732 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 504
}
```

</details>

---


### Tool call

_source line 3730 · 2026-05-22T10:13:43.561340+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/diagnostic.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/diagnostic.tex"
  }
}
```

</details>

---


### Tool result

_source line 3731 · 2026-05-22T10:13:44.064487+00:00_

1	\section{Diagnostic Framework}\label{sec:method}
2	
3	Our analysis is observational: we characterize statistical associations between agreement signals and output quality without claiming causal mechanisms.
4	
5	\subsection{Problem Formulation}\label{sec:formulation}
6	
7	Given model $\mathcal{M}$ and input $x$, we sample $N$ outputs $\{y_1, \ldots, y_N\}$ at temperature $T > 0$ via constrained decoding \cite{willard2023guided}, where each $y_i$ is an entity set.
8	A \textbf{per-sample signal} $c_{\text{ps}}: (x, y_i) \to \mathbb{R}$ scores each output independently; an \textbf{instance-level signal} $c_{\text{il}}: (x, \{y_i\}_{i=1}^N) \to \mathbb{R}$ produces a single score per input (notation in Appendix~\ref{app:notation}).
9	This distinction is consequential: 4 of 5 signals are instance-level aggregates assigning identical scores to all $N$ candidates.
10	Only LP carries per-sample discriminative power: ensemble optimization assigns LP mean weight $0.78$, with structural signals receiving zero weight (Appendix~\ref{app:supervised_combination}).
11	When LP fails---as in few-shot regimes where LP $\rho{\to}0$ (\S\ref{sec:scaling})---no alternative per-sample signal exists.
12	
13	We define the \textbf{capability ceiling} as the practical performance upper bound achievable through self-consistency at realistic sample budgets ($N{\leq}16$), beyond which diminishing returns render further scaling impractical.
14	
15	\subsection{Confidence Signals}\label{sec:signals}
16	
17	Entity matching uses exact span and type match.
18	We distinguish two signal families: four \textit{agreement signals} computed across samples---\textit{structural} (Soft Jaccard [SJ], entity voting confidence [VC]) and \textit{surface} (exact match [EM], Fleiss' $\kappa$ [FK])---and log-probability [LP] as the sole \textit{model-internal} signal, derived from generation probabilities and providing per-sample discrimination.
19	
20	\paragraph{Log-probability (per-sample).}
21	$c_{\text{lp}}(y_i)
…[truncated 2151 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 3732 · 2026-05-22T10:13:44.064948+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/mechanistic.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/mechanistic.tex"
  }
}
```

</details>

---


### Tool result

_source line 3733 · 2026-05-22T10:13:45.018102+00:00_

1	\section{How Self-Verification Fails}\label{sec:mechanistic}
2	
3	The diagnostic cascade (\S\ref{sec:method}) identifies \textit{where} self-consistency fails; this section probes \textit{why} by testing whether models can self-verify at the entity level.
4	We evaluate self-verification and diagnostic probes on Qwen2.5-7B (a separate model family from the primary Qwen3-8B) fine-tuned for NER on Few-NERD ($N{=}8$, seed 42; full results in Appendix~\ref{app:self_verification}).
5	
6	\paragraph{Entity Self-Judgment (ESJ).}
7	For each extracted entity, we prompt the generating model: ``Is [\textit{entity}] a [\textit{type}] entity in this sentence?''
8	Entity-level AUROC is $0.512$---indistinguishable from chance---with P(yes$|$correct)${=}0.500$ and P(yes$|$incorrect)${=}0.500$.
9	ESJ-weighted construction degrades F1 to $0.711$ (vs.\ greedy $0.794$).
10	
11	\paragraph{Multi-Round Self-Consistency (MRSC).}
12	Following iterative self-refinement \cite{madaan2023selfrefine}, we re-prompt on disputed entities (agreement ${<}0.6$) with focused verification; P(yes) separation between gold and non-gold entities is $0.0006$ ($0.5003$ vs.\ $0.4997$).
13	MRSC best F1 ($0.763$) falls below greedy.
14	
15	\paragraph{Latent Self-Consistency (LSC).}
16	Mean-pooled final-layer hidden states ($d{=}3584$) provide per-sample latent representations.
17	Centroid selection ($0.759$) underperforms greedy ($0.794$); latent entity confidence ($0.839$) outperforms majority vote ($0.792$) but does not close the oracle gap ($0.882$).
18	
19	\paragraph{Hidden-state probe.}
20	A logistic regression on mean-pooled final-layer hidden states at entity spans achieves AUROC $0.636$ (Few-NERD), $0.882$ (CoNLL), $0.630$ (SciERC), evaluated with GroupKFold CV (5-fold ${\times}$ 3 seeds, groups${=}$source instance to prevent entity-level leakage; Appendix~\ref{app:hidden_probe}).
21	All three exceed ESJ ($0.51$); only CoNLL approaches frequency agreement ($0.868$).
22	Cross-dataset transfer is weak: lea
…[truncated 1062 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 3734 · 2026-05-22T10:13:45.018603+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/single_signal.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/single_signal.tex"
  }
}
```

</details>

---


### Tool result

_source line 3735 · 2026-05-22T10:13:45.470395+00:00_

1	\section{Where Single-Signal Selection Fails}\label{sec:selection_gap}
2	
3	\paragraph{Definitional vs.\ empirical.}
4	We decompose the correlation-selection gap into two layers.
5	The first is structural: four of five signals are instance-level aggregates that assign identical scores to all $N$ candidates from a given input (\S\ref{sec:formulation}), so they estimate quality across inputs but cannot rank candidates within an instance---selection failure is a design property, not an empirical finding.
6	The second layer is empirical and constitutes the core diagnostic: LP---the only per-sample signal---suffers compression under constrained decoding, with 60\% of SciERC instances showing within-instance LP range below 0.041 nats (Appendix~\ref{app:logprob_ties}), effectively eliminating the variation needed for sample discrimination. Even where LP varies, selection gains depend on LP-quality alignment rather than degeneracy alone.
7	Cross-instance $\rho$ (Table~\ref{tab:quality_estimation}) is attenuated by varying instance difficulty; within-instance $\rho$ directly measures whether LP discriminates candidates for a fixed input, making it the relevant predictor of selection success.
8	
9	\begin{table}[t]
10	\centering
11	\small
12	\caption{Best-of-$N$ selection (macro F1) on SciERC ($N{=}8$, $T{=}1.0$). Selection signals: 2-seed mean${\pm}\sigma$; baselines: 3-seed (Oracle${=}0.781$, Greedy${=}0.667$). LP is per-sample; others use consensus-proximity. $^\dagger$One score per input.}
13	\label{tab:selection}
14	\begin{tabular}{lcc}
15	\toprule
16	Method & NER F1 & $p$ \\
17	\midrule
18	Oracle & $0.775 \pm 0.001$ & --- \\
19	Greedy ($T{=}0$) & $0.645 \pm 0.001$ & --- \\
20	\midrule
21	LP           & $\mathbf{0.647} \pm 0.005$ & .29 \\
22	SJ           & $0.646 \pm 0.002$ & .67 \\
23	FK           & $0.646 \pm 0.001$ & .79 \\
24	EM           & $0.637 \pm 0.001$ & n/a$^\dagger$ \\
25	VC           & $0.623 \pm 0.004$ & n/a$^\dagger$ \\
26	\midrule
27	Random       & $0.61
…[truncated 2668 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 3736 · 2026-05-22T10:13:45.521041+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/adaptive.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/adaptive.tex"
  }
}
```

</details>

---


### Tool result

_source line 3737 · 2026-05-22T10:13:45.973033+00:00_

1	\section{Adaptive Methods}\label{sec:adaptive}
2	
3	Since instance-level selection fails (\S\ref{sec:selection_gap}), we present approaches that extract value from multi-sample generation beyond single-signal sample ranking.
4	Table~\ref{tab:method_summary} summarizes all 9 method categories evaluated; only cross-model ensembles yield an unconditional positive result.
5	
6	\begin{table}[t]
7	\centering
8	\small
9	\caption{Summary of 9 method categories tested (including MV baseline, LP selection, and cross-model ensemble beyond the seven verification methods in \S\ref{sec:mechanistic}--\S\ref{sec:adaptive}). $\Delta$F1 vs.\ greedy; dataset in parentheses. Full coverage in Appendix~\ref{app:method_coverage}.}
10	\label{tab:method_summary}
11	\resizebox{\columnwidth}{!}{%
12	\begin{tabular}{@{}llrl@{}}
13	\toprule
14	Category & Method & $\Delta$F1 / metric & § \\
15	\midrule
16	Freq.\ voting & MV & baseline & \ref{sec:prescriptive} \\
17	LP selection & Best-of-$N$ (LP) & $+1.39$\,pp (FN)$^\dagger$ & \ref{sec:selection_gap} \\
18	Self-verif.\ (prompt) & ESJ & AUROC $0.51$ & \ref{sec:mechanistic} \\
19	Multi-round refine. & MRSC & $-3.1$\,pp (FN) & \ref{sec:mechanistic} \\
20	Latent aggregation & LSC & $-3.5$\,pp (FN) & \ref{sec:mechanistic} \\
21	Adaptive gating & DALS & $+0.71$\,pp (SciERC)$^\ddagger$ & App.~\ref{app:dals} \\
22	Supervised verifier & LGB & $+0.30$\,pp (OOF) & \ref{sec:verifier} \\
23	Sup.\ combination & LR/MLP/RF & $-0.4$ to $-3.1$\,pp & App.~\ref{app:supervised_combination} \\
24	Cross-model & Qwen$+$LLaMA & $\mathbf{+0.42}$\,pp (FN) & \ref{sec:cross_model} \\
25	\bottomrule
26	\end{tabular}}
27	{\footnotesize $^\dagger$Few-NERD only; SciERC $+0.2$\,pp ($p{=}0.29$). $^\ddagger$Seed-sensitive ($\sigma{=}0.48$\,pp).}
28	\end{table}
29	
30	\subsection{Cross-Model Self-Consistency}\label{sec:cross_model}
31	
32	Mixing samples from architecturally distinct models can partially bypass within-model degeneracy.
33	Combining 4 samples each from Qwen3-8B and
…[truncated 764 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 3738 · 2026-05-22T10:13:45.973526+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/theory.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/theory.tex"
  }
}
```

</details>

---


### Tool result

_source line 3739 · 2026-05-22T10:13:46.476426+00:00_

1	\section{Threshold Regime Analysis}\label{sec:theory_scaling}
2	
3	\subsection{Entity Construction as MBR Decoding}\label{sec:mbr_theory}
4	
5	Entity-level construction selects $\hat{y}_{\textup{MBR}} = \{e \in E_\cup : \hat{p}(e) > \alpha/(\alpha{+}1)\}$ under balanced set-overlap utility; $\alpha{=}1$ recovers majority vote (Proposition~\ref{prop:construction_mbr}; Table~\ref{tab:entity_construction}; Appendix~\ref{app:mbr_proof}).
6	Signal-derived weights $w_i$ yield quality-weighted MBR: $\hat{p}_w(e) = \sum_{i} w_i \, \mathbf{1}[e {\in} y_i] / \sum_{i} w_i$; weighting improves when $w_i$ correlates with instance quality but degrades otherwise (LP on SciERC: $\rho{\approx}0.2$; \S\ref{sec:prescriptive}).
7	We select $\varepsilon{=}0.05$ at the elbow of the compression curve, where LP-best selection advantage transitions from $+1.5$\,pp (compressed) to $+4.6$\,pp (non-compressed; Appendix~\ref{app:fewnerd_epsilon}).
8	
9	\subsection{Scaling and Inverse Scaling}\label{sec:scaling}
10	
11	Oracle F1 follows $F_1(N) = a - b \cdot N^{-c}$ ($R^2 > 0.999$; Figure~\ref{fig:oracle_scaling}): Few-NERD ($c{\approx}0.61$) scales comparably to reasoning tasks \cite{brown2024monkeys}, SciERC converges more slowly ($c{\approx}0.35$), yet confidence-based aggregation recovers ${<}1$\,pp---a persistent gap.
12	The gap persists across scales and families: scaling from 8B to 14B FT increases oracle headroom ($+1.2$\,pp) with minimal greedy gain ($+0.9$\,pp), and GPT-5.5 (200 Few-NERD instances, zero-shot) exhibits the same pattern---50\% degeneracy, SJ $\rho{=}0.346$, MV $+1.4$\,pp yet 6.8\,pp oracle headroom unrealized.\footnote{Of the 10.1\% of GPT-5.5 samples producing empty entity sets, 88\% correspond to gold-empty instances; true parse failures affect only 1.2\% of samples (19/1{,}600) and shift all reported metrics by ${<}0.5$\,pp. See Appendix~\ref{app:frontier_sc}.}
13	Degeneracy is model-family-dependent rather than scale-dependent (Qwen2.5: $31.7$--$46.2$\% vs.\ Qwen3:
…[truncated 3578 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 3740 · 2026-05-22T10:13:46.476888+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments_main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments_main.tex"
  }
}
```

</details>

---


### Tool result

_source line 3741 · 2026-05-22T10:13:46.578614+00:00_

1	\section{Experiments}\label{sec:experiments}
2	
3	\subsection{Experimental Setup}\label{sec:setup}
4	
5	\paragraph{Datasets.}
6	We evaluate on four English NER benchmarks spanning a difficulty gradient.
7	\textbf{SciERC} \cite{luan2018scierc} (551 test instances, 6 entity types) is the primary medium-difficulty test bed (${\approx}$65\% F1).
8	\textbf{Few-NERD} \cite{ding2021fewnerd} (INTRA coarse; 37{,}648 instances, 8 entity types, ${\approx}$75\% F1) provides a low-degeneracy contrast where LP selection succeeds (\S\ref{sec:selection_gap}).
9	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} (3{,}453 test sentences, 4 entity types, ${\approx}$91\% F1) serves as a ceiling-effect control.
10	\textbf{WNUT-17} \cite{derczynski2017wnut} (1{,}287 social media instances, 51\% zero F1) probes the signal-collapse boundary.
11	
12	\paragraph{Models and sampling.}
13	\textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are LoRA fine-tuned using LLaMA Factory \cite{zheng2024llamafactory} (Appendix~\ref{app:training}; Few-NERD uses 3 epochs vs.\ 5 for others; Appendix~\ref{app:epoch_confound}).
14	$N{=}8$ samples at $T{=}1.0$ (primary) with vLLM constrained decoding \cite{willard2023guided}; $N {\in} \{16, 32, 64\}$ for scaling (Figure~\ref{fig:n_scaling}; Appendix~\ref{app:n_scaling}).
15	
16	\begin{figure}[t]
17	\centering
18	\includegraphics[width=\columnwidth]{figures/fig_n_scaling_mv.pdf}
19	\caption{MV $\Delta$F1 vs.\ $\log_2 N$ across three datasets (Qwen3-8B FT, seed${=}42$). Dotted gray: $\Delta{=}0$. Gains are dataset-dependent: persistently negative on Few-NERD, near zero on SciERC at higher $N$, marginally positive on CoNLL ($+0.6$\,pp at $N{=}64$).}
20	\label{fig:n_scaling}
21	\end{figure}
22	
23	%% ============================================================
24	\subsection{Quality Estimation Results}\label{sec:qe_results}
25	
26	\begin{table*}[t]
27	\centering
28	\small
29	\caption{NER quality estimation ($\rho$ and AUROC; $N{=}8$, primary seed${=}42$; 3-seed $
…[truncated 7619 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 3742 · 2026-05-22T10:13:52.600934+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/background.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/background.tex"
  }
}
```

</details>

---


### Tool result

_source line 3743 · 2026-05-22T10:13:53.655523+00:00_

1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Test-time compute scaling.}
4	Self-consistency \cite{wang2023selfconsistency} and best-of-$N$ \cite{snell2025scaling, brown2024monkeys} drive large gains on reasoning and code \cite{chen2021codex}.
5	Reward-free selectors \cite{taubenfeld2025cisc, kang2025selfcertainty}, BoN scaling laws \cite{gao2023scaling}, adaptive allocation \cite{aggarwal2023adaptive}, and trained verifiers \cite{cobbe2021verifiers, lightman2024verify} all target discrete-answer settings; structured prediction requires different aggregation because degeneracy operates at the entity-set level.
6	
7	\paragraph{SC failure modes and fine-grained variants.}
8	\citet{chen2023twofailures} identify SC failures where consistent outputs are systematically wrong; \citet{huang2024large} show LLMs cannot self-correct reasoning without external feedback.
9	\citet{chen2024usc} extend SC to free-form tasks and \citet{thirukovalluru2024atomic} decompose claims atomically; both face limits under constrained decoding where sub-output agreement does not translate to selection gain (\S\ref{sec:selection_gap}).
10	
11	\paragraph{Consistency for structured IE.}
12	\citet{yao2026consistency} show task-level QE correlation ($\rho$ up to 0.47) for NER/RE; \citet{xie2023zeroshot} propose entity voting for zero-shot NER and \citet{xie2024selfimproving} report positive SC where zero-shot diversity is high.
13	\paragraph{Uncertainty estimation and MBR.}
14	Our selection instantiates MBR decoding \cite{eikema2022sampling, denero2009fast}; despite MBR's success in translation \cite{freitag2022high, muller2021understanding} and code generation \cite{jinnai2024mbr}, all variants fail to improve over greedy due to instance degeneracy (Appendix~\ref{app:mbr_connection}).
15	\citet{eikema2025structured} find MBR utilities degrade on structured outputs; our cascade localizes this to entity-set degeneracy and LP compression (\S\ref{sec:selection_gap}).
16	LLM confidence ca
…[truncated 958 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 1054
}
```

</details>

---


### Tool call

_source line 3744 · 2026-05-22T10:13:53.655901+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 3745 · 2026-05-22T10:13:54.158167+00:00_

1	\section{Discussion and Conclusion}\label{sec:discussion}\label{sec:selection_method}\label{sec:conclusion}
2	
3	\paragraph{Why test-time scaling fails for structured outputs.}
4	For discrete-answer reasoning, sample diversity reflects diverse reasoning paths; for structured outputs, output convergence (degeneracy $12$--$68$\%) eliminates candidate diversity while signal alignment collapse ($\alpha{\to}0$) prevents ranking---a \textit{capability-diversity tension} that persists across model families (5.5--74\%; Table~\ref{tab:frontier_sc_cross}) and scales (4B--72B; \S\ref{sec:scaling}).
5	On CoNLL, pretrained MV captures ${\sim}98$\% of oracle headroom versus ${<}2$\% finetuned (Appendix~\ref{app:cross_scale}), directly demonstrating capability-induced convergence.
6	A free-form decoding ablation confirms this is not a constrained decoding artifact: CoNLL free-form degeneracy is $59.3$\% versus $56.7$\% constrained ($\Delta{=}2.6$\,pp); SciERC score compression persists (output-std ratio $0.97{\times}$; Appendix~\ref{app:freeform_ablation}), indicating degeneracy is model-intrinsic rather than grammar-induced.
7	
8	\paragraph{Practical implications.}
9	The cascade provides a pre-deployment diagnostic: measure degeneracy and LP-F1 alignment with $N{=}8$ samples before investing in $N{\times}$ inference.
10	When degeneracy exceeds $\theta_{\text{crit}}{=}0.70$, aggregation is unlikely to help; when both conditions are favorable ($D{<}22\%$, LP $\rho{>}0.2$), exploratory entity-level construction offers modest gains.
11	These findings are primarily validated on 7--14B fine-tuned NER models; generalization to other structured tasks requires further investigation.
12	
13	\paragraph{Conclusion.}
14	We characterize when test-time compute scaling fails for structured prediction, using NER and RE as case studies.
15	The correlation-selection gap is governed by output convergence and signal alignment collapse, not signal quality per se; our contribution is empirical charac
…[truncated 189 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 3746 · 2026-05-22T10:13:54.158551+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 3747 · 2026-05-22T10:13:54.359661+00:00_

1	Our evidence is correlational and theoretical (MBR framework, conditional decomposition), not interventional: we have not performed controlled interventions (e.g., artificially varying degeneracy while holding other factors constant), and the cascade stages interact in ways that resist decomposition into independent causal effects ($R^2{<}0$; \S\ref{sec:selection_gap}); causal claims require future intervention experiments.
2	
3	Scope: structured IE (NER primary, RE and SQL exploratory), English only, open-weight (Qwen and LLaMA) and closed-source (GPT-5.5) families, fine-tuned (4B--14B) and zero-shot (72B, GPT-5.5) regimes, sample budget $N{\leq}32$.
4	Our evaluation covers four NER datasets; the RE extension covers a single SciERC benchmark ($n{=}397$; $40$\% of instances yield zero F1, primarily from upstream entity span errors), and the SQL extension covers a single Spider subset ($n{=}196$) with 87.2\% degeneracy---both are exploratory and do not support generalization claims.
5	All experiments use English-language datasets; cross-lingual generalization remains untested.
6	Cross-model consistency results (\S\ref{sec:cross_model}) are limited to one dataset (Few-NERD) and one model pair (Qwen3-8B + LLaMA-3.1-8B).
7	Entity-level construction assumes the model produces useful partial outputs across samples; when model capability is insufficient (WNUT-17, 51\% F1${=}0$), this precondition fails and construction cannot improve over greedy.
8	Entity-level construction requires $N{\times}$ inference cost for $+1$\textendash$1.4$\,pp gain; cost-effectiveness may not justify deployment in resource-constrained settings.
9	We cover 4B\textendash 14B fine-tuned, 72B zero-shot, and GPT-5.5 zero-shot; the gap persists across all but behavior with 72B fine-tuning is untested.
10	Frontier API models exhibit markedly different degeneracy profiles (e.g., Claude Sonnet~4 at 74\% vs.\ DeepSeek Chat at 5.5\%; Table~\ref{tab:frontier_sc_cross}), suggesting that our findings from f
…[truncated 4566 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 3748 · 2026-05-22T10:13:54.410469+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 3749 · 2026-05-22T10:13:54.661809+00:00_

File content (65864 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 3750 · 2026-05-22T10:14:09.007312+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:read_local_file,TodoWrite",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:read_local_file,TodoWrite",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 3751 · 2026-05-22T10:14:09.108074+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 3752 · 2026-05-22T10:14:16.939203+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '完成资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'in_progress', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.7: 派发视觉审查', 'status': 'pending', 'activeForm': '派发视觉审查 Agent'}, {'content': 'Step 1: Round 1 独立审稿 — 分配 Reviewer 任务', 'status': 'pending', 'activeForm': '分配 Reviewer 审稿任务'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': '执行交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总并投递审稿报告'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '完成资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'in_progress', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.7: 派发视觉审查', 'status': 'pending', 'activeForm': '派发视觉审查 Agent'}, {'content': 'Step 1: Round 1 独立审稿 — 分配 Reviewer 任务', 'status': 'pending', 'activeForm': '分配 Reviewer 审稿任务'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': '执行交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总并投递审稿报告'}]"
  }
}
```

</details>

---


### Tool result

_source line 3753 · 2026-05-22T10:14:16.939711+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 3754 · 2026-05-22T10:14:17.642438+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "paper_checklist.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "file": "paper_checklist.yaml"
  }
}
```

</details>

---


### Tool result

_source line 3755 · 2026-05-22T10:14:17.694181+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'struct_self_consist_ie'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 3756 · 2026-05-22T10:14:22.913075+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml 2>/dev/null && echo \"EXISTS\" || echo \"NOT_FOUND\"",
  "description": "Check if review_issues.yaml exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml 2>/dev/null && echo \"EXISTS\" || echo \"NOT_FOUND\"",
    "description": "Check if review_issues.yaml exists"
  }
}
```

</details>

---


### Tool result

_source line 3757 · 2026-05-22T10:14:23.264832+00:00_

-rw-r--r-- 1 ubuntu ubuntu 13585 May 22 09:22 /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml
EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 3758 · 2026-05-22T10:14:23.415852+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/ 2>/dev/null && echo \"DIR_EXISTS\" || echo \"DIR_NOT_FOUND\"",
  "description": "Check review reports directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_reports/ 2>/dev/null && echo \"DIR_EXISTS\" || echo \"DIR_NOT_FOUND\"",
    "description": "Check review reports directory"
  }
}
```

</details>

---


### Tool result

_source line 3759 · 2026-05-22T10:14:23.466648+00:00_

total 568
drwxr-xr-x   2 ubuntu ubuntu  4096 May 22 09:06 .
drwxr-xr-x 151 ubuntu ubuntu 20480 May 22 10:12 ..
-rw-r--r--   1 ubuntu ubuntu  8866 May 16 03:06 data_integrity_audit_v2.md
-rw-r--r--   1 ubuntu ubuntu 11576 May 14 12:20 round_0.md
-rw-r--r--   1 ubuntu ubuntu 16761 May 15 02:09 round_1.md
-rw-r--r--   1 ubuntu ubuntu 15622 May 16 02:29 round_10.md
-rw-r--r--   1 ubuntu ubuntu 15266 May 16 04:34 round_11.md
-rw-r--r--   1 ubuntu ubuntu 15571 May 16 05:32 round_12.md
-rw-r--r--   1 ubuntu ubuntu 10927 May 16 06:55 round_13.md
-rw-r--r--   1 ubuntu ubuntu 16657 May 16 08:02 round_14.md
-rw-r--r--   1 ubuntu ubuntu 15908 May 16 08:58 round_15.md
-rw-r--r--   1 ubuntu ubuntu 13412 May 17 06:42 round_16.md
-rw-r--r--   1 ubuntu ubuntu 15352 May 17 07:27 round_17.md
-rw-r--r--   1 ubuntu ubuntu  9583 May 18 01:47 round_18.md
-rw-r--r--   1 ubuntu ubuntu 15884 May 18 06:16 round_19.md
-rw-r--r--   1 ubuntu ubuntu 14511 May 15 02:56 round_2.md
-rw-r--r--   1 ubuntu ubuntu 13356 May 18 13:19 round_20.md
-rw-r--r--   1 ubuntu ubuntu 15281 May 19 03:51 round_21.md
-rw-r--r--   1 ubuntu ubuntu 13992 May 19 05:08 round_22.md
-rw-r--r--   1 ubuntu ubuntu 13524 May 19 06:26 round_23.md
-rw-r--r--   1 ubuntu ubuntu 17272 May 20 13:24 round_24.md
-rw-r--r--   1 ubuntu ubuntu 16727 May 20 14:42 round_25.md
-rw-r--r--   1 ubuntu ubuntu 13640 May 21 04:53 round_26.md
-rw-r--r--   1 ubuntu ubuntu 15149 May 21 11:45 round_27.md
-rw-r--r--   1 ubuntu ubuntu 17021 May 21 15:27 round_29.md
-rw-r--r--   1 ubuntu ubuntu 15327 May 15 04:14 round_3.md
-rw-r--r--   1 ubuntu ubuntu 16290 May 21 17:17 round_30.md
-rw-r--r--   1 ubuntu ubuntu 16429 May 22 01:19 round_31.md
-rw-r--r--   1 ubuntu ubuntu 13531 May 22 08:21 round_33.md
-rw-r--r--   1 ubuntu ubuntu 15638 May 22 09:06 round_34.md
-rw-r--r--   1 ubuntu ubuntu 14214 May 15 07:08 round_4.md
-rw-r--r--   1 ubuntu ubuntu 14121 May 15 08:08 round_5.md
-rw-r--r--   1 ubuntu ubuntu 14108 May 15 09:05 round_6.md
-rw-r--r--   1 ubuntu
…[truncated 178 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 3760 · 2026-05-22T10:14:46.975311+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "struct_self_consist_ie",
  "review_chat_id": "oc_3897c2857f11615119e277e820eae311"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "review_chat_id": "oc_3897c2857f11615119e277e820eae311"
  }
}
```

</details>

---


### Tool result

_source line 3761 · 2026-05-22T10:15:01.986720+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 15011
}
```

</details>

---


### Tool call

_source line 3762 · 2026-05-22T10:15:02.188448+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "你是 Reviewer 1，负责审查 **方法严谨性 + 实验设计**。\n\n## Venue 信息\n- **目标会议**: EMNLP 2026 via ARR May 2026\n- **截止日期**: 2026-05-25\n- **页数限制**: Long paper，正文 8 页，参考文献无限\n- **模板**: ACL 模板 (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind\n- **Limitations**: 必须包含\n\n## 论文信息\n- **标题**: When Does Test-Time Scaling Fail? Boundary Conditions for Structured Prediction\n- **论文路径**: `projects/struct_self_consist_ie/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_round_35/submitted.pdf`\n\n## 你的审查侧重\n\n请重点审查以下方面：\n\n1. **诊断框架有效性**：四阶段 cascade（degeneracy → oracle headroom → LP compression → signal alignment）是否逻辑自洽？每个阶段的度量是否有效？\n2. **统计分析严谨性**：\n   - 多重比较校正（Holm-Bonferroni k=57）是否恰当？\n   - 3-seed 统计功效是否足够？SciERC 仅 1 seed 是否构成威胁？\n   - Bootstrap CI、paired tests 的使用是否正确？\n   - MDE 分析是否合理？\n3. **实验设计完整性**：\n   - 4 个 NER 数据集 + RE + SQL 的覆盖度是否足够？\n   - 模型选择（Qwen3-8B, LLaMA-3.1-8B 为主，4B/14B/72B/GPT-5.5 为辅）是否合理？\n   - N=8 为主、N∈{16,32,64} 为辅的 scaling 是否充分？\n   - Constrained decoding 是否是混淆因素？free-form ablation 是否充分解决？\n4. **基线公平性**：greedy baseline 的设置是否合理？9 种方法的对比是否公平？\n5. **消融实验**：温度、seed、epoch、LoRA rank 等消融是否覆盖关键变量？\n6. **可复现性**：实验细节是否足以复现？\n\n请按 ARR 标准给出完整审稿意见：Summary → Strengths → Weaknesses → Questions → Overall Assessment。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "你是 Reviewer 1，负责审查 **方法严谨性 + 实验设计**。\n\n## Venue 信息\n- **目标会议**: EMNLP 2026 via ARR May 2026\n- **截止日期**: 2026-05-25\n- **页数限制**: Long paper，正文 8 页，参考文献无限\n- **模板**: ACL 模板 (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind\n- **Limitations**: 必须包含\n\n## 论文信息\n- **标题**: When Does Test-Time Scaling Fail? Boundary Conditions for Structured Prediction\n- **论文路径**: `projects/struct_self_consist_ie/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_round_35/submitted.pdf`\n\n## 你的审查侧重\n\n请重点审查以下方面：\n\n1. **诊断框架有效性**：四阶段 cascade（degeneracy → oracle headroom → LP compression → signal alignment）是否逻辑自洽？每个阶段的度量是否有效？\n2. **统计分析严谨性**：\n   - 多重比较校正（Holm-Bonferroni k=57）是否恰当？\n   - 3-seed 统计功效是否足够？SciERC 仅 1 seed 是否构成威胁？\n   - Bootstrap CI、paired tests 的使用是否正确？\n   - MDE 分析是否合理？\n3. **实验设计完整性**：\n   - 4 个 NER 数据集 + RE + SQL 的覆盖度是否足够？\n   - 模型选择（Qwen3-8B, LLaMA-3.1-8B 为主，4B/14B/72B/GPT-5.5 为辅）是否合理？\n   - N=8 为主、N∈{16,32,64} 为辅的 scaling 是否充分？\n   - Constrained decoding 是否是混淆因素？free-form ablation 是否充分解决？\n4. **基线公平性**：greedy baseline 的设置是否合理？9 种方法的对比是否公平？\n5. **消融实验**：温度、seed、epoch、LoRA rank 等消融是否覆盖关键变量？\n6. **可复现性**：实验细节是否足以复现？\n\n请按 ARR 标准给出完整审稿意见：Summary → Strengths → Weaknesses → Questions → Overall Assessment。"
  }
}
```

</details>

---


### Tool result

_source line 3763 · 2026-05-22T10:15:13.712327+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 11523
}
```

</details>

---


### Tool call

_source line 3764 · 2026-05-22T10:15:13.863362+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "你是 Reviewer 2，负责审查 **新颖性 + 完整性**。\n\n## Venue 信息\n- **目标会议**: EMNLP 2026 via ARR May 2026\n- **截止日期**: 2026-05-25\n- **页数限制**: Long paper，正文 8 页，参考文献无限\n- **模板**: ACL 模板 (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind\n- **Limitations**: 必须包含\n\n## 论文信息\n- **标题**: When Does Test-Time Scaling Fail? Boundary Conditions for Structured Prediction\n- **论文路径**: `projects/struct_self_consist_ie/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_round_35/submitted.pdf`\n\n## 你的审查侧重\n\n请重点审查以下方面：\n\n1. **新颖贡献评估**：\n   - \"correlation-selection gap\" 这一发现是否有足够新颖性？与 Yao et al. (2026), Yun & Price (2025), Chen et al. (2023) 的区别是否清晰？\n   - Capability-diversity tension 作为 central finding 是否有足够深度？\n   - 诊断 cascade 作为方法论贡献是否有独立价值？\n2. **相关工作覆盖**：\n   - MBR decoding、uncertainty estimation、self-consistency 等领域的引用是否完整？\n   - 是否遗漏了重要的 concurrent work？\n   - 与 Yun & Price (2025) 的差异化论述是否充分？\n3. **写作质量**：\n   - 论文结构是否清晰？Discover → Diagnose → Explore 的叙事是否连贯？\n   - Abstract 和 Introduction 是否准确反映论文贡献？\n   - 术语定义是否一致（degeneracy、alignment collapse、introspection boundary）？\n   - 是否存在 overclaim 或 underclaim？\n4. **论文完整性**：\n   - Limitations 是否覆盖关键限制？\n   - Ethics Statement 是否合规？\n   - 匿名化是否到位（检查是否泄露作者身份）？\n   - 页数是否符合 8 页限制？\n5. **Findings vs. Main Conference 定位**：\n   - 这篇论文的贡献水平适合 Main Conference 还是 Findings？\n   - 作为 primarily empirical/diagnostic 的工作，理论深度是否足够？\n\n请按 ARR 标准给出完整审稿意见：Summary → Strengths → Weaknesses → Questions → Overall Assessment。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "你是 Reviewer 2，负责审查 **新颖性 + 完整性**。\n\n## Venue 信息\n- **目标会议**: EMNLP 2026 via ARR May 2026\n- **截止日期**: 2026-05-25\n- **页数限制**: Long paper，正文 8 页，参考文献无限\n- **模板**: ACL 模板 (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind\n- **Limitations**: 必须包含\n\n## 论文信息\n- **标题**: When Does Test-Time Scaling Fail? Boundary Conditions for Structured Prediction\n- **论文路径**: `projects/struct_self_consist_ie/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_round_35/submitted.pdf`\n\n## 你的审查侧重\n\n请重点审查以下方面：\n\n1. **新颖贡献评估**：\n   - \"correlation-selection gap\" 这一发现是否有足够新颖性？与 Yao et al. (2026), Yun & Price (2025), Chen et al. (2023) 的区别是否清晰？\n   - Capability-diversity tension 作为 central finding 是否有足够深度？\n   - 诊断 cascade 作为方法论贡献是否有独立价值？\n2. **相关工作覆盖**：\n   - MBR decoding、uncertainty estimation、self-consistency 等领域的引用是否完整？\n   - 是否遗漏了重要的 concurrent work？\n   - 与 Yun & Price (2025) 的差异化论述是否充分？\n3. **写作质量**：\n   - 论文结构是否清晰？Discover → Diagnose → Explore 的叙事是否连贯？\n   - Abstract 和 Introduction 是否准确反映论文贡献？\n   - 术语定义是否一致（degeneracy、alignment collapse、introspection boundary）？\n   - 是否存在 overclaim 或 underclaim？\n4. **论文完整性**：\n   - Limitations 是否覆盖关键限制？\n   - Ethics Statement 是否合规？\n   - 匿名化是否到位（检查是否泄露作者身份）？\n   - 页数是否符合 8 页限制？\n5. **Findings vs. Main Conference 定位**：\n   - 这篇论文的贡献水平适合 Main Conference 还是 Findings？\n   - 作为 primarily empirical/diagnostic 的工作，理论深度是否足够？\n\n请按 ARR 标准给出完整审稿意见：Summary → Strengths → Weaknesses → Questions → Overall Assessment。"
  }
}
```

</details>

---


### Tool result

_source line 3765 · 2026-05-22T10:15:15.692960+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1829
}
```

</details>

---


### Tool call

_source line 3766 · 2026-05-22T10:15:22.389449+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '完成资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.7: 派发视觉审查', 'status': 'completed', 'activeForm': '派发视觉审查 Agent'}, {'content': 'Step 1: Round 1 独立审稿 — 等待 Reviewer 返回', 'status': 'in_progress', 'activeForm': '等待 Reviewer 1 和 Reviewer 2 返回审稿意见'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': '执行交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总并投递审稿报告'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '完成资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.7: 派发视觉审查', 'status': 'completed', 'activeForm': '派发视觉审查 Agent'}, {'content': 'Step 1: Round 1 独立审稿 — 等待 Reviewer 返回', 'status': 'in_progress', 'activeForm': '等待 Reviewer 1 和 Reviewer 2 返回审稿意见'}, {'content': 'Step 2: 交叉分享', 'status': 'pending', 'activeForm': '执行交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总并投递审稿报告'}]"
  }
}
```

</details>

---


### Tool result

_source line 3767 · 2026-05-22T10:15:22.389947+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "TodoWrite",
  "elapsed_ms": 0
}
```

</details>

---


### Assistant

_source line 3768 · 2026-05-22T10:15:26.884100+00:00_

Round 1 已启动：
- 视觉审查 Agent 已派发（fire-and-forget）
- Reviewer 1（方法严谨性 + 实验设计）已分配
- Reviewer 2（新颖性 + 完整性）已分配
- 外部审稿未配置，跳过

等待两位 Reviewer 返回独立审稿意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 278

## Round 278

2 recorded events


### User

_source line 3769 · 2026-05-22T10:21:15.976747+00:00_

[Reviewer 1 审稿意见]:

## 总体评分
**Overall**: 3.5 — Borderline Conference
**一句话总结**: 在 NER 上对 test-time scaling 失败条件进行了统计严谨的实证分析，提出了有用的诊断框架，但"结构化预测"的广泛声明超出了实际证据范围（主要是 NER），且 SciERC 单 seed 是统计弱点。

## 官方维度打分（来自 ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | NER 核心 claim 有充分实验支撑，统计方法论（Holm-Bonferroni k=57、MDE、bootstrap CI、equivalence testing）远超 NLP 论文平均水平；但 SciERC 单 seed、entity independence 假设、以及 RE/SQL 证据薄弱削弱了泛化声明 |
| Excitement | 3.5/5 | 研究问题及时（test-time scaling 热门话题），correlation-selection gap 是真实的新发现；但发现主要是描述性/负面结果，prescriptive guidance 有限，capability-diversity tension 未深入形式化 |
| Overall Assessment | 3.5/5 | Borderline Conference — 扎实的 NER 实证工作 + 有用的诊断框架，但 scope 与 evidence 之间有 gap |
| Reproducibility | 4/5 | Appendix k 提供了完整的训练配置（Table 20），代码承诺公开，实验细节充分；但 GPU 总计算预算未报告，prompt 模板虽提及但未完整展示 |
| Confidence | 4/5 | 我仔细审查了方法论、统计分析和实验设计，熟悉 self-consistency 和 NER 文献 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Title/Scope 与实际证据不匹配："Structured Prediction" vs. 实际主要是 NER
- 具体位置：Title, Abstract, Section 1 (Introduction), Section 9 (Discussion)
- 问题：标题声称研究"structured prediction"的 boundary conditions，但实际充分实验的只有 NER（4 个数据集 × 2 模型家族）。RE 仅作为 SciERC 上的 exploratory extension（Appendix o, p.29，仅用 Qwen3-8B 1 个模型），共 397 个 full-set 实例。SQL parsing 仅在 Section 4 中以一句话提及 87.2% degeneracy，无任何 selection 或 diagnostic cascade 分析。Abstract 第一句就说"structured prediction remains uncharacterized"，但论文只 characterize 了 NER 和初步的 RE。
- 为什么影响接收：Reviewer 和读者会期望看到对 structured prediction 的广泛验证（parsing、code generation、relation extraction、event extraction 等），否则 claim 与 evidence 之间的 gap 会严重影响可信度。Discussion (p.8) 承认"generalization to other structured tasks requires further investigation"，但这应该反映在标题和 abstract 的 scope 定义中。
- 建议修改方向：(a) 将标题和 abstract 限定为 NER（如 "Boundary Conditions for Entity Recognition"），或 (b) 补充至少一个非 NER structured prediction task 的完整分析（如完整的 RE diagnostic cascade + selection analysis，或 SQL/code generation 的系统实验）。

**N2** [critical] SciERC 仅 1 个 seed 构成统计可靠性威胁
- 具体位置：Section 7.1 (p.6), Appendix C.2 (p.10), Table 3 (p.7), Table 12 (p.25)
- 问题：SciERC 是四个 NER 数据集中最核心的一个（论文中分析最详尽），但仅使用 1 个 training seed（seed=42）。Few-NERD 和 CoNLL 使用 3 seeds。SciERC 测试集仅 529 实例。论文自己承认 "SciERC uses 1 primary seed with high seed sensitivity (σ=0-0.48 pp, n=529)"（p.10, Checklist C.3），且 Table 36 (p.34) 显示 SciERC 上 Kendall's W 虽然高（>0.9），但这只衡量排名稳定性，不保证绝对值的稳定性。
- MDE 分析（Table 58, p.42）显示 n=23 configurations 下 80% power 仅能检测 ρ≥0.5 的效应，对 ρ=0.3 需要 n≈85。这意味着 SciERC 上许多中等效应可能被遗漏。
- 为什么影响接收：SciERC 是论文中最具挑战性的数据集（degeneracy 最低，headroom 最大），许多核心发现（如 correlation-selection gap 的首次发现 Figure 2、LP compression 分析、entity-level verification probes）都以 SciERC 为 primary showcase。单 seed 的结果不确定性大——如果另一个 seed 的 fine-tuned 模型表现不同，核心结论可能动摇。
- 建议修改方向：(a) 在 SciERC 上补充至少 2 个额外 seeds 的实验（或报告 3-seed 结果），(b) 如果计算资源不允许，至少提供更详细的 sensitivity analysis（如 bootstrap resampling 的 seed 依赖性分析），(c) 在 Discussion 中明确将 SciERC 的单 seed 结果标记为 tentative。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Diagnostic cascade 的理论基础依赖 entity independence 假设
- 具体位置：Proposition 1 (p.31), Remark (p.31)
- 问题：Proposition 1 的核心推导假设 entity-wise independence（"each entity inclusion is an independent binary decision"）。Remark 承认这是近似的（"balanced set-overlap and F1 induce a closed-form threshold rule"），且使用 balanced F1 作为近似。但结构化预测的关键特征恰恰是实体之间有依赖关系（如同一句中的嵌套实体、相关实体类型的共现）。论文提到 actual entity correlations 为 3-12%（p.6），但未量化这对 bound 的影响。
- 建议：(a) 提供 correlation 3-12% 下 bound 偏移的数值分析，(b) 讨论何时 independence 假设会显著失效（如嵌套 NER、密集实体文本）。

**W2** [warning] 9 种方法对比的公平性问题
- 具体位置：Table 2 (p.5), Section 5
- 问题：Table 2 比较了 9 种方法，但计算预算不等。Cross-model SC 使用了额外模型（Qwen + LLaMA）的 outputs，计算量至少翻倍。Multi-round MRC 需要多轮 prompting。与仅用 N=8 samples 的 LP/SI/FK selection 方法相比，这不是等计算预算比较。Table 65 (p.45) 的 cost-benefit analysis 部分解决了这一问题（显示 entity construction 是唯一 consistently positive 的方法），但主文 Table 2 的呈现方式容易误导读者。
- 建议：在 Table 2 中添加一列标注各方法的 compute cost（如相对于 greedy 的倍数），或在 caption 中明确说明。

**W3** [warning] Greedy baseline 的选择可能低估了 test-time scaling 的潜力
- 具体位置：Section 2.3 (p.3), Table 1 (p.4)
- 问题：Greedy decoding (T=0) 是主 baseline。但在实际部署中，用户可能使用 T>0 的单次采样（非 greedy）作为 baseline。如果 baseline 是 T=0.7 或 T=1.0 的单次采样，self-consistency 的 gain 可能更大，因为 greedy 本身已经是一种"最佳单样本"策略。论文在 Appendix n (p.28) 讨论了 consistency-stratified selection，但未直接对比 "T=1.0 single sample vs. majority vote of N=8 at T=1.0"。
- 建议：补充 random single sample at T=1.0 作为额外 baseline 的对比，以展示 self-consistency 相对于非确定性 baseline 的 gain。

**W4** [warning] Capability-diversity tension 是核心发现但缺乏形式化
- 具体位置：Section 9 (p.8), Section 6.1 (p.5)
- 问题：论文将"capability-diversity tension"呈现为 central finding（p.8: "The central finding is a capability-diversity tension"），声称随着模型能力提升，output convergence rises 但 test-time scaling returns diminish。但这一 tension 没有形式化定义或量化指标。Section 6.1 的 scaling analysis（Figure 3）仅显示 3 个数据集上 MV ΔF1 vs. log₂(N) 的趋势，且 CoNLL 在 N=64 时 MV gain 为正。缺乏对 "在什么 capability 水平下 scaling returns 开始 diminish" 的精确刻画。
- 建议：(a) 给 capability-diversity tension 一个可测量的定义（如 degeneracy rate vs. oracle headroom 的 trade-off curve），(b) 或降低 framing，不将其作为 "central finding" 而是 "observed pattern"。

**W5** [warning] Free-form decoding ablation 仅覆盖 SciERC + CoNLL，不够全面
- 具体位置：Section q (p.32), Table 33
- 问题：Constrained decoding 是一个潜在混淆因素（限制输出空间可能人为压缩 LP 分布）。Free-form ablation 仅在 SciERC（4 seeds）和 CoNLL（p.32）上进行。Few-NERD（最大数据集）和 WNUT-17 未覆盖。CoNLL 的 free-form 结果显示 "free-form decoding reduces the tied fraction modestly, yet selection remains below single-sample"（p.32），但 Few-NERD 上 degeneracy 最低，可能是 free-form 影响最大的数据集。
- 建议：补充 Few-NERD 的 free-form decoding ablation。

---

## 小问题（不影响接收）

- **Figure 2 (p.4)**: Correlation-selection gap 图的 y 轴标签 "ΔF1" 与 "ρ" 共用同一图但量纲不同，初看容易混淆。建议分成双轴或更清晰的标注。
- **Section 2.2 (p.2)**: "Soft Jaccard [SJ]" 的定义引用了 Fleiss 1971，但 Soft Jaccard 通常不归于 Fleiss。请确认引用正确性。
- **Table 5 (p.14)**: Notation table 中 "SJ" 定义为 "Soft localized similarity"，但正文中有时称 "Soft Jaccard"，有时称 "structural similarity"——术语应统一。
- **Appendix p.2 (Proposition 2, p.30)**: MBR connection 的 Remark 提到 "We use balanced linear utility (v=1)"，但未解释为何 v=1 是合理选择。
- **p.7 Table 4**: "Instance degeneracy vs. LP selection gain across 23 configurations" 的 caption 说 "paired bootstrap"，但表中报告的是 Spearman ρ 而非 bootstrap 统计量，caption 可能有误。
- **Ethics Statement (p.10)**: 声称 "No dual-use concerns"，但论文的 diagnostic framework 可能被用于优化 adversarial attacks on structured outputs（如优化 NER poisoning 策略）。建议至少简要讨论。

---

## 主要优势

1. **统计方法论显著超越同行水平**：Holm-Bonferroni 全局校正（k=57 tests, Table 12）、MDE 分析（Table 58）、equivalence testing（TOST, Table 15-16）、bootstrap CI、permutation tests 的组合使用在 NLP 论文中极为罕见。这为实证分析设立了高标准。

2. **Diagnostic cascade 概念清晰且实用**：四阶段 cascade（degeneracy → oracle headroom → LP compression → signal alignment）逻辑自洽，每个阶段都有可操作的度量。Appendix ae (p.44) 将其整理为可复用的三步评估协议，对社区有直接实用价值。

3. **异常详尽的消融和 robustness 分析（47 页）**：覆盖 temperature（Table 6/45）、sample size scaling（Table 38）、epoch（Table 55-56）、LoRA rank（Section 7.4）、cross-model transfer（Section 5.1）、OOD（Table 47）、free-form decoding（Table 33）、thinking tokens（Section l）、entity-level LP decomposition（Section m）、construction threshold sensitivity（Table 62）等。这种彻底性极大增强了核心发现的可信度。

4. **Failure mode gallery (Appendix ag, p.47)** 提供了 9 个具体失败案例的质性分析，直观展示了 degeneracy、LP confidence failure 和 consensus-based verification failure 三类典型错误模式，有教学价值。

5. **Honest about limitations**：MDE 分析坦承 "absence of evidence, not evidence of absence"（p.42），Limitations 章节讨论了 prompt 模板、controlled intervention、cascade 因果性等限制。这种自我批评在稿件中不常见。

6. **Correlation-selection gap 是一个有价值的概念贡献**：将"QE 信号有效"与"selection 成功"解耦，指出两者之间存在系统性断裂。Figure 1 的可视化清晰传达了这一核心 insight。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 3770 · 2026-05-22T10:21:24.102436+00:00_

Reviewer 1 审稿意见已收到。等待 Reviewer 2 返回后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 279

## Round 279

2 recorded events


### User

_source line 3771 · 2026-05-22T10:21:26.828911+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

**总结**：Overall 3.5（Borderline Conference）。论文在 NER test-time scaling 失败条件分析上做了扎实的实证工作，统计方法论远超 NLP 论文平均水平（Holm-Bonferroni k=57、MDE、equivalence testing），diagnostic cascade 是有价值的概念贡献。

两个 critical 问题：(1) 标题声称"structured prediction"但证据主要是 NER，RE/SQL 覆盖极薄；(2) 核心数据集 SciERC 仅 1 seed。五个 warning 级问题涵盖 entity independence 假设、方法对比公平性、greedy baseline 选择、capability-diversity tension 形式化不足、free-form ablation 覆盖不全。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 3772 · 2026-05-22T10:21:33.895588+00:00_

Reviewer 1 意见已收到。等待 Reviewer 2 返回后进行交叉分享。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 280

## Round 280

8 recorded events


### User

_source line 3773 · 2026-05-22T10:21:53.114475+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿意见：新颖性 + 完整性

**论文**: When Does Test-Time Scaling Fail? Boundary Conditions for Structured Prediction
**Venue**: EMNLP 2026 via ARR May 2026

---

## 总体评分
**Overall**: 3.5 (Borderline Conference)
**一句话总结**: 扎实的经验性诊断工作，"correlation-selection gap"是有价值的发现，但任务范围局限于 NER、理论贡献偏薄、且部分 claim 超出了实验证据的支撑范围，处于 Conference 和 Findings 的边界。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 实验方法论扎实（bootstrap CI、Holm-Bonferroni correction、57 项统计检验），但理论分析基于强独立性假设（Proposition 1），且从 NER 推广到 "structured prediction" 的 claim 超出了实验覆盖 |
| Excitement | 3/5 | correlation-selection gap 是有用的经验发现，诊断 cascade 有方法论价值，但整体是诊断性工作而非提出解决方案，且核心发现对熟悉结构化输出的研究者而言有一定可预见性 |
| Reproducibility | 4/5 | 详细的超参设置（Appendix k, Table 20）、3-seed 均值 + CI、代码承诺释放、数据集均为公开基准；但未报告总 GPU 小时数，部分 72B 实验未说明精确配置 |
| Confidence | 4/5 | 我熟悉 self-consistency、test-time scaling 和 NER 领域的相关工作 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Scope overclaim：论文标题和 Abstract 声称研究 "structured prediction" 的 boundary conditions，但实验覆盖几乎仅限 NER（4 个数据集）+ 极初步的 RE 扩展（Appendix o, §6.3 仅 1 段 + Table 45）

- 具体位置：Title、Abstract ("for set-valued outputs")、Section 9 Conclusion ("structured prediction")
- 问题：NER 的 entity-set 输出结构（无序集合 + span 级别）与其他结构化预测任务差异巨大——如 dependency parsing（树结构）、SRL（predicate-argument 结构）、event extraction（嵌套结构）。论文的核心发现——degeneracy（重复/空输出）和 signal alignment collapse——很可能是 NER 特有的 artifact，而非 structured prediction 的通用 boundary condition。RE 扩展过于初步（仅 SciERC 一个数据集），不足以支撑泛化 claim。
- 为什么影响接收：Reviewer 和 AC 期望标题与实际贡献匹配。如果论文框架为 "NER/IE boundary conditions"，evaluation criteria 会更宽松；但 "structured prediction" 的框架设定了更高的验证门槛，当前实验不满足。
- 建议：(a) 将标题和 abstract 限缩为 NER / information extraction；或 (b) 增加至少 2 个结构不同的任务（如 dependency parsing、event extraction）的实验验证。

**N2** [critical] Capability-diversity tension 作为 central finding 缺乏足够深度

- 具体位置：Section 9 "The central finding is a capability-diversity tension"、Figure 3
- 问题：模型能力越强 → 输出越趋同 → 多样性降低 → test-time scaling 收益递减——这一观察在 test-time scaling 文献中已有隐含讨论。Snell et al. (2025, ICLR) 的 compute-optimal scaling 框架已指出 easy/hard 问题的最优策略不同；Brown et al. (2024) 在 "large language monkeys" 中展示了 coverage 随 N 增长的 diminishing returns。本文的贡献是将此具象化到 NER 中的 degeneracy rate（Figure 3 的 Δ 趋势），但作为 "central finding" 缺乏理论刻画——Proposition 1 基于 pair-wise independence 假设（§p.3），而实际 NER 输出高度相关（论文自身在 §b 报告 split-half r≈0.578-0.644）。
- 为什么影响接收：如果 central finding 被认为是已知 insight 的任务特定实例化，会显著削弱 excitement 评分。
- 建议：(a) 正式引用和对比 Snell et al. (2025) 和 Brown et al. (2024) 中关于 diminishing returns 的讨论；(b) 要么弱化 "central finding" 的定位，要么提供更强的理论分析（如松弛独立性假设的 bound）。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] 正文可能超出 8 页限制

- 具体位置：Page 8 → Page 9 过渡处
- 问题：Section 9 (Discussion and Conclusion) 从 Page 8 右栏开始，但结论段落 "Conclusion. We characterize when test-time compute scaling fails..." 延续到 Page 9 左栏顶部（约 3-4 行）。Limitations section 在这之后才开始。根据 EMNLP 2026 规则，"Mandatory limitations and optional ethical considerations do not count towards this page limit"，但主体文本（含 Conclusion）必须在 8 页内。当前排版使 Conclusion 溢出到 Page 9。
- 建议：压缩 Related Work (§8) 或 Discussion (§9) 中的冗余内容以确保 Conclusion 在 Page 8 内结束。这是纯粹的排版问题，修复难度低。

**W2** [warning] 与 Yun & Price (2025) 的差异化论述不够充分

- 具体位置：§8 "What is new relative to concurrent work"、Table 66（Appendix af）
- 问题：Table 66 的差异化矩阵列出了 4 个维度的比较（root cause, tasks, methods tested, theoretical construct），但 Yun & Price (2025) 的 "price of format diversity collapse" 概念与本文的 "signal alignment collapse (α→0)" 在语义上高度重叠——两者都在描述模型输出多样性消失导致 selection 失效。论文未正面讨论这两个概念的本质区别。此外，Yun & Price 的论文在引用列表中标注为 "EMNLP 2025"，但主文 §8 仅用一句话带过差异。
- 建议：在 §8 中增加 1-2 段明确对比：(a) alignment collapse 和 format diversity collapse 的定义级区别；(b) 本文的诊断 cascade 在 Yun & Price 的框架中是否可复现或是否提供增量信息。

**W3** [warning] 相关工作缺少重要领域

- 具体位置：§8 Related Work
- 问题：
  (a) **Conformal prediction for NLP structured outputs**——近年有多项工作将 conformal prediction 应用于 NER/序列标注的 uncertainty quantification，与本文的 quality estimation + selection 管线高度相关，但完全未讨论。
  (b) **Token-level uncertainty decomposition**——如 Xiao et al. (2020) 的 epistemic/aleatoric 分解，与本文的 LP/entropy 信号分析直接相关。
  (c) **Active learning for structured prediction**——该领域 20+ 年的文献大量讨论了 structured output 的 uncertainty-based selection，是自然的 intellectual predecessor。
  (d) **MBR decoding with structural utility**——论文引用了 Eikema & Aziz (2022) 和 Eikema et al. (2025, structural-conditional MBR)，但未讨论将 entity-level F1 作为 MBR utility function 的可能性——这在概念上就是 §5 entity-level construction 的 principled 版本。
- 建议：在 §8 末尾增加 1 段涵盖上述领域，明确论文定位与这些方向的关系。

**W4** [warning] 诊断 cascade 的独立方法论价值需要更多验证

- 具体位置：§2-§4（Discover → Diagnose 流程）
- 问题：论文提出的三阶段诊断 cascade（quality estimation → selection → construction）是一个有用的方法论框架，但当前仅在 NER 上验证。如果作者将此定位为通用的诊断方法论（如 Abstract 所暗示），需要展示它在至少一个额外任务上的适用性。此外，cascade 中的具体阈值（如 degeneracy >30% 时 LP 失效、α<0.05 的 alignment collapse 临界点）是否 task-specific？论文未讨论这些阈值的 generalizability。
- 建议：(a) 明确说明阈值的 task-specificity；(b) 在 RE 扩展中完整运行 cascade 而非仅报告 LP 结果。

**W5** [warning] Proposition 1 的独立性假设与实际数据不符

- 具体位置：§p.3 Definition 1 & Proposition 1、Appendix p.4 Proof
- 问题：Proposition 1 假设 degenerate instances 的 N 个 samples 完全相同（"all N samples produce the same entity set"），而 non-degenerate instances 的 greedy output 等于 oracle。这是一个极端简化：(a) 现实中 partial degeneracy 普遍存在——论文自身报告 Few-NERD 上 48% 的 instances 有高多样性（>4 unique outputs, Appendix g）；(b) split-half reliability 仅 r≈0.578-0.644（Table 7），远低于完全一致。论文在 §p.4 提供了数值验证显示 bound 是 loose 的（actual/weak bound ratio 在 Table 31 中为 0.13-0.63），但这恰恰说明理论分析的指导价值有限。
- 建议：要么提供更 tight 的分析（松弛完全 degeneracy 假设），要么将 Proposition 1 明确降格为 "illustrative bound" 而非核心理论贡献。

---

## 小问题（不影响接收）

- **术语一致性**：论文引入了多个新术语——"correlation-selection gap"、"degeneracy"、"alignment collapse"、"introspection boundary"、"capability ceiling"——部分在不同 section 中使用方式略有不同。建议在 §2 统一给出定义列表。
- **Figure 1 可读性**：Figure 1 试图在一张图中展示三个概念（QE、selection、construction），信息密度过高。左侧的 AUROC=0.82 和 ρ=0.39 并列显示，但这两个数字来自不同的 evaluation protocol（分类 vs. 排序），容易混淆。
- **Table 2 过于密集**：9 methods × 7 columns 的表格难以快速解读。建议突出显示 key comparisons（如 best baseline vs. LP-best vs. cross-model）。
- **Appendix 体量**：37 页附录展示了极致的 thoroughness，但部分内容（如 Appendix ag failure mode gallery, Appendix af differentiation matrix）可以考虑浓缩。
- **"Introspection boundary" (§3)**：这个术语在论文后续部分很少被重新使用。如果不是核心概念，建议去掉以减少 cognitive load。

---

## 主要优势

1. **问题定义精准且有价值**：将 test-time scaling 的失效条件从 "有时不 work" 提升为可诊断的具体 boundary conditions（degeneracy rate + alignment collapse），对社区理解 SC 的适用边界有实际指导价值。

2. **实验方法论严谨**：3-seed 均值 + bootstrap CI、Holm-Bonferroni 多重比较校正（Table 12, 57 项检验）、split-half reliability test（Table 7）、TOST equivalence testing（Table 15）。统计实践达到高标准。

3. **Correlation-selection gap 是真正的 empirical contribution**：QE signals 能区分好坏输出（AUROC 0.82）但无法有效指导 selection（<1pp gain），这一 disconnect 是此前文献中未被清晰命名和系统量化的。Section 4 的分解分析（definitional vs. empirical layers）为理解 gap 来源提供了有用的框架。

4. **诚实报告**：论文没有过度渲染 bypass 策略的效果——cross-model SC 仅 +0.42pp、entity-level construction +1.4pp（§5, §6.1），如实呈现了这些方法的局限性。

5. **47 页附录的 exhaustive validation**：包括 per-type analysis（Appendix aa）、calibration analysis（Appendix e）、free-form decoding ablation（Appendix q）、N-scaling detailed analysis（Appendix t）、post-hoc power analysis（Appendix ab3），几乎覆盖了所有可预见的 reviewer 质疑。

---

## Questions for Authors

**Q1**: correlation-selection gap 是否在任何非 NER 的结构化预测任务中被验证过？如果 cascade 在 dependency parsing 或 event extraction 上运行，degeneracy rate 和 alignment collapse 的量化是否会有质的不同？

**Q2**: 既然 entity-level construction（§6.1）的 MBR framing 已经被提到，为什么没有直接实验 entity-level F1 作为 MBR utility function 的方案？这在概念上比 majority vote 更 principled，且实现成本不高。

**Q3**: Proposition 1 的 bound 在 Table 31 中 ratio 仅 0.13-0.63——这意味着理论 bound 至少松弛了 37%。作者是否考虑过更 tight 的分析，例如基于 partial degeneracy 的连续 bound？

**Q4**: Figure 3 展示的 MV ΔF1 vs. N 趋势中，Few-NERD 在 N=64 时仍有正向增益，而 SciERC 几乎平坦。这是否主要由 base model quality 驱动？如果使用更弱的模型（如 3B 或 1B），是否会观察到更大的 scaling gains？

---

## Findings vs. Main Conference 定位评估

这篇论文处于 Conference (4.0) 和 Findings (3.0) 的边界，我倾向 **3.5 (Borderline Conference)**。

**支持 Conference 的因素**：
- correlation-selection gap 是社区有用的经验发现
- 诊断框架有方法论价值
- 实验方法论高标准

**倾向 Findings 的因素**：
- 核心贡献是诊断性的（"what fails"）而非建设性的（"how to fix"）
- 任务范围过窄不支撑 "structured prediction" 的泛化 claim
- capability-diversity tension 作为 central finding 的新颖性增量有限
- 理论贡献（Proposition 1）偏薄

如果作者能在 camera-ready 中 (a) 限缩 claim 范围到 NER/IE，(b) 加强与 Yun & Price (2025) 的差异化论述，(c) 修复页数溢出，这篇论文可以达到 Conference 水平（4.0）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 3774 · 2026-05-22T10:22:05.919557+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '完成资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.7: 派发视觉审查', 'status': 'completed', 'activeForm': '派发视觉审查 Agent'}, {'content': 'Step 1: Round 1 独立审稿 — 收集 Reviewer 意见', 'status': 'completed', 'activeForm': '收集 Reviewer 审稿意见'}, {'content': 'Step 2: 交叉分享 — 互换意见并要求逐条回应', 'status': 'in_progress', 'activeForm': '执行交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总并投递审稿报告'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '完成资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.7: 派发视觉审查', 'status': 'completed', 'activeForm': '派发视觉审查 Agent'}, {'content': 'Step 1: Round 1 独立审稿 — 收集 Reviewer 意见', 'status': 'completed', 'activeForm': '收集 Reviewer 审稿意见'}, {'content': 'Step 2: 交叉分享 — 互换意见并要求逐条回应', 'status': 'in_progress', 'activeForm': '执行交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'pending', 'activeForm': '判断是否收敛'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'pending', 'activeForm': '汇总并投递审稿报告'}]"
  }
}
```

</details>

---


### Tool result

_source line 3775 · 2026-05-22T10:22:06.020430+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "TodoWrite",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 3776 · 2026-05-22T10:22:26.622319+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Must-Fix、Should-Fix 和主要论点，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 完整审稿意见\n\n**Overall**: 3.5 (Borderline Conference)\n**一句话总结**: 扎实的经验性诊断工作，\"correlation-selection gap\"是有价值的发现，但任务范围局限于 NER、理论贡献偏薄、且部分 claim 超出了实验证据的支撑范围，处于 Conference 和 Findings 的边界。\n\n### Must-Fix 问题\n\n**N1** [critical] Scope overclaim：标题和 Abstract 声称研究 \"structured prediction\" 的 boundary conditions，但实验覆盖几乎仅限 NER + 极初步的 RE 扩展。NER 的 entity-set 输出结构与 dependency parsing、SRL、event extraction 差异巨大。RE 扩展过于初步（仅 SciERC 一个数据集），不足以支撑泛化 claim。\n\n**N2** [critical] Capability-diversity tension 作为 central finding 缺乏足够深度。模型能力越强 → 输出越趋同 → 多样性降低 → test-time scaling 收益递减——这一观察在文献中已有隐含讨论（Snell et al. 2025, Brown et al. 2024）。Proposition 1 基于 pair-wise independence 假设，而 split-half reliability 仅 r≈0.578-0.644。\n\n### Should-Fix 问题\n\n**W1** 正文可能超出 8 页限制（Conclusion 溢出到 Page 9）。\n\n**W2** 与 Yun & Price (2025) 的差异化论述不够充分——\"signal alignment collapse\" 与 \"format diversity collapse\" 语义高度重叠。\n\n**W3** 相关工作缺少重要领域：conformal prediction for NLP、token-level uncertainty decomposition、active learning for structured prediction、MBR with structural utility。\n\n**W4** 诊断 cascade 的方法论价值需要更多验证——仅在 NER 上验证，cascade 阈值（degeneracy >30%, α<0.05）是否 task-specific 未讨论。\n\n**W5** Proposition 1 的独立性假设与实际数据不符——Table 31 中 bound ratio 仅 0.13-0.63，理论 bound 至少松弛了 37%。\n\n### 主要优势\n\n1. 问题定义精准且有价值\n2. 实验方法论严谨（3-seed、bootstrap CI、Holm-Bonferroni k=57）\n3. Correlation-selection gap 是真正的 empirical contribution\n4. 诚实报告（未过度渲染 bypass 策略效果）\n5. 47 页附录的 exhaustive validation\n\n### Findings vs. Main Conference 定位\n\n倾向 3.5 (Borderline Conference)。支持 Conference：correlation-selection gap 有用、诊断框架有方法论价值、实验方法论高标准。倾向 Findings：核心贡献是诊断性的、任务范围过窄、capability-diversity tension 新颖性增量有限、理论贡献偏薄。\n\n---\n\n请逐条回应上述所有 Must-Fix 和 Should-Fix 问题。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Must-Fix、Should-Fix 和主要论点，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 完整审稿意见\n\n**Overall**: 3.5 (Borderline Conference)\n**一句话总结**: 扎实的经验性诊断工作，\"correlation-selection gap\"是有价值的发现，但任务范围局限于 NER、理论贡献偏薄、且部分 claim 超出了实验证据的支撑范围，处于 Conference 和 Findings 的边界。\n\n### Must-Fix 问题\n\n**N1** [critical] Scope overclaim：标题和 Abstract 声称研究 \"structured prediction\" 的 boundary conditions，但实验覆盖几乎仅限 NER + 极初步的 RE 扩展。NER 的 entity-set 输出结构与 dependency parsing、SRL、event extraction 差异巨大。RE 扩展过于初步（仅 SciERC 一个数据集），不足以支撑泛化 claim。\n\n**N2** [critical] Capability-diversity tension 作为 central finding 缺乏足够深度。模型能力越强 → 输出越趋同 → 多样性降低 → test-time scaling 收益递减——这一观察在文献中已有隐含讨论（Snell et al. 2025, Brown et al. 2024）。Proposition 1 基于 pair-wise independence 假设，而 split-half reliability 仅 r≈0.578-0.644。\n\n### Should-Fix 问题\n\n**W1** 正文可能超出 8 页限制（Conclusion 溢出到 Page 9）。\n\n**W2** 与 Yun & Price (2025) 的差异化论述不够充分——\"signal alignment collapse\" 与 \"format diversity collapse\" 语义高度重叠。\n\n**W3** 相关工作缺少重要领域：conformal prediction for NLP、token-level uncertainty decomposition、active learning for structured prediction、MBR with structural utility。\n\n**W4** 诊断 cascade 的方法论价值需要更多验证——仅在 NER 上验证，cascade 阈值（degeneracy >30%, α<0.05）是否 task-specific 未讨论。\n\n**W5** Proposition 1 的独立性假设与实际数据不符——Table 31 中 bound ratio 仅 0.13-0.63，理论 bound 至少松弛了 37%。\n\n### 主要优势\n\n1. 问题定义精准且有价值\n2. 实验方法论严谨（3-seed、bootstrap CI、Holm-Bonferroni k=57）\n3. Correlation-selection gap 是真正的 empirical contribution\n4. 诚实报告（未过度渲染 bypass 策略效果）\n5. 47 页附录的 exhaustive validation\n\n### Findings vs. Main Conference 定位\n\n倾向 3.5 (Borderline Conference)。支持 Conference：correlation-selection gap 有用、诊断框架有方法论价值、实验方法论高标准。倾向 Findings：核心贡献是诊断性的、任务范围过窄、capability-diversity tension 新颖性增量有限、理论贡献偏薄。\n\n---\n\n请逐条回应上述所有 Must-Fix 和 Should-Fix 问题。"
  }
}
```

</details>

---


### Tool result

_source line 3777 · 2026-05-22T10:22:55.810163+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 29187
}
```

</details>

---


### Tool call

_source line 3778 · 2026-05-22T10:22:59.629416+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Must-Fix、Should-Fix 和主要论点，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 完整审稿意见\n\n**Overall**: 3.5 (Borderline Conference)\n**一句话总结**: 在 NER 上对 test-time scaling 失败条件进行了统计严谨的实证分析，提出了有用的诊断框架，但\"结构化预测\"的广泛声明超出了实际证据范围（主要是 NER），且 SciERC 单 seed 是统计弱点。\n\n### Must-Fix 问题\n\n**N1** [critical] Title/Scope 与实际证据不匹配：\"Structured Prediction\" vs. 实际主要是 NER。标题声称研究\"structured prediction\"的 boundary conditions，但充分实验的只有 NER（4 数据集 × 2 模型家族）。RE 仅 SciERC 上的 exploratory extension（397 实例，1 模型），SQL 仅一句话提及。Discussion 承认\"generalization to other structured tasks requires further investigation\"。建议将标题限定为 NER 或补充完整的非 NER 任务分析。\n\n**N2** [critical] SciERC 仅 1 个 seed 构成统计可靠性威胁。SciERC 是最核心的数据集（分析最详尽、degeneracy 最低、headroom 最大），但仅用 1 个 training seed（seed=42），测试集仅 529 实例。论文自承 σ=0.48pp。许多核心发现（Figure 2、LP compression、entity probes）以 SciERC 为 primary showcase。MDE 分析显示 n=23 下仅能检测 ρ≥0.5 的效应。\n\n### Should-Fix 问题\n\n**W1** Diagnostic cascade 的理论基础依赖 entity independence 假设。Proposition 1 假设 entity-wise independence，但结构化预测的关键特征恰恰是实体间有依赖。论文报告 correlation 3-12% 但未量化对 bound 的影响。\n\n**W2** 9 种方法对比的公平性问题。Cross-model SC 计算量翻倍、Multi-round MRC 需多轮 prompting，与 N=8 的 LP/SJ/FK 不是等计算预算比较。Table 65 部分解决但主文 Table 2 呈现方式可能误导。\n\n**W3** Greedy baseline 可能低估 test-time scaling 潜力。Greedy (T=0) 本身是\"最佳单样本\"策略。应补充 random single sample at T=1.0 作为额外 baseline。\n\n**W4** Capability-diversity tension 是核心发现但缺乏形式化。没有可测量定义，Figure 3 仅展示 3 数据集的 MV ΔF1 趋势，且 CoNLL N=64 时 MV gain 为正。\n\n**W5** Free-form decoding ablation 仅覆盖 SciERC + CoNLL，Few-NERD（degeneracy 最低）和 WNUT-17 未覆盖。\n\n### 小问题\n- Figure 2 双量纲共轴混淆\n- SJ 引用 Fleiss 1971 可能有误\n- Table 5 术语不一致（Soft Jaccard vs. structural similarity）\n- Proposition 2 Remark 未解释 v=1 选择\n- Table 4 caption 与内容不匹配\n- Ethics Statement 未讨论 adversarial dual-use\n\n### 主要优势\n1. 统计方法论显著超越同行（Holm-Bonferroni k=57、MDE、TOST equivalence testing）\n2. Diagnostic cascade 概念清晰且实用\n3. 47 页消融和 robustness 分析\n4. Failure mode gallery 有教学价值\n5. 诚实讨论 limitations\n6. Correlation-selection gap 是有价值的概念贡献\n\n---\n\n请逐条回应上述所有 Must-Fix 和 Should-Fix 问题。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每个 Must-Fix、Should-Fix 和主要论点，标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 1 完整审稿意见\n\n**Overall**: 3.5 (Borderline Conference)\n**一句话总结**: 在 NER 上对 test-time scaling 失败条件进行了统计严谨的实证分析，提出了有用的诊断框架，但\"结构化预测\"的广泛声明超出了实际证据范围（主要是 NER），且 SciERC 单 seed 是统计弱点。\n\n### Must-Fix 问题\n\n**N1** [critical] Title/Scope 与实际证据不匹配：\"Structured Prediction\" vs. 实际主要是 NER。标题声称研究\"structured prediction\"的 boundary conditions，但充分实验的只有 NER（4 数据集 × 2 模型家族）。RE 仅 SciERC 上的 exploratory extension（397 实例，1 模型），SQL 仅一句话提及。Discussion 承认\"generalization to other structured tasks requires further investigation\"。建议将标题限定为 NER 或补充完整的非 NER 任务分析。\n\n**N2** [critical] SciERC 仅 1 个 seed 构成统计可靠性威胁。SciERC 是最核心的数据集（分析最详尽、degeneracy 最低、headroom 最大），但仅用 1 个 training seed（seed=42），测试集仅 529 实例。论文自承 σ=0.48pp。许多核心发现（Figure 2、LP compression、entity probes）以 SciERC 为 primary showcase。MDE 分析显示 n=23 下仅能检测 ρ≥0.5 的效应。\n\n### Should-Fix 问题\n\n**W1** Diagnostic cascade 的理论基础依赖 entity independence 假设。Proposition 1 假设 entity-wise independence，但结构化预测的关键特征恰恰是实体间有依赖。论文报告 correlation 3-12% 但未量化对 bound 的影响。\n\n**W2** 9 种方法对比的公平性问题。Cross-model SC 计算量翻倍、Multi-round MRC 需多轮 prompting，与 N=8 的 LP/SJ/FK 不是等计算预算比较。Table 65 部分解决但主文 Table 2 呈现方式可能误导。\n\n**W3** Greedy baseline 可能低估 test-time scaling 潜力。Greedy (T=0) 本身是\"最佳单样本\"策略。应补充 random single sample at T=1.0 作为额外 baseline。\n\n**W4** Capability-diversity tension 是核心发现但缺乏形式化。没有可测量定义，Figure 3 仅展示 3 数据集的 MV ΔF1 趋势，且 CoNLL N=64 时 MV gain 为正。\n\n**W5** Free-form decoding ablation 仅覆盖 SciERC + CoNLL，Few-NERD（degeneracy 最低）和 WNUT-17 未覆盖。\n\n### 小问题\n- Figure 2 双量纲共轴混淆\n- SJ 引用 Fleiss 1971 可能有误\n- Table 5 术语不一致（Soft Jaccard vs. structural similarity）\n- Proposition 2 Remark 未解释 v=1 选择\n- Table 4 caption 与内容不匹配\n- Ethics Statement 未讨论 adversarial dual-use\n\n### 主要优势\n1. 统计方法论显著超越同行（Holm-Bonferroni k=57、MDE、TOST equivalence testing）\n2. Diagnostic cascade 概念清晰且实用\n3. 47 页消融和 robustness 分析\n4. Failure mode gallery 有教学价值\n5. 诚实讨论 limitations\n6. Correlation-selection gap 是有价值的概念贡献\n\n---\n\n请逐条回应上述所有 Must-Fix 和 Should-Fix 问题。"
  }
}
```

</details>

---


### Tool result

_source line 3779 · 2026-05-22T10:23:01.292997+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1663
}
```

</details>

---


### Assistant

_source line 3780 · 2026-05-22T10:23:03.996373+00:00_

交叉分享已发出，等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 281

## Round 281

2 recorded events


### User

_source line 3781 · 2026-05-22T10:23:06.759039+00:00_

[Reviewer 2 审稿结果]:
审稿完成。已向 Review Director 提交完整审稿意见，核心结论：

- **Overall: 3.5 (Borderline Conference)**
- **2 个 Must-Fix**：(1) scope overclaim——标题声称 "structured prediction" 但仅验证 NER；(2) capability-diversity tension 作为 central finding 新颖性增量有限
- **5 个 Should-Fix**：页数可能超 8 页、与 Yun & Price (2025) 差异化不足、相关工作缺 conformal prediction/MBR/active learning 等领域、诊断 cascade 泛化性未验证、Proposition 1 的 bound 过松
- **主要优势**：correlation-selection gap 是真正有价值的经验发现、实验统计方法论严谨（Holm-Bonferroni, bootstrap CI, TOST）、47 页附录体现极致 thoroughness

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 3782 · 2026-05-22T10:23:12.120793+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 282

## Round 282

2 recorded events


### User

_source line 3783 · 2026-05-22T10:24:42.022165+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 对 Reviewer 1 审稿意见的逐条回应

---

### Must-Fix 问题

**[AGREE] R1-N1: Title/Scope 与实际证据不匹配**

完全同意。这与我的 N1 一致。论文标题 "Boundary Conditions for Structured Prediction" 设定了远超实验覆盖的期望。NER（无序 entity set）、RE（三元组集合）、dependency parsing（有向树）、event extraction（嵌套结构）的输出空间结构差异巨大，degeneracy 和 alignment collapse 的表现形式可能完全不同。RE 扩展（Appendix o, §6.3）仅涉及 SciERC 单数据集的 LP 结果（Table 45），远不足以支撑泛化。SQL 更只是一句话提及。

补充我的观察：论文 Conclusion（§9, Page 8-9）自身承认 "generalization to other structured tasks requires further investigation"，这与标题的强 claim 形成内在矛盾。建议与 R1 一致——限缩标题为 NER/IE 或补充实验。

---

**[AGREE] R1-N2: SciERC 单 seed 统计可靠性问题，但严重程度需限定**

同意这是一个方法论弱点，但我认为严重程度略低于 R1 的判断。理由：

(a) **同意的部分**：SciERC 确实是论文中分析最详尽的数据集——Figure 2 的 LP compression 分析、entity-level probe（§h.1）、calibration analysis（Appendix e, Figure 6）、free-form decoding ablation（Appendix q）都以 SciERC 为 primary showcase。单 seed（seed=42）+ 529 test instances 的 power 确实有限。MDE 分析（Appendix ab3）坦诚报告了 n=23 下仅能检测 ρ≥0.5 的效应，这意味着 medium-size effects 可能被遗漏。

(b) **部分缓解**：论文提供了 split-half reliability（Table 7, SciERC r=0.309-0.395），instance-level FK permutation test（Table 12, k=57 项检验中 SciERC 的 p-values），以及 TOST equivalence testing（Table 15）。这些测试部分弥补了单 seed 的限制，但不能替代多 seed 的 training variance 估计。

(c) **关键问题**：论文为 Few-NERD 和 CoNLL 使用了 3 seeds（§7.1），但 SciERC 为何只用 1 seed 未给出解释。如果是资源限制，应明确说明。如果 SciERC 的核心发现（如 LP compression ratio、degeneracy 作为 strongest predictor）在另外 2 个 seed 上不稳定，会动摇论文的多项结论。

建议：将此作为 Must-Fix 但允许在 camera-ready 中补充 SciERC 2-3 seeds（训练成本应可控，SciERC 仅 1861 train sentences），而非阻挡论文。

---

### Should-Fix 问题

**[REBUT] R1-W2: 9 种方法对比的公平性问题**

R1 指出 cross-model SC 计算量翻倍、multi-round MRC 需多轮 prompting，与 N=8 的 LP/SJ/FK 不是等计算预算比较。我认为这个担忧被论文已有内容部分化解：

(a) 论文的核心论点不是 "哪种方法在等预算下最好"，而是 "selection 本身是否能显著超越 greedy"。Table 2 的 key message 是：**所有 9 种方法的 gain 都很小**（< 1pp over greedy on most datasets），包括计算量更大的方法。如果更多计算都无法解锁显著增益，这恰恰强化了 correlation-selection gap 的论点。

(b) Table 4（Instance degeneracy vs. LP selection gain, 23 configurations）控制了 N、seed 和数据集，展示 degeneracy 而非 compute 是 selection 失败的主要 predictor（ρ=-0.881）。

(c) 论文 §5 明确将 cross-model SC 和 entity-level construction 定位为 "exploratory bypasses"，不是作为等预算下的公平替代方案。

但 R1 的一个合理子点是：Table 2 的呈现方式可能让读者误以为这是一个 method comparison table——建议在 caption 中添加 compute budget 注释。

---

**[AGREE] R1-W1: Proposition 1 的 entity independence 假设**

同意，这与我的 W5 一致。补充证据：论文自身报告的 split-half reliability r=0.578-0.644（Table 7）说明 entity-level 信号在同一 instance 内是 positively correlated 的，违反了 independence 假设。Table 31 显示 actual/bound ratio 为 0.13-0.63，证实 bound 过松。建议作者提供 correlated entity 的 tighter bound 或明确降格 Proposition 1 为 illustrative upper bound。

---

**[REBUT] R1-W3: Greedy baseline 可能低估 test-time scaling 潜力**

不同意。R1 建议增加 random single sample at T=1.0 作为额外 baseline，理由是 greedy 是 "最佳单样本" 策略，可能低估 scaling 潜力。

(a) **Greedy 是正确的比较基准**：test-time scaling 的标准问题设定是 "给定更多 compute budget（N samples），能否超越最佳单次推理？"——Snell et al. (2025, ICLR)、Wang et al. (2023)、Brown et al. (2024) 全部使用 greedy/argmax 作为 baseline。使用更弱的 random baseline 反而会 inflate scaling gains，掩盖论文要揭示的核心问题。

(b) **论文已提供 random baseline 数据**：Appendix t 的 N-scaling analysis（Table 38）报告了 N=1 at T=1.0 vs. greedy 的对比。Few-NERD N=1 T=1.0 的 F1 低于 greedy 约 2pp，CoNLL 差异更小。所以 "diversity tax" 的信息已经可以从论文中提取。

(c) **使用 random baseline 会误导读者**：如果 MV at N=8 对比 random-at-T=1.0 显示 +2pp gain，读者可能误以为 test-time scaling 有效——但这 2pp 中大部分只是 sampling noise 的恢复（回到 greedy 水平），不是真正的 scaling gain。

---

**[AGREE] R1-W4: Capability-diversity tension 缺乏形式化**

同意，这与我的 N2 一致。Figure 3 仅展示了 3 个数据集（SciERC、CoNLL、Few-NERD）的 MV ΔF1 趋势，CoNLL 在 N=64 时 MV gain 仍为正（约 +0.6pp），这直接反例了 "tension" 的叙事。论文需要：(a) 给出 capability-diversity tension 的可操作定义（如 degeneracy rate vs. base F1 的函数关系）；(b) 解释 CoNLL N=64 的正 gain 为何不构成反例。

---

**[AGREE] R1-W5: Free-form decoding ablation覆盖不全**

同意。Appendix q（Table 33）的 free-form decoding ablation 仅覆盖 SciERC（N=8, 4-seed RE）和 CoNLL（4-seed RE, 22 configurations）。Few-NERD 是 degeneracy 最低的数据集（12%），恰恰是 constrained decoding 效果应最小的场景——如果 free-form decoding 在 Few-NERD 上也未带来显著改善，这会强化论文的 degeneracy-是-根本原因的论点。缺少这个验证是一个遗漏。WNUT-17 作为社交媒体域的数据集也值得覆盖，以测试格式约束在 noise 环境中的影响。

---

### 小问题回应

**[AGREE] Figure 2 双量纲共轴**：同意可读性问题。左轴 AUROC 和右轴 ρ 的 scale 不同（0-1 vs. -1 to 1），且 AUROC=0.82 和 ρ=0.39 的视觉位置接近，容易误读为相似水平的效果。

**[AGREE] SJ 引用 Fleiss 1971 可能有误**：Fleiss (1971) "Measuring nominal scale agreement among raters" 是 inter-rater reliability（Cohen's kappa 的多 rater 推广），不是 Soft Jaccard 的原始来源。如果 SJ 指 Soft Jaccard similarity，引用应为 jaccard 相关文献。如果 SJ 指 Fleiss' kappa 的变体，论文应说明连接。

**[AGREE] Table 5 术语不一致**：论文中 SJ 有时称 "Soft Jaccard"（§3），有时称 "structural similarity"（Table 5），应统一。

**[REBUT] Ethics Statement 未讨论 adversarial dual-use**：论文研究的是 NER 质量估计信号的诊断，不涉及对抗性攻击或有 dual-use 风险的技术。Ethics Statement 已讨论了 "risk of deploying unreliable confidence-based selection in production systems"（Page 10），这是最相关的伦理考虑。要求 NER 诊断论文讨论 adversarial dual-use 不太合理。

**[AGREE] Proposition 2 Remark 未解释 v=1**：有效的可读性问题，但影响不大。

**[AGREE] Table 4 caption 与内容不匹配**：如果 caption 说 "instance degeneracy vs. LP selection gain" 但表格包含更多列，应修正。

---

### 对 R1 主要优势的补充

R1 列出的 6 项优势与我的评估高度一致。我特别同意以下两点的 weighting：

1. **统计方法论（Holm-Bonferroni k=57, MDE, TOST）**：这是论文最突出的优势之一，远超 NLP 经验性论文的平均水平。
2. **Correlation-selection gap 作为概念贡献**：R1 和我都认为这是论文最有价值的 finding——它命名了一个此前未被清晰表述的现象。

---

### 与 R1 评分的分歧和共识

**共识**：Overall 3.5 (Borderline Conference)。R1 和我的核心判断一致——扎实的经验性工作，有用的诊断框架，但 scope overclaim 和部分方法论弱点使其处于 Conference/Findings 边界。

**分歧点**：
- R1 将 SciERC 单 seed 列为 critical Must-Fix，我认为严重程度略低（should-fix + camera-ready 可补），因为论文的核心结论（correlation-selection gap）主要由 3-seed 的 Few-NERD 和 CoNLL 支撑，SciERC 更多是补充验证。
- R1 对 W3（greedy baseline）的担忧我不同意——greedy 是 test-time scaling 文献的标准 baseline。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 3784 · 2026-05-22T10:24:48.010346+00:00_

Reviewer 2 交叉回应已收到。等待 Reviewer 1 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 283

## Round 283

2 recorded events


### User

_source line 3785 · 2026-05-22T10:24:50.860820+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。总结：

- **AGREE**: R1-N1（scope overclaim）、R1-N2（SciERC 单 seed，但严重程度稍低）、R1-W1（independence 假设）、R1-W4（capability-diversity 缺形式化）、R1-W5（free-form ablation 覆盖不全）
- **REBUT**: R1-W2（方法对比公平性——论文论点是 "所有方法都 gain 小"，不是 iso-compute 竞赛）、R1-W3（greedy baseline——是 test-time scaling 标准基准，random baseline 反而会 inflate gains）
- **分歧**：SciERC 单 seed 我认为 should-fix 而非 critical must-fix，核心结论由 3-seed 的 Few-NERD/CoNLL 支撑

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 3786 · 2026-05-22T10:24:56.492544+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 284

## Round 284

14 recorded events


### User

_source line 3787 · 2026-05-22T10:25:47.078869+00:00_

[Reviewer 1 审稿意见]:

## Reviewer 1 对 Reviewer 2 审稿意见的逐条回应

---

### Must-Fix 问题

**[AGREE] R2-N1: Scope overclaim — "structured prediction" 标题 vs. 主要 NER 实验**

完全同意，这与我自己的 N1 一致。补充几点：

1. 论文自身在 p.9 Limitations 中承认 "Scope: structured IE (NER primary, RE and SQL exploratory). English only, open-weight (Qwen and LLaMA) and closed-source (GPT-5.5) families"。RE 扩展仅在 Appendix o (p.29) 用 Qwen3-8B 1 个模型做了 SciERC RE（397 full-set 实例），且结果本身很弱——40% RE 实例 zero F1, degeneracy 87.2%（Section 4, p.4），这使得 diagnostic cascade 的大部分阶段在 RE 上无法有效运行。
2. NER 的 entity-set 输出结构（无序集合、可部分匹配）与 dependency parsing（树结构、全局约束）、SRL（predicate-argument 结构）、event extraction（触发词+论元+角色）差异显著。论文的 Proposition 1 (p.31) 基于 entity-wise independence 推导，这一假设在树结构或图结构输出中完全不成立。
3. 修改建议应采取我 N1 中提出的方案：限定标题为 NER（如 "Boundary Conditions for Entity Recognition"），或补充至少一个完整的非 NER task 分析。

**[REBUT] R2-N2: Capability-diversity tension 缺乏深度 / 文献已有隐含讨论**

部分反驳，理由如下：

1. **新颖性方面**：R2 声称 Snell et al. (2025) 和 Brown et al. (2024) 已有"隐含讨论"，但这两篇关注的是 discrete-answer reasoning（数学、选择题），未涉及 structured output 的特殊问题——entity-level degeneracy、partial-match F1 下的 aggregation failure、LP compression。本文的贡献不是发现"stronger models → less diversity"这一泛化趋势（确实已知），而是在 NER 上量化了具体的断裂机制：degeneracy 12-68%（Table 1, p.4）、oracle headroom 仅 +1.5pp 但 selection 无法实现（Table 2, p.5）、LP 分布压缩到 <1pp intra-instance range（Section 4, p.4）。这些 structured-output-specific 的量化是新的。

2. **但我同意形式化不足**：正如我在 W4 中指出的，"capability-diversity tension"被呈现为 central finding（Section 9, p.8）但缺乏可操作的定义。论文未提供一个可测量的指标来刻画"在什么 capability 水平下 scaling returns 开始 diminish"。Figure 3 (p.6) 的 N-scaling curves 是有用的，但不够。

3. **关于 Proposition 1 和 split-half reliability**：R2 将这两点并列但它们衡量不同层面。Split-half r≈0.578-0.644 来自 Table 7 (p.15) 的 FK score 稳定性测试，反映的是 FK 这一特定信号的 within-instance stability，与 Proposition 1 的 entity independence 假设是不同的问题。Proposition 1 的问题在于 bound looseness（我的 W1 也提到），而非 split-half reliability。

**综合判断**：R2-N2 中 "文献已有" 的论断过强，但 "形式化不足" 的批评成立。建议降级为 Should-Fix 而非 Must-Fix——capability-diversity tension 作为 empirical observation 有价值，但不应被 framed 为论文的 "central finding"。

---

### Should-Fix 问题

**[REBUT] R2-W1: 正文可能超出 8 页限制**

经仔细检查 p.8-9，Section 9 "Discussion and Conclusion" 确实从 p.8 下半部分延伸到 p.9 上部约 15-20 行，然后 "Limitations" 才开始。按 EMNLP 2026 规则，Limitations 和 Ethics 不计入 8 页限制，但 Discussion/Conclusion 属于正文。

**更正：经核实，我改为 [AGREE]。** Section 9 的结论段落（"Conclusion. We characterize when test-time compute scaling fails..."）出现在 p.9 顶部，明确超出了 8 页正文限制。这是一个格式合规问题，需要压缩 Section 8 (Related Work) 或 Section 9 (Discussion and Conclusion) 以确保正文在 p.8 内完结。R2 的观察是准确的。

**[AGREE] R2-W2: 与 Yun & Price (2025) 的差异化不足**

合理关切。Section 8 (p.8) 提到 "Consistency for structured IE" 并引用了多篇相关工作，但我注意到论文的 "signal alignment collapse" 概念（Section 4: alignment collapse (α→0)）确实与 output diversity collapse 在语义上高度相关。如果 Yun & Price (2025) 已经讨论了 format diversity 在 structured outputs 上的坍缩，论文需要明确说明自己的诊断框架如何超越 diversity collapse 的描述——关键差异应该是本文提供了四阶段 cascade 的定量诊断（不仅观察到坍缩，还分析了坍缩在哪个阶段发生、为什么发生），这一点需要更显式地论述。

**[AGREE partially] R2-W3: 相关工作缺少重要领域**

部分同意。R2 列举的四个领域中：

- **MBR with structural utility**：论文实际上在 Section 8 (p.8) 和 Proposition 2 (Appendix p.2, p.30) 中讨论了 MBR connection，指出 "Our selection instantiates MBR decoding (Eikema and Aziz, 2022)" 并证明了在 entity-wise independence 下 MBR-optimal 集合即为 majority-vote threshold 之上的实体。这一点 R2 可能遗漏了。
- **Conformal prediction for NLP**：有效的遗漏——conformal prediction 提供了另一种不依赖 quality estimation 的 selection/abstention 框架，且在 NER 上有近期工作（如 uncertainty sets for structured outputs）。至少应在 Related Work 中提及并讨论为何不采用。
- **Token-level uncertainty decomposition**：与本文的 entity-level LP decomposition（Section m, p.28）直接相关，确实应该讨论。
- **Active learning for structured prediction**：关联较弱。本文关注 inference-time selection，与 training-time data selection 问题不同。可以不讨论。

**[AGREE] R2-W4: Diagnostic cascade 阈值的 task-specificity**

完全同意，这是我在 Round 1 审查中未充分注意到的一个问题。论文使用的诊断阈值如 degeneracy >30%（p.5, Section 6.1: "we select τ=0.05 at the elbow of the compression curve"）、α<0.05 for equivalence testing（Table 15-16, p.19-20），以及 AUROC >0.6 作为 "moderate" quality estimation 的标准（Section 3, p.3），都未讨论这些阈值在不同 task 上是否稳定。考虑到论文已经观察到 task-specific 差异很大（如 SciERC degeneracy 30% vs. WNUT-17 51%，CoNLL RE zero F1 rate 40%），cascade 的通用性需要更多论证。

**[REBUT] R2-W5: Proposition 1 独立性假设——bound ratio 0.13-0.63 并非严重问题**

R2 认为 Table 31 中 bound ratio 0.13-0.63 表明理论 bound "至少松弛了 37%"，因此独立性假设是严重缺陷。但这一解读过于严苛，理由如下：

1. **Proposition 1 的目的是方向性的**（directional），不是为了给出 tight bound。论文在 Remark (p.31) 中明确说明："We use balanced linear utility (v=1). We use balanced F1 as a closed approximation when |E_i| is small (typically 5-15 in our experiments)." 目标是建立 "marginal-entity precision 必须超过某个 threshold 才能使 MV gain structurally impossible" 这一定性结论。

2. **即使 bound 松弛，定性结论仍然成立**。Table 32 (p.31) 的 empirical validation 显示：MV does not improve F1 on any dataset when degeneracy 在 ≥50% 时，这与 Proposition 1 的预测方向一致。bound 的松弛不改变"高 degeneracy → MV 无法改善"这一核心推论。

3. **但我承认松弛程度应更透明**。论文应在 Proposition 1 之后添加一段量化讨论：在 3-12% entity correlation 下，bound 偏移多少？这是一个可以轻松补充的 robustness check。

---

### 对 R2 Findings vs. Conference 定位的评论

R2 倾向 3.5 (Borderline Conference)，我给出了相同分数。

**共识点**：
- Correlation-selection gap 是一个 genuine empirical contribution
- 统计方法论在 NLP 论文中属于上乘
- 但 scope overclaim（NER vs. "structured prediction"）和理论深度不足是 Conference 级别的主要障碍

**我与 R2 的分歧**：
- R2 认为 capability-diversity tension "文献已有隐含讨论"，我认为在 structured outputs 的量化分析上是新的——但确实形式化不足，不足以支撑 "central finding" 的 framing
- R2 将 Proposition 1 的 bound looseness 视为 Must-Fix 级别问题（嵌入在 N2 中），我认为这是 Should-Fix——Proposition 提供的是定性方向性指导，不是工程公式

**最终倾向**：维持 3.5 (Borderline Conference)。如果作者能 (a) 修正标题 scope、(b) 补充 SciERC 多 seed、(c) 压缩正文至 8 页内，该论文可达 Conference 水平。当前版本适合 Findings。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 3788 · 2026-05-22T10:26:16.387317+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '完成资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.7: 派发视觉审查', 'status': 'completed', 'activeForm': '派发视觉审查 Agent'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': '收集 Reviewer 审稿意见'}, {'content': 'Step 2: 交叉分享', 'status': 'completed', 'activeForm': '完成交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'completed', 'activeForm': '判断收敛'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'in_progress', 'activeForm': '汇总并投递审稿报告'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '完成资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.7: 派发视觉审查', 'status': 'completed', 'activeForm': '派发视觉审查 Agent'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': '收集 Reviewer 审稿意见'}, {'content': 'Step 2: 交叉分享', 'status': 'completed', 'activeForm': '完成交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'completed', 'activeForm': '判断收敛'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'in_progress', 'activeForm': '汇总并投递审稿报告'}]"
  }
}
```

</details>

---


### Tool result

_source line 3789 · 2026-05-22T10:26:16.438117+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "TodoWrite",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 3790 · 2026-05-22T10:26:20.554097+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 3791 · 2026-05-22T10:26:21.708956+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-22T10:14:51.152967+00:00\", \"completed_at\": \"2026-05-22T10:19:07.060207+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 24\", \"message\": \"附录页面约 2/3 空白——Appendix n 节结尾仅占页面上部 ~1/3，下方全空。建议将后续 Appendix 内容提前或调整 LaTeX float/section break，避免整页浪费。\"}, {\"severity\": \"warning\", \"dimension\": \"page 17\", \"message\": \"Figure 7 质量估计热力图使用红→绿色阶，对红绿色盲用户不友好。建议改用 viridis 或 Blue→Orange 色阶。单元格内已印数值（辅助可读），但色盲审稿人仍可能提出意见。\"}, {\"severity\": \"warning\", \"dimension\": \"page 16\", \"message\": \"Figure 6 可靠性校准图同样使用绿→红色阶，与 Figure 7 存在相同的色盲友好性问题。\"}, {\"severity\": \"warning\", \"dimension\": \"page 7\", \"message\": \"主文单页密度极高（Table 3 + Table 4 + Figure 4 + 两个 section 的文字），视觉上略显拥挤。功能上无问题，但审稿人可能感觉 overwhelming。\"}, {\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"首页无视觉锚点。Figure 1 出现在 Page 2 顶部，延迟仅 1 页，对审稿人第一印象影响可控。若 Introduction 能缩短半栏使 Figure 1 上提到 Page 1 底部则更佳，但非必须。\"}, {\"severity\": \"info\", \"dimension\": \"page 3\", \"message\": \"主文唯一纯文本页（五种 confidence signal 的描述）。内容为方法论定义，纯文本合理；但若能加一个小型 signal summary 表（名称 / 类型 / 是否 per-sample）会改善可浏览性。\"}, {\"severity\": \"info\", \"dimension\": \"pages 14-47\", \"message\": \"附录共 34 页，内容极为详尽（~44 张表 + ~6 张图 + 数学证明 + failure mode gallery）。全面性值得肯定，但审稿人可能选择性跳读。关键附录（如 Appendix a 的 Notation 表、Appendix ag 的 Failure Mode Gallery）建议在主文中显式指引。\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Table 2（9 类方法汇总）跨全宽，信息密度高。表内使用了脚注标记区分配置差异，格式正确。部分列标题字号偏小但仍可读。\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Figure 3 线图使用 3 色区分数据集（绿/橙/蓝），色彩区分度良好且色盲友好。\"}, {\"severity\": \"info\", \"dimension\": \"page 47\", \"message\": \"最末页（Failure Mode Gallery）内容填满约 85% 页面，空间利用合理。\"}], \"counts\": {\"critical\": 0, \"warning\": 4, \"info\": 6}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 1154
}
```

</details>

---


### Tool call

_source line 3792 · 2026-05-22T10:26:21.709470+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 3793 · 2026-05-22T10:26:21.762584+00:00_

1	issues:
2	- id: R1-N1
3	  summary: "θ_crit=0.70 阈值缺乏 held-out 验证"
4	  category: method
5	  severity: warning
6	  status: in_progress
7	  first_raised_round: 33
8	  last_seen_round: 34
9	  mentions:
10	    - round: 33
11	      reviewers: [1]
12	      note: "R1 认为 Must-Fix（post-hoc fitting 风险）；R2 反驳称有 Corollary 1 理论支撑，降级为 Should-Fix。共识：理论基础 sound 但缺 held-out validation 和 sensitivity sweep。"
13	    - round: 34
14	      reviewers: [1, 2]
15	      note: "R1 再次列为 Must-Fix (N2)；R2 同意需要澄清但建议降级为 Should-Fix，认为 θ_crit 更像描述性发现而非模型参数。共识：需明确定位（descriptive vs normative）并报告 sensitivity/LOO-CV。"
16	  action_items:
17	    - round: 33
18	      action: "Agent CPU: sweep θ∈{0.60,0.65,0.70,0.75,0.80}，检查 Table 31 结论稳定性；在 RE 上验证"
19	      assigned_to: agent
20	      status: in_progress
21	  resolution: ""
22	  resolution_round: null
23	
24	- id: R1-N3
25	  summary: "Entity construction 作为 prescriptive contribution 证据不足"
26	  category: experiment
27	  severity: warning
28	  status: in_progress
29	  first_raised_round: 33
30	  last_seen_round: 34
31	  mentions:
32	    - round: 33
33	      reviewers: [1, 2]
34	      note: "双方共识：(a) 阈值 k per-dataset 优化无部署策略；(b) Holm-Bonferroni 全局校正后多数 construction 结果不显著；(c) CoNLL 无增益。"
35	    - round: 34
36	      reviewers: [1, 2]
37	      note: "双方 AGREE prescriptive arm 薄弱。R1-W3 指出 Abstract prescriptive 口吻与 Section 7.5 exploratory 标记矛盾。R2-N2 认为三阶段叙事 Prescribe 阶段不完整。共识：应降级为 exploratory with promising but inconsistent initial results。"
38	  action_items:
39	    - round: 33
40	      action: "Paper Agent: 降级 construction 为 exploratory result；加 Xie et al. (2023) 对比；§7.5 加 k deployment note"
41	      assigned_to: paper_agent
42	      status: in_progress
43	  resolution: ""
44	  resolution_round: null
45	
46	- id: R2-W1
47	  summary: "Entity-level construction 与 Xie et al. (2023) 差异不清晰"
48	  category: framing
49	  severity: warning
50	  status: in_progress
51	  first_raised_round: 33
52	  last_seen_round: 34
53	  mentions:
54	    - round: 33
55	      reviewers: [
…[truncated 10404 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 53
}
```

</details>

---


### Tool call

_source line 3794 · 2026-05-22T10:28:17.108610+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "struct_self_consist_ie",
  "issues_yaml": "issues:\n# ===== CRITICAL / MUST-FIX =====\n- id: R35-N1\n  summary: \"Scope overclaim: 标题声称 'structured prediction' 但证据主要是 NER\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 33\n  last_seen_round: 35\n  mentions:\n    - round: 33\n      reviewers: [1, 2]\n      note: \"R1-W4: RE/SQL 覆盖有限。当时为 warning。\"\n    - round: 34\n      reviewers: [1, 2]\n      note: \"继续作为 warning。\"\n    - round: 35\n      reviewers: [1, 2]\n      note: \"双方升级为 Critical Must-Fix。标题 'Boundary Conditions for Structured Prediction' 但充分实验仅 NER（4 数据集 × 2 模型家族）。RE 仅 SciERC 单数据集 exploratory（397 实例，1 模型），SQL 仅一句话。NER entity-set 与 parsing/SRL/event extraction 输出结构差异巨大。Discussion 自承 'generalization to other structured tasks requires further investigation'，与标题矛盾。\"\n  action_items:\n    - round: 35\n      action: \"限缩标题为 NER/IE（如 'Boundary Conditions for Entity Recognition'），或补充至少一个完整的非 NER 任务分析\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R35-N2\n  summary: \"SciERC 仅 1 个 training seed，统计可靠性不足\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 35\n  last_seen_round: 35\n  mentions:\n    - round: 35\n      reviewers: [1, 2]\n      note: \"R1 列为 Critical Must-Fix，R2 认为 Should-Fix（核心结论由 3-seed Few-NERD/CoNLL 支撑）。共识：SciERC 是分析最详尽的数据集（Figure 2、LP compression、entity probes），单 seed + 529 实例的 power 有限。σ=0.48pp。建议补充 2-3 seeds 或在主文标记为 tentative。\"\n  action_items:\n    - round: 35\n      action: \"SciERC 补充 2 个额外 training seeds（1861 train sentences，训练成本可控），或在 Discussion 中明确标记相关结论为 tentative\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ===== SHOULD-FIX =====\n- id: R35-W1\n  summary: \"正文超出 8 页限制（Conclusion 溢出到 Page 9）\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 35\n  last_seen_round: 35\n  mentions:\n    - round: 35\n      reviewers: [1, 2]\n      note: \"R2 首先发现，R1 核实后同意。Section 9 Discussion/Conclusion 结论段落延续到 p.9 顶部。EMNLP 2026 规则：正文 8 页，Limitations/Ethics 不计入。需压缩 Related Work 或 Discussion。\"\n  action_items:\n    - round: 35\n      action: \"压缩 Section 8 (Related Work) 或 Section 9 (Discussion) 以确保正文在 Page 8 内完结\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R35-W2\n  summary: \"Capability-diversity tension 作为 central finding 缺乏形式化定义\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 35\n  last_seen_round: 35\n  mentions:\n    - round: 35\n      reviewers: [1, 2]\n      note: \"R2 列为 Must-Fix（文献已有隐含讨论），R1 部分反驳（structured output 量化是新的）但同意形式化不足。共识：Figure 3 不够，缺乏可操作定义。CoNLL N=64 时 MV gain 为正 (+0.6pp) 与 'tension' 叙事矛盾。建议给出可测量定义或降级为 observed pattern。\"\n  action_items:\n    - round: 35\n      action: \"给 capability-diversity tension 可操作定义（如 degeneracy vs base F1 函数关系），或降级 framing 为 observed pattern 而非 central finding\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R35-W3\n  summary: \"与 Yun & Price (2025) 差异化论述不充分\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 34\n  last_seen_round: 35\n  mentions:\n    - round: 34\n      reviewers: [1, 2]\n      note: \"R34-W2: 双方 AGREE 需深入讨论 diversity collapse 与 degeneracy 关系。\"\n    - round: 35\n      reviewers: [1, 2]\n      note: \"R2-W2 再次提出：'signal alignment collapse' 与 'format diversity collapse' 语义高度重叠。R1 同意需更显式论述增量差异（四阶段 cascade 的定量诊断 vs 现象描述）。\"\n  action_items:\n    - round: 35\n      action: \"Section 8 增加 1-2 段：(a) alignment collapse vs format diversity collapse 定义级区别；(b) 诊断 cascade 在 Yun & Price 框架中是否可复现或提供增量信息\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R35-W4\n  summary: \"相关工作缺少 conformal prediction、token-level uncertainty decomposition 等领域\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 33\n  last_seen_round: 35\n  mentions:\n    - round: 33\n      reviewers: [1, 2]\n      note: \"R2-W6: 需补 MBR for structured NLP、LLM calibration、concurrent works。\"\n    - round: 34\n      reviewers: [1, 2]\n      note: \"继续指出 Snell et al. (2025)、Eikema et al. (2025) 讨论不足。\"\n    - round: 35\n      reviewers: [1, 2]\n      note: \"R2-W3 新增：conformal prediction for NLP structured outputs、token-level uncertainty decomposition（Xiao et al. 2020）。R1 部分同意（conformal prediction 和 token-level 相关，active learning 关联较弱）。MBR with entity-level F1 utility 概念上是 entity construction 的 principled 版本，应讨论。\"\n  action_items:\n    - round: 35\n      action: \"Section 8 末尾增加 1 段覆盖 conformal prediction for NLP、token-level uncertainty decomposition、MBR with structural utility\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R35-W5\n  summary: \"Proposition 1 entity independence 假设与数据不符，bound 过松\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 33\n  last_seen_round: 35\n  mentions:\n    - round: 33\n      reviewers: [1]\n      note: \"R1-N1: θ_crit 验证问题。\"\n    - round: 35\n      reviewers: [1, 2]\n      note: \"双方 AGREE independence 假设是问题。Split-half r=0.578-0.644 违反假设，Table 31 bound ratio 0.13-0.63。R1 认为 Proposition 定性方向仍成立但松弛度应更透明；R2 建议降格为 illustrative bound。共识：提供 correlated entity 下 bound 偏移数值分析，或明确降格。\"\n  action_items:\n    - round: 35\n      action: \"在 Proposition 1 后添加 correlated entity 的数值分析（bound 在 3-12% correlation 下偏移多少），或明确降格为 illustrative upper bound\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R35-W6\n  summary: \"Free-form decoding ablation 缺少 Few-NERD（degeneracy 最低的数据集）\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 34\n  last_seen_round: 35\n  mentions:\n    - round: 34\n      reviewers: [1, 2]\n      note: \"R34-W1: 仅覆盖 SciERC。\"\n    - round: 35\n      reviewers: [1, 2]\n      note: \"R1-W5 再次提出，R2 完全同意。Few-NERD degeneracy 最低（12%），恰是 constrained decoding 效果应最小的场景——补充该实验可强化或反驳 'degeneracy 是根本原因' 的论点。\"\n  action_items:\n    - round: 35\n      action: \"补充 Few-NERD free-form decoding ablation 实验\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R35-W7\n  summary: \"诊断 cascade 阈值（degeneracy >30%, α<0.05）的 task-specificity 未讨论\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 35\n  last_seen_round: 35\n  mentions:\n    - round: 35\n      reviewers: [1, 2]\n      note: \"R2-W4 首次提出，R1 完全同意。论文已观察到 task-specific 差异大（SciERC 12% vs WNUT-17 51% degeneracy），但未讨论 cascade 阈值在不同 task 上是否稳定。若定位为通用诊断方法论，需展示适用性。\"\n  action_items:\n    - round: 35\n      action: \"明确说明阈值的 task-specificity；在 RE 扩展中完整运行 cascade 而非仅报告 LP 结果\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ===== PRIOR ISSUES NOT RAISED THIS ROUND =====\n- id: R1-N1\n  summary: \"θ_crit=0.70 阈值缺乏 held-out 验证\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 33\n  last_seen_round: 34\n  mentions:\n    - round: 33\n      reviewers: [1]\n      note: \"R1 认为 Must-Fix（post-hoc fitting 风险）；R2 反驳称有 Corollary 1 理论支撑，降级为 Should-Fix。\"\n    - round: 34\n      reviewers: [1, 2]\n      note: \"R1 再次列为 Must-Fix；R2 同意需要澄清但建议降级为 Should-Fix。\"\n    - round: 35\n      reviewers: []\n      note: \"本轮未被任何 Reviewer 提及。论文 Section 6 / Discussion 已有 θ_crit 相关讨论。可能已部分解决，待 Research Director 确认。\"\n  action_items:\n    - round: 33\n      action: \"Agent CPU: sweep θ∈{0.60,0.65,0.70,0.75,0.80}，检查 Table 31 结论稳定性\"\n      assigned_to: agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R1-N3\n  summary: \"Entity construction 作为 prescriptive contribution 证据不足\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 33\n  last_seen_round: 34\n  mentions:\n    - round: 33\n      reviewers: [1, 2]\n      note: \"双方共识：阈值 k per-dataset 优化无部署策略；Holm 全局校正后多数不显著。\"\n    - round: 34\n      reviewers: [1, 2]\n      note: \"双方 AGREE prescriptive arm 薄弱。\"\n    - round: 35\n      reviewers: []\n      note: \"本轮未被 Reviewer 提及。论文 Section 6.1 已将 construction 标记为 exploratory。可能已修复，待 Research Director 确认。\"\n  action_items:\n    - round: 33\n      action: \"Paper Agent: 降级 construction 为 exploratory result\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R2-W1\n  summary: \"Entity-level construction 与 Xie et al. (2023) 差异不清晰\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 33\n  last_seen_round: 34\n  mentions:\n    - round: 33\n      reviewers: [1, 2]\n      note: \"双方 AGREE。增量贡献阐述不充分。\"\n    - round: 34\n      reviewers: [2]\n      note: \"R2 再次指出。\"\n    - round: 35\n      reviewers: []\n      note: \"本轮未被 Reviewer 直接提及。可能已通过 Section 8 'What is new' 段落部分解决，待确认。\"\n  action_items:\n    - round: 33\n      action: \"Paper Agent: §6.1 增加与 Xie et al. 显式对比\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R2-W3\n  summary: \"Framework vs empirical study 定位模糊\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 33\n  last_seen_round: 34\n  mentions:\n    - round: 33\n      reviewers: [1, 2]\n      note: \"标题用 'Diagnostic Framework' 但更接近分析方法论。\"\n    - round: 34\n      reviewers: [1, 2]\n      note: \"分歧未解决。\"\n    - round: 35\n      reviewers: []\n      note: \"本轮未直接提及，但 scope overclaim (R35-N1) 部分覆盖此问题——标题已从 'Diagnostic Framework' 转向 'Boundary Conditions'。\"\n  action_items:\n    - round: 34\n      action: \"Framing 调整：强化 empirical characterization 定位\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R34-N1\n  summary: \"全局 Holm-Bonferroni (k=57) 下核心 NER claim 不显著 (p_HB=0.055)\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 34\n  last_seen_round: 34\n  mentions:\n    - round: 34\n      reviewers: [1, 2]\n      note: \"双方共识：主文需透明报告全局校正结果。\"\n    - round: 35\n      reviewers: []\n      note: \"本轮未被 Reviewer 提及。论文 Limitations 已讨论全局校正和 BH FDR，Table 12 已呈现。可能已修复，待确认。\"\n  action_items:\n    - round: 34\n      action: \"Paper Agent: 主文增加全局 Holm-Bonferroni 结果\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R2-M1\n  summary: \"Table 1 '2-seed' vs 正文 '3-seed' 不一致\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 33\n  last_seen_round: 34\n  mentions:\n    - round: 33\n      reviewers: [1, 2]\n      note: \"双方 AGREE。\"\n    - round: 34\n      reviewers: [1, 2]\n      note: \"仍未解决。\"\n    - round: 35\n      reviewers: []\n      note: \"本轮未被提及。Table 1 注脚已标明 '2-seed mean±σ'，Section 7.1 说明了不同实验的 seed 数量差异。可能已部分解决。\"\n  action_items:\n    - round: 33\n      action: \"Paper Agent: 统一 seed 数量描述或说明原因\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "issues_yaml": "issues:\n# ===== CRITICAL / MUST-FIX =====\n- id: R35-N1\n  summary: \"Scope overclaim: 标题声称 'structured prediction' 但证据主要是 NER\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 33\n  last_seen_round: 35\n  mentions:\n    - round: 33\n      reviewers: [1, 2]\n      note: \"R1-W4: RE/SQL 覆盖有限。当时为 warning。\"\n    - round: 34\n      reviewers: [1, 2]\n      note: \"继续作为 warning。\"\n    - round: 35\n      reviewers: [1, 2]\n      note: \"双方升级为 Critical Must-Fix。标题 'Boundary Conditions for Structured Prediction' 但充分实验仅 NER（4 数据集 × 2 模型家族）。RE 仅 SciERC 单数据集 exploratory（397 实例，1 模型），SQL 仅一句话。NER entity-set 与 parsing/SRL/event extraction 输出结构差异巨大。Discussion 自承 'generalization to other structured tasks requires further investigation'，与标题矛盾。\"\n  action_items:\n    - round: 35\n      action: \"限缩标题为 NER/IE（如 'Boundary Conditions for Entity Recognition'），或补充至少一个完整的非 NER 任务分析\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R35-N2\n  summary: \"SciERC 仅 1 个 training seed，统计可靠性不足\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 35\n  last_seen_round: 35\n  mentions:\n    - round: 35\n      reviewers: [1, 2]\n      note: \"R1 列为 Critical Must-Fix，R2 认为 Should-Fix（核心结论由 3-seed Few-NERD/CoNLL 支撑）。共识：SciERC 是分析最详尽的数据集（Figure 2、LP compression、entity probes），单 seed + 529 实例的 power 有限。σ=0.48pp。建议补充 2-3 seeds 或在主文标记为 tentative。\"\n  action_items:\n    - round: 35\n      action: \"SciERC 补充 2 个额外 training seeds（1861 train sentences，训练成本可控），或在 Discussion 中明确标记相关结论为 tentative\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ===== SHOULD-FIX =====\n- id: R35-W1\n  summary: \"正文超出 8 页限制（Conclusion 溢出到 Page 9）\"\n  category: format\n  severity: warning\n  status: open\n  first_raised_round: 35\n  last_seen_round: 35\n  mentions:\n    - round: 35\n      reviewers: [1, 2]\n      note: \"R2 首先发现，R1 核实后同意。Section 9 Discussion/Conclusion 结论段落延续到 p.9 顶部。EMNLP 2026 规则：正文 8 页，Limitations/Ethics 不计入。需压缩 Related Work 或 Discussion。\"\n  action_items:\n    - round: 35\n      action: \"压缩 Section 8 (Related Work) 或 Section 9 (Discussion) 以确保正文在 Page 8 内完结\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R35-W2\n  summary: \"Capability-diversity tension 作为 central finding 缺乏形式化定义\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 35\n  last_seen_round: 35\n  mentions:\n    - round: 35\n      reviewers: [1, 2]\n      note: \"R2 列为 Must-Fix（文献已有隐含讨论），R1 部分反驳（structured output 量化是新的）但同意形式化不足。共识：Figure 3 不够，缺乏可操作定义。CoNLL N=64 时 MV gain 为正 (+0.6pp) 与 'tension' 叙事矛盾。建议给出可测量定义或降级为 observed pattern。\"\n  action_items:\n    - round: 35\n      action: \"给 capability-diversity tension 可操作定义（如 degeneracy vs base F1 函数关系），或降级 framing 为 observed pattern 而非 central finding\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R35-W3\n  summary: \"与 Yun & Price (2025) 差异化论述不充分\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 34\n  last_seen_round: 35\n  mentions:\n    - round: 34\n      reviewers: [1, 2]\n      note: \"R34-W2: 双方 AGREE 需深入讨论 diversity collapse 与 degeneracy 关系。\"\n    - round: 35\n      reviewers: [1, 2]\n      note: \"R2-W2 再次提出：'signal alignment collapse' 与 'format diversity collapse' 语义高度重叠。R1 同意需更显式论述增量差异（四阶段 cascade 的定量诊断 vs 现象描述）。\"\n  action_items:\n    - round: 35\n      action: \"Section 8 增加 1-2 段：(a) alignment collapse vs format diversity collapse 定义级区别；(b) 诊断 cascade 在 Yun & Price 框架中是否可复现或提供增量信息\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R35-W4\n  summary: \"相关工作缺少 conformal prediction、token-level uncertainty decomposition 等领域\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 33\n  last_seen_round: 35\n  mentions:\n    - round: 33\n      reviewers: [1, 2]\n      note: \"R2-W6: 需补 MBR for structured NLP、LLM calibration、concurrent works。\"\n    - round: 34\n      reviewers: [1, 2]\n      note: \"继续指出 Snell et al. (2025)、Eikema et al. (2025) 讨论不足。\"\n    - round: 35\n      reviewers: [1, 2]\n      note: \"R2-W3 新增：conformal prediction for NLP structured outputs、token-level uncertainty decomposition（Xiao et al. 2020）。R1 部分同意（conformal prediction 和 token-level 相关，active learning 关联较弱）。MBR with entity-level F1 utility 概念上是 entity construction 的 principled 版本，应讨论。\"\n  action_items:\n    - round: 35\n      action: \"Section 8 末尾增加 1 段覆盖 conformal prediction for NLP、token-level uncertainty decomposition、MBR with structural utility\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R35-W5\n  summary: \"Proposition 1 entity independence 假设与数据不符，bound 过松\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 33\n  last_seen_round: 35\n  mentions:\n    - round: 33\n      reviewers: [1]\n      note: \"R1-N1: θ_crit 验证问题。\"\n    - round: 35\n      reviewers: [1, 2]\n      note: \"双方 AGREE independence 假设是问题。Split-half r=0.578-0.644 违反假设，Table 31 bound ratio 0.13-0.63。R1 认为 Proposition 定性方向仍成立但松弛度应更透明；R2 建议降格为 illustrative bound。共识：提供 correlated entity 下 bound 偏移数值分析，或明确降格。\"\n  action_items:\n    - round: 35\n      action: \"在 Proposition 1 后添加 correlated entity 的数值分析（bound 在 3-12% correlation 下偏移多少），或明确降格为 illustrative upper bound\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R35-W6\n  summary: \"Free-form decoding ablation 缺少 Few-NERD（degeneracy 最低的数据集）\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 34\n  last_seen_round: 35\n  mentions:\n    - round: 34\n      reviewers: [1, 2]\n      note: \"R34-W1: 仅覆盖 SciERC。\"\n    - round: 35\n      reviewers: [1, 2]\n      note: \"R1-W5 再次提出，R2 完全同意。Few-NERD degeneracy 最低（12%），恰是 constrained decoding 效果应最小的场景——补充该实验可强化或反驳 'degeneracy 是根本原因' 的论点。\"\n  action_items:\n    - round: 35\n      action: \"补充 Few-NERD free-form decoding ablation 实验\"\n      assigned_to: agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n- id: R35-W7\n  summary: \"诊断 cascade 阈值（degeneracy >30%, α<0.05）的 task-specificity 未讨论\"\n  category: method\n  severity: warning\n  status: open\n  first_raised_round: 35\n  last_seen_round: 35\n  mentions:\n    - round: 35\n      reviewers: [1, 2]\n      note: \"R2-W4 首次提出，R1 完全同意。论文已观察到 task-specific 差异大（SciERC 12% vs WNUT-17 51% degeneracy），但未讨论 cascade 阈值在不同 task 上是否稳定。若定位为通用诊断方法论，需展示适用性。\"\n  action_items:\n    - round: 35\n      action: \"明确说明阈值的 task-specificity；在 RE 扩展中完整运行 cascade 而非仅报告 LP 结果\"\n      assigned_to: paper_agent\n      status: open\n  resolution: \"\"\n  resolution_round: null\n\n# ===== PRIOR ISSUES NOT RAISED THIS ROUND =====\n- id: R1-N1\n  summary: \"θ_crit=0.70 阈值缺乏 held-out 验证\"\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 33\n  last_seen_round: 34\n  mentions:\n    - round: 33\n      reviewers: [1]\n      note: \"R1 认为 Must-Fix（post-hoc fitting 风险）；R2 反驳称有 Corollary 1 理论支撑，降级为 Should-Fix。\"\n    - round: 34\n      reviewers: [1, 2]\n      note: \"R1 再次列为 Must-Fix；R2 同意需要澄清但建议降级为 Should-Fix。\"\n    - round: 35\n      reviewers: []\n      note: \"本轮未被任何 Reviewer 提及。论文 Section 6 / Discussion 已有 θ_crit 相关讨论。可能已部分解决，待 Research Director 确认。\"\n  action_items:\n    - round: 33\n      action: \"Agent CPU: sweep θ∈{0.60,0.65,0.70,0.75,0.80}，检查 Table 31 结论稳定性\"\n      assigned_to: agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R1-N3\n  summary: \"Entity construction 作为 prescriptive contribution 证据不足\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 33\n  last_seen_round: 34\n  mentions:\n    - round: 33\n      reviewers: [1, 2]\n      note: \"双方共识：阈值 k per-dataset 优化无部署策略；Holm 全局校正后多数不显著。\"\n    - round: 34\n      reviewers: [1, 2]\n      note: \"双方 AGREE prescriptive arm 薄弱。\"\n    - round: 35\n      reviewers: []\n      note: \"本轮未被 Reviewer 提及。论文 Section 6.1 已将 construction 标记为 exploratory。可能已修复，待 Research Director 确认。\"\n  action_items:\n    - round: 33\n      action: \"Paper Agent: 降级 construction 为 exploratory result\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R2-W1\n  summary: \"Entity-level construction 与 Xie et al. (2023) 差异不清晰\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 33\n  last_seen_round: 34\n  mentions:\n    - round: 33\n      reviewers: [1, 2]\n      note: \"双方 AGREE。增量贡献阐述不充分。\"\n    - round: 34\n      reviewers: [2]\n      note: \"R2 再次指出。\"\n    - round: 35\n      reviewers: []\n      note: \"本轮未被 Reviewer 直接提及。可能已通过 Section 8 'What is new' 段落部分解决，待确认。\"\n  action_items:\n    - round: 33\n      action: \"Paper Agent: §6.1 增加与 Xie et al. 显式对比\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R2-W3\n  summary: \"Framework vs empirical study 定位模糊\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 33\n  last_seen_round: 34\n  mentions:\n    - round: 33\n      reviewers: [1, 2]\n      note: \"标题用 'Diagnostic Framework' 但更接近分析方法论。\"\n    - round: 34\n      reviewers: [1, 2]\n      note: \"分歧未解决。\"\n    - round: 35\n      reviewers: []\n      note: \"本轮未直接提及，但 scope overclaim (R35-N1) 部分覆盖此问题——标题已从 'Diagnostic Framework' 转向 'Boundary Conditions'。\"\n  action_items:\n    - round: 34\n      action: \"Framing 调整：强化 empirical characterization 定位\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R34-N1\n  summary: \"全局 Holm-Bonferroni (k=57) 下核心 NER claim 不显著 (p_HB=0.055)\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 34\n  last_seen_round: 34\n  mentions:\n    - round: 34\n      reviewers: [1, 2]\n      note: \"双方共识：主文需透明报告全局校正结果。\"\n    - round: 35\n      reviewers: []\n      note: \"本轮未被 Reviewer 提及。论文 Limitations 已讨论全局校正和 BH FDR，Table 12 已呈现。可能已修复，待确认。\"\n  action_items:\n    - round: 34\n      action: \"Paper Agent: 主文增加全局 Holm-Bonferroni 结果\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null\n\n- id: R2-M1\n  summary: \"Table 1 '2-seed' vs 正文 '3-seed' 不一致\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 33\n  last_seen_round: 34\n  mentions:\n    - round: 33\n      reviewers: [1, 2]\n      note: \"双方 AGREE。\"\n    - round: 34\n      reviewers: [1, 2]\n      note: \"仍未解决。\"\n    - round: 35\n      reviewers: []\n      note: \"本轮未被提及。Table 1 注脚已标明 '2-seed mean±σ'，Section 7.1 说明了不同实验的 seed 数量差异。可能已部分解决。\"\n  action_items:\n    - round: 33\n      action: \"Paper Agent: 统一 seed 数量描述或说明原因\"\n      assigned_to: paper_agent\n      status: in_progress\n  resolution: \"\"\n  resolution_round: null"
  }
}
```

</details>

---


### Tool result

_source line 3795 · 2026-05-22T10:28:17.259753+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml\", \"bytes\": 10643}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 3796 · 2026-05-22T10:30:31.425372+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "struct_self_consist_ie",
  "report": "# 审稿报告 — Round 35 (Fresh Review)\n\n**论文**: When Does Test-Time Scaling Fail? Boundary Conditions for Structured Prediction\n**Venue**: EMNLP 2026 via ARR May 2026 (Deadline: 2026-05-25)\n**审稿模式**: Fresh（全新初审）\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计; R2: 新颖性+完整性）\n**轮次**: Round 1 独立审稿 → 交叉分享 → 收敛（1 轮达成）\n\n---\n\n## Summary\n\n论文研究 test-time compute scaling（self-consistency、best-of-N）在结构化预测上的失败条件，以 NER（4 个数据集）和 RE（exploratory）为案例。核心发现 **correlation-selection gap**：质量估计信号能有效预测输出质量（AUROC 最高 0.82），但 instance-level selection 始终无法超越 greedy decoding（gain < 1pp，N=64）。诊断 cascade 将失败定位到两个 boundary conditions：output convergence（degeneracy 12-68%）和 signal alignment collapse（α→0）。Exploratory entity-level construction 在低 degeneracy 条件下部分绕过瓶颈（+1.40pp on Few-NERD）。\n\n---\n\n## Strengths\n\n**S1** [R1+R2 共识] **统计方法论显著超越 NLP 论文平均水平**。Holm-Bonferroni 全局校正（k=57）、MDE 分析、TOST equivalence testing、bootstrap CI、permutation tests 的组合使用在 NLP 经验性论文中极为罕见，为实证分析设立了高标准。\n\n**S2** [R1+R2 共识] **Correlation-selection gap 是一个真正有价值的经验贡献**。将 \"QE 信号有效\" 与 \"selection 成功\" 解耦，命名并系统量化了此前文献中未被清晰表述的现象。Figure 1 的可视化清晰传达了核心 insight。\n\n**S3** [R1+R2 共识] **Diagnostic cascade 概念清晰且实用**。四阶段诊断（degeneracy → oracle headroom → LP compression → signal alignment）逻辑自洽，每个阶段有可操作的度量。Appendix ae 的三步评估协议对社区有直接实用价值。\n\n**S4** [R1+R2 共识] **异常详尽的消融和 robustness 分析**（47 页附录）。覆盖 temperature、sample size scaling、epoch、LoRA rank、cross-model transfer、OOD、free-form decoding、thinking tokens、entity-level LP decomposition、construction threshold sensitivity 等。\n\n**S5** [R1+R2 共识] **诚实报告负面和有限结果**。MDE 分析坦承 \"absence of evidence, not evidence of absence\"；bypass 策略效果如实呈现（cross-model +0.42pp, entity construction +1.4pp），未过度渲染。\n\n**S6** [R1] **Failure mode gallery**（Appendix ag）提供 9 个具体失败案例的质性分析，直观展示三类典型错误模式，有教学价值。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**N1** [R1+R2 共识, Critical] **Scope overclaim：标题声称 \"Structured Prediction\" 但证据主要是 NER。**\n标题 \"Boundary Conditions for Structured Prediction\" 设定了远超实验覆盖的验证门槛。充分实验仅 NER（4 数据集 × 2 模型家族）。RE 仅 SciERC 单数据集 exploratory 扩展（Appendix o, 397 实例, 1 模型），SQL 仅一句话提及 87.2% degeneracy。NER entity-set（无序集合）与 dependency parsing（树结构）、SRL（predicate-argument）、event extraction（嵌套结构）的输出空间结构差异巨大——degeneracy 和 alignment collapse 的表现形式可能完全不同。Discussion (p.8) 自承 \"generalization to other structured tasks requires further investigation\"，与标题的强 claim 形成内在矛盾。\n→ **建议**：(a) 限缩标题为 NER/IE（如 \"Boundary Conditions for Entity Recognition\"）；或 (b) 补充至少一个完整的非 NER 结构化预测任务的 cascade 分析。\n\n**N2** [R1 Critical, R2 Should-Fix, 分歧] **SciERC 仅 1 个 training seed，统计可靠性不足。**\nSciERC 是论文中分析最详尽的数据集（Figure 2 LP compression、entity-level probe、calibration analysis、free-form ablation 都以 SciERC 为 primary showcase），但仅用 1 个 training seed（seed=42），测试集仅 529 实例。论文自承 σ=0.48pp。Few-NERD 和 CoNLL 使用 3 seeds，SciERC 为何只用 1 seed 未解释。R1 认为 critical（核心发现可能不稳定），R2 认为 should-fix（核心结论由 3-seed Few-NERD/CoNLL 支撑，SciERC 更多是补充验证）。\n→ **建议**：补充 SciERC 2 个额外 training seeds（1861 train sentences，训练成本可控）；若不可行，在主文明确标记 SciERC 相关结论为 tentative。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1** [R2 提出, R1 确认] **正文可能超出 8 页限制。** Section 9 (Discussion and Conclusion) 结论段落溢出到 Page 9 顶部。EMNLP 2026 规则：正文 8 页，Limitations/Ethics 不计入。需压缩 Related Work 或 Discussion。\n\n**W2** [R1+R2 共识] **Capability-diversity tension 作为 central finding 缺乏形式化。** 论文将此呈现为 central finding（Section 9），但缺乏可操作定义。Figure 3 仅展示 3 个数据集的 MV ΔF1 趋势，且 CoNLL N=64 时 MV gain 为正（+0.6pp），与 tension 叙事部分矛盾。R1 认为 structured output 上的量化分析是新的，但同意形式化不足。R2 认为文献已有隐含讨论（Snell et al. 2025, Brown et al. 2024）。\n→ **建议**：给出可测量定义（如 degeneracy vs base F1 的函数关系），或降级为 observed pattern。\n\n**W3** [R1+R2 共识] **与 Yun & Price (2025) 差异化论述不充分。** \"Signal alignment collapse\" 与 \"format diversity collapse\" 语义高度重叠。Section 8 仅一句话带过差异。需 1-2 段明确对比两个概念的定义级区别及诊断 cascade 的增量信息。\n\n**W4** [R2 提出, R1 部分同意] **相关工作缺少重要领域。** 缺失：conformal prediction for NLP structured outputs、token-level uncertainty decomposition（Xiao et al. 2020）、MBR with entity-level F1 utility function（概念上即 entity construction 的 principled 版本）。R1 同意 conformal prediction 和 token-level 相关，认为 active learning 关联较弱。\n\n**W5** [R1+R2 共识] **Proposition 1 entity independence 假设与数据不符。** Split-half r=0.578-0.644 违反 independence 假设。Table 31 bound ratio 0.13-0.63 证实 bound 过松。R1 认为定性方向仍成立（高 degeneracy → MV 无法改善），R2 建议降格为 illustrative bound。\n→ **建议**：提供 correlated entity（3-12% correlation）下 bound 偏移的数值分析，或明确降格。\n\n**W6** [R1+R2 共识] **Free-form decoding ablation 覆盖不全。** 仅 SciERC + CoNLL。Few-NERD（degeneracy 最低 12%）是最应验证的数据集——若 free-form 下 degeneracy 不变，强化 \"model-intrinsic\" 论点；若显著下降，cascade 结论需重新解读。\n\n**W7** [R2 提出, R1 同意] **诊断 cascade 阈值的 task-specificity 未讨论。** Degeneracy >30%、α<0.05 等阈值在不同 task 上是否稳定？已观察到 task 差异大（SciERC 12% vs WNUT-17 67.9% degeneracy），需明确说明。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **Scope overclaim 是最严重的问题**：两位 Reviewer 独立提出且交叉确认，NER 证据不能支撑 \"structured prediction\" 的标题\n2. **Correlation-selection gap 是最有价值的贡献**：命名并量化了此前未被清晰表述的现象\n3. **统计方法论达到高标准**：Holm-Bonferroni k=57、MDE、TOST 组合使用远超同行\n4. **Entity independence 假设需要更透明的讨论**：bound 过松但定性方向成立\n5. **Capability-diversity tension 形式化不足**：需要可操作定义或降级 framing\n6. **Free-form ablation 需要覆盖 Few-NERD**\n7. **正文页数超限需修复**（格式合规）\n\n## Reviewer Divergence [REBUT]\n\n1. **SciERC 单 seed 严重程度**：R1 认为 Critical Must-Fix（核心发现可能不稳定），R2 认为 Should-Fix（核心结论由 3-seed Few-NERD/CoNLL 支撑）。**Director 判断**：列为 Must-Fix 但允许 camera-ready 补充，不一票否决。\n\n2. **方法对比公平性**（R1-W2）：R2 反驳——论文论点是 \"所有方法 gain 都小\"，不是 iso-compute 竞赛。**Director 判断**：R2 论点更强，降级为小问题（建议 Table 2 caption 标注 compute cost）。\n\n3. **Greedy baseline 选择**（R1-W3）：R2 反驳——greedy 是 test-time scaling 文献标准 baseline（Snell et al. 2025, Wang et al. 2023, Brown et al. 2024）。**Director 判断**：R2 论点成立，不构成问题。\n\n4. **Capability-diversity tension 新颖性**：R1 认为 structured output 量化是新的，R2 认为增量有限。**Director 判断**：作为经验观察有价值，但不应 framed 为 central finding——Should-Fix。\n\n---\n\n## Questions\n\n**Q1** [R2] Correlation-selection gap 是否在任何非 NER 结构化预测任务中被验证过？\n\n**Q2** [R2] 为何没有直接实验 entity-level F1 作为 MBR utility function 的方案？概念上比 majority vote 更 principled。\n\n**Q3** [R2] Proposition 1 bound ratio 仅 0.13-0.63——是否考虑过基于 partial degeneracy 的连续 bound？\n\n**Q4** [R2] Figure 3 中 Few-NERD N=64 仍有正向增益，SciERC 几乎平坦——是否主要由 base model quality 驱动？更弱模型（3B/1B）是否会有更大 scaling gains？\n\n**Q5** [R1] SciERC 为何只用 1 个 training seed？是资源限制还是其他原因？\n\n---\n\n## Missing References\n\n- Conformal prediction for NLP structured outputs（近年多项工作将 conformal prediction 应用于 NER/序列标注的 uncertainty quantification）\n- Token-level uncertainty decomposition（如 Xiao et al. 2020 epistemic/aleatoric 分解）\n- Snell et al. (2025, ICLR) compute-optimal scaling 中关于 diminishing returns 的讨论\n- Entity-level F1 作为 MBR utility function 的 principled 版本（vs 当前的 majority vote）\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未启用。项目配置中 `external_review.paperreview_ai.enabled` 未设置为 true。\n\n---\n\n## Visual Layout Check（非评分项）\n\n状态：**done**（耗时约 4 分钟）\n\n| 严重度 | 位置 | 发现 |\n|--------|------|------|\n| warning | p.24 | 附录页面约 2/3 空白（Appendix n 结尾），建议调整 float/section break |\n| warning | p.17 | Figure 7 热力图使用红→绿色阶，对红绿色盲不友好，建议改 viridis 或 Blue→Orange |\n| warning | p.16 | Figure 6 校准图同样存在色盲友好性问题 |\n| warning | p.7 | 主文单页密度极高（Table 3 + Table 4 + Figure 4 + 两段文字），视觉上略拥挤 |\n| info | p.1 | 首页无视觉锚点，Figure 1 在 p.2，延迟可控 |\n| info | p.3 | 唯一纯文本页（信号定义），建议加小型 signal summary 表 |\n| info | p.14-47 | 附录 34 页极为详尽，关键附录建议主文显式指引 |\n| info | p.5 | Table 2 信息密度高但格式正确 |\n| info | p.6 | Figure 3 色彩区分度良好且色盲友好 |\n| info | p.47 | 末页空间利用合理（~85%） |\n\n无 critical 排版问题。色盲友好性（Figure 6, 7）建议修复。\n\n---\n\n## Overall Assessment\n\n**评分**: **3.5 — Borderline Conference**\n**置信度**: 4/5（两位 Reviewer 均熟悉 self-consistency 和 NER 领域文献）\n\n### 评分理由\n\n**支持 Conference (4.0) 的因素**：\n- Correlation-selection gap 是社区有价值的经验发现，命名并量化了此前模糊的现象\n- 诊断 cascade 有独立方法论价值，附带可复用的三步评估协议\n- 统计方法论（Holm-Bonferroni k=57、MDE、TOST）在 NLP 经验性论文中属上乘\n- 47 页附录体现极致的 thoroughness，几乎覆盖所有可预见的 reviewer 质疑\n- 诚实报告负面结果和方法局限性\n\n**限制 Conference 的因素**：\n- **[Critical]** 标题/Abstract 声称 \"structured prediction\" 但证据主要是 NER——scope-evidence gap 是最大问题\n- SciERC（最核心数据集）仅 1 training seed，统计可靠性不足\n- Capability-diversity tension 作为 central finding 形式化不足，且文献中已有隐含讨论\n- 核心贡献是诊断性的（\"what fails\"）而非建设性的（\"how to fix\"），prescriptive guidance 有限\n- Proposition 1 的理论贡献偏薄（independence 假设不成立，bound 过松）\n\n### 改进路径（Conference 4.0 所需）\n\n若作者能在 camera-ready 中完成以下修改，论文可达 Conference 水平：\n1. **[必须]** 限缩标题和 Abstract scope 为 NER/Information Extraction\n2. **[必须]** 补充 SciERC 多 seed 实验（或标记为 tentative）\n3. **[必须]** 修复页数溢出（压缩至 8 页正文）\n4. **[强烈建议]** 加强与 Yun & Price (2025) 的差异化论述\n5. **[建议]** 降级 capability-diversity tension 的 framing 或给出可操作定义\n\n当前版本适合 **Findings (3.0-3.5)**；scope 修正后为 **Borderline Conference (3.5-4.0)**。\n\n---\n\n## Detailed Comments\n\n### Section-by-Section\n\n**Abstract**: 第一句 \"structured prediction remains uncharacterized\" 过强，实际只 characterize 了 NER（和初步 RE）。建议改为 \"entity-level information extraction\" 或 \"set-valued NER outputs\"。\"Exploratory entity-level construction partially bypasses\" 中 \"partially\" 用词准确。\n\n**Section 1 (Introduction)**: Discover → Diagnose → Explore bypasses 三阶段叙事清晰。但 \"using NER...and RE as case studies\" 中 RE 的篇幅远不能称为 case study（Appendix 2 段 vs NER 的完整 pipeline）。\n\n**Section 2 (Diagnostic Framework)**: 五种信号的定义清晰。SJ 引用 Fleiss 1971 可能有误（Fleiss 是 inter-rater reliability，非 Soft Jaccard 来源）。Table 5 术语不一致（\"Soft Jaccard\" vs \"structural similarity\"）。建议 p.3 加小型 signal summary 表改善可浏览性。\n\n**Section 3 (How Self-Verification Fails)**: Introspection boundary 是有趣概念但后续很少复用——考虑去掉以减少 cognitive load，或在 Discussion 中回顾。\n\n**Section 4 (Where Single-Signal Selection Fails)**: 核心 section。Figure 2 双量纲共轴（AUROC vs ρ）初看混淆，建议分双轴。Table 1 caption \"paired bootstrap\" 但内容是 Spearman ρ，可能有误。\n\n**Section 5 (Adaptive Methods)**: Table 2 信息密度高。建议添加 compute cost 列（各方法相对于 greedy 的倍数），避免误导为等预算比较。\n\n**Section 6 (Threshold Regime Analysis)**: Proposition 1 的 \"entity selection diagnostic\" 方向性有用，但应在正文中明确标记为 illustrative upper bound（当前表述可能让读者误以为是 tight bound）。θ_crit=0.70 的 task-specificity 应讨论。\n\n**Section 7 (Experiments)**: 详尽。Few-NERD LP selection +1.39pp (p<0.001) 是论文最强的正面结果。Table 4 的 \"2-seed\" vs Section 7.1 \"3-seed\" 不一致应修复。\n\n**Section 8 (Related Work)**: 需扩展：补充 conformal prediction、token-level uncertainty、MBR with structural utility。与 Yun & Price (2025) 的差异化需从一句话扩展为 1-2 段。\n\n**Section 9 (Discussion and Conclusion)**: \"Central finding is a capability-diversity tension\" 需更强支撑或降级。Conclusion 段落溢出到 p.9——必须压缩。\n\n**Limitations**: 覆盖面广（correlational vs interventional、scope、seed、prompt template）。建议明确提及为何 SciERC 只用 1 seed。\n\n**Ethics Statement**: 基本合规。论文脚注已注明 \"No new human data was collected\"。",
  "reviewer_ids_acknowledged": "[\"1\", \"2\"]",
  "cross_response_reviewer_ids": "[\"1\", \"2\"]",
  "overall_score": "3.5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "report": "# 审稿报告 — Round 35 (Fresh Review)\n\n**论文**: When Does Test-Time Scaling Fail? Boundary Conditions for Structured Prediction\n**Venue**: EMNLP 2026 via ARR May 2026 (Deadline: 2026-05-25)\n**审稿模式**: Fresh（全新初审）\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计; R2: 新颖性+完整性）\n**轮次**: Round 1 独立审稿 → 交叉分享 → 收敛（1 轮达成）\n\n---\n\n## Summary\n\n论文研究 test-time compute scaling（self-consistency、best-of-N）在结构化预测上的失败条件，以 NER（4 个数据集）和 RE（exploratory）为案例。核心发现 **correlation-selection gap**：质量估计信号能有效预测输出质量（AUROC 最高 0.82），但 instance-level selection 始终无法超越 greedy decoding（gain < 1pp，N=64）。诊断 cascade 将失败定位到两个 boundary conditions：output convergence（degeneracy 12-68%）和 signal alignment collapse（α→0）。Exploratory entity-level construction 在低 degeneracy 条件下部分绕过瓶颈（+1.40pp on Few-NERD）。\n\n---\n\n## Strengths\n\n**S1** [R1+R2 共识] **统计方法论显著超越 NLP 论文平均水平**。Holm-Bonferroni 全局校正（k=57）、MDE 分析、TOST equivalence testing、bootstrap CI、permutation tests 的组合使用在 NLP 经验性论文中极为罕见，为实证分析设立了高标准。\n\n**S2** [R1+R2 共识] **Correlation-selection gap 是一个真正有价值的经验贡献**。将 \"QE 信号有效\" 与 \"selection 成功\" 解耦，命名并系统量化了此前文献中未被清晰表述的现象。Figure 1 的可视化清晰传达了核心 insight。\n\n**S3** [R1+R2 共识] **Diagnostic cascade 概念清晰且实用**。四阶段诊断（degeneracy → oracle headroom → LP compression → signal alignment）逻辑自洽，每个阶段有可操作的度量。Appendix ae 的三步评估协议对社区有直接实用价值。\n\n**S4** [R1+R2 共识] **异常详尽的消融和 robustness 分析**（47 页附录）。覆盖 temperature、sample size scaling、epoch、LoRA rank、cross-model transfer、OOD、free-form decoding、thinking tokens、entity-level LP decomposition、construction threshold sensitivity 等。\n\n**S5** [R1+R2 共识] **诚实报告负面和有限结果**。MDE 分析坦承 \"absence of evidence, not evidence of absence\"；bypass 策略效果如实呈现（cross-model +0.42pp, entity construction +1.4pp），未过度渲染。\n\n**S6** [R1] **Failure mode gallery**（Appendix ag）提供 9 个具体失败案例的质性分析，直观展示三类典型错误模式，有教学价值。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**N1** [R1+R2 共识, Critical] **Scope overclaim：标题声称 \"Structured Prediction\" 但证据主要是 NER。**\n标题 \"Boundary Conditions for Structured Prediction\" 设定了远超实验覆盖的验证门槛。充分实验仅 NER（4 数据集 × 2 模型家族）。RE 仅 SciERC 单数据集 exploratory 扩展（Appendix o, 397 实例, 1 模型），SQL 仅一句话提及 87.2% degeneracy。NER entity-set（无序集合）与 dependency parsing（树结构）、SRL（predicate-argument）、event extraction（嵌套结构）的输出空间结构差异巨大——degeneracy 和 alignment collapse 的表现形式可能完全不同。Discussion (p.8) 自承 \"generalization to other structured tasks requires further investigation\"，与标题的强 claim 形成内在矛盾。\n→ **建议**：(a) 限缩标题为 NER/IE（如 \"Boundary Conditions for Entity Recognition\"）；或 (b) 补充至少一个完整的非 NER 结构化预测任务的 cascade 分析。\n\n**N2** [R1 Critical, R2 Should-Fix, 分歧] **SciERC 仅 1 个 training seed，统计可靠性不足。**\nSciERC 是论文中分析最详尽的数据集（Figure 2 LP compression、entity-level probe、calibration analysis、free-form ablation 都以 SciERC 为 primary showcase），但仅用 1 个 training seed（seed=42），测试集仅 529 实例。论文自承 σ=0.48pp。Few-NERD 和 CoNLL 使用 3 seeds，SciERC 为何只用 1 seed 未解释。R1 认为 critical（核心发现可能不稳定），R2 认为 should-fix（核心结论由 3-seed Few-NERD/CoNLL 支撑，SciERC 更多是补充验证）。\n→ **建议**：补充 SciERC 2 个额外 training seeds（1861 train sentences，训练成本可控）；若不可行，在主文明确标记 SciERC 相关结论为 tentative。\n\n### Should-Fix（影响评分但不一票否决）\n\n**W1** [R2 提出, R1 确认] **正文可能超出 8 页限制。** Section 9 (Discussion and Conclusion) 结论段落溢出到 Page 9 顶部。EMNLP 2026 规则：正文 8 页，Limitations/Ethics 不计入。需压缩 Related Work 或 Discussion。\n\n**W2** [R1+R2 共识] **Capability-diversity tension 作为 central finding 缺乏形式化。** 论文将此呈现为 central finding（Section 9），但缺乏可操作定义。Figure 3 仅展示 3 个数据集的 MV ΔF1 趋势，且 CoNLL N=64 时 MV gain 为正（+0.6pp），与 tension 叙事部分矛盾。R1 认为 structured output 上的量化分析是新的，但同意形式化不足。R2 认为文献已有隐含讨论（Snell et al. 2025, Brown et al. 2024）。\n→ **建议**：给出可测量定义（如 degeneracy vs base F1 的函数关系），或降级为 observed pattern。\n\n**W3** [R1+R2 共识] **与 Yun & Price (2025) 差异化论述不充分。** \"Signal alignment collapse\" 与 \"format diversity collapse\" 语义高度重叠。Section 8 仅一句话带过差异。需 1-2 段明确对比两个概念的定义级区别及诊断 cascade 的增量信息。\n\n**W4** [R2 提出, R1 部分同意] **相关工作缺少重要领域。** 缺失：conformal prediction for NLP structured outputs、token-level uncertainty decomposition（Xiao et al. 2020）、MBR with entity-level F1 utility function（概念上即 entity construction 的 principled 版本）。R1 同意 conformal prediction 和 token-level 相关，认为 active learning 关联较弱。\n\n**W5** [R1+R2 共识] **Proposition 1 entity independence 假设与数据不符。** Split-half r=0.578-0.644 违反 independence 假设。Table 31 bound ratio 0.13-0.63 证实 bound 过松。R1 认为定性方向仍成立（高 degeneracy → MV 无法改善），R2 建议降格为 illustrative bound。\n→ **建议**：提供 correlated entity（3-12% correlation）下 bound 偏移的数值分析，或明确降格。\n\n**W6** [R1+R2 共识] **Free-form decoding ablation 覆盖不全。** 仅 SciERC + CoNLL。Few-NERD（degeneracy 最低 12%）是最应验证的数据集——若 free-form 下 degeneracy 不变，强化 \"model-intrinsic\" 论点；若显著下降，cascade 结论需重新解读。\n\n**W7** [R2 提出, R1 同意] **诊断 cascade 阈值的 task-specificity 未讨论。** Degeneracy >30%、α<0.05 等阈值在不同 task 上是否稳定？已观察到 task 差异大（SciERC 12% vs WNUT-17 67.9% degeneracy），需明确说明。\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **Scope overclaim 是最严重的问题**：两位 Reviewer 独立提出且交叉确认，NER 证据不能支撑 \"structured prediction\" 的标题\n2. **Correlation-selection gap 是最有价值的贡献**：命名并量化了此前未被清晰表述的现象\n3. **统计方法论达到高标准**：Holm-Bonferroni k=57、MDE、TOST 组合使用远超同行\n4. **Entity independence 假设需要更透明的讨论**：bound 过松但定性方向成立\n5. **Capability-diversity tension 形式化不足**：需要可操作定义或降级 framing\n6. **Free-form ablation 需要覆盖 Few-NERD**\n7. **正文页数超限需修复**（格式合规）\n\n## Reviewer Divergence [REBUT]\n\n1. **SciERC 单 seed 严重程度**：R1 认为 Critical Must-Fix（核心发现可能不稳定），R2 认为 Should-Fix（核心结论由 3-seed Few-NERD/CoNLL 支撑）。**Director 判断**：列为 Must-Fix 但允许 camera-ready 补充，不一票否决。\n\n2. **方法对比公平性**（R1-W2）：R2 反驳——论文论点是 \"所有方法 gain 都小\"，不是 iso-compute 竞赛。**Director 判断**：R2 论点更强，降级为小问题（建议 Table 2 caption 标注 compute cost）。\n\n3. **Greedy baseline 选择**（R1-W3）：R2 反驳——greedy 是 test-time scaling 文献标准 baseline（Snell et al. 2025, Wang et al. 2023, Brown et al. 2024）。**Director 判断**：R2 论点成立，不构成问题。\n\n4. **Capability-diversity tension 新颖性**：R1 认为 structured output 量化是新的，R2 认为增量有限。**Director 判断**：作为经验观察有价值，但不应 framed 为 central finding——Should-Fix。\n\n---\n\n## Questions\n\n**Q1** [R2] Correlation-selection gap 是否在任何非 NER 结构化预测任务中被验证过？\n\n**Q2** [R2] 为何没有直接实验 entity-level F1 作为 MBR utility function 的方案？概念上比 majority vote 更 principled。\n\n**Q3** [R2] Proposition 1 bound ratio 仅 0.13-0.63——是否考虑过基于 partial degeneracy 的连续 bound？\n\n**Q4** [R2] Figure 3 中 Few-NERD N=64 仍有正向增益，SciERC 几乎平坦——是否主要由 base model quality 驱动？更弱模型（3B/1B）是否会有更大 scaling gains？\n\n**Q5** [R1] SciERC 为何只用 1 个 training seed？是资源限制还是其他原因？\n\n---\n\n## Missing References\n\n- Conformal prediction for NLP structured outputs（近年多项工作将 conformal prediction 应用于 NER/序列标注的 uncertainty quantification）\n- Token-level uncertainty decomposition（如 Xiao et al. 2020 epistemic/aleatoric 分解）\n- Snell et al. (2025, ICLR) compute-optimal scaling 中关于 diminishing returns 的讨论\n- Entity-level F1 作为 MBR utility function 的 principled 版本（vs 当前的 majority vote）\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未启用。项目配置中 `external_review.paperreview_ai.enabled` 未设置为 true。\n\n---\n\n## Visual Layout Check（非评分项）\n\n状态：**done**（耗时约 4 分钟）\n\n| 严重度 | 位置 | 发现 |\n|--------|------|------|\n| warning | p.24 | 附录页面约 2/3 空白（Appendix n 结尾），建议调整 float/section break |\n| warning | p.17 | Figure 7 热力图使用红→绿色阶，对红绿色盲不友好，建议改 viridis 或 Blue→Orange |\n| warning | p.16 | Figure 6 校准图同样存在色盲友好性问题 |\n| warning | p.7 | 主文单页密度极高（Table 3 + Table 4 + Figure 4 + 两段文字），视觉上略拥挤 |\n| info | p.1 | 首页无视觉锚点，Figure 1 在 p.2，延迟可控 |\n| info | p.3 | 唯一纯文本页（信号定义），建议加小型 signal summary 表 |\n| info | p.14-47 | 附录 34 页极为详尽，关键附录建议主文显式指引 |\n| info | p.5 | Table 2 信息密度高但格式正确 |\n| info | p.6 | Figure 3 色彩区分度良好且色盲友好 |\n| info | p.47 | 末页空间利用合理（~85%） |\n\n无 critical 排版问题。色盲友好性（Figure 6, 7）建议修复。\n\n---\n\n## Overall Assessment\n\n**评分**: **3.5 — Borderline Conference**\n**置信度**: 4/5（两位 Reviewer 均熟悉 self-consistency 和 NER 领域文献）\n\n### 评分理由\n\n**支持 Conference (4.0) 的因素**：\n- Correlation-selection gap 是社区有价值的经验发现，命名并量化了此前模糊的现象\n- 诊断 cascade 有独立方法论价值，附带可复用的三步评估协议\n- 统计方法论（Holm-Bonferroni k=57、MDE、TOST）在 NLP 经验性论文中属上乘\n- 47 页附录体现极致的 thoroughness，几乎覆盖所有可预见的 reviewer 质疑\n- 诚实报告负面结果和方法局限性\n\n**限制 Conference 的因素**：\n- **[Critical]** 标题/Abstract 声称 \"structured prediction\" 但证据主要是 NER——scope-evidence gap 是最大问题\n- SciERC（最核心数据集）仅 1 training seed，统计可靠性不足\n- Capability-diversity tension 作为 central finding 形式化不足，且文献中已有隐含讨论\n- 核心贡献是诊断性的（\"what fails\"）而非建设性的（\"how to fix\"），prescriptive guidance 有限\n- Proposition 1 的理论贡献偏薄（independence 假设不成立，bound 过松）\n\n### 改进路径（Conference 4.0 所需）\n\n若作者能在 camera-ready 中完成以下修改，论文可达 Conference 水平：\n1. **[必须]** 限缩标题和 Abstract scope 为 NER/Information Extraction\n2. **[必须]** 补充 SciERC 多 seed 实验（或标记为 tentative）\n3. **[必须]** 修复页数溢出（压缩至 8 页正文）\n4. **[强烈建议]** 加强与 Yun & Price (2025) 的差异化论述\n5. **[建议]** 降级 capability-diversity tension 的 framing 或给出可操作定义\n\n当前版本适合 **Findings (3.0-3.5)**；scope 修正后为 **Borderline Conference (3.5-4.0)**。\n\n---\n\n## Detailed Comments\n\n### Section-by-Section\n\n**Abstract**: 第一句 \"structured prediction remains uncharacterized\" 过强，实际只 characterize 了 NER（和初步 RE）。建议改为 \"entity-level information extraction\" 或 \"set-valued NER outputs\"。\"Exploratory entity-level construction partially bypasses\" 中 \"partially\" 用词准确。\n\n**Section 1 (Introduction)**: Discover → Diagnose → Explore bypasses 三阶段叙事清晰。但 \"using NER...and RE as case studies\" 中 RE 的篇幅远不能称为 case study（Appendix 2 段 vs NER 的完整 pipeline）。\n\n**Section 2 (Diagnostic Framework)**: 五种信号的定义清晰。SJ 引用 Fleiss 1971 可能有误（Fleiss 是 inter-rater reliability，非 Soft Jaccard 来源）。Table 5 术语不一致（\"Soft Jaccard\" vs \"structural similarity\"）。建议 p.3 加小型 signal summary 表改善可浏览性。\n\n**Section 3 (How Self-Verification Fails)**: Introspection boundary 是有趣概念但后续很少复用——考虑去掉以减少 cognitive load，或在 Discussion 中回顾。\n\n**Section 4 (Where Single-Signal Selection Fails)**: 核心 section。Figure 2 双量纲共轴（AUROC vs ρ）初看混淆，建议分双轴。Table 1 caption \"paired bootstrap\" 但内容是 Spearman ρ，可能有误。\n\n**Section 5 (Adaptive Methods)**: Table 2 信息密度高。建议添加 compute cost 列（各方法相对于 greedy 的倍数），避免误导为等预算比较。\n\n**Section 6 (Threshold Regime Analysis)**: Proposition 1 的 \"entity selection diagnostic\" 方向性有用，但应在正文中明确标记为 illustrative upper bound（当前表述可能让读者误以为是 tight bound）。θ_crit=0.70 的 task-specificity 应讨论。\n\n**Section 7 (Experiments)**: 详尽。Few-NERD LP selection +1.39pp (p<0.001) 是论文最强的正面结果。Table 4 的 \"2-seed\" vs Section 7.1 \"3-seed\" 不一致应修复。\n\n**Section 8 (Related Work)**: 需扩展：补充 conformal prediction、token-level uncertainty、MBR with structural utility。与 Yun & Price (2025) 的差异化需从一句话扩展为 1-2 段。\n\n**Section 9 (Discussion and Conclusion)**: \"Central finding is a capability-diversity tension\" 需更强支撑或降级。Conclusion 段落溢出到 p.9——必须压缩。\n\n**Limitations**: 覆盖面广（correlational vs interventional、scope、seed、prompt template）。建议明确提及为何 SciERC 只用 1 seed。\n\n**Ethics Statement**: 基本合规。论文脚注已注明 \"No new human data was collected\"。",
    "reviewer_ids_acknowledged": "[\"1\", \"2\"]",
    "cross_response_reviewer_ids": "[\"1\", \"2\"]",
    "overall_score": "3.5"
  }
}
```

</details>

---


### Tool result

_source line 3797 · 2026-05-22T10:30:35.845274+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_1b56445332d8ca2b4964b30f300f0e00:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4419
}
```

</details>

---


### Tool call

_source line 3798 · 2026-05-22T10:30:45.461682+00:00_

called TodoWrite

<details open><summary>🔧 Tool call — TodoWrite</summary>

```json
{
  "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '完成资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.7: 派发视觉审查', 'status': 'completed', 'activeForm': '派发视觉审查 Agent'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': '收集 Reviewer 审稿意见'}, {'content': 'Step 2: 交叉分享', 'status': 'completed', 'activeForm': '完成交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'completed', 'activeForm': '判断收敛'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'completed', 'activeForm': '完成报告投递'}]"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "TodoWrite",
  "tool_args": {
    "todos": "[{'content': 'Step 0: 资料检查 + Venue 调研', 'status': 'completed', 'activeForm': '完成资料检查和 Venue 调研'}, {'content': 'Step 0.5: 决定 Reviewer 编排', 'status': 'completed', 'activeForm': '决定 Reviewer 编排方案'}, {'content': 'Step 0.7: 派发视觉审查', 'status': 'completed', 'activeForm': '派发视觉审查 Agent'}, {'content': 'Step 1: Round 1 独立审稿', 'status': 'completed', 'activeForm': '收集 Reviewer 审稿意见'}, {'content': 'Step 2: 交叉分享', 'status': 'completed', 'activeForm': '完成交叉分享'}, {'content': 'Step 3: 收敛判断', 'status': 'completed', 'activeForm': '判断收敛'}, {'content': 'Step 4: 汇总报告 & 投递', 'status': 'completed', 'activeForm': '完成报告投递'}]"
  }
}
```

</details>

---


### Tool result

_source line 3799 · 2026-05-22T10:30:45.512880+00:00_

Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "TodoWrite",
  "elapsed_ms": 51
}
```

</details>

---


### Assistant

_source line 3800 · 2026-05-22T10:30:55.020503+00:00_

**Round 35 审稿完成，报告已投递至 Research Director。**

汇总：
- **Overall**: 3.5 (Borderline Conference)，R1 和 R2 评分一致
- **1 个共识 Critical**：标题 "Structured Prediction" 超出 NER 实验证据范围
- **1 个分歧 Must-Fix**：SciERC 单 seed（R1 认为 critical，R2 认为 should-fix，Director 判为 must-fix 但不一票否决）
- **7 个 Should-Fix**：页数超限、capability-diversity tension 形式化不足、Yun & Price 差异化不充分、相关工作缺失、Proposition 1 independence 假设、free-form ablation 覆盖不全、cascade 阈值 task-specificity
- **核心优势**：correlation-selection gap 是有价值的经验贡献、统计方法论远超同行、47 页附录体现极致 thoroughness
- **改进路径**：限缩标题 scope + 补 SciERC 多 seed + 修复页数 → 可达 Conference (4.0)

Issue tracker 和视觉审查结果已同步纳入报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 285

## Round 285

2 recorded events


### User

_source line 3801 · 2026-05-22T10:30:57.718111+00:00_

[Reviewer 1 审稿结果]:
已完成对 Reviewer 2 全部意见的逐条回应并提交给 Director。核心判断：

- **N1 (Scope overclaim)**: AGREE — 与我的 N1 一致
- **N2 (Capability-diversity tension)**: REBUT 新颖性部分（structured output 的量化分析确实是新的），AGREE 形式化不足部分，建议降为 Should-Fix
- **W1 (页数超限)**: AGREE — 经核实 Section 9 确实溢出到 p.9
- **W2 (Yun & Price 差异化)**: AGREE
- **W3 (缺失相关工作)**: 部分 AGREE（conformal prediction 和 token-level uncertainty 应补充），部分 REBUT（MBR 已有讨论）
- **W4 (cascade 阈值 task-specificity)**: AGREE
- **W5 (Proposition 1 bound looseness)**: REBUT — bound 目的是方向性的，松弛不改变定性结论

维持 3.5 (Borderline Conference) 评分不变。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 3802 · 2026-05-22T10:31:08.348407+00:00_

Round 35 审稿已完成，报告已投递至 Research Director。

**最终结论：3.5 — Borderline Conference**

两位 Reviewer 独立评分一致（均 3.5），交叉分享后在所有关键问题上达成共识或明确记录分歧。1 轮即收敛，无需进入 Round 2。

**核心发现：**
- 1 个 Critical Must-Fix（scope overclaim：标题 "structured prediction" 但证据主要是 NER）
- 1 个争议 Must-Fix（SciERC 单 seed：R1 认为 critical，R2 认为 should-fix）
- 7 个 Should-Fix（页数超限、capability-diversity tension 形式化、Yun & Price 差异化、相关工作缺失、Proposition 1 bound、free-form ablation 覆盖、cascade 阈值泛化性）
- Issue tracker 已同步更新（`review_issues.yaml`）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director"
}
```

</details>

---


## Round 286

## Round 286

68 recorded events


### User

_source line 3803 · 2026-05-22T10:53:12.631419+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: struct_self_consist_ie
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Long Paper (ARR)
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 3804 · 2026-05-22T10:53:18.286237+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 3805 · 2026-05-22T10:53:18.337313+00:00_

1	---
2	name: review-director-session-start
3	description: Review Director session 启动初始化流程——圆桌多轮审稿协议。Review Director 角色 session 启动时自动使用。
4	priority: 9
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 3
11	roles:
12	- review_director
13	---
14	
15	# Review Director Session 启动流程（圆桌会议模式）
16	
17	## 初始化
18	
19	1. `director_get_project_overview(project)` — 了解研究现状（实验状态、最新报告）
20	2. 读取论文文件状态：检查 `projects/{project}/paper/` 或 `main.tex` 是否存在
21	3. 检查是否有来自 Research Director 的论文提交（`[论文提交]` 消息）
22	4. 向用户简要汇报：
23	   - **投稿目标**：venue 和 deadline
24	   - **论文状态**：当前草稿位置和版本
25	   - **资料完整性**：提交的材料是否齐全
26	   - **下一步**：即将开始的圆桌审稿流程
27	
28	## 评审流程（收到论文提交后执行）
29	
30	### Step 0 — 资料检查 + Venue 调研（必须先做，不可跳过）
31	
32	1. 检查提交资料完整性：论文文件是否存在、是否可读、补充材料是否齐全
33	2. 确认目标投稿 venue（从提交消息中获取）
34	3. 用 `web_search` 搜索该 venue 当前轮次的 CFP（Call for Papers），关键词示例：
35	   - `"&lt;venue name> 2026 call for papers" site:aclweb.org`
36	   - `"&lt;venue name> 2026 submission deadline"`
37	   - `"&lt;venue name> 2026 author guidelines"`
38	4. **验证 deadline 未过期**：今天日期与截止日期对比，若已过期立即通知用户，不继续
39	5. 提取当前版本的格式要求：
40	   - 页数限制（正文 / 附录 / 参考文献）
41	   - 模板（ACL / IEEE / NeurIPS / ICML / ...）
42	   - 匿名规则（double-blind / single-blind / open）
43	   - 附录规则（是否允许、是否参与审稿）
44	   - 引用格式（natbib / biblatex / 特定 .bst）
45	6. 将以上信息作为上下文，随任务一起传递给 Reviewer
46	
47	⚠️ 禁止使用训练知识中的 venue 要求——格式标准每年都会更新，必须实时搜索确认。
48	
49	### Step 0.5 — 决定 Reviewer 编排
50	
51	根据 venue 类型和论文特点，决定：
52	- 需要几个 Reviewer（1-5 人）
53	- 每个 Reviewer 的审查侧重
54	
55	参考：
56	- **顶会长文**（NeurIPS/ICML/ACL）：3 人（方法/实验 + novelty/related work + 格式/ethics）
57	- **一般会议**（EMNLP/NAACL）：2 人（方法严谨性 + 新颖性/完整性）
58	- **Workshop / 短文**：1 人（全面审查）
59	
60	向 Group C（即项目配置中的 `feishu.review_chat_id` 审稿群）汇报编排决定。
61	
62	### Step 0.6 — 外部审稿线（与 Step 1 并行）
63	
64	检查项目配置中 `external_review.paperreview_ai.enabled` 是否为 `true`：
65	- 如果启用：调用 `request_external_review(project, paper_pdf_path, venue)` 向用户群发送协助提交卡片
66	- 这一步与 Step 1（内部 Reviewer 分配）**并行执行**，不阻塞内部审稿流程
67	- 外部结果到达后（用户在群里粘贴），纳入 Step 4 最终报告
68	- 如果到 Ste
…[truncated 3286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 3806 · 2026-05-22T10:53:25.332904+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,request_external_review,dispatch_visual_check,director_post_to_reviewer,WebSearch,submit_review_report_to_research_director,get_external_review_status,get_visual_check_status,update_review_issues",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,request_external_review,dispatch_visual_check,director_post_to_reviewer,WebSearch,submit_review_report_to_research_director,get_external_review_status,get_visual_check_status,update_review_issues",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 3807 · 2026-05-22T10:53:25.333347+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 3808 · 2026-05-22T10:53:29.949729+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,read_project_file,request_external_review,dispatch_visual_check,director_post_to_reviewer,submit_review_report_to_research_director,get_external_review_status,get_visual_check_status,update_review_issues,read_local_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,read_project_file,request_external_review,dispatch_visual_check,director_post_to_reviewer,submit_review_report_to_research_director,get_external_review_status,get_visual_check_status,update_review_issues,read_local_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 3809 · 2026-05-22T10:53:29.950201+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 3810 · 2026-05-22T10:53:35.836743+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_local_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_local_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 3811 · 2026-05-22T10:53:35.937526+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 3812 · 2026-05-22T10:53:38.501479+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_local_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_local_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 3813 · 2026-05-22T10:53:38.552165+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 3814 · 2026-05-22T10:53:45.480307+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 3815 · 2026-05-22T10:53:46.886190+00:00_

{"result":"# 项目 struct_self_consist_ie 概况\n\n## 实验状态 (319 个)\n\n- **exp_002_ner_conll2003**: DONE (success) — \n- **exp_004_re_diagnostic**: DONE (success) — \n- **exp_005**: DONE (success) — \n- **exp_014_entity_majority_voting**: DONE (success) — \n- **exp_013_exact_match_voting**: DONE (negative) — \n- **exp_012_logprob_baseline**: DONE (success) — \n- **mvp_pilot_005**: DONE (negative) — \n- **e1_component_wise_re_sj**: DONE (negative) — \n- **mvp_pilot_004**: DONE (negative) — \n- **ft_002_v2**: DONE (success) — \n- **mvp_pilot_002**: DONE (failed) — \n- **ft_002**: DONE (killed) — \n- **ft_001**: DONE (success) — \n- **mvp_pilot_003**: DONE (negative) — \n- **mvp_pilot_001**: DONE (negative) — \n\n## 最新报告\n&lt;!-- AUTO-FACTS-BEGIN (generated 2026-05-22T10:37:00Z; do not edit — regenerated by auto_build_report_facts) -->\n## 📊 当前状态（auto-derived from registry）\n\n**总计**: 318 个实验 — DONE 295, PREPARING 19, QUEUED 1, RUNNING 3\n**DONE 分布**: failed 13, killed 35, negative 53, success 194\n\n### GPU 占用\n- **分配**: 8 张 — autodl-5090:cuda:0, autodl-5090:cuda:1, autodl-5090:cuda:2, autodl-5090:cuda:3, autodl-5090-c:cuda:0, autodl-5090-c:cuda:1, autodl-5090-c:cuda:2, autodl-5090-c:cuda:3\n- **实际运行**: 3 张 — autodl-5090-c:cuda:0(exp_fewnerd_mf4_s42), autodl-5090-c:cuda:2(exp_fewnerd_mf4_s456), autodl-5090-c:cuda:3(exp_fewnerd_pretrained_n32_s42)\n\n### 💾 磁盘余量\n- **autodl-5090**:\n  - `/autodl-pub`: 8.6T/14T 可用（已用 39%）\n  - `/autodl-pub/data`: 5.7T/10T 可用（已用 44%）\n  - `/usr/bin/nvidia-smi`: 813G/879G 可用（已用 3%）\n- **autodl-5090-c**:\n  - `/autodl-pub`: 6.4T/14T 可用（已用 55%）\n  - `/autodl-pub/data`: 18T/20T 可用（已用 9%）\n  - `/usr/bin/nvidia-smi`: 813G/879G 可用（已用 3%）\n\n### 🏃 RUNNING\n| exp_id | server | gpu | pid | log |\n|--------|--------|-----|-----|-----|\n| `exp_fewnerd_mf4_s42` | autodl-5090-c | cuda:0 | 426032 | `~/runs/struct_self_consist_ie/exp_fewnerd_mf4_s42.log` |\n| `exp_fewnerd_mf4_s456` | autodl-5090-c | cuda:2 | 426513 | `~/runs/struct_self_consist_ie/exp_fewnerd_mf4_
…[truncated 1777 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 1405
}
```

</details>

---


### Tool call

_source line 3816 · 2026-05-22T10:53:46.886540+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 3817 · 2026-05-22T10:53:47.338422+00:00_

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
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{amsthm}
16	\newtheorem{proposition}{Proposition}
17	\newtheorem{theorem}{Theorem}
18	\newtheorem{corollary}{Corollary}
19	\newtheorem{definition}{Definition}
20	\usepackage{multirow}
21	\usepackage{xcolor}
22	\usepackage{subcaption}
23	\usepackage{alphalph}
24	\usepackage{enumitem}
25	
26	\graphicspath{{figures/}}
27	
28	\title{When Does Test-Time Scaling Fail?\\ Boundary Conditions for Information Extraction}
29	
30	\author{Anonymous}
31	
32	\begin{document}
33	\maketitle
34	
35	\input{sections/abstract}
36	\input{sections/introduction}
37	\input{sections/diagnostic}
38	\input{sections/mechanistic}
39	\input{sections/single_signal}
40	\input{sections/adaptive}
41	\input{sections/theory}
42	\input{sections/experiments_main}
43	\input{sections/background}
44	\input{sections/discussion}
45	
46	\section*{Limitations}
47	\input{sections/limitations}
48	
49	\section*{Ethics Statement}
50	All experiments use publicly available benchmarks (SciERC, CoNLL-2003, Few-NERD, WNUT-17), open-weight models (Qwen3-8B, Qwen3-14B, Qwen3-4B, LLaMA-3.1-8B), and the GPT-5.5 API.
51	CoNLL-2003 is derived from the Reuters RCV1 corpus, which is available for research purposes under a NIST agreement; we use the standard research distribution.
52	No new human data was collected or annotated for this study.
53	Our findings on signal limitations could inform more reliable deployment of IE systems by guiding practitioners toward appropriate confidence signals for their use case.
54	Code and data will be released upon acceptance at [anonymized URL].
55	
56	\section*{Responsible NLP Research Checklist}
57	\input{sections/checklist}
58	
59	\bibliography{references}
60	
61
…[truncated 123 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 3818 · 2026-05-22T10:53:47.338962+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"
  }
}
```

</details>

---


### Tool call

_source line 3819 · 2026-05-22T10:53:47.740878+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 3820 · 2026-05-22T10:53:47.791841+00:00_

1	issues:
2	# ===== CRITICAL / MUST-FIX =====
3	- id: R35-N1
4	  summary: "Scope overclaim: 标题声称 'structured prediction' 但证据主要是 NER"
5	  category: framing
6	  severity: critical
7	  status: in_progress
8	  first_raised_round: 33
9	  last_seen_round: 35
10	  mentions:
11	    - round: 33
12	      reviewers: [1, 2]
13	      note: "R1-W4: RE/SQL 覆盖有限。当时为 warning。"
14	    - round: 34
15	      reviewers: [1, 2]
16	      note: "继续作为 warning。"
17	    - round: 35
18	      reviewers: [1, 2]
19	      note: "双方升级为 Critical Must-Fix。标题 'Boundary Conditions for Structured Prediction' 但充分实验仅 NER（4 数据集 × 2 模型家族）。RE 仅 SciERC 单数据集 exploratory（397 实例，1 模型），SQL 仅一句话。"
20	  action_items:
21	    - round: 35
22	      action: "标题改为 'Boundary Conditions for Information Extraction'；全文收窄 scope claims"
23	      assigned_to: paper_agent
24	      status: in_progress
25	  resolution: ""
26	  resolution_round: null
27	
28	- id: R35-N2
29	  summary: "SciERC 仅 1 个 training seed，统计可靠性不足"
30	  category: experiment
31	  severity: warning
32	  status: in_progress
33	  first_raised_round: 35
34	  last_seen_round: 35
35	  mentions:
36	    - round: 35
37	      reviewers: [1, 2]
38	      note: "共识：SciERC 分析最详尽但单 seed + 529 实例 power 有限。"
39	  action_items:
40	    - round: 35
41	      action: "Discussion 标记 SciERC 结论为 tentative + 尝试补 2 额外 seeds"
42	      assigned_to: paper_agent
43	      status: in_progress
44	    - round: 35
45	      action: "SciERC 额外 training seeds (s123, s456) 如 GPU 允许"
46	      assigned_to: agent
47	      status: in_progress
48	  resolution: ""
49	  resolution_round: null
50	
51	# ===== SHOULD-FIX =====
52	- id: R35-W1
53	  summary: "正文超出 8 页限制（Conclusion 溢出到 Page 9）"
54	  category: format
55	  severity: warning
56	  status: in_progress
57	  first_raised_round: 35
58	  last_seen_round: 35
59	  mentions:
60	    - round: 35
61	      reviewers: [1, 2]
62	      note: "Section 9 Discussion/Conclusion 延续到 p.9 顶部。EMNLP 2026：正文 8 页。"
63	  action_items:
64	    - round: 35
65	      action: "压缩 Rel
…[truncated 9233 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 3821 · 2026-05-22T10:53:53.161198+00:00_

Web search results for query: "EMNLP 2026 call for papers submission guidelines ARR site:aclweb.org"

Links: [{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"*SEM 2026: Commitment Link for ARR-Reviewed Papers (Deadline: 10 April 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/sem-2026-commitment-link-arr-reviewed-papers-deadline-10-april-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"The 64th Annual Meeting of the Association for Computational Linguistics - ACL 2026","url":"https://2026.aclweb.org/"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"EMNLP 2025: Call for System Demonstrations | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-call-system-demonstrations"},{"title":"Jan. 2025 ACL Standing Committee on Peer Review (COPR) Report 1","url":"https://www.aclweb.org/adminwiki/images/9/9e/COPR-5-cycle-report-to-publish.pdf"}]

I found search results related to EMNLP 2026 and ARR, though the results mostly focus on w
…[truncated 1163 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 5822
}
```

</details>

---


### Tool call

_source line 3822 · 2026-05-22T10:54:04.122394+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 submission guidelines page limit ARR commitment deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 submission guidelines page limit ARR commitment deadline"
  }
}
```

</details>

---


### Tool call

_source line 3823 · 2026-05-22T10:54:04.624410+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 May cycle submission deadline author guidelines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 May cycle submission deadline author guidelines"
  }
}
```

</details>

---


### Tool call

_source line 3824 · 2026-05-22T10:54:07.538588+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_round_36/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_NOT_FOUND\"",
  "description": "Check if submitted PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_round_36/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_NOT_FOUND\"",
    "description": "Check if submitted PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 3825 · 2026-05-22T10:54:07.790103+00:00_

-rw-r--r-- 1 ubuntu ubuntu 990112 May 22 10:51 /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/review_round_36/submitted.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 3826 · 2026-05-22T10:54:07.790521+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "paper_checklist.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "file": "paper_checklist.yaml"
  }
}
```

</details>

---


### Tool result

_source line 3827 · 2026-05-22T10:54:11.304494+00:00_

Web search results for query: "EMNLP 2026 submission guidelines page limit ARR commitment deadline"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"EMNLP 2026 2026 Deadlines — Submission, Rebuttal & Dates | Paperpin | Paperpin","url":"https://www.getpaperpin.com/deadlines/emnlp26"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"}]

Based on the search results, here's the information about EMNLP 2026 submission guidelines:

## Page Limits

The format is two-column with an 8-page limit for long papers and a 4-page limit for short papers. Additionally, final versions of accepted papers will be given one additional page of content (up to 9 pages for long papers, up to 5 pages for short papers) to address reviewers' comments.

## ARR Submission Deadline

The ARR submission deadline for long and short papers is May 25, 2026.

## ARR Commitment Deadline

The EMNLP commitmen
…[truncated 883 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 7182
}
```

</details>

---


### Tool result

_source line 3828 · 2026-05-22T10:54:12.460095+00:00_

Web search results for query: "ACL Rolling Review 2026 May cycle submission deadline author guidelines"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"}]

Based on the search results, here's information about the ACL Rolling Review 2026 May cycle:

## Submission Deadline

There is a submission deadline every two months, and the May 2026 cycle is the next upcoming submission cycle for ARR.

## Author Registration and Reviewer Requirements

After submission, all authors must complete the author registration form by May 27, 2026 EoD AoE (End of Day, Anywhere on Earth). Starting in May 2025, all submitting authors have
…[truncated 1041 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "WebSearch",
  "elapsed_ms": 7835
}
```

</details>

---


### Tool result

_source line 3829 · 2026-05-22T10:54:12.460584+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'struct_self_consist_ie'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 4670
}
```

</details>

---


### Tool call

_source line 3830 · 2026-05-22T10:54:27.431948+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 3831 · 2026-05-22T10:54:27.432410+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 3832 · 2026-05-22T10:54:30.796659+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/ -name \"*.tex\" -type f | sort",
  "description": "Find all tex files in paper directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/ -name \"*.tex\" -type f | sort",
    "description": "Find all tex files in paper directory"
  }
}
```

</details>

---


### Tool result

_source line 3833 · 2026-05-22T10:54:30.847278+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/_archived/experiments_OLD.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/adaptive.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/background.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/checklist.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/diagnostic.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments_main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/mechanistic.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/single_signal.tex
/home/ubuntu/.agent-ml-research-idea_gen_
…[truncated 185 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Bash",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 3834 · 2026-05-22T10:54:33.659832+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 3835 · 2026-05-22T10:54:34.011267+00:00_

1	\begin{abstract}
2	Test-time compute scaling---repeated sampling with self-consistency or best-of-$N$---yields large gains on discrete-answer reasoning, but whether these gains transfer to information extraction remains open.
3	Using named entity recognition (four datasets, primarily 7--14B fine-tuned; tentative cross-scale observations to 72B) as the primary case study and relation extraction as an exploratory extension, we characterize when test-time scaling succeeds and fails for set-valued outputs.
4	Quality estimation signals effectively predict output quality (AUROC up to $0.82$ across nine method categories), yet instance-level selection yields ${<}1$\,pp even at $N{=}64$, revealing a \textbf{correlation-selection gap}.
5	A diagnostic cascade identifies two boundary conditions: output convergence (degeneracy $12$--$68$\%) and signal alignment collapse ($\alpha{\to}0$), which jointly determine scaling returns.
6	Cross-task validation on RE reveals a distinct bottleneck---$40$\% zero-F1 from upstream errors rather than degeneracy---confirming task-specific failure modes.
7	Exploratory entity-level construction partially bypasses the sample-level bottleneck ($+1.40$\,pp where low degeneracy and signal alignment provide headroom).
8	The diagnostic cascade enables predicting test-time scaling failure before investing in repeated inference; the observed \textit{capability-diversity tension}---output convergence increasing with model capability---suggests a structural constraint for IE warranting investigation in other structured tasks.
9	\end{abstract}
10	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 3836 · 2026-05-22T10:54:34.162084+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 3837 · 2026-05-22T10:54:34.463451+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Test-time compute scaling---self-consistency \cite{wang2023selfconsistency}, best-of-$N$ \cite{snell2025scaling, brown2024monkeys}, extended reasoning \cite{muennighoff2025s1}---yields large gains on discrete-answer tasks where outputs admit equivalence classes or execution-based verification.
4	For NER, where outputs are entity sets with partial overlap, the boundary conditions for effective scaling are unknown; prior work \cite{yao2026consistency, yun2025price} provides initial observations but no systematic characterization of instance-level failure.
5	
6	Using NER (four datasets, primarily 7--14B fine-tuned; tentative cross-scale observations to 72B) and RE as case studies, we identify a \textbf{correlation-selection gap}: quality estimation signals predict output quality ($\rho$ up to $0.45$, AUROC $0.82$; Table~\ref{tab:quality_estimation}), yet selection fails---MV gains ${<}1$\,pp even at $N{=}64$ (Figure~\ref{fig:n_scaling}; Table~\ref{tab:selection}).
7	This gap decomposes into a definitional layer---four instance-level signals assign identical scores to all candidates---and an empirical one: LP, the only per-sample signal, also fails through within-instance compression (\S\ref{sec:selection_gap}).
8	A hidden-state probe confirms models encode entity quality internally (AUROC $0.63$\textendash$0.88$; \S\ref{sec:mechanistic}), exposing an \textit{introspection boundary} \cite{huang2024large}: the information exists but cannot be leveraged for selection.
9	A diagnostic cascade localizes the failure to two boundary conditions---output convergence (degeneracy $12$--$68$\%) and signal alignment collapse ($\alpha{\to}0$)---which jointly prevent selection, validated across nine methods and two model families (Table~\ref{tab:method_summary}).
10	The optimal strategy is dataset-dependent (LP: $+1.39$\,pp on Few-NERD; MV: $+0.61$\,pp on CoNLL at $N{=}64$), and RE reveals a distinct bottleneck ($40$\% zero-F1 from
…[truncated 2941 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 3838 · 2026-05-22T10:54:34.463822+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/diagnostic.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/diagnostic.tex"
  }
}
```

</details>

---


### Tool result

_source line 3839 · 2026-05-22T10:54:34.967362+00:00_

1	\section{Diagnostic Framework}\label{sec:method}
2	
3	Our analysis is observational: we characterize statistical associations between agreement signals and output quality without claiming causal mechanisms.
4	
5	\subsection{Problem Formulation}\label{sec:formulation}
6	
7	Given model $\mathcal{M}$ and input $x$, we sample $N$ outputs $\{y_1, \ldots, y_N\}$ at temperature $T > 0$ via constrained decoding \cite{willard2023guided}, where each $y_i$ is an entity set.
8	A \textbf{per-sample signal} $c_{\text{ps}}: (x, y_i) \to \mathbb{R}$ scores each output independently; an \textbf{instance-level signal} $c_{\text{il}}: (x, \{y_i\}_{i=1}^N) \to \mathbb{R}$ produces a single score per input (notation in Appendix~\ref{app:notation}).
9	This distinction is consequential: 4 of 5 signals are instance-level aggregates assigning identical scores to all $N$ candidates.
10	Only LP carries per-sample discriminative power: ensemble optimization assigns LP mean weight $0.78$, with structural signals receiving zero weight (Appendix~\ref{app:supervised_combination}).
11	When LP fails---as in few-shot regimes where LP $\rho{\to}0$ (\S\ref{sec:scaling})---no alternative per-sample signal exists.
12	
13	We define the \textbf{capability ceiling} as the practical performance upper bound achievable through self-consistency at realistic sample budgets ($N{\leq}16$), beyond which diminishing returns render further scaling impractical.
14	
15	\subsection{Confidence Signals}\label{sec:signals}
16	
17	Entity matching uses exact span and type match.
18	We distinguish two signal families: four \textit{agreement signals} computed across samples---\textit{structural} (Soft Jaccard [SJ], entity voting confidence [VC]) and \textit{surface} (exact match [EM], Fleiss' $\kappa$ [FK])---and log-probability [LP] as the sole \textit{model-internal} signal, derived from generation probabilities and providing per-sample discrimination.
19	
20	\paragraph{Log-probability (per-sample).}
21	$c_{\text{lp}}(y_i)
…[truncated 2151 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 3840 · 2026-05-22T10:54:34.967718+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/mechanistic.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/mechanistic.tex"
  }
}
```

</details>

---


### Tool result

_source line 3841 · 2026-05-22T10:54:35.870623+00:00_

1	\section{How Self-Verification Fails}\label{sec:mechanistic}
2	
3	The diagnostic cascade (\S\ref{sec:method}) identifies \textit{where} self-consistency fails; this section probes \textit{why} by testing whether models can self-verify at the entity level.
4	We evaluate self-verification and diagnostic probes on Qwen2.5-7B (a separate model family from the primary Qwen3-8B) fine-tuned for NER on Few-NERD ($N{=}8$, seed 42; full results in Appendix~\ref{app:self_verification}).
5	
6	\paragraph{Entity Self-Judgment (ESJ).}
7	For each extracted entity, we prompt the generating model: ``Is [\textit{entity}] a [\textit{type}] entity in this sentence?''
8	Entity-level AUROC is $0.512$---indistinguishable from chance---with P(yes$|$correct)${=}0.500$ and P(yes$|$incorrect)${=}0.500$.
9	ESJ-weighted construction degrades F1 to $0.711$ (vs.\ greedy $0.794$).
10	
11	\paragraph{Multi-Round Self-Consistency (MRSC).}
12	Following iterative self-refinement \cite{madaan2023selfrefine}, we re-prompt on disputed entities (agreement ${<}0.6$) with focused verification; P(yes) separation between gold and non-gold entities is $0.0006$ ($0.5003$ vs.\ $0.4997$).
13	MRSC best F1 ($0.763$) falls below greedy.
14	
15	\paragraph{Latent Self-Consistency (LSC).}
16	Mean-pooled final-layer hidden states ($d{=}3584$) provide per-sample latent representations.
17	Centroid selection ($0.759$) underperforms greedy ($0.794$); latent entity confidence ($0.839$) outperforms majority vote ($0.792$) but does not close the oracle gap ($0.882$).
18	
19	\paragraph{Hidden-state probe.}
20	A logistic regression on mean-pooled final-layer hidden states at entity spans achieves AUROC $0.636$ (Few-NERD), $0.882$ (CoNLL), $0.630$ (SciERC), evaluated with GroupKFold CV (5-fold ${\times}$ 3 seeds, groups${=}$source instance to prevent entity-level leakage; Appendix~\ref{app:hidden_probe}).
21	All three exceed ESJ ($0.51$); only CoNLL approaches frequency agreement ($0.868$).
22	Cross-dataset transfer is weak: lea
…[truncated 1062 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 902
}
```

</details>

---


### Tool call

_source line 3842 · 2026-05-22T10:54:35.871080+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/single_signal.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/single_signal.tex"
  }
}
```

</details>

---


### Tool result

_source line 3843 · 2026-05-22T10:54:36.373097+00:00_

1	\section{Where Single-Signal Selection Fails}\label{sec:selection_gap}
2	
3	\paragraph{Definitional vs.\ empirical.}
4	We decompose the correlation-selection gap into two layers.
5	The first is structural: four of five signals are instance-level aggregates that assign identical scores to all $N$ candidates from a given input (\S\ref{sec:formulation}), so they estimate quality across inputs but cannot rank candidates within an instance---selection failure is a design property, not an empirical finding.
6	The second layer is empirical and constitutes the core diagnostic: LP---the only per-sample signal---suffers compression under constrained decoding, with 60\% of SciERC instances showing within-instance LP range below 0.041 nats (Appendix~\ref{app:logprob_ties}), effectively eliminating the variation needed for sample discrimination. Even where LP varies, selection gains depend on LP-quality alignment rather than degeneracy alone.
7	Cross-instance $\rho$ (Table~\ref{tab:quality_estimation}) is attenuated by varying instance difficulty; within-instance $\rho$ directly measures whether LP discriminates candidates for a fixed input, making it the relevant predictor of selection success.
8	
9	\begin{table}[t]
10	\centering
11	\small
12	\caption{Best-of-$N$ selection (macro F1) on SciERC ($N{=}8$, $T{=}1.0$). Selection signals: 2-seed mean${\pm}\sigma$; baselines: 3-seed (Oracle${=}0.781$, Greedy${=}0.667$). LP is per-sample; others use consensus-proximity. $^\dagger$One score per input.}
13	\label{tab:selection}
14	\begin{tabular}{lcc}
15	\toprule
16	Method & NER F1 & $p$ \\
17	\midrule
18	Oracle & $0.775 \pm 0.001$ & --- \\
19	Greedy ($T{=}0$) & $0.645 \pm 0.001$ & --- \\
20	\midrule
21	LP           & $\mathbf{0.647} \pm 0.005$ & .29 \\
22	SJ           & $0.646 \pm 0.002$ & .67 \\
23	FK           & $0.646 \pm 0.001$ & .79 \\
24	EM           & $0.637 \pm 0.001$ & n/a$^\dagger$ \\
25	VC           & $0.623 \pm 0.004$ & n/a$^\dagger$ \\
26	\midrule
27	Random       & $0.61
…[truncated 2668 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 3844 · 2026-05-22T10:54:36.373591+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/adaptive.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/adaptive.tex"
  }
}
```

</details>

---


### Tool result

_source line 3845 · 2026-05-22T10:54:36.830613+00:00_

1	\section{Adaptive Methods}\label{sec:adaptive}
2	
3	Since instance-level selection fails (\S\ref{sec:selection_gap}), we present approaches that extract value from multi-sample generation beyond single-signal sample ranking.
4	Table~\ref{tab:method_summary} summarizes all 9 method categories evaluated; only cross-model ensembles yield an unconditional positive result.
5	
6	\begin{table}[t]
7	\centering
8	\small
9	\caption{Summary of 9 method categories tested (including MV baseline, LP selection, and cross-model ensemble beyond the seven verification methods in \S\ref{sec:mechanistic}--\S\ref{sec:adaptive}). $\Delta$F1 vs.\ greedy; dataset in parentheses. Full coverage in Appendix~\ref{app:method_coverage}.}
10	\label{tab:method_summary}
11	\resizebox{\columnwidth}{!}{%
12	\begin{tabular}{@{}llrl@{}}
13	\toprule
14	Category & Method & $\Delta$F1 / metric & § \\
15	\midrule
16	Freq.\ voting & MV & baseline & \ref{sec:prescriptive} \\
17	LP selection & Best-of-$N$ (LP) & $+1.39$\,pp (FN)$^\dagger$ & \ref{sec:selection_gap} \\
18	Self-verif.\ (prompt) & ESJ & AUROC $0.51$ & \ref{sec:mechanistic} \\
19	Multi-round refine. & MRSC & $-3.1$\,pp (FN) & \ref{sec:mechanistic} \\
20	Latent aggregation & LSC & $-3.5$\,pp (FN) & \ref{sec:mechanistic} \\
21	Adaptive gating & DALS & $+0.71$\,pp (SciERC)$^\ddagger$ & App.~\ref{app:dals} \\
22	Supervised verifier & LGB & $+0.30$\,pp (OOF) & \ref{sec:verifier} \\
23	Sup.\ combination & LR/MLP/RF & $-0.4$ to $-3.1$\,pp & App.~\ref{app:supervised_combination} \\
24	Cross-model & Qwen$+$LLaMA & $\mathbf{+0.42}$\,pp (FN) & \ref{sec:cross_model} \\
25	\bottomrule
26	\end{tabular}}
27	{\footnotesize $^\dagger$Few-NERD only; SciERC $+0.2$\,pp ($p{=}0.29$). $^\ddagger$Seed-sensitive ($\sigma{=}0.48$\,pp).}
28	\end{table}
29	
30	\subsection{Cross-Model Self-Consistency}\label{sec:cross_model}
31	
32	Mixing samples from architecturally distinct models can partially bypass within-model degeneracy.
33	Combining 4 samples each from Qwen3-8B and
…[truncated 764 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 457
}
```

</details>

---


### Tool call

_source line 3846 · 2026-05-22T10:54:36.831113+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/theory.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/theory.tex"
  }
}
```

</details>

---


### Tool result

_source line 3847 · 2026-05-22T10:54:37.132472+00:00_

1	\section{Threshold Regime Analysis}\label{sec:theory_scaling}
2	
3	\subsection{Entity Construction as MBR Decoding}\label{sec:mbr_theory}
4	
5	Entity-level construction selects $\hat{y}_{\textup{MBR}} = \{e \in E_\cup : \hat{p}(e) > \alpha/(\alpha{+}1)\}$ under balanced set-overlap utility; $\alpha{=}1$ recovers majority vote (Proposition~\ref{prop:construction_mbr}; Table~\ref{tab:entity_construction}; Appendix~\ref{app:mbr_proof}).
6	Signal-derived weights $w_i$ yield quality-weighted MBR: $\hat{p}_w(e) = \sum_{i} w_i \, \mathbf{1}[e {\in} y_i] / \sum_{i} w_i$; weighting improves when $w_i$ correlates with instance quality but degrades otherwise (LP on SciERC: $\rho{\approx}0.2$; \S\ref{sec:prescriptive}).
7	We select $\varepsilon{=}0.05$ at the elbow of the compression curve, where LP-best selection advantage transitions from $+1.5$\,pp (compressed) to $+4.6$\,pp (non-compressed; Appendix~\ref{app:fewnerd_epsilon}).
8	
9	\subsection{Scaling and Inverse Scaling}\label{sec:scaling}
10	
11	Oracle F1 follows $F_1(N) = a - b \cdot N^{-c}$ ($R^2 > 0.999$; Figure~\ref{fig:oracle_scaling}): Few-NERD ($c{\approx}0.61$) scales comparably to reasoning tasks \cite{brown2024monkeys}, SciERC converges more slowly ($c{\approx}0.35$), yet confidence-based aggregation recovers ${<}1$\,pp---a persistent gap.
12	The gap persists across scales and families: scaling from 8B to 14B FT increases oracle headroom ($+1.2$\,pp) with minimal greedy gain ($+0.9$\,pp), and GPT-5.5 (200 Few-NERD instances, zero-shot) exhibits the same pattern---50\% degeneracy, SJ $\rho{=}0.346$, MV $+1.4$\,pp yet 6.8\,pp oracle headroom unrealized.\footnote{Of the 10.1\% of GPT-5.5 samples producing empty entity sets, 88\% correspond to gold-empty instances; true parse failures affect only 1.2\% of samples (19/1{,}600) and shift all reported metrics by ${<}0.5$\,pp. See Appendix~\ref{app:frontier_sc}.}
13	Degeneracy is model-family-dependent rather than scale-dependent (Qwen2.5: $31.7$--$46.2$\% vs.\ Qwen3:
…[truncated 3691 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 3848 · 2026-05-22T10:54:37.233183+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments_main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments_main.tex"
  }
}
```

</details>

---


### Tool result

_source line 3849 · 2026-05-22T10:54:37.283895+00:00_

1	\section{Experiments}\label{sec:experiments}
2	
3	\subsection{Experimental Setup}\label{sec:setup}
4	
5	\paragraph{Datasets.}
6	We evaluate on four English NER benchmarks spanning a difficulty gradient.
7	\textbf{SciERC} \cite{luan2018scierc} (551 test instances, 6 entity types) is the primary medium-difficulty test bed (${\approx}$65\% F1).
8	\textbf{Few-NERD} \cite{ding2021fewnerd} (INTRA coarse; 37{,}648 instances, 8 entity types, ${\approx}$75\% F1) provides a low-degeneracy contrast where LP selection succeeds (\S\ref{sec:selection_gap}).
9	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} (3{,}453 test sentences, 4 entity types, ${\approx}$91\% F1) serves as a ceiling-effect control.
10	\textbf{WNUT-17} \cite{derczynski2017wnut} (1{,}287 social media instances, 51\% zero F1) probes the signal-collapse boundary.
11	
12	\paragraph{Models and sampling.}
13	\textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are LoRA fine-tuned using LLaMA Factory \cite{zheng2024llamafactory} (Appendix~\ref{app:training}; Few-NERD uses 3 epochs vs.\ 5 for others; Appendix~\ref{app:epoch_confound}).
14	$N{=}8$ samples at $T{=}1.0$ (primary) with vLLM constrained decoding \cite{willard2023guided}; $N {\in} \{16, 32, 64\}$ for scaling (Figure~\ref{fig:n_scaling}; Appendix~\ref{app:n_scaling}).
15	
16	\begin{figure}[t]
17	\centering
18	\includegraphics[width=\columnwidth]{figures/fig_n_scaling_mv.pdf}
19	\caption{MV $\Delta$F1 vs.\ $\log_2 N$ across three datasets (Qwen3-8B FT, seed${=}42$). Dotted gray: $\Delta{=}0$. Gains are dataset-dependent: persistently negative on Few-NERD, near zero on SciERC at higher $N$, marginally positive on CoNLL ($+0.6$\,pp at $N{=}64$).}
20	\label{fig:n_scaling}
21	\end{figure}
22	
23	%% ============================================================
24	\subsection{Quality Estimation Results}\label{sec:qe_results}
25	
26	\begin{table*}[t]
27	\centering
28	\small
29	\caption{NER quality estimation ($\rho$ and AUROC; $N{=}8$, primary seed${=}42$; 3-seed $
…[truncated 7619 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 3850 · 2026-05-22T10:54:41.649264+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/background.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/background.tex"
  }
}
```

</details>

---


### Tool result

_source line 3851 · 2026-05-22T10:54:42.001201+00:00_

1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Test-time compute scaling.}
4	Self-consistency \cite{wang2023selfconsistency} and best-of-$N$ \cite{snell2025scaling, brown2024monkeys} drive large gains on reasoning and code \cite{chen2021codex}.
5	Reward-free selectors \cite{taubenfeld2025cisc, kang2025selfcertainty}, BoN scaling laws \cite{gao2023scaling}, and trained verifiers \cite{cobbe2021verifiers, lightman2024verify} target discrete-answer settings; NER requires different aggregation because degeneracy operates at the entity-set level.
6	
7	\paragraph{SC failure modes.}
8	\citet{chen2023twofailures} identify SC failures where consistent outputs are wrong; free-form \cite{chen2024usc} and atomic \cite{thirukovalluru2024atomic} SC variants face limits where sub-output agreement does not yield selection gain (\S\ref{sec:selection_gap}).
9	
10	\paragraph{Consistency for structured IE.}
11	\citet{yao2026consistency} show task-level QE correlation ($\rho$ up to 0.47) for NER/RE; \citet{xie2023zeroshot} propose entity voting for zero-shot NER and \citet{xie2024selfimproving} report positive SC where zero-shot diversity is high.
12	\paragraph{Uncertainty estimation and MBR.}
13	Our selection instantiates MBR decoding \cite{eikema2022sampling, denero2009fast}; despite success in translation \cite{freitag2022high} and code \cite{jinnai2024mbr}, all variants fail due to instance degeneracy (Appendix~\ref{app:mbr_connection}).
14	\citet{eikema2025structured} find MBR utilities degrade on structured outputs; our cascade localizes this to degeneracy and LP compression (\S\ref{sec:selection_gap}).
15	LP is well-calibrated at population level (ECE $0.069$--$0.096$) but too compressed within instances for selection \cite{kadavath2022language, tian2023calibration}.
16	
17	\paragraph{Capability ceiling vs.\ diversity collapse.}\label{sec:yun_contrast}
18	\citet{yun2025price} identify \textit{diversity collapse} under constrained decoding for discrete answers (Table~
…[truncated 971 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 3852 · 2026-05-22T10:54:42.001733+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 3853 · 2026-05-22T10:54:43.106097+00:00_

1	\section{Discussion and Conclusion}\label{sec:discussion}\label{sec:selection_method}\label{sec:conclusion}
2	
3	\paragraph{Why test-time scaling fails for NER.}
4	For discrete-answer reasoning, sample diversity reflects diverse reasoning paths; for NER, output convergence (degeneracy $12$--$68$\%) eliminates candidate diversity while signal alignment collapse ($\alpha{\to}0$) prevents ranking---a \textit{capability-diversity tension} observed across model families (5.5--74\%; Table~\ref{tab:frontier_sc_cross}) and scales (4B--72B; \S\ref{sec:scaling}).
5	A free-form decoding ablation confirms degeneracy is model-intrinsic: CoNLL free-form degeneracy is $59.3$\% versus $56.7$\% constrained ($\Delta{=}2.6$\,pp; Appendix~\ref{app:freeform_ablation}).
6	
7	\paragraph{Practical implications.}
8	The cascade provides a pre-deployment diagnostic: measure degeneracy and LP-F1 alignment with $N{=}8$ samples before investing in $N{\times}$ inference; when degeneracy exceeds $\theta_{\text{crit}}{=}0.70$, aggregation is unlikely to help.
9	Cascade thresholds are empirically stable across our NER datasets but may require task-specific calibration; SciERC conclusions are tentative ($n{=}529$, single seed).
10	These findings are validated on 7--14B fine-tuned NER; generalization to broader IE, parsing, and code generation requires dedicated investigation.
11	
12	\paragraph{Conclusion.}
13	We characterize when test-time scaling fails for NER, with exploratory RE and SQL extensions.
14	The diagnostic cascade---localizing failure to output convergence and signal alignment collapse---is our primary contribution; the capability-diversity tension likely extends beyond NER but requires further validation.
15	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 1104
}
```

</details>

---


### Tool call

_source line 3854 · 2026-05-22T10:54:43.206948+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 3855 · 2026-05-22T10:54:43.508493+00:00_

1	Our primary evidence is from NER (four English datasets, 7--14B fine-tuned); the RE extension ($n{=}397$, single dataset) and SQL pilot ($n{=}196$) are exploratory. SciERC results are tentative ($n{=}529$, single training seed). Frontier models exhibit markedly different degeneracy profiles (5.5--74\%; Table~\ref{tab:frontier_sc_cross}), suggesting findings from fine-tuned open-weight models may not fully generalize to proprietary systems.
2	Our cascade is diagnostic, not causal: stages resist decomposition into independent effects ($R^2{<}0$; \S\ref{sec:selection_gap}). Under global Holm--Bonferroni ($k{=}57$), the most liberal core claim reaches $p_{\text{HB}}{=}0.055$; under BH FDR, $19/57$ tests are significant at FDR${<}0.05$ including $6/10$ construction comparisons (Appendix~\ref{app:holm}).
3	We evaluate at $N{\in}\{2,\ldots,64\}$; entity-level construction requires $N{\times}$ inference cost for modest gains ($+1$--$1.4$\,pp). We use a single prompt template per task; prompt variations may affect entity recall, degeneracy, and LP distributions.
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 3856 · 2026-05-22T10:54:43.709617+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/checklist.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/checklist.tex"
  }
}
```

</details>

---


### Tool result

_source line 3857 · 2026-05-22T10:54:43.760476+00:00_

1	% Responsible NLP Research Checklist
2	% Following the ACL Rolling Review guidelines:
3	% https://aclrollingreview.org/responsibleNLPresearch/
4	
5	\subsection*{A\hspace{0.5em} For Every Submission}
6	
7	\begin{enumerate}
8	\item[A1.] \textbf{Did you discuss the limitations of your work?}\\
9	Yes. See the Limitations section after the Conclusion.
10	
11	\item[A2.] \textbf{Did you discuss any potential risks of your work?}\\
12	Yes. See the Ethics Statement. This work analyzes existing confidence signals for NER and identifies when they fail; the findings reduce risk of deploying unreliable confidence-based selection in production systems. No dual-use concerns.
13	
14	\item[A3.] \textbf{Do the abstract and introduction summarize the paper's main claims?}\\
15	Yes. The Abstract and Section~\ref{sec:introduction} (3 enumerated contributions) summarize all main claims with supporting evidence pointers.
16	\end{enumerate}
17	
18	\subsection*{B\hspace{0.5em} Did you use or create scientific artifacts?}
19	
20	Yes. We use existing datasets and pre-trained models.
21	
22	\begin{enumerate}
23	\item[B1.] \textbf{Did you cite the creators of artifacts you used?}\\
24	Yes. All datasets are cited: SciERC \cite{luan2018scierc}, CoNLL-2003 \cite{tjongkimsang2003conll}, Few-NERD \cite{ding2021fewnerd}, WNUT-17 \cite{derczynski2017wnut}. Models: Qwen3-8B/4B and LLaMA-3.1-8B-Instruct. Training framework: LLaMA Factory \cite{zheng2024llamafactory}. Constrained decoding: XGrammar \cite{dong2024xgrammar}. See Sections~\ref{sec:introduction}, \ref{sec:evaluation}, and Appendix~\ref{app:training}.
25	
26	\item[B2.] \textbf{Did you discuss the license or terms for use and/or distribution of any artifacts?}\\
27	Partially. The Ethics Statement notes that CoNLL-2003 is derived from the Reuters RCV1 corpus, available under a NIST agreement for research. SciERC, Few-NERD, and WNUT-17 are publicly available research benchmarks. Qwen3 and LLaMA-3.1 are open-weight models released under their r
…[truncated 4168 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 3858 · 2026-05-22T10:54:44.664625+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 3859 · 2026-05-22T10:54:45.267181+00:00_

File content (65864 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "Read",
  "elapsed_ms": 602
}
```

</details>

---


### Tool call

_source line 3860 · 2026-05-22T10:55:10.769177+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "decisions.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "struct_self_consist_ie",
    "file": "decisions.yaml"
  }
}
```

</details>

---
