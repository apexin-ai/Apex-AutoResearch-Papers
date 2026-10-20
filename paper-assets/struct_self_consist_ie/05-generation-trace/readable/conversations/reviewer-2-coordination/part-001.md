# Reviewer 2 coordination — Part 1 of 9

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Conversation logs

[Transcript overview](../reviewer-2-coordination.md) · [Part 2 →](part-002.md) · [Structured JSON](../../../sessions/dd/dded1175c26e184c6fa2.json)

## Round 1

## Round 1

68 recorded events


### User

_source line 1 · 2026-05-14T12:03:59.740429+00:00_

[Round 1 审稿请求]:
## R2 审稿任务：新颖性与相关工作

**论文**："Log-Probability Is All You Need? A Systematic Evaluation of Confidence Signals for Test-Time Scaling in Structured Information Extraction"

**论文概要**：本文系统比较了 5 种 confidence signal 在结构化 IE test-time scaling 中的表现，核心发现是 "systematic negative result"：multi-sampling consistency 不优于 log-probability，揭示了 task-complexity boundary（RE 上所有信号退化），并确立 soft Jaccard 为 consistency 族内最佳实践。论文自我定位为 "systematic negative result + diagnostic framework" 贡献模式，目标 EMNLP Main/Findings。

**你的审稿重点**：新颖性评估 + 相关工作完整性

请围绕以下维度评审：
1. **新颖性**：
   - "首个系统比较 log-prob vs consistency for structured IE" 的 claim 是否成立？是否有先驱工作已做过类似比较？
   - 负面结果的信息量如何？是否可预测（fine-tuned model 的 log-prob 本来就该是好的 calibration signal）？
   - "diagnostic framework"（ceiling/floor/hallucination consistency）作为贡献是否充分？还是仅仅是 post-hoc 观察？
2. **相关工作覆盖**：
   - Self-consistency 文献：Wang et al. 2023, USC, 是否遗漏 Chen et al. 2023 (universal self-consistency variants)、Aggarwal et al. 2023？
   - Calibration 文献：是否引用 Guo et al. 2017 (modern neural net calibration)、Kadavath et al. 2022 (LM self-evaluation)？
   - TTS scaling 文献：是否提及 Snell et al. 2024 (scaling test-time compute)、process reward models？
   - Structured prediction confidence：CRF-based 方法、span-based NER 的 confidence 估计？
   - 注意：论文中所有引用都是 "?" 占位符
3. **Claim 与证据匹配**：
   - Claim 1 (log-prob dominates NER): 证据链是否完整？
   - Claim 2 (task-complexity boundary): 仅 SciERC RE 一个数据集是否充分？
   - Claim 3 (SJ best within consistency): 与主结论（consistency 不如 log-prob）的关系是否清晰？
4. **贡献定位**：
   - "Systematic negative result" 在 EMNLP 的接受历史中是否有先例？
   - 对比 Findings vs Main 的门槛，本文在哪个层级？
5. **写作与呈现**：
   - Abstract/Introduction 的 framing 是否恰当？
   - 3 个 key findings 的层次是否清晰？
   - Discussion (Section 6) 是否充分？

请输出：3-5 个 strengths、5-8 个 weaknesses，每个带具体引用，最后给出初步评分（1-6 scale）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 2 · 2026-05-14T12:04:06.961767+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 3 · 2026-05-14T12:04:07.012564+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 4 · 2026-05-14T12:04:09.521698+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review-reviewer-session-start*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review-reviewer-session-start*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1"
  }
}
```

</details>

---


### Tool result

_source line 5 · 2026-05-14T12:04:09.622402+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 6 · 2026-05-14T12:04:14.044305+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review-reviewer-session-start*",
  "path": "/home/ubuntu/agent-ml-research"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review-reviewer-session-start*",
    "path": "/home/ubuntu/agent-ml-research"
  }
}
```

</details>

---


### Tool result

_source line 7 · 2026-05-14T12:04:14.195244+00:00_

/home/ubuntu/agent-ml-research/skills/global/review-reviewer-session-start.skill.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 8 · 2026-05-14T12:04:16.063334+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 9 · 2026-05-14T12:04:16.064067+00:00_

1	---
2	name: review-reviewer-session-start
3	description: Review Reviewer session 启动初始化——检查论文格式、编译状态、材料清单。Review Reviewer 角色 session 启动时自动使用。
4	priority: 8
5	scope: global
6	tags:
7	- workflow
8	- review
9	- session
10	version: 2
11	roles: []
12	---
13	
14	# Review Reviewer Session 启动流程
15	
16	执行顺序：
17	1. 读取论文文件（`projects/{project}/paper/main.tex` 或类似路径）
18	2. 检查论文格式状态：
19	   - 页数是否在 venue 要求内（若已知 venue）
20	   - LaTeX 是否可编译（调用 `ssh_execute` 运行 `pdflatex` 或 `latexmk`）
21	   - 图表是否有标题和标签
22	3. 视觉检查：如果已有编译好的 PDF，使用 `paper-visual-review` skill 渲染关键页面（首页、图表页、参考文献页），检查排版溢出、公式渲染、图表质量等视觉问题
23	4. 检查投稿材料清单：
24	   - cover letter 是否存在
25	   - 补充材料是否准备
26	   - 参考文献格式是否正确
27	5. 向 Review Director 汇报（`review_reviewer_post_to_director`）：
28	   - 论文当前状态
29	   - 发现的格式问题（如有）
30	   - 视觉检查结果（如有）
31	   - 缺少的材料（如有）
32	
33	此流程在 Review Director 分配任务后执行。
34	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 10 · 2026-05-14T12:04:19.832112+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.pdf",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 11 · 2026-05-14T12:04:21.488855+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T093336/best/paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T093336/median/paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T093336/worst/paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/median/paper.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/worst/paper.pdf

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 1656
}
```

</details>

---


### Tool call

_source line 12 · 2026-05-14T12:04:21.489457+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 13 · 2026-05-14T12:04:21.539969+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 14 · 2026-05-14T12:04:34.938035+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/",
  "description": "List latest dream report best directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/",
    "description": "List latest dream report best directory"
  }
}
```

</details>

---


### Tool result

_source line 15 · 2026-05-14T12:04:35.390617+00:00_

total 496
drwxr-xr-x 3 ubuntu ubuntu   4096 May 14 12:04 .
drwxr-xr-x 6 ubuntu ubuntu   4096 May 14 11:42 ..
drwxr-xr-x 2 ubuntu ubuntu   4096 May 14 12:04 _pdf_images
-rw-r--r-- 1 ubuntu ubuntu  48249 May 14 11:32 experiment_data.json
-rw-r--r-- 1 ubuntu ubuntu  45454 May 14 11:32 imagined_experiments.yaml
-rw-r--r-- 1 ubuntu ubuntu  14995 May 14 11:37 paper.aux
-rw-r--r-- 1 ubuntu ubuntu  22907 May 14 11:37 paper.log
-rw-r--r-- 1 ubuntu ubuntu   4055 May 14 11:37 paper.out
-rw-r--r-- 1 ubuntu ubuntu 222709 May 14 11:37 paper.pdf
-rw-r--r-- 1 ubuntu ubuntu  41198 May 14 11:37 paper.tex
-rw-r--r-- 1 ubuntu ubuntu   6745 May 14 11:32 paper_framing.md
-rw-r--r-- 1 ubuntu ubuntu  45443 May 14 11:46 review_context.yaml
lrwxrwxrwx 1 ubuntu ubuntu    140 May 14 11:46 review_input_db82206b.pdf -> /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/paper.pdf
-rw-r--r-- 1 ubuntu ubuntu  16970 May 14 11:56 review_report.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 16 · 2026-05-14T12:04:35.892706+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/",
  "description": "List dream reports directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/",
    "description": "List dream reports directory"
  }
}
```

</details>

---


### Tool result

_source line 17 · 2026-05-14T12:04:36.145198+00:00_

total 20
drwxr-xr-x  4 ubuntu ubuntu 4096 May 14 10:53 .
drwxr-xr-x 16 ubuntu ubuntu 4096 May 14 11:56 ..
drwxr-xr-x  6 ubuntu ubuntu 4096 May 14 10:29 dream_20260514T093336
drwxr-xr-x  6 ubuntu ubuntu 4096 May 14 11:42 dream_20260514T105303
lrwxrwxrwx  1 ubuntu ubuntu  125 May 14 10:29 latest -> /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T093336

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 252
}
```

</details>

---


### Tool call

_source line 18 · 2026-05-14T12:04:36.195834+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2025 2026 reviewer guidelines review form criteria scoring"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2025 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool result

_source line 19 · 2026-05-14T12:04:44.845053+00:00_

Web search results for query: "EMNLP 2025 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"FAQ - EMNLP 2026","url":"https://2026.emnlp.org/faq/"},{"title":"Changes to reviewer volunteering requirement and incentives in May 2025 cycle (EMNLP 2025)","url":"http://aclrollingreview.org/incentives2025"},{"title":"EMNLP 2025 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2025%2FConference"},{"title":"ClimateNLP 2026","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"[Policy Spotlight] EMNLP 2025 Criteria for “Highly Irresponsible” Reviewers — What It Means & Why It Matters | CSPaper Forum","url":"https://forum.cspaper.org/topic/70/policy-spotlight-emnlp-2025-criteria-for-highly-irresponsible-reviewers-what-it-means-why-it-matters"},{"title":"[Policy Spotlight] EMNLP 2025 Criteria for “Highly Irresponsible” Reviewers — What It Means & Why It Matters | CSPaper","url":"https://cspaper.org/topic/70/policy-spotlight-emnlp-2025-criteria-for-highly-irresponsible-reviewers-what-it-means-why-it-matters"},{"title":"ARR Reviewer Guidelines","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Advice on Reviewing for EMNLP","url":"https://2020.emnlp.org/blog/2020-05-17-write-good-reviews/"},{"title":"EMNLP 2026 (@emnlpmeeting) / Posts / X","url":"https://x.com/emnlpmeeting?lang=en"}]

Based on the search results, here's what I found about EMNLP 2025/2026 reviewer guidelines and scoring criteria:

## Scoring System

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation. Additionally, soundness scores must be justified by the text of the review.

## Review Quality and Standards

The EMNLP 2025 program chairs have established clear expectations for responsible reviewing. The program chairs and ARR
…[truncated 1151 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8649
}
```

</details>

---


### Tool call

_source line 20 · 2026-05-14T12:04:49.018762+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR review form 2025 2026 soundness excitement overall recommendation scoring scale 1-5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR review form 2025 2026 soundness excitement overall recommendation scoring scale 1-5"
  }
}
```

</details>

---


### Tool call

_source line 21 · 2026-05-14T12:04:49.370322+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
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

_source line 22 · 2026-05-14T12:04:49.421196+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 23 · 2026-05-14T12:04:55.999344+00:00_

Web search results for query: "ACL ARR review form 2025 2026 soundness excitement overall recommendation scoring scale 1-5"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"ACL 2023 Acceptance Recommendations - ACL 2023","url":"https://2023.aclweb.org/blog/overall-recommendation/"},{"title":"aclrollingreview/reviewerguidelines.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewerguidelines.md"},{"title":"Program Chairs’ Report on Peer Review at ACL 2023 Anna Rogers}","url":"https://aclanthology.org/2023.acl-long.report.pdf"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"ACL 2026 on X: \"Checkout the blog post on the soundness/excitement scores https://t.co/AKSO9DjiYP . It clarifies the reasoning behind the separation of overall scores and how it might make the reviewer recommendation more robust. #ACL2023Toronto #ACL2023NLP #NLProc\" / X","url":"https://x.com/aclmeeting/status/1637827267173953540"},{"title":"ACL’23 Peer Review Policies - ACL 2023","url":"https://2023.aclweb.org/blog/review-acl23/"}]

Based on the search results, here's what I found about the ACL ARR review form for 2025-2026:

## Three Scoring Components

Starting with February 
…[truncated 1418 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6980
}
```

</details>

---


### Tool call

_source line 24 · 2026-05-14T12:05:02.133239+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form including all scoring dimensions, their scales (1-5 or whatever scale is used), and the description for each score level. I need the exact wording for soundness, excitement, overall recommendation, and any other scored dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form including all scoring dimensions, their scales (1-5 or whatever scale is used), and the description for each score level. I need the exact wording for soundness, excitement, overall recommendation, and any other scored dimensions."
  }
}
```

</details>

---


### Tool result

_source line 25 · 2026-05-14T12:05:12.789352+00:00_

# ACL Rolling Review Form - Scoring Dimensions

## 1. **Reviewer Confidence**
Scale: 1-5
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: "Quite sure. I tried to check the important points carefully."
- **3**: "Pretty sure, but there's a chance I missed something."
- **2**: "Willing to defend my evaluation, but it is fairly likely that I missed some details."
- **1**: "Not my area, or paper is very hard to understand."

## 2. **Soundness**
Scale: 1-5 (with half-point increments)
- **5**: "Excellent: This study is one of the most thorough I have seen, given its type."
- **4**: "Strong: This study provides sufficient support for all its claims."
- **3**: "Acceptable: This study provides sufficient support for its main claims."
- **2**: "Poor: Some of the main claims are not sufficiently supported."
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication."

## 3. **Excitement**
Scale: 1-5 (with half-point increments)
- **5**: "Highly Exciting: I would recommend this paper to others and/or attend its presentation."
- **4**: "Exciting: I would mention this paper to others and/or make effort to attend."
- **3**: "Interesting: I might mention some points to others and/or attend if time permits."
- **2**: "Potentially Interesting: this paper does not resonate with me, but it might with others."
- **1**: "Not Exciting: this paper does not resonate with me, and I don't think it would with others."

## 4. **Overall Assessment**
Scale: 1-5 (with half-point increments)
- **5**: "Consider for Award: could be considered for outstanding paper award (top 2.5%)."
- **4**: "Conference: could be accepted to an ACL conference."
- **3**: "Findings: could be accepted to the Findings of the ACL."
- **2**: "Resubmit next cycle: needs substantial revisions by next ARR cycle."
- **1**: "Do not resubmit: has to be fully redone or irrelevant to ACL community."

## 5. **Reproducibilit
…[truncated 1059 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 10656
}
```

</details>

---


### Tool call

_source line 26 · 2026-05-14T12:05:22.198937+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/paper.pdf",
  "pages": "1-8",
  "dpi": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/paper.pdf",
    "pages": "1-8",
    "dpi": "200"
  }
}
```

</details>

---


### Tool call

_source line 27 · 2026-05-14T12:05:24.260106+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete reviewer guidelines, especially: what makes a good review, how to evaluate novelty, how to handle negative results papers, any specific guidance on scoring, and what reviewers should look for in terms of related work coverage and claims-evidence matching."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete reviewer guidelines, especially: what makes a good review, how to evaluate novelty, how to handle negative results papers, any specific guidance on scoring, and what reviewers should look for in terms of related work coverage and claims-evidence matching."
  }
}
```

</details>

---


### Tool result

_source line 28 · 2026-05-14T12:05:26.171357+00:00_

Error: result (4,146,127 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-2-a0c838f5/02891594-3c8d-48a5-ba32-a91063a88a0a/tool-results/mcp-agent-ml-research-pdf_to_images-1778760325950.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-2-a0c838f5/02891594-3c8d-48a5-ba32-a91063a88a0a/tool-results/mcp-agent-ml-research-pdf_to_images-1778760325950.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-2-a0c838f5/02891594-3c8d-48a5-ba32-a91063a88a0a/tool-results/mcp-agent-ml-research-pdf_to_images-1778760325950.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 3972
}
```

</details>

---


### Tool result

_source line 29 · 2026-05-14T12:05:36.067556+00:00_

# ARR Reviewer Guidelines: Key Principles for Writing Strong Reviews

## What Makes a Good Review

ARR emphasizes **specificity and clarity**. Reviews should avoid vague criticisms like "X is not clear" in favor of precise statements: "Y and Z are missing from the description of X." The goal is enabling area chairs to understand issues without rereading the full paper.

Reviews must maintain **professional, neutral tone**. As the guidelines state: "Write the review you would like to get yourself." Sarcasm and dismissiveness damage reviewer credibility and author morale.

## Evaluating Novelty

The guidelines caution against several common biases regarding novelty:

- **Results seeming obvious in retrospect** doesn't mean the community already knows them
- **Lack of precedent** shouldn't trigger rejection—truly novel work is inherently harder to publish
- **Missing specific references** matters more than general claims; cite actual prior work when asserting non-novelty

Papers may contribute through methods, resources, surveys, or analysis—not all require SOTA results.

## Handling Negative Results

Negative results address publication bias plaguing science. The guidelines explicitly state that systematic failures "the community does need to know about." Rejection based on results being negative reflects reviewer bias, not sound evaluation.

## Scoring Guidance

Three separate scores are required:

**Soundness** must align with review text. Low soundness scores need clear justification; unsupported low scores suggest unconscious bias.

**Excitement** reflects personal interest independently from soundness—papers can be sound but personally uninteresting.

**Overall assessment** combines soundness, excitement, novelty, and potential impact for venue suitability.

## Related Work Coverage

Papers should fairly represent prior contributions. Missing references published 3+ months before submission deadlines qualify as problematic gaps. However, recent preprints needn't 
…[truncated 645 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 11807
}
```

</details>

---


### Tool call

_source line 30 · 2026-05-14T12:05:41.544261+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/paper.pdf",
  "pages": "1-2",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/paper.pdf",
    "pages": "1-2",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 31 · 2026-05-14T12:05:42.157710+00:00_

Error: result (942,429 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-2-a0c838f5/02891594-3c8d-48a5-ba32-a91063a88a0a/tool-results/mcp-agent-ml-research-pdf_to_images-1778760342127.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-2-a0c838f5/02891594-3c8d-48a5-ba32-a91063a88a0a/tool-results/mcp-agent-ml-research-pdf_to_images-1778760342127.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-2-a0c838f5/02891594-3c8d-48a5-ba32-a91063a88a0a/tool-results/mcp-agent-ml-research-pdf_to_images-1778760342127.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 613
}
```

</details>

---


### Tool call

_source line 32 · 2026-05-14T12:05:52.109629+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/_pdf_images/",
  "description": "List rendered PDF images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/_pdf_images/",
    "description": "List rendered PDF images"
  }
}
```

</details>

---


### Tool result

_source line 33 · 2026-05-14T12:05:52.261292+00:00_

total 3860
drwxr-xr-x 2 ubuntu ubuntu   4096 May 14 12:05 .
drwxr-xr-x 3 ubuntu ubuntu   4096 May 14 12:04 ..
-rw-r--r-- 1 ubuntu ubuntu 305224 May 14 12:05 paper_p1.png
-rw-r--r-- 1 ubuntu ubuntu 295100 May 14 12:05 paper_p10.png
-rw-r--r-- 1 ubuntu ubuntu 320082 May 14 12:05 paper_p11.png
-rw-r--r-- 1 ubuntu ubuntu  64455 May 14 12:05 paper_p12.png
-rw-r--r-- 1 ubuntu ubuntu 400971 May 14 12:05 paper_p2.png
-rw-r--r-- 1 ubuntu ubuntu 318351 May 14 12:05 paper_p3.png
-rw-r--r-- 1 ubuntu ubuntu 367604 May 14 12:05 paper_p4.png
-rw-r--r-- 1 ubuntu ubuntu 369345 May 14 12:05 paper_p5.png
-rw-r--r-- 1 ubuntu ubuntu 375077 May 14 12:05 paper_p6.png
-rw-r--r-- 1 ubuntu ubuntu 397215 May 14 12:05 paper_p7.png
-rw-r--r-- 1 ubuntu ubuntu 400425 May 14 12:05 paper_p8.png
-rw-r--r-- 1 ubuntu ubuntu 309062 May 14 12:05 paper_p9.png

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 34 · 2026-05-14T12:05:57.782695+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/_pdf_images/paper_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/_pdf_images/paper_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 35 · 2026-05-14T12:05:58.135309+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/_pdf_images/paper_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/_pdf_images/paper_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 36 · 2026-05-14T12:05:58.439428+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 656
}
```

</details>

---


### Tool call

_source line 37 · 2026-05-14T12:05:58.439937+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/_pdf_images/paper_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/_pdf_images/paper_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 38 · 2026-05-14T12:05:59.145409+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/_pdf_images/paper_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/_pdf_images/paper_p4.png"
  }
}
```

</details>

---


### Tool result

_source line 39 · 2026-05-14T12:05:59.246822+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1111
}
```

</details>

---


### Tool result

_source line 40 · 2026-05-14T12:06:01.113172+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2673
}
```

</details>

---


### Tool result

_source line 41 · 2026-05-14T12:06:01.617878+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2472
}
```

</details>

---


### Tool call

_source line 42 · 2026-05-14T12:06:08.558315+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/_pdf_images/paper_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/_pdf_images/paper_p5.png"
  }
}
```

</details>

---


### Tool call

_source line 43 · 2026-05-14T12:06:09.012316+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/_pdf_images/paper_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/_pdf_images/paper_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 44 · 2026-05-14T12:06:10.372709+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/_pdf_images/paper_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/_pdf_images/paper_p7.png"
  }
}
```

</details>

---


### Tool call

_source line 45 · 2026-05-14T12:06:10.423495+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/_pdf_images/paper_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/_pdf_images/paper_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 46 · 2026-05-14T12:06:11.835691+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 3277
}
```

</details>

---


### Tool result

_source line 47 · 2026-05-14T12:06:12.505817+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 3493
}
```

</details>

---


### Tool result

_source line 48 · 2026-05-14T12:06:14.019905+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 3647
}
```

</details>

---


### Tool result

_source line 49 · 2026-05-14T12:06:14.121222+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 3697
}
```

</details>

---


### Tool call

_source line 50 · 2026-05-14T12:06:19.494841+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/_pdf_images/paper_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/_pdf_images/paper_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 51 · 2026-05-14T12:06:20.351054+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 856
}
```

</details>

---


### Tool call

_source line 52 · 2026-05-14T12:06:20.351567+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/_pdf_images/paper_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/_pdf_images/paper_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 53 · 2026-05-14T12:06:20.859182+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 507
}
```

</details>

---


### Tool call

_source line 54 · 2026-05-14T12:06:20.859656+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/_pdf_images/paper_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/_pdf_images/paper_p11.png"
  }
}
```

</details>

---


### Tool result

_source line 55 · 2026-05-14T12:06:21.363570+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 56 · 2026-05-14T12:06:21.363902+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/_pdf_images/paper_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/_pdf_images/paper_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 57 · 2026-05-14T12:06:21.415217+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 58 · 2026-05-14T12:09:12.466710+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "systematic comparison confidence signals self-consistency log-probability information extraction NER test-time scaling"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "systematic comparison confidence signals self-consistency log-probability information extraction NER test-time scaling"
  }
}
```

</details>

---


### Tool call

_source line 59 · 2026-05-14T12:09:12.922081+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Aggarwal 2023 adaptive consistency self-consistency LLM sampling"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Aggarwal 2023 adaptive consistency self-consistency LLM sampling"
  }
}
```

</details>

---


### Tool call

_source line 60 · 2026-05-14T12:09:13.326199+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Snell 2024 \"scaling LLM test-time compute\" optimal"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Snell 2024 \"scaling LLM test-time compute\" optimal"
  }
}
```

</details>

---


### Tool result

_source line 61 · 2026-05-14T12:09:17.802766+00:00_

Web search results for query: "Aggarwal 2023 adaptive consistency self-consistency LLM sampling"

Links: [{"title":"Let’s Sample Step by Step: Adaptive-Consistency for Efficient Reasoning and Coding with LLMs - ACL Anthology","url":"https://aclanthology.org/2023.emnlp-main.761/"},{"title":"[2305.11860] Let's Sample Step by Step: Adaptive-Consistency for Efficient Reasoning and Coding with LLMs","url":"https://arxiv.org/abs/2305.11860"},{"title":"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning","url":"https://arxiv.org/html/2601.02970v1"},{"title":"GitHub - Pranjal2041/AdaptiveConsistency: Let's Sample Step by Step: Adaptive-Consistency for Efficient Reasoning with LLMs · GitHub","url":"https://github.com/Pranjal2041/AdaptiveConsistency"},{"title":"Paper page - Let's Sample Step by Step: Adaptive-Consistency for Efficient Reasoning with LLMs","url":"https://huggingface.co/papers/2305.11860"},{"title":"Let's Sample Step by Step: Adaptive-Consistency for Efficient Reasoning & Coding with LLMs","url":"https://sample-step-by-step.info/"},{"title":"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM","url":"https://arxiv.org/pdf/2601.02970"},{"title":"Self-Consistency Sampling in LLMs","url":"https://www.emergentmind.com/topics/self-consistency-sampling"},{"title":"Reevaluating Self-Consistency Scaling in Multi-Agent Systems Chiyan Loo","url":"https://arxiv.org/pdf/2511.00751"},{"title":"Let's Sample Step by Step: Adaptive-Consistency for Efficient Reasoning and Coding with LLMs | OpenReview","url":"https://openreview.net/forum?id=ETNa4Wb65J"}]

Based on the search results, I found comprehensive information about the Aggarwal 2023 paper on Adaptive-Consistency:

## Overview

The paper titled "Let's Sample Step by Step: Adaptive-Consistency for Efficient Reasoning and Coding with LLMs" was published in the 2023 Conference on Empirical Methods in Natural Language Processing. The authors are Pranjal Aggarwal, Aman Mad
…[truncated 1196 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 4880
}
```

</details>

---


### Tool result

_source line 62 · 2026-05-14T12:09:20.265274+00:00_

Web search results for query: "Snell 2024 "scaling LLM test-time compute" optimal"

Links: [{"title":"[2408.03314] Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters","url":"https://arxiv.org/abs/2408.03314"},{"title":"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters","url":"https://arxiv.org/html/2408.03314v1"},{"title":"Scaling LLM Test-Time Compute Optimally Can be More Effective than Scaling Parameters for Reasoning | OpenReview","url":"https://openreview.net/forum?id=4FWAwZtd2n"},{"title":"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters | by Eleventh Hour Enthusiast | Medium","url":"https://medium.com/@EleventhHourEnthusiast/scaling-llm-test-time-compute-optimally-can-be-more-effective-than-scaling-model-parameters-19a0c9fb7c44"},{"title":"Scaling LLM Test-Time Compute Optimally can be More ...","url":"https://www.emergentmind.com/papers/2408.03314"},{"title":"Scaling LLM Test Time Compute","url":"https://www.jonvet.com/blog/llm-test-time-compute"},{"title":"Is That Your Final Answer? Test-Time Scaling Improves ...","url":"https://aclanthology.org/2025.acl-short.50.pdf"},{"title":"What is Test Time Compute? | CSA","url":"https://cloudsecurityalliance.org/blog/2024/12/13/test-time-compute"},{"title":"Scaling LLM Test-Time Compute Optimally Can be More ...","url":"https://faculty.cc.gatech.edu/~zk15/teaching/AY2025_cs7643_spring/assets/L25_Charlie_Snell_Scaling_TestTime_Compute.pdf"},{"title":"24. Scaling LLM Test-Time Compute Optimally (Snell et al., 2024) - YouTube","url":"https://www.youtube.com/watch?v=7AztQ9xuHWQ"}]

I found the paper you're looking for. Here are the key details:

## Paper Overview

The paper is titled "Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters" by Charlie Snell and 3 other authors (Lee, Xu, and Kumar from Google DeepMind).

## Main Research Question

The paper focus
…[truncated 1133 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6939
}
```

</details>

---


### Tool result

_source line 63 · 2026-05-14T12:09:22.423792+00:00_

Web search results for query: "systematic comparison confidence signals self-consistency log-probability information extraction NER test-time scaling"

Links: [{"title":"DeepConf: Thinking Smarter, Not Harder — How Confidence Signals Revolutionize LLM Reasoning Efficiency | by Sai Dheeraj Gummadi | Data Science in Your Pocket | Medium","url":"https://medium.com/data-science-in-your-pocket/deepconf-thinking-smarter-not-harder-how-confidence-signals-revolutionize-llm-reasoning-67ae5ec0ae2a"},{"title":"Confidence Improves Self-Consistency in LLMs","url":"https://aclanthology.org/2025.findings-acl.1030.pdf"},{"title":"A Theoretical Study on Bridging Internal Probability and ...","url":"https://www.arxiv.org/pdf/2510.15444"},{"title":"DeepConf: Confidence-Based LLM Reasoning","url":"https://www.emergentmind.com/topics/deep-think-with-confidence-deepconf"},{"title":"Confidence Improves Self-Consistency in LLMs","url":"https://arxiv.org/html/2502.06233v1"},{"title":"Certified Self-Consistency: Statistical Guarantees and Test-Time Training for Reliable Reasoning in LLMs","url":"https://arxiv.org/html/2510.17472"},{"title":"CERTIFIED SELF-CONSISTENCY: STATISTICAL GUARANTEES AND TEST-TIME","url":"https://arxiv.org/pdf/2510.17472"},{"title":"Self-Consistency in Language Models","url":"https://www.emergentmind.com/topics/self-consistency-in-language-models"},{"title":"Self-Consistency Sampling in LLMs","url":"https://www.emergentmind.com/topics/self-consistency-sampling"},{"title":"GitHub - IAAR-Shanghai/ICSFSurvey: Explore concepts like Self-Correct, Self-Refine, Self-Improve, Self-Contradict, Self-Play, and Self-Knowledge, alongside o1-like reasoning elevation🍓 and hallucination alleviation🍄.","url":"https://github.com/IAAR-Shanghai/ICSFSurvey"}]

I found relevant research on confidence signals, self-consistency, and test-time scaling in LLMs. Here are the key findings:

## Overview of Recent Research

Confidence signals are metrics derived from an LLM's internal token probab
…[truncated 1904 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 9957
}
```

</details>

---


### Tool call

_source line 64 · 2026-05-14T12:09:28.898381+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"confidence estimation\" \"named entity recognition\" LLM self-consistency comparison 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"confidence estimation\" \"named entity recognition\" LLM self-consistency comparison 2024 2025"
  }
}
```

</details>

---


### Tool result

_source line 65 · 2026-05-14T12:09:35.024214+00:00_

Web search results for query: ""confidence estimation" "named entity recognition" LLM self-consistency comparison 2024 2025"

Links: [{"title":"Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models - ACL Anthology","url":"https://aclanthology.org/2024.naacl-short.49/"},{"title":"Confidence Improves Self-Consistency in LLMs","url":"https://arxiv.org/html/2502.06233v1"},{"title":"Confidence Improves Self-Consistency in LLMs","url":"https://aclanthology.org/2025.findings-acl.1030.pdf"},{"title":"Confidence Improves Self-Consistency in LLMs - ACL Anthology","url":"https://aclanthology.org/2025.findings-acl.1030/"},{"title":"GitHub - Emma1066/Self-Improve-Zero-Shot-NER: This is the github repository for the paper at NAACL 2024: Self-Improving for Zero-Shot Named Entity Recognition with Large Language Models. · GitHub","url":"https://github.com/Emma1066/Self-Improve-Zero-Shot-NER"},{"title":"Measuring Confidence in LLM responses | by George Karapetyan | Medium","url":"https://medium.com/@georgekar91/measuring-confidence-in-llm-responses-e7df525c283f"},{"title":"Benchmarking LLM Uncertainty and Calibration with ...","url":"https://aclanthology.org/2026.eacl-long.106.pdf"},{"title":"Stability Evaluation of Confidence Features Across Model and Data Variants in Large Language Models — Research and Science Today","url":"https://www.rstjournal.com/article/4.2026"},{"title":"Confidence Improves Self-Consistency in LLMs | by Ema Ilic | Medium","url":"https://medium.com/@ema.ilic9/confidence-improves-self-consistency-in-llms-313e80467168"},{"title":"[2502.06233] Confidence Improves Self-Consistency in LLMs","url":"https://arxiv.org/abs/2502.06233"}]

Based on the search results, here's what I found regarding confidence estimation, named entity recognition, LLM self-consistency, and comparisons from 2024-2025:

## Key Research Findings

### Self-Consistency with Named Entity Recognition (2024)

Research on applying large language models to named entity re
…[truncated 1576 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6125
}
```

</details>

---


### Tool call

_source line 66 · 2026-05-14T12:12:00.496367+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## R2 审稿完成：新颖性与相关工作\n\n**论文**: \"Log-Probability Is All You Need? A Systematic Evaluation of Confidence Signals for Test-Time Scaling in Structured Information Extraction\"\n\n---\n\n## 总体评分\n**Overall**: 3/5 (Findings)\n**一句话总结**: 实验设计扎实的经验研究，但方法新颖性有限（SJ 是评估指标的自然迁移），RE 上的 task-complexity boundary claim 仅由单一数据集支撑，相关工作存在显著遗漏。\n\n## 官方维度打分（ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | NER claims 有多 seed + 多数据集 + p-value 支撑；RE complexity boundary 仅基于 SciERC 一个数据集(n=397)，证据链不完整 |\n| Excitement | 2.5/5 | 研究问题实用，但核心发现（set-level agreement > sequence-level log-prob）对领域内可预期；\"diagnostic framework\" 实为标准消融包装 |\n| Overall | 3/5 | Findings 水平——有用的经验贡献但不够 Main 的新颖性门槛 |\n| Reproducibility | 4/5 | 方法清晰、超参明确、多 seed，但未提供代码 |\n| Confidence | 4/5 | 熟悉 self-consistency、calibration、NER/RE 文献 |\n\n## Must-Fix 问题\n\n**N1** [critical] 方法新颖性有限——SJ 是 IE 评估指标到 confidence 的自然迁移\n- Section 3.2, Eq(1): type-grouped Hungarian matching + token-overlap kernel 本质是 set-level F1/Jaccard 的 confidence 版本\n- 未提供理论分析解释 Δρ≈0.16 的来源，也未与其他 set-similarity kernel（edit distance、embedding similarity）做消融\n\n**N2** [critical] Task-complexity boundary 证据严重不足\n- Section 5.9, Table 12: 全部 RE 实验仅在 SciERC relation subset (n=397, 6 relation types) 上进行\n- \"Universal bottleneck\" claim 需跨数据集验证（TACRED/DocRED/NYT），单数据集观察至多是 hypothesis\n\n**N3** [critical] 相关工作显著遗漏\n- **Guo et al. 2017** (On Calibration of Modern Neural Networks, ICML) — 论文讨论 ECE 但未引用定义 ECE 的奠基论文\n- **Snell et al. 2024** (Scaling LLM Test-Time Compute, ICLR 2025) — 标题围绕 TTS 却未引用该核心工作\n- **Aggarwal et al. 2023** (Adaptive-Consistency, EMNLP 2023) — 与 N-scaling (Section 5.2) 直接相关\n- **CISC** (Huang et al. 2025, Confidence Improves Self-Consistency, ACL Findings 2025) — 加权投票+confidence 融合，发现 \"最 calibrated 的方法反而最无效\"，直接挑战本文解读\n- **传统 IE confidence** — CRF 边际概率、span-level confidence、MC-dropout uncertainty 完全未讨论\n\n**N4** [critical] 标题与核心发现不匹配\n- \"Log-Probability Is All You Need?\" 暗示 log-prob 可能足够，但论文核心发现是 SJ 显著优于 log-prob (Δρ=0.16, p<10⁻²⁵)\n- 修辞反问制造阅读期望与实际结论的认知冲突\n\n## Should-Fix 问题\n\n**W1** [warning] 仅 2 个 8B 模型，70B+ 模型的 calibration 可能改变 SJ vs log-prob 的差距\n**W2** [warning] 未比较任何 trained approach (verifier/reward model/learned combination)\n**W3** [warning] \"Diagnostic framework\" 过度包装——实际是标准 error analysis (F1 分桶、component 分解、stratification)\n**W4** [warning] 全文 17 张表 0 张图，可读性差\n**W5** [warning] Exact-Match Voting 对结构化输出是 straw man baseline\n\n## 小问题\n- Abstract 有 \"?\" 未解析引用\n- 仅英语数据集\n- 温度敏感性分析仅 T=0.7 和 T=1.0 两点\n\n## 主要优势\n- **S1**: 研究问题清晰且有实际意义\n- **S2**: 实验设计系统化（3 dataset × 2 model × 2 budget × 4 metric × 3 seed）\n- **S3**: SJ 的 Hungarian matching 设计合理，leave-one-out 验证排除 circularity\n- **S4**: Best-of-N selection 将 ranking → F1 gain，实用性强\n- **S5**: 消融维度全面（N-scaling、cross-dataset、cross-model、temperature、OOD、stratification）\n\n## 对 Director 问题的回应\n\n**1. \"首个系统比较\" claim 是否成立？**\n基本成立但需限定。在 {LLM-based IE} × {多种 confidence signals} × {best-of-N selection} 这个交叉点上，我未找到直接先驱工作。但论文忽略了：(a) 传统 IE 的 confidence 估计传统；(b) reasoning 任务上的类似比较（CISC 等）。建议改为 \"first systematic comparison for LLM-based structured IE\"。\n\n**2. 负面结果信息量？**\n需要澄清：论文的核心发现实际上是 **正面结果**（SJ > log-prob），不是 Director 概要中说的 \"consistency 不优于 log-probability\"。RE 上的退化是次要发现，且仅单数据集支撑。负面结果（RE 退化）的可预测性中等——compound error 对有 IE 经验的人不意外，但系统量化有一定价值。\n\n**3. Diagnostic framework 贡献是否充分？**\n不充分。这些是标准消融技术（分桶、分层、component 分解），不构成可复用的 framework。建议降格为 \"diagnostic analysis\"。\n\n**4. EMNLP 定位？**\nFindings 可接受，Main 偏弱。论文的实用价值（practitioners 的 confidence signal 选择指南）适合 Findings 定位，但方法新颖性和 claim 覆盖不足以支撑 Main。",
  "reviewer_id": "2",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## R2 审稿完成：新颖性与相关工作\n\n**论文**: \"Log-Probability Is All You Need? A Systematic Evaluation of Confidence Signals for Test-Time Scaling in Structured Information Extraction\"\n\n---\n\n## 总体评分\n**Overall**: 3/5 (Findings)\n**一句话总结**: 实验设计扎实的经验研究，但方法新颖性有限（SJ 是评估指标的自然迁移），RE 上的 task-complexity boundary claim 仅由单一数据集支撑，相关工作存在显著遗漏。\n\n## 官方维度打分（ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | NER claims 有多 seed + 多数据集 + p-value 支撑；RE complexity boundary 仅基于 SciERC 一个数据集(n=397)，证据链不完整 |\n| Excitement | 2.5/5 | 研究问题实用，但核心发现（set-level agreement > sequence-level log-prob）对领域内可预期；\"diagnostic framework\" 实为标准消融包装 |\n| Overall | 3/5 | Findings 水平——有用的经验贡献但不够 Main 的新颖性门槛 |\n| Reproducibility | 4/5 | 方法清晰、超参明确、多 seed，但未提供代码 |\n| Confidence | 4/5 | 熟悉 self-consistency、calibration、NER/RE 文献 |\n\n## Must-Fix 问题\n\n**N1** [critical] 方法新颖性有限——SJ 是 IE 评估指标到 confidence 的自然迁移\n- Section 3.2, Eq(1): type-grouped Hungarian matching + token-overlap kernel 本质是 set-level F1/Jaccard 的 confidence 版本\n- 未提供理论分析解释 Δρ≈0.16 的来源，也未与其他 set-similarity kernel（edit distance、embedding similarity）做消融\n\n**N2** [critical] Task-complexity boundary 证据严重不足\n- Section 5.9, Table 12: 全部 RE 实验仅在 SciERC relation subset (n=397, 6 relation types) 上进行\n- \"Universal bottleneck\" claim 需跨数据集验证（TACRED/DocRED/NYT），单数据集观察至多是 hypothesis\n\n**N3** [critical] 相关工作显著遗漏\n- **Guo et al. 2017** (On Calibration of Modern Neural Networks, ICML) — 论文讨论 ECE 但未引用定义 ECE 的奠基论文\n- **Snell et al. 2024** (Scaling LLM Test-Time Compute, ICLR 2025) — 标题围绕 TTS 却未引用该核心工作\n- **Aggarwal et al. 2023** (Adaptive-Consistency, EMNLP 2023) — 与 N-scaling (Section 5.2) 直接相关\n- **CISC** (Huang et al. 2025, Confidence Improves Self-Consistency, ACL Findings 2025) — 加权投票+confidence 融合，发现 \"最 calibrated 的方法反而最无效\"，直接挑战本文解读\n- **传统 IE confidence** — CRF 边际概率、span-level confidence、MC-dropout uncertainty 完全未讨论\n\n**N4** [critical] 标题与核心发现不匹配\n- \"Log-Probability Is All You Need?\" 暗示 log-prob 可能足够，但论文核心发现是 SJ 显著优于 log-prob (Δρ=0.16, p<10⁻²⁵)\n- 修辞反问制造阅读期望与实际结论的认知冲突\n\n## Should-Fix 问题\n\n**W1** [warning] 仅 2 个 8B 模型，70B+ 模型的 calibration 可能改变 SJ vs log-prob 的差距\n**W2** [warning] 未比较任何 trained approach (verifier/reward model/learned combination)\n**W3** [warning] \"Diagnostic framework\" 过度包装——实际是标准 error analysis (F1 分桶、component 分解、stratification)\n**W4** [warning] 全文 17 张表 0 张图，可读性差\n**W5** [warning] Exact-Match Voting 对结构化输出是 straw man baseline\n\n## 小问题\n- Abstract 有 \"?\" 未解析引用\n- 仅英语数据集\n- 温度敏感性分析仅 T=0.7 和 T=1.0 两点\n\n## 主要优势\n- **S1**: 研究问题清晰且有实际意义\n- **S2**: 实验设计系统化（3 dataset × 2 model × 2 budget × 4 metric × 3 seed）\n- **S3**: SJ 的 Hungarian matching 设计合理，leave-one-out 验证排除 circularity\n- **S4**: Best-of-N selection 将 ranking → F1 gain，实用性强\n- **S5**: 消融维度全面（N-scaling、cross-dataset、cross-model、temperature、OOD、stratification）\n\n## 对 Director 问题的回应\n\n**1. \"首个系统比较\" claim 是否成立？**\n基本成立但需限定。在 {LLM-based IE} × {多种 confidence signals} × {best-of-N selection} 这个交叉点上，我未找到直接先驱工作。但论文忽略了：(a) 传统 IE 的 confidence 估计传统；(b) reasoning 任务上的类似比较（CISC 等）。建议改为 \"first systematic comparison for LLM-based structured IE\"。\n\n**2. 负面结果信息量？**\n需要澄清：论文的核心发现实际上是 **正面结果**（SJ > log-prob），不是 Director 概要中说的 \"consistency 不优于 log-probability\"。RE 上的退化是次要发现，且仅单数据集支撑。负面结果（RE 退化）的可预测性中等——compound error 对有 IE 经验的人不意外，但系统量化有一定价值。\n\n**3. Diagnostic framework 贡献是否充分？**\n不充分。这些是标准消融技术（分桶、分层、component 分解），不构成可复用的 framework。建议降格为 \"diagnostic analysis\"。\n\n**4. EMNLP 定位？**\nFindings 可接受，Main 偏弱。论文的实用价值（practitioners 的 confidence signal 选择指南）适合 Findings 定位，但方法新颖性和 claim 覆盖不足以支撑 Main。",
    "reviewer_id": "2",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 67 · 2026-05-14T12:12:04.622463+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4126
}
```

</details>

---


### Assistant

_source line 68 · 2026-05-14T12:12:13.590299+00:00_

审稿已完成并提交给 Review Director。

核心判断：**Overall 3/5 (Findings)**。4 个 Must-Fix 问题中最关键的是——(1) SJ 方法新颖性有限（评估指标到 confidence 的自然迁移），(2) RE task-complexity boundary 仅由 SciERC 一个数据集支撑无法称 "universal"，(3) 5 篇重要参考文献缺失（Guo 2017、Snell 2024、Aggarwal 2023、CISC 2025、传统 IE confidence），(4) 标题暗示 log-prob 足够但论文实际证明 SJ 大幅优于 log-prob，存在 framing 冲突。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2"
}
```

</details>

---


## Round 2

## Round 2

14 recorded events


### User

_source line 69 · 2026-05-14T12:14:19.717660+00:00_

[Round 1 审稿请求]:
## 交叉分享：请逐条回应 Reviewer 1 的审稿意见

以下是 Reviewer 1（方法与实验方向）的完整审稿原文。请逐条回应：
- **[AGREE]** 同意并说明理由
- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）
- 特别关注你与 R1 是否在相同问题上有不同判断

---

## R1 审稿意见：方法与实验

### 总体评分
**Overall Assessment**: 3/5 (Findings) | Director 1-6 scale: **4/6** (Weak Accept, borderline Findings)
**一句话总结**: 实验覆盖面广、诊断分析有深度的 empirical study，但模型规模单一（仅 8B）、零图表的呈现方式、以及误导性的成本分析共同削弱了核心主张的说服力。

### ARR 官方维度打分

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/5 | 核心方法论合理，评估协议良好；但成本分析存在误导，仅 2 个 8B 模型限制普适性 |
| Excitement | 3/5 | 研究问题及时，compound error boundary 有启发性；但贡献以 empirical comparison 为主 |
| Reproducibility | 4/5 | 数据集公开、参数详尽；但未发布代码，prompt 模板未给出 |
| Confidence | 4/5 | 熟悉 NER/RE 评估和 TTS 方法 |

### 主要优势

**S1.** 系统且全面的实验矩阵（5 signal × 3 NER dataset × 1 RE dataset × 2 model × 2 budget × 2 temp × 4 metric，13/15 完整覆盖）
**S2.** LOO-SJ circularity check 是方法论亮点（Table 1, ρ=0.40 vs full SJ ρ=0.42）
**S3.** Compound error boundary 诊断有理论价值（Section 5.9, Table 12）
**S4.** 多维度鲁棒性验证（multi-seed, cross-dataset, cross-model, OOD）
**S5.** Inverted-U pattern（Section 5.11, Table 15）为 SJ 适用条件提供直觉

### Must-Fix 问题

**N1** [critical] 模型规模单一，严重限制普适性
- 仅 Qwen3-8B 和 LLaMA-3.1-8B 两个 8B 模型
- 更大模型的 greedy 可能已足够准确（LP 优势更明显），更小模型高方差可能放大 SJ 优势
- Abstract 中 "establish" 措辞过强
- 建议：至少增加一个 >30B 或 <3B 模型，或降级措辞

**N2** [critical] 成本分析系统性误导
- Section 6: 称 SJ 额外成本 "negligible (O(N²) set comparisons vs. O(N) LLM forward passes)"
- 忽略 LP 可在 greedy decode（1 pass）上工作，SJ 需要 N≥8 pass
- 公平对比：LP@N=1 → ρ≈0.26; SJ@N=8 → 8× cost → ρ≈0.38; SJ@N=16 → 16× cost → ρ≈0.42
- 将 8-16× 推理开销描述为 "negligible" 是不准确的
- 建议：增加 cost-effectiveness 分析

**N3** [critical] 全文零图表
- 17 个表格，0 个 Figure
- 缺少 selection curves、reliability diagrams、cost-effectiveness scatter
- Table 8 有 selection curve 数据但以表格呈现
- 建议：至少添加 3 个核心 Figure

### Should-Fix 问题

**W1** [warning] 未探索 signal combination（Section 5.8, SJ 和 LP 互补 Δρ=0.14）
**W2** [warning] 单一 prompt 模板，缺乏 prompt sensitivity 分析
**W3** [warning] RE 仅有 SciERC 一个数据集，"universal bottleneck" 主张建立在单一数据集上
**W4** [warning] 统计检验不系统（3 seed std 不替代正式 bootstrap CI）
**W5** [warning] 缺少 SJ 失败案例分析（高 SJ 低 F1 / 低 SJ 高 F1 的模式）

### 小问题
- 标题暗示答案为 yes，但实际结论为 no
- Table 16 entity count 6+ 时 SJ ρ 降至 0.34 未解释
- Eq.(1) SJ 的 similarity kernel 未明确
- adaptive_compute_demo 无显式 adaptive 策略呈现

---

请对以上每个 Must-Fix（N1-N3）、Should-Fix（W1-W5）和小问题逐条给出 [AGREE] 或 [REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 70 · 2026-05-14T12:14:36.983296+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/_pdf_images/paper_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/_pdf_images/paper_p2.png"
  }
}
```

</details>

---


### Tool call

_source line 71 · 2026-05-14T12:14:37.438683+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/_pdf_images/paper_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/_pdf_images/paper_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 72 · 2026-05-14T12:14:38.418534+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1435
}
```

</details>

---


### Tool result

_source line 73 · 2026-05-14T12:14:40.477601+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 3038
}
```

</details>

---


### Tool call

_source line 74 · 2026-05-14T12:14:43.897449+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/_pdf_images/paper_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/_pdf_images/paper_p5.png"
  }
}
```

</details>

---


### Tool call

_source line 75 · 2026-05-14T12:14:45.003918+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/_pdf_images/paper_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/_pdf_images/paper_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 76 · 2026-05-14T12:14:45.155389+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/_pdf_images/paper_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/_pdf_images/paper_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 77 · 2026-05-14T12:14:46.113329+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2215
}
```

</details>

---


### Tool result

_source line 78 · 2026-05-14T12:14:48.078740+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 3074
}
```

</details>

---


### Tool result

_source line 79 · 2026-05-14T12:14:48.230219+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 3074
}
```

</details>

---


### Tool call

_source line 80 · 2026-05-14T12:17:07.901014+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## R2 交叉回应 R1 审稿意见\n\n### 汇总\n\n| R1 Issue | R2 判断 | 要点 |\n|----------|--------|------|\n| N1 模型规模 | [AGREE] | 与 R2-W1 一致，8B→8B 只验证了架构鲁棒性非规模鲁棒性 |\n| N2 成本误导 | [REBUT] | 同意加 cost-effectiveness 分析，但反对\"系统性误导\"定性——论文在 TTS 语境内准确（同 N 下 SJ 远优于 LP），R1 的 LP@N=1 vs SJ@N=8 对比混淆了 selective prediction 与 TTS |\n| N3 零图表 | [AGREE] | 与 R2-W4 一致 |\n| W1 signal combo | [AGREE] | 与 R2-W2 一致，Section 5.8 已证明互补性却不做组合实验 |\n| W2 prompt sensitivity | [AGREE] | R1 的有价值补充，我原始审稿未覆盖 |\n| W3 RE 单数据集 | [AGREE] | 与 R2-N2 一致，两位 reviewer 共同 critical |\n| W4 统计检验 | [AGREE] | 部分同意，但 p-value 极小(10⁻²⁵)已部分弥补 |\n| W5 失败案例 | [REBUT] | Section 5.11 inverted-U + Table 15 已提供统计层面分析，但确实缺实例级 case study |\n| Minor-1 标题 | [AGREE] | 与 R2-N4 一致 |\n| Minor-2 Table 16 | [AGREE] | entity count 6+ 的 ρ 下降需解释 |\n| Minor-3 Eq.(1) kernel | [REBUT] | Section 3.2 有写\"token-level overlap\"，只是表述分散 |\n| Minor-4 adaptive demo | [AGREE] | PDF 中未找到相关内容 |\n\n### R1 与 R2 的共识和分歧\n\n**共识（高置信度问题）**:\n- 模型规模不足（R1-N1 = R2-W1）\n- RE 单数据集不支撑 universal claim（R1-W3 = R2-N2）\n- 零图表严重影响可读性（R1-N3 = R2-W4）\n- 标题与结论矛盾（R1-Minor-1 = R2-N4）\n- 需要 signal combination 实验（R1-W1 ≈ R2-W2）\n\n**分歧**:\n- **成本分析**: R1 定性为 \"systematic misleading\"（critical），我认为在 TTS 语境下论文的 O(N²) vs O(N) 陈述是准确的，应降为 warning 级（需补充 cost-effectiveness 分析但不构成误导）\n- **SJ 失败分析**: R1 认为完全缺失，我认为 Section 5.11 的 inverted-U 分析部分覆盖了此问题\n- **严重程度排序**: R1 将模型规模列为最高优先级 critical，我认为相关工作遗漏（R2-N3）同等或更高优先级——遗漏 Snell et al. 2024、Guo et al. 2017、CISC 等核心文献对论文可信度的影响大于模型数量\n\n### 总体判断一致性\n两位 reviewer 对 Overall 评分完全一致：**3/5 (Findings)**。核心分歧在于具体问题的严重程度排序，而非论文整体定位。",
  "reviewer_id": "2",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## R2 交叉回应 R1 审稿意见\n\n### 汇总\n\n| R1 Issue | R2 判断 | 要点 |\n|----------|--------|------|\n| N1 模型规模 | [AGREE] | 与 R2-W1 一致，8B→8B 只验证了架构鲁棒性非规模鲁棒性 |\n| N2 成本误导 | [REBUT] | 同意加 cost-effectiveness 分析，但反对\"系统性误导\"定性——论文在 TTS 语境内准确（同 N 下 SJ 远优于 LP），R1 的 LP@N=1 vs SJ@N=8 对比混淆了 selective prediction 与 TTS |\n| N3 零图表 | [AGREE] | 与 R2-W4 一致 |\n| W1 signal combo | [AGREE] | 与 R2-W2 一致，Section 5.8 已证明互补性却不做组合实验 |\n| W2 prompt sensitivity | [AGREE] | R1 的有价值补充，我原始审稿未覆盖 |\n| W3 RE 单数据集 | [AGREE] | 与 R2-N2 一致，两位 reviewer 共同 critical |\n| W4 统计检验 | [AGREE] | 部分同意，但 p-value 极小(10⁻²⁵)已部分弥补 |\n| W5 失败案例 | [REBUT] | Section 5.11 inverted-U + Table 15 已提供统计层面分析，但确实缺实例级 case study |\n| Minor-1 标题 | [AGREE] | 与 R2-N4 一致 |\n| Minor-2 Table 16 | [AGREE] | entity count 6+ 的 ρ 下降需解释 |\n| Minor-3 Eq.(1) kernel | [REBUT] | Section 3.2 有写\"token-level overlap\"，只是表述分散 |\n| Minor-4 adaptive demo | [AGREE] | PDF 中未找到相关内容 |\n\n### R1 与 R2 的共识和分歧\n\n**共识（高置信度问题）**:\n- 模型规模不足（R1-N1 = R2-W1）\n- RE 单数据集不支撑 universal claim（R1-W3 = R2-N2）\n- 零图表严重影响可读性（R1-N3 = R2-W4）\n- 标题与结论矛盾（R1-Minor-1 = R2-N4）\n- 需要 signal combination 实验（R1-W1 ≈ R2-W2）\n\n**分歧**:\n- **成本分析**: R1 定性为 \"systematic misleading\"（critical），我认为在 TTS 语境下论文的 O(N²) vs O(N) 陈述是准确的，应降为 warning 级（需补充 cost-effectiveness 分析但不构成误导）\n- **SJ 失败分析**: R1 认为完全缺失，我认为 Section 5.11 的 inverted-U 分析部分覆盖了此问题\n- **严重程度排序**: R1 将模型规模列为最高优先级 critical，我认为相关工作遗漏（R2-N3）同等或更高优先级——遗漏 Snell et al. 2024、Guo et al. 2017、CISC 等核心文献对论文可信度的影响大于模型数量\n\n### 总体判断一致性\n两位 reviewer 对 Overall 评分完全一致：**3/5 (Findings)**。核心分歧在于具体问题的严重程度排序，而非论文整体定位。",
    "reviewer_id": "2",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 81 · 2026-05-14T12:17:12.028175+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4127
}
```

</details>

---


### Assistant

_source line 82 · 2026-05-14T12:17:20.459378+00:00_

交叉回应已提交。汇总：

- **8/12 项 AGREE**（N1 模型规模、N3 零图表、W1-W4、Minor-1/2），其中多项与我的原始审稿高度重叠
- **3/12 项 REBUT**：
  - **N2 成本误导**：论文在 TTS 语境下准确（同 N 时 SJ≫LP），R1 的 LP@N=1 vs SJ@N=8 对比混淆了 selective prediction 与 TTS，"系统性误导"定性过重
  - **W5 失败案例**：Section 5.11 inverted-U 已提供统计层面分析，但确实缺实例级 case study
  - **Minor-3 Eq.(1) kernel**：Section 3.2 明确写了 "token-level overlap"，只是表述分散
- **1 项无法验证**（Minor-4 adaptive demo，PDF 中未出现）

两位 reviewer 的 Overall 评分一致：**3/5 (Findings)**。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2"
}
```

</details>

---


## Round 3

## Round 3

54 recorded events


### User

_source line 83 · 2026-05-15T01:50:44.186277+00:00_

[Round 1 审稿请求]:
## Round 1 审稿任务 — Reviewer 2（新颖性 + Related Work 完整性 + 整体连贯性）

### Venue 信息
- **目标**: EMNLP 2026 Main Conference (via ACL Rolling Review, May cycle)
- **截止日期**: 2026-05-25
- **格式**: ACL template (`\usepackage[review]{acl}`)，长文 8 页正文 + 无限参考文献 + 附录不计页
- **匿名规则**: Double-blind (作者已标注 Anonymous)

### 论文信息
- **标题**: "Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence Signals for Test-Time Scaling in Information Extraction"
- **论文路径**: `projects/struct_self_consist_ie/docs/paper/main.tex`
- **各 section 文件**: `docs/paper/sections/` 下的 abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, discussion.tex, conclusion.tex, limitations.tex, appendix.tex

### 你的审查侧重

**新颖性 + Related Work 完整性 + 整体连贯性**。重点关注：

1. **新颖性评估**：
   - "correlation-selection gap" 概念是否为真正的新发现，还是已知现象的重新命名
   - 5 个 confidence signal 中哪些是新提出的、哪些是已有方法的直接套用
   - Soft Jaccard with Hungarian matching 的技术新颖性如何
   - 对比 Nedellec et al. (2026)，本文的增量贡献是否足够支撑 EMNLP 长文
   - "systematic comparison" 类论文在 EMNLP 的接受标准——是否有足够的 insight 而非仅仅是 benchmark

2. **Related Work 完整性**：
   - Self-consistency 线：Wang et al. (2023), Chen et al. (2024), Taubenfeld et al. (2025), Kang et al. (2025) 等是否全面
   - Structured IE 线：是否遗漏重要的 generative IE / constrained decoding 工作
   - Uncertainty/calibration 线：是否遗漏关键方法（如 conformal prediction 在 NLP 中的应用）
   - Test-time compute scaling 线：Snell et al. (2024), Brown et al. (2024) 之外是否有遗漏
   - 是否有 2025-2026 年的重要新工作被遗漏
   - **验证引用真实性**：抽查至少 5 篇引用，确认作者、年份、标题、venue 是否正确（特别关注 2025-2026 年的引用）

3. **整体连贯性**：
   - Abstract → Introduction → Method → Experiments → Discussion → Conclusion 的叙事线是否一致
   - Claims 是否都有实验支撑，是否有 overclaim
   - "Strong Predictors, Weak Selectors" 标题是否准确反映论文内容
   - Contribution list 是否与实际内容匹配
   - Discussion section 是否有多余的推测性内容

4. **写作质量**：
   - 术语一致性（signal names、metric names）
   - 图表标题是否自足（self-contained）
   - 数学符号是否一致
   - 是否有 repetitive content 或不必要的冗余

5. **遗漏的重要引用搜索**：
   - 请用 web_search 搜索以下关键词，检查是否有遗漏的重要 2025-2026 工作：
     - "self-consistency structured prediction 2025 2026"
     - "confidence estimation information extraction LLM 2025 2026"
     - "test-time scaling NER relation extraction 2025 2026"

请按 EMNLP 顶会最严格标准评审，不留情面。输出结构：Summary → Strengths → Weaknesses (Must-Fix / Should-Fix / Minor) → Missing References → Questions → Overall Assessment (strong reject / weak reject / borderline / weak accept / strong accept + 置信度)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 84 · 2026-05-15T01:51:00.147068+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
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

_source line 85 · 2026-05-15T01:51:00.198070+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 86 · 2026-05-15T01:51:05.722011+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 87 · 2026-05-15T01:51:06.425563+00:00_

1	\begin{abstract}
2	Test-time scaling through multi-sample generation promises quality improvements for LLM-based information extraction, but which confidence signals best serve quality estimation versus sample selection remains unclear.
3	We systematically compare five confidence signals from three families---structural (entity voting, Soft Jaccard), surface (exact match, Fleiss' $\kappa$), and model-internal (log-probability)---across NER and relation extraction on three datasets (SciERC, CoNLL-2003, WNUT-17) with two model families (Qwen3-8B, LLaMA-3.1-8B).
4	We find that the strongest signals achieve $\rho{=}0.38$ (entity voting) and AUROC${=}0.75$ (exact match) for quality estimation, with ranking and classification favoring different signals across task complexity; however, this strong quality estimation does not translate into selection gains---no signal reliably surpasses greedy decoding on either task ($p{>}0.39$, bootstrap) despite 13--18~pp of oracle headroom.
5	We term this disconnect the \textit{correlation-selection gap}: instance-level consistency signals predict which inputs the model handles reliably, not which output is best among $N$ candidates.
6	Signal rankings further depend on task difficulty---exact match dominates easy tasks, structural signals dominate hard tasks, and all signals converge when model capability is insufficient---establishing that signal choice should be guided by task difficulty and intended application.
7	These results reframe consistency signals as quality estimators rather than output selectors for structured IE.
8	\end{abstract}
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 703
}
```

</details>

---


### Tool call

_source line 88 · 2026-05-15T01:51:06.526493+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 89 · 2026-05-15T01:51:06.677921+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Self-consistency---sampling multiple outputs and aggregating them---has become a powerful strategy for improving language model reasoning.
4	On discrete-answer tasks such as arithmetic and commonsense QA, majority voting over chain-of-thought samples yields large gains: +18 percentage points on GSM8K \cite{wang2023selfconsistency}.
5	More broadly, test-time compute scaling through repeated sampling and selection has emerged as a complementary axis to model scaling, offering substantial quality improvements at inference time \cite{snell2024scaling, brown2024monkeys}.
6	These results rest on a shared assumption: that among $N$ stochastic samples, a selection mechanism can identify better outputs.
7	For tasks with a single correct answer, this assumption holds naturally---the majority vote is the selector.
8	But information extraction (IE) poses a fundamentally different challenge.
9	The output is not a single token or number; it is a \textit{set} of entities or relations with internal dependencies, where two samples may extract overlapping but non-identical structures.
10	There is no obvious majority to vote on, partial agreement is the norm rather than the exception, and the space of valid outputs is combinatorially large.
11	Can self-consistency still provide useful signal in this structured setting?
12	
13	Prior work on confidence estimation for LLM-based IE has conflated two distinct objectives: \textit{quality estimation} (which inputs does the model handle reliably?) and \textit{sample selection} (which of $N$ outputs is best?).
14	These require fundamentally different signal properties: the former benefits from instance-level aggregation, while the latter demands per-sample discrimination.
15	Self-consistency methods for discrete answers \cite{wang2023selfconsistency, chen2024usc} and weighted variants \cite{taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalence---an assumpti
…[truncated 3524 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 90 · 2026-05-15T01:51:06.678439+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 91 · 2026-05-15T01:51:07.180961+00:00_

1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Self-consistency and test-time scaling.}
4	Self-consistency decoding \cite{wang2023selfconsistency} improves reasoning by majority voting over chain-of-thought samples, assuming a discrete answer space.
5	Extensions to free-form text use LLM-based comparison \cite{chen2024usc}, atomic sub-claim decomposition \cite{thirukovalluru2024atomic}, or cross-sample hallucination detection \cite{manakul2023selfcheckgpt}.
6	For test-time scaling, \citet{snell2024scaling} characterize compute scaling laws and \citet{brown2024monkeys} show best-of-$N$ gains across tasks.
7	Recent reward-free selectors include confidence-weighted voting \cite{taubenfeld2025cisc}, KL-based self-certainty \cite{kang2025selfcertainty}, adaptive sampling \cite{kim2026reasc}, ranked aggregation \cite{wang2025rankedvoting}, and latent-space consistency \cite{oh2025latentsc}.
8	All target reasoning/QA with discrete answers.
9	Our work extends self-consistency to set-valued structured outputs and identifies the correlation-selection gap: strong quality estimation ($\rho{=}0.38$) coexists with selection failure ($p{>}0.39$).
10	
11	\paragraph{Consistency for structured IE.}
12	\citet{nedellec2026consistency} study consistency--accuracy correlations for LLM-based NER/RE, corroborating our quality-estimation findings.
13	However, they rely on surface-level matching (explicitly acknowledging it ``overlooks semantically consistent outputs''), do not study best-of-$N$ selection, and evaluate a single domain with hard prompting.
14	Our Soft Jaccard signal addresses the matching limitation through type-aware bipartite matching with span overlap.
15	CoCoA \cite{vashurin2025cocoa} fuses model confidence with inter-sample consistency for QA/summarization but does not address structured extraction.
16	Our evaluation builds on generative IE work \cite{zhou2024uniner, sainz2024gollie, josifoski2022genie, li2023codeie, wadhwa2023revisiting, wang2023instructuie
…[truncated 1727 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 92 · 2026-05-15T01:51:07.181489+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 93 · 2026-05-15T01:51:08.136411+00:00_

1	\section{Method}\label{sec:method}
2	
3	\subsection{Problem Formulation}\label{sec:formulation}
4	
5	Given a language model $\mathcal{M}$ and input $x$, we sample $N$ structured outputs $\{y_1, \ldots, y_N\}$ at temperature $T > 0$ via constrained decoding \cite{willard2023guided}.
6	Each $y_i$ is an entity set (NER) or relation set (RE).
7	A confidence signal $c$ serves two purposes: (a) \textit{quality estimation}---predicting which instances the model handles reliably, and (b) \textit{sample selection}---identifying the best output among $N$ candidates.
8	
9	A \textbf{per-sample signal} scores each $y_i$ independently, $c_{\text{ps}}: (x, y_i) \to \mathbb{R}$, enabling direct candidate ranking.
10	An \textbf{instance-level signal} aggregates over all $N$ samples, $c_{\text{il}}: (x, \{y_i\}_{i=1}^N) \to \mathbb{R}$, producing a single score per input.
11	This asymmetry---between predicting \textit{which inputs} are easy and selecting \textit{which output} is best---is central to the correlation-selection gap we investigate.
12	Notation is summarized in Appendix~\ref{app:notation}.
13	
14	\subsection{Confidence Signals}\label{sec:signals}
15	
16	We compare five signals from three families: \textit{model-internal} (log-probability), \textit{surface} (exact match, Fleiss' $\kappa$), and \textit{structural} (Soft Jaccard, entity voting).
17	
18	\paragraph{Log-probability (model-internal, per-sample).}
19	The only per-sample signal.
20	For sample $y_i$ with tokens $t_1, \ldots, t_{|y_i|}$:
21	\begin{equation}\label{eq:logprob}
22	c_{\text{lp}}(y_i) = \frac{1}{|y_i|} \sum_{j=1}^{|y_i|} \log p_{\mathcal{M}}(t_j \mid t_{<j}, x)
23	\end{equation}
24	
25	\paragraph{Exact match voting (surface, instance-level).}
26	The majority fraction---the proportion of samples producing the most common output:
27	\begin{equation}\label{eq:em}
28	c_{\text{em}}(x) = \frac{1}{N} \max_{y} \big|\{i : y_i = y\}\big|
29	\end{equation}
30	
31	\paragraph{Fleiss' $\kappa$ (surface, instance-lev
…[truncated 2626 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 94 · 2026-05-15T01:51:08.136862+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 95 · 2026-05-15T01:51:08.589306+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Datasets.}
8	We evaluate on three English IE benchmarks spanning a difficulty gradient.
9	\textbf{SciERC} \cite{luan2018scierc} contains 551 test instances annotated for joint NER (6 types) and RE (7 types).
10	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} provides 3{,}453 test sentences with 4 entity types, where models achieve ${>}$91\% micro F1.
11	\textbf{WNUT-17} \cite{derczynski2017wnut} consists of 1{,}287 social media instances with emerging entities, used to probe method boundaries (54\% zero F1).
12	
13	\paragraph{Models and sampling.}
14	Our primary model is \textbf{Qwen3-8B} (LoRA, $r{=}32$); for cross-model validation, we evaluate \textbf{LLaMA-3.1-8B-Instruct}.
15	We draw $N{=}8$ samples at $T{=}1.0$ (primary), with $N{=}16$ for scaling experiments.\footnote{$N{=}16$ results for CoNLL (Qwen) and SciERC (LLaMA) are in Table~\ref{tab:robustness} (Appendix~\ref{app:robustness}).}
16	Quality estimation uses Spearman $\rho$ and AUROC; downstream utility uses best-of-$N$ selection F1 with exact span matching (NER) and head-tail-label matching (RE).
17	Inference uses vLLM with constrained decoding \cite{willard2023guided}.
18	
19	%% ============================================================
20	\subsection{Quality Estimation Results}
21	\label{sec:qe_results}
22	
23	\begin{table*}[t]
24	\centering
25	\small
26	\caption{Quality estimation across tasks and models (Spearman $\rho$ and AUROC). Best value per block and column in \textbf{bold}. SciERC evaluates joint NER (6 types) and RE (7 types); CoNLL evaluates NER (4 types). Primary results use $N{=}8$, $T{=}1.0$; $N{=}16$ block reports LLaMA CoNLL 3-seed mean${\pm}$std.}
27	\label{tab:quality_estimation}
28	\begin{tabular}{ll cc cc cc cc}
29	\toprule
30	& & \multicolumn{2}{c}{\textbf{SciERC NER}} & \multicolumn{2}{c}{\textbf{SciERC RE}} & \multicolumn{2}{c}{\textbf{CoNLL (Qwen)}} & \mu
…[truncated 7771 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 96 · 2026-05-15T01:51:08.589688+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 97 · 2026-05-15T01:51:09.041949+00:00_

1	\section{Discussion}\label{sec:discussion}
2	
3	\paragraph{Practical recommendations.}
4	For per-instance quality ranking, entity voting provides the strongest rank correlation ($\rho{=}0.38$, Table~\ref{tab:quality_estimation}), though exact match leads binary discrimination on SciERC (AUROC${=}0.749$).
5	When temperature or cross-condition robustness is required, SJ is preferable: its temperature sensitivity is small with bootstrap CIs including zero (Table~\ref{tab:robustness}).
6	Under conditional filtering, EM leads on both NER and RE ($\rho{=}0.360$, $0.417$), extending binary-agreement advantages to the within-capability regime.
7	Signal rankings depend on task difficulty: EM dominates on easy tasks (CoNLL, F1${>}$0.91), Voting and SJ dominate on hard tasks (SciERC, F1$\,{\approx}\,$0.66), and all signals converge when model capability is insufficient (WNUT-17).
8	This ordering is model-agnostic, suggesting the difficulty gradient determines which signal family is most informative.
9	Conditional filtering confirms this pattern: removing zero-F1 instances shifts effective difficulty toward the easy-task regime, and EM reclaims the lead while Voting and SJ drop substantially (Voting RE: $0.350{\to}0.241$).
10	
11	\paragraph{Why quality estimators fail as selectors.}
12	Quality estimation ranks \textit{instances} by expected output quality via output distribution entropy; sample selection ranks \textit{candidates within a single instance}, requiring per-sample quality information that instance-level aggregation discards.
13	On SciERC NER, the random baseline (0.608) falls 3.6~pp below greedy (0.644), confirming per-instance sample variance exists; yet the oracle gap of 13.2~pp shows substantially better candidates exist, and the best signal captures only +0.6~pp ($p{=}0.39$).
14	The $\rho$--AUROC dissociation illuminates the same asymmetry: on SciERC, EM achieves the highest AUROC (0.749 NER, 0.706 RE) yet ranks third or last in $\rho$; both metrics measure be
…[truncated 1013 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 98 · 2026-05-15T01:51:09.042517+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 99 · 2026-05-15T01:51:09.544996+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	This work provides the first systematic evaluation of confidence signals for test-time scaling in generative information extraction.
4	By comparing five signals from three families---structural, surface, and model-internal---across NER and RE tasks of varying difficulty, we disentangle two objectives that prior work has conflated: quality estimation (ranking instances by expected performance) and sample selection (choosing the best output among $N$ candidates).
5	Our experiments on SciERC, CoNLL-2003, and WNUT-17 with Qwen3-8B and LLaMA-3.1-8B reveal that these objectives require fundamentally different signal properties.
6	
7	Three findings anchor our analysis.
8	First, consistency-based signals are effective quality estimators: entity voting achieves the strongest rank correlation ($\rho{=}0.38$) while exact match leads binary discrimination (AUROC${=}0.75$) on SciERC NER, with signal rankings depending on both task complexity and evaluation metric.
9	Second, the \textit{correlation-selection gap} shows that strong instance-level correlation does not yield substantial selection gains---no signal reliably surpasses greedy on either task (NER logprob: +0.6~pp, $p{=}0.39$; RE: $-$0.9~pp) despite 13--18~pp of oracle headroom---because instance-level signals cannot discriminate among candidates with similar consistency profiles.
10	Third, signal rankings depend on task difficulty: exact match leads on easy tasks, Soft Jaccard and voting lead on hard tasks, and all signals converge when model capability is insufficient, establishing practical guidance for signal choice.
11	
12	Several directions remain open.
13	Trained verifiers or reward models could close the selection gap by learning per-sample quality discrimination that unsupervised consistency signals lack.
14	Cross-task transfer of confidence signals beyond IE---to structured prediction tasks such as semantic parsing and code generation---would test the generality
…[truncated 321 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 100 · 2026-05-15T01:51:09.545501+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 101 · 2026-05-15T01:51:09.997546+00:00_

1	Our evaluation covers three datasets but only one RE benchmark (SciERC), where 44\% of instances receive zero F1, compressing the discriminable range and limiting signal differentiation for relation extraction.
2	WNUT-17 confirms the capability boundary of our approach, but our positive results on formal-domain text (CoNLL, SciERC) have not been validated on informal or noisy text where models achieve non-trivial performance.
3	
4	We evaluate two model families (Qwen3-8B and LLaMA-3.1-8B), both at 8B parameters.
5	Whether our findings---particularly the correlation-selection gap and the structural-over-surface signal ordering---hold for larger models (70B+) or closed-source APIs remains untested.
6	Larger models may produce higher-quality and more diverse samples, potentially altering the signal landscape.
7	
8	Our analysis of selection potential uses unsupervised signals and a logistic regression proxy as an upper bound.
9	We do not train a dedicated verifier or reward model, leaving unknown how much of the oracle headroom a supervised approach could recover.
10	
11	We evaluate at $N{=}8$ and $N{=}16$.
12	The behavior of confidence signals at larger sample sizes (e.g., $N{=}64$ or $N{=}128$) is unknown, and $N$-scaling gains are setting-dependent: SJ improves by $+0.052$ on Qwen SciERC NER but only $+0.016$ on LLaMA SciERC NER when doubling from $N{=}8$ to $N{=}16$.
13	
14	On CoNLL with LLaMA, the SJ--FK gap is only 0.003 ($\rho{=}0.431$ vs.\ $0.428$), so the structural advantage over surface signals may not generalize to all simple-schema datasets.
15	Finally, log-probability was excluded from the temperature comparison ($T{=}0.7$ vs.\ $T{=}1.0$) due to missing $T{=}0.7$ logprob data, leaving its temperature sensitivity uncharacterized.
16	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 102 · 2026-05-15T01:51:09.997977+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 103 · 2026-05-15T01:51:11.002263+00:00_

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
21	$c_{\text{vote}}$ & Entity voting confidence \\
22	$c_{\text{lp}}$ & Log-probability (mean token log-likelihood) \\
23	\bottomrule
24	\end{tabular}
25	\caption{Notation used throughout the paper.}
26	\label{tab:notation}
27	\end{table}
28	
29	\section{Robustness Analysis}\label{app:robustness}
30	
31	\begin{table}[t]
32	\centering
33	\small
34	\caption{Signal robustness across configurations (Spearman $\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: cross-model transfer (LLaMA CoNLL $N{=}16$, 3-seed mean $\pm\sigma$). $^\dagger$Mean over 3 seeds ($\sigma{=}0.025$; individual: 0.428, 0.424, 0.384).}
35	\label{tab:robustness}
36	\begin{tabular}{llcc}
37	\toprule
38	& & NER $\rho$ & RE $\rho$ \\
39	\midrule
40	\multicolumn{4}{l}{\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\
41	\quad SJ & $T{=}0.7$ & 0.388 & 0.234 \\
42	\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\
43	\quad FK & $T{=}0.7$ & 0.321 & 0.184 \\
44	\quad FK & $T{=}1.0$ & 0.267 & 0.275 \\
45	\midrule
46	\multicolumn{4}{l}{\textit{Sample size} (Qwen SciERC, $T{=}1.0$)} \\
47	\quad SJ & $N{=}8$  & 0.360 & 0.250 \\
48	\quad SJ & $N{=}16$ & 0.412$^\dagger$ & 0.281 \\
49	\quad FK & $N{=}8$  & 0.267 & 0.275 \\
50	\quad FK & $N{=}16$ & 0.280 & 0.279 \\
51	\midrule
52	\multicolumn{4}{l}{\textit{Cross-model} (LLaMA CoNLL, $N{=}16$, 3 seeds)} \\
53	\quad SJ &  & $0.463{\pm}0.007$ & --- \\
54	\quad FK &  & $0.455{\pm}0.006$ & --- \\
55	\quad EM &  & $0.460{\pm
…[truncated 9406 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1004
}
```

</details>

---


### Tool call

_source line 104 · 2026-05-15T01:51:11.002776+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 105 · 2026-05-15T01:51:11.454772+00:00_

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
15	\usepackage{multirow}
16	\usepackage{xcolor}
17	\usepackage{subcaption}
18	
19	\graphicspath{{figures/}}
20	
21	\title{Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence Signals for Test-Time Scaling in Information Extraction}
22	
23	\author{Anonymous}
24	
25	\begin{document}
26	\maketitle
27	
28	\input{sections/abstract}
29	\input{sections/introduction}
30	\input{sections/related_work}
31	\input{sections/method}
32	\input{sections/experiments}
33	\input{sections/discussion}
34	\input{sections/conclusion}
35	
36	\section*{Limitations}
37	\input{sections/limitations}
38	
39	\bibliography{references}
40	
41	\appendix
42	\input{sections/appendix}
43	
44	\end{document}
45	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 106 · 2026-05-15T01:51:11.455311+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review reviewer guidelines review form criteria 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review reviewer guidelines review form criteria 2025 2026"
  }
}
```

</details>

---


### Tool call

_source line 107 · 2026-05-15T01:51:12.409580+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "self-consistency structured prediction 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "self-consistency structured prediction 2025 2026"
  }
}
```

</details>

---


### Tool call

_source line 108 · 2026-05-15T01:51:12.863322+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "confidence estimation information extraction LLM 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "confidence estimation information extraction LLM 2025 2026"
  }
}
```

</details>

---


### Tool call

_source line 109 · 2026-05-15T01:51:13.114726+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "test-time scaling NER relation extraction 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "test-time scaling NER relation extraction 2025 2026"
  }
}
```

</details>

---


### Tool result

_source line 110 · 2026-05-15T01:51:19.690466+00:00_

Web search results for query: "ACL Rolling Review reviewer guidelines review form criteria 2025 2026"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"ACLRollingReview (@ReviewAcl) / Posts / X","url":"https://x.com/ReviewAcl"},{"title":"aclrollingreview/reviewerguidelines.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewerguidelines.md"}]

Based on the search results, here's information about ACL Rolling Review (ARR) reviewer guidelines, review form criteria, and recent updates for 2025-2026:

## Reviewer Scoring Criteria (February 2025 onwards)

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation. The soundness scores must be justif
…[truncated 1932 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8235
}
```

</details>

---


### Tool result

_source line 111 · 2026-05-15T01:51:21.348106+00:00_

Web search results for query: "test-time scaling NER relation extraction 2025 2026"

Links: [{"title":"Benchmarking LLM-based Information Extraction Tools for Medical Documents | medRxiv","url":"https://www.medrxiv.org/content/10.64898/2026.01.19.26344287v1.full"},{"title":"The construction and refined extraction techniques of knowledge graph based on large language models | Scientific Reports","url":"https://www.nature.com/articles/s41598-026-38066-w"},{"title":"Advancing clinical information extraction with LLM-Augmenter | Truveta","url":"https://www.truveta.com/blog/research/advancing-clinical-information-extraction-with-llm-augmenter/"},{"title":"Test-time Scaling for Computer Vision - CVPR 2026","url":"https://cvpr.thecvf.com/virtual/2025/workshop/32352"},{"title":"Evaluating Test-Time Scaling LLMs for Legal Reasoning","url":"https://aclanthology.org/2025.findings-emnlp.742.pdf"},{"title":"Large language model augmented joint learning framework for entity-relation extraction - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S1568494625014073"},{"title":"Entity relationship extraction method based on dependency parsing and graph neural networks | Scientific Reports","url":"https://www.nature.com/articles/s41598-025-33922-7"},{"title":"1 Introduction","url":"https://arxiv.org/html/2605.10716"},{"title":"JMIR Formative Research - Ontology-Based Medication Named Entity Recognition Using Pretrained Transformer Models From a Thai Hospital: Model Fine-Tuning and Validation Study","url":"https://formative.jmir.org/2026/1/e82685"},{"title":"Clinical named entity recognition and relation extraction using natural language processing of medical free text: A systematic review | Request PDF","url":"https://www.researchgate.net/publication/371334097_Clinical_named_entity_recognition_and_relation_extraction_using_natural_language_processing_of_medical_free_text_A_systematic_review"}]

Based on the search results, here's what I found regarding test-t
…[truncated 1694 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8233
}
```

</details>

---


### Tool result

_source line 112 · 2026-05-15T01:51:22.252601+00:00_

Web search results for query: "confidence estimation information extraction LLM 2025 2026"

Links: [{"title":"Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs | OpenReview","url":"https://openreview.net/forum?id=gjeQKFxFpZ"},{"title":"can llms express their uncertainty? an empirical evaluation ...","url":"https://arxiv.org/pdf/2306.13063"},{"title":"GitHub - MiaoXiong2320/llm-uncertainty: code repo for ICLR 2024 paper \"Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs\" · GitHub","url":"https://github.com/MiaoXiong2320/llm-uncertainty"},{"title":"Large Language Model Confidence Estimation via Black-Box Access | OpenReview","url":"https://openreview.net/forum?id=lJcSDsGgYH"},{"title":"Frontiers | An overview of model uncertainty and variability in LLM-based sentiment analysis: challenges, mitigation strategies, and the role of explainability","url":"https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2025.1609097/full"},{"title":"[2306.13063] Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs","url":"https://arxiv.org/abs/2306.13063"},{"title":"Alkymi's Data Science Room - Building confidence in LLM outputs","url":"https://www.alkymi.io/data-science-room/building-confidence-in-llm-outputs"},{"title":"JMIR Medical Informatics - Benchmarking the Confidence of Large Language Models in Answering Clinical Questions: Cross-Sectional Evaluation Study","url":"https://medinform.jmir.org/2025/1/e66917"},{"title":"Mind the Generation Process: Fine-Grained Confidence Estimation During LLM Generation","url":"https://arxiv.org/html/2508.12040v1"},{"title":"Confidence Signals: the LLM alternative to confidence scores | Sensible Blog","url":"https://www.sensible.so/blog/confidence-signals"}]

Based on the search results, here are the key findings on confidence estimation for information extraction in LLMs in 2025-2026:

#
…[truncated 2193 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 9389
}
```

</details>

---


### Tool result

_source line 113 · 2026-05-15T01:51:27.125179+00:00_

Web search results for query: "self-consistency structured prediction 2025 2026"

Links: [{"title":"Self-Consistency Improves Chain of Thought Reasoning in Language Models | OpenReview","url":"https://openreview.net/forum?id=1PL1NIMMrw"},{"title":"Mind the Gap: Structure-Aware Consistency in Preference Learning","url":"https://arxiv.org/pdf/2604.27733"},{"title":"Difficulty-Adaptive Self-Consistency for Cost-Efficient ...","url":"https://aclanthology.org/2025.findings-naacl.383.pdf"},{"title":"[2511.12309] Optimal Self-Consistency for Efficient Reasoning with Large Language Models","url":"https://arxiv.org/abs/2511.12309"},{"title":"[PDF] Self-Consistency Improves Chain of Thought Reasoning in Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Self-Consistency-Improves-Chain-of-Thought-in-Wang-Wei/5f19ae1135a9500940978104ec15a5b8751bc7d2"},{"title":"[2203.11171] Self-Consistency Improves Chain of Thought Reasoning in Language Models","url":"https://arxiv.org/abs/2203.11171"},{"title":"(PDF) Self-Consistency Improves Chain of Thought Reasoning in Language Models","url":"https://www.researchgate.net/publication/359390115_Self-Consistency_Improves_Chain_of_Thought_Reasoning_in_Language_Models"},{"title":"Confidence Improves Self-Consistency in LLMs","url":"https://aclanthology.org/2025.findings-acl.1030.pdf"},{"title":"Frontiers in Psychology 01 frontiersin.org Self-consistency and congruence,","url":"https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2025.1588734/pdf"},{"title":"Feature 14 IEEE CIRCUITS AND SYSTEMS MAGAZINE FOURTH QUARTER 2025","url":"https://mn.cs.tsinghua.edu.cn/xinwang/PDF/papers/2025_Embodied%20AI%20from%20LLMs%20to%20World%20Models.pdf"}]

Based on the search results, here's what I found about self-consistency and structured prediction from 2025-2026:

## Self-Consistency Research (2025-2026)

Recent work introduces Blend-ASC, a novel variant of self-consistency that dynamically allocates samples 
…[truncated 1425 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 14715
}
```

</details>

---


### Tool call

_source line 114 · 2026-05-15T01:51:39.378429+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form: all scoring dimensions (soundness, excitement, overall, etc.), their scales (1-5? 1-6?), and descriptions of each score level. Also extract any specific criteria reviewers should evaluate."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form: all scoring dimensions (soundness, excitement, overall, etc.), their scales (1-5? 1-6?), and descriptions of each score level. Also extract any specific criteria reviewers should evaluate."
  }
}
```

</details>

---


### Tool call

_source line 115 · 2026-05-15T01:51:41.487696+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool call

_source line 116 · 2026-05-15T01:51:42.543986+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Nedellec 2026 consistency LLM information extraction NER"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Nedellec 2026 consistency LLM information extraction NER"
  }
}
```

</details>

---


### Tool call

_source line 117 · 2026-05-15T01:51:42.745272+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"conformal prediction\" NLP structured prediction NER 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"conformal prediction\" NLP structured prediction NER 2025 2026"
  }
}
```

</details>

---


### Tool call

_source line 118 · 2026-05-15T01:51:43.197521+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Kim 2026 ReASC adaptive sampling self-consistency"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Kim 2026 ReASC adaptive sampling self-consistency"
  }
}
```

</details>

---


### Tool result

_source line 119 · 2026-05-15T01:51:45.865540+00:00_

# ACL Rolling Review Form - Scoring Dimensions

## Reviewer Confidence (1-5 scale)
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: High confidence with unlikely but conceivable gaps
- **3**: Adequate understanding but possible oversights in details
- **2**: Capable defense despite likely missed elements or novelty uncertainties
- **1**: "Not my area, or paper is very hard to understand"

## Soundness (1-5 scale with .5 increments)
- **5**: "Excellent: This study is one of the most thorough I have seen"
- **4**: "Strong: This study provides sufficient support for all of its claims"
- **3**: "Acceptable: This study provides sufficient support for its main claims"
- **2**: "Poor: Some of the main claims are not sufficiently supported"
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication"

## Excitement (1-5 scale with .5 increments)
- **5**: "Highly Exciting: I would recommend this paper to others and/or attend its presentation"
- **4**: "Exciting: I would mention this paper to others and/or make an effort to attend"
- **3**: "Interesting: I might mention some points and/or attend if time permits"
- **2**: "Potentially Interesting: does not resonate with me, but might with others"
- **1**: "Not Exciting: does not resonate with me" or lacks relevance to computational linguistics

## Overall Assessment (1-5 scale with .5 increments)
- **5**: Consider for Award (top 2.5%)
- **4**: Conference acceptance recommended
- **3**: Findings track acceptance
- **2**: Resubmit next cycle with substantial revisions
- **1**: Do not resubmit or lacks relevance

## Additional Metrics
- **Reproducibility** (1-5): Information sufficiency for result replication
- **Datasets** (1-5): Usefulness and impact of released data
- **Software** (1-5): Utility and enabling potential of released code
- **Author Identity** (1-5): Anonymity status assessment

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 6487
}
```

</details>

---


### Tool result

_source line 120 · 2026-05-15T01:52:25.141520+00:00_

{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 46, \"total_citations\": 65, \"unique_cited_keys\": 46, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 43, \"online_not_found\": 2, \"online_mismatch\": 1}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"angelopoulos2021conformal\", \"type\": \"inproceedings\", \"title\": \"Uncertainty Sets for Image Classifiers using Conformal Prediction\", \"authors\": \"Angelopoulos, Anastasios N. and Bates, Stephen and Malik, Jitendra and Jordan, M...\", \"year\": \"2021\", \"venue\": \"ICLR 2021\"}, {\"key\": \"brown2024monkeys\", \"type\": \"article\", \"title\": \"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\", \"authors\": \"Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, ...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2407.21787\"}, {\"key\": \"chen2024usc\", \"type\": \"inproceedings\", \"title\": \"Universal Self-Consistency for Large Language Model Generation\", \"authors\": \"Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Y...\", \"year\": \"2024\", \"venue\": \"arXiv preprint (ICML 2024 Workshop ICL)\"}, {\"key\": \"cobbe2021verifiers\", \"type\": \"article\", \"title\": \"Training Verifiers to Solve Math Word Problems\", \"authors\": \"Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, ...\", \"year\": \"2021\", \"venue\": \"arXiv preprint arXiv:2110.14168\"}, {\"key\": \"culotta2004confidence\", \"type\": \"inproceedings\", \"title\": \"Confidence Estimation for Information Extraction\", \"authors\": \"Culotta, Aron and McCallum, Andrew\", \"year\": \"2004\", \"venue\": \"HLT-NAACL 2004\"}, {\"key\": \"derczynski2017wnut\", \"type\": \"inproceedings\", \"title\": \"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recogniti
…[truncated 35625 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 43653
}
```

</details>

---


### Tool result

_source line 121 · 2026-05-15T01:52:32.572566+00:00_

Web search results for query: ""conformal prediction" NLP structured prediction NER 2025 2026"

Links: [{"title":"Conformal Prediction: A Data Perspective | ACM Computing Surveys","url":"https://dl.acm.org/doi/10.1145/3736575"},{"title":"Conformal Structured Prediction | OpenReview","url":"https://openreview.net/forum?id=mKfmLQXP6J"},{"title":"Conformal Prediction for Natural Language Processing: A Survey | Transactions of the Association for Computational Linguistics | MIT Press","url":"https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00715/125278/Conformal-Prediction-for-Natural-Language"},{"title":"Published as a conference paper at ICLR 2025 CONFORMAL STRUCTURED PREDICTION","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/1868a3c73d0d2a44c42458575fa8514c-Paper-Conference.pdf"},{"title":"[2601.16999] Uncertainty Quantification for Named Entity Recognition via Full-Sequence and Subsequence Conformal Prediction","url":"https://arxiv.org/abs/2601.16999"},{"title":"Conformal Prediction for Natural Language Processing: A Survey","url":"https://arxiv.org/html/2405.01976"},{"title":"[2405.01976] Conformal Prediction for Natural Language Processing: A Survey","url":"https://arxiv.org/abs/2405.01976"},{"title":"ICML Poster Volume Optimality in Conformal Prediction with Structured Prediction Sets","url":"https://icml.cc/virtual/2025/poster/44066"},{"title":"Adaptive Conformal Prediction for Improving Factuality of Generations by Large Language Models","url":"https://arxiv.org/html/2604.13991"},{"title":"Conformal Prediction for Natural Language Processing: A Survey - ACL Anthology","url":"https://aclanthology.org/2024.tacl-1.82/"}]

Here are the search results for your query on conformal prediction, NLP, structured prediction, and NER:

## Key Recent Research

**Recent Surveys and Frameworks:**

The rapid proliferation of large language models and NLP applications creates a crucial need for uncertainty quantification to mitigate risks such as hallucinat
…[truncated 1881 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 49827
}
```

</details>

---


### Tool result

_source line 122 · 2026-05-15T01:52:32.623680+00:00_

Web search results for query: "Nedellec 2026 consistency LLM information extraction NER"

Links: [{"title":"Benchmarking LLM-based Information Extraction Tools for ...","url":"https://www.medrxiv.org/content/10.64898/2026.01.19.26344287v1.full.pdf"},{"title":"Benchmarking LLM-based Information Extraction Tools for Medical Documents | medRxiv","url":"https://www.medrxiv.org/content/10.64898/2026.01.19.26344287v1.full"},{"title":"GitHub - quqxui/Awesome-LLM4IE-Papers: Awesome papers about generative Information Extraction (IE) using Large Language Models (LLMs) · GitHub","url":"https://github.com/quqxui/Awesome-LLM4IE-Papers"},{"title":"Large language models for generative information extraction: a survey | Frontiers of Computer Science | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11704-024-40555-y"},{"title":"Advancing clinical information extraction with LLM-Augmenter | Truveta","url":"https://www.truveta.com/blog/research/advancing-clinical-information-extraction-with-llm-augmenter/"},{"title":"GitHub - lbnlp/NERRE: Code and data for the publication \"Structured information extraction from scientific text with large language models\" by Dagdelen & Dunn et al. · GitHub","url":"https://github.com/lbnlp/NERRE"},{"title":"LLM-based AI agents for automated extraction of material properties and structural features - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0927025626000406"},{"title":"Structured information extraction from scientific text with large language models | Nature Communications","url":"https://www.nature.com/articles/s41467-024-45563-x"},{"title":"Analysing Lightweight Large Language Models for Biomedical Named Entity Recognition on Diverse Ouput Formats","url":"https://arxiv.org/html/2604.25920"},{"title":"Universal NER","url":"https://universal-ner.github.io/"}]

Based on the search results, I found relevant information about your query. Here's what the research reveals:

## Search Results Over
…[truncated 1677 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 50079
}
```

</details>

---


### Tool result

_source line 123 · 2026-05-15T01:52:33.226946+00:00_

Web search results for query: "Kim 2026 ReASC adaptive sampling self-consistency"

Links: [{"title":"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning","url":"https://arxiv.org/html/2601.02970"},{"title":"ReASC: Reliability-Aware Adaptive Self-Consistency","url":"https://www.emergentmind.com/topics/reliability-aware-adaptive-self-consistency-reasc"},{"title":"[2601.02970] Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning","url":"https://arxiv.org/abs/2601.02970"},{"title":"Self-Consistency Sampling in LLMs","url":"https://www.emergentmind.com/topics/self-consistency-sampling"},{"title":"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM","url":"https://arxiv.org/pdf/2601.02970"},{"title":"GitHub - fscdc/Awesome-Efficient-Reasoning-Models: [TMLR 2025] Efficient Reasoning Models: A Survey · GitHub","url":"https://github.com/fscdc/Awesome-Efficient-Reasoning-Models"},{"title":"Self-Consistency Improves Chain of Thought Reasoning in Language Models | OpenReview","url":"https://openreview.net/forum?id=1PL1NIMMrw"},{"title":"Difficulty-Adaptive Self-Consistency for Cost-Efficient ...","url":"https://aclanthology.org/2025.findings-naacl.383.pdf"},{"title":"[2305.11860] Let's Sample Step by Step: Adaptive-Consistency for Efficient Reasoning and Coding with LLMs","url":"https://arxiv.org/abs/2305.11860"},{"title":"(PDF) Self-Consistency Improves Chain of Thought Reasoning in Language Models","url":"https://www.researchgate.net/publication/359390115_Self-Consistency_Improves_Chain_of_Thought_Reasoning_in_Language_Models"}]

Based on the search results, here's what I found about Kim 2026 ReASC adaptive sampling self-consistency:

## Overview

ReASC (Reliability-Aware Adaptive Self-Consistency) addresses limitations in adaptive sampling by reframing it from response counting to evidence sufficiency, leveraging response-level confidence for principled information aggregation.

## How It Wo
…[truncated 1203 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 50029
}
```

</details>

---


### Tool call

_source line 124 · 2026-05-15T01:52:37.896682+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"best-of-N\" selection structured output LLM 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"best-of-N\" selection structured output LLM 2025 2026"
  }
}
```

</details>

---


### Tool call

_source line 125 · 2026-05-15T01:52:38.499352+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "generative NER LLM self-consistency voting aggregation 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "generative NER LLM self-consistency voting aggregation 2025 2026"
  }
}
```

</details>

---


### Tool call

_source line 126 · 2026-05-15T01:52:39.302869+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Vashurin 2025 CoCoA confidence consistency uncertainty quantification LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Vashurin 2025 CoCoA confidence consistency uncertainty quantification LLM"
  }
}
```

</details>

---


### Tool result

_source line 127 · 2026-05-15T01:52:45.430778+00:00_

Web search results for query: ""best-of-N" selection structured output LLM 2025 2026"

Links: [{"title":"LLM Benchmarks 2026: 30+ Models Ranked — MMLU, SWE-bench, Arena Elo & Pricing","url":"https://iternal.ai/llm-selection-guide"},{"title":"LLM Leaderboard 2026: Best AI Models Benchmark & Ranking","url":"https://www.clickrank.ai/llm-leaderboard/"},{"title":"LLM Leaderboard 2026: Compare 300+ Top AI Models by Intelligence, Speed & Price","url":"https://llm-stats.com/"},{"title":"GraphInstruct: A Progressive Benchmark for Diagnosing Capability Gaps in LLM Graph Generation","url":"https://arxiv.org/html/2605.09997v1"},{"title":"StructEval: Benchmarking LLMs’ Capabilities to Generate Structural Outputs","url":"https://arxiv.org/html/2505.20139v1"},{"title":"LLM Structured Outputs: The Practical Guide for Every Provider [2026]","url":"https://techsy.io/en/blog/llm-structured-outputs-guide"},{"title":"LLM Leaderboard 2026 — Compare Top AI Models - Vellum","url":"https://www.vellum.ai/llm-leaderboard"},{"title":"Open LLM Leaderboard 2026 - Compare Open Source LLM Rankings","url":"https://llm-stats.com/leaderboards/open-llm-leaderboard"},{"title":"How to Choose an LLM in 2026: Which AI Model Is Best for Your Use Case | BenchLM.ai","url":"https://benchlm.ai/blog/posts/which-llm-to-use"},{"title":"Speculative Decoding: 2-3x Faster LLM Inference (2026)","url":"https://blog.premai.io/speculative-decoding-2-3x-faster-llm-inference-2026/"}]

Based on the search results, I found relevant information about structured output for LLMs in 2025-2026, though the specific "best-of-N" selection technique wasn't directly addressed. Here's what I found:

## Structured Output LLM Landscape (2025-2026)

OpenAI (since August 2024), Google Gemini (2024, expanded 2026), Anthropic (beta November 2025, GA early 2026), Cohere, and xAI (Grok) all support native structured output.

Structured output is a mechanism that guarantees an LLM's response conforms to a predefined JSON Schema. Unlike plain t
…[truncated 1103 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7534
}
```

</details>

---


### Tool result

_source line 128 · 2026-05-15T01:52:46.894561+00:00_

Web search results for query: "Vashurin 2025 CoCoA confidence consistency uncertainty quantification LLM"

Links: [{"title":"[2502.04964] Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency","url":"https://arxiv.org/abs/2502.04964"},{"title":"GitHub - stat-ml/llm_uncertainty_cocoa · GitHub","url":"https://github.com/stat-ml/llm_uncertainty_cocoa"},{"title":"CoCoA: A Minimum Bayes Risk Framework Bridging Confidence and Consistency for Uncertainty Quantification in LLMs | OpenReview","url":"https://openreview.net/forum?id=H1NGlLNaVC"},{"title":"Systematic Evaluation of Uncertainty Estimation Methods in Large Language Models","url":"https://arxiv.org/html/2510.20460v1"},{"title":"CoCoA: A Generalized Approach to Uncertainty Quantification by Integrating Confidence and Consistency of LLM Outputs","url":"https://arxiv.org/html/2502.04964v1"},{"title":"[Literature Review] CoCoA: A Generalized Approach to Uncertainty Quantification by Integrating Confidence and Consistency of LLM Outputs","url":"https://www.themoonlight.io/en/review/cocoa-a-generalized-approach-to-uncertainty-quantification-by-integrating-confidence-and-consistency-of-llm-outputs"},{"title":"CoCoA: A Minimum Bayes Risk Framework Bridging Confidence and Consistency for Uncertainty Quantification in LLMs","url":"https://arxiv.org/html/2502.04964"},{"title":"CoCoA: A Generalized Approach to Uncertainty Quantification","url":"https://arxiv.org/pdf/2502.04964v2"},{"title":"[2502.04964v3] Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency","url":"https://arxiv.org/abs/2502.04964v3"},{"title":"Uncertainty Quantification for LLMs through Minimum Bayes Risk: Bridging Confidence and Consistency","url":"https://arxiv.org/html/2502.04964v3"}]

Based on the search results, I found comprehensive information about the Vashurin 2025 CoCoA research:

## CoCoA: A Minimum Bayes Risk Framework for Uncertainty Quantification in LLM
…[truncated 1875 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7591
}
```

</details>

---


### Tool result

_source line 129 · 2026-05-15T01:52:48.300506+00:00_

Web search results for query: "generative NER LLM self-consistency voting aggregation 2025 2026"

Links: [{"title":"Generative AI voting: fair collective choice is resilient to LLM biases and inconsistencies - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12963128/"},{"title":"Ranked Voting based Self-Consistency of Large Language ...","url":"https://aclanthology.org/2025.findings-acl.744.pdf"},{"title":"Self-Consistency Sampling in LLMs","url":"https://www.emergentmind.com/topics/self-consistency-sampling"},{"title":"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning","url":"https://arxiv.org/html/2601.02970v1"},{"title":"Generative AI Voting: Fair Collective Choice is Resilient to LLM Biases and Inconsistencies","url":"https://arxiv.org/html/2406.11871v1"},{"title":"Generative AI voting: fair collective choice is resilient to LLM biases and inconsistencies | EPJ Data Science | Springer Nature Link","url":"https://link.springer.com/article/10.1140/epjds/s13688-025-00612-3"},{"title":"The Majority is not always right: RL training for solution aggregation","url":"https://arxiv.org/pdf/2509.06870"},{"title":"[2503.04104] LLMs Can Generate a Better Answer by Aggregating Their Own Responses","url":"https://arxiv.org/abs/2503.04104"},{"title":"[2505.10772] Ranked Voting based Self-Consistency of Large Language Models","url":"https://arxiv.org/abs/2505.10772"},{"title":"[2406.11871] Generative AI voting: fair collective choice is resilient to LLM biases and inconsistencies","url":"https://arxiv.org/abs/2406.11871"}]

Based on the search results, I found several relevant recent works combining generative AI, self-consistency, and voting/aggregation methods in 2025-2026:

## Key Recent Papers

### 1. **Ranked Voting based Self-Consistency**
A 2025 work proposes generating ranked answers in reasoning processes and conducting ranked voting among multiple ranked answers, using Instant-runoff voting, Borda count voting, and mean reciproca
…[truncated 1941 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 9801
}
```

</details>

---


### Tool call

_source line 130 · 2026-05-15T01:52:57.787644+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2601.16999 conformal prediction named entity recognition uncertainty quantification"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2601.16999 conformal prediction named entity recognition uncertainty quantification"
  }
}
```

</details>

---


### Tool call

_source line 131 · 2026-05-15T01:52:58.641261+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Optimal Self-Consistency\" 2025 arxiv efficient reasoning LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Optimal Self-Consistency\" 2025 arxiv efficient reasoning LLM"
  }
}
```

</details>

---


### Tool result

_source line 132 · 2026-05-15T01:53:06.319528+00:00_

Web search results for query: ""Optimal Self-Consistency" 2025 arxiv efficient reasoning LLM"

Links: [{"title":"[2511.12309] Optimal Self-Consistency for Efficient Reasoning with Large Language Models","url":"https://arxiv.org/abs/2511.12309"},{"title":"Optimal Self-Consistency for Efficient Reasoning with Large Language Models","url":"https://arxiv.org/pdf/2511.12309"},{"title":"[2408.17017v3] Reasoning Aware Self-Consistency: Leveraging Reasoning Paths for Efficient LLM Sampling","url":"https://arxiv.org/abs/2408.17017v3"},{"title":"[2408.17017] Reasoning Aware Self-Consistency: Leveraging Reasoning Paths for Efficient LLM Sampling","url":"https://arxiv.org/abs/2408.17017"},{"title":"[2601.02970] Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning","url":"https://arxiv.org/abs/2601.02970"},{"title":"Confidence Improves Self-Consistency in LLMs","url":"https://arxiv.org/pdf/2502.06233"},{"title":"[2502.06233] Confidence Improves Self-Consistency in LLMs","url":"https://arxiv.org/abs/2502.06233"},{"title":"[2604.26954] The Impact of LLM Self-Consistency and Reasoning Effort on Automated Scoring Accuracy and Cost","url":"https://arxiv.org/abs/2604.26954"},{"title":"[2203.11171] Self-Consistency Improves Chain of Thought Reasoning in Language Models","url":"https://arxiv.org/abs/2203.11171"},{"title":"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning","url":"https://arxiv.org/html/2601.02970v1"}]

I found relevant search results for your query. Here are the key findings:

## Main Result: "Optimal Self-Consistency for Efficient Reasoning with Large Language Models"

The primary paper is titled "Optimal Self-Consistency for Efficient Reasoning with Large Language Models", available on arXiv as paper 2511.12309 (submitted November 15, 2025).

### What is Self-Consistency?

Self-consistency involves generating multiple responses, or samples from a large language model (LLM) and selecting the most frequent 
…[truncated 1162 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7678
}
```

</details>

---


### Tool result

_source line 133 · 2026-05-15T01:53:09.030298+00:00_

Web search results for query: "arxiv 2601.16999 conformal prediction named entity recognition uncertainty quantification"

Links: [{"title":"[2601.16999] Uncertainty Quantification for Named Entity Recognition via Full-Sequence and Subsequence Conformal Prediction","url":"https://arxiv.org/abs/2601.16999"},{"title":"Uncertainty Quantification for Named Entity Recognition via Full-Sequence and Subsequence Conformal Prediction","url":"https://arxiv.org/html/2601.16999"},{"title":"Class Adaptive Conformal Training","url":"https://arxiv.org/html/2601.09522"},{"title":"[2605.07549] Probabilistic Object Detection with Conformal Prediction","url":"https://arxiv.org/abs/2605.07549"},{"title":"[2107.07511] A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification","url":"https://arxiv.org/abs/2107.07511"},{"title":"Uncertainty-Aware Transformers: Conformal Prediction for Language Models","url":"https://arxiv.org/html/2604.08885"},{"title":"Geometry-Aware Uncertainty Quantification via Conformal Prediction on Manifolds","url":"https://arxiv.org/html/2602.16015"},{"title":"Conformal Prediction for Natural Language Processing: A Survey","url":"https://arxiv.org/html/2405.01976v1"},{"title":"[2604.08885] Uncertainty-Aware Transformers: Conformal Prediction for Language Models","url":"https://arxiv.org/abs/2604.08885"},{"title":"A Conformal Prediction Framework for Uncertainty Quantification in Physics-Informed Neural Networks","url":"https://arxiv.org/html/2509.13717"}]

Based on the search results, I found the paper you're looking for:

**arXiv:2601.16999** titled "Uncertainty Quantification for Named Entity Recognition via Full-Sequence and Subsequence Conformal Prediction" by Matthew Singer, Srijan Sengupta, and Karl Pazdernik, submitted on January 13, 2026.

## Summary

The paper addresses the fact that current NER models typically output a single predicted label sequence without any accompanying measure of uncertainty, leaving downstream
…[truncated 1001 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 11242
}
```

</details>

---


### Tool call

_source line 134 · 2026-05-15T01:55:40.991495+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 — Round 1 审稿完成\n\n### 总体评分\n**Overall**: 3.0/5（Findings track acceptance）\n**Soundness**: 3.5/5 | **Excitement**: 2.5/5 | **Reproducibility**: 4.0/5\n**Confidence**: 4/5\n\n### 核心判断\n论文选择了有价值的研究问题，实验设计合理、统计检验到位。但作为 EMNLP 主会长文有三个核心不足：\n\n### Must-Fix 问题 (3 个)\n\n**N1** [critical] \"Correlation-selection gap\" 的解释力不足——4/5 个 signals 是 instance-level 的，它们不能做 per-sample selection 是定义上的必然结果，不是发现。真正需要深入分析的是唯一的 per-sample signal (logprob) 为何也失败（calibration? length bias? constrained decoding 干扰?），但论文对此几乎没有分析。\n\n**N2** [critical] Per-sample signal 探索严重不足——5 个 signals 中只有 logprob 1 个能做 per-sample selection，论文却声称 \"systematic comparison\"。LOO-SJ 已在 Appendix D 计算（Δρ=-0.014），但未测试其 selection 能力——这是一个自然的 per-sample structural signal。Consensus-proximity ranking 也未被分析。\n\n**N3** [critical] 对 Nedellec et al. (2026) 的增量贡献论证不足。三个区分点中：selection 结论是负面的、multi-domain 是标准做法、SJ 的优势不一致（CoNLL 上 EM > SJ，conditional filtering 后 EM > SJ）。\n\n### Should-Fix 问题 (5 个)\n- W1: \"first systematic evaluation\" claim 过强，需收窄 scope\n- W2: 遗漏 Singer et al. (2026) conformal prediction for NER（arXiv:2601.16999）和 ICLR 2025 conformal structured prediction\n- W3: 遗漏 \"Optimal Self-Consistency\" (arXiv:2511.12309) 和 \"Difficulty-Adaptive SC\" (NAACL 2025 Findings)\n- W4: 实验规模偏小（仅 8B 模型、1 个 RE benchmark、LoRA fine-tuned 非典型 generative IE 设置）\n- W5: ρ-AUROC dissociation 机制分析浅，主文应明确 EM=1 同时包含 all-correct 和 all-wrong 的压缩效应\n\n### 引用真实性\n46 篇中 43 篇验证通过。`nedellec2026consistency` 第一作者应为 Yao 而非 Nédellec，论文中 \"Nedellec et al.\" 引用有误。`lightman2024verify` 和 `hobelsberger2025systematic` 未匹配但属 API 问题，实质上是真实论文。\n\n### 遗漏重要引用\n1. Singer et al. (2026) \"UQ for NER via Conformal Prediction\"\n2. Conformal Structured Prediction (ICLR 2025)\n3. Optimal Self-Consistency (arXiv:2511.12309)\n4. Difficulty-Adaptive Self-Consistency (NAACL 2025 Findings)\n5. Generative Self-Aggregation (arXiv:2503.04104)\n\n### 审稿判断\n当前版本更适合 Findings track。如能深入分析 per-sample signal failure 原因、测试 LOO-SJ 等 per-sample structural signals、讨论 constrained decoding 影响，可提升至主会水准。",
  "reviewer_id": "2",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 — Round 1 审稿完成\n\n### 总体评分\n**Overall**: 3.0/5（Findings track acceptance）\n**Soundness**: 3.5/5 | **Excitement**: 2.5/5 | **Reproducibility**: 4.0/5\n**Confidence**: 4/5\n\n### 核心判断\n论文选择了有价值的研究问题，实验设计合理、统计检验到位。但作为 EMNLP 主会长文有三个核心不足：\n\n### Must-Fix 问题 (3 个)\n\n**N1** [critical] \"Correlation-selection gap\" 的解释力不足——4/5 个 signals 是 instance-level 的，它们不能做 per-sample selection 是定义上的必然结果，不是发现。真正需要深入分析的是唯一的 per-sample signal (logprob) 为何也失败（calibration? length bias? constrained decoding 干扰?），但论文对此几乎没有分析。\n\n**N2** [critical] Per-sample signal 探索严重不足——5 个 signals 中只有 logprob 1 个能做 per-sample selection，论文却声称 \"systematic comparison\"。LOO-SJ 已在 Appendix D 计算（Δρ=-0.014），但未测试其 selection 能力——这是一个自然的 per-sample structural signal。Consensus-proximity ranking 也未被分析。\n\n**N3** [critical] 对 Nedellec et al. (2026) 的增量贡献论证不足。三个区分点中：selection 结论是负面的、multi-domain 是标准做法、SJ 的优势不一致（CoNLL 上 EM > SJ，conditional filtering 后 EM > SJ）。\n\n### Should-Fix 问题 (5 个)\n- W1: \"first systematic evaluation\" claim 过强，需收窄 scope\n- W2: 遗漏 Singer et al. (2026) conformal prediction for NER（arXiv:2601.16999）和 ICLR 2025 conformal structured prediction\n- W3: 遗漏 \"Optimal Self-Consistency\" (arXiv:2511.12309) 和 \"Difficulty-Adaptive SC\" (NAACL 2025 Findings)\n- W4: 实验规模偏小（仅 8B 模型、1 个 RE benchmark、LoRA fine-tuned 非典型 generative IE 设置）\n- W5: ρ-AUROC dissociation 机制分析浅，主文应明确 EM=1 同时包含 all-correct 和 all-wrong 的压缩效应\n\n### 引用真实性\n46 篇中 43 篇验证通过。`nedellec2026consistency` 第一作者应为 Yao 而非 Nédellec，论文中 \"Nedellec et al.\" 引用有误。`lightman2024verify` 和 `hobelsberger2025systematic` 未匹配但属 API 问题，实质上是真实论文。\n\n### 遗漏重要引用\n1. Singer et al. (2026) \"UQ for NER via Conformal Prediction\"\n2. Conformal Structured Prediction (ICLR 2025)\n3. Optimal Self-Consistency (arXiv:2511.12309)\n4. Difficulty-Adaptive Self-Consistency (NAACL 2025 Findings)\n5. Generative Self-Aggregation (arXiv:2503.04104)\n\n### 审稿判断\n当前版本更适合 Findings track。如能深入分析 per-sample signal failure 原因、测试 LOO-SJ 等 per-sample structural signals、讨论 constrained decoding 影响，可提升至主会水准。",
    "reviewer_id": "2",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 135 · 2026-05-15T01:55:44.961059+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3969
}
```

</details>

---


### Assistant

_source line 136 · 2026-05-15T01:55:53.861514+00:00_

审稿意见已提交给 Review Director。

总结：Overall 3.0/5，建议 Findings track。三个 critical 问题：(1) correlation-selection gap 是定义推论而非发现，logprob failure 分析缺失；(2) per-sample signal 只测了 logprob 一个，LOO-SJ 未测 selection；(3) 与 Nedellec 2026 增量贡献论证不足。另有 5 个 should-fix（遗漏 conformal prediction for NER 等重要引用、"first" claim 过强、实验规模偏小等）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2"
}
```

</details>

---


## Round 4

## Round 4

52 recorded events


### User

_source line 137 · 2026-05-15T01:58:25.795069+00:00_

[Round 1 审稿请求]:
## 交叉分享：Reviewer 1 的完整 Round 1 审稿意见

请逐条回应 Reviewer 1 的每个问题：用 [AGREE] 表示同意并说明理由，或 [REBUT] 表示反驳并引用论文具体 Section/Table/Figure 作为证据。

---

以下是 Reviewer 1 的完整审稿原文：

### 总体评分
**Overall**: 3/5 — Findings
**Soundness**: 3.5/5 | **Excitement**: 3/5 | **Reproducibility**: 3.5/5
**Confidence**: 4/5

### Must-Fix 问题（影响接收决定）

**N1** [critical] Bootstrap 检验细节严重不足，核心统计结论无法验证

- 具体位置：Section 5.3, "p=0.39, 3-seed bootstrap; Cohen's d=0.038"
- 问题：论文的核心负面结论（"no signal reliably surpasses greedy"）完全建立在 p=0.39 这一 bootstrap 检验上，但以下关键细节未报告：(1) bootstrap 迭代次数；(2) 是 paired bootstrap 还是 unpaired；(3) 检验统计量是什么；(4) "3-seed bootstrap"的含义不明——是对 3 个 seed 做 bootstrap（n=3，完全无统计功效），还是在每个 seed 内对 instance 做 bootstrap 再合并？如果是前者，p=0.39 无任何诊断价值。
- 为什么影响接收：这是支撑全文标题（"Weak Selectors"）和主要贡献（contribution #2）的唯一定量证据。

**N2** [critical] 仅 8B 模型，"model-agnostic" claim 缺乏支撑

- 具体位置：Section 5.1, 5.4, Discussion 多处使用"model-agnostic"
- 问题：只测试了 Qwen3-8B 和 LLaMA-3.1-8B-Instruct——同一参数规模。70B+ 模型可能产生更高质量更多样的样本，从根本上改变 correlation-selection gap 的形态。Limitations 承认了这一点，但 Discussion 仍使用"model-agnostic"措辞，形成内部矛盾（ARR R4 overclaiming）。

**N3** [critical] RE 结论仅基于 SciERC，44% zero-F1 floor effect 严重扭曲信号评估

- 具体位置：Section 5.1, Limitations 第 1 段
- 问题：RE 的所有结论全部来自 SciERC RE 一个数据集，其中 44% 实例 F1=0。ρ 和 AUROC 在很大程度上反映二元区分而非细粒度质量预测。论文声称覆盖"NER and RE"但 RE 实验基础极其薄弱。

### Should-Fix 问题

**W1** [warning] Soft Jaccard 形式化有歧义：g_i/g_j 未定义，sim 具体公式缺失，Hungarian algorithm 匹配阈值未说明。

**W2** [warning] Entity voting 的 mean frequency 聚合方式未讨论替代选择（median、thresholded voting 等），当模型产生大量低频幻觉实体时 |E_∪| 膨胀导致置信度系统性偏低。

**W3** [warning] ρ=0.38 被反复描述为"effective/strong quality estimation"但仅解释 ~14% F1 方差，未与 uncertainty estimation 文献中其他方法的 ρ 对比 contextualize。

**W4** [warning] Logprob（唯一 per-sample signal、selection 最佳信号）的温度敏感性数据缺失（T=0.7 unavailable），但论文做出了"signals robust across temperatures"的笼统结论。

**W5** [warning] WNUT-17 p=0.106 被解读为"establishing the capability boundary where all signals break down"，措辞过于确定——fail to reject null ≠ accept null。

**W6** [warning] Qwen3-8B (LoRA r=32) vs LLaMA-3.1-8B-Instruct（未说明是否微调）训练设置不对称，可能混淆 cross-model 比较。

**W7** [warning] 约束解码对 sampling diversity 的影响未讨论——这可能是 correlation-selection gap 的一个成因。

### 小问题
- Table 2 EM "---" 需更显著的解释
- Limitations 提到"logistic regression proxy as an upper bound"但正文/Appendix 无此分析结果
- snell2024scaling bib 作者格式与 OpenAlex 有 mismatch
- Cross-model Δ=0.005 未报告是否在 bootstrap CI 内
- Introduction "+18pp on GSM8K" 未注明具体模型(PaLM-540B)
- Appendix D \textsc 编译检查

### 主要优势
1. 研究问题定义精准：quality estimation vs. sample selection 的解耦是有价值的概念贡献
2. 实验设计的系统性出色：5 signals × 3 families × 3 datasets × 2 models × 2 N × 2 T + 多项辅助分析
3. Task difficulty gradient 设计合理（CoNLL/SciERC/WNUT），信号排序随难度变化的发现有实用价值
4. 统计实践总体规范（p-values, Cohen's d, CI, 3-seed, Fisher z-test, LOO circularity check）
5. Limitations section 全面诚实

### Overall Assessment
**Verdict: Borderline → Weak Accept for Findings**
核心顾虑：(1) bootstrap 细节不足以确认核心负面结论成立（N1）；(2) model-agnostic overclaim（N2）；(3) RE 结论基础薄弱（N3）。如果 N1 确认执行正确、N2/N3 做适当限定，适合 Findings。进入 Main Conference 需要额外模型规模或 RE 数据集验证。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 138 · 2026-05-15T01:58:38.416217+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 139 · 2026-05-15T01:58:38.416583+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 140 · 2026-05-15T01:58:38.918978+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,WebFetch",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,WebFetch",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 141 · 2026-05-15T01:58:38.972326+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 53
}
```

</details>

---


### Tool call

_source line 142 · 2026-05-15T01:58:45.499664+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper/main.tex",
  "limit": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/paper/main.tex",
    "limit": "150"
  }
}
```

</details>

---


### Tool result

_source line 143 · 2026-05-15T01:58:45.951774+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 144 · 2026-05-15T01:58:45.952113+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool result

_source line 145 · 2026-05-15T01:58:54.895041+00:00_

Web search results for query: "ACL ARR 2025 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"ACL ARR 2025 July | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2025%2FJuly"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"ACLRollingReview (@ReviewAcl) / Posts / X","url":"https://x.com/ReviewAcl"}]

Based on the search results, here's information about ACL ARR 2025-2026 reviewer guidelines, review form criteria, and scoring:

## Reviewer Scores

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation. The soundness scores must be justified by the text of the review.

## Overall Recommendation Scale

The review form includes the following overall recomm
…[truncated 1388 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8942
}
```

</details>

---


### Tool call

_source line 146 · 2026-05-15T01:58:59.062087+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/main.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/main.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 147 · 2026-05-15T01:58:59.566598+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 504
}
```

</details>

---


### Tool call

_source line 148 · 2026-05-15T01:59:00.922327+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form: all scoring dimensions, their scales (1-5 etc.), and descriptions of each score level. Include soundness, excitement, overall recommendation, reproducibility, and any other scored dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form: all scoring dimensions, their scales (1-5 etc.), and descriptions of each score level. Include soundness, excitement, overall recommendation, reproducibility, and any other scored dimensions."
  }
}
```

</details>

---


### Tool result

_source line 149 · 2026-05-15T01:59:08.755456+00:00_

# ACL Rolling Review Form - Scoring Dimensions

## 1. Reviewer Confidence
Scale: 1-5
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: "Quite sure. I tried to check the important points carefully."
- **3**: "Pretty sure, but there's a chance I missed something."
- **2**: "Willing to defend my evaluation, but it is fairly likely that I missed some details."
- **1**: "Not my area, or paper is very hard to understand."

## 2. Soundness
Scale: 1-5 (with .5 increments)
- **5**: Study is among the most thorough for its type
- **4**: Provides sufficient support for claims; extra experiments optional
- **3**: Adequate support for main claims with minor gaps
- **2**: Main claims lack sufficient support; major technical problems
- **1**: Insufficiently thorough or irrelevant to ACL

## 3. Excitement
Scale: 1-5 (with .5 increments)
- **5**: "Highly Exciting: I would recommend this paper to others"
- **4**: Would mention to others; would attend presentation
- **3**: Might mention points to others; would attend if time permits
- **2**: Doesn't resonate personally but may interest others
- **1**: "Not Exciting...I don't think it would with others"

## 4. Overall Assessment
Scale: 1-5 (with .5 increments)
- **5**: Consider for Award (top 2.5%)
- **4**: Conference acceptance
- **3**: Accept to Findings
- **2**: Resubmit next cycle
- **1**: Do not resubmit

## 5. Reproducibility
Scale: 1-5
- **5**: Results easily reproducible
- **4**: Mostly reproducible with minor variations
- **3**: Reproducible with some difficulty
- **2**: Difficult due to unavailable data or insufficient details
- **1**: Impossible to reproduce

## 6. Datasets & Software
Scale: 1-5 (separate)
- **5**: Enabling impact on research decisions
- **4**: Useful for ongoing work
- **3**: Potentially useful
- **2**: Documentary value only
- **1**: No usable contribution

## 7. Author Identity Knowledge
Scale: 1-5
- **5**: Know author identity f
…[truncated 183 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 7833
}
```

</details>

---


### Tool call

_source line 150 · 2026-05-15T01:59:12.928377+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 151 · 2026-05-15T01:59:12.928876+00:00_

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
15	\usepackage{multirow}
16	\usepackage{xcolor}
17	\usepackage{subcaption}
18	
19	\graphicspath{{figures/}}
20	
21	\title{Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence Signals for Test-Time Scaling in Information Extraction}
22	
23	\author{Anonymous}
24	
25	\begin{document}
26	\maketitle
27	
28	\input{sections/abstract}
29	\input{sections/introduction}
30	\input{sections/related_work}
31	\input{sections/method}
32	\input{sections/experiments}
33	\input{sections/discussion}
34	\input{sections/conclusion}
35	
36	\section*{Limitations}
37	\input{sections/limitations}
38	
39	\bibliography{references}
40	
41	\appendix
42	\input{sections/appendix}
43	
44	\end{document}
45	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 152 · 2026-05-15T01:59:16.693959+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
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

_source line 153 · 2026-05-15T01:59:16.694509+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 154 · 2026-05-15T01:59:20.613631+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
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

_source line 155 · 2026-05-15T01:59:20.664526+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 156 · 2026-05-15T01:59:23.626064+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 157 · 2026-05-15T01:59:24.077994+00:00_

1	\begin{abstract}
2	Test-time scaling through multi-sample generation promises quality improvements for LLM-based information extraction, but which confidence signals best serve quality estimation versus sample selection remains unclear.
3	We systematically compare five confidence signals from three families---structural (entity voting, Soft Jaccard), surface (exact match, Fleiss' $\kappa$), and model-internal (log-probability)---across NER and relation extraction on three datasets (SciERC, CoNLL-2003, WNUT-17) with two model families (Qwen3-8B, LLaMA-3.1-8B).
4	We find that the strongest signals achieve $\rho{=}0.38$ (entity voting) and AUROC${=}0.75$ (exact match) for quality estimation, with ranking and classification favoring different signals across task complexity; however, this strong quality estimation does not translate into selection gains---no signal reliably surpasses greedy decoding on either task ($p{>}0.39$, bootstrap) despite 13--18~pp of oracle headroom.
5	We term this disconnect the \textit{correlation-selection gap}: instance-level consistency signals predict which inputs the model handles reliably, not which output is best among $N$ candidates.
6	Signal rankings further depend on task difficulty---exact match dominates easy tasks, structural signals dominate hard tasks, and all signals converge when model capability is insufficient---establishing that signal choice should be guided by task difficulty and intended application.
7	These results reframe consistency signals as quality estimators rather than output selectors for structured IE.
8	\end{abstract}
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 158 · 2026-05-15T01:59:24.278985+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 159 · 2026-05-15T01:59:25.031671+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Self-consistency---sampling multiple outputs and aggregating them---has become a powerful strategy for improving language model reasoning.
4	On discrete-answer tasks such as arithmetic and commonsense QA, majority voting over chain-of-thought samples yields large gains: +18 percentage points on GSM8K \cite{wang2023selfconsistency}.
5	More broadly, test-time compute scaling through repeated sampling and selection has emerged as a complementary axis to model scaling, offering substantial quality improvements at inference time \cite{snell2024scaling, brown2024monkeys}.
6	These results rest on a shared assumption: that among $N$ stochastic samples, a selection mechanism can identify better outputs.
7	For tasks with a single correct answer, this assumption holds naturally---the majority vote is the selector.
8	But information extraction (IE) poses a fundamentally different challenge.
9	The output is not a single token or number; it is a \textit{set} of entities or relations with internal dependencies, where two samples may extract overlapping but non-identical structures.
10	There is no obvious majority to vote on, partial agreement is the norm rather than the exception, and the space of valid outputs is combinatorially large.
11	Can self-consistency still provide useful signal in this structured setting?
12	
13	Prior work on confidence estimation for LLM-based IE has conflated two distinct objectives: \textit{quality estimation} (which inputs does the model handle reliably?) and \textit{sample selection} (which of $N$ outputs is best?).
14	These require fundamentally different signal properties: the former benefits from instance-level aggregation, while the latter demands per-sample discrimination.
15	Self-consistency methods for discrete answers \cite{wang2023selfconsistency, chen2024usc} and weighted variants \cite{taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalence---an assumpti
…[truncated 3524 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 752
}
```

</details>

---


### Tool call

_source line 160 · 2026-05-15T01:59:25.032031+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 161 · 2026-05-15T01:59:25.132700+00:00_

1	\section{Method}\label{sec:method}
2	
3	\subsection{Problem Formulation}\label{sec:formulation}
4	
5	Given a language model $\mathcal{M}$ and input $x$, we sample $N$ structured outputs $\{y_1, \ldots, y_N\}$ at temperature $T > 0$ via constrained decoding \cite{willard2023guided}.
6	Each $y_i$ is an entity set (NER) or relation set (RE).
7	A confidence signal $c$ serves two purposes: (a) \textit{quality estimation}---predicting which instances the model handles reliably, and (b) \textit{sample selection}---identifying the best output among $N$ candidates.
8	
9	A \textbf{per-sample signal} scores each $y_i$ independently, $c_{\text{ps}}: (x, y_i) \to \mathbb{R}$, enabling direct candidate ranking.
10	An \textbf{instance-level signal} aggregates over all $N$ samples, $c_{\text{il}}: (x, \{y_i\}_{i=1}^N) \to \mathbb{R}$, producing a single score per input.
11	This asymmetry---between predicting \textit{which inputs} are easy and selecting \textit{which output} is best---is central to the correlation-selection gap we investigate.
12	Notation is summarized in Appendix~\ref{app:notation}.
13	
14	\subsection{Confidence Signals}\label{sec:signals}
15	
16	We compare five signals from three families: \textit{model-internal} (log-probability), \textit{surface} (exact match, Fleiss' $\kappa$), and \textit{structural} (Soft Jaccard, entity voting).
17	
18	\paragraph{Log-probability (model-internal, per-sample).}
19	The only per-sample signal.
20	For sample $y_i$ with tokens $t_1, \ldots, t_{|y_i|}$:
21	\begin{equation}\label{eq:logprob}
22	c_{\text{lp}}(y_i) = \frac{1}{|y_i|} \sum_{j=1}^{|y_i|} \log p_{\mathcal{M}}(t_j \mid t_{<j}, x)
23	\end{equation}
24	
25	\paragraph{Exact match voting (surface, instance-level).}
26	The majority fraction---the proportion of samples producing the most common output:
27	\begin{equation}\label{eq:em}
28	c_{\text{em}}(x) = \frac{1}{N} \max_{y} \big|\{i : y_i = y\}\big|
29	\end{equation}
30	
31	\paragraph{Fleiss' $\kappa$ (surface, instance-lev
…[truncated 2626 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 162 · 2026-05-15T01:59:25.183460+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 163 · 2026-05-15T01:59:25.234237+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Datasets.}
8	We evaluate on three English IE benchmarks spanning a difficulty gradient.
9	\textbf{SciERC} \cite{luan2018scierc} contains 551 test instances annotated for joint NER (6 types) and RE (7 types).
10	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} provides 3{,}453 test sentences with 4 entity types, where models achieve ${>}$91\% micro F1.
11	\textbf{WNUT-17} \cite{derczynski2017wnut} consists of 1{,}287 social media instances with emerging entities, used to probe method boundaries (54\% zero F1).
12	
13	\paragraph{Models and sampling.}
14	Our primary model is \textbf{Qwen3-8B} (LoRA, $r{=}32$); for cross-model validation, we evaluate \textbf{LLaMA-3.1-8B-Instruct}.
15	We draw $N{=}8$ samples at $T{=}1.0$ (primary), with $N{=}16$ for scaling experiments.\footnote{$N{=}16$ results for CoNLL (Qwen) and SciERC (LLaMA) are in Table~\ref{tab:robustness} (Appendix~\ref{app:robustness}).}
16	Quality estimation uses Spearman $\rho$ and AUROC; downstream utility uses best-of-$N$ selection F1 with exact span matching (NER) and head-tail-label matching (RE).
17	Inference uses vLLM with constrained decoding \cite{willard2023guided}.
18	
19	%% ============================================================
20	\subsection{Quality Estimation Results}
21	\label{sec:qe_results}
22	
23	\begin{table*}[t]
24	\centering
25	\small
26	\caption{Quality estimation across tasks and models (Spearman $\rho$ and AUROC). Best value per block and column in \textbf{bold}. SciERC evaluates joint NER (6 types) and RE (7 types); CoNLL evaluates NER (4 types). Primary results use $N{=}8$, $T{=}1.0$; $N{=}16$ block reports LLaMA CoNLL 3-seed mean${\pm}$std.}
27	\label{tab:quality_estimation}
28	\begin{tabular}{ll cc cc cc cc}
29	\toprule
30	& & \multicolumn{2}{c}{\textbf{SciERC NER}} & \multicolumn{2}{c}{\textbf{SciERC RE}} & \multicolumn{2}{c}{\textbf{CoNLL (Qwen)}} & \mu
…[truncated 7771 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 164 · 2026-05-15T01:59:29.458089+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 165 · 2026-05-15T01:59:29.860083+00:00_

1	\section{Discussion}\label{sec:discussion}
2	
3	\paragraph{Practical recommendations.}
4	For per-instance quality ranking, entity voting provides the strongest rank correlation ($\rho{=}0.38$, Table~\ref{tab:quality_estimation}), though exact match leads binary discrimination on SciERC (AUROC${=}0.749$).
5	When temperature or cross-condition robustness is required, SJ is preferable: its temperature sensitivity is small with bootstrap CIs including zero (Table~\ref{tab:robustness}).
6	Under conditional filtering, EM leads on both NER and RE ($\rho{=}0.360$, $0.417$), extending binary-agreement advantages to the within-capability regime.
7	Signal rankings depend on task difficulty: EM dominates on easy tasks (CoNLL, F1${>}$0.91), Voting and SJ dominate on hard tasks (SciERC, F1$\,{\approx}\,$0.66), and all signals converge when model capability is insufficient (WNUT-17).
8	This ordering is model-agnostic, suggesting the difficulty gradient determines which signal family is most informative.
9	Conditional filtering confirms this pattern: removing zero-F1 instances shifts effective difficulty toward the easy-task regime, and EM reclaims the lead while Voting and SJ drop substantially (Voting RE: $0.350{\to}0.241$).
10	
11	\paragraph{Why quality estimators fail as selectors.}
12	Quality estimation ranks \textit{instances} by expected output quality via output distribution entropy; sample selection ranks \textit{candidates within a single instance}, requiring per-sample quality information that instance-level aggregation discards.
13	On SciERC NER, the random baseline (0.608) falls 3.6~pp below greedy (0.644), confirming per-instance sample variance exists; yet the oracle gap of 13.2~pp shows substantially better candidates exist, and the best signal captures only +0.6~pp ($p{=}0.39$).
14	The $\rho$--AUROC dissociation illuminates the same asymmetry: on SciERC, EM achieves the highest AUROC (0.749 NER, 0.706 RE) yet ranks third or last in $\rho$; both metrics measure be
…[truncated 1013 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 166 · 2026-05-15T01:59:29.860506+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 167 · 2026-05-15T01:59:29.961288+00:00_

1	Our evaluation covers three datasets but only one RE benchmark (SciERC), where 44\% of instances receive zero F1, compressing the discriminable range and limiting signal differentiation for relation extraction.
2	WNUT-17 confirms the capability boundary of our approach, but our positive results on formal-domain text (CoNLL, SciERC) have not been validated on informal or noisy text where models achieve non-trivial performance.
3	
4	We evaluate two model families (Qwen3-8B and LLaMA-3.1-8B), both at 8B parameters.
5	Whether our findings---particularly the correlation-selection gap and the structural-over-surface signal ordering---hold for larger models (70B+) or closed-source APIs remains untested.
6	Larger models may produce higher-quality and more diverse samples, potentially altering the signal landscape.
7	
8	Our analysis of selection potential uses unsupervised signals and a logistic regression proxy as an upper bound.
9	We do not train a dedicated verifier or reward model, leaving unknown how much of the oracle headroom a supervised approach could recover.
10	
11	We evaluate at $N{=}8$ and $N{=}16$.
12	The behavior of confidence signals at larger sample sizes (e.g., $N{=}64$ or $N{=}128$) is unknown, and $N$-scaling gains are setting-dependent: SJ improves by $+0.052$ on Qwen SciERC NER but only $+0.016$ on LLaMA SciERC NER when doubling from $N{=}8$ to $N{=}16$.
13	
14	On CoNLL with LLaMA, the SJ--FK gap is only 0.003 ($\rho{=}0.431$ vs.\ $0.428$), so the structural advantage over surface signals may not generalize to all simple-schema datasets.
15	Finally, log-probability was excluded from the temperature comparison ($T{=}0.7$ vs.\ $T{=}1.0$) due to missing $T{=}0.7$ logprob data, leaving its temperature sensitivity uncharacterized.
16	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 168 · 2026-05-15T01:59:30.363544+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 169 · 2026-05-15T01:59:30.816018+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	This work provides the first systematic evaluation of confidence signals for test-time scaling in generative information extraction.
4	By comparing five signals from three families---structural, surface, and model-internal---across NER and RE tasks of varying difficulty, we disentangle two objectives that prior work has conflated: quality estimation (ranking instances by expected performance) and sample selection (choosing the best output among $N$ candidates).
5	Our experiments on SciERC, CoNLL-2003, and WNUT-17 with Qwen3-8B and LLaMA-3.1-8B reveal that these objectives require fundamentally different signal properties.
6	
7	Three findings anchor our analysis.
8	First, consistency-based signals are effective quality estimators: entity voting achieves the strongest rank correlation ($\rho{=}0.38$) while exact match leads binary discrimination (AUROC${=}0.75$) on SciERC NER, with signal rankings depending on both task complexity and evaluation metric.
9	Second, the \textit{correlation-selection gap} shows that strong instance-level correlation does not yield substantial selection gains---no signal reliably surpasses greedy on either task (NER logprob: +0.6~pp, $p{=}0.39$; RE: $-$0.9~pp) despite 13--18~pp of oracle headroom---because instance-level signals cannot discriminate among candidates with similar consistency profiles.
10	Third, signal rankings depend on task difficulty: exact match leads on easy tasks, Soft Jaccard and voting lead on hard tasks, and all signals converge when model capability is insufficient, establishing practical guidance for signal choice.
11	
12	Several directions remain open.
13	Trained verifiers or reward models could close the selection gap by learning per-sample quality discrimination that unsupervised consistency signals lack.
14	Cross-task transfer of confidence signals beyond IE---to structured prediction tasks such as semantic parsing and code generation---would test the generality
…[truncated 321 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 170 · 2026-05-15T01:59:30.816560+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 171 · 2026-05-15T01:59:30.967655+00:00_

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
21	$c_{\text{vote}}$ & Entity voting confidence \\
22	$c_{\text{lp}}$ & Log-probability (mean token log-likelihood) \\
23	\bottomrule
24	\end{tabular}
25	\caption{Notation used throughout the paper.}
26	\label{tab:notation}
27	\end{table}
28	
29	\section{Robustness Analysis}\label{app:robustness}
30	
31	\begin{table}[t]
32	\centering
33	\small
34	\caption{Signal robustness across configurations (Spearman $\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: cross-model transfer (LLaMA CoNLL $N{=}16$, 3-seed mean $\pm\sigma$). $^\dagger$Mean over 3 seeds ($\sigma{=}0.025$; individual: 0.428, 0.424, 0.384).}
35	\label{tab:robustness}
36	\begin{tabular}{llcc}
37	\toprule
38	& & NER $\rho$ & RE $\rho$ \\
39	\midrule
40	\multicolumn{4}{l}{\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\
41	\quad SJ & $T{=}0.7$ & 0.388 & 0.234 \\
42	\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\
43	\quad FK & $T{=}0.7$ & 0.321 & 0.184 \\
44	\quad FK & $T{=}1.0$ & 0.267 & 0.275 \\
45	\midrule
46	\multicolumn{4}{l}{\textit{Sample size} (Qwen SciERC, $T{=}1.0$)} \\
47	\quad SJ & $N{=}8$  & 0.360 & 0.250 \\
48	\quad SJ & $N{=}16$ & 0.412$^\dagger$ & 0.281 \\
49	\quad FK & $N{=}8$  & 0.267 & 0.275 \\
50	\quad FK & $N{=}16$ & 0.280 & 0.279 \\
51	\midrule
52	\multicolumn{4}{l}{\textit{Cross-model} (LLaMA CoNLL, $N{=}16$, 3 seeds)} \\
53	\quad SJ &  & $0.463{\pm}0.007$ & --- \\
54	\quad FK &  & $0.455{\pm}0.006$ & --- \\
55	\quad EM &  & $0.460{\pm
…[truncated 9406 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 172 · 2026-05-15T01:59:34.932742+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 173 · 2026-05-15T01:59:34.933310+00:00_

1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Self-consistency and test-time scaling.}
4	Self-consistency decoding \cite{wang2023selfconsistency} improves reasoning by majority voting over chain-of-thought samples, assuming a discrete answer space.
5	Extensions to free-form text use LLM-based comparison \cite{chen2024usc}, atomic sub-claim decomposition \cite{thirukovalluru2024atomic}, or cross-sample hallucination detection \cite{manakul2023selfcheckgpt}.
6	For test-time scaling, \citet{snell2024scaling} characterize compute scaling laws and \citet{brown2024monkeys} show best-of-$N$ gains across tasks.
7	Recent reward-free selectors include confidence-weighted voting \cite{taubenfeld2025cisc}, KL-based self-certainty \cite{kang2025selfcertainty}, adaptive sampling \cite{kim2026reasc}, ranked aggregation \cite{wang2025rankedvoting}, and latent-space consistency \cite{oh2025latentsc}.
8	All target reasoning/QA with discrete answers.
9	Our work extends self-consistency to set-valued structured outputs and identifies the correlation-selection gap: strong quality estimation ($\rho{=}0.38$) coexists with selection failure ($p{>}0.39$).
10	
11	\paragraph{Consistency for structured IE.}
12	\citet{nedellec2026consistency} study consistency--accuracy correlations for LLM-based NER/RE, corroborating our quality-estimation findings.
13	However, they rely on surface-level matching (explicitly acknowledging it ``overlooks semantically consistent outputs''), do not study best-of-$N$ selection, and evaluate a single domain with hard prompting.
14	Our Soft Jaccard signal addresses the matching limitation through type-aware bipartite matching with span overlap.
15	CoCoA \cite{vashurin2025cocoa} fuses model confidence with inter-sample consistency for QA/summarization but does not address structured extraction.
16	Our evaluation builds on generative IE work \cite{zhou2024uniner, sainz2024gollie, josifoski2022genie, li2023codeie, wadhwa2023revisiting, wang2023instructuie
…[truncated 1727 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 174 · 2026-05-15T01:59:40.254833+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.bib",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 175 · 2026-05-15T01:59:40.405887+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 176 · 2026-05-15T01:59:44.723320+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "snell2024scaling",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
  "output_mode": "content",
  "-A": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "snell2024scaling",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib",
    "output_mode": "content",
    "-A": "10"
  }
}
```

</details>

---


### Tool result

_source line 177 · 2026-05-15T01:59:44.773992+00:00_

253:@inproceedings{snell2024scaling,
254-  title = {Scaling {LLM} Test-Time Compute Optimally can be More Effective than Scaling Model Parameters},
255-  author = {Snell, Charlie and Lee, Jaehoon and Xu, Kelvin and Kumar, Aviral},
256-  booktitle = {ICLR 2025},
257-  year = {2024},
258-  url = {https://arxiv.org/abs/2408.03314}
259-}
260-
261-@inproceedings{taubenfeld2025cisc,
262-  title = {Confidence Improves Self-Consistency in LLMs},
263-  author = {Taubenfeld, Amir and Sheffer, Tom and Ofek, Eran and Feder, Amir and Goldstein, Ariel and Gekhman, Zorik and Yona, Gal},

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 178 · 2026-05-15T01:59:49.298057+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "model-agnostic|model.agnostic",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
  "output_mode": "content",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "model-agnostic|model.agnostic",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
    "output_mode": "content",
    "-i": "True"
  }
}
```

</details>

---


### Tool result

_source line 179 · 2026-05-15T01:59:49.499287+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:135:The structural-over-logprob advantage is model-agnostic, holding across all four $N{=}16$ settings ($\Delta\rho{=}{+}0.135$ to ${+}0.175$).
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex:8:This ordering is model-agnostic, suggesting the difficulty gradient determines which signal family is most informative.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 180 · 2026-05-15T01:59:52.818532+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "logistic regression|upper bound",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
  "output_mode": "content",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "logistic regression|upper bound",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
    "output_mode": "content",
    "-i": "True"
  }
}
```

</details>

---


### Tool result

_source line 181 · 2026-05-15T01:59:52.869181+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:89:\caption{The correlation-selection gap on SciERC ($N{=}8$, $T{=}1.0$). Left: NER; right: RE. Bars show best-of-$N$ selection F1; the line marks quality estimation $\rho$. Despite $\rho$ up to 0.38, no signal reliably surpasses greedy on either task ($p{=}0.39$ for NER logprob, the best signal). Dashed line indicates oracle upper bound.}
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex:8:Our analysis of selection potential uses unsupervised signals and a logistic regression proxy as an upper bound.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:132:For sample selection, additional samples increase the oracle upper bound---more draws raise the probability of a high-quality candidate---but signal-based selection remains flat because the selector's inability to identify the best candidate is a granularity limitation, not a sample size limitation.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.aux:556:\@writefile{lof}{\contentsline {figure}{\numberline {3}{\ignorespaces The correlation-selection gap on SciERC ($N{=}8$, $T{=}1.0$). Left: NER; right: RE. Bars show best-of-$N$ selection F1; the line marks quality estimation $\rho $. Despite $\rho $ up to 0.38, no signal reliably surpasses greedy on either task ($p{=}0.39$ for NER logprob, the best signal). Dashed line indicates oracle upper bound.}}{7}{figure.caption.21}\protected@file@percent }
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.aux:557:\newlabel{fig:selection_gap}{{3}{7}{The correlation-selection gap on SciERC ($N{=}8$, $T{=}1.0$). Left: NER; right: RE. Bars show best-of-$N$ selection F1; the line marks quality estimation $\rho $. Despite $\rho $ up to 0.38, no signa
…[truncated 153 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 182 · 2026-05-15T02:00:00.304394+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "bootstrap",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
  "output_mode": "content",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "bootstrap",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
    "output_mode": "content",
    "-i": "True"
  }
}
```

</details>

---


### Tool result

_source line 183 · 2026-05-15T02:00:00.355065+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex:21:Yet no signal reliably surpasses greedy decoding on best-of-$N$ selection ($p{>}0.39$, bootstrap) despite 13--18~pp of oracle headroom.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex:41:    Despite strong instance-level correlations ($\rho$ up to 0.38), no signal reliably surpasses greedy on either task ($p{>}0.39$, bootstrap) despite 13--18~pp of oracle headroom.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:119:Logprob achieves the highest selection F1 (0.650, +0.6~pp), but this is not statistically significant ($p{=}0.39$, 3-seed bootstrap; Cohen's $d{=}0.038$).
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex:133:SJ NER $\rho$ shifts by only 0.028 between $T{=}0.7$ and $T{=}1.0$ (bootstrap CI includes zero).
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex:4:We find that the strongest signals achieve $\rho{=}0.38$ (entity voting) and AUROC${=}0.75$ (exact match) for quality estimation, with ranking and classification favoring different signals across task complexity; however, this strong quality estimation does not translate into selection gains---no signal reliably surpasses greedy decoding on either task ($p{>}0.39$, bootstrap) despite 13--18~pp of oracle headroom.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex:70:SJ NER $\rho$ shifts from 0.388 ($T{=}0.7$) to 0.360 ($T{=}1.0$), a difference of 0.028 whose bootstrap confidence interval includes zero.
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex:5:When temperature or cross-condition robustness 
…[truncated 131 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 184 · 2026-05-15T02:00:03.922192+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "PaLM|540B|GSM8K",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
  "output_mode": "content",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Grep",
  "tool_args": {
    "pattern": "PaLM|540B|GSM8K",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
    "output_mode": "content",
    "-i": "True"
  }
}
```

</details>

---


### Tool result

_source line 185 · 2026-05-15T02:00:04.025000+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex:4:On discrete-answer tasks such as arithmetic and commonsense QA, majority voting over chain-of-thought samples yields large gains: +18 percentage points on GSM8K \cite{wang2023selfconsistency}.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Grep",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 186 · 2026-05-15T02:02:50.109765+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 对 Reviewer 1 Round 1 意见的交叉回应\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R1-N1: Bootstrap 检验细节严重不足**\n\n同意，且认为这是本文最关键的方法论缺陷。\n\n逐一验证 R1 的子问题：\n1. **Bootstrap 迭代次数**：全文未报告。Section 5.3 仅写 \"p=0.39, 3-seed bootstrap; Cohen's d=0.038\"，Appendix 未补充。\n2. **Paired vs unpaired**：未说明。这对 best-of-N vs greedy 比较至关重要——paired bootstrap 在每个 instance 上匹配两种方法，统计功效远高于 unpaired。\n3. **检验统计量**：未说明是对 F1 差值做 bootstrap，还是对 paired difference 做 bootstrap-t。\n4. **\"3-seed bootstrap\" 含义**：这是最致命的歧义。对照 Table 1 的 N=16 block 使用 \"3-seed mean±std\" 的语境，\"3-seed\" 最可能指 3 次独立 sampling 的随机种子。如果 bootstrap 是在这 3 个 seed 的 mean F1 上做 (n=3)，则完全无统计功效——任何 p 值都没有诊断价值。即使是在每个 seed 内对 551 个 SciERC instance 做 paired bootstrap 再合并，论文也必须说明合并策略。\n\n**补充发现**：论文在 5 处重复引用 \"p>0.39, bootstrap\"（Abstract、Introduction ×2、Section 5.3、Conclusion），但从未给出检验的完整规范。这个 p 值支撑了标题 (\"Weak Selectors\")、Contribution #2（correlation-selection gap）、以及 Discussion 中对 trained verifier 的呼吁。如果检验无效，论文的核心贡献坍塌为 \"我们没有足够的统计功效来判断 selection 是否有效\"——这是一个完全不同的结论。\n\n---\n\n**[AGREE] R1-N2: \"Model-agnostic\" overclaim，但需精确定位**\n\n同意存在 overclaiming，但 R1 对问题的定位可以更精确。\n\n论文中 \"model-agnostic\" 出现两处：\n- Section 5.4 (experiments.tex:135): \"The structural-over-logprob advantage is model-agnostic, holding across all four N=16 settings\"\n- Discussion (discussion.tex:8): \"This ordering is model-agnostic, suggesting the difficulty gradient determines which signal family is most informative\"\n\n两处的上下文都是在描述 Qwen3-8B 与 LLaMA-3.1-8B 之间的一致性。论文确实在 Limitations 中承认 \"Whether our findings hold for larger models (70B+) or closed-source APIs remains untested\"（limitations.tex:5-6）。R1 正确指出这构成内部矛盾。\n\n然而，我认为修复成本很低：将 \"model-agnostic\" 替换为 \"consistent across tested model families\" 即可。核心发现（structural > logprob 在两个 8B 模型上一致）本身是有效的，overclaim 在于措辞而非实验设计。ARR R4 标准下，这是 Should-Fix 级别——需要措辞修正，但不构成一票否决。\n\n---\n\n**[AGREE] R1-N3: RE 结论仅基于 SciERC，但严重程度可适度下调**\n\n同意 RE 实验基础薄弱。SciERC RE 是唯一的 RE 数据集，44% zero-F1 严重限制了信号区分度。论文自身在 Section 5.1 (experiments.tex:62) 承认 \"all signals weaken due to the 44% zero-F1 floor effect\"，Limitations 再次确认（limitations.tex:1-2），Appendix 的 per-relation diagnostic 也指出 \"entity span errors account for 55.5% of RE false negatives\"——这意味着 RE correlation 很大程度上反映 NER 上游错误传播，而非 RE 本身的信号质量。\n\n但有两点缓和因素 R1 未提及：\n1. **Conditional filtering**（Appendix, appendix.tex:120-121）移除 zero-F1 instance 后，SJ RE 恢复到 ρ=0.405，EM RE 达到 ρ=0.417——说明在 non-trivial subset 上信号仍有区分力。\n2. **Capability stratification**（Appendix, appendix.tex:112）在高复杂度 RE 子集上，Voting 达到 ρ=0.630——说明信号在有足够结构信息时表现良好。\n\n综合看：R1 说 \"RE 的所有结论全部来自 SciERC RE 一个数据集\" 是事实。但论文标题和贡献声称覆盖 \"NER and RE\"，RE 部分用 conditional analysis 做了缓解。我建议将 R1 的评估从 critical 降到 high-warning：要求作者在 Discussion 中更显式地限定 RE 结论的泛化范围，而非要求追加 RE 数据集实验（这超出 revision 的合理范围）。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R1-W1: Soft Jaccard 形式化有歧义**\n\n同意。Eq. (4) 中 g_i, g_j 在文本中说是 \"per-type extraction counts\"（method.tex:43），但符号定义和 denominator 的直觉不够清晰——读者需要推断 denominator 是 type-wise max count 的求和。sim 在文本中定义为 \"span-level Jaccard overlap\"（method.tex:43），但未给出公式（是 token-level IoU 还是 character-level？）。Hungarian algorithm 的匹配阈值（e.g., 最低 overlap 要求）也未说明。\n\n这些缺失不影响论文结论的有效性，但影响 reproducibility。\n\n---\n\n**[AGREE] R1-W2: Entity voting 的 mean frequency 聚合方式**\n\n同意这是一个有效的方法论关注。Eq. (6) 用 |E_∪| 做分母，当模型产生大量低频幻觉实体时，|E_∪| 膨胀导致 c_vote 系统性偏低。论文未讨论替代方案（median frequency、frequency-thresholded voting、top-k entity filtering）。\n\n补充一个 R1 未提到的相关问题：entity voting 和 Soft Jaccard 在概念上有 overlap——两者都基于 entity-level 跨 sample 一致性，只是聚合方式不同。论文未讨论这两个 structural signal 之间的冗余度（e.g., 它们的 instance-level correlation 是多少？）。如果高度相关，那么 \"两个 structural signal 都优于 surface signal\" 的论证就被削弱——实际上可能是同一个 signal 的两种近似。\n\n---\n\n**[REBUT] R1-W3: ρ=0.38 被描述为 \"effective/strong\"**\n\n部分反驳。R1 的 framing 有偏差。\n\n论文实际措辞是 \"effective quality estimators\"（Section 5.3 标题, discussion.tex:1-4）和 \"strongest rank correlation\"（discussion.tex:1），而非 \"strong correlation\"。\"Strongest\" 是相对于其他信号的比较级，\"effective\" 指向实用价值。论文从未声称 ρ=0.38 在绝对意义上 \"strong\"。\n\n更重要的是，ρ 不是论文用来论证实用价值的唯一指标：AUROC=0.749（NER）和 0.706（RE）才是面向 routing/triage 应用的核心证据。AUROC 0.75 意味着 75% 的概率正确区分高/低质量 instance——这对于 \"flagging uncertain instances for human review\"（discussion.tex:15）而言是实用的。\n\n但 R1 关于缺乏 contextualization 的批评部分成立：论文未与 uncertainty estimation 文献中的其他方法（如 semantic entropy、P(True)、ensemble-based uncertainty）的 ρ 值对比。这个对比在 Related Work 中是缺失的。\n\n---\n\n**[AGREE] R1-W4: Logprob 温度敏感性数据缺失**\n\n同意。Section 5.4 (experiments.tex:132) 说 \"Signal rankings are robust across temperatures\"，但 logprob 是唯一的 per-sample signal（也是 Section 5.3 中 selection F1 最高的 signal），其 T=0.7 数据在 Limitations 中承认 \"unavailable\"（limitations.tex:15）。\n\n这不仅是一个数据缺失问题，还影响论文的核心论点：如果 logprob 在 T=0.7 时 selection 表现显著不同，那么 \"no signal reliably surpasses greedy\" 的结论可能不成立。论文至少应将 \"robust across temperatures\" 的表述限定为 \"consistency-based signals are robust across temperatures; logprob temperature sensitivity remains uncharacterized\"。\n\n---\n\n**[AGREE] R1-W5: WNUT-17 \"establishing the capability boundary\" 措辞过度**\n\n同意 R1 的统计学批评：fail to reject null ≠ accept null。p=0.106 不能 \"establish\" 一个 boundary。\n\n但补充 R1 未提到的一点：WNUT-17 上 ρ=0.082 的效应量本身（不论 p 值）已经非常小，结合 54% zero-F1 的先验信息，\"capability boundary\" 的实质结论是合理的。问题在于 statistical rhetoric——应改为 \"consistent with a capability boundary\" 或 \"suggests that signals break down\"。\n\n---\n\n**[AGREE] R1-W6: Qwen3-8B (LoRA) vs LLaMA-3.1-8B-Instruct 训练设置不对称**\n\n同意。Section 5.1 (experiments.tex:14) 说 \"Qwen3-8B (LoRA, r=32)\" 但 LLaMA-3.1-8B-Instruct 未说明是否经过 LoRA/SFT fine-tuning。如果 LLaMA 使用的是 off-the-shelf instruction-tuned model 而 Qwen 经过了 task-specific LoRA fine-tuning，那么 cross-model comparison 混淆了 model architecture 和 training strategy 两个变量。\n\n这个问题在 Table 1 的 cross-model 比较 (Δ=0.005) 和 Section 5.4 的 \"model-agnostic\" 结论中尤为突出。\n\n---\n\n**[AGREE] R1-W7: 约束解码对 sampling diversity 的影响**\n\n同意，且认为 R1 低估了这个问题的重要性。\n\n约束解码（constrained decoding via Outlines/vLLM, method.tex:5）强制输出符合预定义的 JSON/structured schema。这会显著减少 token-level 自由度，从而压缩 per-sample variance。如果 per-sample variance 被约束解码人为压低，那么 correlation-selection gap 可能部分是实验设计的 artifact 而非结构化 IE 的固有属性。\n\n具体来说：\n- Discussion (discussion.tex:12-13) 用 random baseline (0.608) 和 greedy (0.644) 的 gap (3.6 pp) 证明 \"per-instance sample variance exists\"。但这个 variance 是在约束解码下的 variance——无约束解码下可能更大。\n- 如果无约束解码产生更多样的（但可能格式不正确的）输出，selection 的 headroom 可能更大，信号的 selection 能力可能更强。\n\n论文应至少讨论这个 confound，即使无法提供无约束解码的对比实验。\n\n---\n\n### 小问题\n\n**[AGREE] Table 2 EM \"---\"**：Caption 中有解释（\"EM produces binary agreement without sample ranking\"），但 Table 2 自身缺乏脚注或更显眼的标注。\n\n**[AGREE] Logistic regression proxy**：Limitations (limitations.tex:8) 提到 \"logistic regression proxy as an upper bound\" 但正文和 Appendix 均未报告结果。要么展示结果，要么删除提及。\n\n**[AGREE] snell2024scaling bib**：bib entry 显示 \"Snell, Charlie and Lee, Jaehoon and Xu, Kelvin and Kumar, Aviral\" (ICLR 2025)。需要与 OpenAlex 交叉验证是否缺少作者。\n\n**[AGREE] Cross-model Δ=0.005 bootstrap CI**：experiments.tex:73 报告 SJ ρ=0.436 (Qwen) vs 0.431 (LLaMA) 但未报告差异是否在 CI 内。鉴于 N=16 的 3-seed std 约 0.007，Δ=0.005 几乎确定不显著，但应明确报告。\n\n**[AGREE] Introduction \"+18pp on GSM8K\" 未注明模型**：wang2023selfconsistency 的 +18pp 来自 PaLM-540B，一个与本文 8B 模型规模相差甚远的模型。不注明可能误导读者认为 +18pp 在小模型上也成立。\n\n**[AGREE] Appendix D \\textsc**：appendix.tex:102 使用 `\\textsc{Feature-Of}` 和 `\\textsc{Hyponym-Of}`，需确认编译无误（特别是连字符在 small caps 下的渲染）。\n\n---\n\n### 对 R1 主要优势的回应\n\nR1 列出的 5 点优势全部成立，我补充两点：\n\n1. **Quality estimation vs sample selection 的概念解耦**确实是本文最有价值的贡献。这个 framing 对后续工作有直接指导意义——不论负面结论（weak selectors）是否最终成立。\n2. **Conditional filtering analysis**（Appendix）是一个被忽视的亮点。它揭示了 EM 在 non-trivial subset 上的优势，并提供了 \"task difficulty determines signal choice\" 的额外证据维度。\n\n---\n\n### 对 R1 Overall Assessment 的回应\n\nR1 给出 \"Borderline → Weak Accept for Findings, Overall 3/5\"。我基本同意这个判断区间。\n\n我与 R1 的主要分歧在于问题严重程度的校准：\n- **N1 (bootstrap)**：完全同意 critical。这是最需要修复的问题。\n- **N2 (model-agnostic)**：同意需修正，但认为是 should-fix 级别（措辞修正即可），不构成 critical。\n- **N3 (RE 基础薄弱)**：同意 concern，但论文已有 conditional analysis 作为缓解，建议降为 high-warning。\n- **W7 (constrained decoding)**：R1 将此列为 warning，我认为应升级——这可能从根本上解释 correlation-selection gap，而非仅是一个遗漏的讨论点。\n\n如果 N1 bootstrap 细节补全且确认方法学正确，加上 N2 措辞修正，本文适合 Findings track。",
  "reviewer_id": "2",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 对 Reviewer 1 Round 1 意见的交叉回应\n\n---\n\n### Must-Fix 问题\n\n**[AGREE] R1-N1: Bootstrap 检验细节严重不足**\n\n同意，且认为这是本文最关键的方法论缺陷。\n\n逐一验证 R1 的子问题：\n1. **Bootstrap 迭代次数**：全文未报告。Section 5.3 仅写 \"p=0.39, 3-seed bootstrap; Cohen's d=0.038\"，Appendix 未补充。\n2. **Paired vs unpaired**：未说明。这对 best-of-N vs greedy 比较至关重要——paired bootstrap 在每个 instance 上匹配两种方法，统计功效远高于 unpaired。\n3. **检验统计量**：未说明是对 F1 差值做 bootstrap，还是对 paired difference 做 bootstrap-t。\n4. **\"3-seed bootstrap\" 含义**：这是最致命的歧义。对照 Table 1 的 N=16 block 使用 \"3-seed mean±std\" 的语境，\"3-seed\" 最可能指 3 次独立 sampling 的随机种子。如果 bootstrap 是在这 3 个 seed 的 mean F1 上做 (n=3)，则完全无统计功效——任何 p 值都没有诊断价值。即使是在每个 seed 内对 551 个 SciERC instance 做 paired bootstrap 再合并，论文也必须说明合并策略。\n\n**补充发现**：论文在 5 处重复引用 \"p>0.39, bootstrap\"（Abstract、Introduction ×2、Section 5.3、Conclusion），但从未给出检验的完整规范。这个 p 值支撑了标题 (\"Weak Selectors\")、Contribution #2（correlation-selection gap）、以及 Discussion 中对 trained verifier 的呼吁。如果检验无效，论文的核心贡献坍塌为 \"我们没有足够的统计功效来判断 selection 是否有效\"——这是一个完全不同的结论。\n\n---\n\n**[AGREE] R1-N2: \"Model-agnostic\" overclaim，但需精确定位**\n\n同意存在 overclaiming，但 R1 对问题的定位可以更精确。\n\n论文中 \"model-agnostic\" 出现两处：\n- Section 5.4 (experiments.tex:135): \"The structural-over-logprob advantage is model-agnostic, holding across all four N=16 settings\"\n- Discussion (discussion.tex:8): \"This ordering is model-agnostic, suggesting the difficulty gradient determines which signal family is most informative\"\n\n两处的上下文都是在描述 Qwen3-8B 与 LLaMA-3.1-8B 之间的一致性。论文确实在 Limitations 中承认 \"Whether our findings hold for larger models (70B+) or closed-source APIs remains untested\"（limitations.tex:5-6）。R1 正确指出这构成内部矛盾。\n\n然而，我认为修复成本很低：将 \"model-agnostic\" 替换为 \"consistent across tested model families\" 即可。核心发现（structural > logprob 在两个 8B 模型上一致）本身是有效的，overclaim 在于措辞而非实验设计。ARR R4 标准下，这是 Should-Fix 级别——需要措辞修正，但不构成一票否决。\n\n---\n\n**[AGREE] R1-N3: RE 结论仅基于 SciERC，但严重程度可适度下调**\n\n同意 RE 实验基础薄弱。SciERC RE 是唯一的 RE 数据集，44% zero-F1 严重限制了信号区分度。论文自身在 Section 5.1 (experiments.tex:62) 承认 \"all signals weaken due to the 44% zero-F1 floor effect\"，Limitations 再次确认（limitations.tex:1-2），Appendix 的 per-relation diagnostic 也指出 \"entity span errors account for 55.5% of RE false negatives\"——这意味着 RE correlation 很大程度上反映 NER 上游错误传播，而非 RE 本身的信号质量。\n\n但有两点缓和因素 R1 未提及：\n1. **Conditional filtering**（Appendix, appendix.tex:120-121）移除 zero-F1 instance 后，SJ RE 恢复到 ρ=0.405，EM RE 达到 ρ=0.417——说明在 non-trivial subset 上信号仍有区分力。\n2. **Capability stratification**（Appendix, appendix.tex:112）在高复杂度 RE 子集上，Voting 达到 ρ=0.630——说明信号在有足够结构信息时表现良好。\n\n综合看：R1 说 \"RE 的所有结论全部来自 SciERC RE 一个数据集\" 是事实。但论文标题和贡献声称覆盖 \"NER and RE\"，RE 部分用 conditional analysis 做了缓解。我建议将 R1 的评估从 critical 降到 high-warning：要求作者在 Discussion 中更显式地限定 RE 结论的泛化范围，而非要求追加 RE 数据集实验（这超出 revision 的合理范围）。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R1-W1: Soft Jaccard 形式化有歧义**\n\n同意。Eq. (4) 中 g_i, g_j 在文本中说是 \"per-type extraction counts\"（method.tex:43），但符号定义和 denominator 的直觉不够清晰——读者需要推断 denominator 是 type-wise max count 的求和。sim 在文本中定义为 \"span-level Jaccard overlap\"（method.tex:43），但未给出公式（是 token-level IoU 还是 character-level？）。Hungarian algorithm 的匹配阈值（e.g., 最低 overlap 要求）也未说明。\n\n这些缺失不影响论文结论的有效性，但影响 reproducibility。\n\n---\n\n**[AGREE] R1-W2: Entity voting 的 mean frequency 聚合方式**\n\n同意这是一个有效的方法论关注。Eq. (6) 用 |E_∪| 做分母，当模型产生大量低频幻觉实体时，|E_∪| 膨胀导致 c_vote 系统性偏低。论文未讨论替代方案（median frequency、frequency-thresholded voting、top-k entity filtering）。\n\n补充一个 R1 未提到的相关问题：entity voting 和 Soft Jaccard 在概念上有 overlap——两者都基于 entity-level 跨 sample 一致性，只是聚合方式不同。论文未讨论这两个 structural signal 之间的冗余度（e.g., 它们的 instance-level correlation 是多少？）。如果高度相关，那么 \"两个 structural signal 都优于 surface signal\" 的论证就被削弱——实际上可能是同一个 signal 的两种近似。\n\n---\n\n**[REBUT] R1-W3: ρ=0.38 被描述为 \"effective/strong\"**\n\n部分反驳。R1 的 framing 有偏差。\n\n论文实际措辞是 \"effective quality estimators\"（Section 5.3 标题, discussion.tex:1-4）和 \"strongest rank correlation\"（discussion.tex:1），而非 \"strong correlation\"。\"Strongest\" 是相对于其他信号的比较级，\"effective\" 指向实用价值。论文从未声称 ρ=0.38 在绝对意义上 \"strong\"。\n\n更重要的是，ρ 不是论文用来论证实用价值的唯一指标：AUROC=0.749（NER）和 0.706（RE）才是面向 routing/triage 应用的核心证据。AUROC 0.75 意味着 75% 的概率正确区分高/低质量 instance——这对于 \"flagging uncertain instances for human review\"（discussion.tex:15）而言是实用的。\n\n但 R1 关于缺乏 contextualization 的批评部分成立：论文未与 uncertainty estimation 文献中的其他方法（如 semantic entropy、P(True)、ensemble-based uncertainty）的 ρ 值对比。这个对比在 Related Work 中是缺失的。\n\n---\n\n**[AGREE] R1-W4: Logprob 温度敏感性数据缺失**\n\n同意。Section 5.4 (experiments.tex:132) 说 \"Signal rankings are robust across temperatures\"，但 logprob 是唯一的 per-sample signal（也是 Section 5.3 中 selection F1 最高的 signal），其 T=0.7 数据在 Limitations 中承认 \"unavailable\"（limitations.tex:15）。\n\n这不仅是一个数据缺失问题，还影响论文的核心论点：如果 logprob 在 T=0.7 时 selection 表现显著不同，那么 \"no signal reliably surpasses greedy\" 的结论可能不成立。论文至少应将 \"robust across temperatures\" 的表述限定为 \"consistency-based signals are robust across temperatures; logprob temperature sensitivity remains uncharacterized\"。\n\n---\n\n**[AGREE] R1-W5: WNUT-17 \"establishing the capability boundary\" 措辞过度**\n\n同意 R1 的统计学批评：fail to reject null ≠ accept null。p=0.106 不能 \"establish\" 一个 boundary。\n\n但补充 R1 未提到的一点：WNUT-17 上 ρ=0.082 的效应量本身（不论 p 值）已经非常小，结合 54% zero-F1 的先验信息，\"capability boundary\" 的实质结论是合理的。问题在于 statistical rhetoric——应改为 \"consistent with a capability boundary\" 或 \"suggests that signals break down\"。\n\n---\n\n**[AGREE] R1-W6: Qwen3-8B (LoRA) vs LLaMA-3.1-8B-Instruct 训练设置不对称**\n\n同意。Section 5.1 (experiments.tex:14) 说 \"Qwen3-8B (LoRA, r=32)\" 但 LLaMA-3.1-8B-Instruct 未说明是否经过 LoRA/SFT fine-tuning。如果 LLaMA 使用的是 off-the-shelf instruction-tuned model 而 Qwen 经过了 task-specific LoRA fine-tuning，那么 cross-model comparison 混淆了 model architecture 和 training strategy 两个变量。\n\n这个问题在 Table 1 的 cross-model 比较 (Δ=0.005) 和 Section 5.4 的 \"model-agnostic\" 结论中尤为突出。\n\n---\n\n**[AGREE] R1-W7: 约束解码对 sampling diversity 的影响**\n\n同意，且认为 R1 低估了这个问题的重要性。\n\n约束解码（constrained decoding via Outlines/vLLM, method.tex:5）强制输出符合预定义的 JSON/structured schema。这会显著减少 token-level 自由度，从而压缩 per-sample variance。如果 per-sample variance 被约束解码人为压低，那么 correlation-selection gap 可能部分是实验设计的 artifact 而非结构化 IE 的固有属性。\n\n具体来说：\n- Discussion (discussion.tex:12-13) 用 random baseline (0.608) 和 greedy (0.644) 的 gap (3.6 pp) 证明 \"per-instance sample variance exists\"。但这个 variance 是在约束解码下的 variance——无约束解码下可能更大。\n- 如果无约束解码产生更多样的（但可能格式不正确的）输出，selection 的 headroom 可能更大，信号的 selection 能力可能更强。\n\n论文应至少讨论这个 confound，即使无法提供无约束解码的对比实验。\n\n---\n\n### 小问题\n\n**[AGREE] Table 2 EM \"---\"**：Caption 中有解释（\"EM produces binary agreement without sample ranking\"），但 Table 2 自身缺乏脚注或更显眼的标注。\n\n**[AGREE] Logistic regression proxy**：Limitations (limitations.tex:8) 提到 \"logistic regression proxy as an upper bound\" 但正文和 Appendix 均未报告结果。要么展示结果，要么删除提及。\n\n**[AGREE] snell2024scaling bib**：bib entry 显示 \"Snell, Charlie and Lee, Jaehoon and Xu, Kelvin and Kumar, Aviral\" (ICLR 2025)。需要与 OpenAlex 交叉验证是否缺少作者。\n\n**[AGREE] Cross-model Δ=0.005 bootstrap CI**：experiments.tex:73 报告 SJ ρ=0.436 (Qwen) vs 0.431 (LLaMA) 但未报告差异是否在 CI 内。鉴于 N=16 的 3-seed std 约 0.007，Δ=0.005 几乎确定不显著，但应明确报告。\n\n**[AGREE] Introduction \"+18pp on GSM8K\" 未注明模型**：wang2023selfconsistency 的 +18pp 来自 PaLM-540B，一个与本文 8B 模型规模相差甚远的模型。不注明可能误导读者认为 +18pp 在小模型上也成立。\n\n**[AGREE] Appendix D \\textsc**：appendix.tex:102 使用 `\\textsc{Feature-Of}` 和 `\\textsc{Hyponym-Of}`，需确认编译无误（特别是连字符在 small caps 下的渲染）。\n\n---\n\n### 对 R1 主要优势的回应\n\nR1 列出的 5 点优势全部成立，我补充两点：\n\n1. **Quality estimation vs sample selection 的概念解耦**确实是本文最有价值的贡献。这个 framing 对后续工作有直接指导意义——不论负面结论（weak selectors）是否最终成立。\n2. **Conditional filtering analysis**（Appendix）是一个被忽视的亮点。它揭示了 EM 在 non-trivial subset 上的优势，并提供了 \"task difficulty determines signal choice\" 的额外证据维度。\n\n---\n\n### 对 R1 Overall Assessment 的回应\n\nR1 给出 \"Borderline → Weak Accept for Findings, Overall 3/5\"。我基本同意这个判断区间。\n\n我与 R1 的主要分歧在于问题严重程度的校准：\n- **N1 (bootstrap)**：完全同意 critical。这是最需要修复的问题。\n- **N2 (model-agnostic)**：同意需修正，但认为是 should-fix 级别（措辞修正即可），不构成 critical。\n- **N3 (RE 基础薄弱)**：同意 concern，但论文已有 conditional analysis 作为缓解，建议降为 high-warning。\n- **W7 (constrained decoding)**：R1 将此列为 warning，我认为应升级——这可能从根本上解释 correlation-selection gap，而非仅是一个遗漏的讨论点。\n\n如果 N1 bootstrap 细节补全且确认方法学正确，加上 N2 措辞修正，本文适合 Findings track。",
    "reviewer_id": "2",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 187 · 2026-05-15T02:02:54.627524+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4517
}
```

</details>

---


### Assistant

_source line 188 · 2026-05-15T02:03:04.665593+00:00_

交叉回应已提交给 Review Director。

总结：对 R1 的 3 个 Must-Fix 全部 AGREE（N1 bootstrap 细节最为关键），7 个 Should-Fix 中 6 个 AGREE、1 个 REBUT（W3 关于 ρ=0.38 "effective" 的措辞——论文实际并未称 "strong"，且 AUROC=0.75 才是实用性论据），所有小问题 AGREE。主要分歧在于问题严重程度校准：建议 N2 从 critical 降为 should-fix（措辞修正即可），W7（约束解码对 diversity 的影响）从 warning 升级——这可能是 correlation-selection gap 的根本成因而非仅是讨论遗漏。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2"
}
```

</details>

---


## Round 5

## Round 5

48 recorded events


### User

_source line 189 · 2026-05-15T02:42:55.594464+00:00_

[Round 2 审稿请求]:
## Round 2 审稿任务 — Reviewer 2（新颖性 + 完整性 + 格式）

### Venue 信息
- **目标**: EMNLP 2026 Main Conference（通过 ARR May 2026 cycle）
- **截止日期**: 2026-05-25
- **格式**: ACL 模板，long paper ≤8 页正文，double-blind
- **匿名规则**: Double-blind，无匿名期要求
- **附录**: 允许，不计页数，不保证审稿人阅读

### 论文路径
`projects/struct_self_consist_ie/docs/paper/main.tex`（sections/ 子目录含全部章节，references.bib 含 40 条引用）

### 你的审查侧重
**新颖性 + 完整性 + 格式**。重点关注：
1. **Novelty 定位**：相对于 Nedellec et al. (2026) 的增量贡献是否充分论证，"first multi-family comparison" claim 是否准确
2. **Related Work 覆盖**：是否遗漏重要相关工作（特别是 self-consistency 变体、difficulty-adaptive 方法、conformal prediction、generative self-aggregation）
3. **Claim 强度校准**：所有 claim 是否有数据支撑，ρ=0.38 是否有上下文对比，"establishing capability boundary" 等措辞是否过强
4. **写作质量**：论文结构是否清晰，符号一致性，图表可读性，引用格式
5. **ρ-AUROC dissociation 分析**：EM=1 压缩效应是否在主文充分解释
6. **Contribution 声明**：三个 contributions 是否准确反映论文实际发现
7. **引用真实性**：检查 bib 条目是否准确（特别是 nedellec2026consistency 的作者字段）

### Round 0-1 遗留 Open Issues（你需要检查是否已修复）
- **R1-N4 [critical]**: Nedellec et al. 增量贡献论证不足 + 引用作者错误——需确认 bib 是否已修正（Yao et al. vs Nédellec），增量论证是否加强
- **R0-C2 [warning]**: 相关工作遗漏——需确认是否已补充 Optimal SC、Difficulty-Adaptive SC、conformal prediction 类引用
- **R1-W3 [warning]**: ρ=0.38 缺乏 contextualization——需确认是否已补充与 semantic entropy/P(True) 等的对比
- **R1-W5 [warning]**: "establishing capability boundary" 措辞过强——需确认是否已改为 "consistent with" 或 "suggests"
- **R1-W8 [warning]**: "first systematic evaluation" claim 过强——需确认是否已收窄 scope
- **R1-W9 [warning]**: 遗漏引用——需确认 Optimal SC (2511.12309)、Difficulty-Adaptive SC (NAACL 2025)、Generative Self-Aggregation 是否已补
- **R1-W10 [warning]**: ρ-AUROC dissociation 机制分析浅——需确认 EM=1 压缩效应是否已在主文阐述
- **R1-M1 [info]**: Logistic regression proxy 提及但无结果——需确认是否已删除
- **R1-M2 [info]**: +18pp on GSM8K 未注明模型——需确认是否已补 (PaLM-540B)
- **R0-C1 [critical]**: 模型规模单一——需确认是否已消除 model-agnostic 与 Limitations 的内部矛盾
- **R0-C4 [warning]**: SJ 新颖性有限——需确认增量贡献论证是否加强

### 输出格式
按 EMNLP 审稿标准输出：Summary → Strengths → Weaknesses（分 Must-Fix / Should-Fix / Minor）→ Questions → Missing References → 对遗留 Issue 的逐条状态判定（resolved/partially/unresolved）→ Overall Score（1-5）+ Confidence（1-5）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 190 · 2026-05-15T02:43:04.688457+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
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

_source line 191 · 2026-05-15T02:43:04.739258+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 192 · 2026-05-15T02:43:08.356405+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2026 reviewer guidelines review form criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 193 · 2026-05-15T02:43:08.808773+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "projects/struct_self_consist_ie/docs/paper/**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "projects/struct_self_consist_ie/docs/paper/**/*.tex"
  }
}
```

</details>

---


### Tool result

_source line 194 · 2026-05-15T02:43:09.311354+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 195 · 2026-05-15T02:43:09.311749+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "projects/struct_self_consist_ie/docs/paper/**/*.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "projects/struct_self_consist_ie/docs/paper/**/*.bib"
  }
}
```

</details>

---


### Tool result

_source line 196 · 2026-05-15T02:43:09.763868+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 197 · 2026-05-15T02:43:09.914829+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "projects/struct_self_consist_ie/docs/paper",
  "project": "struct_self_consist_ie",
  "skip_online": "False"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "projects/struct_self_consist_ie/docs/paper",
    "project": "struct_self_consist_ie",
    "skip_online": "False"
  }
}
```

</details>

---


### Tool result

_source line 198 · 2026-05-15T02:43:19.108238+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"}]

Based on the search results, I found comprehensive information about ACL ARR 2026 reviewer guidelines and the review form criteria. Here's what I found:

## Reviewer Guidelines Overview

Reviewers are asked to follow this workflow: (1) read the paper and get the first impression, (2) search for related 
…[truncated 2154 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 10751
}
```

</details>

---


### Tool result

_source line 199 · 2026-05-15T02:43:19.108599+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"目录不存在: /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/projects/struct_self_consist_ie/docs/paper\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 9193
}
```

</details>

---


### Tool call

_source line 200 · 2026-05-15T02:43:23.526782+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/main.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/main.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 201 · 2026-05-15T02:43:23.979061+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 202 · 2026-05-15T02:43:24.537339+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/paper/**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/paper/**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 203 · 2026-05-15T02:43:24.688373+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 204 · 2026-05-15T02:43:24.688740+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
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

_source line 205 · 2026-05-15T02:43:24.739314+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 206 · 2026-05-15T02:43:31.270800+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all scoring dimensions, their scales (1-5), and descriptions. Include: Overall Assessment, Soundness, Excitement/Novelty, Reproducibility, and any other scored dimensions. List exact score descriptions (e.g., 5=outstanding, 4=good, etc.)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with all scoring dimensions, their scales (1-5), and descriptions. Include: Overall Assessment, Soundness, Excitement/Novelty, Reproducibility, and any other scored dimensions. List exact score descriptions (e.g., 5=outstanding, 4=good, etc.)"
  }
}
```

</details>

---


### Tool call

_source line 207 · 2026-05-15T02:43:31.724247+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 208 · 2026-05-15T02:43:32.176537+00:00_

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
15	\usepackage{multirow}
16	\usepackage{xcolor}
17	\usepackage{subcaption}
18	
19	\graphicspath{{figures/}}
20	
21	\title{Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence Signals for Test-Time Scaling in Information Extraction}
22	
23	\author{Anonymous}
24	
25	\begin{document}
26	\maketitle
27	
28	\input{sections/abstract}
29	\input{sections/introduction}
30	\input{sections/related_work}
31	\input{sections/method}
32	\input{sections/experiments}
33	\input{sections/discussion}
34	\input{sections/conclusion}
35	
36	\section*{Limitations}
37	\input{sections/limitations}
38	
39	\bibliography{references}
40	
41	\appendix
42	\input{sections/appendix}
43	
44	\end{document}
45	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 209 · 2026-05-15T02:43:32.177023+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 210 · 2026-05-15T02:43:33.080412+00:00_

1	\begin{abstract}
2	Test-time scaling through multi-sample generation promises quality improvements for LLM-based information extraction, but which confidence signals best serve quality estimation versus sample selection remains unclear.
3	We systematically compare five confidence signals from three families---structural (entity voting, Soft Jaccard), surface (exact match, Fleiss' $\kappa$), and model-internal (log-probability)---across NER and relation extraction on three datasets (SciERC, CoNLL-2003, WNUT-17) with two model families (Qwen3-8B, LLaMA-3.1-8B).
4	We find that the strongest signals achieve $\rho{=}0.38$ (entity voting) and AUROC${=}0.75$ (exact match) for quality estimation, with ranking and classification favoring different signals across task complexity; however, this strong quality estimation does not translate into selection gains---no signal reliably surpasses greedy decoding on either task ($p{>}0.39$, bootstrap) despite 13--18~pp of oracle headroom.
5	We term this disconnect the \textit{correlation-selection gap}: instance-level consistency signals predict which inputs the model handles reliably, not which output is best among $N$ candidates.
6	Signal rankings further depend on task difficulty---exact match dominates easy tasks, structural signals dominate hard tasks, and all signals converge when model capability is insufficient---establishing that signal choice should be guided by task difficulty and intended application.
7	These results reframe consistency signals as quality estimators rather than output selectors for structured IE.
8	\end{abstract}
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 903
}
```

</details>

---


### Tool call

_source line 211 · 2026-05-15T02:43:33.131254+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 212 · 2026-05-15T02:43:33.583689+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Self-consistency---sampling multiple outputs and aggregating them---has become a powerful strategy for improving language model reasoning.
4	On discrete-answer tasks such as arithmetic and commonsense QA, majority voting over chain-of-thought samples yields large gains: +18 percentage points on GSM8K (PaLM-540B; \citealp{wang2023selfconsistency}).
5	More broadly, test-time compute scaling through repeated sampling and selection has emerged as a complementary axis to model scaling, offering substantial quality improvements at inference time \cite{snell2024scaling, brown2024monkeys}.
6	These results rest on a shared assumption: that among $N$ stochastic samples, a selection mechanism can identify better outputs.
7	For tasks with a single correct answer, this assumption holds naturally---the majority vote is the selector.
8	But information extraction (IE) poses a fundamentally different challenge.
9	The output is not a single token or number; it is a \textit{set} of entities or relations with internal dependencies, where two samples may extract overlapping but non-identical structures.
10	There is no obvious majority to vote on, partial agreement is the norm rather than the exception, and the space of valid outputs is combinatorially large.
11	Can self-consistency still provide useful signal in this structured setting?
12	
13	Prior work on confidence estimation for LLM-based IE has conflated two distinct objectives: \textit{quality estimation} (which inputs does the model handle reliably?) and \textit{sample selection} (which of $N$ outputs is best?).
14	These require fundamentally different signal properties: the former benefits from instance-level aggregation, while the latter demands per-sample discrimination.
15	Self-consistency methods for discrete answers \cite{wang2023selfconsistency, chen2024usc} and weighted variants \cite{taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalen
…[truncated 3826 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 213 · 2026-05-15T02:43:33.584213+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 214 · 2026-05-15T02:43:34.087808+00:00_

1	\section{Method}\label{sec:method}
2	
3	\subsection{Problem Formulation}\label{sec:formulation}
4	
5	Given a language model $\mathcal{M}$ and input $x$, we sample $N$ structured outputs $\{y_1, \ldots, y_N\}$ at temperature $T > 0$ via constrained decoding \cite{willard2023guided}.
6	Each $y_i$ is an entity set (NER) or relation set (RE).
7	A confidence signal $c$ serves two purposes: (a) \textit{quality estimation}---predicting which instances the model handles reliably, and (b) \textit{sample selection}---identifying the best output among $N$ candidates.
8	
9	A \textbf{per-sample signal} scores each $y_i$ independently, $c_{\text{ps}}: (x, y_i) \to \mathbb{R}$, enabling direct candidate ranking.
10	An \textbf{instance-level signal} aggregates over all $N$ samples, $c_{\text{il}}: (x, \{y_i\}_{i=1}^N) \to \mathbb{R}$, producing a single score per input.
11	This asymmetry---between predicting \textit{which inputs} are easy and selecting \textit{which output} is best---is central to the correlation-selection gap we investigate.
12	Notation is summarized in Appendix~\ref{app:notation}.
13	
14	\subsection{Confidence Signals}\label{sec:signals}
15	
16	We compare five signals from three families: \textit{model-internal} (log-probability), \textit{surface} (exact match, Fleiss' $\kappa$), and \textit{structural} (Soft Jaccard, entity voting).
17	
18	\paragraph{Log-probability (model-internal, per-sample).}
19	The only per-sample signal.
20	For sample $y_i$ with tokens $t_1, \ldots, t_{|y_i|}$:
21	\begin{equation}\label{eq:logprob}
22	c_{\text{lp}}(y_i) = \frac{1}{|y_i|} \sum_{j=1}^{|y_i|} \log p_{\mathcal{M}}(t_j \mid t_{<j}, x)
23	\end{equation}
24	
25	\paragraph{Exact match voting (surface, instance-level).}
26	The majority fraction---the proportion of samples producing the most common output:
27	\begin{equation}\label{eq:em}
28	c_{\text{em}}(x) = \frac{1}{N} \max_{y} \big|\{i : y_i = y\}\big|
29	\end{equation}
30	
31	\paragraph{Fleiss' $\kappa$ (surface, instance-lev
…[truncated 2853 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 215 · 2026-05-15T02:43:34.088248+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 216 · 2026-05-15T02:43:34.540431+00:00_

1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Self-consistency and test-time scaling.}
4	Self-consistency decoding \cite{wang2023selfconsistency} improves reasoning by majority voting over chain-of-thought samples, assuming a discrete answer space.
5	Extensions to free-form text use LLM-based comparison \cite{chen2024usc}, atomic sub-claim decomposition \cite{thirukovalluru2024atomic}, or cross-sample hallucination detection \cite{manakul2023selfcheckgpt}.
6	For test-time scaling, \citet{snell2024scaling} characterize compute scaling laws and \citet{brown2024monkeys} show best-of-$N$ gains across tasks.
7	Recent reward-free selectors include confidence-weighted voting \cite{taubenfeld2025cisc}, KL-based self-certainty \cite{kang2025selfcertainty}, adaptive sampling \cite{kim2026reasc}, ranked aggregation \cite{wang2025rankedvoting}, and latent-space consistency \cite{oh2025latentsc}.
8	Concurrently, \citet{feng2025optimal} and \citet{wang2025make} adapt self-consistency to difficulty-aware settings, echoing our finding that signal rankings shift with task complexity; \citet{li2025llms} propose generative self-aggregation for IE but focus on output fusion rather than confidence-based selection.
9	All of the above target reasoning/QA with discrete answers or specific aggregation strategies.
10	Our work extends self-consistency to set-valued structured outputs and identifies the correlation-selection gap: strong quality estimation ($\rho{=}0.38$) coexists with selection failure ($p{>}0.39$).
11	
12	\paragraph{Consistency for structured IE.}
13	\citet{nedellec2026consistency} study consistency--accuracy correlations for LLM-based NER/RE, corroborating our quality-estimation findings.
14	However, their work differs in three key respects: (i)~it relies on surface-level matching, explicitly acknowledging it ``overlooks semantically consistent outputs''; (ii)~it evaluates only quality estimation without studying best-of-$N$ selection, leaving the correlation-s
…[truncated 2466 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 217 · 2026-05-15T02:43:34.541023+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 218 · 2026-05-15T02:43:34.993634+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Datasets.}
8	We evaluate on three English IE benchmarks spanning a difficulty gradient.
9	\textbf{SciERC} \cite{luan2018scierc} contains 551 test instances annotated for joint NER (6 types) and RE (7 types).
10	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} provides 3{,}453 test sentences with 4 entity types, where models achieve ${>}$91\% micro F1.
11	\textbf{WNUT-17} \cite{derczynski2017wnut} consists of 1{,}287 social media instances with emerging entities, used to probe method boundaries (54\% zero F1).
12	
13	\paragraph{Models and sampling.}
14	Both \textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are fine-tuned with LoRA (rank$=$32, $\alpha{=}64$) for 5 epochs using LLaMA Factory under identical training procedures, ensuring cross-model comparisons reflect architectural differences rather than training confounds.
15	We draw $N{=}8$ samples at $T{=}1.0$ (primary), with $N{=}16$ for scaling experiments.\footnote{$N{=}16$ results for CoNLL (Qwen) and SciERC (LLaMA) are in Table~\ref{tab:robustness} (Appendix~\ref{app:robustness}).}
16	Quality estimation uses Spearman $\rho$ and AUROC; downstream utility uses best-of-$N$ selection F1 with exact span matching (NER) and head-tail-label matching (RE).
17	Inference uses vLLM with constrained decoding \cite{willard2023guided}.
18	
19	%% ============================================================
20	\subsection{Quality Estimation Results}
21	\label{sec:qe_results}
22	
23	\begin{table*}[t]
24	\centering
25	\small
26	\caption{Quality estimation across tasks and models (Spearman $\rho$ and AUROC). Best value per block and column in \textbf{bold}. SciERC evaluates joint NER (6 types) and RE (7 types); CoNLL evaluates NER (4 types). Primary results use $N{=}8$, $T{=}1.0$; $N{=}16$ block reports LLaMA CoNLL 3-seed mean${\pm}$std.}
27	\label{tab:quality_estimation}
28	\begin{tabular}{ll cc cc cc cc}
…[truncated 9072 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 219 · 2026-05-15T02:43:35.044206+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 220 · 2026-05-15T02:43:35.898155+00:00_

1	\section{Discussion}\label{sec:discussion}
2	
3	\paragraph{Practical recommendations.}
4	For per-instance quality ranking, entity voting provides the strongest rank correlation ($\rho{=}0.38$, Table~\ref{tab:quality_estimation}), though exact match leads binary discrimination on SciERC (AUROC${=}0.749$).
5	When temperature or cross-condition robustness is required, SJ is preferable: its temperature sensitivity is small with bootstrap CIs including zero (Table~\ref{tab:robustness}).
6	Under conditional filtering, EM leads on both NER and RE ($\rho{=}0.360$, $0.417$), extending binary-agreement advantages to the within-capability regime.
7	Signal rankings depend on task difficulty: EM dominates on easy tasks (CoNLL, F1${>}$0.91), Voting and SJ dominate on hard tasks (SciERC, F1$\,{\approx}\,$0.66), and all signals converge when model capability is insufficient (WNUT-17).
8	This ordering is consistent across tested model families, suggesting the difficulty gradient determines which signal family is most informative.
9	Conditional filtering confirms this pattern: removing zero-F1 instances shifts effective difficulty toward the easy-task regime, and EM reclaims the lead while Voting and SJ drop substantially (Voting RE: $0.350{\to}0.241$).
10	While our NER findings are validated across three datasets, our RE conclusions rest on SciERC alone and warrant further validation.
11	
12	\paragraph{Why quality estimators fail as selectors.}
13	The four instance-level signals (Voting, SJ, FK, EM) produce a single score per input, which by construction cannot rank $N$ candidates; the consensus-proximity strategy (\S\ref{sec:evaluation}) converts them to per-sample scores, but the resulting selection performance (Table~\ref{tab:selection}) shows this conversion adds no reliable value.
14	Quality estimation ranks \textit{instances} by expected output quality; sample selection ranks \textit{candidates within a single instance}, requiring per-sample quality information that instance
…[truncated 3070 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 853
}
```

</details>

---


### Tool call

_source line 221 · 2026-05-15T02:43:35.948982+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 222 · 2026-05-15T02:43:36.551741+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	This work provides the first multi-family comparison of confidence signals for test-time scaling in generative information extraction.
4	By comparing five signals from three families---structural, surface, and model-internal---across NER and RE tasks of varying difficulty, we disentangle two objectives that prior work has conflated: quality estimation (ranking instances by expected performance) and sample selection (choosing the best output among $N$ candidates).
5	Our experiments on SciERC, CoNLL-2003, and WNUT-17 with Qwen3-8B and LLaMA-3.1-8B reveal that these objectives require fundamentally different signal properties.
6	
7	Three findings anchor our analysis.
8	First, consistency-based signals are effective quality estimators: entity voting achieves the strongest rank correlation ($\rho{=}0.38$) while exact match leads binary discrimination (AUROC${=}0.75$) on SciERC NER, with signal rankings depending on both task complexity and evaluation metric.
9	Second, the \textit{correlation-selection gap} shows that strong instance-level correlation does not yield substantial selection gains---no signal reliably surpasses greedy on either task (NER logprob: +0.6~pp, $p{=}0.39$; RE: $-$0.9~pp) despite 13--18~pp of oracle headroom---because instance-level signals cannot discriminate among candidates with similar consistency profiles.
10	Third, signal rankings depend on task difficulty: exact match leads on easy tasks, Soft Jaccard and voting lead on hard tasks, and all signals converge when model capability is insufficient.
11	This ordering is consistent across tested model families, suggesting the difficulty gradient determines which signal family is most informative.
12	While our NER findings are validated across three datasets, our RE conclusions rest on SciERC alone and warrant further validation.
13	
14	Several directions remain open.
15	Trained verifiers or reward models could close the selection gap by learning per-
…[truncated 555 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 602
}
```

</details>

---


### Tool call

_source line 223 · 2026-05-15T02:43:36.552238+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 224 · 2026-05-15T02:43:36.903739+00:00_

# ACL Rolling Review Form - Scoring Dimensions

## Overall Assessment
*Scale: 1-5*
- **5** = Consider for Award (top 2.5% papers)
- **4.5** = Borderline Award
- **4** = Conference acceptance
- **3.5** = Borderline Conference
- **3** = Findings acceptance
- **2.5** = Borderline Findings
- **2** = Resubmit next cycle
- **1.5** = Resubmit after next cycle
- **1** = Do not resubmit

## Soundness
*Scale: 1-5*
- **5** = Excellent: "most thorough" study of its type
- **4** = Strong: "sufficient support for all claims"
- **3** = Acceptable: supports main claims with minor gaps
- **2** = Poor: "major technical/methodological problems"
- **1** = Major Issues: insufficient rigor for publication

## Excitement
*Scale: 1-5*
- **5** = Highly Exciting: would recommend to others
- **4** = Exciting: would mention to colleagues
- **3** = Interesting: might discuss selectively
- **2** = Potentially Interesting: limited personal resonance
- **1** = Not Exciting: misaligned with community interests

## Reviewer Confidence
*Scale: 1-5*
- **5** = Positive evaluation is correct; familiar with related work
- **4** = Quite sure; unlikely to have missed critical details
- **3** = Pretty sure; some gaps in thoroughness possible
- **2** = Defensible but likely missed some details
- **1** = Not expert area or paper is unclear

## Reproducibility
*Scale: 1-5*
- **5** = Could easily reproduce results
- **4** = Mostly reproducible with minor variations
- **3** = Reproducible with difficulty
- **2** = "Hard pressed to reproduce"
- **1** = Cannot reproduce regardless of effort

## Datasets & Software
*Scale: 1-5 (when applicable)*
- **5** = Enabling: "should affect research project choices"
- **4** = Useful: recommendable for ongoing work
- **3** = Potentially useful to some researchers
- **2** = Documentary: useful for replication only
- **1** = No usable resources released

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 5632
}
```

</details>

---


### Tool result

_source line 225 · 2026-05-15T02:43:36.904179+00:00_

1	Our evaluation covers three datasets but only one RE benchmark (SciERC), where 44\% of instances receive zero F1, compressing the discriminable range and limiting signal differentiation for relation extraction.
2	WNUT-17 confirms the capability boundary of our approach, but our positive results on formal-domain text (CoNLL, SciERC) have not been validated on informal or noisy text where models achieve non-trivial performance.
3	
4	We evaluate two model families (Qwen3-8B and LLaMA-3.1-8B), both at 8B parameters.
5	Whether our findings---particularly the correlation-selection gap and the difficulty-dependent signal ordering, which are consistent across our two tested model families---hold for larger models (70B+) or closed-source APIs remains untested.
6	Larger models may produce higher-quality and more diverse samples, potentially altering the signal landscape.
7	
8	Our analysis of selection potential uses only unsupervised signals.
9	We do not train a dedicated verifier or reward model, leaving unknown how much of the oracle headroom a supervised approach could recover.
10	
11	We evaluate at $N{=}8$ and $N{=}16$.
12	The behavior of confidence signals at larger sample sizes (e.g., $N{=}64$ or $N{=}128$) is unknown, and $N$-scaling gains are setting-dependent: SJ improves by $+0.052$ on Qwen SciERC NER but only $+0.016$ on LLaMA SciERC NER when doubling from $N{=}8$ to $N{=}16$.
13	
14	On CoNLL with LLaMA, the SJ--FK gap is only 0.003 ($\rho{=}0.431$ vs.\ $0.428$), so the structural advantage over surface signals may not generalize to all simple-schema datasets.
15	Finally, log-probability was excluded from the temperature comparison ($T{=}0.7$ vs.\ $T{=}1.0$) due to missing $T{=}0.7$ logprob data, leaving its temperature sensitivity uncharacterized.
16	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 226 · 2026-05-15T02:43:36.904421+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 227 · 2026-05-15T02:43:37.306517+00:00_

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
21	$c_{\text{vote}}$ & Entity voting confidence \\
22	$c_{\text{lp}}$ & Log-probability (mean token log-likelihood) \\
23	\bottomrule
24	\end{tabular}
25	\caption{Notation used throughout the paper.}
26	\label{tab:notation}
27	\end{table}
28	
29	\section{Robustness Analysis}\label{app:robustness}
30	
31	\begin{table}[t]
32	\centering
33	\small
34	\caption{Signal robustness across configurations (Spearman $\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: cross-model transfer (LLaMA CoNLL $N{=}16$, 3-seed mean $\pm\sigma$). $^\dagger$Mean over 3 seeds ($\sigma{=}0.025$; individual: 0.428, 0.424, 0.384).}
35	\label{tab:robustness}
36	\begin{tabular}{llcc}
37	\toprule
38	& & NER $\rho$ & RE $\rho$ \\
39	\midrule
40	\multicolumn{4}{l}{\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\
41	\quad SJ & $T{=}0.7$ & 0.388 & 0.234 \\
42	\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\
43	\quad FK & $T{=}0.7$ & 0.321 & 0.184 \\
44	\quad FK & $T{=}1.0$ & 0.267 & 0.275 \\
45	\midrule
46	\multicolumn{4}{l}{\textit{Sample size} (Qwen SciERC, $T{=}1.0$)} \\
47	\quad SJ & $N{=}8$  & 0.360 & 0.250 \\
48	\quad SJ & $N{=}16$ & 0.412$^\dagger$ & 0.281 \\
49	\quad FK & $N{=}8$  & 0.267 & 0.275 \\
50	\quad FK & $N{=}16$ & 0.280 & 0.279 \\
51	\midrule
52	\multicolumn{4}{l}{\textit{Cross-model} (LLaMA CoNLL, $N{=}16$, 3 seeds)} \\
53	\quad SJ &  & $0.463{\pm}0.007$ & --- \\
54	\quad FK &  & $0.455{\pm}0.006$ & --- \\
55	\quad EM &  & $0.460{\pm
…[truncated 10209 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 228 · 2026-05-15T02:43:37.306971+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/paper/**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/paper/**/*.bib",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 229 · 2026-05-15T02:43:37.358322+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 230 · 2026-05-15T02:43:43.033503+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 231 · 2026-05-15T02:43:43.385552+00:00_

1	% Auto-generated from literature_map.yaml — do not edit manually
2	
3	@inproceedings{angelopoulos2021conformal,
4	  title = {Uncertainty Sets for Image Classifiers using Conformal Prediction},
5	  author = {Angelopoulos, Anastasios N. and Bates, Stephen and Malik, Jitendra and Jordan, Michael I.},
6	  booktitle = {ICLR 2021},
7	  year = {2021},
8	  url = {https://arxiv.org/abs/2009.14193}
9	}
10	
11	@article{brown2024monkeys,
12	  title = {Large Language Monkeys: Scaling Inference Compute with Repeated Sampling},
13	  author = {Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, Quoc V. and Ré, Christopher and Mirhoseini, Azalia},
14	  journal = {arXiv preprint arXiv:2407.21787},
15	  year = {2024},
16	  url = {https://arxiv.org/abs/2407.21787}
17	}
18	
19	@inproceedings{chen2024usc,
20	  title = {Universal Self-Consistency for Large Language Model Generation},
21	  author = {Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Yin, Pengcheng and Prakash, Sushant and Sutton, Charles and Wang, Xuezhi and Zhou, Denny},
22	  booktitle = {arXiv preprint (ICML 2024 Workshop ICL)},
23	  year = {2024},
24	  url = {https://arxiv.org/abs/2311.17311}
25	}
26	
27	@article{cobbe2021verifiers,
28	  title = {Training Verifiers to Solve Math Word Problems},
29	  author = {Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, Heewoo and Kaiser, Lukasz and Plappert, Matthias and Tworek, Jerry and Hilton, Jacob and Nakano, Reiichiro and Hesse, Christopher and Schulman, John},
30	  journal = {arXiv preprint arXiv:2110.14168},
31	  year = {2021},
32	  url = {https://arxiv.org/abs/2110.14168}
33	}
34	
35	@inproceedings{culotta2004confidence,
36	  title = {Confidence Estimation for Information Extraction},
37	  author = {Culotta, Aron and McCallum, Andrew},
38	  booktitle = {HLT-NAACL 2004},
39	  year = {2004},
40	  url = {https://aclanthology.org/N04-4028/}
41	}
42	
43	@inproceedings{derczynski2017wnut,
44
…[truncated 17900 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 232 · 2026-05-15T02:43:43.687325+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
  "project": "struct_self_consist_ie",
  "skip_online": "False"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
    "project": "struct_self_consist_ie",
    "skip_online": "False"
  }
}
```

</details>

---


### Tool result

_source line 233 · 2026-05-15T02:44:29.446760+00:00_

{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 49, \"total_citations\": 68, \"unique_cited_keys\": 49, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 45, \"online_not_found\": 2, \"online_mismatch\": 2}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"angelopoulos2021conformal\", \"type\": \"inproceedings\", \"title\": \"Uncertainty Sets for Image Classifiers using Conformal Prediction\", \"authors\": \"Angelopoulos, Anastasios N. and Bates, Stephen and Malik, Jitendra and Jordan, M...\", \"year\": \"2021\", \"venue\": \"ICLR 2021\"}, {\"key\": \"brown2024monkeys\", \"type\": \"article\", \"title\": \"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\", \"authors\": \"Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, ...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2407.21787\"}, {\"key\": \"chen2024usc\", \"type\": \"inproceedings\", \"title\": \"Universal Self-Consistency for Large Language Model Generation\", \"authors\": \"Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Y...\", \"year\": \"2024\", \"venue\": \"arXiv preprint (ICML 2024 Workshop ICL)\"}, {\"key\": \"cobbe2021verifiers\", \"type\": \"article\", \"title\": \"Training Verifiers to Solve Math Word Problems\", \"authors\": \"Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, ...\", \"year\": \"2021\", \"venue\": \"arXiv preprint arXiv:2110.14168\"}, {\"key\": \"culotta2004confidence\", \"type\": \"inproceedings\", \"title\": \"Confidence Estimation for Information Extraction\", \"authors\": \"Culotta, Aron and McCallum, Andrew\", \"year\": \"2004\", \"venue\": \"HLT-NAACL 2004\"}, {\"key\": \"derczynski2017wnut\", \"type\": \"inproceedings\", \"title\": \"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recogniti
…[truncated 37980 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 45759
}
```

</details>

---


### Tool call

_source line 234 · 2026-05-15T02:48:53.335714+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 — Round 2 审稿意见（新颖性 + 完整性 + 格式）\n\n### Summary\n\n本文系统比较了五种来自三个family的confidence signals（structural: entity voting, Soft Jaccard; surface: exact match, Fleiss' κ; model-internal: log-probability）在generative IE（NER + RE）中的quality estimation和sample selection表现。核心发现是\"correlation-selection gap\"：instance-level consistency signals是有效的quality estimators（ρ达0.38, AUROC达0.75），但无法可靠超越greedy decoding进行best-of-N selection（p>0.39），尽管存在13-18pp的oracle headroom。附带发现signal ranking随task difficulty变化。\n\n---\n\n### Strengths\n\n- **S1: 清晰定义的研究问题。** quality estimation与sample selection的解耦（§3.1, per-sample vs. instance-level signal）对该领域有框架性价值。\n- **S2: 统计严谨性。** Bootstrap resampling (B=10,000)、95% CI、Cohen's d、sign test、多seed验证等，远超多数同类empirical study。\n- **S3: Correlation-selection gap是genuinely useful negative result。** Table 3 + Figure 3 直观展示gap，对test-time scaling后续研究有指导价值。\n- **S4: 诚实的Limitations section。** 全文多处hedged表述（\"consistent across tested model families\"），未过度泛化。\n- **S5: Related work覆盖全面。** §2涵盖self-consistency变体、difficulty-adaptive方法、generative self-aggregation、conformal prediction、semantic uncertainty等。\n\n---\n\n### Must-Fix 问题（影响接收决定）\n\n**N1** [critical] ρ=0.38 仍缺乏跨方法数值对比（R1-W3 部分未解决）\n- 位置：§4.2 第一段（experiments.tex line 64）；§5 Discussion 第一段\n- 问题：论文将ρ=0.38 contextualize为\"14% variance explained\"和AUROC=0.749，但这是intra-study context。读者无法判断0.38在confidence estimation文献中的位置——semantic entropy (Kuhn 2023)在QA上报告AUROC通常0.75-0.85，P(True) (Kadavath 2022)也有公开ρ值。论文§2引用了这些方法但零数值对比。\n- 影响：若ρ=0.38属于typical甚至below-average，则\"effective quality estimators\"的framing需重新校准。\n- 建议：§4.2或§5加footnote，引用已有方法的典型值，明确structured IE与discrete-answer tasks直接比较的困难性。\n\n**N2** [critical] Selection实验仅在SciERC上进行，未解释CoNLL/WNUT-17的缺失\n- 位置：Table 3（experiments.tex line 96-115）\n- 问题：Best-of-N selection仅报告SciERC，但核心claim是gap在IE中普遍存在。CoNLL headroom可能极小、WNUT-17样本质量太低——但这些reasoning需要stated。\n- 影响：三数据集quality estimation → 一数据集selection验证，逻辑链不完整。\n- 建议：补充CoNLL/WNUT-17 selection结果（即使headroom为0也有信息量），或明确说明omission原因并给出oracle-greedy gap。\n\n---\n\n### Should-Fix 问题\n\n**W1** [warning] Constrained decoding作为全局confound未充分讨论\n- 位置：§5 \"Why logprob fails\" 段（discussion.tex lines 25-27）\n- 问题：constrained decoding压缩per-sample diversity的影响不仅限于logprob，可能影响所有signal的selection表现。论文仅在logprob段落提及，未在Limitations中列为key confound。\n- 建议：Limitations section明确列出，或提供per-sample F1 variance数据证明diversity已足够。\n\n**W2** [warning] Abstract \"across NER and relation extraction on three datasets\" 可能误导\n- 位置：Abstract line 3\n- 问题：RE实际仅在SciERC上评估。\n- 建议：改为\"across NER (three datasets) and RE (SciERC)\"或类似表述。\n\n**W3** [warning] WNUT-17对\"三数据集difficulty gradient\"的贡献有限\n- 位置：§4.2 line 76；Contribution 3\n- 问题：WNUT-17 SJ ρ=0.082 (p=0.106)，信号与F1的相关性不显著，本质上是negative control。\n- 建议：明确定位为\"capability boundary probe\"而非同等地位的evaluation benchmark。\n\n**W4** [warning] EM用于selection的缺失未充分解释\n- 位置：Table 3 \"---\" for EM\n- 问题：EM<1时majority output可被识别，picking majority output就是standard self-consistency voting。未解释为何不以此方式使用EM。\n- 建议：实现majority-vote selection并报告，或解释为何majority在structured IE中不well-defined。\n\n---\n\n### Minor Issues\n\n- M1: Ethics Statement section缺失（ARR不强制但建议补充）\n- M2: `hobelsberger2025systematic`和`lightman2024verify`在OpenAlex中未找到，likely是API覆盖问题而非引用错误\n- M3: `feng2025optimal` first-author mismatch为false positive（API surname/firstname混淆）\n\n---\n\n### 遗留 Issue 状态\n\n| Issue | 状态 |\n|-------|------|\n| R1-N4 bib作者+增量论证 | ✅ Resolved |\n| R0-C2 Related work遗漏 | ✅ Resolved |\n| R1-W3 ρ=0.38 context | ⚠️ Partially — intra-study OK, cross-method仍缺 |\n| R1-W5 \"establishing capability boundary\" | ✅ Resolved |\n| R1-W8 \"first systematic evaluation\" | ✅ Resolved |\n| R1-W9 遗漏引用 | ✅ Resolved |\n| R1-W10 ρ-AUROC dissociation | ✅ Resolved |\n| R1-M1 Logistic regression proxy | ✅ Resolved |\n| R1-M2 +18pp model attribution | ✅ Resolved |\n| R0-C1 模型规模单一 | ✅ Resolved（不再overclaim） |\n| R0-C4 SJ新颖性 | ⚠️ Partially — 框架转向comparison study |\n\n---\n\n### Overall Assessment\n\n**Overall**: 3.5（Borderline Conference）\n**Confidence**: 4/5\n\n| 维度 | 分数 | 理由 |\n|------|------|------|\n| Soundness | 4/5 | 实验严谨，但selection仅SciERC + constrained decoding confound |\n| Excitement | 3/5 | Gap是useful contribution，但整体为empirical study without methodological novelty |\n| Reproducibility | 4/5 | 配置明确，缺代码release承诺 |\n\n**核心判断**：方法论扎实、统计严谨的empirical study。Correlation-selection gap有价值，但ρ=0.38缺乏cross-method context、selection仅单数据集验证制约了说服力。大部分Round 0-1 issues已resolved，仅R1-W3和R0-C4 partially open。如果N1和N2得到修复，可以支持conference acceptance。",
  "reviewer_id": "2",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 — Round 2 审稿意见（新颖性 + 完整性 + 格式）\n\n### Summary\n\n本文系统比较了五种来自三个family的confidence signals（structural: entity voting, Soft Jaccard; surface: exact match, Fleiss' κ; model-internal: log-probability）在generative IE（NER + RE）中的quality estimation和sample selection表现。核心发现是\"correlation-selection gap\"：instance-level consistency signals是有效的quality estimators（ρ达0.38, AUROC达0.75），但无法可靠超越greedy decoding进行best-of-N selection（p>0.39），尽管存在13-18pp的oracle headroom。附带发现signal ranking随task difficulty变化。\n\n---\n\n### Strengths\n\n- **S1: 清晰定义的研究问题。** quality estimation与sample selection的解耦（§3.1, per-sample vs. instance-level signal）对该领域有框架性价值。\n- **S2: 统计严谨性。** Bootstrap resampling (B=10,000)、95% CI、Cohen's d、sign test、多seed验证等，远超多数同类empirical study。\n- **S3: Correlation-selection gap是genuinely useful negative result。** Table 3 + Figure 3 直观展示gap，对test-time scaling后续研究有指导价值。\n- **S4: 诚实的Limitations section。** 全文多处hedged表述（\"consistent across tested model families\"），未过度泛化。\n- **S5: Related work覆盖全面。** §2涵盖self-consistency变体、difficulty-adaptive方法、generative self-aggregation、conformal prediction、semantic uncertainty等。\n\n---\n\n### Must-Fix 问题（影响接收决定）\n\n**N1** [critical] ρ=0.38 仍缺乏跨方法数值对比（R1-W3 部分未解决）\n- 位置：§4.2 第一段（experiments.tex line 64）；§5 Discussion 第一段\n- 问题：论文将ρ=0.38 contextualize为\"14% variance explained\"和AUROC=0.749，但这是intra-study context。读者无法判断0.38在confidence estimation文献中的位置——semantic entropy (Kuhn 2023)在QA上报告AUROC通常0.75-0.85，P(True) (Kadavath 2022)也有公开ρ值。论文§2引用了这些方法但零数值对比。\n- 影响：若ρ=0.38属于typical甚至below-average，则\"effective quality estimators\"的framing需重新校准。\n- 建议：§4.2或§5加footnote，引用已有方法的典型值，明确structured IE与discrete-answer tasks直接比较的困难性。\n\n**N2** [critical] Selection实验仅在SciERC上进行，未解释CoNLL/WNUT-17的缺失\n- 位置：Table 3（experiments.tex line 96-115）\n- 问题：Best-of-N selection仅报告SciERC，但核心claim是gap在IE中普遍存在。CoNLL headroom可能极小、WNUT-17样本质量太低——但这些reasoning需要stated。\n- 影响：三数据集quality estimation → 一数据集selection验证，逻辑链不完整。\n- 建议：补充CoNLL/WNUT-17 selection结果（即使headroom为0也有信息量），或明确说明omission原因并给出oracle-greedy gap。\n\n---\n\n### Should-Fix 问题\n\n**W1** [warning] Constrained decoding作为全局confound未充分讨论\n- 位置：§5 \"Why logprob fails\" 段（discussion.tex lines 25-27）\n- 问题：constrained decoding压缩per-sample diversity的影响不仅限于logprob，可能影响所有signal的selection表现。论文仅在logprob段落提及，未在Limitations中列为key confound。\n- 建议：Limitations section明确列出，或提供per-sample F1 variance数据证明diversity已足够。\n\n**W2** [warning] Abstract \"across NER and relation extraction on three datasets\" 可能误导\n- 位置：Abstract line 3\n- 问题：RE实际仅在SciERC上评估。\n- 建议：改为\"across NER (three datasets) and RE (SciERC)\"或类似表述。\n\n**W3** [warning] WNUT-17对\"三数据集difficulty gradient\"的贡献有限\n- 位置：§4.2 line 76；Contribution 3\n- 问题：WNUT-17 SJ ρ=0.082 (p=0.106)，信号与F1的相关性不显著，本质上是negative control。\n- 建议：明确定位为\"capability boundary probe\"而非同等地位的evaluation benchmark。\n\n**W4** [warning] EM用于selection的缺失未充分解释\n- 位置：Table 3 \"---\" for EM\n- 问题：EM<1时majority output可被识别，picking majority output就是standard self-consistency voting。未解释为何不以此方式使用EM。\n- 建议：实现majority-vote selection并报告，或解释为何majority在structured IE中不well-defined。\n\n---\n\n### Minor Issues\n\n- M1: Ethics Statement section缺失（ARR不强制但建议补充）\n- M2: `hobelsberger2025systematic`和`lightman2024verify`在OpenAlex中未找到，likely是API覆盖问题而非引用错误\n- M3: `feng2025optimal` first-author mismatch为false positive（API surname/firstname混淆）\n\n---\n\n### 遗留 Issue 状态\n\n| Issue | 状态 |\n|-------|------|\n| R1-N4 bib作者+增量论证 | ✅ Resolved |\n| R0-C2 Related work遗漏 | ✅ Resolved |\n| R1-W3 ρ=0.38 context | ⚠️ Partially — intra-study OK, cross-method仍缺 |\n| R1-W5 \"establishing capability boundary\" | ✅ Resolved |\n| R1-W8 \"first systematic evaluation\" | ✅ Resolved |\n| R1-W9 遗漏引用 | ✅ Resolved |\n| R1-W10 ρ-AUROC dissociation | ✅ Resolved |\n| R1-M1 Logistic regression proxy | ✅ Resolved |\n| R1-M2 +18pp model attribution | ✅ Resolved |\n| R0-C1 模型规模单一 | ✅ Resolved（不再overclaim） |\n| R0-C4 SJ新颖性 | ⚠️ Partially — 框架转向comparison study |\n\n---\n\n### Overall Assessment\n\n**Overall**: 3.5（Borderline Conference）\n**Confidence**: 4/5\n\n| 维度 | 分数 | 理由 |\n|------|------|------|\n| Soundness | 4/5 | 实验严谨，但selection仅SciERC + constrained decoding confound |\n| Excitement | 3/5 | Gap是useful contribution，但整体为empirical study without methodological novelty |\n| Reproducibility | 4/5 | 配置明确，缺代码release承诺 |\n\n**核心判断**：方法论扎实、统计严谨的empirical study。Correlation-selection gap有价值，但ρ=0.38缺乏cross-method context、selection仅单数据集验证制约了说服力。大部分Round 0-1 issues已resolved，仅R1-W3和R0-C4 partially open。如果N1和N2得到修复，可以支持conference acceptance。",
    "reviewer_id": "2",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 235 · 2026-05-15T02:48:57.251389+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3915
}
```

</details>

---


### Assistant

_source line 236 · 2026-05-15T02:49:05.082784+00:00_

Round 2 审稿完成，已发送给 Review Director。

核心结论：

- **Overall 3.5**（Borderline Conference），Confidence 4/5
- **2个 Must-Fix**：(1) ρ=0.38仍缺乏与semantic entropy/P(True)等方法的跨方法数值对比；(2) selection实验仅SciERC一个数据集，CoNLL/WNUT-17未报告且未解释原因
- **4个 Should-Fix**：constrained decoding confound、abstract RE措辞误导、WNUT-17贡献有限、EM majority-vote selection缺失
- **遗留Issues**：11项中9项resolved，R1-W3和R0-C4 partially open
- **引用验证**：49条bib entry全部cited，0 orphan/0 missing，45条verified，2条API not_found（hobelsberger2025, lightman2024，为API覆盖问题），2条mismatch为false positive

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2"
}
```

</details>

---


## Round 6

## Round 6

4 recorded events


### User

_source line 237 · 2026-05-15T02:49:56.809519+00:00_

[Round 2 审稿请求]:
## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见

以下是 Reviewer 1 的完整审稿原文。请逐条回应：
- **[AGREE]** 同意并说明理由
- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）

---

## Reviewer 1 — Round 2 审稿意见（方法严谨性 + 实验设计）

### Must-Fix 问题

**N1** [critical] Selection 结果仅限 SciERC/Qwen，与 framing 不匹配
- 具体位置：Table 3 (Section 5.3)；Abstract ("no signal reliably surpasses greedy decoding on either task")
- 问题：论文最核心的贡献——correlation-selection gap——仅在 SciERC 上用 Qwen 验证。Quality estimation 覆盖 3 datasets × 2 models，但 selection 仅 1 dataset × 1 model。Abstract 和 Conclusion 的 framing 暗示这是跨 task/model 的 "fundamental disconnect"，但 evidence base 不支撑这一泛化。CoNLL selection 未报告（即使 headroom 小，negative result 本身也有价值），LLaMA SciERC selection 未报告。
- 建议：至少补 LLaMA SciERC selection 结果以验证 cross-model generalization；CoNLL selection 放 appendix。

**N2** [critical] WNUT-17 "capability boundary" claim 缺乏系统证据
- 具体位置：Section 5.1
- 问题：全文仅报告 SJ 一个信号的一个 ρ 值（0.082, p=0.106）。其他四个信号未报告。用一个不显著的单信号结果支撑 "all signals break down" 在逻辑上不成立。
- 建议：Appendix 增加 WNUT-17 完整 table（5 signals × ρ + AUROC）。

### Should-Fix 问题

**W1** QE ρ 在 N=8 缺乏 uncertainty quantification（Table 1 point estimates without CIs）
**W2** SJ Hungarian matching 缺 threshold 规范
**W3** RE selection 无统计检验
**W4** SciERC cross-model 不对称（LLaMA SciERC N=8 仅 2/5 signals 有数据）
**W5** n=529 vs SciERC n=551 discrepancy 未解释

### Minor Issues
- Eq.(4) 非标准 Jaccard variant 缺一句解释
- FK "independent raters" 假设不成立
- Table 1 N=8 是 single-seed 还是 averaged 未说明

### Overall: 3.5/5 (Borderline Conference / Strong Findings), Confidence: 4/5

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 238 · 2026-05-15T02:51:28.411032+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 交叉回应 — 对 Reviewer 1 Round 2 意见的逐条回应\n\n### Must-Fix\n\n**[AGREE] R1-N1: Selection 仅 SciERC/Qwen**\n同意，与我的 N2 本质相同。补充：Abstract \"either task\" 的 evidence base 实际是 1 dataset × 1 model × 2 tasks，比 R1 指出的更窄。\n\n**[AGREE] R1-N2: WNUT-17 \"all signals break down\" 仅有 SJ 单一数据点**\n同意。与我的 W3 互补。R1 的 formulation 更精准（需 5 signals 完整 table），我补充 conditional ρ（non-zero F1 subset）也应报告以排除 floor effect。\n\n### Should-Fix\n\n**[AGREE] R1-W1: N=8 ρ 无 CIs** — signal ordering 中多处 Δ=0.003-0.01，在 N=16 σ≈0.006-0.008 参照下可能 within noise。\n**[AGREE] R1-W2: SJ matching 无 threshold** — 同意并提升严重性，Eq.(4) 分母用 max 而非 union 也属非标准，需解释。\n**[AGREE] R1-W3: RE selection 无统计检验** — RE oracle headroom 18.1pp 更大，selection failure 更需 p-value。\n**[REBUT] R1-W4: LLaMA SciERC N=8 数据不全** — Table 1 CoNLL 有完整 cross-model 覆盖（5 signals, Δρ≤0.005），Appendix N=16 有 LLaMA SciERC 数据。但同意 Table 1 SciERC 列应标注 \"Qwen-only\"。\n**[AGREE] R1-W5: n=529 vs n=551** — 差额 22 instances 未解释，需 stated。\n\n### Minor — 全部同意，其中 Eq.(4) 非标准 Jaccard 应提升为 Should-Fix。\n\n### 两份审稿的共同核心\n**Selection claim evidence base 过窄**是两份审稿的共同 #1 问题（R1-N1 = R2-N2）。次要共识：WNUT-17 evidence 不足（R1-N2 ≈ R2-W3）、N=8 缺 uncertainty（R1-W1）。\n\nR1 未覆盖但我认为重要：(1) ρ=0.38 跨方法 contextualization（R2-N1），(2) constrained decoding 全局 confound（R2-W1），(3) EM majority-vote selection 缺失（R2-W4）。",
  "reviewer_id": "2",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 交叉回应 — 对 Reviewer 1 Round 2 意见的逐条回应\n\n### Must-Fix\n\n**[AGREE] R1-N1: Selection 仅 SciERC/Qwen**\n同意，与我的 N2 本质相同。补充：Abstract \"either task\" 的 evidence base 实际是 1 dataset × 1 model × 2 tasks，比 R1 指出的更窄。\n\n**[AGREE] R1-N2: WNUT-17 \"all signals break down\" 仅有 SJ 单一数据点**\n同意。与我的 W3 互补。R1 的 formulation 更精准（需 5 signals 完整 table），我补充 conditional ρ（non-zero F1 subset）也应报告以排除 floor effect。\n\n### Should-Fix\n\n**[AGREE] R1-W1: N=8 ρ 无 CIs** — signal ordering 中多处 Δ=0.003-0.01，在 N=16 σ≈0.006-0.008 参照下可能 within noise。\n**[AGREE] R1-W2: SJ matching 无 threshold** — 同意并提升严重性，Eq.(4) 分母用 max 而非 union 也属非标准，需解释。\n**[AGREE] R1-W3: RE selection 无统计检验** — RE oracle headroom 18.1pp 更大，selection failure 更需 p-value。\n**[REBUT] R1-W4: LLaMA SciERC N=8 数据不全** — Table 1 CoNLL 有完整 cross-model 覆盖（5 signals, Δρ≤0.005），Appendix N=16 有 LLaMA SciERC 数据。但同意 Table 1 SciERC 列应标注 \"Qwen-only\"。\n**[AGREE] R1-W5: n=529 vs n=551** — 差额 22 instances 未解释，需 stated。\n\n### Minor — 全部同意，其中 Eq.(4) 非标准 Jaccard 应提升为 Should-Fix。\n\n### 两份审稿的共同核心\n**Selection claim evidence base 过窄**是两份审稿的共同 #1 问题（R1-N1 = R2-N2）。次要共识：WNUT-17 evidence 不足（R1-N2 ≈ R2-W3）、N=8 缺 uncertainty（R1-W1）。\n\nR1 未覆盖但我认为重要：(1) ρ=0.38 跨方法 contextualization（R2-N1），(2) constrained decoding 全局 confound（R2-W1），(3) EM majority-vote selection 缺失（R2-W4）。",
    "reviewer_id": "2",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 239 · 2026-05-15T02:51:32.429741+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4018
}
```

</details>

---


### Assistant

_source line 240 · 2026-05-15T02:51:36.797522+00:00_

交叉回应已提交。R1 的 7 个 substantive issues 中同意 6 个、部分反驳 1 个（W4，因 CoNLL 已有完整 cross-model 覆盖且 Appendix N=16 补充了 LLaMA SciERC 数据，但同意 Table 1 标注不清）。两份审稿最大共识是 selection claim 的 evidence base 过窄。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2"
}
```

</details>

---


## Round 7

## Round 7

50 recorded events


### User

_source line 241 · 2026-05-15T03:57:41.891611+00:00_

[Round 1 审稿请求]:
你是 Reviewer 2，负责**新颖性 + 完整性 + 写作质量**。

## 审稿对象
- 论文路径：`projects/struct_self_consist_ie/docs/paper/main.tex`（分节结构，各节在 `sections/` 下）
- 目标 venue：**EMNLP 2026 Main Conference**（通过 ARR May 2026 cycle 提交）
- 截止日期：2026-05-25
- 格式：ACL 模板 `[review]`，长文 8 页正文，Limitations/Ethics 不计入页数，double-blind

## 你的审查侧重

### 1. 新颖性与贡献定位
- "First multi-family comparison of confidence signals for generative IE" 是否成立？是否有已发表工作做了类似比较？
- "Correlation-selection gap" 作为核心发现——是否真正新颖，还是 self-consistency 文献中已知的现象？
- Soft Jaccard 相对于 Nedellec (2026) 的增量贡献是否足够
- 三项 contributions 是否分别有实质性的学术价值

### 2. Related Work 覆盖
- 自查以下方向是否有重要遗漏：
  - Self-consistency / test-time scaling（2024-2026）
  - Confidence / uncertainty estimation for LLMs（2024-2026）
  - Generative IE 方法（UniNER, GoLLIE 等）
  - Structured prediction 中的 calibration 工作
- 对 Nedellec (2026) 的差异化论述是否公平准确
- 引用是否真实存在（检查是否有可疑的 hallucinated citations）

### 3. 写作质量与逻辑
- Abstract → Introduction → Contributions 的叙事是否连贯
- 论文结构是否合理（是否有冗余或缺失的 section）
- 术语使用是否一致（如 "quality estimation" vs "quality prediction"）
- Figure/Table 是否自解释、caption 是否充分
- Discussion 是否过度推断或保守不足

### 4. 格式合规
- 页数是否符合 8 页限制（请估算）
- 参考文献格式是否正确
- 匿名性是否完整（是否有泄露身份的线索：GitHub URL、acknowledgments、自引模式）
- Limitations section 是否充分（ARR 要求，desk-reject 项）
- 是否缺少 Ethics Statement

### 5. 负面结果的呈现
- "No signal reliably surpasses greedy" 是核心负面结果——呈现是否平衡
- 是否过度包装负面结果为正面贡献
- 对未来工作的建议是否具体且可行

请输出标准审稿格式：Summary → Strengths → Weaknesses（分 Must-Fix / Should-Fix / Minor） → Questions → Missing References → Score (1-10) + Confidence (1-5)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 242 · 2026-05-15T03:57:49.177761+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 243 · 2026-05-15T03:57:49.629974+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 244 · 2026-05-15T03:57:49.630386+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 245 · 2026-05-15T03:57:49.681065+00:00_

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
15	\usepackage{multirow}
16	\usepackage{xcolor}
17	\usepackage{subcaption}
18	
19	\graphicspath{{figures/}}
20	
21	\title{Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence Signals for Test-Time Scaling in Information Extraction}
22	
23	\author{Anonymous}
24	
25	\begin{document}
26	\maketitle
27	
28	\input{sections/abstract}
29	\input{sections/introduction}
30	\input{sections/related_work}
31	\input{sections/method}
32	\input{sections/experiments}
33	\input{sections/discussion}
34	\input{sections/conclusion}
35	
36	\section*{Limitations}
37	\input{sections/limitations}
38	
39	\bibliography{references}
40	
41	\appendix
42	\input{sections/appendix}
43	
44	\end{document}
45	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 246 · 2026-05-15T03:57:53.851116+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
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

_source line 247 · 2026-05-15T03:57:55.659271+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 1808
}
```

</details>

---


### Tool call

_source line 248 · 2026-05-15T03:57:55.659708+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__verify_references,mcp__agent-ml-research__review_reviewer_post_to_director",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__verify_references,mcp__agent-ml-research__review_reviewer_post_to_director",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 249 · 2026-05-15T03:57:55.710215+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 250 · 2026-05-15T03:58:00.791555+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 251 · 2026-05-15T03:58:01.799569+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 1008
}
```

</details>

---


### Tool call

_source line 252 · 2026-05-15T03:58:01.799984+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2026 reviewer guidelines review form criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 253 · 2026-05-15T03:58:02.151293+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 submission guidelines page limit format requirements"
  }
}
```

</details>

---


### Tool result

_source line 254 · 2026-05-15T03:58:09.231553+00:00_

Web search results for query: "EMNLP 2026 submission guidelines page limit format requirements"

Links: [{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Confs: 2026 Conference on Empirical Methods in Natural ...","url":"https://www.facebook.com/linguistlist/posts/confs-2026-conference-on-empirical-methods-in-natural-language-processing-emnlp-/1351983883622556/"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"EMNLP: Empirical Methods in Natural Language Processing 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=883"}]

Based on the search results, here are the EMNLP 2026 submission guidelines regarding page limits and format requirements:

## Page Limits

Long papers should be 8 pages and short papers should be 4 pages. Industry Track papers cannot exceed 6 pages in length (excluding ethical considerations and references), and references and limitations sections do not count toward the page limit.

## Format Requirements

The format is two-column with an 8-page limit for long papers and a 4-page limit for short papers. Manuscripts should be submitted electronically in PDF format and f
…[truncated 755 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7080
}
```

</details>

---


### Tool result

_source line 255 · 2026-05-15T03:58:09.583906+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"}]

I found comprehensive information about the ACL Rolling Review (ARR) 2026 reviewer guidelines and review form criteria. Here are the key details:

## Review Form Criteria

For main papers, the main criteria are soundness, while for Findings papers the main criteria are soundness and reproducibility. Con
…[truncated 1613 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7783
}
```

</details>

---


### Tool call

_source line 256 · 2026-05-15T03:58:16.370828+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 257 · 2026-05-15T03:58:16.924026+00:00_

1	\begin{abstract}
2	Test-time scaling through multi-sample generation promises quality improvements for LLM-based information extraction, but which confidence signals best serve quality estimation versus sample selection remains unclear.
3	We systematically compare five confidence signals from three families---structural (entity voting, Soft Jaccard), surface (exact match, Fleiss' $\kappa$), and model-internal (log-probability)---across NER (three datasets of varying difficulty) and RE (SciERC) with two model families (Qwen3-8B, LLaMA-3.1-8B).
4	We find that the strongest signals achieve $\rho{=}0.38$ (entity voting) and AUROC${=}0.75$ (exact match) for quality estimation, with ranking and classification favoring different signals across task complexity; however, this strong quality estimation does not translate into selection gains---no signal reliably surpasses greedy decoding in any of six tested configurations spanning two models and three datasets ($p{>}0.39$, bootstrap) despite 13--18~pp of oracle headroom.
5	We term this disconnect the \textit{correlation-selection gap}: instance-level consistency signals predict which inputs the model handles reliably, not which output is best among $N$ candidates.
6	Signal rankings further depend on task difficulty---exact match dominates easy tasks, structural signals dominate hard tasks, and when model capability is insufficient, apparent correlations are driven by zero/non-zero separation rather than genuine quality gradation---establishing that signal choice should be guided by task difficulty and intended application.
7	These results reframe consistency signals as quality estimators rather than output selectors for structured IE.
8	\end{abstract}
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 553
}
```

</details>

---


### Tool call

_source line 258 · 2026-05-15T03:58:16.974683+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 259 · 2026-05-15T03:58:17.025388+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Self-consistency---sampling multiple outputs and aggregating them---has become a powerful strategy for improving language model reasoning.
4	On discrete-answer tasks such as arithmetic and commonsense QA, majority voting over chain-of-thought samples yields large gains: +18 percentage points on GSM8K (PaLM-540B; \citealp{wang2023selfconsistency}).
5	More broadly, test-time compute scaling through repeated sampling and selection has emerged as a complementary axis to model scaling, offering substantial quality improvements at inference time \cite{snell2024scaling, brown2024monkeys}.
6	These results rest on a shared assumption: that among $N$ stochastic samples, a selection mechanism can identify better outputs.
7	For tasks with a single correct answer, this assumption holds naturally---the majority vote is the selector.
8	But information extraction (IE) poses a fundamentally different challenge.
9	The output is not a single token or number; it is a \textit{set} of entities or relations with internal dependencies, where two samples may extract overlapping but non-identical structures.
10	There is no obvious majority to vote on, partial agreement is the norm rather than the exception, and the space of valid outputs is combinatorially large.
11	Can self-consistency still provide useful signal in this structured setting?
12	
13	Prior work on confidence estimation for LLM-based IE has conflated two distinct objectives: \textit{quality estimation} (which inputs does the model handle reliably?) and \textit{sample selection} (which of $N$ outputs is best?).
14	These require fundamentally different signal properties: the former benefits from instance-level aggregation, while the latter demands per-sample discrimination.
15	Self-consistency methods for discrete answers \cite{wang2023selfconsistency, chen2024usc} and weighted variants \cite{taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalen
…[truncated 4012 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 260 · 2026-05-15T03:58:17.428478+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 261 · 2026-05-15T03:58:18.282239+00:00_

1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Self-consistency and test-time scaling.}
4	Self-consistency decoding \cite{wang2023selfconsistency} improves reasoning by majority voting over chain-of-thought samples, assuming a discrete answer space.
5	Extensions to free-form text use LLM-based comparison \cite{chen2024usc}, atomic sub-claim decomposition \cite{thirukovalluru2024atomic}, or cross-sample hallucination detection \cite{manakul2023selfcheckgpt}.
6	For test-time scaling, \citet{snell2024scaling} characterize compute scaling laws and \citet{brown2024monkeys} show best-of-$N$ gains across tasks.
7	Recent reward-free selectors include confidence-weighted voting \cite{taubenfeld2025cisc}, KL-based self-certainty \cite{kang2025selfcertainty}, adaptive sampling \cite{kim2026reasc}, ranked aggregation \cite{wang2025rankedvoting}, and latent-space consistency \cite{oh2025latentsc}.
8	Concurrently, \citet{feng2025optimal} and \citet{wang2025make} adapt self-consistency to difficulty-aware settings, echoing our finding that signal rankings shift with task complexity; \citet{li2025llms} propose generative self-aggregation for IE but focus on output fusion rather than confidence-based selection.
9	All of the above target reasoning/QA with discrete answers or specific aggregation strategies.
10	Our work extends self-consistency to set-valued structured outputs and identifies the correlation-selection gap: strong quality estimation ($\rho{=}0.38$) coexists with selection failure ($p{>}0.39$).
11	
12	\paragraph{Consistency for structured IE.}
13	\citet{nedellec2026consistency} study consistency--accuracy correlations for LLM-based NER/RE, corroborating our quality-estimation findings.
14	However, their work differs in three key respects: (i)~it relies on surface-level matching, explicitly acknowledging it ``overlooks semantically consistent outputs''; (ii)~it evaluates only quality estimation without studying best-of-$N$ selection, leaving the correlation-s
…[truncated 2466 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 853
}
```

</details>

---


### Tool call

_source line 262 · 2026-05-15T03:58:18.282631+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 263 · 2026-05-15T03:58:18.785349+00:00_

1	\section{Method}\label{sec:method}
2	
3	\subsection{Problem Formulation}\label{sec:formulation}
4	
5	Given a language model $\mathcal{M}$ and input $x$, we sample $N$ structured outputs $\{y_1, \ldots, y_N\}$ at temperature $T > 0$ via constrained decoding \cite{willard2023guided}.
6	Each $y_i$ is an entity set (NER) or relation set (RE).
7	A confidence signal $c$ serves two purposes: (a) \textit{quality estimation}---predicting which instances the model handles reliably, and (b) \textit{sample selection}---identifying the best output among $N$ candidates.
8	
9	A \textbf{per-sample signal} scores each $y_i$ independently, $c_{\text{ps}}: (x, y_i) \to \mathbb{R}$, enabling direct candidate ranking.
10	An \textbf{instance-level signal} aggregates over all $N$ samples, $c_{\text{il}}: (x, \{y_i\}_{i=1}^N) \to \mathbb{R}$, producing a single score per input.
11	This asymmetry---between predicting \textit{which inputs} are easy and selecting \textit{which output} is best---is central to the correlation-selection gap we investigate.
12	Notation is summarized in Appendix~\ref{app:notation}.
13	
14	\subsection{Confidence Signals}\label{sec:signals}
15	
16	We compare five signals from three families: \textit{model-internal} (log-probability), \textit{surface} (exact match, Fleiss' $\kappa$), and \textit{structural} (Soft Jaccard, entity voting).
17	
18	\paragraph{Log-probability (model-internal, per-sample).}
19	The only per-sample signal.
20	For sample $y_i$ with tokens $t_1, \ldots, t_{|y_i|}$:
21	\begin{equation}\label{eq:logprob}
22	c_{\text{lp}}(y_i) = \frac{1}{|y_i|} \sum_{j=1}^{|y_i|} \log p_{\mathcal{M}}(t_j \mid t_{<j}, x)
23	\end{equation}
24	
25	\paragraph{Exact match voting (surface, instance-level).}
26	The majority fraction---the proportion of samples producing the most common output:
27	\begin{equation}\label{eq:em}
28	c_{\text{em}}(x) = \frac{1}{N} \max_{y} \big|\{i : y_i = y\}\big|
29	\end{equation}
30	
31	\paragraph{Fleiss' $\kappa$ (surface, instance-lev
…[truncated 3184 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 264 · 2026-05-15T03:58:18.785730+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 265 · 2026-05-15T03:58:19.288054+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Datasets.}
8	We evaluate on three English IE benchmarks spanning a difficulty gradient.
9	\textbf{SciERC} \cite{luan2018scierc} contains 551 test instances annotated for joint NER (6 types) and RE (7 types).
10	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} provides 3{,}453 test sentences with 4 entity types, where models achieve ${\approx}$91\% micro F1.
11	\textbf{WNUT-17} \cite{derczynski2017wnut} consists of 1{,}287 social media instances with emerging entities, used to probe method boundaries (54\% zero F1).
12	
13	\paragraph{Models and sampling.}
14	Both \textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are fine-tuned with LoRA (rank$=$32, $\alpha{=}64$) for 5 epochs using LLaMA Factory under identical training procedures, ensuring cross-model comparisons reflect architectural differences rather than training confounds.
15	We draw $N{=}8$ samples at $T{=}1.0$ (primary), with $N{=}16$ for scaling experiments.\footnote{$N{=}16$ results for CoNLL (Qwen) and SciERC (LLaMA) are in Table~\ref{tab:robustness} (Appendix~\ref{app:robustness}).}
16	Quality estimation uses Spearman $\rho$ and AUROC; downstream utility uses best-of-$N$ selection F1 with exact span matching (NER) and head-tail-label matching (RE).
17	Inference uses vLLM with constrained decoding \cite{willard2023guided}.
18	
19	%% ============================================================
20	\subsection{Quality Estimation Results}
21	\label{sec:qe_results}
22	
23	\begin{table*}[t]
24	\centering
25	\small
26	\caption{Quality estimation across tasks and models (Spearman $\rho$ and AUROC). Best value per block and column in \textbf{bold}. SciERC evaluates joint NER (6 types) and RE (7 types); CoNLL evaluates NER (4 types). $N{=}8$ results use seed${=}42$; $N{=}16$ results are averaged across seeds \{42, 123, 456\}.}
27	\label{tab:quality_estimation}
28	\begin{tabular}{ll cc cc cc c
…[truncated 10971 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 266 · 2026-05-15T03:58:19.288478+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 267 · 2026-05-15T03:58:19.741384+00:00_

1	\section{Discussion}\label{sec:discussion}
2	
3	\paragraph{Practical recommendations.}
4	For per-instance quality ranking, entity voting provides the strongest rank correlation ($\rho{=}0.38$, Table~\ref{tab:quality_estimation}), though exact match leads binary discrimination on SciERC (AUROC${=}0.749$).
5	When temperature or cross-condition robustness is required, SJ is preferable: its temperature sensitivity is small with bootstrap CIs including zero (Table~\ref{tab:robustness}).
6	Under conditional filtering, EM leads on both NER and RE ($\rho{=}0.360$, $0.417$), extending binary-agreement advantages to the within-capability regime.
7	Signal rankings depend on task difficulty: EM dominates on easy tasks (CoNLL, F1${\approx}$0.91), Voting and SJ dominate on hard tasks (SciERC, F1$\,{\approx}\,$0.66), and when model capability is insufficient (WNUT-17), full-set correlations are inflated by zero/non-zero separation (Voting $\rho{=}0.724$, conditional $\rho{=}0.038$, n.s.) while all signals converge toward weak or non-significant conditional correlations.
8	This ordering is consistent across tested model families, suggesting the difficulty gradient determines which signal family is most informative.
9	Conditional filtering confirms this pattern: removing zero-F1 instances shifts effective difficulty toward the easy-task regime, and EM reclaims the lead while Voting and SJ drop substantially (Voting RE: $0.350{\to}0.241$).
10	While our NER findings are validated across three datasets, our RE conclusions rest on SciERC alone and warrant further validation.
11	
12	\paragraph{Why quality estimators fail as selectors.}
13	The four instance-level signals (Voting, SJ, FK, EM) produce a single score per input, which by construction cannot rank $N$ candidates; the consensus-proximity strategy (\S\ref{sec:evaluation}) converts them to per-sample scores, but the resulting selection performance (Table~\ref{tab:selection}) shows this conversion adds no reliable value.
14	Quali
…[truncated 3455 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 268 · 2026-05-15T03:58:19.742254+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 269 · 2026-05-15T03:58:20.646094+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	This work provides the first multi-family comparison of confidence signals for test-time scaling in generative information extraction.
4	By comparing five signals from three families---structural, surface, and model-internal---across NER and RE tasks of varying difficulty, we disentangle two objectives that prior work has conflated: quality estimation (ranking instances by expected performance) and sample selection (choosing the best output among $N$ candidates).
5	Our experiments on SciERC, CoNLL-2003, and WNUT-17 with Qwen3-8B and LLaMA-3.1-8B reveal that these objectives require fundamentally different signal properties.
6	
7	Three findings anchor our analysis.
8	First, consistency-based signals are effective quality estimators: entity voting achieves the strongest rank correlation ($\rho{=}0.38$) while exact match leads binary discrimination (AUROC${=}0.75$) on SciERC NER, with signal rankings depending on both task complexity and evaluation metric.
9	Second, the \textit{correlation-selection gap} shows that strong instance-level correlation does not yield substantial selection gains---no signal reliably surpasses greedy on either task (NER logprob: +0.6~pp, $p{=}0.39$; RE: $-$0.9~pp) despite 13--18~pp of oracle headroom---because instance-level signals cannot discriminate among candidates with similar consistency profiles.
10	Third, signal rankings depend on task difficulty: exact match leads on easy tasks, Soft Jaccard and voting lead on hard tasks, and when model capability is insufficient, inflated full-set correlations (driven by zero/non-zero separation) mask the collapse of all signals on the conditional set.
11	This ordering is consistent across tested model families, suggesting the difficulty gradient determines which signal family is most informative.
12	While our NER findings are validated across three datasets, our RE conclusions rest on SciERC alone and warrant further validation.
13	
14	Several dire
…[truncated 659 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 903
}
```

</details>

---


### Tool call

_source line 270 · 2026-05-15T03:58:20.696779+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 271 · 2026-05-15T03:58:21.199398+00:00_

1	Our evaluation covers three datasets but only one RE benchmark (SciERC), where 44\% of instances receive zero F1, compressing the discriminable range and limiting signal differentiation for relation extraction.
2	WNUT-17 confirms the capability boundary of our approach, but our positive results on formal-domain text (CoNLL, SciERC) have not been validated on informal or noisy text where models achieve non-trivial performance.
3	
4	We evaluate two model families (Qwen3-8B and LLaMA-3.1-8B), both at 8B parameters.
5	Whether our findings---particularly the correlation-selection gap and the difficulty-dependent signal ordering, which are consistent across our two tested model families---hold for larger models (70B+) or closed-source APIs remains untested.
6	Larger models may produce higher-quality and more diverse samples, potentially altering the signal landscape.
7	
8	Our analysis of selection potential uses only unsupervised signals.
9	We do not train a dedicated verifier or reward model, leaving unknown how much of the oracle headroom a supervised approach could recover.
10	
11	We evaluate at $N{=}8$ and $N{=}16$.
12	The behavior of confidence signals at larger sample sizes (e.g., $N{=}64$ or $N{=}128$) is unknown, and $N$-scaling gains are setting-dependent: SJ improves by $+0.052$ on Qwen SciERC NER but only $+0.016$ on LLaMA SciERC NER when doubling from $N{=}8$ to $N{=}16$.
13	
14	On CoNLL with LLaMA, the SJ--FK gap is only 0.003 ($\rho{=}0.431$ vs.\ $0.428$), so the structural advantage over surface signals may not generalize to all simple-schema datasets.
15	Constrained decoding (Outlines/vLLM) enforces schema compliance, potentially compressing per-sample diversity and contributing to the correlation-selection gap beyond what free-form generation would exhibit.
16	Finally, log-probability was excluded from the temperature comparison ($T{=}0.7$ vs.\ $T{=}1.0$) due to missing $T{=}0.7$ logprob data, leaving its temperature sensitivity uncharacterized.
17	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 272 · 2026-05-15T03:58:21.199738+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 273 · 2026-05-15T03:58:21.601937+00:00_

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
21	$c_{\text{vote}}$ & Entity voting confidence \\
22	$c_{\text{lp}}$ & Log-probability (mean token log-likelihood) \\
23	\bottomrule
24	\end{tabular}
25	\caption{Notation used throughout the paper.}
26	\label{tab:notation}
27	\end{table}
28	
29	\section{Robustness Analysis}\label{app:robustness}
30	
31	\begin{table}[t]
32	\centering
33	\small
34	\caption{Signal robustness across configurations (Spearman $\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: cross-model transfer (LLaMA CoNLL $N{=}16$, 3-seed mean $\pm\sigma$). $^\dagger$Mean over 3 seeds ($\sigma{=}0.025$; individual: 0.428, 0.424, 0.384).}
35	\label{tab:robustness}
36	\begin{tabular}{llcc}
37	\toprule
38	& & NER $\rho$ & RE $\rho$ \\
39	\midrule
40	\multicolumn{4}{l}{\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\
41	\quad SJ & $T{=}0.7$ & 0.388 & 0.234 \\
42	\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\
43	\quad FK & $T{=}0.7$ & 0.321 & 0.184 \\
44	\quad FK & $T{=}1.0$ & 0.267 & 0.275 \\
45	\midrule
46	\multicolumn{4}{l}{\textit{Sample size} (Qwen SciERC, $T{=}1.0$)} \\
47	\quad SJ & $N{=}8$  & 0.360 & 0.250 \\
48	\quad SJ & $N{=}16$ & 0.412$^\dagger$ & 0.281 \\
49	\quad FK & $N{=}8$  & 0.267 & 0.275 \\
50	\quad FK & $N{=}16$ & 0.280 & 0.279 \\
51	\midrule
52	\multicolumn{4}{l}{\textit{Cross-model} (LLaMA CoNLL, $N{=}16$, 3 seeds)} \\
53	\quad SJ &  & $0.463{\pm}0.007$ & --- \\
54	\quad FK &  & $0.455{\pm}0.006$ & --- \\
55	\quad EM &  & $0.460{\pm
…[truncated 14999 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 274 · 2026-05-15T03:58:23.511427+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form: all questions, rating scales (with numeric values and labels), and any instructions for reviewers. I need the exact scoring dimensions and their scales."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form: all questions, rating scales (with numeric values and labels), and any instructions for reviewers. I need the exact scoring dimensions and their scales."
  }
}
```

</details>

---


### Tool call

_source line 275 · 2026-05-15T03:58:24.318153+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 276 · 2026-05-15T03:58:29.231751+00:00_

# ACL Rolling Review Form - Complete Structure

## Main Scoring Dimensions

**Reviewer Confidence** (1-5 scale)
- "5 = Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- 4 = Quite sure with unlikely but conceivable gaps
- 3 = Pretty sure but possible missed details
- 2 = Willing to defend, fairly likely missed elements
- "1 = Not my area, or paper is very hard to understand"

**Soundness** (1-5 scale with half-point increments)
- "5 = Excellent: This study is one of the most thorough I have seen"
- 4 = Strong with sufficient claim support
- 3 = Acceptable with minor gaps
- 2 = Poor with insufficient support for main claims
- "1 = Major Issues: not yet sufficiently thorough to warrant publication"

**Excitement** (1-5 scale with half-point increments)
- "5 = Highly Exciting: I would recommend this paper to others"
- 4 = Exciting; would mention to others
- 3 = Interesting; might mention selectively
- 2 = Potentially interesting despite personal disengagement
- "1 = Not Exciting: does not resonate with me or broader community"

**Overall Assessment** (1-5 scale with half-point increments)
- 5 = Award consideration (top 2.5%)
- 4 = Conference acceptance
- 3 = Findings track
- 2 = Resubmit next cycle
- 1 = Do not resubmit

## Additional Rating Dimensions

**Reproducibility** (1-5): Easy reproduction → Unable to reproduce
**Datasets** (1-5): Enabling → No usable datasets
**Software** (1-5): Enabling → No usable software released
**Author Identity Knowledge** (1-5): Confirmed identity → No educated guess

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 5720
}
```

</details>

---


### Tool result

_source line 277 · 2026-05-15T03:59:07.542209+00:00_

{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 49, \"total_citations\": 69, \"unique_cited_keys\": 49, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 45, \"online_not_found\": 2, \"online_mismatch\": 2}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"angelopoulos2021conformal\", \"type\": \"inproceedings\", \"title\": \"Uncertainty Sets for Image Classifiers using Conformal Prediction\", \"authors\": \"Angelopoulos, Anastasios N. and Bates, Stephen and Malik, Jitendra and Jordan, M...\", \"year\": \"2021\", \"venue\": \"ICLR 2021\"}, {\"key\": \"brown2024monkeys\", \"type\": \"article\", \"title\": \"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\", \"authors\": \"Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, ...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2407.21787\"}, {\"key\": \"chen2024usc\", \"type\": \"inproceedings\", \"title\": \"Universal Self-Consistency for Large Language Model Generation\", \"authors\": \"Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Y...\", \"year\": \"2024\", \"venue\": \"arXiv preprint (ICML 2024 Workshop ICL)\"}, {\"key\": \"cobbe2021verifiers\", \"type\": \"article\", \"title\": \"Training Verifiers to Solve Math Word Problems\", \"authors\": \"Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, ...\", \"year\": \"2021\", \"venue\": \"arXiv preprint arXiv:2110.14168\"}, {\"key\": \"culotta2004confidence\", \"type\": \"inproceedings\", \"title\": \"Confidence Estimation for Information Extraction\", \"authors\": \"Culotta, Aron and McCallum, Andrew\", \"year\": \"2004\", \"venue\": \"HLT-NAACL 2004\"}, {\"key\": \"derczynski2017wnut\", \"type\": \"inproceedings\", \"title\": \"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recogniti
…[truncated 38090 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 43224
}
```

</details>

---


### Tool call

_source line 278 · 2026-05-15T03:59:26.240278+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "self-consistency structured prediction information extraction confidence LLM 2024 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "self-consistency structured prediction information extraction confidence LLM 2024 2025 2026"
  }
}
```

</details>

---


### Tool call

_source line 279 · 2026-05-15T03:59:27.345750+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"best-of-N\" selection structured output information extraction verifier 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"best-of-N\" selection structured output information extraction verifier 2024 2025"
  }
}
```

</details>

---


### Tool call

_source line 280 · 2026-05-15T03:59:27.700091+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "calibration uncertainty structured prediction sequence labeling NER 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "calibration uncertainty structured prediction sequence labeling NER 2024 2025"
  }
}
```

</details>

---


### Tool result

_source line 281 · 2026-05-15T03:59:34.731441+00:00_

Web search results for query: ""best-of-N" selection structured output information extraction verifier 2024 2025"

Links: [{"title":"SLOT: Structuring the Output of Large Language Models","url":"https://aclanthology.org/2025.emnlp-industry.32.pdf"},{"title":"Structured Outputs: Reliable Schema-Validated Data Extraction from Language Models - Interactive | Michael Brenndoerfer | Michael Brenndoerfer","url":"https://mbrenndoerfer.com/writing/structured-outputs-schema-validated-data-extraction-language-models"},{"title":"STRUCTSENSE: A TASK-AGNOSTIC AGENTIC FRAMEWORK for STRUCTURED INFORMATION EXTRACTION with HUMAN-IN-THE-LOOP EVALUATION and BENCHMARKING","url":"https://arxiv.org/html/2507.03674v1"},{"title":"Leveraging large language models for structured information extraction from pathology reports - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S2153353925001075"},{"title":"Large language models for generative information extraction: a survey | Frontiers of Computer Science | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11704-024-40555-y"},{"title":"READOC: A Unified Benchmark for Realistic Document ...","url":"https://aclanthology.org/2025.findings-acl.1128.pdf"},{"title":"Benchmarking LLM-based Information Extraction Tools for ...","url":"https://www.medrxiv.org/content/10.64898/2026.01.19.26344287v1.full.pdf"},{"title":"StructEval: Benchmarking LLMs’ Capabilities to Generate Structural Outputs","url":"https://arxiv.org/html/2505.20139v1"},{"title":"A Survey of Generative Information Extraction","url":"https://aclanthology.org/2025.coling-main.324.pdf"},{"title":"Structured data extraction from unstructured content using LLM schemas","url":"https://simonwillison.net/2025/Feb/28/llm-schemas/"}]

Based on the web search results, here are the key findings related to your query about "best-of-N" selection, structured output, information extraction, and verifier systems from 2024-2025:

## Structured Output and Info
…[truncated 1506 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7385
}
```

</details>

---


### Tool result

_source line 282 · 2026-05-15T03:59:35.284117+00:00_

Web search results for query: "self-consistency structured prediction information extraction confidence LLM 2024 2025 2026"

Links: [{"title":"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning","url":"https://arxiv.org/html/2601.02970v1"},{"title":"Confidence Improves Self-Consistency in LLMs","url":"https://arxiv.org/html/2502.06233v1"},{"title":"Towards Reliable LLM Grading Through Self-Consistency and Selective Human Review: Higher Accuracy, Less Work","url":"https://www.mdpi.com/2504-4990/8/3/74"},{"title":"Confidence Improves Self-Consistency in LLMs","url":"https://aclanthology.org/2025.findings-acl.1030.pdf"},{"title":"[2502.06233] Confidence Improves Self-Consistency in LLMs","url":"https://arxiv.org/abs/2502.06233"},{"title":"Confidence Improves Self-Consistency in LLMs - ACL Anthology","url":"https://aclanthology.org/2025.findings-acl.1030/"},{"title":"Self-Consistency Sampling in LLMs","url":"https://www.emergentmind.com/topics/self-consistency-sampling"},{"title":"Stability Evaluation of Confidence Features Across Model and Data Variants in Large Language Models — Research and Science Today","url":"https://www.rstjournal.com/article/4.2026"},{"title":"GitHub - IAAR-Shanghai/ICSFSurvey: Explore concepts like Self-Correct, Self-Refine, Self-Improve, Self-Contradict, Self-Play, and Self-Knowledge, alongside o1-like reasoning elevation🍓 and hallucination alleviation🍄.","url":"https://github.com/IAAR-Shanghai/ICSFSurvey"},{"title":"THE PATH OF LEAST RESISTANCE: GUIDING LLM REASONING TRAJECTORIES WITH PREFIX CONSENSUS | OpenReview","url":"https://openreview.net/forum?id=hrnSqERgPn"}]

Here are the search results for your query on self-consistency, structured prediction, information extraction, confidence, and LLM developments from 2024-2026:

## Key Recent Developments

### Confidence-Informed Self-Consistency (CISC)

Confidence-Informed Self-Consistency (CISC) performs a weighted majority vote based on confidence scores obtai
…[truncated 1992 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 9043
}
```

</details>

---


### Tool result

_source line 283 · 2026-05-15T03:59:40.608213+00:00_

Web search results for query: "calibration uncertainty structured prediction sequence labeling NER 2024 2025"

Links: [{"title":"Uncertainty Quantification for Named Entity Recognition via Full-Sequence and Subsequence Conformal Prediction","url":"https://arxiv.org/html/2601.16999"},{"title":"Calibrating Language Models for Neural Ranking under ...","url":"https://aclanthology.org/2025.uncertainlp-main.22.pdf"},{"title":"Calibrating Structured Output Predictors for Natural Language Processing - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC7890517/"},{"title":"Uncertainty Quantification and Confidence Calibration in Large","url":"https://xiao0o0o.github.io/2025KDD_tutorial/survey.pdf"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/b94d8b035e2183e47afef9e2f299ba47-Paper-Conference.pdf"},{"title":"Uncertainty Estimation on Sequential Labeling via ... - People","url":"https://people.cs.vt.edu/~clu/Publication/2024/NAACL-Findings-2024-He.pdf"},{"title":"Uncertainty Quantification and Confidence Calibration in ...","url":"https://arxiv.org/pdf/2503.15850"},{"title":"Published as a conference paper at ICLR 2025 DO LLMS ESTIMATE UNCERTAINTY WELL","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/ef472869c217bf693f2d9bbde66a6b07-Paper-Conference.pdf"},{"title":"Calibrated Structured Prediction - Stanford Computer Science","url":"https://cs.stanford.edu/~pliang/papers/calibration-nips2015.pdf"},{"title":"Calibration in Deep Learning: A Survey of the State-of-the-Art Cheng Wang","url":"https://arxiv.org/pdf/2308.01222"}]

I've performed the web search and found several highly relevant recent papers and resources on this topic. Here are the key findings:

## Recent Work (2024-2025)

Combining deep sequence-labeling architectures with distribution-free uncertainty quantification illustrates how formal statistical inference can strengthen the reliability and interpretability of AI system
…[truncated 1657 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 12908
}
```

</details>

---


### Tool call

_source line 284 · 2026-05-15T03:59:55.889869+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"correlation selection gap\" OR \"quality estimation vs selection\" self-consistency LLM sampling 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"correlation selection gap\" OR \"quality estimation vs selection\" self-consistency LLM sampling 2024 2025"
  }
}
```

</details>

---


### Tool call

_source line 285 · 2026-05-15T03:59:56.145544+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "VerifiNER verification augmented NER LLM 2024 ACL"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "VerifiNER verification augmented NER LLM 2024 ACL"
  }
}
```

</details>

---


### Tool result

_source line 286 · 2026-05-15T04:00:03.384288+00:00_

Web search results for query: ""correlation selection gap" OR "quality estimation vs selection" self-consistency LLM sampling 2024 2025"

Links: [{"title":"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning","url":"https://arxiv.org/html/2601.02970v1"},{"title":"NeurIPS Poster Scalable Best-of-N Selection for Large Language Models via Self-Certainty","url":"https://neurips.cc/virtual/2025/poster/120166"},{"title":"Reasoning Aware Self-Consistency: Leveraging Reasoning Paths for Efficient LLM Sampling - ACL Anthology","url":"https://aclanthology.org/2025.naacl-long.184/"},{"title":"Self-Consistency Sampling in LLMs","url":"https://www.emergentmind.com/topics/self-consistency-sampling"},{"title":"Towards Reliable LLM Grading Through Self-Consistency and Selective Human Review: Higher Accuracy, Less Work","url":"https://www.mdpi.com/2504-4990/8/3/74"},{"title":"Estimating LLM Consistency: A User Baseline vs Surrogate ...","url":"https://aclanthology.org/2025.emnlp-main.1554.pdf"},{"title":"Leveraging Reasoning Paths for Efficient LLM Sampling","url":"https://aclanthology.org/2025.naacl-long.184.pdf"},{"title":"Confidence Improves Self-Consistency in LLMs","url":"https://aclanthology.org/2025.findings-acl.1030.pdf"},{"title":"Reasoning Aware Self-Consistency: Leveraging Reasoning Paths for Efficient LLM Sampling | Request PDF","url":"https://www.researchgate.net/publication/392503883_Reasoning_Aware_Self-Consistency_Leveraging_Reasoning_Paths_for_Efficient_LLM_Sampling"},{"title":"Confidence Improves Self-Consistency in LLMs","url":"https://arxiv.org/pdf/2502.06233"}]

Based on the search results, I found several relevant recent papers addressing correlations between quality estimation and selection in self-consistency LLM sampling from 2024-2025:

## Key Findings

**Self-Certainty and Quality Estimation:**
Self-certainty is a novel metric that leverages the inherent probability distribution of LLM outputs to estimate response quality wi
…[truncated 1449 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7494
}
```

</details>

---


### Tool result

_source line 287 · 2026-05-15T04:00:03.736244+00:00_

Web search results for query: "VerifiNER verification augmented NER LLM 2024 ACL"

Links: [{"title":"VerifiNER: Verification-augmented NER via Knowledge-grounded Reasoning with Large Language Models - ACL Anthology","url":"https://aclanthology.org/2024.acl-long.134/"},{"title":"[Quick Review] VerifiNER: Verification-augmented NER via Knowledge-grounded Reasoning with Large Language Models","url":"https://liner.com/review/verifiner-verificationaugmented-ner-via-knowledgegrounded-reasoning-with-large-language-models"},{"title":"Accepted Main Conference Papers - ACL 2024","url":"https://2024.aclweb.org/program/main_conference_papers/"},{"title":"GitHub - emseoyk/VerifiNER","url":"https://github.com/emseoyk/verifiner"},{"title":"VerifiNER: Verification-augmented NER via Knowledge-grounded Reasoning with Large Language Models | Request PDF","url":"https://www.researchgate.net/publication/384213955_VerifiNER_Verification-augmented_NER_via_Knowledge-grounded_Reasoning_with_Large_Language_Models"},{"title":"Math-Shepherd: Verify and Reinforce LLMs Step-by- ...","url":"https://aclanthology.org/2024.acl-long.510.pdf"},{"title":"LLatrieval: LLM-Verified Retrieval for Verifiable Generation - ACL Anthology","url":"https://aclanthology.org/2024.naacl-long.305/"},{"title":"When Does Verification Pay Off? A Closer Look at LLMs as Solution Verifiers","url":"https://www.arxiv.org/pdf/2512.02304"},{"title":"Provenance: A Light-weight Fact-checker for Retrieval Augmented LLM Generation Output - ACL Anthology","url":"https://aclanthology.org/2024.emnlp-industry.97/"},{"title":"Chain-of-Verification Reduces Hallucination in Large ...","url":"https://aclanthology.org/2024.findings-acl.212.pdf"}]

I've found comprehensive information about VerifiNER. Here's a summary of the search results:

## VerifiNER: Verification-augmented NER with LLMs (ACL 2024)

VerifiNER is a paper titled "Verification-augmented NER via Knowledge-grounded Reasoning with Large Language Models" that was presented at 
…[truncated 1380 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7590
}
```

</details>

---


### Tool call

_source line 288 · 2026-05-15T04:03:08.754958+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 审稿意见：Strong Predictors, Weak Selectors\n\n### Summary\n\n本文系统比较了三个 family（structural / surface / model-internal）的五种 confidence signal 在 generative IE（NER + RE）上的 quality estimation 和 sample selection 性能。核心发现是 correlation-selection gap：instance-level consistency signal 能预测哪些输入模型处理得好（ρ 最高 0.38, AUROC 最高 0.75），但无法在 best-of-N selection 中可靠超越 greedy decoding（p>0.39），尽管存在 13–18pp 的 oracle headroom。\n\n---\n\n### Strengths\n\n- **S1**: Quality estimation 与 sample selection 的问题分解有真正洞察力，将先前工作混淆的两个目标清晰剥离\n- **S2**: 实验方法论严谨：paired bootstrap (B=10,000)、多 seed、proper CI、Cohen's d、sign test\n- **S3**: WNUT-17 分析揭示 inflated correlation 由 zero/non-zero boundary 驱动（Voting ρ=0.724 → conditional ρ=0.038, n.s.），是重要的 methodological warning\n- **S4**: 负面结果处理诚实 balanced，Limitations 坦率承认多项局限\n- **S5**: 论文结构和叙事流畅\n- **S6**: Robustness 分析覆盖 temperature、N-scaling、cross-model\n\n---\n\n### Must-Fix (Critical)\n\n**N1** [critical] RE 结论建立在单一 benchmark 上且受严重 floor effect 影响\n- SciERC RE 44% zero F1，gap 的 RE 证据（-0.9pp, p=0.80）基础薄弱\n- 一个 dataset + 严重 floor effect 不足以支撑 generalized conclusion\n- 建议增加 RE benchmark 或显著降低 RE claim 强度\n\n**N2** [critical] Logprob 失败缺乏实证解释\n- 4 个 instance-level signal 无法 select 在定义上 expected；logprob 作为唯一 per-sample signal 为什么也失败才是关键问题\n- Discussion 的 \"constrained decoding 压缩 diversity\" 解释是猜测性的\n- 如果 gap 来自实验设置 artifact 而非结构化 IE 固有属性，核心 claim 需要重新审视\n- 建议报告 per-sample logprob variance、unique output fraction、或比较 constrained vs. unconstrained decoding\n\n**N3** [critical] 缺少 Ethics Statement\n- ARR review form 明确要求 reviewer 评估 ethical considerations，缺失是格式问题\n\n---\n\n### Should-Fix (Warning)\n\n**W1** \"First multi-family comparison\" claim 边界需更精确限定，与 CoCoA、CISC 等 existing multi-signal comparison 的差异应更明确\n**W2** Soft Jaccard 增量贡献 borderline（vs. Voting Δρ CI 包含零，vs. EM borderline significant CI lower bound +0.003）\n**W3** ρ–AUROC dissociation 是 expected statistical behavior，不应作为独立发现过度强调\n**W4** 术语不一致：\"confidence signal\" vs \"consistency signal\"、\"VC\" vs \"Voting Conf.\"、LLaMA Factory 未引用\n**W5** Related Work 遗漏：VerifiNER (ACL 2024)、RASC (NAACL 2025)\n\n---\n\n### Minor Issues\n\n- Abstract 中 \"oracle headroom\" 此时无定义\n- 对 Nedellec (2026) 措辞偏 adversarial\n- FK independent raters 假设的 justification 不足\n- Table 2 EM omission 需 unique output fraction 数据支持\n\n---\n\n### Missing References\n\n1. Kim et al. (2024) \"VerifiNER\" — ACL 2024\n2. Aggarwal et al. (2025) \"Reasoning Aware Self-Consistency\" — NAACL 2025\n3. He et al. (2024) \"Uncertainty Estimation on Sequential Labeling\" — NAACL Findings 2024\n\n---\n\n### Scores\n\n| 维度 | 分数 | 理由 |\n|------|------|------|\n| Overall | 3.0/5 | Findings track |\n| Soundness | 3.5/5 | NER 扎实，RE 单 dataset + constrained decoding confound 未 disentangle |\n| Excitement | 3.0/5 | 概念贡献有价值但 partially obvious + 无 positive path forward |\n| Reproducibility | 4.0/5 | 方法详细、公开 benchmark/model，但代码公开未提及 |\n| Confidence | 4/5 | 熟悉相关文献 |\n\n**一句话**：方法论严谨的 empirical study，correlation-selection gap 有概念价值，但 RE 证据薄弱 + logprob 失败解释缺乏实证，适合 Findings 而非 Main。",
  "reviewer_id": "2",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 审稿意见：Strong Predictors, Weak Selectors\n\n### Summary\n\n本文系统比较了三个 family（structural / surface / model-internal）的五种 confidence signal 在 generative IE（NER + RE）上的 quality estimation 和 sample selection 性能。核心发现是 correlation-selection gap：instance-level consistency signal 能预测哪些输入模型处理得好（ρ 最高 0.38, AUROC 最高 0.75），但无法在 best-of-N selection 中可靠超越 greedy decoding（p>0.39），尽管存在 13–18pp 的 oracle headroom。\n\n---\n\n### Strengths\n\n- **S1**: Quality estimation 与 sample selection 的问题分解有真正洞察力，将先前工作混淆的两个目标清晰剥离\n- **S2**: 实验方法论严谨：paired bootstrap (B=10,000)、多 seed、proper CI、Cohen's d、sign test\n- **S3**: WNUT-17 分析揭示 inflated correlation 由 zero/non-zero boundary 驱动（Voting ρ=0.724 → conditional ρ=0.038, n.s.），是重要的 methodological warning\n- **S4**: 负面结果处理诚实 balanced，Limitations 坦率承认多项局限\n- **S5**: 论文结构和叙事流畅\n- **S6**: Robustness 分析覆盖 temperature、N-scaling、cross-model\n\n---\n\n### Must-Fix (Critical)\n\n**N1** [critical] RE 结论建立在单一 benchmark 上且受严重 floor effect 影响\n- SciERC RE 44% zero F1，gap 的 RE 证据（-0.9pp, p=0.80）基础薄弱\n- 一个 dataset + 严重 floor effect 不足以支撑 generalized conclusion\n- 建议增加 RE benchmark 或显著降低 RE claim 强度\n\n**N2** [critical] Logprob 失败缺乏实证解释\n- 4 个 instance-level signal 无法 select 在定义上 expected；logprob 作为唯一 per-sample signal 为什么也失败才是关键问题\n- Discussion 的 \"constrained decoding 压缩 diversity\" 解释是猜测性的\n- 如果 gap 来自实验设置 artifact 而非结构化 IE 固有属性，核心 claim 需要重新审视\n- 建议报告 per-sample logprob variance、unique output fraction、或比较 constrained vs. unconstrained decoding\n\n**N3** [critical] 缺少 Ethics Statement\n- ARR review form 明确要求 reviewer 评估 ethical considerations，缺失是格式问题\n\n---\n\n### Should-Fix (Warning)\n\n**W1** \"First multi-family comparison\" claim 边界需更精确限定，与 CoCoA、CISC 等 existing multi-signal comparison 的差异应更明确\n**W2** Soft Jaccard 增量贡献 borderline（vs. Voting Δρ CI 包含零，vs. EM borderline significant CI lower bound +0.003）\n**W3** ρ–AUROC dissociation 是 expected statistical behavior，不应作为独立发现过度强调\n**W4** 术语不一致：\"confidence signal\" vs \"consistency signal\"、\"VC\" vs \"Voting Conf.\"、LLaMA Factory 未引用\n**W5** Related Work 遗漏：VerifiNER (ACL 2024)、RASC (NAACL 2025)\n\n---\n\n### Minor Issues\n\n- Abstract 中 \"oracle headroom\" 此时无定义\n- 对 Nedellec (2026) 措辞偏 adversarial\n- FK independent raters 假设的 justification 不足\n- Table 2 EM omission 需 unique output fraction 数据支持\n\n---\n\n### Missing References\n\n1. Kim et al. (2024) \"VerifiNER\" — ACL 2024\n2. Aggarwal et al. (2025) \"Reasoning Aware Self-Consistency\" — NAACL 2025\n3. He et al. (2024) \"Uncertainty Estimation on Sequential Labeling\" — NAACL Findings 2024\n\n---\n\n### Scores\n\n| 维度 | 分数 | 理由 |\n|------|------|------|\n| Overall | 3.0/5 | Findings track |\n| Soundness | 3.5/5 | NER 扎实，RE 单 dataset + constrained decoding confound 未 disentangle |\n| Excitement | 3.0/5 | 概念贡献有价值但 partially obvious + 无 positive path forward |\n| Reproducibility | 4.0/5 | 方法详细、公开 benchmark/model，但代码公开未提及 |\n| Confidence | 4/5 | 熟悉相关文献 |\n\n**一句话**：方法论严谨的 empirical study，correlation-selection gap 有概念价值，但 RE 证据薄弱 + logprob 失败解释缺乏实证，适合 Findings 而非 Main。",
    "reviewer_id": "2",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 289 · 2026-05-15T04:03:12.678015+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3923
}
```

</details>

---


### Assistant

_source line 290 · 2026-05-15T04:03:19.100049+00:00_

审稿意见已提交给 Review Director。

核心判断：**Overall 3.0/5（Findings track）**。论文方法论严谨、correlation-selection gap 概念有价值，但三个 critical 问题影响接收——RE 仅一个 benchmark 且 floor effect 严重、logprob 失败的 constrained decoding 解释缺乏实证（可能是 artifact）、缺少 Ethics Statement。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2"
}
```

</details>

---


## Round 8

## Round 8

4 recorded events


### User

_source line 291 · 2026-05-15T04:06:32.609104+00:00_

[Round 1 审稿请求]:
## 交叉分享：Reviewer 1 的完整审稿意见

请逐条回应以下 Reviewer 1 的审稿意见。对每个 Must-Fix、Should-Fix 和 Minor Issue：
- **[AGREE]** 同意并说明理由
- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）

---

以下是 Reviewer 1 的完整审稿原文：

### Summary
本文系统比较了生成式信息抽取（IE）中五种置信度信号用于质量估计和样本选择两个不同目标的表现。核心发现是"correlation-selection gap"：一致性信号在实例级质量估计上有效（ρ 最高 0.38，AUROC 最高 0.75），但用于 best-of-N 选择时没有任何信号能显著超过 greedy decoding（p>0.39），尽管存在 13–18pp 的 oracle headroom。论文还发现信号排序依赖于任务难度。

### Strengths
- S1: 清晰的问题分解与严谨的框架设计（per-sample vs. instance-level 形式化）
- S2: 全面的统计报告（Bootstrap B=10,000 + CI + Cohen's d + sign test）
- S3: 诚实的 scope limitation 声明（RE 单数据集在 4 处明确提及）
- S4: Task difficulty 分析有洞察力（EM vs. SJ crossover）
- S5: Soft Jaccard 信号设计合理（type-aware Hungarian matching + token-level IoU）

### Must-Fix (Critical)
**N1** [critical] Constrained decoding 是 correlation-selection gap 的未控制混淆变量
- 论文核心发现"no signal reliably surpasses greedy"可能部分是 constrained decoding（Outlines/vLLM）压缩 per-sample diversity 的产物
- Random baseline gap 仅 3.6pp，可能远低于 unconstrained generation 的 variance
- 建议增加 unconstrained generation 对照或量化 constrained decoding 下的实际 diversity level

**N2** [critical] "No signal reliably surpasses greedy" 的统计论证逻辑不完整——failure to reject ≠ evidence of absence
- p>0.39 只是 absence of evidence，不是 evidence of absence
- CI 范围 [−3.0, +4.2] 不能排除有意义的选择增益
- 建议补充等价性检验（TOST）或 power analysis

**N3** [critical] N=8 主要结果仅使用单一 seed（seed=42），缺乏可靠性验证
- Table 1 N=8 和 Table 2 全部基于 single random seed
- N=16 的 3-seed σ 约 0.003-0.008 暗示 N=8 的方差可能更大
- 信号排序差异很小（Voting vs. SJ Δρ=0.019，CI 含零），single-seed 无法确认稳定性

### Should-Fix (Warning)
**W1** 多重比较校正缺失（SJ–EM borderline significant 在任何 correction 下不会 survive）
**W2** "Correlation-selection gap" 部分为 tautological（4/5 instance-level 信号 by design 无法 per-sample 区分）
**W3** FK 独立性假设未经验证（温度采样非独立）
**W4** SJ 定义中 Hungarian matching 的 cost function 未明确（max IoU? 允许 zero-IoU match?）
**W5** "Cross-model" 实为 cross-architecture at fixed 8B scale
**W6** Consensus-proximity 是唯一 instance-to-sample 转换策略，未比较替代方案（如 MBR decoding）

### Minor Issues
**M1** WNUT-17 "54% zero F1" vs Table 7 显示 51.5%，数据不一致
**M2** Table 1 N=16 区域大面积空白
**M3** EM selection 排除理由缺乏经验支持
**M4** LOO-SJ Δρ 和 per-instance Δρ 量纲不同
**M5** Figure 1 caption 引入 figure 未直接呈现的 p=0.39
**M6** Semantic entropy footnote 比较既然不可比就不应出现
**M7** 引用格式细节

### Questions to Authors
Q1: 是否考虑过 unconstrained generation 作为对照？
Q2: Logprob 在 WNUT conditional set 最高 ρ=0.350，如何 reconcile "logprob 最弱"？
Q3: LoRA rank=32 是否影响 sample diversity？
Q4: N=16 selection 结果有无 multi-seed bootstrap p-value？

### Missing References
- MBR decoding: Eikema & Aziz (2022), Freitag et al. (2022)
- Structured prediction uncertainty: Malinin & Gales (2021)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 292 · 2026-05-15T04:09:17.476026+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 交叉回应 Reviewer 1\n\n### Must-Fix\n\n[AGREE] R1-N1 (constrained decoding confound): 同意，与我的 N2 一致。补充建议：即使不跑 unconstrained 实验，报告 unique output fraction 和 per-sample logprob variance 也能大幅帮助 disentangle。\n\n[REBUT] R1-N2 (failure to reject ≠ evidence of absence): 统计原理正确，但 6/6 configurations 一致未显著（Table 4），cumulative evidence 远强于单一 test。且 CI 正面端仅 +4.2pp vs 13.2pp oracle headroom，practical significance 有限。建议降为 Should-Fix。\n\n[AGREE] R1-N3 (single seed): 合理关切。但 N=16 3-seed 下 signal rankings 完全一致（Table 3），且 N=8→N=16 ranking 也稳定——ordering 稳定性有保障。建议降为 Should-Fix。\n\n### Should-Fix\n\n[AGREE] R1-W1 (多重比较): SJ-EM CI lower bound +0.003，Bonferroni 下几乎必然不 survive。\n[AGREE] R1-W2 (tautological gap): 与我观点一致。4/5 instance-level signals 的 selection 失败是 definitional，真正的 empirical contribution 应聚焦 logprob 失败和 consensus-proximity 局限。\n[AGREE] R1-W3 (FK independence): 同意。\n[AGREE] R1-W4 (SJ cost function): 同意需补充 maximize/minimize 方向和 unmatched entities 处理。\n[AGREE] R1-W5 (cross-model at fixed 8B): 同意。\n[AGREE] R1-W6 (consensus-proximity 唯一策略): 强烈同意，这是 R1 最有力的 Should-Fix。MBR decoding 是成熟替代方案，仅测试一种转换策略就声称 \"signals fail as selectors\" 不充分。\n\n### Minor\n\n[AGREE] R1-M1 (54% vs 51.5%): 数据不一致。\n[AGREE] R1-M2 (Table 1 空白): 建议移至 Appendix。\n[AGREE] R1-M3 (EM exclusion): 同意需 empirical support。\n[AGREE] R1-M4 (LOO-SJ 量纲): 同意表述混淆。\n[REBUT] R1-M5 (Figure 1 p=0.39): Overview figure caption 引用 supporting statistic 是常见做法，建议保留但加 \"(Table 2)\" 交叉引用。\n[REBUT] R1-M6 (semantic entropy footnote): 该 footnote 提供重要 calibration context 且已显式 caveat，删除反而让读者缺少 reference point。建议强化 caveat placement 但保留。\n[AGREE] R1-M7 (引用格式): 同意。\n\n### Missing References\n[AGREE] MBR decoding (Eikema & Aziz 2022; Freitag et al. 2022) — 直接相关 W6，significant gap。\n[AGREE] Malinin & Gales (2021) — 相关于 uncertainty estimation。\n\n### 综合评价\nR1 的审稿意见质量高，技术判断准确。我们的分歧主要在严重程度而非方向上：\n- R1-N2 (statistical logic): 我认为 should-fix 而非 critical，因 6/6 配置一致性提供了 cumulative evidence\n- R1-N3 (single seed): 我认为 should-fix 因 ranking stability 有保障\n- R1-W6 (MBR alternative): 我认为这是 R1 最有价值的贡献点，论文确实只测了一种 instance-to-sample 转换策略就做了 sweeping claim",
  "reviewer_id": "2",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 交叉回应 Reviewer 1\n\n### Must-Fix\n\n[AGREE] R1-N1 (constrained decoding confound): 同意，与我的 N2 一致。补充建议：即使不跑 unconstrained 实验，报告 unique output fraction 和 per-sample logprob variance 也能大幅帮助 disentangle。\n\n[REBUT] R1-N2 (failure to reject ≠ evidence of absence): 统计原理正确，但 6/6 configurations 一致未显著（Table 4），cumulative evidence 远强于单一 test。且 CI 正面端仅 +4.2pp vs 13.2pp oracle headroom，practical significance 有限。建议降为 Should-Fix。\n\n[AGREE] R1-N3 (single seed): 合理关切。但 N=16 3-seed 下 signal rankings 完全一致（Table 3），且 N=8→N=16 ranking 也稳定——ordering 稳定性有保障。建议降为 Should-Fix。\n\n### Should-Fix\n\n[AGREE] R1-W1 (多重比较): SJ-EM CI lower bound +0.003，Bonferroni 下几乎必然不 survive。\n[AGREE] R1-W2 (tautological gap): 与我观点一致。4/5 instance-level signals 的 selection 失败是 definitional，真正的 empirical contribution 应聚焦 logprob 失败和 consensus-proximity 局限。\n[AGREE] R1-W3 (FK independence): 同意。\n[AGREE] R1-W4 (SJ cost function): 同意需补充 maximize/minimize 方向和 unmatched entities 处理。\n[AGREE] R1-W5 (cross-model at fixed 8B): 同意。\n[AGREE] R1-W6 (consensus-proximity 唯一策略): 强烈同意，这是 R1 最有力的 Should-Fix。MBR decoding 是成熟替代方案，仅测试一种转换策略就声称 \"signals fail as selectors\" 不充分。\n\n### Minor\n\n[AGREE] R1-M1 (54% vs 51.5%): 数据不一致。\n[AGREE] R1-M2 (Table 1 空白): 建议移至 Appendix。\n[AGREE] R1-M3 (EM exclusion): 同意需 empirical support。\n[AGREE] R1-M4 (LOO-SJ 量纲): 同意表述混淆。\n[REBUT] R1-M5 (Figure 1 p=0.39): Overview figure caption 引用 supporting statistic 是常见做法，建议保留但加 \"(Table 2)\" 交叉引用。\n[REBUT] R1-M6 (semantic entropy footnote): 该 footnote 提供重要 calibration context 且已显式 caveat，删除反而让读者缺少 reference point。建议强化 caveat placement 但保留。\n[AGREE] R1-M7 (引用格式): 同意。\n\n### Missing References\n[AGREE] MBR decoding (Eikema & Aziz 2022; Freitag et al. 2022) — 直接相关 W6，significant gap。\n[AGREE] Malinin & Gales (2021) — 相关于 uncertainty estimation。\n\n### 综合评价\nR1 的审稿意见质量高，技术判断准确。我们的分歧主要在严重程度而非方向上：\n- R1-N2 (statistical logic): 我认为 should-fix 而非 critical，因 6/6 配置一致性提供了 cumulative evidence\n- R1-N3 (single seed): 我认为 should-fix 因 ranking stability 有保障\n- R1-W6 (MBR alternative): 我认为这是 R1 最有价值的贡献点，论文确实只测了一种 instance-to-sample 转换策略就做了 sweeping claim",
    "reviewer_id": "2",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 293 · 2026-05-15T04:09:21.242328+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3766
}
```

</details>

---


### Assistant

_source line 294 · 2026-05-15T04:09:31.882464+00:00_

交叉回应已提交。

与 R1 的核心分歧在于严重程度判断：
- R1-N2（统计逻辑）和 R1-N3（单 seed）我认为应降为 Should-Fix，因为 6/6 配置一致性和 ranking 稳定性提供了足够的 cumulative evidence
- R1-W6（consensus-proximity 唯一策略 + 缺少 MBR 对比）是 R1 最有力的贡献点，我的原始审稿未充分关注到这一点

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2"
}
```

</details>

---


## Round 9

## Round 9

44 recorded events


### User

_source line 295 · 2026-05-15T06:42:38.349627+00:00_

[Round 1 审稿请求]:
## Round 1 审稿任务 — Reviewer 2

**你的审查侧重：新颖性 + 相关工作完整性 + 写作质量 + 格式合规**

### 论文信息
- **标题**: Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence Signals for Test-Time Scaling in Information Extraction
- **路径**: projects/struct_self_consist_ie/docs/paper/main.tex（含 sections/ 下 9 个 .tex 文件 + references.bib + figures/）
- **目标 Venue**: EMNLP 2026 Findings track
- **截止日期**: 2026-05-25（ARR May cycle）
- **格式**: ACL template, 长文 8 页正文, double-blind, 附录须 double-column
- **匿名**: Double-blind（当前标注 Anonymous ✓）

### 论文概要
本文系统比较了三族五种置信度信号在生成式 IE（NER + RE）中的 test-time scaling 表现。核心贡献：(1) 首个多族信号比较；(2) 发现 correlation-selection gap（信号能估计质量但不能选择最佳样本）；(3) 信号排名依赖任务难度。使用 Qwen3-8B 和 LLaMA-3.1-8B，在 SciERC、CoNLL-2003、WNUT-17 上评测。

### 审查要求
请从以下维度深入评审，给出结构化报告（Summary → Strengths → Weaknesses → Questions → Missing References → Detailed Comments）：

1. **新颖性与贡献**
   - "Correlation-selection gap" 概念的原创性和学术价值
   - 相对于 Nedellec (2026)（最相关先行工作）的增量贡献是否充分
   - "First multi-family comparison" claim 的准确性和 scope
   - Findings track 的定位是否合适（empirical study with negative result）
   - 对 NLP/IE 社区的实际影响力评估

2. **相关工作完整性**
   - 自洽性文献（Wang 2023, Chen 2024, Taubenfeld 2025 等）覆盖度
   - MBR decoding 文献（Eikema & Aziz 2022, Freitag 2022）是否充分讨论
   - 结构化 IE 不确定性文献（VerifiNER, CoCoA 等）
   - Uncertainty estimation 综述类文献
   - 是否有重要遗漏（特别关注 2025-2026 年最新工作）

3. **写作质量**
   - 论文结构和叙事流畅度
   - 术语一致性（confidence signal vs consistency signal, 缩写统一）
   - 图表质量和信息密度（6 figures, 多张 tables）
   - Abstract 和 Conclusion 是否准确反映 claims
   - 对 Nedellec 等先行工作的语气是否中立客观

4. **格式合规**
   - 页数限制（8 页正文）
   - 匿名审查合规
   - Limitations section 内容充实度
   - Ethics statement 存在性
   - 附录格式（double-column 要求）
   - 参考文献格式一致性
   - Responsible NLP Checklist 相关内容

请独立审查，给出你对本文的 overall assessment（strong reject / weak reject / borderline / weak accept / strong accept）+ 置信度。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 296 · 2026-05-15T06:42:46.493113+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 297 · 2026-05-15T06:42:48.250896+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1757
}
```

</details>

---


### Tool call

_source line 298 · 2026-05-15T06:42:48.351770+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,mcp__agent-ml-research__verify_references",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 299 · 2026-05-15T06:42:48.352251+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 300 · 2026-05-15T06:42:54.528122+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2026 reviewer guidelines review form criteria scoring"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool call

_source line 301 · 2026-05-15T06:42:55.482349+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 Findings track reviewer form dimensions scoring rubric"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 Findings track reviewer form dimensions scoring rubric"
  }
}
```

</details>

---


### Tool call

_source line 302 · 2026-05-15T06:42:56.889459+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 303 · 2026-05-15T06:42:57.341721+00:00_

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
15	\usepackage{multirow}
16	\usepackage{xcolor}
17	\usepackage{subcaption}
18	
19	\graphicspath{{figures/}}
20	
21	\title{Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence Signals for Test-Time Scaling in Information Extraction}
22	
23	\author{Anonymous}
24	
25	\begin{document}
26	\maketitle
27	
28	\input{sections/abstract}
29	\input{sections/introduction}
30	\input{sections/related_work}
31	\input{sections/method}
32	\input{sections/experiments}
33	\input{sections/discussion}
34	\input{sections/conclusion}
35	
36	\section*{Limitations}
37	\input{sections/limitations}
38	
39	\bibliography{references}
40	
41	\appendix
42	\input{sections/appendix}
43	
44	\end{document}
45	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 304 · 2026-05-15T06:42:57.342069+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 305 · 2026-05-15T06:42:59.551378+00:00_

Web search results for query: "EMNLP 2026 Findings track reviewer form dimensions scoring rubric"

Links: [{"title":"FAQ - EMNLP 2026","url":"https://2026.emnlp.org/faq/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"GitHub - acl-org/emnlp-2026: Repository for the EMNLP 2026 conference · GitHub","url":"https://github.com/acl-org/emnlp-2026"},{"title":"EMNLP 2026 | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026"},{"title":"ARR Reviewer Guidelines","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"EMNLP 2023 Statistics - Paper Copilot","url":"https://papercopilot.com/statistics/emnlp-statistics/emnlp-2023-statistics/"},{"title":"EMNLP: Empirical Methods in Natural Language Processing 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=883"},{"title":"EMNLP Statistics - Paper Copilot","url":"https://papercopilot.com/statistics/emnlp-statistics/"},{"title":"EMNLP 2024 Statistics - Paper Copilot","url":"https://papercopilot.com/statistics/emnlp-statistics/emnlp-2024-statistics/"},{"title":"EMNLP 2026 (@emnlpmeeting) / Posts / X","url":"https://x.com/emnlpmeeting"}]

Based on the search results, I was unable to find specific information about the EMNLP 2026 Findings track reviewer form dimensions or scoring rubric. The search returned general information about EMNLP 2026 submission policies, important dates, and review guidelines, but not the specific technical details about the Findings track reviewer form structure and scoring dimensions.

To access this information, you may want to:
1. Check the official EMNLP 2026 website directly at https://2026.emnlp.org/
2. Consult the ARR (ACL Rolling Review) website at aclrollingreview.org, as EMNLP 2026 uses the ARR review system
3. Contact the EMNLP 2026 organizers or program chairs directly

The reviewer guidelines and form specifications are typically published closer to the actual revi
…[truncated 184 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 4069
}
```

</details>

---


### Tool result

_source line 306 · 2026-05-15T06:43:01.812406+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ACLRollingReview (@ReviewAcl) / Posts / X","url":"https://x.com/ReviewAcl"}]

Based on the search results, here's what I found regarding ACL ARR 2026 reviewer guidelines, review form criteria, and scoring:

## Reviewer Scoring System

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

## Soundness Score

The soundness scores must b
…[truncated 1392 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7284
}
```

</details>

---


### Tool result

_source line 307 · 2026-05-15T06:43:45.041303+00:00_

{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 55, \"total_citations\": 76, \"unique_cited_keys\": 55, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 51, \"online_not_found\": 2, \"online_mismatch\": 2}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"angelopoulos2021conformal\", \"type\": \"inproceedings\", \"title\": \"Uncertainty Sets for Image Classifiers using Conformal Prediction\", \"authors\": \"Angelopoulos, Anastasios N. and Bates, Stephen and Malik, Jitendra and Jordan, M...\", \"year\": \"2021\", \"venue\": \"ICLR 2021\"}, {\"key\": \"brown2024monkeys\", \"type\": \"article\", \"title\": \"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\", \"authors\": \"Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, ...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2407.21787\"}, {\"key\": \"chen2024usc\", \"type\": \"inproceedings\", \"title\": \"Universal Self-Consistency for Large Language Model Generation\", \"authors\": \"Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Y...\", \"year\": \"2024\", \"venue\": \"arXiv preprint (ICML 2024 Workshop ICL)\"}, {\"key\": \"cobbe2021verifiers\", \"type\": \"article\", \"title\": \"Training Verifiers to Solve Math Word Problems\", \"authors\": \"Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, ...\", \"year\": \"2021\", \"venue\": \"arXiv preprint arXiv:2110.14168\"}, {\"key\": \"culotta2004confidence\", \"type\": \"inproceedings\", \"title\": \"Confidence Estimation for Information Extraction\", \"authors\": \"Culotta, Aron and McCallum, Andrew\", \"year\": \"2004\", \"venue\": \"HLT-NAACL 2004\"}, {\"key\": \"derczynski2017wnut\", \"type\": \"inproceedings\", \"title\": \"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recogniti
…[truncated 43119 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 47699
}
```

</details>

---


### Tool call

_source line 308 · 2026-05-15T06:43:55.494105+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form: all scoring dimensions (soundness, excitement, overall recommendation, confidence, etc.), their scales (1-5), and the detailed description for each score level. Also extract any special criteria for Findings track papers."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form: all scoring dimensions (soundness, excitement, overall recommendation, confidence, etc.), their scales (1-5), and the detailed description for each score level. Also extract any special criteria for Findings track papers."
  }
}
```

</details>

---


### Tool call

_source line 309 · 2026-05-15T06:43:57.803470+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 310 · 2026-05-15T06:43:58.205502+00:00_

1	\begin{abstract}
2	Test-time scaling through multi-sample generation promises quality improvements for LLM-based information extraction, but which confidence signals best serve quality estimation versus sample selection remains unclear.
3	We systematically compare five confidence signals from three families---structural (entity voting, Soft Jaccard), surface (exact match, Fleiss' $\kappa$), and model-internal (log-probability)---across NER (three datasets of varying difficulty) and RE (SciERC) with two model families (Qwen3-8B, LLaMA-3.1-8B).
4	We find that the strongest signals achieve $\rho{=}0.38$ (entity voting) and AUROC${=}0.75$ (exact match) for quality estimation, with ranking and classification favoring different signals across task complexity; however, this strong quality estimation does not translate into selection gains---we find no statistically significant evidence that any signal surpasses greedy decoding on SciERC---where output diversity is substantial---across both model architectures ($p{>}0.39$, bootstrap) despite 13--18~pp of oracle headroom; on easier tasks, near-identical outputs preclude meaningful selection analysis.
5	We term this disconnect the \textit{correlation-selection gap}: instance-level consistency signals predict which inputs the model handles reliably, not which output is best among $N$ candidates.
6	Signal rankings further depend on task difficulty---exact match dominates easy tasks, structural signals dominate hard tasks---with consistent ordering direction across models but model-dependent magnitude; when model capability is insufficient, apparent correlations are driven by zero/non-zero separation rather than genuine quality gradation.
7	These results reframe consistency signals as quality estimators rather than output selectors for structured IE.
8	\end{abstract}
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 311 · 2026-05-15T06:43:58.205875+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 312 · 2026-05-15T06:43:58.707825+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Self-consistency---sampling multiple outputs and aggregating them---has become a powerful strategy for improving language model reasoning.
4	On discrete-answer tasks such as arithmetic and commonsense QA, majority voting over chain-of-thought samples yields large gains: +18 percentage points on GSM8K (PaLM-540B; \citealp{wang2023selfconsistency}).
5	More broadly, test-time compute scaling through repeated sampling and selection has emerged as a complementary axis to model scaling, offering substantial quality improvements at inference time \cite{snell2024scaling, brown2024monkeys}.
6	These results rest on a shared assumption: that among $N$ stochastic samples, a selection mechanism can identify better outputs.
7	For tasks with a single correct answer, this assumption holds naturally---the majority vote is the selector.
8	But information extraction (IE) poses a fundamentally different challenge.
9	The output is not a single token or number; it is a \textit{set} of entities or relations with internal dependencies, where two samples may extract overlapping but non-identical structures.
10	There is no obvious majority to vote on, partial agreement is the norm rather than the exception, and the space of valid outputs is combinatorially large.
11	Can self-consistency still provide useful signal in this structured setting?
12	
13	Prior work on confidence estimation for LLM-based IE has conflated two distinct objectives: \textit{quality estimation} (which inputs does the model handle reliably?) and \textit{sample selection} (which of $N$ outputs is best?).
14	These require fundamentally different signal properties: the former benefits from instance-level aggregation, while the latter demands per-sample discrimination.
15	Self-consistency methods for discrete answers \cite{wang2023selfconsistency, chen2024usc} and weighted variants \cite{taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalen
…[truncated 4333 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 501
}
```

</details>

---


### Tool call

_source line 313 · 2026-05-15T06:43:58.708241+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 314 · 2026-05-15T06:43:59.611749+00:00_

1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Self-consistency and test-time scaling.}
4	Self-consistency decoding \cite{wang2023selfconsistency} improves reasoning by majority voting over chain-of-thought samples, assuming a discrete answer space.
5	Extensions to free-form text use LLM-based comparison \cite{chen2024usc}, atomic sub-claim decomposition \cite{thirukovalluru2024atomic}, or cross-sample hallucination detection \cite{manakul2023selfcheckgpt}.
6	For test-time scaling, \citet{snell2024scaling} characterize compute scaling laws and \citet{brown2024monkeys} show best-of-$N$ gains across tasks.
7	Recent reward-free selectors include confidence-weighted voting \cite{taubenfeld2025cisc}, KL-based self-certainty \cite{kang2025selfcertainty}, adaptive sampling \cite{kim2026reasc}, ranked aggregation \cite{wang2025rankedvoting}, and latent-space consistency \cite{oh2025latentsc}.
8	Concurrently, \citet{feng2025optimal} and \citet{wang2025make} adapt self-consistency to difficulty-aware settings, echoing our finding that signal rankings shift with task complexity; \citet{li2025llms} propose generative self-aggregation for IE but focus on output fusion rather than confidence-based selection.
9	All of the above target reasoning/QA with discrete answers or specific aggregation strategies.
10	Our work extends self-consistency to set-valued structured outputs and identifies the correlation-selection gap: strong quality estimation ($\rho{=}0.38$) coexists with selection failure ($p{>}0.39$).
11	
12	\paragraph{Consistency for structured IE.}
13	\citet{nedellec2026consistency} study consistency--accuracy correlations for LLM-based NER/RE, corroborating our quality-estimation findings.
14	Their work leaves open three questions we address: (i)~whether structural matching improves on surface-level agreement (which they acknowledge ``overlooks semantically consistent outputs''); (ii)~whether quality estimation translates to best-of-$N$ selection; and (iii)~whet
…[truncated 3141 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 903
}
```

</details>

---


### Tool call

_source line 315 · 2026-05-15T06:43:59.612240+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 316 · 2026-05-15T06:44:00.114559+00:00_

1	\section{Method}\label{sec:method}
2	
3	\subsection{Problem Formulation}\label{sec:formulation}
4	
5	Given a language model $\mathcal{M}$ and input $x$, we sample $N$ structured outputs $\{y_1, \ldots, y_N\}$ at temperature $T > 0$ via constrained decoding \cite{willard2023guided}.
6	Each $y_i$ is an entity set (NER) or relation set (RE).
7	A confidence signal $c$ serves two purposes: (a) \textit{quality estimation}---predicting which instances the model handles reliably, and (b) \textit{sample selection}---identifying the best output among $N$ candidates.
8	
9	A \textbf{per-sample signal} scores each $y_i$ independently, $c_{\text{ps}}: (x, y_i) \to \mathbb{R}$, enabling direct candidate ranking.
10	An \textbf{instance-level signal} aggregates over all $N$ samples, $c_{\text{il}}: (x, \{y_i\}_{i=1}^N) \to \mathbb{R}$, producing a single score per input.
11	This asymmetry---between predicting \textit{which inputs} are easy and selecting \textit{which output} is best---is central to the correlation-selection gap we investigate.
12	Notation is summarized in Appendix~\ref{app:notation}.
13	
14	\subsection{Confidence Signals}\label{sec:signals}
15	
16	We compare five signals from three families: \textit{model-internal} (log-probability), \textit{surface} (exact match, Fleiss' $\kappa$), and \textit{structural} (Soft Jaccard, entity voting).
17	
18	\paragraph{Log-probability (model-internal, per-sample).}
19	The only per-sample signal.
20	For sample $y_i$ with tokens $t_1, \ldots, t_{|y_i|}$:
21	\begin{equation}\label{eq:logprob}
22	c_{\text{lp}}(y_i) = \frac{1}{|y_i|} \sum_{j=1}^{|y_i|} \log p_{\mathcal{M}}(t_j \mid t_{<j}, x)
23	\end{equation}
24	
25	\paragraph{Exact match voting (surface, instance-level).}
26	The majority fraction---the proportion of samples producing the most common output:
27	\begin{equation}\label{eq:em}
28	c_{\text{em}}(x) = \frac{1}{N} \max_{y} \big|\{i : y_i = y\}\big|
29	\end{equation}
30	
31	\paragraph{Fleiss' $\kappa$ (surface, instance-lev
…[truncated 3478 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 317 · 2026-05-15T06:44:00.114937+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 318 · 2026-05-15T06:44:00.567157+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Datasets.}
8	We evaluate on three English IE benchmarks spanning a difficulty gradient.
9	\textbf{SciERC} \cite{luan2018scierc} contains 551 test instances annotated for joint NER (6 types) and RE (7 types).
10	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} provides 3{,}453 test sentences with 4 entity types, where models achieve ${\approx}$91\% micro F1.
11	\textbf{WNUT-17} \cite{derczynski2017wnut} consists of 1{,}287 social media instances with emerging entities, used to probe method boundaries (52\% zero F1).
12	
13	\paragraph{Models and sampling.}
14	Both \textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are fine-tuned with LoRA (rank$=$32, $\alpha{=}64$) for 5 epochs using LLaMA Factory \cite{zheng2024llamafactory} under identical training procedures, ensuring cross-architecture comparisons (at 8B scale) reflect architectural differences rather than training confounds.
15	We draw $N{=}8$ samples at $T{=}1.0$ (primary), with $N{=}16$ for scaling experiments.\footnote{$N{=}16$ results for CoNLL (Qwen) and SciERC (LLaMA) are in Table~\ref{tab:robustness} (Appendix~\ref{app:robustness}).}
16	Quality estimation uses Spearman $\rho$ and AUROC; downstream utility uses best-of-$N$ selection F1 with exact span matching (NER) and head-tail-label matching (RE).
17	Inference uses vLLM with constrained decoding \cite{willard2023guided}.
18	
19	%% ============================================================
20	\subsection{Quality Estimation Results}
21	\label{sec:qe_results}
22	
23	\begin{table*}[t]
24	\centering
25	\small
26	\caption{Quality estimation across tasks and models (Spearman $\rho$ and AUROC). Best value per block and column in \textbf{bold}. SciERC evaluates joint NER (6 types) and RE (7 types); CoNLL evaluates NER (4 types). $N{=}8$ results use seed${=}42$; $N{=}16$ results are averaged across seeds \{42, 123, 456\}.}
27	\label{tab:qu
…[truncated 11663 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 319 · 2026-05-15T06:44:00.567627+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 320 · 2026-05-15T06:44:01.070058+00:00_

1	\section{Discussion}\label{sec:discussion}
2	
3	\paragraph{Practical recommendations.}
4	For per-instance quality ranking, entity voting provides the strongest rank correlation ($\rho{=}0.38$), though exact match leads binary discrimination (AUROC${=}0.749$); under conditional filtering, EM leads on both NER and RE ($\rho{=}0.360$, $0.417$).
5	Signal rankings depend on task difficulty---EM dominates easy tasks (CoNLL), Voting and SJ dominate hard tasks (SciERC)---directionally consistent across tested model families, though with model-dependent magnitude.
6	When model capability is insufficient (WNUT-17), all signals converge toward non-significant conditional correlations (Table~\ref{tab:wnut}).
7	
8	\paragraph{Why the gap exists.}
9	Four of five signals are instance-level by construction and cannot rank $N$ candidates; the consensus-proximity strategy (\S\ref{sec:evaluation}) adds no reliable value (Table~\ref{tab:selection}).
10	Logprob, the sole per-sample signal, primarily reflects grammar compliance under constrained decoding---75\% of comparisons are effectively ties (\S\ref{sec:selection_gap}).
11	The common root is that quality estimation ranks \textit{instances}, while sample selection ranks \textit{candidates within a single instance}, requiring per-sample quality information that neither instance-level aggregation nor token-level confidence provides.
12	On SciERC, diversity-stratified analysis confirms the gap persists even among high-diversity instances (Appendix~\ref{app:diversity}); calibration analysis shows RE miscalibration (ECE 0.109--0.339; Appendix~\ref{app:calibration}) may compound this failure.
13	These signals are thus well-suited for quality-aware routing but not for discriminating among candidates.
14	
15	\paragraph{Connection to MBR decoding.}
16	Our selection strategies instantiate minimum Bayes risk (MBR) decoding \cite{eikema2022sampling}: SJ uses $U{=}\text{SJ}(y_i, y_j)$, EM uses $U{=}\mathbb{1}[y_i{=}y_j]$ (standard majority votin
…[truncated 918 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 321 · 2026-05-15T06:44:01.070579+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 322 · 2026-05-15T06:44:01.974486+00:00_

# ACL Rolling Review Form - Scoring Dimensions

## 1. **Reviewer Confidence** (1-5 scale)
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: "Quite sure. I tried to check the important points carefully."
- **3**: "Pretty sure, but there's a chance I missed something."
- **2**: "Willing to defend my evaluation, but it is fairly likely that I missed some details."
- **1**: "Not my area, or paper is very hard to understand."

## 2. **Soundness** (1-5 scale with half-points)
- **5**: "Excellent: This study is one of the most thorough I have seen, given its type."
- **4**: "Strong: This study provides sufficient support for all of its claims."
- **3**: "Acceptable: This study provides sufficient support for its main claims."
- **2**: "Poor: Some of the main claims are not sufficiently supported."
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication."

## 3. **Excitement** (1-5 scale with half-points)
- **5**: "Highly Exciting: I would recommend this paper to others."
- **4**: "Exciting: I would mention this paper to others."
- **3**: "Interesting: I might mention some points of this paper to others."
- **2**: "Potentially Interesting: this paper does not resonate with me."
- **1**: "Not Exciting: this paper does not resonate with me."

## 4. **Overall Assessment** (1-5 scale with half-points)
- **5**: "Consider for Award: top 2.5% papers"
- **4**: "Conference: could be accepted to an ACL conference"
- **3**: "Findings: could be accepted to Findings of the ACL"
- **2**: "Resubmit next cycle: needs substantial revisions"
- **1**: "Do not resubmit: fully redone or not relevant"

## Findings Track Criteria
"The main criteria for Findings are soundness and reproducibility."

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 6480
}
```

</details>

---


### Tool result

_source line 323 · 2026-05-15T06:44:01.975093+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	This work provides, to our knowledge, the first multi-family comparison of confidence signals for test-time scaling in generative information extraction.
4	By comparing five signals from three families across NER and RE tasks of varying difficulty, we disentangle quality estimation from sample selection---two objectives that prior work has conflated.
5	Consistency-based signals are effective quality estimators ($\rho$ up to 0.38, AUROC up to 0.75), but we find no significant evidence that any signal surpasses greedy on best-of-$N$ selection on SciERC ($p{>}0.39$, 13--18~pp oracle headroom), a disconnect we term the \textit{correlation-selection gap}.
6	Signal rankings depend on task difficulty---exact match leads on easy tasks, structural signals on hard tasks---with this ordering directionally consistent across model families, though magnitudes are model-dependent.
7	While our NER findings are validated across three datasets, our RE conclusions rest on SciERC alone and warrant further validation.
8	
9	Trained verifiers or reward models could close the selection gap by learning per-sample quality discrimination.
10	Cross-task transfer beyond IE, scaling to larger models (70B+), and integration with conformal prediction are promising directions.
11	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 904
}
```

</details>

---


### Tool call

_source line 324 · 2026-05-15T06:44:02.025710+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 325 · 2026-05-15T06:44:02.126537+00:00_

1	Our evaluation covers three datasets but only one RE benchmark (SciERC), where 40\% of instances receive zero F1, compressing the discriminable range and limiting signal differentiation for relation extraction.
2	WNUT-17 confirms the capability boundary of our approach, but our positive results on formal-domain text (CoNLL, SciERC) have not been validated on informal or noisy text where models achieve non-trivial performance.
3	
4	We evaluate two model families (Qwen3-8B and LLaMA-3.1-8B), both at 8B parameters.
5	A 3-seed robustness analysis confirms that signal rankings are stable across seeds ($\sigma{\leq}0.025$; Table~\ref{tab:multiseed}), but whether our findings---particularly the correlation-selection gap and the difficulty-dependent signal ordering---hold for larger models (70B+) or closed-source APIs remains untested.
6	Larger models may produce higher-quality and more diverse samples, potentially altering the signal landscape.
7	
8	Our analysis of selection potential uses only unsupervised signals.
9	We do not train a dedicated verifier or reward model, leaving unknown how much of the oracle headroom a supervised approach could recover.
10	
11	We evaluate at $N{=}8$ and $N{=}16$.
12	The behavior of confidence signals at larger sample sizes (e.g., $N{=}64$ or $N{=}128$) is unknown, and $N$-scaling gains are setting-dependent: SJ improves by $+0.052$ on Qwen SciERC NER but only $+0.016$ on LLaMA SciERC NER when doubling from $N{=}8$ to $N{=}16$.
13	
14	On CoNLL with LLaMA, the SJ--FK gap is only 0.003 ($\rho{=}0.431$ vs.\ $0.428$), so the structural advantage over surface signals may not generalize to all simple-schema datasets.
15	Constrained decoding (Outlines/vLLM) enforces schema compliance, potentially compressing per-sample diversity and contributing to the correlation-selection gap beyond what free-form generation would exhibit.
16	Finally, log-probability was excluded from the temperature comparison ($T{=}0.7$ vs.\ $T{=}1.0$) due to missing $T{=}0
…[truncated 307 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 326 · 2026-05-15T06:44:02.277618+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 327 · 2026-05-15T06:44:02.579575+00:00_

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
21	$c_{\text{vote}}$ & Entity voting confidence \\
22	$c_{\text{lp}}$ & Log-probability (mean token log-likelihood) \\
23	\bottomrule
24	\end{tabular}
25	\caption{Notation used throughout the paper.}
26	\label{tab:notation}
27	\end{table}
28	
29	\section{Robustness Analysis}\label{app:robustness}
30	
31	\begin{table}[t]
32	\centering
33	\small
34	\caption{Signal robustness across configurations (Spearman $\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: cross-architecture transfer (LLaMA CoNLL $N{=}16$, 3-seed mean $\pm\sigma$). $^\dagger$Mean over 3 seeds ($\sigma{=}0.025$; individual: 0.428, 0.424, 0.384).}
35	\label{tab:robustness}
36	\begin{tabular}{llcc}
37	\toprule
38	& & NER $\rho$ & RE $\rho$ \\
39	\midrule
40	\multicolumn{4}{l}{\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\
41	\quad SJ & $T{=}0.7$ & 0.388 & 0.234 \\
42	\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\
43	\quad FK & $T{=}0.7$ & 0.321 & 0.184 \\
44	\quad FK & $T{=}1.0$ & 0.267 & 0.275 \\
45	\midrule
46	\multicolumn{4}{l}{\textit{Sample size} (Qwen SciERC, $T{=}1.0$)} \\
47	\quad SJ & $N{=}8$  & 0.360 & 0.250 \\
48	\quad SJ & $N{=}16$ & 0.412$^\dagger$ & 0.281 \\
49	\quad FK & $N{=}8$  & 0.267 & 0.275 \\
50	\quad FK & $N{=}16$ & 0.280 & 0.279 \\
51	\midrule
52	\multicolumn{4}{l}{\textit{Cross-architecture} (LLaMA CoNLL, $N{=}16$, 3 seeds)} \\
53	\quad SJ &  & $0.463{\pm}0.007$ & --- \\
54	\quad FK &  & $0.455{\pm}0.006$ & --- \\
55	\quad EM &
…[truncated 21352 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 328 · 2026-05-15T06:45:09.574308+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LLM confidence uncertainty structured prediction information extraction 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LLM confidence uncertainty structured prediction information extraction 2025 2026"
  }
}
```

</details>

---


### Tool call

_source line 329 · 2026-05-15T06:45:09.926103+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "self-consistency structured output generation NER relation extraction 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "self-consistency structured output generation NER relation extraction 2025"
  }
}
```

</details>

---


### Tool call

_source line 330 · 2026-05-15T06:45:10.930409+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "best-of-N selection reward-free verifier-free LLM 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "best-of-N selection reward-free verifier-free LLM 2025 2026"
  }
}
```

</details>

---


### Tool call

_source line 331 · 2026-05-15T06:45:12.387347+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 332 · 2026-05-15T06:45:12.438277+00:00_

1	% Auto-generated from literature_map.yaml — do not edit manually
2	
3	@inproceedings{angelopoulos2021conformal,
4	  title = {Uncertainty Sets for Image Classifiers using Conformal Prediction},
5	  author = {Angelopoulos, Anastasios N. and Bates, Stephen and Malik, Jitendra and Jordan, Michael I.},
6	  booktitle = {ICLR 2021},
7	  year = {2021},
8	  url = {https://arxiv.org/abs/2009.14193}
9	}
10	
11	@article{brown2024monkeys,
12	  title = {Large Language Monkeys: Scaling Inference Compute with Repeated Sampling},
13	  author = {Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, Quoc V. and Ré, Christopher and Mirhoseini, Azalia},
14	  journal = {arXiv preprint arXiv:2407.21787},
15	  year = {2024},
16	  url = {https://arxiv.org/abs/2407.21787}
17	}
18	
19	@inproceedings{chen2024usc,
20	  title = {Universal Self-Consistency for Large Language Model Generation},
21	  author = {Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Yin, Pengcheng and Prakash, Sushant and Sutton, Charles and Wang, Xuezhi and Zhou, Denny},
22	  booktitle = {arXiv preprint (ICML 2024 Workshop ICL)},
23	  year = {2024},
24	  url = {https://arxiv.org/abs/2311.17311}
25	}
26	
27	@article{cobbe2021verifiers,
28	  title = {Training Verifiers to Solve Math Word Problems},
29	  author = {Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, Heewoo and Kaiser, Lukasz and Plappert, Matthias and Tworek, Jerry and Hilton, Jacob and Nakano, Reiichiro and Hesse, Christopher and Schulman, John},
30	  journal = {arXiv preprint arXiv:2110.14168},
31	  year = {2021},
32	  url = {https://arxiv.org/abs/2110.14168}
33	}
34	
35	@inproceedings{culotta2004confidence,
36	  title = {Confidence Estimation for Information Extraction},
37	  author = {Culotta, Aron and McCallum, Andrew},
38	  booktitle = {HLT-NAACL 2004},
39	  year = {2004},
40	  url = {https://aclanthology.org/N04-4028/}
41	}
42	
43	@inproceedings{derczynski2017wnut,
44
…[truncated 20478 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 333 · 2026-05-15T06:45:18.066760+00:00_

Web search results for query: "self-consistency structured output generation NER relation extraction 2025"

Links: [{"title":"Cross-Type and Cross-Task Multi-Agent LLM Collaboration ...","url":"https://aclanthology.org/2025.findings-acl.718.pdf"},{"title":"Structured Language Generation Model: Loss Calibration and Formatted Decoding for Robust Structure Prediction and Knowledge Retrieval","url":"https://arxiv.org/html/2402.08971"},{"title":"A Simple but Effective Approach to Improve Structured Language Model Output for Information Extraction","url":"https://arxiv.org/html/2402.13364v1"},{"title":"STRUCTSENSE: A TASK-AGNOSTIC AGENTIC FRAMEWORK for STRUCTURED INFORMATION EXTRACTION with HUMAN-IN-THE-LOOP EVALUATION and BENCHMARKING","url":"https://arxiv.org/html/2507.03674v1"},{"title":"A Survey of Generative Information Extraction","url":"https://aclanthology.org/2025.coling-main.324.pdf"},{"title":"Few-Shot Relation Extraction via Two-Stage Knowledge- ...","url":"https://www.ijcai.org/proceedings/2025/0897.pdf"},{"title":"[2402.08971] Structured Language Generation Model: Loss Calibration and Formatted Decoding for Robust Structure Prediction and Knowledge Retrieval","url":"https://arxiv.org/abs/2402.08971"},{"title":"[2402.13364] A Simple but Effective Approach to Improve Structured Language Model Output for Information Extraction","url":"https://arxiv.org/abs/2402.13364"},{"title":"Journal of Information Security, 2025, 16(4), 544-567","url":"https://www.scirp.org/pdf/jis_7801162.pdf"},{"title":"Agent-based multimodal information extraction for nanomaterials | npj Computational Materials","url":"https://www.nature.com/articles/s41524-025-01674-7"}]

I found several recent research papers and results related to your query. Here's what the search revealed about self-consistency, structured output generation, NER, and relation extraction in 2025:

## Key Findings:

**Self-Consistency in Structured Output Generation:**
Self-consistency can be integrated with technique
…[truncated 1599 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8140
}
```

</details>

---


### Tool result

_source line 334 · 2026-05-15T06:45:18.117559+00:00_

Web search results for query: "best-of-N selection reward-free verifier-free LLM 2025 2026"

Links: [{"title":"[2502.18581] Scalable Best-of-N Selection for Large Language Models via Self-Certainty","url":"https://arxiv.org/abs/2502.18581"},{"title":"Scalable Best-of-N Selection for Large Language Models via Self-Certainty","url":"https://arxiv.org/html/2502.18581v1"},{"title":"LLM Leaderboard 2026: Best AI Models Benchmark & Ranking","url":"https://www.clickrank.ai/llm-leaderboard/"},{"title":"Best LLM for Coding in 2026: Ranked by Real Benchmarks | WhatLLM.org","url":"https://whatllm.org/best-llm-for-coding"},{"title":"Scalable Best-of-N Selection for Large Language Models via Self-Certainty","url":"https://openreview.net/pdf?id=29FRqmVQK8"},{"title":"LLM Leaderboard 2026: Compare 300+ Top AI Models by Intelligence, Speed & Price","url":"https://llm-stats.com/"},{"title":"Scalable Best-of-N Selection for Large Language Models via Self-Certainty | alphaXiv","url":"https://www.alphaxiv.org/overview/2502.18581v2"},{"title":"Best Open Source LLM 2026 Ranking + Ollama Guide","url":"https://whatllm.org/best-open-source-llm"},{"title":"LLM Benchmarks 2026 - Compare AI Benchmarks and Tests","url":"https://llm-stats.com/benchmarks"},{"title":"LLM Leaderboard 2026 — Compare Top AI Models - Vellum","url":"https://www.vellum.ai/llm-leaderboard"}]

Based on the search results, I found highly relevant research on best-of-N selection for LLMs that directly addresses your query:

## Key Finding: Self-Certainty for Best-of-N Selection

Best-of-N selection is a key technique for improving the reasoning performance of Large Language Models (LLMs) through increased test-time computation. A recent paper from February 2025 introduces an important approach to this problem.

Researchers at UC Berkeley propose self-certainty, a novel and efficient metric that leverages the inherent probability distribution of LLM outputs to estimate response quality without requiring external reward model
…[truncated 1143 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7187
}
```

</details>

---


### Tool result

_source line 335 · 2026-05-15T06:45:18.469357+00:00_

Web search results for query: "LLM confidence uncertainty structured prediction information extraction 2025 2026"

Links: [{"title":"An overview of model uncertainty and variability in LLM-based sentiment analysis: challenges, mitigation strategies, and the role of explainability - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12375657/"},{"title":"Frontiers | An overview of model uncertainty and variability in LLM-based sentiment analysis: challenges, mitigation strategies, and the role of explainability","url":"https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2025.1609097/full"},{"title":"A Survey on Uncertainty Quantification of Large Language Models: Taxonomy, Open Research Challenges, and Future Directions | ACM Computing Surveys","url":"https://dl.acm.org/doi/10.1145/3744238"},{"title":"Published as a conference paper at ICLR 2026","url":"https://openreview.net/pdf?id=SsuBd46twl"},{"title":"Uncertainty Propagation in LLM-Based Systems","url":"https://arxiv.org/html/2604.23505"},{"title":"Accepted Findings Papers - EMNLP 2025","url":"https://2025.emnlp.org/program/find_papers/"},{"title":"Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs | OpenReview","url":"https://openreview.net/forum?id=gjeQKFxFpZ"},{"title":"Published as a conference paper at ICLR 2025 DO LLMS ESTIMATE UNCERTAINTY WELL","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/ef472869c217bf693f2d9bbde66a6b07-Paper-Conference.pdf"},{"title":"Uncertainty Quantification and Confidence Calibration in ...","url":"https://arxiv.org/pdf/2503.15850"},{"title":"Uncertainty Quantification of Large Language Models using Approximate Bayesian Computation","url":"https://arxiv.org/html/2509.19375v1"}]

I've completed the web search for "LLM confidence uncertainty structured prediction information extraction 2025 2026". Here are the key findings:

## Recent Research on LLM Confidence and Uncertainty (2025-2026)

###
…[truncated 1937 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8895
}
```

</details>

---


### Tool call

_source line 336 · 2026-05-15T06:47:57.512410+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 — Round 1 审稿报告\n\n**论文**: Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence Signals for Test-Time Scaling in Information Extraction\n**Venue**: EMNLP 2026 Findings (ACL ARR May 2026 cycle)\n\n---\n\n## 总体评分\n\n**Overall**: 3.5 / 5（Findings: borderline accept）\n**一句话总结**: 方法论扎实、统计分析严谨的实证研究，\"correlation-selection gap\"概念有用，但新颖性受限于 gap 可从信号设计原理预见，且实验范围（2个8B模型、1个RE数据集）制约了结论的泛化性。\n\n---\n\n## 官方维度打分（ACL ARR Review Form, Feb 2025+）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| **Soundness** | 4 / 5 | 统计方法严谨（bootstrap CI, TOST equivalence testing, 3-seed validation），实验设计控制了训练混淆变量（identical LoRA procedure），结论的 hedge 恰当（\"no statistically significant evidence\" 而非 \"no effect\"）。RE 仅 SciERC 单数据集是主要弱点。 |\n| **Excitement** | 2.5 / 5 | Correlation-selection gap 概念有实用价值，但其核心原因——4/5信号是 instance-level、无法区分候选样本——可从信号定义直接推出，缺少\"意外性\"。对 Nedellec (2026) 的增量贡献真实但幅度有限。 |\n| **Overall Assessment** | 3.5 / 5 | 符合 Findings 标准：sound, reproducible, 有实用 takeaway（routing vs. selection）。但 novelty 不足以达到 main conference 水平。 |\n| **Confidence** | 4 / 5 | 熟悉自洽性解码、MBR、LLM 不确定性估计和生成式 IE 文献。仔细阅读了全文和附录。 |\n\n---\n\n## 主要优势\n\n1. **系统性和严谨性出色**。五种信号×三族系×四个配置的交叉比较，bootstrap CI（B=10,000）、TOST 等价检验、3-seed 稳定性验证——统计分析在 NLP 实证论文中属于上乘水准。特别是 TOST 等价检验（Table 8, Appendix D）不常见但非常恰当：它区分了\"没有显著差异\"和\"确认等价\"（例如 EM/Voting 在 RE 上即使±5pp 也不等价于 greedy，说明是系统性劣化）。\n\n2. **质量估计 vs. 样本选择的解耦**（Section 3.3）是清晰的方法论贡献。将 per-sample signal 和 instance-level signal 明确区分（Eq. 1–7），并展示 ρ 和 AUROC 的分离（Section 4.2 \"ρ–AUROC dissociation\"），为后续工作提供了好的评估框架。\n\n3. **任务难度依赖的信号排名**有实际指导意义：EM 在简单任务领先、结构化信号在复杂任务领先、能力不足时所有信号退化为 binary success/failure 检测器（WNUT-17 conditional ρ=0.038, Table 5）——这三层梯度比单一结论更有价值。\n\n4. **MBR 连接**（Discussion Section \"Connection to MBR decoding\"）将自洽性选择策略统一为 MBR 框架下不同 utility function 的实例化，概念上很优雅。\n\n5. **Limitations section 诚实且具体**，涵盖了 RE 单数据集、模型规模、constrained decoding 对 diversity 的压缩效应、logprob 温度敏感性数据缺失等——审稿人能想到的大部分限制作者都提前讨论了。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Correlation-selection gap 的\"意外性\"论证不足\n\n- **具体位置**: Section 1 (Introduction para 3), Section 4.3 (Selection Gap), Section 5 (Discussion \"Why the gap exists\")\n- **问题**: 论文将 correlation-selection gap 作为核心贡献（Contribution #2），但 gap 的主要原因——4/5 信号是 instance-level 的、对同一 input 的 N 个候选给出相同分数——是从信号设计中可以直接推导出的（Section 5 自己承认 \"Four of five signals are instance-level by construction and cannot rank N candidates\"）。唯一的 per-sample 信号 logprob 的失败更有趣（75% comparisons are ties），但探讨不够深入。如果 gap 在实验前就可以从原理预测，那核心贡献更多是\"验证一个预期结论\"而非\"发现一个意外现象\"。\n- **为什么影响接收**: 这直接关系到论文的 novelty 判断——Findings track 接收的最低标准包括 \"interesting findings\"。如果 reviewers 认为 gap 是显而易见的，excitement 评分会低于可接收线。\n- **建议修改方向**: (a) 在 Introduction 中正面讨论 \"why the gap is not obvious a priori\"——例如，MBR 在 MT 中成功地用 instance-level utility 做了有效选择（Freitag 2022），为什么在 IE 中失败？consensus-proximity 策略在理论上应该能产生 per-sample 区分度，为什么实际上不行？(b) 对 logprob 的 per-sample 选择失败做更深入的分析——logprob ties 的 75% 统计数据非常有价值，可以量化分析 constrained decoding 如何压缩了 logprob 的判别力（例如比较自由生成 vs. constrained decoding 下的 logprob 方差）。(c) 如果空间允许，讨论什么样的 per-sample 信号可能 work（不仅仅是 \"trained verifiers\"——是否存在无监督的 per-sample 结构化信号？）。\n\n**N2** [critical] RE 结论基于单一数据集（SciERC），泛化性不明\n\n- **具体位置**: Section 4.1 (Datasets), Section 6 (Conclusion para 1 最后一句), Limitations para 1\n- **问题**: SciERC RE 有 40% zero-F1 的 floor effect（Section 4.2 para 1），且 7 种关系类型的信号质量差异巨大（Feature-Of ρ=0.004 vs. Hyponym-Of ρ=0.646, Appendix C）。论文所有 RE 结论（correlation-selection gap、信号排名、calibration 等）都只来自这一个数据集。Conclusion 的 hedge（\"our RE conclusions rest on SciERC alone and warrant further validation\"）是诚实的，但 Contribution #1 的表述（\"quality estimation for NER and RE\"）在 RE 部分缺乏足够支撑。\n- **为什么影响接收**: 作为 systematic comparison 论文，单一 RE 数据集削弱了\"systematic\"的 claim。RE 结论中的 floor effect 使得很难区分\"信号本身的局限\"与\"数据集特性的伪影\"。\n- **建议修改方向**: (a) 增加至少一个 RE 数据集（如 TACRED/Re-TACRED 的子集或 NYT/WebNLG），或在 Contribution claims 中明确降低 RE 部分的贡献力度。(b) 对 SciERC RE 的 floor effect 做更系统的消融——例如，在 non-zero F1 的 RE 子集上重做选择分析，看 gap 是否依然存在。(c) 如果不增加数据集，至少在 Abstract 和 Contribution 列表中将 RE 标记为 preliminary/exploratory。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Abstract 过于密集，可读性差\n\n- **具体位置**: Abstract (sections/abstract.tex), 尤其第 4 行和第 6 行\n- **问题**: 第 4 行是一个包含 6 个括号注释、3 个分号、跨越 4 行的超长句子（\"We find that...despite 13–18 pp of oracle headroom\"）。第 6 行同样包含多层嵌套的条件限定。虽然信息量大，但第一次阅读很难把握核心信息。\n- **建议**: 将核心发现拆分为 2-3 个独立句子。具体数字（如 ρ=0.38, AUROC=0.75, p>0.39）可以保留，但每个句子应只传达一个关键 claim。\n\n**W2** [warning] \"confidence signal\" vs \"consistency signal\" 术语不一致\n\n- **具体位置**: Abstract line 7 (\"consistency signals\"), Introduction line 17 (\"confidence signals\"), Section 3 (\"confidence signal\" 作为 formal term), Discussion 多处\n- **问题**: 论文用 \"confidence signal\" 作为五种信号的统称（Section 3.2），但 Abstract 结尾和 Discussion 多处用 \"consistency signals\" 泛指——而 logprob 不是 consistency signal。这种混用虽然上下文可以区分，但对快速阅读的 reviewer 会造成困惑。\n- **建议**: 在 Method 开头（Section 3.2 之前）明确定义：\"We use confidence signal as the umbrella term for all five signals; the four non-logprob signals are collectively referred to as consistency signals.\"\n\n**W3** [warning] Nedellec (2026) 的引用键名 misleading\n\n- **具体位置**: references.bib line 280–287, 多处引用\n- **问题**: BibTeX 键名为 `nedellec2026consistency`，但查看 bib 条目，第一作者实际上是 Yao, Xinzhi，Nédellec 是第二作者。论文正文中使用 `\\citet{nedellec2026consistency}` 会产生 \"Yao et al. (2026)\" 的输出——但论文多处文字讨论说 \"Nedellec (2026)\" 指代这篇工作（如 Introduction line 16, Related Work line 13），可能造成读者混淆。\n- **建议**: 统一使用 Yao et al. (2026) 或更新 bib 键名为 `yao2026consistency`。\n\n**W4** [warning] Soft Jaccard 对 Nedellec (2026) 的改进幅度有限\n\n- **具体位置**: Section 4.2 para 1, Appendix E (Table 6)\n- **问题**: Contribution #1 的核心卖点之一是 structural matching 相对于 surface-level agreement 的优势（回应 Nedellec 的 limitation）。但 SJ vs. EM 在 SciERC NER 上 Δρ=+0.065，bootstrap CI 的下界仅为 +0.003，在 Bonferroni correction 下不显著（Table 6 footnote）。在 CoNLL 上 EM 反超 SJ。这意味着 structural matching 的优势是 task-dependent 且 marginal 的。\n- **为什么影响评分**: 这削弱了\"structural signals are superior\"的叙事——更准确的表述应该是 \"structural and surface signals are complementary, with the choice depending on task complexity\"。\n- **建议**: (a) 在 Contribution #1 中弱化 \"structural advantage\" 的表述，改为强调 difficulty-dependent complementarity。(b) 讨论在什么条件下用户应该选择 structural vs. surface signal，提供决策树或简单规则。\n\n**W5** [warning] 缺少 constrained decoding 对 diversity 影响的实验对照\n\n- **具体位置**: Limitations para 5 (line 15)\n- **问题**: 论文承认 \"constrained decoding (Outlines/vLLM) enforces schema compliance, potentially compressing per-sample diversity and contributing to the correlation-selection gap beyond what free-form generation would exhibit\"，但没有提供对照实验。这是一个重要的混淆变量：如果 constrained decoding 大幅压缩了 sample diversity，那么 correlation-selection gap 可能是 constrained decoding 的伪影，而非 structured IE 的固有属性。\n- **建议**: 增加一个 free-form generation baseline（无 constrained decoding），比较 output diversity 和 selection gap 的变化。哪怕只在一个 model-dataset 配置上做也很有说明力。\n\n**W6** [warning] 缺少若干相关工作\n\n- **具体位置**: Section 2 (Related Work)\n- **遗漏文献**:\n  1. **Xiong et al. (2024) \"Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs\"** (ICLR 2024) — 系统评估了 LLM 置信度获取方法（verbalized, consistency-based, logit-based），与本文的多族信号比较直接相关。\n  2. **Ye et al. (2024) \"Do LLMs Estimate Uncertainty Well in Instruction Following?\"** (ICLR 2025) — 评估 LLM 在指令跟随任务中的不确定性估计，与本文的 structured output + confidence 主题有交叉。\n  3. **最近的 Generative IE survey**（如 COLING 2025 的 \"A Survey of Generative Information Extraction\"）——可在 Related Work 的 generative IE 段落中引用以加强 IE 背景。\n- **建议**: 在 Related Work 的 \"Uncertainty estimation\" 段落中加入 Xiong et al. 的讨论，明确说明本文与 verbalized confidence 方法的区别（本文不要求模型显式表达置信度）。\n\n---\n\n## 小问题（不影响接收）\n\n1. **Table 1 N=16 行数据不完整**: N=16 的 3-seed 结果只报告了 LLaMA CoNLL（5列），SciERC 的 N=16 数据完全空白。虽然 Table 3 (Appendix) 有部分 N=16 数据，但 Table 1 的空白列给人\"实验不完整\"的印象。建议填充或添加脚注说明 N=16 全部数据的位置。\n\n2. **Figure 1 (Overview) 的右侧面板**: 标题说 \"the same instance-level signal assigns identical scores to all N candidates\"，但没有解释 consensus-proximity 策略如何将 instance-level 信号转化为 per-sample 排序。建议在 caption 中增加一句说明。\n\n3. **references.bib 格式小问题**: `feng2025optimal` 的第一作者姓名 mismatch（bib: Feng, Austin vs OpenAlex API: Austin as first name, suggesting `author = {Austin, Feng}`?），`snell2024scaling` 同理。实际上检查 bib 内容，author field 写的是 \"Feng, Austin and Alonso, Marius...\"——这里 Feng 是 last name, Austin 是 first name, 应该没问题。OpenAlex API 的 mismatch 可能是 API 端的解析问题。不影响论文。\n\n4. **Appendix 中 Table 5 (WNUT-17)**: Conditional ρ 和 p 值很有价值，建议将其关键数字在主文中也提及（目前主文 Section 4.2 最后一段提到了但没有给出所有信号的 conditional ρ）。\n\n5. **Ethics statement 位于 Limitations section 内部**（limitations.tex line 18–20）——ACL 格式通常建议将 Ethics Statement 作为独立段落或 section。当前位置不影响合规但不够规范。\n\n---\n\n## Missing References 总结\n\n| 文献 | 类型 | 相关度 | 优先级 |\n|------|------|--------|--------|\n| Xiong et al. (2024) \"Can LLMs Express Their Uncertainty?\" ICLR 2024 | Confidence elicitation survey | 高 | Should-cite |\n| Ye et al. (2025) \"Do LLMs Estimate Uncertainty Well?\" ICLR 2025 | Uncertainty in instruction-following | 中 | Nice-to-cite |\n| Xu et al. (2025) \"A Survey of Generative Information Extraction\" COLING 2025 | Generative IE survey | 中 | Nice-to-cite |\n\n---\n\n## 关于 Findings Track 定位\n\n本文作为 empirical study with negative result，Findings track 是合适的定位。论文满足 Findings 的核心标准：\n- **Soundness**: 方法论扎实，统计分析严谨（4/5）\n- **Reproducibility**: 使用公开模型和数据集，实验设置详细（LoRA 参数、N、T、seed 均明确）\n\n但 excitement 偏低（2.5/5），主要因为：(a) 核心 gap 可从信号设计预测；(b) 对社区的实际影响有限——实用 takeaway 是\"用 consistency 信号做 routing 而不做 selection\"，这个结论已经在 reasoning 领域有类似的先例。\n\n**对 Findings 的接收建议**: Borderline Accept — 方法论上足以发表，但建议作者加强 N1（gap 的非显然性论证）和 W4（弱化 structural advantage claim），这将使论文更有说服力。\n\n---\n\n**Reviewer 2 Confidence**: 4/5 — 熟悉该领域，仔细阅读全文及附录。",
  "reviewer_id": "2",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 — Round 1 审稿报告\n\n**论文**: Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence Signals for Test-Time Scaling in Information Extraction\n**Venue**: EMNLP 2026 Findings (ACL ARR May 2026 cycle)\n\n---\n\n## 总体评分\n\n**Overall**: 3.5 / 5（Findings: borderline accept）\n**一句话总结**: 方法论扎实、统计分析严谨的实证研究，\"correlation-selection gap\"概念有用，但新颖性受限于 gap 可从信号设计原理预见，且实验范围（2个8B模型、1个RE数据集）制约了结论的泛化性。\n\n---\n\n## 官方维度打分（ACL ARR Review Form, Feb 2025+）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| **Soundness** | 4 / 5 | 统计方法严谨（bootstrap CI, TOST equivalence testing, 3-seed validation），实验设计控制了训练混淆变量（identical LoRA procedure），结论的 hedge 恰当（\"no statistically significant evidence\" 而非 \"no effect\"）。RE 仅 SciERC 单数据集是主要弱点。 |\n| **Excitement** | 2.5 / 5 | Correlation-selection gap 概念有实用价值，但其核心原因——4/5信号是 instance-level、无法区分候选样本——可从信号定义直接推出，缺少\"意外性\"。对 Nedellec (2026) 的增量贡献真实但幅度有限。 |\n| **Overall Assessment** | 3.5 / 5 | 符合 Findings 标准：sound, reproducible, 有实用 takeaway（routing vs. selection）。但 novelty 不足以达到 main conference 水平。 |\n| **Confidence** | 4 / 5 | 熟悉自洽性解码、MBR、LLM 不确定性估计和生成式 IE 文献。仔细阅读了全文和附录。 |\n\n---\n\n## 主要优势\n\n1. **系统性和严谨性出色**。五种信号×三族系×四个配置的交叉比较，bootstrap CI（B=10,000）、TOST 等价检验、3-seed 稳定性验证——统计分析在 NLP 实证论文中属于上乘水准。特别是 TOST 等价检验（Table 8, Appendix D）不常见但非常恰当：它区分了\"没有显著差异\"和\"确认等价\"（例如 EM/Voting 在 RE 上即使±5pp 也不等价于 greedy，说明是系统性劣化）。\n\n2. **质量估计 vs. 样本选择的解耦**（Section 3.3）是清晰的方法论贡献。将 per-sample signal 和 instance-level signal 明确区分（Eq. 1–7），并展示 ρ 和 AUROC 的分离（Section 4.2 \"ρ–AUROC dissociation\"），为后续工作提供了好的评估框架。\n\n3. **任务难度依赖的信号排名**有实际指导意义：EM 在简单任务领先、结构化信号在复杂任务领先、能力不足时所有信号退化为 binary success/failure 检测器（WNUT-17 conditional ρ=0.038, Table 5）——这三层梯度比单一结论更有价值。\n\n4. **MBR 连接**（Discussion Section \"Connection to MBR decoding\"）将自洽性选择策略统一为 MBR 框架下不同 utility function 的实例化，概念上很优雅。\n\n5. **Limitations section 诚实且具体**，涵盖了 RE 单数据集、模型规模、constrained decoding 对 diversity 的压缩效应、logprob 温度敏感性数据缺失等——审稿人能想到的大部分限制作者都提前讨论了。\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Correlation-selection gap 的\"意外性\"论证不足\n\n- **具体位置**: Section 1 (Introduction para 3), Section 4.3 (Selection Gap), Section 5 (Discussion \"Why the gap exists\")\n- **问题**: 论文将 correlation-selection gap 作为核心贡献（Contribution #2），但 gap 的主要原因——4/5 信号是 instance-level 的、对同一 input 的 N 个候选给出相同分数——是从信号设计中可以直接推导出的（Section 5 自己承认 \"Four of five signals are instance-level by construction and cannot rank N candidates\"）。唯一的 per-sample 信号 logprob 的失败更有趣（75% comparisons are ties），但探讨不够深入。如果 gap 在实验前就可以从原理预测，那核心贡献更多是\"验证一个预期结论\"而非\"发现一个意外现象\"。\n- **为什么影响接收**: 这直接关系到论文的 novelty 判断——Findings track 接收的最低标准包括 \"interesting findings\"。如果 reviewers 认为 gap 是显而易见的，excitement 评分会低于可接收线。\n- **建议修改方向**: (a) 在 Introduction 中正面讨论 \"why the gap is not obvious a priori\"——例如，MBR 在 MT 中成功地用 instance-level utility 做了有效选择（Freitag 2022），为什么在 IE 中失败？consensus-proximity 策略在理论上应该能产生 per-sample 区分度，为什么实际上不行？(b) 对 logprob 的 per-sample 选择失败做更深入的分析——logprob ties 的 75% 统计数据非常有价值，可以量化分析 constrained decoding 如何压缩了 logprob 的判别力（例如比较自由生成 vs. constrained decoding 下的 logprob 方差）。(c) 如果空间允许，讨论什么样的 per-sample 信号可能 work（不仅仅是 \"trained verifiers\"——是否存在无监督的 per-sample 结构化信号？）。\n\n**N2** [critical] RE 结论基于单一数据集（SciERC），泛化性不明\n\n- **具体位置**: Section 4.1 (Datasets), Section 6 (Conclusion para 1 最后一句), Limitations para 1\n- **问题**: SciERC RE 有 40% zero-F1 的 floor effect（Section 4.2 para 1），且 7 种关系类型的信号质量差异巨大（Feature-Of ρ=0.004 vs. Hyponym-Of ρ=0.646, Appendix C）。论文所有 RE 结论（correlation-selection gap、信号排名、calibration 等）都只来自这一个数据集。Conclusion 的 hedge（\"our RE conclusions rest on SciERC alone and warrant further validation\"）是诚实的，但 Contribution #1 的表述（\"quality estimation for NER and RE\"）在 RE 部分缺乏足够支撑。\n- **为什么影响接收**: 作为 systematic comparison 论文，单一 RE 数据集削弱了\"systematic\"的 claim。RE 结论中的 floor effect 使得很难区分\"信号本身的局限\"与\"数据集特性的伪影\"。\n- **建议修改方向**: (a) 增加至少一个 RE 数据集（如 TACRED/Re-TACRED 的子集或 NYT/WebNLG），或在 Contribution claims 中明确降低 RE 部分的贡献力度。(b) 对 SciERC RE 的 floor effect 做更系统的消融——例如，在 non-zero F1 的 RE 子集上重做选择分析，看 gap 是否依然存在。(c) 如果不增加数据集，至少在 Abstract 和 Contribution 列表中将 RE 标记为 preliminary/exploratory。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Abstract 过于密集，可读性差\n\n- **具体位置**: Abstract (sections/abstract.tex), 尤其第 4 行和第 6 行\n- **问题**: 第 4 行是一个包含 6 个括号注释、3 个分号、跨越 4 行的超长句子（\"We find that...despite 13–18 pp of oracle headroom\"）。第 6 行同样包含多层嵌套的条件限定。虽然信息量大，但第一次阅读很难把握核心信息。\n- **建议**: 将核心发现拆分为 2-3 个独立句子。具体数字（如 ρ=0.38, AUROC=0.75, p>0.39）可以保留，但每个句子应只传达一个关键 claim。\n\n**W2** [warning] \"confidence signal\" vs \"consistency signal\" 术语不一致\n\n- **具体位置**: Abstract line 7 (\"consistency signals\"), Introduction line 17 (\"confidence signals\"), Section 3 (\"confidence signal\" 作为 formal term), Discussion 多处\n- **问题**: 论文用 \"confidence signal\" 作为五种信号的统称（Section 3.2），但 Abstract 结尾和 Discussion 多处用 \"consistency signals\" 泛指——而 logprob 不是 consistency signal。这种混用虽然上下文可以区分，但对快速阅读的 reviewer 会造成困惑。\n- **建议**: 在 Method 开头（Section 3.2 之前）明确定义：\"We use confidence signal as the umbrella term for all five signals; the four non-logprob signals are collectively referred to as consistency signals.\"\n\n**W3** [warning] Nedellec (2026) 的引用键名 misleading\n\n- **具体位置**: references.bib line 280–287, 多处引用\n- **问题**: BibTeX 键名为 `nedellec2026consistency`，但查看 bib 条目，第一作者实际上是 Yao, Xinzhi，Nédellec 是第二作者。论文正文中使用 `\\citet{nedellec2026consistency}` 会产生 \"Yao et al. (2026)\" 的输出——但论文多处文字讨论说 \"Nedellec (2026)\" 指代这篇工作（如 Introduction line 16, Related Work line 13），可能造成读者混淆。\n- **建议**: 统一使用 Yao et al. (2026) 或更新 bib 键名为 `yao2026consistency`。\n\n**W4** [warning] Soft Jaccard 对 Nedellec (2026) 的改进幅度有限\n\n- **具体位置**: Section 4.2 para 1, Appendix E (Table 6)\n- **问题**: Contribution #1 的核心卖点之一是 structural matching 相对于 surface-level agreement 的优势（回应 Nedellec 的 limitation）。但 SJ vs. EM 在 SciERC NER 上 Δρ=+0.065，bootstrap CI 的下界仅为 +0.003，在 Bonferroni correction 下不显著（Table 6 footnote）。在 CoNLL 上 EM 反超 SJ。这意味着 structural matching 的优势是 task-dependent 且 marginal 的。\n- **为什么影响评分**: 这削弱了\"structural signals are superior\"的叙事——更准确的表述应该是 \"structural and surface signals are complementary, with the choice depending on task complexity\"。\n- **建议**: (a) 在 Contribution #1 中弱化 \"structural advantage\" 的表述，改为强调 difficulty-dependent complementarity。(b) 讨论在什么条件下用户应该选择 structural vs. surface signal，提供决策树或简单规则。\n\n**W5** [warning] 缺少 constrained decoding 对 diversity 影响的实验对照\n\n- **具体位置**: Limitations para 5 (line 15)\n- **问题**: 论文承认 \"constrained decoding (Outlines/vLLM) enforces schema compliance, potentially compressing per-sample diversity and contributing to the correlation-selection gap beyond what free-form generation would exhibit\"，但没有提供对照实验。这是一个重要的混淆变量：如果 constrained decoding 大幅压缩了 sample diversity，那么 correlation-selection gap 可能是 constrained decoding 的伪影，而非 structured IE 的固有属性。\n- **建议**: 增加一个 free-form generation baseline（无 constrained decoding），比较 output diversity 和 selection gap 的变化。哪怕只在一个 model-dataset 配置上做也很有说明力。\n\n**W6** [warning] 缺少若干相关工作\n\n- **具体位置**: Section 2 (Related Work)\n- **遗漏文献**:\n  1. **Xiong et al. (2024) \"Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs\"** (ICLR 2024) — 系统评估了 LLM 置信度获取方法（verbalized, consistency-based, logit-based），与本文的多族信号比较直接相关。\n  2. **Ye et al. (2024) \"Do LLMs Estimate Uncertainty Well in Instruction Following?\"** (ICLR 2025) — 评估 LLM 在指令跟随任务中的不确定性估计，与本文的 structured output + confidence 主题有交叉。\n  3. **最近的 Generative IE survey**（如 COLING 2025 的 \"A Survey of Generative Information Extraction\"）——可在 Related Work 的 generative IE 段落中引用以加强 IE 背景。\n- **建议**: 在 Related Work 的 \"Uncertainty estimation\" 段落中加入 Xiong et al. 的讨论，明确说明本文与 verbalized confidence 方法的区别（本文不要求模型显式表达置信度）。\n\n---\n\n## 小问题（不影响接收）\n\n1. **Table 1 N=16 行数据不完整**: N=16 的 3-seed 结果只报告了 LLaMA CoNLL（5列），SciERC 的 N=16 数据完全空白。虽然 Table 3 (Appendix) 有部分 N=16 数据，但 Table 1 的空白列给人\"实验不完整\"的印象。建议填充或添加脚注说明 N=16 全部数据的位置。\n\n2. **Figure 1 (Overview) 的右侧面板**: 标题说 \"the same instance-level signal assigns identical scores to all N candidates\"，但没有解释 consensus-proximity 策略如何将 instance-level 信号转化为 per-sample 排序。建议在 caption 中增加一句说明。\n\n3. **references.bib 格式小问题**: `feng2025optimal` 的第一作者姓名 mismatch（bib: Feng, Austin vs OpenAlex API: Austin as first name, suggesting `author = {Austin, Feng}`?），`snell2024scaling` 同理。实际上检查 bib 内容，author field 写的是 \"Feng, Austin and Alonso, Marius...\"——这里 Feng 是 last name, Austin 是 first name, 应该没问题。OpenAlex API 的 mismatch 可能是 API 端的解析问题。不影响论文。\n\n4. **Appendix 中 Table 5 (WNUT-17)**: Conditional ρ 和 p 值很有价值，建议将其关键数字在主文中也提及（目前主文 Section 4.2 最后一段提到了但没有给出所有信号的 conditional ρ）。\n\n5. **Ethics statement 位于 Limitations section 内部**（limitations.tex line 18–20）——ACL 格式通常建议将 Ethics Statement 作为独立段落或 section。当前位置不影响合规但不够规范。\n\n---\n\n## Missing References 总结\n\n| 文献 | 类型 | 相关度 | 优先级 |\n|------|------|--------|--------|\n| Xiong et al. (2024) \"Can LLMs Express Their Uncertainty?\" ICLR 2024 | Confidence elicitation survey | 高 | Should-cite |\n| Ye et al. (2025) \"Do LLMs Estimate Uncertainty Well?\" ICLR 2025 | Uncertainty in instruction-following | 中 | Nice-to-cite |\n| Xu et al. (2025) \"A Survey of Generative Information Extraction\" COLING 2025 | Generative IE survey | 中 | Nice-to-cite |\n\n---\n\n## 关于 Findings Track 定位\n\n本文作为 empirical study with negative result，Findings track 是合适的定位。论文满足 Findings 的核心标准：\n- **Soundness**: 方法论扎实，统计分析严谨（4/5）\n- **Reproducibility**: 使用公开模型和数据集，实验设置详细（LoRA 参数、N、T、seed 均明确）\n\n但 excitement 偏低（2.5/5），主要因为：(a) 核心 gap 可从信号设计预测；(b) 对社区的实际影响有限——实用 takeaway 是\"用 consistency 信号做 routing 而不做 selection\"，这个结论已经在 reasoning 领域有类似的先例。\n\n**对 Findings 的接收建议**: Borderline Accept — 方法论上足以发表，但建议作者加强 N1（gap 的非显然性论证）和 W4（弱化 structural advantage claim），这将使论文更有说服力。\n\n---\n\n**Reviewer 2 Confidence**: 4/5 — 熟悉该领域，仔细阅读全文及附录。",
    "reviewer_id": "2",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 337 · 2026-05-15T06:48:02.136396+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4623
}
```

</details>

---


### Assistant

_source line 338 · 2026-05-15T06:48:14.231854+00:00_

审稿报告已提交给 Review Director。

**总结**：给出 Overall 3.5/5（Findings borderline accept），Soundness 4/5，Excitement 2.5/5。

主要发现：
- **2 个 Must-Fix**：(N1) correlation-selection gap 的"意外性"论证不足——4/5 信号 instance-level 的局限可从设计原理直接推出，需正面论证 why not obvious；(N2) RE 结论仅基于 SciERC 单一数据集，泛化性不明。
- **6 个 Should-Fix**：Abstract 过密、术语不一致（confidence vs consistency signal）、Nedellec 引用键名 misleading（实际第一作者是 Yao）、Soft Jaccard 优势幅度有限且 Bonferroni 下不显著、缺少 constrained decoding 对 diversity 影响的对照实验、缺少 Xiong et al. (2024) 等相关工作。
- **格式合规总体良好**：匿名合规、Limitations 充实、Ethics statement 存在（但位置不够规范）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2"
}
```

</details>

---


## Round 10

## Round 10

36 recorded events


### User

_source line 339 · 2026-05-15T06:51:07.728983+00:00_

[Round 4 审稿请求]:
## Round 4 审稿任务 — Reviewer 2

**论文**: Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence Signals for Test-Time Scaling in Information Extraction
**论文路径**: `projects/struct_self_consist_ie/docs/paper/main.tex`
**Venue**: EMNLP 2026 Findings (ACL ARR May 2026 cycle)
- 正文 8 页（不含 references），附录不限
- ACL 模板 (acl_natbib)
- Double-blind 匿名审稿
- 附录参与审稿但不要求审稿人阅读

**你的审查侧重：新颖性 + 完整性 + 写作质量 + Round 3 issue 修复验证**

### 侧重维度

1. **新颖性与贡献定位**：
   - "Correlation-selection gap" 作为概念的新颖性和非平凡性
   - Contribution claims 的 scope 是否与实际证据匹配
   - 论文在 uncertainty estimation / self-consistency / MBR decoding 文献中的定位是否准确

2. **完整性**：
   - 数据集覆盖（NER 3 个 vs RE 仅 1 个）对结论的支撑力
   - 模型规模（仅 8B）对 generalization claims 的限制
   - 相关工作覆盖是否充分——特别检查 MBR decoding 相关文献是否已补充（Round 3 要求补 Eikema & Aziz 2022, Freitag et al. 2022）
   - 训练配置完整性（LoRA 超参、prompt template、training data split）

3. **写作质量**：
   - 术语一致性（confidence signal vs consistency signal; VC vs Voting Conf.）
   - 统计措辞准确性（failure-to-reject ≠ evidence of absence）
   - 对 prior work（尤其 Nedellec 2026）的措辞是否 neutral

4. **ACL ARR 格式规范**：
   - Ethics Statement 是否已添加
   - Limitations section 是否充分
   - 引用格式、页数合规

### Round 3 遗留 Open Issues（请验证修复状态）

以下是 Round 3 审稿中标记为 in_progress 的核心问题，请检查论文当前版本是否已解决：

| ID | 问题 | 严重性 | 修复预期 |
|----|------|--------|----------|
| R3-C1 | Constrained decoding 是 gap 的未控制混淆变量 | critical | 量化 diversity 或限定 scope |
| R3-C2 | Failure-to-reject ≠ evidence of absence | warning | 措辞修改或补 TOST |
| R3-C3 | N=8 结果 single seed | warning | Limitations 声明或补 multi-seed |
| R3-W1 | 多重比较校正缺失 | warning | 声明 + 修改 borderline 措辞 |
| R3-W2 | Gap 概念部分 tautological | warning | Discussion 分层论证 |
| R3-W3 | Consensus-proximity 未与 MBR 建立联系 | warning | 补 MBR 讨论+引用 |
| R3-W4 | FK 独立性假设 justification 不足 | warning | 报告 inter-sample correlation |
| R3-W5 | Cross-model → cross-architecture | warning | 加限定词 |
| R3-W6 | First multi-family claim scope 过宽 | warning | 收窄措辞 |
| R3-W7 | 术语不一致 | warning | 统一 |
| R3-W8 | 遗漏引用（VerifiNER, MBR, Malinin&Gales, He+ 2024） | warning | 补引用 |
| R0-C3 | RE 结论仅基于 SciERC 单数据集 | critical | 降级 claim 为 preliminary |
| R1-W1 | SJ Hungarian 形式化歧义 | warning | 补 cost function 方向+zero-IoU 处理 |

### 输出格式

请按 ACL ARR review form 格式输出：
- 总体评分 (1-5)
- 维度打分：Soundness, Excitement, Reproducibility, Confidence
- Must-Fix 问题（影响接收决定）
- Should-Fix 问题（影响评分）
- 小问题
- 主要优势
- 缺失引用
- 总结判断

对每个 Round 3 遗留问题，明确标注 [RESOLVED] / [PARTIALLY RESOLVED] / [UNRESOLVED] 及理由。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 340 · 2026-05-15T06:51:19.467009+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
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

_source line 341 · 2026-05-15T06:51:19.518985+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 342 · 2026-05-15T06:51:23.947733+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 343 · 2026-05-15T06:51:24.802648+00:00_

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
15	\usepackage{multirow}
16	\usepackage{xcolor}
17	\usepackage{subcaption}
18	
19	\graphicspath{{figures/}}
20	
21	\title{Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence Signals for Test-Time Scaling in Information Extraction}
22	
23	\author{Anonymous}
24	
25	\begin{document}
26	\maketitle
27	
28	\input{sections/abstract}
29	\input{sections/introduction}
30	\input{sections/related_work}
31	\input{sections/method}
32	\input{sections/experiments}
33	\input{sections/discussion}
34	\input{sections/conclusion}
35	
36	\section*{Limitations}
37	\input{sections/limitations}
38	
39	\bibliography{references}
40	
41	\appendix
42	\input{sections/appendix}
43	
44	\end{document}
45	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 854
}
```

</details>

---


### Tool call

_source line 344 · 2026-05-15T06:51:24.853272+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2026 reviewer guidelines review form criteria scoring"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool call

_source line 345 · 2026-05-15T06:51:25.256142+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 346 · 2026-05-15T06:51:31.632339+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ACLRollingReview (@ReviewAcl) / Posts / X","url":"https://x.com/ReviewAcl"}]

Based on the search results, here's what I found about ACL ARR 2026 reviewer guidelines, review form criteria, and scoring:

## Review Scoring System

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

### Soundness Score
The soundness scores must be just
…[truncated 1213 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6779
}
```

</details>

---


### Tool result

_source line 347 · 2026-05-15T06:52:16.783790+00:00_

{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 55, \"total_citations\": 76, \"unique_cited_keys\": 55, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 51, \"online_not_found\": 2, \"online_mismatch\": 2}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"angelopoulos2021conformal\", \"type\": \"inproceedings\", \"title\": \"Uncertainty Sets for Image Classifiers using Conformal Prediction\", \"authors\": \"Angelopoulos, Anastasios N. and Bates, Stephen and Malik, Jitendra and Jordan, M...\", \"year\": \"2021\", \"venue\": \"ICLR 2021\"}, {\"key\": \"brown2024monkeys\", \"type\": \"article\", \"title\": \"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\", \"authors\": \"Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, ...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2407.21787\"}, {\"key\": \"chen2024usc\", \"type\": \"inproceedings\", \"title\": \"Universal Self-Consistency for Large Language Model Generation\", \"authors\": \"Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Y...\", \"year\": \"2024\", \"venue\": \"arXiv preprint (ICML 2024 Workshop ICL)\"}, {\"key\": \"cobbe2021verifiers\", \"type\": \"article\", \"title\": \"Training Verifiers to Solve Math Word Problems\", \"authors\": \"Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, ...\", \"year\": \"2021\", \"venue\": \"arXiv preprint arXiv:2110.14168\"}, {\"key\": \"culotta2004confidence\", \"type\": \"inproceedings\", \"title\": \"Confidence Estimation for Information Extraction\", \"authors\": \"Culotta, Aron and McCallum, Andrew\", \"year\": \"2004\", \"venue\": \"HLT-NAACL 2004\"}, {\"key\": \"derczynski2017wnut\", \"type\": \"inproceedings\", \"title\": \"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recogniti
…[truncated 43119 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 51527
}
```

</details>

---


### Tool call

_source line 348 · 2026-05-15T06:52:22.914321+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 349 · 2026-05-15T06:52:23.366635+00:00_

1	\begin{abstract}
2	Test-time scaling through multi-sample generation promises quality improvements for LLM-based information extraction, but which confidence signals best serve quality estimation versus sample selection remains unclear.
3	We systematically compare five confidence signals from three families---structural (entity voting, Soft Jaccard), surface (exact match, Fleiss' $\kappa$), and model-internal (log-probability)---across NER (three datasets of varying difficulty) and RE (SciERC) with two model families (Qwen3-8B, LLaMA-3.1-8B).
4	We find that the strongest signals achieve $\rho{=}0.38$ (entity voting) and AUROC${=}0.75$ (exact match) for quality estimation, with ranking and classification favoring different signals across task complexity; however, this strong quality estimation does not translate into selection gains---we find no statistically significant evidence that any signal surpasses greedy decoding on SciERC---where output diversity is substantial---across both model architectures ($p{>}0.39$, bootstrap) despite 13--18~pp of oracle headroom; on easier tasks, near-identical outputs preclude meaningful selection analysis.
5	We term this disconnect the \textit{correlation-selection gap}: instance-level consistency signals predict which inputs the model handles reliably, not which output is best among $N$ candidates.
6	Signal rankings further depend on task difficulty---exact match dominates easy tasks, structural signals dominate hard tasks---with consistent ordering direction across models but model-dependent magnitude; when model capability is insufficient, apparent correlations are driven by zero/non-zero separation rather than genuine quality gradation.
7	These results reframe consistency signals as quality estimators rather than output selectors for structured IE.
8	\end{abstract}
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 350 · 2026-05-15T06:52:23.367156+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 351 · 2026-05-15T06:52:23.869536+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Self-consistency---sampling multiple outputs and aggregating them---has become a powerful strategy for improving language model reasoning.
4	On discrete-answer tasks such as arithmetic and commonsense QA, majority voting over chain-of-thought samples yields large gains: +18 percentage points on GSM8K (PaLM-540B; \citealp{wang2023selfconsistency}).
5	More broadly, test-time compute scaling through repeated sampling and selection has emerged as a complementary axis to model scaling, offering substantial quality improvements at inference time \cite{snell2024scaling, brown2024monkeys}.
6	These results rest on a shared assumption: that among $N$ stochastic samples, a selection mechanism can identify better outputs.
7	For tasks with a single correct answer, this assumption holds naturally---the majority vote is the selector.
8	But information extraction (IE) poses a fundamentally different challenge.
9	The output is not a single token or number; it is a \textit{set} of entities or relations with internal dependencies, where two samples may extract overlapping but non-identical structures.
10	There is no obvious majority to vote on, partial agreement is the norm rather than the exception, and the space of valid outputs is combinatorially large.
11	Can self-consistency still provide useful signal in this structured setting?
12	
13	Prior work on confidence estimation for LLM-based IE has conflated two distinct objectives: \textit{quality estimation} (which inputs does the model handle reliably?) and \textit{sample selection} (which of $N$ outputs is best?).
14	These require fundamentally different signal properties: the former benefits from instance-level aggregation, while the latter demands per-sample discrimination.
15	Self-consistency methods for discrete answers \cite{wang2023selfconsistency, chen2024usc} and weighted variants \cite{taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalen
…[truncated 4333 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 352 · 2026-05-15T06:52:23.869896+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 353 · 2026-05-15T06:52:24.874348+00:00_

1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Self-consistency and test-time scaling.}
4	Self-consistency decoding \cite{wang2023selfconsistency} improves reasoning by majority voting over chain-of-thought samples, assuming a discrete answer space.
5	Extensions to free-form text use LLM-based comparison \cite{chen2024usc}, atomic sub-claim decomposition \cite{thirukovalluru2024atomic}, or cross-sample hallucination detection \cite{manakul2023selfcheckgpt}.
6	For test-time scaling, \citet{snell2024scaling} characterize compute scaling laws and \citet{brown2024monkeys} show best-of-$N$ gains across tasks.
7	Recent reward-free selectors include confidence-weighted voting \cite{taubenfeld2025cisc}, KL-based self-certainty \cite{kang2025selfcertainty}, adaptive sampling \cite{kim2026reasc}, ranked aggregation \cite{wang2025rankedvoting}, and latent-space consistency \cite{oh2025latentsc}.
8	Concurrently, \citet{feng2025optimal} and \citet{wang2025make} adapt self-consistency to difficulty-aware settings, echoing our finding that signal rankings shift with task complexity; \citet{li2025llms} propose generative self-aggregation for IE but focus on output fusion rather than confidence-based selection.
9	All of the above target reasoning/QA with discrete answers or specific aggregation strategies.
10	Our work extends self-consistency to set-valued structured outputs and identifies the correlation-selection gap: strong quality estimation ($\rho{=}0.38$) coexists with selection failure ($p{>}0.39$).
11	
12	\paragraph{Consistency for structured IE.}
13	\citet{nedellec2026consistency} study consistency--accuracy correlations for LLM-based NER/RE, corroborating our quality-estimation findings.
14	Their work leaves open three questions we address: (i)~whether structural matching improves on surface-level agreement (which they acknowledge ``overlooks semantically consistent outputs''); (ii)~whether quality estimation translates to best-of-$N$ selection; and (iii)~whet
…[truncated 3141 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1004
}
```

</details>

---


### Tool call

_source line 354 · 2026-05-15T06:52:24.874738+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 355 · 2026-05-15T06:52:25.326728+00:00_

1	\section{Method}\label{sec:method}
2	
3	\subsection{Problem Formulation}\label{sec:formulation}
4	
5	Given a language model $\mathcal{M}$ and input $x$, we sample $N$ structured outputs $\{y_1, \ldots, y_N\}$ at temperature $T > 0$ via constrained decoding \cite{willard2023guided}.
6	Each $y_i$ is an entity set (NER) or relation set (RE).
7	A confidence signal $c$ serves two purposes: (a) \textit{quality estimation}---predicting which instances the model handles reliably, and (b) \textit{sample selection}---identifying the best output among $N$ candidates.
8	
9	A \textbf{per-sample signal} scores each $y_i$ independently, $c_{\text{ps}}: (x, y_i) \to \mathbb{R}$, enabling direct candidate ranking.
10	An \textbf{instance-level signal} aggregates over all $N$ samples, $c_{\text{il}}: (x, \{y_i\}_{i=1}^N) \to \mathbb{R}$, producing a single score per input.
11	This asymmetry---between predicting \textit{which inputs} are easy and selecting \textit{which output} is best---is central to the correlation-selection gap we investigate.
12	Notation is summarized in Appendix~\ref{app:notation}.
13	
14	\subsection{Confidence Signals}\label{sec:signals}
15	
16	We compare five signals from three families: \textit{model-internal} (log-probability), \textit{surface} (exact match, Fleiss' $\kappa$), and \textit{structural} (Soft Jaccard, entity voting).
17	
18	\paragraph{Log-probability (model-internal, per-sample).}
19	The only per-sample signal.
20	For sample $y_i$ with tokens $t_1, \ldots, t_{|y_i|}$:
21	\begin{equation}\label{eq:logprob}
22	c_{\text{lp}}(y_i) = \frac{1}{|y_i|} \sum_{j=1}^{|y_i|} \log p_{\mathcal{M}}(t_j \mid t_{<j}, x)
23	\end{equation}
24	
25	\paragraph{Exact match voting (surface, instance-level).}
26	The majority fraction---the proportion of samples producing the most common output:
27	\begin{equation}\label{eq:em}
28	c_{\text{em}}(x) = \frac{1}{N} \max_{y} \big|\{i : y_i = y\}\big|
29	\end{equation}
30	
31	\paragraph{Fleiss' $\kappa$ (surface, instance-lev
…[truncated 3478 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 356 · 2026-05-15T06:52:25.327122+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 357 · 2026-05-15T06:52:25.779120+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Datasets.}
8	We evaluate on three English IE benchmarks spanning a difficulty gradient.
9	\textbf{SciERC} \cite{luan2018scierc} contains 551 test instances annotated for joint NER (6 types) and RE (7 types).
10	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} provides 3{,}453 test sentences with 4 entity types, where models achieve ${\approx}$91\% micro F1.
11	\textbf{WNUT-17} \cite{derczynski2017wnut} consists of 1{,}287 social media instances with emerging entities, used to probe method boundaries (52\% zero F1).
12	
13	\paragraph{Models and sampling.}
14	Both \textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are fine-tuned with LoRA (rank$=$32, $\alpha{=}64$) for 5 epochs using LLaMA Factory \cite{zheng2024llamafactory} under identical training procedures, ensuring cross-architecture comparisons (at 8B scale) reflect architectural differences rather than training confounds.
15	We draw $N{=}8$ samples at $T{=}1.0$ (primary), with $N{=}16$ for scaling experiments.\footnote{$N{=}16$ results for CoNLL (Qwen) and SciERC (LLaMA) are in Table~\ref{tab:robustness} (Appendix~\ref{app:robustness}).}
16	Quality estimation uses Spearman $\rho$ and AUROC; downstream utility uses best-of-$N$ selection F1 with exact span matching (NER) and head-tail-label matching (RE).
17	Inference uses vLLM with constrained decoding \cite{willard2023guided}.
18	
19	%% ============================================================
20	\subsection{Quality Estimation Results}
21	\label{sec:qe_results}
22	
23	\begin{table*}[t]
24	\centering
25	\small
26	\caption{Quality estimation across tasks and models (Spearman $\rho$ and AUROC). Best value per block and column in \textbf{bold}. SciERC evaluates joint NER (6 types) and RE (7 types); CoNLL evaluates NER (4 types). $N{=}8$ results use seed${=}42$; $N{=}16$ results are averaged across seeds \{42, 123, 456\}.}
27	\label{tab:qu
…[truncated 11663 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 358 · 2026-05-15T06:52:25.779529+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 359 · 2026-05-15T06:52:26.281901+00:00_

1	\section{Discussion}\label{sec:discussion}
2	
3	\paragraph{Practical recommendations.}
4	For per-instance quality ranking, entity voting provides the strongest rank correlation ($\rho{=}0.38$), though exact match leads binary discrimination (AUROC${=}0.749$); under conditional filtering, EM leads on both NER and RE ($\rho{=}0.360$, $0.417$).
5	Signal rankings depend on task difficulty---EM dominates easy tasks (CoNLL), Voting and SJ dominate hard tasks (SciERC)---directionally consistent across tested model families, though with model-dependent magnitude.
6	When model capability is insufficient (WNUT-17), all signals converge toward non-significant conditional correlations (Table~\ref{tab:wnut}).
7	
8	\paragraph{Why the gap exists.}
9	Four of five signals are instance-level by construction and cannot rank $N$ candidates; the consensus-proximity strategy (\S\ref{sec:evaluation}) adds no reliable value (Table~\ref{tab:selection}).
10	Logprob, the sole per-sample signal, primarily reflects grammar compliance under constrained decoding---75\% of comparisons are effectively ties (\S\ref{sec:selection_gap}).
11	The common root is that quality estimation ranks \textit{instances}, while sample selection ranks \textit{candidates within a single instance}, requiring per-sample quality information that neither instance-level aggregation nor token-level confidence provides.
12	On SciERC, diversity-stratified analysis confirms the gap persists even among high-diversity instances (Appendix~\ref{app:diversity}); calibration analysis shows RE miscalibration (ECE 0.109--0.339; Appendix~\ref{app:calibration}) may compound this failure.
13	These signals are thus well-suited for quality-aware routing but not for discriminating among candidates.
14	
15	\paragraph{Connection to MBR decoding.}
16	Our selection strategies instantiate minimum Bayes risk (MBR) decoding \cite{eikema2022sampling}: SJ uses $U{=}\text{SJ}(y_i, y_j)$, EM uses $U{=}\mathbb{1}[y_i{=}y_j]$ (standard majority votin
…[truncated 918 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 360 · 2026-05-15T06:52:26.282383+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 361 · 2026-05-15T06:52:27.237486+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	This work provides, to our knowledge, the first multi-family comparison of confidence signals for test-time scaling in generative information extraction.
4	By comparing five signals from three families across NER and RE tasks of varying difficulty, we disentangle quality estimation from sample selection---two objectives that prior work has conflated.
5	Consistency-based signals are effective quality estimators ($\rho$ up to 0.38, AUROC up to 0.75), but we find no significant evidence that any signal surpasses greedy on best-of-$N$ selection on SciERC ($p{>}0.39$, 13--18~pp oracle headroom), a disconnect we term the \textit{correlation-selection gap}.
6	Signal rankings depend on task difficulty---exact match leads on easy tasks, structural signals on hard tasks---with this ordering directionally consistent across model families, though magnitudes are model-dependent.
7	While our NER findings are validated across three datasets, our RE conclusions rest on SciERC alone and warrant further validation.
8	
9	Trained verifiers or reward models could close the selection gap by learning per-sample quality discrimination.
10	Cross-task transfer beyond IE, scaling to larger models (70B+), and integration with conformal prediction are promising directions.
11	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 955
}
```

</details>

---


### Tool call

_source line 362 · 2026-05-15T06:52:27.288321+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 363 · 2026-05-15T06:52:27.691499+00:00_

1	Our evaluation covers three datasets but only one RE benchmark (SciERC), where 40\% of instances receive zero F1, compressing the discriminable range and limiting signal differentiation for relation extraction.
2	WNUT-17 confirms the capability boundary of our approach, but our positive results on formal-domain text (CoNLL, SciERC) have not been validated on informal or noisy text where models achieve non-trivial performance.
3	
4	We evaluate two model families (Qwen3-8B and LLaMA-3.1-8B), both at 8B parameters.
5	A 3-seed robustness analysis confirms that signal rankings are stable across seeds ($\sigma{\leq}0.025$; Table~\ref{tab:multiseed}), but whether our findings---particularly the correlation-selection gap and the difficulty-dependent signal ordering---hold for larger models (70B+) or closed-source APIs remains untested.
6	Larger models may produce higher-quality and more diverse samples, potentially altering the signal landscape.
7	
8	Our analysis of selection potential uses only unsupervised signals.
9	We do not train a dedicated verifier or reward model, leaving unknown how much of the oracle headroom a supervised approach could recover.
10	
11	We evaluate at $N{=}8$ and $N{=}16$.
12	The behavior of confidence signals at larger sample sizes (e.g., $N{=}64$ or $N{=}128$) is unknown, and $N$-scaling gains are setting-dependent: SJ improves by $+0.052$ on Qwen SciERC NER but only $+0.016$ on LLaMA SciERC NER when doubling from $N{=}8$ to $N{=}16$.
13	
14	On CoNLL with LLaMA, the SJ--FK gap is only 0.003 ($\rho{=}0.431$ vs.\ $0.428$), so the structural advantage over surface signals may not generalize to all simple-schema datasets.
15	Constrained decoding (Outlines/vLLM) enforces schema compliance, potentially compressing per-sample diversity and contributing to the correlation-selection gap beyond what free-form generation would exhibit.
16	Finally, log-probability was excluded from the temperature comparison ($T{=}0.7$ vs.\ $T{=}1.0$) due to missing $T{=}0
…[truncated 307 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 403
}
```

</details>

---


### Tool call

_source line 364 · 2026-05-15T06:52:27.691876+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 365 · 2026-05-15T06:52:28.495309+00:00_

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
21	$c_{\text{vote}}$ & Entity voting confidence \\
22	$c_{\text{lp}}$ & Log-probability (mean token log-likelihood) \\
23	\bottomrule
24	\end{tabular}
25	\caption{Notation used throughout the paper.}
26	\label{tab:notation}
27	\end{table}
28	
29	\section{Robustness Analysis}\label{app:robustness}
30	
31	\begin{table}[t]
32	\centering
33	\small
34	\caption{Signal robustness across configurations (Spearman $\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: cross-architecture transfer (LLaMA CoNLL $N{=}16$, 3-seed mean $\pm\sigma$). $^\dagger$Mean over 3 seeds ($\sigma{=}0.025$; individual: 0.428, 0.424, 0.384).}
35	\label{tab:robustness}
36	\begin{tabular}{llcc}
37	\toprule
38	& & NER $\rho$ & RE $\rho$ \\
39	\midrule
40	\multicolumn{4}{l}{\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\
41	\quad SJ & $T{=}0.7$ & 0.388 & 0.234 \\
42	\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\
43	\quad FK & $T{=}0.7$ & 0.321 & 0.184 \\
44	\quad FK & $T{=}1.0$ & 0.267 & 0.275 \\
45	\midrule
46	\multicolumn{4}{l}{\textit{Sample size} (Qwen SciERC, $T{=}1.0$)} \\
47	\quad SJ & $N{=}8$  & 0.360 & 0.250 \\
48	\quad SJ & $N{=}16$ & 0.412$^\dagger$ & 0.281 \\
49	\quad FK & $N{=}8$  & 0.267 & 0.275 \\
50	\quad FK & $N{=}16$ & 0.280 & 0.279 \\
51	\midrule
52	\multicolumn{4}{l}{\textit{Cross-architecture} (LLaMA CoNLL, $N{=}16$, 3 seeds)} \\
53	\quad SJ &  & $0.463{\pm}0.007$ & --- \\
54	\quad FK &  & $0.455{\pm}0.006$ & --- \\
55	\quad EM &
…[truncated 21352 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 803
}
```

</details>

---


### Tool call

_source line 366 · 2026-05-15T06:52:28.495687+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR review form 2025 2026 soundness excitement overall scoring scale criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR review form 2025 2026 soundness excitement overall scoring scale criteria"
  }
}
```

</details>

---


### Tool result

_source line 367 · 2026-05-15T06:52:36.879295+00:00_

Web search results for query: "ACL ARR review form 2025 2026 soundness excitement overall scoring scale criteria"

Links: [{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"ACL 2023 Acceptance Recommendations - ACL 2023","url":"https://2023.aclweb.org/blog/overall-recommendation/"},{"title":"ACL 2026 on X: \"Checkout the blog post on the soundness/excitement scores https://t.co/AKSO9DjiYP . It clarifies the reasoning behind the separation of overall scores and how it might make the reviewer recommendation more robust. #ACL2023Toronto #ACL2023NLP #NLProc\" / X","url":"https://x.com/aclmeeting/status/1637827267173953540"},{"title":"aclrollingreview/reviewerguidelines.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewerguidelines.md"},{"title":"Program Chairs’ Report on Peer Review at ACL 2023 Anna Rogers}","url":"https://aclanthology.org/2023.acl-long.report.pdf"},{"title":"ACL’23 Peer Review Policies - ACL 2023","url":"https://2023.aclweb.org/blog/review-acl23/"},{"title":"The 6th Trustworthy NLP Workshop at ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/6th-trustworthy-nlp-workshop-acl-2026"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"}]

Based on the search results, here's information about the ACL ARR review form for 2025-2026:

## Three Score Categories

Starting with February 2025, ARR reviewers 
…[truncated 1592 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8383
}
```

</details>

---


### Tool call

_source line 368 · 2026-05-15T06:52:41.347824+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
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

_source line 369 · 2026-05-15T06:52:41.448659+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 370 · 2026-05-15T06:52:45.669358+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete scoring scales for: 1) Soundness (all score levels and descriptions), 2) Excitement (all score levels), 3) Overall Recommendation (all score levels), 4) Confidence score, 5) Any other scored dimensions like Reproducibility. List every numeric score level with its exact description text."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete scoring scales for: 1) Soundness (all score levels and descriptions), 2) Excitement (all score levels), 3) Overall Recommendation (all score levels), 4) Confidence score, 5) Any other scored dimensions like Reproducibility. List every numeric score level with its exact description text."
  }
}
```

</details>

---


### Tool result

_source line 371 · 2026-05-15T06:52:56.164144+00:00_

# ACL Rolling Review Scoring Scales

## 1) Soundness
- **5** = "Excellent: This study is one of the most thorough I have seen, given its type."
- **4.5** = (No description provided)
- **4** = "Strong: This study provides sufficient support for all of its claims. Some extra experiments could be nice, but not essential."
- **3.5** = (No description provided)
- **3** = "Acceptable: This study provides sufficient support for its main claims. Some minor points may need extra support or details."
- **2.5** = (No description provided)
- **2** = "Poor: Some of the main claims are not sufficiently supported. There are major technical/methodological problems."
- **1.5** = (No description provided)
- **1** = "Major Issues: This study is not yet sufficiently thorough to warrant publication or is not relevant to ACL."

## 2) Excitement
- **5** = "Highly Exciting: I would recommend this paper to others and/or attend its presentation in a conference."
- **4.5** = (No description provided)
- **4** = "Exciting: I would mention this paper to others and/or make an effort to attend its presentation in a conference."
- **3.5** = (No description provided)
- **3** = "Interesting: I might mention some points of this paper to others and/or attend its presentation if there's time."
- **2.5** = (No description provided)
- **2** = "Potentially Interesting: this paper does not resonate with me, but it might with others in the *ACL community."
- **1.5** = (No description provided)
- **1** = "Not Exciting: this paper does not resonate with me, and I don't think it would with others in the *ACL community."

## 3) Overall Assessment (Recommendation)
- **5** = "Consider for Award: I think this paper could be considered for an outstanding paper award at an *ACL conference (up to top 2.5% papers)."
- **4.5** = Borderline Award
- **4** = "Conference: I think this paper could be accepted to an *ACL conference."
- **3.5** = Borderline Conference
- **3** = "Findings: I think this paper could be accepted t
…[truncated 2004 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 10494
}
```

</details>

---


### Tool call

_source line 372 · 2026-05-15T06:56:39.596222+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 — Round 4 审稿报告\n\n**Overall**: 3.0 (Findings)\n**Soundness**: 3.5 | **Excitement**: 2.5 | **Reproducibility**: 3 | **Confidence**: 4\n\n### Round 3 修复状态总览\n- **RESOLVED (8/13)**: R3-C2 (TOST已补), R3-C3 (3-seed已补), R3-W1 (Bonferroni已补), R3-W3 (MBR连接已补), R3-W4 (FK excess agreement数据已补), R3-W5 (cross-architecture统一), R3-W8 (引用已补全), R0-C3 (RE claim已降级), R1-W1 (SJ形式化已完善)\n- **PARTIALLY RESOLVED (4/13)**: R3-C1 (constrained decoding承认但未量化), R3-W2 (gap tautology改善但核心张力仍在), R3-W6 (hedge加在Conclusion但Introduction仍断言式), R3-W7 (表格缩写VC/Voting Conf.不统一)\n- **UNRESOLVED (1/13)**: 无完全未解决的问题\n\n### 新发现的 Must-Fix (2个)\n1. **N1 [critical] Contribution #2 非平凡性不足**: 4/5 信号是 instance-level 的，其 selection 失败是定义性推论。真正的经验贡献是 logprob（唯一 per-sample 信号）也失败了，但论文对此区分不清晰。建议重新 frame：区分 \"定义性 gap\"（instance-level 信号）和\"经验性 gap\"（logprob 也失败），后者才是需要实验验证的贡献。\n2. **N2 [critical] Prompt template 和 fine-tuning 数据细节缺失**: 附录无 prompt template、training split、schema constraint 定义，影响独立复现。\n\n### Should-Fix (5个)\n- W1: Constrained decoding 对 logprob 信号语义的影响未充分讨论（R3-C1延续）\n- W2: Ethics Statement 应为独立 section 而非 Limitations 内 paragraph\n- W3: 表格缩写不统一（Voting Conf. vs VC）\n- W4: Introduction novelty claim 缺 hedge（Conclusion 有但 Introduction 无）\n- W5: Table 1 N=16 block 大面积空白，未引导读者到附录\n\n### 主要优势\n统计方法论显著改进（TOST/bootstrap CI/Bonferroni/3-seed）、多层面评估框架设计合理、MBR 连接清晰、条件过滤分析有洞察力、claims 范围审慎。\n\n### 判断\n推荐 Findings 接收，条件是 N1（framing 调整区分定义性/经验性 gap）和 N2（prompt template 补充）得到修复。论文经四轮迭代已达到较高的统计严谨度。",
  "reviewer_id": "2",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 — Round 4 审稿报告\n\n**Overall**: 3.0 (Findings)\n**Soundness**: 3.5 | **Excitement**: 2.5 | **Reproducibility**: 3 | **Confidence**: 4\n\n### Round 3 修复状态总览\n- **RESOLVED (8/13)**: R3-C2 (TOST已补), R3-C3 (3-seed已补), R3-W1 (Bonferroni已补), R3-W3 (MBR连接已补), R3-W4 (FK excess agreement数据已补), R3-W5 (cross-architecture统一), R3-W8 (引用已补全), R0-C3 (RE claim已降级), R1-W1 (SJ形式化已完善)\n- **PARTIALLY RESOLVED (4/13)**: R3-C1 (constrained decoding承认但未量化), R3-W2 (gap tautology改善但核心张力仍在), R3-W6 (hedge加在Conclusion但Introduction仍断言式), R3-W7 (表格缩写VC/Voting Conf.不统一)\n- **UNRESOLVED (1/13)**: 无完全未解决的问题\n\n### 新发现的 Must-Fix (2个)\n1. **N1 [critical] Contribution #2 非平凡性不足**: 4/5 信号是 instance-level 的，其 selection 失败是定义性推论。真正的经验贡献是 logprob（唯一 per-sample 信号）也失败了，但论文对此区分不清晰。建议重新 frame：区分 \"定义性 gap\"（instance-level 信号）和\"经验性 gap\"（logprob 也失败），后者才是需要实验验证的贡献。\n2. **N2 [critical] Prompt template 和 fine-tuning 数据细节缺失**: 附录无 prompt template、training split、schema constraint 定义，影响独立复现。\n\n### Should-Fix (5个)\n- W1: Constrained decoding 对 logprob 信号语义的影响未充分讨论（R3-C1延续）\n- W2: Ethics Statement 应为独立 section 而非 Limitations 内 paragraph\n- W3: 表格缩写不统一（Voting Conf. vs VC）\n- W4: Introduction novelty claim 缺 hedge（Conclusion 有但 Introduction 无）\n- W5: Table 1 N=16 block 大面积空白，未引导读者到附录\n\n### 主要优势\n统计方法论显著改进（TOST/bootstrap CI/Bonferroni/3-seed）、多层面评估框架设计合理、MBR 连接清晰、条件过滤分析有洞察力、claims 范围审慎。\n\n### 判断\n推荐 Findings 接收，条件是 N1（framing 调整区分定义性/经验性 gap）和 N2（prompt template 补充）得到修复。论文经四轮迭代已达到较高的统计严谨度。",
    "reviewer_id": "2",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 373 · 2026-05-15T06:56:43.512687+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3916
}
```

</details>

---


### Assistant

_source line 374 · 2026-05-15T06:56:49.314370+00:00_

审稿报告已提交给 Review Director。

总结：Round 4 审稿完成。论文统计方法论显著改进，Round 3 的 13 个问题中 8 个完全解决、4 个部分解决。新发现 2 个 Must-Fix：(1) correlation-selection gap 的非平凡性论证需区分定义性结果与经验性发现，(2) prompt template 等训练细节缺失影响复现。整体评分 Overall 3.0 (Findings)，推荐条件接收。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2"
}
```

</details>

---


## Round 11

## Round 11

4 recorded events


### User

_source line 375 · 2026-05-15T06:56:50.604233+00:00_

[Round 4 审稿请求]:
## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见

以下是 Reviewer 1 的完整审稿报告。请对每个 Must-Fix 和 Should-Fix 逐条回应：
- **[AGREE]** 同意并说明理由
- **[REBUT]** 反驳并提供证据（引用论文具体 Section/Table/Figure）

---

## Reviewer 1 — 审稿报告

**Overall**: 3.0 / 5（Findings acceptance 边缘）

### 维度打分
| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5 / 5 | 统计方法论优秀，但核心 claim 非平凡性受质疑；constrained decoding confound 未验证 |
| Excitement | 3.0 / 5 | 填补了 QE vs. selection 区分空白，但本质是 negative result + 对已知设计限制的实证确认 |
| Reproducibility | 3.0 / 5 | 使用公开数据和开源模型，但 LoRA 训练缺关键超参（lr, batch size, warmup, prompt template） |
| Confidence | 4 / 5 | 熟悉相关文献 |

### 主要优势
1. 研究问题定义清晰（QE vs. selection 区分）
2. 统计方法论严谨（bootstrap B=10,000, TOST, Cohen's d, multi-seed）
3. Difficulty gradient 分析有深度（CoNLL→SciERC→WNUT-17 + conditional filtering）
4. Transparency：自身局限性讨论诚实全面
5. MBR decoding 连接有价值
6. 引用质量高（55 条，0 orphan，51 条 OpenAlex 验证通过）

### Must-Fix

**N1** [critical] Correlation-selection gap 非平凡性不足——instance-level 信号的 selection 失败部分为 tautological
- §3.1: 5 个信号中 4 个是 instance-level，consensus-proximity 转换等价于 MBR decoding
- 论文将 "所有信号均未超越 greedy" 包装为统一经验发现，但 instance-level 信号的 selection 失败主要是**设计层面的先验预期**
- 真正非平凡的发现是 **logprob 的 selection 失败**（SciERC +0.6pp, p=0.39, Cohen's d=0.038），但被淹没在统一叙述中
- Discussion 承认 "Four of five signals are instance-level by construction" 但这与 §4.3/abstract 的 core empirical contribution 定位存在张力
- 建议：(a) 明确分离 instance-level 失败（by-design）和 logprob 失败（empirical）为两个独立发现；(b) 重定义 gap scope 聚焦 "consensus-proximity/MBR selection 在 structured IE 上失败"

**N2** [critical] Constrained decoding 作为 correlation-selection gap 的 confounding factor 未被实验量化
- §4.1 使用 vLLM + Outlines constrained decoding
- 可能从两方面 confound：(1) 压缩 per-sample diversity；(2) 使 logprob 主要反映 grammar compliance
- 论文报告 SciERC 43% unique outputs + per-sample F1 std=0.14，但不排除 diversity 被压缩到 constrained 子空间
- §5 承认 "75% of comparisons are effectively ties" 但归因于 logprob 特性而非实验设置
- 建议：(a) 增加 free-form generation 对照；(b) 或分析 logprob 分布——在 non-tie 的 25% 上 logprob 是否能成功 select；(c) 区分 logprob 值差异小（grammar path 导致）vs. 差异大但与 F1 无关

**N3** [critical] 训练细节不足以复现
- §4.1: LoRA rank=32, α=64, 5 epochs, LLaMA Factory——但缺少：
  - learning rate, batch size, warmup, weight decay, optimizer
  - early stopping 策略, train/dev split
  - prompt template（NER/RE 各用什么格式？）
  - LoRA target modules, max sequence length
- LoRA 微调对 lr 和 target modules 敏感，不同配置可能影响 output diversity 和信号表现

### Should-Fix

**W1** [warning] RE 结论仅基于 SciERC 单一数据集
- SciERC 40% zero-F1，RE gap 证据薄弱（-0.9pp, p=0.80）
- Abstract/Introduction 将 RE 作为等权证据呈现
- 建议增加 RE 数据集或降级 RE claim 为 preliminary

**W2** [warning] Fleiss' κ 应用于非独立 temperature-sampled outputs 的理论 justification 薄弱
- FK 假设独立 raters，但 temperature sampling 共享模型权重/prompt/前缀
- excess agreement (-0.4% to -4.0%) 的 baseline 和 negative 值含义不清
- 建议解释 excess agreement 计算方法或限定 FK 为"经验度量"

**W3** [warning] Soft Jaccard normalizer 选择缺乏对比
- max(|g_i|, |g_j|) vs. |g_i ∪ g_j| 未比较
- 建议至少在附录报告替代 normalizer 结果

**W4** [warning] 模型规模限于 8B
- Larger models 可能改变 signal landscape（logprob 在更强模型上可能更有区分力）
- 建议讨论 model scale 对 gap 方向的影响

**W5** [warning] TOST δ 选择缺乏依据
- ±2, ±3, ±5 pp 的选择未讨论合理性
- 建议提供 δ 选择的实际意义论证

**W6** [warning] N=8 主实验的 single-seed 稳定性
- Table 1, Table 3 N=8 均 seed=42 单次运行
- Appendix D 3-seed 分析仅覆盖 SciERC NER（Table 7），不覆盖 CoNLL N=8 和 SciERC RE
- 建议补多 seed 或注明局限

### 小问题
- semantic entropy footnote 不可比数字可能误导
- Table 1 N=16 区域不完整
- Entity Voting 公式分母为 0 的边界条件
- Appendix Fig 3 ECE bin 数量未报告

### 缺失引用
- Bertsch et al. (2024) "In-Context Learning with Long-Context Models"
- Wiher et al. (2022) "On Decoding Strategies for Neural Text Generators"
- Müller & Sennrich (2021) "Understanding the Properties of MBR Decoding in NMT"

---

请逐条回应以上所有 Must-Fix 和 Should-Fix 问题。特别关注：
1. 你是否同意 N3（训练细节不足）的严重性评估？
2. 你对 W2（FK 独立性）和 W3（SJ normalizer）的看法？
3. R1 提出的 3 篇缺失引用你是否认同？

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 376 · 2026-05-15T06:59:13.345062+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 交叉回应 — 对 Reviewer 1 审稿报告的逐条意见\n\n### Must-Fix 共识度\n- **R1-N1 (gap 非平凡性)**: [AGREE] 与我的 N1 独立一致，进一步佐证此问题的核心性。补充：Abstract \"any signal\" 措辞混淆了定义性失败和经验性失败。\n- **R1-N2 (constrained decoding confound)**: [AGREE with severity downgrade → should-fix] 论文已有 diversity-stratified 分析作为间接证据。但赞同 R1 建议 (b)：分析 logprob non-tie 25% 上的 selection 表现——成本低且直接回答 logprob 失败根因。\n- **R1-N3 (训练细节不足)**: [AGREE] 与我的 N2 一致。R1 的列举更完整（lr, batch size, optimizer, LoRA target modules）。\n\n### Should-Fix 共识度\n- **R1-W1 (RE 单数据集)**: [REBUT] 论文已在 4 处显式声明限制并降级 claim。\n- **R1-W2 (FK 独立性)**: [PARTIALLY AGREE] 论证方向正确（excess agreement 为负→FK 保守），但需补充计算方法说明。\n- **R1-W3 (SJ normalizer)**: [WEAKLY AGREE] 有 rationale，ablation 为 nice-to-have。\n- **R1-W4 (8B 限制)**: [REBUT] Limitations 已充分讨论。\n- **R1-W5 (TOST δ 选择)**: [AGREE] 需补充 practical significance 论证。\n- **R1-W6 (single-seed)**: [PARTIALLY AGREE] SciERC RE single-seed 是最弱环节，建议 Limitations 补一句。\n\n### 缺失引用\n- Bertsch et al. 2024: [REBUT] ICL focus，与 fine-tuned 模型的 confidence signals 关联薄弱\n- Wiher et al. 2022: [WEAKLY AGREE] 边际相关\n- Müller & Sennrich 2021: [AGREE] 与 MBR discussion 直接呼应，应补引用\n\n### 两位 Reviewer 的核心共识\n1. **Contribution #2 framing 需调整**（R1-N1 = R2-N1）——两位 reviewer 独立指出同一问题，高置信度\n2. **训练细节必须补充**（R1-N3 = R2-N2）——prompt template 缺失尤其关键\n3. **Constrained decoding 对 logprob 的影响需深化讨论**——R1 评为 critical，R2 评为 should-fix，建议折中处理：分析 non-tie subset + 补充 Discussion 段落\n\n### 分歧点\n- R1-W1 (RE 单数据集)：R1 认为需进一步降级，R2 认为已充分处理\n- R1-N2 严重性：R1 评 critical，R2 评 should-fix（基于已有 diversity 分析）",
  "reviewer_id": "2",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 交叉回应 — 对 Reviewer 1 审稿报告的逐条意见\n\n### Must-Fix 共识度\n- **R1-N1 (gap 非平凡性)**: [AGREE] 与我的 N1 独立一致，进一步佐证此问题的核心性。补充：Abstract \"any signal\" 措辞混淆了定义性失败和经验性失败。\n- **R1-N2 (constrained decoding confound)**: [AGREE with severity downgrade → should-fix] 论文已有 diversity-stratified 分析作为间接证据。但赞同 R1 建议 (b)：分析 logprob non-tie 25% 上的 selection 表现——成本低且直接回答 logprob 失败根因。\n- **R1-N3 (训练细节不足)**: [AGREE] 与我的 N2 一致。R1 的列举更完整（lr, batch size, optimizer, LoRA target modules）。\n\n### Should-Fix 共识度\n- **R1-W1 (RE 单数据集)**: [REBUT] 论文已在 4 处显式声明限制并降级 claim。\n- **R1-W2 (FK 独立性)**: [PARTIALLY AGREE] 论证方向正确（excess agreement 为负→FK 保守），但需补充计算方法说明。\n- **R1-W3 (SJ normalizer)**: [WEAKLY AGREE] 有 rationale，ablation 为 nice-to-have。\n- **R1-W4 (8B 限制)**: [REBUT] Limitations 已充分讨论。\n- **R1-W5 (TOST δ 选择)**: [AGREE] 需补充 practical significance 论证。\n- **R1-W6 (single-seed)**: [PARTIALLY AGREE] SciERC RE single-seed 是最弱环节，建议 Limitations 补一句。\n\n### 缺失引用\n- Bertsch et al. 2024: [REBUT] ICL focus，与 fine-tuned 模型的 confidence signals 关联薄弱\n- Wiher et al. 2022: [WEAKLY AGREE] 边际相关\n- Müller & Sennrich 2021: [AGREE] 与 MBR discussion 直接呼应，应补引用\n\n### 两位 Reviewer 的核心共识\n1. **Contribution #2 framing 需调整**（R1-N1 = R2-N1）——两位 reviewer 独立指出同一问题，高置信度\n2. **训练细节必须补充**（R1-N3 = R2-N2）——prompt template 缺失尤其关键\n3. **Constrained decoding 对 logprob 的影响需深化讨论**——R1 评为 critical，R2 评为 should-fix，建议折中处理：分析 non-tie subset + 补充 Discussion 段落\n\n### 分歧点\n- R1-W1 (RE 单数据集)：R1 认为需进一步降级，R2 认为已充分处理\n- R1-N2 严重性：R1 评 critical，R2 评 should-fix（基于已有 diversity 分析）",
    "reviewer_id": "2",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 377 · 2026-05-15T06:59:17.511768+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4166
}
```

</details>

---


### Assistant

_source line 378 · 2026-05-15T06:59:23.479592+00:00_

交叉回应已提交给 Director。

核心结论：两位 Reviewer 在两个关键问题上达成独立共识——(1) gap framing 需区分定义性/经验性失败，(2) 训练细节必须补充。对 constrained decoding confound 的严重性有分歧（R1: critical, R2: should-fix），建议折中处理。R1 提出的 3 篇缺失引用中仅 Müller & Sennrich 2021 值得补充。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2"
}
```

</details>

---


## Round 12

## Round 12

54 recorded events


### User

_source line 379 · 2026-05-15T07:52:05.885738+00:00_

[Round 1 审稿请求]:
## 审稿任务 — Reviewer 2 (Round 1)

### Venue 信息
- **Target**: EMNLP 2026 Findings (via ARR May 2026 cycle)
- **Deadline**: 2026-05-25
- **页数限制**: 正文 8 页 + unlimited references
- **模板**: ACL format (`\usepackage[review]{acl}`)
- **匿名规则**: Double-blind
- **Limitations section**: 必须，位于 Conclusion 后、References 前，不计页数
- **附录**: 允许，不计页数

### 论文路径
`projects/struct_self_consist_ie/docs/paper/main.tex`
（各 section 在 `sections/` 子目录下）

### 你的审查侧重：新颖性 + framing + related work 完整性 + 写作质量

请重点评估以下方面：

1. **新颖性与贡献**
   - "correlation-selection gap" 作为概念贡献是否有足够新颖性？（注意：4/5 信号是 instance-level，定义上无法做 sample selection——这部分论证中有多少是 trivial/tautological 的？）
   - 与 Nédellec et al. (2026) 的增量贡献是否充分论证？
   - Soft Jaccard 作为方法贡献的新颖性如何？
   - 三个 contribution 的每一个是否都有实质性新知识？

2. **Framing 与 claim scope**
   - 论文的核心 narrative 是否自洽？（Abstract → Introduction → Conclusion 的 claim 一致性）
   - "first multi-family comparison" 的 claim 是否准确？scope 是否被恰当限定？
   - Abstract 是否过于密集？是否首次阅读即可把握核心信息？
   - RE 被标记为 "preliminary" 但在多处仍作为主要证据——framing 是否一致？

3. **Related Work 完整性**
   - 引用是否覆盖了该领域的核心文献？
   - 是否遗漏了重要的相关工作？特别关注：
     - LLM confidence/uncertainty estimation 领域的核心论文
     - Self-consistency 的最新变体
     - MBR decoding 在非 MT 领域的应用
     - 结构化预测不确定性估计
   - 与已有工作的对比定位是否公允（不过度贬低或忽略先前工作）？

4. **写作质量**
   - 术语使用是否一致？（confidence signal vs consistency signal; VC vs Voting Conf. 等）
   - 论文整体组织结构是否清晰？
   - 图表是否有效传达信息？caption 是否自足？
   - Ethics Statement 的位置和内容是否符合 ACL 要求？
   - Limitations section 是否诚实全面？

5. **格式合规性**
   - 是否符合 ACL 模板要求？
   - 正文是否在 8 页内？
   - 匿名性是否保持（无 self-citation 泄露）？
   - 引用格式是否正确？

请按 EMNLP 审稿标准给出完整审稿报告，包含：Summary、Strengths、Weaknesses (must-fix / should-fix / minor)、Questions、Missing References、Overall Assessment（评分 + 置信度）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 380 · 2026-05-15T07:52:12.410468+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 381 · 2026-05-15T07:52:12.461407+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/review_reviewer_2_a0c838f5.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 382 · 2026-05-15T07:52:14.368716+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review-reviewer-session-start.skill.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review-reviewer-session-start.skill.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1"
  }
}
```

</details>

---


### Tool result

_source line 383 · 2026-05-15T07:52:14.419478+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 384 · 2026-05-15T07:52:16.679390+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.skill.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.skill.md",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1"
  }
}
```

</details>

---


### Tool result

_source line 385 · 2026-05-15T07:52:16.780253+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 386 · 2026-05-15T07:52:21.097508+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
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

_source line 387 · 2026-05-15T07:52:21.148172+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 388 · 2026-05-15T07:52:27.375917+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 389 · 2026-05-15T07:52:27.727774+00:00_

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
15	\usepackage{multirow}
16	\usepackage{xcolor}
17	\usepackage{subcaption}
18	
19	\graphicspath{{figures/}}
20	
21	\title{Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence Signals for Test-Time Scaling in Information Extraction}
22	
23	\author{Anonymous}
24	
25	\begin{document}
26	\maketitle
27	
28	\input{sections/abstract}
29	\input{sections/introduction}
30	\input{sections/related_work}
31	\input{sections/method}
32	\input{sections/experiments}
33	\input{sections/discussion}
34	\input{sections/conclusion}
35	
36	\section*{Limitations}
37	\input{sections/limitations}
38	
39	\section*{Ethics Statement}
40	All experiments use publicly available benchmarks (SciERC, CoNLL-2003, WNUT-17) and open-weight models (Qwen3-8B, LLaMA-3.1-8B).
41	No new human data was collected or annotated for this study.
42	
43	\bibliography{references}
44	
45	\appendix
46	\input{sections/appendix}
47	
48	\end{document}
49	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 390 · 2026-05-15T07:52:27.728164+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2026 review form criteria scoring rubric"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 review form criteria scoring rubric"
  }
}
```

</details>

---


### Tool call

_source line 391 · 2026-05-15T07:52:28.234823+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "projects/struct_self_consist_ie/docs/paper/sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "projects/struct_self_consist_ie/docs/paper/sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1"
  }
}
```

</details>

---


### Tool result

_source line 392 · 2026-05-15T07:52:28.837474+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 602
}
```

</details>

---


### Tool call

_source line 393 · 2026-05-15T07:52:28.988366+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 394 · 2026-05-15T07:52:35.265423+00:00_

Web search results for query: "ACL ARR 2026 review form criteria scoring rubric"

Links: [{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"ACL ARR 2026 | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026"},{"title":"ACL ARR 2026 March | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026%2FMarch"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"}]

Based on my search results, here's information about the ACL ARR 2026 review form criteria and scoring rubric:

## Scoring System

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

## Soundness and Excitement Scores

The Overall assessment score is an explicit recommendation for the outcome of this paper, 
…[truncated 1241 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7537
}
```

</details>

---


### Tool result

_source line 395 · 2026-05-15T07:53:31.570112+00:00_

{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 58, \"total_citations\": 84, \"unique_cited_keys\": 58, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 52, \"online_not_found\": 2, \"online_mismatch\": 4}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"angelopoulos2021conformal\", \"type\": \"inproceedings\", \"title\": \"Uncertainty Sets for Image Classifiers using Conformal Prediction\", \"authors\": \"Angelopoulos, Anastasios N. and Bates, Stephen and Malik, Jitendra and Jordan, M...\", \"year\": \"2021\", \"venue\": \"ICLR 2021\"}, {\"key\": \"brown2024monkeys\", \"type\": \"article\", \"title\": \"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\", \"authors\": \"Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, ...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2407.21787\"}, {\"key\": \"chen2024usc\", \"type\": \"inproceedings\", \"title\": \"Universal Self-Consistency for Large Language Model Generation\", \"authors\": \"Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Y...\", \"year\": \"2024\", \"venue\": \"arXiv preprint (ICML 2024 Workshop ICL)\"}, {\"key\": \"cobbe2021verifiers\", \"type\": \"article\", \"title\": \"Training Verifiers to Solve Math Word Problems\", \"authors\": \"Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, ...\", \"year\": \"2021\", \"venue\": \"arXiv preprint arXiv:2110.14168\"}, {\"key\": \"culotta2004confidence\", \"type\": \"inproceedings\", \"title\": \"Confidence Estimation for Information Extraction\", \"authors\": \"Culotta, Aron and McCallum, Andrew\", \"year\": \"2004\", \"venue\": \"HLT-NAACL 2004\"}, {\"key\": \"derczynski2017wnut\", \"type\": \"inproceedings\", \"title\": \"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recogniti
…[truncated 46238 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 62581
}
```

</details>

---


### Tool call

_source line 396 · 2026-05-15T07:53:38.450313+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/docs/paper/sections/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/docs/paper/sections/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1"
  }
}
```

</details>

---


### Tool result

_source line 397 · 2026-05-15T07:53:38.652296+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 201
}
```

</details>

---


### Tool call

_source line 398 · 2026-05-15T07:53:38.652622+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
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

_source line 399 · 2026-05-15T07:53:38.753262+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 400 · 2026-05-15T07:53:40.911727+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 401 · 2026-05-15T07:53:41.414016+00:00_

1	\begin{abstract}
2	Test-time scaling through multi-sample generation promises quality improvements for LLM-based information extraction, but which confidence signals best serve quality estimation versus sample selection remains unclear.
3	We systematically compare five confidence signals from three families---structural (entity voting, Soft Jaccard), surface (exact match, Fleiss' $\kappa$), and model-internal (log-probability)---across NER (three datasets of varying difficulty) and RE (SciERC, preliminary) with two model families (Qwen3-8B, LLaMA-3.1-8B).
4	For quality estimation, the strongest signals achieve $\rho{=}0.38$ (entity voting) and AUROC${=}0.75$ (exact match), with ranking and classification favoring different signals across task complexity.
5	However, this strong estimation does not translate into selection gains: four of five signals are instance-level by construction, and log-probability---the only per-sample signal---also fails to outperform greedy decoding on SciERC ($p{>}0.39$, bootstrap) despite 13--18~pp of oracle headroom.
6	We term this the \textit{correlation-selection gap}.
7	Signal rankings further depend on task difficulty---exact match dominates easy tasks, structural signals dominate hard tasks---with consistent ordering direction across models but model-dependent magnitude; when model capability is insufficient, apparent correlations are driven by zero/non-zero separation rather than genuine quality gradation.
8	These results reframe consistency signals as quality estimators rather than output selectors for structured IE.
9	\end{abstract}
10	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 402 · 2026-05-15T07:53:41.414409+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 403 · 2026-05-15T07:53:41.816105+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Self-consistency---sampling multiple outputs and aggregating them---has become a powerful strategy for improving language model reasoning.
4	On discrete-answer tasks such as arithmetic and commonsense QA, majority voting over chain-of-thought samples yields large gains: +18 percentage points on GSM8K (PaLM-540B; \citealp{wang2023selfconsistency}).
5	More broadly, test-time compute scaling through repeated sampling and selection has emerged as a complementary axis to model scaling, offering substantial quality improvements at inference time \cite{snell2024scaling, brown2024monkeys}.
6	These results rest on a shared assumption: that among $N$ stochastic samples, a selection mechanism can identify better outputs.
7	For tasks with a single correct answer, this assumption holds naturally---the majority vote is the selector.
8	But information extraction (IE) poses a fundamentally different challenge.
9	The output is not a single token or number; it is a \textit{set} of entities or relations with internal dependencies, where two samples may extract overlapping but non-identical structures.
10	There is no obvious majority to vote on, partial agreement is the norm rather than the exception, and the space of valid outputs is combinatorially large.
11	Can self-consistency still provide useful signal in this structured setting?
12	
13	Prior work on confidence estimation for LLM-based IE has conflated two distinct objectives: \textit{quality estimation} (which inputs does the model handle reliably?) and \textit{sample selection} (which of $N$ outputs is best?).
14	These require fundamentally different signal properties: the former benefits from instance-level aggregation, while the latter demands per-sample discrimination.
15	Self-consistency methods for discrete answers \cite{wang2023selfconsistency, chen2024usc} and weighted variants \cite{taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalen
…[truncated 4876 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 404 · 2026-05-15T07:53:41.866726+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 405 · 2026-05-15T07:53:43.021562+00:00_

1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Self-consistency and test-time scaling.}
4	Self-consistency decoding \cite{wang2023selfconsistency} improves reasoning by majority voting over chain-of-thought samples, assuming a discrete answer space.
5	Extensions to free-form text use LLM-based comparison \cite{chen2024usc}, atomic sub-claim decomposition \cite{thirukovalluru2024atomic}, or cross-sample hallucination detection \cite{manakul2023selfcheckgpt}.
6	For test-time scaling, \citet{snell2024scaling} characterize compute scaling laws and \citet{brown2024monkeys} show best-of-$N$ gains across tasks.
7	Recent reward-free selectors include confidence-weighted voting \cite{taubenfeld2025cisc}, KL-based self-certainty \cite{kang2025selfcertainty}, adaptive sampling \cite{kim2026reasc}, ranked aggregation \cite{wang2025rankedvoting}, and latent-space consistency \cite{oh2025latentsc}.
8	Concurrently, \citet{feng2025optimal} and \citet{wang2025make} adapt self-consistency to difficulty-aware settings, echoing our finding that signal rankings shift with task complexity; \citet{li2025llms} propose generative self-aggregation for IE but focus on output fusion rather than confidence-based selection.
9	All of the above target reasoning/QA with discrete answers or specific aggregation strategies.
10	Our work extends self-consistency to set-valued structured outputs and identifies the correlation-selection gap: strong quality estimation ($\rho{=}0.38$) coexists with selection failure ($p{>}0.39$).
11	
12	\paragraph{Consistency for structured IE.}
13	\citet{nedellec2026consistency} study consistency--accuracy correlations for LLM-based NER/RE, corroborating our quality-estimation findings.
14	Their work leaves open three questions we address: (i)~whether structural matching improves on surface-level agreement (which they acknowledge ``overlooks semantically consistent outputs''); (ii)~whether quality estimation translates to best-of-$N$ selection; and (iii)~whet
…[truncated 3430 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1154
}
```

</details>

---


### Tool call

_source line 406 · 2026-05-15T07:53:43.323362+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 407 · 2026-05-15T07:53:43.323822+00:00_

1	\section{Method}\label{sec:method}
2	
3	\subsection{Problem Formulation}\label{sec:formulation}
4	
5	Given a language model $\mathcal{M}$ and input $x$, we sample $N$ structured outputs $\{y_1, \ldots, y_N\}$ at temperature $T > 0$ via constrained decoding \cite{willard2023guided}.
6	Each $y_i$ is an entity set (NER) or relation set (RE).
7	A confidence signal $c$ serves two purposes: (a) \textit{quality estimation}---predicting which instances the model handles reliably, and (b) \textit{sample selection}---identifying the best output among $N$ candidates.
8	
9	A \textbf{per-sample signal} scores each $y_i$ independently, $c_{\text{ps}}: (x, y_i) \to \mathbb{R}$, enabling direct candidate ranking.
10	An \textbf{instance-level signal} aggregates over all $N$ samples, $c_{\text{il}}: (x, \{y_i\}_{i=1}^N) \to \mathbb{R}$, producing a single score per input.
11	This asymmetry---between predicting \textit{which inputs} are easy and selecting \textit{which output} is best---is central to the correlation-selection gap we investigate.
12	Notation is summarized in Appendix~\ref{app:notation}.
13	
14	\subsection{Confidence Signals}\label{sec:signals}
15	
16	We use \textit{confidence signal} as the umbrella term for all five measures.
17	Four are \textit{consistency signals}---computed from inter-sample agreement---spanning two families: \textit{structural} (Soft Jaccard, entity voting) and \textit{surface} (exact match, Fleiss' $\kappa$).
18	The fifth, log-probability, is the sole \textit{model-internal} signal and the only one that scores individual samples rather than the instance as a whole.
19	
20	\paragraph{Log-probability (model-internal, per-sample).}
21	The only per-sample signal.
22	For sample $y_i$ with tokens $t_1, \ldots, t_{|y_i|}$:
23	\begin{equation}\label{eq:logprob}
24	c_{\text{lp}}(y_i) = \frac{1}{|y_i|} \sum_{j=1}^{|y_i|} \log p_{\mathcal{M}}(t_j \mid t_{<j}, x)
25	\end{equation}
26	
27	\paragraph{Exact match voting (surface, instance-level).}
28	The majo
…[truncated 4022 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 408 · 2026-05-15T07:53:43.374288+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 409 · 2026-05-15T07:53:43.877055+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Datasets.}
8	We evaluate on three English IE benchmarks spanning a difficulty gradient.
9	\textbf{SciERC} \cite{luan2018scierc} contains 551 test instances annotated for joint NER (6 types) and RE (7 types).
10	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} provides 3{,}453 test sentences with 4 entity types, where models achieve ${\approx}$91\% micro F1.
11	\textbf{WNUT-17} \cite{derczynski2017wnut} consists of 1{,}287 social media instances with emerging entities, used to probe method boundaries (52\% zero F1).
12	
13	\paragraph{Models and sampling.}
14	Both \textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are fine-tuned with LoRA (rank$=$32, $\alpha{=}64$) for 5 epochs using LLaMA Factory \cite{zheng2024llamafactory} under identical training procedures, ensuring cross-architecture comparisons (at 8B scale) reflect architectural differences rather than training confounds.
15	We draw $N{=}8$ samples at $T{=}1.0$ (primary), with $N{=}16$ for scaling experiments.\footnote{$N{=}16$ results for CoNLL (Qwen) and SciERC (LLaMA) are in Table~\ref{tab:robustness} (Appendix~\ref{app:robustness}).}
16	Quality estimation uses Spearman $\rho$ and AUROC; downstream utility uses best-of-$N$ selection F1 with exact span matching (NER) and head-tail-label matching (RE).
17	Inference uses vLLM with constrained decoding \cite{willard2023guided}.
18	
19	%% ============================================================
20	\subsection{Quality Estimation Results}
21	\label{sec:qe_results}
22	
23	\begin{table*}[t]
24	\centering
25	\small
26	\caption{Quality estimation across tasks and models (Spearman $\rho$ and AUROC). Best value per block and column in \textbf{bold}. SciERC evaluates joint NER (6 types) and RE (7 types); CoNLL evaluates NER (4 types). $N{=}8$ results use seed${=}42$; $N{=}16$ results are averaged across seeds \{42, 123, 456\}.\textsuperscript{$
…[truncated 12480 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 410 · 2026-05-15T07:53:44.279104+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 411 · 2026-05-15T07:53:44.279652+00:00_

1	\section{Discussion}\label{sec:discussion}
2	
3	\paragraph{Practical recommendations.}
4	For per-instance quality ranking, entity voting provides the strongest rank correlation ($\rho{=}0.38$), though exact match leads binary discrimination (AUROC${=}0.749$); under conditional filtering, EM leads on both NER and RE ($\rho{=}0.360$, $0.417$).
5	Signal rankings depend on task difficulty---EM dominates easy tasks (CoNLL), Voting and SJ dominate hard tasks (SciERC)---directionally consistent across tested model families, though with model-dependent magnitude.
6	When model capability is insufficient (WNUT-17), all signals converge toward non-significant conditional correlations (Table~\ref{tab:wnut}).
7	
8	\paragraph{Why the gap exists: two layers.}
9	\textit{Layer 1 (structural):} Four of five signals are instance-level aggregates that assign a single score per input; they cannot rank candidates by construction.
10	Consensus-proximity selection (\S\ref{sec:evaluation}) does not recover per-sample discrimination (Table~\ref{tab:selection}).
11	\textit{Layer 2 (empirical):} Log-probability, the only per-sample signal, also fails to exploit the 13--18~pp oracle headroom.
12	Under constrained decoding, logprob scores are severely compressed: 60\% of instances have a within-sample range below 0.05, and 75\% of pairwise comparisons are effective ties ($|\Delta|{<}0.026$; Appendix~\ref{app:logprob_ties}).
13	In the non-tied 40\%, logprob selection significantly outperforms greedy ($+2.9$~pp, $p{=}0.01$), confirming the signal carries useful information but is resolution-limited.
14	The common root is that quality estimation ranks \textit{instances}, while sample selection requires ranking \textit{candidates within a single instance}---a finer granularity that neither instance-level aggregation nor token-level confidence provides.
15	Diversity-stratified analysis confirms the gap persists even among high-diversity instances (Appendix~\ref{app:diversity}); RE miscalibration (E
…[truncated 1117 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 412 · 2026-05-15T07:53:44.330074+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 413 · 2026-05-15T07:53:44.782315+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	This work provides, to our knowledge, the first multi-family comparison of confidence signals for test-time scaling in generative information extraction.
4	By comparing five signals from three families across NER and RE tasks of varying difficulty, we disentangle quality estimation from sample selection---two objectives that prior work has conflated.
5	Consistency-based signals are effective quality estimators ($\rho$ up to 0.38, AUROC up to 0.75).
6	Four of five signals are instance-level by construction and cannot rank candidates; log-probability, the only per-sample signal, also fails ($p{>}0.39$, 13--18~pp oracle headroom on SciERC), a disconnect we term the \textit{correlation-selection gap}.
7	Signal rankings depend on task difficulty---exact match leads on easy tasks, structural signals on hard tasks---with this ordering directionally consistent across model families, though magnitudes are model-dependent.
8	While our NER findings are validated across three datasets, our RE conclusions rest on SciERC alone and warrant further validation.
9	
10	Trained verifiers or reward models could close the selection gap by learning per-sample quality discrimination.
11	Cross-task transfer beyond IE, scaling to larger models (70B+), and integration with conformal prediction are promising directions.
12	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 414 · 2026-05-15T07:53:44.782766+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 415 · 2026-05-15T07:53:45.691568+00:00_

1	Our evaluation covers three datasets but only one RE benchmark (SciERC), where 40\% of instances receive zero F1, compressing the discriminable range and limiting signal differentiation for relation extraction.
2	RE selection failure persists even when restricting to non-zero F1 instances (Appendix~\ref{app:re_conditional_selection}), ruling out floor effects as the sole explanation, but generalization to other RE benchmarks remains unvalidated.
3	WNUT-17 confirms the capability boundary of our approach, but our positive results on formal-domain text (CoNLL, SciERC) have not been validated on informal or noisy text where models achieve non-trivial performance.
4	
5	We evaluate two model families (Qwen3-8B and LLaMA-3.1-8B), both at 8B parameters.
6	A 3-seed robustness analysis confirms that signal rankings are stable across seeds ($\sigma{\leq}0.025$; Table~\ref{tab:multiseed}), but whether our findings---particularly the correlation-selection gap and the difficulty-dependent signal ordering---hold for larger models (70B+) or closed-source APIs remains untested.
7	Larger models may produce higher-quality and more diverse samples, potentially altering the signal landscape.
8	
9	Our analysis of selection potential uses only unsupervised signals.
10	We do not train a dedicated verifier or reward model, leaving unknown how much of the oracle headroom a supervised approach could recover.
11	
12	We evaluate at $N{=}8$ and $N{=}16$.
13	The behavior of confidence signals at larger sample sizes (e.g., $N{=}64$ or $N{=}128$) is unknown, and $N$-scaling gains are setting-dependent: SJ improves by $+0.052$ on Qwen SciERC NER but only $+0.016$ on LLaMA SciERC NER when doubling from $N{=}8$ to $N{=}16$.
14	
15	On CoNLL with LLaMA, the SJ--FK gap is only 0.003 ($\rho{=}0.431$ vs.\ $0.428$), so the structural advantage over surface signals may not generalize to all simple-schema datasets.
16	Constrained decoding (Outlines/vLLM) enforces schema compliance, potentially compressing 
…[truncated 314 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 908
}
```

</details>

---


### Tool call

_source line 416 · 2026-05-15T07:53:45.692644+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 417 · 2026-05-15T07:53:46.195091+00:00_

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
21	$c_{\text{vote}}$ & Entity voting confidence \\
22	$c_{\text{lp}}$ & Log-probability (mean token log-likelihood) \\
23	\bottomrule
24	\end{tabular}
25	\caption{Notation used throughout the paper.}
26	\label{tab:notation}
27	\end{table}
28	
29	\section{Robustness Analysis}\label{app:robustness}
30	
31	\begin{table}[t]
32	\centering
33	\small
34	\caption{Signal robustness across configurations (Spearman $\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: cross-architecture transfer (LLaMA CoNLL $N{=}16$, 3-seed mean $\pm\sigma$). $^\dagger$Mean over 3 seeds ($\sigma{=}0.025$; individual: 0.428, 0.424, 0.384).}
35	\label{tab:robustness}
36	\begin{tabular}{llcc}
37	\toprule
38	& & NER $\rho$ & RE $\rho$ \\
39	\midrule
40	\multicolumn{4}{l}{\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\
41	\quad SJ & $T{=}0.7$ & 0.388 & 0.234 \\
42	\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\
43	\quad FK & $T{=}0.7$ & 0.321 & 0.184 \\
44	\quad FK & $T{=}1.0$ & 0.267 & 0.275 \\
45	\midrule
46	\multicolumn{4}{l}{\textit{Sample size} (Qwen SciERC, $T{=}1.0$)} \\
47	\quad SJ & $N{=}8$  & 0.360 & 0.250 \\
48	\quad SJ & $N{=}16$ & 0.412$^\dagger$ & 0.281 \\
49	\quad FK & $N{=}8$  & 0.267 & 0.275 \\
50	\quad FK & $N{=}16$ & 0.280 & 0.279 \\
51	\midrule
52	\multicolumn{4}{l}{\textit{Cross-architecture} (LLaMA CoNLL, $N{=}16$, 3 seeds)} \\
53	\quad SJ &  & $0.463{\pm}0.007$ & --- \\
54	\quad FK &  & $0.455{\pm}0.006$ & --- \\
55	\quad EM &
…[truncated 27104 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 418 · 2026-05-15T07:53:47.249272+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all scoring dimensions, their scales (1-5 etc.), and the exact rubric descriptions for each score level. Include soundness, excitement, overall assessment, confidence, and any other dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with all scoring dimensions, their scales (1-5 etc.), and the exact rubric descriptions for each score level. Include soundness, excitement, overall assessment, confidence, and any other dimensions."
  }
}
```

</details>

---


### Tool result

_source line 419 · 2026-05-15T07:53:52.420346+00:00_

# ACL Rolling Review Form - Complete Scoring Dimensions

## 1. Reviewer Confidence (1-5 Scale)
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: "Quite sure. I tried to check the important points carefully."
- **3**: "Pretty sure, but there's a chance I missed something."
- **2**: "Willing to defend my evaluation, but it is fairly likely that I missed some details."
- **1**: "Not my area, or paper is very hard to understand."

## 2. Soundness (1-5 Scale with Half-Points)
- **5**: "Excellent: This study is one of the most thorough I have seen."
- **4**: "Strong: This study provides sufficient support for all of its claims."
- **3**: "Acceptable: This study provides sufficient support for its main claims."
- **2**: "Poor: Some of the main claims are not sufficiently supported."
- **1**: "Major Issues: This study is not yet sufficiently thorough to warrant publication."

## 3. Excitement (1-5 Scale with Half-Points)
Ranges from "Highly Exciting" (5) through "Interesting" (3) to "Not Exciting" (1), emphasizing subjective assessment of innovation, impact, and relevance.

## 4. Overall Assessment (1-5 Scale with Half-Points)
- **5**: "Consider for Award"
- **4**: "Conference acceptance"
- **3**: "Findings publication"
- **2**: "Resubmit next cycle"
- **1**: "Do not resubmit"

## Additional Dimensions
- Reproducibility (1-5)
- Dataset Value (1-5)
- Software Value (1-5)
- Author Identity Knowledge (1-5)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 5171
}
```

</details>

---


### Tool call

_source line 420 · 2026-05-15T07:54:45.711967+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "self-consistency structured prediction information extraction LLM confidence 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "self-consistency structured prediction information extraction LLM confidence 2025 2026"
  }
}
```

</details>

---


### Tool call

_source line 421 · 2026-05-15T07:54:45.963393+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "MBR decoding beyond machine translation NER relation extraction structured output 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "MBR decoding beyond machine translation NER relation extraction structured output 2024 2025"
  }
}
```

</details>

---


### Tool call

_source line 422 · 2026-05-15T07:54:46.516001+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"best-of-N\" selection structured prediction information extraction LLM 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"best-of-N\" selection structured prediction information extraction LLM 2025"
  }
}
```

</details>

---


### Tool result

_source line 423 · 2026-05-15T07:54:52.401114+00:00_

Web search results for query: "self-consistency structured prediction information extraction LLM confidence 2025 2026"

Links: [{"title":"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning","url":"https://arxiv.org/html/2601.02970v1"},{"title":"Confidence Improves Self-Consistency in LLMs","url":"https://arxiv.org/html/2502.06233v1"},{"title":"Confidence Improves Self-Consistency in LLMs","url":"https://aclanthology.org/2025.findings-acl.1030.pdf"},{"title":"Self-Consistency Sampling in LLMs","url":"https://www.emergentmind.com/topics/self-consistency-sampling"},{"title":"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12888769/"},{"title":"Towards Reliable LLM Grading Through Self-Consistency and Selective Human Review: Higher Accuracy, Less Work","url":"https://www.mdpi.com/2504-4990/8/3/74"},{"title":"Frontiers | An overview of model uncertainty and variability in LLM-based sentiment analysis: challenges, mitigation strategies, and the role of explainability","url":"https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2025.1609097/full"},{"title":"Confidence Improves Self-Consistency in LLMs - ACL Anthology","url":"https://aclanthology.org/2025.findings-acl.1030/"},{"title":"Stability Evaluation of Confidence Features Across Model and Data Variants in Large Language Models — Research and Science Today","url":"https://www.rstjournal.com/article/4.2026"},{"title":"[2502.06233] Confidence Improves Self-Consistency in LLMs","url":"https://arxiv.org/abs/2502.06233"}]

I've completed the web search for your query on self-consistency, structured prediction, information extraction, and LLM confidence. Here are the key findings:

## Recent Research Highlights (2025-2026)

**Self-Consistency with Confidence Integration**

Reliability-Aware Adaptive Self-Consistency (ReASC) 
…[truncated 1599 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6689
}
```

</details>

---


### Tool result

_source line 424 · 2026-05-15T07:54:53.117646+00:00_

Web search results for query: "MBR decoding beyond machine translation NER relation extraction structured output 2024 2025"

Links: [{"title":"[1911.09886] Effective Modeling of Encoder-Decoder Architecture for Joint Entity and Relation Extraction","url":"https://ar5iv.labs.arxiv.org/html/1911.09886"},{"title":"Effective Modeling of Encoder-Decoder Architecture for ...","url":"https://arxiv.org/pdf/1911.09886"},{"title":"Structured information extraction from scientific text with large language models | Nature Communications","url":"https://www.nature.com/articles/s41467-024-45563-x"},{"title":"Information Extraction: NER, Relations, and Structured Output - Interactive | Michael Brenndoerfer | Michael Brenndoerfer","url":"https://mbrenndoerfer.com/writing/information-extraction"},{"title":"(PDF) Lattice Minimum Bayes-Risk Decoding for Statistical Machine Translation","url":"https://www.academia.edu/6354227/Lattice_Minimum_Bayes_Risk_Decoding_for_Statistical_Machine_Translation"},{"title":"Lattice Minimum Bayes-Risk Decoding for Statistical Machine Translation. | Request PDF","url":"https://www.researchgate.net/publication/221012583_Lattice_Minimum_Bayes-Risk_Decoding_for_Statistical_Machine_Translation"},{"title":"Foundation Models for Information Extraction | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-031-23190-2_5"},{"title":"A survey on cutting-edge relation extraction techniques based on language models","url":"https://arxiv.org/html/2411.18157v1"},{"title":"Structured Language Generation Model: Loss Calibration and Formatted Decoding for Robust Structure Prediction and Knowledge Retrieval","url":"https://arxiv.org/html/2402.08971"},{"title":"Unveiling the Power of Source: Source-based Minimum Bayes Risk Decoding for Neural Machine Translation","url":"https://arxiv.org/html/2406.11632"}]

Based on the search results, I found relevant information about applications of MBR (Minimum Bayes-Risk) decoding and structured output tasks 
…[truncated 1747 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7154
}
```

</details>

---


### Tool result

_source line 425 · 2026-05-15T07:54:53.772368+00:00_

Web search results for query: ""best-of-N" selection structured prediction information extraction LLM 2025"

Links: [{"title":"Leveraging large language models for structured information extraction from pathology reports - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S2153353925001075"},{"title":"Benchmarking LLM-based Information Extraction Tools for Medical Documents | medRxiv","url":"https://www.medrxiv.org/content/10.64898/2026.01.19.26344287v1.full"},{"title":"Large language models for generative information extraction: a survey | Frontiers of Computer Science | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11704-024-40555-y"},{"title":"Large language model driven transferable key information ...","url":"https://www.nature.com/articles/s41598-025-15627-z.pdf"},{"title":"SLOT: Structuring the Output of Large Language Models","url":"https://aclanthology.org/2025.emnlp-industry.32.pdf"},{"title":"Data+AI: LLM4Data and Data4LLM Guoliang Li Tsinghua University Beijing, China","url":"https://dbgroup.cs.tsinghua.edu.cn/ligl/papers/SIGMOD2025-Data+AI.pdf"},{"title":"End-to-End Structured Extraction with LLM – Part 1... - Databricks Community - 98396","url":"https://community.databricks.com/t5/technical-blog/end-to-end-structured-extraction-with-llm-part-1-batch-entity/ba-p/98396"},{"title":"Benchmarking LLM-based Information Extraction Tools for ...","url":"https://www.medrxiv.org/content/10.64898/2026.01.19.26344287v1.full.pdf"},{"title":"StructEval: Benchmarking LLMs’ Capabilities to Generate Structural Outputs","url":"https://arxiv.org/html/2505.20139v1"},{"title":"arXiv:2505.18458v3 [cs.DB] 1 Jun 2025 1 A Survey of LLM × DATA","url":"https://arxiv.org/pdf/2505.18458"}]

I've completed the web search for your query on "best-of-N" selection structured prediction information extraction LLM 2025. Here's what the search results revealed:

## Key Findings:

The search results contain recent research on **structured inf
…[truncated 1489 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7256
}
```

</details>

---


### Tool call

_source line 426 · 2026-05-15T07:55:00.923841+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Huang et al 2025 \"uncertainty quantification\" \"information extraction\" generative LLM NER"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Huang et al 2025 \"uncertainty quantification\" \"information extraction\" generative LLM NER"
  }
}
```

</details>

---


### Tool call

_source line 427 · 2026-05-15T07:55:00.974462+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"test-time compute\" \"structured output\" selection verifier reward model NER 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"test-time compute\" \"structured output\" selection verifier reward model NER 2025 2026"
  }
}
```

</details>

---


### Tool result

_source line 428 · 2026-05-15T07:55:07.402596+00:00_

Web search results for query: "Huang et al 2025 "uncertainty quantification" "information extraction" generative LLM NER"

Links: [{"title":"Uncertainty quantification by large language models - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S2666827025001562"},{"title":"IUQ: Interrogative Uncertainty Quantification for Long-Form Large Language Model Generation","url":"https://arxiv.org/html/2604.15109"},{"title":"Large language models for generative information extraction: a survey | Frontiers of Computer Science | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11704-024-40555-y"},{"title":"Uncertainty Quantification for Hallucination Detection in Large Language Models: Foundations, Methodology, and Future Directions","url":"https://arxiv.org/html/2510.12040"},{"title":"A Survey of Uncertainty Estimation Methods on Large ...","url":"https://aclanthology.org/2025.findings-acl.1101.pdf"},{"title":"Uncertainty Quantification and Confidence Calibration in Large Language Models: A Survey","url":"https://arxiv.org/html/2503.15850v1"},{"title":"Uncertainty Quantification of Large Language Models through Multi-Dimensional Responses","url":"https://arxiv.org/html/2502.16820v2"},{"title":"Simple Yet Effective: An Information-Theoretic Approach to Multi-LLM Uncertainty Quantification - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12702469/"},{"title":"Uncertainty Quantification for LLM-Based Survey Simulations Chengpiao Huang∗","url":"https://arxiv.org/pdf/2502.17773v1"},{"title":"Uncertainty Quantification and Decomposition for LLM-based Recommendation | Proceedings of the ACM on Web Conference 2025","url":"https://dl.acm.org/doi/10.1145/3696410.3714601"}]

I found several results related to your search query. Here's what I discovered:

## Key Findings

The search results reference multiple works by Huang et al. from 2025 related to uncertainty quantification in large language models, though I found limited specific i
…[truncated 1333 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6478
}
```

</details>

---


### Tool result

_source line 429 · 2026-05-15T07:55:09.514036+00:00_

Web search results for query: ""test-time compute" "structured output" selection verifier reward model NER 2025 2026"

Links: [{"title":"GitHub - ThreeSR/Awesome-Inference-Time-Scaling: Paper List of Inference/Test Time Scaling/Computing · GitHub","url":"https://github.com/ThreeSR/Awesome-Inference-Time-Scaling"},{"title":"Scaling LLM Test-Time Compute Optimally Can be More Effective than Scaling Parameters for Reasoning | OpenReview","url":"https://openreview.net/forum?id=4FWAwZtd2n"},{"title":"Rewarding Progress: Scaling Automated Process Verifiers for LLM Reasoning | OpenReview","url":"https://openreview.net/forum?id=A6Y7AqlzLW"},{"title":"Trust but Verify! A Survey on Verification Design for Test-time Scaling","url":"https://arxiv.org/html/2508.16665v3"},{"title":"Inference-Time Scaling of Verification: Self-Evolving Deep Research Agents via Test-Time Rubric-Guided Verification","url":"https://arxiv.org/html/2601.15808"},{"title":"2026-01-10 Parallel Test-Time Scaling for Latent Reasoning Models Runyang You1","url":"https://arxiv.org/pdf/2510.07745"},{"title":"Reward Model Generalization for Compute-Aware Test-Time Reasoning | OpenReview","url":"https://openreview.net/forum?id=xaTmmj47Iu"},{"title":"Optimizing Test-Time Compute for LLMs: A Meta-Reinforcement Learning Approach with Cumulative Regret Minimization - MarkTechPost","url":"https://www.marktechpost.com/2025/03/14/optimizing-test-time-compute-for-llms-a-meta-reinforcement-learning-approach-with-cumulative-regret-minimization/"},{"title":"AI Trends 2026: Test-Time Reasoning and the Rise of Reflective Agents","url":"https://huggingface.co/blog/aufklarer/ai-trends-2026-test-time-reasoning-reflective-agen"},{"title":"A Survey on Test-Time Scaling. This blog is based a comprehensive… | by Yanan Chen | Medium","url":"https://medium.com/@yananchen1116/a-survey-on-test-time-scaling-04b1c1dadb9d"}]

I've found relevant research on test-time compute, structured output, verifier reward models, and related topics. 
…[truncated 1848 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8539
}
```

</details>

---


### Tool call

_source line 430 · 2026-05-15T07:57:36.816143+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 — Round 1 完整审稿报告\n\n### 审稿侧重：新颖性 + framing + related work 完整性 + 写作质量\n\n---\n\n## 总体评分\n**Overall**: 3.0 / 5（Findings publication）\n**一句话总结**: 实验设计严谨、统计分析到位的 empirical study，但核心概念贡献\"correlation-selection gap\"的新颖性因 4/5 信号在定义上就无法做 sample selection 而被大幅削弱——这是一个 tautological observation 被包装成 empirical finding 的 framing 问题。\n\n## 官方维度打分（来自 ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 实验严谨（bootstrap CI、TOST、multi-seed），但核心 claim 中的 tautological 成分削弱了论证的 substantiveness |\n| Excitement | 2.5/5 | 负面结果对实践有价值，但新颖性有限——核心发现部分来自定义而非实验 |\n| Reproducibility | 4/5 | 训练细节、prompt template、超参数、统计测试均有详细描述 |\n| Confidence | 4/5 | 熟悉 self-consistency、uncertainty estimation、generative IE 文献 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Correlation-selection gap 的核心论证存在 tautological 成分，新颖性不足\n\n- 具体位置：Section 1 (L22–24), Section 5.3, Section 6 (Discussion \"Why the gap exists: two layers\")\n- 问题：论文将\"correlation-selection gap\"作为三个 contribution 之一（C2），但 4/5 信号（EM、FK、SJ、Voting）是 instance-level by definition——它们对同一 input 的所有 N 个 sample 产生同一个分数。论文自己承认：\"they cannot rank candidates by construction\"（Section 5.3, L121; Discussion Layer 1）。这意味着这 4 个信号的\"selection failure\"不是实验发现，而是定义的逻辑后果。将一个 definitional impossibility 包装为\"gap\"并命名为 contribution，exaggerates the novelty。\n\n  真正 non-trivial 的发现只有 logprob 的失败——但 Appendix F 已解释：constrained decoding 造成 score compression（60% instances 的 within-instance range < 0.05），且在 non-tied subset 中 logprob 显著优于 greedy（+2.9 pp, p=0.01）。这说明 logprob 的\"failure\"是 constrained decoding 的 artifact，而非 confidence signal 的 intrinsic limitation。\n\n  因此，\"correlation-selection gap\"被两头夹击：instance-level signals 的 failure 是 tautological；logprob 的 failure 是 constrained-decoding artifact。\n\n- 为什么影响接收：核心 contribution 的新颖性是 Findings 接收的底线要求。\n- 建议修改方向：(1) 明确区分\"by-construction impossibility\"和\"empirical finding\"，不要将前者算作 contribution；(2) 将 C2 重心转向 logprob score compression 分析；(3) 考虑标题和 abstract 的 reframing。\n\n**N2** [critical] 与 Nédellec et al. (2026) 的增量贡献论证不充分\n\n- 具体位置：Section 1 (L16), Section 2 (L13–15), Table 5 (Appendix B)\n- 问题：三个增量均偏弱：(i) SJ vs EM 的 Δρ=+0.065 在 Bonferroni 校正后不显著（Table 5 自述），且 conditional set 上 EM 反而第一；(ii) selection analysis 如 N1 所述主要是 tautological；(iii) difficulty gradient 发现（harder→structural better, easier→EM better）在直觉上不意外。\n- 建议修改方向：更诚实地量化增量大小，或找到 structural matching 有 clearly significant 优势的 setting。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Abstract 信息密度过高\n- 9 行包含 5 个 signal、3 个 family、4 个数值指标、3 个数据集、2 个模型、gap 概念、technical arguments。首次阅读难以把握核心 message。\n- 建议聚焦 1–2 个核心发现，将细节数字移入 Introduction。\n\n**W2** [warning] RE \"preliminary\" 标注与实际使用不一致\n- Abstract 标注 \"preliminary\"，但 RE 结果在 Table 1（2 列）、Table 2、Figure 2–3、Discussion 中被大量使用作为主要论证。\n- 建议：要么移 RE 至 Appendix，要么去掉\"preliminary\"标签。\n\n**W3** [warning] Soft Jaccard 方法论新颖性有限\n- 本质是 Hungarian matching + token-level IoU，均为标准技术。缺少与 soft set similarity 已有工作（如 object detection 中的 soft IoU）的对比讨论。\n\n**W4** [warning] \"first multi-family comparison\" claim 过度依赖 scope 限定\n- \"first\" 依赖\"for test-time scaling\" + \"in generative IE\"的双重限定。建议去掉\"first\"或将 gap 描述清楚而非宣称优先权。\n\n---\n\n## 小问题（不影响接收）\n\n- 术语不一致：Table 1 用 \"Voting Conf.\"，Table 4 用 \"VC\"，建议统一。\n- Ethics Statement 仅两句话，可补充 LLM extraction error 的潜在影响。\n- 引用验证：`hobelsberger2025systematic` 和 `lightman2024verify` 在 OpenAlex 未找到（可能索引延迟）；`feng2025optimal` 和 `ye2025uncertainty` 的 first author 与 API 记录不匹配，建议核查 bib。\n- Figure 1 caption 引用了 Table 2，降低 self-containment。\n- Table 1 的 `\\footnotetext` 紧跟 `\\caption`，某些模板编译下可能显示异常。\n\n---\n\n## Missing References\n\n1. \"Trust but Verify! A Survey on Verification Design for Test-time Scaling\" (2025, arXiv:2508.16665) — 与 Discussion 中 verifier 建议直接相关\n2. 2025–2026 最新 uncertainty quantification survey（如 arXiv:2503.15850）\n3. SLOT (EMNLP 2025 Industry) — structured output generation + constrained decoding 相关\n4. MBR 在非 MT 任务中的应用（summarization、dialogue）——帮助 contextualize MBR 的 task-dependent 表现\n\n---\n\n## 主要优势\n\n- 统计分析的严谨性：bootstrap CI、TOST、multi-seed、conditional filtering、diversity stratification 远超同类 empirical papers\n- Negative result 的充分刻画：logprob compression analysis 和 diversity-stratified gap 排除了多个 alternative explanations\n- 实验设计公平：两模型相同训练配置，三数据集覆盖难度梯度\n- Limitations section 诚实全面\n- 整体写作质量良好（除 abstract 过密和术语不一致外）",
  "reviewer_id": "2",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 — Round 1 完整审稿报告\n\n### 审稿侧重：新颖性 + framing + related work 完整性 + 写作质量\n\n---\n\n## 总体评分\n**Overall**: 3.0 / 5（Findings publication）\n**一句话总结**: 实验设计严谨、统计分析到位的 empirical study，但核心概念贡献\"correlation-selection gap\"的新颖性因 4/5 信号在定义上就无法做 sample selection 而被大幅削弱——这是一个 tautological observation 被包装成 empirical finding 的 framing 问题。\n\n## 官方维度打分（来自 ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 实验严谨（bootstrap CI、TOST、multi-seed），但核心 claim 中的 tautological 成分削弱了论证的 substantiveness |\n| Excitement | 2.5/5 | 负面结果对实践有价值，但新颖性有限——核心发现部分来自定义而非实验 |\n| Reproducibility | 4/5 | 训练细节、prompt template、超参数、统计测试均有详细描述 |\n| Confidence | 4/5 | 熟悉 self-consistency、uncertainty estimation、generative IE 文献 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Correlation-selection gap 的核心论证存在 tautological 成分，新颖性不足\n\n- 具体位置：Section 1 (L22–24), Section 5.3, Section 6 (Discussion \"Why the gap exists: two layers\")\n- 问题：论文将\"correlation-selection gap\"作为三个 contribution 之一（C2），但 4/5 信号（EM、FK、SJ、Voting）是 instance-level by definition——它们对同一 input 的所有 N 个 sample 产生同一个分数。论文自己承认：\"they cannot rank candidates by construction\"（Section 5.3, L121; Discussion Layer 1）。这意味着这 4 个信号的\"selection failure\"不是实验发现，而是定义的逻辑后果。将一个 definitional impossibility 包装为\"gap\"并命名为 contribution，exaggerates the novelty。\n\n  真正 non-trivial 的发现只有 logprob 的失败——但 Appendix F 已解释：constrained decoding 造成 score compression（60% instances 的 within-instance range < 0.05），且在 non-tied subset 中 logprob 显著优于 greedy（+2.9 pp, p=0.01）。这说明 logprob 的\"failure\"是 constrained decoding 的 artifact，而非 confidence signal 的 intrinsic limitation。\n\n  因此，\"correlation-selection gap\"被两头夹击：instance-level signals 的 failure 是 tautological；logprob 的 failure 是 constrained-decoding artifact。\n\n- 为什么影响接收：核心 contribution 的新颖性是 Findings 接收的底线要求。\n- 建议修改方向：(1) 明确区分\"by-construction impossibility\"和\"empirical finding\"，不要将前者算作 contribution；(2) 将 C2 重心转向 logprob score compression 分析；(3) 考虑标题和 abstract 的 reframing。\n\n**N2** [critical] 与 Nédellec et al. (2026) 的增量贡献论证不充分\n\n- 具体位置：Section 1 (L16), Section 2 (L13–15), Table 5 (Appendix B)\n- 问题：三个增量均偏弱：(i) SJ vs EM 的 Δρ=+0.065 在 Bonferroni 校正后不显著（Table 5 自述），且 conditional set 上 EM 反而第一；(ii) selection analysis 如 N1 所述主要是 tautological；(iii) difficulty gradient 发现（harder→structural better, easier→EM better）在直觉上不意外。\n- 建议修改方向：更诚实地量化增量大小，或找到 structural matching 有 clearly significant 优势的 setting。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] Abstract 信息密度过高\n- 9 行包含 5 个 signal、3 个 family、4 个数值指标、3 个数据集、2 个模型、gap 概念、technical arguments。首次阅读难以把握核心 message。\n- 建议聚焦 1–2 个核心发现，将细节数字移入 Introduction。\n\n**W2** [warning] RE \"preliminary\" 标注与实际使用不一致\n- Abstract 标注 \"preliminary\"，但 RE 结果在 Table 1（2 列）、Table 2、Figure 2–3、Discussion 中被大量使用作为主要论证。\n- 建议：要么移 RE 至 Appendix，要么去掉\"preliminary\"标签。\n\n**W3** [warning] Soft Jaccard 方法论新颖性有限\n- 本质是 Hungarian matching + token-level IoU，均为标准技术。缺少与 soft set similarity 已有工作（如 object detection 中的 soft IoU）的对比讨论。\n\n**W4** [warning] \"first multi-family comparison\" claim 过度依赖 scope 限定\n- \"first\" 依赖\"for test-time scaling\" + \"in generative IE\"的双重限定。建议去掉\"first\"或将 gap 描述清楚而非宣称优先权。\n\n---\n\n## 小问题（不影响接收）\n\n- 术语不一致：Table 1 用 \"Voting Conf.\"，Table 4 用 \"VC\"，建议统一。\n- Ethics Statement 仅两句话，可补充 LLM extraction error 的潜在影响。\n- 引用验证：`hobelsberger2025systematic` 和 `lightman2024verify` 在 OpenAlex 未找到（可能索引延迟）；`feng2025optimal` 和 `ye2025uncertainty` 的 first author 与 API 记录不匹配，建议核查 bib。\n- Figure 1 caption 引用了 Table 2，降低 self-containment。\n- Table 1 的 `\\footnotetext` 紧跟 `\\caption`，某些模板编译下可能显示异常。\n\n---\n\n## Missing References\n\n1. \"Trust but Verify! A Survey on Verification Design for Test-time Scaling\" (2025, arXiv:2508.16665) — 与 Discussion 中 verifier 建议直接相关\n2. 2025–2026 最新 uncertainty quantification survey（如 arXiv:2503.15850）\n3. SLOT (EMNLP 2025 Industry) — structured output generation + constrained decoding 相关\n4. MBR 在非 MT 任务中的应用（summarization、dialogue）——帮助 contextualize MBR 的 task-dependent 表现\n\n---\n\n## 主要优势\n\n- 统计分析的严谨性：bootstrap CI、TOST、multi-seed、conditional filtering、diversity stratification 远超同类 empirical papers\n- Negative result 的充分刻画：logprob compression analysis 和 diversity-stratified gap 排除了多个 alternative explanations\n- 实验设计公平：两模型相同训练配置，三数据集覆盖难度梯度\n- Limitations section 诚实全面\n- 整体写作质量良好（除 abstract 过密和术语不一致外）",
    "reviewer_id": "2",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 431 · 2026-05-15T07:57:40.831669+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4015
}
```

</details>

---


### Assistant

_source line 432 · 2026-05-15T07:57:46.859924+00:00_

审稿报告已发送给 Director。

总结：论文在实验设计和统计分析上质量很高，但核心概念贡献（correlation-selection gap）的新颖性存在结构性问题——4/5 信号的 selection failure 是定义的逻辑后果而非实验发现，logprob 的 failure 是 constrained decoding 的 artifact。整体评分 Overall 3.0/5（Findings 水平），需要在 framing 上做 substantial rewrite 才能更准确地反映实际贡献。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2"
}
```

</details>

---


## Round 13

## Round 13

4 recorded events


### User

_source line 433 · 2026-05-15T07:58:18.636451+00:00_

[Round 1 审稿请求]:
## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见

以下是 Reviewer 1 的完整审稿意见。请逐条回应：
- **[AGREE]** 同意并说明理由
- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）

---

### Reviewer 1 的 Must-Fix 问题

**R1-N1** [critical] Constrained decoding 作为核心混淆变量未被隔离
- 所有实验均使用 constrained decoding (vLLM + XGrammar)。论文承认 "may compress per-sample diversity"（Limitations §16），Appendix F 显示 60% instance logprob range < 0.05。论文无法区分 correlation-selection gap 是 structured IE 固有属性还是 constrained decoding 的人工产物。
- 建议：添加 free-form decoding 消融，或在 title/abstract/conclusion 限定 scope。

**R1-N2** [critical] Appendix F 的 non-tied subset 结果（logprob +2.9pp, p=0.01）实际削弱核心 claim
- 在 non-tied 40% 中 logprob selection 显著优于 greedy，within-instance ρ 从 0.08 升到 0.39。更直接的解读是 logprob 在有 score resolution 时确实有效，gap 根因是 constrained decoding 的 score compression。
- 建议：提升 non-tied analysis 至主文，重新组织 Discussion。

### Reviewer 1 的 Should-Fix 问题

**R1-W1** RE 结论仅基于 SciERC，abstract/contribution/conclusion 限定不一致
**R1-W2** FK independence 假设 justification 不够严格，excess agreement 数据不全
**R1-W3** "Cross-architecture" 用词过度（均为 8B decoder-only transformer）
**R1-W4** TOST δ 选择缺乏外部锚点
**R1-W5** Qwen3-8B thinking token 训练不一致（SciERC vs CoNLL/WNUT）

### Reviewer 1 的 Minor 问题

**R1-M1** Table 1 脚注格式可能渲染异常
**R1-M2** SJ 全称首次出现时应统一
**R1-M3** §4.2 脚注 semantic entropy 比较——如果 "not meaningful" 为何引用？
**R1-M4** `he2024uncertainty` bib entry 与引用上下文不匹配
**R1-M5** 部分引用在 OpenAlex 未找到

### Reviewer 1 的 Questions

1. Free-form decoding 下 logprob 是否可能成为有效 selector？
2. Consensus-proximity = LOO-SJ 的证明？
3. FK excess agreement 在哪个配置测量？
4. WNUT-17 logprob 负相关的解释？

### Reviewer 1 评分
Overall 3/5, Soundness 3, Excitement 3.5, Reproducibility 4, Confidence 4

---

请对以上每个 N/W/M 和 Question 逐条给出 [AGREE] 或 [REBUT]。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 434 · 2026-05-15T08:00:21.507856+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 — 交叉回应 Reviewer 1\n\n### Must-Fix\n\n[AGREE] R1-N1: Constrained decoding 混淆变量 — 与我的 N1 高度一致。补充：free-form decoding 消融本身也非 clean experiment（格式错误），但论文至少应在 title/abstract 限定 scope（\"under constrained decoding\"），当前 framing 将 gap 呈现为 structured IE 固有属性，证据不支持。\n\n[AGREE] R1-N2: Non-tied subset 削弱核心 claim — 完全同意，这是我 N1 的核心论据之一。logprob 在有 score resolution 时有效（+2.9pp, p=0.01, ρ=0.39），说明 gap 根因是 score compression 而非 signal intrinsic limitation。论文应将此提升为主文核心发现。\n\n### Should-Fix\n\n[AGREE] R1-W1: RE scope 不一致 — 与我的 W2 一致\n[AGREE with nuance] R1-W2: FK independence — 关切有效但 severity 偏低（FK 非核心 contribution，负 excess agreement 回应了核心担忧）\n[AGREE] R1-W3: \"Cross-architecture\" 过度 — 应改为 \"cross-model-family\"\n[AGREE with nuance] R1-W4: TOST δ — 多水平 δ 已构成 sensitivity analysis，建议引用 IAA 数据即可\n[AGREE] R1-W5: Thinking token 训练不一致 — SciERC 是核心 benchmark，训练配置差异需严肃对待\n\n### Minor\n\n[AGREE] R1-M1, M2, M4, M5\n[REBUT] R1-M3: Semantic entropy 脚注意图合理（提供 AUROC scale 参考），但执行上可能误导快速读者，建议缩短或删除\n\n### Questions\n\nQ1: 基于 non-tied evidence，free-form 下 logprob 很可能有效，同意这是关键消融\nQ2: Consensus-proximity = LOO-SJ 需数学证明或更正为\"approximately equivalent\"\nQ3: FK excess agreement 应注明 configuration\nQ4: WNUT-17 logprob 负相关需机制解释（可能是 novel entities + overconfident familiar patterns）\n\n### 两份审稿的互补性\n\nR1 和 R2 在核心问题上高度一致（constrained decoding 混淆变量、RE scope、术语）。R1 技术层面更深（FK、thinking token、TOST δ），R2 在 framing/novelty 层面着力更多（tautological argument、incremental over Nédellec、abstract density）。两份审稿互补。",
  "reviewer_id": "2",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 — 交叉回应 Reviewer 1\n\n### Must-Fix\n\n[AGREE] R1-N1: Constrained decoding 混淆变量 — 与我的 N1 高度一致。补充：free-form decoding 消融本身也非 clean experiment（格式错误），但论文至少应在 title/abstract 限定 scope（\"under constrained decoding\"），当前 framing 将 gap 呈现为 structured IE 固有属性，证据不支持。\n\n[AGREE] R1-N2: Non-tied subset 削弱核心 claim — 完全同意，这是我 N1 的核心论据之一。logprob 在有 score resolution 时有效（+2.9pp, p=0.01, ρ=0.39），说明 gap 根因是 score compression 而非 signal intrinsic limitation。论文应将此提升为主文核心发现。\n\n### Should-Fix\n\n[AGREE] R1-W1: RE scope 不一致 — 与我的 W2 一致\n[AGREE with nuance] R1-W2: FK independence — 关切有效但 severity 偏低（FK 非核心 contribution，负 excess agreement 回应了核心担忧）\n[AGREE] R1-W3: \"Cross-architecture\" 过度 — 应改为 \"cross-model-family\"\n[AGREE with nuance] R1-W4: TOST δ — 多水平 δ 已构成 sensitivity analysis，建议引用 IAA 数据即可\n[AGREE] R1-W5: Thinking token 训练不一致 — SciERC 是核心 benchmark，训练配置差异需严肃对待\n\n### Minor\n\n[AGREE] R1-M1, M2, M4, M5\n[REBUT] R1-M3: Semantic entropy 脚注意图合理（提供 AUROC scale 参考），但执行上可能误导快速读者，建议缩短或删除\n\n### Questions\n\nQ1: 基于 non-tied evidence，free-form 下 logprob 很可能有效，同意这是关键消融\nQ2: Consensus-proximity = LOO-SJ 需数学证明或更正为\"approximately equivalent\"\nQ3: FK excess agreement 应注明 configuration\nQ4: WNUT-17 logprob 负相关需机制解释（可能是 novel entities + overconfident familiar patterns）\n\n### 两份审稿的互补性\n\nR1 和 R2 在核心问题上高度一致（constrained decoding 混淆变量、RE scope、术语）。R1 技术层面更深（FK、thinking token、TOST δ），R2 在 framing/novelty 层面着力更多（tautological argument、incremental over Nédellec、abstract density）。两份审稿互补。",
    "reviewer_id": "2",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 435 · 2026-05-15T08:00:25.823938+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4316
}
```

</details>

---


### Assistant

_source line 436 · 2026-05-15T08:00:30.043514+00:00_

交叉回应已提交给 Director。对 R1 的 11 个具体意见中，9 个 [AGREE]（其中 3 个 with nuance），1 个 [REBUT]（M3 semantic entropy 脚注），1 个 [AGREE]（M4 bib mismatch）。两份审稿在核心问题（constrained decoding 混淆变量、gap 的 tautological 成分）上高度一致。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2"
}
```

</details>

---


## Round 14

## Round 14

56 recorded events


### User

_source line 437 · 2026-05-15T08:46:04.261063+00:00_

[Round 1 审稿请求]:
## Round 1 审稿任务 — Reviewer 2

**你的审查侧重：新颖性 + 完整性 + 相关工作**

### 论文信息
- **论文路径**: `projects/struct_self_consist_ie/docs/paper/main.tex`（各章节在 `sections/` 子目录）
- **目标 venue**: EMNLP 2026 Findings
- **截止日期**: 2026-05-25
- **页数限制**: 长文 8 页正文（不含 limitations/ethics/references/appendix）
- **模板**: ACL style files（`\usepackage[review]{acl}`）
- **匿名规则**: Double-blind

### 论文概要
标题：Strong Predictors, Weak Selectors: Confidence Signals for Test-Time Scaling in Information Extraction under Constrained Decoding

研究在 constrained decoding 下，5 种 confidence signals（VC, SJ, FK, EM, logprob）对 structured IE（NER + RE）的 quality estimation 和 sample selection 效果。核心发现：信号是有效的 quality estimator（ρ=0.38, AUROC=0.75）但无法做 sample selection（correlation-selection gap）。

### 你需要重点审查
1. **Contribution 新颖性**：与 Nédellec et al. (2026) 的增量有多大？三个声称的贡献（multi-family comparison / gap identification / difficulty gradient）是否各自有足够新意？
2. **Related work 覆盖度**：是否遗漏重要工作（test-time scaling verification surveys, MBR 在非 MT 任务的应用, 最新 self-consistency 变体等）？引用是否准确（检查引用上下文是否与被引论文实际内容匹配）
3. **Framing 诚实度**："first" claim 是否站得住？cross-model 措辞是否过度外推？gap 概念是否被呈现为比实际更新颖？
4. **写作质量**：Abstract 密度是否过高？术语一致性（confidence signal vs consistency signal, VC vs Voting Conf.）？论文结构是否清晰？
5. **完整性**：是否有关键分析缺失？Future work 是否充分讨论？Limitations 是否诚实？
6. **引用格式与准确性**：bib entry 是否正确、是否有 orphan 引用、是否有引用上下文与实际论文不匹配的情况

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 438 · 2026-05-15T08:46:10.596294+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__verify_references,mcp__agent-ml-research__review_reviewer_post_to_director,WebSearch,WebFetch",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__verify_references,mcp__agent-ml-research__review_reviewer_post_to_director,WebSearch,WebFetch",
    "max_results": "5"
  }
}
```

</details>

---


### Tool result

_source line 439 · 2026-05-15T08:46:10.647232+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 440 · 2026-05-15T08:46:15.971282+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR review form criteria 2026 reviewer guidelines"
  }
}
```

</details>

---


### Tool call

_source line 441 · 2026-05-15T08:46:16.423410+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 reviewer guidelines review form"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 reviewer guidelines review form"
  }
}
```

</details>

---


### Tool call

_source line 442 · 2026-05-15T08:46:17.430329+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool call

_source line 443 · 2026-05-15T08:46:18.087445+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "projects/struct_self_consist_ie/docs/paper/**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "projects/struct_self_consist_ie/docs/paper/**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1"
  }
}
```

</details>

---


### Tool result

_source line 444 · 2026-05-15T08:46:21.807771+00:00_

Web search results for query: "EMNLP 2026 reviewer guidelines review form"

Links: [{"title":"FAQ - EMNLP 2026","url":"https://2026.emnlp.org/faq/"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Instructions for Reviewers for EMNLP 2020","url":"https://2020.emnlp.org/blog/2020-05-26-instructions-for-reviewers/"},{"title":"Changes to reviewer volunteering requirement and incentives in May 2025 cycle (EMNLP 2025)","url":"http://aclrollingreview.org/incentives2025"},{"title":"ClimateNLP 2026","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"Advice on Reviewing for EMNLP","url":"https://2020.emnlp.org/blog/2020-05-17-write-good-reviews/"},{"title":"EMNLP 2026 | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026"},{"title":"EMNLP | OpenReview","url":"https://openreview.net/group?id=EMNLP"},{"title":"EMNLP 2023 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2023%2FConference"}]

I found search results related to EMNLP 2026. Based on the results, here's what I found:

## EMNLP 2026 Review Process

EMNLP 2026 uses the ACL Rolling Review (ARR) system where submissions receive reviews and meta-reviews from ARR reviewers and action editors, and Senior Area Chairs and Program Chairs make acceptance decisions from the ARR reviews and meta-reviews.

## Important Dates for Reviewers

If you receive review assignments, reviews must be completed by July 6, or meta-reviews by July 29.

## Review Form Structure

While the search results don't contain the specific EMNLP 2026 reviewer guidelines or review form, the results reference the ARR (ACL Rolling Review) platform which handles the reviews. The actual review form and detailed guidelines would typically be available throu
…[truncated 500 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 5384
}
```

</details>

---


### Tool result

_source line 445 · 2026-05-15T08:46:25.774099+00:00_

Web search results for query: "ACL ARR review form criteria 2026 reviewer guidelines"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"}]

Based on the web search results, I found comprehensive information about ACL ARR review form criteria and reviewer guidelines for 2026. Here's what I found:

## Review Form Criteria

The main criteria for Findings papers are soundness and reproducibility, while conference recommendations may also consid
…[truncated 2218 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 9802
}
```

</details>

---


### Tool result

_source line 446 · 2026-05-15T08:47:14.575684+00:00_

&lt;persisted-output>
Output too large (49.2KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-2-a0c838f5/313d3164-b33f-469a-ac80-ab56759640ec/tool-results/toolu_01KP4iaFBTELYQpzGV1zxGJw.txt

Preview (first 2KB):
{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 60, \"total_citations\": 91, \"unique_cited_keys\": 60, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 53, \"online_not_found\": 3, \"online_mismatch\": 4}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"angelopoulos2021conformal\", \"type\": \"inproceedings\", \"title\": \"Uncertainty Sets for Image Classifiers using Conformal Prediction\", \"authors\": \"Angelopoulos, Anastasios N. and Bates, Stephen and Malik, Jitendra and Jordan, M...\", \"year\": \"2021\", \"venue\": \"ICLR 2021\"}, {\"key\": \"brown2024monkeys\", \"type\": \"article\", \"title\": \"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\", \"authors\": \"Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, ...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2407.21787\"}, {\"key\": \"chen2024usc\", \"type\": \"inproceedings\", \"title\": \"Universal Self-Consistency for Large Language Model Generation\", \"authors\": \"Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Y...\", \"year\": \"2024\", \"venue\": \"arXiv preprint (ICML 2024 Workshop ICL)\"}, {\"key\": \"cobbe2021verifiers\", \"type\": \"article\", \"title\": \"Training Verifiers to Solve Math Word Problems\", \"authors\": \"Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, ...\", \"year\": \"2021\", \"venue\": \"arXiv preprint arXiv:2110.14168\"}, {\"key\": \"culotta2004confidence\", \"type\": 
…[truncated 363 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 57145
}
```

</details>

---


### Tool result

_source line 447 · 2026-05-15T08:47:14.577306+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 56489
}
```

</details>

---


### Tool call

_source line 448 · 2026-05-15T08:47:19.097425+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/docs/paper/**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/docs/paper/**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 449 · 2026-05-15T08:47:19.499950+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 402
}
```

</details>

---


### Tool call

_source line 450 · 2026-05-15T08:47:20.906316+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form: all scoring dimensions, their scales (numeric ranges), and descriptions. I need every field a reviewer must fill out."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form: all scoring dimensions, their scales (numeric ranges), and descriptions. I need every field a reviewer must fill out."
  }
}
```

</details>

---


### Tool call

_source line 451 · 2026-05-15T08:47:21.057304+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 452 · 2026-05-15T08:47:21.057752+00:00_

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
15	\usepackage{multirow}
16	\usepackage{xcolor}
17	\usepackage{subcaption}
18	
19	\graphicspath{{figures/}}
20	
21	\title{Strong Predictors, Weak Selectors:\\ Confidence Signals for Test-Time Scaling in Information Extraction under Constrained Decoding}
22	
23	\author{Anonymous}
24	
25	\begin{document}
26	\maketitle
27	
28	\input{sections/abstract}
29	\input{sections/introduction}
30	\input{sections/related_work}
31	\input{sections/method}
32	\input{sections/experiments}
33	\input{sections/discussion}
34	\input{sections/conclusion}
35	
36	\section*{Limitations}
37	\input{sections/limitations}
38	
39	\section*{Ethics Statement}
40	All experiments use publicly available benchmarks (SciERC, CoNLL-2003, WNUT-17) and open-weight models (Qwen3-8B, LLaMA-3.1-8B).
41	No new human data was collected or annotated for this study.
42	Our findings on signal limitations could inform more reliable deployment of IE systems by guiding practitioners toward appropriate confidence signals for their use case.
43	
44	\bibliography{references}
45	
46	\appendix
47	\input{sections/appendix}
48	
49	\end{document}
50	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 453 · 2026-05-15T08:47:29.871802+00:00_

# ACL Rolling Review Form - Complete Scoring Dimensions

## Required Review Fields

**1. Paper Summary**
Open-ended text field for describing paper content and identifying potential misunderstandings.

**2. Summary of Strengths**
Open-ended text for major publication reasons (methodology, empirical results, clarity, etc.).

**3. Summary of Weaknesses**
Numbered open-ended text addressing concerns prioritizing other papers, including correctness and impact issues.

**4. Comments/Suggestions/Typos**
Open-ended text for improvement suggestions beyond main concerns.

**5. Reviewer Confidence**
Scale: 1-5
- 5 = "Positive that my evaluation is correct"
- 4 = "Quite sure"
- 3 = "Pretty sure, but there's a chance I missed something"
- 2 = "Willing to defend my evaluation, but fairly likely missed details"
- 1 = "Not my area, or paper is very hard to understand"

**6. Soundness**
Scale: 1-5 (with .5 increments)
- 5 = "Excellent: most thorough study"
- 4 = "Strong: sufficient support for claims"
- 3 = "Acceptable: sufficient for main claims"
- 2 = "Poor: main claims unsupported"
- 1 = "Major Issues: not sufficiently thorough"

**7. Excitement**
Scale: 1-5 (with .5 increments)
- 5 = "Highly Exciting: recommend to others"
- 4 = "Exciting: mention to others"
- 3 = "Interesting: might mention points"
- 2 = "Potentially Interesting: doesn't resonate personally"
- 1 = "Not Exciting: lacks relevance to community"

**8. Overall Assessment**
Scale: 1-5 (with .5 increments)
- 5 = "Consider for Award"
- 4 = "Conference acceptance"
- 3 = "Findings track"
- 2 = "Resubmit next cycle"
- 1 = "Do not resubmit"

**9. Best Paper Justification**
Conditional open-ended text (if rating 4.5-5).

**10. Limitations and Societal Impact**
Open-ended evaluation of author discussion regarding limitations and potential impacts.

**11. Ethical Concerns**
Open-ended assessment against ACL Code of Ethics and submission checklist.

**12. Needs Ethics Review**
Yes/No decision with open-ended justification.

**
…[truncated 808 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 8965
}
```

</details>

---


### Tool call

_source line 454 · 2026-05-15T08:47:34.640958+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 455 · 2026-05-15T08:47:34.641446+00:00_

1	\begin{abstract}
2	Test-time scaling through multi-sample generation promises quality improvements for LLM-based information extraction (IE), but which confidence signals best serve quality estimation versus sample selection remains unclear.
3	Under constrained decoding---the standard inference regime for schema-compliant IE---we compare five signals from three families (structural, surface, model-internal) across NER (three datasets) and RE (SciERC, preliminary) with two 8B-parameter model families.
4	For quality estimation, the strongest signals achieve Spearman $\rho{=}0.38$ and AUROC${=}0.75$, with ranking and classification favoring different signals depending on task complexity.
5	However, this estimation does not translate into selection gains: four of five signals are instance-level by construction, and log-probability---the only per-sample signal---fails to outperform greedy decoding ($p{>}0.39$, bootstrap) despite 13--18~pp of oracle headroom.
6	We term this the \textit{correlation-selection gap} and diagnose its mechanism: log-probability scores are severely compressed under constrained decoding, but in the 40\% of instances where compression is mitigated, log-probability becomes a significant selector ($+2.9$~pp, $p{=}0.01$).
7	Signal rankings further depend on task difficulty, with consistent ordering across models but model-dependent magnitude.
8	These results reframe consistency signals as quality estimators rather than output selectors for structured IE under constrained decoding.
9	\end{abstract}
10	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 456 · 2026-05-15T08:47:35.043345+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 457 · 2026-05-15T08:47:35.094159+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Self-consistency---sampling multiple outputs and aggregating them---has become a powerful strategy for improving language model reasoning.
4	On discrete-answer tasks such as arithmetic and commonsense QA, majority voting over chain-of-thought samples yields large gains: +18 percentage points on GSM8K (PaLM-540B; \citealp{wang2023selfconsistency}).
5	More broadly, test-time compute scaling through repeated sampling and selection has emerged as a complementary axis to model scaling, offering substantial quality improvements at inference time \cite{snell2024scaling, brown2024monkeys}.
6	These results rest on a shared assumption: that among $N$ stochastic samples, a selection mechanism can identify better outputs.
7	For tasks with a single correct answer, this assumption holds naturally---the majority vote is the selector.
8	But information extraction (IE) poses a fundamentally different challenge.
9	The output is not a single token or number; it is a \textit{set} of entities or relations with internal dependencies, where two samples may extract overlapping but non-identical structures.
10	There is no obvious majority to vote on, partial agreement is the norm rather than the exception, and the space of valid outputs is combinatorially large.
11	Can self-consistency still provide useful signal in this structured setting?
12	
13	Prior work on confidence estimation for LLM-based IE has conflated two distinct objectives: \textit{quality estimation} (which inputs does the model handle reliably?) and \textit{sample selection} (which of $N$ outputs is best?).
14	These require fundamentally different signal properties: the former benefits from instance-level aggregation, while the latter demands per-sample discrimination.
15	Self-consistency methods for discrete answers \cite{wang2023selfconsistency, chen2024usc} and weighted variants \cite{taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalen
…[truncated 5169 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 458 · 2026-05-15T08:47:35.395852+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 459 · 2026-05-15T08:47:35.396394+00:00_

1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Self-consistency and test-time scaling.}
4	Self-consistency decoding \cite{wang2023selfconsistency} improves reasoning by majority voting over chain-of-thought samples, assuming a discrete answer space.
5	Extensions to free-form text use LLM-based comparison \cite{chen2024usc}, atomic sub-claim decomposition \cite{thirukovalluru2024atomic}, or cross-sample hallucination detection \cite{manakul2023selfcheckgpt}.
6	For test-time scaling, \citet{snell2024scaling} characterize compute scaling laws and \citet{brown2024monkeys} show best-of-$N$ gains across tasks.
7	Recent reward-free selectors include confidence-weighted voting \cite{taubenfeld2025cisc}, KL-based self-certainty \cite{kang2025selfcertainty}, adaptive sampling \cite{kim2026reasc}, ranked aggregation \cite{wang2025rankedvoting}, and latent-space consistency \cite{oh2025latentsc}.
8	Concurrently, \citet{feng2025optimal} and \citet{wang2025make} adapt self-consistency to difficulty-aware settings, echoing our finding that signal rankings shift with task complexity; \citet{li2025llms} propose generative self-aggregation for IE but focus on output fusion rather than confidence-based selection.
9	All of the above target reasoning/QA with discrete answers or specific aggregation strategies.
10	Our work extends self-consistency to set-valued structured outputs and identifies the correlation-selection gap: strong quality estimation ($\rho{=}0.38$) coexists with selection failure ($p{>}0.39$).
11	
12	\paragraph{Consistency for structured IE.}
13	\citet{nedellec2026consistency} study consistency--accuracy correlations for LLM-based NER/RE, corroborating our quality-estimation findings.
14	Their work leaves open three questions we address: (i)~whether structural matching improves on surface-level agreement (which they acknowledge ``overlooks semantically consistent outputs''); (ii)~whether quality estimation translates to best-of-$N$ selection; and (iii)~whet
…[truncated 2752 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 460 · 2026-05-15T08:47:36.400327+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 461 · 2026-05-15T08:47:36.401031+00:00_

1	\section{Method}\label{sec:method}
2	
3	\subsection{Problem Formulation}\label{sec:formulation}
4	
5	Given a language model $\mathcal{M}$ and input $x$, we sample $N$ structured outputs $\{y_1, \ldots, y_N\}$ at temperature $T > 0$ via constrained decoding \cite{willard2023guided}.
6	Each $y_i$ is an entity set (NER) or relation set (RE).
7	A confidence signal $c$ serves two purposes: (a) \textit{quality estimation}---predicting which instances the model handles reliably, and (b) \textit{sample selection}---identifying the best output among $N$ candidates.
8	
9	A \textbf{per-sample signal} scores each $y_i$ independently, $c_{\text{ps}}: (x, y_i) \to \mathbb{R}$, enabling direct candidate ranking.
10	An \textbf{instance-level signal} aggregates over all $N$ samples, $c_{\text{il}}: (x, \{y_i\}_{i=1}^N) \to \mathbb{R}$, producing a single score per input.
11	This asymmetry---between predicting \textit{which inputs} are easy and selecting \textit{which output} is best---is central to the correlation-selection gap we investigate.
12	Notation is summarized in Appendix~\ref{app:notation}.
13	
14	\subsection{Confidence Signals}\label{sec:signals}
15	
16	We use \textit{confidence signal} as the umbrella term for all five measures.
17	Four are \textit{consistency signals}---computed from inter-sample agreement---spanning two families: \textit{structural} (Soft Jaccard [SJ], entity voting confidence [VC]) and \textit{surface} (exact match [EM], Fleiss' $\kappa$ [FK]).
18	The fifth, log-probability, is the sole \textit{model-internal} signal and the only one that scores individual samples rather than the instance as a whole.
19	
20	\paragraph{Log-probability (model-internal, per-sample).}
21	The only per-sample signal.
22	For sample $y_i$ with tokens $t_1, \ldots, t_{|y_i|}$:
23	\begin{equation}\label{eq:logprob}
24	c_{\text{lp}}(y_i) = \frac{1}{|y_i|} \sum_{j=1}^{|y_i|} \log p_{\mathcal{M}}(t_j \mid t_{<j}, x)
25	\end{equation}
26	
27	\paragraph{Exact match voting (surface
…[truncated 4314 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 462 · 2026-05-15T08:47:36.552037+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 463 · 2026-05-15T08:47:36.552580+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Datasets.}
8	We evaluate on three English IE benchmarks spanning a difficulty gradient.
9	\textbf{SciERC} \cite{luan2018scierc} contains 551 test instances annotated for joint NER (6 types) and RE (7 types).
10	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} provides 3{,}453 test sentences with 4 entity types, where models achieve ${\approx}$91\% micro F1.
11	\textbf{WNUT-17} \cite{derczynski2017wnut} consists of 1{,}287 social media instances with emerging entities, used to probe method boundaries (52\% zero F1).
12	
13	\paragraph{Models and sampling.}
14	Both \textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are fine-tuned with LoRA (rank$=$32, $\alpha{=}64$) for 5 epochs using LLaMA Factory \cite{zheng2024llamafactory} under identical training procedures, ensuring comparisons across the two model families (both at 8B scale) reflect model differences rather than training confounds.
15	We draw $N{=}8$ samples at $T{=}1.0$ (primary), with $N{=}16$ for scaling experiments.\footnote{$N{=}16$ results for CoNLL (Qwen) and SciERC (LLaMA) are in Table~\ref{tab:robustness} (Appendix~\ref{app:robustness}).}
16	Quality estimation uses Spearman $\rho$ and AUROC; downstream utility uses best-of-$N$ selection F1 with exact span matching (NER) and head-tail-label matching (RE).
17	Inference uses vLLM with constrained decoding \cite{willard2023guided}.
18	
19	%% ============================================================
20	\subsection{Quality Estimation Results}
21	\label{sec:qe_results}
22	
23	\begin{table*}[t]
24	\centering
25	\small
26	\caption{Quality estimation across tasks and models (Spearman $\rho$ and AUROC). Best value per block and column in \textbf{bold}. SciERC evaluates joint NER (6 types) and RE (7 types, single benchmark---preliminary); CoNLL evaluates NER (4 types). $N{=}8$ results use seed${=}42$. $N{=}16$ results (LLaMA CoNLL only; 3-
…[truncated 11185 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 464 · 2026-05-15T08:47:36.754099+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool result

_source line 465 · 2026-05-15T08:47:36.755398+00:00_

1	\section{Discussion}\label{sec:discussion}
2	
3	\paragraph{Practical recommendations.}
4	For per-instance quality ranking, VC provides the strongest rank correlation ($\rho{=}0.38$), though exact match leads binary discrimination (AUROC${=}0.749$); under conditional filtering, EM leads on both NER and RE ($\rho{=}0.360$, $0.417$).
5	Signal rankings depend on task difficulty---EM dominates easy tasks (CoNLL), VC and SJ dominate hard tasks (SciERC)---directionally consistent across tested model families, though with model-dependent magnitude.
6	When model capability is insufficient (WNUT-17), all signals converge toward non-significant conditional correlations (Table~\ref{tab:wnut}).
7	
8	\paragraph{Why the gap exists: two layers.}
9	\textit{Layer 1 (definitional):} Four of five signals are instance-level aggregates that assign a single score per input; they cannot rank candidates by construction.
10	Consensus-proximity selection (\S\ref{sec:evaluation}) does not recover per-sample discrimination (Table~\ref{tab:selection}).
11	\textit{Layer 2 (constrained-decoding compression):} Log-probability, the only per-sample signal, also fails to exploit the 13--18~pp oracle headroom.
12	Under constrained decoding, logprob scores are severely compressed: 60\% of instances have a within-sample range below 0.05, and 75\% of pairwise comparisons are effective ties ($|\Delta|{<}0.026$; Appendix~\ref{app:logprob_ties}).
13	In the 40\% of instances where compression is mitigated (logprob range ${\geq}0.05$, $n{=}210$), logprob \textit{significantly} outperforms greedy ($+2.9$~pp, $p{=}0.01$; within-instance $\rho$: 0.08$\to$0.39).
14	This diagnostic confirms that logprob carries useful per-sample quality information; score compression under constrained decoding---the standard regime for schema-compliant IE---is the primary mechanistic bottleneck, though whether compression fully accounts for the gap remains open.
15	Diversity-stratified analysis confirms the gap persists even amon
…[truncated 1387 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1
}
```

</details>

---


### Tool call

_source line 466 · 2026-05-15T08:47:37.710327+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 467 · 2026-05-15T08:47:37.710794+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	Within the constrained decoding regime standard for structured IE, we demonstrate that consistency signals are effective quality estimators ($\rho$ up to 0.38, AUROC up to 0.75) but fail at sample selection---the \textit{correlation-selection gap}.
4	Four of five signals are instance-level by construction; log-probability also fails ($p{>}0.39$) despite 13--18~pp oracle headroom.
5	Mechanistic diagnosis identifies logprob score compression as the bottleneck: where compression is mitigated, logprob becomes a significant selector ($+2.9$~pp, $p{=}0.01$).
6	Signal rankings depend on task difficulty, with consistent ordering across two model families at 8B scale.
7	RE findings rest on SciERC alone and warrant multi-benchmark validation.
8	Trained verifiers, relaxed decoding constraints, scaling to 70B+ models, and conformal prediction are promising directions.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 468 · 2026-05-15T08:47:38.614516+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 469 · 2026-05-15T08:47:38.665383+00:00_

1	Our evaluation covers three datasets but only one RE benchmark (SciERC), where 40\% of instances receive zero F1, compressing the discriminable range and limiting signal differentiation for relation extraction.
2	RE selection failure persists even when restricting to non-zero F1 instances (Appendix~\ref{app:re_conditional_selection}), ruling out floor effects as the sole explanation, but generalization to other RE benchmarks remains unvalidated.
3	WNUT-17 confirms the capability boundary of our approach, but our positive results on formal-domain text (CoNLL, SciERC) have not been validated on informal or noisy text where models achieve non-trivial performance.
4	
5	We evaluate two model families (Qwen3-8B and LLaMA-3.1-8B), both at 8B parameters.
6	A 3-seed robustness analysis confirms that signal rankings are stable across seeds ($\sigma{\leq}0.025$; Table~\ref{tab:multiseed}), but whether our findings---particularly the correlation-selection gap and the difficulty-dependent signal ordering---hold for larger models (70B+) or closed-source APIs remains untested.
7	Larger models may produce higher-quality and more diverse samples, potentially altering the signal landscape.
8	
9	Our analysis of selection potential uses only unsupervised signals.
10	We do not train a dedicated verifier or reward model, leaving unknown how much of the oracle headroom a supervised approach could recover.
11	
12	We evaluate at $N{=}8$ and $N{=}16$.
13	The behavior of confidence signals at larger sample sizes (e.g., $N{=}64$ or $N{=}128$) is unknown, and $N$-scaling gains are setting-dependent: SJ improves by $+0.052$ on Qwen SciERC NER but only $+0.016$ on LLaMA SciERC NER when doubling from $N{=}8$ to $N{=}16$.
14	
15	On CoNLL with LLaMA, the SJ--FK gap is only 0.003 ($\rho{=}0.431$ vs.\ $0.428$), so the structural advantage over surface signals may not generalize to all simple-schema datasets.
16	Constrained decoding (Outlines/vLLM) enforces schema compliance, potentially compressing 
…[truncated 1014 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 470 · 2026-05-15T08:47:38.866526+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 471 · 2026-05-15T08:47:39.118842+00:00_

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
21	$c_{\text{vote}}$ & Entity voting confidence \\
22	$c_{\text{lp}}$ & Log-probability (mean token log-likelihood) \\
23	\bottomrule
24	\end{tabular}
25	\caption{Notation used throughout the paper.}
26	\label{tab:notation}
27	\end{table}
28	
29	\section{Robustness Analysis}\label{app:robustness}
30	
31	\begin{table}[t]
32	\centering
33	\small
34	\caption{Signal robustness across configurations (Spearman $\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: cross-model transfer (LLaMA CoNLL $N{=}16$, 3-seed mean $\pm\sigma$). $^\dagger$Mean over 3 seeds ($\sigma{=}0.025$; individual: 0.428, 0.424, 0.384).}
35	\label{tab:robustness}
36	\begin{tabular}{llcc}
37	\toprule
38	& & NER $\rho$ & RE $\rho$ \\
39	\midrule
40	\multicolumn{4}{l}{\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\
41	\quad SJ & $T{=}0.7$ & 0.388 & 0.234 \\
42	\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\
43	\quad FK & $T{=}0.7$ & 0.321 & 0.184 \\
44	\quad FK & $T{=}1.0$ & 0.267 & 0.275 \\
45	\midrule
46	\multicolumn{4}{l}{\textit{Sample size} (Qwen SciERC, $T{=}1.0$)} \\
47	\quad SJ & $N{=}8$  & 0.360 & 0.250 \\
48	\quad SJ & $N{=}16$ & 0.412$^\dagger$ & 0.281 \\
49	\quad FK & $N{=}8$  & 0.267 & 0.275 \\
50	\quad FK & $N{=}16$ & 0.280 & 0.279 \\
51	\midrule
52	\multicolumn{4}{l}{\textit{Cross-model} (LLaMA CoNLL, $N{=}16$, 3 seeds)} \\
53	\quad SJ &  & $0.463{\pm}0.007$ & --- \\
54	\quad FK &  & $0.455{\pm}0.006$ & --- \\
55	\quad EM &  & $0.460{\pm
…[truncated 27696 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 252
}
```

</details>

---


### Tool call

_source line 472 · 2026-05-15T08:47:50.665306+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-2-a0c838f5/313d3164-b33f-469a-ac80-ab56759640ec/tool-results/toolu_01KP4iaFBTELYQpzGV1zxGJw.txt",
  "offset": "0",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-2-a0c838f5/313d3164-b33f-469a-ac80-ab56759640ec/tool-results/toolu_01KP4iaFBTELYQpzGV1zxGJw.txt",
    "offset": "0",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 473 · 2026-05-15T08:47:50.917860+00:00_

0	{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 60, \"total_citations\": 91, \"unique_cited_keys\": 60, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 53, \"online_not_found\": 3, \"online_mismatch\": 4}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"angelopoulos2021conformal\", \"type\": \"inproceedings\", \"title\": \"Uncertainty Sets for Image Classifiers using Conformal Prediction\", \"authors\": \"Angelopoulos, Anastasios N. and Bates, Stephen and Malik, Jitendra and Jordan, M...\", \"year\": \"2021\", \"venue\": \"ICLR 2021\"}, {\"key\": \"brown2024monkeys\", \"type\": \"article\", \"title\": \"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\", \"authors\": \"Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, ...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2407.21787\"}, {\"key\": \"chen2024usc\", \"type\": \"inproceedings\", \"title\": \"Universal Self-Consistency for Large Language Model Generation\", \"authors\": \"Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Y...\", \"year\": \"2024\", \"venue\": \"arXiv preprint (ICML 2024 Workshop ICL)\"}, {\"key\": \"cobbe2021verifiers\", \"type\": \"article\", \"title\": \"Training Verifiers to Solve Math Word Problems\", \"authors\": \"Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, ...\", \"year\": \"2021\", \"venue\": \"arXiv preprint arXiv:2110.14168\"}, {\"key\": \"culotta2004confidence\", \"type\": \"inproceedings\", \"title\": \"Confidence Estimation for Information Extraction\", \"authors\": \"Culotta, Aron and McCallum, Andrew\", \"year\": \"2004\", \"venue\": \"HLT-NAACL 2004\"}, {\"key\": \"derczynski2017wnut\", \"type\": \"inproceedings\", \"title\": \"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recogni
…[truncated 48404 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 252
}
```

</details>

---


### Tool call

_source line 474 · 2026-05-15T08:47:50.968509+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "MBR decoding structured prediction information extraction 2024 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "MBR decoding structured prediction information extraction 2024 2025 2026"
  }
}
```

</details>

---


### Tool call

_source line 475 · 2026-05-15T08:47:51.119562+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "test-time scaling verification survey 2025 2026 LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "test-time scaling verification survey 2025 2026 LLM"
  }
}
```

</details>

---


### Tool call

_source line 476 · 2026-05-15T08:47:51.270572+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "self-consistency structured output 2025 2026 NER relation extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "self-consistency structured output 2025 2026 NER relation extraction"
  }
}
```

</details>

---


### Tool result

_source line 477 · 2026-05-15T08:47:58.352457+00:00_

Web search results for query: "test-time scaling verification survey 2025 2026 LLM"

Links: [{"title":"What, How, Where, and How Well? A Survey on Test-Time Scaling in Large Language Models","url":"https://testtimescaling.github.io/"},{"title":"Trust but Verify! A Survey on Verification Design for Test-time Scaling","url":"https://arxiv.org/html/2508.16665v3"},{"title":"GitHub - testtimescaling/testtimescaling.github.io: \"what, how, where, and how well? a survey on test-time scaling in large language models\" repository","url":"https://github.com/testtimescaling/testtimescaling.github.io"},{"title":"[2503.24235] A Survey on Test-Time Scaling in Large Language Models: What, How, Where, and How Well?","url":"https://arxiv.org/abs/2503.24235"},{"title":"GitHub - ThreeSR/Awesome-Inference-Time-Scaling: Paper List of Inference/Test Time Scaling/Computing · GitHub","url":"https://github.com/ThreeSR/Awesome-Inference-Time-Scaling"},{"title":"A Survey on Test-Time Scaling. This blog is based a comprehensive… | by Yanan Chen | Medium","url":"https://medium.com/@yananchen1116/a-survey-on-test-time-scaling-04b1c1dadb9d"},{"title":"Paper page - What, How, Where, and How Well? A Survey on Test-Time Scaling in Large Language Models","url":"https://huggingface.co/papers/2503.24235"},{"title":"NeurIPS Poster Rethinking Fine-Tuning when Scaling Test-Time Compute: Limiting Confidence Improves Mathematical Reasoning","url":"https://neurips.cc/virtual/2025/poster/116423"},{"title":"Scaling LLM Test-Time Compute Optimally Can be More Effective than Scaling Parameters for Reasoning | OpenReview","url":"https://openreview.net/forum?id=4FWAwZtd2n"},{"title":"The State Of LLMs 2025: Progress, Progress, and Predictions","url":"https://magazine.sebastianraschka.com/p/state-of-llms-2025"}]

I found comprehensive results about test-time scaling in LLMs, including specific surveys and verification approaches. Here are the key findings:

## Major Surveys

The most prominent survey is "What, How,
…[truncated 1489 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7232
}
```

</details>

---


### Tool result

_source line 478 · 2026-05-15T08:47:58.603660+00:00_

Web search results for query: "self-consistency structured output 2025 2026 NER relation extraction"

Links: [{"title":"Benchmarking LLM-based Information Extraction Tools for ...","url":"https://www.medrxiv.org/content/10.64898/2026.01.19.26344287v1.full.pdf"},{"title":"STRUCTSENSE: A TASK-AGNOSTIC AGENTIC FRAMEWORK for STRUCTURED INFORMATION EXTRACTION with HUMAN-IN-THE-LOOP EVALUATION and BENCHMARKING","url":"https://arxiv.org/html/2507.03674v1"},{"title":"The construction and refined extraction techniques of knowledge graph based on large language models | Scientific Reports","url":"https://www.nature.com/articles/s41598-026-38066-w"},{"title":"Cross-Type and Cross-Task Multi-Agent LLM Collaboration ...","url":"https://aclanthology.org/2025.findings-acl.718.pdf"},{"title":"Agent-based multimodal information extraction for nanomaterials | npj Computational Materials","url":"https://www.nature.com/articles/s41524-025-01674-7"},{"title":"GitHub - zjunlp/Low-resource-KEPapers: A Paper List of Low-resource Information Extraction","url":"https://github.com/zjunlp/Low-resource-KEPapers"},{"title":"Structured information extraction from scientific text with large language models | Nature Communications","url":"https://www.nature.com/articles/s41467-024-45563-x"},{"title":"GitHub - quqxui/Awesome-LLM4IE-Papers: Awesome papers about generative Information Extraction (IE) using Large Language Models (LLMs) · GitHub","url":"https://github.com/quqxui/Awesome-LLM4IE-Papers"},{"title":"Large Language Models for Generative Information Extraction: A Survey","url":"https://arxiv.org/html/2312.17617v3"},{"title":"DiZiNER: Disagreement-guided Instruction Refinement via Pilot Annotation Simulation for Zero-shot Named Entity Recognition","url":"https://arxiv.org/html/2604.15866v1"}]

Based on the search results, here are the key findings on self-consistency, structured output, NER, and relation extraction in 2025-2026:

## Recent Developments (2025-2026)

### Self-Consistency in Info
…[truncated 1464 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7333
}
```

</details>

---


### Tool result

_source line 479 · 2026-05-15T08:47:59.356523+00:00_

Web search results for query: "MBR decoding structured prediction information extraction 2024 2025 2026"

Links: [{"title":"Frontiers | Grammar-constrained decoding for structured information extraction with fine-tuned generative models applied to clinical trial abstracts","url":"https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2024.1406857/full"},{"title":"SLOT: Structuring the Output of Large Language Models","url":"https://aclanthology.org/2025.emnlp-industry.32.pdf"},{"title":"GitHub - Saibo-creator/Awesome-LLM-Constrained-Decoding: A curated list of papers related to constrained decoding of LLM, along with their relevant code and resources. · GitHub","url":"https://github.com/Saibo-creator/Awesome-LLM-Constrained-Decoding"},{"title":"Efficient Minimum Bayes Risk Decoding using Low-Rank Matrix Completion Algorithms","url":"https://arxiv.org/html/2406.02832v1"},{"title":"[2311.05263] Model-Based Minimum Bayes Risk Decoding for Text Generation","url":"https://arxiv.org/abs/2311.05263"},{"title":"Structure-Conditional Minimum Bayes Risk Decoding","url":"https://arxiv.org/html/2510.20700"},{"title":"A Guide to Structured Outputs Using Constrained Decoding","url":"https://www.aidancooper.co.uk/constrained-decoding/"},{"title":"Speculative Decoding and Beyond: A Survey of Speculative Decoding Techniques","url":"https://blog.codingconfessions.com/p/a-selective-survey-of-speculative-decoding"},{"title":"Benchmarking LLM-based Information Extraction Tools for Medical Documents | medRxiv","url":"https://www.medrxiv.org/content/10.64898/2026.01.19.26344287v1.full"},{"title":"ICLR 2024 Papers","url":"https://iclr.cc/virtual/2024/papers.html"}]

I've found several relevant research papers and resources related to MBR (Minimum Bayes Risk) decoding, structured prediction, and information extraction from 2024-2026:

## Recent Research on MBR Decoding

Minimum Bayes Risk (MBR) decoding has been shown to be a powerful alternative to beam search d
…[truncated 1879 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8388
}
```

</details>

---


### Tool call

_source line 480 · 2026-05-15T08:48:05.331735+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Nédellec Yao Xia Bossy 2026 \"consistency accuracy correlation\" LLM entity relation extraction plant health Genomics Informatics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Nédellec Yao Xia Bossy 2026 \"consistency accuracy correlation\" LLM entity relation extraction plant health Genomics Informatics"
  }
}
```

</details>

---


### Tool call

_source line 481 · 2026-05-15T08:48:06.135459+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"correlation-selection gap\" OR \"quality estimation sample selection\" confidence LLM structured output 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"correlation-selection gap\" OR \"quality estimation sample selection\" confidence LLM structured output 2025 2026"
  }
}
```

</details>

---


### Tool result

_source line 482 · 2026-05-15T08:48:10.814720+00:00_

Web search results for query: "Nédellec Yao Xia Bossy 2026 "consistency accuracy correlation" LLM entity relation extraction plant health Genomics Informatics"

Links: [{"title":"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12888769/"},{"title":"Main Conference Accepted Papers -","url":"https://2026.eacl.org/program/main-accepted/"},{"title":"Paper Digest: Recent Papers on Relation Extraction – Resources | Paper Digest","url":"https://resources.paperdigest.org/2020/04/recent-papers-on-relation-extraction/"},{"title":"Benchmarking LLM-based Information Extraction Tools for Medical Documents | medRxiv","url":"https://www.medrxiv.org/content/10.64898/2026.01.19.26344287v1.full"},{"title":"A review of named entity recognition: from learning methods to modelling paradigms and tasks | Artificial Intelligence Review | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10462-025-11321-8"},{"title":"GitHub - quqxui/Awesome-LLM4IE-Papers: Awesome papers about generative Information Extraction (IE) using Large Language Models (LLMs) · GitHub","url":"https://github.com/quqxui/Awesome-LLM4IE-Papers"},{"title":"A Comprehensive Survey on Relation Extraction: Recent Advances and New Frontiers | ACM Computing Surveys","url":"https://dl.acm.org/doi/full/10.1145/3674501"},{"title":"Large language model augmented joint learning framework for entity-relation extraction - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S1568494625014073"},{"title":"A survey on cutting-edge relation extraction techniques based on language models","url":"https://arxiv.org/html/2411.18157v1"},{"title":"Leveraging large language models for the deidentification and temporal normalization of sensitive health information in electronic health records | npj Digital Medicine","url":"https://www.nature.com/articles/s41746-025-
…[truncated 1018 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 5482
}
```

</details>

---


### Tool result

_source line 483 · 2026-05-15T08:48:14.077860+00:00_

Web search results for query: ""correlation-selection gap" OR "quality estimation sample selection" confidence LLM structured output 2025 2026"

Links: [{"title":"Cycles of Thought: Measuring LLM Confidence through Stable Explanations","url":"https://arxiv.org/html/2406.03441v1"},{"title":"SubLIME: Subset Selection via Rank Correlation Prediction for Data-Efficient LLM Evaluation - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.1477/"},{"title":"LLM Evaluation Metrics: The Ultimate LLM Evaluation Guide - Confident AI","url":"https://www.confident-ai.com/blog/llm-evaluation-metrics-everything-you-need-for-llm-evaluation"},{"title":"SubLIME: Subset Selection via Rank Correlation Prediction ...","url":"https://aclanthology.org/2025.acl-long.1477.pdf"},{"title":"Calibrating LLM Confidence by Probing Perturbed ...","url":"https://aclanthology.org/2025.emnlp-main.530.pdf"},{"title":"Quantifying LLMs Uncertainty with Confidence Scores | by Faustin Pulvéric | Capgemini Invent Lab | Medium","url":"https://medium.com/capgemini-invent-lab/quantifying-llms-uncertainty-with-confidence-scores-6bb8a6712aa0"},{"title":"Estimating LLM classification confidence with log probabilities (logprobs) – Eric Jinks","url":"https://ericjinks.com/blog/2025/logprobs/"},{"title":"Using Supporting Statistics to Improve LLM Confidence in Answers","url":"https://www.singlegrain.com/blog-posts/analytics/using-supporting-statistics-to-improve-llm-confidence-in-answers/"},{"title":"Measuring Confidence in LLM responses | by George Karapetyan | Medium","url":"https://medium.com/@georgekar91/measuring-confidence-in-llm-responses-e7df525c283f"},{"title":"Alkymi's Data Science Room - Building confidence in LLM outputs","url":"https://www.alkymi.io/data-science-room/building-confidence-in-llm-outputs"}]

Based on the web search results, here are the findings related to your query about correlation-selection gap, quality estimation, sample selection, confidence in LLMs, and structured output (
…[truncated 1868 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7942
}
```

</details>

---


### Tool call

_source line 484 · 2026-05-15T08:48:21.107220+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12888769/",
  "prompt": "Extract the full methodology, results, and conclusions. Specifically: 1) What signals/metrics did they use to measure consistency? 2) What datasets/tasks did they evaluate on? 3) What correlation values did they find? 4) What were their main claims? 5) Did they test sample selection (best-of-N)? 6) Did they use constrained decoding? 7) Did they compare multiple signal families? 8) Did they test across difficulty levels?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12888769/",
    "prompt": "Extract the full methodology, results, and conclusions. Specifically: 1) What signals/metrics did they use to measure consistency? 2) What datasets/tasks did they evaluate on? 3) What correlation values did they find? 4) What were their main claims? 5) Did they test sample selection (best-of-N)? 6) Did they use constrained decoding? 7) Did they compare multiple signal families? 8) Did they test across difficulty levels?"
  }
}
```

</details>

---


### Tool call

_source line 485 · 2026-05-15T08:48:21.308584+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Structure-Conditional Minimum Bayes Risk\" structured prediction 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Structure-Conditional Minimum Bayes Risk\" structured prediction 2025"
  }
}
```

</details>

---


### Tool result

_source line 486 · 2026-05-15T08:48:27.587363+00:00_

Web search results for query: ""Structure-Conditional Minimum Bayes Risk" structured prediction 2025"

Links: [{"title":"Structure-Conditional Minimum Bayes Risk Decoding - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.1616/"},{"title":"Structure-Conditional Minimum Bayes Risk Decoding","url":"https://aclanthology.org/2025.emnlp-main.1616.pdf"},{"title":"[1611.07096] Structured Prediction by Conditional Risk Minimization","url":"https://arxiv.org/abs/1611.07096"},{"title":"Empirical Minimum Bayes Risk Prediction | IEEE Journals & Magazine | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/7425216/"},{"title":"Empirical Minimum Bayes Risk Prediction: How to Extract an Extra Few % Performance from Vision Models with Just Three More Parameters | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/6909533"},{"title":"uncertainty-aware decoding with minimum bayes risk","url":"https://arxiv.org/pdf/2503.05318"},{"title":"Structured prediction - Wikipedia","url":"https://en.wikipedia.org/wiki/Structured_prediction"},{"title":"Artificial Intelligence Dec 2025","url":"https://arxiv.org/list/cs.AI/2025-12?skip=975&show=50"},{"title":"A General Framework for Consistent Structured Prediction ...","url":"https://jmlr.org/papers/volume21/20-097/20-097.pdf"},{"title":"Bayes Decision Rule for prediction problems","url":"https://stephens999.github.io/fiveMinuteStats/decision_theory_bayes_rule.html"}]

Based on the search results, here's what I found about "Structure-Conditional Minimum Bayes Risk":

## Overview

Structure-Conditional Minimum Bayes Risk Decoding is a paper by Bryan Eikema, Anna Rutkiewicz, and Mario Giulianelli published at the 2025 Conference on Empirical Methods in Natural Language Processing.

## Key Contribution

The authors curate a dataset capturing three representative types of latent structure—dialogue act, emotion, and response structure (e.g., a sentence, a paragraph, or a list)—and propose two met
…[truncated 823 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6278
}
```

</details>

---


### Tool result

_source line 487 · 2026-05-15T08:48:33.163864+00:00_

# Methodology, Results, and Conclusions Analysis

## 1) Consistency Metrics

The researchers employed **Fleiss' Kappa** as their primary consistency measure. They treated "multiple generations of the same model on the same input as different raters" and measured whether relation triplets appeared consistently across runs. Each unique predicted relation received a binary label (present/absent) per generation, yielding an N×2 rating matrix analyzed with the formula: κ = (P̄ - Pe)/(1 - Pe).

## 2) Datasets and Tasks

Evaluation focused on **document-level relation extraction (DocRE)** using the **EPOP corpus** (plant-health epidemiomonitoring data). The dataset contained:
- 5 entity types and 5 relation types
- 1,652 reference relations in the aggregated version
- Documents with nested entities, long-range relations, and strict argument-type constraints

The task avoided text-bound grounding requirements, instead requesting entity and relation extraction formatted as JSON triplets.

## 3) Correlation Values Found

Correlation analysis revealed **weak associations** across all four tested models (GPT-4o-mini, DeepSeek-V3, Kimi, Qwen3):

| Measure | Range |
|---------|-------|
| Pearson | 0.2230–0.2980 |
| Spearman's rank | 0.2019–0.2795 |
| Kendall's tau | 0.1420–0.1978 |

All p-values were statistically significant, yet the researchers concluded these correlations demonstrated "limited association between accuracy and consistency."

## 4) Main Claims

The authors asserted three primary findings:

- **Consistency does not reliably predict accuracy** in relational IE tasks, contradicting assumptions underlying self-consistency methods
- **Semantic equivalence matters**: They distinguished "recoverable variations" (synonyms, coreferences) from critical semantic errors, showing accuracy drops 23–30 points without equivalence mapping
- **Task complexity negatively impacts both metrics**: Document length and entity count showed strong negative correlations with both accuracy
…[truncated 1665 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 12056
}
```

</details>

---


### Tool call

_source line 488 · 2026-05-15T08:48:39.087692+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Zhang 2025 \"survey test-time scaling\" LLM arxiv 2503.24235"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Zhang 2025 \"survey test-time scaling\" LLM arxiv 2503.24235"
  }
}
```

</details>

---


### Tool result

_source line 489 · 2026-05-15T08:48:44.013617+00:00_

Web search results for query: "Zhang 2025 "survey test-time scaling" LLM arxiv 2503.24235"

Links: [{"title":"[2503.24235] A Survey on Test-Time Scaling in Large Language Models: What, How, Where, and How Well?","url":"https://arxiv.org/abs/2503.24235"},{"title":"What, How, Where, and How Well? A Survey on Test-Time Scaling in Large Language Models","url":"https://testtimescaling.github.io/"},{"title":"Paper page - What, How, Where, and How Well? A Survey on Test-Time Scaling in Large Language Models","url":"https://huggingface.co/papers/2503.24235"},{"title":"[2503.24235v2] What, How, Where, and How Well? A Survey on Test-Time Scaling in Large Language Models","url":"http://arxiv.org/abs/2503.24235v2"},{"title":"[2503.24235v1] What, How, Where, and How Well? A Survey on Test-Time Scaling in Large Language Models","url":"http://arxiv.org/abs/2503.24235v1"},{"title":"What, How, Where, and How Well? A Survey on Test-Time Scaling in Large Language Models | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/arxiv/2503.24235"},{"title":"A Survey of Process Reward Models: From Outcome Signals to Process Supervisions for Large Language Models","url":"https://arxiv.org/html/2510.08049v3"},{"title":"A Survey on Test-Time Scaling in Large Language Models: What, How, Where, and How Well? | alphaXiv","url":"https://www.alphaxiv.org/abs/2503.24235"},{"title":"s1: Simple test-time scaling","url":"https://aclanthology.org/2025.emnlp-main.1025.pdf"},{"title":"Trust but Verify! A Survey on Verification Design for Test-time Scaling","url":"https://arxiv.org/html/2508.16665v3"}]

I found the paper! Here are the details:

The paper is "A Survey on Test-Time Scaling in Large Language Models: What, How, Where, and How Well?" by Qiyuan Zhang and 12 other authors, submitted on March 31, 2025, with the latest version (v3) revised on May 4, 2025, available as arXiv:2503.24235.

The survey demonstrates that test-time scaling (TTS) can further elicit the problem-solving capabi
…[truncated 478 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 4925
}
```

</details>

---


### Tool call

_source line 490 · 2026-05-15T08:51:12.802366+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 — Round 1 审稿报告\n\n**论文**: Strong Predictors, Weak Selectors: Confidence Signals for Test-Time Scaling in Information Extraction under Constrained Decoding\n**审查侧重**: 新颖性 + 完整性 + 相关工作\n\n---\n\n## 总体评分\n\n**Overall**: 3/5 (Findings track)\n**一句话总结**: 实验设计扎实、统计分析严谨的负面结果论文，对 structured IE 的 test-time scaling 提供了有价值的实证警告，但核心发现的新颖性有限——correlation-selection gap 的 4/5 信号来源于定义层面的不可避免性（instance-level 信号天然无法做 sample selection），真正有趣的 logprob 压缩诊断只占论文的一小部分。\n\n---\n\n## 官方维度打分（来自 ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 统计方法严谨（bootstrap, TOST, multi-seed），但 FK 独立性假设仅以经验验证部分回应，consensus-proximity 作为 selection 唯一策略有局限 |\n| Excitement | 2.5/5 | 负面结果对从业者有参考价值，但 gap 的 4/5 来源是定义性的（instance-level 信号不可能做 per-sample selection），最有趣的 logprob 压缩分析篇幅不足 |\n| Reproducibility | 3/5 | Training config、prompt template、超参详尽（Table 7, Appendix F），但未提及代码/数据发布计划 |\n| Reviewer Confidence | 4/5 | 熟悉 self-consistency、MBR decoding、结构化 IE 和不确定性估计文献 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Contribution 1 \"systematic multi-family comparison\" 的新颖性与 framing 不匹配\n- 具体位置：Section 1 (Introduction), Contribution (i); Section 2 (Related Work), ¶2\n- 问题：论文将 \"5 signals from 3 families\" 的对比定位为主要贡献，但这本质上是 engineering benchmark——将已知的 confidence signals（logprob, exact match, Fleiss' κ 等）应用于新任务设置。与 Nédellec et al. (2026) 的增量确实存在（结构化匹配、constrained decoding、多数据集），但论文在 Introduction 中没有足够清楚地区分 \"applying known signals to a new setting\" 和 \"discovering new signals or principles\"。\n- 为什么影响接收：如果 reviewer 将这理解为 \"known metrics on new tasks\" 的简单应用研究，会直接影响 novelty 评分。\n- 建议修改方向：在 Introduction 中更明确地说明，核心贡献不是比较本身，而是 (a) 发现质量估计与选择之间的 gap，(b) logprob 压缩的机制诊断。将 Contribution 1 降级为 setup/methodology，将 Contribution 2 (gap) 提升为核心 claim。\n\n**N2** [critical] Correlation-selection gap 的 4/5 来源是定义性的，非实证发现\n- 具体位置：Section 1 (Introduction), ¶5; Section 5 (Discussion), ¶2 \"Layer 1 (definitional)\"\n- 问题：论文在 Discussion 中自己承认 4/5 信号的 selection failure 是 \"by construction\"（Layer 1），因为 instance-level 信号天然给所有候选样本相同分数。这不是一个需要通过实验才能发现的 gap——这是信号定义的直接推论。论文的真正实证贡献是 Layer 2（logprob 在 constrained decoding 下的压缩），但这在当前 framing 中被埋在了 \"gap\" 这个更大叙事之下。\n- 为什么影响接收：将定义性结论包装为实证发现会降低论文的可信度。一个熟悉这些信号的 reviewer 会立即意识到 instance-level 信号不能做 per-sample selection，这不需要实验验证。\n- 建议修改方向：(1) 在 Introduction 中提前透明化 Layer 1 是 definitional，而非卖悬念；(2) 将叙事重心转向 Layer 2——logprob（唯一的 per-sample signal）为何也失败，constrained decoding 压缩的机制及其条件性缓解（+2.9pp, p=0.01）才是论文最有价值的贡献。\n\n**N3** [critical] Related Work 遗漏关键引用\n- 具体位置：Section 2 (Related Work)\n- 问题：\n  (a) **Zhang et al. (2025) \"A Survey on Test-Time Scaling in Large Language Models: What, How, Where, and How Well?\" (arXiv:2503.24235)**——目前最全面的 test-time scaling survey，提出了系统性的 TTS 分类框架（what/how/where/how well to scale），论文引用了 Snell 和 Brown 的个别工作但遗漏了这个综述，考虑到论文标题包含 \"Test-Time Scaling\" 这个关键词，这是显著的遗漏。\n  (b) **Eikema, Rutkiewicz & Giulianelli (EMNLP 2025) \"Structure-Conditional Minimum Bayes Risk Decoding\"**——直接研究 MBR decoding 在结构化输出上的问题，发现 common utility functions 在结构化场景（dialogue, instruction-following）下表现不佳，与本文 Section 5 ¶3 的 MBR 失败发现高度相关。\n- 为什么影响接收：Related Work 完整性是 EMNLP Findings 的基本要求；遗漏了同一 venue (EMNLP 2025) 的直接相关工作会被 reviewer 视为文献调研不充分。\n- 建议修改方向：在 Section 2 ¶1 补充 Zhang et al. survey 作为 test-time scaling 的综述引用；在 ¶3 (uncertainty/MBR) 补充 Eikema et al. (2025) 并讨论其 utility function 对结构化输出不适用的发现如何与本文的 MBR failure 互相印证。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] \"cross-model\" 措辞过度外推\n- 具体位置：Section 1 (Introduction), Contribution (iii) \"consistent ordering across models\"；Section 4.1 \"cross-model stability is strong\"\n- 问题：实际只测试了 2 个同规模 (8B) 模型。\"cross-model\" 的说法暗示了比实际更广的泛化性。Limitations 中承认了 70B+/closed-source 未测试，但 main text 的措辞没有同步限定。\n- 建议：将 main text 中的 \"cross-model\" 改为 \"cross-architecture\" 或 \"across two model families (at 8B scale)\"，使措辞与实际实验范围匹配。\n\n**W2** [warning] Abstract 信息密度过高\n- 具体位置：sections/abstract.tex\n- 问题：9 行 abstract 包含：5 个信号名、3 个信号家族名、4 个数字 (ρ=0.38, AUROC=0.75, p>0.39, +2.9pp)、3 个数据集（隐含在 \"three datasets\"）、2 个任务、2 个模型（隐含在 \"two 8B-parameter model families\"）、plus \"correlation-selection gap\" 这个新术语的引入。对于不熟悉该领域的 reviewer，首次阅读时信息过载。\n- 建议：减少具体数字，将 signal family 名称移到正文；abstract 聚焦于问题-发现-意义三段式。\n\n**W3** [warning] 术语一致性问题\n- 具体位置：全文多处\n- 问题：\n  (a) \"VC\" 在 Table 1 和正文中用，但 Method Section 定义为 \"entity voting confidence\"，Notation Table (Appendix A) 用 $c_{\\text{vote}}$——三个名称指同一个东西。\n  (b) \"confidence signal\" 是 umbrella term (Section 3.2 line 1)，但 Introduction line 1 说 \"Self-consistency...sampling multiple outputs and aggregating them\" 然后用 \"confidence signals\" 包含 logprob 这个非 consistency-based 的信号——读者需要读到 Method 才明白这个术语层次。\n  (c) \"LP\" 在 Table 5 使用，但 Table 1 用 \"Log-prob\"，正文用 \"logprob\"。\n- 建议：统一为一套术语，在第一次出现时明确定义缩写并全文一致使用。\n\n**W4** [warning] RE 结论建立在单一数据集上，但 main text 中的呈现方式容易让读者忽略这一点\n- 具体位置：Table 1 (tab:quality_estimation), Table 2 (tab:selection), Section 4.2\n- 问题：SciERC 是唯一的 RE 数据集，40% 的 instances 有 zero F1，RE 结果在 Table 1 中与 NER 并列呈现但缺少明确的 \"preliminary/single-benchmark\" 标记。虽然 Table 1 caption 说 \"single benchmark—preliminary\"，Table 2 caption 也说 \"RE results are from a single benchmark (preliminary)\"，但 Discussion 和 Conclusion 中 RE 的发现与 NER 一起总结，没有在每次引用 RE 结论时重申 preliminary 性质。\n- 建议：在 Discussion/Conclusion 中每次引用 RE 结论时加 \"(preliminary, single benchmark)\" 后缀，或在 Conclusion 中用独立句子总结 RE 的局限性（当前只有一句 \"RE findings rest on SciERC alone\"）。\n\n**W5** [warning] Qwen3-8B thinking mode 配置不一致\n- 具体位置：Section 7 (Limitations), ¶6; Appendix F ¶3\n- 问题：SciERC 训练时未显式关闭 thinking mode，CoNLL/WNUT 显式关闭了。虽然 constrained decoding 在推理时会覆盖 thinking behavior，但训练时暴露 thinking tokens 可能影响 learned representations——论文自己在 Limitations 中也承认了这一点。这引入了一个潜在的 confound：SciERC 和 CoNLL/WNUT 之间的 signal behavior 差异可能部分来自训练配置不一致而非数据集特性差异。\n- 建议：要么补做实验（统一配置重新训练 SciERC），要么在 Experiments Setup 中 prominently 声明这一 confound（当前只在 Limitations 和 Appendix 的脚注中提及），让 reader 在解读 cross-dataset comparisons 时有充分的背景信息。\n\n**W6** [warning] 缺少与 supervised verifier 的对比\n- 具体位置：Section 5 (Discussion) ¶4; Section 7 (Limitations) ¶3\n- 问题：论文反复建议 \"trained verifiers\" 作为 closing the gap 的方向（Discussion: \"Effective selection likely requires...trained verifiers\"；Conclusion: \"Trained verifiers...are promising directions\"），但没有提供任何 supervised baseline。即使训练一个简单的 linear probe on logprob features 也能量化 supervision 能 recover 多少 oracle headroom，使得 \"trained verifiers needed\" 的结论从猜测变为有证据的 claim。\n- 建议：加入一个简单的 supervised verifier baseline（例如 logistic regression on signal features predicting per-sample F1），哪怕只是 oracle-bound analysis，以量化 unsupervised 和 supervised 之间的 gap。\n\n---\n\n## 小问题（不影响接收）\n\n- Figure 1 caption 重复了正文 Section 4.2 的大部分内容（\"p=0.39 for NER logprob; Table 2\"），caption 应更简洁。\n- Table 1 的 $N{=}16$ 行只有 LLaMA CoNLL 一个配置的数据，且只报告了 $\\rho$ 没有 AUROC——要么删除这一行移到 Appendix，要么补全数据。\n- Section 3.2 ¶3 (FK): \"excess agreement ($\\bar{P} - \\bar{P}_e$) across all configurations...between $-$0.4% and $-$4.0%\" ——负的 excess agreement 意味着 $\\bar{P} < \\bar{P}_e$（observed agreement 低于随机预期），这表示轻微负依赖。论文将此解读为 \"confirms that FK is not inflated by inter-sample dependence\"，这个推理是正确的，但措辞可以更清晰——\"mild negative dependence\" 比 \"sufficient response diversity\" 更准确。\n- Appendix A Notation Table: $c_{\\text{vote}}$ 的 Meaning 列写 \"Entity voting confidence\"，但没有列出 LP/logprob 的 shorthand \"LP\"（Table 5 使用了 LP 缩写）。\n- Ethics Statement 提及 \"CoNLL-2003\" 但该数据集基于 Reuters 新闻语料，其 license 有使用限制（研究目的）——可以在 Ethics Statement 中简要注明。\n\n---\n\n## 引用格式与准确性\n\n引用验证工具结果：60 条 bib entries，91 条引用，0 orphan，0 missing，53 条在线验证通过。\n\n具体问题：\n1. **feng2025optimal**: OpenAlex 显示 first author 为 \"Austin\"（全名 Austin Feng），bib 中 authors 字段写 \"Feng, Austin and Marius, Alonso and...\"——检查是否应为 \"Feng, Austin and Alonso, Marius and Odonnat, Ambroise\"，当前 bib 中 Marius 被放在了 first name 位置。\n2. **ye2025uncertainty**: OpenAlex 显示 first author 可能为 Heo 而非 Ye——需确认正确的 first author。\n3. **hobelsberger2025systematic** 和 **venktesh2025trust**: OpenAlex 未找到，可能是较新的 preprint；建议确认 arXiv ID 正确。\n4. **lightman2024verify**: OpenAlex 未找到（\"Let's Verify Step by Step\"），这是 ICLR 2024 论文，可能是 API 覆盖问题而非引用错误。\n5. **snell2024scaling**: bib 标注为 2024 但 venue 为 \"ICLR 2025\"——key 和 year 应统一为 2025。\n\n---\n\n## 主要优势\n\n1. **统计分析的严谨性**：Bootstrap CI、TOST equivalence testing、multi-seed stability analysis、diversity stratification、conditional filtering——这是我在 IE 领域论文中少见的统计严谨程度，远超大多数只报 point estimates 的工作。\n2. **Logprob 压缩诊断**：Section 5 ¶2 (Layer 2) 和 Appendix G 的 non-tied subset analysis（+2.9pp, p=0.01）是论文最有价值的贡献——它不仅报告了 selection failure，还提供了 actionable 的机制解释（constrained decoding 压缩 logprob resolution）。\n3. **Limitations 的诚实程度**：Section 7 覆盖了 RE 单数据集、模型规模限制、N-scaling 范围、thinking mode confound、logprob temperature gap——这种自我批评的坦诚值得肯定。\n4. **Difficulty gradient 设计**：三个 NER 数据集跨越 easy (CoNLL, 91% F1) → hard (SciERC) → boundary (WNUT-17, 52% zero F1) 的梯度设计合理，WNUT-17 的负面 logprob correlation (ρ=−0.410) 是一个有趣且非显然的发现。\n5. **质量估计与选择的明确区分**：即使 4/5 的 selection failure 是 definitional，将 quality estimation 和 sample selection 作为两个独立评价维度进行系统对比，在 IE 文献中是有价值的框架贡献。",
  "reviewer_id": "2",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 — Round 1 审稿报告\n\n**论文**: Strong Predictors, Weak Selectors: Confidence Signals for Test-Time Scaling in Information Extraction under Constrained Decoding\n**审查侧重**: 新颖性 + 完整性 + 相关工作\n\n---\n\n## 总体评分\n\n**Overall**: 3/5 (Findings track)\n**一句话总结**: 实验设计扎实、统计分析严谨的负面结果论文，对 structured IE 的 test-time scaling 提供了有价值的实证警告，但核心发现的新颖性有限——correlation-selection gap 的 4/5 信号来源于定义层面的不可避免性（instance-level 信号天然无法做 sample selection），真正有趣的 logprob 压缩诊断只占论文的一小部分。\n\n---\n\n## 官方维度打分（来自 ACL ARR review form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | 统计方法严谨（bootstrap, TOST, multi-seed），但 FK 独立性假设仅以经验验证部分回应，consensus-proximity 作为 selection 唯一策略有局限 |\n| Excitement | 2.5/5 | 负面结果对从业者有参考价值，但 gap 的 4/5 来源是定义性的（instance-level 信号不可能做 per-sample selection），最有趣的 logprob 压缩分析篇幅不足 |\n| Reproducibility | 3/5 | Training config、prompt template、超参详尽（Table 7, Appendix F），但未提及代码/数据发布计划 |\n| Reviewer Confidence | 4/5 | 熟悉 self-consistency、MBR decoding、结构化 IE 和不确定性估计文献 |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] Contribution 1 \"systematic multi-family comparison\" 的新颖性与 framing 不匹配\n- 具体位置：Section 1 (Introduction), Contribution (i); Section 2 (Related Work), ¶2\n- 问题：论文将 \"5 signals from 3 families\" 的对比定位为主要贡献，但这本质上是 engineering benchmark——将已知的 confidence signals（logprob, exact match, Fleiss' κ 等）应用于新任务设置。与 Nédellec et al. (2026) 的增量确实存在（结构化匹配、constrained decoding、多数据集），但论文在 Introduction 中没有足够清楚地区分 \"applying known signals to a new setting\" 和 \"discovering new signals or principles\"。\n- 为什么影响接收：如果 reviewer 将这理解为 \"known metrics on new tasks\" 的简单应用研究，会直接影响 novelty 评分。\n- 建议修改方向：在 Introduction 中更明确地说明，核心贡献不是比较本身，而是 (a) 发现质量估计与选择之间的 gap，(b) logprob 压缩的机制诊断。将 Contribution 1 降级为 setup/methodology，将 Contribution 2 (gap) 提升为核心 claim。\n\n**N2** [critical] Correlation-selection gap 的 4/5 来源是定义性的，非实证发现\n- 具体位置：Section 1 (Introduction), ¶5; Section 5 (Discussion), ¶2 \"Layer 1 (definitional)\"\n- 问题：论文在 Discussion 中自己承认 4/5 信号的 selection failure 是 \"by construction\"（Layer 1），因为 instance-level 信号天然给所有候选样本相同分数。这不是一个需要通过实验才能发现的 gap——这是信号定义的直接推论。论文的真正实证贡献是 Layer 2（logprob 在 constrained decoding 下的压缩），但这在当前 framing 中被埋在了 \"gap\" 这个更大叙事之下。\n- 为什么影响接收：将定义性结论包装为实证发现会降低论文的可信度。一个熟悉这些信号的 reviewer 会立即意识到 instance-level 信号不能做 per-sample selection，这不需要实验验证。\n- 建议修改方向：(1) 在 Introduction 中提前透明化 Layer 1 是 definitional，而非卖悬念；(2) 将叙事重心转向 Layer 2——logprob（唯一的 per-sample signal）为何也失败，constrained decoding 压缩的机制及其条件性缓解（+2.9pp, p=0.01）才是论文最有价值的贡献。\n\n**N3** [critical] Related Work 遗漏关键引用\n- 具体位置：Section 2 (Related Work)\n- 问题：\n  (a) **Zhang et al. (2025) \"A Survey on Test-Time Scaling in Large Language Models: What, How, Where, and How Well?\" (arXiv:2503.24235)**——目前最全面的 test-time scaling survey，提出了系统性的 TTS 分类框架（what/how/where/how well to scale），论文引用了 Snell 和 Brown 的个别工作但遗漏了这个综述，考虑到论文标题包含 \"Test-Time Scaling\" 这个关键词，这是显著的遗漏。\n  (b) **Eikema, Rutkiewicz & Giulianelli (EMNLP 2025) \"Structure-Conditional Minimum Bayes Risk Decoding\"**——直接研究 MBR decoding 在结构化输出上的问题，发现 common utility functions 在结构化场景（dialogue, instruction-following）下表现不佳，与本文 Section 5 ¶3 的 MBR 失败发现高度相关。\n- 为什么影响接收：Related Work 完整性是 EMNLP Findings 的基本要求；遗漏了同一 venue (EMNLP 2025) 的直接相关工作会被 reviewer 视为文献调研不充分。\n- 建议修改方向：在 Section 2 ¶1 补充 Zhang et al. survey 作为 test-time scaling 的综述引用；在 ¶3 (uncertainty/MBR) 补充 Eikema et al. (2025) 并讨论其 utility function 对结构化输出不适用的发现如何与本文的 MBR failure 互相印证。\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] \"cross-model\" 措辞过度外推\n- 具体位置：Section 1 (Introduction), Contribution (iii) \"consistent ordering across models\"；Section 4.1 \"cross-model stability is strong\"\n- 问题：实际只测试了 2 个同规模 (8B) 模型。\"cross-model\" 的说法暗示了比实际更广的泛化性。Limitations 中承认了 70B+/closed-source 未测试，但 main text 的措辞没有同步限定。\n- 建议：将 main text 中的 \"cross-model\" 改为 \"cross-architecture\" 或 \"across two model families (at 8B scale)\"，使措辞与实际实验范围匹配。\n\n**W2** [warning] Abstract 信息密度过高\n- 具体位置：sections/abstract.tex\n- 问题：9 行 abstract 包含：5 个信号名、3 个信号家族名、4 个数字 (ρ=0.38, AUROC=0.75, p>0.39, +2.9pp)、3 个数据集（隐含在 \"three datasets\"）、2 个任务、2 个模型（隐含在 \"two 8B-parameter model families\"）、plus \"correlation-selection gap\" 这个新术语的引入。对于不熟悉该领域的 reviewer，首次阅读时信息过载。\n- 建议：减少具体数字，将 signal family 名称移到正文；abstract 聚焦于问题-发现-意义三段式。\n\n**W3** [warning] 术语一致性问题\n- 具体位置：全文多处\n- 问题：\n  (a) \"VC\" 在 Table 1 和正文中用，但 Method Section 定义为 \"entity voting confidence\"，Notation Table (Appendix A) 用 $c_{\\text{vote}}$——三个名称指同一个东西。\n  (b) \"confidence signal\" 是 umbrella term (Section 3.2 line 1)，但 Introduction line 1 说 \"Self-consistency...sampling multiple outputs and aggregating them\" 然后用 \"confidence signals\" 包含 logprob 这个非 consistency-based 的信号——读者需要读到 Method 才明白这个术语层次。\n  (c) \"LP\" 在 Table 5 使用，但 Table 1 用 \"Log-prob\"，正文用 \"logprob\"。\n- 建议：统一为一套术语，在第一次出现时明确定义缩写并全文一致使用。\n\n**W4** [warning] RE 结论建立在单一数据集上，但 main text 中的呈现方式容易让读者忽略这一点\n- 具体位置：Table 1 (tab:quality_estimation), Table 2 (tab:selection), Section 4.2\n- 问题：SciERC 是唯一的 RE 数据集，40% 的 instances 有 zero F1，RE 结果在 Table 1 中与 NER 并列呈现但缺少明确的 \"preliminary/single-benchmark\" 标记。虽然 Table 1 caption 说 \"single benchmark—preliminary\"，Table 2 caption 也说 \"RE results are from a single benchmark (preliminary)\"，但 Discussion 和 Conclusion 中 RE 的发现与 NER 一起总结，没有在每次引用 RE 结论时重申 preliminary 性质。\n- 建议：在 Discussion/Conclusion 中每次引用 RE 结论时加 \"(preliminary, single benchmark)\" 后缀，或在 Conclusion 中用独立句子总结 RE 的局限性（当前只有一句 \"RE findings rest on SciERC alone\"）。\n\n**W5** [warning] Qwen3-8B thinking mode 配置不一致\n- 具体位置：Section 7 (Limitations), ¶6; Appendix F ¶3\n- 问题：SciERC 训练时未显式关闭 thinking mode，CoNLL/WNUT 显式关闭了。虽然 constrained decoding 在推理时会覆盖 thinking behavior，但训练时暴露 thinking tokens 可能影响 learned representations——论文自己在 Limitations 中也承认了这一点。这引入了一个潜在的 confound：SciERC 和 CoNLL/WNUT 之间的 signal behavior 差异可能部分来自训练配置不一致而非数据集特性差异。\n- 建议：要么补做实验（统一配置重新训练 SciERC），要么在 Experiments Setup 中 prominently 声明这一 confound（当前只在 Limitations 和 Appendix 的脚注中提及），让 reader 在解读 cross-dataset comparisons 时有充分的背景信息。\n\n**W6** [warning] 缺少与 supervised verifier 的对比\n- 具体位置：Section 5 (Discussion) ¶4; Section 7 (Limitations) ¶3\n- 问题：论文反复建议 \"trained verifiers\" 作为 closing the gap 的方向（Discussion: \"Effective selection likely requires...trained verifiers\"；Conclusion: \"Trained verifiers...are promising directions\"），但没有提供任何 supervised baseline。即使训练一个简单的 linear probe on logprob features 也能量化 supervision 能 recover 多少 oracle headroom，使得 \"trained verifiers needed\" 的结论从猜测变为有证据的 claim。\n- 建议：加入一个简单的 supervised verifier baseline（例如 logistic regression on signal features predicting per-sample F1），哪怕只是 oracle-bound analysis，以量化 unsupervised 和 supervised 之间的 gap。\n\n---\n\n## 小问题（不影响接收）\n\n- Figure 1 caption 重复了正文 Section 4.2 的大部分内容（\"p=0.39 for NER logprob; Table 2\"），caption 应更简洁。\n- Table 1 的 $N{=}16$ 行只有 LLaMA CoNLL 一个配置的数据，且只报告了 $\\rho$ 没有 AUROC——要么删除这一行移到 Appendix，要么补全数据。\n- Section 3.2 ¶3 (FK): \"excess agreement ($\\bar{P} - \\bar{P}_e$) across all configurations...between $-$0.4% and $-$4.0%\" ——负的 excess agreement 意味着 $\\bar{P} < \\bar{P}_e$（observed agreement 低于随机预期），这表示轻微负依赖。论文将此解读为 \"confirms that FK is not inflated by inter-sample dependence\"，这个推理是正确的，但措辞可以更清晰——\"mild negative dependence\" 比 \"sufficient response diversity\" 更准确。\n- Appendix A Notation Table: $c_{\\text{vote}}$ 的 Meaning 列写 \"Entity voting confidence\"，但没有列出 LP/logprob 的 shorthand \"LP\"（Table 5 使用了 LP 缩写）。\n- Ethics Statement 提及 \"CoNLL-2003\" 但该数据集基于 Reuters 新闻语料，其 license 有使用限制（研究目的）——可以在 Ethics Statement 中简要注明。\n\n---\n\n## 引用格式与准确性\n\n引用验证工具结果：60 条 bib entries，91 条引用，0 orphan，0 missing，53 条在线验证通过。\n\n具体问题：\n1. **feng2025optimal**: OpenAlex 显示 first author 为 \"Austin\"（全名 Austin Feng），bib 中 authors 字段写 \"Feng, Austin and Marius, Alonso and...\"——检查是否应为 \"Feng, Austin and Alonso, Marius and Odonnat, Ambroise\"，当前 bib 中 Marius 被放在了 first name 位置。\n2. **ye2025uncertainty**: OpenAlex 显示 first author 可能为 Heo 而非 Ye——需确认正确的 first author。\n3. **hobelsberger2025systematic** 和 **venktesh2025trust**: OpenAlex 未找到，可能是较新的 preprint；建议确认 arXiv ID 正确。\n4. **lightman2024verify**: OpenAlex 未找到（\"Let's Verify Step by Step\"），这是 ICLR 2024 论文，可能是 API 覆盖问题而非引用错误。\n5. **snell2024scaling**: bib 标注为 2024 但 venue 为 \"ICLR 2025\"——key 和 year 应统一为 2025。\n\n---\n\n## 主要优势\n\n1. **统计分析的严谨性**：Bootstrap CI、TOST equivalence testing、multi-seed stability analysis、diversity stratification、conditional filtering——这是我在 IE 领域论文中少见的统计严谨程度，远超大多数只报 point estimates 的工作。\n2. **Logprob 压缩诊断**：Section 5 ¶2 (Layer 2) 和 Appendix G 的 non-tied subset analysis（+2.9pp, p=0.01）是论文最有价值的贡献——它不仅报告了 selection failure，还提供了 actionable 的机制解释（constrained decoding 压缩 logprob resolution）。\n3. **Limitations 的诚实程度**：Section 7 覆盖了 RE 单数据集、模型规模限制、N-scaling 范围、thinking mode confound、logprob temperature gap——这种自我批评的坦诚值得肯定。\n4. **Difficulty gradient 设计**：三个 NER 数据集跨越 easy (CoNLL, 91% F1) → hard (SciERC) → boundary (WNUT-17, 52% zero F1) 的梯度设计合理，WNUT-17 的负面 logprob correlation (ρ=−0.410) 是一个有趣且非显然的发现。\n5. **质量估计与选择的明确区分**：即使 4/5 的 selection failure 是 definitional，将 quality estimation 和 sample selection 作为两个独立评价维度进行系统对比，在 IE 文献中是有价值的框架贡献。",
    "reviewer_id": "2",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 491 · 2026-05-15T08:51:17.069836+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4267
}
```

</details>

---


### Assistant

_source line 492 · 2026-05-15T08:51:25.826232+00:00_

审稿报告已提交给 Review Director。

核心判断：**Overall 3/5，适合 Findings track**。

3 个 Must-Fix：
- **N1**: Contribution 1（multi-family comparison）本质是 benchmark 应用研究，framing 应将 logprob 压缩诊断提升为核心贡献
- **N2**: Correlation-selection gap 的 4/5 来源是 instance-level 信号的定义性质而非实证发现，当前 framing 掩盖了这一点
- **N3**: 遗漏 Zhang et al. (2025) test-time scaling 综述和 Eikema et al. (EMNLP 2025) Structure-Conditional MBR——均为高度相关的近期工作

6 个 Should-Fix 涵盖 cross-model 过度外推、abstract 信息过载、术语不一致、RE 单数据集标注不足、Qwen3 thinking mode confound、缺少 supervised verifier baseline。引用验证发现 5 处 bib 条目需修正。

主要优势：统计分析严谨度远超同类工作，logprob 压缩诊断有 actionable 价值，Limitations 坦诚。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2"
}
```

</details>

---


## Round 15

## Round 15

4 recorded events


### User

_source line 493 · 2026-05-15T08:52:49.853504+00:00_

[Round 1 审稿请求]:
## 交叉分享 — Reviewer 1 的完整审稿意见

请逐条回应以下 Reviewer 1 的审稿意见。对每条使用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

以下是 Reviewer 1 的完整审稿原文：

## Reviewer 1 — Round 1 审稿报告

**总体评分**: 3.0/5（Findings acceptance）

### Must-Fix 问题

**N1** [critical] **缺少 free-form decoding 对照实验——核心发现可能是 constrained decoding artifact**
- 具体位置：Section 5 (Discussion), Limitations
- 问题：论文的核心概念 "correlation-selection gap" 被呈现为 structured IE 的重要发现，但 non-tied subset analysis（Section 5）已经证明：当 score compression 被缓解时（logprob range ≥ 0.05 的 40% instances），logprob 成为显著 selector（+2.9pp, p=0.01, within-instance ρ: 0.08→0.39）。这直接暗示 gap 主要源于 constrained decoding 的技术限制，而非 structured IE 的固有属性。缺少 free-form decoding（不使用 grammar constraint）的对照实验，无法区分这两种解释。
- 为什么影响接收：如果 gap 仅存在于 constrained decoding 下（且已可追溯到 score compression），贡献从 "发现 structured IE 的基本现象" 降级为 "记录 constrained decoding 的一个副作用"。
- 建议修改方向：(1) 在可解析子集上报告 free-form selection F1 作为参照；(2) 至少在 SciERC 上运行 free-form + post-hoc parsing 的对照；(3) 或更明确地将 claim scope 限定为 "constrained decoding 下的 selection 瓶颈 = score compression"。

**N2** [critical] **TOST 等价检验的 δ 选择缺乏直接理据**
- 具体位置：Appendix F (Table 4), Section 4.3
- 问题：δ 取值 ±2pp, ±3pp, ±5pp 的唯一理由是 IAA 变异，但 IAA 变异反映标注噪声，与 "一个好的 selector 应该带来多少增益" 是不同概念。Oracle headroom = 13-18pp，δ=5pp 意味着放弃 38% 的可能增益——这算"等价"吗？
- 建议：用 SESOI 框架或报告 breakpoint analysis。

### Should-Fix 问题

**W1** [warning] **Qwen3 thinking token 训练不一致的影响被低估**
- SciERC 训练未禁用 enable_thinking，而 CoNLL/WNUT 禁用了。训练时 thinking tokens 可能影响 learned representations 和 logprob 分布。SciERC 是 selection analysis 的主要数据集。

**W2** [warning] **RE 证据强度不足以支撑多处主体论述中的 RE claims**
- RE 基于单数据集（238 个 non-zero F1 instances），per-relation 变异极大。建议将 RE 更多移入 Appendix。

**W3** [warning] **VC 定义：公式与实现不一致**
- Equation 6 无阈值，但 footnote 2 承认实现使用 majority threshold (>N/2)。两者数学上不等价，影响可复现性。

**W4** [warning] **Instance-level 信号无法 select 的论证部分 tautological**
- 4/5 信号不能 select 在定义上成立，不算 empirical finding。真正的 finding 是 consensus-proximity 和 logprob 也失败。Abstract/Introduction 的 "four of five signals fail" 表述模糊了这一点。

### 小问题
- ye2025uncertainty 作者信息需核实
- Table 1 布局密集，建议拆分
- Semantic entropy 脚注价值有限
- FK excess agreement 未做显著性检验
- N=8 primary results 使用单一 seed=42，与 σ 在同一数量级

### 主要优势
1. Quality estimation vs. sample selection 区分有价值
2. 统计实践远超同类论文
3. 诚实的局限性讨论
4. Mechanistic diagnosis（non-tied subset）有说服力
5. Difficulty-dependent signal ranking 实用
6. Cross-model consistency 增强可信度

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 494 · 2026-05-15T08:54:19.391395+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 — 交叉回应 Reviewer 1 审稿意见\n\n---\n\n### Must-Fix 问题\n\n**[REBUT] R1-N1: 缺少 free-form decoding 对照实验**\n\nR1 的论点是 correlation-selection gap 可能主要是 constrained decoding artifact。这个关切部分成立但程度被高估了，理由如下：\n\n1. **Gap 的 Layer 1 与 constrained decoding 无关。** 论文在 Section 5 ¶2 明确区分了两个层次：Layer 1 是 definitional——4/5 信号是 instance-level aggregates，无论有无 constrained decoding 都无法做 per-sample selection。Free-form decoding 不会改变这一事实。R1 的论点仅适用于 Layer 2（logprob 压缩），但论文的 gap 概念包含两个层次。\n\n2. **Free-form decoding 对 structured IE 的实用性存疑。** Section 1 (Introduction, line 19) 指出 \"without it [constrained decoding], a substantial fraction of outputs are unparseable\"。如果 free-form 下大量输出不可解析，那么在可解析子集上的 selection 结果会有严重的 selection bias——只有模型最确信的 outputs 才能通过格式过滤，这本身就会压缩 per-sample 变异。R1 建议的 \"free-form + post-hoc parsing 对照\" 需要处理不可解析样本（丢弃？赋零分？），每种处理方式都引入新的 confound。\n\n3. **但 R1 的核心建议有道理：claim scope 应更明确。** 论文标题已包含 \"under Constrained Decoding\"，但 Introduction 和 Discussion 中部分措辞确实暗示 gap 是 structured IE 的固有属性而非特定推理 regime 下的现象。建议作者在 Section 5 ¶2 末尾增加一句明确声明：\"The extent to which the correlation-selection gap persists under free-form generation remains an open question; our findings are specific to the constrained decoding regime standard for schema-compliant IE.\"\n\n**综合判断：** R1 将此列为 must-fix 我认为过重。论文标题和多处表述已明确限定在 constrained decoding 下，且 Layer 1 的 definitional gap 不受 decoding 策略影响。但 claim scope 的收紧（R1 建议 (3)）是合理的 should-fix。\n\n---\n\n**[AGREE] R1-N2: TOST δ 选择缺乏直接理据**\n\n同意 R1 的分析。Appendix F (Table 4) 用 IAA 变异（3–5pp annotation-induced variation）来论证 δ 的合理性，但 IAA 测量的是标注噪声天花板，而 TOST 检验的是 \"selector 与 greedy 是否实质等价\"——两者概念不同。\n\n补充 R1 未提到的一个问题：Oracle headroom 在 NER 为 13.2pp、RE 为 18.1pp（Table 2），δ=5pp 意味着即使 selector 只 recover 了 oracle headroom 的 28%（NER）或 28%（RE），也会被判定为\"不等价\"而被拒绝。这个门槛看起来合理。但 δ=2pp 时，只需 recover 15% 的 headroom 就算\"显著\"——在 N=8 的 bootstrap 方差下，这个精度可能不够。\n\n建议作者：(1) 报告 breakpoint δ*（使结论翻转的最小 δ），给读者完整信息；(2) 直接报告 effect size (Cohen's d) 和 bootstrap CI（当前已在 Section 4.2 ¶2 报告了 NER logprob 的 d=0.038 和 CI [−3.0, +4.2]pp），这些比 TOST 更直观。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R1-W1: Qwen3 thinking token 训练不一致**\n\n完全同意，我在 R2-W5 中提出了相同问题。SciERC 是 selection analysis 的主要数据集，thinking token 训练不一致可能影响 logprob 分布，而 logprob 压缩诊断是论文的核心机制分析。补充一点：如果 thinking tokens 在训练时改变了 Qwen3 在 SciERC 上的 logprob scale，那么 Section 5 中 \"60% of instances effectively tied\" 的数字可能在 thinking-disabled 训练下不同——这会直接动摇 Layer 2 诊断的可靠性。\n\n---\n\n**[AGREE] R1-W2: RE 证据强度不足**\n\n同意，我在 R2-W4 中也提出了类似关切。238 个 non-zero F1 instances 用于 RE conditional analysis（Appendix H, Table 6），per-relation 变异极大（Feature-Of ρ=0.004 vs. Hyponym-Of ρ=0.646，Appendix D ¶1）——这种量级的变异使得 aggregate RE 结论的信息量有限。建议至少将 RE selection results（Table 2 RE column, Table 6）标记为 exploratory，或在 Discussion 中每次引用 RE 结论时加 \"(exploratory, n=238)\" 后缀。\n\n---\n\n**[AGREE] R1-W3: VC 定义与实现不一致**\n\n好的 catch，我审稿时未注意到这个细节。Equation 6 定义 $c_{\\text{vote}}(x) = \\frac{1}{|E_\\cup|} \\sum_{e \\in E_\\cup} \\text{freq}(e)$——这是所有 entity 的平均频率，没有阈值。但 Footnote 2（Section 3.2, method.tex line 62）说 \"Our implementation computes the mean entity-level match rate against a majority threshold (>N/2)\"——这意味着实现时只统计 freq(e) > 0.5 的 entity 的 match rate，与公式的 \"average over ALL entities in E_∪\" 不等价。\n\n具体差异：如果某 entity 只在 2/8 sample 中出现（freq=0.25），Eq.6 会将其 0.25 纳入平均，但 thresholded 实现可能会忽略它或给它 0 分。这会系统性地影响 low-agreement entities 的贡献，可能改变 VC 与其他信号的相对排名——尤其是在 SciERC 这种 entity 集合大、低频 entity 多的数据集上。\n\nFootnote 2 最后说 \"yields slightly different absolute values but identical qualitative conclusions\"——但没有提供 quantitative 比较（例如两种实现的 ρ 差值）。建议作者：(1) 报告两种实现的 ρ 对比，(2) 明确 Table 1 中报告的是哪种实现的结果。\n\n---\n\n**[AGREE] R1-W4: Instance-level 信号的 selection failure 部分 tautological**\n\n强烈同意，这与我在 R2-N2 中的核心关切一致。Instance-level 信号给同一 input 的所有 N 个 sample 相同的分数——它们不能做 per-sample selection 是 **定义的直接推论**，不是需要实验验证的发现。\n\n论文的真正 empirical findings 是：\n1. Consensus-proximity selection（Section 3.3, method.tex line 71）——将 instance-level SJ 转化为 per-sample 排名——也失败了（Table 2: SJ selection 0.645 vs greedy 0.644）\n2. Logprob（唯一 per-sample signal）也失败了（p=0.39）\n3. Logprob 失败的机制是 constrained decoding 下的 score compression（Appendix G）\n\n当前 Abstract（\"four of five signals are instance-level by construction\"）和 Introduction（Section 1, ¶5 \"Four of five signals are instance-level by construction; log-probability...also fails\"）的表述方式将 definitional fact 和 empirical finding 混在一起呈现。建议作者重构叙事：先一句话 dismiss instance-level 信号的 selection potential（\"by definition, not empirically\"），然后集中论证 consensus-proximity 和 logprob 为何失败——这才是需要实验证据的部分。\n\n---\n\n### 小问题\n\n**[AGREE] R1-小问题-1: ye2025uncertainty 作者**\n同意，我也在引用审计中标记了此条。OpenAlex 显示 first author 可能为 Heo 而非 Ye。\n\n**[AGREE] R1-小问题-2: Table 1 布局**\n同意密度过高。N=16 行只有 LLaMA CoNLL 的数据，与上方 N=8 的完整矩阵形成不对称——要么补全 N=16 数据，要么移到 Appendix。\n\n**[REBUT] R1-小问题-3: Semantic entropy 脚注价值有限**\n部分不同意。Section 4.1 脚注（experiments.tex line 64）将 AUROC 0.749 与 semantic entropy 做 scale context 比较，并明确说 \"direct comparison is not meaningful due to fundamentally different output spaces\"。这种 calibrated comparison 对不熟悉该领域的 reviewer 有帮助——它提供了 AUROC 0.75 在 LLM confidence 文献中的大致位置，同时避免了不当的跨任务 claim。脚注是合适的呈现方式（不在正文中突出）。\n\n**[AGREE] R1-小问题-4: FK excess agreement 未做显著性检验**\n合理关切。Section 3.2（method.tex line 40）报告 excess agreement 在 −0.4% 到 −4.0% 之间，但没有 CI 或 p-value。对于一个关键假设（FK 不被 inter-sample dependence inflate）的验证，应该提供 permutation test 或 bootstrap CI。\n\n**[AGREE] R1-小问题-5: N=8 primary results 单一 seed**\n合理关切。Table 1 的 N=8 主结果用 seed=42，Appendix E (Table 5) 的 3-seed analysis 显示 σ≤0.025——与部分信号间差异在同一量级（例如 SJ−FK gap = 0.093 on SciERC NER，大于 σ 但 VC−SJ gap = 0.019 远小于 σ）。建议至少在 main text 中注明 single-seed limitation 并引用 Appendix 的 stability analysis，当前 Table 1 caption 只说 \"seed=42\" 没有引导读者去查看 multi-seed 结果。\n\n---\n\n### 总结\n\n与 R1 的评估高度一致。主要分歧在 N1（free-form 对照）的严重程度：我认为 Layer 1 (definitional) 不受 decoding 策略影响，因此 gap 不完全是 constrained decoding artifact；但同意 Layer 2 的 scope 应更明确限定。R1 和 R2 共同识别的核心问题是 **叙事结构**——论文将 definitional facts（instance-level 信号不能 select）与 empirical findings（consensus-proximity 和 logprob 也失败）混合呈现，降低了真正贡献（logprob 压缩诊断）的 visibility。",
  "reviewer_id": "2",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 — 交叉回应 Reviewer 1 审稿意见\n\n---\n\n### Must-Fix 问题\n\n**[REBUT] R1-N1: 缺少 free-form decoding 对照实验**\n\nR1 的论点是 correlation-selection gap 可能主要是 constrained decoding artifact。这个关切部分成立但程度被高估了，理由如下：\n\n1. **Gap 的 Layer 1 与 constrained decoding 无关。** 论文在 Section 5 ¶2 明确区分了两个层次：Layer 1 是 definitional——4/5 信号是 instance-level aggregates，无论有无 constrained decoding 都无法做 per-sample selection。Free-form decoding 不会改变这一事实。R1 的论点仅适用于 Layer 2（logprob 压缩），但论文的 gap 概念包含两个层次。\n\n2. **Free-form decoding 对 structured IE 的实用性存疑。** Section 1 (Introduction, line 19) 指出 \"without it [constrained decoding], a substantial fraction of outputs are unparseable\"。如果 free-form 下大量输出不可解析，那么在可解析子集上的 selection 结果会有严重的 selection bias——只有模型最确信的 outputs 才能通过格式过滤，这本身就会压缩 per-sample 变异。R1 建议的 \"free-form + post-hoc parsing 对照\" 需要处理不可解析样本（丢弃？赋零分？），每种处理方式都引入新的 confound。\n\n3. **但 R1 的核心建议有道理：claim scope 应更明确。** 论文标题已包含 \"under Constrained Decoding\"，但 Introduction 和 Discussion 中部分措辞确实暗示 gap 是 structured IE 的固有属性而非特定推理 regime 下的现象。建议作者在 Section 5 ¶2 末尾增加一句明确声明：\"The extent to which the correlation-selection gap persists under free-form generation remains an open question; our findings are specific to the constrained decoding regime standard for schema-compliant IE.\"\n\n**综合判断：** R1 将此列为 must-fix 我认为过重。论文标题和多处表述已明确限定在 constrained decoding 下，且 Layer 1 的 definitional gap 不受 decoding 策略影响。但 claim scope 的收紧（R1 建议 (3)）是合理的 should-fix。\n\n---\n\n**[AGREE] R1-N2: TOST δ 选择缺乏直接理据**\n\n同意 R1 的分析。Appendix F (Table 4) 用 IAA 变异（3–5pp annotation-induced variation）来论证 δ 的合理性，但 IAA 测量的是标注噪声天花板，而 TOST 检验的是 \"selector 与 greedy 是否实质等价\"——两者概念不同。\n\n补充 R1 未提到的一个问题：Oracle headroom 在 NER 为 13.2pp、RE 为 18.1pp（Table 2），δ=5pp 意味着即使 selector 只 recover 了 oracle headroom 的 28%（NER）或 28%（RE），也会被判定为\"不等价\"而被拒绝。这个门槛看起来合理。但 δ=2pp 时，只需 recover 15% 的 headroom 就算\"显著\"——在 N=8 的 bootstrap 方差下，这个精度可能不够。\n\n建议作者：(1) 报告 breakpoint δ*（使结论翻转的最小 δ），给读者完整信息；(2) 直接报告 effect size (Cohen's d) 和 bootstrap CI（当前已在 Section 4.2 ¶2 报告了 NER logprob 的 d=0.038 和 CI [−3.0, +4.2]pp），这些比 TOST 更直观。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R1-W1: Qwen3 thinking token 训练不一致**\n\n完全同意，我在 R2-W5 中提出了相同问题。SciERC 是 selection analysis 的主要数据集，thinking token 训练不一致可能影响 logprob 分布，而 logprob 压缩诊断是论文的核心机制分析。补充一点：如果 thinking tokens 在训练时改变了 Qwen3 在 SciERC 上的 logprob scale，那么 Section 5 中 \"60% of instances effectively tied\" 的数字可能在 thinking-disabled 训练下不同——这会直接动摇 Layer 2 诊断的可靠性。\n\n---\n\n**[AGREE] R1-W2: RE 证据强度不足**\n\n同意，我在 R2-W4 中也提出了类似关切。238 个 non-zero F1 instances 用于 RE conditional analysis（Appendix H, Table 6），per-relation 变异极大（Feature-Of ρ=0.004 vs. Hyponym-Of ρ=0.646，Appendix D ¶1）——这种量级的变异使得 aggregate RE 结论的信息量有限。建议至少将 RE selection results（Table 2 RE column, Table 6）标记为 exploratory，或在 Discussion 中每次引用 RE 结论时加 \"(exploratory, n=238)\" 后缀。\n\n---\n\n**[AGREE] R1-W3: VC 定义与实现不一致**\n\n好的 catch，我审稿时未注意到这个细节。Equation 6 定义 $c_{\\text{vote}}(x) = \\frac{1}{|E_\\cup|} \\sum_{e \\in E_\\cup} \\text{freq}(e)$——这是所有 entity 的平均频率，没有阈值。但 Footnote 2（Section 3.2, method.tex line 62）说 \"Our implementation computes the mean entity-level match rate against a majority threshold (>N/2)\"——这意味着实现时只统计 freq(e) > 0.5 的 entity 的 match rate，与公式的 \"average over ALL entities in E_∪\" 不等价。\n\n具体差异：如果某 entity 只在 2/8 sample 中出现（freq=0.25），Eq.6 会将其 0.25 纳入平均，但 thresholded 实现可能会忽略它或给它 0 分。这会系统性地影响 low-agreement entities 的贡献，可能改变 VC 与其他信号的相对排名——尤其是在 SciERC 这种 entity 集合大、低频 entity 多的数据集上。\n\nFootnote 2 最后说 \"yields slightly different absolute values but identical qualitative conclusions\"——但没有提供 quantitative 比较（例如两种实现的 ρ 差值）。建议作者：(1) 报告两种实现的 ρ 对比，(2) 明确 Table 1 中报告的是哪种实现的结果。\n\n---\n\n**[AGREE] R1-W4: Instance-level 信号的 selection failure 部分 tautological**\n\n强烈同意，这与我在 R2-N2 中的核心关切一致。Instance-level 信号给同一 input 的所有 N 个 sample 相同的分数——它们不能做 per-sample selection 是 **定义的直接推论**，不是需要实验验证的发现。\n\n论文的真正 empirical findings 是：\n1. Consensus-proximity selection（Section 3.3, method.tex line 71）——将 instance-level SJ 转化为 per-sample 排名——也失败了（Table 2: SJ selection 0.645 vs greedy 0.644）\n2. Logprob（唯一 per-sample signal）也失败了（p=0.39）\n3. Logprob 失败的机制是 constrained decoding 下的 score compression（Appendix G）\n\n当前 Abstract（\"four of five signals are instance-level by construction\"）和 Introduction（Section 1, ¶5 \"Four of five signals are instance-level by construction; log-probability...also fails\"）的表述方式将 definitional fact 和 empirical finding 混在一起呈现。建议作者重构叙事：先一句话 dismiss instance-level 信号的 selection potential（\"by definition, not empirically\"），然后集中论证 consensus-proximity 和 logprob 为何失败——这才是需要实验证据的部分。\n\n---\n\n### 小问题\n\n**[AGREE] R1-小问题-1: ye2025uncertainty 作者**\n同意，我也在引用审计中标记了此条。OpenAlex 显示 first author 可能为 Heo 而非 Ye。\n\n**[AGREE] R1-小问题-2: Table 1 布局**\n同意密度过高。N=16 行只有 LLaMA CoNLL 的数据，与上方 N=8 的完整矩阵形成不对称——要么补全 N=16 数据，要么移到 Appendix。\n\n**[REBUT] R1-小问题-3: Semantic entropy 脚注价值有限**\n部分不同意。Section 4.1 脚注（experiments.tex line 64）将 AUROC 0.749 与 semantic entropy 做 scale context 比较，并明确说 \"direct comparison is not meaningful due to fundamentally different output spaces\"。这种 calibrated comparison 对不熟悉该领域的 reviewer 有帮助——它提供了 AUROC 0.75 在 LLM confidence 文献中的大致位置，同时避免了不当的跨任务 claim。脚注是合适的呈现方式（不在正文中突出）。\n\n**[AGREE] R1-小问题-4: FK excess agreement 未做显著性检验**\n合理关切。Section 3.2（method.tex line 40）报告 excess agreement 在 −0.4% 到 −4.0% 之间，但没有 CI 或 p-value。对于一个关键假设（FK 不被 inter-sample dependence inflate）的验证，应该提供 permutation test 或 bootstrap CI。\n\n**[AGREE] R1-小问题-5: N=8 primary results 单一 seed**\n合理关切。Table 1 的 N=8 主结果用 seed=42，Appendix E (Table 5) 的 3-seed analysis 显示 σ≤0.025——与部分信号间差异在同一量级（例如 SJ−FK gap = 0.093 on SciERC NER，大于 σ 但 VC−SJ gap = 0.019 远小于 σ）。建议至少在 main text 中注明 single-seed limitation 并引用 Appendix 的 stability analysis，当前 Table 1 caption 只说 \"seed=42\" 没有引导读者去查看 multi-seed 结果。\n\n---\n\n### 总结\n\n与 R1 的评估高度一致。主要分歧在 N1（free-form 对照）的严重程度：我认为 Layer 1 (definitional) 不受 decoding 策略影响，因此 gap 不完全是 constrained decoding artifact；但同意 Layer 2 的 scope 应更明确限定。R1 和 R2 共同识别的核心问题是 **叙事结构**——论文将 definitional facts（instance-level 信号不能 select）与 empirical findings（consensus-proximity 和 logprob 也失败）混合呈现，降低了真正贡献（logprob 压缩诊断）的 visibility。",
    "reviewer_id": "2",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 495 · 2026-05-15T08:54:23.776309+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_3897c2857f11615119e277e820eae311:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4384
}
```

</details>

---


### Assistant

_source line 496 · 2026-05-15T08:54:28.941590+00:00_

交叉回应已提交。与 R1 在大部分问题上达成一致，主要分歧在 N1（free-form 对照实验）——我认为 R1 将其列为 must-fix 过重，因为 Layer 1 的 definitional gap 不受 decoding 策略影响，但同意 Layer 2 的 claim scope 应收紧。两位 reviewer 共同识别的核心问题是叙事结构：definitional facts 与 empirical findings 的混合呈现削弱了 logprob 压缩诊断这一真正贡献的 visibility。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2"
}
```

</details>

---


## Round 16

## Round 16

70 recorded events


### User

_source line 497 · 2026-05-15T12:15:08.435184+00:00_

[Round 1 审稿请求]:
你是 Reviewer 2，负责 **新颖性 + 完整性 + 写作质量** 的审查。

## 论文信息
- **标题**: Strong Predictors, Weak Selectors: Why Confidence Signals Do Not Scale Structured Information Extraction
- **论文路径**: `projects/struct_self_consist_ie/docs/paper/main.tex`（含 sections/ 子目录各章节）
- **目标 Venue**: EMNLP 2026 Main Conference
- **Track**: Main Conference (Long Paper)
- **Deadline**: 2026-05-25 (ARR May 2026 cycle)

## Venue 格式要求
- ACL 模板，8 页正文 + 引用不限 + 附录
- Double-blind（匿名审稿）
- Limitations section 必需
- 提交时必须选择 EMNLP（绑定选择）

## 你的审查侧重

### 1. 新颖性与贡献定位
- 论文的三个 contributions 是否清晰、non-trivial
- Contribution 1（evaluation framework）：是否本质是 engineering benchmark 而非 methodological contribution？是否应降级？
- Contribution 2（correlation-selection gap）：4/5 instance-level signals 无法 rank candidates 是 by construction——论文是否充分区分了 definitional limitation 和 empirical finding？
- Contribution 3（task-complexity boundary）：是否充分展示了 non-obvious findings（WNUT-17 conditional collapse, LP negative correlation）？
- 与 Nédellec et al. (2026) 的增量贡献是否充分量化？三个增量方向是否偏弱？
- SJ（Soft Jaccard）方法论本身是否过度宣传？是否只是标准技术组合？

### 2. Related Work 完整性
- 是否遗漏重要相关工作（test-time scaling surveys, MBR in non-MT tasks, verification surveys）
- 引用是否准确——特别关注 bib entries 的 author name、venue、year 一致性
- 与 concurrent work 的定位是否公平

### 3. 写作质量与 Framing
- Abstract 是否过于密集（具体数字、signal 名称过多）？是否适合三段式精简？
- 术语一致性：VC/Voting Conf./entity voting 是否统一？LP/Log-prob/logprob？
- "Cross-model" 措辞是否过度（实为 cross-architecture at fixed 8B scale）？
- "First multi-family comparison" 是否为 scope engineering？应改为描述性表述？
- RE 结论在各处引用时是否一致标注 "preliminary, single benchmark"？
- Figure/Table captions 是否简洁有效？
- Ethics Statement 内容是否充分？

### 4. 格式合规
- 页数是否在 8 页正文限制内
- Limitations section 是否存在且充分
- 匿名是否完整（无作者信息泄露）
- 引用格式是否符合 ACL natbib 规范

请严格按照 EMNLP 审稿标准评审，不留情面。输出格式：Summary → Strengths → Weaknesses (Critical/Warning/Minor 分级) → Questions → Missing References → Scores (Soundness/Presentation/Contribution/Overall 1-5) → Confidence。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 498 · 2026-05-15T12:15:39.610940+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__verify_references,mcp__agent-ml-research__review_reviewer_post_to_director",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__verify_references,mcp__agent-ml-research__review_reviewer_post_to_director",
    "max_results": "3"
  }
}
```

</details>

---


### Tool result

_source line 499 · 2026-05-15T12:15:39.662301+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 500 · 2026-05-15T12:15:40.114521+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,WebFetch",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,WebFetch",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 501 · 2026-05-15T12:15:40.165290+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 502 · 2026-05-15T12:15:46.095700+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2026 reviewer guidelines review form criteria scoring"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria scoring"
  }
}
```

</details>

---


### Tool call

_source line 503 · 2026-05-15T12:15:48.009744+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.pdf",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 504 · 2026-05-15T12:15:48.965570+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_overview.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_reliability.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_signal_heatmap.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_selection_gap.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_temperature_robustness.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/figures/fig_length_logprob_scatter.pdf
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.pdf

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 955
}
```

</details>

---


### Tool call

_source line 505 · 2026-05-15T12:15:48.965993+00:00_

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
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
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

_source line 506 · 2026-05-15T12:15:49.468298+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 507 · 2026-05-15T12:15:49.468784+00:00_

called mcp__agent-ml-research__verify_references

<details open><summary>🔧 Tool call — mcp__agent-ml-research__verify_references</summary>

```json
{
  "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "tool_args": {
    "paper_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper",
    "project": "struct_self_consist_ie"
  }
}
```

</details>

---


### Tool result

_source line 508 · 2026-05-15T12:15:52.987845+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria scoring"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"}]

Based on the search results, here's information about ACL ARR 2026 reviewer guidelines, review form criteria, and scoring:

## Review Scoring System

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excite
…[truncated 1438 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 6892
}
```

</details>

---


### Tool result

_source line 509 · 2026-05-15T12:16:50.248109+00:00_

&lt;persisted-output>
Output too large (50.8KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie--claude-sessions-review-reviewer-2-a0c838f5/f80efada-c3f3-4e97-81ce-06aa0ee50f5a/tool-results/toolu_013r31ZAsoWdWc82Ssb5fKgg.txt

Preview (first 2KB):
{"result":"{\"success\": true, \"data\": {\"summary\": {\"total_bib_entries\": 62, \"total_citations\": 93, \"unique_cited_keys\": 62, \"orphan_bib\": 0, \"missing_bib\": 0, \"duplicate_keys\": 0, \"online_verified\": 56, \"online_not_found\": 3, \"online_mismatch\": 3}, \"cross_check\": {\"orphan_bib\": [], \"missing_bib\": [], \"orphan_count\": 0, \"missing_count\": 0}, \"bib_entries\": [{\"key\": \"angelopoulos2021conformal\", \"type\": \"inproceedings\", \"title\": \"Uncertainty Sets for Image Classifiers using Conformal Prediction\", \"authors\": \"Angelopoulos, Anastasios N. and Bates, Stephen and Malik, Jitendra and Jordan, M...\", \"year\": \"2021\", \"venue\": \"ICLR 2021\"}, {\"key\": \"brown2024monkeys\", \"type\": \"article\", \"title\": \"Large Language Monkeys: Scaling Inference Compute with Repeated Sampling\", \"authors\": \"Brown, Bradley and Juravsky, Jordan and Ehrlich, Ryan and Clark, Ronald and Le, ...\", \"year\": \"2024\", \"venue\": \"arXiv preprint arXiv:2407.21787\"}, {\"key\": \"chen2024usc\", \"type\": \"inproceedings\", \"title\": \"Universal Self-Consistency for Large Language Model Generation\", \"authors\": \"Chen, Xinyun and Aksitov, Renat and Alon, Uri and Ren, Jie and Xiao, Kefan and Y...\", \"year\": \"2024\", \"venue\": \"arXiv preprint (ICML 2024 Workshop ICL)\"}, {\"key\": \"cobbe2021verifiers\", \"type\": \"article\", \"title\": \"Training Verifiers to Solve Math Word Problems\", \"authors\": \"Cobbe, Karl and Kosaraju, Vineet and Bavarian, Mohammad and Chen, Mark and Jun, ...\", \"year\": \"2021\", \"venue\": \"arXiv preprint arXiv:2110.14168\"}, {\"key\": \"culotta2004confidence\", \"type\": 
…[truncated 363 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "mcp__agent-ml-research__verify_references",
  "elapsed_ms": 60779
}
```

</details>

---


### Tool call

_source line 510 · 2026-05-15T12:16:59.991998+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all scoring dimensions, their scale (1-5), and the description for each score level. Include soundness, excitement, overall assessment, confidence, and any other dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_3897c2857f11615119e277e820eae311:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with all scoring dimensions, their scale (1-5), and the description for each score level. Include soundness, excitement, overall assessment, confidence, and any other dimensions."
  }
}
```

</details>

---
