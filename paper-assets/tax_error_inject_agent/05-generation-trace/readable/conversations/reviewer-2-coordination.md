# Reviewer 2 coordination

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 110
- **Recorded user turns:** 4
- **Tool calls:** 51
- **Original source:** `logs/chats/feishu_group_oc_8acbea284219b548bfc4c50949ea43a8_reviewer_2.jsonl`
- **Structured JSON:** [`bd818683e918eae588d5.json`](../../sessions/bd/bd818683e918eae588d5.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

62 recorded events

### User

_source line 1 · 2026-05-15T07:13:27.343773+00:00_

[Round 1 审稿请求]:
## Round 1 审稿任务 — Reviewer 2

**你的审查侧重：新颖性 + Framing + Related Work + 写作/格式合规**

### 论文信息
- **标题**: "When Does Error Injection Help LLM Agents? Boundary Conditions from a Failed Transfer to Embodied Planning"
- **文件路径**: `projects/tax_error_inject_agent/docs/paper/main.tex`（主文件，子文件在同目录）
- **附录**: `projects/tax_error_inject_agent/docs/paper/appendix.tex`
- **已编译 PDF 截图**: `projects/tax_error_inject_agent/docs/paper/_pdf_images/main_p1.png` ~ `main_p7.png`

### Venue 信息
- **目标 venue**: Insights from Negative Results in NLP @ EMNLP 2026
- **地点**: Budapest, Hungary, Oct 22-29, 2026
- **Deadline**: TBD (~Aug 2026)，CFP 尚未发布
- **格式**: ACL 两栏格式，短文 ≤ 4 页（不含 references）
- **匿名规则**: Double-blind，作者信息必须匿名
- **Appendix**: 允许，但审稿人无义务审阅

### 你的审查重点

请重点审查以下方面：

1. **新颖性评估**：
   - 相对于 PALADIN（taxonomy-guided error injection for tool-use）、AgentDebug（ALFWorld 5-dim error taxonomy）、ETO/EEF/AgentHER 等，本文的差异化贡献是什么？
   - "negative result + boundary conditions" 的贡献是否足够？对于 Insights from Negative Results workshop 来说是否 well-scoped？
   - 三个 boundary conditions 是否真正新颖，还是已有文献的直接推论？

2. **Framing 和叙事**：
   - 论文的核心 claim 是什么？framing 是否一致贯穿全文？
   - Title/abstract/intro/conclusion 的信息传递是否准确反映实验结果？
   - "failed transfer" 的 framing 是否公平——是否存在方法设计缺陷（如缺少 recovery pairing）导致的 false negative？

3. **Related Work 完整性**：
   - 是否遗漏了重要相关工作？特别是：
     - ALFWorld 上的其他 training-time 方法
     - Negative results 文献中的 methodological precedents
     - Error injection / adversarial training 在 embodied AI 的工作
   - 引用格式是否符合 ACL natbib 要求？

4. **写作质量和格式合规**：
   - 页数是否符合 ≤ 4 页（不含 references）限制？从 PDF 看主体文本约几页？
   - 语言是否清晰、简洁？有无冗余或歧义表述？
   - 图表标注是否完整？Table/Figure 的 caption 是否自解释？
   - 匿名是否彻底（无 self-citation 泄露、无 GitHub 链接等）？
   - References 格式是否一致？是否有 arXiv preprint 应替换为正式出版版本的情况？

请输出完整审稿意见，按 Strengths / Weaknesses / Questions / Minor Issues 组织。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-15T07:13:39.923988+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-15T07:13:41.685448+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/.claude/sessions/review_reviewer_2_f8f885b0.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1761
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-15T07:13:41.786347+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references,WebSearch,WebFetch",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references,WebSearch,WebFetch",
    "max_results": "5"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-15T07:13:41.786790+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-15T07:13:48.782866+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR review form criteria 2026 reviewer guidelines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR review form criteria 2026 reviewer guidelines"
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-15T07:13:49.285244+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 Insights from Negative Results workshop CFP reviewer guidelines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 Insights from Negative Results workshop CFP reviewer guidelines"
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-15T07:13:51.799188+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-15T07:13:51.849858+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	% \usepackage{inconsolata}
11	\usepackage{graphicx}
12	\usepackage{amsmath}
13	\usepackage{booktabs}
14	\usepackage{enumitem}
15	\usepackage{amssymb}
16	\usepackage{pifont}
17	
18	\newcommand{\cmark}{\ding{51}}
19	\newcommand{\xmark}{\ding{55}}
20	
21	\title{When Does Error Injection Help LLM Agents? \\ Boundary Conditions from a Failed Transfer to Embodied Planning}
22	
23	\author{Anonymous}
24	
25	\begin{document}
26	\maketitle
27	
28	\input{abstract}
29	
30	\input{introduction}
31	
32	\input{method}
33	
34	\input{experiments}
35	
36	\input{analysis}
37	
38	\input{discussion}
39	
40	\input{related_work}
41	
42	\input{conclusion}
43	
44	\bibliography{references}
45	
46	\input{appendix}
47	
48	\end{document}
49	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-15T07:13:52.151216+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/docs/paper",
  "project": "tax_error_inject_agent"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/docs/paper",
    "project": "tax_error_inject_agent"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-15T07:13:56.970803+00:00_

Web search results for query: "ACL ARR review form criteria 2026 reviewer guidelines"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ACLRollingReview (@ReviewAcl) / Posts / X","url":"https://x.com/ReviewAcl"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"}]

Based on the web search results, here's information about the ACL ARR review form criteria and 2026 reviewer guidelines:

## Review Form Criteria

The review form asks for the major reasons to publish a paper at a selective *ACL venue, which could include novel and useful methodology, insightful empirical results or t
…[truncated 1552 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8187
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-15T07:13:59.582403+00:00_

Web search results for query: "EMNLP 2026 Insights from Negative Results workshop CFP reviewer guidelines"

Links: [{"title":"CFP | Insights 2024","url":"https://insights-workshop.github.io/2021/cfp/"},{"title":"Insights 2024 | Workshop on Insights from Negative Results in NLP","url":"https://insights-workshop.github.io/"},{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"EMNLP: Empirical Methods in Natural Language Processing 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=883"},{"title":"Workshop on Insights from Negative Results | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-insights-negative-results"},{"title":"Call For Papers: The Second Workshop on Insights from Negative Results (EMNLP 2021) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-second-workshop-insights-negative-results-emnlp-2021"},{"title":"MINT 2026 : EMNLP Workshop on Multimodal Interaction in Face-to-Face Dialogue","url":"http://www.wikicfp.com/cfp/servlet/event.showcfp?eventid=194269&copyownerid=320"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in Natural Language Processing","url":"http://www.wikicfp.com/cfp/servlet/event.showcfp?copyownerid=90704&eventid=192857"},{"title":"CFP | Insights 2020","url":"https://insights-workshop.github.io/2020/cfp/"}]

Let me search for more specific information about reviewer guidelines for the 2026 workshop.

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"CFP | Insights 2024","url":"https://insights-workshop.git
…[truncated 4565 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 10297
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-15T07:14:18.064884+00:00_

{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 20, \"total_citations\": 21, \"unique_cited_keys\": 13, \"orphan_bib\": 7, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 15, \"online_not_found\": 3, \"online_mismatch\": 2}, \"cross_check\": {\"orphan_bib\": [\"bengio2009curriculum\", \"damour2022underspecification\", \"madry2018adversarial\", \"mccoy2020seeds\", \"mosbach2021stability\", \"rolnick2017robust\", \"ye2025mixing_laws\"], \"missing_bib\": [], \"orphan_count\": 7, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"rolnick2017robust\", \"type\": \"article\", \"title\": \"Deep Learning is Robust to Massive Label Noise\", \"authors\": \"Rolnick, D. and Veit, A. and Belongie, S. and Shavit, N.\", \"year\": \"2017\", \"venue\": \"arXiv preprint arXiv:1705.10694\"}, {\"key\": \"wang2024learning_from_failure\", \"type\": \"article\", \"title\": \"Learning From Failure: Integrating Negative Examples when Fine-tuning Large Language Models as Agents\", \"authors\": \"Wang, R. and Li, H. and Han, X. and Zhang, Y. and Baldwin, T.\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2402.11651\"}, {\"key\": \"song2024eto\", \"type\": \"inproceedings\", \"title\": \"Trial and Error: Exploration-Based Trajectory Optimization for LLM Agents\", \"authors\": \"Song, Y. and Yin, D. and Yue, X. and Huang, J. and Li, S. and Lin, B. Y.\", \"year\": \"2024\", \"venue\": \"Proceedings of the Annual Meeting of the Association for Computational Linguisti...\"}, {\"key\": \"paladin2025\", \"type\": \"article\", \"title\": \"PALADIN: Self-Correcting Language Model Agents to Cure Tool-Failure Cases\", \"authors\": \"Vuddanti, S. V. and Shah, A. and Chittiprolu, S. K. and Song, T. and Dev, S. and...\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2509.25238\"}, {\"key\": \"agentHER2025\", \"type\": \"article\", \"title\": \"AgentHER: Hindsight Experience Replay for LLM Agent Trajectory Relabeling\", \"authors\": \"Ding, L.
…[truncated 13437 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 25913
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-15T07:14:26.598775+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form: all review dimensions/criteria, their rating scales, and descriptions. List every scored dimension with its scale."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form: all review dimensions/criteria, their rating scales, and descriptions. List every scored dimension with its scale."
  }
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-15T07:14:28.512850+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/docs/paper"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-15T07:14:29.567393+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/docs/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/docs/paper/analysis.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/docs/paper/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/docs/paper/conclusion.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 1054
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-15T07:14:29.619733+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/docs/paper/_pdf_images/main_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/docs/paper/_pdf_images/main_p1.png"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-15T07:14:30.424318+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 804
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-15T07:14:30.426045+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/docs/paper/_pdf_images/main_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/docs/paper/_pdf_images/main_p2.png"
  }
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-15T07:14:30.929221+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/docs/paper/_pdf_images/main_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/docs/paper/_pdf_images/main_p3.png"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-15T07:14:31.536239+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1110
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-15T07:14:31.536701+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/docs/paper/_pdf_images/main_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/docs/paper/_pdf_images/main_p4.png"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-15T07:14:31.939209+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1009
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-15T07:14:31.939718+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/docs/paper/_pdf_images/main_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/docs/paper/_pdf_images/main_p5.png"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-15T07:14:32.845734+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1309
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-15T07:14:32.847269+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 907
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-15T07:14:32.847642+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/docs/paper/_pdf_images/main_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/docs/paper/_pdf_images/main_p6.png"
  }
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-15T07:14:33.149110+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/docs/paper/_pdf_images/main_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/docs/paper/_pdf_images/main_p7.png"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-15T07:14:33.153877+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 4
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-15T07:14:33.455916+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 608
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-15T07:14:34.560513+00:00_

# ACL Rolling Review Form - Complete Review Dimensions

## Scored Dimensions with Rating Scales

### 1. **Reviewer Confidence**
Scale: 1-5
- 5: "Positive that my evaluation is correct"
- 4: "Quite sure" with unlikely missed details
- 3: "Pretty sure" but possible oversights
- 2: Willing to defend evaluation despite likely gaps
- 1: Outside expertise or incomprehensible paper

### 2. **Soundness**
Scale: 1-5 (with .5 increments)
- 5: "Excellent: This study is one of the most thorough"
- 4: "Strong: This study provides sufficient support"
- 3: "Acceptable: sufficient support for main claims"
- 2: "Poor: Some main claims not sufficiently supported"
- 1: "Major Issues: not sufficiently thorough to warrant publication"

### 3. **Excitement**
Scale: 1-5 (with .5 increments)
- 5: "Highly Exciting: I would recommend this paper"
- 4: "Exciting: I would mention this paper to others"
- 3: "Interesting: I might mention some points"
- 2: "Potentially Interesting: does not resonate with me"
- 1: "Not Exciting: does not resonate with me"

### 4. **Overall Assessment**
Scale: 1-5 (with .5 increments)
- 5: "Consider for Award" (top 2.5% papers)
- 4: "Conference: could be accepted"
- 3: "Findings: could be accepted to Findings"
- 2: "Resubmit next cycle: needs substantial revisions"
- 1: "Do not resubmit: fully redone or irrelevant"

### 5. **Reproducibility**
Scale: 1-5
- 5: "Could easily reproduce the results"
- 4: "Could mostly reproduce" with minor variations
- 3: "Could reproduce with some difficulty"
- 2: "Hard pressed to reproduce results"
- 1: "Would not be able to reproduce results"

### 6. **Datasets**
Scale: 1-5
- 5: "Enabling: should affect research projects"
- 4: "Useful: would recommend to researchers"
- 3: "Potentially useful: someone might find useful"
- 2: "Documentary: useful for replication"
- 1: "No usable datasets submitted"

### 7. **Software**
Scale: 1-5
- 5: "Enabling: should affect research projects"
- 4: "Useful: would recommend to researchers"
- 3: "Potenti
…[truncated 656 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 7961
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-15T07:14:41.991469+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/docs/paper/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-15T07:14:42.444704+00:00_

1	\begin{abstract}
2	Taxonomy-guided error injection improves tool-use LLM agents by +57pp (PALADIN; including inference-time retrieval), but does this transfer to embodied planning? We test TaxEI---a four-operator error taxonomy---on ALFWorld with Qwen3-8B, comparing clean training (Vanilla), taxonomy-tagged injection (TaxEI), and generic-labeled injection (Random) across three seeds. TaxEI yields no improvement ($-8.6$pp, $p{=}0.054$). Beyond this negative result, we identify three boundary conditions: (1)~a \emph{variance gradient} where instability increases from Vanilla (SD 3.3pp) through Random (7.0pp) to TaxEI (8.6pp); (2)~a shared \emph{dose-response threshold} at 10--25\% injection where both methods collapse by 12.8pp; and (3)~a \emph{per-operator local/global split} where local errors (+9.1pp) are learnable but global errors ($-8.3$pp) are harmful. These findings suggest error injection requires discrete, observable, locally recoverable errors---conditions met in tool-use but not in embodied planning.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-15T07:14:42.445189+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-15T07:14:42.947307+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Training LLM agents on failure trajectories is an increasingly popular paradigm. PALADIN \cite{paladin2025} demonstrates that taxonomy-guided error injection---where training data includes systematically corrupted trajectories tagged with error types---improves tool-use agent performance by +57pp (including inference-time retrieval augmentation). Related approaches show gains across tool-use \cite{song2024eto,eef2025,wang2024learning_from_failure} and dialogue tasks \cite{agentHER2025}. A natural question arises: does this transfer to embodied planning, where agents must execute multi-step physical manipulation tasks?
5	
6	We test this on ALFWorld \cite{shridhar2021alfworld} with TaxEI, a four-operator error taxonomy for embodied planning, training Qwen3-8B agents under three conditions (Vanilla, TaxEI, Random) across three seeds. TaxEI yields no improvement ($-8.6$pp, $p{=}0.054$) and directionally increases instability. Beyond reporting failure, we identify three boundary conditions:
7	
8	\begin{enumerate}[nosep,leftmargin=*]
9	\item \textbf{Variance gradient and dose-response threshold.} Instability follows Vanilla (SD 3.3pp) $<$ Random (7.0pp) $<$ TaxEI (8.6pp), though all variance tests are NS at $n{=}3$. Both methods share a sharp collapse between 10--25\% injection ($-12.8$pp each), followed by a plateau.
10	
11	\item \textbf{Per-operator local/global split.} Local errors (observation masking: $+9.1$pp) are learnable; global errors (context truncation, sub-goal deletion: $-8.3$pp each) are harmful---an exploratory finding ($N{=}11$--$12$) suggesting error injection requires observable, locally recoverable errors.
12	
13	\item \textbf{Training-evaluation paradox.} At $\geq$25\% injection, models achieve lower training loss but worse evaluation, consistent with memorization of injected patterns rather than learning.
14	\end{enumerate}
15	
16	These findings offer preliminary guidance for ALFWorld-like embo
…[truncated 161 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-15T07:14:42.947881+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/docs/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-15T07:14:43.450403+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Task Environment}
5	\label{sec:task_env}
6	
7	ALFWorld \cite{shridhar2021alfworld} is a text-based embodied environment where agents execute multi-step household tasks (e.g., \emph{heat a potato and place it in the fridge}). Each task requires a sequence of \texttt{think}/\texttt{act} steps in a ReAct-style loop \cite{yao2023react}. We use the standard 47-task unseen test split across six task types: \texttt{look\_at\_obj}, \texttt{pick\_and\_place}, \texttt{pick\_clean}, \texttt{pick\_cool}, \texttt{pick\_heat}, and \texttt{pick\_two\_obj}.
8	
9	\subsection{Error Taxonomy}
10	\label{sec:error_taxonomy}
11	
12	We define four error injection operators adapted for embodied planning, organized along two axes:
13	
14	\paragraph{Local operators} affect single steps without disrupting the overall plan structure:
15	\begin{itemize}[nosep,leftmargin=*]
16	\item \textbf{C4 (observation\_masking)}: Replaces environment observations with generic placeholders, removing perceptual grounding for one step.
17	\item \textbf{P1 (step\_order\_swap)}: Swaps two adjacent action steps, creating a locally incorrect but recoverable sequence.
18	\end{itemize}
19	
20	\paragraph{Global operators} disrupt the trajectory's causal chain:
21	\begin{itemize}[nosep,leftmargin=*]
22	\item \textbf{P2 (sub\_goal\_deletion)}: Removes a complete sub-goal (e.g., the ``clean'' step in a pick-clean-place task), breaking the plan's logical structure.
23	\item \textbf{C1 (context\_truncation)}: Truncates the context window, causing all subsequent decisions to rely on incomplete history.
24	\end{itemize}
25	
26	All operators achieve 100\% injection legality (valid action format) and 97.5\% recovery quality (trajectories remain parseable). Error-recovery pairs are \emph{not} explicitly paired in training data---errors are mixed as additional demonstrations.
27	
28	\subsection{Training Setup}
29	\label{sec:training_setup}
30	
31	We collect 501 expert tra
…[truncated 1135 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-15T07:14:43.450882+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/docs/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-15T07:14:43.903031+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate three training conditions on ALFWorld's 47 unseen test tasks \cite{shridhar2021alfworld}: \textbf{Vanilla} (4{,}358 clean demonstrations), \textbf{TaxEI} (4{,}358 clean + 4{,}671 taxonomy-tagged error trajectories = 9{,}029), and \textbf{Random} (4{,}358 clean + 4{,}671 generic-labeled errors = 9{,}029). Training details are in \S\ref{sec:training_setup}. We report results across three seeds (42, 0, 123).
5	
6	\subsection{Main Results}
7	\label{sec:main_results}
8	
9	Table~\ref{tab:main_results} shows three-seed evaluation results. TaxEI degrades directionally ($-8.6$pp vs.\ Vanilla), but the difference is not statistically significant (permutation test, $p{=}0.054$, $N{=}10{,}000$). No TaxEI seed exceeds the Vanilla mean. Random injection shows minimal degradation ($-2.2$pp, $p{>}0.3$).
10	
11	\begin{table}[t]
12	\centering
13	\small
14	\begin{tabular}{lccccc}
15	\toprule
16	\textbf{Method} & \textbf{$N$} & \textbf{s42} & \textbf{s0} & \textbf{s123} & \textbf{Mean$\pm$SD} \\
17	\midrule
18	Vanilla & 4{,}358 & 61.7 & 68.1 & 66.0 & 65.3$\pm$3.3 \\
19	TaxEI   & 9{,}029 & 61.7 & 46.8 & 61.7 & 56.7$\pm$8.6 \\
20	Random  & 9{,}029 & 66.0 & 55.3 & 68.1 & 63.1$\pm$7.0 \\
21	\bottomrule
22	\end{tabular}
23	\caption{Three-seed clean evaluation on ALFWorld (47 tasks, accuracy \%). TaxEI vs.\ Vanilla: $p{=}0.054$; TaxEI vs.\ Random: $p{=}0.170$; Random vs.\ Vanilla: $p{>}0.3$ (pooled permutation, 10K). Note: TaxEI/Random use $2.1\times$ more training data than Vanilla.}
24	\label{tab:main_results}
25	\end{table}
26	
27	Standard deviations follow a directional ordering: Vanilla (3.3pp) $<$ Random (7.0pp) $<$ TaxEI (8.6pp). However, this pattern is not statistically confirmed at $n{=}3$ (Levene's $p{=}0.085$; $F$-test $p{=}0.252$; bootstrap $P(\text{SD}_\text{TaxEI} > \text{SD}_\text{Vanilla}){=}69\%$).
28	
29	\subsection{Dose-Response}
30	\label{sec:dose_response}
31	
32	To control for data volume, we fix total 
…[truncated 4118 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-15T07:14:43.903390+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/docs/paper/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/docs/paper/analysis.tex"
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-15T07:14:44.858857+00:00_

1	% Analysis section merged into Experiments (§4.5, §4.6)
2	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 955
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-15T07:14:44.859272+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/docs/paper/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-15T07:14:44.859457+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Structural hypothesis.}
5	We hypothesize that the transfer failure stems from structural differences between tool-use and embodied planning (Table~\ref{tab:structural} in Appendix). In tool-use, errors produce discrete signals (API error codes) mapping to specific recovery actions; taxonomy labels encode this mapping. In embodied planning, errors propagate silently---picking the wrong object produces no error message, and recovery requires replanning from an unknown state. The taxonomy labels that help in tool-use become noise because there is no clean error$\to$recovery mapping to learn.
6	
7	\paragraph{Recovery-pairing confound.}
8	PALADIN pairs each error with an explicit recovery demonstration via retrieval augmentation, contributing an estimated $\sim$30pp of its +57pp gain. Our TaxEI injects standalone errors without paired recoveries. The negative result may stem from missing recovery pairing rather than (or in addition to) task structure. Future work should test recovery-paired injection on ALFWorld.
9	
10	\paragraph{Limitations.}
11	We evaluate on a single environment (ALFWorld, 47 tasks) with one base model. Three seeds provide limited statistical power; the variance gradient is directional but underpowered. The dose-response ablation uses a single seed. TaxEI/Random use $2.1\times$ more training data than Vanilla; the fixed-size ablation partially controls for this. Per-operator analysis ($N{=}11$--$12$) is exploratory. We acknowledge the tension in arguing $n{=}3$ is insufficient while reporting only $n{=}3$.
12	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-15T07:14:45.361529+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/docs/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-15T07:14:45.813410+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Error injection for LLM agents.}
5	Several recent methods augment agent training with failure trajectories. PALADIN \cite{paladin2025} uses a multi-category error taxonomy with retrieval-augmented recovery for tool-use agents. ETO \cite{song2024eto} applies DPO on exploration-generated failures. EEF \cite{eef2025} extracts positive signals from expert failures. Wang et al.\ \shortcite{wang2024learning_from_failure} integrate contrastive negative examples. AgentHER \cite{agentHER2025} applies hindsight relabeling. AgentDebug \cite{agentdebug2025} proposes a 5-dimensional error taxonomy for ALFWorld but focuses on diagnosis rather than training augmentation. Our work differs in two ways: (1) we test \emph{cross-domain transfer} of the error injection paradigm, and (2) we use direct SFT mixing rather than contrastive or DPO-based methods.
6	
7	\paragraph{Training instability and seed sensitivity.}
8	McCoy et al.\ \shortcite{mccoy2020seeds} show that BERT models with similar test performance exhibit large variability in out-of-distribution generalization across seeds. Mosbach et al.\ \shortcite{mosbach2021stability} identify instability in BERT fine-tuning and propose mitigation strategies. D'Amour et al.\ \shortcite{damour2022underspecification} frame this as underspecification in ML pipelines. Our variance gradient (Vanilla $<$ Random $<$ TaxEI) extends these observations to error-augmented agent training, suggesting that structured noise amplifies seed sensitivity.
9	
10	\paragraph{Data mixing and noise tolerance.}
11	Rolnick et al.\ \shortcite{rolnick2017robust} show deep networks are robust to massive label noise in vision---contrasting with our sharp threshold at 10--25\% injection in sequential decision-making. Ye et al.\ \shortcite{ye2025mixing_laws} establish data mixing laws with critical proportions for SFT. Bengio et al.\ \shortcite{bengio2009curriculum} introduce curriculum learning, where 
…[truncated 892 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-15T07:14:45.813853+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/docs/paper/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-15T07:14:46.014729+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We tested whether taxonomy-guided error injection---effective for tool-use agents---transfers to embodied planning. On ALFWorld, TaxEI provides no improvement over clean training ($-8.6$pp, $p{=}0.054$) and directionally increases training instability. We identify three boundary conditions: a variance gradient (Vanilla $<$ Random $<$ TaxEI), a shared dose-response threshold at 10--25\% injection, and a per-operator local/global split where only local, observable errors are learnable.
5	
6	Based on these results in ALFWorld, we suggest that practitioners considering error injection for embodied tasks first check three properties: (1)~are errors discrete and observable? (2)~can recovery be achieved locally? (3)~does the task provide immediate feedback? These criteria require validation in other environments.
7	
8	Future work should test recovery-paired injection on ALFWorld (disentangling the PALADIN confound), replicate on a second environment (e.g., WebShop), and run multi-seed dose-response ablations.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 200
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-15T07:14:46.065319+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/docs/paper/appendix.tex"
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-15T07:14:46.115960+00:00_

1	\appendix
2	
3	\section{Structural Comparison}
4	\label{app:structural}
5	
6	\begin{table}[h]
7	\centering
8	\small
9	\begin{tabular}{p{2.2cm}p{2.3cm}p{2.3cm}}
10	\toprule
11	\textbf{Dimension} & \textbf{Tool-Use} \cite{paladin2025} & \textbf{Embodied} \\
12	\midrule
13	Error signal & Discrete (API error codes) & Diffuse (wrong object, wrong room) \\
14	Observability & Explicit (stack trace) & Silent (no error msg) \\
15	Recovery scope & Local (retry call) & Global (replan) \\
16	Feedback & Immediate & Delayed \\
17	Error locality & Single step & Cascading \\
18	\bottomrule
19	\end{tabular}
20	\caption{Structural comparison: tool-use vs.\ embodied planning. Error injection benefits from discrete, observable, locally recoverable errors.}
21	\label{tab:structural}
22	\end{table}
23	
24	\section{Training Dynamics}
25	\label{app:training_dynamics}
26	
27	Figure~\ref{fig:training_curves} shows training loss curves across conditions. At $\geq$25\% injection, models achieve lower final training loss than Vanilla (TaxEI-50\%: 0.259 vs.\ Vanilla: 0.288) despite worse evaluation performance (\S\ref{sec:paradox}). At 10\% injection, training loss (0.308) remains above Vanilla.
28	
29	\begin{figure}[t]
30	\centering
31	\includegraphics[width=\columnwidth]{figures/paper/fig_app_training_curves.pdf}
32	\caption{Left: training loss curves. Right: final loss vs.\ eval accuracy---lower loss corresponds to worse performance at $\geq$25\% injection.}
33	\label{fig:training_curves}
34	\end{figure}
35	
36	\section{Per-Task Cross-Analysis}
37	\label{app:cross_analysis}
38	
39	The $\sim$6.4pp aggregate gap between TaxEI and Random at each dose point corresponds to $\approx$3 tasks on a 47-task evaluation. Cross-dose analysis reveals this is a discretization coincidence: zero tasks appear as TaxEI-penalty in all three dose points (10\%, 25\%, 50\%). The specific tasks that flip between conditions rotate across doses---9 different tasks contribute to the penalty, with no single task appea
…[truncated 367 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-15T07:14:53.704977+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://insights-workshop.github.io/",
  "prompt": "Extract the review criteria, evaluation dimensions, paper types they accept, and any specific guidance for what makes a good negative results paper. Also extract any information about the 2025 or 2026 edition."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://insights-workshop.github.io/",
    "prompt": "Extract the review criteria, evaluation dimensions, paper types they accept, and any specific guidance for what makes a good negative results paper. Also extract any information about the 2025 or 2026 edition."
  }
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-15T07:14:55.061648+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://insights-workshop.github.io/2021/cfp/",
  "prompt": "Extract the full call for papers: paper types accepted, review criteria, what makes a good submission for Insights from Negative Results, any specific guidance on how negative results should be presented."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://insights-workshop.github.io/2021/cfp/",
    "prompt": "Extract the full call for papers: paper types accepted, review criteria, what makes a good submission for Insights from Negative Results, any specific guidance on how negative results should be presented."
  }
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-15T07:14:56.015902+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "AgentDebug ALFWorld 5-dimensional error taxonomy \"where LLM agents fail\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "AgentDebug ALFWorld 5-dimensional error taxonomy \"where LLM agents fail\""
  }
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-15T07:14:57.221102+00:00_

# Workshop Information Analysis

Based on the provided content, I cannot extract the requested information because **the webpage content does not include review criteria, evaluation dimensions, paper types, or guidance for negative results papers.**

## What Is Available:

The page only provides navigation and structural information for the Insights 2026 workshop:

- **Location & Date**: "Budapest, Hungary, October 22-29, 2026 (co-located with EMNLP. Exact day TBA)"
- **Available Sections**: Links to Call for Papers, Accepted Papers, Program, Speakers, and Committee pages exist, but their actual content is not included in the excerpt provided

## What's Missing:

To answer your full question, I would need access to the actual content from:
- The Call for Papers page (/2026/cfp)
- The About page (/index)
- Previous editions (2024 or 2025) for comparison

**Recommendation**: Check the full Call for Papers document directly, as that section typically contains submission guidelines, review criteria, and expectations for paper quality.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 3516
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-15T07:15:00.438211+00:00_

# Call for Papers: Insights from Negative Results Workshop

## Paper Types Accepted

The workshop accepts two submission formats:

1. **Short papers**: Up to 4 pages excluding references
2. **Non-archival abstracts**: 1-2 pages for papers published elsewhere (main conferences or non-NLP venues)

Both types welcome participation in workshop discussions.

## What Makes a Strong Submission

Successful papers should contribute one of these elements:

- "experiments on(in) stability of the previously published results due to hardware, random initializations, etc."
- Ablation studies demonstrating components contribute differently than initially claimed
- Datasets or probing tasks revealing previous approaches fail to generalize
- Dataset extensions showing prior successes stem from "spurious statistical factors or annotation artifacts"
- Analysis of pre-training versus fine-tuning contributions
- Cross-lingual studies demonstrating technique limitations for specific languages
- "broadly applicable recommendations for training/fine-tuning" accompanied by explanations for why approaches failed

## Key Submission Requirements

- Follow EMNLP 2021 two-column formatting exactly
- Include all authors making substantial contributions
- Cite relevant refereed publications
- Provide code repositories in camera-ready versions when possible
- Submit with optional supplementary materials (appendices, software, data)

## Presentation Obligation

"All accepted papers must be presented at the workshop to appear in the proceedings." At least one author must register.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 5376
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-15T07:15:03.502240+00:00_

Web search results for query: "AgentDebug ALFWorld 5-dimensional error taxonomy "where LLM agents fail""

Links: [{"title":"Where LLM Agents Fail and How They can Learn From Failures | alphaXiv","url":"https://www.alphaxiv.org/overview/2509.25370v1"},{"title":"[2509.25370] Where LLM Agents Fail and How They can Learn From Failures","url":"https://arxiv.org/abs/2509.25370"},{"title":"WHERE LLM AGENTS FAIL AND HOW THEY CAN LEARN FROM FAILURES","url":"https://arxiv.org/pdf/2509.25370"},{"title":"GitHub - ulab-uiuc/AgentDebug · GitHub","url":"https://github.com/ulab-uiuc/AgentDebug"},{"title":"Where LLM Agents Fail And How They can Learn From Failures | OpenReview","url":"https://openreview.net/forum?id=PFR4E8583W"},{"title":"WHERE LLM AGENTS FAIL AND HOW THEY CAN LEARN ...","url":"https://openreview.net/pdf?id=PFR4E8583W"},{"title":"Paper page - Where LLM Agents Fail and How They can Learn From Failures","url":"https://huggingface.co/papers/2509.25370"},{"title":"[Literature Review] Where LLM Agents Fail and How They can Learn From Failures","url":"https://www.themoonlight.io/en/review/where-llm-agents-fail-and-how-they-can-learn-from-failures"},{"title":"How AgentDebug Helps LLM Agents Learn From Their Mistakes: Stanford and Illinois’ Breakthrough Research | by Algo Insights | Coding Nexus | Medium","url":"https://medium.com/coding-nexus/where-llm-agents-fail-and-how-they-can-learn-from-their-mistakes-9d407eaedb40"},{"title":"Why Do Multi-Agent LLM Systems Fail? Mert Cemri1∗ Melissa Z. Pan1∗ Shuyi Yang2∗","url":"https://arxiv.org/pdf/2503.13657"}]

I found comprehensive search results about the AgentDebug research and the 5-dimensional error taxonomy. Here's what I found:

## Summary

The research introduces the AgentErrorTaxonomy, a modular classification of failure modes spanning memory, reflection, planning, action, and system-level operations. This represents the five dimensions you asked about.

The researchers constructed AgentErrorBench, the first dataset of sy
…[truncated 1074 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7486
}
```

</details>

---

### Tool call

_source line 56 · 2026-05-15T07:15:10.539108+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://insights-workshop.github.io/2026/cfp/",
  "prompt": "Extract all review criteria, submission types, what makes a good negative results paper, evaluation dimensions, and any reviewer instructions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://insights-workshop.github.io/2026/cfp/",
    "prompt": "Extract all review criteria, submission types, what makes a good negative results paper, evaluation dimensions, and any reviewer instructions."
  }
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-15T07:15:11.291749+00:00_

Request failed with status code 404

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 752
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-15T07:15:11.342411+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "PALADIN self-correcting language model agents tool-failure taxonomy-guided error injection retrieval augmented recovery"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "PALADIN self-correcting language model agents tool-failure taxonomy-guided error injection retrieval augmented recovery"
  }
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-15T07:15:18.726276+00:00_

Web search results for query: "PALADIN self-correcting language model agents tool-failure taxonomy-guided error injection retrieval augmented recovery"

Links: [{"title":"PALADIN: Self-Correcting Language Model Agents to Cure Tool-Failure Cases","url":"https://arxiv.org/html/2509.25238v1"},{"title":"[2509.25238] PALADIN: Self-Correcting Language Model Agents to Cure Tool-Failure Cases","url":"https://arxiv.org/abs/2509.25238"},{"title":"PALADIN: Self-Correcting Language Model Agents to Cure ...","url":"https://arxiv.org/pdf/2509.25238"},{"title":"PALADIN: Self-Correcting Language Model Agents to Cure Tool-Failure Cases","url":"https://openreview.net/pdf?id=NVTtoO297p"},{"title":"PALADIN: Self-Correcting Language Model Agents to Cure Tool-Failure Cases | alphaXiv","url":"https://www.alphaxiv.org/abs/2509.25238"},{"title":"PALADIN: SELF-CORRECTING LANGUAGE MODEL","url":"https://openreview.net/pdf?id=M2AXTAKXbz"},{"title":"(PDF) PALADIN: Self-Correcting Language Model Agents to Cure Tool-Failure Cases","url":"https://www.researchgate.net/publication/396048240_PALADIN_Self-Correcting_Language_Model_Agents_to_Cure_Tool-Failure_Cases"},{"title":"PALADIN: Self-Correcting Language Model Agents to Cure Tool-Failure Cases - haebom","url":"https://slashpage.com/haebom/daily_arxiv?lang=en&tl=en&post=7916x82r8wqjj24kpyg3"},{"title":"PALADIN: Self-Correcting Tool-Using LLMs | Framework and dataset for robust, self-recovering tool-using language model agents.","url":"https://33k0.github.io/PALADIN-Framework/"},{"title":"[PDF] PALADIN: Self-Correcting Language Model Agents to Cure Tool-Failure Cases | Semantic Scholar","url":"https://www.semanticscholar.org/paper/PALADIN:-Self-Correcting-Language-Model-Agents-to-Vuddanti-Shah/9ae73fb066a4d577bce84c42ec285a05f0b24c46"}]

Based on the search results, here's what I found about PALADIN:

## Overview

PALADIN addresses the problem that tool-augmented language agents frequently fail in real-world deployment due to tool malfunctions like 
…[truncated 1487 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7383
}
```

</details>

---

### Tool call

_source line 60 · 2026-05-15T07:18:20.977571+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 — Round 1 审稿意见\n\n**论文**: \"When Does Error Injection Help LLM Agents? Boundary Conditions from a Failed Transfer to Embodied Planning\"\n**审查侧重**: 新颖性 + Framing + Related Work + 写作/格式合规\n\n---\n\n## 总体评分\n**Overall**: 2.5/5（Findings 边缘偏下，需要实质性修改后重投）\n**一句话总结**: 研究问题有价值、实验透明诚实，但 recovery-pairing confound 使核心\"迁移失败\"结论不可靠，且主体文本明显超过 4 页限制。\n\n## 官方维度打分（ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 2.5/5 | 核心 claim 受 recovery-pairing confound 严重威胁（§5.2 自己承认）；n=3 统计力不足；per-operator 分析 N=11-12 无法支撑结论 |\n| Excitement | 3/5 | 跨域迁移失败的负面结果有信息量，boundary conditions 有初步启发性，但新颖性有限 |\n| Reproducibility | 3.5/5 | 超参完整（LoRA rank 16, α=32, lr 1e-4, 3 epochs, bf16）；代码/数据未提供，GPT-5.2 trajectory 无法复现 |\n| Overall Assessment | 2.5/5 | 选题适合 Insights workshop，但需修复 framing、页数、统计问题 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 主体文本超过 4 页限制\n- 位置：PDF pages 1–5，Conclusion 结束于 page 5 上半部，References 随后开始\n- 问题：Insights workshop 短文 ≤ 4 pages excluding references。主体文本（§1–7）约 4.3–4.5 页，超标。\n- 影响：硬性格式违规，可能 desk rejection。\n- 建议：大幅精简 Related Work（当前约 0.8 页），或将部分 Discussion 移至 Appendix。\n\n**N2** [critical] Recovery-pairing confound 使核心 claim 不可靠\n- 位置：Abstract（\"does this transfer?\"）、Title（\"Failed Transfer\"）、§5.2\n- 问题：PALADIN = taxonomy + recovery pairing + retrieval augmentation。TaxEI 只复现了 taxonomy tagging。\"迁移失败\"无法区分：(a) error injection 在 embodied planning 无效 vs (b) 缺少 recovery pairing 导致失败。§5.2 承认了这点，但 title/abstract/intro/conclusion 的 framing 暗示 (a)。\n- 影响：confounded design，核心 claim 内部效度不足。\"没能完整复现方法 X\"≠\"方法 X 的核心思路在新领域失败\"。\n- 建议：修改 framing 明确限定为\"unpaired error injection\"的迁移测试；将 confound 从 Discussion 提升至 Introduction。\n\n**N3** [critical] PALADIN +57pp 归因不准确\n- 位置：Abstract 第 1 句、Introduction §1 第 1 段\n- 问题：+57pp 是 PALADIN 完整系统增益，非\"error injection\"单独增益。§5.2 估计 retrieval 贡献约 30pp。归因不准确误导读者。\n- 建议：首次提及时拆分增益来源。\n\n---\n\n## Should-Fix 问题\n\n**W1** [warning] 三个 boundary conditions 新颖性有限\n- 位置：Introduction 列表项 1–3、§3.2–§3.6\n- Variance gradient：n=3 无统计显著性；\"加噪声增加不稳定性\"是预期。\n- Dose-response threshold：已知现象（curriculum learning, noisy label 文献）。\n- Local/global split：基本是 error locality 的定义性属性；AgentDebug 在 ALFWorld 已有 error cascading 发现。\n- 建议：frame 为\"经验验证\"而非\"新发现的 boundary conditions\"。\n\n**W2** [warning] AgentDebug 重叠讨论不足\n- 位置：Related Work §6 第 1 段\n- AgentDebug 在 ALFWorld 提出 5 维 error taxonomy 且发现 error cascading 是主要瓶颈，与本文 local/global split 直接相关。仅一句话提及不够。\n- 建议：详细对比两套 taxonomy 设计和 cascading 发现。\n\n**W3** [warning] Dose-response 和 per-operator 分析均为单 seed\n- 位置：§3.2（seed=42 only）、§3.5（seed=42, N=11–12）\n- 问题：主实验 seed 间方差很大（TaxEI s0=46.8% vs s42/s123=61.7%），单 seed 结论可靠性存疑。±1 task = ±8–9pp 意味着 local/global split 可能是随机波动。\n- 建议：补充 seeds 或更明确标记为 preliminary。\n\n**W4** [warning] 缺少 ALFWorld 上 training-time 方法对比\n- 位置：Related Work §6 \"ALFWorld methods\" 段\n- 列出的都是 inference-time 方法。应讨论是否有 training-time 方法在 ALFWorld 上成功/失败。\n\n**W5** [warning] Title/claim scope vs 实际实验\n- Title 说\"Embodied Planning\"但只测了 ALFWorld（text-based）。与 vision-based embodied planning 有本质区别。\n- 建议：Title 中加 \"ALFWorld\" 或限定为 \"Text-Based Embodied Planning\"。\n\n---\n\n## 小问题\n\n1. `\\shortcite` 在 ACL 格式下应确认是否应使用 `\\citep`/`\\citet`。\n2. Table 1 提到 pooled permutation 但未解释 pooling 策略，未做多重比较校正。\n3. Figure 1/2 的\"Single seed\"标注应更醒目。\n4. Appendix D: v3→v4 baseline 变化 −12.8pp 增加实验流程稳健性疑虑。\n5. 匿名性：通过，未发现泄露。✓\n\n---\n\n## 主要优势\n\n1. **研究问题有价值**: cross-domain transfer 测试是自然的下一步，负面结果避免社区重复尝试。\n2. **实验透明**: 诚实报告负面结果和局限性。\n3. **Table 3 structural comparison** 提供有用对比框架。\n4. **选题适合 venue**: 与 Insights workshop 的 CFP 高度匹配。\n5. **写作清晰**: 叙事流畅，实验细节充分。",
  "reviewer_id": "2",
  "project": "tax_error_inject_agent"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 — Round 1 审稿意见\n\n**论文**: \"When Does Error Injection Help LLM Agents? Boundary Conditions from a Failed Transfer to Embodied Planning\"\n**审查侧重**: 新颖性 + Framing + Related Work + 写作/格式合规\n\n---\n\n## 总体评分\n**Overall**: 2.5/5（Findings 边缘偏下，需要实质性修改后重投）\n**一句话总结**: 研究问题有价值、实验透明诚实，但 recovery-pairing confound 使核心\"迁移失败\"结论不可靠，且主体文本明显超过 4 页限制。\n\n## 官方维度打分（ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 2.5/5 | 核心 claim 受 recovery-pairing confound 严重威胁（§5.2 自己承认）；n=3 统计力不足；per-operator 分析 N=11-12 无法支撑结论 |\n| Excitement | 3/5 | 跨域迁移失败的负面结果有信息量，boundary conditions 有初步启发性，但新颖性有限 |\n| Reproducibility | 3.5/5 | 超参完整（LoRA rank 16, α=32, lr 1e-4, 3 epochs, bf16）；代码/数据未提供，GPT-5.2 trajectory 无法复现 |\n| Overall Assessment | 2.5/5 | 选题适合 Insights workshop，但需修复 framing、页数、统计问题 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 主体文本超过 4 页限制\n- 位置：PDF pages 1–5，Conclusion 结束于 page 5 上半部，References 随后开始\n- 问题：Insights workshop 短文 ≤ 4 pages excluding references。主体文本（§1–7）约 4.3–4.5 页，超标。\n- 影响：硬性格式违规，可能 desk rejection。\n- 建议：大幅精简 Related Work（当前约 0.8 页），或将部分 Discussion 移至 Appendix。\n\n**N2** [critical] Recovery-pairing confound 使核心 claim 不可靠\n- 位置：Abstract（\"does this transfer?\"）、Title（\"Failed Transfer\"）、§5.2\n- 问题：PALADIN = taxonomy + recovery pairing + retrieval augmentation。TaxEI 只复现了 taxonomy tagging。\"迁移失败\"无法区分：(a) error injection 在 embodied planning 无效 vs (b) 缺少 recovery pairing 导致失败。§5.2 承认了这点，但 title/abstract/intro/conclusion 的 framing 暗示 (a)。\n- 影响：confounded design，核心 claim 内部效度不足。\"没能完整复现方法 X\"≠\"方法 X 的核心思路在新领域失败\"。\n- 建议：修改 framing 明确限定为\"unpaired error injection\"的迁移测试；将 confound 从 Discussion 提升至 Introduction。\n\n**N3** [critical] PALADIN +57pp 归因不准确\n- 位置：Abstract 第 1 句、Introduction §1 第 1 段\n- 问题：+57pp 是 PALADIN 完整系统增益，非\"error injection\"单独增益。§5.2 估计 retrieval 贡献约 30pp。归因不准确误导读者。\n- 建议：首次提及时拆分增益来源。\n\n---\n\n## Should-Fix 问题\n\n**W1** [warning] 三个 boundary conditions 新颖性有限\n- 位置：Introduction 列表项 1–3、§3.2–§3.6\n- Variance gradient：n=3 无统计显著性；\"加噪声增加不稳定性\"是预期。\n- Dose-response threshold：已知现象（curriculum learning, noisy label 文献）。\n- Local/global split：基本是 error locality 的定义性属性；AgentDebug 在 ALFWorld 已有 error cascading 发现。\n- 建议：frame 为\"经验验证\"而非\"新发现的 boundary conditions\"。\n\n**W2** [warning] AgentDebug 重叠讨论不足\n- 位置：Related Work §6 第 1 段\n- AgentDebug 在 ALFWorld 提出 5 维 error taxonomy 且发现 error cascading 是主要瓶颈，与本文 local/global split 直接相关。仅一句话提及不够。\n- 建议：详细对比两套 taxonomy 设计和 cascading 发现。\n\n**W3** [warning] Dose-response 和 per-operator 分析均为单 seed\n- 位置：§3.2（seed=42 only）、§3.5（seed=42, N=11–12）\n- 问题：主实验 seed 间方差很大（TaxEI s0=46.8% vs s42/s123=61.7%），单 seed 结论可靠性存疑。±1 task = ±8–9pp 意味着 local/global split 可能是随机波动。\n- 建议：补充 seeds 或更明确标记为 preliminary。\n\n**W4** [warning] 缺少 ALFWorld 上 training-time 方法对比\n- 位置：Related Work §6 \"ALFWorld methods\" 段\n- 列出的都是 inference-time 方法。应讨论是否有 training-time 方法在 ALFWorld 上成功/失败。\n\n**W5** [warning] Title/claim scope vs 实际实验\n- Title 说\"Embodied Planning\"但只测了 ALFWorld（text-based）。与 vision-based embodied planning 有本质区别。\n- 建议：Title 中加 \"ALFWorld\" 或限定为 \"Text-Based Embodied Planning\"。\n\n---\n\n## 小问题\n\n1. `\\shortcite` 在 ACL 格式下应确认是否应使用 `\\citep`/`\\citet`。\n2. Table 1 提到 pooled permutation 但未解释 pooling 策略，未做多重比较校正。\n3. Figure 1/2 的\"Single seed\"标注应更醒目。\n4. Appendix D: v3→v4 baseline 变化 −12.8pp 增加实验流程稳健性疑虑。\n5. 匿名性：通过，未发现泄露。✓\n\n---\n\n## 主要优势\n\n1. **研究问题有价值**: cross-domain transfer 测试是自然的下一步，负面结果避免社区重复尝试。\n2. **实验透明**: 诚实报告负面结果和局限性。\n3. **Table 3 structural comparison** 提供有用对比框架。\n4. **选题适合 venue**: 与 Insights workshop 的 CFP 高度匹配。\n5. **写作清晰**: 叙事流畅，实验细节充分。",
    "reviewer_id": "2",
    "project": "tax_error_inject_agent"
  }
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-15T07:18:24.944895+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3967
}
```

</details>

---

### Assistant

_source line 62 · 2026-05-15T07:18:34.600986+00:00_

审稿意见已提交给 Review Director。

总结：给出 Overall 2.5/5。3 个 must-fix 问题：(1) 主体文本超 4 页限制；(2) recovery-pairing confound 使 "failed transfer" 核心结论不可靠——TaxEI 未复现 PALADIN 的 recovery pairing，无法区分是 error injection 本身无效还是实验缺少关键组件；(3) 将 PALADIN 全系统 +57pp 归因于 error injection 不准确。5 个 should-fix 问题涉及 boundary conditions 新颖性有限、AgentDebug 重叠讨论不足、单 seed ablation 可靠性、缺少 ALFWorld training-time 方法对比、claim scope 过宽。优势方面肯定了选题价值、实验透明度和 venue 匹配度。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2"
}
```

</details>

---

## Round 2

4 recorded events

### User

_source line 63 · 2026-05-15T07:19:34.779222+00:00_

[Round 1 审稿请求]:
## Step 2 — 交叉分享：请逐条回应 Reviewer 1 的审稿意见

以下是 Reviewer 1 的完整审稿原文。请对每个 Must-Fix 和 Should-Fix 逐条回应：
- **[AGREE]** 同意并说明理由
- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）

---

## Reviewer 1 — Round 1 审稿意见

**审查侧重**: 方法严谨性 + 实验设计 + 统计分析
**Overall**: 3/5

### Must-Fix 问题

**N1** [critical] 主实验的数据量混淆与统计功效不足同时存在
- Table 1: TaxEI/Random 9,029 vs Vanilla 4,358（2.1×）。固定数据量的 dose-response 消融（Table 2）更公平但仅单 seed。n=3 seeds 下 permutation test 分辨率接近极限。三个 boundary conditions 的证据基础都建立在 underpowered 设计上。
- 建议：将 dose-response 扩展到 3 seeds；或将 Table 1 定位为"保守估计——TaxEI 即使多出 2.1× 数据仍更差"。

**N2** [critical] Variance gradient 作为 boundary condition 完全没有统计支撑
- 三组 SD 3.3/7.0/8.6pp，每组仅 n=3。Levene's p=0.085, F-test p=0.252, bootstrap P=69%——所有检验均 NS。但 Abstract 和 Conclusion 仍列为第一个 boundary condition。从 3 个观测估计 SD 的 95% CI 极宽，三组 CI 大幅重叠。
- 建议：从 boundary conditions 列表中移除或降级为"方向性观察"。

**N3** [critical] Recovery-pairing confound 可能独立解释全部负面结果
- PALADIN 使用 retrieval-augmented recovery pairing（贡献 ~30pp），TaxEI 不配对。"缺少 recovery pairing"是比"task structure 差异"更简单的竞争假说。
- 建议：将两个假说并列为等权重解释。

### Should-Fix 问题

**W1** [warning] Per-operator local/global split 粒度过粗
- N=11-12 per operator，单 seed，±1 task ≈ ±8-9pp。C4 的 +9.1pp = +1 task。"Binary split"可能是 ±1 task 的随机波动。
- 建议：报告 exact task count，降级为 hypothesis-generating。

**W2** [warning] Training-evaluation paradox 忽略更简单假说
- 更简单解释是 distribution shift 而非 memorization。50% injection training loss 更低可能只因错误轨迹是 easy-to-fit patterns。

**W3** [warning] "+57pp" PALADIN 数字呈现具有误导性
- 括号里"including inference-time retrieval"容易被忽略。

**W4** [warning] 页数可能超限
- 主体约 4.5 页，超出 ≤4 页限制。

**W5** [warning] 缺少与其他数据增强方法的对比
- 无法区分"error injection 没帮助"和"任何额外噪声数据都没帮助"。

### 小问题
- Abstract "no improvement" 应为 "no statistically significant improvement"（p=0.054 borderline）。
- §3.4 error detection rate 0% 值得更突出讨论。
- \shortcite 命令需确认编译正确。

### 主要优势
1. 选题精准，测试跨域迁移有价值。
2. Limitations 坦承几乎所有统计弱点，诚实透明。
3. 超越简单报告失败，用多维分析生成可检验假说。
4. 三条件 + 多 seed + dose-response 的整体框架合理。
5. Version discrepancy 透明披露。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---

### Tool call

_source line 64 · 2026-05-15T07:21:05.608132+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 — 对 Reviewer 1 审稿意见的逐条交叉回应\n\n---\n\n### Must-Fix\n\n**[AGREE] R1-N1: 数据量混淆与统计功效不足**\n同意核心设计缺陷。补充：Table 2 dose-response ablation 用 seed=42（TaxEI 表现最好的 seed），可能系统性高估。R1 建议\"保守估计\"framing 务实——TaxEI 有 2.1× 数据优势仍更差，本身有信息量。\n\n**[AGREE] R1-N2: Variance gradient 无统计支撑**\n强烈同意。n=3 估 SD 的 95% CI 极宽（SD=3.3 的 CI ≈ [1.9, 12.6]，SD=8.6 的 CI ≈ [4.9, 33.0]），大幅重叠。列为第一个 boundary condition 严重夸大证据。同意降级为\"方向性观察\"，但该趋势仍有 hypothesis-generating 价值。\n\n**[AGREE] R1-N3: Recovery-pairing confound**\n完全同意，与我的 N2 一致。补充：§5.2 估计 retrieval 贡献约 30pp，但来源不明——未引用 PALADIN 消融实验，这个估计本身的可靠性也需质疑。\n\n### Should-Fix\n\n**[AGREE] R1-W1: Per-operator split 粒度过粗**\n同意。C4 的 +9.1pp = +1 task。\"Binary split\"措辞过强。应报告 exact task count。\n\n**[REBUT] R1-W2: Training-evaluation paradox 替代假说**\n部分反驳。论文的 memorization 解释有一定依据：paradox 仅在 ≥25% 出现，10% 时 training loss 仍高于 Vanilla（0.308 vs 0.288）。若纯为 distribution shift / easy-to-fit，10% 也应降低 loss。非线性模式更符合 memorization 阈值效应。但两种解释可共存，论文应讨论 distribution shift 作为 competing explanation。\n\n**[AGREE] R1-W3: +57pp 误导**\n完全同意。我将此列为 must-fix（N3），严重性高于 R1 的 should-fix 评级。\n\n**[AGREE] R1-W4: 页数超限**\n同意。我列为 must-fix（N1）——workshop 格式限制通常是 desk rejection 标准。\n\n**[AGREE] R1-W5: 缺少其他增强方法对比**\n同意有效批评。Random 条件部分回应但不充分。若非错误增强也导致 dose-response collapse，结论变为\"任何 off-distribution augmentation 在小数据 SFT 下 harmful\"而非\"error injection 在 embodied planning 无效\"——本质不同的 takeaway。建议在 Discussion 承认。\n\n### 小问题\n- Abstract \"no improvement\" → \"no statistically significant improvement\"：[AGREE]\n- §3.4 error detection rate 0% 应更突出讨论：[AGREE]，0% detection 直接说明 taxonomy labels 未被学到\n- \\shortcite 编译：[AGREE]\n\n### 与我审稿的主要分歧/互补\n\n1. **+57pp 严重性**：我列 must-fix，R1 列 should-fix。我维持 must-fix——它影响论文 framing 基础。\n2. **页数超限严重性**：同上，我列 must-fix，R1 列 should-fix。\n3. **Training-evaluation paradox**：唯一实质分歧。R1 认为 distribution shift 更简单，我认为 10% vs ≥25% 的非线性提供了 memorization 方向的证据，但同意应讨论替代解释。\n4. **互补**：R1 更深入地分析了统计方法问题（permutation test 分辨率、CI 估计），我更侧重新颖性和 framing。两份审稿的 must-fix 高度一致。",
  "reviewer_id": "2",
  "project": "tax_error_inject_agent"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 — 对 Reviewer 1 审稿意见的逐条交叉回应\n\n---\n\n### Must-Fix\n\n**[AGREE] R1-N1: 数据量混淆与统计功效不足**\n同意核心设计缺陷。补充：Table 2 dose-response ablation 用 seed=42（TaxEI 表现最好的 seed），可能系统性高估。R1 建议\"保守估计\"framing 务实——TaxEI 有 2.1× 数据优势仍更差，本身有信息量。\n\n**[AGREE] R1-N2: Variance gradient 无统计支撑**\n强烈同意。n=3 估 SD 的 95% CI 极宽（SD=3.3 的 CI ≈ [1.9, 12.6]，SD=8.6 的 CI ≈ [4.9, 33.0]），大幅重叠。列为第一个 boundary condition 严重夸大证据。同意降级为\"方向性观察\"，但该趋势仍有 hypothesis-generating 价值。\n\n**[AGREE] R1-N3: Recovery-pairing confound**\n完全同意，与我的 N2 一致。补充：§5.2 估计 retrieval 贡献约 30pp，但来源不明——未引用 PALADIN 消融实验，这个估计本身的可靠性也需质疑。\n\n### Should-Fix\n\n**[AGREE] R1-W1: Per-operator split 粒度过粗**\n同意。C4 的 +9.1pp = +1 task。\"Binary split\"措辞过强。应报告 exact task count。\n\n**[REBUT] R1-W2: Training-evaluation paradox 替代假说**\n部分反驳。论文的 memorization 解释有一定依据：paradox 仅在 ≥25% 出现，10% 时 training loss 仍高于 Vanilla（0.308 vs 0.288）。若纯为 distribution shift / easy-to-fit，10% 也应降低 loss。非线性模式更符合 memorization 阈值效应。但两种解释可共存，论文应讨论 distribution shift 作为 competing explanation。\n\n**[AGREE] R1-W3: +57pp 误导**\n完全同意。我将此列为 must-fix（N3），严重性高于 R1 的 should-fix 评级。\n\n**[AGREE] R1-W4: 页数超限**\n同意。我列为 must-fix（N1）——workshop 格式限制通常是 desk rejection 标准。\n\n**[AGREE] R1-W5: 缺少其他增强方法对比**\n同意有效批评。Random 条件部分回应但不充分。若非错误增强也导致 dose-response collapse，结论变为\"任何 off-distribution augmentation 在小数据 SFT 下 harmful\"而非\"error injection 在 embodied planning 无效\"——本质不同的 takeaway。建议在 Discussion 承认。\n\n### 小问题\n- Abstract \"no improvement\" → \"no statistically significant improvement\"：[AGREE]\n- §3.4 error detection rate 0% 应更突出讨论：[AGREE]，0% detection 直接说明 taxonomy labels 未被学到\n- \\shortcite 编译：[AGREE]\n\n### 与我审稿的主要分歧/互补\n\n1. **+57pp 严重性**：我列 must-fix，R1 列 should-fix。我维持 must-fix——它影响论文 framing 基础。\n2. **页数超限严重性**：同上，我列 must-fix，R1 列 should-fix。\n3. **Training-evaluation paradox**：唯一实质分歧。R1 认为 distribution shift 更简单，我认为 10% vs ≥25% 的非线性提供了 memorization 方向的证据，但同意应讨论替代解释。\n4. **互补**：R1 更深入地分析了统计方法问题（permutation test 分辨率、CI 估计），我更侧重新颖性和 framing。两份审稿的 must-fix 高度一致。",
    "reviewer_id": "2",
    "project": "tax_error_inject_agent"
  }
}
```

</details>

---

### Tool result

_source line 65 · 2026-05-15T07:21:10.428458+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4820
}
```

</details>

---

### Assistant

_source line 66 · 2026-05-15T07:21:16.156937+00:00_

交叉回应已发送。总结：对 R1 的 8 个 Must-Fix/Should-Fix 中 7 个 [AGREE]，仅对 W2（training-evaluation paradox 的替代假说）[REBUT]——10% vs ≥25% 的非线性模式为 memorization 解释提供了一定支撑。两份审稿在核心问题上高度一致：recovery-pairing confound、+57pp 误导、页数超限、统计功效不足。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2"
}
```

</details>

---

## Round 3

40 recorded events

### User

_source line 67 · 2026-05-15T11:35:10.524220+00:00_

[Round 2 审稿请求]:
## Round 2 聚焦审稿任务

**论文路径**: `projects/tax_error_inject_agent/docs/paper/main.tex`（含 abstract.tex, introduction.tex, method.tex, experiments.tex, analysis.tex, discussion.tex, related_work.tex, conclusion.tex, appendix.tex, references.bib）

**目标 Venue**: Insights from Negative Results in NLP @ EMNLP 2026
**Track**: Workshop short paper
**格式要求**: ACL 两栏模板，正文 ≤ 4 页（不含 references, appendix, limitations），double-blind

---

### 背景

Round 2 修订评审。Round 1 评分 Weak Reject，共 16 个 issue。Reviewer 1 已完成全面审查，发现 13/16 resolved，3 partially resolved。本轮重点关注 Reviewer 1 发现的剩余问题和潜在遗漏。

---

### 你的聚焦审查领域

你负责以下 3 个核心问题的深度审查：

#### 1. 页数合规性（最关键）
- 估算主体文本（Introduction 到 Conclusion 结束）在 ACL 两栏格式下是否 ≤ 4 页
- 注意：当前 Limitations 嵌入 Discussion §4 最后一段（~150 词）。ACL 政策：独立 `\section*{Limitations}` 不计入页数。如果拆出 Limitations，是否能解决超页问题？
- 考虑因素：2 tables（Table 1 ~6行 + Table 2 ~10行），2 figures（各 \columnwidth），6 subsections in Experiments
- 如超页，具体建议哪些内容可压缩或移至 Appendix

#### 2. Framing 强度 vs 证据水平
- Title "Boundary Conditions from a Failed Transfer" — 是否过强？论文仅测试 1 environment + 1 model
- Conclusion 的 4-point checklist: (1) discrete/observable errors, (2) local recovery, (3) immediate feedback, (4) recovery pairing
  - Criterion (4) "recovery pairing" 在本文未被独立测试——是从 PALADIN 对比推理得出
  - Criterion (3) "immediate feedback" 与 Discussion 承认 ALFWorld 的 "Nothing happens" 反馈 "partially resembles tool-use observability" 有张力
- 评估 claim 强度是否与证据水平匹配

#### 3. 数据呈现一致性
- Table 2 dose-response 的 Δ 列：所有行对比 vanilla 3-seed mean (65.3±3.3)，但 10% 行是单 seed（seed=42），vanilla seed=42 = 61.7%。TaxEI 10% = 61.7%，Δ=-3.6（vs 65.3）。如果对比同 seed vanilla，Δ=0pp。这是否构成误导？
- Figure 1（seed=42 only）vs Table 2（3-seed）的覆盖不一致
- Recovery eval（§3.4）仅 seed=42，但论文已建立 seed sensitivity 极高——这是否削弱 recovery 结论的可信度？

---

### 你也需要快速检查

- Round 1 的 5 个 Must-Fix 是否已解决（Reviewer 1 判定 4/5 resolved，1 partially）
- Abstract 长度是否适合 4-page short paper
- 引用格式和匿名性

---

### 输出格式

1. **页数评估** — 估算结果 + 操作建议
2. **Framing 评估** — claim 强度 vs 证据匹配度
3. **数据呈现问题** — 具体指出不一致/误导
4. **Round 1 Must-Fix 快速确认** — 逐条确认或反对 Reviewer 1 判定
5. **Overall Assessment** — 评分（strong reject / weak reject / borderline / weak accept / strong accept）+ 置信度 + 简要理由

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---

### Tool call

_source line 68 · 2026-05-15T11:35:20.455887+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references,WebSearch,WebFetch",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references,WebSearch,WebFetch",
    "max_results": "5"
  }
}
```

