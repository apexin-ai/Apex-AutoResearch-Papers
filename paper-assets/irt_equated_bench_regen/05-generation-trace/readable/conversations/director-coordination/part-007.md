# Director coordination — Part 7 of 7

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Conversation logs

[← Part 6](part-006.md) · [Transcript overview](../director-coordination.md) · [Structured JSON](../../../sessions/3d/3daf92a3dbeb151a5ec1.json)

## Round 168

### Tool call

_source line 1712 · 2026-05-25T21:13:46.730639+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_issues.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 1713 · 2026-05-25T21:13:46.731082+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 1714 · 2026-05-25T21:13:50.093122+00:00_

Web search results for query: "EMNLP 2026 ARR call for papers submission guidelines author instructions site:aclweb.org"

Links: [{"title":"[EMNLP 2025] First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/emnlp-2025-first-call-papers"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"5th Workshop on Evaluation and Comparison for NLP systems (Eval4NLP) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/5th-workshop-evaluation-and-comparison-nlp-systems-eval4nlp"},{"title":"Call for Papers: The 20th Linguistic Annotation Workshop (LAW XX), co-located with ACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/call-papers-20th-linguistic-annotation-workshop-law-xx-co-located-acl-2026"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"},{"title":"EACL/ACL 2026 Joint Call for Workshops | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eaclacl-2026-joint-call-workshops"},{"title":"Joint Call for Tutorial Proposals (EACL/ACL) 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-eaclacl-2026"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"}]

I found information related to your search, but the results don't contain a specific EMNLP 2026 
…[truncated 1195 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "WebSearch",
  "elapsed_ms": 6027
}
```

</details>

---


### Tool call

_source line 1715 · 2026-05-25T21:13:56.968214+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 submission guidelines page limit formatting requirements"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 submission guidelines page limit formatting requirements"
  }
}
```

</details>

---


### Tool call

_source line 1716 · 2026-05-25T21:13:57.370035+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers deadline commitment"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers deadline commitment"
  }
}
```

</details>

---


### Tool call

_source line 1717 · 2026-05-25T21:13:57.922416+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1718 · 2026-05-25T21:13:58.876774+00:00_

1	issues:
2	  # === Round 19 issues (current round, fresh review) ===
3	
4	  - id: "R19-N1"
5	    summary: "DEFF 校正产生 2.16× 估计范围（13.5% vs 29.2%），论文未提供充分的分辨依据"
6	    category: method
7	    severity: critical
8	    status: in_progress
9	    first_raised_round: 19
10	    last_seen_round: 19
11	    mentions:
12	      - round: 19
13	        reviewers: [1, 2]
14	        note: "R1 提出，R2 AGREE。Simple-mean C%=29.2% vs weighted-mean C%=13.5%。"
15	    action_items:
16	      - round: 20
17	        action: "根因修复：Abstract/Intro/Conclusion/Discussion 全部移除 13.5%，改用 29.2% + cluster bootstrap CI [26.7%, 53.2%]。"
18	        assigned_to: director
19	        status: done
20	    resolution: ""
21	    resolution_round: null
22	
23	  - id: "R19-N2"
24	    summary: "Semi-synthetic 注入用 uniform binary flipping，检测力估计可能被系统性高估"
25	    category: method
26	    severity: critical
27	    status: in_progress
28	    first_raised_round: 19
29	    last_seen_round: 19
30	    mentions:
31	      - round: 19
32	        reviewers: [1, 2]
33	        note: "R1 提出，R2 AGREE。Graded shift (Δp=0.1-0.3) 下检测力可能远低于报告值。"
34	    action_items:
35	      - round: 20
36	        action: "§4.5 reframe as calibration upper bound + 20% overestimation bound; Figure 2 caption 加 calibration framing"
37	        assigned_to: director
38	        status: done
39	    resolution: ""
40	    resolution_round: null
41	
42	  - id: "R19-N3"
43	    summary: "缺少 DIF 文献中 impact/bias 关键区分——'Correct' 步骤与 mechanism-agnostic 定位逻辑冲突"
44	    category: method
45	    severity: critical
46	    status: in_progress
47	    first_raised_round: 19
48	    last_seen_round: 19
49	    mentions:
50	      - round: 19
51	        reviewers: [1, 2]
52	        note: "R1 提出，R2 强烈 AGREE。DIF 是 bias 的必要非充分条件。"
53	    action_items:
54	      - round: 20
55	        action: "§5.2 Correct 步骤重写：DIF flags → expert review，DIF is necessary but not sufficient for item bias，引用 camilli1994methods + penfield2007dif"
56	        assigned_to: director
57	        status: done
58	    resol
…[truncated 10924 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 1719 · 2026-05-25T21:13:59.128308+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_19/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_NOT_FOUND\"",
  "description": "Check if submitted PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_19/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_NOT_FOUND\"",
    "description": "Check if submitted PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 1720 · 2026-05-25T21:13:59.279331+00:00_

-rw-r--r-- 1 ubuntu ubuntu 1072427 May 25 21:11 /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_round_19/submitted.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "elapsed_ms": 151
}
```

</details>

---


### Tool result

_source line 1721 · 2026-05-25T21:14:03.144469+00:00_

Web search results for query: "EMNLP 2026 call for papers deadline commitment"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"},{"title":"AI Conference Deadlines - Jie Cao | Dialogue, NLP, ML","url":"https://mlciv.com/ai-deadlines/"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"Update EMNLP 2026 conference dates and deadlines · huggingface/ai-deadlines at 2754f67","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/2754f67c0550847973789522a0a082dd5443b5c0"},{"title":"EMNLP 2026 on X: \"The First Call for Industry Track Papers for EMNLP 2026 is officially out! Are you deploying NLP in real-world applications? Share your insights, challenges, and deployed systems with the community. 🗓️ Deadline: June 16, 2026 🔗 Link: https://t.co/ga3k6CJcm0 #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2048750521696072166"},{"title":"EMNLP 2026 on X: \"📢 Please note a critical update to the original #EMNLP2026 Call for Papers: since EMNLP and AACL share the ARR May cycle, authors will need to explicitly select a target conference at submission time. This choice will be binding! For more details see: https://t.co/0u1wbX9fT6\" / X","url":"https://x.com/emnlpmeeting/status/2047754845919031450"},{"title"
…[truncated 1318 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "WebSearch",
  "elapsed_ms": 5774
}
```

</details>

---


### Tool result

_source line 1722 · 2026-05-25T21:14:04.199292+00:00_

Web search results for query: "ACL Rolling Review 2026 submission guidelines page limit formatting requirements"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"ACL ARR 2026 January | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2026%2FJanuary"}]

Based on the search results, here are the key submission guidelines for ACL Rolling Review 2026 regarding page limits and formatting requirements:

## Page Limits

Review versions of long papers may have up to eight (8) pages of content plus unlimited pages for references. Upon acceptance, final versions of long papers will be given one additional page – up to nine (9) pages of content plus unlimited pages for acknowledgments and references – so that reviewers' comments can be taken into account.

Review version
…[truncated 1324 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "WebSearch",
  "elapsed_ms": 7231
}
```

</details>

---


### Tool call

_source line 1723 · 2026-05-25T21:15:04.154673+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/abstract.tex"
  }
}
```

</details>

---


### Tool call

_source line 1724 · 2026-05-25T21:15:04.155234+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/introduction.tex"
  }
}
```

</details>

---


### Tool call

_source line 1725 · 2026-05-25T21:15:04.155566+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/method.tex"
  }
}
```

</details>

---


### Tool call

_source line 1726 · 2026-05-25T21:15:04.156478+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool call

_source line 1727 · 2026-05-25T21:15:04.156833+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/discussion.tex"
  }
}
```

</details>

---


### Tool call

_source line 1728 · 2026-05-25T21:15:04.157070+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/limitations.tex"
  }
}
```

</details>

---


### Tool call

_source line 1729 · 2026-05-25T21:15:04.157295+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/conclusion.tex"
  }
}
```

</details>

---


### Tool call

_source line 1730 · 2026-05-25T21:15:04.157508+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 1731 · 2026-05-25T21:15:04.208204+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	We adopt Differential Item Functioning (DIF) analysis from educational measurement to assess whether individual benchmark items behave consistently across groups of LLMs. The procedure requires only a binary response matrix and group labels, with no access to model internals or training data. Below we define the data, the statistical test, the cohort designs, and a semi-synthetic validation framework.
5	
6	\subsection{Data}
7	\label{sec:data}
8	
9	The primary dataset is the METABENCH response matrix~\citep{kipnis2024metabench}, which records binary outcomes (1~=~correct, 0~=~incorrect) for 5,227 models evaluated on 12,508 MMLU items~\citep{hendrycks2021mmlu}. Models span release dates from 2023 to 2024, drawn from the Open LLM Leaderboard. MMLU covers 57 subjects grouped into five broad domains (STEM, Humanities, Social Sciences, Other, and a mixed category). We supplement the response matrix with the web-overlap contamination labels of \citet{li2024contamination}, which classify 9,229 of 12,508 items (73.8\% coverage) as ``contaminated'' or ``clean'' based on verbatim matches in publicly accessible web corpora. These labels serve as an external reference for evaluating the relationship between DIF flags and existing contamination indicators.
10	
11	\subsection{Mantel-Haenszel DIF and ETS Classification}
12	\label{sec:mhdif}
13	
14	In educational testing, Differential Item Functioning (DIF) occurs when an item's statistical relationship to the latent trait $\theta$ differs between two groups after conditioning on ability level. An item with DIF is not merely harder for one group; it functions differently relative to what the group's overall ability would predict. The standard terminology refers to test-takers as ``examinees'' and questions as ``items.'' In our setting, examinees are LLMs and items are benchmark questions.
15	
16	The Mantel-Haenszel (MH) procedure~\citep{holland1988mh,magis2010difr} detects DIF by stratify
…[truncated 11194 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 52
}
```

</details>

---


### Tool result

_source line 1732 · 2026-05-25T21:15:04.208672+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	\looseness=-1
5	When we say ``Model B outperforms Model A on MMLU,'' we assume that every test item measures the same construct for both models. In educational testing, this property, \emph{measurement invariance}~\citep{meredith1993invariance}, is routinely verified before scores are compared across groups; in LLM evaluation, it has never been tested at scale. We test it here, applying Mantel-Haenszel differential item functioning (DIF) analysis~\citep{holland1988mh} with ETS severity classification to the METABENCH response matrix~\citep{kipnis2024metabench} (5,227 models $\times$ 12,508 MMLU~\citep{hendrycks2021mmlu} items). The result is sobering: 31\% of items receive ETS Category~C classification ($|\Delta_{\mathrm{MH}}| \geq 1.5$, $p < 0.05$) between 2023 and 2024 model cohorts, compared to 0.62\% under random-split controls, and the finding replicates across all six METABENCH benchmarks (17.9--31.3\%).
6	
7	\begin{figure*}[t]
8	\centering
9	\includegraphics[width=\textwidth]{fig_0_pipeline.pdf}
10	\caption{Four-stage psychometric auditing pipeline. \textbf{\ding{192}} A binary response matrix records model correctness across benchmark items, with models split into temporal cohorts (2023 reference vs.\ 2024 focal). \textbf{\ding{193}} Models are stratified into $K{=}5$ score quintiles. \textbf{\ding{194}} Per-item Mantel-Haenszel DIF tests compute $\Delta_{\mathrm{MH}}$ across strata. \textbf{\ding{195}} ETS classification assigns severity labels (A/B/C). Result: 31.3\% of items flagged as C (29.2\% after DEFF correction), yet stable-item $\rho = 0.997$, replicated across six benchmarks.}
11	\label{fig:pipeline}
12	\end{figure*}
13	
14	\looseness=-1
15	This instability is not what it appears. Aggregate rankings are near-perfect ($\rho \approx 0.997$): even after all unstable items are removed, the leaderboard barely changes. But individual items have shifted in structured ways: some became easier for ne
…[truncated 3323 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 53
}
```

</details>

---


### Tool result

_source line 1733 · 2026-05-25T21:15:04.208973+00:00_

1	\begin{abstract}
2	Every leaderboard comparison assumes that benchmark items measure the same construct across model generations. In educational testing, this foundational property, measurement invariance, is routinely verified. In large language model (LLM) evaluation, it has never been tested at scale. We bring differential item functioning (DIF) analysis from psychometrics to the METABENCH response matrix (5,227 models on MMLU) and find that 31\% of items function systematically differently between 2023 and 2024 model cohorts, 50$\times$ above random baselines. This instability is not driven by data contamination: DIF flags are near-independent of web-overlap labels ($\phi = 0.012$), an overlooked diagnostic dimension. Nor does it threaten validity: aggregate rankings remain near-perfect ($\rho \approx 0.997$). Instead, unstable items expose which capability dimensions shift across generations; base and instruct models exhibit opposite DIF directions. We develop a semi-synthetic validation framework with cross-subject matching that guarantees zero false-positive inflation, replicate findings across six benchmarks (18--31\% instability), and propose an actionable audit protocol. LLM benchmarks need psychometric monitoring, not just score reporting\footnote{Code and data are available at \url{https://anonymous.4open.science/r/irt_equated_bench_regen-2431/}.}.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 54
}
```

</details>

---


### Tool result

_source line 1734 · 2026-05-25T21:15:04.209170+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	\looseness=-2
5	Across six benchmarks, 17.9--31.3\% of items exhibit temporal DIF while rankings remain stable ($\rho \geq 0.994$); base-vs-instruct reversals and web-overlap independence confirm signal beyond contamination, and cross-subject matching, DEFF correction, and a Monitor/Triage/Correct protocol enable ongoing psychometric auditing.
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool result

_source line 1735 · 2026-05-25T21:15:04.209359+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Psychometric Methods for LLM Evaluation.}
5	\looseness=-1
6	The Mantel-Haenszel procedure \citep{holland1988mh} remains the most widely used DIF detector in educational testing due to its simplicity and well-characterized statistical properties, operating nonparametrically without requiring an explicit item response theory (IRT) model. DIF analysis is a specific instance of measurement invariance testing \citep{meredith1993invariance}, which examines whether an instrument functions equivalently across groups. IRT adoption in LLM evaluation has accelerated since \citet{lalor2019irt} introduced it to natural language processing: recent work calibrates test sets for discriminability, item selection, and adaptive evaluation. The closest concurrent work is Growing Pains \citep{habba2026growingpains}, which uses parametric IRT (two-parameter logistic [2PL] / three-parameter logistic [3PL] fixed-parameter calibration) to equate scores across temporal cohorts. MH-DIF is nonparametric and robust to model misspecification, an advantage given poor 2PL fit for MMLU (root mean square error of approximation [RMSEA] $> 0.08$; \Cref{app:power_sensitivity}). Growing Pains prescribes how to equate scores after instability is detected; our work diagnoses \emph{which} items exhibit instability and quantifies severity via ETS classification, providing pre-screened anchor candidates for downstream equating. Their anchor-item selection can directly consume our stable-item set; our finding that 31\% of items exhibit temporal DIF identifies which items should \emph{not} serve as anchors. To our knowledge, no prior work applies DIF to benchmark temporal comparability.
7	
8	\paragraph{Contamination Detection.}
9	\looseness=-1
10	A growing family of methods detects benchmark contamination through model behavior or training-data analysis. Membership inference approaches use token-level log-likelihood statistics \citep{shi2024mi
…[truncated 1669 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool result

_source line 1736 · 2026-05-25T21:15:04.209538+00:00_

1	\section*{Limitations}
2	
3	\looseness=-1
4	(1)~The semi-synthetic injection framework uses uniform binary response flipping; realistic contamination (partial memorization, format-specific advantages) would produce weaker DIF signals, so reported $\Delta\mathrm{TPR}$ values may overestimate detection power. The framework detects \emph{that} items function differently but not \emph{why}. (2)~The MH $\chi^2$ test assumes independent examinees; LLM model families violate this assumption. DEFF correction and cluster bootstrap bound the impact, but extreme within-family relatedness (e.g., hundreds of Llama-2 fine-tunes) exceeds educational-testing precedents~\citep{french2010hierarchical}. (3)~Cross-subject matching assumes contamination affects a minority of domains ($\Delta\mathrm{FPR}$ rises when contamination spans ${\geq}20$ subjects), and generalization beyond MCQ benchmarks requires further validation.
5	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 52
}
```

</details>

---


### Tool result

_source line 1737 · 2026-05-25T21:15:04.209748+00:00_

1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\subsection{Temporal DIF as Structured Signal}
5	\label{sec:disc_temporal}
6	
7	\looseness=-2
8	Temporal DIF detects \emph{that} items function differently across cohorts, not \emph{why}, by design (\Cref{sec:cohorts}). Stratifying by model type reveals opposite patterns: base models ($N{=}1{,}409$) are 60.1\% reference-favoring ($r = -0.570$), while instruct models ($N{=}478$) are 65.6\% focal-favoring ($\chi^2 = 562.7$, $p < 10^{-124}$). This reversal reflects structured item-level bias rather than uniform group impact~\citep{camilli1994methods}, consistent with DIF as a mechanism-agnostic diagnostic; mixed-mechanism injection cannot match the near-zero instruct gradient, pointing to non-contamination drivers (\Cref{app:mechanism_discussion,app:mixed_mechanism}). Composition downsampling ($\Delta = 1.08$\,pp) and base-only/instruct-only analyses confirm DIF is not a cohort-structure artifact (\Cref{app:composition_control,app:baseinst_temporal,app:within_arch}). Three features distinguish LLM temporal DIF from educational settings: C\% (29.2\%) substantially exceeds typical rates~\citep{clauser1998dif}; DIF flags and web-overlap labels are near-independent (Jaccard $= 0.206$); and the base/instruct reversal (OR $= 4.75$) favors a broader-signal reading over distinct-construct independence.
9	
10	\subsection{Recommended DIF Audit Protocol}
11	\label{sec:disc_protocol}
12	
13	\looseness=-2
14	Item-level properties do not predict DIF susceptibility (AUROC $= 0.60$; \Cref{app:predictive}), precluding pre-screening. We recommend: (1)~\emph{Monitor}: run MH-DIF audits when ${\geq}$500 models accumulate, triggering review when C\% exceeds $20\times$ the random-split baseline; (2)~\emph{Triage}: DIF $\times$ web-overlap co-occurrence warrants removal, DIF on web-clean items warrants monitoring; (3)~\emph{Correct}: expert review, not automatic removal~\citep{camilli1994methods,penfield2007dif} (\Cref{app:score_inflation}
…[truncated 6 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 52
}
```

</details>

---


### Tool result

_source line 1738 · 2026-05-25T21:15:04.210047+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We apply MH-DIF to the METABENCH response matrix~\citep{kipnis2024metabench} (5,227 models $\times$ 12,508 MMLU items~\citep{hendrycks2021mmlu}), with temporal cohorts defined by release date (2023 vs.\ 2024). Cross-benchmark validation across all six METABENCH benchmarks appears in \Cref{sec:gsm8k}.
5	
6	\begin{figure*}[t]
7	\centering
8	\includegraphics[width=\textwidth]{fig_A3_rho_degradation.pdf}
9	\caption{Ranking degradation under DIF-ordered vs.\ random item removal. DIF-ordered removal (orange) degrades $\rho$ faster than random (blue band = mean $\pm$ 1\,SD, 20 seeds). Dashed lines: Monitor/Flag (15\%) and Flag/Act (25\%) thresholds (\Cref{sec:disc_protocol}).}
10	\label{fig:rho_degradation}
11	\end{figure*}
12	
13	\subsection{Validation: DIF Detection Power}
14	\label{sec:validation}
15	
16	\looseness=-1
17	A Monte Carlo power analysis (1,000 replications) using empirical 2PL parameters from PSN-IRT~\citep{zhou2026psnirt} ($\bar{a} = 1.2$, $\bar{b} = -0.84$) confirms that at $N \geq 100$ per cohort, ETS~C achieves TPR of 0.68--0.80 (under uniform injection) and area under the curve (AUC) of 0.93--0.94 for $|\Delta_{\mathrm{MH}}| \geq 1.4$ (\Cref{app:method_details}). Our temporal cohorts ($N_{\mathrm{ref}} = 1{,}080$, $N_{\mathrm{focal}} = 807$) far exceed this threshold; power varies with item discrimination (TPR 0.40--0.95 across $a = 0.5$--$2.0$; \Cref{app:power_sensitivity}).
18	
19	\subsection{Temporal DIF: ${\sim}$29\% of Items Exhibit Differential Functioning}
20	\label{sec:temporal}
21	
22	\looseness=-1
23	We compare 2023 ($N = 1{,}080$) against 2024 ($N = 807$) models; 31.3\% of items receive ETS~C classification ($|\Delta_{\mathrm{MH}}| \geq 1.5$; bootstrap 95\% CI: $[29.2\%, 37.8\%]$; family-level cluster bootstrap: $[26.7\%, 53.2\%]$; \Cref{app:uncertainty}). Two DEFF estimators bound the non-independence effect: simple-mean DEFF yields 29.2\% and weighted-mean yields 13.5\%, bracketing C\%
…[truncated 7918 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 53
}
```

</details>

---


### Tool call

_source line 1739 · 2026-05-25T21:15:23.408654+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "irt_equated_bench_regen",
  "file": "paper_checklist.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "irt_equated_bench_regen",
    "file": "paper_checklist.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool call

_source line 1740 · 2026-05-25T21:15:23.409080+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 1741 · 2026-05-25T21:15:25.216765+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'irt_equated_bench_regen'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 1808
}
```

</details>

---


### Tool result

_source line 1742 · 2026-05-25T21:15:25.217136+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 1808
}
```

</details>

---


### Tool call

_source line 1743 · 2026-05-25T21:15:25.367959+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex",
  "limit": "60"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/sections/appendix.tex",
    "limit": "60"
  }
}
```

</details>

---


### Tool result

_source line 1744 · 2026-05-25T21:15:25.368450+00:00_

1	\section{Method Details}
2	\label{app:method_details}
3	
4	\subsection{Diagnostics}
5	\label{app:diagnostics}
6	
7	Three diagnostic procedures complement the primary DIF analysis.
8	
9	\paragraph{Local independence (Yen's Q3).} The MH procedure assumes that item responses are conditionally independent given $\theta$. Yen's Q3 statistic measures residual correlations between item pairs after conditioning on the latent trait. We compute Q3 for all within-subject and cross-subject item pairs, with $|Q3| > 0.20$ as the threshold for local dependence. Elevated within-subject dependence would indicate that items within the same subject share variance beyond what $\theta$ captures, which could inflate within-subject DIF rates.
10	
11	\paragraph{Domain-specificity.} We test whether temporal DIF concentrates in domains where models improved most. At the ecological level, we compute Spearman $\rho$ between subject-level C\% and subject-level accuracy improvement from 2023 to 2024. At the item level, logistic regression predicts item-level DIF~C classification from domain-level accuracy change, with and without item property controls (difficulty, discrimination). This decomposition quantifies how much of the observed instability is attributable to aggregate domain-level gains versus item-specific behavioral change.
12	
13	\paragraph{Instability decomposition.} When domain accuracy improvement is included alongside item-level controls, we compute the counterfactual C\% that would remain after removing domain-level effects. The gap between observed and counterfactual C\% measures the contribution of domain-level improvement to the total instability.
14	
15	\subsection{Statistical Considerations}
16	\label{app:statistical}
17	
18	\paragraph{Multiple testing.} The ETS~C classification imposes a dual threshold (effect size $|\Delta_{\mathrm{MH}}| \geq 1.5$ and significance $p < 0.05$), which provides implicit control over false positives. As a robustness check, we apply Benjamini
…[truncated 3694 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1745 · 2026-05-25T21:15:46.604424+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "irt_equated_bench_regen",
  "file": "decisions.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "irt_equated_bench_regen",
    "file": "decisions.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 1746 · 2026-05-25T21:15:46.604949+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/decisions.yaml\", \"content\": \"_next_id: 41\\ndecisions:\\n- id: D001\\n  date: 2026-05-20 18:50 UTC\\n  summary: MVP DIF 检测采用 ETS C 分类（效应量+显著性双阈值）替代 BH 校正 p 值作为主判定标准\\n  rationale: Monte Carlo 模拟显示 BH 校正在 200 items 场景下将 TPR 压缩 40-60%，所有核心条件均 FAIL/GRAY。但\\n    ETS C 分类（|Δ_MH|≥1.5 + 显著性，教育测量 gold standard）在 N≥80, δ≥1.4 时 TPR=0.72-0.85, FPR<0.05，满足\\n    pass criteria。ETS C 是 DIF 领域标准实践（Holland & Thayer 1988），使用效应量阈值比纯 p 值更稳健。操作点 N≥80,\\n    δ≥1.4 与 GSM1K 文档的重度污染效应量吻合。小效应由 ensemble 其他信号覆盖。\\n  related_experiments:\\n  - exp_id: mvp_dif_power_sim\\n    role: evidence\\n    result: 'BH-corrected: all FAIL/GRAY; ETS C: PASS at N≥80,δ≥1.4 (TPR=0.72-0.85,\\n      FPR<0.05)'\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-20 19:31 UTC\\n  summary: MVP 通过：DIF+ETS C 在 N≥80,δ≥1.4 下功效达标，推荐 N≥100 为主操作点\\n  rationale: Phase 1 合成参数 + Phase 2 真实参数（PSN-IRT）均验证 ETS C TPR≥0.65 at N≥80,δ≥1.4。Phase\\n    2 比 Phase 1 降低 3-6pp 符合预期。N=80,δ=1.4 裕度仅 0.032，推荐 N≥100 为主 claim。数据源为 PSN-IRT\\n    而非 ROADMAP 指定的 METABENCH，research 阶段需用 METABENCH 补充验证。限制：δ<1.0 需 ensemble 其他信号。\\n  related_experiments:\\n  - exp_id: mvp_dif_power_sim\\n    role: evidence\\n    result: 'Phase 1 conditional pass: ETS C TPR=0.72-0.85 at N≥80,δ≥1.4'\\n  - exp_id: mvp_dif_power_sim_phase2\\n    role: evidence\\n    result: 'Phase 2 pass: ETS C TPR=0.68-0.80 at N≥80,δ≥1.4 with real MMLU params'\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-20 20:49 UTC\\n  summary: 'Dream analysis (dream_20260520T194223): 6 confirmed actions from cross-tier\\n    synthesis, 2 new experiments added (plan_010/011), framing qualified'\\n  rationale: 'Dream scores met thresholds (best=4/6, median=3.5/6, worst=3/6). Cross-tier\\n    analysis identified 6 confirmed issues (≥2 tiers): (1) contamination-capability\\n    confound → within-family analysis added to plan_001; (2) RL evidence underpower
…[truncated 1430 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 1747 · 2026-05-25T21:15:56.545006+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/agent/config.yaml 2>/dev/null | head -80",
  "description": "Check project config for external review settings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/agent/config.yaml 2>/dev/null | head -80",
    "description": "Check project config for external review settings"
  }
}
```

