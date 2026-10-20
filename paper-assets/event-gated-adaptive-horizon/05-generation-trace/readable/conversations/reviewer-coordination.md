# Reviewer coordination

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 64
- **Recorded user turns:** 2
- **Tool calls:** 30
- **Original source:** `logs/chats/feishu_group_oc_dd4a07a509df7e5f9a31d65f776059bc_reviewer_3.jsonl`
- **Structured JSON:** [`af4d68ff6978b38e9c97.json`](../../sessions/af/af4d68ff6978b38e9c97.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

54 recorded events

### User

_source line 1 · 2026-05-15T12:29:59.035721+00:00_

[Round 1 审稿请求]:
## Round 1 审稿任务 — Reviewer 3

**你的审查侧重：格式合规 & 写作质量 & 呈现清晰度**

### 投稿信息
- **Venue**: CoRL 2026 Main Conference
- **Deadline**: 2026-05-29 (abstract: 2026-05-26)
- **格式要求**: 8页正文, PMLR模板 (`\usepackage[final]{corl_2026}`), double-blind, 须包含 Limitations section
- **匿名规则**: Double-blind（不可泄露作者身份）
- **论文路径**: `projects/event-gated-adaptive-horizon/docs/paper/main.tex`（含7个分节 .tex 文件）
- **模板**: 官方 LaTeX template 使用 `\usepackage[final]{corl_2026}`，基于 PMLR 格式

### 论文概述
标题："Why Temporal Abstraction Fails in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3"

诊断性论文，factorial ablation 分析 DreamerV3 中 variable-rate imagination 失败的原因。

### 你需要重点审查
1. **模板合规**：当前论文使用 `\documentclass[10pt,letterpaper,twocolumn]{article}` + `\usepackage[margin=0.75in]{geometry}`，**未使用 CoRL 官方 PMLR 模板**。这是否会导致 desk reject？
2. **页数合规**：检查正文是否在8页以内（不含参考文献和附录）
3. **Double-blind 合规**：
   - 作者信息是否正确匿名化？（当前显示 "Anonymous Authors"）
   - 正文中是否有泄露身份的线索（如 self-citation 用第一人称、GitHub 链接、致谢等）？
4. **Limitations Section**：CoRL 2026 要求包含 Limitations section。检查是否存在及质量。
5. **写作质量**：
   - Abstract 是否过长？是否清晰传达核心贡献？
   - Introduction 的叙事是否引人入胜？
   - Figures/Tables 是否 self-contained（caption 足够描述内容）？
   - 术语是否一致（CIVO, NVE, dt-embedding 等首次出现是否定义）？
6. **图表质量**：引用了 fig1-fig6 的 PDF 文件，检查路径和命名是否一致
7. **参考文献格式**：使用 natbib + plainnat，是否符合 PMLR 惯例？
8. **Supplementary materials**：是否需要附录或补充材料？

请按标准学术审稿格式输出：Summary → Strengths → Weaknesses → Questions → Minor Issues → Overall Assessment (1-10分)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_3",
  "source": "review_reviewer_3"
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-15T12:30:07.903029+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_3",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-15T12:30:08.515112+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/.claude/sessions/review_reviewer_3_2f53b6cb.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_3",
  "tool": "Read",
  "elapsed_ms": 612
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-15T12:30:08.566054+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_3",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references",
    "max_results": "4"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-15T12:30:08.566561+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_3",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-15T12:30:12.461875+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_3",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-15T12:30:12.926120+00:00_

1	\documentclass[10pt,letterpaper,twocolumn]{article}
2	\usepackage[utf8]{inputenc}
3	\usepackage[T1]{fontenc}
4	\usepackage{amsmath,amssymb}
5	\usepackage{booktabs}
6	\usepackage{multirow}
7	\usepackage{graphicx}
8	\graphicspath{{../../artifacts/}}
9	\usepackage[table]{xcolor}
10	\usepackage{colortbl}
11	\usepackage[margin=0.75in]{geometry}
12	\usepackage[colorlinks,citecolor=blue,urlcolor=blue,linkcolor=blue]{hyperref}
13	\usepackage{natbib}
14	\usepackage{caption}
15	\usepackage{subcaption}
16	\usepackage{array}
17	\usepackage{enumitem}
18	\usepackage{wrapfig}
19	
20	% Custom commands
21	\newcommand{\dt}{\mathrm{dt}}
22	\newcommand{\nve}{\mathrm{nve}}
23	\newcommand{\ie}{\textit{i.e.}}
24	\newcommand{\eg}{\textit{e.g.}}
25	\newcommand{\cf}{\textit{cf.}}
26	\newcommand{\etal}{\textit{et al.}}
27	
28	\title{Why Temporal Abstraction Fails in Imagination-Based RL:\\
29	A Diagnostic Analysis of Variable-Rate DreamerV3}
30	
31	\author{Anonymous Authors}
32	\date{}
33	
34	\begin{document}
35	\maketitle
36	
37	% --- ABSTRACT ---
38	\input{sections/abstract}
39	
40	% --- INTRODUCTION ---
41	\input{sections/introduction}
42	
43	% --- RELATED WORK ---
44	\input{sections/related_work}
45	
46	% --- METHODOLOGY ---
47	\input{sections/methodology}
48	
49	% --- RESULTS ---
50	\input{sections/results}
51	
52	% --- ANALYSIS ---
53	\input{sections/analysis}
54	
55	% --- CONCLUSION ---
56	\input{sections/conclusion}
57	
58	\bibliographystyle{plainnat}
59	\bibliography{references}
60	
61	\end{document}
62	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_3",
  "tool": "Read",
  "elapsed_ms": 464
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-15T12:30:12.927638+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoRL 2026 reviewer guidelines review form criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_3",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-15T12:30:13.281767+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoRL 2025 2026 review form scoring criteria dimensions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_3",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL 2025 2026 review form scoring criteria dimensions"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T12:30:18.801166+00:00_

Web search results for query: "CoRL 2026 reviewer guidelines review form criteria"

Links: [{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"ICLR 2026 Reviewer Guide","url":"https://iclr.cc/Conferences/2026/ReviewerGuide"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"CoRL 2026 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference"},{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"CVPR 2026 Reviewer Guidelines","url":"https://cvpr.thecvf.com/Conferences/2026/ReviewerGuidelinesq"},{"title":"Robot Learning Foundation","url":"https://www.robot-learning.org/"},{"title":"CoRL 2024 - Instruction for Reviews","url":"https://2024.corl.org/contributions/instruction-for-reviews"},{"title":"Reviewer Guidelines — CoRL 2023","url":"https://www.corl2023.org/reviewer-guidelines"},{"title":"2026 Reviewer Guidelines","url":"https://neurips.cc/Conferences/2026/ReviewerGuidelines"}]

Based on the search results, I found limited specific information about CoRL 2026 reviewer guidelines and review form criteria. The most detailed information available comes from the CoRL 2024 reviewer guidelines, which may provide insight into the review process structure.

For regular papers, submissions will be evaluated based on the significance and novelty of the results, either theoretical or empirical.

The search results also show that CoRL aims to have at least two reviewers per paper.

However, the search results do not contain a complete CoRL 2026-specific reviewer guidelines document with detailed review form criteria. The most recent detailed reviewer guidelines I found were from CoRL 2023, which included criteria such as:

- Relevance: whether the paper addresses a problem in robot learning, applies or improves a learning-based method, is evaluated in simulation or on real robots, and wi
…[truncated 563 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_3",
  "tool": "WebSearch",
  "elapsed_ms": 5873
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-15T12:30:32.424268+00:00_

Web search results for query: "CoRL 2025 2026 review form scoring criteria dimensions"

Links: [{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"CORL 2025 Statistics - Paper Copilot","url":"https://papercopilot.com/statistics/corl-statistics/corl-2025-statistics/"},{"title":"CoRL 2025 Accepted Paper List - Paper Copilot","url":"https://papercopilot.com/paper-list/corl-paper-list/corl-2025-paper-list/"},{"title":"CoRL 2025","url":"https://2025.corl.org/"},{"title":"CoRL 2025 | OpenReview","url":"https://openreview.net/group?id=robot-learning.org/CoRL/2025"},{"title":"CoRL 2026 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference"},{"title":"CoRL 2025 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2025%2FConference"},{"title":"CoRL 2025 Workshop H2R | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2025%2FWorkshop%2FH2R"},{"title":"CoRL 2025 Demos | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2025%2FDemos"},{"title":"CoRL | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL"}]

The search results provide general information about CoRL 2025 and 2026, but don't contain the specific review form scoring criteria dimensions. Let me search more specifically for the review form details.

Links: [{"title":"Reviewer Guidelines — CoRL 2023","url":"https://www.corl2023.org/reviewer-guidelines"},{"title":"CoRL 2024 - Instruction for Reviews","url":"https://2024.corl.org/contributions/instruction-for-reviews"},{"title":"Scoring Rubrics - help - Texas A&M University","url":"https://help.dsasites.tamu.edu/getinvolved/admin/forms/rubrics/"},{"title":"Rubrics for Assessment | Center for Innovative Teaching and Learning | Northern Illinois University","url":"https://www.niu.edu/citl/resources/guides/instructional-guide/r
…[truncated 7266 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_3",
  "tool": "WebSearch",
  "elapsed_ms": 19142
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-15T12:30:37.486117+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebFetch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_3",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebFetch",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-15T12:30:37.536760+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_3",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-15T12:30:41.569381+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://2024.corl.org/contributions/instruction-for-reviews",
  "prompt": "Extract the complete review form criteria, scoring dimensions, score scales (1-10 or 1-5), and any specific guidelines for reviewers. List all rating dimensions and their score ranges."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_3",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://2024.corl.org/contributions/instruction-for-reviews",
    "prompt": "Extract the complete review form criteria, scoring dimensions, score scales (1-10 or 1-5), and any specific guidelines for reviewers. List all rating dimensions and their score ranges."
  }
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-15T12:30:43.484320+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://www.corl.org/contributions/instruction-for-authors",
  "prompt": "Extract all formatting requirements: page limits, template specifications, anonymity rules, required sections (especially Limitations), font size, margins, column format, supplementary material rules, and any desk-reject criteria."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_3",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://www.corl.org/contributions/instruction-for-authors",
    "prompt": "Extract all formatting requirements: page limits, template specifications, anonymity rules, required sections (especially Limitations), font size, margins, column format, supplementary material rules, and any desk-reject criteria."
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-15T12:30:44.856433+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://www.corl.org/contributions/call-for-papers",
  "prompt": "Extract submission requirements, page limits, formatting rules, required sections, review criteria, and any desk-reject conditions for CoRL 2026."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_3",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://www.corl.org/contributions/call-for-papers",
    "prompt": "Extract submission requirements, page limits, formatting rules, required sections, review criteria, and any desk-reject conditions for CoRL 2026."
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-15T12:30:46.066851+00:00_

# CoRL 2024 Review Criteria Analysis

Based on the provided webpage, I cannot extract a complete review form with specific scoring dimensions or numerical scales. The document does not contain this information.

## What IS Available:

**Review Criteria for Regular Papers:**
The guidelines state submissions will be assessed on "significance and novelty of the results, either theoretical or empirical" and "the degree to which they have been objectively established" along with potential scientific impact and relevance to robotic learning.

**Desk Rejection Criteria:**
Three grounds for rejection are specified:
- Formatting issues (length or incorrect format)
- Anonymity violations in manuscript or materials
- Scope: Papers must demonstrate relevance through either explicitly addressing "a learning question for physical robots" OR testing solutions "on physical robots"

**Reviewer Qualifications:**
Reviewers should possess "expertise in robotics, robot learning, machine learning and complementary fields" with ideally "a minimum of 3 first author publications in major robotics conferences and journals" and machine learning venues.

## Missing Information:

The webpage does not provide:
- Specific scoring scales (1-10, 1-5, etc.)
- Detailed rating dimensions beyond general criteria
- Numerical evaluation guidelines
- Structured review form template

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_3",
  "tool": "WebFetch",
  "elapsed_ms": 4497
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-15T12:30:46.218147+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_3",
  "tool": "Glob",
  "tool_args": {
    "pattern": "sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-15T12:30:46.469736+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_3",
  "tool": "Glob",
  "elapsed_ms": 251
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-15T12:30:47.876030+00:00_

# CoRL 2026 Submission Requirements

Based on the provided content, here's what I found:

## Explicitly Stated Requirements

**Core Focus:**
- "Submissions should focus on a core robotics problem" and demonstrate relevance to robotics
- Papers without robotics focus will be rejected without review

**Required Section:**
- A Limitations section must be included, addressing "limiting assumptions, failure modes, and other limitations of the results and experiments"

**Encouraged Elements:**
- Real-robot experiments or convincing evidence that simulations transfer to real robots
- Supplementary materials including video, code, and data

## Missing Information

The page does **not** provide:
- Specific page limits
- Detailed formatting rules
- Complete list of required sections beyond Limitations
- Explicit review criteria
- Other desk-reject conditions

**Note:** The page directs authors to consult the "[Instruction for Authors](/contributions/instruction-for-authors)" page for "paper submission format and timeline." That detailed document would contain the comprehensive submission specifications you're seeking.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_3",
  "tool": "WebFetch",
  "elapsed_ms": 3019
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-15T12:30:54.842177+00:00_

# CoRL 2026 Formatting Requirements

## Page Limits
- **Initial submission**: 8 pages for main paper
- **Camera-ready**: 9 pages for main text (accommodating reviewer feedback)
- Acknowledgments, references, and appendix do not count toward page limits

## Template & Format
- Use the provided LaTeX template (available via Google Drive link)
- Camera-ready must include `\usepackage[final]{corl_2026}`
- Maintain specified text density, fonts, spacing, and margins from template
- Footer on first page: "10th Conference on Robot Learning (CoRL 2026), Austin, Texas, USA."

## Anonymity
- Initial submissions must be double-blind anonymized
- Camera-ready versions are de-anonymized with full author attribution

## Required Sections
- **Limitations section** (mandatory, counted in 8-page limit): must describe assumptions, failure modes, and limitations with future mitigation strategies

## Supplementary Materials
- Submit as single zip file through OpenReview
- Video: maximum 250 MB, suggested 3-minute limit
- Appendix may be included in main PDF or supplement
- Note: "PMLR does not allow videos as supplementary material" — host externally with links provided in paper

## Desk-Reject Criteria
- Papers with nonexistent references
- Dual submissions at other archival venues (without prior approval)
- Failure to meet reciprocal reviewing requirements
- Multiple substantially similar submissions

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_3",
  "tool": "WebFetch",
  "elapsed_ms": 11357
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-15T12:30:58.854838+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/docs/paper/sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_3",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/docs/paper/sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-15T12:30:59.208565+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/analysis.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/methodology.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_3",
  "tool": "Glob",
  "elapsed_ms": 353
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-15T12:30:59.464093+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/docs/paper/**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_3",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/docs/paper/**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-15T12:30:59.514776+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/analysis.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/methodology.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_3",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-15T12:31:03.019231+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_3",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-15T12:31:03.932718+00:00_

1	\begin{abstract}
2	Temporal abstraction via variable-rate imagination is a natural extension of world-model reinforcement learning, yet we find that every variable-rate configuration of DreamerV3 degrades performance---despite the success of identical $\Delta t$-conditioning in MPC-based methods. Through a factorial diagnostic on Walker Walk, we identify trained temporal embedding as the causal factor and characterize the resulting failure mode: \emph{conditioning-induced value overestimation} (CIVO). The trained embedding enables the RSSM reward head to develop a $2.78\times$ prediction gap between $\Delta t{=}1$ and $\Delta t{=}2$, which the critic internalizes as optimistic values. A normalized value-to-eval ratio threshold of $1.5\times$ achieves 4/4 separating power within the factorial grid (88.9\% accuracy across all configurations, with one false negative under $\Delta t{=}1$-only imagination). The same CIVO trigger produces stochastic downstream outcomes across seeds---full collapse, self-correction, and oscillatory degradation---from identical configurations. Critically, restricting imagination to $\Delta t{=}1$ does not prevent collapse: one of two seeds fails via a distinct non-CIVO pathway with increasing entropy, revealing that trained temporal conditioning creates vulnerability through multiple mechanisms. Our analysis identifies the feedback architecture---imagination-based actor-critic bootstrapping versus MPC re-planning---as the structural factor that transforms manageable model imprecision into pathological value dynamics.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_3",
  "tool": "Read",
  "elapsed_ms": 913
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-15T12:31:03.933254+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_3",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-15T12:31:04.387972+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	TAWM \citep{nhu2025tawm} shows that conditioning a world model on step size $\dt$ yields consistent gains within TD-MPC2's MPC framework \citep{hansen2024tdmpc2}. Can the same $\dt$-conditioning bring temporal abstraction to imagination-based actor-critic methods like DreamerV3 \citep{hafner2023dreamerv3}, where policies are trained entirely in imagined rollouts?
5	
6	We find that it cannot. Every variable-rate configuration we test degrades performance catastrophically: fixed $\dt{=}2$ collapses to $14\%$ of baseline, fixed $\dt{=}4$ never exceeds $19\%$ of baseline, and a learned Gumbel-Softmax gate collapses to $11\%$. Through a factorial analysis on Walker Walk \citep{tassa2018dmcontrol}, we isolate the \emph{trained} $\dt$-embedding as the causal factor. This embedding enables the RSSM reward head to develop a $2.78\times$ prediction gap between $\dt{=}1$ and $\dt{=}2$, which the critic internalizes as optimistic value estimates---a failure mode we term \emph{conditioning-induced value overestimation} (CIVO). A normalized value-to-eval threshold of $\nve > 1.5\times$ achieves 4/4 separating power within the factorial grid (88.9\% across all configurations), analogous to the delusional bias of \citet{lu2018nondelusional} but arising from model imprecision amplified by learned temporal conditioning.
7	
8	Three further findings complicate the picture: (1)~the same CIVO trigger produces stochastic downstream outcomes---full collapse, self-correction, and oscillatory degradation---across seeds of identical configurations; (2)~restricting imagination to $\dt{=}1$ while retaining the trained embedding does not prevent collapse, with one of two seeds failing via a qualitatively distinct non-CIVO pathway (evaluation-driven, increasing entropy); and (3)~the contrast with TAWM identifies the feedback architecture---imagination-based bootstrapping versus MPC re-planning---as the structural factor that transforms mana
…[truncated 61 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_3",
  "tool": "Read",
  "elapsed_ms": 454
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-15T12:31:04.439103+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_3",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-15T12:31:04.891510+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Temporal Abstraction.}
5	The options framework \citep{sutton1999options} and model-free action-repetition methods \citep{sharma2017figar, biedenkapp2021temporl, lakshminarayanan2017dynamic} achieve temporal abstraction by training values on real transitions, insulating them from model-induced bias. In world-model RL, the Dreamer family \citep{hafner2020dreamerv1, hafner2021dreamerv2, hafner2023dreamerv3} and transformer-based variants \citep{micheli2023iris, robine2023twm, hafner2025dreamerv4} train policies in imagination at fixed $\dt{=}1$. Several works introduce temporal abstraction via hierarchical representations \citep{gumbsch2024thick, mattes2024hieros}, goal-conditioned jumps \citep{li2025lsimagine}, or multi-scale state-space models \citep{shaj2023mts3}, but none conditions a flat dynamics model on $\dt$ for imagination-based policy training.
6	
7	\paragraph{TAWM and the MPC--Imagination Contrast.}
8	TAWM \citep{nhu2025tawm} conditions a world model on $\dt$ within TD-MPC2 \citep{hansen2024tdmpc2} and achieves consistent gains. The critical distinction is architectural: TAWM re-plans from real states at every step, so model errors do not accumulate into the critic. We show that identical $\dt$-conditioning fails in DreamerV3's imagination loop, where errors compound through bootstrapping---transforming manageable imprecision into pathological value overestimation.
9	
10	\paragraph{Value Overestimation.}
11	Value overestimation is well-studied in model-free \citep{fujimoto2018td3, vanhasselt2016double} and model-based settings \citep{janner2019mbpo, yu2020mopo}. \citet{lu2018nondelusional} identify delusional bias from policy-class constraints; our CIVO is mechanistically distinct, arising from model imprecision amplified by learned temporal conditioning. \citet{tallec2019making} show Q-function degradation with temporal resolution mismatches, underpinning our finding at $\dt > 1$. \citet{f
…[truncated 299 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_3",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-15T12:31:04.892061+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/methodology.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_3",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/methodology.tex"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-15T12:31:05.351262+00:00_

1	\section{Experimental Setup}
2	\label{sec:methodology}
3	
4	\subsection{Base Architecture}
5	\label{sec:base_arch}
6	
7	All experiments build on DreamerV3 \citep{hafner2023dreamerv3}, which learns a recurrent state-space model (RSSM) with discrete latent states ($32$ categories $\times$ $32$ classes), uses symlog-transformed predictions, and trains an actor-critic entirely within imagined trajectories. The standard configuration imagines $H{=}15$ steps at a fixed temporal resolution of $\dt{=}1$, meaning each imagination step corresponds to one environment transition.
8	
9	\subsection{Variable-Rate Imagination Mechanism}
10	\label{sec:variable_rate}
11	
12	We introduce three orthogonal architectural modifications that enable variable-rate imagination in DreamerV3. Each can be independently toggled to isolate its contribution.
13	
14	\paragraph{Temporal embedding.}
15	A learned embedding $e(\dt)$ is concatenated to the RSSM input at each imagination step, conditioning state predictions on the temporal scale. We test three modes:
16	\begin{itemize}[nosep,leftmargin=*]
17	\item \textbf{Trained}: embedding parameters are updated via backpropagation through the world model loss, allowing the RSSM to co-adapt its dynamics and reward predictions to the temporal scale.
18	\item \textbf{Untrained}: a fixed random projection of identical dimensionality. The RSSM receives a temporal signal but cannot co-adapt to it.
19	\item \textbf{Removed}: embedding dimension set to zero; no temporal conditioning signal is provided.
20	\end{itemize}
21	The trained-vs-untrained contrast is the key causal control: it isolates the effect of \emph{learning} the temporal conditioning from its mere architectural presence.
22	
23	\paragraph{Temporal subsampling.}
24	When enabled, the replay buffer augments training data with variable-$\dt$ transitions by subsampling consecutive frames. Concretely, with a maximum subsampling factor of~2, the RSSM trains on both $\dt{=}1$ and $\dt{=}2$ transitions
…[truncated 6703 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_3",
  "tool": "Read",
  "elapsed_ms": 459
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-15T12:31:05.354058+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_3",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex"
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-15T12:31:05.807184+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	We organize results around six findings (F1--F6) that establish a causal chain from trained temporal conditioning to pathological value dynamics and performance collapse. All experiments use Walker Walk (DMC) with DreamerV3; treatments run to 105K steps and the baseline to 505K steps. We report evaluation returns (mean over 10 episodes) and the normalized value-to-eval ratio ($\nve$), defined as the ratio of a configuration's imagined value to evaluation return, normalized by the baseline's ratio at the same training step.
5	
6	%% ============================================================
7	%% TABLE 1: Main results summary
8	%% ============================================================
9	
10	\begin{table*}[t]
11	\centering
12	\caption{All configurations and outcomes. Configurations with trained $\dt$-embedding and $\nve > 1.5\times$ are shaded.}
13	\label{tab:main_results}
14	\footnotesize
15	\setlength{\tabcolsep}{4pt}
16	\begin{tabular}{llcccccl}
17	\toprule
18	\textbf{Exp} & \textbf{Config} & \textbf{dt\_emb} & \textbf{Sub} & \textbf{H} & \textbf{Eval@final} & \textbf{NVE} & \textbf{Outcome} \\
19	\midrule
20	001 & Baseline ($\dt{=}1$) & --- & OFF & 15 & 915.7 @105K & 1.00$\times$ & Healthy \\
21	006 & Fixed $\dt{=}2$ & trained & OFF & 15 & 132.9 @65K & --- & Collapsed \\
22	007 & Fixed $\dt{=}4$ & trained & OFF & 15 & 152.5 @55K & --- & Collapsed \\
23	005 & Learned gate & trained & ON & 15 & 98.8 @145K & --- & Collapsed \\
24	\midrule
25	\rowcolor{gray!15}
26	008d & Factorial (s0) & trained & ON & 8 & 82.8 @55K & 4.12$\times$ & Full collapse \\
27	\rowcolor{gray!15}
28	009b & Factorial (s2) & trained & ON & 8 & 267.9 @105K & 0.38$\times$ & Self-correction \\
29	\rowcolor{gray!15}
30	009e & Factorial (s1) & trained & ON & 8 & 131.1 @105K & 1.57$\times$ & Oscillatory \\
31	008f & No dt\_emb (s0) & none & ON & 8 & 503.0 @105K & 0.30$\times$ & Healthy \\
32	009c & No dt\_emb (s2) & none & ON & 8 & 148.3 @105K & 1.1
…[truncated 15200 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_3",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-15T12:31:05.807752+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_3",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/analysis.tex"
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-15T12:31:06.362271+00:00_

1	\section{Analysis \& Discussion}
2	\label{sec:analysis}
3	
4	The preceding results establish that trained $\dt$-embedding is the causal factor behind pathological value dynamics in variable-rate DreamerV3. In this section, we synthesize these findings into a mechanistic account of conditioning-induced value overestimation (CIVO), explain why the same CIVO trigger produces divergent outcomes across seeds, contrast the imagination-based setting with MPC-based temporal conditioning, and discuss the fundamental tension inherent in the $\dt$-embedding design.
5	
6	\subsection{The CIVO Mechanism}
7	\label{sec:civo_mechanism}
8	
9	The RSSM fidelity analysis (Table~\ref{tab:rssm_fidelity}) reveals the mechanistic core of CIVO.  The trained $\dt$-embedding enables the reward head to learn temporally differentiated predictions, but these predictions are asymmetrically accurate: reward MAE at $\dt{=}1$ is $0.0568$, while at $\dt{=}2$ it rises to $0.1579$---a $2.78\times$ gap.  This gap is not an artifact of prediction difficulty alone; the no-embedding configuration (008f) exhibits a $1.01\times$ gap, and the baseline shows $1.56\times$.  The trained embedding actively amplifies the fidelity discrepancy by allowing the reward head to co-adapt with the temporal signal.
10	
11	This asymmetric fidelity initiates a feedback loop with four stages: (1) the trained $\dt$-embedding causes RSSM predictions at $\dt > 1$ to carry systematically biased reward estimates; (2) the critic, trained entirely on imagined trajectories, internalizes these biased rewards as optimistic value estimates; (3) the actor exploits the overestimated regions of the value landscape, shifting its policy toward states that appear high-value only under the biased model; and (4) this policy shift further skews the distribution of imagined states, reinforcing the bias.  The diagnostic signature is a sustained $\nve$ above $1.5\times$, followed by evaluation collapse.  In exp\_008d (seed 0), $\nve$ rises from $1
…[truncated 10750 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_3",
  "tool": "Read",
  "elapsed_ms": 554
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-15T12:31:06.362791+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_3",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-15T12:31:06.413434+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We have presented a systematic factorial diagnostic of temporal abstraction in DreamerV3, identifying trained $\dt$-embedding as the causal factor behind conditioning-induced value overestimation (CIVO). The key findings are:
5	
6	\begin{enumerate}[nosep,leftmargin=*]
7	\item Every variable-rate imagination configuration degrades relative to the $\dt{=}1$ baseline, with degradation scaling monotonically with $\dt$.
8	\item Trained $\dt$-embedding reliably triggers pathological value overestimation ($\nve > 1.5\times$, 4/4 separating power within the factorial grid, 88.9\% across all configurations), while untrained or removed embeddings prevent it.
9	\item The RSSM reward head develops a $2.78\times$ prediction gap between $\dt{=}1$ and $\dt{=}2$ under trained conditioning, providing the systematic bias that drives critic overestimation.
10	\item The same CIVO trigger produces stochastic downstream outcomes---full collapse, self-correction, and oscillatory degradation---across seeds of identical configurations.
11	\item Restricting imagination to $\dt{=}1$ does not fully prevent collapse: one of two seeds fails via a qualitatively distinct non-CIVO pathway (eval-driven with increasing entropy), demonstrating that the trained $\dt$-embedding creates vulnerability through multiple mechanisms.
12	\end{enumerate}
13	
14	The contrast with TAWM's success in MPC identifies the feedback architecture as the critical factor: $\dt$-conditioning succeeds when errors are contained by re-planning from real states, but fails when errors compound through imagination-based actor-critic bootstrapping.
15	
16	\paragraph{Limitations.}
17	Our experiments focus on a single environment (Walker Walk) and a single world-model architecture (DreamerV3/RSSM). While multi-seed replication establishes robustness within this setting, generalization to other environments and architectures---particularly transformer-based world models such as Dre
…[truncated 863 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_3",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-15T12:31:14.346429+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/docs/paper/references.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_3",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/docs/paper/references.bib",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon"
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-15T12:31:14.748971+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_3",
  "tool": "Glob",
  "elapsed_ms": 402
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-15T12:31:15.254312+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/artifacts/figures/paper/*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_3",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/artifacts/figures/paper/*.pdf",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon"
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-15T12:31:15.706869+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/figures/paper/fig1_learning_curves.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/figures/paper/fig4_mechanism_diagram.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/figures/paper/fig5_dt_amplification.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/figures/paper/fig6_multiple_pathways.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/figures/paper/fig3_factorial_grid.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/artifacts/figures/paper/fig2_nve_trajectory.pdf

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_3",
  "tool": "Glob",
  "elapsed_ms": 452
}
```

</details>

---

### Tool call

_source line 44 · 2026-05-15T12:31:17.013362+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://www.corl2023.org/reviewer-guidelines",
  "prompt": "Extract the complete review form criteria with all scoring dimensions, their descriptions, score ranges (1-10 scale), and any detailed rubrics. I need the exact review form fields and rating scales used by CoRL."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_3",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://www.corl2023.org/reviewer-guidelines",
    "prompt": "Extract the complete review form criteria with all scoring dimensions, their descriptions, score ranges (1-10 scale), and any detailed rubrics. I need the exact review form fields and rating scales used by CoRL."
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-15T12:31:21.569629+00:00_

# CoRL 2023 Review Form Criteria

Based on the provided guidelines, CoRL uses **six main evaluation dimensions** for paper reviews:

1. **Originality** - Assesses novelty of problems/methods and how the work distinguishes itself from prior contributions

2. **Quality** - Evaluates technical soundness, whether claims are substantiated, and completeness of the work

3. **Clarity** - Examines writing quality, organization, and whether information suffices for expert reproduction

4. **Significance** - Determines if results are important and advance the state of the art demonstrably

5. **Relevance** - Focuses on whether papers address robot learning problems and use learning-based methods evaluated in simulation or on real robots

6. **Limitations** - Reviewers must appreciate "honestly reported limitations kindly" while noting unacknowledged shortcomings

## Important Limitation

**The document does not specify a numerical scoring scale** (1-10 or otherwise). While the guidelines outline evaluation dimensions and expectations, the actual review form fields, specific rating scales, and detailed scoring rubrics are not detailed in this content. Reviewers receive technical instructions separately via OpenReview email.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_3",
  "tool": "WebFetch",
  "elapsed_ms": 4556
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-15T12:31:24.752101+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_3",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-15T12:31:25.611041+00:00_

1	% Auto-generated from literature_map.yaml
2	% 76 entries
3	
4	@article{sutton1999options,
5	  title = {Between MDPs and Semi-MDPs: A Framework for Temporal Abstraction in Reinforcement Learning},
6	  author = {Sutton, R.S and Precup, D and Singh, S},
7	  year = {1999},
8	  journal = {Artificial Intelligence 112},
9	}
10	
11	@inproceedings{hafner2020dreamerv1,
12	  title = {Dream to Control: Learning Behaviors by Latent Imagination},
13	  author = {Hafner, D and Lillicrap, T and Ba, J and Norouzi, M},
14	  year = {2020},
15	  booktitle = {International Conference on Learning Representations},
16	}
17	
18	@article{hafner2023dreamerv3,
19	  title = {Mastering Diverse Domains through World Models},
20	  author = {Hafner, Danijar and Pasukonis, Jurgis and Ba, Jimmy and Lillicrap, Timothy},
21	  year = {2025},
22	  journal = {Nature},
23	  eprint = {2301.04104},
24	  archivePrefix = {arXiv},
25	}
26	
27	@inproceedings{sharma2017figar,
28	  title = {Fine Grained Action Repetition for Deep Reinforcement Learning},
29	  author = {Sharma, S and Lakshminarayanan, A.S and Ravindran, B},
30	  year = {2017},
31	  booktitle = {International Conference on Learning Representations},
32	}
33	
34	@inproceedings{janner2019mbpo,
35	  title = {When to Trust Your Model: Model-Based Policy Optimization},
36	  author = {Janner, M and Fu, J and Zhang, M and Levine, S},
37	  year = {2019},
38	  booktitle = {Advances in Neural Information Processing Systems},
39	}
40	
41	@inproceedings{ke2019learning,
42	  title = {Learning Dynamics Model in Reinforcement Learning by Incorporating the Long Term Future},
43	  author = {Ke, N.R and Singh, A and Touati, A and Goyal, A and Bengio, Y and Parikh, D and Batra, D},
44	  year = {2019},
45	  booktitle = {International Conference on Learning Representations},
46	}
47	
48	@article{asadi2019combating,
49	  title = {Combating the Compounding-Error Problem with a Multi-step Model},
50	  author = {Asadi, K and Misra, D and Kim, S and Littman, M.L},
51	  yea
…[truncated 22609 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_3",
  "tool": "Read",
  "elapsed_ms": 858
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-15T12:31:25.661808+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper",
  "project": "event-gated-adaptive-horizon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_3",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper",
    "project": "event-gated-adaptive-horizon"
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-15T12:32:30.678108+00:00_

&lt;persisted-output>
Output too large (53.1KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon--claude-sessions-review-reviewer-3-2f53b6cb/2f33c2c1-985e-4ab4-be30-a6a71d2b724b/tool-results/toolu_01GmAaAK8ofyg3xMRjKurpKe.txt

Preview (first 2KB):
{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 77, \"total_citations\": 44, \"unique_cited_keys\": 29, \"orphan_bib\": 48, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 63, \"online_not_found\": 5, \"online_mismatch\": 9}, \"cross_check\": {\"orphan_bib\": [\"asadi2019combating\", \"barkley2024stealing\", \"beckerehmck2023multitimestep\", \"bjorck2022variance\", \"braylan2015frame\", \"bredis2026nedreamer\", \"chen2022transdreamer\", \"chua2018pets\", \"colas2018seeds\", \"farebrother2024stopregressing\", \"haarnoja2018sac\", \"hafner2022director\", \"henderson2018deep\", \"hussing2024dissecting\", \"jaderberg2017unreal\", \"ke2019learning\", \"kim2025deas\", \"kobayashi2025metacontroller\", \"kumar2022dr3\", \"lambert2020objective\", \"lambert2022investigating\", \"lee2021sunrise\", \"lenz2025macura\", \"liu2022dmve\", \"liu2025vanta\", \"luo2025vpl\", \"lyle2021auxiliary\", \"lyle2024normalization\", \"ma2024harmonydream\", \"nachum2018hiro\", \"nagabandi2018neural\", \"nie2025sdar\", \"nikishin2022primacy\", \"nikishin2023plasticity\", \"palenicek2025diminishing\", \"park2021sar\", \"qiao2023mind\", \"schwarzer2023bbf\", \"sokar2023dormant\", \"splates2025\", \"su2020conqur\", \"thrun1993issues\", \"venkatraman2015improving\", \"voelcker2025madtd\", \"wang2024seac\", \"zhang2025dymodreamer\", \"zhang2026hwm\", \"zhang2026instability\"], \"missing_bib\": [], \"orphan_count\": 48, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"sutton1999options\", \"type\": \"article\", \"title\": \"Between MDPs and Semi-MDPs: A Framework for Temporal Abstraction in Reinforcement Learning
…[truncated 369 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_3",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 65016
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-15T12:32:36.432980+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon--claude-sessions-review-reviewer-3-2f53b6cb/2f33c2c1-985e-4ab4-be30-a6a71d2b724b/tool-results/toolu_01GmAaAK8ofyg3xMRjKurpKe.txt",
  "offset": "0",
  "limit": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_3",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-9-projects-event-gated-adaptive-horizon--claude-sessions-review-reviewer-3-2f53b6cb/2f33c2c1-985e-4ab4-be30-a6a71d2b724b/tool-results/toolu_01GmAaAK8ofyg3xMRjKurpKe.txt",
    "offset": "0",
    "limit": "150"
  }
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-15T12:32:36.739453+00:00_

0	{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 77, \"total_citations\": 44, \"unique_cited_keys\": 29, \"orphan_bib\": 48, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 63, \"online_not_found\": 5, \"online_mismatch\": 9}, \"cross_check\": {\"orphan_bib\": [\"asadi2019combating\", \"barkley2024stealing\", \"beckerehmck2023multitimestep\", \"bjorck2022variance\", \"braylan2015frame\", \"bredis2026nedreamer\", \"chen2022transdreamer\", \"chua2018pets\", \"colas2018seeds\", \"farebrother2024stopregressing\", \"haarnoja2018sac\", \"hafner2022director\", \"henderson2018deep\", \"hussing2024dissecting\", \"jaderberg2017unreal\", \"ke2019learning\", \"kim2025deas\", \"kobayashi2025metacontroller\", \"kumar2022dr3\", \"lambert2020objective\", \"lambert2022investigating\", \"lee2021sunrise\", \"lenz2025macura\", \"liu2022dmve\", \"liu2025vanta\", \"luo2025vpl\", \"lyle2021auxiliary\", \"lyle2024normalization\", \"ma2024harmonydream\", \"nachum2018hiro\", \"nagabandi2018neural\", \"nie2025sdar\", \"nikishin2022primacy\", \"nikishin2023plasticity\", \"palenicek2025diminishing\", \"park2021sar\", \"qiao2023mind\", \"schwarzer2023bbf\", \"sokar2023dormant\", \"splates2025\", \"su2020conqur\", \"thrun1993issues\", \"venkatraman2015improving\", \"voelcker2025madtd\", \"wang2024seac\", \"zhang2025dymodreamer\", \"zhang2026hwm\", \"zhang2026instability\"], \"missing_bib\": [], \"orphan_count\": 48, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"sutton1999options\", \"type\": \"article\", \"title\": \"Between MDPs and Semi-MDPs: A Framework for Temporal Abstraction in Reinforcement Learning\", \"authors\": \"Sutton, R.S and Precup, D and Singh, S\", \"year\": \"1999\", \"venue\": \"Artificial Intelligence 112\"}, {\"key\": \"hafner2020dreamerv1\", \"type\": \"inproceedings\", \"title\": \"Dream to Control: Learning Behaviors by Latent Imagination\", \"authors\": \"Hafner, D and Lillicrap, T and Ba, J and Norouzi, M\", \"year\"
…[truncated 52410 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_3",
  "tool": "Read",
  "elapsed_ms": 306
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-15T12:35:07.075511+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 3 — Round 1 审稿报告\n\n**论文**: \"Why Temporal Abstraction Fails in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3\"\n**Venue**: CoRL 2026 Main Conference\n**审查侧重**: 格式合规 & 写作质量 & 呈现清晰度\n\n---\n\n## 总体评分\n\n**Overall**: 4/10（Borderline Reject）\n**一句话总结**: 写作质量出色、诊断方法论清晰，但**未使用 CoRL 官方 PMLR 模板**构成 desk reject 风险，且论文与物理机器人学习的关联薄弱，可能不符合 CoRL scope。\n\n---\n\n## 官方维度打分（基于 CoRL review form 维度）\n\n| 维度 | 评分 | 理由摘要 |\n|------|------|----------|\n| Originality | 3/5 | CIVO 作为诊断性发现有新意，但本质是 negative result + factorial ablation，概念增量有限 |\n| Quality | 3/5 | 实验设计严谨（factorial design），但单环境（Walker Walk）、少 seeds（2-3）限制结论可靠性 |\n| Clarity | 4/5 | 写作组织出色，F1-F6 因果链叙述清晰，术语定义到位 |\n| Significance | 2/5 | 诊断性发现有价值，但无解决方案；对 CoRL 社区的直接 actionable insight 有限 |\n| Relevance | 1/5 | **未涉及物理机器人**，仅在 DMC Walker Walk 上做 proprioceptive 实验；未讨论 robot learning 场景 |\n| Limitations | 3/5 | 存在 Limitations 段落，诚实列出了单环境和单架构的限制，但作为子段落而非独立 section |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] **未使用 CoRL 2026 官方 PMLR 模板——desk reject 风险**\n- 具体位置：`main.tex` 第 1-11 行\n- 问题：论文使用 `\\documentclass[10pt,letterpaper,twocolumn]{article}` + `\\usepackage[margin=0.75in]{geometry}`，**完全没有使用 CoRL 2026 官方模板**。CoRL 2026 Instruction for Authors 明确要求使用官方提供的 LaTeX template（camera-ready 需 `\\usepackage[final]{corl_2026}`），并要求保持模板规定的 \"text density, fonts, spacing, and margins\"。当前的自定义排版（0.75in margins、无 PMLR 页眉/脚注、无 conference footer）与官方格式差异巨大。\n- 为什么影响接收：CoRL 2024 desk rejection criteria 明确包括 \"formatting issues (length or incorrect format)\"。使用非官方模板**极大概率导致 desk reject**，不会进入审稿流程。\n- 建议修改方向：立即切换到 CoRL 2026 官方 PMLR 模板，确保首页 footer 包含 \"10th Conference on Robot Learning (CoRL 2026), Austin, Texas, USA.\"。\n\n**N2** [critical] **CoRL scope 适配性严重不足**\n- 具体位置：全文，尤其是 Section 4.5（Environment and Training Details）\n- 问题：CoRL CFP 明确要求 \"Submissions should focus on a core robotics problem\" 且 \"Papers without robotics focus will be rejected without review\"。CoRL 2024 desk rejection criteria 包括 scope（必须 \"address a learning question for physical robots\" 或 \"test solutions on physical robots\"）。本文仅在 DMC Walker Walk（一个纯仿真 locomotion task）上使用 proprioceptive observations 做实验，**全文未提及任何物理机器人场景、sim-to-real transfer、或 robot learning 的直接应用**。Analysis & Discussion（Section 6）也未讨论 findings 对 robot learning 的意义。\n- 为什么影响接收：即使论文技术质量过关，CoRL 的 relevance 要求是硬约束。当前论文更适合 ICML/NeurIPS/ICLR 等 general ML venue。\n- 建议修改方向：(1) 至少增加一个 robot-relevant 环境（如 DMC 的 manipulation task 或 robosuite）的验证实验；(2) 在 Introduction 和 Discussion 中明确阐述 CIVO 对 robot learning 的影响——例如 variable-rate world model 对于需要 multi-timescale control 的实际机器人任务（manipulation、locomotion、navigation）的重要性；(3) 讨论 findings 对 sim-to-real pipeline 中时间分辨率选择的启示。\n\n**N3** [critical] **页数合规性无法验证（因模板错误）**\n- 具体位置：全文\n- 问题：由于未使用 PMLR 模板，当前排版下的页数无法与 CoRL 的 8-page 限制进行对照。自定义的 0.75in 全向 margins 比 PMLR 模板通常更紧凑，意味着**换成 PMLR 模板后正文极有可能超过 8 页**。论文包含 5 个 figure（其中 3 个 columnwidth、2 个需要验证）、4 个 table（其中 1 个 table*）、大量详细文本（F1-F6 每个 finding 都有完整阐述），内容量很大。\n- 为什么影响接收：超页是另一个 desk reject 条件。\n- 建议修改方向：换模板后立即编译检查页数。如超页，优先压缩的候选：(a) Section 5（Results）中 F4 和 F5 可精简为1-2段；(b) Table 3（Post-CIVO outcomes）可合并入正文叙述或移至 appendix；(c) Analysis Section 6.2（Seed Divergence）的假设性讨论可大幅精简。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] **Limitations 作为段落嵌入 Conclusion，而非独立 Section**\n- 具体位置：`conclusion.tex` 第 16-17 行，`\\paragraph{Limitations.}`\n- 问题：CoRL 2026 Instruction for Authors 要求 \"must include a Limitations section\"，CoRL reviewer guidelines 要求 reviewer 评估 Limitations section 的质量。当前 Limitations 仅是 Conclusion 中的一个 `\\paragraph`，不是一个独立的 `\\section` 或 `\\subsection`。这在形式上可能不满足要求。\n- 建议：将 `\\paragraph{Limitations.}` 提升为 `\\subsection{Limitations}` 或单独的 `\\section{Limitations}`（放在 Conclusion 之前或之后）。\n\n**W2** [warning] **Abstract 过长且过于技术化**\n- 具体位置：`abstract.tex`\n- 问题：Abstract 约 180 词，包含大量具体数字（$2.78\\times$、$1.5\\times$、88.9%、4/4）和技术术语（CIVO、NVE、RSSM reward head、Gumbel-Softmax gate）。对于 CoRL 这样的 robotics + learning 交叉会议，abstract 需要对不熟悉 DreamerV3 内部机制的 reviewer（如来自 robotics 背景的 reviewer）也能快速理解。当前 abstract 读起来更像是一个 ICML workshop 的 extended abstract。\n- 建议：(1) 开头增加 1-2 句建立 motivation（为什么 temporal abstraction 对 robot learning 重要）；(2) 减少具体数字，保留关键发现的定性描述；(3) 结尾增加对 robot learning community 的 takeaway。\n\n**W3** [warning] **Bibliography 严重冗余：77 条 bib entry 中仅 29 条被引用**\n- 具体位置：`references.bib`\n- 问题：引用验证显示 77 条 bib entry 中有 48 条是 orphan（在 .bib 中存在但论文正文未引用）。此外，`splates2025` 条目的 author 字段为 \"SPlaTES, authors\"（明显是占位符/不完整条目），多个条目（`nie2025sdar`, `zhang2026instability`, `kobayashi2025metacontroller`, `liu2022dmve`, `kim2025deas`, `lenz2025macura`）使用 \"et, al\" 作为字面 author，说明 bib 文件是批量生成且未经清理。\n- 建议：清理 .bib，移除所有未引用条目；修复占位符 author 字段。虽然未引用的条目不会出现在 compiled PDF 的参考文献列表中，但提交时包含这样的 .bib 文件显得不够专业，且如果 reviewer 查看源文件可能留下负面印象。\n\n**W4** [warning] **参考文献格式可能不符合 PMLR 惯例**\n- 具体位置：`main.tex` 第 58 行 `\\bibliographystyle{plainnat}`\n- 问题：当前使用 `natbib` + `plainnat` 格式。PMLR/CoRL 模板通常自带或指定特定的 bibliography style。切换到官方模板后需确认是否需要使用模板指定的 bib style。\n- 建议：换模板后检查并使用官方模板附带的 bibliography style。\n\n**W5** [warning] **fig4_mechanism_diagram.pdf 存在但未被论文引用**\n- 具体位置：`artifacts/figures/paper/` 目录\n- 问题：论文引用了 fig1, fig2, fig3, fig5, fig6 五个图文件，fig4_mechanism_diagram.pdf 存在于目录中但未在任何 .tex 文件中引用。这意味着论文中图编号为 1-5（LaTeX 自动编号），但底层文件命名跳过了 fig4。如果这个 mechanism diagram 对理解 CIVO 机制有帮助，缺少它是一个呈现缺陷。\n- 建议：评估 fig4_mechanism_diagram.pdf 是否应纳入论文（一个 CIVO 机制流程图对理解 Section 6.1 非常有帮助）。如不纳入，重命名其余文件以保持一致性。\n\n---\n\n## 小问题（不影响接收）\n\n- `\\ie`, `\\eg`, `\\cf` 宏定义为 `\\textit{i.e.}` 等，但标准学术排版要求这些缩写后面有逗号（\"i.e.,\" 而非 \"i.e.\"），且是否使用斜体存在争议（多数 style guide 不建议斜体）。\n- `main.tex` 第 26 行定义了 `\\etal` 宏但未在正文中使用（正文用 `et al.` 的自然文本形式或在 bib 中处理）。\n- `hafner2023dreamerv3` 的 bib key 用 2023 但 year 字段是 2025（Nature 发表年）。引用验证确认 OpenAlex 记录年为 2023。建议统一。\n- 部分 bib entry 的 journal 字段不规范，如 `sutton1999options` 的 journal 为 \"Artificial Intelligence 112\"（卷号不应在 journal 字段中）。\n- Conclusion（Section 7）中 `\\paragraph{Future directions.}` 应考虑是否需要保留——如果页数紧张，可移至 appendix。\n\n---\n\n## 主要优势\n\n- **实验设计方法论出色**：factorial ablation 设计清晰，trained vs. untrained vs. removed embedding 的三重对照是确立因果关系的典范做法。\n- **叙事结构强**：F1-F6 的因果链式展开使论文从 \"what fails\" 到 \"why it fails\" 到 \"what doesn't fix it\" 有清晰的逻辑递进。\n- **诊断指标有价值**：NVE threshold（$1.5\\times$）和 RSSM fidelity gap 作为诊断工具有实用价值，且论文诚实报告了 88.9% 准确率（而非声称完美分离）。\n- **Multiple pathways 的发现**（F6）是真正有价值的 insight——表明问题比 \"fix the critic\" 更深层，为后续研究指明了方向。\n- **写作清晰度高**：Section 3（Methodology）的 factorial design table 和 Section 5（Results）的 per-seed trajectory 报告方式专业规范，遵循了 Agarwal et al. (2021) 的 best practice。\n\n---\n\n## 总结\n\n本文在写作质量和实验方法论上达到了高标准，factorial diagnostic 框架对 MBRL 社区有价值。然而，**三个 critical 问题严重阻碍其在 CoRL 2026 的接收前景**：\n\n1. **模板不合规**（desk reject 级别）——必须立即切换到 PMLR 官方模板\n2. **CoRL scope**——无物理机器人实验、无 robot learning 讨论，不符合 CoRL 的 relevance 要求\n3. **页数未知**——换模板后可能超页\n\n建议作者认真考虑目标 venue 的选择。如果坚持投 CoRL，需要增加 robot-relevant 实验并大幅强化 robotics motivation。如果 timeline 不允许这些改动，ICML/NeurIPS/ICLR 可能是更自然的选择。",
  "reviewer_id": "3",
  "project": "event-gated-adaptive-horizon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_3",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 3 — Round 1 审稿报告\n\n**论文**: \"Why Temporal Abstraction Fails in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3\"\n**Venue**: CoRL 2026 Main Conference\n**审查侧重**: 格式合规 & 写作质量 & 呈现清晰度\n\n---\n\n## 总体评分\n\n**Overall**: 4/10（Borderline Reject）\n**一句话总结**: 写作质量出色、诊断方法论清晰，但**未使用 CoRL 官方 PMLR 模板**构成 desk reject 风险，且论文与物理机器人学习的关联薄弱，可能不符合 CoRL scope。\n\n---\n\n## 官方维度打分（基于 CoRL review form 维度）\n\n| 维度 | 评分 | 理由摘要 |\n|------|------|----------|\n| Originality | 3/5 | CIVO 作为诊断性发现有新意，但本质是 negative result + factorial ablation，概念增量有限 |\n| Quality | 3/5 | 实验设计严谨（factorial design），但单环境（Walker Walk）、少 seeds（2-3）限制结论可靠性 |\n| Clarity | 4/5 | 写作组织出色，F1-F6 因果链叙述清晰，术语定义到位 |\n| Significance | 2/5 | 诊断性发现有价值，但无解决方案；对 CoRL 社区的直接 actionable insight 有限 |\n| Relevance | 1/5 | **未涉及物理机器人**，仅在 DMC Walker Walk 上做 proprioceptive 实验；未讨论 robot learning 场景 |\n| Limitations | 3/5 | 存在 Limitations 段落，诚实列出了单环境和单架构的限制，但作为子段落而非独立 section |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] **未使用 CoRL 2026 官方 PMLR 模板——desk reject 风险**\n- 具体位置：`main.tex` 第 1-11 行\n- 问题：论文使用 `\\documentclass[10pt,letterpaper,twocolumn]{article}` + `\\usepackage[margin=0.75in]{geometry}`，**完全没有使用 CoRL 2026 官方模板**。CoRL 2026 Instruction for Authors 明确要求使用官方提供的 LaTeX template（camera-ready 需 `\\usepackage[final]{corl_2026}`），并要求保持模板规定的 \"text density, fonts, spacing, and margins\"。当前的自定义排版（0.75in margins、无 PMLR 页眉/脚注、无 conference footer）与官方格式差异巨大。\n- 为什么影响接收：CoRL 2024 desk rejection criteria 明确包括 \"formatting issues (length or incorrect format)\"。使用非官方模板**极大概率导致 desk reject**，不会进入审稿流程。\n- 建议修改方向：立即切换到 CoRL 2026 官方 PMLR 模板，确保首页 footer 包含 \"10th Conference on Robot Learning (CoRL 2026), Austin, Texas, USA.\"。\n\n**N2** [critical] **CoRL scope 适配性严重不足**\n- 具体位置：全文，尤其是 Section 4.5（Environment and Training Details）\n- 问题：CoRL CFP 明确要求 \"Submissions should focus on a core robotics problem\" 且 \"Papers without robotics focus will be rejected without review\"。CoRL 2024 desk rejection criteria 包括 scope（必须 \"address a learning question for physical robots\" 或 \"test solutions on physical robots\"）。本文仅在 DMC Walker Walk（一个纯仿真 locomotion task）上使用 proprioceptive observations 做实验，**全文未提及任何物理机器人场景、sim-to-real transfer、或 robot learning 的直接应用**。Analysis & Discussion（Section 6）也未讨论 findings 对 robot learning 的意义。\n- 为什么影响接收：即使论文技术质量过关，CoRL 的 relevance 要求是硬约束。当前论文更适合 ICML/NeurIPS/ICLR 等 general ML venue。\n- 建议修改方向：(1) 至少增加一个 robot-relevant 环境（如 DMC 的 manipulation task 或 robosuite）的验证实验；(2) 在 Introduction 和 Discussion 中明确阐述 CIVO 对 robot learning 的影响——例如 variable-rate world model 对于需要 multi-timescale control 的实际机器人任务（manipulation、locomotion、navigation）的重要性；(3) 讨论 findings 对 sim-to-real pipeline 中时间分辨率选择的启示。\n\n**N3** [critical] **页数合规性无法验证（因模板错误）**\n- 具体位置：全文\n- 问题：由于未使用 PMLR 模板，当前排版下的页数无法与 CoRL 的 8-page 限制进行对照。自定义的 0.75in 全向 margins 比 PMLR 模板通常更紧凑，意味着**换成 PMLR 模板后正文极有可能超过 8 页**。论文包含 5 个 figure（其中 3 个 columnwidth、2 个需要验证）、4 个 table（其中 1 个 table*）、大量详细文本（F1-F6 每个 finding 都有完整阐述），内容量很大。\n- 为什么影响接收：超页是另一个 desk reject 条件。\n- 建议修改方向：换模板后立即编译检查页数。如超页，优先压缩的候选：(a) Section 5（Results）中 F4 和 F5 可精简为1-2段；(b) Table 3（Post-CIVO outcomes）可合并入正文叙述或移至 appendix；(c) Analysis Section 6.2（Seed Divergence）的假设性讨论可大幅精简。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] **Limitations 作为段落嵌入 Conclusion，而非独立 Section**\n- 具体位置：`conclusion.tex` 第 16-17 行，`\\paragraph{Limitations.}`\n- 问题：CoRL 2026 Instruction for Authors 要求 \"must include a Limitations section\"，CoRL reviewer guidelines 要求 reviewer 评估 Limitations section 的质量。当前 Limitations 仅是 Conclusion 中的一个 `\\paragraph`，不是一个独立的 `\\section` 或 `\\subsection`。这在形式上可能不满足要求。\n- 建议：将 `\\paragraph{Limitations.}` 提升为 `\\subsection{Limitations}` 或单独的 `\\section{Limitations}`（放在 Conclusion 之前或之后）。\n\n**W2** [warning] **Abstract 过长且过于技术化**\n- 具体位置：`abstract.tex`\n- 问题：Abstract 约 180 词，包含大量具体数字（$2.78\\times$、$1.5\\times$、88.9%、4/4）和技术术语（CIVO、NVE、RSSM reward head、Gumbel-Softmax gate）。对于 CoRL 这样的 robotics + learning 交叉会议，abstract 需要对不熟悉 DreamerV3 内部机制的 reviewer（如来自 robotics 背景的 reviewer）也能快速理解。当前 abstract 读起来更像是一个 ICML workshop 的 extended abstract。\n- 建议：(1) 开头增加 1-2 句建立 motivation（为什么 temporal abstraction 对 robot learning 重要）；(2) 减少具体数字，保留关键发现的定性描述；(3) 结尾增加对 robot learning community 的 takeaway。\n\n**W3** [warning] **Bibliography 严重冗余：77 条 bib entry 中仅 29 条被引用**\n- 具体位置：`references.bib`\n- 问题：引用验证显示 77 条 bib entry 中有 48 条是 orphan（在 .bib 中存在但论文正文未引用）。此外，`splates2025` 条目的 author 字段为 \"SPlaTES, authors\"（明显是占位符/不完整条目），多个条目（`nie2025sdar`, `zhang2026instability`, `kobayashi2025metacontroller`, `liu2022dmve`, `kim2025deas`, `lenz2025macura`）使用 \"et, al\" 作为字面 author，说明 bib 文件是批量生成且未经清理。\n- 建议：清理 .bib，移除所有未引用条目；修复占位符 author 字段。虽然未引用的条目不会出现在 compiled PDF 的参考文献列表中，但提交时包含这样的 .bib 文件显得不够专业，且如果 reviewer 查看源文件可能留下负面印象。\n\n**W4** [warning] **参考文献格式可能不符合 PMLR 惯例**\n- 具体位置：`main.tex` 第 58 行 `\\bibliographystyle{plainnat}`\n- 问题：当前使用 `natbib` + `plainnat` 格式。PMLR/CoRL 模板通常自带或指定特定的 bibliography style。切换到官方模板后需确认是否需要使用模板指定的 bib style。\n- 建议：换模板后检查并使用官方模板附带的 bibliography style。\n\n**W5** [warning] **fig4_mechanism_diagram.pdf 存在但未被论文引用**\n- 具体位置：`artifacts/figures/paper/` 目录\n- 问题：论文引用了 fig1, fig2, fig3, fig5, fig6 五个图文件，fig4_mechanism_diagram.pdf 存在于目录中但未在任何 .tex 文件中引用。这意味着论文中图编号为 1-5（LaTeX 自动编号），但底层文件命名跳过了 fig4。如果这个 mechanism diagram 对理解 CIVO 机制有帮助，缺少它是一个呈现缺陷。\n- 建议：评估 fig4_mechanism_diagram.pdf 是否应纳入论文（一个 CIVO 机制流程图对理解 Section 6.1 非常有帮助）。如不纳入，重命名其余文件以保持一致性。\n\n---\n\n## 小问题（不影响接收）\n\n- `\\ie`, `\\eg`, `\\cf` 宏定义为 `\\textit{i.e.}` 等，但标准学术排版要求这些缩写后面有逗号（\"i.e.,\" 而非 \"i.e.\"），且是否使用斜体存在争议（多数 style guide 不建议斜体）。\n- `main.tex` 第 26 行定义了 `\\etal` 宏但未在正文中使用（正文用 `et al.` 的自然文本形式或在 bib 中处理）。\n- `hafner2023dreamerv3` 的 bib key 用 2023 但 year 字段是 2025（Nature 发表年）。引用验证确认 OpenAlex 记录年为 2023。建议统一。\n- 部分 bib entry 的 journal 字段不规范，如 `sutton1999options` 的 journal 为 \"Artificial Intelligence 112\"（卷号不应在 journal 字段中）。\n- Conclusion（Section 7）中 `\\paragraph{Future directions.}` 应考虑是否需要保留——如果页数紧张，可移至 appendix。\n\n---\n\n## 主要优势\n\n- **实验设计方法论出色**：factorial ablation 设计清晰，trained vs. untrained vs. removed embedding 的三重对照是确立因果关系的典范做法。\n- **叙事结构强**：F1-F6 的因果链式展开使论文从 \"what fails\" 到 \"why it fails\" 到 \"what doesn't fix it\" 有清晰的逻辑递进。\n- **诊断指标有价值**：NVE threshold（$1.5\\times$）和 RSSM fidelity gap 作为诊断工具有实用价值，且论文诚实报告了 88.9% 准确率（而非声称完美分离）。\n- **Multiple pathways 的发现**（F6）是真正有价值的 insight——表明问题比 \"fix the critic\" 更深层，为后续研究指明了方向。\n- **写作清晰度高**：Section 3（Methodology）的 factorial design table 和 Section 5（Results）的 per-seed trajectory 报告方式专业规范，遵循了 Agarwal et al. (2021) 的 best practice。\n\n---\n\n## 总结\n\n本文在写作质量和实验方法论上达到了高标准，factorial diagnostic 框架对 MBRL 社区有价值。然而，**三个 critical 问题严重阻碍其在 CoRL 2026 的接收前景**：\n\n1. **模板不合规**（desk reject 级别）——必须立即切换到 PMLR 官方模板\n2. **CoRL scope**——无物理机器人实验、无 robot learning 讨论，不符合 CoRL 的 relevance 要求\n3. **页数未知**——换模板后可能超页\n\n建议作者认真考虑目标 venue 的选择。如果坚持投 CoRL，需要增加 robot-relevant 实验并大幅强化 robotics motivation。如果 timeline 不允许这些改动，ICML/NeurIPS/ICLR 可能是更自然的选择。",
    "reviewer_id": "3",
    "project": "event-gated-adaptive-horizon"
  }
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-15T12:35:12.118171+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_3",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 5042
}
```

</details>

---

### Assistant

_source line 54 · 2026-05-15T12:35:19.267934+00:00_

审稿报告已提交给 Review Director。

**核心结论**：论文写作质量和实验方法论均达到较高水准，但有 3 个 critical 问题：

1. **模板不合规**（desk reject 级别）：使用自定义 `\documentclass{article}` 而非 CoRL PMLR 官方模板
2. **CoRL scope 不符**：全文仅在 DMC Walker Walk 仿真环境做实验，未涉及物理机器人
3. **页数风险**：换到 PMLR 模板后正文大概率超过 8 页限制

评分 4/10（Borderline Reject）。建议作者认真考虑是否应转投 ICML/NeurIPS/ICLR 等 general ML venue。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_3"
}
```

</details>

---

## Round 2

10 recorded events

### User

_source line 55 · 2026-05-15T12:37:07.427379+00:00_

[Round 1 审稿请求]:
## 交叉分享 — 请逐条回应 Reviewer 1 和 Reviewer 2 的意见

以下是 Reviewer 1 和 Reviewer 2 的完整审稿意见。请对每条 Must-Fix 和 Should-Fix 逐条回应：
- **[AGREE]** 同意并说明理由
- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）
- 特别关注与你自己意见的共识和分歧点

---

## Reviewer 1 的审稿意见（侧重：方法严谨性 & 实验设计）

**Overall: 4/10 (Reject)**

### Must-Fix:
- **N1** [critical] 统计检验力严重不足。核心 "causal factor" 声明依赖 n=2 per group。"4/4 separating power" 在随机零假设下 P=1/16≈6.25%，离统计显著性甚远（需考虑多重比较修正）。Agarwal et al. (2021) 的核心论点是需要更多 seeds + IQM。
- **N2** [critical] NVE 阈值 1.5× 为 post-hoc 选择。"88.9% accuracy"是训练准确率，无独立验证。
- **N3** [critical] CoRL Relevance 严重不足。
- **N4** [critical] 单环境局限使因果声明不可泛化。

### Should-Fix:
- **W1** Factorial design 混淆变量：trained vs untrained 对比同时改变 subsampling 和 horizon。
- **W2** 105K vs 505K 训练步数不对等。
- **W3** Pathway B 解释不充分——可能只是普通 training instability。
- **W4** RSSM fidelity analysis：MAE 不区分 over- vs under-prediction，需 signed error。
- **W5** 格式不符合 CoRL 2026 要求。

---

## Reviewer 2 的审稿意见（侧重：新颖性 & 贡献度 & Venue Fit & Related Work）

**Overall: 4/10 (Reject)**

### Must-Fix:
- **N1** [critical] Venue Fit 严重不足——CoRL 要求 robot learning 相关性。Introduction 直接从 TAWM 的 RL 结果出发，完全没有 robotics motivation。
- **N2** [critical] 单环境实验无法支撑因果 claim 的泛化性。Dense reward + low-dim observation 的 Walker Walk 不具代表性。
- **N3** [critical] 贡献度不足——纯诊断负面结果缺乏 actionable solution。论文的 output 仅是 "dt-conditioning 在 DreamerV3 中不 work"。

### Should-Fix:
- **W1** 与 TAWM 的对比仅基于 architectural reasoning，未实际运行 TAWM 验证。
- **W2** NVE threshold 1.5× post-hoc fitting，无 cross-validation。
- **W3** CIVO 与已知 value overestimation 的区分不够清晰——可能只是 compounding model error 的实例化。
- **W4** Related Work 遗漏：Becker-Ehmck et al. (2023)、Park et al. (2021)、Wang & Beltrame (2024) 在 .bib 中未引用；DreamerV4 讨论不足。

---

请逐条给出你的 [AGREE] 或 [REBUT] 回应，特别关注与你自己审稿意见的共识和分歧。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_3",
  "source": "review_reviewer_3"
}
```

</details>

---

### Tool call

_source line 56 · 2026-05-15T12:37:46.778370+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/methodology.tex",
  "offset": "28",
  "limit": "35"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_3",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/methodology.tex",
    "offset": "28",
    "limit": "35"
  }
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-15T12:37:47.281281+00:00_

28	
29	\subsection{Factorial Design}
30	\label{sec:factorial}
31	
32	We adopt a structured factorial ablation across four factors: $\dt$-embedding mode (trained / untrained / none), temporal subsampling (on / off), imagination horizon ($H{=}15$ / $H{=}8$), and imagination step size ($\dt{=}1$, $2$, or $4$). Table~\ref{tab:factorial_design} summarizes the nine configurations.
33	
34	\begin{table}[t]
35	\centering
36	\caption{Factorial design. Each row specifies one experimental configuration. \textbf{Emb}: $\dt$-embedding mode. \textbf{Sub}: temporal subsampling. \textbf{H}: imagination horizon. \textbf{Imag $\dt$}: temporal resolution used during imagination.}
37	\label{tab:factorial_design}
38	\small
39	\setlength{\tabcolsep}{3.5pt}
40	\begin{tabular}{@{}llcccc@{}}
41	\toprule
42	\textbf{ID} & \textbf{Purpose} & \textbf{Emb} & \textbf{Sub} & \textbf{H} & \textbf{Imag $\dt$} \\
43	\midrule
44	001 & Reference baseline & --- & off & 15 & 1 \\
45	006 & Fixed $\dt{=}2$ & trn & off & 15 & 2 \\
46	007 & Fixed $\dt{=}4$ & trn & off & 15 & 4 \\
47	005 & Learned gate & trn & on & 15 & learned \\
48	\midrule
49	008d & Full treatment & trn & on & 8 & 2 \\
50	008f & Isolate emb & --- & on & 8 & 2 \\
51	008a & Isolate subsample & utr & off & 15 & 2 \\
52	008c & Isolate horizon & utr & off & 8 & 2 \\
53	\midrule
54	008e\_v3 & Mitigation ($\dt{=}1$ imag) & trn & on & 15 & 1 \\
55	\bottomrule
56	\end{tabular}
57	\vspace{-2pt}
58	{\raggedright\footnotesize trn = trained, utr = untrained (frozen random projection), --- = removed.\par}
59	\end{table}
60	
61	The design targets three diagnostic questions. First, comparing 008d (trained embedding) against 008f (no embedding) with all other factors held constant isolates whether \emph{training} the temporal conditioning triggers pathological dynamics. Second, comparing 008a and 008c (both untrained, differing only in $H$) against 008d (trained) separates embedding training from horizon and subsampling effects. Third, the mitigation config
…[truncated 197 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_3",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-15T12:37:47.739119+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex",
  "offset": "62",
  "limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_3",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/results.tex",
    "offset": "62",
    "limit": "20"
  }
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-15T12:37:48.192375+00:00_

62	%% ============================================================
63	
64	\subsection{F2: Trained Temporal Embedding Triggers Value Overestimation}
65	\label{sec:f2}
66	
67	The factorial design isolates trained $\dt$-embedding as the factor that reliably triggers pathological value overestimation. The key causal control compares exp\_008d (trained $\dt$-embedding, subsampling ON, $H{=}8$) against exp\_008f (identical configuration but \emph{no} trained $\dt$-embedding). As shown in Figure~\ref{fig:nve_trajectory}:
68	
69	\begin{itemize}[nosep,leftmargin=*]
70	\item \textbf{008d} (trained): $\nve = 1.78\times$ at 25K $\rightarrow$ $4.12\times$ at 55K $\rightarrow$ collapse (eval 167$\rightarrow$82.8).
71	\item \textbf{008f} (no dt\_emb): $\nve = 1.02\times$ at 25K $\rightarrow$ $0.30\times$ at 105K $\rightarrow$ no collapse (eval 503.0 at 105K).
72	\end{itemize}
73	
74	Using the $\nve > 1.5\times$ threshold as a diagnostic marker within the factorial grid (008d/009b vs.\ 008f/009c), trained configurations exceed this threshold in 2/2 seeds while untrained configurations remain below in 2/2 seeds, yielding 4/4 separating power. Across all nine tested configurations, the threshold achieves 8/9 accuracy (88.9\%) with 100\% specificity; the single false negative is 008e\_v3 seed 1 (trained embedding, max $\nve = 0.94\times$), which restricts imagination to $\dt{=}1$.
75	
76	\begin{figure}[t]
77	\centering
78	\includegraphics[width=\columnwidth]{figures/paper/fig2_nve_trajectory.pdf}
79	\caption{Normalized value-to-eval ratio ($\nve$) trajectories. The dashed line marks the $1.5\times$ threshold. All trained-embedding configurations with $\dt > 1$ imagination (red/orange) exceed this threshold; the mitigation configuration (008e\_v3 s1, dash-dot) with $\dt{=}1$-only imagination remains below it.}
80	\label{fig:nve_trajectory}
81	\end{figure}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_3",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---

### Tool call

_source line 60 · 2026-05-15T12:37:48.546410+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/analysis.tex",
  "offset": "36",
  "limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_3",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_9/projects/event-gated-adaptive-horizon/docs/paper/sections/analysis.tex",
    "offset": "36",
    "limit": "20"
  }
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-15T12:37:48.648197+00:00_

36	\subsection{Multiple Vulnerability Pathways}
37	\label{sec:pathways}
38	
39	The partial falsification of C6 (that restricting imagination to $\dt{=}1$ prevents collapse) reveals that the trained $\dt$-embedding creates vulnerability through at least two mechanistically distinct pathways.
40	
41	\textbf{Pathway A (CIVO, value-driven).}  Trained $\dt$-embedding $\rightarrow$ RSSM produces asymmetrically biased predictions at $\dt > 1$ $\rightarrow$ reward head systematic error $\rightarrow$ critic overestimation ($\nve > 1.5\times$) $\rightarrow$ actor exploits overestimated regions $\rightarrow$ performance collapse.  This pathway requires $\dt > 1$ imagination and produces a characteristic signature: value explosion preceding evaluation decline, with entropy \emph{decreasing} as the actor concentrates on overestimated regions.  Exp\_008d seed 0 is the canonical example.
42	
43	\textbf{Pathway B (non-CIVO, eval-driven).}  Trained $\dt$-embedding $\rightarrow$ policy instability $\rightarrow$ evaluation crashes ($-81\%$) while the value function remains initially stable $\rightarrow$ a late $\nve$ spike emerges as a consequence of the eval decline, not a cause.  This pathway does \emph{not} require $\dt > 1$ imagination: exp\_008e\_v3 seed 2 imagines exclusively at $\dt{=}1$.  The signature is distinct from Pathway A: entropy \emph{increases} ($-5.21 \rightarrow -3.83$), indicating the actor is becoming more stochastic rather than less; the value function remains well-calibrated until evaluation has already degraded substantially.  The baseline with the same seed (009a) is stable at 836.5, ruling out inherent seed fragility.
44	
45	The existence of two pathways broadens the diagnostic beyond CIVO alone.  The architectural coupling between the trained temporal embedding and the world model creates a more general vulnerability: the embedding's learned features affect not only reward prediction across temporal scales (Pathway A) but also the representation space in wh
…[truncated 2103 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_3",
  "tool": "Read",
  "elapsed_ms": 101
}
```

</details>

---

### Tool call

_source line 62 · 2026-05-15T12:39:30.107065+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 3 — 交叉回应 Reviewer 1 和 Reviewer 2 意见\n\n---\n\n# 回应 Reviewer 1（方法严谨性 & 实验设计）\n\n## Must-Fix\n\n**[AGREE] R1-N1: 统计检验力不足**\n同意这是核心方法论缺陷。论文的 \"4/4 separating power\" 声明（Section 5.2, F2）确实仅基于 n=2 per group（008d/009b vs 008f/009c）。在随机零假设下 P(4/4)=1/16≈6.25%，虽然接近传统 5% 显著性水平但未达到，且未做多重比较修正。论文引用 Agarwal et al. (2021) 作为方法论背书，但该文的核心主张恰恰是需要更多 seeds + IQM 聚合——论文实际做法（2-3 seeds，报告 per-seed trajectory）仅采纳了其部分建议。\n\n补充我的视角：作为格式/写作审查者，我注意到论文在语言上频繁使用因果性措辞（\"causal factor\", \"triggers\", \"necessary and sufficient\"），这些措辞与 n=2 的证据强度不匹配。即使因果方向大致正确，措辞应降级为 \"strongly suggests\" 或 \"consistent with\"。\n\n**[AGREE] R1-N2: NVE 阈值 1.5× post-hoc**\n同意。Section 4.4 定义 NVE 阈值时（methodology.tex 第 79-80 行）说 \"We use nve > 1.5× as a diagnostic threshold\"，但未说明该值是 a priori 选定还是 data-driven。从 \"achieves 4/4 separating power\" 和 \"88.9% accuracy\" 的表述看，这明显是在全部数据上拟合后报告的 in-sample 准确率。论文缺少任何形式的 cross-validation、sensitivity analysis（如 1.3× 或 1.7× 会怎样？）、或 held-out 验证。这严重削弱了 NVE 作为 \"diagnostic marker\" 的可信度。\n\n**[AGREE] R1-N3: CoRL Relevance 不足**\n与我自己的 N2（critical）完全一致。三位 reviewer 一致认为这是 critical issue，进一步确认了 venue fit 问题的严重性。\n\n**[AGREE] R1-N4: 单环境局限**\n同意。Walker Walk 是 DMC 中相对简单的连续控制任务（dense reward、low-dim proprioceptive observation、smooth dynamics）。CIVO 是否在 sparse reward、high-dim observation、contact-rich dynamics 环境中同样出现完全未知。论文 Limitations 段（conclusion.tex 第 16-17 行）虽然承认了这一点，但 \"causal factor\" 级别的声明需要至少 2-3 个环境才能让 reviewer 信服。\n\n## Should-Fix\n\n**[REBUT] R1-W1: Factorial design 混淆变量**\n部分不同意。R1 的担忧对部分比较成立，但**论文的核心因果对照（008d vs 008f）是干净的**。\n\n查看 Table 1（methodology.tex 第 34-59 行）：\n- 008d: trained emb, Sub=ON, H=8, dt=2\n- 008f: **none** emb, Sub=ON, H=8, dt=2\n\n两者**仅在 embedding 上不同**，其余三个因素完全一致。论文在 Section 3.3 明确说明：\"comparing 008d (trained embedding) against 008f (no embedding) with all other factors held constant isolates whether training the temporal conditioning triggers pathological dynamics.\"\n\nR1 的混淆变量担忧适用于 008a（utr, OFF, 15）和 008c（utr, OFF, 8）与 008d 的比较——这些比较确实同时改变了 embedding、subsampling 和 horizon。但论文并未将这些作为主要因果证据，而是作为辅助对照（Section 5.5, F5：\"horizon length and temporal subsampling affect learning speed [but] neither is sufficient to trigger collapse\"）。\n\n建议论文更明确地区分 primary causal comparison（008d vs 008f，干净）和 secondary comparisons（有混淆但用于排除辅助因素），以避免 R1 的误读。\n\n**[AGREE] R1-W2: 105K vs 505K 不对等**\n同意这存在解释性局限。虽然 105K 足以观察 collapse onset，但对于 self-correction 的 seed（如 009b 在 105K 时 eval=267.9、nve=0.38×），我们无法知道它是否最终能恢复到 baseline 水平。Section 5.2 将 seed 2 标记为 \"self-correction\"，但 267.9 vs baseline 的 915.7 仍然只有 29%——这可能只是 \"slower collapse\" 而非真正的 self-correction。延长 treatment runs 至少到 200-300K 步才能区分这两种可能性。\n\n**[AGREE] R1-W3: Pathway B 解释不充分**\n同意。Pathway B（008e_v3 seed 2）的证据仅来自**单个 seed**（analysis.tex 第 42-43 行）。论文用 baseline seed 2（009a）的稳定性排除 \"inherent seed fragility\"，但这不足以排除所有混淆因素。Pathway B 的特征（entropy increase, eval-driven collapse）与普通 training instability（如 plasticity loss、capacity collapse 等已知现象）的区分不够清晰。论文需要更强的证据或更谨慎的措辞来支撑 \"qualitatively distinct pathway\" 的声明。\n\n**[AGREE] R1-W4: RSSM fidelity 需 signed error**\n同意这是技术审查的合理要求。Table 4（results.tex 第 196-212 行）报告 reward MAE，但 CIVO 机制依赖于 **systematic overprediction**（而非双向误差）。MAE=0.1579 at dt=2 可能是均匀分布的 over/under prediction，也可能是单向 overprediction——两者对 CIVO 机制的支持力度完全不同。补充 signed error（mean error 而非 MAE）是验证 CIVO 因果链条的关键一步。\n\n**[AGREE] R1-W5: 格式不符合 CoRL 2026**\n与我自己的 N1（critical）完全一致。\n\n---\n\n# 回应 Reviewer 2（新颖性 & 贡献度 & Venue Fit）\n\n## Must-Fix\n\n**[AGREE] R2-N1: Venue Fit 不足**\n与我的 N2 和 R1-N3 一致。三位 reviewer 形成共识：论文的 Introduction（introduction.tex）直接从 \"TAWM shows that conditioning a world model on step size dt yields consistent gains within TD-MPC2's MPC framework\" 出发，完全没有 robotics motivation 或 robot learning 的 framing。这对 CoRL 来说是根本性问题。\n\n**[AGREE] R2-N2: 单环境 + dense reward 不具代表性**\n同意，且 R2 补充的 \"dense reward + low-dim observation\" 视角比 R1-N4 更精确。Dense reward 环境中 critic 获得频繁的真实信号，value overestimation 的影响可能与 sparse reward 环境截然不同。在 sparse reward 下，critic 更依赖 imagination 中的 bootstrapped values，CIVO 可能更严重——但也可能不会出现（因为 reward head 本身就难以学好）。这两种可能性都未被讨论。\n\n**[REBUT] R2-N3: 贡献度不足——纯诊断负面结果缺乏 actionable solution**\n部分不同意。R2 将论文定性为 \"output 仅是 dt-conditioning 在 DreamerV3 中不 work\"，我认为这低估了论文的实际贡献。\n\n论文的核心输出不仅是负面结果，还包括：\n1. **NVE 诊断框架**（Section 4.4）：提供了可复用的 value overestimation 检测指标，虽然阈值需要 cross-validation\n2. **CIVO 机制分析**（Section 6.1）：不只是说 \"不 work\"，而是通过 RSSM fidelity analysis（Table 4）定位到 reward head co-adaptation 这一具体机制\n3. **MPC vs imagination 架构对比**（Section 6.3）：识别出 feedback architecture 作为结构性因素，这对后续研究设计有直接指导意义\n4. **Multiple pathways 发现**（Section 6.5）：表明问题比 \"fix the critic\" 更深层\n\n这些发现对 MBRL 社区有 diagnostic value，类似于 Henderson et al. (2018) \"Deep RL that Matters\" 和 Engstrom et al. (2020) \"Implementation Matters\" 的贡献模式。\n\n**但我同意**，对于 CoRL 这个特定 venue，纯诊断论文确实贡献度偏低——CoRL 更偏好有实际解决方案或系统实现的工作。如果投 ICML/NeurIPS，贡献度的评价可能不同。\n\n## Should-Fix\n\n**[AGREE] R2-W1: 未实际运行 TAWM 验证**\n同意。Section 6.3（analysis.tex 第 24-28 行）对 MPC 免疫性的解释完全基于 architectural reasoning（\"re-plans from real states at every step, so model errors do not accumulate into the critic\"）。这是合理的假说，但未经验证。一个可能的反驳是 TAWM 使用了不同的 world model architecture（不是 RSSM），所以直接复现不等价。但至少应该 (a) 在 TD-MPC2 框架下复现 dt-conditioning 的增益以确认 baseline，或 (b) 引用 TAWM 的具体数据来支撑论点。\n\n**[AGREE] R2-W2: NVE threshold post-hoc**\n与 R1-N2 一致。两位 reviewer 独立指出同一问题，进一步确认了这是论文的关键方法论弱点。\n\n**[REBUT] R2-W3: CIVO 可能只是 compounding model error 的实例化**\n部分不同意。R2 的观点是 CIVO 可能只是已知 compounding model error 的一个具体 case。这在高层面上成立，但论文通过 trained vs untrained embedding 的对照（Section 5.2-5.3）提供了超越 generic compounding error 的特异性证据：\n\n- 如果 CIVO 仅是 compounding error 的实例化，那么 untrained embedding + dt=2 imagination（008a, 008c）也应该出现类似 value overestimation——因为 dt=2 本身就会增加 compounding error。但实际上 008a（nve=0.59×）和 008c（nve=0.58×）均未出现 overestimation。\n- 关键区别在于 **learned co-adaptation**：trained embedding 使 reward head 对不同 dt 产生 asymmetric prediction quality（Table 4, 2.78× reward gap），这不是 generic compounding error 会产生的模式。\n\n然而，我同意论文应该更系统地区分 CIVO 和 generic compounding model error——例如通过控制实验：在 untrained embedding 下也测量 RSSM fidelity gap，以展示 trained embedding 特有的 asymmetric co-adaptation。实际上 Table 4 已经包含了 008f（no emb）的数据（reward gap 1.01×），但论文没有将此显式框架为 \"CIVO vs generic compounding error\" 的对照论证。\n\n**[AGREE] R2-W4: Related Work 遗漏**\n同意。我在引用验证中也发现：`beckerehmck2023multitimestep`、`park2021sar`、`wang2024seac` 均存在于 .bib 但未在正文中引用。这三篇分别涉及 multi-timestep models、time discretization-invariant action repetition、elastic time steps——都与本文主题高度相关。\n\n关于 DreamerV4：R2 说 \"讨论不足\"，但我查证 analysis.tex 第 52 行确实有一段讨论（\"DreamerV4 replaces the RSSM with a transformer architecture, raising the question of whether CIVO transfers...\"），篇幅约 4 行。这段讨论的深度对于一篇非 DreamerV4 的论文来说是合理的，但可以增加对 transformer 架构下 CIVO 是否会出现的更具体分析。\n\n---\n\n# 三位 Reviewer 的共识总结\n\n| 问题 | R1 | R2 | R3 (我) | 共识 |\n|------|----|----|---------|------|\n| 模板不合规 | W5 | — | N1 (critical) | 2/3 提到，desk reject 级 |\n| CoRL scope/relevance | N3 | N1 | N2 (critical) | **3/3 一致**，最强共识 |\n| 单环境局限 | N4 | N2 | 未单独列出但认同 | **3/3 一致** |\n| 统计检验力不足 | N1 | — | 交叉回应中同意 | 2/3 |\n| NVE 阈值 post-hoc | N2 | W2 | 交叉回应中同意 | **3/3 一致** |\n| 贡献度/解决方案缺失 | — | N3 | 部分同意 | 2/3 |\n\n**最终判断**：三位 reviewer 在 CoRL scope、单环境局限、NVE post-hoc 三个问题上形成完全共识。这些问题叠加在一起，使得论文在 CoRL 2026 的接收前景非常不乐观。建议作者认真考虑 (1) 增加 robot-relevant 环境、(2) 增加 seeds、(3) 对 NVE 做 cross-validation，然后转投 ICML/NeurIPS。",
  "reviewer_id": "3",
  "project": "event-gated-adaptive-horizon"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_3",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 3 — 交叉回应 Reviewer 1 和 Reviewer 2 意见\n\n---\n\n# 回应 Reviewer 1（方法严谨性 & 实验设计）\n\n## Must-Fix\n\n**[AGREE] R1-N1: 统计检验力不足**\n同意这是核心方法论缺陷。论文的 \"4/4 separating power\" 声明（Section 5.2, F2）确实仅基于 n=2 per group（008d/009b vs 008f/009c）。在随机零假设下 P(4/4)=1/16≈6.25%，虽然接近传统 5% 显著性水平但未达到，且未做多重比较修正。论文引用 Agarwal et al. (2021) 作为方法论背书，但该文的核心主张恰恰是需要更多 seeds + IQM 聚合——论文实际做法（2-3 seeds，报告 per-seed trajectory）仅采纳了其部分建议。\n\n补充我的视角：作为格式/写作审查者，我注意到论文在语言上频繁使用因果性措辞（\"causal factor\", \"triggers\", \"necessary and sufficient\"），这些措辞与 n=2 的证据强度不匹配。即使因果方向大致正确，措辞应降级为 \"strongly suggests\" 或 \"consistent with\"。\n\n**[AGREE] R1-N2: NVE 阈值 1.5× post-hoc**\n同意。Section 4.4 定义 NVE 阈值时（methodology.tex 第 79-80 行）说 \"We use nve > 1.5× as a diagnostic threshold\"，但未说明该值是 a priori 选定还是 data-driven。从 \"achieves 4/4 separating power\" 和 \"88.9% accuracy\" 的表述看，这明显是在全部数据上拟合后报告的 in-sample 准确率。论文缺少任何形式的 cross-validation、sensitivity analysis（如 1.3× 或 1.7× 会怎样？）、或 held-out 验证。这严重削弱了 NVE 作为 \"diagnostic marker\" 的可信度。\n\n**[AGREE] R1-N3: CoRL Relevance 不足**\n与我自己的 N2（critical）完全一致。三位 reviewer 一致认为这是 critical issue，进一步确认了 venue fit 问题的严重性。\n\n**[AGREE] R1-N4: 单环境局限**\n同意。Walker Walk 是 DMC 中相对简单的连续控制任务（dense reward、low-dim proprioceptive observation、smooth dynamics）。CIVO 是否在 sparse reward、high-dim observation、contact-rich dynamics 环境中同样出现完全未知。论文 Limitations 段（conclusion.tex 第 16-17 行）虽然承认了这一点，但 \"causal factor\" 级别的声明需要至少 2-3 个环境才能让 reviewer 信服。\n\n## Should-Fix\n\n**[REBUT] R1-W1: Factorial design 混淆变量**\n部分不同意。R1 的担忧对部分比较成立，但**论文的核心因果对照（008d vs 008f）是干净的**。\n\n查看 Table 1（methodology.tex 第 34-59 行）：\n- 008d: trained emb, Sub=ON, H=8, dt=2\n- 008f: **none** emb, Sub=ON, H=8, dt=2\n\n两者**仅在 embedding 上不同**，其余三个因素完全一致。论文在 Section 3.3 明确说明：\"comparing 008d (trained embedding) against 008f (no embedding) with all other factors held constant isolates whether training the temporal conditioning triggers pathological dynamics.\"\n\nR1 的混淆变量担忧适用于 008a（utr, OFF, 15）和 008c（utr, OFF, 8）与 008d 的比较——这些比较确实同时改变了 embedding、subsampling 和 horizon。但论文并未将这些作为主要因果证据，而是作为辅助对照（Section 5.5, F5：\"horizon length and temporal subsampling affect learning speed [but] neither is sufficient to trigger collapse\"）。\n\n建议论文更明确地区分 primary causal comparison（008d vs 008f，干净）和 secondary comparisons（有混淆但用于排除辅助因素），以避免 R1 的误读。\n\n**[AGREE] R1-W2: 105K vs 505K 不对等**\n同意这存在解释性局限。虽然 105K 足以观察 collapse onset，但对于 self-correction 的 seed（如 009b 在 105K 时 eval=267.9、nve=0.38×），我们无法知道它是否最终能恢复到 baseline 水平。Section 5.2 将 seed 2 标记为 \"self-correction\"，但 267.9 vs baseline 的 915.7 仍然只有 29%——这可能只是 \"slower collapse\" 而非真正的 self-correction。延长 treatment runs 至少到 200-300K 步才能区分这两种可能性。\n\n**[AGREE] R1-W3: Pathway B 解释不充分**\n同意。Pathway B（008e_v3 seed 2）的证据仅来自**单个 seed**（analysis.tex 第 42-43 行）。论文用 baseline seed 2（009a）的稳定性排除 \"inherent seed fragility\"，但这不足以排除所有混淆因素。Pathway B 的特征（entropy increase, eval-driven collapse）与普通 training instability（如 plasticity loss、capacity collapse 等已知现象）的区分不够清晰。论文需要更强的证据或更谨慎的措辞来支撑 \"qualitatively distinct pathway\" 的声明。\n\n**[AGREE] R1-W4: RSSM fidelity 需 signed error**\n同意这是技术审查的合理要求。Table 4（results.tex 第 196-212 行）报告 reward MAE，但 CIVO 机制依赖于 **systematic overprediction**（而非双向误差）。MAE=0.1579 at dt=2 可能是均匀分布的 over/under prediction，也可能是单向 overprediction——两者对 CIVO 机制的支持力度完全不同。补充 signed error（mean error 而非 MAE）是验证 CIVO 因果链条的关键一步。\n\n**[AGREE] R1-W5: 格式不符合 CoRL 2026**\n与我自己的 N1（critical）完全一致。\n\n---\n\n# 回应 Reviewer 2（新颖性 & 贡献度 & Venue Fit）\n\n## Must-Fix\n\n**[AGREE] R2-N1: Venue Fit 不足**\n与我的 N2 和 R1-N3 一致。三位 reviewer 形成共识：论文的 Introduction（introduction.tex）直接从 \"TAWM shows that conditioning a world model on step size dt yields consistent gains within TD-MPC2's MPC framework\" 出发，完全没有 robotics motivation 或 robot learning 的 framing。这对 CoRL 来说是根本性问题。\n\n**[AGREE] R2-N2: 单环境 + dense reward 不具代表性**\n同意，且 R2 补充的 \"dense reward + low-dim observation\" 视角比 R1-N4 更精确。Dense reward 环境中 critic 获得频繁的真实信号，value overestimation 的影响可能与 sparse reward 环境截然不同。在 sparse reward 下，critic 更依赖 imagination 中的 bootstrapped values，CIVO 可能更严重——但也可能不会出现（因为 reward head 本身就难以学好）。这两种可能性都未被讨论。\n\n**[REBUT] R2-N3: 贡献度不足——纯诊断负面结果缺乏 actionable solution**\n部分不同意。R2 将论文定性为 \"output 仅是 dt-conditioning 在 DreamerV3 中不 work\"，我认为这低估了论文的实际贡献。\n\n论文的核心输出不仅是负面结果，还包括：\n1. **NVE 诊断框架**（Section 4.4）：提供了可复用的 value overestimation 检测指标，虽然阈值需要 cross-validation\n2. **CIVO 机制分析**（Section 6.1）：不只是说 \"不 work\"，而是通过 RSSM fidelity analysis（Table 4）定位到 reward head co-adaptation 这一具体机制\n3. **MPC vs imagination 架构对比**（Section 6.3）：识别出 feedback architecture 作为结构性因素，这对后续研究设计有直接指导意义\n4. **Multiple pathways 发现**（Section 6.5）：表明问题比 \"fix the critic\" 更深层\n\n这些发现对 MBRL 社区有 diagnostic value，类似于 Henderson et al. (2018) \"Deep RL that Matters\" 和 Engstrom et al. (2020) \"Implementation Matters\" 的贡献模式。\n\n**但我同意**，对于 CoRL 这个特定 venue，纯诊断论文确实贡献度偏低——CoRL 更偏好有实际解决方案或系统实现的工作。如果投 ICML/NeurIPS，贡献度的评价可能不同。\n\n## Should-Fix\n\n**[AGREE] R2-W1: 未实际运行 TAWM 验证**\n同意。Section 6.3（analysis.tex 第 24-28 行）对 MPC 免疫性的解释完全基于 architectural reasoning（\"re-plans from real states at every step, so model errors do not accumulate into the critic\"）。这是合理的假说，但未经验证。一个可能的反驳是 TAWM 使用了不同的 world model architecture（不是 RSSM），所以直接复现不等价。但至少应该 (a) 在 TD-MPC2 框架下复现 dt-conditioning 的增益以确认 baseline，或 (b) 引用 TAWM 的具体数据来支撑论点。\n\n**[AGREE] R2-W2: NVE threshold post-hoc**\n与 R1-N2 一致。两位 reviewer 独立指出同一问题，进一步确认了这是论文的关键方法论弱点。\n\n**[REBUT] R2-W3: CIVO 可能只是 compounding model error 的实例化**\n部分不同意。R2 的观点是 CIVO 可能只是已知 compounding model error 的一个具体 case。这在高层面上成立，但论文通过 trained vs untrained embedding 的对照（Section 5.2-5.3）提供了超越 generic compounding error 的特异性证据：\n\n- 如果 CIVO 仅是 compounding error 的实例化，那么 untrained embedding + dt=2 imagination（008a, 008c）也应该出现类似 value overestimation——因为 dt=2 本身就会增加 compounding error。但实际上 008a（nve=0.59×）和 008c（nve=0.58×）均未出现 overestimation。\n- 关键区别在于 **learned co-adaptation**：trained embedding 使 reward head 对不同 dt 产生 asymmetric prediction quality（Table 4, 2.78× reward gap），这不是 generic compounding error 会产生的模式。\n\n然而，我同意论文应该更系统地区分 CIVO 和 generic compounding model error——例如通过控制实验：在 untrained embedding 下也测量 RSSM fidelity gap，以展示 trained embedding 特有的 asymmetric co-adaptation。实际上 Table 4 已经包含了 008f（no emb）的数据（reward gap 1.01×），但论文没有将此显式框架为 \"CIVO vs generic compounding error\" 的对照论证。\n\n**[AGREE] R2-W4: Related Work 遗漏**\n同意。我在引用验证中也发现：`beckerehmck2023multitimestep`、`park2021sar`、`wang2024seac` 均存在于 .bib 但未在正文中引用。这三篇分别涉及 multi-timestep models、time discretization-invariant action repetition、elastic time steps——都与本文主题高度相关。\n\n关于 DreamerV4：R2 说 \"讨论不足\"，但我查证 analysis.tex 第 52 行确实有一段讨论（\"DreamerV4 replaces the RSSM with a transformer architecture, raising the question of whether CIVO transfers...\"），篇幅约 4 行。这段讨论的深度对于一篇非 DreamerV4 的论文来说是合理的，但可以增加对 transformer 架构下 CIVO 是否会出现的更具体分析。\n\n---\n\n# 三位 Reviewer 的共识总结\n\n| 问题 | R1 | R2 | R3 (我) | 共识 |\n|------|----|----|---------|------|\n| 模板不合规 | W5 | — | N1 (critical) | 2/3 提到，desk reject 级 |\n| CoRL scope/relevance | N3 | N1 | N2 (critical) | **3/3 一致**，最强共识 |\n| 单环境局限 | N4 | N2 | 未单独列出但认同 | **3/3 一致** |\n| 统计检验力不足 | N1 | — | 交叉回应中同意 | 2/3 |\n| NVE 阈值 post-hoc | N2 | W2 | 交叉回应中同意 | **3/3 一致** |\n| 贡献度/解决方案缺失 | — | N3 | 部分同意 | 2/3 |\n\n**最终判断**：三位 reviewer 在 CoRL scope、单环境局限、NVE post-hoc 三个问题上形成完全共识。这些问题叠加在一起，使得论文在 CoRL 2026 的接收前景非常不乐观。建议作者认真考虑 (1) 增加 robot-relevant 环境、(2) 增加 seeds、(3) 对 NVE 做 cross-validation，然后转投 ICML/NeurIPS。",
    "reviewer_id": "3",
    "project": "event-gated-adaptive-horizon"
  }
}
```

</details>

---

### Tool result

_source line 63 · 2026-05-15T12:39:34.948466+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_3",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4841
}
```

</details>

---

### Assistant

_source line 64 · 2026-05-15T12:39:41.900880+00:00_

交叉回应已提交。核心判断：

- R1 的 5 条 Must-Fix 全部同意，W1（factorial confound）部分反驳——论文的核心对照 008d vs 008f 实际上是干净的，但 secondary comparisons 确实有混淆
- R2 的 N1/N2 同意，**N3（贡献度不足）部分反驳**——论文的诊断框架（NVE、RSSM fidelity、multiple pathways）超越了简单的 negative result，但对 CoRL 确实偏弱
- R2-W3（CIVO vs generic compounding error）部分反驳——trained vs untrained 对照提供了特异性证据，Table 4 的 reward gap 1.01× vs 2.78× 是关键区分
- **三位 reviewer 在 CoRL scope、单环境、NVE post-hoc 上形成完全共识**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_dd4a07a509df7e5f9a31d65f776059bc:reviewer_3"
}
```

</details>

---