</details>

---

### Tool result

_source line 69 · 2026-05-15T11:35:20.506475+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 70 · 2026-05-15T11:35:26.278978+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 71 · 2026-05-15T11:35:26.831401+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	% \usepackage{inconsolata}
11	\usepackage{graphicx}
12	\usepackage{amsmath}
13	\usepackage{booktabs}
14	\usepackage{enumitem}
15	\usepackage{amssymb}
16	\usepackage{pifont}
17	
18	\newcommand{\cmark}{\ding{51}}
19	\newcommand{\xmark}{\ding{55}}
20	
21	\title{When Does Unpaired Error Injection Help LLM Agents? \\ Boundary Conditions from a Failed Transfer to Embodied Planning}
22	
23	\author{Anonymous}
24	
25	\begin{document}
26	\maketitle
27	
28	\input{abstract}
29	
30	\input{introduction}
31	
32	\input{method}
33	
34	\input{experiments}
35	
36	\input{analysis}
37	
38	\input{discussion}
39	
40	\input{related_work}
41	
42	\input{conclusion}
43	
44	\bibliography{references}
45	
46	\input{appendix}
47	
48	\end{document}
49	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---

### Tool call

_source line 72 · 2026-05-15T11:35:26.831822+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/docs/paper/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 73 · 2026-05-15T11:35:27.334060+00:00_