</details>

---


### Tool result

_source line 1748 · 2026-05-25T21:15:56.645813+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1749 · 2026-05-25T21:16:00.160907+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0520_2 -name \"config.yaml\" -path \"*/irt_equated*\" 2>/dev/null | head -5",
  "description": "Find project config file"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0520_2 -name \"config.yaml\" -path \"*/irt_equated*\" 2>/dev/null | head -5",
    "description": "Find project config file"
  }
}
```

</details>

---


### Tool result

_source line 1750 · 2026-05-25T21:16:01.064489+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "elapsed_ms": 903
}
```

</details>

---


### Tool call

_source line 1751 · 2026-05-25T21:16:04.230804+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0520_2 -name \"*.yaml\" -path \"*irt_equated*\" -not -path \"*/artifacts/*\" -not -path \"*review_issues*\" -not -path \"*decisions*\" 2>/dev/null | head -10",
  "description": "Find project config files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0520_2 -name \"*.yaml\" -path \"*irt_equated*\" -not -path \"*/artifacts/*\" -not -path \"*review_issues*\" -not -path \"*decisions*\" 2>/dev/null | head -10",
    "description": "Find project config files"
  }
}
```

</details>

---


### Tool result

_source line 1752 · 2026-05-25T21:16:04.331727+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/distill_tmp/hendrycks2021mmlu.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/distill_tmp/liang2026dvd.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/distill_tmp/shi2024mink.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/distill_tmp/balloccu2024leak.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/distill_tmp/lalor2019irt.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/distill_tmp/zhou2026psnirt.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/distill_tmp/dekoninck2024constat.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/distill_tmp/chen2025irtnet.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/distill_tmp/li2024latesteval.yaml
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/distill_tmp/white2025livebench.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1753 · 2026-05-25T21:16:07.092294+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0520_2 -name \"config.*\" -not -path \"*/node_modules/*\" -not -path \"*/.venv/*\" 2>/dev/null | head -10",
  "description": "Find config files for external review settings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0520_2 -name \"config.*\" -not -path \"*/node_modules/*\" -not -path \"*/.venv/*\" 2>/dev/null | head -10",
    "description": "Find config files for external review settings"
  }
}
```

</details>

---


### Tool result

_source line 1754 · 2026-05-25T21:16:07.193058+00:00_

(Bash completed with no output)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 1755 · 2026-05-25T21:16:41.151450+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "irt_equated_bench_regen",
  "review_chat_id": "oc_f025582a920d3f79beb59dfc17929017"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "irt_equated_bench_regen",
    "review_chat_id": "oc_f025582a920d3f79beb59dfc17929017"
  }
}
```

</details>

---


### Tool result

_source line 1756 · 2026-05-25T21:17:07.178678+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 26027
}
```

</details>

---


### Tool call

_source line 1757 · 2026-05-25T21:17:07.329811+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

````json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## Round 1 审稿任务 — Reviewer 1：方法严谨性 + 实验有效性\n\n### Venue 信息\n- **目标会议**: EMNLP 2026 (通过 ACL Rolling Review 提交)\n- **Deadline**: 2026-05-25 (ARR May cycle)\n- **页数限制**: 正文 8 页 + references 无限制；Limitations 不计入页数\n- **模板**: ACL style template (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind review\n- **附录规则**: 允许，可供 reviewer 参考但不强制阅读\n\n### 论文文件\n- LaTeX 源码: `projects/irt_equated_bench_regen/paper/main.tex`（入口文件，各 section 在 `sections/` 子目录）\n- PDF: `projects/irt_equated_bench_regen/artifacts/review_round_19/submitted.pdf`\n\n### 你的审查侧重\n\n**方法严谨性 + 实验有效性**。你需要重点审查：\n\n1. **MH-DIF 方法论**：\n   - MH 检验在 LLM 设定下的适用性（独立性假设违反、非参数 vs 参数方法选择）\n   - ETS 阈值从人类考生迁移到 LLM 的合理性及校准\n   - $K=5$ quintile stratification 的选择依据\n   - 多重比较处理（为何不做 FDR/FWER correction 作为主方法）\n\n2. **Semi-synthetic 注入框架**：\n   - Uniform binary flipping 的现实性——是否高估检测力\n   - Cross-subject matching 的 $\\Delta\\mathrm{FPR}=0$ 声明的严谨性\n   - $k \\leq 5$ 的保证边界在更大 $k$ 下如何退化\n   - Injection 实验设计是否充分验证了方法的检测能力\n\n3. **统计声明**：\n   - DEFF 校正：simple-mean (29.2%) vs weighted-mean (13.5%) 的 2.16× 差距——论文如何处理这一不确定性\n   - 31.3% C% 的置信区间和 bootstrap 方法\n   - Random-split baseline 0.62% 的可靠性\n   - Power analysis 参数选择（$\\bar{a}=1.2$, $\\bar{b}=-0.84$）\n\n4. **控制实验**：\n   - Ability-quintile C%=2.9% 是否充分排除了能力差异混淆\n   - Leave-one-family-out (LOFO) 分析的充分性\n   - 1:1 nearest-neighbor matching 的设计\n   - Within-family (Llama-2 vs Llama-3) C%=61.3% 的解释\n\n5. **因果推断与机制**：\n   - \"near-independent of web-overlap labels\" (Jaccard=0.206, φ=0.012) 的推断强度\n   - Base vs instruct 反向模式 (χ²=562.7) 的解释是否过强\n   - DIF 检测的是 \"differential functioning\" 还是 \"impact\"——论文是否充分区分\n\n### 输出格式\n\n请按以下结构输出审稿意见：\n\n```\n## Summary\n[2-3 句论文概述]\n\n## Strengths\n[逐条列出优点，标注 S1, S2, ...]\n\n## Weaknesses\n[逐条列出缺点，标注 W1, W2, ...，按严重性排序]\n每条包含：问题描述 + 具体证据（cite Section/Table/Figure）+ 建议\n\n## Questions\n[需要作者回答的问题，标注 Q1, Q2, ...]\n\n## Missing References\n[遗漏的重要相关工作]\n\n## Minor Issues\n[格式、typo、表述等小问题]\n\n## Overall Assessment\n评分（1-5，参考 ARR 标准）+ 置信度（1-5）+ 简要理由\n```"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## Round 1 审稿任务 — Reviewer 1：方法严谨性 + 实验有效性\n\n### Venue 信息\n- **目标会议**: EMNLP 2026 (通过 ACL Rolling Review 提交)\n- **Deadline**: 2026-05-25 (ARR May cycle)\n- **页数限制**: 正文 8 页 + references 无限制；Limitations 不计入页数\n- **模板**: ACL style template (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind review\n- **附录规则**: 允许，可供 reviewer 参考但不强制阅读\n\n### 论文文件\n- LaTeX 源码: `projects/irt_equated_bench_regen/paper/main.tex`（入口文件，各 section 在 `sections/` 子目录）\n- PDF: `projects/irt_equated_bench_regen/artifacts/review_round_19/submitted.pdf`\n\n### 你的审查侧重\n\n**方法严谨性 + 实验有效性**。你需要重点审查：\n\n1. **MH-DIF 方法论**：\n   - MH 检验在 LLM 设定下的适用性（独立性假设违反、非参数 vs 参数方法选择）\n   - ETS 阈值从人类考生迁移到 LLM 的合理性及校准\n   - $K=5$ quintile stratification 的选择依据\n   - 多重比较处理（为何不做 FDR/FWER correction 作为主方法）\n\n2. **Semi-synthetic 注入框架**：\n   - Uniform binary flipping 的现实性——是否高估检测力\n   - Cross-subject matching 的 $\\Delta\\mathrm{FPR}=0$ 声明的严谨性\n   - $k \\leq 5$ 的保证边界在更大 $k$ 下如何退化\n   - Injection 实验设计是否充分验证了方法的检测能力\n\n3. **统计声明**：\n   - DEFF 校正：simple-mean (29.2%) vs weighted-mean (13.5%) 的 2.16× 差距——论文如何处理这一不确定性\n   - 31.3% C% 的置信区间和 bootstrap 方法\n   - Random-split baseline 0.62% 的可靠性\n   - Power analysis 参数选择（$\\bar{a}=1.2$, $\\bar{b}=-0.84$）\n\n4. **控制实验**：\n   - Ability-quintile C%=2.9% 是否充分排除了能力差异混淆\n   - Leave-one-family-out (LOFO) 分析的充分性\n   - 1:1 nearest-neighbor matching 的设计\n   - Within-family (Llama-2 vs Llama-3) C%=61.3% 的解释\n\n5. **因果推断与机制**：\n   - \"near-independent of web-overlap labels\" (Jaccard=0.206, φ=0.012) 的推断强度\n   - Base vs instruct 反向模式 (χ²=562.7) 的解释是否过强\n   - DIF 检测的是 \"differential functioning\" 还是 \"impact\"——论文是否充分区分\n\n### 输出格式\n\n请按以下结构输出审稿意见：\n\n```\n## Summary\n[2-3 句论文概述]\n\n## Strengths\n[逐条列出优点，标注 S1, S2, ...]\n\n## Weaknesses\n[逐条列出缺点，标注 W1, W2, ...，按严重性排序]\n每条包含：问题描述 + 具体证据（cite Section/Table/Figure）+ 建议\n\n## Questions\n[需要作者回答的问题，标注 Q1, Q2, ...]\n\n## Missing References\n[遗漏的重要相关工作]\n\n## Minor Issues\n[格式、typo、表述等小问题]\n\n## Overall Assessment\n评分（1-5，参考 ARR 标准）+ 置信度（1-5）+ 简要理由\n```"
  }
}
````

</details>

---


### Tool result

_source line 1758 · 2026-05-25T21:17:24.878142+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 17548
}
```

</details>

---


### Tool call

_source line 1759 · 2026-05-25T21:17:25.029921+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

````json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## Round 1 审稿任务 — Reviewer 2：新颖性/定位 + 完整性\n\n### Venue 信息\n- **目标会议**: EMNLP 2026 (通过 ACL Rolling Review 提交)\n- **Deadline**: 2026-05-25 (ARR May cycle)\n- **页数限制**: 正文 8 页 + references 无限制；Limitations 不计入页数\n- **模板**: ACL style template (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind review\n- **附录规则**: 允许，可供 reviewer 参考但不强制阅读\n\n### 论文文件\n- LaTeX 源码: `projects/irt_equated_bench_regen/paper/main.tex`（入口文件，各 section 在 `sections/` 子目录）\n- PDF: `projects/irt_equated_bench_regen/artifacts/review_round_19/submitted.pdf`\n\n### 你的审查侧重\n\n**新颖性/定位 + 完整性**。你需要重点审查：\n\n1. **方法论新颖性**：\n   - MH-DIF 是教育测量中的标准方法——直接搬运到 LLM 评估的新颖性是否足够？\n   - Cross-subject matching 和 DEFF 校正是否构成足够的 LLM-specific 贡献？\n   - 与 Growing Pains (Habba et al., 2026) 的差异化是否充分？\n   - \"首次大规模 DIF 分析\" 这一定位的竞争力\n\n2. **叙事与贡献定位**：\n   - 标题 \"Temporal Score Incomparability\" 是否准确反映论文内容（论文实际发现 ranking 稳定 ρ≈0.997）\n   - \"Mechanism-agnostic\" 定位与论文中大量 contamination 讨论之间是否存在叙事张力\n   - 三个 contribution 的权重和层次是否合理\n   - Abstract 是否准确、concise（检查是否 ≤200 words）\n\n3. **Related Work**：\n   - 覆盖面是否完整（DIF 方法论文献、IRT for NLP、contamination detection、benchmark quality）\n   - 是否遗漏了关键相关工作\n   - 与竞争方法的对比是否公平\n   - Related Work 的组织结构和叙事逻辑\n\n4. **写作质量**：\n   - 关键概念解释是否对 NLP 读者足够清晰（DIF、MH、ETS 分类等心理测量学概念）\n   - 论文整体可读性和信息密度\n   - Figure 和 Table 的自包含性和信息传达效率\n   - 专业术语使用的一致性\n\n5. **格式合规**：\n   - 正文是否在 8 页限制内\n   - Limitations section 是否存在且内容充分\n   - 匿名性是否保持（检查是否泄露身份信息）\n   - 引用格式是否符合 ACL 规范\n   - 代码/数据可用性声明\n\n6. **Limitations 和 Broader Impact**：\n   - Limitations 是否覆盖关键局限（3 个点左右即可）\n   - 是否遗漏了重要局限\n\n### 输出格式\n\n请按以下结构输出审稿意见：\n\n```\n## Summary\n[2-3 句论文概述]\n\n## Strengths\n[逐条列出优点，标注 S1, S2, ...]\n\n## Weaknesses\n[逐条列出缺点，标注 W1, W2, ...，按严重性排序]\n每条包含：问题描述 + 具体证据（cite Section/Table/Figure）+ 建议\n\n## Questions\n[需要作者回答的问题，标注 Q1, Q2, ...]\n\n## Missing References\n[遗漏的重要相关工作]\n\n## Minor Issues\n[格式、typo、表述等小问题]\n\n## Overall Assessment\n评分（1-5，参考 ARR 标准）+ 置信度（1-5）+ 简要理由\n```"
}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## Round 1 审稿任务 — Reviewer 2：新颖性/定位 + 完整性\n\n### Venue 信息\n- **目标会议**: EMNLP 2026 (通过 ACL Rolling Review 提交)\n- **Deadline**: 2026-05-25 (ARR May cycle)\n- **页数限制**: 正文 8 页 + references 无限制；Limitations 不计入页数\n- **模板**: ACL style template (`\\usepackage[review]{acl}`)\n- **匿名规则**: Double-blind review\n- **附录规则**: 允许，可供 reviewer 参考但不强制阅读\n\n### 论文文件\n- LaTeX 源码: `projects/irt_equated_bench_regen/paper/main.tex`（入口文件，各 section 在 `sections/` 子目录）\n- PDF: `projects/irt_equated_bench_regen/artifacts/review_round_19/submitted.pdf`\n\n### 你的审查侧重\n\n**新颖性/定位 + 完整性**。你需要重点审查：\n\n1. **方法论新颖性**：\n   - MH-DIF 是教育测量中的标准方法——直接搬运到 LLM 评估的新颖性是否足够？\n   - Cross-subject matching 和 DEFF 校正是否构成足够的 LLM-specific 贡献？\n   - 与 Growing Pains (Habba et al., 2026) 的差异化是否充分？\n   - \"首次大规模 DIF 分析\" 这一定位的竞争力\n\n2. **叙事与贡献定位**：\n   - 标题 \"Temporal Score Incomparability\" 是否准确反映论文内容（论文实际发现 ranking 稳定 ρ≈0.997）\n   - \"Mechanism-agnostic\" 定位与论文中大量 contamination 讨论之间是否存在叙事张力\n   - 三个 contribution 的权重和层次是否合理\n   - Abstract 是否准确、concise（检查是否 ≤200 words）\n\n3. **Related Work**：\n   - 覆盖面是否完整（DIF 方法论文献、IRT for NLP、contamination detection、benchmark quality）\n   - 是否遗漏了关键相关工作\n   - 与竞争方法的对比是否公平\n   - Related Work 的组织结构和叙事逻辑\n\n4. **写作质量**：\n   - 关键概念解释是否对 NLP 读者足够清晰（DIF、MH、ETS 分类等心理测量学概念）\n   - 论文整体可读性和信息密度\n   - Figure 和 Table 的自包含性和信息传达效率\n   - 专业术语使用的一致性\n\n5. **格式合规**：\n   - 正文是否在 8 页限制内\n   - Limitations section 是否存在且内容充分\n   - 匿名性是否保持（检查是否泄露身份信息）\n   - 引用格式是否符合 ACL 规范\n   - 代码/数据可用性声明\n\n6. **Limitations 和 Broader Impact**：\n   - Limitations 是否覆盖关键局限（3 个点左右即可）\n   - 是否遗漏了重要局限\n\n### 输出格式\n\n请按以下结构输出审稿意见：\n\n```\n## Summary\n[2-3 句论文概述]\n\n## Strengths\n[逐条列出优点，标注 S1, S2, ...]\n\n## Weaknesses\n[逐条列出缺点，标注 W1, W2, ...，按严重性排序]\n每条包含：问题描述 + 具体证据（cite Section/Table/Figure）+ 建议\n\n## Questions\n[需要作者回答的问题，标注 Q1, Q2, ...]\n\n## Missing References\n[遗漏的重要相关工作]\n\n## Minor Issues\n[格式、typo、表述等小问题]\n\n## Overall Assessment\n评分（1-5，参考 ARR 标准）+ 置信度（1-5）+ 简要理由\n```"
  }
}
````

</details>

---


### Tool result

