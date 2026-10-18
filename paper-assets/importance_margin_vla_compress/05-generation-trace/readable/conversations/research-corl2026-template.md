# research corl2026 template

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 19
- **Recorded user turns:** 0
- **Tool calls:** 9
- **Original source:** `logs/chats/worker_research_corl2026_template_20260518T172947.jsonl`
- **Structured JSON:** [`50a9615197d0660b14ee.json`](../../sessions/50/50a9615197d0660b14ee.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

19 recorded events

### Tool call

_source line 1 · 2026-05-18T17:31:04.290907+00:00_

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
  "session": "worker_research_corl2026_template_20260518T172947",
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

_source line 2 · 2026-05-18T17:31:04.291275+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_corl2026_template_20260518T172947",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-18T17:31:04.291476+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoRL 2026 official latex template"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_corl2026_template_20260518T172947",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL 2026 official latex template"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-18T17:31:04.291654+00:00_

Web search results for query: "CoRL 2026 official latex template"

Links: [{"title":"CoRL LaTeX Template | Robot Learning Conference Format | Underleaf","url":"https://www.underleaf.ai/templates/corl"},{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"LaTeX Templates for NeurIPS, ICML, CVPR, ACL & More | Underleaf","url":"https://www.underleaf.ai/templates"},{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"GitHub - korpling/CRC-template: LaTeX template for Collaborative Research Center proposals following the DFG guidelines. · GitHub","url":"https://github.com/korpling/CRC-template"},{"title":"LaTeX Templates [Lehigh ISE / COR@L Lab Wiki]","url":"https://coral.ise.lehigh.edu/wiki/doku.php/resources:latex"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"Update CoRL 2026 conference details · huggingface/ai-deadlines at 0ba012a","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/0ba012abbc2f4e96e0072f99fd68649bfc69d9cf"},{"title":"COLM 2026 Template - Overleaf, Online LaTeX Editor","url":"https://www.overleaf.com/latex/templates/colm-2026-template/wbwzrwczsqvg"},{"title":"Robot Learning Foundation","url":"https://www.robot-learning.org/"}]

Based on the search results, here's information about the CoRL 2026 official LaTeX template:

## Official Template Source

The official LaTeX template is available at: https://drive.google.com/file/d/1R9irIW0ImqeDHh5g8Ukm2XGy91sWxOsQ/view?usp=drive_link

## Template Specifications

The CoRL LaTeX template uses a custom style based on PMLR (Proceedings of Machine Learning Research) format. Papers are limited to 8 pages of content plus unlimited references.

## Important Usage Notes

When using the template, make sure to use "\usepackage[final]{corl_2026}." For those preparing camera-ready papers, the camera-ready paper should follow the template: 8-page main text + ack
…[truncated 426 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_corl2026_template_20260518T172947",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-18T17:31:04.291845+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CoRL 2026 instruction for authors latex template download",
  "allowed_domains": "['corl.org', 'www.corl.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_corl2026_template_20260518T172947",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CoRL 2026 instruction for authors latex template download",
    "allowed_domains": "['corl.org', 'www.corl.org']"
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-18T17:31:04.291981+00:00_

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
  "session": "worker_research_corl2026_template_20260518T172947",
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

_source line 7 · 2026-05-18T17:31:04.292102+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_corl2026_template_20260518T172947",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-18T17:31:04.292267+00:00_

Web search results for query: "CoRL 2026 instruction for authors latex template download"

Links: [{"title":"CoRL 2026 - Instruction for Authors","url":"https://www.corl.org/contributions/instruction-for-authors"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"CoRL 2026","url":"https://www.corl.org/"},{"title":"CoRL 2026 - Instruction for Presentations","url":"https://www.corl.org/contributions/instruction-for-presentations"},{"title":"CoRL 2026 - Annoucements","url":"https://www.corl.org/annoucements"},{"title":"CoRL 2024 - Instruction for Authors","url":"https://2024.corl.org/contributions/instruction-for-authors"},{"title":"CoRL 2026 - Demos","url":"https://www.corl.org/program/demos"},{"title":"CoRL 2026 - Registration","url":"https://www.corl.org/attending/registration"},{"title":"CoRL 2026 - Contributions","url":"https://www.corl.org/contributions"},{"title":"CoRL 2021 - Submission Instructions","url":"https://2021.corl.org/author-information/submission-instructions"}]

Based on the search results, I found the information about the CoRL 2026 LaTeX template for authors:

The LaTeX template for CoRL 2026 is available here: https://drive.google.com/file/d/1R9irIW0ImqeDHh5g8Ukm2XGy91sWxOsQ/view?usp=drive_link

All submissions should comply with the format and length indicated, with a page limit of 8 pages for the main paper, while Acknowledgments, References, and Appendix (optional) will not count towards the page limit.

You can access the template directly from the Google Drive link provided above to download it for your paper submission.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_corl2026_template_20260518T172947",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-18T17:31:04.292416+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://www.corl.org/contributions/instruction-for-authors",
  "prompt": "Extract all information about: 1) LaTeX template download link, 2) submission format requirements (page limit, anonymous, line numbers), 3) documentclass options, 4) submission platform (OpenReview?), 5) any style file details (corl_2026.sty, .cls, etc)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_corl2026_template_20260518T172947",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://www.corl.org/contributions/instruction-for-authors",
    "prompt": "Extract all information about: 1) LaTeX template download link, 2) submission format requirements (page limit, anonymous, line numbers), 3) documentclass options, 4) submission platform (OpenReview?), 5) any style file details (corl_2026.sty, .cls, etc)"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-18T17:31:04.292549+00:00_

# CoRL 2026 Submission Information

## 1) LaTeX Template Download Links

- **Initial Submission Template**: Available at https://drive.google.com/file/d/1R9irIW0ImqeDHh5g8Ukm2XGy91sWxOsQ/view?usp=drive_link
- **Camera-Ready Template**: Available at https://drive.google.com/file/d/19xt72-5YaVqhWRO-ErqRQZ2SPZef8FFe/view?usp=drive_link

## 2) Submission Format Requirements

- **Page Limit**: "8 pages for the main paper" for initial submission; 9 pages for camera-ready version
- **Anonymous Submission**: Double-blind required; all papers must be anonymized for review
- **Line Numbers**: Not mentioned in the provided content

## 3) Documentclass Options

The camera-ready instructions specify: "make sure to use `\usepackage[final]{corl_2026}`"

This indicates a package rather than a documentclass option, suggesting the template uses a custom `corl_2026` package.

## 4) Submission Platform

Yes, submissions occur through OpenReview: "Papers may be submitted through OpenReview via the link [here]" at https://openreview.net/group?id=robot-learning.org/CoRL/2026/Conference

## 5) Style File Details

The document references `corl_2026` as a package (not a separate `.sty` or `.cls` file explicitly detailed). Authors should use `\usepackage[final]{corl_2026}` in their camera-ready submissions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_corl2026_template_20260518T172947",
  "tool": "WebFetch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-18T17:31:04.292748+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts && mkdir -p corl_template && cd corl_template && curl -L \"https://drive.google.com/uc?export=download&id=1R9irIW0ImqeDHh5g8Ukm2XGy91sWxOsQ\" -o corl_2026_template.zip 2>&1 | tail -5 && ls -la corl_2026_template.zip && file corl_2026_template.zip",
  "description": "Download CoRL 2026 initial submission template from Google Drive",
  "timeout": "30000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_corl2026_template_20260518T172947",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts && mkdir -p corl_template && cd corl_template && curl -L \"https://drive.google.com/uc?export=download&id=1R9irIW0ImqeDHh5g8Ukm2XGy91sWxOsQ\" -o corl_2026_template.zip 2>&1 | tail -5 && ls -la corl_2026_template.zip && file corl_2026_template.zip",
    "description": "Download CoRL 2026 initial submission template from Google Drive",
    "timeout": "30000"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-18T17:31:04.292952+00:00_

  % Total    % Received % Xferd  Average Speed  Time    Time    Time   Current
                                 Dload  Upload  Total   Spent   Left   Speed
  0      0   0      0   0      0      0      0                              0  0      0   0      0   0      0      0      0                              0  0      0   0      0   0      0      0      0                              0
  0      0   0      0   0      0      0      0                              0  0      0   0      0   0      0      0      0           00:01              0100  17423 100  17423   0      0  13663      0   00:01   00:01          16028100  17423 100  17423   0      0  13662      0   00:01   00:01          16028100  17423 100  17423   0      0  13661      0   00:01   00:01          16028
-rw-r--r-- 1 ubuntu ubuntu 17423 May 18 17:30 corl_2026_template.zip
corl_2026_template.zip: Zip archive data, made by v2.0 UNIX, extract using at least v2.0, last modified Feb 09 2026 10:00:08, uncompressed size 0, method=store

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_corl2026_template_20260518T172947",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-18T17:31:04.293093+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "unzip -o corl_2026_template.zip && find . -type f | head -30",
  "description": "Unzip CoRL 2026 template and list files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_corl2026_template_20260518T172947",
  "tool": "Bash",
  "tool_args": {
    "command": "unzip -o corl_2026_template.zip && find . -type f | head -30",
    "description": "Unzip CoRL 2026 template and list files"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-18T17:31:04.293341+00:00_

Archive:  corl_2026_template.zip
   creating: corl_2026_template_submission/
  inflating: __MACOSX/._corl_2026_template_submission  
  inflating: corl_2026_template_submission/.DS_Store  
  inflating: __MACOSX/corl_2026_template_submission/._.DS_Store  
  inflating: corl_2026_template_submission/example.bib  
  inflating: __MACOSX/corl_2026_template_submission/._example.bib  
  inflating: corl_2026_template_submission/corlabbrvnat.bst  
  inflating: __MACOSX/corl_2026_template_submission/._corlabbrvnat.bst  
  inflating: corl_2026_template_submission/example.tex  
  inflating: __MACOSX/corl_2026_template_submission/._example.tex  
  inflating: corl_2026_template_submission/corl_2026.sty  
  inflating: __MACOSX/corl_2026_template_submission/._corl_2026.sty  
./corl_2026_template.zip
./corl_2026_template_submission/corl_2026.sty
./corl_2026_template_submission/.DS_Store
./corl_2026_template_submission/example.tex
./corl_2026_template_submission/corlabbrvnat.bst
./corl_2026_template_submission/example.bib
./__MACOSX/corl_2026_template_submission/._corl_2026.sty
./__MACOSX/corl_2026_template_submission/._example.tex
./__MACOSX/corl_2026_template_submission/._corlabbrvnat.bst
./__MACOSX/corl_2026_template_submission/._example.bib
./__MACOSX/corl_2026_template_submission/._.DS_Store
./__MACOSX/._corl_2026_template_submission

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_corl2026_template_20260518T172947",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-18T17:31:04.293558+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/corl_template/corl_2026_template_submission/example.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_corl2026_template_20260518T172947",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/corl_template/corl_2026_template_submission/example.tex"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-18T17:31:04.293749+00:00_

1	\documentclass{article}
2	
3	\usepackage{corl_2026} % Use this for the initial submission.
4	% \usepackage[final]{corl_2026} % Uncomment for the camera-ready ``final'' version.
5	% \usepackage[preprint]{corl_2026} % Uncomment for pre-prints (e.g., arxiv); This is like ``final'', but will remove the CORL footnote.
6	
7	\title{Formatting Instructions for CoRL 2026 Camera-Ready}
8	
9	% The \author macro works with any number of authors. There are two
10	% commands used to separate the names and addresses of multiple
11	% authors: \And and \AND.
12	%
13	% Using \And between authors leaves it to LaTeX to determine where to
14	% break the lines. Using \AND forces a line break at that point. So,
15	% if LaTeX puts 3 of 4 authors names on the first line, and the last
16	% on the second line, try using \AND instead of \And before the third
17	% author name.
18	
19	% NOTE: authors will be visible only in the camera-ready and preprint versions (i.e., when using the option 'final' or 'preprint'). 
20	% 	For the initial submission the authors will be anonymized.
21	
22	\author{
23	  Jane E.~Doe\\
24	  Department of Electrical Engineering and Computer Sciences\\
25	  University of California Berkeley 
26	  United States\\
27	  \texttt{janedoe@berkeley.edu} \\
28	  %% examples of more authors
29	  %% \And
30	  %% Coauthor \\
31	  %% Affiliation \\
32	  %% Address \\
33	  %% \texttt{email} \\
34	  %% \AND
35	  %% Coauthor \\
36	  %% Affiliation \\
37	  %% Address \\
38	  %% \texttt{email} \\
39	  %% \And
40	  %% Coauthor \\
41	  %% Affiliation \\
42	  %% Address \\
43	  %% \texttt{email} \\
44	  %% \And
45	  %% Coauthor \\
46	  %% Affiliation \\
47	  %% Address \\
48	  %% \texttt{email} \\
49	}
50	
51	
52	\begin{document}
53	\maketitle
54	
55	%===============================================================================
56	
57	\begin{abstract}
58	    The purpose of this document is to provide both the basic paper template and submission guidelines. Abstracts should be a single 
…[truncated 6129 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_corl2026_template_20260518T172947",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-18T17:31:04.293908+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/corl_template/corl_2026_template_submission/corl_2026.sty"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_corl2026_template_20260518T172947",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/corl_template/corl_2026_template_submission/corl_2026.sty"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-18T17:31:04.294223+00:00_

1	% File: corl_2026.sty 
2	%
3	% Latex templates for the Conference on Robot Learning (CoRL)
4	%
5	% This template is heavily inspired by the NeurIPS, ICML, ICLR and IEEE Transactions latex templates.
6	% Hence we would like to thank: Roman Garnett and the previous mantainers of the NIPS style, Percy Liang and the previous mantainers of the ICML style, Hugo Larochelle for the ICLR style, and Michael Shell for the IEEE Transactions style.
7	%
8	% History:
9	% 2017/04/16 - First revision by Roberto Calandra (roberto.calandra@berkeley.edu).
10	%	       Main changes:
11	%	       - The abstract is more compact compared to NeurIPS/ICML
12	%	       - References are by default using natbib with squared numbers (e.g., [1])
13	%	       - DOI fields from the bibtex are automatically converted to hyperlinks 
14	%	       to the corresponding page
15	%	       - acknowledgments are now a command, and the corresponding subsubsection is
16	%	       automatically included only in the final version
17	% 2017/06/12 - Modified to use corlabbrvnat.bst, which order the reference by order of appearance in the paper
18	% 2017/06/13 - fixed typo
19	% 2018/05/09 - Slightly modified for CoRL 2018 by Jun Morimoto (xmorimo@atr.jp)
20	% 2019/01/28 - Slightly modified for CoRL 2019 by Jun Nakanishi (jnakanis@meijo-u.ac.jp)
21	% 2020/02/02 - Slightly modified for CoRL 2020 by Cynthia Matuszek (cmat@umbc.edu)
22	% 2020/08/19 - Added preprint option by Roberto Calandra (rcalandra@fb.com)
23	% 2021/05/06 - Slightly modified for CoRL 2021 by Gerhard Neumann (gerhard.neumann@kit.edu)
24	% 2022/03/09 - Slightly modified for CoRL 2022 by Minas Liarokapis (minas.liarokapis@auckland.ac.nz)
25	% 2022/03/06 - Slightly modified for CoRL 2023 by Marc Toussaint (toussaint@tu-berlin.de)
26	% 2024/03/26 - Slightly modified for CoRL 2024 by David Held (dheld@andrew.cmu.edu)
27	% 2026/01/10 - Slightly modified for CoRL 2026 by Yoonchang Sung (yoonchang.sung@ntu.edu.sg)
28	%
29	% TODO: nohyperref is not working at th
…[truncated 14645 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_corl2026_template_20260518T172947",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-18T17:31:04.294479+00:00_

模板文件已完整获取。以下是结果汇总：

---

## CoRL 2026 官方 LaTeX 模板

### 模板来源
- **官方页面**: [CoRL 2026 Instruction for Authors](https://www.corl.org/contributions/instruction-for-authors)
- **Initial Submission 模板**: [Google Drive 下载](https://drive.google.com/file/d/1R9irIW0ImqeDHh5g8Ukm2XGy91sWxOsQ/view?usp=drive_link)
- **Camera-Ready 模板**: [Google Drive 下载](https://drive.google.com/file/d/19xt72-5YaVqhWRO-ErqRQZ2SPZef8FFe/view?usp=drive_link)

### 模板类型
**CoRL 自定义 .sty**（基于 NeurIPS/ICML/ICLR 风格修改），不是 .cls 文件。

模板文件清单：
- `corl_2026.sty` — 主样式文件
- `example.tex` — 模板主文件
- `example.bib` — 参考文献示例
- `corlabbrvnat.bst` — 引用排序样式（按出现顺序）

### documentclass 选项

```latex
\documentclass{article}

\usepackage{corl_2026}            % 初始投稿（匿名、带行号）
% \usepackage[final]{corl_2026}   % Camera-ready（显示作者、去行号）
% \usepackage[preprint]{corl_2026} % Preprint/arXiv（显示作者、去 CoRL 脚注）
```

可用选项：`final`, `preprint`, `nonatbib`, `nohyperref`

### 关键格式规范
- **页数**: 正文 8 页（camera-ready 9 页），References 和 Appendix 不计入
- **匿名**: 默认 double-blind，作者显示为 "Anonymous Author(s)"
- **行号**: submission 版自动启用（`\linenumbers`），final/preprint 版无行号
- **投稿平台**: [OpenReview](https://openreview.net/group?id=robot-learning.org/CoRL/2026/Conference)
- **会议信息**: 第 10 届 CoRL，Austin TX, USA

### 已下载位置
模板已解压到：
```
artifacts/corl_template/corl_2026_template_submission/
```

**当前项目的 12 行 placeholder `corl_2026.cls` 应替换为这个官方 `corl_2026.sty`，并将 `\documentclass` 改为 `\documentclass{article}` + `\usepackage{corl_2026}`。**

Sources:
- [CoRL 2026 Instruction for Authors](https://www.corl.org/contributions/instruction-for-authors)
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)
- [CoRL 2026 Homepage](https://www.corl.org/)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_corl2026_template_20260518T172947"
}
```

</details>

---