1	\begin{abstract}
2	Taxonomy-guided error injection yields +57pp system-level improvement for tool-use LLM agents (PALADIN; combining taxonomy-guided injection, recovery pairing, and inference-time retrieval), but does this transfer to embodied planning? We test TaxEI---a four-operator error taxonomy---on ALFWorld with Qwen3-8B, comparing clean training (Vanilla), taxonomy-tagged injection (TaxEI), and generic-labeled injection (Random) across three seeds. TaxEI yields no statistically significant improvement ($-8.6$pp, $p{=}0.054$). However, this comparison is confounded: PALADIN pairs errors with recovery demonstrations, while our TaxEI injects standalone errors. The negative result may reflect missing recovery pairing rather than task structure. Beyond this negative result, we observe a dose-dependent dual regime: at moderate injection (25\%), performance degrades deterministically ($-17.8$pp, SD${=}$1.2pp, 3 seeds), while at high injection (50\%), extreme seed sensitivity emerges (SD${\approx}$12pp), with individual seeds ranging from 46.8\% to 70.2\%. We additionally observe a per-operator local/global split where local errors (+9.1pp) are learnable but global errors ($-8.3$pp) are harmful (exploratory, $N{=}11$--$12$). These patterns suggest that unpaired error injection may require discrete, observable, locally recoverable errors---conditions met in tool-use but not in embodied planning.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---