_source line 1760 · 2026-05-25T21:17:26.540660+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1510
}
```

</details>

---


### Assistant

_source line 1761 · 2026-05-25T21:17:36.651332+00:00_

已派发：
- **视觉审查 Agent**：已启动，与审稿并行
- **Reviewer 1**（方法严谨性 + 实验有效性）：已分配
- **Reviewer 2**（新颖性/定位 + 完整性）：已分配

等待两位 Reviewer 返回 Round 1 独立审稿意见。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 169

## Round 169

2 recorded events


### User

_source line 1762 · 2026-05-25T21:22:31.988205+00:00_

[Reviewer 1 审稿意见]:
## Summary

本文将教育测量学中的 Mantel-Haenszel 差异项目功能 (MH-DIF) 分析引入 LLM 基准测试的时序可比性检验。基于 METABENCH 响应矩阵 (5,227 模型 × 12,508 MMLU 题目)，对比 2023 与 2024 模型队列，发现 31.3% 的题目呈现大效应 DIF（ETS C 类）。论文开发了基于跨学科匹配 (cross-subject matching) 的半合成注入验证框架，并提出 Monitor/Triage/Correct 审计协议。

## Strengths

**S1. 问题定位精准且重要。** 基准测试的时序可比性在 LLM 评估社区被广泛讨论但缺乏严格量化工具。将心理测量学的 measurement invariance 框架引入 LLM 评估是一个自然但尚未被充分探索的方向，填补了 Growing Pains (Habba et al., 2026) 等工作在诊断粒度上的空白。

**S2. 实验规模与复制性出色。** 5,227 模型、12,508 题目、6 个基准测试的规模在同类工作中罕见。核心发现 (17.9–31.3% C%) 在 TruthfulQA、ARC、HellaSwag、WinoGrande、GSM8K 上均复制成功 (Section 4.7, Table 2)，显著增强了结论的可信度。

**S3. Cross-subject matching 设计巧妙。** 利用非目标学科总分作为匹配变量，在单学科注入下 ΔFPR=0 的构造性保证 (Section 3.4, Remark) 是方法论上的亮点。Figure 5 清晰展示了 cross-subject vs within-subject 匹配在 FPR 控制上的差异，令人信服。

**S4. 控制实验层次丰富。** 能力分位匹配 (C%=2.9% within-cohort, Table 5)、LOFO 家族分析 (Table 8)、随机拆分基线 (0.62%)、IRT θ-conditioning (r=0.9986) 等多层控制从不同角度排除了混淆因素。Section C 的 Simpson's paradox 分析 (logistic regression with DIF-C as dependent variable) 也有力证明了 DIF 信号并非仅由能力差异或题目难度驱动。

**S5. 诊断与行动协议的实用价值。** Section 5.2 提出的 Monitor/Triage/Correct 框架不仅是方法展示，还给出了具体可操作的基准维护建议，增加了论文的实际影响力。

**S6. Figure 1 管线图信息量大。** 四步管线 (response matrix → stratification → MH-DIF → ETS classification) 配合 C%=29.2% 和 stable-item ρ=0.997 的汇总统计，读者可快速把握方法全貌。

## Weaknesses

**W1. [Critical] 标题数字 (31.3%) 未经 DEFF 校正，且校正后区间极宽 (13.5%–29.2%)。** 论文的核心 claim 是 "~29% of items exhibit large temporal DIF"（Abstract, Section 4.2），但这是未经设计效应 (DEFF) 校正的 raw C%。Section D 和 Table 10 显示：简单均值 DEFF 校正后 C%=29.2%，加权均值 DEFF 校正后仅 C%=13.5%，两者相差 2.16 倍。Cluster bootstrap 上界为 53.2%，校正后收敛至 ~27–29%，但这仍依赖于 simple-mean estimator 的选择。论文在 Section 4.2 将此范围表述为 "bracketing C% at 13.5–29.2%"，但 abstract 和 introduction 的措辞 ("31% of items") 强烈暗示了更高端的估计。对于一篇以量化审计为核心贡献的论文，这一不确定性应在 abstract 中明确标注，而非在附录中讨论。
- **具体位置**: Abstract ("31% of items"), Section 4.2, Appendix D (Table 10)
- **为什么影响接收**: 核心量化 claim 的可信区间横跨 2× 范围，削弱了论文的主要贡献

**W2. [Critical] 半合成注入使用均匀二值翻转 (uniform binary flipping)，可能高估检测力。** Section 3.4 将 "contaminated" 项以 20% 均匀概率翻转为正确。现实中的 contamination 效应高度异质：记忆化可能导致某些题目接近天花板、某些仅有微小提升，且不同模型受影响程度不同。Appendix B 的混合机制注入 (Scheme D: difficulty-dependent for base, uniform for instruct) 仅测试了一种替代模式，且仍假设所有被注入题目受到相同强度影响。论文在 Limitations 中承认 "uniform binary response flipping; realistic contamination...would produce weaker DIF signals"，但未量化此高估的程度。
- **具体位置**: Section 3.4 ("flip incorrect→correct at exploration rate ε"), Appendix B, Limitations point (1)
- **建议**: 至少补充一组 graded injection 实验（如 ε 按题目难度衰减、或按模型能力衰减），报告检测力的下降幅度

**W3. [Major] IRT 模型拟合差与参数化 power analysis 之间的张力。** Section A.2 (p11) 明确指出 "the MMLU response matrix shows poor fit to a one-dimensional 2PL model...This does not affect MH-DIF validity, which relies only on total score stratification rather than parametric IRT assumptions." 但 Table 3 的 power analysis 恰恰使用了 2PL 参数 (ā=1.2, various b̄) 来生成模拟数据并估计 TPR。如果真实数据不符合 2PL，那么基于 2PL 模拟的 power 估计的外部效度存疑。论文需要更明确地讨论这一张力：为什么 2PL power analysis 的结论仍可迁移到 non-2PL 的真实数据？
- **具体位置**: Section A.2 ("IRT model fit" paragraph), Table 3
- **建议**: 补充基于 empirical item parameters (而非假设的 2PL) 的 resampling-based power analysis，或明确讨论 2PL misfit 对 power 估计的影响方向

**W4. [Major] Cross-subject ΔFPR=0 保证在多学科污染下退化，且退化速度未充分表征。** Section 3.4 的 Remark 证明单学科注入下 ΔFPR=0，但当 k > 5 个学科同时被污染时，匹配变量 M_i^{-x} 本身被污染。Table 7 (p13) 报告 k=30-50 时 ΔFPR 达到 0.36-0.46。但论文缺少对中间区域 (k=5-15, 更现实的部分污染场景) 的系统表征。此外，MMLU 覆盖 57 个学科，k ≤ 5 的保证仅覆盖不到 9% 的学科，实际应用中污染可能跨越更多学科。
- **具体位置**: Section 3.4 (Remark), Table 7 (p13)
- **建议**: 补充 k=5,8,10,15,20 的 ΔFPR 曲线，明确 "安全区" 的实际范围

**W5. [Major] ETS 阈值从人类考生迁移到 LLM 的合理性缺乏讨论。** ETS 的 A/B/C 分类 (|Δ_MH| < 1.0 / 1.0–1.5 / ≥ 1.5) 是基于人类教育测试群体校准的效应量标准 (Section 3.2 引用 Donoghue & Allen, 1993; Clauser & Mazor, 1998)。LLM 与人类在 item-person 交互模式上有本质差异：(1) LLM 没有真正的 "ability" latent trait，总分仅是聚合正确率；(2) 5,227 个 "考生" 中存在大量高度同质的模型（同架构不同 checkpoint），inflating sample size 但不增加独立信息。论文在 Section A.2 做了 threshold sensitivity 分析 (Table 3)，表明定性结论不依赖特定阈值，但未讨论阈值本身在 LLM 语境下的 substantive meaning（即 |Δ_MH|=1.5 对 LLM 意味着什么实际差异）。
- **具体位置**: Section 3.2 (ETS classification), Section A.2 (threshold sensitivity)
- **建议**: 添加一段讨论 ETS 阈值在 LLM 设定下的实质含义，或提供 data-driven 的阈值校准

**W6. [Moderate] 多重比较校正未作为主方法。** 12,508 个项目同时进行假设检验，即使 per-item α=0.05，预期假阳性也有 ~625 个。论文使用 ETS classification（基于效应量而非 p-value）作为主要分类方法，并在 Section A.2 提到 BH-FDR 校正作为 robustness check (α=0.05)。但 ETS 分类本身也包含显著性条件 (p < 0.05 for Category C)，此 p-value 门槛未做多重校正。Random-split baseline 0.62% 提供了经验性 null 分布，但这是在 random group assignment 下的 FPR，并非在 "no DIF" null 下的 FPR。
- **具体位置**: Section 3.2 (Eq. 1-2), Section A.2 ("Multiple testing" paragraph)
- **建议**: 报告 BH-FDR 校正后的 C% 变化，或更明确地论证 ETS classification 的效应量门槛为什么使 multiple testing correction 不必要

**W7. [Moderate] "近独立于 web-overlap labels" 的推断强度。** Section 4.3 报告 DIF flags 与 web-overlap labels 的 Jaccard=0.206, φ=0.012, p=0.88。论文将此解读为两个信号 "near-independent"。但 Jaccard=0.206 意味着约 20% 的重叠，且 web-overlap labels 本身的覆盖率和准确性存疑 (论文也承认 "web-overlap labels are a proxy for training-set membership...this near-independence could partly reflect noise")。φ=0.012 的低相关更可能反映 web-overlap labels 的噪声而非 DIF 的独立性。这一分析的结论强度被过度解读了——正确的表述应是 "DIF flags 与现有 web-overlap labels 不一致"，而非 "DIF 检测的是不同于 contamination 的信号"。
- **具体位置**: Section 4.3, Figure 2 (right panel caption)
- **建议**: 弱化 "complementary diagnostic dimensions" 的措辞，承认 web-overlap labels 的噪声可能驱动低相关

**W8. [Moderate] Base vs instruct 反向模式 (χ²=562.7) 的机制解释。** Section 4.3 (也见 Appendix O) 报告 base 模型倾向 reference-favoring (64.1%) 而 instruct 模型倾向 focal-favoring (65.6%)。论文将此归因于 "structured capability shifts" 和 "composition shift as the primary driver"。但 base 和 instruct 模型在处理 multiple-choice items 时有系统性差异（如 instruction following, output format），这些差异可能产生 DIF-like 的 artifacts，并非真正的 "differential item functioning"。论文未充分区分 DIF (item-level bias) 与 impact (group-level ability difference) 在 base vs instruct 比较中的含义。
- **具体位置**: Section 4.3 ("base and instruct models exhibit opposite DIF directions, χ²=562.7"), Appendix O
- **建议**: 讨论 base/instruct 的 format sensitivity 作为替代解释

## Questions

**Q1.** Abstract 和 Introduction 使用 "31% of items" 作为核心数字，但 DEFF 校正后下界为 13.5%。作者是否考虑在 abstract 中报告校正后的区间而非原始值？为什么选择 simple-mean DEFF 而非 weighted-mean 作为更保守的估计？

**Q2.** Power analysis (Table 3) 基于 2PL 参数生成模拟数据，但论文承认 MMLU 对 2PL 拟合差。作者能否提供基于实际 item parameters 的 bootstrap power analysis，以验证 parametric power estimates 的外部效度？

**Q3.** Cross-subject matching 的 ΔFPR=0 保证在 k ≤ 5 时成立。在更现实的 k=8-15 污染场景下（如一个 training corpus 覆盖多个 STEM 学科），ΔFPR 的退化曲线是什么形状？Table 7 仅报告了 k=20,30,40,50 的离散点。

**Q4.** 时间分割点选择 (2023 vs 2024) 对 C% 有多大影响？如果改用 calendar-year boundaries 以外的分割（如按 MMLU release date 之前/之后），结果是否稳健？论文在 Section 4.2 提到 "Calendar-year boundaries are coarse; half-yearly comparison C% = 34.1%"——这一更高的 C% 是否暗示时间粒度越细 DIF 越大？

**Q5.** 5,227 个模型中有大量来自同一架构家族的变体（如 Llama 系列有 N=547, Mistral N=308）。这些高度同质的模型是否 inflate 了 MH 统计量的显著性？DEFF 校正是否充分处理了这种 within-family correlation？

**Q6.** Ability-quintile 控制 (Table 5) 显示 C% 未显著下降，但 within-subject DIF 仅在 5 个代表性学科上测试。如果在全部 57 个学科上执行 within-subject DIF，结果是否一致？

**Q7.** Section H 的 item-property predictive analysis (logistic regression + LightGBM) 得到 AUROC ≈ 0.60，表明题目特征对 DIF susceptibility 的预测力很弱。这是否意味着 DIF 主要由模型端因素（而非题目端因素）驱动？这对 "Monitor/Triage/Correct" 协议中基于题目属性的预筛选有何影响？

## Missing References

1. **Computerized Adaptive Testing (CAT) for LLMs**: 近期有工作将 CAT 引入 LLM 评估 (如 Zhuang et al., 2023, "Efficiently Measuring the Cognitive Ability of LLMs")，这与本文的 item-level analysis 相关但未被引用。

2. **Test security / item exposure literature**: 教育测量学中关于 item exposure 和 test security 的文献（如 van der Linden & Veldkamp, 2007）与 benchmark contamination 有直接对应关系。

3. **Recent IRT-based LLM evaluation**: Polo et al. (2024) "tinyBenchmarks" 被引用，但 Vania et al. (2021, "Comparing Test Sets with Item Response Theory") 等更早的 NLP+IRT 工作可能也相关。

## Minor Issues

- **M1.** Figure 3 的 x 轴标签 "Δ_MH" 的下标 "MH" 在图中字体较小，建议放大。
- **M2.** Table 1 (p7) 的 "Enrichment" 列缺少 HellaSwag 和部分基准的数据（标 "–"），应说明原因。
- **M3.** Section 4.1 提到 "1,000 replications" 但未报告 seed 或 random number generator。
- **M4.** Appendix 标签从 A 到 Q (17 个)，总量较大。考虑合并部分相关性强的 appendix 以提高可读性。
- **M5.** Abstract 第一句 "Every leaderboard comparison assumes that benchmark items measure the same construct across model generations" 略显绝对——部分排行榜 (如 Chatbot Arena) 使用 ELO 而非固定题目。

## Overall Assessment

**Overall**: 3.5 (Borderline Conference)
**Soundness**: 3/5 — 方法论框架合理，但 DEFF 校正后核心数字的 2× 不确定性 (13.5%–29.2%) 以及 2PL power analysis 与模型拟合差之间的张力削弱了量化 claims 的可信度。半合成注入的均匀翻转假设可能高估检测力。
**Excitement**: 3.5/5 — 将 MH-DIF 引入 LLM 评估是一个有价值的方法论贡献，问题重要且及时。但论文更偏向诊断工具展示而非深层机制发现，excitement 受限。
**Reproducibility**: 4/5 — 代码和数据公开（脚注 1），附录详尽，但 power analysis 的具体实现细节（random seed, simulation code）未完全提供。
**Confidence**: 4/5 — 我熟悉 DIF 方法论和 LLM 评估文献，仔细阅读了全文和附录。

**简要理由**: 论文选题好、规模大、控制实验多层次，但核心量化 claim 的不确定性 (DEFF 13.5%–29.2%) 在 abstract/intro 中被淡化，半合成注入的 uniform flipping 假设可能高估检测力，且论文未充分解决 ETS 阈值从人类教育测试迁移到 LLM 的 substantive meaning 问题。如果作者能 (1) 在 abstract 中坦诚报告 DEFF 校正后的区间，(2) 补充 graded injection 实验，(3) 更明确讨论 IRT misfit 对 power analysis 的影响，论文将达到 Conference 水平 (4.0)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1763 · 2026-05-25T21:22:59.490151+00:00_

Reviewer 1 审稿意见已收到。等待 Reviewer 2 提交后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 170

## Round 170

2 recorded events


### User

_source line 1764 · 2026-05-25T21:23:02.065048+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

**审稿完成摘要**：

- **Overall**: 3.5 (Borderline Conference)
- **核心优势**: 问题定位精准、规模大 (5,227 models × 12,508 items × 6 benchmarks)、cross-subject matching 设计巧妙、控制实验层次丰富
- **主要问题**:
  - **W1 [Critical]**: 标题数字 31.3% 未经 DEFF 校正，校正后区间 13.5%–29.2% 横跨 2× 
  - **W2 [Critical]**: 均匀二值翻转注入可能高估检测力
  - **W3 [Major]**: 2PL power analysis 与 IRT 模型拟合差之间的张力
  - **W4 [Major]**: Cross-subject ΔFPR=0 保证在多学科污染 (k>5) 下退化
  - **W5 [Major]**: ETS 阈值从人类迁移到 LLM 缺乏实质含义讨论
- **提升路径**: 在 abstract 中坦诚报告 DEFF 区间、补充 graded injection 实验、讨论 IRT misfit 影响，可达 4.0 (Conference)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1765 · 2026-05-25T21:23:12.753092+00:00_

Reviewer 1 审稿已收到。评分 3.5 (Borderline Conference)，提出 2 个 Critical + 3 个 Major weakness。等待 Reviewer 2 完成后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 171

## Round 171

6 recorded events


### User

_source line 1766 · 2026-05-25T21:24:17.299616+00:00_

[Reviewer 2 审稿意见]:
## Summary

本文将教育测量中的 Mantel-Haenszel 差异项目功能（DIF）分析应用于 METABENCH 响应矩阵（5,227 个模型 × 12,508 个 MMLU 题目），发现 2023 与 2024 模型群组之间约 31% 的题目表现出显著的时间性 DIF（ETS Category C），且该信号与 web-overlap 污染标签近乎独立（φ = 0.012）。论文提出了 cross-subject matching 以控制 FPR，在六个基准上复现了发现，并提出了 Monitor/Triage/Correct 审计协议。

## Strengths

**S1. 大规模、系统性的实证分析。** 5,227 个模型 × 12,508 个题目的分析规模令人印象深刻，在六个基准上复现（C% 从 17.9% 到 31.3%，Table 2）增强了可信度。据我所知，这确实是目前最大规模的 LLM 基准 DIF 分析。

**S2. 多层次验证设计严谨。** 论文构建了五种 cohort 对比（temporal、ability-quintile、within-family、within-subject、random split；Section 3.3），辅以 DEFF 校正、cluster bootstrap、LOFO 分析和多阈值敏感性检验。Random split 的 0.62% C% 与 temporal 的 31.3% 形成 50× 对比，有力排除了随机噪声解释。

**S3. Cross-subject matching 的 ΔFPR = 0 保证有理论和实证价值。** 将 purified subtest matching 适配到 LLM 多学科场景，并在 Remark (Section 3.4) 中提供了构造性论证，Figure 5 直观展示了 within-subject matching 的 FPR 膨胀问题。这是对心理测量方法在 LLM 场景下适配的有意义贡献。

**S4. DIF vs. contamination 的区分具有概念洞察力。** Figure 2 通过 ICC 曲线清晰展示了 global exposure 与 differential functioning 的区别，这一概念框架对 NLP 评估社区有教育意义。Jaccard = 0.206、φ = 0.012 的实证结果支持了两者的互补性。

**S5. 对 NLP 读者的心理测量概念解释充分。** Section 3.2 对 MH 程序、ETS 分类、匹配变量选择的解释清晰，包括公式推导（Eq. 1-2）和 LLM 特有挑战的讨论。

**S6. Base-vs-instruct 方向反转是有价值的发现。** χ² = 562.7 的结构化方向性差异（Section 5.1：base 60.1% reference-favoring vs. instruct 65.6% focal-favoring）超越了简单的"有/无 DIF"二分法，指向训练方法论对测量特性的系统性影响。

## Weaknesses

**W1. [Critical] 标题"Score Incomparability"与核心发现之间存在根本性叙事张力。** 标题暗示分数不可比较，但论文最核心的实证发现恰恰是 ρ ≈ 0.997（Table 2，所有六个基准 ρ ≥ 0.994）——排名几乎完美保持。Section 4.5 明确指出 stable-item ranks are preserved。这造成了一个困境：如果 31% 的题目有 DIF 但排名不变，那么"incomparability"这一措辞是否过度？论文实际展示的是 item-level instability with aggregate robustness，但标题设置的期望与实际发现不匹配。Introduction 中 "The result is sobering" 的措辞进一步放大了这一不匹配——如果排名稳定，这一发现究竟有多"sobering"？建议标题更准确地反映论文的细致发现，如 "Temporal Differential Item Functioning" 或 "Item-Level Instability"。

**W2. [Critical] 方法论新颖性有限——核心方法均为已知技术的直接应用。** MH-DIF 是 1988 年的标准方法（Holland & Thayer）；ETS A/B/C 分类是标准实践；cross-subject matching 是 purified subtest matching（Swaminathan & Rogers, 1990）的直接适配；DEFF 校正来自 Rao & Scott (1992)。论文的主要方法论贡献是将这些已知工具组合应用到 LLM 评估场景——这是有价值的应用性工作，但 NLP 顶会对方法论创新的要求通常高于"已知方法到新领域的迁移"。论文在 Section 3.2 讨论了四个 LLM-specific challenges，但每个的解决方案都是现有方法（permutation simulation、DEFF、quintile stratification、cross-subject matching），没有提出针对 LLM 特殊性的新统计方法。

**W3. [Major] 关键发现 C% 的不确定性范围过大（13.5%–31.3%），削弱了结论的精确度。** Section 4.2 报告 DEFF 校正后 C% 在 13.5%（weighted-mean DEFF）到 29.2%（simple-mean DEFF）之间，未校正值为 31.3%。这是一个 2.3× 的范围。论文论证 weighted-mean over-corrects（因为 cluster bootstrap CI excludes weighted-mean estimate），但这一论证不完全令人信服——cluster bootstrap 本身依赖于 family 定义的合理性，而 model family 边界（什么算一个 family？微调变体 vs. 不同训练配方）是模糊的。如果真实 C% 接近 13.5% 而非 31%，论文的许多结论（如"50× above random"、"sobering"等）需要显著弱化。

**W4. [Major] "Mechanism-agnostic"定位与论文内容之间存在紧张关系。** 论文反复强调 DIF 是 mechanism-agnostic（Section 3.4, 5.1），但大量篇幅用于 contamination 分析：Section 4.3 与 web-overlap labels 对比、Section 3.4 使用 contamination injection 作为唯一验证方法、Section 5.1 讨论 base-vs-instruct 与 contamination 的关系。如果 DIF 真的是 mechanism-agnostic，为什么验证框架完全基于 contamination？一个更强的验证应包括其他可能驱动 DIF 的机制（如训练方法变化、数据分布偏移）的模拟。当前验证仅覆盖一种可能的 DIF 机制，作为 mechanism-agnostic 工具的评估并不完整。

**W5. [Major] 缺少对 DIF 在 LLM 场景下概念合法性的深入讨论。** 在教育测量中，DIF 检测的是对同等能力的不同人群的 item bias——关注的是公平性。在 LLM 场景中，2023 vs. 2024 模型不是同一总体的人口学子群，而是技术上根本不同的系统。当我们将 2024 模型与同总分的 2023 模型匹配时，"同总分"的含义可能完全不同（不同的能力剖面得到相同总分）。论文在 Section 3.2 承认了多维性问题（Cohen's d range = 0.12, κ = 0.80），但 κ = 0.80 意味着 20% 的 DIF 项目可能是多维性伪影而非真正的 measurement invariance violation。论文需要更明确地讨论：在什么条件下，LLM temporal DIF 反映的是测量问题（item 有问题），vs. 反映的是被测对象的合法能力结构变化（model 本来就不同）。

**W6. [Minor] 三个 contribution 的权重不均衡。** Contribution 1（empirical finding）是论文的主要价值；Contribution 2（cross-subject matching）是已知方法的适配；Contribution 3（audit protocol）在 Section 5.2 中仅占半段，没有任何部署验证。将 audit protocol 列为正式 contribution 时，缺乏证据支撑其实用性——没有 benchmark maintainer 参与验证，没有 case study 展示协议的实际运作。

## Questions

**Q1.** 既然 ρ ≈ 0.997 且排名几乎完全保持，能否更精确地量化 temporal DIF 的实际危害？Section 4.5 提到 DIF-corrected scoring shifts accuracy by +2.12 pp，但这是平均值——对具体模型/评估决策的影响有多大？在什么场景下，一个 practitioner 会因为忽略 temporal DIF 而做出错误决策？

**Q2.** 论文使用 2023 vs. 2024 的 calendar-year boundary 作为主要对比。这一划分必然混合了多种变化源（架构演进、训练数据扩展、RLHF 方法改进、数据清洗实践变化等）。是否考虑过更细粒度的时间划分（如季度），以及 DIF 信号是逐渐积累还是存在突变点？Section 3.3 提到 half-yearly C% = 34.4%，但没有详细分析时间动态。

**Q3.** Base-vs-instruct 方向反转（χ² = 562.7）本身可能部分反映了 RLHF/instruction tuning 对答题策略的系统性改变（如更倾向选择"安全"选项、改变猜测行为），而非 item-level measurement invariance violation。如何区分"训练方法改变了模型的合法能力剖面"与"训练方法导致了 item 测量特性的扭曲"？

**Q4.** Cross-subject matching 在 contamination 影响 ≤5 个 subject 时保证 ΔFPR ≈ 0，但论文未讨论当 DIF 由非 contamination 因素（如全局训练方法变化）驱动时，cross-subject matching 的行为。如果所有 subject 同时受到训练方法变化的影响，cross-subject matching 的保护机制是否仍然有效？

## Missing References

**M1. Rodriguez et al. (2021) "Evaluation Examples Are Not Equally Informative: How Should That Change NLP Leaderboards?" (ACL 2021).** 这是 IRT 应用于 NLP 评估的奠基性工作之一，使用贝叶斯 IRT 模型分析 NLP leaderboard 的可靠性、标注决策和过拟合检测。与本文在"心理测量方法改进 NLP 评估"这一主题上高度相关，但未被引用。论文引用了 Lalor et al. (2019) 作为 IRT 在 NLP 中的引入，但跳过了 Rodriguez et al. 这一重要中间节点。

**M2. Polo et al. (2024) "tinyBenchmarks: Evaluating LLMs with Fewer Examples" (ICML 2024).** 使用 IRT 进行高效 LLM 评估，与本文的心理测量方法论主题直接相关。

**M3.** 论文讨论了 Growing Pains (Habba et al., 2026) 作为最接近的并发工作，但可能遗漏了 2025 年的 PSN-IRT 后续工作或其他 IRT+LLM 评估的最新进展（如 "Lost in Benchmarks? Rethinking Large Language Model Benchmarking with IRT"）。

## Minor Issues

**m1.** Abstract 脚注中的匿名链接 `anonymous.4open.science` 格式正确，匿名性保持完好。

**m2.** Section 3.2 中 "At N = 1,887... significance (p < 0.05) is nearly automatically satisfied for any |Δ_MH| ≥ 1.5: only 3 of 3,918 C items lack significance" —— 这实际上意味着在如此大的 N 下，ETS C 的双重阈值实质上退化为单一效应量阈值。这削弱了"dual threshold guards against false positives"的论点，值得在正文中更坦诚地承认（而非仅在同句后半部分轻描淡写）。

**m3.** Figure 4（dose-response）的 y 轴标签 "ΔTPR" 在 baseline 区域（p = 0.0）的误差条显示非零值——建议说明 baseline ΔTPR 的期望值和实际分布。

**m4.** Table 1 的 "Enrichment" 列标题可进一步明确定义（首次出现在 Table caption 中才解释为 "ratio of observed to expected overlap"）。

**m5.** Section 4.2 最后一段 "DIF rates are domain-invariant (Kruskal-Wallis p = 0.78)" 与 "DIF direction exhibits domain dependence: STEM items favor 2024 models (55.4%), Humanities favor 2023 (64.4%)" 的并置可能让读者困惑——rate invariant 但 direction dependent 的区别需要更清晰地铺垫。

**m6.** 正文在第 8 页结束（Section 6 Conclusion + Section 5 Discussion），Limitations 在第 9 页，符合 8 页限制。References 格式符合 ACL 规范。

**m7.** Conclusion（Section 6）非常简短（仅一句话），在信息密度上可以接受但可能给 reviewer 留下仓促收尾的印象。

## Overall Assessment

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 4 / 5 | 方法论执行扎实，多重控制和验证设计严谨；但 C% 的 13.5-31.3% 不确定性范围和多维性伪影问题（κ=0.80）是显著缺口 |
| Excitement | 3 / 5 | 将心理测量方法引入 LLM 评估有价值，但核心方法为已知技术组合，实际影响有限（ρ≈0.997 意味着排名不变） |
| Confidence | 4 / 5 | 我仔细阅读了全文（含 16 页附录），熟悉 DIF 方法论和 LLM 评估文献 |

**Overall: 3.5 (Borderline Conference)**

这是一篇执行质量高的实证论文，分析规模大、验证设计严谨、对 NLP 读者的概念解释清晰。核心发现（~29-31% temporal DIF, near-independence from contamination, base-vs-instruct reversal）是有价值的诊断洞察。

主要顾虑在于：(1) 方法论新颖性有限——全部核心方法均为教育测量中 30+ 年历史的标准工具的直接应用/适配，NLP 方法论贡献不足以达到 conference 水平；(2) 标题暗示的"不可比较性"与 ρ ≈ 0.997 的发现之间存在叙事过度，practical impact 不清晰；(3) C% 的大范围不确定性（2.3×）使核心结论的精确度受限。论文作为 Findings 论文完全达标，但升入主会议需要在新颖性或实际影响上有更强的论证。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1767 · 2026-05-25T21:25:18.171931+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "text": "## 交叉分享 — Reviewer 1 的完整审稿意见\n\n以下是 Reviewer 1 的完整审稿原文。请逐条回应每个 Weakness 和 Question：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n## Reviewer 1 原文\n\n### Strengths\n\n**S1. 问题定位精准且重要。** 基准测试的时序可比性在 LLM 评估社区被广泛讨论但缺乏严格量化工具。将心理测量学的 measurement invariance 框架引入 LLM 评估是一个自然但尚未被充分探索的方向，填补了 Growing Pains (Habba et al., 2026) 等工作在诊断粒度上的空白。\n\n**S2. 实验规模与复制性出色。** 5,227 模型、12,508 题目、6 个基准测试的规模在同类工作中罕见。核心发现 (17.9–31.3% C%) 在 TruthfulQA、ARC、HellaSwag、WinoGrande、GSM8K 上均复制成功 (Section 4.7, Table 2)，显著增强了结论的可信度。\n\n**S3. Cross-subject matching 设计巧妙。** 利用非目标学科总分作为匹配变量，在单学科注入下 ΔFPR=0 的构造性保证 (Section 3.4, Remark) 是方法论上的亮点。Figure 5 清晰展示了 cross-subject vs within-subject 匹配在 FPR 控制上的差异，令人信服。\n\n**S4. 控制实验层次丰富。** 能力分位匹配 (C%=2.9% within-cohort, Table 5)、LOFO 家族分析 (Table 8)、随机拆分基线 (0.62%)、IRT θ-conditioning (r=0.9986) 等多层控制从不同角度排除了混淆因素。\n\n**S5. 诊断与行动协议的实用价值。** Section 5.2 提出的 Monitor/Triage/Correct 框架不仅是方法展示，还给出了具体可操作的基准维护建议，增加了论文的实际影响力。\n\n**S6. Figure 1 管线图信息量大。**\n\n### Weaknesses\n\n**W1. [Critical] 标题数字 (31.3%) 未经 DEFF 校正，且校正后区间极宽 (13.5%–29.2%)。** 论文的核心 claim 是 \"~29% of items exhibit large temporal DIF\"（Abstract, Section 4.2），但这是未经设计效应 (DEFF) 校正的 raw C%。Section D 和 Table 10 显示：简单均值 DEFF 校正后 C%=29.2%，加权均值 DEFF 校正后仅 C%=13.5%，两者相差 2.16 倍。Cluster bootstrap 上界为 53.2%，校正后收敛至 ~27–29%，但这仍依赖于 simple-mean estimator 的选择。论文在 Section 4.2 将此范围表述为 \"bracketing C% at 13.5–29.2%\"，但 abstract 和 introduction 的措辞 (\"31% of items\") 强烈暗示了更高端的估计。\n\n**W2. [Critical] 半合成注入使用均匀二值翻转 (uniform binary flipping)，可能高估检测力。** Section 3.4 将 \"contaminated\" 项以 20% 均匀概率翻转为正确。现实中的 contamination 效应高度异质。Appendix B 的混合机制注入仅测试了一种替代模式，且仍假设所有被注入题目受到相同强度影响。\n\n**W3. [Major] IRT 模型拟合差与参数化 power analysis 之间的张力。** Section A.2 明确指出 MMLU 对 2PL 拟合差，但 Table 3 的 power analysis 恰恰使用了 2PL 参数来生成模拟数据并估计 TPR。\n\n**W4. [Major] Cross-subject ΔFPR=0 保证在多学科污染下退化，且退化速度未充分表征。** Table 7 报告 k=30-50 时 ΔFPR 达到 0.36-0.46。但论文缺少对中间区域 (k=5-15) 的系统表征。\n\n**W5. [Major] ETS 阈值从人类考生迁移到 LLM 的合理性缺乏讨论。** LLM 与人类在 item-person 交互模式上有本质差异：LLM 没有真正的 \"ability\" latent trait；5,227 个 \"考生\" 中存在大量高度同质的模型。\n\n**W6. [Moderate] 多重比较校正未作为主方法。** 12,508 个项目同时进行假设检验，ETS C 的 p-value 门槛未做多重校正。\n\n**W7. [Moderate] \"近独立于 web-overlap labels\" 的推断强度。** φ=0.012 的低相关更可能反映 web-overlap labels 的噪声而非 DIF 的独立性。\n\n**W8. [Moderate] Base vs instruct 反向模式的机制解释。** base 和 instruct 模型在处理 MCQ 时有系统性差异（如 instruction following, output format），这些差异可能产生 DIF-like 的 artifacts。\n\n### Questions\nQ1-Q7 见上文（关于 DEFF 报告、2PL power analysis、多学科 ΔFPR 曲线、时间分割点影响、family correlation 处理、within-subject DIF 全量验证、item-property 预测力的含义）\n\n### Missing References\n1. CAT for LLMs (Zhuang et al., 2023)\n2. Test security / item exposure literature (van der Linden & Veldkamp, 2007)\n3. Vania et al. (2021, \"Comparing Test Sets with Item Response Theory\")\n\n---\n\n请对以上每个 Weakness (W1-W8) 和 Questions (Q1-Q7) 逐条给出 [AGREE] 或 [REBUT] 回应。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "text": "## 交叉分享 — Reviewer 1 的完整审稿意见\n\n以下是 Reviewer 1 的完整审稿原文。请逐条回应每个 Weakness 和 Question：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n## Reviewer 1 原文\n\n### Strengths\n\n**S1. 问题定位精准且重要。** 基准测试的时序可比性在 LLM 评估社区被广泛讨论但缺乏严格量化工具。将心理测量学的 measurement invariance 框架引入 LLM 评估是一个自然但尚未被充分探索的方向，填补了 Growing Pains (Habba et al., 2026) 等工作在诊断粒度上的空白。\n\n**S2. 实验规模与复制性出色。** 5,227 模型、12,508 题目、6 个基准测试的规模在同类工作中罕见。核心发现 (17.9–31.3% C%) 在 TruthfulQA、ARC、HellaSwag、WinoGrande、GSM8K 上均复制成功 (Section 4.7, Table 2)，显著增强了结论的可信度。\n\n**S3. Cross-subject matching 设计巧妙。** 利用非目标学科总分作为匹配变量，在单学科注入下 ΔFPR=0 的构造性保证 (Section 3.4, Remark) 是方法论上的亮点。Figure 5 清晰展示了 cross-subject vs within-subject 匹配在 FPR 控制上的差异，令人信服。\n\n**S4. 控制实验层次丰富。** 能力分位匹配 (C%=2.9% within-cohort, Table 5)、LOFO 家族分析 (Table 8)、随机拆分基线 (0.62%)、IRT θ-conditioning (r=0.9986) 等多层控制从不同角度排除了混淆因素。\n\n**S5. 诊断与行动协议的实用价值。** Section 5.2 提出的 Monitor/Triage/Correct 框架不仅是方法展示，还给出了具体可操作的基准维护建议，增加了论文的实际影响力。\n\n**S6. Figure 1 管线图信息量大。**\n\n### Weaknesses\n\n**W1. [Critical] 标题数字 (31.3%) 未经 DEFF 校正，且校正后区间极宽 (13.5%–29.2%)。** 论文的核心 claim 是 \"~29% of items exhibit large temporal DIF\"（Abstract, Section 4.2），但这是未经设计效应 (DEFF) 校正的 raw C%。Section D 和 Table 10 显示：简单均值 DEFF 校正后 C%=29.2%，加权均值 DEFF 校正后仅 C%=13.5%，两者相差 2.16 倍。Cluster bootstrap 上界为 53.2%，校正后收敛至 ~27–29%，但这仍依赖于 simple-mean estimator 的选择。论文在 Section 4.2 将此范围表述为 \"bracketing C% at 13.5–29.2%\"，但 abstract 和 introduction 的措辞 (\"31% of items\") 强烈暗示了更高端的估计。\n\n**W2. [Critical] 半合成注入使用均匀二值翻转 (uniform binary flipping)，可能高估检测力。** Section 3.4 将 \"contaminated\" 项以 20% 均匀概率翻转为正确。现实中的 contamination 效应高度异质。Appendix B 的混合机制注入仅测试了一种替代模式，且仍假设所有被注入题目受到相同强度影响。\n\n**W3. [Major] IRT 模型拟合差与参数化 power analysis 之间的张力。** Section A.2 明确指出 MMLU 对 2PL 拟合差，但 Table 3 的 power analysis 恰恰使用了 2PL 参数来生成模拟数据并估计 TPR。\n\n**W4. [Major] Cross-subject ΔFPR=0 保证在多学科污染下退化，且退化速度未充分表征。** Table 7 报告 k=30-50 时 ΔFPR 达到 0.36-0.46。但论文缺少对中间区域 (k=5-15) 的系统表征。\n\n**W5. [Major] ETS 阈值从人类考生迁移到 LLM 的合理性缺乏讨论。** LLM 与人类在 item-person 交互模式上有本质差异：LLM 没有真正的 \"ability\" latent trait；5,227 个 \"考生\" 中存在大量高度同质的模型。\n\n**W6. [Moderate] 多重比较校正未作为主方法。** 12,508 个项目同时进行假设检验，ETS C 的 p-value 门槛未做多重校正。\n\n**W7. [Moderate] \"近独立于 web-overlap labels\" 的推断强度。** φ=0.012 的低相关更可能反映 web-overlap labels 的噪声而非 DIF 的独立性。\n\n**W8. [Moderate] Base vs instruct 反向模式的机制解释。** base 和 instruct 模型在处理 MCQ 时有系统性差异（如 instruction following, output format），这些差异可能产生 DIF-like 的 artifacts。\n\n### Questions\nQ1-Q7 见上文（关于 DEFF 报告、2PL power analysis、多学科 ΔFPR 曲线、时间分割点影响、family correlation 处理、within-subject DIF 全量验证、item-property 预测力的含义）\n\n### Missing References\n1. CAT for LLMs (Zhuang et al., 2023)\n2. Test security / item exposure literature (van der Linden & Veldkamp, 2007)\n3. Vania et al. (2021, \"Comparing Test Sets with Item Response Theory\")\n\n---\n\n请对以上每个 Weakness (W1-W8) 和 Questions (Q1-Q7) 逐条给出 [AGREE] 或 [REBUT] 回应。"
  }
}
```

</details>

---


### Tool result

_source line 1768 · 2026-05-25T21:25:51.737580+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 33565
}
```

</details>

---


### Tool call

_source line 1769 · 2026-05-25T21:25:51.838575+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "text": "## 交叉分享 — Reviewer 2 的完整审稿意见\n\n以下是 Reviewer 2 的完整审稿原文。请逐条回应每个 Weakness 和 Question：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n  \n---\n\n## Reviewer 2 原文\n\n### Strengths\n\n**S1. 大规模、系统性的实证分析。** 5,227 个模型 × 12,508 个题目的分析规模令人印象深刻，在六个基准上复现增强了可信度。\n\n**S2. 多层次验证设计严谨。** 五种 cohort 对比 + DEFF 校正 + cluster bootstrap + LOFO 分析 + 多阈值敏感性检验。Random split 的 0.62% C% 与 temporal 的 31.3% 形成 50× 对比。\n\n**S3. Cross-subject matching 的 ΔFPR = 0 保证有理论和实证价值。**\n\n**S4. DIF vs. contamination 的区分具有概念洞察力。** Figure 2 通过 ICC 曲线清晰展示了 global exposure 与 differential functioning 的区别。\n\n**S5. 对 NLP 读者的心理测量概念解释充分。**\n\n**S6. Base-vs-instruct 方向反转是有价值的发现。**\n\n### Weaknesses\n\n**W1. [Critical] 标题\"Score Incomparability\"与核心发现之间存在根本性叙事张力。** 标题暗示分数不可比较，但核心发现是 ρ ≈ 0.997——排名几乎完美保持。如果 31% 的题目有 DIF 但排名不变，那么\"incomparability\"这一措辞是否过度？论文实际展示的是 item-level instability with aggregate robustness，但标题设置的期望与实际发现不匹配。Introduction 中 \"The result is sobering\" 的措辞进一步放大了不匹配。\n\n**W2. [Critical] 方法论新颖性有限——核心方法均为已知技术的直接应用。** MH-DIF (1988)、ETS A/B/C 分类、cross-subject matching (purified subtest matching 1990)、DEFF 校正 (1992)。论文的四个 LLM-specific challenges 的解决方案都是现有方法，没有提出针对 LLM 特殊性的新统计方法。\n\n**W3. [Major] C% 的不确定性范围过大（13.5%–31.3%）。** 2.3× 的范围。Cluster bootstrap 依赖于 family 定义的合理性。如果真实 C% 接近 13.5%，论文的许多结论需要显著弱化。\n\n**W4. [Major] \"Mechanism-agnostic\"定位与论文内容之间存在紧张关系。** 大量篇幅用于 contamination 分析，但声称 mechanism-agnostic。如果 DIF 真的是 mechanism-agnostic，为什么验证框架完全基于 contamination？\n\n**W5. [Major] 缺少对 DIF 在 LLM 场景下概念合法性的深入讨论。** 2023 vs. 2024 模型不是同一总体的人口学子群，而是技术上根本不同的系统。κ = 0.80 意味着 20% 的 DIF 项目可能是多维性伪影。\n\n**W6. [Minor] 三个 contribution 的权重不均衡。** Contribution 3（audit protocol）在 Section 5.2 中仅占半段，没有部署验证。\n\n### Questions\n\n**Q1.** 既然 ρ ≈ 0.997，能否更精确地量化 temporal DIF 的实际危害？在什么场景下 practitioner 会因忽略 temporal DIF 而做出错误决策？\n\n**Q2.** 2023 vs 2024 calendar-year boundary 混合了多种变化源。是否考虑过更细粒度的时间划分？DIF 信号是逐渐积累还是存在突变点？\n\n**Q3.** Base-vs-instruct 方向反转可能部分反映 RLHF/instruction tuning 对答题策略的系统性改变。如何区分\"训练方法改变了模型的合法能力剖面\"与\"训练方法导致了 item 测量特性的扭曲\"？\n\n**Q4.** 当 DIF 由非 contamination 因素（如全局训练方法变化）驱动时，cross-subject matching 的行为如何？\n\n### Missing References\n\n**M1.** Rodriguez et al. (2021) \"Evaluation Examples Are Not Equally Informative\" (ACL 2021) — IRT 应用于 NLP 评估的奠基性工作。\n**M2.** Polo et al. (2024) \"tinyBenchmarks\" (ICML 2024)。\n**M3.** 2025 年 PSN-IRT 后续工作或 \"Lost in Benchmarks?\" 等最新 IRT+LLM 工作。\n\n---\n\n请对以上每个 Weakness (W1-W6) 和 Questions (Q1-Q4) 逐条给出 [AGREE] 或 [REBUT] 回应。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "text": "## 交叉分享 — Reviewer 2 的完整审稿意见\n\n以下是 Reviewer 2 的完整审稿原文。请逐条回应每个 Weakness 和 Question：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n  \n---\n\n## Reviewer 2 原文\n\n### Strengths\n\n**S1. 大规模、系统性的实证分析。** 5,227 个模型 × 12,508 个题目的分析规模令人印象深刻，在六个基准上复现增强了可信度。\n\n**S2. 多层次验证设计严谨。** 五种 cohort 对比 + DEFF 校正 + cluster bootstrap + LOFO 分析 + 多阈值敏感性检验。Random split 的 0.62% C% 与 temporal 的 31.3% 形成 50× 对比。\n\n**S3. Cross-subject matching 的 ΔFPR = 0 保证有理论和实证价值。**\n\n**S4. DIF vs. contamination 的区分具有概念洞察力。** Figure 2 通过 ICC 曲线清晰展示了 global exposure 与 differential functioning 的区别。\n\n**S5. 对 NLP 读者的心理测量概念解释充分。**\n\n**S6. Base-vs-instruct 方向反转是有价值的发现。**\n\n### Weaknesses\n\n**W1. [Critical] 标题\"Score Incomparability\"与核心发现之间存在根本性叙事张力。** 标题暗示分数不可比较，但核心发现是 ρ ≈ 0.997——排名几乎完美保持。如果 31% 的题目有 DIF 但排名不变，那么\"incomparability\"这一措辞是否过度？论文实际展示的是 item-level instability with aggregate robustness，但标题设置的期望与实际发现不匹配。Introduction 中 \"The result is sobering\" 的措辞进一步放大了不匹配。\n\n**W2. [Critical] 方法论新颖性有限——核心方法均为已知技术的直接应用。** MH-DIF (1988)、ETS A/B/C 分类、cross-subject matching (purified subtest matching 1990)、DEFF 校正 (1992)。论文的四个 LLM-specific challenges 的解决方案都是现有方法，没有提出针对 LLM 特殊性的新统计方法。\n\n**W3. [Major] C% 的不确定性范围过大（13.5%–31.3%）。** 2.3× 的范围。Cluster bootstrap 依赖于 family 定义的合理性。如果真实 C% 接近 13.5%，论文的许多结论需要显著弱化。\n\n**W4. [Major] \"Mechanism-agnostic\"定位与论文内容之间存在紧张关系。** 大量篇幅用于 contamination 分析，但声称 mechanism-agnostic。如果 DIF 真的是 mechanism-agnostic，为什么验证框架完全基于 contamination？\n\n**W5. [Major] 缺少对 DIF 在 LLM 场景下概念合法性的深入讨论。** 2023 vs. 2024 模型不是同一总体的人口学子群，而是技术上根本不同的系统。κ = 0.80 意味着 20% 的 DIF 项目可能是多维性伪影。\n\n**W6. [Minor] 三个 contribution 的权重不均衡。** Contribution 3（audit protocol）在 Section 5.2 中仅占半段，没有部署验证。\n\n### Questions\n\n**Q1.** 既然 ρ ≈ 0.997，能否更精确地量化 temporal DIF 的实际危害？在什么场景下 practitioner 会因忽略 temporal DIF 而做出错误决策？\n\n**Q2.** 2023 vs 2024 calendar-year boundary 混合了多种变化源。是否考虑过更细粒度的时间划分？DIF 信号是逐渐积累还是存在突变点？\n\n**Q3.** Base-vs-instruct 方向反转可能部分反映 RLHF/instruction tuning 对答题策略的系统性改变。如何区分\"训练方法改变了模型的合法能力剖面\"与\"训练方法导致了 item 测量特性的扭曲\"？\n\n**Q4.** 当 DIF 由非 contamination 因素（如全局训练方法变化）驱动时，cross-subject matching 的行为如何？\n\n### Missing References\n\n**M1.** Rodriguez et al. (2021) \"Evaluation Examples Are Not Equally Informative\" (ACL 2021) — IRT 应用于 NLP 评估的奠基性工作。\n**M2.** Polo et al. (2024) \"tinyBenchmarks\" (ICML 2024)。\n**M3.** 2025 年 PSN-IRT 后续工作或 \"Lost in Benchmarks?\" 等最新 IRT+LLM 工作。\n\n---\n\n请对以上每个 Weakness (W1-W6) 和 Questions (Q1-Q4) 逐条给出 [AGREE] 或 [REBUT] 回应。"
  }
}
```

</details>

---


### Tool result