### Tool call

_source line 74 · 2026-05-15T11:35:27.334413+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 75 · 2026-05-15T11:35:27.937139+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Training LLM agents on failure trajectories is an increasingly popular paradigm. PALADIN \cite{paladin2025} demonstrates that taxonomy-guided error injection---where training data includes systematically corrupted trajectories tagged with error types---yields +57pp system-level improvement for tool-use agents (combining taxonomy-guided injection, recovery pairing, and inference-time retrieval). Related approaches show gains across tool-use \cite{song2024eto,eef2025,wang2024learning_from_failure} and dialogue tasks \cite{agentHER2025}. A natural question arises: does this transfer to embodied planning, where agents must execute multi-step physical manipulation tasks?
5	
6	We test this on ALFWorld \cite{shridhar2021alfworld} with TaxEI, a four-operator error taxonomy for embodied planning, training Qwen3-8B agents under three conditions (Vanilla, TaxEI, Random) across three seeds. TaxEI yields no statistically significant improvement ($-8.6$pp, $p{=}0.054$) and directionally increases instability. Crucially, this comparison is confounded: PALADIN pairs each injected error with an explicit recovery demonstration, while our TaxEI injects standalone errors without paired recoveries. The negative result may therefore reflect missing recovery pairing rather than---or in addition to---differences in task structure.
7	
8	Beyond reporting this negative result, we make two contributions:
9	
10	\begin{enumerate}[nosep,leftmargin=*]
11	\item \textbf{Negative transfer with competing hypotheses.} Unpaired error injection provides no statistically significant benefit on ALFWorld. Two equally plausible explanations exist: (a)~embodied planning lacks the discrete, observable error structure that makes injection effective in tool-use, and (b)~the absence of recovery pairing renders injected errors unlearnable. Disentangling these requires recovery-paired injection experiments.
12	
13	\item \textbf{Dose-dependent dual regime.} At
…[truncated 701 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 602
}
```

</details>

---

### Tool call

_source line 76 · 2026-05-15T11:35:27.937649+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/docs/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 77 · 2026-05-15T11:35:27.937970+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Task Environment}
5	\label{sec:task_env}
6	
7	ALFWorld \cite{shridhar2021alfworld} is a text-based embodied environment where agents execute multi-step household tasks (e.g., \emph{heat a potato and place it in the fridge}). Each task requires a sequence of \texttt{think}/\texttt{act} steps in a ReAct-style loop \cite{yao2023react}. We use the standard 47-task unseen test split across six task types: \texttt{look\_at\_obj}, \texttt{pick\_and\_place}, \texttt{pick\_clean}, \texttt{pick\_cool}, \texttt{pick\_heat}, and \texttt{pick\_two\_obj}.
8	
9	\subsection{Error Taxonomy}
10	\label{sec:error_taxonomy}
11	
12	We define four error injection operators adapted for embodied planning, organized along two axes:
13	
14	\paragraph{Local operators} affect single steps without disrupting the overall plan structure:
15	\begin{itemize}[nosep,leftmargin=*]
16	\item \textbf{C4 (observation\_masking)}: Replaces environment observations with generic placeholders, removing perceptual grounding for one step.
17	\item \textbf{P1 (step\_order\_swap)}: Swaps two adjacent action steps, creating a locally incorrect but recoverable sequence.
18	\end{itemize}
19	
20	\paragraph{Global operators} disrupt the trajectory's causal chain:
21	\begin{itemize}[nosep,leftmargin=*]
22	\item \textbf{P2 (sub\_goal\_deletion)}: Removes a complete sub-goal (e.g., the ``clean'' step in a pick-clean-place task), breaking the plan's logical structure.
23	\item \textbf{C1 (context\_truncation)}: Truncates the context window, causing all subsequent decisions to rely on incomplete history.
24	\end{itemize}
25	
26	All operators achieve 100\% injection legality (valid action format) and 97.5\% recovery quality (trajectories remain parseable). Error-recovery pairs are \emph{not} explicitly paired in training data---errors are mixed as additional demonstrations.
27	
28	\subsection{Training Setup}
29	\label{sec:training_setup}
30	
31	We collect 501 expert tra
…[truncated 1214 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 78 · 2026-05-15T11:35:28.339746+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/docs/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 79 · 2026-05-15T11:35:28.842114+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate three training conditions on ALFWorld's 47 unseen test tasks \cite{shridhar2021alfworld}: \textbf{Vanilla} (4{,}358 clean demonstrations), \textbf{TaxEI} (4{,}358 clean + 4{,}671 taxonomy-tagged error trajectories = 9{,}029), and \textbf{Random} (4{,}358 clean + 4{,}671 generic-labeled errors = 9{,}029). Training details are in \S\ref{sec:training_setup}. We report results across three seeds (42, 0, 123).
5	
6	\subsection{Main Results}
7	\label{sec:main_results}
8	
9	Table~\ref{tab:main_results} shows three-seed evaluation results. TaxEI degrades directionally ($-8.6$pp vs.\ Vanilla), but the difference is not statistically significant (permutation test, $p{=}0.054$, $N{=}10{,}000$). No TaxEI seed exceeds the Vanilla mean. Random injection shows minimal degradation ($-2.2$pp, $p{>}0.3$). The TaxEI--Random gap is driven by two of six task types (\texttt{pick\_cool}: $-19.0$pp; \texttt{pick\_two\_obj}: $-14.3$pp).
10	
11	\begin{table}[t]
12	\centering
13	\small
14	\begin{tabular}{lccccc}
15	\toprule
16	\textbf{Method} & \textbf{$N$} & \textbf{s42} & \textbf{s0} & \textbf{s123} & \textbf{Mean$\pm$SD} \\
17	\midrule
18	Vanilla & 4{,}358 & 61.7 & 68.1 & 66.0 & 65.3$\pm$3.3 \\
19	TaxEI   & 9{,}029 & 61.7 & 46.8 & 61.7 & 56.7$\pm$8.6 \\
20	Random  & 9{,}029 & 66.0 & 55.3 & 68.1 & 63.1$\pm$7.0 \\
21	\bottomrule
22	\end{tabular}
23	\caption{Three-seed clean evaluation on ALFWorld (47 tasks, accuracy \%). TaxEI vs.\ Vanilla: $p{=}0.054$; TaxEI vs.\ Random: $p{=}0.170$; Random vs.\ Vanilla: $p{>}0.3$ (pooled permutation, 10K). Note: TaxEI/Random use 9{,}029 samples ($2.1\times$ vanilla). The dose-response ablation (Table~\ref{tab:dose_response}) controls for data volume at a fixed 4{,}358 total.}
24	\label{tab:main_results}
25	\end{table}
26	
27	At full training scale, standard deviations follow Vanilla (3.3pp) $<$ Random (7.0pp) $<$ TaxEI (8.6pp), though not statistically confirmed at $n{=}3$. The dose-respons
…[truncated 4323 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---

### Tool call

_source line 80 · 2026-05-15T11:35:28.892707+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/docs/paper/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/docs/paper/analysis.tex"
  }
}
```

</details>

---

### Tool result

_source line 81 · 2026-05-15T11:35:29.294711+00:00_

1	% Analysis section merged into Experiments (§4.5, §4.6)
2	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---

### Tool call