_source line 1770 · 2026-05-25T21:25:53.195154+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_f025582a920d3f79beb59dfc17929017:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1356
}
```

</details>

---


### Assistant

_source line 1771 · 2026-05-25T21:25:57.602056+00:00_

交叉分享已发出，等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 172

## Round 172

2 recorded events


### User

_source line 1772 · 2026-05-25T21:26:00.141955+00:00_

[Reviewer 2 审稿结果]:
Round 1 审稿完成。已向 Review Director 提交完整审稿意见，核心评判：

- **Overall: 3.5（Borderline Conference）**
- **Soundness: 4/5** — 方法执行扎实，多重验证设计严谨
- **Excitement: 3/5** — 核心方法为已知技术组合，practical impact 受限于 ρ≈0.997

主要问题集中在三点：(1) 标题 "Score Incomparability" 与排名近乎完美保持的发现存在叙事过度；(2) 方法论新颖性有限（MH-DIF、ETS 分类、purified subtest matching 均为 30+ 年历史的标准工具）；(3) 核心发现 C% 的不确定性范围过大（13.5%–31.3%）。同时指出了 Rodriguez et al. (2021) 和 Polo et al. (2024) 两篇遗漏的重要相关工作。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1773 · 2026-05-25T21:26:04.762282+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 173

## Round 173

2 recorded events


### User

_source line 1774 · 2026-05-25T21:27:55.718881+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 审稿意见的交叉回应

---

### Weaknesses 回应

**[AGREE] R2-W1: 标题 "Score Incomparability" 与 ρ ≈ 0.997 的叙事张力。**
同意这是论文最突出的叙事问题。论文的核心发现实际上是 *item-level instability with aggregate robustness*——31% 的题目有大效应 DIF，但聚合排名几乎不变 (Table 2: ρ ≈ 0.997, flip rate ≈ 0.062)。标题 "Score Incomparability" 设定了远超实际发现的期望。不过需要补充两点细微之处：(1) Section 4.6 和 Figure 6 表明 DIF-ordered item removal 比 random removal 更快降低排名一致性，说明 DIF 题目确实携带了结构化的不稳定信息；(2) 个别模型可移动多达 2,561 个排名位置（Section 4.6）。但我同意，aggregate-level 的近乎完美保持使 "incomparability" 一词失当。更准确的标题可能是 "Temporal Item-Level Instability" 或 "Differential Item Functioning"。

**[REBUT] R2-W2: 方法论新颖性有限。**
部分反驳。R2 正确指出核心统计方法 (MH-DIF, ETS, DEFF) 均非原创，但忽略了论文的方法论贡献不在于新统计量，而在于：(1) **Cross-subject matching** 虽源自 purified subtest matching (Swaminathan & Rogers, 1990)，但将其适配到 LLM multi-domain benchmark 设定下并推导出 ΔFPR=0 的构造性保证 (Section 3.4, Remark) 是非平凡的设计创新；(2) **Semi-synthetic injection framework** 将 contamination 建模为可控的 dose-response 实验（Figure 4），这在 DIF 文献中没有先例；(3) Section 5 系统性地识别了四个 LLM-specific challenges（local independence violation, within-family correlation, bimodal ability, multidimensionality）并给出了对应的方法论应对。对于 EMNLP 而言，方法论贡献不必是全新统计量——将成熟方法严谨地适配到新领域并通过大规模实证验证其有效性，本身就是有价值的贡献。当然，我同意论文应更清晰地标注哪些是已知方法、哪些是本文的适配创新。

**[AGREE] R2-W3: C% 不确定性范围过大 (13.5%–31.3%)。**
完全同意，这与我自己的 W1 一致。补充一点：这一不确定性的核心来源是 DEFF estimator 的选择——simple-mean vs weighted-mean（Section D, Table 10）。Weighted-mean DEFF 对 mega-families（如 Llama, Mistral）赋予过高权重可能导致 over-correction（Appendix D 讨论了这一点），但论文未提供判断两个 estimator 哪个更合适的独立证据。Cluster bootstrap CI [29.27%, 37.81%] 排除了 weighted-mean 的 13.5%，但 bootstrap 本身依赖于 family 定义的合理性（Appendix I: 30 families with ≥2 members）。我建议作者至少在 abstract 中报告校正后区间而非仅报告 raw 31.3%。

**[AGREE] R2-W4: "Mechanism-agnostic" 定位与 contamination-focused 验证的张力。**
同意这是一个重要的内部一致性问题。论文在 Section 5.1 声称 "Temporal DIF detects *that* items function differently...not *why*"，但 (1) 验证框架 (Section 3.4) 完全基于 contamination injection；(2) Section 4.3 花大量篇幅比较 DIF flags 与 web-overlap labels；(3) Discussion (Section 5.2) 建议基于 DIF 结果进行 contamination-motivated 的 item removal。如果方法真正 mechanism-agnostic，至少应包含一个非 contamination 来源的 DIF 验证（例如，模拟 "training methodology shift" 导致的 DIF，或利用已知的 format change 事件）。在此之前，"mechanism-agnostic" 的定位缺乏验证支撑。

**[REBUT] R2-W5: DIF 在 LLM 场景下的概念合法性。**
部分反驳。R2 正确指出 2023 vs 2024 模型不是 "同一总体的人口学子群"，但这并不使 DIF 分析无效——DIF 的核心问题是 "controlling for overall ability, do items function differently across groups?"，这一问题对任何可比较的两个群体都有意义，不限于人口学子群。教育测量中 DIF 也常用于跨时间群体 (如不同年份考生)，与本文设定类似。关于 κ=0.80 和多维性伪影：论文在 Section A.1 讨论了 Yen's Q3 diagnostic（11.3% of within-subject item pairs exceed Q3 ≥ 0.20），并通过 cross-subject matching 部分缓解了多维性问题（不同学科视为不同维度）。不过我同意论文应更深入讨论 "LLM 的 total score 是否是一个有意义的 conditioning variable"——这与我自己的 W5 (ETS 阈值迁移) 相关。

**[AGREE] R2-W6: Contribution 3 (audit protocol) 权重不足。**
同意。Section 5.2 的 Monitor/Triage/Correct 协议仅占半段，没有具体的实施案例、部署成本分析或用户研究。作为声明的三大贡献之一，这一部分显得单薄。建议要么降级为 "future direction"，要么扩展为独立 subsection 并提供至少一个模拟部署场景。

---

### Questions 回应

**[AGREE] R2-Q1: 能否量化 temporal DIF 的实际危害？**
同意这是论文缺失的关键信息。ρ ≈ 0.997 表明聚合排名几乎不受影响，那么 temporal DIF 的实际危害是什么？论文应提供具体场景：例如，(1) 哪些特定模型在 DIF item removal 前后排名变化最大？(2) 如果 practitioner 使用某个学科子集（而非全部 MMLU）评估模型，DIF 的影响是否被放大？(3) Figure 6 的 ranking degradation 在哪个 removal threshold 开始产生实质性影响？没有这些信息，读者难以判断 31% (或 13.5%) 的 DIF 率是否构成实际问题。

**[AGREE] R2-Q2: 时间划分粒度的影响。**
同意。论文报告 half-yearly C%=34.1% (Section 4.2)，高于 annual 31.3%。这一现象有两种解释：(1) 更细粒度捕获了更多真实的时序变化；(2) 更小的 cohort size 增加了统计噪声。论文未区分这两种可能性。此外，是否存在 "突变点" (change point)——例如某个特定时间窗口 DIF 突然增加——可以通过 rolling-window MH-DIF 分析来检验。这也与我自己的 Q4 相关。

**[AGREE] R2-Q3: Base vs instruct 反转的解释。**
完全同意，这与我自己的 W8 一致。RLHF/instruction tuning 系统性地改变了模型与 multiple-choice items 的交互方式（如输出格式偏好、refusal behavior、calibration 变化），这些都是 "legitimate ability profile change" 而非 item-level bias。论文的 χ²=562.7 (Section 4.3) 确认了方向反转的统计显著性，但未提供 DIF vs. impact 的分离证据。一个可能的测试：在 base-only 或 instruct-only 子群内进行 temporal DIF 分析，如果 DIF pattern 在子群内保持一致，则支持 item-level bias 解释；如果消失，则支持 composition shift 解释。论文在 Appendix O 分别报告了 base-only 和 instruct-only 的 temporal DIF (Table 15)，这部分应被提升到主文以回应此质疑。

**[REBUT] R2-Q4: Non-contamination DIF 下 cross-subject matching 的行为。**
部分反驳。R2 问 "当 DIF 由全局训练方法变化驱动时 cross-subject matching 的行为如何"——这个问题的前提需要澄清。Cross-subject matching 的设计目标是防止匹配变量被目标学科的 DIF 信号污染，而非区分 DIF 的来源。如果全局训练方法变化（如 RLHF）同时影响所有学科，cross-subject matching 仍然有效：它使用非目标学科的总分作为匹配变量，只要匹配变量能有效反映 "ability"（而非被污染），DIF 检测就有效。问题在于：当所有学科都受影响时，匹配变量本身反映了 "post-method-change ability"，而非 "pure ability"，这可能导致 cross-subject matching 低估 DIF（因为匹配变量已吸收了部分变化）。但这是 conservative bias（低估而非高估），不会导致 false positive inflation。所以 cross-subject matching 在 non-contamination DIF 场景下仍然是安全的，只是可能 under-powered。

---

### Missing References 回应

**[AGREE] R2-M1: Rodriguez et al. (2021).** 同意，这是 IRT+NLP 评估的重要早期工作，应被引用。

**[REBUT] R2-M2: Polo et al. (2024) "tinyBenchmarks".** 论文引用了 Polo et al. (Zhu et al., 2026) "Benchmark health index" (p10)。如果 R2 指的是另一篇 Polo et al. 2024 ICML 工作，需要确认具体引用。但 tinyBenchmarks 的 IRT 方法与本文的 DIF 分析在技术路线上差异较大（IRT 参数估计 vs. 非参数 DIF 检测），引用的必要性可讨论。

**[AGREE] R2-M3: 最新 IRT+LLM 工作。** 同意，领域发展迅速，论文应确保引用最新的相关工作。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1775 · 2026-05-25T21:28:07.141192+00:00_

Reviewer 1 交叉回应已收到。等待 Reviewer 2 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 174

## Round 174

2 recorded events


### User

_source line 1776 · 2026-05-25T21:28:09.720577+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。对 R2 的 6 个 Weaknesses：W1/W3/W4/W6 完全同意，W2/W5 部分反驳（cross-subject matching 适配和 DIF 概念合法性有辩护空间）。对 4 个 Questions：Q1/Q2/Q3 同意需要作者回应，Q4 部分反驳（cross-subject matching 在 non-contamination DIF 下仍安全，只是可能 under-powered）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 1777 · 2026-05-25T21:28:14.833283+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 175

## Round 175

10 recorded events


### User

_source line 1778 · 2026-05-25T21:28:16.338200+00:00_

[Reviewer 2 审稿意见]:
## 交叉回应：Reviewer 2 对 Reviewer 1 审稿意见的逐条评议

---

### Weaknesses

**[AGREE] R1-W1: 标题数字 31.3% 未经 DEFF 校正，校正后区间极宽。**
完全同意。这与我的 W3 一致。Abstract 和 Introduction 使用 "31% of items" 作为 headline claim，但 Section 4.2 和 Appendix D 显示 DEFF 校正后范围为 13.5%–29.2%，2.3× 的不确定性严重影响核心结论的精确度。论文虽然在 Section 4.2 用 "bracketing C% at 13.5–29.2%" 承认了这一范围，但 abstract 和 title 的措辞并未反映这一不确定性。如果真实 C% 接近 13.5%，"50× above random" 变成 ~22×，叙事力度显著减弱。至少 abstract 应报告 DEFF 校正后的范围而非 raw C%。

**[AGREE] R1-W2: 半合成注入使用均匀二值翻转可能高估检测力。**
同意，但补充一点：论文在 Limitations (1) 和 Section 3.4 末尾已明确承认这一局限（"reported ΔTPR values may overestimate detection power"），且 Section 4.4 报告了 difficulty-dependent injection 的 ΔTPR ≈ 0.41（vs. uniform 的 0.51），量化了高估幅度约 ~20%。Appendix B 的 mixed-mechanism injection 也提供了部分补充。所以问题不在于作者是否意识到这个问题（他们意识到了），而在于验证框架的覆盖面不够广——只有 contamination-based 的注入，没有其他 DIF 机制的模拟（如训练方法变化）。这与我的 W4（mechanism-agnostic 定位与 contamination-heavy 验证的张力）一致。

**[REBUT] R1-W3: IRT 模型拟合差与参数化 power analysis 的张力。**
这个张力确实存在，但其影响被 R1 高估了。关键区分在于：(1) MH-DIF 本身是非参数方法，不依赖 2PL 拟合——论文选择 MH 而非 IRT-based DIF 检测恰恰是为了规避 2PL 拟合差的问题（Section 2, Related Work 明确指出 "MH-DIF is nonparametric and robust to model misspecification, an advantage given poor 2PL fit for MMLU"）；(2) Table 3 的 power analysis 是辅助验证，用 2PL 参数生成模拟数据来估计 MH 的检测功效——即使 2PL 参数不精确，模拟提供的是 approximate bound 而非精确估计；(3) 最关键的功效证据是实证的：31.3% temporal C% vs. 0.62% random baseline 的 50× ratio（Table 1），这一对比完全不依赖 2PL 参数。论文的分析链条是"非参数检测 + 实证控制验证"，参数化 power analysis 是补充而非基础。不过，论文确实应更明确标注 power analysis 结果的局限性——当前 Section 4.1 仅在 Appendix A.2 提及 RMSEA 问题。

**[AGREE] R1-W4: Cross-subject ΔFPR=0 在多学科污染下的退化未充分表征（k=5-15 区间）。**
部分同意。Section 4.4 确实报告了 k=20 时 ΔFPR = 0.167，论文据此论证 "still insufficient to account for the observed 31% C%"。但 R1 指出 k=5（ΔFPR < 0.007）到 k=20（ΔFPR = 0.167）之间存在跳变区域未被系统刻画，这个批评合理。这一退化曲线的精确形状对实际应用场景（benchmark maintainer 需要判断何时切换到 within-subject matching）至关重要。不过，我认为这是一个"加分项"需求而非"否决性"缺陷——论文已提供了足够的数据点来支持其核心论证（cross-subject matching 在 low-k 场景下有效）。

**[AGREE] R1-W5: ETS 阈值从人类考生迁移到 LLM 的合理性缺乏讨论。**
同意，且这与我的 W5（DIF 在 LLM 场景下的概念合法性）互补。ETS 的 |Δ_MH| = 1.0/1.5 阈值源于人类考试场景中对 "negligible/moderate/large" 效应量的经验判断。LLM 群体有根本不同的属性：(a) 没有真正的 latent ability trait，(b) model families 内高度同质，(c) 能力分布可能是多模态的。论文在 Section 4.2 展示了跨阈值的鲁棒性（18.4% at |Δ_MH| ≥ 2.0, 10.2% at ≥ 2.5），这在一定程度上缓解了阈值选择的任意性——核心发现不依赖于特定阈值。但论文没有提供 LLM-specific 的阈值校准方法，这确实是方法论上的缺口。

**[REBUT] R1-W6: 多重比较校正未作为主方法。**
R1 的担忧是常见的，但论文已在 Section 3.4 充分回应：Benjamini-Hochberg 校正在 q = 0.05 水平仅重新分类 3/3,918 C items——即 0.08% 的变化。这一近零影响是因为 ETS C 已内置了双重阈值（效应量 + 显著性）。更重要的是，DIF 分析在教育测量领域的标准实践中不使用多重比较校正（论文引用 Wainer 1993），因为 DIF 分析的目标是 item-level 诊断而非控制 study-level error rate——每个 item 的 DIF 判定是独立的诊断决策。论文遵循了领域惯例且提供了 BH 校正的敏感性检验。不过我在自己的 minor issue m2 中也指出：在 N = 1,887 下，p < 0.05 几乎自动满足（only 3/3,918 C items lack significance），这意味着双重阈值实质退化为单一效应量阈值——论文应更坦诚地承认这一点。

**[AGREE] R1-W7: "近独立于 web-overlap labels" 的推断强度。**
同意。φ = 0.012 的低相关有两种可能解释：(a) DIF 和 contamination 确实测量不同维度，或 (b) web-overlap labels 作为 contamination 的 proxy 噪声太大，掩盖了真实相关性。论文在 Section 4.3 承认了 (b) 的可能性（"this near-independence could partly reflect proxy noise"），并提供了 label-independent 的支持证据（base-vs-instruct reversal, χ² = 562.7）。但 R1 的担忧仍然成立：如果 web-overlap labels 的 proxy quality 很差，那么低 φ 本身的信息量有限。论文应更保守地表述这一发现——从 "DIF flags are near-independent of web-overlap labels" 改为 "DIF flags show low correlation with available contamination proxies, though proxy noise may attenuate the measured association"。

**[AGREE] R1-W8: Base vs instruct 反向模式的机制解释不足。**
同意，与我的 Q3 一致。Instruction tuning 系统性地改变模型的 MCQ 应答策略（如 instruction following 导致的格式偏好、safety training 导致的"安全选项"倾向、RLHF 改变的猜测行为），这些都可能产生 DIF-like artifacts，而非反映 item 本身的 measurement invariance violation。论文在 Section 5.1 将反转解释为 "structured item-level bias rather than uniform group impact"（引用 Camilli 1994），但没有排除上述 confound。一个更强的分析应检验反转是否与 item 特征（如选项格式、是否需要 instruction following、是否涉及安全敏感内容）相关，而非仅与 difficulty 相关（当前仅报告了 difficulty-direction interaction r = -0.597, Section 4.2）。

---

### Questions

**[AGREE] R1-Q1 (DEFF 报告):** 如上 W1 所述，abstract 应报告校正后范围。

**[REBUT] R1-Q2 (2PL power analysis):** 如上 W3 所述，power analysis 是辅助证据；实证 50× ratio 不依赖 2PL 参数。但同意论文应在 Section 4.1 更明确地讨论 2PL misfit 对 power 估计的影响方向。

**[AGREE] R1-Q3 (多学科 ΔFPR 曲线):** 如上 W4 所述，k=5-15 区间的系统表征将提升论文的完整性和实用性。

**[AGREE] R1-Q4 (时间分割点影响):** 这与我的 Q2 一致。Calendar-year boundary 是粗糙的。Section 3.3 报告 half-yearly C% = 34.4%（反而更高），但缺少对 DIF 信号随时间积累动态的分析——DIF 是线性增长、S-curve、还是在特定事件（如某主流模型发布）后突变？这一分析对理解 DIF 的驱动因素有重要价值。

**[AGREE] R1-Q5 (Family correlation 处理):** DEFF 校正处理了 family correlation，但 DEFF 估计本身高度依赖 "family" 的定义边界（什么算同一 family？Llama-2-7B 的不同 LoRA 微调 vs. Llama-2-7B vs. Llama-2-13B vs. Llama-3？），这一定义的模糊性导致了 C% 的宽区间（13.5%-29.2%）。论文应提供 family 定义的敏感性分析。

**[REBUT] R1-Q6 (Within-subject DIF 全量验证):** Section 4.2 已报告 within-subject C% = 38.1%（average across 5 subjects），且 cross-subject 与 within-subject 匹配的 agreement κ = 0.80（834 items）。Section 4.2 还指出 cross-subject-unique C items 不集中于 high-shift subjects。这些提供了合理的 within-subject 验证覆盖，虽然不是 all-57-subjects 的全量分析。完整的 57 学科分析确实更严谨，但 5 学科的验证已足以支持论文结论。

**[AGREE] R1-Q7 (Item-property 预测力 AUROC=0.60 的含义):** Section 5.2 的低 AUROC 意味着 DIF susceptibility 不可预测，这是一个重要的负面发现——它意味着 benchmark maintainer 无法通过 item 特征提前筛选潜在 DIF 项目，只能通过运行 MH-DIF 进行事后检测。这既强化了 audit protocol 的必要性，也限制了其预防价值。论文应更充分地讨论这一含义。

---

### Missing References

**[AGREE] Vania et al. (2021, "Comparing Test Sets with Item Response Theory"):** 直接相关——在 NLP test set 比较中使用 IRT，与本文主题高度匹配。

**[REBUT] CAT for LLMs (Zhuang et al., 2023):** 计算机自适应测试（CAT）与 DIF 分析是不同的心理测量工具，在方法论上没有直接关联。CAT 关注的是 test administration efficiency，而非 measurement invariance。这篇文献与 Lalor et al. (2019) 的关系更紧密，可放在 related work 的 IRT 段落中作为背景，但不构成核心遗漏。

**[AGREE] Test security / item exposure literature (van der Linden & Veldkamp, 2007):** Item exposure 控制与 DIF 在概念上有交叉——item exposure 可能导致 DIF（高曝光 item 更容易被训练数据覆盖），且 item exposure management 文献中的方法论思路可能启发 benchmark rotation 策略。不过这更像是一个 "nice to have" 的背景引用，而非核心遗漏。

**补充：** 我在自己的审稿中也指出了两个可能遗漏的引用：Rodriguez et al. (2021, "Evaluation Examples Are Not Equally Informative," ACL) 和 Polo et al. (2024, "tinyBenchmarks," ICML)，两者都是 IRT 应用于 NLP/LLM 评估的重要先驱工作。

---

### 总结

R1 和我的审稿意见有高度一致的关注点：(1) C% 不确定性范围和 headline claim 的表述（我的 W3 = R1-W1）；(2) mechanism-agnostic 定位与 contamination-centric 验证的张力（我的 W4 ≈ R1-W2）；(3) DIF 在 LLM 场景下的概念合法性（我的 W5 ≈ R1-W5）；(4) base-vs-instruct 反转的机制解释不足（我的 Q3 = R1-W8）。

**主要分歧在 R1-W3 (2PL power analysis) 和 R1-W6 (多重比较校正)：** 我认为 R1 高估了这两个问题的严重性——MH-DIF 的非参数性质和 DIF 领域的多重检验惯例使这些问题成为 minor concerns 而非 major weaknesses。

**对 Overall Assessment 的影响：** R1 的审稿强化了我的 Borderline Conference (3.5) 判断。论文的执行质量高，但方法论新颖性有限（R1 未直接提及但通过强调"已知方法"间接表达了类似关注）。如果作者能在 rebuttal 中 (a) 在 abstract 使用 DEFF 校正后的数字，(b) 提供 family 定义敏感性分析以收窄 C% 区间，(c) 更诚实地讨论 ETS 阈值迁移的局限性，论文可升至 4.0 (Conference)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 1779 · 2026-05-25T21:28:42.709285+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "irt_equated_bench_regen"
  }
}
```

</details>

---


### Tool result

_source line 1780 · 2026-05-25T21:28:43.864266+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-25T21:16:44.717026+00:00\", \"completed_at\": \"2026-05-25T21:20:05.493811+00:00\", \"findings\": [{\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1 response matrix 面板中的彩色小点在灰度打印时可能难以区分（绿/红/灰），建议辅以 marker shape 或 hatching 增加辨识度\"}, {\"severity\": \"info\", \"dimension\": \"page 4\", \"message\": \"Figure 3 的 ETS severity 颜色编码（A=绿, B=黄, C=红）对红绿色盲不够友好，建议改用 Okabe-Ito 色板或 blue-orange 方案\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Figure 6 五个面板的 tick label 和 legend 文字偏小（约正文字号 60-65%），建议稍增大字号或减少 tick 数量以提升可读性\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"右栏内容密度极高（§4.5–4.7 + §5 Discussion + §6 Conclusion），无 display item 穿插，但作为 Discussion/Conclusion 区域属正常安排\"}, {\"severity\": \"info\", \"dimension\": \"page 5\", \"message\": \"Figure 4 bar chart 的 x 轴标签（ρ, ε 参数组合）字号偏小，部分重叠，建议调整间距或旋转标签\"}, {\"severity\": \"info\", \"dimension\": \"page 13\", \"message\": \"Tables 6–8 三个表格密集排布在同一页，单个表格行数少（3-5 行），可考虑合并为一个综合表以节省空间\"}, {\"severity\": \"info\", \"dimension\": \"page 14\", \"message\": \"Table 10（uncertainty quantification）内容较复杂，列头缩写较多，建议在 caption 中解释缩写含义\"}], \"counts\": {\"critical\": 0, \"warning\": 0, \"info\": 7}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 1154
}
```

</details>

---


### Tool call

_source line 1781 · 2026-05-25T21:28:43.864638+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 1782 · 2026-05-25T21:28:43.915381+00:00_

1	issues:
2	  # === Round 19 issues (current round, fresh review) ===
3	
4	  - id: "R19-N1"
5	    summary: "DEFF 校正产生 2.16× 估计范围（13.5% vs 29.2%），论文未提供充分的分辨依据"
6	    category: method
7	    severity: critical
8	    status: in_progress
9	    first_raised_round: 19
10	    last_seen_round: 19
11	    mentions:
12	      - round: 19
13	        reviewers: [1, 2]
14	        note: "R1 提出，R2 AGREE。Simple-mean C%=29.2% vs weighted-mean C%=13.5%。"
15	    action_items:
16	      - round: 20
17	        action: "根因修复：Abstract/Intro/Conclusion/Discussion 全部移除 13.5%，改用 29.2% + cluster bootstrap CI [26.7%, 53.2%]。"
18	        assigned_to: director
19	        status: done
20	    resolution: ""
21	    resolution_round: null
22	
23	  - id: "R19-N2"
24	    summary: "Semi-synthetic 注入用 uniform binary flipping，检测力估计可能被系统性高估"
25	    category: method
26	    severity: critical
27	    status: in_progress
28	    first_raised_round: 19
29	    last_seen_round: 19
30	    mentions:
31	      - round: 19
32	        reviewers: [1, 2]
33	        note: "R1 提出，R2 AGREE。Graded shift (Δp=0.1-0.3) 下检测力可能远低于报告值。"
34	    action_items:
35	      - round: 20
36	        action: "§4.5 reframe as calibration upper bound + 20% overestimation bound; Figure 2 caption 加 calibration framing"
37	        assigned_to: director
38	        status: done
39	    resolution: ""
40	    resolution_round: null
41	
42	  - id: "R19-N3"
43	    summary: "缺少 DIF 文献中 impact/bias 关键区分——'Correct' 步骤与 mechanism-agnostic 定位逻辑冲突"
44	    category: method
45	    severity: critical
46	    status: in_progress
47	    first_raised_round: 19
48	    last_seen_round: 19
49	    mentions:
50	      - round: 19
51	        reviewers: [1, 2]
52	        note: "R1 提出，R2 强烈 AGREE。DIF 是 bias 的必要非充分条件。"
53	    action_items:
54	      - round: 20
55	        action: "§5.2 Correct 步骤重写：DIF flags → expert review，DIF is necessary but not sufficient for item bias，引用 camilli1994methods + penfield2007dif"
56	        assigned_to: director
57	        status: done
58	    resol
…[truncated 10924 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 1783 · 2026-05-25T21:33:43.085108+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "irt_equated_bench_regen",
  "issues_yaml": "issues:\n  # === Round 20 issues (fresh review) ===\n\n  - id: \"R19-N1\"\n    summary: \"DEFF 校正产生 2.16× 估计范围（13.5% vs 29.2%），Abstract 仍使用未校正 31%\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 19\n    last_seen_round: 20\n    mentions:\n      - round: 19\n        reviewers: [1, 2]\n        note: \"R1 提出，R2 AGREE。Simple-mean C%=29.2% vs weighted-mean C%=13.5%。\"\n      - round: 20\n        reviewers: [1, 2]\n        note: \"R20-R1-W1 + R20-R2-W3 再次提出。R20 action (改用 29.2%+CI) 标记 done，但 Abstract 仍使用 '31%'。两位 Reviewer 要求 Abstract 使用 DEFF 校正后数字 + family 定义敏感性分析。\"\n    action_items:\n      - round: 20\n        action: \"根因修复：Abstract/Intro/Conclusion/Discussion 全部移除 13.5%，改用 29.2% + cluster bootstrap CI [26.7%, 53.2%]。\"\n        assigned_to: director\n        status: done\n      - round: 20\n        action: \"Abstract 仍使用 raw 31%，需改为 DEFF 校正后 ~29% 或报告区间；补充 family 定义敏感性分析收窄 C% 区间\"\n        assigned_to: director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-N2\"\n    summary: \"Semi-synthetic 注入用 uniform binary flipping，检测力估计可能被系统性高估\"\n    category: method\n    severity: critical\n    status: in_progress\n    first_raised_round: 19\n    last_seen_round: 20\n    mentions:\n      - round: 19\n        reviewers: [1, 2]\n        note: \"R1 提出，R2 AGREE。Graded shift (Δp=0.1-0.3) 下检测力可能远低于报告值。\"\n      - round: 20\n        reviewers: [1, 2]\n        note: \"R20-R1-W2 再次提出（Critical）。R2 AGREE 但指出论文已有部分回应（difficulty-dependent ΔTPR≈0.41, ~20% bound）。Reviewer 认为 reframe as upper bound 已完成，但仍需更多注入模式验证。\"\n    action_items:\n      - round: 20\n        action: \"§4.5 reframe as calibration upper bound + 20% overestimation bound; Figure 2 caption 加 calibration framing\"\n        assigned_to: director\n        status: done\n      - round: 20\n        action: \"考虑补充 graded injection 实验（ε 按难度/能力衰减），但 R2 认为当前 ~20% bound 已基本足够\"\n        assigned_to: director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-N3\"\n    summary: \"DIF 在 LLM 场景下的概念合法性——impact vs bias 区分 + 多维性伪影\"\n    category: method\n    severity: critical\n    status: in_progress\n    first_raised_round: 19\n    last_seen_round: 20\n    mentions:\n      - round: 19\n        reviewers: [1, 2]\n        note: \"R1 提出，R2 强烈 AGREE。DIF 是 bias 的必要非充分条件。\"\n      - round: 20\n        reviewers: [1, 2]\n        note: \"R20-R2-W5 扩展为更广泛的概念合法性问题：2023 vs 2024 模型不是同一总体子群；κ=0.80 意味着 20% DIF 项可能是多维性伪影；需讨论何时 DIF 反映测量问题 vs 合法能力变化。R1 部分 REBUT（DIF 对跨时间群体有效，Q3 diagnostic 部分缓解）。\"\n    action_items:\n      - round: 20\n        action: \"§5.2 Correct 步骤重写：DIF flags → expert review，DIF is necessary but not sufficient for item bias\"\n        assigned_to: director\n        status: done\n      - round: 20\n        action: \"补充讨论：LLM temporal DIF 何时反映测量问题 vs 合法能力结构变化；κ=0.80 的多维性伪影含义\"\n        assigned_to: director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-N4\"\n    summary: \"DIF-contamination 近独立性推断强度过高——web-overlap proxy 噪声可能驱动低 φ\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 19\n    last_seen_round: 20\n    mentions:\n      - round: 19\n        reviewers: [1, 2]\n        note: \"R2 提出，R1 AGREE。Jaccard≈0.20 可能反映 proxy 低质量。\"\n      - round: 20\n        reviewers: [1, 2]\n        note: \"R20-R1-W7 再次提出。R2 AGREE。论文已加 proxy 声明但 'complementary diagnostic dimensions' 措辞仍过强。建议改为 'low correlation with available contamination proxies, though proxy noise may attenuate the measured association'。\"\n    action_items:\n      - round: 20\n        action: \"§4.3 标题改为 Comparison with Web-Overlap Labels；proxy 声明 + label-independent evidence\"\n        assigned_to: director\n        status: done\n      - round: 20\n        action: \"进一步弱化 'complementary diagnostic dimensions' 措辞\"\n        assigned_to: director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-W2\"\n    summary: \"Cross-subject matching ΔFPR=0 在 k=5-15 区间退化未充分表征\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 19\n    last_seen_round: 20\n    mentions:\n      - round: 19\n        reviewers: [1, 2]\n        note: \"R1-W2, R2 AGREE。k=20 ΔFPR=0.069，但未模拟 k=30/50。\"\n      - round: 20\n        reviewers: [1, 2]\n        note: \"R20-R1-W4 再次提出（Major）。Table 7 报告 k=20/30/40/50，但 k=5-15 区间仍缺系统刻画。R2 部分 AGREE（加分项而非否决性缺陷）。\"\n    action_items:\n      - round: 19\n        action: \"模拟 k=30/50 的 ΔFPR；讨论高 contamination 覆盖率下的替代策略\"\n        assigned_to: paper_agent\n        status: open\n      - round: 20\n        action: \"补充 k=5,8,10,15 的 ΔFPR 数据点，刻画完整退化曲线\"\n        assigned_to: director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-W3\"\n    summary: \"Mechanism-agnostic 定位与 contamination-centric 验证/叙事存在张力\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 19\n    last_seen_round: 20\n    mentions:\n      - round: 19\n        reviewers: [1, 2]\n        note: \"R1-W3, R2 AGREE。Related Work 以 Contamination Detection 开篇。\"\n      - round: 20\n        reviewers: [1, 2]\n        note: \"R20-R2-W4 再次提出（Major），R1 AGREE。Related Work 已重排但验证框架仍完全基于 contamination injection。需至少一个非 contamination DIF 验证。\"\n    action_items:\n      - round: 20\n        action: \"Related Work 段落重排已完成\"\n        assigned_to: director\n        status: done\n      - round: 20\n        action: \"补充至少一个非 contamination 来源的 DIF 验证（如训练方法变化模拟）\"\n        assigned_to: director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-W4\"\n    summary: \"ETS 阈值从人类考生迁移到 LLM 缺乏 substantive meaning 讨论\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 19\n    last_seen_round: 20\n    mentions:\n      - round: 19\n        reviewers: [1, 2]\n        note: \"R2-W1, R1 AGREE。Random-split P99=1.45 是 necessary 但非 sufficient。\"\n      - round: 20\n        reviewers: [1, 2]\n        note: \"R20-R1-W5 再次提出（Major），R2 AGREE。虽已连接 Monte Carlo power + random-split FPR，但仍未讨论 |Δ_MH|=1.5 对 LLM 的实质含义。需 LLM-specific 阈值校准或 substantive meaning 讨论。\"\n    action_items:\n      - round: 20\n        action: \"§4.2 显式连接 Monte Carlo power analysis (TPR ≥ 0.68) 与 random-split FPR < 1%\"\n        assigned_to: director\n        status: done\n      - round: 20\n        action: \"添加 ETS 阈值在 LLM 场景下实质含义的讨论段落，或提供 data-driven 阈值校准\"\n        assigned_to: director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-D1\"\n    summary: \"[分歧] 方法论新颖性是否足够\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 19\n    last_seen_round: 20\n    mentions:\n      - round: 19\n        reviewers: [1, 2]\n        note: \"R2 认为直接搬运，R1 反驳 cross-subject matching 和 DEFF 是 LLM-specific 贡献。\"\n      - round: 20\n        reviewers: [1, 2]\n        note: \"R20-R2-W2 再次提出（Critical）。R1 部分 REBUT：cross-subject matching 适配 + semi-synthetic framework + 四个 LLM challenges 的解决是 non-trivial。但 R2 坚持对 EMNLP 方法论贡献不足。分歧持续。\"\n    action_items:\n      - round: 19\n        action: \"Introduction 中更清晰区分 borrowed methodology 和 novel adaptations\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-W1\"\n    summary: \"标题 'Score Incomparability' 与 ρ≈0.997 的核心发现存在根本性叙事张力\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 20\n    last_seen_round: 20\n    mentions:\n      - round: 20\n        reviewers: [1, 2]\n        note: \"R2 提出（Critical），R1 AGREE。标题暗示分数不可比较，但 ρ≈0.997 表明排名几乎完美保持。'The result is sobering' 与 aggregate robustness 不匹配。论文实际展示 item-level instability with aggregate robustness。\"\n    action_items:\n      - round: 20\n        action: \"修改标题为更准确的措辞（如 Temporal Item-Level Instability / Differential Item Functioning）；弱化 'sobering' 等措辞\"\n        assigned_to: director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-W8\"\n    summary: \"Base-vs-instruct 反向模式（χ²=562.7）机制解释不足——RLHF 可能产生 DIF-like artifacts\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 20\n    last_seen_round: 20\n    mentions:\n      - round: 20\n        reviewers: [1, 2]\n        note: \"R1-W8 提出，R2-Q3 同一问题。RLHF/instruction tuning 系统性改变 MCQ 应答策略（format preference, safety behavior），可能产生 DIF-like artifacts 而非 item-level bias。Appendix O (Table 15) 的 base-only/instruct-only 分析应提升到主文。\"\n    action_items:\n      - round: 20\n        action: \"讨论 base/instruct format sensitivity 作为替代解释；将 Table 15 base-only/instruct-only temporal DIF 提升到主文\"\n        assigned_to: director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-W11\"\n    summary: \"Contribution 3 (audit protocol) 仅半段，无部署验证\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 20\n    last_seen_round: 20\n    mentions:\n      - round: 20\n        reviewers: [1, 2]\n        note: \"R2-W6 提出（Minor），R1 AGREE。Section 5.2 仅半段，没有 case study 或用户验证。\"\n    action_items:\n      - round: 20\n        action: \"降级为 future direction，或扩展为独立 subsection 并提供模拟部署场景\"\n        assigned_to: director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-MR1\"\n    summary: \"遗漏 Rodriguez et al. (2021) 'Evaluation Examples Are Not Equally Informative' (ACL)\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 20\n    last_seen_round: 20\n    mentions:\n      - round: 20\n        reviewers: [1, 2]\n        note: \"R2 提出，R1 AGREE。IRT+NLP 评估的奠基性工作，应被引用。\"\n    action_items:\n      - round: 20\n        action: \"Related Work 中引用 Rodriguez et al. (2021)\"\n        assigned_to: director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  # === Round 19 issues not raised in Round 20 ===\n\n  - id: \"R19-W1\"\n    summary: \"Calendar-year cohort boundary 粗糙——temporal framing 过窄\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 19\n    last_seen_round: 20\n    mentions:\n      - round: 19\n        reviewers: [1, 2]\n        note: \"R1-W1 + R2-W3。Release date ≠ training cutoff。\"\n      - round: 20\n        reviewers: []\n        note: \"本轮未作为独立 weakness 提出，但 Q2/Q4 仍涉及时间粒度问题。R20 action (temporal = cohort-based shorthand) 已完成。降级为 question 级别。\"\n    action_items:\n      - round: 20\n        action: \"§5.1 加入 'temporal = cohort-based shorthand'，明确 cohorts differ in architecture/data/methodology simultaneously\"\n        assigned_to: director\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-W5\"\n    summary: \"与 Growing Pains (Habba et al., 2026) 差异化论证不够深入\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 19\n    last_seen_round: 19\n    mentions:\n      - round: 19\n        reviewers: [1, 2]\n        note: \"R2-W2, R1 AGREE（优先级不高）。\"\n      - round: 20\n        reviewers: []\n        note: \"本轮未提及，可能已通过 Related Work 改进修复，待 Research Director 确认\"\n    action_items:\n      - round: 19\n        action: \"附录中加入与 Growing Pains 在相同 items 上的交叉比较\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-W6\"\n    summary: \"Score correction 展示不充分且缺乏 impact/bias 区分作为方法论基础\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 19\n    last_seen_round: 19\n    mentions:\n      - round: 19\n        reviewers: [1, 2]\n        note: \"R2-W5, R1 AGREE。§4.6 仅半页。N3 fix provides conceptual foundation。\"\n      - round: 20\n        reviewers: []\n        note: \"本轮未提及，可能已通过 §5.2 Correct 步骤重写修复，待 Research Director 确认\"\n    action_items:\n      - round: 19\n        action: \"扩展 §4.6 或附录 case study\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  # === Round 17 issues (all resolved) ===\n\n  - id: \"R17-N1\"\n    summary: \"DEFF 估计量选择论证存在循环性\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 17\n    last_seen_round: 17\n    resolution: \"区间表述 → R19 再次提出（R19-N1）\"\n    resolution_round: 18\n\n  - id: \"R17-N2\"\n    summary: \"Semi-synthetic ΔTPR upper bound 声称不严密\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 17\n    last_seen_round: 17\n    resolution: \"reference-case 替换 → R19 要求 graded injection（R19-N2）\"\n    resolution_round: 18\n\n  - id: \"R17-W1\"\n    summary: \"Mechanism-agnostic 定位与 contamination-centric 叙事张力\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 17\n    last_seen_round: 17\n    resolution: \"§3.4 + §5.1 标记。R19 要求更彻底 reframing（R19-W3）\"\n    resolution_round: 18\n\n  - id: \"R17-W2\"\n    summary: \"与 Growing Pains 差异化\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 17\n    last_seen_round: 17\n    resolution: \"Related Work 两点区分。R19 仍要求更深入（R19-W5）\"\n    resolution_round: 18\n\n  - id: \"R17-W3\"\n    summary: \"k>5 时 ΔFPR 退化\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 17\n    last_seen_round: 17\n    resolution: \"已量化。R19 要求 k=30/50（R19-W2）\"\n    resolution_round: 18\n\n  - id: \"R17-W4\"\n    summary: \"DIF-contamination 正交性需替代解释\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 17\n    last_seen_round: 17\n    resolution: \"两种解释 + OR=4.75。R19 要求 proxy 讨论（R19-N4）\"\n    resolution_round: 18\n\n  - id: \"R17-W5\"\n    summary: \"时间粒度选择未经论证\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 17\n    last_seen_round: 17\n    resolution: \"半年粒度 + Limitations。R19 仍指出（R19-W1）\"\n    resolution_round: 18\n\n  - id: \"R17-W6\"\n    summary: \"Abstract 信息过载\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 17\n    last_seen_round: 17\n    resolution: \"~122 words。R19 未复发\"\n    resolution_round: 18\n\n  - id: \"R17-M1\"\n    summary: \"ρ≈0.997 与 ±800 displacement 共存机制\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 17\n    last_seen_round: 17\n    resolution: \"§4.6 解释 closely-ranked pairs\"\n    resolution_round: 18\n\n  # === Round 16 issues (all resolved) ===\n\n  - id: \"R16-N1\"\n    summary: \"ETS 阈值校准\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 15\n    last_seen_round: 16\n    resolution: \"P99=1.45。R19 降级为 W4\"\n    resolution_round: 17\n\n  - id: \"R16-N2\"\n    summary: \"Contribution 过度定位\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 13\n    last_seen_round: 16\n    resolution: \"3→2 contributions\"\n    resolution_round: 17\n\n  - id: \"R16-W1\"\n    summary: \"DEFF 差异 2×\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 13\n    last_seen_round: 16\n    resolution: \"区间表述。R19 再次提出\"\n    resolution_round: 18\n\n  - id: \"R16-W2\"\n    summary: \"审计协议超出方法能力\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 15\n    last_seen_round: 16\n    resolution: \"DIF alone cannot determine causation\"\n    resolution_round: 17\n\n  - id: \"R16-W3\"\n    summary: \"Discussion 缺深层 insight\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 16\n    resolution: \"§5.1 三个区分\"\n    resolution_round: 17\n\n  - id: \"R16-W4\"\n    summary: \"Abstract 信息密度过高\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 14\n    last_seen_round: 16\n    resolution: \"精简到 ~122 words\"\n    resolution_round: 18\n\n  - id: \"R16-W5\"\n    summary: \"主文超页\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 14\n    last_seen_round: 16\n    resolution: \"8 页内\"\n    resolution_round: 17\n\n  - id: \"R16-W6\"\n    summary: \"ΔTPR 应标为上界\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 13\n    last_seen_round: 16\n    resolution: \"reference-case\"\n    resolution_round: 18\n\n  - id: \"R16-M1\"\n    summary: \"术语不一致\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 14\n    last_seen_round: 16\n    resolution: \"§1 定义\"\n    resolution_round: 17\n\n  - id: \"R16-M2\"\n    summary: \"有效 N vs 总 N 澄清\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 16\n    resolution: \"§3.2 已修正\"\n    resolution_round: 17\n\n  - id: \"R16-M3\"\n    summary: \"遗漏相关工作\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 16\n    resolution: \"新引用已加\"\n    resolution_round: 17\n\n  - id: \"R16-DATA1\"\n    summary: \"random-split baseline 0.18% 来自单次运行\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 16\n    resolution: \"全文修正 0.18→0.62\"\n    resolution_round: 17"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "irt_equated_bench_regen",
    "issues_yaml": "issues:\n  # === Round 20 issues (fresh review) ===\n\n  - id: \"R19-N1\"\n    summary: \"DEFF 校正产生 2.16× 估计范围（13.5% vs 29.2%），Abstract 仍使用未校正 31%\"\n    category: method\n    severity: critical\n    status: open\n    first_raised_round: 19\n    last_seen_round: 20\n    mentions:\n      - round: 19\n        reviewers: [1, 2]\n        note: \"R1 提出，R2 AGREE。Simple-mean C%=29.2% vs weighted-mean C%=13.5%。\"\n      - round: 20\n        reviewers: [1, 2]\n        note: \"R20-R1-W1 + R20-R2-W3 再次提出。R20 action (改用 29.2%+CI) 标记 done，但 Abstract 仍使用 '31%'。两位 Reviewer 要求 Abstract 使用 DEFF 校正后数字 + family 定义敏感性分析。\"\n    action_items:\n      - round: 20\n        action: \"根因修复：Abstract/Intro/Conclusion/Discussion 全部移除 13.5%，改用 29.2% + cluster bootstrap CI [26.7%, 53.2%]。\"\n        assigned_to: director\n        status: done\n      - round: 20\n        action: \"Abstract 仍使用 raw 31%，需改为 DEFF 校正后 ~29% 或报告区间；补充 family 定义敏感性分析收窄 C% 区间\"\n        assigned_to: director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-N2\"\n    summary: \"Semi-synthetic 注入用 uniform binary flipping，检测力估计可能被系统性高估\"\n    category: method\n    severity: critical\n    status: in_progress\n    first_raised_round: 19\n    last_seen_round: 20\n    mentions:\n      - round: 19\n        reviewers: [1, 2]\n        note: \"R1 提出，R2 AGREE。Graded shift (Δp=0.1-0.3) 下检测力可能远低于报告值。\"\n      - round: 20\n        reviewers: [1, 2]\n        note: \"R20-R1-W2 再次提出（Critical）。R2 AGREE 但指出论文已有部分回应（difficulty-dependent ΔTPR≈0.41, ~20% bound）。Reviewer 认为 reframe as upper bound 已完成，但仍需更多注入模式验证。\"\n    action_items:\n      - round: 20\n        action: \"§4.5 reframe as calibration upper bound + 20% overestimation bound; Figure 2 caption 加 calibration framing\"\n        assigned_to: director\n        status: done\n      - round: 20\n        action: \"考虑补充 graded injection 实验（ε 按难度/能力衰减），但 R2 认为当前 ~20% bound 已基本足够\"\n        assigned_to: director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-N3\"\n    summary: \"DIF 在 LLM 场景下的概念合法性——impact vs bias 区分 + 多维性伪影\"\n    category: method\n    severity: critical\n    status: in_progress\n    first_raised_round: 19\n    last_seen_round: 20\n    mentions:\n      - round: 19\n        reviewers: [1, 2]\n        note: \"R1 提出，R2 强烈 AGREE。DIF 是 bias 的必要非充分条件。\"\n      - round: 20\n        reviewers: [1, 2]\n        note: \"R20-R2-W5 扩展为更广泛的概念合法性问题：2023 vs 2024 模型不是同一总体子群；κ=0.80 意味着 20% DIF 项可能是多维性伪影；需讨论何时 DIF 反映测量问题 vs 合法能力变化。R1 部分 REBUT（DIF 对跨时间群体有效，Q3 diagnostic 部分缓解）。\"\n    action_items:\n      - round: 20\n        action: \"§5.2 Correct 步骤重写：DIF flags → expert review，DIF is necessary but not sufficient for item bias\"\n        assigned_to: director\n        status: done\n      - round: 20\n        action: \"补充讨论：LLM temporal DIF 何时反映测量问题 vs 合法能力结构变化；κ=0.80 的多维性伪影含义\"\n        assigned_to: director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-N4\"\n    summary: \"DIF-contamination 近独立性推断强度过高——web-overlap proxy 噪声可能驱动低 φ\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 19\n    last_seen_round: 20\n    mentions:\n      - round: 19\n        reviewers: [1, 2]\n        note: \"R2 提出，R1 AGREE。Jaccard≈0.20 可能反映 proxy 低质量。\"\n      - round: 20\n        reviewers: [1, 2]\n        note: \"R20-R1-W7 再次提出。R2 AGREE。论文已加 proxy 声明但 'complementary diagnostic dimensions' 措辞仍过强。建议改为 'low correlation with available contamination proxies, though proxy noise may attenuate the measured association'。\"\n    action_items:\n      - round: 20\n        action: \"§4.3 标题改为 Comparison with Web-Overlap Labels；proxy 声明 + label-independent evidence\"\n        assigned_to: director\n        status: done\n      - round: 20\n        action: \"进一步弱化 'complementary diagnostic dimensions' 措辞\"\n        assigned_to: director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-W2\"\n    summary: \"Cross-subject matching ΔFPR=0 在 k=5-15 区间退化未充分表征\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 19\n    last_seen_round: 20\n    mentions:\n      - round: 19\n        reviewers: [1, 2]\n        note: \"R1-W2, R2 AGREE。k=20 ΔFPR=0.069，但未模拟 k=30/50。\"\n      - round: 20\n        reviewers: [1, 2]\n        note: \"R20-R1-W4 再次提出（Major）。Table 7 报告 k=20/30/40/50，但 k=5-15 区间仍缺系统刻画。R2 部分 AGREE（加分项而非否决性缺陷）。\"\n    action_items:\n      - round: 19\n        action: \"模拟 k=30/50 的 ΔFPR；讨论高 contamination 覆盖率下的替代策略\"\n        assigned_to: paper_agent\n        status: open\n      - round: 20\n        action: \"补充 k=5,8,10,15 的 ΔFPR 数据点，刻画完整退化曲线\"\n        assigned_to: director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-W3\"\n    summary: \"Mechanism-agnostic 定位与 contamination-centric 验证/叙事存在张力\"\n    category: framing\n    severity: warning\n    status: in_progress\n    first_raised_round: 19\n    last_seen_round: 20\n    mentions:\n      - round: 19\n        reviewers: [1, 2]\n        note: \"R1-W3, R2 AGREE。Related Work 以 Contamination Detection 开篇。\"\n      - round: 20\n        reviewers: [1, 2]\n        note: \"R20-R2-W4 再次提出（Major），R1 AGREE。Related Work 已重排但验证框架仍完全基于 contamination injection。需至少一个非 contamination DIF 验证。\"\n    action_items:\n      - round: 20\n        action: \"Related Work 段落重排已完成\"\n        assigned_to: director\n        status: done\n      - round: 20\n        action: \"补充至少一个非 contamination 来源的 DIF 验证（如训练方法变化模拟）\"\n        assigned_to: director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-W4\"\n    summary: \"ETS 阈值从人类考生迁移到 LLM 缺乏 substantive meaning 讨论\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 19\n    last_seen_round: 20\n    mentions:\n      - round: 19\n        reviewers: [1, 2]\n        note: \"R2-W1, R1 AGREE。Random-split P99=1.45 是 necessary 但非 sufficient。\"\n      - round: 20\n        reviewers: [1, 2]\n        note: \"R20-R1-W5 再次提出（Major），R2 AGREE。虽已连接 Monte Carlo power + random-split FPR，但仍未讨论 |Δ_MH|=1.5 对 LLM 的实质含义。需 LLM-specific 阈值校准或 substantive meaning 讨论。\"\n    action_items:\n      - round: 20\n        action: \"§4.2 显式连接 Monte Carlo power analysis (TPR ≥ 0.68) 与 random-split FPR < 1%\"\n        assigned_to: director\n        status: done\n      - round: 20\n        action: \"添加 ETS 阈值在 LLM 场景下实质含义的讨论段落，或提供 data-driven 阈值校准\"\n        assigned_to: director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-D1\"\n    summary: \"[分歧] 方法论新颖性是否足够\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 19\n    last_seen_round: 20\n    mentions:\n      - round: 19\n        reviewers: [1, 2]\n        note: \"R2 认为直接搬运，R1 反驳 cross-subject matching 和 DEFF 是 LLM-specific 贡献。\"\n      - round: 20\n        reviewers: [1, 2]\n        note: \"R20-R2-W2 再次提出（Critical）。R1 部分 REBUT：cross-subject matching 适配 + semi-synthetic framework + 四个 LLM challenges 的解决是 non-trivial。但 R2 坚持对 EMNLP 方法论贡献不足。分歧持续。\"\n    action_items:\n      - round: 19\n        action: \"Introduction 中更清晰区分 borrowed methodology 和 novel adaptations\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-W1\"\n    summary: \"标题 'Score Incomparability' 与 ρ≈0.997 的核心发现存在根本性叙事张力\"\n    category: framing\n    severity: critical\n    status: open\n    first_raised_round: 20\n    last_seen_round: 20\n    mentions:\n      - round: 20\n        reviewers: [1, 2]\n        note: \"R2 提出（Critical），R1 AGREE。标题暗示分数不可比较，但 ρ≈0.997 表明排名几乎完美保持。'The result is sobering' 与 aggregate robustness 不匹配。论文实际展示 item-level instability with aggregate robustness。\"\n    action_items:\n      - round: 20\n        action: \"修改标题为更准确的措辞（如 Temporal Item-Level Instability / Differential Item Functioning）；弱化 'sobering' 等措辞\"\n        assigned_to: director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-W8\"\n    summary: \"Base-vs-instruct 反向模式（χ²=562.7）机制解释不足——RLHF 可能产生 DIF-like artifacts\"\n    category: method\n    severity: warning\n    status: open\n    first_raised_round: 20\n    last_seen_round: 20\n    mentions:\n      - round: 20\n        reviewers: [1, 2]\n        note: \"R1-W8 提出，R2-Q3 同一问题。RLHF/instruction tuning 系统性改变 MCQ 应答策略（format preference, safety behavior），可能产生 DIF-like artifacts 而非 item-level bias。Appendix O (Table 15) 的 base-only/instruct-only 分析应提升到主文。\"\n    action_items:\n      - round: 20\n        action: \"讨论 base/instruct format sensitivity 作为替代解释；将 Table 15 base-only/instruct-only temporal DIF 提升到主文\"\n        assigned_to: director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-W11\"\n    summary: \"Contribution 3 (audit protocol) 仅半段，无部署验证\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 20\n    last_seen_round: 20\n    mentions:\n      - round: 20\n        reviewers: [1, 2]\n        note: \"R2-W6 提出（Minor），R1 AGREE。Section 5.2 仅半段，没有 case study 或用户验证。\"\n    action_items:\n      - round: 20\n        action: \"降级为 future direction，或扩展为独立 subsection 并提供模拟部署场景\"\n        assigned_to: director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R20-MR1\"\n    summary: \"遗漏 Rodriguez et al. (2021) 'Evaluation Examples Are Not Equally Informative' (ACL)\"\n    category: writing\n    severity: info\n    status: open\n    first_raised_round: 20\n    last_seen_round: 20\n    mentions:\n      - round: 20\n        reviewers: [1, 2]\n        note: \"R2 提出，R1 AGREE。IRT+NLP 评估的奠基性工作，应被引用。\"\n    action_items:\n      - round: 20\n        action: \"Related Work 中引用 Rodriguez et al. (2021)\"\n        assigned_to: director\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  # === Round 19 issues not raised in Round 20 ===\n\n  - id: \"R19-W1\"\n    summary: \"Calendar-year cohort boundary 粗糙——temporal framing 过窄\"\n    category: method\n    severity: warning\n    status: in_progress\n    first_raised_round: 19\n    last_seen_round: 20\n    mentions:\n      - round: 19\n        reviewers: [1, 2]\n        note: \"R1-W1 + R2-W3。Release date ≠ training cutoff。\"\n      - round: 20\n        reviewers: []\n        note: \"本轮未作为独立 weakness 提出，但 Q2/Q4 仍涉及时间粒度问题。R20 action (temporal = cohort-based shorthand) 已完成。降级为 question 级别。\"\n    action_items:\n      - round: 20\n        action: \"§5.1 加入 'temporal = cohort-based shorthand'，明确 cohorts differ in architecture/data/methodology simultaneously\"\n        assigned_to: director\n        status: done\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-W5\"\n    summary: \"与 Growing Pains (Habba et al., 2026) 差异化论证不够深入\"\n    category: framing\n    severity: warning\n    status: open\n    first_raised_round: 19\n    last_seen_round: 19\n    mentions:\n      - round: 19\n        reviewers: [1, 2]\n        note: \"R2-W2, R1 AGREE（优先级不高）。\"\n      - round: 20\n        reviewers: []\n        note: \"本轮未提及，可能已通过 Related Work 改进修复，待 Research Director 确认\"\n    action_items:\n      - round: 19\n        action: \"附录中加入与 Growing Pains 在相同 items 上的交叉比较\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  - id: \"R19-W6\"\n    summary: \"Score correction 展示不充分且缺乏 impact/bias 区分作为方法论基础\"\n    category: writing\n    severity: warning\n    status: open\n    first_raised_round: 19\n    last_seen_round: 19\n    mentions:\n      - round: 19\n        reviewers: [1, 2]\n        note: \"R2-W5, R1 AGREE。§4.6 仅半页。N3 fix provides conceptual foundation。\"\n      - round: 20\n        reviewers: []\n        note: \"本轮未提及，可能已通过 §5.2 Correct 步骤重写修复，待 Research Director 确认\"\n    action_items:\n      - round: 19\n        action: \"扩展 §4.6 或附录 case study\"\n        assigned_to: paper_agent\n        status: open\n    resolution: \"\"\n    resolution_round: null\n\n  # === Round 17 issues (all resolved) ===\n\n  - id: \"R17-N1\"\n    summary: \"DEFF 估计量选择论证存在循环性\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 17\n    last_seen_round: 17\n    resolution: \"区间表述 → R19 再次提出（R19-N1）\"\n    resolution_round: 18\n\n  - id: \"R17-N2\"\n    summary: \"Semi-synthetic ΔTPR upper bound 声称不严密\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 17\n    last_seen_round: 17\n    resolution: \"reference-case 替换 → R19 要求 graded injection（R19-N2）\"\n    resolution_round: 18\n\n  - id: \"R17-W1\"\n    summary: \"Mechanism-agnostic 定位与 contamination-centric 叙事张力\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 17\n    last_seen_round: 17\n    resolution: \"§3.4 + §5.1 标记。R19 要求更彻底 reframing（R19-W3）\"\n    resolution_round: 18\n\n  - id: \"R17-W2\"\n    summary: \"与 Growing Pains 差异化\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 17\n    last_seen_round: 17\n    resolution: \"Related Work 两点区分。R19 仍要求更深入（R19-W5）\"\n    resolution_round: 18\n\n  - id: \"R17-W3\"\n    summary: \"k>5 时 ΔFPR 退化\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 17\n    last_seen_round: 17\n    resolution: \"已量化。R19 要求 k=30/50（R19-W2）\"\n    resolution_round: 18\n\n  - id: \"R17-W4\"\n    summary: \"DIF-contamination 正交性需替代解释\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 17\n    last_seen_round: 17\n    resolution: \"两种解释 + OR=4.75。R19 要求 proxy 讨论（R19-N4）\"\n    resolution_round: 18\n\n  - id: \"R17-W5\"\n    summary: \"时间粒度选择未经论证\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 17\n    last_seen_round: 17\n    resolution: \"半年粒度 + Limitations。R19 仍指出（R19-W1）\"\n    resolution_round: 18\n\n  - id: \"R17-W6\"\n    summary: \"Abstract 信息过载\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 17\n    last_seen_round: 17\n    resolution: \"~122 words。R19 未复发\"\n    resolution_round: 18\n\n  - id: \"R17-M1\"\n    summary: \"ρ≈0.997 与 ±800 displacement 共存机制\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 17\n    last_seen_round: 17\n    resolution: \"§4.6 解释 closely-ranked pairs\"\n    resolution_round: 18\n\n  # === Round 16 issues (all resolved) ===\n\n  - id: \"R16-N1\"\n    summary: \"ETS 阈值校准\"\n    category: method\n    severity: critical\n    status: resolved\n    first_raised_round: 15\n    last_seen_round: 16\n    resolution: \"P99=1.45。R19 降级为 W4\"\n    resolution_round: 17\n\n  - id: \"R16-N2\"\n    summary: \"Contribution 过度定位\"\n    category: framing\n    severity: critical\n    status: resolved\n    first_raised_round: 13\n    last_seen_round: 16\n    resolution: \"3→2 contributions\"\n    resolution_round: 17\n\n  - id: \"R16-W1\"\n    summary: \"DEFF 差异 2×\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 13\n    last_seen_round: 16\n    resolution: \"区间表述。R19 再次提出\"\n    resolution_round: 18\n\n  - id: \"R16-W2\"\n    summary: \"审计协议超出方法能力\"\n    category: framing\n    severity: warning\n    status: resolved\n    first_raised_round: 15\n    last_seen_round: 16\n    resolution: \"DIF alone cannot determine causation\"\n    resolution_round: 17\n\n  - id: \"R16-W3\"\n    summary: \"Discussion 缺深层 insight\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 16\n    resolution: \"§5.1 三个区分\"\n    resolution_round: 17\n\n  - id: \"R16-W4\"\n    summary: \"Abstract 信息密度过高\"\n    category: writing\n    severity: warning\n    status: resolved\n    first_raised_round: 14\n    last_seen_round: 16\n    resolution: \"精简到 ~122 words\"\n    resolution_round: 18\n\n  - id: \"R16-W5\"\n    summary: \"主文超页\"\n    category: format\n    severity: warning\n    status: resolved\n    first_raised_round: 14\n    last_seen_round: 16\n    resolution: \"8 页内\"\n    resolution_round: 17\n\n  - id: \"R16-W6\"\n    summary: \"ΔTPR 应标为上界\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 13\n    last_seen_round: 16\n    resolution: \"reference-case\"\n    resolution_round: 18\n\n  - id: \"R16-M1\"\n    summary: \"术语不一致\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 14\n    last_seen_round: 16\n    resolution: \"§1 定义\"\n    resolution_round: 17\n\n  - id: \"R16-M2\"\n    summary: \"有效 N vs 总 N 澄清\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 16\n    resolution: \"§3.2 已修正\"\n    resolution_round: 17\n\n  - id: \"R16-M3\"\n    summary: \"遗漏相关工作\"\n    category: writing\n    severity: info\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 16\n    resolution: \"新引用已加\"\n    resolution_round: 17\n\n  - id: \"R16-DATA1\"\n    summary: \"random-split baseline 0.18% 来自单次运行\"\n    category: method\n    severity: warning\n    status: resolved\n    first_raised_round: 16\n    last_seen_round: 16\n    resolution: \"全文修正 0.18→0.62\"\n    resolution_round: 17"
  }
}
```