_source line 82 · 2026-05-15T11:35:29.295140+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/docs/paper/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 83 · 2026-05-15T11:35:30.249431+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Structural hypothesis.}
5	We hypothesize that the transfer failure stems from structural differences between tool-use and embodied planning (Table~\ref{tab:structural} in Appendix). In tool-use, errors produce discrete signals (API error codes) mapping to specific recovery actions; taxonomy labels encode this mapping. In embodied planning, errors propagate silently---picking the wrong object produces no error message, and recovery requires replanning from an unknown state. Reflexion \cite{shinn2023reflexion} achieves $\sim$97\% on ALFWorld through inference-time failure reflection, suggesting that inference-time self-correction succeeds where training-time injection fails in embodied planning.
6	
7	\paragraph{Recovery-pairing confound.}
8	PALADIN pairs each error with an explicit recovery demonstration via retrieval augmentation, contributing an estimated $\sim$30pp of its +57pp system-level gain. Our TaxEI injects standalone errors without paired recoveries. We cannot distinguish between these two hypotheses with the current design: the negative result may stem from (a)~missing recovery pairing, or (b)~structural differences between tool-use and embodied planning, or both. Recovery-paired injection on ALFWorld is needed to disentangle these factors.
9	
10	\paragraph{Training lottery at high injection.}
11	At 50\% injection, individual seeds range from 46.8\% to 70.2\%---the latter exceeding all vanilla seeds. The 70.2\% anomaly occurs in both TaxEI (seed=0) and Random (seed=123), suggesting a generic high-dose phenomenon independent of taxonomy labeling. This cross-condition coincidence may reflect a seed-initialization $\times$ injection interaction warranting further investigation.
12	
13	\paragraph{Limitations.}
14	We evaluate on a single environment (ALFWorld, 47 tasks) with one base model. Three seeds provide limited statistical power; the 10\% dose-response uses a single seed (25\%/50\% confirmed
…[truncated 684 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---

### Tool call

_source line 84 · 2026-05-15T11:35:30.601033+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/docs/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 85 · 2026-05-15T11:35:30.601388+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Error injection for LLM agents.}
5	Several methods augment agent training with failure trajectories: PALADIN \cite{paladin2025} uses taxonomy-guided injection with retrieval-augmented recovery; ETO \cite{song2024eto} applies DPO on exploration failures; EEF \cite{eef2025} extracts positive signals from expert failures; Wang et al.\ \shortcite{wang2024learning_from_failure} and AgentHER \cite{agentHER2025} integrate contrastive or relabeled negatives. AgentDebug \cite{agentdebug2025} identifies five error dimensions including error cascading---a phenomenon our per-operator analysis independently corroborates. Their diagnostic taxonomy differs from our injection-oriented 4-operator design: AgentDebug classifies observed errors post-hoc, while our operators generate controlled perturbations. The overlap in cascading-error findings suggests this structural property is a robust moderator of error-injection effectiveness. Our work tests \emph{cross-domain transfer} of the injection paradigm using direct SFT mixing.
6	
7	\paragraph{Training dynamics and data mixing.}
8	McCoy et al.\ \shortcite{mccoy2020seeds} and Mosbach et al.\ \shortcite{mosbach2021stability} document seed sensitivity in fine-tuning; D'Amour et al.\ \shortcite{damour2022underspecification} frame this as underspecification. Our dose-dependent variance findings extend these observations to error-augmented agent training. Rolnick et al.\ \shortcite{rolnick2017robust} show robustness to massive label noise in vision---contrasting with our sharp degradation at 25\% injection in sequential decision-making. Ye et al.\ \shortcite{ye2025mixing_laws} and Bengio et al.\ \shortcite{bengio2009curriculum} establish that data composition has non-linear effects on SFT performance.
9	
10	\paragraph{ALFWorld methods.}
11	ReAct \cite{yao2023react} establishes think/act prompting. Reflexion \cite{shinn2023reflexion} achieves $\sim$97\% via multi-trial infer
…[truncated 407 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 86 · 2026-05-15T11:35:30.952837+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/docs/paper/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 87 · 2026-05-15T11:35:30.953184+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We tested whether unpaired taxonomy-guided error injection---effective for tool-use agents---transfers to embodied planning. On ALFWorld, TaxEI provides no statistically significant improvement over clean training ($-8.6$pp, $p{=}0.054$). Two competing hypotheses explain this: embodied planning may lack the discrete, observable error structure required for injection to help, or the absence of recovery pairing (present in PALADIN) may render standalone errors unlearnable. We additionally identify a dose-dependent dual regime (3-seed confirmed at 25\%/50\%): deterministic degradation at moderate injection, chaotic seed-dependent outcomes at high injection. We also observe a per-operator local/global split (exploratory, $N{=}11$--$12$).
5	
6	Based on our results and the two competing hypotheses, we suggest that practitioners considering error injection for embodied tasks check four properties: (1)~are errors discrete and observable? (2)~can recovery be achieved locally? (3)~does the task provide immediate feedback? (4)~are errors paired with explicit recovery demonstrations? These criteria require validation in other environments.
7	
8	Future work should first test recovery-paired injection on ALFWorld to disentangle the task-structure hypothesis from recovery-pairing effects, then replicate on a second environment (e.g., WebShop) and investigate the seed-initialization $\times$ injection interaction observed at high doses.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 88 · 2026-05-15T11:35:31.304615+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/docs/paper/appendix.tex"
  }
}
```

</details>

---

### Tool result

_source line 89 · 2026-05-15T11:35:31.355372+00:00_

1	\appendix
2	
3	\section{Structural Comparison}
4	\label{app:structural}
5	
6	\begin{table}[h]
7	\centering
8	\small
9	\begin{tabular}{p{2.2cm}p{2.3cm}p{2.3cm}}
10	\toprule
11	\textbf{Dimension} & \textbf{Tool-Use} \cite{paladin2025} & \textbf{Embodied} \\
12	\midrule
13	Error signal & Discrete (API error codes) & Diffuse (wrong object, wrong room) \\
14	Observability & Explicit (stack trace) & Silent (no error msg) \\
15	Recovery scope & Local (retry call) & Global (replan) \\
16	Feedback & Immediate & Delayed \\
17	Error locality & Single step & Cascading \\
18	\bottomrule
19	\end{tabular}
20	\caption{Structural comparison: tool-use vs.\ embodied planning. Error injection benefits from discrete, observable, locally recoverable errors.}
21	\label{tab:structural}
22	\end{table}
23	
24	\section{Training Dynamics}
25	\label{app:training_dynamics}
26	
27	Figure~\ref{fig:training_curves} shows training loss curves across conditions. At $\geq$25\% injection, models achieve lower final training loss than Vanilla (TaxEI-50\%: 0.259 vs.\ Vanilla: 0.288) despite worse evaluation performance (\S\ref{sec:paradox}). At 10\% injection, training loss (0.308) remains above Vanilla.
28	
29	\begin{figure}[t]
30	\centering
31	\includegraphics[width=\columnwidth]{figures/paper/fig_app_training_curves.pdf}
32	\caption{Left: training loss curves. Right: final loss vs.\ eval accuracy---lower loss corresponds to worse performance at $\geq$25\% injection.}
33	\label{fig:training_curves}
34	\end{figure}
35	
36	\section{Per-Task Cross-Analysis}
37	\label{app:cross_analysis}
38	
39	For seed=42, the $\sim$6.4pp aggregate gap between TaxEI and Random at each dose point corresponds to $\approx$3 tasks on a 47-task evaluation. This consistency does not hold across seeds: at 25\% the 3-seed mean gap is 8.5pp, at 50\% it is 2.1pp. Cross-dose analysis reveals this is a discretization coincidence: zero tasks appear as TaxEI-penalty in all three dose points (10\%, 25\%, 50\%). The specific tasks that
…[truncated 815 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 90 · 2026-05-15T11:35:31.707142+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/docs/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 91 · 2026-05-15T11:35:32.109021+00:00_

1	@article{rolnick2017robust,
2	  title={Deep Learning is Robust to Massive Label Noise},
3	  author={{Rolnick, D.} and {Veit, A.} and {Belongie, S.} and {Shavit, N.}},
4	  year={2017},
5	  journal={arXiv preprint arXiv:1705.10694},
6	  url={https://arxiv.org/abs/1705.10694}
7	}
8	
9	@article{wang2024learning_from_failure,
10	  title={Learning From Failure: Integrating Negative Examples when Fine-tuning Large Language Models as Agents},
11	  author={{Wang, R.} and {Li, H.} and {Han, X.} and {Zhang, Y.} and {Baldwin, T.}},
12	  year={2024},
13	  journal={arXiv preprint arXiv:2402.11651},
14	  url={https://arxiv.org/abs/2402.11651}
15	}
16	
17	@inproceedings{song2024eto,
18	  title={Trial and Error: Exploration-Based Trajectory Optimization for LLM Agents},
19	  author={{Song, Y.} and {Yin, D.} and {Yue, X.} and {Huang, J.} and {Li, S.} and {Lin, B. Y.}},
20	  year={2024},
21	  booktitle={Proceedings of the Annual Meeting of the Association for Computational Linguistics}
22	}
23	
24	@article{paladin2025,
25	  title={{PALADIN}: Self-Correcting Language Model Agents to Cure Tool-Failure Cases},
26	  author={{Vuddanti, S. V.} and {Shah, A.} and {Chittiprolu, S. K.} and {Song, T.} and {Dev, S.} and {Zhu, K.} and {Chaudhary, M.}},
27	  year={2025},
28	  journal={arXiv preprint arXiv:2509.25238},
29	  url={https://arxiv.org/abs/2509.25238}
30	}
31	
32	@article{agentHER2025,
33	  title={{AgentHER}: Hindsight Experience Replay for LLM Agent Trajectory Relabeling},
34	  author={{Ding, L.}},
35	  year={2025},
36	  journal={arXiv preprint arXiv:2603.21357},
37	  url={https://arxiv.org/abs/2603.21357}
38	}
39	
40	@inproceedings{ye2025mixing_laws,
41	  title={Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance},
42	  author={{Ye, J.} and others},
43	  year={2025},
44	  booktitle={International Conference on Learning Representations}
45	}
46	
47	@article{agentprm2025,
48	  title={Process Reward Models for LLM Agents: Practical Framework and Direct
…[truncated 4506 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---

### Tool call

_source line 92 · 2026-05-15T11:35:32.109579+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 Insights from Negative Results workshop reviewer guidelines review form"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 Insights from Negative Results workshop reviewer guidelines review form"
  }
}
```

</details>

---

### Tool call

_source line 93 · 2026-05-15T11:35:32.611675+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2026 review form criteria scoring dimensions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 review form criteria scoring dimensions"
  }
}
```

</details>

---

### Tool result

_source line 94 · 2026-05-15T11:35:40.494088+00:00_

Web search results for query: "ACL ARR 2026 review form criteria scoring dimensions"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"ARR Dashboard","url":"https://stats.aclrollingreview.org/"},{"title":"ACL ARR 2026 | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"}]

Based on my search results, here's information about the ACL ARR 2026 review form criteria and scoring dimensions:

## Scoring Dimensions

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

### Key Criteria

**Soundness:** The soundness scores must be justified by the text of the review. 
…[truncated 1246 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7882
}
```

</details>

---

### Tool result

_source line 95 · 2026-05-15T11:35:46.567980+00:00_

Web search results for query: "EMNLP 2026 Insights from Negative Results workshop reviewer guidelines review form"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Workshop on Insights from Negative Results | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-insights-negative-results"},{"title":"CFP | Insights 2024","url":"https://insights-workshop.github.io/2021/cfp/"},{"title":"EMNLP 2026 | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026"},{"title":"Insights 2024 | Workshop on Insights from Negative Results in NLP","url":"https://insights-workshop.github.io/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"2026 Reviewer Guidelines","url":"https://neurips.cc/Conferences/2026/ReviewerGuidelines"},{"title":"EMNLP | OpenReview","url":"https://openreview.net/group?id=EMNLP"}]

I found some general information about EMNLP 2026 and the Workshop on Insights from Negative Results, but the search results don't contain specific information about reviewer guidelines or a review form for the EMNLP 2026 "Insights from Negative Results" workshop. Let me search more specifically for the 2026 workshop details.

Links: [{"title":"Insights 2024 | Workshop on Insights from Negative Results in NLP","url":"https://insights-workshop.github.io/"},{"title":"CFP | Insights 2024","url":"https://insights-workshop.github.io/2021/cfp/"},{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},
…[truncated 4542 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 14458
}
```

</details>

---

### Tool call

_source line 96 · 2026-05-15T11:35:53.545311+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "http://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form: all scoring dimensions, their scales (1-5 or whatever), and descriptions of each score level. Also extract any special guidance for workshop papers or short papers."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "http://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form: all scoring dimensions, their scales (1-5 or whatever), and descriptions of each score level. Also extract any special guidance for workshop papers or short papers."
  }
}
```

</details>

---

### Tool call

_source line 97 · 2026-05-15T11:35:54.950924+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://insights-workshop.github.io/2021/cfp/",
  "prompt": "Extract the full call for papers including: paper format requirements, page limits, review criteria, what types of papers they accept, and any specific reviewer guidelines or evaluation criteria for the Insights from Negative Results workshop."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://insights-workshop.github.io/2021/cfp/",
    "prompt": "Extract the full call for papers including: paper format requirements, page limits, review criteria, what types of papers they accept, and any specific reviewer guidelines or evaluation criteria for the Insights from Negative Results workshop."
  }
}
```

</details>

---

### Tool call

_source line 98 · 2026-05-15T11:35:56.105235+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "http://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract all reviewer guidelines: scoring criteria, how to assess soundness/excitement/overall, what constitutes each score level, and any guidance on reviewing negative results or short papers."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "http://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract all reviewer guidelines: scoring criteria, how to assess soundness/excitement/overall, what constitutes each score level, and any guidance on reviewing negative results or short papers."
  }
}
```

</details>

---

### Tool result

_source line 99 · 2026-05-15T11:36:01.173774+00:00_

# Insights Workshop Call for Papers Summary

## Paper Types Accepted
The workshop accepts two submission categories:
- Short papers (up to 4 pages, excluding references)
- Non-archival abstracts (1-2 pages) for work published elsewhere

## Format Requirements
Submissions must follow "the EMNLP 2021 two-column format" with official style sheets from the conference. Papers failing to meet specifications regarding "paper size, margin width, and font size restrictions" face rejection without review.

## Review Criteria & Acceptable Content
The workshop seeks negative results that contribute:
- Reproducibility experiments examining result stability across hardware/initializations
- Ablation studies showing actual vs. reported component contributions
- Probing tasks demonstrating lack of generalization across domains
- Dataset extensions revealing spurious correlations or annotation artifacts
- Analyses of pre-training versus fine-tuning contributions
- Cross-lingual studies showing technique limitations
- Training recommendations with explanations for why approaches failed

## Reviewer Guidelines
Reviewers assess whether papers truly demonstrate failure rather than methodological bugs. Authors should provide code repositories and supplementary materials documenting "preprocessing decisions, model parameters, feature templates" to establish reproducibility. Contemporary papers (published within 3 months of submission) don't require detailed comparative analysis.

## Submission Requirements
All listed authors must have "made substantial contributions," with no post-deadline authorship changes permitted.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 6222
}
```

</details>

---

### Tool result

_source line 100 · 2026-05-15T11:36:01.876692+00:00_

# ACL Rolling Review Form - Scoring Dimensions

## 1. **Reviewer Confidence** (1-5 scale)
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: "Quite sure. I tried to check the important points carefully."
- **3**: "Pretty sure, but there's a chance I missed something."
- **2**: "Willing to defend my evaluation, but it is fairly likely that I missed some details."
- **1**: "Not my area, or paper is very hard to understand."

## 2. **Soundness** (1-5 scale, with half-point increments)
- **5**: "Excellent: This study is one of the most thorough I have seen, given its type."
- **4**: "Strong: This study provides sufficient support for all of its claims."
- **3**: "Acceptable: This study provides sufficient support for its main claims."
- **2**: "Poor: Some of the main claims are not sufficiently supported."
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication."

## 3. **Excitement** (1-5 scale, with half-point increments)
Describes subjective interest in conceptual breakthroughs, community impact, or personal relevance.
- **5**: "Highly Exciting: I would recommend this paper to others."
- **4**: "Exciting: I would mention this paper to others."
- **3**: "Interesting: I might mention some points to others."
- **2**: "Potentially Interesting: does not resonate with me, but it might with others."
- **1**: "Not Exciting: does not resonate with me, and I don't think it would with others."

## 4. **Overall Assessment** (1-5 scale, with half-point increments)
Final recommendation from award consideration through rejection:
- **5**: "Consider for Award"
- **4.5**: "Borderline Award"
- **4**: "Conference: could be accepted to an *ACL conference"
- **3.5**: "Borderline Conference"
- **3**: "Findings: could be accepted to the Findings of the ACL"
- **2.5**: "Borderline Findings"
- **2**: "Resubmit next cycle"
- **1.5**: "Resubmit after next cycle"
- **1**: "Do not resub
…[truncated 812 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 8331
}
```

</details>

---

### Tool result

_source line 101 · 2026-05-15T11:36:02.741761+00:00_

# ARR Reviewer Guidelines: Scoring Criteria and Assessment

## Scoring Framework

ARR uses three distinct scores starting February 2025:

### 1. Soundness Score
This reflects technical validity. "The _soundness_ scores must be justified by the text of the review." Low soundness ratings require explicit justification tied to identified flaws. Reviewers should ensure their written feedback actually supports their assigned score.

### 2. Excitement Score
This captures personal interest, independent of soundness. "Such preferences are more subjective and should be reflected in a separate _excitement_ score, which is orthogonal to the assessment of the soundness of the paper." A reviewer might find technically sound work uninteresting personally—both assessments are valid.

### 3. Overall Recommendation
This composite judgment considers soundness, excitement, novelty, and impact together. Papers committed to conferences must meet soundness thresholds, though reviewers may recommend acceptance for intellectually significant work even without personal enthusiasm.

## Key Assessment Guidance

**For Negative Results:** The guidelines explicitly combat bias here: "The bias towards publishing only positive results is a known problem in many fields." Negative findings where something systematically fails deserve publication when communities need that knowledge.

**For Short Papers:** Reviewers should avoid requiring extensive additions. "Such a criticism can be made for most papers. It is only valid if the argument that is being made depends on X."

**Avoiding Common Biases:** The guidelines list 17 heuristics (H1-H17) where reviewers commonly make unjustified judgments—from dismissing "simple" methods to expecting SOTA results.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 6636
}
```

</details>

---

### Tool call

_source line 102 · 2026-05-15T11:37:50.861492+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/docs/paper",
  "project": "tax_error_inject_agent"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_2/projects/tax_error_inject_agent/docs/paper",
    "project": "tax_error_inject_agent"
  }
}
```

</details>

---

### Tool result

_source line 103 · 2026-05-15T11:38:58.324990+00:00_