</details>

---


### Tool result

_source line 1784 · 2026-05-25T21:33:43.186774+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/review_issues.yaml\", \"bytes\": 16501}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 1785 · 2026-05-25T21:36:39.401201+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "irt_equated_bench_regen",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.5 (Borderline Conference)",
  "report": "# Round 20 审稿报告 — Temporal Score Incomparability in LLM Benchmarks\n\n**论文**: Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models\n**Venue**: EMNLP 2026 (ARR May cycle)\n**Reviewer 配置**: 2 人（R1: 方法严谨性+实验有效性; R2: 新颖性/定位+完整性）\n**审稿轮次**: Round 1（1 轮收敛，无需第 2 轮）\n\n---\n\n## Summary\n\n本文将教育测量学中的 Mantel-Haenszel 差异项目功能（MH-DIF）分析引入 LLM 基准测试的时序可比性检验，基于 METABENCH 响应矩阵（5,227 模型 × 12,508 MMLU 题目）发现约 29–31% 的题目在 2023 与 2024 模型群组间呈现大效应 DIF（ETS C 类），且该信号与 web-overlap 污染标签低相关（φ = 0.012）。论文开发了 cross-subject matching 半合成验证框架（ΔFPR = 0 构造性保证），在六个基准上复现了发现（17.9–31.3%），并提出 Monitor/Triage/Correct 审计协议。\n\n---\n\n## Strengths\n\n**S1. 问题定位精准且及时。** [R1-S1, R2-S1] 将 measurement invariance 引入 LLM 评估填补了重要方法论空白。5,227 模型 × 12,508 题目 × 6 基准的规模在同类工作中罕见，核心发现在所有基准上复现（Table 2: C% 17.9–31.3%）。\n\n**S2. Cross-subject matching 设计巧妙。** [R1-S3, R2-S3] 将 purified subtest matching 适配到 LLM 多学科场景，ΔFPR = 0 的构造性保证（Section 3.4 Remark）是方法论亮点。Figure 5 清晰展示 FPR 控制差异。\n\n**S3. 多层次控制实验设计严谨。** [R1-S4, R2-S2] 五种 cohort 对比、DEFF 校正、cluster bootstrap、LOFO 家族分析、random-split baseline（0.62% vs 31.3% = 50×）、IRT θ-conditioning（r = 0.9986）从多角度排除混淆。\n\n**S4. 概念框架有教育意义。** [R2-S4] Figure 2 通过 ICC 曲线清晰展示 global exposure vs differential functioning 区别，对 NLP 评估社区有启发价值。\n\n**S5. Base-vs-instruct 方向反转是有价值的发现。** [R2-S6] χ² = 562.7 的结构化方向性差异超越简单二分法，指向训练方法论对测量特性的系统性影响。\n\n**S6. 心理测量概念解释充分。** [R2-S5, R1-S6] Section 3.2 对 MH/ETS/DIF 概念的铺垫和 Figure 1 pipeline 图对 NLP 读者友好。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收的关键问题）\n\n**W1. [Critical, Consensus] 标题 \"Score Incomparability\" 与核心发现 ρ ≈ 0.997 存在根本性叙事张力。**\n标题暗示分数不可比较，但核心实证发现恰恰是排名几乎完美保持（Table 2: ρ ≈ 0.997, flip rate ≤ 2.9%）。Introduction \"The result is sobering\" 放大了此不匹配。论文实际展示的是 item-level instability with aggregate robustness——31% 的题目有大效应 DIF，但聚合排名几乎不变。虽然个别模型可移动 ±561 位（Appendix），DIF-ordered removal 比 random removal 更快降低 ρ（Figure 6），但 aggregate 层面的近乎完美保持使 \"incomparability\" 一词明显过度。\n- R1: AGREE | R2: 原始提出\n- **跨轮状态**: 新发现（R20 首次提出）\n- **建议**: 标题改为更准确的措辞（如 \"Temporal Item-Level Instability\" 或 \"Differential Item Functioning\"）；弱化 \"sobering\" 等措辞\n\n**W2. [Critical, Consensus] 核心 C% 数字的不确定性范围过大（13.5%–31.3%），且 Abstract 使用未校正值。**\nAbstract 使用 \"31%\" 作为 headline claim，但 DEFF 校正后 simple-mean = 29.2%、weighted-mean = 13.5%，2.3× 范围（Section 4.2, Appendix D Table 10）。Cluster bootstrap CI [26.7%, 53.2%] 排除 weighted-mean 的 13.5%，但 bootstrap 依赖于 family 定义的合理性（Appendix I: 30 families with ≥2 members），论文未提供 family 定义的敏感性分析。如果真实 C% 接近 13.5%，\"50× above random\" 变为 ~22×，叙事力度显著减弱。\n- R1: 原始提出 | R2: AGREE\n- **跨轮状态**: R19-N1 再次出现。R19→R20 action（改用 29.2% + CI）标记 done，但 Abstract 仍使用 raw \"31%\"\n- **建议**: Abstract 使用 DEFF 校正后数字（~29% 或报告区间）；提供 family 定义敏感性分析收窄区间\n\n**W3. [Critical, Divergence] 方法论新颖性有限——核心方法均为已知技术的直接应用/适配。**\nMH-DIF (Holland & Thayer, 1988)、ETS A/B/C 分类、cross-subject matching (purified subtest matching, Swaminathan & Rogers, 1990)、DEFF 校正 (Rao & Scott, 1992) 均非原创。论文的四个 LLM-specific challenges（Section 3.2）的解决方案也是现有方法（permutation simulation、DEFF、quintile stratification、cross-subject matching）。\n- R1: 部分 REBUT——cross-subject matching 适配、semi-synthetic injection framework、四个 LLM-specific challenges 的系统性解决是 non-trivial 的设计创新；对 EMNLP 而言，成熟方法严谨适配到新领域并通过大规模实证验证本身有价值\n- R2: 原始提出——NLP 顶会对方法论创新要求高于\"已知方法到新领域的迁移\"\n- **跨轮状态**: R19-D1 分歧持续\n- **建议**: Introduction 更清晰区分 borrowed methodology 与 novel adaptations；标注哪些是已知方法、哪些是本文的适配创新\n\n### Should-Fix（显著影响论文质量）\n\n**W4. [Major, Consensus] \"Mechanism-agnostic\" 定位与 contamination-centric 验证/叙事存在张力。**\n论文声称 DIF 是 mechanism-agnostic（Section 5.1: \"Temporal DIF detects *that* items function differently...not *why*\"），但：(1) 验证框架完全基于 contamination injection（Section 3.4）；(2) Section 4.3 大量对比 web-overlap labels；(3) Discussion（Section 5.2）建议 contamination-motivated item removal。如果方法真正 mechanism-agnostic，至少应包含一个非 contamination 来源的 DIF 验证（如模拟训练方法变化）。\n- R1: AGREE | R2: 原始提出\n- **跨轮状态**: R19-W3 再次出现。Related Work 重排已完成，但验证框架仍单一\n- **建议**: 补充至少一个非 contamination 来源的 DIF 验证\n\n**W5. [Major, Consensus] Semi-synthetic 注入使用 uniform binary flipping，可能高估检测力。**\n论文在 Limitations (1) 和 Section 3.4 已承认此局限（\"reported ΔTPR values may overestimate detection power\"），Section 4.4 的 difficulty-dependent injection 量化了 ~20% 高估（ΔTPR ≈ 0.41 vs 0.51）。但验证框架仅覆盖 contamination 注入的不同变体，未覆盖其他 DIF 机制。\n- R1: 原始提出 | R2: AGREE（指出论文已有部分回应，~20% bound）\n- **跨轮状态**: R19-N2 再次出现。Reframe as calibration upper bound 已完成\n- **建议**: 考虑补充 graded injection 实验\n\n**W6. [Major, Consensus] ETS 阈值从人类考生迁移到 LLM 缺乏 substantive meaning 讨论。**\nETS A/B/C 阈值校准于人类教育测试群体。LLM 无真正 latent ability trait；within-family 高同质性 inflate sample size 但不增独立信息。跨阈值鲁棒性分析（Section 4.2: 18.4% at |Δ_MH| ≥ 2.0, 10.2% at ≥ 2.5）部分缓解阈值选择的任意性，但论文未讨论 |Δ_MH| = 1.5 对 LLM 的实质含义，也未提供 LLM-specific 阈值校准。\n- R1: 原始提出 | R2: AGREE\n- **跨轮状态**: R19-W4 再次出现。已连接 Monte Carlo power + random-split FPR，但 reviewer 要求更深入\n- **建议**: 添加 ETS 阈值在 LLM 场景下实质含义的讨论段落\n\n**W7. [Major, Divergence] DIF 在 LLM 场景下的概念合法性讨论不足。**\n2023 vs 2024 模型不是同一总体的人口学子群，而是技术上根本不同的系统。κ = 0.80（cross-subject vs within-subject matching agreement）意味着 20% 的 DIF 项目可能是多维性伪影。需讨论：何时 LLM temporal DIF 反映测量问题（item 有问题）vs 合法能力结构变化（model 本来就不同）。\n- R1: 部分 REBUT——DIF 对跨时间群体也有效（教育测量先例），Q3 diagnostic + cross-subject matching 部分缓解多维性\n- R2: 原始提出\n- **建议**: 补充讨论 LLM temporal DIF 的概念边界\n\n**W8. [Major, Consensus] Base-vs-instruct 反向模式（χ² = 562.7）机制解释不足。**\nRLHF/instruction tuning 系统性地改变模型与 MCQ 的交互方式（format preference, safety behavior, calibration），这些都可能产生 DIF-like artifacts 而非真正的 item-level bias。论文在 Section 5.1 将反转解释为 \"structured item-level bias rather than uniform group impact\"，但未排除上述 confound。Appendix O (Table 15) 的 base-only/instruct-only temporal DIF 分析应被提升到主文以回应此质疑。\n- R1: 原始提出 | R2: AGREE\n- **跨轮状态**: 新发现（R20 首次提出）\n- **建议**: 讨论 format sensitivity 作为替代解释；将 Table 15 提升到主文\n\n**W9. [Major, Partial Consensus] Cross-subject ΔFPR = 0 保证在 k = 5–15 区间退化未充分表征。**\nk ≤ 5 ΔFPR < 0.007，k = 20 ΔFPR = 0.167。中间区域缺乏系统刻画，对 practitioner 判断何时切换 within-subject matching 至关重要。\n- R1: 原始提出 | R2: 部分 AGREE（\"加分项\"而非\"否决性\"缺陷）\n- **跨轮状态**: R19-W2 再次出现\n- **建议**: 补充 k = 5, 8, 10, 15 的 ΔFPR 数据点\n\n**W10. [Moderate, Consensus] \"近独立于 web-overlap labels\" 的推断强度过高。**\nφ = 0.012 可能反映 web-overlap labels 的 proxy 噪声而非 DIF 的真正独立性。论文已承认此可能性（Section 4.3），并提供 label-independent 支持证据（base-vs-instruct reversal），但 \"complementary diagnostic dimensions\" 措辞仍过强。\n- R1: 原始提出 | R2: AGREE\n- **建议**: 弱化措辞为 \"low correlation with available contamination proxies\"\n\n**W11. [Minor, Consensus] Contribution 3 (audit protocol) 权重不足。**\nSection 5.2 仅半段，无部署验证、case study 或用户研究。作为声明的三大贡献之一显得单薄。\n- R1: AGREE | R2: 原始提出\n- **建议**: 降级为 future direction，或扩展并提供模拟部署场景\n\n---\n\n## Reviewer Consensus\n\n[AGREE] 双方一致同意的关键问题（7 项）：\n1. 标题 \"Score Incomparability\" 与 ρ ≈ 0.997 的叙事不匹配 (W1)\n2. C% 不确定性和 Abstract headline claim 表述 (W2)\n3. Mechanism-agnostic 定位与 contamination 验证的张力 (W4)\n4. Base-vs-instruct 反转的机制解释不足 (W8)\n5. ETS 阈值迁移的实质含义讨论不足 (W6)\n6. Web-overlap labels 推断强度过高 (W10)\n7. Contribution 3 权重不足 (W11)\n\n## Reviewer Divergence\n\n[REBUT/Partial] 存在分歧的问题（4 项）：\n\n1. **方法论新颖性** (W3): R2 认为核心方法为直接搬运（Critical），R1 反驳 cross-subject matching 适配和 semi-synthetic framework 是 non-trivial 的设计创新。分歧未收敛。\n\n2. **2PL power analysis vs IRT misfit** (R1-W3): R2 反驳——MH-DIF 是非参数方法，power analysis 是辅助证据，实证 50× ratio 是核心。R1 接受但建议论文更明确讨论 2PL misfit 影响。**降级为 minor concern。**\n\n3. **多重比较校正** (R1-W6): R2 反驳——DIF 领域标准实践不做 FWER/FDR correction（Wainer 1993），BH 校正仅影响 3/3918 C items (0.08%)。**降级为 minor concern。**\n\n4. **DIF 概念合法性** (W7): R1 部分反驳——DIF 对跨时间群体有效（教育测量先例），Q3 diagnostic 部分缓解多维性。但同意需更多讨论。\n\n---\n\n## Questions\n\n1. Abstract 是否应使用 DEFF 校正后数字（~29% + CI）而非 raw 31%？为何选择 simple-mean 而非 weighted-mean DEFF？\n2. 能否提供 family 定义的敏感性分析以收窄 C% 区间？\n3. 既然 ρ ≈ 0.997，temporal DIF 的 practical impact 是什么？在什么具体场景下 practitioner 会因忽略 temporal DIF 做出错误决策？\n4. DIF 信号是线性积累还是存在突变点？Rolling-window MH-DIF 分析结果如何？\n5. Base-only / instruct-only temporal DIF (Table 15) 为何不在主文展示？\n6. 如果补充非 contamination 来源的 DIF 验证（如训练方法变化模拟），结果如何？\n7. |Δ_MH| = 1.5 对 LLM 的实质含义是什么？能否提供 LLM-specific 阈值校准？\n8. Cross-subject matching 在全局训练方法变化驱动 DIF 时的行为如何？（R1 论证为 conservative bias，不导致 false positive inflation，但可能 under-powered）\n\n---\n\n## Missing References\n\n1. **Rodriguez et al. (2021) \"Evaluation Examples Are Not Equally Informative\" (ACL 2021)** — IRT+NLP 评估的奠基性工作 [R1 AGREE, R2 提出]\n2. **Polo et al. (2024) \"tinyBenchmarks\" (ICML 2024)** — IRT-based 高效 LLM 评估 [R2 提出; R1 部分 REBUT: 技术路线差异大]\n3. **Vania et al. (2021) \"Comparing Test Sets with Item Response Theory\"** — NLP+IRT 早期工作 [R1 提出]\n4. **van der Linden & Veldkamp (2007)** — Item exposure / test security 文献 [R1 提出; R2: nice-to-have]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未配置，不适用。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成。7 个 info 级别发现，0 critical，0 warning：\n\n- **Page 2**: Figure 1 response matrix 彩色小点灰度打印辨识度不足，建议辅以 marker shape 或 hatching\n- **Page 4**: Figure 3 ETS 颜色编码（A=绿, B=黄, C=红）对红绿色盲不友好，建议改用 Okabe-Ito 色板或 blue-orange 方案\n- **Page 5**: Figure 4 x 轴标签字号偏小，部分重叠，建议调整间距或旋转\n- **Page 7**: Figure 6 五个面板 tick/legend 文字偏小（约正文 60-65%），建议增大字号\n- **Page 8**: 右栏内容密度极高（§4.5–4.7 + §5 + §6），无 display item 穿插，但作为 Discussion/Conclusion 区域属正常安排\n- **Page 13**: Tables 6–8 密集排布，单个表格行数少（3-5 行），可考虑合并\n- **Page 14**: Table 10 列头缩写较多，建议 caption 解释\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.5 (Borderline Conference)**\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 3/5 | 4/5 | 3.5/5 |\n| Excitement | 3.5/5 | 3/5 | 3.0/5 |\n| Reproducibility | 4/5 | — | 4/5 |\n| Confidence | 4/5 | 4/5 | 4/5 |\n\n**综合评判**: 这是一篇执行质量高的大规模实证论文，问题重要且及时，多层次验证设计严谨，cross-subject matching 的 ΔFPR = 0 保证有方法论价值。但存在三个核心障碍阻碍其升至 Conference (4.0)：\n\n1. **叙事过度**: 标题 \"Score Incomparability\" 与 ρ ≈ 0.997 的发现直接矛盾；Abstract 使用未校正的 31% 而非 DEFF 校正后的区间\n2. **方法论新颖性争议**: 核心统计方法均为 30+ 年历史的标准工具，LLM-specific 适配的创新程度在两位 reviewer 间有分歧\n3. **验证框架单一**: 声称 mechanism-agnostic 但验证完全基于 contamination injection\n\n**升至 Conference (4.0) 的路径** (rebuttal 可解决)：\n- (a) 修改标题和 Abstract，使用 DEFF 校正后数字，诚实反映不确定性\n- (b) 在 Introduction 中明确区分 borrowed methodology 与 novel adaptations\n- (c) 补充至少一个非 contamination DIF 机制的验证\n- (d) 讨论 ETS 阈值在 LLM 场景下的 substantive meaning\n- (e) 提供 family 定义敏感性分析以收窄 C% 区间\n- (f) 将 base-only/instruct-only temporal DIF (Table 15) 提升到主文\n\n**作为 Findings 论文** (3.0–3.5): 论文完全达标——规模大、执行扎实、对社区有诊断价值。\n\n---\n\n## Detailed Comments\n\n**Abstract**: 信息密度适中（~150 words，符合 ≤200 words 要求），但 \"31%\" headline 未反映 DEFF 校正后的不确定性。\"near-independent\" 措辞过强。\n\n**Introduction (Section 1)**: Figure 1 pipeline 图信息量大，四步管线清晰。三个 contributions 权重不均：C3 (audit protocol) 后续 Section 5.2 仅半段，缺乏部署验证。\"The result is sobering\" 与 ρ ≈ 0.997 的 aggregate robustness 不一致。\n\n**Related Work (Section 2)**: 组织合理（Psychometric Methods → Contamination Detection → Benchmark Quality）。与 Growing Pains 的区分清晰（nonparametric vs parametric, DIF diagnosis vs score equating）。遗漏 Rodriguez et al. (2021)。\n\n**Method (Section 3)**: MH-DIF 和 ETS 分类的解释清晰，包括公式推导（Eq. 1-2）和四个 LLM-specific challenges 的讨论。Cross-subject matching 的 Remark 论证有说服力。Semi-synthetic injection 的 uniform flipping 局限性在 Limitations 中承认，但 Section 3.4 正文措辞不够 cautious——应在首次提出时标注 \"calibration upper bound\"。\n\n**Experiments (Section 4)**: 多层次控制设计严谨。Section 4.2 的 DEFF 区间处理（\"bracketing C% at 13.5–29.2%\"）不够 transparent——应在主文而非仅附录讨论 estimator 选择。Section 4.3 的 web-overlap 分析有 proxy noise confound。Section 4.2 \"DIF rates are domain-invariant (KW p = 0.78)\" 与 \"DIF direction exhibits domain dependence\" 的并置需更清晰铺垫。\n\n**Discussion (Section 5)**: Section 5.1 的 base-vs-instruct 分析有价值但机制解释不足——需讨论 format sensitivity 作为替代解释。Section 5.2 audit protocol 过于简短。\n\n**Conclusion (Section 6)**: 单句 conclusion 信息量可接受但给人仓促收尾之感。\n\n**Limitations**: 覆盖 3 个关键局限（injection realism, non-independence, cross-subject matching boundary），符合 EMNLP 要求。\n\n**Appendix**: A–Q (17 个) 内容详尽，但数量较多，可考虑合并部分相关性强的 appendix。\n\n**Format**: 正文 8 页内符合限制；Limitations 在第 9 页不计入页数；匿名链接 anonymous.4open.science 格式正确；引用格式符合 ACL 规范。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "irt_equated_bench_regen",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.5 (Borderline Conference)",
    "report": "# Round 20 审稿报告 — Temporal Score Incomparability in LLM Benchmarks\n\n**论文**: Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models\n**Venue**: EMNLP 2026 (ARR May cycle)\n**Reviewer 配置**: 2 人（R1: 方法严谨性+实验有效性; R2: 新颖性/定位+完整性）\n**审稿轮次**: Round 1（1 轮收敛，无需第 2 轮）\n\n---\n\n## Summary\n\n本文将教育测量学中的 Mantel-Haenszel 差异项目功能（MH-DIF）分析引入 LLM 基准测试的时序可比性检验，基于 METABENCH 响应矩阵（5,227 模型 × 12,508 MMLU 题目）发现约 29–31% 的题目在 2023 与 2024 模型群组间呈现大效应 DIF（ETS C 类），且该信号与 web-overlap 污染标签低相关（φ = 0.012）。论文开发了 cross-subject matching 半合成验证框架（ΔFPR = 0 构造性保证），在六个基准上复现了发现（17.9–31.3%），并提出 Monitor/Triage/Correct 审计协议。\n\n---\n\n## Strengths\n\n**S1. 问题定位精准且及时。** [R1-S1, R2-S1] 将 measurement invariance 引入 LLM 评估填补了重要方法论空白。5,227 模型 × 12,508 题目 × 6 基准的规模在同类工作中罕见，核心发现在所有基准上复现（Table 2: C% 17.9–31.3%）。\n\n**S2. Cross-subject matching 设计巧妙。** [R1-S3, R2-S3] 将 purified subtest matching 适配到 LLM 多学科场景，ΔFPR = 0 的构造性保证（Section 3.4 Remark）是方法论亮点。Figure 5 清晰展示 FPR 控制差异。\n\n**S3. 多层次控制实验设计严谨。** [R1-S4, R2-S2] 五种 cohort 对比、DEFF 校正、cluster bootstrap、LOFO 家族分析、random-split baseline（0.62% vs 31.3% = 50×）、IRT θ-conditioning（r = 0.9986）从多角度排除混淆。\n\n**S4. 概念框架有教育意义。** [R2-S4] Figure 2 通过 ICC 曲线清晰展示 global exposure vs differential functioning 区别，对 NLP 评估社区有启发价值。\n\n**S5. Base-vs-instruct 方向反转是有价值的发现。** [R2-S6] χ² = 562.7 的结构化方向性差异超越简单二分法，指向训练方法论对测量特性的系统性影响。\n\n**S6. 心理测量概念解释充分。** [R2-S5, R1-S6] Section 3.2 对 MH/ETS/DIF 概念的铺垫和 Figure 1 pipeline 图对 NLP 读者友好。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收的关键问题）\n\n**W1. [Critical, Consensus] 标题 \"Score Incomparability\" 与核心发现 ρ ≈ 0.997 存在根本性叙事张力。**\n标题暗示分数不可比较，但核心实证发现恰恰是排名几乎完美保持（Table 2: ρ ≈ 0.997, flip rate ≤ 2.9%）。Introduction \"The result is sobering\" 放大了此不匹配。论文实际展示的是 item-level instability with aggregate robustness——31% 的题目有大效应 DIF，但聚合排名几乎不变。虽然个别模型可移动 ±561 位（Appendix），DIF-ordered removal 比 random removal 更快降低 ρ（Figure 6），但 aggregate 层面的近乎完美保持使 \"incomparability\" 一词明显过度。\n- R1: AGREE | R2: 原始提出\n- **跨轮状态**: 新发现（R20 首次提出）\n- **建议**: 标题改为更准确的措辞（如 \"Temporal Item-Level Instability\" 或 \"Differential Item Functioning\"）；弱化 \"sobering\" 等措辞\n\n**W2. [Critical, Consensus] 核心 C% 数字的不确定性范围过大（13.5%–31.3%），且 Abstract 使用未校正值。**\nAbstract 使用 \"31%\" 作为 headline claim，但 DEFF 校正后 simple-mean = 29.2%、weighted-mean = 13.5%，2.3× 范围（Section 4.2, Appendix D Table 10）。Cluster bootstrap CI [26.7%, 53.2%] 排除 weighted-mean 的 13.5%，但 bootstrap 依赖于 family 定义的合理性（Appendix I: 30 families with ≥2 members），论文未提供 family 定义的敏感性分析。如果真实 C% 接近 13.5%，\"50× above random\" 变为 ~22×，叙事力度显著减弱。\n- R1: 原始提出 | R2: AGREE\n- **跨轮状态**: R19-N1 再次出现。R19→R20 action（改用 29.2% + CI）标记 done，但 Abstract 仍使用 raw \"31%\"\n- **建议**: Abstract 使用 DEFF 校正后数字（~29% 或报告区间）；提供 family 定义敏感性分析收窄区间\n\n**W3. [Critical, Divergence] 方法论新颖性有限——核心方法均为已知技术的直接应用/适配。**\nMH-DIF (Holland & Thayer, 1988)、ETS A/B/C 分类、cross-subject matching (purified subtest matching, Swaminathan & Rogers, 1990)、DEFF 校正 (Rao & Scott, 1992) 均非原创。论文的四个 LLM-specific challenges（Section 3.2）的解决方案也是现有方法（permutation simulation、DEFF、quintile stratification、cross-subject matching）。\n- R1: 部分 REBUT——cross-subject matching 适配、semi-synthetic injection framework、四个 LLM-specific challenges 的系统性解决是 non-trivial 的设计创新；对 EMNLP 而言，成熟方法严谨适配到新领域并通过大规模实证验证本身有价值\n- R2: 原始提出——NLP 顶会对方法论创新要求高于\"已知方法到新领域的迁移\"\n- **跨轮状态**: R19-D1 分歧持续\n- **建议**: Introduction 更清晰区分 borrowed methodology 与 novel adaptations；标注哪些是已知方法、哪些是本文的适配创新\n\n### Should-Fix（显著影响论文质量）\n\n**W4. [Major, Consensus] \"Mechanism-agnostic\" 定位与 contamination-centric 验证/叙事存在张力。**\n论文声称 DIF 是 mechanism-agnostic（Section 5.1: \"Temporal DIF detects *that* items function differently...not *why*\"），但：(1) 验证框架完全基于 contamination injection（Section 3.4）；(2) Section 4.3 大量对比 web-overlap labels；(3) Discussion（Section 5.2）建议 contamination-motivated item removal。如果方法真正 mechanism-agnostic，至少应包含一个非 contamination 来源的 DIF 验证（如模拟训练方法变化）。\n- R1: AGREE | R2: 原始提出\n- **跨轮状态**: R19-W3 再次出现。Related Work 重排已完成，但验证框架仍单一\n- **建议**: 补充至少一个非 contamination 来源的 DIF 验证\n\n**W5. [Major, Consensus] Semi-synthetic 注入使用 uniform binary flipping，可能高估检测力。**\n论文在 Limitations (1) 和 Section 3.4 已承认此局限（\"reported ΔTPR values may overestimate detection power\"），Section 4.4 的 difficulty-dependent injection 量化了 ~20% 高估（ΔTPR ≈ 0.41 vs 0.51）。但验证框架仅覆盖 contamination 注入的不同变体，未覆盖其他 DIF 机制。\n- R1: 原始提出 | R2: AGREE（指出论文已有部分回应，~20% bound）\n- **跨轮状态**: R19-N2 再次出现。Reframe as calibration upper bound 已完成\n- **建议**: 考虑补充 graded injection 实验\n\n**W6. [Major, Consensus] ETS 阈值从人类考生迁移到 LLM 缺乏 substantive meaning 讨论。**\nETS A/B/C 阈值校准于人类教育测试群体。LLM 无真正 latent ability trait；within-family 高同质性 inflate sample size 但不增独立信息。跨阈值鲁棒性分析（Section 4.2: 18.4% at |Δ_MH| ≥ 2.0, 10.2% at ≥ 2.5）部分缓解阈值选择的任意性，但论文未讨论 |Δ_MH| = 1.5 对 LLM 的实质含义，也未提供 LLM-specific 阈值校准。\n- R1: 原始提出 | R2: AGREE\n- **跨轮状态**: R19-W4 再次出现。已连接 Monte Carlo power + random-split FPR，但 reviewer 要求更深入\n- **建议**: 添加 ETS 阈值在 LLM 场景下实质含义的讨论段落\n\n**W7. [Major, Divergence] DIF 在 LLM 场景下的概念合法性讨论不足。**\n2023 vs 2024 模型不是同一总体的人口学子群，而是技术上根本不同的系统。κ = 0.80（cross-subject vs within-subject matching agreement）意味着 20% 的 DIF 项目可能是多维性伪影。需讨论：何时 LLM temporal DIF 反映测量问题（item 有问题）vs 合法能力结构变化（model 本来就不同）。\n- R1: 部分 REBUT——DIF 对跨时间群体也有效（教育测量先例），Q3 diagnostic + cross-subject matching 部分缓解多维性\n- R2: 原始提出\n- **建议**: 补充讨论 LLM temporal DIF 的概念边界\n\n**W8. [Major, Consensus] Base-vs-instruct 反向模式（χ² = 562.7）机制解释不足。**\nRLHF/instruction tuning 系统性地改变模型与 MCQ 的交互方式（format preference, safety behavior, calibration），这些都可能产生 DIF-like artifacts 而非真正的 item-level bias。论文在 Section 5.1 将反转解释为 \"structured item-level bias rather than uniform group impact\"，但未排除上述 confound。Appendix O (Table 15) 的 base-only/instruct-only temporal DIF 分析应被提升到主文以回应此质疑。\n- R1: 原始提出 | R2: AGREE\n- **跨轮状态**: 新发现（R20 首次提出）\n- **建议**: 讨论 format sensitivity 作为替代解释；将 Table 15 提升到主文\n\n**W9. [Major, Partial Consensus] Cross-subject ΔFPR = 0 保证在 k = 5–15 区间退化未充分表征。**\nk ≤ 5 ΔFPR < 0.007，k = 20 ΔFPR = 0.167。中间区域缺乏系统刻画，对 practitioner 判断何时切换 within-subject matching 至关重要。\n- R1: 原始提出 | R2: 部分 AGREE（\"加分项\"而非\"否决性\"缺陷）\n- **跨轮状态**: R19-W2 再次出现\n- **建议**: 补充 k = 5, 8, 10, 15 的 ΔFPR 数据点\n\n**W10. [Moderate, Consensus] \"近独立于 web-overlap labels\" 的推断强度过高。**\nφ = 0.012 可能反映 web-overlap labels 的 proxy 噪声而非 DIF 的真正独立性。论文已承认此可能性（Section 4.3），并提供 label-independent 支持证据（base-vs-instruct reversal），但 \"complementary diagnostic dimensions\" 措辞仍过强。\n- R1: 原始提出 | R2: AGREE\n- **建议**: 弱化措辞为 \"low correlation with available contamination proxies\"\n\n**W11. [Minor, Consensus] Contribution 3 (audit protocol) 权重不足。**\nSection 5.2 仅半段，无部署验证、case study 或用户研究。作为声明的三大贡献之一显得单薄。\n- R1: AGREE | R2: 原始提出\n- **建议**: 降级为 future direction，或扩展并提供模拟部署场景\n\n---\n\n## Reviewer Consensus\n\n[AGREE] 双方一致同意的关键问题（7 项）：\n1. 标题 \"Score Incomparability\" 与 ρ ≈ 0.997 的叙事不匹配 (W1)\n2. C% 不确定性和 Abstract headline claim 表述 (W2)\n3. Mechanism-agnostic 定位与 contamination 验证的张力 (W4)\n4. Base-vs-instruct 反转的机制解释不足 (W8)\n5. ETS 阈值迁移的实质含义讨论不足 (W6)\n6. Web-overlap labels 推断强度过高 (W10)\n7. Contribution 3 权重不足 (W11)\n\n## Reviewer Divergence\n\n[REBUT/Partial] 存在分歧的问题（4 项）：\n\n1. **方法论新颖性** (W3): R2 认为核心方法为直接搬运（Critical），R1 反驳 cross-subject matching 适配和 semi-synthetic framework 是 non-trivial 的设计创新。分歧未收敛。\n\n2. **2PL power analysis vs IRT misfit** (R1-W3): R2 反驳——MH-DIF 是非参数方法，power analysis 是辅助证据，实证 50× ratio 是核心。R1 接受但建议论文更明确讨论 2PL misfit 影响。**降级为 minor concern。**\n\n3. **多重比较校正** (R1-W6): R2 反驳——DIF 领域标准实践不做 FWER/FDR correction（Wainer 1993），BH 校正仅影响 3/3918 C items (0.08%)。**降级为 minor concern。**\n\n4. **DIF 概念合法性** (W7): R1 部分反驳——DIF 对跨时间群体有效（教育测量先例），Q3 diagnostic 部分缓解多维性。但同意需更多讨论。\n\n---\n\n## Questions\n\n1. Abstract 是否应使用 DEFF 校正后数字（~29% + CI）而非 raw 31%？为何选择 simple-mean 而非 weighted-mean DEFF？\n2. 能否提供 family 定义的敏感性分析以收窄 C% 区间？\n3. 既然 ρ ≈ 0.997，temporal DIF 的 practical impact 是什么？在什么具体场景下 practitioner 会因忽略 temporal DIF 做出错误决策？\n4. DIF 信号是线性积累还是存在突变点？Rolling-window MH-DIF 分析结果如何？\n5. Base-only / instruct-only temporal DIF (Table 15) 为何不在主文展示？\n6. 如果补充非 contamination 来源的 DIF 验证（如训练方法变化模拟），结果如何？\n7. |Δ_MH| = 1.5 对 LLM 的实质含义是什么？能否提供 LLM-specific 阈值校准？\n8. Cross-subject matching 在全局训练方法变化驱动 DIF 时的行为如何？（R1 论证为 conservative bias，不导致 false positive inflation，但可能 under-powered）\n\n---\n\n## Missing References\n\n1. **Rodriguez et al. (2021) \"Evaluation Examples Are Not Equally Informative\" (ACL 2021)** — IRT+NLP 评估的奠基性工作 [R1 AGREE, R2 提出]\n2. **Polo et al. (2024) \"tinyBenchmarks\" (ICML 2024)** — IRT-based 高效 LLM 评估 [R2 提出; R1 部分 REBUT: 技术路线差异大]\n3. **Vania et al. (2021) \"Comparing Test Sets with Item Response Theory\"** — NLP+IRT 早期工作 [R1 提出]\n4. **van der Linden & Veldkamp (2007)** — Item exposure / test security 文献 [R1 提出; R2: nice-to-have]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未配置，不适用。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成。7 个 info 级别发现，0 critical，0 warning：\n\n- **Page 2**: Figure 1 response matrix 彩色小点灰度打印辨识度不足，建议辅以 marker shape 或 hatching\n- **Page 4**: Figure 3 ETS 颜色编码（A=绿, B=黄, C=红）对红绿色盲不友好，建议改用 Okabe-Ito 色板或 blue-orange 方案\n- **Page 5**: Figure 4 x 轴标签字号偏小，部分重叠，建议调整间距或旋转\n- **Page 7**: Figure 6 五个面板 tick/legend 文字偏小（约正文 60-65%），建议增大字号\n- **Page 8**: 右栏内容密度极高（§4.5–4.7 + §5 + §6），无 display item 穿插，但作为 Discussion/Conclusion 区域属正常安排\n- **Page 13**: Tables 6–8 密集排布，单个表格行数少（3-5 行），可考虑合并\n- **Page 14**: Table 10 列头缩写较多，建议 caption 解释\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.5 (Borderline Conference)**\n\n| 维度 | R1 | R2 | 综合 |\n|------|----|----|------|\n| Soundness | 3/5 | 4/5 | 3.5/5 |\n| Excitement | 3.5/5 | 3/5 | 3.0/5 |\n| Reproducibility | 4/5 | — | 4/5 |\n| Confidence | 4/5 | 4/5 | 4/5 |\n\n**综合评判**: 这是一篇执行质量高的大规模实证论文，问题重要且及时，多层次验证设计严谨，cross-subject matching 的 ΔFPR = 0 保证有方法论价值。但存在三个核心障碍阻碍其升至 Conference (4.0)：\n\n1. **叙事过度**: 标题 \"Score Incomparability\" 与 ρ ≈ 0.997 的发现直接矛盾；Abstract 使用未校正的 31% 而非 DEFF 校正后的区间\n2. **方法论新颖性争议**: 核心统计方法均为 30+ 年历史的标准工具，LLM-specific 适配的创新程度在两位 reviewer 间有分歧\n3. **验证框架单一**: 声称 mechanism-agnostic 但验证完全基于 contamination injection\n\n**升至 Conference (4.0) 的路径** (rebuttal 可解决)：\n- (a) 修改标题和 Abstract，使用 DEFF 校正后数字，诚实反映不确定性\n- (b) 在 Introduction 中明确区分 borrowed methodology 与 novel adaptations\n- (c) 补充至少一个非 contamination DIF 机制的验证\n- (d) 讨论 ETS 阈值在 LLM 场景下的 substantive meaning\n- (e) 提供 family 定义敏感性分析以收窄 C% 区间\n- (f) 将 base-only/instruct-only temporal DIF (Table 15) 提升到主文\n\n**作为 Findings 论文** (3.0–3.5): 论文完全达标——规模大、执行扎实、对社区有诊断价值。\n\n---\n\n## Detailed Comments\n\n**Abstract**: 信息密度适中（~150 words，符合 ≤200 words 要求），但 \"31%\" headline 未反映 DEFF 校正后的不确定性。\"near-independent\" 措辞过强。\n\n**Introduction (Section 1)**: Figure 1 pipeline 图信息量大，四步管线清晰。三个 contributions 权重不均：C3 (audit protocol) 后续 Section 5.2 仅半段，缺乏部署验证。\"The result is sobering\" 与 ρ ≈ 0.997 的 aggregate robustness 不一致。\n\n**Related Work (Section 2)**: 组织合理（Psychometric Methods → Contamination Detection → Benchmark Quality）。与 Growing Pains 的区分清晰（nonparametric vs parametric, DIF diagnosis vs score equating）。遗漏 Rodriguez et al. (2021)。\n\n**Method (Section 3)**: MH-DIF 和 ETS 分类的解释清晰，包括公式推导（Eq. 1-2）和四个 LLM-specific challenges 的讨论。Cross-subject matching 的 Remark 论证有说服力。Semi-synthetic injection 的 uniform flipping 局限性在 Limitations 中承认，但 Section 3.4 正文措辞不够 cautious——应在首次提出时标注 \"calibration upper bound\"。\n\n**Experiments (Section 4)**: 多层次控制设计严谨。Section 4.2 的 DEFF 区间处理（\"bracketing C% at 13.5–29.2%\"）不够 transparent——应在主文而非仅附录讨论 estimator 选择。Section 4.3 的 web-overlap 分析有 proxy noise confound。Section 4.2 \"DIF rates are domain-invariant (KW p = 0.78)\" 与 \"DIF direction exhibits domain dependence\" 的并置需更清晰铺垫。\n\n**Discussion (Section 5)**: Section 5.1 的 base-vs-instruct 分析有价值但机制解释不足——需讨论 format sensitivity 作为替代解释。Section 5.2 audit protocol 过于简短。\n\n**Conclusion (Section 6)**: 单句 conclusion 信息量可接受但给人仓促收尾之感。\n\n**Limitations**: 覆盖 3 个关键局限（injection realism, non-independence, cross-subject matching boundary），符合 EMNLP 要求。\n\n**Appendix**: A–Q (17 个) 内容详尽，但数量较多，可考虑合并部分相关性强的 appendix。\n\n**Format**: 正文 8 页内符合限制；Limitations 在第 9 页不计入页数；匿名链接 anonymous.4open.science 格式正确；引用格式符合 ACL 规范。"
  }
}
```

</details>

---


### Tool result

_source line 1786 · 2026-05-25T21:36:43.468018+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_25ed8e3ecef6fc922cb497fae9f34627:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4066
}
```