{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 19, \"total_citations\": 22, \"unique_cited_keys\": 13, \"orphan_bib\": 6, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 15, \"online_not_found\": 3, \"online_mismatch\": 1}, \"cross_check\": {\"orphan_bib\": [\"bengio2009curriculum\", \"damour2022underspecification\", \"mccoy2020seeds\", \"mosbach2021stability\", \"rolnick2017robust\", \"ye2025mixing_laws\"], \"missing_bib\": [], \"orphan_count\": 6, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"rolnick2017robust\", \"type\": \"article\", \"title\": \"Deep Learning is Robust to Massive Label Noise\", \"authors\": \"Rolnick, D. and Veit, A. and Belongie, S. and Shavit, N.\", \"year\": \"2017\", \"venue\": \"arXiv preprint arXiv:1705.10694\"}, {\"key\": \"wang2024learning_from_failure\", \"type\": \"article\", \"title\": \"Learning From Failure: Integrating Negative Examples when Fine-tuning Large Language Models as Agents\", \"authors\": \"Wang, R. and Li, H. and Han, X. and Zhang, Y. and Baldwin, T.\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2402.11651\"}, {\"key\": \"song2024eto\", \"type\": \"inproceedings\", \"title\": \"Trial and Error: Exploration-Based Trajectory Optimization for LLM Agents\", \"authors\": \"Song, Y. and Yin, D. and Yue, X. and Huang, J. and Li, S. and Lin, B. Y.\", \"year\": \"2024\", \"venue\": \"Proceedings of the Annual Meeting of the Association for Computational Linguisti...\"}, {\"key\": \"paladin2025\", \"type\": \"article\", \"title\": \"PALADIN: Self-Correcting Language Model Agents to Cure Tool-Failure Cases\", \"authors\": \"Vuddanti, S. V. and Shah, A. and Chittiprolu, S. K. and Song, T. and Dev, S. and...\", \"year\": \"2025\", \"venue\": \"arXiv preprint arXiv:2509.25238\"}, {\"key\": \"agentHER2025\", \"type\": \"article\", \"title\": \"AgentHER: Hindsight Experience Replay for LLM Agent Trajectory Relabeling\", \"authors\": \"Ding, L.\", \"year\": \"2025\", \"
…[truncated 12832 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 67463
}
```

</details>

---

### Tool call

_source line 104 · 2026-05-15T11:42:28.816870+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 — Round 2 聚焦审稿报告\n\n**论文**: \"When Does Unpaired Error Injection Help LLM Agents? Boundary Conditions from a Failed Transfer to Embodied Planning\"\n**Venue**: Insights from Negative Results in NLP @ EMNLP 2026\n**审查依据**: ACL ARR review form (Soundness / Excitement / Overall, 1–5 scale with half-point increments)\n\n---\n\n## 1. 页数评估\n\n### 估算方法\n逐 section 统计正文词数（Introduction → Conclusion），结合 ACL 两栏 11pt 格式经验值（~650 words/page body text），加上 float 和 overhead。\n\n| 组成 | 估算页面占用 |\n|------|-------------|\n| Title + Author + Abstract (~180 words) | ~0.40 page |\n| Introduction (~300 words) | ~0.46 page |\n| Method (~400 words, 含 itemized lists) | ~0.62 page |\n| Experiments (~430 words text) | ~0.66 page |\n| Table 1 + caption | ~0.20 page |\n| Table 2 + caption | ~0.25 page |\n| Figure 1 (\\columnwidth) + caption | ~0.30 page |\n| Figure 2 (\\columnwidth) + caption | ~0.30 page |\n| Discussion (~400 words, 含 Limitations ~150w) | ~0.62 page |\n| Related Work (~240 words) | ~0.37 page |\n| Conclusion (~170 words) | ~0.26 page |\n| Section/subsection headers + spacing | ~0.25 page |\n| **合计** | **~4.7 page** |\n\n**判定：正文极大概率超过 4 页。**\n\n### 操作建议\n\n**必做**：将 Discussion §4 末段 Limitations (~150 words) 拆为独立 `\\section*{Limitations}`。ACL 政策明确规定独立 Limitations section 不计入页数限制。这可节省 ~0.2 page。\n\n**仍然不够**（拆出后仍 ~4.5 page），需进一步压缩：\n1. **§3.5 Training-Evaluation Paradox**（~80 words + 具体数字）：核心发现可浓缩为 1 句并入 Discussion，详细数据移至 Appendix\n2. **Related Work**（~240 words）：当前 3 段结构合理但偏冗长，可压缩至 ~180 words——特别是 \"Training dynamics\" 段引用了 6 篇但只做了 1 句话的连接\n3. **Abstract**：~180 words 对 4-page short paper 偏长，建议压缩至 ~140 words（去掉 dose-response 的具体数字细节）\n4. **Method §2.2 Error Taxonomy**：4 个 operator 的 description 可以做一个紧凑的表格替代当前 itemized list，节省 ~0.1 page\n\n**优先级**：Limitations 拆出 > Paradox 移至 Appendix > 压缩 Related Work > 压缩 Abstract\n\n---\n\n## 2. Framing 评估：Claim 强度 vs 证据水平\n\n### Title 评估\nTitle \"Boundary Conditions from a Failed Transfer\" — **偏强**。\n\n\"Boundary conditions\" 暗示一组经过系统性验证的必要/充分条件。但本文仅测试：\n- 1 environment (ALFWorld)\n- 1 model (Qwen3-8B)\n- 仅 unpaired injection（未测试 recovery pairing）\n\n建议改为更审慎的表述，如 \"Hypotheses from...\" 或 \"Observations from...\"。\n\n### Conclusion 4-point Checklist 逐条评估\n\n**Criterion (1) \"discrete and observable errors\"** — ⚠️ 部分支撑\n- 证据：Appendix Table 3 structural comparison（tool-use: discrete API error codes vs embodied: diffuse errors）\n- 问题：这是基于任务结构的 a priori 分析，不是从实验数据中 derived 的 finding。论文未操纵 error observability 来测试这个假设\n\n**Criterion (2) \"local recovery\"** — ⚠️ 探索性支撑\n- 证据：§3.4 Figure 2 per-operator analysis，local errors +9.1pp vs global errors -8.3pp\n- 问题：N=11–12，仅 seed=42，±1 task ≈ ±8–9pp。效应量与噪声量级相当，无统计检验。论文正确标注 \"exploratory\"，但 Conclusion 将其升格为 checklist item 时未保留该 qualifier\n\n**Criterion (3) \"immediate feedback\"** — ❌ 自相矛盾\n- 证据：Appendix Table 3 列 embodied planning 为 \"Delayed\" feedback\n- 矛盾：Discussion §4 Limitations 段承认 ALFWorld 的 \"Nothing happens\" 反馈 \"partially resembles tool-use error observability\"\n- 问题：如果 ALFWorld 确实具有某种程度的 immediate feedback，那么 error injection 的失败就不能归因于缺乏 immediate feedback。这个 criterion 与论文自身的 limitation disclosure 直接冲突\n\n**Criterion (4) \"recovery pairing\"** — ❌ 未被测试\n- 证据：PALADIN 使用 recovery pairing 且成功，本文不使用且失败\n- 问题：这是一个 confound，不是一个 tested condition。论文在 Discussion §4 正确地将其识别为 confound（\"We cannot distinguish between these two hypotheses\"），但 Conclusion 将其作为 checklist 的第 4 条\"建议\"——这在逻辑上不一致。一个被明确承认为 confound 的因素不应成为 prescriptive checklist item\n- 作者自己说 \"Recovery-paired injection on ALFWorld is needed to disentangle these factors\"——在做这个实验之前，criterion (4) 只是假设\n\n**总体判定**：4 条 criteria 中，(1) 是 a priori structural analysis 非实验 finding，(2) 是 exploratory 且 underpowered，(3) 自相矛盾，(4) 未被测试。Checklist 应明确标注为 \"hypothesized boundary conditions requiring validation\" 而非隐含 \"derived from our results\"。Conclusion 最后一句 \"These criteria require validation in other environments\" 做了 hedge，但 hedge 范围不够——不仅需要在其他环境验证，(3) 和 (4) 在 ALFWorld 上都尚未被验证。\n\n---\n\n## 3. 数据呈现一致性\n\n### 3a. Table 2 Δ 列的 10% 行问题 [critical]\n\n**具体位置**：Table 2（§3.2, experiments.tex line 34–54）\n\n| 条件 | seed=42 | Δ (vs vanilla mean 65.3) | Δ (vs same-seed vanilla 61.7) |\n|------|---------|--------------------------|-------------------------------|\n| TaxEI 10% | 61.7 | **-3.6** | **0.0** |\n| Random 10% | 68.1 | **+2.8** | **+6.4** |\n\n- Δ 列对比 3-seed vanilla mean (65.3±3.3)，但 10% 行仅 seed=42\n- TaxEI 10% 的 -3.6pp \"degradation\" 完全来自其他 vanilla seeds（s0=68.1, s123=66.0）的上拉效应，而非 treatment effect\n- 同 seed 对比：TaxEI 10% = Vanilla seed=42 = 61.7%，Δ = 0pp\n- Random 10% 反向：Δ=+2.8 低估了同 seed 差异（+6.4pp）\n- 脚注 †Single seed 存在，但 Δ 值仍在同一列中呈现，读者自然理解为可比较的 treatment effect\n\n**影响**：读者可能误解 10% TaxEI \"轻微降低了 3.6pp\"，实际同 seed 完全无差异。这 undermines dose-response narrative 的起点。\n\n**建议**：10% 行的 Δ 应标注 \"N/A (single seed)\" 或改为 same-seed delta 并加注释说明。\n\n### 3b. Figure 1 vs Table 2 覆盖不一致 [warning]\n\n**具体位置**：Figure 1 caption（experiments.tex line 57–61）\n\nFigure 1 仅展示 seed=42 的 dose-response 曲线。Caption 说 \"3-seed data in Table 2 reveals non-monotonic dose-response with regime bifurcation at 25%→50%\"。\n\n问题：\n- 视觉上，Figure 1 呈现的是 **单调递降**（seed=42: 61.7% → 48.9% → 51.1%），不是 non-monotonic\n- Non-monotonic pattern（50% mean > 25% mean）只在 3-seed 数据中成立\n- 读者看到图的第一印象与 caption 声称的 pattern 不匹配\n\n**建议**：Figure 1 应展示 3-seed 数据（均值 + error bar），或至少标注 3-seed 均值作为参考线。\n\n### 3c. Recovery Evaluation 仅 seed=42 [critical]\n\n**具体位置**：§3.3（experiments.tex line 65–68）\n\nRecovery evaluation 结果：TaxEI 59.6%, Vanilla 61.7%, Random 63.8%（差异 1–4pp）。\n\n问题：\n1. 论文已建立 seed sensitivity 极高（SD≈12pp at 50%），但 recovery evaluation 仅 seed=42\n2. Seed=42 恰好是 TaxEI 在多个配置中表现最差的 seed（Table 1: s42=61.7 vs s123=61.7, s0=46.8 中最差；Table 2 50%: s42=51.1 是最低 seed）\n3. 1–4pp 的差异远小于已观察到的 seed variance (SD≈12pp)，无法区分 \"no effect\" 和 \"effect masked by seed choice\"\n4. 无统计检验（甚至无 confidence interval）报告\n\n**影响**：Recovery evaluation 是支撑 \"taxonomy labels were not internalized\" 结论的主要证据。单 seed + 无统计检验使这个结论不可靠。\n\n**建议**：至少在 Limitations 中明确说明 recovery evaluation 的单 seed 局限，或降级该结论为 \"preliminary observation\"。\n\n---\n\n## 4. Round 1 Must-Fix 快速确认\n\n基于当前论文状态，评估 Reviewer 1 报告的 4/5 resolved + 1 partially：\n\n| 推测的 Round 1 Must-Fix | 当前状态 | 我的判定 |\n|------------------------|---------|---------|\n| MF1: PALADIN confound 未披露 | Abstract/Intro/Discussion/Conclusion 四处明确说明 | ✅ **Resolved** — 同意 R1 |\n| MF2: 主结论过度声称 | 标题和正文有 hedge，但 boundary conditions checklist 仍偏强（见 §2） | ⚠️ **Partially Resolved** — 同意 R1 的 partially；checklist 需进一步弱化 |\n| MF3: 缺乏统计检验 | Permutation test + p-values 已加入 Table 1 | ✅ **Resolved** — 同意 R1 |\n| MF4: Data volume confound | Fixed-size dose-response ablation 已控制 | ✅ **Resolved** — 同意 R1 |\n| MF5: Limitations 缺失/不足 | Limitations 存在但嵌入 Discussion，覆盖了主要局限 | ⚠️ **Partially Resolved** — 同意 R1；需独立 section + 补充 recovery eval 的 single-seed limitation |\n\n**额外发现（R1 可能遗漏）：**\n- Table 2 的 10% single-seed Δ 问题未被 R1 提及（可能因为 Round 1 版本没有 dose-response table）\n- Recovery evaluation 的 single-seed 问题是新发现的 critical issue\n\n---\n\n## 5. 其他快速检查\n\n**Abstract 长度**：~180 words，对 4-page short paper 偏长。建议压缩至 ~140 words。\n\n**引用验证**：\n- 19 bib 条目，13 被 `\\cite` 引用，6 被 `\\shortcite` 引用（无真正 orphan）\n- 15/19 在线验证通过\n- 3 条 not_found（yao2023react, eef2025, agentdebug2025）：均为已知论文/新 arXiv 预印本，OpenAlex 未收录，非伪造\n- 1 条年份 mismatch：damour2022underspecification（bib=2022 JMLR 版，API=2020 arXiv 版）——bib 使用正式发表年份，合理\n\n**匿名性**：`\\usepackage[review]{acl}` + `\\author{Anonymous}`，合规。无匿名性泄露。\n\n**BibTeX 格式**：所有 author 字段使用 double-brace `{{Author, I.}}` 格式，会阻止 BibTeX 正确解析姓名。应改为标准格式 `{Last, First and ...}`。这是排版问题，不影响审稿决定。\n\n---\n\n## 总体评分\n\n### ACL ARR 维度打分\n\n| 维度 | 分数 | 理由 |\n|------|------|------|\n| **Soundness** | 3/5 (Acceptable) | 主要 negative result 有统计支撑；dose-response 分析有价值。但 recovery evaluation 仅单 seed 且无统计检验；Table 2 的 Δ 列对 single-seed 行存在误导；4-point checklist 中 2/4 条与自身证据矛盾或未被测试 |\n| **Excitement** | 3.5/5 | 对 Insights 这个 venue 很合适——systematically 记录了 cross-domain transfer 失败并提供了 dose-response 分析。Dual regime 发现（确定性降解 vs 混沌 seed 依赖）有独立学术价值 |\n| **Reproducibility** | 3.5/5 | Training setup 详细（LoRA config, seed, data sizes）。但 expert trajectory 收集细节不足；ALFWorld prompt format 未提供 |\n| **Overall** | 2.5/5 (Borderline Findings) | 论文有有价值的 negative result 和 dose-response 发现，适合 Insights venue。但页数问题（可能超页）、framing 过强（boundary conditions checklist）、recovery evaluation 统计不足是接收的 barrier |\n| **Confidence** | 4/5 | 仔细审读了全文和 references |\n\n### 一句话总结\n有价值的 negative result 论文，dose-response dual regime 是最有意义的贡献，但 4-point boundary conditions checklist 的 evidence basis 不足以支撑其 prescriptive framing，recovery evaluation 的单 seed 设计严重削弱了核心结论之一。\n\n### 接收建议\n**Borderline — lean weak reject**。如果作者能：(1) 确认页数合规，(2) 将 checklist 降级为 \"hypothesized conditions\"，(3) 修正 Table 2 Δ 列的 single-seed 呈现，论文可以达到 weak accept 水平。当前版本的 framing 问题和数据呈现不一致还不够 clean。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Conclusion 4-point checklist framing 过强\n- 具体位置：Conclusion §5, conclusion.tex line 6\n- 4 条 criteria 中 (3) 与 Discussion 自身矛盾，(4) 未被独立测试，(1)(2) 缺乏操纵性实验支撑\n- 建议：改为 \"We hypothesize four properties that may moderate error injection effectiveness, requiring validation: ...\"\n\n**N2** [critical] Table 2 Δ 列 single-seed 行误导\n- 具体位置：Table 2, experiments.tex line 34-54\n- 10% 行的 Δ 对比 3-seed mean 而非 same-seed vanilla，产生虚假的 -3.6pp / +2.8pp treatment effect\n- 建议：10% Δ 改为 same-seed delta 或标注 \"N/A\"\n\n**N3** [critical] Recovery evaluation (§3.3) 统计不足\n- 具体位置：§3.3, experiments.tex line 65-68\n- 仅 seed=42，无统计检验，差异 (1-4pp) 远小于已知 seed variance (SD≈12pp)\n- \"Taxonomy labels were not internalized\" 结论基于不可靠证据\n- 建议：降级为 \"preliminary single-seed observation\" 或补充多 seed 数据\n\n## Should-Fix 问题\n\n**W1** [warning] 页数可能超限\n- 估算 ~4.5 page（含 embedded Limitations）\n- 拆出 Limitations 后仍 ~4.3 page\n- 建议操作路径见 §1\n\n**W2** [warning] Figure 1 单 seed 视觉与 caption 描述的 3-seed pattern 不匹配\n- 具体位置：Figure 1, experiments.tex line 56-61\n- Figure 1 (seed=42) 呈现近单调递降，但 caption 声称 non-monotonic dose-response\n\n**W3** [warning] Title \"Boundary Conditions\" 措辞偏强\n- 单 environment + 单 model + 未测试 recovery pairing\n- 建议改为 \"Hypotheses\" 或 \"Observations\"\n\n## 小问题\n\n- Abstract ~180 words，对 short paper 偏长\n- BibTeX author 字段格式非标准（double-brace），可能导致排版异常\n- damour2022underspecification 年份应确认使用 JMLR 正式发表版 (2022) 而非 arXiv 版 (2020)\n\n## 主要优势\n\n- 系统性的 negative result 文档化，对 agent training community 有实际指导价值\n- Dose-dependent dual regime（25% 确定性降解 vs 50% 混沌）是原创且 well-supported 的发现（3-seed confirmed）\n- Recovery-pairing confound 的明确披露体现了诚实的科学态度\n- 实验设计合理：fixed-size ablation 控制了 data volume confound\n- 对 Insights from Negative Results 这个 venue 高度契合",
  "reviewer_id": "2",
  "project": "tax_error_inject_agent"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 — Round 2 聚焦审稿报告\n\n**论文**: \"When Does Unpaired Error Injection Help LLM Agents? Boundary Conditions from a Failed Transfer to Embodied Planning\"\n**Venue**: Insights from Negative Results in NLP @ EMNLP 2026\n**审查依据**: ACL ARR review form (Soundness / Excitement / Overall, 1–5 scale with half-point increments)\n\n---\n\n## 1. 页数评估\n\n### 估算方法\n逐 section 统计正文词数（Introduction → Conclusion），结合 ACL 两栏 11pt 格式经验值（~650 words/page body text），加上 float 和 overhead。\n\n| 组成 | 估算页面占用 |\n|------|-------------|\n| Title + Author + Abstract (~180 words) | ~0.40 page |\n| Introduction (~300 words) | ~0.46 page |\n| Method (~400 words, 含 itemized lists) | ~0.62 page |\n| Experiments (~430 words text) | ~0.66 page |\n| Table 1 + caption | ~0.20 page |\n| Table 2 + caption | ~0.25 page |\n| Figure 1 (\\columnwidth) + caption | ~0.30 page |\n| Figure 2 (\\columnwidth) + caption | ~0.30 page |\n| Discussion (~400 words, 含 Limitations ~150w) | ~0.62 page |\n| Related Work (~240 words) | ~0.37 page |\n| Conclusion (~170 words) | ~0.26 page |\n| Section/subsection headers + spacing | ~0.25 page |\n| **合计** | **~4.7 page** |\n\n**判定：正文极大概率超过 4 页。**\n\n### 操作建议\n\n**必做**：将 Discussion §4 末段 Limitations (~150 words) 拆为独立 `\\section*{Limitations}`。ACL 政策明确规定独立 Limitations section 不计入页数限制。这可节省 ~0.2 page。\n\n**仍然不够**（拆出后仍 ~4.5 page），需进一步压缩：\n1. **§3.5 Training-Evaluation Paradox**（~80 words + 具体数字）：核心发现可浓缩为 1 句并入 Discussion，详细数据移至 Appendix\n2. **Related Work**（~240 words）：当前 3 段结构合理但偏冗长，可压缩至 ~180 words——特别是 \"Training dynamics\" 段引用了 6 篇但只做了 1 句话的连接\n3. **Abstract**：~180 words 对 4-page short paper 偏长，建议压缩至 ~140 words（去掉 dose-response 的具体数字细节）\n4. **Method §2.2 Error Taxonomy**：4 个 operator 的 description 可以做一个紧凑的表格替代当前 itemized list，节省 ~0.1 page\n\n**优先级**：Limitations 拆出 > Paradox 移至 Appendix > 压缩 Related Work > 压缩 Abstract\n\n---\n\n## 2. Framing 评估：Claim 强度 vs 证据水平\n\n### Title 评估\nTitle \"Boundary Conditions from a Failed Transfer\" — **偏强**。\n\n\"Boundary conditions\" 暗示一组经过系统性验证的必要/充分条件。但本文仅测试：\n- 1 environment (ALFWorld)\n- 1 model (Qwen3-8B)\n- 仅 unpaired injection（未测试 recovery pairing）\n\n建议改为更审慎的表述，如 \"Hypotheses from...\" 或 \"Observations from...\"。\n\n### Conclusion 4-point Checklist 逐条评估\n\n**Criterion (1) \"discrete and observable errors\"** — ⚠️ 部分支撑\n- 证据：Appendix Table 3 structural comparison（tool-use: discrete API error codes vs embodied: diffuse errors）\n- 问题：这是基于任务结构的 a priori 分析，不是从实验数据中 derived 的 finding。论文未操纵 error observability 来测试这个假设\n\n**Criterion (2) \"local recovery\"** — ⚠️ 探索性支撑\n- 证据：§3.4 Figure 2 per-operator analysis，local errors +9.1pp vs global errors -8.3pp\n- 问题：N=11–12，仅 seed=42，±1 task ≈ ±8–9pp。效应量与噪声量级相当，无统计检验。论文正确标注 \"exploratory\"，但 Conclusion 将其升格为 checklist item 时未保留该 qualifier\n\n**Criterion (3) \"immediate feedback\"** — ❌ 自相矛盾\n- 证据：Appendix Table 3 列 embodied planning 为 \"Delayed\" feedback\n- 矛盾：Discussion §4 Limitations 段承认 ALFWorld 的 \"Nothing happens\" 反馈 \"partially resembles tool-use error observability\"\n- 问题：如果 ALFWorld 确实具有某种程度的 immediate feedback，那么 error injection 的失败就不能归因于缺乏 immediate feedback。这个 criterion 与论文自身的 limitation disclosure 直接冲突\n\n**Criterion (4) \"recovery pairing\"** — ❌ 未被测试\n- 证据：PALADIN 使用 recovery pairing 且成功，本文不使用且失败\n- 问题：这是一个 confound，不是一个 tested condition。论文在 Discussion §4 正确地将其识别为 confound（\"We cannot distinguish between these two hypotheses\"），但 Conclusion 将其作为 checklist 的第 4 条\"建议\"——这在逻辑上不一致。一个被明确承认为 confound 的因素不应成为 prescriptive checklist item\n- 作者自己说 \"Recovery-paired injection on ALFWorld is needed to disentangle these factors\"——在做这个实验之前，criterion (4) 只是假设\n\n**总体判定**：4 条 criteria 中，(1) 是 a priori structural analysis 非实验 finding，(2) 是 exploratory 且 underpowered，(3) 自相矛盾，(4) 未被测试。Checklist 应明确标注为 \"hypothesized boundary conditions requiring validation\" 而非隐含 \"derived from our results\"。Conclusion 最后一句 \"These criteria require validation in other environments\" 做了 hedge，但 hedge 范围不够——不仅需要在其他环境验证，(3) 和 (4) 在 ALFWorld 上都尚未被验证。\n\n---\n\n## 3. 数据呈现一致性\n\n### 3a. Table 2 Δ 列的 10% 行问题 [critical]\n\n**具体位置**：Table 2（§3.2, experiments.tex line 34–54）\n\n| 条件 | seed=42 | Δ (vs vanilla mean 65.3) | Δ (vs same-seed vanilla 61.7) |\n|------|---------|--------------------------|-------------------------------|\n| TaxEI 10% | 61.7 | **-3.6** | **0.0** |\n| Random 10% | 68.1 | **+2.8** | **+6.4** |\n\n- Δ 列对比 3-seed vanilla mean (65.3±3.3)，但 10% 行仅 seed=42\n- TaxEI 10% 的 -3.6pp \"degradation\" 完全来自其他 vanilla seeds（s0=68.1, s123=66.0）的上拉效应，而非 treatment effect\n- 同 seed 对比：TaxEI 10% = Vanilla seed=42 = 61.7%，Δ = 0pp\n- Random 10% 反向：Δ=+2.8 低估了同 seed 差异（+6.4pp）\n- 脚注 †Single seed 存在，但 Δ 值仍在同一列中呈现，读者自然理解为可比较的 treatment effect\n\n**影响**：读者可能误解 10% TaxEI \"轻微降低了 3.6pp\"，实际同 seed 完全无差异。这 undermines dose-response narrative 的起点。\n\n**建议**：10% 行的 Δ 应标注 \"N/A (single seed)\" 或改为 same-seed delta 并加注释说明。\n\n### 3b. Figure 1 vs Table 2 覆盖不一致 [warning]\n\n**具体位置**：Figure 1 caption（experiments.tex line 57–61）\n\nFigure 1 仅展示 seed=42 的 dose-response 曲线。Caption 说 \"3-seed data in Table 2 reveals non-monotonic dose-response with regime bifurcation at 25%→50%\"。\n\n问题：\n- 视觉上，Figure 1 呈现的是 **单调递降**（seed=42: 61.7% → 48.9% → 51.1%），不是 non-monotonic\n- Non-monotonic pattern（50% mean > 25% mean）只在 3-seed 数据中成立\n- 读者看到图的第一印象与 caption 声称的 pattern 不匹配\n\n**建议**：Figure 1 应展示 3-seed 数据（均值 + error bar），或至少标注 3-seed 均值作为参考线。\n\n### 3c. Recovery Evaluation 仅 seed=42 [critical]\n\n**具体位置**：§3.3（experiments.tex line 65–68）\n\nRecovery evaluation 结果：TaxEI 59.6%, Vanilla 61.7%, Random 63.8%（差异 1–4pp）。\n\n问题：\n1. 论文已建立 seed sensitivity 极高（SD≈12pp at 50%），但 recovery evaluation 仅 seed=42\n2. Seed=42 恰好是 TaxEI 在多个配置中表现最差的 seed（Table 1: s42=61.7 vs s123=61.7, s0=46.8 中最差；Table 2 50%: s42=51.1 是最低 seed）\n3. 1–4pp 的差异远小于已观察到的 seed variance (SD≈12pp)，无法区分 \"no effect\" 和 \"effect masked by seed choice\"\n4. 无统计检验（甚至无 confidence interval）报告\n\n**影响**：Recovery evaluation 是支撑 \"taxonomy labels were not internalized\" 结论的主要证据。单 seed + 无统计检验使这个结论不可靠。\n\n**建议**：至少在 Limitations 中明确说明 recovery evaluation 的单 seed 局限，或降级该结论为 \"preliminary observation\"。\n\n---\n\n## 4. Round 1 Must-Fix 快速确认\n\n基于当前论文状态，评估 Reviewer 1 报告的 4/5 resolved + 1 partially：\n\n| 推测的 Round 1 Must-Fix | 当前状态 | 我的判定 |\n|------------------------|---------|---------|\n| MF1: PALADIN confound 未披露 | Abstract/Intro/Discussion/Conclusion 四处明确说明 | ✅ **Resolved** — 同意 R1 |\n| MF2: 主结论过度声称 | 标题和正文有 hedge，但 boundary conditions checklist 仍偏强（见 §2） | ⚠️ **Partially Resolved** — 同意 R1 的 partially；checklist 需进一步弱化 |\n| MF3: 缺乏统计检验 | Permutation test + p-values 已加入 Table 1 | ✅ **Resolved** — 同意 R1 |\n| MF4: Data volume confound | Fixed-size dose-response ablation 已控制 | ✅ **Resolved** — 同意 R1 |\n| MF5: Limitations 缺失/不足 | Limitations 存在但嵌入 Discussion，覆盖了主要局限 | ⚠️ **Partially Resolved** — 同意 R1；需独立 section + 补充 recovery eval 的 single-seed limitation |\n\n**额外发现（R1 可能遗漏）：**\n- Table 2 的 10% single-seed Δ 问题未被 R1 提及（可能因为 Round 1 版本没有 dose-response table）\n- Recovery evaluation 的 single-seed 问题是新发现的 critical issue\n\n---\n\n## 5. 其他快速检查\n\n**Abstract 长度**：~180 words，对 4-page short paper 偏长。建议压缩至 ~140 words。\n\n**引用验证**：\n- 19 bib 条目，13 被 `\\cite` 引用，6 被 `\\shortcite` 引用（无真正 orphan）\n- 15/19 在线验证通过\n- 3 条 not_found（yao2023react, eef2025, agentdebug2025）：均为已知论文/新 arXiv 预印本，OpenAlex 未收录，非伪造\n- 1 条年份 mismatch：damour2022underspecification（bib=2022 JMLR 版，API=2020 arXiv 版）——bib 使用正式发表年份，合理\n\n**匿名性**：`\\usepackage[review]{acl}` + `\\author{Anonymous}`，合规。无匿名性泄露。\n\n**BibTeX 格式**：所有 author 字段使用 double-brace `{{Author, I.}}` 格式，会阻止 BibTeX 正确解析姓名。应改为标准格式 `{Last, First and ...}`。这是排版问题，不影响审稿决定。\n\n---\n\n## 总体评分\n\n### ACL ARR 维度打分\n\n| 维度 | 分数 | 理由 |\n|------|------|------|\n| **Soundness** | 3/5 (Acceptable) | 主要 negative result 有统计支撑；dose-response 分析有价值。但 recovery evaluation 仅单 seed 且无统计检验；Table 2 的 Δ 列对 single-seed 行存在误导；4-point checklist 中 2/4 条与自身证据矛盾或未被测试 |\n| **Excitement** | 3.5/5 | 对 Insights 这个 venue 很合适——systematically 记录了 cross-domain transfer 失败并提供了 dose-response 分析。Dual regime 发现（确定性降解 vs 混沌 seed 依赖）有独立学术价值 |\n| **Reproducibility** | 3.5/5 | Training setup 详细（LoRA config, seed, data sizes）。但 expert trajectory 收集细节不足；ALFWorld prompt format 未提供 |\n| **Overall** | 2.5/5 (Borderline Findings) | 论文有有价值的 negative result 和 dose-response 发现，适合 Insights venue。但页数问题（可能超页）、framing 过强（boundary conditions checklist）、recovery evaluation 统计不足是接收的 barrier |\n| **Confidence** | 4/5 | 仔细审读了全文和 references |\n\n### 一句话总结\n有价值的 negative result 论文，dose-response dual regime 是最有意义的贡献，但 4-point boundary conditions checklist 的 evidence basis 不足以支撑其 prescriptive framing，recovery evaluation 的单 seed 设计严重削弱了核心结论之一。\n\n### 接收建议\n**Borderline — lean weak reject**。如果作者能：(1) 确认页数合规，(2) 将 checklist 降级为 \"hypothesized conditions\"，(3) 修正 Table 2 Δ 列的 single-seed 呈现，论文可以达到 weak accept 水平。当前版本的 framing 问题和数据呈现不一致还不够 clean。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Conclusion 4-point checklist framing 过强\n- 具体位置：Conclusion §5, conclusion.tex line 6\n- 4 条 criteria 中 (3) 与 Discussion 自身矛盾，(4) 未被独立测试，(1)(2) 缺乏操纵性实验支撑\n- 建议：改为 \"We hypothesize four properties that may moderate error injection effectiveness, requiring validation: ...\"\n\n**N2** [critical] Table 2 Δ 列 single-seed 行误导\n- 具体位置：Table 2, experiments.tex line 34-54\n- 10% 行的 Δ 对比 3-seed mean 而非 same-seed vanilla，产生虚假的 -3.6pp / +2.8pp treatment effect\n- 建议：10% Δ 改为 same-seed delta 或标注 \"N/A\"\n\n**N3** [critical] Recovery evaluation (§3.3) 统计不足\n- 具体位置：§3.3, experiments.tex line 65-68\n- 仅 seed=42，无统计检验，差异 (1-4pp) 远小于已知 seed variance (SD≈12pp)\n- \"Taxonomy labels were not internalized\" 结论基于不可靠证据\n- 建议：降级为 \"preliminary single-seed observation\" 或补充多 seed 数据\n\n## Should-Fix 问题\n\n**W1** [warning] 页数可能超限\n- 估算 ~4.5 page（含 embedded Limitations）\n- 拆出 Limitations 后仍 ~4.3 page\n- 建议操作路径见 §1\n\n**W2** [warning] Figure 1 单 seed 视觉与 caption 描述的 3-seed pattern 不匹配\n- 具体位置：Figure 1, experiments.tex line 56-61\n- Figure 1 (seed=42) 呈现近单调递降，但 caption 声称 non-monotonic dose-response\n\n**W3** [warning] Title \"Boundary Conditions\" 措辞偏强\n- 单 environment + 单 model + 未测试 recovery pairing\n- 建议改为 \"Hypotheses\" 或 \"Observations\"\n\n## 小问题\n\n- Abstract ~180 words，对 short paper 偏长\n- BibTeX author 字段格式非标准（double-brace），可能导致排版异常\n- damour2022underspecification 年份应确认使用 JMLR 正式发表版 (2022) 而非 arXiv 版 (2020)\n\n## 主要优势\n\n- 系统性的 negative result 文档化，对 agent training community 有实际指导价值\n- Dose-dependent dual regime（25% 确定性降解 vs 50% 混沌）是原创且 well-supported 的发现（3-seed confirmed）\n- Recovery-pairing confound 的明确披露体现了诚实的科学态度\n- 实验设计合理：fixed-size ablation 控制了 data volume confound\n- 对 Insights from Negative Results 这个 venue 高度契合",
    "reviewer_id": "2",
    "project": "tax_error_inject_agent"
  }
}
```

</details>

---

### Tool result

_source line 105 · 2026-05-15T11:42:32.834124+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4017
}
```

</details>

---

### Assistant

_source line 106 · 2026-05-15T11:42:45.675713+00:00_

Round 2 聚焦审稿已完成并提交给 Director。

核心发现：

1. **页数**：估算 ~4.5 页，超限。即使拆出 Limitations 仍约 4.3 页，需额外压缩（Training-Evaluation Paradox 移至 Appendix、压缩 Related Work 等）。

2. **Framing**：Conclusion 的 4-point checklist 中，criterion (3) "immediate feedback" 与 Discussion 自身承认 ALFWorld 有 "Nothing happens" 反馈矛盾，criterion (4) "recovery pairing" 是被论文明确标记的 confound 却成了 prescriptive checklist item。建议降级为 "hypothesized conditions"。

3. **数据呈现**：Table 2 的 10% 行用单 seed 结果对比 3-seed vanilla mean 产生虚假的 Δ=-3.6pp（同 seed 实际为 0pp）；Recovery evaluation 仅 seed=42 且无统计检验，在已知 SD≈12pp 的情况下不足以支撑 "labels not internalized" 结论。

4. **Round 1 Must-Fix**：同意 Reviewer 1 的 4/5 resolved 判定，1 partially（Limitations 嵌入 + checklist 过强）。

**Overall**：2.5/5 (Borderline)，lean weak reject。修正 checklist framing、Table 2 呈现、页数后可达 weak accept。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2"
}
```