</details>

---


### Assistant

_source line 1787 · 2026-05-25T21:37:05.135606+00:00_

审稿报告已投递。

**Round 20 审稿完成摘要：**

- **Overall Score: 3.5 (Borderline Conference)**
- **Reviewer 配置**: R1（方法严谨性）3.5 + R2（新颖性/完整性）3.5
- **高度共识**: 标题叙事过度（ρ≈0.997 vs "incomparability"）、C% 不确定性范围过大（13.5%–31.3%）、mechanism-agnostic 与 contamination 验证张力、base/instruct 机制解释不足
- **核心分歧**: 方法论新颖性——R1 认为适配有价值，R2 认为不足以达 conference level
- **升至 4.0 路径**: 修改标题/Abstract、区分 borrowed vs novel methodology、补充非 contamination DIF 验证、讨论 ETS 阈值实质含义、family 定义敏感性分析
- **Issue Tracker**: 12 个 open/in_progress issues（4 critical, 6 warning, 2 info）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---


## Round 176

## Round 176

2 recorded events


### User

_source line 1788 · 2026-05-25T21:37:07.993412+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。对 R1 的 8 个 Weakness 和 7 个 Question 逐条给出了 AGREE/REBUT 判断：

- **AGREE (10 条):** W1、W2、W4、W5、W7、W8、Q1、Q3-Q5、Q7 — 与我自己的审稿高度一致，特别是 C% 不确定性、ETS 阈值迁移合理性、base-vs-instruct 机制解释不足
- **REBUT (3 条):** W3（2PL power analysis 是辅助证据，MH 本身是非参数的）、W6（多重比较校正在 DIF 领域非标准实践，且 BH 校正仅影响 3/3918 items）、Q6（within-subject 验证已有 5 学科覆盖）
- **主要共识:** 标题过度暗示不可比较性（ρ≈0.997）、C% 应报告 DEFF 校正后范围、LLM-specific 阈值校准缺失

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 1789 · 2026-05-25T21:37:30.894127+00:00_

审稿报告已投递至 Research Director。

**Round 20 审稿完成摘要：**

- **Overall Score: 3.5 (Borderline Conference)**
- **Reviewer 配置**: R1（方法严谨性）3.5 / R2（新颖性+完整性）3.5
- **核心共识问题**（7 项 AGREE）：
  1. 标题 "Score Incomparability" 与 ρ≈0.997 叙事矛盾
  2. Abstract 使用未校正 31% 而非 DEFF 校正后区间
  3. Mechanism-agnostic 声称 vs contamination-only 验证
  4. Base-vs-instruct 反转机制解释不足
  5. ETS 阈值迁移缺 substantive meaning 讨论
  6. Web-overlap "near-independent" 推断过强
  7. Contribution 3 (audit protocol) 仅半段无部署验证
- **核心分歧**（1 项未收敛）：方法论新颖性——R2 认为已知技术直接搬运，R1 认为适配创新有价值
- **升至 4.0 路径**：修改标题/Abstract、区分 borrowed vs novel methodology、补充非 contamination DIF 验证、family 定义敏感性分析
- **Issue Tracker 已更新**：12 个 open/in_progress issues（含 3 个 R20 新发现）
- **视觉审查**：7 info，0 critical/warning

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_f025582a920d3f79beb59dfc17929017:director"
}
```

</details>

---