</details>

---

## Round 4

4 recorded events

### User

_source line 107 · 2026-05-15T11:43:20.979088+00:00_

[Round 2 审稿请求]:
## 交叉分享：Reviewer 1 的审稿意见

请逐条回应以下 Reviewer 1 的发现。对每个要点标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

### Reviewer 1 的 Must-Fix (1)

**R1-MF1** 页数仍存疑（预估 4.0–4.5 页）
- Limitations 嵌入 Discussion 占用正文空间，建议拆为独立 `\section*{Limitations}`
- 如仍超，压缩 §3.4–§3.6 或移 training-eval paradox 至 Appendix

### Reviewer 1 的 Should-Fix (2)

**R1-SF1** "Boundary Conditions" 措辞偏强
- 4 条 criteria 从 1 environment + 1 model 推导，criterion (4) 未被独立测试
- 建议 Title 改为 "Lessons from..." 或 Conclusion 用 "we hypothesize"

**R1-SF2** Recovery evaluation 仅 seed=42
- 论文已建立 seed sensitivity 极高，但 recovery eval 和 0% detection rate 均基于单 seed
- 建议补充至少 1 个额外 seed 或明确标注 "single-seed, preliminary"

### Reviewer 1 的 Minor (3)

**R1-M1** Figure 1 仅 seed=42，Table 2 有 3-seed——图表覆盖不一致
**R1-M2** 0% detection rate 讨论仅一句（§3.4），建议 Discussion 中呼应
**R1-M3** Conclusion criterion (3) "immediate feedback" 与 Discussion "partially resembling tool-use observability" 存在张力

### Reviewer 1 的 Round 1 Issue Resolution 判定
- 13/16 ✅ RESOLVED, 2 ⚠️ PARTIALLY（页数、boundary conditions 措辞）, 1 改进空间（detection rate 讨论）

### Reviewer 1 的 Overall Assessment
- Soundness 3.5/5, Excitement 3.0/5, Overall 3.0/5
- Borderline Accept
- 认为 recovery-pairing confound 处理出色，多 seed dose-response 数据质量好
- 主要保留意见：页数、recovery eval 单 seed、boundary conditions 措辞

---

请对以上每个要点给出 [AGREE] 或 [REBUT] 回应。特别关注你和 Reviewer 1 在以下问题上的分歧：
1. 页数预估差异（你估 ~4.7 page vs R1 估 4.0–4.5 page）
2. Overall 评分差异（你 2.5/5 vs R1 3.0/5）
3. Table 2 Δ 列问题（R1 未提及，你列为 critical）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---

### Tool call

_source line 108 · 2026-05-15T11:44:49.135043+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

````json
{
  "text": "## Reviewer 2 — 交叉回应 Reviewer 1\n\n---\n\n### Must-Fix\n\n**[AGREE] R1-MF1: 页数仍存疑**\n\n同意方向，但我的估算更悲观。R1 估 4.0–4.5 page，我估 ~4.7 page。差异来源：\n\n1. R1 可能低估了 float 占用。论文有 2 个 `\\columnwidth` figure + 2 个 table，在 ACL 两栏格式中 float 通常被推至 column top，与正文争夺空间。我逐项计算 float 高度（Table 1 ~0.20p, Table 2 ~0.25p, Fig1 ~0.30p, Fig2 ~0.30p = ~1.05p），R1 似乎按 \"2 tables + 2 figures\" 整体估算\n2. Experiments 有 6 个 subsection（§3.1–§3.6），每个 `\\subsection{}` header + 前后 spacing 占 ~2–3 行。6 个 subsection headers ≈ 0.1 page，加上 Discussion 的 4 个 `\\paragraph{}` headers\n\n**核心共识**：拆出 Limitations 是必做项，但可能不够。R1 建议的 \"压缩 §3.4–§3.6 或移 training-eval paradox 至 Appendix\" 我完全同意——§3.5 Training-Evaluation Paradox (~80 words) 的核心发现可浓缩为 Discussion 中 1 句话，详细数据移至 Appendix。\n\n**补充建议**：即使无法编译 PDF 确认，安全起见应按 ~4.5+ page 准备压缩方案，而非赌 4.0 page 的乐观估计。\n\n---\n\n### Should-Fix\n\n**[AGREE] R1-SF1: \"Boundary Conditions\" 措辞偏强**\n\n完全同意，且我认为问题比 R1 描述的更严重。\n\nR1 指出 criterion (4) 未被独立测试——正确。但我的审查进一步发现：\n- **Criterion (3) \"immediate feedback\" 与论文自身矛盾**：Discussion §4 Limitations 承认 ALFWorld 的 \"Nothing happens\" 反馈 \"partially resembles tool-use error observability\"（discussion.tex line 14）。如果 ALFWorld 已部分具备 immediate feedback，error injection 仍失败，则 criterion (3) 的因果推理不成立\n- **Criterion (1)(2) 缺乏操纵性实验**：均基于 structural comparison（Appendix Table 3）的 a priori 分析，非从实验数据中 derived\n\n4 条 criteria 的 evidence basis：(1) a priori 分析，(2) exploratory N=11–12 单 seed，(3) 自相矛盾，(4) 未测试。R1 建议的 \"we hypothesize\" 修改是最低限度的修复。我建议更进一步：Conclusion 的 checklist 应明确标注 \"hypothesized conditions requiring validation even on ALFWorld itself\"——因为 (3)(4) 不仅需要 cross-environment 验证，在 ALFWorld 上都尚未被验证。\n\n**[AGREE] R1-SF2: Recovery evaluation 仅 seed=42**\n\n完全同意。我在独立审查中同样将此列为 critical issue（我的 N3），理由与 R1 一致但补充了定量论证：\n\n- Recovery evaluation 的条件间差异仅 1–4pp（TaxEI 59.6% vs Vanilla 61.7% vs Random 63.8%）\n- 论文已建立的 seed variance SD≈12pp（Table 2, 50% 行）\n- 1–4pp 差异 / 12pp SD ≈ 0.1–0.3 个标准差，完全在噪声范围内\n- 更关键：seed=42 恰好是 TaxEI 在多个配置中表现最差的 seed（Table 1 s42=61.7 是 TaxEI 3 seed 中并列最低；Table 2 50% s42=51.1 是最低）\n\nR1 建议 \"补充至少 1 个额外 seed 或明确标注 single-seed, preliminary\"。我认为后者（明确标注）是最低要求，但补充 seed 应作为强烈建议——因为 \"taxonomy labels were not internalized\"（§3.3）是论文的一个关键 mechanistic claim，不应建立在单 seed 无统计检验的基础上。\n\n---\n\n### Minor\n\n**[AGREE] R1-M1: Figure 1 vs Table 2 覆盖不一致**\n\n同意。我在独立审查中列为 W2 (warning)。补充一个 R1 未提及的具体问题：Figure 1（seed=42）呈现近单调递降（61.7% → 48.9% → 51.1%），但 caption 声称 \"non-monotonic dose-response with regime bifurcation\"——这个 non-monotonic pattern 只在 3-seed 均值中成立（25% mean 47.5% → 50% mean 56.0%）。图的视觉印象与 caption 描述的 pattern 不匹配。建议 Figure 1 改为展示 3-seed 数据（均值 + error bar）。\n\n**[AGREE] R1-M2: 0% detection rate 讨论不足**\n\n同意。§3.3 仅一句 \"The uniform 0% detection rate suggests taxonomy labels were not internalized during SFT\"（experiments.tex line 68）。这是一个有意义的 negative finding——如果模型完全没有学到 error classification 能力，这对 \"taxonomy-guided injection 是否有机制性优势\" 这个核心问题有重要含义。应在 Discussion 中用 1–2 句呼应，讨论为什么 SFT 未能 internalize taxonomy labels（可能原因：error-type labels 仅作为 prompt prefix 出现，训练目标是 next-token prediction 而非 classification）。\n\n**[AGREE] R1-M3: Criterion (3) \"immediate feedback\" 与 Discussion 矛盾**\n\n强烈同意。这是我在 §2 Framing 评估中标注为 ❌ 的问题。R1 将其列为 Minor，我认为应升级为 Should-Fix——因为这不仅是措辞不一致，而是 undermines checklist 的逻辑基础。如果 ALFWorld \"partially resembles tool-use observability\"（作者自己的话），那么 error injection 在 ALFWorld 上的失败就不能用 \"lack of immediate feedback\" 解释。这直接影响 Conclusion 的 4-point checklist 的可信度。\n\n---\n\n### Round 1 Resolution 判定\n\n**[AGREE]** R1 判定 13/16 resolved, 2 partially, 1 改进空间——我同意这个整体评估。论文在 Round 1 → Round 2 的修订中做了实质性改进，特别是：\n- Recovery-pairing confound 的 4 处明确披露（做得出色）\n- 统计检验的加入（permutation test + p-values）\n- Fixed-size dose-response ablation 控制 data volume confound\n\n剩余问题集中在 framing calibration（boundary conditions 措辞）和统计覆盖面（recovery eval 单 seed）。\n\n---\n\n### 三个分歧点的回应\n\n#### 分歧 1: 页数预估（R2 ~4.7p vs R1 4.0–4.5p）\n\n差异不影响结论——两个估算都指向 \"可能超页，需要压缩\"。精确页数需要编译 PDF 确认。但我认为按更保守的估计准备压缩方案更安全：如果实际 4.5+ page，仅拆 Limitations 不够；如果实际 4.1 page，拆 Limitations 就解决了。压缩 §3.5 → Appendix 无论如何都是好建议（改善 paper flow）。\n\n**建议 Director**：如果可以编译 PDF，以实际编译结果为准。如果不能，按 4.3–4.5 page 的中间估计做压缩预案。\n\n#### 分歧 2: Overall 评分（R2 2.5/5 vs R1 3.0/5）\n\n0.5 分差异来源：\n\n**R1 给 3.0 (Findings level) 的理由**：认为 recovery-pairing confound 处理出色 + 多 seed dose-response 数据质量好 → Borderline Accept。\n\n**我给 2.5 (Borderline Findings) 的理由**：在 R1 认可的优点之外，我发现了 3 个 R1 未提及的问题——Table 2 Δ 列 single-seed 误导（我的 N2）、criterion (3) 的自相矛盾（R1 仅列为 Minor）、4-point checklist 的整体 evidence basis 不足。这些问题叠加起来，使我对论文的 soundness 评估低于 R1（我给 3.0 vs R1 给 3.5）。\n\n**我愿意调整的条件**：如果作者能解决 N1（checklist 降级为 hypothesized）+ N2（Table 2 Δ 列修正）+ 页数合规，我会上调至 3.0/5。当前 2.5 反映的是 \"论文有 fixable 的问题但尚未 fix\" 的状态。\n\n**对 Insights venue 的校准**：这个 workshop 专门接收 negative results，审查标准应侧重 \"negative result 是否 well-documented and informative\" 而非 \"是否有 strong positive contribution\"。从这个角度，dose-response dual regime 是一个 genuinely informative finding。我的 2.5 不是对论文价值的否定，而是对当前 framing + 数据呈现质量的技术性评估。\n\n#### 分歧 3: Table 2 Δ 列问题（R1 未提及，R2 列为 critical）\n\n这是我和 R1 最大的分歧点。具体论证：\n\nTable 2 的 10% 行（experiments.tex line 42）：\n```\n10%† & 61.7 & --- & --- & 61.7 & −3.6\n```\n\n- TaxEI 10% seed=42 = 61.7%\n- Vanilla seed=42 = 61.7%（Table 1, experiments.tex line 18）\n- **同 seed 对比：完全无差异（0.0pp）**\n- Δ = -3.6pp 完全来自 vanilla 其他 seeds 的均值拉升效应\n\n这不是 nitpick。Dose-response 分析的叙事是 \"从 10% 的轻微降解到 25% 的严重降解再到 50% 的混沌\"。但如果 10% 实际是 0.0pp（同 seed），叙事起点就不成立——dose-response 曲线的形状在最低剂量点被人为扭曲了。\n\nR1 可能因为以下原因未标注此问题：\n1. 将 †Single seed 脚注视为充分披露\n2. 未将 Table 1 的 per-seed vanilla 数据与 Table 2 的 Δ 列交叉验证\n3. 关注重心在 25%/50% 的多 seed 数据（那些数据确实更可靠）\n\n**我的判定**：维持 critical。不需要作者重跑实验——只需将 10% Δ 改为 same-seed delta 或 \"N/A\"，并在文字中注明 \"At 10% (single seed), TaxEI matches same-seed vanilla exactly\"。这是一个 0 成本的修复，能显著提升数据呈现的诚实度。\n\n---\n\n### 汇总建议给 Director\n\n**R1 和 R2 的共识区域**（高置信度）：\n1. 页数需要压缩（拆 Limitations + 移 §3.5 至 Appendix）\n2. \"Boundary Conditions\" 措辞需弱化\n3. Recovery evaluation 单 seed 是显著局限\n4. Figure 1 应改进为 3-seed 展示\n5. 论文的 dose-response dual regime 发现有独立价值\n6. Recovery-pairing confound 的处理出色\n\n**R2 独立发现（R1 未覆盖）**：\n1. Table 2 Δ 列 10% 行的 single-seed vs multi-seed mean 对比问题 [critical]\n2. Criterion (3) \"immediate feedback\" 的自相矛盾严重性（R1 列 Minor，R2 认为应升级）\n3. 4-point checklist 整体 evidence basis 的系统性不足（不仅是 criterion 4）\n\n**建议最终评分区间**：Borderline（2.5–3.0/5），取决于作者对上述问题的修复程度。",
  "reviewer_id": "2",
  "project": "tax_error_inject_agent"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 — 交叉回应 Reviewer 1\n\n---\n\n### Must-Fix\n\n**[AGREE] R1-MF1: 页数仍存疑**\n\n同意方向，但我的估算更悲观。R1 估 4.0–4.5 page，我估 ~4.7 page。差异来源：\n\n1. R1 可能低估了 float 占用。论文有 2 个 `\\columnwidth` figure + 2 个 table，在 ACL 两栏格式中 float 通常被推至 column top，与正文争夺空间。我逐项计算 float 高度（Table 1 ~0.20p, Table 2 ~0.25p, Fig1 ~0.30p, Fig2 ~0.30p = ~1.05p），R1 似乎按 \"2 tables + 2 figures\" 整体估算\n2. Experiments 有 6 个 subsection（§3.1–§3.6），每个 `\\subsection{}` header + 前后 spacing 占 ~2–3 行。6 个 subsection headers ≈ 0.1 page，加上 Discussion 的 4 个 `\\paragraph{}` headers\n\n**核心共识**：拆出 Limitations 是必做项，但可能不够。R1 建议的 \"压缩 §3.4–§3.6 或移 training-eval paradox 至 Appendix\" 我完全同意——§3.5 Training-Evaluation Paradox (~80 words) 的核心发现可浓缩为 Discussion 中 1 句话，详细数据移至 Appendix。\n\n**补充建议**：即使无法编译 PDF 确认，安全起见应按 ~4.5+ page 准备压缩方案，而非赌 4.0 page 的乐观估计。\n\n---\n\n### Should-Fix\n\n**[AGREE] R1-SF1: \"Boundary Conditions\" 措辞偏强**\n\n完全同意，且我认为问题比 R1 描述的更严重。\n\nR1 指出 criterion (4) 未被独立测试——正确。但我的审查进一步发现：\n- **Criterion (3) \"immediate feedback\" 与论文自身矛盾**：Discussion §4 Limitations 承认 ALFWorld 的 \"Nothing happens\" 反馈 \"partially resembles tool-use error observability\"（discussion.tex line 14）。如果 ALFWorld 已部分具备 immediate feedback，error injection 仍失败，则 criterion (3) 的因果推理不成立\n- **Criterion (1)(2) 缺乏操纵性实验**：均基于 structural comparison（Appendix Table 3）的 a priori 分析，非从实验数据中 derived\n\n4 条 criteria 的 evidence basis：(1) a priori 分析，(2) exploratory N=11–12 单 seed，(3) 自相矛盾，(4) 未测试。R1 建议的 \"we hypothesize\" 修改是最低限度的修复。我建议更进一步：Conclusion 的 checklist 应明确标注 \"hypothesized conditions requiring validation even on ALFWorld itself\"——因为 (3)(4) 不仅需要 cross-environment 验证，在 ALFWorld 上都尚未被验证。\n\n**[AGREE] R1-SF2: Recovery evaluation 仅 seed=42**\n\n完全同意。我在独立审查中同样将此列为 critical issue（我的 N3），理由与 R1 一致但补充了定量论证：\n\n- Recovery evaluation 的条件间差异仅 1–4pp（TaxEI 59.6% vs Vanilla 61.7% vs Random 63.8%）\n- 论文已建立的 seed variance SD≈12pp（Table 2, 50% 行）\n- 1–4pp 差异 / 12pp SD ≈ 0.1–0.3 个标准差，完全在噪声范围内\n- 更关键：seed=42 恰好是 TaxEI 在多个配置中表现最差的 seed（Table 1 s42=61.7 是 TaxEI 3 seed 中并列最低；Table 2 50% s42=51.1 是最低）\n\nR1 建议 \"补充至少 1 个额外 seed 或明确标注 single-seed, preliminary\"。我认为后者（明确标注）是最低要求，但补充 seed 应作为强烈建议——因为 \"taxonomy labels were not internalized\"（§3.3）是论文的一个关键 mechanistic claim，不应建立在单 seed 无统计检验的基础上。\n\n---\n\n### Minor\n\n**[AGREE] R1-M1: Figure 1 vs Table 2 覆盖不一致**\n\n同意。我在独立审查中列为 W2 (warning)。补充一个 R1 未提及的具体问题：Figure 1（seed=42）呈现近单调递降（61.7% → 48.9% → 51.1%），但 caption 声称 \"non-monotonic dose-response with regime bifurcation\"——这个 non-monotonic pattern 只在 3-seed 均值中成立（25% mean 47.5% → 50% mean 56.0%）。图的视觉印象与 caption 描述的 pattern 不匹配。建议 Figure 1 改为展示 3-seed 数据（均值 + error bar）。\n\n**[AGREE] R1-M2: 0% detection rate 讨论不足**\n\n同意。§3.3 仅一句 \"The uniform 0% detection rate suggests taxonomy labels were not internalized during SFT\"（experiments.tex line 68）。这是一个有意义的 negative finding——如果模型完全没有学到 error classification 能力，这对 \"taxonomy-guided injection 是否有机制性优势\" 这个核心问题有重要含义。应在 Discussion 中用 1–2 句呼应，讨论为什么 SFT 未能 internalize taxonomy labels（可能原因：error-type labels 仅作为 prompt prefix 出现，训练目标是 next-token prediction 而非 classification）。\n\n**[AGREE] R1-M3: Criterion (3) \"immediate feedback\" 与 Discussion 矛盾**\n\n强烈同意。这是我在 §2 Framing 评估中标注为 ❌ 的问题。R1 将其列为 Minor，我认为应升级为 Should-Fix——因为这不仅是措辞不一致，而是 undermines checklist 的逻辑基础。如果 ALFWorld \"partially resembles tool-use observability\"（作者自己的话），那么 error injection 在 ALFWorld 上的失败就不能用 \"lack of immediate feedback\" 解释。这直接影响 Conclusion 的 4-point checklist 的可信度。\n\n---\n\n### Round 1 Resolution 判定\n\n**[AGREE]** R1 判定 13/16 resolved, 2 partially, 1 改进空间——我同意这个整体评估。论文在 Round 1 → Round 2 的修订中做了实质性改进，特别是：\n- Recovery-pairing confound 的 4 处明确披露（做得出色）\n- 统计检验的加入（permutation test + p-values）\n- Fixed-size dose-response ablation 控制 data volume confound\n\n剩余问题集中在 framing calibration（boundary conditions 措辞）和统计覆盖面（recovery eval 单 seed）。\n\n---\n\n### 三个分歧点的回应\n\n#### 分歧 1: 页数预估（R2 ~4.7p vs R1 4.0–4.5p）\n\n差异不影响结论——两个估算都指向 \"可能超页，需要压缩\"。精确页数需要编译 PDF 确认。但我认为按更保守的估计准备压缩方案更安全：如果实际 4.5+ page，仅拆 Limitations 不够；如果实际 4.1 page，拆 Limitations 就解决了。压缩 §3.5 → Appendix 无论如何都是好建议（改善 paper flow）。\n\n**建议 Director**：如果可以编译 PDF，以实际编译结果为准。如果不能，按 4.3–4.5 page 的中间估计做压缩预案。\n\n#### 分歧 2: Overall 评分（R2 2.5/5 vs R1 3.0/5）\n\n0.5 分差异来源：\n\n**R1 给 3.0 (Findings level) 的理由**：认为 recovery-pairing confound 处理出色 + 多 seed dose-response 数据质量好 → Borderline Accept。\n\n**我给 2.5 (Borderline Findings) 的理由**：在 R1 认可的优点之外，我发现了 3 个 R1 未提及的问题——Table 2 Δ 列 single-seed 误导（我的 N2）、criterion (3) 的自相矛盾（R1 仅列为 Minor）、4-point checklist 的整体 evidence basis 不足。这些问题叠加起来，使我对论文的 soundness 评估低于 R1（我给 3.0 vs R1 给 3.5）。\n\n**我愿意调整的条件**：如果作者能解决 N1（checklist 降级为 hypothesized）+ N2（Table 2 Δ 列修正）+ 页数合规，我会上调至 3.0/5。当前 2.5 反映的是 \"论文有 fixable 的问题但尚未 fix\" 的状态。\n\n**对 Insights venue 的校准**：这个 workshop 专门接收 negative results，审查标准应侧重 \"negative result 是否 well-documented and informative\" 而非 \"是否有 strong positive contribution\"。从这个角度，dose-response dual regime 是一个 genuinely informative finding。我的 2.5 不是对论文价值的否定，而是对当前 framing + 数据呈现质量的技术性评估。\n\n#### 分歧 3: Table 2 Δ 列问题（R1 未提及，R2 列为 critical）\n\n这是我和 R1 最大的分歧点。具体论证：\n\nTable 2 的 10% 行（experiments.tex line 42）：\n```\n10%† & 61.7 & --- & --- & 61.7 & −3.6\n```\n\n- TaxEI 10% seed=42 = 61.7%\n- Vanilla seed=42 = 61.7%（Table 1, experiments.tex line 18）\n- **同 seed 对比：完全无差异（0.0pp）**\n- Δ = -3.6pp 完全来自 vanilla 其他 seeds 的均值拉升效应\n\n这不是 nitpick。Dose-response 分析的叙事是 \"从 10% 的轻微降解到 25% 的严重降解再到 50% 的混沌\"。但如果 10% 实际是 0.0pp（同 seed），叙事起点就不成立——dose-response 曲线的形状在最低剂量点被人为扭曲了。\n\nR1 可能因为以下原因未标注此问题：\n1. 将 †Single seed 脚注视为充分披露\n2. 未将 Table 1 的 per-seed vanilla 数据与 Table 2 的 Δ 列交叉验证\n3. 关注重心在 25%/50% 的多 seed 数据（那些数据确实更可靠）\n\n**我的判定**：维持 critical。不需要作者重跑实验——只需将 10% Δ 改为 same-seed delta 或 \"N/A\"，并在文字中注明 \"At 10% (single seed), TaxEI matches same-seed vanilla exactly\"。这是一个 0 成本的修复，能显著提升数据呈现的诚实度。\n\n---\n\n### 汇总建议给 Director\n\n**R1 和 R2 的共识区域**（高置信度）：\n1. 页数需要压缩（拆 Limitations + 移 §3.5 至 Appendix）\n2. \"Boundary Conditions\" 措辞需弱化\n3. Recovery evaluation 单 seed 是显著局限\n4. Figure 1 应改进为 3-seed 展示\n5. 论文的 dose-response dual regime 发现有独立价值\n6. Recovery-pairing confound 的处理出色\n\n**R2 独立发现（R1 未覆盖）**：\n1. Table 2 Δ 列 10% 行的 single-seed vs multi-seed mean 对比问题 [critical]\n2. Criterion (3) \"immediate feedback\" 的自相矛盾严重性（R1 列 Minor，R2 认为应升级）\n3. 4-point checklist 整体 evidence basis 的系统性不足（不仅是 criterion 4）\n\n**建议最终评分区间**：Borderline（2.5–3.0/5），取决于作者对上述问题的修复程度。",
    "reviewer_id": "2",
    "project": "tax_error_inject_agent"
  }
}
````

</details>

---

### Tool result

_source line 109 · 2026-05-15T11:44:52.949794+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3814
}
```

</details>

---

### Assistant

_source line 110 · 2026-05-15T11:45:01.374975+00:00_

交叉回应已提交。对 R1 的 6 个要点全部标注 [AGREE]，同时在 3 个分歧点上给出了详细论证：

1. **页数**：共识需压缩，我的估算更保守（~4.7p vs R1 4.0–4.5p），建议按中间值准备方案
2. **评分差异**（2.5 vs 3.0）：源于我发现的 Table 2 Δ 列问题和 criterion (3) 矛盾的严重性评估——如果作者修复 checklist framing + Table 2 Δ 列，我愿意上调至 3.0
3. **Table 2 Δ 列**：维持 critical——10% TaxEI 同 seed 对比实际 Δ=0.0pp 而非报告的 -3.6pp，扭曲了 dose-response 叙事的起点，0 成本可修复

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_8acbea284219b548bfc4c50949ea43a8:reviewer_2"
}
```

</details>

---
